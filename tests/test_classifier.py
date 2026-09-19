"""Offline contracts for evidence selection and the live-service boundary."""

from dataclasses import replace
import json

import httpx
import pytest

from dismech.classifier.evidence import EvidenceInput, evidence_task, iter_evidence
from dismech.classifier.typesafe import TypeSafeClassifier


def item():
    return EvidenceInput(
        claim={"description": "X causes Y"},
        snippet="X did not cause Y.",
        supports="REFUTE",
        directness="DIRECT",
        context={"disease": "Example"},
    )


def response():
    return {
        "model": "jev-test",
        "usage": {"input_tokens": 100, "output_tokens": 10},
        "answers": {
            "claim_evidence": {
                "type": "choice",
                "choice": "MATCH",
                "confidence": 0.8,
                "probabilities": {"MATCH": 0.9, "MISMATCH": 0.1},
            }
        },
    }


def test_annotation_is_part_of_state_and_missing_directness_stays_missing():
    assert evidence_task(item()).state["supports"] == "REFUTE"
    assert evidence_task(item()).state["directness"] == "DIRECT"
    assert evidence_task(replace(item(), directness=None)).state["directness"] is None
    with pytest.raises(ValueError, match="supports"):
        replace(item(), supports="PARTIAL")
    with pytest.raises(ValueError, match="snippet"):
        replace(item(), snippet=" ")


def test_nested_edge_keeps_source_target_and_own_annotation_only():
    doc = {
        "name": "Disease",
        "pathophysiology": [
            {
                "name": "Source",
                "description": "Source mechanism",
                "downstream": [
                    {
                        "target": "Target",
                        "description": "Source causes target",
                        "evidence": [
                            {
                                "reference": "PMID:1",
                                "snippet": "No effect",
                                "supports": "REFUTE",
                                "directness": "INDIRECT",
                            }
                        ],
                    }
                ],
                "evidence": [
                    {"reference": "PMID:2", "snippet": "Sibling", "supports": "SUPPORT"}
                ],
            }
        ],
    }
    rows = list(iter_evidence(doc))
    edge = rows[1]
    assert edge["id"] == "pathophysiology[0].downstream[0].evidence[0]"
    assert edge["input"]["claim"]["target"] == "Target"
    assert edge["input"]["context"]["ancestors"][0]["name"] == "Source"
    assert edge["input"]["supports"] == "REFUTE"
    assert "Sibling" not in json.dumps(edge["input"])
    assert "No effect" not in json.dumps(rows[0]["input"]["claim"])


def test_http_payload_result_and_annotation_sensitive_hash():
    sent = []

    def handle(request):
        assert request.headers["authorization"] == "Bearer test-key"
        payload = json.loads(request.content)
        assert set(payload) == {"state", "questions", "model"}
        assert payload["questions"]["claim_evidence"]["type"] == "choice"
        sent.append(payload)
        return httpx.Response(200, json=response())

    client = TypeSafeClassifier(
        api_key="test-key", transport=httpx.MockTransport(handle)
    )
    first = client.classify(evidence_task(item()))
    second = client.classify(evidence_task(replace(item(), directness="INDIRECT")))
    assert first.label == "MATCH"
    assert first.probabilities["MISMATCH"] == 0.1
    assert first.model == "jev-test"
    assert first.request_sha256 != second.request_sha256
    assert sent[0]["state"]["supports"] == "REFUTE"
    assert "test-key" not in repr(first)


@pytest.mark.parametrize(
    "change",
    [
        {"choice": "OTHER"},
        {"choice": "MISMATCH"},
        {"probabilities": {"MATCH": 0.8, "MISMATCH": 0.8}},
        {"probabilities": {"MATCH": -0.1, "MISMATCH": 1.1}},
        {"confidence": float("nan")},
        {"type": "noul"},
    ],
)
def test_malformed_answer_is_never_a_verdict(change):
    body = response()
    body["answers"]["claim_evidence"].update(change)
    client = TypeSafeClassifier(
        api_key="test",
        transport=httpx.MockTransport(
            lambda request: httpx.Response(200, content=json.dumps(body)),
        ),
    )
    with pytest.raises(ValueError):
        client.classify(evidence_task(item()))


def test_missing_key_and_http_failure(monkeypatch):
    monkeypatch.delenv("TYPESAFE_API_KEY", raising=False)
    with pytest.raises(ValueError, match="TYPESAFE_API_KEY"):
        TypeSafeClassifier()
    client = TypeSafeClassifier(
        api_key="test",
        transport=httpx.MockTransport(
            lambda request: httpx.Response(401),
        ),
    )
    with pytest.raises(httpx.HTTPStatusError):
        client.classify(evidence_task(item()))


def test_rate_limit_retry(monkeypatch):
    sleeps = []
    monkeypatch.setattr("dismech.classifier.typesafe.time.sleep", sleeps.append)
    calls = []

    def handle(request):
        calls.append(request)
        return (
            httpx.Response(429)
            if len(calls) == 1
            else httpx.Response(200, json=response())
        )

    client = TypeSafeClassifier(api_key="test", transport=httpx.MockTransport(handle))
    assert client.classify(evidence_task(item())).label == "MATCH"
    assert sleeps == [1]


def test_cli_dry_run_omits_expected_label_and_preserves_existing_output(
    tmp_path, monkeypatch
):
    from dataclasses import asdict
    import sys
    from dismech.classifier.__main__ import main

    source = tmp_path / "cases.jsonl"
    output = tmp_path / "report.jsonl"
    source.write_text(
        json.dumps({"id": "case", "expected": "MATCH", "input": asdict(item())}) + "\n"
    )
    monkeypatch.delenv("TYPESAFE_API_KEY", raising=False)
    monkeypatch.setattr(
        sys, "argv", ["classifier", str(source), "--dry-run", "--output", str(output)]
    )
    assert main() == 0
    record = json.loads(output.read_text())
    assert "expected" not in record
    assert "result" not in record
    assert record["task"]["state"]["supports"] == "REFUTE"
    before = output.read_bytes()
    with pytest.raises(FileExistsError):
        main()
    assert output.read_bytes() == before


def test_cli_service_failure_is_recorded_not_classified(tmp_path, monkeypatch):
    from dataclasses import asdict
    import sys
    from dismech.classifier.__main__ import main

    source = tmp_path / "cases.jsonl"
    output = tmp_path / "report.jsonl"
    source.write_text(json.dumps({"id": "case", "input": asdict(item())}) + "\n")
    monkeypatch.setenv("TYPESAFE_API_KEY", "test-key")
    monkeypatch.setattr(
        sys, "argv", ["classifier", str(source), "--output", str(output)]
    )

    def fail(self, task):
        raise httpx.ReadTimeout("sensitive diagnostic must not enter output")

    monkeypatch.setattr(TypeSafeClassifier, "classify", fail)
    assert main() == 1
    record = json.loads(output.read_text())
    assert record["error"] == "ReadTimeout"
    assert "result" not in record
    assert "sensitive" not in output.read_text()


def test_direct_support_arms_only_differ_by_source_text():
    from dismech.classifier.direct_support import direct_support_task

    without = direct_support_task("X causes Y", "These patients had Y.")
    with_source = direct_support_task(
        "X causes Y",
        "These patients had Y.",
        "We studied patients with X. These patients had Y.",
    )
    assert without.instructions == with_source.instructions
    assert without.criteria == with_source.criteria
    assert without.version == with_source.version
    assert without.state == {
        k: v for k, v in with_source.state.items() if k != "source_text"
    }
    assert set(without.state) == {"claim", "snippet"}
    assert "supports" not in with_source.state
    assert "directness" not in with_source.state
    assert with_source.state["source_text"].startswith("We studied")


@pytest.mark.parametrize("args", [("", "quote"), ("claim", ""), ("claim", "quote", "")])
def test_direct_support_rejects_empty_inputs(args):
    from dismech.classifier.direct_support import direct_support_task

    with pytest.raises(ValueError, match="nonempty"):
        direct_support_task(*args)
