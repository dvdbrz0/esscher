---
{
 "layout": "story",
 "title": "Postgres 19 slips because language models find bugs faster than people fix them",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/11/02/daily/",
 "date": "2026-11-02 05:00:00 +0300",
 "summary": "Robert Haas, a PostgreSQL committer, blames AI-reported bugs for the late release. Back-patched commits rose by more than 60% between feature freeze and 25 September.",
 "body": [
  "PostgreSQL major versions have shipped between mid-September and mid-October for a decade. Version 19 will most likely arrive in November, and three large features were reverted between 27 August and 15 September. Robert Haas, a long-standing committer who works at Databricks, says the cause is language models.",
  "His evidence is commit counts over the same window each year. Commits to the release branch rose from 724 in 2025 to 1,169 in 2026, and commits to the previous stable branch from 248 to 433, a rise of more than 74%. He attributes this to people reporting bugs they found with language models. Fixes can be drafted by models, but humans must still review them, and that work took time away from reviewing the release.",
  "Haas calls the delay itself minor. The harder question he poses is how a project with 40 years of accumulated bugs catches up with tools that find them far more cheaply than they can be fixed."
 ],
 "why": "It is a measured account of AI changing the cost of finding bugs relative to fixing them in a major code base.",
 "sources": [
  {
   "name": "Robert Haas",
   "url": "https://rhaas.blogspot.com/2026/10/postgres-19-is-late-and-its-ais-fault.html"
  }
 ],
 "published": "2026-10-30",
 "topics": [
  "Agents",
  "AI industry"
 ],
 "image": "/assets/og/2026-11-02-daily-postgres-19-slips-because-language-models-find-bugs-faster-than-people.png"
}
---
