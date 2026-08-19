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

The single-exact-match rule is load-bearing: it is what keeps names like
"Trisomy 21", "SOD1 Mutations" and "HLA-DQB1*06:02" out of the backfill. Do
not loosen it to fuzzy/synonym matching.

Edits are applied as **line insertions into the original file text**, not as a
YAML round-trip dump, so the resulting diff is pure additions and carries no
incidental reflow or whitespace normalization of untouched content.

Run with:

    uv run python scripts/upgrade_genetic_gene_terms.py             # dry-run, summary
    uv run python scripts/upgrade_genetic_gene_terms.py --apply     # write files
    uv run python scripts/upgrade_genetic_gene_terms.py --apply kb/disorders/Asthma.yaml
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from oaklib import get_adapter
from ruamel.yaml import YAML


def resolve_symbol(adapter, symbol: str) -> tuple[str, str] | None:
    """Return (curie, label) for a unique HGNC match, else None.

    Matching is against HGNC's *primary* rdfs:label (the current approved gene
    symbol) only, and only when exactly one CURIE matches. Aliases, previous
    symbols and ambiguous names deliberately do not resolve, so a retired
    symbol is left for a human rather than being silently rewritten to a
    label that no longer matches the curated `name`.
    """
    if not symbol:
        return None
    curies = list(adapter.curies_by_label(symbol))
    if len(curies) != 1:
        return None
    curie = curies[0]
    # This repo's canonical CURIE form is lowercase `hgnc:` (see CLAUDE.md).
    # Refuse anything else rather than case-fixing it, so an adapter change
    # surfaces as a skipped entry instead of a silently rewritten identifier.
    if not curie.startswith("hgnc:"):
        return None
    label = adapter.label(curie)
    if not label:
        return None
    return curie, label


def render_gene_term(symbol: str, curie: str, label: str, indent: int) -> list[str]:
    """Render the gene_term block as YAML text lines at the given indent."""
    pad = " " * indent
    return [
        f"{pad}gene_term:",
        f"{pad}  preferred_term: {symbol}",
        f"{pad}  term:",
        f"{pad}    id: {curie}",
        f"{pad}    label: {label}",
    ]


def iter_genetic_lists(data):
    """Yield each genetic[] list in a disorder document (top-level and subtypes)."""
    if not isinstance(data, dict):
        return
    if isinstance(data.get("genetic"), list):
        yield data["genetic"]
    for subtype in data.get("has_subtypes") or []:
        if isinstance(subtype, dict) and isinstance(subtype.get("genetic"), list):
            yield subtype["genetic"]


def plan_insertion(entry) -> tuple[int, int] | None:
    """Return (line_index, indent) at which to insert a gene_term block.

    The block is placed immediately after `name`, matching the placement
    convention in hand-curated genetic[] entries. Positioning is derived from
    the key *after* `name` where one exists, which is exact even if the `name`
    scalar were to span several lines; only a single-key entry falls back to
    the line after `name` itself.
    """
    keys = list(entry.keys())
    if "name" not in keys:
        return None
    name_line, indent = entry.lc.key("name")
    after = keys[keys.index("name") + 1 :]
    for key in after:
        line, col = entry.lc.key(key)
        if col == indent and line > name_line:
            return line, indent
    return name_line + 1, indent


def upgrade_file(path: Path, adapter, apply: bool) -> tuple[int, int, list[str]]:
    """Returns (upgraded, unresolved_count, unresolved_names)."""
    yaml = YAML()
    yaml.preserve_quotes = True

    text = path.read_text()
    data = yaml.load(text)

    insertions: list[tuple[int, list[str]]] = []
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
            plan = plan_insertion(entry)
            if plan is None:
                unresolved_names.append(name)
                continue
            line, indent = plan
            curie, label = resolved
            insertions.append((line, render_gene_term(name, curie, label, indent)))

    if apply and insertions:
        lines = text.splitlines(keepends=True)
        # Apply bottom-up so earlier line indices stay valid.
        for line, block in sorted(insertions, key=lambda x: x[0], reverse=True):
            lines[line:line] = [b + "\n" for b in block]
        path.write_text("".join(lines))

    return len(insertions), len(unresolved_names), unresolved_names


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

    print("Loading HGNC adapter (sqlite:obo:hgnc)...", file=sys.stderr)
    adapter = get_adapter("sqlite:obo:hgnc")

    total_upgraded = 0
    total_unresolved = 0
    files_touched = 0
    for path in targets:
        upgraded, unresolved, names = upgrade_file(path, adapter, args.apply)
        if upgraded or unresolved:
            files_touched += 1
            print(f"{path.name}: +{upgraded} resolved, {unresolved} unresolved {names[:5]!r}")
        total_upgraded += upgraded
        total_unresolved += unresolved

    print()
    print(f"Files touched: {files_touched}")
    print(f"Entries upgraded: {total_upgraded}")
    print(f"Entries unresolved (will be dropped by exporter): {total_unresolved}")
    if not args.apply:
        print("(dry-run -- re-run with --apply to write changes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
