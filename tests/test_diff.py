"""Tests for the semantic YAML diff tool."""

import glob
from datetime import date, datetime
from pathlib import Path

import pytest
import yaml

from dismech.diff import (
    DiffEntry,
    FileDiffResult,
    _find_key_field,
    _normalize_value,
    diff_dicts,
    diff_lists,
)

ROOT_DIR = Path(__file__).parent.parent
KB_DIR = ROOT_DIR / "kb" / "disorders"


# --- _find_key_field ---


class TestFindKeyField:
    def test_name_key(self):
        items = [{"name": "a", "x": 1}, {"name": "b", "x": 2}]
        assert _find_key_field(items) == "name"

    def test_id_key(self):
        items = [{"id": "HP:001", "label": "x"}, {"id": "HP:002", "label": "y"}]
        assert _find_key_field(items) == "id"

    def test_reference_key(self):
        items = [{"reference": "PMID:1"}, {"reference": "PMID:2"}]
        assert _find_key_field(items) == "reference"

    def test_non_unique_returns_none(self):
        items = [{"name": "a"}, {"name": "a"}]
        assert _find_key_field(items) is None

    def test_empty_list(self):
        assert _find_key_field([]) is None

    def test_mixed_types_no_common_key(self):
        items = [{"id": "x"}, {"name": "y"}]
        assert _find_key_field(items) is None

    def test_non_dict_items(self):
        items = [1, 2, 3]
        assert _find_key_field(items) is None

    def test_prefers_name_over_id(self):
        """name comes before id in KEY_CANDIDATES."""
        items = [
            {"name": "a", "id": "1"},
            {"name": "b", "id": "2"},
        ]
        assert _find_key_field(items) == "name"

    def test_falls_through_to_id(self):
        """If name is not unique, tries id."""
        items = [
            {"name": "a", "id": "1"},
            {"name": "a", "id": "2"},
        ]
        assert _find_key_field(items) == "id"


# --- _normalize_value ---


class TestNormalizeValue:
    def test_datetime(self):
        assert (
            _normalize_value(datetime(2025, 1, 15, 10, 30, 0)) == "2025-01-15T10:30:00"
        )

    def test_date(self):
        assert _normalize_value(date(2025, 1, 15)) == "2025-01-15"

    def test_string_strips_whitespace(self):
        assert _normalize_value("  hello  ") == "hello"

    def test_preserves_internal_whitespace(self):
        assert _normalize_value("  hello  world  ") == "hello  world"

    def test_int_passthrough(self):
        assert _normalize_value(42) == 42

    def test_none_passthrough(self):
        assert _normalize_value(None) is None

    def test_list_passthrough(self):
        assert _normalize_value([1, 2]) == [1, 2]

    def test_dict_passthrough(self):
        assert _normalize_value({"a": 1}) == {"a": 1}


# --- diff_dicts ---


class TestDiffDicts:
    def test_identical(self):
        d = {"a": 1, "b": "hello"}
        assert diff_dicts(d, d) == []

    def test_scalar_change(self):
        result = diff_dicts({"a": 1}, {"a": 2})
        assert len(result) == 1
        assert result[0].path == "a"
        assert result[0].change_type == "changed"
        assert result[0].old_value == 1
        assert result[0].new_value == 2

    def test_field_added(self):
        result = diff_dicts({}, {"b": 3})
        assert len(result) == 1
        assert result[0].change_type == "added"
        assert result[0].new_value == 3

    def test_field_removed(self):
        result = diff_dicts({"b": 3}, {})
        assert len(result) == 1
        assert result[0].change_type == "removed"
        assert result[0].old_value == 3

    def test_nested_dict_change(self):
        old = {"outer": {"inner": 1}}
        new = {"outer": {"inner": 2}}
        result = diff_dicts(old, new)
        assert len(result) == 1
        assert result[0].path == "outer.inner"
        assert result[0].change_type == "changed"

    def test_ignore_fields(self):
        old = {"a": 1, "updated_date": "old"}
        new = {"a": 1, "updated_date": "new"}
        result = diff_dicts(old, new, ignore_fields={"updated_date"})
        assert result == []

    def test_ignore_fields_still_shows_others(self):
        old = {"a": 1, "updated_date": "old"}
        new = {"a": 2, "updated_date": "new"}
        result = diff_dicts(old, new, ignore_fields={"updated_date"})
        assert len(result) == 1
        assert result[0].path == "a"

    def test_datetime_normalization(self):
        """yaml.safe_load parses dates; normalization should make them equal."""
        old = {"date": datetime(2025, 1, 15)}
        new = {"date": "2025-01-15T00:00:00"}
        result = diff_dicts(old, new)
        assert result == []

    def test_string_whitespace_normalization(self):
        old = {"desc": "hello "}
        new = {"desc": "hello"}
        result = diff_dicts(old, new)
        assert result == []


# --- diff_lists ---


class TestDiffLists:
    def test_identical_scalars(self):
        assert diff_lists([1, 2, 3], [1, 2, 3], "x") == []

    def test_positional_addition(self):
        result = diff_lists([1], [1, 2], "x")
        assert len(result) == 1
        assert result[0].path == "x[1]"
        assert result[0].change_type == "added"

    def test_positional_removal(self):
        result = diff_lists([1, 2], [1], "x")
        assert len(result) == 1
        assert result[0].path == "x[1]"
        assert result[0].change_type == "removed"

    def test_keyed_match_by_name(self):
        old = [{"name": "a", "val": 1}, {"name": "b", "val": 2}]
        new = [{"name": "b", "val": 2}, {"name": "a", "val": 1}]
        result = diff_lists(old, new, "items")
        assert result == []  # Reordering should not matter with keyed match

    def test_keyed_match_detects_change(self):
        old = [{"name": "a", "val": 1}]
        new = [{"name": "a", "val": 2}]
        result = diff_lists(old, new, "items")
        assert len(result) == 1
        assert result[0].path == "items[name=a].val"

    def test_keyed_match_addition(self):
        old = [{"name": "a"}]
        new = [{"name": "a"}, {"name": "b"}]
        result = diff_lists(old, new, "items")
        added = [r for r in result if r.change_type == "added"]
        assert len(added) == 1
        assert "name=b" in added[0].path

    def test_keyed_match_removal(self):
        old = [{"name": "a"}, {"name": "b"}]
        new = [{"name": "a"}]
        result = diff_lists(old, new, "items")
        removed = [r for r in result if r.change_type == "removed"]
        assert len(removed) == 1
        assert "name=b" in removed[0].path

    def test_positional_fallback_for_non_dicts(self):
        result = diff_lists(["a", "b"], ["a", "c"], "tags")
        assert len(result) == 1
        assert result[0].path == "tags[1]"
        assert result[0].change_type == "changed"

    def test_empty_lists(self):
        assert diff_lists([], [], "x") == []


# --- FileDiffResult ---


class TestFileDiffResult:
    def test_has_changes_true(self):
        r = FileDiffResult("f.yaml", [DiffEntry("a", "changed", 1, 2)])
        assert r.has_changes is True

    def test_has_changes_false(self):
        r = FileDiffResult("f.yaml", [])
        assert r.has_changes is False


# --- Integration: roundtrip real YAML ---


DISORDER_FILES = [
    f for f in glob.glob(str(KB_DIR / "*.yaml")) if not f.endswith(".history.yaml")
]


@pytest.mark.parametrize(
    "filepath",
    DISORDER_FILES[:5],  # Test a sample for speed
    ids=lambda p: Path(p).stem,
)
def test_roundtrip_zero_diff(filepath):
    """Loading a YAML file and comparing it to itself should produce zero diffs."""
    data = yaml.safe_load(Path(filepath).read_text())
    result = diff_dicts(data, data)
    assert result == [], f"Self-diff should be empty for {filepath}"


@pytest.mark.parametrize(
    "filepath",
    DISORDER_FILES[:5],
    ids=lambda p: Path(p).stem,
)
def test_dump_reload_zero_diff(filepath):
    """Dumping and reloading YAML should not introduce spurious diffs."""
    data = yaml.safe_load(Path(filepath).read_text())
    roundtripped = yaml.safe_load(yaml.dump(data, default_flow_style=False))
    result = diff_dicts(data, roundtripped)
    assert result == [], f"Roundtrip diff should be empty for {filepath}"
