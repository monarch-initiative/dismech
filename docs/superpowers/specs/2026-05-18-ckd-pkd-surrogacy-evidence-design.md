# Design: Class A surrogacy provenance for kidney surrogate endpoints (CKD eGFR, PKD TKV)

Date: 2026-05-18
Status: Approved (brainstorming) — pending implementation plan
Branch: `feat/endpoints-computational`

## Goal

Curate Class A (statistical / meta-analytic) surrogacy provenance for the three
already-mapped kidney rows in the FDA Surrogate Endpoint Table, so that each row
states the clinical outcome it predicts and cites the published validating
analysis. **No schema change.** Provenance linkage only.

"Class A" = the statistical evidence that directly answers *"is this surrogate a
good proxy for the clinical outcome?"* (trial-level meta-analytic R², proportion
of treatment effect explained, surrogate threshold effect, biomarker
qualification), as distinct from Class B mechanistic in-silico models.

## In scope

Three FDA rows (`kb/surrogate_endpoints/fda_surrogate_endpoints.yaml`):

| Row ID | Disease/use | Surrogate | Validation level (unchanged) |
|---|---|---|---|
| `FDA-SE-adult-noncancer-012` | Chronic kidney disease | eGFR or serum creatinine | VALIDATED_SURROGATE_ENDPOINT |
| `FDA-SE-pediatric-noncancer-008` | Chronic kidney disease (pediatric) | eGFR or serum creatinine | VALIDATED_SURROGATE_ENDPOINT |
| `FDA-SE-adult-noncancer-090` | Polycystic kidney disease | Total kidney volume | REASONABLY_LIKELY_SURROGATE_ENDPOINT |

Two disorder files for the disease-side bridge:
`kb/disorders/Chronic_Kidney_Disease.yaml`,
`kb/disorders/Polycystic_Kidney_Disease.yaml`.

## Out of scope

- No schema extension (no new surrogacy-statistic slot). If machine-queryable
  statistics are wanted later, that is a separate, clean follow-up.
- No change to `endpoint_validation_level`, `clinical_benefit_linkage`,
  `approval_type`, or `mapping_status` on any row.
- No Class B (mechanistic in-silico) modeling work; tracked separately.
- Other kidney rows (`FDA-SE-adult-noncancer-036` hepatorenal,
  `-104`/`-pediatric-068` secondary hyperparathyroidism) remain
  `NEEDS_CURATION` and are untouched.

## Architecture / artifacts

Two artifacts per surrogate, using only existing schema:

### A. FDA-row provenance (`SurrogateEndpoint`)

For each of the three rows, set/append:

- `clinical_benefit`: plain-English statement of the clinical outcome the
  surrogate predicts (no numbers here).
- `evidence`: one appended `EvidenceItem`:
  - `reference: PMID:<verified>`
  - `supports: SUPPORT`
  - `evidence_source: HUMAN_CLINICAL`
  - `snippet:` an **exact substring** of the cached abstract — this is the
    *only* place quantitative surrogacy results (R²_trial, PTE, STE, n trials)
    appear, and only as verbatim quotes.
  - `explanation:` one line of curatorial context naming the analysis.

Encoding decision (locked): **plain quote only**. No hand-structured
"surrogacy: ..." convention in `notes`; numbers live solely inside the verbatim
`snippet`.

### B. Disease-side bridge (`BiomarkerReadout`)

Mirrors the Fabry flagship pattern. **Correction (found during implementation):**
there is no top-level `biomarker_readouts` Disease slot. The schema slot is
`readouts`, owned by the **`Biochemical`** class. The Fabry flagship structure
is `biochemical: → <biomarker entry> → readouts: → BiomarkerReadout`, and Fabry
already models a non-serum biomarker (`Renal Globotriaosylceramide Inclusions`,
a tissue/biopsy biomarker) this way. The bridge is therefore attached via a
`Biochemical` entry, not a Disease-level key.

- `Chronic_Kidney_Disease.yaml`: add a `readouts:` block to the existing
  `Creatinine` `Biochemical` entry (serum creatinine is the reciprocal of
  eGFR) — `target: Nephron Loss` (existing pathophysiology node),
  `relationship: READOUT_OF`, `direction: NEGATIVE`,
  `endpoint_context: PROGNOSTIC`,
  `regulatory_endpoint_refs: [FDA-SE-adult-noncancer-012, FDA-SE-pediatric-noncancer-008]`,
  plus `interpretation` and the verified `evidence`.
- `Polycystic_Kidney_Disease.yaml`: TKV is an imaging biomarker with no
  existing serum entry, so add a new `Biochemical` entry
  `Total Kidney Volume (height-adjusted)` (`presence: Increased`) carrying the
  `readouts:` block — `target: Epithelial Proliferation and Kidney Enlargement`
  (existing pathophysiology node), `direction: POSITIVE`,
  `endpoint_context: PROGNOSTIC`,
  `regulatory_endpoint_refs: [FDA-SE-adult-noncancer-090]`. Optional
  `biomarker_term` (NCIT) is a possible follow-up, deferred to keep this
  provenance-only and within scope.

If the target disorder file lacks a suitable existing pathophysiology node, the
node name is matched to the closest existing node rather than inventing one;
any mismatch is surfaced for review, not silently forced.

## Reference strategy (anti-hallucination — load-bearing)

Candidate primary sources; **PMIDs and the quotable sentence are verified at
implementation, never assumed**:

- **CKD eGFR/creatinine** (validated): NKF-FDA-EMA scientific workshop and
  Inker / Levey / Greene trial-level meta-analyses of GFR slope and
  ≥30–40% eGFR decline as surrogate endpoints for kidney failure.
- **PKD TKV** (prognostic enrichment, *not* a validated efficacy surrogate):
  Mayo Imaging Classification (Irazabal), CRISP, PKD Outcomes Consortium
  (Perrone), and the FDA/EMA biomarker **qualification of htTKV as a prognostic
  enrichment biomarker**.

Per-reference workflow (dismech SOP):

1. Choose candidate PMID.
2. `just fetch-reference PMID:XXXX` (creates `references_cache/PMID_XXXX.md`;
   never hand-written).
3. Read the cached abstract; select a snippet that is an exact substring.
4. Write the YAML.
5. `just validate-references` on every touched file.

If no exact quotable sentence with the statistic exists in the abstract, the
statistic is **omitted** and `clinical_benefit` falls back to the qualitative
outcome statement. No fabricated PMIDs, no paraphrased snippets.

## Accuracy guardrail (enforced)

CKD eGFR/creatinine is written as a **validated surrogate for kidney-failure
outcomes**. PKD TKV is written strictly as a **prognostic / trial-enrichment
biomarker that is reasonably likely to predict benefit** — never as a validated
efficacy surrogate. Wording, `clinical_benefit`, `explanation`, and
`endpoint_context` reflect this asymmetry.

## Validation & testing

Before commit:

- `just validate kb/disorders/Chronic_Kidney_Disease.yaml`
- `just validate kb/disorders/Polycystic_Kidney_Disease.yaml`
- `just validate-references` on the FDA YAML and both disorder files
- `just validate-terms-file` on both disorder files
- `pytest tests/test_fda_surrogate_endpoints.py tests/test_regulatory_endpoint_refs.py`

Targeted `git add` only:
`kb/surrogate_endpoints/fda_surrogate_endpoints.yaml`,
`kb/disorders/Chronic_Kidney_Disease.yaml`,
`kb/disorders/Polycystic_Kidney_Disease.yaml`,
new `references_cache/PMID_*.md`,
and this spec.

## Success criteria

- All three rows have a non-empty `clinical_benefit` and at least one verified
  `evidence` item whose snippet passes `validate-references`.
- Both disorder files have a `BiomarkerReadout` linking the surrogate to a real
  pathophysiology node with correct `regulatory_endpoint_refs`.
- Full validation suite and the two named test modules pass.
- TKV is not overstated as a validated efficacy surrogate.
