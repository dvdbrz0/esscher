---
{
 "layout": "story",
 "title": "Where Is the Truth When AI Agents Disagree? Dependence-Aware Belief Propagation for Unsupervised Truth Discovery (Extended Version)",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/05/daily/",
 "date": "2026-11-05 05:00:00 +0300",
 "summary": "BP-TD discounts agents built on the same base model, so that they count as about one vote. On MMLU it beats majority vote without labels, 0.716 to 0.624 on 160 questions.",
 "body": [
  "Many deployed agents are variants of one base model, so their errors are correlated. Classical truth-discovery estimators then reward the agreeing bloc and can fall below majority vote. BP-TD adds per-agent decorrelation weights to mean-field variational inference on a one-coin Dawid-Skene model. Its first iteration is exactly a weighted vote.",
  "With 13 local agents it also ranks agents by their true accuracy. The gain depends on the pool. Over 2,852 sub-pools, decorrelation helps when the largest correlated bloc is weaker than the other agents and hurts when it is the strongest, and the author found no label-free statistic that separates the two cases. With 20 labelled questions, selecting the single best agent beat every aggregator tested."
 ],
 "published": "2026-11-03",
 "authors": "Berti-Equille",
 "arxiv": "2611.04805",
 "tag": "Reasoning and inference",
 "topics": [
  "Reasoning and inference",
  "Agents"
 ],
 "image": "/assets/og/2026-11-05-daily-where-is-the-truth-when-ai-agents-disagree-dependence-aware-belief-pro.png"
}
---
