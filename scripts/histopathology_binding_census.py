"""Census of ``histopathology[].finding_term`` ontology binding across the KB.

Answers the empirical questions behind the open design discussion in
`docs/explanation/design-decisions.md` §12 / issue #5140 ("the boundary between
phenotypes (HP) and histopathology (NCIT)"):

1. How many histopathology findings carry an ontology-bound ``finding_term``,
   and how are the bound ones split between NCIT and the narrow ``HP:0025461``
   carve-out?
2. Is the unbound tail made of *recurring single concepts* (which a wider
   vocabulary would rescue) or of *one-off post-composed descriptions* (which it
   would not)?
3. Are the post-composition slots ``HistopathologyFindingDescriptor`` inherits
   from ``Descriptor`` (``located_in``, ``modifier``, ``laterality``,
   ``spatial_extent``) actually used?

Fully offline — it reads ``kb/`` only, so it can be re-run to regenerate the
numbers in any report that cites it rather than trusting a snapshot.

Usage:
    uv run python scripts/histopathology_binding_census.py
    uv run python scripts/histopathology_binding_census.py --markdown
    uv run python scripts/histopathology_binding_census.py --list-unbound
"""

from __future__ import annotations

import argparse
import collections
import glob
import os
import re

from dismech.yaml_io import safe_load

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_GLOBS = ("kb/disorders/*.yaml", "kb/modules/*.yaml", "kb/comorbidities/*.yaml")

# Slots HistopathologyFindingDescriptor inherits from Descriptor and could use
# to post-compose a head term into a specific finding.
POSTCOMPOSITION_SLOTS = ("located_in", "modifier", "laterality", "spatial_extent", "severity")

# A label is treated as post-composed (rather than a single concept) if it joins
# clauses or runs long enough that no pre-composed ontology term is plausible.
_COMPOUND_RE = re.compile(r"\b(?:with|and|plus|without)\b|,|/")
_MAX_SINGLE_CONCEPT_WORDS = 4


def is_compound(label: str) -> bool:
    """True if the label reads as a post-composition rather than one concept."""
    return bool(_COMPOUND_RE.search(label.lower())) or len(label.split()) > _MAX_SINGLE_CONCEPT_WORDS


def normalize(label: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", label.lower()).split())


class Finding:
    def __init__(self, path: str, finding: dict) -> None:
        self.path = path
        term_block = finding.get("finding_term") or {}
        self.has_finding_term = bool(finding.get("finding_term"))
        self.label = (term_block.get("preferred_term") or finding.get("name") or "").strip()
        self.curie = ((term_block.get("term") or {}) or {}).get("id")
        self.postcomposition = [s for s in POSTCOMPOSITION_SLOTS if term_block.get(s)]


def collect() -> list[Finding]:
    findings: list[Finding] = []
    for pattern in KB_GLOBS:
        for path in sorted(glob.glob(os.path.join(ROOT, pattern))):
            data = safe_load(open(path))
            if not isinstance(data, dict):
                continue
            for finding in data.get("histopathology") or []:
                findings.append(Finding(os.path.relpath(path, ROOT), finding))
    return findings


def summarize(findings: list[Finding]) -> dict:
    bound = [f for f in findings if f.curie]
    unbound = [f for f in findings if not f.curie]
    prefixes = collections.Counter(f.curie.split(":")[0] for f in bound)
    distinct_unbound = {normalize(f.label) for f in unbound if f.label}
    return {
        "total": len(findings),
        "bound": len(bound),
        "unbound": len(unbound),
        "no_finding_term_block": sum(1 for f in unbound if not f.has_finding_term),
        "preferred_term_only": sum(1 for f in unbound if f.has_finding_term),
        "files_with_histopathology": len({f.path for f in findings}),
        "files_with_unbound": len({f.path for f in unbound}),
        "prefixes": dict(prefixes),
        "distinct_unbound_labels": len(distinct_unbound),
        "compound_unbound": sum(1 for f in unbound if is_compound(f.label)),
        "compound_bound": sum(1 for f in bound if is_compound(f.label)),
        "postcomposed": sum(1 for f in findings if f.postcomposition),
        "unbound_list": unbound,
    }


def _pct(part: int, whole: int) -> str:
    return f"{100 * part / whole:.0f}%" if whole else "n/a"


def render(stats: dict, markdown: bool) -> str:
    total, bound, unbound = stats["total"], stats["bound"], stats["unbound"]
    lines = [
        f"histopathology findings: {total} across {stats['files_with_histopathology']} KB files",
        f"  ontology-bound finding_term: {bound} ({_pct(bound, total)})",
        f"  unbound: {unbound} ({_pct(unbound, total)}) across {stats['files_with_unbound']} files",
        f"    no finding_term block at all: {stats['no_finding_term_block']}",
        f"    finding_term with preferred_term only: {stats['preferred_term_only']}",
        "",
        "bound-term vocabulary: "
        + ", ".join(f"{p} {n}" for p, n in sorted(stats["prefixes"].items(), key=lambda kv: -kv[1])),
        "",
        (
            f"distinct unbound labels: {stats['distinct_unbound_labels']} for {unbound} unbound"
            f" findings (the closer these are, the less recurring vocabulary there is to bind)"
        ),
        (
            f"post-composed labels: {stats['compound_unbound']} of {unbound} unbound"
            f" ({_pct(stats['compound_unbound'], unbound)})"
            f" vs {stats['compound_bound']} of {bound} bound"
            f" ({_pct(stats['compound_bound'], bound)})"
        ),
        (
            "findings using an inherited post-composition slot"
            f" ({', '.join(POSTCOMPOSITION_SLOTS)}): {stats['postcomposed']} of {total}"
        ),
    ]
    if markdown:
        return "```\n" + "\n".join(lines) + "\n```"
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--markdown", action="store_true", help="wrap output in a fenced block")
    parser.add_argument("--list-unbound", action="store_true", help="list every unbound finding")
    args = parser.parse_args()

    stats = summarize(collect())
    print(render(stats, args.markdown))
    if args.list_unbound:
        print()
        for finding in stats["unbound_list"]:
            kind = "compound" if is_compound(finding.label) else "single"
            print(f"{kind}\t{os.path.basename(finding.path)}\t{finding.label}")


if __name__ == "__main__":
    main()
