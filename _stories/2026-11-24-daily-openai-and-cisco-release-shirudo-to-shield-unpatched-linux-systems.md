---
{
 "layout": "story",
 "title": "OpenAI and Cisco release Shirudo to shield unpatched Linux systems",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/11/24/daily/",
 "date": "2026-11-24 05:00:00 +0300",
 "summary": "The open-source runtime lets operators load signed eBPF programs that block a vulnerable code path in a running system while a patch is prepared, without a restart.",
 "body": [
  "OpenAI and Cisco released Shirudo on 23 November under a BSD 2-Clause licence. It attaches small eBPF programs, called shields, at points inside the Linux kernel to block the behaviour an exploit needs while leaving legitimate requests through. Operators can watch how a shield would affect applications before enforcing it; shields are cryptographically signed and checked by the kernel’s eBPF verifier, and a Trusted Platform Module keeps a record of what was loaded or removed.",
  "In a controlled test, a shield generated with Codex added an input check to Java’s Base64 decoder inside a running Elasticsearch process and rejected an exploit attempt without taking the service down. The companies say agents should eventually investigate a vulnerability, write a shield and validate it, with security teams approving deployment.",
  "The release follows OpenAI’s report on 4 November that its cyber model produced 948 working local privilege-escalation exploits for Linux in one run costing about $1.2m, a rate of discovery that patching has struggled to match."
 ],
 "sources": [
  {
   "name": "OpenAI: Shirudo",
   "url": "https://openai.com/index/introducing-shirudo/"
  },
  {
   "name": "OpenAI: A thousand fewer paths to root",
   "url": "https://openai.com/index/a-thousand-fewer-paths-to-root/"
  }
 ],
 "published": "2026-11-23",
 "topics": [
  "Agents",
  "AI industry"
 ],
 "image": "/assets/og/2026-11-24-daily-openai-and-cisco-release-shirudo-to-shield-unpatched-linux-systems.png"
}
---
