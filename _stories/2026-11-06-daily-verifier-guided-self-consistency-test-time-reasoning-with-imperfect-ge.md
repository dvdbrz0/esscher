---
{
 "layout": "story",
 "title": "Verifier-Guided Self-Consistency: Test-Time Reasoning with Imperfect Generators and Verifiers",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/06/daily/",
 "date": "2026-11-06 05:00:00 +0300",
 "summary": "A stochastic decoder steers generation with step-level and outcome signals while keeping several trajectories for a final vote, and can be read as approximate sampling from a verifier-tilted distribution.",
 "body": [
  "Test-time reasoning has to balance two imperfect signals: a generator that supplies diversity and a verifier that points towards correctness. Verifier-weighted voting cannot steer generation, because it only reweights trajectories already sampled. Beam-style search can steer, but it may concentrate on a narrow set of trajectories and amplify the verifier’s errors.",
  "The method proposed here repeatedly draws candidate next steps from the base model and uses a step-level correctness estimate and a future-outcome estimate in an acceptance and resampling procedure, while maintaining multiple trajectories for answer-level self-consistency. The authors give a probabilistic interpretation as approximate sampling from a verifier-tilted trajectory distribution, and report higher average accuracy than representative baselines across several benchmarks, generators and verifier families."
 ],
 "published": "2026-11-04",
 "authors": "Fadeeva et al.",
 "arxiv": "2611.06606",
 "tag": "Reasoning and inference",
 "topics": [
  "Reasoning and inference",
  "Large language models"
 ],
 "image": "/assets/og/2026-11-06-daily-verifier-guided-self-consistency-test-time-reasoning-with-imperfect-ge.png"
}
---
