"""Gate a time-sliced dismech entry: fail if it cites anything outside its packet,
mentions a banned post-cutoff term, keeps present-day subtype structure, or has a
pathophysiology node with no evidence.

Usage:
    uv run python experiments/diagnostic_retrodiction/check_cutoff.py \
        <entry.yaml> --packet <packet/packet.tsv> --banned <banned_terms.txt>
Exit code 0 = pass, 1 = fail. Prints one line per violation.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml


def walk(node, path=""):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from walk(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk(v, f"{path}[{i}]")
    else:
        yield path, node


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("entry", type=Path)
    ap.add_argument("--packet", required=True, type=Path)
    ap.add_argument("--banned", required=True, type=Path,
                    help="one term per line; matched case-insensitively as whole words")
    a = ap.parse_args()

    allowed = {l.split("\t")[0] for l in a.packet.read_text().splitlines()[1:] if l.strip()}
    banned = [t.strip() for t in a.banned.read_text().splitlines() if t.strip() and not t.startswith("#")]
    text = a.entry.read_text()
    data = yaml.safe_load(text)
    errors = []

    for path, val in walk(data):
        if isinstance(val, str) and re.fullmatch(r"PMID:\d+", val.strip()) and val.strip() not in allowed:
            errors.append(f"OUTSIDE_PACKET {val.strip()} at {path}")
        if isinstance(val, str) and re.match(r"^(DOI|NCT|PMC|URL|http)", val.strip(), re.I) and path.endswith("reference"):
            errors.append(f"NON_PMID_REFERENCE {val.strip()} at {path}")

    for term in banned:
        for m in re.finditer(rf"(?i)\b{re.escape(term)}\b", text):
            line = text.count("\n", 0, m.start()) + 1
            errors.append(f"BANNED_TERM '{term}' at line {line}")

    if data.get("has_subtypes"):
        errors.append("HAS_SUBTYPES present (strip present-day subtype structure)")

    for i, node in enumerate(data.get("pathophysiology") or []):
        if not node.get("evidence"):
            errors.append(f"UNSUPPORTED_NODE pathophysiology[{i}] '{node.get('name')}' has no evidence")

    for e in errors:
        print(e)
    print(f"{'FAIL' if errors else 'PASS'}: {len(errors)} violation(s) in {a.entry}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
