"""Tests for standalone dismech history records."""

import importlib.util
import sys
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
NEW_HISTORY_SCRIPT = ROOT_DIR / "scripts" / "new_history.py"
KIND_DIRS = {
    "disorder": "disorders",
    "module": "modules",
    "comorbidity": "comorbidities",
    "schema": "schema",
}


def _load_new_history_module():
    spec = importlib.util.spec_from_file_location("new_history", NEW_HISTORY_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


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


def test_history_actor_preserves_agent_tool_metadata(schema_view):
    induced = schema_view.class_induced_slots("HistoryActor")
    slots = {slot.name: slot for slot in induced}

    assert "model" in slots
    assert "agent_tool" in slots
    assert "agent_version" in slots


def test_history_event_types_include_general_not_migration(schema_view):
    enum = schema_view.get_enum("HistoryEventTypeEnum")

    assert "GENERAL" in enum.permissible_values
    assert "MIGRATION" not in enum.permissible_values


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
                    "agent_tool": "codex",
                    "agent_version": "1.0",
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


@pytest.mark.parametrize(
    "argv, expected_parent, expected_stem_contains",
    [
        (
            [
                "--kind", "disorder", "--slug", "Asthma",
                "--event", "CREATE", "--outcome", "changed",
                "--summary", "Create: Asthma",
                "--agent-tool", "claude-code", "--model", "claude-opus-4-8",
                "--sections", "phenotypes,evidence",
                "--pr", "5123", "--issue", "2892",
                "--details", "Scaffolder smoke test.",
            ],
            "history/disorders/Asthma",
            "claude-code",
        ),
        (
            [
                "--kind", "module", "--slug", "fibrotic_response",
                "--event", "EDIT", "--outcome", "changed",
                "--summary", "Edit: fibrotic_response",
                "--actor-name", "cjm", "--actor-type", "human",
                "--details", "x",
            ],
            "history/modules/fibrotic_response",
            "cjm",
        ),
    ],
)
def test_new_history_scaffolder_emits_valid_record(
    validator, argv, expected_parent, expected_stem_contains
):
    module = _load_new_history_module()
    args = module.parse_args(argv)
    record, out_path = module.build_record(args)

    # Path layout matches the committed convention.
    assert out_path.parent.as_posix().endswith(expected_parent)
    assert expected_stem_contains in out_path.stem
    assert out_path.stem == record["session"]["id"]

    # Bare issue/PR numbers are expanded to full repo URLs.
    for url in record["links"]["issues"] + record["links"]["prs"]:
        assert url.startswith("https://github.com/monarch-initiative/dismech/")

    report = validator.validate(record, target_class="HistoryRecord")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Scaffolded record failed validation: {[str(e) for e in errors]}"


def test_new_history_scaffolder_requires_slug_for_kb_kinds():
    module = _load_new_history_module()
    args = module.parse_args(
        ["--kind", "disorder", "--event", "EDIT", "--outcome", "changed",
         "--summary", "x", "--details", "y"]
    )
    with pytest.raises(SystemExit):
        module.build_record(args)


def test_committed_history_records_do_not_use_migration_event():
    history_files = sorted(HISTORY_DIR.glob("**/*.yaml"))
    assert history_files

    assert not list(HISTORY_DIR.glob("**/*legacy-import*.yaml"))
    for path in history_files:
        record = yaml.safe_load(path.read_text())
        for event in record["events"]:
            assert event["type"] != "MIGRATION"
