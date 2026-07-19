#!/usr/bin/env python3
"""Report disorders whose references/evidence lack a reference title.

Two structures carry a human-readable publication title:
- Top-level ``references:`` entries are ``PublicationReference`` objects and use
  the ``title`` slot.
- Inlined ``evidence:`` entries are ``EvidenceItem`` objects and use the
  ``reference_title`` slot.

This walks every kb/disorders/*.yaml file and reports, per file, how many of
each are missing their title (blank/absent counts as missing).
"""

import sys
from pathlib import Path

import yaml

DISORDERS = Path("kb/disorders")


def is_blank(v) -> bool:
    return v is None or (isinstance(v, str) and not v.strip())


def walk(node, missing_ev, missing_ref):
    """Recursively collect evidence items and publication references missing titles.

    missing_ev: list of (reference) for EvidenceItem lacking reference_title
    missing_ref: list of (reference) for PublicationReference lacking title
    """
    if isinstance(node, dict):
        for key, val in node.items():
            if key == "evidence" and isinstance(val, list):
                for item in val:
                    if isinstance(item, dict) and "reference" in item:
                        if is_blank(item.get("reference_title")):
                            missing_ev.append(item.get("reference"))
            elif key == "references" and isinstance(val, list):
                for item in val:
                    if isinstance(item, dict) and "reference" in item:
                        if is_blank(item.get("title")):
                            missing_ref.append(item.get("reference"))
            # recurse into every value regardless (evidence/references nest deeply)
            walk(val, missing_ev, missing_ref)
    elif isinstance(node, list):
        for item in node:
            walk(item, missing_ev, missing_ref)


def main():
    rows = []
    for path in sorted(DISORDERS.glob("*.yaml")):
        data = yaml.safe_load(path.read_text())
        if data is None:
            continue
        missing_ev, missing_ref = [], []
        walk(data, missing_ev, missing_ref)
        if missing_ev or missing_ref:
            rows.append(
                (path.name, len(missing_ev), len(missing_ref), missing_ev, missing_ref)
            )

    total_files = len(list(DISORDERS.glob("*.yaml")))
    print(f"Scanned {total_files} disorder files.")
    print(f"Files with at least one missing title: {len(rows)}\n")
    print(f"{'file':<55} {'ev_missing':>10} {'ref_missing':>11}")
    print("-" * 78)
    ev_total = ref_total = 0
    for name, ne, nr, _, _ in rows:
        ev_total += ne
        ref_total += nr
        print(f"{name:<55} {ne:>10} {nr:>11}")
    print("-" * 78)
    print(f"{'TOTALS':<55} {ev_total:>10} {ref_total:>11}")

    if "--details" in sys.argv:
        print("\n=== Detail: references cited without a title ===")
        for name, ne, nr, mev, mref in rows:
            print(f"\n{name}:")
            if mev:
                print(
                    f"  evidence (no reference_title): {', '.join(str(r) for r in mev)}"
                )
            if mref:
                print(f"  references (no title): {', '.join(str(r) for r in mref)}")


if __name__ == "__main__":
    main()
