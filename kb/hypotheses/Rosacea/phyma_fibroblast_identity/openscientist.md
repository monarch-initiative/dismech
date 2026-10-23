---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-06T18:05:57.490291'
end_time: '2026-09-06T18:50:42.850829'
duration_seconds: 2685.36
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Rosacea
  category: Complex
  hypothesis_group_id: phyma_fibroblast_identity
  hypothesis_label: Rhinophyma fibroblasts are the PTGDS-high pro-inflammatory population
    of papulopustular disease, not a scar-type myofibroblast
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: phyma_fibroblast_identity\nhypothesis_label:\
    \ Rhinophyma fibroblasts are the PTGDS-high pro-inflammatory population of papulopustular\n\
    \  disease, not a scar-type myofibroblast\nstatus: EMERGING\napplies_to_subtypes:\n\
    - Phymatous Rosacea\ndescription: 'Single-cell transcriptomics of papulopustular\
    \ rosacea identifies an expanded pro-inflammatory\n  fibroblast population, marked\
    \ by PTGDS, as the leading source of inflammatory and vasodilatory signals,\n\
    \  and fibroblast depletion or PTGDS knockdown blocks disease in mice. Rhinophyma,\
    \ the end-stage phymatous\n  lesion, is clinically fibrotic yet reverts toward\
    \ normal after surgical debulking, unlike hypertrophic\n  scar. The hypothesis\
    \ is that the phyma fibroblast is the same inflammation-driven state as the papulopustular\n\
    \  fibroblast, persisting rather than transitioning to a scar-type myofibroblast,\
    \ which would explain both\n  the reversibility and why the fibrotic remodeling\
    \ node feeds phymatous change. An exploratory comparison\n  of the rhinophyma\
    \ versus hypertrophic scar versus healthy skin single-cell atlas (ArrayExpress\
    \ E-MTAB-16629)\n  against the published papulopustular fibroblast markers asks\
    \ whether rhinophyma fibroblasts carry the\n  PTGDS pro-inflammatory signature\
    \ or the ACTA2/COL1A1 myofibroblast signature of scar. Downstream causal\n  edges\
    \ that belong to this hypothesis opt in via hypothesis_groups: [phyma_fibroblast_identity].'\n\
    evidence:\n- reference: PMID:39384741\n  reference_title: Single-cell transcriptomics\
    \ reveals aberrant skin-resident cell populations and identifies\n    fibroblasts\
    \ as a determinant in rosacea.\n  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n\
    \  snippet: The papulopustular rosacea is featured by expansion of pro-inflammatory\
    \ fibroblasts, Schwann,\n    endothelial and macrophage/dendritic cells.\n  explanation:\
    \ The papulopustular fibroblast population the phyma fibroblast is to be compared\
    \ against.\n- reference: PMID:39384741\n  reference_title: Single-cell transcriptomics\
    \ reveals aberrant skin-resident cell populations and identifies\n    fibroblasts\
    \ as a determinant in rosacea.\n  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n\
    \  snippet: Depletion of fibroblasts or knockdown of PTGDS, a gene specifically\
    \ upregulated in fibroblasts,\n    blocks rosacea development in mice.\n  explanation:\
    \ Establishes PTGDS as the marker and the fibroblast as causal in the inflammatory\
    \ subtype.\nnotes: 'Exploratory dataset run: arrayexpress:E-MTAB-16629 (released\
    \ 2026-02-18). The papulopustular single-cell\n  data of Chen et al. have no public\
    \ accession in the cached full text, so the comparison must use the\n  published\
    \ marker genes rather than a joint embedding.'"
  artifact_dir: kb/hypotheses/Rosacea/phyma_fibroblast_identity/openscientist_artifacts
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
citation_count: 11
term_validation:
  total_terms: 7
  verified: 7
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: CL:0000057
    reported_labels:
    - Candidate ontology terms:** fibroblast
    ontology_label: fibroblast
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
- filename: logs/dataset_access_log.md
  path: openscientist_artifacts/logs/dataset_access_log.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist dataset access log
- filename: logs/pubmed_search_log.md
  path: openscientist_artifacts/logs/pubmed_search_log.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pubmed search log
- filename: results/fibroblast_marker_table.csv
  path: openscientist_artifacts/results/fibroblast_marker_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist fibroblast marker table
- filename: results/lineage_composition.csv
  path: openscientist_artifacts/results/lineage_composition.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist lineage composition
- filename: results/rhinophyma_ptgds_robustness.md
  path: openscientist_artifacts/results/rhinophyma_ptgds_robustness.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist rhinophyma ptgds robustness
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Rosacea
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** phyma_fibroblast_identity
- **Hypothesis Label:** Rhinophyma fibroblasts are the PTGDS-high pro-inflammatory population of papulopustular disease, not a scar-type myofibroblast
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: phyma_fibroblast_identity
hypothesis_label: Rhinophyma fibroblasts are the PTGDS-high pro-inflammatory population of papulopustular
  disease, not a scar-type myofibroblast
status: EMERGING
applies_to_subtypes:
- Phymatous Rosacea
description: 'Single-cell transcriptomics of papulopustular rosacea identifies an expanded pro-inflammatory
  fibroblast population, marked by PTGDS, as the leading source of inflammatory and vasodilatory signals,
  and fibroblast depletion or PTGDS knockdown blocks disease in mice. Rhinophyma, the end-stage phymatous
  lesion, is clinically fibrotic yet reverts toward normal after surgical debulking, unlike hypertrophic
  scar. The hypothesis is that the phyma fibroblast is the same inflammation-driven state as the papulopustular
  fibroblast, persisting rather than transitioning to a scar-type myofibroblast, which would explain both
  the reversibility and why the fibrotic remodeling node feeds phymatous change. An exploratory comparison
  of the rhinophyma versus hypertrophic scar versus healthy skin single-cell atlas (ArrayExpress E-MTAB-16629)
  against the published papulopustular fibroblast markers asks whether rhinophyma fibroblasts carry the
  PTGDS pro-inflammatory signature or the ACTA2/COL1A1 myofibroblast signature of scar. Downstream causal
  edges that belong to this hypothesis opt in via hypothesis_groups: [phyma_fibroblast_identity].'
evidence:
- reference: PMID:39384741
  reference_title: Single-cell transcriptomics reveals aberrant skin-resident cell populations and identifies
    fibroblasts as a determinant in rosacea.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: The papulopustular rosacea is featured by expansion of pro-inflammatory fibroblasts, Schwann,
    endothelial and macrophage/dendritic cells.
  explanation: The papulopustular fibroblast population the phyma fibroblast is to be compared against.
- reference: PMID:39384741
  reference_title: Single-cell transcriptomics reveals aberrant skin-resident cell populations and identifies
    fibroblasts as a determinant in rosacea.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Depletion of fibroblasts or knockdown of PTGDS, a gene specifically upregulated in fibroblasts,
    blocks rosacea development in mice.
  explanation: Establishes PTGDS as the marker and the fibroblast as causal in the inflammatory subtype.
notes: 'Exploratory dataset run: arrayexpress:E-MTAB-16629 (released 2026-02-18). The papulopustular single-cell
  data of Chen et al. have no public accession in the cached full text, so the comparison must use the
  published marker genes rather than a joint embedding.'
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
result beneath `kb/hypotheses/Rosacea/phyma_fibroblast_identity/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.


## Output

# Hypothesis-Search Report — Rosacea / `phyma_fibroblast_identity`

**Hypothesis label:** Rhinophyma fibroblasts are the PTGDS-high pro-inflammatory population of papulopustular disease, not a scar-type myofibroblast.
**KB status:** EMERGING · **Applies to:** Phymatous Rosacea
**Search/analysis date:** 2026-09-06 · **Iterations:** 1–4 of 5

---

## 1. Executive Judgment

**Verdict: PARTIALLY SUPPORTED — the hypothesis is right in spirit but wrong on its named biomarker.**

The seed hypothesis bundles two separable claims:

- **(A) Specific/biomarker claim:** rhinophyma fibroblasts carry the **PTGDS-high** pro-inflammatory signature of papulopustular rosacea.
- **(B) Conceptual/identity claim:** the phyma fibroblast is an **inflammation-driven state**, *not* a persistent ACTA2/COL1A1 scar-type myofibroblast, which explains rhinophyma's post-surgical reversibility.

A direct, first-hand computational test against the dataset named in the hypothesis (**ArrayExpress E-MTAB-16629**, actually downloaded and analysed) yields:

- **Claim (A) is CONTRADICTED in this atlas.** PTGDS is *lowest* in rhinophyma fibroblasts (5.0% positive) and *highest* in healthy-skin fibroblasts (54.5%), with hypertrophic scar intermediate (22.7%). PTGDS here behaves as a **homeostatic** dermal-fibroblast marker (co-tracking CFD/APOD), not an inflammatory disease marker, and the little PTGDS in rhinophyma localizes to **endothelium**, not fibroblasts. There is no hidden PTGDS-high fibroblast subpopulation.
- **Claim (B) is QUALIFIEDLY SUPPORTED.** Rhinophyma fibroblasts (i) show ACTA2 activation (38.9%) yet (ii) **lack the POSTN/CTHRC1 myofibroblast-persistence program** that defines hypertrophic scar (POSTN 3.1% vs 46.4%; CTHRC1 8.0% vs 43.4%), and (iii) express **reticular/inflammatory chemokines above scar levels** (CCL19 3.1×, CXCL12 1.9×, CCL2 1.7× the scar fraction). So they are inflammatory-but-non-persistent — consistent with the hypothesis's "not a classical scar myofibroblast" and with reversibility.

**Most important caveats:** the referenced dataset has **one individual per condition** (pseudo-replication; no cross-donor statistics are possible), lineage was assigned by canonical-marker scoring rather than full integration, and — critically — the papulopustular reference (Chen et al., PMID 39384741) **has no public accession**, so the comparison used **published/proxy marker genes rather than a joint embedding**. PTGDS was therefore operationalized as a single gene plus a proxy inflammatory set, not Chen et al.'s exact pro-inflammatory-fibroblast signature. The verdict should be read as "the specific PTGDS-transfer claim fails in the only accessible dataset; the broader inflammatory-non-scar identity is plausible and partly supported, pending replication."

---

## 2. Evidence Matrix

| # | Citation | Type | Stance | Mechanistic claim tested | Key finding | Subtype/context | Confidence & limitations |
|---|----------|------|--------|--------------------------|-------------|-----------------|--------------------------|
| 1 | PMID:39384741 (Chen 2024) | Human clinical + model organism | **Supports** (seed basis) | PTGDS+ pro-inflammatory fibroblasts are causal in rosacea | Papulopustular rosacea shows expansion of pro-inflammatory fibroblasts; fibroblast depletion or PTGDS knockdown blocks murine rosacea | Papulopustular (erythematotelangiectatic/inflammatory) | High for papulopustular; does **not** cover phyma; no public scRNA accession |
| 2 | **E-MTAB-16629** reanalysis (this report, computational) | Computational (scRNA-seq) | **Refutes (A)** | Do rhinophyma fibroblasts carry the PTGDS signature? | PTGDS+ fibroblasts: Healthy 54.5% > HS 22.7% > **Rhinophyma 5.0%**; PTGDS is homeostatic here | Rhinophyma vs HS vs healthy | Moderate–low: n=1/condition, marker-based lineage, depth confounds |
| 3 | **E-MTAB-16629** robustness (this report) | Computational | **Refutes (A)** | Is there a hidden PTGDS-high fibroblast subset? | PTGDS in only 2.9% of rhinophyma cells; PTGDS-high cells are **endothelial**; stringent fibroblasts 4.0% PTGDS+/46.9% ACTA2+ | Rhinophyma | Moderate: clustering-free, single donor |
| 4 | **E-MTAB-16629** reanalysis (this report) | Computational | **Qualifies/supports (B)** | Scar-persistence program in phyma? | POSTN 3.1% vs 46.4% (HS); CTHRC1 8.0% vs 43.4% — rhinophyma lacks the scar-persistence program | Rhinophyma vs HS | Moderate: %positive robust to depth; single donor |
| 5 | **E-MTAB-16629** reanalysis (this report) | Computational | **Qualifies/supports (B)** | Is phyma fibroblast inflammatory? | CCL19 3.14×, CXCL12 1.88×, CCL2 1.71× higher than scar fibroblasts | Rhinophyma vs HS | Low–moderate: immune-rich sample → possible ambient-RNA spillover |
| 6 | PMID:25421393 (Crawford 2015) | In vitro | **Supports (B) mechanism** | POSTN drives myofibroblast persistence | Periostin induces proliferation/α-SMA/contraction & sustains HS myofibroblasts; knockdown lowers α-SMA | Hypertrophic scar | High in vitro; anchors why phyma (POSTN-low) is reversible |
| 7 | PMID:20531985 (Zhou 2010) | In vitro/human tissue | **Supports (B)** | POSTN marks scar not inflammation | Periostin over-expressed in keloid/HS but "largely absent from sites of inflammation" | Scar vs inflammatory dermatoses | Moderate–high |
| 8 | PMID:31066603 (Maeda 2019) | In vitro | Context (B) | IL4/IL13→POSTN→RhoA/ROCK→TGF-β1 loop | Th2 cytokines and TGF-β1 drive a self-reinforcing periostin loop in abnormal scar | Keloid/HS | High in vitro; identifies the persistence circuit phyma lacks |
| 9 | PMID:40478772 (Fang 2025) | In vitro + model organism | **Competing/qualifies** | Is PTGDS an inflammatory-not-scar discriminator? | PTGDS+ pro-inflammatory fibroblasts are themselves **profibrotic**; AT56 (PTGDS inhibitor) reduces fibrosis in SSc | Systemic sclerosis skin | High; undercuts the clean PTGDS = inflammatory-vs-scar dichotomy |
| 10 | PMID:24563692 (Two 2014) | Review (mechanism) | **Competing (upstream)** | KLK5→LL-37 innate axis drives rosacea | Elevated KLK5 → cathelicidin/LL-37 → inflammation, vasodilation, vascular proliferation | Rosacea (all subtypes) | Review-level; established upstream driver |
| 11 | PMID:22076323 (Meyer-Hoffert 2011) | Review | **Competing (upstream)** | Epidermal proteases in rosacea | KLK5-derived LL-37 fragments are proinflammatory/angiogenic; keratinocyte-origin | Rosacea | Review-level |
| 12 | PMID:42106045 (Wu 2026) | Model organism (mouse) | **Competing (upstream)** | LL-37 model, mast-cell/NF-κB | LL-37-induced rosacea-like dermatitis with mast-cell activation, Th1/Th17, NF-κB | Rosacea-like mouse | Moderate; supports keratinocyte/mast-cell axis, not fibroblast-primary |
| 13 | PMID:41898724 (Fouani 2026) | Review | Competing (upstream/parallel) | TRPV4–mast cell neuroimmune signaling | Direct TRPV4-dependent mast-cell activation in LL-37-driven rosacea | Rosacea neurogenic inflammation | Review-level |
| 14 | PMID:42423091 (Bayar Muluk 2026) | Review (clinical) | **Qualifies (B)** | Is phyma reversible by anti-inflammatory Rx? | Medical Rx (doxycycline/isotretinoin) helps only **early inflammatory Grade I**; fibrotic Grades II–IV need **surgery** | Rhinophyma staging | Review-level; implies late phyma is structural, not purely inflammatory |
| 15 | PMID:24206029 / 23197212 | Human clinical (case) | Context | Phyma histology | Rhinophyma = sebaceous hypertrophy + lymphoedema + fibrosis; phyma = end-stage rosacea | Phymatous | Descriptive |

---

## 3. Data and Tool Use

### 3.1 Datasets / sources

| Source | Accession / URI | Repo | Version/snapshot | Retrieved | Status | Relevance |
|--------|-----------------|------|------------------|-----------|--------|-----------|
| Rhinophyma vs HS vs healthy scRNA-seq | **E-MTAB-16629** (https://www.ebi.ac.uk/biostudies/studies/E-MTAB-16629) | ArrayExpress / EBI BioStudies | Released 2026-02-18 | 2026-09-06 | **Accessed & analysed** (API HTTP 200; 9 processed 10x files + SDRF/IDF downloaded) | Directly on-topic — the exact atlas named in the seed |
| Papulopustular rosacea scRNA-seq (Chen et al.) | none found | — | — | 2026-09-06 | **Could not be verified** — no public accession in cached full text | Would be the ideal comparator; absence forces proxy-marker comparison |
| PubMed | 14 queries (see `logs/pubmed_search_log.md`) | NCBI | live | 2026-09-06 | Accessed; some queries 0-hit or rate-limited (logged) | Relevant |

Exact E-MTAB-16629 subset used: **all three samples** — ROS (rhinophyma), HS-H (hypertrophic scar, chest, 22 y/o male, S6), Skin-H (healthy). Organism *Homo sapiens*; assay 10x 3′ v3; comparison = fibroblast marker profiles across the three conditions. **One individual per condition (no biological replicates).** File paths, byte sizes, and the resolved API response are logged in `openscientist_artifacts/logs/dataset_access_log.md`.

Databases **not** queried (declared, not checked): GenCC, ClinGen, GWAS Catalog, ClinicalTrials.gov, GEO for an independent rhinophyma cohort. These are logged as **unverified** in Knowledge Gaps, not as evidence of absence.

### 3.2 Analyses (input → method → output)

| ID | Outcome | Input | Method | Output artifact |
|----|---------|-------|--------|-----------------|
| `fibroblast_marker_comparison` | **succeeded** | E-MTAB-16629 (3 samples) | scanpy 1.12.1: QC (min_genes=200, mito<20%) → CP10k+log1p → lineage by marker score-argmax → fibroblast subset → per-gene mean & %positive + composite scores; seed=0 | `results/fibroblast_marker_table.csv`, `results/lineage_composition.csv` |
| `rhinophyma_ptgds_robustness` | **succeeded** | E-MTAB-16629 (ROS) | clustering-free: rank cells by PTGDS; lineage profile of PTGDS-high cells; stringent fibroblast gate | `results/rhinophyma_ptgds_robustness.md` |
| Leiden subclustering of ROS | **failed** | E-MTAB-16629 (ROS) | HVG→PCA→neighbors→leiden | none — exceeded 60 s executor limit; replaced by clustering-free test |
| `inflammatory_chemokine_comparison` | **succeeded** | E-MTAB-16629 | fibroblast %positive chemokines, Rhino vs HS | `results/fibroblast_marker_barplot.png` (local-only; see manifest) |
| Joint embedding with papulopustular data | **skipped** | — | not possible: no public Chen et al. accession | none |

Environment: `openscientist_artifacts/environment.txt` (python 3.12; scanpy 1.12.1; anndata 0.12.6; scipy 1.17.1; numpy 2.3.5; pandas 3.0.3; sklearn 1.8.0; seed 0). Executor constraints: 60 s wall-clock per call, no cross-call filesystem persistence, network via `requests` only — these forced per-sample processing and precluded full multi-sample integration and cell-level cross-condition statistics.

---

## 4. Mechanistic Causal Chain

**Seed-implied chain (phyma arm):**
Upstream rosacea trigger → keratinocyte/innate activation → pro-inflammatory fibroblast expansion (**PTGDS+**, per papulopustular data) → sustained inflammatory + vasodilatory signalling → *phyma* as a persisting inflammatory-fibroblast state (not scar) → surgically reversible.

**What the evidence supports vs infers:**

- **Upstream trigger → innate/keratinocyte activation:** STRONG (KLK5/LL-37/TLR2/mast-cell/TRPV4; PMIDs 24563692, 22076323, 42106045, 41898724). This is keratinocyte/immune-centred, **upstream of and largely independent from** the fibroblast-identity question.
- **Papulopustular pro-inflammatory fibroblast is causal & PTGDS-marked:** STRONG for papulopustular (PMID 39384741), but **stage- and subtype-specific**.
- **Same PTGDS+ state persists in phyma:** **NOT SUPPORTED** in E-MTAB-16629 (rows 2–3). This is the **broken link** in the seed chain.
- **Phyma ≠ scar myofibroblast:** SUPPORTED via a different molecular route — phyma is ACTA2+ but **POSTN/CTHRC1-negative** (rows 4, 6–7), so it lacks the self-reinforcing POSTN→RhoA/ROCK→TGF-β1 persistence loop (PMID 31066603).
- **Reversibility:** best explained by **absence of the POSTN persistence program** plus surgical removal of sebaceous/fibroplastic bulk (PMID 42423091), rather than by "inflammation that resolves." **Inferred**, not directly demonstrated longitudinally.

**Missing causal steps:** (i) a direct phyma↔papulopustular fibroblast lineage/state comparison in one embedding; (ii) demonstration that phyma fibroblasts are *derived from* the papulopustular pro-inflammatory state (no trajectory/longitudinal data); (iii) any perturbation showing PTGDS is functionally relevant *in phyma* (as opposed to papulopustular).

---

## 5. Knowledge Gaps

1. **PTGDS identity of phyma fibroblasts (conflicting evidence).** Scope: core claim (A). Checked: E-MTAB-16629 (accessed) → PTGDS-low in rhinophyma fibroblasts; Chen et al. → PTGDS-high in papulopustular (no accession to re-test). Why it matters: the seed's biomarker fails to transfer in the only accessible atlas. Resolve: obtain/authorize the Chen papulopustular scRNA-seq and co-embed with E-MTAB-16629; add ≥3–5 rhinophyma donors; IHC/RNAscope for PTGDS in phyma fibroblasts vs endothelium.
2. **Single-donor pseudo-replication.** Scope: all computational claims. Checked: SDRF confirms n=1/condition. Why: no cross-donor statistics; batch/depth confounds. Resolve: multi-donor cohort with mixed-effects modelling.
3. **Proxy vs exact signature.** Scope: claims (A)/(B). Checked: no public Chen gene list. Why: PTGDS-only + proxy chemokines may misrepresent the true papulopustular signature. Resolve: apply the published exact signature once available.
4. **Ambient-RNA confound for chemokines.** Scope: claim 5. Checked: rhinophyma sample is immune/endothelial-rich. Why: fibroblast chemokine fractions may be inflated by spillover. Resolve: SoupX/CellBender decontamination; spatial validation.
5. **Reversibility is inferred, not observed.** Scope: claim (B) clinical arm. Checked: PMID 42423091 (staging), but no longitudinal omics before/after debulking. Resolve: paired pre/post-surgery biopsies with recurrence follow-up.
6. **Source/database absences (unverified, not "absent").** Scope: causal-graph completeness. Checked so far: PubMed only. **Not** queried: GenCC, ClinGen, GWAS Catalog, ClinicalTrials.gov, an independent GEO rhinophyma dataset. Resolve: run those queries with recorded version/date/filters before asserting absence.
7. **PTGDS directionality is context-dependent.** Scope: mechanism. Checked: PMID 40478772 shows PTGDS+ fibroblasts are profibrotic in SSc. Why: PTGDS cannot cleanly separate "inflammatory-reversible" from "fibrotic-persistent." Resolve: functional PTGDS perturbation in phyma-derived fibroblasts.

---

## 6. Alternative Models

| Model | Relation to seed | Summary | Evidence |
|-------|------------------|---------|----------|
| **KLK5/cathelicidin(LL-37)/TLR2 innate-immune axis** | **Upstream cause** (keratinocyte-centred) | Serine-protease-driven LL-37 generation initiates inflammation/vasodilation/angiogenesis; fibroblast changes are downstream | PMID 24563692, 22076323, 23871720 |
| **Mast cell / TRPV4 neurogenic inflammation** | **Parallel/upstream** | LL-37→mast-cell degranulation & TRPV4 neuroimmune signalling drive erythema/edema | PMID 42106045, 41898724 |
| **Demodex / microbiome persistence** | **Upstream cofactor** | Follicular Demodex sustains innate activation; ivermectin efficacy | PMID 42544818, 42541637 |
| **POSTN-negative activated-fibroblast model (this report)** | **Refinement of seed claim B** | Phyma fibroblast = ACTA2+, chemokine-high, **POSTN/CTHRC1-low** → inflammatory, non-persistent, surgically reversible; PTGDS is *not* its marker | Rows 4–7 |
| **Sebaceous-hyperplasia + lymphoedema/fibroplasia (structural)** | **Downstream/parallel** | Late phyma bulk is sebaceous + fibrotic tissue requiring surgery, not anti-inflammatory reversal | PMID 42423091, 24206029 |
| **PTGDS+ profibrotic-fibroblast model** | **Competes with seed's dichotomy** | PTGDS+ pro-inflammatory fibroblasts can *drive* fibrosis (SSc), so PTGDS ≠ "inflammatory not scar" | PMID 40478772 |

---

## 7. Discriminating Tests

1. **Joint scRNA-seq embedding, phyma vs papulopustular vs HS vs healthy** (≥5 donors each). Stratify by rosacea subtype/phyma grade. *Expected if seed true:* phyma fibroblasts co-cluster with papulopustular PTGDS+ fibroblasts. *Expected from this report:* phyma fibroblasts form a PTGDS-low, POSTN-low, chemokine-high cluster distinct from both papulopustular and scar.
2. **Spatial/IHC of PTGDS in phyma** (RNAscope PTGDS + DCN/PDGFRA fibroblast vs PECAM1 endothelial). *Expected from this report:* PTGDS predominantly endothelial, not fibroblast.
3. **POSTN/CTHRC1 vs chemokine staining across phyma grades I–IV.** *Expected:* POSTN stays low across grades (reversibility correlate); chemokines high in early/inflammatory phyma.
4. **Paired pre/post-debulking biopsies with 12-month recurrence follow-up + bulk RNA-seq.** *Expected:* low baseline POSTN predicts non-recurrence; contrast with HS.
5. **Functional PTGDS perturbation (AT56 or knockdown) in phyma-derived fibroblasts.** *Expected if seed true:* PTGDS inhibition reduces inflammatory output of phyma fibroblasts (as in papulopustular mice / SSc). If phyma fibroblasts are PTGDS-low, minimal effect — discriminating.

---

## 8. Curation Leads (require curator verification)

- **Status:** consider **EMERGING → CONTESTED/PARTIALLY-SUPPORTED** for claim (A) (PTGDS-high phyma fibroblast) based on the E-MTAB-16629 reanalysis; retain EMERGING for claim (B) (non-scar-myofibroblast identity).
- **Subtype restriction:** the PTGDS+ pro-inflammatory fibroblast is evidenced for **papulopustular** rosacea (PMID 39384741); do **not** extend the PTGDS marker to phymatous without direct phyma evidence.
- **Candidate nodes/edges:**
  - `Rhinophyma fibroblast` —is_a→ `activated fibroblast (ACTA2+, POSTN−/CTHRC1−)` (computational lead).
  - `PTGDS` —marker_of→ `homeostatic/quiescent dermal fibroblast` **and** `dermal endothelial cell` in phyma (computational lead; contradicts PTGDS→phyma-fibroblast edge).
  - `POSTN/CTHRC1 persistence loop` —distinguishes→ `hypertrophic scar` from `rhinophyma` (PMID 25421393, 20531985, 31066603).
  - `KLK5/LL-37 axis` —upstream_of→ rosacea inflammation (PMID 24563692).
- **Candidate ontology terms:** fibroblast (CL:0000057), myofibroblast (CL:0000186), dermal fibroblast (CL:0002620), endothelial cell (CL:0000115); processes: chronic inflammatory response (GO:0002544), extracellular matrix organization (GO:0030198), myofibroblast differentiation (GO:0036446).
- **Candidate evidence snippets to verify:**
  - PMID 25421393: "Hypertrophic scarring is characterized by the excessive development and persistence of myofibroblasts."
  - PMID 20531985: "over-expressed in keloid and hypertrophic scars, atopic dermatitis, but is largely absent from sites of inflammation…"
  - PMID 40478772: "Prostaglandin D2 synthase (PTGDS) … enriched expression in pro-inflammatory fibroblasts associated with skin fibrosis."
  - PMID 42423091: "Medical therapy, including doxycycline and isotretinoin, is primarily beneficial in early inflammatory disease (Clark Grade I). Established fibrotic rhinophyma (Grades II-IV) generally requires surgical intervention."
- **Candidate knowledge_gaps prompts:** add gaps #1 (PTGDS non-transfer conflict), #5 (reversibility not longitudinally shown), #6 (GenCC/ClinGen/GWAS/trials unverified), #7 (PTGDS context-dependent directionality).

---

## 9. Limitations & Future Directions

Primary limitation is the **single donor per condition** in the only accessible dataset and the **absence of a public papulopustular scRNA-seq accession**, which together prevent a definitive joint test and any cross-donor statistics. All computational claims are **exploratory and descriptive**. The strongest next step is a **multi-donor joint embedding of phyma, papulopustular, scar, and healthy skin**, paired with **PTGDS spatial validation** and **pre/post-surgery longitudinal sampling**. The report never silently substituted literature for the failed/limited analyses: the Leiden step is reported as failed, the joint embedding as skipped (no accession), and un-queried databases as unverified.

*Artifact bundle:* `kb/hypotheses/Rosacea/phyma_fibroblast_identity/openscientist_artifacts/` (MANIFEST.yaml, code, derived tables, robustness note, search & access logs; figure noted local-only).


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist dataset access log](openscientist_artifacts/logs/dataset_access_log.md)
- [OpenScientist pubmed search log](openscientist_artifacts/logs/pubmed_search_log.md)
- [OpenScientist fibroblast marker table](openscientist_artifacts/results/fibroblast_marker_table.csv)
- [OpenScientist lineage composition](openscientist_artifacts/results/lineage_composition.csv)
- [OpenScientist rhinophyma ptgds robustness](openscientist_artifacts/results/rhinophyma_ptgds_robustness.md)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0000057` (1 mention) - the report calls it "Candidate ontology terms:** fibroblast"; CL calls it **fibroblast**

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 1 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:24206029` (1 mention) - Rhinophyma--a patient case study.
  - shared terms: rhinophyma

Weighed against this report's own most characteristic terms: `fibroblast`, `ptgd`, `papulopustular`, `phyma`, `scar`, `rhinophyma`, `seed`, `rosacea`, `e-mtab-16629`, `claim`, `inflammatory`, `pro-inflammatory`, `marker`, `accession`, `ptgds-high`, `public`, `postn`, `computational`, `myofibroblast`, `chen`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.
