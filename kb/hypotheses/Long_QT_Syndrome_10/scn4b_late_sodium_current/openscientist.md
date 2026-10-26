---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T15:00:03.724679'
end_time: '2026-10-24T15:25:01.380143'
duration_seconds: 1497.66
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Long QT Syndrome 10
  category: Genetic
  hypothesis_group_id: scn4b_late_sodium_current
  hypothesis_label: SCN4B variant raises cardiac late sodium current, as in LQT3
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: scn4b_late_sodium_current\nhypothesis_label:\
    \ SCN4B variant raises cardiac late sodium current, as in LQT3\nstatus: EMERGING\n\
    description: 'The proposed model: the L179F variant in the sodium channel beta-4\
    \ subunit increases the\n  late (persistent) Nav1.5 current, which delays ventricular\
    \ repolarization and prolongs the QT interval\n  in the way SCN5A gain-of-function\
    \ variants do in LQT3. The current change has been shown only in one\n  heterologous-expression\
    \ study, and the variant has been found in one family without significant segregation,\n\
    \  so the gene-disease relationship the model explains is itself disputed. Recorded\
    \ as EMERGING rather\n  than CANONICAL for that reason; the open question is the\
    \ knowledge gap lqt10_scn4b_causality_unestablished.'"
  artifact_dir: kb/hypotheses/Long_QT_Syndrome_10/scn4b_late_sodium_current/openscientist_artifacts
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
citation_count: 8
term_validation:
  total_terms: 4
  verified: 4
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: CL:0002129
    reported_labels:
    - "Candidate ontology terms:** cell type \u2014 ventricular cardiomyocyte"
    ontology_label: regular atrial cardiac myocyte
  needs_review: true
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
- filename: kb_hypotheses_Long_QT_Syndrome_10_scn4b_late_sodium_current_openscientist_artifacts_data_evidence_matrix.csv
  path: openscientist_artifacts/kb_hypotheses_Long_QT_Syndrome_10_scn4b_late_sodium_current_openscientist_artifacts_data_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: kb_hypotheses_Long_QT_Syndrome_10_scn4b_late_sodium_current_openscientist_artifacts_environment.json
  path: openscientist_artifacts/kb_hypotheses_Long_QT_Syndrome_10_scn4b_late_sodium_current_openscientist_artifacts_environment.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist environment
- filename: kb_hypotheses_Long_QT_Syndrome_10_scn4b_late_sodium_current_openscientist_artifacts_logs_gnomad_clinvar_scn4b_L179F.json
  path: openscientist_artifacts/kb_hypotheses_Long_QT_Syndrome_10_scn4b_late_sodium_current_openscientist_artifacts_logs_gnomad_clinvar_scn4b_L179F.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gnomad clinvar scn4b L179F
- filename: kb_hypotheses_Long_QT_Syndrome_10_scn4b_late_sodium_current_openscientist_artifacts_logs_gnomad_constraint_and_gencc.json
  path: openscientist_artifacts/kb_hypotheses_Long_QT_Syndrome_10_scn4b_late_sodium_current_openscientist_artifacts_logs_gnomad_constraint_and_gencc.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gnomad constraint and gencc
- filename: kb_hypotheses_Long_QT_Syndrome_10_scn4b_late_sodium_current_openscientist_artifacts_logs_pubmed_search_log.json
  path: openscientist_artifacts/kb_hypotheses_Long_QT_Syndrome_10_scn4b_late_sodium_current_openscientist_artifacts_logs_pubmed_search_log.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pubmed search log
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Long QT Syndrome 10
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** scn4b_late_sodium_current
- **Hypothesis Label:** SCN4B variant raises cardiac late sodium current, as in LQT3
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: scn4b_late_sodium_current
hypothesis_label: SCN4B variant raises cardiac late sodium current, as in LQT3
status: EMERGING
description: 'The proposed model: the L179F variant in the sodium channel beta-4 subunit increases the
  late (persistent) Nav1.5 current, which delays ventricular repolarization and prolongs the QT interval
  in the way SCN5A gain-of-function variants do in LQT3. The current change has been shown only in one
  heterologous-expression study, and the variant has been found in one family without significant segregation,
  so the gene-disease relationship the model explains is itself disputed. Recorded as EMERGING rather
  than CANONICAL for that reason; the open question is the knowledge gap lqt10_scn4b_causality_unestablished.'
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
result beneath `kb/hypotheses/Long_QT_Syndrome_10/scn4b_late_sodium_current/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.


## Output

# Mechanistic Hypothesis Search — Long QT Syndrome 10

## Hypothesis under evaluation
**ID:** `scn4b_late_sodium_current`
**Label:** SCN4B variant raises cardiac late sodium current, as in LQT3
**KB status:** EMERGING
**Target disease:** Long QT Syndrome 10 (Genetic)
**Search/analysis date:** 2026-10-24

---

## Executive Judgment

**Verdict: Weakly / partially supported. The seed hypothesis should retain EMERGING status, and the knowledge gap `lqt10_scn4b_causality_unestablished` should be retained.**

The proposed model — that the **SCN4B L179F** missense variant in the sodium-channel β4 subunit increases the **late (persistent) Nav1.5 sodium current**, thereby delaying ventricular repolarization and prolonging the QT interval in the same gain-of-function manner as SCN5A variants do in LQT3 — is **biophysically plausible but thinly evidenced and unreplicated**. The entire direct evidentiary basis is a single 2007 report: one three-generation family harboring L179F plus one heterologous-expression experiment in HEK293 cells showing an ~8-fold increase in persistent sodium current ([PMID: 17592081](https://pubmed.ncbi.nlm.nih.gov/17592081/)). No independent family and no human cardiomyocyte or iPSC-derived cardiomyocyte (iPSC-CM) replication of the late-current phenotype were found in the literature search.

Three independent lines of evidence weaken the causal attribution. First, an international ClinGen-framework reappraisal placed SCN4B among the LQTS genes with **limited or disputed** gene–disease validity and explicitly advised against using variants in such genes for clinical decision-making without new genetic evidence ([PMID: 31983240](https://pubmed.ncbi.nlm.nih.gov/31983240/)). Second, the variant itself (rs121434386, p.Leu179Phe) is a current **ClinVar Variant of Uncertain Significance** and exists in gnomAD v4.1 as a **single ultra-rare allele** (AC=1, AF≈6.6×10⁻⁶) confined to the Admixed American population. Third, **SCN4B shows no loss-of-function constraint** (pLI≈0, LOEUF≈1.48), consistent with an auxiliary/modifier role rather than a dosage-critical Mendelian LQTS gene — which means the hypothesis must stand entirely on a specific gain-of-function mechanism, not on haploinsufficiency or dosage.

A competing and arguably more parsimonious explanation for weak-monogenic and genotype-negative LQTS exists: **polygenic QT risk**. Large population and carrier studies show QTc is shaped by both rare repolarization-gene variants and a sizeable polygenic contribution, and that a QTc polygenic score modulates penetrance even within carriers of established monogenic variants ([PMID: 35389749](https://pubmed.ncbi.nlm.nih.gov/35389749/); [PMID: 39209900](https://pubmed.ncbi.nlm.nih.gov/39209900/)). This provides a plausible confound for the single-family segregation that underpins the SCN4B claim. The most important caveat is that absence of replication is not refutation — the mechanism class (β-subunit variants raising late Iₙₐ) is demonstrated elsewhere — but as of the current literature the LQT10-specific causal claim remains unestablished.

---

## Key Findings

### F001 — Direct evidence rests on a single family plus one heterologous-expression study

The foundational and still essentially sole source of direct support for the hypothesis is **Medeiros-Domingo et al. 2007** ([PMID: 17592081](https://pubmed.ncbi.nlm.nih.gov/17592081/)). In that study an L179F (c.C535T) missense variant in SCN4B was identified in a single proband — a 21-month-old child with a markedly prolonged QTc of 712 ms — and the variant *"cosegregated properly throughout a 3-generation pedigree and was absent in 800 reference alleles."* Functionally, in HEK293 cells stably expressing human Nav1.5 (SCN5A), the L179F-β4 construct increased persistent/late sodium current approximately **8-fold** relative to SCN5A alone (and ~3-fold relative to wild-type β4). This is the LQT3-like gain-of-function signature the seed hypothesis invokes.

Crucially, the same study found **no replication** of SCN4B as a recurrent cause: screening of *"262 genotype-negative LQTS patients (96% white)"* yielded *"no further mutations."* Thus from its inception the gene–disease relationship rested on n=1 family and a single in-vitro assay, with no second index case in a sizeable genotype-negative cohort. This is the central structural weakness of the hypothesis: the mechanism was demonstrated once, in one expression system, for one variant, in one family.

### F002 — SCN4B–LQTS gene–disease validity was downgraded to limited/disputed

**Adler et al. 2020** ([PMID: 31983240](https://pubmed.ncbi.nlm.nih.gov/31983240/)) applied the ClinGen clinical-validity framework to 17 genes reported to cause LQTS, using three blinded curation teams. The reappraisal concluded that *"more than half of the genes reported as causing LQTS have limited or disputed evidence to support their disease causation,"* a tier that includes the atypical/auxiliary genes such as SCN4B. The authors were explicit about the clinical consequence: *"Genetic variants in these genes should not be used for clinical decision-making, unless accompanied by new and sufficient genetic evidence."* This is an evidence-based, framework-driven downgrade that directly bears on the LQT10/SCN4B gene-disease edge and is the primary reason the seed hypothesis cannot be elevated beyond EMERGING.

### F003 — Nav β-subunit variants can raise late Iₙₐ in other phenotypes (class plausibility, not LQT10-specific support)

The *mechanistic class* — a non-pore-forming β-subunit variant increasing persistent/late sodium current — is independently demonstrated, lending the hypothesis biophysical plausibility even though these studies are not LQT10. Riuró et al. 2014 ([PMID: 24662403](https://pubmed.ncbi.nlm.nih.gov/24662403/)) showed that the SCN1B β1b-P213T variant *"increases late sodium current"* and prolonged action potential duration in HL-1 cells, establishing SCN1B as an LQTS-susceptibility gene. Tan et al. 2010 ([PMID: 20226894](https://pubmed.ncbi.nlm.nih.gov/20226894/)) showed that another SCN4B/β4 variant, β4-S206L, *"accentuated late I(Na) and positively shifted the midpoint of inactivation compared with SCN5A+beta4-WT"* — but in a **sudden infant death syndrome (SIDS)** context, not LQT10. These results confirm that β-subunits can modulate late Iₙₐ, but they qualify rather than confirm the LQT10 claim: the mechanism is real as a class, yet the specific L179F→LQT10 causal chain remains supported by a single source.

### F004 — L179F is an ultra-rare gnomAD allele and a ClinVar VUS

A direct gnomAD v4.1 query (GraphQL API, retrieved 2026-10-24) resolved the variant **11-118141265-G-A (GRCh38)**, p.Leu179Phe, rs121434386: genome **AC=1, AN=152,122, AF=6.57×10⁻⁶**, absent from the exome dataset, with the single observed allele in the Admixed American (amr) population. ClinVar (as surfaced through gnomAD) classifies it **"Uncertain significance"**, 1 gold star, criteria provided by a single submitter, last evaluated 2023-09-01. An allele count of one across >150,000 genomes is consistent with an ultra-rare variant but provides no population-genetic leverage to confirm or exclude pathogenicity, and the standing VUS classification reflects precisely the unresolved causality the seed hypothesis flags.

### F005 — Polygenic QT risk is a competing / parallel explanation

**Nauffal et al. 2022** ([PMID: 35389749](https://pubmed.ncbi.nlm.nih.gov/35389749/)), using TOPMed and UK Biobank, found that *"QTc duration in the population is influenced by both rare variants in genes underlying cardiac repolarization and polygenic risk, with a sizeable contribution from polygenic risk."* The polygenic contribution also operates *within* monogenic carriers: in LQT5, *"among carriers, the QTc polygenic score is independently associated with QTc prolongation"* ([PMID: 39209900](https://pubmed.ncbi.nlm.nih.gov/39209900/)); similar PRS modulation is reported in LQT1 ([PMID: 42111135](https://pubmed.ncbi.nlm.nih.gov/42111135/)). A review-level synthesis notes that missing heritability and incomplete penetrance in inherited arrhythmia syndromes are increasingly attributed to common-variant/polygenic effects ([PMID: 36167638](https://pubmed.ncbi.nlm.nih.gov/36167638/), review-level orientation). For a single small pedigree, polygenic background is a credible confounder of apparent co-segregation and offers a more parsimonious account of borderline/variable QT prolongation than a novel monogenic mechanism.

### F006 — SCN4B is highly loss-of-function tolerant (modifier-like)

gnomAD v4.1 constraint metrics for **SCN4B (ENSG00000177098**, retrieved 2026-10-24): **pLI = 1.1×10⁻⁷ (≈0)**, observed/expected LoF = 1.02 (90% CI 0.72–1.48; **LOEUF ≈ 1.48**), obs_lof=20 vs exp_lof=19.6, lof_z = −0.07. There is **no depletion of predicted loss-of-function variants**, indicating the gene tolerates haploinsufficiency. This is consistent with an auxiliary/modifier role rather than a dosage-critical Mendelian gene, and it has a sharp logical consequence for the hypothesis: the model cannot lean on dosage/LoF effects and must rest entirely on a **specific gain-of-function** (increased late Iₙₐ) mechanism — which to date has been shown only once.

### F007 — Overall verdict: weakly/partially supported; retain EMERGING and the causality gap

Synthesizing the six findings: direct support is one three-generation family plus one HEK293 experiment (~8-fold late-Iₙₐ increase, [PMID: 17592081](https://pubmed.ncbi.nlm.nih.gov/17592081/)); no second family and no cardiomyocyte/iPSC-CM replication were found across 8 PubMed queries (2026-10-24). Counter/limiting evidence: the ClinGen-framework reappraisal places SCN4B in the limited/disputed tier ([PMID: 31983240](https://pubmed.ncbi.nlm.nih.gov/31983240/)); the variant is a ClinVar VUS present as a single ultra-rare AMR allele in gnomAD v4.1; and SCN4B shows no LoF constraint. The leading competing model is polygenic QT burden ([PMID: 35389749](https://pubmed.ncbi.nlm.nih.gov/35389749/); [PMID: 39209900](https://pubmed.ncbi.nlm.nih.gov/39209900/)). The verdict is therefore **weakly/partially supported**, and both the EMERGING status and the knowledge gap are appropriate to retain.

---

## Mechanistic Model / Interpretation

The hypothesis posits a linear LQT3-like causal chain. The diagram and table below annotate the strength of each link as established by the current search.

```
 UPSTREAM TRIGGER                     MOLECULAR EFFECT                 CELLULAR EFFECT              CLINICAL MANIFESTATION
 ┌────────────────────┐   [DISPUTED] ┌───────────────────────┐ [1 study]┌──────────────────┐ [INFER]┌────────────────────┐
 │ SCN4B L179F variant │ ───────────▶│ β4 subunit alters      │ ───────▶ │ Delayed ventric.  │ ──────▶│ QT prolongation,    │
 │ (β4 aux. subunit)   │             │ Nav1.5 gating →        │          │ repolarization /  │        │ ↑ torsades risk,    │
 │                     │             │ ~8× persistent/late    │          │ prolonged APD     │        │ LQT10 phenotype     │
 │                     │             │ Iₙₐ (HEK293, 1 study)  │          │ (NOT shown in CM) │        │ (1 family, QTc 712) │
 └────────────────────┘             └───────────────────────┘          └──────────────────┘        └────────────────────┘
        │                                      │                                │                              │
   single ultra-rare                   single heterologous               NOT demonstrated in            single 3-generation
   VUS allele; gene                     expression study; no             native/iPSC-CM;                pedigree; no 2nd family;
   disputed (ClinGen)                   CM/iPSC replication              inferred from LQT3 analogy      polygenic confound
```

| Causal link | Evidence status | Basis |
|---|---|---|
| L179F → altered Nav1.5 gating / ↑ late Iₙₐ | **Demonstrated once** (in vitro) | HEK293, ~8-fold increase, [PMID: 17592081](https://pubmed.ncbi.nlm.nih.gov/17592081/) |
| ↑ late Iₙₐ → prolonged APD / delayed repolarization | **Inferred** from LQT3 physiology; class-plausible | β-subunit→late Iₙₐ shown for SCN1B ([PMID: 24662403](https://pubmed.ncbi.nlm.nih.gov/24662403/)) and β4-S206L ([PMID: 20226894](https://pubmed.ncbi.nlm.nih.gov/20226894/)), not L179F in CM |
| Prolonged APD → QT prolongation/arrhythmia | **Inferred**; standard LQTS physiology | General LQTS mechanism (reviews) |
| Variant → clinical LQT10 (gene–disease) | **Disputed / limited** | ClinGen reappraisal ([PMID: 31983240](https://pubmed.ncbi.nlm.nih.gov/31983240/)); VUS; single family |

The literature is **strong only at the first molecular node** (and even there, from a single study/system). Every downstream link in the native-tissue chain is **inferred by analogy to LQT3** rather than directly observed for L179F. The gene–disease edge itself is actively disputed. The hypothesis is best understood as a *mechanistically plausible but empirically under-determined* model whose plausibility derives from the broader β-subunit→late-Iₙₐ class rather than from LQT10-specific data.

### Where the hypothesis best fits
The model, if true, would best explain a **rare, early-onset, strongly QT-prolonged monogenic subtype** (the index proband presented at 21 months with QTc 712 ms) acting in **ventricular cardiomyocytes** via the **Nav1.5 late-sodium-current pathway** — i.e., mechanistically indistinguishable from LQT3, with β4 acting as an auxiliary modifier of the SCN5A α-subunit. It does *not* explain the common, genotype-negative, mildly-prolonged QT population, for which polygenic risk is the better-supported account.

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Role | Mechanistic claim tested | Key finding | Subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [17592081](https://pubmed.ncbi.nlm.nih.gov/17592081/) | Human clinical + in vitro | **Supports** | L179F raises Nav1.5 late Iₙₐ → LQT | ~8× persistent Iₙₐ in HEK293; cosegregates in 3-gen pedigree; absent in 800 alleles; 0/262 genotype-neg had SCN4B mutation | LQT10, 1 family | Foundational but single family + single expression system; no CM replication |
| [31983240](https://pubmed.ncbi.nlm.nih.gov/31983240/) | Review / evidence-based curation | **Refutes / limits** | SCN4B causes LQTS | >½ reported LQTS genes limited/disputed; advise against clinical use | All LQTS genes incl. SCN4B | High-confidence framework appraisal; gene-level, not variant-specific |
| [20226894](https://pubmed.ncbi.nlm.nih.gov/20226894/) | In vitro | **Qualifies** | β4 variant raises late Iₙₐ | β4-S206L accentuated late Iₙₐ, +shift inactivation | SIDS (not LQT10) | Supports class mechanism; wrong phenotype |
| [24662403](https://pubmed.ncbi.nlm.nih.gov/24662403/) | In vitro | **Qualifies** | Nav β-subunit variant raises late Iₙₐ | β1b-P213T ↑ late Iₙₐ, ↑ APD in HL-1 | SCN1B/LQTS susceptibility | Supports class mechanism; different gene |
| gnomAD v4.1 (rs121434386) | Computational / population | **Qualifies / limits** | Variant rarity & classification | AC=1, AF 6.6×10⁻⁶, single AMR allele; ClinVar VUS | LQT10 variant | Ultra-rare, no population leverage; standing VUS |
| gnomAD v4.1 constraint (SCN4B) | Computational / population | **Qualifies / limits** | SCN4B dosage sensitivity | pLI≈0, LOEUF≈1.48; no LoF depletion | Gene-level | LoF-tolerant → hypothesis needs GoF, not dosage |
| [35389749](https://pubmed.ncbi.nlm.nih.gov/35389749/) | Human clinical / population | **Competing** | Polygenic risk drives QTc | Sizeable polygenic contribution to QTc alongside rare variants | Population QT | Strong population evidence; competing explanation |
| [39209900](https://pubmed.ncbi.nlm.nih.gov/39209900/) | Human clinical | **Competing** | PRS modulates penetrance in carriers | QTc PRS independently associated with QTc among carriers | LQT5 carriers | Shows polygenic confound of segregation |
| [42111135](https://pubmed.ncbi.nlm.nih.gov/42111135/) | Human clinical | **Competing** | PRS modulates repolarization | PRS modestly ↑ QTc and T-wave params | LQT1 carriers | Reinforces polygenic modulation |
| [36167638](https://pubmed.ncbi.nlm.nih.gov/36167638/) | Review | Orientation | Polygenic & curation framework | Missing heritability increasingly polygenic; curated panels | Inherited arrhythmias | Review-level; context only |

---

## Data and Tool Use

| Source / dataset | Accession / URI | Access status | Query / filters | Resolved & relevant? |
|---|---|---|---|---|
| gnomAD v4.1 (variant) | 11-118141265-G-A (GRCh38), rs121434386, GraphQL API | **Accessed** (2026-10-24) | p.Leu179Phe allele frequency, population breakdown, ClinVar annotation | Yes — resolved; directly relevant (the seed variant) |
| gnomAD v4.1 (gene constraint) | ENSG00000177098 (SCN4B), GraphQL API | **Accessed** (2026-10-24) | pLI, LOEUF, obs/exp LoF | Yes — resolved; directly relevant (dosage sensitivity) |
| ClinVar (via gnomAD) | rs121434386 | **Accessed** (2026-10-24) | Classification, review status, last eval date | Yes — VUS, 1 star, 2023-09-01 |
| PubMed | — | **Searched** (2026-10-24) | 8 queries on SCN4B/LQT10/β4/late-Iₙₐ/iPSC-CM | Yes — 24 papers reviewed; no CM replication or 2nd family found |
| ClinGen LQTS curation | via [PMID: 31983240](https://pubmed.ncbi.nlm.nih.gov/31983240/) | **Accessed via literature** | SCN4B gene-disease validity tier | Yes — limited/disputed |

**Analysis inventory.** (1) *gnomAD variant/constraint retrieval* — input: rs121434386 / ENSG00000177098; method: gnomAD v4.1 GraphQL API query; output: allele counts, AF, pLI/LOEUF; outcome: **succeeded**; limitation: single-allele variant provides no statistical leverage on pathogenicity. (2) *PubMed replication search* — input: 8 search strings; method: search_pubmed; output: negative for second family / iPSC-CM late-Iₙₐ replication; outcome: **succeeded (negative result)**; limitation: absence of indexed replication is not proof of non-existence. No controlled/patient-level datasets, omics cohorts, or trial datasets specific to SCN4B-L179F LQT10 were located; **no GenCC/ClinGen positive validation beyond the disputed-tier curation was found.** No structural-biology (Phenix) analysis was applicable or performed. No silent fallback occurred: computational checks (gnomAD) were performed where testable; literature synthesis is labeled as such throughout.

---

## Mechanistic Causal Chain

- **Upstream trigger (DISPUTED edge):** SCN4B L179F, an ultra-rare VUS in an LoF-tolerant auxiliary subunit, within a disputed gene–disease relationship.
- **Molecular effect (STRONG only in 1 system):** L179F-β4 co-assembles with Nav1.5 and increases persistent/late sodium current ~8-fold in HEK293 ([PMID: 17592081](https://pubmed.ncbi.nlm.nih.gov/17592081/)). The β-subunit→late-Iₙₐ mechanism is corroborated as a *class* by SCN1B-β1b-P213T and SCN4B-β4-S206L in other phenotypes.
- **Cellular effect (INFERRED):** increased late Iₙₐ prolongs action-potential duration and favors early afterdepolarizations — standard LQT3 physiology, but **never shown for L179F in cardiomyocytes/iPSC-CM**.
- **Clinical manifestation (INFERRED, single family):** prolonged QT, torsades risk, LQT10 (index QTc 712 ms).

The literature is strong at the molecular node (single system) and weak/inferred at every native-tissue and clinical link; the gene–disease edge is a known missing/disputed step.

---

## Limitations and Knowledge Gaps

**Gap 1 — Unreplicated functional phenotype in native tissue.** *Scope:* the ↑late-Iₙₐ effect of L179F has been shown only in HEK293 heterologous expression ([PMID: 17592081](https://pubmed.ncbi.nlm.nih.gov/17592081/)). *Why it matters:* heterologous systems can over- or under-state β-subunit effects; the cellular→clinical links are inferred. *What was checked:* PubMed (2026-10-24, 8 queries) found no iPSC-CM or native-cardiomyocyte replication. *Resolution:* patient/isogenic iPSC-CM electrophysiology.

**Gap 2 — No second family / segregation power.** *Scope:* a single 3-generation pedigree; 0/262 genotype-negative patients carried SCN4B mutations. *Why it matters:* single-family segregation is statistically weak and confoundable by polygenic background. *What was checked:* literature and the original cohort. *Resolution:* additional unrelated families, biobank IBD-haplotype approaches analogous to LQT5 ([PMID: 39209900](https://pubmed.ncbi.nlm.nih.gov/39209900/)).

**Gap 3 — Disputed gene–disease edge.** *Scope:* ClinGen places SCN4B–LQTS in the limited/disputed tier ([PMID: 31983240](https://pubmed.ncbi.nlm.nih.gov/31983240/)). *Why it matters:* undermines clinical actionability of any L179F-based model. *Resolution:* new sufficient genetic evidence per ClinGen criteria.

**Gap 4 — Variant-level uncertainty.** *Scope:* ClinVar VUS, single ultra-rare gnomAD allele. *Why it matters:* pathogenicity unestablished at the variant level. *Resolution:* additional carriers with deep phenotyping; functional ACMG evidence (PS3) from independent assays.

**Gap 5 — Polygenic confounding not excluded.** *Scope:* polygenic QT burden is a competing determinant ([PMID: 35389749](https://pubmed.ncbi.nlm.nih.gov/35389749/)). *Why it matters:* apparent monogenic co-segregation may reflect shared polygenic background. *Resolution:* QTc PRS computation in any SCN4B pedigree.

**Gap 6 — Dosage vs. gain-of-function.** *Scope:* SCN4B is LoF-tolerant (pLI≈0). *Why it matters:* constrains the admissible mechanism to strict gain-of-function and raises the evidentiary bar. *Resolution:* side-by-side GoF assays across systems.

**Source/data absences (verified as of 2026-10-24):** No positive GenCC/ClinGen validation beyond the disputed tier; no SCN4B-L179F-specific omics, trial, or cohort dataset located in PubMed searches; no iPSC-CM dataset found. These are reported as negative search outcomes with the queries and date above, not as proven global absence.

---

## Alternative / Competing Models

| Model | Relationship to seed | Summary |
|---|---|---|
| **Polygenic QT burden** | **Alternative / parallel** | Common-variant PRS drives QTc at population level and modulates penetrance within carriers; more parsimonious for borderline/variable QT ([PMID: 35389749](https://pubmed.ncbi.nlm.nih.gov/35389749/), [39209900](https://pubmed.ncbi.nlm.nih.gov/39209900/), [42111135](https://pubmed.ncbi.nlm.nih.gov/42111135/)). |
| **Primary SCN5A / other-gene variant with SCN4B as modifier** | **Upstream cause (β4 modifier)** | β4 is auxiliary to Nav1.5; L179F may modify an α-subunit defect rather than be independently causal. Consistent with LoF tolerance and modifier role. |
| **β-subunit→late-Iₙₐ as a trans-phenotype class** | **Parallel mechanism** | Same biophysical lever produces different phenotypes (AF, SIDS, VT) depending on context ([PMID: 20226894](https://pubmed.ncbi.nlm.nih.gov/20226894/), [24662403](https://pubmed.ncbi.nlm.nih.gov/24662403/)); questions LQT10 specificity. |
| **Benign/incidental variant** | **Null alternative** | L179F could be a rare non-causal VUS; phenotype arising from undetected variants or polygenic load. Supported by VUS status and disputed gene validity. |

---

## Discriminating Tests

1. **Patient-specific & isogenic iPSC-CM electrophysiology.** Derive iPSC-CMs from an L179F carrier and an isogenic CRISPR-corrected control; measure late Iₙₐ, APD, and early afterdepolarizations. *Expected if hypothesis true:* corrected line normalizes late Iₙₐ and APD. This directly tests the native-tissue link currently only inferred.

2. **Independent heterologous replication across systems.** Re-express L179F-β4 + Nav1.5 in ≥2 systems (e.g., CHO and iPSC-CM) by independent labs to satisfy ACMG PS3; compare to WT-β4 and to β4-S206L as a positive class control.

3. **Biobank IBD-haplotype carrier ascertainment + PRS.** Apply the DRIVE-style approach used for LQT5 ([PMID: 39209900](https://pubmed.ncbi.nlm.nih.gov/39209900/)) to find additional L179F carriers; compute QTc PRS to separate monogenic from polygenic contribution. *Expected if hypothesis true:* carriers show QTc prolongation beyond their PRS-predicted value.

4. **Additional-family segregation with quantitative penetrance.** Seek unrelated L179F families; formal LOD/segregation with PRS covariate adjustment.

5. **Late-Iₙₐ-blocker (mexiletine) response (mechanistic pharmacology).** If a carrier's QT shortens with a selective late-Iₙₐ blocker (as in LQT3), this functionally corroborates a late-Iₙₐ mechanism in vivo.

---

## Curation Leads (require curator verification)

- **Status:** Retain **EMERGING**; do **not** elevate to CANONICAL. Retain knowledge gap `lqt10_scn4b_causality_unestablished`.
- **Candidate evidence references & snippets to verify:**
  - [PMID: 17592081](https://pubmed.ncbi.nlm.nih.gov/17592081/) — *"revealed a L179F (C535T) missense mutation in SCN4B that cosegregated properly throughout a 3-generation pedigree and was absent in 800 reference alleles"* and *"SCN4B was analyzed in 262 genotype-negative LQTS patients (96% white), but no further mutations were found."*
  - [PMID: 31983240](https://pubmed.ncbi.nlm.nih.gov/31983240/) — *"More than half of the genes reported as causing LQTS have limited or disputed evidence to support their disease causation"*; *"Genetic variants in these genes should not be used for clinical decision-making, unless accompanied by new and sufficient genetic evidence."*
  - [PMID: 20226894](https://pubmed.ncbi.nlm.nih.gov/20226894/) — *"beta4-S206L accentuated late I(Na) and positively shifted the midpoint of inactivation compared with SCN5A+beta4-WT."*
  - [PMID: 24662403](https://pubmed.ncbi.nlm.nih.gov/24662403/) — *"Our electrophysiological analysis revealed that β1bP213T increases late sodium current."*
  - [PMID: 35389749](https://pubmed.ncbi.nlm.nih.gov/35389749/) — *"QTc duration in the population is influenced by both rare variants in genes underlying cardiac repolarization and polygenic risk, with a sizeable contribution from polygenic risk."*
  - [PMID: 39209900](https://pubmed.ncbi.nlm.nih.gov/39209900/) — *"among carriers, the QTc polygenic score is independently associated with QTc prolongation."*
- **Candidate pathophysiology nodes/edges:** node *SCN4B-L179F (β4 subunit)*; edge *β4-L179F → ↑Nav1.5 late/persistent Iₙₐ* (label: in-vitro only, 1 study); edge *↑late Iₙₐ → delayed ventricular repolarization → QT prolongation* (label: inferred by LQT3 analogy); disputed edge *SCN4B → LQTS* (label: ClinGen limited/disputed).
- **Candidate ontology terms:** cell type — ventricular cardiomyocyte (CL:0002129); processes — membrane repolarization during cardiac action potential (GO:0098915), regulation of sodium ion transmembrane transport (GO:1902305); phenotype — prolonged QT interval (HP:0001657).
- **Candidate subtype restriction:** restrict the model to a rare, early-onset, severely QT-prolonged monogenic subtype; explicitly exclude the common genotype-negative/mild-QT population (better explained by polygenic risk).
- **Candidate knowledge_gaps / discussion prompts:** (a) no iPSC-CM/native-tissue replication of L179F late Iₙₐ; (b) no second unrelated family; (c) polygenic confounding of single-pedigree segregation not excluded; (d) variant remains ClinVar VUS / ultra-rare gnomAD allele; (e) SCN4B LoF-tolerant → hypothesis constrained to strict gain-of-function.

**Artifact note:** gnomAD v4.1 query parameters and results (variant 11-118141265-G-A; gene ENSG00000177098; retrieved 2026-10-24) and the 8-query PubMed negative-replication log should be deposited under `kb/hypotheses/Long_QT_Syndrome_10/scn4b_late_sodium_current/openscientist_artifacts` with a `MANIFEST.yaml` recording status/fallback flags and checksums. No controlled/patient-level data or large raw downloads should be bundled; external accessions (rs121434386, ENSG00000177098) are recorded instead.

---

## Evidence Base (summary of key literature)

- **[PMID: 17592081](https://pubmed.ncbi.nlm.nih.gov/17592081/)** — *SCN4B-encoded sodium channel beta4 subunit in congenital long-QT syndrome.* The sole direct source: 1 family, ~8× late Iₙₐ in HEK293. **Supports.**
- **[PMID: 31983240](https://pubmed.ncbi.nlm.nih.gov/31983240/)** — *An International, Multicentered, Evidence-Based Reappraisal of Genes Reported to Cause Congenital Long QT Syndrome.* Places SCN4B in limited/disputed tier. **Refutes/limits.**
- **[PMID: 20226894](https://pubmed.ncbi.nlm.nih.gov/20226894/)** — *SIDS-associated mutations in sodium channel beta subunits.* β4-S206L raises late Iₙₐ (SIDS). **Qualifies (class plausibility).**
- **[PMID: 24662403](https://pubmed.ncbi.nlm.nih.gov/24662403/)** — *A missense mutation in SCN1B β1b reveals SCN1B as an LQTS susceptibility gene.* β1b-P213T raises late Iₙₐ. **Qualifies (class plausibility).**
- **[PMID: 35389749](https://pubmed.ncbi.nlm.nih.gov/35389749/)** — *Monogenic and Polygenic Contributions to QTc Prolongation.* Sizeable polygenic contribution. **Competing.**
- **[PMID: 39209900](https://pubmed.ncbi.nlm.nih.gov/39209900/)** — *Detection of distant relatedness in biobanks (LQT5).* QTc PRS modulates penetrance within carriers. **Competing.**
- **[PMID: 42111135](https://pubmed.ncbi.nlm.nih.gov/42111135/)** — *Polygenic risk modulates repolarization in LQT1.* **Competing.**
- **[PMID: 36167638](https://pubmed.ncbi.nlm.nih.gov/36167638/)** — *Cardiogenetics review.* Curated panels; polygenic context. **Review-level orientation.**

---

## Proposed Follow-up Experiments / Actions

1. Commission/seek **isogenic iPSC-CM** functional data for L179F (highest-value discriminating test).
2. Launch **biobank IBD-haplotype ascertainment** of additional carriers with QTc PRS adjustment.
3. Track **ClinVar reclassification** of rs121434386 and any new ClinGen SCN4B recuration.
4. Keep the **EMERGING** status and `lqt10_scn4b_causality_unestablished` gap open until (a) ≥1 independent family and (b) ≥1 native-tissue functional replication exist.
5. Deposit the gnomAD query artifacts and PubMed negative-search log in the artifact bundle with a checksummed `MANIFEST.yaml`.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist evidence matrix](openscientist_artifacts/kb_hypotheses_Long_QT_Syndrome_10_scn4b_late_sodium_current_openscientist_artifacts_data_evidence_matrix.csv)
- [OpenScientist environment](openscientist_artifacts/kb_hypotheses_Long_QT_Syndrome_10_scn4b_late_sodium_current_openscientist_artifacts_environment.json)
- [OpenScientist gnomad clinvar scn4b L179F](openscientist_artifacts/kb_hypotheses_Long_QT_Syndrome_10_scn4b_late_sodium_current_openscientist_artifacts_logs_gnomad_clinvar_scn4b_L179F.json)
- [OpenScientist gnomad constraint and gencc](openscientist_artifacts/kb_hypotheses_Long_QT_Syndrome_10_scn4b_late_sodium_current_openscientist_artifacts_logs_gnomad_constraint_and_gencc.json)
- [OpenScientist pubmed search log](openscientist_artifacts/kb_hypotheses_Long_QT_Syndrome_10_scn4b_late_sodium_current_openscientist_artifacts_logs_pubmed_search_log.json)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0002129` (1 mention) - the report calls it "Candidate ontology terms:** cell type — ventricular cardiomyocyte"; CL calls it **regular atrial cardiac myocyte**