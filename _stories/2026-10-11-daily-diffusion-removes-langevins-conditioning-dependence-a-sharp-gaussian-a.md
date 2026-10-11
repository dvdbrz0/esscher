---
{
 "layout": "story",
 "title": "Diffusion Removes Langevin’s Conditioning Dependence: A Sharp Gaussian Analysis",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/10/11/daily/",
 "date": "2026-10-11 05:00:00 +0300",
 "summary": "For Gaussian targets, tuned diffusion sampling avoids the condition-number penalty that Langevin methods pay; both rates are sharp.",
 "body": [
  "The paper compares diffusion-based sampling with Langevin methods on Gaussian target distributions, a setting where both can be analysed exactly.",
  "Tuned diffusion sampling reaches a 2-Wasserstein error of order \\(\\sqrt{d\\,\\lambda_{\\max}}\\,\\log N / N\\), while Langevin methods pay an extra factor of \\(\\sqrt{\\kappa}\\), the square root of the condition number. Both rates are shown to be sharp.",
  "The conclusion is that the noising process helps sampling itself, separately from any benefit it brings to learning."
 ],
 "authors": "Perbost et al.",
 "arxiv": "2610.12052",
 "tag": "Optimization",
 "topics": [
  "Optimization",
  "Probability"
 ],
 "math": true,
 "image": "/assets/og/2026-10-11-daily-diffusion-removes-langevins-conditioning-dependence-a-sharp-gaussian-a.png"
}
---
