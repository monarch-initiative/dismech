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


def test_causal_environmental_edge_connects_phenotype() -> None:
    """A triggering exposure mechanistically explains a phenotype (#8033)."""
    data = {
        "phenotypes": [{"name": "Contact Dermatitis"}],
        "environmental": [
            {
                "name": "Nickel exposure",
                "influences_mechanisms": [
                    {
                        "target": "Contact Dermatitis",
                        "environmental_effect": "TRIGGERS",
                    }
                ],
            }
        ],
    }
    connected, total, unconnected = causal_inlink_coverage(data)
    assert (connected, total) == (1, 1)
    assert unconnected == []


def test_noncausal_environmental_edges_do_not_connect_phenotype() -> None:
    """Protective, predisposing and non-committal exposures do not explain a
    phenotype, so they must not count toward causal-inlink coverage (#8033)."""
    for effect in ["PROTECTS_AGAINST", "PREDISPOSES", "MODULATES", None]:
        link = {"target": "Contact Dermatitis"}
        if effect:
            link["environmental_effect"] = effect
        data = {
            "phenotypes": [{"name": "Contact Dermatitis"}],
            "environmental": [
                {"name": "Some exposure", "influences_mechanisms": [link]}
            ],
        }
        connected, total, unconnected = causal_inlink_coverage(data)
        assert (connected, total) == (0, 1), f"unexpected wiring for {effect!r}"
        assert unconnected == ["Contact Dermatitis"]


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
    assert (
        PhenotypeConnectivityPlugin().evaluate({"name": "x"}, QCConfig.default()) == []
    )


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
    assert any(v.slot_name == "causal_inlink" for v in base.threshold_violations)


def test_committed_causal_inlink_floor_is_set_and_never_lowered() -> None:
    """The committed connectivity floor is a ratchet: it moves up, never down.

    `phenotypes[].causal_inlink` carried `min_compliance: null` while the metric
    was advisory. It is now enforced -- `just compliance-connectivity` exits
    non-zero when the KB-wide aggregate falls below it, in `just qc` and as an
    ungated whole-KB CI step.

    The floor was set to 50.0 against a measured 52.4% (17354/33138 phenotype
    nodes). This test pins two things a future edit could quietly undo: that a
    floor exists at all (reverting to null disables the gate without touching
    any code), and that it is not lowered below its starting value to get a red
    build green. Raising it as coverage improves is the intended change and
    requires editing the constant here too, which is the point -- lowering it
    should be a deliberate, reviewed act rather than a one-character config fix.
    """
    from pathlib import Path

    config = QCConfig.from_yaml(
        str(Path(__file__).parent.parent / "conf" / "qc_config.yaml")
    )
    # Look the floor up exactly as the CLI does, through the plugin's own
    # `path`/`slot_name`. `get_min_compliance` takes the container path
    # ("phenotypes[]") and the slot separately and joins them; passing the
    # joined "phenotypes[].causal_inlink" as the path silently returns None,
    # which would make this test pass against a config that has no floor.
    plugin = PhenotypeConnectivityPlugin()
    floor = config.get_min_compliance(plugin.path, plugin.slot_name)

    assert floor is not None, (
        "phenotypes[].causal_inlink lost its min_compliance floor; a null here "
        "silently disables the connectivity gate in `just qc` and CI."
    )
    assert floor >= 50.0, (
        f"connectivity floor lowered to {floor}; it is a ratchet against erosion "
        "and is only ever raised. If CI is failing, wire up floating phenotypes "
        "(`just compliance-connectivity --list-unconnected`) rather than lowering "
        "the floor."
    )
