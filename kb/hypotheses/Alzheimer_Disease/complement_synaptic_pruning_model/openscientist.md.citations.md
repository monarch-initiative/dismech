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

**Provider:** openscientist
**Generated:** 2026-08-28T07:54:33.743613

1. PMID:27033548
2. PMID:28566429
3. PMID:31433986
4. PMID:41000995
5. PMID:30392797
6. PMID:42271460
7. PMID:37652017
8. PMID:22488444
9. PMID:40676597
10. PMID:29504051
11. PMID:37480051
12. PMID:42393750
13. PMID:42614559
14. PMID:33609158
15. PMID:34767070
16. PMID:38480892
17. PMID:34239132
18. PMID:33432193
19. PMID:37442133
20. PMID:38712321
21. PMID:36989373
22. PMID:32460813
23. PMID:42619689