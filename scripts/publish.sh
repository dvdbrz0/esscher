#!/usr/bin/env bash
# Commit and push everything an edition or a correction produces.
# Usage: bash scripts/publish.sh "Daily brief 2026-10-12"
set -euo pipefail
cd "$(dirname "$0")/.."
msg="${1:?give a commit message}"
git config user.name "dvdbrz0"
git config user.email "dvdbrz0@users.noreply.github.com"
git add -A _posts _stories _includes/charts assets/og
if git diff --cached --quiet; then
  echo "publish.sh: nothing to publish"
  exit 0
fi
git commit -q -m "$msg"
if ! git push -q origin main; then
  echo "publish.sh: push rejected, rebasing once"
  git pull -q --rebase origin main
  git push -q origin main
fi
echo "publish.sh: pushed \"$msg\""
git log --oneline -1
