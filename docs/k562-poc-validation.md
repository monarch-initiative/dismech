# K562 Blood Trait PoC Validation

## Overview

This document validates whether K562 Perturb-seq gene programs (Ota et al., Nature 2025)
whose GO annotations match a disorder's pathophysiology also contain genes documented in
that disorder. We focus on the three traits with the strongest K562 S-LDSC heritability
enrichment: **MCH**, **RDW**, and **IRF**.

### S-LDSC Heritability Enrichment (Table S3)

| Trait | K562 Enrichment | Enrichment p | Coefficient p |
|-------|:-:|:-:|:-:|
| MCH (Mean corpuscular haemoglobin) | **16x** | 2.8e-15 | 1.7e-11 |
| RDW (Red cell distribution width) | **13x** | 1.3e-12 | 5.8e-09 |
| IRF (Immature reticulocyte fraction) | **11x** | 1.4e-07 | 6.4e-05 |

These are the strongest K562-specific signals in the Ota et al. data, confirming
that K562 chromatin accessibility explains a substantial fraction of heritability
for these red blood cell traits.

### Data Sources

- **Programs**: 60 consensus NMF programs from `docs/assets/k562_validation/program_go_mapping.yaml`
- **Traits**: 54 UK Biobank LOF traits from `docs/assets/k562_validation/trait_to_hpo.yaml`
- **Disorders**: dismech knowledge base entries at `kb/disorders/*.yaml`

---

## 1. MCH (Mean Corpuscular Hemoglobin)

**Trait**: Mean amount of hemoglobin per red blood cell. Low MCH indicates hypochromic anemia
(iron deficiency, thalassemia); high MCH indicates macrocytic anemia.

### Related Disorders in dismech

| Disorder | Status | Genes | GO Terms |
|----------|--------|:-----:|:-------:|
| Beta Thalassemia | Curated | 9 | 10 |
| Sickle Cell Disease | Curated | 3 | 10 |
| Alpha Thalassemia | Not yet curated | - | - |
| Hereditary Spherocytosis | Not yet curated | - | - |

**Combined gene set** (from curated disorders): BCL11A, HAMP, HBA1, HBA2, HBB, HBS1L,
HBS1L-MYB, KLF1, MYB

**Key GO terms**: GO:0042541 (hemoglobin biosynthetic process), GO:0006783 (heme biosynthetic
process), GO:0030218 (erythrocyte differentiation), GO:0006879 (iron ion homeostasis),
GO:0034101 (erythrocyte homeostasis)

### Matching Programs

| Program | Annotation | Match Type | GO Overlap | Gene Overlap | Marker |
|---------|-----------|:----------:|------------|--------------|--------|
| **P40** | Hemoglobin synthesis | **CONFIRMED** | hemoglobin biosynthetic, heme biosynthetic | HBA1 | RBC |
| P28 | RBC (glycoproteins) | PARTIAL_GO | hemoglobin biosynthetic, heme biosynthetic | - | RBC |
| P22 | RNA metabolic process (myeloid) | PARTIAL_GENE | - | MYB | myeloid |
| P42 | Chaperone complex | PARTIAL_GENE | - | HBS1L | erythroid progenitor, RBC |

### Analysis

**P40 (Hemoglobin synthesis)** is the strongest match -- a CONFIRMED hit with both GO term
overlap (hemoglobin/heme biosynthesis) and gene overlap (HBA1). This program contains the
globin gene cluster (HBG2, HBZ, HBG1, HBA1) plus heme biosynthesis enzymes (ALAS2, HMBS,
SLC25A37, BLVRB). Its RBC marker coexpression confirms erythroid lineage specificity. This
is exactly the kind of program expected to explain MCH heritability.

**P28 (RBC glycoproteins)** shows GO overlap through HALLMARK_HEME_METABOLISM enrichment
and includes ALAS2 and glycophorin genes (GYPA, GYPB) -- classic erythroid markers.
Though no gene directly matches the dismech gene set, the pathway biology is clearly relevant.

**P22 and P42** contribute MYB and HBS1L respectively -- both are known HbF modifiers
(PMID:18667698, Lettre et al. 2008) and documented in the Beta Thalassemia and SCD
dismech entries. MYB is in a myeloid transcription regulation program, consistent with
its role in erythroid-myeloid lineage decisions. HBS1L appears in a chaperone complex
program with erythroid progenitor coexpression.

**MCH classification**: 1 CONFIRMED, 1 PARTIAL_GO, 2 PARTIAL_GENE

---

## 2. RDW (Red Cell Distribution Width)

**Trait**: Measures variation in red cell volume (anisocytosis). Elevated RDW reflects
heterogeneous red cell populations, seen in iron deficiency, thalassemia trait, and mixed
anemias.

### Related Disorders in dismech

| Disorder | Status | Genes | GO Terms |
|----------|--------|:-----:|:-------:|
| Sickle Cell Disease | Curated | 3 | 10 |
| Beta Thalassemia | Curated | 9 | 10 |
| Hemochromatosis | Curated | 1+ | 11 |
| Alpha Thalassemia | Not yet curated | - | - |
| Hereditary Spherocytosis | Not yet curated | - | - |

**Combined gene set**: BCL11A, HAMP, HBA1, HBA2, HBB, HBS1L, HBS1L-MYB, KLF1, MYB,
plus HFE-related genes from Hemochromatosis

**Key GO terms**: All MCH GO terms plus iron-related terms from Hemochromatosis:
GO:0010039 (response to iron ion), GO:0034756/57/58 (regulation of iron ion transport),
GO:0008631 (intrinsic apoptotic signaling in response to oxidative stress)

### Matching Programs

| Program | Annotation | Match Type | GO Overlap | Gene Overlap | Marker |
|---------|-----------|:----------:|------------|--------------|--------|
| **P40** | Hemoglobin synthesis | **CONFIRMED** | hemoglobin biosynthetic, heme biosynthetic | HBA1 | RBC |
| P28 | RBC (glycoproteins) | PARTIAL_GO | hemoglobin biosynthetic, heme biosynthetic | - | RBC |
| P22 | RNA metabolic process (myeloid) | PARTIAL_GENE | - | MYB | myeloid |
| P42 | Chaperone complex | PARTIAL_GENE | - | HBS1L | erythroid progenitor, RBC |

### Analysis

The same 4 programs match for RDW as for MCH. This overlap is expected: MCH and RDW are
genetically correlated traits, both driven by hemoglobin and erythrocyte biology. The addition
of Hemochromatosis to the disorder set adds iron homeostasis GO terms but does not recruit
additional programs, because none of the 60 K562 programs have iron transport/homeostasis
as their representative GO term. However, P28's top10 pathways do include `iron_ion_homeostasis`,
which would be captured by a more granular pathway-level matching strategy.

**RDW classification**: 1 CONFIRMED, 1 PARTIAL_GO, 2 PARTIAL_GENE

---

## 3. IRF (Immature Reticulocyte Fraction)

**Trait**: Proportion of immature reticulocytes among all reticulocytes. High IRF indicates
active/stressed erythropoiesis (hemolysis, recovery from aplasia, bleeding).

### Related Disorders in dismech

| Disorder | Status | Genes | GO Terms |
|----------|--------|:-----:|:-------:|
| Diamond-Blackfan Anemia | Not yet curated | - | - |
| Sickle Cell Disease | Curated | 3 | 10 |
| Beta Thalassemia | Curated | 9 | 10 |
| Fanconi Anemia | Curated | 22 | 12 |

**Combined gene set** (34 genes): Includes globin/HbF modifiers (BCL11A, HBA1, HBA2, HBB,
HBS1L, KLF1, MYB, HAMP) plus the complete Fanconi anemia DNA repair pathway (FANCA-M,
BRCA1, BRCA2, PALB2, RAD51, RAD51C, RFWD3, SLX4, UBE2T, XRCC2, ALDH2, ADH5, MAD2L2, KMT2D)

**Key GO terms**: Hemoglobin/heme biosynthesis terms plus DNA repair terms from FA:
GO:0036297 (interstrand cross-link repair), GO:0035825 (homologous recombination),
GO:0016567 (protein ubiquitination), GO:0002244 (hematopoietic progenitor differentiation)

### Matching Programs

| Program | Annotation | Match Type | GO Overlap | Gene Overlap | Marker |
|---------|-----------|:----------:|------------|--------------|--------|
| **P40** | Hemoglobin synthesis | **CONFIRMED** | hemoglobin biosynthetic, heme biosynthetic | HBA1 | RBC |
| P28 | RBC (glycoproteins) | PARTIAL_GO | hemoglobin biosynthetic, heme biosynthetic | - | RBC |
| P4 | Cell cycle (S phase, DNA replication) | PARTIAL_GENE | - | XRCC2 | Sphase |
| P22 | RNA metabolic process (myeloid) | PARTIAL_GENE | - | MYB | myeloid |
| P42 | Chaperone complex | PARTIAL_GENE | - | HBS1L | erythroid progenitor, RBC |

### Analysis

IRF recruits one additional program compared to MCH/RDW: **P4 (Cell cycle, S phase, DNA
replication)**, which contains XRCC2 -- a Fanconi anemia complementation group gene involved
in homologous recombination. This program is enriched for DNA repair and cell cycle pathways,
matching the FA DNA damage response biology. The S-phase marker coexpression is mechanistically
consistent: FA pathway defects lead to S-phase checkpoint activation and replication stress,
contributing to bone marrow failure and reduced reticulocyte production.

The P40 CONFIRMED match again anchors the analysis through hemoglobin biosynthesis.

**IRF classification**: 1 CONFIRMED, 1 PARTIAL_GO, 3 PARTIAL_GENE

---

## Summary

### Match Counts

| Trait | CONFIRMED | PARTIAL_GO | PARTIAL_GENE | Total | Unique Genes |
|-------|:---------:|:----------:|:------------:|:-----:|:------------:|
| MCH | 1 | 1 | 2 | 4 | HBA1, MYB, HBS1L |
| RDW | 1 | 1 | 2 | 4 | HBA1, MYB, HBS1L |
| IRF | 1 | 1 | 3 | 5 | HBA1, MYB, HBS1L, XRCC2 |

### Key Findings

1. **P40 (Hemoglobin synthesis) is the anchor program** for all three traits, providing
   both GO and gene-level validation. Its top10 genes include the globin gene cluster and
   heme biosynthesis machinery, directly matching Beta Thalassemia pathophysiology.

2. **Gene confirmation rate**: 4 unique genes confirmed across all three traits (HBA1, MYB,
   HBS1L, XRCC2) out of ~40 combined disorder genes = ~10% gene confirmation rate, compared
   to 6.1% for the T cell validation. The higher rate likely reflects K562's erythroid
   lineage being a more direct match for blood disorders than T cells are for autoimmune
   diseases.

3. **GO term matching adds value**: P28 (RBC glycoproteins) would be missed by gene-only
   matching but is captured through hemoglobin/heme biosynthesis GO term overlap. Its
   pathway profile (porphyrin metabolism, iron homeostasis) is clearly relevant to MCH/RDW/IRF.

4. **Lineage markers validate matches**: All CONFIRMED and PARTIAL_GO matches have RBC or
   erythroid progenitor marker coexpression, providing independent evidence that these programs
   operate in the relevant cell lineage.

5. **Cross-trait stability**: The core matches (P40, P28, P22, P42) are stable across all
   three traits, reflecting the shared biology of hemoglobin synthesis and erythrocyte
   homeostasis. Only P4 (DNA replication/repair) is IRF-specific, reflecting the Fanconi
   anemia contribution.

### Curation Gaps

- **Alpha Thalassemia** and **Hereditary Spherocytosis** are not yet curated. Adding these
  would increase the MCH/RDW gene set (HBA1/HBA2 for alpha-thal; ANK1, SLC4A1, SPTA1,
  SPTB, EPB42 for HS) and potentially recruit additional programs.

- **Diamond-Blackfan Anemia** is not yet curated. Its ribosomal protein genes (RPS19, RPL5,
  RPL11, RPL35A, RPS26) would likely match the ribosome programs (P19, P20, P21, P37, P38,
  P52, P59, P60), which are abundant in K562. This could significantly increase the IRF
  match count.

- **Broader pathway matching**: The current analysis uses exact GO term ID matching. A
  hierarchical approach (matching GO ancestors/descendants) would capture more biology --
  for example, iron_ion_homeostasis in P28's pathways would match Hemochromatosis GO terms.

### Comparison to T Cell Validation

| Metric | T Cell (Autoimmune) | K562 (Blood Traits) |
|--------|:---:|:---:|
| Gene confirmation rate | 6.1% | ~10% |
| Confirmed programs | 5 | 1 (stable across traits) |
| Disorders validated | 14 | 3 (curated) |
| Traits analyzed | 11 (disease risk) | 3 (quantitative) |
| GO matching value-add | Moderate | Clear (P28 captured) |

The K562 validation shows a higher gene confirmation rate but validates against fewer
disorders (since many blood disorders are not yet curated). Curating the remaining
4 disorders from Phase 1 would substantially increase coverage.
