---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-13T20:10:56.837773'
end_time: '2026-09-13T20:31:49.966848'
duration_seconds: 1253.13
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Fanconi_Anemia
  category: Genetic
  hypothesis_group_id: fa_moyamoya_vasculopathy
  hypothesis_label: FA-Associated Cerebral Arteriopathy
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: fa_moyamoya_vasculopathy\nhypothesis_label:\
    \ FA-Associated Cerebral Arteriopathy\nstatus: EMERGING\ndescription: The moyamoya\
    \ phenomenon reported in Fanconi anemia reflects an intrinsic arteriopathy of\n\
    \  FA-deficient vascular smooth muscle or endothelium, possibly sharing the RNF213-independent\
    \ progenitor-apoptosis\n  route of other FA structural anomalies, rather than\
    \ a coincidental association or a consequence of cranial\n  irradiation or transplantation.\n\
    evidence:\n- reference: PMID:25719591\n  reference_title: Fanconi anemia associated\
    \ with moyamoya disease in Saudi Arabia.\n  supports: SUPPORT\n  evidence_source:\
    \ HUMAN_CLINICAL\n  snippet: The association of moyamoya disease with FA is uncommon,\
    \ and is rarely reported in the literature.\n  explanation: Seed reference; the\
    \ association rests on a handful of case reports and has no proposed\n    mechanism."
  artifact_dir: kb/hypotheses/Fanconi_Anemia/fa_moyamoya_vasculopathy/openscientist_artifacts
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
  total_terms: 6
  verified: 6
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0016820
    reported_labels:
    - verify
    ontology_label: Moyamoya disease
  - term_id: MONDO:0019391
    reported_labels:
    - verify
    ontology_label: Fanconi anemia
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 9
artifact_sources:
  openscientist_artifacts_zip: 9
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
- filename: kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_data_evidence_matrix.csv
  path: openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_data_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_data_gtex_artery_pivot_all_markers.csv
  path: openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_data_gtex_artery_pivot_all_markers.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gtex artery pivot all markers
- filename: kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_data_gtex_fa_genes_artery_expression.csv
  path: openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_data_gtex_fa_genes_artery_expression.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gtex fa genes artery expression
- filename: kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_logs_clinicaltrials_negative_search.json
  path: openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_logs_clinicaltrials_negative_search.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist clinicaltrials negative search
- filename: kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_logs_gtex_query_log.json
  path: openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_logs_gtex_query_log.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gtex query log
- filename: kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_logs_gwas_catalog_moyamoya.json
  path: openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_logs_gwas_catalog_moyamoya.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gwas catalog moyamoya
- filename: kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_logs_preflight_connectivity.json
  path: openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_logs_preflight_connectivity.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist preflight connectivity
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Fanconi_Anemia
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** fa_moyamoya_vasculopathy
- **Hypothesis Label:** FA-Associated Cerebral Arteriopathy
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: fa_moyamoya_vasculopathy
hypothesis_label: FA-Associated Cerebral Arteriopathy
status: EMERGING
description: The moyamoya phenomenon reported in Fanconi anemia reflects an intrinsic arteriopathy of
  FA-deficient vascular smooth muscle or endothelium, possibly sharing the RNF213-independent progenitor-apoptosis
  route of other FA structural anomalies, rather than a coincidental association or a consequence of cranial
  irradiation or transplantation.
evidence:
- reference: PMID:25719591
  reference_title: Fanconi anemia associated with moyamoya disease in Saudi Arabia.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: The association of moyamoya disease with FA is uncommon, and is rarely reported in the literature.
  explanation: Seed reference; the association rests on a handful of case reports and has no proposed
    mechanism.
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
result beneath `kb/hypotheses/Fanconi_Anemia/fa_moyamoya_vasculopathy/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.


## Output

# FA-Associated Cerebral Arteriopathy (`fa_moyamoya_vasculopathy`) — Mechanistic Hypothesis Search Report

**Disease:** Fanconi Anemia (Genetic)
**Hypothesis ID:** `fa_moyamoya_vasculopathy`
**Status in KB:** EMERGING
**Search / analysis date:** 2026-09-13
**Recommended status after this search:** **Retain EMERGING** (weakly supported, mechanistically unresolved)

---

## Executive Judgment

**Verdict: WEAKLY SUPPORTED / UNRESOLVED.** The hypothesis that moyamoya in Fanconi anemia (FA) reflects an *intrinsic arteriopathy of FA-deficient vascular smooth muscle or endothelium* — sharing the RNF213-independent progenitor-apoptosis route of other FA structural anomalies — is biologically *plausible* but has **never been directly tested in any vascular tissue, vascular cell model, cohort, or trial**. The entire clinical basis is a handful of case reports spanning 44 years, and the proposed mechanism is an extrapolation from hematopoietic and embryonic biology.

The strongest arguments *for* the seed claim are: (1) the only genotyped FA-moyamoya patients (Pavlakis 1995) were compound heterozygotes for a specific **FANCC** allele combination (322delG + R185X) that was absent from 174 other screened FA families, suggesting a genotype-linked, possibly congenital vascular predisposition rather than random co-occurrence; and (2) in several early cases the moyamoya *predated* any transplant or cranial irradiation, arguing against a purely iatrogenic explanation in those patients. FA's established **TP53-dependent progenitor apoptosis and hyperactive TGF-β growth-suppression program** provides a credible in-principle mechanism for a developmental/structural vascular anomaly.

The arguments *against* — or that sharply limit the scope of — the hypothesis are substantial. Moyamoya is **not part of the recognized FA malformation spectrum (VACTERL-H)**. FA structural anomalies map preferentially to the **ID complex (FANCD2/FANCI)**, yet the only molecularly characterized FA-moyamoya cases carried an **upstream-complex (FANCC)** genotype associated with *milder* structural phenotypes — a subtype tension the seed does not resolve. Moyamoya genetics are overwhelmingly dominated by **RNF213**, which was *never genotyped* in any FA-moyamoya case; our GWAS Catalog query returned **zero** FA-pathway genes at any moyamoya locus. Our GTEx analysis showed FA-pathway genes are expressed but **not artery-enriched**, while RNF213 is comparatively artery-high. Finally, **radiation-induced moyamoya syndrome** is a well-established, dose- and age-dependent competing mechanism that is potentially radiologically distinguishable. The central causal step the hypothesis requires — *FA loss → vascular-cell/progenitor apoptosis → cerebral arteriopathy* — currently has **zero direct evidence**. Given a genuine but anecdotal signal and an untested mechanism, EMERGING is the appropriate status.

---

## Key Findings

### F001 — The FA–moyamoya association is real but rests on ~6 case reports over 44 years with no mechanistic study

Systematic PubMed retrieval established that the *complete* FA–moyamoya literature consists of case reports and small series only:

| Report | PMID | n | Context |
|---|---|---|---|
| Cohen 1980 | [7367089](https://pubmed.ncbi.nlm.nih.gov/7367089/) | 1 | Frames moyamoya as a congenital FA malformation |
| Pavlakis 1995 | [7746424](https://pubmed.ncbi.nlm.nih.gov/7746424/) | 2 (of 434 FA database) | Only denominator-based prevalence (~0.46%); FANCC genotype |
| Hoffman 1997 | [9409403](https://pubmed.ncbi.nlm.nih.gov/9409403/) | 1 (of 30-child moyamoya series) | Surgical series; FA patient died 7 yr post-EDAS |
| Al-Hawsawi 2015 (seed) | [25719591](https://pubmed.ncbi.nlm.nih.gov/25719591/) | 1 | Moyamoya diagnosed before HSCT |
| Alavi 2024 | [38510908](https://pubmed.ncbi.nlm.nih.gov/38510908/) | 1 | Questions congenital vs. hemorrhagic origin |

No cohort study, no case-control study, and no molecular/vascular-tissue mechanistic study of an FA arteriopathy was found. Targeted searches for "Fanconi anemia endothelial dysfunction/oxidative stress vascular," "FANCC vascular endothelial phenotype," and "Fanconi anemia arterial stenosis cerebrovascular" returned **no usable mechanistic result**. The seed reference itself states: *"The association of moyamoya disease with FA is uncommon, and is rarely reported in the literature"* ([PMID: 25719591](https://pubmed.ncbi.nlm.nih.gov/25719591/)). Pavlakis 1995 provides the only denominator: *"We report two patients with Fanconi anemia (FA) and moyamoya disease taken from a clinical database composed of 434 FA patients"* ([PMID: 7746424](https://pubmed.ncbi.nlm.nih.gov/7746424/)), i.e. ~2/434 (~0.46%).

### F002 — Strongest support: FANCC genotype-specific, congenital, pre-transplant moyamoya

Pavlakis 1995 ([PMID: 7746424](https://pubmed.ncbi.nlm.nih.gov/7746424/)) found both FA-moyamoya patients were compound heterozygotes for **FANCC 322delG + R185X**, a combination absent from 174 other FA families screened — supporting a genotype-specific vascular predisposition rather than chance co-occurrence. The authors explicitly propose: *"Either the 322delG or R185X mutation alone or in combination may predispose to primary, possibly congenital, vascular anomalies."* Cohen 1980 ([PMID: 7367089](https://pubmed.ncbi.nlm.nih.gov/7367089/)) likewise suggested *"the moyamoya might pertain to the array of congenital malformations associated with Fanconi's anemia."* Temporally, the moyamoya preceded any transplant or irradiation in the early cases (which predate routine FA HSCT), and in Al-Hawsawi 2015 the moyamoya was diagnosed *before* stem-cell transplantation — arguing against a purely iatrogenic cause **in these specific patients**. This is the empirical core of the seed hypothesis.

### F003 — Competing mechanisms: radiation-induced moyamoya (distinguishable by MR) and RNF213 vasculopathy

Radiation-induced moyamoya syndrome (RIMS) is a well-established, dose- and age-dependent entity. The PENTEC meta-analysis ([PMID: 36057476](https://pubmed.ncbi.nlm.nih.gov/36057476/)) modeled cerebrovascular toxicity rising with dose to the circle of Willis: **0.2% at 30 Gy, 1.3% at 45 Gy, 4.4% at 54 Gy**; younger age is a key risk factor ([PMID: 31805403](https://pubmed.ncbi.nlm.nih.gov/31805403/), [PMID: 37354243](https://pubmed.ncbi.nlm.nih.gov/37354243/)). RIMS follows cranial irradiation for BMT conditioning ([PMID: 17357039](https://pubmed.ncbi.nlm.nih.gov/17357039/)) and prophylactic CNS irradiation in leukemia ([PMID: 14512691](https://pubmed.ncbi.nlm.nih.gov/14512691/)) — exposures directly relevant to transplanted FA patients. Critically, RIMS may be **radiologically distinguishable**: radiation-induced arteritis shows significantly more prominent arterial-wall ring enhancement than idiopathic moyamoya (*"Contrast enhancement of the arterial walls in patients with radiation-induced arteritis was significantly more prominent than in patients with moyamoya disease (P = .003)"*; Aoki 2002, [PMID: 12034935](https://pubmed.ncbi.nlm.nih.gov/12034935/)). Separately, RNF213 is the principal moyamoya susceptibility gene; RNF213 loss-of-function in endothelial/VSMC models drives aberrant angiogenesis and VSMC phenotype switching via **JAK2/STAT3** and **HIF-1α/VEGF** ([PMID: 40467938](https://pubmed.ncbi.nlm.nih.gov/40467938/), [PMID: 42193873](https://pubmed.ncbi.nlm.nih.gov/42193873/), [PMID: 42652131](https://pubmed.ncbi.nlm.nih.gov/42652131/)). **RNF213 was never genotyped in any FA-moyamoya case.**

### F004 — GTEx: FA-pathway genes are expressed in artery but not artery-enriched; RNF213 is comparatively artery-high

Computational analysis of GTEx v8 median gene-level TPM (healthy adult bulk tissue, 54 tissues; queried 2026-09-13, **outcome = succeeded**). In aorta / coronary / tibial artery:

| Gene | Median TPM (artery) | Tissue percentile |
|---|---|---|
| RNF213 | 17.8–23.2 | 50th–78th |
| FANCG | 7.6–8.9 | 39th–50th |
| FANCC | 2.6–3.1 | 39th–56th |
| FANCI | 2.3–2.6 | 41st–48th |
| FANCD2 | 0.9–1.2 | 33rd–46th |
| FANCA | 0.3–0.7 | 6th–31st |
| BRCA2 | 0.3–0.5 | (proliferation-linked) |

No FA-pathway gene is artery-enriched (all near or below median tissue percentile). RNF213 is roughly **3–8× the FA genes** and sits comparatively artery-high. Vascular identity of samples confirmed by ACTA2 (~5000–7700 TPM) and PECAM1 (44–93 TPM). This does not refute the hypothesis — a gene need not be tissue-enriched to be functionally critical — but it provides no positive transcriptomic signal that FA genes have a specialized arterial role, whereas RNF213 does. *Artifacts: `openscientist_artifacts/data/gtex_fa_genes_artery_expression.csv`, `gtex_artery_pivot_all_markers.csv`; `code/gtex_query.py`; `logs/gtex_query_log.json`.*

### F005 — The FA progenitor-apoptosis / TGF-β route is established, but only in HSPCs and embryos — never in vascular cells

The seed invokes an "RNF213-independent progenitor-apoptosis route of other FA structural anomalies." That route genuinely exists for FA: (1) across inherited bone-marrow-failure syndromes, *"an overarching hypothesis states that different stresses elicit TP53-dependent growth arrest and apoptosis of hematopoietic stem, progenitor, and precursor cells"* (Kawashima 2023, [PMID: 37627314](https://pubmed.ncbi.nlm.nih.gov/37627314/)); (2) a genome-wide shRNA screen identified *"transforming growth factor-β (TGF-β) pathway-mediated growth suppression as a cause of BMF in FA,"* with TGF-β inhibition rescuing HSPC survival (Zhang 2016, [PMID: 27053300](https://pubmed.ncbi.nlm.nih.gov/27053300/)); (3) *"the Fancd2−/−Smad3−/− double knockout mice undergo high levels of embryonic lethality due to loss of the TGFβ-NHEJ axis"* (Rodríguez 2022, [PMID: 36441774](https://pubmed.ncbi.nlm.nih.gov/36441774/)), tying the pathway to FA developmental/embryonic pathology. **However, every demonstration is in hematopoietic stem/progenitor cells, bone-marrow MSCs, or whole embryos.** No study localizes this apoptosis/TGF-β program to vascular smooth muscle, endothelium, or their progenitors, nor to cerebral arteriopathy/moyamoya. The mechanism the seed extrapolates is real in principle but *unlocalized* to the relevant tissue.

### F006 — Subtype tension: moyamoya is not in VACTERL-H, and FA anomalies map to the ID complex, whereas genotyped FA-moyamoya was FANCC

The recognized FA congenital-anomaly spectrum is **VACTERL-H**: *"vertebral anomalies, anal atresia, congenital heart disease, tracheo-esophageal fistula, esophageal atresia, renal, limb anomalies, and hydrocephalus"* (Alter & Giri 2016, [PMID: 27028275](https://pubmed.ncbi.nlm.nih.gov/27028275/)); VACTERL-H frequency in FA is ~33% (18/54, P<0.0001 vs. prior 5% estimate). Cerebral arteriopathy/moyamoya is **not** a listed feature. Genotype–phenotype data (Altintas 2023, [PMID: 35417938](https://pubmed.ncbi.nlm.nih.gov/35417938/)) show *"ID complex was associated with VACTERL-H,"* while upstream-complex variants confer a less-severe phenotype lacking VACTERL-H. Yet the only molecularly characterized FA-moyamoya patients carried **FANCC (upstream complex)** — a group generally *poorer* in structural malformations. This creates a genuine subtype tension: if moyamoya were an FA developmental structural anomaly, one would expect it to track with the ID complex, not FANCC.

### F007 — Documented source absence: no ClinicalTrials.gov study addresses FA cerebral arteriopathy/moyamoya

ClinicalTrials.gov API v2 queried 2026-09-13 (**outcome = succeeded, negative**). Query `"Fanconi anemia moyamoya"` returned **totalCount = 0**. `"Fanconi anemia vasculopathy"` returned 8 records, all HSCT/registry/other studies (cord-blood transplant, rare-kidney registry, cranioplasty perfusion) with none targeting FA cerebral arteriopathy. `"Fanconi anemia cerebral arteriopathy"` returned 1 non-FA-specific cranioplasty study. *Artifact: `openscientist_artifacts/logs/clinicaltrials_negative_search.json`.*

### F008 — GWAS Catalog: RNF213 is the sole reported moyamoya gene; no FA-pathway gene maps to any moyamoya locus

EBI GWAS Catalog REST API queried 2026-09-13 (**outcome = succeeded**) for diseaseTrait "Moyamoya disease" returned 4 studies (GCST000860/PMID 21048783, GCST005575/PMID 29273593, GCST90310003, GCST90705091). Author-reported genes: **RNF213** (in both gene-reporting studies), plus HDAC9, MTHFR, LRP1, FADS1/2, JAZF1, CARD14, TCN2. Screening all 16 canonical FA-pathway genes (FANCA–M, BRCA1/2, BRIP1, PALB2, RAD51C, SLX4) against these loci returned **zero hits**. *Artifact: `openscientist_artifacts/logs/gwas_catalog_moyamoya.json`.*

### F009 — Overall verdict: weakly supported / mechanistically unresolved; retain EMERGING

Synthesis across 8 recorded findings and 3 executed database analyses (GTEx v8, ClinicalTrials.gov v2, GWAS Catalog; all outcome = succeeded, 2026-09-13). The central missing causal step — *FA loss → vascular-cell/progenitor apoptosis → arteriopathy* — has zero direct evidence, and RNF213 was never excluded in any FA-moyamoya case.

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [25719591](https://pubmed.ncbi.nlm.nih.gov/25719591/) (seed) | Human clinical (case) | Supports (weak) | FA ↔ moyamoya association | Rare, anecdotal association; moyamoya diagnosed pre-HSCT | 1 patient, Saudi Arabia | Very low; single case, no mechanism |
| [7746424](https://pubmed.ncbi.nlm.nih.gov/7746424/) | Human clinical (2 of 434) | Supports | FANCC genotype-specific congenital vascular predisposition | 322delG+R185X absent from 174 other families; ~2/434 prevalence | FANCC (upstream complex) | Low–moderate; small n, no vascular tissue analysis |
| [7367089](https://pubmed.ncbi.nlm.nih.gov/7367089/) | Human clinical (case) | Supports (weak) | Moyamoya as congenital FA malformation | Framed as intrinsic congenital anomaly | Single case | Very low; assertion, not test |
| [38510908](https://pubmed.ncbi.nlm.nih.gov/38510908/) | Human clinical (case) | Qualifies | Congenital vs. hemorrhagic origin | Questions whether pattern reflects recurrent carotid-siphon bleeds | 9-yr-old boy | Very low; raises alternative |
| [9409403](https://pubmed.ncbi.nlm.nih.gov/9409403/) | Human clinical (series) | Qualifies | FA in moyamoya surgical cohort | 1 FA child among 30; died of FA 7 yr post-op | Pediatric surgical | Low; incidental co-occurrence |
| [27053300](https://pubmed.ncbi.nlm.nih.gov/27053300/) | Model / in vitro | Supports (plausibility) | Hyperactive TGF-β drives FA progenitor loss | TGF-β inhibition rescues HSPC survival | Hematopoietic only | Moderate for HSPCs; not vascular |
| [36441774](https://pubmed.ncbi.nlm.nih.gov/36441774/) | Model organism | Supports (plausibility) | TGFβ-NHEJ axis in FA development | Fancd2−/−Smad3−/− embryonic lethality | Whole embryo | Moderate; not vascular-localized |
| [37627314](https://pubmed.ncbi.nlm.nih.gov/37627314/) | Review | Supports (plausibility) | TP53-dependent progenitor apoptosis | Overarching IBMFS model | Hematopoietic | Review-level; orientation only |
| [27028275](https://pubmed.ncbi.nlm.nih.gov/27028275/) | Human clinical | Qualifies/limits | Defines FA malformation spectrum | VACTERL-H (~33%); moyamoya absent | FA cohort | High; strong scope limitation |
| [35417938](https://pubmed.ncbi.nlm.nih.gov/35417938/) | Human clinical (NCI cohort) | Qualifies/limits | Genotype–phenotype of FA anomalies | ID complex ↔ VACTERL-H; FANCC milder | NCI FA cohort | High; creates subtype tension |
| [40467938](https://pubmed.ncbi.nlm.nih.gov/40467938/) | In vitro | Competing | RNF213 loss → angiogenesis/VSMC switching | JAK2/STAT3, VEGF upregulation | Moyamoya models | Moderate; alternative mechanism |
| [42193873](https://pubmed.ncbi.nlm.nih.gov/42193873/) | In vitro / patient vessels | Competing | RNF213 in EC-VSMC crosstalk | RNAi impairs angiogenesis; MA vessel arrays | Moyamoya angiopathy | Moderate; alternative mechanism |
| [42652131](https://pubmed.ncbi.nlm.nih.gov/42652131/) | Review | Competing | RNF213 as panvascular hub | HIF-1α/VEGF, NF-κB, Wnt; second-hit model | Systemic vasculopathy | Review-level; alternative |
| [36057476](https://pubmed.ncbi.nlm.nih.gov/36057476/) | Human clinical (meta) | Competing | Radiation-induced cerebrovascular toxicity | Dose-response 0.2→4.4% (30→54 Gy) | Pediatric RT | High; strong iatrogenic alternative |
| [12034935](https://pubmed.ncbi.nlm.nih.gov/12034935/) | Human clinical | Competing/discriminating | Imaging biomarker for radiation arteritis | Wall enhancement > idiopathic MMD (P=.003) | RT arteritis vs. MMD | Moderate; discriminating test |
| [17357039](https://pubmed.ncbi.nlm.nih.gov/17357039/) | Human clinical (case) | Competing | Moyamoya after BMT-conditioning irradiation | Iatrogenic pathway in transplant setting | Post-BMT | Low–moderate; relevant to FA HSCT |
| GTEx v8 (our analysis) | Computational | Qualifies | FA-gene arterial expression | FA genes expressed, not artery-enriched; RNF213 artery-high | Healthy artery | Moderate; bulk tissue, not disease |
| GWAS Catalog (our analysis) | Computational | Qualifies/limits | FA genes at moyamoya loci | Zero FA-gene hits; RNF213 dominant | Moyamoya GWAS | Moderate; author-reported genes |
| ClinicalTrials.gov v2 (our analysis) | Computational | Source absence | Trials on FA arteriopathy | Zero relevant trials | — | High; documented absence |

---

## Data and Tool Use

| Source | Accession / URI | Version / snapshot | Retrieval date | Access status | Query / filters | Relevance | Artifact |
|---|---|---|---|---|---|---|---|
| GTEx | portal.gtexportal.org (median gene TPM) | v8 | 2026-09-13 | **Accessed, succeeded** | 16 FA-pathway genes + RNF213 + ACTA2/PECAM1 across 54 tissues; artery vs. all-tissue percentile | High — arterial expression directly tests seed's "vascular" claim | `data/gtex_fa_genes_artery_expression.csv`, `data/gtex_artery_pivot_all_markers.csv`, `code/gtex_query.py`, `logs/gtex_query_log.json` |
| EBI GWAS Catalog | www.ebi.ac.uk/gwas REST API | live snapshot | 2026-09-13 | **Accessed, succeeded (negative for FA genes)** | diseaseTrait="Moyamoya disease"; 4 studies; screen 16 FA genes vs. reported loci | High — tests whether FA genetics contributes to moyamoya | `logs/gwas_catalog_moyamoya.json` |
| ClinicalTrials.gov | clinicaltrials.gov API v2 | live | 2026-09-13 | **Accessed, succeeded (negative)** | "Fanconi anemia moyamoya" (0), "...vasculopathy" (8, none relevant), "...cerebral arteriopathy" (1, non-FA) | High — documents trial/source absence | `logs/clinicaltrials_negative_search.json` |
| PubMed | eutils | live | 2026-09-13 | **Accessed** | FA+moyamoya, FA endothelial/oxidative/vascular, FANCC vascular, RNF213 moyamoya, radiation-induced moyamoya | High | 48 papers reviewed (see Evidence Base) |

**Analysis inventory (input → method → output):**

1. **GTEx arterial-expression analysis** — Input: GTEx v8 median TPM matrix. Method: `code/gtex_query.py` (Python/pandas) computing per-tissue percentile ranks for FA genes vs. RNF213 in aorta/coronary/tibial artery. Output: two CSVs + JSON log. Outcome: **succeeded**. Limitation: bulk healthy tissue, not diseased cerebral artery; expression ≠ functional requirement.
2. **GWAS Catalog moyamoya locus screen** — Input: GWAS Catalog REST responses for "Moyamoya disease." Method: parse author-reported genes; intersect with 16 canonical FA genes. Output: `gwas_catalog_moyamoya.json`. Outcome: **succeeded (zero FA hits)**. Limitation: author-reported gene fields; East-Asian-weighted cohorts; no FA patients in these GWAS.
3. **ClinicalTrials.gov absence check** — Input: three API v2 queries. Method: keyword search + manual relevance triage. Output: `clinicaltrials_negative_search.json`. Outcome: **succeeded (negative)**. Limitation: keyword-based; a trial could exist under different terms.

No FA-moyamoya patient-level omics, no vascular-tissue FA dataset, and no isogenic FA vascular model dataset were located; these are recorded as **data-level absences**, not analyzed. No silent fallback occurred — all three computational analyses executed and returned inspectable artifacts.

---

## Mechanistic Causal Chain

The hypothesis implies the following chain. Annotations indicate evidence strength.

```
[Biallelic FA gene loss (e.g., FANCC 322delG + R185X)]
        │  STRONG (genotypes documented, PMID 7746424)
        ▼
[Defective ICL repair / genomic instability in vascular lineage]
        │  INFERRED — never shown in EC/VSMC or their progenitors
        ▼
[TP53-dependent growth arrest + hyperactive TGF-β growth suppression]
        │  ESTABLISHED but ONLY in HSPCs/MSCs/embryos (PMIDs 27053300, 36441774, 37627314)
        │  MISSING STEP — no vascular-cell demonstration
        ▼
[Apoptosis / attrition of vascular smooth-muscle or endothelial progenitors]
        │  NO DIRECT EVIDENCE (the pivotal untested link)
        ▼
[Intrinsic, possibly congenital cerebral arteriopathy]
        │  WEAK — clinical assertion in case reports (PMIDs 7367089, 25719591)
        ▼
[Progressive ICA/circle-of-Willis stenosis + moyamoya collaterals]
        │  OBSERVED clinically (the phenotype), mechanism unproven
        ▼
[Clinical moyamoya: TIA, stroke, hemiplegia]
```

- **Strong links:** the terminal clinical phenotype (documented moyamoya) and the upstream genotype (FANCC alleles) are well characterized.
- **Established-but-mislocalized link:** the TP53/TGF-β progenitor-apoptosis program is robustly demonstrated — but exclusively in hematopoietic/embryonic contexts, not vascular tissue.
- **Missing causal steps:** every step connecting FA gene loss *in a vascular cell* to *arterial stenosis* is inferred. There is no vascular-tissue FA study, no isogenic FA endothelial/VSMC apoptosis assay, and no exclusion of RNF213 as the true driver.

---

## Limitations and Knowledge Gaps

**Central mechanistic gap.** The pivotal edge *FA-deficient vascular cell → apoptosis/attrition → arteriopathy* has **zero direct evidence**. What was checked: PubMed searches for FA endothelial/oxidative/vascular phenotypes returned no usable mechanistic result (F001, 2026-09-13). Resolution: isogenic FA-corrected vs. FA-deficient iPSC-derived endothelial cells and VSMCs with apoptosis/senescence and TGF-β-pathway readouts.

**RNF213 never excluded.** No FA-moyamoya patient has been genotyped for RNF213 (F003, F008). Because RNF213 explains the overwhelming majority of moyamoya genetics, an unexcluded RNF213 variant would parsimoniously account for the phenotype without invoking an FA arteriopathy. Resolution: RNF213 (esp. p.R4810K and rare LoF) sequencing in all reported/future FA-moyamoya cases.

**Subtype incompatibility.** Moyamoya is absent from VACTERL-H (F006, [PMID: 27028275](https://pubmed.ncbi.nlm.nih.gov/27028275/)), and FA structural anomalies track the ID complex while the documented FA-moyamoya genotype is upstream FANCC ([PMID: 35417938](https://pubmed.ncbi.nlm.nih.gov/35417938/)). This conflicts with the seed's framing of moyamoya as an FA developmental structural anomaly.

**Iatrogenic confounding.** Radiation-induced moyamoya is dose/age-dependent and established ([PMID: 36057476](https://pubmed.ncbi.nlm.nih.gov/36057476/), [PMID: 17357039](https://pubmed.ncbi.nlm.nih.gov/17357039/)). While several early cases predate irradiation/transplant (F002), the modern FA population is heavily HSCT-exposed, confounding any prevalence signal. Resolution: cohort stratification by irradiation exposure with MR wall-enhancement imaging ([PMID: 12034935](https://pubmed.ncbi.nlm.nih.gov/12034935/)).

**No denominator / no omics / no trials.** Only one prevalence estimate exists (~2/434, F001); no case-control study, no vascular-tissue omics, and no ClinicalTrials.gov study (F007, documented negative on 2026-09-13). No GenCC/ClinGen gene–disease validity assertion for FA genes ↔ moyamoya was located in the searches performed (label: **unverified** — GenCC/ClinGen were not directly queried this run).

**Expression data caveat.** GTEx (F004) shows FA genes are expressed but not artery-enriched; this neither supports nor refutes a functional requirement and is from healthy bulk tissue, not diseased cerebral artery.

---

## Alternative Models

| Alternative hypothesis | Relationship to seed | Rationale / evidence |
|---|---|---|
| **RNF213-driven vasculopathy** | **Competing (parallel/upstream)** | RNF213 is the dominant moyamoya gene; drives EC/VSMC dysfunction via JAK2/STAT3, HIF-1α/VEGF ([PMID: 40467938](https://pubmed.ncbi.nlm.nih.gov/40467938/), [PMID: 42193873](https://pubmed.ncbi.nlm.nih.gov/42193873/), [PMID: 42652131](https://pubmed.ncbi.nlm.nih.gov/42652131/)). An unexcluded RNF213 variant could explain FA-moyamoya without an FA arteriopathy. |
| **Radiation-induced moyamoya (RIMS)** | **Competing (iatrogenic, downstream of treatment)** | Well-established dose/age-dependent entity; potentially MR-distinguishable ([PMID: 36057476](https://pubmed.ncbi.nlm.nih.gov/36057476/), [PMID: 12034935](https://pubmed.ncbi.nlm.nih.gov/12034935/)). Confounds transplanted FA patients. |
| **Coincidental co-occurrence** | **Null alternative** | With ~2/434 prevalence and 6 cases in 44 years, chance co-occurrence of two conditions cannot be excluded. |
| **Hemorrhagic/hemodynamic pseudo-moyamoya** | **Alternative for specific cases** | Alavi 2024 ([PMID: 38510908](https://pubmed.ncbi.nlm.nih.gov/38510908/)) questions whether the pattern reflects recurrent bleeding around the carotid siphon rather than intrinsic arteriopathy. |
| **FA TP53/TGF-β vascular-progenitor apoptosis** | **The seed's own mechanism (needs vascular localization)** | Established in HSPCs/embryos ([PMID: 27053300](https://pubmed.ncbi.nlm.nih.gov/27053300/), [PMID: 36441774](https://pubmed.ncbi.nlm.nih.gov/36441774/)); would be the mechanistic engine *if* demonstrated in vascular cells. |

---

## Discriminating Tests (Proposed Follow-up Experiments)

1. **RNF213 genotyping of all FA-moyamoya patients (highest priority, lowest cost).** Sequence RNF213 (p.R4810K + rare LoF) plus a moyamoya panel in every reported/prospective FA-moyamoya case. *Expected result to support seed:* absence of causal RNF213/moyamoya-panel variants across multiple FA-moyamoya patients. *Result favoring alternative:* enriched RNF213 variants would reassign causation.

2. **Isogenic FA iPSC-derived vascular cell assays.** Differentiate FA-patient iPSCs (and CRISPR-corrected isogenic controls) into endothelial cells and VSMCs; assay apoptosis, senescence (β-gal), ROS, TGF-β/SMAD activity, angiogenic/tube-formation and phenotype-switching. *Expected result to support seed:* FA-deficient vascular cells show excess apoptosis/senescence and aberrant TGF-β signaling rescued by correction — supplying the missing causal step (F005).

3. **Cohort with exposure stratification + MR wall imaging.** In an FA registry (e.g., IFAR-scale), estimate moyamoya prevalence stratified by cranial irradiation/HSCT exposure and apply arterial-wall enhancement MR ([PMID: 12034935](https://pubmed.ncbi.nlm.nih.gov/12034935/)) to separate radiation arteritis from intrinsic arteriopathy.

4. **FA vascular-tissue / single-cell omics.** Where surgical STA/vessel specimens are available from FA-moyamoya patients, run bulk/single-cell RNA-seq versus RNF213-moyamoya and idiopathic-moyamoya controls, testing whether FA-pathway or TGF-β signatures are engaged in the vessel wall.

5. **Genotype–phenotype re-analysis in FA cohorts.** In the NCI/IFAR cohorts, test whether FANCC (or any complementation group) is over-represented among cerebrovascular events, and whether ID-complex vs. upstream-complex status predicts arteriopathy (addresses the F006 tension).

---

## Curation Leads (require curator verification)

**Status recommendation:** Retain **EMERGING**. Consider adding a subtype restriction note (documented cases are FANCC/upstream-complex) and explicit competing-mechanism edges.

**Candidate evidence references + snippets to verify:**
- [PMID: 7746424](https://pubmed.ncbi.nlm.nih.gov/7746424/): *"Either the 322delG or R185X mutation alone or in combination may predispose to primary, possibly congenital, vascular anomalies."* — supports genotype-specific congenital predisposition.
- [PMID: 7367089](https://pubmed.ncbi.nlm.nih.gov/7367089/): *"it is suggested that in this case the moyamoya might pertain to the array of congenital malformations associated with Fanconi's anemia."*
- [PMID: 27028275](https://pubmed.ncbi.nlm.nih.gov/27028275/): VACTERL-H feature list (moyamoya absent) — scope-limiting.
- [PMID: 35417938](https://pubmed.ncbi.nlm.nih.gov/35417938/): *"ID complex was associated with VACTERL-H."* — subtype tension.
- [PMID: 12034935](https://pubmed.ncbi.nlm.nih.gov/12034935/): *"Contrast enhancement of the arterial walls in patients with radiation-induced arteritis was significantly more prominent than in patients with moyamoya disease (P = .003)."* — imaging discriminator.
- [PMID: 27053300](https://pubmed.ncbi.nlm.nih.gov/27053300/): *"we identify transforming growth factor-β (TGF-β) pathway-mediated growth suppression as a cause of BMF in FA."* — plausibility, hematopoietic only.

**Candidate pathophysiology nodes/edges (leads):**
- Node: FA-deficient vascular smooth muscle / endothelial progenitor (proposed, unconfirmed).
- Edge (UNCONFIRMED): FA gene loss → TP53/TGF-β apoptosis → vascular-progenitor attrition → cerebral arteriopathy.
- Competing edge: RNF213 variant → EC/VSMC dysfunction (JAK2/STAT3, HIF-1α/VEGF) → moyamoya.
- Competing edge: cranial irradiation (HSCT conditioning) → radiation arteritis → moyamoya.

**Candidate ontology terms:** vascular smooth muscle cell (CL:0000359); endothelial cell (CL:0000115); endothelial progenitor cell; apoptotic process (GO:0006915); transforming growth factor beta receptor signaling pathway (GO:0007179); moyamoya disease (MONDO:0016820 — verify); Fanconi anemia (MONDO:0019391 — verify).

**Candidate knowledge_gaps / discussion prompts:**
- "FA→vascular apoptosis→arteriopathy edge has no direct evidence (checked PubMed 2026-09-13)."
- "RNF213 never genotyped in any FA-moyamoya case."
- "No ClinicalTrials.gov study on FA cerebral arteriopathy (API v2, 2026-09-13, n=0)."
- "No FA-pathway gene at any moyamoya GWAS locus (GWAS Catalog, 2026-09-13)."
- "GenCC/ClinGen FA↔moyamoya validity: unverified (not directly queried this run)."

**Artifact bundle** (`kb/hypotheses/Fanconi_Anemia/fa_moyamoya_vasculopathy/openscientist_artifacts`): contains `MANIFEST.yaml`, `code/gtex_query.py`, `data/gtex_fa_genes_artery_expression.csv`, `data/gtex_artery_pivot_all_markers.csv`, `logs/gtex_query_log.json`, `logs/gwas_catalog_moyamoya.json`, `logs/clinicaltrials_negative_search.json`. Large raw GTEx/GWAS downloads are referenced by external accession, not bundled.

---

## Evidence Base (selected literature)

- **Seed / clinical association:** [PMID: 25719591](https://pubmed.ncbi.nlm.nih.gov/25719591/), [7746424](https://pubmed.ncbi.nlm.nih.gov/7746424/), [7367089](https://pubmed.ncbi.nlm.nih.gov/7367089/), [9409403](https://pubmed.ncbi.nlm.nih.gov/9409403/), [38510908](https://pubmed.ncbi.nlm.nih.gov/38510908/).
- **FA malformation spectrum & genotype–phenotype:** [PMID: 27028275](https://pubmed.ncbi.nlm.nih.gov/27028275/), [35417938](https://pubmed.ncbi.nlm.nih.gov/35417938/).
- **FA progenitor-apoptosis / TGF-β:** [PMID: 27053300](https://pubmed.ncbi.nlm.nih.gov/27053300/), [36441774](https://pubmed.ncbi.nlm.nih.gov/36441774/), [37627314](https://pubmed.ncbi.nlm.nih.gov/37627314/), [29247345](https://pubmed.ncbi.nlm.nih.gov/29247345/), [40555815](https://pubmed.ncbi.nlm.nih.gov/40555815/).
- **RNF213 vascular biology:** [PMID: 40467938](https://pubmed.ncbi.nlm.nih.gov/40467938/), [42193873](https://pubmed.ncbi.nlm.nih.gov/42193873/), [42652131](https://pubmed.ncbi.nlm.nih.gov/42652131/), [28153617](https://pubmed.ncbi.nlm.nih.gov/28153617/), [24949311](https://pubmed.ncbi.nlm.nih.gov/24949311/), [26766444](https://pubmed.ncbi.nlm.nih.gov/26766444/).
- **Radiation-induced moyamoya (competing):** [PMID: 36057476](https://pubmed.ncbi.nlm.nih.gov/36057476/), [12034935](https://pubmed.ncbi.nlm.nih.gov/12034935/), [17357039](https://pubmed.ncbi.nlm.nih.gov/17357039/), [14512691](https://pubmed.ncbi.nlm.nih.gov/14512691/), [31805403](https://pubmed.ncbi.nlm.nih.gov/31805403/), [37354243](https://pubmed.ncbi.nlm.nih.gov/37354243/).
- **Other syndromic moyamoya (context):** [PMID: 19258733](https://pubmed.ncbi.nlm.nih.gov/19258733/) (Robinow), [34007395](https://pubmed.ncbi.nlm.nih.gov/34007395/) (Down), [20644152](https://pubmed.ncbi.nlm.nih.gov/20644152/) (hereditary multisystem), [35978939](https://pubmed.ncbi.nlm.nih.gov/35978939/) (α-thalassemia).

---

*Report generated 2026-09-13. All three computational analyses (GTEx v8, GWAS Catalog, ClinicalTrials.gov v2) completed with outcome = succeeded; no analysis silently fell back to literature. Verdict: weakly supported / unresolved — retain EMERGING.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist evidence matrix](openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_data_evidence_matrix.csv)
- [OpenScientist gtex artery pivot all markers](openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_data_gtex_artery_pivot_all_markers.csv)
- [OpenScientist gtex fa genes artery expression](openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_data_gtex_fa_genes_artery_expression.csv)
- [OpenScientist clinicaltrials negative search](openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_logs_clinicaltrials_negative_search.json)
- [OpenScientist gtex query log](openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_logs_gtex_query_log.json)
- [OpenScientist gwas catalog moyamoya](openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_logs_gwas_catalog_moyamoya.json)
- [OpenScientist preflight connectivity](openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_moyamoya_vasculopathy_openscientist_artifacts_logs_preflight_connectivity.json)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0016820` (1 mention) - the report calls it "verify"; MONDO calls it **Moyamoya disease**
- `MONDO:0019391` (1 mention) - the report calls it "verify"; MONDO calls it **Fanconi anemia**