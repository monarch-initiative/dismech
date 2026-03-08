# TODO: Populate Inheritance Detail Fields

## Problem

The `Inheritance` class has slots for `de_novo_rate`, `penetrance`,
`expressivity`, and `parent_of_origin_effect`, but they are almost
empty. Of 75 Mendelian disorders, only 4 have `de_novo_rate` and 6
have `penetrance`. 70 files record mode of inheritance (AD/AR/XL)
with no further detail. 10 Mendelian files lack inheritance sections
entirely.

This data is needed to inform Mondo's ongoing discussion on
representing inherited vs. de novo variation
([mondo#8483](https://github.com/monarch-initiative/mondo/issues/8483)).

## Tasks

### 1. Schema additions (do first)

- [ ] Add `de_novo_type` enum to distinguish germline de novo,
  post-zygotic mosaic, and somatic-only mutations. Proposed values:
  `GERMLINE_DE_NOVO`, `POSTZYGOTIC_MOSAIC`, `SOMATIC_ONLY`, `MIXED`,
  `UNKNOWN`.
- [ ] Add optional `gene` slot on `Inheritance` for gene-specific
  inheritance data (e.g., Noonan syndrome PTPN11 vs. RAF1 have
  different de novo rates).

### 2. Tier 0: Add basic inheritance to 10 files missing it

MONDO:0013282 Alpha-1 Antitrypsin Deficiency,
MONDO:0009562 Beta Mannosidosis,
MONDO:0700294 CTCF-related Neurodevelopmental Disorder,
MONDO:0010526 Fabry disease,
MONDO:0006507 Hemochromatosis,
MONDO:0007422 Keratoderma Hereditarium Mutilans,
MONDO:0020642 Polycystic Kidney Disease,
MONDO:0008318 Proteus syndrome,
MONDO:0011382 Sickle Cell Disease,
MONDO:0014848 You-Hoover-Fong Syndrome.

### 3. Tier 1: Full detail for severe AD disorders (highest Mondo value)

These have high expected de novo rates and are most informative for
the inherited/de novo modeling question:

- [ ] Apert Syndrome (MONDO:0007041) - ~98% de novo
- [ ] Cardiofaciocutaneous Syndrome (MONDO:0015280)
- [ ] Costello Syndrome (MONDO:0009026)
- [ ] Noonan Syndrome (MONDO:0018997) - mixed, gene-specific rates
- [ ] Loeys-Dietz Syndrome (MONDO:0018954) - ~75% de novo
- [ ] Diamond-Blackfan Anemia (MONDO:0015253) - ~40-45% de novo
- [ ] Pfeiffer Syndrome (MONDO:0007043)
- [ ] Shprintzen-Goldberg Syndrome (MONDO:0008426)
- [ ] Gorlin Syndrome (MONDO:0007187)
- [ ] Hypochondrogenesis (MONDO:0019669) - lethal, all de novo
- [ ] Thanatophoric Dysplasia Type 1 (MONDO:0008546) - lethal, all de novo
- [ ] Thanatophoric Dysplasia Type 2 (MONDO:0008547) - lethal, all de novo
- [ ] SADDAN (MONDO:0014658)
- [ ] Osteogenesis Imperfecta I-IV (MONDO:0008146-8148) - variable by type

### 4. Tier 2: Remaining AD disorders

CADASIL, Camurati-Engelmann, Brachydactyly Type A1, Hand-Foot-Genital,
Ulnar-Mammary, Pallister-Hall, Greig, Multiple Synostoses, Stickler
Type 1.

### 5. Tier 3: AR / X-linked (penetrance and expressivity only)

De novo distinction less relevant for AR, but penetrance/expressivity
still useful.

### 6. Generate Mondo summary table

Export populated data as a table for the
[mondo#8483](https://github.com/monarch-initiative/mondo/issues/8483)
discussion, showing which diseases have a clinically meaningful
inherited/de novo split and where the binary breaks down.

## Data Sources

1. GeneReviews (via `aurelian fulltext`) - best single source
2. OMIM clinical synopsis
3. ClinGen gene-disease validity
4. Primary literature (PubMed)

## Full Plan

See [projects/INHERITANCE_ENRICHMENT.md](../../projects/INHERITANCE_ENRICHMENT.md)
for detailed rationale, special cases, and curation protocol.
