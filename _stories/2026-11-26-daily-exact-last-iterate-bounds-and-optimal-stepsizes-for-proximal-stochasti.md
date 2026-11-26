---
{
 "layout": "story",
 "title": "Exact Last-Iterate Bounds and Optimal Stepsizes for Proximal Stochastic Gradient Descent",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/26/daily/",
 "date": "2026-11-26 05:00:00 +0300",
 "summary": "The exact worst-case expected gap of the last iterate of proximal SGD is computed for every predetermined schedule with steps at most \\(3/(2L)\\), and the minimax schedule satisfies \\((D\\sigma/M_T)^2 = T + \\log T + C_\\star + o(1)\\).",
 "body": [
  "Proximal stochastic gradient descent minimises an \\(L\\)-smooth convex function, accessed through unbiased gradients of bounded variance, plus a nonsmooth convex term accessed through its proximity operator. The authors derive the exact worst-case expected objective gap of the last iterate for a broad class of schedules containing all those with stepsizes at most \\(3/(2L)\\), extending a result of Grimmer and Shen for the smooth case. The bound is a sum of an initial-error term and one noise term per iteration, damped by the stepsizes that follow it.",
  "The formula shows that a logarithmic factor is unavoidable with a constant stepsize. For a uniform variance bound \\(\\sigma^2\\), the best schedule is unique and decreasing, and the minimax value after \\(T\\) steps satisfies \\((D\\sigma/M_T)^2 = T + \\log T + C_\\star + o(1)\\) with \\(C_\\star \\approx 1.768\\); unlike the smooth case, \\(L\\) plays no role at this order."
 ],
 "published": "2026-11-24",
 "authors": "Condat and Richtárik",
 "arxiv": "2611.32428",
 "tag": "Optimization",
 "topics": [
  "Optimization",
  "Probability"
 ],
 "math": true,
 "summary_plain": "The exact worst-case expected gap of the last iterate of proximal SGD is computed for every predetermined schedule with steps at most 3/(2L), and the minimax schedule satisfies (Dσ/M_T)² = T+log T+C_⋆+o(1).",
 "image": "/assets/og/2026-11-26-daily-exact-last-iterate-bounds-and-optimal-stepsizes-for-proximal-stochasti.png"
}
---
