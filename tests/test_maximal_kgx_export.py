"""Tests for the maximal KGX export (dismech.export.maximal_kgx_export)."""

from dismech.export.maximal_kgx_export import (
    GraphAccumulator,
    process_comorbidity,
    process_entry,
)
from dismech.export.sepio_export import pathophysiology_node_id

DISORDER = {
    "name": "Test Disease",
    "disease_term": {"term": {"id": "MONDO:0000001", "label": "test disease"}},
    "pathophysiology": [
        {
            "name": "KRAS Oncogene Activation",
            "genetic_context": {
                "variant_origin": "SOMATIC",
                "functional_impact_category": "GAIN_OF_FUNCTION",
                "gene": {
                    "preferred_term": "KRAS",
                    "term": {"id": "hgnc:6407", "label": "KRAS"},
                },
            },
            "downstream": [{"target": "Fibrosis"}],
        },
        {
            "name": "Mesenchymal Cell Activation",
            "conforms_to": "fibrotic_response#Mesenchymal Cell Activation",
            "cell_types": [
                {
                    "preferred_term": "hepatic stellate cell",
                    "term": {"id": "CL:0000632", "label": "hepatic stellate cell"},
                }
            ],
            "downstream": [{"target": "Fibrosis"}],
        },
        {"name": "Fibrosis"},
    ],
    "phenotypes": [
        {
            "name": "Jaundice",
            "phenotype_term": {"term": {"id": "HP:0000952", "label": "Jaundice"}},
        }
    ],
    "has_subtypes": [
        {
            "name": "Type 1",
            "subtype_term": {"term": {"id": "MONDO:0000002", "label": "test subtype"}},
        }
    ],
}


def test_process_entry_promotes_pathograph_nodes():
    acc = GraphAccumulator()
    entry_id = process_entry(acc, "Test_Disease", DISORDER, "disorder")

    assert entry_id == "MONDO:0000001"
    node_id = pathophysiology_node_id("Test_Disease", "Mesenchymal Cell Activation")
    assert node_id == "dismech:Test_Disease#Mesenchymal_Cell_Activation"
    assert acc.nodes[node_id]["category"] == ["dismech:PathophysiologyNode"]

    # membership, causal, grounding, and conformance edges
    triples = set(acc.edges)
    assert (entry_id, "dismech:has_graph_node", node_id) in triples
    fibrosis_id = pathophysiology_node_id("Test_Disease", "Fibrosis")
    assert any(s == node_id and o == fibrosis_id for s, _, o in triples)
    assert (node_id, "dismech:involves_cell_type", "CL:0000632") in triples
    assert (
        node_id,
        "dismech:conforms_to",
        pathophysiology_node_id("fibrotic_response", "Mesenchymal Cell Activation"),
    ) in triples


def test_genetic_context_exports_with_variant_origin():
    acc = GraphAccumulator()
    process_entry(acc, "Test_Disease", DISORDER, "disorder")
    kras_node = pathophysiology_node_id("Test_Disease", "KRAS Oncogene Activation")
    edge = acc.edges[(kras_node, "dismech:has_causal_variant_in", "hgnc:6407")]
    assert edge["variant_origin"] == "SOMATIC"
    assert edge["functional_impact_category"] == "GAIN_OF_FUNCTION"
    assert acc.nodes["hgnc:6407"]["category"] == ["biolink:Gene"]


def test_process_entry_grounds_phenotypes_and_subtypes():
    acc = GraphAccumulator()
    process_entry(acc, "Test_Disease", DISORDER, "disorder")
    triples = set(acc.edges)

    jaundice_id = pathophysiology_node_id("Test_Disease", "Jaundice")
    assert (jaundice_id, "dismech:grounded_to", "HP:0000952") in triples
    assert acc.nodes["HP:0000952"]["category"] == ["biolink:PhenotypicFeature"]

    subtype_id = pathophysiology_node_id("Test_Disease", "Type 1")
    assert acc.nodes[subtype_id]["category"] == ["dismech:Subtype"]
    assert (subtype_id, "dismech:subtype_of", "MONDO:0000001") in triples
    assert (subtype_id, "dismech:grounded_to", "MONDO:0000002") in triples


def test_module_entry_id_uses_file_stem():
    acc = GraphAccumulator()
    entry_id = process_entry(
        acc, "fibrotic_response", {"name": "Fibrotic Response Module"}, "module"
    )
    assert entry_id == "dismech:fibrotic_response"
    assert acc.nodes[entry_id]["category"] == ["dismech:MechanismModule"]


def test_process_comorbidity_links_disease_pair():
    acc = GraphAccumulator()
    process_comorbidity(
        acc,
        "com_A__B",
        {
            "disease_a": {"term": {"id": "MONDO:0000010", "label": "a"}},
            "disease_b": {"term": {"id": "MONDO:0000011", "label": "b"}},
            "directionality": "UNKNOWN",
        },
    )
    assert ("MONDO:0000010", "dismech:comorbid_with", "MONDO:0000011") in acc.edges
