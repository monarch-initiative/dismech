# Phenotype-systems overview: design note

**Date:** 2026-09-13 · **Status:** implemented (`src/dismech/phenotype_systems.py`)

## The ask

An UpSet plot over the browser's "Phenotype Systems" facet (Nervous System
1,629, Musculoskeletal 1,361, ...), or some other way to get a sense of
"multiple parentage" for a disease.

## What the data said

Before drawing anything, the facet data was profiled (2,569 diseases at the
time; 2,924 by implementation):

| Fact | Value |
|---|---|
| Distinct exact combinations of systems | 1,721 |
| Diseases whose combination no other disease shares | 56% |
| Diseases in a combination shared by 5+ diseases | 22% |
| Coverage of the 30 most frequent combinations | 18% |
| Median systems per disease (presence) | 5 |
| HP terms in use that sit under 2+ top-level branches | 407 of 1,415 |

Two consequences drove the design:

1. **Exact combinations are nearly unique per disease.** A classic UpSet plot
   sorts exact intersections by size, and here the size-1 tail is the corpus.
   The plot can only ever draw the shared fifth, and a reader would take the
   drawn bars for the whole picture.
2. **"Multiple parentage" has two sources that must not be conflated.** A
   disease can span systems because it has phenotypes in several of them, or
   because a single HP term is under two branches (HP is a DAG). The facet
   counts both identically, and it is presence-only: Marfan syndrome counts in
   Nervous System on the strength of one phenotype out of 26.

## Framings considered

Four framings were mocked up with the real data and reviewed:

- **A. UpSet over exact combinations.** Rejected as the primary view for the
  reason above, kept as a degree-limited panel with a sharing bar in front of
  it that shows what it cannot draw.
- **B. Pairwise co-occurrence matrix** coloured by lift. Adopted: it is what an
  UpSet plot degrades to gracefully when exact sets fragment, and it answers
  "which systems travel together beyond chance".
- **C. Per-disease profile with an effective number of systems** (exp of the
  Shannon entropy of phenotypes per system). Adopted as the per-disease answer
  to the original question: it separates Rett (14 phenotypes, effectively 1.8
  systems) from Fanconi anemia (180 phenotypes, effectively 15).
- **D. Distribution of systems per disease.** Adopted, drawn twice (presence
  and effective) on one axis so the overstatement is visible.

A first round of mockups truncated the system list (top 9 in the UpSet rows,
top 14 in the matrix, top 8 per profile) and was rightly called out as giving
a misleading picture of heterogeneity. Every panel now carries all 23 systems.

## Design

- **One module, `dismech.phenotype_systems`,** with the computation
  (`profile_disorder`, `collect_phenotype_systems`) separated from rendering
  (`render_phenotype_systems_page`) and from the report writer that follows the
  existing `qc_dashboard` pattern: HTML + JSON under `dashboard/`, and a
  sentinel-delimited block injected into `dashboard/index.html`.
- **Input is the browser's category cache,** `app/hpo_category_cache.json`,
  so the module never touches the ontology and the two views cannot disagree on
  what a system is. The CI build already writes that cache before the dashboard.
- **Charts are server-rendered inline SVG** with no JavaScript library; the
  only script is the sortable/filterable disease table. Dashboard pages are
  light-theme only, so the page follows that rather than the disorder pages'
  theme handling.
- **Wired into `just gen-dashboard`** via a new `gen-phenotype-systems`
  recipe, so the `generate-pages` workflow picks it up without changes.

## Deliberately out of scope

- Changing the browser facet, or adding sort-by-spread to the browser. The
  per-disease numbers are in the JSON if that is wanted later.
- Frequency-weighting phenotypes (a `VERY_FREQUENT` finding counting more than
  an `OCCASIONAL` one). Frequency coverage is uneven across entries, so it would
  make the effective count depend on curation depth as much as biology.
- A second axis of parentage, MONDO parents. Half the KB's diseases have two
  MONDO parents; that is a different question from phenotype spread and would
  be its own page.
