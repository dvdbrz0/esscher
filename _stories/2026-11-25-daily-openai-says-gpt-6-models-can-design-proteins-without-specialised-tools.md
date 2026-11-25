---
{
 "layout": "story",
 "title": "OpenAI says GPT-6 models can design proteins without specialised tools",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/11/25/daily/",
 "date": "2026-11-25 05:00:00 +0300",
 "summary": "In a preprint, OpenAI reports that its GPT-6 models design protein structures and sequences using only reasoning and general-purpose code, and that lab tests found binding for designs aimed at five targets.",
 "body": [
  "OpenAI published a preprint on 24 November arguing that its GPT-6 family can do much of the work of specialised protein-design models. Given a target protein and a marked binding site, GPT-6.2 wrote code to generate three-dimensional designs for small binding proteins, without calling dedicated biology models. On computational quality measures its designs scored slightly below RFdiffusion, a specialised design model, while OpenAI’s latest internal models scored above it.",
  "With the research partner Onava, OpenAI made and tested proteins based on the designs. For each of the five targets at least one protein showed evidence of binding. The pipeline was not purely the language model: a specialised model, SolubleMPNN, supplied the amino acid sequences, and other specialised models helped choose candidates. In separate tests GPT-6.2 redesigned sequences for existing binders and antibodies, many of which kept their binding.",
  "Across 14 computational protein tasks the newest models matched or beat specialised models on most, according to OpenAI. Predicting a complete protein structure remained a clear weakness."
 ],
 "why": "It is evidence that a general model can replace parts of a specialised scientific toolchain, though the lab results still relied on specialised models for sequences and selection.",
 "sources": [
  {
   "name": "OpenAI",
   "url": "https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/"
  }
 ],
 "published": "2026-11-24",
 "topics": [
  "Large language models",
  "AI industry"
 ],
 "image": "/assets/og/2026-11-25-daily-openai-says-gpt-6-models-can-design-proteins-without-specialised-tools.png"
}
---
