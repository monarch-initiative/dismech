"""Deep-research reference extraction keeps markdown link syntax out of the ID.

Issue #9514: a report citing ``DOI [10.x/y](https://doi.org/10.x/y)`` recorded
the identifier as ``DOI:10.x/y](https://doi.org/10.x/y``, which cannot resolve,
so ``confabulation_rate`` counted real references as fabricated. About two dozen
such entries still sit in committed reports under ``research/``. The extractor lives
upstream, in ``deep_research_client.validation.extraction``. Of the releases
checked, 0.2.12 is the first that handles every form below: 0.2.10 and 0.2.11
still captured the ``...)](https://...`` tail. ``pyproject.toml`` has required
``>=0.2.12`` since #10167.

Nothing else in this repository records that dependency, so these tests pin the
behaviour: a pin loosened back below 0.2.12, or an upstream regression, would
bring the false "unresolved reference" back with no failing test to name it.
Every input is a citation shape seen in a committed report (issue #9514 lists
where), with the surrounding prose shortened.
"""

from __future__ import annotations

import pytest
from deep_research_client.validation.extraction import extract_references


def _ids(text: str) -> list[str]:
    return [ref.normalized_id for ref in extract_references(text)]


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        pytest.param(
            "DOI [10.1007/s00439-016-1756-5](https://doi.org/10.1007/s00439-016-1756-5)",
            ["DOI:10.1007/s00439-016-1756-5"],
            id="doi-org-link",
        ),
        pytest.param(
            "[Report, doi:10.1111/cge.14411]"
            "(https://onlinelibrary.wiley.com/doi/full/10.1111/cge.14411)",
            ["DOI:10.1111/cge.14411"],
            id="publisher-landing-page",
        ),
        pytest.param(
            "[Report, doi:10.3390/ijms27104455)](https://www.mdpi.com/1422-0067/27/10/4455)",
            ["DOI:10.3390/ijms27104455"],
            id="stray-close-paren-before-bracket",
        ),
        pytest.param(
            "[Preprint, doi:10.1101/2025.04.09.646620]"
            "(https://www.biorxiv.org/content/10.1101/2025.04.09.646620v2)",
            ["DOI:10.1101/2025.04.09.646620"],
            id="versioned-preprint-url",
        ),
        pytest.param(
            "[Report, doi:10.1371/journal.pone.0162111](https://journals.plos.org)",
            ["DOI:10.1371/journal.pone.0162111"],
            id="bare-host-target",
        ),
        pytest.param(
            # The link target is a PMC article, so both identifiers are real.
            "[Report, doi:10.3390/genes17020154)]"
            "(https://pmc.ncbi.nlm.nih.gov/articles/PMC12941242/)",
            ["DOI:10.3390/genes17020154", "PMC:PMC12941242"],
            id="pmc-link-target",
        ),
        pytest.param(
            # A DOI may contain balanced parentheses: do not stop at ")".
            "doi:10.1016/s0022-5347(05)64215-2",
            ["DOI:10.1016/s0022-5347(05)64215-2"],
            id="balanced-parens-in-doi",
        ),
        pytest.param(
            "([PMID: 23712021](https://pubmed.ncbi.nlm.nih.gov/23712021/))",
            ["PMID:23712021"],
            id="pmid-space-after-colon",
        ),
    ],
)
def test_markdown_link_citation_yields_each_identifier_exactly_once(text, expected):
    assert sorted(_ids(text)) == sorted(expected)


def test_one_doi_written_two_ways_is_one_reference():
    """``SLC25A12`` counted one DOI twice, once with a stray ``)`` (issue #9514)."""
    text = (
        "[A](https://www.mdpi.com/1422-0067/27/10/4455) "
        "[Report, doi:10.3390/ijms27104455](https://www.mdpi.com/1422-0067/27/10/4455) "
        "[Report, doi:10.3390/ijms27104455)](https://www.mdpi.com/1422-0067/27/10/4455)"
    )
    assert _ids(text) == ["DOI:10.3390/ijms27104455"]


def test_no_extracted_identifier_contains_link_syntax():
    text = (
        "DOI [10.1007/s00439-016-1756-5](https://doi.org/10.1007/s00439-016-1756-5)\n"
        "[x, doi:10.3390/ijms27104455)](https://www.mdpi.com/1422-0067/27/10/4455)\n"
        "([PMID: 23712021](https://pubmed.ncbi.nlm.nih.gov/23712021/))"
    )
    for identifier in _ids(text):
        assert not any(ch in identifier for ch in "[]") and "://" not in identifier


@pytest.mark.xfail(
    strict=True,
    reason=(
        "deep-research-client 0.2.12 de-duplicates DOIs case-sensitively, so one "
        "DOI written in two cases is two references. DOIs are case-insensitive. "
        "Remove this marker when upstream folds case."
    ),
)
def test_a_doi_and_its_lowercased_link_target_are_one_reference():
    """``Caroli_Disease``'s falcon report links ``JCTH`` to a lowercased doi.org URL.

    The link syntax no longer leaks into the identifier, but the two spellings
    are still counted separately, which inflates ``total_references``. Across
    the committed reports in ``research/`` this affects hundreds of them.
    """
    text = (
        "[Caroli review, doi:10.14218/JCTH.2024.00119]"
        "(https://doi.org/10.14218/jcth.2024.00119)"
    )
    assert [i.lower() for i in _ids(text)] == ["doi:10.14218/jcth.2024.00119"]
