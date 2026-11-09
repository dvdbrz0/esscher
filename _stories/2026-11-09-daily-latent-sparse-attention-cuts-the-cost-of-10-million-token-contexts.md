---
{
 "layout": "story",
 "title": "Latent Sparse Attention cuts the cost of 10-million-token contexts",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/11/09/daily/",
 "date": "2026-11-09 05:00:00 +0300",
 "summary": "Kubicek et al. cluster attention keys in a learned latent space so that queries score groups of keys, speeding one attention layer by up to 72.4 times at 10 million tokens.",
 "body": [
  "Sparse attention replaces full attention with a selection of keys chosen by an indexer, but current indexers still pay a cost quadratic in context length or lose accuracy above a million tokens. Latent Sparse Attention, from Ales Kubicek and colleagues including Torsten Hoefler, clusters keys hierarchically in a learned latent space, so that a query scores the hierarchy of clusters rather than every key.",
  "A distilled variant can be added to a pre-trained model. At 10 million tokens it sped up one attention layer of GLM-5.3-Flash by 22.7 times in prefill and 4.6 times in decoding against the original sparse attention, and of Qwen-3.8-27B by 72.4 and 42.5 times against full attention, with similar accuracy across tasks. A native variant, trained on the next-token loss, matched full attention at 128,000 tokens and trained 1.6 times faster per layer."
 ],
 "sources": [
  {
   "name": "arXiv",
   "url": "https://arxiv.org/abs/2610.42147"
  }
 ],
 "published": "2026-10-30",
 "topics": [
  "Large language models",
  "Agents"
 ],
 "image": "/assets/og/2026-11-09-daily-latent-sparse-attention-cuts-the-cost-of-10-million-token-contexts.png"
}
---
