---
{
 "layout": "story",
 "title": "Why the winner of a leaderboard is overrated, and by how much",
 "kind": "explainer",
 "section": "The maths behind the news",
 "edition": "weekly",
 "edition_url": "/2026/11/01/weekly/",
 "date": "2026-11-01 08:00:00 +0300",
 "summary": "When the best of \\(M\\) noisy but unbiased scores is reported, its expected value is too high. A short argument bounds the excess by \\(\\sqrt{(M-1)V/M}\\), where \\(V\\) is the total noise variance, whatever the dependence between the errors.",
 "body": [
  "Leaderboards rank models by scores measured with error, then report the top one. A paper posted on 22 October by Ivan Viakhirev, Kirill Borodin and Grach Mkrtchian makes precise how much this inflates the winner, and the week’s new leader on a large model index is a reminder of why it matters.",
  "Write the score of candidate \\(i\\) as \\(X_i = \\mu_i + \\varepsilon_i\\), where \\(\\mu_i\\) is its true value and the noise satisfies \\(\\mathbb{E}[\\varepsilon_i] = 0\\), for \\(i = 1, \\dots, M\\). Because \\(\\max_i X_i \\ge X_j\\) for every \\(j\\), taking expectations gives \\(\\mathbb{E}[\\max_i X_i] \\ge \\max_j \\mu_j\\). The reported winner is biased upwards, and the bias \\(B = \\mathbb{E}[\\max_i X_i] - \\max_j \\mu_j\\) is never negative.",
  "For an upper bound, note that \\(\\max_i (\\mu_i + \\varepsilon_i) \\le \\max_j \\mu_j + \\max_i \\varepsilon_i\\), so \\(B \\le \\mathbb{E}[\\max_i \\varepsilon_i]\\). Let \\(\\bar\\varepsilon\\) be the mean of the errors and \\(y_i = \\varepsilon_i - \\bar\\varepsilon\\), so that \\(\\sum_i y_i = 0\\). If \\(y_1\\) is the largest, the other \\(M-1\\) values sum to \\(-y_1\\), and by the Cauchy-Schwarz inequality their squares sum to at least \\(y_1^2/(M-1)\\). Hence\n\\[ \\max_i y_i \\le \\sqrt{\\tfrac{M-1}{M} \\textstyle\\sum_i y_i^2}. \\]",
  "Since \\(\\mathbb{E}[\\bar\\varepsilon] = 0\\), Jensen’s inequality for the concave square root gives\n\\[ \\begin{aligned} B &\\le \\mathbb{E}\\Big[\\sqrt{\\tfrac{M-1}{M} \\textstyle\\sum_i y_i^2}\\Big] \\\\ &\\le \\sqrt{\\tfrac{M-1}{M}\\, \\mathbb{E}\\textstyle\\sum_i y_i^2} \\\\ &\\le \\sqrt{\\tfrac{M-1}{M}\\, V}, \\end{aligned} \\]\nwith \\(V = \\sum_i \\operatorname{Var}(\\varepsilon_i)\\), because \\(\\sum_i y_i^2 = \\sum_i \\varepsilon_i^2 - M\\bar\\varepsilon^2 \\le \\sum_i \\varepsilon_i^2\\). Nothing in the argument uses independence: the bound holds for any dependence between the errors, and the constant \\(\\sqrt{(M-1)/M}\\) was already known to be sharp in that case.",
  "The paper’s contribution is the classes in between. For independent noise that is not identically distributed the sharp constant is \\(\\sqrt{(M-1)/(2M)}\\), and for pairwise nonnegatively correlated noise it is \\((M-1)/M\\); explicit constructions attain both, and the theorems are checked in Lean 4. Across 448 selection pipelines for language models and classifiers, designs that give each candidate its own test items reach a median of 0.75 of the independent-class ceiling.",
  "The practical lesson is about design. At a fixed budget of test items, the authors find that scoring all candidates on the same items is markedly less optimistic than giving each its own. The argument above shows why: only the deviations \\(y_i\\) from the average error lift one candidate above the rest, and an error shared by every candidate cancels. The same reasoning applies to best-of-\\(n\\) selection at inference time, where a verifier picks the highest-scoring of \\(n\\) sampled answers."
 ],
 "sources": [
  {
   "name": "arXiv:2610.31948",
   "url": "https://arxiv.org/abs/2610.31948"
  },
  {
   "name": "9to5Google",
   "url": "https://9to5google.com/2026/10/28/gemini-4-carbon/"
  }
 ],
 "published": "2026-10-22",
 "topics": [
  "Mathematics",
  "Probability"
 ],
 "math": true,
 "summary_plain": "When the best of M noisy but unbiased scores is reported, its expected value is too high. A short argument bounds the excess by √((M−1)V/M), where V is the total noise variance, whatever the dependence between the errors.",
 "image": "/assets/og/2026-11-01-weekly-why-the-winner-of-a-leaderboard-is-overrated-and-by-how-much.png"
}
---
