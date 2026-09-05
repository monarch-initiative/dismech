#!/usr/bin/env python3
"""Require a stated reason for phenotypes bound to top-level HPO terms.

A phenotype bound to ``HP:0000478`` *Abnormality of the eye* validates, renders,
exports, and derives the correct UI facet -- while saying almost nothing. The
common case is a curator who stopped early: ``Schaaf-Yang_Syndrome`` names
strabismus, esotropia and myopia in its ``description`` and then throws all
three away in the binding.

But three legitimate reasons for a coarse binding exist, and the KB already
contains all three written as prose that nothing can read:

* a **pleiotropic spectrum** where enumerating every finding is not the honest
  grain (``Rubinstein-Taybi_Syndrome``);
* a **source that genuinely says no more** (``PAICS_Deficiency``: "the specific
  ocular finding is not characterized in the available abstract, so the binding
  is deliberately at the general level");
* a **claim narrower than any HPO term**, where the coarse parent is the best
  available anchor and ``preferred_term`` carries the specificity.

So this guard does not chase specificity. It requires that a coarse binding
declare which situation it is in, via ``coarse_binding_basis``, leaving the
*unexplained* coarse binding as the only thing that fails.

What counts as coarse
---------------------
The 23 direct children of ``HP:0000118``, read from the ``meaning:`` values of
``PhenotypeCategoryEnum`` (``schema/classifications/phenotype_category.yaml``) --
the same list that drives the browser's *Phenotype Systems* facet. One source of
truth, already label-verified by ``just validate-terms-schema``. A term in that
set names a facet bucket; it cannot name a finding.

Deliberately NOT a depth or information-content rule. Depth is a property of how
HPO happens to be built, not of the claim: ``HP:0004322`` *Short stature* is the
most-used HP term in the KB and is exactly as specific as the literature ever
gets, while ``HP:0001627`` *Abnormal heart morphology* carries "Congenital heart
defect" as an EXACT synonym and *is* the clinical concept when a paper says
"CHD". Any metric that ranks those as vague would push curators to manufacture a
narrower binding than the source supports, which the term contract forbids
outright. Membership in a hand-reviewed list is the whole specificity model;
extending it is a schema PR with an argument attached.

Two finding classes
-------------------
``missing_basis``
    A coarse binding with no ``coarse_binding_basis``. The ~190 committed
    occurrences are grandfathered in ``tests/coarse_phenotype_baseline.txt``,
    which may only shrink; new ones fail.

``companion`` (never grandfathered)
    A declared basis whose companion requirement does not hold. These can only
    come from content written after the slot existed, so there is nothing to
    grandfather:

    ==================  ====================================================
    basis               requirement
    ==================  ====================================================
    SPECTRUM_SUMMARY    >= 2 ``spectrum_terms``, each bound, each narrower
                        than the summary term and not itself coarse
    SOURCE_UNSPECIFIED  none -- the evidence snippet is the proof
    NO_HPO_TERM         ``preferred_term`` differs from the bound label
                        (otherwise nothing narrower was actually claimed)
    PATHOGRAPH_HUB      on a ``phenotypes[]`` entry, targeted by at least one
                        causal edge in the same entry, and carrying no
                        ``frequency``
    ==================  ====================================================

    Plus the two inverses: ``spectrum_terms`` outside SPECTRUM_SUMMARY (where it
    is required) or PATHOGRAPH_HUB (where it is optional), and ``term_gap``
    without ``NO_HPO_TERM``.

    The hub rule is about *incoming* edges, not outgoing ones. An earlier draft
    required outgoing ``sequelae`` into the specific findings, which is wrong:
    ``sequelae`` is a ``CausalEdge``, and a coloboma is not *caused by* an eye
    abnormality -- it *is* one. Drawing subsumption as causation would corrupt
    the graph to satisfy a guard. What actually makes a node a hub is that a
    mechanism leads to it: something in the entry targets it. Its constituents,
    if worth naming, go in ``spectrum_terms``, which asserts no causation.

Companion rules are checked wherever a basis is declared, including on terms
outside the coarse subset. That is deliberate: it lets a curator declare a basis
on a second-tier term (``HP:0000924`` *Abnormality of the skeletal system*)
before anyone decides whether to widen the subset, without the declaration going
unchecked.

Why an ungated, whole-KB pass rather than only pytest
-----------------------------------------------------
Same reason as ``check_entity_refs.py`` and ``check_causal_targets.py``: CI
selects pytest by changed path, and a curation PR touches only ``kb/`` --
matching neither the ``python`` nor the ``schema`` filter. The checks written to
protect KB content are exactly the ones a content-only PR skips.

Usage
-----
    python scripts/check_coarse_phenotypes.py                  # gate
    python scripts/check_coarse_phenotypes.py --report         # census, exit 0
    python scripts/check_coarse_phenotypes.py --update-baseline
    python scripts/check_coarse_phenotypes.py kb/disorders/Asthma.yaml
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterator, NamedTuple

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.yaml_io import safe_load  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_causal_targets import BARE_TARGET_SLOTS  # noqa: E402

BASELINE_PATH = ROOT / "tests" / "coarse_phenotype_baseline.txt"
CATEGORY_ENUM_PATH = (
    ROOT / "src" / "dismech" / "schema" / "classifications" / "phenotype_category.yaml"
)

DEFAULT_ROOTS = ("kb/disorders", "kb/modules", "kb/comorbidities", "kb/groupings")

# Slots whose range is PhenotypeDescriptor. `spectrum_terms` is deliberately
# absent: its entries are checked as the *companions* of the summary binding
# that holds them, not as independent bindings of their own.
DESCRIPTOR_SLOT = "phenotype_term"
DESCRIPTOR_LIST_SLOT = "target_phenotypes"


def load_coarse_terms() -> dict[str, str]:
    """CURIE -> enum key for the top-level HPO organ-system terms."""
    enum = safe_load(CATEGORY_ENUM_PATH.read_text(encoding="utf-8"))
    values = enum["enums"]["PhenotypeCategoryEnum"]["permissible_values"]
    terms = {v["meaning"]: k for k, v in values.items() if v.get("meaning")}
    if not terms:
        raise SystemExit(f"no meanings found in {CATEGORY_ENUM_PATH}")
    return terms


class Finding(NamedTuple):
    path: str
    kind: str  # "missing_basis" | "companion"
    location: str
    curie: str
    detail: str

    def key(self) -> str:
        return f"{self.path}\t{self.location}\t{self.curie}"


class Binding(NamedTuple):
    location: str
    descriptor: dict[str, Any]
    parent: dict[str, Any] | None
    parent_section: str | None


def _label(item: Any) -> str:
    if isinstance(item, dict):
        for key in ("name", "preferred_term", "accession", "population"):
            value = item.get(key)
            if isinstance(value, str) and value:
                return value
    return ""


def iter_bindings(
    node: Any,
    trail: str = "",
    parent: dict[str, Any] | None = None,
    section: str | None = None,
) -> Iterator[Binding]:
    """Yield every PhenotypeDescriptor in an entry, with its containing item."""
    if isinstance(node, dict):
        for key, value in node.items():
            here = f"{trail}.{key}" if trail else key
            if key == DESCRIPTOR_SLOT and isinstance(value, dict):
                yield Binding(here, value, node, section)
                continue
            if key == DESCRIPTOR_LIST_SLOT and isinstance(value, list):
                for i, entry in enumerate(value):
                    if isinstance(entry, dict):
                        yield Binding(f"{here}[{i}]", entry, node, section)
                continue
            if key == "spectrum_terms":
                # Companion of its holder; never an independent binding.
                continue
            yield from iter_bindings(value, here, node, section or (key if not trail else section))
    elif isinstance(node, list):
        for i, entry in enumerate(node):
            tag = _label(entry)
            here = f"{trail}[{tag}]" if tag else f"{trail}[{i}]"
            yield from iter_bindings(entry, here, parent, section)


def _term_id(descriptor: dict[str, Any]) -> str | None:
    term = descriptor.get("term")
    if isinstance(term, dict):
        curie = term.get("id")
        if isinstance(curie, str):
            return curie
    return None


def _term_label(descriptor: dict[str, Any]) -> str:
    term = descriptor.get("term")
    if isinstance(term, dict):
        label = term.get("label")
        if isinstance(label, str):
            return label
    return ""


def _is_phenotype_entry(location: str) -> bool:
    """True for a `phenotypes[...]` element's own `phenotype_term`.

    Written as an explicit two-segment test rather than a substring search:
    `target_phenotypes[0]` contains "phenotypes", and an `imaging_findings[]`
    entry also carries a `phenotype_term`. Neither is a node in the causal
    graph, so neither can be a hub.
    """
    parts = location.split(".")
    return (
        len(parts) >= 2
        and parts[-1] == DESCRIPTOR_SLOT
        and parts[-2].startswith("phenotypes[")
    )


def check_companions(
    binding: Binding, coarse: dict[str, str], display: str, incoming: set[str]
) -> list[Finding]:
    """Validate the requirement that goes with a declared basis."""
    d = binding.descriptor
    basis = d.get("coarse_binding_basis")
    curie = _term_id(d) or "-"
    spectrum = d.get("spectrum_terms") or []
    findings: list[Finding] = []

    def add(detail: str) -> None:
        findings.append(Finding(display, "companion", binding.location, curie, detail))

    if basis is not None and not isinstance(basis, str):
        add(f"coarse_binding_basis must be a string, got {type(basis).__name__}")
        return findings

    if spectrum and basis not in ("SPECTRUM_SUMMARY", "PATHOGRAPH_HUB"):
        add(
            "spectrum_terms names the specific findings a coarse binding stands in "
            "for, so it goes with SPECTRUM_SUMMARY (where it is required) or "
            f"PATHOGRAPH_HUB (where it is optional). Basis here: {basis or 'absent'}."
        )
    if d.get("term_gap") and basis != "NO_HPO_TERM":
        add(
            "term_gap records the ontology gap behind a NO_HPO_TERM binding "
            f"(basis here: {basis or 'absent'})"
        )

    if basis in ("SPECTRUM_SUMMARY", "PATHOGRAPH_HUB"):
        bound = [t for t in spectrum if isinstance(t, dict) and _term_id(t)]
        if basis == "SPECTRUM_SUMMARY" and len(bound) < 2:
            add(
                f"SPECTRUM_SUMMARY needs >= 2 bound spectrum_terms, found {len(bound)}. "
                "One specific finding is not a spectrum -- bind that finding directly, "
                "or use SOURCE_UNSPECIFIED if the source names none."
            )
        for entry in bound:
            entry_curie = _term_id(entry)
            if entry_curie in coarse:
                add(
                    f"spectrum_terms entry {entry_curie} is itself a top-level term "
                    "-- a spectrum must be made of specific findings"
                )
            elif entry_curie == curie:
                add(f"spectrum_terms entry {entry_curie} repeats the summary term")
    if basis == "NO_HPO_TERM":
        preferred = (d.get("preferred_term") or "").strip()
        label = _term_label(d).strip()
        if not preferred:
            add("NO_HPO_TERM needs a preferred_term carrying the specificity the ontology lacks")
        elif preferred.casefold() == label.casefold():
            add(
                f"NO_HPO_TERM but preferred_term ({preferred!r}) just echoes the bound "
                "label, so nothing narrower is actually claimed"
            )
    if basis == "PATHOGRAPH_HUB":
        holder = binding.parent or {}
        name = holder.get("name")
        if not _is_phenotype_entry(binding.location):
            add(
                "PATHOGRAPH_HUB belongs on a phenotypes[] entry -- it names a node in the "
                "causal graph, and only those entries are nodes"
            )
        else:
            if not name or name not in incoming:
                add(
                    "PATHOGRAPH_HUB is a convergence point INSIDE the pathograph, so "
                    "something must lead to it: no causal edge in this entry targets "
                    f"{name!r}. Without one it is just an unexplained coarse binding "
                    "(SOURCE_UNSPECIFIED or SPECTRUM_SUMMARY is probably what you mean)."
                )
            if holder.get("frequency") is not None:
                add(
                    "PATHOGRAPH_HUB carries no clinical claim of its own, so it takes no "
                    "frequency -- the specific findings carry theirs. A coarse node with a "
                    "frequency is making a claim about patients, which is SPECTRUM_SUMMARY."
                )
    return findings


def incoming_targets(data: dict[str, Any]) -> set[str]:
    """Every bare node name something in this entry points a causal edge at.

    The slot list is imported from `check_causal_targets` rather than restated,
    so the two guards cannot drift about what an edge is. Self-edges are dropped:
    a node listing itself does not make it a convergence point.
    """
    targets: set[str] = set()
    for section, slot in BARE_TARGET_SLOTS:
        for item in data.get(section) or []:
            if not isinstance(item, dict):
                continue
            source = item.get("name")
            for edge in item.get(slot) or []:
                if not isinstance(edge, dict):
                    continue
                target = edge.get("target")
                if isinstance(target, str) and target and target != source:
                    targets.add(target)
    return targets


def find_in(data: dict[str, Any], display: str, coarse: dict[str, str]) -> list[Finding]:
    findings: list[Finding] = []
    incoming = incoming_targets(data)
    for binding in iter_bindings(data):
        d = binding.descriptor
        if not isinstance(d, dict):
            continue
        findings.extend(check_companions(binding, coarse, display, incoming))
        curie = _term_id(d)
        if curie in coarse and not d.get("coarse_binding_basis"):
            findings.append(
                Finding(
                    display,
                    "missing_basis",
                    binding.location,
                    curie,
                    f"{curie} ({coarse[curie]}) names an organ system, not a finding",
                )
            )
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


def collect(paths: list[str], coarse: dict[str, str]) -> list[Finding]:
    findings: list[Finding] = []
    for path in iter_yaml_files(paths):
        try:
            data = safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError):
            # `check-duplicate-keys` and `linkml-validate` report a parse failure
            # with better detail; don't fail the build twice for it.
            continue
        if isinstance(data, dict):
            findings.extend(find_in(data, _display(path), coarse))
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
    keys = sorted({f.key() for f in findings if f.kind == "missing_basis"})
    header = (
        "# Grandfathered coarse phenotype bindings "
        "(see scripts/check_coarse_phenotypes.py).\n"
        "# Each line is `path<TAB>location<TAB>curie`: a phenotype bound to a\n"
        "# top-level HPO organ-system term without saying why, via\n"
        "# `coarse_binding_basis`. New occurrences NOT listed here fail the guard.\n"
        "# Only ever shrink this file -- clearing a row means a curator decided\n"
        "# between SPECTRUM_SUMMARY / SOURCE_UNSPECIFIED / NO_HPO_TERM /\n"
        "# PATHOGRAPH_HUB, or bound a specific term instead.\n"
        "# Regenerate with: just update-coarse-phenotype-baseline\n"
    )
    BASELINE_PATH.write_text(header + "\n".join(keys) + "\n", encoding="utf-8")
    return len(keys)


def _print_census(findings: list[Finding], paths: list[str], coarse: dict[str, str]) -> None:
    missing = [f for f in findings if f.kind == "missing_basis"]
    companion = [f for f in findings if f.kind == "companion"]
    per_term = Counter(f.curie for f in missing)
    print(f"== unexplained coarse bindings: {len(missing)} ==")
    for curie, count in per_term.most_common():
        print(f"  {count:4d}  {curie}  {coarse.get(curie, '')}")
    print(f"\n== files: {len({f.path for f in missing})} ==")
    for f in missing:
        print(f"  {f.path}\n     {f.location}: {f.curie}")
    print(f"\n== companion-rule violations: {len(companion)} ==")
    for f in companion:
        print(f"  {f.path}\n     {f.location}: {f.detail}")

    # Bindings that DID say why. Not a defect -- the point of the guard -- but
    # the count is what tells you whether the backlog is being worked.
    declared: Counter[str] = Counter()
    for path in iter_yaml_files(paths):
        try:
            data = safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError):
            continue
        if not isinstance(data, dict):
            continue
        for binding in iter_bindings(data):
            basis = binding.descriptor.get("coarse_binding_basis")
            if isinstance(basis, str):
                declared[basis] += 1
    print(f"\n== declared bases: {sum(declared.values())} ==")
    for basis, count in declared.most_common():
        print(f"  {count:4d}  {basis}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help=f"default: {', '.join(DEFAULT_ROOTS)}")
    parser.add_argument(
        "--report", action="store_true", help="print the full census and exit 0"
    )
    parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="rewrite the grandfathered-binding baseline from the current tree",
    )
    args = parser.parse_args()

    if args.update_baseline and args.paths:
        # `write_baseline` records only what was scanned, so combining these
        # would truncate the committed baseline to that subset. Same trap
        # `check_causal_targets.py` refuses; refuse it the same way.
        parser.error(
            "--update-baseline rewrites the whole baseline and cannot be scoped "
            "to individual files; re-run it with no paths."
        )

    coarse = load_coarse_terms()
    findings = collect(args.paths, coarse)
    missing = [f for f in findings if f.kind == "missing_basis"]
    companion = [f for f in findings if f.kind == "companion"]

    if args.update_baseline:
        n = write_baseline(findings)
        print(f"wrote {n} grandfathered coarse binding(s) to {_display(BASELINE_PATH)}")
        return 0

    if args.report:
        _print_census(findings, args.paths, coarse)
        return 0

    baseline = load_baseline()
    new_missing = [f for f in missing if f.key() not in baseline]
    # Rows whose binding has since been explained or narrowed. Never a failure,
    # but the baseline's value is that its size is an honest measure of the
    # remaining backlog, so a stale row is worth reporting. Only computable over
    # the whole tree: under explicit paths every row outside the subset would
    # look stale.
    stale = [] if args.paths else sorted(baseline - {f.key() for f in missing})

    if stale:
        print(
            f"note: {len(stale)} baseline row(s) no longer match anything in the KB, "
            "so those bindings have since been explained or narrowed. Not a failure, "
            "but the grandfathered count overstates the backlog by that much. Shrink "
            "it with `just update-coarse-phenotype-baseline`:\n"
        )
        for key in stale:
            path, location, curie = key.split("\t")
            print(f"  {path}\n     {location}: {curie}")
        print()

    if not new_missing and not companion:
        remaining = len(baseline) - len(stale)
        print(
            "OK: no new unexplained coarse phenotype bindings "
            f"({remaining} grandfathered)."
        )
        return 0

    if new_missing:
        print(
            f"-- {len(new_missing)} phenotype(s) bound to a top-level HPO term with no "
            "stated reason --\n"
        )
        print(
            "   These terms are the direct children of HP:0000118: they name an organ\n"
            "   system, and are what the browser's 'Phenotype Systems' facet is built\n"
            "   from. A binding to one is not wrong, but it must say which it is:\n"
            "     SPECTRUM_SUMMARY    many findings, variable -- list them in spectrum_terms\n"
            "     SOURCE_UNSPECIFIED  the cited source characterizes it no further\n"
            "     NO_HPO_TERM         narrower than any HP term; preferred_term carries it\n"
            "     PATHOGRAPH_HUB      a convergence node with sequelae into the specifics\n"
            "   If none of those is true, bind the specific finding instead. Do NOT pick\n"
            "   a narrower term the source does not support just to clear this.\n"
        )
        for f in new_missing:
            print(f"  {f.path}")
            print(f"     {f.location}: {f.detail}")
    if companion:
        print(f"\n-- {len(companion)} declared basis(es) whose requirement does not hold --\n")
        for f in companion:
            print(f"  {f.path}")
            print(f"     {f.location}: {f.detail}")
    print(f"\n{len(new_missing) + len(companion)} finding(s).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
