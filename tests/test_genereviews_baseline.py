"""Semi-deterministic GeneReviews / StatPearls baseline check.

Exercises :mod:`dismech.bookshelf` and ``scripts/check_genereviews_baseline.py``
against a tiny synthetic Bookshelf index and synthetic entries, so no network,
no real cache and no whole-KB walk is involved. The committed index itself is
checked only structurally (well-formed, sorted, both collections present).

See PR #11592, where the automated reviewer could not verify a "no GeneReviews
chapter exists" note because its sandbox blocks every network tool.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pytest

from dismech.bookshelf import (
    DEFAULT_INDEX_DIR,
    SOURCE_TAGS,
    BookshelfIndex,
    Chapter,
    entry_names,
    normalize,
    source_from_cache_text,
)
from scripts import check_genereviews_baseline as cgb

ROOT = Path(__file__).resolve().parents[1]


# -- fixtures -----------------------------------------------------------------


def _chapter(
    source: str, pmid: str, nbk: str, title: str, retired: bool = False
) -> Chapter:
    return Chapter(source=source, pmid=pmid, nbk=nbk, title=title, retired=retired)


@pytest.fixture
def index() -> BookshelfIndex:
    idx = BookshelfIndex()
    for chapter in [
        _chapter("genereviews", "20301510", "NBK1335", "FBN1-Related Marfan Syndrome."),
        _chapter("genereviews", "20301648", "NBK1475", "Aicardi-Goutières Syndrome."),
        _chapter("genereviews", "20301442", "NBK1265", "Usher Syndrome Type I."),
        _chapter(
            "genereviews",
            "25577943",
            "NBK268648",
            "Autosomal Dominant Robinow Syndrome.",
        ),
        _chapter(
            "genereviews",
            "20301622",
            "NBK1449",
            "Alpha-Thalassemia X-Linked Intellectual Disability Syndrome.",
        ),
        _chapter(
            "genereviews",
            "20301370",
            "NBK1191",
            "1p36 Deletion Syndrome – RETIRED CHAPTER, FOR HISTORICAL REFERENCE ONLY.",
            retired=True,
        ),
        _chapter(
            "genereviews", "27308687", "NBK367946", "Maternal 15q Duplication Syndrome."
        ),
        _chapter("genereviews", "20301340", "NBK1161", "Alzheimer Disease Overview."),
        _chapter(
            "genereviews",
            "11111111",
            "NBK11111",
            "ATN1-Related Neurodevelopmental Disorder.",
        ),
        _chapter("statpearls", "30855785", "NBK538197", "Dandy-Walker Malformation."),
        _chapter("statpearls", "30726024", "NBK537339", "Marfan Syndrome."),
    ]:
        idx.add(chapter)
    idx.snapshot_date = "2026-09-10"
    return idx


def _entry(
    name: str,
    synonyms: list[str] = (),
    label: str | None = None,
    references: list[dict] = (),
) -> dict:
    doc: dict = {"name": name, "synonyms": list(synonyms)}
    doc["disease_term"] = {
        "preferred_term": label or name,
        "term": {"id": "MONDO:0000001", "label": label or name},
    }
    if references:
        doc["references"] = list(references)
    return doc


def _assess(
    tmp_path: Path, index: BookshelfIndex, doc: dict, text: str = ""
) -> cgb.EntryReport:
    path = tmp_path / "Entry.yaml"
    path.write_text(text or f"name: {doc['name']}\n", encoding="utf-8")
    return cgb.assess_entry(
        path,
        doc,
        path.read_text(),
        index,
        cache_dir=tmp_path / "cache",
        rel_to=tmp_path,
    )


# -- normalisation and matching ----------------------------------------------


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("Aicardi-Goutières Syndrome.", "aicardi goutieres syndrome"),
        ("GeneReviews(®) Marfan", "genereviews marfan"),
        ("Alzheimer Disease Overview", "alzheimer disease"),
        ("22q11.2 Deletion Syndrome", "22q11 2 deletion syndrome"),
    ],
)
def test_normalize(raw, expected):
    assert normalize(raw) == expected


def test_exact_match_ignores_gene_prefix_diacritics_and_overview(index):
    assert [
        (m.kind, m.chapter.pmid)
        for m in index.match("Marfan Syndrome", sources=["genereviews"])
    ] == [("EXACT", "20301510")]
    assert [m.kind for m in index.match("Aicardi-Goutieres Syndrome")] == ["EXACT"]
    assert [m.kind for m in index.match("Alzheimer Disease")] == ["EXACT"]


def test_both_collections_are_matched_and_distinguished(index):
    matches = index.match("Marfan Syndrome")
    assert {(m.chapter.source, m.kind) for m in matches} == {
        ("genereviews", "EXACT"),
        ("statpearls", "EXACT"),
    }


def test_containment_is_a_candidate_not_an_exact_match(index):
    matches = index.match("Alpha Thalassemia")
    assert [m.kind for m in matches] == ["CONTAINS"]


def test_numbered_subtypes_do_not_borrow_each_others_chapter(index):
    # "Usher Syndrome Type I" is one edit away from "Usher Syndrome Type 4" and is a different disease.
    assert index.match("Usher Syndrome Type 4") == []
    # ...but a subtype-numbered entry may sit under an unnumbered chapter, as a weak candidate.
    kinds = {m.kind for m in index.match("Autosomal Dominant Robinow Syndrome 1")}
    assert kinds and kinds <= {"TITLE_IN_NAME", "NEAR"}


def test_gene_related_forms_must_name_the_same_gene(index):
    assert index.match("ANK2-Related Neurodevelopmental Disorder") == []
    assert [
        m.kind for m in index.match("ATN1-Related Neurodevelopmental Disorder")
    ] == ["EXACT"]


def test_single_token_and_stopword_only_names_never_contain_match(index):
    assert index.match("Syndrome") == []
    assert index.match("Marfan") == []  # one token: exact only, and no exact title


def test_retired_chapter_is_flagged(index):
    (match,) = index.match("1p36 Deletion Syndrome")
    assert match.kind == "EXACT" and match.chapter.retired


def test_source_of_resolves_pmid_and_nbk_url(index):
    assert (
        index.source_of("PMID:27308687").title == "Maternal 15q Duplication Syndrome."
    )
    assert (
        index.source_of("url:https://www.ncbi.nlm.nih.gov/books/NBK367946/").pmid
        == "27308687"
    )
    assert index.source_of("PMID:99999999") is None
    assert (
        index.source_of("url:https://www.ncbi.nlm.nih.gov/books/n/gene/ptdss1-lmhd/")
        is None
    )


def test_cache_marker_is_the_citation_form_not_the_bare_word():
    assert (
        source_from_cache_text("In: GeneReviews(®) [Internet]. Seattle (WA)")
        == "genereviews"
    )
    assert (
        source_from_cache_text("In: StatPearls [Internet]. Treasure Island (FL)")
        == "statpearls"
    )
    # A journal article citing GeneReviews in its reference list is not a chapter.
    assert (
        source_from_cache_text(
            "16. Malm D, Nilssen O: Alpha-Mannosidosis. GeneReviews. Medical"
        )
        is None
    )


def test_entry_names_collects_name_synonyms_and_disease_term():
    doc = _entry(
        "Dandy-Walker Syndrome",
        ["Dandy-Walker malformation", "DWM", ""],
        label="Dandy-Walker syndrome",
    )
    doc["has_subtypes"] = [{"name": "Type 1"}]
    names = entry_names(doc)
    assert names == [
        "Dandy-Walker Syndrome",
        "Dandy-Walker malformation",
        "DWM",
        "Dandy-Walker syndrome",
    ]


# -- verdicts ---------------------------------------------------------------


def test_no_chapter_when_nothing_names_the_entry(tmp_path, index):
    report = _assess(
        tmp_path, index, _entry("Dandy-Walker Syndrome", ["Dandy-Walker malformation"])
    )
    assert report.sources["genereviews"].verdict == "NO_CHAPTER"
    # ...while the StatPearls chapter is reported, and never gates.
    sp = report.sources["statpearls"]
    assert sp.verdict == "UNTAGGED_CHAPTER"
    assert sp.chapters[0].pmid == "30855785" and sp.chapters[0].kind == "EXACT"
    assert not report.gating


def test_untagged_exact_chapter_gates_for_genereviews(tmp_path, index):
    report = _assess(tmp_path, index, _entry("Marfan Syndrome"))
    assert report.sources["genereviews"].verdict == "UNTAGGED_CHAPTER"
    assert report.gating


def test_cited_but_untagged_chapter_by_pmid_and_by_nbk_url(tmp_path, index):
    doc = _entry("Marfan Syndrome")
    report = _assess(
        tmp_path,
        index,
        doc,
        text="name: Marfan Syndrome\nevidence:\n- reference: PMID:20301510\n",
    )
    gr = report.sources["genereviews"]
    assert gr.verdict == "CITED_UNTAGGED" and gr.chapters[0].cited_as == "PMID"

    doc = _entry("Achondroplasia")
    index.add(_chapter("genereviews", "20301331", "NBK1152", "Achondroplasia."))
    report = _assess(
        tmp_path,
        index,
        doc,
        text="name: Achondroplasia\nreferences:\n- reference: url:https://www.ncbi.nlm.nih.gov/books/NBK1152/\n",
    )
    gr = report.sources["genereviews"]
    assert gr.verdict == "CITED_UNTAGGED" and gr.chapters[0].cited_as == "NBK"


def test_tagged_chapter_verified_by_identity_even_when_title_differs(tmp_path, index):
    doc = _entry(
        "15q11q13 Microduplication Syndrome",
        ["Dup15q syndrome"],
        references=[{"reference": "PMID:27308687", "tags": ["GeneReviews"]}],
    )
    report = _assess(tmp_path, index, doc)
    gr = report.sources["genereviews"]
    assert gr.verdict == "TAGGED"
    assert (
        gr.chapters[0].tagged and gr.chapters[0].kind == ""
    )  # found by identity, not by title
    assert not report.gating


def test_tagged_by_nbk_url_counts(tmp_path, index):
    doc = _entry(
        "Maternal 15q Duplication Syndrome",
        references=[
            {
                "reference": "url:https://www.ncbi.nlm.nih.gov/books/NBK367946/",
                "tags": ["GeneReviews"],
            },
        ],
    )
    assert _assess(tmp_path, index, doc).sources["genereviews"].verdict == "TAGGED"


def test_mistagged_journal_article_is_reported(tmp_path, index):
    cache = tmp_path / "cache"
    cache.mkdir()
    (cache / "PMID_18651971.md").write_text(
        "# Alpha-mannosidosis.\n\nOrphanet J Rare Dis. 16. GeneReviews. Medical\n"
    )
    doc = _entry(
        "Alpha-mannosidosis",
        references=[{"reference": "PMID:18651971", "tags": ["GeneReviews"]}],
    )
    report = _assess(tmp_path, index, doc)
    gr = report.sources["genereviews"]
    assert gr.verdict == "MISTAGGED"
    assert gr.tag_problems[0].problem == "MISTAGGED"
    assert report.gating


def test_statpearls_chapter_tagged_genereviews_is_mistagged(tmp_path, index):
    doc = _entry(
        "Marfan Syndrome",
        references=[{"reference": "PMID:30726024", "tags": ["GeneReviews"]}],
    )
    gr = _assess(tmp_path, index, doc).sources["genereviews"]
    assert (
        gr.verdict == "MISTAGGED" and "StatPearls chapter" in gr.tag_problems[0].detail
    )


def test_uncached_unknown_pmid_and_slug_url_are_unverified_not_mistagged(
    tmp_path, index
):
    doc = _entry(
        "Marfan Syndrome",
        references=[
            {"reference": "PMID:88888888", "tags": ["GeneReviews"]},
            {
                "reference": "url:https://www.ncbi.nlm.nih.gov/books/n/gene/ptdss1-lmhd/",
                "tags": ["GeneReviews"],
            },
        ],
    )
    gr = _assess(tmp_path, index, doc).sources["genereviews"]
    assert {p.problem for p in gr.tag_problems} == {"TAGGED_UNVERIFIED"}
    # No verified tag and an exact untagged chapter: still the gap it is.
    assert gr.verdict == "UNTAGGED_CHAPTER"


def test_cached_bookshelf_citation_newer_than_snapshot_is_accepted(tmp_path, index):
    cache = tmp_path / "cache"
    cache.mkdir()
    (cache / "PMID_77777777.md").write_text(
        "# New Chapter.\n\nIn: GeneReviews(®) [Internet]. Seattle (WA)\n"
    )
    doc = _entry(
        "Some New Disease",
        references=[{"reference": "PMID:77777777", "tags": ["GeneReviews"]}],
    )
    assert _assess(tmp_path, index, doc).sources["genereviews"].verdict == "TAGGED"


def test_retired_or_partial_matches_are_candidates_not_gaps(tmp_path, index):
    report = _assess(
        tmp_path,
        index,
        _entry("Chromosome 1p36 Deletion Syndrome", ["1p36 deletion syndrome"]),
    )
    gr = report.sources["genereviews"]
    assert gr.verdict == "CANDIDATE_CHAPTER" and gr.chapters[0].retired
    assert not report.gating
    report = _assess(tmp_path, index, _entry("Alpha Thalassemia"))
    assert report.sources["genereviews"].verdict == "CANDIDATE_CHAPTER"
    assert not report.gating


def test_strict_exit_code_and_formats(tmp_path, index, monkeypatch, capsys):
    index_dir = tmp_path / "index"
    index_dir.mkdir()
    for source in SOURCE_TAGS:
        rows = [r.chapter for r in index.rows if r.chapter.source == source]
        with (index_dir / f"{source}.csv").open("w", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["pmid", "nbk", "retired", "pubdate", "title"])
            for c in rows:
                writer.writerow([c.pmid, c.nbk, "1" if c.retired else "0", "", c.title])
    entry = tmp_path / "Marfan_Syndrome.yaml"
    entry.write_text("name: Marfan Syndrome\n")
    args = [
        str(entry),
        "--index-dir",
        str(index_dir),
        "--cache-dir",
        str(tmp_path / "cache"),
    ]
    assert cgb.main(args) == 0
    assert "UNTAGGED_CHAPTER" in capsys.readouterr().out
    assert cgb.main(args + ["--strict"]) == 1
    capsys.readouterr()
    assert cgb.main(args + ["--format", "tsv"]) == 0
    out = capsys.readouterr().out
    assert out.splitlines()[0].startswith("path\tcollection\tverdict")
    assert cgb.main(args + ["--format", "json"]) == 0


# -- the committed index ----------------------------------------------------


def test_committed_index_is_well_formed():
    idx = BookshelfIndex.load(DEFAULT_INDEX_DIR)
    assert idx.sources == set(SOURCE_TAGS), "both collections must be present"
    assert idx.snapshot_date
    for source in SOURCE_TAGS:
        with (DEFAULT_INDEX_DIR / f"{source}.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            rows = list(csv.DictReader(handle))
        assert rows and rows[0].keys() == {"pmid", "nbk", "retired", "pubdate", "title"}
        pmids = [int(r["pmid"]) for r in rows]
        assert pmids == sorted(pmids) and len(set(pmids)) == len(pmids), (
            f"{source}.csv must be sorted and unique"
        )
        assert all(r["nbk"].startswith("NBK") for r in rows)
        assert all(r["retired"] in {"0", "1"} for r in rows)
    # Sanity: a chapter every curator knows.
    assert idx.source_of("PMID:20301510").title == "FBN1-Related Marfan Syndrome."
