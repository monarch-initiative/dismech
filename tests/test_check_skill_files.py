"""Tests for the ``.claude/skills/`` well-formedness gate (issue #11758).

The defect this exists for is silent: a skill whose file is named ``skill.md``
rather than ``SKILL.md`` is simply not loaded, with no error anywhere. So the
first test below reproduces exactly that, and the last one asserts the committed
corpus is clean -- which is what makes this a gate that sits green rather than a
backlog.
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "check_skill_files",
    Path(__file__).resolve().parents[1] / "scripts" / "check_skill_files.py",
)
check_skill_files = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = check_skill_files
_SPEC.loader.exec_module(check_skill_files)

check_skill = check_skill_files.check_skill
split_frontmatter = check_skill_files.split_frontmatter
skill_directories = check_skill_files.skill_directories

VALID = """---
name: {name}
description: What this skill is for and when to reach for it.
---

# Body
"""


def _write_skill(tmp_path: Path, name: str, *, filename: str = "SKILL.md", body: str | None = None):
    directory = tmp_path / name
    directory.mkdir()
    (directory / filename).write_text(body if body is not None else VALID.format(name=name))
    return directory


def test_wellformed_skill_has_no_findings(tmp_path):
    findings, frontmatter = check_skill(_write_skill(tmp_path, "curate-grouping"))
    assert findings == []
    assert frontmatter["name"] == "curate-grouping"


def test_lowercase_filename_is_reported_as_miscased(tmp_path):
    """The real #11758 defect: the file is there, under the wrong name."""
    directory = _write_skill(tmp_path, "microbiome-curation", filename="skill.md")
    findings, frontmatter = check_skill(directory)
    assert [f.kind for f in findings] == ["miscased_skill_file"]
    assert "skill.md" in findings[0].detail
    assert frontmatter is None


def test_absent_skill_file_is_distinguished_from_a_miscased_one(tmp_path):
    directory = tmp_path / "empty-skill"
    directory.mkdir()
    findings, _ = check_skill(directory)
    assert [f.kind for f in findings] == ["missing_skill_file"]


def test_name_not_matching_the_directory_is_reported(tmp_path):
    directory = _write_skill(tmp_path, "curate-grouping", body=VALID.format(name="curate-groupings"))
    findings, _ = check_skill(directory)
    assert [f.kind for f in findings] == ["name_mismatch"]


def test_uppercase_name_is_reported_as_malformed(tmp_path):
    """A name is how the skill is addressed, so its form is not cosmetic."""
    directory = tmp_path / "Curate-Grouping"
    directory.mkdir()
    (directory / "SKILL.md").write_text(VALID.format(name="Curate-Grouping"))
    findings, _ = check_skill(directory)
    assert [f.kind for f in findings] == ["malformed_name"]


def test_empty_description_is_reported(tmp_path):
    body = "---\nname: boss\ndescription: '   '\n---\n\n# Body\n"
    findings, _ = check_skill(_write_skill(tmp_path, "boss", body=body))
    assert [f.kind for f in findings] == ["missing_description"]


def test_missing_description_key_is_reported(tmp_path):
    findings, _ = check_skill(_write_skill(tmp_path, "boss", body="---\nname: boss\n---\n\n# Body\n"))
    assert [f.kind for f in findings] == ["missing_description"]


def test_unparsable_frontmatter_is_reported(tmp_path):
    body = "---\nname: boss\ndescription: [unclosed\n---\n\n# Body\n"
    findings, frontmatter = check_skill(_write_skill(tmp_path, "boss", body=body))
    assert [f.kind for f in findings] == ["unparsable_frontmatter"]
    assert frontmatter is None


def test_body_without_frontmatter_is_reported(tmp_path):
    findings, _ = check_skill(_write_skill(tmp_path, "boss", body="# Just a heading\n"))
    assert [f.kind for f in findings] == ["missing_frontmatter"]


def test_unterminated_frontmatter_fence_is_not_frontmatter(tmp_path):
    findings, _ = check_skill(_write_skill(tmp_path, "boss", body="---\nname: boss\n\n# Body\n"))
    assert [f.kind for f in findings] == ["missing_frontmatter"]


def test_split_frontmatter_returns_only_the_fenced_block():
    assert split_frontmatter("---\na: 1\n---\nbody\n---\nmore\n") == "a: 1"
    assert split_frontmatter("no fence\n") is None


def test_committed_skills_are_all_wellformed():
    """The corpus is clean, so the gate is green rather than a backlog."""
    directories = skill_directories()
    assert directories, "expected skill directories under .claude/skills/"
    findings = [f for directory in directories for f in check_skill(directory)[0]]
    assert findings == [], "\n".join(f"{f.location}: {f.kind}: {f.detail}" for f in findings)


def test_cli_passes_on_the_committed_tree():
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "scripts/check_skill_files.py"],
        cwd=root,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_reference_scan_flags_a_justfile_path_that_no_longer_exists(tmp_path):
    """`project.justfile` runs a script inside a skill; moving it must not go quiet."""
    (tmp_path / "project.justfile").write_text(
        "sync:\n    uv run python .claude/skills/projman/scripts/sync_epic.py\n"
    )
    findings = check_skill_files.check_references(root=tmp_path)
    assert [f.kind for f in findings] == ["missing_referenced_path"]
    assert "sync_epic.py" in findings[0].detail

    target = tmp_path / ".claude" / "skills" / "projman" / "scripts"
    target.mkdir(parents=True)
    (target / "sync_epic.py").write_text("")
    assert check_skill_files.check_references(root=tmp_path) == []


def test_committed_skill_references_all_resolve():
    assert check_skill_files.check_references() == []


def test_miscasing_is_caught_even_on_a_case_insensitive_filesystem(tmp_path, monkeypatch):
    """macOS answers `is_file()` True for skill.md, so presence comes from the listing.

    Without this, the gate passes on a curator's Mac for exactly the defect it
    exists to catch, and only CI (Linux) disagrees.
    """
    directory = _write_skill(tmp_path, "microbiome-curation", filename="skill.md")
    monkeypatch.setattr(Path, "is_file", lambda self: self.exists() or self.name == "SKILL.md")
    findings, _ = check_skill(directory)
    assert [f.kind for f in findings] == ["miscased_skill_file"]


def test_elisions_and_the_bare_directory_are_not_treated_as_references(tmp_path):
    """These resolve only because `.claude/skills/` exists — not a real check."""
    (tmp_path / "project.justfile").write_text(
        "# see .claude/skills/... and .claude/skills/ for details\n"
    )
    assert check_skill_files.check_references(root=tmp_path) == []


def test_composite_actions_are_scanned(tmp_path):
    action = tmp_path / ".github" / "actions" / "resolve-agent-config"
    action.mkdir(parents=True)
    (action / "action.yml").write_text(
        "runs:\n  steps:\n    - run: python .claude/skills/projman/scripts/gone.py\n"
    )
    findings = check_skill_files.check_references(root=tmp_path)
    assert [f.kind for f in findings] == ["missing_referenced_path"]
