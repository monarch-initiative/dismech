"""GeneReviews chapters whose cached abstract is a statement of purpose (#11848).

An Overview-format GeneReviews chapter's PubMed abstract says what the chapter
will do and lists no clinical characteristics, so it cannot be the phenotype
baseline ``initiate-new-disorder-creation`` asks for. These tests cover the
detector in :mod:`dismech.bookshelf` and the fetch-time warning in
:mod:`dismech.reference_cache_frontmatter`, against synthetic cache files and a
synthetic index. One test reads the committed cache to pin the case the issue
was filed with.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from dismech.bookshelf import (
    BookshelfIndex,
    Chapter,
    is_purpose_only_chapter,
    is_purpose_statement_only,
)
from dismech.reference_cache_frontmatter import (
    genereviews_baseline_warnings,
    main_fetch_warning,
)

ROOT = Path(__file__).resolve().parents[1]

CITATION = (
    "In: Adam MP, Bick S, Mirzaa GM, Pagon RA, Wallace SE, Amemiya A, editors.\n"
    "GeneReviews(®) [Internet]. Seattle (WA): University of Washington, Seattle;\n"
    "1993–2026.\n"
)
PURPOSE = (
    "The purpose of this overview is to: 1.. Describe the clinical characteristics of\n"
    "arrhythmogenic right ventricular cardiomyopathy (ARVC); 2.. Review the genetic\n"
    "causes of ARVC; 3.. Provide an evaluation strategy.\n"
)
STRUCTURED = (
    "CLINICAL CHARACTERISTICS: Marfan syndrome is a systemic disorder of\n"
    "connective tissue with a high degree of clinical variability.\n"
    "DIAGNOSIS/TESTING: The diagnosis is established by clinical criteria.\n"
)


def _cache(cache_dir: Path, pmid: str, body: str) -> Path:
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / f"PMID_{pmid}.md"
    path.write_text(
        "---\n"
        f"reference_id: PMID:{pmid}\n"
        "title: A chapter.\n"
        "year: '1993'\n"
        "content_type: abstract_only\n"
        "---\n\n"
        "# A chapter.\n\n## Content\n\n" + body,
        encoding="utf-8",
    )
    return path


@pytest.fixture
def index() -> BookshelfIndex:
    idx = BookshelfIndex()
    for chapter in [
        Chapter(
            "genereviews",
            "20301310",
            "NBK1131",
            "Arrhythmogenic Right Ventricular Cardiomyopathy Overview.",
            False,
        ),
        Chapter(
            "genereviews", "20301510", "NBK1335", "FBN1-Related Marfan Syndrome.", False
        ),
        Chapter(
            "genereviews",
            "20301507",
            "NBK1332",
            "Congenital Disorders of N-Linked Glycosylation and Multiple Pathway "
            "Overview – RETIRED CHAPTER, FOR HISTORICAL REFERENCE ONLY.",
            True,
        ),
        Chapter(
            "genereviews",
            "20301582",
            "NBK1408",
            "Limb-Girdle Muscular Dystrophy Overview – RETIRED CHAPTER, FOR "
            "HISTORICAL REFERENCE ONLY.",
            True,
        ),
        Chapter(
            "statpearls", "30855785", "NBK538197", "Dandy-Walker Malformation.", False
        ),
    ]:
        idx.add(chapter)
    return idx


# -- the detector -------------------------------------------------------------


@pytest.mark.parametrize(
    "text",
    [
        PURPOSE,
        CITATION + PURPOSE,
        # The wording varies across chapters.
        "The purpose of this GeneReview is to: 1.. Describe the audiometric aspects",
        (
            "The goals of this overview on hereditary hyperekplexia (HPX) caused by "
            "dysfunction of glycinergic inhibitory transmission is to: 1.. Describe"
        ),
        # PubMed wraps the abstract at arbitrary points.
        "The purpose of this\noverview is to: 1.. Briefly describe",
    ],
)
def test_purpose_statement_abstracts_are_detected(text):
    assert is_purpose_statement_only(text)


@pytest.mark.parametrize(
    "text",
    [
        STRUCTURED,
        CITATION + STRUCTURED,
        # An older Overview with a structured abstract is a usable baseline,
        # whatever its title says (the retired LGMD Overview is one).
        PURPOSE + STRUCTURED,
        # A journal article that merely uses the word.
        "The purpose of this study was to compare two treatments.",
        "",
    ],
)
def test_structured_or_unrelated_abstracts_are_not(text):
    assert not is_purpose_statement_only(text)


def test_uncached_chapter_claims_nothing(tmp_path):
    assert not is_purpose_only_chapter(tmp_path, "20301310")


def test_frontmatter_is_not_read_as_abstract(tmp_path):
    """A title in the frontmatter that happens to match is not the abstract."""
    _cache(tmp_path, "1", STRUCTURED)
    path = tmp_path / "PMID_1.md"
    path.write_text(
        path.read_text().replace(
            "title: A chapter.", f"title: {PURPOSE.splitlines()[0]}"
        )
    )
    assert not is_purpose_only_chapter(tmp_path, "1")


def test_committed_arvc_overview_is_purpose_only():
    """The instance #11848 was filed with, read from the committed cache."""
    cache = ROOT / "references_cache"
    if not (cache / "PMID_20301310.md").exists():
        pytest.skip("ARVC Overview not cached")
    assert is_purpose_only_chapter(cache, "20301310")


# -- fetch-time warnings --------------------------------------------------------


def test_overview_chapter_warns_at_fetch(tmp_path, index):
    _cache(tmp_path, "20301310", CITATION + PURPOSE)
    (warning,) = genereviews_baseline_warnings("PMID:20301310", tmp_path, index)
    assert warning.startswith("WARNING: PMID:20301310 is a GeneReviews chapter")
    assert "Arrhythmogenic Right Ventricular Cardiomyopathy Overview." in warning
    assert "cannot serve as the phenotype" in warning
    assert "#11848" in warning


def test_structured_chapter_is_silent(tmp_path, index):
    _cache(tmp_path, "20301510", CITATION + STRUCTURED)
    assert genereviews_baseline_warnings("PMID:20301510", tmp_path, index) == []


def test_retired_overview_gets_both_warnings(tmp_path, index):
    _cache(tmp_path, "20301507", CITATION + PURPOSE)
    warnings = genereviews_baseline_warnings("20301507", tmp_path, index)
    assert len(warnings) == 2
    assert "Overview format" in warnings[0]
    assert "retired GeneReviews chapter" in warnings[1]


def test_retired_chapter_with_structured_abstract_warns_only_retired(tmp_path, index):
    _cache(tmp_path, "20301582", CITATION + STRUCTURED)
    (warning,) = genereviews_baseline_warnings("PMID:20301582", tmp_path, index)
    assert "retired GeneReviews chapter" in warning


def test_chapter_newer_than_snapshot_is_recognised_by_its_citation(tmp_path, index):
    _cache(tmp_path, "41000000", CITATION + PURPOSE)
    (warning,) = genereviews_baseline_warnings("PMID:41000000", tmp_path, index)
    assert "Title:" not in warning  # nothing to name it by


@pytest.mark.parametrize(
    ("reference", "body"),
    [
        # A journal article that reads like a purpose statement.
        ("PMID:12345678", PURPOSE),
        # A StatPearls chapter is never a baseline in the first place.
        ("PMID:30855785", PURPOSE),
        # Not a PMID.
        ("DOI:10.1/x", PURPOSE),
    ],
)
def test_non_genereviews_records_are_silent(tmp_path, index, reference, body):
    if reference.startswith("PMID:"):
        _cache(tmp_path, reference.split(":")[1], body)
    assert genereviews_baseline_warnings(reference, tmp_path, index) == []


def test_fetch_warning_cli_prints_to_stderr_and_exits_zero(tmp_path, capsys):
    """The CLI the validator wrapper calls, against the committed index."""
    _cache(tmp_path, "20301310", CITATION + PURPOSE)
    assert main_fetch_warning(["PMID:20301310", "--cache-dir", str(tmp_path)]) == 0
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "Overview format" in captured.err
