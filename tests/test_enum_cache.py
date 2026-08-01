from __future__ import annotations

import csv
import os
import re
import subprocess
from pathlib import Path

from linkml_term_validator.plugins import BindingValidationPlugin

from dismech.enum_cache import (
    canonical_curie_rows,
    current_enum_caches,
    main,
    repair_enum_cache_dir,
    scan_cache_order,
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


def _recipe_body(justfile: str, recipe: str) -> str:
    match = re.search(rf"(?m)^{re.escape(recipe)}:\n", justfile)
    assert match is not None, f"recipe {recipe!r} not found"
    body = justfile[match.end() :]
    return body.split("\n# ", 1)[0]


def test_enum_cache_scan_and_repair_reject_stale_invalid_and_duplicate_rows(
    tmp_path: Path, monkeypatch
) -> None:
    schema_path = tmp_path / "schema.yaml"
    cache_dir = tmp_path / "cache"
    enum_dir = cache_dir / "enums"
    enum_dir.mkdir(parents=True)
    _write_toy_schema(schema_path)

    def fake_membership(self, value, enum_def, schema_view=None):
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
    # stale-file finding is a warning; structural errors are not
    stale = [f for f in findings if "stale" in f.reason]
    assert all(f.is_warning for f in stale)
    errors = [f for f in findings if not f.is_warning]
    assert len(errors) >= 2

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

    def boom(self, value, enum_def, schema_view=None):
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


def test_enum_cache_ordering_is_warning_until_strict_cutover(
    tmp_path: Path, monkeypatch
) -> None:
    schema_path = tmp_path / "schema.yaml"
    cache_dir = tmp_path / "cache"
    (cache_dir / "enums").mkdir(parents=True)
    _write_toy_schema(schema_path)

    monkeypatch.setattr(
        BindingValidationPlugin,
        "is_value_in_enum",
        lambda *args: (_ for _ in ()).throw(
            AssertionError("offline scan must not call is_value_in_enum")
        ),
    )

    current = next(
        iter(current_enum_caches(schema_path, cache_dir, oak_config=None).values())
    )
    _write_curie_csv(current.path, ["TEST:0000", "TEST:0002", "TEST:0001"])

    findings = scan_enum_cache_dir(
        schema_path, cache_dir, oak_config=None, offline=True
    )
    order = [f for f in findings if "canonical order" in f.reason]
    assert len(order) == 1
    assert order[0].is_warning
    assert "sorted through row 2" in order[0].reason
    assert "out-of-order tail 1" in order[0].reason

    assert (
        main(
            [
                "--schema",
                str(schema_path),
                "--cache-dir",
                str(cache_dir),
                "--offline",
            ]
        )
        == 0
    )
    assert (
        main(
            [
                "--schema",
                str(schema_path),
                "--cache-dir",
                str(cache_dir),
                "--offline",
                "--strict-order",
            ]
        )
        == 1
    )


def test_cache_order_audit_covers_enum_and_term_caches(tmp_path: Path) -> None:
    cache_dir = tmp_path / "cache"
    enum_dir = cache_dir / "enums"
    term_dir = cache_dir / "mondo"
    enum_dir.mkdir(parents=True)
    term_dir.mkdir(parents=True)
    _write_curie_csv(enum_dir / "example.csv", ["TEST:2", "TEST:1"])
    (term_dir / "terms.csv").write_text(
        "curie,label,retrieved_at\nTEST:2,two,2026-01-01\nTEST:1,one,2026-01-01\n",
        encoding="utf-8",
    )

    findings = scan_cache_order(cache_dir)
    assert [f.path for f in findings] == [
        enum_dir / "example.csv",
        term_dir / "terms.csv",
    ]
    assert all(f.sorted_through == 1 for f in findings)
    assert all(f.tail_size == 1 for f in findings)
    assert main(["--cache-dir", str(cache_dir), "--check-order"]) == 0
    assert (
        main(
            [
                "--cache-dir",
                str(cache_dir),
                "--check-order",
                "--strict-order",
            ]
        )
        == 1
    )


def test_cache_order_audit_reports_malformed_headers_without_failing(
    tmp_path: Path, capsys
) -> None:
    cache_dir = tmp_path / "cache"
    empty_term_dir = cache_dir / "empty"
    malformed_term_dir = cache_dir / "malformed"
    empty_term_dir.mkdir(parents=True)
    malformed_term_dir.mkdir(parents=True)
    (empty_term_dir / "terms.csv").write_text("", encoding="utf-8")
    (malformed_term_dir / "terms.csv").write_text(
        "id,label\nTEST:1,one\n", encoding="utf-8"
    )

    findings = scan_cache_order(cache_dir)
    assert len(findings) == 2
    assert all("expected first CSV column" in finding.format() for finding in findings)

    assert main(["--cache-dir", str(cache_dir), "--check-order"]) == 0
    assert (
        main(
            [
                "--cache-dir",
                str(cache_dir),
                "--check-order",
                "--strict-order",
            ]
        )
        == 0
    )
    captured = capsys.readouterr()
    assert "[WARNING]" in captured.err
    assert "Traceback" not in captured.err


def test_default_validate_recipes_do_not_run_online_check_enum_cache() -> None:
    """Default validation must not depend on the online enum cache audit, which
    re-derives every dynamic enum from OAK and can pull multi-GB DBs (#5150)."""
    justfile = (Path(__file__).parent.parent / "project.justfile").read_text()

    online_check = re.compile(r"(?m)^\s+just check-enum-cache$")
    any_check = re.compile(r"(?m)^\s+just check-enum-cache(?:-offline)?$")

    assert online_check.search(justfile) is None

    offline_recipes = [
        "validate-all",
        "validate-comorbidities-all",
        "validate-modules",
        "validate-groupings",
        "validate-terms-all",
    ]
    for recipe in offline_recipes:
        body = _recipe_body(justfile, recipe)
        assert "just check-enum-cache-offline" in body, (
            f"{recipe!r} should run the offline enum cache check"
        )

    single_file_recipes = [
        "validate file",
        "validate-comorbidity file",
        "validate-module file",
        "validate-grouping file",
        "validate-terms file",
    ]
    for recipe in single_file_recipes:
        body = _recipe_body(justfile, recipe)
        assert any_check.search(body) is None, (
            f"{recipe!r} should not run enum cache audits"
        )

    # The provisioning recipe and offline check exist for constrained envs.
    assert "fetch-ontology-dbs" in justfile
    assert "check-enum-cache-offline" in justfile


def test_validate_all_batches_expensive_validators() -> None:
    """Full validation should reuse each validator process across all files."""
    justfile = (Path(__file__).parent.parent / "project.justfile").read_text()
    body = _recipe_body(justfile, "validate-all")

    assert "for f in {{kb_dir}}/*.yaml" not in body
    assert "mapfile -t files" in body
    assert (
        'uv run linkml-validate --schema {{schema_path}} --target-class Disease "${files[@]}"'
        in body
    )
    assert (
        '{{term_validator}} validate-data "${files[@]}" -s {{schema_path}} -t Disease'
        in body
    )
    assert (
        '{{ref_validator}} validate data "${files[@]}" --schema {{schema_path}}' in body
    )


def test_validate_disorders_batches_expensive_validators() -> None:
    """Changed-file disorder validation should also reuse validator processes."""
    justfile = (Path(__file__).parent.parent / "project.justfile").read_text()
    body = _recipe_body(justfile, "validate-disorders *files")

    # Iterate positional args ("$@") rather than interpolating {{files}} as raw
    # shell text, so filenames with metacharacters don't break the recipe (#5525).
    assert 'for f in "$@"; do' in body
    assert (
        'uv run linkml-validate --schema {{schema_path}} --target-class Disease "${existing[@]}"'
        in body
    )
    assert (
        '{{term_validator}} validate-data "${existing[@]}" -s {{schema_path}} -t Disease'
        in body
    )
    assert (
        '{{ref_validator}} validate data "${existing[@]}" --schema {{schema_path}}'
        in body
    )
    assert "--no-full-text" in body


def test_ci_changed_disorder_validation_uses_batched_recipe() -> None:
    workflow = (
        Path(__file__).parent.parent / ".github" / "workflows" / "main.yaml"
    ).read_text()
    changed_step = workflow.split("- name: Validate changed disorder KB files", 1)[
        1
    ].split("- name: Validate changed comorbidity KB files", 1)[0]

    assert "just validate-disorders" in changed_step
    assert 'just validate "$f"' not in changed_step


def test_normalize_cache_uses_repo_local_temp_files() -> None:
    justfile = (Path(__file__).parent.parent / "project.justfile").read_text()
    assert "/tmp/_sorted_enum.csv" not in justfile
    assert "${TMPDIR:-/tmp}" not in justfile
    assert "mktemp -d tmp/dismech_enum_cache.XXXXXX" in justfile
    assert "LC_ALL=C sort -u" in justfile


def test_shell_and_python_enum_cache_sorting_agree() -> None:
    """The shell normalizer must match Python codepoint ordering exactly."""

    root_dir = Path(__file__).parent.parent
    env = os.environ.copy()
    env["LC_ALL"] = "C"

    for path in sorted((root_dir / "cache" / "enums").glob("*.csv")):
        rows = path.read_text(encoding="utf-8").splitlines()[1:]
        shell = subprocess.run(
            ["sort", "-u"],
            input="".join(f"{row}\n" for row in rows),
            text=True,
            capture_output=True,
            check=True,
            env=env,
        ).stdout
        python = "".join(f"{row}\n" for row in canonical_curie_rows(rows))
        assert shell == python, f"shell/Python ordering differs for {path}"


def test_validate_terms_all_skips_history_files() -> None:
    justfile = (Path(__file__).parent.parent / "project.justfile").read_text()
    validate_terms_all = justfile.split("validate-terms-all:", 1)[1].split(
        "# Validate terms in a single file", 1
    )[0]
    assert "*.history.yaml" in validate_terms_all


def test_stale_only_scan_is_warning_not_error(tmp_path: Path) -> None:
    """A stale cache file (validator hash shift) must not fail CI — just warn."""
    schema_path = tmp_path / "schema.yaml"
    cache_dir = tmp_path / "cache"
    (cache_dir / "enums").mkdir(parents=True)
    _write_toy_schema(schema_path)

    # Write only a stale file; the expected cache file is absent.
    (cache_dir / "enums" / "oldterm_deadbeef0000.csv").write_text(
        "curie\nGOOD:1\n", encoding="utf-8"
    )

    findings = scan_enum_cache_dir(
        schema_path, cache_dir, oak_config=None, offline=True
    )
    assert findings, "expected at least one stale finding"
    assert all(f.is_warning for f in findings), (
        "stale-only findings must all be warnings"
    )

    # main() must exit 0 (warning-only path)
    rc = main(
        [
            "--schema",
            str(schema_path),
            "--cache-dir",
            str(cache_dir),
            "--offline",
        ]
    )
    assert rc == 0, "stale-only scan must exit 0 (non-fatal warning)"


def test_error_findings_still_fail(tmp_path: Path, monkeypatch) -> None:
    """Malformed headers, duplicate rows, and invalid CURIEs are still errors."""
    schema_path = tmp_path / "schema.yaml"
    cache_dir = tmp_path / "cache"
    (cache_dir / "enums").mkdir(parents=True)
    _write_toy_schema(schema_path)

    monkeypatch.setattr(BindingValidationPlugin, "is_value_in_enum", lambda *a: False)

    expected = current_enum_caches(schema_path, cache_dir, oak_config=None)
    current_cache = next(iter(expected.values()))
    _write_curie_csv(current_cache.path, ["BAD:1"])

    findings = scan_enum_cache_dir(schema_path, cache_dir, oak_config=None)
    errors = [f for f in findings if not f.is_warning]
    assert errors, "invalid CURIE must produce an error finding"

    rc = main(
        [
            "--schema",
            str(schema_path),
            "--cache-dir",
            str(cache_dir),
        ]
    )
    assert rc == 1, "error findings must exit 1"


def test_mixed_warnings_and_errors_fail(tmp_path: Path, monkeypatch) -> None:
    """When stale files (warnings) and structural errors coexist, exit 1."""
    schema_path = tmp_path / "schema.yaml"
    cache_dir = tmp_path / "cache"
    enum_dir = cache_dir / "enums"
    enum_dir.mkdir(parents=True)
    _write_toy_schema(schema_path)

    monkeypatch.setattr(BindingValidationPlugin, "is_value_in_enum", lambda *a: False)

    expected = current_enum_caches(schema_path, cache_dir, oak_config=None)
    current_cache = next(iter(expected.values()))
    _write_curie_csv(current_cache.path, ["BAD:1"])
    # Also add a stale file
    (enum_dir / "oldterm_deadbeef0000.csv").write_text(
        "curie\nGOOD:1\n", encoding="utf-8"
    )

    findings = scan_enum_cache_dir(schema_path, cache_dir, oak_config=None)
    warnings = [f for f in findings if f.is_warning]
    errors = [f for f in findings if not f.is_warning]
    assert warnings
    assert errors

    rc = main(["--schema", str(schema_path), "--cache-dir", str(cache_dir)])
    assert rc == 1, "errors alongside warnings must still exit 1"
