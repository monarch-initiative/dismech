"""A hypothesis exploration must resolve to the entry whose hypothesis it explores.

``render.collect_hypothesis_research_links`` performs two verbatim name matches:
the directory under ``kb/hypotheses/`` must be named for the entry's filename
stem, and each subdirectory must be named for a ``hypothesis_group_id`` that
entry declares. ``render_disorder`` softens the first with one retry on
``slugify(name)``, fired whenever the primary lookup yields no sections -- which
happens both when the directory is missing and when it holds no report.

So a directory reached only by that retry does render, and the checker reports
it as advisory rather than failing it; only a directory reached by neither name
is unreachable. A mismatch that survives both is silent to every other check in
the repo, and its only symptom is an absence on the rendered page.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

import pytest

from scripts.check_hypothesis_links import BLOCKING_KINDS, collect, main


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


def test_directory_named_for_the_disease_name_is_advisory_not_blocking(
    repo: Path,
) -> None:
    """render_disorder retries with slugify(name), so this one does render.

    Several hundred entries have slugify(name) != file stem. Failing them
    would make this gate stricter than the renderer it guards.
    """
    kb = repo / "kb"
    (kb / "disorders" / "46_XX_Gonadal_Dysgenesis.yaml").write_text(
        "name: 46,XX Gonadal Dysgenesis\n"
        "mechanistic_hypotheses:\n"
        "- hypothesis_group_id: h1\n",
        encoding="utf-8",
    )
    _report(kb, "46,XX_Gonadal_Dysgenesis", "h1")

    findings = collect(repo)
    assert [f.kind for f in findings] == ["non_canonical_slug"]
    assert not [f for f in findings if f.kind in BLOCKING_KINDS]


def test_shadowed_directory_blocks_because_the_retry_never_runs(
    repo: Path,
) -> None:
    """The retry only fires when the file-stem lookup found nothing."""
    kb = repo / "kb"
    (kb / "disorders" / "46_XX_Gonadal_Dysgenesis.yaml").write_text(
        "name: 46,XX Gonadal Dysgenesis\n"
        "mechanistic_hypotheses:\n"
        "- hypothesis_group_id: h1\n",
        encoding="utf-8",
    )
    _report(kb, "46,XX_Gonadal_Dysgenesis", "h1")
    _report(kb, "46_XX_Gonadal_Dysgenesis", "h1")

    findings = collect(repo)
    blocking = [f for f in findings if f.kind in BLOCKING_KINDS]
    assert len(blocking) == 1
    assert "already has its own" in blocking[0].detail


def test_reportless_canonical_directory_does_not_shadow(repo: Path) -> None:
    """collect_hypothesis_research_links returns [] for a reportless directory too.

    `render_disorder` retries whenever the primary lookup yields no sections, not
    only when the directory is missing, so a canonical directory holding no
    report does not block the fallback -- and the page does render.
    """
    kb = repo / "kb"
    (kb / "disorders" / "46_XX_Gonadal_Dysgenesis.yaml").write_text(
        "name: 46,XX Gonadal Dysgenesis\n"
        "mechanistic_hypotheses:\n"
        "- hypothesis_group_id: h1\n",
        encoding="utf-8",
    )
    _report(kb, "46,XX_Gonadal_Dysgenesis", "h1")
    reportless = kb / "hypotheses" / "46_XX_Gonadal_Dysgenesis" / "h1"
    reportless.mkdir(parents=True)
    (reportless / "openscientist.md.citations.md").write_text("x", encoding="utf-8")

    findings = collect(repo)
    assert [f.kind for f in findings] == ["non_canonical_slug"]
    assert not [f for f in findings if f.kind in BLOCKING_KINDS]


def test_exit_code_is_zero_for_advisory_only(
    repo: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """An advisory must not fail CI -- that is the whole point of the split."""
    kb = repo / "kb"
    (kb / "disorders" / "46_XX_Gonadal_Dysgenesis.yaml").write_text(
        "name: 46,XX Gonadal Dysgenesis\n"
        "mechanistic_hypotheses:\n"
        "- hypothesis_group_id: h1\n",
        encoding="utf-8",
    )
    _report(kb, "46,XX_Gonadal_Dysgenesis", "h1")

    monkeypatch.setattr("sys.argv", ["check", "--repo-root", str(repo)])
    assert main() == 0
    assert "advisory finding(s); nothing unreachable" in capsys.readouterr().out


def test_exit_code_is_one_for_a_blocking_finding(
    repo: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _entry(repo / "kb", "Huntington_Disease", ["alternative_excitotoxicity"])
    _report(repo / "kb", "Huntingtons_Disease", "alternative_excitotoxicity")

    monkeypatch.setattr("sys.argv", ["check", "--repo-root", str(repo)])
    assert main() == 1


def test_report_mode_never_fails(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _entry(repo / "kb", "Huntington_Disease", ["alternative_excitotoxicity"])
    _report(repo / "kb", "Huntingtons_Disease", "alternative_excitotoxicity")

    monkeypatch.setattr("sys.argv", ["check", "--repo-root", str(repo), "--report"])
    assert main() == 0


def test_slug_collision_does_not_falsely_shadow(repo: Path) -> None:
    """Two entries can slugify to one name; only one of them can own it.

    The directory renders on the page of whichever entry lacks a canonical
    directory, so keeping just one candidate would block a rendering tree.
    """
    kb = repo / "kb"
    for stem in ("A_Variant", "B_Variant"):
        (kb / "disorders" / f"{stem}.yaml").write_text(
            "name: Foo (Bar)\nmechanistic_hypotheses:\n- hypothesis_group_id: h1\n",
            encoding="utf-8",
        )
    # A_Variant has its own directory; B_Variant does not, so B's page renders
    # Foo_Bar through the retry.
    _report(kb, "A_Variant", "h1")
    _report(kb, "Foo_Bar", "h1")

    findings = collect(repo)
    assert [f.kind for f in findings] == ["non_canonical_slug"]
    assert not [f for f in findings if f.kind in BLOCKING_KINDS]


def test_reportless_directory_is_never_a_finding(repo: Path) -> None:
    """A directory with no report has no reachability to lose."""
    kb = repo / "kb"
    _entry(kb, "Real_Entry", ["h1"])
    empty = kb / "hypotheses" / "Not_An_Entry_At_All" / "h1"
    empty.mkdir(parents=True)
    (empty / "openscientist.md.citations.md").write_text("x", encoding="utf-8")

    assert collect(repo) == []


@pytest.mark.parametrize(
    ("header", "label"),
    [
        ("name: >-\n  Folded Real Name\n", "folded header"),
        ("name: Folded Real Name  # legacy\n", "trailing comment"),
    ],
)
def test_unreadable_name_header_still_reaches_the_retry_path(
    repo: Path, header: str, label: str
) -> None:
    """A name the line scan cannot read must not drop the entry from the index.

    The directory is named for the *real* slugified name, not the file stem --
    that is the path the renderer's retry uses, and the one that breaks if
    `_slug_index` falls back to the stem. Naming it for the stem would pass
    even with the bug present.
    """
    kb = repo / "kb"
    (kb / "disorders" / "Weird_Stem.yaml").write_text(
        header + "mechanistic_hypotheses:\n- hypothesis_group_id: h1\n",
        encoding="utf-8",
    )
    _report(kb, "Folded_Real_Name", "h1")

    from scripts.check_hypothesis_links import _entry_name

    assert _entry_name(kb / "disorders" / "Weird_Stem.yaml") is None, label
    findings = collect(repo)
    assert [f.kind for f in findings] == ["non_canonical_slug"], label
    assert not [f for f in findings if f.kind in BLOCKING_KINDS], label


def test_committed_kb_has_no_disconnected_hypothesis_directories() -> None:
    """The real tree must stay clean; this is the regression guard."""
    root = Path(__file__).resolve().parents[1]
    blocking = [f for f in collect(root) if f.kind in BLOCKING_KINDS]
    assert blocking == [], "\n".join(f"{f.directory}: {f.detail}" for f in blocking)
