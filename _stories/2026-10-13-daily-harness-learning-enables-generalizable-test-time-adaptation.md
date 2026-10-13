---
{
 "layout": "story",
 "title": "Harness Learning Enables Generalizable Test-Time Adaptation",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/10/13/daily/",
 "date": "2026-10-13 05:00:00 +0300",
 "summary": "A trained proposer model rewrites an agent’s harness from execution feedback at test time, with no weight updates, and the gains carry over to unseen tasks.",
 "body": [
  "The harness is the executable program around a model: it handles model calls, tool use and information flow. The authors train a proposer model with reinforcement learning to revise the harness of a solver, using the revised harness’s task performance as the reward.",
  "At test time the proposer refines the harness from execution feedback on a new task, while the solver’s parameters stay frozen. The authors report experiments on reasoning and multi-hop question answering, where revision quality improved and the adaptation transferred to unseen tasks. The abstract page could not be opened this morning, so details here come from the paper’s public listing."
 ],
 "authors": "Zhang et al.",
 "arxiv": "2609.35738",
 "tag": "Reasoning and inference",
 "topics": [
  "Reasoning and inference",
  "Agents"
 ]
}
---
