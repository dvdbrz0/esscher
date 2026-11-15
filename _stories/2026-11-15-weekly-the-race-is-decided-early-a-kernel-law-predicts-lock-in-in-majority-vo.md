---
{
 "layout": "story",
 "title": "The Race Is Decided Early! A Kernel Law Predicts Lock-In in Majority-Vote Test-Time RL",
 "kind": "paper",
 "section": "Read this week",
 "edition": "weekly",
 "edition_url": "/2026/11/15/weekly/",
 "date": "2026-11-15 08:00:00 +0300",
 "summary": "In test-time reinforcement learning rewarded by majority vote, each question locks into one answer early. The authors derive the probability that the runner-up wins as a normal tail probability of the initial logit gap, corrected through the kernel of the shared parameters.",
 "body": [
  "Test-time reinforcement learning trains a language model on unlabelled questions by rewarding the samples that agree with its most frequent answer. During training each question locks into one answer, on hard questions often a wrong one, and until now which answer won was known only afterwards.",
  "The authors show the outcome is decided early, in a short race driven by sampling noise between answers that start close together. With a separate logit for each answer, the runner-up wins with a normal tail probability of the initial gap, scaled by an explicit noise constant. In a network the logits share parameters, so updates to trailing answers also move the gap between the two leaders; a closed form computes the shifted probability from a kernel probe and the starting logits. In LoRA experiments on three models from two families, predictions made before training, with the kernel frozen at its starting value, forecast the locked-in answer better than a logistic model refitted on the outcomes."
 ],
 "why": "It turns self-consistency training into a quantitative prediction: which answer a question will lock into can be computed before training, from the starting logits and a kernel probe, with no fitted constants. For readers interested in the probability of test-time reasoning it is a clean example of a diffusion-style race analysed in closed form.",
 "published": "2026-11-08",
 "authors": "Hwang et al.",
 "arxiv": "2611.11165",
 "tag": "Reasoning and inference",
 "topics": [
  "Reasoning and inference",
  "Probability"
 ],
 "image": "/assets/og/2026-11-15-weekly-the-race-is-decided-early-a-kernel-law-predicts-lock-in-in-majority-vo.png"
}
---
