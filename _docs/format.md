# How an edition is written

Read `_docs/style.md` first: it is the house style every edition follows.

Every edition is a JSON file turned into a post by `scripts/new_post.py`:

    python3 scripts/new_post.py /tmp/brief.json

The script validates the file, unwraps tracking links and writes
`_posts/YYYY-MM-DD-daily.md` or `_posts/YYYY-MM-DD-weekly.md`, a page per story
in `_stories/`, and the chart in `_includes/charts/`. It prints every file it
wrote. Run it again with the same date to replace an edition: the original
publication time is kept and the edition is marked as updated.

Then publish with:

    bash scripts/publish.sh "Daily brief YYYY-MM-DD"

which commits the post, the story pages, the chart and the share images, and pushes
(rebasing once if the push is rejected).

A new edition pushed to GitHub is also emailed to newsletter subscribers
automatically (`.github/workflows/newsletter.yml`); a rerun of the same date is
not emailed again.

Write everything in English, in your own words. Every string is plain text
(no HTML, no markdown). Every `url` is a full https link to the original source.

Publication dates: every story and paper may carry `"published"`, the date the
original source was published, exactly as shown on the source page (for a paper,
the date on its arXiv abstract page). Format `YYYY-MM-DD`, or
`YYYY-MM-DDTHH:MM:SSZ` in UTC when the page gives a time. If you did not see the
date on the page, leave the field out: never guess. The time the edition itself
goes online is added by the script automatically.

Story pages: every story and paper should also carry `"body"`, a list of 2 or 3
paragraphs (about 100 to 200 words in total). The script turns each item with a
body into its own page, linked from the headline, where readers get a fuller
picture before deciding to open the original. Rules for `body`:
- Only facts you read in the sources (the article, the paper's abstract and
  introduction, the official announcement). Never fill gaps from guesswork.
- Your own words and your own structure: explain what happened or what was
  shown, the key details and numbers, and the context a mathematically minded
  reader needs. Do not retell the source paragraph by paragraph, and do not quote.
- For a paywalled source, use what is publicly visible and other coverage of the
  same story; if that is too thin, keep the body short rather than invent.
- Optional per item: `"why"`, one sentence on why it matters (shown beside the story).

Topics: every story and paper carries `"topics"`, a list of 1 to 3 names taken
exactly from this list (each has its own page on the site):
Learning theory, Probability, Optimization, Reasoning and inference,
Large language models, Agents, AI safety, AI policy, AI industry,
Quantitative finance, Market microstructure, Credit risk, Markets, Economy,
Mathematics. For papers, `"tag"` should also be one of these names. Unknown names
are dropped by the script.

Mathematics: every piece of mathematical notation is written in LaTeX, everywhere
except headlines: variables, functions, rates, bounds, probabilities and formulas,
in `"summary"`, `"three_lines"`, `"five_lines"`, `"dek"`, `"why"`, `"voices"`,
the chart `"note"` and `"body"`. Use `\( ... \)` inline everywhere and
`\[ ... \]` for displayed formulas, only in `"body"`. Never write mathematics as
plain text (`n^2`, `sqrt(n)`, `O(1/n)`, `eps`, `lambda_max`, `<=`) and never as
Unicode in these fields: `\(n^2\)`, `\(\sqrt{n}\)`, `\(O(1/n)\)`,
`\(\varepsilon\)`, `\(\lambda_{\max}\)`, `\(\le\)`. Plain quantities are not
formulas: percentages, prices, dates and counts stay as text ("5.31%", "$30bn",
"722 papers"). Remember that in JSON
every backslash is doubled: `"\\(\\sqrt{d \\lambda_{\\max}}\\)"`. Never use
dollar signs for math (prices use them).

Headlines and paper titles are shown where nothing can be typeset (page titles,
share images, feeds), so they contain no LaTeX: write the mathematics in them with
Unicode characters (√n, ε², ≤, ℝᵈ, λₘₐₓ). `new_post.py` converts any LaTeX left in
a headline and warns. Link previews, search engines, the feed and the newsletter
get a Unicode version of every formula automatically (`scripts/mathtext.py`).

## Daily brief

```json
{
  "edition": "daily",
  "date": "2026-10-12",
  "ticker_label": "Friday close",
  "ticker_asof": "2026-10-09",
  "ticker_source": "Yahoo Finance, CNBC",
  "ticker": [
    {"label": "S&P 500", "value": "7,811.54", "change": "+1.2% wk", "dir": "up"},
    {"label": "US 10Y", "value": "5.25%"}
  ],
  "three_lines": ["...", "...", "..."],
  "chart": {
    "kind": "line",
    "title": "Long-term US yields at their highest since 2002",
    "subtitle": "US 10-year Treasury yield, daily close, %",
    "unit": "%", "decimals": 2,
    "points": [{"x": "2026-07-01", "y": 4.48}, {"x": "2026-07-02", "y": 4.46}],
    "source": "Board of Governors of the Federal Reserve System, via FRED",
    "source_url": "https://fred.stlouisfed.org/series/DGS10",
    "note": "Two or three sentences with the key numbers and dates.",
    "alt": "One sentence describing the chart for screen readers."
  },
  "must_read": {
    "section": "Mathematics · AI",
    "headline": "...",
    "dek": "One or two sentences.",
    "body": ["Paragraph one.", "Paragraph two.", "Paragraph three."],
    "why": "Why it matters, one sentence.",
    "status": "Partly unconfirmed",
    "links": [{"label": "New Scientist: the announcement", "url": "https://..."}]
  },
  "ai": [
    {"headline": "...", "summary": "One or two sentences.", "body": ["Paragraph one.", "Paragraph two."], "why": "Optional.", "topics": ["AI safety", "Agents"], "published": "2026-10-09", "sources": [{"name": "TechCrunch", "url": "https://..."}]}
  ],
  "voices": [{"name": "Yann LeCun", "role": "chief AI scientist at Meta", "headline": "...", "summary": "One or two sentences.", "body": ["Paragraph one.", "Paragraph two."], "url": "https://x.com/...", "published": "2026-10-11"}],
  "papers_note": "New on arXiv today",
  "papers": [
    {"tag": "Learning theory", "title": "...", "authors": "Hanneke et al.", "summary": "Main result in words.", "body": ["The question.", "The main result in words, and why it matters."], "topics": ["Learning theory", "Reasoning and inference"], "arxiv": "2610.10600", "published": "2026-10-09"}
  ],
  "markets": [{"headline": "...", "summary": "...", "body": ["...", "..."], "sources": [{"name": "...", "url": "https://..."}]}],
  "economy": [{"headline": "...", "summary": "...", "body": ["...", "..."], "sources": [{"name": "...", "url": "https://..."}]}],
  "mathematics": [{"headline": "...", "summary": "...", "body": ["...", "..."], "sources": [{"name": "...", "url": "https://..."}]}]
}
```

- `must_read` is optional: leave it out when nothing qualifies.
- The first item of `ai` is shown largest: put the most important story first.
- `ticker` holds only figures taken from a source; leave out anything you do not have. `dir` is "up" or "down".
  `ticker_asof` is the date the figures refer to (the last close), `ticker_source` names where they come from.
- `chart` is optional; see "Chart of the day" below.
- `voices`, `mathematics`, `papers_note`, `status` are optional.
- `voices` are posts and public statements by leading figures (see "Posts by leading figures"
  in style.md). They appear near the top of the edition, under "What researchers are saying".
  Each needs `name`, `summary` and `url` (the post itself). With a `headline` and a `body` of
  two or three paragraphs, a voice gets its own page, like a story, with the post as its
  source; give every substantive post one. `role` is optional (a few words, no capitals).

## The maths behind the news (weekly)

`maths` is one object: the mathematics underneath one story of the week, explained on its
own page and listed at /maths/. Rules:
- Pick a story from this week's editions whose mechanism is mathematical: a pricing formula,
  a statistical claim, a scaling law, an optimisation result, a probability argument.
- `body`: four to seven paragraphs (about 350 to 600 words). Start from the news, state the
  question, then build the mathematics step by step with the formulas written in LaTeX
  (`\( \)` inline, `\[ \]` displayed), and end with what the mathematics says about the story.
- Only standard, well-established mathematics, stated correctly with its assumptions. If a
  number is used, it comes from a source in `sources`. No speculation dressed as derivation.
- Pitched at a reader comfortable with undergraduate probability and calculus.
- `headline` contains no LaTeX (Unicode mathematics only); `summary` may use inline `\( \)`.

## Chart of the day

`chart` draws one chart in the house style. Two kinds:

- `"kind": "line"` with `"points": [{"x": "YYYY-MM-DD", "y": number}, ...]` for a series over time.
  Get the points from FRED with `python3 scripts/fred.py SERIES_ID START_DATE`, which prints
  the list ready to paste (run `python3 scripts/fred.py` alone for useful series). The source
  is then "Board of Governors of the Federal Reserve System, via FRED" for Treasury yields, or
  the agency named on the series page, with `source_url` `https://fred.stlouisfed.org/series/SERIES_ID`.
- `"kind": "bar"` with `"points": [{"label": "AT&T", "y": -10.2}, ...]` for a comparison of a few
  figures, each one stated in a source you read (put that source in `source` and `source_url`).

`unit` is printed after values ("%", "bp"), `prefix` before them ("$"), `decimals` sets the
rounding. Every figure in `title`, `subtitle` and `note` must be visible in the points.

## Corrections

When a fact in an earlier edition turns out to be wrong:

    python3 scripts/correct.py /stories/STORY-NAME/ --note "An earlier version of this story said X. It is Y." --replace "wrong text" "right text"
    bash scripts/publish.sh "Correction: STORY-NAME"

The note appears at the end of the story, the story is marked "Corrected" in its edition,
and it is listed on the corrections page.

## Weekly review

```json
{
  "edition": "weekly",
  "date": "2026-10-18",
  "week_of": "12 October 2026",
  "headline": "A short headline for the week",
  "five_lines": ["...", "...", "...", "...", "..."],
  "mattered": [{"headline": "...", "summary": "Two to four sentences, shown on the review page.", "body": ["Paragraphs for the story page."], "sources": [{"name": "...", "url": "https://..."}]}],
  "maths": {"headline": "Why a 24-year high in yields hits long bonds hardest", "summary": "Two sentences on the question and the answer.", "body": ["Four to seven paragraphs, with LaTeX where it helps."], "topics": ["Markets", "Mathematics"], "sources": [{"name": "...", "url": "https://..."}]},
  "canon": [{"tag": "...", "title": "...", "authors": "...", "summary": "...", "body": ["..."], "arxiv": "2610.10600"}],
  "read": [{"title": "...", "authors": "...", "why": "...", "prerequisites": "...", "focus": "Sections 2 and 4", "time": "About 2 hours", "arxiv": "..."}],
  "debates": [{"headline": "...", "summary": "...", "body": ["..."], "sources": [{"name": "...", "url": "https://..."}]}],
  "markets": [{"headline": "...", "summary": "...", "body": ["..."], "sources": [...]}],
  "economy": [{"headline": "...", "summary": "...", "body": ["..."], "sources": [...]}],
  "mathematics": [{"headline": "...", "summary": "...", "body": ["..."], "sources": [...]}],
  "watch": [{"date": "Tue 13 Oct", "item": "IMF World Economic Outlook"}]
}
```
