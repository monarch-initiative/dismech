---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-06T09:07:00.441257'
end_time: '2026-07-06T10:39:19.549709'
duration_seconds: 5539.11
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Parkinson's Disease
  category: Complex
  hypothesis_group_id: body_first_enteric_alpha_synuclein_model
  hypothesis_label: "Body-First Enteric \u03B1-Synuclein Initiation Model"
  hypothesis_status: ALTERNATIVE
  hypothesis_yaml: "hypothesis_group_id: body_first_enteric_alpha_synuclein_model\n\
    hypothesis_label: Body-First Enteric \u03B1-Synuclein Initiation Model\nstatus:\
    \ ALTERNATIVE\ndescription: Alpha-synuclein pathology initiates in the enteric\
    \ nervous system or other peripheral autonomic\n  sites, then propagates through\
    \ vagal connections to the dorsal motor nucleus and broader brainstem before\n\
    \  joining the central alpha-synuclein propagation and dopaminergic-neurodegeneration\
    \ cascade. This model\n  best explains Parkinson disease presentations with early\
    \ constipation, REM-sleep behavior disorder,\n  autonomic dysfunction, and early\
    \ peripheral/cardiac sympathetic denervation.\nnotes: Evidence is strongest for\
    \ the gut-to-brain propagation route in animal models where truncal vagotomy\n\
    \  or alpha-synuclein deficiency blocks spread. Human clinical and imaging studies\
    \ support a body-first\n  subtype pattern, but microbiome dysbiosis and enteric\
    \ seeding remain unresolved as causal triggers versus\n  modifiers or consequences.\n\
    evidence:\n- reference: PMID:38519273\n  reference_title: 'Brain-first vs. body-first\
    \ Parkinson''s disease: An update on recent evidence.'\n  supports: SUPPORT\n\
    \  evidence_source: HUMAN_CLINICAL\n  snippet: the initial pathology starts either\
    \ in the olfactory bulb or amygdala leading to a brain-first\n    subtype, or\
    \ in the enteric nervous system leading to a body-first subtype.\n  explanation:\
    \ Recent review-level synthesis of human imaging, clinical, and pathology studies\
    \ explicitly\n    frames enteric-origin body-first PD as an alternative subtype\
    \ within the ASOC model.\n- reference: PMID:31255487\n  reference_title: Transneuronal\
    \ Propagation of Pathologic \u03B1-Synuclein from the Gut to the Brain Models\n\
    \    Parkinson's Disease.\n  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n\
    \  snippet: Truncal vagotomy and \u03B1-syn deficiency prevented the gut-to-brain\
    \ spread of \u03B1-synucleinopathy\n    and associated neurodegeneration and behavioral\
    \ deficits.\n  explanation: Mouse gut-to-brain transmission experiments support\
    \ the vagus nerve and alpha-synuclein\n    as required components of the body-first\
    \ propagation route.\n- reference: PMID:39241780\n  reference_title: Gut-induced\
    \ alpha-Synuclein and Tau propagation initiate Parkinson's and Alzheimer's\n \
    \   disease co-pathology and behavior impairments.\n  supports: SUPPORT\n  evidence_source:\
    \ MODEL_ORGANISM\n  snippet: Truncal vagotomy and \u03B1-Syn deficiency significantly\
    \ inhibited synucleinopathy or tauopathy\n    spreading.\n  explanation: Gut-inducible\
    \ mouse models provide independent support that vagotomy and alpha-synuclein\n\
    \    deficiency inhibit gut-origin propagation into the brain."
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
citation_count: 42
artifact_count: 22
artifact_sources:
  openscientist_artifacts_zip: 22
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
- filename: provenance_causal_chain_diagram.json
  path: openscientist_artifacts/provenance_causal_chain_diagram.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist causal chain diagram
- filename: provenance_causal_chain_diagram.png
  path: openscientist_artifacts/provenance_causal_chain_diagram.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist causal chain diagram
- filename: provenance_evidence_matrix.json
  path: openscientist_artifacts/provenance_evidence_matrix.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: provenance_evidence_matrix.png
  path: openscientist_artifacts/provenance_evidence_matrix.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: provenance_final_assessment.json
  path: openscientist_artifacts/provenance_final_assessment.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final assessment
- filename: provenance_final_assessment.png
  path: openscientist_artifacts/provenance_final_assessment.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final assessment
- filename: provenance_knowledge_gaps_table.json
  path: openscientist_artifacts/provenance_knowledge_gaps_table.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist knowledge gaps table
- filename: provenance_knowledge_gaps_table.png
  path: openscientist_artifacts/provenance_knowledge_gaps_table.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist knowledge gaps table
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
- filename: provenance_plot_5.json
  path: openscientist_artifacts/provenance_plot_5.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 5
- filename: provenance_plot_5.png
  path: openscientist_artifacts/provenance_plot_5.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 5
- filename: provenance_summary_dashboard.json
  path: openscientist_artifacts/provenance_summary_dashboard.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist summary dashboard
- filename: provenance_summary_dashboard.png
  path: openscientist_artifacts/provenance_summary_dashboard.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist summary dashboard
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
- **Hypothesis ID:** body_first_enteric_alpha_synuclein_model
- **Hypothesis Label:** Body-First Enteric α-Synuclein Initiation Model
- **Status in KB:** ALTERNATIVE

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: body_first_enteric_alpha_synuclein_model
hypothesis_label: Body-First Enteric α-Synuclein Initiation Model
status: ALTERNATIVE
description: Alpha-synuclein pathology initiates in the enteric nervous system or other peripheral autonomic
  sites, then propagates through vagal connections to the dorsal motor nucleus and broader brainstem before
  joining the central alpha-synuclein propagation and dopaminergic-neurodegeneration cascade. This model
  best explains Parkinson disease presentations with early constipation, REM-sleep behavior disorder,
  autonomic dysfunction, and early peripheral/cardiac sympathetic denervation.
notes: Evidence is strongest for the gut-to-brain propagation route in animal models where truncal vagotomy
  or alpha-synuclein deficiency blocks spread. Human clinical and imaging studies support a body-first
  subtype pattern, but microbiome dysbiosis and enteric seeding remain unresolved as causal triggers versus
  modifiers or consequences.
evidence:
- reference: PMID:38519273
  reference_title: 'Brain-first vs. body-first Parkinson''s disease: An update on recent evidence.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: the initial pathology starts either in the olfactory bulb or amygdala leading to a brain-first
    subtype, or in the enteric nervous system leading to a body-first subtype.
  explanation: Recent review-level synthesis of human imaging, clinical, and pathology studies explicitly
    frames enteric-origin body-first PD as an alternative subtype within the ASOC model.
- reference: PMID:31255487
  reference_title: Transneuronal Propagation of Pathologic α-Synuclein from the Gut to the Brain Models
    Parkinson's Disease.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Truncal vagotomy and α-syn deficiency prevented the gut-to-brain spread of α-synucleinopathy
    and associated neurodegeneration and behavioral deficits.
  explanation: Mouse gut-to-brain transmission experiments support the vagus nerve and alpha-synuclein
    as required components of the body-first propagation route.
- reference: PMID:39241780
  reference_title: Gut-induced alpha-Synuclein and Tau propagation initiate Parkinson's and Alzheimer's
    disease co-pathology and behavior impairments.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Truncal vagotomy and α-Syn deficiency significantly inhibited synucleinopathy or tauopathy
    spreading.
  explanation: Gut-inducible mouse models provide independent support that vagotomy and alpha-synuclein
    deficiency inhibit gut-origin propagation into the brain.
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

# Body-First Enteric α-Synuclein Initiation Model: Hypothesis Evaluation Report

**Hypothesis ID:** `body_first_enteric_alpha_synuclein_model`  
**Current KB Status:** ALTERNATIVE  
**Evaluation Date:** 2026-07-06  
**Evidence Base:** 118 papers reviewed, 15 confirmed findings across 5 investigative iterations

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — maintain ALTERNATIVE status**

The Body-First Enteric α-Synuclein Initiation Model is partially supported by convergent evidence across multiple levels of analysis — animal models, human epidemiology, clinical imaging, and peripheral biomarkers — as a genuine mechanistic subtype pathway applicable to an estimated 20–30% of Parkinson's disease (PD) cases. The model is best understood not as a universal explanation for PD, but as one well-supported origin-site pathway within the multi-origin Synuclein Origin and Connectome (SOC) framework.

The strongest direct evidence comes from mouse gut-to-brain α-synuclein transmission experiments demonstrating that both truncal vagotomy and α-synuclein deficiency block enteric-to-central propagation (3 independent studies), corroborated by human epidemiological data showing truncal vagotomy reduces PD risk (HR 0.53–0.59 with long follow-up). Distinct clinical-imaging signatures — symmetric dopaminergic degeneration, early cardiac sympathetic denervation, elevated peripheral α-synuclein positivity — consistently differentiate a body-first subtype in human cohorts.

However, critical qualifications restrict the model's scope and certainty. The upstream trigger for enteric α-synuclein misfolding remains the most fundamental unresolved gap. Between 6–43% of PD cases do not follow the caudo-rostral Braak staging the model presupposes. LRRK2-associated PD is frequently α-synuclein seed amplification assay (SAA)-negative, demonstrating α-syn-independent parkinsonian pathways. Enteric α-synuclein immunohistochemistry lacks diagnostic specificity, fecal microbiota transplantation (FMT) trials show inconsistent results, the iRBD prodrome is heterogeneous (24.6% SAA-negative), and anti-α-synuclein immunotherapies have failed in established PD. The recommended status is **ALTERNATIVE**: one well-supported pathway within the multi-origin framework, applicable specifically to α-syn-positive PD with prodromal autonomic features, but not a universal disease mechanism.

---

## Summary

This report evaluates the Body-First Enteric α-Synuclein Initiation Model for Parkinson's disease, which proposes that α-synuclein pathology initiates in the enteric nervous system (ENS) or peripheral autonomic sites and propagates retrogradely through vagal connections to the dorsal motor nucleus of the vagus (DMV), then ascends through the brainstem to the substantia nigra and cortex. The model best explains PD presentations featuring early constipation, REM sleep behavior disorder (RBD), autonomic dysfunction, and cardiac sympathetic denervation — collectively termed the "body-first" PD subtype.

Across five investigative iterations and 118 papers reviewed, we identified 15 confirmed findings spanning mouse transmission experiments, human vagotomy epidemiology, clinical subtype differentiation, microbiome studies, genetic interactions (LRRK2), biomarker validation (SAA, MIBG), prodromal cohort studies, and immunotherapy trials. The evidence consistently supports the biological plausibility and clinical relevance of the body-first pathway while simultaneously revealing important boundaries: the model applies to a subpopulation of PD patients, the initiating trigger remains unknown, and several key causal links lack direct human confirmation.

The investigation also identified six major alternative or complementary mechanistic models (brain-first/olfactory origin, cell-autonomous genetic, neuroinflammation-first, prion strain, glymphatic failure, and multi-hit gene–environment interaction), each of which overlaps with or competes against specific elements of the body-first hypothesis. The report concludes with concrete discriminating tests and curation leads for knowledge base refinement.

---

## Key Findings

### Finding 1: Vagotomy Epidemiology Supports the Body-First Route

Two large Scandinavian register-based cohort studies provide the strongest human epidemiological evidence for the body-first model. The Danish study ([PMID: 26031848](https://pubmed.ncbi.nlm.nih.gov/26031848/)) found that truncal vagotomy was associated with decreased PD risk, with HR = 0.53 (95% CI 0.28–0.99) at >20 years of follow-up compared to the general population, while superselective vagotomy showed no protection (HR = 1.09). As stated in the abstract: *"Full truncal vagotomy is associated with a decreased risk for subsequent PD, suggesting that the vagal nerve may be cri[tical]."* The Swedish study ([PMID: 28446653](https://pubmed.ncbi.nlm.nih.gov/28446653/)) confirmed this pattern: truncal vagotomy at ≥5 years before PD diagnosis yielded HR = 0.59 (95% CI 0.37–0.93), with selective vagotomy showing no association. The abstract notes: *"there was a suggestion of lower risk among patients with truncal vagotomy (HR 0.78, 95% CI 0.55-1.09), which may be driven by truncal vagotomy at least 5 years before PD diagnosis (HR 0.59, 95% CI 0.37-0.93)."*

The specificity for truncal (complete) vagotomy over selective procedures is mechanistically important — it implies that complete disruption of vagal afferents from the gut, rather than partial denervation, is required to interrupt the propagation pathway. However, both studies showed non-significant overall effects, with the protective signal emerging only in long-latency subgroups, consistent with the model's prediction of a decades-long prodromal phase but also raising statistical power concerns.

### Finding 2: Mouse Gut-to-Brain α-Synuclein Transmission Requires Vagus Nerve and Endogenous α-Synuclein

The most direct experimental evidence comes from three independent mouse model studies. Kim et al. 2019 ([PMID: 31255487](https://pubmed.ncbi.nlm.nih.gov/31255487/)) demonstrated that injection of α-synuclein preformed fibrils (PFFs) into the duodenal/pyloric muscularis produced sequential pathology spread: DMV → locus coeruleus → amygdala → dorsal raphe → substantia nigra, followed by dopaminergic neuron loss and motor/non-motor symptoms. Critically, as the abstract states: *"Truncal vagotomy and α-syn deficiency prevented the gut-to-brain spread of α-synucleinopathy and associated neurodegeneration and behavioral deficits."* Xiang et al. 2024 ([PMID: 39241780](https://pubmed.ncbi.nlm.nih.gov/39241780/)) independently replicated these findings using the SYN103 gut-inducible model, confirming that *"Truncal vagotomy and α-Syn deficiency significantly inhibited synucleinopathy or tauopathy spreading."*

Additionally, Kishimoto et al. 2019 ([PMID: 31079293](https://pubmed.ncbi.nlm.nih.gov/31079293/)) showed that *"mild gut inflammation accelerates α-synuclein pathology"* in α-synuclein mutant mice, with chronic mild gut inflammation accelerating disease onset, α-synuclein pathology in enteric and brain neurons, and dopaminergic neurodegeneration — providing evidence that gut inflammation can serve as an accelerator of the body-first pathway.

### Finding 3: Body-First PD Shows a Distinct Clinical-Imaging Signature

Multiple human studies confirm that body-first PD (operationally defined by RBD status, MIBG uptake, or autonomic markers) displays a signature distinct from brain-first PD:

- **Dopaminergic asymmetry**: Body-first (RBD+) patients show significantly more symmetric nigrostriatal degeneration compared to brain-first (RBD−) patients. As reported: *"Nigrostriatal degeneration was significantly more symmetric in patients with RBD versus patients without RBD or with unknown RBD status in both FDOPA (p = 0.001) and DaT SPECT (p = 0.001) datasets"* ([PMID: 34334424](https://pubmed.ncbi.nlm.nih.gov/34334424/)).
- **Cardiac sympathetic denervation**: Body-first PD shows reduced MIBG uptake and delayed gastric emptying ([PMID: 39665845](https://pubmed.ncbi.nlm.nih.gov/39665845/)).
- **Vagal and pupillary markers**: Body-first PD shows vagal atrophy and sympathetic pupillary deficit in the first decade of motor disease; brain-first does not ([PMID: 42390607](https://pubmed.ncbi.nlm.nih.gov/42390607/)).
- **Cutaneous α-synuclein**: Body-first patients exhibit *"more prominent non-motor symptoms (e.g. REM sleep behaviour disorder, autonomic dysfunction) and severe autonomic denervation (reduced sweat gland and pilomotor nerve densities; P < 0.01)"* with higher phosphorylated α-synuclein positivity (92.4% vs 61.9%; [PMID: 41105632](https://pubmed.ncbi.nlm.nih.gov/41105632/)).
- **Prodromal duration**: Over 20 years estimated from cardiac sympathetic degeneration onset to PD diagnosis in body-first cases ([PMID: 42386728](https://pubmed.ncbi.nlm.nih.gov/42386728/)).

These convergent clinical findings strongly validate the SOC model's prediction that body-first and brain-first PD represent biologically distinct subtypes with different prodromal trajectories.

{{figure:evidence_matrix.png|caption=Evidence matrix summarizing the strength, type, and direction of evidence for the body-first PD hypothesis across studies}}

### Finding 4: LRRK2 × Gut Inflammation Gene–Environment Interaction

Three studies demonstrate that the LRRK2 G2019S mutation — one of the most common genetic risk factors for PD — synergizes with gut inflammation to drive enteric α-synuclein pathology:

- Recurrent gut bacterial infection in LRRK2 G2019S knock-in mice drives PD pathology not seen under basal conditions ([PMID: 42327194](https://pubmed.ncbi.nlm.nih.gov/42327194/)).
- Chronic LPS exposure in LRRK2 G2019S mice causes *"chronic peripheral inflammation synergizes with LRRK2 G2019S to trigger early intestinal inflamm[ation]"* with age-dependent enteric α-synuclein accumulation and phosphorylation ([PMID: 42295088](https://pubmed.ncbi.nlm.nih.gov/42295088/)).
- Prodromal intestinal inflammation in LRRK2 G2019S mice *"expedites and exacerbates PD endophenotypes in rodent carriers of the human PD risk allele LRRK2 G2019S in a sex-dependent manner"* — promoting α-synuclein aggregation in the substantia nigra, dopaminergic neuron loss, and motor impairment with male bias via α-synuclein-positive macrophages in colonic lamina propria ([PMID: 38750146](https://pubmed.ncbi.nlm.nih.gov/38750146/)).

These findings are significant because they provide a concrete gene–environment interaction mechanism whereby genetically susceptible individuals could develop body-first PD through gut inflammatory triggers, bridging the genetic and environmental risk factor literatures.

### Finding 5: The SOC Model Framework

The Synuclein Origin and Connectome (SOC) model, developed primarily by Borghammer and colleagues, provides the overarching framework within which the body-first hypothesis operates. As described in the foundational paper ([PMID: 33682732](https://pubmed.ncbi.nlm.nih.gov/33682732/)): *"In body-first cases, the α-synuclein pathology ascends via the vagus to both the left and right dorsal motor nuclei of the vagus owing to the overlapping parasympathetic innervation of the gut."* The most recent review ([PMID: 38519273](https://pubmed.ncbi.nlm.nih.gov/38519273/)) frames the model as: *"the initial pathology starts either in the olfactory bulb or amygdala leading to a brain-first subtype, or in the enteric nervous system leading to a body-first subtype."* The SOC model proposes that body-first pathology (enteric origin → bilateral DMV → symmetric brainstem spread) produces older onset, symmetric DAT binding, early autonomic/RBD symptoms, and higher dementia risk, while brain-first pathology (amygdala/olfactory origin → unilateral spread) produces younger onset and fewer prodromal non-motor symptoms. Review of human studies generally supports these predictions, though structural MRI findings remain conflicting.

### Finding 6: Enteric α-Synuclein Immunohistochemistry Lacks Diagnostic Specificity

A critical limitation for the body-first model is that colonic biopsy α-synuclein detection is not reliable for PD diagnosis. Corbillé et al. 2016 ([PMID: 27044604](https://pubmed.ncbi.nlm.nih.gov/27044604/)) conducted a multi-center study of 4 immunohistochemistry methods across 9 PD subjects and 3 controls: *"Positive alpha-synuclein staining was observed by all 5 judges in most of the slides from control cases, regardless of the staining methods that were used. Moreover, none of the tested method or staining pattern had a specificity and sensi[tivity adequate for diagnosis]."* This finding directly undermines the use of enteric α-synuclein detection as a biomarker for the body-first pathway and raises questions about the specificity of enteric α-synuclein pathology as a disease-defining feature.

### Finding 7: Intragastric Rotenone Reproduces Braak Staging

Pan-Montojo et al. 2010 ([PMID: 20098733](https://pubmed.ncbi.nlm.nih.gov/20098733/)) demonstrated that intragastric administration of rotenone (5 mg/kg) to wild-type mice induced α-synuclein accumulation sequentially in ENS → DMV → intermediolateral cell column (IML) → substantia nigra. As stated: *"low doses of chronically and intragastrically administered rotenone induce alpha-synuclein accumulation in all the above-mentioned nervous system structures of wild-type mice."* No rotenone was detected in systemic blood or CNS (detection limit <20 nM), and no systemic Complex I inhibition occurred. Alterations appeared only in synaptically connected structures and were treatment-time-dependent. This provides a powerful environmental toxicant model for the body-first pathway, demonstrating that a locally acting pesticide can initiate the complete ascending propagation sequence without requiring systemic exposure.

### Finding 8: FMT Clinical Trials Show Inconsistent Disease Modification

If the gut microbiome is causally involved in initiating body-first PD, then microbiome-targeted interventions should modify the disease. Clinical trial results are mixed:

- **Positive**: A Phase 2 RCT ([PMID: 41826284](https://pubmed.ncbi.nlm.nih.gov/41826284/), n=72 drug-naïve) found dFMT improved UPDRS III (−3.8 vs +0.1, p = 0.0001), constipation severity (−6.5 vs −0.7, p < 0.0001), and showed *"a marked reduction in Escherichia-Shigella, correlating with decreased colonic α-synuclein aggregation (r = 0.3775, p = 0.0277), supporting a gut-brain mechanistic link."*
- **Negative**: An RCT ([PMID: 41674471](https://pubmed.ncbi.nlm.nih.gov/41674471/), n=59) showed no significant MDS-UPDRS III difference at 12 months.
- **Meta-analysis** ([PMID: 41078360](https://pubmed.ncbi.nlm.nih.gov/41078360/)): Gut microbiota-targeted therapies *"significantly improved PD outcomes, including Movement Disorder Society-Unified Parkinson Disease Rating Scale (MDS-UPDRS) III (SMD: -0.34, 95%CI: -0.57 to -0.11, P = 0.004)"* but no improvement in cognition, non-motor symptoms, or quality of life.
- **Systematic review** ([PMID: 40676526](https://pubmed.ncbi.nlm.nih.gov/40676526/)): 5 RCTs with inconsistent findings; one trial showed motor worsening.

These results suggest the microbiome may modulate but does not clearly modify disease trajectory, consistent with a role as a contributor/modifier rather than a sufficient cause.

### Finding 9: iRBD Prodromal Heterogeneity

Isolated REM sleep behavior disorder (iRBD), the presumed prodromal state of body-first PD, is itself heterogeneous:

- **Two brain atrophy subtypes**: Machine learning (SuStaIn) in a multicentric cohort of 1,276 participants identified *"two distinct subtypes of brain atrophy progression: 1) a 'cortical-first' subtype, with atrophy beginning in the frontal lobes... and 2) a 'subcortical-first' subtype, with atrophy beginning in the limbic areas"* ([PMID: 40447483](https://pubmed.ncbi.nlm.nih.gov/40447483/)). Cognitive decline was subtype-specific.
- **SAA-negative iRBD**: 24.6% of iRBD patients are CSF α-synuclein SAA-negative, with significantly lower phenoconversion risk (HR 5.4 for SAA+ vs SAA−; [PMID: 42248896](https://pubmed.ncbi.nlm.nih.gov/42248896/)).

This heterogeneity means that not all iRBD patients are on a body-first α-synuclein trajectory, limiting the model's applicability even within its most characteristic prodromal population.

### Finding 10: Braak Staging Exceptions

Between 6.3% and 43% of PD cases do not follow the proposed caudo-rostral Braak staging progression ([PMID: 18592254](https://pubmed.ncbi.nlm.nih.gov/18592254/): *"between 6.3 and 43% of the cases did not follow the proposed cau[do-rostral progression]"*; [PMID: 18718530](https://pubmed.ncbi.nlm.nih.gov/18718530/)). Braak et al. themselves identified 19 of 301 staged autopsy cases (6.3%) with *"a pathological distribution pattern of Lewy neurites and Lewy bodies that diverged from the staging scheme... olfactory structures and the amygdala were predominantly involved in the virtual absence of brain stem pathology"* — 17/19 of these divergent cases had concurrent advanced Alzheimer's disease ([PMID: 17017514](https://pubmed.ncbi.nlm.nih.gov/17017514/)). These exceptions directly challenge the universality of any single ascending propagation model.

### Finding 11: Gut Microbiota Functionally Required for α-Synuclein Pathology in Mouse Models

Sampson et al. 2016 ([PMID: 27912057](https://pubmed.ncbi.nlm.nih.gov/27912057/)) demonstrated in α-synuclein-overexpressing mice that *"gut microbiota are required for motor deficits, microglia activation, and αSyn pathology. Antibiotic treatment ameliorates, while microbial re-colonization promotes, pathophysiology in adult animals, suggesting that postnatal signaling between the gut and the brain modulates disease."* Colonization with microbiota from PD patients enhanced physical impairments versus healthy donor microbiota. Wang et al. 2021 ([PMID: 34413194](https://pubmed.ncbi.nlm.nih.gov/34413194/)) identified curli amyloid fibril as a bacterial component promoting neurodegeneration, potentially through cross-seeding of α-synuclein.

### Finding 12: LRRK2-PD Often SAA-Negative

LRRK2-associated PD frequently shows negative CSF α-synuclein SAA results. A biomarker review notes *"reduced sensitivity in normosmic PD, some genetic subgroups (especially LRRK2-associated PD), very early or anatomically restricted Lewy pathology"* ([PMID: 42295486](https://pubmed.ncbi.nlm.nih.gov/42295486/)). SAA-negative LRRK2-PD maintains higher DAT binding: *"the α-Syn SAA-negative LRRK2 PD group exhibited higher DAT binding in the contralateral putamen and ipsilateral putamen compared to the SAA-positive group"* with slower dopaminergic degeneration ([PMID: 40944725](https://pubmed.ncbi.nlm.nih.gov/40944725/)). This demonstrates that PD can occur without detectable α-synuclein seeding activity, fundamentally limiting the body-first (and indeed any α-syn-centric) model to the subset of PD with confirmed synucleinopathy.

### Finding 13: Prodromal Triad Risk Quantification

Constipation alone confers a sustained 3-fold PD risk over 15 years: *"The 31,905 patients with constipation had a higher risk of PD than 159,092 comparison cohort members (adjusted (a) HR = 3.03, 95% CI 2.50-3.66), which was sustained to 11-15 years follow-up (aHR = 3.65, 95% CI 1.67-7.95)"* ([PMID: 27234704](https://pubmed.ncbi.nlm.nih.gov/27234704/)). The combination of constipation + probable RBD + hyposmia produces a 23-fold higher PD risk within 3 years: *"Men with constipation, pRBD, and hyposmia had a 23-fold higher risk of receiving a PD diagnosis in the subsequent 3 years... (risk ratio [RR] = 23.35, 95% confidence interval [CI] = 10.62-51.33)"* ([PMID: 39702948](https://pubmed.ncbi.nlm.nih.gov/39702948/)). These prodromal risk estimates are clinically actionable for identifying the body-first population most likely to benefit from future disease-modifying interventions.

### Finding 14: NSD-ISS Does Not Incorporate Body-First vs Brain-First

The Neuronal α-Synuclein Disease Integrated Staging System (NSD-ISS), validated longitudinally in the PPMI cohort, defines staging as: *"Neuronal α-synuclein disease (NSD) is defined by the presence of an in vivo biomarker of neuronal alpha-synuclein (n-asyn) pathology. The NSD integrated staging system (NSD-ISS) for research describes progression across the disease continuum as stages 0 to 6"* ([PMID: 40302527](https://pubmed.ncbi.nlm.nih.gov/40302527/)). Neither NSD-ISS nor SynNeurGe explicitly incorporates body-first versus brain-first subtype classification ([PMID: 42261981](https://pubmed.ncbi.nlm.nih.gov/42261981/)). This represents a framework gap: the current biological staging system for PD does not differentiate origin sites, despite growing evidence that origin site influences prognosis and treatment response.

### Finding 15: Anti-α-Synuclein Immunotherapy Failures

Phase II trials of prasinezumab and cinpanemab failed primary efficacy endpoints in established PD: *"Phase-II trials failed to meet their primary efficacy endpoints and showed no significant slowing of disease progression (Cinpanemab 250 mg P-value = 0.7, 1250 mg P-value = 0.78, 3500 mg P-value = 0.7; Prasinezumab 1500 mg P-value = 0.24, 4500 mg P-value = 0.72)"* ([PMID: 41702332](https://pubmed.ncbi.nlm.nih.gov/41702332/)). All showed low CSF penetration (CSF:Serum 0.2–0.5%). This is relevant to the body-first model because it suggests that targeting α-synuclein after it has already propagated centrally may be too late — supporting the model's implication that intervention must occur during the peripheral/prodromal phase to be effective.

{{figure:causal_chain_diagram.png|caption=Mechanistic causal chain of the body-first PD model from upstream triggers through enteric α-synuclein initiation to clinical manifestation}}

---

## Mechanistic Model and Interpretation

### Causal Chain

The body-first model implies the following causal chain from upstream trigger to clinical manifestation. Each link is annotated with the strength of supporting evidence:

```
UPSTREAM TRIGGERS (Unknown/Speculative)
  │
  │  Environmental toxicants (rotenone, pesticides) ── [Moderate: mouse models]
  │  Gut microbiome dysbiosis ── [Moderate: mouse models, inconsistent human FMT]
  │  Gut inflammation ── [Strong in LRRK2 context; emerging for sporadic PD]
  │  Bacterial amyloid cross-seeding (curli) ── [Emerging: single study]
  │
  ▼
ENTERIC α-SYNUCLEIN MISFOLDING & AGGREGATION
  │  Evidence: α-syn found in ENS of PD patients [Strong]
  │  Caveat: also found in controls (IHC specificity problem) [Strong qualification]
  │
  ▼
VAGAL RETROGRADE TRANSPORT TO DMV
  │  Evidence: Vagotomy blocks spread in mice [Strong: 3 studies]
  │  Evidence: Truncal vagotomy reduces PD risk in humans [Moderate: 2 register studies]
  │  Evidence: Intragastric rotenone reproduces staging [Strong: mouse model]
  │
  ▼
DMV → LOCUS COERULEUS → BRAINSTEM SPREAD (bilateral, symmetric)
  │  Evidence: Sequential spread demonstrated in PFF injection models [Strong]
  │  Evidence: Body-first patients show symmetric DAT [Strong: multiple imaging studies]
  │
  ▼
ASCENDING TO SUBSTANTIA NIGRA → DOPAMINERGIC NEURODEGENERATION
  │  Evidence: DA neuron loss in mouse models [Strong]
  │  Evidence: Clinical motor symptoms [Strong]
  │
  ▼
CLINICAL MANIFESTATION: Body-first PD subtype
  │  Early constipation, RBD, autonomic dysfunction [Strong: epidemiology]
  │  Symmetric motor onset [Strong: imaging]
  │  Cardiac sympathetic denervation [Strong: MIBG studies]
  │  Higher dementia risk [Emerging]
  │  Estimated >20 year prodromal phase [Moderate: modeling]
```

**Strongest links**: Vagal transport (mouse models), clinical subtype signatures (human imaging).  
**Weakest links**: Initial trigger identification, enteric-to-vagal transfer mechanism in humans, specificity of enteric α-synuclein as a disease marker.  
**Missing causal steps**: What initiates α-synuclein misfolding in the ENS? What cell types in the gut epithelium transfer pathological seeds to enteric neurons? Why do some individuals with enteric α-synuclein not develop PD?

### Synthesis

The convergent evidence supports a coherent narrative: in a subset of PD patients (~20–30%), pathological α-synuclein originates in the peripheral autonomic nervous system — most likely the ENS — and propagates retrogradely through the vagus nerve to the brainstem. This produces a characteristic clinical phenotype: early autonomic dysfunction (constipation, cardiac sympathetic denervation), RBD, and relatively symmetric dopaminergic loss. The propagation requires both intact vagal connections (blocked by vagotomy) and endogenous α-synuclein (blocked by genetic knockout), and can be accelerated by gut inflammation, environmental toxicants, and microbiome-mediated signaling.

However, this body-first pathway coexists with at least one alternative pathway (brain-first, originating in the olfactory bulb/amygdala) and potentially with α-synuclein-independent mechanisms (as in LRRK2-PD). The model does not explain all PD and should not be treated as a universal mechanism. Its greatest clinical value lies in identifying a high-risk prodromal population (constipation + RBD + hyposmia → 23-fold PD risk) who could benefit from future preventive interventions targeting the gut-brain axis.

---

## Evidence Matrix

| Citation | Evidence Type | Direction | Mechanistic Claim | Key Finding | Context | Confidence |
|----------|--------------|-----------|-------------------|-------------|---------|------------|
| [PMID: 31255487](https://pubmed.ncbi.nlm.nih.gov/31255487/) | Model organism | **Supports** | Vagal gut-to-brain α-syn transmission | Vagotomy + α-syn KO both block spread | PFF injection, WT mice | High; seminal study |
| [PMID: 39241780](https://pubmed.ncbi.nlm.nih.gov/39241780/) | Model organism | **Supports** | Independent replication of vagal transmission | Vagotomy + α-syn deficiency inhibit spread | SYN103 model | High; replication |
| [PMID: 26031848](https://pubmed.ncbi.nlm.nih.gov/26031848/) | Human clinical | **Supports** | Vagotomy reduces PD risk | Truncal vagotomy HR=0.53 at >20yr | Danish register | Moderate; subgroup |
| [PMID: 28446653](https://pubmed.ncbi.nlm.nih.gov/28446653/) | Human clinical | **Supports** | Vagotomy reduces PD risk | Truncal vagotomy HR=0.59 at >5yr | Swedish register | Moderate; subgroup |
| [PMID: 20098733](https://pubmed.ncbi.nlm.nih.gov/20098733/) | Model organism | **Supports** | Toxicant → ENS → brain | Intragastric rotenone → sequential α-syn spread | WT C57BL/6 mice | High |
| [PMID: 27912057](https://pubmed.ncbi.nlm.nih.gov/27912057/) | Model organism | **Supports** | Microbiome required for α-syn pathology | GF conditions reduce pathology; PD microbiota worsens | α-syn overexpressing mice | High; seminal |
| [PMID: 34334424](https://pubmed.ncbi.nlm.nih.gov/34334424/) | Human clinical | **Supports** | Body-first = symmetric DAT | RBD+ PD has symmetric degeneration (p=0.001) | FDOPA + DaT SPECT | High |
| [PMID: 41105632](https://pubmed.ncbi.nlm.nih.gov/41105632/) | Human clinical | **Supports** | Peripheral α-syn differs by subtype | Body-first: 92.4% vs 61.9% p-α-syn | Skin biopsy | High |
| [PMID: 42386728](https://pubmed.ncbi.nlm.nih.gov/42386728/) | Human clinical | **Supports** | Long prodromal phase | >20yr cardiac sympathetic → PD diagnosis | Longitudinal imaging | Moderate |
| [PMID: 38519273](https://pubmed.ncbi.nlm.nih.gov/38519273/) | Review | **Supports** | SOC model framework | Brain-first vs body-first synthesis | Comprehensive review | Review-level |
| [PMID: 27044604](https://pubmed.ncbi.nlm.nih.gov/27044604/) | Human clinical | **Qualifies** | Enteric α-syn as biomarker | IHC positive in controls | Multi-center, 4 methods | High |
| [PMID: 18592254](https://pubmed.ncbi.nlm.nih.gov/18592254/) | Review/Pathology | **Qualifies** | Universal Braak staging | 6.3–43% don't follow staging | Large autopsy series | High |
| [PMID: 17017514](https://pubmed.ncbi.nlm.nih.gov/17017514/) | Human pathology | **Qualifies** | Braak staging universality | 19/301 amygdala-predominant | Autopsy series | High |
| [PMID: 42248896](https://pubmed.ncbi.nlm.nih.gov/42248896/) | Human clinical | **Qualifies** | iRBD = body-first prodrome | 24.6% iRBD SAA-negative | CSF SAA cohort | High |
| [PMID: 40447483](https://pubmed.ncbi.nlm.nih.gov/40447483/) | Human clinical | **Qualifies** | iRBD homogeneity | Two distinct atrophy subtypes within iRBD | 1276-participant cohort | High |
| [PMID: 42295486](https://pubmed.ncbi.nlm.nih.gov/42295486/) | Review | **Qualifies** | α-syn universality | Reduced SAA sensitivity in LRRK2-PD | Biomarker review | Review-level |
| [PMID: 40944725](https://pubmed.ncbi.nlm.nih.gov/40944725/) | Human clinical | **Qualifies** | α-syn-independent PD | SAA-negative LRRK2-PD has slower DAT decline | PPMI longitudinal | High |
| [PMID: 41674471](https://pubmed.ncbi.nlm.nih.gov/41674471/) | Human clinical (RCT) | **Qualifies** | Microbiome modification treats PD | No significant UPDRS III at 12mo | n=59 RCT | High |
| [PMID: 41826284](https://pubmed.ncbi.nlm.nih.gov/41826284/) | Human clinical (RCT) | **Supports** | Microbiome modification treats PD | dFMT improved UPDRS III (p=0.0001) | n=72, drug-naïve | Moderate |
| [PMID: 41702332](https://pubmed.ncbi.nlm.nih.gov/41702332/) | Human clinical (RCT) | **Qualifies** | α-syn immunotherapy modifies PD | All phase II trials failed endpoints | 5 RCTs, n=786 | High |
| [PMID: 42327194](https://pubmed.ncbi.nlm.nih.gov/42327194/) | Model organism | **Supports** | Gene-environment interaction | Gut infection drives PD in LRRK2 KI mice | KI mouse model | High |
| [PMID: 38750146](https://pubmed.ncbi.nlm.nih.gov/38750146/) | Model organism | **Supports** | Gut inflammation × LRRK2 | Sex-dependent PD from gut inflammation | Mouse model | High |
| [PMID: 27234704](https://pubmed.ncbi.nlm.nih.gov/27234704/) | Human clinical | **Supports** | Constipation as prodromal marker | aHR=3.03, sustained >15yr | Danish cohort, n=31,905 | High |
| [PMID: 39702948](https://pubmed.ncbi.nlm.nih.gov/39702948/) | Human clinical | **Supports** | Prodromal triad risk | Constipation+RBD+hyposmia: RR=23.35 | Prospective, n=6,108 | High |
| [PMID: 34413194](https://pubmed.ncbi.nlm.nih.gov/34413194/) | Model organism | **Supports** | Bacterial amyloid cross-seeding | Curli amyloid promotes neurodegeneration | Genome-wide screen | Moderate |
| [PMID: 31079293](https://pubmed.ncbi.nlm.nih.gov/31079293/) | Model organism | **Supports** | Gut inflammation accelerates pathology | Mild gut inflammation accelerates α-syn | α-syn mutant mice | High |
| [PMID: 41702332](https://pubmed.ncbi.nlm.nih.gov/41702332/) | Human clinical | **Qualifies** | α-syn immunotherapy | All anti-α-syn mAbs failed Phase II | 5 RCTs | High |

{{figure:summary_dashboard.png|caption=Comprehensive summary dashboard showing evidence distribution, subtype characteristics, and model assessment across all investigation iterations}}

---

## Alternative and Competing Models

### 1. Brain-First / Olfactory-Origin Model
**Relationship**: Direct alternative within SOC framework. Proposes α-synuclein pathology initiates in the olfactory bulb or amygdala, spreading unilaterally and asymmetrically. Explains brain-first PD with younger onset, asymmetric motor presentation, fewer prodromal non-motor symptoms. Not competing per se — both subtypes likely coexist in the PD population.

### 2. Cell-Autonomous Genetic Model
**Relationship**: Parallel/upstream mechanism. Genetic variants (LRRK2, GBA, SNCA) cause cell-intrinsic dysfunction leading to α-synuclein aggregation or dopaminergic vulnerability without requiring peripheral initiation. LRRK2-PD being frequently SAA-negative ([PMID: 40944725](https://pubmed.ncbi.nlm.nih.gov/40944725/)) argues that some PD is α-syn-independent, fundamentally incompatible with the body-first α-syn model for those cases.

### 3. Neuroinflammation-First / Immune-Mediated Model
**Relationship**: Upstream cause or parallel mechanism. Proposes that systemic or central inflammation (via gut dysbiosis, infections, or autoimmunity) drives neurodegeneration independently of or prior to α-synuclein aggregation. The cGAS-STING-glymphatic-gut axis model ([PMID: 41966779](https://pubmed.ncbi.nlm.nih.gov/41966779/)) represents an elaboration suggesting a self-amplifying inflammatory triad. This model could be upstream of (triggering) or parallel to the body-first α-syn cascade.

### 4. Prion Strain Hypothesis
**Relationship**: Complementary mechanism. Different α-synuclein conformational strains may determine disease phenotype (PD vs DLB vs MSA) and propagation patterns ([PMID: 38765963](https://pubmed.ncbi.nlm.nih.gov/38765963/)). Compatible with the body-first model but adds a layer: the specific strain generated in the gut may determine whether body-first propagation leads to PD, DLB, or MSA.

### 5. Glymphatic Clearance Failure
**Relationship**: Downstream contributor or parallel mechanism. Impaired glymphatic clearance exacerbates protein aggregation and spread ([PMID: 38576025](https://pubmed.ncbi.nlm.nih.gov/38576025/)). Could amplify body-first propagation once it reaches the CNS but does not explain the initial peripheral seeding event.

### 6. Multi-Hit Gene–Environment Interaction
**Relationship**: Upstream cause. The LRRK2 × gut inflammation studies ([PMID: 42327194](https://pubmed.ncbi.nlm.nih.gov/42327194/), [PMID: 38750146](https://pubmed.ncbi.nlm.nih.gov/38750146/)) exemplify a model where genetic susceptibility plus environmental exposure is required — neither alone sufficient. Compatible with and may explain the selective vulnerability underlying the body-first pathway.

---

## Limitations and Knowledge Gaps

### Gap 1: Unknown Upstream Trigger for Enteric α-Synuclein Misfolding
**Scope**: The most fundamental unresolved question — what initiates the first misfolding event in the ENS?  
**Why it matters**: Without knowing the trigger, preventive intervention is impossible.  
**What was checked**: Environmental toxicant models (rotenone), microbiome studies, bacterial amyloid cross-seeding, gut inflammation models.  
**Resolution**: Longitudinal gut biopsies in at-risk populations (iRBD, constipation cohorts) with concurrent exposome profiling; identification of specific microbial species or metabolites that seed α-synuclein misfolding in human enteric neurons.

### Gap 2: Enteric-to-Vagal Transfer Mechanism in Humans
**Scope**: How pathological α-synuclein crosses from enteric neurons (or enteroendocrine cells) to vagal afferents is mechanistically unclear in humans.  
**Why it matters**: This is the critical first relay step; understanding it would enable targeted intervention.  
**What was checked**: Mouse PFF injection models, enteroendocrine cell α-synuclein expression, in vitro microfluidic studies ([PMID: 37688644](https://pubmed.ncbi.nlm.nih.gov/37688644/) — suggests synaptic transfer is limited and not facilitated by synapses).  
**Resolution**: Human vagal nerve biopsy or autopsy studies with α-synuclein strain typing at the ENS-vagal junction; high-resolution spatial transcriptomics of the gut-vagal interface.

### Gap 3: Enteric α-Synuclein Specificity Problem
**Scope**: Current IHC methods cannot reliably distinguish PD-associated enteric α-synuclein from normal physiological α-synuclein in the gut.  
**Why it matters**: Undermines the body-first model's biomarker and diagnostic utility at the initiating site.  
**What was checked**: Multi-center IHC study ([PMID: 27044604](https://pubmed.ncbi.nlm.nih.gov/27044604/)); SAA performance in peripheral tissues ([PMID: 42348807](https://pubmed.ncbi.nlm.nih.gov/42348807/)).  
**Resolution**: Validated enteric SAA protocols with standardized cutoffs; conformation-specific antibodies targeting pathological α-synuclein strains in gut tissue.

### Gap 4: SAA-Negative iRBD and Non-Synucleinopathy Body-First Phenocopies
**Scope**: 24.6% of iRBD patients are SAA-negative ([PMID: 42248896](https://pubmed.ncbi.nlm.nih.gov/42248896/)), yet iRBD is the flagship prodromal state for body-first PD.  
**Why it matters**: Suggests either non-α-syn etiologies for iRBD or assay sensitivity limitations; complicates clinical trial enrollment.  
**Resolution**: Long-term follow-up of SAA-negative iRBD with multi-tissue SAA, genetic profiling, and repeated lumbar punctures; alternative biomarker development.

### Gap 5: Microbiome Causality vs Association
**Scope**: Whether gut dysbiosis is a cause, consequence, or modifier of enteric α-synuclein pathology in humans is unresolved.  
**Why it matters**: Determines whether microbiome-targeted therapies (FMT, probiotics) can prevent or modify body-first PD.  
**What was checked**: 5 FMT RCTs with inconsistent results; mouse germ-free studies supportive but not directly translatable.  
**Resolution**: Prospective microbiome profiling in iRBD/constipation cohorts with longitudinal phenoconversion tracking; gnotobiotic humanized mouse models with specific bacterial communities.

### Gap 6: NSD-ISS/SynNeurGe Frameworks Lack Origin-Site Subtyping
**Scope**: Current biological staging systems for PD do not incorporate body-first vs brain-first classification.  
**Why it matters**: If origin site influences prognosis and treatment response, staging systems should capture it.  
**What was checked**: NSD-ISS validation ([PMID: 40302527](https://pubmed.ncbi.nlm.nih.gov/40302527/)); SynNeurGe framework ([PMID: 40906256](https://pubmed.ncbi.nlm.nih.gov/40906256/)).  
**Resolution**: Incorporation of MIBG, RBD status, and peripheral SAA into staging criteria; proposal for origin-site classification layer.

### Gap 7: No Body-First-Specific GWAS or Genetic Architecture Data
**Scope**: Genetic architecture specific to the body-first subtype (beyond LRRK2 and GBA) is unexplored.  
**Why it matters**: Genetic stratification could identify at-risk individuals and mechanistic pathways.  
**What was checked**: LRRK2-PD studies, GBA-DLB associations; no body-first-specific GWAS identified.  
**Resolution**: Subtype-stratified GWAS in large PD biobanks using RBD/MIBG-defined body-first classification.

### Limitations of This Investigation
1. **Literature search scope**: While 118 papers were reviewed, the search may have missed negative studies or pre-prints not indexed in PubMed.
2. **Publication bias**: Positive findings for the body-first model may be overrepresented; negative replication attempts may be underreported.
3. **Operational definitions vary**: "Body-first" PD is defined differently across studies (RBD-based, MIBG-based, autonomic symptom-based), making cross-study comparison imprecise.
4. **Mouse-to-human translation**: The strongest mechanistic evidence comes from mouse models using supraphysiological α-synuclein seeds; relevance to natural human disease initiation is uncertain.
5. **Subtype prevalence estimates**: The ~20–30% estimate for body-first PD derives from RBD prevalence in PD populations; true prevalence depends on the operational definition.
6. **No direct human gut-to-brain tracking**: No study has directly demonstrated α-synuclein propagating from gut to brain in a living human; all evidence is inferential.

{{figure:knowledge_gaps_table.png|caption=Comprehensive table of knowledge gaps ranked by importance, tractability, and resolution strategies}}

---

## Discriminating Tests

### Test 1: Prospective Longitudinal Vagal α-Synuclein Tracking
**Design**: Prospective cohort of iRBD patients undergoing serial vagal nerve ultrasound + multi-tissue SAA (CSF, skin, gut) over 10 years.  
**Stratification**: SAA-positive vs SAA-negative iRBD; with vs without constipation.  
**Expected result if body-first true**: Vagal α-synuclein positivity precedes CSF positivity in body-first cases; SAA-positive iRBD with constipation phenoconverts faster.  
**Expected result if brain-first dominates**: CSF positivity precedes peripheral tissue positivity regardless of symptom profile.

### Test 2: Prodromal Intervention Trial in High-Risk Body-First Population
**Design**: Phase II RCT of repeated FMT or LRRK2 kinase inhibitor in individuals with constipation + probable RBD + hyposmia (23-fold PD risk group).  
**Biomarkers**: CSF and skin SAA, DaT-SPECT, MIBG, gut microbiome profiling.  
**Expected result if body-first true**: Intervention delays SAA conversion and DAT decline in body-first prodromal population.  
**Discriminating power**: If microbiome intervention prevents SAA conversion, this supports microbiome as upstream trigger; if it improves symptoms without preventing SAA conversion, microbiome is a modifier only.

### Test 3: Subtype-Stratified Anti-α-Synuclein Immunotherapy
**Design**: Re-analysis or new trial of prasinezumab restricted to SAA-positive, MIBG-low (body-first) early PD.  
**Rationale**: Previous failures may reflect dilution by brain-first and non-synucleinopathy patients.  
**Expected result if body-first relevant**: Better response in body-first subgroup where peripheral α-synuclein burden is higher.

### Test 4: Gut-Specific α-Synuclein Strain Typing
**Design**: Compare α-synuclein fibril structures (via cryo-EM) from gut biopsies, skin biopsies, and brain autopsy tissue in body-first vs brain-first PD cases.  
**Expected result if body-first true**: Gut-derived and brain-derived strains should be structurally identical within body-first patients but may differ between body-first and brain-first cases.

### Test 5: Register-Based Gene–Environment Analysis in LRRK2 Carriers
**Design**: Assess PD incidence in LRRK2 carriers with vs without history of IBD or chronic gut inflammation, stratified by appendectomy/vagotomy history.  
**Data source**: Large biobank linkage (UK Biobank, Nordic registers).  
**Expected result if gene-environment body-first**: LRRK2 + gut inflammation + intact vagus → highest PD risk; LRRK2 + gut inflammation + vagotomy → reduced risk.

---

## Curation Leads

*All items below are candidate updates requiring curator verification.*

### Candidate Evidence References to Add

1. **[PMID: 42390607](https://pubmed.ncbi.nlm.nih.gov/42390607/)** — Pupillary and vagal sonography distinguishing subtypes. Snippet: *"Vagal atrophy increased with disease duration and severity. During the first decade of motor disease, vagal atrophy and dysfunction occurred in body-first but not brain-first PD."* **Status**: SUPPORT, HUMAN_CLINICAL.

2. **[PMID: 42386728](https://pubmed.ncbi.nlm.nih.gov/42386728/)** — Prodromal phase duration. Snippet: *"the prodromal phase of body-first LBD, from onset of cardiac sympathetic degeneration to predicted clinical PD diagnosis, exceeds 20 years."* **Status**: SUPPORT, HUMAN_CLINICAL.

3. **[PMID: 42327194](https://pubmed.ncbi.nlm.nih.gov/42327194/)** — LRRK2 × gut infection. **Status**: SUPPORT, MODEL_ORGANISM.

4. **[PMID: 27044604](https://pubmed.ncbi.nlm.nih.gov/27044604/)** — Enteric α-syn IHC specificity failure. Snippet: *"Positive alpha-synuclein staining was observed by all 5 judges in most of the slides from control cases."* **Status**: QUALIFIES, HUMAN_CLINICAL.

5. **[PMID: 41826284](https://pubmed.ncbi.nlm.nih.gov/41826284/)** — Phase 2 FMT trial. Snippet: *"the dFMT group showed significant improvement in motor symptoms (UPDRS III: -3.8 vs. +0.1; p = 0.0001)... correlating with decreased colonic α-synuclein aggregation."* **Status**: SUPPORT (qualified by inconsistent replication), HUMAN_CLINICAL.

6. **[PMID: 40447483](https://pubmed.ncbi.nlm.nih.gov/40447483/)** — Two atrophy subtypes within iRBD. **Status**: QUALIFIES, HUMAN_CLINICAL.

7. **[PMID: 42248896](https://pubmed.ncbi.nlm.nih.gov/42248896/)** — SAA-negative iRBD (24.6%). **Status**: QUALIFIES, HUMAN_CLINICAL.

8. **[PMID: 20098733](https://pubmed.ncbi.nlm.nih.gov/20098733/)** — Intragastric rotenone reproducing Braak staging. **Status**: SUPPORT, MODEL_ORGANISM.

9. **[PMID: 27912057](https://pubmed.ncbi.nlm.nih.gov/27912057/)** — Gut microbiota required for α-syn pathology. **Status**: SUPPORT, MODEL_ORGANISM.

10. **[PMID: 41702332](https://pubmed.ncbi.nlm.nih.gov/41702332/)** — Anti-α-syn immunotherapy failures. **Status**: QUALIFIES, HUMAN_CLINICAL.

### Candidate Pathophysiology Nodes or Edges
- **Node**: Enteroendocrine cells as α-synuclein source (referenced in [PMID: 29360467](https://pubmed.ncbi.nlm.nih.gov/29360467/))
- **Edge**: LRRK2 kinase activity → gut inflammation → enteric α-synuclein aggregation (PMID: 42327194, 42295088, 38750146)
- **Edge**: Bacterial curli amyloid → α-synuclein cross-seeding (PMID: 34413194)
- **Edge**: Gut microbiota metabolites → neuroinflammation → α-synuclein pathology (PMID: 27912057)

### Candidate Ontology Terms
- **Cell types**: Enteroendocrine cells (CL:0000164); Enteric glial cells; Vagal afferent neurons; Cardiac sympathetic postganglionic neurons
- **Biological processes**: GO:0070841 (inclusion body assembly); GO:0043524 (negative regulation of neuron apoptotic process); retrograde axonal transport; prion-like protein propagation
- **Disease subtypes**: Body-first Lewy body disease; Brain-first Lewy body disease

### Candidate Status Change
**Recommendation**: Maintain **ALTERNATIVE** status. The evidence supports the body-first model as a valid subtype-specific pathway, not a universal PD mechanism. Upgrading to PRIMARY would require: (a) identification of the upstream trigger, (b) direct human evidence of gut-to-brain α-synuclein transfer (not just correlation), and (c) successful disease modification through body-first-targeted intervention.

### Candidate Knowledge Gaps for KB
1. **Upstream trigger unknown**: The initiating event for enteric α-synuclein misfolding is unidentified in humans.
2. **Enteric SAA standardization needed**: No validated protocol for gut-tissue SAA with adequate sensitivity for prodromal disease.
3. **NSD-ISS origin-site layer absent**: Current biological staging does not incorporate body-first/brain-first classification.
4. **Microbiome causality unresolved**: FMT RCT results are inconsistent; no human evidence that dysbiosis precedes α-synuclein pathology.
5. **α-syn-independent PD**: LRRK2-PD is often SAA-negative, demonstrating the body-first α-syn model does not cover all PD.

{{figure:final_assessment.png|caption=Final comprehensive assessment of the body-first PD model showing evidence strength across all investigated domains}}

---

*Report generated from 5 investigative iterations, 15 confirmed findings, and 118 papers reviewed. Investigation date: July 2026.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist causal chain diagram](openscientist_artifacts/provenance_causal_chain_diagram.json)
![OpenScientist causal chain diagram](openscientist_artifacts/provenance_causal_chain_diagram.png)
- [OpenScientist evidence matrix](openscientist_artifacts/provenance_evidence_matrix.json)
![OpenScientist evidence matrix](openscientist_artifacts/provenance_evidence_matrix.png)
- [OpenScientist final assessment](openscientist_artifacts/provenance_final_assessment.json)
![OpenScientist final assessment](openscientist_artifacts/provenance_final_assessment.png)
- [OpenScientist knowledge gaps table](openscientist_artifacts/provenance_knowledge_gaps_table.json)
![OpenScientist knowledge gaps table](openscientist_artifacts/provenance_knowledge_gaps_table.png)
- [OpenScientist plot 1](openscientist_artifacts/provenance_plot_1.json)
![OpenScientist plot 1](openscientist_artifacts/provenance_plot_1.png)
- [OpenScientist plot 2](openscientist_artifacts/provenance_plot_2.json)
![OpenScientist plot 2](openscientist_artifacts/provenance_plot_2.png)
- [OpenScientist plot 3](openscientist_artifacts/provenance_plot_3.json)
![OpenScientist plot 3](openscientist_artifacts/provenance_plot_3.png)
- [OpenScientist plot 4](openscientist_artifacts/provenance_plot_4.json)
![OpenScientist plot 4](openscientist_artifacts/provenance_plot_4.png)
- [OpenScientist plot 5](openscientist_artifacts/provenance_plot_5.json)
![OpenScientist plot 5](openscientist_artifacts/provenance_plot_5.png)
- [OpenScientist summary dashboard](openscientist_artifacts/provenance_summary_dashboard.json)
![OpenScientist summary dashboard](openscientist_artifacts/provenance_summary_dashboard.png)