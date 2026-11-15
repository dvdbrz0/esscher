---
{
 "layout": "story",
 "title": "A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets",
 "kind": "paper",
 "section": "Papers that became canon",
 "edition": "weekly",
 "edition_url": "/2026/11/15/weekly/",
 "date": "2026-11-15 08:00:00 +0300",
 "summary": "REINFORCE, the basis of PPO and GRPO, can drive the probability of optimal responses towards zero even as reward rises, and KL regularisation to the base model does not prevent it. Repeatedly resetting the KL reference to the latest policy does, and gives the first global convergence guarantees for these families of algorithms.",
 "body": [
  "The paper, by Audrey Huang, Nan Jiang, Sham Kakade, Sadhika Malladi, Akshay Krishnamurthy and Dylan Foster, measures post-training by the base model’s coverage, how readily it samples optimal responses, and asks which algorithms learn near-optimal policies at a cost governed by that coverage.",
  "Its negative result is coverage collapse: even with exact gradients, REINFORCE can push the probability of optimal answers close to zero while average reward improves, and convergence can then take exponentially many steps. The positive result is Approximate Policy Mirror Descent, a sequence of KL-regularised subproblems whose reference is reset to the most recent policy. For softmax linear policies over pretrained features this yields global convergence for stylised PPO and GRPO variants with resets, and for squared-loss methods that implement resets implicitly. The link to test-time reasoning is direct: majority voting and self-consistency rely on the diversity that collapse destroys."
 ],
 "published": "2026-11-10",
 "authors": "Huang et al.",
 "arxiv": "2611.14467",
 "tag": "Learning theory",
 "topics": [
  "Learning theory",
  "Reasoning and inference"
 ],
 "image": "/assets/og/2026-11-15-weekly-a-theory-of-policy-optimization-in-post-training-coverage-collapse-and.png"
}
---
