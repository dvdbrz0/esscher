---
{
 "layout": "story",
 "title": "H-JEPA stacks world models to plan far ahead from video",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/10/12/daily/",
 "date": "2026-10-12 05:00:00 +0300",
 "summary": "A paper co-written by Yann LeCun trains levels of latent predictors that each look further ahead. On Visual AntMaze a three-level hierarchy raises success from 18% to 73% while using less planner compute.",
 "body": [
  "H-JEPA, by Wancong Zhang, Basile Terver, Michael Rabbat, Yann LeCun and Randall Balestriero, trains a stack of action-conditioned joint-embedding predictive models. Each level predicts further ahead in its own latent space. Planning runs from the top down, and the predictions of one level serve as subgoals for the level below.",
  "Across four simulated navigation and manipulation environments, hierarchical planning beats a flat model of the same kind. On Visual AntMaze, a three-level hierarchy lifts success from 18% to 73% with less planner compute. With inverse-dynamics supervision the method also extends to real-robot videos from the DROID dataset, where it improves offline planning at lower compute.",
  "VentureBeat reports that a regularisation term prevents the model from mapping every observation to the same representation, and that the time spans between levels are fixed in advance. The results come from simulation and offline video, not from robots acting in the loop."
 ],
 "why": "It tests whether hierarchy in latent space makes long-horizon visual planning cheaper.",
 "sources": [
  {
   "name": "arXiv",
   "url": "https://arxiv.org/abs/2610.06805"
  },
  {
   "name": "VentureBeat",
   "url": "https://venturebeat.com/technology/h-jepa-teaches-world-models-to-plan-at-multiple-levels-of-abstraction"
  }
 ],
 "published": "2026-10-05",
 "topics": [
  "Agents",
  "Large language models"
 ]
}
---
