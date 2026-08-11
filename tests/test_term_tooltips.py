"""Tests for the plain-language tooltips on ontology term pills (issue #8310)."""

from pathlib import Path

import yaml

from dismech.render import render_disorder
from dismech.term_tooltips import TERM_ROLES, ontology_label, term_tooltip


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


def test_rendered_pills_carry_the_tooltip(tmp_path: Path) -> None:
    """End to end: the pill and its CURIE chip both get the hover text."""
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
    # The CURIE chip inside the pill repeats it, so the hover text does not
    # change as the pointer crosses onto the identifier.
    assert f'class="curie-chip curie-chip-cl" title="{expected}"' in html
    assert "title=\"Open CL:0000097\"" not in html
