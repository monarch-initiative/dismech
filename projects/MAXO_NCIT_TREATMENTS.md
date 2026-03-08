# MAXO vs NCIT for Treatment Descriptors

Date: 2026-02-11

## Goal

Assess whether NCIT is a better fit than MAXO for treatment descriptors, using:

- `output/tabular/sections/treatments/descriptors.tsv`
- core rows where `path = treatment_term`

## Correction Note

The first analysis pass had a lookup bug: NCIT retrieval used `oaklib` `basic_search` with unnormalized case, and this adapter is case-sensitive.

Example (verified):

- `Genetic counseling` with naive `basic_search` -> no hit
- `Genetic Counseling` -> `NCIT:C15240`
- `runoak -i sqlite:obo:ncit info 'l^Genetic Counsel'` confirms NCIT entries exist

This report is based on a corrected OAK pass that title-cases lookup queries before search.

## Data Snapshot

- Treatment rows (`path=treatment_term`): **1,046**
- Unique treatment names: **708**
- MAXO labels are frequently generic:
  - `pharmacotherapy`: 443
  - `surgical procedure`: 150
  - `chemotherapy`: 59
  - `supportive care`: 59
  - `radiation therapy`: 41

## Method (Corrected)

For each treatment name:

1. Query NCIT via OAK (`sqlite:obo:ncit`) using title-cased name.
2. Rank returned NCIT candidates by lexical similarity to treatment name.
3. Compare NCIT-vs-current MAXO label using the same score function:
   - sequence similarity
   - token overlap
   - description token overlap

This is still a triage heuristic, not final ontology curation.

Command-line OAK spot checks (agentic lookup with `l~` patterns) were used to verify disputed terms:

- `uv run runoak -i sqlite:obo:ncit info 'l~Fecal microbiota transplantation'` -> `NCIT:C118643`
- `uv run runoak -i sqlite:obo:ncit info 'l~Genetic counseling'` -> `NCIT:C15240`

Artifacts:

- `tmp/ncit_treatment_candidates_casefix.tsv`
- `tmp/ncit_treatment_summary_casefix.txt`

## Quantitative Results (Corrected)

Across 1,046 treatment rows:

- NCIT candidate found: **412**
- No NCIT candidate found: **634**

Delta (`ncit_score - maxo_score`):

- NCIT better (`> 0.05`): **300**
- MAXO better (`< -0.05`): **601**
- Tie (`|delta| <= 0.05`): **145**

Key caveat:

- For rows with NCIT hits (412), NCIT was **never worse** by this heuristic:
  - NCIT better: 300
  - Tie: 112
  - MAXO better: 0
- MAXO-better rows are effectively rows where NCIT had no candidate.

At unique-treatment-name level:

- NCIT hit for **222 / 708** names
- No NCIT hit for **486 / 708** names

## Pattern Readout

### Where NCIT adds value

NCIT strongly improves specificity for many concrete drugs/procedures currently under broad MAXO actions:

- `Cannabidiol` -> `NCIT:C118452 Cannabidiol`
- `Dapsone` -> `NCIT:C415 Dapsone`
- `Thyroidectomy` -> `NCIT:C51648 Thyroidectomy`
- `Midostaurin` -> `NCIT:C1872 Midostaurin`
- `Sentinel Lymph Node Biopsy` -> `NCIT:C15667 Sentinel Lymph Node Biopsy`
- `Vancomycin` -> `NCIT:C925 Vancomycin`

### Where MAXO remains stronger

Many intervention phrasings are still hard to map cleanly to a single NCIT concept:

- `Speech therapy`
- `Speech and language therapy`
- `MRD-guided therapy`
- multi-agent/free-text regimen strings (e.g., `Gemcitabine plus Cisplatin plus Durvalumab`)

Notes:

- `Fecal microbiota transplantation` is **not** a no-hit; NCIT has `NCIT:C118643`.
- `Genetic counseling` is **not** a no-hit; NCIT has `NCIT:C15240`.
- `Dialysis` is present in NCIT (`NCIT:C15221 ! Dialysis`), so prior misses were retrieval failures.
- `Gene therapy` is present in NCIT (`NCIT:C15238 ! Gene Therapy`), so prior misses were retrieval failures.
- `Vitamin supplementation` is present in NCIT (`NCIT:C210732 ! Vitamin Supplement`); so vitamin-related misses in this pass are a query/granularity issue, not clear ontology absence.

## Recommendation

General conclusion remains:

- Keep **MAXO primary** for `treatment_term` (intervention/action semantics).
- Use **NCIT as a secondary specificity layer** when a clear concept exists (drug/procedure/regimen detail).
- Favor NCIT in post-composition (`qualifier_therapeutic_agent`) and/or additional mappings, not wholesale replacement of MAXO.

## Practical Next Step

Build a curation queue from `tmp/ncit_treatment_candidates_casefix.tsv`:

- `ncit_candidate_count > 0`
- `delta > 0.25`
- prioritize rows whose MAXO label is generic (`pharmacotherapy`, `surgical procedure`, etc.)

## Manual OAK Curation Progress (Agentic Search)

I started a term-by-term manual curation pass using command-line OAK and explicit query trails in:

- `projects/MAXO_NCIT_TREATMENTS_MANUAL.tsv`

Current progress:

- curated names: **233 / 708**
- `MATCH`: **125**
- `NEAR_MATCH`: **69**
- `NO_MATCH`: **39**
- remaining `PENDING`: **475**

Coverage is front-loaded on highest-frequency treatment labels (to maximize row coverage early):

- weighted rows covered so far (sum of `count`): **571**

Update in this pass:

- additional curated names this run: **+100**

Examples of corrected high-impact mappings from manual pass:

- `Anticoagulation` -> `NCIT:C63341` (`Anticoagulation Therapy`)
- `Radioiodine Therapy` -> `NCIT:C157968` (`Radioactive Iodine Therapy`)
- `Risk-Reducing Mastectomy` -> `NCIT:C94445` (`Prophylactic Mastectomy`)
- `Intravenous Immunoglobulin (IVIG)` -> `NCIT:C121331` (`Intravenous Immunoglobulin Therapy`)
- `CAR-T Cell Therapy` -> `NCIT:C126102` (`Chimeric Antigen Receptor T-Cell Therapy`)
- `Fecal Microbiota Transplantation` -> `NCIT:C118643`
- `Renal Dialysis` -> `NCIT:C15221` (`Dialysis`)

No-match patterns (so far) are mostly free-text composition rather than ontology absence:

- conjunction/disjunction regimens (`A plus B`, `A or B`)
- strategy phrases (`MRD-guided therapy`)
- service/support formulations lacking direct NCIT treatment classes.

Case/format variants (e.g., capitalization-only differences) are being propagated from already-manualized rows and explicitly marked in `queries_tried` as `propagated_case_variant_from:<label>`.
