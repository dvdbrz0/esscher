---
{
 "layout": "story",
 "title": "e-means: outperforming k-means (in one-tenth the epochs)",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/10/daily/",
 "date": "2026-11-10 05:00:00 +0300",
 "summary": "A mini-batch k-means with exponential moving averages and scaling-law hyperparameters beats the loss of Lloyd’s algorithm after 25 epochs in 1.4 to 2.6 epochs.",
 "body": [
  "Lloyd’s algorithm, a full-batch method, is still the standard for k-means clustering. The Meta FAIR team replaces it with mini-batch updates in which each cluster’s running sum and count are exponential moving averages, and the centroid is their ratio. Scaling laws relating decay rate and batch size to final loss fix both hyperparameters for each problem size, so no sweep is needed.",
  "On a range of embedding datasets, e-means reaches a loss below Lloyd’s at 25 epochs within 1.4 to 2.6 epochs, which the authors report as 10 to 45 times faster on GPU than leading k-means implementations, often beating k-means++ as well. It partitioned 10 billion DINO embeddings into 16 million clusters in 2.5 epochs. The code is released in Faiss."
 ],
 "published": "2026-11-06",
 "authors": "Bessa et al.",
 "arxiv": "2611.09501",
 "tag": "Optimization",
 "topics": [
  "Optimization"
 ],
 "image": "/assets/og/2026-11-10-daily-e-means-outperforming-k-means-in-one-tenth-the-epochs.png"
}
---
