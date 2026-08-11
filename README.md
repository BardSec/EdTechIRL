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

The archive is built from Substack's public post data. For each article, the post page
embeds a `window._preloads` JSON blob containing `body_html`; that HTML is converted to
Markdown with [pandoc](https://pandoc.org) and cleaned up to match the conventions above
(fenced code blocks, plain-text captions, no raw HTML, cover image as the first block).

To find articles that are on the site but not yet archived, compare the slugs in each
file's `source:` field against the publication's archive listing:

```
https://www.edtechirl.com/api/v1/archive?sort=new&limit=50&offset=0
```

Note that this endpoint's pagination is inconsistent — overlap the offset windows and
deduplicate by post `id` rather than trusting a single pass.

## Content calendar

`content-schedule.md` tracks planned and published posts by date, with category
(Tools / Thoughts) and publication status for both the blog and LinkedIn. Statuses were
last reconciled against the archive on 2026-08-07.
