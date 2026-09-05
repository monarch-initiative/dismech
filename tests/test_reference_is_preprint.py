"""Unit tests for preprint detection behind the "not peer-reviewed" badge.

The DOI-pattern half must not misfire on Cold Spring Harbor *journal* DOIs
(``10.1101/gad.*``, ``10.1101/cshperspect.*`` etc.), which share the bioRxiv/
medRxiv ``10.1101`` prefix but are peer-reviewed articles, not preprints.
"""

import pytest

from dismech.render import _reference_is_preprint


@pytest.mark.parametrize(
    "reference",
    [
        "DOI:10.64898/2026.04.30.721933",  # bioRxiv (new prefix), dated
        "DOI:10.1101/2024.01.09.574075",  # bioRxiv, dated
        "DOI:10.1101/2024.01.23.24301643",  # medRxiv, dated
        "DOI:10.21203/rs.3.rs-123456/v1",  # Research Square
        "DOI:10.48550/arXiv.2401.00001",  # arXiv
        "DOI:10.2139/ssrn.1234567",  # SSRN
        "doi:10.1101/2024.01.09.574075",  # case-insensitive prefix
    ],
)
def test_preprint_dois_are_flagged(reference: str) -> None:
    assert _reference_is_preprint(reference) is True


@pytest.mark.parametrize(
    "reference",
    [
        "DOI:10.1101/gad.12345",  # Genes & Development (CSH journal)
        "DOI:10.1101/cshperspect.a015370",  # CSH Perspectives (a real journal)
        "DOI:10.1101/gr.123456.789",  # Genome Research (CSH journal)
        "DOI:10.1001/jama.2022.5368",  # peer-reviewed journal DOI
        "DOI:10.1038/s41586-024-00001-2",  # Nature journal DOI
        None,
        "",
        "not-a-curie",
    ],
)
def test_non_preprint_references_are_not_flagged(reference) -> None:
    # No cache file exists for any of these, so the result rests entirely on the
    # DOI-pattern half; CSH journal DOIs must not be treated as preprints.
    assert _reference_is_preprint(reference) is False
