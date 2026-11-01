---
{
 "layout": "story",
 "title": "Proving and Improving the Platonic Representation Hypothesis with JEPAs",
 "kind": "paper",
 "section": "Papers that became canon",
 "edition": "weekly",
 "edition_url": "/2026/11/01/weekly/",
 "date": "2026-11-01 08:00:00 +0300",
 "summary": "Balestriero and LeCun turn the Platonic Representation Hypothesis into a theorem for joint-embedding predictive architectures and argue that next-token prediction is an inefficient route to it.",
 "body": [
  "The authors prove that joint-embedding predictive architectures (JEPAs) trained separately on any number of modalities learn the same representation up to one rotation when their positive pairs are two observations of one scene, and that their misalignment is bounded otherwise. Next-token prediction appears as a JEPA with poor pairs, parts of a single document, which would explain why language models align with vision only through scale.",
  "Good pairs need 42 times fewer training samples than next-token prediction on the same corpus to reach the same alignment, and a 109M-parameter text JEPA aligns with the image encoders of DINOv2 and CLIP better than every language model the authors tested, up to 72B parameters. It is the formal version of Yann LeCun’s long argument against scaling next-token prediction alone, so it will be read closely and contested."
 ],
 "published": "2026-10-29",
 "authors": "Balestriero and LeCun",
 "arxiv": "2610.39302",
 "tag": "Representation learning",
 "topics": [
  "Large language models",
  "Learning theory"
 ],
 "image": "/assets/og/2026-11-01-weekly-proving-and-improving-the-platonic-representation-hypothesis-with-jepa.png"
}
---
