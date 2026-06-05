"""Named Entity Confusion (NEC) preflight check for deep-research reports.

This module catches the NEC failure mode tracked in dismech issue #3889: a
deep-research (DR) tool resolves the *queried* disease name to a *different*
disease entity and produces a report that is coherent but about the wrong
condition (e.g. SCAR20/SNX14 returned for Lichtenstein-Knorr/SLC9A1, PR #3874;
the Temtamy eponym collision, PRs #3835/#3871).

NEC is invisible to the standard hallucination stack (snippet-in-abstract
validation, PMID existence, ontology-term validation) because a wrong-entity
report validates correctly against its own (real) wrong-disease sources. The
only reliable catch is semantic: does the report's primary causal gene match
the authoritative MONDO causal gene for the queried disease?

The check has two cleanly separated halves so the decision logic can be
unit-tested without any network/OAK access:

1. Pure logic — :func:`extract_gene_mentions`, :func:`rank_genes`,
   :func:`evaluate` — operates on plain strings and gene sets.
2. OAK-backed lookup — :func:`mondo_causal_genes` — queries
   ``sqlite:obo:mondo`` for ``RO:0004003`` (*has material basis in germline
   mutation in*) edges to HGNC genes.

CLI::

    just preflight-dr research/Some_Disease-deep-research-falcon.md MONDO:0014572
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

# OAK relationship predicates that connect a MONDO disease to its causal
# gene(s). Germline is the primary signal; somatic is included so that
# cancer/somatic-driver entries are not spuriously flagged SKIP.
CAUSAL_GENE_PREDICATES = (
    "RO:0004003",  # has material basis in germline mutation in
    "RO:0004013",  # has material basis in germline mutation in (somatic variant)
    "RO:0004020",  # has material basis in somatic mutation in
    "RO:0004021",  # has material basis in somatic mutation in (loss/gain)
)

DEFAULT_MONDO_ADAPTER_SPEC = "sqlite:obo:mondo"

# A competing (non-causal) gene must reach at least this many mentions, and at
# least this fraction of the top gene's mentions, before it is treated as a
# genuine conflation signal rather than an incidental aside.
MIN_COMPETITOR_MENTIONS = 3
COMPETITOR_RATIO = 0.5

# Uppercase tokens that look gene-symbol-like but are not genes. Kept small and
# focused on tokens that actually recur in dismech DR reports; the goal is to
# cut obvious false positives, not to be an exhaustive dictionary.
NON_GENE_TOKENS = frozenset(
    {
        # Ontologies / identifiers / pipeline jargon
        "MONDO", "OMIM", "ORPHA", "HGNC", "HPO", "HP", "GO", "CL", "MAXO",
        "CHEBI", "NCIT", "UBERON", "GENO", "PMID", "DOI", "NCT", "CURIE",
        "DR", "NEC", "QC", "CI", "SOP", "URL", "YAML", "JSON", "ID", "IDS",
        # Common biomedical abbreviations
        "DNA", "RNA", "MRNA", "CDNA", "RRNA", "TRNA", "SNRNA", "MIRNA",
        "ATP", "ADP", "AMP", "GTP", "NAD", "NADH", "NADP", "FAD",
        "CSF", "CNS", "PNS", "ECM", "ER", "ROS", "ATP", "PH", "BMI",
        "MRI", "CT", "EEG", "ECG", "EKG", "PET", "USA", "UK", "EU", "WHO",
        "AR", "AD", "XL", "XLR", "XLD", "MOI", "SNV", "CNV", "INDEL",
        "WT", "KO", "KI", "IPSC", "IPSCS", "FDA", "EMA", "ICP", "LP",
        "TYPE", "MIM", "OK", "NA", "ND", "II", "III", "IV", "VI", "VII",
        "VIII", "IX", "XI", "XII",
        # Organizations / databases / sources that recur in DR report prose
        "CDC", "NCBI", "NIH", "ICD", "GTR", "NORD", "GARD", "OLS", "PDF",
        "HTML", "API", "WWW", "HTTP", "HTTPS",
        # Gangliosides / glycolipids — substrate names, not gene symbols
        "GM1", "GM2", "GM3", "GD1A", "GD1B", "GD2", "GD3", "GA1", "GA2",
        "GQ1B", "GT1B", "GB3", "GB4", "GL3", "LACCER",
    }
)

# Gene-symbol shapes. HGNC symbols are uppercase, start with a letter, and
# either contain a digit (SLC9A1, SNX14, HEXB? no digit) or are an all-letter
# symbol of >=2 chars (HEXB, DMD, APOB). The "orf" open-reading-frame symbols
# (C12orf57) are a special mixed-case case handled explicitly.
_ORF_RE = re.compile(r"\bC[0-9]{1,2}orf[0-9]{1,4}\b")
_GENE_RE = re.compile(r"\b[A-Z][A-Z0-9]*[0-9][A-Z0-9]*\b|\b[A-Z]{2,8}\b")


@dataclass
class PreflightResult:
    """Outcome of an NEC preflight comparison."""

    status: str  # PASS | WARN | FAIL | SKIP
    mondo_id: str
    causal_genes: list[str]
    top_genes: list[tuple[str, int]]
    message: str
    competitors: list[tuple[str, int]] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        """True when the report is consistent with the queried disease."""
        return self.status in {"PASS", "SKIP"}

    def render(self) -> str:
        top = ", ".join(f"{g} ({c})" for g, c in self.top_genes[:5]) or "<none>"
        causal = ", ".join(self.causal_genes) or "<none>"
        return (
            f"NEC preflight: {self.status}\n"
            f"  MONDO:        {self.mondo_id}\n"
            f"  causal gene:  {causal}\n"
            f"  top in report:{top}\n"
            f"  {self.message}"
        )


def extract_gene_mentions(text: str) -> Counter:
    """Return a Counter of candidate gene-symbol mentions in ``text``.

    Heuristic, not authoritative: matches uppercase gene-symbol-shaped tokens
    plus ``CNNorfNN`` open-reading-frame symbols, then drops a stoplist of
    common non-gene uppercase tokens (ontology prefixes, lab abbreviations).
    Good enough for a WARN/FAIL preflight signal; it is intentionally
    permissive and should never be treated as a curated gene list.
    """
    counts: Counter = Counter()
    for match in _ORF_RE.findall(text):
        counts[match] += 1
    # Mask orf hits so the generic pattern does not double-count fragments.
    masked = _ORF_RE.sub(" ", text)
    for token in _GENE_RE.findall(masked):
        if token in NON_GENE_TOKENS:
            continue
        counts[token] += 1
    return counts


def rank_genes(counts: Counter) -> list[tuple[str, int]]:
    """Return (gene, count) pairs sorted by count desc, then name for ties."""
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))


def _norm(genes) -> set[str]:
    return {g.upper() for g in genes}


def evaluate(
    top_genes: list[tuple[str, int]],
    causal_genes,
    mondo_id: str = "",
) -> PreflightResult:
    """Compare ranked report genes against the MONDO causal gene set.

    Decision table:

    * ``SKIP`` — MONDO has no single causal gene (multifactorial/complex), or
      the report has no recognizable gene mentions.
    * ``PASS`` — the report's most-mentioned gene is a MONDO causal gene and no
      non-causal gene competes strongly.
    * ``WARN`` — a causal gene appears in the report but is not the top gene, or
      the top gene is causal yet a non-causal gene competes strongly
      (eponym/locus mixing, e.g. the Temtamy pattern).
    * ``FAIL`` — no causal gene appears among the report's genes and the top
      gene is a different real gene (wrong-entity report, e.g. SNX14 for a
      SLC9A1 disease).
    """
    causal = _norm(causal_genes)
    causal_display = sorted(causal_genes)

    if not causal:
        return PreflightResult(
            status="SKIP",
            mondo_id=mondo_id,
            causal_genes=causal_display,
            top_genes=top_genes,
            message=(
                "MONDO entry has no single germline/somatic causal gene; "
                "NEC gene-identity check not applicable."
            ),
        )

    if not top_genes:
        return PreflightResult(
            status="SKIP",
            mondo_id=mondo_id,
            causal_genes=causal_display,
            top_genes=top_genes,
            message="No gene-symbol mentions found in report; cannot assess.",
        )

    mentioned = {g.upper() for g, _ in top_genes}
    causal_mentioned = sorted(causal & mentioned)
    top_gene, top_count = top_genes[0]
    competitors = [
        (g, c) for g, c in top_genes if g.upper() not in causal
    ]

    if top_gene.upper() in causal:
        strong = [
            (g, c)
            for g, c in competitors
            if c >= MIN_COMPETITOR_MENTIONS and c >= COMPETITOR_RATIO * top_count
        ]
        if strong:
            return PreflightResult(
                status="WARN",
                mondo_id=mondo_id,
                causal_genes=causal_display,
                top_genes=top_genes,
                competitors=strong,
                message=(
                    f"Primary gene {top_gene} matches MONDO, but non-causal "
                    f"gene(s) {', '.join(g for g, _ in strong)} are mentioned "
                    "comparably — possible eponym/locus conflation."
                ),
            )
        return PreflightResult(
            status="PASS",
            mondo_id=mondo_id,
            causal_genes=causal_display,
            top_genes=top_genes,
            message=f"Primary gene {top_gene} matches MONDO causal gene.",
        )

    if causal_mentioned:
        return PreflightResult(
            status="WARN",
            mondo_id=mondo_id,
            causal_genes=causal_display,
            top_genes=top_genes,
            competitors=competitors[:3],
            message=(
                f"Top gene {top_gene} is NOT the MONDO causal gene, though "
                f"causal gene(s) {', '.join(causal_mentioned)} appear lower in "
                "the report — likely mixed-entity content. Review before use."
            ),
        )

    return PreflightResult(
        status="FAIL",
        mondo_id=mondo_id,
        causal_genes=causal_display,
        top_genes=top_genes,
        competitors=competitors[:3],
        message=(
            f"Top gene {top_gene} is not a MONDO causal gene and no causal gene "
            f"({', '.join(causal_display)}) is mentioned — report likely "
            "describes a different disease entity. Discard; do not cherry-pick."
        ),
    )


def mondo_causal_genes(mondo_id: str, adapter=None) -> list[str]:
    """Return the HGNC gene symbol(s) MONDO records as causal for ``mondo_id``.

    Uses the ``RO:0004003``/somatic relationship edges in ``sqlite:obo:mondo``.
    Returns gene *labels* (symbols, e.g. ``SLC9A1``) when available, falling
    back to the bare HGNC CURIE. An empty list means MONDO has no single causal
    gene (multifactorial disease) — callers should treat that as SKIP.
    """
    if adapter is None:
        from oaklib import get_adapter

        adapter = get_adapter(DEFAULT_MONDO_ADAPTER_SPEC)

    predicates = set(CAUSAL_GENE_PREDICATES)
    genes: list[str] = []
    seen: set[str] = set()
    for _s, p, o in adapter.relationships(subjects=[mondo_id]):
        if p not in predicates:
            continue
        if not str(o).upper().startswith("HGNC:"):
            continue
        label = adapter.label(o) or o
        key = label.upper()
        if key not in seen:
            seen.add(key)
            genes.append(label)
    return genes


def preflight_report(
    report_path: Path,
    mondo_id: str,
    adapter=None,
) -> PreflightResult:
    """Run the NEC preflight on a DR report file against a MONDO ID."""
    text = Path(report_path).read_text(encoding="utf-8", errors="replace")
    ranked = rank_genes(extract_gene_mentions(text))
    causal = mondo_causal_genes(mondo_id, adapter=adapter)
    return evaluate(ranked, causal, mondo_id=mondo_id)


# Exit codes: 0 PASS/SKIP, 1 WARN, 2 FAIL. WARN is non-zero so a CI gate can
# choose to treat it as a soft failure; SKIP is success.
_EXIT_CODES = {"PASS": 0, "SKIP": 0, "WARN": 1, "FAIL": 2}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="preflight-dr",
        description=(
            "Named Entity Confusion (NEC) preflight: check that a deep-research "
            "report's primary gene matches the queried disease's MONDO causal "
            "gene (dismech #3889)."
        ),
    )
    parser.add_argument("report", type=Path, help="Path to a research/*.md DR report")
    parser.add_argument("mondo_id", help="MONDO CURIE of the queried disease, e.g. MONDO:0014572")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero on WARN as well as FAIL (default: only FAIL).",
    )
    args = parser.parse_args(argv)

    if not args.report.exists():
        parser.error(f"report not found: {args.report}")
    if not re.fullmatch(r"MONDO:\d+", args.mondo_id):
        parser.error(f"not a MONDO CURIE: {args.mondo_id}")

    result = preflight_report(args.report, args.mondo_id)
    print(result.render())

    code = _EXIT_CODES[result.status]
    if not args.strict and result.status == "WARN":
        code = 0
    return code


if __name__ == "__main__":
    sys.exit(main())
