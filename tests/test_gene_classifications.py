"""Regression tests for the gene-classification collections under ``kb/gene_classifications/``.

These are transcriptions of external gene-classification systems (see
``GeneClassificationCollection``). The tests check the structural contract and
the things that silently go wrong in a scraped transcription: values that are
not members of the declared enum, CURIEs in the wrong prefix casing, duplicated
genes, and the symbol-resolution regressions described in
``scripts/fetch_nmd_gene_table.py``.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

from dismech.yaml_io import safe_load_path

SCHEMA_PATH = Path("src/dismech/schema/dismech.yaml")
GENE_CLASSIFICATION_DIR = Path("kb/gene_classifications")
NMD_GENE_TABLE_PATH = GENE_CLASSIFICATION_DIR / "nmd_gene_table.yaml"

#: Classification system identifier -> the enum its ``values`` are drawn from.
SYSTEM_ENUMS = {"GENE_TABLE_NMD": "GeneTableNMDGroupEnum"}

COLLECTION_PATHS = sorted(GENE_CLASSIFICATION_DIR.glob("*.yaml"))


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


def _collection(path: Path) -> dict:
    return safe_load_path(path)


def test_gene_classification_directory_is_not_empty() -> None:
    assert COLLECTION_PATHS, f"no collections found under {GENE_CLASSIFICATION_DIR}"


@pytest.mark.parametrize("path", COLLECTION_PATHS, ids=lambda p: p.stem)
def test_collection_has_source_provenance(path: Path) -> None:
    """Provenance lives at file level, so every collection must carry it."""
    collection = _collection(path)
    for field in (
        "name",
        "classification_system",
        "source_url",
        "retrieved_date",
        "genes",
    ):
        assert collection.get(field), f"{path.name} is missing {field}"
    assert collection["classification_system"] in SYSTEM_ENUMS, (
        f"{path.name} declares unknown classification_system "
        f"{collection['classification_system']!r}; add it to SYSTEM_ENUMS "
        "together with the enum its values come from"
    )


@pytest.mark.parametrize("path", COLLECTION_PATHS, ids=lambda p: p.stem)
def test_collection_values_are_enum_members(
    path: Path, schema_view: SchemaView
) -> None:
    """Every value must be a permissible value of the declared enum.

    ``GeneClassification.values`` has range ``string`` because each collection
    draws from a different enum, so this is the check that keeps it honest.
    """
    collection = _collection(path)
    enum_name = SYSTEM_ENUMS[collection["classification_system"]]
    permissible = set(schema_view.get_enum(enum_name).permissible_values)

    bad: list[str] = []
    for row in collection["genes"]:
        label = row["gene"]["term"]["id"]
        assert row.get("values"), f"{path.name}: {label} has no values"
        for value in row["values"]:
            if value not in permissible:
                bad.append(f"{label}: {value!r}")
    assert not bad, f"{path.name}: values not in {enum_name}: {bad}"


@pytest.mark.parametrize("path", COLLECTION_PATHS, ids=lambda p: p.stem)
def test_collection_genes_are_unique_and_well_formed(path: Path) -> None:
    """One row per gene, each bound to a lowercase-prefixed HGNC CURIE.

    dismech uses the lowercase ``hgnc:`` prefix (see CLAUDE.md); an uppercase
    one silently fails term validation.
    """
    collection = _collection(path)
    seen: dict[str, str] = {}
    for row in collection["genes"]:
        term = row["gene"]["term"]
        curie, label = term["id"], term["label"]
        assert curie.startswith("hgnc:"), (
            f"{path.name}: {curie} is not a lowercase hgnc: CURIE"
        )
        assert curie not in seen, (
            f"{path.name}: {curie} appears twice ({seen[curie]} and {label}); "
            "rows for one gene should be merged, not repeated"
        )
        seen[curie] = label
        assert row["gene"]["preferred_term"] == label
        # A source_label is only meaningful when it differs from the approved symbol.
        assert row.get("source_label") != label


def test_nmd_gene_table_resolves_run_together_symbols() -> None:
    """Guard the two symbol-resolution regressions the scraper was built around.

    The gene table renders a gene cell as symbol-plus-protein-name with no
    separator, so resolution is by prefix. Matching on length alone picks
    ``LAMB2L`` (a pseudogene alias) over LAMB2, and ``ARA`` (an ABCC6 alias)
    over AR. Both genes must be present, correctly grouped, and neither
    impostor may appear.
    """
    rows = {
        r["gene"]["term"]["label"]: r for r in _collection(NMD_GENE_TABLE_PATH)["genes"]
    }

    assert "AR" in rows, (
        "androgen receptor (Kennedy disease) should resolve from 'ARAndrogen'"
    )
    assert rows["AR"]["values"] == ["spinal_muscular_atrophies_motoneuron_diseases"]
    assert "LAMB2" in rows, (
        "LAMB2 (Pierson syndrome/CMS) should resolve from 'LAMB2Laminin'"
    )
    assert rows["LAMB2"]["values"] == ["congenital_myasthenic_syndromes"]

    assert "ABCC6" not in rows, "ABCC6 is not a neuromuscular gene; 'ARA' mis-resolved"
    assert "LAMB2P1" not in rows, "LAMB2P1 is a pseudogene; 'LAMB2L' mis-resolved"


def test_nmd_gene_table_membership_is_set_valued() -> None:
    """A gene appears once per clinically distinct allelic presentation.

    This is the property that makes gene classification a separate axis from
    disease classification, so it is asserted rather than assumed. TTN is the
    canonical case: Udd distal myopathy, LGMDR10, centronuclear myopathy,
    HMERF, and dilated/hypertrophic cardiomyopathy are five different groups.
    """
    rows = {
        r["gene"]["term"]["label"]: r for r in _collection(NMD_GENE_TABLE_PATH)["genes"]
    }

    assert set(rows["TTN"]["values"]) == {
        "muscular_dystrophies",
        "congenital_myopathies",
        "distal_myopathies",
        "other_myopathies",
        "hereditary_cardiomyopathies",
        "spinal_muscular_atrophies_motoneuron_diseases",
    }
    # Single-group genes must stay single-group: DMPK is myotonic dystrophy only,
    # and the non-dystrophic myotonias belong to the ion channel group instead.
    assert rows["DMPK"]["values"] == ["myotonic_syndromes"]
    assert set(rows["CLCN1"]["values"]) == {
        "myotonic_syndromes",
        "ion_channel_muscle_diseases",
    }

    multi = [label for label, row in rows.items() if len(row["values"]) > 1]
    assert len(multi) > 50, (
        "expected many multi-group genes; a collapse to near-single-valued means "
        "the allelic-phenotype column stopped being parsed"
    )
