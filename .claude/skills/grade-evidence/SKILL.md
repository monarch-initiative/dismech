---
name: grade-evidence
description: >
  Skill for adding Cochrane/GRADE evidence fields to dismech Treatment and EvidenceItem
  entries. Use when asked to upgrade existing curation with GRADE certainty ratings,
  PICO-structured population/comparator fields, and quantitative effect sizes.
  Applies to new curation or retrofitting existing disorder YAML files.
---

# GRADE Evidence Curation Skill

## Overview

This skill guides you in populating the Cochrane-compatible evidence fields added to the
dismech schema:

- `study_design` on `EvidenceItem` — the design of the individual cited study
- `grade_certainty` on `Treatment` — the overall GRADE certainty for this treatment
- `population_context` on `Treatment` — PICO P: which patient subgroup
- `comparator` on `Treatment` — PICO C: what was compared against
- `effect_size` on `Treatment` — best quantitative estimate with CI

These fields transform dismech treatment entries into GRADE summary table equivalents.

## When to Use

- When curating a new disorder and the treatment section has clinical RCTs or SRs
- When asked to "GRADE" or "add evidence grading" to an existing disorder
- When retrofitting treatment evidence for a specific disorder

## Workflow

### Step 1 — Identify the Best Evidence per Treatment

For each treatment, search PubMed/EuropePMC for:
1. A **systematic review with meta-analysis** (highest priority)
2. A **Cochrane review** specifically
3. A landmark **RCT** if no SR exists

Search template: `(<treatment>) AND (<disease>) AND (systematic review OR meta-analysis OR randomized controlled trial)`

### Step 2 — Assign `study_design` to EvidenceItems

On each `EvidenceItem`, set `study_design` to the design of that specific reference:

| Reference type | study_design value |
|---|---|
| Cochrane review / SR with meta-analysis | `SYSTEMATIC_REVIEW_WITH_META_ANALYSIS` |
| Systematic review (no pooling) | `SYSTEMATIC_REVIEW` |
| RCT | `RCT` |
| Cluster RCT | `CLUSTER_RCT` |
| Prospective cohort | `COHORT` |
| Case-control | `CASE_CONTROL` |
| Case series / case report | `CASE_SERIES` |
| Expert guideline / consensus | `EXPERT_OPINION` |

Do **not** populate `study_design` when the reference is a narrative review or
the design is unclear from the abstract alone.

### Step 3 — Assign `grade_certainty` to Treatment

Apply GRADE at the treatment level, summarising across all evidence items:

| Situation | grade_certainty |
|---|---|
| ≥2 well-conducted RCTs or Cochrane SR, consistent results, not downgraded | `HIGH` |
| RCTs with limitations (risk of bias, inconsistency, indirectness) OR upgraded observational | `MODERATE` |
| Observational studies (cohort, case-control) | `LOW` |
| Case series, expert opinion, or heavily downgraded studies | `VERY_LOW` |

**GRADE downgrades** (reduce certainty one level each):
- Serious/very serious risk of bias
- Important/very important inconsistency (high I²)
- Serious indirectness (population, intervention, or outcome differs)
- Serious imprecision (wide CIs, few events)
- Strong suspicion of publication bias

**GRADE upgrades** from observational (rare; raise by one level):
- Large effect (OR/RR > 2 or < 0.5)
- Dose-response gradient
- All plausible confounders would reduce effect

### Step 4 — Populate PICO Fields

**`population_context`** (PICO P): Specify the patient population.
- Prefer HPO, MONDO, age, or severity descriptors
- Examples:
  - `"adults with moderate-to-severe persistent asthma"`
  - `"children under 12 with atopic dermatitis"`
  - `"newly diagnosed type 2 diabetes, HbA1c > 8%"`

**`comparator`** (PICO C): Specify what the treatment was compared against.
- Examples:
  - `"placebo"`
  - `"inhaled corticosteroid monotherapy"`
  - `"standard of care (salbutamol PRN)"`
  - `"no treatment"`

### Step 5 — Populate `effect_size`

Extract the **primary outcome** effect size from the best available evidence
(Cochrane SR pooled estimate > other SR > individual RCT):

```yaml
effect_size:
  value: 0.72          # point estimate
  measure_type: RR     # OR | RR | HR | MD | SMD | ARR | NNT
  ci_lower: 0.58
  ci_upper: 0.90
  p_value: 0.003       # optional
  heterogeneity_i2: 42  # optional, from meta-analysis
  unit: ""             # leave blank for ratios; fill for MD (e.g. "mmHg")
```

Rules:
- Always pair `ci_lower` + `ci_upper` when available
- Report the outcome explicitly in `description` (e.g. "RR for asthma exacerbation requiring
  oral steroids vs placebo")
- If multiple outcomes are available, pick the most patient-important (mortality >
  hospitalisation > functional outcome > surrogate)
- For NNT: derive from ARR if not directly reported (NNT = 1/ARR)

## Example: Complete Treatment Entry

```yaml
- name: Inhaled Corticosteroid
  description: >-
    First-line controller therapy for persistent asthma. Reduces airway
    inflammation, prevents exacerbations, and improves lung function.
  population_context: "adults and children ≥5 years with mild-to-severe persistent asthma"
  comparator: "placebo or no controller therapy"
  grade_certainty: HIGH
  effect_size:
    value: 0.66
    measure_type: RR
    ci_lower: 0.59
    ci_upper: 0.74
    heterogeneity_i2: 28
  evidence:
  - reference: PMID:22559870
    reference_title: "The role of inhaled corticosteroids in asthma treatment: a health economic perspective."
    study_design: SYSTEMATIC_REVIEW_WITH_META_ANALYSIS
    supports: SUPPORT
    snippet: "ICS reduce asthma exacerbation rates by approximately 34% compared with placebo (RR 0.66, 95% CI 0.59–0.74)."
    explanation: Systematic review with meta-analysis confirming ICS efficacy for exacerbation prevention.
```

## Adding review_notes

Always add a `review_notes` entry documenting the GRADE rationale:

```yaml
review_notes: >-
  GRADE HIGH based on Cochrane SR (Reddel 2023, PMID:36476169) of 45 RCTs,
  n=14 000; consistent effect across populations; RR 0.66 (0.59–0.74) for
  exacerbations. No serious downgrade factors. Population context limited to
  persistent asthma — evidence for intermittent disease is MODERATE.
```

## Validation Checklist

Before committing:
- [ ] Every RCT or SR evidence item has `study_design` populated
- [ ] Every `Treatment` with ≥1 RCT/SR evidence item has `grade_certainty`
- [ ] `population_context` and `comparator` are populated when grade_certainty is set
- [ ] `effect_size.measure_type` is set whenever `effect_size.value` is set
- [ ] `ci_lower` and `ci_upper` are both present or both absent (never one without the other)
- [ ] `review_notes` explains the GRADE rating

## Priority Disorders for Piloting

Apply this skill first to disorders with well-studied treatments and established Cochrane
reviews. Good starting candidates from the existing KB:

- **Asthma** — extensive Cochrane review coverage (ICS, LABA, montelukast, biologics)
- **Rheumatoid Arthritis** — dense RCT/MA literature for DMARDs and biologics
- **Type 2 Diabetes** — strong SR evidence for metformin, GLP-1 agonists, SGLT2i
- **Atopic Dermatitis** — recent Cochrane reviews for dupilumab and TCS

For rare diseases, `LOW` or `VERY_LOW` ratings are expected — populate fields honestly
rather than leaving them empty.
