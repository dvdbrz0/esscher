---
{
 "layout": "story",
 "title": "e-means: outperforming k-means (in one-tenth the epochs)",
 "kind": "paper",
 "section": "Papers that became canon",
 "edition": "weekly",
 "edition_url": "/2026/11/15/weekly/",
 "date": "2026-11-15 08:00:00 +0300",
 "summary": "A mini-batch k-means with exponential moving average updates, whose decay rate and batch size are fixed by fitted scaling laws, beats the loss of 25 epochs of Lloyd’s algorithm in 1.4 to 2.6 epochs, a 10–45 times speed-up on GPUs.",
 "body": [
  "Lloyd’s algorithm alternates assigning every point to its nearest centre and recomputing the centres, so each round reads the whole dataset. The authors replace the full recomputation with mini-batch updates of an exponential moving average per centre, and fits scaling laws for how the decay rate and batch size affect the final loss, which removes the need for a hyperparameter sweep.",
  "On a range of embedding datasets the method reaches a lower loss than 25 epochs of Lloyd’s algorithm in 1.4 to 2.6 epochs, and often beats k-means++. As a demonstration it splits 10 billion DINO embeddings into 16 million clusters in 2.5 epochs. Clustering at this scale sits underneath retrieval, quantisation and data curation for large models, so a tenfold saving in passes matters in practice."
 ],
 "published": "2026-11-06",
 "authors": "Bessa et al.",
 "arxiv": "2611.09501",
 "tag": "Optimization",
 "topics": [
  "Optimization",
  "Large language models"
 ],
 "image": "/assets/og/2026-11-15-weekly-e-means-outperforming-k-means-in-one-tenth-the-epochs.png"
}
---
