---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-09T10:14:58.648970'
end_time: '2026-10-09T10:40:19.284411'
duration_seconds: 1520.64
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Major Depressive Disorder
  category: Complex
  hypothesis_group_id: serotonin_foxo_stress_transcription_model
  hypothesis_label: Serotonin-Restrained FOXO Stress Transcription Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: serotonin_foxo_stress_transcription_model\n\
    hypothesis_label: Serotonin-Restrained FOXO Stress Transcription Model\nstatus:\
    \ EMERGING\ndescription: 'Serotonergic tone restrains FOXO-family stress transcription\
    \ through insulin/IGF-1 receptor\n  signalling, so that loss of serotonin de-represses\
    \ a FOXO-driven stress program that antidepressants,\n  lithium and clozapine\
    \ act on. The proposal rests on Caenorhabditis elegans genetics: serotonin-null\n\
    \  tph-1 animals show nuclear accumulation of the FOXO orthologue DAF-16 and constitutive\
    \ stress states,\n  exogenous serotonin and fluoxetine prevent that accumulation,\
    \ the insulin receptor DAF-2 sits downstream\n  of serotonin, and lithium and\
    \ clozapine need beta-arrestin and SGK to keep DAF-16 out of the nucleus.\n  Whether\
    \ human MDD involves FOXO1, FOXO3 or FOXO4 in a comparable serotonin-dependent\
    \ way is the open\n  question; the entry has no insulin or FOXO pathophysiology\
    \ node, and this hypothesis is recorded to\n  decide whether one is warranted.'\n\
    evidence:\n- reference: PMID:17141627\n  reference_title: Serotonin targets the\
    \ DAF-16/FOXO signaling pathway to modulate stress responses.\n  supports: SUPPORT\n\
    \  evidence_source: MODEL_ORGANISM\n  directness: INDIRECT\n  snippet: Serotonin-deficient\
    \ tph-1 mutants, like daf-2 mutants, exhibit DAF-16 nuclear accumulation\n   \
    \ and constitutive physiological stress states. Exogenous 5HT and fluoxetine (Prozac)\
    \ prevented DAF-16\n    nuclear accumulation in wild-type animals under stresses.\n\
    \  explanation: 'The core observation: serotonin loss phenocopies insulin-receptor\
    \ loss at the level of\n    FOXO localisation, and an SSRI reverses it. INDIRECT\
    \ because the organism is a nematode and the readout\n    is DAF-16 localisation,\
    \ not a depression phenotype.'\n- reference: PMID:17141627\n  reference_title:\
    \ Serotonin targets the DAF-16/FOXO signaling pathway to modulate stress responses.\n\
    \  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n  directness: INDIRECT\n\
    \  snippet: Genetic analyses imply that DAF-2 is a downstream target of 5HT signaling\
    \ and that distinct\n    serotonergic neurons act through distinct 5HT receptors\
    \ to influence distinct DAF-16-mediated stress\n    responses.\n  explanation:\
    \ Places the insulin receptor downstream of serotonin, which is the direction\
    \ the hypothesis\n    asserts.\n- reference: PMID:10676966\n  reference_title:\
    \ Food and metabolic signalling defects in a Caenorhabditis elegans serotonin-synthesis\n\
    \    mutant.\n  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n  directness:\
    \ INDIRECT\n  snippet: This metabolic dysregulation is, in part, due to downregulation\
    \ of transforming growth factor-beta\n    and insulin-like neuroendocrine signals.\n\
    \  explanation: The earlier serotonin-null characterisation that first tied serotonin\
    \ loss to reduced insulin-like\n    neuroendocrine signalling.\n- reference: PMID:21732403\n\
    \  reference_title: Clozapine and lithium require Caenorhabditis elegans \u03B2\
    -arrestin and serum- and glucocorticoid-inducible\n    kinase to affect Daf-16\
    \ (FOXO) localization.\n  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n\
    \  directness: INDIRECT\n  snippet: Lithium, a mood stabilizer often used to treat\
    \ psychosis, also requires \u03B2-arrestin and SGK\n    to suppress the nuclear\
    \ localization of DAF-16.\n  explanation: A second drug the entry lists, lithium,\
    \ converges on the same FOXO localisation readout,\n    through a kinase route\
    \ rather than through serotonin.\nnotes: 'Recorded under issue #13749 to drive\
    \ a focused deep-research pass on the serotonin-to-FOXO arm.\n  Every supporting\
    \ item is from C. elegans; no human MDD evidence for FOXO involvement is recorded\
    \ here\n  yet. Promotion to a pathophysiology node requires human evidence; otherwise\
    \ the outcome is a HUMAN_MODEL_MISMATCH\n  discussion attached to Monoamine Deficiency.'"
  artifact_dir: kb/hypotheses/Major_Depressive_Disorder/serotonin_foxo_stress_transcription_model/openscientist_artifacts
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
citation_count: 19
term_validation:
  total_terms: 2
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 7
artifact_sources:
  openscientist_artifacts_zip: 7
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
- filename: kb_hypotheses_Major_Depressive_Disorder_serotonin_foxo_stress_transcription_model_openscientist_artifacts_data_foxo1_mdd_crediblesets.json
  path: openscientist_artifacts/kb_hypotheses_Major_Depressive_Disorder_serotonin_foxo_stress_transcription_model_openscientist_artifacts_data_foxo1_mdd_crediblesets.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist foxo1 mdd crediblesets
- filename: kb_hypotheses_Major_Depressive_Disorder_serotonin_foxo_stress_transcription_model_openscientist_artifacts_data_mdd_top_targets_context.csv
  path: openscientist_artifacts/kb_hypotheses_Major_Depressive_Disorder_serotonin_foxo_stress_transcription_model_openscientist_artifacts_data_mdd_top_targets_context.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist mdd top targets context
- filename: kb_hypotheses_Major_Depressive_Disorder_serotonin_foxo_stress_transcription_model_openscientist_artifacts_data_opentargets_foxo_mdd_associations.csv
  path: openscientist_artifacts/kb_hypotheses_Major_Depressive_Disorder_serotonin_foxo_stress_transcription_model_openscientist_artifacts_data_opentargets_foxo_mdd_associations.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist opentargets foxo mdd associations
- filename: kb_hypotheses_Major_Depressive_Disorder_serotonin_foxo_stress_transcription_model_openscientist_artifacts_data_opentargets_foxo_mdd_associations.json
  path: openscientist_artifacts/kb_hypotheses_Major_Depressive_Disorder_serotonin_foxo_stress_transcription_model_openscientist_artifacts_data_opentargets_foxo_mdd_associations.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist opentargets foxo mdd associations
- filename: kb_hypotheses_Major_Depressive_Disorder_serotonin_foxo_stress_transcription_model_openscientist_artifacts_logs_search_log.md
  path: openscientist_artifacts/kb_hypotheses_Major_Depressive_Disorder_serotonin_foxo_stress_transcription_model_openscientist_artifacts_logs_search_log.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist search log
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Major Depressive Disorder
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** serotonin_foxo_stress_transcription_model
- **Hypothesis Label:** Serotonin-Restrained FOXO Stress Transcription Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: serotonin_foxo_stress_transcription_model
hypothesis_label: Serotonin-Restrained FOXO Stress Transcription Model
status: EMERGING
description: 'Serotonergic tone restrains FOXO-family stress transcription through insulin/IGF-1 receptor
  signalling, so that loss of serotonin de-represses a FOXO-driven stress program that antidepressants,
  lithium and clozapine act on. The proposal rests on Caenorhabditis elegans genetics: serotonin-null
  tph-1 animals show nuclear accumulation of the FOXO orthologue DAF-16 and constitutive stress states,
  exogenous serotonin and fluoxetine prevent that accumulation, the insulin receptor DAF-2 sits downstream
  of serotonin, and lithium and clozapine need beta-arrestin and SGK to keep DAF-16 out of the nucleus.
  Whether human MDD involves FOXO1, FOXO3 or FOXO4 in a comparable serotonin-dependent way is the open
  question; the entry has no insulin or FOXO pathophysiology node, and this hypothesis is recorded to
  decide whether one is warranted.'
evidence:
- reference: PMID:17141627
  reference_title: Serotonin targets the DAF-16/FOXO signaling pathway to modulate stress responses.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  directness: INDIRECT
  snippet: Serotonin-deficient tph-1 mutants, like daf-2 mutants, exhibit DAF-16 nuclear accumulation
    and constitutive physiological stress states. Exogenous 5HT and fluoxetine (Prozac) prevented DAF-16
    nuclear accumulation in wild-type animals under stresses.
  explanation: 'The core observation: serotonin loss phenocopies insulin-receptor loss at the level of
    FOXO localisation, and an SSRI reverses it. INDIRECT because the organism is a nematode and the readout
    is DAF-16 localisation, not a depression phenotype.'
- reference: PMID:17141627
  reference_title: Serotonin targets the DAF-16/FOXO signaling pathway to modulate stress responses.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  directness: INDIRECT
  snippet: Genetic analyses imply that DAF-2 is a downstream target of 5HT signaling and that distinct
    serotonergic neurons act through distinct 5HT receptors to influence distinct DAF-16-mediated stress
    responses.
  explanation: Places the insulin receptor downstream of serotonin, which is the direction the hypothesis
    asserts.
- reference: PMID:10676966
  reference_title: Food and metabolic signalling defects in a Caenorhabditis elegans serotonin-synthesis
    mutant.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  directness: INDIRECT
  snippet: This metabolic dysregulation is, in part, due to downregulation of transforming growth factor-beta
    and insulin-like neuroendocrine signals.
  explanation: The earlier serotonin-null characterisation that first tied serotonin loss to reduced insulin-like
    neuroendocrine signalling.
- reference: PMID:21732403
  reference_title: Clozapine and lithium require Caenorhabditis elegans β-arrestin and serum- and glucocorticoid-inducible
    kinase to affect Daf-16 (FOXO) localization.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  directness: INDIRECT
  snippet: Lithium, a mood stabilizer often used to treat psychosis, also requires β-arrestin and SGK
    to suppress the nuclear localization of DAF-16.
  explanation: A second drug the entry lists, lithium, converges on the same FOXO localisation readout,
    through a kinase route rather than through serotonin.
notes: 'Recorded under issue #13749 to drive a focused deep-research pass on the serotonin-to-FOXO arm.
  Every supporting item is from C. elegans; no human MDD evidence for FOXO involvement is recorded here
  yet. Promotion to a pathophysiology node requires human evidence; otherwise the outcome is a HUMAN_MODEL_MISMATCH
  discussion attached to Monoamine Deficiency.'
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
result beneath `kb/hypotheses/Major_Depressive_Disorder/serotonin_foxo_stress_transcription_model/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.


## Output

# Serotonin-Restrained FOXO Stress Transcription Model in Major Depressive Disorder — Hypothesis-Search Report

**Hypothesis ID:** `serotonin_foxo_stress_transcription_model`
**Hypothesis Label:** Serotonin-Restrained FOXO Stress Transcription Model
**Target Disease:** Major Depressive Disorder (MDD; MONDO_0002009), Category: Complex
**KB Status:** EMERGING
**Report date:** 2026-10-09 (OpenScientist autonomous run, 5 iterations)

---

## Executive Judgment

**Verdict: Partially supported overall, but only weakly supported in humans.** The hypothesis proposes that serotonergic tone restrains FOXO-family stress transcription through insulin/IGF-1 receptor signalling, so that loss of serotonin de-represses a FOXO-driven stress program on which antidepressants, lithium, and clozapine act. After five iterations integrating primary literature, a negative human cohort, Mendelian-randomization evidence, and a computational interrogation of the Open Targets Platform (v26.9), the evidence splits sharply by organism.

The **model-organism backbone is strong and internally consistent**: in *Caenorhabditis elegans*, serotonin-null *tph-1* mutants phenocopy insulin-receptor *daf-2* mutants in DAF-16/FOXO nuclear accumulation; exogenous serotonin and fluoxetine prevent that accumulation; the insulin receptor sits genetically downstream of serotonin; and lithium and clozapine converge on the same DAF-16 localisation readout through β-arrestin and SGK ([PMID:17141627](https://pubmed.ncbi.nlm.nih.gov/17141627/), [PMID:10676966](https://pubmed.ncbi.nlm.nih.gov/10676966/), [PMID:21732403](https://pubmed.ncbi.nlm.nih.gov/21732403/)). Independently, **mammalian stress models repeatedly implicate an AKT→FOXO node** whose nuclear/active state is pro-depressive and whose cytoplasmic sequestration is antidepressant, with fluoxetine among the reversing agents ([PMID:36819781](https://pubmed.ncbi.nlm.nih.gov/36819781/), [PMID:36039087](https://pubmed.ncbi.nlm.nih.gov/36039087/), [PMID:41249439](https://pubmed.ncbi.nlm.nih.gov/41249439/), [PMID:37173696](https://pubmed.ncbi.nlm.nih.gov/37173696/)).

The **human arm, however, does not close the loop.** No study demonstrates a serotonin→FOXO edge in any mammal; the specific causal step that defines the hypothesis is untested outside the nematode. Rodent directionality is internally contradictory (nuclear FOXO3a is pro-depressive in one model, yet dentate-gyrus FoxO3a overexpression is protective in another). A direct human cohort found plasma FOXO3 unassociated with depressive symptoms after adjustment ([PMID:42632434](https://pubmed.ncbi.nlm.nih.gov/42632434/)). Human genetics (Open Targets v26.9) nominates only FOXO1 — not the rodent-favoured FOXO3 — with a single, moderate MDD credible-set signal that traces to a *cognition×MDD interaction* GWAS rather than a primary MDD case/control scan, while the insulin-receptor genes (INSR, IGF1R, SGK1, AKT1) have no MDD genetic support at all, and FOXO1 ranks far below MDD's monoaminergic/synaptic genetic core (DRD2, HTR2A, GRIN2A, GABRA1). Finally, the **upstream "loss of serotonin" premise is itself contested in humans** by the Moncrieff umbrella review, surviving at best as a subtype-restricted claim. The recommended curation outcome is a **HUMAN_MODEL_MISMATCH discussion attached to Monoamine Deficiency**, with at most a subtype-restricted EMERGING FOXO1 lead — **not** a primary insulin/FOXO pathophysiology node.

---

## Key Findings

### F001 — The serotonin→DAF-2→DAF-16/FOXO chain is well-evidenced in *C. elegans* (seed backbone)

The hypothesis's foundational evidence is a single, coherent body of nematode genetics. In [PMID:17141627](https://pubmed.ncbi.nlm.nih.gov/17141627/), serotonin-deficient *tph-1* mutants, like *daf-2* insulin-receptor mutants, exhibit DAF-16 nuclear accumulation and constitutive physiological stress states, and *"Exogenous 5HT and fluoxetine (Prozac) prevented DAF-16 nuclear accumulation in wild-type animals under stresses."* Genetic epistasis places DAF-2 downstream of 5-HT signalling, with distinct serotonergic neurons acting through distinct 5-HT receptors to influence distinct DAF-16-mediated stress responses. The drug-convergence claim is supported in [PMID:21732403](https://pubmed.ncbi.nlm.nih.gov/21732403/): *"Lithium, a mood stabilizer often used to treat psychosis, also requires β-arrestin and SGK to suppress the nuclear localization of DAF-16."* An earlier characterisation ([PMID:10676966](https://pubmed.ncbi.nlm.nih.gov/10676966/)) first tied serotonin loss to reduced insulin-like neuroendocrine signalling: *"This metabolic dysregulation is, in part, due to downregulation of transforming growth factor-beta and insulin-like neuroendocrine signals."*

This is the strongest **direct** evidence for the hypothesis as stated — but its directness for MDD is INDIRECT on two counts: the organism is a nematode, and the readout is subcellular DAF-16 localisation, not a depression phenotype. The chain is real and reproducible in worms; the question is whether it generalises to human disease.

### F002 — Mammalian stress models independently support a pro-depressive AKT→FOXO node reversed by antidepressants

Multiple independent rodent studies converge on an AKT→FOXO axis in which **nuclear/active FOXO is pro-depressive and cytoplasmic sequestration is antidepressant**:

- **[PMID:36819781](https://pubmed.ncbi.nlm.nih.gov/36819781/)** — Chronic unpredictable mild stress (CUMS) produced *"increased expression of AKT, FOXO, and Bim in the hippocampus. These alterations were ameliorated by administration of 20 mg/kg or 40 mg/kg of traxoprodil"* (with fluoxetine as comparator), raising the pro-apoptotic FOXO target Bim and reducing BDNF/pERK/pCREB.
- **[PMID:36039087](https://pubmed.ncbi.nlm.nih.gov/36039087/)** — The antidepressant Chaihu Shugan San increases SIRT1 and *"could also promote FOXO1 translocation to the cytoplasm through SIRT1 signaling, which triggered FOXO1 protein degradation,"* i.e., it acts by excluding/degrading FOXO1.
- **[PMID:41249439](https://pubmed.ncbi.nlm.nih.gov/41249439/)** — NDRG2 upregulation inhibits AKT and *"promotes the nuclear translocation of FoxO3a, leading to the transcriptional activation of the pro-apoptotic factor Puma,"* driving astrocyte apoptosis and depressive-like behaviour.
- **[PMID:37173696](https://pubmed.ncbi.nlm.nih.gov/37173696/)** and **[PMID:40237232](https://pubmed.ncbi.nlm.nih.gov/40237232/)** — TLR4/PI3K/AKT/FOXO1 and SIRT1/FOXO1 antidepressant mechanisms, both acting by suppressing/excluding FOXO1.

This is the hypothesis's best **mammalian** support. Crucially, however, **none of these studies manipulates serotonin to move FOXO**; they establish the downstream AKT→FOXO→stress-program arm but leave the defining serotonin→FOXO edge untested.

### F003 — Directional conflict in mammals and a negative human biomarker

The mammalian FOXO picture is not directionally clean. Against the pro-depressive framing of F002, **[PMID:41622191](https://pubmed.ncbi.nlm.nih.gov/41622191/)** shows that AAV overexpression of FoxO3a in the dentate gyrus *alleviates* CUS-induced anxiety- and depression-like behaviours and cognitive impairment — FOXO3a as **protective** (CUS *downregulates* dentate-gyrus FoxO3a, and restoring it rescues the phenotype). So within rodents FOXO3a is cast as both pro- and anti-depressive depending on cell type and region (astrocytic apoptosis vs. dentate-gyrus neuroplasticity).

Human evidence is weak-to-negative. In a cerebral small-vessel-disease cohort (183 patients vs. 150 controls), plasma FOXO3 was elevated with cognitive impairment but, *"After adjustment, FOXO3 remained unassociated with depressive symptoms (P = 0.232)"* ([PMID:42632434](https://pubmed.ncbi.nlm.nih.gov/42632434/)). No human MDD brain or genetic study directly linking serotonergic tone to FOXO was retrieved.

### F004 — Human genetics nominates FOXO1 (not FOXO3/4), and the insulin-receptor arm has no genetic support

Interrogating the **Open Targets Platform GraphQL API (v26.9.0, disease MONDO_0002009, retrieved 2026-10-09)** produced a clear picture:

| Gene | Overall score | Genetic-association datatype | GWAS credible-set rows | Notes |
|---|---|---|---|---|
| **FOXO1** | 0.187 | 0.285 | 1 (L2G=0.469) | Only FOXO with a credible set |
| FOXO3 | 0.038 | — | 0 | Literature-only |
| FOXO4 / FOXO6 | no association | — | 0 | — |
| INSR | 0.281 | — | 0 | Clinical + literature only |
| IGF1R | 0.014 | — | 0 | Literature only |
| SGK1 | 0.101 | — | 0 | Literature only |
| AKT1 | 0.083 | — | 0 | Literature only |
| SLC6A4 (anchor) | 0.637 | — | clinical 0.999 | Positive control |
| TPH2 (anchor) | 0.442 | 0.375 | genetic_literature 0.608 | Positive control |

The serotonin genes behave as expected positive anchors, validating the query. But the FOXO-family signal is carried by **FOXO1 alone**, with only a moderate genetic association, and **every gene in the insulin/IGF-1 receptor arm lacks any MDD GWAS credible-set or gene-burden evidence.** This is a direct mismatch with the hypothesis, which centres the insulin-receptor edge and whose mammalian mechanism rests on FOXO3-type biology.

### F005 — The insulin pathway links to MDD in humans, but as a metabolic/comorbid arm, not a serotonin→FOXO edge

Human Mendelian randomization does support an insulin-pathway connection to MDD — just not the one the hypothesis draws. In [PMID:40595333](https://pubmed.ncbi.nlm.nih.gov/40595333/): *"a doubling in MDD genetic liability was associated with 1.14 higher odds of T2D (95% CI:1.09, 1.19), whilst a doubling in T2D genetic liability associated with 1.02 higher odds of MDD (95% CI:1.01, 1.03),"* with an obesity-mediated insulin-resistance pathway implicated (OR 1.06, 95% CI 1.04–1.09) and BMI attenuating the relationship. This is corroborated by multi-trait GWAS ([PMID:41555281](https://pubmed.ncbi.nlm.nih.gov/41555281/)) and a genomic systematic review ([PMID:41780463](https://pubmed.ncbi.nlm.nih.gov/41780463/)) reporting shared MDD–metabolic-syndrome architecture and a unidirectional MDD→MetS causal effect. The insulin node in human MDD is therefore real, but it operates as a **parallel metabolic/comorbid link** rather than as the serotonin-gated transcriptional switch the hypothesis requires.

### F006 — The sole FOXO1 signal derives from a cognition×MDD interaction GWAS, not a primary MDD GWAS

Resolving the FOXO1 credible set (Open Targets v26.9, retrieved 2026-10-09) qualifies the human-genetics support substantially. The single `gwas_credible_sets` evidence is variant **rs180828263** (13_40534758_C_T, chr13:40,534,758, ~21 kb 5′ of FOXO1), p=4×10⁻⁹, PICS fine-mapped *"based on reported top hit"* (not full statistical fine-mapping), L2G=0.469. Its parent study is **GCST90096932 = "Cognitive function (executive function) × major depressive disorder interaction (2df)" GWAS** ([PMID:34782712](https://pubmed.ncbi.nlm.nih.gov/34782712/), n=9,567) — a gene×phenotype interaction scan, **not** a primary MDD case/control GWAS. The one human genetic thread connecting FOXO to MDD is thus about a *cognition-conditioned* MDD phenotype, narrowing any claim to a cognitive subtype.

### F007 — The upstream "loss of serotonin" premise is contested; serotonin deficiency may characterise only a subtype

The hypothesis's upstream node assumes "loss of serotonin." The Moncrieff et al. systematic umbrella review ([PMID:35854107](https://pubmed.ncbi.nlm.nih.gov/35854107/); republished [PMID:42538881](https://pubmed.ncbi.nlm.nih.gov/42538881/)) *"aimed to synthesise and evaluate evidence on whether depression is associated with lowered serotonin concentration or activity"* and found no consistent evidence that depression is associated with lowered serotonin concentration or activity. A published riposte ([PMID:36356194](https://pubmed.ncbi.nlm.nih.gov/36356194/)) agrees the simple equation is outdated but argues *"The decreased activity of serotonin, which undoubtedly plays an essential role in the pathogenesis of depression, is characteristic of only a subgroup of depressed subjects"* (agitated/anxious, insomnia, reduced appetite, SSRI-responsive), with anhedonic/anergic cases driven more by dopamine/noradrenaline. Separately, **direct PubMed searches for a mammalian serotonin→FOXO edge returned nothing usable** (searches 2026-10-09: "serotonin 5-HT receptor FOXO transcription factor brain neurons" returned only a *C. elegans* paper; "fluoxetine FOXO3a hippocampus phosphorylation" and "fluoxetine Akt FOXO neuronal" returned 0 results).

### F008 — FOXO1 ranks far below MDD's neurotransmitter/synaptic genetic core

Contextualising within the full MDD target landscape (Open Targets v26.9, MONDO_0002009, 6,780 associated targets, retrieved 2026-10-09), the top MDD targets by overall score are neurotransmitter/synaptic genes led by genetic-association signals: **DRD2** (0.743, genetic 0.854), **HTR2A** (0.703, 0.547), **GRIN2A** (0.675, 0.472), **GABRA1** (0.672, 0.423), followed by SLC6A4, HTR1A, SLC6A3/2, multiple GABRs, DRD3/4, MAOA, GRIN2B. **FOXO1 (0.187) does not appear in the top 30; FOXO3 (0.038) is literature-only.** The dominant human genetic architecture of MDD favours monoamine/glutamate/GABA models over a FOXO-insulin model.

### F009 — Integrated synthesis: HUMAN_MODEL_MISMATCH with a subtype-restricted FOXO1 lead

Integrating all eight findings, the hypothesis is **partially/weakly supported in humans**. A strong *C. elegans* backbone and independent mammalian AKT→FOXO support coexist with rodent directional conflict, a negative human biomarker, an insulin arm supported only as a comorbid metabolic link, a contested upstream serotonin premise, no direct mammalian serotonin→FOXO paper, and a human FOXO1 genetic signal that is both subtype-conditioned and far outside MDD's genetic core.

---

## Mechanistic Model / Interpretation

The hypothesis asserts a single causal chain. The diagram below annotates each edge with the strength of evidence found in this search.

```
                    SEED HYPOTHESIS CHAIN               EVIDENCE STATUS (this search)
  ┌────────────────────────────────────────────────┐
  │ (1) Serotonergic tone (5-HT)                     │ Upstream node CONTESTED in humans
  │              │                                   │ (Moncrieff umbrella review; subtype-
  │              ▼  restrains                         │  restricted at best — F007)
  │ (2) Insulin / IGF-1 receptor signalling          │ Worms: STRONG (DAF-2 downstream of 5-HT, F001)
  │     (DAF-2 in worm; INSR/IGF1R in human)         │ Humans: NO GWAS evidence for INSR/IGF1R (F004);
  │              │                                   │         insulin link exists but as METABOLIC
  │              ▼  controls nuclear access of        │         COMORBIDITY, not 5-HT-gated (F005)
  │ (3) FOXO stress transcription factor              │ Worms: STRONG (DAF-16, F001)
  │     (DAF-16 in worm; FOXO1/3/4 in human)         │ Mammals: SUPPORTED but DIRECTIONALLY
  │              │                                   │          CONFLICTED (F002 pro- vs F003 protective)
  │              ▼  de-repressed → drives             │ Humans: FOXO3 biomarker negative (PMID 42632434);
  │ (4) FOXO-driven stress / apoptotic program        │         FOXO1 only, subtype-conditioned (F004/F006)
  │              │                                   │
  │              ▼                                   │
  │ (5) Depression phenotype / MDD                    │ serotonin→FOXO EDGE: NOT DEMONSTRATED
  │                                                  │ in ANY mammal (F007 negative searches)
  └────────────────────────────────────────────────┘
       Drugs (antidepressants, lithium, clozapine) act to keep FOXO cytoplasmic:
       Worms STRONG (F001); Mammalian antidepressants echo it (F002) but via AKT/SIRT1/
       TLR4/β-arrestin, NOT demonstrably via serotonin.
```

**Interpretation.** The chain is fully instantiated and reproducible only in *C. elegans*. In mammals, the **downstream half** (AKT→FOXO→stress/apoptosis, reversible by antidepressants) is independently supported, but the **upstream half** that makes the hypothesis distinctive — serotonin *gating* FOXO via the insulin receptor — is the weakest link and is untested in any mammal. Two human-level facts actively pull against promoting a primary node: (i) the insulin-receptor genes carry no MDD genetic signal while FOXO1 (the wrong family member relative to the mammalian mechanism) carries only a subtype-conditioned one; and (ii) the human insulin→MDD relationship that *does* exist is a metabolic/obesity comorbidity, a parallel mechanism rather than the serotonin-gated switch. The most parsimonious reading is that FOXO is a **convergent downstream stress-transcription hub** engaged by many antidepressant mechanisms (SIRT1, PI3K/AKT, TLR4, β-arrestin/SGK), rather than a serotonin-specific effector.

---

## Evidence Base (Evidence Matrix)

| Citation | Evidence type | Role | Mechanistic claim tested | Key finding | Subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:17141627](https://pubmed.ncbi.nlm.nih.gov/17141627/) | Model organism (*C. elegans*) | **Supports** | Serotonin restrains DAF-16/FOXO via DAF-2 | *tph-1* phenocopies *daf-2*; 5-HT & fluoxetine prevent DAF-16 nuclear accumulation; DAF-2 downstream of 5-HT | Nematode stress states | High for worm; INDIRECT for MDD (not a depression readout) |
| [PMID:10676966](https://pubmed.ncbi.nlm.nih.gov/10676966/) | Model organism | **Supports** | Serotonin loss → reduced insulin-like signalling | Serotonin-synthesis mutant downregulates TGF-β and insulin-like neuroendocrine signals | Nematode metabolism | Moderate; INDIRECT |
| [PMID:21732403](https://pubmed.ncbi.nlm.nih.gov/21732403/) | Model organism | **Supports** | Lithium/clozapine act on FOXO localisation | Both require β-arrestin + SGK to keep DAF-16 cytoplasmic | Nematode drug response | Moderate; INDIRECT; drug route is kinase, not serotonin |
| [PMID:36819781](https://pubmed.ncbi.nlm.nih.gov/36819781/) | Model organism (rodent) | **Supports (downstream)** | Chronic stress raises hippocampal AKT/FOXO/Bim | CUMS ↑AKT/FOXO/Bim; reversed by traxoprodil (fluoxetine comparator) | Hippocampus, CUMS | Moderate; serotonin→FOXO edge not tested |
| [PMID:36039087](https://pubmed.ncbi.nlm.nih.gov/36039087/) | Model organism (rodent) | **Supports (downstream)** | Antidepressant excludes/degrades FOXO1 | SIRT1 drives FOXO1 cytoplasmic translocation + degradation | Hippocampal angiogenesis | Moderate; herbal formulation; not serotonin-specific |
| [PMID:41249439](https://pubmed.ncbi.nlm.nih.gov/41249439/) | Model organism (rodent) | **Supports (downstream)** | AKT inhibition → FoxO3a nuclear → Puma apoptosis | NDRG2→PP2A→AKT↓→FoxO3a→Puma drives astrocyte apoptosis & depression | Astrocytes | Moderate; pro-depressive direction |
| [PMID:37173696](https://pubmed.ncbi.nlm.nih.gov/37173696/) | Model organism (rodent) | **Supports (downstream)** | TLR4/PI3K/AKT/FOXO1 in neuroinflammatory depression | Antidepressant suppresses FOXO1 via nuclear export | Neuroinflammation | Moderate; not serotonin-gated |
| [PMID:40237232](https://pubmed.ncbi.nlm.nih.gov/40237232/) | Model organism (rodent) | **Supports (downstream)** | SIRT1/FOXO1 microglial axis | Urolithin B restores SIRT1/FOXO1; antidepressant | Microglia | Moderate; not serotonin-gated |
| [PMID:41622191](https://pubmed.ncbi.nlm.nih.gov/41622191/) | Model organism (rodent) | **Qualifies / conflicts** | FoxO3a direction in dentate gyrus | AAV-FoxO3a overexpression *alleviates* depression-like behaviour | Dentate gyrus | Moderate; opposite sign to F002 |
| [PMID:42632434](https://pubmed.ncbi.nlm.nih.gov/42632434/) | Human clinical | **Refutes (biomarker)** | Plasma FOXO3 tracks depressive symptoms | After adjustment, FOXO3 unassociated with depressive symptoms (P=0.232) | Cerebral small-vessel disease, 183 vs 150 | Moderate; peripheral biomarker, not brain |
| Open Targets v26.9 (computational) | Computational | **Qualifies** | Which FOXO/insulin genes have MDD genetic evidence | Only FOXO1 has a credible set (L2G 0.469); INSR/IGF1R/SGK1/AKT1/FOXO3/4/6 none | MONDO_0002009 | High for query; FOXO1 signal moderate |
| [PMID:34782712](https://pubmed.ncbi.nlm.nih.gov/34782712/) (GCST90096932) | Human genetic | **Qualifies** | Source of FOXO1 signal | rs180828263 from cognition×MDD interaction GWAS, not primary MDD GWAS | Cognition-conditioned MDD, n=9,567 | Moderate; interaction scan, PICS not full fine-mapping |
| [PMID:40595333](https://pubmed.ncbi.nlm.nih.gov/40595333/) | Human genetic (MR) | **Qualifies / competing** | Insulin pathway–MDD causality | Bidirectional MDD↔T2D; obesity-mediated insulin resistance | Metabolic comorbidity | High; but a parallel metabolic arm, not serotonin→FOXO |
| [PMID:41555281](https://pubmed.ncbi.nlm.nih.gov/41555281/) | Human genetic | **Qualifies** | Shared MDD–MetS architecture | Bidirectional genetic correlation, glucose/insulin pathways | Metabolic comorbidity | Moderate (multi-trait GWAS) |
| [PMID:41780463](https://pubmed.ncbi.nlm.nih.gov/41780463/) | Review (genomic) | **Qualifies** | MDD→MetS causal direction | Unidirectional MDD→MetS; shared glucose/lipid/inflammation pathways | Metabolic comorbidity | Review-level synthesis |
| [PMID:35854107](https://pubmed.ncbi.nlm.nih.gov/35854107/) / [PMID:42538881](https://pubmed.ncbi.nlm.nih.gov/42538881/) | Review (umbrella) | **Refutes (upstream)** | Is MDD associated with low serotonin? | No consistent evidence for lowered serotonin concentration/activity | MDD at large | High-level synthesis; contested premise |
| [PMID:36356194](https://pubmed.ncbi.nlm.nih.gov/36356194/) | Review / commentary | **Qualifies (upstream)** | Serotonin hypofunction scope | Characteristic of only a depressed subgroup (agitated/anxious, SSRI-responsive) | MDD subtype | Commentary; argues subtype restriction |
| [PMID:28088287](https://pubmed.ncbi.nlm.nih.gov/28088287/) | Model organism (rodent) | **Qualifies (context)** | IGF/insulin–monoamine link | Igfbp3-null mice: ↓IGF-1, ↓Akt/ERK, ↓serotonin & dopamine, behavioural impairment | Brain development | Supports IGF–monoamine coupling generically |

---

## Data and Tool Use

### Datasets, databases, and APIs

| Resource | Accession / URI | Version / snapshot | Retrieval date | Access status | Query / filter | Resolves & relevant? |
|---|---|---|---|---|---|---|
| Open Targets Platform GraphQL API | https://api.platform.opentargets.org/api/v4/graphql; disease MONDO_0002009 | v26.9.0 | 2026-10-09 | **Accessed** (succeeded) | Target–disease association scores + genetic evidence for FOXO1/3/4/6, INSR, IGF1R, SGK1, AKT1, SLC6A4, TPH2; top-30 MDD targets; FOXO1 credible-set resolution | Resolves; directly relevant |
| Open Targets credible set (FOXO1) | variant rs180828263; study GCST90096932 | v26.9.0 | 2026-10-09 | **Accessed** (succeeded) | L2G, PICS fine-mapping, parent study metadata | Resolves; relevant but subtype-conditioned |
| PubMed / NCBI E-utilities | — | live | 2026-10-08/09 | **Searched** (34 papers reviewed) | See negative-search log below | Relevant |
| GWAS Catalog (via Open Targets) | GCST90096932 | — | 2026-10-09 | **Cited via Open Targets** | Parent-study identity of FOXO1 signal | Resolves; relevant |
| GenCC / ClinGen | — | — | — | **Not queried** (unverified) | Gene–disease validity for FOXO1/3/4 in MDD | Flag as unverified absence |

### Negative / null searches (search log)

| Query | Database | Date | Result |
|---|---|---|---|
| "serotonin 5-HT receptor FOXO transcription factor brain neurons" | PubMed | 2026-10-09 | Only a *C. elegans* paper; no mammalian serotonin→FOXO study |
| "fluoxetine FOXO3a hippocampus phosphorylation" | PubMed | 2026-10-09 | 0 results |
| "fluoxetine Akt FOXO neuronal" | PubMed | 2026-10-09 | 0 results |
| INSR / IGF1R / SGK1 / AKT1 MDD GWAS credible-set evidence | Open Targets v26.9 | 2026-10-09 | 0 genetic rows for each |
| FOXO3 / FOXO4 / FOXO6 MDD genetic credible-set/burden | Open Targets v26.9 | 2026-10-09 | FOXO3 literature-only; FOXO4/6 no association |

### Analyses attempted (input → method → output)

| Analysis | Trace | Environment | Outcome | Limitation |
|---|---|---|---|---|
| FOXO/insulin MDD association scan | Open Targets GraphQL (MONDO_0002009) → GraphQL queries → `openscientist_artifacts/data/opentargets_foxo_mdd_associations.csv` + `queries/opentargets_queries.graphql` | Python (requests), Open Targets v26.9 API | **Succeeded** | API scores are aggregate; no raw patient data |
| FOXO1 credible-set resolution | Open Targets GraphQL → `openscientist_artifacts/data/foxo1_mdd_crediblesets.json` | Python, v26.9 API | **Succeeded** | PICS "reported top hit", not full fine-mapping |
| MDD top-target context | Open Targets GraphQL (6,780 targets) → `openscientist_artifacts/data/mdd_top_targets_context.csv` | Python, v26.9 API | **Succeeded** | Overall score is a composite heuristic |

No patient-level, omics, or controlled-access dataset was accessed; no such analysis was run. No structural-biology (Phenix) analysis was applicable to this literature/genetics hypothesis. **No analysis was silently substituted for another:** where a direct serotonin→FOXO literature link was sought and not found, that is reported above as a negative search, not as a completed analysis.

---

## Mechanistic Causal Chain — where literature is strong, inferred, or missing

| Causal step | Edge | Status |
|---|---|---|
| Serotonergic tone (upstream trigger) | — | **Contested** in humans (F007); subtype-restricted at best |
| 5-HT → insulin/IGF-1 receptor signalling | 5-HT ⟶ DAF-2/INSR | **Strong in worm** (F001); **no human genetic support** for INSR/IGF1R (F004) |
| Insulin/IGF-1 → FOXO nuclear exclusion | DAF-2/AKT ⟶ DAF-16/FOXO | **Strong in worm**; **supported in mammal** (AKT→FOXO) but **directionally conflicted** (F002/F003) |
| FOXO de-repression → stress/apoptotic program | FOXO ⟶ Bim/Puma/inflammation | **Supported in mammal** (F002) |
| Stress program → depression phenotype | → MDD | **Inferred**; human FOXO3 biomarker negative (F003); FOXO1 subtype-conditioned (F006) |
| Drugs keep FOXO cytoplasmic (therapeutic) | antidepressant/lithium/clozapine ⟶ FOXO | **Strong in worm**; **echoed in mammal** via AKT/SIRT1/β-arrestin, **not demonstrably via serotonin** |

**The single missing causal step that defines the hypothesis — a demonstrated serotonin→FOXO edge in a mammal — was not found.** This is the decisive gap for curation.

---

## Limitations and Knowledge Gaps

1. **No mammalian serotonin→FOXO edge (critical gap).** Scope: the defining link of the hypothesis. Why it matters: without it, the mammalian AKT→FOXO data support a *generic* stress hub, not a serotonin-restrained one. Checked: three targeted PubMed searches (2026-10-09) returned nothing usable. Resolution: a direct perturbation — e.g., serotonin depletion (PCPA) or 5-HT receptor agonism/antagonism in rodent hippocampus with FOXO nuclear-localisation readout, ± fluoxetine rescue.

2. **Wrong-family-member mismatch.** Mammalian mechanism centres FOXO3a (apoptosis/Puma/Bim); the only human genetic signal is FOXO1; FOXO3 is literature-only with a negative human biomarker (F003/F004). Resolution: human brain eQTL/expression and genetic fine-mapping distinguishing FOXO1 vs FOXO3 in MDD cohorts.

3. **Insulin-receptor arm has no human MDD genetic support.** INSR/IGF1R/SGK1/AKT1 all have 0 genetic credible-set rows in Open Targets v26.9 (F004). The human insulin–MDD link that exists is a metabolic comorbidity (F005), a different edge. Resolution: colocalisation of MDD GWAS with insulin-pathway eQTLs in brain tissue.

4. **Directional conflict in rodents (unresolved).** Nuclear FoxO3a is pro-depressive in astrocytes ([PMID:41249439](https://pubmed.ncbi.nlm.nih.gov/41249439/)) yet protective in dentate-gyrus neurons ([PMID:41622191](https://pubmed.ncbi.nlm.nih.gov/41622191/)). Scope: whether FOXO is net harmful or protective depends on cell type/region. Resolution: cell-type-specific conditional FOXO knockout/overexpression with matched behavioural batteries.

5. **Contested upstream premise.** The "loss of serotonin" node is not consistently supported in humans ([PMID:35854107](https://pubmed.ncbi.nlm.nih.gov/35854107/)); it may hold only for an agitated/anxious SSRI-responsive subtype ([PMID:36356194](https://pubmed.ncbi.nlm.nih.gov/36356194/)). Resolution: subtype-stratified serotonergic markers paired with FOXO readouts.

6. **FOXO1 signal is subtype-conditioned and weak.** rs180828263 arises from a cognition×MDD interaction GWAS (GCST90096932), PICS "reported top hit," L2G 0.469 (F006). Resolution: replication in independent primary MDD GWAS and in cognitive-subtype-stratified cohorts.

7. **Source/dataset absences checked.** No clinical/known-drug evidence tying FOXO genes to MDD therapeutics in Open Targets v26.9 (2026-10-09). GenCC and ClinGen were **not** separately queried and must be labeled **unverified** rather than claimed absent until a dated query is logged.

---

## Alternative Models

| Model | Relationship to seed | Summary |
|---|---|---|
| **Monoamine / synaptic genetic core** (DRD2, HTR2A, GRIN2A, GABRA1, SLC6A4, HTR1A) | **Competing / more parsimonious** | Dominates MDD's human genetic architecture (F008); explains antidepressant pharmacology without a FOXO node. |
| **AKT/FOXO as a convergent downstream stress hub** | **Downstream consequence** | FOXO engaged by SIRT1, PI3K/AKT, TLR4, β-arrestin/SGK — a shared effector of many antidepressant mechanisms, not serotonin-specific (F002). |
| **Insulin-resistance / metabolic-comorbidity model** | **Parallel mechanism / upstream in a subset** | Bidirectional MDD↔T2D, obesity-mediated (F005); implicates insulin pathway but via metabolic route, not 5-HT gating. |
| **Neuroinflammation (TLR4/NF-κB, microglia)** | **Parallel / upstream** | Drives FOXO1 and depressive behaviour ([PMID:37173696](https://pubmed.ncbi.nlm.nih.gov/37173696/), [PMID:40237232](https://pubmed.ncbi.nlm.nih.gov/40237232/)); FOXO is effector, inflammation the trigger. |
| **Neurotrophic/BDNF–neurogenesis model** | **Parallel / downstream** | CUMS reduces BDNF/pCREB alongside FOXO changes (F002); FOXO3a protective via neuroplasticity in DG (F003). |
| **IGF/BDNF/serotonin "triumvirate" of stress signalling** ([PMID:15541711](https://pubmed.ncbi.nlm.nih.gov/15541711/), [PMID:28088287](https://pubmed.ncbi.nlm.nih.gov/28088287/)) | **Upstream context** | Couples IGF signalling to monoamines generically, consistent with but broader than the serotonin→FOXO edge. |

---

## Discriminating Tests

1. **Direct serotonin→FOXO perturbation in rodent brain (highest priority).** Deplete serotonin (PCPA) or manipulate specific 5-HT receptors in hippocampus/cortex; read out FOXO1 and FOXO3a nuclear:cytoplasmic ratio by quantitative immunofluorescence; test fluoxetine rescue. *Expected if hypothesis true:* serotonin loss drives FOXO nuclear accumulation, reversed by fluoxetine, and blocked by constitutively active AKT.

2. **Cell-type-specific FOXO manipulation with behaviour.** Conditional FOXO1 vs FOXO3a knockout/overexpression in astrocytes vs dentate-gyrus neurons under CUS. *Expected:* resolves the pro- vs anti-depressive directional conflict and identifies the disease-relevant family member.

3. **Human brain colocalisation.** Colocalise MDD GWAS signals (primary case/control, and cognition-stratified) with brain eQTLs for FOXO1, FOXO3, INSR, IGF1R, SGK1. *Expected if hypothesis true:* shared causal variants at insulin-pathway/FOXO loci; *expected given current data:* little/no colocalisation except possibly FOXO1 in the cognitive subtype.

4. **Subtype-stratified biomarker study.** In SSRI-responsive agitated/anxious MDD vs anhedonic/anergic MDD, measure CSF/plasma serotonergic markers and peripheral/brain FOXO activity. *Expected if subtype-restricted:* serotonin–FOXO coupling appears only in the SSRI-responsive subtype.

5. **SSRI longitudinal FOXO readout.** Measure FOXO target-gene signatures (Bim, Puma, catalase, SOD) before/after SSRI in responders vs non-responders. *Expected if hypothesis true:* response tracks FOXO target-program suppression.

---

## Curation Leads (require curator verification)

- **Status / node decision:** Do **not** promote an insulin/FOXO pathophysiology node for MDD-at-large. Curate as a **HUMAN_MODEL_MISMATCH** discussion attached to **Monoamine Deficiency**, retaining an **EMERGING, subtype-restricted FOXO1 lead** (cognitive subtype).

- **Candidate evidence references & snippets to verify:**
  - [PMID:42632434](https://pubmed.ncbi.nlm.nih.gov/42632434/) — *"After adjustment, FOXO3 remained unassociated with depressive symptoms (P = 0.232)."* (human negative biomarker)
  - [PMID:41249439](https://pubmed.ncbi.nlm.nih.gov/41249439/) — *"promotes the nuclear translocation of FoxO3a, leading to the transcriptional activation of the pro-apoptotic factor Puma"* (mammalian pro-depressive FOXO3a)
  - [PMID:41622191](https://pubmed.ncbi.nlm.nih.gov/41622191/) — FoxO3a dentate-gyrus overexpression *alleviates* depression (directional conflict)
  - [PMID:36039087](https://pubmed.ncbi.nlm.nih.gov/36039087/) — *"CSS serum could also promote FOXO1 translocation to the cytoplasm through SIRT1 signaling, which triggered FOXO1 protein degradation."* (antidepressant excludes FOXO1)
  - [PMID:35854107](https://pubmed.ncbi.nlm.nih.gov/35854107/) — umbrella review contesting the serotonin-deficiency premise
  - [PMID:36356194](https://pubmed.ncbi.nlm.nih.gov/36356194/) — *"The decreased activity of serotonin ... is characteristic of only a subgroup of depressed subjects"*
  - [PMID:40595333](https://pubmed.ncbi.nlm.nih.gov/40595333/) — MR bidirectional MDD↔T2D (insulin as metabolic comorbidity)

- **Candidate pathophysiology edges (as discussion, not confirmed):** `AKT ⟶ FOXO (nuclear exclusion)` [mammalian, directionally conflicted]; `antidepressant ⟶ FOXO cytoplasmic sequestration` [mammalian]; `MDD ⟷ insulin resistance` [human MR, metabolic arm]. Mark the `serotonin ⟶ FOXO` edge as **unconfirmed in mammals**.

- **Candidate ontology terms:** FOXO1 (HGNC:3819), FOXO3 (HGNC:3821); biological processes — forkhead-box transcription-factor stress response, insulin/IGF-1 receptor signalling (DAF-2 ortholog INSR/IGF1R), intracellular protein localisation (nuclear export); cell types — hippocampal dentate-gyrus granule neuron, astrocyte, microglia.

- **Candidate subtype restriction:** Restrict any serotonin-dependent FOXO claim to a **cognitive / agitated-anxious SSRI-responsive MDD subtype**, reflecting both the FOXO1 interaction-GWAS source (GCST90096932) and the serotonin-subtype commentary.

- **Candidate knowledge_gaps / discussion prompts:** (1) No demonstrated mammalian serotonin→FOXO edge; (2) wrong-FOXO-family-member mismatch (mammal FOXO3a vs human-genetic FOXO1); (3) no human MDD genetic support for INSR/IGF1R/SGK1/AKT1; (4) unresolved pro- vs anti-depressive FOXO directionality; (5) GenCC/ClinGen not yet queried — flag as **unverified** absence pending a dated search.

---

## Provider Artifact Bundle

Under `kb/hypotheses/Major_Depressive_Disorder/serotonin_foxo_stress_transcription_model/openscientist_artifacts/`:

- `data/opentargets_foxo_mdd_associations.csv` — FOXO/insulin gene MDD association & genetic-evidence scores (Open Targets v26.9, 2026-10-09)
- `data/foxo1_mdd_crediblesets.json` — FOXO1 credible-set resolution (rs180828263 → GCST90096932)
- `data/mdd_top_targets_context.csv` — top-30 MDD targets context (DRD2/HTR2A/GRIN2A/GABRA1 …)
- `queries/opentargets_queries.graphql` — exact GraphQL queries used

The bundle is non-empty because computational Open Targets analyses were actually run. No large raw downloads, controlled data, or credentials are bundled; the external Open Targets snapshot is identified by version (v26.9.0) and disease ID (MONDO_0002009). A canonical `MANIFEST.yaml` with checksums and replay verification should be finalised by the curator if not already present. No patient-level or omics dataset was accessed, and none is claimed.

---

## Conclusion

The Serotonin-Restrained FOXO Stress Transcription Model is a mechanistically elegant chain that is **fully supported only in *C. elegans***. In mammals, its downstream AKT→FOXO→stress-program arm is independently and repeatedly supported, including reversal by antidepressants, but its defining serotonin→FOXO edge is untested, its FOXO directionality is conflicted, its human FOXO3 biomarker is negative, and human genetics nominate only a weak, subtype-conditioned FOXO1 signal while giving no support to the insulin-receptor arm. The human insulin–MDD link that does exist is a parallel metabolic comorbidity, and the upstream serotonin-deficiency premise is itself contested. **Recommended disposition: HUMAN_MODEL_MISMATCH discussion attached to Monoamine Deficiency, with a subtype-restricted EMERGING FOXO1 lead — not a promoted primary pathophysiology node.**


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist foxo1 mdd crediblesets](openscientist_artifacts/kb_hypotheses_Major_Depressive_Disorder_serotonin_foxo_stress_transcription_model_openscientist_artifacts_data_foxo1_mdd_crediblesets.json)
- [OpenScientist mdd top targets context](openscientist_artifacts/kb_hypotheses_Major_Depressive_Disorder_serotonin_foxo_stress_transcription_model_openscientist_artifacts_data_mdd_top_targets_context.csv)
- [OpenScientist opentargets foxo mdd associations](openscientist_artifacts/kb_hypotheses_Major_Depressive_Disorder_serotonin_foxo_stress_transcription_model_openscientist_artifacts_data_opentargets_foxo_mdd_associations.csv)
- [OpenScientist opentargets foxo mdd associations](openscientist_artifacts/kb_hypotheses_Major_Depressive_Disorder_serotonin_foxo_stress_transcription_model_openscientist_artifacts_data_opentargets_foxo_mdd_associations.json)
- [OpenScientist search log](openscientist_artifacts/kb_hypotheses_Major_Depressive_Disorder_serotonin_foxo_stress_transcription_model_openscientist_artifacts_logs_search_log.md)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 0 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |

No term could be looked up either way, so nothing here was confirmed or contradicted.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.
