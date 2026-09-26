"""Check grouping MONDO mappings by walking members UP, not the class DOWN.

A grouping that maps a MONDO class with ``skos:exactMatch`` or
``skos:narrowMatch`` is claiming its members sit inside that class. Verifying
that used to mean expanding the class's descendant closure and testing members
against it -- the expensive direction. It scales with the ontology rather than
with the grouping (``MONDO:0015286`` alone has ~169 descendants, and a broader
class has thousands), and it needs the ~588 MB local MONDO build, because the
``ols:mondo`` adapter this repo is configured with raises ``NotImplementedError``
for ``descendants``.

Inverting it removes both problems. The question is per member -- "is *this*
disease under the mapped class?" -- so resolve each member's own MONDO term to
its ancestor set and look the class up in it. Each walk returns on the order of
10-40 terms and is bounded by the member rather than by the ontology, and the
OLS REST ``hierarchicalAncestors`` endpoint serves ancestors directly even
though the OAK wrapper over the same service exposes neither direction. A
grouping of 38 members costs 38 bounded lookups and no download.

What this does NOT replace: ``scripts/grouping_mondo_gaps.py``. Finding MONDO
descendants that have *no* dismech entry is irreducibly a descendant query --
you cannot enumerate what you do not already hold by walking up from what you
do. That script still needs the local build. The two answer different halves:
gaps looks outward for uncurated concepts, this looks inward at whether the
members you already list support the mapping predicate you declared.

Expectation by predicate, which is the whole verdict logic:

  exactMatch / narrowMatch  the dismech concept is the class or sits inside it,
                            so every member is expected to descend from it
  broadMatch                the dismech concept contains the class; members
                            need not descend, so nothing is asserted
  closeMatch / relatedMatch  a cross-reference, not a subsumption claim

Usage:
    uv run python scripts/grouping_mondo_consistency.py
    uv run python scripts/grouping_mondo_consistency.py --grouping "Ciliopathies"
    uv run python scripts/grouping_mondo_consistency.py --format tsv
    uv run python scripts/grouping_mondo_consistency.py --strict

Needs network (EBI OLS). It is a report, not a gate: ``--strict`` exits 1 only
for a grouping whose declared predicate its own members contradict.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field

from dismech import kb_cache
from dismech.groupings import iter_disease_targets, load_groupings_by_name

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GROUPINGS_DIR = os.path.join(ROOT, "kb", "groupings")
DISORDERS_DIR = os.path.join(ROOT, "kb", "disorders")

OLS_BASE = "https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms"
SUBSUMING_PREDICATES = {"skos:exactMatch", "skos:narrowMatch"}
NO_CLAIM_PREDICATES = {"skos:broadMatch", "skos:closeMatch", "skos:relatedMatch"}


@dataclass
class MemberVerdict:
    disease: str
    via: str | None
    mondo: str | None
    verdict: str  # descendant | outside | no_mondo_term | lookup_failed


@dataclass
class GroupingVerdict:
    grouping: str
    mondo: str
    predicate: str
    members: list[MemberVerdict] = field(default_factory=list)

    @property
    def asserts_subsumption(self) -> bool:
        return self.predicate in SUBSUMING_PREDICATES

    @property
    def outside(self) -> list[MemberVerdict]:
        return [m for m in self.members if m.verdict == "outside"]

    @property
    def descendants(self) -> list[MemberVerdict]:
        return [m for m in self.members if m.verdict == "descendant"]

    @property
    def unresolved(self) -> list[MemberVerdict]:
        return [m for m in self.members if m.verdict in ("no_mondo_term", "lookup_failed")]

    @property
    def contradicted(self) -> bool:
        """The declared predicate claims subsumption that the members deny."""
        return self.asserts_subsumption and bool(self.outside)


def _encode(curie: str) -> str:
    iri = f"http://purl.obolibrary.org/obo/{curie.replace(':', '_')}"
    return urllib.parse.quote(urllib.parse.quote(iri, safe=""), safe="")


def ancestors(curie: str, cache: dict[str, list[str] | None], *, pause: float) -> list[str] | None:
    """Hierarchical ancestors of one MONDO term, or None if the lookup failed."""
    if curie in cache:
        return cache[curie]
    url = f"{OLS_BASE}/{_encode(curie)}/hierarchicalAncestors?size=500"
    result: list[str] | None
    try:
        with urllib.request.urlopen(url, timeout=60) as resp:
            payload = json.load(resp)
        terms = payload.get("_embedded", {}).get("terms", [])
        result = [t["obo_id"] for t in terms if t.get("obo_id")]
    except (urllib.error.URLError, TimeoutError, ValueError, KeyError):
        result = None
    cache[curie] = result
    if pause:
        time.sleep(pause)
    return result


def disorder_mondo_index() -> dict[str, str]:
    """Map disorder `name` -> its primary `disease_term` MONDO id."""
    index: dict[str, str] = {}
    for path in sorted(glob.glob(os.path.join(DISORDERS_DIR, "*.yaml"))):
        data = kb_cache.load_document(path)
        if not isinstance(data, dict) or not data.get("name"):
            continue
        term = (data.get("disease_term") or {}).get("term") or {}
        mid = term.get("id")
        if isinstance(mid, str) and mid.startswith("MONDO:"):
            index[str(data["name"])] = mid
    return index


def build_verdicts(only: str | None = None, *, pause: float = 0.15) -> list[GroupingVerdict]:
    groupings = load_groupings_by_name(sorted(glob.glob(os.path.join(GROUPINGS_DIR, "*.yaml"))))
    disease_mondo = disorder_mondo_index()
    cache: dict[str, list[str] | None] = {}
    out: list[GroupingVerdict] = []

    for name in sorted(groupings):
        if only and name != only:
            continue
        data = groupings[name]
        for mapping in (data.get("mappings") or {}).get("mondo_mappings") or []:
            mid = ((mapping or {}).get("term") or {}).get("id")
            if not (isinstance(mid, str) and mid.startswith("MONDO:")):
                continue
            gv = GroupingVerdict(name, mid, (mapping or {}).get("mapping_predicate") or "")
            for disease, _mtype, via in iter_disease_targets(data, groupings):
                member_mondo = disease_mondo.get(disease)
                if not member_mondo:
                    gv.members.append(MemberVerdict(disease, via, None, "no_mondo_term"))
                    continue
                anc = ancestors(member_mondo, cache, pause=pause)
                if anc is None:
                    verdict = "lookup_failed"
                elif mid in anc:
                    verdict = "descendant"
                else:
                    verdict = "outside"
                gv.members.append(MemberVerdict(disease, via, member_mondo, verdict))
            out.append(gv)
    return out


def _print_summary(verdicts: list[GroupingVerdict]) -> None:
    contradicted = [v for v in verdicts if v.contradicted]
    for v in verdicts:
        total = len(v.members)
        n_desc = len(v.descendants)
        flag = "  <-- predicate contradicted by its own members" if v.contradicted else ""
        claim = "expects all members inside" if v.asserts_subsumption else "asserts no subsumption"
        print(f"\n=== {v.grouping}")
        print(f"    {v.mondo}  {v.predicate or '(no predicate)'}  [{claim}]")
        print(f"    {n_desc}/{total} members descend from the mapped class{flag}")
        for m in v.outside:
            via = f" (via {m.via})" if m.via else ""
            print(f"      outside: {m.disease}{via}  {m.mondo}")
        for m in v.unresolved:
            via = f" (via {m.via})" if m.via else ""
            print(f"      {m.verdict}: {m.disease}{via}")

    print("\n" + "-" * 72)
    print(f"{len(verdicts)} MONDO mapping(s) across {len({v.grouping for v in verdicts})} grouping(s).")
    if contradicted:
        print(
            f"{len(contradicted)} declare exactMatch/narrowMatch while holding members "
            "outside the mapped class:"
        )
        for v in contradicted:
            print(f"  {v.grouping}  {v.mondo} {v.predicate}  ({len(v.outside)} outside)")
        print(
            "\nA member outside the class is not automatically a membership error. It is\n"
            "either a genuine scope difference (the dismech concept is broader than the\n"
            "MONDO class, so the predicate is wrong) or MONDO classifying the disease by\n"
            "clinical presentation rather than mechanism (a candidate MONDO term request).\n"
            "Read the members before changing anything."
        )
    else:
        print("No grouping's declared predicate is contradicted by its own members.")


def _print_tsv(verdicts: list[GroupingVerdict]) -> None:
    print("grouping\tmondo\tpredicate\tmember\tvia\tmember_mondo\tverdict")
    for v in verdicts:
        for m in v.members:
            print(
                f"{v.grouping}\t{v.mondo}\t{v.predicate}\t{m.disease}\t"
                f"{m.via or ''}\t{m.mondo or ''}\t{m.verdict}"
            )


def main(argv: list[str] | None = None) -> int:
    kb_cache.default_off()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--grouping", help="Only this grouping, by its `name`.")
    ap.add_argument("--format", choices=("summary", "tsv"), default="summary")
    ap.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 if any grouping declares exactMatch/narrowMatch while holding "
        "members outside the mapped class.",
    )
    ap.add_argument(
        "--pause",
        type=float,
        default=0.15,
        help="Seconds between OLS requests (default 0.15).",
    )
    args = ap.parse_args(argv)

    verdicts = build_verdicts(args.grouping, pause=args.pause)
    if not verdicts:
        target = f" matching {args.grouping!r}" if args.grouping else ""
        print(f"No grouping with a MONDO mapping{target}.")
        return 0

    if args.format == "tsv":
        _print_tsv(verdicts)
    else:
        _print_summary(verdicts)

    failed = [v for v in verdicts if v.unresolved and any(m.verdict == "lookup_failed" for m in v.members)]
    if failed:
        print(f"\nWARNING: {len(failed)} grouping(s) had at least one failed OLS lookup; "
              "those members are reported as lookup_failed, not as outside.", file=sys.stderr)

    if args.strict and any(v.contradicted for v in verdicts):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
