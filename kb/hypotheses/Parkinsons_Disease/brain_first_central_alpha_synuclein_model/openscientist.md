---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-06T05:29:38.971304'
end_time: '2026-07-06T06:14:58.676310'
duration_seconds: 2719.71
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Parkinson's Disease
  category: Complex
  hypothesis_group_id: brain_first_central_alpha_synuclein_model
  hypothesis_label: "Brain-First Central \u03B1-Synuclein Initiation Model"
  hypothesis_status: ALTERNATIVE
  hypothesis_yaml: "hypothesis_group_id: brain_first_central_alpha_synuclein_model\n\
    hypothesis_label: Brain-First Central \u03B1-Synuclein Initiation Model\nstatus:\
    \ ALTERNATIVE\ndescription: Alpha-synuclein pathology initiates within central\
    \ nervous system sites such as the olfactory\n  bulb or amygdala and spreads centrifugally\
    \ to brainstem and peripheral autonomic structures. This model\n  best explains\
    \ Parkinson disease presentations where central dopaminergic or olfactory involvement\
    \ precedes\n  prominent autonomic and enteric manifestations.\nnotes: The model\
    \ is supported mainly by subtype-level human imaging, clinical, and neuropathological\
    \ patterns.\n  It competes with, rather than refutes, the body-first model because\
    \ both origin routes may exist within\n  clinically diagnosed Parkinson disease.\n\
    evidence:\n- reference: PMID:38519273\n  reference_title: 'Brain-first vs. body-first\
    \ Parkinson''s disease: An update on recent evidence.'\n  supports: SUPPORT\n\
    \  evidence_source: HUMAN_CLINICAL\n  snippet: the initial pathology starts either\
    \ in the olfactory bulb or amygdala leading to a brain-first\n    subtype, or\
    \ in the enteric nervous system leading to a body-first subtype.\n  explanation:\
    \ The ASOC model explicitly defines an olfactory bulb/amygdala origin as the brain-first\n\
    \    subtype that competes with the enteric body-first route.\n- reference: PMID:38519273\n\
    \  reference_title: 'Brain-first vs. body-first Parkinson''s disease: An update\
    \ on recent evidence.'\n  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n\
    \  snippet: These subtypes should be distinguishable early in the disease course\
    \ on a range of imaging,\n    clinical, and neuropathological markers.\n  explanation:\
    \ Human subtype distinguishability supports representing brain-first and body-first\
    \ disease\n    routes as alternative mechanistic hypothesis groups.\n- reference:\
    \ PMID:32830221\n  reference_title: 'Brain-first versus body-first Parkinson''s\
    \ disease: a multimodal imaging case-control\n    study.'\n  supports: SUPPORT\n\
    \  evidence_source: HUMAN_CLINICAL\n  snippet: the PDRBD- data were compatible\
    \ with a brain-first trajectory, characterized by primary loss\n    of putaminal\
    \ FDOPA uptake followed by a secondary loss of cardiac MIBG signal and 11C-donepezil\
    \ signal.\n  explanation: Primary multimodal imaging data support a brain-first\
    \ trajectory in RBD-negative de novo\n    PD, where central dopaminergic dysfunction\
    \ appears before peripheral autonomic marker loss."
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
citation_count: 36
artifact_count: 18
artifact_sources:
  openscientist_artifacts_zip: 18
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
- filename: provenance_evidence_matrix_summary.json
  path: openscientist_artifacts/provenance_evidence_matrix_summary.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix summary
- filename: provenance_evidence_matrix_summary.png
  path: openscientist_artifacts/provenance_evidence_matrix_summary.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix summary
- filename: provenance_final_evidence_summary.json
  path: openscientist_artifacts/provenance_final_evidence_summary.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final evidence summary
- filename: provenance_final_evidence_summary.png
  path: openscientist_artifacts/provenance_final_evidence_summary.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final evidence summary
- filename: provenance_final_gaps_alternatives.json
  path: openscientist_artifacts/provenance_final_gaps_alternatives.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final gaps alternatives
- filename: provenance_final_gaps_alternatives.png
  path: openscientist_artifacts/provenance_final_gaps_alternatives.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final gaps alternatives
- filename: provenance_mechanistic_causal_chain.json
  path: openscientist_artifacts/provenance_mechanistic_causal_chain.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist mechanistic causal chain
- filename: provenance_mechanistic_causal_chain.png
  path: openscientist_artifacts/provenance_mechanistic_causal_chain.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist mechanistic causal chain
- filename: provenance_plot_1.json
  path: openscientist_artifacts/provenance_plot_1.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 1
- filename: provenance_plot_1.png
  path: openscientist_artifacts/provenance_plot_1.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 1
- filename: provenance_plot_2.json
  path: openscientist_artifacts/provenance_plot_2.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 2
- filename: provenance_plot_2.png
  path: openscientist_artifacts/provenance_plot_2.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 2
- filename: provenance_plot_3.json
  path: openscientist_artifacts/provenance_plot_3.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 3
- filename: provenance_plot_3.png
  path: openscientist_artifacts/provenance_plot_3.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 3
- filename: provenance_plot_4.json
  path: openscientist_artifacts/provenance_plot_4.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 4
- filename: provenance_plot_4.png
  path: openscientist_artifacts/provenance_plot_4.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 4
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Parkinson's Disease
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** brain_first_central_alpha_synuclein_model
- **Hypothesis Label:** Brain-First Central α-Synuclein Initiation Model
- **Status in KB:** ALTERNATIVE

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: brain_first_central_alpha_synuclein_model
hypothesis_label: Brain-First Central α-Synuclein Initiation Model
status: ALTERNATIVE
description: Alpha-synuclein pathology initiates within central nervous system sites such as the olfactory
  bulb or amygdala and spreads centrifugally to brainstem and peripheral autonomic structures. This model
  best explains Parkinson disease presentations where central dopaminergic or olfactory involvement precedes
  prominent autonomic and enteric manifestations.
notes: The model is supported mainly by subtype-level human imaging, clinical, and neuropathological patterns.
  It competes with, rather than refutes, the body-first model because both origin routes may exist within
  clinically diagnosed Parkinson disease.
evidence:
- reference: PMID:38519273
  reference_title: 'Brain-first vs. body-first Parkinson''s disease: An update on recent evidence.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: the initial pathology starts either in the olfactory bulb or amygdala leading to a brain-first
    subtype, or in the enteric nervous system leading to a body-first subtype.
  explanation: The ASOC model explicitly defines an olfactory bulb/amygdala origin as the brain-first
    subtype that competes with the enteric body-first route.
- reference: PMID:38519273
  reference_title: 'Brain-first vs. body-first Parkinson''s disease: An update on recent evidence.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: These subtypes should be distinguishable early in the disease course on a range of imaging,
    clinical, and neuropathological markers.
  explanation: Human subtype distinguishability supports representing brain-first and body-first disease
    routes as alternative mechanistic hypothesis groups.
- reference: PMID:32830221
  reference_title: 'Brain-first versus body-first Parkinson''s disease: a multimodal imaging case-control
    study.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: the PDRBD- data were compatible with a brain-first trajectory, characterized by primary loss
    of putaminal FDOPA uptake followed by a secondary loss of cardiac MIBG signal and 11C-donepezil signal.
  explanation: Primary multimodal imaging data support a brain-first trajectory in RBD-negative de novo
    PD, where central dopaminergic dysfunction appears before peripheral autonomic marker loss.
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

# Brain-First Central α-Synuclein Initiation Model in Parkinson's Disease: Hypothesis Evaluation Report

**Hypothesis ID:** brain_first_central_alpha_synuclein_model
**Disease:** Parkinson's Disease (Complex)
**KB Status:** ALTERNATIVE
**Evaluation Date:** 2026-07-06
**Papers Reviewed:** 82 | **Findings Confirmed:** 15 | **Iterations:** 5

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — Retain ALTERNATIVE status in the Knowledge Base.**

The brain-first central α-synuclein initiation model proposes that in a subset of Parkinson's disease (PD) patients, α-synuclein pathology originates within central nervous system sites — principally the olfactory bulb or amygdala — and spreads centrifugally to brainstem and peripheral autonomic structures. This model is supported by three convergent lines of evidence: large-scale neuropathological trajectory modeling showing 81.9% of Lewy body disease donors have earliest pathology in the olfactory bulb; multimodal molecular imaging demonstrating asymmetric central dopaminergic loss preceding peripheral autonomic denervation in RBD-negative PD; and animal models confirming olfactory bulb-to-limbic-to-brainstem α-synuclein propagation in both primates and transgenic mice. Additional supporting data include distinct genetic pathway enrichments (synaptic/immune in brain-first vs. lysosomal/autophagy in body-first), pronounced amygdala degeneration with a large effect size (Cohen's d = −1.22), and differential peripheral autonomic markers that distinguish subtypes in early disease.

However, five critical qualifications prevent an upgrade to "supported" status. First, the proxy classification using REM sleep behavior disorder (RBD) as a surrogate for body-first PD suffers from profound methodological variability, with RBD prevalence in PD ranging from 17.8% to 62.5% depending on ascertainment method. Second, no prospective longitudinal human study has directly tracked α-synuclein pathology from a CNS origin site to peripheral structures in living patients. Third, the subtypes converge clinically and pathologically in advanced disease, reducing their discriminative value over time. Fourth, data-driven subtyping approaches outperform the brain-first/body-first classification for predicting disease progression milestones. Fifth, the model remains unintegrated into the emerging NSD-ISS and SynNeurGe biological staging frameworks that define PD by biomarker status rather than origin site. These caveats collectively indicate that while the brain-first model captures a real biological phenomenon in a subset of PD patients, it is best understood as one component of a more complex, heterogeneous disease landscape.

---

## Summary

The brain-first central α-synuclein initiation model, formalized within the α-Synuclein Origin and Connectome (SOC) framework by Borghammer and colleagues, represents a significant advance in understanding PD heterogeneity. Our systematic evaluation across 82 publications and 15 confirmed findings reveals that the model is well-supported at the subtype level by imaging and neuropathological evidence but faces important limitations in clinical translation, biomarker validation, and framework integration.

The strongest evidence comes from Horsager et al. (2020), who demonstrated that RBD-negative de novo PD patients show primary loss of putaminal dopaminergic function before peripheral autonomic marker decline — the temporal ordering predicted by a brain-first trajectory. This is reinforced by Mastenbroek et al. (2024), whose data-driven modeling of 814 brain donors showed that 81.9% exhibited earliest Lewy body pathology in the olfactory bulb. Animal models by Sawamura et al. (2022) in marmosets and Uemura et al. (2021) in mice confirm that α-synuclein preformed fibrils injected into the olfactory bulb propagate along predicted pathways to limbic and brainstem structures, including the substantia nigra.

Key challenges include the reliance on RBD as a classification proxy, the absence of direct longitudinal tracking in humans, conflicting structural MRI findings, the limited utility of seed amplification assays for subtype differentiation in established disease, and the superior prognostic performance of data-driven subtyping approaches. These gaps define the frontier for future research and suggest that the brain-first model, while mechanistically plausible, requires integration with molecular and genetic frameworks to achieve clinical utility.

---

## Key Findings

### Finding 1: Multimodal Imaging Supports the Brain-First Trajectory in RBD-Negative PD

The foundational imaging evidence for the brain-first model comes from the Aarhus group's multimodal imaging studies. Horsager et al. (2020) ([PMID: 32830221](https://pubmed.ncbi.nlm.nih.gov/32830221/)) conducted a case-control study showing that in RBD-negative de novo PD (the brain-first proxy), putaminal FDOPA uptake was reduced before cardiac MIBG and 11C-donepezil signals declined, establishing the temporal ordering of central-before-peripheral dysfunction. Knudsen et al. (2021) ([PMID: 34334424](https://pubmed.ncbi.nlm.nih.gov/34334424/)) extended this by demonstrating significantly more asymmetric nigrostriatal degeneration in brain-first versus body-first PD in both FDOPA PET (p = 0.001) and DaT SPECT (p = 0.001) datasets. Most recently, Schröter et al. (2025) ([PMID: 40209563](https://pubmed.ncbi.nlm.nih.gov/40209563/)) showed that amygdala degeneration was significantly more pronounced in brain-first versus body-first PD (increased free interstitial fluid, p = 0.02, Cohen's d = −1.22), providing structural MRI evidence for the amygdala as an early pathology site.

{{figure:evidence_matrix_summary.png|caption=Summary of evidence types and their support/refutation status for the brain-first α-synuclein initiation model across 40 evidence items}}

### Finding 2: Neuropathological Trajectory Modeling Shows Olfactory-First Predominance

Mastenbroek et al. (2024) ([PMID: 38879548](https://pubmed.ncbi.nlm.nih.gov/38879548/)) applied data-driven disease progression modeling to regional Lewy body density scores from 814 brain donors and identified three distinct trajectories. The majority (81.9%) showed earliest pathology in the olfactory bulb, with subsequent spread to either limbic regions (60.8%) or brainstem regions (21.1%). The remaining 18.1% exhibited brainstem-first pathology associated with substantial Lewy body pathology outside the brain — consistent with body-first predictions. This large-scale neuropathological study provides perhaps the most direct support for the brain-first model, demonstrating that olfactory-initiated pathology is the predominant trajectory in Lewy body disease, though importantly not the only one.

### Finding 3: Animal Models Confirm Olfactory Bulb-Initiated α-Synuclein Propagation

Two key animal studies provide mechanistic proof-of-concept. Sawamura et al. (2022) ([PMID: 35989519](https://pubmed.ncbi.nlm.nih.gov/35989519/)) injected α-synuclein preformed fibrils (PFFs) into the olfactory bulb of marmosets, producing severe pathology along the olfactory pathway and limbic system, with mild pathology reaching the substantia nigra pars compacta, locus coeruleus, and even the dorsal motor nucleus of the vagus nerve. Uemura et al. (2021) ([PMID: 33547846](https://pubmed.ncbi.nlm.nih.gov/33547846/)) performed similar injections in BAC-SNCA transgenic mice and observed pathology first along the olfactory pathway, then in limbic structures, accompanied by hyposmia, anxiety, and memory impairment — but notably not motor dysfunction. These studies confirm the anatomical plausibility of olfactory-to-limbic-to-brainstem spread but also highlight that animal models may not fully recapitulate the motor phenotype of human PD.

### Finding 4: Conflicting Structural MRI Findings

While molecular imaging generally supports the model, structural MRI studies show mixed results. Banwinkler et al. (2022) ([PMID: 35943058](https://pubmed.ncbi.nlm.nih.gov/35943058/)) analyzed 255 de novo PD patients from the PPMI cohort and found that putaminal DaT asymmetry was not associated with reduced gray matter volume (GMV) or higher GMV asymmetry, and RBD-negative versus RBD-positive patients did not demonstrate significant GMV differences. This negative finding from a large cohort directly challenges one prediction of the brain-first model. Notably, Horsager & Borghammer (2024) ([PMID: 38519273](https://pubmed.ncbi.nlm.nih.gov/38519273/)) themselves acknowledged that "molecular imaging studies were generally in agreement with the model, whereas structural imaging studies, such as MRI volumetry, showed conflicting findings." However, Shi et al. (2025) ([PMID: 41309711](https://pubmed.ncbi.nlm.nih.gov/41309711/)) did find differential MRI structural and functional axial asymmetry between subtypes in a multi-cohort validation study, suggesting that specific MRI metrics and analysis approaches may capture subtype-specific patterns that global GMV measures miss.

### Finding 5: Peripheral Autonomic Markers Differentiate Subtypes in Early Disease

Walter et al. (2026) ([PMID: 42390607](https://pubmed.ncbi.nlm.nih.gov/42390607/)) demonstrated that during the first decade of motor disease, vagal atrophy and dysfunction occurred in body-first but not brain-first PD, and sympathetic pupillary innervation was reduced in de novo body-first but not brain-first PD. Kim et al. (2024) ([PMID: 39665845](https://pubmed.ncbi.nlm.nih.gov/39665845/)) showed delayed gastric emptying was more prevalent in body-first PD compared to brain-first PD. These findings provide independent validation that peripheral autonomic markers can differentiate the proposed subtypes, particularly in early disease stages.

### Finding 6: Distinct Genetic Pathways for Brain-First and Body-First Subtypes

Passaretti et al. (2025) ([PMID: 40542411](https://pubmed.ncbi.nlm.nih.gov/40542411/)) analyzed 910 prodromal and 1,120 clinical PD cases from PPMI over 12 years and found that body-first cases were enriched for lysosomal/autophagy genetic pathways while brain-first cases were enriched for synaptic/immune pathways. Body-first cases showed more pronounced changes in caudal locus coeruleus and symmetrical striatal/glymphatic alterations. Both phenotypes were stable over time and predicted conversion in prodromal cases, lending biological credibility to the subtype distinction beyond purely clinical classification.

### Finding 7: RBD-Based Classification Has Fundamental Methodological Limitations

The brain-first/body-first classification relies heavily on RBD status as a surrogate marker, but RBD prevalence in PD varies dramatically by ascertainment method. Zhang et al. (2026) ([PMID: 41714532](https://pubmed.ncbi.nlm.nih.gov/41714532/)) found PSG-confirmed RBD prevalence of only 17.8% in 264 PD patients, while Sobreira-Neto et al. (2017) ([PMID: 29084403](https://pubmed.ncbi.nlm.nih.gov/29084403/)) found 62.5% in 88 consecutive PD patients using video-PSG. Li et al. (2023) ([PMID: 37422999](https://pubmed.ncbi.nlm.nih.gov/37422999/)) demonstrated significant sex differences in RBD prevalence. This 3.5-fold range in RBD prevalence fundamentally undermines the reliability of body-first proportion estimates and, by extension, brain-first classification accuracy.

### Finding 8: Data-Driven Subtyping Outperforms Brain-First/Body-First for Prognosis

Negida et al. (2025) ([PMID: 40678221](https://pubmed.ncbi.nlm.nih.gov/40678221/)) directly compared clinical (TD, PIGD), pathological (brain-first, body-first), and data-driven (DM, IM, MMP) PD subtypes for progression milestone attainment over 10 years in PPMI data. Data-driven subtypes exhibited the highest progression rates, with diffuse malignant (DM) patients attaining 50% of milestones versus PIGD 43% and body-first 42%. DM had more than twice the hazard of progression compared to the mild motor-predominant subtype (SHR 2.02, 95% CI 1.49–2.75, p < 0.001). Trial power simulations showed enrolling DM patients could reduce required sample sizes by approximately 50%, suggesting data-driven subtyping has greater practical utility for clinical trial design.

### Finding 9: Dermal SAA Has Limited Subtype Differentiation Utility

Vieregge et al. (2025) ([PMID: 41316710](https://pubmed.ncbi.nlm.nih.gov/41316710/)) found that while patients with clinical features of suspected body-first PD showed slightly higher dermal α-synuclein seed amplification assay (SAA) titers, significant differences were mainly observed between iRBD patients and PD patients, not between brain-first and body-first PD subgroups. The authors concluded that widespread α-synuclein aggregation in advanced PD limits the use of dermal SAA for subtype differentiation. Hall et al. (2022) ([PMID: 35733234](https://pubmed.ncbi.nlm.nih.gov/35733234/)) additionally showed that CSF α-synuclein RT-QuIC sensitivity dropped to only 57% for non-standard/incidental Lewy body disease, relevant to early brain-first detection when pathology may be focal.

### Finding 10: Biological Staging Frameworks Are Orthogonal to Origin-Site Classification

The NSD-ISS biological staging system (Simuni et al. 2024, [PMID: 38267190](https://pubmed.ncbi.nlm.nih.gov/38267190/)) defines PD by the presence of pathological α-synuclein (S) and dopaminergic neuronal dysfunction (D) regardless of clinical phenotype. The SynNeurGe framework (Höglinger & Lang 2025, [PMID: 39973492](https://pubmed.ncbi.nlm.nih.gov/39973492/)) integrates α-synuclein pathology, neurodegeneration, and genetics. Neither framework incorporates brain-first versus body-first origin site, creating a conceptual gap that must be bridged for the model to achieve clinical integration.

### Finding 11: Brain-First PD May Be the Dominant Subtype with Younger Onset

Nagaraj et al. (2026) ([PMID: 40796681](https://pubmed.ncbi.nlm.nih.gov/40796681/)) found that among 400 PD patients in an Indian cohort, body-first patients constituted only 9.5%, suggesting brain-first may be the dominant subtype. Stefanis & Borghammer (2025) ([PMID: 41195692](https://pubmed.ncbi.nlm.nih.gov/41195692/)) proposed that mean age of motor onset in brain-first PD may be up to 10 years earlier than body-first PD, with early onset PD showing features related to brain-first PD including relative clinical and nigrostriatal asymmetry and a restricted motor phenotype.

{{figure:mechanistic_causal_chain.png|caption=Mechanistic causal chain of the brain-first α-synuclein initiation model from upstream triggers through clinical manifestation, with evidence strength ratings}}

---

## Mechanistic Causal Chain

The brain-first model implies the following causal chain from upstream trigger to clinical manifestation:

### Step 1: Environmental/Genetic Trigger → α-Synuclein Misfolding at CNS Origin Site
**Evidence strength: Moderate (inferred)**

The upstream trigger initiating α-synuclein misfolding in the olfactory bulb or amygdala remains incompletely characterized. Dorsey et al. (2024) ([PMID: 38607765](https://pubmed.ncbi.nlm.nih.gov/38607765/)) proposed that inhaled toxicants (pesticides, industrial chemicals, air pollution) passing through the nose could trigger pathological changes in α-synuclein in the olfactory system. Genetic factors also play a role: brain-first PD is enriched for synaptic/immune pathway variants ([PMID: 40542411](https://pubmed.ncbi.nlm.nih.gov/40542411/)), and LRRK2-variant carriers mostly resemble a brain-first profile ([PMID: 35031485](https://pubmed.ncbi.nlm.nih.gov/35031485/)). However, the specific molecular events converting normal α-synuclein to pathological seeds at CNS sites remain uncharacterized, and no direct causal evidence links specific environmental exposures to brain-first PD initiation in humans.

### Step 2: Prion-Like Propagation from Origin Site → Ipsilateral Limbic/Brainstem Spread
**Evidence strength: Strong (animal models) / Moderate (human inference)**

The SOC model ([PMID: 33682732](https://pubmed.ncbi.nlm.nih.gov/33682732/)) predicts that unilateral α-synuclein pathology in the amygdala spreads preferentially via ipsilateral connections due to the lateralized connectivity architecture of the human brain. Animal models robustly support this: marmoset olfactory bulb injection produced severe pathology along olfactory and limbic pathways with spread to substantia nigra ([PMID: 35989519](https://pubmed.ncbi.nlm.nih.gov/35989519/)); mouse olfactory bulb injection showed sequential olfactory→limbic→brainstem propagation ([PMID: 33547846](https://pubmed.ncbi.nlm.nih.gov/33547846/)). Computational modeling by Bhattacharjee et al. (2022, [PMID: 34910119](https://pubmed.ncbi.nlm.nih.gov/34910119/)) confirmed that brain connectome topology and α-synuclein gene expression together predict pathology distribution following seeded propagation.

### Step 3: Asymmetric Nigrostriatal Degeneration → Motor Asymmetry
**Evidence strength: Strong (human imaging)**

The asymmetric ipsilateral spread from a unilateral CNS origin predicts asymmetric dopaminergic neurodegeneration, which is a hallmark of brain-first PD. This is directly supported by Knudsen et al. (2021) ([PMID: 34334424](https://pubmed.ncbi.nlm.nih.gov/34334424/)) showing significantly more asymmetric nigrostriatal degeneration in brain-first versus body-first PD (p = 0.001 in both FDOPA PET and DaT SPECT). The association between brain-first PD and therapy-resistant rest tremor with greater dopaminergic asymmetry ([PMID: 39370052](https://pubmed.ncbi.nlm.nih.gov/39370052/)) further supports this link.

### Step 4: Secondary Centrifugal Spread → Delayed Peripheral Autonomic Involvement
**Evidence strength: Strong (human imaging/clinical)**

The model predicts that peripheral autonomic denervation occurs secondarily in brain-first PD, after central dopaminergic dysfunction. This is supported by the temporal ordering of imaging markers in Horsager et al. (2020) ([PMID: 32830221](https://pubmed.ncbi.nlm.nih.gov/32830221/)) and by Walter et al. (2026) ([PMID: 42390607](https://pubmed.ncbi.nlm.nih.gov/42390607/)) showing vagal and pupillary autonomic markers are preserved in early brain-first PD but compromised in body-first PD.

### Missing Causal Steps

| Gap | Status | Importance |
|-----|--------|------------|
| Specific trigger converting normal to pathological α-synuclein at CNS sites | Unknown | Critical — foundational to the model |
| Whether α-synuclein strain differences determine brain-first vs. body-first | Uncharacterized | High — could explain divergent trajectories |
| Mechanism by which ipsilateral connectivity bias produces asymmetric spread | Inferred from connectomics | Moderate — computationally supported but unvalidated in humans |
| Why some olfactory-first pathology spreads to limbic vs. brainstem regions | Unknown | High — explains within-brain-first heterogeneity |
| Timeline from initial misfolding to clinical detection in humans | No longitudinal data | Critical — required for early intervention |

{{figure:final_evidence_summary.png|caption=Comprehensive four-panel summary showing evidence distribution, confidence levels, knowledge gaps, and timeline of key publications}}

---

## Evidence Matrix

| Citation | Evidence Type | Direction | Mechanistic Claim | Key Finding | Subtype/Context | Confidence | Limitations |
|----------|--------------|-----------|-------------------|-------------|-----------------|------------|-------------|
| [PMID: 32830221](https://pubmed.ncbi.nlm.nih.gov/32830221/) | Human clinical (imaging) | Supports | Central dopaminergic loss precedes peripheral autonomic loss in brain-first PD | FDOPA loss before MIBG/donepezil decline in RBD− PD | De novo RBD-negative PD | High | Small sample; cross-sectional design limits temporal inference |
| [PMID: 34334424](https://pubmed.ncbi.nlm.nih.gov/34334424/) | Human clinical (imaging) | Supports | Brain-first PD has asymmetric dopaminergic degeneration | Asymmetry significantly greater in FDOPA (p=0.001) and DaT SPECT (p=0.001) | Brain-first vs body-first PD | High | RBD-based classification; retrospective |
| [PMID: 38879548](https://pubmed.ncbi.nlm.nih.gov/38879548/) | Human neuropathology | Supports | Olfactory bulb is the most common origin site for LB pathology | 81.9% olfactory-first in 814 brain donors; three distinct trajectories | All Lewy body disorders | High | Post-mortem; cannot confirm in vivo timing |
| [PMID: 40209563](https://pubmed.ncbi.nlm.nih.gov/40209563/) | Human clinical (MRI) | Supports | Amygdala is an early brain-first pathology site | Greater amygdala degeneration in brain-first (p=0.02, d=−1.22) | Brain-first vs body-first PD | Moderate | Small sample (n=42 total); single-center |
| [PMID: 35989519](https://pubmed.ncbi.nlm.nih.gov/35989519/) | Model organism (primate) | Supports | OB-initiated α-synuclein propagates to brainstem | Severe OB/limbic pathology; mild SN, LC, DMNV pathology in marmosets | Animal model | High | Species differences; PFF model limitations |
| [PMID: 33547846](https://pubmed.ncbi.nlm.nih.gov/33547846/) | Model organism (mouse) | Supports | OB-initiated α-synuclein causes hyposmia and limbic dysfunction | Sequential OB→limbic→brainstem spread; hyposmia, anxiety, memory loss | BAC-SNCA transgenic mice | Moderate | Transgenic overexpression; no motor phenotype |
| [PMID: 40542411](https://pubmed.ncbi.nlm.nih.gov/40542411/) | Human clinical (genetic) | Supports | Subtypes have distinct genetic pathway enrichment | Brain-first: synaptic/immune; body-first: lysosomal/autophagy | PPMI cohort (n=2030) | High | RBD-based classification; pathway-level |
| [PMID: 42390607](https://pubmed.ncbi.nlm.nih.gov/42390607/) | Human clinical | Supports | Peripheral autonomic markers intact early in brain-first PD | Vagal atrophy/dysfunction only in body-first during first decade | Early-stage PD subtypes | High | Cross-sectional; single study |
| [PMID: 41195692](https://pubmed.ncbi.nlm.nih.gov/41195692/) | Human clinical (review) | Supports | Brain-first PD associated with younger onset age | Onset up to 10 years earlier; more asymmetric motor phenotype | Population-level | Moderate | Review-level synthesis; age proxy not validated |
| [PMID: 40796681](https://pubmed.ncbi.nlm.nih.gov/40796681/) | Human clinical | Supports (qualified) | Brain-first is dominant subtype | Body-first only 9.5% in Indian cohort; unexpected clinical features | Indian PD (n=400) | Moderate | Single-center; geographic variation possible |
| [PMID: 41309711](https://pubmed.ncbi.nlm.nih.gov/41309711/) | Human clinical (MRI) | Supports | Subtypes have distinct structural/functional asymmetry | Differential GMV and zALFF in multi-cohort validation | Brain-first vs body-first PD | Moderate | Multi-cohort but small per-site samples |
| [PMID: 39370052](https://pubmed.ncbi.nlm.nih.gov/39370052/) | Human clinical | Supports | Brain-first enriched in therapy-resistant rest tremor | RT-resistant patients enriched with brain-first profile | PPMI 5-year follow-up | Moderate | Indirect association |
| [PMID: 40250815](https://pubmed.ncbi.nlm.nih.gov/40250815/) | Human clinical (fMRI) | Supports | Amygdala FC distinguishes subtypes | Amygdala FC differed; AUC=0.834 for subtype discrimination | Early-stage PD (PPMI) | Moderate | Small sample; needs replication |
| [PMID: 35943058](https://pubmed.ncbi.nlm.nih.gov/35943058/) | Human clinical (MRI) | Refutes | Brain-first should show GMV asymmetry | No GMV differences between RBD+ and RBD− in 255 PPMI patients | De novo PD (PPMI) | High | Large cohort negative finding |
| [PMID: 38519273](https://pubmed.ncbi.nlm.nih.gov/38519273/) | Review | Qualifies | Structural imaging conflicts acknowledged | Model proponents note MRI volumetry conflicts | All PD subtypes | High (review-level) | Self-acknowledgment of limitation |
| [PMID: 41316710](https://pubmed.ncbi.nlm.nih.gov/41316710/) | Human clinical (biomarker) | Qualifies | Peripheral SAA should differentiate subtypes | Dermal SAA cannot reliably distinguish subtypes in established PD | Established PD | Moderate | Widespread α-synuclein limits applicability |
| [PMID: 35733234](https://pubmed.ncbi.nlm.nih.gov/35733234/) | Human clinical (biomarker) | Qualifies | CSF SAA detects early brain-first pathology | Only 57% sensitivity for non-standard/incidental LBD | Early/focal LB pathology | Moderate | RT-QuIC; focal pathology detection gap |
| [PMID: 40678221](https://pubmed.ncbi.nlm.nih.gov/40678221/) | Human clinical (comparative) | Competing | Brain-first/body-first is optimal classification | Data-driven DM: 50% milestones vs body-first 42%; SHR 2.02 | PPMI 10-year follow-up | High | Different goals; not mutually exclusive |
| [PMID: 41714532](https://pubmed.ncbi.nlm.nih.gov/41714532/) | Human clinical | Qualifies | RBD is reliable body-first proxy | PSG-confirmed RBD prevalence only 17.8% vs questionnaire 40–60% | PD (n=264) | High | Fundamental measurement problem |
| [PMID: 29084403](https://pubmed.ncbi.nlm.nih.gov/29084403/) | Human clinical | Qualifies | RBD prevalence consistency | Video-PSG found RBD in 62.5% of 88 PD patients | PD (n=88) | Moderate | Small sample; method-dependent |
| [PMID: 38267190](https://pubmed.ncbi.nlm.nih.gov/38267190/) | Framework/consensus | Qualifies | Biological staging integrates origin site | NSD-ISS defines PD by SAA/DAT status, orthogonal to origin | All PD | High | Framework design, not refutation |
| [PMID: 39973492](https://pubmed.ncbi.nlm.nih.gov/39973492/) | Framework/consensus | Qualifies | SynNeurGe accommodates origin site | Does not incorporate brain-first/body-first but could | All PD | High | Framework design, not refutation |
| [PMID: 31797870](https://pubmed.ncbi.nlm.nih.gov/31797870/) | In vitro (biochemical) | Qualifies | α-syn strains contribute to subtype divergence | Greater structural heterogeneity in PD vs MSA fibrils | PD vs MSA | Moderate | No brain-first vs body-first comparison |
| [PMID: 33978813](https://pubmed.ncbi.nlm.nih.gov/33978813/) | In vitro/model | Qualifies | Local environment determines α-syn strain | p25α redirects α-syn into distinct strain with different properties | In vitro/in vivo | Moderate | MSA-focused; relevance to PD subtypes inferred |
| [PMID: 31254094](https://pubmed.ncbi.nlm.nih.gov/31254094/) | Model organism (rat) | Competing (body-first) | Gut-to-brain α-syn propagation | Bidirectional trans-synaptic propagation from duodenum in BAC rats | Body-first animal model | High | BAC overexpression; not wild-type |

---

## Alternative and Competing Models

### 1. Body-First (Gut-First) Model
**Relationship: Direct alternative (competing origin route)**

The body-first model proposes that α-synuclein pathology initiates in the enteric nervous system and propagates retrogradely via the vagus nerve to the brainstem. Evidence includes: bidirectional trans-synaptic α-synuclein propagation from the duodenum in BAC-SNCA rats ([PMID: 31254094](https://pubmed.ncbi.nlm.nih.gov/31254094/)); the strong association of iRBD with subsequent PD development ([PMID: 30166532](https://pubmed.ncbi.nlm.nih.gov/30166532/)); and reduced MIBG uptake in prodromal conditions ([PMID: 40754311](https://pubmed.ncbi.nlm.nih.gov/40754311/)). The SOC model positions brain-first and body-first as complementary rather than mutually exclusive, with both routes operative in different patients.

### 2. Braak Staging Model (Unified Ascending Pathology)
**Relationship: Predecessor model, partially superseded**

Braak's original staging posits a single caudo-rostral ascending trajectory from the lower brainstem. The brain-first model emerged precisely because Braak staging could not account for PD cases without lower brainstem pathology at early stages ([PMID: 37062013](https://pubmed.ncbi.nlm.nih.gov/37062013/)). Neuropathological data showing 81.9% olfactory-first pathology ([PMID: 38879548](https://pubmed.ncbi.nlm.nih.gov/38879548/)) fundamentally challenges Braak's single-trajectory assumption.

### 3. Data-Driven Phenotypic Subtypes (DM/IM/MMP)
**Relationship: Parallel classification system (agnostic to origin)**

Data-driven clustering identifies subtypes based on clinical trajectory rather than inferred origin site. Negida et al. (2025) ([PMID: 40678221](https://pubmed.ncbi.nlm.nih.gov/40678221/)) showed these subtypes outperform brain-first/body-first for predicting progression milestones. This approach is origin-agnostic but more clinically actionable for trial design. The two frameworks are not mutually exclusive and could be integrated.

### 4. Multicentric/Stochastic Origin Model
**Relationship: Alternative to single-origin hypothesis**

Some evidence suggests α-synuclein pathology may arise simultaneously at multiple sites rather than spreading from a single origin. Neuropathological data showing cases with α-synuclein pathology in midbrain and limbic cortex without medullary involvement ([PMID: 15480835](https://pubmed.ncbi.nlm.nih.gov/15480835/)) suggests deviation from stereotypic expansion patterns, consistent with multicentric initiation in at least some cases.

### 5. α-Synuclein Strain Hypothesis
**Relationship: Potential upstream determinant of brain-first vs. body-first**

Strohäker et al. (2019) ([PMID: 31797870](https://pubmed.ncbi.nlm.nih.gov/31797870/)) showed greater structural heterogeneity among α-synuclein fibrils from PD brain compared to MSA brain. Ferreira et al. (2021) ([PMID: 33978813](https://pubmed.ncbi.nlm.nih.gov/33978813/)) demonstrated that local cellular environment (p25α presence) can redirect α-synuclein into distinct strains with different structures and prodegenerative properties. If different strains preferentially arise at or propagate from different anatomical sites, strain biology could be the molecular determinant of brain-first versus body-first trajectories. No studies have directly compared strains between subtypes.

{{figure:final_gaps_alternatives.png|caption=Knowledge gap mapping to discriminating tests and comparison of alternative models for Parkinson's disease α-synuclein origin}}

---

## Knowledge Gaps

### Gap 1: No Prospective Longitudinal Validation in Humans
**Scope:** Critical — the entire brain-first temporal ordering is inferred from cross-sectional data and post-mortem studies.
**What was checked:** All imaging studies ([PMID: 32830221](https://pubmed.ncbi.nlm.nih.gov/32830221/), [PMID: 34334424](https://pubmed.ncbi.nlm.nih.gov/34334424/), [PMID: 40209563](https://pubmed.ncbi.nlm.nih.gov/40209563/), [PMID: 42390607](https://pubmed.ncbi.nlm.nih.gov/42390607/)) are cross-sectional case-control designs. No study was found tracking the same individuals from pre-symptomatic α-synuclein seeding to established PD with serial multi-organ imaging.
**Resolution:** A prodromal cohort study with serial SAA, DaT SPECT, MIBG, and olfactory testing in SAA-positive/iRBD-negative hyposmic individuals followed longitudinally for 10+ years.

### Gap 2: α-Synuclein Strain Characterization Across Subtypes
**Scope:** High importance — strains may be the molecular basis of subtype divergence.
**What was checked:** Strohäker et al. ([PMID: 31797870](https://pubmed.ncbi.nlm.nih.gov/31797870/)) compared PD vs. MSA strains; Ferreira et al. ([PMID: 33978813](https://pubmed.ncbi.nlm.nih.gov/33978813/)) showed environment-dependent strain formation. No study was found directly comparing α-synuclein strains between brain-first and body-first PD patients.
**Resolution:** Comparative cryo-EM or hydrogen-deuterium exchange analysis of SAA-amplified seeds from CSF, olfactory mucosa, and skin biopsies of well-characterized brain-first versus body-first patients.

### Gap 3: RBD Proxy Reliability and Standardization
**Scope:** Fundamental to current classification. RBD prevalence ranges from 17.8% (PSG-confirmed, [PMID: 41714532](https://pubmed.ncbi.nlm.nih.gov/41714532/)) to 62.5% (video-PSG, [PMID: 29084403](https://pubmed.ncbi.nlm.nih.gov/29084403/)).
**What was checked:** Multiple studies confirmed dramatic variability by ascertainment method, sex ([PMID: 37422999](https://pubmed.ncbi.nlm.nih.gov/37422999/)), and cultural context ([PMID: 40796681](https://pubmed.ncbi.nlm.nih.gov/40796681/)).
**Resolution:** Consensus protocol for RBD ascertainment in brain-first/body-first research; development of non-RBD classification biomarkers (e.g., combined SAA topography + DaT asymmetry + autonomic panels).

### Gap 4: Integration with NSD-ISS/SynNeurGe Frameworks
**Scope:** The emerging biological definition of PD ([PMID: 38267190](https://pubmed.ncbi.nlm.nih.gov/38267190/), [PMID: 39973492](https://pubmed.ncbi.nlm.nih.gov/39973492/)) does not incorporate origin site.
**What was checked:** Both frameworks were reviewed; neither includes a brain-first/body-first dimension.
**Resolution:** Formal proposal for adding an origin-site modifier (e.g., O1 = brain-first, O2 = body-first) to NSD-ISS or SynNeurGe staging, with validation against clinical outcomes.

### Gap 5: Subtype Convergence in Advanced Disease
**Scope:** Multiple studies indicate brain-first and body-first subtypes become clinically indistinguishable over time, reducing long-term clinical utility.
**What was checked:** Dermal SAA fails to differentiate established PD subtypes ([PMID: 41316710](https://pubmed.ncbi.nlm.nih.gov/41316710/)); GMV differences are not present at baseline but emerge differentially over 48 months ([PMID: 40771982](https://pubmed.ncbi.nlm.nih.gov/40771982/)).
**Resolution:** Long-term (>10 year) longitudinal cohorts with repeated multimodal assessment to define when and how subtypes converge.

### Gap 6: Upstream Environmental Triggers Unvalidated in Humans
**Scope:** The inhaled-toxicant → olfactory α-synuclein hypothesis ([PMID: 38607765](https://pubmed.ncbi.nlm.nih.gov/38607765/)) remains speculative; air pollution and pesticide exposure data are epidemiological only.
**What was checked:** No interventional or mechanistic human study linking a specific inhaled toxicant to olfactory α-synuclein seeding was found.
**Resolution:** Biomonitoring studies in occupationally exposed populations combined with olfactory mucosa SAA and olfactory function testing.

### Gap 7: Source/Data Absences
**Scope:** No relevant GenCC or ClinGen entries specific to brain-first PD; no clinical trials stratified by brain-first/body-first; no single-cell transcriptomic comparison of olfactory bulb versus enteric α-synuclein pathology sites in human PD tissue.
**What was checked:** PubMed searched for clinical trials with brain-first/body-first stratification, GenCC/ClinGen references, and single-cell omics of PD olfactory tissue.
**Resolution:** snRNA-seq of olfactory bulb and enteric nervous system from well-characterized brain-first and body-first PD donors; clinical trial design incorporating origin-site stratification.

---

## Discriminating Tests

### Test 1: Prospective Multi-Organ Imaging in Prodromal Cohorts
- **Stratification:** SAA-positive hyposmic individuals without RBD (brain-first candidates) vs. iRBD patients (body-first candidates) vs. healthy SAA-negative controls
- **Biomarkers:** Serial DaT SPECT, cardiac MIBG, colonic 11C-donepezil PET, olfactory testing
- **Expected result:** Brain-first candidates should show DaT deficit before MIBG decline; body-first should show the reverse
- **Timeline:** 5–10 year longitudinal follow-up

### Test 2: Multi-Site SAA Topography
- **Sample type:** CSF, olfactory mucosa, skin (cervical C7 + leg), and colonic biopsies from the same patients
- **Patient stratification:** RBD-negative de novo PD vs. PD with pre-motor RBD vs. iRBD vs. healthy controls
- **Expected result:** Brain-first patients should have higher SAA positivity rates in olfactory mucosa relative to distal skin/gut; body-first should show the reverse gradient
- **Model system:** Cross-sectional, multi-center

### Test 3: Cryo-EM Strain Comparison
- **Sample type:** SAA-amplified α-synuclein seeds from CSF and olfactory mucosa
- **Patient stratification:** Well-characterized brain-first vs. body-first PD by multimodal imaging (not RBD alone)
- **Perturbation:** Compare fibril structure, seeding kinetics, and cellular toxicity profiles
- **Expected result:** Distinct structural polymorphs or kinetic signatures if strains determine trajectory

### Test 4: Vagotomy/Appendectomy Cohort Analysis Stratified by Origin
- **Cohort:** Large registry-based study of PD patients with history of vagotomy or appendectomy
- **Expected result:** If body-first PD is initiated peripherally, these procedures should preferentially reduce body-first PD incidence but not brain-first PD. Subtype classification of incident PD cases should show enrichment for brain-first features.

### Test 5: Clinical Trial with Origin-Site Stratification
- **Design:** Phase II disease-modification trial (e.g., anti-α-synuclein antibody) stratified by brain-first vs. body-first classification
- **Biomarkers:** DaT asymmetry index + MIBG + RBD status at baseline
- **Expected result:** Differential treatment response between subtypes would validate the biological distinction; if a CNS-penetrant therapy benefits brain-first more, it would confirm origin-site relevance to therapeutic targeting

---

## Curation Leads

*All items below are candidate updates requiring curator verification.*

### Candidate Evidence References

1. **[PMID: 40542411](https://pubmed.ncbi.nlm.nih.gov/40542411/)** — Passaretti et al. (2025): Add as SUPPORT evidence for brain-first model. Verified snippet: *"body-first cases displayed more pronounced changes in the caudal LC, as well as symmetrical alterations in the striatum and glymph."* Establishes distinct genetic pathway enrichment (synaptic/immune for brain-first).

2. **[PMID: 42390607](https://pubmed.ncbi.nlm.nih.gov/42390607/)** — Walter et al. (2026): Add as SUPPORT evidence. Verified snippet: *"During the first decade of motor disease, vagal atrophy and dysfunction occurred in body-first but not brain-first PD. Sympathetic pupillary innervation was reduced in de novo body-first but not brain-first PD patients."* Provides peripheral autonomic differentiation.

3. **[PMID: 35943058](https://pubmed.ncbi.nlm.nih.gov/35943058/)** — Banwinkler et al. (2022): Add as REFUTE/QUALIFY evidence. Verified snippet: *"the degree of putaminal DaT asymmetry was not associated with reduced GMV or higher GMV asymmetry."* Challenges structural MRI predictions.

4. **[PMID: 40678221](https://pubmed.ncbi.nlm.nih.gov/40678221/)** — Negida et al. (2025): Add as COMPETING evidence. Verified snippet: *"Data-driven subtypes exhibited the highest progression rates, with DM patients attaining 50% of milestones, surpassing PIGD (43.0%) and body-first (42.0%) subtypes."* Shows alternative classification superiority for prognosis.

5. **[PMID: 38879548](https://pubmed.ncbi.nlm.nih.gov/38879548/)** — Mastenbroek et al. (2024): Add as SUPPORT evidence. Snippet: *"Most donors (81.9%) show earliest pathology in the olfactory bulb, followed by accumulation in either limbic (60.8%) or brainstem (21.1%) regions."* Large-scale neuropathological validation.

6. **[PMID: 41714532](https://pubmed.ncbi.nlm.nih.gov/41714532/)** — Zhang et al. (2026): Add as QUALIFY evidence. Verified snippet from abstract context: *"RBD prevalence 47.1% vs 17.8% (p < 0.001)."* PSG-confirmed RBD prevalence of 17.8% highlights classification instability.

### Candidate Pathophysiology Nodes/Edges

- **Node:** Olfactory bulb α-synuclein seeding → Add as initial pathology site for brain-first subtype
- **Edge:** Olfactory bulb → amygdala → substantia nigra (ipsilateral) → confirmed in animal models, inferred in humans
- **Edge:** Amygdala → dorsal motor nucleus of vagus (centrifugal) → demonstrated in marmoset model ([PMID: 35989519](https://pubmed.ncbi.nlm.nih.gov/35989519/))
- **Node:** Synaptic/immune genetic pathway enrichment → brain-first specific molecular signature

### Candidate Ontology Terms

- **Cell types:** Olfactory sensory neurons (CL:0000066), dopaminergic neurons of substantia nigra (CL:0002148), amygdala neurons
- **Biological processes:** GO:0070841 (inclusion body assembly), GO:0031175 (neuron projection development), GO:0007409 (axonogenesis), GO:0006914 (autophagy)
- **Disease context:** MONDO:0005180 (Parkinson disease) with subtype qualifier for brain-first

### Candidate Status Assessment

- **Recommendation:** Retain **ALTERNATIVE** status. The evidence is strong at the subtype level but requires prospective longitudinal human validation, integration with biological staging frameworks, and resolution of the RBD proxy problem before an upgrade to ESTABLISHED.

### Candidate Knowledge Gaps for KB

1. **No longitudinal human validation of brain-first temporal ordering** — Critical gap; all evidence is cross-sectional or post-mortem
2. **α-Synuclein strain comparison between brain-first and body-first PD** — Not yet attempted; could resolve molecular basis
3. **RBD ascertainment standardization** — Unresolved methodological issue undermining all RBD-based studies
4. **NSD-ISS/SynNeurGe integration** — Frameworks are orthogonal to origin-site classification; formal proposal needed
5. **Single-cell omics of origin sites** — No snRNA-seq comparing olfactory bulb vs. enteric nervous system pathology in PD
6. **Upstream trigger validation** — No mechanistic human study linking specific inhaled toxicants to olfactory α-synuclein seeding

---

## Limitations of This Report

1. **Literature search scope:** This evaluation is based on 82 papers identified through iterative PubMed searches. Important evidence in non-English literature, conference abstracts, or preprints may have been missed.

2. **RBD proxy assumption:** Many conclusions about brain-first PD are derived from studies using RBD-negative status as a proxy, which has known limitations documented throughout this report.

3. **Publication bias:** Studies reporting significant subtype differences are more likely to be published than null findings, potentially inflating the perceived strength of the model.

4. **Temporal limitation:** This search was conducted through July 2026. Rapidly evolving areas (SAA technology, NSD-ISS validation studies, prodromal cohort results) may have produced relevant evidence not captured here.

5. **Cross-sectional evidence dominance:** The vast majority of evidence supporting the brain-first temporal ordering is cross-sectional. The causal chain should be interpreted as the best current inference rather than established fact.

---

## Proposed Follow-Up Experiments and Actions

1. **Immediate (KB curation):** Add the six candidate evidence references listed above; add knowledge gap entries for the seven gaps identified; consider adding α-synuclein strain comparison as a research priority.

2. **Short-term (1–2 years):** Design and fund a multi-site SAA topography study comparing olfactory mucosa, CSF, skin, and colonic biopsy SAA results across well-characterized brain-first and body-first PD patients classified by multimodal imaging (not RBD alone).

3. **Medium-term (2–5 years):** Initiate a prospective prodromal cohort study enrolling SAA-positive hyposmic individuals without RBD (brain-first candidates) for serial multi-organ imaging to directly test the predicted temporal ordering.

4. **Long-term (5–10 years):** Conduct a disease-modification trial with origin-site stratification to determine whether brain-first and body-first patients respond differently to CNS-targeted versus periphery-targeted α-synuclein therapies.

5. **Framework integration:** Propose a formal origin-site modifier for the NSD-ISS or SynNeurGe staging system and validate its additive prognostic value in existing cohorts (PPMI, DeNoPa, ICEBERG).

---

*Report generated July 2026. Based on systematic evaluation of 82 publications across 5 investigation iterations with 15 confirmed findings.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist evidence matrix summary](openscientist_artifacts/provenance_evidence_matrix_summary.json)
![OpenScientist evidence matrix summary](openscientist_artifacts/provenance_evidence_matrix_summary.png)
- [OpenScientist final evidence summary](openscientist_artifacts/provenance_final_evidence_summary.json)
![OpenScientist final evidence summary](openscientist_artifacts/provenance_final_evidence_summary.png)
- [OpenScientist final gaps alternatives](openscientist_artifacts/provenance_final_gaps_alternatives.json)
![OpenScientist final gaps alternatives](openscientist_artifacts/provenance_final_gaps_alternatives.png)
- [OpenScientist mechanistic causal chain](openscientist_artifacts/provenance_mechanistic_causal_chain.json)
![OpenScientist mechanistic causal chain](openscientist_artifacts/provenance_mechanistic_causal_chain.png)
- [OpenScientist plot 1](openscientist_artifacts/provenance_plot_1.json)
![OpenScientist plot 1](openscientist_artifacts/provenance_plot_1.png)
- [OpenScientist plot 2](openscientist_artifacts/provenance_plot_2.json)
![OpenScientist plot 2](openscientist_artifacts/provenance_plot_2.png)
- [OpenScientist plot 3](openscientist_artifacts/provenance_plot_3.json)
![OpenScientist plot 3](openscientist_artifacts/provenance_plot_3.png)
- [OpenScientist plot 4](openscientist_artifacts/provenance_plot_4.json)
![OpenScientist plot 4](openscientist_artifacts/provenance_plot_4.png)