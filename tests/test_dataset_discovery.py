"""Focused regression tests for dataset discovery metadata."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from discover_datasets import map_data_type, refine_data_type
from discover_omicsdi import clean_description
from disease_title_match import compile_phrases


def test_generic_copy_number_profiles_are_not_called_gwas():
    assert map_data_type("Genome variation profiling by genome tiling array") == ""
    assert map_data_type("Genome variation profiling by SNP array") == ""


def test_paired_single_nucleus_and_atac_is_multi_omics():
    coarse = map_data_type("Expression profiling by high throughput sequencing")
    assert (
        refine_data_type(
            "Expression profiling by high throughput sequencing",
            "paired snRNA-seq and snATAC-seq",
            coarse,
        )
        == "MULTI_OMICS"
    )


def test_spatial_10x_platform_is_not_inferred_as_multi_omics():
    coarse = map_data_type("Expression profiling by high throughput sequencing")
    text = "Spatial transcriptomics with the 10x Genomics Xenium platform"
    assert (
        refine_data_type(
            "Expression profiling by high throughput sequencing", text, coarse
        )
        == "SPATIAL_TRANSCRIPTOMICS"
    )


def test_comparison_to_single_cell_is_not_assay_evidence():
    coarse = map_data_type("Expression profiling by high throughput sequencing")
    text = "NETSseq profiles bulk nuclei. Compared to single-cell technologies, it detects lowly expressed genes."
    assert (
        refine_data_type(
            "Expression profiling by high throughput sequencing", text, coarse
        )
        == "BULK_RNA_SEQ"
    )


def test_bracketed_bulk_title_beats_single_cell_context():
    coarse = map_data_type("Expression profiling by high throughput sequencing")
    title = "[bulk RNA-seq] Myocardial infarction"
    assert (
        refine_data_type(
            "Expression profiling by high throughput sequencing",
            f"{title} compared with single-cell data",
            coarse,
            title,
        )
        == "BULK_RNA_SEQ"
    )


def test_spatial_organization_is_not_spatial_transcriptomics():
    assert (
        refine_data_type(
            "Genome binding/occupancy profiling",
            "ChIP-seq reveals spatial organization of chromatin",
            "CHIP_SEQ",
        )
        == "CHIP_SEQ"
    )


def test_spatial_single_cell_transcriptomics_is_spatial():
    coarse = map_data_type("Expression profiling by high throughput sequencing")
    assert (
        refine_data_type(
            "Expression profiling by high throughput sequencing",
            "single-cell spatial transcriptomics",
            coarse,
        )
        == "SPATIAL_TRANSCRIPTOMICS"
    )


def test_mass_spectrometry_is_proteomics():
    coarse = map_data_type("Expression profiling by high throughput sequencing")
    assert (
        refine_data_type(
            "Expression profiling by high throughput sequencing",
            "quantitative mass spectrometry proteomic analysis",
            coarse,
        )
        == "PROTEOMICS"
    )


def test_hyphenated_sibling_name_does_not_match():
    pick = compile_phrases(["Pick disease"])[0][1]
    small_cell = compile_phrases(["small cell lung cancer"])[0][1]
    assert pick.search("Niemann-Pick disease cohort") is None
    assert small_cell.search("non-small cell lung cancer cohort") is None
    assert pick.search("Pick disease cohort") is not None


def test_omicsdi_description_strips_markup_and_ends_at_sentence():
    text = (
        "First sentence. <a href='https://example.org'>Second sentence with markup</a>. "
        + "x" * 700
    )
    cleaned = clean_description(text)
    assert "<a" not in cleaned
    assert cleaned.endswith(".")
    assert len(cleaned) <= 600
