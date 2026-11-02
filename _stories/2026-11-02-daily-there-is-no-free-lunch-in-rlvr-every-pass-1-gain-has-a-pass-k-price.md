---
{
 "layout": "story",
 "title": "There Is No Free Lunch in RLVR: Every pass@1 Gain Has a pass@k Price",
 "kind": "paper",
 "section": "Papers",
 "edition": "daily",
 "edition_url": "/2026/11/02/daily/",
 "date": "2026-11-02 05:00:00 +0300",
 "summary": "Modelling reinforcement learning as an exponential tilt of a base policy, the paper proves that first-try gains cost success on other prompts and force a crossover at large sampling budgets \\(k\\).",
 "body": [
  "Reinforcement learning with verifiable rewards makes a language model solve more problems on the first try, yet the base model overtakes it when both may sample \\(k\\) times. Liu asks whether this reversal is a transient or a price, and models the update as an exponential tilt of a base policy over strategies shared across prompts.",
  "Under exclusive specialisation, every update that raises pass@1 strictly lowers success on some prompt, and a strictly positive price on prompts, from Stiemke duality, is the exact condition. When the loss reaches the hardest prompts, a pass@k crossover is forced. The number of crossings is bounded by the sign variation of the shift in per-prompt success. Removing the crossover costs the whole pass@1 gain.",
  "The conclusion, stated by the author, is that this form of training moves along a reasoning frontier without widening it. The result bears directly on test-time schemes that sample many answers, though it is a single-author preprint and rests on the tilt model."
 ],
 "published": "2026-10-29",
 "authors": "Liu",
 "arxiv": "2610.39295",
 "tag": "Reasoning and inference",
 "topics": [
  "Reasoning and inference",
  "Learning theory"
 ],
 "math": true,
 "summary_plain": "Modelling reinforcement learning as an exponential tilt of a base policy, the paper proves that first-try gains cost success on other prompts and force a crossover at large sampling budgets k.",
 "image": "/assets/og/2026-11-02-daily-there-is-no-free-lunch-in-rlvr-every-pass-1-gain-has-a-pass-k-price.png"
}
---
