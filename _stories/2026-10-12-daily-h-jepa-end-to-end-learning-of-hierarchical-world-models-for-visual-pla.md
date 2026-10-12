---
{
 "layout": "story",
 "title": "H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/10/12/daily/",
 "date": "2026-10-12 05:00:00 +0300",
 "summary": "Levels of latent predictors each forecast further ahead and hand subgoals downwards. A three-level hierarchy raises Visual AntMaze success from 18% to 73% with less planner compute.",
 "body": [
  "The paper asks whether world models that predict in a learned latent space can plan over long horizons if the prediction is organised in levels. Each level is an action-conditioned joint-embedding predictive model that looks further ahead than the one beneath it.",
  "Planning is top-down: the upper level proposes a latent target, and the lower level plans toward it. In four simulated environments the hierarchy outperforms a flat model, and on Visual AntMaze the three-level version reaches 73% success against 18%, using less planning compute.",
  "The authors also report an extension to real-robot videos from DROID, using inverse-dynamics supervision, with better offline planning fidelity at lower compute. Code and weights were released."
 ],
 "published": "2026-10-05",
 "authors": "Zhang et al.",
 "arxiv": "2610.06805",
 "tag": "Agents",
 "topics": [
  "Agents",
  "Large language models"
 ],
 "image": "/assets/og/2026-10-12-daily-h-jepa-end-to-end-learning-of-hierarchical-world-models-for-visual-pla.png"
}
---
