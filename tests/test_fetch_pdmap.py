"""A disease-map reaction is a lead, so the fetcher must not dress it as evidence.

``scripts/fetch_pdmap.py`` turns a MINERVA instance's REST responses into lead
files under ``pathways/``. Nothing downstream validates those files, so these
tests pin the transformations a curator relies on: which annotation types become
CURIEs (and in which case), that a reaction's map-native type and modifier
polarity survive verbatim rather than being translated into a dismech predicate,
and that an unreferenced reaction is dropped by default -- it is structure, not a
lead.

Offline: every test drives the pure functions with MINERVA-shaped dicts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import fetch_pdmap  # noqa: E402


def protein(element_id: int, name: str, hgnc: str, symbol: str | None = None) -> dict:
    return {
        "id": element_id,
        "name": name,
        "type": "Protein",
        "fullName": symbol,
        "references": [
            {"type": "HGNC", "resource": hgnc},
            {"type": "HGNC_SYMBOL", "resource": name},
            {"type": "INCHIKEY", "resource": "ignored"},
            {"type": "REFSEQ", "resource": "NM_000000"},
        ],
    }


def reaction(reaction_id: str, kind: str, pmids: list[str], **parts: object) -> dict:
    return {
        "id": hash(reaction_id) % 100000,
        "reactionId": reaction_id,
        "type": kind,
        "name": "",
        "references": [
            {
                "type": "PUBMED",
                "resource": pmid,
                "article": {
                    "title": f"Study {pmid}",
                    "journal": "J Test",
                    "year": 2020,
                },
            }
            for pmid in pmids
        ],
        **parts,
    }


def test_hgnc_curies_are_lowercased_to_match_the_repository_convention():
    # `hgnc:12435`, not `HGNC:12435` -- see the CURIE-casing rule in CLAUDE.md.
    assert fetch_pdmap.curies([{"type": "HGNC", "resource": "12435"}]) == ["hgnc:12435"]


def test_structure_and_registry_annotations_are_dropped_but_biology_is_kept():
    identifiers = fetch_pdmap.curies(
        [
            {"type": "CHEBI", "resource": "16240"},
            {"type": "UNIPROT", "resource": "P10599"},
            {"type": "GO", "resource": "0006915"},
            {"type": "INCHI", "resource": "InChI=1S/H2O2/c1-2/h1-2H"},
            {"type": "STITCH", "resource": "CIDs00000784"},
            {"type": "VMH_METABOLITE", "resource": "h2o2"},
        ]
    )
    assert identifiers == ["CHEBI:16240", "GO:0006915", "uniprot:P10599"]


def test_an_unreferenced_reaction_is_not_a_lead_and_is_dropped_by_default():
    elements = [protein(1, "LRRK2", "18618"), protein(2, "RAB10", "9762")]
    reactions = [
        reaction(
            "r1",
            "State transition",
            ["26546614"],
            reactants=[{"aliasId": 1}],
            products=[{"aliasId": 2}],
        ),
        reaction("r2", "State transition", [], reactants=[{"aliasId": 1}]),
    ]

    kept, _, _ = fetch_pdmap.build_submap(reactions, elements, referenced_only=True)
    assert [r["id"] for r in kept] == ["r1"]

    both, _, _ = fetch_pdmap.build_submap(reactions, elements, referenced_only=False)
    assert [r["id"] for r in both] == ["r1", "r2"]


def test_map_native_reaction_and_modifier_types_are_recorded_verbatim():
    # The map's polarity is not translated into a dismech causal predicate:
    # `downstream` edges are unsigned, and the translation is a curation call.
    elements = [protein(1, "LRRK2", "18618"), protein(2, "RAB10", "9762")]
    kept, _, _ = fetch_pdmap.build_submap(
        [
            reaction(
                "lra9",
                "Negative influence",
                ["26546614"],
                reactants=[{"aliasId": 1}],
                products=[{"aliasId": 2}],
                modifiers=[{"aliasId": 2, "type": "Inhibition"}],
            )
        ],
        elements,
        referenced_only=True,
    )
    assert kept[0]["type"] == "Negative influence"
    assert kept[0]["modifiers"] == [{"type": "Inhibition", "element": "RAB10"}]
    assert kept[0]["pmids"] == ["PMID:26546614"]


def test_one_species_drawn_twice_yields_one_element_record():
    # MINERVA returns a record per glyph, so the same protein arrives repeatedly.
    elements = [protein(1, "LRRK2", "18618"), protein(2, "LRRK2", "18618")]
    reactions = [
        reaction(
            "r1",
            "State transition",
            ["26546614"],
            reactants=[{"aliasId": 1}],
            products=[{"aliasId": 2}],
        )
    ]
    _, element_records, _ = fetch_pdmap.build_submap(reactions, elements, True)
    assert [e["name"] for e in element_records] == ["LRRK2"]


def test_only_referenced_elements_are_emitted_and_compartments_never_are():
    elements = [
        protein(1, "LRRK2", "18618"),
        protein(2, "RAB10", "9762"),
        protein(3, "UNUSED", "1"),
        {"id": 4, "name": "neuron", "type": "Compartment", "references": []},
    ]
    reactions = [
        reaction(
            "r1",
            "State transition",
            ["26546614"],
            reactants=[{"aliasId": 1}, {"aliasId": 4}],
            products=[{"aliasId": 2}],
        )
    ]
    _, element_records, _ = fetch_pdmap.build_submap(reactions, elements, True)
    assert [e["name"] for e in element_records] == ["LRRK2", "RAB10"]


def test_article_metadata_is_captured_per_pmid_for_the_lead_table():
    elements = [protein(1, "LRRK2", "18618")]
    _, _, meta = fetch_pdmap.build_submap(
        [reaction("r1", "State transition", ["26546614"], reactants=[{"aliasId": 1}])],
        elements,
        True,
    )
    assert meta["26546614"] == {
        "title": "Study 26546614",
        "journal": "J Test",
        "year": 2020,
    }


def test_submap_names_become_stable_file_slugs():
    assert fetch_pdmap.slugify("Mitochondrial and ROS metabolism") == (
        "mitochondrial_and_ros_metabolism"
    )
    assert (
        fetch_pdmap.slugify("Ubiquitin-proteasome system")
        == "ubiquitin_proteasome_system"
    )
    assert fetch_pdmap.slugify("!!!") == "submap"
