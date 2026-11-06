---
{
 "layout": "story",
 "title": "Give Up to Get More: Priors, Not Policies, Govern Test-Time Compute Allocation",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/06/daily/",
 "date": "2026-11-06 05:00:00 +0300",
 "summary": "The value of one more attempt peaks at intermediate difficulty, so the best static allocation is an inverted U. Thompson Sampling with a verifier and a good prior lifts the solved share from 14% to 27%.",
 "body": [
  "When many inputs share a budget of repeated attempts, a common rule gives harder inputs more. On public maths, code and formal-proof samples, the best published difficulty-proportional rule captures half or more of the oracle gain where the model mostly succeeds, but at most 13% on hard workloads, even with true pass rates. The optimal static allocation is an inverted U and gives little to inputs that are hopeless at the current budget.",
  "Acting on this requires knowing which inputs are solvable, so information rather than the policy drives the gain. With a verifier and a prior from a related model’s past runs, Thompson Sampling raises the solved share on the hardest workload from 14% to 27%. Without such a prior, no tested policy beats round-robin. The gain vanishes between prior rank correlations of about 0.3 and 0.55, and it needs a verifier whose false acceptances are rare relative to the pass rate."
 ],
 "published": "2026-11-04",
 "authors": "Bae",
 "arxiv": "2611.06372",
 "tag": "Reasoning and inference",
 "topics": [
  "Reasoning and inference",
  "Optimization"
 ],
 "image": "/assets/og/2026-11-06-daily-give-up-to-get-more-priors-not-policies-govern-test-time-compute-alloc.png"
}
---
