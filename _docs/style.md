# Esscher house style

Read this before writing an edition. It keeps every edition sounding like the
same publication. When in doubt, write it the way The Economist or Reuters would.

## Voice

- Plain, precise, calm. State what happened, then why it matters. No hype.
- Lead with the fact, not with the context: "The Fed raised rates to 4%",
  not "In a move that surprised few, the Fed...".
- Short sentences. One idea per sentence. Active voice.
- Never address the reader ("you"), never mention who writes Esscher, never
  write about the newsletter itself.
- No rhetorical questions, no exclamation marks, no jokes in news items.
- Do not pad. If a story is thin, keep it short.

Words and habits to avoid, because they read as filler or as machine-written:
groundbreaking, revolutionary, game-changer, game-changing, unprecedented,
paradigm shift, cutting-edge, state-of-the-art (unless quoting a paper),
landscape, ecosystem (unless literal), delve, dive into, deep dive, unpack,
navigate, leverage (as a verb), harness, unlock, empower, robust (outside
statistics), seamless, crucial, pivotal, vital, notably, importantly,
interestingly, it is worth noting, it remains to be seen, in a significant
move, sent shockwaves, amid (more than once per edition), "not just X but Y",
lists of three adjectives, and sentences built around a colon or a dash for
drama. Use at most one dash-pair aside per story.

Patterns that make text read as machine-written even when every word is fine:

- Inflated significance: "marks a turning point", "a pivotal moment",
  "underscores", "highlights the importance of", "reflects a broader trend".
- Sentences that trail off in a vague participle clause: "..., highlighting
  the risks", "..., reflecting growing concern", "..., signalling a shift".
- Groups of three for rhythm (adjectives, parallel clauses) when the facts do
  not come in threes.
- "Actually", "really", "truly", "Here's", "In short", "The upshot", "The
  takeaway", "It's not X, it's Y", and openings that restate the headline.
- Every item in a section built the same way. Vary length and shape: some
  items are one sentence, some lead with a number, some with a name.

## Spelling and grammar

- British English with -ise endings: optimise, generalisation, randomised,
  organisation, centre, labour, modelling, programme (but "computer program").
- "maths", not "math". "Data" takes a plural or singular verb, be consistent
  within a story.
- Proper names keep their own spelling: "Center for AI Safety",
  "Federal Reserve", "Lean formalization" when quoting a title.
- Paper titles exactly as on arXiv.

## Headlines

- Sentence case: capital only for the first word and proper names.
- Say what happened, with a verb, in present tense: "Fed signals another hike".
- At most about 70 characters. No full stop. At most one colon.
- Digits for all numbers: "722 papers", "3 labs".
- A question headline only when the piece itself is an open question.
- No "BREAKING", no "Here's why", no "everything you need to know".
- The must-read headline states the news as a sentence with a verb. Never
  build it as topic, colon, verdict ("X: the hard part is Y"), the most
  recognisable machine-written headline shape.

## Summaries and three lines

- Summary: one or two sentences, at most 40 words, starting with the news.
- The three lines (five for the weekly) each stand alone, one sentence each,
  and together tell the reader the day in 30 seconds.
- Dek of the must-read: two sentences at most.

## Numbers, money, dates

- Numbers: words for one to nine in running text ("three labs"), digits for
  10 and above; always digits with units, percentages, money, ages, scores.
- Percentages: "5.25%" everywhere. Changes in rates and yields in basis
  points: "up 12 basis points". Changes in percentages as "percentage points".
- Money: "$30bn", "$51m", "€2.5bn", "£400m". "Trillion" as "tn": "$1.2tn".
- Large plain numbers with commas: "7,811.54".
- Dates: "9 October 2026"; with weekday "Tuesday 13 October". No ordinals
  ("13th"). Times in 24-hour UTC: "14:30 UTC".
- Ranges: "8–13%" with an en dash.
- Times stay in UTC in the JSON; the site shows each reader the time in their
  own zone.
- Quotation marks: type plain quotes and apostrophes in the JSON.
  `scripts/new_post.py` turns them into typographer's quotes (“ ” ‘ ’)
  everywhere except inside formulas.

## Names and attribution

- People: full name and role on first mention ("Jerome Powell, chair of the
  Federal Reserve"), surname afterwards. No honorifics.
- Companies by their usual names: "OpenAI", "Anthropic", "Jane Street".
- Abbreviations: write the full name the first time in a story with the short
  form in brackets, then the short form: "European Central Bank (ECB)".
  Exceptions that never need spelling out: AI, US, UK, EU, GDP, IPO, CEO.
- Attribute every claim that is not plainly established: "according to the
  Financial Times", "the company said". Use "said", not "claimed",
  "admitted" or "revealed".
- Unconfirmed claims say so: "not yet independently reviewed",
  "reportedly, according to Bloomberg". Never repeat a rumour without a named
  source.
- Posts by leading figures. A post on X by a leading researcher, founder,
  executive or mathematician is its own source for what that person said, and
  belongs in the edition: under "voices" when it is an argument or an
  observation, as a story when the post itself announces something. Report it
  as their statement, in our own words ("Andrej Karpathy argued that..."), and
  link the post. A factual claim inside the post stays attributed to its
  author ("Altman said the model would ship in November"), never stated as
  established fact. Posts from anonymous or minor accounts, and posts known
  only secondhand without a link, are not sources.
- A voice's headline says what the person argued, with the surname as the
  subject: "Karpathy describes a steep funnel in how people understand AI".
  Its page explains the argument in full, in our own words, and says which
  figures are the author's own estimates.
- Papers: "Hanneke et al." for three or more authors, both surnames for two.

## Markets band

- Figures only from a source read that morning, with the date they refer to
  in "ticker_asof" and the source names in "ticker_source".
- Label the band with the close it shows: "Friday close", "Monday close".

## Chart of the day

- One chart, from data downloaded that morning (for example with
  `scripts/fred.py`) or figures stated in a source. Never estimate a point.
- Title states the finding ("Long-term US yields at their highest since
  2002"); subtitle states exactly what is plotted, frequency and unit
  ("US 10-year Treasury yield, daily close, %").
- The note is two or three sentences with the key numbers and dates, every one
  of them visible in the data.
- Leave the chart out when nothing in the day's news has data worth showing.

## Mathematical notation

- Notation is typeset, never typed: every variable, rate, bound or formula goes
  in LaTeX between `\( \)` (see "Mathematics" in format.md), in summaries and
  the lines of the day as much as in story bodies. "An error of order
  \(\sqrt{d}/N\)", not "an error of order sqrt(d)/N" and not "of order root d
  over N".
- Name a quantity in words the first time, then use its symbol: "the VC
  dimension \(d\)", "the noise level \(s\)".
- Use the notation of the paper being described, with its symbols and its
  conventions.
- Headlines carry no LaTeX: when a headline needs a symbol, use the Unicode
  character (√n, ε, ≤).

## The maths behind the news

- The tone of a good lecture: precise, unhurried, no jokes, no "simply" or
  "obviously". Define every symbol the first time it appears.
- One idea per paragraph; a displayed formula gets a sentence before it saying
  what it is and a sentence after it saying what it means.
- State assumptions explicitly ("for small changes in yield", "if returns are
  independent"). Never present an approximation as exact.

## Corrections

- If a fact published in an earlier edition turns out to be wrong, correct it
  with `scripts/correct.py` and a note in this form:
  "An earlier version of this story said X. It is Y."
- Never change a published fact without a correction. Fixing a typo or a
  broken link needs no correction note.
