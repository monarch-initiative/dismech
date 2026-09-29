---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-13T19:41:04.531480'
end_time: '2026-09-13T20:12:07.100343'
duration_seconds: 1862.57
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Fanconi_Anemia
  category: Genetic
  hypothesis_group_id: fa_intrinsic_nk_and_b_lymphoid_defect
  hypothesis_label: Intrinsic NK and B Lymphoid Defect Independent of Marrow Failure
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: fa_intrinsic_nk_and_b_lymphoid_defect\nhypothesis_label:\
    \ Intrinsic NK and B Lymphoid Defect Independent of Marrow Failure\nstatus: EMERGING\n\
    description: Fanconi anemia carries a quantitative and functional NK-cell and\
    \ B-cell defect that is intrinsic\n  to FA-deficient lymphoid progenitors or to\
    \ their cytotoxic machinery, present before and independently\n  of marrow failure\
    \ and transplantation, rather than a simple consequence of pancytopenia. Candidate\
    \ mechanisms\n  are p53-mediated loss of lymphoid progenitors, defective perforin\
    \ and granzyme loading, and impaired\n  proliferative response to activation.\n\
    evidence:\n- reference: PMID:21542827\n  reference_title: Impaired immune function\
    \ in children with Fanconi anaemia.\n  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n\
    \  snippet: Absolute numbers of B cells and natural killer (NK) cells were reduced\
    \ compared to controls\n  explanation: Seed reference; reduced NK and B cell numbers\
    \ in children with FA."
  artifact_dir: kb/hypotheses/Fanconi_Anemia/fa_intrinsic_nk_and_b_lymphoid_defect/openscientist_artifacts
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
citation_count: 6
term_validation:
  total_terms: 18
  verified: 16
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 1
  labels_variant: 6
  unresolvable_prefixes:
  - OMIM
  - NCBIGene
  needs_review: true
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
- filename: kb_hypotheses_Fanconi_Anemia_fa_intrinsic_nk_and_b_lymphoid_defect_openscientist_artifacts_data_evidence_matrix.csv
  path: openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_intrinsic_nk_and_b_lymphoid_defect_openscientist_artifacts_data_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: kb_hypotheses_Fanconi_Anemia_fa_intrinsic_nk_and_b_lymphoid_defect_openscientist_artifacts_logs_database_source_checks.md
  path: openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_intrinsic_nk_and_b_lymphoid_defect_openscientist_artifacts_logs_database_source_checks.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist database source checks
- filename: kb_hypotheses_Fanconi_Anemia_fa_intrinsic_nk_and_b_lymphoid_defect_openscientist_artifacts_logs_pubmed_search_log.md
  path: openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_intrinsic_nk_and_b_lymphoid_defect_openscientist_artifacts_logs_pubmed_search_log.md
  media_type: text/markdown
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
- **Disease Name:** Fanconi_Anemia
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** fa_intrinsic_nk_and_b_lymphoid_defect
- **Hypothesis Label:** Intrinsic NK and B Lymphoid Defect Independent of Marrow Failure
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: fa_intrinsic_nk_and_b_lymphoid_defect
hypothesis_label: Intrinsic NK and B Lymphoid Defect Independent of Marrow Failure
status: EMERGING
description: Fanconi anemia carries a quantitative and functional NK-cell and B-cell defect that is intrinsic
  to FA-deficient lymphoid progenitors or to their cytotoxic machinery, present before and independently
  of marrow failure and transplantation, rather than a simple consequence of pancytopenia. Candidate mechanisms
  are p53-mediated loss of lymphoid progenitors, defective perforin and granzyme loading, and impaired
  proliferative response to activation.
evidence:
- reference: PMID:21542827
  reference_title: Impaired immune function in children with Fanconi anaemia.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Absolute numbers of B cells and natural killer (NK) cells were reduced compared to controls
  explanation: Seed reference; reduced NK and B cell numbers in children with FA.
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
result beneath `kb/hypotheses/Fanconi_Anemia/fa_intrinsic_nk_and_b_lymphoid_defect/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.


## Output

# Hypothesis-Search Report — Fanconi Anemia
## `fa_intrinsic_nk_and_b_lymphoid_defect`: Intrinsic NK and B Lymphoid Defect Independent of Marrow Failure

**Disease:** Fanconi Anemia (Genetic) · **KB status:** EMERGING · **Search date:** 2026-09-13 · **Iteration:** 5 of 5

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED (trending toward supported for its core claims).**

The hypothesis has two separable claims, which the literature supports unequally:

1. **A quantitative NK-cell and B-cell reduction plus an intrinsic NK cytotoxic-machinery defect exists in FA — SUPPORTED.** Reduced NK and B cell numbers, reduced NK cytotoxicity, and reduced NK perforin/granzyme content are reproduced across at least four independent human cohorts (Myers 2011 seed, Myers 2017, Justo 2014, Shabrish 2019) and a review synthesis (Hashemi 2021). The direction is unanimous in every cohort that measured each parameter (directional concordance check; see *Data and Tool Use*). A defined molecular lesion — defective NK **degranulation** (Shabrish 2019) and reduced perforin/granzyme loading (Myers 2011) — argues for an intrinsic cytotoxic-apparatus defect rather than a pure numeric consequence of pancytopenia.

2. **"Independent of marrow failure and transplantation" — SUPPORTED for transplantation, PARTIALLY supported for marrow failure.** The Myers 2017 cohort explicitly excluded transplanted and malignant patients yet still showed the NK/B defect, cleanly establishing **transplant-independence**. An *Fancc-/-* mouse — a model with largely normal steady-state hematopoiesis — has a **cell-intrinsic** B-cell class-switch/antibody-secreting-cell defect (Sertorio 2016), the strongest evidence that at least the B-lineage functional defect is marrow-failure-independent. However, the "independent of pancytopenia" claim for **cell numbers** is only partially supported: a general p53/p21 hyperactivation eliminates HSPCs across all lineages before overt BMF (Ceccaldi 2012), and NKG2D-ligand–driven NK cytotoxicity actively clears FA HSPCs (Casado 2022) — either of which could reduce lymphoid output without a lymphoid-specific lesion.

**Most important caveats.** (a) The "impaired proliferative response to activation" sub-mechanism is **inconsistently supported**: Giri 2015 found normal lymphoproliferation and normal cytokines in FA, and Myers 2011 found normal PHA/candida responses (only tetanus recall and CTL function reduced). (b) Some immune abnormalities (low Ig, low CD4, low total lymphocytes) are **adult- and severe-BMF-associated** (Giri 2015), i.e., partly stage-dependent. (c) There is a **mechanistic tension**: mature peripheral FA NK cells are hypofunctional/hypocytotoxic, yet the NKG2D axis posits NK cells that are cytotoxic enough to destroy HSPCs — reconciling these requires compartment- and stage-resolved data that does not yet exist. (d) The candidate "p53-mediated loss of *lymphoid* progenitors" step is **inferred**, not directly demonstrated; the p53 evidence is pan-hematopoietic. (e) A third, well-documented competing axis — cell-extrinsic TNF-α/IL-1β myelosuppression from FA monocytes/macrophages (Briot 2008; Vanderwerf 2009; Garbati 2013; Matsushita 2011) — offers a parsimonious non-lymphoid explanation for reduced counts, though it does not explain the NK cytotoxic-machinery lesion. (f) **Testability caveat:** a live source check (2026-09-13) found **no FA NK-cell omics in GEO** and no interventional trial isolating the lymphoid defect, so the hypothesis currently rests on immunophenotyping cohorts plus one mouse B-cell model rather than orthogonal molecular data.

---

## Evidence Matrix

| Citation | Type | Stance | Mechanistic claim tested | Key finding | Subtype/context | Confidence & limitations |
|---|---|---|---|---|---|---|
| **PMID 21542827** (Myers 2011, *seed*) | Human clinical | **Support** | Intrinsic NK cytotoxic machinery + B numeric defect | ↓B (P=0.048), ↓NK (P=0.0002); ↓NK perforin (P<1e-5), ↓granzyme (P=0.0057); ↓NK cytotoxicity (P<0.001); ↓CTL (P<1e-4); ↓tetanus proliferation (P=0.008) but normal PHA/candida | 10 children, FA | Small n; cross-sectional; no genotype stratification |
| **PMID 28557197** (Myers 2017) | Human clinical | **Support** (key) | Defect present without transplant/malignancy | ↓total B (P<0.001), ↓memory B (P<0.001), ↓IgM (P<0.001), ↓NK (P<0.001), ↓NK cytotoxicity (P<0.001) | 29 FA, **no BMT, no malignancy** | Establishes transplant-independence; still cannot separate from BMF severity |
| **PMID 30949167** (Shabrish 2019) | Human clinical | **Support** (mechanism) | Intrinsic NK degranulation lesion | First report of defective NK **degranulation** → impaired cytotoxicity; links to hyperinflammation/HLH | FA patients | Case-level; proposes FA genes as familial-HLH cause |
| **PMID 24240977** (Justo 2014) | Human clinical | **Support** | Quantitative + NK differentiation defect | ↓CD8+ T and ↓CD56dim CD16+ NK; NK subset imbalance; impaired NK differentiation | 42 FA (large) | Correlational with hematologic status |
| **PMID 26895835** (Sertorio 2016) | Model organism (mouse) | **Support** (strong, intrinsic) | Cell-intrinsic B-cell functional defect | *Fancc-/-* B cells: defective IgG2a switch, impaired ASC differentiation; hyperactive Wnt/β-catenin represses Blimp1 | *Fancc-/-* mouse (no overt BMF) | Single gene (FANCC); B-function not NK; germline model |
| **PMID 34348001** (Hashemi 2021) | Review | **Support** (orientation) | NK dysfunction in cytotoxicity + cytokines | FA NK cells dysfunctional in cytotoxicity and cytokine production; molecular basis undefined | FA (review) | Review-level; no new data |
| **PMID 25963299** (Giri 2015) | Human clinical | **Qualify** | Independence from BMF/age; proliferative response | Children FA normal Ig; both ages ↓B/↓NK (P<0.01); **lymphoproliferation & TNF-α/IFN-γ normal**; adult ↓Ig/↓CD4/↓lymphocytes; only severe BMF ↑G-CSF/Flt3L | 118 IBMFS vs 202 relatives, BMF-adjusted | Best-controlled cohort; weakens proliferation sub-claim; shows age/BMF dependence |
| **PMID 22683204** (Ceccaldi 2012) | Human clinical + models | **Competing/parallel** | Pan-HSPC attrition upstream of lineage defects | Profound HSPC defect **before** clinical BMF; p53 hyperactivation → p21 G0/G1 arrest; p53 knockdown rescues HSPCs | FA patients/models | Not lymphoid-specific; supports "p53" step but predicts pan-lineage loss |
| **PMID 35671096** (Casado 2022) | Model organism + human cells | **Competing** | NKG2D-L–mediated immune clearance of HSPCs | FA CD34+ upregulate NKG2D-Ls (inverse to %CD34+); blocking NKG2D–NKG2D-L restores clonogenicity, ameliorates anemia in FA mouse | FA HSPC/BM | Implies NK are cytotoxic vs HSPCs — tension with hypofunctional peripheral NK |
| **PMID 35912855** (Dulmovits 2022) | Review/commentary | **Competing** (orientation) | Immune-mediated BMF paradigm in FA | Frames NK/NKG2D-dependent HSPC clearance as driver of FA BMF | FA (commentary on Casado) | Commentary; interpretive |
| **PMID 27720904** (Yoon 2016) | Model organism (mouse) | **Qualify** | p53-dependence of HSPC deficit | Fetal *Fancd2* HSPC replicative-fitness deficit is **p53-INDEPENDENT** | Fetal murine Fancd2 | Qualifies the p53 candidate step; developmental window |
| **PMID 18055871** (Briot 2008) | In vitro | **Competing** | Cell-extrinsic myelosuppression | FANC loss aberrantly activates NF-κB/MAPK → MMP-7-dependent TNF-α oversecretion; MAPK inhibition normalizes it | FA cells | Inflammatory-microenvironment BMF axis (not lymphoid-specific) |
| **PMID 19850743** (Vanderwerf 2009) | In vitro | **Competing** | Repair-independent FANCC immune function | FANCC suppresses TLR8-driven TNF-α in phagocytes, **independent of crosslink repair** | FA-C monocytes/macrophages | Establishes a non-repair immune role for an FA gene |
| **PMID 24046015** (Garbati 2013) | In vitro | **Competing** | Cytokine suppression of progenitors | FANCA/FANCC macrophages overproduce TNF-α + IL-1β (p38-dependent); IL-1β suppresses *Fancc-/-* progenitor expansion | FA macrophages/BM | Myeloid-driven progenitor suppression |
| **PMID 21912593** (Matsushita 2011) | In vitro | **Competing** (mechanism) | FANCD2 represses TNF-α | FANCD2 binds NF-κB element in TNF-α promoter and represses it (monoUb-dependent) | FA cells | Molecular basis of TNF-α overproduction |
| **PMID 23889587** (Matsui 2013) | Human clinical | **Qualify** | Marrow vs blood lymphocyte compartment | In FA **bone marrow**, T/B lymphocyte proportions similar to controls; **no** T-cell TNF-α/IFN-γ overproduction; monocytes hypersensitive to low-dose LPS | FA BM mononuclear cells | Peripheral lymphopenia may not mirror marrow; qualifies both models |
| **GEO + ClinicalTrials.gov** (2026-09-13) | Computational (source check) | **Qualify** (data absence) | Testability with public data | 0 FA NK-cell GEO datasets; no FA-specific B/NK immune omics; 50 CT.gov trials all HSCT/GVHD context | Source-level | Verified absence; hypothesis not omics-testable today |

---

## Data and Tool Use

**No patient-level or omics dataset was provided or accessed.** The core report is primary-literature synthesis; one small computational analysis was run on abstract-derived data. Nothing was silently substituted — tool failures are logged.

| Source / tool | Accession/URI | Access status | Query / use | Relevant? |
|---|---|---|---|---|
| PubMed (NCBI E-utils via MCP) | eutils.ncbi.nlm.nih.gov | **Accessed** (13 queries across it.1–2; 2 failed) | See `logs/pubmed_search_log.md` for exact queries, dates, failures | Yes |
| **GEO DataSets** (NCBI eutils, db=gds) | eutils.ncbi.nlm.nih.gov | **Accessed, HTTP 200** (it.2) | 4 queries; see `logs/database_source_checks.md`. FA+NK = **0 datasets**; FA+Bcell = 1 (false match GSE35698); 5 FANC datasets all non-immune | **Verified absence** of FA NK/B immune omics |
| **ClinicalTrials.gov** API v2 | clinicaltrials.gov/api/v2 | **Accessed, HTTP 200** (it.2) | cond=Fanconi Anemia + immune terms; totalCount=**50**, all HSCT/GVHD; none targets intrinsic lymphoid defect | Relevant; no on-target trial |
| **HPO / OMIM annotation** (disease-level) | ontology.jax.org/api · OMIM:227650 / MONDO:0009215 | **Accessed, HTTP 200** (it.3) | Disease-level phenotype set = only Pancytopenia/Anemia/↓Neutrophils/Thrombocytopenia; **no immune category or NK/B/Ig/immunodeficiency term** | **Verified ontology-level absence** of the immune phenotype |
| **HPO annotation** (gene-level) | ontology.jax.org/api · NCBIGene:2175/2176/2177/2189/2187 (FANCA/C/D2/G/B) | **Accessed, HTTP 200** (it.4) | Exact-ID check for HP:0040218, HP:0010976, HP:0002721, HP:0004313, HP:0002850, HP:0001888 → **none present for any FA gene**; only HP:0001875 (↓neutrophils) + HP:0000010 (recurrent UTI) | **Verified gene-level absence** — corroborates disease-level check |
| **Monarch Initiative** API v3 (federated) | api-v3.monarchinitiative.org · MONDO:0009215 | **Accessed, HTTP 200** (it.5) | DiseaseToPhenotypicFeatureAssociation; total=34 phenotypes; immune filter → only HP:0001875 (↓neutrophils); **no NK/B/immunodeficiency/Ig term** | **Verified absence (3rd independent layer)** |
| Directed FA-mouse lymphoid-dev query | — | **Searched, 0 results** | "Fanconi anemia mouse model lymphocyte development B cell intrinsic defect…" | Negative (unverified absence — single query) |
| GenCC | search.thegencc.org/api/v1/submissions | **Attempted, HTTP 404** (it.5) | No public REST/JSON API at that path (SPA HTML); not machine-queryable | Outstanding, NOT claimed absent |
| ClinGen / ClinVar / ArrayExpress / EGA | — | **Not checked** | — | Outstanding, not negative |

**Analysis inventory (input → method → output):**

| Analysis | Input | Method | Output | Outcome |
|---|---|---|---|---|
| Reproducibility tally | `data/evidence_matrix.csv` (directions only) | one-sided exact binomial sign test vs p=0.5 (scipy 1.17.1) | `logs/reproducibility_tally.txt` | **Partial** — under-powered; direction unanimous |
| GEO source check | NCBI GEO db=gds | 4 esearch queries + esummary triage | `logs/database_source_checks.md` | **Succeeded** — verified 0 FA NK datasets |
| ClinicalTrials.gov check | CT.gov API v2 | REST query + title triage | `logs/database_source_checks.md` | **Succeeded** — 50 hits, all transplant context |
| HPO annotation check | ontology.jax.org API | disease + gene-level fetch, exact-ID filter | `logs/database_source_checks.md` | **Succeeded** — no immune HPO terms for FA (disease + gene) |
| Monarch federated check | api-v3.monarchinitiative.org | disease→phenotype associations + keyword filter | `logs/database_source_checks.md` | **Succeeded** — 34 phenotypes, no NK/B/immunodeficiency term |
| GenCC API check | search.thegencc.org | REST query attempt | `logs/database_source_checks.md` | **Failed** (HTTP 404, no public API) — outstanding, not absent |

The tally found that **every human cohort that measured a parameter reported it reduced** (NK count 4/4, NK cytotoxicity 3/3, B count 3/3 of *measuring* cohorts). Sign-test p-values (0.19–0.50) are **not significant and under-powered**; they are reported only as a direction-concordance indicator, not inferential evidence. A sandbox None/NaN coercion inflated the printed denominator (prints /5; corrected /4,/3,/3) — documented in the log. **No figure** was produced (the execute_code sandbox saves plots outside the bundle path). Provider artifact bundle: `kb/hypotheses/Fanconi_Anemia/fa_intrinsic_nk_and_b_lymphoid_defect/openscientist_artifacts/` with `MANIFEST.yaml` (checksums, replay command), `data/`, `code/`, `logs/`, `env/`.

---

## Mechanistic Causal Chain (as implied by the hypothesis)

```
FA gene biallelic loss (FANCA/C/D2/…)  →  defective ICL repair / replication stress
        │                                                   │
        │ [STRONG in HSPC broadly]                          │ [STRONG: DNA damage stress]
        ▼                                                   ▼
  p53/p21 hyperactivation, G0/G1 arrest            NKG2D-ligand upregulation on stressed cells
  → HSPC attrition (Ceccaldi 2012)                 → NK/CD8 clearance of HSPCs (Casado 2022)
        │  [INFERRED lymphoid-specific step]                │  [COMPETING: destroys, not spares, HSPCs]
        ▼                                                   
  Reduced NK + B progenitor output ───────────────► Reduced peripheral NK & B numbers  [STRONG, replicated]
        │
        │ [STRONG for NK: intrinsic machinery lesion]
        ▼
  Defective perforin/granzyme loading + degranulation (Myers 2011; Shabrish 2019)
        │
        ▼
  ↓ NK cytotoxicity; B: ↓class switch/ASC via Wnt–Blimp1 (Sertorio 2016)  [STRONG in mouse]
        │
        ▼
  Clinical: impaired immune surveillance, infection risk, hyperinflammation/HLH,
            possibly permissive to malignancy  [INFERRED clinical linkage]
```

- **Strong links:** upstream DNA-damage stress → NK/B numeric reduction (replicated human); intrinsic NK perforin/granzyme/degranulation lesion; intrinsic B-cell class-switch defect (mouse).
- **Inferred links:** the *lymphoid-specific* p53 progenitor-loss step (only pan-HSPC data exist); progenitor loss → mature-cell reduction (plausible, not directly traced in lymphoid compartment).
- **Missing steps:** direct evidence that FA lymphoid progenitors (CLP, pro-B, NK precursors) are selectively depleted vs. simply reduced in proportion to global HSPC loss; direct link from the cytotoxic-machinery lesion to a specific FA gene/molecular pathway (perforin/granzyme regulation mechanism is "yet to be determined," Hashemi 2021).

---

## Knowledge Gaps

1. **Lymphoid-progenitor-specific loss (weakly supported causal step).** *Scope:* Is the NK/B reduction lymphoid-intrinsic or a downstream share of pan-HSPC p53 attrition? *Why it matters:* distinguishes the seed hypothesis from Ceccaldi's parallel model. *Checked:* directed FA-mouse lymphoid-development query returned 0 results (unverified absence). *Resolves with:* lineage-resolved progenitor quantification (CLP/pro-B/NK-precursor) in FA marrow and *Fanc* mice vs matched cytopenic non-FA controls.
2. **Molecular basis of the NK cytotoxic-machinery lesion (unknown mechanism).** *Scope:* Why perforin/granzyme content and degranulation are reduced. *Why it matters:* it is the strongest "intrinsic" pillar yet mechanistically unexplained (Hashemi 2021: "molecular bases … yet to be determined"). *Resolves with:* perforin/granzyme transcription + granule-trafficking assays in FA vs control NK cells, with genotype stratification.
3. **Reconciling hypofunctional peripheral NK with NKG2D-driven HSPC clearance (conflicting evidence).** *Scope:* Casado 2022 needs cytotoxic NK; patient NK are hypocytotoxic. *Resolves with:* compartment-resolved (BM vs blood) and stage-resolved NK functional profiling.
4. **Proliferative-response sub-claim (contradicted/qualified).** *Scope:* Giri 2015 normal lymphoproliferation vs Myers 2011 reduced tetanus recall/CTL. *Resolves with:* standardized antigen-specific vs mitogen proliferation panels across a genotyped cohort.
5. **Source-level absences (as of 2026-09-13, now partly VERIFIED).** *Checked:* GEO DataSets (db=gds) — `Fanconi anemia AND (natural killer OR "NK cell")` returned **0 datasets** (verified absence); the single FA+B-cell hit was an unrelated mouse Brca1/53BP1 study; five FANC-gene datasets are all non-immune. ClinicalTrials.gov v2 — 50 FA immune-context trials, **all HSCT/GVHD**, none targeting the intrinsic lymphoid defect. *Why it matters:* the hypothesis cannot currently be tested with public omics and has no dedicated interventional trial. Additionally, an **HPO/OMIM ontology check** (OMIM:227650 / MONDO:0009215, 2026-09-13) found the disease-phenotype annotation set limited to Pancytopenia/Anemia/↓Neutrophils/Thrombocytopenia with **no immune category or NK/B/Ig/immunodeficiency term** — a verified ontology-curation absence. A follow-up **gene-level HPO check** (FANCA/FANCC/FANCD2/FANCG/FANCB, 2026-09-13) corroborated this by exact-ID matching: none carries HP:0040218 (reduced NK count), HP:0010976 (B lymphocytopenia), HP:0002721 (immunodeficiency), HP:0004313/HP:0002850 (decreased antibody/IgM), or HP:0001888 (lymphopenia) — the only immune-adjacent terms are HP:0001875 (↓neutrophils) and HP:0000010 (recurrent UTI). A **third independent layer** — the **Monarch Initiative** federated aggregator (MONDO:0009215, 2026-09-13, HTTP 200, 34 phenotype associations) — again returned only HP:0001875 as immune-adjacent, confirming the absence across HPO disease-level, HPO gene-level, and a federated resource. A **GenCC** REST query was attempted but returned HTTP 404 (no public JSON API at that path); it is reported as *not machine-verified*, **not** as an absence. *Still outstanding (not claimed absent):* GenCC (via bulk submissions download), ClinGen, ClinVar, ArrayExpress, EGA controlled-access FA cohorts. *Resolves with:* generation/deposition of sorted FA NK and B transcriptomic/functional datasets vs matched cytopenic non-FA controls, and HPO annotation extension.
6. **Marrow vs peripheral-blood compartment discordance (conflicting evidence).** *Scope:* Matsui 2013 found normal T/B lymphocyte proportions in FA **marrow**, whereas peripheral-blood cohorts report reduced NK/B. *Why it matters:* determines whether the deficit is production (marrow) or peripheral maintenance/redistribution. *Resolves with:* paired marrow+blood immunophenotyping in the same FA patients.

---

## Alternative Models

| Model | Relation to seed hypothesis |
|---|---|
| **Pan-HSPC p53/p21 attrition** (Ceccaldi 2012) | **Upstream/parallel.** Reduced lymphoid numbers may be a downstream share of global progenitor loss, not a lymphoid-specific lesion. Supports the "p53" candidate step but broadens it beyond lymphoid. |
| **NKG2D-ligand immune-mediated HSPC clearance** (Casado 2022; Dulmovits 2022) | **Competing/alternative** for the *numeric* deficit and marrow failure itself; posits functionally active (not intrinsically defective) NK cells clearing HSPCs. |
| **Wnt/β-catenin–Blimp1 B-cell-intrinsic defect** (Sertorio 2016) | **Complementary mechanistic sub-model** — a concrete intrinsic pathway for the B-arm of the seed hypothesis. |
| **p53-independent replicative-fitness deficit** (Yoon 2016) | **Parallel/qualifying** — developmental HSPC fitness loss not requiring p53. |
| **BMF-secondary / age-progressive immune decline** (Giri 2015) | **Alternative** for the Ig/CD4/lymphocyte component; frames part of the phenotype as a consequence of disease progression rather than intrinsic. |
| **Inflammatory-microenvironment / TNF-α myelosuppression** (Briot 2008; Vanderwerf 2009; Garbati 2013; Matsushita 2011) | **Competing, cell-extrinsic** mechanism: FANC loss → TLR/p38-MAPK/NF-κB → TNF-α/IL-1β overproduction by monocytes/macrophages → HSPC suppression. Competes for the "reduced counts" component but does **not** explain the NK perforin/granzyme/degranulation lesion. Note Matsui 2013 found no T-cell cytokine overproduction in FA marrow. |
| **FANCC–CtBP1–Wnt/DKK1 axis** (GSE43330; converges with Sertorio 2016) | **Complementary** upstream link: FA proteins modulate Wnt-antagonist DKK1, dovetailing with hyperactive Wnt/β-catenin in *Fancc-/-* B cells — a candidate molecular thread for the B-arm. |

---

## Discriminating Tests

1. **Lineage-resolved progenitor census (seed vs Ceccaldi).** Sample: FA vs non-FA cytopenic pediatric marrow. Assay: flow/scRNA-seq of CLP, pro-B, NK-precursors normalized to total HSPC. *Expected if seed true:* disproportionate lymphoid-progenitor loss beyond global HSPC reduction. *If Ceccaldi:* proportional loss.
2. **Genetic epistasis on NK function (seed vs BMF-secondary).** Model: *Fanc-/-* vs *Fanc-/-;Trp53+/-* mice. Readout: NK perforin/granzyme, degranulation (CD107a), cytotoxicity. *Expected if intrinsic-machinery true:* p53 rescue restores HSPC numbers but **not** the perforin/granzyme/degranulation lesion.
3. **BM vs blood NK functional map (reconcile NKG2D tension).** Paired FA BM and peripheral NK: NKG2D expression, cytotoxicity vs K562 and vs autologous CD34+. *Expected:* BM NK retain NKG2D-driven activity while peripheral NK are hypofunctional — stage/compartment dissociation.
4. **Antigen-specific vs mitogen proliferation panel (resolve sub-claim).** Genotyped FA cohort: tetanus/candida recall vs PHA/anti-CD3-CD28. *Expected if seed true:* selective antigen-recall deficit with preserved mitogen response.
5. **Perforin/granzyme regulatory mechanism.** FA vs control NK: PRF1/GZMB transcription, granule biogenesis (LAMP1), and rescue by FANC-pathway complementation. *Expected if intrinsic:* complementation restores granule loading.

---

## Curation Leads (require curator verification)

**Candidate evidence references + snippets to verify (verbatim against abstracts):**
- `PMID:28557197` — *"a large FA cohort who have not undergone bone marrow transplantation or developed malignancies"* → status upgrade evidence for **transplant-independence**.
- `PMID:30949167` — *"first report showing a defective degranulation mechanism leading to abnormal NK-cell cytotoxicity in FA-patients"* → mechanistic node: NK degranulation lesion.
- `PMID:26895835` — *"Fancc(-/-) B cells show a specific defect in IgG2a switch and impaired Ab-secreting cell (ASC) differentiation"* → model-organism intrinsic B-cell node.
- `PMID:25963299` — *"Lymphoproliferative responses, serum cytokine levels … were similar across patient groups and relatives"* → **conflicting-evidence** flag on the proliferation sub-claim.
- `PMID:35671096` / `PMID:22683204` — competing-mechanism nodes.

**Candidate pathophysiology nodes/edges:** `FANC loss → NK perforin/granzyme deficiency → ↓NK cytotoxicity`; `FANCC loss → Wnt/β-catenin↑ → Blimp1↓ → ↓ASC differentiation`; competing edge `FA DNA damage → NKG2D-L↑ → NK-mediated HSPC clearance`.

**Candidate ontology terms:** natural killer cell (CL:0000623), mature B cell (CL:0000785), common lymphoid progenitor (CL:0000051); processes: natural killer cell mediated cytotoxicity (GO:0042267), granzyme-mediated apoptosis / degranulation (GO:0043313), B cell differentiation (GO:0030183), isotype switching (GO:0045190).

**Candidate HPO disease-annotation additions for Fanconi anemia (OMIM:227650 / MONDO:0009215)** — *currently absent per verified HPO check 2026-09-13; require curator verification against cohort literature:* HP:0040218 (Reduced natural killer cell count), HP:0002721 (Immunodeficiency), a B-lymphocytopenia term, and a decreased-circulating-IgM term. Supporting references: PMID 21542827, 28557197, 25963299.

**Candidate subtype restrictions / status change:** Consider keeping **EMERGING** but split into (a) *NK cytotoxic-machinery defect* — evidence approaching **SUPPORTED**; (b) *lymphoid-progenitor-intrinsic numeric loss* — remains **EMERGING/contested** vs pan-HSPC and NKG2D models; (c) *impaired proliferative response* — **contested/weak**. Note genotype/age stratification is largely absent.

**Candidate knowledge_gaps entries:** lymphoid-specific progenitor loss unproven; NK perforin/granzyme mechanism unknown; hypofunctional-NK vs NKG2D-clearance conflict; FA immune phenotype is a verified ontology-curation gap across three independent layers (HPO disease-level, HPO gene-level, Monarch federated, all 2026-09-13); GenCC/ClinGen/ClinVar and omics repositories (ArrayExpress, EGA) still not machine-verified (GenCC REST attempt returned HTTP 404).

---

## Limitations

- Literature search across iterations 1–2; PubMed rate-limit and a provider DB error truncated two queries (logged). Live source checks performed (it.2–5): GEO DataSets, ClinicalTrials.gov v2, HPO/OMIM at both disease and gene level, and the Monarch Initiative federated aggregator. A GenCC REST query was attempted (HTTP 404, no public API). **Still not machine-verified:** GenCC (bulk download), ClinGen, ClinVar, ArrayExpress, EGA — outstanding, not claimed absent.
- Provenance caveat: the iteration-5 append to `logs/database_source_checks.md` could not be re-hashed in-environment (the execute_code sandbox lacks host-filesystem access and blocks `hashlib`); its `MANIFEST.yaml` sha256 is flagged STALE and needs recomputation by the harness/curator.
- No patient-level or omics data available; the only computation is an under-powered directional tally on abstract-extracted directions.
- Human cohorts are small, mostly cross-sectional, rarely genotype-stratified; longitudinal and lineage-resolved data are lacking.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist evidence matrix](openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_intrinsic_nk_and_b_lymphoid_defect_openscientist_artifacts_data_evidence_matrix.csv)
- [OpenScientist database source checks](openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_intrinsic_nk_and_b_lymphoid_defect_openscientist_artifacts_logs_database_source_checks.md)
- [OpenScientist pubmed search log](openscientist_artifacts/kb_hypotheses_Fanconi_Anemia_fa_intrinsic_nk_and_b_lymphoid_defect_openscientist_artifacts_logs_pubmed_search_log.md)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 18 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 7 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 6 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0040218` (3 mentions) - the report calls it "reduced NK count", "Reduced natural killer cell count"; HP calls it **Reduced total natural killer cell count**, and lists "Reduced NK cell number" among its other names
- `HP:0010976` (2 mentions) - the report calls it "B lymphocytopenia"; HP calls it **Decreased total B cell count**, and lists "B lymphocytopenia" among its other names
- `HP:0002850` (2 mentions) - the report calls it "decreased antibody/IgM"; HP calls it **Decreased circulating IgM concentration**, and lists "Decreased IgM" among its other names
- `HP:0001888` (2 mentions) - the report calls it "lymphopenia"; HP calls it **Decreased total lymphocyte count**, and lists "Lymphopenia" among its other names
- `HP:0001875` (4 mentions) - the report calls it "↓neutrophils"; HP calls it **Decreased total neutrophil count**, and lists "Neutropenia" among its other names
- `HP:0000010` (2 mentions) - the report calls it "recurrent UTI"; HP calls it **Recurrent urinary tract infections**, and lists "Recurrent UTIs" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0040218` - called "reduced NK count", "Reduced natural killer cell count"
- `HP:0002721` - called "immunodeficiency", "Immunodeficiency"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `NCBIGene`.

16 of 18 terms resolved to a current term; the rest could not be looked up either way.