"""Focused regression tests for dataset discovery metadata."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from discover_datasets import (
    Candidate,
    map_data_type,
    refine_data_type,
    score_candidate,
)
from discover_omicsdi import clean_description, infer_data_type, infer_organism
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
    coarse = map_data_type("Other")
    assert (
        refine_data_type(
            "Other",
            "quantitative mass spectrometry proteomic analysis",
            coarse,
        )
        == "PROTEOMICS"
    )


def test_proteome_topic_does_not_switch_rna_seq_modality():
    coarse = map_data_type("Expression profiling by high throughput sequencing")
    assert (
        refine_data_type(
            "Expression profiling by high throughput sequencing",
            "Mouse RNA-seq resource reveals a restored proteome",
            coarse,
        )
        == "BULK_RNA_SEQ"
    )


def test_bracketed_rna_seq_beats_companion_chip_seq_context():
    coarse = map_data_type("Expression profiling by high throughput sequencing")
    title = "SuperSeries component [RNA-seq]"
    assert (
        refine_data_type(
            "Expression profiling by high throughput sequencing",
            f"{title} Companion H3K27ac ChIP-seq data are available.",
            coarse,
            title,
        )
        == "BULK_RNA_SEQ"
    )


def test_hyphenated_sibling_name_does_not_match():
    pick = compile_phrases(["Pick disease"])[0][1]
    small_cell = compile_phrases(["small cell lung cancer"])[0][1]
    assert pick.search("Niemann-Pick disease cohort") is None
    assert small_cell.search("non-small cell lung cancer cohort") is None
    assert pick.search("Pick disease cohort") is not None


def test_negated_disease_name_is_rejected_without_leading_qualifier():
    candidate = Candidate(
        accession="ega:test",
        title="Study of non-clear cell renal cell carcinoma",
        summary="",
    )
    score_candidate(candidate, ["clear cell renal cell carcinoma"], [], [])
    assert candidate.relevance == "CONFLICT"
    assert candidate.score == -10.0


def test_omicsdi_description_strips_markup_and_ends_at_sentence():
    text = (
        "First sentence. <a href='https://example.org'>Second sentence with markup</a>. "
        + "x" * 700
    )
    cleaned = clean_description(text)
    assert "<a" not in cleaned
    assert cleaned.endswith(".")
    assert len(cleaned) <= 600


def test_omicsdi_uses_assay_metadata_not_repository_prefix():
    hit = {"source": "massive", "omicsType": ["Metabolomics"]}
    assert infer_data_type(hit) == "METABOLOMICS"


def test_omicsdi_explicit_mixed_assays_are_multi_omics():
    hit = {
        "title": "Metabolic and Proteomic Changes in Disease",
        "omicsType": ["Proteomics"],
    }
    assert infer_data_type(hit) == "MULTI_OMICS"


def test_omicsdi_model_organism_uses_source_metadata():
    hit = {"organisms": [{"name": "Mus Musculus (ncbitaxon:10090)"}]}
    assert infer_organism(hit) == {
        "preferred_term": "mouse",
        "term": {"id": "NCBITaxon:10090", "label": "Mus musculus"},
    }


def test_omicsdi_authoritative_human_beats_a_model_system_in_the_title():
    hit = {
        "title": "Proteomics of patient tumours compared with a mouse xenograft model",
        "organisms": [{"name": "Homo sapiens"}],
    }
    assert infer_organism(hit) == {
        "preferred_term": "human",
        "term": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
    }


def test_omicsdi_human_tropic_virus_name_is_not_read_as_a_human_sample():
    # NCBI taxon names for these viruses begin with "Human", so a substring
    # match would claim the sample is human and suppress the title fallback.
    for virus in (
        "Human papillomavirus",
        "Human immunodeficiency virus 1",
        "Human herpesvirus 4",
    ):
        hit = {
            "title": "Viral replication in Vero cells",
            "organisms": [{"name": virus}],
        }
        assert infer_organism(hit) == {
            "preferred_term": "African green monkey",
            "term": {"id": "NCBITaxon:60711", "label": "Chlorocebus sabaeus"},
        }, virus


def test_omicsdi_model_organism_virus_name_is_not_read_as_that_host():
    # The same trap predates HUMAN_NAMES: these virus taxon names contain a
    # model-organism word, so the pathogen was being reported as the sample.
    for virus in (
        "Murine leukemia virus",
        "Rat cytomegalovirus",
        "Canine parvovirus",
    ):
        hit = {
            "title": "Viral replication in Vero cells",
            "organisms": [{"name": virus}],
        }
        assert infer_organism(hit)["term"]["id"] == "NCBITaxon:60711", virus


def test_omicsdi_human_entry_with_a_taxon_suffix_still_matches():
    hit = {
        "title": "mouse comparison",
        "organisms": [{"name": "Homo sapiens (ncbitaxon:9606)"}],
    }
    assert infer_organism(hit)["term"]["id"] == "NCBITaxon:9606"


def test_omicsdi_named_model_organism_wins_over_its_human_source():
    # Xenograft/patient-derived records name both; the model organism is the
    # conservative answer, so pattern order must not be reversed by the fix.
    hit = {
        "title": "PDX panel",
        "organisms": [{"name": "Homo sapiens"}, {"name": "Mus musculus"}],
    }
    assert infer_organism(hit)["term"]["id"] == "NCBITaxon:10090"


def test_omicsdi_vero_title_maps_to_green_monkey():
    hit = {
        "title": "Chikungunya replication in Vero cells",
        "organisms": [{"name": "Chikungunya virus"}],
    }
    assert infer_organism(hit) == {
        "preferred_term": "African green monkey",
        "term": {"id": "NCBITaxon:60711", "label": "Chlorocebus sabaeus"},
    }
