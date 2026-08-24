"""Unit tests for the entity-reference resolver (issue #9193).

`tests/test_data.py::test_entity_ref_foreign_keys` exercises this against real
content; these cover the resolution rules themselves — in particular the three
sections that are *not* keyed on `name`, and the two ways a reference is
skipped rather than failed.
"""

import pathlib
import re

import pytest
import yaml

from dismech import render
from dismech.entity_refs import (
    SECTION_KEYS,
    EntityRef,
    entity_ref_index,
    iter_entity_refs,
    parse_entity_ref,
    resolve_entity_ref,
    section_items,
)

ENTRY = {
    "name": "Test Disease",
    "pathophysiology": [{"name": "Node A"}, {"name": "Node B"}],
    "phenotypes": [{"name": "Pheno A"}],
    "treatments": [{"name": "Drug A"}],
    "genetic": [{"name": "GENE1", "variants": [{"name": "Nested Variant"}]}],
    "variants": [{"name": "Top Variant"}],
    "mechanistic_hypotheses": [
        {"hypothesis_group_id": "canonical_model", "hypothesis_label": "Canonical"}
    ],
    "prevalence": [{"population": "Worldwide"}],
    "progression": [{"phase": "Chronic phase"}],
    "datasets": [{"accession": "geo:GSE1", "title": "A dataset"}],
    "animal_models": [{"species": "Mus musculus", "genotype": "Foo-/-"}],
    "discussions": [{"discussion_id": "gap_one"}],
    "clinical_burden": {"burden_level": "SEVERE"},
}


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("pathophysiology#Node A", EntityRef(None, "pathophysiology", "Node A")),
        (
            "Liver_Cirrhosis:pathophysiology#Hepatic Stellate Cell Activation",
            EntityRef(
                "Liver_Cirrhosis",
                "pathophysiology",
                "Hepatic Stellate Cell Activation",
            ),
        ),
        # A name may itself contain a '#'; only the first splits.
        ("phenotype#Grade #2", EntityRef(None, "phenotype", "Grade #2")),
    ],
)
def test_parse_entity_ref(raw, expected):
    assert parse_entity_ref(raw) == expected


@pytest.mark.parametrize("raw", ["Node A", "", None, 42, "#orphan"])
def test_parse_rejects_non_references(raw):
    """A `target:` carrying a plain node name is not an entity reference."""
    assert parse_entity_ref(raw) is None


@pytest.mark.parametrize(
    "ref",
    [
        "pathophysiology#Node A",
        "phenotype#Pheno A",
        "phenotypes#Pheno A",  # both spellings resolve
        "treatment#Drug A",
        "treatments#Drug A",
        "genetic#GENE1",
        "disease#Test Disease",  # virtual whole-entry anchor
        "mechanistic_hypothesis#canonical_model",  # keyed on hypothesis_group_id
        "mechanistic_hypothesis#Canonical",  # ...and on the human-readable label
        "prevalence#Worldwide",  # keyed on population
        "progression#Chronic phase",  # keyed on phase
        "dataset#geo:GSE1",  # keyed on accession
        "dataset#A dataset",  # ...or title
        "animal_models#Mus musculus",  # unnamed model, keyed on species
        "animal_models#Foo-/-",
        "discussion#gap_one",
        "variant#Top Variant",
        "variant#Nested Variant",  # nested under genetic[].variants
    ],
)
def test_resolves(ref):
    assert resolve_entity_ref(ENTRY, ref) is True


@pytest.mark.parametrize(
    "ref",
    [
        "pathophysiology#Node C",
        "phenotypes#Nope",
        "disease#Other Disease",
        "mechanistic_hypothesis#other_model",
        "prevalence#Elsewhere",
        # A section absent from the entry dangles rather than being skipped.
        "biochemical#Anything",
    ],
)
def test_dangles(ref):
    assert resolve_entity_ref(ENTRY, ref) is False


@pytest.mark.parametrize(
    "ref",
    [
        "Liver_Cirrhosis:pathophysiology#Hepatic Stellate Cell Activation",
        "gene#LRRK2",  # prefix absent from SECTION_KEYS
        "biological_process#tRNA processing",
        "Node A",  # not a reference at all
    ],
)
def test_skipped_never_fails(ref):
    """An unmapped prefix is a gap in the map, not a defect in the content."""
    assert resolve_entity_ref(ENTRY, ref) is None


def test_section_items_merges_nested_variants():
    names = {v["name"] for v in section_items(ENTRY, "variants")}
    assert names == {"Top Variant", "Nested Variant"}
    assert [n["name"] for n in section_items(ENTRY, "pathophysiology")] == [
        "Node A",
        "Node B",
    ]
    assert section_items(ENTRY, "clinical_trials") == []


def test_entity_ref_index_covers_every_resolvable_ref():
    index = entity_ref_index(ENTRY)
    assert index["disease#Test Disease"] == [ENTRY]
    assert index["pathophysiology#Node A"] == [ENTRY["pathophysiology"][0]]
    # Every key the index emits must also resolve, and vice versa.
    for key in index:
        assert resolve_entity_ref(ENTRY, key) is True


def test_iter_entity_refs_reports_paths():
    doc = {
        "discussions": [
            {
                "attaches_to": ["pathophysiology#Node A", "phenotype#Pheno A"],
                "proposed_experiments": [
                    {
                        "would_support": ["pathophysiology#Node B"],
                        "would_refute": ["pathophysiology#Node C"],
                        "perturbations": [{"target": "genetic#GENE1"}],
                        "readouts": [{"target": "Plain node name"}],
                    }
                ],
            }
        ],
        # `target` on a model link carries a plain name, not a reference.
        "animal_models": [{"modeled_mechanisms": [{"target": "Node A"}]}],
    }
    found = dict(iter_entity_refs(doc))
    assert found["discussions[0].attaches_to[0]"] == "pathophysiology#Node A"
    assert found["discussions[0].attaches_to[1]"] == "phenotype#Pheno A"
    assert (
        found["discussions[0].proposed_experiments[0].would_refute[0]"]
        == "pathophysiology#Node C"
    )
    assert (
        found["discussions[0].proposed_experiments[0].perturbations[0].target"]
        == "genetic#GENE1"
    )
    # Plain-name targets are yielded but parse to None, so they never fail.
    assert (
        parse_entity_ref(found["animal_models[0].modeled_mechanisms[0].target"]) is None
    )


def test_section_keys_point_at_real_disease_slots():
    """Every mapped section must name a slot the Disease class actually has."""
    schema = yaml.safe_load(open("src/dismech/schema/dismech.yaml"))
    disease_slots = set(schema["classes"]["Disease"]["slots"])
    for kind, (slot, key_slots) in SECTION_KEYS.items():
        assert slot in disease_slots, f"{kind} -> unknown slot {slot}"
        assert key_slots, kind


@pytest.mark.parametrize(
    "ref",
    [
        "prevalence#",  # the section as a whole, not one population
        "treatments#",
        "clinical_burden#",  # a singleton object with no name to anchor to
        "disease#",  # the entry as a whole
    ],
)
def test_whole_section_anchor_resolves(ref):
    """An empty anchor names the section itself (#9394)."""
    assert resolve_entity_ref(ENTRY, ref) is True


def test_whole_section_anchor_resolves_on_the_name_not_the_contents():
    """A section with no content still satisfies `<section>#`.

    The motivating case is a KNOWLEDGE_GAP attached to a section precisely
    because it is empty — `Spondyloepimetaphyseal_Dysplasia_Bieganski_Type`
    records that no disease-specific management is established and curates no
    `treatments:` at all. Requiring content would make that gap unattachable.
    """
    empty = {"name": "Bare Disease"}
    assert resolve_entity_ref(empty, "treatments#") is True
    assert resolve_entity_ref(empty, "clinical_burden#") is True
    # A misspelled or invented section is still caught — that is what the
    # check is for once contents are not required.
    assert resolve_entity_ref(empty, "treatmnets#") is None


def test_singleton_section_rejects_a_named_anchor():
    """`clinical_burden` has no `name`, so only the whole-section form works."""
    assert resolve_entity_ref(ENTRY, "clinical_burden#Anything") is False


def test_iter_entity_refs_walks_objects_inside_a_ref_slot():
    """A ref slot holding objects, or a mix, loses neither half (#9385 review).

    Every ref slot holds a string or a list of strings today, so this is
    forward-looking — but the two ways of getting it wrong are both silent.
    Stopping at the slot drops references nested underneath it; recursing past
    the whole list drops the plain strings beside them.
    """
    doc = {
        "discussions": [
            {
                "attaches_to": [
                    "pathophysiology#Node A",
                    {"target": "phenotype#Pheno A"},
                    "genetic#GENE1",
                ]
            }
        ],
        "experiments": [{"target": {"nested": {"target": "treatments#Drug A"}}}],
    }
    found = dict(iter_entity_refs(doc))

    # The strings beside the object survive...
    assert found["discussions[0].attaches_to[0]"] == "pathophysiology#Node A"
    assert found["discussions[0].attaches_to[2]"] == "genetic#GENE1"
    # ...and so does the reference inside it.
    assert found["discussions[0].attaches_to[1].target"] == "phenotype#Pheno A"
    # An object directly under a ref slot is walked rather than stopped at.
    assert found["experiments[0].target.nested.target"] == "treatments#Drug A"


def test_semantic_ref_index_covers_every_annotated_section(tmp_path):
    """Guard the renderer's ordering dependency (#9193 review, suggestion 5).

    `_build_semantic_ref_index` relies on the `_annotate_*` passes having run,
    and silently emits no link for an item without an `_anchor_id` — a quietly
    missing link rather than an error. This runs the same passes
    `render_disorder` does, in the same order, over the two entries the issue
    named as exercising the awkward prefixes, and checks two things: every href
    the index emits is an id the rendered page actually carries — which catches
    breakage from *any* of the passes on these fixtures — and that the seven ref
    kinds listed below are actually exercised rather than silently absent.
    Dropping or reordering a pass fails here rather than quietly losing links.

    The kind list is not one-per-pass: `_annotate_variant_anchors`,
    `_annotate_external_assertion_anchors` and `_annotate_model_links` are
    covered only by the href-resolves assertion, because these two fixtures
    carry no `variant#`, `external_assertions#` or model references to name.
    """
    # HPAH carries inheritance/clinical_trials/genetic; Gorlin carries the
    # hypotheses. Neither has all of them, which is the point of using both.
    sources = [
        "kb/disorders/Heritable_Pulmonary_Arterial_Hypertension.yaml",
        "kb/disorders/Gorlin_Syndrome.yaml",
    ]
    seen_kinds: set[str] = set()

    for name in sources:
        src = pathlib.Path(name)
        disorder = render.load_disorder(src)

        render._annotate_model_links(disorder)
        render._annotate_card_anchors(disorder)
        render._annotate_variant_anchors(disorder)
        render._annotate_external_assertion_anchors(disorder)
        render._annotate_ref_target_anchors(disorder)
        render._annotate_hypothesis_group_links(disorder)
        index = render._build_semantic_ref_index(disorder)

        out = tmp_path / f"{src.stem}.html"
        render.render_disorder(src, out)
        ids = set(re.findall(r'\sid="([^"]+)"', out.read_text()))

        for ref, href in index.items():
            assert href.lstrip("#") in ids, f"{src.stem}: {ref} -> {href} not on page"
            seen_kinds.add(ref.split("#", 1)[0])

    # Kinds these two fixtures do carry, spanning the card-anchor and
    # ref-target passes, the hypothesis pass, and the two the index
    # resolves inline.
    for kind in (
        "pathophysiology",  # inline fallback in the index
        "disease",  # virtual whole-entry anchor, also inline
        "genetic",  # _annotate_card_anchors
        "treatments",  # _annotate_card_anchors
        "inheritance",  # _annotate_ref_target_anchors
        "clinical_trials",  # _annotate_ref_target_anchors
        "mechanistic_hypothesis",  # _annotate_hypothesis_group_links
    ):
        assert kind in seen_kinds, f"no semantic-ref index entries for {kind}#"
