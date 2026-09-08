#!/bin/bash
# Build the HTML and PDF versions of a report from report/<name>.md.
# Usage: build_report.sh [name]  (default: impactor-confidence-report)
# Requires pandoc and Google Chrome (headless). Run from the repo root.
set -e
cd "$(dirname "$0")/.."
name="${1:-impactor-confidence-report}"
pandoc "report/$name.md" -f markdown -t html5 --standalone --columns=2000 \
  --css report/report.css --embed-resources \
  -o "report/$name.html"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$PWD/report/$name.pdf" "file://$PWD/report/$name.html" >/dev/null 2>&1
echo "wrote report/$name.pdf"
