"""Regression tests for rendered pathograph payloads."""

import json
import re
from collections import defaultdict, deque
from pathlib import Path

import pytest

from dismech.render import render_disorder


def _extract_graph_data(html: str) -> dict:
    """Extract the embedded graphData payload from a rendered disorder page."""
    match = re.search(r"var graphData = JSON\.parse\((\".*?\")\);", html, re.S)
    assert match is not None, "Rendered HTML did not include graphData payload"
    return json.loads(json.loads(match.group(1)))


def _connected_component_count(graph_data: dict) -> int:
    """Return the number of connected components in an undirected view of the graph."""
    adjacency: dict[str, set[str]] = defaultdict(set)
    nodes = {node["id"] for node in graph_data.get("nodes", [])}

    for edge in graph_data.get("edges", []):
        source = edge["source"]
        target = edge["target"]
        adjacency[source].add(target)
        adjacency[target].add(source)
        nodes.add(source)
        nodes.add(target)

    remaining = set(nodes)
    components = 0
    while remaining:
        components += 1
        start = remaining.pop()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in adjacency[node]:
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    queue.append(neighbor)
    return components


def test_rendered_crohn_pathograph_payload_is_connected(tmp_path: Path) -> None:
    """Crohn's rendered graph payload should remain a single connected graph."""
    repo_root = Path(__file__).resolve().parents[1]
    disorder_path = repo_root / "kb" / "disorders" / "Crohn_Disease.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Crohn_Disease.html"

    render_disorder(disorder_path, output_path=output_path)
    graph_data = _extract_graph_data(output_path.read_text())
    edges = {(edge["source"], edge["target"]) for edge in graph_data["edges"]}

    assert (
        "Dysregulated Immune Response",
        "Intestinal Inflammation and Epithelial Injury",
    ) in edges
    assert (
        "Antimicrobial Defense Deficiency",
        "Intestinal Barrier Dysfunction",
    ) in edges
    assert (
        "Intestinal Barrier Dysfunction",
        "Dysregulated Immune Response",
    ) in edges
    assert (
        "Intestinal Inflammation and Epithelial Injury",
        "Diarrhea",
    ) in edges
    assert (
        "TL1A-Mediated T Cell Activation",
        "Dysregulated Immune Response",
    ) in edges
    assert (
        "Dysregulated Immune Response",
        "Diarrhea",
    ) not in edges
    assert _connected_component_count(graph_data) == 1


def test_rendered_crohn_pathograph_payload_includes_experimental_model_nodes(
    tmp_path: Path,
) -> None:
    """Crohn's page should include explicit experimental model nodes and links."""
    repo_root = Path(__file__).resolve().parents[1]
    disorder_path = repo_root / "kb" / "disorders" / "Crohn_Disease.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Crohn_Disease.html"

    render_disorder(disorder_path, output_path=output_path)
    graph_data = _extract_graph_data(output_path.read_text())

    node_types = {node["id"]: node["node_type"] for node in graph_data["nodes"]}
    edges = {(edge["source"], edge["target"]) for edge in graph_data["edges"]}

    assert (
        "Primary human small-intestinal monolayer barrier model",
        "Intestinal Barrier Dysfunction",
    ) in edges
    assert (
        "PSC-derived intestinal organoid-macrophage coculture model",
        "Dysregulated Immune Response",
    ) in edges
    assert (
        node_types["Primary human small-intestinal monolayer barrier model"]
        == "experimental_model"
    )


def test_rendered_stargardt_pathograph_payload_includes_treatments_and_genetics(
    tmp_path: Path,
) -> None:
    """Stargardt's page should surface linked treatment and genetics content."""
    repo_root = Path(__file__).resolve().parents[1]
    disorder_path = repo_root / "kb" / "disorders" / "Stargardt_Disease.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Stargardt_Disease.html"

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()
    graph_data = _extract_graph_data(html)
    node_types = {node["id"]: node["node_type"] for node in graph_data["nodes"]}
    edges = {(edge["source"], edge["target"]) for edge in graph_data["edges"]}

    assert ("ABCA4", "ABCA4 transporter dysfunction") in edges
    assert ("Gene therapy (investigational)", "ABCA4 transporter dysfunction") in edges
    assert ("Low vision rehabilitation", "Reduced visual acuity") in edges
    assert node_types["ABCA4"] == "genetic"
    assert node_types["Gene therapy (investigational)"] == "treatment"
    assert 'href="#pathograph"' in html
    assert html.count('id="pathograph"') == 1
    assert ">Pathograph</div>" in html
    assert f">Pathograph {len(graph_data['nodes'])}</a>" in html


def test_rendered_pdac_pathograph_payload_includes_histopathology_metadata(
    tmp_path: Path,
) -> None:
    """PDAC pathograph should surface histopathology and computational model links."""
    repo_root = Path(__file__).resolve().parents[1]
    disorder_path = (
        repo_root / "kb" / "disorders" / "Pancreatic_Ductal_Adenocarcinoma.yaml"
    )
    output_path = (
        tmp_path / "pages" / "disorders" / "Pancreatic_Ductal_Adenocarcinoma.html"
    )

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()
    graph_data = _extract_graph_data(html)
    node_meta = {node["id"]: node.get("meta", {}) for node in graph_data["nodes"]}
    node_types = {node["id"]: node["node_type"] for node in graph_data["nodes"]}
    edges = {(edge["source"], edge["target"]) for edge in graph_data["edges"]}

    assert "Histopath:" in html
    assert "Computational models" in html
    assert (
        "PDAC CAF-Mediated Invasion PhysiCell Model",
        "Desmoplastic Stroma",
    ) in edges
    assert (
        "PDAC Immunotherapy PhysiCell Model",
        "Immune Evasion",
    ) in edges
    assert (
        node_types["PDAC CAF-Mediated Invasion PhysiCell Model"]
        == "computational_model"
    )
    assert node_meta["Desmoplastic Stroma"]["histopathology_terms"] == [
        {
            "name": "Desmoplastic Stroma",
            "preferred_term": "desmoplastic stroma",
            "term_id": "NCIT:C36178",
            "term_label": "Fibrotic Stroma Formation",
        }
    ]
    assert node_meta["Desmoplastic Stroma"]["computational_models"] == [
        {
            "name": "PDAC CAF-Mediated Invasion PhysiCell Model",
            "model_type": "AGENT_BASED",
            "model_software": "PhysiCell",
            "model_format": "C++/XML/CSV",
            "description": "Implements ECM-driven fibroblast motility and epithelial-mesenchymal state switching encoded in `config/cell_rules.csv` for the stromal invasion program.",
        }
    ]


def test_rendered_mediator_complex_pathograph_payload_is_hierarchical_and_subtyped(
    tmp_path: Path,
) -> None:
    """Mediatoropathy graph should preserve branch hierarchy and subtype metadata."""
    repo_root = Path(__file__).resolve().parents[1]
    disorder_path = (
        repo_root
        / "kb"
        / "disorders"
        / "Mediator_Complex_Neurodevelopmental_Disorder.yaml"
    )
    output_path = (
        tmp_path
        / "pages"
        / "disorders"
        / "Mediator_Complex_Neurodevelopmental_Disorder.html"
    )

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()
    graph_data = _extract_graph_data(html)
    edges = {(edge["source"], edge["target"]) for edge in graph_data["edges"]}
    node_meta = {node["id"]: node.get("meta", {}) for node in graph_data["nodes"]}

    assert ("Mediator Complex Disruption", "CDK8 Kinase Module Dysfunction") in edges
    assert (
        "Mediator Complex Disruption",
        "Tail Module Disruption and Immediate Early Gene Dysregulation",
    ) in edges
    assert (
        "CDK8 Kinase Module Dysfunction",
        "Neurodevelopmental Transcriptional Dysregulation",
    ) in edges
    assert ("CDK8 Kinase Module Dysfunction", "Cardiac Developmental Defects") in edges
    assert (
        "Tail Module Disruption and Immediate Early Gene Dysregulation",
        "Neurodevelopmental Transcriptional Dysregulation",
    ) in edges
    assert (
        "Neurodevelopmental Transcriptional Dysregulation",
        "Cortical Neuron Migration and Projection Defects",
    ) in edges

    assert (
        "Mediator Complex Disruption",
        "Neurodevelopmental Transcriptional Dysregulation",
    ) not in edges
    assert ("Mediator Complex Disruption", "Cardiac Developmental Defects") not in edges

    assert node_meta["CDK8 Kinase Module Dysfunction"]["subtypes"] == [
        "MED13",
        "MED13L",
        "MED12",
    ]
    assert node_meta["Tail Module Disruption and Immediate Early Gene Dysregulation"][
        "subtypes"
    ] == ["MED23"]
    assert node_meta["Cortical Neuron Migration and Projection Defects"][
        "subtypes"
    ] == ["MED13"]
    assert node_meta["Cardiac Developmental Defects"]["subtypes"] == [
        "MED13",
        "MED13L",
        "MED12",
    ]
    assert "Subtypes:" in html


@pytest.mark.parametrize(
    ("filename", "expected_edges", "expected_nodes", "expected_functions"),
    [
        (
            "Wilsons_Disease.yaml",
            {
                ("ATP7B", "Impaired Biliary Copper Excretion"),
                ("ATP7B", "Impaired Ceruloplasmin Loading"),
            },
            {"ATP7B": "genetic"},
            {
                "Impaired Biliary Copper Excretion": [
                    "P-type monovalent copper transporter activity"
                ],
                "Impaired Ceruloplasmin Loading": [
                    "P-type monovalent copper transporter activity"
                ],
            },
        ),
        (
            "Danon_disease.yaml",
            {("LAMP2 mutations", "LAMP2 protein deficiency")},
            {"LAMP2 mutations": "genetic"},
            {"LAMP2 protein deficiency": ["protein-macromolecule adaptor activity"]},
        ),
        (
            "CACNA1A_Related_Disorder.yaml",
            {("CACNA1A", "P/Q-type Calcium Channel Dysfunction")},
            {"CACNA1A": "genetic"},
            {
                "P/Q-type Calcium Channel Dysfunction": [
                    "P/Q-type calcium channel activity"
                ]
            },
        ),
        (
            "Niemann_Pick_Disease_Type_C.yaml",
            {
                ("NPC1", "NPC1/NPC2-Mediated Cholesterol Egress Failure"),
                ("NPC2", "NPC1/NPC2-Mediated Cholesterol Egress Failure"),
            },
            {"NPC1": "genetic", "NPC2": "genetic"},
            {
                "NPC1/NPC2-Mediated Cholesterol Egress Failure": [
                    "cholesterol transfer activity"
                ]
            },
        ),
        (
            "Gaucher_Disease.yaml",
            {("GBA1", "Glucocerebrosidase Deficiency")},
            {"GBA1": "genetic"},
            {"Glucocerebrosidase Deficiency": ["glucocerebrosidase activity"]},
        ),
        (
            "Lesch-Nyhan_Syndrome.yaml",
            {("HPRT1 mutations", "HPRT1 Enzyme Deficiency and Purine Overproduction")},
            {"HPRT1 mutations": "genetic"},
            {
                "HPRT1 Enzyme Deficiency and Purine Overproduction": [
                    "hypoxanthine phosphoribosyltransferase activity",
                    "guanine phosphoribosyltransferase activity",
                ]
            },
        ),
        (
            "Diastrophic_Dysplasia.yaml",
            {
                (
                    "SLC26A2 Pathogenic Variants",
                    "Sulfate Transport Defect in Cartilage",
                )
            },
            {"SLC26A2 Pathogenic Variants": "genetic"},
            {
                "Sulfate Transport Defect in Cartilage": [
                    "sulfate transmembrane transporter activity"
                ]
            },
        ),
        (
            "BEST1_Bestrophinopathies.yaml",
            {("BEST1", "BEST1 Channel Dysfunction")},
            {"BEST1": "genetic"},
            {
                "BEST1 Channel Dysfunction": [
                    "calcium-activated chloride channel activity"
                ]
            },
        ),
        (
            "Acromesomelic_Dysplasia_Maroteaux_Type.yaml",
            {
                (
                    "NPR2 Loss-of-Function Mutations",
                    "Impaired CNP-NPR-B-cGMP Signaling in Growth Plate",
                )
            },
            {"NPR2 Loss-of-Function Mutations": "genetic"},
            {
                "Impaired CNP-NPR-B-cGMP Signaling in Growth Plate": [
                    "receptor guanylyl cyclase activity",
                    "natriuretic peptide receptor activity",
                ]
            },
        ),
        (
            "CLOVES_Syndrome.yaml",
            {("PIK3CA Somatic Mutations", "Constitutive PI3K Activation")},
            {"PIK3CA Somatic Mutations": "genetic"},
            {
                "Constitutive PI3K Activation": [
                    "phosphatidylinositol 3-kinase activity"
                ]
            },
        ),
        (
            "Fibrochondrogenesis.yaml",
            {
                (
                    "COL11A1 Mutations (Fibrochondrogenesis Type 1)",
                    "COL11A1/COL11A2 Loss-of-Function",
                ),
                (
                    "COL11A2 Mutations (Fibrochondrogenesis Type 2)",
                    "COL11A1/COL11A2 Loss-of-Function",
                ),
            },
            {
                "COL11A1 Mutations (Fibrochondrogenesis Type 1)": "genetic",
                "COL11A2 Mutations (Fibrochondrogenesis Type 2)": "genetic",
            },
            {
                "COL11A1/COL11A2 Loss-of-Function": [
                    "extracellular matrix structural constituent"
                ]
            },
        ),
        (
            "Atelosteogenesis_Type_II.yaml",
            {
                (
                    "SLC26A2 Pathogenic Variants",
                    "Sulfate Transport Deficiency in Chondrocytes",
                )
            },
            {"SLC26A2 Pathogenic Variants": "genetic"},
            {
                "Sulfate Transport Deficiency in Chondrocytes": [
                    "sulfate transmembrane transporter activity"
                ]
            },
        ),
        (
            "Carvajal_Syndrome.yaml",
            {
                (
                    "DSP Biallelic Loss-of-Function Variants",
                    "Biallelic DSP Deficiency — Desmosome-IF Uncoupling",
                )
            },
            {"DSP Biallelic Loss-of-Function Variants": "genetic"},
            {
                "Biallelic DSP Deficiency — Desmosome-IF Uncoupling": [
                    "structural constituent of cytoskeleton"
                ]
            },
        ),
        (
            "Pelizaeus_Merzbacher_Disease.yaml",
            {
                ("PLP1", "PLP1 Missense Mutation Causing Protein Misfolding"),
                ("PLP1", "PLP1 Gene Duplication Causing Overexpression"),
            },
            {"PLP1": "genetic"},
            {
                "PLP1 Missense Mutation Causing Protein Misfolding": [
                    "structural constituent of myelin sheath"
                ],
                "PLP1 Gene Duplication Causing Overexpression": [
                    "structural constituent of myelin sheath"
                ],
            },
        ),
        (
            "Campomelic_Dysplasia.yaml",
            {
                ("SOX9 Pathogenic Variants", "SOX9-Mediated Chondrogenesis Disruption"),
                ("SOX9 Pathogenic Variants", "Disrupted 46,XY Sex Determination"),
            },
            {"SOX9 Pathogenic Variants": "genetic"},
            {
                "SOX9-Mediated Chondrogenesis Disruption": [
                    "DNA-binding transcription factor activity, RNA polymerase II-specific"
                ],
                "Disrupted 46,XY Sex Determination": [
                    "DNA-binding transcription factor activity, RNA polymerase II-specific"
                ],
            },
        ),
        (
            "Cleidocranial_Dysplasia.yaml",
            {
                (
                    "RUNX2 Pathogenic Variants",
                    "RUNX2 Haploinsufficiency and Osteoblast Differentiation Failure",
                )
            },
            {"RUNX2 Pathogenic Variants": "genetic"},
            {
                "RUNX2 Haploinsufficiency and Osteoblast Differentiation Failure": [
                    "DNA-binding transcription factor activity, RNA polymerase II-specific"
                ]
            },
        ),
        (
            "Achondrogenesis_Type_II.yaml",
            {("COL2A1 Mutations", "Type II Collagen Structural Defect")},
            {"COL2A1 Mutations": "genetic"},
            {
                "Type II Collagen Structural Defect": [
                    "extracellular matrix structural constituent"
                ]
            },
        ),
        (
            "Alexander_Disease.yaml",
            {
                (
                    "GFAP Gain-of-Function Mutations",
                    "GFAP Aggregation and Rosenthal Fiber Formation",
                ),
                (
                    "GFAP Gain-of-Function Mutations",
                    "GFAP Post-Translational Modifications and Aggregation",
                ),
            },
            {"GFAP Gain-of-Function Mutations": "genetic"},
            {
                "GFAP Aggregation and Rosenthal Fiber Formation": [
                    "structural constituent of cytoskeleton"
                ],
                "GFAP Post-Translational Modifications and Aggregation": [
                    "structural constituent of cytoskeleton"
                ],
            },
        ),
        (
            "Ataxia_Telangiectasia.yaml",
            {("ATM", "ATM kinase deficiency and defective DNA damage signaling")},
            {"ATM": "genetic"},
            {
                "ATM kinase deficiency and defective DNA damage signaling": [
                    "protein serine/threonine kinase activity"
                ]
            },
        ),
        (
            "DSP_Cardiomyopathy.yaml",
            {
                (
                    "DSP Heterozygous Truncating Variants",
                    "Desmoplakin Haploinsufficiency — Desmosomal Disruption",
                )
            },
            {"DSP Heterozygous Truncating Variants": "genetic"},
            {
                "Desmoplakin Haploinsufficiency — Desmosomal Disruption": [
                    "structural constituent of cytoskeleton"
                ]
            },
        ),
        (
            "Atelosteogenesis_Type_I.yaml",
            {
                (
                    "FLNB Pathogenic Variants",
                    "FLNB Gain-of-Function Cytoskeletal Dysregulation",
                )
            },
            {"FLNB Pathogenic Variants": "genetic"},
            {
                "FLNB Gain-of-Function Cytoskeletal Dysregulation": [
                    "actin filament binding"
                ]
            },
        ),
        (
            "Atelosteogenesis_Type_III.yaml",
            {("FLNB Pathogenic Variants", "FLNB Cytoskeletal Signaling Dysfunction")},
            {"FLNB Pathogenic Variants": "genetic"},
            {"FLNB Cytoskeletal Signaling Dysfunction": ["actin filament binding"]},
        ),
        (
            "FLNA_Intestinal_Pseudoobstruction.yaml",
            {
                (
                    "FLNA Loss-of-Function Variants",
                    "FLNA Deficiency and Enteric Neuron Development Failure",
                )
            },
            {"FLNA Loss-of-Function Variants": "genetic"},
            {
                "FLNA Deficiency and Enteric Neuron Development Failure": [
                    "actin filament binding"
                ]
            },
        ),
        (
            "FOXE3_Anterior_Segment_Dysgenesis.yaml",
            {("FOXE3", "Failed Lens Placode Induction and Differentiation")},
            {"FOXE3": "genetic"},
            {
                "Failed Lens Placode Induction and Differentiation": [
                    "DNA-binding transcription factor activity, RNA polymerase II-specific"
                ]
            },
        ),
        (
            "PKP2_Cardiomyopathy.yaml",
            {("PKP2 Loss-of-Function Variants", "Desmosomal Disruption")},
            {"PKP2 Loss-of-Function Variants": "genetic"},
            {"Desmosomal Disruption": ["cadherin binding"]},
        ),
        (
            "PRPS1_Deficiency_Spectrum.yaml",
            {("PRPS1 Loss-of-Function Variants", "PRS-I loss of function")},
            {"PRPS1 Loss-of-Function Variants": "genetic"},
            {"PRS-I loss of function": ["ribose phosphate diphosphokinase activity"]},
        ),
        (
            "PRPS1_Superactivity.yaml",
            {
                (
                    "PRPS1 gain-of-function and overexpression mechanisms",
                    "PRS-I allosteric gain of function",
                )
            },
            {"PRPS1 gain-of-function and overexpression mechanisms": "genetic"},
            {
                "PRS-I allosteric gain of function": [
                    "ribose phosphate diphosphokinase activity"
                ]
            },
        ),
        (
            "Periventricular_Nodular_Heterotopia.yaml",
            {
                (
                    "FLNA Loss-of-Function Variants",
                    "FLNA Loss of Function and Neuronal Migration Failure",
                )
            },
            {"FLNA Loss-of-Function Variants": "genetic"},
            {
                "FLNA Loss of Function and Neuronal Migration Failure": [
                    "actin filament binding"
                ]
            },
        ),
        (
            "Metaphyseal_Chondrodysplasia_Schmid_Type.yaml",
            {("COL10A1 Pathogenic Variants", "Collagen X Misfolding and ER Stress")},
            {"COL10A1 Pathogenic Variants": "genetic"},
            {
                "Collagen X Misfolding and ER Stress": [
                    "extracellular matrix structural constituent conferring tensile strength"
                ]
            },
        ),
        (
            "RYR2_CPVT.yaml",
            {("RYR2 gain-of-function variants", "RYR2 Gain-of-Function Calcium Leak")},
            {"RYR2 gain-of-function variants": "genetic"},
            {
                "RYR2 Gain-of-Function Calcium Leak": [
                    "ryanodine-sensitive calcium-release channel activity"
                ]
            },
        ),
        (
            "MYO6_Hearing_Loss.yaml",
            {
                (
                    "MYO6 pathogenic variants",
                    "Stereocilia Dysfunction in Cochlear Hair Cells",
                )
            },
            {"MYO6 pathogenic variants": "genetic"},
            {
                "Stereocilia Dysfunction in Cochlear Hair Cells": [
                    "microfilament motor activity"
                ]
            },
        ),
        (
            "Kosaki_Overgrowth_Syndrome.yaml",
            {("PDGFRB Gain-of-Function Mutations", "Constitutive PDGFRB Activation")},
            {"PDGFRB Gain-of-Function Mutations": "genetic"},
            {
                "Constitutive PDGFRB Activation": [
                    "platelet-derived growth factor beta-receptor activity"
                ]
            },
        ),
        (
            "Infantile_Myofibromatosis.yaml",
            {("PDGFRB Gain-of-Function Mutations", "Constitutive PDGFRB Signaling")},
            {"PDGFRB Gain-of-Function Mutations": "genetic"},
            {
                "Constitutive PDGFRB Signaling": [
                    "platelet-derived growth factor beta-receptor activity"
                ]
            },
        ),
        (
            "Penttinen_Premature_Aging_Syndrome.yaml",
            {("PDGFRB Gain-of-Function Mutations", "Constitutive PDGFRB Activation")},
            {"PDGFRB Gain-of-Function Mutations": "genetic"},
            {
                "Constitutive PDGFRB Activation": [
                    "platelet-derived growth factor beta-receptor activity"
                ]
            },
        ),
        (
            "Metatropic_Dysplasia.yaml",
            {
                (
                    "TRPV4 Pathogenic Variants",
                    "TRPV4 Channel Hyperactivity in Growth Plate Chondrocytes",
                )
            },
            {"TRPV4 Pathogenic Variants": "genetic"},
            {
                "TRPV4 Channel Hyperactivity in Growth Plate Chondrocytes": [
                    "calcium channel activity"
                ]
            },
        ),
        (
            "Otopalatodigital_Spectrum_Disorders.yaml",
            {
                (
                    "FLNA Gain-of-Function Missense Variants",
                    "FLNA Gain-of-Function and Cytoskeletal Signaling Dysregulation",
                )
            },
            {"FLNA Gain-of-Function Missense Variants": "genetic"},
            {
                "FLNA Gain-of-Function and Cytoskeletal Signaling Dysregulation": [
                    "actin filament binding"
                ]
            },
        ),
        (
            "Larsen_Syndrome.yaml",
            {
                (
                    "FLNB Pathogenic Variants",
                    "Gain-of-Function Actin-Binding Dysregulation",
                )
            },
            {"FLNB Pathogenic Variants": "genetic"},
            {
                "Gain-of-Function Actin-Binding Dysregulation": [
                    "actin filament binding"
                ]
            },
        ),
        (
            "Spondyloepimetaphyseal_Dysplasia_Strudwick_Type.yaml",
            {("COL2A1", "Collagen Triple Helix Disruption")},
            {"COL2A1": "genetic"},
            {
                "Collagen Triple Helix Disruption": [
                    "extracellular matrix structural constituent"
                ]
            },
        ),
        (
            "Spondyloepiphyseal_Dysplasia_Congenita.yaml",
            {("COL2A1 Mutations", "Dominant-Negative Collagen Misfolding")},
            {"COL2A1 Mutations": "genetic"},
            {
                "Dominant-Negative Collagen Misfolding": [
                    "extracellular matrix structural constituent"
                ]
            },
        ),
        (
            "TP63_Ectodermal_Dysplasia_Spectrum.yaml",
            {
                (
                    "TP63 Heterozygous Mutations",
                    "TP63 Mutations and p63 Transcription Factor Dysfunction",
                )
            },
            {"TP63 Heterozygous Mutations": "genetic"},
            {
                "TP63 Mutations and p63 Transcription Factor Dysfunction": [
                    "DNA-binding transcription factor activity, RNA polymerase II-specific"
                ]
            },
        ),
    ],
)
def test_rendered_pathograph_payload_includes_expected_rare_disease_gene_edges(
    tmp_path: Path,
    filename: str,
    expected_edges: set[tuple[str, str]],
    expected_nodes: dict[str, str],
    expected_functions: dict[str, list[str]],
) -> None:
    """Selected rare-disease pathographs should surface inferred HGNC gene links."""
    repo_root = Path(__file__).resolve().parents[1]
    disorder_path = repo_root / "kb" / "disorders" / filename
    output_path = tmp_path / "pages" / "disorders" / filename.replace(".yaml", ".html")

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()
    graph_data = _extract_graph_data(html)
    node_types = {node["id"]: node["node_type"] for node in graph_data["nodes"]}
    node_meta = {node["id"]: node.get("meta", {}) for node in graph_data["nodes"]}
    edges = {(edge["source"], edge["target"]) for edge in graph_data["edges"]}

    for edge in expected_edges:
        assert edge in edges

    for node_name, node_type in expected_nodes.items():
        assert node_types[node_name] == node_type

    for node_name, molecular_functions in expected_functions.items():
        assert node_meta[node_name]["molecular_functions"] == molecular_functions

    assert "Functions:" in html
