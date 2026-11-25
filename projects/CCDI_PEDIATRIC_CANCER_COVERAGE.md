---
title: CCDI and WHO Pediatric Cancer Coverage
status: IN_PROGRESS
description: >-
  Measure and close dismech's coverage of the CCDI pediatric cancer diagnosis
  categories and value lists and the WHO 5th edition Paediatric Tumours and CNS
  classifications, so that every CCDI diagnosis can be linked to a mechanism
  record (driver lesion, cell of origin, disrupted processes).
tags: [DISEASE_DOMAIN, ONCOLOGY, PEDIATRIC_CANCER, CCDI, COVERAGE_AUDIT]
nih_topics:
  - NIH_HT_68_childhood_adolescent_young_adult_aya_cancer
  - NIH_HT_42_rare_cancers_across_cancer_control_continuum
diseases:
  - Medulloblastoma
  - Medulloblastoma_WNT_Activated
  - Medulloblastoma_SHH_Activated
  - Medulloblastoma_Non_WNT_Non_SHH
  - Ependymoma
  - Atypical_Teratoid_Rhabdoid_Tumor
  - Rhabdoid_Tumor
  - Epithelioid_Sarcoma
  - Ewing_Sarcoma
  - Neuroblastoma
  - Wilms_Tumor
  - Hepatoblastoma
  - Retinoblastoma
  - Osteosarcoma
  - Alveolar_Rhabdomyosarcoma
  - Embryonal_Rhabdomyosarcoma
  - H3_K27_Altered_Diffuse_Midline_Glioma
  - Diffuse_Astrocytoma
  - Pilocytic_Astrocytoma
  - Mixed_Neuronal-Glial_Tumor
  - Acute_Lymphoblastic_Leukemia
  - B-Lymphoblastic_Leukemia_Lymphoma_With_Recurrent_Genetic_Abnormality
  - IDH_Mutant_AML
  - Core_Binding_Factor_AML
  - Acute_Megakaryoblastic_Leukemia
  - Juvenile_Myelomonocytic_Leukemia
  - NUT_Carcinoma
  - Pleuropulmonary_Blastoma
  - DICER1_Tumor_Predisposition_Syndrome
  - Li-Fraumeni_Syndrome
---

# CCDI and WHO Pediatric Cancer Coverage

## Purpose

The NCI Childhood Cancer Data Initiative (CCDI) codes pediatric, adolescent and
young adult (AYA) cancer diagnoses in a flat category list and a long value
list, both of which are hard to compute over. The UNC submission to the CCDI
Innovation Challenge, Track 1 ("Computable Pediatric, Adolescent, and Young
Adult Cancer Categories for CCDI"), proposes reconciling those vocabularies
through Mondo and, in its Aim 4, linking each pediatric Mondo class to its
dismech record: the driver lesion, the cell of origin, and the GO processes the
lesion disrupts. That mechanism layer is only as good as dismech's coverage of
the pediatric entities, so this project measures that coverage against the
vocabularies the proposal names and tracks the work to close the gaps.

This project is the coverage-and-alignment companion to
[CHILDHOOD_CANCER.md](CHILDHOOD_CANCER.md), which covers the wider CCDI and MCI
integration strategy, and [NEUROBLASTOMA.md](NEUROBLASTOMA.md), which covers one
tumour family in depth.

## Reference vocabularies

| Vocabulary | Size | How it was compared | Status |
|---|---|---|---|
| CCDI Diagnosis Pediatric Oncology Grouping Category (caDSR CDE 16607972 v1) | 31 categories, each with NCIt codes | Read from the caDSR API; each category assigned by hand to the dismech entries that fall under it | Done |
| CCDI data model v3.1.0, `diagnosis` permissible values (`CBIIT/ccdi-model`, `model-desc/ccdi-model-props.yml`) | 540 values, no codes attached | Each value looked up in Mondo and NCIt through the OLS search API (exact label or synonym), matched to dismech by identifier and label, then reviewed by hand | Done |
| WHO Classification of CNS Tumours, 5th ed. (CNS5) | 95 entities (Louis et al. 2021 summary, PMID:34185076) | Entity list taken from the published summary; matched by hand | Done |
| WHO Paediatric Tumours, 5th ed. (2023) | 113 tumour entities and 25 predisposition syndromes | The volume is not open access; the entity list here was reconstructed from its chapter structure and is approximate | Done, needs checking against the book |
| St. Jude CC4K v4.1 mapping template (199 diagnoses, 33 categories) | 199 | Not compared: not publicly available | Open |
| St. Jude Encyclopedia of Composable Characteristics (`stjudecloud/ecc`) | - | The public repository holds only an example record | Open |
| OncoTree, ICCC-3 | - | Not compared | Open |

## Coverage summary (2026-11-18)

### CCDI data-model diagnosis values (540)

| Status | Count | Meaning |
|---|---|---|
| `ENTRY` | 175 | A dismech entry whose `disease_term`, mappings, name or synonyms match the value |
| `SUBTYPE` | 95 | A `has_subtypes` row of an existing entry matches the value |
| `UNDER_BROADER` | 48 | Only a broader entry exists (for example a value under `Glioma`); treated as not covered |
| `MISSING` | 155 | A specific diagnosis with no entry or subtype |
| `NOT_A_SPECIFIC_DIAGNOSIS` | 67 | Grouping, NOS histology or placeholder values ("Carcinoma, NOS", "Unknown", "Healthy Control") |

Of the 473 values that name a specific diagnosis, 270 (57%) have an entry or a
subtype. Many of the 155 missing values are adult or generic histologies that
CCDI carries for completeness; the pediatric gaps are listed below.

### WHO 5th edition entities

| Classification | Entry | Subtype only | Mentioned only | Missing |
|---|---|---|---|---|
| CNS5 (95) | 35 | 24 | 9 | 27 |
| Paediatric Tumours (137, incl. 25 predisposition syndromes) | 81 | 14 | 18 | 24 |

"Mentioned only" means the entity appears in another entry's text (a
differential diagnosis, a phenotype, a predisposition syndrome's tumour
spectrum) but has no node, subtype or entry of its own. Predisposition
syndromes are close to complete: 24 of 25 have an entry, and ELP1
medulloblastoma predisposition is mentioned only in
GPR161-related_Medulloblastoma_Predisposition.

### CCDI categories (31)

| Coverage | Categories |
|---|---|
| Good | Atypical Teratoid/Rhabdoid Tumors; Choroid Plexus Tumors; CNS Germ Cell Tumors; Craniopharyngiomas; Ependymoma; Medulloblastoma; Other CNS Embryonal Tumors; Lymphoblastic Leukemia; Hodgkin Lymphoma; Soft Tissue Tumors; Neuroblastoma; Osteosarcoma; Germ Cell Tumors; Ewings Sarcoma; Rhabdoid Tumors; Retinoblastoma; Other Hematopoietic Tumors |
| Partial | CNS Sarcomas; Glioneuronal and Neuronal Tumors; High-Grade Glioma; Myeloid Leukemia; Non-Hodgkin Lymphoma; Renal Tumors; Liver Tumors; Other Brain Tumors; Other Solid Tumors; Rhabdomyosarcoma; Endocrine and Neuroendocrine Tumors |
| Weak | Low-Grade Gliomas; Other Gliomas; Lymphoproliferative Diseases |

Per-category entries and gaps are in
[`ccdi_categories_vs_dismech.tsv`](CCDI_PEDIATRIC_CANCER_COVERAGE/ccdi_categories_vs_dismech.tsv).

## Findings that affect the mechanism layer

1. **The SMARCB1 pooling example has no cell of origin to pool on.**
   Rhabdoid_Tumor and Atypical_Teratoid_Rhabdoid_Tumor describe SMARCB1 loss in
   detail but bind no Cell Ontology term anywhere, so
   `scripts/check_cancer_origin.py` derives no cell of origin for either.
   Epithelioid_Sarcoma does derive one (CL:0000134).
2. **Ewing sarcoma already records its unresolved origin as two candidates**
   (CL:0000134 mesenchymal stem cell and CL:0000333 migratory neural crest
   cell), which is the representation the proposal describes.
3. **Several core pediatric entries bind cell types but mark no origin node:**
   Medulloblastoma_SHH_Activated, Hepatoblastoma, Osteosarcoma, Ependymoma,
   Acute_Lymphoblastic_Leukemia, Juvenile_Myelomonocytic_Leukemia,
   Pleuropulmonary_Blastoma and Desmoplastic_Small_Round_Cell_Tumor.
4. **There is no overall acute myeloid leukemia entry.** IDH_Mutant_AML uses the
   generic AML Mondo term (MONDO:0018874) as its `disease_term`, so an
   identifier lookup for "Acute myeloid leukemia, NOS" lands on the IDH-mutant
   entry. Pediatric KMT2A-rearranged and NUP98-rearranged AML exist only as
   subtypes of Acute_Megakaryoblastic_Leukemia.
5. **There is no overall rhabdomyosarcoma entry**, so CCDI's
   "Rhabdomyosarcoma, NOS" has nothing to resolve to.
6. **Adrenocortical carcinoma has no entry**, although it is a CCDI value, a
   WHO paediatric entity and a core Li-Fraumeni tumour.

## Pediatric gaps by priority

### Tier A: common pediatric diagnoses or CCDI category anchors

- [ ] Adrenocortical carcinoma (MONDO:0006639), with pediatric TP53 / Li-Fraumeni context
- [ ] Overall acute myeloid leukemia entry, with pediatric KMT2A-r, NUP98-r and CBFA2T3::GLIS2 strata; decide whether IDH_Mutant_AML should keep MONDO:0018874
- [ ] Overall rhabdomyosarcoma entry, or a grouping over the alveolar and embryonal entries
- [ ] Pleomorphic xanthoastrocytoma
- [ ] Diffuse low-grade glioma, MAPK pathway-altered, and the other pediatric-type diffuse LGGs (MYB/MYBL1-altered, angiocentric glioma, PLNTY)
- [ ] Infant-type hemispheric glioma
- [ ] Lymphoblastic lymphoma (T and B)
- [ ] Primary mediastinal large B-cell lymphoma
- [ ] Post-transplant lymphoproliferative disorder

### Tier B: rare pediatric entities with clear mechanism anchors

- [ ] Primary intracranial sarcoma, DICER1-mutant
- [ ] Intracranial mesenchymal tumor, FET::CREB fusion-positive
- [ ] Desmoplastic myxoid tumor of the pineal region, SMARCB1-mutant
- [ ] Cribriform neuroepithelial tumor (SMARCB1)
- [ ] Pituitary blastoma (DICER1)
- [ ] Embryonal sarcoma of the liver
- [ ] MiT family translocation renal cell carcinoma
- [ ] Pancreatoblastoma
- [ ] Solid pseudopapillary neoplasm
- [ ] NTRK-rearranged spindle cell neoplasm
- [ ] Juvenile granulosa cell tumor
- [ ] Histiocytic sarcoma
- [ ] High-grade astrocytoma with piloid features
- [ ] Astroblastoma, MN1-altered
- [ ] Subependymal giant cell astrocytoma
- [ ] Hemangioblastoma
- [ ] Pineocytoma and pineal parenchymal tumor of intermediate differentiation

### Tier C: benign or low-volume entities

- [ ] Glioneuronal: DLGNT, MVNT, myxoid glioneuronal tumor, DGONC, central and extraventricular neurocytoma, cerebellar liponeurocytoma
- [ ] Renal: metanephric adenoma, ossifying renal tumor of infancy, cystic nephroma, anaplastic sarcoma of kidney
- [ ] Soft tissue and bone: lipoblastoma, lipofibromatosis, fibrous hamartoma of infancy, plexiform fibrohistiocytic tumor, kaposiform hemangioendothelioma, osteoblastoma, chondroblastoma
- [ ] Other: Spitz tumours, mesenchymal hamartoma of liver, congenital peribronchial myofibroblastic tumor, fetal lung interstitial tumor

Before creating any of these, check the stub queue and open `claim` issues, and
decide entry versus subtype by the cancer granularity ladder (design decisions
§3a): a histologic or WHO-defined molecular entity is an entry, a biomarker
stratum is a subtype by default.

## Tasks

### Mechanism layer on existing entries

- [ ] Bind cell types and mark the origin node on Rhabdoid_Tumor and Atypical_Teratoid_Rhabdoid_Tumor
- [ ] Mark origin nodes on the eight entries in finding 3
- [ ] Check that every pediatric entry with a recurrent driver has a `variant_origin: SOMATIC` node, so the driver lesion is queryable
- [ ] Add `conforms_to` links where a pediatric node instantiates an existing module (for example SWI/SNF loss, fusion-driven transcriptional reprogramming)

### Alignment

- [ ] Compare against the CC4K v4.1 diagnosis list once it can be obtained
- [ ] Check the reconstructed WHO Paediatric Tumours entity list against the book
- [ ] Add OncoTree and ICCC-3 columns to the crosswalk
- [ ] Add NCIt mappings on pediatric entries that lack them, so CCDI category NCIt codes resolve
- [ ] Re-run the crosswalk after each tranche of new entries and update the summary counts

## Data files

All in [`CCDI_PEDIATRIC_CANCER_COVERAGE/`](CCDI_PEDIATRIC_CANCER_COVERAGE/):

| File | Rows | Contents |
|---|---|---|
| `ccdi_categories_vs_dismech.tsv` | 31 | CCDI category, NCIt codes, coverage grade, dismech entries, gaps |
| `ccdi_diagnosis_values_vs_dismech.tsv` | 540 | CCDI data-model value, Mondo and NCIt match from OLS, reviewed `dismech_status`, location (`File[subtype]`), and the unreviewed `auto_status` |
| `who_entities_vs_dismech.tsv` | 232 | WHO CNS5 and Paediatric Tumours entity, WHO group, `dismech_status`, location |

The Mondo and NCIt identifiers in the CCDI value table come from an automatic
OLS search and have not been curated; treat them as leads, not mappings. The
`dismech_status` column was reviewed by hand, but a location of the form
`File[subtype]` asserts only that the subtype exists, not that its content is
complete.
