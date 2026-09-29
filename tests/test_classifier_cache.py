"""Paid judgments survive changes, partial runs, merges and claim reactivation."""

import json
from copy import deepcopy

import pytest
import yaml
from click.testing import CliRunner

from dismech.classifier.audit import assess, inventory
from dismech.classifier.audit import main as audit_main
from dismech.classifier.cache import BENCHMARK, ResultCache, main
from tests.test_classifier_audit import FakeClassifier, disease


@pytest.fixture(autouse=True)
def isolate_cache_environment(monkeypatch):
    import os

    monkeypatch.setenv("DISMECH_KB_CACHE", os.environ.get("DISMECH_KB_CACHE", "1"))


def setup(tmp_path):
    file = tmp_path / "Example.yaml"
    file.write_text(yaml.safe_dump(disease()))
    root = tmp_path / "cache"
    cache = ResultCache(root)
    rows = [r for r in inventory([file]) if r["status"] == "ready"]
    return file, root, cache, rows


def document(root):
    return yaml.safe_load((root / "Example" / f"{BENCHMARK}.yaml").read_text())


def test_punctuation_history_reactivation_and_unchanged_bytes(tmp_path):
    file, root, cache, rows = setup(tmp_path)
    fake = FakeClassifier()
    original = list(assess(rows, fake, cache, 1, revision="first-revision"))
    cache.reconcile([file], "first-revision")
    before = document(root)
    old_key = original[0]["cache_key"]
    identity = before["assessments"][old_key]["input_sha256"]
    old_claim = deepcopy(before["inputs"][identity]["claim"])
    old_scores = deepcopy(before["assessments"][old_key]["result"])
    initial_calls = fake.calls
    path = root / "Example" / f"{BENCHMARK}.yaml"
    raw = path.read_bytes()
    cache.reconcile([file], "unrelated-revision")
    assert path.read_bytes() == raw
    # A single punctuation change invalidates precisely the affected input.
    data = disease()
    data["pathophysiology"][0]["evidence"][0]["snippet"] += "!"
    file.write_text(yaml.safe_dump(data))
    cache.reconcile([file], "edit-revision")
    changed = list(assess(inventory([file]), fake, cache, 2, revision="edit-revision"))
    cache.reconcile([file], "edit-revision")
    assert fake.calls == initial_calls + 1
    after = document(root)
    retired = after["inputs"][identity]
    assert not retired["active"]
    assert retired["claim"] == old_claim
    assert after["assessments"][old_key]["result"] == old_scores
    assert retired["first_seen_revision"] == "first-revision"
    assert retired["activity_history"][-1]["source_revision"] == "edit-revision"
    assert sum(r["active"] for r in after["inputs"].values()) == initial_calls
    assert sum(r.get("cached", False) for r in changed) == initial_calls - 1
    # Restoring the original wording reuses its original judgment.
    file.write_text(yaml.safe_dump(disease()))
    cache.reconcile([file], "restore-revision")
    restored = list(assess(inventory([file]), fake, cache, 2))
    assert fake.calls == initial_calls + 1
    assert all(r["cached"] for r in restored if r["status"] == "assessed")
    assert document(root)["inputs"][identity]["active"]
    assert [
        h["active"] for h in document(root)["inputs"][identity]["activity_history"]
    ] == [False, True]


def test_filter_and_limit_never_retire_unselected_claims(tmp_path, monkeypatch):
    file, root, cache, rows = setup(tmp_path)
    fake = FakeClassifier()
    list(assess(rows, fake, cache, 1))
    cache.close()
    monkeypatch.setattr(
        "dismech.classifier.audit.TypeSafeClassifier", lambda model: fake
    )
    result = CliRunner().invoke(
        audit_main,
        [
            "--input",
            str(file),
            "--cache",
            str(root),
            "--output",
            str(tmp_path / "report"),
            "--section",
            "phenotypes",
            "--limit",
            "1",
        ],
    )
    assert result.exit_code == 0, result.output
    assert all(r["active"] for r in document(root)["inputs"].values())
    assert fake.calls == len(rows)


def test_model_change_does_not_retire_claim_and_refresh_preserves_response(tmp_path):
    file, root, cache, rows = setup(tmp_path)
    fake = FakeClassifier()
    (first,) = assess(rows[:1], fake, cache, 1)
    fake.model = "jev-next"
    (second,) = assess(rows[:1], fake, cache, 1)
    cache.reconcile([file])
    records = document(root)["assessments"]
    assert len(records) == 2
    inputs = document(root)["inputs"]
    assert len(inputs) == 1 and all(r["active"] for r in inputs.values())
    assert all("claim" not in r and "model_input" not in r for r in records.values())
    assert len({r["input_sha256"] for r in records.values()}) == 1
    assert len({r["configuration_sha256"] for r in records.values()}) == 2
    (refreshed,) = assess(rows[:1], fake, cache, 1, refresh=True)
    records = document(root)["assessments"]
    original = records[second["cache_key"]]
    assert original["assessed_at"] == second["assessed_at"]
    assert original["reassessments"][0]["assessed_at"] == refreshed["assessed_at"]
    assert records[first["cache_key"]]["model"] == "jev-test"
    (again,) = assess(rows[:1], fake, cache, 1)
    assert again["assessed_at"] == refreshed["assessed_at"]
    assert fake.calls == 3


def test_removed_claim_missing_source_and_invalid_source(tmp_path):
    file, root, cache, rows = setup(tmp_path)
    list(assess(rows, FakeClassifier(), cache, 1))
    cache.reconcile([file])
    file.write_text("name: Example\nphenotypes: [")
    cache.reconcile([file])
    assert not document(root)["inventory"]["complete"]
    assert all(r["active"] for r in document(root)["inputs"].values())
    file.write_text("name: Example\n")
    cache.reconcile([file])
    assert not any(r["active"] for r in document(root)["inputs"].values())
    file.write_text(yaml.safe_dump(disease()))
    cache.reconcile([file])
    file.unlink()
    cache.reconcile()
    assert not any(r["active"] for r in document(root)["inputs"].values())
    assert not document(root)["inventory"]["source_exists"]


def test_duplicate_requests_are_paid_once_even_during_refresh(tmp_path):
    _, root, cache, rows = setup(tmp_path)
    fake = FakeClassifier()
    repeated = [rows[0]] * 8
    outcomes = list(assess(repeated, fake, cache, 4))
    assert fake.calls == 1
    assert len(outcomes) == 8
    assert sum(not r["cached"] for r in outcomes) == 1
    outcomes = list(assess(repeated, fake, cache, 4, refresh=True))
    assert fake.calls == 2
    assert len(document(root)["assessments"]) == 1


def test_merge_preserves_both_histories_and_is_idempotent(tmp_path):
    file, root, cache, rows = setup(tmp_path)
    list(assess(rows[:2], FakeClassifier(), cache, 1))
    cache.reconcile([file])
    other_root = tmp_path / "other"
    other = ResultCache(other_root)
    list(assess(rows[1:], FakeClassifier(), other, 1))
    other.reconcile([file])
    cache.merge(other_root)
    cache.reconcile([file])
    path = root / "Example" / f"{BENCHMARK}.yaml"
    first = path.read_bytes()
    assert len(document(root)["assessments"]) == len(rows)
    assert (
        sum(
            len(r.get("reassessments", []))
            for r in document(root)["assessments"].values()
        )
        == 1
    )
    cache.merge(other_root)
    cache.reconcile([file])
    assert path.read_bytes() == first
    fake = FakeClassifier()
    assert all(r["cached"] for r in assess(rows, fake, cache, 1))
    assert fake.calls == 0


def test_corrupt_cache_aborts_before_paid_requests(tmp_path, monkeypatch):
    file, root, cache, rows = setup(tmp_path)
    list(assess(rows[:1], FakeClassifier(), cache, 1))
    path = root / "Example" / f"{BENCHMARK}.yaml"
    path.write_text(path.read_text() + "format_version: 123\n")
    fake = FakeClassifier()
    monkeypatch.setattr(
        "dismech.classifier.audit.TypeSafeClassifier", lambda model: fake
    )
    result = CliRunner().invoke(
        audit_main,
        [
            "--input",
            str(file),
            "--cache",
            str(root),
            "--output",
            str(tmp_path / "reports"),
        ],
    )
    assert result.exit_code != 0
    assert fake.calls == 0
    assert path.read_text().endswith("format_version: 123\n")


def test_import_reuses_paid_results_with_original_timestamp(tmp_path):
    file, _root, cache, rows = setup(tmp_path)
    outcomes = list(assess(rows, FakeClassifier(), cache, 1))
    report = tmp_path / "results.jsonl"
    report.write_text("".join(json.dumps(r) + "\n" for r in outcomes))
    (tmp_path / "manifest.json").write_text(json.dumps({"source_revision": "original"}))
    destination = tmp_path / "imported"
    result = CliRunner().invoke(
        main, ["--cache", str(destination), "--import-results", str(report)]
    )
    assert result.exit_code == 0, result.output
    imported = ResultCache(destination)
    fake = FakeClassifier()
    replay = list(assess(inventory([file]), fake, imported, 1))
    assert fake.calls == 0
    assert {r["assessed_at"] for r in replay if r["status"] == "assessed"} == {
        r["assessed_at"] for r in outcomes
    }
    assert all(
        r["first_seen_revision"] == "original"
        for r in document(destination)["inputs"].values()
    )


def test_extraction_changes_advance_observation_without_rebuying_scores(tmp_path):
    file, root, cache, rows = setup(tmp_path)
    list(assess(rows[:1], FakeClassifier(), cache, 1))
    cache.reconcile([file], "first")
    before = document(root)
    cache.extraction_sha256 = "new-extractor"
    cache.reconcile([file], "second")
    after = document(root)
    assert after["inventory"]["observed_at"] != before["inventory"]["observed_at"]
    assert after["inventory"]["source_revision"] == "second"
    for key, record in before["assessments"].items():
        assert after["assessments"][key]["result"] == record["result"]
        assert after["assessments"][key]["assessed_at"] == record["assessed_at"]


def test_v1_migration_keeps_scores_and_one_input_across_models(tmp_path):
    file, root, cache, rows = setup(tmp_path)
    fake = FakeClassifier()
    list(assess(rows[:1], fake, cache, 1))
    fake.model = "jev-next"
    list(assess(rows[:1], fake, cache, 1))
    cache.reconcile([file])
    before = document(root)
    legacy = deepcopy(before)
    for key, record in legacy["assessments"].items():
        item = legacy["inputs"][record["input_sha256"]]
        record.update(
            {
                k: v
                for k, v in item.items()
                if k not in {"origin", "evidence_metadata", "active_as_of"}
            }
        )
        record["claim"] = deepcopy(rows[0]["claim"])
        record["model_input"] = deepcopy(item["claim"])
        record["assessment_sha256"] = key
    del legacy["inputs"]
    legacy["format_version"] = 1
    path = root / "Example" / f"{BENCHMARK}.yaml"
    path.write_text(yaml.safe_dump(legacy))
    cache.close()
    cache = ResultCache(root)
    cache.reconcile([file])
    migrated = document(root)
    assert migrated["format_version"] == 2
    assert len(migrated["inputs"]) == 1
    assert migrated["assessments"] == before["assessments"]
    fake.calls = 0
    assert all(r["cached"] for r in assess(rows[:1], fake, cache, 1))
    assert fake.calls == 0
