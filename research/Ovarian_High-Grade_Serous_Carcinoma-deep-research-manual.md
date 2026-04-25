# Ovarian High-Grade Serous Carcinoma Manual Research Notes

Date: 2026-04-12

## Scope

This note distills the literature and modeling decisions used for the
`kb/disorders/Ovarian_High-Grade_Serous_Carcinoma.yaml` curation.

## Cancer Modeling Decisions

- Applied issue `#1198` guidance before rewriting the disease entry.
- Kept **one disease-level mechanism graph** for HGSOC instead of splitting BRCA-associated,
  HRD-positive, or platinum-response contexts into separate dismech pages.
- Kept the disease anchor **MONDO-first**. OLS search returned `MONDO:0005211`
  (`ovarian serous adenocarcinoma`) as the closest MONDO concept, but not a separate
  high-grade ovarian serous MONDO leaf.
- Used **NCIT** to recover oncology specificity where the schema supports it:
  `NCIT:C105555` Ovarian High Grade Serous Adenocarcinoma for disease-alignment context,
  `NCIT:C213446` High Grade Serous Adenocarcinoma and `NCIT:C126449` Serous Tubal
  Intraepithelial Carcinoma for histopathology, and NCIT drug/biomarker terms for
  olaparib, bevacizumab, carboplatin, paclitaxel, HRD, CCNE1 amplification, CA-125,
  and HE4.
- Treated subtype handling as a **flat facet axis** rather than as separate causal programs.
  In the YAML, BRCA-associated versus BRCA-wild-type HGSOC is represented as a disease
  facet inside one graph, not as separate disease pages. I did not force a
  `subtype_term` for the BRCA-associated facet once review confirmed that
  `MONDO:0003582` denotes a predisposition syndrome rather than a carcinoma subtype.
- Kept pathophysiology nodes **atomic**. The old entry bundled origin, TP53, HRD, and
  genomic instability into broad blocks; the revised entry separates tubal origin,
  early TP53-mutant precursor state, STIC, HRD, copy-number instability, and CCNE1-linked
  replication stress.
- Important schema constraint: the current dismech schema exposes MONDO/ICD disease mapping
  containers, but not a dedicated `ncit_mappings` disease slot. Because of that, NCIT
  disease alignment is recorded in the curation notes and expressed structurally through
  histopathology, biomarker, regimen, and therapeutic-agent terms.

## Ontology Grounding Used

- Disease anchor: `MONDO:0005211` ovarian serous adenocarcinoma
- Disease-level oncology counterpart: `NCIT:C105555` Ovarian High Grade Serous Adenocarcinoma
- Precursor lesion: `NCIT:C126449` Serous Tubal Intraepithelial Carcinoma
- Defining histology: `NCIT:C213446` High Grade Serous Adenocarcinoma
- Key biomarker state: `NCIT:C120465` Homologous Recombination Deficiency
- Key copy-number biomarker: `NCIT:C36682` CCNE1 Gene Amplification
- Candidate regimen concept not retained in final YAML because the current `RegimenTerm`
  enum rejected it during validation: `NCIT:C63402` Carboplatin/Paclitaxel Regimen

## Primary Claims Used In YAML

### 1. Tubal origin and precursor sequence

- `PMID:33011111` supports the tubal-origin model and the TP53-to-STIC-to-HGSOC sequence.
- Used for:
  - tubal cell-of-origin node
  - TP53 as earliest recurrent lesion
  - STIC as precursor histopathology and pathophysiology node
- Evidence type in YAML: `OTHER`
  - This paper is a review/synthesis, not a direct cohort study.

### 2. Near-universal TP53 mutation and core genomic architecture

- `PMID:21720365` (TCGA) remains the foundational human study for HGSOC.
- Used for:
  - TP53 near-universality
  - HRD in about half of tumors
  - recurrent BRCA1/2 alteration
  - recurrent CCNE1 amplification
  - focal copy-number burden
- Evidence type in YAML: `HUMAN_CLINICAL`
  - The study is based on clinically annotated human HGSOC tumors.

### 3. Pre-ciliated tubal epithelial susceptibility

- `PMID:39366996` adds recent mechanistic depth beyond the older secretory-cell-only
  origin model.
- Used for:
  - the atomic node describing a cancer-prone pre-ciliated tubal epithelial state
- Evidence type in YAML: `MODEL_ORGANISM`
  - The key mechanistic evidence is mouse-based lineage tracing and transformation work.

### 4. Copy-number-driven disease framing

- `PMID:36804485` gives a compact recent synthesis of the defining HGSOC genomic pattern:
  universal TP53 alteration plus widespread copy-number change.
- Used for:
  - the copy-number-driven chromosomal instability node
- Evidence type in YAML: `OTHER`
  - This paper is a review.

### 5. Clinical presentation and first-line management context

- `PMID:40690248` is a recent JAMA review of ovarian cancer.
- Used for:
  - ascites, abdominal pain, abdominal distention presentation context
  - cytoreductive surgery and carboplatin/paclitaxel first-line treatment framing
- Evidence type in YAML: `OTHER`
  - The paper is a review and not HGSOC-exclusive, but it is recent and clinically
    aligned with HGSOC-dominant advanced ovarian cancer care.

### 6. Maintenance olaparib

- `PMID:36082969` (SOLO1 7-year follow-up) is the clearest long-term randomized evidence
  tied to the BRCA-associated HGSOC facet.
- Used for:
  - olaparib maintenance treatment entry
- Evidence type in YAML: `HUMAN_CLINICAL`

### 7. Bevacizumab benefit enrichment

- `PMID:36252167` (GOG-0218 validation) supports biomarker-informed bevacizumab use.
- Used for:
  - bevacizumab treatment entry
- Evidence type in YAML: `HUMAN_CLINICAL`

### 8. CA-125 and HE4 biomarker context

- `PMID:30917847` supports CA-125 and HE4 as practical biomarker entries.
- Evidence type in YAML: `OTHER`
  - Review article summarizing diagnostic biomarker performance.

## Literature Not Fully Expanded Into YAML

- The existing `research/Ovarian_High-Grade_Serous_Carcinoma-deep-research-falcon.md`
  already captures additional 2023-2025 literature on dissemination timing, spheroid
  biology, and tumor microenvironment variation.
- I did not turn every one of those claims into YAML because the issue called for a
  coherent disease-level curation, not a maximal import of every published HGSC detail.
- In particular, dissemination-mode, stromal subtype, and immune-ecosystem papers were
  treated as background unless they cleanly sharpened an atomic disease mechanism node.

## Remaining Curation Judgment Calls

- The subtype list is intentionally narrow. Under the `#1198` guidance, I did not encode
  multiple orthogonal axes (BRCA status, HRD status, stage, platinum sensitivity, site of
  spread) as if they were one subtype tree.
- The current schema does not yet provide a structured disease-level NCIT mapping slot.
  If that slot is added later, `NCIT:C105555` should be promoted from curation notes into
  a first-class disease mapping.
- The current `RegimenTerm` dynamic enum also rejected `NCIT:C63402` and
  `NCIT:C160097`, so the final YAML keeps oncology specificity through NCIT therapeutic
  agents rather than regimen descriptors.
