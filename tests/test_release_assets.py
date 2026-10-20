"""Tests for the release-asset builders (dismech.export.release_assets)."""

import json
import zipfile
from pathlib import Path

import yaml

from dismech.export import release_assets

DISORDER = {
    "name": "Test Disease",
    "disease_term": {"term": {"id": "MONDO:0000001", "label": "test disease"}},
    "pathophysiology": [
        {"name": "Cause", "downstream": [{"target": "Effect"}]},
        {"name": "Effect"},
    ],
}


def _write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def _kb(tmp_path: Path) -> Path:
    kb = tmp_path / "kb"
    _write(kb / "disorders" / "Test_Disease.yaml", yaml.safe_dump(DISORDER))
    _write(kb / "modules" / "fibrosis.yaml", "name: Fibrosis Module\n")
    _write(kb / "hypotheses" / "Test_Disease" / "h1" / "assessment.yaml", "a: 1\n")
    _write(kb / "hypotheses" / "Test_Disease" / "h1" / "reconciliation.yaml", "a: 1\n")
    _write(
        kb / "hypotheses" / "Test_Disease" / "h2" / "openscientist.md.job.yaml",
        "a: 1\n",
    )
    _write(kb / "hypotheses" / "Test_Disease" / "h1" / "report.md", "provider report\n")
    _write(kb / "hypotheses" / "Test_Disease" / "h1" / "figure.png", "png")
    _write(kb / "genes" / "curated" / "hgnc_1.md", "summary\n")
    _write(kb / "genes" / "ingest" / "hgnc.tsv", "id\tsymbol\n")
    _write(kb / "node_classes" / "pathograph_node_classes.txt", "CELLULAR\n")
    return kb


def test_kb_zip_keeps_curated_content_and_drops_ingest_and_provider_artifacts(tmp_path):
    kb = _kb(tmp_path)
    zip_path = tmp_path / "kb.zip"
    release_assets.build_kb_zip(kb, zip_path)

    names = set(zipfile.ZipFile(zip_path).namelist())
    assert names == {
        "kb/disorders/Test_Disease.yaml",
        "kb/modules/fibrosis.yaml",
        "kb/hypotheses/Test_Disease/h1/assessment.yaml",
        "kb/hypotheses/Test_Disease/h1/reconciliation.yaml",
        "kb/hypotheses/Test_Disease/h2/openscientist.md.job.yaml",
        "kb/genes/curated/hgnc_1.md",
        "kb/node_classes/pathograph_node_classes.txt",
    }


def test_zips_are_byte_identical_across_rebuilds(tmp_path):
    kb = _kb(tmp_path)
    first, second = tmp_path / "a.zip", tmp_path / "b.zip"
    release_assets.build_kb_zip(kb, first)
    release_assets.build_kb_zip(kb, second)
    assert first.read_bytes() == second.read_bytes()


def test_cx2_zip_writes_one_network_per_disorder_with_edges(tmp_path):
    kb = _kb(tmp_path)
    _write(kb / "disorders" / "No_Edges.yaml", yaml.safe_dump({"name": "No Edges"}))
    zip_path = tmp_path / "cx2.zip"

    stats = release_assets.build_cx2_zip(
        kb / "disorders", zip_path, release_version="v1"
    )

    assert stats == {"networks": 1, "skipped_no_edges": 1}
    names = zipfile.ZipFile(zip_path).namelist()
    assert names == ["pathographs_cx2/Test_Disease.cx2.json"]


def test_kgx_metadata_counts_categories_and_predicates(tmp_path):
    nodes = _write(
        tmp_path / "nodes.jsonl",
        "\n".join(
            json.dumps(n)
            for n in [
                {"id": "MONDO:1", "category": ["biolink:Disease"]},
                {"id": "HP:1", "category": ["biolink:PhenotypicFeature"]},
                {"id": "HP:2", "category": ["biolink:PhenotypicFeature"]},
            ]
        )
        + "\n",
    )
    edges = _write(
        tmp_path / "edges.jsonl",
        json.dumps(
            {
                "subject": "MONDO:1",
                "predicate": "biolink:has_phenotype",
                "object": "HP:1",
            }
        )
        + "\n",
    )

    metadata = release_assets.kgx_metadata(
        nodes, edges, biolink=True, experimental=False
    )

    assert metadata["node_count"] == 3
    assert metadata["edge_count"] == 1
    assert metadata["nodes_by_category"] == {
        "biolink:Disease": 1,
        "biolink:PhenotypicFeature": 2,
    }
    assert metadata["edges_by_predicate"] == {"biolink:has_phenotype": 1}
    assert metadata["biolink_model_version"]

    unversioned = release_assets.kgx_metadata(
        nodes, edges, biolink=False, experimental=True
    )
    assert "biolink_model_version" not in unversioned
    assert unversioned["experimental"] is True


def test_manifest_counts_entries_and_hashes_assets(tmp_path):
    kb = _kb(tmp_path)
    assets = tmp_path / "dist"
    _write(assets / "kb.zip", "zip bytes")
    _write(assets / "release_manifest.json", "{}")

    manifest = release_assets.build_manifest(kb, assets, tag="v1", commit="abc")

    assert manifest["release_tag"] == "v1"
    counts = manifest["kb_entry_counts"]
    assert counts["disorders"] == 1
    assert counts["modules"] == 1
    assert counts["hypotheses_assessed"] == 1
    assert counts["genes/curated"] == 1
    assert counts["groupings"] == 0
    # The manifest never lists itself.
    assert [a["name"] for a in manifest["assets"]] == ["kb.zip"]
    assert len(manifest["assets"][0]["sha256"]) == 64


def test_every_uploaded_release_file_has_a_downloads_page_row():
    """A file a release workflow attaches must be listed on the Downloads page."""
    root = Path(__file__).resolve().parents[1]
    page = (root / "downloads" / "index.html").read_text(encoding="utf-8")
    uploaded = set()
    for workflow in (root / ".github" / "workflows").glob("*release*.yaml"):
        for job in yaml.safe_load(workflow.read_text(encoding="utf-8"))[
            "jobs"
        ].values():
            for step in job["steps"]:
                if str(step.get("uses", "")).startswith("softprops/action-gh-release"):
                    uploaded.update(
                        Path(line.strip()).name
                        for line in step["with"]["files"].splitlines()
                        if line.strip()
                    )
    assert uploaded, "no release uploads found; has the upload action changed?"
    missing = sorted(
        name for name in uploaded if f"releases/latest/download/{name}" not in page
    )
    assert not missing, f"release files with no Downloads page link: {missing}"


def test_kgx_tsv_keeps_every_property_and_protects_quoted_pipes(tmp_path):
    edges = _write(
        tmp_path / "edges.jsonl",
        json.dumps(
            {
                "id": "e1",
                "subject": "MONDO:1",
                "predicate": "biolink:has_phenotype",
                "object": "HP:1",
                "category": ["biolink:Association"],
                "publications": ["PMID:1", "ORPHA:2"],
                "supporting_text": ['HP:1 | Jaundice | "Frequent"\nsecond\tline'],
            }
        )
        + "\n"
        + json.dumps({"id": "e2", "subject": "a", "predicate": "p", "object": "b"})
        + "\n",
    )
    out = tmp_path / "edges.tsv"

    assert release_assets.jsonl_to_kgx_tsv(edges, out, "edges") == 2

    header, first, second = out.read_text(encoding="utf-8").splitlines()
    columns = header.split("\t")
    assert columns[:5] == ["id", "subject", "predicate", "object", "category"]
    row = dict(zip(columns, first.split("\t")))
    assert row["publications"] == "PMID:1|ORPHA:2"
    assert row["supporting_text"] == 'HP:1 ¦ Jaundice ¦ "Frequent" second line'
    # Properties a record lacks are empty cells, not missing columns.
    assert len(second.split("\t")) == len(columns)
