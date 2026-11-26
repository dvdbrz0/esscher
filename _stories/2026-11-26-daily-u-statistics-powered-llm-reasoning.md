---
{
 "layout": "story",
 "title": "U-Statistics-Powered LLM Reasoning",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/26/daily/",
 "date": "2026-11-26 05:00:00 +0300",
 "summary": "The policy gradient in group relative policy optimisation is a U-statistic, which turns the choice of group size into a classical variance-ratio estimation problem.",
 "body": [
  "Group relative policy optimisation (GRPO), introduced by DeepSeek, is widely used to train reasoning models, yet its group size is usually chosen by trial and error. The authors, including Victor Chernozhukov, exploit the U-statistic structure of its policy gradient to recast group-size selection as estimating a ratio of variances.",
  "Because the denominator can be small, plug-in estimates are unstable, so they propose a pessimistic estimator that accounts for the denominator’s uncertainty and characterise it in three sample-size regimes. On Reasoning Gym tasks and on mathematical reasoning and code-generation benchmarks, adaptive group sizes reduce the mean squared error of the gradient and improve training over fixed sizes at modest extra cost."
 ],
 "published": "2026-11-24",
 "authors": "Gong et al.",
 "arxiv": "2611.33064",
 "tag": "Reasoning and inference",
 "topics": [
  "Reasoning and inference",
  "Large language models"
 ],
 "image": "/assets/og/2026-11-26-daily-u-statistics-powered-llm-reasoning.png"
}
---
