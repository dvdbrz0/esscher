---
{
 "layout": "story",
 "title": "Anytime-Valid PAC-Bayes Certificates for Adaptive Test-Time Scaling",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/18/daily/",
 "date": "2026-11-18 05:00:00 +0300",
 "summary": "A time-uniform PAC-Bayes certificate stays valid after a test-time scaling recipe is chosen adaptively, and a margin law shows when plurality voting helps and when more samples hurt.",
 "body": [
  "Test-time scaling systems pick a sample budget, a prompt and a verifier or aggregation rule after repeatedly looking at a calibration set, and ordinary validation error bars are not valid after such selection. The authors model a recipe as a randomised predictor with a random cost and prove a PAC-Bayes certificate that holds simultaneously over all calibration times, all posterior mixtures over recipes and all data-dependent stopping rules.",
  "For a finite grid of \\(M\\) budgets and verifiers with \\(n\\) calibration examples the penalty is of order \\(\\log M / n\\), which the authors show no certificate valid after selection can avoid in the worst case. Specialised to self-consistency, a margin analysis shows that plurality voting improves exponentially in the sample budget only on examples where the correct answer is the generator’s unique mode; otherwise more compute can amplify errors. The same analysis gives a water-filling rule for allocating compute.",
  "On GSM8K, selected-best error bars fell below the out-of-split risk in up to 22.5% of random splits at a nominal 5%, while the certificate never did. The paper was accepted at NeurIPS 2026."
 ],
 "published": "2026-11-16",
 "authors": "Li and Long",
 "arxiv": "2611.21241",
 "tag": "Reasoning and inference",
 "topics": [
  "Reasoning and inference",
  "Learning theory"
 ],
 "math": true,
 "image": "/assets/og/2026-11-18-daily-anytime-valid-pac-bayes-certificates-for-adaptive-test-time-scaling.png"
}
---
