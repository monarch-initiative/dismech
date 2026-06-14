"""Use grouping MONDO mappings as a curation prioritization signal.

For each grouping in kb/groupings/ that carries an exact MONDO mapping, this script:

1. Fetches the reflexive is-a descendants of the grouping's MONDO term.
2. Cross-references them against the MONDO ids declared by dismech disorder
   entries (primary ``disease_term`` plus any ``mappings.mondo_mappings``).
3. Reports which descendants are already covered by a dismech entry and which
   are gaps (candidate disorders to curate), prioritising leaf classes.
4. Prints the grouping term's MONDO OWL logical definition (genus + property
   restrictions) so we can eyeball whether the MONDO class is something this
   grouping could be made consistent with, or is a higher-level grouping we do
   not attempt to capture.

By default, descendant gaps are derived only from ``skos:exactMatch`` mappings:
an exact grouping mapping says the DisMech grouping and MONDO class are the same
intended concept, so missing MONDO descendants are curation gaps. Use
``--include-inexact`` for diagnostic reports over narrow/broad/related mappings;
those descendants are not exhaustive curation targets for the DisMech grouping.

Usage:
    uv run python scripts/grouping_mondo_gaps.py
    uv run python scripts/grouping_mondo_gaps.py --grouping Ciliopathies
    uv run python scripts/grouping_mondo_gaps.py --markdown > research/grouping_mondo_gaps.md
"""

from __future__ import annotations

import argparse
import glob
import os
from dataclasses import dataclass, field

import yaml
from oaklib import get_adapter
from oaklib.datamodels.vocabulary import IS_A

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GROUPINGS_DIR = os.path.join(ROOT, "kb", "groupings")
DISORDERS_DIR = os.path.join(ROOT, "kb", "disorders")
EXACT_MATCH = "skos:exactMatch"


def _mondo_ids(obj):
    """Yield every MONDO id appearing as term.id anywhere under obj."""
    if isinstance(obj, dict):
        term = obj.get("term")
        if isinstance(term, dict) and isinstance(term.get("id"), str):
            if term["id"].startswith("MONDO:"):
                yield term["id"]
        for v in obj.values():
            yield from _mondo_ids(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _mondo_ids(v)


def grouping_mondo_terms(
    include_inexact: bool = False,
) -> list[tuple[str, str, str]]:
    """Return (grouping_name, mondo_id, predicate) for eligible mappings."""
    out = []
    for path in sorted(glob.glob(os.path.join(GROUPINGS_DIR, "*.yaml"))):
        with open(path) as fh:
            data = yaml.safe_load(fh)
        if not isinstance(data, dict):
            continue
        mappings = (data.get("mappings") or {}).get("mondo_mappings") or []
        for m in mappings:
            term = (m or {}).get("term") or {}
            mid = term.get("id")
            predicate = (m or {}).get("mapping_predicate") or ""
            if not include_inexact and predicate != EXACT_MATCH:
                continue
            if isinstance(mid, str) and mid.startswith("MONDO:"):
                out.append((data.get("name", os.path.basename(path)), mid, predicate))
    return out


def disorder_mondo_index() -> dict[str, list[str]]:
    """Map every MONDO id declared by a dismech disorder -> [disorder names].

    Indexes the primary ``disease_term`` MONDO plus any MONDO ids under the
    top-level ``mappings`` block (the disease's own identity), which is where a
    disorder declares what MONDO class it *is*.
    """
    index: dict[str, list[str]] = {}
    for path in sorted(glob.glob(os.path.join(DISORDERS_DIR, "*.yaml"))):
        if path.endswith(".history"):
            continue
        with open(path) as fh:
            data = yaml.safe_load(fh)
        if not isinstance(data, dict):
            continue
        name = data.get("name", os.path.basename(path))
        ids = set()
        ids.update(_mondo_ids(data.get("disease_term")))
        ids.update(_mondo_ids(data.get("mappings")))
        for mid in ids:
            index.setdefault(mid, []).append(name)
    return index


@dataclass
class GroupingReport:
    grouping: str
    mondo: str
    mapping_predicate: str
    mondo_label: str
    logical_definition: str
    covered: list[tuple[str, str, list[str]]] = field(default_factory=list)
    gaps: list[tuple[str, str, bool]] = field(default_factory=list)  # id,label,is_leaf


def logical_definition_str(adapter, mondo: str) -> str:
    try:
        lds = list(adapter.logical_definitions([mondo]))
    except Exception:
        return "(none)"
    if not lds:
        return "(none)"
    parts = []
    for ld in lds:
        genus = ", ".join(ld.genusIds or [])
        rests = [f"{r.propertyId} some {r.fillerId}" for r in (ld.restrictions or [])]
        body = genus
        if rests:
            body += " and (" + " and ".join(rests) + ")"
        parts.append(body)
    return " ; ".join(parts)


def build_reports(
    only: str | None = None,
    *,
    include_inexact: bool = False,
) -> list[GroupingReport]:
    adapter = get_adapter("sqlite:obo:mondo")
    index = disorder_mondo_index()
    descendant_cache: dict[str, set[str]] = {}

    try:
        rows = adapter.connection.exec_driver_sql(
            "SELECT DISTINCT object FROM edge "
            "WHERE predicate = 'rdfs:subClassOf' "
            "AND subject LIKE 'MONDO:%' "
            "AND object LIKE 'MONDO:%'"
        )
        mondo_terms_with_children = {row[0] for row in rows}
    except Exception:
        mondo_terms_with_children = set()

    def mondo_descendants(term_id: str) -> set[str]:
        if term_id not in descendant_cache:
            descendant_cache[term_id] = {
                d
                for d in adapter.descendants([term_id], predicates=[IS_A])
                if isinstance(d, str) and d.startswith("MONDO:") and d != term_id
            }
        return descendant_cache[term_id]

    def is_mondo_leaf(term_id: str) -> bool:
        if mondo_terms_with_children:
            return term_id not in mondo_terms_with_children
        return not {
            child
            for _, child in adapter.incoming_relationships(term_id)
            if isinstance(child, str) and child.startswith("MONDO:")
        }

    reports: list[GroupingReport] = []
    for name, mondo, predicate in grouping_mondo_terms(include_inexact):
        if only and only.lower() not in name.lower():
            continue
        label = adapter.label(mondo) or ""
        ld = logical_definition_str(adapter, mondo)
        rep = GroupingReport(name, mondo, predicate, label, ld)
        descendants = mondo_descendants(mondo)
        covered_ids = {d for d in descendants if d in index}
        # "Shadowed" = descendants of an already-covered entry. A gap inside the
        # shadow is just a finer MONDO split of a disorder we already curate
        # (e.g. "Bardet-Biedl syndrome 1" under our lumped BBS entry) and is not
        # a real curation gap. Gaps outside every shadow are the real candidates.
        shadowed: set[str] = set()
        for cid in covered_ids:
            shadowed.update(mondo_descendants(cid))
        for d in sorted(descendants):
            dlabel = adapter.label(d) or ""
            if d in index:
                rep.covered.append((d, dlabel, index[d]))
            elif d in shadowed:
                continue  # finer split of an already-curated entry; skip
            else:
                rep.gaps.append((d, dlabel, is_mondo_leaf(d)))
        reports.append(rep)
    return reports


def render(reports: list[GroupingReport], markdown: bool) -> str:
    lines: list[str] = []
    h = (lambda s: f"## {s}") if markdown else (lambda s: f"\n=== {s} ===")
    for r in reports:
        total = len(r.covered) + len(r.gaps)
        lines.append(
            h(f"{r.grouping}  [{r.mapping_predicate} {r.mondo} {r.mondo_label}]")
        )
        if r.mapping_predicate != EXACT_MATCH:
            lines.append(
                "Mapping diagnostic only: inexact mappings do not imply that all "
                "MONDO descendants are DisMech curation gaps."
            )
        lines.append(f"MONDO logical definition: {r.logical_definition}")
        lines.append(
            f"Coverage: {len(r.covered)}/{total} descendant classes have a dismech entry"
        )
        leaf_gaps = [g for g in r.gaps if g[2]]
        lines.append(
            f"Gaps (no dismech entry): {len(r.gaps)}  (leaf classes: {len(leaf_gaps)})"
        )
        if r.covered:
            lines.append("  covered:")
            for mid, lab, names in r.covered:
                lines.append(f"    - {mid} {lab}  ->  {', '.join(names)}")
        if leaf_gaps:
            lines.append("  leaf-class gaps (highest-priority curation candidates):")
            for mid, lab, _ in leaf_gaps:
                lines.append(f"    - {mid} {lab}")
        branch_gaps = [g for g in r.gaps if not g[2]]
        if branch_gaps:
            lines.append("  intermediate/branch gaps (sub-groupings, lower priority):")
            for mid, lab, _ in branch_gaps:
                lines.append(f"    - {mid} {lab}")
    return "\n".join(lines)


def _audit_recommendation(
    current_predicate: str | None,
    *,
    outside_count: int,
) -> str:
    """Recommend follow-up without treating incomplete curation as mismatch."""
    if not current_predicate:
        return "(no mapping)"
    if current_predicate == EXACT_MATCH:
        if outside_count:
            return "keep exactMatch if conceptually equivalent; review outside-subtree members"
        return EXACT_MATCH
    if current_predicate == "skos:closeMatch":
        if outside_count:
            return (
                "consider exactMatch if conceptually equivalent; record "
                "outside-subtree members as consistency signals"
            )
        return "consider skos:exactMatch; partial DisMech coverage is not a downgrade reason"
    if current_predicate in {
        "skos:narrowMatch",
        "skos:broadMatch",
        "skos:relatedMatch",
    }:
        return f"keep {current_predicate} unless conceptual scope changes"
    return f"review current predicate {current_predicate}"


def audit_consistency(only: str | None = None) -> str:
    """For each grouping MONDO mapping, report whether the term is-a-subsumes the
    members' primary MONDO ids, and flag consistency signals.

    Mapping predicates describe conceptual scope, not current DisMech curation
    completeness. If an exact grouping mapping is missing many MONDO descendants,
    those descendants are curation gaps. If listed members sit outside the mapped
    MONDO subtree, that is a MONDO/member-alignment signal to record in
    `consistency`, not an automatic reason to weaken the mapping predicate.
    """
    adapter = get_adapter("sqlite:obo:mondo")
    # disorder name -> primary MONDO (disease_term)
    prim: dict[str, str] = {}
    for path in sorted(glob.glob(os.path.join(DISORDERS_DIR, "*.yaml"))):
        data = yaml.safe_load(open(path))
        if isinstance(data, dict):
            ids = list(_mondo_ids(data.get("disease_term")))
            if ids:
                prim[data.get("name")] = ids[0]
    lines: list[str] = []
    for path in sorted(glob.glob(os.path.join(GROUPINGS_DIR, "*.yaml"))):
        g = yaml.safe_load(open(path))
        if not isinstance(g, dict):
            continue
        if only and only.lower() not in (g.get("name", "")).lower():
            continue
        maps = (g.get("mappings") or {}).get("mondo_mappings") or []
        first_map = maps[0] if maps else {}
        gm = (first_map.get("term") or {}).get("id") if first_map else None
        current = first_map.get("mapping_predicate") if first_map else None
        members = [m.get("member") for m in (g.get("members") or [])]
        desc = (
            {
                x
                for x in adapter.descendants([gm], predicates=[IS_A])
                if x.startswith("MONDO:")
            }
            if gm
            else set()
        )
        sub = [m for m in members if prim.get(m) in desc]
        out = [m for m in members if prim.get(m) and prim.get(m) not in desc]
        nomondo = [m for m in members if not prim.get(m)]
        rec = _audit_recommendation(current, outside_count=len(out))
        lines.append(
            f"## {g.get('name')}  mapping={gm or '(none)'}  "
            f"current={current or '(none)'}  recommend={rec}"
        )
        lines.append(
            f"   subsumed {len(sub)}/{len(members)}; outside-subtree {len(out)}; no-mondo {len(nomondo)}"
        )
        for m in out:
            lines.append(f"   - OUTSIDE: {m} -> {prim.get(m)}")
        for m in nomondo:
            lines.append(f"   - NO MONDO IN ENTRY: {m}")
    return "\n".join(lines)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--grouping", help="Only analyze groupings whose name contains this substring."
    )
    p.add_argument("--markdown", action="store_true", help="Emit markdown.")
    p.add_argument(
        "--audit",
        action="store_true",
        help="Audit MONDO mapping consistency (subsumption of members) and recommend a SKOS predicate.",
    )
    p.add_argument(
        "--include-inexact",
        action="store_true",
        help=(
            "Include narrow/broad/related mappings in descendant reports for "
            "diagnostics. By default only skos:exactMatch mappings generate "
            "curation-gap reports."
        ),
    )
    args = p.parse_args(argv)

    if args.audit:
        print(audit_consistency(args.grouping))
        return 0
    reports = build_reports(args.grouping, include_inexact=args.include_inexact)
    if not reports:
        print("No groupings with MONDO mappings matched.")
        return 0
    if args.markdown:
        print("# Grouping MONDO descendant coverage (curation prioritization)\n")
        print(
            "Generated by `scripts/grouping_mondo_gaps.py`. For each grouping that "
            "carries an exact MONDO mapping, this lists the MONDO term's is-a "
            "descendants and whether a dismech disorder declares that MONDO id. "
            "**Finer MONDO splits beneath an already-curated entry are collapsed** "
            "(e.g. *Bardet-Biedl syndrome 1* under our lumped BBS entry), so "
            "`Coverage: X/Y` counts only meaningful classes: Y = covered + "
            "unshadowed gaps. Leaf-class gaps are the highest-priority curation "
            "candidates. Inexact mappings can be included with `--include-inexact`, "
            "but their descendants are diagnostic rather than exhaustive curation "
            "targets.\n"
        )
    print(render(reports, args.markdown))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
