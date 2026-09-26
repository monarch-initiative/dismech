"""Tests for the NEC (Named Entity Confusion) deep-research preflight (#3889).

The four scenarios named in issue #3889 are each exercised against the *real*
deep-research reports that produced the documented NEC incidents, so the
regression is anchored on the actual failure rather than a synthetic string:

* Case 1 (PASS) -- Temtamy preaxial brachydactyly / CHSY1 (PR #3871)
* Case 2 (FAIL) -- Lichtenstein-Knorr / SLC9A1, report is about SNX14 (PR #3874)
* Case 3 (WARN) -- Temtamy syndrome / C12orf57 contaminated with CHSY1 (PR #3835)
* Case 4 (SKIP) -- a MONDO entity with no single causal gene

MONDO lookups are stubbed so the suite stays offline and deterministic; the
stub values are the ones the live ``sqlite:obo:mondo`` adapter returns.
"""
from __future__ import annotations

import os
from collections import Counter
from pathlib import Path

import pytest

import dismech.preflight_dr as P
from dismech.preflight_dr import (
    FAIL,
    PASS,
    SKIP,
    WARN,
    HeuristicLexicon,
    HgncLexicon,
    LexiconUnavailable,
    MondoBuildUnavailable,
    MondoRecord,
    assess,
    default_lexicon,
    extract_gene_mentions,
    extract_omim_ids,
    fetch_mondo_record,
    find_rival_diseases,
    format_report,
    main,
    preflight,
    strip_curies,
)

RESEARCH = Path(__file__).resolve().parent.parent / "research"

LICHTENSTEIN_KNORR = RESEARCH / "Lichtenstein-Knorr_Syndrome-deep-research-falcon.md"
TEMTAMY = RESEARCH / "Temtamy_Syndrome-deep-research-falcon.md"
TEMTAMY_PREAXIAL = (
    RESEARCH / "Temtamy_Preaxial_Brachydactyly_Syndrome-deep-research-falcon.md"
)

# The fixtures are the *real* DR reports that produced the documented NEC
# incidents, which is the point -- but two of them are wrong-entity reports and
# are plausible candidates for future cleanup of research/. Skip loudly rather
# than dying with a bare FileNotFoundError if that happens.
requires_reports = pytest.mark.skipif(
    not (
        LICHTENSTEIN_KNORR.exists()
        and TEMTAMY.exists()
        and TEMTAMY_PREAXIAL.exists()
    ),
    reason="NEC incident reports are no longer present under research/",
)

# MONDO records as returned by the live adapter, frozen here for offline tests.
REC_LIKNS = MondoRecord(
    id="MONDO:0014572",
    label="Lichtenstein-Knorr syndrome",
    genes=("SLC9A1",),
    omim_ids=("616291",),
)
REC_TEMTAMY = MondoRecord(
    id="MONDO:0009033",
    label="temtamy syndrome",
    genes=("C12orf57",),
    omim_ids=("218340",),
)
REC_TEMTAMY_PREAXIAL = MondoRecord(
    id="MONDO:0011533",
    label="temtamy preaxial brachydactyly syndrome",
    genes=("CHSY1",),
    omim_ids=("605282",),
)
REC_NO_GENE = MondoRecord(
    id="MONDO:0005148",
    label="type 2 diabetes mellitus",
    genes=(),
    omim_ids=("125853",),
)


class FakeLexicon:
    """Accepts only an explicit symbol set, keeping tests HGNC-independent."""

    name = "fake"

    def __init__(self, symbols):
        self.symbols = set(symbols)

    def __contains__(self, symbol):
        return symbol in self.symbols


CASE_GENES = FakeLexicon({"SLC9A1", "SNX14", "C12orf57", "CHSY1", "JAG1", "AR", "HP", "CS"})


def _stub_adapter(monkeypatch, record):
    monkeypatch.setattr(
        "dismech.preflight_dr.fetch_mondo_record",
        lambda mondo_id, adapter=None, **kwargs: record,
    )
    # ``main`` opens MONDO before anything else; the record above stands in for
    # what that adapter would have returned.
    monkeypatch.setattr("dismech.preflight_dr.open_mondo_adapter", lambda: object())
    # The rival-gene disease lookup would otherwise open the real MONDO build.
    monkeypatch.setattr(
        "dismech.preflight_dr._default_rival_lookup",
        lambda adapter, use_hgnc: (lambda symbols, exclude: ({}, [])),
    )


# --------------------------------------------------------------------------
# Text extraction
# --------------------------------------------------------------------------


def test_strip_curies_removes_ontology_ids_but_keeps_gene_symbols():
    text = "HP:0001250 seizure in SLC9A1; see PMID:26350204 and MONDO:0014572."
    stripped = strip_curies(text)
    assert "SLC9A1" in stripped
    assert "HP:0001250" not in stripped
    assert "PMID:26350204" not in stripped


def test_hpo_curies_do_not_inflate_the_haptoglobin_gene_symbol():
    """HP is a real HGNC symbol; HPO CURIEs must not be counted as gene mentions."""
    text = "HP:0001250 HP:0002376 HP:0000750 with one true SNX14 mention."
    counts = extract_gene_mentions(text, FakeLexicon({"HP", "SNX14"}))
    assert counts["HP"] == 0
    assert counts["SNX14"] == 1


def test_extract_gene_mentions_matches_c_orf_symbols():
    counts = extract_gene_mentions(
        "C12orf57 is mutated; C12orf57 again.", FakeLexicon({"C12orf57"})
    )
    assert counts["C12orf57"] == 2


def test_extract_omim_ids_handles_common_prose_forms():
    text = "OMIM:616291 and MIM #605282 and (OMIM 218340)"
    assert extract_omim_ids(text) == {"616291", "605282", "218340"}


def test_heuristic_lexicon_rejects_common_non_gene_acronyms():
    lex = HeuristicLexicon()
    assert "DNA" not in lex
    assert "MRI" not in lex
    assert "SLC9A1" in lex


# --------------------------------------------------------------------------
# Verdict logic -- the four cases from issue #3889
# --------------------------------------------------------------------------


@requires_reports
def test_case1_pass_report_matches_mondo_canonical_gene():
    """Case 1: the report's dominant gene IS the MONDO canonical gene."""
    text = TEMTAMY_PREAXIAL.read_text(encoding="utf-8")
    result = assess(
        REC_TEMTAMY_PREAXIAL,
        extract_gene_mentions(text, CASE_GENES),
        extract_omim_ids(text),
    )
    assert result.verdict == PASS
    assert result.ok
    assert result.expected_mentions["CHSY1"] > 0


@requires_reports
def test_case2_fail_lichtenstein_knorr_report_is_about_snx14():
    """Case 2: MONDO:0014572 is SLC9A1, but the DR report is entirely about SNX14."""
    text = LICHTENSTEIN_KNORR.read_text(encoding="utf-8")
    counts = extract_gene_mentions(text, CASE_GENES)
    result = assess(REC_LIKNS, counts, extract_omim_ids(text))

    assert result.verdict == FAIL
    assert not result.ok
    assert result.expected_mentions["SLC9A1"] == 0
    # The wrong-entity gene dominates -- the signature documented in #3889.
    assert counts["SNX14"] >= 40
    assert result.rival_genes[0][0] == "SNX14"
    assert "different disease entity" in " ".join(result.reasons)


@requires_reports
def test_case2_report_also_cites_the_wrong_entity_omim():
    """The SCAR20 report cites OMIM:616354, not Lichtenstein-Knorr's OMIM:616291."""
    report_omim = extract_omim_ids(LICHTENSTEIN_KNORR.read_text(encoding="utf-8"))
    assert "616354" in report_omim
    assert "616291" not in report_omim


@requires_reports
def test_case3_warn_temtamy_report_mixes_a_second_eponymous_entity():
    """Case 3: C12orf57 dominates but CHSY1 (a different Temtamy disease) contaminates."""
    text = TEMTAMY.read_text(encoding="utf-8")
    counts = extract_gene_mentions(text, CASE_GENES)
    result = assess(REC_TEMTAMY, counts, extract_omim_ids(text))

    assert result.verdict == WARN
    assert counts["C12orf57"] > counts["CHSY1"] > 0
    assert result.rival_genes[0][0] == "CHSY1"
    assert "mix in a second disease entity" in " ".join(result.reasons)


def test_case4_skip_when_mondo_records_no_causal_gene():
    """Case 4: complex/multifactorial entities have no RO:0004003 edge to check."""
    result = assess(REC_NO_GENE, Counter({"TCF7L2": 12}))
    assert result.verdict == SKIP
    assert result.ok
    assert "no causal gene" in " ".join(result.reasons)


# --------------------------------------------------------------------------
# Threshold behaviour
# --------------------------------------------------------------------------


def test_rival_below_min_signal_does_not_trigger_a_warning():
    counts = Counter({"CHSY1": 30, "JAG1": 2})
    result = assess(REC_TEMTAMY_PREAXIAL, counts, min_signal=3)
    assert result.verdict == PASS


def test_rival_below_ratio_does_not_trigger_a_warning():
    counts = Counter({"CHSY1": 100, "JAG1": 10})
    result = assess(REC_TEMTAMY_PREAXIAL, counts, rival_ratio=0.25)
    assert result.verdict == PASS


def test_rival_at_or_above_ratio_triggers_a_warning():
    counts = Counter({"CHSY1": 100, "JAG1": 25})
    result = assess(REC_TEMTAMY_PREAXIAL, counts, rival_ratio=0.25)
    assert result.verdict == WARN


# KDM1A-related adrenal hyperplasia (#9826): GIP is the disease's own effector
# (KDM1A loss derepresses GIPR), yet at 21/48 = 0.44 it clears the ratio by
# more than the Temtamy rival (0.40) the threshold was tuned on.
REC_AIMAH3 = MondoRecord(
    id="MONDO:0700299",
    label="ACTH-independent macronodular adrenal hyperplasia 3",
    genes=("KDM1A",),
)


def test_effector_gene_warning_does_not_tell_the_curator_to_exclude_sections():
    counts = Counter({"KDM1A": 48, "GIP": 21, "GIPR": 21, "ARMC5": 10, "GNAS": 2})
    result = assess(REC_AIMAH3, counts)

    assert result.verdict == WARN
    assert result.rival_genes[0] == ("GIP", 21)
    reason = next(r for r in result.reasons if "GIP" in r)
    assert "44% of KDM1A" in reason
    assert "modifier gene" in reason
    assert "exclude them only if they are about a different disease" in reason
    assert "exclude those sections before curating" not in reason


def test_bare_ontology_prefixes_in_prose_are_not_rival_genes():
    """ "HP calls it ..." survives CURIE stripping but is the ontology, not haptoglobin."""
    text = "ACO2 " * 46 + 'The report calls it "Physical"; HP calls it Optic atrophy. ' * 14
    counts = extract_gene_mentions(text, FakeLexicon({"ACO2", "HP"}))
    assert counts["HP"] == 14
    record = MondoRecord(id="MONDO:0013802", label="ICRD", genes=("ACO2",))

    result = assess(record, counts)

    assert result.verdict == PASS
    assert all(sym != "HP" for sym, _ in result.rival_genes)


def test_an_ontology_prefix_alone_cannot_manufacture_a_fail():
    record = MondoRecord(id="MONDO:0014572", label="LIKNS", genes=("SLC9A1",))
    result = assess(record, Counter({"HP": 40}))
    assert result.verdict != FAIL


def test_a_prefix_symbol_that_is_the_expected_gene_is_still_counted():
    """HP (haptoglobin) is excluded from the rival pool, never from the expected gene."""
    record = MondoRecord(id="MONDO:0000001", label="hypohaptoglobinemia", genes=("HP",))
    result = assess(record, Counter({"HP": 12}))
    assert result.verdict == PASS
    assert result.expected_mentions == {"HP": 12}


def test_no_gene_mentions_at_all_warns_rather_than_fails():
    """An absent expected gene with no rival is unverifiable, not proven wrong."""
    result = assess(REC_LIKNS, Counter())
    assert result.verdict == WARN
    assert "could not be confirmed" in " ".join(result.reasons)


def test_omim_disagreement_downgrades_a_pass_to_warn():
    result = assess(REC_LIKNS, Counter({"SLC9A1": 20}), {"616354"})
    assert result.verdict == WARN
    assert "616354" in " ".join(result.reasons)


def test_matching_omim_leaves_the_pass_intact():
    result = assess(REC_LIKNS, Counter({"SLC9A1": 20}), {"616291"})
    assert result.verdict == PASS


# --------------------------------------------------------------------------
# End-to-end / CLI
# --------------------------------------------------------------------------


@requires_reports
def test_preflight_end_to_end_flags_the_known_nec_report(monkeypatch):
    _stub_adapter(monkeypatch, REC_LIKNS)
    result = preflight(LICHTENSTEIN_KNORR, "MONDO:0014572", lexicon=CASE_GENES)
    assert result.verdict == FAIL
    assert result.report.endswith("Lichtenstein-Knorr_Syndrome-deep-research-falcon.md")


def test_format_report_names_the_verdict_and_the_expected_gene():
    result = assess(REC_LIKNS, Counter({"SNX14": 43}))
    rendered = format_report(result)
    assert rendered.startswith("FAIL")
    assert "SLC9A1" in rendered
    assert "SNX14" in rendered


@requires_reports
def test_cli_exits_nonzero_on_fail(monkeypatch, capsys):
    _stub_adapter(monkeypatch, REC_LIKNS)
    monkeypatch.setattr(
        "dismech.preflight_dr.default_lexicon", lambda **kw: CASE_GENES
    )
    code = main([str(LICHTENSTEIN_KNORR), "MONDO:0014572"])
    assert code == 1
    assert "FAIL" in capsys.readouterr().out


@requires_reports
def test_cli_warn_is_tolerated_unless_strict(monkeypatch):
    _stub_adapter(monkeypatch, REC_TEMTAMY)
    monkeypatch.setattr(
        "dismech.preflight_dr.default_lexicon", lambda **kw: CASE_GENES
    )
    assert main([str(TEMTAMY), "MONDO:0009033"]) == 0
    assert main([str(TEMTAMY), "MONDO:0009033", "--strict"]) == 1


@requires_reports
def test_cli_emits_json(monkeypatch, capsys):
    import json

    _stub_adapter(monkeypatch, REC_LIKNS)
    monkeypatch.setattr(
        "dismech.preflight_dr.default_lexicon", lambda **kw: CASE_GENES
    )
    main([str(LICHTENSTEIN_KNORR), "MONDO:0014572", "--json"])
    payload = json.loads(capsys.readouterr().out)
    assert payload["verdict"] == FAIL
    assert payload["expected_genes"] == ["SLC9A1"]


@requires_reports
def test_cli_rejects_a_non_mondo_identifier(monkeypatch):
    _stub_adapter(monkeypatch, REC_LIKNS)
    with pytest.raises(SystemExit):
        main([str(LICHTENSTEIN_KNORR), "OMIM:616291"])


# --------------------------------------------------------------------------
# Degraded paths -- a safety gate must not fail towards "looks clean"
# --------------------------------------------------------------------------


class DeadAdapter:
    """An OAK adapter whose every call raises, as a missing db or drift would."""

    def __init__(self, message="adapter is not available"):
        self.message = message

    def _boom(self, *_args, **_kwargs):
        raise RuntimeError(self.message)

    label = definition = relationships = _boom
    curies_by_label = simple_mappings_by_curie = entity_aliases = _boom


class StubMondoAdapter:
    """Minimal MONDO adapter: RO:0004003 edges with configurable labels.

    ``relationships`` filters the way oaklib's does, so the same stub answers
    the forward lookup (disease -> gene) and the reverse one (gene -> disease).
    """

    def __init__(self, labels, relationships, mappings=()):
        self._labels = labels
        self._relationships = relationships
        self._mappings = mappings

    def label(self, curie):
        return self._labels.get(curie)

    def curies_by_label(self, label):
        return [curie for curie, value in self._labels.items() if value == label]

    def relationships(self, subjects=None, predicates=None, objects=None):
        return [
            (s, p, o)
            for s, p, o in self._relationships
            if (subjects is None or s in subjects)
            and (predicates is None or p in predicates)
            and (objects is None or o in objects)
        ]

    def simple_mappings_by_curie(self, curie):
        return list(self._mappings)


def test_dead_hgnc_adapter_raises_rather_than_rejecting_every_symbol():
    """A silent lexicon failure would empty gene counts and turn FAIL into WARN."""
    lexicon = HgncLexicon(adapter=DeadAdapter())
    with pytest.raises(LexiconUnavailable):
        lexicon.probe()
    with pytest.raises(LexiconUnavailable):
        "SLC9A1" in lexicon  # noqa: B015 - exercising __contains__


def test_default_lexicon_falls_back_to_a_labelled_heuristic(monkeypatch):
    monkeypatch.setattr(
        "dismech.preflight_dr.HgncLexicon", lambda: HgncLexicon(adapter=DeadAdapter())
    )
    lexicon = default_lexicon()
    assert isinstance(lexicon, HeuristicLexicon)
    assert lexicon.name == "heuristic"
    assert "adapter is not available" in lexicon.reason


def test_default_lexicon_can_hard_error_instead_of_degrading(monkeypatch):
    monkeypatch.setattr(
        "dismech.preflight_dr.HgncLexicon", lambda: HgncLexicon(adapter=DeadAdapter())
    )
    with pytest.raises(LexiconUnavailable):
        default_lexicon(allow_fallback=False)


@requires_reports
def test_a_dead_lexicon_still_produces_the_fail_verdict(monkeypatch):
    """The regression the reviewer flagged: FAIL must not degrade to WARN."""
    monkeypatch.setattr(
        "dismech.preflight_dr.HgncLexicon", lambda: HgncLexicon(adapter=DeadAdapter())
    )
    _stub_adapter(monkeypatch, REC_LIKNS)
    result = preflight(LICHTENSTEIN_KNORR, "MONDO:0014572")
    assert result.verdict == FAIL
    assert result.lexicon == "heuristic"
    assert "HGNC unavailable" in format_report(result)


def test_a_failed_gene_lookup_is_reported_as_a_failure_not_as_no_gene():
    record = fetch_mondo_record("MONDO:0014572", adapter=DeadAdapter(), hgnc_adapter=None)
    assert record.genes == ()
    assert record.lookup_errors
    result = assess(record, Counter({"SNX14": 43}))
    assert result.verdict == WARN
    joined = " ".join(result.reasons)
    assert "did not complete" in joined
    assert "no causal gene" not in joined


def test_an_unresolved_gene_curie_warns_instead_of_manufacturing_a_fail():
    """`adapter.label()` returning nothing must not condemn a correct report."""
    adapter = StubMondoAdapter(
        labels={"MONDO:0014572": "Lichtenstein-Knorr syndrome"},
        relationships=[("MONDO:0014572", "RO:0004003", "HGNC:11071")],
    )
    record = fetch_mondo_record("MONDO:0014572", adapter=adapter, hgnc_adapter=DeadAdapter())
    assert record.genes == ("HGNC:11071",)
    assert record.unresolved_genes == ("HGNC:11071",)

    result = assess(record, Counter({"SNX14": 43}))
    assert result.verdict == WARN
    assert "Could not resolve" in " ".join(result.reasons)


def test_hgnc_repairs_a_gene_label_mondo_does_not_carry():
    adapter = StubMondoAdapter(
        labels={"MONDO:0014572": "Lichtenstein-Knorr syndrome"},
        relationships=[("MONDO:0014572", "RO:0004003", "HGNC:11071")],
    )

    class Hgnc:
        def label(self, curie):
            return "SLC9A1" if curie == "HGNC:11071" else None

        def entity_aliases(self, curie):
            return ["NHE1", "sodium/hydrogen exchanger 1", "APNH"]

    record = fetch_mondo_record("MONDO:0014572", adapter=adapter, hgnc_adapter=Hgnc())
    assert record.genes == ("SLC9A1",)
    assert record.unresolved_genes == ()
    # Free-text names are dropped; only symbol-shaped aliases survive.
    assert record.gene_aliases["SLC9A1"] == ("NHE1", "APNH")


def test_alias_mentions_count_towards_the_canonical_gene():
    """A report that writes NHE1 throughout is still about SLC9A1."""
    record = MondoRecord(
        id="MONDO:0014572",
        label="Lichtenstein-Knorr syndrome",
        genes=("SLC9A1",),
        gene_aliases={"SLC9A1": ("NHE1",)},
    )
    result = assess(record, Counter({"NHE1": 30, "SNX14": 4}))
    assert result.verdict == PASS
    assert result.alias_mentions == {"NHE1": 30}
    assert result.expected_mentions["SLC9A1"] == 30


def test_a_single_incidental_mention_is_not_a_clean_bill_of_health():
    """One mention in a citation title must not read as PASS."""
    result = assess(REC_LIKNS, Counter({"SLC9A1": 1}), min_signal=3)
    assert result.verdict == WARN
    assert "below the 3-mention threshold" in " ".join(result.reasons)


def test_at_the_min_signal_threshold_a_clean_report_still_passes():
    result = assess(REC_LIKNS, Counter({"SLC9A1": 3}), min_signal=3)
    assert result.verdict == PASS


def test_a_failed_omim_lookup_caps_the_verdict_at_warn():
    record = MondoRecord(
        id="MONDO:0014572",
        label="Lichtenstein-Knorr syndrome",
        genes=("SLC9A1",),
        lookup_errors=("OMIM xref lookup for MONDO:0014572 failed: boom",),
    )
    result = assess(record, Counter({"SLC9A1": 40}))
    assert result.verdict == WARN
    assert "Some ontology lookups failed" in " ".join(result.reasons)
    assert "lookup failed" in format_report(result)


# --------------------------------------------------------------------------
# FAIL is the most destructive verdict, so nothing may contradict it
# --------------------------------------------------------------------------


def test_a_failed_alias_lookup_does_not_manufacture_a_fail():
    """The alias rescue is what makes an alias-written report survive.

    When that lookup is the one that failed, the absence of the canonical
    symbol says nothing — telling the curator to discard a correct report is
    the worst outcome this tool can produce.
    """
    record = MondoRecord(
        id="MONDO:0014572",
        label="Lichtenstein-Knorr syndrome",
        genes=("SLC9A1",),
        omim_ids=("616291",),
        lookup_errors=("alias lookup for HGNC:11071 failed: hgnc down",),
    )
    result = assess(record, Counter({"NHE1": 41}), {"616291"})
    assert result.verdict == WARN
    joined = " ".join(result.reasons)
    assert "not conclusive" in joined
    assert "discard it rather than cherry-picking" not in joined
    assert "Some ontology lookups failed" in joined


def test_a_matching_omim_keeps_warn_when_no_rival_causes_another_disease():
    """A report written in a protein name the alias list lacks must not be binned.

    NHE1 is not an HGNC alias of SLC9A1, so the canonical symbol is never
    counted. With no rival gene resolving to a disease of its own, the matching
    OMIM number is the only identity evidence, and it keeps the verdict at WARN.
    """
    record = MondoRecord(
        id="MONDO:0014572",
        label="Lichtenstein-Knorr syndrome",
        genes=("SLC9A1",),
        omim_ids=("616291",),
    )
    result = assess(
        record,
        Counter({"NHE1": 41}),
        {"616291"},
        rival_disease_lookup=lambda symbols, exclude: ({}, []),
    )
    assert result.verdict == WARN
    joined = " ".join(result.reasons)
    assert "616291" in joined
    assert "pointed at the right entry" in joined
    assert "None of the rival genes checked (NHE1)" in joined
    assert "under any name" in joined
    # The old wording read as permission to keep the report.
    assert "reconcile" not in joined
    assert result.rival_diseases == {}


def test_without_a_rival_lookup_a_matching_omim_still_only_warns():
    """No lookup means no determination, so nothing can escalate to FAIL."""
    record = MondoRecord(
        id="MONDO:0014572",
        label="Lichtenstein-Knorr syndrome",
        genes=("SLC9A1",),
        omim_ids=("616291",),
    )
    result = assess(record, Counter({"NHE1": 41}), {"616291"})
    assert result.verdict == WARN
    assert "were not checked" in " ".join(result.reasons)


@requires_reports
def test_the_lichtenstein_knorr_fixture_still_fails_despite_the_new_rescues():
    """Neither rescue applies to the real NEC report: it cites 616354, not 616291."""
    counts = extract_gene_mentions(LICHTENSTEIN_KNORR.read_text(), CASE_GENES)
    omim = extract_omim_ids(LICHTENSTEIN_KNORR.read_text())
    assert "616291" not in omim
    result = assess(REC_LIKNS, counts, omim)
    assert result.verdict == FAIL


def test_a_mismatched_omim_leaves_the_fail_intact():
    result = assess(REC_LIKNS, Counter({"SNX14": 43}), {"616354"})
    assert result.verdict == FAIL
    assert "discard it rather than cherry-picking" in " ".join(result.reasons)


# --------------------------------------------------------------------------
# Alias handling
# --------------------------------------------------------------------------


class StubHgnc:
    """HGNC adapter stub keyed on a single canonical CURIE casing."""

    def __init__(self, curie="HGNC:11071", symbol="SLC9A1", aliases=(), approved=None):
        self._curie = curie
        self._symbol = symbol
        self._aliases = list(aliases)
        #: label -> CURIE, i.e. which gene each symbol is the *approved* symbol of
        self._approved = dict(approved or {symbol: curie})

    def label(self, curie):
        return self._symbol if curie == self._curie else None

    def entity_aliases(self, curie):
        return list(self._aliases) if curie == self._curie else []

    def curies_by_label(self, label):
        curie = self._approved.get(label)
        return [curie] if curie else []


def test_alias_lookup_survives_a_curie_prefix_case_mismatch():
    """MONDO emits `HGNC:`, this repo's canonical form is lowercase `hgnc:`."""
    adapter = StubMondoAdapter(
        labels={"MONDO:0014572": "Lichtenstein-Knorr syndrome"},
        relationships=[("MONDO:0014572", "RO:0004003", "HGNC:11071")],
    )
    hgnc = StubHgnc(curie="hgnc:11071", aliases=["NHE1", "APNH"])
    record = fetch_mondo_record("MONDO:0014572", adapter=adapter, hgnc_adapter=hgnc)
    assert record.genes == ("SLC9A1",)
    assert record.gene_aliases["SLC9A1"] == ("NHE1", "APNH")


def test_an_alias_that_is_another_genes_approved_symbol_is_dropped():
    """Otherwise a genuine rival is double-discounted, biasing towards PASS."""
    adapter = StubMondoAdapter(
        labels={
            "MONDO:0014572": "Lichtenstein-Knorr syndrome",
            "HGNC:11071": "SLC9A1",
        },
        relationships=[("MONDO:0014572", "RO:0004003", "HGNC:11071")],
    )
    hgnc = StubHgnc(
        aliases=["NHE1", "SNX14"],
        approved={"SLC9A1": "HGNC:11071", "SNX14": "HGNC:14977"},
    )
    record = fetch_mondo_record("MONDO:0014572", adapter=adapter, hgnc_adapter=hgnc)
    assert record.gene_aliases["SLC9A1"] == ("NHE1",)
    # SNX14 is therefore still counted as a rival rather than credited to SLC9A1.
    result = assess(record, Counter({"SNX14": 43}))
    assert result.verdict == FAIL


def test_no_hgnc_mode_never_opens_the_hgnc_adapter(monkeypatch):
    """`--no-hgnc` documents itself as offline; make it actually be offline."""
    def _explode(*_args, **_kwargs):  # pragma: no cover - must never run
        raise AssertionError("HGNC adapter was opened in --no-hgnc mode")

    monkeypatch.setattr("oaklib.get_adapter", _explode)
    adapter = StubMondoAdapter(
        labels={
            "MONDO:0014572": "Lichtenstein-Knorr syndrome",
            "HGNC:11071": "SLC9A1",
        },
        relationships=[("MONDO:0014572", "RO:0004003", "HGNC:11071")],
    )
    record = fetch_mondo_record("MONDO:0014572", adapter=adapter, use_hgnc=False)
    assert record.genes == ("SLC9A1",)
    assert record.lookup_errors == ()


def _no_local_builds(monkeypatch, tmp_path):
    """Point OAK's build directory at an empty dir, and make opening fatal.

    Opening ``sqlite:obo:*`` on a missing build downloads it rather than
    failing, so the test must prove the adapter is never opened at all.
    """
    monkeypatch.setenv("PYSTOW_HOME", str(tmp_path))

    def _explode(spec, *_args, **_kwargs):  # pragma: no cover - must never run
        raise AssertionError(f"{spec} was opened; it would have been downloaded")

    monkeypatch.setattr("oaklib.get_adapter", _explode)


def test_fetch_mondo_record_refuses_to_download_a_missing_mondo_build(
    monkeypatch, tmp_path
):
    """#12687: no local ``mondo.db`` is a hard error, never a lazy download.

    Nor an empty record: that would read as "MONDO records no causal gene"
    and come out as a SKIP verdict.
    """
    _no_local_builds(monkeypatch, tmp_path)
    with pytest.raises(MondoBuildUnavailable, match="just fetch-ontology-dbs mondo"):
        fetch_mondo_record("MONDO:0014572", use_hgnc=False)


def test_cli_exits_2_without_the_mondo_build_before_opening_hgnc(
    monkeypatch, tmp_path, capsys
):
    """The CLI fails fast, and before the HGNC lexicon can fetch its own build."""
    _no_local_builds(monkeypatch, tmp_path)

    def _no_lexicon(**_kwargs):  # pragma: no cover - must never run
        raise AssertionError("HGNC lexicon was built for a run that cannot finish")

    monkeypatch.setattr("dismech.preflight_dr.default_lexicon", _no_lexicon)
    report = tmp_path / "report.md"
    report.write_text("SLC9A1 SLC9A1 SLC9A1\n", encoding="utf-8")
    with pytest.raises(SystemExit) as excinfo:
        main([str(report), "MONDO:0014572"])
    assert excinfo.value.code == 2
    err = capsys.readouterr().err
    assert "just fetch-ontology-dbs mondo" in err
    assert str(tmp_path / "oaklib" / "mondo.db") in err


def test_cli_opens_mondo_when_the_build_is_present(monkeypatch, tmp_path, capsys):
    """With ``mondo.db`` on disk the guard lets the adapter through."""
    monkeypatch.setenv("PYSTOW_HOME", str(tmp_path))
    (tmp_path / "oaklib").mkdir()
    (tmp_path / "oaklib" / "mondo.db").write_bytes(b"")
    adapter = StubMondoAdapter(
        labels={
            "MONDO:0014572": "Lichtenstein-Knorr syndrome",
            "HGNC:11071": "SLC9A1",
        },
        relationships=[("MONDO:0014572", "RO:0004003", "HGNC:11071")],
    )
    opened = []

    def _get_adapter(spec, *_args, **_kwargs):
        opened.append(spec)
        return adapter

    monkeypatch.setattr("oaklib.get_adapter", _get_adapter)
    report = tmp_path / "report.md"
    report.write_text("SLC9A1 " * 5 + "\n", encoding="utf-8")
    assert main([str(report), "MONDO:0014572", "--no-hgnc"]) == 0
    assert opened == ["sqlite:obo:mondo"]
    assert capsys.readouterr().out.startswith("PASS")


# --------------------------------------------------------------------------
# #12166: the right OMIM number does not make a report about the right gene
# --------------------------------------------------------------------------

# MONDO:0030717 as the live adapter returns it.
REC_IMD97 = MondoRecord(
    id="MONDO:0030717",
    label="immunodeficiency 97 with autoinflammation",
    genes=("PIK3CG",),
    omim_ids=("619802",),
)

# Gene counts and OMIM citations of the openscientist report filed as #12166.
# The report itself was replaced by a re-run before it was committed.
IMD97_TBK1_COUNTS = Counter({"TNF": 58, "TBK1": 47, "RIPK1": 27, "TANK": 6, "RIPK3": 4})
IMD97_TBK1_OMIM = {"604834", "619802"}

# The reverse RO:0004003 edges the live sqlite:obo:mondo adapter holds for
# these genes. TNF, the report's most-mentioned gene, causes no MONDO disease.
IMD97_MONDO = StubMondoAdapter(
    labels={
        "MONDO:0030717": "immunodeficiency 97 with autoinflammation",
        "MONDO:0971173": "autoinflammation with arthritis and vasculitis",
        "MONDO:0014641": "frontotemporal dementia and/or amyotrophic lateral sclerosis 4",
        "HGNC:8978": "PIK3CG",
        "HGNC:11584": "TBK1",
        "HGNC:11892": "TNF",
    },
    relationships=[
        ("MONDO:0030717", "RO:0004003", "HGNC:8978"),
        ("MONDO:0971173", "RO:0004003", "HGNC:11584"),
        ("MONDO:0014641", "RO:0004003", "HGNC:11584"),
    ],
)


def _imd97_lookup(symbols, exclude):
    return find_rival_diseases(symbols, exclude, IMD97_MONDO)


def test_a_rival_gene_with_its_own_disease_fails_despite_a_matching_omim():
    """The #12166 case: PIK3CG=0, TBK1=47, OMIM 619802 cited. That is a FAIL."""
    result = assess(
        REC_IMD97,
        IMD97_TBK1_COUNTS,
        IMD97_TBK1_OMIM,
        rival_disease_lookup=_imd97_lookup,
    )
    assert result.verdict == FAIL
    assert result.expected_absent
    assert "TBK1" in result.rival_diseases
    assert ("MONDO:0971173", "autoinflammation with arthritis and vasculitis") in (
        result.rival_diseases["TBK1"]
    )
    joined = " ".join(result.reasons)
    assert "zero mentions, not a low count" in joined
    assert "discard it rather than cherry-picking" in joined
    # The OMIM match is still reported, as context that does not soften the FAIL.
    assert "619802" in joined
    assert "does not soften this verdict" in joined


def test_the_rival_lookup_goes_past_the_most_mentioned_rival():
    """TNF out-ranks TBK1 in the #12166 report and causes no MONDO disease."""
    seen = []

    def _lookup(symbols, exclude):
        seen.extend(symbols)
        return _imd97_lookup(symbols, exclude)

    result = assess(
        REC_IMD97, IMD97_TBK1_COUNTS, IMD97_TBK1_OMIM, rival_disease_lookup=_lookup
    )
    assert seen[:2] == ["TNF", "TBK1"]
    assert "TNF" not in result.rival_diseases
    assert result.verdict == FAIL


def test_a_failed_rival_lookup_never_manufactures_a_fail():
    """Could-not-check leaves the OMIM-matching case at WARN, and says so."""

    def _broken(symbols, exclude):
        raise RuntimeError("mondo.db unreadable")

    result = assess(
        REC_IMD97, IMD97_TBK1_COUNTS, IMD97_TBK1_OMIM, rival_disease_lookup=_broken
    )
    assert result.verdict == WARN
    joined = " ".join(result.reasons)
    assert "did not complete" in joined
    assert any("mondo.db unreadable" in e for e in result.lookup_errors)


def test_the_rival_lookup_only_runs_when_the_canonical_gene_is_absent():
    """A clean run must not pay for, or depend on, the reverse lookup."""

    def _explode(symbols, exclude):  # pragma: no cover - must never run
        raise AssertionError("rival lookup ran on a report naming its gene")

    for counts in (Counter({"PIK3CG": 30, "TBK1": 4}), Counter({"PIK3CG": 1, "TBK1": 47})):
        result = assess(REC_IMD97, counts, {"619802"}, rival_disease_lookup=_explode)
        assert result.verdict in (PASS, WARN)
        assert not result.expected_absent


def test_an_abbreviation_that_is_also_a_gene_symbol_cannot_decide_a_fail():
    """AR is an HGNC symbol, and the cause of Kennedy disease.

    A report on the right disease that writes "AR" for autosomal recessive,
    names its gene only by protein name, and cites the right OMIM number must
    stay at WARN rather than be binned as a Kennedy disease report.
    """
    asked = []

    def _lookup(symbols, exclude):
        asked.extend(symbols)
        return {"AR": [("MONDO:0010735", "Kennedy disease")]}, []

    record = MondoRecord(
        id="MONDO:0014572",
        label="Lichtenstein-Knorr syndrome",
        genes=("SLC9A1",),
        omim_ids=("616291",),
    )
    result = assess(
        record, Counter({"AR": 12, "HR": 4}), {"616291"}, rival_disease_lookup=_lookup
    )
    assert asked == []
    assert result.verdict == WARN
    assert result.rival_diseases == {}
    assert "common abbreviation" in " ".join(result.reasons)


def test_an_abbreviation_is_skipped_but_a_real_rival_gene_still_decides():
    """The #12166-shaped DC report: TYMS/ENOSF1 decide, AR and HR are skipped."""
    asked = []

    def _lookup(symbols, exclude):
        asked.extend(symbols)
        return {"TYMS": [("MONDO:0031057", "dyskeratosis congenita, digenic")]}, []

    record = MondoRecord(
        id="MONDO:0859319",
        label="dyskeratosis congenita, autosomal recessive 8",
        genes=("DCLRE1B",),
        omim_ids=("620133",),
    )
    counts = Counter({"TYMS": 70, "ENOSF1": 41, "AR": 6, "BMF": 5, "HR": 4})
    result = assess(record, counts, {"620133"}, rival_disease_lookup=_lookup)
    assert "AR" not in asked and "HR" not in asked
    assert asked[:2] == ["TYMS", "ENOSF1"]
    assert result.verdict == FAIL


def test_the_default_rival_lookup_never_downloads_a_build(monkeypatch, tmp_path):
    """No local HGNC build: the fallback is skipped, not fetched (#12687)."""
    _no_local_builds(monkeypatch, tmp_path)
    lookup = P._default_rival_lookup(IMD97_MONDO, use_hgnc=True)
    found, errors = lookup(["TBK1"], "MONDO:0030717")
    assert errors == []
    assert "TBK1" in found


def test_the_default_rival_lookup_refuses_a_missing_mondo_build(monkeypatch, tmp_path):
    """With no adapter passed it goes through open_mondo_adapter's guard."""
    _no_local_builds(monkeypatch, tmp_path)
    lookup = P._default_rival_lookup(None, use_hgnc=False)
    with pytest.raises(MondoBuildUnavailable):
        lookup(["TBK1"], "MONDO:0030717")


def test_find_rival_diseases_excludes_the_intended_entity():
    """PIK3CG causes MONDO:0030717 itself; that is not a *rival* disease."""
    found, errors = find_rival_diseases(["PIK3CG", "TBK1", "TNF"], "MONDO:0030717", IMD97_MONDO)
    assert errors == []
    assert set(found) == {"TBK1"}
    assert [mid for mid, _label in found["TBK1"]] == ["MONDO:0014641", "MONDO:0971173"]


def test_find_rival_diseases_falls_back_to_hgnc_for_the_identifier():
    """A gene MONDO does not label is looked up in HGNC before being given up on."""
    mondo = StubMondoAdapter(
        labels={"MONDO:0971173": "autoinflammation with arthritis and vasculitis"},
        relationships=[("MONDO:0971173", "RO:0004003", "HGNC:11584")],
    )
    hgnc = StubHgnc(curie="hgnc:11584", symbol="TBK1", approved={"TBK1": "hgnc:11584"})
    found, errors = find_rival_diseases(["TBK1"], "MONDO:0030717", mondo, hgnc)
    assert errors == []
    assert found == {"TBK1": [("MONDO:0971173", "autoinflammation with arthritis and vasculitis")]}


def test_find_rival_diseases_records_a_failed_lookup_instead_of_an_empty_answer():
    class _Dead(StubMondoAdapter):
        def relationships(self, subjects=None, predicates=None, objects=None):
            raise RuntimeError("boom")

    dead = _Dead(labels={"HGNC:11584": "TBK1"}, relationships=[])
    found, errors = find_rival_diseases(["TBK1"], "MONDO:0030717", dead)
    assert found == {}
    assert len(errors) == 1 and "TBK1" in errors[0] and "boom" in errors[0]


def test_format_report_marks_zero_mentions_and_names_the_rival_disease():
    result = assess(
        REC_IMD97, IMD97_TBK1_COUNTS, IMD97_TBK1_OMIM, rival_disease_lookup=_imd97_lookup
    )
    text = format_report(result)
    assert "PIK3CG=0 (never named)" in text
    assert "rival disease   : TBK1 -> MONDO:0971173 autoinflammation with arthritis" in text


def test_a_low_count_is_not_reported_as_never_named():
    result = assess(REC_IMD97, Counter({"PIK3CG": 2, "TBK1": 1}))
    assert not result.expected_absent
    assert "never named" not in format_report(result)
    assert "mentioned only 2 time(s)" in " ".join(result.reasons)


def test_cli_fails_the_12166_report_shape(monkeypatch, tmp_path, capsys):
    """End to end through ``main``: the reverse lookup reaches the verdict."""
    monkeypatch.setattr(
        "dismech.preflight_dr.fetch_mondo_record",
        lambda mondo_id, adapter=None, **kwargs: REC_IMD97,
    )
    monkeypatch.setattr(
        "dismech.preflight_dr._default_rival_lookup",
        lambda adapter, use_hgnc: _imd97_lookup,
    )
    # ``main`` opens MONDO first; without this the test needs a local mondo.db.
    monkeypatch.setattr("dismech.preflight_dr.open_mondo_adapter", lambda: object())
    report = tmp_path / "report.md"
    lines = ["OMIM 619802 and OMIM 604834."]
    for gene, n in IMD97_TBK1_COUNTS.items():
        lines += [f"{gene} is discussed."] * n
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    exit_code = main(
        [str(report), "MONDO:0030717", "--no-hgnc"]
    )
    out = capsys.readouterr().out
    assert exit_code == 1
    assert out.startswith("FAIL")
    assert "MONDO:0971173" in out


@pytest.mark.oak_db
@pytest.mark.skipif(
    os.environ.get("DISMECH_OAK_INTEGRATION") != "1",
    reason="set DISMECH_OAK_INTEGRATION=1 to check the live sqlite:obo:mondo adapter",
)
def test_integration_live_mondo_reverse_lookup_finds_the_tbk1_disease():
    """The reverse RO:0004003 query the #12166 fix depends on, against real MONDO."""
    from dismech.oak_db import local_build_present

    if not local_build_present("sqlite:obo:mondo"):
        pytest.skip("local mondo.db absent; `just fetch-ontology-dbs mondo`")
    from oaklib import get_adapter

    found, errors = find_rival_diseases(
        ["TNF", "TBK1"], "MONDO:0030717", get_adapter("sqlite:obo:mondo")
    )
    assert errors == []
    assert "TNF" not in found
    assert "MONDO:0971173" in {mid for mid, _label in found["TBK1"]}


@pytest.mark.oak_db
@pytest.mark.skipif(
    os.environ.get("DISMECH_OAK_INTEGRATION") != "1",
    reason="set DISMECH_OAK_INTEGRATION=1 to check the live sqlite:obo:mondo adapter",
)
def test_integration_live_mondo_adapter_resolves_the_canonical_gene_symbol():
    """Guards the load-bearing claim this PR added to CLAUDE.md.

    The rest of the suite stubs ``fetch_mondo_record``, so nothing else checks
    that ``sqlite:obo:mondo`` really carries the ``RO:0004003`` edge *and* a
    resolvable gene symbol on the other end of it.
    """
    from dismech.oak_db import local_build_present

    if not local_build_present("sqlite:obo:mondo"):
        pytest.skip("local mondo.db absent; `just fetch-ontology-dbs mondo`")
    record = fetch_mondo_record("MONDO:0014572")
    assert record.lookup_errors == ()
    assert record.genes == ("SLC9A1",)
    assert record.unresolved_genes == ()
    assert "616291" in record.omim_ids
    # The alias rescue is load-bearing for not manufacturing a FAIL, and it is
    # the one part of it that a prefix-case mismatch would silently disable.
    assert "PPP1R143" in record.gene_aliases.get("SLC9A1", ())
    # The gene's own approved symbol must not be listed as its alias: `assess`
    # would then count every SLC9A1 mention twice.
    assert "SLC9A1" not in record.gene_aliases.get("SLC9A1", ())
