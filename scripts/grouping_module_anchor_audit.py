#!/usr/bin/env python3
"""Measure the CONFORMS_TO_MODULE `#Node` anchor gap (dismech#9403).

A grouping's `CONFORMS_TO_MODULE` criterion is written as
``module_stem#Node Name``, but `dismech.groupings` matches on the **stem**
alone. So SATISFIED means "this member conforms to that module somewhere", not
"at the node the criterion names".

This script reports the size of that gap at the two levels that get confused
with each other:

* **per-leaf** — (member, criterion) pairs where the member conforms to the
  named module but not at the named node. Informative, but mostly *not*
  actionable: a miss on one arm of an ``OR`` whose sibling is satisfied is the
  disjunction working as designed.
* **per-block** — members whose whole criteria-block verdict would change if
  every anchor were honoured. This is the adjudication worklist.

Both are computed with the same evaluator the audit and the grouping pages use,
so the numbers cannot drift from the tooling.

Usage::

    uv run python scripts/grouping_module_anchor_audit.py            # summary
    uv run python scripts/grouping_module_anchor_audit.py --format tsv
    uv run python scripts/grouping_module_anchor_audit.py --closure  # slow/online

Term-valued leaves (HP/GO/inheritance) default to exact matching rather than
ontology-closure matching so a run is offline and deterministic. Closure only
ever turns other leaves from NOT_SATISFIED to SATISFIED, so the per-block count
reported offline is a **lower bound**; pass ``--closure`` to get the online
number.
"""

from __future__ import annotations

import argparse
import glob
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from dismech.groupings import (
    GROUPINGS_DIR,
    evaluate_grouping,
    load_disease_index,
    set_closure_enabled,
)
from dismech.yaml_io import safe_load


def collect(paths: list[str]) -> tuple[list[tuple], list[tuple]]:
    """Return (leaf_rows, block_rows) over the given grouping files."""
    index = load_disease_index()
    leaf_rows: list[tuple] = []
    block_rows: list[tuple] = []

    for path in paths:
        with open(path) as f:
            grouping = safe_load(f)
        if not isinstance(grouping, dict):
            continue
        name = str(grouping.get("name") or Path(path).stem)
        for ev in evaluate_grouping(grouping, index):
            for miss in ev.anchor_misses:
                leaf_rows.append((name, ev.member, ev.criteria_index, miss))
            if ev.anchor_exact_result is not None:
                block_rows.append(
                    (
                        name,
                        ev.member,
                        ev.criteria_index,
                        ev.semantics or "-",
                        ev.result.value,
                        ev.anchor_exact_result.value,
                    )
                )
    return leaf_rows, block_rows


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "paths", nargs="*", help="Grouping YAML files (default: all of kb/groupings/)."
    )
    parser.add_argument(
        "--format",
        choices=("summary", "tsv"),
        default="summary",
        help="summary (default) or machine-readable TSV.",
    )
    parser.add_argument(
        "--closure",
        action="store_true",
        help=(
            "Evaluate term-valued leaves over the ontology subsumption closure. "
            "Requires ontology adapters; slower and non-offline."
        ),
    )
    args = parser.parse_args(argv)

    set_closure_enabled(args.closure)
    paths = args.paths or sorted(glob.glob(str(GROUPINGS_DIR / "*.yaml")))
    leaf_rows, block_rows = collect(paths)

    if args.format == "tsv":
        print(
            "level\tgrouping\tmember\tcriteria_index\tdetail\tverdict_today\tverdict_anchored"
        )
        for name, member, ci, miss in leaf_rows:
            print(f"leaf\t{name}\t{member}\t{ci}\t{miss}\t\t")
        for name, member, ci, semantics, today, anchored in block_rows:
            print(f"block\t{name}\t{member}\t{ci}\t{semantics}\t{today}\t{anchored}")
        return 0

    closure_note = "ontology closure ON" if args.closure else "exact terms (offline)"
    print(f"=== CONFORMS_TO_MODULE #Node anchor audit ({closure_note}) ===")
    print(f"  groupings scanned: {len(paths)}")
    print()
    print(f"  per-leaf anchor misses:  {len(leaf_rows)}")
    for name, count in sorted(
        Counter(r[0] for r in leaf_rows).items(), key=lambda kv: (-kv[1], kv[0])
    ):
        print(f"    {count:4d}  {name}")
    print()
    print(f"  per-block verdict flips: {len(block_rows)}")
    for name, member, ci, semantics, today, anchored in block_rows:
        print(
            f"    {name} / {member} [criteria {ci} {semantics}]: {today} -> {anchored}"
        )
    print()
    print(
        "  Per-leaf is informative; per-block is the adjudication worklist. A leaf\n"
        "  miss under an OR whose sibling passes does not move the block verdict."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
