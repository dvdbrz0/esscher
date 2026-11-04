---
{
 "layout": "story",
 "title": "Watch Your Step: Adam’s Margin Maximization Bias Depends on the Learning Rate Schedule",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/04/daily/",
 "date": "2026-11-04 05:00:00 +0300",
 "summary": "For a schedule \\(t^{\\alpha}\\) and homogeneity degree \\(L\\), when \\(\\alpha>\\frac{1}{L}-\\frac{1}{2}\\) Adam has no trajectory-independent margin-maximisation bias on deep linear networks.",
 "body": [
  "Earlier work showed an \\(\\ell_\\infty\\)-margin bias for Adam under strongly decaying schedules. This paper studies the more common regime of constant and weakly decaying rates. For \\(\\alpha>\\frac{1}{L}-\\frac{1}{2}\\) there is no non-trivial, locally Lipschitz, convex implicit regulariser on deep linear networks, including any squared norm.",
  "Adam instead maximises a trajectory-dependent weighted \\(\\ell_2\\) margin, because its preconditioner converges to a trajectory-dependent vector. The limiting direction therefore depends on initialisation. In the intermediate regime \\(\\frac{1}{L}-1\\le\\alpha\\le\\frac{1}{L}-\\frac{1}{2}\\) the authors prove an \\(\\ell_\\infty\\) bias, conditional on gradient directional convergence to a full-support vector."
 ],
 "published": "2026-11-01",
 "authors": "Gronich and Vardi",
 "arxiv": "2611.01929",
 "tag": "Learning theory",
 "topics": [
  "Learning theory",
  "Optimization"
 ],
 "math": true,
 "summary_plain": "For a schedule t^α and homogeneity degree L, when α > 1/L−1/2 Adam has no trajectory-independent margin-maximisation bias on deep linear networks.",
 "image": "/assets/og/2026-11-04-daily-watch-your-step-adams-margin-maximization-bias-depends-on-the-learning.png"
}
---
