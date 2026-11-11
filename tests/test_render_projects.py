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
    _write_yaml(groupings / "Demo_Grouping.yaml", {"name": "Demo Grouping"})
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
        "groupings:\n"
        "  - Demo_Grouping\n"
        "drugs:\n"
        "  - id: CHEBI:45783\n"
        "    label: imatinib\n"
        "---\n\n"
        "# Demo Project\n\n"
        "We curate Test_Disease using the test_module module under Demo_Grouping.\n\n"
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
    # Grouping slugs resolve to the grouping page (sidebar + body).
    assert 'href="../groupings/Demo_Grouping.html"' in html
    # Filename references keep their extension intact (not auto-linked).
    assert "Test_Disease.yaml" in html
    # Sidebar resolves entities, including external drug CURIE.
    assert "obo/CHEBI_45783" in html
    assert "Demo Project" in html
    assert "In progress" in html


def test_render_project_does_not_link_inside_code(tmp_path: Path) -> None:
    dirs = _fixture(tmp_path)
    project_md = tmp_path / "projects" / "CODE.md"
    _write(
        project_md,
        "---\n"
        "title: Code Project\n"
        "diseases:\n"
        "  - Test_Disease\n"
        "---\n\n"
        "# Code Project\n\n"
        "Inline `Test_Disease` stays literal.\n\n"
        "```yaml\n"
        "conforms_to: Test_Disease\n"
        "```\n",
    )

    output = tmp_path / "out" / "CODE.html"
    render_project(
        project_md,
        output,
        disorders_dir=dirs["disorders"],
        modules_dir=dirs["modules"],
        groupings_dir=dirs["groupings"],
    )
    html = output.read_text()

    # Isolate the rendered markdown body (the sidebar always links declared
    # entities; code protection only concerns the body itself).
    body_html = html.split('<article class="content">', 1)[1]

    # The slug appears only in inline/fenced code, so it must not be linked
    # in the body, but it must still be present as literal code text.
    assert 'href="../disorders/Test_Disease.html"' not in body_html
    assert "Test_Disease" in body_html


def test_render_all_projects_builds_index(tmp_path: Path) -> None:
    dirs = _fixture(tmp_path)
    projects_dir = tmp_path / "projects"
    _write(
        projects_dir / "ALPHA.md",
        "---\ntitle: Alpha Project\nstatus: COMPLETE\n"
        "diseases:\n  - Test_Disease\n"
        "groupings:\n  - Demo_Grouping\n---\n\n# Alpha Project\n",
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
    # Index summaries must resolve groupings (regression: previously the index
    # used an empty grouping index and always reported 0 groupings).
    assert "1 grouping" in index_html


def test_project_docs_links_are_rewritten_to_published_urls(tmp_path: Path) -> None:
    """``../docs/`` links must point at the MkDocs-published URL once rendered.

    From ``pages/projects/`` the source-markdown form ``../docs/X`` resolves to
    the nonexistent ``pages/docs/X``, so it has to be rewritten. See issue
    #7340.
    """
    docs = tmp_path / "docs"
    _write(docs / "explanation" / "design-decisions.md", "# Decisions\n")
    _write(docs / "research" / "table.tsv", "a\tb\n")
    _write(docs / "primers" / "index.md", "# Primers\n")
    _write(docs / "index.md", "# Docs home\n")
    _write(docs / "issues" / "internal-note.md", "# Not published\n")

    body = """---
title: Link Test
---

# Link Test

- [decisions](../docs/explanation/design-decisions.md#12-gaps)
- [table](../docs/research/table.tsv)
- [primers](../docs/primers/index.md)
- [docs home](../docs/index.md)
- [excluded](../docs/issues/internal-note.md#a-heading)
- [missing](../docs/nope/absent.md)

```markdown
- [fenced sample](../docs/explanation/design-decisions.md)
```
"""
    md_path = tmp_path / "projects" / "LINKS.md"
    _write(md_path, body)

    out = render_project(
        md_path,
        output_path=tmp_path / "pages" / "projects" / "LINKS.html",
    )
    html = out.read_text()

    # .md -> directory URL, anchor preserved
    assert 'href="../../elements/explanation/design-decisions/#12-gaps"' in html
    # non-markdown -> copied verbatim by MkDocs, extension kept
    assert 'href="../../elements/research/table.tsv"' in html
    # dir/index.md -> the directory itself
    assert 'href="../../elements/primers/"' in html
    # the root index.md -> the site root, not elements/index/
    assert 'href="../../elements/"' in html
    # excluded from the MkDocs build -> GitHub, since there is no published URL
    assert (
        'href="https://github.com/monarch-initiative/dismech/blob/main/'
        'docs/issues/internal-note.md#a-heading"' in html
    )
    # nonexistent target -> left untouched, so it stays visibly broken
    assert 'href="../docs/nope/absent.md"' in html
    # fenced code is documentation about the path, not a link to rewrite.
    # Anchored on the fence's own link text so this cannot pass on the strength
    # of some other surviving ../docs/ occurrence.
    assert "[fenced sample](../docs/explanation/design-decisions.md)" in html
    # and the old broken form is gone for the real links
    assert 'href="../docs/explanation/design-decisions.md#12-gaps"' not in html


def test_docs_exclusion_list_matches_mkdocs_config() -> None:
    """``_DOCS_EXCLUDED_FROM_SITE`` must track ``exclude_docs`` in mkdocs.yml.

    The two are kept in step by a comment; nothing else enforces it, and the
    drift would be silent — a newly excluded path would be rewritten to an
    ``elements/`` URL that MkDocs never publishes.
    """
    from dismech.render import _DOCS_EXCLUDED_FROM_SITE

    repo_root = Path(__file__).resolve().parents[1]
    mkdocs = repo_root / "mkdocs.yml"
    block: list[str] = []
    in_block = False
    for line in mkdocs.read_text().splitlines():
        if line.startswith("exclude_docs:"):
            in_block = True
            continue
        if in_block:
            if not line.startswith((" ", "\t")) or not line.strip():
                break
            block.append(line.strip())

    assert block, "could not parse exclude_docs from mkdocs.yml"
    # mkdocs lists them root-anchored ("/issues/"); the renderer stores them
    # relative to docs/ ("issues/").
    expected = {entry.lstrip("/") for entry in block}
    assert set(_DOCS_EXCLUDED_FROM_SITE) == expected


def test_render_graphical_abstract_on_project_and_module(tmp_path: Path) -> None:
    """``graphical_abstract`` renders its image and checkable ``legend`` chips on project and module pages."""
    from dismech.render import render_module

    dirs = _fixture(tmp_path)
    project_md = tmp_path / "projects" / "GA_DEMO.md"
    _write(
        project_md,
        "---\n"
        "title: GA Demo Project\n"
        "diseases:\n"
        "  - Test_Disease\n"
        "modules:\n"
        "  - test_module\n"
        "graphical_abstract:\n"
        "  image_path: assets/graphical_abstracts/MEMBRANE_CONTACT_SITES.png\n"
        "  archetype: RADIAL_STRUCTURAL_HUB\n"
        "  caption: Test project graphical abstract caption.\n"
        "  legend:\n"
        "    - panel: A. Hub\n"
        "      depicts: Hub panel description\n"
        "      attaches_to:\n"
        "        - modules#test_module\n"
        "        - diseases#Test_Disease\n"
        "---\n\n"
        "# GA Demo Project\n",
    )
    proj_out = tmp_path / "pages" / "projects" / "GA_DEMO.html"
    render_project(
        project_md,
        proj_out,
        disorders_dir=dirs["disorders"],
        modules_dir=dirs["modules"],
        groupings_dir=dirs["groupings"],
    )
    proj_html = proj_out.read_text()
    assert 'id="graphical-abstract"' in proj_html
    assert (
        'src="../../assets/graphical_abstracts/MEMBRANE_CONTACT_SITES.png"' in proj_html
    )
    assert 'href="../modules/test_module.html"' in proj_html
    assert 'href="../disorders/Test_Disease.html"' in proj_html

    module_yaml = dirs["modules"] / "ga_module.yaml"
    _write_yaml(
        module_yaml,
        {
            "name": "GA Module",
            "category": "Module",
            "pathophysiology": [
                {"name": "Trigger Node", "role": "trigger"},
            ],
            "graphical_abstract": {
                "image_path": "assets/graphical_abstracts/cgas_sting_pathway_activation.png",
                "archetype": "HYBRID_SUBCELLULAR_CUTAWAY",
                "caption": "Test module graphical abstract caption.",
                "legend": [
                    {
                        "panel": "1. Trigger",
                        "depicts": "Trigger panel description",
                        "attaches_to": ["pathophysiology#Trigger Node"],
                    }
                ],
            },
        },
    )
    mod_out = tmp_path / "pages" / "modules" / "ga_module.html"
    render_module(module_yaml, mod_out, disorders_dir=dirs["disorders"])
    mod_html = mod_out.read_text()
    assert 'id="graphical-abstract"' in mod_html
    assert 'href="#graphical-abstract">Graphical Abstract</a>' in mod_html
    assert (
        'src="../../assets/graphical_abstracts/cgas_sting_pathway_activation.png"'
        in mod_html
    )
    assert 'href="#module-pathophysiology-trigger-node"' in mod_html


def test_graphical_abstract_todo_escape_hatch(tmp_path: Path) -> None:
    """A ``todo`` (or ``panel: TODO``) legend entry bypasses validation errors for that node and renders a TODO badge."""
    from dismech.entity_refs import entity_ref_errors
    from dismech.render import render_module
    from scripts.check_graphical_abstracts import check_kb_entry

    dirs = _fixture(tmp_path)
    img_rel = "assets/graphical_abstracts/test_ga.png"
    _write(tmp_path / img_rel, "fake-png")
    mod_path = dirs["modules"] / "todo_module.yaml"

    # 1. Without a TODO, an unmapped pathograph node fails check_kb_entry
    inconsistent_data = {
        "name": "Todo Module",
        "category": "Module",
        "pathophysiology": [
            {"name": "Trigger Node", "role": "trigger"},
            {"name": "Newly Added Node", "role": "effector"},
        ],
        "graphical_abstract": {
            "image_path": img_rel,
            "archetype": "HORIZONTAL_ROLE_CASCADE",
            "legend": [
                {
                    "panel": "1. Trigger",
                    "depicts": "Trigger panel description",
                    "attaches_to": ["pathophysiology#Trigger Node"],
                }
            ],
        },
    }
    errs = check_kb_entry(mod_path, inconsistent_data, root=tmp_path)
    assert any("Newly Added Node" in e for e in errs)

    # 2. Adding a TODO legend node (even without `depicts`, or with a renamed/deleted ref)
    # bypasses validation errors in both entity_ref_errors and check_kb_entry
    todo_data = {
        "name": "Todo Module",
        "category": "Module",
        "pathophysiology": [
            {"name": "Trigger Node", "role": "trigger"},
            {"name": "Newly Added Node", "role": "effector"},
        ],
        "graphical_abstract": {
            "image_path": img_rel,
            "archetype": "HORIZONTAL_ROLE_CASCADE",
            "legend": [
                {
                    "panel": "1. Trigger",
                    "depicts": "Trigger panel description",
                    "attaches_to": ["pathophysiology#Trigger Node"],
                },
                {
                    "panel": "TODO",
                    "todo": "Draw Newly Added Node in Panel 2 and remove Deleted Node",
                    "attaches_to": [
                        "pathophysiology#Newly Added Node",
                        "pathophysiology#Deleted Node",
                    ],
                },
            ],
        },
    }
    todos: list[str] = []
    assert entity_ref_errors(todo_data) == []
    assert check_kb_entry(mod_path, todo_data, root=tmp_path, todos_out=todos) == []
    assert len(todos) >= 1
    assert any("Draw Newly Added Node" in t for t in todos)

    # 3. Rendering the module displays the visible Redraw TODO badge in the HTML legend
    _write_yaml(mod_path, todo_data)
    mod_out = tmp_path / "pages" / "modules" / "todo_module.html"
    render_module(mod_path, mod_out, disorders_dir=dirs["disorders"])
    mod_html = mod_out.read_text()
    assert "ga-legend-row-todo" in mod_html
    assert "Redraw TODO:" in mod_html
    assert "Draw Newly Added Node in Panel 2" in mod_html
