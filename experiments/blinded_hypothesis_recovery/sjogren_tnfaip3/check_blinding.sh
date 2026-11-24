#!/usr/bin/env bash
# Fail if any prompt input names the reference hypothesis.
set -euo pipefail
here=$(dirname "$0")
files=("$here"/../template.md "$here"/existing_mechanism.txt "$here"/existing_genetics.txt "$here"/focus_blind.txt "$here"/focus_semi.txt)
for f in "${files[@]}"; do
    [[ -f "$f" ]] || { echo "Missing prompt input: $f" >&2; exit 1; }
done
forbidden='TNFAIP3|A20|NF-?κ?k?B|NF-kappa|ubiquitin|deubiquitin|OTUD|30662920|30067782|24159176|26445930|rs2230926'
if grep -E -i -n "$forbidden" "${files[@]}"; then
    echo "Blinding violated" >&2
    exit 1
fi
echo "Blinding OK (${#files[@]} files)"
