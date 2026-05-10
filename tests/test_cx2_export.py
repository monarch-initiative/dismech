"""Regression tests for disorder pathograph CX2 export."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

from dismech.export import cx2_export
from dismech.export.cx2_export import disorder_to_cx2, load_disorder


def _aspect_map(cx2: list[dict]) -> dict:
    aspects: dict = {}
    for aspect in cx2:
        aspects.update(aspect)
    return aspects


def _nodes_by_name(aspects: dict) -> tuple[dict[str, dict], dict[int, str]]:
    node_map = {node["v"]["name"]: node for node in aspects["nodes"]}
    id_to_name = {node["id"]: node["v"]["name"] for node in aspects["nodes"]}
    return node_map, id_to_name


def _edges_by_endpoints(aspects: dict) -> dict[tuple[str, str], dict]:
    _, id_to_name = _nodes_by_name(aspects)
    return {
        (id_to_name[edge["s"]], id_to_name[edge["t"]]): edge
        for edge in aspects["edges"]
    }


def _write_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def test_disorder_to_cx2_exports_stargardt_with_layout_and_metadata() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    disorder_path = repo_root / "kb" / "disorders" / "Stargardt_Disease.yaml"

    cx2 = disorder_to_cx2(
        load_disorder(disorder_path),
        source_path=disorder_path,
    )
    aspects = _aspect_map(cx2)
    nodes, _ = _nodes_by_name(aspects)
    edges = _edges_by_endpoints(aspects)

    assert isinstance(cx2, list)
    assert "visualProperties" in aspects
    assert "visualEditorProperties" in aspects

    network_attributes = aspects["networkAttributes"][0]
    assert network_attributes["name"] == "Stargardt Disease"
    assert "Stargardt disease" in network_attributes["disease"]
    assert network_attributes["disease_term_id"] == "MONDO:0019353"
    assert network_attributes["node_count"] == len(aspects["nodes"])
    assert network_attributes["edge_count"] == len(aspects["edges"])
    assert "PMID:" in network_attributes["reference"]
    assert network_attributes["source_file"].endswith(
        "kb/disorders/Stargardt_Disease.yaml"
    )
    assert "photoreceptor cell" in network_attributes["tissue"]
    assert "retinal pigment epithelial cell" in network_attributes["tissue"]
    assert (
        "github.com/monarch-initiative/dismech/blob/main/kb/disorders/Stargardt_Disease.yaml"
        in network_attributes["prov:wasDerivedFrom"]
    )

    abca4_node = nodes["ABCA4"]
    assert abca4_node["v"]["type"] == "gene"
    assert abca4_node["v"]["dismech_type"] == "genetic"
    assert abca4_node["v"]["represents"] == "hgnc:34"
    assert abca4_node["v"]["iquery_gene_symbols"] == ["ABCA4"]
    assert "member" not in abca4_node["v"]
    assert "x" in abca4_node and "y" in abca4_node

    mechanism_node = nodes["ABCA4 transporter dysfunction"]
    assert mechanism_node["v"]["type"] == "proteinfamily"
    assert mechanism_node["v"]["dismech_type"] == "pathophysiology"
    assert mechanism_node["v"]["genes"] == ["ABCA4"]
    assert mechanism_node["v"]["member"] == ["ABCA4"]
    assert mechanism_node["v"]["cell_type_ids"] == [
        "CL:0000210",
        "CL:0000573",
        "CL:0000604",
    ]
    assert mechanism_node["v"]["biological_process_ids"] == ["GO:0006869"]
    assert "CL:0000210" in mechanism_node["v"]["cell_type_links"]
    assert "GO:0006869" in mechanism_node["v"]["biological_process_links"]
    assert mechanism_node["v"]["biological_processes"] == ["lipid transport"]

    treatment_edge = edges[
        ("Gene therapy (investigational)", "ABCA4 transporter dysfunction")
    ]
    assert treatment_edge["v"]["predicate"] == "targets"
    assert treatment_edge["v"]["treatment_effect"] == "RESTORES"
    assert treatment_edge["v"]["line_color"] == "#16a34a"
    assert "PMID:39201545" in treatment_edge["v"]["Evidence"]

    genetic_edge = edges[("ABCA4", "ABCA4 transporter dysfunction")]
    assert genetic_edge["v"]["predicate"] == "contributes_to"
    assert genetic_edge["v"]["inferred"] is True
    assert genetic_edge["v"]["inference_basis"] == "shared_gene_identifier"


def test_disorder_to_cx2_skips_modifier_gene_mechanism_edges() -> None:
    disorder = {
        "name": "Example Disease",
        "pathophysiology": [
            {
                "name": "CFTR dysfunction",
                "genes": [
                    {
                        "preferred_term": "CFTR",
                        "term": {"id": "hgnc:1884", "label": "CFTR"},
                    }
                ],
                "downstream": [{"target": "Bronchiectasis"}],
            }
        ],
        "phenotypes": [{"name": "Bronchiectasis"}],
        "genetic": [
            {
                "name": "CFTR",
                "association": "Causative",
                "gene_term": {
                    "preferred_term": "CFTR",
                    "term": {"id": "hgnc:1884", "label": "CFTR"},
                },
            },
            {
                "name": "CFTR modifier locus",
                "relationship_type": "MODIFIER",
                "gene_term": {
                    "preferred_term": "CFTR",
                    "term": {"id": "hgnc:1884", "label": "CFTR"},
                },
            },
        ],
    }

    cx2 = disorder_to_cx2(disorder)
    edges = _edges_by_endpoints(_aspect_map(cx2))

    assert ("CFTR", "CFTR dysfunction") in edges
    assert ("CFTR modifier locus", "CFTR dysfunction") not in edges


def test_disorder_to_cx2_exports_crohn_model_edges() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    disorder_path = repo_root / "kb" / "disorders" / "Crohn_Disease.yaml"

    cx2 = disorder_to_cx2(
        load_disorder(disorder_path),
        source_path=disorder_path,
    )
    aspects = _aspect_map(cx2)
    edges = _edges_by_endpoints(aspects)

    model_edge = edges[
        (
            "PSC-derived intestinal organoid-macrophage coculture model",
            "Dysregulated Immune Response",
        )
    ]
    assert model_edge["v"]["predicate"] == "models"
    assert model_edge["v"]["line_style"] == "dashed"
    assert "PMID:39701210" in model_edge["v"]["Evidence"]


def test_disorder_to_cx2_exports_event_location_links() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    disorder_path = repo_root / "kb" / "disorders" / "APL_PML_RARA.yaml"

    cx2 = disorder_to_cx2(
        load_disorder(disorder_path),
        source_path=disorder_path,
    )
    aspects = _aspect_map(cx2)
    nodes, _ = _nodes_by_name(aspects)

    event_node = nodes["Promyelocyte Accumulation"]
    assert event_node["v"]["location_ids"] == ["UBERON:0002371"]
    assert "UBERON:0002371" in event_node["v"]["location_links"]
    assert event_node["v"]["cell_type_ids"] == ["CL:0000836"]
    assert "CL:0000836" in event_node["v"]["cell_type_links"]


def test_disorder_to_cx2_uses_top_level_references_for_network_header() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    disorder_path = repo_root / "kb" / "disorders" / "Spinal_Muscular_Atrophy.yaml"

    cx2 = disorder_to_cx2(
        load_disorder(disorder_path),
        source_path=disorder_path,
    )
    aspects = _aspect_map(cx2)

    reference_html = aspects["networkAttributes"][0]["reference"]
    assert "DOI:10.1007/s00415-024-12724-3" in reference_html
    assert "Cytoskeleton dysfunction of motor neuron in spinal muscular atrophy" in (
        reference_html
    )


def test_cx2_export_cli_writes_json_file(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    disorder_path = repo_root / "kb" / "disorders" / "Stargardt_Disease.yaml"
    output_path = tmp_path / "stargardt.cx2.json"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "dismech.export.cx2_export",
            str(disorder_path),
            "-o",
            str(output_path),
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert output_path.exists()

    aspects = _aspect_map(json.loads(output_path.read_text()))
    assert aspects["networkAttributes"][0]["name"] == "Stargardt Disease"


def test_cx2_export_cli_can_skip_empty_pathograph(tmp_path: Path) -> None:
    disorder_path = tmp_path / "Empty_Disorder.yaml"
    output_path = tmp_path / "empty.cx2.json"
    _write_yaml(disorder_path, {"name": "Empty Disorder"})

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "dismech.export.cx2_export",
            str(disorder_path),
            "-o",
            str(output_path),
            "--skip-empty",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "Skipping" in result.stdout
    assert not output_path.exists()


def test_upload_cx2_to_ndex_tolerates_index_level_failure(monkeypatch) -> None:
    class FakeNdex2:
        def __init__(self, *, host=None, username=None, password=None, **kwargs):
            self.host = host
            self.username = username
            self.password = password

        def save_new_cx2_network(self, cx2, visibility=None):
            assert visibility == "PUBLIC"
            return "https://test.ndexbio.org/v3/networks/1234-uuid"

        def set_network_system_properties(self, network_id, properties):
            assert network_id == "1234-uuid"
            assert properties == {"index_level": "META"}
            raise RuntimeError("500 test server error")

    monkeypatch.setattr(cx2_export, "Ndex2", FakeNdex2)

    url = cx2_export.upload_cx2_to_ndex(
        [{"CXVersion": "2.0"}],
        host="test.ndexbio.org",
        username="monarch-agent",
        password="secret",
        visibility="PUBLIC",
    )

    assert url == "https://test.ndexbio.org/viewer/networks/1234-uuid"


def test_upload_cx2_to_ndex_replaces_existing_networks_by_name(monkeypatch) -> None:
    calls: dict[str, list] = {
        "updated": [],
        "deleted": [],
        "visibility": [],
    }

    class FakeNdex2:
        def __init__(self, *, host=None, username=None, password=None, **kwargs):
            self.host = host
            self.username = username
            self.password = password

        def get_user_network_summaries(self, username, offset=0, limit=1000):
            assert username == "monarch-agent"
            assert offset == 0
            return [
                {
                    "externalId": "older-uuid",
                    "name": "Stargardt Disease",
                    "modificationTime": 10,
                },
                {
                    "externalId": "newer-uuid",
                    "name": "Stargardt Disease",
                    "modificationTime": 20,
                },
                {
                    "externalId": "other-uuid",
                    "name": "Other Network",
                    "modificationTime": 30,
                },
            ]

        def update_cx2_network(self, cx_stream, network_id):
            calls["updated"].append((network_id, cx_stream.read().decode("utf-8")))

        def make_network_public(self, network_id):
            calls["visibility"].append(("PUBLIC", network_id))

        def delete_network(self, network_id):
            calls["deleted"].append(network_id)

        def set_network_system_properties(self, network_id, properties):
            assert network_id == "newer-uuid"
            assert properties == {"index_level": "META"}

    monkeypatch.setattr(cx2_export, "Ndex2", FakeNdex2)

    url = cx2_export.upload_cx2_to_ndex(
        [{"CXVersion": "2.0"}],
        network_name="Stargardt Disease",
        host="test.ndexbio.org",
        username="monarch-agent",
        password="secret",
        visibility="PUBLIC",
        replace_existing=True,
    )

    assert calls["updated"] == [("newer-uuid", '[{"CXVersion": "2.0"}]')]
    assert calls["deleted"] == ["older-uuid"]
    assert calls["visibility"] == [("PUBLIC", "newer-uuid")]
    assert url == "https://test.ndexbio.org/viewer/networks/newer-uuid"
