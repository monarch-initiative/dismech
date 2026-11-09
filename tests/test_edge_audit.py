"""Synthetic end-to-end edge extraction, caching and reporting contracts."""

import csv
import json
from copy import deepcopy
from dataclasses import asdict

import pytest
import yaml
from click.testing import CliRunner

from dismech.classifier.aspects import aspect_output_schema, aspect_prompt
from dismech.classifier.audit import assess, inventory, main, tasks_for
from dismech.classifier.audit_report import write_reports
from dismech.classifier.base import ClassificationTask
from dismech.classifier.cache import ResultCache, cache_key, digest, input_key
from dismech.classifier.claims import extract_claim
from dismech.classifier.edge_reading import canonical_edge_claim, extract_edge_claim
from dismech.classifier.rubric import CRITERIA
from dismech.classifier.structured import structured_claim_task
from tests.test_classifier_audit import FakeClassifier
from tests.test_edge_reading import document

PATH = "/pathophysiology/0/downstream/0/evidence/0"


@pytest.mark.parametrize("kind", ["mechanism", "phenotype", "treatment"])
def test_automatic_bindings_equal_explicit_extraction(kind):
    doc = document(treatment=kind == "treatment")
    path = (
        PATH if kind != "treatment" else "/treatments/0/target_mechanisms/0/evidence/0"
    )
    target = "/pathophysiology/0" if kind == "treatment" else "/pathophysiology/1"
    if kind == "phenotype":
        endpoint = doc["pathophysiology"].pop()
        endpoint.pop("biological_processes")
        endpoint.pop("downstream")
        doc["phenotypes"].append(endpoint)
        target = "/phenotypes/1"
    paths = [target]
    if kind != "treatment":
        paths += ["/mechanistic_hypotheses/0"]
    before = deepcopy(doc)
    expected = canonical_edge_claim(extract_claim(doc, path, context_paths=paths))
    actual = canonical_edge_claim(extract_edge_claim(doc, path))
    assert actual == expected
    assert doc == before
    assert "MUST NOT LEAK" not in json.dumps(actual)


def test_target_only_scope_is_bound_without_duplicate_inherited_subtype():
    doc = document()
    doc["has_subtypes"].append({"name": "Endpoint subtype"})
    doc["pathophysiology"][1]["subtypes"] = ["Model subtype", "Endpoint subtype"]
    doc["pathophysiology"][1]["hypothesis_groups"] = ["candidate_route"]
    result = canonical_edge_claim(extract_edge_claim(doc, PATH))
    assert [s["name"] for s in result["scope"]["subtypes"]] == [
        "Endpoint subtype",
        "Model subtype",
    ]
    assert len(result["scope"]["hypotheses"]) == 1


@pytest.mark.parametrize(
    "problem", ["missing", "ambiguous", "hypothesis", "duplicate_hypothesis", "subtype"]
)
def test_unresolved_edges_are_reported_without_paid_calls(tmp_path, problem):
    doc = document()
    if problem == "missing":
        doc["pathophysiology"][0]["downstream"][0]["target"] = "Absent"
    elif problem == "ambiguous":
        doc["phenotypes"].append({"name": doc["pathophysiology"][1]["name"]})
    elif problem == "hypothesis":
        doc["mechanistic_hypotheses"] = []
    elif problem == "duplicate_hypothesis":
        doc["mechanistic_hypotheses"] *= 2
    else:
        doc["pathophysiology"][1]["subtypes"] = ["Absent"]
    file = tmp_path / "example.yaml"
    file.write_text(yaml.safe_dump(doc))
    rows = list(inventory([file], assertion_types=["CausalEdge"]))
    row = next(r for r in rows if r["evidence_path"] == PATH)
    assert row["status"] == "invalid_input"
    fake = FakeClassifier()
    list(assess(rows, fake, ResultCache(tmp_path / "cache"), 1))
    assert fake.calls == 0


def test_node_tasks_and_keys_are_identical_to_previous_contract():
    doc = document()
    doc["pathophysiology"][0]["evidence"] = [
        {"snippet": "Synthetic node observation.", "supports": "SUPPORT"}
    ]
    claim = extract_claim(doc, "/pathophysiology/0/evidence/0")
    state = structured_claim_task(claim).state
    prompt = aspect_prompt()
    expected = [
        ClassificationTask(
            name=path,
            version=prompt["version"],
            state=state,
            instructions=prompt["instructions"] + "\n" + spec["description"],
            criteria=dict(CRITERIA),
        )
        for path, spec in aspect_output_schema(claim, fields=None)["properties"].items()
    ]
    assert [asdict(t) for t in tasks_for(claim)] == [asdict(t) for t in expected]
    assert cache_key("test", tasks_for(claim)) == cache_key("test", expected)
    assert input_key(claim) == digest(state)


def test_edge_cache_provenance_resume_and_reports(tmp_path):
    file = tmp_path / "example.yaml"
    file.write_text(yaml.safe_dump(document()))
    row = next(r for r in inventory([file]) if r["evidence_path"] == PATH)
    cache = ResultCache(tmp_path / "cache")
    fake = FakeClassifier()
    results = list(assess([row], fake, cache, 1, revision="revision"))
    assert list(assess([row], fake, cache, 1))[0]["cached"]
    assert fake.calls == 1
    saved = yaml.safe_load(next((tmp_path / "cache").glob("*/*.yaml")).read_text())
    item = saved["inputs"][input_key(row["claim"])]
    assert item["claim"] == row["claim"]
    assert item["origin"]["evidence_path"] == PATH
    assert item["evidence_metadata"]["reference"] == "SYNTHETIC:1"
    assert "EXPLANATION" in item["evidence_metadata"]["explanation"]
    (tmp_path / "results.jsonl").write_text(json.dumps(results[0]) + "\n")
    assert write_reports(tmp_path)["assessed_pairs"] == 1
    aspects = list(csv.DictReader((tmp_path / "aspects.csv").open()))
    root = next(a for a in aspects if a["aspect_path"] == "/")
    assert json.loads(root["aspect_value"])["subject"] == row["claim"]["subject"]


def test_cli_filter_and_manifest(tmp_path):
    file = tmp_path / "example.yaml"
    file.write_text(yaml.safe_dump(document(treatment=True)))
    args = [
        "--input",
        str(file),
        "--output",
        str(tmp_path / "output"),
        "--dry-run",
        "--assertion-type",
        "TreatmentMechanismTarget",
        "--limit",
        "1",
    ]
    result = CliRunner().invoke(main, args)
    assert result.exit_code == 0, result.output
    manifest = json.loads((tmp_path / "output/manifest.json").read_text())
    assert manifest["assertion_types"] == ["TreatmentMechanismTarget"]
    assert manifest["edge_prompt"]["version"] == "2"
    assert manifest["inventory_counts"] == {"ready": 1}
    assert (
        CliRunner().invoke(main, ["--dry-run", "--assertion-type", "Typo"]).exit_code
        != 0
    )


def test_canonical_migration_preserves_old_scores_and_node_activity(tmp_path):
    doc = document(treatment=True)
    doc["treatments"][0]["evidence"] = [
        {"snippet": "Synthetic treatment observation.", "supports": "SUPPORT"}
    ]
    file = tmp_path / "example.yaml"
    file.write_text(yaml.safe_dump(doc))
    edge_path = "/treatments/0/target_mechanisms/0/evidence/0"
    edge = next(r for r in inventory([file]) if r["evidence_path"] == edge_path)
    legacy = dict(edge, claim=extract_claim(doc, edge_path))
    node = next(
        r for r in inventory([file]) if r["evidence_path"] == "/treatments/0/evidence/0"
    )
    cache = ResultCache(tmp_path / "cache")
    fake = FakeClassifier()
    old = list(assess([legacy, node], fake, cache, 1))
    list(assess([edge], fake, cache, 1))
    cache.reconcile([file], "canonical-revision")
    saved = yaml.safe_load(next((tmp_path / "cache").glob("*/*.yaml")).read_text())
    assert not saved["inputs"][input_key(legacy["claim"])]["active"]
    assert saved["inputs"][input_key(edge["claim"])]["active"]
    assert saved["inputs"][input_key(node["claim"])]["active"]
    assert saved["assessments"][old[0]["cache_key"]]["result"] == old[0]["result"]
    assert list(assess([node], fake, cache, 1))[0]["cached"]
    assert fake.calls == 3
