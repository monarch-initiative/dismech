"""NEC preflight check for deep-research reports (issue #3889).

Named Entity Confusion (NEC) is the deep-research failure mode in which a DR
tool resolves the queried disease name to a *different* disease entity and
returns a report that is coherent but about the wrong condition. None of the
standard anti-hallucination checks can catch it: the PMIDs are real, the
snippets validate as exact substrings of their (wrong-disease) abstracts, and
the ontology terms exist. The only catch is semantic.

This module automates the manual NEC preflight documented in ``CLAUDE.md``:
it counts gene-symbol mentions in a DR report, looks up the canonical causal
gene for the MONDO entity the curator *intended* to curate, and reports
PASS / WARN / FAIL / SKIP.

It is the per-report counterpart of ``scripts/nec_risk_audit.py``, which flags
structurally NEC-prone disease *classes* across the whole knowledge base.

Usage::

    just preflight-dr research/Lichtenstein-Knorr_Syndrome-deep-research-falcon.md MONDO:0014572
    uv run python -m dismech.preflight_dr <report.md> <MONDO:XXXXXXX> [--json] [--strict]

Verdicts
--------
``FAIL``
    The MONDO entity's canonical gene is absent from the report while some
    other gene is discussed substantively. This is the Lichtenstein-Knorr
    pattern (PR #3874): the report named SNX14 43 times and SLC9A1 zero times.
    **Discard the report entirely — do not cherry-pick from it.**
``WARN``
    The canonical gene is present but a rival gene is also discussed
    substantively, or the report's OMIM IDs disagree with the MONDO xref, or
    no genes could be found at all. This is the Temtamy pattern (PR #3835):
    a single report mixing C12orf57 and CHSY1 content. Sections about the
    rival entity must be excluded before curating.
``PASS``
    The canonical gene dominates the report's gene mentions.
``SKIP``
    MONDO records no causal gene for this entity (complex/multifactorial
    disease, or a grouping term). The check cannot discriminate; fall back to
    the manual OMIM/synonym preflight.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path

# MONDO's "disease has basis in dysfunction of" relation, which links a disease
# term to the HGNC gene(s) whose disruption causes it.
GENE_RELATION = "RO:0004003"

# Gene-symbol-shaped tokens. Covers the ordinary all-caps form (SLC9A1, BRCA2),
# hyphenated forms (BCR-ABL1, HLA-B), and the mixed-case chromosome-open-reading-
# frame form (C12orf57) that a naive all-caps pattern misses -- and C12orf57 is
# precisely the gene at issue in the Temtamy NEC case.
GENE_TOKEN_RE = re.compile(
    r"\b(?:C\d{1,2}orf\d{1,3}|[A-Z][A-Z0-9]{1,9}(?:-[A-Z0-9]{1,6})?)\b"
)

# OMIM / MIM identifiers as they appear in DR prose: "OMIM:616291", "OMIM 616291",
# "MIM #605282", "(MIM 616354)".
OMIM_RE = re.compile(r"\b(?:OMIM|MIM)\s*[:#\s]\s*#?\s*(\d{6})\b", re.IGNORECASE)

# Ontology/database CURIEs (HP:0001250, GO:0007179, PMID:12345678, MONDO:0014572).
# These must be stripped before gene tokens are counted: several ontology prefixes
# are *also* real HGNC symbols -- HP is haptoglobin, CS is citrate synthase -- so a
# phenotype-rich DR report otherwise ranks "HP" among its top genes and drowns out
# the actual rival-gene signal.
CURIE_RE = re.compile(r"\b[A-Za-z][A-Za-z0-9_]*\s*:\s*\d[\w.]*")

# A gene needs at least this many mentions before it counts as "discussed
# substantively". Below it, a symbol is usually an aside, a pathway member, or a
# gene named once in a citation title -- not the subject of the report.
DEFAULT_MIN_SIGNAL = 3

# A rival gene mentioned at least this fraction as often as the expected gene
# marks the report as contaminated. Tuned against the Temtamy report, where the
# wrong-entity gene CHSY1 (23) reaches 0.40 of C12orf57 (57).
DEFAULT_RIVAL_RATIO = 0.25

PASS, WARN, FAIL, SKIP = "PASS", "WARN", "FAIL", "SKIP"

# Uppercase tokens that look like gene symbols but are not. Used only when no
# HGNC lexicon is available (``--no-hgnc`` or an OAK failure); with the lexicon
# these are rejected because they are not HGNC symbols.
NON_GENE_TOKENS = frozenset({
    # Molecular-biology and assay acronyms
    "DNA", "RNA", "MRNA", "CDNA", "SNP", "SNV", "CNV", "WES", "WGS", "PCR",
    "QPCR", "RT", "ELISA", "CRISPR", "IPSC", "ESC", "PBMC", "FACS",
    # Imaging / clinical measurement
    "MRI", "CT", "PET", "EEG", "ECG", "EMG", "CSF", "CNS", "PNS", "BMI",
    "ICU", "NICU",
    # Metabolites and second messengers
    "ATP", "ADP", "NAD", "NADH", "NADPH", "FAD", "GTP", "CAMP", "CGMP", "ROS",
    "PH",
    # Database / ontology prefixes (belt-and-braces; CURIE_RE strips most)
    "OMIM", "MIM", "MONDO", "HPO", "HGNC", "PMID", "DOI", "NCT", "ORPHA",
    "GARD", "MEDGEN", "UMLS", "DOID", "ORPHANET", "ICD", "ICD10",
    # Genetics / statistics shorthand
    "AR", "AD", "XL", "XLR", "XLD", "MOI", "VUS", "ACMG", "CI", "SD", "SE",
    "IQR", "HR", "RR", "PPV", "NPV", "SEM", "ANOVA",
    # Organisations and project shorthand
    "FDA", "EMA", "NIH", "USA", "UK", "EU", "WHO", "IRB", "SOP", "QC", "KB",
    # Formats and prose stopwords that survive the uppercase filter
    "PDF", "HTML", "URL", "API", "CLI", "CSV", "TSV", "YAML", "JSON", "XML",
    "ID", "IDS", "TBD", "TODO", "NA", "ND", "NB", "EG", "IE", "VS", "ETC",
    "FIG", "TABLE", "TAB", "REF", "REFS", "SUPP", "AKA",
    "OR", "AND", "NOT", "THE", "FOR", "WITH", "FROM", "THIS", "THAT", "THESE",
    "THOSE", "ALL", "ANY", "ONE", "TWO",
})


@dataclass(frozen=True)
class MondoRecord:
    """The identity anchors for the disease the curator intended to curate."""

    id: str
    label: str = ""
    definition: str = ""
    genes: tuple[str, ...] = ()
    omim_ids: tuple[str, ...] = ()
    synonyms: tuple[str, ...] = ()


@dataclass
class PreflightResult:
    verdict: str
    mondo: str
    mondo_label: str
    report: str
    expected_genes: list[str]
    expected_mentions: dict[str, int]
    top_genes: list[tuple[str, int]]
    rival_genes: list[tuple[str, int]]
    expected_omim: list[str]
    report_omim: list[str]
    reasons: list[str] = field(default_factory=list)
    lexicon: str = "hgnc"

    @property
    def ok(self) -> bool:
        return self.verdict in (PASS, SKIP)


class HgncLexicon:
    """Gene-symbol membership test backed by the OAK HGNC adapter.

    Lookups are memoised because a DR report yields a few hundred distinct
    candidate tokens and each one would otherwise hit SQLite.
    """

    name = "hgnc"

    def __init__(self, adapter=None):
        self._adapter = adapter
        self._cache: dict[str, bool] = {}

    def _get_adapter(self):
        if self._adapter is None:
            from oaklib import get_adapter

            self._adapter = get_adapter("sqlite:obo:hgnc")
        return self._adapter

    def __contains__(self, symbol: str) -> bool:
        if symbol not in self._cache:
            try:
                hits = list(self._get_adapter().curies_by_label(symbol))
            except Exception:  # pragma: no cover - adapter/network failure
                hits = []
            self._cache[symbol] = bool(hits)
        return self._cache[symbol]


class HeuristicLexicon:
    """Fallback lexicon: everything that is not a known non-gene acronym.

    Noisier than :class:`HgncLexicon` -- used only when HGNC is unavailable.
    """

    name = "heuristic"

    def __contains__(self, symbol: str) -> bool:
        return symbol.upper() not in NON_GENE_TOKENS


def strip_curies(text: str) -> str:
    """Remove ontology/database CURIEs so their prefixes are not counted as genes."""
    return CURIE_RE.sub(" ", text)


def extract_gene_mentions(text: str, lexicon=None) -> Counter:
    """Count gene-symbol mentions in ``text``, most frequent first.

    CURIEs are stripped first (see :data:`CURIE_RE`).
    """
    lexicon = lexicon if lexicon is not None else HeuristicLexicon()
    counts: Counter = Counter()
    for token in GENE_TOKEN_RE.findall(strip_curies(text)):
        if token in lexicon:
            counts[token] += 1
    return counts


def extract_omim_ids(text: str) -> set[str]:
    """Return the six-digit OMIM/MIM identifiers cited in ``text``."""
    return set(OMIM_RE.findall(text))


def fetch_mondo_record(mondo_id: str, adapter=None) -> MondoRecord:
    """Look up the label, definition, causal gene(s), and OMIM xrefs for a MONDO term.

    The causal gene comes from the ``RO:0004003`` relation. Contrary to an
    earlier note in ``CLAUDE.md``, the local ``sqlite:obo:mondo`` adapter does
    expose this relation, so the definition text is only a fallback for terms
    that lack the edge.
    """
    if adapter is None:
        from oaklib import get_adapter

        adapter = get_adapter("sqlite:obo:mondo")

    label = adapter.label(mondo_id) or ""
    try:
        definition = adapter.definition(mondo_id) or ""
    except Exception:  # pragma: no cover - adapter variance
        definition = ""

    genes: list[str] = []
    try:
        for _subject, predicate, obj in adapter.relationships([mondo_id]):
            if predicate != GENE_RELATION:
                continue
            symbol = adapter.label(obj) or obj
            if symbol not in genes:
                genes.append(symbol)
    except Exception:  # pragma: no cover - adapter variance
        pass

    omim_ids: list[str] = []
    try:
        for _predicate, target in adapter.simple_mappings_by_curie(mondo_id) or []:
            if not str(target).upper().startswith("OMIM:"):
                continue
            digits = str(target).split(":", 1)[1].strip()
            if digits.isdigit() and digits not in omim_ids:
                omim_ids.append(digits)
    except Exception:  # pragma: no cover - adapter variance
        pass

    synonyms: list[str] = []
    try:
        synonyms = [str(s) for s in (adapter.entity_aliases(mondo_id) or [])]
    except Exception:  # pragma: no cover - adapter variance
        pass

    return MondoRecord(
        id=mondo_id,
        label=label,
        definition=definition,
        genes=tuple(genes),
        omim_ids=tuple(omim_ids),
        synonyms=tuple(synonyms),
    )


def assess(
    record: MondoRecord,
    gene_counts: Counter,
    report_omim: set[str] | None = None,
    *,
    report: str = "",
    min_signal: int = DEFAULT_MIN_SIGNAL,
    rival_ratio: float = DEFAULT_RIVAL_RATIO,
    lexicon_name: str = "hgnc",
) -> PreflightResult:
    """Compare a report's gene mentions against a MONDO entity's canonical gene."""
    report_omim = report_omim or set()
    expected = list(record.genes)
    expected_mentions = {g: gene_counts.get(g, 0) for g in expected}
    expected_total = sum(expected_mentions.values())

    rivals = [
        (sym, n)
        for sym, n in gene_counts.most_common()
        if sym not in set(expected) and n >= min_signal
    ]

    result = PreflightResult(
        verdict=SKIP,
        mondo=record.id,
        mondo_label=record.label,
        report=report,
        expected_genes=expected,
        expected_mentions=expected_mentions,
        top_genes=gene_counts.most_common(10),
        rival_genes=rivals[:10],
        expected_omim=list(record.omim_ids),
        report_omim=sorted(report_omim),
        lexicon=lexicon_name,
    )

    if not expected:
        result.verdict = SKIP
        result.reasons.append(
            f"MONDO records no causal gene ({GENE_RELATION}) for {record.id} "
            f"({record.label or 'unlabelled'}); the gene-identity check cannot "
            "discriminate. Fall back to the manual OMIM/synonym preflight."
        )
        return result

    expected_str = "/".join(expected)

    if expected_total == 0 and rivals:
        result.verdict = FAIL
        top_sym, top_n = rivals[0]
        result.reasons.append(
            f"Expected gene {expected_str} is never mentioned, but {top_sym} is "
            f"mentioned {top_n} times. The report is most likely about a "
            "different disease entity — discard it rather than cherry-picking."
        )
        return result

    if expected_total == 0:
        result.verdict = WARN
        result.reasons.append(
            f"No gene mentions found at all, so {expected_str} could not be "
            "confirmed. Verify the report's disease identity manually."
        )
        return result

    result.verdict = PASS
    result.reasons.append(
        f"Expected gene {expected_str} is mentioned {expected_total} times."
    )

    if rivals and rivals[0][1] >= expected_total * rival_ratio:
        result.verdict = WARN
        rival_sym, rival_n = rivals[0]
        result.reasons.append(
            f"Rival gene {rival_sym} is mentioned {rival_n} times "
            f"({rival_n / expected_total:.0%} of {expected_str}). The report may "
            "mix in a second disease entity — exclude those sections before curating."
        )

    if record.omim_ids and report_omim and not (set(record.omim_ids) & report_omim):
        if result.verdict == PASS:
            result.verdict = WARN
        result.reasons.append(
            f"Report cites OMIM {', '.join(sorted(report_omim))} but "
            f"{record.id} xrefs OMIM {', '.join(record.omim_ids)}."
        )

    return result


def preflight(
    report_path: str | Path,
    mondo_id: str,
    *,
    adapter=None,
    lexicon=None,
    min_signal: int = DEFAULT_MIN_SIGNAL,
    rival_ratio: float = DEFAULT_RIVAL_RATIO,
) -> PreflightResult:
    """Run the full NEC preflight on a report file against a MONDO ID."""
    text = Path(report_path).read_text(encoding="utf-8")
    lexicon = lexicon if lexicon is not None else HgncLexicon()
    record = fetch_mondo_record(mondo_id, adapter=adapter)
    counts = extract_gene_mentions(text, lexicon)
    return assess(
        record,
        counts,
        extract_omim_ids(text),
        report=str(report_path),
        min_signal=min_signal,
        rival_ratio=rival_ratio,
        lexicon_name=getattr(lexicon, "name", "custom"),
    )


def format_report(result: PreflightResult) -> str:
    lines = [
        f"{result.verdict}  {result.report}",
        f"  intended entity : {result.mondo} {result.mondo_label}".rstrip(),
        f"  canonical gene  : {'/'.join(result.expected_genes) or '(none recorded)'}",
    ]
    if result.expected_mentions:
        mentions = ", ".join(
            f"{g}={n}" for g, n in sorted(result.expected_mentions.items())
        )
        lines.append(f"  mentions        : {mentions}")
    if result.top_genes:
        top = ", ".join(f"{g}={n}" for g, n in result.top_genes[:5])
        lines.append(f"  top genes       : {top}")
    if result.expected_omim or result.report_omim:
        lines.append(
            f"  OMIM (MONDO)    : {', '.join(result.expected_omim) or '-'}"
        )
        lines.append(
            f"  OMIM (report)   : {', '.join(result.report_omim[:8]) or '-'}"
        )
    if result.lexicon != "hgnc":
        lines.append(f"  lexicon         : {result.lexicon} (HGNC unavailable)")
    for reason in result.reasons:
        lines.append(f"  - {reason}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Named Entity Confusion (NEC) preflight: check that a deep-research "
            "report is about the disease entity you intend to curate (issue #3889)."
        )
    )
    parser.add_argument("report", help="Path to the deep-research markdown report.")
    parser.add_argument("mondo", help="MONDO ID of the intended disease, e.g. MONDO:0014572.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero on WARN as well as FAIL.",
    )
    parser.add_argument(
        "--no-hgnc",
        action="store_true",
        help="Skip HGNC validation of gene tokens (offline heuristic mode; noisier).",
    )
    parser.add_argument(
        "--min-signal",
        type=int,
        default=DEFAULT_MIN_SIGNAL,
        help=f"Mentions before a rival gene counts as substantive (default {DEFAULT_MIN_SIGNAL}).",
    )
    parser.add_argument(
        "--rival-ratio",
        type=float,
        default=DEFAULT_RIVAL_RATIO,
        help=(
            "Rival-to-expected mention ratio that triggers a contamination WARN "
            f"(default {DEFAULT_RIVAL_RATIO})."
        ),
    )
    args = parser.parse_args(argv)

    mondo = args.mondo.strip()
    if not mondo.upper().startswith("MONDO:"):
        parser.error(f"expected a MONDO CURIE, got {args.mondo!r}")

    result = preflight(
        args.report,
        mondo,
        lexicon=HeuristicLexicon() if args.no_hgnc else None,
        min_signal=args.min_signal,
        rival_ratio=args.rival_ratio,
    )

    if args.json:
        print(json.dumps(asdict(result), indent=2))
    else:
        print(format_report(result))

    if result.verdict == FAIL:
        return 1
    if result.verdict == WARN and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
