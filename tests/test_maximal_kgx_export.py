"""Tests for the maximal KGX export (dismech.export.maximal_kgx_export)."""

from dismech.export.maximal_kgx_export import (
    GraphAccumulator,
    export_kb,
    process_comorbidity,
    process_entry,
    subtype_node_id,
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

    subtype_id = subtype_node_id("Test_Disease", "Type 1")
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


def test_genetic_context_origin_is_a_node_property_without_a_gene():
    """A fusion lesion with no bound gene still carries its somatic origin."""
    record = {
        "name": "Fusion Disease",
        "pathophysiology": [
            {
                "name": "Somatic PML-RARA Fusion",
                "genetic_context": {"variant_origin": "SOMATIC"},
            }
        ],
    }
    acc = GraphAccumulator()
    process_entry(acc, "Fusion_Disease", record, "disorder")
    node = acc.nodes[
        pathophysiology_node_id("Fusion_Disease", "Somatic PML-RARA Fusion")
    ]
    assert node["variant_origin"] == "SOMATIC"
    assert not any(p == "dismech:has_causal_variant_in" for _, p, _ in acc.edges)

    acc = GraphAccumulator()
    process_entry(acc, "Test_Disease", DISORDER, "disorder")
    kras = acc.nodes[
        pathophysiology_node_id("Test_Disease", "KRAS Oncogene Activation")
    ]
    assert kras["variant_origin"] == "SOMATIC"
    assert kras["functional_impact_category"] == "GAIN_OF_FUNCTION"


def test_shared_mondo_curie_keeps_entries_distinct():
    shared = {"term": {"id": "MONDO:0005061", "label": "lung adenocarcinoma"}}
    acc = GraphAccumulator()
    shared_curies = frozenset({"MONDO:0005061"})
    id_a = process_entry(
        acc,
        "EGFR_Mutant_NSCLC",
        {"name": "A", "disease_term": shared},
        "disorder",
        shared_curies,
    )
    id_b = process_entry(
        acc,
        "KRAS_G12C_Mutant_NSCLC",
        {"name": "B", "disease_term": shared},
        "disorder",
        shared_curies,
    )
    assert id_a == "dismech:EGFR_Mutant_NSCLC"
    assert id_b == "dismech:KRAS_G12C_Mutant_NSCLC"
    assert (id_a, "dismech:grounded_to", "MONDO:0005061") in acc.edges
    assert (id_b, "dismech:grounded_to", "MONDO:0005061") in acc.edges


def test_subtype_does_not_merge_with_same_named_genetic_node():
    record = {
        "name": "Clash Disease",
        "genetic": [
            {
                "name": "DKC1",
                "gene_term": {"term": {"id": "hgnc:2890", "label": "DKC1"}},
            }
        ],
        "has_subtypes": [{"name": "DKC1"}],
    }
    acc = GraphAccumulator()
    entry_id = process_entry(acc, "Clash_Disease", record, "disorder")
    genetic_id = pathophysiology_node_id("Clash_Disease", "DKC1")
    subtype_id = subtype_node_id("Clash_Disease", "DKC1")
    assert genetic_id != subtype_id
    assert acc.nodes[genetic_id]["category"] == ["dismech:GeneticNode"]
    assert acc.nodes[subtype_id]["category"] == ["dismech:Subtype"]
    assert (subtype_id, "dismech:subtype_of", entry_id) in acc.edges


def test_process_comorbidity_falls_back_to_entry_slug():
    acc = GraphAccumulator()
    process_comorbidity(
        acc,
        "com_Influenza__Alzheimer_Disease",
        {
            "disease_a": {"slug": "Influenza"},
            "disease_b": {"slug": "Alzheimer_Disease"},
        },
        {"Influenza": "MONDO:0005812", "Alzheimer_Disease": "MONDO:0004975"},
    )
    assert ("MONDO:0005812", "dismech:comorbid_with", "MONDO:0004975") in acc.edges


def test_add_node_widens_category_and_edge_ids_are_stable():
    acc = GraphAccumulator()
    acc.add_node("hgnc:7739", "NEFL", "biolink:MolecularEntity")
    acc.add_node("hgnc:7739", "NEFL", "biolink:Gene")
    assert acc.nodes["hgnc:7739"]["category"] == [
        "biolink:MolecularEntity",
        "biolink:Gene",
    ]

    first, second = GraphAccumulator(), GraphAccumulator()
    first.add_edge("a", "p", "b", "s", "Entry")
    second.add_edge("x", "p", "y", "s", "Other")
    second.add_edge("a", "p", "b", "s", "Entry")
    assert first.edges[("a", "p", "b")]["id"] == second.edges[("a", "p", "b")]["id"]
    assert first.edges[("a", "p", "b")]["id"].startswith("urn:uuid:")


def test_export_kb_marks_shared_curies(tmp_path):
    kb = tmp_path / "kb"
    (kb / "disorders").mkdir(parents=True)
    body = "name: {name}\ndisease_term:\n  term:\n    id: MONDO:0000100\n    label: x\n"
    (kb / "disorders" / "A.yaml").write_text(body.format(name="A"))
    (kb / "disorders" / "B.yaml").write_text(body.format(name="B"))
    (kb / "disorders" / "C.yaml").write_text(
        "name: C\ndisease_term:\n  term:\n    id: MONDO:0000200\n    label: c\n"
    )
    out = tmp_path / "out"
    export_kb(kb, out)
    ids = {
        line.split('"id": "')[1].split('"')[0]
        for line in (out / "maximal_nodes.jsonl").read_text().splitlines()
    }
    assert {"dismech:A", "dismech:B", "MONDO:0000100", "MONDO:0000200"} <= ids


def test_process_comorbidity_expands_composite_side():
    acc = GraphAccumulator()
    process_comorbidity(
        acc,
        "com_T2D__LSC__PN",
        {
            "disease_a": {"slug": "T2D"},
            "disease_b": {
                "composition": "UNION",
                "components": [{"slug": "LSC"}, {"slug": "PN"}],
            },
        },
        {"T2D": "MONDO:1", "LSC": "MONDO:2", "PN": "MONDO:3"},
    )
    assert ("MONDO:1", "dismech:comorbid_with", "MONDO:2") in acc.edges
    assert ("MONDO:1", "dismech:comorbid_with", "MONDO:3") in acc.edges
