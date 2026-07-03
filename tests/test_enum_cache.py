from __future__ import annotations

import csv
from pathlib import Path

from linkml_term_validator.plugins import BindingValidationPlugin

from dismech.enum_cache import (
    current_enum_caches,
    repair_enum_cache_dir,
    scan_enum_cache_dir,
)


def _write_toy_schema(path: Path) -> None:
    path.write_text(
        """
id: https://example.org/test
name: test_schema
prefixes:
  TEST: https://example.org/TEST_
enums:
  TestTerm:
    reachable_from:
      source_nodes:
        - TEST:0000
      relationship_types:
        - rdfs:subClassOf
""".lstrip()
    )


def _write_curie_csv(path: Path, curies: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["curie"], lineterminator="\n")
        writer.writeheader()
        for curie in curies:
            writer.writerow({"curie": curie})


def test_enum_cache_scan_and_repair_reject_stale_invalid_and_duplicate_rows(
    tmp_path: Path, monkeypatch
) -> None:
    schema_path = tmp_path / "schema.yaml"
    cache_dir = tmp_path / "cache"
    enum_dir = cache_dir / "enums"
    enum_dir.mkdir(parents=True)
    _write_toy_schema(schema_path)

    def fake_membership(self, value, enum_def, schema_view=None):  # noqa: ANN001
        return value.startswith("GOOD:")

    monkeypatch.setattr(BindingValidationPlugin, "is_value_in_enum", fake_membership)

    expected = current_enum_caches(schema_path, cache_dir, oak_config=None)
    current = next(iter(expected.values()))
    _write_curie_csv(current.path, ["GOOD:1", "BAD:1", "GOOD:1"])
    _write_curie_csv(enum_dir / "oldterm_deadbeef0000.csv", ["GOOD:2"])

    findings = scan_enum_cache_dir(schema_path, cache_dir, oak_config=None)
    formatted = "\n".join(f.format() for f in findings)
    assert "stale enum cache file" in formatted
    assert "cached CURIE is not valid for current enum: BAD:1" in formatted
    assert "duplicate cached CURIE: GOOD:1" in formatted

    repair_findings = repair_enum_cache_dir(schema_path, cache_dir, oak_config=None)
    repaired = "\n".join(f.format() for f in repair_findings)
    assert "removed stale enum cache file" in repaired
    assert "removed invalid cached CURIE: BAD:1" in repaired
    assert "removed duplicate cached CURIE: GOOD:1" in repaired
    assert not (enum_dir / "oldterm_deadbeef0000.csv").exists()
    assert current.path.read_text() == "curie\nGOOD:1\n"
    assert scan_enum_cache_dir(schema_path, cache_dir, oak_config=None) == []


def test_enum_cache_repair_rewrites_malformed_current_file(
    tmp_path: Path, monkeypatch
) -> None:
    schema_path = tmp_path / "schema.yaml"
    cache_dir = tmp_path / "cache"
    (cache_dir / "enums").mkdir(parents=True)
    _write_toy_schema(schema_path)

    monkeypatch.setattr(BindingValidationPlugin, "is_value_in_enum", lambda *args: True)

    current = next(
        iter(current_enum_caches(schema_path, cache_dir, oak_config=None).values())
    )
    current.path.write_text("bad_header\nGOOD:1\n", encoding="utf-8")

    findings = repair_enum_cache_dir(schema_path, cache_dir, oak_config=None)
    formatted = "\n".join(f.format() for f in findings)
    assert "rewrote malformed enum cache file" in formatted
    assert current.path.read_text(encoding="utf-8") == "curie\n"


def test_enum_cache_offline_scan_skips_membership_but_keeps_structural_checks(
    tmp_path: Path, monkeypatch
) -> None:
    """Offline mode must not touch OAK: it skips is_value_in_enum (which can
    trigger multi-GB downloads) while still catching stale files, malformed
    headers, and duplicate rows."""
    schema_path = tmp_path / "schema.yaml"
    cache_dir = tmp_path / "cache"
    enum_dir = cache_dir / "enums"
    enum_dir.mkdir(parents=True)
    _write_toy_schema(schema_path)

    def boom(self, value, enum_def, schema_view=None):  # noqa: ANN001
        raise AssertionError("offline scan must not call is_value_in_enum")

    monkeypatch.setattr(BindingValidationPlugin, "is_value_in_enum", boom)

    current = next(
        iter(current_enum_caches(schema_path, cache_dir, oak_config=None).values())
    )
    # BAD:1 would be flagged online, but offline membership is not re-derived.
    _write_curie_csv(current.path, ["GOOD:1", "BAD:1", "GOOD:1"])
    _write_curie_csv(enum_dir / "oldterm_deadbeef0000.csv", ["GOOD:2"])

    findings = scan_enum_cache_dir(
        schema_path, cache_dir, oak_config=None, offline=True
    )
    formatted = "\n".join(f.format() for f in findings)
    assert "stale enum cache file" in formatted
    assert "duplicate cached CURIE: GOOD:1" in formatted
    # Membership was NOT re-derived, so the invalid CURIE is not reported.
    assert "not valid for current enum" not in formatted


def test_single_file_validate_recipes_do_not_run_check_enum_cache() -> None:
    """Single-file validation must not depend on check-enum-cache, which
    re-derives every dynamic enum from OAK and can pull multi-GB DBs (#5150)."""
    justfile = (Path(__file__).parent.parent / "project.justfile").read_text()

    markers = [
        "# Full validation of a single disorder file",
        "# Full validation of a single comorbidity file",
        "# Validate a single mechanism module file",
        "# Validate a single disease grouping file",
        "# Validate terms in a single file",
    ]
    for i, marker in enumerate(markers):
        body = justfile.split(marker, 1)[1]
        # bound the recipe body at the start of the next top-level comment recipe
        body = body.split("\n# ", 1)[0]
        assert "just check-enum-cache" not in body, (
            f"recipe after {marker!r} should not call check-enum-cache"
        )

    # The provisioning recipe and offline check exist for constrained envs.
    assert "fetch-ontology-dbs" in justfile
    assert "check-enum-cache-offline" in justfile


def test_normalize_cache_uses_repo_local_temp_files() -> None:
    justfile = (Path(__file__).parent.parent / "project.justfile").read_text()
    assert "/tmp/_sorted_enum.csv" not in justfile
    assert "${TMPDIR:-/tmp}" not in justfile
    assert "mktemp -d tmp/dismech_enum_cache.XXXXXX" in justfile


def test_validate_terms_all_skips_history_files() -> None:
    justfile = (Path(__file__).parent.parent / "project.justfile").read_text()
    validate_terms_all = justfile.split("validate-terms-all:", 1)[1].split(
        "# Validate terms in a single file", 1
    )[0]
    assert "*.history.yaml" in validate_terms_all
