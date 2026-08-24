"""Unit tests for the entity-reference resolver (issue #9193).

`tests/test_data.py::test_entity_ref_foreign_keys` exercises this against real
content; these cover the resolution rules themselves — in particular the three
sections that are *not* keyed on `name`, and the two ways a reference is
skipped rather than failed.
"""

import pytest

from dismech.entity_refs import (
    EntityRef,
    SECTION_KEYS,
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
    import yaml

    schema = yaml.safe_load(open("src/dismech/schema/dismech.yaml"))
    disease_slots = set(schema["classes"]["Disease"]["slots"])
    for kind, (slot, key_slots) in SECTION_KEYS.items():
        assert slot in disease_slots, f"{kind} -> unknown slot {slot}"
        assert key_slots, kind
