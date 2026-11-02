---
{
 "layout": "story",
 "title": "Closing the Log Gap: Minimax-Optimal Regret for Episodic RL",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/02/daily/",
 "date": "2026-11-02 05:00:00 +0300",
 "summary": "A variant of UCBVI reaches expected regret of order \\(\\sqrt{H^3 S A K}\\) for large \\(K\\), matching the minimax lower bound with no extra polylogarithmic factors for the first time.",
 "body": [
  "For episodic tabular Markov decision processes with episode length \\(H\\), \\(S\\) states, \\(A\\) actions and \\(K\\) episodes, the lower bound on regret was known, but algorithms carried extra logarithmic factors. Zamir et al. close that gap for sufficiently large \\(K\\), with expected regret scaling as \\(\\sqrt{H^3 S A K}\\).",
  "The algorithm gives up strict optimism. It uses MOSS-style exploration bonuses whose logarithmic terms adapt to visit counts and estimated variances. The difficulty is then controlling errors from under-optimism, which the authors handle in an occupancy-weighted way, avoiding the logarithmic cost of concentration uniform over rows.",
  "The analysis yields time-uniform, variance-aware concentration bounds that may be useful elsewhere. A corollary gives \\((\\varepsilon, \\delta)\\)-PAC best-policy identification matching the lower bound \\(\\Omega(H^3 S A \\log(1/\\delta)\\varepsilon^{-2})\\) up to constants in some regimes."
 ],
 "published": "2026-10-29",
 "authors": "Zamir et al.",
 "arxiv": "2610.40165",
 "tag": "Learning theory",
 "topics": [
  "Learning theory",
  "Probability"
 ],
 "math": true,
 "summary_plain": "A variant of UCBVI reaches expected regret of order √H³SAK for large K, matching the minimax lower bound with no extra polylogarithmic factors for the first time.",
 "image": "/assets/og/2026-11-02-daily-closing-the-log-gap-minimax-optimal-regret-for-episodic-rl.png"
}
---
