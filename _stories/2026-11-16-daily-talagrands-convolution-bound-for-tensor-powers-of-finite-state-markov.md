---
{
 "layout": "story",
 "title": "Talagrand’s Convolution Bound for Tensor Powers of Finite-State Markov Semigroups",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/16/daily/",
 "date": "2026-11-16 05:00:00 +0300",
 "summary": "Talagrand’s convolution bound, recently proved on the cube \\(\\{-1,1\\}^N\\), is extended to tensor powers of any irreducible Markov semigroup on a finite state space, with a constant independent of the dimension \\(N\\).",
 "body": [
  "Talagrand’s convolution conjecture asks how much the heat semigroup on the discrete cube smooths a nonnegative function: the probability that the smoothed function exceeds \\(\\eta\\) times its mean should be smaller than the bound \\(1/\\eta\\) given by Markov’s inequality, by a factor that grows with \\(\\eta\\). It was proved recently by Lu, Guo and Fang.",
  "Marsh extends their perturbed coupled reverse-heat method to a semigroup \\((S_t)\\) of an irreducible continuous-time Markov chain on a finite set \\(G_0\\) with stationary law \\(\\pi\\). For every \\(\\tau>0\\) there is a constant \\(C\\) such that \\[ \\pi^{\\otimes N}\\Big(S_\\tau^{\\otimes N} f > \\eta \\int f \\, d\\pi^{\\otimes N}\\Big) \\le \\frac{C}{\\eta\\sqrt{\\log \\eta}} \\] for all \\(N\\), all nonnegative \\(f\\) and all \\(\\eta>1\\).",
  "The new difficulty is that a distribution on more than two points is not determined by its mean, so the proof uses explicit terminal bridge laws to keep the bound free of the dimension. The result has been formalised in Lean 4, and the formalisation is public."
 ],
 "published": "2026-11-11",
 "authors": "Marsh",
 "arxiv": "2611.14869",
 "tag": "Probability",
 "topics": [
  "Probability",
  "Mathematics"
 ],
 "math": true,
 "summary_plain": "Talagrand’s convolution bound, recently proved on the cube {−1, 1}ᴺ, is extended to tensor powers of any irreducible Markov semigroup on a finite state space, with a constant independent of the dimension N.",
 "image": "/assets/og/2026-11-16-daily-talagrands-convolution-bound-for-tensor-powers-of-finite-state-markov.png"
}
---
