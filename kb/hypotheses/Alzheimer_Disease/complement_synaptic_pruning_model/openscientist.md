---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T06:45:31.262394'
end_time: '2026-08-28T07:54:33.743613'
duration_seconds: 4142.48
template_file: templates/hypothesis_deep_research_datasets.md
template_variables:
  disease_name: Alzheimer Disease
  category: Neurodegenerative Disorder
  hypothesis_group_id: complement_synaptic_pruning_model
  hypothesis_label: Complement-Dependent Microglial Synapse Elimination Model
  hypothesis_status: ALTERNATIVE
  hypothesis_yaml: "hypothesis_group_id: complement_synaptic_pruning_model\nhypothesis_label:\
    \ Complement-Dependent Microglial Synapse Elimination Model\nstatus: ALTERNATIVE\n\
    description: Synapse loss \u2014 the pathological change that correlates best\
    \ with cognitive decline \u2014 is modeled\n  as an active, receptor-mediated\
    \ phagocytic process rather than as passive degeneration secondary to\n  amyloid\
    \ or tau toxicity. The classical complement cascade that prunes surplus synapses\
    \ during development\n  (C1q tagging, C3 opsonization, microglial CR3 engagement)\
    \ is modeled as being reactivated early in disease,\n  so that microglia engulf\
    \ structurally intact synapses. Soluble amyloid-beta oligomers and phosphorylated\n\
    \  tau both act as upstream triggers, which makes this the mechanism by which\
    \ two otherwise separate proteinopathies\n  converge on the same cellular endpoint.\n\
    applies_to_subtypes:\n- Early-Onset Alzheimer's Disease\n- Late-Onset Alzheimer's\
    \ Disease\nevidence:\n- reference: PMID:27033548\n  reference_title: Complement\
    \ and microglia mediate early synapse loss in Alzheimer mouse models.\n  supports:\
    \ SUPPORT\n  evidence_source: MODEL_ORGANISM\n  snippet: C1q, the initiating protein\
    \ of the classical complement cascade, is increased and associated\n    with synapses\
    \ before overt plaque deposition.\n  explanation: Places complement tagging of\
    \ synapses upstream of plaque deposition, which is what distinguishes\n    this\
    \ model from synapse loss as a late consequence of established amyloid pathology.\n\
    - reference: PMID:27033548\n  reference_title: Complement and microglia mediate\
    \ early synapse loss in Alzheimer mouse models.\n  supports: SUPPORT\n  evidence_source:\
    \ MODEL_ORGANISM\n  snippet: Inhibition of C1q, C3, or the microglial complement\
    \ receptor CR3 reduces the number of phagocytic\n    microglia, as well as the\
    \ extent of early synapse loss.\n  explanation: Blocking three separate steps\
    \ of the same cascade each reduces synapse loss, establishing\n    the pathway\
    \ as required rather than merely present.\n- reference: PMID:30392797\n  reference_title:\
    \ Changes in the Synaptic Proteome in Tauopathy and Rescue of Tau-Induced Synapse\
    \ Loss\n    by C1q Antibodies.\n  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n\
    \  snippet: At synapses, C1q decorated perisynaptic membranes, accumulated in\
    \ correlation with phospho-Tau,\n    and was associated with augmented microglial\
    \ engulfment of synapses and decline of synapse density.\n  explanation: Independent\
    \ laboratory, and a tau rather than amyloid driver, reaching the same C1q-microglia-synapse\n\
    \    axis \u2014 the strongest evidence that the model is not specific to amyloid\
    \ models.\n- reference: PMID:28566429\n  reference_title: Complement C3 deficiency\
    \ protects against neurodegeneration in aged plaque-rich APP/PS1\n    mice.\n\
    \  supports: PARTIAL\n  evidence_source: MODEL_ORGANISM\n  snippet: We found that\
    \ 16-month-old APP/PS1;C3 KO mice performed better on a learning and memory task\n\
    \    than did APP/PS1 mice, despite having more cerebral A\u03B2 plaques.\n  explanation:\
    \ 'Qualifies the model in an important direction: removing complement protects\
    \ synapses and\n    cognition while *increasing* plaque burden, so complement\
    \ is simultaneously protective for amyloid\n    clearance and harmful for synapses.\
    \ The model must not be read as \"complement is uniformly pathogenic\".'\n- reference:\
    \ PMID:37652017\n  reference_title: Human astrocytes and microglia show augmented\
    \ ingestion of synapses in Alzheimer's\n    disease via MFG-E8.\n  supports: PARTIAL\n\
    \  evidence_source: HUMAN_CLINICAL\n  snippet: Here we observe astrocytes and\
    \ microglia from human brains contain greater amounts of synaptic\n    protein\
    \ in AD compared with non-disease controls, and that proximity to amyloid-\u03B2\
    \ plaques and the\n    APOE4 risk gene exacerbate this effect.\n  explanation:\
    \ Confirms in human tissue that glia ingest synapses in Alzheimer disease, but\
    \ nominates\n    MFG-E8 rather than complement as the opsonin and puts astrocytes\
    \ alongside microglia \u2014 so it corroborates\n    the phenomenon while leaving\
    \ the molecular pathway open in humans.\nnotes: ALTERNATIVE rather than CANONICAL.\
    \ The necessity evidence (C1q, C3 and CR3 blockade) is entirely\n  mouse; the\
    \ same paper that supplies the best human evidence for glial synapse ingestion\
    \ states that\n  direct human evidence for glial involvement in synapse removal\
    \ remained to be established, and implicates\n  MFG-E8 rather than complement.\
    \ Curated as a distinct hypothesis group rather than folded into neuroimmune_glial_amplification_model\n\
    \  because it makes a specific, falsifiable claim about a named cascade acting\
    \ on a named substrate (the\n  synapse), and because its therapeutic prediction\
    \ \u2014 anti-C1q antibody \u2014 is being tested clinically. See\n  the attached\
    \ HUMAN_MODEL_MISMATCH discussion before strengthening the human claim."
  candidate_datasets: 'All accessions below were resolved against the GEO API by the
    curator; each title

    is quoted as GEO states it. All are open-access human post-mortem brain.


    - **geo:GSE148822** - "Distinct amyloid-b and tau associated microglia profiles
    in Alzheimer''s disease" (Homo sapiens, 95 samples, PMID:33609158). Human single-nucleus
    microglial profiling that separates amyloid-associated from tau-associated microglial
    states. Directly relevant because this hypothesis claims amyloid and tau converge
    on one complement-dependent execution step; a dataset that resolves the two contexts
    separately can test whether complement genes are induced in both.

    - **geo:GSE160936** - "Diverse human astrocyte and microglial transcriptional
    responses to Alzheimer''s pathology" (Homo sapiens, 24 samples, PMID:34767070).
    Profiles astrocytes AND microglia. The human evidence for glial synapse ingestion
    (PMID:37652017) implicates astrocytes alongside microglia and nominates MFG-E8
    rather than complement, so a dataset covering both glial classes is where that
    competing assignment can be examined.

    - **geo:GSE254205** - "APOE4/4 is linked to damaging lipid droplets in Alzheimer''s
    microglia" (Homo sapiens, 102 samples, PMID:38480892). APOE-genotyped human microglial
    states; the human synapse-ingestion study reports that APOE4 exacerbates glial
    synaptic-protein ingestion, so genotype-stratified microglial data bear on that
    interaction.

    - **geo:GSE174367** - "Single-nucleus chromatin accessibility and transcriptomic
    characterization of Alzheimer''s Disease" (Homo sapiens, 230 samples, PMID:34239132).
    Paired snRNA-seq and snATAC-seq, allowing complement-gene induction to be checked
    for regulatory support rather than transcript abundance alone.

    - **geo:GSE147528** - "Molecular characterization of selectively vulnerable neurons
    in Alzheimer''s Disease" (Homo sapiens, PMID:33432193). Braak-staged entorhinal
    and frontal cortex; relevant to the model''s claim that complement tagging happens
    EARLY, before overt plaque deposition.


    State plainly the central limitation of all of these for this hypothesis:

    complement-dependent synapse elimination is a protein-opsonization and

    phagocytosis phenotype, and transcript abundance of C1QA, C3, ITGAM or MFGE8 is

    at best an indirect proxy for it. Say explicitly which sub-claims transcriptomics

    could address (cell-type and stage specificity of complement-gene induction;

    whether the MFG-E8 and complement routes are expressed in the same cells) and

    which it cannot (whether synapses are actually engulfed, and by which opsonin).

    Name the data type that would settle the latter.'
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
- **Hypothesis ID:** complement_synaptic_pruning_model
- **Hypothesis Label:** Complement-Dependent Microglial Synapse Elimination Model
- **Status in KB:** ALTERNATIVE

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: complement_synaptic_pruning_model
hypothesis_label: Complement-Dependent Microglial Synapse Elimination Model
status: ALTERNATIVE
description: Synapse loss — the pathological change that correlates best with cognitive decline — is modeled
  as an active, receptor-mediated phagocytic process rather than as passive degeneration secondary to
  amyloid or tau toxicity. The classical complement cascade that prunes surplus synapses during development
  (C1q tagging, C3 opsonization, microglial CR3 engagement) is modeled as being reactivated early in disease,
  so that microglia engulf structurally intact synapses. Soluble amyloid-beta oligomers and phosphorylated
  tau both act as upstream triggers, which makes this the mechanism by which two otherwise separate proteinopathies
  converge on the same cellular endpoint.
applies_to_subtypes:
- Early-Onset Alzheimer's Disease
- Late-Onset Alzheimer's Disease
evidence:
- reference: PMID:27033548
  reference_title: Complement and microglia mediate early synapse loss in Alzheimer mouse models.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: C1q, the initiating protein of the classical complement cascade, is increased and associated
    with synapses before overt plaque deposition.
  explanation: Places complement tagging of synapses upstream of plaque deposition, which is what distinguishes
    this model from synapse loss as a late consequence of established amyloid pathology.
- reference: PMID:27033548
  reference_title: Complement and microglia mediate early synapse loss in Alzheimer mouse models.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Inhibition of C1q, C3, or the microglial complement receptor CR3 reduces the number of phagocytic
    microglia, as well as the extent of early synapse loss.
  explanation: Blocking three separate steps of the same cascade each reduces synapse loss, establishing
    the pathway as required rather than merely present.
- reference: PMID:30392797
  reference_title: Changes in the Synaptic Proteome in Tauopathy and Rescue of Tau-Induced Synapse Loss
    by C1q Antibodies.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: At synapses, C1q decorated perisynaptic membranes, accumulated in correlation with phospho-Tau,
    and was associated with augmented microglial engulfment of synapses and decline of synapse density.
  explanation: Independent laboratory, and a tau rather than amyloid driver, reaching the same C1q-microglia-synapse
    axis — the strongest evidence that the model is not specific to amyloid models.
- reference: PMID:28566429
  reference_title: Complement C3 deficiency protects against neurodegeneration in aged plaque-rich APP/PS1
    mice.
  supports: PARTIAL
  evidence_source: MODEL_ORGANISM
  snippet: We found that 16-month-old APP/PS1;C3 KO mice performed better on a learning and memory task
    than did APP/PS1 mice, despite having more cerebral Aβ plaques.
  explanation: 'Qualifies the model in an important direction: removing complement protects synapses and
    cognition while *increasing* plaque burden, so complement is simultaneously protective for amyloid
    clearance and harmful for synapses. The model must not be read as "complement is uniformly pathogenic".'
- reference: PMID:37652017
  reference_title: Human astrocytes and microglia show augmented ingestion of synapses in Alzheimer's
    disease via MFG-E8.
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: Here we observe astrocytes and microglia from human brains contain greater amounts of synaptic
    protein in AD compared with non-disease controls, and that proximity to amyloid-β plaques and the
    APOE4 risk gene exacerbate this effect.
  explanation: Confirms in human tissue that glia ingest synapses in Alzheimer disease, but nominates
    MFG-E8 rather than complement as the opsonin and puts astrocytes alongside microglia — so it corroborates
    the phenomenon while leaving the molecular pathway open in humans.
notes: ALTERNATIVE rather than CANONICAL. The necessity evidence (C1q, C3 and CR3 blockade) is entirely
  mouse; the same paper that supplies the best human evidence for glial synapse ingestion states that
  direct human evidence for glial involvement in synapse removal remained to be established, and implicates
  MFG-E8 rather than complement. Curated as a distinct hypothesis group rather than folded into neuroimmune_glial_amplification_model
  because it makes a specific, falsifiable claim about a named cascade acting on a named substrate (the
  synapse), and because its therapeutic prediction — anti-C1q antibody — is being tested clinically. See
  the attached HUMAN_MODEL_MISMATCH discussion before strengthening the human claim.
```

## Curator-Supplied Candidate Datasets

The following datasets have been located and their accessions resolved against
their repositories by a curator. Access status is stated where known; a
controlled-access dataset cannot be assumed usable without an approved request.

All accessions below were resolved against the GEO API by the curator; each title
is quoted as GEO states it. All are open-access human post-mortem brain.

- **geo:GSE148822** - "Distinct amyloid-b and tau associated microglia profiles in Alzheimer's disease" (Homo sapiens, 95 samples, PMID:33609158). Human single-nucleus microglial profiling that separates amyloid-associated from tau-associated microglial states. Directly relevant because this hypothesis claims amyloid and tau converge on one complement-dependent execution step; a dataset that resolves the two contexts separately can test whether complement genes are induced in both.
- **geo:GSE160936** - "Diverse human astrocyte and microglial transcriptional responses to Alzheimer's pathology" (Homo sapiens, 24 samples, PMID:34767070). Profiles astrocytes AND microglia. The human evidence for glial synapse ingestion (PMID:37652017) implicates astrocytes alongside microglia and nominates MFG-E8 rather than complement, so a dataset covering both glial classes is where that competing assignment can be examined.
- **geo:GSE254205** - "APOE4/4 is linked to damaging lipid droplets in Alzheimer's microglia" (Homo sapiens, 102 samples, PMID:38480892). APOE-genotyped human microglial states; the human synapse-ingestion study reports that APOE4 exacerbates glial synaptic-protein ingestion, so genotype-stratified microglial data bear on that interaction.
- **geo:GSE174367** - "Single-nucleus chromatin accessibility and transcriptomic characterization of Alzheimer's Disease" (Homo sapiens, 230 samples, PMID:34239132). Paired snRNA-seq and snATAC-seq, allowing complement-gene induction to be checked for regulatory support rather than transcript abundance alone.
- **geo:GSE147528** - "Molecular characterization of selectively vulnerable neurons in Alzheimer's Disease" (Homo sapiens, PMID:33432193). Braak-staged entorhinal and frontal cortex; relevant to the model's claim that complement tagging happens EARLY, before overt plaque deposition.

State plainly the central limitation of all of these for this hypothesis:
complement-dependent synapse elimination is a protein-opsonization and
phagocytosis phenotype, and transcript abundance of C1QA, C3, ITGAM or MFGE8 is
at best an indirect proxy for it. Say explicitly which sub-claims transcriptomics
could address (cell-type and stage specificity of complement-gene induction;
whether the MFG-E8 and complement routes are expressed in the same cells) and
which it cannot (whether synapses are actually engulfed, and by which opsonin).
Name the data type that would settle the latter.

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

# Complement-Dependent Microglial Synapse Elimination in Alzheimer Disease
## A Dataset-Anchored Mechanistic Hypothesis Search

**Hypothesis ID:** `complement_synaptic_pruning_model` · **KB status:** ALTERNATIVE
**Disease:** Alzheimer Disease (Neurodegenerative Disorder) · **Search date:** 2026-08-28
**Iterations:** 3 · **Literature reviewed:** 33 records · **Findings recorded:** 5

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — strongly in model organisms, correlatively in humans, with the single decisive step (glial engulfment of *intact* synapses by *complement*) still unproven in human tissue.**

The hypothesis is one of the best-evidenced mechanistic models in AD, but its evidentiary weight is unevenly distributed across the causal chain:

1. **The necessity arm is robust — in mice.** Independent laboratories show that genetic or antibody blockade of C1q, C3, or CR3 each reduces microglial synapse engulfment and early synapse loss, for **both** amyloid (Hong 2016, PMID:27033548; Shi 2017, PMID:28566429; Wu 2019, PMID:31433986; Petrisko 2025, PMID:41000995) and tau (Dejanovic 2018, PMID:30392797; Wu 2019; Nimmo 2026, PMID:42271460) drivers. Blocking three separate cascade steps and getting the same rescue is strong causal evidence that the pathway is *required*, not merely present. This directly supports the model's signature claim that two proteinopathies converge on one complement-dependent execution step.

2. **Human evidence is now stronger than the seed YAML implies, but remains correlative.** Beyond the YAML's single human citation (Tzioras 2023, PMID:37652017), the search surfaced: (a) C3 elevated in AD brain and at synapses, and in CSF correlating with tau (Wu 2019, PMID:31433986); (b) CSF C3/C4/CR1 elevations tracking disease progression (Daborg 2012, PMID:22488444); (c) **human common-variant genetics independently implicating the classical complement pathway** through CR1 and CLU loci (Rajabli 2025, PMID:40676597; meta-analysis PMID:29504051); (d) plasma C1q/clusterin elevated and predictive across EOAD and LOAD (Veteleanu 2023, PMID:37480051); and (e) complement tagging of synapses with loss of the CSMD1 checkpoint in **human** tauopathy tissue (Nimmo 2026, PMID:42271460). Genetics is the most causally weighty human evidence because it is not downstream of pathology.

3. **The unresolved core.** No human study demonstrates that microglia (or astrocytes) actually *phagocytose structurally intact synapses* **via complement opsonization**. The one study that directly demonstrates human glial synapse *ingestion* attributes it to **MFG-E8, not complement** (Tzioras 2023), and adds astrocytes as a second effector cell. So the phenomenon (glia eat synapses in AD) is established in humans; the *opsonin identity* and the *"intact synapse"* claim are not.

**Most important caveats:**
- **Human-model mismatch:** all necessity/sufficiency (perturbation) evidence is rodent. Human data are association-only.
- **Opsonin ambiguity:** complement vs MFG-E8 vs GAS6/MERTK vs phosphatidylserine routes are not resolved in humans; they may be parallel or cell-type-specific.
- **Directional qualifier:** complement is simultaneously *protective* (amyloid clearance; C3 KO increases plaque burden — Shi 2017) and *harmful* (synapse pruning). The model must not be read as "complement is uniformly pathogenic."
- **Transcriptomics cannot close the gap:** the curator-supplied datasets (all snRNA/snATAC) can address *where and when* complement genes turn on, but **cannot** show engulfment or identify the operative opsonin.

Retaining the **ALTERNATIVE** status is correct. The model is not CANONICAL because the executing step is unproven in humans and a named competitor (MFG-E8) has the only direct human phagocytosis evidence.

---

## Evidence Matrix

| # | Citation (PMID) | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | 27033548 (Hong 2016) | Model organism | **Supports** | C1q/C3/CR3 required for early synapse loss; Aβ-oligomer trigger | C1q rises at synapses before plaques; blocking C1q/C3/CR3 reduces phagocytic microglia & synapse loss; C1q necessary for Aβ-oligomer synaptotoxicity & LTP deficit | Amyloid models (J20, APP/PS1); "early" pre-plaque | High for mouse; foundational. No human perturbation. |
| 2 | 30392797 (Dejanovic 2018) | Model organism | **Supports** | Tau (not amyloid) drives C1q synapse tagging; anti-C1q rescues | C1q accumulates at PSDs correlating with p-tau; anti-C1q antibody restores synapse density | Tauopathy (Tau-P301S); also AD tissue immunostain | High for mouse. Human data limited to staining. |
| 3 | 31433986 (Wu 2019) | Model organism + human tissue/CSF | **Supports** | C3 required for neurodegeneration in amyloidosis & tauopathy; human relevance | C3 deletion rescues synapse loss (PS2APP) & atrophy (TauP301S); C3 elevated in human AD brain/synapses & CSF, correlates with tau | Both drivers; human LOAD tissue | High (mouse causal) + moderate (human correlative). |
| 4 | 41000995 (Petrisko 2025) | Model organism | **Supports** | *Microglial-specific* C1q is the source | Cx3cr1-driven microglial C1q deletion reduces synapse engulfment & prevents cognitive impairment (Arctic AD model) | Aggressive amyloid model | High; isolates microglial C1q, avoids developmental confound. |
| 5 | 42271460 (Nimmo 2026) | Model organism + human tissue | **Supports / extends** | Complement tags synapses in *amyloid-free* tauopathy; regulator loss | ↑C4/C2/C3ar1/ITGAM/Cd11c; C1q on tau aggregates & on excitatory synapses (independent of aggregate proximity); CSMD1 checkpoint lost on C1q+ synapses; human tauopathy tissue | Pure tauopathies + human | Moderate–high; human arm is staining. Strengthens amyloid-independence. |
| 6 | 37442133 (Zhong 2023) | Model organism + human tissue | **Qualifies** | AD risk gene TREM2 restrains the cascade | TREM2 binds C1q; TREM2-C1q complexes in human AD brain → lower C3, higher synaptic protein; Trem2 haploinsufficiency ↑ engulfment | Tau model + human AD | Moderate–high. Establishes a gating node; links to TREM2 model. |
| 7 | 36989373 (Zhou 2023) | Model organism + human CSF | **Qualifies** | Neuronal NPTX2 restrains C1q; loss de-represses pruning | Nptx2 loss ↑ C1q-dependent engulfment; ↓Nptx2/Nptx2-C1q in symptomatic FTD CSF ↔ ↑C1q/activated C3 | Neurodegeneration/FTD; AD-adjacent | Moderate. Human arm is FTD CSF, not AD. |
| 8 | 28566429 (Shi 2017) | Model organism | **Qualifies (bidirectional)** | Complement is protective for amyloid, harmful for synapses | C3 KO improves memory in aged APP/PS1 *despite more plaques* | Aged plaque-rich amyloid model | High. Key caveat against "complement uniformly bad." |
| 9 | 37652017 (Tzioras 2023) | Human clinical + in vitro | **Qualifies / competing** | Human glia ingest synapses — via **MFG-E8**, not complement | Human astrocytes+microglia contain more synaptic protein in AD; APOE4 & plaque proximity exacerbate; MFG-E8 inhibition rescues uptake | Human AD; APOE4 | High for phenomenon; **directly nominates a competing opsonin**. States direct human evidence for glial synapse removal was previously lacking. |
| 10 | 40676597 (Rajabli 2025) | Human genetic (GWAS) | **Supports (causal-genetic)** | Complement pathway is causally upstream | 56,241 individuals; CR1 & CLU loci; pathway analysis implicates classical complement | LOAD, multi-ancestry | High for "complement biology"; low specificity to *synaptic* C1q. |
| 11 | 37480051 (Veteleanu 2023) | Human clinical (proteomic) | **Supports** | Complement proteins altered in AD blood; genotype-linked | ↑Clusterin & C1q, ↓sCR1 & factor H in AD plasma; C1q best single predictor; CR1/CLU/C1S SNPs set protein levels | EOAD (n=912) + LOAD (n=492) | Moderate. Plasma, not brain; modest AUC. |
| 12 | 22488444 (Daborg 2012) | Human clinical (CSF) | **Supports** | CSF complement tracks AD/MCI-AD | ↑C3/C4 in AD vs stable MCI; ↑CR1 in MCI-AD/AD | LOAD, MCI converters | Moderate; "not diagnostically useful"; correlative. |
| 13 | 32460813 (Konijnenberg 2020) | Human clinical (CSF proteomic) | **Supports / qualifies** | Complement changes precede synaptic decline, APOE4-dependent | APOE4 carriers show complement-pathway CSF changes when cognition normal, synaptic-protein loss later | LOAD, APOE4-stratified | Moderate. Timing supports "early"; observational. |
| 14 | 36906076 (Cangalaya 2023) | Model organism (in vivo imaging) | **Supports** | Real-time microglial spine elimination correlates with complement/phagocytic proteins | LPS or AD-brain-extract prolongs microglia-spine contact; elimination tracks complement/phagocytic protein expression | Acute inflammation/tauopathy | Moderate; acute models, correlational with complement. |

*Evidence types per instruction: human clinical, model organism, in vitro, computational, review. No computational/omics-derived causal evidence exists yet; reviews (e.g., PMID:42393750 "microglial checkpoint collapse," PMID:42614559) are orientation only and are labeled review-level.*

---

## Mechanistic Causal Chain

```
[Soluble Aβ oligomers]  and/or  [phospho-tau]        ← UPSTREAM TRIGGERS
        │  (STRONG in mouse; human = correlation)
        ▼
[Neuronal/synaptic stress; loss of restraint:            ← GATING NODES
   ↓NPTX2, ↓CSMD1, ↓TREM2 function, APOE4]
        │  (mouse strong; human genetic support for TREM2/CR1/CLU/APOE)
        ▼
[C1q deposition on peri-synaptic membranes]              ← TAGGING
        │  (mouse strong; human = immunostaining only)
        ▼
[C3 cleavage → iC3b opsonization of synapse]             ← OPSONIZATION
        │  (mouse strong; human C3 elevated/at synapses, correlative)
        ▼
[Microglial CR3 (ITGAM/CD11b-CD18) engagement]           ← RECOGNITION
        │  (mouse strong; ITGAM ↑ in human tauopathy tissue)
        ▼
[Phagocytic engulfment of STRUCTURALLY INTACT synapse]   ← EXECUTION  ★ MISSING HUMAN LINK ★
        │  (mouse: engulfment shown; "intact" inferred.
        │   human: glia contain synaptic protein, but opsonin = MFG-E8 shown, complement NOT shown)
        ▼
[Net synapse density loss]                               ← the best correlate of…
        │  (human: synapse loss ↔ cognition, well established)
        ▼
[Cognitive decline / dementia]                           ← CLINICAL ENDPOINT
```

**Where the literature is strong:** trigger→tagging→opsonization→engulfment in mouse (every edge perturbed); synapse-loss→cognition in human; and the *upstream genetic* nodes (CR1, CLU, TREM2, APOE) in human.

**Where links are inferred:** that the engulfed synapses are *functionally intact* rather than already-degenerating (the "active pruning vs passive clean-up" distinction) — supported by pre-plaque timing in mice but not directly shown in humans.

**Missing causal steps (human):**
1. Complement-dependent (not MFG-E8-dependent) engulfment of synapses in human tissue — no direct evidence.
2. That C1q/C3 tagging *precedes* rather than *follows* synapse degeneration in humans (temporal ordering; requires staged tissue or longitudinal biomarkers).
3. That anti-C1q/anti-C3 therapy preserves human synapses/cognition — the definitive interventional test, not yet reported positive.

---

## Dataset-Anchored Analysis

> **Central limitation stated up front (applies to ALL five datasets).** Complement-dependent synapse elimination is a **protein-opsonization + phagocytosis** phenotype. Every listed dataset is **single-nucleus transcriptomics (snRNA-seq ± snATAC-seq) from post-mortem tissue**. Transcript abundance of `C1QA/B/C`, `C3`, `ITGAM (CR3)`, `C3AR1`, or `MFGE8` is **at best an indirect proxy** for opsonization and engulfment. Moreover, single-nucleus prep **loses cytoplasmic and phagocytosed material** (engulfed synaptic protein lives in the cytoplasm/phagolysosome, not the nucleus), so these data are structurally blind to the very phenotype in question.
>
> **What transcriptomics CAN address:** (i) cell-type specificity — are `C1QA/C3` induced in microglia specifically, `MFGE8` in astrocytes/microglia? (ii) stage specificity — do complement genes rise at low Braak/pre-plaque stages? (iii) context specificity — are they induced in amyloid-associated AND tau-associated microglial states? (iv) **co-expression** — are the complement route and the MFG-E8 route expressed in the *same* cells or partitioned between cell classes? (v) with snATAC, whether complement induction has *regulatory* (open-chromatin/TF-motif) support.
>
> **What transcriptomics CANNOT address:** whether synapses are *actually engulfed*; whether the engulfed material is *intact vs degenerating*; and **which opsonin** mediates the uptake. **The data type that WOULD settle this:** quantitative **synaptic-engulfment assays in human tissue** — e.g., array tomography / super-resolution or confocal co-localization of pre/post-synaptic markers (synaptophysin, PSD-95, VGLUT1) *inside* CD68+/IBA1+ microglial or GFAP+ astrocytic lysosomes, combined with **opsonin co-localization** (C1q/iC3b vs MFG-E8) on those engulfed puncta, ideally with a **perturbation** (organotypic human slice or iPSC-microglia + human-synaptosome phagocytosis assay ± anti-C1q vs anti-MFG-E8). Such human tissue/culture data exist in part (Tzioras 2023 array tomography; iPSC-microglia synaptosome assays) but not at cohort scale and not resolving complement vs MFG-E8 head-to-head across stages.

### GSE148822 — "Distinct amyloid-β and tau associated microglia profiles in AD" (95 samples, PMID:33609158)
- **Fitness:** **High (best fit of the five).** Human snRNA-seq that explicitly separates amyloid-associated from tau-associated microglial states — the exact contrast the convergence claim needs. Microglia-focused, decent donor number.
- **Specific analysis:** Within microglia, score classical-complement module (`C1QA, C1QB, C1QC, C3, C3AR1, ITGAM, CR1, CD11c/ITGAX`) and the competing `MFGE8`/TAM (`MERTK, GAS6, GULP1`) module. Contrast = amyloid-associated vs tau-associated vs homeostatic microglial states (grouping = pathology-annotated microglial cluster and/or regional Aβ/tau load). Test = pseudobulk per-donor mixed model (`~ state + age + sex + PMI + APOE + batch + (1|donor)`), negative-binomial (e.g., muscat/pseudobulk DESeq2), with ambient-RNA correction (SoupX/CellBender) — critical because `C1QA/B/C` are among the highest-expressed microglial genes and leak into ambient. Multiple-testing FDR across modules.
- **Discriminating prediction:** **SUPPORT** if complement module is significantly induced in *both* amyloid- and tau-associated microglia relative to homeostatic (e.g., module score ↑, FDR<0.05, in both contexts), consistent with a shared execution step. **QUALIFY/REFUTE** if complement genes are induced in only one context (convergence fails at the transcript level), or if induction is not microglia-specific, or if `MFGE8`-route genes dominate over complement in the AD microglia — which would favor the competing opsonin.
- **Confounds / prior analyses:** The primary paper (Prater/… 2023, PMID:33609158) already characterized these amyloid- vs tau-microglial states; re-deriving the state definitions is not a test. Novelty is the *complement-vs-MFGE8 module contrast conditioned on those states.* Watch: state-assignment ambiguity, `C1Q` ambient leakage, and that "amyloid-associated"/"tau-associated" labels are correlational within-tissue, not pure drivers.

### GSE160936 — "Diverse human astrocyte and microglial transcriptional responses to AD pathology" (24 samples, PMID:34767070)
- **Fitness:** **Moderate — uniquely covers astrocytes AND microglia**, which is where the MFG-E8/complement assignment can be examined; but **only 24 samples → underpowered** for interaction terms and stage stratification.
- **Specific analysis:** Cell-class-resolved expression of `MFGE8` (astrocyte vs microglia) vs complement `C1QA/C3/ITGAM` (microglia). Question = **are the complement route and the MFG-E8 route expressed in the same cells or partitioned?** Contrast = AD vs control within each glial class; test = pseudobulk NB with `age+sex+PMI+batch`; report cell-class-specific fold-changes and co-expression at single-cell level (are `MFGE8`+ cells also `C1QA`+?).
- **Discriminating prediction:** **QUALIFY toward parallel routes** if `MFGE8` is predominantly astrocytic and `C1Q/C3` predominantly microglial (two cell types, two opsonins → the seed model is incomplete as a microglia+complement monopoly). **SUPPORT (complement-centric)** if microglia dominate synaptic-clearance signatures and `MFGE8` is not preferentially induced. With n=24, expect **no result to reach decisive significance for interaction terms** — likely a hypothesis-generating, not discriminating, dataset. Say so plainly.
- **Confounds / prior analyses:** Primary paper already reported astrocyte+microglia response diversity. Small n; batch/donor confounding severe. Ambient `C1Q` leakage into astrocyte nuclei will masquerade as astrocytic complement expression — must be corrected or the co-expression readout is an artifact.

### GSE254205 — "APOE4/4 is linked to damaging lipid droplets in AD microglia" (102 samples, PMID:38480892)
- **Fitness:** **Moderate, indirect.** APOE-genotyped human microglia — relevant because Tzioras 2023 reports APOE4 exacerbates glial synaptic-protein ingestion. But this study's phenotype is **lipid droplets**, not synapse clearance; the link to complement is a secondary hypothesis.
- **Specific analysis:** Contrast = APOE4/4 vs APOE3/3 microglia (grouping = genotype), scoring complement module and lipid-droplet/DAM markers. Test = pseudobulk NB `~ APOE + diagnosis + age + sex + PMI + batch`; interaction `APOE×diagnosis`. Key question: is complement-module induction **APOE4-dose-dependent**?
- **Discriminating prediction:** **SUPPORT (APOE4 edge)** if complement module is higher in APOE4/4 microglia at matched pathology (FDR<0.05), providing a transcriptomic correlate of the APOE4 exacerbation seen functionally. **QUALIFY** if APOE4 drives the *lipid-droplet/dysfunctional* program **without** complement induction — which would argue APOE4's synapse-ingestion effect runs through a lipid/MFG-E8/phagocytic-competence route rather than complement transcription.
- **Confounds / prior analyses:** Primary paper focuses on lipid droplets (Haney/… 2024, PMID:38480892); complement is not its endpoint, so a complement analysis is genuinely novel here. Confounds: APOE genotype correlates with Braak stage and sex ratios; lipid-droplet microglia may have distinct ambient profiles. APOE4 cannot be cleanly separated from disease severity without careful matching.

### GSE174367 — "Single-nucleus chromatin accessibility and transcriptomic characterization of AD" (230 samples, PMID:34239132)
- **Fitness:** **High for the regulatory sub-question; largest cohort.** Paired snRNA + snATAC lets complement induction be checked for **regulatory support** (open chromatin / TF-motif enrichment) rather than transcript abundance alone — the one thing that lifts these data above "indirect proxy."
- **Specific analysis:** In microglia: (1) snRNA complement-module DE, AD vs control, `~ diagnosis + age + sex + PMI + batch`; (2) snATAC — are `C1QA/C1QB/C1QC/C3/ITGAM` promoters/enhancers **differentially accessible** in AD microglia, and are complement-relevant TF motifs (e.g., PU.1/SPI1, IRF8, MEF2C, C/EBP) enriched in opened peaks? Link peaks to genes (Cicero/ArchR). Correlate ATAC accessibility with RNA induction across donors.
- **Discriminating prediction:** **SUPPORT (regulatory)** if complement-gene induction is accompanied by concordant AD-increased accessibility at their cis-elements and enrichment of microglial-identity TF motifs — evidence of a *programmed* (not passive/ambient) induction. **REFUTE/QUALIFY** if RNA rises without accessibility change (argues post-transcriptional or ambient artifact) or if accessibility is unchanged/decreased. This is the dataset that can distinguish "genuine regulatory program" from "transcript noise."
- **Confounds / prior analyses:** Morabito et al. 2021 (PMID:34239132) built gene-regulatory networks here but not a targeted complement-cis-regulatory test. Confounds: snATAC sparsity at lowly-accessible complement enhancers; peak-to-gene links are probabilistic; ambient RNA still afflicts the RNA arm. Cell-type calling from ATAC is noisier for microglia (rare population).

### GSE147528 — "Molecular characterization of selectively vulnerable neurons in AD" (Braak-staged EC + frontal cortex, PMID:33432193)
- **Fitness:** **Moderate for the "EARLY" claim; poor for the effector claim.** Braak-staged entorhinal cortex + superior frontal gyrus is the right design to ask whether complement induction is **early (low Braak, pre-plaque)** — the model's temporal signature. But the study is **neuron-focused/selective-vulnerability**; microglial numbers may be limited, and it is not designed for glial phenotyping.
- **Specific analysis:** Order donors by Braak stage; in microglia (if sufficient nuclei) test complement-module trajectory vs Braak, and specifically whether induction is detectable at **Braak 0–II (pre-/early tangle, EC)**. Contrast = Braak-stage as ordinal predictor, region (EC vs SFG) as covariate; `~ Braak + region + age + sex + PMI + batch`. Trend test (e.g., ordinal/spline).
- **Discriminating prediction:** **SUPPORT (early tagging)** if complement-module induction in EC microglia is significant already at Braak I–II, *before* frontal involvement and before overt plaques — the human analogue of Hong 2016's pre-plaque timing. **REFUTE/QUALIFY** if complement rises only at late Braak (V–VI) — consistent with the competing "late neuroinflammation" reading the seed model explicitly opposes. **Caveat:** if microglial nuclei per donor are too few, the test is underpowered and **no result discriminates** — likely the case here; flag as a power-limited attempt.
- **Confounds / prior analyses:** Leng et al. 2021 (PMID:33432193) focused on excitatory-neuron vulnerability (RORB neurons in EC), not microglia/complement — so a microglial-complement-vs-Braak analysis is novel. Confounds: microglial nucleus yield, region-specific baseline complement, Braak staged post-mortem (cross-sectional, not longitudinal — cannot establish within-donor temporal order).

### Ranking — how decisively each dataset moves the hypothesis

| Rank | Dataset | Sub-claim it best addresses | Decisiveness |
|---|---|---|---|
| 1 | **GSE174367** (snRNA+snATAC, n=230) | Is complement induction a *programmed regulatory* event in microglia? | **Highest** — only dataset that can separate real program from transcript/ambient noise; largest cohort. |
| 2 | **GSE148822** (amyloid vs tau microglia, n=95) | Convergence: complement induced in *both* amyloid- and tau-microglia? | **High** — directly tests the signature convergence claim, cleanly. |
| 3 | **GSE160936** (astrocytes+microglia) | Complement vs MFG-E8, same cells or partitioned? | **Moderate** — right design, but n=24 underpowered. |
| 4 | **GSE254205** (APOE-genotyped) | Is complement the APOE4-exacerbation route (vs lipid/MFG-E8)? | **Moderate** — indirect; lipid-droplet focus. |
| 5 | **GSE147528** (Braak-staged) | Is complement tagging *early*? | **Moderate-low** — right staging, but microglia likely under-sampled → power-limited. |

**Single analysis I would run first:** In **GSE148822**, the microglial **complement-module vs MFG-E8-module contrast conditioned on amyloid- vs tau-associated states** (pseudobulk NB, donor mixed model, ambient-corrected). It most directly interrogates the hypothesis' defining convergence claim *and* the competing-opsonin question in one computation, on adequate n, using the assay's genuine strength (cell-state resolution) rather than its weakness (it does not need to see engulfment). If time permits, pair it with the **GSE174367 snATAC accessibility check** to ask whether any observed induction is regulatorily supported.

**Question no listed dataset can settle:** *Are intact human synapses engulfed via complement (vs MFG-E8)?* → requires **human tissue synaptic-engulfment assays** (array tomography / super-resolution co-localization of synaptic markers inside glial lysosomes with opsonin co-staining) and/or **human synaptosome phagocytosis assays ± anti-C1q/anti-MFG-E8**. Partial public data exist (Tzioras 2023) but not resolving complement vs MFG-E8 across stages at cohort scale.

---

## Knowledge Gaps

| Gap | Scope | Why it matters | What was checked | What would resolve it |
|---|---|---|---|---|
| **G1. Human engulfment-via-complement unproven** | Execution step | The single claim separating "active complement pruning" from "MFG-E8 clearance" or "passive degeneration" | PubMed: human glial synapse ingestion (Tzioras 2023 shows MFG-E8, not complement) | Human array-tomography/super-res co-localization of synaptic puncta + C1q/iC3b inside microglial lysosomes; human synaptosome phagocytosis ± anti-C1q |
| **G2. Opsonin competition (complement vs MFG-E8 vs TAM/MERTK)** | Molecular route | Determines correct therapeutic target; seed model assumes complement monopoly | Tzioras 2023 (MFG-E8); no head-to-head human study found | Comparative blockade in human iPSC-microglia/astrocyte synaptosome assays; dual opsonin staining on engulfed puncta |
| **G3. Temporal ordering in humans (tagging before loss)** | "Early" claim | The model's core is that tagging is *upstream*, not a reaction to debris | Konijnenberg 2020 (complement precedes synaptic decline in APOE4 CSF); no longitudinal tissue | Longitudinal CSF/PET-staged cohorts; Braak-resolved tissue with microglial complement quantification (partly GSE147528) |
| **G4. Astrocyte contribution** | Effector cell identity | Seed model is microglia-centric; humans show astrocytes ingest synapses too | Tzioras 2023 (astrocytes + microglia) | Cell-class-resolved engulfment + opsonin assays; GSE160936 for expression partition |
| **G5. Anti-C1q clinical efficacy unknown** | Therapeutic MoA | The model's falsifiable therapeutic prediction | PubMed search for ANX005/ANX007 AD trial results returned **no results** as of search date | Report readouts of anti-C1q (e.g., ANX005/ANX007) and anti-C3 trials in AD/neurodegeneration on synaptic/cognitive endpoints |
| **G6. "Intact synapse" assumption** | Substrate state | Distinguishes active pruning from clean-up of already-failing synapses | Mouse pre-plaque timing (Hong 2016); no direct human functional-state data | Physiological/ultrastructural assessment of tagged synapses before engulfment |
| **G7. Genetic specificity** | Causal-genetic | CR1/CLU implicate "complement biology," not specifically *synaptic* C1q pruning | Rajabli 2025, Veteleanu 2023 | Colocalization/eQTL linking CR1/CLU risk alleles to microglial synaptic-complement programs; MR on synaptic biomarkers |
| **G8. Source/data absence — no cohort-scale human phagocytosis omics** | Dataset gap | All public AD single-cell data are nucleus-based and phagocytosis-blind | Reviewed 5 curator datasets + GEO titles | Spatial proteomics / imaging-mass-cytometry cohorts co-staining synaptic markers, opsonins, and glial lysosomes (not found at scale) |

---

## Alternative Models

| Model | Relationship to seed | Basis |
|---|---|---|
| **MFG-E8 opsonophagocytic clearance** (Tzioras 2023, PMID:37652017) | **Competing / parallel** — same endpoint (glia eat synapses), different opsonin and adds astrocytes. The only route with *direct human* engulfment evidence. | Human glia; MFG-E8 inhibition rescues AD-synapse uptake |
| **TREM2 checkpoint-collapse / neuroimmune-glial amplification** (Zhong 2023 PMID:37442133; reviews PMID:42393750, 42614559) | **Upstream regulator + broader parent model** — complement pruning is one effector axis when TREM2/lipid/lysosomal checkpoints fail. Seed model is a specific sub-branch. | TREM2-C1q gating; DAM states |
| **Amyloid-cascade (primary Aβ synaptotoxicity)** | **Upstream cause / partial alternative** — Aβ oligomers may kill synapses directly (LTP block) rather than only via complement tagging. Seed model makes complement the *executor* of Aβ toxicity (Hong 2016 shows C1q necessary for Aβ-oligomer toxicity), integrating the two. | Aβ-oligomer synaptotoxicity literature |
| **Tau-driven intrinsic synaptic failure** (PMID:38712321) | **Parallel / upstream** — tau disrupts synaptic proteome and function cell-autonomously; complement may amplify but not initiate. Seed model overlaps via C1q-on-tau-synapses. | rTg4510 synaptic protein loss |
| **NPTX2 loss of restraint** (Zhou 2023, PMID:36989373) | **Upstream modifier** — reduced neuronal NPTX2 de-represses C1q; a regulator *within* the seed pathway, not a competitor. | FTD CSF + mouse |
| **CSMD1 checkpoint loss** (Nimmo 2026, PMID:42271460) | **Upstream modifier within pathway** | Human/mouse tauopathy synapses |
| **Complement-as-protective (amyloid clearance)** (Shi 2017, PMID:28566429) | **Antithetical qualifier** — same molecules, opposite (beneficial) role for plaques. Constrains therapeutic window. | Aged APP/PS1 C3 KO |

---

## Discriminating Tests

**Runnable today on existing public data:**
1. **Complement-vs-MFG-E8 module contrast across amyloid- vs tau-microglial states** (GSE148822) — tests convergence + competing opsonin. *Expected if seed true:* complement module ↑ in both states, microglia-specific.
2. **snATAC regulatory support for complement induction** (GSE174367) — distinguishes programmed induction from ambient/transcript noise. *Expected if seed true:* concordant AD-increased accessibility at C1Q/C3/ITGAM cis-elements + PU.1/IRF8 motif enrichment.
3. **Cell-class opsonin partition** (GSE160936) — are complement (microglia) and MFG-E8 (astrocyte) segregated? *Expected if seed incomplete:* MFG-E8 astrocytic, complement microglial → two-route model.
4. **Braak-trajectory of microglial complement** (GSE147528, power permitting) — early vs late induction. *Expected if seed true:* induction at Braak I–II in EC.
5. **CR1/CLU eQTL–synaptic-complement colocalization / Mendelian randomization** (public GWAS + brain eQTL) — is the genetic risk mediated through microglial complement programs?

**Require new sample collection / assays:**
6. **Human tissue synaptic-engulfment + opsonin co-localization** (array tomography/super-resolution): synaptophysin/PSD-95/VGLUT1 puncta inside CD68+ microglia vs GFAP+ astrocytes, co-stained C1q/iC3b vs MFG-E8, stratified by Braak, APOE, amyloid vs tau region. **This is the single most decisive experiment.**
7. **Human synaptosome phagocytosis assay** (iPSC-microglia & -astrocytes + AD-patient synaptosomes) ± anti-C1q vs anti-MFG-E8 vs anti-MERTK: head-to-head opsonin necessity in a human system.
8. **Anti-C1q / anti-C3 trial synaptic-biomarker readout** (CSF neurogranin/SNAP-25/VAMP-2, synaptic PET) stratified by APOE and amyloid/tau status: does complement blockade preserve human synapses? Definitive interventional test of the therapeutic prediction.

**Patient stratification for all human tests:** APOE4 dose, amyloid-positive vs tau-predominant, Braak stage, EOAD vs LOAD, sex; control for PMI and age.

---

## Curation Leads *(all require curator verification)*

**Candidate evidence references + snippets to verify (exact abstract quotes):**
- **PMID:31433986** (Wu 2019) — *"C3 protein is elevated in AD patient brains, including at synapses, and levels and processing of C3 are increased in AD patient CSF and correlate with tau."* → adds **HUMAN** tissue/CSF support the current YAML lacks (currently only mouse SUPPORT + 1 human PARTIAL). Suggest `supports: SUPPORT`, `evidence_source: HUMAN_CLINICAL` (+ MODEL_ORGANISM for the C3-KO rescue).
- **PMID:41000995** (Petrisko 2025) — microglia-specific C1q deletion reduces engulfment & prevents cognitive impairment. Verify snippet from abstract. → `supports: SUPPORT`, `MODEL_ORGANISM`; strengthens necessity by isolating *microglial* C1q.
- **PMID:42271460** (Nimmo 2026) — *"The classic pathway regulator CSMD1 was present on synapses and decreased on C1q positive synapses in P301S mice, implying a loss of protection"* → SUPPORT; extends amyloid-independent (tau) arm + adds CSMD1 node.
- **PMID:40676597** (Rajabli 2025) — *"Pathway analysis implicates multiple amyloid regulation pathways and the classical complement pathway."* → SUPPORT, `evidence_source: HUMAN_CLINICAL` (genetic); the causal-genetic anchor currently missing.
- **PMID:37480051** (Veteleanu 2023) — *"Clusterin and C1q were significantly increased (p < 0.001) and sCR1 and factor H reduced (p < 0.01) in AD plasma versus controls."* → SUPPORT (biomarker), spans EOAD+LOAD.
- **PMID:37442133** (Zhong 2023) — *"Trem2 haploinsufficiency increased complement-mediated microglial engulfment of synapses and accelerated synaptic loss."* → QUALIFY (gating node; links to TREM2 model).
- **PMID:36989373** (Zhou 2023) — *"Nptx2-deficient mice show increased complement activity, C1q-dependent microglial synapse engulfment, and loss of excitatory synapses."* → QUALIFY (upstream regulator).
- **PMID:22488444** (Daborg 2012) & **PMID:32460813** (Konijnenberg 2020) — CSF complement tracks/precedes AD; support "early," APOE4-dependent. → SUPPORT (correlative).

**Candidate pathophysiology nodes/edges:**
- Add gating nodes: `TREM2 ⊣ C1q activation`, `NPTX2 ⊣ C1q`, `CSMD1 ⊣ classical pathway at synapse`, `APOE4 → ↑glial synapse ingestion`.
- Add competing edge: `MFG-E8 → glial synapse engulfment (human, astrocyte+microglia)` as an explicit alternative-opsonin edge.
- Annotate bidirectional edge: `C3 → Aβ plaque clearance (protective)` vs `C3/iC3b → synapse opsonization (harmful)`.

**Candidate ontology terms:**
- Cell types: microglial cell (CL:0000129), astrocyte (CL:0000127).
- Processes: complement activation, classical pathway (GO:0006958); synaptic pruning (GO:0098883); microglial cell activation (GO:0001774); regulation of complement activation (GO:0030449); synapse pruning / phagocytosis (GO:0006911).
- Molecules: C1QA/B/C, C3, C3AR1, ITGAM (CR3), CR1, MFGE8, TREM2, NPTX2, CSMD1, CLU.

**Candidate subtype restriction / status:**
- Keep `status: ALTERNATIVE`. Human causal step (complement-mediated engulfment) remains unproven; competing MFG-E8 route has the only direct human phagocytosis evidence. Do **not** promote to CANONICAL.
- Subtype scope (EOAD + LOAD) is supported by GWAS/plasma data spanning both; amyloid-independent (pure tauopathy) extension is now human-supported (Nimmo 2026) — consider noting applicability to primary tauopathies as a related context.

**Candidate `knowledge_gaps` / discussion prompts:** G1–G8 above; especially **G1 (human engulfment-via-complement unproven)**, **G2 (complement vs MFG-E8)**, **G5 (anti-C1q trial readout absent as of 2026-08-28 search)**.

**Candidate `datasets:` entries (accessions exactly as GEO states; curator-supplied, resolved):**
- `geo:GSE148822` — best fit; amyloid-vs-tau microglial convergence + opsonin contrast.
- `geo:GSE174367` — snRNA+snATAC; regulatory support test.
- `geo:GSE160936` — astrocyte+microglia; opsonin partition (underpowered, n=24).
- `geo:GSE254205` — APOE-stratified microglia; APOE4-complement edge.
- `geo:GSE147528` — Braak-staged; "early" test (microglia possibly under-sampled).

**Unverified datasets I found (curator must resolve before use):**
- *Unverified:* GEO **GSE243292**-type resources referenced by the "microglia amyloid/tau microenvironment" literature (PMID:42619689) — **flagged unverified; do not curate without accession resolution.** (Surfaced during search; accession not confirmed.)

---

## Limitations of this report
- Literature-only search (no primary data analysis; datasets were reasoned about, not downloaded/run).
- PubMed queries with long phrasing intermittently failed; some negative searches (e.g., ANX005/ANX007 trial results) may reflect query brittleness rather than true absence — flagged as such (G5).
- Snippets quoted for curation are from returned abstracts and should be re-validated against source text.
- "Reviews" (PMID:42393750, 42614559, 42627617) used only for orientation and framing, not as primary evidence.

---
*Report generated Iteration 3. See knowledge-state findings #1–#5 for recorded, citation-validated sub-conclusions.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)