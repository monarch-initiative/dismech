---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-09T12:48:53.653948'
end_time: '2026-10-09T13:02:18.114769'
duration_seconds: 804.46
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Hypertrophic Cardiomyopathy
  category: Complex
  hypothesis_group_id: myosin_inhibitor_obstruction_vs_substrate
  hypothesis_label: Myosin inhibitors act chiefly by relieving outflow obstruction
    rather than reversing the sarcomere substrate
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: myosin_inhibitor_obstruction_vs_substrate\n\
    hypothesis_label: Myosin inhibitors act chiefly by relieving outflow obstruction\
    \ rather than reversing\n  the sarcomere substrate\nstatus: EMERGING\ndescription:\
    \ Cardiac myosin inhibitors (mavacamten, aficamten) reduce actin-myosin cross-bridge\
    \ formation\n  and stabilize the myosin super-relaxed state. This hypothesis holds\
    \ that their clinical benefit in obstructive\n  HCM derives predominantly from\
    \ a load-dependent reduction of left ventricular outflow tract obstruction\n \
    \ rather than from reversal of the underlying sarcomeric and myocardial substrate\
    \ (myocyte disarray, interstitial\n  fibrosis). The discriminating prediction\
    \ is that benefit should be attenuated where there is no gradient\n  to relieve,\
    \ consistent with mavacamten's reported primary-endpoint miss in non-obstructive\
    \ HCM (ODYSSEY-HCM);\n  the competing view is a genuine gradient-independent effect\
    \ on sarcomere energetics and diastolic function.\n  Modeled EMERGING because\
    \ the distinguishing trial readouts are recent and the obstructive-versus-non-obstructive\n\
    \  contrast is not yet settled.\nevidence:\n- reference: PMID:37060436\n  reference_title:\
    \ Mechanisms of Sarcomere Protein Mutation-Induced Cardiomyopathies.\n  supports:\
    \ SUPPORT\n  evidence_source: OTHER\n  snippet: Recent advances in our mechanistic\
    \ understanding of sarcomere pathophysiology include high-resolution\n    molecular\
    \ models of sarcomere components and the identification of the myosin super-relaxed\
    \ state.\n  explanation: Establishes the myosin super-relaxed state as the molecular\
    \ target through which myosin\n    inhibitors act, which this hypothesis builds\
    \ on."
  artifact_dir: kb/hypotheses/Hypertrophic_Cardiomyopathy/myosin_inhibitor_obstruction_vs_substrate/openscientist_artifacts
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
term_validation:
  total_terms: 6
  verified: 6
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: kb_hypotheses_Hypertrophic_Cardiomyopathy_myosin_inhibitor_obstruction_vs_substrate_openscientist_artifacts_evidence_matrix.csv
  path: openscientist_artifacts/kb_hypotheses_Hypertrophic_Cardiomyopathy_myosin_inhibitor_obstruction_vs_substrate_openscientist_artifacts_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: kb_hypotheses_Hypertrophic_Cardiomyopathy_myosin_inhibitor_obstruction_vs_substrate_openscientist_artifacts_search_log.md
  path: openscientist_artifacts/kb_hypotheses_Hypertrophic_Cardiomyopathy_myosin_inhibitor_obstruction_vs_substrate_openscientist_artifacts_search_log.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist search log
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** myosin_inhibitor_obstruction_vs_substrate
- **Hypothesis Label:** Myosin inhibitors act chiefly by relieving outflow obstruction rather than reversing the sarcomere substrate
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: myosin_inhibitor_obstruction_vs_substrate
hypothesis_label: Myosin inhibitors act chiefly by relieving outflow obstruction rather than reversing
  the sarcomere substrate
status: EMERGING
description: Cardiac myosin inhibitors (mavacamten, aficamten) reduce actin-myosin cross-bridge formation
  and stabilize the myosin super-relaxed state. This hypothesis holds that their clinical benefit in obstructive
  HCM derives predominantly from a load-dependent reduction of left ventricular outflow tract obstruction
  rather than from reversal of the underlying sarcomeric and myocardial substrate (myocyte disarray, interstitial
  fibrosis). The discriminating prediction is that benefit should be attenuated where there is no gradient
  to relieve, consistent with mavacamten's reported primary-endpoint miss in non-obstructive HCM (ODYSSEY-HCM);
  the competing view is a genuine gradient-independent effect on sarcomere energetics and diastolic function.
  Modeled EMERGING because the distinguishing trial readouts are recent and the obstructive-versus-non-obstructive
  contrast is not yet settled.
evidence:
- reference: PMID:37060436
  reference_title: Mechanisms of Sarcomere Protein Mutation-Induced Cardiomyopathies.
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Recent advances in our mechanistic understanding of sarcomere pathophysiology include high-resolution
    molecular models of sarcomere components and the identification of the myosin super-relaxed state.
  explanation: Establishes the myosin super-relaxed state as the molecular target through which myosin
    inhibitors act, which this hypothesis builds on.
```

## Research Objective

Build a focused hypothesis-search report that answers:

1. What is the strongest direct evidence for this hypothesis?
2. What evidence argues against it, fails to reproduce it, or limits its scope?
3. Which claims are established, emerging, speculative, or contradicted?
4. Which patient subtypes, stages, tissues, cell types, molecular pathways, or
   biomarkers does the hypothesis best explain?
5. Which alternative or competing mechanistic hypotheses explain the same disease
   features better or more parsimoniously?
6. What are the explicit knowledge gaps: missing causal steps, unconfirmed edges,
   contradictory evidence, unknown source-to-target links, or source/data absences?
7. What experiments, cohorts, assays, datasets, or trials would most directly
   distinguish this hypothesis from alternatives?

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews as orientation unless they
contain directly relevant synthesized evidence that should be clearly labeled as
review-level support.

When dataset or scientific-tool access is available, use it for questions that
can be tested computationally rather than limiting the run to literature search.
Preflight the required data lake, databases, packages, credentials, and tools
before claiming that an analysis can run. Never silently fall back from a failed
dataset/tool analysis to literature synthesis or model knowledge: report the
failure, the fallback, and the resulting limitation explicitly. A proposed
analysis must never be described as performed.

## Required Output

### Executive Judgment

Give a concise verdict on the hypothesis as of the current literature:
supported, partially supported, unresolved, weakly supported, or refuted. Explain
the reasoning and the most important caveats.

### Evidence Matrix

Create a table with one row per important evidence item:

- Citation (PMID preferred)
- Evidence type (human clinical, model organism, in vitro, computational, review)
- Supports / refutes / qualifies / competing
- Mechanistic claim tested
- Key finding
- Disease subtype or context
- Confidence and limitations

### Data and Tool Use

Inventory every dataset, database, API, supplementary file, or local input
material to the report. For each, state:

- stable accession or URI, repository/source, version or snapshot, and retrieval
  date where known;
- whether it was only cited/proposed, actually accessed, searched with no usable
  result, or could not be verified;
- the exact query, filters, cohort, sample subset, organism, tissue, assay, and
  comparison used where applicable;
- whether the accession resolved and whether its subject matter is genuinely
  relevant to this disease and hypothesis.

For accessed sources and negative searches, save a sanitized query response,
input manifest, or search log in the provider artifact bundle; prose alone does
not establish access or a negative result.

Inventory each attempted analysis separately. Trace input -> method -> output,
including software/model versions, material parameters, code or workflow,
environment, random seeds where relevant, output files, and limitations. Label
the execution outcome as succeeded, partial, failed, skipped, or reported-only.
Do not count a prose assertion without inspectable execution evidence as a
successful analysis.

### Mechanistic Causal Chain

Describe the causal chain implied by the hypothesis from upstream trigger to
clinical manifestation. Identify where the literature is strong, where the links
are inferred, and where there are missing causal steps.

### Knowledge Gaps

Identify explicit known unknowns surfaced by the search. Treat absence of
evidence as a curation-relevant finding only when the search actually checked for
it. Include:

- Unknown or weakly supported causal steps in the hypothesis
- Unconfirmed causal graph edges that need direct perturbation or longitudinal
  evidence
- Conflicting evidence, failed replications, or incompatible subtype-specific
  findings
- Unknown mechanism of action for relevant treatments, biomarkers, or
  interventions tied to this hypothesis
- Source-level or dataset-level absences, such as no relevant GenCC, ClinGen,
  trial, omics, or cohort evidence found as of the search date

For each gap, state the scope, why it matters, what was checked, and what
evidence or experiment would resolve it. A negative database search must include
the database/version, query, filters, and search date; otherwise label it
unverified rather than claiming absence.

### Alternative Models

List competing or complementary hypotheses. For each, explain whether it is an
alternative to the seed hypothesis, a downstream consequence, an upstream cause,
or a parallel mechanism.

### Discriminating Tests

Recommend concrete studies or assays that would most efficiently test this
hypothesis against alternatives. Include patient stratification, biomarkers,
sample type, model system, perturbation, and expected result where applicable.

### Curation Leads

Provide candidate updates for the KB, but label these as leads requiring curator
verification. Include:

- candidate evidence references and exact abstract snippets to verify
- candidate pathophysiology nodes or edges
- candidate ontology terms for cell types and biological processes
- candidate subtype restrictions or status changes
- candidate `knowledge_gaps` or discussion prompts for unresolved causal claims,
  conflicting evidence, or explicit source/data absences

If the provider supports artifacts, produce a provider artifact bundle containing
canonical `MANIFEST.yaml` (schema version, status/fallback flags, checksummed
inputs/outputs, and replay verification), code/query/configuration, an
environment or package-version record,
sanitized execution logs, and small derived tables/figures needed to inspect the
result beneath `kb/hypotheses/Hypertrophic_Cardiomyopathy/myosin_inhibitor_obstruction_vs_substrate/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.


## Output

# Hypothesis-Search Report
## Myosin inhibitors act chiefly by relieving outflow obstruction rather than reversing the sarcomere substrate

**Disease:** Hypertrophic Cardiomyopathy (Complex)
**Hypothesis ID:** `myosin_inhibitor_obstruction_vs_substrate`
**KB status (input):** EMERGING
**Report date:** 2026-10-09
**Run mode:** Literature-hypothesis search (no data files provided; no omics/patient-level dataset or computational analysis performed — see *Data and Tool Use*).

---

## 1. Executive Judgment

**Verdict: PARTIALLY SUPPORTED (lean-supported for the symptomatic/functional endpoint; unresolved for the substrate-reversal claim).**

The strong form of the hypothesis — that the *clinical benefit* of cardiac myosin inhibitors (CMIs; mavacamten, aficamten) in obstructive HCM (oHCM) is **predominantly load-dependent relief of LV outflow tract (LVOT) obstruction** — is well supported for symptomatic and functional endpoints:

- In oHCM, CMIs produce **large, rapid, reversible LVOT-gradient reductions** that track symptom and exercise gains, and benefit **reverses on drug withdrawal** (PMID 42251960, 42002189, 42667283, 41093262). Reversibility is the signature of a load/hemodynamic effect rather than durable substrate remodeling.
- The **discriminating prediction holds at the trial level**: in non-obstructive HCM (nHCM), where there is no gradient to relieve, the phase 3 **ODYSSEY-HCM trial did not meet its primary endpoint** (review synthesis PMID 40624601).

However, the **"rather than reversing the sarcomere substrate"** clause is only *partially* correct and is actively contested by three lines of evidence:

1. **The molecular target is intrinsically gradient-independent.** CMIs act on the myosin super-relaxed/off-actin (SRX) state and cross-bridge cycling in *any* myocardium (PMID 40000285, 30371160, 37060436). Mechanistically there is no reason the effect should be confined to obstructed hearts.
2. **Gradient-independent biomarker signal.** In nHCM cohorts (MAVERICK-HCM, REDWOOD-HCM cohort 4) CMIs lowered cardiac biomarkers (NT-proBNP/troponin) and improved symptoms despite no gradient (PMID 40624601, 41841680) — a wall-stress/sarcomere-energetics effect, not obstruction relief.
3. **Preclinical substrate modification.** Early chronic mavacamten (MYK-461) in non-obstructed MYH7-mutant mice **prevented hypertrophy, myocyte disarray, and fibrosis** (PMID 26912705) — direct gradient-independent substrate modification (prevention, not reversal).

The best synthesis: in **established adult oHCM**, the dominant and reproducible driver of symptomatic benefit is **obstruction relief**, and the **fibrotic substrate (LGE scar) does not clearly reverse** over 6–30 months (PMID 42715826, 41877729). But CMIs also produce **reverse hypertrophic remodeling (LV-mass regression)** and **gradient-independent biomarker effects**, and preclinical data show they can **prevent** substrate pathology. So "chiefly obstruction relief" is accurate for *current symptomatic endpoints in obstructive disease*, but the hypothesis **overstates the dichotomy**: a genuine load-independent sarcomere/energetics component exists and is not excluded.

**Most important caveats:**
- The decisive nHCM readout (ODYSSEY-HCM) was available only via **review-level synthesis**; the primary trial report was **not retrievable** through the search tool this run.
- LV-mass regression is itself **partly load-mediated** (reduced wall stress after gradient relief), so mass change does not cleanly prove sarcomere-substrate reversal.
- Several key abstracts were **truncated** (SEQUOIA CMR, EXPLORER-CN CMR, ASA-vs-mavacamten), limiting exact effect extraction.

---

## 2. Evidence Matrix

Full machine-readable table: `openscientist_artifacts/evidence_matrix.csv` (16 rows). Summary:

| PMID | Type | Stance | Mechanistic claim tested | Key finding | Subtype | Confidence / limitation |
|------|------|--------|--------------------------|-------------|---------|--------------------------|
| 42002189 | Human RCT subanalysis | **Support** | Load-dependent gradient relief | Aficamten −66% Valsalva LVOT-G (123→41 mmHg, p=0.001); NT-proBNP −85%; pVO2 +1.8 | oHCM, very-high gradient | High for gradient; 24 wk; subgroup |
| 42251960 | Human RCT | **Support** | Benefit tracks obstruction, reversible | HCMSQ improved vs placebo (p<0.001); scores return to baseline by wk38 after stopping | oHCM (EXPLORER) | High; reversibility = load-dependent |
| 42667283 | Human RCT | **Support** | CMI > beta-blocker functionally | Aficamten > metoprolol pVO2 (+1.9 to +3.1) | oHCM (MAPLE) | High; active comparator |
| 41093262 | Meta-analysis | Support/qualify | Class clinical effect + remodeling | 4 RCTs/726: +NYHA 36%, KCCQ +8.4, pVO2 +1.6; favourable remodeling | oHCM | High clinical; no fibrosis endpoint |
| 40624601 | Review | **Support + qualify** | Benefit attenuated without gradient | ODYSSEY-HCM primary endpoints NOT met in nHCM; MAVERICK/REDWOOD biomarker+symptom gains | nHCM vs oHCM | Moderate; review; primary report not retrieved |
| 41841680 | Review | Qualify/compete | CMIs don't fix energy deficit | Robust biomarker gains but no resolution of nHCM energy mismatch | nHCM | Moderate; review |
| 26912705 | Model organism | **Competing** | Gradient-independent substrate prevention | Early chronic MYK-461 suppressed hypertrophy, disarray, fibrosis in MYH7-mutant mice | Genetic HCM mouse (non-obstructed) | High internal validity; prevention≠reversal; murine |
| 42715826 | Meta-analysis (CMR) | Support/qualify | Structural substrate reversal | LV mass index −20.01 g/m²; fibrosis impact "unclear" | oHCM (3 RCTs, n=150) | Moderate; small n; fibrosis inconclusive |
| 40632050 | Human RCT (CMR) | Qualify | Mass + fibrosis markers | Mavacamten LV mass index −30.8 g/m²; some fibrosis indicators reduced (wk30) | oHCM (EXPLORER-CN) | Moderate; truncated; mass may be load-mediated |
| 41877729 | Human case (serial CMR) | Support/qualify | Long-term substrate reversal | 2 yr: mass down; **LGE scar unchanged**; T1 down; ECV up then normalized | oHCM (n=1) | Low (single case); scar persists |
| 39217563 | Human RCT (CMR) | Support/qualify | Reverse remodeling | SEQUOIA CMR substudy (n=50): aficamten vs placebo structure/function | oHCM | Moderate; truncated results |
| 41688269 | Human observational | Qualify | Diastolic/LA remodeling | NT-proBNP 1431→158; LAESV 50.8→39.9; LVOT 65→12 | oHCM (n=55) | Moderate; diastolic gains confounded by gradient relief |
| 41590843 | Human retrospective | Qualify (discriminating design) | Diastolic effect CMI vs ASA | Mavacamten vs alcohol septal ablation diastolic comparison | oHCM | Moderate; truncated; isolates gradient-independent diastolic effect |
| 40000285 | Review | Mechanism (compete-basis) | Gradient-independent MoA | HCM = ↑crossbridge formation + destabilized SRX; CMIs reduce crossbridges | HCM general | Moderate; review |
| 30371160 | In vitro | Mechanism | CMI blunts hypercontractility | Myk461 reduced hypercontractile crossbridge kinetics incl cMyBPC-KO | Model myocardium | Moderate; skinned fibers |
| 37060436 | Review (seed) | Support (basis) | SRX is the target | Identifies SRX state in sarcomere cardiomyopathy | HCM | Moderate; orientation |

---

## 3. Data and Tool Use

**Inventory of sources (see `openscientist_artifacts/search_log.md` for the full 21-query log):**

- **PubMed** (NCBI E-utilities via OpenScientist `search_pubmed`). Live query, no fixed snapshot version. Retrieval date 2026-10-09. **Accessed** — abstracts retrieved for 11/21 queries; 10 queries returned no usable result; 1 HTTP 429 rate-limit. All returned PMIDs are genuinely on-topic (HCM + myosin inhibitors). Full-text not retrieved; several abstracts truncated (noted per row in `evidence_matrix.csv`).
- **ClinicalTrials.gov / trial registry API** — **NOT queried** this run. NCT IDs (EXPLORER NCT03470545, VALOR NCT04349072, SEQUOIA NCT05186818, MAPLE NCT05767346, EXPLORER-CN NCT05174416, MAVA-LTE NCT03723655) were read from abstract text, not verified against the registry. *Source absence recorded.*
- **GenCC / ClinGen / omics (GEO, GTEx, cBioPortal) / cohort datasets** — **NOT queried**. The hypothesis is a pharmacodynamic/trial-level mechanism claim, not a gene–disease validity claim, so these were out of scope. *Source absences recorded; no silent fallback occurred because no dataset analysis was attempted and abandoned.*

**Analyses attempted:**

| Analysis | Input → Method → Output | Outcome |
|----------|--------------------------|---------|
| Literature evidence synthesis | PubMed abstracts → manual stance classification → `evidence_matrix.csv`, knowledge_state findings | **Succeeded** (literature only) |
| Artifact bundle authoring | findings → file authoring + `sha256sum` → `search_log.md`, `evidence_matrix.csv`, `environment.txt`, `MANIFEST.yaml` | **Succeeded** |
| Computational/statistical analysis of patient or omics data | — | **Skipped** (no data files provided; none available to preflight) |

No statistical computation was performed; no result in this report is derived from executed analysis of primary data. All quantitative values are extracted from published abstracts.

---

## 4. Mechanistic Causal Chain

**Hypothesis-implied chain (obstruction-relief dominant):**

1. **Upstream trigger:** sarcomere gene mutation (MYH7, MYBPC3, …) → destabilized myosin SRX/off-actin state → ↑actin–myosin cross-bridges → **hypercontractility**. *(Strong: PMID 40000285, 30371160, 37060436.)*
2. **Hypercontractility → dynamic LVOT obstruction** (+ SAM of mitral valve). *(Strong in oHCM.)*
3. **CMI binds myosin → ↓cross-bridge formation → ↓contractility → ↓LVOT gradient (load reduction).** *(Strong, reversible: PMID 42002189, 42251960.)*
4. **↓gradient → ↓wall stress, ↓filling pressure → symptom/exercise/biomarker improvement.** *(Strong in oHCM: PMID 41093262, 41688269.)*

**Where the chain is strong:** steps 1–4 in obstructive disease.

**Where links are inferred / missing:**
- **Step 3→substrate:** Does ↓cross-bridge cycling durably **reverse** myocyte disarray / interstitial fibrosis in humans? **Inferred/absent.** Human CMR shows **mass regression but no clear fibrosis/LGE reversal** (PMID 42715826, 41877729). Preclinical shows **prevention** of substrate, not reversal of established disease (PMID 26912705).
- **Gradient-independent arm:** CMI → ↓wall stress / improved energetics → biomarker/diastolic benefit **without** a gradient. **Supported in nHCM biomarkers but the clinically meaningful endpoint failed (ODYSSEY).** This is the unresolved fork between the seed hypothesis and its competitor.

---

## 5. Knowledge Gaps

1. **Does CMI reverse the fibrotic substrate in humans?** Scope: oHCM/nHCM, longitudinal CMR (T1/ECV/LGE). Why it matters: central to the seed's "not reversing the substrate" clause. Checked: PubMed CMR queries (#9,#11,#12 null; #17,#19 informative). Current state: **mass reverses; fibrosis unclear/scar persists.** Resolver: ≥24-month RCT with ECV/T1 primary endpoint and endomyocardial sampling.
2. **ODYSSEY-HCM primary report.** Scope: the decisive nHCM readout. Why it matters: discriminates seed vs competitor. Checked: queries #2, #4, and dedicated ODYSSEY query (iter 3) — **primary report NOT retrieved via tool** (only review PMID 40624601). Label: **unverified absence** (tool-indexing limitation, not confirmed PubMed absence). Resolver: retrieve the primary publication / NCT results.
3. **Gradient-independent clinical efficacy.** Scope: nHCM. Conflict: biomarker/symptom gains (MAVERICK/REDWOOD) vs failed ODYSSEY primary endpoint. Resolver: adequately powered nHCM RCT with objective endpoints; subgroup by fibrosis burden/energetic phenotype.
4. **Is LV-mass regression substrate reversal or load unloading?** Scope: oHCM. Why it matters: mass change is used as "reverse remodeling" but is confounded by wall-stress reduction. Resolver: compare CMI vs pure mechanical gradient relief (myectomy/ASA) head-to-head on mass/ECV (partially addressed by PMID 41590843, truncated).
5. **Genotype stratification of response.** Scope: sarcomere-positive vs -negative. Checked: query null (iter 3). If benefit were substrate-directed, genotype-positive patients might respond differently. **Data not retrieved — gap.**
6. **Source absences:** no ClinicalTrials.gov/GenCC/ClinGen/omics query this run (out of scope for a pharmacodynamic claim) — recorded, not claimed as biological absence.

---

## 6. Alternative / Competing Models

1. **Gradient-independent sarcomere-energetics model (primary competitor).** CMIs restore SRX, reduce ATP waste and wall stress, improving diastolic function and biomarkers regardless of obstruction. *Alternative* to the seed. Support: PMID 40000285, 26912705, nHCM biomarker gains. Weakness: ODYSSEY primary-endpoint miss.
2. **Reverse-remodeling / disease-modification model.** Sustained contractility reduction → LV-mass regression, atrial reverse remodeling, possibly lower arrhythmic risk. *Downstream consequence* that may be partly load-mediated. Support: PMID 42715826, 40632050, 41711735 (SCD-risk-score effects). Weakness: fibrosis/scar unchanged.
3. **Pure hemodynamic palliation (strong seed form).** CMIs = reversible gradient relief only; stop drug → disease returns. Support: reversibility (PMID 42251960). Weakness: cannot explain nHCM biomarker gains or preclinical substrate prevention.
4. **Metabolic/energetic substrate model (parallel mechanism).** nHCM is driven by an energy deficit CMIs do not fix; metabolic modulators (ninerafaxstat) target this. *Parallel/complementary.* Support: PMID 41841680. Implication: explains why a sarcomere-contractility drug underperforms in nHCM.
5. **Mitral-apparatus/geometry model (upstream contributor to obstruction).** AMVL length predicts CMI response (PMID 40606967) — obstruction is partly anatomic, consistent with the seed's load-centric view in oHCM.

---

## 7. Discriminating Tests

1. **CMI vs mechanical gradient relief (myectomy/ASA), matched gradient reduction, CMR primary endpoint (ECV/T1, disarray surrogate), 24 months.** Stratify oHCM by baseline fibrosis. *Expected if seed true:* equal symptom benefit, **no** extra fibrosis/ECV improvement from CMI beyond load relief. *If competitor true:* CMI yields extra interstitial-fibrosis/energetic improvement. (PMID 41590843 is a small retrospective start.)
2. **Adequately powered nHCM RCT (aficamten/mavacamten) with objective primary endpoint (pVO2) + CMR/biomarker secondaries,** pre-stratified by fibrosis burden and energetic phenotype (31P-MRS PCr/ATP). *Expected if seed true:* no functional benefit despite biomarker change; *if competitor true:* functional benefit in low-fibrosis/high-energy-deficit subgroup.
3. **Genotype-stratified response analysis** (sarcomere-positive vs -negative) across pooled trials.
4. **31P-MRS myocardial energetics (PCr/ATP) before/after CMI** in oHCM and nHCM — directly tests the "sarcomere-energetics" competitor. *Expected if competitor true:* PCr/ATP improves independent of gradient.
5. **Serial endomyocardial or imaging biomarkers of myocyte disarray (diffusion-tensor CMR)** to test substrate reversal directly.

---

## 8. Curation Leads (require curator verification)

**Candidate status:** Keep **EMERGING**, refine label to subtype-qualified: *"In obstructive HCM, CMI symptomatic benefit is chiefly load-dependent gradient relief; a gradient-independent sarcomere/energetics effect exists but has not yet translated to a positive non-obstructive clinical endpoint."*

**Candidate evidence references (verify exact snippets):**
- PMID 40624601 — snippet: *"the preliminary results from phase 3 trials (ODYSSEY-HCM trial) revealed that primary endpoints were not met in nonobstructive HCM"* (SUPPORT, review-level).
- PMID 40624601 — snippet: *"In nonobstructive HCM, preliminary studies (MAVERICK-HCM trial and cohort 4 of REDWOOD-HCM trial) have reported improvements in cardiac serum biomarkers and symptoms."* (QUALIFY).
- PMID 26912705 — snippet: *"early, chronic administration of MYK-461 suppresses the development of ventricular hypertrophy, cardiomyocyte disarray, and myocardial fibrosis"* (COMPETING).
- PMID 42715826 — snippet: *"the impact on myocardial fibrosis remains unclear"* (SUPPORT for substrate-not-reversed).
- PMID 42251960 — snippet: *"Therapy cessation was associated with return to baseline in HCMSQ scores by week 38."* (SUPPORT, reversibility).
- PMID 40000285 — snippet: *"an enhanced rate of myosin-actin crossbridge formation and destabilization of the energy-conserving \"super-relaxed off-actin state\" of myosin"* (mechanism basis).

**Candidate pathophysiology nodes/edges:**
- Node: *myosin super-relaxed (SRX) / off-actin state* → Node: *cross-bridge formation rate* → Node: *hypercontractility* → Node: *dynamic LVOT obstruction* → Node: *symptoms/wall-stress*.
- Edge (well-supported): CMI ⊣ cross-bridge formation ⊣ LVOT gradient (reversible).
- Edge (inferred/contested): CMI ⊣ interstitial fibrosis / myocyte disarray (preclinical-only; human-unconfirmed).
- Edge (parallel): nHCM energy deficit — not addressed by CMI.

**Candidate ontology terms:**
- Cell type: cardiomyocyte (CL:0000746); cardiac fibroblast (CL:0002548).
- Processes: myosin ATPase activity (GO:0016887-related), muscle contraction (GO:0006936), cardiac muscle hypertrophy (GO:0003300), extracellular matrix / collagen fibril (fibrosis) remodeling.
- Disease: hypertrophic cardiomyopathy (MONDO:0005045); subtype split obstructive vs non-obstructive.

**Candidate knowledge_gaps / discussion prompts:** items 1–6 in §5, especially (a) unverified ODYSSEY primary report, (b) human fibrosis-reversal unconfirmed, (c) mass-regression load-confound.

---

## 9. Limitations

- Literature-only run; no primary data analyzed. Quantities taken from abstracts, several truncated.
- The decisive nHCM endpoint relied on review synthesis (ODYSSEY primary report not retrieved via tool).
- Rapidly moving field (multiple 2026 reports); hit counts are time-sensitive (PubMed is live).

---

## Artifact Bundle
`kb/hypotheses/Hypertrophic_Cardiomyopathy/myosin_inhibitor_obstruction_vs_substrate/openscientist_artifacts/`
- `MANIFEST.yaml` (schema 1.0, status flags, checksums, traceability)
- `search_log.md` (21-query PubMed log incl. negatives)
- `evidence_matrix.csv` (16 evidence rows)
- `environment.txt` (run-mode/environment record)


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist evidence matrix](openscientist_artifacts/kb_hypotheses_Hypertrophic_Cardiomyopathy_myosin_inhibitor_obstruction_vs_substrate_openscientist_artifacts_evidence_matrix.csv)
- [OpenScientist search log](openscientist_artifacts/kb_hypotheses_Hypertrophic_Cardiomyopathy_myosin_inhibitor_obstruction_vs_substrate_openscientist_artifacts_search_log.md)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000746` (1 mention) - the report calls it "Cell type: cardiomyocyte"; CL calls it **cardiac muscle cell**, and lists "cardiomyocyte" among its other names
- `MONDO:0005045` (1 mention) - the report calls it "Disease: hypertrophic cardiomyopathy"; MONDO calls it **hypertrophic cardiomyopathy**

Every term resolved, and every label the report gave matched.