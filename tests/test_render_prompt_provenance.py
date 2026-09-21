"""Tests for showing a report's prompt revision on its rendered page.

A deep-research report records the prompt it came from as a bare path, so the
file behind that path changes while the reference does not (issue #10183). The
research recipes now also stamp a ``template_sha`` — the template's git blob
hash — and this is what surfaces it to a reader of the rendered page.

Only a *stamped* hash is shown. An older report's revision is inferable from its
timestamp against the template's commit history, but that is a reconstruction
rather than a record, and a metadata chip has no room to say which it is
showing.
"""

from pathlib import Path

import yaml

from dismech.render import (
    _prompt_provenance,
    render_research_report,
)

SHA = "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"


def _write_report(path: Path, frontmatter: dict) -> Path:
    path.write_text(
        "---\n"
        + yaml.safe_dump(frontmatter, sort_keys=False)
        + "---\n\n# Report\n\n## Key Findings\n\nSomething.\n",
        encoding="utf-8",
    )
    return path


def test_absent_stamp_yields_no_chip() -> None:
    """The overwhelming majority of committed reports predate stamping."""
    assert _prompt_provenance({"provider": "falcon"}) is None


def test_blank_stamp_is_treated_as_absent() -> None:
    assert _prompt_provenance({"template_sha": "   "}) is None


def test_non_string_stamp_is_treated_as_absent() -> None:
    """An all-digit hash can load from YAML as an int if written unquoted."""
    assert _prompt_provenance({"template_sha": 1234}) is None


def test_stamp_carries_full_and_short_hash() -> None:
    provenance = _prompt_provenance({"template_sha": SHA})

    assert provenance is not None
    assert provenance["sha"] == SHA
    assert provenance["short"] == "1e7ea4ee817a"


def test_template_path_becomes_a_named_link() -> None:
    provenance = _prompt_provenance(
        {
            "template_sha": SHA,
            "template_file": "templates/disease_pathophysiology_research.md",
        }
    )

    assert provenance["name"] == "disease_pathophysiology_research.md"
    assert provenance["url"].endswith(
        "/blob/main/templates/disease_pathophysiology_research.md"
    )


def test_windows_separators_still_resolve_to_a_link() -> None:
    """Twenty committed reports record the path with backslashes (#10183)."""
    provenance = _prompt_provenance(
        {
            "template_sha": SHA,
            "template_file": "templates\\disease_pathophysiology_research.md",
        }
    )

    assert provenance["name"] == "disease_pathophysiology_research.md"
    assert provenance["url"].endswith(
        "/blob/main/templates/disease_pathophysiology_research.md"
    )


def test_free_text_label_is_shown_but_not_linked() -> None:
    """Several reports record a label rather than a path.

    `manual_curation` names no file, so linking it would produce a 404 dressed
    up as provenance.
    """
    provenance = _prompt_provenance(
        {"template_sha": SHA, "template_file": "manual_curation"}
    )

    assert provenance["name"] == "manual_curation"
    assert provenance["url"] is None


def test_stamp_without_a_template_file_still_shows_the_hash() -> None:
    provenance = _prompt_provenance({"template_sha": SHA})

    assert provenance["name"] is None
    assert provenance["url"] is None
    assert provenance["short"] == "1e7ea4ee817a"


def _render(tmp_path: Path, frontmatter: dict) -> str:
    research_dir = tmp_path / "research"
    research_dir.mkdir()
    output_dir = tmp_path / "pages"
    output_dir.mkdir()
    report_path = _write_report(
        research_dir / "Asthma-deep-research-falcon.md", frontmatter
    )
    written = render_research_report(
        {
            "path": report_path,
            "disorder_name": "Asthma",
            "provider_key": "falcon",
            "provider_label": "Falcon",
            "prefix": "",
            "output_name": "Asthma-falcon.html",
        },
        siblings=[],
        prev_report=None,
        next_report=None,
        output_dir=output_dir,
    )
    return written.read_text(encoding="utf-8")


def test_rendered_page_shows_the_hash_and_links_the_template(tmp_path: Path) -> None:
    html = _render(
        tmp_path,
        {
            "provider": "falcon",
            "template_file": "templates/disease_pathophysiology_research.md",
            "template_sha": SHA,
        },
    )

    assert "1e7ea4ee817a" in html
    assert "disease_pathophysiology_research.md" in html
    assert SHA in html, "the full hash belongs in the tooltip, not only the short one"
    assert f"git log --find-object={SHA} -- templates/" in html, (
        "the command should carry the full hash, which is what gets pasted, and "
        "scope to templates/ only when the prompt really is a templates/ path"
    )


def test_tooltip_drops_the_pathspec_for_an_unlinked_prompt(tmp_path: Path) -> None:
    """A label's blob is not under `templates/`.

    Scoping the lookup there would return nothing, which reads as "this hash is
    not in the repo" rather than "wrong directory". Defensive: `stamp_report`
    declines unless the template is a file on disk, so a label is never stamped
    by the pipeline.
    """
    html = _render(
        tmp_path,
        {
            "provider": "falcon",
            "template_file": "manual_curation",
            "template_sha": SHA,
        },
    )

    assert f"git log --find-object={SHA}" in html
    assert "-- templates/" not in html
    assert "manual_curation" in html
    assert "blob/main/manual_curation" not in html, "a label must not be linked"


def test_rendered_page_omits_the_chip_when_unstamped(tmp_path: Path) -> None:
    html = _render(tmp_path, {"provider": "falcon", "model": "falcon-1"})

    # The CSS rule is emitted unconditionally, so assert on the chip markup
    # rather than the class name, which would match the stylesheet too.
    assert '<span class="meta-chip meta-chip-prompt"' not in html
    assert "Prompt:" not in html
    assert "git log --find-object" not in html
