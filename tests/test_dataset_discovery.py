"""Focused regression tests for dataset discovery metadata."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from discover_datasets import map_data_type, refine_data_type
from disease_title_match import compile_phrases


def test_generic_copy_number_profiles_are_not_called_gwas():
    assert map_data_type("Genome variation profiling by genome tiling array") == ""
    assert map_data_type("Genome variation profiling by SNP array") == ""


def test_paired_single_nucleus_and_atac_is_multi_omics():
    coarse = map_data_type("Expression profiling by high throughput sequencing")
    assert refine_data_type("Expression profiling by high throughput sequencing", "paired snRNA-seq and snATAC-seq", coarse) == "MULTI_OMICS"


def test_hyphenated_sibling_name_does_not_match():
    pick = compile_phrases(["Pick disease"])[0][1]
    small_cell = compile_phrases(["small cell lung cancer"])[0][1]
    assert pick.search("Niemann-Pick disease cohort") is None
    assert small_cell.search("non-small cell lung cancer cohort") is None
    assert pick.search("Pick disease cohort") is not None
