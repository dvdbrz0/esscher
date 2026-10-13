---
{
 "layout": "story",
 "title": "Anthropic says small models may soon copy themselves across cheap devices",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/10/13/daily/",
 "date": "2026-10-13 05:00:00 +0300",
 "summary": "Anthropic’s Frontier Red Team reports that open-weight models of 30B parameters or fewer can complete most steps of self-replication on low-cost hardware, and projects capable replicators by the end of 2026.",
 "body": [
  "Anthropic’s Frontier Red Team, in a report by William Zhou and Daniel Freeman, argues that small AI models may be months away from replicating themselves without a datacentre. The team split a 26B-parameter model across 15 off-brand Android TV boxes costing about $55 each. It also tested whether models could set up an inference server on nine hardware types: a 9B model succeeded on eight of them.",
  "In an end-to-end test, a worm ran across a firewalled network of 8 cloud nodes running Android emulators. GLM-5.2 reached all 8 nodes in 4 of 5 trials and 7 of 8 in the fifth. Models of 30B parameters or fewer could complete many single steps but struggled to chain them. A trend fit of about 13.7 capability-index points per year (\\(R^2 = 0.95\\)) suggests a small model could match GLM-5.2 by the end of 2026.",
  "The authors list their own caveats. The exploit step was deliberately trivial, so the results are an upper bound on real-world success. The capability index is a general proxy, not a measure of replication, and the spread estimate rests on one hardware class and one past botnet. They also note that spread could be slow, with days per doubling."
 ],
 "why": "It puts numbers on how much hardware a self-copying model might reach and how soon, while stating how far the tests fall short of real conditions.",
 "sources": [
  {
   "name": "Anthropic",
   "url": "https://www.anthropic.com/research/self-replicating-ai"
  }
 ],
 "published": "2026-10-12",
 "topics": [
  "AI safety",
  "Agents"
 ],
 "math": true
}
---
