#!/usr/bin/env python3
"""Worklist and backfill for ``CriteriaItem.attaches_to``.

A criterion inside ``definitions[]`` used to reach the phenotype it tests for
only through a shared CURIE. ``attaches_to`` now names the phenotype directly.
Many existing criteria can be linked mechanically: their ``term`` is the
``phenotype_term`` of exactly one phenotype in the same entry and their wording
is that phenotype's. A shared term alone is a candidate, not an answer.

Each criterion without ``attaches_to`` is reported as one of:

``EXACT``
    Exactly one phenotype carries the criterion's term, under the same
    wording: the criterion's ``preferred_term`` is the phenotype's ``name``
    or ``preferred_term``, ignoring case. ``--apply`` writes
    ``attaches_to: [phenotypes#<name>]`` for these and nothing else.
``TERM_ONLY``
    Exactly one phenotype carries the term, under different wording. The
    candidate is listed, not written: a shared CURIE does not show that the
    phenotype row says what the criterion says. NMOSD's "Acute myelitis"
    criterion and its "Longitudinally Extensive Transverse Myelitis"
    phenotype share ``HP:0012486``, and the phenotype is the narrower one.
``AMBIGUOUS``
    Several phenotypes carry the term, usually rows stratified by subtype.
    A person picks.
``NO_MATCH``
    No phenotype carries the term. Either the entry lacks the phenotype, or
    one of the two bindings is wrong; both are worth a look.
``NO_TERM``
    The criterion has no term. It may still correspond to a phenotype, or to
    a biochemical or histopathology record, but only a reader can say which.

``--apply`` inserts lines of text rather than round-tripping the file through a
YAML library, which would reflow quoting and folded scalars across the whole
entry. An item is written only when its ``preferred_term`` and ``term.id`` pair
appears in the ``definitions`` block exactly as many times as the worklist has
EXACT criteria with that pair; anything else is skipped with a message.

Usage
-----
    python scripts/criteria_item_refs.py                     # summary, whole KB
    python scripts/criteria_item_refs.py --format tsv
    python scripts/criteria_item_refs.py kb/disorders/X.yaml --apply
"""

from __future__ import annotations

import argparse
import re
import sys
import textwrap
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.definition_criteria import attaches_to_candidates
from dismech.yaml_io import safe_load

DEFAULT_ROOTS = ("kb/disorders", "kb/modules", "kb/comorbidities")
STATUSES = ("EXACT", "TERM_ONLY", "AMBIGUOUS", "NO_MATCH", "NO_TERM")


def iter_paths(paths: list[str]) -> list[Path]:
    if paths:
        return [Path(p) for p in paths]
    out: list[Path] = []
    for root in DEFAULT_ROOTS:
        out.extend(sorted((ROOT / root).glob("*.yaml")))
    return out


def _display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def _definitions_span(lines: list[str]) -> tuple[int, int] | None:
    """Line range of the top-level ``definitions:`` block, end exclusive."""
    start = next(
        (i for i, line in enumerate(lines) if line.rstrip() == "definitions:"), None
    )
    if start is None:
        return None
    # The KB style writes list items at the key's own indent (`definitions:`
    # then `- name:` in column 0), so the block ends at the next top-level
    # key, not at the next column-0 line.
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if _TOP_LEVEL_KEY.match(lines[i]):
            end = i
            break
    return start + 1, end


_TOP_LEVEL_KEY = re.compile(r"^[A-Za-z_][\w-]*:")


_DASH = re.compile(r"^(\s*)- ")


def _item_blocks(lines: list[str], start: int, end: int):
    """Yield (dash_line, block_end, indent, parsed) for each list item in a span."""
    for i in range(start, end):
        match = _DASH.match(lines[i])
        if not match:
            continue
        indent = len(match.group(1))
        j = i + 1
        while j < end:
            line = lines[j]
            if line.strip() and (len(line) - len(line.lstrip())) <= indent:
                break
            j += 1
        while j > i + 1 and not lines[j - 1].strip():
            j -= 1
        block = textwrap.dedent("".join(lines[i:j]))
        try:
            parsed = yaml.safe_load(block)
        except yaml.YAMLError:
            continue
        if (
            isinstance(parsed, list)
            and len(parsed) == 1
            and isinstance(parsed[0], dict)
        ):
            yield i, j, indent, parsed[0]


def _key(item: dict) -> tuple[str, str] | None:
    term = item.get("term")
    if not isinstance(term, dict) or not isinstance(item.get("preferred_term"), str):
        return None
    if not isinstance(term.get("id"), str):
        return None
    return item["preferred_term"], term["id"]


def _yaml_scalar(value: str) -> str:
    dumped = yaml.safe_dump(
        value, default_flow_style=True, allow_unicode=True, width=10_000
    )
    return dumped.strip().removesuffix("...").strip()


def apply_file(path: Path, ready) -> int:
    """Write ``attaches_to`` for the EXACT criteria in one file; return how many."""
    want: Counter = Counter()
    ref_for: dict[tuple[str, str], str] = {}
    for cand in ready:
        key = _key(cand.site.item)
        if key is None:
            continue
        want[key] += 1
        ref_for[key] = cand.ref

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    span = _definitions_span(lines)
    if span is None:
        return 0

    found: dict[tuple[str, str], list[tuple[int, int]]] = {}
    for dash, block_end, indent, item in _item_blocks(lines, *span):
        key = _key(item)
        if key in want and not item.get("attaches_to"):
            found.setdefault(key, []).append((block_end, indent))

    inserts: list[tuple[int, str]] = []
    for key, count in want.items():
        sites = found.get(key, [])
        if len(sites) != count:
            print(
                f"  skip: {_display(path)}: {key[0]!r} ({key[1]}) matched "
                f"{len(sites)} item(s) in the text, expected {count}",
                file=sys.stderr,
            )
            continue
        for block_end, indent in sites:
            pad = " " * (indent + 2)
            inserts.append(
                (block_end, f"{pad}attaches_to:\n{pad}- {_yaml_scalar(ref_for[key])}\n")
            )

    for at, chunk in sorted(inserts, reverse=True):
        lines.insert(at, chunk)
    if inserts:
        path.write_text("".join(lines), encoding="utf-8")
    return len(inserts)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("paths", nargs="*")
    parser.add_argument("--format", choices=("summary", "tsv"), default="summary")
    parser.add_argument(
        "--apply", action="store_true", help="write attaches_to for the EXACT criteria"
    )
    args = parser.parse_args(argv)

    totals: Counter = Counter()
    per_file: dict[Path, list] = {}
    if args.format == "tsv":
        print("file\tpath\tstatus\tpreferred_term\tterm_id\tref\tphenotypes")
    for path in iter_paths(args.paths):
        data = safe_load(path.read_text(encoding="utf-8")) or {}
        cands = attaches_to_candidates(data)
        if not cands:
            continue
        per_file[path] = cands
        for cand in cands:
            totals[cand.status] += 1
            if args.format == "tsv":
                term = cand.site.item.get("term") or {}
                print(
                    "\t".join(
                        [
                            _display(path),
                            cand.site.path,
                            cand.status,
                            str(cand.site.item.get("preferred_term", "")),
                            str(term.get("id", "") if isinstance(term, dict) else ""),
                            cand.ref,
                            "; ".join(cand.matches),
                        ]
                    )
                )

    if args.format == "summary":
        print(f"Criteria without attaches_to, across {len(per_file)} file(s):")
        for status in STATUSES:
            print(f"  {status:<10} {totals[status]}")
        ranked = sorted(
            per_file.items(),
            key=lambda kv: -sum(c.status == "EXACT" for c in kv[1]),
        )
        shown = [(p, c) for p, c in ranked if any(x.status == "EXACT" for x in c)][:15]
        if shown:
            print("\nMost EXACT criteria:")
            for path, cands in shown:
                n = sum(c.status == "EXACT" for c in cands)
                print(f"  {n:>3}  {_display(path)}")

    if args.apply:
        written = 0
        for path, cands in per_file.items():
            ready = [c for c in cands if c.status == "EXACT"]
            if ready:
                written += apply_file(path, ready)
        print(f"\nWrote attaches_to on {written} criterion item(s).", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
