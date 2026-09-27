"""Tests for pruning orphan HTML pages on a full render (issue #7426).

Page filenames come from ``slugify(name)``, so renaming an entry used to leave
its old page behind forever as a stale, publicly served snapshot. A full build
now deletes any page in the output directory it did not write; an incremental
build (issue #5507) must never prune, because it renders only a subset.
"""

from pathlib import Path

import pytest
import yaml

from dismech import render
from dismech.render import (
    _prune_orphan_pages,
    render_all_disorders,
    render_all_groupings,
)


def _write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def _disorder(name: str) -> dict:
    return {
        "name": name,
        "description": f"{name} test entry.",
        "pathophysiology": [],
    }


@pytest.fixture
def isolated_disorder_render(monkeypatch: pytest.MonkeyPatch) -> None:
    """Stub the cwd-relative aggregate passes a disorder build also triggers.

    ``render_all_disorders`` regenerates comorbidity, module, research, and
    classification pages from repo-relative default paths; a tmp-dir test only
    cares about the disorder pages themselves.
    """
    monkeypatch.setattr(render, "render_all_comorbidities", lambda *a, **k: [])
    monkeypatch.setattr(render, "render_all_modules", lambda *a, **k: [])
    monkeypatch.setattr(render, "render_research_index_page", lambda *a, **k: None)
    monkeypatch.setattr(render, "render_classification_pages", lambda *a, **k: [])


def test_prune_removes_unrendered_pages_and_keeps_the_rest(tmp_path: Path) -> None:
    output_dir = tmp_path / "pages"
    output_dir.mkdir()
    rendered = output_dir / "Real_Disease.html"
    rendered.write_text("<html></html>")
    index = output_dir / "index.html"
    index.write_text("<html></html>")
    orphan = output_dir / "Bogus_Disease.html"
    orphan.write_text("<html></html>")
    unrelated = output_dir / "notes.txt"
    unrelated.write_text("keep me")

    removed = _prune_orphan_pages(output_dir, [rendered], label="disorder")

    assert removed == [orphan]
    assert not orphan.exists()
    assert rendered.exists()
    assert index.exists()
    assert unrelated.exists()


def test_prune_is_a_noop_when_output_dir_is_missing(tmp_path: Path) -> None:
    assert _prune_orphan_pages(tmp_path / "nope", [], label="disorder") == []


def test_prune_is_a_noop_when_nothing_was_rendered(tmp_path: Path) -> None:
    """An empty rendered set means the input was missing, not that all pages died.

    ``python -m dismech.render --all <typo>`` binds the mistyped path to
    ``input_dir`` while ``output_dir`` stays at the default ``pages/disorders``,
    so a build that wrote nothing would otherwise delete every committed page.
    """
    output_dir = tmp_path / "pages"
    output_dir.mkdir()
    pages = [output_dir / "One.html", output_dir / "Two.html"]
    for page in pages:
        page.write_text("<html></html>")

    assert _prune_orphan_pages(output_dir, [], label="disorder") == []
    assert all(page.exists() for page in pages)


def test_full_disorder_render_over_an_empty_input_dir_keeps_pages(
    tmp_path: Path, isolated_disorder_render: None
) -> None:
    """The end-to-end shape of the mistyped-path case: no input, no deletions."""
    input_dir = tmp_path / "kb" / "typo"
    input_dir.mkdir(parents=True)
    output_dir = tmp_path / "pages" / "disorders"
    output_dir.mkdir(parents=True)
    survivor = output_dir / "Real_Disease.html"
    survivor.write_text("<html></html>")

    rendered = render_all_disorders(input_dir=input_dir, output_dir=output_dir)

    assert rendered == []
    assert survivor.exists()


def test_prune_keeps_a_differently_named_page_that_is_the_same_file(
    tmp_path: Path,
) -> None:
    """Exercise the ``samefile`` fallback on a case-sensitive filesystem.

    The branch exists for case-insensitive filesystems, where two case-only
    slug variants are one file — a condition Linux CI can never reach. A
    hardlink reproduces the same "two names, one inode" shape so the guard
    that prevented the #599 self-deletion is actually covered.
    """
    output_dir = tmp_path / "pages"
    output_dir.mkdir()
    rendered = output_dir / "Holt-Oram_syndrome.html"
    rendered.write_text("<html></html>")
    alias = output_dir / "Holt-Oram_Syndrome.html"
    alias.hardlink_to(rendered)

    removed = _prune_orphan_pages(output_dir, [rendered], label="disorder")

    assert removed == []
    assert alias.exists()
    assert rendered.exists()


def test_full_disorder_render_prunes_orphan_pages(
    tmp_path: Path, isolated_disorder_render: None
) -> None:
    input_dir = tmp_path / "kb" / "disorders"
    output_dir = tmp_path / "pages" / "disorders"
    _write_yaml(input_dir / "Real_Disease.yaml", _disorder("Real Disease"))
    output_dir.mkdir(parents=True)
    orphan = output_dir / "Bogus_Disease.html"
    orphan.write_text("<html>stale</html>")

    rendered = render_all_disorders(input_dir=input_dir, output_dir=output_dir)

    assert not orphan.exists()
    survivors = sorted(path.name for path in output_dir.glob("*.html"))
    assert survivors == ["Real_Disease.html"]
    assert [path.name for path in rendered] == ["Real_Disease.html"]


def test_full_disorder_render_prunes_a_case_only_slug_collision(
    tmp_path: Path, isolated_disorder_render: None
) -> None:
    """The stale capital-S page goes; the page the KB entry names survives.

    ``Holt-Oram_Syndrome.html`` (an old stem-derived slug) collided with the
    ``slugify(name)`` page ``Holt-Oram_syndrome.html`` on case-insensitive
    filesystems, and the *correct* page was hand-deleted twice as a result.
    """
    input_dir = tmp_path / "kb" / "disorders"
    output_dir = tmp_path / "pages" / "disorders"
    _write_yaml(input_dir / "Holt-Oram_Syndrome.yaml", _disorder("Holt-Oram syndrome"))
    output_dir.mkdir(parents=True)
    stale = output_dir / "Holt-Oram_Syndrome.html"
    stale.write_text("<html>STALE-SNAPSHOT-MARKER</html>")

    render_all_disorders(input_dir=input_dir, output_dir=output_dir)

    # The page the entry's ``name`` maps to survives with fresh content, and it
    # is the only page left — on a case-sensitive filesystem the stale capital-S
    # file is pruned; on a case-insensitive one the two were the same file all
    # along and it was overwritten, not deleted.
    current = output_dir / "Holt-Oram_syndrome.html"
    assert current.exists()
    assert "STALE-SNAPSHOT-MARKER" not in current.read_text()
    assert len(list(output_dir.glob("*.html"))) == 1


def test_incremental_disorder_render_never_prunes(
    tmp_path: Path, isolated_disorder_render: None
) -> None:
    """``only=`` renders a subset by design (#5507), so pruning would be fatal."""
    input_dir = tmp_path / "kb" / "disorders"
    output_dir = tmp_path / "pages" / "disorders"
    changed = input_dir / "Changed_Disease.yaml"
    _write_yaml(changed, _disorder("Changed Disease"))
    _write_yaml(input_dir / "Untouched_Disease.yaml", _disorder("Untouched Disease"))
    output_dir.mkdir(parents=True)
    untouched = output_dir / "Untouched_Disease.html"
    untouched.write_text("<html>previous build</html>")

    render_all_disorders(input_dir=input_dir, output_dir=output_dir, only={changed})

    assert untouched.exists()
    assert (output_dir / "Changed_Disease.html").exists()


def test_full_grouping_render_prunes_orphan_pages(tmp_path: Path) -> None:
    input_dir = tmp_path / "kb" / "groupings"
    disorders_dir = tmp_path / "kb" / "disorders"
    output_dir = tmp_path / "pages" / "groupings"
    disorders_dir.mkdir(parents=True)
    _write_yaml(
        input_dir / "Test_Grouping.yaml",
        {
            "name": "Test Grouping",
            "description": "A grouping for prune testing.",
            "members": [],
        },
    )
    output_dir.mkdir(parents=True)
    orphan = output_dir / "Renamed_Grouping.html"
    orphan.write_text("<html>stale</html>")

    render_all_groupings(
        input_dir=input_dir, output_dir=output_dir, disorders_dir=disorders_dir
    )

    assert not orphan.exists()
    assert (output_dir / "Test_Grouping.html").exists()
    assert (output_dir / "index.html").exists()
