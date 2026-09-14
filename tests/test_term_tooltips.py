"""Tests for the plain-language tooltips on ontology term pills (issue #8310)."""

import ast
import inspect
import re
import textwrap
from pathlib import Path

import pytest
import yaml
from bs4 import BeautifulSoup

from dismech import term_tooltips
from dismech.render import render_comorbidity, render_disorder, render_module
from dismech.term_tooltips import (
    _QUALIFIER_SLOTS,
    _SCALAR_QUALIFIER_SLOTS,
    ONTOLOGY_NAMES,
    TERM_ROLES,
    ontology_label,
    sample_type_descriptor,
    term_tooltip,
)

TEMPLATE_DIR = Path(__file__).resolve().parents[1] / "src" / "dismech" / "templates"

#: Calls that name a role: `term_tooltip(...)` or one of the
#: `render_descriptor_tag(s)` macros.
_ROLE_CALL = re.compile(r"(?:term_tooltip|render_descriptor_tags?)\(")

#: A role string, recognised by its `<container>.<slot>` shape. Matching the
#: string rather than its argument position sidesteps parsing the call: a
#: positional role, a `role=` keyword, and an argument that is itself a call all
#: collect the same. Nothing else in these calls looks like this -- CSS classes
#: are `tag-bio`, hyphenated and undotted.
_ROLE_STRING = re.compile(r'"([a-z_]+\.[a-z_]+)"')

#: A Jinja expression ends at its delimiter. Scanning to there rather than to
#: end-of-line keeps a call that wraps across lines in view -- Jinja permits it,
#: and the longer `render_descriptor_tags(...)` invocations invite it.
_EXPRESSION_END = re.compile(r"%\}|\}\}")


def _roles_used_in_templates() -> set[str]:
    used: set[str] = set()
    for template in TEMPLATE_DIR.glob("*.j2"):
        text = template.read_text()
        for call in _ROLE_CALL.finditer(text):
            end = _EXPRESSION_END.search(text, call.end())
            used.update(
                _ROLE_STRING.findall(text[call.end() : end.start() if end else len(text)])
            )
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
            "onset": {"onset_category": "CHILDHOOD", "min_age_years": 2},
        },
        "readout.phenotype_term",
    )

    assert "measures increased diarrhea" in tooltip
    assert "qualified as laterality bilateral; temporality chronic; severity severe" in tooltip
    # The category is an adjective, so it leads: "childhood onset", not "onset childhood".
    assert "childhood onset, from 2y" in tooltip


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
    """Guard against a role entry that renders as gibberish.

    Checks the shape each field has to have for the two sentences to come out
    grammatical, rather than an allowlist of noun endings -- that only ever
    catches the roles someone remembered to enumerate, and rejects perfectly
    good new ones.
    """
    for role, term_role in TERM_ROLES.items():
        # The subject opens a sentence ("This treatment ...") and is lowercased
        # mid-sentence for the relation line, so it has to start that way.
        assert term_role.subject.startswith("This "), role
        for field in (term_role.subject, term_role.relation, term_role.kind):
            assert field == field.strip(), role
            assert field, role
            assert not field.endswith("."), role
        # The kind is a bare noun phrase: it follows "a"/"an" and "this".
        assert term_role.kind == term_role.kind.lower(), role
        assert not term_role.kind.startswith(("a ", "an ", "the ")), role

        tooltip = term_tooltip(
            {"term": {"id": "CL:0000097", "label": "mast cell"}}, role
        )
        heading, relation_line, sentence = tooltip.splitlines()
        assert heading == "Cell Ontology (CL)"
        assert relation_line == (
            f"Relation: this{term_role.subject[4:]} "
            f"{term_role.relation} this {term_role.kind}"
        )
        assert sentence.startswith(f"{term_role.subject} {term_role.relation} mast cell")
        assert sentence.endswith("from the Cell Ontology.")
        for line in (relation_line, sentence):
            assert "  " not in line, role


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
    for prefix, ontology in ONTOLOGY_NAMES.items():
        assert "(" not in ontology.name, f"{prefix} would render a double parenthetical"


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
    # No definite article: "from the Mouse Genome Informatics" is not English.
    assert "is a gene from Mouse Genome Informatics." in tooltip


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
    # The text lives in a real element, not a `title` attribute, so it can be
    # shown on focus and referenced by aria-describedby (issue #8355).
    assert f'<span class="pill-tip" role="tooltip" id="pill-tip-1">{expected}</span>' in html
    # The chip is the pill's single tab stop: focusing it reveals the tooltip via
    # CSS :focus-within and announces it via the description.
    assert 'class="curie-chip curie-chip-cl" aria-describedby="pill-tip-1"' in html
    assert 'title="Open CL:0000097"' not in html
    # No pill keeps a native title tooltip -- two competing tooltips on one hover.
    assert not re.search(r'title="[^"]*\nRelation: ', html)


def test_definite_article_follows_the_ontology_record() -> None:
    """"the Gene Ontology" but "Mouse Genome Informatics" -- both from data."""
    gene_ontology = term_tooltip(
        {"term": {"id": "GO:0007155", "label": "cell adhesion"}},
        "pathophysiology.biological_processes",
    )
    assert "from the Gene Ontology." in gene_ontology

    chebi = term_tooltip(
        {"term": {"id": "CHEBI:36796", "label": "duloxetine"}},
        "treatment.therapeutic_agent",
    )
    assert "from Chemical Entities of Biological Interest." in chebi
    assert "from the Chemical Entities" not in chebi


def test_sample_type_tooltip_describes_the_label_on_the_pill() -> None:
    """The pill shows the sample type's own label, so the tooltip must too.

    Most sample types bind their own (usually UBERON) term; some bind only a
    nested cell type. Either way the pill displays the outer `preferred_term`.
    """
    # Its own binding, with no cell type to prefer.
    tissue = term_tooltip(
        sample_type_descriptor(
            {
                "preferred_term": "stomach tissue",
                "term": {"id": "UBERON:0000945", "label": "stomach"},
            }
        ),
        "dataset.sample_types",
    )
    assert "This dataset samples stomach tissue, annotated with stomach (UBERON:0000945)" in tissue
    assert "is a sample type from the Uberon" in tissue

    # Only a nested cell type: keep the pill's more specific label and let the
    # usual "annotated with" handling explain the binding.
    nested = term_tooltip(
        sample_type_descriptor(
            {
                "preferred_term": "molar epithelium from furcation region",
                "cell_type_term": {
                    "preferred_term": "epithelial cell",
                    "term": {"id": "CL:0000066", "label": "epithelial cell"},
                },
            }
        ),
        "dataset.sample_types",
    )
    assert "samples molar epithelium from furcation region" in nested
    assert "annotated with epithelial cell (CL:0000066)" in nested

    # Bound only through `tissue_term` -- 63 sample types in the KB are this
    # shape and used to render with no ontology heading and no identifier.
    tissue_only = term_tooltip(
        sample_type_descriptor(
            {
                "preferred_term": "whole lung tissue",
                "tissue_term": {"term": {"id": "UBERON:0002048", "label": "lung"}},
            }
        ),
        "dataset.sample_types",
    )
    assert tissue_only.startswith("Uberon multi-species anatomy ontology (UBERON)")
    assert "samples whole lung tissue, annotated with lung (UBERON:0002048)" in tissue_only


def test_sample_type_prefers_the_cell_type_over_the_tissue_it_came_from() -> None:
    """"peripheral blood monocytes" is explained by `monocyte`, not by `blood`."""
    chosen = sample_type_descriptor(
        {
            "preferred_term": "peripheral blood monocytes",
            "term": {"id": "UBERON:0000178", "label": "blood"},
            "cell_type_term": {"term": {"id": "CL:0000576", "label": "monocyte"}},
            "tissue_term": {"term": {"id": "UBERON:0000178", "label": "blood"}},
        }
    )

    # The chip renders from this same mapping, so choosing here also decides
    # which CURIE the reader sees and clicks -- they cannot disagree.
    assert chosen["term"]["id"] == "CL:0000576"
    assert chosen["preferred_term"] == "peripheral blood monocytes"


def test_sample_type_descriptor_handles_the_awkward_shapes() -> None:
    # Nothing to merge.
    assert sample_type_descriptor(None) == {}
    assert sample_type_descriptor({}) == {}
    # No label of its own: the binding's own label is the better one.
    assert sample_type_descriptor(
        {"cell_type_term": {"preferred_term": "macrophage", "term": {"id": "CL:0000235"}}}
    ) == {"preferred_term": "macrophage", "term": {"id": "CL:0000235"}}
    # No binding anywhere: passed through untouched.
    bare = {"preferred_term": "whole blood"}
    assert sample_type_descriptor(bare) == bare
    # A binding slot present but carrying no id is not a binding.
    empty = {"preferred_term": "serum", "tissue_term": {"preferred_term": "blood"}}
    assert sample_type_descriptor(empty) == empty


def test_legacy_qualifier_pairs_render_as_labels_not_dicts() -> None:
    """Both sides of a Qualifier range over Descriptor, not over a string.

    Reading them as scalars put a Python dict repr in the title attribute, on
    every pill in the 53 disorder files that carry a treatment-term qualifier.
    Shaped after kb/disorders/Folliculitis.yaml.
    """
    tooltip = term_tooltip(
        {
            "preferred_term": "topical pharmacotherapy",
            "term": {"id": "NCIT:C15986", "label": "Pharmacotherapy"},
            "qualifiers": [
                {
                    "predicate": {
                        "preferred_term": "therapeutic procedure",
                        "term": {"id": "NCIT:C49236", "label": "Therapeutic Procedure"},
                    },
                    "value": {
                        "preferred_term": "topical route of administration",
                        "term": {"id": "NCIT:C38304", "label": "Topical Route of Administration"},
                    },
                }
            ],
        },
        "treatment.treatment_term",
    )

    assert "qualified as therapeutic procedure topical route of administration" in tooltip
    assert "{" not in tooltip and "'" not in tooltip
    # The CURIE inside a nested descriptor must not be lower-cased into prose.
    assert "ncit:" not in tooltip


def test_qualifier_sides_fall_back_to_the_ontology_label_then_the_curie() -> None:
    tooltip = term_tooltip(
        {
            "preferred_term": "physical therapy",
            "term": {"id": "NCIT:C15302", "label": "Physical Therapy"},
            "qualifiers": [
                {
                    "predicate": {"term": {"id": "RO:0002233", "label": "has input"}},
                    "value": {"term": {"id": "CL:0000097"}},
                }
            ],
        },
        "treatment.treatment_term",
    )

    assert "qualified as has input CL:0000097" in tooltip


def test_a_qualifier_missing_a_side_is_skipped() -> None:
    tooltip = term_tooltip(
        {
            "preferred_term": "physical therapy",
            "term": {"id": "NCIT:C15302", "label": "Physical Therapy"},
            "qualifiers": [{"predicate": {"preferred_term": "has input"}}, {}],
        },
        "treatment.treatment_term",
    )

    assert "qualified as" not in tooltip


def test_sample_type_merge_keeps_qualifiers_written_on_the_outer_descriptor() -> None:
    """The nested branch is the common path now, so it must not drop them."""
    tooltip = term_tooltip(
        sample_type_descriptor(
            {
                "preferred_term": "inflamed bronchial epithelium",
                "severity": "SEVERE",
                "temporality": "CHRONIC",
                "cell_type_term": {
                    "term": {"id": "CL:0002328", "label": "bronchial epithelial cell"}
                },
            }
        ),
        "dataset.sample_types",
    )

    assert "samples inflamed bronchial epithelium" in tooltip
    assert "qualified as temporality chronic; severity severe" in tooltip


def _slots_read_by_qualifier_phrases() -> set[str]:
    """Every slot `_qualifier_phrases` reads, taken from the function itself.

    Walks its AST for `descriptor.get("<literal>")` and unions that with the
    slots consumed by the `_SCALAR_QUALIFIER_SLOTS` loop, which reads through a
    variable and so has no literal to find. Deriving this instead of listing it
    is the point: a spelled-out list only covers the reads someone remembered to
    spell out, and a *new* non-scalar read added to neither list would pass.

    Scope, stated rather than implied. Two reads are invisible here:
    `descriptor["penetrance"]` subscript form (in practice `.get()` is the only
    workable idiom, since every qualifier slot is optional and a subscript would
    raise); and a slot read inside a *helper* called from `_qualifier_phrases`,
    because `inspect.getsource` sees only that one function. `_onset_phrase` is
    already that shape -- it stays covered because the literal
    `descriptor.get("onset")` sits at the call site, not inside the helper.
    """
    source = textwrap.dedent(inspect.getsource(term_tooltips._qualifier_phrases))
    literal_reads = {
        node.args[0].value
        for node in ast.walk(ast.parse(source))
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "get"
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "descriptor"
        and node.args
        and isinstance(node.args[0], ast.Constant)
        and isinstance(node.args[0].value, str)
    }
    return literal_reads | {slot for slot, _wording in _SCALAR_QUALIFIER_SLOTS}


def test_qualifier_slot_lists_stay_in_step() -> None:
    """The recomposition list must cover every slot the tooltip actually reads.

    `_QUALIFIER_SLOTS` is what `sample_type_descriptor` carries across a merge.
    Adding a slot to the tooltip without adding it here would silently drop it
    on the merge path -- the same quiet-omission shape as the `Qualifier` bug
    this file covers.
    """
    reads = _slots_read_by_qualifier_phrases()

    assert reads, "found no descriptor reads at all -- the AST walk is broken"
    assert _QUALIFIER_SLOTS == reads


def test_onset_phrase_shapes() -> None:
    """Category leads when present; ages alone keep the bare noun."""
    def onset_of(**onset):
        return term_tooltip(
            {
                "preferred_term": "seizure",
                "term": {"id": "HP:0001250", "label": "Seizure"},
                "onset": onset,
            },
            "readout.phenotype_term",
        )

    assert "qualified as congenital onset." in onset_of(onset_category="CONGENITAL")
    assert "qualified as young adult onset." in onset_of(onset_category="YOUNG_ADULT")
    # No category: nothing to lead with, so the noun stays in front of the ages.
    assert "qualified as onset, mean 7y." in onset_of(mean_age_years=7)
    assert "qualified as" not in onset_of()


def test_shared_phenotype_tooltip_is_gated_on_a_bound_term() -> None:
    """A term-less shared phenotype shows `pheno.name`, so it gets no tooltip.

    Without the gate the item would carry hover text built from
    `phenotype_term.preferred_term` while displaying something else -- the same
    describes-the-wrong-thing shape the dataset sample-type pill had.
    """
    template = TEMPLATE_DIR / "comorbidity.html.j2"
    text = template.read_text()

    assert '{% set has_term = pheno.phenotype_term' in text
    assert (
        '{% set tooltip = term_tooltip(pheno.phenotype_term, '
        '"comorbidity.phenotypes") if has_term else "" %}'
    ) in text


def test_go_enrichment_tooltip_is_gated_on_a_bound_term() -> None:
    """Same gate as the shared phenotype, for the same reason.

    `GOEnrichmentTerm` carries no label of its own today, so an unbound one
    yields no tooltip regardless -- but that is correct by data shape, not by
    construction, and stops being true if the class ever gains a label slot.
    """
    text = (TEMPLATE_DIR / "comorbidity.html.j2").read_text()

    assert '{% set has_term = term.term and term.term.id %}' in text
    assert (
        '{% set tooltip = term_tooltip(term, "signal.go_enrichment") '
        'if has_term else "" %}'
    ) in text
    # The link is gated on the same name, so the two cannot drift apart.
    assert (
        "{% if has_term %}\n"
        "                            {{ render_term_link(term.term.id"
    ) in text


def _rendered_pill_page(tmp_path: Path) -> str:
    """A disorder page exercising the pill shapes that differ for keyboard use."""
    disorder_path = tmp_path / "A11y_Disorder.yaml"
    output_path = tmp_path / "pages" / "disorders" / "A11y_Disorder.html"
    _write_disorder(
        disorder_path,
        {
            "name": "A11y Disorder",
            "pathophysiology": [
                {
                    "name": "Mast cell degranulation",
                    "description": "Mast cells release mediators.",
                    # Bound: renders a CURIE chip, which is already a tab stop.
                    "cell_types": [
                        {
                            "preferred_term": "mast cell",
                            "term": {"id": "CL:0000097", "label": "mast cell"},
                        }
                    ],
                    # Unbound: no chip, so the pill itself must become focusable.
                    "biological_processes": [{"preferred_term": "unbound process"}],
                }
            ],
        },
    )
    render_disorder(disorder_path, output_path=output_path)
    return output_path.read_text()


def test_every_tooltip_is_reachable_and_uniquely_referenced(tmp_path: Path) -> None:
    """The accessibility contract, checked on real output rather than asserted.

    Every tooltip must have a unique id, exactly one element that points at it,
    and that element must be focusable -- otherwise the text is still
    mouse-only, which is the whole complaint in issue #8355.
    """
    html = _rendered_pill_page(tmp_path)

    ids = re.findall(r'<span class="pill-tip" role="tooltip" id="([^"]+)"', html)
    refs = re.findall(r'aria-describedby="([^"]+)"', html)

    assert ids, "no tooltips rendered at all"
    assert len(ids) == len(set(ids)), "duplicate tooltip ids -- invalid HTML"
    assert sorted(refs) == sorted(ids), "every tooltip needs exactly one referrer"

    # The referring element is focusable: either a link, or a pill given a tab
    # stop precisely because it has no link to borrow.
    for ref in refs:
        owner = re.search(rf'<(\w+)([^>]*aria-describedby="{re.escape(ref)}"[^>]*)>', html)
        assert owner, ref
        tag, attrs = owner.group(1), owner.group(2)
        assert tag == "a" or 'tabindex="0"' in attrs, f"{ref} is not reachable by keyboard"


def test_pill_without_a_chip_gets_its_own_tab_stop(tmp_path: Path) -> None:
    """A pill whose descriptor has no CURIE has no link to borrow focus from."""
    html = _rendered_pill_page(tmp_path)

    assert 'tabindex="0"' in html
    # ...and one that does have a chip must NOT add a second, redundant stop.
    bound = re.search(r'<span class="tag tag-cell"([^>]*)>', html)
    assert bound and "tabindex" not in bound.group(1)


def test_tooltips_are_dismissable(tmp_path: Path) -> None:
    """WCAG 2.1 SC 1.4.13 requires hover/focus content to be dismissable."""
    html = _rendered_pill_page(tmp_path)

    assert "'Escape'" in html
    assert "tip.hidden = true" in html
    # ...and the CSS must let [hidden] beat the :hover / :focus-within rules.
    assert "> .pill-tip[hidden]" in html


def test_tooltip_shows_on_focus_not_only_hover(tmp_path: Path) -> None:
    """The keyboard and touch half of issue #8355 is this one CSS rule."""
    html = _rendered_pill_page(tmp_path)

    assert "*:focus-within > .pill-tip" in html
    assert "*:hover > .pill-tip" in html
    # A pill host must not have to carry a class to show its tooltip: the two
    # comorbidity pills are bare <li>, and an `[class]` gate silently hid them.
    assert "[class]:hover > .pill-tip" not in html
    # Hovering the tooltip itself must keep it open (SC 1.4.13 "hoverable").
    assert ".pill-tip:hover" in html


def _show_selector(html: str) -> str:
    """The structural half of the CSS rule that reveals a tooltip.

    Pulled out of the page itself rather than hard-coded, so the test tracks the
    stylesheet instead of a copy of it. `:hover` / `:focus-within` describe user
    state, which a static parse cannot evaluate -- stripping them leaves exactly
    the structural requirement: which parents can ever show their tooltip.
    """
    rule = re.search(r"^\s*(\S+:hover > \.pill-tip),", html, re.MULTILINE)
    assert rule, "no .pill-tip show rule found in the page stylesheet"
    return rule.group(1).replace(":hover", "")


def _assert_every_tooltip_can_be_shown(html: str, page: str) -> None:
    soup = BeautifulSoup(html, "html.parser")
    tips = soup.select(".pill-tip")
    assert tips, f"{page} rendered no tooltips, so it proves nothing"
    showable = soup.select(_show_selector(html))
    unreachable = [t for t in tips if t not in showable]
    assert not unreachable, (
        f"{page}: {len(unreachable)} of {len(tips)} tooltips can never be shown; "
        f"first offender sits in <{unreachable[0].parent.name} "
        f"class={unreachable[0].parent.get('class')}>"
    )
    # The JS (Escape dismissal, viewport clamp) walks up with its own selector,
    # which has to agree with the CSS about what counts as a pill.
    pill_selector = re.search(r"var PILL = '([^']+)'", html)
    assert pill_selector, f"{page}: no PILL selector in the dismissal script"
    known = soup.select(pill_selector.group(1))
    assert all(t.parent in known for t in tips), (
        f"{page}: a tooltip's parent is not matched by the script's PILL selector"
    )


def test_comorbidity_tooltips_can_all_be_shown(tmp_path: Path) -> None:
    """The `<li>`-hosted pills here have no class, which a `[class]` show rule
    silently excluded -- losing the text for mouse users entirely."""
    source = Path("kb/comorbidities")
    entries = sorted(source.glob("*.yaml")) if source.is_dir() else []
    if not entries:
        pytest.skip("no comorbidity entries available")
    out = tmp_path / "comorbidities"
    rendered = [render_comorbidity(e, out / f"{e.stem}.html") for e in entries]
    pages = [
        text
        for text in (p.read_text() for p in rendered)
        if 'class="pill-tip"' in text
    ]
    assert pages, "no comorbidity page carries a tooltip"
    for i, html in enumerate(pages):
        _assert_every_tooltip_can_be_shown(html, f"comorbidity page {i}")


def test_module_tooltips_can_all_be_shown(tmp_path: Path) -> None:
    source = Path("kb/modules")
    entries = sorted(source.glob("*.yaml")) if source.is_dir() else []
    if not entries:
        pytest.skip("no module entries available")
    html = render_module(entries[0], tmp_path / "module.html").read_text()
    _assert_every_tooltip_can_be_shown(html, entries[0].name)


def test_disorder_tooltips_can_all_be_shown(tmp_path: Path) -> None:
    _assert_every_tooltip_can_be_shown(_rendered_pill_page(tmp_path), "disorder")
