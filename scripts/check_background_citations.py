#!/usr/bin/env python3
"""Report evidence items whose snippet is not the cited paper's own finding.

``EvidenceItem`` records **which paper** a quote came from. Until ``quote_role``
it did not record **whether that paper produced the finding or was repeating
somebody else's**, and those are different epistemic objects (issue #10262).

The motivating case is a chick-embryo study whose *introduction* states the
human clinical picture, quoted for that human fact::

    evidence:
    - reference: PMID:31884688      # bead implantation in chick somites
      evidence_source: HUMAN_CLINICAL
      snippet: "perinatal mortality is high, due to an inadequate thorax"

Neither ``evidence_source`` value is right. ``MODEL_ORGANISM`` asserts a chick
measured human perinatal mortality; ``HUMAN_CLINICAL`` asserts a study type the
paper never ran; the ``OTHER`` that review tends to settle on says nothing at
all. The distinction the situation needs is *which part of the paper's argument
the sentence sits in*, which is what ``quote_role`` records.

This report builds the worklist for populating that slot. It is **report-only**:
no baseline, no gate, not wired into ``just qc``. It never writes ``quote_role``
and must not be used to, for the same reason ``dismech-terms`` refuses to
autofill an ontology binding from a suggestion -- see the ``--format tsv``
detail mode and decide each one by reading the sentence.

Three tiers, with very different precision
------------------------------------------
**Tier A, ``ABSTRACT_SECTION`` -- deterministic.** NLM structured-abstract
section labels (``BACKGROUND:``, ``METHODS:``, ``RESULTS:`` …) are author
supplied and NLM normalized, and ``just fetch-reference`` has been writing them
into the cached body all along. For a reference whose body carries them, which
zone a snippet sits in is a string containment, not an inference: no MeSH, no
publication type, no false positives from indexing lag. Snippets landing in a
background-stating zone are reported as ``BACKGROUND`` candidates; snippets
landing in the paper's own aim statement (``OBJECTIVE:``, ``PURPOSE:``) are
reported separately as ``AIM`` -- those are not background *and* not a finding,
the neighbouring defect ``check_title_snippets`` guards against.

The zone is a strong signal and still not a verdict. A structured ``BACKGROUND:``
paragraph routinely closes with the authors' own framing of what *they* did, so
a flagged snippet can be correctly ``PRIMARY_RESULT``. That is why this reports
and does not gate.

**Tier B, ``MESH_HEURISTIC``.** The scan in the issue: an item graded for human
evidence whose cached reference carries animal MeSH descriptors and no
``Humans``. A heuristic, with a real false-positive rate -- MeSH indexing lags,
some papers are genuinely mixed, and ``Humans`` is occasionally simply absent
from an older record.

Tier B covers **only** items graded ``HUMAN_CLINICAL`` or ``OTHER`` that cite
animal-only papers, so its count is a lower bound on a narrow slice and is
**not** an estimate of the problem's size. Every background quote taken from a
human paper -- the majority case, and the one Tier A is good at -- is outside it
by construction. ``OTHER`` is included on the strength of the observation in
#10262 that review pressure pushes exactly these items to ``OTHER``, which is
where the pattern goes to be forgotten.

The two tiers are complementary rather than competing: an unstructured abstract
is invisible to Tier A and can be caught by Tier B, and a structured human-cohort
paper restating somebody else's prevalence figure is invisible to Tier B and
caught by Tier A.

**Tier C, ``QUOTE_ROLE_CONFLICT``.** An item that already carries ``quote_role``
whose value contradicts the Tier A zone -- ``PRIMARY_RESULT`` on a sentence
sitting in ``BACKGROUND:``, or ``BACKGROUND`` on one sitting in ``RESULTS:``.
Empty until the slot is populated, and the reason Tier A is worth having as
machinery rather than a one-off scan.

Usage::

    just list-background-citations
    just list-background-citations --format tsv
    just list-background-citations --tier A --format list
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:  # pragma: no cover - import bootstrap
    sys.path.insert(0, str(ROOT / "src"))
if str(ROOT) not in sys.path:  # pragma: no cover - import bootstrap
    sys.path.insert(0, str(ROOT))

from dismech import kb_cache
from dismech.frontmatter import split_frontmatter
from dismech.kb_cache import load_document
from dismech.reference_snippet_audit import CachedReferenceIndex
from dismech.yaml_io import safe_load

SCAN_DIR = ROOT / "kb"
CACHE_DIR = ROOT / "references_cache"

#: Only PMID references carry NLM section labels and MeSH indexing. A DOI or
#: ORPHA record has neither, so both tiers would be silent on it anyway.
REFERENCE_PREFIX = "PMID:"

#: NLM structured-abstract section labels, mapped to the zone they open.
#:
#: Configurable by design: NLM normalizes to a core set but publishers emit
#: their own, and an unrecognized label still ends the preceding section (see
#: :func:`split_sections`) so a missing entry degrades to ``OTHER`` rather than
#: swallowing the next paragraph into the previous zone.
#:
#: ``BACKGROUND`` means "states what was already known"; ``AIM`` means "states
#: what this study set out to do"; ``FINDING`` means "reports or interprets what
#: this study observed".
SECTION_ZONES: dict[str, str] = {
    "BACKGROUND": "BACKGROUND",
    "INTRODUCTION": "BACKGROUND",
    "CONTEXT": "BACKGROUND",
    "IMPORTANCE": "BACKGROUND",
    "RATIONALE": "BACKGROUND",
    "BACKGROUND AND AIMS": "BACKGROUND",
    "BACKGROUND AND OBJECTIVE": "BACKGROUND",
    "BACKGROUND AND OBJECTIVES": "BACKGROUND",
    "BACKGROUND AND PURPOSE": "BACKGROUND",
    "OBJECTIVE": "AIM",
    "OBJECTIVES": "AIM",
    "PURPOSE": "AIM",
    "AIM": "AIM",
    "AIMS": "AIM",
    "AIM OF THE STUDY": "AIM",
    "HYPOTHESIS": "AIM",
    "METHODS": "FINDING",
    "METHOD": "FINDING",
    "MATERIALS AND METHODS": "FINDING",
    "PATIENTS AND METHODS": "FINDING",
    "SUBJECTS AND METHODS": "FINDING",
    "METHODS AND RESULTS": "FINDING",
    "DESIGN": "FINDING",
    "SETTING": "FINDING",
    "PATIENTS": "FINDING",
    "PARTICIPANTS": "FINDING",
    "SUBJECTS": "FINDING",
    "INTERVENTION": "FINDING",
    "INTERVENTIONS": "FINDING",
    "MEASUREMENTS": "FINDING",
    "MAIN OUTCOME MEASURES": "FINDING",
    "MAIN OUTCOME MEASURE": "FINDING",
    "RESULTS": "FINDING",
    "RESULT": "FINDING",
    "FINDINGS": "FINDING",
    "OBSERVATIONS": "FINDING",
    "DISCUSSION": "FINDING",
    "CONCLUSION": "FINDING",
    "CONCLUSIONS": "FINDING",
    "CONCLUSIONS AND RELEVANCE": "FINDING",
    "INTERPRETATION": "FINDING",
    "SIGNIFICANCE": "FINDING",
    "SUMMARY": "FINDING",
}

#: The zone a ``quote_role`` value claims, for the Tier C contradiction check.
#:
#: ``REVIEW_SYNTHESIS`` is deliberately absent: a review's synthesis sentence
#: legitimately sits in any zone of its own abstract, so no section placement
#: contradicts it.
QUOTE_ROLE_ZONES: dict[str, str] = {
    "PRIMARY_RESULT": "FINDING",
    "BACKGROUND": "BACKGROUND",
}

#: Zones whose snippets are reported as Tier A candidates, and the
#: ``quote_role`` each suggests. ``AIM`` suggests nothing -- a quoted aim
#: statement is evidence of neither a finding nor a background fact, and the
#: remedy is usually a different sentence rather than a ``quote_role`` value.
FLAGGED_ZONES: dict[str, str] = {"BACKGROUND": "BACKGROUND", "AIM": ""}

#: MeSH descriptors that mark a record as reporting non-human animal work.
#:
#: Matched against the descriptor (the part before any ``/`` qualifier list),
#: either exactly or as the head of an inverted form -- ``Mice`` also matches
#: ``Mice, Knockout`` and ``Mice, Inbred C57BL``, which is how MeSH spells its
#: narrower animal terms.
ANIMAL_MESH_DESCRIPTORS: frozenset[str] = frozenset(
    {
        "Animals",
        "Animals, Genetically Modified",
        "Animals, Newborn",
        "Birds",
        "Caenorhabditis elegans",
        "Cats",
        "Cattle",
        "Chick Embryo",
        "Chickens",
        "Cricetinae",
        "Disease Models, Animal",
        "Dogs",
        "Drosophila",
        "Drosophila melanogaster",
        "Ferrets",
        "Fishes",
        "Goats",
        "Guinea Pigs",
        "Horses",
        "Macaca",
        "Macaca fascicularis",
        "Macaca mulatta",
        "Mice",
        "Models, Animal",
        "Oryzias",
        "Primates",
        "Rabbits",
        "Rats",
        "Sheep",
        "Swine",
        "Swine, Miniature",
        "Xenopus",
        "Xenopus laevis",
        "Zebrafish",
    }
)

#: The MeSH descriptor whose presence takes a record out of Tier B entirely.
HUMAN_MESH_DESCRIPTOR = "Humans"

#: ``evidence_source`` values Tier B considers. ``HUMAN_CLINICAL`` is the
#: documented default for an absent value, so an omitted grade is treated as
#: that; ``OTHER`` is included because review pressure on exactly these items
#: pushes them there (#10262).
TIER_B_GRADES: frozenset[str] = frozenset({"HUMAN_CLINICAL", "OTHER"})
DEFAULT_EVIDENCE_SOURCE = "HUMAN_CLINICAL"

#: An all-caps label owning the start of a line, e.g. ``MAIN OUTCOME MEASURES:``.
#: Requires at least three characters so an initialism such as ``MRI:`` inside a
#: sentence-initial position is not mistaken for a section boundary.
_SECTION_LABEL_RE = re.compile(
    r"^(?P<label>[A-Z][A-Z0-9 ,/&'()\-]{2,60}):[ \t]+", re.MULTILINE
)

_TIERS = ("A", "B", "C")


@dataclass(frozen=True)
class Finding:
    """One reported evidence item."""

    tier: str
    path: str
    location: str
    reference: str
    zone: str
    evidence_source: str
    quote_role: str
    suggested: str
    snippet: str

    @property
    def kind(self) -> str:
        return {
            "A": "ABSTRACT_SECTION",
            "B": "MESH_HEURISTIC",
            "C": "QUOTE_ROLE_CONFLICT",
        }[self.tier]


@dataclass
class Coverage:
    """How much of the corpus each tier could actually see.

    Reported alongside the findings because a tier that saw little is not the
    same as a tier that found little, and the two read identically from a bare
    count.
    """

    items: int = 0
    pmid_items: int = 0
    cached: int = 0
    structured: int = 0
    located: int = 0
    outside_sections: int = 0
    unlocated: int = 0
    mesh_indexed: int = 0
    already_assessed: int = 0


def split_sections(body: str) -> list[tuple[str, str]]:
    """Split a cached body into ``(label, text)`` structured-abstract sections.

    Returns ``[]`` when the body carries no labels at all, which is what makes a
    reference ineligible for Tier A rather than silently judged by it.

    A section ends at the next label **or at the paragraph break that ends it**,
    whichever comes first. The paragraph bound is load-bearing on a
    ``content_type: full_text*`` cache: there the structured abstract is
    followed by the whole article, and without it the final abstract section
    (usually ``CONCLUSIONS:``) would swallow every later paragraph. A sentence
    quoted from the article's own introduction would then be reported as
    sitting in the abstract's conclusions -- confidently, deterministically, and
    wrongly. Text outside any labelled section is left unclassified, which is
    the honest answer for a full-text body: parsing its real section headings is
    a separate problem (#9711).
    """
    matches = list(_SECTION_LABEL_RE.finditer(body))
    if not matches:
        return []
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        text = body[match.end() : end]
        paragraph_break = text.find("\n\n")
        if paragraph_break != -1:
            text = text[:paragraph_break]
        label = " ".join(match.group("label").split())
        sections.append((label, text))
    return sections


def zone_of(label: str) -> str:
    """The zone a section label opens; ``OTHER`` for a label we do not know."""
    return SECTION_ZONES.get(label.upper(), "OTHER")


def descriptor_of(keyword: str) -> str:
    """The MeSH descriptor in a cached ``keywords:`` entry, without qualifiers."""
    return keyword.split("/", 1)[0].strip()


def is_animal_descriptor(descriptor: str) -> bool:
    """Whether *descriptor* names a non-human animal, including inverted forms."""
    if descriptor in ANIMAL_MESH_DESCRIPTORS:
        return True
    head = descriptor.split(",", 1)[0].strip()
    return head in ANIMAL_MESH_DESCRIPTORS and head != descriptor


class ReferenceFacts:
    """Memoized per-reference view of the two signals, read once per PMID."""

    def __init__(self, cache_dir: Path = CACHE_DIR) -> None:
        self._index = CachedReferenceIndex(cache_dir)
        self._facts: dict[str, dict[str, Any] | None] = {}

    def _load(self, reference: str) -> dict[str, Any] | None:
        path = self._index.resolve_cache_path(reference)
        if path is None:
            return None
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return None
        split = split_frontmatter(text)
        try:
            frontmatter = safe_load(split.frontmatter) if split is not None else {}
        except Exception:
            # A malformed cache file is `check-reference-cache-frontmatter`'s
            # gate, not this report's; treat it as carrying no signal.
            frontmatter = {}
        keywords = (frontmatter or {}).get("keywords") or []
        descriptors = [
            descriptor_of(str(keyword)) for keyword in keywords if str(keyword).strip()
        ]
        body = CachedReferenceIndex.extract_body(text)
        sections = split_sections(body)
        return {
            "sections": [
                (label, self._index.normalize(text_)) for label, text_ in sections
            ],
            "normalized_body": self._index.normalize(body),
            "descriptors": descriptors,
            "animal_only": bool(descriptors)
            and HUMAN_MESH_DESCRIPTOR not in descriptors
            and any(is_animal_descriptor(item) for item in descriptors),
            "mesh_indexed": bool(descriptors),
        }

    def facts(self, reference: str) -> dict[str, Any] | None:
        if reference not in self._facts:
            self._facts[reference] = self._load(reference)
        return self._facts[reference]

    def locate(self, reference: str, snippet: str) -> tuple[str, str] | None:
        """``(label, zone)`` for the section containing *snippet*, else ``None``.

        Matching is done on the reference validator's own normalized text, so a
        quote that verifies under ``just validate-references`` is located here
        too: case, punctuation and whitespace differences between the cache and
        a curator's transcription are already folded away on both sides.
        """
        facts = self.facts(reference)
        if not facts or not facts["sections"]:
            return None
        needle = self._index.normalize(snippet)
        if not needle:
            return None
        for label, text in facts["sections"]:
            if needle in text:
                return label, zone_of(label)
        return None

    def in_body(self, reference: str, snippet: str) -> bool:
        """Whether *snippet* appears anywhere in the cached body.

        Separates "quoted from a part of the document Tier A cannot classify"
        (a full text's own sections) from "not found at all" (a quote the
        reference validator would also reject, or one it accepts only through a
        looser match than this report makes).
        """
        facts = self.facts(reference)
        if not facts:
            return False
        needle = self._index.normalize(snippet)
        return bool(needle) and needle in facts["normalized_body"]


def _as_str(value: Any) -> str:
    return value.strip() if isinstance(value, str) else ""


def iter_evidence(data: Any) -> Iterator[tuple[str, dict[str, Any]]]:
    """Yield ``(location, item)`` for every evidence-shaped mapping in *data*.

    Shape-based rather than slot-name based: an evidence item is a mapping
    carrying both ``reference`` and ``snippet``. That is the same pair
    ``reference_snippet_audit`` keys on, and it reaches every block that embeds
    ``EvidenceItem`` without this report having to enumerate them.
    """

    def walk(node: Any, location: str) -> Iterator[tuple[str, dict[str, Any]]]:
        if isinstance(node, dict):
            if _as_str(node.get("reference")) and _as_str(node.get("snippet")):
                yield location, node
            for key, value in node.items():
                yield from walk(value, f"{location}.{key}" if location else str(key))
        elif isinstance(node, list):
            for index, value in enumerate(node):
                yield from walk(value, f"{location}[{index}]")

    yield from walk(data, "")


def kb_section(location: str) -> str:
    """The top-level KB slot a location sits in, e.g. ``pathophysiology``."""
    return location.split(".", 1)[0].split("[", 1)[0] or "(root)"


def classify(
    rel: str,
    location: str,
    item: dict[str, Any],
    refs: ReferenceFacts,
    coverage: Coverage,
    include_assessed: bool = False,
) -> list[Finding]:
    """Every finding one evidence item produces, across all three tiers."""
    reference = _as_str(item.get("reference"))
    snippet = _as_str(item.get("snippet"))
    coverage.items += 1
    if not reference.upper().startswith(REFERENCE_PREFIX):
        return []
    coverage.pmid_items += 1

    facts = refs.facts(reference)
    if facts is None:
        return []
    coverage.cached += 1
    if facts["mesh_indexed"]:
        coverage.mesh_indexed += 1

    evidence_source = _as_str(item.get("evidence_source")) or DEFAULT_EVIDENCE_SOURCE
    quote_role = _as_str(item.get("quote_role"))
    if quote_role:
        coverage.already_assessed += 1
    # An item that already carries `quote_role` has been decided, so it is off
    # the worklist -- unless it is being reported *because* of that value, which
    # is tier C. `include_assessed` puts it back for a census run.
    worklist = include_assessed or not quote_role
    findings: list[Finding] = []

    if facts["sections"]:
        coverage.structured += 1
        placed = refs.locate(reference, snippet)
        if placed is None:
            if refs.in_body(reference, snippet):
                coverage.outside_sections += 1
            else:
                coverage.unlocated += 1
        else:
            coverage.located += 1
            label, zone = placed
            if worklist and zone in FLAGGED_ZONES:
                findings.append(
                    Finding(
                        tier="A",
                        path=rel,
                        location=location,
                        reference=reference,
                        zone=label,
                        evidence_source=evidence_source,
                        quote_role=quote_role,
                        suggested=FLAGGED_ZONES[zone],
                        snippet=snippet,
                    )
                )
            claimed = QUOTE_ROLE_ZONES.get(quote_role)
            if (
                claimed is not None
                and zone in {"BACKGROUND", "FINDING"}
                and claimed != zone
            ):
                findings.append(
                    Finding(
                        tier="C",
                        path=rel,
                        location=location,
                        reference=reference,
                        zone=label,
                        evidence_source=evidence_source,
                        quote_role=quote_role,
                        suggested=FLAGGED_ZONES.get(zone, "PRIMARY_RESULT"),
                        snippet=snippet,
                    )
                )

    if worklist and facts["animal_only"] and evidence_source in TIER_B_GRADES:
        findings.append(
            Finding(
                tier="B",
                path=rel,
                location=location,
                reference=reference,
                zone="",
                evidence_source=evidence_source,
                quote_role=quote_role,
                suggested="",
                snippet=snippet,
            )
        )
    return findings


def scan_repo(
    scan_dir: Path = SCAN_DIR,
    cache_dir: Path = CACHE_DIR,
    rel_to: Path = ROOT,
    paths: Iterable[Path] | None = None,
    include_assessed: bool = False,
) -> tuple[list[Finding], Coverage]:
    """Return every finding in *scan_dir* (or *paths*), plus tier coverage."""
    refs = ReferenceFacts(cache_dir)
    coverage = Coverage()
    findings: list[Finding] = []
    targets = sorted(paths) if paths is not None else sorted(scan_dir.rglob("*.yaml"))
    for path in targets:
        try:
            data = load_document(path)
        except Exception as exc:
            # Gating on malformed YAML is `validate-all`'s job; skipping silently
            # would make the file invisible here rather than merely unchecked.
            print(
                f"warning: skipping unparseable {path}: {exc.__class__.__name__}",
                file=sys.stderr,
            )
            continue
        try:
            rel = path.relative_to(rel_to).as_posix()
        except ValueError:
            rel = path.as_posix()
        for location, item in iter_evidence(data):
            findings.extend(
                classify(rel, location, item, refs, coverage, include_assessed)
            )
    findings.sort(key=lambda f: (f.tier, f.path, f.location))
    return findings, coverage


HEADER = """Background-citation report (issue #10262) -- REPORT ONLY, never a gate.

Which part of a cited paper's argument a snippet sits in is what `quote_role`
records. This report builds the worklist for populating it; it does not decide
any item. Read the sentence.

  Tier A ABSTRACT_SECTION    deterministic: the snippet's zone in an NLM
                             structured abstract. A BACKGROUND: paragraph can
                             still close with the authors' own framing, so a
                             flag is a candidate, not a defect.
  Tier B MESH_HEURISTIC      heuristic: an item graded HUMAN_CLINICAL or OTHER
                             citing a paper indexed with animal MeSH and no
                             Humans. Covers only that narrow slice, so its
                             count is a LOWER BOUND and NOT an estimate of the
                             problem's size -- every background quote from a
                             human paper is outside it by construction.
  Tier C QUOTE_ROLE_CONFLICT a recorded quote_role that contradicts the Tier A
                             zone.
"""


def format_finding(finding: Finding) -> str:
    bits = [f"{finding.path}: {finding.kind} {finding.reference}"]
    if finding.zone:
        bits.append(f"[{finding.zone}]")
    bits.append(f"evidence_source={finding.evidence_source}")
    if finding.quote_role:
        bits.append(f"quote_role={finding.quote_role}")
    if finding.suggested:
        bits.append(f"suggests quote_role={finding.suggested}")
    quote = " ".join(finding.snippet.split())
    if len(quote) > 160:
        quote = quote[:157] + "..."
    return " ".join(bits) + f"\n    at {finding.location}\n    quote: {quote!r}"


def print_summary(findings: list[Finding], coverage: Coverage) -> None:
    print(HEADER)
    by_tier = Counter(finding.tier for finding in findings)
    print(
        f"scanned: {coverage.items} evidence item(s), "
        f"{coverage.pmid_items} with a PMID reference, "
        f"{coverage.cached} of those cached"
    )
    print(
        f"Tier A coverage: {coverage.structured} item(s) cite a reference whose "
        f"cached body carries section labels; {coverage.located} snippet(s) "
        f"located in a labelled section, {coverage.outside_sections} elsewhere "
        f"in the body (typically a full text's own prose, which carries no NLM "
        f"labels), {coverage.unlocated} not found in the cached body at all"
    )
    print(
        f"Tier B coverage: {coverage.mesh_indexed} item(s) cite a MeSH-indexed record"
    )
    print(
        f"already assessed: {coverage.already_assessed} item(s) carry a quote_role "
        "and are off the worklist (--include-assessed keeps them)"
    )
    print()
    for tier in _TIERS:
        tier_findings = [f for f in findings if f.tier == tier]
        kind = Finding(tier, "", "", "", "", "", "", "", "").kind
        files = {f.path for f in tier_findings}
        refs = {f.reference for f in tier_findings}
        print(
            f"Tier {tier} {kind}: {len(tier_findings)} item(s) across "
            f"{len(files)} file(s), {len(refs)} distinct reference(s)"
        )
        if not tier_findings:
            continue
        if tier == "A":
            zones = Counter(f.zone for f in tier_findings)
            for zone, count in sorted(zones.items(), key=lambda kv: (-kv[1], kv[0])):
                print(f"    {zone}: {count}")
        if tier == "B":
            grades = Counter(f.evidence_source for f in tier_findings)
            for grade, count in sorted(grades.items()):
                print(f"    evidence_source={grade}: {count}")
        sections = Counter(kb_section(f.location) for f in tier_findings)
        print(
            "    by KB section: "
            + ", ".join(
                f"{name} {count}"
                for name, count in sorted(
                    sections.items(), key=lambda kv: (-kv[1], kv[0])
                )
            )
        )
        top = Counter(f.path for f in tier_findings).most_common(8)
        for path, count in top:
            print(f"    {count:>4}  {path}")
    print(f"\ntotal: {sum(by_tier.values())} finding(s).")


def print_tsv(findings: list[Finding]) -> None:
    print(
        "\t".join(
            (
                "tier",
                "kind",
                "file",
                "kb_section",
                "location",
                "reference",
                "abstract_section",
                "evidence_source",
                "quote_role",
                "suggested_quote_role",
                "snippet",
            )
        )
    )
    for finding in findings:
        print(
            "\t".join(
                (
                    finding.tier,
                    finding.kind,
                    finding.path,
                    kb_section(finding.location),
                    finding.location,
                    finding.reference,
                    finding.zone,
                    finding.evidence_source,
                    finding.quote_role,
                    finding.suggested,
                    " ".join(finding.snippet.split()),
                )
            )
        )


def main(argv: list[str] | None = None) -> int:
    # One corpus walk, so the parsed-KB cache has no second walk to serve and is
    # pure cost (CLAUDE.md, "Parsed-KB Cache"). An explicit DISMECH_KB_CACHE
    # still wins.
    kb_cache.default_off()
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="specific YAML files to scan (default: every file under kb/)",
    )
    parser.add_argument(
        "--tier",
        choices=(*_TIERS, "all"),
        default="all",
        help="restrict the report to one tier",
    )
    parser.add_argument(
        "--include-assessed",
        action="store_true",
        help="also report items that already carry a quote_role (census, not worklist)",
    )
    parser.add_argument(
        "--format",
        choices=("summary", "list", "tsv"),
        default="summary",
        help="summary (default), one paragraph per finding, or TSV detail",
    )
    args = parser.parse_args(argv)

    findings, coverage = scan_repo(
        paths=args.paths or None, include_assessed=args.include_assessed
    )
    if args.tier != "all":
        findings = [finding for finding in findings if finding.tier == args.tier]

    if args.format == "tsv":
        print_tsv(findings)
    elif args.format == "list":
        for finding in findings:
            print(format_finding(finding))
        print(f"\n{len(findings)} finding(s).")
    else:
        print_summary(findings, coverage)
    # Report-only: a finding is a worklist entry, never a failure.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
