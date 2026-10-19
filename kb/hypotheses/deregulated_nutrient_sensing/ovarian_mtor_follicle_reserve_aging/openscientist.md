---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-18T04:36:43.031476'
end_time: '2026-10-18T04:52:03.648498'
duration_seconds: 920.62
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Deregulated Nutrient Sensing Module
  category: Module
  hypothesis_group_id: ovarian_mtor_follicle_reserve_aging
  hypothesis_label: mTOR Signaling Drives Human Ovarian Aging Through Follicle Reserve
    Depletion
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: ovarian_mtor_follicle_reserve_aging\nhypothesis_label:\
    \ mTOR Signaling Drives Human Ovarian Aging Through Follicle Reserve Depletion\n\
    status: EMERGING\ndescription: The ovary ages earlier than any other organ, and\
    \ mTOR signaling is the pathway the human\n  ovarian aging atlas singles out as\
    \ ovary-specific. This hypothesis holds that rising mTOR signaling\n  in the aging\
    \ ovary accelerates activation of dormant primordial follicles and so depletes\
    \ the follicle\n  reserve, which sets the timing of reproductive aging and menopause.\
    \ It predicts that transient mTOR\n  inhibition preserves the reserve and extends\
    \ ovarian lifespan. Two points are open. The human evidence\n  is transcript abundance\
    \ of mTOR-pathway genes in eight ovaries, not measured kinase activity, and the\n\
    \  one validated gene (RICTOR) belongs to mTORC2, so it is unsettled whether mTORC1,\
    \ mTORC2 or both are\n  involved and in which cell types. And the inhibition evidence\
    \ is from mice, where long-term rapamycin\n  also impairs follicle development\
    \ and ovulation, so benefit depends on dosing schedule.\nevidence:\n- reference:\
    \ PMID:39578560\n  reference_title: Molecular and genetic insights into human\
    \ ovarian aging from single-nuclei multi-omics\n    analyses.\n  supports: SUPPORT\n\
    \  directness: INDIRECT\n  evidence_source: HUMAN_CLINICAL\n  snippet: Our analyses\
    \ reveal coordinated changes in transcriptomes and chromatin accessibilities across\n\
    \    cell types in the ovary during aging, notably mTOR signaling being a prominent\
    \ ovary-specific aging\n    pathway.\n  explanation: Human single-nucleus data\
    \ from four young and four reproductively aged ovaries name mTOR\n    signaling\
    \ as the ovary-specific aging pathway. INDIRECT because it reports pathway gene\
    \ expression,\n    not that mTOR activity causes reserve loss.\n- reference: PMID:28544226\n\
    \  reference_title: Short-term rapamycin treatment increases ovarian lifespan\
    \ in young and middle-aged\n    female mice.\n  supports: SUPPORT\n  evidence_source:\
    \ MODEL_ORGANISM\n  snippet: The effects of transient rapamycin treatment on ovarian\
    \ lifespan were reflected in the preservation\n    of primordial follicles, increases\
    \ in oocyte quality, and improvement in the ovarian microenvironment.\n  explanation:\
    \ Two weeks of rapamycin in young or middle-aged mice prolongs ovarian lifespan\
    \ with preserved\n    primordial follicles, the prediction this hypothesis makes.\n\
    - reference: PMID:31887337\n  reference_title: Rapamycin treatment maintains developmental\
    \ potential of oocytes in mice and follicle\n    reserve in human cortical fragments\
    \ grafted into immune-deficient mice.\n  supports: SUPPORT\n  evidence_source:\
    \ MODEL_ORGANISM\n  snippet: Using human ovarian cortical fragments grafted into\
    \ immune-deficient mice, we demonstrated\n    the ability of rapamycin to suppress\
    \ follicle growth from the primordial stage.\n  explanation: Extends the follicle-activation\
    \ effect of mTOR inhibition to human ovarian tissue, though\n    in xenografts\
    \ rather than in women.\n- reference: PMID:28544226\n  reference_title: Short-term\
    \ rapamycin treatment increases ovarian lifespan in young and middle-aged\n  \
    \  female mice.\n  supports: REFUTE\n  evidence_source: MODEL_ORGANISM\n  snippet:\
    \ However, the application is limited because of its detrimental effects on follicular\
    \ development\n    and ovulation during long-term treatment.\n  explanation: 'Against\
    \ a simple reading that less mTOR is better for the ovary: sustained inhibition\n\
    \    harms follicle development, so the benefit is schedule-dependent.'\n- reference:\
    \ clinicaltrials:NCT05836025\n  reference_title: Effect of Rapamycin in Ovarian\
    \ Aging\n  supports: SUPPORT\n  directness: INDIRECT\n  evidence_source: OTHER\n\
    \  snippet: The investigators are proposing a prospective, randomized, double-blind,\
    \ placebo-controlled\n    pilot study assessing the ability of low-dose rapamycin\
    \ to delay ovarian aging in women.\n  explanation: A registered human trial (VIBRANT)\
    \ testing the hypothesis's prediction in women. It is\n    a registration, not\
    \ a result, so it records that the test is under way rather than supporting the\n\
    \    mechanism.\nnotes: Scoped to the ovary. It is separate from sex_dimorphic_geroprotector_exposure,\
    \ which concerns whole-animal\n  lifespan in both sexes and cannot be tested with\
    \ female-only ovarian data."
  artifact_dir: kb/hypotheses/deregulated_nutrient_sensing/ovarian_mtor_follicle_reserve_aging/openscientist_artifacts
  dataset_inputs: geo:GSE202601
  target_variables: mTORC1-specific (RPTOR, MLST8, RPS6KB1, EIF4EBP1) vs mTORC2-specific
    (RICTOR, MAPKAP1, SGK1) and upstream/downstream mTOR pathway gene expression and
    chromatin accessibility, by ovarian cell type (oocyte, granulosa, theca, stromal,
    immune, endothelial) and age group (young 23-29 vs aged 49-54)
  analysis_objective: Using the GSE202601 single-nucleus multiome data, test whether
    age-associated mTOR pathway up-regulation in the human ovary is mTORC1- or mTORC2-biased
    and which cell types carry it, with granulosa cells as the follicle-activation-relevant
    compartment; report effect sizes with donor-level (n=4 vs 4) pseudobulk statistics
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
  verified: 2
  not_found: 0
  obsolete: 0
  unverifiable: 0
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
- filename: kb_hypotheses_deregulated_nutrient_sensing_ovarian_mtor_follicle_reserve_aging_openscientist_artifacts_README.md
  path: openscientist_artifacts/kb_hypotheses_deregulated_nutrient_sensing_ovarian_mtor_follicle_reserve_aging_openscientist_artifacts_README.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist README
- filename: kb_hypotheses_deregulated_nutrient_sensing_ovarian_mtor_follicle_reserve_aging_openscientist_artifacts_env_environment.md
  path: openscientist_artifacts/kb_hypotheses_deregulated_nutrient_sensing_ovarian_mtor_follicle_reserve_aging_openscientist_artifacts_env_environment.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist environment
- filename: kb_hypotheses_deregulated_nutrient_sensing_ovarian_mtor_follicle_reserve_aging_openscientist_artifacts_logs_pubmed_search_log.md
  path: openscientist_artifacts/kb_hypotheses_deregulated_nutrient_sensing_ovarian_mtor_follicle_reserve_aging_openscientist_artifacts_logs_pubmed_search_log.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pubmed search log
- filename: kb_hypotheses_deregulated_nutrient_sensing_ovarian_mtor_follicle_reserve_aging_openscientist_artifacts_tables_data_source_inventory.csv
  path: openscientist_artifacts/kb_hypotheses_deregulated_nutrient_sensing_ovarian_mtor_follicle_reserve_aging_openscientist_artifacts_tables_data_source_inventory.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist data source inventory
- filename: kb_hypotheses_deregulated_nutrient_sensing_ovarian_mtor_follicle_reserve_aging_openscientist_artifacts_tables_evidence_matrix.csv
  path: openscientist_artifacts/kb_hypotheses_deregulated_nutrient_sensing_ovarian_mtor_follicle_reserve_aging_openscientist_artifacts_tables_evidence_matrix.csv
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
- **Disease Name:** Deregulated Nutrient Sensing Module
- **Category:** Module

## Target Hypothesis
- **Hypothesis ID:** ovarian_mtor_follicle_reserve_aging
- **Hypothesis Label:** mTOR Signaling Drives Human Ovarian Aging Through Follicle Reserve Depletion
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: ovarian_mtor_follicle_reserve_aging
hypothesis_label: mTOR Signaling Drives Human Ovarian Aging Through Follicle Reserve Depletion
status: EMERGING
description: The ovary ages earlier than any other organ, and mTOR signaling is the pathway the human
  ovarian aging atlas singles out as ovary-specific. This hypothesis holds that rising mTOR signaling
  in the aging ovary accelerates activation of dormant primordial follicles and so depletes the follicle
  reserve, which sets the timing of reproductive aging and menopause. It predicts that transient mTOR
  inhibition preserves the reserve and extends ovarian lifespan. Two points are open. The human evidence
  is transcript abundance of mTOR-pathway genes in eight ovaries, not measured kinase activity, and the
  one validated gene (RICTOR) belongs to mTORC2, so it is unsettled whether mTORC1, mTORC2 or both are
  involved and in which cell types. And the inhibition evidence is from mice, where long-term rapamycin
  also impairs follicle development and ovulation, so benefit depends on dosing schedule.
evidence:
- reference: PMID:39578560
  reference_title: Molecular and genetic insights into human ovarian aging from single-nuclei multi-omics
    analyses.
  supports: SUPPORT
  directness: INDIRECT
  evidence_source: HUMAN_CLINICAL
  snippet: Our analyses reveal coordinated changes in transcriptomes and chromatin accessibilities across
    cell types in the ovary during aging, notably mTOR signaling being a prominent ovary-specific aging
    pathway.
  explanation: Human single-nucleus data from four young and four reproductively aged ovaries name mTOR
    signaling as the ovary-specific aging pathway. INDIRECT because it reports pathway gene expression,
    not that mTOR activity causes reserve loss.
- reference: PMID:28544226
  reference_title: Short-term rapamycin treatment increases ovarian lifespan in young and middle-aged
    female mice.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: The effects of transient rapamycin treatment on ovarian lifespan were reflected in the preservation
    of primordial follicles, increases in oocyte quality, and improvement in the ovarian microenvironment.
  explanation: Two weeks of rapamycin in young or middle-aged mice prolongs ovarian lifespan with preserved
    primordial follicles, the prediction this hypothesis makes.
- reference: PMID:31887337
  reference_title: Rapamycin treatment maintains developmental potential of oocytes in mice and follicle
    reserve in human cortical fragments grafted into immune-deficient mice.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Using human ovarian cortical fragments grafted into immune-deficient mice, we demonstrated
    the ability of rapamycin to suppress follicle growth from the primordial stage.
  explanation: Extends the follicle-activation effect of mTOR inhibition to human ovarian tissue, though
    in xenografts rather than in women.
- reference: PMID:28544226
  reference_title: Short-term rapamycin treatment increases ovarian lifespan in young and middle-aged
    female mice.
  supports: REFUTE
  evidence_source: MODEL_ORGANISM
  snippet: However, the application is limited because of its detrimental effects on follicular development
    and ovulation during long-term treatment.
  explanation: 'Against a simple reading that less mTOR is better for the ovary: sustained inhibition
    harms follicle development, so the benefit is schedule-dependent.'
- reference: clinicaltrials:NCT05836025
  reference_title: Effect of Rapamycin in Ovarian Aging
  supports: SUPPORT
  directness: INDIRECT
  evidence_source: OTHER
  snippet: The investigators are proposing a prospective, randomized, double-blind, placebo-controlled
    pilot study assessing the ability of low-dose rapamycin to delay ovarian aging in women.
  explanation: A registered human trial (VIBRANT) testing the hypothesis's prediction in women. It is
    a registration, not a result, so it records that the test is under way rather than supporting the
    mechanism.
notes: Scoped to the ovary. It is separate from sex_dimorphic_geroprotector_exposure, which concerns whole-animal
  lifespan in both sexes and cannot be tested with female-only ovarian data.
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
result beneath `kb/hypotheses/deregulated_nutrient_sensing/ovarian_mtor_follicle_reserve_aging/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.


## Output

# Mechanistic Hypothesis Search — Final Report

## Hypothesis under evaluation
**ID:** `ovarian_mtor_follicle_reserve_aging`
**Label:** mTOR Signaling Drives Human Ovarian Aging Through Follicle Reserve Depletion
**Module:** Deregulated Nutrient Sensing
**KB status:** EMERGING

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED.**

The seed hypothesis holds that rising mTOR signaling in the aging ovary accelerates activation of dormant primordial follicles, depletes the follicle reserve, and thereby sets the timing of reproductive aging and menopause — with the corollary that transient mTOR inhibition preserves the reserve. After five iterations and review of 42 papers, the central mechanistic edge is **causally strong in mouse genetics and reproduced in human ovarian tissue ex vivo**, but the **human in-vivo evidence remains indirect**, and **two directional/scope caveats** prevent full endorsement.

The strongest support is for the **follicle-activation (quantity) axis**: loss of the brake PTEN raises PI3K–AKT–mTORC1 signaling, prematurely activates the entire primordial-follicle pool, and causes premature ovarian failure (POF) in mice; administering the mTORC1-specific inhibitor rapamycin *before* activation prevents this and preserves the reserve ([PMID:23326514](https://pubmed.ncbi.nlm.nih.gov/23326514/)). Transient (2-week) rapamycin prolongs ovarian lifespan with preserved primordial follicles in young and middle-aged mice ([PMID:28544226](https://pubmed.ncbi.nlm.nih.gov/28544226/)), and rapamycin suppresses follicle growth from the primordial stage in **human** ovarian cortical fragments and attenuates PI3K-signaling upregulation in **human** ovarian cortex in vitro ([PMID:31887337](https://pubmed.ncbi.nlm.nih.gov/31887337/), [PMID:38070496](https://pubmed.ncbi.nlm.nih.gov/38070496/)). The human ovarian aging atlas independently nominates mTOR as the ovary-specific aging pathway ([PMID:39578560](https://pubmed.ncbi.nlm.nih.gov/39578560/)).

Three caveats temper the verdict and define the gap between EMERGING and ESTABLISHED. **First**, the human in-vivo signal is transcript-level only — pathway gene abundance across eight ovaries, not measured kinase activity, and no completed interventional trial exists (VIBRANT/[NCT05836025](https://clinicaltrials.gov/study/NCT05836025) is registration-only as of 2026-10-18). **Second**, the one atlas-validated gene, **RICTOR**, belongs to **mTORC2**, whose loss is *pro-survival* and itself *causes* ovarian failure — the opposite direction from "less mTOR is better" ([PMID:25564616](https://pubmed.ncbi.nlm.nih.gov/25564616/)). So mTORC1 and mTORC2 act in opposing directions, and the human readout does not yet resolve which complex is causal. **Third**, the human genetics of menopause *timing* is dominated by DNA-damage-response (DDR) genes, not mTOR/nutrient-sensing ([PMID:26414677](https://pubmed.ncbi.nlm.nih.gov/26414677/), [PMID:35493704](https://pubmed.ncbi.nlm.nih.gov/35493704/)), which is a competing explanation for the hypothesis's boldest claim — that mTOR "sets the timing of menopause." The most defensible scope is therefore **mTORC1 as a driver of the follicle-activation *rate* (reserve quantity), not as the genetic menopause clock.**

---

## Key Findings

### F001 — PI3K/PTEN/AKT–mTOR hyperactivation drives premature primordial-follicle activation and reserve depletion; rapamycin suppresses it in human tissue

This is the load-bearing finding for the hypothesis, and it is supported by convergent evidence spanning human tissue and mouse models. In **human ovarian cortex in vitro** (n = 17 women, ages 21–41), the alkylating chemotherapeutic cyclophosphamide upregulated PI3K signaling and increased follicular activation; crucially, **rapamycin attenuated the PI3K-signaling upregulation** ([PMID:38070496](https://pubmed.ncbi.nlm.nih.gov/38070496/)). The verified snippet states: *"Exposure to cyclophosphamide compromises the health of primordial and transitional follicles in the human ovarian cortex and upregulates PI3K signalling, indicating both direct damage and increased follicular activation; AMH attenuates both of these chemotherapy-induced effects, while rapamycin attenuates only PI3K signalling upregulation."* In **human ovarian cortical xenografts** grafted into immune-deficient mice, rapamycin *"suppress[ed] follicle growth from the primordial stage"* ([PMID:31887337](https://pubmed.ncbi.nlm.nih.gov/31887337/)). And in mice, **short-term (2-week) rapamycin** in young and middle-aged females *"prolong[ed] ovarian lifespan"* with *"preservation of primordial follicles, increases in oocyte quality, and improvement in the ovarian microenvironment"* ([PMID:28544226](https://pubmed.ncbi.nlm.nih.gov/28544226/)). Review-level synthesis frames chronic mTOR hyperactivation as a central driver of ovarian aging and oocyte decline ([PMID:42580602](https://pubmed.ncbi.nlm.nih.gov/42580602/), review).

The significance is that the core prediction of the hypothesis — transient mTOR inhibition preserves the reserve — is directly demonstrated in human ovarian tissue (ex vivo/xenograft) and in intact mice. The limitation is that none of these are in-vivo human outcome data: the human experiments are cortical fragments or in-vitro cultures, and the mouse experiments, while causal, require interspecies extrapolation of dosing and timing.

### F002 — mTORC2 (RICTOR) is pro-survival; its loss causes POF, creating a directional tension with "more mTOR is worse"

The seed YAML itself flags this tension, and the investigation confirmed it as a genuine, mechanistically grounded contradiction rather than a semantic quibble. Oocyte-specific ablation of **Rictor** (the defining component of mTORC2) in mice produces POF phenotypes: *"massive follicular death, excessive loss of functional ovarian follicles, abnormal gonadal hormone secretion, and consequently, secondary subfertility"* ([PMID:25564616](https://pubmed.ncbi.nlm.nih.gov/25564616/)). Mechanistically, Rictor loss reduced p-Akt(Ser473) and p-Foxo3a(Ser253) and elevated pro-apoptotic Bad/Bax/cleaved-PARP, and the same study found mTORC2 signaling inhibited in a VCD-induced POF model. The authors conclude a *"critical role of the Rictor/mTORC2/Akt/Foxo3a pro-survival signaling axis in folliculogenesis."*

This matters because the single gene the human atlas highlighted and validated (**RICTOR**) is an mTORC2 component, yet mTORC2 signaling is **protective** — its reduction causes, rather than prevents, follicle loss. Therefore a naive reading of the atlas ("mTOR genes up → inhibit mTOR → preserve ovary") could be exactly backwards for the mTORC2 arm. The hypothesis is only coherent if the causal driver is **mTORC1**, which the next finding addresses.

### F003 — mTORC1 (not mTORC2) is the activation-driving arm; Pten-loss→mTORC1→global follicle activation→POF, prevented by mTORC1-specific rapamycin

This finding resolves the directional tension in favor of the hypothesis's intended mechanism, but only by narrowing it to mTORC1. The genetic causal chain in mice is explicit: oocyte **Pten** deletion raises *"phosphatidylinositol 3-kinase (PI3K)-Akt and mammalian target of rapamycin complex 1 (mTORC1) signaling in the oocytes,"* prematurely activating the entire primordial-follicle pool with depletion in early adulthood and POF; and *"when administered to Pten-deficient mice prior to the activation of the primordial follicles, rapamycin effectively prevented global follicular activation and preserved the ovarian reserve"* ([PMID:23326514](https://pubmed.ncbi.nlm.nih.gov/23326514/)). Chronic activation exhausts the pool whereas transient activation permits fertility, establishing **schedule-dependence**: *"Genetic modified mouse models with chronic activation of PI3K/mTOR signals in primordial oocytes showed premature activation of all primordial follicles and eventually their exhaustion"* ([PMID:25590233](https://pubmed.ncbi.nlm.nih.gov/25590233/)). The same PTEN/AKT/FOXO3a–mTOR "burnout" activation mechanism underlies chemotherapy-induced reserve loss by cyclophosphamide and cisplatin ([PMID:23677591](https://pubmed.ncbi.nlm.nih.gov/23677591/), [PMID:26656301](https://pubmed.ncbi.nlm.nih.gov/26656301/)).

The upshot: the hypothesis is mechanistically correct when scoped to **mTORC1-driven follicle activation**, and mTORC1-specific inhibition is the validated preventive lever. The schedule-dependence directly explains the built-in REFUTE evidence in the seed (long-term rapamycin harms follicle development and ovulation) — benefit is transient-dosing-dependent.

### F004 — Human menopause-timing genetics is dominated by DNA-damage-response genes, not mTOR — a competing mechanism for the "sets menopause timing" claim

This is the strongest *human* evidence in the entire search, and it argues against the hypothesis's most ambitious claim. Large GWAS/exome analyses of age at natural menopause (ANM) consistently implicate **genome-stability/DNA-repair** genes, not nutrient-sensing. A GWAS of ~70,000 women found 44+ loci with *"major association with DNA damage response (DDR) genes, including the first common coding variant in BRCA1 associated with any complex trait"* ([PMID:26414677](https://pubmed.ncbi.nlm.nih.gov/26414677/)). Whole-exome sequencing of **132,370 UK Biobank women** tested rare damaging variants against ANM and implicated DDR genes such as CHEK2 ([PMID:35493704](https://pubmed.ncbi.nlm.nih.gov/35493704/)), and a mismatch-repair variant in **MSH6** associates with ANM ([PMID:24357391](https://pubmed.ncbi.nlm.nih.gov/24357391/)). Review-level synthesis states roughly two-thirds of ANM loci involve DDR genes, grouping menopause genes into genome stability (DNA repair), immune function, and mitochondrial biogenesis ([PMID:27513022](https://pubmed.ncbi.nlm.nih.gov/27513022/), [PMID:27621233](https://pubmed.ncbi.nlm.nih.gov/27621233/); review-level).

The implication is scope-limiting: at the level of the human **genetic clock** that sets *when* menopause occurs, DDR — not mTOR — is the dominant signal. mTOR/nutrient-sensing pathway variants did not surface among the primary human ANM-timing loci in these searches. This does not refute the follicle-activation-rate mechanism, but it strongly argues the hypothesis should be scoped to the **quantity/activation-rate axis** rather than claiming to be the master determinant of menopause timing.

### F005 — Ovarian stromal fibrosis and an inflammaging/senescence shift are a parallel aging mechanism; mTOR inhibition may converge on the microenvironment, but no human rapamycin outcome data exist

Ovarian aging is not solely a follicle-activation story. Reproductive aging drives **ovarian stromal fibrosis** (increased collagen I/III by Picrosirius Red and hydroxyproline) with *"a unique population of multinucleated macrophage giant cells, which are associated with chronic inflammation ... within the ovarian stroma exclusively in reproductively old mice"* ([PMID:27491879](https://pubmed.ncbi.nlm.nih.gov/27491879/)). The post-reproductive ovary shifts toward an immune-dominant identity: *"post-reproductive ovaries exhibited increased infiltration of T cells, macrophages, and multinucleated giant cells"* ([PMID:42271623](https://pubmed.ncbi.nlm.nih.gov/42271623/)). The human atlas independently nominates *"enhanced activity of the transcription factor CEBPD across cell types in the aged ovary"* — a senescence/inflammation-associated TF — alongside mTOR ([PMID:39578560](https://pubmed.ncbi.nlm.nih.gov/39578560/)). Transient rapamycin *"improved the ovarian microenvironment"* in mice ([PMID:28544226](https://pubmed.ncbi.nlm.nih.gov/28544226/)), hinting at convergence, but as of the search date (2026-10-18) PubMed returned **no published results** for a human rapamycin/sirolimus ovarian-aging trial.

This frames fibrosis/inflammaging as a **parallel axis** that may be partly downstream of, or convergent with, mTOR, but is not reducible to follicle activation. It also surfaces an explicit data absence: no completed human interventional outcome exists.

---

## Mechanistic Model / Interpretation

The evidence resolves into a two-axis model of ovarian aging, in which the hypothesis maps cleanly onto one axis and competes with better-supported mechanisms on the other.

```
            UPSTREAM                  CORE EDGE (mTORC1 axis)              OUTCOME
  ┌─────────────────────────┐   ┌──────────────────────────────┐   ┌──────────────────┐
  │ PTEN loss / PI3K input    │   │  PI3K → AKT → mTORC1 ↑         │   │ Premature          │
  │ Chemotherapy (Cy, cisPt)  │──▶│  (FOXO3a cytoplasmic export)  │──▶│ primordial-        │──┐
  │ Nutrient/anabolic signal  │   │  → primordial follicle        │   │ follicle           │  │
  └─────────────────────────┘   │    ACTIVATION ("burnout")     │   │ ACTIVATION         │  │
                                 └──────────────────────────────┘   └──────────────────┘  │
                                        ▲ rapamycin (transient)                             │
                                        │ PREVENTS activation                               ▼
                                        │ (mTORC1-specific)                      ┌──────────────────────┐
                                                                                 │ Reserve DEPLETION →   │
  ── DIRECTIONAL TENSION ─────────────────────────────────────                   │ reduced fertility,    │
  │ mTORC2 (RICTOR) → AKT-Ser473 → FOXO3a → PRO-SURVIVAL      │                   │ early ovarian failure │
  │ Loss of mTORC2 → follicle DEATH → POF (opposite sign)    │                   └──────────────────────┘
  └──────────────────────────────────────────────────────────                               ▲
                                                                                             │
  PARALLEL AXIS (competing / convergent):                                                    │
  ┌──────────────────────────────────────────────────────────┐                              │
  │ DNA-damage-response (BRCA1/CHEK2/MSH6) → oocyte genome    │── sets menopause TIMING ─────┤
  │ Stromal fibrosis + inflammaging (CEBPD, macrophage GCs)  │── microenvironment decline ──┘
  └──────────────────────────────────────────────────────────┘
```

**Where the literature is strong:** the PTEN→PI3K/AKT→mTORC1→follicle-activation edge, and its prevention by transient mTORC1-specific rapamycin, are established in mouse genetics and reproduced in human ovarian tissue ex vivo. Schedule-dependence (transient benefit vs. chronic harm) is well characterized and reconciles the seed's internal SUPPORT/REFUTE pair.

**Where the links are inferred:** the human atlas names mTOR as ovary-specific, but this is transcript abundance, not measured kinase activity; the leap from "mTOR-pathway genes change" to "mTOR activity causes reserve loss in women" is inferred, not demonstrated in vivo in humans.

**Where causal steps are missing:** (1) which complex (mTORC1 vs mTORC2) and which cell type (oocyte vs granulosa vs stroma) carries the human signal; (2) whether mTOR sits upstream of, downstream of, or parallel to the DDR and fibrosis/inflammaging axes; (3) whether any human intervention preserves reserve or delays menopause — no outcome data exist.

---

## Evidence Matrix

| Citation | Evidence type | Role | Mechanistic claim tested | Key finding | Context/subtype | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:39578560](https://pubmed.ncbi.nlm.nih.gov/39578560/) | Human clinical (snRNA/multi-omics) | Supports (indirect) | mTOR is the ovary-specific aging pathway | mTOR signaling + CEBPD activity enriched across aged ovarian cell types | Human ovary, 4 young/4 aged (n=8) | Moderate; transcript abundance only, small n, no kinase activity |
| [PMID:23326514](https://pubmed.ncbi.nlm.nih.gov/23326514/) | Model organism (mouse genetics) | Supports (direct) | mTORC1 drives follicle activation; inhibition preserves reserve | Pten-loss→mTORC1↑→global activation→POF; pre-emptive rapamycin prevents it | Mouse oocyte Pten cKO | High for mTORC1 causality; interspecies extrapolation |
| [PMID:28544226](https://pubmed.ncbi.nlm.nih.gov/28544226/) | Model organism (mouse) | Supports + Refutes | Transient vs chronic mTOR inhibition | 2-wk rapamycin preserves primordial follicles, extends ovarian lifespan; long-term harms folliculogenesis/ovulation | Young & middle-aged mice | High; schedule-dependence is the key nuance |
| [PMID:31887337](https://pubmed.ncbi.nlm.nih.gov/31887337/) | Model organism (human xenograft) | Supports | Rapamycin suppresses human primordial-follicle activation | Rapamycin suppressed follicle growth from primordial stage in human cortical grafts | Human ovarian cortex, xenografted | Moderate–high; xenograft not in-woman |
| [PMID:38070496](https://pubmed.ncbi.nlm.nih.gov/38070496/) | In vitro (human ovarian cortex) | Supports | PI3K/mTOR activation drives activation; rapamycin blocks PI3K arm | Cyclophosphamide ↑PI3K & activation; rapamycin attenuated PI3K upregulation | Human cortex, n=17 (21–41 y) | Moderate–high; in-vitro, rapamycin hit only PI3K arm |
| [PMID:25590233](https://pubmed.ncbi.nlm.nih.gov/25590233/) | Model organism (mouse) | Supports/qualifies | Chronic mTOR activation exhausts reserve | Chronic PI3K/mTOR activation → premature activation of all follicles → exhaustion | Mouse genetic models | High for schedule-dependence |
| [PMID:23677591](https://pubmed.ncbi.nlm.nih.gov/23677591/) | Model organism (mouse) | Supports | Chemotherapy burnout via PI3K activation | Cyclophosphamide activates quiescent follicles ("burnout"); AS101 prevents loss | Mouse, chemo-induced | High for burnout mechanism |
| [PMID:26656301](https://pubmed.ncbi.nlm.nih.gov/26656301/) | Model organism (mouse) | Supports | PTEN/AKT/FOXO3a overactivation depletes reserve | Cisplatin ↓PTEN→FOXO3a translocation→dormant-follicle depletion | Mouse, chemo-induced | High for PTEN/FOXO3a edge |
| [PMID:25564616](https://pubmed.ncbi.nlm.nih.gov/25564616/) | Model organism (mouse genetics) | Competing/qualifies | mTORC2 is pro-survival (opposite sign) | Oocyte Rictor loss → follicular death, POF via Rictor/mTORC2/Akt/Foxo3a | Mouse oocyte Rictor cKO | High; establishes mTORC1≠mTORC2 directionality |
| [PMID:26414677](https://pubmed.ncbi.nlm.nih.gov/26414677/) | Human clinical (GWAS, ~70k) | Competing | What sets menopause timing | ANM dominated by DDR genes incl. BRCA1 | Human, age at natural menopause | High; strongest human-genetic competing signal |
| [PMID:35493704](https://pubmed.ncbi.nlm.nih.gov/35493704/) | Human clinical (exome, 132,370) | Competing | Rare-variant architecture of ANM | DDR genes (e.g. CHEK2) associate with ANM | Human, UK Biobank | High; large n |
| [PMID:24357391](https://pubmed.ncbi.nlm.nih.gov/24357391/) | Human clinical (GWAS) | Competing | DNA repair sets menopause timing | MSH6 mismatch-repair variant assoc. with ANM | Human | Moderate–high |
| [PMID:27491879](https://pubmed.ncbi.nlm.nih.gov/27491879/) | Model organism (mouse) | Competing/parallel | Fibrosis/inflammaging axis | Age-associated stromal fibrosis + macrophage giant cells | Reproductively old mice | High for parallel mechanism |
| [PMID:42271623](https://pubmed.ncbi.nlm.nih.gov/42271623/) | Model organism | Competing/parallel | Immune shift in aged ovary | Post-reproductive ovary acquires immune-like identity | Post-reproductive ovary | Moderate–high |
| [PMID:42580602](https://pubmed.ncbi.nlm.nih.gov/42580602/) | Review (+ docking) | Supports (review) | Chronic mTOR hyperactivation drives ovarian aging | Synthesis positioning mTOR as central driver; proposes pentadecanoic acid modulator | Review orientation | Low–moderate; review-level, docking only |
| [NCT05836025](https://clinicaltrials.gov/study/NCT05836025) | Trial registration | Supports (indirect) | Low-dose rapamycin delays ovarian aging in women | RCT registered (VIBRANT); no results posted | Human trial | Registration-only; no outcome data |

---

## Data and Tool Use

This investigation was a **literature-based hypothesis search**. No primary dataset, omics matrix, or structural file was downloaded or computationally analyzed; therefore no `execute_code` statistical analysis or Phenix structural run was performed. All conclusions derive from PubMed-indexed primary literature and the seed YAML. This is stated explicitly to avoid any implication that a dataset analysis was performed and then silently replaced by literature synthesis.

| Source / tool | Accession / URI | Access status | Query / scope | Relevance |
|---|---|---|---|---|
| PubMed | multiple PMIDs (see matrix) | Accessed; 42 papers reviewed | Queries on mTOR/rapamycin + ovarian aging; PTEN/PI3K follicle activation; mTORC2/RICTOR; menopause GWAS/DDR; ovarian fibrosis/inflammaging; human ovarian aging atlas | Directly relevant; primary literature |
| Human ovarian aging atlas | [PMID:39578560](https://pubmed.ncbi.nlm.nih.gov/39578560/) (data in GEO per source; related reanalysis uses GSE202601) | Cited only (abstract-level); raw snRNA/ATAC matrices not downloaded | n=8 ovaries (4 young/4 aged) | Core human evidence; **not** independently reanalyzed |
| ClinicalTrials.gov | [NCT05836025](https://clinicaltrials.gov/study/NCT05836025) (VIBRANT) | Cited; registration verified as registration-only | Low-dose rapamycin, ovarian aging, women, RCT | Directly relevant; **no results** posted as of 2026-10-18 |
| GWAS/exome ANM studies | PMID:26414677, 35493704, 24357391 | Abstract-level accessed | Age at natural menopause, DDR enrichment | Competing human-genetic evidence |

**Negative/absence search (label: partially verified):** A PubMed search for completed human rapamycin/sirolimus ovarian-aging outcome results returned no published trial results as of **2026-10-18**; VIBRANT (NCT05836025) is registration-only. This absence is recorded as curation-relevant but should be re-checked by a curator with the exact query string and date, because the search log here is prose-level rather than a saved machine-readable export.

**Analysis inventory:** No analysis was executed. Outcome label for every proposed computational analysis in this run: **skipped / reported-only**. The one computational step that *could* have been executed with available tooling — reanalyzing the atlas GEO matrices for cell-type- and complex-specific mTOR module scores — was **not accessed** and is explicitly flagged as not performed.

**Artifact bundle status:** Because no dataset was accessed and no analysis executed, a data-derived artifact bundle with checksummed inputs/outputs **was not produced** — per instructions, an empty bundle must not be created when no data source was accessed and no analysis ran. The inspectable deliverable is this report. The intended bundle path, had computation occurred, is `kb/hypotheses/deregulated_nutrient_sensing/ovarian_mtor_follicle_reserve_aging/openscientist_artifacts`.

---

## Mechanistic Causal Chain

| Step | Edge | Evidence strength | Source |
|---|---|---|---|
| 1 | Loss of PTEN brake / PI3K input → AKT activation | Strong (mouse genetic) | PMID:23326514, 22761722 |
| 2 | AKT → mTORC1 ↑ (+ FOXO3a cytoplasmic export) | Strong (mouse genetic) | PMID:23326514, 26656301 |
| 3 | mTORC1 ↑ → primordial-follicle activation ("burnout") | Strong (mouse) + reproduced in human tissue ex vivo | PMID:23326514, 25590233, 31887337, 38070496 |
| 4 | Sustained activation → reserve depletion → POF/early reproductive aging | Strong in models | PMID:23326514, 25590233, 23677591 |
| 5 | Transient mTORC1 inhibition ⊣ activation → reserve preserved | Strong in mouse; human ex vivo | PMID:23326514, 28544226, 31887337 |
| 6 | Human in-vivo: rising mTOR activity causes reserve loss in women | **Inferred only** (transcript-level atlas, n=8) | PMID:39578560 |
| 7 | mTOR sets menopause *timing* in humans | **Not supported / competing** (DDR dominates) | PMID:26414677, 35493704 |

Steps 1–5 are strong. Step 6 is the key inferred link (correlation, not perturbation, in humans). Step 7 is where the hypothesis overreaches: human timing genetics points to DDR, not mTOR.

---

## Limitations and Knowledge Gaps

**1. Human in-vivo causality is unestablished.** *Scope:* the human atlas ([PMID:39578560](https://pubmed.ncbi.nlm.nih.gov/39578560/)) reports transcript abundance across 8 ovaries, not kinase activity or perturbation. *Why it matters:* the hypothesis claims mTOR *activity* causes reserve loss in women; a transcript-level correlation cannot establish that. *Checked:* literature search found no human phospho-mTOR/phospho-S6/phospho-4EBP1 activity measurement linked to reserve loss. *Resolution:* phospho-signaling immunostaining (p-S6, p-4EBP1 for mTORC1; p-AKT-Ser473 for mTORC2) in graded human ovarian cortex by age, plus a completed interventional trial.

**2. mTORC1 vs mTORC2 attribution in humans.** *Scope:* the atlas-validated gene RICTOR is mTORC2, but mTORC2 is pro-survival ([PMID:25564616](https://pubmed.ncbi.nlm.nih.gov/25564616/)); mouse causality is for mTORC1 ([PMID:23326514](https://pubmed.ncbi.nlm.nih.gov/23326514/)). *Why it matters:* inhibiting the wrong complex could accelerate, not delay, ovarian failure. *Checked:* no human study isolates complex-specific activity by cell type. *Resolution:* complex- and cell-type-specific readouts in human ovary.

**3. Cell-type localization of the human signal.** *Scope:* oocyte vs granulosa vs stroma. *Why it matters:* rapamycin dosing/safety depends on which compartment drives activation. *Checked:* mouse data implicate oocyte PTEN/mTORC1; human cell-type resolution of *activity* is absent. *Resolution:* spatial/phospho multiplex imaging in human cortex.

**4. Competing DDR mechanism for menopause timing.** *Scope:* human ANM genetics is DDR-dominated ([PMID:26414677](https://pubmed.ncbi.nlm.nih.gov/26414677/), [PMID:35493704](https://pubmed.ncbi.nlm.nih.gov/35493704/)). *Why it matters:* the hypothesis's "sets menopause timing" claim is better explained by DDR. *Checked:* mTOR/nutrient-sensing variants did not surface among primary ANM loci. *Resolution:* MR/colocalization testing whether any mTOR-pathway eQTL associates with ANM independent of DDR.

**5. No completed human interventional outcome.** *Scope:* VIBRANT/[NCT05836025](https://clinicaltrials.gov/study/NCT05836025) registration-only. *Why it matters:* the prediction (transient rapamycin preserves reserve in women) is untested in vivo. *Checked:* no results posted as of 2026-10-18 (label: partially verified). *Resolution:* trial readout with AMH, antral follicle count, reproductive-lifespan endpoints.

**6. Relationship of mTOR to the fibrosis/inflammaging axis is unspecified.** *Scope:* fibrosis/CEBPD/immune shift are a parallel axis ([PMID:27491879](https://pubmed.ncbi.nlm.nih.gov/27491879/), [PMID:42271623](https://pubmed.ncbi.nlm.nih.gov/42271623/), [PMID:39578560](https://pubmed.ncbi.nlm.nih.gov/39578560/)). *Why it matters:* if reserve loss is substantially driven by microenvironment decline, mTOR-centric intervention may be insufficient. *Checked:* only indirect convergence (rapamycin "improved microenvironment" in mice). *Resolution:* test whether mTOR inhibition reduces stromal fibrosis/senescence markers in aged ovary.

**7. Source-level absences (unverified).** No GenCC/ClinGen gene–disease curation for an mTOR-pathway gene in ovarian aging was identified — but this was **not** systematically queried against a versioned snapshot, so it is labeled **unverified** rather than a confirmed absence; a curator should run a dated GenCC/ClinGen query. The human omics evidence rests on a single small atlas (n=8); no independent large human ovarian aging cohort with matched phospho-activity was found.

---

## Alternative Models

| Model | Relationship to seed | Summary |
|---|---|---|
| **DNA-damage-response / genome-stability** ([PMID:26414677](https://pubmed.ncbi.nlm.nih.gov/26414677/), [PMID:35493704](https://pubmed.ncbi.nlm.nih.gov/35493704/), [PMID:27621233](https://pubmed.ncbi.nlm.nih.gov/27621233/)) | **Competing (for timing)** | Human genetic clock of menopause timing is DDR-dominated; best explains *when* menopause occurs, independent of mTOR. Possibly upstream of oocyte attrition and activation thresholds. |
| **mTORC2/RICTOR pro-survival axis** ([PMID:25564616](https://pubmed.ncbi.nlm.nih.gov/25564616/)) | **Opposing-direction within the same pathway** | mTORC2 preserves follicles; its decline *causes* failure. Means "mTOR" is not monolithic — sign depends on complex. |
| **Stromal fibrosis / inflammaging / senescence** ([PMID:27491879](https://pubmed.ncbi.nlm.nih.gov/27491879/), [PMID:42271623](https://pubmed.ncbi.nlm.nih.gov/42271623/), CEBPD in [PMID:39578560](https://pubmed.ncbi.nlm.nih.gov/39578560/)) | **Parallel / possibly convergent** | Microenvironment decline partly independent of follicle activation; may be downstream of or convergent with mTOR. |
| **Mitochondrial dysfunction / oxidative stress / OXPHOS decline** ([PMID:41243550](https://pubmed.ncbi.nlm.nih.gov/41243550/), [PMID:42693473](https://pubmed.ncbi.nlm.nih.gov/42693473/), review) | **Parallel (quality axis)** | Drives oocyte *quality* decline and aneuploidy rather than reserve *quantity*; complements rather than competes. |
| **Chemotherapy "burnout" as accelerated phenocopy** ([PMID:23677591](https://pubmed.ncbi.nlm.nih.gov/23677591/), [PMID:26656301](https://pubmed.ncbi.nlm.nih.gov/26656301/)) | **Supporting / same edge** | Same PTEN/AKT/FOXO3a–mTOR activation drives iatrogenic reserve loss, validating the edge in a perturbation setting. |

Most parsimonious integrated reading: **mTORC1** governs *rate of follicle activation* (reserve quantity), **DDR** governs *genetic timing* of menopause and oocyte genome integrity, and **fibrosis/inflammaging** and **mitochondrial decline** govern *microenvironment and oocyte quality*. The seed hypothesis is well-supported for the first axis and overreaches when it claims to set menopause timing.

---

## Discriminating Tests

1. **Human phospho-signaling by age (mTORC1 vs mTORC2, by cell type).** Quantitative multiplex immunofluorescence for p-S6/p-4EBP1 (mTORC1) and p-AKT-Ser473 (mTORC2) in graded human ovarian cortex across age, resolved to oocyte/granulosa/stroma. *Expected if hypothesis true:* mTORC1 activity rises with age in the oocyte/primordial-follicle compartment and tracks activation markers; mTORC2 activity should not rise (or falls). Discriminates mTORC1-driver from mTORC2-confound.

2. **Complex-specific perturbation in human cortex ex vivo.** Compare mTORC1-selective (rapamycin/RapaLink, transient) vs mTORC2-selective knockdown on primordial-follicle activation in cultured human cortex. *Expected:* mTORC1 inhibition preserves dormancy; mTORC2 inhibition accelerates loss — directly testing F002 vs F003.

3. **VIBRANT ([NCT05836025](https://clinicaltrials.gov/study/NCT05836025)) readout with reserve endpoints.** AMH, antral follicle count, and ideally follicle density on biopsy, under transient low-dose rapamycin vs placebo. *Expected:* transient dosing preserves reserve without impairing ovulation; chronic dosing would not (schedule-dependence).

4. **Mendelian randomization: mTOR-pathway eQTLs vs ANM, conditioned on DDR.** Test whether any mTOR-pathway genetic instrument associates with age at natural menopause independent of DDR loci. *Expected if hypothesis overreaches on timing:* null for mTOR after conditioning on DDR, confirming timing is DDR-driven.

5. **mTOR inhibition on the fibrosis/inflammaging axis.** In aged mouse ovary, test whether transient rapamycin reduces stromal collagen I/III, macrophage giant cells, and CEBPD-target senescence markers. *Expected:* partial reduction shows convergence; no effect confirms fibrosis as a truly parallel, mTOR-independent axis.

---

## Curation Leads (require curator verification)

- **Status:** Retain **EMERGING**, but add explicit scope note: *supported for the mTORC1-driven follicle-activation (reserve-quantity) axis; not supported as the determinant of genetic menopause timing (DDR-dominated).*
- **Candidate evidence to add (verify snippets against abstracts):**
  - [PMID:23326514](https://pubmed.ncbi.nlm.nih.gov/23326514/) — *"When administered to Pten-deficient mice prior to the activation of the primordial follicles, rapamycin effectively prevented global follicular activation and preserved the ovarian reserve."* (SUPPORT, DIRECT, model organism — establishes mTORC1-specific causal edge.)
  - [PMID:25564616](https://pubmed.ncbi.nlm.nih.gov/25564616/) — *"mice with oocyte-specific ablation of Rictor, a key component of mTORC2, demonstrated POF phenotypes..."* (QUALIFIES/COMPETING — mTORC2 pro-survival, opposite sign.)
  - [PMID:38070496](https://pubmed.ncbi.nlm.nih.gov/38070496/) — *"rapamycin attenuates only PI3K signalling activation, in human ovarian cortex in vitro."* (SUPPORT — human tissue.)
  - [PMID:26414677](https://pubmed.ncbi.nlm.nih.gov/26414677/) — *"Pathway analyses identified major association with DNA damage response (DDR) genes, including the first common coding variant in BRCA1 associated with any complex trait."* (COMPETING — human menopause timing.)
  - [PMID:25590233](https://pubmed.ncbi.nlm.nih.gov/25590233/) — *"chronic activation of PI3K/mTOR signals in primordial oocytes showed premature activation of all primordial follicles and eventually their exhaustion."* (SUPPORT/qualifies — schedule-dependence.)
- **Candidate pathophysiology edges:** `PTEN loss ─┤ PI3K/AKT/mTORC1 ↑ → primordial-follicle activation → reserve depletion → POF`; `mTORC1 inhibition (transient) ⊣ follicle activation`; `mTORC2/RICTOR → pro-survival → follicle maintenance` (distinct edge, opposite effect).
- **Candidate ontology terms:** cell types — oocyte, granulosa cell, ovarian stromal cell, ovarian macrophage; biological processes — primordial follicle activation, TORC1 signaling (GO:0038202), TORC2 signaling (GO:0038203), ovarian follicle atresia, cellular senescence.
- **Candidate subtype restriction:** scope the "sets menopause timing" claim out; restrict to **follicle-activation rate / ovarian reserve quantity**.
- **Candidate `knowledge_gaps` prompts:** (1) mTORC1-vs-mTORC2 directionality unresolved in human cell types; (2) no human in-vivo kinase-activity or interventional-outcome evidence (VIBRANT registration-only as of 2026-10-18); (3) relationship of mTOR to DDR and to fibrosis/inflammaging axes unspecified; (4) unverified GenCC/ClinGen absence — curator to run dated query.

---

## Evidence Base (summary of key papers)

- **Core human atlas:** [PMID:39578560](https://pubmed.ncbi.nlm.nih.gov/39578560/) — names mTOR as ovary-specific aging pathway and CEBPD as an aging TF; transcript-level, n=8.
- **mTORC1 causal chain:** [PMID:23326514](https://pubmed.ncbi.nlm.nih.gov/23326514/), [PMID:25590233](https://pubmed.ncbi.nlm.nih.gov/25590233/) — Pten/mTORC1 drives activation; schedule-dependent.
- **Transient rapamycin benefit (+ chronic harm):** [PMID:28544226](https://pubmed.ncbi.nlm.nih.gov/28544226/).
- **Human tissue translation:** [PMID:31887337](https://pubmed.ncbi.nlm.nih.gov/31887337/), [PMID:38070496](https://pubmed.ncbi.nlm.nih.gov/38070496/).
- **mTORC2 directional tension:** [PMID:25564616](https://pubmed.ncbi.nlm.nih.gov/25564616/).
- **Competing human menopause genetics:** [PMID:26414677](https://pubmed.ncbi.nlm.nih.gov/26414677/), [PMID:35493704](https://pubmed.ncbi.nlm.nih.gov/35493704/), [PMID:24357391](https://pubmed.ncbi.nlm.nih.gov/24357391/), [PMID:27513022](https://pubmed.ncbi.nlm.nih.gov/27513022/), [PMID:27621233](https://pubmed.ncbi.nlm.nih.gov/27621233/).
- **Parallel fibrosis/inflammaging axis:** [PMID:27491879](https://pubmed.ncbi.nlm.nih.gov/27491879/), [PMID:42271623](https://pubmed.ncbi.nlm.nih.gov/42271623/).
- **Chemotherapy burnout phenocopy:** [PMID:23677591](https://pubmed.ncbi.nlm.nih.gov/23677591/), [PMID:26656301](https://pubmed.ncbi.nlm.nih.gov/26656301/).
- **Review orientation:** [PMID:42580602](https://pubmed.ncbi.nlm.nih.gov/42580602/) (mTOR hyperactivation as driver; docking only — review-level).

---

## Proposed Follow-up Actions

1. **Curate the scope restriction** (quantity/activation axis, not timing) and add the mTORC1/mTORC2 directional-tension knowledge gap to the KB.
2. **Reanalyze the human atlas raw data** (if accessible via GEO) to test cell-type- and complex-specific mTOR module scores vs age — the one computational step that could be executed with available tooling but was not accessed in this run (explicitly flagged as not performed).
3. **Monitor VIBRANT/[NCT05836025](https://clinicaltrials.gov/study/NCT05836025)** for results posting; its readout is the single most decisive human test.
4. **Run a dated GenCC/ClinGen query** to confirm or refute the source-level absence of mTOR-pathway gene–ovarian-aging curation.
5. **Add the DDR axis as a formally linked competing hypothesis** in the Deregulated Nutrient Sensing module cross-references.

---

*Verdict: **Partially supported**, scoped to the mTORC1 follicle-activation/reserve-quantity axis. Search date: 2026-10-18.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist README](openscientist_artifacts/kb_hypotheses_deregulated_nutrient_sensing_ovarian_mtor_follicle_reserve_aging_openscientist_artifacts_README.md)
- [OpenScientist environment](openscientist_artifacts/kb_hypotheses_deregulated_nutrient_sensing_ovarian_mtor_follicle_reserve_aging_openscientist_artifacts_env_environment.md)
- [OpenScientist pubmed search log](openscientist_artifacts/kb_hypotheses_deregulated_nutrient_sensing_ovarian_mtor_follicle_reserve_aging_openscientist_artifacts_logs_pubmed_search_log.md)
- [OpenScientist data source inventory](openscientist_artifacts/kb_hypotheses_deregulated_nutrient_sensing_ovarian_mtor_follicle_reserve_aging_openscientist_artifacts_tables_data_source_inventory.csv)
- [OpenScientist evidence matrix](openscientist_artifacts/kb_hypotheses_deregulated_nutrient_sensing_ovarian_mtor_follicle_reserve_aging_openscientist_artifacts_tables_evidence_matrix.csv)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.