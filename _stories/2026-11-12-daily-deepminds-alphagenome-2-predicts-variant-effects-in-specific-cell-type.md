---
{
 "layout": "story",
 "title": "DeepMind’s AlphaGenome 2 predicts variant effects in specific cell types",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/11/12/daily/",
 "date": "2026-11-12 05:00:00 +0300",
 "summary": "Google DeepMind released AlphaGenome 2, a model trained on more than 100 million single-cell profiles that predicts how DNA variants change gene activity in a chosen cell type or state.",
 "body": [
  "The first AlphaGenome took a million-letter DNA sequence and predicted thousands of molecular readouts across bulk tissues in parallel. AlphaGenome 2 is a conditional model: it takes the sequence together with one biological condition, a tissue, cell type or cell state, and feeds that condition into every stage of the network. DeepMind says this lets it learn how the same stretch of DNA is read differently in closely related cells. It was trained on human and mouse data including more than 107 million individual cell profiles, and adds DNA methylation to the readouts the first model covered.",
  "On TenK10K, a single-cell map of 28 immune cell types, the model identified 30% of causal variants against 16% for a fine-tuned version of the original, and 43% of directional gene effects against 23%. It can also be conditioned on a new single-cell experiment of a few dozen cells without retraining, which DeepMind used to show that a variant linked to severe COVID-19 matters more in vaccine-activated T cells than in resting ones.",
  "The model is available for non-commercial research through the AlphaGenome API, and in private preview for commercial use."
 ],
 "why": "Most disease-linked variants act through gene regulation in particular cells, which tissue-average models cannot see.",
 "sources": [
  {
   "name": "Google DeepMind",
   "url": "https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/"
  },
  {
   "name": "Discussion on X",
   "url": "https://x.com/demishassabis/status/2120565316619284734"
  }
 ],
 "published": "2026-11-11",
 "topics": [
  "AI industry"
 ],
 "image": "/assets/og/2026-11-12-daily-deepminds-alphagenome-2-predicts-variant-effects-in-specific-cell-type.png"
}
---
