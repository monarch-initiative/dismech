"""The curation-queue coverage audit must not over-retire a shared anchor.

dismech#10165 and dismech#16243: design decisions §3a lets a promoted stratum
with no MONDO class of its own anchor its own `disease_term` to its broader
parent's MONDO id, recording that in `mappings.mondo_mappings` (historically
`skos:narrowMatch`, now `skos:broadMatch`). `curated_mondo_ids()` must not
read that anchor as "the parent disease is curated" -- a stratum anchoring to
a shared term is not the same claim as an entry that IS that term's class.
These tests pin the fix: a shared `disease_term` only counts as curated when
some entry in the group also claims `skos:exactMatch` for it.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from audit_curation_queue_coverage import curated_mondo_ids


def _write(path: Path, doc: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(doc), encoding="utf-8")


def _stratum(curie: str, predicate: str) -> dict:
    """A promoted stratum anchoring its disease_term to a shared parent."""
    return {
        "disease_term": {"term": {"id": curie, "label": "x"}},
        "mappings": {
            "mondo_mappings": [
                {"term": {"id": curie}, "mapping_predicate": predicate}
            ]
        },
    }


def test_shared_anchor_with_no_exact_claimant_is_not_covered(tmp_path, monkeypatch):
    """The live bug: MONDO:0005575-shaped groups, all broadMatch, no class entry."""
    monkeypatch.chdir(tmp_path)
    curie = "MONDO:0005575"
    _write(tmp_path / "kb/disorders/Stratum_One.yaml", _stratum(curie, "skos:broadMatch"))
    _write(tmp_path / "kb/disorders/Stratum_Two.yaml", _stratum(curie, "skos:broadMatch"))

    assert curie not in curated_mondo_ids()


def test_legacy_narrow_match_anchor_with_no_exact_claimant_is_not_covered(
    tmp_path, monkeypatch
):
    """Same bug, the legacy skos:narrowMatch spelling (the shape #10165 reported)."""
    monkeypatch.chdir(tmp_path)
    curie = "MONDO:0005575"
    _write(tmp_path / "kb/disorders/Stratum_One.yaml", _stratum(curie, "skos:narrowMatch"))
    _write(tmp_path / "kb/disorders/Stratum_Two.yaml", _stratum(curie, "skos:narrowMatch"))

    assert curie not in curated_mondo_ids()


def test_shared_anchor_with_an_exact_claimant_is_covered(tmp_path, monkeypatch):
    """Once a real class entry exists (exactMatch), the shared term is covered."""
    monkeypatch.chdir(tmp_path)
    curie = "MONDO:0004989"
    _write(
        tmp_path / "kb/disorders/Breast_Carcinoma.yaml",
        {
            "disease_term": {"term": {"id": curie, "label": "breast carcinoma"}},
            "mappings": {
                "mondo_mappings": [
                    {"term": {"id": curie}, "mapping_predicate": "skos:exactMatch"}
                ]
            },
        },
    )
    _write(
        tmp_path / "kb/disorders/PIK3CA_Mutant_Breast_Cancer.yaml",
        _stratum(curie, "skos:broadMatch"),
    )

    covered = curated_mondo_ids()
    assert covered.get(curie) == "Breast_Carcinoma"


def test_unshared_disease_term_is_covered_with_no_mapping_row(tmp_path, monkeypatch):
    """The ordinary case -- one entry, no sharing -- is unaffected by the fix."""
    monkeypatch.chdir(tmp_path)
    curie = "MONDO:0007947"
    _write(
        tmp_path / "kb/disorders/Marfan_Syndrome.yaml",
        {"disease_term": {"term": {"id": curie, "label": "Marfan syndrome"}}},
    )

    assert curated_mondo_ids().get(curie) == "Marfan_Syndrome"


def test_narrow_match_to_an_unshared_curie_still_retires_it(tmp_path, monkeypatch):
    """The legitimate case: a narrower MONDO phase class the entry's own content
    covers (the Hepatitis_C -> MONDO:0100371 pattern), not anyone's disease_term.
    """
    monkeypatch.chdir(tmp_path)
    phase_curie = "MONDO:0100371"
    _write(
        tmp_path / "kb/disorders/Hepatitis_C.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0005231", "label": "hepatitis C"}},
            "mappings": {
                "mondo_mappings": [
                    {
                        "term": {"id": phase_curie},
                        "mapping_predicate": "skos:narrowMatch",
                    }
                ]
            },
        },
    )

    assert curated_mondo_ids().get(phase_curie) == "Hepatitis_C"


def test_unshared_broad_match_never_retires_its_target(tmp_path, monkeypatch):
    """broadMatch is a cross-reference and must never retire a concept (CLAUDE.md),
    even when it is not the shared-anchor case this fix is otherwise about --
    e.g. an entry recording broadMatch to some unrelated broader concept.
    """
    monkeypatch.chdir(tmp_path)
    broader_curie = "MONDO:0700096"
    _write(
        tmp_path / "kb/disorders/Some_Disease.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0012345", "label": "some disease"}},
            "mappings": {
                "mondo_mappings": [
                    {
                        "term": {"id": broader_curie},
                        "mapping_predicate": "skos:broadMatch",
                    }
                ]
            },
        },
    )

    assert broader_curie not in curated_mondo_ids()


def test_has_subtypes_term_is_always_covered(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    sub_curie = "MONDO:0016862"
    _write(
        tmp_path / "kb/disorders/Alagille_syndrome.yaml",
        {
            "disease_term": {"term": {"id": "MONDO:0016662", "label": "Alagille syndrome"}},
            "has_subtypes": [{"subtype_term": {"term": {"id": sub_curie}}}],
        },
    )

    assert curated_mondo_ids().get(sub_curie) == "Alagille_syndrome"
