---
{
 "layout": "story",
 "title": "Sharp Last-Iterate Bounds for the Stochastic subGradient Method",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/24/daily/",
 "date": "2026-11-24 05:00:00 +0300",
 "summary": "The worst-case expected error of the last iterate of constant-stepsize projected stochastic subgradient descent on convex Lipschitz objectives is pinned down up to universal constants, and it depends on the dimension.",
 "body": [
  "Averaged iterates of the stochastic subgradient method are well understood, but in practice the last iterate is what gets used, and its worst-case behaviour with a constant stepsize has been harder to pin down. The authors give upper and lower bounds on its expected optimisation error that match up to universal constants for every stepsize, horizon, dimension and conditional noise moment of order \\(p \\in [1, \\infty]\\).",
  "With bounded noise and a fixed bound on the initial distance to a minimiser, the best constant stepsize gives an error after \\(n\\) steps of order \\(1/\\sqrt{n}\\) on the line, but \\(\\sqrt{\\log n / (n \\log\\log n)}\\) in every fixed dimension of at least two. The last iterate is therefore strictly worse than the average once the problem leaves one dimension, by a factor that is now known exactly."
 ],
 "published": "2026-11-20",
 "authors": "Beretta et al.",
 "arxiv": "2611.27922",
 "tag": "Optimization",
 "topics": [
  "Optimization",
  "Learning theory"
 ],
 "math": true,
 "image": "/assets/og/2026-11-24-daily-sharp-last-iterate-bounds-for-the-stochastic-subgradient-method.png"
}
---
