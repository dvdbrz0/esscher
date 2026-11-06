---
{
 "layout": "story",
 "title": "Hard to Fool: A Bounded LLM Research Loop for Quantitative Finance, and What Two Dozen Campaigns Found",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/06/daily/",
 "date": "2026-11-06 05:00:00 +0300",
 "summary": "An open-source loop lets a language model propose trading hypotheses while fixed code decides. One survivor with Sharpe ratios near 3 in validation fell to 0.26 on its single holdout use.",
 "body": [
  "Loops that keep whatever improves a metric work well in machine learning, but in trading research they tend to produce false discoveries. This system takes the opposite premise. Proposals are declarative JSON over a fixed vocabulary, evaluation runs on immutable chronological stores split into discovery, validation and a holdout that can be opened once, and acceptance requires a conjunction of absolute gates, including a positive bootstrap lower bound and survival at elevated costs.",
  "Every campaign run so far is reported, across options, ETF rules, prediction-market binaries and alternative data. Most hypotheses fail, and two results survive their pre-registered bars. The author treats a failure as the clearest evidence that the loop works, and argues that its value lies in how hard it is to make it report something that is not there."
 ],
 "published": "2026-11-04",
 "authors": "Zhang",
 "arxiv": "2611.06607",
 "tag": "Quantitative finance",
 "topics": [
  "Quantitative finance",
  "Agents"
 ],
 "image": "/assets/og/2026-11-06-daily-hard-to-fool-a-bounded-llm-research-loop-for-quantitative-finance-and.png"
}
---
