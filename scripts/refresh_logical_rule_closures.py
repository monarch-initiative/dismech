#!/usr/bin/env python3
"""Regenerate the descendant closures ``conf/logical_rules.yaml`` reads.

``check_logical_rules.py`` has to answer "is ``CL:0000186 myofibroblast`` a
connective tissue cell?" for every cell type in the KB, on every CI run, on a
runner with no ontology build and no reason to hit the network. So the answers
are precomputed here and committed under ``cache/closure/``, the same bargain
``cache/enums/*.csv`` strikes for dynamic-enum membership.

One file per closure root, named for the root (``CL_0002320.csv``) and sorted
by CURIE, so a refresh produces a reviewable diff rather than a reordering. The
root itself is not written as a row -- the reader adds it, since every closure
is reflexive.

Only ``is_a`` is traversed. ``part_of`` would pull in terms that are parts of a
connective tissue cell rather than kinds of one, and the rules ask about kinds.

    python scripts/refresh_logical_rule_closures.py            # all roots
    python scripts/refresh_logical_rule_closures.py --check    # CI: is it stale?
"""

from __future__ import annotations

import argparse
import csv
import io
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import yaml
from oaklib import get_adapter
from oaklib.datamodels.vocabulary import IS_A

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.logical_rules import (  # noqa: E402
    DEFAULT_CLOSURE_DIR,
    DEFAULT_RULES_PATH,
    closure_filename,
    load_rules,
)

OAK_CONFIG = ROOT / "conf" / "oak_config.yaml"
FIELDS = ("curie", "label", "root", "retrieved_at")

#: Concurrent label lookups. Enough to hide OLS latency without hammering it.
LABEL_WORKERS = 16


def adapter_for(prefix: str) -> str:
    """Resolve a CURIE prefix to the adapter ``conf/oak_config.yaml`` names.

    Going through the shared config rather than hardcoding ``ols:cl`` keeps
    this script on the same ontology sources as term validation, so a future
    migration of a prefix moves both at once.
    """
    config = yaml.safe_load(OAK_CONFIG.read_text(encoding="utf-8")) or {}
    adapters = config.get("ontology_adapters") or {}
    adapter = adapters.get(prefix)
    if not adapter:
        raise SystemExit(
            f"{OAK_CONFIG}: no adapter for prefix {prefix!r}; add one before "
            "writing a rule against that ontology"
        )
    return str(adapter)


def descendants(root: str) -> list[tuple[str, str]]:
    """Return ``(curie, label)`` for every is_a descendant of *root*.

    Labels are fetched concurrently. Against an ``ols:`` adapter each one is
    its own HTTP round trip -- about three quarters of a second -- and the
    rules need roughly 1,250 of them, so serial fetching turns a one-minute
    refresh into a quarter-hour one. The traversal itself is a single call and
    is left alone.
    """
    prefix = root.split(":", 1)[0]
    adapter = get_adapter(adapter_for(prefix))
    curies = sorted(
        curie
        for curie in adapter.descendants([root], predicates=[IS_A])
        if curie != root and curie.startswith(f"{prefix}:")
    )
    with ThreadPoolExecutor(max_workers=LABEL_WORKERS) as pool:
        labels = list(pool.map(lambda curie: adapter.label(curie) or "", curies))
    return list(zip(curies, labels))


def render(rows: list[tuple[str, str]], root: str, stamp: str) -> str:
    """Serialize one closure file. Goes through csv so labels carrying a comma
    (``CL:0002343 decidual natural killer cell, human``) are quoted."""
    out = io.StringIO()
    writer = csv.writer(out, lineterminator="\n")
    writer.writerow(FIELDS)
    for curie, label in rows:
        writer.writerow([curie, label, root, stamp])
    return out.getvalue()


def existing_rows(path: Path) -> list[tuple[str, str]]:
    if not path.is_file():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return [
            ((row.get("curie") or "").strip(), (row.get("label") or "").strip())
            for row in csv.DictReader(handle)
        ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rules", type=Path, default=DEFAULT_RULES_PATH)
    parser.add_argument("--closure-dir", type=Path, default=DEFAULT_CLOSURE_DIR)
    parser.add_argument(
        "--check",
        action="store_true",
        help="report drift and exit 1 instead of rewriting the cache",
    )
    args = parser.parse_args()

    rules = load_rules(args.rules)
    roots = list(dict.fromkeys(r for rule in rules for r in rule.closure_roots))
    args.closure_dir.mkdir(parents=True, exist_ok=True)

    stale: list[str] = []
    for root in roots:
        path = args.closure_dir / closure_filename(root)
        rows = descendants(root)
        if args.check:
            if rows != existing_rows(path):
                stale.append(root)
            continue
        # Keep the previous timestamp when the membership is unchanged, so a
        # no-op refresh does not churn every row's `retrieved_at`.
        stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        if rows == existing_rows(path) and path.is_file():
            print(f"unchanged {path.relative_to(ROOT)} ({len(rows)} descendants)")
            continue
        path.write_text(render(rows, root, stamp), encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)} ({len(rows)} descendants)")

    if args.check:
        if stale:
            print("Closure cache is stale for: " + ", ".join(stale))
            print("Run `just refresh-logical-rule-closures` and commit the result.")
            return 1
        print(f"OK: {len(roots)} closure(s) match the ontologies.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
