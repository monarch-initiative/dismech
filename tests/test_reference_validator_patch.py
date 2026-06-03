"""Tests for local linkml-reference-validator compatibility patches."""

from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher
from linkml_reference_validator.models import ReferenceValidationConfig


def test_clinicaltrials_cache_path_uses_repo_lowercase_naming(tmp_path):
    import dismech.patch_reference_validator  # noqa: F401

    fetcher = ReferenceFetcher(ReferenceValidationConfig(cache_dir=tmp_path))

    cache_path = fetcher.get_cache_path("CLINICALTRIALS:NCT00004645")

    assert cache_path.name == "clinicaltrials_NCT00004645.md"
