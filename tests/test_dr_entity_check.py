"""Tests for the Named Entity Confusion (NEC) preflight check (dismech #3889).

All tests are offline: the OAK-backed MONDO lookup is exercised only through
injected gene sets, so the decision logic is deterministic and network-free.
"""

from __future__ import annotations

import pytest

from dismech import preflight_dr
from dismech.preflight_dr import (
    CAUSAL_GENE_PREDICATES,
    evaluate,
    extract_gene_mentions,
    main,
    mondo_causal_genes,
    rank_genes,
)


def _ranked(text: str):
    return rank_genes(extract_gene_mentions(text))


# --------------------------------------------------------------------------- #
# Gene extraction
# --------------------------------------------------------------------------- #


def test_extract_picks_up_gene_symbols():
    text = "Variants in SLC9A1 (NHE1) impair sodium-hydrogen exchange."
    counts = extract_gene_mentions(text)
    assert counts["SLC9A1"] == 1
    assert counts["NHE1"] == 1


def test_extract_handles_orf_symbols():
    text = "C12orf57 is the causal gene; C12orf57 loss disrupts neurons."
    counts = extract_gene_mentions(text)
    assert counts["C12orf57"] == 2
    # The orf token must not be double-counted as a fragment.
    assert "C" not in counts


def test_extract_drops_ontology_and_lab_tokens():
    text = "MONDO:0014572 OMIM PMID DNA RNA CSF AR review of HEXB."
    counts = extract_gene_mentions(text)
    assert counts["HEXB"] == 1
    for noise in ("MONDO", "OMIM", "PMID", "DNA", "RNA", "CSF", "AR"):
        assert noise not in counts


def test_extract_drops_sequencing_method_acronyms():
    # Lab/sequencing acronyms recur in DR prose and must not inflate gene counts.
    text = "WES and WGS plus PCR, NGS, FISH and MLPA confirmed HEXB variants."
    counts = extract_gene_mentions(text)
    assert counts["HEXB"] == 1
    for noise in ("WES", "WGS", "PCR", "NGS", "FISH", "MLPA"):
        assert noise not in counts


# --------------------------------------------------------------------------- #
# Case 1 (PASS): report's primary gene matches MONDO canonical gene
# --------------------------------------------------------------------------- #


def test_case1_pass_primary_gene_matches():
    report = (
        "Lichtenstein-Knorr syndrome arises from biallelic SLC9A1 variants. "
        "SLC9A1 encodes NHE1; loss of SLC9A1 function impairs pH regulation. "
        "SLC9A1 is expressed in Purkinje cells."
    )
    result = evaluate(_ranked(report), {"SLC9A1"}, mondo_id="MONDO:0014572")
    assert result.status == "PASS"
    assert result.ok


# --------------------------------------------------------------------------- #
# Case 2 (FAIL): report's primary gene is SNX14 but canonical gene is SLC9A1
# --------------------------------------------------------------------------- #


def test_case2_fail_wrong_entity_gene():
    report = (
        "This disorder is caused by SNX14 mutations. SNX14 loss leads to "
        "autophagy-lysosome dysfunction. SNX14 deficient neurons degenerate; "
        "SNX14 is the SCAR20 gene."
    )
    result = evaluate(_ranked(report), {"SLC9A1"}, mondo_id="MONDO:0014572")
    assert result.status == "FAIL"
    assert not result.ok
    assert "SNX14" in result.message


# --------------------------------------------------------------------------- #
# Case 3 (WARN): two genes from different eponymous diseases (Temtamy pattern)
# --------------------------------------------------------------------------- #


def test_case3_warn_eponym_mix_top_is_noncausal():
    # CHSY1 (TPBS) dominates but the true causal C12orf57 is also present.
    report = (
        "Temtamy preaxial brachydactyly involves CHSY1 and chondroitin "
        "sulfate. CHSY1 regulates BMP and NOTCH. CHSY1 morphants in zebrafish "
        "show brachydactyly. The C12orf57 Temtamy syndrome is distinct."
    )
    result = evaluate(_ranked(report), {"C12orf57"}, mondo_id="MONDO:0009033")
    assert result.status == "WARN"
    assert not result.ok


def test_case3_warn_competing_gene_when_top_is_causal():
    # Causal gene leads, but a non-causal eponym gene competes strongly.
    report = (
        "C12orf57 syndrome features intellectual disability. C12orf57 loss "
        "impairs neurons. C12orf57 is the cause. However CHSY1 brachydactyly "
        "CHSY1 chondroitin CHSY1 BMP signaling are frequently conflated."
    )
    result = evaluate(_ranked(report), {"C12orf57"}, mondo_id="MONDO:0009033")
    assert result.status == "WARN"
    assert any(g == "CHSY1" for g, _ in result.competitors)


# --------------------------------------------------------------------------- #
# Case 4 (SKIP): MONDO ID has no single causal gene (complex/multifactorial)
# --------------------------------------------------------------------------- #


def test_case4_skip_no_causal_gene():
    report = "Idiopathic intracranial hypertension involves obesity and CSF."
    result = evaluate(_ranked(report), set(), mondo_id="MONDO:0009468")
    assert result.status == "SKIP"
    assert result.ok


def test_skip_when_no_gene_mentions():
    report = "A purely clinical description with no gene symbols at all."
    result = evaluate(_ranked(report), {"SLC9A1"}, mondo_id="MONDO:0014572")
    assert result.status == "SKIP"


def test_skip_when_all_tokens_are_stoplisted():
    # Gene-shaped tokens are present but every one is in the stoplist, so the
    # ranked list is empty after filtering and the check must SKIP, not FAIL.
    report = "DNA RNA MRI CT PCR WES MONDO OMIM HGNC CNS ROS analysis."
    ranked = _ranked(report)
    assert ranked == []
    result = evaluate(ranked, {"SLC9A1"}, mondo_id="MONDO:0014572")
    assert result.status == "SKIP"
    assert result.ok


# --------------------------------------------------------------------------- #
# Multi-gene MONDO entries and exit-code mapping
# --------------------------------------------------------------------------- #


def test_pass_when_top_gene_is_one_of_several_causal():
    report = "TGFBR1 signaling drives this aortopathy. TGFBR1 TGFBR1 variants."
    result = evaluate(
        _ranked(report), {"TGFBR1", "TGFBR2"}, mondo_id="MONDO:0000000"
    )
    assert result.status == "PASS"


def test_render_is_human_readable():
    result = evaluate(_ranked("SLC9A1 SLC9A1 SLC9A1"), {"SLC9A1"})
    text = result.render()
    assert "NEC preflight: PASS" in text
    assert "SLC9A1" in text


# --------------------------------------------------------------------------- #
# Predicate set is grounded in what MONDO actually uses for causal-gene edges
# --------------------------------------------------------------------------- #


def test_causal_predicate_set_covers_germline_and_somatic():
    # The two dominant germline forms and the somatic-driver form must all be
    # present, otherwise GoF-germline / cancer entries would spuriously SKIP.
    for predicate in ("RO:0004003", "RO:0004001", "RO:0004004"):
        assert predicate in CAUSAL_GENE_PREDICATES


# --------------------------------------------------------------------------- #
# OAK-backed lookup exercised through a stub adapter (no network)
# --------------------------------------------------------------------------- #


class _StubAdapter:
    """Minimal OAK-like adapter for mondo_causal_genes tests."""

    def __init__(self, triples, labels=None):
        self._triples = triples
        self._labels = labels or {}

    def relationships(self, subjects=None):
        return list(self._triples)

    def label(self, curie):
        return self._labels.get(curie)


def test_mondo_causal_genes_filters_to_hgnc_and_uses_labels():
    adapter = _StubAdapter(
        triples=[
            ("MONDO:0014572", "RO:0004003", "HGNC:11071"),
            # Non-causal predicate is ignored even though object is HGNC.
            ("MONDO:0014572", "RO:0004026", "HGNC:99999"),
            # Non-HGNC object is ignored.
            ("MONDO:0014572", "RO:0004003", "UBERON:0000955"),
        ],
        labels={"HGNC:11071": "SLC9A1"},
    )
    assert mondo_causal_genes("MONDO:0014572", adapter=adapter) == ["SLC9A1"]


def test_mondo_causal_genes_falls_back_to_curie_without_label():
    adapter = _StubAdapter(
        triples=[("MONDO:0000123", "RO:0004004", "HGNC:1234")],
        labels={},  # no label available
    )
    assert mondo_causal_genes("MONDO:0000123", adapter=adapter) == ["HGNC:1234"]


def test_mondo_causal_genes_deduplicates_case_insensitively():
    adapter = _StubAdapter(
        triples=[
            ("MONDO:0000123", "RO:0004003", "HGNC:1"),
            ("MONDO:0000123", "RO:0004013", "HGNC:2"),
        ],
        labels={"HGNC:1": "ABC1", "HGNC:2": "abc1"},
    )
    assert mondo_causal_genes("MONDO:0000123", adapter=adapter) == ["ABC1"]


def test_mondo_causal_genes_empty_for_multifactorial():
    adapter = _StubAdapter(triples=[("MONDO:0007", "RO:0004026", "HGNC:5")])
    assert mondo_causal_genes("MONDO:0007", adapter=adapter) == []


# --------------------------------------------------------------------------- #
# CLI entry point
# --------------------------------------------------------------------------- #


def test_main_errors_on_missing_report(tmp_path):
    missing = tmp_path / "nope.md"
    with pytest.raises(SystemExit):
        main([str(missing), "MONDO:0014572"])


def test_main_errors_on_bad_mondo_curie(tmp_path):
    report = tmp_path / "r.md"
    report.write_text("SLC9A1", encoding="utf-8")
    with pytest.raises(SystemExit):
        main([str(report), "not-a-curie"])


def test_main_exit_codes(tmp_path, monkeypatch, capsys):
    report = tmp_path / "r.md"
    report.write_text("SNX14 SNX14 SNX14 dominate this report.", encoding="utf-8")

    # Stub the OAK lookup so the CLI stays offline and deterministic.
    monkeypatch.setattr(preflight_dr, "mondo_causal_genes", lambda *_a, **_k: ["SLC9A1"])
    code = main([str(report), "MONDO:0014572"])
    out = capsys.readouterr().out
    assert "NEC preflight: FAIL" in out
    assert code == 2  # FAIL is always non-zero

    # PASS path returns 0.
    report.write_text("SLC9A1 SLC9A1 SLC9A1 confirmed.", encoding="utf-8")
    assert main([str(report), "MONDO:0014572"]) == 0


def test_main_warn_exit_respects_strict(tmp_path, monkeypatch):
    report = tmp_path / "r.md"
    # Top gene is causal but a non-causal gene competes strongly → WARN.
    report.write_text(
        "C12orf57 C12orf57 C12orf57 cause. CHSY1 CHSY1 CHSY1 conflated.",
        encoding="utf-8",
    )
    monkeypatch.setattr(preflight_dr, "mondo_causal_genes", lambda *_a, **_k: ["C12orf57"])
    # Default: WARN is downgraded to exit 0.
    assert main([str(report), "MONDO:0009033"]) == 0
    # --strict: WARN exits non-zero.
    assert main([str(report), "MONDO:0009033", "--strict"]) == 1
