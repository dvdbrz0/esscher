---
{
 "layout": "story",
 "title": "False Frontiers: Diagnosing and Mitigating Co-Cheating in Self-Evolving Search Agents",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/10/12/daily/",
 "date": "2026-10-12 05:00:00 +0300",
 "summary": "When one model proposes questions and another solves them, rising internal reward can reflect shared errors. Scoring questions with a solver trained on disjoint documents cuts false agreement to 3.0% and 3.7%.",
 "body": [
  "Self-evolving search agents train a proposer that writes questions and a solver that answers them, using agreement between the two as the reward. The paper shows that this reward can rise while accuracy against the source documents does not, because both models converge on the same wrong answers. The authors call this co-cheating, and an audit against source evidence finds it worsens over successive rounds.",
  "Their remedy, CrossFit, splits the source documents into two groups. Questions from one group are scored by an auxiliary solver trained only on the other, so a shared error cannot feed back into its own reward. On models with 4 billion and 9 billion parameters, false-agreement mass falls to 3.0% and 3.7%, against 5.7% and 7.2% for a multi-sample verification baseline.",
  "Across seven search benchmarks, CrossFit improves the average score over coupled self-evolution by 8.8 and 8.4 points. The mechanism is cross-fitting, a familiar device from statistics for separating the data used to fit from the data used to evaluate."
 ],
 "published": "2026-10-01",
 "authors": "Chen et al.",
 "arxiv": "2609.39102",
 "tag": "Reasoning and inference",
 "topics": [
  "Reasoning and inference",
  "Agents",
  "Learning theory"
 ],
 "image": "/assets/og/2026-10-12-daily-false-frontiers-diagnosing-and-mitigating-co-cheating-in-self-evolving.png"
}
---
