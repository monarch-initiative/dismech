"""A hypothesis exploration must resolve to the entry whose hypothesis it explores.

``render.collect_hypothesis_research_links`` performs two verbatim name matches
and has no fallback for either: the directory under ``kb/hypotheses/`` must be
named for the entry's filename stem, and each subdirectory must be named for a
``hypothesis_group_id`` that entry declares. A mismatch is silent to every other
check in the repo, and its only symptom is an absence on the rendered page.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

import pytest

from scripts.check_hypothesis_links import collect


def _entry(kb: Path, slug: str, ids: list[str]) -> None:
    (kb / "disorders").mkdir(parents=True, exist_ok=True)
    blocks = "\n".join(
        textwrap.dedent(
            f"""\
            - hypothesis_group_id: {i}
              hypothesis_label: Label for {i}
              status: CANONICAL
            """
        )
        for i in ids
    )
    body = f"name: {slug}\ncategory: Disease\n"
    if ids:
        body += f"mechanistic_hypotheses:\n{blocks}"
    (kb / "disorders" / f"{slug}.yaml").write_text(body, encoding="utf-8")


def _report(kb: Path, slug: str, hypothesis_id: str) -> None:
    d = kb / "hypotheses" / slug / hypothesis_id
    d.mkdir(parents=True, exist_ok=True)
    (d / "openscientist.md").write_text(
        "---\nprovider: openscientist\n---\n", encoding="utf-8"
    )


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    for sub in ("disorders", "modules", "comorbidities", "groupings", "hypotheses"):
        (tmp_path / "kb" / sub).mkdir(parents=True)
    return tmp_path


def test_matching_directory_and_id_is_clean(repo: Path) -> None:
    _entry(repo / "kb", "Long_COVID", ["canonical_persistence_immune_model"])
    _report(repo / "kb", "Long_COVID", "canonical_persistence_immune_model")
    assert collect(repo) == []


def test_directory_naming_no_entry_is_reported(repo: Path) -> None:
    """The Huntington case: the entry is Huntington_Disease, the directory is not."""
    _entry(repo / "kb", "Huntington_Disease", ["alternative_excitotoxicity"])
    _report(repo / "kb", "Huntingtons_Disease", "alternative_excitotoxicity")

    findings = collect(repo)
    assert [f.kind for f in findings] == ["no_entry"]
    assert "Huntingtons_Disease" in findings[0].directory
    # the hint must actually name the entry a curator should rename to
    assert "Huntington_Disease" in findings[0].detail


def test_undeclared_hypothesis_id_is_reported(repo: Path) -> None:
    """The HMGCS2 case: curation renamed the id, the directory kept the old one."""
    _entry(
        repo / "kb", "HMGCS2_Deficiency", ["canonical_human_hmgcs2_ketogenesis_failure"]
    )
    _report(
        repo / "kb", "HMGCS2_Deficiency", "canonical_hmgcs2_ketogenesis_failure_model"
    )

    findings = collect(repo)
    assert [f.kind for f in findings] == ["undeclared_id"]
    # the message must list what the entry does declare, so the fix is obvious
    assert "canonical_human_hmgcs2_ketogenesis_failure" in findings[0].detail


def test_directory_without_a_report_is_ignored(repo: Path) -> None:
    """Only a directory holding a real report can render, so only it can fail."""
    _entry(repo / "kb", "Long_COVID", ["declared_model"])
    empty = repo / "kb" / "hypotheses" / "Long_COVID" / "undeclared_but_empty"
    empty.mkdir(parents=True)
    (empty / "openscientist.md.citations.md").write_text("x", encoding="utf-8")
    assert collect(repo) == []


def test_module_and_grouping_entries_also_resolve(repo: Path) -> None:
    """Modules carry mechanistic_hypotheses too, so they are valid targets."""
    (repo / "kb" / "modules" / "deregulated_nutrient_sensing.yaml").write_text(
        "name: x\nmechanistic_hypotheses:\n- hypothesis_group_id: m1\n",
        encoding="utf-8",
    )
    _report(repo / "kb", "deregulated_nutrient_sensing", "m1")
    assert collect(repo) == []


def test_committed_kb_has_no_disconnected_hypothesis_directories() -> None:
    """The real tree must stay clean; this is the regression guard."""
    root = Path(__file__).resolve().parents[1]
    findings = collect(root)
    assert findings == [], "\n".join(f"{f.directory}: {f.detail}" for f in findings)
