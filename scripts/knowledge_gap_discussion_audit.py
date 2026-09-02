#!/usr/bin/env python3
"""Audit the completeness of ``KNOWLEDGE_GAP`` discussions across the KB.

A knowledge gap is curated as a ``discussions[]`` entry with
``kind: KNOWLEDGE_GAP`` (design decisions defer the structural ``knowledge_gaps:``
slot, so ``discussions`` is where a gap lives today). The prose half of such an
entry -- the ``prompt`` and ``rationale`` -- is what a curator reads, and it is
consistently good. The *structural* half is not, and nothing in ``just qc`` looks
at it: a gap that anchors to nothing, or proposes an experiment with no way to
tell a supporting result from a refuting one, validates and renders exactly like
a complete one.

Six states are counted per gap, each independently reportable:

* ``UNANCHORED``      -- no ``attaches_to``. The gap is not attached to any node,
  so it never reaches the pathograph or the attached-node facet of the
  discussions browser. ``CLAUDE.md`` supplies the empty-anchor idiom
  (``prevalence#``, ``progression#``, ``clinical_burden#``) for a gap about a
  whole section, so "there was nothing to point at" is rarely the real answer.
* ``NO_STATUS``       -- no ``status``. ``DiscussionStatusEnum`` is what
  distinguishes an open gap from a resolved or archived one, and the export
  renders the value; absent, a gap cannot be filtered as open.
* ``UNDECIDABLE_EXPERIMENT`` -- a ``proposed_experiments[]`` entry carrying only
  ``experiment_id``/``name``/``description``: no ``decision_criterion``, no
  ``would_support``/``would_refute``, no ``supporting_outcome``/
  ``refuting_outcome``, no ``readouts``. The Experiment class exists to say what
  result would settle the question; without any of those slots the proposal is
  a paragraph of prose in a structured slot.
* ``BARE_EXPERIMENT_TARGET`` -- a ``perturbations[]``/``readouts[]`` ``target``
  written as a bare node name rather than ``<kind>#<name>``. This is the silent
  one: ``check-entity-refs`` skips a ``target`` with no ``#`` (the slot carries
  bare names in its pathograph homes), and ``check-causal-targets`` excludes
  experiment readouts outright, so nothing in the repo sees it.
* ``RESOLVED_NO_NOTE`` -- ``status: RESOLVED`` with no ``resolution_note``.
* ``RETIRED_GRADE_PROSE`` -- an evidence ``explanation`` still arguing for the
  retired ``PARTIAL`` grade (#10003 migrated the values, not the prose).

Report-only by design, like ``environmental-term-audit``: most of these are a
pre-existing backlog rather than a defect introduced by the change in front of
you, and a gate that goes red on 900 grandfathered rows teaches nothing.
``--strict`` exits non-zero on the two states that are unambiguous breakage
(``BARE_EXPERIMENT_TARGET``, ``RESOLVED_NO_NOTE``) so a targeted lane can use it.

Usage::

    uv run python scripts/knowledge_gap_discussion_audit.py
    uv run python scripts/knowledge_gap_discussion_audit.py --format list --state UNANCHORED
    uv run python scripts/knowledge_gap_discussion_audit.py --format tsv --out gaps.tsv
    uv run python scripts/knowledge_gap_discussion_audit.py --strict
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO_ROOT / "src"))

# Imported after the sys.path insertion above, so it resolves from src/.
from dismech.yaml_io import safe_load_path  # noqa: E402

#: KB subtrees whose entries may carry ``discussions:``.
_KB_GLOBS = (
    "kb/disorders/*.yaml",
    "kb/modules/*.yaml",
    "kb/comorbidities/*.yaml",
    "kb/groupings/*.yaml",
)

#: Slots any one of which makes a proposed experiment decidable.
_DECISION_SLOTS = (
    "decision_criterion",
    "would_support",
    "would_refute",
    "supporting_outcome",
    "refuting_outcome",
    "readouts",
)

#: The states this audit reports, in the order they are printed.
STATES = (
    "UNANCHORED",
    "NO_STATUS",
    "UNDECIDABLE_EXPERIMENT",
    "BARE_EXPERIMENT_TARGET",
    "RESOLVED_NO_NOTE",
    "RETIRED_GRADE_PROSE",
)

#: States that are breakage rather than backlog, and so gate under ``--strict``.
_STRICT_STATES = ("BARE_EXPERIMENT_TARGET", "RESOLVED_NO_NOTE")


@dataclass
class Gap:
    """One ``kind: KNOWLEDGE_GAP`` discussion and what it is missing."""

    path: str
    slug: str
    discussion_id: str
    prompt: str
    status: str
    n_experiments: int
    n_evidence: int
    states: list[str] = field(default_factory=list)
    detail: list[str] = field(default_factory=list)


def _kb_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for pattern in _KB_GLOBS:
        files.extend(
            p for p in root.glob(pattern) if not p.name.endswith(".history.yaml")
        )
    return sorted(files)


def audit_entry(path: Path, root: Path) -> list[Gap]:
    """Every knowledge gap in one loaded entry, with its states filled in."""
    data = safe_load_path(path) or {}
    if not isinstance(data, dict):
        return []
    slug = path.stem
    rel = str(path.relative_to(root))
    gaps: list[Gap] = []
    for discussion in data.get("discussions") or []:
        if not isinstance(discussion, dict):
            continue
        if discussion.get("kind") != "KNOWLEDGE_GAP":
            continue
        experiments = [
            e
            for e in (discussion.get("proposed_experiments") or [])
            if isinstance(e, dict)
        ]
        evidence = [
            e for e in (discussion.get("evidence") or []) if isinstance(e, dict)
        ]
        gap = Gap(
            path=rel,
            slug=slug,
            discussion_id=str(discussion.get("discussion_id") or ""),
            prompt=" ".join(str(discussion.get("prompt") or "").split()),
            status=str(discussion.get("status") or ""),
            n_experiments=len(experiments),
            n_evidence=len(evidence),
        )
        if not discussion.get("attaches_to"):
            gap.states.append("UNANCHORED")
        if not discussion.get("status"):
            gap.states.append("NO_STATUS")
        if discussion.get("status") == "RESOLVED" and not discussion.get(
            "resolution_note"
        ):
            gap.states.append("RESOLVED_NO_NOTE")

        undecidable = [
            str(e.get("experiment_id") or e.get("name") or "?")
            for e in experiments
            if not any(e.get(slot) for slot in _DECISION_SLOTS)
        ]
        if undecidable:
            gap.states.append("UNDECIDABLE_EXPERIMENT")
            gap.detail.extend(f"undecidable experiment: {name}" for name in undecidable)

        for experiment in experiments:
            for slot in ("perturbations", "readouts"):
                for item in experiment.get(slot) or []:
                    if not isinstance(item, dict):
                        continue
                    target = item.get("target")
                    if target and "#" not in str(target):
                        if "BARE_EXPERIMENT_TARGET" not in gap.states:
                            gap.states.append("BARE_EXPERIMENT_TARGET")
                        gap.detail.append(
                            f"bare target in {experiment.get('experiment_id')}.{slot}: "
                            f"{target!r}"
                        )

        if any("PARTIAL" in str(item.get("explanation") or "") for item in evidence):
            gap.states.append("RETIRED_GRADE_PROSE")
        gaps.append(gap)
    return gaps


def collect(root: Path, paths: list[Path] | None = None) -> list[Gap]:
    files = paths or _kb_files(root)
    gaps: list[Gap] = []
    for path in files:
        gaps.extend(audit_entry(path, root))
    return gaps


def print_summary(gaps: list[Gap]) -> None:
    counts = Counter(state for gap in gaps for state in set(gap.states))
    files = {gap.path for gap in gaps}
    experiments = sum(gap.n_experiments for gap in gaps)
    print(f"KNOWLEDGE_GAP discussions: {len(gaps)} across {len(files)} entries")
    print(f"  with proposed experiments: {sum(1 for g in gaps if g.n_experiments)}")
    print(f"  with evidence:             {sum(1 for g in gaps if g.n_evidence)}")
    print(f"  proposed experiments:      {experiments}")
    print()
    print(f"  {'count':>6}  {'entries':>7}  state")
    print(f"  {'-' * 6}  {'-' * 7}  {'-' * 24}")
    for state in STATES:
        entries = len({gap.path for gap in gaps if state in gap.states})
        print(f"  {counts.get(state, 0):>6}  {entries:>7}  {state}")
    print()
    clean = sum(1 for gap in gaps if not gap.states)
    print(f"  complete (no state above): {clean}")


def print_list(gaps: list[Gap], state: str | None) -> None:
    selected = [g for g in gaps if (state in g.states if state else g.states)]
    for i, gap in enumerate(
        sorted(selected, key=lambda g: (g.path, g.discussion_id)), 1
    ):
        print(f"{i:4d}. [{','.join(gap.states)}] {gap.path} :: {gap.discussion_id}")
        print(f"      {gap.prompt[:150]}")
        for line in gap.detail:
            print(f"      - {line}")


def write_tsv(gaps: list[Gap], out: Path | None) -> None:
    handle = out.open("w", newline="") if out else sys.stdout
    try:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(
            [
                "path",
                "discussion_id",
                "status",
                "n_experiments",
                "n_evidence",
                "states",
                "detail",
                "prompt",
            ]
        )
        for gap in gaps:
            writer.writerow(
                [
                    gap.path,
                    gap.discussion_id,
                    gap.status,
                    gap.n_experiments,
                    gap.n_evidence,
                    ";".join(gap.states),
                    ";".join(gap.detail),
                    gap.prompt,
                ]
            )
    finally:
        if out:
            handle.close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "files",
        nargs="*",
        type=Path,
        help="KB files to audit (default: every kb/ entry that may carry discussions)",
    )
    parser.add_argument(
        "--format",
        choices=("summary", "list", "tsv"),
        default="summary",
        help="summary census (default), per-gap list, or a TSV table",
    )
    parser.add_argument(
        "--state",
        choices=STATES,
        help="with --format list, show only gaps in this state",
    )
    parser.add_argument("--out", type=Path, help="write to this file instead of stdout")
    parser.add_argument(
        "--strict",
        action="store_true",
        help=(
            "exit 1 on a state that is breakage rather than backlog "
            f"({', '.join(_STRICT_STATES)})"
        ),
    )
    args = parser.parse_args(argv)

    gaps = collect(_REPO_ROOT, [p.resolve() for p in args.files] or None)

    if args.format == "tsv":
        write_tsv(gaps, args.out)
        if args.out:
            print(f"Wrote {args.out}", file=sys.stderr)
    elif args.format == "list":
        print_list(gaps, args.state)
    else:
        print_summary(gaps)

    if args.strict:
        broken = [g for g in gaps if any(s in g.states for s in _STRICT_STATES)]
        if broken:
            print(
                f"\nFAIL: {len(broken)} knowledge gap(s) in "
                f"{', '.join(_STRICT_STATES)}",
                file=sys.stderr,
            )
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
