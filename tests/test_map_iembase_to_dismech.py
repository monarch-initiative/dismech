from __future__ import annotations

import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import map_iembase_to_dismech as mid  # noqa: E402


def test_alias_variants_strip_gene_related_prefix() -> None:
    aliases = mid.alias_variants(
        "GALNS-related N-Acetylgalactosamine 6-sulfatase deficiency"
    )

    assert "galns related n acetylgalactosamine 6 sulfatase deficiency" in aliases
    assert "n acetylgalactosamine 6 sulfatase deficiency" in aliases


def test_normalize_text_handles_mps_roman_variants() -> None:
    assert mid.normalize_text("Mucopolysaccharidosis type IVB") == (
        "mucopolysaccharidosis type 4b"
    )
    assert mid.normalize_text("MPS IVA") == "mps 4a"


def test_identifier_match_maps_single_entity() -> None:
    entity = mid.DismechEntity(
        entity_key="Phenylketonuria",
        entry_type="disease",
        name="Phenylketonuria",
        source_file="Phenylketonuria.yaml",
        identifiers={"OMIM:261600"},
    )
    mid.add_alias(entity, "Phenylketonuria")
    by_identifier, _by_mondo, by_alias, by_gene, by_token = mid.build_lookup([entity])

    result = mid.match_record(
        {
            "name": "PAH-related Phenylalanine hydroxylase deficiency",
            "omim_no": "261600",
            "orphacode": None,
        },
        entities=[entity],
        by_identifier=by_identifier,
        by_alias=by_alias,
        by_gene=by_gene,
        by_token=by_token,
    )

    assert result.status == "MAPPED"
    assert result.method == "identifier:OMIM:261600"
    assert result.entities == [entity]


def test_fuzzy_candidate_uses_token_index() -> None:
    entity = mid.DismechEntity(
        entity_key="Maple_Syrup_Urine_Disease",
        entry_type="disease",
        name="Maple syrup urine disease",
        source_file="Maple_Syrup_Urine_Disease.yaml",
    )
    mid.add_alias(entity, "Maple syrup urine disease")
    by_identifier, _by_mondo, by_alias, by_gene, by_token = mid.build_lookup([entity])

    result = mid.match_record(
        {
            "name": "Maple syrup urin disease",
            "omim_no": None,
            "orphacode": None,
        },
        entities=[entity],
        by_identifier=by_identifier,
        by_alias=by_alias,
        by_gene=by_gene,
        by_token=by_token,
    )

    assert result.status == "CANDIDATE"
    assert result.method == "fuzzy_alias"
    assert result.best_candidate == entity
