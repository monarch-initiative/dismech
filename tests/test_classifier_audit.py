"""Bulk audits preserve scope, resume paid work, and distinguish failures."""

import csv
import json
import time
from copy import deepcopy
from dataclasses import asdict

import httpx
import pytest
import yaml
from click.testing import CliRunner

from dismech.classifier.audit import (
    ResultCache,
    assess,
    cache_key,
    inventory,
    main,
    tasks_for,
)
from dismech.classifier.audit_report import merge_shards, write_reports
from dismech.classifier.base import ChoiceAnswer, ClassificationBatch
from dismech.classifier.claims import extract_claim
from dismech.classifier.typesafe import TypeSafeClassifier


def evidence(text="Example disease causes fever."):
    return {"reference": "PMID:1", "supports": "SUPPORT", "snippet": text}


def disease():
    return {
        "name": "Example disease",
        "has_subtypes": [{"name": "Childhood", "description": "Childhood onset"}],
        "phenotypes": [
            {
                "name": "Fever",
                "frequency": "FREQUENT",
                "subtypes": ["Childhood"],
                "phenotype_term": {"term": {"id": "HP:0001945", "label": "Fever"}},
                "evidence": [
                    evidence(),
                    evidence("Fever in children with Example disease."),
                ],
                "sequelae": [
                    {
                        "target": "Seizures",
                        "evidence": [
                            evidence("Fever causes seizures in Example disease.")
                        ],
                    }
                ],
            }
        ],
        "pathophysiology": [
            {
                "name": "Inflammation",
                "evidence": [evidence()],
                "downstream": [{"target": "Fever"}],
            }
        ],
        "treatments": [
            {
                "name": "Therapy",
                "evidence": [{"reference": "PMID:2", "supports": "SUPPORT"}],
            }
        ],
    }


def rows(tmp_path):
    file = tmp_path / "disease.yaml"
    file.write_text(yaml.safe_dump(disease()))
    return list(inventory([file]))


class FakeClassifier:
    model = "jev-test"

    def __init__(self, fail=()):
        self.calls = 0
        self.fail = fail

    def classify_many(self, tasks):
        self.calls += 1
        if self.calls in self.fail:
            raise httpx.ReadTimeout("secret should not appear in reports")
        answers = {}
        for task in tasks:
            label = (
                "MISMATCH"
                if "frequency" in task.name
                else "PARTIAL"
                if task.name == "/"
                else "MATCH"
            )
            probabilities = {
                k: 0.8 if k == label else 0.1 for k in ("MATCH", "MISMATCH", "PARTIAL")
            }
            answers[task.name] = ChoiceAnswer(label, probabilities, 0.6)
        return ClassificationBatch(
            answers, self.model, {"input_tokens": 12, "output_tokens": 4}, 0.01, "hash"
        )


def test_every_evidence_pair_and_missing_evidence_is_inventoried(tmp_path):
    result = rows(tmp_path)
    assert len(result) == 7
    assert [r["status"] for r in result].count("ready") == 4
    assert [r["status"] for r in result].count("no_evidence") == 2
    assert [r["status"] for r in result].count("missing_snippet") == 1
    parent = next(r for r in result if r["evidence_path"] == "/phenotypes/0/evidence/0")
    assert "sequelae" not in parent["claim"]["assertion"]
    assert "evidence" not in json.dumps(parent["claim"]["assertion"])
    paths = {t.name for t in tasks_for(parent["claim"])}
    assert {
        "/",
        "/about/disease",
        "/assertion/subtypes",
        "/assertion/frequency",
        "/assertion/phenotype_term/term",
        "/about/context/0/value",
    } <= paths
    edge = next(r for r in result if "sequelae/0/evidence" in r["evidence_path"])
    assert edge["claim"]["assertion_type"] == "CausalEdge"
    assert edge["claim"]["about"]["context"][0]["value"]["name"] == "Fever"


def test_invalid_direction_and_subtype_are_data_errors(tmp_path):
    data = disease()
    data["phenotypes"][0]["subtypes"] = ["Nonexistent"]
    data["pathophysiology"][0]["evidence"][0].pop("supports")
    file = tmp_path / "bad.yaml"
    file.write_text(yaml.safe_dump(data))
    result = list(inventory([file]))
    assert sum(r["status"] == "invalid_input" for r in result) == 4
    assert all("result" not in r for r in result)


def test_successes_resume_errors_retry_and_input_changes_invalidate(tmp_path):
    cache = ResultCache(tmp_path / "cache.sqlite")
    selected = [r for r in rows(tmp_path) if r["status"] == "ready"]
    fake = FakeClassifier(fail={2})
    first = list(assess(selected, fake, cache, workers=1))
    assert fake.calls == 4
    assert first[1]["status"] == "api_error"
    assert "secret" not in json.dumps(first)
    second = list(assess(selected, fake, cache, workers=1))
    assert fake.calls == 5
    assert sum(r["cached"] for r in second) == 3
    third = list(assess(selected, fake, cache, workers=2))
    assert all(r["cached"] for r in third)
    changed = deepcopy(selected[:1])
    changed[0]["claim"]["selected_evidence"]["snippet"] += " In adults only."
    (changed_result,) = assess(changed, fake, cache, workers=1)
    assert not changed_result["cached"]
    assert fake.calls == 6
    tasks = tasks_for(selected[0]["claim"])
    assert cache_key("other-model", tasks) != cache_key(fake.model, tasks)
    list(assess(selected[:1], fake, cache, workers=1, refresh=True))
    assert fake.calls == 7
    cache.close()


def test_report_counts_unique_assertions_not_snippets_or_aspects(tmp_path):
    cache = ResultCache(tmp_path / "cache.sqlite")
    result = list(assess(rows(tmp_path), FakeClassifier(), cache, workers=1))
    with (tmp_path / "results.jsonl").open("w") as stream:
        for row in result:
            stream.write(json.dumps(row) + "\n")
    totals = write_reports(tmp_path)
    assert totals["pairs"] == 7
    assert totals["assessed_pairs"] == 4
    assert totals["mismatch_assertions"] == 1
    entry = next(iter(csv.DictReader((tmp_path / "entries.csv").open())))
    assert entry["mismatch_aspects"] == "2"
    assert entry["mismatch_assertions"] == "1"
    assert entry["root_partial"] == "4"
    assert entry["no_evidence"] == "2"
    detail = list(csv.DictReader((tmp_path / "aspects.csv").open()))
    assert all(not r["label"] for r in detail if r["status"] != "assessed")
    assert any(
        r["aspect_path"] == "/assertion/frequency" and r["label"] == "MISMATCH"
        for r in detail
    )
    cache.close()


def test_dry_run_needs_no_key_and_writes_no_cache(tmp_path, monkeypatch):
    file = tmp_path / "data.yaml"
    file.write_text(yaml.safe_dump(disease()))
    monkeypatch.delenv("TYPESAFE_API_KEY", raising=False)
    output = tmp_path / "output"
    cache = tmp_path / "no.sqlite"
    result = CliRunner().invoke(
        main,
        [
            "--input",
            str(file),
            "--output",
            str(output),
            "--cache",
            str(cache),
            "--dry-run",
            "--section",
            "phenotypes",
            "--limit",
            "2",
        ],
    )
    assert result.exit_code == 0, result.output
    assert not cache.exists()
    manifest = json.loads((output / "manifest.json").read_text())
    assert manifest["pairs"] == 2
    assert manifest["assessed_pairs"] == 0
    assert manifest["complete"]


def test_auth_failure_stops_paid_requests_without_dropping_inventory(tmp_path):
    class Unauthorized(FakeClassifier):
        def classify_many(self, tasks):
            self.calls += 1
            response = httpx.Response(
                401, request=httpx.Request("POST", "https://api.example")
            )
            raise httpx.HTTPStatusError(
                "hidden", request=response.request, response=response
            )

    cache = ResultCache(tmp_path / "cache.sqlite")
    fake = Unauthorized()
    result = list(assess(rows(tmp_path), fake, cache, workers=1))
    assert len(result) == 7
    assert fake.calls == 1
    assert sum(r["status"] == "not_assessed" for r in result) == 3
    cache.close()


def test_time_budget_preserves_cached_results_and_reports_unassessed(
    tmp_path, monkeypatch
):
    cache = ResultCache(tmp_path / "cache.sqlite")
    selected = [r for r in rows(tmp_path) if r["status"] == "ready"]
    fake = FakeClassifier()
    list(assess(selected[:1], fake, cache, workers=1))
    times = iter([0, 2, 2, 2, 2])
    monkeypatch.setattr(time, "monotonic", lambda: next(times))
    result = list(assess(selected, fake, cache, workers=1, max_seconds=1))
    assert result[0]["cached"]
    assert fake.calls == 1
    assert sum(r["status"] == "not_assessed" for r in result) == 3
    cache.close()


def test_merge_rejects_mixed_settings_and_marks_missing_shards(tmp_path):
    source = tmp_path / "shards"
    shard = source / "zero"
    shard.mkdir(parents=True)
    manifest = {
        "model": "jev-test",
        "source_revision": "abc",
        "schema_sha256": "s",
        "classifier_sha256": "c",
        "shard_count": 2,
        "shard_index": 0,
        "sections": [],
        "inputs": ["kb/disorders"],
        "limit": 0,
        "dry_run": False,
        "prompt": {},
        "criteria": {},
        "complete": True,
    }
    (shard / "manifest.json").write_text(json.dumps(manifest))
    (shard / "results.jsonl").write_text("")
    output = tmp_path / "combined"
    assert not merge_shards(output, source, 2)
    assert "INCOMPLETE RUN" in (output / "summary.md").read_text()
    other = source / "one"
    other.mkdir()
    (other / "manifest.json").write_text(
        json.dumps(manifest | {"shard_index": 1, "model": "other"})
    )
    (other / "results.jsonl").write_text("")
    with pytest.raises(Exception, match="different sources or inference settings"):
        merge_shards(output, source, 2)
    (other / "manifest.json").write_text(json.dumps(manifest | {"shard_index": 1}))
    assert merge_shards(output, source, 2)


def test_type_safe_rounded_probability_response():
    claim = extract_claim(disease(), "/phenotypes/0/evidence/0")
    tasks = tasks_for(claim)

    def handle(request):
        payload = json.loads(request.content)
        return httpx.Response(
            200,
            json={
                "model": "jev-test",
                "usage": {"input_tokens": 2, "output_tokens": 1},
                "answers": {
                    k: {
                        "type": "choice",
                        "choice": "MATCH",
                        "probabilities": {
                            "MATCH": 0.5,
                            "MISMATCH": 0.25,
                            "PARTIAL": 0.26,
                        },
                        "confidence": 0.1,
                    }
                    for k in payload["questions"]
                },
            },
        )

    classifier = TypeSafeClassifier(
        api_key="test", transport=httpx.MockTransport(handle)
    )
    result = classifier.classify_many(tasks)
    assert all(a.label == "MATCH" for a in result.answers.values())
    assert all(a.probabilities["PARTIAL"] == 0.26 for a in result.answers.values())
    assert asdict(result)["usage"]["input_tokens"] == 2


@pytest.mark.parametrize("failure", [429, 529, 503, "timeout"])
def test_transport_retries_transient_failures(failure, monkeypatch):
    from dismech.classifier import typesafe

    monkeypatch.setattr(typesafe.time, "sleep", lambda seconds: None)
    tasks = tasks_for(extract_claim(disease(), "/phenotypes/0/evidence/0"))
    calls = []

    def handle(request):
        calls.append(request)
        if len(calls) == 1:
            if failure == "timeout":
                raise httpx.ReadTimeout("transient", request=request)
            return httpx.Response(failure)
        return httpx.Response(
            200,
            json={
                "model": "jev-test",
                "usage": {},
                "answers": {
                    t.name: {
                        "type": "choice",
                        "choice": "MATCH",
                        "probabilities": {"MATCH": 1, "MISMATCH": 0, "PARTIAL": 0},
                        "confidence": 1,
                    }
                    for t in tasks
                },
            },
        )

    classifier = TypeSafeClassifier(
        api_key="test", transport=httpx.MockTransport(handle)
    )
    assert len(classifier.classify_many(tasks).answers) == len(tasks)
    assert len(calls) == 2


def test_time_limited_cli_and_merged_report_are_incomplete(tmp_path, monkeypatch):
    from dismech.classifier import audit

    source = tmp_path / "shards"
    output = source / "zero"
    file = tmp_path / "data.yaml"
    file.write_text(yaml.safe_dump(disease()))
    fake = FakeClassifier()
    monkeypatch.setattr(audit, "TypeSafeClassifier", lambda model: fake)
    ticks = iter([0, 2])
    monkeypatch.setattr(audit.time, "monotonic", lambda: next(ticks, 2))
    result = CliRunner().invoke(
        main,
        [
            "--input",
            str(file),
            "--output",
            str(output),
            "--cache",
            str(tmp_path / "cache.sqlite"),
            "--max-seconds",
            "1",
        ],
    )
    assert result.exit_code == 1, result.output
    assert fake.calls == 0
    manifest = json.loads((output / "manifest.json").read_text())
    assert manifest["pairs"] == 7
    assert manifest["errors"] == 4
    assert not manifest["complete"]
    assert "INCOMPLETE RUN" in (output / "summary.md").read_text()
    assert not merge_shards(tmp_path / "combined", source, 1)
    combined = json.loads((tmp_path / "combined" / "manifest.json").read_text())
    assert not combined["complete"]
    assert "INCOMPLETE RUN" in (tmp_path / "combined" / "summary.md").read_text()
