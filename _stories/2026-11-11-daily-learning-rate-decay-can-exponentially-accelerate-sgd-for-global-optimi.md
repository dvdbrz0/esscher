---
{
 "layout": "story",
 "title": "Learning Rate Decay Can Exponentially Accelerate SGD for Global Optimization of Nonconvex Functions",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/11/daily/",
 "date": "2026-11-11 05:00:00 +0300",
 "summary": "For a natural class of nonconvex functions, SGD with a decaying learning rate needs exponentially fewer gradient queries to find the global minimum than SGD with any fixed small step size.",
 "body": [
  "Practitioners have long believed that decaying the learning rate helps stochastic gradient descent, but it was not known whether it gives an asymptotic advantage for global nonconvex optimisation. The paper proves that it can, exhibiting a class of functions, which includes many standard nonconvex benchmarks, on which the gap in query complexity is exponential in the small-step regime.",
  "The argument treats annealed SGD as a sampler: decaying the step size performs the associated non-log-concave sampling task in polynomial time. The key tool is a weak Poincaré inequality, which controls mixing where a standard Poincaré constant would be exponentially bad. The authors say it is the first exponential separation shown for learning-rate decay."
 ],
 "published": "2026-11-09",
 "authors": "Ozgul et al.",
 "arxiv": "2611.12769",
 "tag": "Optimization",
 "topics": [
  "Optimization",
  "Probability"
 ],
 "image": "/assets/og/2026-11-11-daily-learning-rate-decay-can-exponentially-accelerate-sgd-for-global-optimi.png"
}
---
