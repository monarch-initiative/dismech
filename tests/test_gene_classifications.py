"""Regression tests for the gene-classification collections under ``kb/gene_classifications/``.

These are transcriptions of external gene-classification systems (see
``GeneClassificationCollection``). The tests check the structural contract and
the things that silently go wrong in a scraped transcription: values that are
not members of the declared enum, CURIEs in the wrong prefix casing, duplicated
genes, and the symbol-resolution regressions described in
``scripts/fetch_nmd_gene_table.py``.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

from dismech.yaml_io import safe_load_path


def _load_scraper():
    """Import the scraper by path; ``scripts/`` is not an importable package."""
    spec = importlib.util.spec_from_file_location(
        "fetch_nmd_gene_table", Path("scripts/fetch_nmd_gene_table.py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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
    HMERF, dilated/hypertrophic cardiomyopathy, and a motoneuron-disease
    presentation are six different groups.
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


def test_group_coordinates_are_read_only_inside_parentheses() -> None:
    """Coordinates are parenthesised; decimals in disease or locus names are not.

    TAZ is listed with its old locus designation "G4.5". A bare
    ``\\d{1,2}\\.\\d+`` scan over the whole cell reads that as group 4 and puts
    TAFAZZIN -- a cardioskeletal myopathy with proximal weakness -- into distal
    myopathies. This is the exact cell text from the live table.
    """
    parse = _load_scraper().parse_group_coordinates

    taz_cell = (
        "* Barth syndrome - BTHS (10.103, 10.90)"
        "* Endocardial fibroelastosis-2 - G4.5 (10.103, 10.90)"
        "* Noncompaction of left ventricular myocardium, isolated - INVM (10.103, 10.90)"
    )
    assert parse(taz_cell) == {10}, "G4.5 must not be read as a group coordinate"

    # A genuinely multi-group cell still parses every coordinate.
    assert parse("* A - X (4.4, 1.2)* B - Y (10.9)") == {1, 4, 10}
    # Out-of-range group numbers are dropped rather than emitted.
    assert parse("* C - Z (99.1)") == set()


def test_short_symbols_resolve_only_via_the_allow_list() -> None:
    """The resolution floor must make an unhandled pattern loud, not silent.

    Without a minimum prefix length, resolution walks down to a one- or
    two-letter match and `None` becomes unreachable, so a mis-resolution looks
    exactly like a correct one. KY (kyphoscoliosis peptidase) is the worked
    case: it is a real two-letter symbol in the table and is allow-listed.
    """
    scraper = _load_scraper()
    approved = {"KY": ("hgnc:21208", "KY"), "ZZ": ("hgnc:99999", "ZZ")}

    resolved = scraper.resolve_symbol("KYKyphoscoliosis peptidase", approved, {})
    assert resolved is not None and resolved[1][1] == "KY"

    # Same shape, but not allow-listed: must fail rather than resolve.
    assert scraper.resolve_symbol("ZZSome protein", approved, {}) is None


def test_header_assertion_covers_every_positional_column() -> None:
    """The header guard must cover every column read by index, including cells[2].

    The scraper takes the gene from ``cells[0]`` and the coordinates from
    ``cells[2]``. Asserting only the first two headers would let a column
    inserted at position 2 pass while silently changing what is parsed as
    coordinates -- the exact failure the assertion exists to prevent.
    """
    scraper = _load_scraper()
    assert len(scraper._EXPECTED_HEADER) >= 3, (
        "header assertion must cover cells[2], the coordinate column"
    )
    assert "allelic disease phenotypes" in scraper._EXPECTED_HEADER[2]


def test_short_symbol_allow_list_has_no_unreachable_entries() -> None:
    """Only symbols shorter than the floor are ever consulted.

    An entry at or above ``_MIN_SYMBOL_LEN`` is dead config: the floor never
    rejects a prefix that long, so the allow-list is not read for it.
    """
    scraper = _load_scraper()
    unreachable = sorted(
        s for s in scraper._SHORT_SYMBOLS if len(s) >= scraper._MIN_SYMBOL_LEN
    )
    assert not unreachable, (
        f"_SHORT_SYMBOLS entries never consulted (len >= "
        f"{scraper._MIN_SYMBOL_LEN}): {unreachable}"
    )


def test_nmd_gene_table_has_no_unresolved_symbols() -> None:
    """A committed collection should carry no unresolved-symbol note.

    The note is how the scraper reports a symbol it could not resolve. Its
    presence means a run-together pattern needs handling or a short symbol
    needs allow-listing -- not that the row should be left out.
    """
    collection = _collection(NMD_GENE_TABLE_PATH)
    assert "unresolved" not in (collection.get("notes") or "").lower()
