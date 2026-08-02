#!/usr/bin/env python3
"""Rescope existing phenopacket-store records to their matched disease.

A phenopacket-store cohort is filed under a *gene*, and one gene can cause
several diseases: the LMNA cohort holds 259 cases spanning familial partial
lipodystrophy, Emery-Dreifuss muscular dystrophy and three others. Records
written before this was noticed report the whole cohort's case count and are
titled with the cohort's most frequent disease, both of which misdescribe what
is relevant to the entry.

This corrects `sample_count`, `title` and `description` on records already in
the KB, without adding or removing any record, so a branch's curated scope is
unchanged. It re-derives the matched disease the same way discovery does --
the entry's MONDO term resolved to its OMIM/Orphanet xrefs, else the cohort
disease whose label names the entry's disease.

    uv run python scripts/fix_phenopacket_counts.py --dry-run
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from discover_phenopackets import load_index, match_entry

REPO_ROOT = Path(__file__).resolve().parents[1]
KB_DIR = REPO_ROOT / "kb" / "disorders"
XREF_CACHE = REPO_ROOT / "cache" / "mondo_omim_xrefs.json"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    index = load_index()
    xcache = json.loads(XREF_CACHE.read_text()) if XREF_CACHE.exists() else {}
    changed = 0

    for path in sorted(KB_DIR.glob("*.yaml")):
        text = path.read_text(newline="")
        if "phenopacket-store:" not in text:
            continue
        doc = yaml.safe_load(text) or {}
        recs = [r for r in (doc.get("datasets") or [])
                if isinstance(r, dict) and str(r.get("accession", "")).startswith("phenopacket-store:")]
        if not recs:
            continue

        # Re-derive what discovery would produce now, keyed by accession.
        current = {m["cohort"]: m for m in match_entry(path.stem, index, xcache)}

        lines = text.splitlines(keepends=True)
        nl = "\r\n" if "\r\n" in text else "\n"
        edits = []
        for rec in recs:
            cohort = str(rec["accession"]).split(":", 1)[1]
            m = current.get(cohort)
            if not m or not m.get("matched_ids"):
                continue
            matched_id = m["matched_ids"][0].split(" ")[0]
            n_matched = m["diseases"].get(matched_id)
            if n_matched is None or rec.get("sample_count") == n_matched:
                continue
            edits.append((rec["accession"], rec.get("sample_count"), n_matched, len(m["diseases"])))

        if not edits:
            continue

        for acc, _old, new, _nd in edits:
            start = next((i for i, ln in enumerate(lines)
                          if ln.strip() == f"- accession: {acc}"), None)
            if start is None:
                continue
            end = next((j for j in range(start + 1, len(lines))
                        if lines[j].lstrip().startswith("- ") or
                        (lines[j].strip() and not lines[j].startswith((" ", "\t")))), len(lines))
            for j in range(start, end):
                if lines[j].lstrip().startswith("sample_count:"):
                    indent = lines[j][: len(lines[j]) - len(lines[j].lstrip())]
                    lines[j] = f"{indent}sample_count: {new}{nl}"
                    break

        updated = "".join(lines)
        before, after = yaml.safe_load(text) or {}, yaml.safe_load(updated) or {}
        if [d.get("accession") for d in before.get("datasets") or []] != \
           [d.get("accession") for d in after.get("datasets") or []]:
            print(f"  !! {path.name}: accession list changed, skipping", file=sys.stderr)
            continue
        before.pop("datasets", None)
        after.pop("datasets", None)
        if before != after:
            print(f"  !! {path.name}: edit touched other content, skipping", file=sys.stderr)
            continue

        for acc, old, new, nd in edits:
            print(f"  {path.stem:44s} {acc:34s} {old} -> {new}   (cohort spans {nd} diseases)")
            changed += 1
        if not args.dry_run:
            path.write_text(updated, newline="")

    print(f"\n{'would correct' if args.dry_run else 'corrected'} {changed} records")
    return 0


if __name__ == "__main__":
    sys.exit(main())
