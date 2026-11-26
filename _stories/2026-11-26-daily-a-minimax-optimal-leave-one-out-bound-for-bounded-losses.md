---
{
 "layout": "story",
 "title": "A Minimax Optimal Leave One Out Bound for Bounded Losses",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/26/daily/",
 "date": "2026-11-26 05:00:00 +0300",
 "summary": "For proper leave-one-out prediction with \\(M\\) experts and a loss bounded by \\(B\\), the minimax excess loss is of order \\(\\min\\{B, \\sqrt{B r \\log M / n} + B \\log M / n\\}\\), attained by one deterministic rule.",
 "body": [
  "The paper studies proper leave-one-out prediction with \\(M\\) real-valued experts on \\(n\\) fixed inputs: each label is hidden in turn and the learner uses the others to choose one expert’s prediction at the held-out point. The question is how close such a rule can come to the average loss of the best single expert on the full sample.",
  "For any bounded loss that is a continuous nondecreasing function of absolute error and vanishes at zero, with maximum value \\(B\\), and over samples on which the best expert has average loss at most \\(r\\), the minimax excess loss is of order \\(\\min\\{B, \\sqrt{B r \\log M / n} + B \\log M / n\\}\\). A single deterministic rule attains this rate for every \\(r \\in [0, B]\\), and the matching lower bound holds even for randomised proper rules that know \\(r\\). The result gives a sharp, small-loss-adaptive guarantee for leave-one-out selection."
 ],
 "published": "2026-11-24",
 "authors": "Gao and Qian",
 "arxiv": "2611.31972",
 "tag": "Learning theory",
 "topics": [
  "Learning theory"
 ],
 "math": true,
 "summary_plain": "For proper leave-one-out prediction with M experts and a loss bounded by B, the minimax excess loss is of order min {B, √(Brlog M/n)+Blog M/n}, attained by one deterministic rule.",
 "image": "/assets/og/2026-11-26-daily-a-minimax-optimal-leave-one-out-bound-for-bounded-losses.png"
}
---
