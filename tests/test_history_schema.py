"""Tests for standalone dismech history records."""

from pathlib import Path

import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

ROOT_DIR = Path(__file__).parent.parent
HISTORY_SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "history.yaml"
HISTORY_DIR = ROOT_DIR / "history"
KB_DISORDERS_DIR = ROOT_DIR / "kb" / "disorders"
KIND_DIRS = {
    "disorder": "disorders",
    "module": "modules",
    "comorbidity": "comorbidities",
    "schema": "schema",
}


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(HISTORY_SCHEMA_PATH))


@pytest.fixture(scope="module")
def validator() -> Validator:
    return Validator(
        HISTORY_SCHEMA_PATH,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def test_history_record_has_multivalued_actors(schema_view):
    induced = schema_view.class_induced_slots("HistorySession")
    slots = {slot.name: slot for slot in induced}

    assert "actors" in slots
    assert slots["actors"].multivalued is True
    assert slots["actors"].range == "HistoryActor"
    assert slots["actors"].minimum_cardinality == 1


def test_history_record_requires_details(schema_view):
    induced = schema_view.class_induced_slots("HistoryEvent")
    slots = {slot.name: slot for slot in induced}

    assert "details" in slots
    assert slots["details"].required is True


def test_history_record_validates_multiple_actors(validator):
    record = {
        "history_version": 1,
        "target": {
            "kind": "disorder",
            "slug": "Asthma",
            "path": "kb/disorders/Asthma.yaml",
        },
        "session": {
            "id": "2026-05-31T174412Z-codex-a3f9c2",
            "timestamp": "2026-05-31T17:44:12Z",
            "actors": [
                {
                    "type": "ai_agent",
                    "name": "codex",
                    "model": "gpt-5",
                },
                {
                    "type": "human",
                    "name": "cjm",
                },
            ],
        },
        "links": {
            "issues": ["https://github.com/monarch-initiative/dismech/issues/2892"],
            "prs": ["https://github.com/monarch-initiative/dismech/pull/3151"],
            "urls": [],
        },
        "events": [
            {
                "type": "REVIEW",
                "outcome": "no_change",
                "sections": ["phenotypes", "evidence"],
                "summary": "Reviewed evidence quality and found no immediate edits needed.",
                "details": "The review found no required changes.",
            }
        ],
    }

    report = validator.validate(record, target_class="HistoryRecord")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Unexpected validation errors: {[str(e) for e in errors]}"


def test_invalid_history_event_type_rejected(validator):
    record = {
        "history_version": 1,
        "target": {
            "kind": "disorder",
            "slug": "Asthma",
            "path": "kb/disorders/Asthma.yaml",
        },
        "session": {
            "id": "2026-05-31T174412Z-codex-a3f9c2",
            "timestamp": "2026-05-31T17:44:12Z",
            "actors": [{"type": "ai_agent", "name": "codex"}],
        },
        "events": [
            {
                "type": "TOTALLY_MADE_UP",
                "outcome": "no_change",
                "summary": "Invalid event type should fail validation.",
                "details": "This deliberately uses an invalid event type.",
            }
        ],
    }

    report = validator.validate(record, target_class="HistoryRecord")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert errors, "Expected validation error for invalid history event type"


def test_no_legacy_kb_history_files():
    assert not list(KB_DISORDERS_DIR.glob("*.history.yaml"))


def test_committed_history_records_validate(validator):
    history_files = sorted(HISTORY_DIR.glob("**/*.yaml"))
    assert history_files

    errors = []
    for path in history_files:
        report = validator.validate(
            yaml.safe_load(path.read_text()), target_class="HistoryRecord"
        )
        errors.extend(
            f"{path.relative_to(ROOT_DIR)}: {result.message}"
            for result in report.results
            if result.severity.name == "ERROR"
        )

    assert not errors


def test_committed_history_records_follow_layout():
    history_files = sorted(HISTORY_DIR.glob("**/*.yaml"))
    assert history_files

    for path in history_files:
        record = yaml.safe_load(path.read_text())
        target = record["target"]
        kind = target["kind"]
        slug = target["slug"]
        target_path = ROOT_DIR / target["path"]

        assert target_path.exists(), (
            f"{path.relative_to(ROOT_DIR)} target does not exist"
        )
        if kind in KIND_DIRS:
            expected_parent = HISTORY_DIR / KIND_DIRS[kind] / slug
            assert path.parent == expected_parent
