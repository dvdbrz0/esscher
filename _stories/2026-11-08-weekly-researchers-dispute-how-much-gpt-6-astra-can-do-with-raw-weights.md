---
{
 "layout": "story",
 "title": "Researchers dispute how much GPT-6 Astra can do with raw weights",
 "kind": "story",
 "section": "The debates",
 "edition": "weekly",
 "edition_url": "/2026/11/08/weekly/",
 "date": "2026-11-08 08:00:00 +0300",
 "summary": "MIT CSAIL researchers reported that GPT-6 Astra raised a small model’s MATH-500 score from 7.9% to 48.1% by editing 0.016% of its weights. Critics replied that the headline result used tools and many forward passes, and that the no-tools setting covers only small networks.",
 "body": [
  "Rikiya Takehi, Omar Khattab and colleagues published their results on 2 November under the name weight-space programming. Given a Python session over the weights of Qwen3.5-0.8B and 50 forward passes on practice problems, Astra traced the model’s thinking loops to one direction and subtracted it from 131,072 weights. On Gemma 3 270M, which does not loop, scores hardly moved.",
  "Sean Goedecke argued that a competent researcher could do the same and that the edit resembles known steering methods. Matthew Honnibal, author of spaCy, counted only three experiments in the setting with raw weights and no tools, on networks of 17,000 to 172,000 weights. Simon Willison tested that setting himself: an open model on his laptop named Pac-Man, Pong and Breakout from raw weights in roughly 46 to 65 minutes each and failed on Freeway.",
  "The two sides agree the work shows real progress. They disagree over whether it is one capability or several familiar techniques run by a capable agent."
 ],
 "sources": [
  {
   "name": "Takehi et al.: Sparks of Weight-Space Programming",
   "url": "https://rikiyat.github.io/blog/weight-space-programming/"
  },
  {
   "name": "Matthew Honnibal",
   "url": "https://honnibal.dev/blog/astra-read-write-misleading"
  },
  {
   "name": "Simon Willison",
   "url": "https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/"
  },
  {
   "name": "Discussion on X",
   "url": "https://x.com/rikiyatakehi/status/2117313742891327994"
  }
 ],
 "published": "2026-11-03",
 "topics": [
  "Large language models",
  "AI safety"
 ],
 "image": "/assets/og/2026-11-08-weekly-researchers-dispute-how-much-gpt-6-astra-can-do-with-raw-weights.png"
}
---
