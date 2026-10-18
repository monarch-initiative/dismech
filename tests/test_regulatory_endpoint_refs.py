"""Tests for disease-local biomarker links to source-level regulatory endpoints."""

from __future__ import annotations

from pathlib import Path

from dismech.kb_cache import load_document
from dismech.render import render_disorder

FDA_ENDPOINTS_PATH = Path("kb/surrogate_endpoints/fda_surrogate_endpoints.yaml")
DISORDERS_DIR = Path("kb/disorders")


def _load_yaml(path: Path) -> dict:
    return load_document(path) or {}


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


KB_ENTRY_DIRS = (Path("kb/disorders"), Path("kb/modules"), Path("kb/comorbidities"))


def _readouts_with_endpoint_fields(node, trail="") -> list[tuple[str, dict]]:
    """Every mapping in an entry that carries endpoint_context or regulatory refs."""
    found: list[tuple[str, dict]] = []
    if isinstance(node, dict):
        if "endpoint_context" in node or "regulatory_endpoint_refs" in node:
            found.append((trail, node))
        for key, value in node.items():
            found.extend(_readouts_with_endpoint_fields(value, f"{trail}.{key}"))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            found.extend(_readouts_with_endpoint_fields(value, f"{trail}[{index}]"))
    return found


def test_regulatory_surrogate_context_matches_regulatory_refs() -> None:
    """REGULATORY_SURROGATE is used exactly when regulatory_endpoint_refs is set.

    The value claims a regulator accepted the readout as a surrogate endpoint,
    which only the referenced source row can establish; and a readout that cites
    such a row is, by that citation, a regulatory surrogate, so labelling it
    PHARMACODYNAMIC or PROGNOSTIC hides the claim from anyone filtering on the
    enum.
    """
    problems: list[str] = []
    for directory in KB_ENTRY_DIRS:
        for path in sorted(directory.glob("*.yaml")):
            if path.name.endswith(".history.yaml"):
                continue
            for trail, readout in _readouts_with_endpoint_fields(_load_yaml(path)):
                has_refs = bool(readout.get("regulatory_endpoint_refs"))
                is_regulatory = readout.get("endpoint_context") == "REGULATORY_SURROGATE"
                if is_regulatory and not has_refs:
                    problems.append(
                        f"{path}{trail}: endpoint_context REGULATORY_SURROGATE needs "
                        "regulatory_endpoint_refs naming the source rows"
                    )
                elif has_refs and not is_regulatory:
                    problems.append(
                        f"{path}{trail}: has regulatory_endpoint_refs, so endpoint_context "
                        f"should be REGULATORY_SURROGATE, not {readout.get('endpoint_context')}"
                    )
    assert not problems, "\n".join(problems)
