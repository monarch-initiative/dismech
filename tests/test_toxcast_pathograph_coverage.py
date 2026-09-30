"""The coverage count is a join, and every rule of the join is a place to miscount.

``scripts/toxcast_pathograph_coverage.py`` pairs a ToxCast endpoint with a
pathophysiology node when both name the same gene. These tests pin what does and
does not count as naming it, on either side, against the trimmed annotation
fixture and a four-entry knowledge base built for the purpose. No test needs
``CTX_API_KEY`` or the cached panel.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import toxcast_pathograph_coverage as coverage

from dismech.toxcast_assays import ToxCastAssayAnnotations

DATA_DIR = Path(__file__).parent / "data" / "toxcast"


def gene(symbol: str, hgnc_id: str) -> str:
    return (
        f"    - preferred_term: {symbol}\n"
        f"      term:\n        id: {hgnc_id}\n        label: {symbol}\n"
    )


# ESR1 reaches a node three ways across two entries; AR is bound nowhere.
ON_NODE = (
    "name: Receptor Disease\n"
    "pathophysiology:\n"
    "- name: Receptor Activation\n"
    "  biological_scale: MOLECULAR\n"
    "  genes:\n" + gene("ESR1", "hgnc:3467") + "- name: Receptor Variant\n"
    "  biological_scale: MOLECULAR\n"
    "  genetic_context:\n"
    "    variant_origin: GERMLINE\n"
    "    gene:\n"
    "      preferred_term: ESR1\n"
    "      term:\n        id: hgnc:3467\n        label: ESR1\n"
    "- name: Tissue Consequence\n"
    "  biological_scale: TISSUE\n"
)

SINGULAR_GENE = (
    "name: Second Receptor Disease\n"
    "pathophysiology:\n"
    "- name: Receptor Loss\n"
    "  gene:\n"
    "    preferred_term: ESR1\n"
    "    term:\n      id: hgnc:3467\n      label: ESR1\n"
)

# ESR2 sits in `genetic:` and on no node; TTR only as a treatment's target.
OFF_NODE = (
    "name: Off Node Disease\n"
    "pathophysiology:\n"
    "- name: Unexplained Step\n"
    "genetic:\n"
    "- name: ESR2\n"
    "  gene_term:\n"
    "    preferred_term: ESR2\n"
    "    term:\n      id: hgnc:3468\n      label: ESR2\n"
    "treatments:\n"
    "- name: Silencer\n"
    "  oligonucleotide_details:\n"
    "    target_gene:\n"
    "      preferred_term: TTR\n"
    "      term:\n        id: hgnc:12405\n        label: TTR\n"
)

# Names AR twice without binding the human gene either time.
UNBOUND = (
    "name: Unbound Disease\n"
    "pathophysiology:\n"
    "- name: Free Text Gene\n"
    "  genes:\n"
    "  - preferred_term: AR\n"
    "  - preferred_term: Ar\n"
    "    term:\n      id: MGI:88064\n      label: Ar\n"
)

MODULE = (
    "name: Receptor Module\n"
    "pathophysiology:\n"
    "- name: Generic Receptor Step\n"
    "  genes:\n" + gene("ESR1", "hgnc:3467")
)


@pytest.fixture
def cov(tmp_path: Path) -> coverage.Coverage:
    disorders = tmp_path / "disorders"
    modules = tmp_path / "modules"
    disorders.mkdir()
    modules.mkdir()
    (disorders / "Receptor_Disease.yaml").write_text(ON_NODE, encoding="utf-8")
    (disorders / "Second_Receptor_Disease.yaml").write_text(
        SINGULAR_GENE, encoding="utf-8"
    )
    (disorders / "Off_Node_Disease.yaml").write_text(OFF_NODE, encoding="utf-8")
    (disorders / "Unbound_Disease.yaml").write_text(UNBOUND, encoding="utf-8")
    (modules / "receptor_module.yaml").write_text(MODULE, encoding="utf-8")
    snapshot = ToxCastAssayAnnotations(DATA_DIR).load()
    return coverage.build(snapshot, disorders, modules)


# ----- the ToxCast side -----


def test_symbol_key_upper_cases_so_orthologs_share_a_key():
    assert coverage.symbol_keys("Esr1") == ["ESR1"]


def test_superseded_symbols_are_read_as_the_approved_symbol():
    """Otherwise the gene reads as absent from dismech whatever dismech binds."""
    assert coverage.symbol_keys("H2AFX") == ["H2AX"]
    assert coverage.symbol_keys("H3F3A") == ["H3-3A"]
    assert coverage.symbol_keys("PPP2R4") == ["PTPA"]


def test_a_composite_gene_object_is_split_into_its_genes():
    """Endpoint 1846 names `FOS|JUN` as one gene object."""
    assert coverage.symbol_keys("FOS|JUN") == ["FOS", "JUN"]


def test_a_target_is_human_only_through_a_human_gene_object(cov):
    """ESR1 collects mouse endpoint 725, which does not make 725 a human one."""
    esr1 = cov.targets["ESR1"]
    assert esr1.aeids == {2, 725, 744}
    assert esr1.human_aeids == {2, 744}
    assert esr1.human
    assert esr1.written_as == {"ESR1", "Esr1"}


def test_gene_less_endpoints_contribute_no_target(cov):
    assert set(cov.targets) == {"AR", "ESR1", "ESR2", "TTR"}
    assert {e.aeid for e in cov.with_gene()} == {2, 725, 744, 1816, 3089}


# ----- the dismech side -----


def test_a_node_names_a_gene_through_any_slot_the_graph_links_on(cov):
    """`genes[]`, the singular `gene`, and the gene of a `genetic_context`."""
    names = {(n.entry, n.name) for n in cov.index.nodes_by_gene["ESR1"]}
    assert names == {
        ("Receptor_Disease", "Receptor Activation"),
        ("Receptor_Disease", "Receptor Variant"),
        ("Second_Receptor_Disease", "Receptor Loss"),
    }


def test_an_unbound_or_non_hgnc_descriptor_names_no_gene(cov):
    """Free text `AR` and mouse `MGI:` Ar are not bindings of the human gene."""
    assert "AR" not in cov.index.nodes_by_gene
    assert "AR" not in cov.index.anywhere_by_gene
    assert cov.index.n_nodes == 6
    assert len(cov.index.gene_nodes) == 3


def test_a_genetic_context_marks_the_node_as_recording_a_variant(cov):
    by_name = {n.name: n for n in cov.candidate_nodes()}
    assert by_name["Receptor Variant"].has_variant
    assert not by_name["Receptor Activation"].has_variant


def test_an_untagged_node_is_counted_as_untagged_not_dropped(cov):
    assert cov.index.scale_of_all_nodes["MOLECULAR"] == 2
    assert cov.index.scale_of_all_nodes["TISSUE"] == 1
    assert cov.index.scale_of_all_nodes[coverage.UNTAGGED] == 3


# ----- the join -----


def test_each_target_takes_the_strictest_tier_it_satisfies(cov):
    assert cov.tier("ESR1") == "ON_NODE"
    assert cov.tier("ESR2") == "GENETIC_ONLY"
    assert cov.tier("TTR") == "ELSEWHERE_ONLY"
    assert cov.tier("AR") == "ABSENT"


def test_a_candidate_endpoint_is_one_whose_target_a_node_names(cov):
    assert {e.aeid for e in cov.candidates()} == {2, 725, 744}


def test_an_ortholog_endpoint_is_a_candidate_but_not_a_human_one(cov):
    """725 reaches the ESR1 nodes through mouse Esr1 alone."""
    assert {e.aeid for e in cov.human_candidates()} == {2, 744}


def test_a_two_gene_endpoint_reaches_each_node_once(cov):
    """744 names ESR1 and ESR2; only ESR1 is on a node."""
    endpoint = next(e for e in cov.endpoints if e.aeid == 744)
    assert len(cov.nodes_for(endpoint)) == 3


def test_pairs_count_every_endpoint_against_every_node_it_reaches(cov):
    assert cov.pair_count() == 9


def test_disease_coverage_separates_on_node_from_bound_elsewhere(cov):
    assert cov.candidate_entries() == {"Receptor_Disease", "Second_Receptor_Disease"}
    assert cov.off_node_entries() == {"Off_Node_Disease"}


def test_modules_are_indexed_apart_from_disorders(cov):
    assert cov.modules.n_entries == 1
    assert {n.entry for n in cov.modules.nodes_by_gene["ESR1"]} == {"receptor_module"}
    assert "receptor_module" not in cov.candidate_entries()


# ----- output -----


def test_summary_carries_the_headline_figures(cov):
    figures = coverage.summary(cov)
    assert figures["endpoints"] == 7
    assert figures["endpoints_with_gene"] == 5
    assert figures["candidate_endpoints"] == 3
    assert figures["candidate_endpoints_human_gene"] == 2
    assert figures["targets"] == 4
    assert figures["targets_by_tier"] == {
        "ON_NODE": 1,
        "GENETIC_ONLY": 1,
        "ELSEWHERE_ONLY": 1,
        "ABSENT": 1,
    }
    assert figures["candidate_nodes"] == 3
    assert figures["candidate_nodes_with_genetic_context"] == 1
    assert figures["candidate_entries"] == 2
    assert figures["entries_binding_a_target_off_node"] == 1


def test_markdown_states_that_a_candidate_is_not_a_mapping(cov):
    report = coverage.render_markdown(cov)
    assert "A shared gene is a **candidate**, not a mapping." in report
    assert "## Pathograph node coverage" in report
    assert "## Gene coverage" in report
    assert "## Disease coverage" in report
    assert "retrieved from the EPA CTX API on **2026-09-24**" in report


@pytest.mark.parametrize(
    ("table", "header", "rows"),
    [
        ("targets", "symbol\thuman_gene\ttier", 4),
        ("nodes", "entry\tnode\tbiological_scale", 3),
        ("endpoints", "aeid\tname\tgenes", 7),
        ("diseases", "entry\tcandidate_nodes\ttargets", 2),
    ],
)
def test_each_tsv_table_has_one_row_per_thing_it_names(cov, table, header, rows):
    lines = coverage.render_tsv(cov, table).splitlines()
    assert lines[0].startswith(header)
    assert len(lines) == rows + 1


def test_main_names_the_refresh_recipe_when_nothing_is_cached(tmp_path, capsys):
    """Exit 2, not a traceback and not a fetch."""
    assert coverage.main(["--data-dir", str(tmp_path)]) == 2
    assert "just toxcast-refresh" in capsys.readouterr().err
