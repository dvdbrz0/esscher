---
{
 "layout": "story",
 "title": "Proving and Improving the Platonic Representation Hypothesis with JEPAs",
 "kind": "paper",
 "section": "Papers that became canon",
 "edition": "weekly",
 "edition_url": "/2026/11/08/weekly/",
 "date": "2026-11-08 08:00:00 +0300",
 "summary": "The paper turns the conjecture that models trained on different modalities converge to one representation into a theorem: joint-embedding predictive architectures trained separately learn the same representation up to a rotation when positive pairs are two views of one scene. It argues that next-token prediction is the same architecture with poor views, which explains why language models need scale to align with vision.",
 "body": [
  "The Platonic Representation Hypothesis says that models trained on different data converge, as they scale, to a shared representation of the world. Balestriero and LeCun prove a version of it. Joint-Embedding Predictive Architectures (JEPAs) trained separately on any number of modalities learn the same representation up to one rotation whenever their positive pairs are two observations of the same scene, and their misalignment is bounded otherwise.",
  "Next-token prediction fits the framework as a JEPA whose views are parts of one document, which the authors call bad views. They report a scaling law of alignment that predicts unseen runs within seed noise, and find that good views need 42 times fewer samples than next-token prediction on the same corpus to reach the same alignment. A 109-million-parameter text JEPA aligned with DINOv2 and CLIP image encoders better than every language model they tested, up to 72 billion parameters.",
  "The paper was the most discussed theory result of the week, helped by LeCun’s own posts. The empirical claims await replication."
 ],
 "published": "2026-10-29",
 "authors": "Balestriero and LeCun",
 "arxiv": "2610.39302",
 "tag": "Learning theory",
 "topics": [
  "Learning theory",
  "Large language models"
 ],
 "image": "/assets/og/2026-11-08-weekly-proving-and-improving-the-platonic-representation-hypothesis-with-jepa.png"
}
---
