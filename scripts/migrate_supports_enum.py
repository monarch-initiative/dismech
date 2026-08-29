#!/usr/bin/env python3
"""Migrate ``EvidenceItem.supports`` to the narrowed direction enum (issue #7439).

``EvidenceItemSupportEnum`` used to mix three different kinds of claim in one
slot: which way the evidence cuts (SUPPORT / REFUTE), whether the citation bears
on the claim at all (NO_EVIDENCE), and whether a previous version of the entry
text was factually wrong (WRONG_STATEMENT). PARTIAL sat in the middle doing at
least four jobs at once. The narrowing keeps SUPPORT / REFUTE / NO_EVIDENCE and
adds a separate optional ``directness`` slot.

What this script does
---------------------
``PARTIAL`` becomes ``SUPPORT`` with ``directness`` left **absent**.

It is deliberately not backfilled to a value. ``directness`` is optional, and an
absent value reads as "nobody has assessed this", which is true of every evidence
item in the KB today. Defaulting the migrated items to ``INDIRECT`` would assert
11,000-odd appraisals that no curator made and no reviewer checked -- and PARTIAL
was not a synonym for indirect anyway. Sampling the curators' own ``explanation``
prose, the value was carrying at least four distinct meanings:

  * supports the claim, but through an inference step (INDIRECT)
  * right mechanism, inverted model system (INDIRECT)
  * supports one part of the claim and contradicts another (two items, wrongly
    merged into one -- wants splitting into a SUPPORT and a REFUTE)
  * true, cited, and not actually about this claim (NO_EVIDENCE)

Only a curator reading the snippet against the claim can tell those apart, so
every migrated item is written to a worklist TSV instead, and the assessment is
left as follow-up work.

Why a line edit and not a YAML round-trip
-----------------------------------------
Every ``supports: PARTIAL`` in ``kb/`` is the same single-line unquoted scalar,
so the value can be replaced textually. Round-tripping 1,100+ files through a
YAML writer would reflow folded scalars and reorder nothing usefully, and
``just check-folded-hyphens`` exists precisely because that reflowing corrupts
words. The file is parsed (read-only) to build the worklist, and edited as text.

YAML aliases mean one line can be several items
-----------------------------------------------
Some entries define an evidence list once with a YAML anchor and reuse it by
alias on several edges (``Apert_Syndrome.yaml`` has four ``supports: PARTIAL``
lines but six parsed items). The line edit handles this correctly -- rewriting
the anchor definition changes every alias -- and the worklist deliberately lists
each *location*, because directness is a property of the quote-and-claim pair,
not of the quote alone.

That also exposes a real limitation to note rather than fix here: an aliased
evidence item shares one object across several claims, so it cannot carry a
different ``directness`` for each. Assessing one of those items may mean
un-aliasing it first.

Prose is left alone
-------------------
About 4,130 lines of curator ``explanation`` text name PARTIAL directly ("Marked
PARTIAL because this is an fgfr3 loss-of-function zebrafish model..."). That
prose is the *reason* for the grade and is exactly what the follow-up directness
pass needs, so it is preserved verbatim and flagged in the worklist rather than
rewritten. Only the enum token is stale; the reasoning is still correct.

Usage::

    uv run python scripts/migrate_supports_enum.py --dry-run
    uv run python scripts/migrate_supports_enum.py --apply
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from datetime import UTC, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from dismech.yaml_io import safe_load

ROOT = Path(__file__).resolve().parent.parent
KB = ROOT / "kb"

#: The one textual shape ``supports: PARTIAL`` takes in kb/. Anchored so a
#: ``PARTIAL`` mentioned inside explanation prose can never match.
PARTIAL_LINE = re.compile(r"^(\s*supports:[ \t]*)PARTIAL[ \t]*$")

#: Prose that names the retired value, for the worklist's advisory column.
PROSE_MENTION = re.compile(r"\bPARTIAL(?:LY)?\b")

WORKLIST = ROOT / "docs" / "reports" / "data" / (
    f"partial-evidence-directness-worklist-{datetime.now(UTC).date().isoformat()}.tsv"
)


def iter_evidence(node, path=""):
    """Yield every dict that looks like an EvidenceItem, with its YAML-ish path."""
    if isinstance(node, dict):
        if "supports" in node and ("snippet" in node or "reference" in node):
            yield path, node
        for key, value in node.items():
            yield from iter_evidence(value, f"{path}.{key}" if path else key)
    elif isinstance(node, list):
        for index, item in enumerate(node):
            yield from iter_evidence(item, f"{path}[{index}]")


def collect(paths):
    """Build worklist rows for PARTIAL items, and count the other retired value."""
    rows = []
    wrong_statement = []
    for path in paths:
        try:
            data = safe_load(path.read_text())
        except Exception as exc:  # a malformed file is check-duplicate-keys' job
            print(f"  ! skipped (unparsable): {path.relative_to(ROOT)}: {exc}")
            continue
        for location, item in iter_evidence(data):
            supports = item.get("supports")
            rel = path.relative_to(ROOT).as_posix()
            if supports == "PARTIAL":
                explanation = (item.get("explanation") or "").strip()
                rows.append(
                    {
                        "file": rel,
                        "location": location,
                        "reference": item.get("reference") or "",
                        "evidence_source": item.get("evidence_source") or "",
                        "snippet": " ".join((item.get("snippet") or "").split()),
                        "explanation": " ".join(explanation.split()),
                        "explanation_names_partial": (
                            "yes" if PROSE_MENTION.search(explanation) else "no"
                        ),
                    }
                )
            elif supports == "WRONG_STATEMENT":
                wrong_statement.append((rel, location))
    return rows, wrong_statement


def rewrite(path: str | Path) -> int:
    """Replace ``supports: PARTIAL`` with ``supports: SUPPORT``; return the count."""
    path = Path(path)
    original = path.read_text()
    changed = 0
    out = []
    for line in original.splitlines(keepends=True):
        match = PARTIAL_LINE.match(line.rstrip("\n"))
        if match:
            newline = "\n" if line.endswith("\n") else ""
            out.append(f"{match.group(1)}SUPPORT{newline}")
            changed += 1
        else:
            out.append(line)
    if changed:
        path.write_text("".join(out))
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="report without writing")
    group.add_argument("--apply", action="store_true", help="rewrite files and worklist")
    args = parser.parse_args()

    paths = sorted(KB.rglob("*.yaml"))
    print(f"scanning {len(paths)} files under kb/ ...")
    rows, wrong_statement = collect(paths)

    print(f"\nPARTIAL evidence items:        {len(rows)}")
    named = sum(1 for r in rows if r["explanation_names_partial"] == "yes")
    print(f"  whose explanation says PARTIAL: {named}")
    print(f"WRONG_STATEMENT items:          {len(wrong_statement)}")
    for rel, location in wrong_statement:
        print(f"  ! {rel} :: {location}")
    if wrong_statement:
        print(
            "\n  WRONG_STATEMENT is NOT migrated automatically. Each use records that\n"
            "  an earlier version of the entry text was wrong, so the right direction\n"
            "  depends on whether that text has since been corrected. Fix by hand and\n"
            "  move the correction story to a history/ record."
        )

    if args.dry_run:
        print("\ndry run: nothing written")
        return 0

    WORKLIST.parent.mkdir(parents=True, exist_ok=True)
    with WORKLIST.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "file",
                "location",
                "reference",
                "evidence_source",
                "snippet",
                "explanation",
                "explanation_names_partial",
            ],
            delimiter="\t",
            quoting=csv.QUOTE_MINIMAL,
        )
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r: (r["file"], r["location"])))
    print(f"\nworklist -> {WORKLIST.relative_to(ROOT)}")

    total = 0
    touched = 0
    for path in paths:
        count = rewrite(path)
        if count:
            touched += 1
            total += count
    print(f"rewrote {total} supports: PARTIAL -> SUPPORT across {touched} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
