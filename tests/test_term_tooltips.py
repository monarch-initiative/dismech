"""Tests for the plain-language tooltips on ontology term pills (issue #8310)."""

import re
from pathlib import Path

import yaml

from dismech.render import render_disorder
from dismech.term_tooltips import (
    ONTOLOGY_NAMES,
    TERM_ROLES,
    ontology_label,
    term_tooltip,
)

TEMPLATE_DIR = Path(__file__).resolve().parents[1] / "src" / "dismech" / "templates"

#: How the templates name a role: either a direct `term_tooltip(x, "role")` call
#: or the trailing argument of the `render_descriptor_tag(s)` macros.
_ROLE_PATTERNS = (
    re.compile(r'term_tooltip\([^,]+,\s*"([^"]+)"\)'),
    re.compile(r'render_descriptor_tags?\([^)]*?,\s*"([a-z_]+\.[a-z_]+)"\s*\)'),
)


def _roles_used_in_templates() -> set[str]:
    used: set[str] = set()
    for template in TEMPLATE_DIR.glob("*.j2"):
        text = template.read_text()
        for pattern in _ROLE_PATTERNS:
            used.update(pattern.findall(text))
    return used


def _write_disorder(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def test_tooltip_names_ontology_relation_and_annotation() -> None:
    """The three parts the issue asks for, in order."""
    tooltip = term_tooltip(
        {
            "preferred_term": "abnormal extracellular matrix organization",
            "term": {
                "id": "GO:0030198",
                "label": "abnormal extracellular matrix organization",
            },
        },
        "pathophysiology.biological_processes",
    )

    assert tooltip.splitlines() == [
        "Gene Ontology (GO)",
        "Relation: this pathophysiological event involves this biological process",
        (
            "This pathophysiological event involves abnormal extracellular matrix "
            "organization (GO:0030198). GO:0030198 is a biological process from the "
            "Gene Ontology."
        ),
    ]


def test_tooltip_names_both_labels_when_preferred_term_is_more_specific() -> None:
    tooltip = term_tooltip(
        {
            "preferred_term": "CD4+ regulatory T cell",
            "term": {"id": "CL:0000815", "label": "regulatory T cell"},
        },
        "pathophysiology.cell_types",
    )

    assert (
        "involves CD4+ regulatory T cell, annotated with regulatory T cell (CL:0000815)"
        in tooltip
    )


def test_tooltip_ignores_capitalisation_only_label_differences() -> None:
    """"Mast Cell" vs "mast cell" is not a difference worth a clause."""
    tooltip = term_tooltip(
        {
            "preferred_term": "Mast Cell",
            "term": {"id": "CL:0000097", "label": "mast cell"},
        },
        "pathophysiology.cell_types",
    )

    assert "involves Mast Cell (CL:0000097)." in tooltip
    assert "annotated with" not in tooltip


def test_tooltip_includes_qualifiers() -> None:
    tooltip = term_tooltip(
        {
            "preferred_term": "diarrhea",
            "term": {"id": "HP:0002014", "label": "Diarrhea"},
            "modifier": "INCREASED",
            "temporality": "CHRONIC",
            "severity": "SEVERE",
            "laterality": "BILATERAL",
            "onset": {"onset_category": "ADULT_ONSET", "min_age_years": 20},
        },
        "readout.phenotype_term",
    )

    assert "measures increased diarrhea" in tooltip
    assert "qualified as laterality bilateral; temporality chronic; severity severe" in tooltip
    assert "onset adult onset, from 20y" in tooltip


def test_tooltip_does_not_repeat_a_modifier_already_in_the_label() -> None:
    tooltip = term_tooltip(
        {
            "preferred_term": "abnormal cell adhesion",
            "term": {"id": "GO:0007155", "label": "cell adhesion"},
            "modifier": "ABNORMAL",
        },
        "pathophysiology.biological_processes",
    )

    assert "abnormal abnormal" not in tooltip


def test_tooltip_accepts_flattened_module_summary_terms() -> None:
    """Module summary pages hand over bare {id, label} pairs, not descriptors."""
    tooltip = term_tooltip(
        {"id": "CL:0000097", "label": "mast cell"}, "module.cell_types"
    )

    assert "Cell Ontology (CL)" in tooltip
    assert "This mechanism module involves mast cell (CL:0000097)." in tooltip


def test_tooltip_degrades_without_a_known_role_or_ontology() -> None:
    # Unknown role: still name the ontology rather than raising.
    assert term_tooltip(
        {"term": {"id": "CL:0000097", "label": "mast cell"}}, "nonexistent.slot"
    ) == "Cell Ontology (CL)"
    # Nothing at all to say.
    assert term_tooltip({}, "pathophysiology.cell_types") == ""
    assert term_tooltip(None, "pathophysiology.cell_types") == ""


def test_ontology_label_handles_mixed_curie_casing() -> None:
    # The repo writes gene CURIEs lowercase (see "CURIE Prefix Casing" in CLAUDE.md).
    assert ontology_label("hgnc:746") == ontology_label("HGNC:746")
    assert ontology_label("PMID:12345678") == ""
    assert ontology_label("") == ""
    assert ontology_label(None) == ""


def test_every_role_reads_as_a_sentence() -> None:
    """Guard against a role entry that renders as gibberish."""
    for role in TERM_ROLES:
        tooltip = term_tooltip(
            {"term": {"id": "CL:0000097", "label": "mast cell"}}, role
        )
        relation_line = tooltip.splitlines()[1]
        assert relation_line.startswith("Relation: this ")
        assert relation_line.endswith(("cell type", "gene", "process", "function",
                                       "component", "location", "organism", "entity",
                                       "intervention", "exposure", "phenotype",
                                       "biomarker", "assay", "type", "complex",
                                       "environment", "food"))


def test_template_role_strings_are_all_registered() -> None:
    """A typo'd role would silently drop the tooltip, so pin both directions.

    Unknown roles degrade rather than raising (by design), which is exactly why
    this needs a test: nothing else would notice `pathophysiology.cell_type`.
    """
    used = _roles_used_in_templates()
    assert used, "found no term_tooltip role strings in the templates at all"
    assert not (used - set(TERM_ROLES)), "template uses a role with no TERM_ROLES entry"
    assert not (set(TERM_ROLES) - used), "TERM_ROLES entry no template uses"


def test_ontology_names_do_not_carry_their_own_parenthetical() -> None:
    """The heading appends "(PREFIX)", so a name must not bring its own."""
    for prefix, (_display, name) in ONTOLOGY_NAMES.items():
        assert "(" not in name, f"{prefix} would render a double parenthetical"


def test_qualitative_modifiers_move_to_the_qualifier_clause() -> None:
    """"gain of function phosphatase activity" is not a sentence."""
    tooltip = term_tooltip(
        {
            "preferred_term": "protein tyrosine phosphatase activity",
            "term": {"id": "GO:0004725", "label": "protein tyrosine phosphatase activity"},
            "modifier": "GAIN_OF_FUNCTION",
        },
        "pathophysiology.molecular_functions",
    )

    assert "involves protein tyrosine phosphatase activity (GO:0004725)" in tooltip
    assert "qualified as gain of function" in tooltip
    assert "involves gain of function" not in tooltip


def test_mouse_model_genes_name_their_source() -> None:
    """Mouse-model gene descriptors bind MGI and reach a tooltipped pill."""
    tooltip = term_tooltip(
        {"preferred_term": "Bbs8", "term": {"id": "MGI:1924290", "label": "Bbs8"}},
        "model.genes",
    )

    assert tooltip.startswith("Mouse Genome Informatics (MGI)")
    assert "is a gene from the Mouse Genome Informatics." in tooltip


def test_rendered_pills_carry_the_tooltip(tmp_path: Path) -> None:
    """End to end: the pill carries the hover text and its chip inherits it."""
    disorder_path = tmp_path / "Tooltip_Disorder.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Tooltip_Disorder.html"

    _write_disorder(
        disorder_path,
        {
            "name": "Tooltip Disorder",
            "pathophysiology": [
                {
                    "name": "Mast cell degranulation",
                    "description": "Mast cells release mediators.",
                    "cell_types": [
                        {
                            "preferred_term": "mast cell",
                            "term": {"id": "CL:0000097", "label": "mast cell"},
                        }
                    ],
                }
            ],
        },
    )

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()

    expected = (
        "Cell Ontology (CL)\n"
        "Relation: this pathophysiological event involves this cell type\n"
        "This pathophysiological event involves mast cell (CL:0000097). "
        "CL:0000097 is a cell type from the Cell Ontology."
    )
    assert f'<span class="tag tag-cell" title="{expected}">' in html
    # The chip sits inside that pill and sets no title of its own: HTML resolves
    # `title` from the nearest titled ancestor, so the hover text stays the same
    # as the pointer crosses onto the identifier without duplicating the string.
    assert 'class="curie-chip curie-chip-cl">CL:0000097</a>' in html
    assert 'title="Open CL:0000097"' not in html
