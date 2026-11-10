---
{
 "layout": "story",
 "title": "Where Should Learning Live? Regret Analysis for Text, Parameter, and Joint Adaptation",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/10/daily/",
 "date": "2026-11-10 05:00:00 +0300",
 "summary": "Choosing prompts and adapters repeatedly during deployment has an excess loss that splits into selection regret, family restriction and deployment history; limiting switches gives sublinear regret.",
 "body": [
  "Deployed language-model systems can switch between prompts and parameter adapters using feedback, and each choice can change the context inherited by later ones. The authors compare cumulative loss with the best fixed prompt and adapter pair, and split the excess into three terms: regret of selection within the candidate family, the cost of restricting that family, and the benefit or harm of the actual deployment history.",
  "When losses are fixed independently of the selector’s randomness, past choices matter for only a bounded number of rounds and each candidate’s own-history loss is observed, limiting the number of switches yields sublinear expected regret. In experiments with Qwen3.5-9B on the Spider benchmark, text-only selection had lower within-family regret than joint selection but more failures, because its family excluded stronger configurations."
 ],
 "published": "2026-11-06",
 "authors": "Kim et al.",
 "arxiv": "2611.09701",
 "tag": "Reasoning and inference",
 "topics": [
  "Reasoning and inference",
  "Learning theory"
 ],
 "image": "/assets/og/2026-11-10-daily-where-should-learning-live-regret-analysis-for-text-parameter-and-join.png"
}
---
