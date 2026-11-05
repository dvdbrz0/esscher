---
{
 "layout": "story",
 "title": "How Risky Is Your Data-Driven Policy?",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/05/daily/",
 "date": "2026-11-05 05:00:00 +0300",
 "summary": "Regret in conditional value-at-risk splits into post-sample regret and a sample-risk premium. Sample average approximation learns at \\(n^{-1/2}\\), yet its combined regret is of order \\(n^{-1}\\) or \\(n^{-1/2}\\), depending on the tail.",
 "body": [
  "The paper evaluates a policy by the conditional value-at-risk of its loss over the training sample, any randomisation and the future outcome. Regret against an oracle then decomposes into expected post-sample regret and a sample-risk premium, the tail risk lost by averaging. Under expected loss this premium vanishes.",
  "For losses with a continuous density near the tail cutoff, both parts can decay at the same rate, yet their limiting ratio can reach the thousands. When a probability mass at the cutoff moves with the action, the premium can decay more slowly and dominate. The authors give conditions under which sample average approximation learns the oracle action at rate \\(n^{-1/2}\\), with combined-risk regret of order \\(n^{-1}\\) in the first case and \\(n^{-1/2}\\) in the second."
 ],
 "published": "2026-11-03",
 "authors": "Besbes and Rieger",
 "arxiv": "2611.04292",
 "tag": "Learning theory",
 "topics": [
  "Learning theory",
  "Optimization",
  "Credit risk"
 ],
 "math": true,
 "summary_plain": "Regret in conditional value-at-risk splits into post-sample regret and a sample-risk premium. Sample average approximation learns at n^(−1/2), yet its combined regret is of order n⁻¹ or n^(−1/2), depending on the tail.",
 "image": "/assets/og/2026-11-05-daily-how-risky-is-your-data-driven-policy.png"
}
---
