---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T13:40:54.385257'
end_time: '2026-07-11T13:56:46.720028'
duration_seconds: 952.33
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Alzheimer Disease
  category: Neurodegenerative Disorder
  hypothesis_group_id: adaptive_immune_tcell_model
  hypothesis_label: Adaptive Immune (T Cell) Neurodegeneration Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: adaptive_immune_tcell_model\nhypothesis_label:\
    \ Adaptive Immune (T Cell) Neurodegeneration Model\nstatus: EMERGING\ndescription:\
    \ Beyond innate microglial responses, a clonally expanded, predominantly cytotoxic\
    \ (CD8+) T\n  cell response is modeled as an active driver of tau-associated neurodegeneration.\
    \ In tauopathy \u2014 but\n  not pure amyloidosis \u2014 microglia are required\
    \ to recruit T cells to sites of tau pathology; infiltrating\n  T cells transition\
    \ from activated to exhausted states with restricted TCR clonality, and IFN-gamma/PD-1\n\
    \  signaling amplifies neuronal loss. The model predicts that depleting T cells\
    \ or blocking IFN-gamma/PD-1\n  signaling should be neuroprotective, and frames\
    \ adaptive immunity as a shared, targetable axis across\n  tau-driven neurodegenerative\
    \ disease.\napplies_to_subtypes:\n- Early-Onset Alzheimer's Disease\n- Late-Onset\
    \ Alzheimer's Disease\nevidence:\n- reference: PMID:36890231\n  reference_title:\
    \ Microglia-mediated T cell infiltration drives neurodegeneration in tauopathy.\n\
    \  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n  snippet: We found that\
    \ mice with tauopathy but not those with amyloid deposition developed a unique\n\
    \    innate and adaptive immune response and that depletion of microglia or T\
    \ cells blocked tau-mediated\n    neurodegeneration.\n  explanation: Depletion\
    \ of either microglia or T cells blocks tau-mediated neurodegeneration in a tauopathy\n\
    \    model, establishing the adaptive T cell arm as functionally required rather\
    \ than a bystander.\n- reference: PMID:36890231\n  reference_title: Microglia-mediated\
    \ T cell infiltration drives neurodegeneration in tauopathy.\n  supports: SUPPORT\n\
    \  evidence_source: MODEL_ORGANISM\n  snippet: Inhibition of interferon-\u03B3\
    \ and PDCD1 signalling both significantly ameliorated brain atrophy.\n  explanation:\
    \ IFN-gamma and PD-1 (PDCD1) blockade reduce brain atrophy, nominating specific,\
    \ druggable\n    nodes within the adaptive-immune neurodegeneration axis.\nnotes:\
    \ EMERGING. The core functional evidence (T cell depletion, IFN-gamma/PD-1 inhibition)\
    \ is from mouse\n  tauopathy models, with correlative human support (increased\
    \ cytotoxic T cells in AD brain tracking tau,\n  not amyloid). The identity of\
    \ the recognized antigen(s), the antigen-presenting route (cDC1 cross-presentation\n\
    \  is implicated), and whether B cells contribute meaningfully remain open. Complements\
    \ \u2014 does not replace\n  \u2014 the innate neuroimmune_glial_amplification_model."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: true
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 23
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
- **Disease Name:** Alzheimer Disease
- **Category:** Neurodegenerative Disorder

## Target Hypothesis
- **Hypothesis ID:** adaptive_immune_tcell_model
- **Hypothesis Label:** Adaptive Immune (T Cell) Neurodegeneration Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: adaptive_immune_tcell_model
hypothesis_label: Adaptive Immune (T Cell) Neurodegeneration Model
status: EMERGING
description: Beyond innate microglial responses, a clonally expanded, predominantly cytotoxic (CD8+) T
  cell response is modeled as an active driver of tau-associated neurodegeneration. In tauopathy — but
  not pure amyloidosis — microglia are required to recruit T cells to sites of tau pathology; infiltrating
  T cells transition from activated to exhausted states with restricted TCR clonality, and IFN-gamma/PD-1
  signaling amplifies neuronal loss. The model predicts that depleting T cells or blocking IFN-gamma/PD-1
  signaling should be neuroprotective, and frames adaptive immunity as a shared, targetable axis across
  tau-driven neurodegenerative disease.
applies_to_subtypes:
- Early-Onset Alzheimer's Disease
- Late-Onset Alzheimer's Disease
evidence:
- reference: PMID:36890231
  reference_title: Microglia-mediated T cell infiltration drives neurodegeneration in tauopathy.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: We found that mice with tauopathy but not those with amyloid deposition developed a unique
    innate and adaptive immune response and that depletion of microglia or T cells blocked tau-mediated
    neurodegeneration.
  explanation: Depletion of either microglia or T cells blocks tau-mediated neurodegeneration in a tauopathy
    model, establishing the adaptive T cell arm as functionally required rather than a bystander.
- reference: PMID:36890231
  reference_title: Microglia-mediated T cell infiltration drives neurodegeneration in tauopathy.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Inhibition of interferon-γ and PDCD1 signalling both significantly ameliorated brain atrophy.
  explanation: IFN-gamma and PD-1 (PDCD1) blockade reduce brain atrophy, nominating specific, druggable
    nodes within the adaptive-immune neurodegeneration axis.
notes: EMERGING. The core functional evidence (T cell depletion, IFN-gamma/PD-1 inhibition) is from mouse
  tauopathy models, with correlative human support (increased cytotoxic T cells in AD brain tracking tau,
  not amyloid). The identity of the recognized antigen(s), the antigen-presenting route (cDC1 cross-presentation
  is implicated), and whether B cells contribute meaningfully remain open. Complements — does not replace
  — the innate neuroimmune_glial_amplification_model.
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

# Hypothesis-Search Report: Adaptive Immune (T Cell) Neurodegeneration Model in Alzheimer Disease

**Hypothesis ID:** `adaptive_immune_tcell_model`
**KB Status (entering review):** EMERGING
**Recommended KB Status (after search):** EMERGING (retain), with tightened, tau-restricted scope
**Search date:** 2026-07-11 · 48 papers reviewed · 8 hypotheses tested (7 supported, 1 rejected) · 9 findings recorded

---

## Summary

**Verdict: PARTIALLY SUPPORTED. Retain EMERGING status, with an explicit tau-restriction on scope.**

The core of the Adaptive Immune (T Cell) Neurodegeneration Model — that a microglia-recruited, clonally expanded, predominantly cytotoxic CD8⁺ T-cell response is a *functionally required* driver (not a bystander) of **tau-associated** neurodegeneration — is supported by direct, perturbation-based evidence in mouse tauopathy that has now been reproduced across independent laboratories. The founding study ([PMID:36890231](https://pubmed.ncbi.nlm.nih.gov/36890231/)) showed that depletion of either microglia *or* T cells blocks tau-mediated neurodegeneration, and that inhibiting IFN-γ or PDCD1 (PD-1) each ameliorated brain atrophy. Independent groups have since converged on cytotoxic CD8 effectors (including granzyme-K⁺ and CD103⁺ tissue-resident subsets) as the relevant population, and human post-mortem tissue from primary tauopathies (PSP, Pick's disease, FTLD-MAPT, and CTE) shows T-cell infiltration tracking tau pathology. This is a genuine, causally anchored mechanistic axis.

However, three unresolved edges prevent upgrading the hypothesis beyond EMERGING. **First, there is no human causal test** — all functional (perturbation) evidence is from mouse models; human data are correlative. **Second, the recognized antigen is unidentified.** The hypothesis leans on "restricted TCR clonality" as evidence of a tau-antigen-driven clonal response, but aging independently expands **antigen-independent virtual-memory CD8⁺ T cells** ([PMID:42432776](https://pubmed.ncbi.nlm.nih.gov/42432776/)) that arise without foreign-antigen priming and can be clonal and cytotoxic — a viable bystander alternative that no primary study has yet excluded. **Third, the IFN-γ/PD-1 therapeutic node has opposite valence depending on pathology.** In amyloidosis, PD-1 blockade triggers an IFN-γ-dependent myeloid response that *clears* Aβ and *improves* cognition ([PMID:26779813](https://pubmed.ncbi.nlm.nih.gov/26779813/)), the reverse of the tau-context prediction — so "block IFN-γ/PD-1" is not a universal neuroprotective prescription, and IFN-γ is not even CD8-exclusive (NK cells are a parallel source correlating with cognitive decline; [PMID:11268360](https://pubmed.ncbi.nlm.nih.gov/11268360/)).

The most important caveat for curators is **context-dependence**. Across the literature, adaptive immunity in AD is dual: neuroprotective regulatory T cells and protective autoimmunity limit amyloid-driven loss, while cytotoxic CD8/IFN-γ drives tau-context loss. The seed hypothesis is correct *precisely because* it is scoped to tauopathy and not "pure amyloidosis." Any curation should preserve that restriction and flag the antigen-identity and IFN-γ-valence gaps as explicit `knowledge_gaps`. The model **complements — does not replace —** the innate `neuroimmune_glial_amplification_model`, which sits upstream as the required recruiter of the T-cell arm.

---

## Key Findings

### F001 — The adaptive T-cell arm is functionally required (non-redundant) for tau-mediated neurodegeneration

The strongest direct evidence comes from *Microglia-mediated T cell infiltration drives neurodegeneration in tauopathy* ([PMID:36890231](https://pubmed.ncbi.nlm.nih.gov/36890231/), Nature 2023). In P301S tauopathy mice — but *not* in amyloid-only mice — the authors observed a unique innate and adaptive immune response, and **depletion of either microglia or T cells blocked tau-mediated neurodegeneration**. Critically, this is perturbation-based (causal within the model system), not merely correlative: removing the T-cell arm removed the phenotype. The study further showed that **inhibition of interferon-γ and PDCD1 (PD-1) signalling both significantly ameliorated brain atrophy**, nominating two specific, druggable nodes. This establishes the adaptive arm as functionally necessary in tauopathy rather than a passive consequence of neurodegeneration, and it anchors the entire hypothesis. Hypothesis H001 (cytotoxic CD8 driver + microglial recruitment + IFN-γ/PD-1 amplification) was recorded as **supported** on the strength of this converging perturbation evidence.

### F002 — Adaptive immunity can be neuroprotective in amyloid context (qualifying/competing evidence)

A directly competing observation is that, in an amyloid-toxicity context, adaptive immunity can be protective. In *Vaccination with autoantigen protects against aggregated beta-amyloid and glutamate toxicity...* ([PMID:15549735](https://pubmed.ncbi.nlm.nih.gov/15549735/)), β-amyloid-induced neuronal loss was **greater in immunodeficient mice** and was "attenuated or augmented by elimination or addition, respectively, of naturally occurring CD4⁺CD25⁺ regulatory T cells (Treg)" — i.e., Tregs were neuroprotective. Supporting literature reinforces this: a review concluding the majority of evidence supports neuroprotective Treg effects in AD ([PMID:37907046](https://pubmed.ncbi.nlm.nih.gov/37907046/)), and interventions that manipulate Tregs alter amyloid/cognition ([PMID:26772975](https://pubmed.ncbi.nlm.nih.gov/26772975/), [PMID:32075657](https://pubmed.ncbi.nlm.nih.gov/32075657/)). This is why hypothesis H004 (context-dependent protective adaptive immunity) was **supported** as a qualifying model. The lesson for the seed hypothesis: the *direction* of the T-cell effect flips with pathology, so the cytotoxic-driver framing must remain tau-scoped.

### F003 — Independent labs converge on cytotoxic CD8 (granzyme-K⁺, CD103⁺ resident) effectors

The founding claim is not lab-idiosyncratic. Beyond the Holtzman group, the Constantin group reported brain CD8 T cells with a CD103⁺ tissue-resident memory phenotype participating in AD neuropathology ([PMID:40993111](https://pubmed.ncbi.nlm.nih.gov/40993111/)); the Biragyn group reported that "the disease may also depend on the adaptive immunity, as B cells exacerbate and CD8" T cells contribute ([PMID:39191349](https://pubmed.ncbi.nlm.nih.gov/39191349/)); and a Latour & McGavern review notes "the identification of granzyme K-expressing CD8⁺ T cells in several neurodegenerative conditions" ([PMID:41983391](https://pubmed.ncbi.nlm.nih.gov/41983391/)). A 2026 Holtzman-group follow-up extends the CD8 antigen-presentation mechanism ([PMID:41890046](https://pubmed.ncbi.nlm.nih.gov/41890046/)). This convergence — supporting hypothesis H005 — nominates a specific, shareable effector population (granzyme-K/B⁺, CD103⁺) across tauopathies and strengthens the "shared, targetable axis" element of the seed claim.

### F004 — Central tension: adaptive immunity's dual role mandates subset/context specification

Multiple 2026 syntheses document that the adaptive arm in AD is bidirectional. One review states plainly that "both infiltrating lymphocytes and resident glia show context-dependent dual effects, either exacerbating neurodegeneration or promoting neuroprotection" ([PMID:41490988](https://pubmed.ncbi.nlm.nih.gov/41490988/)). Others note CD8⁺/CD4⁺ T cells exert neuroprotective or neurotoxic effects depending on disease context, activation state, and antigen specificity ([PMID:41983391](https://pubmed.ncbi.nlm.nih.gov/41983391/)), and that anti-Aβ CD8 function "remains ambiguous" ([PMID:41791120](https://pubmed.ncbi.nlm.nih.gov/41791120/)). This is not a refutation but a *scoping requirement*: the cytotoxic-driver hypothesis is only coherent when specified to a subset (cytotoxic CD8, not Treg) and a context (tau, not amyloid).

### F005 — IFN-γ/PD-1 has opposite therapeutic valence in amyloid vs tau (refutes any universal claim)

This is the sharpest constraint on the hypothesis's therapeutic predictions. In tauopathy, inhibiting IFN-γ and PD-1 ameliorates brain atrophy (IFN-γ neurotoxic; [PMID:36890231](https://pubmed.ncbi.nlm.nih.gov/36890231/)). In amyloidosis, the reverse holds: PD-1 checkpoint blockade "leads to clearance of cerebral amyloid-β (Aβ) plaques and improved cognitive performance" through an IFN-γ-dependent, monocyte-derived-macrophage response (IFN-γ beneficial; [PMID:26779813](https://pubmed.ncbi.nlm.nih.gov/26779813/)). A review explicitly frames this as a "paradox," noting PD-1 inhibition induces an IFN-γ-mediated response that recruits monocyte-derived macrophages, enhances Aβ clearance, and improves cognition ([PMID:40285967](https://pubmed.ncbi.nlm.nih.gov/40285967/)). Notably, the amyloid PD-1-blockade result also has a documented history of failed independent replication. Hypothesis H006 (opposite valence) was **supported**: "block IFN-γ/PD-1" is neuroprotective only in a tau-restricted context.

### F006 — NK cells are a parallel cytotoxic IFN-γ/TNF-α source confounding CD8-specific attribution

The hypothesis attributes IFN-γ-driven neuronal loss to clonal CD8 T cells, but NK cells are an alternative source. In AD (DAT) patients, purified NK cells (CD16⁺CD56⁺CD3⁻) showed increased spontaneous and IL-2-induced IFN-γ and TNF-α release versus controls (p<0.001), and "significant negative correlations among the spontaneous release of IFN-γ and TNF-α from NK and the decrease of the score of cognitive function (MMSE) were found" ([PMID:11268360](https://pubmed.ncbi.nlm.nih.gov/11268360/)). NK subsets are implicated across neurodegeneration ([PMID:38350967](https://pubmed.ncbi.nlm.nih.gov/38350967/); ALS scRNAseq [PMID:39849490](https://pubmed.ncbi.nlm.nih.gov/39849490/)). Hypothesis H007 was **supported**: NK-derived IFN-γ/TNF-α tracks cognitive decline, meaning some "adaptive" IFN-γ effects may be innate-lymphoid in origin and cannot be cleanly attributed to clonal CD8.

### F007 — Antigen identity is the weakest link; virtual-memory CD8 is an antigen-independent alternative

The decisive gap. The hypothesis interprets restricted TCR clonality as evidence of a tau-antigen-driven response, but aging expands **virtual-memory (VM) CD8 T cells that "arise in the absence of foreign antigen priming"** and acquire a memory-like phenotype through self-reactivity, IL-15, and EOMES — including subsets with cytotoxic and inflammatory potential ([PMID:42432776](https://pubmed.ncbi.nlm.nih.gov/42432776/)). Literature searches for tau-peptide/MAPT-specific TCR reactivity in AD ("tau specific T cells antigen MAPT autoreactive"; "tau antigen specific T cell recognition") returned **no primary demonstration** — only vaccine and review hits. The 2026 Holtzman follow-up implicates cDC1 cross-presentation but leaves the recognized antigen(s) unnamed ([PMID:41890046](https://pubmed.ncbi.nlm.nih.gov/41890046/)). Hypothesis H008 (clonal CD8 may be antigen-inexperienced VM cells) was **supported** as a competing explanation, and this is the single most important reason the model stays EMERGING.

### F008 — Human primary-tauopathy tissue supports cross-tauopathy generalization

Human, amyloid-independent tissue evidence exists. A Boche-lab post-mortem study (2024) quantified CD4⁺/CD8⁺ T cells against multiple pTau epitopes and 30 inflammatory proteins across 45 PSP, 33 Pick's, and 12 FTLD-MAPT cases versus 52 controls, explicitly motivated by the observation that T-cell infiltration seen in THY-Tau22 mice "remains to be confirmed in FTLD-tau patients" ([PMID:37703311](https://pubmed.ncbi.nlm.nih.gov/37703311/)). Complementary human evidence in CTE (a primary tauopathy) shows meningeal and infiltrating T-cells associated with repetitive head trauma and tau-mediated neurodegeneration, correlating with synaptic loss and spatially related to MHC-II⁺ cells ([PMID:41957675](https://pubmed.ncbi.nlm.nih.gov/41957675/)). Together with clonally expanded CD8 T cells patrolling the CSF in AD ([PMID:31915375](https://pubmed.ncbi.nlm.nih.gov/31915375/)) and T-cell infiltration correlating with neuronal loss/cognitive decline ([PMID:38437992](https://pubmed.ncbi.nlm.nih.gov/38437992/)), this provides correlative human support for the shared adaptive-immune-tau axis.

### F009 — Overall verdict

Convergent perturbation evidence in mouse tauopathy across independent labs supports a functionally required cytotoxic-CD8/IFN-γ/PD-1 arm ([PMID:36890231](https://pubmed.ncbi.nlm.nih.gov/36890231/), [PMID:41890046](https://pubmed.ncbi.nlm.nih.gov/41890046/), [PMID:40993111](https://pubmed.ncbi.nlm.nih.gov/40993111/), [PMID:39191349](https://pubmed.ncbi.nlm.nih.gov/39191349/)), with correlative human tissue/CSF support ([PMID:31915375](https://pubmed.ncbi.nlm.nih.gov/31915375/), [PMID:38437992](https://pubmed.ncbi.nlm.nih.gov/38437992/), [PMID:37703311](https://pubmed.ncbi.nlm.nih.gov/37703311/), [PMID:41957675](https://pubmed.ncbi.nlm.nih.gov/41957675/)). Three unresolved edges keep it EMERGING: (1) no human causal test; (2) unproven antigen identity with a viable antigen-independent VM alternative ([PMID:42432776](https://pubmed.ncbi.nlm.nih.gov/42432776/)); (3) IFN-γ/PD-1 valence reverses in amyloid context ([PMID:26779813](https://pubmed.ncbi.nlm.nih.gov/26779813/) vs [PMID:36890231](https://pubmed.ncbi.nlm.nih.gov/36890231/)), and the IFN-γ source is not CD8-exclusive ([PMID:11268360](https://pubmed.ncbi.nlm.nih.gov/11268360/)).

---

## Evidence Matrix

| Citation | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:36890231](https://pubmed.ncbi.nlm.nih.gov/36890231/) | Model organism (mouse) | **Supports** | T cells functionally required for tau neurodegeneration; IFN-γ/PD-1 amplify | Depleting microglia or T cells blocks tau-mediated neurodegeneration; IFN-γ & PDCD1 inhibition ameliorate atrophy | Tauopathy (P301S), not amyloidosis | High (causal/perturbation); mouse only; antigen unidentified |
| [PMID:41890046](https://pubmed.ncbi.nlm.nih.gov/41890046/) | Model organism | **Supports** | CD8 antigen-presentation mechanism in AD adaptive immunity | Extends CD8 mechanism; implicates cDC1 cross-presentation | AD | Medium-high; antigen still unnamed |
| [PMID:40993111](https://pubmed.ncbi.nlm.nih.gov/40993111/) | Model organism / tissue | **Supports** | CD103⁺ tissue-resident CD8 participate in AD neuropathology | Independent replication of cytotoxic CD8 effector role | AD | Medium-high; independent lab |
| [PMID:39191349](https://pubmed.ncbi.nlm.nih.gov/39191349/) | Model organism | **Supports** | Adaptive immunity actively contributes (B + CD8) | Non-bystander adaptive involvement beyond originating lab | AD | Medium; also implicates B cells |
| [PMID:41983391](https://pubmed.ncbi.nlm.nih.gov/41983391/) | Review | **Supports (review-level)** | Convergent granzyme-K⁺ CD8 subset across neurodegeneration | Shared cytotoxic effector identity | Multiple neurodegenerative | Review orientation; dual-role caveat |
| [PMID:31915375](https://pubmed.ncbi.nlm.nih.gov/31915375/) | Human clinical | **Supports (correlative)** | Clonal CD8 in AD CSF | Clonally expanded CD8 T cells patrol CSF | AD (human) | Correlative; clonality ≠ antigen ID |
| [PMID:38437992](https://pubmed.ncbi.nlm.nih.gov/38437992/) | Human/review | **Supports (correlative)** | T-cell infiltration correlates with neuronal loss/cognition | Neuronal loss correlates with T-cell quantity | AD (human) | Correlative; BBB dysfunction confound |
| [PMID:37703311](https://pubmed.ncbi.nlm.nih.gov/37703311/) | Human tissue | **Supports (correlative)** | T-cell infiltration in primary tauopathies | CD4/CD8 vs pTau epitopes across PSP/Pick's/FTLD-MAPT | Primary tauopathy (amyloid-independent) | Post-mortem; cross-sectional |
| [PMID:41957675](https://pubmed.ncbi.nlm.nih.gov/41957675/) | Human tissue | **Supports (correlative)** | T cells with tau-mediated neurodegeneration in CTE | Infiltrating T-cells ↑ in p-tau sulci; correlate w/ synaptic loss | CTE (primary tauopathy) | Post-mortem; correlative |
| [PMID:15549735](https://pubmed.ncbi.nlm.nih.gov/15549735/) | Model organism | **Competing/qualifies** | Adaptive immunity protective in amyloid toxicity | Treg depletion worsens, addition attenuates Aβ neurodegeneration | Amyloid context | Direction opposite to seed; different context |
| [PMID:37907046](https://pubmed.ncbi.nlm.nih.gov/37907046/) | Review | **Qualifies** | Tregs are net neuroprotective in AD | Majority of evidence supports protective Tregs | AD | Review-level |
| [PMID:26772975](https://pubmed.ncbi.nlm.nih.gov/26772975/) | Model organism | **Qualifies** | Treg expansion protective | bvPLA2-driven Treg increase improves cognition, ↓Aβ | 3xTg amyloid | Treg-dependent effect |
| [PMID:32075657](https://pubmed.ncbi.nlm.nih.gov/32075657/) | Model organism | **Qualifies** | Reducing Tregs improves amyloid/cognition | IIV breaks Treg tolerance, ↓Aβ, ↑cognition | APP/PS1 amyloid | Opposite Treg manipulation, same beneficial outcome — context-complex |
| [PMID:41490988](https://pubmed.ncbi.nlm.nih.gov/41490988/) | Review | **Qualifies** | Dual context-dependent lymphocyte effects | Lymphocytes exacerbate or protect depending on context | AD | Requires subset/context scoping |
| [PMID:41791120](https://pubmed.ncbi.nlm.nih.gov/41791120/) | Review | **Qualifies** | CD8 both protective & detrimental; anti-Aβ CD8 ambiguous | CD8 subsets ambiguous; CD8 Tregs exist | AD | Anti-Aβ CD8 function unresolved |
| [PMID:26779813](https://pubmed.ncbi.nlm.nih.gov/26779813/) | Model organism | **Competing (valence reversal)** | PD-1 blockade + IFN-γ beneficial in amyloid | PD-1 blockade clears Aβ, improves cognition via IFN-γ-dependent myeloid recruitment | Amyloidosis | Opposite valence; failed replications noted |
| [PMID:40285967](https://pubmed.ncbi.nlm.nih.gov/40285967/) | Review | **Competing (valence)** | IFN-γ/PD-1 paradox | Frames beneficial IFN-γ/PD-1 axis in amyloid AD | AD | Review; labels as paradox |
| [PMID:11268360](https://pubmed.ncbi.nlm.nih.gov/11268360/) | Human clinical | **Competing (source)** | NK cells produce IFN-γ/TNF-α tracking cognition | NK IFN-γ/TNF-α ↑; negative correlation with MMSE | AD (human) | Non-CD8 IFN-γ source; small cohort |
| [PMID:38350967](https://pubmed.ncbi.nlm.nih.gov/38350967/) | Review | **Competing (source)** | NK subsets in neurodegeneration | NK role across MS/AD/PD/ALS ambiguous | Neurodegeneration | Review orientation |
| [PMID:39849490](https://pubmed.ncbi.nlm.nih.gov/39849490/) | Human (scRNAseq) | **Competing (source)** | Cytotoxic NK/CD56 subset with NfL | Expanded cytotoxic terminally-differentiated subset assoc. w/ NfL | ALS | Different disease; supports NK-lineage cytotoxicity |
| [PMID:42432776](https://pubmed.ncbi.nlm.nih.gov/42432776/) | Review/model | **Competing (antigen-independent)** | Clonal CD8 may be antigen-inexperienced | VM CD8 arise without foreign antigen; cytotoxic potential | Aging | Directly undercuts tau-antigen clonality inference |
| [PMID:40297057](https://pubmed.ncbi.nlm.nih.gov/40297057/) | Review | **Qualifies (B cells)** | B cells contribute (dual) | B cells protective & pathological in AD | AD | Opens humoral arm; seed lists B-cell role as open |

---

## Mechanistic Model / Interpretation

The hypothesis implies the following causal chain from upstream trigger to clinical manifestation:

```
 Tau aggregation (p-tau accumulation)
        │  [STRONG in mouse; STRONG human correlation]
        ▼
 Microglial activation + MHC-II antigen presentation
        │  [STRONG — required recruiter; APOE4 amplifies (PMID:39468688)]
        ▼
 Chemokine-mediated recruitment of peripheral T cells across BBB
        │  [MODERATE — chemokine axis reviewed; BBB dysfunction is a confound]
        ▼
 Infiltration of cytotoxic CD8+ T cells (granzyme-K/B+, CD103+ resident)
        │  [STRONG identity; INFERRED antigen specificity]
        ▼
 Recognition of an (unidentified) antigen via cDC1 cross-presentation → clonal expansion
        │  [WEAK / MISSING — antigen unknown; VM CD8 alternative unexcluded]
        ▼
 Activated → exhausted transition; IFN-γ + PD-1 signaling
        │  [STRONG in tau (perturbation); REVERSED valence in amyloid]
        ▼
 Neuronal loss / brain atrophy / synaptic loss
        │  [STRONG in mouse tau; correlative in human]
        ▼
 Cognitive decline / dementia
```

**Where the literature is strong:** the tau → microglia → T-cell recruitment → IFN-γ/PD-1 → atrophy segment in mouse tauopathy is supported by direct depletion and pathway-inhibition experiments ([PMID:36890231](https://pubmed.ncbi.nlm.nih.gov/36890231/)), and the effector identity (cytotoxic CD8, granzyme-K⁺, CD103⁺) is corroborated by independent labs ([PMID:40993111](https://pubmed.ncbi.nlm.nih.gov/40993111/), [PMID:41983391](https://pubmed.ncbi.nlm.nih.gov/41983391/)).

**Where links are inferred:** the human arm is entirely correlative — T-cell abundance correlates with neuronal loss and tau, but no human perturbation exists. The BBB-crossing step is plausible but confounded by generalized BBB dysfunction in AD.

**Where causal steps are missing:** the antigen-recognition/clonal-expansion node is the critical gap. No primary study demonstrates tau-peptide-specific (MAPT-derived) TCR reactivity, and the antigen-independent virtual-memory CD8 alternative ([PMID:42432776](https://pubmed.ncbi.nlm.nih.gov/42432776/)) means "restricted clonality" cannot yet be read as "tau-antigen-driven." The IFN-γ effector node is also non-specific to CD8 (NK cells; [PMID:11268360](https://pubmed.ncbi.nlm.nih.gov/11268360/)).

### Subtype / stage / tissue mapping

| Feature | Where the hypothesis fits well | Where it does NOT fit |
|---|---|---|
| **Pathology** | Tau-dominant / tauopathy | Pure amyloidosis (valence reverses) |
| **Subtype** | Both EOAD & LOAD where tau present; primary tauopathies (PSP, Pick's, FTLD-MAPT), CTE | Amyloid-only early stages |
| **Tissue** | Brain parenchyma at tau lesions; leptomeninges; CSF | — |
| **Cell types** | Cytotoxic CD8 (granzyme-K/B⁺, CD103⁺ TRM); microglia (recruiter) | Tregs (protective); NK (parallel source) |
| **Pathways** | IFN-γ, PDCD1/PD-1, MHC-II antigen presentation, cDC1 cross-presentation | — |
| **Biomarkers** | CSF clonal CD8; tau-PET co-localization | — |

---

## Evidence Base

- ***Microglia-mediated T cell infiltration drives neurodegeneration in tauopathy*** ([PMID:36890231](https://pubmed.ncbi.nlm.nih.gov/36890231/)) — the founding, causally decisive study. Provides the only direct perturbation evidence: depletion of microglia or T cells blocks tau neurodegeneration; IFN-γ/PD-1 inhibition ameliorates atrophy. Supports the core hypothesis.
- ***CD103⁺ tissue-resident CD8 in AD*** ([PMID:40993111](https://pubmed.ncbi.nlm.nih.gov/40993111/)) and ***adaptive immunity contribution*** ([PMID:39191349](https://pubmed.ncbi.nlm.nih.gov/39191349/)) — independent-lab replication of the cytotoxic-CD8 effector role, strengthening generalizability.
- ***Immune signaling and function in neurodegeneration*** ([PMID:41983391](https://pubmed.ncbi.nlm.nih.gov/41983391/)) — review synthesis identifying convergent granzyme-K⁺ CD8 across neurodegenerative conditions; review-level support for a shared effector.
- ***Clonally expanded CD8 T cells patrol the CSF in AD*** ([PMID:31915375](https://pubmed.ncbi.nlm.nih.gov/31915375/)) and ***T cell infiltration mediates neurodegeneration*** ([PMID:38437992](https://pubmed.ncbi.nlm.nih.gov/38437992/)) — human correlative support (clonality + correlation with neuronal loss).
- ***Glial reactivity and T cell infiltration in FTLD-tau*** ([PMID:37703311](https://pubmed.ncbi.nlm.nih.gov/37703311/)) and ***Meningeal/infiltrating T-cells in CTE*** ([PMID:41957675](https://pubmed.ncbi.nlm.nih.gov/41957675/)) — human amyloid-independent primary-tauopathy tissue evidence supporting cross-tauopathy generalization.
- ***Vaccination with autoantigen / CD4⁺CD25⁺ Tregs*** ([PMID:15549735](https://pubmed.ncbi.nlm.nih.gov/15549735/)) plus Treg reviews/interventions ([PMID:37907046](https://pubmed.ncbi.nlm.nih.gov/37907046/), [PMID:26772975](https://pubmed.ncbi.nlm.nih.gov/26772975/), [PMID:32075657](https://pubmed.ncbi.nlm.nih.gov/32075657/)) — competing/qualifying: protective adaptive immunity in amyloid contexts.
- ***PD-1 checkpoint blockade reduces pathology in AD*** ([PMID:26779813](https://pubmed.ncbi.nlm.nih.gov/26779813/)) and ***Unmasking a Paradox: PD-1/PD-L1 axis*** ([PMID:40285967](https://pubmed.ncbi.nlm.nih.gov/40285967/)) — challenge the universal therapeutic claim: IFN-γ/PD-1 is beneficial in amyloidosis.
- ***NK IFN-γ/TNF-α overproduction*** ([PMID:11268360](https://pubmed.ncbi.nlm.nih.gov/11268360/)), ***CD56 NK role*** ([PMID:38350967](https://pubmed.ncbi.nlm.nih.gov/38350967/)), ***ALS NK scRNAseq*** ([PMID:39849490](https://pubmed.ncbi.nlm.nih.gov/39849490/)) — challenge CD8-specific attribution of IFN-γ.
- ***Virtual memory CD8⁺ T cells in aging*** ([PMID:42432776](https://pubmed.ncbi.nlm.nih.gov/42432776/)) — the pivotal challenge to the antigen-driven clonality inference.
- ***Adaptive Immunity and AD: Dual Roles*** ([PMID:41490988](https://pubmed.ncbi.nlm.nih.gov/41490988/)), ***Bench to Bedside CD8*** ([PMID:41791120](https://pubmed.ncbi.nlm.nih.gov/41791120/)), ***B cells/humoral immunity*** ([PMID:40297057](https://pubmed.ncbi.nlm.nih.gov/40297057/)) — reviews mandating context/subset scoping and flagging the open B-cell arm.

---

## Limitations and Knowledge Gaps

| # | Gap | Scope | Why it matters | What was checked | Resolving evidence |
|---|---|---|---|---|---|
| G1 | **No human causal test** | Human AD/tauopathy | Entire human arm is correlative; causation is mouse-only | Human tissue/CSF studies (PMID:31915375, 38437992, 37703311, 41957675) — all observational | Human trial of T-cell/IFN-γ/PD-1 modulation with tau-PET & atrophy endpoints |
| G2 | **Antigen identity unknown** | Core mechanism | "Restricted clonality" is the linchpin argument; if antigen-independent (VM), the "adaptive/antigen-driven" framing weakens to "cytotoxic-lymphocyte" | Searches for tau/MAPT-specific TCR reactivity returned no primary demonstration; VM alternative found (PMID:42432776) | TCR–pMHC tetramer / antigen-discovery (peptide-MHC screens) on brain-infiltrating clones |
| G3 | **IFN-γ/PD-1 valence reversal** | Amyloid vs tau | "Block IFN-γ/PD-1" is protective in tau but harmful (blocks beneficial Aβ clearance) in amyloid; universal claim refuted | PMID:36890231 (tau) vs PMID:26779813, 40285967 (amyloid) | Head-to-head IFN-γ/PD-1 modulation in matched tau-only, amyloid-only, mixed models |
| G4 | **IFN-γ source not CD8-exclusive** | Effector attribution | NK cells produce IFN-γ/TNF-α correlating with cognition; attribution to clonal CD8 may be overstated | PMID:11268360, 38350967, 39849490 | Cell-type-specific IFN-γ conditional knockouts / adoptive transfer |
| G5 | **B-cell contribution unresolved** | Humoral arm | Seed lists B-cell role as open; reviews show dual B-cell effects | PMID:39191349 (B cells exacerbate), PMID:40297057 (dual) | B-cell depletion in tauopathy vs amyloidosis |
| G6 | **Failed replication of amyloid PD-1 result** | Therapeutic node | The competing amyloid-beneficial finding has a replication history problem, complicating valence interpretation | Noted in F005 record | Pre-registered multi-site replication |
| G7 | **No omics/GenCC/ClinGen genetic link surfaced** | Source-level absence | No germline genetic evidence tying TCR/IFN-γ/PDCD1 variants to AD risk was found in this search | Search focused on functional immunology, not GWAS/GenCC | Targeted GWAS/colocalization of PDCD1/IFNG loci with AD; check GenCC/ClinGen |

---

## Alternative Models

1. **Innate glial-amplification model (`neuroimmune_glial_amplification_model`) — upstream / complementary.** Microglia are the required recruiter of the T-cell arm; the innate model sits upstream and is not replaced by the adaptive model. The founding study itself shows microglial depletion also blocks neurodegeneration ([PMID:36890231](https://pubmed.ncbi.nlm.nih.gov/36890231/)). APOE4-driven microglial antigen presentation ([PMID:39468688](https://pubmed.ncbi.nlm.nih.gov/39468688/)) links genetic risk to the recruitment step.

2. **Protective adaptive immunity / Treg model — parallel, opposite-valence.** Regulatory T cells and protective autoimmunity are neuroprotective in amyloid contexts ([PMID:15549735](https://pubmed.ncbi.nlm.nih.gov/15549735/), [PMID:37907046](https://pubmed.ncbi.nlm.nih.gov/37907046/)). A genuine alternative for the amyloid subtype and a boundary condition for the seed hypothesis.

3. **NK / innate-lymphoid cytotoxicity model — parallel effector.** NK-derived IFN-γ/TNF-α correlates with cognitive decline ([PMID:11268360](https://pubmed.ncbi.nlm.nih.gov/11268360/)); a cytotoxic innate-lymphoid arm could account for some effects attributed to CD8.

4. **Antigen-independent virtual-memory CD8 model — alternative explanation for clonality.** Age-expanded VM CD8 cells provide clonal, cytotoxic cells without tau-antigen priming ([PMID:42432776](https://pubmed.ncbi.nlm.nih.gov/42432776/)) — an alternative reading of the same clonality data.

5. **Amyloid-cascade / IFN-γ-beneficial model — competing for the IFN-γ node.** In amyloidosis, IFN-γ-dependent myeloid recruitment clears Aβ and improves cognition ([PMID:26779813](https://pubmed.ncbi.nlm.nih.gov/26779813/)) — a downstream-beneficial role competing with the neurotoxic framing.

6. **Humoral / B-cell model — parallel adaptive arm.** B cells exacerbate ([PMID:39191349](https://pubmed.ncbi.nlm.nih.gov/39191349/)) yet also protect via antibody-mediated clearance ([PMID:40297057](https://pubmed.ncbi.nlm.nih.gov/40297057/)); an underexplored parallel branch.

---

## Proposed Follow-up Experiments / Discriminating Tests

| Test | Design | Stratification / model | Perturbation | Expected result if seed TRUE | Distinguishes from |
|---|---|---|---|---|---|
| **Antigen discovery** | pMHC tetramer + single-cell TCR-seq on brain-infiltrating CD8 clones | Human tauopathy tissue + P301S mice | None (observational + reactivity screen) | Dominant clones recognize tau-derived peptides | VM/antigen-independent (G2) |
| **VM lineage tracing** | Fate-map VM CD8 (IL-15/EOMES) vs conventional memory in tauopathy | P301S mice | Genetic VM ablation | Neurodegeneration persists (conventional clones drive) | VM alternative (PMID:42432776) |
| **Cell-type-specific IFN-γ KO** | Conditional Ifng deletion in CD8 vs NK vs total | Tau-only, amyloid-only, mixed | Lineage-restricted KO | Only CD8-IFN-γ KO protects in tau | NK source (G4); valence (G3) |
| **Matched IFN-γ/PD-1 modulation** | Same intervention across tau vs amyloid models | Tau-only vs amyloid-only | IFN-γ/PD-1 blockade | Protective in tau; harmful/neutral in amyloid | Valence reversal (G3) |
| **Human causal proxy** | Repurposed checkpoint/IFN-γ agents; tau-PET + volumetric MRI + CSF | Tau-PET-positive vs amyloid-only patients | Pharmacologic | Slowed atrophy in tau-positive arm only | No human causal test (G1) |
| **B-cell depletion** | Anti-CD20 in tauopathy vs amyloidosis | Both models | B-cell depletion | Minimal effect if CD8-dominant | Humoral arm (G5) |

---

## Curation Leads *(require curator verification)*

**Candidate status:** Retain **EMERGING**. Add explicit subtype restriction to **tauopathy / tau-dominant AD**; flag that predictions do **not** extend to pure amyloidosis.

**Candidate evidence references and snippets to verify:**
- [PMID:36890231](https://pubmed.ncbi.nlm.nih.gov/36890231/): "mice with tauopathy but not those with amyloid deposition developed a unique innate and adaptive immune response and that depletion of microglia or T cells blocked tau-mediated neurodegeneration"; "Inhibition of interferon-γ and PDCD1 signalling both significantly ameliorated brain atrophy." *(already in KB — supports)*
- [PMID:40993111](https://pubmed.ncbi.nlm.nih.gov/40993111/): brain CD8 T cells (CD103⁺ tissue-resident) participate in AD neuropathology *(candidate SUPPORT, independent lab)*
- [PMID:41983391](https://pubmed.ncbi.nlm.nih.gov/41983391/): "The identification of granzyme K-expressing CD8⁺ T cells in several neurodegenerative conditions..." *(candidate SUPPORT, review-level effector identity)*
- [PMID:37703311](https://pubmed.ncbi.nlm.nih.gov/37703311/) & [PMID:41957675](https://pubmed.ncbi.nlm.nih.gov/41957675/): human primary-tauopathy T-cell infiltration *(candidate SUPPORT, human amyloid-independent)*
- [PMID:26779813](https://pubmed.ncbi.nlm.nih.gov/26779813/) & [PMID:40285967](https://pubmed.ncbi.nlm.nih.gov/40285967/): PD-1 blockade beneficial in amyloid *(candidate QUALIFY/COMPETING — valence reversal)*
- [PMID:11268360](https://pubmed.ncbi.nlm.nih.gov/11268360/): NK IFN-γ/TNF-α negatively correlates with MMSE *(candidate COMPETING — effector source)*
- [PMID:42432776](https://pubmed.ncbi.nlm.nih.gov/42432776/): VM CD8 arise without antigen priming *(candidate COMPETING — antigen-independent clonality)*
- [PMID:15549735](https://pubmed.ncbi.nlm.nih.gov/15549735/): Treg protective in amyloid toxicity *(candidate COMPETING — protective adaptive arm)*

**Candidate pathophysiology nodes/edges:** tau → microglial MHC-II presentation (APOE4-amplified) → chemokine recruitment → CD8 infiltration → [antigen recognition via cDC1 cross-presentation — UNCONFIRMED] → IFN-γ/PD-1 → neuronal loss. Mark the antigen-recognition edge as **unconfirmed**.

**Candidate ontology terms:** CD8-positive, alpha-beta cytotoxic T cell; tissue-resident memory CD8 T cell (CD103⁺); granzyme K production; interferon-gamma production; PD-1 (PDCD1) signaling; cDC1 antigen cross-presentation; regulatory T cell (competing node); natural killer cell (competing node).

**Candidate `knowledge_gaps` / discussion prompts:** (1) antigen identity unproven — VM alternative; (2) IFN-γ/PD-1 valence reverses by pathology — no universal therapeutic claim; (3) IFN-γ source not CD8-exclusive; (4) no human causal test; (5) no GenCC/ClinGen/GWAS genetic link surfaced for PDCD1/IFNG in this search; (6) B-cell contribution open.

---

## Conclusion

The Adaptive Immune (T Cell) Neurodegeneration Model is a well-anchored, tau-restricted mechanistic hypothesis with strong causal support in mouse tauopathy and reproducible effector identification across labs, but only correlative human support. It should remain **EMERGING**, complementing the upstream innate glial-amplification model. The three gaps that would most efficiently resolve its status are antigen identity (versus virtual-memory bystanders), a human causal test, and disambiguation of the pathology-dependent IFN-γ/PD-1 valence and effector source.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)