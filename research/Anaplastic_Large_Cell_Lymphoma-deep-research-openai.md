---
provider: openai
model: gpt-5
curation_date: "2026-04-13"
disease_name: Anaplastic Large Cell Lymphoma
issue: 1209
---

# Anaplastic Large Cell Lymphoma Curation Notes

## Modeling Decision

This curation follows the cancer modeling guidance from dismech issue `#1198` and
the Wilms tumor pattern:

- The dismech page is the disease-level mechanism graph for ALCL, not a one-page-per-ontology-subclass expansion.
- `disease_term` stays MONDO-first at `MONDO:0020325` (`anaplastic large cell lymphoma`).
- Major ALCL entities are represented as flat subtype facets under one page:
  - Systemic ALK-positive
  - Systemic ALK-negative
  - Primary cutaneous
  - Breast implant-associated
- Genetic subgroups such as `DUSP22`-rearranged and `TP63`-rearranged ALK-negative
  ALCL are modeled as mechanism/genetic facts inside the unified disease page,
  not as separate dismech pages.
- Current schema only provides `Subtype.subtype_term` as a MONDO-grounded slot
  and does not expose a disease-level `ncit_mappings` slot. Because of that,
  NCIT grounding was carried through histopathology findings, biomarkers, and
  treatment regimens/agents rather than by inventing non-schema subtype mapping
  structures.

## Ontology Anchors

### Disease

- MONDO disease anchor: `MONDO:0020325` `anaplastic large cell lymphoma`
- NCIT companion cancer concept: `NCIT:C3720` `Anaplastic Large Cell Lymphoma`

### MONDO subtype anchors used in YAML

- `MONDO:0017602` `ALK-positive anaplastic large cell lymphoma`
- `MONDO:0017603` `ALK-negative anaplastic large cell lymphoma`
- `MONDO:0017598` `primary cutaneous anaplastic large cell lymphoma`
- `MONDO:0850112` `breast implant-associated anaplastic large cell lymphoma`

### NCIT companion subtype concepts used in interpretation

- `NCIT:C37195` `Systemic Anaplastic Large Cell Lymphoma, ALK-Positive`
- `NCIT:C37196` `Systemic Anaplastic Large Cell Lymphoma, ALK-Negative`
- `NCIT:C6860` `Primary Cutaneous Anaplastic Large Cell Lymphoma`
- `NCIT:C139012` `Breast Implant-Associated Anaplastic Large Cell Lymphoma`

### Histopathology / biomarker / treatment grounding

- `NCIT:C39679` `Hallmark Cell`
- `NCIT:C193484` `CD30 Antigen [Presence] in Tissue by Immune Stain`
- `NCIT:C38906` `Tumor Necrosis Factor Receptor Superfamily Member 8`
- `NCIT:C81946` `ALK Fusion Protein Expression`
- `NCIT:C66944` `Brentuximab Vedotin`
- `NCIT:C159558` `CHP-Brentuximab Vedotin Regimen`
- `NCIT:C160013` `Crizotinib Regimen`

## PMID-Backed Evidence Used

### Disease framing and subtype axes

- `PMID:40565334`
  - Quote: `Anaplastic Large Cell Lymphoma (ALCL) represents a diverse group of mature T-Cell Lymphomas unified by strong CD30 expression but with different molecular and clinical subtypes.`
  - Use: disease-level definition and justification for one unified ALCL page.
- `PMID:40565334`
  - Quote: `ALCL comprises four major entities: systemic ALK-positive ALCL, systemic ALK-negative ALCL, Breast Implant-Associated ALCL (BIA-ALCL), and primary cutaneous ALCL.`
  - Use: flat subtype facet structure.
- `PMID:24894770`
  - Quote: `Thus, ALK-negative ALCL is a genetically heterogeneous disease with widely disparate outcomes following standard therapy.`
  - Use: ALK-negative modeled as one subtype with internal genetic heterogeneity, not split into multiple pages.

### Histopathology and diagnosis

- `PMID:28975123`
  - Quote: `Histologically, all the subtypes showed pleomorphic and "hallmark" cells with strong CD30 expression and variable loss of T-cell antigens.`
  - Use: hallmark-cell histopathology and diffuse CD30-positive tissue phenotype.
- `PMID:28975123`
  - Quote: `Diagnosis of ALCL is based on recognizing the key morphological features, especially the presence of "hallmark" cells.`
  - Use: diagnostic emphasis on morphology.
- `PMID:28975123`
  - Quote: `The inclusion of CD30 in the initial IHC panel will help identify LCA negative cases and avoid misdiagnosis.`
  - Use: diagnostic workflow and IHC panel design.
- `PMID:35941721`
  - Quote: `Together with previous data, these findings support a 4-marker immunohistochemistry algorithm using ALK, LEF1, TIA1, and p63 for genetic subtyping of ALCL.`
  - Use: ancillary subtype-specific diagnostic testing.

### Mechanism notes kept atomic in YAML

- `PMID:29617304`
  - Quote: `ALK is rearranged in approximately 80% of systemic ALCL cases with one of its partner genes, most commonly NPM1`
  - Use: discrete `ALK Fusion Oncogene Formation` node.
- `PMID:11850821`
  - Quote: `We show here that expression of activated ALK induces the constitutive phosphorylation of Stat3 in transfected cells as well as in primary human ALCLs.`
  - Use: separate `ALK-Driven STAT3 Activation` node.
- `PMID:11850821`
  - Quote: `These studies support a pathogenic mechanism whereby stimulation of anti-apoptotic signals through activation of Stat3 contributes to the successful outgrowth of ALK positive tumor cells.`
  - Use: separate `BCL2L1-Mediated Apoptosis Resistance` node.
- `PMID:19088198`
  - Quote: `NPM/ALK induces CD274 expression by activating its key signal transmitter, transcription factor STAT3.`
  - Use: separate `PD-L1-Mediated Immune Evasion` node.
- `PMID:34572893`
  - Quote: `Additionally, systemic ALK- ALCL-apart from DUSP22-rearranged cases-harbors JAK1 and/or STAT3 mutations that result in the activation of the JAK/STAT signaling pathway.`
  - Use: subtype-scoped `JAK/STAT3 Pathway Alteration in ALK-Negative ALCL`.
- `PMID:34382383`
  - Quote: `Consistent with the genomic data, transcriptome analysis uncovered upregulation of signal transduction routes associated with the PI-3-K, MAPK and G-protein pathways (e.g., ERK, phospholipase C, AKT).`
  - Use: distinct primary-cutaneous signaling node rather than collapsing all non-ALK biology together.

### Phenotypes and treatment

- `PMID:37655119`
  - Quote: `This lymphoma has a median age of 34 years, is more common in males, and is in advanced stage at the time of diagnosis in most patients.`
  - Use: advanced-stage presentation phenotype for systemic ALK-positive disease.
- `PMID:24346900`
  - Quote: `Primary cutaneous anaplastic large-cell lymphoma is part of the spectrum of CD30+ lymphoproliferative cutaneous processes, characterized by single or multifocal nodules that ulcerate, are autoregressive and recurrent.`
  - Use: skin-nodule phenotype for primary cutaneous ALCL.
- `PMID:38102324`
  - Quote: `Breast implant-associated anaplastic large cell lymphoma (BIA-ALCL) is a subtype of ALCL that arises as a seroma or a mass in the capsule surrounding textured breast implants.`
  - Use: seroma and capsule-mass phenotypes for BIA-ALCL.
- `PMID:30914464`
  - Quote: `In November 2018, the U.S. Food and Drug Administration (FDA) approved brentuximab vedotin (BV) for the treatment of adult patients with previously untreated systemic anaplastic large cell lymphoma`
  - Use: frontline brentuximab vedotin plus CHP.
- `PMID:28974506`
  - Quote: `These final results, which demonstrated ... durable remissions in a subset of patients with relapsed or refractory systemic ALCL, provide evidence that single-agent brentuximab vedotin may be a potentially curative treatment option.`
  - Use: relapsed/refractory brentuximab vedotin.
- `PMID:37549532`
  - Quote: `CONCLUSION: Crizotinib shows efficacy and an acceptable safety profile in ALK+ ALCL relapsed/refractory patients.`
  - Use: targeted ALK inhibition.
- `PMID:26628470`
  - Quote: `Patients who underwent a complete surgical excision that consisted of total capsulectomy with breast implant removal had better OS (P = .022) and EFS (P = .014)`
  - Use: surgery-first management for BIA-ALCL.

## Why Separate Pages Were Not Created

Separate disease files were not created for ALK-positive ALCL, ALK-negative
ALCL, primary cutaneous ALCL, or BIA-ALCL because:

- the user explicitly requested application of the `#1198` cancer-guideline pattern;
- ALCL is represented in current disease ontology usage as one disease family with
  major subtype entities;
- the important modeling burden here is subtype-scoped mechanism and treatment
  separation inside one page, not proliferating disease pages; and
- only some branches, especially ALK-positive systemic disease and cutaneous/BIA
  disease, show clearly different mechanistic programs, which are captured by
  atomic nodes and subtype-scoped evidence inside the single page.

## Cached References Added for This Slice

- `PMID:40565334`
- `PMID:29617304`
- `PMID:37655119`
- `PMID:24894770`
- `PMID:35941721`
- `PMID:34382383`
- `PMID:34572893`
- `PMID:24404580`
- `PMID:19088198`
- `PMID:11850821`
- `PMID:30914464`
- `PMID:28974506`
- `PMID:37549532`
- `PMID:24346900`
- `PMID:26628470`
- `PMID:38102324`
