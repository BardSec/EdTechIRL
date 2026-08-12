#!/usr/bin/env python3
"""Refresh blog-archive/ from the live EdTechIRL Substack publication.

Finds articles that are published but not yet archived, converts them to the
archive's Markdown conventions, and vendors their images locally.

    tools/refresh_archive.py --check       # report gaps, write nothing
    tools/refresh_archive.py               # fetch and add anything missing
    tools/refresh_archive.py --verify 8    # self-test against existing articles

Requires pandoc (brew install pandoc). Network access, no API key.

How it works: each Substack post page embeds a `window._preloads` JSON blob that
contains the article's `body_html`. That HTML is cleaned of Substack's UI chrome,
converted with pandoc, and post-processed to match the existing archive style
(fenced code blocks, plain-text captions, no raw HTML, cover image first).
"""
import argparse
import difflib
import glob
import json
import os
import random
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from html import unescape as unescape_html
from urllib.parse import unquote, urlparse

SITE = 'https://www.edtechirl.com'
AUTHOR = 'Andy Lombardo'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVE = os.path.join(ROOT, 'blog-archive')
IMGDIR = os.path.join(ARCHIVE, 'images')
UA = {'User-Agent': 'Mozilla/5.0'}

# Markdown images may carry a title: ![alt](url "title")
LINKED_IMG = re.compile(
    r'\[!\[(?P<alt>[^\]]*)\]\((?P<src>[^)\s]+)(?P<stitle>\s+"[^"]*")?\)\]'
    r'\((?P<href>[^)\s]+)(?P<htitle>\s+"[^"]*")?\)')
BARE_IMG = re.compile(
    r'!\[(?P<alt>[^\]]*)\]\((?P<src>[^)\s]+)(?P<stitle>\s+"[^"]*")?\)')


# --------------------------------------------------------------------------
# fetching
# --------------------------------------------------------------------------

def _get(url, timeout=60):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()


def list_live_posts():
    """Every published post, newest first.

    The archive endpoint's pagination is inconsistent -- a limit of 50 at offset 0
    has been observed returning 23 rows -- so windows are overlapped and results
    deduplicated by post id rather than trusting any single pass.
    """
    seen = {}
    offset, empty_streak = 0, 0
    while offset < 2000 and empty_streak < 2:
        url = f'{SITE}/api/v1/archive?sort=new&limit=50&offset={offset}'
        try:
            rows = json.loads(_get(url, timeout=45))
        except Exception as exc:
            print(f'  ! archive listing failed at offset {offset}: {exc}', file=sys.stderr)
            break
        new = [r for r in rows if r['id'] not in seen]
        for r in rows:
            seen[r['id']] = r
        empty_streak = empty_streak + 1 if not new else 0
        if not rows:
            break
        offset += 20            # deliberate overlap
        time.sleep(0.3)
    return sorted(seen.values(), key=lambda r: r['post_date'])


def fetch_post(slug):
    """Full post record, including body_html, from the page's preload blob."""
    html = _get(f'{SITE}/p/{slug}').decode('utf-8', 'replace')
    m = re.search(r'window\._preloads\s*=\s*JSON\.parse\(', html)
    if not m:
        raise ValueError(f'no _preloads blob on /p/{slug}')
    payload, _ = json.JSONDecoder().raw_decode(html, m.end())
    return json.loads(payload)['post']


# --------------------------------------------------------------------------
# html -> markdown
# --------------------------------------------------------------------------

def _drop_subtree(html, open_re):
    """Remove balanced <tag>...</tag> subtrees whose opening tag matches open_re."""
    while True:
        m = re.search(open_re, html, re.I)
        if not m:
            return html
        tag = re.match(r'<\s*([a-zA-Z0-9]+)', m.group(0)).group(1)
        depth, pos = 1, m.end()
        pat = re.compile(rf'<\s*(/?){tag}\b[^>]*?(/?)>', re.I)
        while depth and pos < len(html):
            t = pat.search(html, pos)
            if not t:
                pos = len(html)
                break
            if t.group(1):
                depth -= 1
            elif not t.group(2):
                depth += 1
            pos = t.end()
        html = html[:m.start()] + html[pos:]


def clean_html(h):
    """Strip Substack's UI chrome and reduce markup to what pandoc renders cleanly."""
    for pat in (r'<div[^>]*class="[^"]*image-link-expand[^"]*"[^>]*>',
                r'<svg\b[^>]*>', r'<button\b[^>]*>',
                r'<div[^>]*class="[^"]*subscription-widget[^"]*"[^>]*>',
                r'<div[^>]*class="[^"]*poll-embed[^"]*"[^>]*>'):
        h = _drop_subtree(h, pat)

    # Substack emits <pre><code><code>; the doubled tag makes pandoc fall back to
    # indented code blocks instead of fences.
    h = re.sub(r'(<pre[^>]*>)\s*(?:<code[^>]*>\s*)+', r'\1<code>', h, flags=re.I)
    h = re.sub(r'(?:\s*</code>)+\s*(</pre>)', r'</code>\1', h, flags=re.I)

    # <picture><source ...><img></picture> -> just the <img>
    h = re.sub(r'<source\b[^>]*>', '', h, flags=re.I)
    h = re.sub(r'</?picture\b[^>]*>', '', h, flags=re.I)

    # Captions become their own plain paragraph (the archive never italicises them).
    h = re.sub(r'<figcaption\b[^>]*>(.*?)</figcaption>', r'<p>\1</p>', h, flags=re.I | re.S)

    # Embedded post / video cards -> a plain link to the target.
    def _card(m):
        seg = m.group(0)
        href = re.search(r'href="([^"]+)"', seg)
        text = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', seg)).strip()
        return f'<p><a href="{href.group(1)}">{text}</a></p>' if href else ''

    h = re.sub(r'<div[^>]*class="[^"]*(?:embedded-post-wrap|native-video-embed)[^"]*"[^>]*>'
               r'.*?</div>\s*</div>', _card, h, flags=re.I | re.S)

    # Drop the decorative wrappers so <a><img> sits at block level for pandoc.
    h = re.sub(r'</?(?:div|figure)\b[^>]*>', '', h, flags=re.I)

    # Reduce <a>/<img> to attributes GFM can express. Anything extra (class, target,
    # data-*) forces pandoc into raw HTML, which the stray-HTML pass below would then
    # delete -- silently losing the image.
    def _a(m):
        href = re.search(r'\shref="([^"]*)"', m.group(0))
        return f'<a href="{href.group(1)}">' if href else '<a>'

    def _img(m):
        src = re.search(r'\ssrc="([^"]*)"', m.group(0))
        alt = re.search(r'\salt="([^"]*)"', m.group(0))
        title = re.search(r'\stitle="([^"]*)"', m.group(0))
        if not src:
            return ''
        out = f'<img src="{src.group(1)}" alt="{alt.group(1) if alt else ""}"'
        if title:
            out += f' title="{title.group(1)}"'
        return out + ' />'

    h = re.sub(r'<a\b[^>]*>', _a, h, flags=re.I)
    h = re.sub(r'<img\b[^>]*?/?>', _img, h, flags=re.I)
    return h


def to_markdown(body_html):
    """Return (markdown_with_code_placeholders, code_blocks).

    Code is pulled out before pandoc runs and reinserted verbatim at the very end,
    so no later cleanup pass can touch it. pandoc renders <pre><code> as an indented
    block (the archive uses ``` fences), and the escape and hard-break passes would
    otherwise corrupt shell line continuations.
    """
    h = clean_html(body_html or '')
    blocks = []

    def _stash(m):
        code = re.sub(r'<[^>]+>', '', m.group(1))   # inline markup inside code is noise
        blocks.append(unescape_html(code).strip('\n'))
        return f'<p>@@CODEBLOCK{len(blocks) - 1}@@</p>'

    h = re.sub(r'<pre\b[^>]*>(.*?)</pre>', _stash, h, flags=re.I | re.S)

    md = subprocess.run(['pandoc', '-f', 'html', '-t', 'gfm', '--wrap=none'],
                        input=h, capture_output=True, text=True, check=True).stdout

    md = re.sub(r'^(\s*)(\d+)\.\s{2,}', r'\1\2. ', md, flags=re.M)    # 1.  -> 1.
    md = re.sub(r'^(\s*)-\s{2,}', r'\1- ', md, flags=re.M)            # -  -> -
    md = re.sub(r'^-{4,}$', '---', md, flags=re.M)                    # long rule -> ---
    md = re.sub(r'\\([#$&~^|>.,:;?])', r'\1', md)                     # pandoc escapes
    md = re.sub(r'<[^>]+>', '', md)                                   # any stray HTML
    # Placeholders left behind by embeds that need a browser to render.
    md = re.sub(r'^Unable to execute JavaScript\.$\n?', '', md, flags=re.M)
    md = re.sub(r'^#*\s*An error occurred\.\s*$\n?', '', md, flags=re.M)
    md = re.sub(r'\n{3,}', '\n\n', md)                                # collapse blank runs
    md = '\n'.join(l.rstrip() for l in md.split('\n'))
    return md.strip() + '\n', blocks


def strip_hard_breaks(md):
    """pandoc renders <br> as a trailing backslash; the archive uses a plain newline.

    Skipped inside fenced code blocks, where a trailing backslash is real content.
    """
    out, fenced = [], False
    for line in md.split('\n'):
        if line.lstrip().startswith('```'):
            fenced = not fenced
        elif not fenced and line.endswith('\\'):
            line = line[:-1].rstrip()
        out.append(line)
    return '\n'.join(out)


def tighten_lists(md):
    """Remove blank lines between consecutive list items (pandoc emits loose lists)."""
    out, lines = [], md.split('\n')
    item = re.compile(r'^\s*(?:\d+\.|[-*])\s')
    for i, line in enumerate(lines):
        if line.strip() == '' and out and item.match(out[-1]):
            nxt = next((l for l in lines[i + 1:] if l.strip() != ''), '')
            if item.match(nxt):
                continue
        out.append(line)
    return '\n'.join(out)


def restore_code(md, blocks):
    return re.sub(r'@@CODEBLOCK(\d+)@@',
                  lambda m: '```\n' + blocks[int(m.group(1))] + '\n```', md)


def image_key(url):
    """Stable identity for an image, independent of CDN transform parameters."""
    u = unquote(url)
    for pat in (r'public/images/([0-9a-fA-F-]{36})', r'(photo-[0-9a-zA-Z]+-[0-9a-zA-Z]+)'):
        m = re.search(pat, u)
        if m:
            return m.group(1)
    return None


def render(post):
    """Full Markdown document for a post, with remote image URLs still in place."""
    title = (post.get('title') or '').strip()
    sub = (post.get('subtitle') or '').strip()
    date = post['post_date'][:10]

    fm = ['---', f'title: "{title}"']
    if sub:
        fm.append(f'subtitle: "{sub}"')
    fm += [f'date: {date}', f'author: {AUTHOR}',
           f'source: {SITE}/p/{post["slug"]}', '---', '']
    head = '\n'.join(fm) + f'\n# {title}\n\n'
    if sub:
        head += f'*{sub}*\n\n'

    body, code_blocks = to_markdown(post.get('body_html'))
    body = restore_code(tighten_lists(strip_hard_breaks(body)), code_blocks)

    # The cover image lives outside body_html, so the archive renders it as the first
    # block -- but for many posts the same image also opens the body, and duplicating
    # it would be wrong.
    cover = (post.get('cover_image') or '').strip()
    if cover:
        key = image_key(cover)
        if not (key and key in unquote(body)):
            thumb = cover.replace(',f_auto', ',w_1456,c_limit,f_auto', 1)
            head += f'[![]({thumb})]({cover})\n\n'

    return head + body


# --------------------------------------------------------------------------
# image vendoring
# --------------------------------------------------------------------------

def local_name(url):
    """Local filename for a remote image, derived from its pre-CDN path."""
    if not url.lower().startswith(('http://', 'https://')):
        return None                      # already vendored
    base = os.path.basename(urlparse(unquote(url.strip()).split('?')[0]).path)
    if not base:
        return None
    base = re.sub(r'[^A-Za-z0-9._-]', '_', base)
    if not re.search(r'\.(png|jpe?g|gif|webp|svg)$', base, re.I):
        base += '.jpg'                   # unsplash serves extensionless URLs
    return base


def _origin_url(cdn_url):
    """The pre-CDN source behind a substackcdn /image/fetch/ URL, if present."""
    if '/fetch/' not in cdn_url:
        return None
    tail = cdn_url.split('/fetch/', 1)[1]
    return unquote(tail.split('/', 1)[1]) if '/' in tail else None


def _download(job):
    url, name = job
    dest = os.path.join(IMGDIR, name)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return url, True
    candidates = [url.strip()]
    origin = _origin_url(url)
    if origin:
        candidates.append(origin)        # some old CDN URLs 400; the origin may still serve
    for cand in candidates:
        for attempt in range(3):
            try:
                data = _get(cand)
                if not data:
                    raise ValueError('empty body')
                with open(dest, 'wb') as fh:
                    fh.write(data)
                return url, True
            except Exception:
                if attempt == 2:
                    break
    return url, False


def vendor_images(verbose=True):
    """Download every remote image the archive references and localise the links."""
    os.makedirs(IMGDIR, exist_ok=True)

    mapping = {}
    for path in glob.glob(os.path.join(ARCHIVE, '[0-9]*.md')):
        text = open(path, encoding='utf-8').read()
        for m in LINKED_IMG.finditer(text):
            for u in (m.group('src'), m.group('href')):
                n = local_name(u)
                if n:
                    mapping[u] = n
        for m in BARE_IMG.finditer(text):
            n = local_name(m.group('src'))
            if n:
                mapping[m.group('src')] = n

    if not mapping:
        if verbose:
            print('images: nothing remote to vendor')
        return 0, []

    first = {}
    for url, name in mapping.items():
        first.setdefault(name, url)
    jobs = [(u, n) for n, u in first.items()]
    if verbose:
        print(f'images: {len(mapping)} remote refs -> {len(jobs)} files to fetch')

    ok, bad = set(), set()
    with ThreadPoolExecutor(max_workers=8) as ex:
        for url, good in ex.map(_download, jobs):
            (ok if good else bad).add(mapping[url])

    def repl_linked(m):
        s, h = mapping.get(m.group('src')), mapping.get(m.group('href'))
        if s in ok and h in ok:
            st, ht = m.group('stitle') or '', m.group('htitle') or ''
            return f'[![{m.group("alt")}](images/{s}{st})](images/{h}{ht})'
        return m.group(0)

    def repl_bare(m):
        s = mapping.get(m.group('src'))
        if s not in ok:
            return m.group(0)
        return f'![{m.group("alt")}](images/{s}{m.group("stitle") or ""})'

    changed = 0
    for path in glob.glob(os.path.join(ARCHIVE, '[0-9]*.md')):
        text = open(path, encoding='utf-8').read()
        new = BARE_IMG.sub(repl_bare, LINKED_IMG.sub(repl_linked, text))
        if new != text:
            open(path, 'w', encoding='utf-8').write(new)
            changed += 1

    if verbose:
        print(f'images: {len(ok)} downloaded, {len(bad)} failed, {changed} articles updated')
        for name in sorted(bad):
            print(f'  ! unrecoverable: {name}')
    return len(ok), sorted(bad)


# --------------------------------------------------------------------------
# archive state
# --------------------------------------------------------------------------

def archived_slugs():
    """slug -> path, read from each article's canonical `source:` field."""
    out = {}
    for path in glob.glob(os.path.join(ARCHIVE, '[0-9]*.md')):
        with open(path, encoding='utf-8') as fh:
            head = fh.read(1024)         # frontmatter only
        m = re.search(r'^source:\s*\S+/p/(\S+)\s*$', head, re.M)
        if m:
            out[m.group(1)] = path
        else:
            print(f'  ! no source: field in {os.path.basename(path)}', file=sys.stderr)
    return out


def write_post(post):
    path = os.path.join(ARCHIVE, f'{post["post_date"][:10]}-{post["slug"]}.md')
    open(path, 'w', encoding='utf-8').write(render(post))
    return path


# --------------------------------------------------------------------------
# commands
# --------------------------------------------------------------------------

def cmd_check(live, have):
    missing = [p for p in live if p['slug'] not in have]
    extra = sorted(set(have) - {p['slug'] for p in live})
    print(f'live: {len(live)}   archived: {len(have)}   missing: {len(missing)}')
    for p in missing:
        print(f"  + {p['post_date'][:10]}  {p['title']}")
    for s in extra:
        print(f'  ? archived but not listed live: {s}')
    return missing


def cmd_verify(count):
    """Regenerate already-archived posts and diff, to catch upstream markup changes.

    Image links in the archive are local, so the freshly rendered remote URLs are
    mapped through local_name() before comparing.
    """
    have = archived_slugs()
    slugs = sorted(have)
    random.seed(0)
    sample = random.sample(slugs, min(count, len(slugs)))
    worst = []
    for slug in sample:
        try:
            fresh = render(fetch_post(slug))
        except Exception as exc:
            print(f'  ! {slug}: {exc}')
            continue

        def _localise(m):
            s, h = local_name(m.group('src')), local_name(m.group('href'))
            if s and h:
                return (f'[![{m.group("alt")}](images/{s}{m.group("stitle") or ""})'
                        f'](images/{h}{m.group("htitle") or ""})')
            return m.group(0)

        fresh = LINKED_IMG.sub(_localise, fresh)
        fresh = BARE_IMG.sub(
            lambda m: (f'![{m.group("alt")}](images/{local_name(m.group("src"))}'
                       f'{m.group("stitle") or ""})') if local_name(m.group('src')) else m.group(0),
            fresh)

        current = open(have[slug], encoding='utf-8').read()
        a = [l.rstrip() for l in current.strip().split('\n')]
        b = [l.rstrip() for l in fresh.strip().split('\n')]
        delta = sum(1 for line in difflib.unified_diff(a, b, n=0)
                    if line[:1] in '+-' and not line.startswith(('---', '+++')))
        worst.append((delta, os.path.basename(have[slug])))
        time.sleep(0.4)

    worst.sort(reverse=True)
    exact = sum(1 for d, _ in worst if d == 0)
    for d, name in worst:
        if d:
            print(f'  {d:>5} differing lines  {name}')
    print(f'\nverify: {exact}/{len(worst)} byte-identical')
    print('Non-zero counts are not necessarily failures -- Substack re-renders old posts.\n'
          'Investigate if a recent post drifts, which suggests their markup changed.')
    return 0 if exact else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true', help='report gaps, write nothing')
    ap.add_argument('--verify', type=int, metavar='N', nargs='?', const=8,
                    help='regenerate N archived posts and diff (self-test)')
    ap.add_argument('--slug', action='append', help='force (re)generate a specific slug')
    ap.add_argument('--no-images', action='store_true', help='skip image vendoring')
    args = ap.parse_args()

    if not shutil_which('pandoc'):
        sys.exit('pandoc not found. Install it: brew install pandoc')
    os.makedirs(ARCHIVE, exist_ok=True)

    if args.verify is not None:
        return cmd_verify(args.verify)

    have = archived_slugs()

    if args.slug:
        targets = []
        for s in args.slug:
            try:
                targets.append(fetch_post(s))
            except Exception as exc:
                print(f'  ! {s}: {exc}', file=sys.stderr)
    else:
        print('listing live posts...')
        live = list_live_posts()
        missing = cmd_check(live, have)
        if args.check:
            return 0
        if not missing:
            if not args.no_images:
                vendor_images()
            return 0
        targets = []
        for row in missing:
            try:
                targets.append(fetch_post(row['slug']))
            except Exception as exc:
                print(f"  ! {row['slug']}: {exc}", file=sys.stderr)
            time.sleep(0.6)

    for post in targets:
        path = write_post(post)
        print(f'  wrote {os.path.basename(path)}')

    if not args.no_images:
        vendor_images()

    print(f'\narchive: {len(glob.glob(os.path.join(ARCHIVE, "[0-9]*.md")))} articles')
    return 0


def shutil_which(prog):
    from shutil import which
    return which(prog)


if __name__ == '__main__':
    sys.exit(main())
