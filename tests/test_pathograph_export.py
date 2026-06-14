"""Tests for the Mondo-keyed pathograph exporter."""

import json
import shutil
import tempfile
from pathlib import Path

from dismech.export.pathograph_export import (
    PathographExporter,
    _disorder_term_id,
    _iter_gene_ids,
    slugify,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
DISORDERS = REPO_ROOT / "kb" / "disorders"


def test_disorder_term_id_uppercases_and_handles_missing():
    assert (
        _disorder_term_id({"disease_term": {"term": {"id": "mondo:0010200"}}})
        == "MONDO:0010200"
    )
    assert _disorder_term_id({}) is None
    assert _disorder_term_id({"disease_term": {"term": {}}}) is None


def test_iter_gene_ids_collects_nested_and_skips_idless():
    node = {
        "meta": {
            "gene_terms": [
                {"label": "ATP7B", "id": "hgnc:870"},
                {"label": "NoId"},  # no id -> skipped
            ],
            "genetic_context": {
                "gene_terms": [{"label": "AHR", "id": "hgnc:348"}],
            },
        }
    }
    assert sorted(_iter_gene_ids(node)) == ["hgnc:348", "hgnc:870"]


def test_export_skips_disorders_without_mondo_or_edges():
    """A disorder with no Mondo id, and one with a Mondo but no edges, are skipped."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        inp = tmp_path / "in"
        inp.mkdir()
        # No disease_term -> no Mondo
        (inp / "no_mondo.yaml").write_text("name: No Mondo\n")
        # Has Mondo but no pathophysiology/edges -> empty graph
        (inp / "no_edges.yaml").write_text(
            "name: No Edges\ndisease_term:\n  term:\n    id: MONDO:9999999\n"
        )

        stats = PathographExporter().export(
            sorted(inp.glob("*.yaml")), tmp_path / "out"
        )

        assert stats["pathographs"] == 0
        assert stats["skipped_no_mondo"] == 1
        assert stats["skipped_no_graph"] == 1
        index = json.loads((tmp_path / "out" / "index.json").read_text())
        assert index == {}


def _run_on(filenames: list[str], out_dir: Path) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        inp = Path(tmp)
        files = []
        for name in filenames:
            shutil.copy(DISORDERS / name, inp / name)
            files.append(inp / name)
        return PathographExporter().export(sorted(files), out_dir)


def test_export_is_lossless_and_indexes_genes():
    """Real fixtures: every indexed file exists, gene edges are reverse-indexed."""
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp)
        stats = _run_on(["Wilsons_Disease.yaml", "Gaucher_Disease.yaml"], out)

        index = json.loads((out / "index.json").read_text())
        by_gene = json.loads((out / "by_gene.json").read_text())

        # Every file referenced by the index exists on disk (no clobbering).
        for entries in index.values():
            for entry in entries:
                assert (out / entry["file"]).exists()

        # Wilson's pathograph has edges and surfaces the ATP7B (hgnc:870) gene link.
        assert "MONDO:0010200" in index
        wilson_file = index["MONDO:0010200"][0]["file"]
        graph = json.loads((out / wilson_file).read_text())
        assert graph["edges"]
        assert by_gene["hgnc:870"] == ["MONDO:0010200"]
        assert stats["pathographs"] == 2


def test_nodes_carry_evidence_references():
    """Nodes re-attach the evidence references (not just the count)."""
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp)
        _run_on(["Wilsons_Disease.yaml"], out)
        index = json.loads((out / "index.json").read_text())
        graph = json.loads((out / index["MONDO:0010200"][0]["file"]).read_text())

        evidenced = [n for n in graph["nodes"] if (n.get("meta") or {}).get("evidence")]
        assert evidenced, "expected at least one node with evidence references"
        node = evidenced[0]
        ev = node["meta"]["evidence"][0]
        assert ev["reference"]
        # attached references never exceed the reported count
        assert 0 < len(node["meta"]["evidence"]) <= node["meta"]["evidence_count"]


def test_colliding_mondo_ids_get_distinct_files():
    """Two distinct disorders sharing a Mondo id each get their own file."""
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp)
        _run_on(
            ["EBV_Associated_Gastric_Cancer.yaml", "HER2_Positive_Gastric_Cancer.yaml"],
            out,
        )
        index = json.loads((out / "index.json").read_text())

        entries = index["MONDO:0001056"]
        assert len(entries) == 2
        files = {e["file"] for e in entries}
        assert len(files) == 2  # distinct, not clobbered
        for f in files:
            assert (out / f).exists()


def test_slugify():
    assert slugify("22q11.2 Deletion (Syndrome)/X") == "22q11.2_Deletion_Syndrome_X"
