---
{
 "layout": "story",
 "title": "High-dimensional limit theorems for adaptive variants of SGD I: Ballistic limits",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/18/daily/",
 "date": "2026-11-18 05:00:00 +0300",
 "summary": "High-dimensional effective dynamics for Adam, Muon and related optimisers, obtained by averaging out their memory, allow exact comparisons with plain stochastic gradient descent.",
 "body": [
  "Adaptive optimisers such as Adam and Muon are not Markovian, because of their exponential moving averages and preconditioning. The authors show that in high dimension this memory can be handled by the method of averaging, giving effective dynamics that are a Markov process, for tasks including tensor PCA, Gaussian projective models, teacher-student networks and a multi-layer network trained on XOR.",
  "The limits allow precise comparisons between algorithms. One finding is a crossover: online stochastic gradient descent generalises better than Adam early in training until the learning curves cross and Adam takes over. The authors also prove a version of the Edge of Stability phenomenon, characterised sharply by an analogue of the infinity Laplacian."
 ],
 "published": "2026-11-14",
 "authors": "Jagannath and Sarangian",
 "arxiv": "2611.19059",
 "tag": "Optimization",
 "topics": [
  "Optimization",
  "Probability"
 ],
 "image": "/assets/og/2026-11-18-daily-high-dimensional-limit-theorems-for-adaptive-variants-of-sgd-i-ballist.png"
}
---
