---
{
 "layout": "story",
 "title": "Anthropic replaces git with its own version control system",
 "kind": "story",
 "section": "AI and machine learning",
 "edition": "daily",
 "edition_url": "/2026/10/14/daily/",
 "date": "2026-10-14 05:00:00 +0300",
 "summary": "Anthropic said daily merges to its monorepo rose from about 2,500 in May to over 30,000 in September, and that it migrated from git to an in-house system, Scion, in five months.",
 "body": [
  "Anthropic published an engineering post on 13 October describing why source control had become its main development bottleneck. The company said it averaged around 2,500 merged code changes a day in May 2026 and more than 30,000 a day by September. Its main-branch history is almost 100 GB, and it performs about 25 million code checkouts a day for continuous integration alone. At its peak it ran several hundred internal git mirrors to cope.",
  "Scion starts from the assumption that nearly all clients are agents and jobs that are always online. The server answers queries about history and blame and creates commits, merges and rebases, while clients keep a small cache and fetch only the files they need. Work is recorded as server-side changesets with content-addressed data, so servers need little coordination and scale horizontally.",
  "Anthropic reports that Scion’s infrastructure is 200 times smaller in CPU and memory than the git mirroring it replaced, that jobs check out code two orders of magnitude faster, and that continuous integration gained a 25% CPU capacity saving. A team of seven built Scion and a code review tool, called Antique, in five months. These figures are the company’s own."
 ],
 "why": "The post is a first-hand account of what agent-written code does to developer infrastructure.",
 "sources": [
  {
   "name": "Anthropic Engineering",
   "url": "https://www.anthropic.com/engineering/redesigning-source-control"
  }
 ],
 "published": "2026-10-13",
 "topics": [
  "AI industry",
  "Agents"
 ]
}
---
