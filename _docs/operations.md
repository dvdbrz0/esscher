# How Esscher runs

A map of the moving parts, for whoever works on the site next. The house style is in
`style.md`; the edition format, charts and corrections are in `format.md`.

## Publishing

- Editions are written as JSON by scheduled runs (weekdays before 05:00 Bucharest time,
  Sundays before 08:00) and turned into pages by `scripts/new_post.py`.
- `scripts/publish.sh "message"` commits `_posts`, `_stories`, `_includes/charts` and
  `assets/og`, then pushes to `main`. GitHub Pages rebuilds the site in about a minute.
- After publishing, the scheduled run calls `scripts/check_live.py`, looks at its
  screenshots and emails the owner a one-line status (subject "Esscher status - <date> -
  OK" or "- PROBLEMA"). The check only reads; it never fixes or pushes anything.
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
| `scripts/share_card.py` | Draws the 1200x630 image shown when a page is shared. Fonts in `scripts/fonts/` (SIL Open Font License). The wordmark comes from `scripts/brand/wordmark-white.png`. Needs Pillow; without it pages use `assets/share.png`. |
| `scripts/brand.py` | Redraws the wordmark, the mark and `assets/favicon.svg` from Newsreader (`scripts/fonts/`). Only needed if the brand changes; needs fonttools and uharfbuzz. The PNG icons and `scripts/brand/wordmark-white.png` are rendered from those SVGs. |
| `scripts/typography.py` | Typographer's quotes for edition text, used by `new_post.py` and `correct.py`; formulas are left alone. Run it on its own to test it. |
| `scripts/newsletter.py POST [--send]` | Builds the newsletter email from an edition and sends it through Buttondown. |
| `scripts/publish.sh MESSAGE` | Commit and push everything an edition produces. |
| `scripts/check_live.py [DATE] [daily\|weekly]` | After a publish: waits for Pages to serve the edition (up to 15 minutes, cache-busted requests), then checks that the front page links to it, every new story page answers and shows its headline and is listed on the edition, share images and the chart are served, the publish commit deleted nothing, the sitemap lists every page and the previous edition still answers. In Chromium (Playwright) it opens the front page, the edition and one story at 390 and 1440 pixels, light and dark, and reports JavaScript errors, failed requests, sideways scrolling, broken images, raw LaTeX, formula errors, unloaded fonts and empty sections; screenshots go to `/tmp/esscher-check/`. Last line: `SUMMARY: OK ...` or `SUMMARY: PROBLEM ...`; exit code 0, 1 (problems) or 2 (edition never appeared). |
| `scripts/live_markets.py [--check]` | Fetches delayed quotes for the markets band (CNBC, then Yahoo Finance) and writes `live.json` when a quote changed. Instruments, symbols and quote links are in `_data/markets.json`. |

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
- `.github/workflows/markets.yml`: on weekdays every 15 minutes from 13:07 to 21:52 UTC,
  and hourly from 06:11 to 12:11 UTC, runs `scripts/live_markets.py` and commits
  `live.json` when a quote changed. Run it by hand with "check" to see what each source
  returns without changing anything.
- `.github/workflows/edition-check.yml`: on weekdays at 03:40 UTC and Sundays at 07:30 UTC,
  opens an issue labelled `missing-edition` (GitHub then emails the owner) when the day's
  edition is missing; closes it when the edition is pushed.

## Site features

Daily Brief and Weekly Review pages, a page per story and paper, chart of the day,
markets band with date, source, sparklines, a link from each figure to its full quote, and
delayed quotes from `live.json` on the front page and the latest edition (`assets/js/live-markets.js`;
used only when newer than the edition's close, so the edition's figures stay as the record), topics (`_data/topics.yml`), archive,
search (`search.json`), The maths behind the news (/maths/), corrections (/corrections/),
About and editorial standards, privacy notice, 404 page, RSS feed, sitemap, structured
data (NewsArticle, WebSite, Organization), per-page share images, dark mode, KaTeX
formulas (self-hosted), self-hosted fonts: Newsreader for headlines (the face the wordmark
is drawn from), Source Serif 4 for reading text, Source Sans 3 for interface. Accent colour
#1D4F91 (ink blue; #8AB4F8 in dark mode), used for labels, links and charts.

Times are written in UTC in the page; `assets/js/local-time.js` shows them in the
reader's own time zone (the UTC text stays for readers without scripts).

Masthead: one compact row (drawn wordmark, sections, search; a Menu on phones) above a
thin row with the date, the edition number ("No. N", counted from the first daily
edition) and the markets band, which scrolls sideways when it does not fit. The
wordmark is "Esscher" in Newsreader (display size, weight 700) drawn as outlines with
the two s joined, kept in `_includes/brand/wordmark.svg` and inlined so it follows the
text colour in dark mode. `_includes/brand/mark.svg` is a density and its Esscher tilt,
kept for small uses such as an end mark.

## Known pitfalls

- `text-wrap: pretty` on paragraphs that contain displayed KaTeX formulas crashes
  Chromium. It is only applied to short texts (summaries, deks), never to story bodies.
- A class on the chart `<svg>` must not reuse a chart element class (for example
  `chart-line`), or its stroke is inherited by every label.
- Nothing personal belongs in this repository: it is public.
