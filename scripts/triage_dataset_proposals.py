#!/usr/bin/env python3
"""Review and record triage decisions on a dataset proposal file.

Accession verification proves a dataset *exists*; it cannot prove the dataset is
about the disease it is being filed under. That judgement is the one step in the
dataset pipeline that stays human (or at least model-in-the-loop), because the
failure it prevents -- a real, resolvable accession attached to a sibling
disease -- is invisible to every other check in the stack.

    # print a compact review table
    uv run python scripts/triage_dataset_proposals.py show proposals/batch1.json

    # record rejections, with a reason kept in the file for the PR write-up
    uv run python scripts/triage_dataset_proposals.py reject proposals/batch1.json \\
        --accession geo:GSE219154 --reason "NSAID-induced urticaria, not acquired C1-INH angioedema"
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def show(path: Path, only_pending: bool) -> int:
    data = json.loads(path.read_text())
    n_rec = n_rej = 0
    for entry in data:
        recs = entry["records"]
        if only_pending:
            recs = [r for r in recs if r.get("approved")]
        if not recs:
            continue
        print(f"\n### {entry['slug']}  ({entry['disease_name']})")
        for r in recs:
            rec = r["record"]
            flag = " " if r.get("approved") else "REJECTED"
            n_rec += 1
            n_rej += 0 if r.get("approved") else 1
            print(f"  {flag:9s} {rec['accession']:<18} [{r.get('score')}] "
                  f"{rec.get('data_type', '?'):<24} n={rec.get('sample_count', '?')}")
            print(f"            {rec['title'][:150]}")
            if r.get("reject_reason"):
                print(f"            -> {r['reject_reason']}")
    print(f"\n{n_rec} records shown, {n_rej} rejected", file=sys.stderr)
    return 0


def reject(path: Path, accessions: list[str], reason: str) -> int:
    data = json.loads(path.read_text())
    hit = 0
    targets = set(accessions)
    for entry in data:
        for r in entry["records"]:
            if r["record"]["accession"] in targets:
                r["approved"] = False
                r["reject_reason"] = reason
                hit += 1
                print(f"  rejected {r['record']['accession']} ({entry['slug']})")
    path.write_text(json.dumps(data, indent=2) + "\n")
    missing = targets - {r["record"]["accession"] for e in data for r in e["records"]}
    for m in sorted(missing):
        print(f"  WARN not found in proposals: {m}", file=sys.stderr)
    print(f"{hit} record(s) rejected")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("show")
    s.add_argument("proposals", type=Path)
    s.add_argument("--all", action="store_true", help="include already-rejected records")

    r = sub.add_parser("reject")
    r.add_argument("proposals", type=Path)
    r.add_argument("--accession", action="append", required=True)
    r.add_argument("--reason", required=True)

    args = ap.parse_args()
    if args.cmd == "show":
        return show(args.proposals, only_pending=not args.all)
    return reject(args.proposals, args.accession, args.reason)


if __name__ == "__main__":
    sys.exit(main())
