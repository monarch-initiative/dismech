# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search (Dataset-Anchored)

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

**Provider:** openscientist
**Generated:** 2026-08-28T07:43:02.809538

1. PMID:28758999
2. PMID:31802237
3. PMID:32949047
4. PMID:37708272
5. PMID:31437302
6. PMID:35649245
7. PMID:35971179
8. PMID:42413719
9. PMID:29238035
10. PMID:34267173
11. PMID:32050796
12. PMID:30841460
13. PMID:35741014
14. PMID:35106914
15. PMID:38852117
16. PMID:41620473
17. PMID:33432193
18. PMID:42628775