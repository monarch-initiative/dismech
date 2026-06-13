"""Use grouping MONDO mappings as a curation prioritization signal.

For each grouping in kb/groupings/ that carries a MONDO mapping, this script:

1. Fetches the reflexive is-a descendants of the grouping's MONDO term.
2. Cross-references them against the MONDO ids declared by dismech disorder
   entries (primary ``disease_term`` plus any ``mappings.mondo_mappings``).
3. Reports which descendants are already covered by a dismech entry and which
   are gaps (candidate disorders to curate), prioritising leaf classes.
4. Prints the grouping term's MONDO OWL logical definition (genus + property
   restrictions) so we can eyeball whether the MONDO class is something this
   grouping could be made consistent with, or is a higher-level grouping we do
   not attempt to capture.

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


def grouping_mondo_terms() -> list[tuple[str, str]]:
    """Return (grouping_name, mondo_id) for groupings that carry a mapping."""
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
            if isinstance(mid, str) and mid.startswith("MONDO:"):
                out.append((data.get("name", os.path.basename(path)), mid))
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
        rests = [
            f"{r.propertyId} some {r.fillerId}" for r in (ld.restrictions or [])
        ]
        body = genus
        if rests:
            body += " and (" + " and ".join(rests) + ")"
        parts.append(body)
    return " ; ".join(parts)


def build_reports(only: str | None = None) -> list[GroupingReport]:
    adapter = get_adapter("sqlite:obo:mondo")
    index = disorder_mondo_index()
    reports: list[GroupingReport] = []
    for name, mondo in grouping_mondo_terms():
        if only and only.lower() not in name.lower():
            continue
        label = adapter.label(mondo) or ""
        ld = logical_definition_str(adapter, mondo)
        rep = GroupingReport(name, mondo, label, ld)
        descendants = {
            d
            for d in adapter.descendants([mondo], predicates=[IS_A])
            if d.startswith("MONDO:") and d != mondo
        }
        covered_ids = {d for d in descendants if d in index}
        # "Shadowed" = descendants of an already-covered entry. A gap inside the
        # shadow is just a finer MONDO split of a disorder we already curate
        # (e.g. "Bardet-Biedl syndrome 1" under our lumped BBS entry) and is not
        # a real curation gap. Gaps outside every shadow are the real candidates.
        shadowed: set[str] = set()
        for cid in covered_ids:
            shadowed.update(
                s
                for s in adapter.descendants([cid], predicates=[IS_A])
                if s.startswith("MONDO:")
            )
        for d in sorted(descendants):
            dlabel = adapter.label(d) or ""
            if d in index:
                rep.covered.append((d, dlabel, index[d]))
            elif d in shadowed:
                continue  # finer split of an already-curated entry; skip
            else:
                sub = {
                    s
                    for s in adapter.descendants([d], predicates=[IS_A])
                    if s.startswith("MONDO:")
                }
                is_leaf = sub <= {d}
                rep.gaps.append((d, dlabel, is_leaf))
        reports.append(rep)
    return reports


def render(reports: list[GroupingReport], markdown: bool) -> str:
    lines: list[str] = []
    h = (lambda s: f"## {s}") if markdown else (lambda s: f"\n=== {s} ===")
    for r in reports:
        total = len(r.covered) + len(r.gaps)
        lines.append(h(f"{r.grouping}  [{r.mondo} {r.mondo_label}]"))
        lines.append(f"MONDO logical definition: {r.logical_definition}")
        lines.append(
            f"Coverage: {len(r.covered)}/{total} descendant classes have a dismech entry"
        )
        leaf_gaps = [g for g in r.gaps if g[2]]
        lines.append(f"Gaps (no dismech entry): {len(r.gaps)}  (leaf classes: {len(leaf_gaps)})")
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


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--grouping", help="Only analyze groupings whose name contains this substring.")
    p.add_argument("--markdown", action="store_true", help="Emit markdown.")
    args = p.parse_args(argv)
    reports = build_reports(args.grouping)
    if not reports:
        print("No groupings with MONDO mappings matched.")
        return 0
    if args.markdown:
        print("# Grouping MONDO descendant coverage (curation prioritization)\n")
        print(
            "Generated by `scripts/grouping_mondo_gaps.py`. For each grouping that "
            "carries a MONDO mapping, this lists the MONDO term's is-a descendants "
            "and whether a dismech disorder declares that MONDO id. **Finer MONDO "
            "splits beneath an already-curated entry are collapsed** (e.g. "
            "*Bardet-Biedl syndrome 1* under our lumped BBS entry), so `Coverage: "
            "X/Y` counts only meaningful classes: Y = covered + unshadowed gaps. "
            "Leaf-class gaps are the highest-priority curation candidates. A 0/N "
            "coverage usually means the grouping's MONDO mapping does not is-a-"
            "subsume our curated members (a mapping-predicate/consistency signal, "
            "not N real gaps).\n"
        )
    print(render(reports, args.markdown))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
