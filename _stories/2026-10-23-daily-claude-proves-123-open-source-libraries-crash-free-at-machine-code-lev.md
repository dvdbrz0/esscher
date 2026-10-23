---
{
 "layout": "story",
 "title": "Claude proves 123 open-source libraries crash-free at machine-code level",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/10/23/daily/",
 "date": "2026-10-23 05:00:00 +0300",
 "summary": "Anthropic and Theorem turned fuzz tests into formal specifications and had Claude prove them for RISC-V binaries, finding hundreds of bugs that years of fuzzing had missed.",
 "body": [
  "Anthropic’s Frontier Red Team, working with the verification start-up Theorem, took fuzz tests from Google’s OSS-Fuzz programme and recast each one as a specification: the compiled RISC-V program exits normally, without a memory-safety error or failed assertion, for every input below 64 MB and every modelled operating-system response. Claude wrote the proofs and the Rocq proof checker verified them. The team says this is the first large-scale use of AI to verify production software at the assembly level.",
  "Attempting the proofs surfaced hundreds of bugs, including an out-of-bounds write that appears only on inputs of about 20 MB with one rare layout, out of reach for fuzzers that typically cap inputs at 1 MB. In one library Claude had to prove on machine code that libc++‘s red-black tree keeps its depth logarithmic. Separate experiments proved the Linux kernel’s zlib implementation against a Claude-written specification of RFC 1950.",
  "The guarantees are bounded. The proofs cover single-threaded static binaries linked against musl, not the dynamically linked x86 or ARM builds most people run, and AddressSanitizer does not catch every memory error. Anthropic is publishing a subset of the proofs and the machine semantics."
 ],
 "why": "If proofs become as cheap as fuzzing, the defence against AI-driven bug hunting changes from testing to guarantees.",
 "sources": [
  {
   "name": "Anthropic",
   "url": "https://www.anthropic.com/research/formal-verification"
  }
 ],
 "published": "2026-10-22",
 "topics": [
  "Reasoning and inference",
  "Large language models",
  "AI safety"
 ],
 "image": "/assets/og/2026-10-23-daily-claude-proves-123-open-source-libraries-crash-free-at-machine-code-lev.png"
}
---
