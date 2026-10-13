"""A report that fell back is named for the provider that actually wrote it.

The provider lives in the filename and `scripts/deep_research_coverage.py` reads
it back out of there, so a fallback that left the name alone would make
`just research-status` report coverage the repository does not have.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from dismech.research_reports import (
    AlignmentError,
    align_report_provider,
    place_report,
    read_frontmatter,
    retarget_path,
    strip_run_suffix,
)

ROOT = Path(__file__).parent.parent
JUSTFILE = (ROOT / "project.justfile").read_text()

FELL_BACK_FRONTMATTER = """---
provider: claude_code
fell_back: true
requested_provider: falcon
artifacts:
- path: {stem}_artifacts/artifact-00.md
---

# Report

See [the artifact]({stem}_artifacts/artifact-00.md).
"""

CLEAN_FRONTMATTER = """---
provider: falcon
citation_count: 3
---

# Report
"""


def write_report(
    directory: Path, name: str, body: str, *, artifacts: bool = False
) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    report = directory / name
    report.write_text(body.format(stem=report.stem), encoding="utf-8")
    report.with_name(f"{report.name}.citations.md").write_text(
        "cites\n", encoding="utf-8"
    )
    if artifacts:
        artifact_dir = directory / f"{report.stem}_artifacts"
        artifact_dir.mkdir()
        (artifact_dir / "artifact-00.md").write_text("artifact\n", encoding="utf-8")
    return report


def test_a_report_that_did_not_fall_back_is_left_alone(tmp_path: Path) -> None:
    """The common case: nothing moves, and nothing is reported."""
    report = write_report(tmp_path, "Foo-deep-research-falcon.md", CLEAN_FRONTMATTER)

    alignment = align_report_provider(report, "falcon")

    assert not alignment.fell_back
    assert alignment.report == report
    assert report.exists()


def test_a_mismatched_name_alone_does_not_trigger_a_rename(tmp_path: Path) -> None:
    """`edison` is an alias for `falcon`, and that must not read as a fallback.

    `just research-disorder edison Foo` writes `-edison.md` for a report whose
    provider is `falcon`; the cyberian-codex recipe writes `-cyberian-codex.md`
    for a run whose provider is `cyberian`. Renaming whenever the filename
    disagreed with the frontmatter would rewrite both.
    """
    report = write_report(tmp_path, "Foo-deep-research-edison.md", CLEAN_FRONTMATTER)

    alignment = align_report_provider(report, "edison")

    assert not alignment.fell_back
    assert report.exists()


def test_a_fallback_renames_the_report_and_its_companions(tmp_path: Path) -> None:
    report = write_report(
        tmp_path, "Foo-deep-research-falcon.md", FELL_BACK_FRONTMATTER, artifacts=True
    )

    alignment = align_report_provider(report, "falcon")

    assert alignment.fell_back
    assert alignment.actual_provider == "claude_code"
    assert alignment.requested_provider == "falcon"
    renamed = tmp_path / "Foo-deep-research-claude_code.md"
    assert alignment.report == renamed
    assert renamed.exists()
    assert (tmp_path / "Foo-deep-research-claude_code.md.citations.md").exists()
    assert (tmp_path / "Foo-deep-research-claude_code_artifacts").is_dir()
    assert not report.exists()
    assert not (tmp_path / "Foo-deep-research-falcon_artifacts").exists()


def test_artifact_links_follow_the_artifacts_directory(tmp_path: Path) -> None:
    """A renamed artifacts directory leaves broken links unless they are rewritten.

    Reports link artifacts by directory name, in the body and in the
    frontmatter `artifacts:` block.
    """
    report = write_report(
        tmp_path, "Foo-deep-research-falcon.md", FELL_BACK_FRONTMATTER, artifacts=True
    )

    alignment = align_report_provider(report, "falcon")

    text = alignment.report.read_text(encoding="utf-8")
    assert "Foo-deep-research-falcon_artifacts" not in text
    assert text.count("Foo-deep-research-claude_code_artifacts/artifact-00.md") == 2
    linked = alignment.report.parent / "Foo-deep-research-claude_code_artifacts"
    assert (linked / "artifact-00.md").exists()


def test_the_frontmatter_provider_wins_over_the_requested_slug(tmp_path: Path) -> None:
    """The rename targets the provider in the report, not a guess from the name."""
    report = write_report(
        tmp_path, "Foo-datasets-falcon.md", FELL_BACK_FRONTMATTER, artifacts=False
    )

    alignment = align_report_provider(report, "falcon")

    assert alignment.report == tmp_path / "Foo-datasets-claude_code.md"


def test_the_hypothesis_layout_renames_the_whole_stem(tmp_path: Path) -> None:
    """`kb/hypotheses/<disease>/<group>/<provider>.md` puts the slug in the stem."""
    report = write_report(tmp_path / "g", "falcon.md", FELL_BACK_FRONTMATTER)

    alignment = align_report_provider(report, "falcon")

    assert alignment.report == tmp_path / "g" / "claude_code.md"


def test_an_occupied_destination_is_refused_rather_than_overwritten(
    tmp_path: Path,
) -> None:
    """Two reports, one name: a curator decides, not a `shutil.move`."""
    report = write_report(
        tmp_path, "Foo-deep-research-falcon.md", FELL_BACK_FRONTMATTER
    )
    existing = write_report(
        tmp_path, "Foo-deep-research-claude_code.md", CLEAN_FRONTMATTER
    )
    existing_text = existing.read_text(encoding="utf-8")

    with pytest.raises(AlignmentError, match="already taken"):
        align_report_provider(report, "falcon")

    assert report.exists(), "the report that fell back must survive the refusal"
    assert existing.read_text(encoding="utf-8") == existing_text


def test_a_name_without_the_requested_slug_is_refused(tmp_path: Path) -> None:
    """Guessing which part of an unrecognised name is the provider is worse."""
    report = write_report(
        tmp_path, "Foo-deep-research-falcon.md", FELL_BACK_FRONTMATTER
    )

    with pytest.raises(AlignmentError, match="does not contain the requested provider"):
        align_report_provider(report, "openai")


def test_a_fallback_with_no_provider_is_refused(tmp_path: Path) -> None:
    report = write_report(
        tmp_path,
        "Foo-deep-research-falcon.md",
        "---\nfell_back: true\n---\n\nbody\n",
    )

    with pytest.raises(AlignmentError, match="names no provider"):
        align_report_provider(report, "falcon")


def test_dry_run_moves_nothing(tmp_path: Path) -> None:
    report = write_report(
        tmp_path, "Foo-deep-research-falcon.md", FELL_BACK_FRONTMATTER, artifacts=True
    )

    alignment = align_report_provider(report, "falcon", dry_run=True)

    assert alignment.fell_back
    assert alignment.moved
    assert report.exists()
    assert not (tmp_path / "Foo-deep-research-claude_code.md").exists()


def test_frontmatter_stops_at_the_closing_delimiter(tmp_path: Path) -> None:
    """A `---` in the body is not the end of the frontmatter block."""
    report = tmp_path / "Foo-deep-research-falcon.md"
    report.write_text(
        "---\nprovider: falcon\n---\n\nbody\n\n---\n\nprovider: not-this\n",
        encoding="utf-8",
    )

    assert read_frontmatter(report) == {"provider": "falcon"}


def test_retarget_path_replaces_only_the_trailing_slug() -> None:
    """A disease whose name contains the provider slug keeps its name."""
    path = Path("research/falcon_Fever-deep-research-falcon.md")

    assert retarget_path(path, "falcon", "openai") == Path(
        "research/falcon_Fever-deep-research-openai.md"
    )


def test_a_provider_name_that_is_a_path_is_refused(tmp_path: Path) -> None:
    """`Path.with_name` would raise ValueError, which is not one of our refusals."""
    report = write_report(
        tmp_path,
        "Foo-deep-research-falcon.md",
        "---\nprovider: ../evil\nfell_back: true\n---\n\nbody\n",
    )

    with pytest.raises(AlignmentError, match="not usable as a provider name"):
        align_report_provider(report, "falcon")

    assert report.exists()


def test_the_rename_target_is_lowercased(tmp_path: Path) -> None:
    """The repo writes provider slugs lowercase and reads them case-insensitively.

    `hypothesis_deep_research.output_file_for` lowercases when it builds a path,
    so a mixed-case rename there would produce a file a later existence check
    would not find.
    """
    report = write_report(
        tmp_path,
        "Foo-deep-research-falcon.md",
        "---\nprovider: Claude_Code\nfell_back: true\n---\n\nbody\n",
    )

    alignment = align_report_provider(report, "falcon")

    assert alignment.report == tmp_path / "Foo-deep-research-claude_code.md"
    assert alignment.actual_provider == "claude_code"


def test_every_research_recipe_aligns_the_provider_after_running() -> None:
    """A recipe that can fall back must also fix the name, or coverage lies."""
    fallback_flags = JUSTFILE.count("{{dr_fallback}}")
    alignments = JUSTFILE.count("{{dr_align}} ")

    assert fallback_flags >= 6
    assert alignments == fallback_flags, (
        "every recipe passing {{dr_fallback}} must run {{dr_align}} afterwards; "
        "a fallback without alignment leaves a report named for a provider that "
        "did not write it"
    )


def test_fallback_is_off_by_default() -> None:
    """See the justfile comment: always-on fallback breaks `run-missing`."""
    match = re.search(r'(?m)^dr_fallback := "(.*)"$', JUSTFILE)

    assert match is not None, "dr_fallback variable not found"
    assert match.group(1) == ""


def test_the_align_step_names_the_requested_provider() -> None:
    """Alignment needs the slug the recipe put in the filename, not a guess."""
    for line in JUSTFILE.splitlines():
        if "{{dr_align}}" in line and ":=" not in line:
            assert '--requested "$requested_provider"' in line, line


# --- A run never replaces an existing report (#12700) -----------------------

FALCON_BODY = """---
provider: falcon
artifacts:
- path: {stem}_artifacts/artifact-00.md
---

# The committed falcon report

See [the artifact]({stem}_artifacts/artifact-00.md).
"""


def snapshot(directory: Path) -> dict[str, str]:
    """Every file under ``directory`` with its content, for before/after checks."""
    return {
        str(path.relative_to(directory)): path.read_text(encoding="utf-8")
        for path in sorted(directory.rglob("*"))
        if path.is_file()
    }


def test_a_fallback_rerun_leaves_the_committed_report_untouched(
    tmp_path: Path,
) -> None:
    """The case from #12700, end to end through the staging step.

    `research/` already holds a falcon report with citations and artifacts. A
    new run asks for falcon, falcon fails, claude_code writes the report. The
    falcon files must not move or change, and the claude_code report must land
    under its own name with only its own artifacts.
    """
    research = tmp_path / "research"
    write_report(research, "Foo-deep-research-falcon.md", FALCON_BODY, artifacts=True)
    before = snapshot(research)

    staged = write_report(
        tmp_path / "staging",
        "Foo-deep-research-falcon.md",
        FELL_BACK_FRONTMATTER,
        artifacts=True,
    )
    (staged.parent / f"{staged.stem}_artifacts" / "artifact-00.md").write_text(
        "claude_code artifact\n", encoding="utf-8"
    )

    placed = place_report(staged, research, "falcon")

    assert placed.report == research / "Foo-deep-research-claude_code.md"
    assert placed.kept_alongside is None
    after = snapshot(research)
    for name, text in before.items():
        assert after[name] == text, f"{name} was changed by the new run"
    new_artifact = (
        research / "Foo-deep-research-claude_code_artifacts" / "artifact-00.md"
    )
    assert new_artifact.read_text(encoding="utf-8") == "claude_code artifact\n"
    assert (research / "Foo-deep-research-claude_code.md.citations.md").exists()
    assert not list((tmp_path / "staging").iterdir()), "staging should be emptied"


def test_a_same_provider_rerun_is_added_beside_the_existing_report(
    tmp_path: Path,
) -> None:
    """Re-running falcon must add a second falcon report, not replace the first."""
    research = tmp_path / "research"
    write_report(research, "Foo-deep-research-falcon.md", FALCON_BODY, artifacts=True)
    before = snapshot(research)
    staged = write_report(
        tmp_path / "staging", "Foo-deep-research-falcon.md", FALCON_BODY, artifacts=True
    )

    placed = place_report(staged, research, "falcon", run_date="2026-10-08")

    dated = research / "Foo-deep-research-falcon-2026-10-08.md"
    assert placed.report == dated
    assert placed.kept_alongside == research / "Foo-deep-research-falcon.md"
    after = snapshot(research)
    for name, text in before.items():
        assert after[name] == text
    assert (research / "Foo-deep-research-falcon-2026-10-08.md.citations.md").exists()
    assert (research / "Foo-deep-research-falcon-2026-10-08_artifacts").is_dir()
    text = dated.read_text(encoding="utf-8")
    assert (
        text.count("Foo-deep-research-falcon-2026-10-08_artifacts/artifact-00.md") == 2
    )


def test_a_fallback_onto_an_existing_report_is_dated_not_refused(
    tmp_path: Path,
) -> None:
    """Both the requested and the fallback provider already have reports."""
    research = tmp_path / "research"
    write_report(research, "Foo-deep-research-falcon.md", FALCON_BODY, artifacts=True)
    write_report(research, "Foo-deep-research-claude_code.md", CLEAN_FRONTMATTER)
    before = snapshot(research)
    staged = write_report(
        tmp_path / "staging", "Foo-deep-research-falcon.md", FELL_BACK_FRONTMATTER
    )

    placed = place_report(staged, research, "falcon", run_date="2026-10-08")

    assert placed.report == research / "Foo-deep-research-claude_code-2026-10-08.md"
    after = snapshot(research)
    for name, text in before.items():
        assert after[name] == text


def test_a_second_run_on_the_same_day_gets_a_counter(tmp_path: Path) -> None:
    research = tmp_path / "research"
    write_report(research, "Foo-deep-research-falcon.md", FALCON_BODY)
    write_report(research, "Foo-deep-research-falcon-2026-10-08.md", FALCON_BODY)
    staged = write_report(
        tmp_path / "staging", "Foo-deep-research-falcon.md", FALCON_BODY
    )

    placed = place_report(staged, research, "falcon", run_date="2026-10-08")

    assert placed.report == research / "Foo-deep-research-falcon-2026-10-08-2.md"


def test_an_orphaned_artifacts_directory_also_blocks_the_name(tmp_path: Path) -> None:
    """A name is only free if no part of an old report uses it."""
    research = tmp_path / "research"
    (research / "Foo-deep-research-falcon_artifacts").mkdir(parents=True)
    staged = write_report(
        tmp_path / "staging", "Foo-deep-research-falcon.md", FALCON_BODY
    )

    placed = place_report(staged, research, "falcon", run_date="2026-10-08")

    assert placed.report == research / "Foo-deep-research-falcon-2026-10-08.md"


def test_place_report_dry_run_moves_nothing(tmp_path: Path) -> None:
    research = tmp_path / "research"
    staged = write_report(
        tmp_path / "staging", "Foo-deep-research-falcon.md", FALCON_BODY
    )

    placed = place_report(staged, research, "falcon", dry_run=True)

    assert placed.report == research / "Foo-deep-research-falcon.md"
    assert staged.exists()
    assert not research.exists()


def git(cwd: Path, *args: str) -> None:
    subprocess.run(
        ["git", "-c", "user.name=t", "-c", "user.email=t@t", *args],
        cwd=cwd,
        check=True,
        capture_output=True,
    )


@pytest.mark.skipif(shutil.which("git") is None, reason="needs git")
def test_in_place_alignment_refuses_to_sweep_up_committed_artifacts(
    tmp_path: Path,
) -> None:
    """The second half of #12700: `_sidecars` took whatever sat beside the report.

    A run overwrote a committed falcon report in place, fell back to
    claude_code, and produced no artifacts of its own. The committed falcon
    `_artifacts/` beside it is not this run's output; renaming it to
    claude_code would re-attribute it. Refuse, and move nothing.
    """
    git(tmp_path, "init", "-q")
    report = write_report(
        tmp_path, "Foo-deep-research-falcon.md", FALCON_BODY, artifacts=True
    )
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "-q", "-m", "falcon report")

    report.write_text(FELL_BACK_FRONTMATTER.format(stem=report.stem), encoding="utf-8")

    with pytest.raises(AlignmentError, match="committed and unchanged"):
        align_report_provider(report, "falcon")

    assert report.exists()
    assert (tmp_path / "Foo-deep-research-falcon_artifacts" / "artifact-00.md").exists()
    assert not (tmp_path / "Foo-deep-research-claude_code.md").exists()


@pytest.mark.skipif(shutil.which("git") is None, reason="needs git")
def test_in_place_alignment_still_moves_files_the_run_rewrote(tmp_path: Path) -> None:
    """The hypothesis runner overwrites tracked files deliberately; that is allowed."""
    git(tmp_path, "init", "-q")
    report = write_report(tmp_path / "g", "falcon.md", FALCON_BODY)
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "-q", "-m", "falcon report")

    report.write_text(FELL_BACK_FRONTMATTER.format(stem=report.stem), encoding="utf-8")
    report.with_name("falcon.md.citations.md").write_text(
        "new cites\n", encoding="utf-8"
    )

    alignment = align_report_provider(report, "falcon")

    assert alignment.report == tmp_path / "g" / "claude_code.md"


def test_strip_run_suffix() -> None:
    assert strip_run_suffix("claude_code-2026-07-30") == "claude_code"
    assert strip_run_suffix("falcon-2026-10-08-3") == "falcon"
    assert strip_run_suffix("cyberian-codex") == "cyberian-codex"


def test_coverage_counts_a_dated_report_under_its_provider() -> None:
    sys.path.insert(0, str(ROOT / "scripts"))
    try:
        import deep_research_coverage
    finally:
        sys.path.pop(0)

    parsed = deep_research_coverage.parse_research_filename(
        Path("research/Fountain_Syndrome-deep-research-claude_code-2026-07-30.md")
    )

    assert parsed == ("Fountain_Syndrome", "claude_code")


def test_no_research_recipe_lets_the_client_write_into_research() -> None:
    """The client writes to staging; only `{{dr_align}} --into` touches research/."""
    assert '--output "$output_file"' not in JUSTFILE
    assert JUSTFILE.count('--output "$staged_file"') >= 6
    for line in JUSTFILE.splitlines():
        if (
            "{{dr_align}}" in line
            and ":=" not in line
            and not line.lstrip().startswith("#")
        ):
            assert (
                '"$staged_file"' in line
                and '--into "$(dirname "$output_file")"' in line
            ), line
