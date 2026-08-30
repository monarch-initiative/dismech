"""Tests for research-template revision identification (issue #10183)."""

from __future__ import annotations

import subprocess
from datetime import datetime, timezone
from pathlib import Path

import pytest

from dismech.template_versions import (
    Provenance,
    blob_sha,
    iter_reports,
    resolve_report,
    stamp_report,
    template_history,
)

REPO_ROOT = Path(__file__).resolve().parents[1]


def write_report(path: Path, **frontmatter: object) -> Path:
    """Write a minimal report carrying the given frontmatter."""
    lines = ["---"]
    for key, value in frontmatter.items():
        lines.append(f"{key}: {value}")
    lines.extend(["---", "", "# Body", "", "Some content.", ""])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def test_blob_sha_matches_git_hash_object(tmp_path: Path) -> None:
    """Our hash must be git's, or a stamp cannot be looked up in git history."""
    target = tmp_path / "template.md"
    target.write_text("Ask for a causal chain.\n", encoding="utf-8")

    expected = subprocess.run(
        ["git", "hash-object", str(target)],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()

    assert blob_sha(target) == expected


def test_blob_sha_of_empty_file_matches_git(tmp_path: Path) -> None:
    """The zero-length case is the one a hand-rolled hash usually gets wrong."""
    target = tmp_path / "empty.md"
    target.write_bytes(b"")

    expected = subprocess.run(
        ["git", "hash-object", str(target)],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()

    assert blob_sha(target) == expected


def test_stamp_writes_blob_hash_and_keeps_frontmatter_parseable(tmp_path: Path) -> None:
    template = tmp_path / "templates" / "t.md"
    template.parent.mkdir()
    template.write_text("prompt\n", encoding="utf-8")
    report = write_report(
        tmp_path / "r.md",
        provider="falcon",
        template_file="templates/t.md",
    )

    written = stamp_report(report, repo_root=tmp_path)

    assert written == blob_sha(template)
    assert resolve_report(report).blob == written


def test_stamp_is_idempotent(tmp_path: Path) -> None:
    """Re-running a recipe must not rewrite provenance already recorded."""
    template = tmp_path / "templates" / "t.md"
    template.parent.mkdir()
    template.write_text("prompt\n", encoding="utf-8")
    report = write_report(
        tmp_path / "r.md", provider="falcon", template_file="templates/t.md"
    )

    first = stamp_report(report, repo_root=tmp_path)
    template.write_text("a different prompt entirely\n", encoding="utf-8")
    second = stamp_report(report, repo_root=tmp_path)

    assert first is not None
    assert second is None, "an existing stamp must not be overwritten"
    assert resolve_report(report).blob == first


@pytest.mark.parametrize(
    "frontmatter",
    [
        {"provider": "falcon"},
        {"provider": "falcon", "template_file": "templates/missing.md"},
        {"provider": "falcon", "template_file": "manual_curation"},
    ],
    ids=["no-template-file", "template-not-on-disk", "free-text-label"],
)
def test_stamp_declines_rather_than_guessing(
    tmp_path: Path, frontmatter: dict[str, str]
) -> None:
    """Refusing to stamp is the honest outcome; inventing a hash is not."""
    report = write_report(tmp_path / "r.md", **frontmatter)
    assert stamp_report(report, repo_root=tmp_path) is None


def test_stamped_beats_inferred(tmp_path: Path) -> None:
    """A recorded hash is authoritative even when a timestamp would disagree."""
    report = write_report(
        tmp_path / "r.md",
        template_file="templates/disease_pathophysiology_research.md",
        start_time="'2020-01-01T00:00:00'",
        template_sha='"deadbeef' + "0" * 32 + '"',
    )

    resolution = resolve_report(report)

    assert resolution.provenance is Provenance.STAMPED
    assert resolution.blob == "deadbeef" + "0" * 32


def test_all_digit_hash_survives_a_write_read_round_trip(tmp_path: Path) -> None:
    """A bare all-digit stamp would load as an int and lose its leading zeros.

    Blob hashes are hex, so an all-digit one is rare rather than impossible.
    The writer quotes the value for this reason; this test is what keeps it
    quoted.
    """
    template = tmp_path / "templates" / "t.md"
    template.parent.mkdir()
    template.write_text("prompt\n", encoding="utf-8")
    report = write_report(
        tmp_path / "r.md", provider="falcon", template_file="templates/t.md"
    )
    stamp_report(report, repo_root=tmp_path)

    # Swap in an all-digit hash the way the writer would have emitted it.
    digits = "0123456789" * 4
    text = report.read_text(encoding="utf-8")
    start = text.index("template_sha:")
    end = text.index("\n", start)
    report.write_text(
        text[:start] + f'template_sha: "{digits}"' + text[end:], encoding="utf-8"
    )

    assert resolve_report(report).blob == digits


def test_windows_separators_resolve_to_the_same_template(tmp_path: Path) -> None:
    """Twenty committed reports record the path with backslashes (#10183)."""
    forward = write_report(
        tmp_path / "a.md",
        template_file="templates/disease_pathophysiology_research.md",
        start_time="'2026-06-19T11:45:54'",
    )
    backward = write_report(
        tmp_path / "b.md",
        template_file="templates\\disease_pathophysiology_research.md",
        start_time="'2026-06-19T11:45:54'",
    )

    assert resolve_report(forward).template == resolve_report(backward).template
    assert resolve_report(forward).blob == resolve_report(backward).blob


def test_report_predating_first_commit_is_unknown_not_wrong(tmp_path: Path) -> None:
    """Never attribute a report to a revision that did not exist yet."""
    report = write_report(
        tmp_path / "r.md",
        template_file="templates/disease_pathophysiology_research.md",
        start_time="'1999-01-01T00:00:00'",
    )

    resolution = resolve_report(report)

    assert resolution.provenance is Provenance.UNKNOWN
    assert resolution.blob is None


def test_missing_start_time_is_unknown(tmp_path: Path) -> None:
    report = write_report(
        tmp_path / "r.md",
        template_file="templates/disease_pathophysiology_research.md",
    )
    assert resolve_report(report).provenance is Provenance.UNKNOWN


def test_is_current_distinguishes_undetermined_from_stale() -> None:
    """`None` must not collapse into `False`, or every unknown reads as stale."""
    from dismech.template_versions import Resolution

    known = Resolution(Path("r.md"), "t.md", "abc", Provenance.INFERRED)
    unknown = Resolution(Path("r.md"), "t.md", None, Provenance.UNKNOWN)

    assert known.is_current("abc") is True
    assert known.is_current("def") is False
    assert unknown.is_current("abc") is None
    assert known.is_current(None) is None


def test_iter_reports_excludes_citation_sidecars(tmp_path: Path) -> None:
    """Sidecars are `<report>.md.citations.md` -- a doubled `.md`."""
    (tmp_path / "X-deep-research-falcon.md").write_text("---\n---\n", encoding="utf-8")
    (tmp_path / "X-deep-research-falcon.md.citations.md").write_text(
        "x", encoding="utf-8"
    )

    found = [p.name for p in iter_reports(tmp_path)]

    assert found == ["X-deep-research-falcon.md"]


def test_template_history_is_ordered_newest_first() -> None:
    history = template_history(
        "templates/disease_pathophysiology_research.md", str(REPO_ROOT)
    )

    assert len(history) >= 2, "the disease template has several committed revisions"
    dates = [revision.committed_at for revision in history]
    assert dates == sorted(dates, reverse=True)
    assert all(len(revision.blob) == 40 for revision in history)


def test_history_for_unknown_path_is_empty_not_an_error() -> None:
    """An uncommitted template is an ordinary state, not a failure."""
    assert template_history("templates/does_not_exist.md", str(REPO_ROOT)) == ()


def test_current_disease_template_resolves_to_its_own_blob() -> None:
    """End to end against the real repository."""
    template = REPO_ROOT / "templates" / "disease_pathophysiology_research.md"
    history = template_history(
        "templates/disease_pathophysiology_research.md", str(REPO_ROOT)
    )

    assert history, "expected committed history for the disease template"
    assert history[0].blob == blob_sha(template), (
        "HEAD's committed blob should match the file on disk; a mismatch means "
        "the working tree has uncommitted template edits"
    )


def test_naive_start_time_is_treated_as_utc(tmp_path: Path) -> None:
    """Reports record naive timestamps, so the comparison must not crash."""
    report = write_report(
        tmp_path / "r.md",
        template_file="templates/disease_pathophysiology_research.md",
        start_time="'2026-06-19T11:45:54.659338'",
    )

    resolution = resolve_report(report)

    assert resolution.provenance is Provenance.INFERRED
    assert resolution.blob is not None


def test_history_dates_are_timezone_aware() -> None:
    """Comparing aware and naive datetimes raises; guard the invariant."""
    history = template_history(
        "templates/disease_pathophysiology_research.md", str(REPO_ROOT)
    )
    assert history
    for revision in history:
        assert revision.committed_at.tzinfo is not None
        assert revision.committed_at.astimezone(timezone.utc) <= datetime.now(
            timezone.utc
        )
