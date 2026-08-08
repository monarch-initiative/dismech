"""Tests for the deep-research evidence backfill importer.

Focus: the bibliographic envelope of a plain-text PubMed/PMC cache body must
never reach an evidence ``snippet``. Issue #8096 found 207 snippets on ``main``
that were journal citation lines ("2000 Aug;83(4):463-6. doi: 10.1054/...") --
text that cannot support or refute the claim it is attached to.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "backfill_deep_research_evidence.py"
SPEC = importlib.util.spec_from_file_location(
    "backfill_deep_research_evidence", SCRIPT_PATH
)
assert SPEC and SPEC.loader
backfill = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = backfill
SPEC.loader.exec_module(backfill)


# A verbatim-shaped PubMed plain-text record: numbered citation line, title,
# byline, affiliation block, abstract, identifier trailer. Modelled on
# references_cache/PMID_10945492.md, the source of one of the 207 bad snippets.
PUBMED_PLAIN_TEXT = """---
reference_id: "PMID:10945492"
title: The rate of the founder Jewish mutations in BRCA1 and BRCA2 in prostate cancer patients in Israel.
journal: Br J Cancer
year: '2000'
---

# The rate of the founder Jewish mutations in BRCA1 and BRCA2 in prostate cancer patients in Israel.

## Content

1. Br J Cancer. 2000 Aug;83(4):463-6. doi: 10.1054/bjoc.2000.1249.

The rate of the founder Jewish mutations in BRCA1 and BRCA2 in prostate cancer
patients in Israel.

Vazina A(1), Baniel J, Yaacobi Y, Shtriker A, Engelstein D, Leibovitz I, Zehavi
M, Sidi AA, Ramon Y, Tischler T, Livne PM, Friedman E.

Author information:
(1)Institute of Urology Rabin Medical Center, Petach Tikvah, Israel.
Second affiliation line with no marker of its own, Tel Aviv, Israel.

Inherited predisposition occurs in 5-10% of all prostate cancer (CaP) patients,
but the genes involved in conferring genetic susceptibility remain largely
unknown.

DOI: 10.1054/bjoc.2000.1249
PMCID: PMC2374645
PMID: 10945492 [Indexed for MEDLINE]
"""

TITLE = (
    "The rate of the founder Jewish mutations in BRCA1 and BRCA2 in prostate "
    "cancer patients in Israel."
)


def write_cache(tmp_path: Path, body: str, name: str = "PMID_10945492.md") -> Path:
    path = tmp_path / name
    path.write_text(body, encoding="utf-8")
    return path


def test_supporting_text_is_the_claim_not_the_citation_line(tmp_path: Path) -> None:
    cache_path = write_cache(tmp_path, PUBMED_PLAIN_TEXT)

    supporting_text = backfill.extract_supporting_text(cache_path, TITLE)

    assert supporting_text is not None
    assert supporting_text.startswith("Inherited predisposition occurs in 5-10%")
    assert "doi:" not in supporting_text.lower()
    assert "Vazina" not in supporting_text
    assert "Institute of Urology" not in supporting_text


def test_citation_line_is_recognised_as_bibliographic() -> None:
    citation_lines = [
        "2000 Aug;83(4):463-6. doi: 10.1054/bjoc.2000.1249.",
        "2016 Aug 9;7:12451. doi: 10.1038/ncomms12451.",
        "2022 Jan 10;16:143-154. doi: 10.2147/DDDT.S219433. eCollection 2022.",
        "DOI: 10.1054/bjoc.2000.1249 PMCID: PMC2374645 PMID: 10945492",
    ]

    for line in citation_lines:
        assert backfill.is_bibliographic(line), line


def test_author_list_and_affiliation_are_recognised_as_bibliographic() -> None:
    assert backfill.is_bibliographic(
        "Vazina A(1), Baniel J, Yaacobi Y, Shtriker A, Engelstein D, Leibovitz I."
    )
    # Non-ASCII surnames still parse as a byline.
    assert backfill.is_bibliographic(
        "Żok J(1), Bieńkowski M(2), Radecka B(3), Kuchar A(1), Borowiec S(1), "
        "Jakieła-Drąg A(7), Gełej M(3), Zając P(3), Duchnowska R(1)."
    )
    assert backfill.is_bibliographic(
        "(2)Massachusetts General Hospital Cancer Center, Boston, Massachusetts."
    )
    assert backfill.is_bibliographic(
        "Treasure Island (FL): StatPearls Publishing; 2026 Jan–."
    )


def test_bare_doi_pointer_is_bibliographic_but_a_citing_sentence_is_not() -> None:
    assert backfill.is_bibliographic(
        "Dataset use reported in doi: 10.1371/journal.pntd.0006621."
    )
    assert not backfill.is_bibliographic(
        "Sustained ingestion of contaminated groundwater establishes the systemic "
        "arsenic burden, and all sequencing data are deposited at "
        "doi: 10.5281/zenodo.1."
    )


def test_prose_listing_people_is_not_mistaken_for_a_byline() -> None:
    prose = (
        "Patients were recruited in Boston, Massachusetts, and in Turin, Italy, "
        "between 2003 and 2009."
    )

    assert not backfill.is_bibliographic(prose)
    assert not backfill.looks_like_author_list(prose)


def test_abstract_mentioning_a_doi_is_kept(tmp_path: Path) -> None:
    """A DOI *inside* prose must not cost us the whole paragraph."""
    body = """---
reference_id: "PMID:1"
title: Data availability study.
---

## Content

1. J Test. 2020 Jan;1(1):1-2. doi: 10.1000/test.

Data availability study.

Smith A(1), Jones B(2).

Sustained ingestion of contaminated groundwater establishes the systemic
arsenic burden, and all sequencing data are deposited at doi: 10.5281/zenodo.1.
"""
    cache_path = write_cache(tmp_path, body, name="PMID_1.md")

    supporting_text = backfill.extract_supporting_text(
        cache_path, "Data availability study."
    )

    assert supporting_text is not None
    assert supporting_text.startswith("Sustained ingestion of contaminated")


def test_numbered_structured_abstract_is_not_read_as_an_affiliation(
    tmp_path: Path,
) -> None:
    """MDPI numbers its abstract sections "(1) Background:" -- with a space."""
    body = """---
reference_id: "PMID:2"
title: A numbered abstract.
---

## Content

1. Cells. 2023 Sep 11;12(18):2251. doi: 10.3390/cells12182251.

A numbered abstract.

Ganaiem M(1), Gozes I(2).

(1) Background: Recently, we showed aberrant nuclear boundaries in mutated cell
lines. (2) Methods: Cells were exposed to the compound, followed by live
imaging.
"""
    cache_path = write_cache(tmp_path, body, name="PMID_2.md")

    supporting_text = backfill.extract_supporting_text(
        cache_path, "A numbered abstract."
    )

    assert supporting_text is not None
    assert supporting_text.startswith("Recently, we showed aberrant nuclear boundaries")


def test_compound_structured_header_is_stripped_whole() -> None:
    assert (
        backfill.strip_leading_section_labels(
            "INTRODUCTION AND IMPORTANCE: Beta-ketothiolase deficiency is a rare "
            "inborn error of metabolism."
        )
        == "Beta-ketothiolase deficiency is a rare inborn error of metabolism."
    )
    # Defensive: a compound header whose second half has already been taken
    # off elsewhere still leaves a dangling conjunction, and PDF-derived bodies
    # arrive in that shape on their own.
    assert (
        backfill.strip_leading_section_labels(
            "BACKGROUND AND To demonstrate that the analog is a positive modulator."
        )
        == "To demonstrate that the analog is a positive modulator."
    )
    assert (
        backfill.strip_leading_section_labels(
            "MATERIAL AND Adults with advanced RET fusion-positive NSCLC received "
            "alectinib."
        )
        == "Adults with advanced RET fusion-positive NSCLC received alectinib."
    )


def test_bracket_free_sentence_is_preferred(tmp_path: Path) -> None:
    """A quote the reference validator can check beats one it cannot.

    ``linkml-reference-validator`` strips ``[...]`` as an editorial insertion
    before matching, so a verbatim quote whose brackets carry real content fails
    against the very source it was copied from.
    """
    body = """---
reference_id: "PMID:3"
title: OSR1 and SPAK in pseudohypoaldosteronism.
---

## Content

1. Biochem J. 2013 Nov;456(1):1-10. doi: 10.1042/BJ20130921.

OSR1 and SPAK in pseudohypoaldosteronism.

Chiga M(1), Uchida S(2).

Stimulation of the OSR1/SPAK [STE20/SPS1-related proline/alanine-rich kinase]
cascade plays an important role in the knock-in mouse model of the disease. The
aim of this study was to investigate the respective roles of Osr1 and Spak in
the pathogenesis of PHA II in vivo.
"""
    cache_path = write_cache(tmp_path, body, name="PMID_3.md")

    supporting_text = backfill.extract_supporting_text(
        cache_path, "OSR1 and SPAK in pseudohypoaldosteronism."
    )

    assert supporting_text == (
        "The aim of this study was to investigate the respective roles of Osr1 "
        "and Spak in the pathogenesis of PHA II in vivo."
    )


def test_bracketed_sentence_is_used_when_it_is_the_only_one(tmp_path: Path) -> None:
    body = """---
reference_id: "PMID:4"
title: Only one sentence here.
---

## Content

1. J Test. 2020 Jan;1(1):1-2. doi: 10.1000/test.

Only one sentence here.

Smith A(1).

Yo [Purkinje cell antibody, type 1] syndrome affects women in the sixth decade
and manifests as a subacute severe cerebellar ataxia.
"""
    cache_path = write_cache(tmp_path, body, name="PMID_4.md")

    supporting_text = backfill.extract_supporting_text(
        cache_path, "Only one sentence here."
    )

    assert supporting_text is not None
    assert supporting_text.startswith("Yo [Purkinje cell antibody, type 1] syndrome")


def test_translated_article_marker_is_stripped() -> None:
    assert (
        backfill.strip_leading_section_labels(
            "[Article in French] Alport syndrome (AS) is a hereditary glomerulonephritis."
        )
        == "Alport syndrome (AS) is a hereditary glomerulonephritis."
    )
    assert (
        backfill.strip_leading_section_labels(
            "[Article in Russian; Abstract available in Russian from the publisher] "
            "OBJECTIVE: Angelman syndrome is accompanied by specific EEG changes."
        )
        == "Angelman syndrome is accompanied by specific EEG changes."
    )


def test_record_without_an_abstract_yields_no_supporting_text(tmp_path: Path) -> None:
    """A letter or comment has nothing quotable; None is the honest answer.

    Callers then fall back to the title for ``statement`` and write no evidence
    block at all, which is the CLAUDE.md SOP for an unquotable claim.
    """
    body = """---
reference_id: "PMID:24091959"
title: Overhauls set scientists on edge.
---

## Content

1. Nature. 2013 Oct 3;502(7469):15-6. doi: 10.1038/502015a.

Overhauls set scientists on edge.

Jones C.

DOI: 10.1038/502015a
PMID: 24091959 [Indexed for MEDLINE]
"""
    cache_path = write_cache(tmp_path, body, name="PMID_24091959.md")

    assert (
        backfill.extract_supporting_text(
            cache_path, "Overhauls set scientists on edge."
        )
        is None
    )


def test_a_title_that_is_the_sentence_subject_is_left_alone() -> None:
    """A disease review is titled after the disease its abstract opens by naming.

    Cutting the prefix there beheads the claim — "Scimitar syndrome is a rare
    congenital anomaly ..." becomes "is a rare congenital anomaly ...". The
    remainder is still a verbatim substring, so no downstream check would catch
    it.
    """
    for title, sentence in [
        (
            "Scimitar syndrome.",
            (
                "Scimitar syndrome is a rare congenital anomaly consisting in "
                "part of right pulmonary venous return to the inferior vena cava."
            ),
        ),
        (
            "Multiple system atrophy.",
            "Multiple system atrophy (MSA) is a rare neurodegenerative disease.",
        ),
        (
            "Phenylalanine hydroxylase deficiency.",
            (
                "Phenylalanine hydroxylase deficiency is an autosomal recessive "
                "disorder of amino acid metabolism."
            ),
        ),
    ]:
        assert backfill.strip_leading_title(sentence, title) == sentence


def test_particle_led_surnames_still_count_as_a_byline() -> None:
    assert backfill.is_author_name("van der Meer AB")
    assert backfill.is_author_name("de Groot J")
    assert backfill.is_bibliographic(
        "van der Meer AB(1), de Groot J(2), Bakker PW(3), Visser MJ(1)."
    )
    # A "de novo" clause is not a name: the capital never arrives.
    assert not backfill.is_author_name("de novo variants were found in patient A")


def test_title_glued_to_the_first_sentence_is_dropped() -> None:
    title = "Circulating Tumor DNA Testing Overcomes Limitations of Genomic Profiling."
    candidate = (
        f'{title} "Liquid biopsy" is an established technique for examining '
        "circulating tumor DNA."
    )

    assert backfill.strip_leading_title(candidate, title).startswith('"Liquid biopsy"')


def test_ampersand_header_leaves_no_stray_conjunction() -> None:
    """ "BACKGROUND & AIMS:" must not leave its ampersand behind.

    A candidate arriving as ``BACKGROUND & <sentence>`` has to lose the
    ampersand along with the label, or the snippet opens on punctuation and is
    no longer a verbatim substring of the source.
    """
    assert backfill.strip_leading_section_labels(
        "BACKGROUND & Alpha-1 antitrypsin deficiency (AATD) is a genetic "
        "disorder causing pulmonary and liver disease."
    ) == (
        "Alpha-1 antitrypsin deficiency (AATD) is a genetic disorder causing "
        "pulmonary and liver disease."
    )


def test_a_trial_acronym_is_not_mistaken_for_a_section_label(tmp_path: Path) -> None:
    """ "SEAMARK: phase II study of ..." is a title, not a labelled sentence.

    Stripping the acronym first would leave a headless title that no longer
    matches the title check, so it would be returned as if it were a claim.
    """
    title = "SEAMARK: phase II study of first-line encorafenib and cetuximab."
    body = f"""---
reference_id: "PMID:5"
title: {title}
---

## Content

1. J Test. 2023 Oct;1(1):1-2. doi: 10.1000/test.

{title}

Smith A(1), Jones B(2).

Patients with both BRAF V600E mutations and MSI-H metastatic colorectal cancer
have poor prognosis.
"""
    cache_path = write_cache(tmp_path, body, name="PMID_5.md")

    supporting_text = backfill.extract_supporting_text(cache_path, title)

    assert supporting_text is not None
    assert supporting_text.startswith("Patients with both BRAF V600E mutations")


def test_a_title_that_splits_into_two_sentences_is_not_quoted(tmp_path: Path) -> None:
    """A title with its own sentence break is still a title, in both halves.

    The sentence splitter cuts it, so neither half ever *equals* the title, and
    the question half was being quoted as though it were a finding.
    """
    title = (
        "Does heart surgery change the capacity of alpha1-antitrypsin to inhibit "
        "the release of interleukin-1beta? A preliminary study."
    )
    body = f"""---
reference_id: "PMID:6"
title: {title}
---

## Content

1. Int Immunopharmacol. 2020 Apr;81:106297. doi: 10.1016/j.intimp.2020.106297.

{title}

Smith A(1), Jones B(2).

Heart surgery involving cardiopulmonary bypass induces systemic inflammation.
"""
    cache_path = write_cache(tmp_path, body, name="PMID_6.md")

    supporting_text = backfill.extract_supporting_text(cache_path, title)

    assert supporting_text == (
        "Heart surgery involving cardiopulmonary bypass induces systemic inflammation."
    )


def test_supporting_text_stays_a_verbatim_substring(tmp_path: Path) -> None:
    """Whatever is stripped must be a prefix, never a splice.

    A snippet is checked by substring match against the cached body, so any
    edit that removes text from the *middle* of a candidate produces a quote
    that cannot be verified against the source it came from.
    """
    body = """---
reference_id: "PMID:7"
title: A labelled abstract.
---

## Content

1. J Test. 2020 Jan;1(1):1-2. doi: 10.1000/test.

A labelled abstract.

Smith A(1).

STUDY OBJECTIVES: Chronic disruptions to sleep in childhood are associated with
psychiatric disease. METHODS: Participants were recruited from a birth cohort.
"""
    cache_path = write_cache(tmp_path, body, name="PMID_7.md")

    supporting_text = backfill.extract_supporting_text(
        cache_path, "A labelled abstract."
    )

    assert supporting_text is not None
    assert supporting_text.startswith("Chronic disruptions to sleep in childhood")
    collapsed_body = " ".join(body.split())
    assert " ".join(supporting_text.split()) in collapsed_body
