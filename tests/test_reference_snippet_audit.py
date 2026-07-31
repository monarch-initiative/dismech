"""Tests for the affirmative reference/snippet audit (issue #7252).

``linkml-reference-validator`` reports ``Total checks: 0`` on a clean run because
the counter it echoes holds *issues found*, not checks performed. These tests
cover the downstream mitigation: a read-only, offline count of the
reference/snippet pairs actually verified against ``references_cache/``.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from dismech.reference_snippet_audit import (
    DEFAULT_SCHEMA,
    CachedReferenceIndex,
    audit_files,
    discover_field_names,
    load_cache_dir,
    load_skip_prefixes,
    main,
)

ROOT = Path(__file__).parent.parent

ABSTRACT = (
    "Vici syndrome is caused by recessive mutations in EPG5. "
    "Affected individuals show agenesis of the corpus callosum and cataracts."
)


def _write_cache(cache_dir: Path, filename: str, content: str) -> Path:
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / filename
    path.write_text(
        "---\n"
        f'reference_id: "{filename[:-3].replace("_", ":", 1)}"\n'
        'title: "A real paper"\n'
        "authors:\n"
        "- Doe J\n"
        "journal: Example Journal\n"
        "content_type: abstract_only\n"
        "---\n\n"
        f"{content}\n",
        encoding="utf-8",
    )
    return path


def _write_entry(path: Path, snippets: list[tuple[str, str]]) -> Path:
    lines = ["name: Test Disease", "evidence:"]
    for reference, snippet in snippets:
        lines.append(f"- reference: {reference}")
        lines.append("  supports: SUPPORT")
        lines.append(f"  snippet: {snippet!r}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _audit(tmp_path: Path, snippets: list[tuple[str, str]], **kwargs):
    entry = _write_entry(tmp_path / "entry.yaml", snippets)
    return audit_files([entry], cache_dir=tmp_path / "references_cache", **kwargs)


def test_counts_every_verified_pair(tmp_path: Path) -> None:
    _write_cache(tmp_path / "references_cache", "PMID_123.md", ABSTRACT)

    report = _audit(
        tmp_path,
        [
            ("PMID:123", "recessive mutations in EPG5"),
            ("PMID:123", "agenesis of the corpus callosum"),
        ],
    )

    assert (report.total, report.verified) == (2, 2)
    assert report.mismatched == []
    # The whole point of #7252: a clean run must not read as "0".
    assert "2/2 verified" in report.summary_line()


def test_reports_snippet_absent_from_cached_text(tmp_path: Path) -> None:
    _write_cache(tmp_path / "references_cache", "PMID_123.md", ABSTRACT)

    report = _audit(
        tmp_path,
        [
            ("PMID:123", "recessive mutations in EPG5"),
            ("PMID:123", "The moon is made of green cheese."),
        ],
    )

    assert (report.total, report.verified) == (2, 1)
    assert len(report.mismatched) == 1
    unverified = report.mismatched[0]
    assert unverified.pair.location == "evidence[1].snippet"
    assert "green cheese" in unverified.reason
    assert "1 not found in cached text" in report.summary_line()


def test_matching_mirrors_validator_normalization(tmp_path: Path) -> None:
    """Case, punctuation, whitespace, Greek letters, ``...`` and ``[...]``."""
    _write_cache(
        tmp_path / "references_cache",
        "PMID_123.md",
        "TGF-β signalling drives fibrosis;\nmyofibroblasts then deposit collagen.",
    )

    report = _audit(
        tmp_path,
        [
            ("PMID:123", "tgf beta signalling"),
            ("PMID:123", "drives fibrosis ... deposit collagen"),
            ("PMID:123", "myofibroblasts [i.e. activated fibroblasts] then deposit"),
        ],
    )

    assert (report.total, report.verified) == (3, 3)


def test_skips_configured_prefixes_without_counting_them_as_verified(
    tmp_path: Path,
) -> None:
    config = tmp_path / "config.yaml"
    config.write_text("skip_prefixes:\n  - MONDO\n", encoding="utf-8")
    _write_cache(tmp_path / "references_cache", "PMID_123.md", ABSTRACT)

    report = _audit(
        tmp_path,
        [
            ("PMID:123", "recessive mutations in EPG5"),
            ("MONDO:0012345", "not a literature reference"),
        ],
        config_path=config,
    )

    assert (report.total, report.verified, report.skipped_prefix) == (2, 1, 1)
    assert report.mismatched == []
    assert "skipped by prefix" in report.summary_line()


def test_uncached_reference_is_reported_separately_from_a_mismatch(
    tmp_path: Path,
) -> None:
    (tmp_path / "references_cache").mkdir()

    report = _audit(tmp_path, [("PMID:999", "anything at all")])

    assert (report.total, report.verified, report.not_cached) == (1, 0, 1)
    assert report.mismatched == []
    assert "not cached locally" in report.summary_line()


def test_resolves_cache_files_written_under_a_source_prefix(tmp_path: Path) -> None:
    """A bare ``NCT…`` id is cached as ``clinicaltrials_NCT….md`` (see #7252)."""
    _write_cache(
        tmp_path / "references_cache",
        "clinicaltrials_NCT06087757.md",
        "This study evaluates a novel therapy in Williams syndrome.",
    )

    report = _audit(tmp_path, [("NCT06087757", "a novel therapy in Williams syndrome")])

    assert (report.total, report.verified, report.not_cached) == (1, 1, 0)


def test_ambiguous_bare_identifier_is_not_resolved(tmp_path: Path) -> None:
    cache_dir = tmp_path / "references_cache"
    _write_cache(cache_dir, "foo_ABC1.md", "first source body")
    _write_cache(cache_dir, "bar_ABC1.md", "second source body")

    index = CachedReferenceIndex(cache_dir)

    assert index.resolve_cache_path("ABC1") is None


def test_unreadable_file_is_recorded_without_crashing(tmp_path: Path) -> None:
    broken = tmp_path / "broken.yaml"
    broken.write_text("name: [unclosed\n", encoding="utf-8")

    report = audit_files([broken], cache_dir=tmp_path / "references_cache")

    assert report.files == 0
    assert report.unreadable and "broken.yaml" in report.unreadable[0]


def test_empty_input_summary_does_not_claim_verification(tmp_path: Path) -> None:
    report = _audit(tmp_path, [])

    assert report.total == 0
    assert "no reference/snippet pairs" in report.summary_line()


def test_fields_are_discovered_from_schema_implements_annotations() -> None:
    excerpts, references = discover_field_names(ROOT / DEFAULT_SCHEMA)

    assert "snippet" in excerpts
    assert "reference" in references


def test_config_loaders_read_the_repository_config() -> None:
    config = ROOT / "conf" / "reference_validator_config.yaml"

    assert "MONDO" in load_skip_prefixes(config)
    assert load_cache_dir(config) == Path("references_cache")


def test_cli_is_advisory_by_default_and_gated_by_strict(tmp_path: Path, capsys) -> None:
    _write_cache(tmp_path / "references_cache", "PMID_123.md", ABSTRACT)
    entry = _write_entry(
        tmp_path / "entry.yaml", [("PMID:123", "The moon is made of green cheese.")]
    )
    args = [
        str(entry),
        "--cache-dir",
        str(tmp_path / "references_cache"),
        "--config",
        str(tmp_path / "missing-config.yaml"),
    ]

    assert main(args) == 0
    assert "0/1 verified" in capsys.readouterr().out
    assert main([*args, "--strict"]) == 1


def test_wrapper_appends_the_audit_line_to_validator_output(tmp_path: Path) -> None:
    """The wrapper prints the affirmative count without touching the exit code."""
    entry = _write_entry(tmp_path / "entry.yaml", [("PMID:123", "mutations in EPG5")])
    _write_cache(tmp_path / "references_cache", "PMID_123.md", ABSTRACT)

    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    fake_uv = bin_dir / "uv"
    # Stand in for the validator itself; the audit invocation (``uv run python -m
    # dismech.reference_snippet_audit ...``) is delegated to the real interpreter.
    fake_uv.write_text(
        "#!/usr/bin/env bash\n"
        'if [[ "$*" == *reference_snippet_audit* ]]; then\n'
        "  shift 2\n"
        f'  exec "{sys.executable}" "$@"\n'
        "fi\n"
        "printf '%s\\n' '  Total checks: 0'\n"
        "printf '%s\\n' '  All validations passed!'\n",
        encoding="utf-8",
    )
    fake_uv.chmod(0o755)

    env = {**os.environ, "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}"}
    result = subprocess.run(
        [
            "bash",
            str(ROOT / "scripts" / "run_reference_validator.sh"),
            "validate",
            "data",
            str(entry),
            "--schema",
            str(ROOT / DEFAULT_SCHEMA),
            "--target-class",
            "Disease",
        ],
        capture_output=True,
        check=False,
        # Run from tmp_path so the audit's default references_cache/ is the
        # fixture cache, not the repository's.
        cwd=tmp_path,
        env=env,
        text=True,
    )

    assert result.returncode == 0
    assert "Total checks: 0" in result.stdout
    assert "Snippets checked: 1/1 verified" in result.stdout


def test_wrapper_audit_can_be_disabled(tmp_path: Path) -> None:
    fake_uv = tmp_path / "uv"
    fake_uv.write_text(
        "#!/usr/bin/env bash\nprintf '%s\\n' '  All validations passed!'\n",
        encoding="utf-8",
    )
    fake_uv.chmod(0o755)

    env = {
        **os.environ,
        "PATH": f"{tmp_path}{os.pathsep}{os.environ['PATH']}",
        "DISMECH_SKIP_SNIPPET_AUDIT": "1",
    }
    result = subprocess.run(
        [
            "bash",
            str(ROOT / "scripts" / "run_reference_validator.sh"),
            "validate",
            "data",
            "dummy.yaml",
        ],
        capture_output=True,
        check=False,
        cwd=ROOT,
        env=env,
        text=True,
    )

    assert result.returncode == 0
    assert "Snippets checked" not in result.stdout
