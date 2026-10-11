# How an edition is written

Every edition is a JSON file turned into a post by `scripts/new_post.py`:

    python3 scripts/new_post.py /tmp/brief.json

The script validates the file, unwraps tracking links and writes
`_posts/YYYY-MM-DD-daily.md` or `_posts/YYYY-MM-DD-weekly.md`.
Run it again with the same date to replace an edition.

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
- Optional per item: `"why"`, one sentence on why it matters (shown in a box).

Topics: every story and paper carries `"topics"`, a list of 1 to 3 names taken
exactly from this list (each has its own page on the site):
Learning theory, Probability, Optimization, Reasoning and inference,
Large language models, Agents, AI safety, AI policy, AI industry,
Quantitative finance, Market microstructure, Credit risk, Markets, Economy,
Mathematics. For papers, `"tag"` should also be one of these names. Unknown names
are dropped by the script.

Mathematics: write formulas in LaTeX inside `"body"` (and `"why"` if needed), with
`\( ... \)` for inline formulas and `\[ ... \]` for displayed ones. Remember
that in JSON every backslash is doubled: `"\\(\\sqrt{d \\lambda_{\\max}}\\)"`.
Never use dollar signs for math (prices use them). Keep headlines, summaries and
`"three_lines"` free of LaTeX: they also appear in link previews.

## Daily brief

```json
{
  "edition": "daily",
  "date": "2026-10-12",
  "ticker_label": "Friday close",
  "ticker": [
    {"label": "S&P 500", "value": "7,811.54", "change": "+1.2% wk", "dir": "up"},
    {"label": "US 10Y", "value": "5.25%"}
  ],
  "three_lines": ["...", "...", "..."],
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
  "voices": [{"name": "Yann LeCun", "summary": "...", "url": "https://x.com/..."}],
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
- `voices`, `mathematics`, `papers_note`, `status` are optional.

## Weekly review

```json
{
  "edition": "weekly",
  "date": "2026-10-18",
  "week_of": "12 October 2026",
  "headline": "A short headline for the week",
  "five_lines": ["...", "...", "...", "...", "..."],
  "mattered": [{"headline": "...", "summary": "Two to four sentences, shown on the review page.", "body": ["Paragraphs for the story page."], "sources": [{"name": "...", "url": "https://..."}]}],
  "canon": [{"tag": "...", "title": "...", "authors": "...", "summary": "...", "body": ["..."], "arxiv": "2610.10600"}],
  "read": [{"title": "...", "authors": "...", "why": "...", "prerequisites": "...", "focus": "Sections 2 and 4", "time": "About 2 hours", "arxiv": "..."}],
  "debates": [{"headline": "...", "summary": "...", "body": ["..."], "sources": [{"name": "...", "url": "https://..."}]}],
  "markets": [{"headline": "...", "summary": "...", "body": ["..."], "sources": [...]}],
  "economy": [{"headline": "...", "summary": "...", "body": ["..."], "sources": [...]}],
  "mathematics": [{"headline": "...", "summary": "...", "body": ["..."], "sources": [...]}],
  "watch": [{"date": "Tue 13 Oct", "item": "IMF World Economic Outlook"}]
}
```
