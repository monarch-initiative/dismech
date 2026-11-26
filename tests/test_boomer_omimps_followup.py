"""Frozen follow-ups preserve scope, source corrections, and solver provenance."""

import importlib.util
import json
import os
import sys
from pathlib import Path

import pytest
import yaml

SCRIPTS = Path(__file__).resolve().parents[1] / "analyses/boomer/scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location(
    "omimps_followup", SCRIPTS / "omimps_followup.py"
)
followup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(followup)


def projection(case):
    return json.loads((followup.OUT / case / "projection.json").read_text())


@pytest.mark.parametrize("case", followup.CASES)
@pytest.mark.parametrize("phase", ["before", "after"])
def test_frozen_inputs_and_complete_results(case, phase):
    kb, audit = followup.compile_case(case, projection(case), phase)
    folder = followup.OUT / case / phase
    content = (folder / "kb.yaml").read_bytes()
    assert kb == yaml.safe_load(content)
    assert content == yaml.safe_dump(kb, sort_keys=False, allow_unicode=True).encode()
    assert audit == json.loads((folder / "audit.json").read_text())
    result = json.loads((folder / "result.json").read_text())
    assert result["input_sha256"] == followup.pilot.sha(content)
    assert result["boomer_commit"] == "744038e30741009930f57919ca2f03c6473ed198"
    assert result["n_pfacts"] == len(kb["pfacts"])
    enumeration = json.loads((folder / "enumeration.json").read_text())
    assert enumeration["input_sha256"] == result["input_sha256"]
    assert enumeration["status"] in {"VERIFIED", "EXHAUSTIVELY_ENUMERATED"}
    if case in {"gorlin", "praas", "tpmt"} and phase == "before":
        assert enumeration["confidence"] == pytest.approx(0.5)
        assert all(enumeration["rejected_high_prior_indices"])
    else:
        assert enumeration["rejected_high_prior_indices"] == [[]]
        expected = 0.95 if case == "gorlin" else 0.9
        assert enumeration["confidence"] == pytest.approx(expected)


@pytest.mark.parametrize("case", ["gorlin", "praas", "tpmt"])
def test_source_intervention_holds_curation_and_other_hypotheses_fixed(case):
    p = projection(case)
    assert p["snapshots"]["before"]["records"] == p["snapshots"]["after"]["records"]
    before, _ = followup.compile_case(case, p, "before")
    after, _ = followup.compile_case(case, p, "after")
    assert before["facts"] == after["facts"]
    assert before["labels"] == after["labels"]

    def without_do(kb):
        return [
            pf
            for pf in kb["pfacts"]
            if not any(str(v).startswith("DOID:") for v in pf["fact"].values())
        ]

    assert without_do(before) == without_do(after)


def test_foxe3_legacy_identity_is_removed_without_strengthening_related_match():
    p = projection("foxe3")
    before, _ = followup.compile_case("foxe3", p, "before")
    after, audit = followup.compile_case("foxe3", p, "after")
    subject = "dismech:FOXE3_Anterior_Segment_Dysgenesis"
    eq = {"fact_type": "EquivalentTo", "sub": subject, "equivalent": "MONDO:0019503"}
    assert eq in [pf["fact"] for pf in before["pfacts"]]
    assert eq not in [pf["fact"] for pf in after["pfacts"]]
    assert any(
        a["subject"] == subject
        and a["target"] == "OMIMPS:107250"
        and a["predicate"] == "skos:relatedMatch"
        for a in audit["mapping_assertions"]
    )
    assert not any(
        pf["fact"].get("sub") == subject
        and pf["fact"].get("equivalent") == "OMIMPS:107250"
        for pf in after["pfacts"]
    )


def test_waldenstrom_sensitivity_changes_only_source_equivalence():
    p = projection("waldenstrom")
    before, _ = followup.compile_case("waldenstrom", p, "before")
    after, audit = followup.compile_case("waldenstrom", p, "after")
    assert before["facts"] == after["facts"]
    assert before["labels"] == after["labels"]
    removed = [pf for pf in before["pfacts"] if pf not in after["pfacts"]]
    assert removed == [
        {
            "fact": {
                "fact_type": "EquivalentTo",
                "sub": "MONDO:0100280",
                "equivalent": "OMIMPS:153600",
            },
            "prob": 0.95,
        }
    ]
    assert "not an applied" in next(
        a["source"]
        for a in audit["mapping_assertions"]
        if a["subject"] == "MONDO:0100280" and a["target"] == "OMIMPS:153600"
    )


@pytest.mark.parametrize("case", followup.CASES)
def test_actual_reasoner_all_true_scope_controls(case, monkeypatch):
    source = os.environ.get("BOOMER_SRC")
    if not source:
        pytest.skip("Set BOOMER_SRC to exercise the actual reasoner")
    monkeypatch.syspath_prepend(str(Path(source).resolve()))
    from boomer import model, search

    reasoner = search.get_reasoner(model.SearchConfig().reasoner_class)
    for phase in ("before", "after"):
        data, _ = followup.compile_case(case, projection(case), phase)
        kb = model.KB.model_validate(data)
        result = reasoner.reason(kb, list(enumerate([True] * len(kb.pfacts))))
        assert result.satisfiable == (
            phase == "after" or case in {"foxe3", "waldenstrom"}
        )
