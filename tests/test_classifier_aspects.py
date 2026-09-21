"""Aspect construction and batched transport contracts, without API calls."""

from dataclasses import replace
import json

import httpx
import pytest

from dismech.classifier.aspects import aspect_output_schema
from dismech.classifier.structured import structured_claim_task
from dismech.classifier.typesafe import TypeSafeClassifier


def claim():
    return dict(
        about={"disease": {"name": "Probe"}},
        assertion_type="Phenotype",
        assertion={
            "description": "Recurrent fever",
            "frequency": "OCCASIONAL",
            "phenotype_term": {
                "term": {"id": "HP:0001954", "label": "Recurrent fever"}
            },
        },
        selected_evidence={"snippet": "Fevers.", "supports": "SUPPORT"},
    )


def test_questions_follow_present_fields_and_schema_semantics():
    properties = aspect_output_schema(claim())["properties"]
    assert set(properties) == {
        "/",
        "/assertion/description",
        "/assertion/frequency",
        "/assertion/phenotype_term/term",
    }
    assert "5-29%" in properties["/assertion/frequency"]["description"]
    other = claim()
    other["assertion"]["phenotype_term"]["temporality"] = "RECURRENT"
    assert (
        "/assertion/phenotype_term/temporality"
        in aspect_output_schema(other)["properties"]
    )
    other["reviews"] = [{"judgment": "MATCH", "rationale": "secret"}]
    assert aspect_output_schema(other) == aspect_output_schema(
        {k: v for k, v in other.items() if k != "reviews"}
    )


def test_one_request_maps_all_answers_and_counts_usage_once():
    sent = []
    task = structured_claim_task(claim())
    tasks = [
        replace(task, name=path, instructions=spec["description"])
        for path, spec in aspect_output_schema(claim())["properties"].items()
    ]

    def handle(request):
        payload = json.loads(request.content)
        sent.append(payload)
        return httpx.Response(
            200,
            json={
                "model": "test",
                "usage": {"input_tokens": 50},
                "answers": {
                    name: {
                        "type": "choice",
                        "choice": "MATCH",
                        "confidence": 0.8,
                        "probabilities": {"MATCH": 0.9, "MISMATCH": 0.1},
                    }
                    for name in payload["questions"]
                },
            },
        )

    client = TypeSafeClassifier(api_key="test", transport=httpx.MockTransport(handle))
    result = client.classify_many(tasks)
    assert len(sent) == 1
    assert sent[0]["state"] == task.state
    assert set(result.answers) == {t.name for t in tasks}
    assert result.usage == {"input_tokens": 50}
    assert all(t.name in sent[0]["questions"][t.name]["instructions"] for t in tasks)
    with pytest.raises(ValueError, match="distinct"):
        client.classify_many([task, task])
    with pytest.raises(ValueError, match="same state"):
        client.classify_many([task, replace(task, name="different", state={})])


def test_batch_rejects_missing_answers():
    client = TypeSafeClassifier(
        api_key="test",
        transport=httpx.MockTransport(
            lambda request: httpx.Response(200, json={"answers": {}})
        ),
    )
    with pytest.raises(ValueError, match="unexpected questions"):
        client.classify_many([structured_claim_task(claim())])
