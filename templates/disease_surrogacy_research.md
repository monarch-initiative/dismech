# Class A Surrogacy Evidence Research Template

## Target Surrogacy Question

- **Disease:** {disease_name}
- **Surrogate endpoint:** {surrogate}
- **Clinical outcome under consideration:** {clinical_outcome}

## Research Objectives

Please provide a focused research report on the **trial-level / meta-analytic
("Class A") evidence** for whether the surrogate **"{surrogate}"** is a valid
proxy for the clinical outcome **"{clinical_outcome}"** in **{disease_name}**.
This report will be reconciled against a regulatory-endpoints knowledge base.
Every quantitative claim MUST cite a primary-literature source by PMID (or DOI
/ ClinicalTrials.gov NCT) and include a short verbatim quote from the cited
paper's abstract that contains the claim. Do not paraphrase. Do not invent
PMIDs.

For each section, prefer regulatory documents and high-quality
meta-analyses/registries.

---

### 1. Clinical outcome definition

> **Search first:** FDA/EMA guidance, NKF/KDIGO position statements, Cochrane,
> Biomarkers Consortium (FNIH).

- Name the specific clinical outcome the surrogate is intended to predict in
  this disease (e.g., "end-stage kidney disease", "all-cause mortality",
  "incident vertebral fracture"). If multiple composite endpoints are in
  current use, list each with its component events.
- Note whether the clinical outcome is itself a regulatorily-accepted endpoint
  (validated clinical endpoint) or a composite.

### 2. Trial-level meta-analytic surrogacy

> **Search first:** Buyse-Molenberghs / Burzykowski meta-analytic surrogacy
> literature; disease-specific consortia (e.g., NKF-FDA-EMA workshops for CKD,
> FNIH SABRE for osteoporosis, GLOBAL PBC, IPF Pooled Analyses, FNIH
> Biomarkers Consortium).

For each meta-analysis that quantifies the surrogacy of this
surrogate→outcome pair, report:

- Bibliographic citation with **PMID** and an exact quote from the abstract
  reporting the result.
- Number of RCTs / cohorts pooled, total patients, interventions covered.
- **Trial-level R² (R²_trial)** with 95% credible / confidence interval.
- **Individual-level R² (R²_indiv)** if reported.
- Statistical approach (Bayesian mixed-effects, copula, two-stage, etc.).

If no formal trial-level meta-analytic surrogacy analysis exists, say so
explicitly.

### 3. Proportion of treatment effect explained (PTE / Freedman)

- Report PTE values from individual RCTs or pooled analyses, with PMIDs and
  exact quotes.
- Flag analyses where PTE is low (poor surrogacy) as prominently as those
  where PTE is high.

### 4. Surrogate Threshold Effect (STE)

- Report any published STE estimate (the minimum treatment effect on the
  surrogate above which a non-zero treatment effect on the clinical outcome
  is predicted with stated probability).

### 5. Joint longitudinal–survival / mediation models

- Joint biomarker-trajectory ↔ time-to-event models linking this surrogate
  to the clinical outcome.
- Causal-mediation analyses quantifying the proportion mediated by the
  surrogate. Include PMIDs and exact quotes.

### 6. Regulatory qualification status

> **Search first:** FDA Drug Development Tools Qualification, EMA Qualification
> Opinions, FDA Letters of Support, Biomarker Qualification Program.

- State explicitly which of the following applies, with citations:
  - Validated surrogate endpoint known to predict clinical benefit
  - Surrogate reasonably likely to predict clinical benefit
  - Prognostic / trial-enrichment biomarker (NOT a treatment-efficacy surrogate)
  - Context-dependent
- Quote the regulatory language verbatim where possible (FDA qualification
  decision summary, EMA Qualification Opinion text).

### 7. Negative or refuting evidence

- Trials in which a treatment moved the surrogate but did NOT improve the
  clinical outcome (e.g., classic surrogate failures).
- Meta-analyses or commentaries that argue the surrogate is weak in this
  context. Include PMIDs and exact quotes.

### 8. FDA Surrogate Endpoint Table context

The FDA Surrogate Endpoint Table contains rows naming this surrogate for this
disease. Identify any approved or pending drug approvals using this surrogate
as the basis of efficacy. List the drug, sponsor, approval type
(traditional / accelerated), and approval year.

---

## Output requirements

- **Cite every quantitative claim by PMID** (or DOI/NCT) and include a
  verbatim quote from the cited abstract containing that claim.
- Distinguish *validated surrogate*, *reasonably likely*, and *prognostic
  enrichment* throughout; do not conflate them.
- If a section has no published evidence, say "No published evidence
  identified" — do not invent values.
- Prefer regulatory documents and high-N meta-analyses over single RCTs.
- Do not generate findings that cannot be tied to a real, retrievable
  reference.
