"""Tests for model metadata in pathograph JSON."""

import json

from dismech.graph import (
    _genetic_item_infers_mechanism_edges,
    build_causal_graph,
    graph_to_json,
    model_edge_predicate,
)


def test_genetic_item_infers_mechanism_edges_respects_relationship_type() -> None:
    assert _genetic_item_infers_mechanism_edges({"relationship_type": "CAUSATIVE"})
    assert _genetic_item_infers_mechanism_edges({"association": "Risk factor"})

    assert not _genetic_item_infers_mechanism_edges({"relationship_type": "MODIFIER"})
    assert not _genetic_item_infers_mechanism_edges({"association": "Disease modifier"})
    assert not _genetic_item_infers_mechanism_edges({"relationship_type": "PROTECTIVE"})


def test_graph_to_json_includes_gene_ids_and_structured_genetic_metadata() -> None:
    disorder = {
        "name": "AIP example",
        "pathophysiology": [
            {
                "name": "Biallelic AIP-deficient somatotroph state",
                "gene": {
                    "preferred_term": "AIP",
                    "modifier": "ABSENT",
                    "term": {"id": "hgnc:358", "label": "AIP"},
                },
                "genetic_context": {
                    "gene": {
                        "preferred_term": "AIP",
                        "term": {"id": "hgnc:358", "label": "AIP"},
                    },
                    "variant_origin": "GERMLINE_AND_SOMATIC",
                    "allelic_hit_role": "BIALLELIC_INACTIVATION",
                    "allelic_events": ["BIALLELIC_INACTIVATION"],
                    "functional_impact_category": "LOSS_OF_FUNCTION",
                },
            }
        ],
        "genetic": [
            {
                "name": "AIP",
                "gene_term": {
                    "preferred_term": "AIP",
                    "term": {"id": "hgnc:358", "label": "AIP"},
                },
                "association": (
                    "Germline predisposition with somatic second-hit inactivation"
                ),
                "relationship_type": "SUSCEPTIBILITY",
                "variant_origin": "GERMLINE_AND_SOMATIC",
            }
        ],
    }

    graph = build_causal_graph(disorder)
    data = json.loads(graph_to_json(graph, disorder))
    node_meta = {node["id"]: node.get("meta", {}) for node in data["nodes"]}

    assert node_meta["AIP"]["genes"] == ["AIP"]
    assert node_meta["AIP"]["gene_terms"] == [{"label": "AIP", "id": "hgnc:358"}]
    assert node_meta["AIP"]["relationship_type"] == "SUSCEPTIBILITY"
    assert node_meta["AIP"]["variant_origin"] == "GERMLINE_AND_SOMATIC"
    assert node_meta["Biallelic AIP-deficient somatotroph state"]["gene_terms"] == [
        {"label": "AIP", "id": "hgnc:358", "modifier": "ABSENT"}
    ]
    assert node_meta["Biallelic AIP-deficient somatotroph state"][
        "genetic_context"
    ] == {
        "variant_origin": "GERMLINE_AND_SOMATIC",
        "allelic_hit_role": "BIALLELIC_INACTIVATION",
        "functional_impact_category": "LOSS_OF_FUNCTION",
        "allelic_events": ["BIALLELIC_INACTIVATION"],
        "gene_terms": [{"label": "AIP", "id": "hgnc:358"}],
    }


def test_graph_to_json_includes_experimental_and_computational_model_links() -> None:
    """Pathophysiology nodes should expose linked model metadata in graph JSON."""
    disorder = {
        "name": "Example Disease",
        "pathophysiology": [
            {
                "name": "CFTR Dysfunction",
                "downstream": [{"target": "Bronchiectasis"}],
            }
        ],
        "phenotypes": [{"name": "Bronchiectasis"}],
        "experimental_models": [
            {
                "name": "Patient-derived airway organoid",
                "experimental_model_type": "ORGANOID",
                "namo_type": "namo:Organoid",
                "modeled_mechanisms": [
                    {
                        "target": "CFTR Dysfunction",
                        "description": "Assays epithelial CFTR rescue in patient-derived tissue.",
                    }
                ],
            }
        ],
        "computational_models": [
            {
                "name": "Airway signaling simulator",
                "model_type": "MECHANISTIC_NETWORK",
                "model_software": "PySB",
                "model_format": "Python",
                "modeled_mechanisms": [
                    {
                        "target": "CFTR Dysfunction",
                        "description": "Encodes CFTR-dependent signaling states for in silico perturbation.",
                    }
                ],
            }
        ],
    }

    graph = build_causal_graph(disorder)
    data = json.loads(graph_to_json(graph, disorder))
    node = next(node for node in data["nodes"] if node["id"] == "CFTR Dysfunction")

    assert node["meta"]["experimental_models"] == [
        {
            "name": "Patient-derived airway organoid",
            "model_type": "ORGANOID",
            "namo_type": "namo:Organoid",
            "description": "Assays epithelial CFTR rescue in patient-derived tissue.",
        }
    ]
    assert node["meta"]["computational_models"] == [
        {
            "name": "Airway signaling simulator",
            "model_type": "MECHANISTIC_NETWORK",
            "model_software": "PySB",
            "model_format": "Python",
            "description": "Encodes CFTR-dependent signaling states for in silico perturbation.",
        }
    ]


def test_graph_to_json_includes_animal_model_links() -> None:
    """Animal model links should surface on the node, labelled and typed."""
    disorder = {
        "name": "Example Disease",
        "pathophysiology": [
            {
                "name": "Motor Neuron Degeneration",
                "downstream": [{"target": "Muscle weakness"}],
            }
        ],
        "phenotypes": [{"name": "Muscle weakness"}],
        "animal_models": [
            {
                "name": "SOD1-G93A transgenic mouse",
                "species": "Mus musculus",
                "genotype": "SOD1-G93A",
                "category": "Transgenic mouse",
                "modeled_mechanisms": [
                    {
                        "target": "Motor Neuron Degeneration",
                        "relationship": "RECAPITULATES",
                        "fidelity": "MODERATE",
                        "description": "Progressive spinal motor neuron loss.",
                    }
                ],
            },
            {
                # No `name`: falls back to a genotype/species label rather than
                # being dropped, as the 400 pre-existing entries have none.
                "species": "Danio rerio",
                "genotype": "sod1-null",
                "modeled_mechanisms": [
                    {
                        "target": "Motor Neuron Degeneration",
                        "relationship": "FAILS_TO_RECAPITULATE",
                    }
                ],
            },
        ],
    }

    graph = build_causal_graph(disorder)
    data = json.loads(graph_to_json(graph, disorder))
    node = next(
        node for node in data["nodes"] if node["id"] == "Motor Neuron Degeneration"
    )

    assert node["meta"]["animal_models"] == [
        {
            "name": "SOD1-G93A transgenic mouse",
            "species": "Mus musculus",
            "genotype": "SOD1-G93A",
            "category": "Transgenic mouse",
            "relationship": "RECAPITULATES",
            "fidelity": "MODERATE",
            "description": "Progressive spinal motor neuron loss.",
        },
        {
            "name": "sod1-null Danio rerio",
            "species": "Danio rerio",
            "genotype": "sod1-null",
            "relationship": "FAILS_TO_RECAPITULATE",
        },
    ]

    # The models must also be real graph nodes joined by `models` edges, not
    # only node metadata -- otherwise downstream consumers keyed on edges (the
    # cx2 exporter's edge-detail lookup) have nothing to attach to.
    animal_nodes = {n["id"] for n in data["nodes"] if n["node_type"] == "animal_model"}
    assert animal_nodes == {"SOD1-G93A transgenic mouse", "sod1-null Danio rerio"}

    # The predicate carries the curated claim, so the falsified model is not
    # drawn as an ordinary `models` arrow asserting the opposite.
    model_edges = {
        (e["source"], e["target"], e["predicate"], e.get("relationship"))
        for e in data["edges"]
        if e["source"] in animal_nodes
    }
    assert model_edges == {
        (
            "SOD1-G93A transgenic mouse",
            "Motor Neuron Degeneration",
            "models",
            "RECAPITULATES",
        ),
        (
            "sod1-null Danio rerio",
            "Motor Neuron Degeneration",
            "fails_to_model",
            "FAILS_TO_RECAPITULATE",
        ),
    }
    fidelity = {
        e["source"]: e.get("fidelity")
        for e in data["edges"]
        if e["source"] in animal_nodes
    }
    assert fidelity["SOD1-G93A transgenic mouse"] == "MODERATE"


def test_model_edge_predicate_maps_every_relationship() -> None:
    """Each relationship gets its own predicate; an absent one stays `models`."""
    assert model_edge_predicate(None) == "models"
    assert model_edge_predicate("RECAPITULATES") == "models"
    assert model_edge_predicate("PARTIALLY_RECAPITULATES") == "partially_models"
    assert model_edge_predicate("FAILS_TO_RECAPITULATE") == "fails_to_model"
    assert model_edge_predicate("PERTURBS") == "perturbs"
    assert model_edge_predicate("MEASURES") == "measures"
    assert model_edge_predicate("RESCUES") == "rescues"
    # An unrecognized value degrades to the neutral predicate rather than
    # inventing one or raising.
    assert model_edge_predicate("SOMETHING_NEW") == "models"


def test_animal_models_without_mechanism_links_stay_out_of_the_graph() -> None:
    """An animal model with no `modeled_mechanisms` produces no node or edge.

    This is what keeps the ~400 legacy animal-model entries from flooding every
    pathograph: they opt in by declaring mechanism links, exactly as the
    experimental and computational model sections do.
    """
    disorder = {
        "name": "Example Disease",
        "pathophysiology": [
            {
                "name": "Motor Neuron Degeneration",
                "downstream": [{"target": "Muscle weakness"}],
            }
        ],
        "phenotypes": [{"name": "Muscle weakness"}],
        "animal_models": [
            {"species": "Mus musculus", "genotype": "Msx1-null"},
        ],
    }

    graph = build_causal_graph(disorder)
    data = json.loads(graph_to_json(graph, disorder))

    assert not [n for n in data["nodes"] if n["node_type"] == "animal_model"]
    assert not [e for e in data["edges"] if e.get("predicate") == "models"]


def test_build_causal_graph_includes_linked_models_treatments_and_genetics() -> None:
    """Linked non-causal content should now participate in the pathograph."""
    disorder = {
        "name": "Example Disease",
        "pathophysiology": [
            {
                "name": "CFTR Dysfunction",
                "gene": {
                    "preferred_term": "CFTR",
                    "term": {"id": "hgnc:1884", "label": "CFTR"},
                },
                "downstream": [{"target": "Bronchiectasis"}],
            }
        ],
        "phenotypes": [
            {
                "name": "Bronchiectasis",
                "phenotype_term": {
                    "preferred_term": "Bronchiectasis",
                    "term": {"id": "HP:0002110", "label": "Bronchiectasis"},
                },
            }
        ],
        "genetic": [
            {
                "name": "CFTR",
                "association": "Causative",
                "variants": [{"name": "F508del"}],
            },
            {
                "name": "CFTR modifier locus",
                "association": "Disease modifier",
                "gene_term": {
                    "preferred_term": "CFTR",
                    "term": {"id": "hgnc:1884", "label": "CFTR"},
                },
            },
        ],
        "treatments": [
            {
                "name": "Ivacaftor",
                "target_mechanisms": [{"target": "CFTR Dysfunction"}],
                "target_phenotypes": [
                    {
                        "preferred_term": "Bronchiectasis",
                        "term": {"id": "HP:0002110", "label": "Bronchiectasis"},
                    }
                ],
            }
        ],
        "experimental_models": [
            {
                "name": "Patient-derived airway organoid",
                "experimental_model_type": "ORGANOID",
                "modeled_mechanisms": [{"target": "CFTR Dysfunction"}],
            }
        ],
        "computational_models": [
            {
                "name": "CFTR network model",
                "model_type": "MECHANISTIC_NETWORK",
                "modeled_mechanisms": [{"target": "CFTR Dysfunction"}],
            }
        ],
    }

    graph = build_causal_graph(disorder)
    edges = {(edge.source, edge.target, edge.predicate) for edge in graph.edges}

    assert ("Patient-derived airway organoid", "CFTR Dysfunction", "models") in edges
    assert ("CFTR network model", "CFTR Dysfunction", "models") in edges
    assert ("Ivacaftor", "CFTR Dysfunction", "targets") in edges
    assert ("Ivacaftor", "Bronchiectasis", "treats") in edges
    assert ("CFTR", "CFTR Dysfunction", "contributes_to") in edges
    assert ("CFTR modifier locus", "CFTR Dysfunction", "contributes_to") not in edges
    assert ("F508del", "CFTR", "variant_of") in edges

    data = json.loads(graph_to_json(graph, disorder))
    node_types = {node["id"]: node["node_type"] for node in data["nodes"]}
    assert node_types["Patient-derived airway organoid"] == "experimental_model"
    assert node_types["CFTR network model"] == "computational_model"
    assert node_types["Ivacaftor"] == "treatment"
    assert node_types["CFTR"] == "genetic"
    assert node_types["F508del"] == "genetic"


def test_build_causal_graph_includes_biomarker_readout_links() -> None:
    """Biochemical marker readouts should add observational pathograph edges."""
    disorder = {
        "name": "Example Disease",
        "pathophysiology": [
            {
                "name": "Membrane Injury",
                "downstream": [{"target": "Muscle Weakness"}],
            }
        ],
        "phenotypes": [{"name": "Muscle Weakness"}],
        "biochemical": [
            {
                "name": "Creatine Kinase",
                "presence": "Elevated",
                "biomarker_term": {
                    "preferred_term": "creatine kinase measurement",
                    "term": {
                        "id": "NCIT:C64489",
                        "label": "Creatine Kinase Measurement",
                    },
                },
                "readouts": [
                    {
                        "target": "Membrane Injury",
                        "relationship": "READOUT_OF",
                        "direction": "POSITIVE",
                        "endpoint_context": "MONITORING",
                        "regulatory_endpoint_refs": ["FDA-SE-test-001"],
                        "interpretation": "Higher CK reflects greater membrane injury.",
                    }
                ],
            }
        ],
    }

    graph = build_causal_graph(disorder)
    edges = {(edge.source, edge.target, edge.predicate) for edge in graph.edges}

    assert ("Membrane Injury", "Creatine Kinase", "readout") in edges

    data = json.loads(graph_to_json(graph, disorder))
    edge = next(
        edge
        for edge in data["edges"]
        if edge["source"] == "Membrane Injury" and edge["target"] == "Creatine Kinase"
    )
    assert edge["predicate"] == "readout"
    assert edge["relationship"] == "READOUT_OF"
    assert edge["direction"] == "POSITIVE"
    assert edge["endpoint_context"] == "MONITORING"

    node = next(node for node in data["nodes"] if node["id"] == "Creatine Kinase")
    assert node["node_type"] == "biochemical"
    assert node["meta"]["presence"] == "Elevated"
    assert node["meta"]["readouts"] == [
        {
            "target": "Membrane Injury",
            "relationship": "READOUT_OF",
            "direction": "POSITIVE",
            "endpoint_context": "MONITORING",
            "regulatory_endpoint_refs": ["FDA-SE-test-001"],
            "interpretation": "Higher CK reflects greater membrane injury.",
        }
    ]


def test_build_causal_graph_includes_phenotype_readout_links() -> None:
    """Investigation-readout phenotypes should link to the mechanism they report on.

    An abnormal-test phenotype (e.g. an abnormal electroretinogram) that carries
    ``reports_on`` should add an observational (dashed) edge from the target
    mechanism to the phenotype, rather than floating as a disconnected node — and
    without asserting a causal ``downstream`` relationship.
    """
    disorder = {
        "name": "Example Retinopathy",
        "pathophysiology": [{"name": "Photoreceptor Degeneration"}],
        "phenotypes": [
            {
                "name": "Abnormal electroretinogram",
                "phenotype_term": {
                    "preferred_term": "Abnormal electroretinogram",
                    "term": {"id": "HP:0000512", "label": "Abnormal electroretinogram"},
                },
                "reports_on": [
                    {
                        "target": "Photoreceptor Degeneration",
                        "relationship": "READOUT_OF",
                        "direction": "NEGATIVE",
                        "endpoint_context": "DIAGNOSTIC",
                        "interpretation": "Reduced ERG responses track photoreceptor loss.",
                    }
                ],
            }
        ],
    }

    graph = build_causal_graph(disorder)
    edges = {(edge.source, edge.target, edge.predicate) for edge in graph.edges}

    # Observational readout edge: mechanism -.-> readout phenotype.
    assert (
        "Photoreceptor Degeneration",
        "Abnormal electroretinogram",
        "readout",
    ) in edges
    # The phenotype is not an orphan and carries no causal downstream edge.
    assert "Abnormal electroretinogram" not in graph.orphan_targets

    data = json.loads(graph_to_json(graph, disorder))
    edge = next(
        edge
        for edge in data["edges"]
        if edge["source"] == "Photoreceptor Degeneration"
        and edge["target"] == "Abnormal electroretinogram"
    )
    assert edge["predicate"] == "readout"
    assert edge["relationship"] == "READOUT_OF"
    assert edge["direction"] == "NEGATIVE"
    assert edge["endpoint_context"] == "DIAGNOSTIC"

    node = next(
        node for node in data["nodes"] if node["id"] == "Abnormal electroretinogram"
    )
    assert node["node_type"] == "phenotype"
    assert node["meta"]["reports_on"] == [
        {
            "target": "Photoreceptor Degeneration",
            "relationship": "READOUT_OF",
            "direction": "NEGATIVE",
            "endpoint_context": "DIAGNOSTIC",
            "interpretation": "Reduced ERG responses track photoreceptor loss.",
        }
    ]


def test_graph_to_json_includes_hypothesis_group_edge_metadata() -> None:
    """Pathograph edges should preserve curated hypothesis group links."""
    disorder = {
        "name": "Example Disease",
        "pathophysiology": [
            {
                "name": "Upstream mechanism",
                "downstream": [
                    {
                        "target": "Downstream mechanism",
                        "description": "Mechanistic bridge.",
                        "hypothesis_groups": ["canonical_model"],
                        "causal_link_type": "INDIRECT_KNOWN_INTERMEDIATES",
                        "intermediate_mechanisms": ["Intermediate step"],
                    }
                ],
            },
            {"name": "Downstream mechanism"},
        ],
    }

    graph = build_causal_graph(disorder)
    data = json.loads(graph_to_json(graph, disorder))
    edge = next(
        edge
        for edge in data["edges"]
        if edge["source"] == "Upstream mechanism"
        and edge["target"] == "Downstream mechanism"
    )

    assert edge["description"] == "Mechanistic bridge."
    assert edge["hypothesis_groups"] == ["canonical_model"]
    assert edge["causal_link_type"] == "INDIRECT_KNOWN_INTERMEDIATES"
    assert edge["intermediate_mechanisms"] == ["Intermediate step"]


def test_graph_to_json_includes_matching_histopathology_terms() -> None:
    """Matching pathograph nodes should expose NCIT-backed histopathology metadata."""
    disorder = {
        "name": "Example Disease",
        "pathophysiology": [
            {
                "name": "Desmoplastic Stroma",
                "downstream": [{"target": "CAF-Mediated T Cell Exclusion"}],
            }
        ],
        "phenotypes": [{"name": "CAF-Mediated T Cell Exclusion"}],
        "histopathology": [
            {
                "name": "Desmoplastic Stroma",
                "finding_term": {
                    "preferred_term": "Desmoplastic Stroma",
                    "term": {
                        "id": "NCIT:C36178",
                        "label": "Fibrotic Stroma Formation",
                    },
                },
            }
        ],
    }

    graph = build_causal_graph(disorder)
    data = json.loads(graph_to_json(graph, disorder))
    node = next(node for node in data["nodes"] if node["id"] == "Desmoplastic Stroma")

    assert node["meta"]["histopathology_terms"] == [
        {
            "name": "Desmoplastic Stroma",
            "preferred_term": "Desmoplastic Stroma",
            "term_id": "NCIT:C36178",
            "term_label": "Fibrotic Stroma Formation",
        }
    ]


def test_build_causal_graph_includes_environmental_mechanism_links() -> None:
    """Environmental factors linked via influences_mechanisms should enter the pathograph."""
    disorder = {
        "name": "Example Disease",
        "pathophysiology": [
            {"name": "Airway Inflammation"},
            {"name": "Allergic Sensitization"},
        ],
        "environmental": [
            {
                "name": "Tobacco smoke exposure",
                "influences_mechanisms": [
                    {
                        "target": "Airway Inflammation",
                        "environmental_effect": "EXACERBATES",
                        "causal_link_type": "DIRECT",
                        "description": "Smoke amplifies ongoing airway inflammation.",
                    }
                ],
            },
            {
                "name": "Early-life farm microbial exposure",
                "influences_mechanisms": [
                    {
                        "target": "Allergic Sensitization",
                        "environmental_effect": "PROTECTS_AGAINST",
                    }
                ],
            },
            {
                "name": "Unlinked contextual exposure",
            },
            {
                "name": "Undirected exposure",
                "influences_mechanisms": [{"target": "Airway Inflammation"}],
            },
        ],
    }

    graph = build_causal_graph(disorder)
    edges = {(edge.source, edge.target, edge.predicate) for edge in graph.edges}

    assert ("Tobacco smoke exposure", "Airway Inflammation", "exacerbates") in edges
    assert (
        "Early-life farm microbial exposure",
        "Allergic Sensitization",
        "protects_against",
    ) in edges
    # An unqualified link must not be asserted as causative.
    assert ("Undirected exposure", "Airway Inflammation", "influences") in edges
    assert not graph.integrity_issues

    data = json.loads(graph_to_json(graph, disorder))
    node_types = {node["id"]: node["node_type"] for node in data["nodes"]}
    assert node_types["Tobacco smoke exposure"] == "environmental"
    assert node_types["Early-life farm microbial exposure"] == "environmental"
    # Environmental entries with no mechanism link stay out of the pathograph.
    assert "Unlinked contextual exposure" not in node_types

    smoke_edge = next(
        edge for edge in data["edges"] if edge["source"] == "Tobacco smoke exposure"
    )
    assert smoke_edge["causal_link_type"] == "DIRECT"
    assert smoke_edge["description"] == "Smoke amplifies ongoing airway inflammation."
