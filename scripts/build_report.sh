#!/bin/bash
# Build the HTML and PDF versions of the report from report/impactor-confidence-report.md.
# Requires pandoc and Google Chrome (headless). Run from the repo root.
set -e
cd "$(dirname "$0")/.."
pandoc report/impactor-confidence-report.md -f markdown -t html5 --standalone --columns=2000 \
  --css report/report.css --embed-resources --metadata pagetitle="Impactor confidence ranking" \
  -o report/impactor-confidence-report.html
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$PWD/report/impactor-confidence-report.pdf" "file://$PWD/report/impactor-confidence-report.html" >/dev/null 2>&1
echo "wrote report/impactor-confidence-report.pdf"
