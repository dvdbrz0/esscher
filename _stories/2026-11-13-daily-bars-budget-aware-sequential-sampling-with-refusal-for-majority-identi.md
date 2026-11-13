---
{
 "layout": "story",
 "title": "BARS: Budget-Aware Sequential Sampling with Refusal for Majority Identification under Unknown Distributions",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/13/daily/",
 "date": "2026-11-13 05:00:00 +0300",
 "summary": "Majority voting over repeated samples is cast as identifying the mode of an unknown answer distribution under a budget and a target error, with a rule that stops early, votes or refuses.",
 "body": [
  "Self-consistency asks a language model the same question several times and returns the most frequent answer. Early-stopping variants save samples when the answers agree, but none gives a sound confidence estimate. The authors formalise the task as majority identification under an unknown distribution, with a sampling budget and a target error rate.",
  "Their rule, BARS, samples sequentially and tries to certify the gap between the two most frequent answers. It returns an early answer, a budgeted majority vote or a refusal when the budget cannot establish the answer. A certified mode carries proven bounds on the joint answering error and on refusing instances the budget could handle; a practical mode replaces these with empirical calibration.",
  "On GSM8K the practical mode draws 22.3% fewer samples than a fixed 8 samples, at the cost of declining 18.8% of questions. On MATH it raises the accuracy of the answers it gives to 82.5% while refusing about half of the hard questions the model cannot solve."
 ],
 "published": "2026-11-10",
 "authors": "Liu et al.",
 "arxiv": "2611.14171",
 "tag": "Reasoning and inference",
 "topics": [
  "Reasoning and inference",
  "Probability"
 ],
 "image": "/assets/og/2026-11-13-daily-bars-budget-aware-sequential-sampling-with-refusal-for-majority-identi.png"
}
---
