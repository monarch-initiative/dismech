---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T10:21:26.360487'
end_time: '2026-07-26T10:36:09.068894'
duration_seconds: 882.71
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Coronary Artery Disease
  category: Complex
  hypothesis_group_id: icosapent_ethyl_coronary_plaque_remodeling_model
  hypothesis_label: Icosapent Ethyl Coronary Plaque-Remodeling Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: icosapent_ethyl_coronary_plaque_remodeling_model\n\
    hypothesis_label: Icosapent Ethyl Coronary Plaque-Remodeling Model\nstatus: EMERGING\n\
    description: In statin-treated people with coronary atherosclerosis and persistent\
    \ hypertriglyceridemia,\n  icosapent ethyl may contribute to the observed cardiovascular-event\
    \ contrast by altering coronary plaque\n  composition or progression rather than\
    \ through isolated change in circulating triglyceride concentration.\n  EVAPORATE\
    \ supplies a randomized imaging signal, but it used a mineral-oil comparator and\
    \ a surrogate\n  plaque endpoint and did not test whether plaque change mediated\
    \ clinical events.\nevidence:\n- reference: PMID:32860032\n  reference_title:\
    \ 'Effect of icosapent ethyl on progression of coronary atherosclerosis in patients\
    \ with\n    elevated triglycerides on statin therapy: final results of the EVAPORATE\
    \ trial.'\n  supports: PARTIAL\n  evidence_source: HUMAN_CLINICAL\n  snippet:\
    \ A total of 80 patients were enrolled in this randomized, double-blind, placebo-controlled\
    \ trial.\n  explanation: EVAPORATE was a small mechanistic imaging trial, so its\
    \ randomized plaque-volume signal\n    is hypothesis-generating rather than an\
    \ event-level mechanism result.\n- reference: PMID:32860032\n  reference_title:\
    \ 'Effect of icosapent ethyl on progression of coronary atherosclerosis in patients\
    \ with\n    elevated triglycerides on statin therapy: final results of the EVAPORATE\
    \ trial.'\n  supports: PARTIAL\n  evidence_source: HUMAN_CLINICAL\n  snippet:\
    \ There was a significant reduction in the primary endpoint as IPE reduced LAP\
    \ plaque volume\n    by 17%, while in the placebo group LAP plaque volume more\
    \ than doubled (+109%) (P\u2009=\u20090.0061).\n  explanation: The randomized\
    \ trial supports differential change in a CT-defined coronary plaque surrogate,\n\
    \    not mediation of cardiovascular events or a specific cellular mechanism.\n\
    - reference: PMID:32860032\n  reference_title: 'Effect of icosapent ethyl on progression\
    \ of coronary atherosclerosis in patients with\n    elevated triglycerides on\
    \ statin therapy: final results of the EVAPORATE trial.'\n  supports: PARTIAL\n\
    \  evidence_source: HUMAN_CLINICAL\n  snippet: When further adjusted for age,\
    \ sex, diabetes status, hypertension, and baseline TG, plaque\n    volume changes\
    \ between groups remained significantly different, P\u2009<\u20090.01.\n  explanation:\
    \ Persistence after adjustment for baseline triglyceride is compatible with more\
    \ than baseline-risk\n    imbalance, but it is not a randomized mediation analysis\
    \ of triglyceride response.\nnotes: 'This is a small 80-patient surrogate imaging\
    \ hypothesis, not a treatment-to-pathophysiology edge.\n  REDUCE-IT tested a high-risk\
    \ ASCVD-or-diabetes population broader than coronary artery disease; EVAPORATE\n\
    \  is the coronary-specific lead and did not test clinical outcomes or mediation.\
    \ Focused research must\n  compare plaque remodeling with: remnant- and apolipoprotein-B\
    \ particle number, composition, trafficking,\n  and arterial retention; platelet\
    \ activation and thromboxane biology; specialized inflammatory-resolution\n  lipid\
    \ mediators rather than generic C-reactive-protein lowering; endothelial nitric-oxide\
    \ and vascular-function\n  effects; membrane stabilization, lipid peroxidation,\
    \ and oxidized-lipid effects; and worsening caused\n  by the mineral-oil comparator.\
    \ Achieved-EPA concentrations and other postrandomization biomarker associations\n\
    \  may reflect adherence, absorption, or metabolism and cannot identify a mediator\
    \ without prespecified\n  temporal causal-mediation analysis. Distinguish a causal\
    \ mediator from a baseline effect modifier, parallel\n  pharmacodynamic marker,\
    \ surrogate correlate, or comparator artifact.'"
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
citation_count: 29
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
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
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Coronary Artery Disease
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** icosapent_ethyl_coronary_plaque_remodeling_model
- **Hypothesis Label:** Icosapent Ethyl Coronary Plaque-Remodeling Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: icosapent_ethyl_coronary_plaque_remodeling_model
hypothesis_label: Icosapent Ethyl Coronary Plaque-Remodeling Model
status: EMERGING
description: In statin-treated people with coronary atherosclerosis and persistent hypertriglyceridemia,
  icosapent ethyl may contribute to the observed cardiovascular-event contrast by altering coronary plaque
  composition or progression rather than through isolated change in circulating triglyceride concentration.
  EVAPORATE supplies a randomized imaging signal, but it used a mineral-oil comparator and a surrogate
  plaque endpoint and did not test whether plaque change mediated clinical events.
evidence:
- reference: PMID:32860032
  reference_title: 'Effect of icosapent ethyl on progression of coronary atherosclerosis in patients with
    elevated triglycerides on statin therapy: final results of the EVAPORATE trial.'
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: A total of 80 patients were enrolled in this randomized, double-blind, placebo-controlled trial.
  explanation: EVAPORATE was a small mechanistic imaging trial, so its randomized plaque-volume signal
    is hypothesis-generating rather than an event-level mechanism result.
- reference: PMID:32860032
  reference_title: 'Effect of icosapent ethyl on progression of coronary atherosclerosis in patients with
    elevated triglycerides on statin therapy: final results of the EVAPORATE trial.'
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: There was a significant reduction in the primary endpoint as IPE reduced LAP plaque volume
    by 17%, while in the placebo group LAP plaque volume more than doubled (+109%) (P = 0.0061).
  explanation: The randomized trial supports differential change in a CT-defined coronary plaque surrogate,
    not mediation of cardiovascular events or a specific cellular mechanism.
- reference: PMID:32860032
  reference_title: 'Effect of icosapent ethyl on progression of coronary atherosclerosis in patients with
    elevated triglycerides on statin therapy: final results of the EVAPORATE trial.'
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: When further adjusted for age, sex, diabetes status, hypertension, and baseline TG, plaque
    volume changes between groups remained significantly different, P < 0.01.
  explanation: Persistence after adjustment for baseline triglyceride is compatible with more than baseline-risk
    imbalance, but it is not a randomized mediation analysis of triglyceride response.
notes: 'This is a small 80-patient surrogate imaging hypothesis, not a treatment-to-pathophysiology edge.
  REDUCE-IT tested a high-risk ASCVD-or-diabetes population broader than coronary artery disease; EVAPORATE
  is the coronary-specific lead and did not test clinical outcomes or mediation. Focused research must
  compare plaque remodeling with: remnant- and apolipoprotein-B particle number, composition, trafficking,
  and arterial retention; platelet activation and thromboxane biology; specialized inflammatory-resolution
  lipid mediators rather than generic C-reactive-protein lowering; endothelial nitric-oxide and vascular-function
  effects; membrane stabilization, lipid peroxidation, and oxidized-lipid effects; and worsening caused
  by the mineral-oil comparator. Achieved-EPA concentrations and other postrandomization biomarker associations
  may reflect adherence, absorption, or metabolism and cannot identify a mediator without prespecified
  temporal causal-mediation analysis. Distinguish a causal mediator from a baseline effect modifier, parallel
  pharmacodynamic marker, surrogate correlate, or comparator artifact.'
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

## Issue-Specific Mechanism and Causal-Inference Guardrails

For hypothesis `icosapent_ethyl_coronary_plaque_remodeling_model`, lock the
exposure to icosapent ethyl (IPE; `CHEBI:84883`), an EPA ethyl ester. Record the
exact product, chemical form, EPA and DHA content, dose, duration, and achieved
exposure. Do not conflate IPE with free EPA, dietary fish or fish oil,
over-the-counter supplements, mixed EPA+DHA ethyl esters, or omega-3 carboxylic
acids. EPA-only studies can be mechanistically informative only with formulation,
dose, population, and comparator differences explicit.

The target population is statin-treated people with documented coronary
atherosclerosis and persistent triglyceride elevation. REDUCE-IT randomized
8,179 statin-treated participants with triglycerides 135–499 mg/dL and LDL-C
41–100 mg/dL who had either established cardiovascular disease or diabetes plus
risk factors. Its population and composite outcome were broader than coronary
atherosclerosis. Separate the CAD subset from cerebrovascular/peripheral disease
and diabetes primary-prevention participants; do not convert the whole trial
into a coronary-plaque trial.

REDUCE-IT estimates an IPE-versus-pharmaceutical-grade-mineral-oil contrast, not
IPE versus no treatment or a proven inert placebo. PMID:35762321 found minimal
IPE-arm changes in several inflammatory/oxidation biomarkers while the mineral
oil arm worsened. This neither proves that IPE directly lowered those biomarkers
nor proves that mineral oil explains the clinical-event contrast. Quantify both
possibilities without declaring either settled.

PMID:32860032 (EVAPORATE) enrolled 80 patients, used mineral oil, and measured an
18-month CCTA plaque surrogate. Low-attenuation-plaque change is direct coronary
imaging evidence but not a clinical outcome, cellular mechanism, or
treatment-to-plaque-to-event mediation result. Adjustment for baseline
triglyceride addresses baseline imbalance; it is not mediation by
postrandomization triglyceride change. Because EVAPORATE shares REDUCE-IT's
comparator, it is not independent inert-placebo replication.

Evaluate these candidate mechanisms independently and allow parallel partial
mechanisms:

- circulating triglyceride, remnant cholesterol, apoB particle number,
  composition, trafficking, and arterial proteoglycan retention;
- coronary plaque burden, composition, regression, cap stability, rupture, and
  erosion;
- platelet COX-1/thromboxane signaling, adhesion, aggregation, coagulation, and
  thrombosis;
- specialized pro-resolving lipid mediators and efferocytosis, distinguished
  from generic hsCRP or IL-6 change;
- endothelial nitric-oxide bioavailability and vascular function;
- membrane lipid organization, cholesterol domains, oxidative susceptibility,
  and oxidized lipoproteins;
- mineral-oil comparator effects;
- achieved EPA as adherence, absorption, diet, metabolism, or pharmacokinetic
  exposure rather than a downstream biological mediator;
- atrial fibrillation/flutter and bleeding safety trade-offs.

CCTA, OCT, IVUS, and NIRS are coronary but surrogate. Brachial FMD and blood
biomarkers are systemic; human carotid plaque is anatomically indirect.
Cultured endothelial cells and isolated platelets are `IN_VITRO`. Split
PMID:40397711 into human observational platelet assays, healthy-donor in-vitro
work, and mouse carotid-injury thrombosis; it is not a randomized coronary-event
mechanism study.

Triangulate without collapsing non-equivalent trials. JELIS and RESPECT-EPA are
EPA-only/ethyl-EPA studies with different dose, Japanese population, background
statins, design, and comparator. CHERRY is a small direct-coronary IVUS
surrogate trial of EPA plus pitavastatin after PCI, not IPE 4 g/day event
mediation. STRENGTH used an EPA+DHA carboxylic-acid formulation against corn oil;
its neutral result and achieved-EPA analysis are important competing evidence
but neither directly refutes IPE nor identifies mineral oil as the REDUCE-IT
explanation. MARINE and ANCHOR are short-term lipoprotein/remnant biomarker
studies, not coronary outcome or mediation studies. Treat subgroup, responder,
baseline-EPA/AA, and thin-cap analyses as exploratory unless prespecified and
multiplicity-controlled.

Postrandomization achieved EPA is affected by assignment, adherence, absorption,
diet, metabolism, and health status. Conditioning on it can break randomization
and induce selection or collider bias; it also cannot identify which downstream
EPA pathway acts. Treat REDUCE-IT achieved-EPA analyses and the 2023 EHJ
supplement mediation report (doi:10.1093/eurheartj/ehad655.1309, without an
identified full primary paper/PMID) as secondary or conference analyses, not
definitive causal mediation.

Apply these exact adjudication criteria:

1. Support a mediator only when randomized IPE versus a prevalidated inert
   comparator changes it before plaque/event divergence and a prespecified
   causal indirect effect is estimated with explicit assumptions and sensitivity
   analyses for exposure-induced mediator-outcome confounding.
2. Plaque mediation requires replicated coronary imaging benefit versus an inert
   comparator plus treatment-to-plaque-to-clinical-outcome mediation;
   EVAPORATE alone is `PARTIAL`.
3. A cellular target requires clinically plausible exposure, target-specific
   perturbation or rescue in coronary-relevant cells/models, and concordant
   randomized human pharmacodynamic evidence.
4. Mineral-oil causation of a biomarker contrast requires mineral oil to worsen
   versus inert while IPE and inert do not differ. Explaining a multi-year event
   contrast requires outcome-calibrated evidence, not biomarker extrapolation.
5. Full mediation requires a justified indirect-effect estimand and little
   residual direct effect; ordinary covariate adjustment is insufficient.
6. Refutation requires an adequately powered null/equivalence result with the
   correct IPE formulation, population, timing, comparator, and meaningful
   margin. Small null imaging studies and mixed EPA+DHA trials are not direct
   refutations.

Prioritize REDUCE-IT (PMID:30415628), total events (PMID:30898607),
EVAPORATE (PMID:32860032), mineral-oil biomarkers (PMID:35762321), JELIS
(PMID:17398308), RESPECT-EPA (PMID:38873793), CHERRY (PMID:28863874),
the null overall OCT trial (PMID:32805184), ANCHOR/MARINE particle studies
(PMID:26073397, PMID:23312052, PMID:27596132), and STRENGTH
(PMID:33190147, PMID:33993205) as leads to adjudicate, not assumed conclusions.
Return an evidence matrix with formulation, dose, comparator, population,
confirmed CAD, vascular site, study component/source type, endpoint, timing,
bias/conflicts, and causal verdict.

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
evidence or experiment would resolve it.

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

If the provider supports artifacts, produce artifact-friendly outputs such as an
evidence matrix, mechanistic diagram, knowledge-gap table, or comparison table.
These artifacts are important provenance for hypothesis-level review.


## Output

# Mechanistic Hypothesis Search — Icosapent Ethyl Coronary Plaque-Remodeling Model

**Disease:** Coronary Artery Disease (Complex)
**Hypothesis ID:** `icosapent_ethyl_coronary_plaque_remodeling_model`
**KB Status:** EMERGING
**Search date:** 2026-07-26 · 5 iterations · 9 findings · 62 papers reviewed

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED at the surrogate-imaging level; causally UNRESOLVED at the treatment→plaque→event level.** The seed hypothesis proposes that in statin-treated people with coronary atherosclerosis and persistent hypertriglyceridemia, icosapent ethyl (IPE; CHEBI:84883, EPA ethyl ester, 4 g/day) contributes to the cardiovascular-event benefit by *altering coronary plaque composition or progression* rather than through isolated triglyceride lowering. The literature supplies genuine, randomized coronary-imaging support for the plaque-remodeling *phenotype* — but no study closes the causal chain from plaque change to clinical events, and the strongest imaging trial shares a non-inert comparator with the pivotal outcome trial.

Three pillars determine this verdict. First, **the coronary-imaging signal is real but thin and comparator-confounded**: EVAPORATE ([PMID:32860032](https://pubmed.ncbi.nlm.nih.gov/32860032/)) is an 80-patient CCTA trial showing a 17% reduction in low-attenuation plaque (LAP) with IPE versus a +109% rise on placebo (P=0.0061), and CHERRY ([PMID:28863874](https://pubmed.ncbi.nlm.nih.gov/28863874/)) independently shows EPA+statin reduces atheroma and lipid volume on IVUS. But EVAPORATE used pharmaceutical-grade mineral oil, the same comparator as REDUCE-IT, and the best-controlled OCT cap-stability endpoint was null overall ([PMID:32805184](https://pubmed.ncbi.nlm.nih.gov/32805184/)). Second, **the clinical benefit is established but mechanism-agnostic**: REDUCE-IT ([PMID:30415628](https://pubmed.ncbi.nlm.nih.gov/30415628/)) shows a 25% relative risk reduction (HR 0.75), largest in the prior-PCI/coronary subset (HR 0.66, [PMID:35261279](https://pubmed.ncbi.nlm.nih.gov/35261279/)), yet the trial measured no coronary plaque and performed no mediation. Third, **a comparator artifact and a parallel lipoprotein mechanism are live competitors**: the mineral-oil arm worsened multiple atherosclerosis biomarkers while IPE changed them minimally ([PMID:35762321](https://pubmed.ncbi.nlm.nih.gov/35762321/)), and IPE demonstrably lowers apoB, remnant cholesterol, and atherogenic particle number ([PMID:31277790](https://pubmed.ncbi.nlm.nih.gov/31277790/), [PMID:26073397](https://pubmed.ncbi.nlm.nih.gov/26073397/)) — a plausibly upstream mechanism that could drive both plaque change and events.

**Most important caveats:** (1) No prespecified, temporally-ordered causal-mediation analysis of treatment→plaque→event exists; adjustment for baseline triglyceride in EVAPORATE addresses baseline imbalance, not mediation by post-randomization change. (2) The plaque-remodeling model and the apoB/remnant-particle model are not mutually exclusive and are currently unquantified relative to each other. (3) The EPA-class benefit appears formulation-specific (purified EPA positive; EPA+DHA carboxylic-acid STRENGTH neutral against an *inert* comparator), which strengthens the case for a genuine EPA effect but does not localize it to the coronary plaque. The model should remain **EMERGING**.

---

## Key Findings

### F001 — EVAPORATE is the only randomized coronary-imaging signal for IPE plaque remodeling, and it is small and comparator-confounded

EVAPORATE ([PMID:32860032](https://pubmed.ncbi.nlm.nih.gov/32860032/)) randomized 80 statin-treated patients with coronary atherosclerosis (≥20% stenosis) and triglycerides 135–499 mg/dL (median 259 mg/dL) to IPE 4 g/day or mineral-oil placebo, with serial coronary CT angiography over 18 months. The verbatim primary result: *"There was a significant reduction in the primary endpoint as IPE reduced LAP plaque volume by 17%,"* while placebo LAP volume *more than doubled (+109%)* (P=0.0061). Differences persisted after adjustment for age, sex, diabetes, hypertension, and baseline triglyceride (P<0.01). This is the coronary-specific lead for the hypothesis and provides a genuinely randomized signal of differential plaque change.

Three constraints keep this at **PARTIAL** support. (1) *"A total of 80 patients were enrolled in this randomized, double-blind, placebo-controlled trial"* — the sample is small, making the result hypothesis-generating. (2) LAP is a CT surrogate, not a clinical outcome, cellular mechanism, or mediation result. (3) The comparator is mineral oil, not a proven inert placebo, so part of the between-arm contrast could reflect comparator-arm worsening rather than IPE benefit. Adjustment for *baseline* triglyceride is not mediation by *post-randomization* triglyceride change.

### F002 — The mineral-oil comparator worsened atherosclerosis biomarkers: a competing comparator-artifact explanation

The REDUCE-IT biomarker substudy (Ridker et al., [PMID:35762321](https://pubmed.ncbi.nlm.nih.gov/35762321/)) reports that *"allocation to icosapent ethyl had minimal effects on a series of biomarkers associated with atherosclerotic disease,"* whereas the mineral-oil arm rose at 12 months: median +28.9% IL-1β, +21.9% hsCRP, +18.5% Lp-PLA2, +16.2% IL-6, +10.9% oxidized LDL, +2.2% Lp(a), +1.5% homocysteine. Mechanistically, this means a substantial part of the between-arm biomarker contrast is driven by the comparator worsening rather than IPE lowering. This does **not** prove mineral oil explains the multi-year *event* contrast (that would require outcome-calibrated evidence, not biomarker extrapolation), but it is a genuine competing explanation that must be quantified, not dismissed. Because EVAPORATE shares this comparator, EVAPORATE is not independent inert-placebo replication.

### F003 — RESPECT-EPA replicates an EPA outcome benefit in CAD without a mineral-oil comparator, but at low dose and open-label

RESPECT-EPA ([PMID:38873793](https://pubmed.ncbi.nlm.nih.gov/38873793/)) randomized Japanese patients with stable CAD and a low EPA/AA ratio (<0.4) on statins to icosapent ethyl 1800 mg/day or a no-oil control, open-label with blinded endpoints. *"The primary end point occurred in 112 of 1225 patients (9.1%) and 155 of 1235 patients (12.6%) in the EPA and control group, respectively (hazard ratio, 0.79 [95% CI, 0.62–1.00])"* — a borderline benefit. Critically, the control arm used no oil, so the EPA-class event benefit is at least partly comparator-independent, weakening (though not eliminating) the pure comparator-artifact hypothesis. However, the dose (1800 mg) is below IPE 4 g, the design is open-label, the population is Japanese with different baseline fish intake, and the trial reports clinical events, not plaque mediation. A robustness meta-analysis ([PMID:41870913](https://pubmed.ncbi.nlm.nih.gov/41870913/)) gives REDUCE-IT HR 0.75 (fragility index 123), RESPECT-EPA HR 0.71 (FI 49), JELIS HR 0.81 (FI 15) — consistent direction, decreasing robustness.

### F004 — Formulation specificity: purified EPA positive, EPA+DHA STRENGTH neutral against an inert comparator

STRENGTH ([PMID:33993205](https://pubmed.ncbi.nlm.nih.gov/33993205/)/PMID:33190147) randomized 13,078 high-risk patients to 4 g/day omega-3 *carboxylic acid (EPA+DHA)* versus *"an inert comparator, corn oil."* The trial was neutral, and a prespecified secondary analysis found achieved plasma EPA/DHA levels were **not** associated with reduced cardiovascular outcomes. Because the comparator was inert, STRENGTH's neutrality cannot be blamed on comparator harm and forms a genuine competing datapoint on formulation specificity. A meta-analysis ([PMID:40974959](https://pubmed.ncbi.nlm.nih.gov/40974959/)) found *"CVD-attributable mortality was significantly reduced with purified EPA (HR: 0.79 [95% CI: 0.67–0.94]; P=0.006); this effect was less"* pronounced for mixed EPA/DHA. Together with JELIS ([PMID:17398308](https://pubmed.ncbi.nlm.nih.gov/17398308/), HR 0.81) and RESPECT-EPA, this supports an **EPA-formulation-specific** mechanism — but formulation specificity localizes the effect to the molecule, not to the coronary plaque.

### F005 — Independent coronary-imaging surrogates are mixed: EPA reduces plaque/lipid volume (CHERRY) but did not increase fibrous-cap thickness overall (null OCT)

CHERRY ([PMID:28863874](https://pubmed.ncbi.nlm.nih.gov/28863874/)) randomized 193 post-PCI CHD patients to pitavastatin 4 mg ± EPA 1800 mg over 6–8 months with integrated-backscatter IVUS: *"The PTV/EPA group showed a greater reduction in total atheroma volume compared to PTV group. IB-IVUS analyses revealed that lipid volume was significantly decreased during follow-up period in only PTV/EPA group."* This independently corroborates the plaque-composition remodeling phenotype on a different modality.

However, the best-controlled cap-stability endpoint was null: the OCT ACS trial ([PMID:32805184](https://pubmed.ncbi.nlm.nih.gov/32805184/)) randomized 130 ACS patients to statin ± EPA 1800 mg ± EPA/DHA and found *"no significant differences in the percent change for minimum FCT between the EPA or EPA+DHA group and the control group"*; fibrous-cap thickness increased in all groups. Cap-thickening benefit appeared only in a prespecified-median thin-cap (<120 µm) subgroup (exploratory). An earlier small OCT TCFA study (n=30, [PMID:24637411](https://pubmed.ncbi.nlm.nih.gov/24637411/)) did show greater cap thickening with EPA+statin. Net: plaque *volume/composition* remodeling is reproducibly seen; *cap-stabilization* is not established overall.

### F006 — IPE 4 g lowers apoB, remnant cholesterol, and atherogenic particle number: the leading parallel/upstream mechanism

In ANCHOR (12 weeks, statin-treated, TG 200–499 mg/dL, [PMID:31277790](https://pubmed.ncbi.nlm.nih.gov/31277790/)), IPE 4 g/day versus placebo reduced *"remnant lipoprotein cholesterol (−23.0%; p=0.0125), apolipoprotein B (−7.4%; p=0.0021), apolipoprotein C-III (−16%; p<0.0001), oxidized LDL (−13.7%; p=0.0020)"* without raising LDL-C. The NMR substudy ([PMID:26073397](https://pubmed.ncbi.nlm.nih.gov/26073397/)) showed *"IPE 4 g/day significantly reduced concentrations of: total (12.2%), large (46.4%), and medium (12.1%) VLDL particles; total (7.7%) and small (13.5%) LDL particles."* Pooled MARINE/ANCHOR data ([PMID:25893544](https://pubmed.ncbi.nlm.nih.gov/25893544/), [PMID:22819432](https://pubmed.ncbi.nlm.nih.gov/22819432/)) show ~9% apoB and 22–40% hsCRP reductions. Because atherogenic apoB particles cross and are retained in the arterial intima ([PMID:36889989](https://pubmed.ncbi.nlm.nih.gov/36889989/)), this mechanism is *upstream* of — and could fully explain — the plaque change EVAPORATE observed. These are short-term biomarker studies with a mineral-oil-type placebo, not outcome or mediation studies, but they define the single most parsimonious competing model.

### F007 — Safety trade-off: increased atrial fibrillation/flutter and a bleeding signal

In REDUCE-IT, IPE *"was associated with increased atrial fibrillation/atrial flutter (AF) hospitalization (3.1% IPE versus 2.1% placebo)"* ([PMID:36802845](https://pubmed.ncbi.nlm.nih.gov/36802845/)), plus a serious-bleeding signal ([PMID:40982548](https://pubmed.ncbi.nlm.nih.gov/40982548/)). Real-world cohorts (VA, [PMID:39797933](https://pubmed.ncbi.nlm.nih.gov/39797933/); MarketScan, [PMID:40148153](https://pubmed.ncbi.nlm.nih.gov/40148153/)) reproduce AF/bleeding signals at generally lower absolute frequencies. These effects confirm IPE biological activity and are relevant to net benefit but are orthogonal to plaque remodeling.

### F008 — EPA-specific membrane/antioxidant mechanism supported in vitro, lacking randomized human coronary pharmacodynamic confirmation

In vitro, EPA *"was found to inhibit LDL oxidation in a dose-dependent manner (1.0–10.0 µM) and was distinguished from the other TG-lowering agents, which had no significant effect"* ([PMID:25449996](https://pubmed.ncbi.nlm.nih.gov/25449996/), Mason & Jacob), and prevented glucose-induced cholesterol crystalline-domain formation. A mechanistic review ([PMID:38252923](https://pubmed.ncbi.nlm.nih.gov/38252923/)) synthesizes EPA-vs-DHA differences: *"event reduction appears related to achieved EPA levels suggesting that the particular chemical and biological properties of EPA... may contribute to its distinct clinical efficacy."* Endothelial-NO evidence retrieved was largely mixed-formulation (EPA:DHA 6:1) or animal/ex vivo ([PMID:30878386](https://pubmed.ncbi.nlm.nih.gov/30878386/), [PMID:31830469](https://pubmed.ncbi.nlm.nih.gov/31830469/)), **not IPE-specific randomized human coronary data**. The dedicated IPE platelet/thrombosis study (PMID:40397711) could not be surfaced in this search environment — a curation-relevant absence.

### F009 — REDUCE-IT establishes the event benefit (HR 0.75), largest in the coronary subset (HR 0.66), but tests no mechanism

REDUCE-IT ([PMID:30415628](https://pubmed.ncbi.nlm.nih.gov/30415628/)): 8,179 statin-treated patients (70.7% secondary prevention), TG 135–499 mg/dL, LDL-C 41–100 mg/dL, IPE 4 g/day vs mineral oil, median 4.9 y. *"A primary end-point event occurred in 17.2% of the patients in the icosapent ethyl group, as compared with 22.0% of the patients in the placebo group (hazard ratio, 0.75; 95% CI, 0.68 to 0.83; P<0.001)."* Total (first+recurrent) events fell ~30% ([PMID:30898607](https://pubmed.ncbi.nlm.nih.gov/30898607/)). The prior-PCI coronary subset (n=3408) showed *"a 34% reduction in the primary composite end point (hazard ratio, 0.66; 95% CI, 0.58–0.76)"* ([PMID:35261279](https://pubmed.ncbi.nlm.nih.gov/35261279/)); US subset HR 0.69 ([PMID:31707829](https://pubmed.ncbi.nlm.nih.gov/31707829/)). The trial reports outcomes only — no coronary plaque measurement, no mediation, mineral-oil comparator. The larger coronary-subset effect is *consistent with* but not *proof of* a coronary locus of action.

---

## Mechanistic Model / Interpretation

The hypothesis posits the following causal chain. Below, each link is annotated with the strength of evidence found.

```
 IPE 4 g/day (EPA ethyl ester, CHEBI:84883)
        │  [STRONG: exposure well-defined; achieved-EPA measurable]
        ▼
 EPA incorporation into plasma phospholipids / plaque cell membranes
        │  [MODERATE in vitro; NOT confirmed by randomized human coronary PD]
        ▼
 ┌─────────────────────── PARALLEL, NON-EXCLUSIVE MECHANISMS ───────────────────────┐
 │ (A) ↓ apoB / remnant-C / VLDL & small-LDL particle number   [STRONG: ANCHOR/MARINE]│
 │ (B) ↓ LDL & membrane lipid oxidation, cholesterol domains   [IN VITRO only]        │
 │ (C) membrane stabilization / ↑ endothelial NO               [MIXED-form/ animal]   │
 │ (D) ↓ intra-plaque inflammation / SPM (resolvin) signaling  [SPECULATIVE-coronary] │
 │ (E) antithrombotic / platelet COX-1–thromboxane effects     [NOT retrievable-IPE]  │
 └───────────────────────────────────────┬──────────────────────────────────────────┘
        ▼                                   ▼
 ↓ arterial retention of              Favorable coronary plaque remodeling
   atherogenic particles (inferred)   ↓ LAP volume (EVAPORATE/CCTA)  [PARTIAL]
        │                             ↓ atheroma/lipid volume (CHERRY/IVUS) [SUPPORTIVE]
        │                             cap thickening NULL overall (OCT) [LIMITING]
        └──────────────────┬──────────────────┘
                           ▼
             ??? treatment→plaque→event MEDIATION ???   [MISSING — no study]
                           ▼
        ↓ MI / CV events (REDUCE-IT HR 0.75; coronary subset 0.66) [STRONG]
```

**Where the literature is strong:** the exposure definition (IPE 4 g), the biomarker/lipoprotein pharmacodynamics (mechanism A), and the terminal clinical-event benefit (REDUCE-IT). **Where links are inferred:** the step from EPA membrane incorporation to plaque composition change, and from particle-number lowering to arterial retention. **Where causal steps are missing entirely:** the plaque→event mediation node — no trial has measured coronary plaque *and* clinical events with a prespecified indirect-effect estimand. This missing node is the single most important gap; it is why the plaque-remodeling model cannot be elevated above EMERGING regardless of how convincing the imaging phenotype appears.

The most parsimonious alternative reading is that mechanism (A) — apoB/remnant-particle lowering — is the true upstream driver, producing *both* the imaging plaque change *and* the events, with "plaque remodeling" being a downstream readout rather than an independent mechanism. The data cannot currently distinguish "plaque remodeling as mediator" from "plaque remodeling as parallel surrogate of particle lowering."

---

## Evidence Matrix

| Citation | Type | Role | Mechanistic claim tested | Key finding | Formulation / Comparator | Population / CAD | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| [PMID:32860032](https://pubmed.ncbi.nlm.nih.gov/32860032/) EVAPORATE | Human clinical (CCTA) | **Supports (PARTIAL)** | IPE alters coronary plaque composition/progression | LAP −17% vs +109% placebo (P=0.0061) | IPE 4 g / mineral oil | Statin-treated CAD, TG 135–499 | n=80; surrogate; non-inert comparator; no mediation |
| [PMID:35762321](https://pubmed.ncbi.nlm.nih.gov/35762321/) | Human clinical (biomarker) | **Competing (artifact)** | Between-arm contrast = comparator harm | IPE minimal change; mineral oil ↑ hsCRP/IL-6/oxLDL | IPE 4 g / mineral oil | REDUCE-IT substudy | Does not prove event contrast is artifact |
| [PMID:38873793](https://pubmed.ncbi.nlm.nih.gov/38873793/) RESPECT-EPA | Human clinical (events) | **Qualifies/Supports** | EPA event benefit without mineral oil | HR 0.79 (0.62–1.00) | Ethyl-EPA 1800 mg / no-oil | Japanese stable CAD, EPA/AA<0.4 | Open-label; low dose; borderline; no plaque mediation |
| [PMID:33993205](https://pubmed.ncbi.nlm.nih.gov/33993205/) STRENGTH | Human clinical (events) | **Competing (formulation)** | EPA+DHA event benefit vs inert oil | Neutral; achieved EPA/DHA not associated with benefit | EPA+DHA carboxylic acid 4 g / corn oil | High CV risk, high TG/low HDL | Different formulation; inert comparator |
| [PMID:40974959](https://pubmed.ncbi.nlm.nih.gov/40974959/) | Review/meta | **Qualifies** | Formulation specificity of mortality benefit | Purified EPA HR 0.79 (0.67–0.94); mixed weaker | Purified EPA vs EPA/DHA | Pooled | Meta-level; heterogeneity |
| [PMID:28863874](https://pubmed.ncbi.nlm.nih.gov/28863874/) CHERRY | Human clinical (IVUS) | **Supports** | EPA+statin reduces atheroma/lipid volume | Greater TAV reduction; lipid volume ↓ only in EPA arm | EPA 1800 mg + pitavastatin | Post-PCI CHD | n=193; EPA not IPE 4 g; short term |
| [PMID:32805184](https://pubmed.ncbi.nlm.nih.gov/32805184/) | Human clinical (OCT) | **Qualifies/Limits** | EPA increases fibrous-cap thickness | No between-group FCT difference overall | EPA 1800 mg ± DHA + statin | ACS | n=130; benefit only in thin-cap subgroup (exploratory) |
| [PMID:24637411](https://pubmed.ncbi.nlm.nih.gov/24637411/) | Human clinical (OCT) | Supports | EPA+statin stabilizes TCFA | Greater cap thickening, less macrophage | EPA 1800 mg + rosuvastatin | Dyslipidemia TCFA | n=30; very small |
| [PMID:31277790](https://pubmed.ncbi.nlm.nih.gov/31277790/) ANCHOR | Human clinical (biomarker) | **Competing (upstream)** | IPE lowers apoB/remnant/oxLDL | RemnantC −23%, apoB −7.4%, apoC-III −16%, oxLDL −13.7% | IPE 4 g / placebo | Statin-treated, TG 200–499 | 12 wk; surrogate; mineral-oil-type placebo |
| [PMID:26073397](https://pubmed.ncbi.nlm.nih.gov/26073397/) | Human clinical (NMR) | **Competing (upstream)** | IPE lowers atherogenic particle number | ↓ VLDL, total/small LDL particles | IPE 4 g / placebo | Statin-treated, high TG | Surrogate; short-term |
| [PMID:25893544](https://pubmed.ncbi.nlm.nih.gov/25893544/) | Human clinical | Competing/Supports | IPE lowers hsCRP/apoB | hsCRP −40%/−23%; apoB −9% | IPE 4 g / placebo | Metabolic syndrome | Post hoc exploratory |
| [PMID:30415628](https://pubmed.ncbi.nlm.nih.gov/30415628/) REDUCE-IT | Human clinical (events) | **Supports (terminal)** | IPE reduces CV events | 17.2% vs 22.0%, HR 0.75 | IPE 4 g / mineral oil | ASCVD or DM+risk | No plaque/mediation; non-inert comparator |
| [PMID:30898607](https://pubmed.ncbi.nlm.nih.gov/30898607/) | Human clinical (events) | Supports | Total ischemic events | ~30% reduction | IPE 4 g / mineral oil | Same | Same comparator caveat |
| [PMID:35261279](https://pubmed.ncbi.nlm.nih.gov/35261279/) | Human clinical (subgroup) | Supports (coronary) | Coronary locus of benefit | Prior-PCI HR 0.66 (0.58–0.76) | IPE 4 g / mineral oil | Prior-PCI n=3408 | Subgroup; not mechanism |
| [PMID:41870913](https://pubmed.ncbi.nlm.nih.gov/41870913/) | Review/meta | Qualifies | Robustness of EPA trials | Fragility index 123/49/15 | Purified EPA | Pooled | Fragility of smaller trials |
| [PMID:25449996](https://pubmed.ncbi.nlm.nih.gov/25449996/) | In vitro | Supports (cellular) | EPA-specific antioxidant/membrane effect | EPA inhibits LDL oxidation dose-dependently | EPA (free) | Cell-free/membrane | IN VITRO; not coronary PD |
| [PMID:38252923](https://pubmed.ncbi.nlm.nih.gov/38252923/) | Review | Orientation | EPA-vs-DHA mechanistic differences | Synthesis of membrane/oxidation/endothelial | — | — | Review-level only |
| [PMID:36802845](https://pubmed.ncbi.nlm.nih.gov/36802845/) | Human clinical (safety) | Orthogonal | AF/flutter safety | AF hosp 3.1% vs 2.1% | IPE 4 g / mineral oil | REDUCE-IT | Confirms activity; net-benefit trade-off |

---

## Evidence Base — How Key Papers Support or Challenge the Hypothesis

- **Support the plaque-remodeling phenotype:** EVAPORATE (CCTA LAP, [PMID:32860032](https://pubmed.ncbi.nlm.nih.gov/32860032/)) and CHERRY (IVUS atheroma/lipid volume, [PMID:28863874](https://pubmed.ncbi.nlm.nih.gov/28863874/)) provide two independent, randomized, different-modality coronary imaging signals that IPE/EPA plus statin favorably alters plaque volume and composition.
- **Challenge / limit the phenotype:** The best-controlled OCT cap-stability trial ([PMID:32805184](https://pubmed.ncbi.nlm.nih.gov/32805184/)) was null overall for fibrous-cap thickness, limiting the "cap stabilization" translation of remodeling to exploratory subgroups.
- **Challenge via comparator artifact:** The REDUCE-IT biomarker substudy ([PMID:35762321](https://pubmed.ncbi.nlm.nih.gov/35762321/)) shows the mineral-oil comparator worsened biomarkers, offering an alternative reading of any mineral-oil-controlled contrast.
- **Offer a competing upstream mechanism:** ANCHOR/MARINE ([PMID:31277790](https://pubmed.ncbi.nlm.nih.gov/31277790/), [PMID:26073397](https://pubmed.ncbi.nlm.nih.gov/26073397/), [PMID:25893544](https://pubmed.ncbi.nlm.nih.gov/25893544/)) establish IPE's apoB/remnant/particle lowering, which could drive both plaque change and events.
- **Anchor the clinical benefit the model tries to explain:** REDUCE-IT ([PMID:30415628](https://pubmed.ncbi.nlm.nih.gov/30415628/), [PMID:30898607](https://pubmed.ncbi.nlm.nih.gov/30898607/), [PMID:35261279](https://pubmed.ncbi.nlm.nih.gov/35261279/)).
- **Triangulate the EPA-class effect / formulation specificity:** JELIS ([PMID:17398308](https://pubmed.ncbi.nlm.nih.gov/17398308/)), RESPECT-EPA ([PMID:38873793](https://pubmed.ncbi.nlm.nih.gov/38873793/)), STRENGTH ([PMID:33993205](https://pubmed.ncbi.nlm.nih.gov/33993205/)), meta-analysis ([PMID:40974959](https://pubmed.ncbi.nlm.nih.gov/40974959/)), robustness ([PMID:41870913](https://pubmed.ncbi.nlm.nih.gov/41870913/)).

---

## Knowledge Gaps

| # | Gap (scope) | Why it matters | What was checked | Resolving evidence/experiment |
|---|---|---|---|---|
| G1 | **No treatment→plaque→event mediation** (core causal edge) | This is *the* claim of the hypothesis; without it, plaque change is only a correlated surrogate | EVAPORATE, CHERRY, REDUCE-IT — none link plaque change to events by prespecified indirect effect | A trial/pooled dataset with serial coronary imaging AND adjudicated events, analyzed with a justified indirect-effect estimand and sensitivity analysis for exposure-induced mediator-outcome confounding |
| G2 | **Plaque signal not replicated vs an inert comparator** | EVAPORATE shares mineral oil with REDUCE-IT; cannot separate IPE benefit from comparator harm | EVAPORATE (mineral oil); STRENGTH used corn oil but is EPA+DHA and imaged no coronary plaque | Coronary CCTA/IVUS RCT of IPE 4 g vs a prevalidated inert comparator (corn oil) with LAP endpoint |
| G3 | **apoB/remnant lowering vs plaque remodeling not disentangled** | The parallel lipoprotein mechanism could fully explain the plaque change (collinear surrogates) | ANCHOR/MARINE (particles) and EVAPORATE (plaque) exist separately, never jointly modeled | Joint longitudinal study measuring particle number and plaque volume in the same patients with mediation modeling |
| G4 | **Cap-stabilization unproven overall** | Rupture/erosion prevention is the presumed clinical translation of "remodeling" | OCT trial null overall; benefit only in thin-cap subgroup | Adequately powered OCT trial of IPE 4 g with prespecified min-FCT endpoint |
| G5 | **IPE-specific antithrombotic/platelet coronary data absent** | Antithrombotic axis is invoked in reviews but unconfirmed for IPE in humans | Dedicated IPE platelet-thrombosis study (PMID:40397711) not retrievable in this environment | Retrieve/verify PMID:40397711; randomized IPE platelet-function pharmacodynamics |
| G6 | **Endothelial-NO evidence is mixed-formulation/animal** | Vascular-function is a candidate mediator distinct from lipids | Retrieved EPA:DHA 6:1 and rodent/ex-vivo data only | Randomized IPE-4g human coronary/brachial vascular-function study |
| G7 | **Mineral-oil event causation unquantified** | Determines how much of REDUCE-IT is "IPE benefit" vs "comparator harm" | Biomarker substudy shows comparator worsening, not event attribution | Outcome-calibrated modeling / trial with inert comparator |
| G8 | **No omics/mediation dataset located** | Curation-relevant absence as of search date | Literature search only; no trial-level mediation dataset surfaced | Access to REDUCE-IT/EVAPORATE patient-level data for formal mediation |

---

## Alternative / Competing Models

1. **apoB / remnant-cholesterol / atherogenic-particle-number lowering (parallel, plausibly upstream).** Strongly supported by ANCHOR/MARINE ([PMID:31277790](https://pubmed.ncbi.nlm.nih.gov/31277790/), [PMID:26073397](https://pubmed.ncbi.nlm.nih.gov/26073397/)) and remnant-cholesterol biology ([PMID:36889989](https://pubmed.ncbi.nlm.nih.gov/36889989/)). Leading competitor; could be *upstream* of plaque remodeling, making "plaque remodeling" a downstream consequence rather than an independent mechanism.

2. **Mineral-oil comparator artifact (alternative/competing).** Supported by the biomarker substudy ([PMID:35762321](https://pubmed.ncbi.nlm.nih.gov/35762321/)). Argues part of both the imaging and event contrasts reflect comparator worsening. Weakened but not eliminated by RESPECT-EPA's no-oil control.

3. **EPA-formulation-specific molecular effect (parallel, molecule-level).** Purified EPA positive vs EPA+DHA neutral ([PMID:40974959](https://pubmed.ncbi.nlm.nih.gov/40974959/), STRENGTH). Localizes benefit to the EPA molecule but not specifically to coronary plaque.

4. **Membrane-stabilization / antioxidant / anti-oxidized-lipoprotein (parallel, cellular; possibly upstream of the imaging phenotype).** In vitro support ([PMID:25449996](https://pubmed.ncbi.nlm.nih.gov/25449996/)); lacks randomized human coronary PD.

5. **Specialized pro-resolving mediators (resolvins) / anti-inflammatory (speculative for coronary).** Reviews invoke RvE1–RvE3; direct IPE-coronary evidence not found.

6. **Antithrombotic / platelet COX-1–thromboxane (parallel, event-proximal).** Biologically plausible; IPE-specific human coronary evidence not retrievable here. Would act at the plaque→event step rather than on plaque composition.

7. **Endothelial NO / vascular function (parallel).** Mixed-formulation/animal support only ([PMID:30878386](https://pubmed.ncbi.nlm.nih.gov/30878386/), [PMID:31830469](https://pubmed.ncbi.nlm.nih.gov/31830469/)).

---

## Discriminating Tests / Proposed Follow-up Actions

1. **Inert-comparator coronary-imaging RCT (resolves G2).** Randomize statin-treated CAD patients with TG 135–499 mg/dL to IPE 4 g vs *corn oil* (inert), serial CCTA LAP at 0/18 months. *Expected if hypothesis true:* LAP reduction persists vs inert comparator. *Expected if artifact:* signal attenuates.

2. **Joint particle-and-plaque mediation study (resolves G1/G3).** In the same patients, measure NMR particle number and CCTA/IVUS plaque longitudinally; fit a prespecified causal-mediation model with sensitivity analysis. *Expected:* if apoB/remnant lowering fully mediates plaque change, the direct EPA→plaque effect shrinks toward null.

3. **Powered OCT cap-stability trial (resolves G4).** IPE 4 g vs inert, prespecified min-FCT primary endpoint, stratified by baseline cap thickness. *Expected:* overall FCT increase if cap-stabilization is real; subgroup-only if not.

4. **Patient-level mediation of REDUCE-IT (resolves G1/G7).** Using adjudicated events, estimate the indirect effect through post-randomization apoB/remnant change vs residual direct effect, with exposure-induced confounding sensitivity — treating achieved-EPA analyses as secondary given collider-bias risk.

5. **Randomized IPE-4g human pharmacodynamics (resolves G5/G6).** Platelet aggregation/thromboxane and coronary/brachial vascular function under IPE 4 g vs inert, to confirm or exclude antithrombotic and endothelial axes.

6. **Retrieve PMID:40397711** and split into human observational platelet assays, healthy-donor in-vitro work, and mouse carotid-injury thrombosis before any KB edge is drawn.

---

## Curation Leads (require curator verification)

- **Status:** Keep `status: EMERGING`. The plaque-remodeling edge is `PARTIAL` (EVAPORATE) with an unconfirmed plaque→event mediation node.
- **Candidate evidence references / snippets to verify:**
  - [PMID:28863874](https://pubmed.ncbi.nlm.nih.gov/28863874/) — *"lipid volume was significantly decreased during follow-up period in only PTV/EPA group"* (supports plaque-composition remodeling; EPA+pitavastatin, not IPE 4 g).
  - [PMID:32805184](https://pubmed.ncbi.nlm.nih.gov/32805184/) — *"no significant differences in the percent change for minimum FCT"* (add as LIMITING evidence on cap stabilization).
  - [PMID:35762321](https://pubmed.ncbi.nlm.nih.gov/35762321/) — *"allocation to icosapent ethyl had minimal effects on a series of biomarkers"* (competing comparator-artifact node).
  - [PMID:31277790](https://pubmed.ncbi.nlm.nih.gov/31277790/) — *"remnant lipoprotein cholesterol (−23.0%...), apolipoprotein B (−7.4%...)"* (competing upstream lipoprotein node).
  - [PMID:38873793](https://pubmed.ncbi.nlm.nih.gov/38873793/) — *"hazard ratio, 0.79 [95% CI, 0.62–1.00]"* (no-oil-comparator EPA event benefit; qualifies comparator-artifact model).
- **Candidate pathophysiology nodes/edges:** IPE → ↓apoB/remnant particle number → ↓arterial retention → plaque remodeling (label edges INFERRED); IPE → coronary LAP reduction (PARTIAL); plaque remodeling → CV events (UNCONFIRMED/MISSING).
- **Candidate ontology terms:** low-attenuation coronary plaque; fibrous-cap thickness; apolipoprotein-B-containing lipoprotein; remnant cholesterol; VLDL/LDL particle number; thin-cap fibroatheroma; specialized pro-resolving mediators (resolvin E-series).
- **Candidate subtype restriction:** best-explained subtype = statin-treated CAD with persistent TG 135–499 mg/dL and prior-PCI/coronary phenotype (REDUCE-IT prior-PCI HR 0.66).
- **Candidate `knowledge_gaps`:** G1 (missing plaque→event mediation), G2 (no inert-comparator replication), G3 (apoB vs plaque collinearity), G7 (mineral-oil event attribution unquantified), plus source absence: PMID:40397711 not retrievable and no patient-level mediation dataset located as of 2026-07-26.

---

## Limitations of This Search

- PubMed access was via a proxy; at least one prioritized paper (PMID:40397711, IPE platelet/thrombosis) could not be retrieved, and the 2023 EHJ mediation supplement (doi:10.1093/eurheartj/ehad655.1309) lacks an identified primary PMID — both are treated as unresolved.
- No patient-level trial data, omics, or formal mediation datasets were available; all mediation judgments are inferential from published summary statistics.
- Subgroup, responder, baseline-EPA/AA, and thin-cap analyses are treated as exploratory unless prespecified and multiplicity-controlled.
- EPA-only non-IPE trials (JELIS, RESPECT-EPA, CHERRY, OCT) are triangulating evidence with explicit formulation/dose/population/comparator differences, not direct IPE-4g replication.

---

*Report generated from 5 iterations, 9 confirmed findings, 62 papers reviewed. Exposure locked to icosapent ethyl (IPE; CHEBI:84883), EPA ethyl ester, 4 g/day unless otherwise stated.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
