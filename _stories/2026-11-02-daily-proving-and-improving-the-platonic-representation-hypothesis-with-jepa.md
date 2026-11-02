---
{
 "layout": "story",
 "title": "Proving and Improving the Platonic Representation Hypothesis with JEPAs",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/02/daily/",
 "date": "2026-11-02 05:00:00 +0300",
 "summary": "JEPAs trained separately on any number of modalities learn the same representation up to one rotation when positive pairs are two views of one scene. Next-token prediction is shown to be a case with bad views.",
 "body": [
  "The Platonic Representation Hypothesis conjectures that models trained on different modalities converge to one representation as they scale. Balestriero and LeCun turn it into a theorem for Joint-Embedding Predictive Architectures (JEPAs): when positive pairs are two observations of one scene, separately trained encoders agree up to a single rotation, and their misalignment is bounded otherwise.",
  "They then read next-token prediction as a JEPA whose views are parts of one document, which they call bad views, and which they say explains why language models align with vision only through scale. On corpora from 145,000 captions to the texts of 940 million web images, good views needed 42 times fewer training samples for the same alignment. A 109-million-parameter text JEPA aligned with DINOv2 and CLIP’s image encoders better than every language model tested, up to 72 billion parameters.",
  "A scaling law fitted to the runs predicted unseen runs within seed noise. These are preprint claims by the authors and await independent replication."
 ],
 "published": "2026-10-29",
 "authors": "Balestriero and LeCun",
 "arxiv": "2610.39302",
 "tag": "Learning theory",
 "topics": [
  "Learning theory",
  "Large language models"
 ],
 "image": "/assets/og/2026-11-02-daily-proving-and-improving-the-platonic-representation-hypothesis-with-jepa.png"
}
---
