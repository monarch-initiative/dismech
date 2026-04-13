# Malignant Peripheral Nerve Sheath Tumor Research Notes

Date: 2026-04-12

## Modeling choices

This curation explicitly follows the cancer-modeling guidance called out from
dismech issue `#1198`.

- The dismech page is the disease-level mechanism graph for **MPNST as a whole**,
  not a page-per-ontology-subclass expansion.
- `disease_term` is MONDO-first: `MONDO:0017827` malignant peripheral nerve sheath tumor.
- NCIT was handled where the current schema is strongest today:
  `NCIT:C3798` is recorded in the disease-level notes as the requested disease
  cross-reference, and NCIT histopathology grounding was used for
  `NCIT:C53643` Spindle Cell Pattern.
- Subtypes were modeled as **flat facet axes**, not as separate dismech diseases:
  predisposition context (`NF1-Associated`, `Sporadic`, `Radiation-Associated`)
  and histology (`Epithelioid`, `Malignant Triton Tumor`).
- `Epithelioid` remained inside the parent MPNST page even though it has a
  subtype-specific `SMARCB1` branch, because the broader disease still shares a
  common MPNST clinical/pathologic frame and the schema can represent the
  distinct mechanism with subtype-scoped nodes.

## Ontology grounding used

- Disease: `MONDO:0017827` malignant peripheral nerve sheath tumor
- Histologic subtype: `MONDO:0004540` epithelioid malignant peripheral nerve sheath tumor
- Histologic subtype: `MONDO:0016757` malignant triton tumor
- Histopathology: `NCIT:C53643` Spindle Cell Pattern
- Cell type: `CL:0002573` Schwann cell
- Key GO processes:
  - `GO:0007265` Ras protein signal transduction
  - `GO:0000075` cell cycle checkpoint signaling
  - `GO:0006974` DNA damage response
  - `GO:0006325` chromatin organization
  - `GO:0010468` regulation of gene expression
  - `GO:0008283` cell population proliferation
- Phenotypes:
  - `HP:0031459` Soft tissue neoplasm
  - `HP:0012531` Pain
  - `HP:0001324` Muscle weakness
- Treatments:
  - `MAXO:0000004` surgical procedure
  - `MAXO:0000014` radiation therapy
  - `MAXO:0000647` chemotherapy
  - `CHEBI:5864` ifosfamide

## Core literature used in the YAML

### Disease definition and subtype context

- `PMID:24470531` Farid et al. 2014 review
  - Used for disease definition, NF1/sporadic/radiation-associated subtype
    framing, and poor-prognosis treatment context.
  - Key quote used: "In 50% of cases, they occur in the context of
    neurofibromatosis type I ... the remainder arise sporadically or following
    radiation therapy."

- `PMID:38954182` Somaiah et al. 2024 review
  - Used for current overview of anatomy, spindle-cell identity, surgical role,
    and the absence of a targeted standard of care.

### Core conventional MPNST mechanism

- `PMID:36598417` Cortes-Ciriano et al. 2023
  - Key evolutionary paper for ordering events:
    `NF1` biallelic loss -> `CDKN2A`/`TP53` +/- `PRC2` loss -> extensive SCNAs.
  - Also supports the H3K27me3-loss branch as a distinct evolutionary path.

- `PMID:29118384` Brohl et al. 2017
  - Used for recurrent `NF1`, `SUZ12`, `EED`, `TP53`, and `CDKN2A` lesions and
    for convergent Ras-pathway activation.

- `PMID:30722027` Pemov et al. 2019
  - Used to keep the progression model atomic:
    `CDKN2A/B` deletion is an early step in PN -> atypical neurofibroma
    transition, whereas PRC2 loss is later.

- `PMID:25240281` Lee et al. 2014
  - Key PRC2 paper used for:
    - recurrent `SUZ12` / `EED` inactivation across etiologies
    - `H3K27me3` loss
    - homeobox/developmental gene derepression
    - cell-growth rescue after PRC2 restoration

### Diagnostic biomarker / pathology

- `PMID:26645727` Prieto-Granada et al. 2016
  - Used for H3K27me3-loss diagnostic performance and the fact that epithelioid
    tumors retain H3K27me3.

- `PMID:31175328` Marchione et al. 2019
  - Used for the more specific `H3K27me2`-loss biomarker.

### Histologic subtype-specific biology

- `PMID:25602794` Jo and Fletcher 2015
  - Used for epithelioid subtype morphology, superficial distribution, diffuse
    S100 positivity, and infrequent NF1 association.

- `PMID:30864974` Schaefer et al. 2019
  - Used for subtype-scoped `SMARCB1` inactivation in epithelioid MPNST.

- `PMID:17149968` Stasik and Tawfik 2006
  - Used for malignant triton tumor as the rhabdomyoblastic differentiation
    facet of MPNST.

### Clinical phenotype and treatment

- `PMID:36752552` Donaldson et al. 2023
  - Used for enlarging mass, pain, and motor/sensory deficit presentation.

- `PMID:16033085` Friedrich et al. 2005
  - Used for NF1 surveillance language around atypical pain, tumor growth, and
    neurologic deficits as malignant-warning features.

- `PMID:27281262` Bishop et al. 2018
  - Used for combined surgery plus radiotherapy and local-control outcomes.

- `PMID:40795877` Jansma et al. 2025
  - Used to refine radiotherapy interpretation: lower local-recurrence risk in
    sporadic disease, unclear benefit in NF1-associated disease.

- `PMID:28546782` Hirbe et al. 2017
  - Used for direct human evidence that ifosfamide/anthracycline-based
    chemotherapy can induce response.

## Curation-specific decisions

- I did **not** split epithelioid MPNST into its own disease file even though it
  has a distinct `SMARCB1` branch. Under the `#1198` rule set, that would only
  be warranted if it needed a genuinely separate disease-level mechanism graph.
  Here, subtype-scoped mechanism and genetic nodes are sufficient.
- I did **not** create separate files for NF1-associated or radiation-associated
  MPNST. Those are important subtype facets, but they still sit inside the same
  parent MPNST mechanism graph.
- I kept the conventional pathophysiology nodes atomic:
  `NF1 Biallelic Inactivation`, `Ras Pathway Hyperactivation`, `CDKN2A/B Loss`,
  `TP53 Pathway Loss`, `PRC2 Core Complex Inactivation`, `H3K27 Trimethylation Loss`,
  `Developmental Gene Derepression`, and `Copy-Number Driven Genomic Instability`.
