#!/usr/bin/env python3
"""Precompute ICD10CM/NCIT ancestor paths for every mapped CURIE in the KB.

Writes `cache/<prefix>/hierarchy.csv` beside the existing label caches. The
renderer reads these first and only falls back to a live OAK walk on a miss, so
this turns ~75 s of SQLite traversal per page into a dictionary lookup
(issue #11186).

    just build-hierarchy-cache            # every strict-hierarchy prefix
    just build-hierarchy-cache NCIT       # one prefix
    uv run python scripts/build_hierarchy_cache.py --check   # CI: is it stale?

`--check` reports CURIEs that are mapped in `kb/` but absent from the cache and
exits non-zero. That is a staleness report, not a correctness gate: a miss costs
render time, never a wrong page, so nothing in `just qc` blocks on it.

The output is derived. Never hand-edit it — rerun this script.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import io
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from dismech import hierarchy_cache, oak_db
from dismech.render import (
    STRICT_HIERARCHIES,
    _build_hierarchy_path,
    _get_oak_adapter,
)
from dismech.yaml_io import safe_load


def mapped_curies(kb_root: Path) -> dict[str, set[str]]:
    """Collect every mapping CURIE in `kb/` whose prefix has a strict hierarchy."""
    found: dict[str, set[str]] = {prefix: set() for prefix in STRICT_HIERARCHIES}
    for path in sorted(kb_root.rglob("*.yaml")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        if "mappings:" not in text:
            continue
        try:
            data = safe_load(text)
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        mappings = data.get("mappings") or {}
        if not isinstance(mappings, dict):
            continue
        for mapping_list in mappings.values():
            if not isinstance(mapping_list, list):
                continue
            for mapping in mapping_list:
                if not isinstance(mapping, dict):
                    continue
                term = mapping.get("term") or {}
                if not isinstance(term, dict):
                    continue
                curie = term.get("id")
                if not isinstance(curie, str) or ":" not in curie:
                    continue
                prefix = curie.split(":", 1)[0]
                if prefix in found:
                    found[prefix].add(curie)
    return found


class MemoisingAdapter:
    """Wraps an OAK adapter so each parent/label lookup happens once per run.

    Terms in one vocabulary share most of their upper ancestry, so walking every
    mapped CURIE independently re-asks the same questions repeatedly. Against the
    2.7 GB NCIT build a single `hierarchical_parents` call costs seconds, which
    is the difference between this script taking half an hour and under a minute.
    """

    def __init__(self, adapter) -> None:
        self._adapter = adapter
        self._parents: dict[str, list[str]] = {}
        self._labels: dict[str, str] = {}
        self.parent_queries = 0
        self.label_queries = 0

    def hierarchical_parents(self, term_id: str) -> list[str]:
        if term_id not in self._parents:
            self.parent_queries += 1
            self._parents[term_id] = list(self._adapter.hierarchical_parents(term_id))
        return self._parents[term_id]

    def label(self, term_id: str) -> str:
        if term_id not in self._labels:
            self.label_queries += 1
            try:
                self._labels[term_id] = self._adapter.label(term_id) or term_id
            except Exception:
                self._labels[term_id] = term_id
        return self._labels[term_id]


def resolve(
    prefix: str, curies: set[str]
) -> tuple[dict[str, list[tuple[str, str]]], list[str]]:
    """Walk each CURIE to the vocabulary root. Returns (resolved, unresolved)."""
    hierarchy = STRICT_HIERARCHIES[prefix]
    # Check for the build before opening the adapter. semsql downloads a missing
    # one rather than failing, so `_get_oak_adapter(...) is None` would never be
    # true and this message would never print -- the operator would just watch
    # gigabytes arrive with no explanation.
    if not oak_db.local_build_present(hierarchy["adapter"]):
        raise SystemExit(
            f"no local SQLite build for {prefix} at "
            f"{oak_db.local_build_path(oak_db.adapter_build_name(hierarchy['adapter']) or '')}. "
            f"Fetch it with `just fetch-ontology-dbs {prefix.lower()}` first "
            "(rather than letting OAK download it mid-run)."
        )
    raw = _get_oak_adapter(hierarchy["adapter"])
    if raw is None:
        raise SystemExit(
            f"could not open the OAK adapter {hierarchy['adapter']!r} for {prefix}."
        )
    adapter = MemoisingAdapter(raw)

    resolved: dict[str, list[tuple[str, str]]] = {}
    unresolved: list[str] = []
    for index, curie in enumerate(sorted(curies), start=1):
        path = _build_hierarchy_path(adapter, curie, hierarchy["root"])
        if not path:
            unresolved.append(curie)
            continue
        resolved[curie] = [(node, adapter.label(node)) for node in path]
        print(
            f"  [{index}/{len(curies)}] {curie} -> {len(path)} nodes "
            f"({adapter.parent_queries} parent queries so far)",
            flush=True,
        )
    return resolved, unresolved


def existing_rows(path: Path) -> dict[str, dict[str, str]]:
    """Read the committed cache as raw rows, keyed by CURIE, timestamps included."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}
    return {
        row["curie"]: row
        for row in csv.DictReader(text.splitlines())
        if row.get("curie")
    }


def render_csv(
    resolved: dict[str, list[tuple[str, str]]],
    retrieved_at: str,
    previous: dict[str, dict[str, str]] | None = None,
) -> str:
    """Serialize the cache, keeping the existing timestamp on unchanged rows.

    A run that re-resolves every CURIE would otherwise restamp every row, so
    adding one mapping produces a whole-file diff and two PRs adding neighbouring
    CURIEs collide on every line. The sibling `cache/<prefix>/terms.csv` is
    incremental for the same reason, and the frozen dataset-accession cache is
    the cautionary tale for getting it wrong -- CLAUDE.md records that
    post-mortem, and names the file, which this comment deliberately does not.
    Only a row whose path or labels actually moved gets the new timestamp.
    """
    previous = previous or {}
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(hierarchy_cache.CACHE_HEADER)
    for curie in sorted(resolved):
        pairs = resolved[curie]
        curies = hierarchy_cache.join_field([node for node, _ in pairs])
        labels = hierarchy_cache.join_field([label for _, label in pairs])
        prior = previous.get(curie)
        unchanged = (
            prior is not None
            and prior.get("ancestor_curies") == curies
            and prior.get("ancestor_labels") == labels
            and prior.get("retrieved_at")
        )
        writer.writerow(
            [
                curie,
                curies,
                labels,
                prior["retrieved_at"] if unchanged else retrieved_at,
            ]
        )
    return buffer.getvalue()


def check(kb_root: Path, cache_root: Path) -> int:
    """Report mapped CURIEs missing from the committed cache."""
    stale = 0
    for prefix, curies in sorted(mapped_curies(kb_root).items()):
        if not curies:
            continue
        cached = hierarchy_cache.load_hierarchy_cache(prefix, str(cache_root))
        missing = sorted(curies - set(cached))
        print(f"{prefix}: {len(curies) - len(missing)}/{len(curies)} cached")
        for curie in missing:
            print(f"  MISSING {curie}")
        stale += len(missing)
    if stale:
        print(
            f"\n{stale} mapped CURIE(s) are not in the hierarchy cache. "
            "These still render, via a live OAK walk that costs ~1 s each. "
            "Run `just build-hierarchy-cache` to refresh."
        )
        return 1
    print("\nHierarchy cache is complete for every mapped CURIE.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "prefixes",
        nargs="*",
        help="Prefixes to rebuild (default: every strict-hierarchy prefix).",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report cache staleness without writing; exit 1 if anything is missing.",
    )
    args = parser.parse_args()

    kb_root = REPO_ROOT / "kb"
    cache_root = hierarchy_cache.default_cache_root()

    if args.check:
        return check(kb_root, cache_root)

    selected = args.prefixes or sorted(STRICT_HIERARCHIES)
    unknown = [p for p in selected if p not in STRICT_HIERARCHIES]
    if unknown:
        parser.error(
            f"unknown prefix(es) {unknown}; known: {sorted(STRICT_HIERARCHIES)}"
        )

    all_curies = mapped_curies(kb_root)
    retrieved_at = (
        datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat()
    )

    for prefix in selected:
        curies = all_curies.get(prefix, set())
        if not curies:
            print(f"{prefix}: no mapped CURIEs in kb/, nothing to cache")
            continue
        print(f"{prefix}: resolving {len(curies)} CURIE(s)...", flush=True)
        resolved, unresolved = resolve(prefix, curies)
        out = hierarchy_cache.cache_path(prefix, cache_root)
        previous = existing_rows(out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_csv(resolved, retrieved_at, previous), encoding="utf-8")
        print(f"  wrote {len(resolved)} path(s) to {out.relative_to(REPO_ROOT)}")
        for curie in unresolved:
            print(f"  unresolved (left to live lookup): {curie}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
