# Inheritance Detail Enrichment Project

## Motivation

Mondo is actively debating how to represent the inherited vs. de novo
distinction in the ontology (see
[#8074](https://github.com/monarch-initiative/mondo/issues/8074) on
tuberous sclerosis,
[#8483](https://github.com/monarch-initiative/mondo/issues/8483) on
genetic epilepsies). The dismech schema already has slots for
`de_novo_rate`, `penetrance`, `expressivity`, and
`parent_of_origin_effect` on `Inheritance` objects, but these are
almost entirely unpopulated. Filling them in would:

1. Provide Mondo with structured, evidence-backed data on how often
   diseases arise de novo vs. are inherited, directly informing the
   #8483 proposal.
2. Surface cases where the inherited/de novo split is clinically
   meaningful (different severity, different recurrence risk) vs.
   cases where it is not.
3. Identify diseases where somatic mosaicism complicates the simple
   germline-inherited vs. germline-de-novo dichotomy.

## Current State

| Metric | Count |
|--------|-------|
| Total disorder files | 577 |
| Categorized as Mendelian | 75 |
| Have `inheritance` section | 78 |
| ...with only mode (AD/AR/XL), no detail | 70 |
| Have `de_novo_rate` | 4 |
| Have `penetrance` | 6 |
| Have `expressivity` | 5 |
| Have `parent_of_origin_effect` | 2 |
| Mendelian with NO inheritance section | 10 |

The 4 files with `de_novo_rate` today: Achondroplasia (>90%),
Achondrogenesis Type II (most cases), Temple-Baraitser (>90%), CINCA
(>80%).

## Priority Tiers

### Tier 0: Fix the 10 Mendelian files missing inheritance entirely

These need at least mode-of-inheritance before detail fields make
sense.

| MONDO ID | Disease |
|----------|---------|
| MONDO:0013282 | Alpha-1 Antitrypsin Deficiency |
| MONDO:0009562 | Beta Mannosidosis |
| MONDO:0700294 | CTCF-related Neurodevelopmental Disorder |
| MONDO:0010526 | Fabry disease |
| MONDO:0006507 | Hemochromatosis |
| MONDO:0007422 | Keratoderma Hereditarium Mutilans |
| MONDO:0020642 | Polycystic Kidney Disease |
| MONDO:0008318 | Proteus syndrome |
| MONDO:0011382 | Sickle Cell Disease |
| MONDO:0014848 | You-Hoover-Fong Syndrome |

### Tier 1: AD disorders likely to have high de novo rates

Autosomal dominant disorders with severe phenotypes (reduced
reproductive fitness) are the most informative cases for the Mondo
discussion - they are where the inherited/de novo distinction matters
most for genetic counseling and recurrence risk.

Priority targets (AD, severe, high expected de novo fraction):

| MONDO ID | Disease | Why prioritize |
|----------|---------|----------------|
| MONDO:0007041 | Apert Syndrome | AD, severe craniofacial; ~98% de novo expected |
| MONDO:0015280 | Cardiofaciocutaneous Syndrome | AD, severe; nearly all de novo |
| MONDO:0009026 | Costello Syndrome | AD, severe; nearly all de novo |
| MONDO:0018997 | Noonan Syndrome | AD, variable; mixed inherited/de novo |
| MONDO:0018954 | Loeys-Dietz Syndrome | AD, ~75% de novo |
| MONDO:0015253 | Diamond-Blackfan Anemia | AD, ~40-45% de novo |
| MONDO:0007043 | Pfeiffer Syndrome | AD, severe craniofacial |
| MONDO:0008426 | Shprintzen-Goldberg Syndrome | AD, connective tissue |
| MONDO:0007187 | Gorlin Syndrome | AD, cancer predisposition |
| MONDO:0019669 | Hypochondrogenesis | AD, lethal; all de novo |
| MONDO:0008546 | Thanatophoric Dysplasia Type 1 | AD, lethal; all de novo |
| MONDO:0008547 | Thanatophoric Dysplasia Type 2 | AD, lethal; all de novo |
| MONDO:0014658 | SADDAN | AD, severe; de novo |
| MONDO:0008146-8148 | Osteogenesis Imperfecta I-IV | AD, variable de novo rates by type |

### Tier 2: AD disorders with lower or unknown de novo fraction

| MONDO ID | Disease |
|----------|---------|
| MONDO:0007432 | CADASIL Type 1 |
| MONDO:0007542 | Camurati-Engelmann Disease |
| MONDO:0007215 | Brachydactyly Type A1 |
| MONDO:0007698 | Hand-Foot-Genital Syndrome |
| MONDO:0008411 | Ulnar-Mammary Syndrome |
| MONDO:0007804 | Pallister-Hall Syndrome |
| MONDO:0008287 | Greig Cephalopolysyndactyly Syndrome |
| MONDO:0017923 | Multiple Synostoses Syndrome |
| MONDO:0007160 | Stickler Syndrome Type 1 |

### Tier 3: AR / X-linked disorders

For autosomal recessive disorders, the de novo distinction is less
clinically impactful (both alleles must be affected), but penetrance
and expressivity data is still valuable. X-linked disorders have
intermediate relevance (de novo rate in carrier mothers matters for
counseling).

## Data Sources

For each disorder, the curation agent should consult in order:

1. **GeneReviews** (via `aurelian fulltext`): Most GeneReviews
   entries have an "Inheritance" or "Molecular Genetics" section with
   de novo rates and penetrance. This is the single best source.

2. **OMIM clinical synopsis**: Often states "sporadic" or "de novo"
   with approximate rates. The phenotypic series pages are
   particularly useful for distinguishing inherited from de novo
   subtypes.

3. **ClinGen gene-disease validity**: Structured curation that
   includes inheritance evidence. Available at
   <https://search.clinicalgenome.org/>.

4. **Primary literature** (PubMed): For specific quantitative
   estimates. Large cohort studies or systematic reviews are
   preferred.

## Fields to Populate

For each `Inheritance` entry:

| Field | Type | Notes |
|-------|------|-------|
| `penetrance` | Enum: COMPLETE, INCOMPLETE, UNKNOWN | Most AD Mendelian diseases have complete or near-complete penetrance |
| `penetrance_percentage` | String | When a quantitative estimate exists, e.g., "85-95%" |
| `expressivity` | Enum: VARIABLE, CONSISTENT, UNKNOWN | Variable expressivity is common in AD disorders |
| `de_novo_rate` | FrequencyQuantity (string) | Use percentage or range, e.g., ">90", "40-50", "rare" |
| `parent_of_origin_effect` | String | Parental origin bias, e.g., "paternal origin predominates" |
| `description` | String | Free text for nuances not captured by the structured fields |

All claims require evidence with exact PubMed abstract quotes per
dismech SOP.

## Special Cases for the Mondo Discussion

Some disorders don't fit a clean inherited/de novo binary. These are
particularly informative for the #8483 proposal:

### Somatic mosaicism complicates the picture

- **Proteus syndrome** (MONDO:0008318): Caused by somatic AKT1
  mutations; never inherited (lethal if germline). This is *neither*
  "inherited" nor "de novo germline" - it's somatic-only.
- **Tuberous sclerosis** (#8074): Can be germline inherited, germline
  de novo, or somatic mosaic. The mosaic cases may have milder
  phenotypes and are not heritable.

### De novo rate varies by gene within a phenotypic series

- **Osteogenesis Imperfecta**: OI type I (COL1A1/COL1A2) has lower de
  novo rates than OI type II (often de novo, lethal). Mondo groups
  these under OMIM phenotypic series - how should the de novo rate
  attach?
- **Noonan Syndrome**: PTPN11 mutations more often inherited; RAF1
  mutations more often de novo. The de novo rate is gene-specific, not
  disease-level.

### "De novo" means different things

- Germline de novo in the parent's gamete (classic)
- Post-zygotic de novo leading to mosaicism
- Somatic mutation in affected tissue only

The `de_novo_rate` field as currently defined conflates these. We may
want to add a `de_novo_type` enum or similar.

## Curation Protocol

### Per-disorder workflow

1. Identify the GeneReviews entry (if it exists) using `aurelian
   fulltext`.
2. Extract inheritance details: mode, penetrance, de novo rate,
   expressivity, parent-of-origin effects.
3. For each claim, find a PubMed-cited sentence that can serve as an
   exact-quote snippet.
4. If GeneReviews lacks specifics, search OMIM and primary literature.
5. Populate the `Inheritance` block with structured fields + evidence.
6. Run `just validate kb/disorders/<file>.yaml` and `just
   validate-references kb/disorders/<file>.yaml`.

### Batch approach

An AI curation agent can draft inheritance blocks for multiple
disorders in a batch, but each must be validated against the reference
validation pipeline before merge. Estimated effort:

- Tier 0 (10 files, basic mode): ~1 agent session
- Tier 1 (14 disorders, full detail): ~2-3 agent sessions
- Tier 2 (9 disorders): ~1-2 agent sessions
- Tier 3 (remaining AR/XL): ~2-3 agent sessions

## Output for Mondo

Once populated, generate a summary table for the Mondo #8483
discussion:

```
MONDO_ID | Disease | Mode | De_Novo_Rate | Penetrance | Mosaicism? | Source
```

This table would concretely demonstrate:
- Which diseases have a clinically meaningful inherited/de novo split
- Where the binary fails (mosaicism, gene-specific rates)
- What structured fields an ontology would need to capture this data

## Schema Considerations

The current schema handles most cases, but two extensions may be
needed:

1. **`de_novo_type` enum**: To distinguish germline de novo,
   post-zygotic mosaic, and somatic-only. Values might be:
   `GERMLINE_DE_NOVO`, `POSTZYGOTIC_MOSAIC`, `SOMATIC_ONLY`,
   `MIXED`, `UNKNOWN`.

2. **Gene-specific inheritance blocks**: Some disorders need
   per-gene inheritance data (e.g., Noonan: PTPN11 vs. RAF1 have
   different de novo rates). The current schema attaches inheritance
   to the disease, not to the gene. A `gene` slot on `Inheritance`
   (or nesting inheritance under `genetic`) might be needed.
