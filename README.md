# EdTechIRL

Editorial calendar and full article archive for [EdTechIRL.com](https://www.edtechirl.com) —
a K12 education technology and cybersecurity blog published on Substack by Andy Lombardo.

## Layout

```
content-schedule.md      Editorial calendar: planned and published posts
blog-archive/            Markdown copies of every published article
  index.md               Notes on what the archive is
  YYYY-MM-DD-<slug>.md   One file per article, oldest 2022-03-14
  images/                Every image referenced by the archive, stored locally
tools/
  refresh_archive.py     Pull newly published articles into the archive
```

## The archive

`blog-archive/` holds a self-contained Markdown copy of all **177 published articles**,
spanning 2022-03-14 through 2026-06-14. Each file is named `YYYY-MM-DD-<slug>.md`, where
the slug matches the article's Substack permalink, and opens with YAML frontmatter:

```yaml
---
title: "Cyber Risk is an Equity Issue"
subtitle: "Pt 7: Why Disruptions Hit Some Students Harder Than Others"
date: 2026-04-03
author: Andy Lombardo
source: https://www.edtechirl.com/p/cyber-risk-is-an-equity-issue
---
```

`source` is the canonical URL on edtechirl.com, so any article can be traced back to
the original post.

### Images

Images are stored in `blog-archive/images/` and referenced by relative path, so the
archive renders correctly offline and does not depend on Substack's CDN staying up.
All 955 referenced images are present locally.

Two animated GIFs could not be recovered — they live in a retired Substack storage
bucket that now returns HTTP 403, so those two references still point at the remote
CDN URL. They are likely broken on the live site as well.

## Keeping the archive current

`tools/refresh_archive.py` handles this. It requires [pandoc](https://pandoc.org)
(`brew install pandoc`), needs no API key, and is safe to re-run — it only writes
articles that are missing.

```sh
tools/refresh_archive.py --check      # report what's missing, write nothing
tools/refresh_archive.py              # fetch missing articles + vendor their images
tools/refresh_archive.py --verify 8   # self-test against articles already archived
```

Other flags: `--slug <slug>` force-regenerates specific articles (repeatable), and
`--no-images` skips image vendoring.

### How it works

Each Substack post page embeds a `window._preloads` JSON blob containing the article's
`body_html`. The script pulls that out, strips Substack's UI chrome, converts to Markdown
with pandoc, and post-processes the result to match the conventions above. Missing
articles are found by comparing each local file's `source:` slug against the publication's
archive listing at `/api/v1/archive`.

A few details are load-bearing and easy to regress:

- **Code blocks are removed before pandoc runs and reinserted verbatim afterwards.**
  Substack emits a doubled `<pre><code><code>`, which makes pandoc fall back to indented
  blocks instead of fences, and the later cleanup passes would eat shell line-continuation
  backslashes.
- **`<a>` and `<img>` are reduced to the attributes GFM can express.** A link carrying
  `class`/`target`/`data-*` forces pandoc to emit raw HTML, which the stray-HTML pass then
  deletes — silently dropping the image.
- **The cover image is prepended only if it doesn't already open the body**, since for many
  posts it appears in both places.

### Verifying the converter

Substack changes its markup from time to time. `--verify N` regenerates N articles that are
already archived and reports how many lines differ from the stored copy.

Non-zero counts are not automatically failures — Substack re-renders old posts, and articles
edited after archiving will legitimately differ. What matters is the pattern: drift confined
to older posts is normal, but a **recent** article suddenly differing suggests their markup
changed and the converter needs attention.

## Content calendar

`content-schedule.md` tracks planned and published posts by date, with category
(Tools / Thoughts) and publication status for both the blog and LinkedIn. Statuses were
last reconciled against the archive on 2026-08-07.
