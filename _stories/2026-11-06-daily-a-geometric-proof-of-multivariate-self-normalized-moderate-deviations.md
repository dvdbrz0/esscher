---
{
 "layout": "story",
 "title": "A geometric proof of multivariate self-normalized moderate deviations via ridge regularization",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/06/daily/",
 "date": "2026-11-06 05:00:00 +0300",
 "summary": "A Cramér-type moderate deviation theorem for a self-normalised radius statistic in \\(\\mathbb{R}^d\\) holds for every \\(a_n = o(n^{1/6})\\) under only a finite third moment.",
 "body": [
  "Take i.i.d. vectors \\(X_j\\) in \\(\\mathbb{R}^d\\) with mean zero, identity covariance and \\(\\mathbb{E}\\|X\\|^3 < \\infty\\). With \\(S_n = \\sum_j X_j\\) and \\(A_n = \\sum_j X_j X_j^\\top\\), the statistic is \\(U_{n,+}^2 = S_n^\\top A_n^+ S_n\\), where \\(A_n^+\\) is the Moore–Penrose inverse. The theorem states that for every \\(a_n = o(n^{1/6})\\), \\[\\sup_{0 \\le x \\le a_n} \\left| \\frac{\\mathbb{P}(U_{n,+} \\ge x)}{\\mathbb{P}(\\chi_d \\ge x)} - 1 \\right| \\to 0.\\]",
  "The same result holds for the Hotelling \\(T^2\\) statistic, which closes the gap between the known \\((3+\\delta)\\)-moment condition and the third-moment boundary. The proof is geometric. It truncates at the third-moment scale, averages uniform projected moderate deviations over directions, turns them into a spherical cap transform of the radial law after a whitening map with a ridge term, and recovers the radial tail by a local Abel inversion."
 ],
 "published": "2026-11-04",
 "authors": "Jing et al.",
 "arxiv": "2611.05822",
 "tag": "Probability",
 "topics": [
  "Probability"
 ],
 "math": true,
 "summary_plain": "A Cramér-type moderate deviation theorem for a self-normalised radius statistic in ℝᵈ holds for every aₙ = o(n^(1/6)) under only a finite third moment.",
 "image": "/assets/og/2026-11-06-daily-a-geometric-proof-of-multivariate-self-normalized-moderate-deviations.png"
}
---
