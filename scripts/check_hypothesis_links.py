#!/usr/bin/env python3
"""Guard the two path conventions that attach a hypothesis exploration to its entry.

A hypothesis exploration lives at ``kb/hypotheses/<slug>/<hypothesis_id>/`` and
reaches its disease page through ``render.collect_hypothesis_research_links``,
which does exactly two lookups and has no fallback for either:

1. ``hypotheses_root / disorder_slug`` -- the directory name must equal the
   **filename stem of the kb entry**. If it does not, the function returns ``[]``
   immediately and *every* report under that directory is invisible on the page.
2. ``hypothesis_lookup[hypothesis_dir.name]`` -- the subdirectory name must equal
   a ``mechanistic_hypotheses[].hypothesis_group_id`` declared by that entry. If
   it does not, the section still renders but with a label derived from the
   directory name and **no status**, detached from the hypothesis it explored.

Both failures are silent everywhere else. The reports validate, the assessment
sidecars validate, the entry validates, the page builds, and `just qc` is green.
Nothing in the repo compares a hypothesis directory against a kb entry, so the
drift is only visible by rendering the page and noticing an absence.

It is drift by construction, because the directory is named once, at run time,
from the free-text ``disease_name`` the runner was invoked with, while the entry
filename and the hypothesis ids are curated afterwards and keep moving:

* ``Huntington's Disease`` slugified to ``Huntingtons_Disease``; the entry is
  ``Huntington_Disease.yaml``. Four OpenScientist reports were unreachable.
* ``Metastatic_Pancreatic_Adenocarcinoma`` was folded into
  ``Pancreatic_Ductal_Adenocarcinoma`` per design decisions section 3a, which
  moved the hypothesis ids to the parent and left the directory behind. Two more
  reports unreachable.
* ``canonical_hmgcs2_ketogenesis_failure_model`` was renamed to
  ``canonical_human_hmgcs2_ketogenesis_failure`` in the entry by PR #6565; the
  directory kept the old id and its report rendered detached.

So the natural lifecycle of an entry -- rename it, fold it into a parent, rename
one of its hypotheses -- breaks this link without touching the hypothesis tree at
all. That is why this runs whole-KB and ungated rather than as a path-filtered
test: the PR that breaks it is a PR that never opens ``kb/hypotheses/``.
"""

from __future__ import annotations

import argparse
import difflib
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

KB_SUBDIRS = ("disorders", "modules", "comorbidities", "groupings")


@dataclass(frozen=True)
class Finding:
    kind: str  # "no_entry" | "undeclared_id"
    directory: str
    detail: str
    fix: str


def _entry_paths(kb_root: Path) -> dict[str, Path]:
    """Map every kb entry filename stem to its path."""
    entries: dict[str, Path] = {}
    for sub in KB_SUBDIRS:
        for path in sorted((kb_root / sub).glob("*.yaml")):
            entries.setdefault(path.stem, path)
    return entries


def _declared_ids(entry_path: Path) -> set[str]:
    data = yaml.safe_load(entry_path.read_text(encoding="utf-8")) or {}
    return {
        str(h["hypothesis_group_id"])
        for h in (data.get("mechanistic_hypotheses") or [])
        if isinstance(h, dict) and h.get("hypothesis_group_id")
    }


def _has_report(hypothesis_dir: Path) -> bool:
    """A directory only reaches the page if it holds a non-citations report."""
    return any(
        not p.name.endswith(".citations.md") for p in hypothesis_dir.glob("*.md")
    )


def collect(repo_root: Path) -> list[Finding]:
    kb_root = repo_root / "kb"
    hyp_root = kb_root / "hypotheses"
    if not hyp_root.is_dir():
        return []
    entries = _entry_paths(kb_root)
    findings: list[Finding] = []
    id_cache: dict[str, set[str]] = {}

    for disease_dir in sorted(p for p in hyp_root.iterdir() if p.is_dir()):
        slug = disease_dir.name
        entry = entries.get(slug)
        if entry is None:
            reports = sum(
                1 for d in disease_dir.iterdir() if d.is_dir() and _has_report(d)
            )
            near = difflib.get_close_matches(slug, entries, n=1, cutoff=0.8)
            hint = f" Closest entry: {near[0]!r}." if near else ""
            findings.append(
                Finding(
                    "no_entry",
                    f"kb/hypotheses/{slug}/",
                    f"no kb entry named {slug!r}; "
                    f"{reports} hypothesis report directory/ies are unreachable "
                    f"from any disease page.{hint}",
                    "rename the directory to the entry's filename stem, or "
                    "delete it if the entry was retired",
                )
            )
            continue

        if slug not in id_cache:
            id_cache[slug] = _declared_ids(entry)
        declared = id_cache[slug]

        for hypothesis_dir in sorted(p for p in disease_dir.iterdir() if p.is_dir()):
            if not _has_report(hypothesis_dir):
                continue
            if hypothesis_dir.name in declared:
                continue
            listed = ", ".join(sorted(declared)) if declared else "(none declared)"
            findings.append(
                Finding(
                    "undeclared_id",
                    f"kb/hypotheses/{slug}/{hypothesis_dir.name}/",
                    f"{entry.relative_to(repo_root).as_posix()} declares no "
                    f"hypothesis_group_id {hypothesis_dir.name!r}; the report "
                    f"renders detached, with a derived label and no status. "
                    f"Entry declares: {listed}",
                    "rename the directory to the entry's current "
                    "hypothesis_group_id (ids get renamed by curation)",
                )
            )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root", type=Path, default=Path("."), help="repository root"
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="print findings but always exit 0 (census mode)",
    )
    args = parser.parse_args()

    findings = collect(args.repo_root.resolve())
    if not findings:
        print(
            "OK: every hypothesis directory resolves to a kb entry and a "
            "declared hypothesis_group_id."
        )
        return 0

    print("Hypothesis exploration(s) disconnected from their kb entry.\n")
    print(
        "`render.collect_hypothesis_research_links` matches directory names\n"
        "verbatim against the entry filename stem and against the entry's\n"
        "declared hypothesis_group_id values. There is no fuzzy fallback, and a\n"
        "mismatch is silent: reports, sidecars, the entry and the page all still\n"
        "validate. The symptom is an ABSENCE on the rendered page, so it is only\n"
        "found by looking for it.\n"
    )

    no_entry = [f for f in findings if f.kind == "no_entry"]
    undeclared = [f for f in findings if f.kind == "undeclared_id"]

    if no_entry:
        print(f"-- {len(no_entry)} directory/ies naming no kb entry --")
        print("   Every report beneath these is invisible on every disease page.\n")
        for f in no_entry:
            print(f"  {f.directory}")
            print(f"     {f.detail}")
            print(f"     fix: {f.fix}\n")
    if undeclared:
        print(f"-- {len(undeclared)} directory/ies naming an undeclared hypothesis --")
        print("   These render, but detached from the hypothesis they explored.\n")
        for f in undeclared:
            print(f"  {f.directory}")
            print(f"     {f.detail}")
            print(f"     fix: {f.fix}\n")

    print(f"{len(findings)} finding(s).")
    return 0 if args.report else 1


if __name__ == "__main__":
    sys.exit(main())
