"""Tests for graph-derived QC metric plugins (phenotype connectivity)."""

from linkml_data_qc.config import PathQCConfig, QCConfig
from linkml_data_qc.models import AggregatedPathScore, ComplianceReport

from dismech.qc_plugins import (
    GeneMechanismWiringPlugin,
    PhenotypeConnectivityPlugin,
    augment_report,
    causal_inlink_coverage,
    gene_mechanism_wiring_coverage,
)


def _disorder() -> dict:
    """A disorder with one connected and one floating phenotype."""
    return {
        "name": "Test Disorder",
        "pathophysiology": [
            {
                "name": "Mechanism A",
                "downstream": [{"target": "Connected Phenotype"}],
            }
        ],
        "phenotypes": [
            {"name": "Connected Phenotype"},
            {"name": "Floating Phenotype"},
        ],
    }


def test_causal_inlink_coverage_identifies_floating_phenotype() -> None:
    connected, total, unconnected = causal_inlink_coverage(_disorder())
    assert (connected, total) == (1, 2)
    assert unconnected == ["Floating Phenotype"]


def test_treats_edge_does_not_count_as_causal_connection() -> None:
    """A treatment targeting a phenotype must not mark it mechanistically wired."""
    data = {
        "phenotypes": [{"name": "Pain"}],
        "treatments": [
            {
                "name": "Analgesic",
                "target_phenotypes": [{"preferred_term": "Pain"}],
            }
        ],
    }
    connected, total, unconnected = causal_inlink_coverage(data)
    assert (connected, total) == (0, 1)
    assert unconnected == ["Pain"]


def test_sequelae_chain_connects_downstream_phenotype() -> None:
    data = {
        "pathophysiology": [{"name": "M", "downstream": [{"target": "Pheno A"}]}],
        "phenotypes": [
            {"name": "Pheno A", "sequelae": [{"target": "Pheno B"}]},
            {"name": "Pheno B"},
        ],
    }
    connected, total, _ = causal_inlink_coverage(data)
    assert (connected, total) == (2, 2)


def test_plugin_emits_graded_aggregated_score() -> None:
    config = QCConfig(
        paths={
            "phenotypes[].causal_inlink": PathQCConfig(weight=2.0, min_compliance=90.0)
        }
    )
    scores = PhenotypeConnectivityPlugin().evaluate(_disorder(), config)
    assert len(scores) == 1
    score = scores[0]
    assert isinstance(score, AggregatedPathScore)
    assert score.path == "phenotypes[]"
    assert score.slot_name == "causal_inlink"
    assert (score.populated, score.total) == (1, 2)
    assert score.percentage == 50.0
    assert score.weight == 2.0
    assert score.min_compliance == 90.0


def test_plugin_returns_no_score_when_no_phenotypes() -> None:
    assert PhenotypeConnectivityPlugin().evaluate({"name": "x"}, QCConfig.default()) == []


def _mendelian() -> dict:
    """One gene wired into a mechanism, one gene floating (no matching node)."""
    return {
        "name": "Test Mendelian Disorder",
        "genetic": [
            {
                "name": "COL1A1 pathogenic variant",
                "gene_term": {"term": {"id": "hgnc:2197", "label": "COL1A1"}},
                "relationship_type": "CAUSAL",
            },
            {
                "name": "Floating Gene",
                "gene_term": {"term": {"id": "hgnc:9999", "label": "FLOAT1"}},
                "relationship_type": "CAUSAL",
            },
        ],
        "pathophysiology": [
            {
                "name": "Defective Collagen Synthesis",
                "gene": {"term": {"id": "hgnc:2197", "label": "COL1A1"}},
            }
        ],
    }


def test_gene_wiring_coverage_identifies_floating_gene() -> None:
    wired, total, unwired = gene_mechanism_wiring_coverage(_mendelian())
    assert (wired, total) == (1, 2)
    assert unwired == ["Floating Gene"]


def test_biomarker_gene_excluded_from_denominator() -> None:
    """A non-causal (BIOMARKER) genetic item is not expected to wire in."""
    data = {
        "genetic": [
            {
                "name": "Prognostic Marker",
                "gene_term": {"term": {"id": "hgnc:1234", "label": "MARK1"}},
                "relationship_type": "BIOMARKER",
            }
        ],
        "pathophysiology": [{"name": "Some Mechanism"}],
    }
    wired, total, unwired = gene_mechanism_wiring_coverage(data)
    assert (wired, total) == (0, 0)
    assert unwired == []


def test_gene_wiring_plugin_emits_graded_score() -> None:
    config = QCConfig(
        paths={
            "genetic[].mechanism_outlink": PathQCConfig(weight=1.5, min_compliance=None)
        }
    )
    scores = GeneMechanismWiringPlugin().evaluate(_mendelian(), config)
    assert len(scores) == 1
    score = scores[0]
    assert isinstance(score, AggregatedPathScore)
    assert score.path == "genetic[]"
    assert score.slot_name == "mechanism_outlink"
    assert (score.populated, score.total) == (1, 2)
    assert score.percentage == 50.0
    assert score.weight == 1.5


def test_gene_wiring_plugin_returns_no_score_without_genes() -> None:
    assert GeneMechanismWiringPlugin().evaluate({"name": "x"}, QCConfig.default()) == []


def test_augment_report_folds_in_connectivity_and_recomputes() -> None:
    base = ComplianceReport(
        file_path="t.yaml",
        target_class="Disease",
        schema_path="s.yaml",
        global_compliance=100.0,
        weighted_compliance=100.0,
        total_checks=2,
        total_populated=2,
        aggregated_scores=[
            AggregatedPathScore(
                path="(root)",
                slot_name="description",
                parent_class="Disease",
                populated=2,
                total=2,
                percentage=100.0,
                weight=1.0,
            )
        ],
    )
    config = QCConfig(
        paths={
            "phenotypes[].causal_inlink": PathQCConfig(weight=2.0, min_compliance=90.0)
        }
    )

    augment_report(base, _disorder(), config)

    # New score appended.
    inlink = [s for s in base.aggregated_scores if s.slot_name == "causal_inlink"]
    assert len(inlink) == 1
    # Weighted compliance drops: (2*1 + 1*2) / (2*1 + 2*2) = 4/6.
    assert round(base.weighted_compliance, 1) == 66.7
    # 50% < 90% threshold -> a violation is appended.
    assert any(
        v.slot_name == "causal_inlink" for v in base.threshold_violations
    )
