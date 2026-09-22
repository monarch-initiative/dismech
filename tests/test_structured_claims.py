from copy import deepcopy
import json

import pytest
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from jsonschema import Draft7Validator

from dismech.classifier.claims import extract_claim, resolve, schema
from dismech.classifier.structured import structured_claim_task, mismatch_reason_task
from dismech.classifier.aspects import aspect_output_schema


def document():
    return {
        "name": "Example disease",
        "disease_term": {"preferred_term": "Example"},
        "has_subtypes": [
            {
                "name": "Childhood",
                "description": "Onset in children",
                "inheritance": [
                    {"name": "Autosomal recessive", "evidence": [evidence("REFUTE")]}
                ],
            }
        ],
        "biochemical": [
            {
                "name": "Marker",
                "presence": "Elevated",
                "subtype": "Childhood",
                "biomarker_term": {
                    "preferred_term": "Specific marker",
                    "term": {"id": "CHEBI:1", "label": "Specific marker"},
                },
                "context": "Assay-specific qualification",
                "evidence": [evidence(), evidence(snippet="SIBLING SECRET")],
            }
        ],
    }


def evidence(supports="SUPPORT", snippet="Marker increased."):
    return {
        "reference": "PMID:1",
        "supports": supports,
        "snippet": snippet,
        "explanation": "EXPLANATION MUST NOT NARROW THE CLAIM",
    }


def test_whole_object_preserves_qualifiers_and_subtype_without_other_evidence():
    doc = document()
    before = deepcopy(doc)
    claim = extract_claim(doc, "/biochemical/0/evidence/0")
    assert claim["assertion_type"] == "Biochemical"
    assert claim["assertion"] == {
        k: v for k, v in doc["biochemical"][0].items() if k != "evidence"
    }
    assert claim["about"]["context"][0]["path"] == "/has_subtypes/0"
    assert claim["about"]["context"][0]["value"] == {
        "name": "Childhood",
        "description": "Onset in children",
    }
    task = structured_claim_task(claim)
    assert "SIBLING SECRET" not in json.dumps(task.state)
    assert "EXPLANATION MUST" not in json.dumps(task.state)
    assert "origin" not in task.state
    assert doc == before
    assert set(task.criteria) == {"MATCH", "MISMATCH", "PARTIAL"}


def test_nested_assertion_inherits_parent_scope_and_keeps_refutation_on_evidence():
    claim = extract_claim(document(), "/has_subtypes/0/inheritance/0/evidence/0")
    assert claim["assertion"] == {"name": "Autosomal recessive"}
    assert claim["selected_evidence"]["supports"] == "REFUTE"
    assert claim["about"]["context"][0]["value"]["name"] == "Childhood"
    assert claim["about"]["context"][0]["role"] == "ancestor"
    assert "inheritance" not in claim["about"]["context"][0]["value"]


def test_nested_edge_preserves_source_and_complete_target_assertion():
    doc = {
        "name": "D",
        "pathophysiology": [
            {
                "name": "Source",
                "description": "Source mechanism",
                "genetic_context": {"variant_origin": "SOMATIC"},
                "downstream": [
                    {
                        "target": "phenotype#Target",
                        "causal_link_type": "DIRECT",
                        "evidence": [evidence()],
                    }
                ],
            }
        ],
    }
    c = extract_claim(doc, "/pathophysiology/0/downstream/0/evidence/0")
    assert c["assertion_type"] == "CausalEdge"
    assert c["assertion"]["target"] == "phenotype#Target"
    assert c["about"]["context"][0]["value"]["genetic_context"] == {
        "variant_origin": "SOMATIC"
    }
    assert "downstream" not in c["about"]["context"][0]["value"]


def test_parent_assertion_does_not_drop_child_claim_fields():
    doc = document()
    doc["biochemical"][0]["readouts"] = [
        {"name": "Nested measurement", "evidence": [evidence()]}
    ]
    c = extract_claim(doc, "/biochemical/0/evidence/0")
    assert c["assertion"]["readouts"] == [{"name": "Nested measurement"}]


@pytest.mark.parametrize(
    "edge_evidence", [None, [], [evidence(snippet="EDGE EVIDENCE")]]
)
def test_node_evidence_excludes_independent_edges_even_without_edge_evidence(
    edge_evidence,
):
    edge = {"target": "EDGE TARGET", "description": "EDGE DESCRIPTION"}
    if edge_evidence is not None:
        edge["evidence"] = edge_evidence
    node = {
        "name": "Node",
        "description": "Node mechanism",
        "biological_processes": [
            {"term": {"id": "GO:1", "label": "Process"}, "modifier": "INCREASED"}
        ],
        "downstream": [edge],
        "evidence": [evidence()],
    }
    doc = {"name": "D", "pathophysiology": [node]}
    before = deepcopy(doc)
    path = "/pathophysiology/0/evidence/0"
    claim = extract_claim(doc, path)
    assert "downstream" not in claim["assertion"]
    assert claim["assertion"]["biological_processes"] == node["biological_processes"]
    assert claim["origin"]["evidence_path"] == path
    legacy = extract_claim(doc, path, include_downstream=True)
    assert legacy["assertion"]["downstream"][0]["target"] == "EDGE TARGET"
    for candidate in [claim, legacy]:
        task = structured_claim_task(candidate)
        assert "EDGE" not in json.dumps(task.state)
        assert task.state["assertion"] == claim["assertion"]
        assert not any(
            "downstream" in p for p in aspect_output_schema(candidate)["properties"]
        )
    assert doc == before


def test_pointer_escaping_and_invalid_indices():
    assert resolve({"a/b": {"~key": [42]}}, "/a~1b/~0key/0") == 42
    for path in ("/a~2b", "not/a/pointer", "/items/-1", "/items/01", "/items/2"):
        with pytest.raises(ValueError):
            resolve({"items": [0]}, path)


def test_fail_closed_on_missing_subtype_direction_or_annotation_context():
    d = document()
    d["has_subtypes"] = []
    with pytest.raises(ValueError, match="Subtype"):
        extract_claim(d, "/biochemical/0/evidence/0")
    d = document()
    del d["biochemical"][0]["evidence"][0]["supports"]
    with pytest.raises(ValueError, match="direction"):
        extract_claim(d, "/biochemical/0/evidence/0")
    with pytest.raises(ValueError, match="annotations"):
        extract_claim(
            document(),
            "/biochemical/0/evidence/0",
            context_paths=["/biochemical/0/evidence"],
        )


def test_reason_contract_and_source_context():
    c = extract_claim(document(), "/biochemical/0/evidence/0")
    t = mismatch_reason_task(c, "Full source context")
    assert set(t.criteria) == {
        "insufficient_specificity",
        "incompatible_assertion",
        "unrelated",
        "other",
    }
    assert t.state["source_text"] == "Full source context"


def test_main_schema_validates_wrapper_and_direction():
    generated = json.loads(
        JsonSchemaGenerator(
            schema().schema.source_file, top_class="StructuredClaim"
        ).serialize()
    )
    validator = Draft7Validator(generated)
    c = extract_claim(document(), "/biochemical/0/evidence/0")
    validator.validate(c)
    c["selected_evidence"]["supports"] = "PARTIAL"
    assert list(validator.iter_errors(c))
