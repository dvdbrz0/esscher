---
{
 "layout": "story",
 "title": "A Shadow Sequence Technique for Last-Iterate Convergence Analysis of the Random Reshuffling Method: Relaxed Stepsize Conditions and Beyond",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/10/23/daily/",
 "date": "2026-10-23 05:00:00 +0300",
 "summary": "Last-iterate rates for random reshuffling with any non-increasing stepsizes \\(\\eta_k\\) and \\(\\eta_1 \\lesssim 1/(\\mathrm{polylog}(n) L)\\), relaxing the usual \\(\\eta \\lesssim 1/(nL)\\).",
 "body": [
  "Random reshuffling, in which stochastic gradient descent passes through the \\(n\\) components of a finite sum in a fresh random order each epoch, is what practitioners run, but its last iterate has been hard to analyse. For smooth convex problems Liu, Guo and Han prove a last-iterate rate of order \\(\\widetilde{O}\\big(\\|x_1^1 - x_*\\|^2 / (n \\sum_k \\eta_k) + \\sigma_*^2 \\sum_k \\eta_k^2 / \\sum_{l \\ge k} \\eta_l\\big)\\), where \\(\\sigma_*^2\\) is the gradient variance at the solution, for any non-increasing stepsizes with \\(\\eta_1 \\lesssim 1/(\\mathrm{polylog}(n) L)\\).",
  "A second rate, with \\(n \\sigma_*^2 \\sum_k \\eta_k^3 / \\sum_{l \\ge k} \\eta_l\\) in place of the variance term, was previously known only for a constant stepsize \\(\\eta \\lesssim 1/(nL)\\). The proof rests on a shadow sequence that shares the epoch endpoints of the iterates and can be read as inexact reshuffling on an interpolated problem, a device the authors expect to carry over to other shuffling methods."
 ],
 "published": "2026-10-21",
 "authors": "Liu et al.",
 "arxiv": "2610.29166",
 "tag": "Optimization",
 "topics": [
  "Optimization",
  "Learning theory"
 ],
 "math": true,
 "summary_plain": "Last-iterate rates for random reshuffling with any non-increasing stepsizes ηₖ and η₁ ≲ 1/(polylog(n)L), relaxing the usual η ≲ 1/(nL).",
 "image": "/assets/og/2026-10-23-daily-a-shadow-sequence-technique-for-last-iterate-convergence-analysis-of-t.png"
}
---
