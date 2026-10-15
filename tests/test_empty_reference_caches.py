"""Tests for empty reference cache detection (issue #9825).

A cache file with ``content_type: unavailable`` holds no quotable text. The
signal is that frontmatter field, never body length: structured caches and
records without a ``## Content`` heading are quotable and must not be flagged.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

from dismech.reference_cache_frontmatter import (
    empty_cache_warning,
    find_kb_citations,
    format_empty_cache_summary,
    format_empty_cache_tsv,
    main,
    read_empty_cache,
    resolve_cache_file,
    scan_empty_caches,
)

ROOT = Path(__file__).parent.parent
WRAPPER = ROOT / "scripts" / "run_reference_validator.sh"


def _write_cache(
    cache_dir: Path,
    reference_id: str,
    content_type: str,
    body: str = "",
    extra: str = "",
) -> Path:
    stem = reference_id.replace(":", "_").replace("/", "_")
    path = cache_dir / f"{stem}.md"
    path.write_text(
        "---\n"
        f"reference_id: {reference_id}\n"
        "title: A paper\n"
        "authors:\n- Doe J\n"
        "journal: Example Journal\n"
        f"{extra}"
        f"content_type: {content_type}\n"
        "---\n\n"
        "# A paper\n"
        f"{body}",
        encoding="utf-8",
    )
    return path


def test_unavailable_cache_is_detected(tmp_path: Path):
    path = _write_cache(tmp_path, "PMID:111", "unavailable")
    empty = read_empty_cache(path)
    assert empty is not None
    assert empty.reference_id == "PMID:111"
    assert empty.prefix == "PMID"
    assert empty.full_text_attempted is False


def test_full_text_attempted_marker_is_read(tmp_path: Path):
    path = _write_cache(
        tmp_path, "PMID:112", "unavailable", extra="full_text_attempted: true\n"
    )
    empty = read_empty_cache(path)
    assert empty is not None and empty.full_text_attempted is True


def test_abstract_only_is_not_flagged(tmp_path: Path):
    path = _write_cache(
        tmp_path, "PMID:113", "abstract_only", body="\n## Content\n\nA finding.\n"
    )
    assert read_empty_cache(path) is None


def test_short_body_without_content_heading_is_not_flagged(tmp_path: Path):
    """PMID_31909928 has no ``## Content`` heading and is still quotable."""
    path = _write_cache(tmp_path, "PMID:31909928", "abstract_only", body="Text.\n")
    assert read_empty_cache(path) is None


def test_structured_cache_is_not_flagged(tmp_path: Path):
    path = tmp_path / "ORPHA_558.md"
    path.write_text(
        "---\n"
        "reference_id: ORPHA:558\n"
        "title: Marfan syndrome\n"
        "content_type: structured_database\n"
        "database: orphanet\n"
        "---\n\n"
        "## Definition\n\nshort\n",
        encoding="utf-8",
    )
    assert read_empty_cache(path) is None


def test_resolve_cache_file_is_case_insensitive(tmp_path: Path):
    path = _write_cache(tmp_path, "DOI:10.1000/ABC", "unavailable")
    assert resolve_cache_file(tmp_path, "DOI:10.1000/ABC") == path
    assert resolve_cache_file(tmp_path, "doi:10.1000/abc") == path
    assert resolve_cache_file(tmp_path, "DOI:10.1000/missing") is None


def test_warning_only_for_unavailable(tmp_path: Path):
    _write_cache(tmp_path, "PMID:201", "unavailable")
    _write_cache(tmp_path, "PMID:202", "abstract_only", body="\n## Content\n\nx\n")

    warning = empty_cache_warning("PMID:201", tmp_path)
    assert warning is not None
    assert warning.startswith("WARNING:")
    assert "content_type: unavailable" in warning
    # The wording must describe this fetch, not the record, and point at a retry.
    assert "on this fetch" in warning
    assert "retry may succeed" in warning
    assert "--force" in warning
    assert "cannot be quoted" not in warning

    assert empty_cache_warning("PMID:202", tmp_path) is None
    assert empty_cache_warning("PMID:999", tmp_path) is None


def test_fetch_warning_cli_prints_to_stderr_and_exits_zero(tmp_path: Path, capsys):
    _write_cache(tmp_path, "PMID:201", "unavailable")
    _write_cache(tmp_path, "PMID:202", "abstract_only", body="\n## Content\n\nx\n")

    assert main(["fetch-warning", "--cache-dir", str(tmp_path), "PMID:201"]) == 0
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "WARNING: PMID:201" in captured.err

    assert main(["fetch-warning", "--cache-dir", str(tmp_path), "PMID:202"]) == 0
    assert capsys.readouterr().err == ""


def _sweep_fixture(tmp_path: Path) -> tuple[Path, Path]:
    cache = tmp_path / "references_cache"
    cache.mkdir()
    _write_cache(cache, "PMID:1", "unavailable", extra="full_text_attempted: true\n")
    _write_cache(cache, "PMID:2", "unavailable")
    _write_cache(cache, "PMID:3", "unavailable")
    _write_cache(
        cache, "DOI:10.1/x", "unavailable", extra="full_text_attempted: true\n"
    )
    _write_cache(cache, "PMID:4", "abstract_only", body="\n## Content\n\nx\n")

    kb = tmp_path / "kb" / "disorders"
    kb.mkdir(parents=True)
    (kb / "A.yaml").write_text(
        "name: A\n"
        "references:\n"
        "- reference: PMID:2\n"
        "  title: A paper\n"
        "phenotypes:\n"
        "- name: P\n"
        "  evidence:\n"
        "  - reference: PMID:4\n"
        "    snippet: x\n"
        "  - reference: doi:10.1/X\n"
        "    snippet: quoted text\n",
        encoding="utf-8",
    )
    return cache, tmp_path / "kb"


def test_sweep_groups_by_prefix_and_splits_on_full_text_attempted(tmp_path: Path):
    cache, _ = _sweep_fixture(tmp_path)
    empties = scan_empty_caches([cache])
    by_id = {e.reference_id: e for e in empties}
    assert set(by_id) == {"PMID:1", "PMID:2", "PMID:3", "DOI:10.1/x"}
    assert by_id["PMID:1"].full_text_attempted
    assert not by_id["PMID:2"].full_text_attempted

    summary = format_empty_cache_summary(empties, 5, None)
    assert "4 of 5 cache files" in summary
    pmid_row = next(
        line for line in summary.splitlines() if line.strip().startswith("PMID")
    )
    assert pmid_row.split() == ["PMID", "3", "1", "2"]
    doi_row = next(
        line for line in summary.splitlines() if line.strip().startswith("DOI")
    )
    assert doi_row.split() == ["DOI", "1", "1", "0"]


def test_sweep_reports_kb_citations_and_snippet_citations(tmp_path: Path):
    cache, kb = _sweep_fixture(tmp_path)
    empties = scan_empty_caches([cache])
    citations = find_kb_citations(kb, [e.reference_id for e in empties])

    assert set(citations.files) == {"PMID:2", "DOI:10.1/x"}
    # Only the snippet-bearing evidence item citing an empty cache is flagged;
    # the top-level references: entry and the quotable PMID:4 are not.
    assert set(citations.snippet_citations) == {"DOI:10.1/x"}

    summary = format_empty_cache_summary(empties, 5, citations)
    assert "Cited anywhere in kb/: 2 record(s)" in summary
    assert "Cited by an evidence item carrying a snippet: 1 record(s)" in summary

    tsv = format_empty_cache_tsv(empties, citations).splitlines()
    assert tsv[0].split("\t")[:3] == ["reference_id", "prefix", "full_text_attempted"]
    row = next(r.split("\t") for r in tsv[1:] if r.startswith("PMID:2\t"))
    assert row[1:5] == ["PMID", "false", "1", "0"]


def test_list_empty_cli_exits_zero(tmp_path: Path, capsys):
    cache, kb = _sweep_fixture(tmp_path)
    assert main(["list-empty", str(cache), "--kb-dir", str(kb), "--format", "tsv"]) == 0
    out = capsys.readouterr().out
    assert out.count("\n") == 5  # header + four empty records


def _fake_uv(tmp_path: Path, validator_exit: int = 0) -> dict[str, str]:
    """A ``uv`` stand-in: the validator is faked, dismech modules run for real."""
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    fake_uv = bin_dir / "uv"
    fake_uv.write_text(
        "#!/usr/bin/env bash\n"
        'if [[ "$*" == *reference_cache_frontmatter* ]]; then\n'
        "  shift 2\n"
        f'  exec "{sys.executable}" "$@"\n'
        "fi\n"
        "printf '%s\\n' 'Successfully cached'\n"
        f"exit {validator_exit}\n",
        encoding="utf-8",
    )
    fake_uv.chmod(0o755)
    return {
        **os.environ,
        "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
        "PYTHONPATH": str(ROOT / "src"),
    }


def _run_wrapper(tmp_path: Path, env: dict[str, str], *args: str):
    return subprocess.run(
        ["bash", str(WRAPPER), "cache", "reference", *args],
        capture_output=True,
        check=False,
        cwd=tmp_path,
        env=env,
        text=True,
    )


@pytest.mark.parametrize(
    ("content_type", "warned"), [("unavailable", True), ("abstract_only", False)]
)
def test_wrapper_warns_after_cache_reference_only_for_unavailable(
    tmp_path: Path, content_type: str, warned: bool
):
    cache = tmp_path / "references_cache"
    cache.mkdir()
    _write_cache(cache, "PMID:301", content_type, body="\n## Content\n\nx\n")
    env = _fake_uv(tmp_path)

    result = _run_wrapper(tmp_path, env, "PMID:301", "--force")

    assert result.returncode == 0
    assert "Successfully cached" in result.stdout
    assert ("WARNING: PMID:301" in result.stderr) is warned


def test_wrapper_honours_cache_dir_option(tmp_path: Path):
    cache = tmp_path / "elsewhere"
    cache.mkdir()
    _write_cache(cache, "PMID:302", "unavailable")
    env = _fake_uv(tmp_path)

    result = _run_wrapper(tmp_path, env, "PMID:302", "--cache-dir", str(cache))

    assert result.returncode == 0
    assert "WARNING: PMID:302" in result.stderr


def test_wrapper_keeps_validator_exit_code_and_skips_warning_on_failure(
    tmp_path: Path,
):
    cache = tmp_path / "references_cache"
    cache.mkdir()
    _write_cache(cache, "PMID:303", "unavailable")
    env = _fake_uv(tmp_path, validator_exit=3)

    result = _run_wrapper(tmp_path, env, "PMID:303")

    assert result.returncode == 3
    assert "WARNING" not in result.stderr


def test_wrapper_warning_can_be_disabled(tmp_path: Path):
    cache = tmp_path / "references_cache"
    cache.mkdir()
    _write_cache(cache, "PMID:304", "unavailable")
    env = {**_fake_uv(tmp_path), "DISMECH_SKIP_EMPTY_CACHE_WARNING": "1"}

    result = _run_wrapper(tmp_path, env, "PMID:304")

    assert result.returncode == 0
    assert "WARNING" not in result.stderr
