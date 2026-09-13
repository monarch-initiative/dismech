---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T07:24:46.565919'
end_time: '2026-08-28T07:43:02.809538'
duration_seconds: 1096.24
template_file: templates/hypothesis_deep_research_datasets.md
template_variables:
  disease_name: Alzheimer Disease
  category: Neurodegenerative Disorder
  hypothesis_group_id: necroptosis_model
  hypothesis_label: Necroptosis Model of Neuronal Death
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: necroptosis_model\nhypothesis_label: Necroptosis\
    \ Model of Neuronal Death\nstatus: EMERGING\ndescription: 'The mode of neuronal\
    \ death in Alzheimer disease is modeled as necroptosis \u2014 RIPK1/RIPK3-triggered,\n\
    \  MLKL-executed programmed necrosis \u2014 rather than apoptosis. Activated necrosome\
    \ components are found\n  in granulovacuolar degeneration bodies, a long-recognized\
    \ but mechanistically unexplained Alzheimer\n  lesion, and their regional burden\
    \ tracks neuronal loss. This model is significant because it names an\n  executioner:\
    \ it makes neuronal death a druggable step rather than the passive endpoint of\
    \ upstream pathology.'\napplies_to_subtypes:\n- Early-Onset Alzheimer's Disease\n\
    - Late-Onset Alzheimer's Disease\nevidence:\n- reference: PMID:28758999\n  reference_title:\
    \ Necroptosis activation in Alzheimer's disease.\n  supports: SUPPORT\n  evidence_source:\
    \ HUMAN_CLINICAL\n  snippet: We found that necroptosis was activated in postmortem\
    \ human AD brains, positively correlated\n    with Braak stage, and inversely\
    \ correlated with brain weight and cognitive scores.\n  explanation: Human postmortem\
    \ dose-response between necroptosis activation and both pathological stage\n \
    \   and cognitive outcome.\n- reference: PMID:31802237\n  reference_title: Necrosome\
    \ complex detected in granulovacuolar degeneration is associated with neuronal\n\
    \    loss in Alzheimer's disease.\n  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n\
    \  snippet: GVDn + neurons inversely correlated with neuronal density in the early\
    \ affected CA1 region\n    of the hippocampus and in the late affected frontal\
    \ cortex layer III.\n  explanation: Anchors the mechanism to a specific, classically\
    \ recognized neuropathological lesion and\n    shows its burden tracks neuronal\
    \ density in both an early- and a late-affected region.\n- reference: PMID:37708272\n\
    \  reference_title: MEG3 activates necroptosis in human neuron xenografts modeling\
    \ Alzheimer's disease.\n  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n\
    \  snippet: Down-regulation of MEG3 and inhibition of necroptosis using pharmacological\
    \ or genetic manipulation\n    of receptor-interacting protein kinase 1 (RIPK1),\
    \ RIPK3, or mixed lineage kinase domain-like protein\n    (MLKL) rescued neuronal\
    \ cell loss in xenografted human neurons.\n  explanation: 'Converts the human\
    \ correlation into a causal claim: blocking three separate necroptosis\n    effectors\
    \ each rescues loss of human neurons in vivo.'\n- reference: PMID:32949047\n \
    \ reference_title: Necrosome-positive granulovacuolar degeneration is associated\
    \ with TDP-43 pathological\n    lesions in the hippocampus of ALS/FTLD cases.\n\
    \  supports: PARTIAL\n  evidence_source: HUMAN_CLINICAL\n  snippet: Necrosome-positive\
    \ GVD was primarily observed in hippocampal regions of ALS/FTLD cases and\n  \
    \  was associated with hippocampal TDP-43 inclusions as the main predictor of\
    \ the pMLKL-GVD stage, as\n    well as with the Braak stage of neurofibrillary\
    \ tangle pathology.\n  explanation: 'Boundary condition: necrosome-positive granulovacuolar\
    \ degeneration is not specific to\n    Alzheimer disease but tracks proteinopathy\
    \ more generally, so necroptosis is better modeled as a shared\n    execution\
    \ mechanism than as an Alzheimer-defining one.'\nnotes: EMERGING. The human evidence\
    \ is correlative and rests substantially on phospho-MLKL and phospho-RIPK\n  immunostaining\
    \ of postmortem tissue, where antibody specificity and postmortem interval are\
    \ known problems.\n  The causal arm comes from human neurons xenografted into\
    \ a mouse amyloid brain \u2014 a system whose own\n  headline finding is that\
    \ mouse neurons in the same brain do not show the phenotype, which is an argument\n\
    \  for the model's human relevance and a reminder that rodent neurodegeneration\
    \ models may miss the death\n  mechanism entirely. Distinct from, and not yet\
    \ reconciled with, the PARP1 parthanatos route curated\n  in this entry; both\
    \ are caspase-independent regulated necrosis and no work has established which\
    \ dominates,\n  or whether they act in different cells or stages."
  candidate_datasets: 'All accessions below were resolved against the GEO API by the
    curator; each title

    is quoted as GEO states it. All are open-access human post-mortem brain.


    - **geo:GSE129308** - "Molecular signatures underlying neurofibrillary tangle
    susceptibility in Alzheimer''s disease" (Homo sapiens, 27 samples, PMID:41620473).
    Transcriptomes of single somas WITH neurofibrillary tangles versus tangle-free
    somas from the SAME human AD brains. The necroptosis model predicts that the death
    programme engages in specific, pathology-bearing neurons; this within-donor contrast
    is the natural place to ask whether MEG3, RIPK1, RIPK3 and MLKL transcripts are
    enriched in tangle-bearing neurons, and whether granulovacuolar-degeneration-associated
    neurons are transcriptionally distinct.

    - **geo:GSE147528** - "Molecular characterization of selectively vulnerable neurons
    in Alzheimer''s Disease" (Homo sapiens, PMID:33432193). Entorhinal cortex and
    superior frontal gyrus snRNA-seq across Braak stages, allowing necroptosis-pathway
    expression to be tracked against pathological stage and against the regions that
    degenerate early versus late.

    - **geo:GSE174367** - "Single-nucleus chromatin accessibility and transcriptomic
    characterization of Alzheimer''s Disease" (Homo sapiens). Paired snRNA-seq and
    snATAC-seq; relevant because MEG3 is an imprinted long non-coding RNA whose regulation
    is chromatin- and imprinting-dependent, so accessibility data bear on whether
    its reported up-regulation in AD is regulated or incidental.

    - **geo:GSE138852** - "A single-cell atlas of the human cortex reveals drivers
    of transcriptional changes in Alzheimer''s disease" (Homo sapiens). Independent
    replication cohort for any expression claim.

    - **geo:GSE157827** - "Single-nucleus transcriptome analysis reveals dysregulation
    of angiogenic endothelial cells and neuroprotective glia in Alzheimer''s disease"
    (Homo sapiens). Second independent replication cohort.


    Be explicit about a limitation of all of these for this hypothesis: necroptosis

    is executed by phosphorylation of MLKL, not by transcription, so transcript

    abundance is at best an indirect proxy. State clearly where a transcriptomic

    result could and could not support the model, and what phospho-protein or

    imaging data would be needed instead.'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 18
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

# Mechanistic Hypothesis Search (Dataset-Anchored)

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

This variant additionally supplies a list of **candidate public datasets** that a
curator has already located and resolved. Treat that list as a fixed input: the
point is to reason about what those specific datasets could and could not settle,
not to go looking for new ones (though you may name additional datasets you find).

## Target Disease
- **Disease Name:** Alzheimer Disease
- **Category:** Neurodegenerative Disorder

## Target Hypothesis
- **Hypothesis ID:** necroptosis_model
- **Hypothesis Label:** Necroptosis Model of Neuronal Death
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: necroptosis_model
hypothesis_label: Necroptosis Model of Neuronal Death
status: EMERGING
description: 'The mode of neuronal death in Alzheimer disease is modeled as necroptosis — RIPK1/RIPK3-triggered,
  MLKL-executed programmed necrosis — rather than apoptosis. Activated necrosome components are found
  in granulovacuolar degeneration bodies, a long-recognized but mechanistically unexplained Alzheimer
  lesion, and their regional burden tracks neuronal loss. This model is significant because it names an
  executioner: it makes neuronal death a druggable step rather than the passive endpoint of upstream pathology.'
applies_to_subtypes:
- Early-Onset Alzheimer's Disease
- Late-Onset Alzheimer's Disease
evidence:
- reference: PMID:28758999
  reference_title: Necroptosis activation in Alzheimer's disease.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: We found that necroptosis was activated in postmortem human AD brains, positively correlated
    with Braak stage, and inversely correlated with brain weight and cognitive scores.
  explanation: Human postmortem dose-response between necroptosis activation and both pathological stage
    and cognitive outcome.
- reference: PMID:31802237
  reference_title: Necrosome complex detected in granulovacuolar degeneration is associated with neuronal
    loss in Alzheimer's disease.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: GVDn + neurons inversely correlated with neuronal density in the early affected CA1 region
    of the hippocampus and in the late affected frontal cortex layer III.
  explanation: Anchors the mechanism to a specific, classically recognized neuropathological lesion and
    shows its burden tracks neuronal density in both an early- and a late-affected region.
- reference: PMID:37708272
  reference_title: MEG3 activates necroptosis in human neuron xenografts modeling Alzheimer's disease.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Down-regulation of MEG3 and inhibition of necroptosis using pharmacological or genetic manipulation
    of receptor-interacting protein kinase 1 (RIPK1), RIPK3, or mixed lineage kinase domain-like protein
    (MLKL) rescued neuronal cell loss in xenografted human neurons.
  explanation: 'Converts the human correlation into a causal claim: blocking three separate necroptosis
    effectors each rescues loss of human neurons in vivo.'
- reference: PMID:32949047
  reference_title: Necrosome-positive granulovacuolar degeneration is associated with TDP-43 pathological
    lesions in the hippocampus of ALS/FTLD cases.
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: Necrosome-positive GVD was primarily observed in hippocampal regions of ALS/FTLD cases and
    was associated with hippocampal TDP-43 inclusions as the main predictor of the pMLKL-GVD stage, as
    well as with the Braak stage of neurofibrillary tangle pathology.
  explanation: 'Boundary condition: necrosome-positive granulovacuolar degeneration is not specific to
    Alzheimer disease but tracks proteinopathy more generally, so necroptosis is better modeled as a shared
    execution mechanism than as an Alzheimer-defining one.'
notes: EMERGING. The human evidence is correlative and rests substantially on phospho-MLKL and phospho-RIPK
  immunostaining of postmortem tissue, where antibody specificity and postmortem interval are known problems.
  The causal arm comes from human neurons xenografted into a mouse amyloid brain — a system whose own
  headline finding is that mouse neurons in the same brain do not show the phenotype, which is an argument
  for the model's human relevance and a reminder that rodent neurodegeneration models may miss the death
  mechanism entirely. Distinct from, and not yet reconciled with, the PARP1 parthanatos route curated
  in this entry; both are caspase-independent regulated necrosis and no work has established which dominates,
  or whether they act in different cells or stages.
```

## Curator-Supplied Candidate Datasets

The following datasets have been located and their accessions resolved against
their repositories by a curator. Access status is stated where known; a
controlled-access dataset cannot be assumed usable without an approved request.

All accessions below were resolved against the GEO API by the curator; each title
is quoted as GEO states it. All are open-access human post-mortem brain.

- **geo:GSE129308** - "Molecular signatures underlying neurofibrillary tangle susceptibility in Alzheimer's disease" (Homo sapiens, 27 samples, PMID:41620473). Transcriptomes of single somas WITH neurofibrillary tangles versus tangle-free somas from the SAME human AD brains. The necroptosis model predicts that the death programme engages in specific, pathology-bearing neurons; this within-donor contrast is the natural place to ask whether MEG3, RIPK1, RIPK3 and MLKL transcripts are enriched in tangle-bearing neurons, and whether granulovacuolar-degeneration-associated neurons are transcriptionally distinct.
- **geo:GSE147528** - "Molecular characterization of selectively vulnerable neurons in Alzheimer's Disease" (Homo sapiens, PMID:33432193). Entorhinal cortex and superior frontal gyrus snRNA-seq across Braak stages, allowing necroptosis-pathway expression to be tracked against pathological stage and against the regions that degenerate early versus late.
- **geo:GSE174367** - "Single-nucleus chromatin accessibility and transcriptomic characterization of Alzheimer's Disease" (Homo sapiens). Paired snRNA-seq and snATAC-seq; relevant because MEG3 is an imprinted long non-coding RNA whose regulation is chromatin- and imprinting-dependent, so accessibility data bear on whether its reported up-regulation in AD is regulated or incidental.
- **geo:GSE138852** - "A single-cell atlas of the human cortex reveals drivers of transcriptional changes in Alzheimer's disease" (Homo sapiens). Independent replication cohort for any expression claim.
- **geo:GSE157827** - "Single-nucleus transcriptome analysis reveals dysregulation of angiogenic endothelial cells and neuroprotective glia in Alzheimer's disease" (Homo sapiens). Second independent replication cohort.

Be explicit about a limitation of all of these for this hypothesis: necroptosis
is executed by phosphorylation of MLKL, not by transcription, so transcript
abundance is at best an indirect proxy. State clearly where a transcriptomic
result could and could not support the model, and what phospho-protein or
imaging data would be needed instead.

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

### Dataset-Anchored Analysis

This section is the reason this report was commissioned. For **each** dataset in
the curator-supplied list above, state:

- **Fitness for purpose.** Can this dataset, as it actually exists (assay,
  tissue, cell numbers, donor count, disease staging, covariates), address the
  seed hypothesis at all? Say plainly when it cannot. A dataset that is the wrong
  assay or underpowered for the contrast is a useful negative finding.
- **The specific analysis.** Name the concrete computation: the contrast, the
  grouping variable, the cell types or features to score, the statistical test,
  and the covariates that must be controlled (age, sex, post-mortem interval,
  APOE genotype, Braak stage, batch, ambient RNA).
- **The discriminating prediction.** State what result would SUPPORT the seed
  hypothesis and what result would REFUTE or qualify it, in advance and in
  quantitative terms where possible. If no result would discriminate, say so —
  that is the most important thing you can report about that dataset.
- **Known confounds and prior analyses.** Has this dataset already been analyzed
  for this question, and by whom? Re-deriving a published result is not a test.
  Flag cell-type assignment ambiguity, signature-definition dependence, and
  reference-mapping choices where they would drive the answer.

Then rank the datasets by how decisively each would move the hypothesis, and say
which single analysis you would run first.

If a question central to this hypothesis cannot be settled by any listed dataset,
state which data type WOULD settle it and whether such data exist publicly.

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
Distinguish tests that can be run today on existing public data from tests that
require new sample collection.

### Curation Leads

Provide candidate updates for the KB, but label these as leads requiring curator
verification. Include:

- candidate evidence references and exact abstract snippets to verify
- candidate pathophysiology nodes or edges
- candidate ontology terms for cell types and biological processes
- candidate subtype restrictions or status changes
- candidate `knowledge_gaps` or discussion prompts for unresolved causal claims,
  conflicting evidence, or explicit source/data absences
- candidate `datasets:` entries, giving the accession exactly as the repository
  states it

Do not invent dataset accessions. If you name a dataset you found yourself,
mark it clearly as unverified so a curator resolves it before curation.

If the provider supports artifacts, produce artifact-friendly outputs such as an
evidence matrix, mechanistic diagram, knowledge-gap table, or comparison table.
These artifacts are important provenance for hypothesis-level review.


## Output

# Necroptosis Model of Neuronal Death in Alzheimer Disease — Dataset-Anchored Hypothesis Search

**Hypothesis ID:** `necroptosis_model` · **KB status:** EMERGING · **Disease:** Alzheimer Disease (Neurodegenerative Disorder)
**Report date:** 2026-08-28 · 3 iterations · 8 confirmed findings · 40 papers reviewed

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED. The seed hypothesis is correctly curated as EMERGING and should remain so.**

The necroptosis model proposes that neurons in Alzheimer disease (AD) die not by apoptosis but by RIPK1/RIPK3-triggered, MLKL-executed programmed necrosis, that the activated necrosome is housed in the classical but long-unexplained granulovacuolar degeneration (GVD) lesion, and that this makes neuronal death a *druggable step* rather than a passive endpoint. The strengths of this model are real and unusually complete for an "emerging" claim: it anchors to a specific neuropathological lesion, it scales with pathological stage and with cognition in human post-mortem brain, and — rare among AD death-mechanism hypotheses — it has a genuine *in vivo causal rescue* in a human-neuron system. That combination (lesion + human dose-response + causal rescue) is why the model deserves to be taken seriously rather than dismissed.

Four caveats, each independently sufficient to hold the model short of "supported," keep it EMERGING. **(1) The human arm is correlative** and rests substantially on phospho-MLKL and phospho-RIPK immunostaining of post-mortem tissue, where antibody specificity and post-mortem interval (PMI) are recognized problems and where no cohort-scale orthogonal (mass-spectrometry or biochemical) validation exists. **(2) The lesion is not AD-specific:** necrosome-positive GVD tracks TDP-43 proteinopathy in ALS/FTLD and is absent from some regions that degenerate in ALS, so necroptosis is better modeled as a *shared execution mechanism* across proteinopathies than as an AD-defining one. **(3) The proposed upstream trigger, the lncRNA MEG3, is not necroptosis-specific** — the same MEG3 up-regulation drives *caspase-dependent apoptosis* in multiple independent CNS-injury models, and AD necroptosis is separately framed as a *glial innate-immune / PANoptosis* program, creating a neuron-versus-glia attribution ambiguity. **(4) There is no completed efficacy trial:** CNS-penetrant RIPK1 inhibitors reached AD/ALS patients and engaged their target, but both lead programs were discontinued for non-CNS toxicology reasons before any readout on neuronal loss or cognition.

**On the dataset question — the reason this report was commissioned:** none of the five curator-supplied transcriptomic datasets can confirm the core execution claim, because MLKL activation is post-translational (phosphorylation), not transcriptional. Transcript abundance of *RIPK1/RIPK3/MLKL/MEG3* is at best an indirect proxy. Transcriptomics *can* usefully test the model's *localization* prediction — that the death programme is transcriptionally engaged in specific, pathology-bearing neurons — but it *cannot* demonstrate that MLKL is phosphorylated and executing. The single most decisive available analysis is the within-donor, tangle-bearing-versus-tangle-free contrast in **GSE129308**; the definitive tests require a PMI-controlled, antibody-validated p-MLKL cohort and a pathology-stratified CNS RIPK1-inhibitor trial, neither of which is a transcriptomic dataset.

---

## Key Findings

### F001 — Human post-mortem necroptosis activation tracks AD stage and cognition (dose-response)

Caccamo et al. 2017 ([PMID: 28758999](https://pubmed.ncbi.nlm.nih.gov/28758999/)) reported that necroptosis markers in post-mortem human AD brain are *positively correlated with Braak stage* and *inversely correlated with brain weight and cognitive scores*, and that a RIPK1-regulated gene set overlaps multiple independent AD transcriptomic signatures. This is the model's central human observation: a dose-response linking a molecular death programme to both the pathological severity axis (Braak) and the clinical outcome (cognition, brain atrophy). The critical limitation is that the data are correlative, no p-values are given in the abstract, and the markers rest on phospho-RIPK/phospho-MLKL immunodetection — the same antibody-specificity and PMI vulnerabilities that recur throughout the human evidence for this model. A correlation with Braak stage is also, by construction, a correlation with everything else that scales with Braak stage (tau burden, neuron loss, gliosis), so this finding establishes *association*, not *execution*.

### F002 — Necrosome-positive granulovacuolar degeneration anchors the mechanism to a classical AD lesion and tracks neuronal density

Koper et al. 2020 ([PMID: 31802237](https://pubmed.ncbi.nlm.nih.gov/31802237/)) detected all three activated necrosome components (pRIPK1, pRIPK3, pMLKL) within GVD lesions in neurons, colocalizing with classical GVD markers (pTDP-43, CK1δ). Critically, *GVDn+ neurons inversely correlated with neuronal density in the early-affected hippocampal CA1 region and in the late-affected frontal cortex layer III.* This is the strongest structural pillar of the model: it converts an abstract pathway into a named, microscopically identifiable lesion recognized for over a century, and it shows that the burden of necrosome-bearing neurons tracks neuronal loss in *both* an early- and a late-degenerating region. The limitation is that this remains correlative human neuropathology — the necrosome is *present in dying regions*, but the design cannot prove the necrosome *caused* the loss rather than marking cells already committed to death by another route.

### F003 — Necrosome-positive GVD is not AD-specific: it tracks proteinopathy across ALS/FTLD (scope limit)

Van Schoor et al. 2021 ([PMID: 32949047](https://pubmed.ncbi.nlm.nih.gov/32949047/)) found necrosome-positive GVD *primarily in the hippocampus of ALS/FTLD cases*, associated with hippocampal TDP-43 inclusions (the main predictor of pMLKL-GVD stage) and with Braak NFT stage — while central cortex and spinal-cord motor regions were *devoid* of pRIPK1/pRIPK3/pMLKL despite neuron loss in ALS. This is the model's most important boundary condition. It demonstrates two things at once: (a) necrosome-GVD is a *general proteinopathy-associated* phenomenon, not an AD signature, so the mechanism cannot be "what makes AD AD"; and (b) neuron loss can occur *without* detectable necrosome (ALS motor regions), so necroptosis is not the universal executioner even within a single disease. The mechanism is therefore best modeled as *one shared execution route engaged by proteinopathy*, not as the defining death mode of Alzheimer disease.

### F004 — Causal arm: human (not mouse) neurons xenografted into an AD-mouse brain develop GVD and necroptotic loss

Balusu et al. 2023 ([PMID: 37708272](https://pubmed.ncbi.nlm.nih.gov/37708272/)) provided the model's only *in vivo causal* evidence. Only *human* neurons xenografted into an amyloid mouse brain displayed tangles, Gallyas silver staining, GVD, phospho-tau blood biomarkers, and considerable neuronal loss; mouse neurons in the same brain did not. MEG3 lncRNA up-regulation drove the phenotype, and *genetic or pharmacological inhibition of RIPK1, RIPK3, or MLKL each independently rescued human neuron loss*. Blocking three separate effectors and rescuing loss each time is strong evidence that the pathway is *load-bearing*, not epiphenomenal. The species-specificity is simultaneously the finding's greatest strength and its sharpest caveat: it argues that the death mechanism is genuinely human-relevant (and that rodent neurodegeneration models may miss it entirely), but it also means the causal claim has been demonstrated in exactly one engineered system and awaits independent replication in another human-neuron model.

### F005 — RIPK1 is druggable in the CNS, but no efficacy trial has tested the AD-death hypothesis

Two CNS-penetrant reversible RIPK1 inhibitors reached humans. DNL104 ([PMID: 31437302](https://pubmed.ncbi.nlm.nih.gov/31437302/)) engaged target (inhibited RIP1 kinase phosphorylation) but produced post-dose liver toxicity in 37.5% of the multiple-ascending-dose group. SAR443060/DNL747 ([PMID: 35649245](https://pubmed.ncbi.nlm.nih.gov/35649245/)) distributed into CSF, reduced pRIPK1 in PBMCs, and was *"generally safe and well-tolerated in healthy volunteers and patients with AD or ALS"* — but development was discontinued for long-term nonclinical toxicology findings. The translational significance is double-edged: CNS RIPK1 inhibition is *feasible and tolerated in AD patients* (the drug reaches the target compartment and engages the target), yet the crucial experiment — does blocking the executioner slow neuronal loss or cognitive decline? — has *never been read out*. The model's headline promise ("a druggable step") is therefore established as *druggable* but wholly *untested for efficacy*.

### F006 — Competing/upstream mechanisms: hyperphosphorylated tau triggers necroptosis; parthanatos is a parallel caspase-independent route

Dong et al. 2022 ([PMID: 35971179](https://pubmed.ncbi.nlm.nih.gov/35971179/)) showed that *hyperphosphorylated tau induces RIPK1/RIPK3/MLKL necrosome assembly* and NF-κB cytokine induction, and that Nec-1s ameliorates behavior in TauP301S mice — positioning tau as an upstream trigger that connects the executioner to canonical AD proteinopathy. Separately, a 2026 review on PARP1-dependent parthanatos ([PMID: 42413719](https://pubmed.ncbi.nlm.nih.gov/42413719/)) describes how Aβ-induced oxidative stress and DNA damage overactivate PARP1, driving NAD+/ATP collapse and AIF-mediated parthanatos — a *parallel* caspase-independent death not yet reconciled with necroptosis. Both routes are caspase-independent regulated necrosis, and no work has established which dominates, whether they co-occur in the same neurons, or whether they partition by cell type or disease stage. This is the single most important unresolved competition for the seed hypothesis.

### F007 — MEG3 is a general pro-death lncRNA that acts largely via APOPTOSIS in prior CNS-injury literature (qualifies its necroptosis-specific role)

Across multiple independent CNS-injury models, MEG3 up-regulation drives neuronal death and its silencing is protective — but via *apoptotic/caspase* pathways, not necroptosis: ischemic stroke via miR-21/PDCD4 ([PMID: 29238035](https://pubmed.ncbi.nlm.nih.gov/29238035/): *"MEG3 functions as a competing endogenous RNA … competes with PDCD4 mRNA for directly binding to miR-21, which mediates ischemic neuronal death"*), intracerebral hemorrhage via miR-181b with reduced caspase-3 on knockdown ([PMID: 34267173](https://pubmed.ncbi.nlm.nih.gov/34267173/)), hypoxia via miR-21 ([PMID: 32050796](https://pubmed.ncbi.nlm.nih.gov/32050796/)), and ischemia-reperfusion ([PMID: 30841460](https://pubmed.ncbi.nlm.nih.gov/30841460/)). This directly qualifies the AD xenograft claim (PMID:37708272) that MEG3 drives *specifically* necroptosis. MEG3 appears to be a general pro-neuronal-death effector whose downstream death modality is context-dependent; the necroptotic reading may be specific to the amyloid xenograft context rather than an intrinsic property of MEG3.

### F008 — Cell-type ambiguity: necroptosis in AD may be substantially glial (innate-immune) rather than a pure neuronal executioner

Rajesh & Kanneganti 2022 ([PMID: 35741014](https://pubmed.ncbi.nlm.nih.gov/35741014/)) frame necroptosis in AD as one of several *innate-immune* cell-death programs — alongside pyroptosis, apoptosis, and PANoptosis — engaged by microglia and astrocytes to produce proinflammatory cytokines (*"innate immune cells can cause programmed cell death through multiple pathways, including pyroptosis, apoptosis, necroptosis, and PANoptosis"*). This contrasts with the seed model's neuron-executioner framing. The necrosome-GVD human data (PMID:31802237) is unambiguously *neuronal*, but any *transcriptomic* necroptosis signal in bulk or single-nucleus data could originate in glia. This cell-type attribution ambiguity is precisely what makes cell-resolved data (the curator's datasets) relevant — and precisely why signature-definition and cell-type-assignment choices will drive the answer.

---

## Mechanistic Model / Interpretation

The hypothesis implies the following causal chain. I mark each link by evidential strength.

```
  Aβ / amyloid load          Hyperphosphorylated tau (NFT)          TDP-43 proteinopathy
        │                            │                                     │
        │ (in vitro, PMID:35106914)  │ STRONG causal (mouse+human)         │ (ALS/FTLD, PMID:32949047)
        ▼                            ▼  PMID:35971179                       ▼
        └────────────►  MEG3 lncRNA up-regulation  ◄───────────────────────┘
                               │
                               │  INFERRED / NOT necroptosis-specific
                               │  (MEG3 → apoptosis in other CNS injury: PMID:29238035, 34267173)
                               ▼
              RIPK1 ──► RIPK3 ──► necrosome assembly
                               │   STRONG causal in ONE human-neuron system
                               │   (triple rescue, PMID:37708272)
                               ▼
                    MLKL phosphorylation (p-MLKL)   ◄── THE EXECUTION STEP
                               │                        Post-translational — INVISIBLE to transcriptomics
                               ▼
         Necrosome deposited in GVD bodies  (STRONG human localization, PMID:31802237)
                               │
                               ▼
              Neuronal membrane rupture / programmed necrosis
                               │   correlative human dose-response
                               ▼   (PMID:28758999, 31802237)
              Regional neuronal loss ──► brain atrophy ──► cognitive decline
```

**Where the literature is strong.** The *lesion* link (necrosome → GVD, PMID:31802237) and the *causal effector* link (RIPK1/RIPK3/MLKL each required for human-neuron death, PMID:37708272) are the two well-supported edges. The *upstream trigger* from p-tau to necrosome assembly (PMID:35971179) is also causally supported in a tau mouse model.

**Where links are inferred or contested.** The MEG3 → necroptosis edge is *inferred* and non-specific (F007). The attribution of transcriptomic/bulk necroptosis signal to neurons versus glia is *ambiguous* (F008). The relationship between necroptosis and the parallel parthanatos route is *entirely unmapped* (F006).

**The missing causal step that no listed dataset can supply.** The execution event is MLKL *phosphorylation and membrane translocation* — a post-translational event. Every curator-supplied dataset measures *transcript abundance* or *chromatin accessibility*. None measures p-MLKL. This is the structural reason transcriptomics can localize and stage the pathway's *transcriptional* engagement but can never confirm *execution*.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:28758999](https://pubmed.ncbi.nlm.nih.gov/28758999/) | Human clinical (post-mortem) | **Support** | Necroptosis activation scales with AD severity | Necroptosis markers ↑ with Braak stage, ↓ with brain weight & cognition | LOAD/EOAD, cortex/hippocampus | Moderate. Correlative; phospho-antibody dependent; no p-values in abstract |
| [PMID:31802237](https://pubmed.ncbi.nlm.nih.gov/31802237/) | Human clinical (neuropath) | **Support** | Necrosome localizes to GVD and tracks neuron loss | pRIPK1/pRIPK3/pMLKL in GVD; GVDn+ inversely ∝ neuronal density in CA1 & frontal L-III | Early & late regions | Moderate–high for localization; correlative for causation |
| [PMID:37708272](https://pubmed.ncbi.nlm.nih.gov/37708272/) | Model organism (human-neuron xenograft) | **Support** | RIPK1/RIPK3/MLKL each required for neuron death | Triple genetic/pharmacological rescue; human-neuron-specific GVD & loss | Amyloid xenograft AD model | High for causality *in this system*; single system, awaits replication |
| [PMID:35971179](https://pubmed.ncbi.nlm.nih.gov/35971179/) | Model organism (Tau mouse) + in vitro | **Support (upstream)** | p-tau triggers necrosome assembly | p-tau → RIPK1/RIPK3/MLKL necrosome + NF-κB; Nec-1s improves behavior | Tauopathy | Moderate; mouse tau model |
| [PMID:32949047](https://pubmed.ncbi.nlm.nih.gov/32949047/) | Human clinical (neuropath) | **Qualifies** | Necrosome-GVD specificity to AD | Necrosome-GVD tracks TDP-43/Braak in ALS/FTLD; absent in some degenerating regions | ALS/FTLD | High; strong scope-limiting evidence |
| [PMID:35106914](https://pubmed.ncbi.nlm.nih.gov/35106914/) | In vitro (SH-SY5Y) | **Support** | Aβ drives RIPK1/MLKL necroptosis | Aβ-induced death is caspase/autophagy-independent, RIPK1-dependent | Aβ toxicity | Low–moderate; cell line |
| [PMID:29238035](https://pubmed.ncbi.nlm.nih.gov/29238035/) | Model organism (ischemia) | **Qualifies/competing** | MEG3 death mechanism is necroptosis-specific | MEG3 drives *apoptotic* death via miR-21/PDCD4 | Ischemic stroke | High; undercuts MEG3→necroptosis specificity |
| [PMID:34267173](https://pubmed.ncbi.nlm.nih.gov/34267173/) | Model organism (ICH) | **Qualifies/competing** | MEG3 death mechanism | MEG3 knockdown ↓ caspase-3, ↓ apoptosis via miR-181b | Intracerebral hemorrhage | High; apoptotic, not necroptotic |
| [PMID:32050796](https://pubmed.ncbi.nlm.nih.gov/32050796/) | In vitro (PC12 hypoxia) | **Qualifies** | MEG3 death mechanism | MEG3 silencing ↓ apoptosis via miR-21 | Hypoxia | Moderate |
| [PMID:35741014](https://pubmed.ncbi.nlm.nih.gov/35741014/) | Review | **Qualifies (cell type)** | Neuron-executioner framing | Necroptosis as glial innate-immune death (with pyroptosis/PANoptosis) | AD neuroinflammation | Review-level; reframes cell-of-origin |
| [PMID:42413719](https://pubmed.ncbi.nlm.nih.gov/42413719/) | Review | **Competing** | Sole caspase-independent route | PARP1/parthanatos parallel route from Aβ/oxidative stress | AD | Review-level; unreconciled alternative |
| [PMID:31437302](https://pubmed.ncbi.nlm.nih.gov/31437302/) | Human clinical (Phase I) | **Support (druggability)** | CNS RIPK1 is targetable | DNL104 engaged target; 37.5% post-dose liver toxicity (MAD) | Healthy volunteers | Feasibility only; no efficacy |
| [PMID:35649245](https://pubmed.ncbi.nlm.nih.gov/35649245/) | Human clinical (Phase I/Ib) | **Support (druggability)** | CNS RIPK1 engagement in patients | DNL747 in CSF, ↓pRIPK1, safe in AD/ALS; discontinued (nonclinical tox) | AD & ALS patients | Feasibility only; no efficacy readout |
| [PMID:38852117](https://pubmed.ncbi.nlm.nih.gov/38852117/) | Review | **Support (synthesis)** | Necroptosis drives AD neurodegeneration | Synthesizes neuron-specific GVD-necroptosis pathway & therapeutic case | AD | Review-level orientation |

---

## Dataset-Anchored Analysis

**Overarching limitation applying to all five datasets.** Necroptosis is *executed* by MLKL phosphorylation and membrane translocation — a post-translational event. All five datasets measure RNA (and, for GSE174367, chromatin accessibility). Therefore:

- A transcriptomic result **can** support the model's *localization/staging* sub-claims: that *RIPK1/RIPK3/MLKL/MEG3* transcripts are enriched in pathology-bearing neurons, that they rise with Braak stage, that MEG3 up-regulation is chromatin-regulated rather than incidental, and that these signals are neuronal rather than glial.
- A transcriptomic result **cannot** support the *execution* claim: it cannot show MLKL is phosphorylated, that the necrosome is assembled, or that a neuron died by necroptosis rather than apoptosis/parthanatos. A neuron committed to necroptosis need not up-regulate the pathway's transcripts at all.

### GSE129308 — "Molecular signatures underlying neurofibrillary tangle susceptibility in AD" (27 samples, PMID:41620473)

- **Fitness for purpose: HIGH (best of the five).** This is the only dataset offering a *within-donor* contrast — single somas WITH NFTs versus tangle-free somas from the *same* AD brains. That design directly matches the model's core localization prediction (the death programme engages in specific, pathology-bearing neurons) and eliminates between-donor confounders (age, sex, PMI, APOE, batch) by construction.
- **Specific analysis:** paired differential expression of *MEG3, RIPK1, RIPK3, MLKL* (and canonical necrosome partners *TNFRSF1A, FADD, ZBP1*) in tangle+ vs tangle− somas within donor; paired Wilcoxon or mixed-effects model with donor as random effect; control for soma capture depth and ambient RNA. Secondary: score a curated necroptosis signature and test enrichment; ask whether GVD-associated neurons form a transcriptionally distinct cluster.
- **Discriminating prediction — SUPPORT:** MEG3 and ≥2 of {RIPK1, RIPK3, MLKL} significantly enriched in tangle+ somas (paired FDR<0.05, consistent direction across donors), matching the p-tau→necrosome edge (PMID:35971179). **REFUTE/QUALIFY:** no necroptosis-transcript enrichment in tangle+ somas, or enrichment of apoptotic effectors instead — consistent with F007's apoptotic reading of MEG3.
- **Confounds & priors:** tangle-bearing somas are captured from already-stressed neurons; up-regulation may reflect stress generally, not necroptosis specifically. The associated primary paper (PMID:41620473) should be checked for whether this exact contrast was already reported — re-deriving it is not a test. A positive result is *suggestive, not confirmatory* (transcript ≠ p-MLKL).

### GSE147528 — "Selectively vulnerable neurons in AD" (EC + SFG snRNA-seq across Braak stages, PMID:33432193)

- **Fitness for purpose: MODERATE.** Its across-Braak, early-region (entorhinal cortex) versus late-region (superior frontal gyrus) design fits the *staging* and *regional-vulnerability* predictions. But it is between-donor, so age/sex/PMI/APOE/batch must be modeled, and snRNA-seq under-captures long non-coding and low-abundance transcripts (relevant for MEG3, RIPK3).
- **Specific analysis:** pseudobulk per cell type per donor; test necroptosis-signature score vs Braak stage in excitatory neurons of EC vs SFG; linear mixed model with Braak as ordinal predictor and age/sex/PMI/APOE/batch as covariates; per-cell-type to resolve F008's neuron-vs-glia ambiguity.
- **Discriminating prediction — SUPPORT:** necroptosis-transcript score rises monotonically with Braak in *excitatory neurons*, earlier in EC than SFG. **REFUTE/QUALIFY:** the signal is confined to microglia/astrocytes (supports the glial-innate-immune reframing, F008), or shows no Braak trend.
- **Confounds & priors:** cell-type assignment and signature definition will drive the answer; nuclear RNA depletes cytoplasmic/GVD-localized transcripts. Selective-vulnerability analyses of this dataset are published (PMID:33432193) — check whether necroptosis genes already appeared.

### GSE174367 — "Paired snRNA-seq + snATAC-seq of AD"

- **Fitness for purpose: MODERATE, and uniquely suited to ONE sub-question.** Because MEG3 is an imprinted lncRNA whose regulation is chromatin- and imprinting-dependent, paired ATAC data can test whether reported MEG3 up-regulation is *regulated* (accompanied by accessibility changes at the MEG3/DLK1-DIO3 locus) or *incidental*. No other listed dataset can address this.
- **Specific analysis:** in matched nuclei, correlate MEG3 expression with chromatin accessibility at the MEG3 promoter and DLK1-DIO3 imprinted control region, stratified by cell type and diagnosis; test for differential accessibility in AD vs control neurons; control for batch, PMI, ambient signal.
- **Discriminating prediction — SUPPORT:** MEG3 up-regulation in AD neurons coincides with *increased accessibility* at its regulatory elements (regulated activation). **REFUTE/QUALIFY:** MEG3 RNA changes with *no* accessibility change (incidental / post-transcriptional), weakening the "regulated death programme" reading.
- **Confounds & priors:** snATAC is sparse; imprinted-locus accessibility is technically hard to interpret. This tests *regulation of the trigger*, not execution.

### GSE138852 — "Single-cell atlas of human cortex, drivers of transcriptional change in AD"

- **Fitness for purpose: LOW–MODERATE (replication only).** Useful as an *independent replication cohort* for any expression claim generated in GSE129308/GSE147528, not as a primary test. Cortical, between-donor, standard case/control.
- **Specific analysis:** repeat the pseudobulk necroptosis-signature-vs-diagnosis and per-cell-type analysis; ask whether direction/effect size replicate.
- **Discriminating prediction — SUPPORT:** effect replicates in the same cell type and direction. **REFUTE:** no replication. Replication of a *transcript* result still cannot establish execution.
- **Confounds & priors:** different cohort, dissociation protocol, and annotation; harmonize signatures before comparing.

### GSE157827 — "snRNA-seq, dysregulation of endothelial cells and glia in AD"

- **Fitness for purpose: LOW (second replication).** Its headline biology is vascular/glial, not neuronal death, so it is a *second replication cohort* at best and may be actively unsuited if neuronal capture is limited. A dataset whose emphasis is endothelial/glial is a useful place to *test the glial-necroptosis alternative* (F008) rather than the neuronal-executioner claim.
- **Specific analysis:** score necroptosis signature in microglia/astrocytes vs neurons across diagnosis; use as replication of any glial signal from GSE147528.
- **Discriminating prediction — SUPPORT (of seed):** neuronal necroptosis signal present. **QUALIFY (glial alternative):** signal predominantly glial. **REFUTE:** absent.
- **Confounds & priors:** neuronal under-representation limits power for the neuronal claim.

### Ranking — how decisively each dataset moves the hypothesis

| Rank | Dataset | Decisiveness | Why |
|---|---|---|---|
| 1 | **GSE129308** | Highest available | Within-donor tangle+/tangle− contrast; controls confounders; directly tests localization prediction |
| 2 | **GSE174367** | Targeted | Only dataset that can test whether MEG3 up-regulation is chromatin-regulated |
| 3 | **GSE147528** | Moderate | Staging + regional vulnerability; resolves some neuron-vs-glia ambiguity |
| 4 | **GSE138852** | Low (replication) | Independent replication of expression claims |
| 5 | **GSE157827** | Lowest | Vascular/glial focus; best for testing the glial alternative |

**Run first:** the **paired within-donor tangle+ vs tangle− differential expression of MEG3/RIPK1/RIPK3/MLKL in GSE129308**, with donor as a random effect and a curated necroptosis signature scored per soma. It is the only analysis in the set that both matches a specific model prediction *and* is internally controlled for the covariates that plague between-donor AD transcriptomics. Report it as *suggestive*, never confirmatory.

**The central question no listed dataset can settle** — *is MLKL actually phosphorylated and executing neurons in AD brain?* — requires **p-MLKL quantification** (validated antibody with knockout control, or targeted phospho-proteomic mass spectrometry) in a **PMI-controlled cohort**, ideally with single-cell spatial proteomics to assign the signal to neurons versus glia. Such data are *not* among the five datasets and are only patchily available publicly (immunostaining figures in the primary papers, no open quantitative cohort). Generating it is the highest-value new experiment.

---

## Knowledge Gaps

| Gap | Scope | Why it matters | What was checked | What would resolve it |
|---|---|---|---|---|
| **Execution vs correlation** | Core causal step | Transcript/immunostain data show association, not that p-MLKL executes neurons | Human post-mortem papers (28758999, 31802237); all correlative/IHC | PMI-controlled p-MLKL phospho-proteomics with KO-validated antibody |
| **AD-specificity** | Whole-model scope | Necrosome-GVD tracks proteinopathy broadly, not AD | ALS/FTLD neuropath (32949047) | Head-to-head necrosome quantification across proteinopathies with matched neuron loss |
| **MEG3 death-modality** | Trigger edge | MEG3 drives apoptosis elsewhere; necroptosis reading may be context-specific | 4 CNS-injury studies (29238035, 34267173, 32050796, 30841460) vs xenograft (37708272) | Death-modality dissection (parallel RIPK3-KO + caspase-inhibition) in a second human-neuron AD model |
| **Neuron vs glia** | Cell-of-origin | Bulk/transcriptomic necroptosis could be glial (innate-immune) | Review (35741014); human GVD data is neuronal | Cell-resolved p-MLKL spatial proteomics |
| **Necroptosis vs parthanatos** | Competing routes | Both caspase-independent; which dominates / where is unknown | Review (42413719); no reconciling primary study found | Co-staining p-MLKL + PAR/AIF in same cohort, stage- and cell-stratified |
| **Efficacy** | Therapeutic claim | "Druggable executioner" is untested on outcomes | Phase I only (31437302, 35649245); both discontinued | Pathology-stratified Phase II RIPK1-inhibitor trial with neuronal-loss/cognition endpoints |
| **Antibody/PMI validity** | Data quality | Human arm depends on phospho-antibodies vulnerable to PMI | Noted across post-mortem studies | Orthogonal biochemical/MS validation in PMI-graded tissue |

For each gap, the "what was checked" column records what the search actually examined, so that absence of evidence (e.g., no reconciling necroptosis-vs-parthanatos primary study, no open p-MLKL cohort) is reported as a searched-for absence rather than an assumed one.

---

## Alternative Models

| Model | Relationship to seed | Basis |
|---|---|---|
| **Apoptosis** | Classical alternative executioner | The mode the seed explicitly rejects; MEG3's default death route in non-AD CNS injury (F007) |
| **PARP1 / parthanatos** | *Parallel* caspase-independent route | Aβ→oxidative stress/DNA damage→PARP1→NAD+/ATP collapse→AIF (PMID:42413719); unreconciled with necroptosis (F006) |
| **Ferroptosis** | Parallel iron/lipid-peroxidation death | Iron dyshomeostasis, GPX4 failure (PMID:42628775) — associational in human AD |
| **Pyroptosis / PANoptosis (glial innate-immune)** | *Reframes cell-of-origin* | Necroptosis as one of several microglial/astrocytic innate-immune death programs (PMID:35741014, F008) |
| **Hyperphosphorylated tau** | *Upstream cause*, not competitor | p-tau triggers necrosome assembly (PMID:35971179); GVD houses the necrosome — tau feeds the seed model |
| **Amyloid-β** | *Upstream cause* | Aβ drives RIPK1/MLKL necroptosis in vitro (PMID:35106914) and MEG3 up-regulation in the xenograft |
| **MEG3 lncRNA dysregulation** | *Upstream trigger* within the seed model | Non-specific effector; sits above the necrosome (F007) |

The most consequential distinction: **tau and Aβ are upstream causes that the seed model incorporates**, whereas **parthanatos, ferroptosis, and glial pyroptosis/PANoptosis are genuine competing executioners** the model must be tested against. Parthanatos is the priority competitor because it shares the caspase-independent phenotype and the same Aβ/DNA-damage upstream, making it the hardest to distinguish without direct co-staining.

---

## Discriminating Tests

**Runnable today on existing public data**
1. **Within-donor tangle+/tangle− necroptosis DE (GSE129308).** Paired mixed-effects test of MEG3/RIPK1/RIPK3/MLKL. *Expected if seed true:* enrichment in tangle+ somas. *Cost:* none. *Caveat:* suggestive only.
2. **MEG3 expression-vs-accessibility coupling (GSE174367).** *Expected if seed true:* MEG3 RNA up + accessibility up at MEG3/DLK1-DIO3. Distinguishes regulated from incidental.
3. **Cell-type partition of necroptosis signal across Braak (GSE147528; replicate in GSE138852/GSE157827).** Tests neuron-vs-glia origin (F008) and staging.

**Requires new sample collection**
4. **PMI-graded p-MLKL phospho-proteomics** (KO-validated antibody or targeted MS) across a case/control cohort — the definitive execution test; resolves antibody/PMI concern.
5. **Dual p-MLKL + PAR/AIF spatial proteomics**, stage- and cell-type-stratified — directly arbitrates necroptosis vs parthanatos (F006) in the same tissue.
6. **Independent human-neuron AD model** (organoid or second xenograft) with RIPK3-KO *plus* pan-caspase inhibition to dissect MEG3's death modality (F007) and replicate the triple-rescue (PMID:37708272) outside one lab's system.
7. **Pathology-stratified Phase II RIPK1-inhibitor trial** with a CNS-penetrant, non-hepatotoxic compound, powered on neuronal-loss/atrophy and cognition endpoints — the only test of the "druggable executioner" promise (F005).

---

## Curation Leads *(all require curator verification)*

**Candidate evidence references / snippets to verify**
- [PMID:35971179](https://pubmed.ncbi.nlm.nih.gov/35971179/) — *"Hyperphosphorylated tau could induce necroptosis in neuronal cells by promoting the formation of the RIPK1/RIPK3/MLKL necrosome."* → adds an **upstream trigger (p-tau→necrosome)** edge; stance SUPPORT (upstream), MODEL_ORGANISM.
- [PMID:35106914](https://pubmed.ncbi.nlm.nih.gov/35106914/) — Aβ drives RIPK1/MLKL-dependent, caspase-independent death in SH-SY5Y → SUPPORT (in vitro, Aβ trigger).
- [PMID:29238035](https://pubmed.ncbi.nlm.nih.gov/29238035/) — MEG3→miR-21/PDCD4 *apoptotic* death → QUALIFIES the MEG3-necroptosis-specificity claim.
- [PMID:35741014](https://pubmed.ncbi.nlm.nih.gov/35741014/) — necroptosis as glial innate-immune death → QUALIFIES cell-of-origin.
- [PMID:42413719](https://pubmed.ncbi.nlm.nih.gov/42413719/) — PARP1/parthanatos parallel route → COMPETING model cross-link.
- [PMID:31437302](https://pubmed.ncbi.nlm.nih.gov/31437302/) & [PMID:35649245](https://pubmed.ncbi.nlm.nih.gov/35649245/) — CNS RIPK1 druggability + patient tolerability, no efficacy → SUPPORT (druggability) with explicit "no efficacy readout" note.

**Candidate pathophysiology nodes/edges**
- Add edge: `hyperphosphorylated_tau → necrosome_assembly` (SUPPORT, PMID:35971179).
- Add edge: `amyloid_beta → RIPK1/MLKL necroptosis` (in vitro, PMID:35106914).
- Add edge: `MEG3 → {necroptosis | apoptosis}` marked *context-dependent, non-specific*.
- Add competing node: `PARP1_parthanatos` with an explicit `unreconciled_with: necroptosis_model` link.

**Candidate ontology terms**
- Cell types: neuron (CL:0000540), microglial cell (CL:0000129), astrocyte (CL:0000127).
- Processes: necroptotic process (GO:0070266), programmed necrotic cell death (GO:0097300), parthanatos (GO:0140208), MLKL phosphorylation, granulovacuolar degeneration (lesion, no clean GO term — curator note).

**Candidate subtype restrictions / status**
- Keep status **EMERGING**. Add scope qualifier: mechanism is *shared across proteinopathies (AD, ALS/FTLD)*, not AD-specific (PMID:32949047).
- No basis to differentiate EOAD vs LOAD from current evidence; retain both `applies_to_subtypes` but flag as *untested by subtype*.

**Candidate knowledge_gaps / discussion prompts**
- "Transcriptomic datasets cannot confirm the execution step (p-MLKL); require phospho-proteomic/imaging data."
- "Necroptosis vs parthanatos dominance unresolved — no primary study co-localizes both."
- "No completed efficacy trial; both CNS RIPK1 leads discontinued for non-CNS toxicity."

**Candidate `datasets:` entries (accessions exactly as GEO states)**
- `geo:GSE129308` — "Molecular signatures underlying neurofibrillary tangle susceptibility in Alzheimer's disease" *(primary lead for within-donor tangle contrast)*.
- `geo:GSE147528` — "Molecular characterization of selectively vulnerable neurons in Alzheimer's Disease".
- `geo:GSE174367` — "Single-nucleus chromatin accessibility and transcriptomic characterization of Alzheimer's Disease".
- `geo:GSE138852` — "A single-cell atlas of the human cortex reveals drivers of transcriptional changes in Alzheimer's disease".
- `geo:GSE157827` — "Single-nucleus transcriptome analysis reveals dysregulation of angiogenic endothelial cells and neuroprotective glia in Alzheimer's disease".
- *(Unverified, curator to resolve)* — a **p-MLKL/necrosome immunohistochemistry or spatial-proteomics cohort** would be the decisive data type; no open quantitative accession was located during this search.

---

## Limitations of This Report

This was a literature- and reasoning-based hypothesis search; no dataset was downloaded or computed on. The dataset-anchored section specifies *predictions and analyses in advance* but does not execute them — a deliberate scope choice given that the decisive evidence (p-MLKL) is not transcriptomic. Citation attributions rest on the abstracts and verified snippets in the knowledge state; several supporting items are reviews, labeled as such. Effect sizes for the human post-mortem correlations are not available from abstracts and should be extracted from full texts before curation.

---

*Prepared for the Disorder Mechanisms Knowledge Base — hypothesis-level review. All curation leads require curator verification before entry.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)