"""Tests for the Named Entity Confusion (NEC) preflight check (dismech #3889).

All tests are offline: the OAK-backed MONDO lookup is exercised only through
injected gene sets, so the decision logic is deterministic and network-free.
"""

from __future__ import annotations

from dismech.preflight_dr import (
    evaluate,
    extract_gene_mentions,
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
