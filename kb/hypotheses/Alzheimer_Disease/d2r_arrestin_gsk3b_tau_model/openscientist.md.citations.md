# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Alzheimer Disease
- **Category:** Neurodegenerative Disorder

## Target Hypothesis
- **Hypothesis ID:** d2r_arrestin_gsk3b_tau_model
- **Hypothesis Label:** D2 Receptor-Arrestin-GSK-3beta Tau Kinase Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: d2r_arrestin_gsk3b_tau_model
hypothesis_label: D2 Receptor-Arrestin-GSK-3beta Tau Kinase Model
status: EMERGING
description: 'Tau phosphorylation in Alzheimer disease is modeled as partly set by the signalling state
  of D2-family dopamine receptors, making a D2/D3 partial agonist a candidate disease-modifying rather
  than purely symptomatic agent. D2 receptor over-activation drives the beta-arrestin2/PP2A/Akt scaffold
  toward Akt dephosphorylation, which relieves inhibitory Ser9 phosphorylation on GSK-3beta, the principal
  tau kinase. Aripiprazole, unlike the full antagonist haloperidol, preserves phospho-Akt and phospho-GSK-3beta
  under D2R hyperactivity in cortical neurons, and is a weak-partial or frankly antagonist ligand at D2/D3-mediated
  beta-arrestin translocation. The model is significant because it predicts a readout nobody has measured:
  if it holds, chronic aripiprazole exposure should lower tau phosphorylation at GSK-3beta-dependent epitopes
  in a tauopathy model, and the existing beta-arrestin-biased aripiprazole analogue UNC9994 should fail
  to reproduce the effect or reverse it.'
evidence:
- reference: PMID:30597182
  reference_title: Aripiprazole and haloperidol protect neurite lesions via reducing excessive D2R-DISC1
    complex formation.
  supports: SUPPORT
  directness: INDIRECT
  evidence_source: IN_VITRO
  snippet: Unlike haloperidol, aripiprazole prevented downregulation of phospho (p) Akt-pGSK3β induced
    by D2R hyperactivity, indicating involvement of different pathways.
  explanation: The load-bearing result. It places aripiprazole upstream of Akt-GSK-3beta signalling in
    cortical neurons and distinguishes it from a full D2 antagonist, which is what makes the model a claim
    about this drug rather than about antipsychotics as a class. Indirect because the readout is neurite
    morphology in a neurodevelopmental model, not tau.
- reference: PMID:41192583
  reference_title: Distinct functional profiles of partial agonist antipsychotics in cAMP and β-arrestin
    signaling mechanisms of dopamine D(2) and D(3) receptors in vitro.
  supports: SUPPORT
  directness: INDIRECT
  evidence_source: IN_VITRO
  snippet: aripiprazole and brexpiprazole displayed only weak or no agonist but potent antagonist activity
  explanation: Characterizes the arrestin-pathway ligand profile the model depends on, at recombinant
    human D3 receptors. A drug that antagonizes arrestin recruitment is positioned to prevent the arrestin-dependent
    Akt dephosphorylation this model invokes.
- reference: PMID:39174788
  reference_title: Administration of Aripiprazole Alleviates Memory Impairment and Restores Damaged Glutamatergic
    System in 5xFAD Mice.
  supports: SUPPORT
  directness: INDIRECT
  evidence_source: MODEL_ORGANISM
  snippet: The aripiprazole-treated group exhibited alleviated memory impairment in a novel object recognition
    test.
  explanation: The only in vivo exposure of an Alzheimer model to chronic aripiprazole, establishing that
    the drug is not behaviourally inert in an amyloid model at 1 mg/kg/day. It supports the premise rather
    than the route - the mechanism the authors report is glutamatergic, and neither tau nor GSK-3beta
    was measured.
- reference: PMID:34173272
  reference_title: 'Long-term antipsychotic use and cognitive decline in community-dwelling older adults
    with mild-moderate Alzheimer disease: Data from NILVAD.'
  supports: REFUTE
  directness: INDIRECT
  evidence_source: HUMAN_CLINICAL
  snippet: Long-term antipsychotic use was associated with greater cognitive decline and dementia progression
    in community-dwelling older adults with mild-moderate AD.
  explanation: The principal human counter-evidence, and the constraint any disease-modifying reading
    has to survive. Indirect because the exposure is drug-class-level rather than aripiprazole-specific
    and the design is observational within a trial cohort, so confounding by indication is unresolved
    - neuropsychiatric symptoms themselves predict faster decline.
notes: 'EMERGING, and declared here to scope a deep-research exploration rather than to assert a curated
  mechanism. Nothing in this entry''s pathograph opts into this group yet, and no causal edge should until
  the tau arm has direct support. The route is assembled from cross-domain work: the Akt-GSK-3beta result
  is in cortical neurons in a schizophrenia/DISC1 context, the ligand profiling is in recombinant cell
  lines, and the only Alzheimer-model exposure reports a glutamatergic readout. A PubMed sweep for aripiprazole
  against tau, GSK-3, amyloid or APP returns no study in an Alzheimer or tauopathy model, so the central
  prediction is untested rather than contested. Three things should be checked before this is promoted:
  whether the pAkt-pGSK-3beta preservation reproduces in neurons carrying tau pathology; whether the beta-arrestin-biased
  aripiprazole analogue UNC9994 separates the arrestin-blocking reading from a biased-signalling one;
  and whether the NILVAD class-level signal survives a drug-specific and dose-stratified analysis, given
  that therapeutic-dose D2 occupancy is far above the exposure used in the 5xFAD study.'
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

When dataset or scientific-tool access is available, use it for questions that
can be tested computationally rather than limiting the run to literature search.
Preflight the required data lake, databases, packages, credentials, and tools
before claiming that an analysis can run. Never silently fall back from a failed
dataset/tool analysis to literature synthesis or model knowledge: report the
failure, the fallback, and the resulting limitation explicitly. A proposed
analysis must never be described as performed.

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

### Data and Tool Use

Inventory every dataset, database, API, supplementary file, or local input
material to the report. For each, state:

- stable accession or URI, repository/source, version or snapshot, and retrieval
  date where known;
- whether it was only cited/proposed, actually accessed, searched with no usable
  result, or could not be verified;
- the exact query, filters, cohort, sample subset, organism, tissue, assay, and
  comparison used where applicable;
- whether the accession resolved and whether its subject matter is genuinely
  relevant to this disease and hypothesis.

For accessed sources and negative searches, save a sanitized query response,
input manifest, or search log in the provider artifact bundle; prose alone does
not establish access or a negative result.

Inventory each attempted analysis separately. Trace input -> method -> output,
including software/model versions, material parameters, code or workflow,
environment, random seeds where relevant, output files, and limitations. Label
the execution outcome as succeeded, partial, failed, skipped, or reported-only.
Do not count a prose assertion without inspectable execution evidence as a
successful analysis.

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
evidence or experiment would resolve it. A negative database search must include
the database/version, query, filters, and search date; otherwise label it
unverified rather than claiming absence.

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

If the provider supports artifacts, produce a provider artifact bundle containing
canonical `MANIFEST.yaml` (schema version, status/fallback flags, checksummed
inputs/outputs, and replay verification), code/query/configuration, an
environment or package-version record,
sanitized execution logs, and small derived tables/figures needed to inspect the
result beneath `kb/hypotheses/Alzheimer_Disease/d2r_arrestin_gsk3b_tau_model/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.

**Provider:** openscientist
**Generated:** 2026-09-21T20:49:10.912275

1. PMID:17681085
2. PMID:23321003
3. PMID:30597182
4. PMID:39174788
5. PMID:28367951
6. PMID:28965318
7. PMID:41930581
8. PMID:31156177
9. PMID:22299660
10. PMID:26484916
11. PMID:22025698
12. PMID:36760217
13. PMID:38350636
14. PMID:33684513
15. PMID:34173272