---
{
 "layout": "story",
 "title": "A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/12/daily/",
 "date": "2026-11-12 05:00:00 +0300",
 "summary": "REINFORCE, the basis of PPO and GRPO, can drive the probability of optimal responses towards zero while reward rises; resetting the KL reference to the latest policy prevents this and yields global convergence guarantees.",
 "body": [
  "The paper asks which post-training algorithms learn near-optimal policies at a cost governed by the base model’s coverage, meaning how readily it already samples optimal responses. It calls such algorithms coverage-preserving. REINFORCE is not: it can push the probability of optimal answers close to zero even as average reward improves, after which convergence may take exponentially many steps. The failure occurs with exact gradients and survives KL regularisation towards the base model.",
  "The remedy is to reset the KL reference to the most recent policy, formalised as Approximate Policy Mirror Descent, which solves a sequence of KL-regularised subproblems. For softmax linear policies over pretrained features, the authors prove the first global convergence guarantees showing that stylised PPO and GRPO with explicit regularisation and resets, and squared-loss methods such as those used for the Kimi models, are coverage-preserving. The result bears on why reinforcement learning can narrow the diversity that sampling-based inference such as majority voting relies on."
 ],
 "published": "2026-11-10",
 "authors": "Huang et al.",
 "arxiv": "2611.14467",
 "tag": "Reasoning and inference",
 "topics": [
  "Reasoning and inference",
  "Learning theory",
  "Large language models"
 ],
 "image": "/assets/og/2026-11-12-daily-a-theory-of-policy-optimization-in-post-training-coverage-collapse-and.png"
}
---
