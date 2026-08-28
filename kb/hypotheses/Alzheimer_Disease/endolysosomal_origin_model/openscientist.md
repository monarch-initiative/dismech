---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T06:45:30.991339'
end_time: '2026-08-28T08:09:47.527572'
duration_seconds: 5056.54
template_file: templates/hypothesis_deep_research_datasets.md
template_variables:
  disease_name: Alzheimer Disease
  category: Neurodegenerative Disorder
  hypothesis_group_id: endolysosomal_origin_model
  hypothesis_label: Endolysosomal Origin ("Inside-Out" Amyloid) Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: endolysosomal_origin_model\nhypothesis_label:\
    \ Endolysosomal Origin (\"Inside-Out\" Amyloid) Model\nstatus: EMERGING\ndescription:\
    \ Amyloid pathology is modeled as beginning inside the neuron rather than in the\
    \ extracellular\n  space. Endocytic-pathway activation with enlargement of Rab5-positive\
    \ early endosomes is the earliest\n  recognized neuronal change in sporadic Alzheimer\
    \ disease, preceding plaque deposition; APP-beta-C-terminal\n  fragment accumulation\
    \ then inhibits the lysosomal v-ATPase, autolysosomes fail to acidify, and amyloid-beta\n\
    \  builds up within de-acidified autolysosomes until the neuron ruptures and its\
    \ contents become the plaque\n  core (the PANTHOS pattern). Under this model the\
    \ senile plaque is the tombstone of a dead neuron, not\n  a deposit of secreted\
    \ peptide, which inverts the direction of the classical extracellular cascade.\n\
    applies_to_subtypes:\n- Early-Onset Alzheimer's Disease\n- Late-Onset Alzheimer's\
    \ Disease\nevidence:\n- reference: PMID:10880397\n  reference_title: 'Endocytic\
    \ pathway abnormalities precede amyloid beta deposition in sporadic Alzheimer''s\n\
    \    disease and Down syndrome: differential effects of APOE genotype and presenilin\
    \ mutations.'\n  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n  snippet:\
    \ These abnormalities were evident in pyramidal neurons of the neocortex at preclinical\
    \ stages\n    of disease when Alzheimer-like neuropathology, such as Abeta deposition,\
    \ was restricted to the entorhinal\n    region.\n  explanation: Human postmortem\
    \ evidence that neuronal endosomal abnormality is present at preclinical\n   \
    \ stages, before neocortical amyloid deposition \u2014 the temporal ordering the\
    \ model requires.\n- reference: PMID:10880397\n  reference_title: 'Endocytic pathway\
    \ abnormalities precede amyloid beta deposition in sporadic Alzheimer''s\n   \
    \ disease and Down syndrome: differential effects of APOE genotype and presenilin\
    \ mutations.'\n  supports: PARTIAL\n  evidence_source: HUMAN_CLINICAL\n  snippet:\
    \ By contrast, endosomes were normal in size at advanced stages of familial AD\
    \ caused by mutations\n    of presenilin 1 or 2, indicating that altered endocytosis\
    \ is not a consequence of Abeta deposition.\n  explanation: 'The paper''s own\
    \ internal control cuts both ways: it shows the endosomal phenotype is\n    not\
    \ merely downstream of amyloid, but also that it is absent in presenilin-mutation\
    \ familial disease,\n    so the mechanism is not universal across Alzheimer genetic\
    \ subtypes.'\n- reference: PMID:15465622\n  reference_title: 'Abeta localization\
    \ in abnormal endosomes: association with earliest Abeta elevations\n    in AD\
    \ and Down syndrome.'\n  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n\
    \  snippet: Double-immunofluorescence using numerous Abeta antibodies showed that\
    \ intracellular Abeta localized\n    principally to rab5-positive endosomes in\
    \ neurons from AD brains and was prominent in enlarged endosomes.\n  explanation:\
    \ Locates amyloid-beta inside the enlarged endosomal compartment in human Alzheimer\
    \ brain,\n    connecting the endosomal lesion to the peptide itself.\n- reference:\
    \ PMID:35654956\n  reference_title: Faulty autolysosome acidification in Alzheimer's\
    \ disease mouse models induces autophagic\n    build-up of A\u03B2 in neurons,\
    \ yielding senile plaques.\n  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n\
    \  snippet: Quantitative analyses confirm that individual neurons exhibiting PANTHOS\
    \ are the principal\n    source of senile plaques in amyloid precursor protein\
    \ AD models.\n  explanation: The load-bearing claim of the model \u2014 that the\
    \ plaque originates from a single dying neuron\n    \u2014 stated for amyloid\
    \ precursor protein transgenic mouse models. The corresponding human claim in\
    \ the\n    same work is presence of the pattern, not that it is the source of\
    \ human plaques.\n- reference: PMID:37494443\n  reference_title: Lysosomal dysfunction\
    \ in Down syndrome and Alzheimer mouse models is caused by v-ATPase\n    inhibition\
    \ by Tyr(682)-phosphorylated APP \u03B2CTF.\n  supports: SUPPORT\n  evidence_source:\
    \ MODEL_ORGANISM\n  snippet: Lowering APP-\u03B2CTF Tyr682 phosphorylation restores\
    \ v-ATPase and lysosome function in DS fibroblasts\n    and in vivo in brains\
    \ of DS model mice.\n  explanation: 'Supplies the molecular mechanism and its\
    \ genetic rescue: APP-\u03B2CTF competitively inhibits\n    the v-ATPase V0a1\
    \ subunit, so the acidification failure is caused by an APP fragment upstream\
    \ of amyloid-beta\n    itself.'\nnotes: 'EMERGING, and deliberately curated as\
    \ a competitor to \u2014 not a restatement of \u2014 autophagy_lysosomal_clearance_model.\n\
    \  That model says defective clearance lets amyloid accumulate; this one says\
    \ the plaque is *generated*\n  inside the autolysosomal compartment of a neuron\
    \ that then dies. The distinction is testable and matters\n  therapeutically:\
    \ it predicts that lowering APP-\u03B2CTF or restoring v-ATPase activity acts\
    \ upstream of\n  anything an anti-amyloid antibody can reach. Held EMERGING because\
    \ the human evidence is strong for\n  the endosomal lesion (Cataldo, human postmortem)\
    \ but thin for PANTHOS itself, where the only verified\n  human statement is that\
    \ the pattern is present in Alzheimer brains. The v-ATPase mechanism and the PANTHOS\n\
    \  phenotype come from the same laboratory, so they are not independent replications\
    \ of each other.'"
  candidate_datasets: 'All accessions below were resolved against the GEO API by the
    curator; each title

    is quoted as GEO states it. All are open-access human post-mortem brain.


    - **geo:GSE129308** - "Molecular signatures underlying neurofibrillary tangle
    susceptibility in Alzheimer''s disease" (Homo sapiens, 27 samples, originating
    study PMID:35882228). Single somas with neurofibrillary tangles versus tangle-free
    somas from the SAME human AD brains. Relevant for asking whether endolysosomal
    and v-ATPase subunit programmes distinguish neurons that are accumulating pathology
    from neighbours that are not.

    - **geo:GSE147528** - "Molecular characterization of selectively vulnerable neurons
    in Alzheimer''s Disease" (Homo sapiens, PMID:33432193). Braak-staged entorhinal
    and frontal cortex snRNA-seq; the model claims endosomal abnormality is the EARLIEST
    intraneuronal change, so a stage-resolved dataset is the natural place to test
    whether endolysosomal programmes shift before other markers.

    - **geo:GSE174367** - "Single-nucleus chromatin accessibility and transcriptomic
    characterization of Alzheimer''s Disease" (Homo sapiens, 230 samples, PMID:34239132).
    Paired snRNA-seq and snATAC-seq for regulatory support of any endolysosomal expression
    change.

    - **geo:GSE138852** - "A single-cell atlas of the human cortex reveals drivers
    of transcriptional changes in Alzheimer''s disease in specific cell subpopulations"
    (Homo sapiens, PMID:31768052). Entorhinal cortex replication cohort.

    - **geo:GSE157827** - "Single-nucleus transcriptome analysis reveals dysregulation
    of angiogenic endothelial cells and neuroprotective glia in Alzheimer''s disease"
    (Homo sapiens, PMID:32989152). Independent cortical replication cohort.


    Be direct about fitness for purpose here, because it is genuinely doubtful. The

    core claims of this hypothesis are about organelle morphology, luminal pH,

    v-ATPase subunit assembly, and where a peptide physically accumulates. None of

    those is a transcript-abundance phenotype, and the APP-betaCTF mechanism is a

    post-translational, protein-protein competition event that transcriptomics cannot

    observe at all. Say clearly which listed datasets are unfit, and identify the
    data

    types that WOULD discriminate the intraneuronal-origin model from the

    extracellular-secretion model - for example quantitative human neuropathology
    of

    plaque-associated neuronal remnants, proteomics of the autolysosomal compartment

    (PRIDE), or pH- and organelle-resolved imaging - and state whether such data exist

    publicly.'
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
citation_count: 24
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: evidence_matrix.csv
  path: openscientist_artifacts/evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
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
- filename: knowledge_gaps.csv
  path: openscientist_artifacts/knowledge_gaps.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist knowledge gaps
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


## Output

# Hypothesis-Search Report: Endolysosomal Origin ("Inside-Out" Amyloid) Model of Alzheimer Disease

**Hypothesis ID:** `endolysosomal_origin_model` · **KB status:** EMERGING
**Disease:** Alzheimer Disease (Neurodegenerative) · **Report date:** 2026-08-28 · Iteration 1

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — with a sharp asymmetry between the two halves of the causal chain.**

The model decomposes into an **upstream module** (APP-βCTF → APPL1/Rab5 hyperactivation → early-endosome enlargement, occurring *before* and *independent of* extracellular Aβ) and a **downstream module** (βCTF inhibits the lysosomal v-ATPase → autolysosome de-acidification → intraluminal Aβ build-up → PANTHOS rosette → neuronal rupture → the plaque core is the "tombstone" of a dead neuron).

- **The upstream module is well supported and independently replicated.** Human post-mortem evidence (Cataldo, PMID:10880397), human iPSC neurons from an independent lab (Kwart/Tessier-Lavigne, PMID:31416668), an independent axonal-trafficking lab (Xu/Wu, PMID:27064279), and gain-of-function mouse models (PA-Rab5, PMID:33238112; Thy1-APPL1, PMID:40514243) converge on the same conclusion: the endosomal lesion is the earliest AD-specific neuronal change and is driven by **βCTF, not Aβ**. This is strong.

- **The downstream module (v-ATPase inhibition + PANTHOS + "plaque = dead-neuron tombstone") is emerging and largely single-laboratory (Nixon).** The two load-bearing papers (PANTHOS, PMID:35654956; v-ATPase inhibition by Tyr682-βCTF, PMID:37494443) come from the same group and are not independent replications of each other. The strongest quantitative claim — that individual PANTHOS neurons are *the principal source* of senile plaques — is demonstrated in **APP-transgenic mice**, not in human brain, where only *presence of the pattern* is verified.

- **Scope limitation carried by the hypothesis's own evidence:** endosomes were normal in advanced **PSEN1/2 familial AD** (Cataldo, PMID:10880397), so the mechanism is not universal across genetic subtypes as an *endosome-size* readout — although iPSC work (PMID:31416668) shows PSEN1 mutants still accumulate βCTFs and enlarge endosomes, partly reconciling this.

**Most important caveat:** The core physical claims (organelle pH, v-ATPase subunit assembly, peptide sub-cellular location, plaque-to-neuron correspondence) are **imaging/proteomics/neuropathology phenotypes**. None of the curator-supplied transcriptomic datasets can adjudicate them. The model is therefore best described as *mechanistically compelling upstream, phenotypically documented downstream in mice, and not yet decisively demonstrated as the origin of the human plaque.*

**Iteration-3 update that shifts the balance slightly upward:** the single most discriminating *human* data type — **laser-capture plaque-core proteomics** — is public (Drummond 2022 PMID:35418158; Chu 2026 PMID:41676572), and it already reports that **endosomal/lysosomal proteins are particularly highly enriched within amyloid plaques**, with early lysosomal activation and autophagy/vesicle modules. This is qualitatively what the inside-out model predicts (the plaque contains endolysosomal remnants), though it does not yet exclude glial/dystrophic-neurite lysosomal contributions. The crux is thus **re-analyzable on existing public proteomics**, not a data-absence problem.

---

## Evidence Matrix

| # | Citation (PMID) | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | 10880397 (Cataldo 2000) | Human clinical (post-mortem) | **Supports** | Endosomal abnormality precedes Aβ deposition | Rab5+ early endosomes enlarged in neocortical pyramidal neurons at preclinical stages, before neocortical Aβ; APOE-ε4 accentuates | Sporadic AD, Down syndrome | High for temporal ordering; correlative, cross-sectional (not longitudinal) |
| 2 | 10880397 (Cataldo 2000) | Human clinical | **Qualifies** | Universality across genetic subtypes | Endosomes **normal** in advanced PSEN1/2 familial AD | Familial (PSEN) AD | High; bounds scope — endosome *size* readout not universal |
| 3 | 15465622 (Cataldo 2004) | Human clinical | **Supports** | Aβ physically localizes to the endosomal lesion | Intracellular Aβ localized principally to rab5+ enlarged endosomes | AD, DS brain | Moderate–high; antibody-dependent localization |
| 4 | 26194181 (Kim/Nixon 2016) | In vitro / model | **Supports** | Molecular driver of Rab5 overactivation | βCTF recruits APPL1 → stabilizes GTP-Rab5 → endosome swelling; APPL1 knockdown rescues (DS fibroblasts) | AD/DS | High mechanistically; Nixon lab |
| 5 | 31416668 (Kwart/Tessier-Lavigne 2019) | In vitro (human iPSC) | **Supports (independent)** | βCTF, not Aβ, causes endosome enlargement | Isogenic APP/PSEN1 mutants enlarge Rab5+ endosomes; correlates with βCTF not Aβ; rescued by BACE inhibition | fAD (APP, PSEN1) | High; **independent lab, human, isogenic** — key replication |
| 6 | 27064279 (Xu/Wu 2016) | Model organism / in vitro | **Supports (independent)** | APP/βCTF→Rab5 disrupts axonal trafficking | βCTF induces endosome enlargement + NGF axonal-transport block; rescued by dominant-negative Rab5 | AD/DS models | High; independent lab |
| 7 | 33238112 (Pensalfini/Nixon 2020) | Model organism | **Supports** | Rab5 overactivation alone is sufficient | PA-Rab5 mice reproduce endosome enlargement, synaptic deficits, tau-P, cholinergic degeneration, memory loss — distinct from Aβ | Mouse | High for sufficiency of upstream node |
| 8 | 40514243 / 39345644 (Jiang/Nixon 2025) | Model organism | **Supports** | APPL1 node is causal in vivo | Thy1-APPL1 mice: enlarged endosomes, LTP/LTD changes, basal-forebrain cholinergic degeneration, memory deficit | Mouse | Moderate–high; Nixon lab |
| 9 | 35654956 (Lee/Nixon 2022) | Model organism (+ human pattern) | **Supports** | Autolysosome de-acidification → intraneuronal Aβ → PANTHOS → plaque origin | Acidification declines before extracellular deposits; PANTHOS neurons are principal plaque source in APP models; pattern *present* in human AD | APP-Tg mice; human (pattern only) | Moderate; **plaque-origin claim is murine**; human = presence only; single lab |
| 10 | 37494443 (Im/Nixon 2023) | Model organism / in vitro | **Supports** | βCTF Tyr682-P inhibits v-ATPase V0a1 → acidification failure | Lowering βCTF Tyr682-P restores v-ATPase/lysosome function in DS fibroblasts and DS-model mouse brain | DS/AD models | Moderate; single lab; not independently replicated |
| 11 | 11403971 (Wirths/Bayer 2001) | Model organism | **Supports** | Intraneuronal Aβ precedes plaques | Intracellular Aβ precedes plaque deposition; disappears as plaques mature | APP×PSEN1 mice | Moderate; correlative; overexpression model |
| 12 | 24252153 (Antonios/Bayer 2013) | Model organism / human | **Qualifies** | Intraneuronal N-truncated Aβ | Aβ4-x precedes AβpE3-x intraneuronally pre-plaque; but antibody barely reacts with **human sporadic** plaques | 5XFAD; human | Moderate; human translation caveat |
| 13 | 36278355 (Pontrello 2022) | Model organism | **Competing/upstream** | What is *earliest*? | Oxidative redox (GSH loss) + metabolic (pAkt) shifts precede iAβ in 3xTg-AD | Mouse | Moderate; challenges "endosome is earliest" as sole primum movens |
| 14 | 35226190 (Mishra/Young 2022) | In vitro (human iPSC) | **Supports/complementary** | Endosomal recycling failure converges on swelling | SORL1 loss + APP/PSEN1 mutations pathogenically converge by swelling early endosomes; SORL1 regulates APP recycling | fAD genes | High; ties genetics to the endosomal node |
| 15 | 34708251 (Li 2021, review) | Review / GWAS synthesis | **Qualifies/competing** | Which pathway dominates risk | >130 loci enrich in *myeloid/immune*; BIN1, PICALM, SORL1, RIN3 implicate endocytosis but framed around **microglial Aβ clearance** | LOAD | Review-level; supports endocytosis relevance but favors clearance framing |
| 16 | 24412310 (Domert 2014) | In vitro (co-culture) | **Competing/complementary** | How Aβ spreads between cells | Neuritic cell-to-cell transfer of oligomeric Aβ is driven by *insufficient clearance* and intracellular accumulation, an early event preceding toxicity | 3D co-culture | Moderate; supports intracellular-origin-then-spread but via a clearance (not v-ATPase-origin) logic |
| 17 | 42643714 / 42552749 (2026, clinical) | Clinical / review | **Qualifies (competing)** | Is extracellular amyloid therapeutically inert? | Donanemab & lecanemab remove plaque and slow decline; benefit accrues in extension data (NCT04437511, NCT05738486, NCT03887455) | Early symptomatic AD | High trial evidence; **bounds the "plaque is a mere tombstone" claim** — extracellular amyloid is causally active |
| 18 | 35418158 (Drummond 2022) | Human (LCM proteomics) | **Supports** | Is the plaque made of endolysosomal material? | Endosomal/lysosomal proteins *particularly highly enriched* in plaques; validated ARL8B, moesin, ezrin, SMOC1 | Sporadic EOAD + DS-AD | Moderate; cannot separate neuronal vs glial lysosomal source |
| 19 | 41676572 (Chu 2026) | Human + mouse (single-plaque proteomics) | **Supports** | Temporal composition of plaque microenvironment | >7,000 proteins; *early immune and lysosomal activation*; autophagy/vesicle-organization modules | AD human + 5xFAD/APP-KI | Moderate; microenvironment ≠ neuronal-origin proof |
| 20 | 35575522 (Upadhyay 2022) / 31771055 (Bastrup 2020) | Methods / mouse proteomics | **Supports (enabling)** | Feasibility of plaque-core proteomics | Established purification + LC-MS/PTM workflows for plaque cores | Human + APPPS1 mouse | Enabling resource; the assay that could settle the crux exists |

---

## Mechanistic Causal Chain

```
[AD risk factors: APP/βCTF dose (DS, APP dup), APOE-ε4, SORL1/BIN1/PICALM/RIN3]
        │  STRONG (human PM + human iPSC + independent labs)
        ▼
APP-βCTF accumulation in endosomes ──recruits APPL1──► GTP-Rab5 stabilized/hyperactive
        │  STRONG, independently replicated (PMID:26194181, 31416668, 27064279)
        ▼
Early-endosome ENLARGEMENT  ◄── earliest AD-specific neuronal lesion; preclinical (PMID:10880397)
        │  STRONG for occurrence; sufficiency shown (PA-Rab5, PMID:33238112)
        ▼
βCTF (Tyr682-P) inhibits lysosomal v-ATPase (V0a1) ──► autolysosome DE-ACIDIFICATION
        │  EMERGING — single lab (PMID:37494443); post-translational; not RNA-visible
        ▼
Intraluminal Aβ build-up in de-acidified autolysosomes ──► PANTHOS perikaryal rosettes
        │  EMERGING — murine quantitation; human = pattern present only (PMID:35654956)
        ▼
Lysosomal membrane permeabilization → cathepsin release → lysosomal neuronal death
        │  INFERRED in human; shown in mouse
        ▼
Neuron ruptures; contents seed the PLAQUE CORE ("tombstone")  ◄── INVERTS classical cascade
        │  WEAKEST HUMAN LINK — plaque-origin demonstrated in APP mice, not human brain
        ▼
Extracellular plaque + microglial invasion → network dysfunction → dementia
```

**Where the literature is strong:** the top three edges (risk → βCTF/Rab5 → endosome enlargement), including human iPSC and independent-lab confirmation, and the *sufficiency* of Rab5/APPL1 nodes to produce neurodegeneration.

**Where links are inferred / murine-only:** the v-ATPase inhibition step (mechanistically elegant but single-lab), and the terminal claim that the human senile plaque *originates from* a single ruptured neuron. In human tissue only the *presence* of PANTHOS-like patterns and intraluminal Aβ is verified — not the quantitative source relationship.

**Missing causal steps:** (a) direct human demonstration that plaque cores co-register 1:1 with dead-neuron remnants; (b) independent (non-Nixon) replication of βCTF→v-ATPase competitive inhibition; (c) longitudinal ordering in humans (all human data are cross-sectional); (d) reconciliation of "endosome is earliest" with redox/metabolic changes reported still earlier in mice (PMID:36278355).

---

## Dataset-Anchored Analysis

> **Overarching finding (most important):** The seed hypothesis's decisive claims are about **organelle morphology, luminal pH, v-ATPase subunit assembly, and peptide sub-cellular localization**. The βCTF→v-ATPase event is **post-translational protein–protein competition** — *invisible to transcriptomics by construction*. Therefore **none of the five listed snRNA-seq/snATAC-seq datasets can adjudicate the intraneuronal-origin vs extracellular-secretion question.** They can, at most, test a weak derivative prediction: that *transcriptional programmes* for endolysosomal machinery and v-ATPase subunits are up-regulated earlier/more in pathology-bearing or vulnerable neurons. A positive result is **consistent but non-specific** (up-regulation could be compensatory to any lysosomal stress, including the competing clearance model); a null result **does not refute** a post-translational mechanism. This assay–phenotype mismatch is the single most curation-relevant conclusion of this report.

### 1. GSE129308 — Tangle vs tangle-free somas from the SAME AD brains (PMID:35882228)
- **Fitness:** *Best of the five for a within-neuron contrast*, but still an indirect proxy. Same-brain paired design controls donor-level confounds elegantly. However, NFT status is a *tau* phenotype; the model's earliest claim is *pre-tangle endosomal* change, so tangle-bearing somas may be **too late** in the cascade.
- **Specific analysis:** Paired differential expression (tangle+ vs tangle− somas), donor as blocking factor (paired Wilcoxon / mixed model with random donor effect). Score a curated endolysosomal/v-ATPase gene set (ATP6V0A1, ATP6V0C, ATP6V1 subunits, RAB5A, RAB7A, APPL1, EEA1, SORL1, PICALM, BIN1, CTSB/CTSD, LAMP1, SQSTM1, MAP1LC3B) by AUCell/module score. Covariates: none needed for donor (paired), but control soma-capture batch and RNA quality.
- **Discriminating prediction:** SUPPORT ≈ coordinated up-regulation of v-ATPase + Rab5-axis genes in tangle+ somas with effect size (module-score Δ) that is monotonic and specific vs a matched random gene set (permutation p<0.05, Cliff's δ>0.3). REFUTE/QUALIFY ≈ no enrichment, or enrichment indistinguishable from generic stress/heat-shock programmes. **Neither outcome tests the v-ATPase *inhibition* mechanism** — only whether the compartment is transcriptionally engaged.
- **Confounds / priors:** Published for tangle susceptibility, not for this pathway — a fresh analysis is defensible. LCM/soma-capture ambient contamination and low per-soma depth are major; signature choice will drive the answer.

### 2. GSE147528 — Braak-staged EC & frontal cortex snRNA-seq (PMID:33432193, Leng)
- **Fitness:** *The natural place to test the EARLIEST-change claim* because it is stage-resolved (Braak 0→6) with a selectively-vulnerable-neuron focus (EC excitatory layer II). Still a transcriptional proxy, but the staging is the model's key axis.
- **Specific analysis:** Within EC excitatory neurons, regress endolysosomal/v-ATPase module score on Braak stage (ordinal mixed model, random effect = donor). Test whether the module rises at *early* Braak (1–2) **before** amyloid/tau transcriptional markers and before glial activation. Covariates: age, sex, PMI, batch, ambient RNA (SoupX/CellBender), nuclei/cell depth, APOE if available.
- **Discriminating prediction:** SUPPORT ≈ significant positive stage slope emerging at Braak 1–2, *preceding* an equivalently-scored plaque/tau program (order-of-onset test). REFUTE/QUALIFY ≈ flat slope, or onset simultaneous/after tau, or effect confined to glia.
- **Confounds / priors:** Small donor n per stage → underpowered for early-stage slopes; EC layer-II neuron numbers are low; cell-type assignment ambiguity is real. Leng et al. already characterized vulnerable-neuron trajectories — re-deriving their selective-vulnerability signature is **not** a test of this hypothesis.

### 3. GSE174367 — Paired snRNA-seq + snATAC-seq (PMID:34239132, Morabito)
- **Fitness:** Adds *regulatory* support: does chromatin accessibility at endolysosomal/v-ATPase loci change concordantly? Useful only as corroboration of a transcriptional signal; **cannot** see protein-level v-ATPase inhibition.
- **Specific analysis:** In neuronal clusters, test differential accessibility (DA) at promoters/enhancers of the module genes (AD vs control) and correlate with matched DE; TF-motif enrichment (e.g., TFEB/MiT-family — the master lysosomal-biogenesis regulator). Covariates: age, sex, PMI, batch, FRiP/TSS-enrichment QC.
- **Discriminating prediction:** SUPPORT ≈ coordinated TFEB-driven accessibility gain at lysosomal/v-ATPase loci in AD neurons matching DE direction. QUALIFY ≈ accessibility changes without DE, or TFEB program equally invoked in the competing clearance model (non-discriminating). REFUTE is weak here — absence of regulatory change doesn't refute a post-translational mechanism.
- **Confounds:** 230 "samples" span both modalities/replicates; multiome-style linkage is inferential; ATAC ambient/doublets.

### 4. GSE138852 — Entorhinal cortex snRNA-seq (PMID:31768052, Grubman)
- **Fitness:** *Replication cohort only.* Early atlas, modest depth, no fine staging. Fit only to check reproducibility of any module-score AD-vs-control shift found in #2. Not independently decisive.
- **Specific analysis:** AD vs control neuronal module score, mixed model with donor random effect; covariates age/sex/PMI/batch/ambient.
- **Discriminating prediction:** SUPPORT ≈ same-direction module elevation replicating GSE147528. Null = weakens the transcriptional-proxy claim but not the core mechanism.
- **Confounds:** Low nuclei counts, strong batch/ambient; cell-type labels coarse.

### 5. GSE157827 — Prefrontal cortex snRNA-seq (PMID:32989152, Lau)
- **Fitness:** *Independent cortical replication cohort.* Same limitations as #4; PFC is later-affected than EC, so weaker for the earliest-change claim.
- **Specific analysis:** Identical replication design to #4; optionally test endothelial/vascular clusters only if a vascular-clearance competing model is being contrasted.
- **Discriminating prediction:** As #4 — corroborative, non-decisive.
- **Confounds:** Region mismatch to the "earliest = EC" claim; batch/ambient.

### Ranking (most → least decisive for moving the hypothesis)
1. **GSE147528** (stage-resolved; directly addresses the *earliest-change* prediction) — **run this first.**
2. **GSE129308** (within-brain paired contrast; strongest confound control).
3. **GSE174367** (regulatory corroboration).
4. **GSE138852 / GSE157827** (replication only; tied, least decisive).

**First analysis to run:** In **GSE147528**, an ordinal mixed-effects regression of an endolysosomal/v-ATPase module score on Braak stage *within EC excitatory neurons*, with an explicit **order-of-onset test** against amyloid/tau transcriptional programs, correcting for age/sex/PMI/ambient RNA. State up front: even a clean positive here is *corroborative, not confirmatory* of intraneuronal origin.

### Questions no listed dataset can settle — and the data that would
| Core claim | Discriminating data type | Public availability |
|---|---|---|
| Plaque core = ruptured-neuron remnant (origin) | Quantitative human neuropathology / 3D volumetric EM / spatial co-registration of plaque cores with neuronal-death markers & lipofuscin/organelle debris | Sparse; some human PANTHOS imaging in PMID:35654956; **no open quantitative human origin dataset found** |
| Autolysosomal Aβ + de-acidification | Organelle-resolved / pH-sensor imaging (mRFP-eGFP-LC3), CLEM | Exists in mouse (PMID:35654956); **human pH data absent publicly** |
| βCTF Tyr682-P competitively inhibits v-ATPase V0a1 | Compartment proteomics / phosphoproteomics of autolysosomes; native v-ATPase assembly (BN-PAGE, cryo-EM) | Plaque proteomes exist (below), but **no dataset resolving this specific PTM-driven interaction found** |
| Intraneuronal Aβ localization | Multiplex IF / expansion / spatial proteomics on human brain | Partial (PMID:15465622); no standardized public resource identified |
| **Composition of the plaque itself (is it endolysosomal debris?)** | **LCM plaque-core proteomics (PRIDE/ProteomeXchange)** | **EXISTS PUBLICLY — see below; this is the key correction to the earlier data-absence framing** |

**Important update (Iteration 3): the single most discriminating human data type DOES exist publicly.** Laser-capture-microdissection proteomics of human amyloid plaques has been published and deposited:
- **Drummond 2022 (PMID:35418158)** — plaque vs adjacent tissue in **sporadic EOAD and Down-syndrome AD**; 48 consistently enriched proteins; explicitly reports *"Endosomal/lysosomal proteins were particularly highly enriched in amyloid plaques,"* validating lysosomal **ARL8B**, moesin, ezrin, SMOC1. **Qualitatively supports** the inside-out prediction that the plaque contains neuronal endolysosomal compartment remnants.
- **Chu 2026 (PMID:41676572)** — single-plaque LCM-DIA-MS, >7,000 proteins from >200 plaques (human + 5xFAD/APP-KI); temporal profiling shows *"early immune and lysosomal activation"* and network modules in **vesicle organization and autophagy**.
- **Upadhyay/Savas 2022 (PMID:35575522)** and **Bastrup 2020 (PMID:31771055, mouse + PTM profiling)** — established plaque-core purification + proteomics protocols.

**Caveat that keeps this non-decisive:** endosomal/lysosomal protein enrichment in plaques is *consistent with* neuronal autolysosomal origin but does **not** exclude contribution from plaque-associated **microglia/astrocyte** lysosomes or **dystrophic neurites**. Discrimination requires **cellular deconvolution** of the plaque proteome (neuronal vs glial marker apportionment) and, ideally, direct quantitation of **APP-βCTF and specific v-ATPase V0a1 subunits (ATP6V0A1)** within the plaque core.

**Bottom line for the curator (revised):** transcriptomics remains the wrong instrument, but the crux is **no longer a data-absence problem** — the decisive human assay (plaque-core proteomics) is public in PRIDE/ProteomeXchange and *already leans supportive*. The highest-value human test is therefore a **re-analysis**: cell-type-deconvolved plaque-core proteomics testing whether neuronal endolysosomal/v-ATPase proteins (not merely glial lysosomal proteins) are enriched in early-stage plaques.

---

## Knowledge Gaps

| Gap | Scope | Why it matters | What was checked | What would resolve it |
|---|---|---|---|---|
| Independent replication of βCTF→v-ATPase inhibition | Downstream module | v-ATPase step + PANTHOS both from Nixon lab; not mutually independent | PubMed: PMID:37494443, 35654956 are the only primary sources | Non-Nixon lab reproducing Tyr682-βCTF → V0a1 inhibition (biochemistry/cryo-EM) |
| Human plaque-origin quantitation | Terminal claim | "Plaque = dead-neuron tombstone" is verified only in mice; human = pattern present | PMID:35654956 human statement is presence only | 3D EM / spatial co-registration of human plaque cores with neuronal remnants |
| Longitudinal ordering in humans | Whole chain | All human evidence cross-sectional; "earliest" is inferred from staging | PMID:10880397 (preclinical), 33432193 (Braak) | Longitudinal biomarker/imaging or serial pathology cohorts |
| Is the endosome truly *first*? | Upstream trigger | Redox/metabolic shifts precede iAβ in mice (PMID:36278355) | One competing mouse study found | Multi-omic earliest-event mapping in a single model |
| PSEN subtype discordance | Subtype scope | Cataldo: endosomes normal in advanced PSEN AD; iPSC: PSEN mutants still enlarge via βCTF | PMID:10880397 vs 31416668 | Stage-matched PSEN human tissue endosome quantitation |
| ~~Source/data absence: plaque/autolysosomal proteomics~~ **PARTIALLY RESOLVED (Iter 3)** | Dataset-level | The assay that could see the mechanism | **Public plaque proteomes found: PMID:35418158, 41676572, 35575522, 31771055** — endolysosomal enrichment already reported | Cell-type-deconvolved re-analysis + βCTF/ATP6V0A1 quantitation in plaque cores (not new data collection) |
| Therapeutic MoA prediction untested clinically | Intervention | Model predicts βCTF-lowering / v-ATPase restoration acts *upstream* of anti-amyloid antibodies | Not tested; BACE inhibitors failed clinically for other reasons | Trial stratified by βCTF/endosomal biomarker |

---

## Alternative / Competing Models

| Model | Relationship to seed | Note |
|---|---|---|
| **Classical extracellular amyloid cascade** (secreted Aβ oligomers → plaques → tau → death) | **Direct alternative** — opposite direction (outside-in) | Seed explicitly inverts it; anti-amyloid antibody efficacy (lecanemab/donanemab) targets extracellular/oligomeric Aβ and is partly downstream of what the seed model predicts |
| **Autophagy–lysosomal clearance-failure model** | **Sibling / partial overlap** | Same organelle, different logic: clearance model = *failure to remove* secreted/accumulated Aβ; seed = plaque *generated* intraluminally. Distinguishable by plaque origin |
| **SORL1 / retromer endosomal-recycling model** (PMID:35226190) | **Upstream cause / complementary** | Genetic lesion that *feeds* βCTF/endosome swelling — supports the upstream node; agnostic on plaque origin |
| **APPL1/Rab5 signaling-node model** (PMID:33238112, 40514243) | **Sub-module of the seed's upstream half** | Rab5 overactivation sufficient for degeneration independent of Aβ — strengthens upstream, silent on PANTHOS |
| **Redox/metabolic-first model** (PMID:36278355) | **Competing upstream trigger** | Places oxidative/metabolic shift *before* iAβ; challenges "endosome is earliest" |
| **Neuroimmune / microglial-clearance-failure (GWAS-driven)** (PMID:34708251) | **Parallel / competing** | GWAS enrichment in myeloid regulatory regions; frames endocytosis genes around microglial Aβ clearance rather than neuronal origin |
| **Clearance-dependent cell-to-cell Aβ spreading** (PMID:24412310) | **Complementary / competing** | Shares intracellular-accumulation premise but attributes spread to *insufficient clearance*, not autolysosomal genesis + rupture; distinguishable by whether Aβ egress requires neuronal death |
| **Extracellular/oligomer toxicity arm (anti-amyloid-validated)** (PMID:42643714, 42552749) | **Parallel, causally active** | Plaque removal slows decline, proving extracellular amyloid is not therapeutically inert; the inside-out model must coexist with, not replace, this arm |

---

## Discriminating Tests

**Runnable today on existing public data:**
- **HIGHEST VALUE — plaque-core proteomics re-analysis (Drummond PMID:35418158; Chu PMID:41676572):** apportion plaque-enriched endolysosomal proteins to neuronal vs microglial/astrocytic origin using cell-type marker panels; quantify APP-βCTF and ATP6V0A1/v-ATPase subunits in plaque cores vs adjacent tissue, stratified by early vs late plaques. *SUPPORT* = neuronal endolysosomal + v-ATPase proteins enriched in early plaque cores above glial lysosomal background; *REFUTE/QUALIFY* = enrichment attributable to glia/dystrophic neurites only. This directly targets the crux and the data are public.
- GSE147528 stage-resolved order-of-onset module analysis (see above) — best transcriptomic proxy (corroborative only).
- GSE129308 paired tangle±soma endolysosomal/v-ATPase module test (corroborative only).

**Require new samples / assays (decisive):**
1. **Human plaque-origin morphometry:** volumetric CLEM/expansion microscopy co-registering plaque cores with neuronal-death and organelle-debris markers across Braak stages. *Expected if seed true:* early plaques centered on single ruptured neurons; *if false:* cores dissociated from neuronal remnants, consistent with secreted deposition.
2. **Independent biochemical replication:** non-Nixon lab, cryo-EM/BN-PAGE of native v-ATPase ± Tyr682-P βCTF to confirm competitive V0a1 inhibition and genetic rescue.
3. **Human pH/organelle imaging:** fixed-brain lysosomal-pH proxies (cathepsin maturation, LAMP/v-ATPase assembly IF) in early-stage tissue.
4. **Stratified therapeutic test:** trial of βCTF-lowering (BACE modulation dosed to spare physiology) or v-ATPase-restoring agents in patients stratified by an endosomal/βCTF biomarker; seed predicts benefit upstream of anti-Aβ antibodies.

---

## Curation Leads (require curator verification)

**Candidate evidence references (verify exact abstract snippets against source):**
- **PMID:31416668** — *"endosomal dysfunction correlated with accumulation of β-CTF, not Aβ, and could be rescued by pharmacological modulation of β-secretase (BACE)."* → **SUPPORT, IN_VITRO (human iPSC), independent lab.** Add as independent replication of the upstream βCTF→endosome edge. *(Note: snippet failed automated validation on the β character — curator should re-quote from source.)*
- **PMID:26194181** — *"βCTF recruits APPL1 to rab5 endosomes, where it stabilizes active GTP-rab5, leading to pathologically accelerated endocytosis, endosome swelling."* → **SUPPORT, mechanism (APPL1 node).**
- **PMID:33238112** — *"Rab5 overactivation alone recapitulates diverse prodromal and degenerative features of AD."* → **SUPPORT, sufficiency of upstream node.**
- **PMID:27064279** — *"β-CTF alone induced atrophy of BFCNs that was rescued by the dominant-negative Rab5 mutant, Rab5S34N."* → **SUPPORT, independent lab.**
- **PMID:35226190** — *"loss of SORL1, as well as mutations in autosomal dominant AD genes APP and PSEN1/2, pathogenically converge by swelling early endosomes, AD's cytopathological hallmark."* → **SUPPORT/complementary, genetics→endosome.**
- **PMID:36278355** — *"The order of pathologic progression … was loss of GSH (oxidative redox shift) followed by a pAkt/tAkt metabolic shift in CA1, iAβ accumulation…"* → **QUALIFIES (competing earliest-event).**
- **PMID:24252153** — *"it barely reacted with plaques in the brain of sporadic AD patients"* → **QUALIFIES (human-translation caveat for intraneuronal-Aβ→plaque).**

**Candidate pathophysiology nodes/edges:**
- Node: `APP-βCTF (Tyr682-P)`; Edge: `βCTF —inhibits→ v-ATPase (V0a1/ATP6V0A1)` [EMERGING, single-lab].
- Edge: `βCTF —via APPL1→ Rab5 (GTP) —enlarges→ early endosome` [SUPPORTED, multi-lab].
- Edge: `SORL1 loss / retromer —feeds→ endosomal swelling` [SUPPORTED].
- Edge: `PANTHOS neuron —is-source-of→ senile plaque core` [EMERGING; murine only in human — restrict to MODEL_ORGANISM until human quantitation exists].

**Candidate ontology terms:** GO:0006914 (autophagy), GO:0007040 (lysosome organization), GO:0045324 (endosomal transport), GO:0016471 / v-ATPase complex (GO:0033176), CL: excitatory neuron (CL:0000679), entorhinal cortex layer II neuron; genes ATP6V0A1, ATP6V0C, RAB5A, APPL1, SORL1, PICALM, BIN1, RIN3, CTSD, LAMP1.

**Candidate subtype restrictions / status:**
- Keep **EMERGING**. Consider splitting: upstream endosomal module → could be elevated toward **SUPPORTED**; downstream PANTHOS/v-ATPase/plaque-origin → keep **EMERGING (single-lab, murine human-origin claim)**.
- Add subtype note: endosome-*size* phenotype attenuated in advanced PSEN familial AD (PMID:10880397) though βCTF mechanism persists in PSEN iPSC (PMID:31416668).

**Candidate knowledge_gaps / discussion prompts:** all seven rows of the Knowledge Gaps table, especially (a) single-lab dependence of v-ATPase+PANTHOS, (b) absent human plaque-origin quantitation, (c) assay–phenotype mismatch making transcriptomics non-discriminating.

**Candidate `datasets:` entries (accessions exactly as repositories state):**
- `geo:GSE147528` — verified open, snRNA-seq, Braak-staged EC/frontal — *use for earliest-change proxy test.*
- `geo:GSE129308` — verified open, tangle± soma paired — *within-brain proxy test.*
- `geo:GSE174367` — verified open, paired snRNA+snATAC — *regulatory corroboration.*
- `geo:GSE138852`, `geo:GSE157827` — verified open — *replication only.*
- **Unverified leads (curator to resolve accessions in PRIDE/ProteomeXchange — these are the highest-value additions for this hypothesis):**
  - Drummond et al. 2022, *"The amyloid plaque proteome in early onset Alzheimer's disease and Down syndrome"* (**PMID:35418158**) — LCM plaque-core proteomics, EOAD + DS; reports endosomal/lysosomal enrichment. *Curator: locate the ProteomeXchange/PRIDE identifier from the paper's data-availability statement.*
  - Chu et al. 2026, *"Single Plaque Proteomics…"* (**PMID:41676572**) — single-plaque LCM-DIA-MS, >7,000 proteins, human + 5xFAD/APP-KI. *Curator: resolve PRIDE accession.*
  - Upadhyay & Savas 2022 (**PMID:35575522**) and Bastrup 2020 (**PMID:31771055**) — plaque-core purification/proteomics methods + mouse plaque PTM dataset. *Mark unverified; resolve accessions.*
  - These are marked **unverified** — I did not resolve their repository accessions; a curator must confirm before curation.

---

## Provenance Artifacts (Iteration 2)
Machine-readable companions written alongside this report for curator review:
- `evidence_matrix.csv` — 18-row evidence table (PMID, type, stance, claim, finding, subtype, confidence).
- `knowledge_gaps.csv` — 7 known-unknowns with scope, what-was-checked, and resolver.
- `dataset_ranking.csv` — the five curator datasets with fitness-for-crux flag and decisiveness rank.
- `causal_chain.mmd` — Mermaid diagram of the causal chain with per-edge strength annotations and the anti-amyloid qualifier edge.

## Limitations of This Report
Literature-only iteration (no primary data files provided); the dataset analyses above are *proposed designs*, not executed computations. PubMed retrieval was rate-limited and query-sensitive; some relevant primary sources (e.g., original Cataldo 2004 PMID:15465622 abstract, additional non-Nixon PANTHOS replications) were taken from the seed YAML or single hits and should be re-verified. The single most consequential conclusion — that the curator-supplied transcriptomic datasets cannot adjudicate this hypothesis's crux — is robust to these limitations because it follows from the assay–phenotype mismatch, not from any specific search result.


## Artifacts

- [OpenScientist evidence matrix](openscientist_artifacts/evidence_matrix.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist knowledge gaps](openscientist_artifacts/knowledge_gaps.csv)