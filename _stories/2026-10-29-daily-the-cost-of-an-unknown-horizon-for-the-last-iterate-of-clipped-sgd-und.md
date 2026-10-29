---
{
 "layout": "story",
 "title": "The Cost of an Unknown Horizon for the Last Iterate of Clipped SGD under Heavy-Tailed Noise",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/10/29/daily/",
 "date": "2026-10-29 05:00:00 +0300",
 "summary": "Without a known horizon, the best time-uniform rate for the last iterate of clipped SGD under heavy-tailed noise is \\(\\tilde O(t^{-\\beta_p})\\) with \\(\\beta_p = 2(p-1)/(3p-1)\\), strictly worse than the known-horizon rate.",
 "body": [
  "Training is usually stopped at a time that depends on the data, so a useful guarantee for the last iterate must hold at every time at once. The authors study clipped stochastic gradient descent on smooth convex objectives when the gradient noise has a bounded central moment of order \\(p\\), with \\(1 < p \\le 2\\).",
  "They show that a schedule needing neither the horizon nor a confidence level attains \\(\\tilde O(t^{-\\beta_p})\\) at all times, also almost surely, where \\(\\beta_p = 2(p-1)/(3p-1)\\), and that no rule stepping along the stochastic gradient at the current iterate can do better, even with adaptive steps and thresholds. With a known horizon \\(T\\) the optimal rate is \\(O(T^{-\\alpha_p})\\) with \\(\\alpha_p = (p-1)/p\\); under finite variance the three exponents are \\(1/2\\), \\(2/5\\) and \\(1/3\\), the last being the previous best time-uniform rate.",
  "The result settles a conjecture from ICLR 2026 negatively for the unknown-horizon case. Querying gradients at the running average recovers \\(\\tilde O(t^{-\\alpha_p})\\) at all times, while heavy-ball momentum with geometric forgetting cannot beat \\(\\beta_p\\)."
 ],
 "published": "2026-10-24",
 "authors": "Peng et al.",
 "arxiv": "2610.33381",
 "tag": "Optimization",
 "topics": [
  "Optimization",
  "Learning theory"
 ],
 "math": true,
 "summary_plain": "Without a known horizon, the best time-uniform rate for the last iterate of clipped SGD under heavy-tailed noise is Õ(t^(−βₚ)) with βₚ = 2(p−1)/(3p−1), strictly worse than the known-horizon rate.",
 "image": "/assets/og/2026-10-29-daily-the-cost-of-an-unknown-horizon-for-the-last-iterate-of-clipped-sgd-und.png"
}
---
