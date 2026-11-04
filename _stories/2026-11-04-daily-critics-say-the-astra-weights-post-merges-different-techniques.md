---
{
 "layout": "story",
 "title": "Critics say the Astra weights post merges different techniques",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/11/04/daily/",
 "date": "2026-11-04 05:00:00 +0300",
 "summary": "Matthew Honnibal says the MIT post mixes raw-weight reading with Python tooling, while Simon Willison showed a laptop model can identify some games from raw weights.",
 "body": [
  "The MIT CSAIL post by Rikiya Takehi and colleagues, published on 2 November, said GPT-6 Astra could read and write neural network weights. Matthew Honnibal, author of spaCy, wrote on 3 November that the summary misleads. By his count, the setting with raw floats, no tools and no execution appears only in three experiments, on networks of 17,000 to 172,000 weights.",
  "The headline result lifted Qwen3.5-0.8B on MATH-500 from 7.9% to 48.1%. Honnibal says it used Python and up to 50 passes through the model on practice problems, and that the same approach failed on Gemma 3. He adds that written-from-scratch game networks beat a policy trained with proximal policy optimisation for 500 million steps only on Breakout.",
  "Simon Willison tested the no-tools question. Running Qwen 3.8 27B on his laptop, he reported it named Pac-Man, Pong and Breakout from raw weights in roughly 46 to 65 minutes each, and failed on Freeway. Both critics treat the work as real progress. Their dispute is over how much of it is a single capability."
 ],
 "why": "The claim that models understand large networks directly rests on experiments the critics say were not done on large networks.",
 "sources": [
  {
   "name": "Matthew Honnibal",
   "url": "https://honnibal.dev/blog/astra-read-write-misleading"
  },
  {
   "name": "Simon Willison",
   "url": "https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/"
  },
  {
   "name": "Original post",
   "url": "https://rikiyat.github.io/blog/weight-space-programming/"
  },
  {
   "name": "Discussion on X",
   "url": "https://x.com/rikiyatakehi/status/2117313742891327994"
  }
 ],
 "published": "2026-11-03",
 "topics": [
  "Large language models",
  "Agents"
 ],
 "image": "/assets/og/2026-11-04-daily-critics-say-the-astra-weights-post-merges-different-techniques.png"
}
---
