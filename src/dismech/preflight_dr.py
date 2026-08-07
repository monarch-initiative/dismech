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
    no genes could be found at all, or the canonical gene is mentioned fewer
    than ``min_signal`` times, or a lookup the verdict depends on failed. This
    is the Temtamy pattern (PR #3835): a single report mixing C12orf57 and
    CHSY1 content. Sections about the rival entity must be excluded before
    curating.
``PASS``
    The canonical gene dominates the report's gene mentions.
``SKIP``
    MONDO records no causal gene for this entity (complex/multifactorial
    disease, or a grouping term). The check cannot discriminate; fall back to
    the manual OMIM/synonym preflight.

Failure directions
------------------
This is a safety gate, so every degraded path is biased *away* from a clean
bill of health and away from a spurious "discard the report":

* If the HGNC lexicon cannot be reached, the run does not quietly stop
  recognising gene symbols (which would turn the Lichtenstein-Knorr ``FAIL``
  into a ``WARN``). It falls back to :class:`HeuristicLexicon` and says so.
* If a MONDO lookup *fails*, that is reported as a failure rather than as an
  affirmative "MONDO records no causal gene", and it caps the verdict at
  ``WARN``.
* If the canonical gene's symbol cannot be resolved to something a report
  could plausibly contain (i.e. it is still a bare CURIE), the verdict is
  ``WARN`` — never ``FAIL``, which would tell the curator to bin a correct
  report.
* A single incidental mention of the canonical gene is not enough for
  ``PASS``; ``min_signal`` applies to the expected gene as well as to rivals.
* ``FAIL`` is only issued when nothing contradicts it. If a lookup failed
  (so the alias rescue that could have found the canonical gene never ran),
  or if the report's OMIM IDs agree with the MONDO xref (an *independent*
  identity anchor pointing at the right disease), the verdict is capped at
  ``WARN``.
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
#
# The pattern is case-sensitive by design, which means an ALL-CAPS heading can
# smuggle an ordinary English word in as a "gene" (CAT, SET, SPARC and IMPACT
# are all real HGNC symbols). Note the direction of that bias: such a token can
# only ever be a *rival*, so at worst it inflates a rival past ``min_signal``
# and produces a spurious WARN. It can never suppress the expected gene, and so
# can never manufacture a FAIL.
GENE_TOKEN_RE = re.compile(
    r"\b(?:C\d{1,2}orf\d{1,3}|[A-Z][A-Z0-9]{1,9}(?:-[A-Z0-9]{1,6})?)\b"
)

# A CURIE that survived symbol resolution, e.g. "HGNC:11071". If the canonical
# gene is still shaped like this, no DR report will ever mention it, so the
# gene-frequency comparison is meaningless rather than damning.
CURIE_SHAPED_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_.]*:\S+$")

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
    genes: tuple[str, ...] = ()
    omim_ids: tuple[str, ...] = ()
    #: Entries of :attr:`genes` that could not be resolved to a gene *symbol*
    #: and are still bare CURIEs. A report can never mention these, so they
    #: must not be read as evidence that the report is about another disease.
    unresolved_genes: tuple[str, ...] = ()
    #: Canonical symbol -> previous/alias symbols as HGNC records them. A
    #: report written in terms of SLC9A1's previous symbol "PPP1R143" is still
    #: about SLC9A1. Only symbols HGNC actually lists are rescued: a purely
    #: protein-level name (NHE1) is not an HGNC alias and will not be.
    gene_aliases: dict[str, tuple[str, ...]] = field(default_factory=dict)
    #: Human-readable descriptions of lookups that *failed* (as opposed to
    #: lookups that legitimately returned nothing). Never silently dropped.
    lookup_errors: tuple[str, ...] = ()


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
    #: Why a degraded lexicon is in use, if it is. Empty for a live HGNC run
    #: and for a deliberate ``--no-hgnc`` run.
    lexicon_note: str = ""
    #: Alias symbol -> count, for aliases that actually occur in the report.
    alias_mentions: dict[str, int] = field(default_factory=dict)
    #: Lookups that failed while assembling the comparison (see MondoRecord).
    lookup_errors: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return self.verdict in (PASS, SKIP)


class LexiconUnavailable(RuntimeError):
    """The HGNC gene-symbol lexicon could not be reached.

    Raised rather than swallowed: a lexicon that silently rejects every token
    makes the report look gene-free, which downgrades a ``FAIL`` to a ``WARN``
    -- exactly the wrong direction for a safety gate.
    """


class HgncLexicon:
    """Gene-symbol membership test backed by the OAK HGNC adapter.

    Lookups are memoised because a DR report yields a few hundred distinct
    candidate tokens and each one would otherwise hit SQLite.
    """

    name = "hgnc"

    #: A symbol the adapter must be able to resolve for the lexicon to be
    #: considered live. It is the canonical gene of NEC case 1.
    PROBE_SYMBOL = "SLC9A1"

    def __init__(self, adapter=None):
        self._adapter = adapter
        self._cache: dict[str, bool] = {}

    def _get_adapter(self):
        if self._adapter is None:
            try:
                from oaklib import get_adapter

                self._adapter = get_adapter("sqlite:obo:hgnc")
            except Exception as exc:  # pragma: no cover - install/network failure
                raise LexiconUnavailable(
                    f"could not open the HGNC adapter (sqlite:obo:hgnc): {exc}"
                ) from exc
        return self._adapter

    def probe(self) -> None:
        """Raise :class:`LexiconUnavailable` unless the adapter really answers.

        Checked once up front so a dead adapter is reported as a dead adapter
        rather than as "this report mentions no genes".
        """
        adapter = self._get_adapter()
        try:
            hits = list(adapter.curies_by_label(self.PROBE_SYMBOL))
        except Exception as exc:  # pragma: no cover - adapter/network failure
            raise LexiconUnavailable(
                f"the HGNC adapter failed to answer a lookup: {exc}"
            ) from exc
        if not hits:
            raise LexiconUnavailable(
                f"the HGNC adapter did not resolve the probe symbol "
                f"{self.PROBE_SYMBOL}; it is empty or not the expected ontology"
            )

    def __contains__(self, symbol: str) -> bool:
        if symbol not in self._cache:
            adapter = self._get_adapter()
            try:
                hits = list(adapter.curies_by_label(symbol))
            except Exception as exc:  # pragma: no cover - adapter/network failure
                raise LexiconUnavailable(
                    f"the HGNC adapter failed while looking up {symbol!r}: {exc}"
                ) from exc
            self._cache[symbol] = bool(hits)
        return self._cache[symbol]


class HeuristicLexicon:
    """Fallback lexicon: everything that is not a known non-gene acronym.

    Noisier than :class:`HgncLexicon` -- used only when HGNC is unavailable.
    """

    name = "heuristic"

    def __init__(self, reason: str = ""):
        #: Why HGNC was not used, surfaced in the report output.
        self.reason = reason

    def __contains__(self, symbol: str) -> bool:
        return symbol.upper() not in NON_GENE_TOKENS


def default_lexicon(*, allow_fallback: bool = True):
    """Return a live HGNC lexicon, or an explicitly-degraded heuristic one.

    The fallback is *labelled* (``lexicon: heuristic (HGNC unavailable)`` in
    the output) so a degraded run can never be mistaken for a clean one.
    """
    lexicon = HgncLexicon()
    try:
        lexicon.probe()
    except LexiconUnavailable as exc:
        if not allow_fallback:
            raise
        return HeuristicLexicon(reason=str(exc))
    return lexicon


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


def _is_curie_shaped(value: str) -> bool:
    """True if ``value`` still looks like ``PREFIX:LOCALID`` rather than a symbol."""
    return bool(CURIE_SHAPED_RE.match(value))


def _symbol_like(value: str) -> bool:
    """True if ``value`` could plausibly be matched in report prose as a gene."""
    match = GENE_TOKEN_RE.fullmatch(value)
    return bool(match) and value.upper() not in NON_GENE_TOKENS


def fetch_mondo_record(
    mondo_id: str, adapter=None, hgnc_adapter=None, *, use_hgnc: bool = True
) -> MondoRecord:
    """Look up the label, causal gene(s), and OMIM xrefs for a MONDO term.

    The causal gene comes from the ``RO:0004003`` relation. Contrary to an
    earlier note in ``CLAUDE.md``, the local ``sqlite:obo:mondo`` adapter does
    expose this relation.

    The relation's object is an HGNC CURIE, so it has to be resolved to a
    symbol before it can be compared against report prose. MONDO usually
    carries the label, but when it does not the HGNC adapter is asked; if that
    also fails the CURIE is recorded in
    :attr:`MondoRecord.unresolved_genes` so the caller can refuse to draw a
    conclusion from it. Every lookup that *errors* (as opposed to legitimately
    returning nothing) is recorded in :attr:`MondoRecord.lookup_errors`.

    ``use_hgnc=False`` keeps the whole function offline: HGNC is never opened,
    so ``--no-hgnc`` really is an offline mode rather than only a swap of the
    token lexicon.
    """
    if adapter is None:
        from oaklib import get_adapter

        adapter = get_adapter("sqlite:obo:mondo")

    errors: list[str] = []

    # The HGNC adapter is only needed to repair a missing label or to pull
    # aliases, so it is built lazily and its absence is not fatal.
    hgnc_state: dict[str, object] = {
        "adapter": hgnc_adapter,
        "tried": hgnc_adapter is not None or not use_hgnc,
    }

    def _hgnc():
        if not hgnc_state["tried"]:
            hgnc_state["tried"] = True
            try:
                from oaklib import get_adapter

                hgnc_state["adapter"] = get_adapter("sqlite:obo:hgnc")
            except Exception as exc:  # pragma: no cover - install/network failure
                errors.append(f"HGNC adapter unavailable for symbol resolution: {exc}")
                hgnc_state["adapter"] = None
        return hgnc_state["adapter"]

    try:
        label = adapter.label(mondo_id) or ""
    except Exception as exc:  # pragma: no cover - adapter variance
        errors.append(f"label lookup for {mondo_id} failed: {exc}")
        label = ""

    genes: list[str] = []
    unresolved: list[str] = []
    aliases: dict[str, tuple[str, ...]] = {}
    try:
        relationships = list(adapter.relationships([mondo_id]))
    except Exception as exc:
        errors.append(
            f"causal-gene lookup ({GENE_RELATION}) for {mondo_id} failed: {exc}"
        )
        relationships = []

    for _subject, predicate, obj in relationships:
        if predicate != GENE_RELATION:
            continue
        symbol, resolved = _resolve_gene_symbol(obj, adapter, _hgnc, errors)
        if symbol in genes:
            continue
        genes.append(symbol)
        if not resolved:
            unresolved.append(symbol)
            continue
        gene_aliases = _gene_aliases(obj, symbol, _hgnc, errors)
        if gene_aliases:
            aliases[symbol] = gene_aliases

    omim_ids: list[str] = []
    try:
        mappings = adapter.simple_mappings_by_curie(mondo_id) or []
    except Exception as exc:
        errors.append(f"OMIM xref lookup for {mondo_id} failed: {exc}")
        mappings = []
    for _predicate, target in mappings:
        if not str(target).upper().startswith("OMIM:"):
            continue
        digits = str(target).split(":", 1)[1].strip()
        if digits.isdigit() and digits not in omim_ids:
            omim_ids.append(digits)

    return MondoRecord(
        id=mondo_id,
        label=label,
        genes=tuple(genes),
        omim_ids=tuple(omim_ids),
        unresolved_genes=tuple(unresolved),
        gene_aliases=aliases,
        lookup_errors=tuple(errors),
    )


def _resolve_gene_symbol(curie, adapter, hgnc_getter, errors: list[str]) -> tuple[str, bool]:
    """Resolve an ``RO:0004003`` object to a gene symbol.

    Returns ``(symbol_or_curie, resolved)``. ``resolved`` is False when the
    best available value is still a bare CURIE -- a state that must produce a
    WARN rather than a FAIL, because no correct report would contain it.
    """
    curie = str(curie)
    try:
        symbol = adapter.label(curie) or ""
    except Exception as exc:  # pragma: no cover - adapter variance
        errors.append(f"gene-symbol lookup for {curie} failed in MONDO: {exc}")
        symbol = ""

    if not symbol or _is_curie_shaped(symbol):
        hgnc = hgnc_getter()
        if hgnc is not None:
            try:
                for variant in _curie_variants(curie):
                    repaired = hgnc.label(variant)
                    if repaired:
                        symbol = repaired
                        break
            except Exception as exc:  # pragma: no cover - adapter variance
                errors.append(f"gene-symbol lookup for {curie} failed in HGNC: {exc}")

    if not symbol or _is_curie_shaped(symbol):
        errors.append(
            f"could not resolve {curie} to a gene symbol; "
            "the gene-frequency comparison cannot be made against a bare CURIE"
        )
        return curie, False
    return symbol, True


def _curie_variants(curie: str) -> tuple[str, ...]:
    """The CURIE plus its opposite-cased prefix, e.g. ``hgnc:11071``.

    MONDO emits ``HGNC:11071`` while this repository's canonical form is
    lowercase ``hgnc:`` (see ``CLAUDE.md`` -> "CURIE Prefix Casing"). An OAK
    adapter keyed on the other casing answers such a lookup with an empty
    result *without raising*, which would make the alias rescue silently inert
    -- and that rescue is load-bearing for not manufacturing a ``FAIL``.
    """
    curie = str(curie)
    if ":" not in curie:
        return (curie,)
    prefix, local = curie.split(":", 1)
    variants = [curie]
    for alternative in (prefix.upper(), prefix.lower()):
        candidate = f"{alternative}:{local}"
        if candidate not in variants:
            variants.append(candidate)
    return tuple(variants)


def _alias_belongs_elsewhere(alias: str, curie: str, hgnc, errors: list[str]) -> bool:
    """True if ``alias`` is the *approved* symbol of some other HGNC gene.

    ``claimed`` in :func:`assess` both credits an alias to the expected gene and
    removes it from the rival list, so an alias that collides with another
    gene's approved symbol would be double-discounted and bias the verdict
    towards ``PASS``. On a lookup failure the alias is *kept* (and the failure
    recorded): dropping it could suppress the expected gene's count and
    manufacture a ``FAIL``, which is the worse direction to be wrong in.
    """
    lookup = getattr(hgnc, "curies_by_label", None)
    if lookup is None:  # adapter cannot answer; not a failure, just a gap
        return False
    try:
        hits = list(lookup(alias) or [])
    except Exception as exc:  # pragma: no cover - adapter variance
        errors.append(f"alias collision check for {alias} failed: {exc}")
        return False
    if not hits:
        return False
    own = {c.lower() for c in _curie_variants(curie)}
    return not any(str(hit).lower() in own for hit in hits)


def _gene_aliases(curie, symbol: str, hgnc_getter, errors: list[str]) -> tuple[str, ...]:
    """Previous/alias symbols for a gene, so ``PPP1R143`` still counts for ``SLC9A1``.

    Aliases are filtered to symbol-shaped tokens the report scanner could
    actually produce; free-text names ("sodium/hydrogen exchanger 1") are
    dropped because :data:`GENE_TOKEN_RE` would never emit them. The gene's own
    approved symbol is dropped -- it is already counted directly, and leaving it
    in would double it. Aliases that are *another* gene's approved symbol are
    dropped too (see :func:`_alias_belongs_elsewhere`).
    """
    hgnc = hgnc_getter()
    if hgnc is None:
        return ()
    curie = str(curie)
    raw: list = []
    try:
        for variant in _curie_variants(curie):
            # ``entity_aliases`` on the wrong prefix casing answers ``[None]``
            # rather than raising, so a truthiness test on the raw list is not
            # enough to tell "this variant is the right key" from "it is not".
            candidates = [a for a in (hgnc.entity_aliases(variant) or []) if a]
            if candidates:
                raw = candidates
                break
    except Exception as exc:  # pragma: no cover - adapter variance
        errors.append(f"alias lookup for {curie} failed: {exc}")
        return ()
    seen: list[str] = []
    for alias in raw:
        alias = str(alias).strip()
        if not _symbol_like(alias) or alias in seen or alias == symbol:
            continue
        if _alias_belongs_elsewhere(alias, curie, hgnc, errors):
            continue
        seen.append(alias)
    return tuple(seen)


def assess(
    record: MondoRecord,
    gene_counts: Counter,
    report_omim: set[str] | None = None,
    *,
    report: str = "",
    min_signal: int = DEFAULT_MIN_SIGNAL,
    rival_ratio: float = DEFAULT_RIVAL_RATIO,
    lexicon_name: str = "hgnc",
    lexicon_note: str = "",
) -> PreflightResult:
    """Compare a report's gene mentions against a MONDO entity's canonical gene."""
    report_omim = report_omim or set()
    expected = list(record.genes)
    unresolved = set(record.unresolved_genes)
    resolvable = [g for g in expected if g not in unresolved]

    # An alias mention counts towards its canonical gene: a report that writes
    # a previous HGNC symbol throughout ("PPP1R143" for SLC9A1) is still about
    # that gene, and must not be binned as NEC.
    alias_mentions: dict[str, int] = {}
    expected_mentions: dict[str, int] = {}
    alias_symbols: set[str] = set()
    for gene in expected:
        total = gene_counts.get(gene, 0)
        for alias in record.gene_aliases.get(gene, ()):
            alias_symbols.add(alias)
            hits = gene_counts.get(alias, 0)
            if hits:
                alias_mentions[alias] = alias_mentions.get(alias, 0) + hits
                total += hits
        expected_mentions[gene] = total
    expected_total = sum(expected_mentions[g] for g in resolvable)

    claimed = set(expected) | alias_symbols
    rivals = [
        (sym, n)
        for sym, n in gene_counts.most_common()
        if sym not in claimed and n >= min_signal
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
        lexicon_note=lexicon_note,
        alias_mentions=alias_mentions,
        lookup_errors=list(record.lookup_errors),
    )

    def _cap_at_warn() -> None:
        """A lookup that errored must never leave the run looking clean."""
        if result.lookup_errors and result.verdict in (PASS, SKIP):
            result.verdict = WARN

    if not expected:
        if record.lookup_errors:
            result.verdict = WARN
            result.reasons.append(
                f"The causal-gene lookup for {record.id} did not complete, so it is "
                "unknown whether MONDO records a gene. This is a failed lookup, not "
                "an absent edge — fix the adapter or run the manual preflight."
            )
            return result
        result.verdict = SKIP
        result.reasons.append(
            f"MONDO records no causal gene ({GENE_RELATION}) for {record.id} "
            f"({record.label or 'unlabelled'}); the gene-identity check cannot "
            "discriminate. Fall back to the manual OMIM/synonym preflight."
        )
        return result

    if not resolvable:
        result.verdict = WARN
        result.reasons.append(
            f"Could not resolve {', '.join(sorted(unresolved))} to a gene symbol, so "
            "the report's gene mentions cannot be compared against it. This is a "
            "lookup failure, not evidence about the report — run the manual preflight."
        )
        return result

    expected_str = "/".join(resolvable)

    if expected_total == 0 and rivals:
        top_sym, top_n = rivals[0]
        omim_agrees = bool(record.omim_ids and (set(record.omim_ids) & report_omim))
        # FAIL is the tool's most destructive instruction ("discard the
        # report"), so it is issued only when nothing contradicts it. A lookup
        # that failed is exactly the lookup that could have found the expected
        # gene under an alias, and an OMIM match is an *independent* identity
        # anchor. Either one downgrades to WARN.
        if record.lookup_errors:
            result.verdict = WARN
            result.reasons.append(
                f"Expected gene {expected_str} is never mentioned while {top_sym} is "
                f"mentioned {top_n} times — but an ontology lookup failed, so alias "
                "symbols could not be checked and the absence of the canonical symbol "
                "is not conclusive. Verify the report's identity manually rather than "
                "discarding it on this evidence."
            )
        elif omim_agrees:
            result.verdict = WARN
            shared = ", ".join(sorted(set(record.omim_ids) & report_omim))
            result.reasons.append(
                f"Expected gene {expected_str} is never mentioned while {top_sym} is "
                f"mentioned {top_n} times, but the report cites OMIM {shared}, which "
                f"matches the {record.id} xref. That independent identity anchor "
                "contradicts the gene-frequency signal — reconcile the two manually "
                "instead of discarding the report."
            )
        else:
            result.verdict = FAIL
            result.reasons.append(
                f"Expected gene {expected_str} is never mentioned, but {top_sym} is "
                f"mentioned {top_n} times. The report is most likely about a "
                "different disease entity — discard it rather than cherry-picking."
            )
        if result.lookup_errors:
            result.reasons.append(
                "Some ontology lookups failed, so this verdict is incomplete: "
                + "; ".join(result.lookup_errors)
            )
        return result

    if expected_total == 0:
        result.verdict = WARN
        result.reasons.append(
            f"No gene mentions found at all, so {expected_str} could not be "
            "confirmed. Verify the report's disease identity manually."
        )
        _cap_at_warn()
        return result

    if expected_total < min_signal:
        result.verdict = WARN
        result.reasons.append(
            f"Expected gene {expected_str} is mentioned only {expected_total} "
            f"time(s), below the {min_signal}-mention threshold for a substantive "
            "discussion. A passing mention in a citation title or pathway list is "
            "not evidence the report is about this disease — verify manually."
        )
    else:
        result.verdict = PASS
        result.reasons.append(
            f"Expected gene {expected_str} is mentioned {expected_total} times."
        )

    if alias_mentions:
        result.reasons.append(
            "Counted HGNC alias mention(s) towards the canonical gene: "
            + ", ".join(f"{sym}={n}" for sym, n in sorted(alias_mentions.items()))
            + "."
        )

    if rivals and rivals[0][1] >= expected_total * rival_ratio:
        result.verdict = WARN
        rival_sym, rival_n = rivals[0]
        result.reasons.append(
            f"Rival gene {rival_sym} is mentioned {rival_n} times "
            f"({rival_n / expected_total:.0%} of {expected_str}). The report may "
            "mix in a second disease entity — exclude those sections before curating."
        )

    if unresolved:
        if result.verdict == PASS:
            result.verdict = WARN
        result.reasons.append(
            f"{record.id} records a further causal gene "
            f"({', '.join(sorted(unresolved))}) that could not be resolved to a "
            "symbol and was therefore excluded from the comparison."
        )

    if record.omim_ids and report_omim and not (set(record.omim_ids) & report_omim):
        if result.verdict == PASS:
            result.verdict = WARN
        result.reasons.append(
            f"Report cites OMIM {', '.join(sorted(report_omim))} but "
            f"{record.id} xrefs OMIM {', '.join(record.omim_ids)}."
        )

    _cap_at_warn()
    if result.lookup_errors:
        result.reasons.append(
            "Some ontology lookups failed, so this verdict is incomplete: "
            + "; ".join(result.lookup_errors)
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
    use_hgnc: bool = True,
) -> PreflightResult:
    """Run the full NEC preflight on a report file against a MONDO ID.

    ``use_hgnc=False`` is a genuine offline mode: neither the token lexicon nor
    the MONDO symbol/alias repair opens the HGNC adapter.
    """
    text = Path(report_path).read_text(encoding="utf-8")
    if lexicon is None:
        lexicon = HeuristicLexicon() if not use_hgnc else default_lexicon()
    record = fetch_mondo_record(mondo_id, adapter=adapter, use_hgnc=use_hgnc)
    try:
        counts = extract_gene_mentions(text, lexicon)
    except LexiconUnavailable as exc:
        # The adapter died mid-run (it answered the probe, then stopped). Never
        # continue with a lexicon that rejects everything: that empties the gene
        # counts and silently downgrades a FAIL to a WARN.
        lexicon = HeuristicLexicon(reason=str(exc))
        counts = extract_gene_mentions(text, lexicon)
    return assess(
        record,
        counts,
        extract_omim_ids(text),
        report=str(report_path),
        min_signal=min_signal,
        rival_ratio=rival_ratio,
        lexicon_name=getattr(lexicon, "name", "custom"),
        lexicon_note=getattr(lexicon, "reason", ""),
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
    if result.alias_mentions:
        aliases = ", ".join(f"{g}={n}" for g, n in sorted(result.alias_mentions.items()))
        lines.append(f"  alias mentions  : {aliases}")
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
        suffix = f" (HGNC unavailable: {result.lexicon_note})" if result.lexicon_note else ""
        lines.append(f"  lexicon         : {result.lexicon}{suffix}")
    for error in result.lookup_errors:
        lines.append(f"  ! lookup failed : {error}")
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
        help=(
            "Do not open the HGNC adapter at all: gene tokens are accepted by the "
            "heuristic lexicon and MONDO gene symbols are not repaired or expanded "
            "to aliases (offline mode; noisier)."
        ),
    )
    parser.add_argument(
        "--require-hgnc",
        action="store_true",
        help=(
            "Fail loudly instead of falling back to the heuristic lexicon when the "
            "HGNC adapter is unavailable (use this when gating CI)."
        ),
    )
    parser.add_argument(
        "--min-signal",
        type=int,
        default=DEFAULT_MIN_SIGNAL,
        help=(
            "Mentions before a gene counts as substantive, applied to the expected "
            f"gene as well as to rivals (default {DEFAULT_MIN_SIGNAL})."
        ),
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

    if args.no_hgnc and args.require_hgnc:
        parser.error("--no-hgnc and --require-hgnc are mutually exclusive")

    if args.no_hgnc:
        lexicon = HeuristicLexicon()
    else:
        try:
            lexicon = default_lexicon(allow_fallback=not args.require_hgnc)
        except LexiconUnavailable as exc:
            parser.exit(2, f"error: {exc}\n")

    result = preflight(
        args.report,
        mondo,
        lexicon=lexicon,
        min_signal=args.min_signal,
        rival_ratio=args.rival_ratio,
        use_hgnc=not args.no_hgnc,
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
