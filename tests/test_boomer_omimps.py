"""OMIMPS scope and reproducibility checks, independent of local ontology DBs."""

import importlib.util
import json
import os
from pathlib import Path

import pytest
import yaml

SCRIPT = (
    Path(__file__).resolve().parents[1] / "analyses/boomer/scripts/omimps_pilots.py"
)
spec = importlib.util.spec_from_file_location("omimps_pilots", SCRIPT)
pilot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pilot)


@pytest.fixture
def reasoner_model(monkeypatch):
    source = os.environ.get("BOOMER_SRC")
    if not source:
        pytest.skip("Set BOOMER_SRC to exercise the actual reasoner")
    monkeypatch.syspath_prepend(str(Path(source).resolve()))
    from boomer import model, search

    return model, search.get_reasoner(model.SearchConfig().reasoner_class)


def test_certificate_proves_two_best_worlds(reasoner_model):
    model, reasoner = reasoner_model
    kb = model.KB(
        pfacts=[
            model.PFact(fact=model.EquivalentTo(sub="a", equivalent="b"), prob=0.8),
            model.PFact(fact=model.EquivalentTo(sub="c", equivalent="d"), prob=0.9),
        ]
    )
    result = pilot.certify_assignment(kb, reasoner)
    assert result["status"] == "CERTIFIED"
    assert result["best_assignment"] == [True, True]
    assert result["second_assignment"] == [False, True]
    assert result["confidence"] == pytest.approx(0.8)
    assert result["best_prior_weight"] == pytest.approx(0.72)
    assert result["second_prior_weight"] == pytest.approx(0.18)
    assert result["mapping_marginals"] == "NOT_COMPUTED"


def test_certificate_refuses_inconsistent_all_true(reasoner_model):
    model, reasoner = reasoner_model
    kb = model.KB(
        facts=[model.ProperSubClassOf(sub="a", sup="b")],
        pfacts=[
            model.PFact(fact=model.EquivalentTo(sub="a", equivalent="b"), prob=0.9),
        ],
    )
    assert pilot.certify_assignment(kb, reasoner)["status"] == "ALL_TRUE_INCONSISTENT"


def test_certificate_does_not_claim_blocked_runner_up(reasoner_model):
    model, reasoner = reasoner_model
    kb = model.KB(
        facts=[model.EquivalentTo(sub="a", equivalent="c")],
        pfacts=[
            model.PFact(fact=model.EquivalentTo(sub="a", equivalent="b"), prob=0.9),
            model.PFact(fact=model.EquivalentTo(sub="b", equivalent="c"), prob=0.95),
        ],
    )
    # Either single false contradicts the remaining equivalences. The best
    # feasible alternative flips both; the cheap sufficient proof must decline.
    result = pilot.certify_assignment(kb, reasoner)
    assert result["status"] == "ALL_TRUE_SATISFIABLE_SECOND_NOT_CERTIFIED"
    assert "confidence" not in result


def projection(slug):
    return json.loads((pilot.OUT / slug / "projection.json").read_text())


@pytest.mark.parametrize("slug", pilot.CASES)
@pytest.mark.parametrize("phase", ["before", "after"])
def test_committed_inputs_reproduce(slug, phase):
    kb, audit = pilot.compile_snapshot(projection(slug), phase)
    folder = pilot.OUT / slug / phase
    assert kb == yaml.safe_load((folder / "kb.yaml").read_text())
    assert audit == json.loads((folder / "audit.json").read_text())
    metadata = json.loads((folder / "result.json").read_text())
    assert metadata["input_sha256"] == pilot.sha((folder / "kb.yaml").read_bytes())
    assert metadata["boomer_commit"] == "744038e30741009930f57919ca2f03c6473ed198"
    assert metadata["timeout_seconds"] > 0
    assert metadata["search_config"]["max_pfacts_per_clique"] is None
    assert metadata["search_config"]["max_candidate_solutions"] == 0
    assert metadata["n_pfacts"] == len(kb["pfacts"])
    certificate = json.loads((folder / "certificate.json").read_text())
    assert certificate["input_sha256"] == metadata["input_sha256"]
    assert certificate["status"] == "CERTIFIED"
    assert all(certificate["best_assignment"])
    assert certificate["confidence"] == pytest.approx(0.9)
    verification = json.loads((folder / "enumeration.json").read_text())
    assert verification["input_sha256"] == metadata["input_sha256"]
    assert verification["status"] in {"VERIFIED", "EXHAUSTIVELY_ENUMERATED"}
    assert certificate["best_assignment"] in verification["optimal_assignments"]
    assert verification["confidence"] == pytest.approx(certificate["confidence"])
    assert verification["rejected_high_prior_indices"] == [[]]
    if verification["status"] == "VERIFIED":
        assert metadata["status"] in {"ALL_MAPPINGS_CONSISTENT", "RETRACTED"}
        assert (
            verification["distinct_solutions"]
            == metadata["number_of_satisfiable_combinations"]
        )


def test_msud_related_mapping_is_annotation_only():
    kb, audit = pilot.compile_snapshot(projection("msud"), "after")
    subject = "dismech:Maple_Syrup_Urine_Disease"
    assert any(
        a["subject"] == subject
        and a["target"] == "OMIMPS:248600"
        and a["predicate"] == "skos:relatedMatch"
        for a in audit["mapping_assertions"]
    )
    assert not any(
        p["fact"].get("sub") == subject
        and p["fact"].get("equivalent") == "OMIMPS:248600"
        for p in kb["pfacts"]
    )


def test_grouping_resolves_cbld_hc_not_its_parent():
    _kb, audit = pilot.compile_snapshot(projection("cbl"), "after")
    members = [
        a["fact"]["sub"]
        for a in audit["edge_provenance"]
        if a["source"] == "curated grouping member"
    ]
    assert len(members) == 3
    assert "MONDO:0700297" in {audit["nodes"][n]["term"] for n in members}
    assert any(
        "#" in n and audit["nodes"][n]["term"] == "MONDO:0700297" for n in members
    )


def test_pnh_alias_is_one_entity_and_non_mendelian_selected():
    kb, audit = pilot.compile_snapshot(projection("pnh"), "after")
    assert audit["aliases"][
        "dismech:Paroxysmal_Nocturnal_Hemoglobinuria#PIGT-associated PNH2"
    ] == ("dismech:Paroxysmal_Nocturnal_Hemoglobinuria_2")
    assert sum(n["term"] == "MONDO:0014166" for n in audit["nodes"].values()) == 1
    assert any(
        f["fact_type"] == "ProperSubClassOf"
        and f["sub"] == "dismech:Paroxysmal_Nocturnal_Hemoglobinuria_2"
        for f in kb["facts"]
    )
    assert (
        projection("pnh")["snapshots"]["after"]["records"][pilot.CASES["pnh"][2]][
            "data"
        ]["category"]
        == "Hematologic"
    )


def test_alias_mismatch_fails_loudly():
    data = projection("pnh")
    data["snapshots"]["after"]["records"][
        "kb/disorders/Paroxysmal_Nocturnal_Hemoglobinuria_2.yaml"
    ]["data"]["disease_term"]["term"]["id"] = "MONDO:bad"
    with pytest.raises(ValueError, match="Alias term mismatch"):
        pilot.compile_snapshot(data, "after")


def test_series_and_numbered_disease_are_distinct_identifiers():
    kb, _ = pilot.compile_snapshot(projection("bbs"), "after")
    assert "OMIM:209900" in kb["labels"]
    assert "OMIMPS:209900" in kb["labels"]
    assert kb["labels"]["OMIM:209900"] != kb["labels"]["OMIMPS:209900"]


def test_bbs_narrow_mapping_preserves_direction_and_coverage_scope():
    data = projection("bbs")
    kb, _ = pilot.compile_snapshot(data, "after")
    assert {
        "fact_type": "SubClassOf",
        "sub": "MONDO:0014434",
        "sup": "dismech:Bardet-Biedl_Syndrome#BBS5",
    } in [p["fact"] for p in kb["pfacts"]]
    candidates = pilot.scoped_member_mappings(data, "after", "OMIM:615983")
    assert [c["predicate"] for c in candidates] == ["skos:narrowMatch"]
    assert not data["snapshots"]["after"]["coverage"]["OMIM:615983"][
        "curated_candidates"
    ]


def test_no_missing_hierarchy_path_becomes_negative_fact():
    data = projection("lal")
    for record in data["ontology"].values():
        record["parents"] = []
        record["ancestors"] = []
        record["disjoint_with"] = []
    kb, _ = pilot.compile_snapshot(data, "after")
    assert not any(
        f["fact_type"] in {"DisjointWith", "NotInSubsumptionWith", "NegatedFact"}
        for f in kb["facts"]
    )


def test_pnh_baseline_precedes_entire_curation_pr():
    data = projection("pnh")
    assert (
        data["snapshots"]["before"]["commit"]
        == "bef670f17076625c96e5e8955a0a83d2d5108257"
    )
    assert (
        "kb/disorders/Paroxysmal_Nocturnal_Hemoglobinuria_2.yaml"
        in data["snapshots"]["before"]["missing_paths"]
    )
