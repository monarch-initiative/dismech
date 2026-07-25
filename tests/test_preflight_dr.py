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

from collections import Counter
from pathlib import Path

import pytest

from dismech.preflight_dr import (
    FAIL,
    PASS,
    SKIP,
    WARN,
    HeuristicLexicon,
    MondoRecord,
    assess,
    extract_gene_mentions,
    extract_omim_ids,
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
        lambda mondo_id, adapter=None: record,
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


def test_case2_report_also_cites_the_wrong_entity_omim():
    """The SCAR20 report cites OMIM:616354, not Lichtenstein-Knorr's OMIM:616291."""
    report_omim = extract_omim_ids(LICHTENSTEIN_KNORR.read_text(encoding="utf-8"))
    assert "616354" in report_omim
    assert "616291" not in report_omim


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


def test_cli_exits_nonzero_on_fail(monkeypatch, capsys):
    _stub_adapter(monkeypatch, REC_LIKNS)
    monkeypatch.setattr("dismech.preflight_dr.HgncLexicon", lambda: CASE_GENES)
    code = main([str(LICHTENSTEIN_KNORR), "MONDO:0014572"])
    assert code == 1
    assert "FAIL" in capsys.readouterr().out


def test_cli_warn_is_tolerated_unless_strict(monkeypatch):
    _stub_adapter(monkeypatch, REC_TEMTAMY)
    monkeypatch.setattr("dismech.preflight_dr.HgncLexicon", lambda: CASE_GENES)
    assert main([str(TEMTAMY), "MONDO:0009033"]) == 0
    assert main([str(TEMTAMY), "MONDO:0009033", "--strict"]) == 1


def test_cli_emits_json(monkeypatch, capsys):
    import json

    _stub_adapter(monkeypatch, REC_LIKNS)
    monkeypatch.setattr("dismech.preflight_dr.HgncLexicon", lambda: CASE_GENES)
    main([str(LICHTENSTEIN_KNORR), "MONDO:0014572", "--json"])
    payload = json.loads(capsys.readouterr().out)
    assert payload["verdict"] == FAIL
    assert payload["expected_genes"] == ["SLC9A1"]


def test_cli_rejects_a_non_mondo_identifier(monkeypatch):
    _stub_adapter(monkeypatch, REC_LIKNS)
    with pytest.raises(SystemExit):
        main([str(LICHTENSTEIN_KNORR), "OMIM:616291"])
