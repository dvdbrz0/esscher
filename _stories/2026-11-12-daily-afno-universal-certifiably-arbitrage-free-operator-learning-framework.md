---
{
 "layout": "story",
 "title": "AFNO: Universal Certifiably-Arbitrage-Free Operator Learning Framework for European Call-Price Surfaces",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/12/daily/",
 "date": "2026-11-12 05:00:00 +0300",
 "summary": "A neural operator that maps market or model features to call-price surfaces guaranteed free of static arbitrage, with a proof that arbitrage cannot in general be removed by post-processing.",
 "body": [
  "Neural operators can produce option-price surfaces quickly once trained, but standard architectures carry no guarantee of static no-arbitrage, and the authors show experimentally that violations can produce losses in downstream trading. They also prove that a nearest arbitrage-free correction of an unconstrained surface need not exist, so the property cannot generally be restored after the fact, and that common architectures such as the Fourier neural operator admit parameters whose outputs violate it.",
  "Their framework maps inputs from a reproducing kernel Hilbert space to a convex combination of arbitrage-free European call-price surfaces by continuously solving an approximate nearest-neighbour problem, and is universal in the approximation sense. Hans Buehler, known for work on deep hedging, is among the authors."
 ],
 "published": "2026-10-13",
 "authors": "Kratsios et al.",
 "arxiv": "2611.12899",
 "tag": "Quantitative finance",
 "topics": [
  "Quantitative finance"
 ],
 "image": "/assets/og/2026-11-12-daily-afno-universal-certifiably-arbitrage-free-operator-learning-framework.png"
}
---
