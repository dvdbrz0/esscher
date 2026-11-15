---
{
 "layout": "story",
 "title": "Latent Sparse Attention: Towards Subquadratic Ultra-Long Context Attention",
 "kind": "paper",
 "section": "Papers that became canon",
 "edition": "weekly",
 "edition_url": "/2026/11/15/weekly/",
 "date": "2026-11-15 08:00:00 +0300",
 "summary": "Keys are clustered hierarchically in a learned latent space and queries score clusters rather than every key. At 10 million tokens one attention layer runs 22.7 times faster in prefill than GLM-5.3-Flash’s own sparse attention and 72.4 times faster than full attention in Qwen-3.8-27B, with similar accuracy.",
 "body": [
  "Sparse attention uses an indexer to choose which keys each query attends to, but existing indexers either still cost time quadratic in the context length or lose accuracy beyond a million tokens. The authors organise the keys into a hierarchy of clusters in a learned latent space, so a query descends the hierarchy instead of scoring every key.",
  "A distilled variant can be added to pretrained models: at 10 million tokens it speeds up decoding by 4.6 times over GLM-5.3-Flash’s sparse attention and 42.5 times over full attention in Qwen-3.8-27B. A native variant, trained on next-token loss alone, matches full attention at 128,000 tokens with a 1.6 times training speed-up per layer. The target use is agents that keep very long histories, such as coding agents working over large repositories."
 ],
 "published": "2026-10-30",
 "authors": "Kubicek et al.",
 "arxiv": "2610.42147",
 "tag": "Large language models",
 "topics": [
  "Large language models",
  "Agents"
 ],
 "image": "/assets/og/2026-11-15-weekly-latent-sparse-attention-towards-subquadratic-ultra-long-context-attent.png"
}
---
