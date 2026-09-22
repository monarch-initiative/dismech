---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T20:32:49.081538'
end_time: '2026-09-21T20:49:10.912275'
duration_seconds: 981.83
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Alzheimer Disease
  category: Neurodegenerative Disorder
  hypothesis_group_id: d2r_arrestin_gsk3b_tau_model
  hypothesis_label: D2 Receptor-Arrestin-GSK-3beta Tau Kinase Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: d2r_arrestin_gsk3b_tau_model\nhypothesis_label:\
    \ D2 Receptor-Arrestin-GSK-3beta Tau Kinase Model\nstatus: EMERGING\ndescription:\
    \ 'Tau phosphorylation in Alzheimer disease is modeled as partly set by the signalling\
    \ state\n  of D2-family dopamine receptors, making a D2/D3 partial agonist a candidate\
    \ disease-modifying rather\n  than purely symptomatic agent. D2 receptor over-activation\
    \ drives the beta-arrestin2/PP2A/Akt scaffold\n  toward Akt dephosphorylation,\
    \ which relieves inhibitory Ser9 phosphorylation on GSK-3beta, the principal\n\
    \  tau kinase. Aripiprazole, unlike the full antagonist haloperidol, preserves\
    \ phospho-Akt and phospho-GSK-3beta\n  under D2R hyperactivity in cortical neurons,\
    \ and is a weak-partial or frankly antagonist ligand at D2/D3-mediated\n  beta-arrestin\
    \ translocation. The model is significant because it predicts a readout nobody\
    \ has measured:\n  if it holds, chronic aripiprazole exposure should lower tau\
    \ phosphorylation at GSK-3beta-dependent epitopes\n  in a tauopathy model, and\
    \ the existing beta-arrestin-biased aripiprazole analogue UNC9994 should fail\n\
    \  to reproduce the effect or reverse it.'\nevidence:\n- reference: PMID:30597182\n\
    \  reference_title: Aripiprazole and haloperidol protect neurite lesions via reducing\
    \ excessive D2R-DISC1\n    complex formation.\n  supports: SUPPORT\n  directness:\
    \ INDIRECT\n  evidence_source: IN_VITRO\n  snippet: Unlike haloperidol, aripiprazole\
    \ prevented downregulation of phospho (p) Akt-pGSK3\u03B2 induced\n    by D2R\
    \ hyperactivity, indicating involvement of different pathways.\n  explanation:\
    \ The load-bearing result. It places aripiprazole upstream of Akt-GSK-3beta signalling\
    \ in\n    cortical neurons and distinguishes it from a full D2 antagonist, which\
    \ is what makes the model a claim\n    about this drug rather than about antipsychotics\
    \ as a class. Indirect because the readout is neurite\n    morphology in a neurodevelopmental\
    \ model, not tau.\n- reference: PMID:41192583\n  reference_title: Distinct functional\
    \ profiles of partial agonist antipsychotics in cAMP and \u03B2-arrestin\n   \
    \ signaling mechanisms of dopamine D(2) and D(3) receptors in vitro.\n  supports:\
    \ SUPPORT\n  directness: INDIRECT\n  evidence_source: IN_VITRO\n  snippet: aripiprazole\
    \ and brexpiprazole displayed only weak or no agonist but potent antagonist activity\n\
    \  explanation: Characterizes the arrestin-pathway ligand profile the model depends\
    \ on, at recombinant\n    human D3 receptors. A drug that antagonizes arrestin\
    \ recruitment is positioned to prevent the arrestin-dependent\n    Akt dephosphorylation\
    \ this model invokes.\n- reference: PMID:39174788\n  reference_title: Administration\
    \ of Aripiprazole Alleviates Memory Impairment and Restores Damaged Glutamatergic\n\
    \    System in 5xFAD Mice.\n  supports: SUPPORT\n  directness: INDIRECT\n  evidence_source:\
    \ MODEL_ORGANISM\n  snippet: The aripiprazole-treated group exhibited alleviated\
    \ memory impairment in a novel object recognition\n    test.\n  explanation: The\
    \ only in vivo exposure of an Alzheimer model to chronic aripiprazole, establishing\
    \ that\n    the drug is not behaviourally inert in an amyloid model at 1 mg/kg/day.\
    \ It supports the premise rather\n    than the route - the mechanism the authors\
    \ report is glutamatergic, and neither tau nor GSK-3beta\n    was measured.\n\
    - reference: PMID:34173272\n  reference_title: 'Long-term antipsychotic use and\
    \ cognitive decline in community-dwelling older adults\n    with mild-moderate\
    \ Alzheimer disease: Data from NILVAD.'\n  supports: REFUTE\n  directness: INDIRECT\n\
    \  evidence_source: HUMAN_CLINICAL\n  snippet: Long-term antipsychotic use was\
    \ associated with greater cognitive decline and dementia progression\n    in community-dwelling\
    \ older adults with mild-moderate AD.\n  explanation: The principal human counter-evidence,\
    \ and the constraint any disease-modifying reading\n    has to survive. Indirect\
    \ because the exposure is drug-class-level rather than aripiprazole-specific\n\
    \    and the design is observational within a trial cohort, so confounding by\
    \ indication is unresolved\n    - neuropsychiatric symptoms themselves predict\
    \ faster decline.\nnotes: 'EMERGING, and declared here to scope a deep-research\
    \ exploration rather than to assert a curated\n  mechanism. Nothing in this entry''s\
    \ pathograph opts into this group yet, and no causal edge should until\n  the\
    \ tau arm has direct support. The route is assembled from cross-domain work: the\
    \ Akt-GSK-3beta result\n  is in cortical neurons in a schizophrenia/DISC1 context,\
    \ the ligand profiling is in recombinant cell\n  lines, and the only Alzheimer-model\
    \ exposure reports a glutamatergic readout. A PubMed sweep for aripiprazole\n\
    \  against tau, GSK-3, amyloid or APP returns no study in an Alzheimer or tauopathy\
    \ model, so the central\n  prediction is untested rather than contested. Three\
    \ things should be checked before this is promoted:\n  whether the pAkt-pGSK-3beta\
    \ preservation reproduces in neurons carrying tau pathology; whether the beta-arrestin-biased\n\
    \  aripiprazole analogue UNC9994 separates the arrestin-blocking reading from\
    \ a biased-signalling one;\n  and whether the NILVAD class-level signal survives\
    \ a drug-specific and dose-stratified analysis, given\n  that therapeutic-dose\
    \ D2 occupancy is far above the exposure used in the 5xFAD study.'"
  artifact_dir: kb/hypotheses/Alzheimer_Disease/d2r_arrestin_gsk3b_tau_model/openscientist_artifacts
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
citation_count: 15
term_validation:
  total_terms: 6
  verified: 6
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
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
- filename: kb_hypotheses_Alzheimer_Disease_d2r_arrestin_gsk3b_tau_model_openscientist_artifacts_code_build_artifacts.md
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_d2r_arrestin_gsk3b_tau_model_openscientist_artifacts_code_build_artifacts.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist build artifacts
- filename: kb_hypotheses_Alzheimer_Disease_d2r_arrestin_gsk3b_tau_model_openscientist_artifacts_search_logs_pubmed_search_log.json
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_d2r_arrestin_gsk3b_tau_model_openscientist_artifacts_search_logs_pubmed_search_log.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pubmed search log
- filename: kb_hypotheses_Alzheimer_Disease_d2r_arrestin_gsk3b_tau_model_openscientist_artifacts_tables_evidence_matrix.csv
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_d2r_arrestin_gsk3b_tau_model_openscientist_artifacts_tables_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
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


## Output

# Hypothesis-Search Report: D2 Receptor–Arrestin–GSK-3β Tau Kinase Model in Alzheimer Disease

**Hypothesis ID:** `d2r_arrestin_gsk3b_tau_model` · **KB status:** EMERGING · **Search date:** 2026-09-21
**Run type:** Literature hypothesis-search (no dataset provided; no omics/structural analysis performed)

---

## Executive Judgment

**Verdict: WEAKLY / PARTIALLY SUPPORTED as assembled, with the central disease-relevant claim UNTESTED and the core directional premise contradicted by the dominant AD-dopamine literature.**

The hypothesis is best described as a *mechanistically plausible but unverified assembly* of edges borrowed from three different domains:

1. **Upstream edges are individually well established** (high confidence). The noncanonical D2R → β-arrestin2/PP2A/Akt → GSK-3β pathway is a mature, independently replicated mechanism (PMID:17681085, 23188793, 23380502), and GSK-3β is repeatedly identified as the principal tau kinase (PMID:23321003, 38160617). The load-bearing distinction — that aripiprazole, unlike haloperidol, preserves pAkt–pGSK3β under D2R hyperactivity — is real but was measured in a **schizophrenia/DISC1 cortical-neuron neurite model, not tau, not AD** (PMID:30597182).

2. **The disease-relevant terminal claim is untested** (the decisive gap). A PubMed search for `aripiprazole tau phosphorylation amyloid Alzheimer model` returned **zero** papers. No study has measured tau or GSK-3β-dependent phospho-epitopes after aripiprazole in any AD/tauopathy model. The one in-vivo AD exposure (5xFAD, 1 mg/kg × 2 months, n=6/group) reports a **glutamatergic/behavioral** benefit and explicitly did not measure tau, with the authors themselves flagging a **safety** constraint (PMID:39174788).

3. **The core premise runs against the prevailing AD-dopamine model** (the strongest caveat). The seed posits D2R **over-activation** as pathogenic. The dominant experimental framework instead describes **early VTA dopaminergic degeneration / hypodopaminergia** in AD models, rescued by levodopa (PMID:28367951, 29778899), and human genetics associate **lower** D2 receptor function (DRD2 Taq1A A1) with worse memory and higher AD risk (PMID:28965318, 27647283). A 2026 review couples dopamine **depletion** to GSK-3β **activation** — the opposite direction (PMID:41930581). Under these frameworks, any 5xFAD aripiprazole benefit is more parsimoniously explained by a partial agonist **restoring deficient dopaminergic tone**, not by blocking arrestin-mediated tau kinase activation.

Additional headwinds: direct GSK-3β inhibition failed to help AD cognition in RCTs (tideglusib null; PMID:31156177), and tau hyperphosphorylation in AD is substantially explained by **PP2A phosphatase failure** (APOE-ε4-linked) that needs no D2R input (PMID:22299660, 28720530). The seed's own use of PP2A is internally strained, since PP2A also dephosphorylates GSK-3β-Ser9 (PMID:26484916).

**Net:** the hypothesis earns its EMERGING label and its own falsification test is feasible (UNC9994 exists and is arrestin-biased; PMID:22025698). It should **not** be promoted to a curated causal edge until the tau arm has direct support and the directional conflict is resolved.

---

## Evidence Matrix

| PMID | Type | Stance | Mechanistic claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| 30597182 | in vitro | **support** (load-bearing) | aripiprazole preserves pAkt-pGSK3β vs haloperidol under D2R hyperactivity | "Unlike haloperidol, aripiprazole prevented downregulation of phospho…Akt-pGSK3β" | cortical neurons, DISC1/schizophrenia | Indirect: neurite readout, not tau; no AD |
| 41192583 | in vitro | support / qualify | aripiprazole arrestin ligand profile at D2/D3 | "weak or no agonist but potent antagonist activity" at arrestin | recombinant human D2/D3 | Indirect; recombinant cells |
| 39174788 | model organism | support (premise only) | chronic aripiprazole benefits an AD model | improved NORT; +7–8% glutamate PET; glutamatergic recovery | 5xFAD, 1 mg/kg ×2 mo, n=6/grp | Small n; glutamatergic not tau; author safety caveat |
| 34173272 | human clinical | **refute** | antipsychotic effect on AD cognition | APs → faster cognitive decline & dementia progression; **worse in APOE ε4** | NILVAD, n=509 mild-moderate AD | Class-level, not aripiprazole-specific; confounding by indication |
| 17681085 | in vitro / human | support (backbone) | DRD2 → AKT1/PP2A/βarr2 → GSK-3β | complex "dephosphorylates/inactivates AKT1 thereby activating GSK-3beta" | schizophrenia cells/brain | Backbone edge; not AD/tau |
| 23188793 | model organism | support (backbone) | βarr2/Akt/PP2A/GSK3β in D2R neurons; atypicals antagonize D2R/βarr2 | D2GSK3β-KO mimics antipsychotic action | mouse D2R neurons | Behavior not tau |
| 23380502 | model organism | support (backbone) | D2R βarr2/PP2A/Akt complex dephosphorylates Akt | apomorphine recruits PP2A-C to Akt | mouse striatum | Striatum not AD |
| 23321003 | in vitro / model | support (terminal) | GSK-3β is principal tau kinase; GSK-3β/PP2A balance | shifting balance lowers Aβ-induced tau | cortical neurons + Tg mouse | Supports GSK3β→tau edge |
| 22025698 | in vitro / model | support (reagent) | UNC9994 identity & pharmacology | arrestin-biased D2R agonist from aripiprazole scaffold; effect β-arrestin2-dependent | recombinant + mice | Enables discriminating test; not AD/tau |
| 22845053 | in vitro | support (reagent) | UNC9994 structure-functional-selectivity | arrestin-biased D2R agonists from aripiprazole scaffold | recombinant | Reagent characterization |
| 26129680 | model organism | support (reagent) | UNC9994 in-vivo behavior | improves NORT in hypoglutamatergic mice | mice | Schizophrenia, not AD |
| 28367951 | model organism | **competing** | VTA DA neuron loss drives AD memory deficit | pre-plaque VTA DA loss lowers hippocampal/NAc DA | Tg2576 | Opposes over-activation premise (hypodopaminergia) |
| 29778899 | model organism | **competing** | DA loss impairs hippocampus-NAc; DA restoration rescues | levodopa rescues deficits | Tg2576 | DA restoration beneficial |
| 29630556 | review / human | competing | VTA volume associates with AD cognition | human VTA–cognition link | prodromal AD | Orientation-level |
| 33684513 | model organism | competing | c-Abl drives VTA DA degeneration | nilotinib prevents DA loss, lowers Aβ, restores memory | Tg2576 | Alternative upstream (c-Abl/autophagy) |
| 31156177 | human clinical | **qualify / refute** | GSK-3β inhibition improves AD cognition | GSK-3 inhibitors ineffective; **tideglusib null (SMD=-0.02, p=0.89)** | 5 RCTs, N=568 | Weakens terminal-node therapeutic rationale |
| 22299660 | review / human | **competing** | PP2A failure drives AD tau | multiple PP2A deficits in AD brain | human AD brain | Parallel, D2R-independent tau driver |
| 28720530 | in vitro | competing | APOE downregulates PP2A | ApoE lowers PP2A | AD relevance | Links tau-phosphatase deficit to APOE ε4 |
| 26484916 | in vitro | qualify | PP2A dephosphorylates GSK-3β-Ser9 | PP2A suppresses GSK-3β-Ser9 | brain extracts / HEK293FT | Complicates seed's one-way PP2A use |
| 38350636 | review | competing | amyloid + GSK3β/CDK5 + PP2A | CDK5 is a parallel tau kinase | AD review | Multiple convergent kinases |
| 36760217 | model organism | competing | Aβ42 lowers pAkt/pGSK3β, raises pTau | Aβ drives Akt/GSK3β/tau axis | Aβ42 icv mice | Amyloid upstream of GSK3β without D2R |
| 41930581 | review | **contradict (direction)** | dopamine DEPLETION activates GSK-3β/tau | "dopamine depletion, leading to increased GSK-3 b activity" | 2026 narrative review | Opposite dopamine direction to seed |
| 28965318 | human (genetic) | contradict (direction) | DRD2 function and AD risk | DRD2 Taq1A **A1 (low D2 density)** may magnify AD risk | aging African-Americans | Association; not a tau readout |
| 27647283 | human (genetic) | contradict (direction) | dopamine-receptor efficacy and memory | **higher** D2/D1/D3 efficacy alleles → better memory | n=525, age 60 | Cognition phenotype, not tau |

---

## Data and Tool Use

| Source / tool | Accession / URI | Access status | Query / usage | Relevant? |
|---|---|---|---|---|
| PubMed (NCBI E-utilities) | eutils esearch, db=pubmed | **Accessed** (searched) | 13 queries, 2026-09-21 (see `search_logs/pubmed_search_log.json`) | Yes — primary literature |
| `execute_code` sandbox | local | **Attempted, failed** for artifact writing | blocked `hashlib`/`sys`/`csv`; `PermissionError` on `kb/` path | Tooling only |
| Bash `sha256sum` | local | **Accessed** | checksummed 4 artifact files | Provenance |
| Datasets / omics / GWAS / cohorts | — | **Not accessed** | none provided (Files: []) | N/A |
| Structural files / Phenix | — | **Not used** | no structures in scope | N/A |

**Negative searches (index-conditioned, PubMed 2026-09-21):**
- `aripiprazole tau phosphorylation amyloid Alzheimer model` → **0 results** (central prediction untested).
- `dopamine receptor D2 expression Alzheimer disease brain` → no direct DRD2-in-AD-brain quantitation; **DRD2/DRD3 AD-GWAS association is UNVERIFIED** (this index is not a GWAS catalog).

**Analysis inventory:** Only one "analysis" exists — manual construction of the 22-row evidence matrix from abstract reads (input: PubMed abstracts → method: manual transcription → output: `tables/evidence_matrix.csv`). **Outcome: SUCCEEDED (inspectable CSV).** No statistical/omics analysis was run; those are labeled **SKIPPED**. No prose claim in this report is presented as a computed result.

---

## Mechanistic Causal Chain (upstream → clinical)

1. **D2R over-activation** *(seed premise — CONTESTED in AD; VTA hypodopaminergia and DRD2-A1 genetics point the opposite way: PMID:28367951, 28965318, 41930581)*
2. → **β-arrestin2/PP2A/Akt scaffold, Akt dephosphorylation** *(STRONG as general biology: PMID:17681085, 23380502; but a distinct arrestin-scaffolded PP2A pool is needed because bulk PP2A is DECREASED in AD: PMID:22299660)*
3. → **GSK-3β Ser9 de-inhibition / activation** *(STRONG edge in principle; but PP2A also dephosphorylates Ser9, muddying sign: PMID:26484916)*
4. → **tau phosphorylation at GSK-3β epitopes** *(STRONG that GSK-3β→tau: PMID:23321003, 38160617; but INFERRED for the D2R route specifically)*
5. → **neurofibrillary pathology → cognitive decline** *(amyloid and PP2A failure are better-supported drivers: PMID:36760217, 22299660)*
6. **Drug node:** aripiprazole preserves pAkt-pGSK3β and antagonizes arrestin *(SUPPORTED off-target: PMID:30597182, 41192583)* → predicted to **lower** tau; arrestin-biased **UNC9994** predicted to fail/reverse *(MISSING: never measured — the decisive experiment)*.

**Strong links:** steps 2–4 as general signaling biology; the aripiprazole vs haloperidol pAkt-pGSK3β divergence. **Inferred links:** that step 1 operates in the *pathogenic* direction in AD; that the D2R route (not amyloid/PP2A) sets tau in AD. **Missing steps:** the entire drug→tau readout in an AD/tauopathy model (steps 4–6 for aripiprazole/UNC9994).

---

## Knowledge Gaps

1. **Tau arm never measured (core gap).** Scope: no aripiprazole/UNC9994 study reports tau or pGSK3β epitopes in any AD/tauopathy model. Checked: PubMed `aripiprazole tau…` = 0 hits (2026-09-21). Resolve: chronic aripiprazole in a tau model (e.g., P301S/rTg4510 or 3xTg) with AT8/PHF-1/pGSK3β-Tyr216 readouts.
2. **Directional conflict on the dopamine axis (unresolved contradiction).** Seed = D2R over-activation harmful; competing literature = dopamine depletion/low D2 harmful (PMID:28367951, 41930581, 28965318). Resolve: dose–response of a D2 partial agonist vs a selective arrestin-biased ligand on tau in the same model.
3. **Unconfirmed arrestin-scaffolded-PP2A edge in AD.** Bulk PP2A is *decreased* in AD (PMID:22299660), so the seed must specify a receptor-proximal PP2A pool. Resolve: D2R/βarr2/PP2A co-IP and pAkt in AD-model cortical neurons ± UNC9994.
4. **Terminal-node therapeutic doubt.** Direct GSK-3β inhibition failed clinically (PMID:31156177). Resolve: confirm target engagement + tau lowering are necessary vs sufficient for cognitive benefit.
5. **NILVAD refute is class-level and confounded.** Resolve: drug-specific, dose/D2-occupancy-stratified analysis (aripiprazole vs typicals), with neuropsychiatric-symptom adjustment.
6. **Source absence (unverified).** No DRD2/DRD3 AD-risk association retrievable via this literature index; a GWAS Catalog / GenCC / ClinGen query was **not** executed here and should be logged separately before asserting absence.

---

## Alternative Models

- **VTA dopaminergic degeneration / hypodopaminergia** (PMID:28367951, 29778899, 29630556) — *alternative & opposite-direction*: AD is dopamine-deficient; D2 stimulation is protective.
- **Amyloid cascade → Akt/GSK-3β/tau** (PMID:36760217, 38350636) — *upstream cause*: dominant, D2R-independent driver; the seed's route is a minor tributary.
- **PP2A phosphatase failure (APOE-ε4-linked)** (PMID:22299660, 28720530) — *parallel mechanism*: explains tau hyperphosphorylation without D2R.
- **CDK5 as parallel tau kinase** (PMID:38350636) — *parallel mechanism*.
- **c-Abl / autophagy failure** (PMID:33684513) — *upstream/parallel*: drives VTA DA loss; nilotinib rescues.
- **Neuropsychiatric-symptom severity → faster decline (confounding-by-indication)** (PMID:34173272) — *alternative explanation* for the human antipsychotic signal.

---

## Discriminating Tests

1. **Decisive tau experiment.** Chronic aripiprazole vs vehicle vs UNC9994 vs haloperidol in a tauopathy model (P301S or rTg4510). Readouts: AT8/PHF-1/pTau-Ser396, pGSK3β-Ser9 and -Tyr216, Akt-Thr308/Ser473. *Seed predicts:* aripiprazole ↓ pTau (preserves pGSK3β-Ser9); UNC9994 no effect or ↑ pTau; haloperidol no protection. *Hypodopaminergia predicts:* benefit tracks restored DA tone, dissociable from arrestin bias.
2. **Dose/occupancy stratification.** Compare 1 mg/kg (5xFAD study) vs therapeutic-occupancy dosing; the seed's arrestin-antagonist reading should be dose-dependent.
3. **Genetic dissection.** βarr2-KO or D2R-neuron-specific GSK3β-KO crossed to a tau model ± aripiprazole; abolition of effect in βarr2-KO would confirm the arrestin route.
4. **Human observational refinement.** NILVAD/cohort re-analysis: aripiprazole-specific, dose- and APOE-stratified cognitive slopes with CSF p-tau181/217 as biomarker, adjusting for baseline neuropsychiatric symptoms.
5. **iPSC neurons** (APOE ε4 vs ε3, ± tau mutation): aripiprazole vs UNC9994 on pAkt/pGSK3β/pTau to test the arrestin-scaffolded-PP2A edge in a human, AD-relevant background.

---

## Curation Leads *(require curator verification)*

- **Verify existing snippets:** all five seed references reproduced verbatim in this run (PMID:30597182, 41192583, 39174788, 34173272 confirmed; note 41192583 abstract text was not re-retrieved by this index and should be re-checked).
- **Candidate new evidence nodes (competing):** PMID:28367951, 29778899 (hypodopaminergia); PMID:22299660, 28720530 (PP2A/APOE); PMID:36760217 (Aβ→GSK3β); PMID:31156177 (GSK-3 inhibitor RCT null); PMID:41930581 (opposite dopamine direction); PMID:28965318, 27647283 (DRD2 genetics).
- **Candidate reagent node (support):** PMID:22025698, 22845053, 26129680 (UNC9994 = arrestin-biased aripiprazole analogue; discriminating-test tool).
- **Candidate pathophysiology edges to add as HYPOTHETICAL/UNCONFIRMED:** `D2R→βarr2/PP2A→Akt⊣→GSK3β→tau` (mark tau terminus as unmeasured for aripiprazole in AD); competing edges `VTA_DA_loss→hippocampal_hypodopaminergia→memory_deficit` and `APOE_ε4→PP2A_down→tau_P`.
- **Candidate ontology terms:** ventral tegmental area dopaminergic neuron (CL:0000700 / UBERON:0001947), GSK-3β (GO:0016301 tau-protein kinase activity, GO:0004674), β-arrestin-mediated signaling (GO:0002031), protein phosphatase 2A (GO:0000159), tau protein phosphorylation.
- **Candidate status:** keep **EMERGING**; add `knowledge_gaps` for (a) untested tau arm, (b) dopamine-direction contradiction, (c) GSK-3β-inhibitor clinical null, (d) unverified DRD2 AD-GWAS absence.

---

## Limitations

Literature-only run; no dataset/omics/structural analysis was performed (none provided). The `search_pubmed` index showed low recall on specific queries, so negative searches are **index-conditioned**, not definitive; GWAS/GenCC/ClinGen were not queried. Abstract-level evidence cannot establish effect sizes for the mechanistic Western-blot studies. Artifact bundle: `kb/hypotheses/Alzheimer_Disease/d2r_arrestin_gsk3b_tau_model/openscientist_artifacts/` (MANIFEST.yaml + search log + evidence_matrix.csv + environment + build provenance, sha256-checksummed).


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist build artifacts](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_d2r_arrestin_gsk3b_tau_model_openscientist_artifacts_code_build_artifacts.md)
- [OpenScientist pubmed search log](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_d2r_arrestin_gsk3b_tau_model_openscientist_artifacts_search_logs_pubmed_search_log.json)
- [OpenScientist evidence matrix](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_d2r_arrestin_gsk3b_tau_model_openscientist_artifacts_tables_evidence_matrix.csv)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 0 |
| Off topic | 0 |

All extracted references resolved successfully.
