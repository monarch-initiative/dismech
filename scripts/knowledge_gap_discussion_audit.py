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
import io
import re
import sys
from collections import Counter
from collections.abc import Iterator
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
    "RESOLVED_NO_DATE",
    "RETIRED_GRADE_PROSE",
)

#: States that are breakage rather than backlog, and so gate under ``--strict``.
_STRICT_STATES = ("BARE_EXPERIMENT_TARGET", "RESOLVED_NO_NOTE")

#: The retired ``PARTIAL`` grade as a whole word. A bare substring test also
#: fires on "PARTIALLY", which is ordinary prose and not a retired enum value.
_RETIRED_GRADE = re.compile(r"\bPARTIAL\b")


def _iter_evidence(discussion: dict) -> "Iterator[dict]":
    """Every evidence item under one discussion, at any depth.

    Discussion-level ``evidence`` is only part of it: a proposed experiment
    carries its own, and so does each of its readouts and perturbations. A
    census that reads only the top level reports a floor rather than a count.
    """
    for item in discussion.get("evidence") or []:
        if isinstance(item, dict):
            yield item
    for experiment in discussion.get("proposed_experiments") or []:
        if not isinstance(experiment, dict):
            continue
        for item in experiment.get("evidence") or []:
            if isinstance(item, dict):
                yield item
        for slot in ("perturbations", "readouts"):
            for child in experiment.get(slot) or []:
                if not isinstance(child, dict):
                    continue
                for item in child.get("evidence") or []:
                    if isinstance(item, dict):
                        yield item


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
    n_undecidable: int = 0
    states: list[str] = field(default_factory=list)
    detail: list[str] = field(default_factory=list)
    decision_slots: list[str] = field(default_factory=list)


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
        if discussion.get("status") == "RESOLVED":
            if not discussion.get("resolution_note"):
                gap.states.append("RESOLVED_NO_NOTE")
            # Reported, never gated: unlike the note, a date cannot be
            # reconstructed by whoever notices it is missing.
            if not discussion.get("resolved_date"):
                gap.states.append("RESOLVED_NO_DATE")

        undecidable = [
            str(e.get("experiment_id") or e.get("name") or "?")
            for e in experiments
            if not any(e.get(slot) for slot in _DECISION_SLOTS)
        ]
        gap.n_undecidable = len(undecidable)
        for experiment in experiments:
            gap.decision_slots.extend(
                slot for slot in _DECISION_SLOTS if experiment.get(slot)
            )
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
                        label = (
                            experiment.get("experiment_id")
                            or experiment.get("name")
                            or "?"
                        )
                        gap.detail.append(f"bare target in {label}.{slot}: {target!r}")

        if any(
            _RETIRED_GRADE.search(str(item.get("explanation") or ""))
            for item in _iter_evidence(discussion)
        ):
            gap.states.append("RETIRED_GRADE_PROSE")
        gaps.append(gap)
    return gaps


def collect(root: Path, paths: list[Path] | None = None) -> list[Gap]:
    files = paths or _kb_files(root)
    gaps: list[Gap] = []
    for path in files:
        gaps.extend(audit_entry(path, root))
    return gaps


def summary_text(gaps: list[Gap]) -> str:
    """The census, as text.

    Emits the experiment-level figures too -- the undecidable share and the
    decision-slot table -- so a report citing them can say "regenerate with
    this command" and be telling the truth.
    """
    counts = Counter(state for gap in gaps for state in set(gap.states))
    files = {gap.path for gap in gaps}
    experiments = sum(gap.n_experiments for gap in gaps)
    undecidable = sum(gap.n_undecidable for gap in gaps)
    lines = [
        f"KNOWLEDGE_GAP discussions: {len(gaps)} across {len(files)} entries",
        f"  with proposed experiments: {sum(1 for g in gaps if g.n_experiments)}",
        f"  with evidence:             {sum(1 for g in gaps if g.n_evidence)}",
        "",
        f"  {'count':>6}  {'entries':>7}  state",
        f"  {'-' * 6}  {'-' * 7}  {'-' * 24}",
    ]
    for state in STATES:
        entries = len({gap.path for gap in gaps if state in gap.states})
        lines.append(f"  {counts.get(state, 0):>6}  {entries:>7}  {state}")
    clean = sum(1 for gap in gaps if not gap.states)
    lines += ["", f"  complete (no state above): {clean}", ""]

    share = f"{undecidable / experiments:.0%}" if experiments else "n/a"
    lines += [
        f"Proposed experiments: {experiments}",
        f"  with no decision logic: {undecidable} ({share})",
        "",
        f"  {'used by':>7}  decision slot",
        f"  {'-' * 7}  {'-' * 24}",
    ]
    slot_counts = Counter()
    for gap in gaps:
        slot_counts.update(gap.decision_slots)
    for slot, n in slot_counts.most_common():
        lines.append(f"  {n:>7}  {slot}")
    return "\n".join(lines)


def list_text(gaps: list[Gap]) -> str:
    """One block per gap: its states, location, prompt and per-state detail.

    Filtering happens in :func:`main`, so every format narrows identically.
    """
    lines: list[str] = []
    for i, gap in enumerate(sorted(gaps, key=lambda g: (g.path, g.discussion_id)), 1):
        lines.append(
            f"{i:4d}. [{','.join(gap.states)}] {gap.path} :: {gap.discussion_id}"
        )
        lines.append(f"      {gap.prompt[:150]}")
        lines.extend(f"      - {line}" for line in gap.detail)
    return "\n".join(lines)


def tsv_text(gaps: list[Gap]) -> str:
    """The per-gap table, as text, so every format shares one output path."""
    buffer = io.StringIO()
    writer = csv.writer(buffer, delimiter="\t", lineterminator="\n")
    writer.writerow(
        [
            "path",
            "discussion_id",
            "status",
            "n_experiments",
            "n_evidence",
            "n_undecidable",
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
                gap.n_undecidable,
                ";".join(gap.states),
                ";".join(gap.detail),
                gap.prompt,
            ]
        )
    return buffer.getvalue().rstrip("\n")


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
        help=(
            "restrict the report to gaps in this state; applies to every format "
            "except summary, which always counts the whole corpus"
        ),
    )
    parser.add_argument(
        "--out",
        type=Path,
        help="write the report to this file instead of stdout, in any format",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="print one OK/FAIL line instead of the report; for use as a gate",
    )
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
    broken = [g for g in gaps if any(s in g.states for s in _STRICT_STATES)]

    if args.format == "summary":
        selected = gaps
    elif args.state:
        selected = [g for g in gaps if args.state in g.states]
    else:
        selected = [g for g in gaps if g.states]

    if args.quiet:
        report = None
    elif args.format == "tsv":
        report = tsv_text(selected)
    elif args.format == "list":
        report = list_text(selected)
    else:
        report = summary_text(gaps)

    if report is not None:
        if args.out:
            args.out.write_text(report + "\n")
            print(f"Wrote {args.out}", file=sys.stderr)
        else:
            print(report)

    if args.strict:
        if broken:
            for gap in broken:
                print(
                    f"{gap.path} :: {gap.discussion_id}: {','.join(gap.states)}",
                    file=sys.stderr,
                )
                for line in gap.detail:
                    print(f"  - {line}", file=sys.stderr)
            print(
                f"FAIL: {len(broken)} knowledge gap(s) in {', '.join(_STRICT_STATES)}",
                file=sys.stderr,
            )
            return 1
        if args.quiet:
            print(
                f"OK: no {' or '.join(_STRICT_STATES)} in "
                f"{len(gaps)} KNOWLEDGE_GAP discussion(s)."
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
