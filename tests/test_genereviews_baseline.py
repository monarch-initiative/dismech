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
import json
import sys
import types
from pathlib import Path
from typing import ClassVar

import pytest

from dismech.bookshelf import (
    DEFAULT_INDEX_DIR,
    MATCH_KINDS,
    SOURCE_TAGS,
    BookshelfIndex,
    Chapter,
    Match,
    entry_genes,
    entry_names,
    kind_rank,
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
        _chapter(
            "genereviews", "26925472", "NBK344340", "17q12 Recurrent Duplication."
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
    doc: dict = {"name": name}
    if synonyms:
        doc["synonyms"] = list(synonyms)
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


def _write_index(tmp_path: Path, index: BookshelfIndex) -> Path:
    index_dir = tmp_path / "index"
    index_dir.mkdir()
    for source in SOURCE_TAGS:
        rows = [r.chapter for r in index.rows if r.chapter.source == source]
        with (index_dir / f"{source}.csv").open("w", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["pmid", "nbk", "retired", "pubdate", "title"])
            for c in rows:
                writer.writerow([c.pmid, c.nbk, "1" if c.retired else "0", "", c.title])
    return index_dir


def test_strict_exit_code_and_formats(tmp_path, index, monkeypatch, capsys):
    index_dir = _write_index(tmp_path, index)
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


# -- live PubMed supplement (#14133) -------------------------------------------


def test_match_kinds_share_one_ordering():
    """``Match.rank`` and the report's row sort use one scale, ``""`` last."""
    chapter = _chapter("genereviews", "1", "NBK1", "X.")
    ranks = [Match(chapter, kind, "x").rank for kind in MATCH_KINDS]
    assert ranks == [kind_rank(kind) for kind in MATCH_KINDS] == sorted(ranks)
    assert MATCH_KINDS[0] == "EXACT" and MATCH_KINDS[-1] == "ONLINE"
    assert kind_rank("") > max(ranks)


class _FakeNcbiClient:
    """Stands in for ``build_bookshelf_index.NcbiClient``: one chapter, no network."""

    PMID = "99999999"  # deliberately absent from the fixture index
    calls: ClassVar[list[tuple[str, dict]]] = []

    def __init__(self, api_key=None):
        pass

    def call(self, endpoint: str, **params: str) -> dict:
        self.calls.append((endpoint, params))
        if endpoint == "esearch.fcgi":
            hit = params["term"] == '"DNASE2 Deficiency"[TI] AND genereviews[book]'
            return {"esearchresult": {"idlist": [self.PMID] if hit else []}}
        assert endpoint == "esummary.fcgi" and params["id"] == self.PMID
        return {
            "result": {
                self.PMID: {
                    "title": "DNASE2 Deficiency.",
                    "articleids": [{"idtype": "bookaccession", "value": "NBK999999"}],
                }
            }
        }


def test_online_hit_missing_from_index_returns_a_verdict(
    tmp_path, index, monkeypatch, capsys
):
    """``--online`` used to crash with ``ValueError`` on any live hit (#14133)."""
    fake = types.ModuleType("build_bookshelf_index")
    fake.NcbiClient = _FakeNcbiClient
    monkeypatch.setitem(sys.modules, "build_bookshelf_index", fake)
    monkeypatch.setattr(_FakeNcbiClient, "calls", [])
    assert _FakeNcbiClient.PMID not in index.by_pmid

    index_dir = _write_index(tmp_path, index)
    entry = tmp_path / "DNASE2_Deficiency.yaml"
    entry.write_text("name: DNASE2 Deficiency\nsynonyms:\n- DNase II deficiency\n")
    args = [
        str(entry),
        "--index-dir",
        str(index_dir),
        "--cache-dir",
        str(tmp_path / "cache"),
        "--online",
    ]

    assert cgb.main(args + ["--format", "json"]) == 0
    (report,) = json.loads(capsys.readouterr().out)
    gr = report["sources"]["genereviews"]
    assert gr["verdict"] == "CANDIDATE_CHAPTER"
    (row,) = gr["chapters"]
    assert (row["pmid"], row["nbk"], row["kind"]) == (
        _FakeNcbiClient.PMID,
        "NBK999999",
        "ONLINE",
    )
    assert report["sources"]["statpearls"]["verdict"] == "NO_CHAPTER"
    assert any(endpoint == "esummary.fcgi" for endpoint, _ in _FakeNcbiClient.calls)

    # A live hit is a candidate for a person to read, never a gate.
    assert cgb.main(args + ["--strict"]) == 0
    out = capsys.readouterr().out
    assert f"PMID:{_FakeNcbiClient.PMID} NBK999999" in out and "ONLINE via" in out


class _RecordingNcbiClient:
    """Records each esearch ``term`` and answers with a canned ``esearchresult``."""

    def __init__(self, esearch: dict):
        self.esearch = esearch
        self.terms: list[str] = []

    def call(self, endpoint: str, **params: str) -> dict:
        assert endpoint == "esearch.fcgi", "no hit, so esummary is never called"
        self.terms.append(params["term"])
        return {"esearchresult": self.esearch}


def _online(index, client) -> cgb.OnlineSearch:
    online = cgb.OnlineSearch.__new__(cgb.OnlineSearch)
    online.client, online.index, online.sources = client, index, ["genereviews"]
    return online


def test_online_search_quotes_the_name_as_a_phrase(index):
    """Unquoted, PubMed searched ``mesiodens-cataract syndrome[TI]`` as "syndrome" (#14213)."""
    client = _RecordingNcbiClient({"idlist": []})
    online = _online(index, client)
    assert online.search(["mesiodens-cataract syndrome", 'a "quoted" name', '""']) == []
    assert client.terms == [
        '"mesiodens-cataract syndrome"[TI] AND genereviews[book]',
        '"a quoted name"[TI] AND genereviews[book]',
    ]


def test_online_search_skips_a_rewritten_query(index, capsys):
    client = _RecordingNcbiClient(
        {
            "idlist": ["99999997"],
            "querytranslation": '"syndrome"[Title] AND "genereviews"[Book]',
        }
    )
    assert _online(index, client).search(["mesiodens-cataract syndrome"]) == []
    assert "PubMed rewrote" in capsys.readouterr().err


def test_online_hit_ranks_after_index_title_matches(tmp_path, index):
    class _Online:
        def search(self, names):
            chapter = _chapter("genereviews", "99999998", "", "Usher Syndrome.")
            return [Match(chapter, "ONLINE", "Usher Syndrome")]

    path = tmp_path / "Usher_Syndrome.yaml"
    path.write_text("name: Usher Syndrome\n")
    report = cgb.assess_entry(
        path,
        _entry("Usher Syndrome"),
        path.read_text(),
        index,
        cache_dir=tmp_path / "cache",
        online=_Online(),
        rel_to=tmp_path,
    )
    gr = report.sources["genereviews"]
    assert [(r.pmid, r.kind) for r in gr.chapters] == [
        ("20301442", "CONTAINS"),
        ("99999998", "ONLINE"),
    ]
    assert gr.verdict == "CANDIDATE_CHAPTER"


# -- "<Disease> – <GENE>" titles (#15904) ---------------------------------------


@pytest.fixture
def gene_index() -> BookshelfIndex:
    """The real shapes: three ADTKD chapters split by gene, plus two decoys."""
    idx = BookshelfIndex()
    for chapter in [
        _chapter(
            "genereviews",
            "20301530",
            "NBK1356",
            "Autosomal Dominant Tubulointerstitial Kidney Disease – UMOD.",
        ),
        _chapter(
            "genereviews",
            "21473025",
            "NBK53700",
            "Autosomal Dominant Tubulointerstitial Kidney Disease – REN.",
        ),
        _chapter(
            "genereviews",
            "23946964",
            "NBK153723",
            "Autosomal Dominant Tubulointerstitial Kidney Disease – MUC1.",
        ),
        _chapter(
            "genereviews",
            "20301659",
            "NBK1486",
            "Pyridoxine-Dependent Epilepsy – ALDH7A1.",
        ),
        # A spaced dash followed by words, not a gene symbol.
        _chapter(
            "genereviews",
            "20301498",
            "NBK1323",
            "Udd Distal Myopathy – Tibial Muscular Dystrophy.",
        ),
    ]:
        idx.add(chapter)
    return idx


def _adtkd_ren() -> dict:
    """The entry from #15904, with the shape PR #15905 gives it."""
    doc = _entry(
        "Familial Juvenile Hyperuricemic Nephropathy Type 2",
        [
            "ADTKD-REN",
            "FJHN type 2",
            "REN-associated kidney disease",
            "autosomal dominant tubulointerstitial kidney disease due to mutations in REN",
        ],
        label="familial juvenile hyperuricemic nephropathy type 2",
    )
    return doc


def test_gene_suffix_title_is_a_candidate_for_its_own_gene(tmp_path, gene_index):
    report = _assess(tmp_path, gene_index, _adtkd_ren())
    gr = report.sources["genereviews"]
    # A candidate, never an exact match, so --strict does not start failing on it.
    assert gr.verdict == "CANDIDATE_CHAPTER"
    assert [(r.pmid, r.nbk, r.kind) for r in gr.chapters] == [
        ("21473025", "NBK53700", "GENE_SUFFIX")
    ]
    assert not report.gating


def test_gene_suffix_chapters_do_not_cross_match_by_gene(gene_index):
    for gene, pmid in [("UMOD", "20301530"), ("REN", "21473025"), ("MUC1", "23946964")]:
        name = f"autosomal dominant tubulointerstitial kidney disease due to {gene} variants"
        assert [(m.kind, m.chapter.pmid) for m in gene_index.match(name)] == [
            ("GENE_SUFFIX", pmid)
        ]


def test_gene_suffix_gene_may_come_from_elsewhere_in_the_entry(tmp_path, gene_index):
    name = "Autosomal Dominant Tubulointerstitial Kidney Disease, Renin Type"
    assert gene_index.match(name) == []  # "renin" is not the symbol REN
    doc = _entry(name)
    doc["genetic"] = [
        {
            "name": "REN variants",
            "gene_term": {
                "preferred_term": "REN",
                "term": {"id": "hgnc:9958", "label": "REN"},
            },
        }
    ]
    assert entry_genes(doc) == ["REN variants", "REN"]
    gr = _assess(tmp_path, gene_index, doc).sources["genereviews"]
    assert [(r.pmid, r.kind) for r in gr.chapters] == [("21473025", "GENE_SUFFIX")]


def test_bare_family_entry_is_at_most_a_candidate(tmp_path, gene_index):
    report = _assess(
        tmp_path,
        gene_index,
        _entry("Autosomal Dominant Tubulointerstitial Kidney Disease", ["ADTKD"]),
    )
    gr = report.sources["genereviews"]
    assert gr.verdict == "CANDIDATE_CHAPTER"
    # No gene in the entry, so none of the three is singled out.
    assert {r.kind for r in gr.chapters} == {"CONTAINS"}
    assert len(gr.chapters) == 3


def test_pyridoxine_dependent_epilepsy_keeps_its_exact_match(tmp_path, gene_index):
    doc = _entry(
        "Pyridoxine-Dependent Epilepsy",
        ["pyridoxine-dependent epilepsy (ALDH7A1)"],
    )
    gr = _assess(tmp_path, gene_index, doc).sources["genereviews"]
    assert gr.verdict == "UNTAGGED_CHAPTER"
    assert [(r.pmid, r.kind) for r in gr.chapters] == [("20301659", "EXACT")]


def test_unrelated_entry_stays_no_chapter(tmp_path, gene_index):
    doc = _entry(
        "SEC61A1 Deficiency",
        ["autosomal dominant tubulointerstitial kidney disease due to SEC61A1"],
    )
    gr = _assess(tmp_path, gene_index, doc).sources["genereviews"]
    assert gr.verdict == "NO_CHAPTER"


def test_a_worded_suffix_is_not_read_as_a_gene(gene_index):
    assert (
        gene_index.match("Udd distal myopathy with Tibial Muscular Dystrophy features")
        == []
    )


def test_committed_index_reads_the_gene_suffix_titles():
    idx = BookshelfIndex.load(DEFAULT_INDEX_DIR, sources=["genereviews"])
    suffixed = {
        idx.rows[i].chapter.pmid: idx.rows[i].suffix_gene for i in idx._gene_suffixed
    }
    for pmid, gene in [
        ("20301530", "umod"),
        ("21473025", "ren"),
        ("23946964", "muc1"),
        ("20301659", "aldh7a1"),
    ]:
        assert suffixed.get(pmid) == gene
    # "Udd Distal Myopathy – Tibial Muscular Dystrophy" carries no gene.
    assert "20301498" not in suffixed


# -- entries with no synonyms (#12075) ----------------------------------------


def test_synonymless_no_chapter_is_unproven_and_says_what_was_searched(tmp_path, index):
    # The chapter is titled by a synonym the draft does not carry yet.
    report = _assess(tmp_path, index, _entry("Chromosome 17q12 Duplication Syndrome"))
    assert report.synonymless
    assert report.sources["genereviews"].verdict == "NO_CHAPTER"
    assert report.unproven("genereviews")
    assert report.gating and report.has_unproven and not report.noteworthy
    text = "\n".join(cgb.format_text(report, show_all=False))
    assert "note: entry has no synonyms" in text
    assert "'Chromosome 17q12 Duplication Syndrome'" in text

    # With the synonym the same chapter is an exact match.
    report = _assess(
        tmp_path,
        index,
        _entry(
            "Chromosome 17q12 Duplication Syndrome", ["17q12 recurrent duplication"]
        ),
    )
    assert not report.synonymless
    gr = report.sources["genereviews"]
    assert gr.verdict == "UNTAGGED_CHAPTER" and gr.chapters[0].pmid == "26925472"
    assert not report.unproven("genereviews")


def test_no_chapter_with_synonyms_stays_clean(tmp_path, index):
    report = _assess(
        tmp_path, index, _entry("Dandy-Walker Syndrome", ["Dandy-Walker malformation"])
    )
    assert report.sources["genereviews"].verdict == "NO_CHAPTER"
    assert not report.unproven("genereviews")
    assert not report.gating
    text = "\n".join(cgb.format_text(report, show_all=True))
    assert "note:" not in text


@pytest.mark.parametrize("synonyms", [None, [""], ["   "]])
def test_absent_or_blank_synonyms_count_as_none(tmp_path, index, synonyms):
    doc = _entry("Chromosome 17q12 Duplication Syndrome")
    if synonyms is not None:
        doc["synonyms"] = synonyms
    report = _assess(tmp_path, index, doc)
    assert report.synonymless and report.unproven("genereviews")
    assert not report.no_synonyms_recorded


def test_explicit_empty_synonyms_records_that_none_exist(tmp_path, index):
    doc = _entry("Chromosome 17q12 Duplication Syndrome")
    doc["synonyms"] = []
    report = _assess(tmp_path, index, doc)
    assert report.synonymless and report.no_synonyms_recorded
    assert report.sources["genereviews"].verdict == "NO_CHAPTER"
    assert not report.unproven("genereviews")
    assert not report.gating


def test_synonymless_candidate_is_noted_but_does_not_gate(tmp_path, index):
    report = _assess(tmp_path, index, _entry("Alpha Thalassemia"))
    assert report.sources["genereviews"].verdict == "CANDIDATE_CHAPTER"
    assert report.unproven("genereviews")
    assert not report.gating
    assert "note: entry has no synonyms" in "\n".join(
        cgb.format_text(report, show_all=False)
    )


def test_statpearls_unproven_never_gates(tmp_path, index):
    # Nothing in either collection names this entry, and it has no synonyms.
    report = _assess(tmp_path, index, _entry("Imaginary Syndrome"))
    assert report.unproven("statpearls") and report.unproven("genereviews")
    report.sources["genereviews"].verdict = "TAGGED"  # isolate the StatPearls side
    assert not report.gating


def test_strict_fails_on_synonymless_no_chapter(tmp_path, index, monkeypatch, capsys):
    index_dir = tmp_path / "index"
    index_dir.mkdir()
    for source in SOURCE_TAGS:
        rows = [r.chapter for r in index.rows if r.chapter.source == source]
        with (index_dir / f"{source}.csv").open("w", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["pmid", "nbk", "retired", "pubdate", "title"])
            for c in rows:
                writer.writerow([c.pmid, c.nbk, "1" if c.retired else "0", "", c.title])
    entry = tmp_path / "Draft.yaml"
    entry.write_text("name: Chromosome 17q12 Duplication Syndrome\n")
    args = [
        str(entry),
        "--index-dir",
        str(index_dir),
        "--cache-dir",
        str(tmp_path / "cache"),
    ]
    assert cgb.main(args) == 0
    out = capsys.readouterr().out
    assert "note: entry has no synonyms" in out
    assert "1 NO_CHAPTER/CANDIDATE_CHAPTER verdicts above are from" in out
    assert "is not a\nverified negative" in out
    assert cgb.main(args + ["--strict"]) == 1
    capsys.readouterr()
    assert cgb.main(args + ["--format", "json"]) == 0
    assert '"synonymless": true' in capsys.readouterr().out

    # A whole-KB --strict run names the entries it fails on.
    monkeypatch.setattr(cgb, "iter_targets", lambda paths: [entry])
    assert cgb.main(args[1:] + ["--strict"]) == 1
    out = capsys.readouterr().out
    assert "note: entry has no synonyms" in out and "`--all` lists" not in out
    assert cgb.main(args[1:]) == 0
    assert "`--all` lists those entries" in capsys.readouterr().out

    entry.write_text("name: Chromosome 17q12 Duplication Syndrome\nsynonyms: []\n")
    assert cgb.main(args + ["--strict", "--source", "genereviews"]) == 0
    assert "no synonyms;" not in capsys.readouterr().out

    entry.write_text(
        "name: Dandy-Walker Syndrome\nsynonyms:\n- Dandy-Walker malformation\n"
    )
    assert cgb.main(args + ["--strict", "--source", "genereviews"]) == 0
    assert "no synonyms" not in capsys.readouterr().out


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
