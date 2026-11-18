---
{
 "layout": "story",
 "title": "Optimal Autoregressive Chain-of-Thought Learning via Bagging",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/18/daily/",
 "date": "2026-11-18 05:00:00 +0300",
 "summary": "A majority vote of bootstrap-trained generators learns from chain-of-thought demonstrations with optimal sample complexity that does not depend on the length of the chain.",
 "body": [
  "The paper asks how many chain-of-thought demonstrations are needed to learn an autoregressive next-token generator \\(f\\) from a class \\(\\mathcal{F}\\), when each demonstration has length \\(T\\). The proposed algorithm trains generators that are consistent with the chains on bootstrap samples and outputs their majority vote.",
  "For binary tokens it achieves the optimal sample complexity \\(O((d_{\\mathrm{VC}} + \\log(1/\\delta))/\\epsilon)\\), where \\(d_{\\mathrm{VC}}\\) is the VC dimension of \\(\\mathcal{F}\\), independent of \\(T\\). For finite token sets the Graph dimension replaces the VC dimension and the rate is optimal up to a \\(\\log|\\Sigma|\\) factor. The ensemble needs only \\(O(\\log(T/\\delta))\\) generators and can be distilled into a single member of \\(\\mathcal{F}\\) using \\(n\\log(nT)\\) unlabelled prompts."
 ],
 "published": "2026-11-16",
 "authors": "Altabaa et al.",
 "arxiv": "2611.21597",
 "tag": "Learning theory",
 "topics": [
  "Learning theory",
  "Reasoning and inference"
 ],
 "math": true,
 "image": "/assets/og/2026-11-18-daily-optimal-autoregressive-chain-of-thought-learning-via-bagging.png"
}
---
