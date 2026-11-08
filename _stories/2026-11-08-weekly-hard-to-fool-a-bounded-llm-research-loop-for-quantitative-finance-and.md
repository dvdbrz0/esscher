---
{
 "layout": "story",
 "title": "Hard to Fool: A Bounded LLM Research Loop for Quantitative Finance, and What Two Dozen Campaigns Found",
 "kind": "paper",
 "section": "Papers that became canon",
 "edition": "weekly",
 "edition_url": "/2026/11/08/weekly/",
 "date": "2026-11-08 08:00:00 +0300",
 "summary": "An open-source research loop in which the language model only proposes declarative hypotheses and fixed code decides, on immutable data split into discovery, validation and a holdout that can be opened once. Most hypotheses failed; the clearest success of the design was catching a rule whose Sharpe ratio fell from near 3 to 0.26.",
 "body": [
  "Agentic loops that keep whatever improves a metric work well in machine learning, but in trading research a metric that improves is by default overfit, leaked or a multiple-comparisons artefact. Zhang’s loop, called Autonomous Quant Researcher, restricts proposals to strict JSON over a fixed vocabulary, so no model-written code runs. Acceptance requires every gate to pass: positive net edge after costs, a positive weekly-cluster bootstrap lower bound, survival at higher costs, stability by year and minimum sample sizes. Every proposal, refusal and result goes into a hash-chained, append-only ledger.",
  "The paper reports every campaign run so far, across same-day options, overnight SPX spreads, ETF rules, technical-analysis premises, Kalshi crypto contracts and alternative data. Two results survived their pre-registered bars. The paper became the reference point of the week for practitioners arguing about AI trading agents."
 ],
 "published": "2026-11-04",
 "authors": "Zhang",
 "arxiv": "2611.06607",
 "tag": "Quantitative finance",
 "topics": [
  "Quantitative finance",
  "Agents"
 ],
 "image": "/assets/og/2026-11-08-weekly-hard-to-fool-a-bounded-llm-research-loop-for-quantitative-finance-and.png"
}
---
