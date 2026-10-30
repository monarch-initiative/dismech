# The Complement-ARIE Landscape Analysis as a curation source

Written 2026-10-30 against dismech `main` at commit `ae8c3458fe3`. Sources: the
NIH Common Fund
[Complement-ARIE Landscape Analysis](https://commonfund.nih.gov/sites/commonfund/files/Complement-ARIE-Landscape-Analysis-29-Feb-2024-508.pdf)
(report dated 29 February 2024) and its
[Tableau Public dashboard](https://public.tableau.com/app/profile/complement.arie/viz/Complement-ARIELandscapeAnalysis_17029296896540/ExploreQuestions),
whose "Explore Questions" view offers the per-paper answers as a data download.

The Landscape Analysis surveys the published literature on non-animal
approaches, putting the same 19 questions to each of about 3,000 papers: what
method was described, which tissues, cell types and diseases it examined, how
it was validated, and what limits it. That makes it a ready-made map of the
field for the Monarch NAMs work to build from. Models of disease are a large
part of what DisMech records, through each entry's `experimental_models`,
`animal_models` and `computational_models` and the links that tie a model to
the mechanism it reproduces, so a structured survey of how disease is modelled
without animals bears directly on what DisMech can hold.

This report describes the data download, how it was turned into tables, and
which of the 19 questions could feed DisMech curation. It sits beside
[the Complement-ARIE Challenge winners report](complement-arie-challenge-nam-fit-2026-10-14.md),
which covers a different Complement-ARIE source (20 prize-winning proposals),
and [the NAMs search vocabulary](nams-search-vocabulary-2026-10-20.md). The
Landscape Analysis PDF itself has not been read for this report; everything
below comes from the dashboard download.

## Summary

- **The download gives answers to 19 questions for 2,737 papers.** It lists
  3,051 citation keys; 294 have no answers and 20 group several papers under
  one key, which leaves 2,737 papers with answers that trace to one paper.
- **Nearly every one of those papers has a citable identifier.** 2,427 have a
  PMID and 2,725 a DOI; 2 have neither. Most are 2023 publications (2,447 of
  2,737).
- **The answers are summaries that point to papers.** They read as
  model-generated ("Yes, the paper examines melanoma. The abstract clearly
  states …"); the download does not say how they were produced. They tell a
  curator which paper to read. A DisMech snippet is still quoted from the
  paper itself.
- **Abstracts should be fetched by PMID or DOI.** The download's `Abstract`
  column does not always line up with its row, while the answers follow the
  title and PMID, so the identifiers are the reliable join.
- **The questions closest to DisMech's data model** are diseases, tissues, cell
  types, cellular endpoints, and the validation and limitations of each
  method. Each is answered for between about half and four-fifths of the
  papers.

## The 19 questions

Counts are papers with an answer, out of the 2,737 papers. Every question also
has 294 `NA` answers, all from the same 294 papers without answers, so those
are not shown.

| Question | Full wording | Papers with an answer |
|---|---|---|
| Method Details Described | Provide details on the method described | 2,682 |
| Method Technical Challenges Described | What were the main technical challenges described in the paper that this method was trying to overcome? | 2,477 |
| Method: New Technology or Refinement of Existing Approach | Is the method novel (new technology) or is it an improvement on an existing approach (refinement)? | 2,416 |
| Tissue Types Examined | What tissue types does this paper examine? | 2,152 |
| Remaining Challenges after Method Development | What challenges remain even after the development of this method? | 2,130 |
| Cell Types Examined | What cell types does this paper examine? | 1,961 |
| Human Physiology Elements Considered | What elements of human physiology does this paper consider? | 1,847 |
| Disease(s) Examined | Is a disease examined in this paper? If so what disease? | 1,572 |
| Method Limitations | What are the limitations of the method as described in this paper? | 1,498 |
| Cellular Endpoints Measured | Are cellular endpoints being measured in this paper? If so, what are the endpoints? | 1,472 |
| Method Validation Methods Described | Did the authors describe the validation methods, such as the use of controls, taken for this method? If so, what are they? | 1,391 |
| Research Funding Details | What are the details on the funding of this research, including any grants or sponsors? | 1,303 |
| Population Modeled | Did this paper model outcomes in a specific population? If so, what population? | 553 |
| Model Metabolic Capacity Addressed | Did this model seek to address metabolic capacity of the tissue? If so, in what way? | 373 |
| Economic Considerations Discussed | Did the authors discuss economic considerations? If so, what did they say? | 174 |
| Ethical Considerations Discussed | Did the authors discuss ethical considerations? If so, what did they say? | 119 |
| Method Regulatory Use Discussed | Did the authors discuss the method in terms of a regulatory use? If so, what did the authors say? | 96 |
| Population Diversity and Variability Incorporated | Did the authors incorporate considerations of population diversity or interindividual variability into the technology? If so, how? | 48 |
| Workforce Considerations Discussed | Did the authors discuss workforce considerations? If so, what did they say? | 11 |

Every row in the download has `Answer-simple` set to `yes`, which suggests the
dashboard view lists answered questions only. A paper missing from a
question's count may therefore not have been answered "no".

## The corpus

| | Papers |
|---|---|
| Citation keys in the download | 3,051 |
| Keys grouping several papers (DOI and abstract read `*`) | 20 |
| Keys with `NA` for all 19 questions | 294 |
| **Papers with answers** | **2,737** |
| of which keyed by PMID | 2,427 |
| of which keyed by Web of Science accession | 199 |
| of which keyed by Scopus accession | 111 |
| of which have a DOI | 2,725 |

Each paper answers between 1 and 17 of the 19 questions; most answer 8 to 12.
Publication years run from 2004 to 2024, with 2,447 papers from 2023.

The 294 keys without answers carry no title or accession, but 270 of them
carry a DOI, so they can still be identified.

## Edge cases handled by the parser

A dashboard download is built for viewing rather than for reuse as data, so a
few of its features need handling before it can be read as tables. The parser
handles each one deterministically, and they are listed here so that a reader
of the tables knows what was changed.

| Edge case | Extent | Handling |
|---|---|---|
| `Abstract` does not always line up with its row | 1,020 keys share their abstract text with another key; for example, the row for *Metabolic reprogramming of clear cell renal cell carcinoma* carries an abstract about perovskite nanocrystals | Not carried forward. `abstract_shared=1` marks the keys where it can be detected. Fetch abstracts by PMID or DOI |
| Several papers under one key | 20 `Author et al. YEAR (NA)` keys, 380 answers | Listed with `merged_key=1`; answers left out, since they cannot be traced to one paper |
| Keys without answers | 294 keys | `no_content=1` |
| Title holds the PDF's first-page text (journal citation, DOI, "REVIEW ARTICLE", "Check for updates") | 28 papers | Moved to `title_page_header`; `title` left empty, to be taken from the PMID or DOI |
| Title begins with a journal logo | 1 paper (*ESC Personalizing therapy for atrial fibrillation*, Barichello 2018) | Removed by a per-paper rule, since a general rule would also strip titles that begin with an acronym |
| UTF-8 text read as Windows-1252, up to three times over (`naÃ¯ve` for `naïve`) | about 9,000 fields | Converted back |
| `NA` written for a missing title, DOI or answer | throughout | Emitted as empty, or `answer_is_na` |

## Regenerating the tables

The download is about 128 MB, over GitHub's per-file limit, so neither it nor
the tables derived from it are committed.
[`data/complement-arie/MANIFEST.yaml`](https://github.com/monarch-initiative/dismech/blob/main/data/complement-arie/MANIFEST.yaml)
records the source URL and the download's sha256. To rebuild:

1. Download "Q&A-Question Details" from the dashboard's "Explore Questions"
   view into `data/complement-arie/`.
2. Check `shasum -a 256` against the manifest.
3. Run `python scripts/complement_arie_landscape.py`.

This writes three files beside the download:

- `papers.tsv`: one row per citation key, with authors, year, accession,
  PMID, DOI, title, and the flags above.
- `answers.jsonl`: one record per paper and question, with the answer text.
- `questions.tsv`: the table in [The 19 questions](#the-19-questions).

## What this could offer DisMech

This resource meets a need already recorded in two open issues:

- **The NAMs inventory**
  ([#13602](https://github.com/monarch-initiative/dismech/issues/13602))
  anticipates "an inventory of NAMs from many sources" that will need sorting
  into models that fit a DisMech entry, fringe cases, and models that do not.
  The Landscape Analysis is such a source, already assembled: 2,737 papers,
  each with its method, disease, tissues and cell types described in the same
  form.
- **The NAMs search-term analysis**
  ([#14428](https://github.com/monarch-initiative/dismech/issues/14428)) was
  opened in support of a NAMs landscape analysis. The Complement-ARIE corpus
  is a landscape analysis that has already been carried out, so it can serve
  as the literature base that the search vocabulary in
  [the NAMs search vocabulary report](nams-search-vocabulary-2026-10-20.md)
  is checked against.

Within that, the following are candidate uses, not conclusions; none has been
tried yet.

- **Disease-to-model leads.** The 1,572 "Disease(s) Examined" answers name a
  disease alongside a method described under "Method Details Described". Read
  together, they point at papers that may describe an `experimental_models`
  record for an existing entry, which is the question the
  [winners report](complement-arie-challenge-nam-fit-2026-10-14.md) asked of 20
  proposals, here across 1,572 papers. The disease names are free text and
  need matching to MONDO and to DisMech entries first.
- **Cell and tissue annotation.** "Cell Types Examined" and "Tissue Types
  Examined" are the free-text counterparts of the CL and UBERON bindings an
  experimental model carries.
- **Model limitations.** "Method Limitations" and "Remaining Challenges after
  Method Development" describe the translational caveats that a
  `modeled_mechanisms` link records in `limitations` and `divergences`.
- **Validation.** "Method Validation Methods Described" is one input to the
  `fidelity` tier a model link is given: how faithfully the model captures the
  human mechanism.

In every case the answer points to a paper. Each fact that reaches a DisMech
entry needs the paper fetched with `just fetch-reference` and an exact quote
from it.

## Open questions

- Whether to work through the full corpus, or start with the papers that have
  a disease answer.
- How to match free-text disease names to MONDO and to DisMech entries at this
  scale, and how to decide which matches are close enough to curate.
