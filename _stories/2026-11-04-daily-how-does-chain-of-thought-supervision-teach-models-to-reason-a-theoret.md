---
{
 "layout": "story",
 "title": "How Does Chain-of-Thought Supervision Teach Models to Reason? A Theoretical Analysis",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/04/daily/",
 "date": "2026-11-04 05:00:00 +0300",
 "summary": "A high-dimensional analysis shows phase transitions in long-horizon reasoning, set by context length and supervision budget, and separates two mechanisms of overthinking.",
 "body": [
  "Models trained on finite teacher chains of thought may need to keep reasoning beyond what they saw, and longer reasoning can degrade performance. The authors study this with an in-context weight prediction model trained on finite gradient descent trajectories for linear regression.",
  "High-dimensional asymptotics show that success and failure of long-horizon reasoning undergo phase transitions depending on context length and the total training budget. They distinguish error accumulation from error amplification, and find that with short contexts a larger budget can worsen long-horizon error before reasoning stabilises. Trained linear and multi-head softmax attention show the same qualitative behaviour."
 ],
 "published": "2026-11-01",
 "authors": "Takanami and Pehlevan",
 "arxiv": "2611.01740",
 "tag": "Reasoning and inference",
 "topics": [
  "Reasoning and inference",
  "Learning theory"
 ],
 "image": "/assets/og/2026-11-04-daily-how-does-chain-of-thought-supervision-teach-models-to-reason-a-theoret.png"
}
---
