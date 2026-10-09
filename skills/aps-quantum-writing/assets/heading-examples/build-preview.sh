#!/usr/bin/env bash
set -eu
cd "$(dirname "$0")"
mkdir -p build
args=(-no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build)
# Optional only for isolated test environments. A normal TeX setup needs no variable.
if [ -n "${TEX_FORMAT:-}" ]; then args+=("-fmt=$TEX_FORMAT"); fi
for source in prl-chosen-headings prl-unheaded-opening prl-no-main-headings regular-production-preview nonprl-letter; do
  for pass in 1 2; do
    pdflatex "${args[@]}" "$source.tex" >"build/$source.pass$pass.stdout" 2>&1
  done
  printf '%s\n' "Built build/$source.pdf"
done
