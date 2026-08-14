"""Tests for standalone dismech history records."""

import importlib.util
import sys
from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

from dismech.yaml_io import safe_load_path

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
            safe_load_path(path), target_class="HistoryRecord"
        )
        errors.extend(
            f"{path.relative_to(ROOT_DIR)}: {result.message}"
            for result in report.results
            if result.severity.name == "ERROR"
        )

    assert not errors


def _layout_errors(record: dict, path: Path) -> list[str]:
    """Check one history record's target against the on-disk repository layout.

    History records are append-only, so a record whose target was later renamed
    keeps its original ``slug``/``path``. Such a record documents the move with
    ``target.superseded_by``; the successor is then what must exist on disk, and
    the record files live under the successor's slug directory. Without
    ``superseded_by``, a missing target is an ordinary error and still fails.
    """
    rel = path.relative_to(ROOT_DIR)
    target = record["target"]
    kind = target["kind"]
    slug = target["slug"]
    superseded_by = target.get("superseded_by")
    errors = []

    if superseded_by:
        successor_slug = superseded_by.get("slug")
        successor_rel = superseded_by.get("path")
        if not successor_slug or not successor_rel:
            return [f"{rel} target.superseded_by needs both a slug and a path"]
        if not (ROOT_DIR / successor_rel).exists():
            errors.append(
                f"{rel} target.superseded_by path does not exist: {successor_rel}"
            )
        if Path(successor_rel).stem != successor_slug:
            errors.append(
                f"{rel} target.superseded_by slug '{successor_slug}' does not match "
                f"the stem of its path '{successor_rel}'"
            )
        slug = successor_slug
    elif not (ROOT_DIR / target["path"]).exists():
        errors.append(f"{rel} target does not exist")

    if kind in KIND_DIRS:
        expected_parent = HISTORY_DIR / KIND_DIRS[kind] / slug
        if path.parent != expected_parent:
            errors.append(f"{rel} should live under {expected_parent.relative_to(ROOT_DIR)}")

    return errors


def test_committed_history_records_follow_layout():
    history_files = sorted(HISTORY_DIR.glob("**/*.yaml"))
    assert history_files

    errors = []
    for path in history_files:
        errors.extend(_layout_errors(safe_load_path(path), path))

    assert not errors, "\n".join(errors)


def _supersession_record(successor_path: str, successor_slug: str | None = None) -> dict:
    """Record whose target was renamed. The successor slug defaults to the path
    stem so each negative test below has a single cause; only the slug/stem
    mismatch test overrides it."""
    return {
        "target": {
            "kind": "disorder",
            "slug": "Old_Name",
            "path": "kb/disorders/Old_Name.yaml",
            "superseded_by": {
                "slug": successor_slug or Path(successor_path).stem,
                "path": successor_path,
            },
        }
    }


def test_layout_accepts_renamed_target_with_superseded_by():
    record = _supersession_record("kb/disorders/Asthma.yaml")
    path = HISTORY_DIR / "disorders" / "Asthma" / "2026-08-02T020640Z-codex-abc123.yaml"

    assert _layout_errors(record, path) == []


def test_layout_rejects_superseded_by_pointing_at_missing_target():
    record = _supersession_record("kb/disorders/Does_Not_Exist.yaml")
    path = (
        HISTORY_DIR / "disorders" / "Does_Not_Exist"
        / "2026-08-02T020640Z-codex-abc123.yaml"
    )

    errors = _layout_errors(record, path)
    assert len(errors) == 1, f"expected a single cause, got: {errors}"
    assert "superseded_by path does not exist" in errors[0]


def test_layout_rejects_missing_target_without_superseded_by():
    record = {
        "target": {
            "kind": "disorder",
            "slug": "Does_Not_Exist",
            "path": "kb/disorders/Does_Not_Exist.yaml",
        }
    }
    path = (
        HISTORY_DIR / "disorders" / "Does_Not_Exist"
        / "2026-08-02T020640Z-codex-abc123.yaml"
    )

    errors = _layout_errors(record, path)
    assert len(errors) == 1, f"expected a single cause, got: {errors}"
    assert "target does not exist" in errors[0]


def test_layout_rejects_superseded_by_slug_path_mismatch():
    record = _supersession_record(
        "kb/disorders/Marfan_Syndrome.yaml", successor_slug="Asthma"
    )
    path = HISTORY_DIR / "disorders" / "Asthma" / "2026-08-02T020640Z-codex-abc123.yaml"

    errors = _layout_errors(record, path)
    assert len(errors) == 1, f"expected a single cause, got: {errors}"
    assert "does not match the stem of its path" in errors[0]


def test_layout_rejects_incomplete_superseded_by_block():
    record = {
        "target": {
            "kind": "disorder",
            "slug": "Old_Name",
            "path": "kb/disorders/Old_Name.yaml",
            "superseded_by": {"reason": "no slug or path"},
        }
    }
    path = HISTORY_DIR / "disorders" / "Asthma" / "2026-08-02T020640Z-codex-abc123.yaml"

    errors = _layout_errors(record, path)
    assert any("needs both a slug and a path" in error for error in errors)


def test_layout_requires_record_directory_to_follow_successor_slug():
    record = _supersession_record("kb/disorders/Asthma.yaml")
    path = HISTORY_DIR / "disorders" / "Old_Name" / "2026-08-02T020640Z-codex-abc123.yaml"

    errors = _layout_errors(record, path)
    assert any("should live under" in error for error in errors)


def test_history_record_with_superseded_by_validates(validator):
    record = {
        "history_version": 1,
        "target": {
            "kind": "disorder",
            "slug": "Old_Name",
            "path": "kb/disorders/Old_Name.yaml",
            "superseded_by": {
                "slug": "Asthma",
                "path": "kb/disorders/Asthma.yaml",
                "reason": "Retargeted mid-curation; the old name is not an independent entity.",
            },
        },
        "session": {
            "id": "2026-05-31T174412Z-codex-a3f9c2",
            "timestamp": "2026-05-31T17:44:12Z",
            "actors": [{"type": "ai_agent", "name": "codex"}],
        },
        "events": [
            {
                "type": "CREATE",
                "outcome": "changed",
                "summary": "Create: Old Name",
                "details": "Created under the pre-rename slug.",
            }
        ],
    }

    report = validator.validate(record, target_class="HistoryRecord")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Unexpected validation errors: {[str(e) for e in errors]}"


def test_superseded_by_requires_slug_and_path(validator):
    record = {
        "history_version": 1,
        "target": {
            "kind": "disorder",
            "slug": "Old_Name",
            "path": "kb/disorders/Old_Name.yaml",
            "superseded_by": {"reason": "missing slug and path"},
        },
        "session": {
            "id": "2026-05-31T174412Z-codex-a3f9c2",
            "timestamp": "2026-05-31T17:44:12Z",
            "actors": [{"type": "ai_agent", "name": "codex"}],
        },
        "events": [
            {
                "type": "CREATE",
                "outcome": "changed",
                "summary": "Create: Old Name",
                "details": "Created under the pre-rename slug.",
            }
        ],
    }

    report = validator.validate(record, target_class="HistoryRecord")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert errors, "Expected validation error for superseded_by without slug/path"


def test_superseded_by_requires_reason(validator):
    """The escape hatch must carry its own justification, visible in review."""
    record = {
        "history_version": 1,
        "target": {
            "kind": "disorder",
            "slug": "Old_Name",
            "path": "kb/disorders/Old_Name.yaml",
            "superseded_by": {
                "slug": "Asthma",
                "path": "kb/disorders/Asthma.yaml",
            },
        },
        "session": {
            "id": "2026-05-31T174412Z-codex-a3f9c2",
            "timestamp": "2026-05-31T17:44:12Z",
            "actors": [{"type": "ai_agent", "name": "codex"}],
        },
        "events": [
            {
                "type": "CREATE",
                "outcome": "changed",
                "summary": "Create: Old Name",
                "details": "Created under the pre-rename slug.",
            }
        ],
    }

    report = validator.validate(record, target_class="HistoryRecord")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert errors, "Expected validation error for superseded_by without a reason"


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


def test_new_history_scaffolder_warns_on_missing_target():
    module = _load_new_history_module()

    existing = KB_DISORDERS_DIR / "Asthma.yaml"
    assert module.target_missing_warning(str(existing)) is None

    warning = module.target_missing_warning(str(KB_DISORDERS_DIR / "Does_Not_Exist.yaml"))
    assert warning is not None
    assert "does not exist yet" in warning


def test_committed_history_records_do_not_use_migration_event():
    history_files = sorted(HISTORY_DIR.glob("**/*.yaml"))
    assert history_files

    assert not list(HISTORY_DIR.glob("**/*legacy-import*.yaml"))
    for path in history_files:
        record = safe_load_path(path)
        for event in record["events"]:
            assert event["type"] != "MIGRATION"
