#!/usr/bin/env python3
"""
Upgrade `genetic[]` entries missing `gene_term` by looking up the bare gene
symbol in HGNC via OAK.

For each disorder YAML, walks `genetic[]` and `has_subtypes[*].genetic[]` and
adds a `gene_term` block populated from HGNC whenever:

- `gene_term.term.id` is absent, AND
- `name` resolves to exactly one HGNC CURIE via `sqlite:obo:hgnc`.

Entries whose `name` does not resolve (chromosomal aneuploidies, multi-word
disease classes, variant/allele strings, retired symbols, ambiguous matches)
are left untouched so the KGX exporter's strict mode (see #2099) drops them
deterministically.

Run with:

    uv run python scripts/upgrade_genetic_gene_terms.py             # dry-run, summary
    uv run python scripts/upgrade_genetic_gene_terms.py --apply     # write files
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from oaklib import get_adapter
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap


def resolve_symbol(adapter, symbol: str) -> tuple[str, str] | None:
    """Return (curie, label) for a unique HGNC match, else None."""
    if not symbol:
        return None
    curies = list(adapter.curies_by_label(symbol))
    if len(curies) != 1:
        return None
    curie = curies[0]
    label = adapter.label(curie) or symbol
    return curie, label


def build_gene_term(symbol: str, curie: str, label: str) -> CommentedMap:
    term = CommentedMap()
    term["id"] = curie
    term["label"] = label
    gene_term = CommentedMap()
    gene_term["preferred_term"] = symbol
    gene_term["term"] = term
    return gene_term


def iter_genetic_lists(data):
    """Yield each genetic[] list in a disorder document (top-level and subtypes)."""
    if not isinstance(data, dict):
        return
    if isinstance(data.get("genetic"), list):
        yield data["genetic"]
    for subtype in data.get("has_subtypes") or []:
        if isinstance(subtype, dict) and isinstance(subtype.get("genetic"), list):
            yield subtype["genetic"]


def upgrade_file(path: Path, adapter, apply: bool) -> tuple[int, int, list[str]]:
    """Returns (upgraded, unresolved, sample_unresolved_names)."""
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096

    with path.open() as f:
        data = yaml.load(f)

    upgraded = 0
    unresolved_names: list[str] = []

    for genetic in iter_genetic_lists(data):
        for entry in genetic:
            if not isinstance(entry, dict):
                continue
            existing = ((entry.get("gene_term") or {}).get("term") or {}).get("id")
            if existing:
                continue
            name = entry.get("name")
            if not isinstance(name, str):
                continue
            resolved = resolve_symbol(adapter, name)
            if resolved is None:
                unresolved_names.append(name)
                continue
            curie, label = resolved
            entry["gene_term"] = build_gene_term(name, curie, label)
            upgraded += 1

    if apply and upgraded:
        with path.open("w") as f:
            yaml.dump(data, f)

    return upgraded, len(unresolved_names), unresolved_names[:5]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Write changes to disk")
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[Path("kb/disorders")],
        help="Disorder YAML files or directories (default: kb/disorders)",
    )
    args = parser.parse_args(argv)

    targets: list[Path] = []
    for p in args.paths:
        if p.is_dir():
            targets.extend(sorted(p.glob("*.yaml")))
        else:
            targets.append(p)

    print(f"Loading HGNC adapter (sqlite:obo:hgnc)...", file=sys.stderr)
    adapter = get_adapter("sqlite:obo:hgnc")

    total_upgraded = 0
    total_unresolved = 0
    files_touched = 0
    for path in targets:
        upgraded, unresolved, samples = upgrade_file(path, adapter, args.apply)
        if upgraded or unresolved:
            files_touched += 1
            print(f"{path.name}: +{upgraded} resolved, {unresolved} unresolved {samples!r}")
        total_upgraded += upgraded
        total_unresolved += unresolved

    print()
    print(f"Files touched: {files_touched}")
    print(f"Entries upgraded: {total_upgraded}")
    print(f"Entries unresolved (will be dropped by exporter): {total_unresolved}")
    if not args.apply:
        print("(dry-run — re-run with --apply to write changes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
