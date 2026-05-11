"""Tests for disease-local biomarker links to source-level regulatory endpoints."""

from __future__ import annotations

from pathlib import Path

import yaml

from dismech.render import render_disorder


FDA_ENDPOINTS_PATH = Path("kb/surrogate_endpoints/fda_surrogate_endpoints.yaml")
DISORDERS_DIR = Path("kb/disorders")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text()) or {}


def _fda_rows_by_id() -> dict[str, dict]:
    data = _load_yaml(FDA_ENDPOINTS_PATH)
    return {
        row["row_id"]: row
        for row in data.get("surrogate_endpoints", [])
        if isinstance(row, dict) and row.get("row_id")
    }


def _regulatory_refs_by_disease() -> dict[Path, set[str]]:
    refs_by_file: dict[Path, set[str]] = {}
    for path in sorted(DISORDERS_DIR.glob("*.yaml")):
        if path.name.endswith(".history.yaml"):
            continue
        data = _load_yaml(path)
        refs: set[str] = set()
        for biomarker in data.get("biochemical") or []:
            if not isinstance(biomarker, dict):
                continue
            for readout in biomarker.get("readouts") or []:
                if not isinstance(readout, dict):
                    continue
                for ref in readout.get("regulatory_endpoint_refs") or []:
                    refs.add(str(ref))
        if refs:
            refs_by_file[path] = refs
    return refs_by_file


def test_disease_regulatory_endpoint_refs_resolve_to_source_rows() -> None:
    rows_by_id = _fda_rows_by_id()

    for disease_path, refs in _regulatory_refs_by_disease().items():
        relative_path = disease_path.as_posix()
        for ref in refs:
            assert ref in rows_by_id, (
                f"{relative_path} references unknown FDA row {ref}"
            )
            mapped_files = rows_by_id[ref].get("mapped_disease_files") or []
            assert relative_path in mapped_files, (
                f"{relative_path} references {ref}, but the FDA row does not map "
                "back to that disease file"
            )


def test_first_biochemical_surrogate_endpoint_batch_is_linked() -> None:
    refs_by_file = _regulatory_refs_by_disease()

    expected = {
        Path("kb/disorders/Duchenne_Muscular_Dystrophy.yaml"): {
            "FDA-SE-adult-noncancer-022",
            "FDA-SE-pediatric-noncancer-017",
        },
        Path("kb/disorders/Fabry_Disease.yaml"): {
            "FDA-SE-adult-noncancer-024",
            "FDA-SE-adult-noncancer-025",
            "FDA-SE-pediatric-noncancer-019",
        },
        Path("kb/disorders/Sickle_Cell_Disease.yaml"): {
            "FDA-SE-adult-noncancer-078",
            "FDA-SE-pediatric-noncancer-054",
        },
        Path("kb/disorders/Beta_Thalassemia.yaml"): {
            "FDA-SE-adult-noncancer-073",
            "FDA-SE-pediatric-noncancer-051",
        },
    }

    for disease_path, row_ids in expected.items():
        assert row_ids <= refs_by_file.get(disease_path, set())


def test_rendered_biomarker_readouts_show_resolved_fda_endpoint_context(
    tmp_path: Path,
) -> None:
    output_path = tmp_path / "Duchenne_Muscular_Dystrophy.html"

    render_disorder(Path("kb/disorders/Duchenne_Muscular_Dystrophy.yaml"), output_path)

    html = output_path.read_text()
    assert "FDA-SE-adult-noncancer-022" in html
    assert "Skeletal muscle dystrophin" in html
    assert "Reasonably Likely Surrogate Endpoint" in html
