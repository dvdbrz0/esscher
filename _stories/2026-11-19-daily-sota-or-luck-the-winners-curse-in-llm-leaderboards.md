---
{
 "layout": "story",
 "title": "SOTA or Luck? The Winner’s Curse in LLM Leaderboards",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/19/daily/",
 "date": "2026-11-19 05:00:00 +0300",
 "summary": "Ranking noisy benchmark scores overstates the leaders. An \\(m\\)-out-of-\\(N\\) bootstrap reduces the ranking bias from order \\(N^{-1/2}\\) to \\(o(N^{-1/2})\\) in \\(N\\) tasks.",
 "body": [
  "Leaderboards rank models by average scores over \\(N\\) benchmark tasks, and selecting the top of a noisy ranking rewards luck as well as ability. The authors call the resulting distortion rank-induced bias and correct it with an \\(m\\)-out-of-\\(N\\) bootstrap, assuming independent, identically distributed bounded tasks but allowing arbitrary correlation between models on the same task.",
  "When the population scores fall into tiers separated by positive gaps, they prove the bootstrap cuts the bias from \\(\\Theta(N^{-1/2})\\) to \\(o(N^{-1/2})\\). Across 14 benchmarks the correction to the leader ranges from about 0.09 to 3.86 percentage points; on SWE-bench Verified, 13 of 173 models land in the leading tier."
 ],
 "published": "2026-11-17",
 "authors": "Xu et al.",
 "arxiv": "2611.22227",
 "tag": "Learning theory",
 "topics": [
  "Learning theory",
  "Probability"
 ],
 "math": true,
 "summary_plain": "Ranking noisy benchmark scores overstates the leaders. An m-out-of-N bootstrap reduces the ranking bias from order N^(−1/2) to o(N^(−1/2)) in N tasks.",
 "image": "/assets/og/2026-11-19-daily-sota-or-luck-the-winners-curse-in-llm-leaderboards.png"
}
---
