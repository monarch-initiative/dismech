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
- **Hypothesis ID:** endolysosomal_origin_model
- **Hypothesis Label:** Endolysosomal Origin ("Inside-Out" Amyloid) Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: endolysosomal_origin_model
hypothesis_label: Endolysosomal Origin ("Inside-Out" Amyloid) Model
status: EMERGING
description: Amyloid pathology is modeled as beginning inside the neuron rather than in the extracellular
  space. Endocytic-pathway activation with enlargement of Rab5-positive early endosomes is the earliest
  recognized neuronal change in sporadic Alzheimer disease, preceding plaque deposition; APP-beta-C-terminal
  fragment accumulation then inhibits the lysosomal v-ATPase, autolysosomes fail to acidify, and amyloid-beta
  builds up within de-acidified autolysosomes until the neuron ruptures and its contents become the plaque
  core (the PANTHOS pattern). Under this model the senile plaque is the tombstone of a dead neuron, not
  a deposit of secreted peptide, which inverts the direction of the classical extracellular cascade.
applies_to_subtypes:
- Early-Onset Alzheimer's Disease
- Late-Onset Alzheimer's Disease
evidence:
- reference: PMID:10880397
  reference_title: 'Endocytic pathway abnormalities precede amyloid beta deposition in sporadic Alzheimer''s
    disease and Down syndrome: differential effects of APOE genotype and presenilin mutations.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: These abnormalities were evident in pyramidal neurons of the neocortex at preclinical stages
    of disease when Alzheimer-like neuropathology, such as Abeta deposition, was restricted to the entorhinal
    region.
  explanation: Human postmortem evidence that neuronal endosomal abnormality is present at preclinical
    stages, before neocortical amyloid deposition — the temporal ordering the model requires.
- reference: PMID:10880397
  reference_title: 'Endocytic pathway abnormalities precede amyloid beta deposition in sporadic Alzheimer''s
    disease and Down syndrome: differential effects of APOE genotype and presenilin mutations.'
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: By contrast, endosomes were normal in size at advanced stages of familial AD caused by mutations
    of presenilin 1 or 2, indicating that altered endocytosis is not a consequence of Abeta deposition.
  explanation: 'The paper''s own internal control cuts both ways: it shows the endosomal phenotype is
    not merely downstream of amyloid, but also that it is absent in presenilin-mutation familial disease,
    so the mechanism is not universal across Alzheimer genetic subtypes.'
- reference: PMID:15465622
  reference_title: 'Abeta localization in abnormal endosomes: association with earliest Abeta elevations
    in AD and Down syndrome.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Double-immunofluorescence using numerous Abeta antibodies showed that intracellular Abeta localized
    principally to rab5-positive endosomes in neurons from AD brains and was prominent in enlarged endosomes.
  explanation: Locates amyloid-beta inside the enlarged endosomal compartment in human Alzheimer brain,
    connecting the endosomal lesion to the peptide itself.
- reference: PMID:35654956
  reference_title: Faulty autolysosome acidification in Alzheimer's disease mouse models induces autophagic
    build-up of Aβ in neurons, yielding senile plaques.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Quantitative analyses confirm that individual neurons exhibiting PANTHOS are the principal
    source of senile plaques in amyloid precursor protein AD models.
  explanation: The load-bearing claim of the model — that the plaque originates from a single dying neuron
    — stated for amyloid precursor protein transgenic mouse models. The corresponding human claim in the
    same work is presence of the pattern, not that it is the source of human plaques.
- reference: PMID:37494443
  reference_title: Lysosomal dysfunction in Down syndrome and Alzheimer mouse models is caused by v-ATPase
    inhibition by Tyr(682)-phosphorylated APP βCTF.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Lowering APP-βCTF Tyr682 phosphorylation restores v-ATPase and lysosome function in DS fibroblasts
    and in vivo in brains of DS model mice.
  explanation: 'Supplies the molecular mechanism and its genetic rescue: APP-βCTF competitively inhibits
    the v-ATPase V0a1 subunit, so the acidification failure is caused by an APP fragment upstream of amyloid-beta
    itself.'
notes: 'EMERGING, and deliberately curated as a competitor to — not a restatement of — autophagy_lysosomal_clearance_model.
  That model says defective clearance lets amyloid accumulate; this one says the plaque is *generated*
  inside the autolysosomal compartment of a neuron that then dies. The distinction is testable and matters
  therapeutically: it predicts that lowering APP-βCTF or restoring v-ATPase activity acts upstream of
  anything an anti-amyloid antibody can reach. Held EMERGING because the human evidence is strong for
  the endosomal lesion (Cataldo, human postmortem) but thin for PANTHOS itself, where the only verified
  human statement is that the pattern is present in Alzheimer brains. The v-ATPase mechanism and the PANTHOS
  phenotype come from the same laboratory, so they are not independent replications of each other.'
```

## Curator-Supplied Candidate Datasets

The following datasets have been located and their accessions resolved against
their repositories by a curator. Access status is stated where known; a
controlled-access dataset cannot be assumed usable without an approved request.

All accessions below were resolved against the GEO API by the curator; each title
is quoted as GEO states it. All are open-access human post-mortem brain.

- **geo:GSE129308** - "Molecular signatures underlying neurofibrillary tangle susceptibility in Alzheimer's disease" (Homo sapiens, 27 samples, originating study PMID:35882228). Single somas with neurofibrillary tangles versus tangle-free somas from the SAME human AD brains. Relevant for asking whether endolysosomal and v-ATPase subunit programmes distinguish neurons that are accumulating pathology from neighbours that are not.
- **geo:GSE147528** - "Molecular characterization of selectively vulnerable neurons in Alzheimer's Disease" (Homo sapiens, PMID:33432193). Braak-staged entorhinal and frontal cortex snRNA-seq; the model claims endosomal abnormality is the EARLIEST intraneuronal change, so a stage-resolved dataset is the natural place to test whether endolysosomal programmes shift before other markers.
- **geo:GSE174367** - "Single-nucleus chromatin accessibility and transcriptomic characterization of Alzheimer's Disease" (Homo sapiens, 230 samples, PMID:34239132). Paired snRNA-seq and snATAC-seq for regulatory support of any endolysosomal expression change.
- **geo:GSE138852** - "A single-cell atlas of the human cortex reveals drivers of transcriptional changes in Alzheimer's disease in specific cell subpopulations" (Homo sapiens, PMID:31768052). Entorhinal cortex replication cohort.
- **geo:GSE157827** - "Single-nucleus transcriptome analysis reveals dysregulation of angiogenic endothelial cells and neuroprotective glia in Alzheimer's disease" (Homo sapiens, PMID:32989152). Independent cortical replication cohort.

Be direct about fitness for purpose here, because it is genuinely doubtful. The
core claims of this hypothesis are about organelle morphology, luminal pH,
v-ATPase subunit assembly, and where a peptide physically accumulates. None of
those is a transcript-abundance phenotype, and the APP-betaCTF mechanism is a
post-translational, protein-protein competition event that transcriptomics cannot
observe at all. Say clearly which listed datasets are unfit, and identify the data
types that WOULD discriminate the intraneuronal-origin model from the
extracellular-secretion model - for example quantitative human neuropathology of
plaque-associated neuronal remnants, proteomics of the autolysosomal compartment
(PRIDE), or pH- and organelle-resolved imaging - and state whether such data exist
publicly.

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
**Generated:** 2026-08-28T08:09:47.527572

1. PMID:10880397
2. PMID:31416668
3. PMID:27064279
4. PMID:33238112
5. PMID:40514243
6. PMID:35654956
7. PMID:37494443
8. PMID:35418158
9. PMID:41676572
10. PMID:26194181
11. PMID:36278355
12. PMID:35882228
13. PMID:33432193
14. PMID:34239132
15. PMID:31768052
16. PMID:32989152
17. PMID:15465622
18. PMID:35575522
19. PMID:31771055
20. PMID:35226190
21. PMID:34708251
22. PMID:24412310
23. PMID:42643714
24. PMID:24252153