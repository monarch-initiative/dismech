"""Regression checks for the scoped PS experiment and its saved evidence."""

import json
import sys
from pathlib import Path

import pytest
import yaml

SCRIPTS = Path(__file__).resolve().parents[1] / "analyses/boomer/scripts"
sys.path.insert(0, str(SCRIPTS))
import omimps_hemochromatosis as experiment


def projection():
    return json.loads((experiment.OUT / "projection.json").read_text())


@pytest.mark.parametrize("variant", experiment.VARIANTS)
def test_reproducible_inputs_and_verified_results(variant):
    kb, audit = experiment.build_variant(projection(), variant)
    folder = experiment.OUT / variant
    content = (folder / "kb.yaml").read_bytes()
    assert content == yaml.safe_dump(kb, sort_keys=False, allow_unicode=True).encode()
    assert audit == json.loads((folder / "audit.json").read_text())
    result = json.loads((folder / "result.json").read_text())
    enumerated = json.loads((folder / "enumeration.json").read_text())
    assert (
        result["input_sha256"]
        == enumerated["input_sha256"]
        == experiment.pilot.sha(content)
    )
    assert (
        result["boomer_commit"]
        == enumerated["boomer_commit"]
        == "744038e30741009930f57919ca2f03c6473ed198"
    )
    assert enumerated["status"] in {"VERIFIED", "EXHAUSTIVELY_ENUMERATED"}
    assert enumerated["confidence"] == pytest.approx(
        0.5 if variant in {"ordo", "all"} else 0.9
    )


def test_repair_changes_only_the_contested_equivalence():
    before, _ = experiment.build_variant(projection(), "all")
    after, audit = experiment.build_variant(projection(), "repair")
    assert before["facts"] == after["facts"]
    assert before["labels"] == after["labels"]
    contested = {
        "fact_type": "EquivalentTo",
        "sub": "MONDO:0011631",
        "equivalent": "ORDO:648562",
    }
    assert after["pfacts"] == [p for p in before["pfacts"] if p["fact"] != contested]
    assert any(
        d.get("predicate") == "skos:relatedMatch"
        for d in audit["external_mapping_decisions"]
    )
    assert not any(
        d["decision"] == "PERMIT_PROXY_MERGE" for d in audit["proxy_decisions"]
    )


def test_coverage_does_not_invent_a_curated_african_iron_overload_entry():
    p = projection()
    assert len(p["series_members"]) == 7
    assert p["coverage"]["OMIM:601195"]["curated_candidates"] == []
    assert sum(bool(v["curated_candidates"]) for v in p["coverage"].values()) == 6
    kb, audit = experiment.build_variant(p, "all")
    assert len(audit["nodes"]) == 2  # selected family and SLC40A1 row
    assert "MONDO:0011012" in kb["labels"]
    assert not any(n.endswith("#Type 1") for n in audit["nodes"])


def test_unqualified_codes_do_not_become_equalities():
    kb, audit = experiment.build_variant(projection(), "all")
    unqualified = {
        d["target"]
        for d in audit["external_mapping_decisions"]
        if d["decision"] == "EXCLUDE_UNQUALIFIED"
    }
    assert {"ICD10CM:E83.11", "ICD10CM:E83.119"} <= unqualified
    assert not any(set(p["fact"].values()) & unqualified for p in kb["pfacts"])
    # Each requested vocabulary genuinely contributes a qualified hypothesis.
    targets = {p["fact"].get("equivalent", "") for p in kb["pfacts"]}
    for namespace in ("DOID:", "ORDO:", "ICD10CM:", "icd11f:", "OMIM:", "OMIMPS:"):
        assert any(t.startswith(namespace) for t in targets)
