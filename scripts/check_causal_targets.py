#!/usr/bin/env python3
"""Guard bare-name pathograph targets across the whole KB.

The causal graph is built by matching a ``target`` string against the ``name``
of another item in the same entry (see ``dismech.graph.build_causal_graph``).
Several slots work this way::

    pathophysiology[].downstream[].target        # CausalEdge
    phenotypes[].sequelae[].target               # CausalEdge
    phenotypes[].reports_on[].target             # PhenotypeReadout
    treatments[].target_mechanisms[].target      # TreatmentMechanismTarget
    environmental[].influences_mechanisms[].target

Unlike ``attaches_to``, these are **bare names** — the schema says so in as many
words ("Must match a pathophysiology or phenotype name in the same disease
file"). They are matched verbatim, with no resolution step, which makes a broken
one completely silent: LinkML validation, term validation and snippet
verification all pass, and the page still renders.

What actually happens is worse than a missing edge. ``build_causal_graph``
appends every declared edge unconditionally, so the edge count never moves; the
unresolved target instead lands in ``orphan_targets``, and the renderer draws it
as a **phantom duplicate node** -- red fill, dashed red border, reached by a
dashed edge, labelled with the literal ``phenotypes#Bleeding tendency`` string.
The real node it should have connected to drops out of the graph entirely. So
the chain is fragmented and carries a bogus node, rather than quietly losing an
arrow (issue #10112 found one entry at 0 of 7 phenotypes connected).

Why this needs its own ungated, whole-KB pass
---------------------------------------------
Same reason as ``check_entity_refs.py``: CI selects pytest by changed path, so a
curation PR touching only ``kb/`` matches neither the ``python`` nor the
``schema`` filter, and skips the tests written to protect KB content. And the
breakage is cross-file in the sense that matters — renaming a node breaks the
edges pointing at it, which may live in a part of the file the PR never touched,
or in an entry it did not open at all.

Three finding classes, deliberately kept apart because they have different
causes and different fixes:

``prefixed``
    A target written with the ``<kind>#<name>`` entity-reference grammar in a
    slot that takes a bare name. Never grandfathered: the fix is mechanical
    (drop the prefix) and the reference is unambiguous. This is issue #10112.

``dangling``
    A bare target naming nothing in the entry — typically a node renamed or
    split without updating the edges pointing at it. This is issue #9697. It has
    a committed backlog, so it is baselined rather than gating outright.

``self``
    A node listing itself as its own downstream target. Reported, never gating:
    the two committed cases are both a *pathophysiology node and a phenotype
    sharing one name*, which the flat node namespace collapses into a single
    node, turning a legitimate mechanism→phenotype edge into a self-loop. That
    is a graph-model bug (issue #9896), not a curation error, and deleting the
    edges would destroy evidenced content.

Relationship to `just validate-graphs`
--------------------------------------
``dismech.graph`` has carried a referential-integrity check since long before
this script, and ``just validate-graphs`` runs it. It is broader — it also
reports edges whose *source* is not a named element — but it is wired into
neither ``just qc`` nor CI, and it currently reports issues in 73 disorders, so
it cannot gate anything as it stands. That is the gap this script closes: the
same target-resolution invariant, narrowed to the slots where it is well
defined, with the committed backlog grandfathered so new breakage is the only
thing that fails.

Neither supersedes the other. ``validate-graphs`` stays the broader diagnostic;
this is the gateable subset. Burning down ``tests/causal_target_baseline.txt``
is the path to making the broader check gateable too.

Usage
-----
    python scripts/check_causal_targets.py                 # gate
    python scripts/check_causal_targets.py --report        # full census, exit 0
    python scripts/check_causal_targets.py --update-baseline
    python scripts/check_causal_targets.py kb/disorders/Asthma.yaml
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, NamedTuple

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.yaml_io import safe_load

BASELINE_PATH = ROOT / "tests" / "causal_target_baseline.txt"

DEFAULT_ROOTS = ("kb/disorders", "kb/modules", "kb/comorbidities")

# (section, edge slot) pairs whose `target` is a bare node name.
#
# `discussions[].proposed_experiments[].{readouts,perturbations}[].target` is
# deliberately absent: those reuse the `<kind>#<name>` entity-reference grammar
# (CLAUDE.md says so, and `check_entity_refs.py` already checks them). Listing
# them here would flag ~650 correct references as defects.
BARE_TARGET_SLOTS: tuple[tuple[str, str], ...] = (
    ("pathophysiology", "downstream"),
    ("phenotypes", "sequelae"),
    ("phenotypes", "reports_on"),
    ("treatments", "target_mechanisms"),
    ("environmental", "influences_mechanisms"),
)

# Sections contributing named nodes, mirroring `graph.build_causal_graph`.
NODE_SECTIONS = (
    "pathophysiology",
    "phenotypes",
    "environmental",
    "genetic",
    "treatments",
    "biochemical",
    "experimental_models",
    "computational_models",
)


class Finding(NamedTuple):
    path: str
    kind: str  # "prefixed" | "dangling" | "self"
    section: str
    slot: str
    source: str
    target: str

    def key(self) -> str:
        return f"{self.path}\t{self.section}.{self.slot}\t{self.source}\t{self.target}"


def node_names(data: dict[str, Any]) -> set[str]:
    names: set[str] = set()
    for section in NODE_SECTIONS:
        for item in data.get(section) or []:
            if isinstance(item, dict) and item.get("name"):
                names.add(item["name"])
    return names


def find_in(data: dict[str, Any], display: str) -> list[Finding]:
    names = node_names(data)
    findings: list[Finding] = []
    for section, slot in BARE_TARGET_SLOTS:
        for item in data.get(section) or []:
            if not isinstance(item, dict):
                continue
            source = item.get("name") or "?"
            for edge in item.get(slot) or []:
                if not isinstance(edge, dict):
                    continue
                target = edge.get("target")
                if not isinstance(target, str) or not target:
                    continue
                bare = target.split("#", 1)[1] if "#" in target else target
                if "#" in target and bare in names:
                    # Entity-ref grammar in a bare-name slot, and the bare form
                    # names a real node: mechanically fixable, so never excused.
                    kind = "prefixed"
                elif target == source:
                    kind = "self"
                elif bare not in names:
                    # Names nothing in this entry, prefixed or not. Fixing it
                    # needs a curator to say what was meant, so it is baselined.
                    kind = "dangling"
                else:
                    continue
                findings.append(Finding(display, kind, section, slot, source, target))
    return findings


def iter_yaml_files(paths: list[str]) -> list[Path]:
    if paths:
        return [Path(p) for p in paths]
    files: list[Path] = []
    for root in DEFAULT_ROOTS:
        files.extend(sorted((ROOT / root).rglob("*.yaml")))
    return files


def _display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def collect(paths: list[str]) -> list[Finding]:
    findings: list[Finding] = []
    for path in iter_yaml_files(paths):
        try:
            data = safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError):
            # `check-duplicate-keys` and `linkml-validate` report a parse
            # failure with better detail; don't fail the build twice for it.
            continue
        if isinstance(data, dict):
            findings.extend(find_in(data, _display(path)))
    return findings


def load_baseline() -> set[str]:
    if not BASELINE_PATH.exists():
        return set()
    return {
        line.rstrip("\n")
        for line in BASELINE_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }


def write_baseline(findings: list[Finding]) -> int:
    keys = sorted({f.key() for f in findings if f.kind == "dangling"})
    header = (
        "# Grandfathered dangling pathograph targets "
        "(see scripts/check_causal_targets.py).\n"
        "# Each line is `path<TAB>section.slot<TAB>source<TAB>target`. A target\n"
        "# naming no node in its entry silently drops that edge from the graph.\n"
        "# New occurrences NOT listed here fail the guard. Remove entries as the\n"
        "# backlog is fixed; do not add new ones.\n"
        "# Regenerate with: just update-causal-target-baseline\n"
    )
    BASELINE_PATH.write_text(header + "\n".join(keys) + "\n", encoding="utf-8")
    return len(keys)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help=f"default: {', '.join(DEFAULT_ROOTS)}")
    parser.add_argument(
        "--report", action="store_true", help="print the full census and exit 0"
    )
    parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="rewrite the dangling-target baseline from the current tree",
    )
    args = parser.parse_args()

    findings = collect(args.paths)
    by_kind: dict[str, list[Finding]] = {"prefixed": [], "dangling": [], "self": []}
    for f in findings:
        by_kind[f.kind].append(f)

    if args.update_baseline:
        n = write_baseline(findings)
        print(
            f"wrote {n} grandfathered dangling target(s) to {_display(BASELINE_PATH)}"
        )
        return 0

    if args.report:
        for kind in ("prefixed", "dangling", "self"):
            group = by_kind[kind]
            print(f"\n== {kind}: {len(group)} ==")
            for f in group:
                print(
                    f"  {f.path}\n     {f.section}.{f.slot}: {f.source!r} -> {f.target!r}"
                )
        return 0

    baseline = load_baseline()
    new_dangling = [f for f in by_kind["dangling"] if f.key() not in baseline]
    failures = by_kind["prefixed"] + new_dangling

    if by_kind["self"]:
        print(
            f"note: {len(by_kind['self'])} self-referential target(s) "
            "(a node listed as its own downstream). These are reported, not gated "
            "— see issue #9896 and this script's docstring.\n"
        )
        for f in by_kind["self"]:
            print(f"  {f.path}: {f.source!r} -> itself")
        print()

    if not failures:
        print(
            f"OK: no new broken pathograph targets "
            f"({len(baseline)} dangling target(s) grandfathered)."
        )
        return 0

    print("Broken pathograph target(s) detected in KB YAML.\n")
    print(
        "These slots hold BARE node names matched verbatim against the `name` of\n"
        "another item in the same entry. A broken one is silent to every other\n"
        "check: the entry validates and the page renders. What it does to the\n"
        "pathograph is draw a PHANTOM duplicate node -- red, dashed, labelled with\n"
        "the raw target string -- and orphan the real node out of the graph. So\n"
        "do not go looking for a missing arrow; look for a red node that should\n"
        "not be there.\n"
    )
    if by_kind["prefixed"]:
        print(
            f"-- {len(by_kind['prefixed'])} target(s) using the `<kind>#<name>` grammar --"
        )
        print("   These slots take a bare name; drop the prefix (issue #10112).\n")
        for f in by_kind["prefixed"]:
            bare = f.target.split("#", 1)[1]
            print(f"  {f.path}")
            print(f"     {f.section}.{f.slot}: {f.source!r} -> {f.target!r}")
            print(f"     fix: target: {bare}")
    if new_dangling:
        print(f"\n-- {len(new_dangling)} target(s) naming no node in their entry --")
        print(
            "   Usually a node renamed or split without updating its edges (#9697).\n"
        )
        for f in new_dangling:
            print(f"  {f.path}")
            print(f"     {f.section}.{f.slot}: {f.source!r} -> {f.target!r}")
    print(f"\n{len(failures)} finding(s).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
