# How Esscher runs

A map of the moving parts, for whoever works on the site next. The house style is in
`style.md`; the edition format, charts and corrections are in `format.md`.

## Publishing

- Editions are written as JSON by scheduled runs (weekdays before 05:00 Bucharest time,
  Sundays before 08:00) and turned into pages by `scripts/new_post.py`.
- `scripts/publish.sh "message"` commits `_posts`, `_stories`, `_includes/charts` and
  `assets/og`, then pushes to `main`. GitHub Pages rebuilds the site in about a minute.
- The site is Jekyll 3.10 on GitHub Pages (branch `main`, root folder), custom domain
  in `CNAME`, HTTPS enforced. `future: true` lets an edition dated 05:00 appear as soon
  as it is pushed.

## What each script does

| Script | Purpose |
|---|---|
| `scripts/new_post.py FILE.json` | Validates an edition, writes the post, one page per story, the chart SVG and the share images. Rerunning keeps the first publication time and records an update. |
| `scripts/correct.py STORY --note ... --replace OLD NEW` | Public correction: changes the text, adds a dated note, marks the story in its edition, lists it on /corrections/, redraws the share image if the headline changed. |
| `scripts/chart.py` | Draws the chart of the day (line or bar) as inline SVG styled by `site.css`. |
| `scripts/fred.py SERIES START` | Downloads a FRED series as chart points. |
| `scripts/share_card.py` | Draws the 1200x630 image shown when a page is shared. Fonts in `scripts/fonts/` (SIL Open Font License). Needs Pillow; without it pages use `assets/share.png`. |
| `scripts/newsletter.py POST [--send]` | Builds the newsletter email from an edition and sends it through Buttondown. |
| `scripts/publish.sh MESSAGE` | Commit and push everything an edition produces. |

## Switches in `_config.yml`

| Key | Effect when filled in |
|---|---|
| `contact_email` | Shown in the footer, on /about/ and /privacy/. |
| `newsletter` | Buttondown username. Shows the signup forms and the /subscribe/ page, and lets the newsletter workflow send new editions. |
| `goatcounter` | GoatCounter site code: privacy-friendly visit counts; the privacy page adapts. |
| `google_site_verification`, `bing_site_verification` | Ownership meta tags (not needed when ownership was verified through DNS). |

## GitHub Actions

- `.github/workflows/newsletter.yml`: on a push that adds a new edition in `_posts/`,
  waits two minutes for Pages, then sends it to subscribers through Buttondown (secret
  `BUTTONDOWN_API_KEY`). Does nothing while `newsletter` is empty in `_config.yml`.
  Run it by hand with no input to check the API key; with a post path to resend one edition.
- `.github/workflows/edition-check.yml`: on weekdays at 03:40 UTC and Sundays at 07:30 UTC,
  opens an issue labelled `missing-edition` (GitHub then emails the owner) when the day's
  edition is missing; closes it when the edition is pushed.

## Site features

Daily Brief and Weekly Review pages, a page per story and paper, chart of the day,
markets band with date, source and sparklines, topics (`_data/topics.yml`), archive,
search (`search.json`), The maths behind the news (/maths/), corrections (/corrections/),
About and editorial standards, privacy notice, 404 page, RSS feed, sitemap, structured
data (NewsArticle, WebSite, Organization), per-page share images, dark mode, KaTeX
formulas (self-hosted), self-hosted fonts: Source Serif 4 for headlines and reading text,
Source Sans 3 for interface, Archivo ExtraBold for the wordmark only.

## Known pitfalls

- `text-wrap: pretty` on paragraphs that contain displayed KaTeX formulas crashes
  Chromium. It is only applied to short texts (summaries, deks), never to story bodies.
- A class on the chart `<svg>` must not reuse a chart element class (for example
  `chart-line`), or its stroke is inherited by every label.
- Nothing personal belongs in this repository: it is public.
