"""Tests for curation-project page rendering and entity auto-linking."""

from pathlib import Path

import yaml

from dismech.render import render_all_projects, render_project


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def _write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def _fixture(tmp_path: Path) -> dict[str, Path]:
    disorders = tmp_path / "kb" / "disorders"
    modules = tmp_path / "kb" / "modules"
    groupings = tmp_path / "kb" / "groupings"
    _write_yaml(disorders / "Test_Disease.yaml", {"name": "Test Disease"})
    _write_yaml(modules / "test_module.yaml", {"name": "Test Module"})
    return {"disorders": disorders, "modules": modules, "groupings": groupings}


def test_render_project_autolinks_declared_slugs(tmp_path: Path) -> None:
    dirs = _fixture(tmp_path)
    project_md = tmp_path / "projects" / "DEMO.md"
    _write(
        project_md,
        "---\n"
        "title: Demo Project\n"
        "status: IN_PROGRESS\n"
        "tags: [DEMO]\n"
        "diseases:\n"
        "  - Test_Disease\n"
        "modules:\n"
        "  - test_module\n"
        "drugs:\n"
        "  - id: CHEBI:45783\n"
        "    label: imatinib\n"
        "---\n\n"
        "# Demo Project\n\n"
        "We curate Test_Disease using the test_module module.\n\n"
        "The source file is Test_Disease.yaml (must not be mangled).\n",
    )

    output = tmp_path / "out" / "DEMO.html"
    render_project(
        project_md,
        output,
        disorders_dir=dirs["disorders"],
        modules_dir=dirs["modules"],
        groupings_dir=dirs["groupings"],
    )
    html = output.read_text()

    # Body slug references are auto-linked to their dismech pages.
    assert 'href="../disorders/Test_Disease.html"' in html
    assert 'href="../modules/test_module.html"' in html
    # Filename references keep their extension intact (not auto-linked).
    assert "Test_Disease.yaml" in html
    # Sidebar resolves entities, including external drug CURIE.
    assert "obo/CHEBI_45783" in html
    assert "Demo Project" in html
    assert "In progress" in html


def test_render_all_projects_builds_index(tmp_path: Path) -> None:
    dirs = _fixture(tmp_path)
    projects_dir = tmp_path / "projects"
    _write(
        projects_dir / "ALPHA.md",
        "---\ntitle: Alpha Project\nstatus: COMPLETE\n"
        "diseases:\n  - Test_Disease\n---\n\n# Alpha Project\n",
    )
    _write(projects_dir / "BETA.md", "# Beta Project\n\nNo frontmatter here.\n")

    output_dir = tmp_path / "pages" / "projects"
    outputs = render_all_projects(
        projects_dir,
        output_dir,
        disorders_dir=dirs["disorders"],
        modules_dir=dirs["modules"],
        groupings_dir=dirs["groupings"],
    )

    index = output_dir / "index.html"
    assert index in outputs
    index_html = index.read_text()
    assert 'href="ALPHA.html">Alpha Project' in index_html
    # Falls back to the first H1 when no title frontmatter is given.
    assert 'href="BETA.html">Beta Project' in index_html
    assert "Complete" in index_html
