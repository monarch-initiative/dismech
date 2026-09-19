"""A report that fell back is named for the provider that actually wrote it.

The provider lives in the filename and `scripts/deep_research_coverage.py` reads
it back out of there, so a fallback that left the name alone would make
`just research-status` report coverage the repository does not have.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from dismech.research_reports import (
    AlignmentError,
    align_report_provider,
    read_frontmatter,
    retarget_path,
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
