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
    CHSY1 content. A mention count cannot tell that apart from a report on
    the right disease that names the disease's own receptor, ligand, fusion
    partner or modifier gene: in KDM1A-related adrenal hyperplasia (#9826)
    the effector gene GIP reaches 0.44 of KDM1A, above the 0.40 the Temtamy
    rival reached, so no ratio separates the two. Read the sections naming
    the second gene and exclude them only if they are about another disease.
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
  the verdict is capped at ``WARN``.

What an OMIM match does and does not show
-----------------------------------------
A report that cites the OMIM number MONDO xrefs was pointed at the right
identifier. It does not follow that its text is about the right gene: the
immunodeficiency 97 report (#12166) cites OMIM 619802 and is about TBK1, never
naming the canonical gene PIK3CG. So when the canonical gene is never
mentioned, the matching OMIM number is reported as context and decides nothing
on its own. What decides is :func:`find_rival_diseases`: if a gene the report
does discuss is MONDO's ``RO:0004003`` cause of a *different* disease
(TBK1 -> MONDO:0971173), the report's subject is identified and the verdict is
``FAIL`` whatever the OMIM citation says. Only when no rival resolves to
another disease does the OMIM match keep the verdict at ``WARN``: that is the
report written throughout in a protein name the HGNC alias rescue does not
cover (NHE1 for SLC9A1), which a mention count alone would bin.
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

# Ontology prefixes that are also HGNC symbols, or that the uppercase token
# pattern picks up as one. CURIE_RE removes them when they carry a local ID,
# but reports also name the ontology in prose ("HP calls it Optic atrophy",
# "(HP terms)"), and 40 such bare mentions put haptoglobin among the top
# "rival" genes of a correct ACO2 report (#9826). These are kept out of the
# rival pool only: a disease whose own causal gene is HP still counts it.
ONTOLOGY_PREFIX_TOKENS = frozenset({
    "HP", "HPO", "GO", "CL", "MP", "SO", "MONDO", "PATO", "UBERON", "NCIT",
    "CHEBI", "ECTO", "MAXO", "ORPHA", "OMIM", "HGNC",
})

# A gene needs at least this many mentions before it counts as "discussed
# substantively". Below it, a symbol is usually an aside, a pathway member, or a
# gene named once in a citation title -- not the subject of the report.
DEFAULT_MIN_SIGNAL = 3

# A rival gene mentioned at least this fraction as often as the expected gene
# marks the report as contaminated. Tuned against the Temtamy report, where the
# wrong-entity gene CHSY1 (23) reaches 0.40 of C12orf57 (57).
DEFAULT_RIVAL_RATIO = 0.25

# How many of the most-mentioned rival genes are looked up for a MONDO disease
# of their own. The first rival is not enough: in the #12166 report TNF (58)
# out-ranks TBK1 (47), and only TBK1 is the recorded cause of a disease.
MAX_RIVAL_LOOKUPS = 5

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
    #: Rival gene -> the ``(MONDO id, label)`` pairs MONDO records it as the
    #: ``RO:0004003`` cause of, other than the intended entity. Filled only
    #: when the canonical gene is never mentioned (see :func:`find_rival_diseases`).
    rival_diseases: dict[str, list[tuple[str, str]]] = field(default_factory=dict)

    @property
    def expected_absent(self) -> bool:
        """True when no resolvable canonical gene is named even once.

        Kept apart from a low count: ``PIK3CG=0`` means the report never
        discusses the gene, ``PIK3CG=2`` means it does so in passing.
        """
        return bool(self.expected_mentions) and not any(self.expected_mentions.values())

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


MONDO_ADAPTER = "sqlite:obo:mondo"


class MondoBuildUnavailable(RuntimeError):
    """The local ``mondo.db`` build is absent, so the preflight cannot run.

    Raised instead of opening the adapter, because opening it does not fail on a
    missing build: semsql downloads ``mondo.db`` (232 MB compressed, 1.3 GB on
    disk) with no prompt (#12687). Nor is an empty :class:`MondoRecord` an
    acceptable answer, since it reads as "MONDO records no causal gene" and
    turns into a ``SKIP`` verdict.
    """


def open_mondo_adapter():
    """Open the local MONDO build, refusing to download it.

    The build is fetched deliberately with ``just fetch-ontology-dbs mondo``.
    ``conf/oak_config.yaml`` routes MONDO to ``ols:mondo`` for term validation,
    but this check needs the ``RO:0004003`` causal-gene edges and OMIM xrefs,
    which it reads from the local build.
    """
    from dismech.oak_db import local_build_path, local_build_present

    if not local_build_present(MONDO_ADAPTER):
        raise MondoBuildUnavailable(
            f"the local MONDO build is not present at {local_build_path('mondo')}. "
            "preflight-dr reads the MONDO causal gene and OMIM xrefs from it and "
            "will not download it implicitly (about 1.3 GB on disk). Fetch it "
            "with `just fetch-ontology-dbs mondo`, then re-run."
        )
    from oaklib import get_adapter

    return get_adapter(MONDO_ADAPTER)


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

    With no ``adapter`` given, the local MONDO build must already be on disk:
    :class:`MondoBuildUnavailable` is raised rather than letting semsql
    download it (see :func:`open_mondo_adapter`).
    """
    if adapter is None:
        adapter = open_mondo_adapter()

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


def _hgnc_curies_for_symbol(symbol: str, adapter, hgnc_adapter=None) -> list[str]:
    """HGNC CURIE(s) whose label is ``symbol``, asking MONDO first, then HGNC.

    MONDO labels the HGNC objects of its ``RO:0004003`` edges, so a gene that
    causes any MONDO disease is found there without opening the HGNC build.
    """
    for source in (adapter, hgnc_adapter):
        if source is None:
            continue
        hits = [
            str(c) for c in (source.curies_by_label(symbol) or [])
            if str(c).lower().startswith("hgnc:")
        ]
        if hits:
            return hits
    return []


def find_rival_diseases(
    symbols, exclude: str, adapter, hgnc_adapter=None
) -> tuple[dict[str, list[tuple[str, str]]], list[str]]:
    """Which of ``symbols`` MONDO records as the cause of a disease other than ``exclude``.

    This is the reverse of the ``RO:0004003`` lookup in
    :func:`fetch_mondo_record`: from a gene the report discusses to the
    disease(s) that gene causes. A hit means the report's subject is a disease
    that exists and is not the one intended (#12166: TBK1 ->
    MONDO:0971173 autoinflammation with arthritis and vasculitis).

    Returns ``(found, errors)``. A symbol with no HGNC identifier, or one whose
    gene causes no MONDO disease, is simply absent from ``found``; a lookup
    that *raises* is recorded in ``errors`` instead, because "could not check"
    is not "checked, nothing there".
    """
    found: dict[str, list[tuple[str, str]]] = {}
    errors: list[str] = []
    for symbol in symbols:
        try:
            curies = _hgnc_curies_for_symbol(symbol, adapter, hgnc_adapter)
        except Exception as exc:
            errors.append(f"HGNC identifier lookup for rival gene {symbol} failed: {exc}")
            continue
        diseases: dict[str, str] = {}
        for curie in curies:
            variants = _curie_variants(curie)
            try:
                edges = list(
                    adapter.relationships(predicates=[GENE_RELATION], objects=list(variants))
                )
            except Exception as exc:
                errors.append(
                    f"reverse {GENE_RELATION} lookup for rival gene {symbol} ({curie}) "
                    f"failed: {exc}"
                )
                continue
            for subject, predicate, obj in edges:
                subject = str(subject)
                if (
                    predicate != GENE_RELATION
                    or str(obj) not in variants
                    or subject == exclude
                    or not subject.upper().startswith("MONDO:")
                    or subject in diseases
                ):
                    continue
                try:
                    diseases[subject] = adapter.label(subject) or ""
                except Exception:  # pragma: no cover - adapter variance
                    diseases[subject] = ""
        if diseases:
            found[symbol] = sorted(diseases.items())
    return found, errors


def _default_rival_lookup(adapter, use_hgnc: bool):
    """A lazy :func:`find_rival_diseases` for :func:`assess`.

    Lazy because it is needed only when the canonical gene is never mentioned,
    so a clean run never opens anything it did not open already. Neither
    build is downloaded: MONDO goes through :func:`open_mondo_adapter`, and
    HGNC, only a fallback for genes MONDO does not label, is skipped when its
    build is absent.
    """

    def _lookup(symbols, exclude):
        mondo = adapter if adapter is not None else open_mondo_adapter()
        hgnc = None
        if use_hgnc:
            from dismech.oak_db import local_build_present

            if local_build_present("sqlite:obo:hgnc"):
                try:
                    from oaklib import get_adapter

                    hgnc = get_adapter("sqlite:obo:hgnc")
                except Exception:  # pragma: no cover - install/network failure
                    hgnc = None
        return find_rival_diseases(symbols, exclude, mondo, hgnc)

    return _lookup


def _describe_rival_diseases(found: dict[str, list[tuple[str, str]]], counts: dict) -> str:
    parts = []
    for symbol, diseases in found.items():
        named = "; ".join(f"{mid} {label}".rstrip() for mid, label in diseases)
        parts.append(f"{symbol} ({counts.get(symbol, 0)} mentions) causes {named}")
    return ", and ".join(parts)


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
    rival_disease_lookup=None,
) -> PreflightResult:
    """Compare a report's gene mentions against a MONDO entity's canonical gene.

    ``rival_disease_lookup(symbols, exclude_mondo_id)`` returns what
    :func:`find_rival_diseases` returns. It is called only when the canonical
    gene is never mentioned; ``None`` skips the check, which then cannot turn
    a ``WARN`` into a ``FAIL``.
    """
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
        if sym not in claimed
        and sym not in ONTOLOGY_PREFIX_TOKENS
        and n >= min_signal
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
        shared = ", ".join(sorted(set(record.omim_ids) & report_omim))
        absent = (
            f"Expected gene {expected_str} is never mentioned (zero mentions, not a "
            "low count)"
        )
        # FAIL is the tool's most destructive instruction ("discard the
        # report"), so it is issued only when nothing contradicts it. A lookup
        # that failed is exactly the lookup that could have found the expected
        # gene under an alias, so it downgrades to WARN. An OMIM match does
        # not: it shows the report was pointed at the right identifier, not
        # that its text is about the right gene (#12166).
        if record.lookup_errors:
            result.verdict = WARN
            result.reasons.append(
                f"{absent} while {top_sym} is mentioned {top_n} times, but an "
                "ontology lookup failed, so alias symbols could not be checked and "
                "the absence of the canonical symbol is not conclusive. Verify the "
                "report's identity manually rather than discarding it on this "
                "evidence."
            )
        else:
            found: dict[str, list[tuple[str, str]]] = {}
            rival_errors: list[str] = []
            # Only a real gene may decide a FAIL. "AR" (autosomal recessive)
            # and "HR" (hazard ratio) are HGNC symbols too, and AR is the cause
            # of Kennedy disease, so an abbreviation-heavy report on the right
            # disease would otherwise be binned.
            checked = [
                sym for sym, _n in rivals if sym.upper() not in NON_GENE_TOKENS
            ][:MAX_RIVAL_LOOKUPS]
            if rival_disease_lookup is not None and checked:
                try:
                    found, rival_errors = rival_disease_lookup(checked, record.id)
                except Exception as exc:
                    rival_errors = [f"rival-gene disease lookup failed: {exc}"]
                result.rival_diseases = dict(found)
                result.lookup_errors.extend(rival_errors)
            omim_note = (
                f" The report does cite OMIM {shared}, which matches the {record.id} "
                "xref; that shows it was pointed at the right identifier, not that "
                f"its text is about {expected_str}, so it does not soften this verdict."
                if shared
                else ""
            )
            if found:
                result.verdict = FAIL
                result.reasons.append(
                    f"{absent}, and MONDO ({GENE_RELATION}) records genes the report "
                    "does discuss as the cause of a different disease: "
                    f"{_describe_rival_diseases(found, dict(gene_counts))}. The report "
                    "is about a disease that exists and is not this one; discard it "
                    f"rather than cherry-picking.{omim_note}"
                )
            elif shared:
                result.verdict = WARN
                if not checked:
                    checked_note = (
                        "Every rival symbol is a common abbreviation (such as AR for "
                        "autosomal recessive), so none was looked up as a gene."
                    )
                elif rival_disease_lookup is None:
                    checked_note = (
                        "The rival genes were not checked for a MONDO disease of their "
                        "own."
                    )
                elif rival_errors:
                    checked_note = (
                        "The rival-gene disease lookup did not complete, so it is "
                        "unknown whether the rival genes cause another MONDO disease."
                    )
                else:
                    checked_note = (
                        "None of the rival genes checked "
                        f"({', '.join(checked)}) is "
                        "MONDO's recorded cause of another disease."
                    )
                result.reasons.append(
                    f"{absent} while {top_sym} is mentioned {top_n} times. The report "
                    f"cites OMIM {shared}, matching the {record.id} xref, but a "
                    "matching identifier shows only that the report was pointed at the "
                    f"right entry, not that its text is about {expected_str}. "
                    f"{checked_note} The report may name {expected_str} only by a "
                    "protein or legacy name the HGNC alias list does not carry. Search "
                    "it for the gene under any name; if it is not there, discard the "
                    "report."
                )
            else:
                result.verdict = FAIL
                result.reasons.append(
                    f"{absent}, but {top_sym} is mentioned {top_n} times. The report "
                    "is most likely about a different disease entity; discard it "
                    "rather than cherry-picking."
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
            f"Second gene {rival_sym} is mentioned {rival_n} times "
            f"({rival_n / expected_total:.0%} of {expected_str}). The report may "
            f"mix in a second disease entity, or {rival_sym} may be this disease's "
            "own receptor, ligand, fusion partner, or modifier gene; a mention "
            "count cannot tell the two apart. Read the sections naming "
            f"{rival_sym} and decide which it is; exclude them only if they are "
            "about a different disease."
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
        rival_disease_lookup=_default_rival_lookup(adapter, use_hgnc),
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
        if result.expected_absent:
            mentions += " (never named)"
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
    for symbol, diseases in result.rival_diseases.items():
        for mondo_id, label in diseases:
            lines.append(f"  rival disease   : {symbol} -> {mondo_id} {label}".rstrip())
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

    # Open MONDO first: without it there is no verdict to give, and failing
    # here also stops the HGNC lexicon below from fetching its own build for a
    # run that cannot finish.
    try:
        mondo_adapter = open_mondo_adapter()
    except MondoBuildUnavailable as exc:
        parser.exit(2, f"error: {exc}\n")

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
        adapter=mondo_adapter,
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
