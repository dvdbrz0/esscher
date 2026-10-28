---
{
 "layout": "story",
 "title": "Frequency-Uniform Log-Regret Reinforcement Learning for Diffusions",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/10/28/daily/",
 "date": "2026-10-28 05:00:00 +0300",
 "summary": "Regret of order \\(O(\\log K)\\) over \\(K\\) episodes for reinforcement learning on Euler discretisations of controlled diffusions, with constants that do not depend on the time step \\(\\delta\\).",
 "body": [
  "High-frequency control problems are usually discretised in time, but refining the step \\(\\delta\\) raises the discrete horizon \\(H = T/\\delta\\), and standard finite-horizon regret bounds degrade even when the physical horizon \\(T\\) is fixed. The paper studies episodic value-based reinforcement learning for Euler discretisations of controlled diffusions, measuring regret against the optimal policy of the Euler model.",
  "Under stability and regularity conditions on value-function gradients, Bellman residual derivatives and fitted critics, the authors prove a regret bound of \\(O(\\log K)\\) after \\(K\\) episodes, uniformly in \\(\\delta\\). For drift linear in unknown parameters and an unknown constant diffusion covariance, they verify these conditions for a constrained model-based fitted-\\(Q\\) algorithm and obtain high-probability regret of \\(O(\\log K \\log\\log K)\\), again uniform in \\(\\delta\\). Continuous-time control problems of this kind are common in portfolio and execution models."
 ],
 "published": "2026-10-27",
 "authors": "Blanchet et al.",
 "arxiv": "2610.36758",
 "tag": "Optimization",
 "topics": [
  "Optimization",
  "Learning theory",
  "Quantitative finance"
 ],
 "math": true,
 "summary_plain": "Regret of order O(log K) over K episodes for reinforcement learning on Euler discretisations of controlled diffusions, with constants that do not depend on the time step δ.",
 "image": "/assets/og/2026-10-28-daily-frequency-uniform-log-regret-reinforcement-learning-for-diffusions.png"
}
---
