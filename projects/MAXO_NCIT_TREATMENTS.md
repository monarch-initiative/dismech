---
title: MAXO vs NCIT for Treatment Descriptors
status: IN_PROGRESS
description: 'Date: 2026-02-11'
---

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

- `projects/MAXO_NCIT_TREATMENTS/MANUAL.tsv`

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

## Applied to the KB (2026-07-02)

The `MATCH` and `NEAR_MATCH` rows curated in `MANUAL.tsv` so far were applied
to every `kb/disorders/*.yaml` and `kb/modules/*.yaml` treatment whose `name`
matched a curated `section_name` and whose `treatment_term.term` still held
the original MAXO id/label recorded as `maxo_label`:

- Curated names eligible (`MATCH` + `NEAR_MATCH`): **194**
- Treatment entries updated: **848** across **640** files
- Only `treatment_term.term.id` / `term.label` were changed to the curated
  NCIT id/label. `preferred_term` was updated to the new NCIT label only when
  it previously mirrored the generic MAXO label verbatim (781 entries); the
  67 entries where a curator had already written a more specific
  `preferred_term` (e.g. "Foramen magnum decompression", "Cranial Vault
  Surgery") were left untouched, since `preferred_term` is allowed to be more
  specific than `term.label` per the curation conventions.
- All 159 unique NCIT ids used were spot-checked against
  `sqlite:obo:ncit` (`runoak -i sqlite:obo:ncit labels <ids>`); every id/label
  pair matched the canonical NCIT label except one (`NCIT:C98085`, corrected
  in `MANUAL.tsv` from "GLP-1 Mimetics" to the canonical "GLP-1 Mimetic" —
  this row was never actually applied to a KB file, since its `maxo_label`
  ("pharmacotherapy") does not correspond to an actual MAXO id used in the
  KB).
- `NO_MATCH` (39) and `PENDING` (475) rows were **not** touched — MAXO
  remains the term for those treatment names, consistent with the
  recommendation above to keep MAXO primary except where a clearly better
  NCIT concept exists.
- Schema (`linkml-validate --target-class Disease`) was re-run on all 640
  changed files after the swap: **640/640 passed, 0 failures**.

Remaining work: continue the manual OAK curation pass on the 475 `PENDING`
names, then re-run this apply step to pick up newly curated `MATCH`/
`NEAR_MATCH` rows.

## Post-review correction (2026-07-02)

The automated PR review (ai4c-agent) on PR #5135 flagged 4 `NEAR_MATCH` rows
whose NCIT concept is a substance or qualifier/adjective rather than a
clinical-intervention action, and therefore likely does not satisfy the
`TreatmentActionTerm` dynamic enum's `reachable_from NCIT:C25218` constraint:

- `Leukotriene Modifier` -> `NCIT:C608` (Leukotriene) is the endogenous
  mediator being *blocked*, not the modifier action — semantically inverted.
- `Platinum Chemotherapy` / `Platinum-Based Chemotherapy` -> `NCIT:C25620`
  (Platinum-Based) is a qualifier/adjective, not an action (9 entries, 9 files).
- `Multidisciplinary Care` -> `NCIT:C94845` (Multidisciplinary) is an
  adjective, not a care action (3 entries).
- `Salt Supplementation` -> `NCIT:C29974` (Sodium Chloride) is the chemical
  agent, not the supplementation action (1 entry).

All 14 affected treatment entries (across 13 files) were reverted to their
original MAXO id/label/preferred_term, `linkml-validate` re-passed on all 14
files, and the corresponding `MANUAL.tsv` rows were changed from
`NEAR_MATCH` to `NO_MATCH` with notes explaining the reversion. Updated
counts: `MATCH` 125, `NEAR_MATCH` 64, `NO_MATCH` 44, `PENDING` 475.

## Systematic TreatmentActionTerm enum audit (2026-07-02, same day)

CI's real `linkml-term-validator` pass (with the OAK-backed dynamic enum
expansion the earlier local `linkml-validate`-only check did not exercise)
failed on `NCIT:C210732` (Vitamin Supplement, not reachable from
`NCIT:C25218`). Since the CI loop stops at the first validation failure, a
full proactive audit was run instead of fixing files one CI failure at a
time: every unique NCIT id then in use across the `MATCH`/`NEAR_MATCH` rows
(155 ids after the prior correction) was checked via OAK
(`adapter.ancestors(id, predicates=["rdfs:subClassOf"], reflexive=True)`)
against the schema's `TreatmentActionTerm` `reachable_from` roots
(`NCIT:C25218` / `MAXO:0000001`).

**93 of 155 unique NCIT ids (101 of 189 MATCH/NEAR_MATCH rows) failed** —
overwhelmingly cases where a treatment's *name* happened to be a specific
drug/agent (e.g. "Rituximab", "Imatinib", "Trifarotene") and the curation
queue matched it to the NCIT concept for that drug/substance itself, rather
than the clinical-intervention *action* the `treatment_term` slot requires.
Per the dismech convention, the specific agent belongs in
`therapeutic_agent` (already correctly populated in most of these entries
before the swap), while `treatment_term` should stay on the generic action
(`NCIT:C15986` Pharmacotherapy, `MAXO:0000647` chemotherapy, etc.). A
smaller set were drug-class/substance/device concepts (Corticosteroid,
Beta-Adrenergic Agonist, Hearing Aid, Sunglasses, Brace, Vitamin Supplement,
Actinotherapy, ...).

All 57 affected KB treatment entries (45 files) were reverted to their
original pre-swap MAXO id/label/preferred_term (sourced from the pristine
git blob before the first swap commit, not re-derived from `maxo_label`
text, to guarantee exactness). The corresponding 101 `MANUAL.tsv` rows were
changed to `NO_MATCH` with notes recording the failed reachability check.

One collateral bug surfaced and was fixed during this pass: a handful of
entries (`Acne_Vulgaris.yaml` x3, `Glioblastoma_IDH_Wildtype.yaml` x1) had a
pre-existing `therapeutic_agent` that already correctly cited the same NCIT
drug id the treatment_term swap had also (incorrectly) copied in; a
regex-based revert pass matched the *first* occurrence of that id in the
entry block, which was ambiguous when both fields shared it. These 4
`therapeutic_agent` values were restored from the pristine pre-swap blob and
verified against it programmatically (0 discrepancies across all 45 touched
files). `linkml-term-validator` (the real CI check, not the schema-only
`linkml-validate`) was re-run per-file to confirm.

Updated counts: `MATCH` 59, `NEAR_MATCH` 29, `NO_MATCH` 145, `PENDING` 475.

**Lesson for future passes on this queue:** verify `reachable_from`
reachability via OAK for every candidate NCIT id *before* applying it, and
prefer `just validate` / `linkml-term-validator` (which exercises the real
dynamic enum expansion) over bare `linkml-validate` for local pre-push
checks — the two can disagree on dynamic-enum-constrained fields.
