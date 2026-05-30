# CKD/PKD Class A Surrogacy Provenance — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add cited, verified Class A surrogacy provenance to the three mapped kidney rows in the FDA surrogate endpoint table, plus disease-side `BiomarkerReadout` bridges in the CKD and PKD disorder files — no schema change.

**Architecture:** For each of three `SurrogateEndpoint` rows, populate `clinical_benefit` (plain English) and append one verified `EvidenceItem` whose `snippet` is an exact substring of a freshly fetched PubMed abstract. Mirror each row with a `BiomarkerReadout` in the corresponding disorder file carrying `regulatory_endpoint_refs`. All quantitative surrogacy numbers appear only as verbatim quotes.

**Tech Stack:** dismech LinkML KB; `just` targets (`fetch-reference`, `validate`, `validate-references`, `validate-terms-file`); pytest; PubMed MCP / web for PMID discovery.

**Spec:** `docs/superpowers/specs/2026-05-18-ckd-pkd-surrogacy-evidence-design.md`

---

## Pre-flight (read once, do not skip)

- `references_cache/PMID_*.md` files are created ONLY by `just fetch-reference`. Never hand-write or hand-edit them.
- A `snippet:` must be an exact substring of the cached abstract body. If the statistic is not in the abstract verbatim, omit the number and keep `clinical_benefit` qualitative.
- Do not change `endpoint_validation_level`, `clinical_benefit_linkage`, `approval_type`, or `mapping_status` on any row.
- Use targeted `git add` only — never `git add -A`/`.`.
- Branch is `feat/endpoints-computational` (worktree). Stay on it.

## File map

- Modify: `kb/surrogate_endpoints/fda_surrogate_endpoints.yaml` — rows `FDA-SE-adult-noncancer-012`, `FDA-SE-pediatric-noncancer-008`, `FDA-SE-adult-noncancer-090`
- Modify: `kb/disorders/Chronic_Kidney_Disease.yaml` — add `biomarker_readouts`
- Modify: `kb/disorders/Polycystic_Kidney_Disease.yaml` — add `biomarker_readouts`
- Create (via `just fetch-reference` only): `references_cache/PMID_*.md`

---

## Task 1: Discover and fetch the CKD eGFR surrogacy reference

**Files:**
- Create: `references_cache/PMID_<verified>.md` (via just target only)

- [ ] **Step 1: Find the PMID for the primary CKD eGFR trial-level surrogacy analysis**

Use the PubMed MCP (`mcp__claude_ai_PubMed__search_articles`) or web search to locate the PMID for:

> Inker LA, Heerspink HJL, Tighiouart H, et al. "GFR Slope as a Surrogate End Point for Kidney Disease Progression in Clinical Trials: A Meta-Analysis of Treatment Effects of Randomized Clinical Trials." J Am Soc Nephrol. 2019.

Fallback candidate if the abstract above lacks a quotable statistic:

> Levey AS, Inker LA, Matsushita K, et al. "GFR decline as an end point for clinical trials in CKD: a scientific workshop sponsored by the National Kidney Foundation and the US Food and Drug Administration." Am J Kidney Dis. 2014.

Confirm the returned PMID's title, first author, journal, and year match before proceeding.

- [ ] **Step 2: Fetch and cache the abstract**

Run: `just fetch-reference PMID:<verified>`
Expected: `references_cache/PMID_<verified>.md` created with YAML frontmatter and abstract body.

- [ ] **Step 3: Verify the cache content matches the intended paper**

Run: `cat references_cache/PMID_<verified>.md`
Expected: title/abstract is the CKD GFR-slope/decline surrogacy analysis (mentions GFR slope or eGFR decline as a surrogate/end point and kidney failure / ESKD / treatment effects across RCTs). If it does not match, return to Step 1.

- [ ] **Step 4: Commit the cache file**

```bash
git add references_cache/PMID_<verified>.md
git commit -m "refs: cache CKD eGFR surrogacy reference (PMID:<verified>)"
```

---

## Task 2: Discover and fetch the PKD TKV reference

**Files:**
- Create: `references_cache/PMID_<verified>.md` (via just target only)

- [ ] **Step 1: Find the PMID for the PKD TKV prognostic-biomarker reference**

Use PubMed MCP / web to locate the PMID for:

> Irazabal MV, Rangel LJ, Bergstralh EJ, et al. "Imaging classification of autosomal dominant polycystic kidney disease: a simple model for selecting patients for clinical trials." J Am Soc Nephrol. 2015.

Fallback candidate:

> Perrone RD, Mouksassi MS, Romero K, et al. "Total Kidney Volume Is a Prognostic Biomarker of Renal Function Decline and Progression to End-Stage Renal Disease in Patients With Autosomal Dominant Polycystic Kidney Disease." Kidney Int Rep. 2017.

Confirm title/author/journal/year match.

- [ ] **Step 2: Fetch and cache the abstract**

Run: `just fetch-reference PMID:<verified>`
Expected: `references_cache/PMID_<verified>.md` created.

- [ ] **Step 3: Verify the cache content**

Run: `cat references_cache/PMID_<verified>.md`
Expected: abstract describes TKV/height-adjusted TKV as a prognostic biomarker for eGFR decline / progression to ESKD in ADPKD — NOT a validated treatment-efficacy surrogate. If mismatch, return to Step 1.

- [ ] **Step 4: Commit the cache file**

```bash
git add references_cache/PMID_<verified>.md
git commit -m "refs: cache PKD TKV prognostic-biomarker reference (PMID:<verified>)"
```

---

## Task 3: Curate the two CKD FDA rows

**Files:**
- Modify: `kb/surrogate_endpoints/fda_surrogate_endpoints.yaml` (rows `FDA-SE-adult-noncancer-012`, `FDA-SE-pediatric-noncancer-008`)

- [ ] **Step 1: Locate the two CKD rows**

Run: `grep -n "FDA-SE-adult-noncancer-012\|FDA-SE-pediatric-noncancer-008" kb/surrogate_endpoints/fda_surrogate_endpoints.yaml`
Note the line ranges so edits target the correct row blocks.

- [ ] **Step 2: Select an exact-substring snippet from the cached CKD abstract**

Run: `cat references_cache/PMID_<ckd>.md`
Choose one sentence (the one stating the surrogacy result / treatment-effect relationship) that you will copy verbatim. Copy it character-for-character.

- [ ] **Step 3: Edit row `FDA-SE-adult-noncancer-012`**

Within that row block (do not touch other slots), insert before `mapping_status:`:

```yaml
  clinical_benefit: >-
    Progression to kidney failure (end-stage kidney disease) and the
    composite of kidney failure, sustained >=40% eGFR decline, or death.
  evidence:
  - reference: PMID:<ckd>
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: "<exact sentence copied verbatim from references_cache/PMID_<ckd>.md>"
    explanation: >-
      NKF-FDA-EMA trial-level meta-analysis establishing change in
      GFR/eGFR as a surrogate end point predicting kidney-failure
      outcomes in CKD randomized trials.
```

- [ ] **Step 4: Edit row `FDA-SE-pediatric-noncancer-008`**

Apply the same `clinical_benefit` and `evidence` block (same PMID and verbatim snippet) within the pediatric row block, before its `mapping_status:`.

- [ ] **Step 5: Schema-validate**

Run: `just validate kb/surrogate_endpoints/fda_surrogate_endpoints.yaml`
Expected: PASS (no schema errors).

- [ ] **Step 6: Reference-validate**

Run: `just validate-references kb/surrogate_endpoints/fda_surrogate_endpoints.yaml`
Expected: PASS — snippet found as substring of `PMID_<ckd>.md`. If "Text part not found as substring", fix the snippet to be an exact copy (do not edit the cache).

- [ ] **Step 7: Commit**

```bash
git add kb/surrogate_endpoints/fda_surrogate_endpoints.yaml
git commit -m "feat(endpoints): add CKD eGFR clinical_benefit + verified surrogacy evidence"
```

---

## Task 4: Curate the PKD TKV FDA row

**Files:**
- Modify: `kb/surrogate_endpoints/fda_surrogate_endpoints.yaml` (row `FDA-SE-adult-noncancer-090`)

- [ ] **Step 1: Locate the row**

Run: `grep -n "FDA-SE-adult-noncancer-090" kb/surrogate_endpoints/fda_surrogate_endpoints.yaml`

- [ ] **Step 2: Select an exact-substring snippet from the cached PKD abstract**

Run: `cat references_cache/PMID_<pkd>.md`
Choose one verbatim sentence describing TKV/htTKV as a prognostic predictor of renal function decline / progression to ESKD.

- [ ] **Step 3: Edit row `FDA-SE-adult-noncancer-090`**

Insert before `mapping_status:` (note the deliberately weaker, prognostic-enrichment wording — TKV is NOT a validated efficacy surrogate):

```yaml
  clinical_benefit: >-
    Future decline in renal function and progression to end-stage renal
    disease; height-adjusted total kidney volume functions as a prognostic
    enrichment biomarker (reasonably likely to predict benefit), not a
    validated treatment-efficacy surrogate.
  evidence:
  - reference: PMID:<pkd>
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: "<exact sentence copied verbatim from references_cache/PMID_<pkd>.md>"
    explanation: >-
      Total kidney volume is qualified as a prognostic/enrichment
      biomarker for renal-function decline and progression to ESKD in
      ADPKD; supports the row's reasonably-likely validation level.
```

- [ ] **Step 4: Schema-validate**

Run: `just validate kb/surrogate_endpoints/fda_surrogate_endpoints.yaml`
Expected: PASS.

- [ ] **Step 5: Reference-validate**

Run: `just validate-references kb/surrogate_endpoints/fda_surrogate_endpoints.yaml`
Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add kb/surrogate_endpoints/fda_surrogate_endpoints.yaml
git commit -m "feat(endpoints): add PKD TKV clinical_benefit + verified prognostic-biomarker evidence"
```

---

## Task 5: Add the CKD disease-side BiomarkerReadout bridge

**Files:**
- Modify: `kb/disorders/Chronic_Kidney_Disease.yaml`

- [ ] **Step 1: Confirm the target pathophysiology node and top-level key order**

Run: `grep -n "^pathophysiology:\|^phenotypes:\|^- name: Nephron Loss" kb/disorders/Chronic_Kidney_Disease.yaml`
Expected: `Nephron Loss` exists as a pathophysiology node. Decide a valid top-level insertion point for a new `biomarker_readouts:` key (schema-allowed; place near `pathophysiology`).

- [ ] **Step 2: Add the `biomarker_readouts` block**

Add at top level:

```yaml
biomarker_readouts:
- target: Nephron Loss
  relationship: READOUT_OF
  direction: NEGATIVE
  endpoint_context: PROGNOSTIC
  regulatory_endpoint_refs:
  - FDA-SE-adult-noncancer-012
  - FDA-SE-pediatric-noncancer-008
  interpretation: >-
    Estimated GFR (and its reciprocal, serum creatinine) is a quantitative
    readout of cumulative nephron loss; lower/declining eGFR reflects more
    advanced functional nephron loss and predicts progression to kidney
    failure, which is why it is an FDA-recognized validated surrogate
    endpoint in CKD drug development.
  evidence:
  - reference: PMID:<ckd>
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: "<same verbatim sentence used in Task 3>"
    explanation: >-
      Trial-level meta-analysis linking change in GFR/eGFR to
      kidney-failure outcomes across CKD randomized trials.
```

Use `direction: NEGATIVE` only if the schema's direction enum is the association direction (lower eGFR ↔ more nephron loss); if validation rejects the value, run `grep -n "AssociationDirectionEnum\|direction:" src/dismech/schema/dismech.yaml` and use a permitted value.

- [ ] **Step 3: Schema-validate**

Run: `just validate kb/disorders/Chronic_Kidney_Disease.yaml`
Expected: PASS. If the `target` foreign-key or `direction`/`relationship` enum fails, correct to a schema-valid value and re-run.

- [ ] **Step 4: Reference- and term-validate**

Run: `just validate-references kb/disorders/Chronic_Kidney_Disease.yaml`
Run: `just validate-terms-file kb/disorders/Chronic_Kidney_Disease.yaml`
Expected: both PASS.

- [ ] **Step 5: Commit**

```bash
git add kb/disorders/Chronic_Kidney_Disease.yaml
git commit -m "feat(ckd): add eGFR BiomarkerReadout bridge to FDA surrogate rows"
```

---

## Task 6: Add the PKD disease-side BiomarkerReadout bridge

**Files:**
- Modify: `kb/disorders/Polycystic_Kidney_Disease.yaml`

- [ ] **Step 1: Resolve the real target pathophysiology node name**

Run: `grep -n "^pathophysiology:" kb/disorders/Polycystic_Kidney_Disease.yaml` then list node names:
`awk '/^pathophysiology:/{f=1;next}/^[a-z_]+:/{f=0}f&&/^- name:/{print}' kb/disorders/Polycystic_Kidney_Disease.yaml`
Pick the node representing cyst growth / progressive kidney enlargement / nephron loss. Record its exact `name:` string. Do NOT invent a node.

- [ ] **Step 2: Add the `biomarker_readouts` block**

```yaml
biomarker_readouts:
- target: "<exact existing node name from Step 1>"
  relationship: READOUT_OF
  direction: POSITIVE
  endpoint_context: PROGNOSTIC
  regulatory_endpoint_refs:
  - FDA-SE-adult-noncancer-090
  interpretation: >-
    Total kidney volume (height-adjusted) is an imaging readout of
    cumulative cyst burden and progressive kidney enlargement; larger and
    faster-growing TKV predicts steeper renal-function decline and earlier
    ESKD, supporting its use as a prognostic enrichment biomarker (not a
    validated efficacy surrogate) in ADPKD trials.
  evidence:
  - reference: PMID:<pkd>
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: "<same verbatim sentence used in Task 4>"
    explanation: >-
      TKV qualified as a prognostic biomarker for renal-function decline
      and progression to ESKD in ADPKD.
```

- [ ] **Step 3: Schema-validate**

Run: `just validate kb/disorders/Polycystic_Kidney_Disease.yaml`
Expected: PASS. Fix any `target` foreign-key / enum errors against the schema.

- [ ] **Step 4: Reference- and term-validate**

Run: `just validate-references kb/disorders/Polycystic_Kidney_Disease.yaml`
Run: `just validate-terms-file kb/disorders/Polycystic_Kidney_Disease.yaml`
Expected: both PASS.

- [ ] **Step 5: Commit**

```bash
git add kb/disorders/Polycystic_Kidney_Disease.yaml
git commit -m "feat(pkd): add TKV BiomarkerReadout bridge to FDA surrogate row"
```

---

## Task 7: Full validation sweep, push, PR

- [ ] **Step 1: Run the full named test modules**

Run: `uv run pytest tests/test_fda_surrogate_endpoints.py tests/test_regulatory_endpoint_refs.py -v`
Expected: all PASS. If `test_regulatory_endpoint_refs` fails on a missing/extra ref, reconcile the `regulatory_endpoint_refs` row IDs with the FDA YAML row IDs.

- [ ] **Step 2: Run aggregate QC on touched files**

NOTE (discovered during Task 3/4): `just validate` and `just validate-references`
run with `--target-class Disease`. That is correct for the two disorder files
but is the WRONG validator for `kb/surrogate_endpoints/fda_surrogate_endpoints.yaml`
(it errors at root with a pre-existing "Additional properties … retrieved_date …"
message and, for references, reports `Total checks: 0` — a false green). The
authoritative validation for the FDA file is the pytest suite in Step 1, plus
deterministic substring verification of each snippet against its committed
`references_cache/PMID_*.md` body (whitespace/case/punctuation normalized,
`[...]` stripped). Do NOT rely on `just validate*` for the FDA file.

Run: `just validate-references kb/disorders/Chronic_Kidney_Disease.yaml kb/disorders/Polycystic_Kidney_Disease.yaml`
Expected: PASS for both disorder files (their BiomarkerReadout snippets are real Disease-class checks).

`just validate-references` re-quotes `reference_id:` frontmatter in
`references_cache/*.md` as a benign side effect. After running it, restore that
churn so it is never staged:
Run: `git checkout -- references_cache/`
(The intended cache files were already committed in Tasks 1–2.)

- [ ] **Step 3: Review the diff for scope creep**

Run: `git diff --stat origin/main...HEAD` and `git diff --name-status origin/main...HEAD`
Expected: only the spec, the plan, the FDA YAML, the two disorder files, and the new `references_cache/PMID_*.md`. If any generated/unrelated path (e.g., re-quoted cache frontmatter, `pages/`, `dashboard/`) appears, stop and fix before pushing.

- [ ] **Step 4: Push and open PR from origin**

```bash
git push -u origin feat/endpoints-computational
```
Then open a PR to `main` summarizing: provenance-only curation of three kidney surrogate rows + two BiomarkerReadout bridges; explicitly note TKV is curated as prognostic-enrichment, not a validated efficacy surrogate; list validation results.

- [ ] **Step 5: Post the explanatory PR comment**

Comment on the PR: what changed and why, what was intentionally NOT changed (no schema change; validation levels untouched), and the validation/test output.

---

## Self-Review

**Spec coverage:**
- FDA-row `clinical_benefit` + verified `evidence` for the 3 rows → Tasks 3, 4 ✓
- Disease-side `BiomarkerReadout` bridges → Tasks 5, 6 ✓
- Anti-hallucination fetch→exact-snippet→validate workflow → Tasks 1, 2 + validate steps in 3–6 ✓
- Accuracy guardrail (CKD validated vs PKD prognostic-enrichment) → wording in Tasks 4, 6 ✓
- Validation & testing (named test modules, targeted git add) → Task 7 ✓
- No schema change → no schema task present ✓

**Placeholder scan:** `<verified>`, `<ckd>`, `<pkd>`, and `<exact sentence …>` are intentional resolution points inherent to the dismech anti-hallucination SOP (the real PMID/snippet cannot be known until the abstract is fetched); each is paired with an explicit discovery/verify step. No "TBD/handle edge cases/write tests for the above" style gaps.

**Type/name consistency:** Row IDs (`FDA-SE-adult-noncancer-012`, `FDA-SE-pediatric-noncancer-008`, `FDA-SE-adult-noncancer-090`) consistent across tasks and `regulatory_endpoint_refs`. The same verbatim snippet is reused between the FDA row and its disease-side bridge (Tasks 3↔5, 4↔6). `target: Nephron Loss` verified to exist for CKD; PKD target node name explicitly resolved in Task 6 Step 1 rather than assumed.
