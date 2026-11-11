---
{
 "layout": "story",
 "title": "The Race Is Decided Early! A Kernel Law Predicts Lock-In in Majority-Vote Test-Time RL",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/11/daily/",
 "date": "2026-11-11 05:00:00 +0300",
 "summary": "In test-time reinforcement learning with majority-vote rewards, each question locks into one answer early, and the paper derives the probability of each outcome from the starting logits and a kernel probe.",
 "body": [
  "Test-time reinforcement learning trains a model on unlabelled questions by rewarding samples that agree with its most frequent answer. Each question ends up locked into a single answer, on hard questions often a wrong one. The authors show that the outcome is settled in a short race, driven by sampling noise, between answers that start close together.",
  "With a separate logit per answer, the runner-up wins with a Gaussian tail probability of the initial gap scaled by an explicit noise constant. In a network the logits share parameters, so updates to trailing answers also move the gap between the two leaders; through the kernel of these shared parameters this shifts the decision boundary, and a closed form gives the corrected probability.",
  "In LoRA experiments on three models from two families, predictions made before training, with the kernel frozen at initialisation and no fitted constants, forecast the locked-in answer better than a logistic model fitted to the outcomes."
 ],
 "published": "2026-11-08",
 "authors": "Hwang et al.",
 "arxiv": "2611.11165",
 "tag": "Reasoning and inference",
 "topics": [
  "Reasoning and inference",
  "Learning theory"
 ],
 "image": "/assets/og/2026-11-11-daily-the-race-is-decided-early-a-kernel-law-predicts-lock-in-in-majority-vo.png"
}
---
