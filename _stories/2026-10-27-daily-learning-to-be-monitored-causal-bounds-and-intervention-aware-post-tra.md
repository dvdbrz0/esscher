---
{
 "layout": "story",
 "title": "Learning to Be Monitored: Causal Bounds and Intervention-Aware Post-Training Recipes for Chain-of-Thought Monitorability",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/10/27/daily/",
 "date": "2026-10-27 05:00:00 +0300",
 "summary": "The standard metric for chain-of-thought monitorability is shown to be an upper bound on the true causal detection rate; the authors add a lower bound and train models whose reasoning is easier to monitor.",
 "body": [
  "Chain-of-thought monitoring tries to catch harmful behaviour from a model’s written reasoning. Intervention-based tests ask whether a monitor can see the effect of an intervention in the reasoning when the target behaviour occurs, usually through a minimal-criterion sensitivity \\(\\mathrm{TPR}_{\\mathrm{mc}}\\). The authors point out that behaviour observed under an intervention is not always caused by it.",
  "They prove that \\(\\mathrm{TPR}_{\\mathrm{mc}}\\) upper-bounds the rate at which a monitor detects behaviour actually caused by the intervention, and derive a matching lower bound. Using paired control and intervention tasks, they then train models by off-policy self-distillation, reinforcement learning and on-policy self-distillation, and all three generally improve monitorability under the tighter evaluation."
 ],
 "published": "2026-10-22",
 "authors": "Fu et al.",
 "arxiv": "2610.31733",
 "tag": "Reasoning and inference",
 "topics": [
  "Reasoning and inference",
  "AI safety"
 ],
 "math": true,
 "image": "/assets/og/2026-10-27-daily-learning-to-be-monitored-causal-bounds-and-intervention-aware-post-tra.png"
}
---
