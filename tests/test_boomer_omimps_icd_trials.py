"""Resource additions retain baseline scope and qualified source mappings."""

import importlib.util
import json
import os
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "analyses/boomer/scripts"
CASES = ("gorlin", "foxe3", "waldenstrom")
VARIANTS = ("baseline", "ordo", "icd10cm", "icd11f", "all")
EXPERIMENTS = [(c, v) for c in CASES for v in VARIANTS] + [("foxe3", "repair")]


@pytest.fixture
def trial(monkeypatch):
    monkeypatch.syspath_prepend(str(SCRIPTS))
    spec = importlib.util.spec_from_file_location(
        "icd_trial_test", SCRIPTS / "omimps_icd_trials.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def projection(trial, case):
    return json.loads((trial.OUT / case / "projection.json").read_text())


@pytest.mark.parametrize("case,variant", EXPERIMENTS)
def test_frozen_artifact_reproduction_and_complete_results(trial, case, variant):
    p = projection(trial, case)
    kb, audit = trial.build_variant(p, variant)
    folder = trial.OUT / case / variant
    content = (folder / "kb.yaml").read_bytes()
    assert content == yaml.safe_dump(kb, sort_keys=False, allow_unicode=True).encode()
    assert audit == json.loads((folder / "audit.json").read_text())
    result = json.loads((folder / "result.json").read_text())
    enum = json.loads((folder / "enumeration.json").read_text())
    assert result["input_sha256"] == enum["input_sha256"] == trial.pilot.sha(content)
    assert result["boomer_commit"] == "744038e30741009930f57919ca2f03c6473ed198"
    assert enum["status"] in {"VERIFIED", "EXHAUSTIVELY_ENUMERATED"}
    assert result["search_config"]["max_pfacts_per_clique"] is None
    assert result["search_config"]["max_candidate_solutions"] == 0
    if case == "foxe3" and variant in {"icd11f", "all"}:
        assert enum["confidence"] == pytest.approx(0.5)
        assert len(enum["optimal_assignments"]) == 2
        assert all(len(r) == 1 for r in enum["rejected_high_prior_indices"])
    else:
        assert enum["rejected_high_prior_indices"] == [[]]
    baseline = p["baseline"]["kb"]
    assert kb["pfacts"][: len(baseline["pfacts"])] == baseline["pfacts"]
    assert all(f in kb["facts"] for f in baseline["facts"])
    if variant == "baseline":
        assert trial.pilot.sha(content) == p["baseline"]["input_sha256"]


def test_unqualified_cm_links_do_not_become_equivalences(trial):
    kb, audit = trial.build_variant(projection(trial, "gorlin"), "icd10cm")
    assert audit["mapping_decisions"][0]["target"] == "ICD10CM:Q87.8"
    assert audit["mapping_decisions"][0]["decision"] == "EXCLUDE_UNQUALIFIED"
    assert not any("ICD10CM:" in str(p) for p in kb["pfacts"])
    kb, audit = trial.build_variant(projection(trial, "foxe3"), "icd10cm")
    included = {
        a["target"]
        for a in audit["mapping_decisions"]
        if a["decision"] == "INCLUDE_QUALIFIED"
    }
    assert included == {"ICD10CM:Q12.3"}


def test_missing_icd11_mapping_is_not_invented(trial):
    p = projection(trial, "waldenstrom")
    kb, audit = trial.build_variant(p, "icd11f")
    assert kb == p["baseline"]["kb"]
    assert audit["mapping_decisions"] == []


def test_foxe3_repair_changes_only_one_mapping_at_same_prior(trial):
    p = projection(trial, "foxe3")
    before, audit = trial.build_variant(p, "all")
    after, _ = trial.build_variant(p, "repair")
    assert before["facts"] == after["facts"]
    assert before["labels"] == after["labels"]
    differences = [
        (a, b) for a, b in zip(before["pfacts"], after["pfacts"], strict=True) if a != b
    ]
    assert differences == [
        (
            {
                "fact": {
                    "fact_type": "EquivalentTo",
                    "sub": "MONDO:0019503",
                    "equivalent": "icd11f:943599144",
                },
                "prob": 0.95,
            },
            {
                "fact": {
                    "fact_type": "SubClassOf",
                    "sub": "MONDO:0019503",
                    "sup": "icd11f:943599144",
                },
                "prob": 0.95,
            },
        )
    ]
    assert audit["proxy_decisions"][0]["decision"] == "REVIEW_PREFERENCE_COUNT"
    assert {
        "fact_type": "SubClassOf",
        "sub": "icd11f:1182282997",
        "sup": "icd11f:943599144",
    } in before["facts"]
    assert p["icd11_parent_children"]["icd11f:1050179356"]["label"] == "Blue sclera"
    assert p["icd11_parent_children"]["icd11f:84750333"]["label"] == "Heterochromia"


@pytest.mark.parametrize(
    "reason", ["deprecated", "missing", "conflicting", "obsolete_mondo"]
)
def test_unsuitable_source_mapping_is_excluded(trial, reason):
    p = projection(trial, "gorlin")
    t = p["external"]["ORDO:377"]
    if reason == "deprecated":
        t["deprecated"] = True
    elif reason == "missing":
        t["label"] = None
    elif reason == "conflicting":
        p["catalog"]["terms"]["MONDO:0007187"]["mappings"]["ORDO:377"]["qualifiers"][
            "source"
        ].append("MONDO:mondoIsNarrowerThanSource")
    else:
        p["catalog"]["terms"]["MONDO:0007187"]["obsolete"] = True
    kb, audit = trial.build_variant(p, "ordo")
    assert kb == p["baseline"]["kb"]
    assert audit["mapping_decisions"][0]["decision"].startswith(("EXCLUDE", "REVIEW"))


@pytest.mark.parametrize("case", CASES)
def test_actual_reasoner_resource_comparison(trial, case, monkeypatch):
    source = os.environ.get("BOOMER_SRC")
    if not source:
        pytest.skip("Set BOOMER_SRC to exercise the actual reasoner")
    monkeypatch.syspath_prepend(str(Path(source).resolve()))
    from boomer import model, search

    reasoner = search.get_reasoner(model.SearchConfig().reasoner_class)
    for variant in (*VARIANTS, *(["repair"] if case == "foxe3" else [])):
        data, _ = trial.build_variant(projection(trial, case), variant)
        kb = model.KB.model_validate(data)
        result = reasoner.reason(kb, list(enumerate([True] * len(kb.pfacts))))
        assert result.satisfiable == (
            case != "foxe3" or variant not in {"icd11f", "all"}
        )
