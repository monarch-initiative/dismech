#!/usr/bin/env python3
"""Guard against two disorder entries claiming one ``disease_term`` (#10113).

Nothing else checks that a ``disease_term`` is used by only one entry. Two
curators can curate the same MONDO class from opposite directions under
different filenames; git sees two unrelated adds and every gate passes. That is
how #9618 nearly landed three duplicate entries.

Sharing a term is sometimes deliberate. Design decisions §3a lets a promoted
cancer stratum (EGFR-mutant NSCLC) anchor ``disease_term`` to its parent's MONDO
term when MONDO has no class for the stratum, provided the entry records
``skos:broadMatch`` to that term in ``mappings.mondo_mappings`` -- "never a bare
parent-term reuse presented as exact". SKOS mapping predicates read subject to
object, so the narrower stratum (the subject) records its broader parent as
``broadMatch``, not ``narrowMatch`` -- see CLAUDE.md's "Shared `disease_term`
anchors read subject to object". This script states that rule as a check:

    Every entry sharing a ``disease_term`` must carry a ``mondo_mappings`` row
    for that CURIE whose ``mapping_predicate`` is ``skos:exactMatch`` or
    ``skos:broadMatch``. At most one entry in the group may say exactMatch.

``skos:narrowMatch`` is also accepted on an existing entry: a number of
cancer strata and groupings were written under an earlier, internally
consistent but non-standard reading of the predicate (the entry describing its
own narrower/broader relationship to the mapped term, rather than the term's
relationship to the entry). New curation should write ``broadMatch``; migrating
the legacy ``narrowMatch`` rows is tracked separately (dismech#10165,
dismech#16243), not enforced here.

Zero exactMatch rows is legal: it means the parent rung has no entry of its own
yet (there is no ``Lung_Adenocarcinoma`` for the five lung-adenocarcinoma
strata). A missing row does not count as an exact claim. If it did, a group
with no parent entry would let one arbitrary stratum keep the exact claim, which
is the defect this check is for.

Finding classes, one per member and CURIE, so a new entry joining a
grandfathered group still fails:

``missing``
    The entry shares the term but records no ``mondo_mappings`` row for it.
``bad_predicate``
    It records a row, but with a predicate other than the permitted spellings
    (``skos:closeMatch``, or ``skos:narrowmatch`` in the wrong case).
    ``mapping_predicate`` is a ``uriorcurie`` with no enum, so nothing else
    catches this.
``conflicting``
    It records two or more rows for the same CURIE with different predicates.
``extra_exact``
    More than one entry in the group says exactMatch. Every claimant is
    reported, since the check cannot tell which one is right.

Scope is ``kb/disorders/`` only: a top-level ``disease_term`` does not occur in
``kb/modules/``, ``kb/comorbidities/`` or ``kb/groupings/``. The check is
cross-entry by nature, so it always reads the whole directory and takes no path
arguments.

Relationship to ``just check-granularity``
------------------------------------------
``scripts/check_granularity.py`` reports ``DUPLICATE_ANCHOR`` for infectious
entries (all entries under ``--scope all``) when an entry shares a term and has
no broadMatch (or legacy narrowMatch). That is report-only and weaker: it
accepts a bare shared term as long as one entry in the group has the anchor
predicate, and does not limit exact claims. This script is the gate.

Usage
-----
    python scripts/check_shared_disease_terms.py                 # gate
    python scripts/check_shared_disease_terms.py --report        # census, exit 0
    python scripts/check_shared_disease_terms.py --update-baseline
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, NamedTuple

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech import kb_cache
from dismech.kb_cache import load_document

BASELINE_PATH = ROOT / "tests" / "shared_disease_term_baseline.txt"
DISORDERS_DIR = ROOT / "kb" / "disorders"

EXACT = "skos:exactMatch"
BROAD = "skos:broadMatch"
NARROW = "skos:narrowMatch"  # legacy spelling, still accepted (dismech#10165, #16243)
PERMITTED = (EXACT, BROAD, NARROW)

KINDS = ("missing", "bad_predicate", "conflicting", "extra_exact")


class Member(NamedTuple):
    path: str
    predicates: tuple[str, ...]  # every predicate this entry records for the CURIE


class Finding(NamedTuple):
    curie: str
    path: str
    kind: str
    detail: str

    def key(self) -> str:
        return f"{self.curie}\t{self.path}\t{self.kind}"


def _term_id(block: Any) -> str | None:
    if not isinstance(block, dict):
        return None
    term = block.get("term")
    if isinstance(term, dict) and isinstance(term.get("id"), str):
        return term["id"].strip() or None
    return None


def mondo_predicates(data: dict[str, Any], curie: str) -> tuple[str, ...]:
    """Every ``mapping_predicate`` the entry records for ``curie``, in file order."""
    mappings = data.get("mappings")
    rows = mappings.get("mondo_mappings") if isinstance(mappings, dict) else None
    found: list[str] = []
    for row in rows or []:
        if not isinstance(row, dict) or _term_id(row) != curie:
            continue
        predicate = row.get("mapping_predicate")
        found.append(predicate.strip() if isinstance(predicate, str) else "")
    return tuple(found)


def collect_groups(docs: dict[str, dict[str, Any]]) -> dict[str, list[Member]]:
    """Map each ``disease_term`` held by two or more entries to its members."""
    by_term: dict[str, list[str]] = defaultdict(list)
    for path, data in docs.items():
        curie = _term_id(data.get("disease_term"))
        if curie:
            by_term[curie].append(path)
    return {
        curie: [Member(p, mondo_predicates(docs[p], curie)) for p in sorted(paths)]
        for curie, paths in sorted(by_term.items())
        if len(paths) > 1
    }


def _canonical(predicate: str) -> str | None:
    lowered = predicate.lower()
    for value in PERMITTED:
        if lowered == value.lower():
            return value
    return None


def assess_group(curie: str, members: list[Member]) -> list[Finding]:
    findings: list[Finding] = []
    exact_claimants: list[str] = []
    for m in members:
        distinct = sorted(set(m.predicates))
        if not distinct:
            findings.append(
                Finding(curie, m.path, "missing", f"no mondo_mappings row for {curie}")
            )
            continue
        if len(distinct) > 1:
            findings.append(
                Finding(
                    curie,
                    m.path,
                    "conflicting",
                    f"{len(m.predicates)} rows for {curie} with predicates "
                    + ", ".join(repr(p) for p in distinct),
                )
            )
            continue
        predicate = distinct[0]
        if predicate not in PERMITTED:
            canonical = _canonical(predicate)
            hint = (
                f"write {canonical}"
                if canonical
                else f"use {BROAD} (or {EXACT} for the one entry that is the class)"
            )
            findings.append(
                Finding(
                    curie,
                    m.path,
                    "bad_predicate",
                    f"mapping_predicate {predicate!r}; {hint}",
                )
            )
            continue
        if predicate == EXACT:
            exact_claimants.append(m.path)
    if len(exact_claimants) > 1:
        for path in exact_claimants:
            others = ", ".join(Path(p).stem for p in exact_claimants if p != path)
            findings.append(
                Finding(
                    curie,
                    path,
                    "extra_exact",
                    f"{EXACT} also claimed by {others}",
                )
            )
    return findings


def _display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def load_disorders(directory: Path = DISORDERS_DIR) -> dict[str, dict[str, Any]]:
    docs: dict[str, dict[str, Any]] = {}
    for path in sorted(directory.glob("*.yaml")):
        try:
            # Shared, read-only parse (#11003): this script never mutates it.
            data = load_document(path)
        except yaml.YAMLError:
            # `check-duplicate-keys` and `linkml-validate` report parse failures.
            continue
        if isinstance(data, dict):
            docs[_display(path)] = data
    return docs


def assess_all(
    docs: dict[str, dict[str, Any]],
) -> tuple[dict[str, list[Member]], list[Finding]]:
    groups = collect_groups(docs)
    findings = [f for curie, ms in groups.items() for f in assess_group(curie, ms)]
    return groups, findings


def load_baseline() -> set[str]:
    if not BASELINE_PATH.exists():
        return set()
    return {
        line.rstrip("\n")
        for line in BASELINE_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }


def write_baseline(findings: list[Finding]) -> int:
    keys = sorted({f.key() for f in findings})
    header = (
        "# Grandfathered shared disease_term findings "
        "(see scripts/check_shared_disease_terms.py, #10113).\n"
        "# Each line is `curie<TAB>path<TAB>kind`. Two entries sharing a\n"
        "# disease_term must each record skos:exactMatch or skos:broadMatch to it\n"
        "# (legacy skos:narrowMatch is also accepted, see dismech#10165/#16243)\n"
        "# in mappings.mondo_mappings, with at most one exactMatch per term.\n"
        "# New findings NOT listed here fail the guard. Remove rows as the\n"
        "# backlog is fixed; do not add new ones.\n"
        "# Regenerate with: just update-shared-disease-term-baseline\n"
    )
    BASELINE_PATH.write_text(header + "\n".join(keys) + "\n", encoding="utf-8")
    return len(keys)


def format_group(curie: str, members: list[Member], flagged: set[str]) -> list[str]:
    lines = [curie]
    for m in members:
        predicate = ", ".join(m.predicates) if m.predicates else "(no mapping)"
        mark = "  !" if m.path in flagged else "   "
        lines.append(f"{mark} {m.path}  {predicate}")
    return lines


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="print every shared disease_term group and exit 0",
    )
    parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="rewrite the baseline from the current tree (only ever to shrink it)",
    )
    args = parser.parse_args(argv)
    # One corpus walk, so the parsed-KB cache would only cost memory here.
    # In main(), not at import, so an in-process caller keeps the cache.
    kb_cache.default_off()

    groups, findings = assess_all(load_disorders())

    if args.update_baseline:
        n = write_baseline(findings)
        print(f"wrote {n} grandfathered finding(s) to {_display(BASELINE_PATH)}")
        return 0

    flagged_by_curie: dict[str, set[str]] = defaultdict(set)
    for f in findings:
        flagged_by_curie[f.curie].add(f.path)

    if args.report:
        clean = sum(1 for c in groups if c not in flagged_by_curie)
        print(
            f"{len(groups)} disease_term(s) shared by "
            f"{sum(len(m) for m in groups.values())} entries; "
            f"{clean} group(s) fully recorded, {len(findings)} finding(s).\n"
            "`!` marks a member with a finding.\n"
        )
        for curie, members in groups.items():
            print("\n".join(format_group(curie, members, flagged_by_curie[curie])))
            for f in findings:
                if f.curie == curie:
                    print(f"      {f.kind}: {Path(f.path).stem}: {f.detail}")
            print()
        return 0

    baseline = load_baseline()
    live = {f.key() for f in findings}
    new = [f for f in findings if f.key() not in baseline]
    stale = sorted(baseline - live)

    if stale:
        print(
            f"note: {len(stale)} baseline row(s) no longer match anything in the "
            "KB, so they have been fixed. Not a failure; shrink the baseline with "
            "`just update-shared-disease-term-baseline`:\n"
        )
        for key in stale:
            print("  " + key.replace("\t", "  "))
        print()

    if not new:
        print(
            f"OK: no new shared disease_term findings "
            f"({len(baseline) - len(stale)} grandfathered across "
            f"{len(flagged_by_curie)} group(s); `just list-shared-disease-terms` "
            "for the worklist)."
        )
        return 0

    print("Entries sharing a disease_term without recording how (#10113).\n")
    print(
        "When two disorder entries use the same disease_term, each must record\n"
        "that CURIE in mappings.mondo_mappings as skos:exactMatch (the entry that\n"
        "IS the class; at most one) or skos:broadMatch (an entry narrower than\n"
        "it, anchoring to its broader parent; such as a promoted cancer stratum,\n"
        "design decisions section 3a; the legacy skos:narrowMatch spelling is\n"
        "also accepted on existing entries). If your entry is not narrower than\n"
        "the existing one, it may be a duplicate: read the other entry before\n"
        "adding a mapping.\n"
    )
    new_curies = sorted({f.curie for f in new})
    for curie in new_curies:
        print("\n".join(format_group(curie, groups[curie], flagged_by_curie[curie])))
        for f in new:
            if f.curie == curie:
                print(f"      {f.kind}: {Path(f.path).stem}: {f.detail}")
        print()
    print(f"{len(new)} new finding(s).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
