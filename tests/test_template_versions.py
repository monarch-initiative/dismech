"""Tests for research-template revision identification (issue #10183)."""

from __future__ import annotations

import os
import subprocess
from datetime import UTC, datetime
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


def git(repo: Path, *args: str, when: str | None = None) -> str:
    """Run git in `repo` and return stdout.

    Args:
        repo: Working directory.
        args: Arguments after ``git``.
        when: Commit timestamp to force. Sets both the author and *committer*
            dates -- ``git commit --date`` moves only the author date, while
            :func:`template_history` reads the committer date, which is when the
            revision actually landed and so when it was in effect for anyone
            running a research recipe.
    """
    env = None
    if when is not None:
        env = {**os.environ, "GIT_AUTHOR_DATE": when, "GIT_COMMITTER_DATE": when}
    return subprocess.run(
        ["git", *args],
        cwd=repo,
        capture_output=True,
        text=True,
        check=True,
        env=env,
    ).stdout


@pytest.fixture
def repo_with_two_revisions(tmp_path: Path) -> tuple[Path, str, str]:
    """A git repo whose template has two committed revisions.

    Built rather than borrowed from the repository under test: CI checks out
    with ``actions/checkout``'s default ``fetch-depth: 1``, so the real
    repository has exactly one commit there and any test asserting on multi-
    revision history would pass locally and fail in CI.

    Returns:
        The repo root, the older blob hash, and the newer one.
    """
    repo = tmp_path / "repo"
    (repo / "templates").mkdir(parents=True)
    git(repo.parent, "init", "--quiet", str(repo))
    git(repo, "config", "user.email", "test@example.com")
    git(repo, "config", "user.name", "Test")

    template = repo / "templates" / "prompt.md"
    template.write_text("first revision\n", encoding="utf-8")
    git(repo, "add", "templates/prompt.md")
    git(
        repo,
        "commit",
        "--quiet",
        "-m",
        "add template",
        when="2026-01-01T00:00:00+00:00",
    )
    old = blob_sha(template)

    template.write_text("second revision, asks for a causal chain\n", encoding="utf-8")
    git(repo, "add", "templates/prompt.md")
    git(
        repo, "commit", "--quiet", "-m", "restructure", when="2026-06-01T00:00:00+00:00"
    )
    new = blob_sha(template)

    return repo, old, new


def shallow(repo: Path = REPO_ROOT) -> bool:
    """Whether `repo` is a shallow clone, as CI's checkout is."""
    try:
        return git(repo, "rev-parse", "--is-shallow-repository").strip() == "true"
    except subprocess.SubprocessError:  # pragma: no cover - git always present
        return False


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


def test_stamp_when_template_file_is_the_last_frontmatter_line(
    tmp_path: Path,
) -> None:
    """The boundary the frontmatter-bounded splice got wrong first time.

    The newline before the closing delimiter is also the newline that ends the
    last key line, so an end-exclusive search for it finds nothing and the
    stamp is silently skipped.
    """
    template = tmp_path / "templates" / "t.md"
    template.parent.mkdir()
    template.write_text("prompt\n", encoding="utf-8")
    report = write_report(
        tmp_path / "r.md",
        provider="falcon",
        template_file="templates/t.md",  # deliberately last
    )

    written = stamp_report(report, repo_root=tmp_path)

    assert written == blob_sha(template)
    assert resolve_report(report).blob == written


def test_stamp_ignores_a_template_file_line_in_the_body(tmp_path: Path) -> None:
    """The splice must land in the frontmatter, never in prose below it."""
    template = tmp_path / "templates" / "t.md"
    template.parent.mkdir()
    template.write_text("prompt\n", encoding="utf-8")
    report = tmp_path / "r.md"
    report.write_text(
        "---\n"
        "provider: falcon\n"
        "template_file: templates/t.md\n"
        "---\n"
        "\n"
        "# Body\n"
        "\n"
        "The report mentions template_file: something/else.md in prose.\n",
        encoding="utf-8",
    )

    stamp_report(report, repo_root=tmp_path)

    # Readable back through the frontmatter parser, which only sees the block.
    assert resolve_report(report).blob == blob_sha(template)
    body = report.read_text(encoding="utf-8").split("---\n", 2)[2]
    assert "template_sha" not in body


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


def test_windows_separators_resolve_to_the_same_template(
    repo_with_two_revisions: tuple[Path, str, str], tmp_path: Path
) -> None:
    """Twenty committed reports record the path with backslashes (#10183)."""
    repo, old_blob, _ = repo_with_two_revisions
    forward = write_report(
        tmp_path / "a.md",
        template_file="templates/prompt.md",
        start_time="'2026-03-15T12:00:00'",
    )
    backward = write_report(
        tmp_path / "b.md",
        template_file="templates\\prompt.md",
        start_time="'2026-03-15T12:00:00'",
    )

    resolved_forward = resolve_report(forward, repo_root=str(repo))
    resolved_backward = resolve_report(backward, repo_root=str(repo))

    assert resolved_forward.template == resolved_backward.template
    assert resolved_backward.blob == old_blob, "must resolve, not merely tie at None"


def test_report_predating_first_commit_is_unknown_not_wrong(
    repo_with_two_revisions: tuple[Path, str, str], tmp_path: Path
) -> None:
    """Never attribute a report to a revision that did not exist yet."""
    repo, _, _ = repo_with_two_revisions
    report = write_report(
        tmp_path / "r.md",
        template_file="templates/prompt.md",
        start_time="'1999-01-01T00:00:00'",
    )

    resolution = resolve_report(report, repo_root=str(repo))

    assert resolution.provenance is Provenance.UNKNOWN
    assert resolution.blob is None


def test_zulu_start_time_still_parses(
    repo_with_two_revisions: tuple[Path, str, str], tmp_path: Path
) -> None:
    """`fromisoformat` handles a trailing `Z` natively from 3.11 (we need 3.12).

    The explicit `.replace("Z", "+00:00")` this once carried was dead weight,
    but removing it changes parsing, so pin the behaviour rather than assume it.
    """
    repo, old_blob, _ = repo_with_two_revisions
    report = write_report(
        tmp_path / "r.md",
        template_file="templates/prompt.md",
        start_time="'2026-03-15T12:00:00Z'",
    )

    resolution = resolve_report(report, repo_root=str(repo))

    assert resolution.provenance is Provenance.INFERRED
    assert resolution.blob == old_blob


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


def test_iter_reports_recurses_into_report_subdirectories(tmp_path: Path) -> None:
    """`modules/`, `groupings/`, `surrogacy/` and `datasets/` hold reports too.

    A top-level-only glob reports a corpus census while silently omitting them.
    """
    (tmp_path / "Top-deep-research-falcon.md").write_text(
        "---\n---\n", encoding="utf-8"
    )
    for sub in ("modules", "groupings", "surrogacy", "datasets"):
        (tmp_path / sub).mkdir()
        (tmp_path / sub / f"{sub}-report.md").write_text("---\n---\n", encoding="utf-8")

    found = {p.name for p in iter_reports(tmp_path)}

    assert found == {
        "Top-deep-research-falcon.md",
        "modules-report.md",
        "groupings-report.md",
        "surrogacy-report.md",
        "datasets-report.md",
    }


def test_iter_reports_skips_provider_artifact_directories(tmp_path: Path) -> None:
    """Artifacts sit beside a report but are not reports.

    They outnumber real nested reports by roughly 60 to 1, so including them
    would swamp the census with rows that can never carry a `template_file`.
    """
    (tmp_path / "X-deep-research-falcon.md").write_text("---\n---\n", encoding="utf-8")
    artifacts = tmp_path / "X-deep-research-falcon_artifacts"
    artifacts.mkdir()
    (artifacts / "artifact-00.md").write_text("a table", encoding="utf-8")
    nested = artifacts / "deeper"
    nested.mkdir()
    (nested / "artifact-01.md").write_text("another", encoding="utf-8")

    found = [p.name for p in iter_reports(tmp_path)]

    assert found == ["X-deep-research-falcon.md"]


def test_template_history_is_ordered_newest_first(
    repo_with_two_revisions: tuple[Path, str, str],
) -> None:
    repo, old, new = repo_with_two_revisions

    history = template_history("templates/prompt.md", str(repo))

    assert [revision.blob for revision in history] == [new, old]
    dates = [revision.committed_at for revision in history]
    assert dates == sorted(dates, reverse=True)
    assert all(len(revision.blob) == 40 for revision in history)


def test_inference_picks_the_revision_in_effect_when_the_report_ran(
    repo_with_two_revisions: tuple[Path, str, str], tmp_path: Path
) -> None:
    """Between two revisions, a report belongs to the older one."""
    repo, old, new = repo_with_two_revisions
    between = write_report(
        tmp_path / "between.md",
        template_file="templates/prompt.md",
        start_time="'2026-03-15T12:00:00'",
    )
    after = write_report(
        tmp_path / "after.md",
        template_file="templates/prompt.md",
        start_time="'2026-09-15T12:00:00'",
    )

    assert resolve_report(between, repo_root=str(repo)).blob == old
    assert (
        resolve_report(between, repo_root=str(repo)).provenance is Provenance.INFERRED
    )
    assert resolve_report(after, repo_root=str(repo)).blob == new


def test_history_for_unknown_path_is_empty_not_an_error() -> None:
    """An uncommitted template is an ordinary state, not a failure."""
    assert template_history("templates/does_not_exist.md", str(REPO_ROOT)) == ()


@pytest.mark.skipif(
    shallow(), reason="a shallow checkout has no template history to resolve against"
)
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


def test_naive_start_time_is_treated_as_utc(
    repo_with_two_revisions: tuple[Path, str, str], tmp_path: Path
) -> None:
    """Reports record naive timestamps, so the comparison must not crash.

    Git dates are timezone-aware; comparing them against a naive datetime
    raises, and every committed report records a naive `start_time`.
    """
    repo, old_blob, _ = repo_with_two_revisions
    report = write_report(
        tmp_path / "r.md",
        template_file="templates/prompt.md",
        start_time="'2026-03-15T11:45:54.659338'",
    )

    resolution = resolve_report(report, repo_root=str(repo))

    assert resolution.provenance is Provenance.INFERRED
    assert resolution.blob == old_blob


@pytest.mark.skipif(
    shallow(), reason="a shallow checkout has no template history to resolve against"
)
def test_history_dates_are_timezone_aware() -> None:
    """Comparing aware and naive datetimes raises; guard the invariant."""
    history = template_history(
        "templates/disease_pathophysiology_research.md", str(REPO_ROOT)
    )
    assert history
    for revision in history:
        assert revision.committed_at.tzinfo is not None
        assert revision.committed_at.astimezone(UTC) <= datetime.now(UTC)
