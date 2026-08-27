---
title: Use Cases
status: EVERGREEN
description: >-
  Cross-cutting index of DisMech use cases and applications, aggregated from the
  thematic projects in this repo and from talks, slides, and reports under docs/.
  Groups the ways the knowledge base is (or could be) consumed — clinical decision
  support, precision medicine, drug discovery, causal-genomics validation,
  computational modeling substrates, knowledge-graph integration, EHR mapping,
  AI/ML benchmarking, agentic curation, and education — and also by whether real,
  runnable code that depends on DisMech exists yet.
tags: [META, APPLICATIONS, INDEX, INTEROP]
---

# Use Cases

## Overview

DisMech is not only a curation target — it is a **resource other tools consume**.
Individual project files under `projects/` and talks/reports under `docs/` each
describe applications from their own vantage point. This page **aggregates those
use cases in one place**, grouped by the audience and application domain they
serve, so the "what is this good for?" story can be read end-to-end and each use
case is traceable back to its source.

This is a meta/index project: it does not track disease curation directly.
Curation-domain projects (e.g. [`CANCER`](CANCER.md), [`AUTOIMMUNE`](AUTOIMMUNE.md),
[`NICU`](NICU.md), [`SKELETAL_DYSPLASIAS`](SKELETAL_DYSPLASIAS.md)) define *what*
gets curated; the projects and docs referenced below describe *what the curated
knowledge is used for*.

**Relationship to [`docs/use-cases.md`](../docs/use-cases.md).** That doc is the
prose narrative — the "why" of each application, written for a reader. This
project is the **aggregated, cross-linked map** — the "where", tying each use case
to the concrete project file, talk slide, report, and (below) the actual code that
implements it. The two are meant to be read together; keep them aligned.

**Primary sources aggregated here:**

- [`docs/use-cases.md`](../docs/use-cases.md) — the original prose catalogue of use cases by audience.
- [`docs/slides/dismech-slides.md`](../docs/slides/dismech-slides.md) — the Feb 2026 talk ("A Disease Mechanisms Knowledge Base Built For and With Agentic AI"), whose **Applications**, **Case Studies**, and **Broader Impact** sections enumerate six numbered applications plus clinical-AI, drug-discovery, and AI/ML framings.
- [`docs/presentations/Dismech demo - Feb 2026.pdf`](../docs/presentations/Dismech%20demo%20-%20Feb%202026.pdf) — the demo deck.
- Application-oriented projects: [`GWAS_MECHANISMS`](GWAS_MECHANISMS.md), [`AUTONOMOUS_LABS`](AUTONOMOUS_LABS.md), [`VIRTUAL_CELL`](VIRTUAL_CELL.md), [`TUMOR_MICROENVIRONMENT_MODELING`](TUMOR_MICROENVIRONMENT_MODELING.md), [`SPACE_BIOLOGY`](SPACE_BIOLOGY.md), [`STRUCTURAL_BIOLOGY`](STRUCTURAL_BIOLOGY.md), [`MONDO_EHR_MAPPINGS`](MONDO_EHR_MAPPINGS.md), [`HYPOTHESIS_BASED_PHENOTYPE_ALGORITHMS`](HYPOTHESIS_BASED_PHENOTYPE_ALGORITHMS.md), [`COMORBIDITIES`](COMORBIDITIES.md), [`ORGAN_FIBROSIS_COLLABORATION`](ORGAN_FIBROSIS_COLLABORATION.md), [`NAMO_RD_MODELS`](NAMO_RD_MODELS.md), [`CHILDHOOD_CANCER`](CHILDHOOD_CANCER.md), [`G2P`](G2P.md), [`REACTOME_DISEASES`](REACTOME_DISEASES.md), [`GENESETS`](GENESETS.md), [`INHERITANCE_ENRICHMENT`](INHERITANCE_ENRICHMENT.md).

**Two views of this page.** The [numbered sections](#1-clinical--diagnostic-decision-support)
below group use cases by **audience/domain** (who it's for). The section
immediately below groups them by **implementation maturity** (does code that
consumes DisMech exist yet?). A given use case appears in both.

---

## Tooling view: what actually runs on DisMech

This grouping answers a different question from the domain categories: **which
use cases are backed by real, runnable code in this repo that consumes the
knowledge base**, versus which are still scoping/collaboration plans with no
in-repo tool yet. "Consumes DisMech" means the code reads `kb/**` YAML (or a
derived export of it) as input.

### A. Implemented — tools/code in this repo that depend on DisMech

| Tool / code | Location | Run | Consumes | Use-case § |
|-------------|----------|-----|----------|-----------|
| **Phenomatcher / Phenoagent** — phenopacket ⇄ disease-model matching + agentic explanation + Mermaid match graph | [`src/phenoagent/`](../src/phenoagent/) (`matching.py`, `cyberian_wrapper.py`, `match_graph.py`, `matching_cli.py`, `eval.py`) | `python -m phenoagent.matching_cli` | disorder YAML phenotype frequencies + HPO via OAK | §1.1 |
| **Multi-space embeddings** — pathophysiology/phenotype/treatment/cell-type + per-mechanism embedding, interactive browser | [`src/dismech/embed.py`](../src/dismech/embed.py), [`app/embeddings/`](../app/embeddings/) | `just embed-index`, `just embed-mechanisms-all` | disorder YAML text projected per space | §3.2, §3.1 |
| **KGX / Biolink export** | [`src/dismech/export/kgx_export.py`](../src/dismech/export/kgx_export.py) | `just export-kgx` | disorder YAML → typed Biolink edges | §7.1 |
| **HPOA export** — HPO annotation-format export | [`src/dismech/export/hpoa_export.py`](../src/dismech/export/hpoa_export.py) | `just export-hpoa` | disorder YAML phenotypes | §7.1 |
| **CX2 / NDEx export** — Cytoscape-exchange pathographs | [`src/dismech/export/cx2_export.py`](../src/dismech/export/cx2_export.py); [`docs/cx2-ndex-publishing.md`](../docs/cx2-ndex-publishing.md) | via export module | pathophysiology causal graphs | §7.1 |
| **Tabular / DuckDB export** — relational flatten for SQL/ML | [`src/dismech/export/tabular_export.py`](../src/dismech/export/tabular_export.py) | `python -m dismech.export.tabular_export` | all assertions/descriptors/evidence | §7.2 |
| **Faceted disorder browser** | [`src/dismech/export/browser_export.py`](../src/dismech/export/browser_export.py) → `app/data.js`; [`render.py`](../src/dismech/render.py) | `just gen-browser-data`, `just gen-pages` | disorder YAML | §10.1 |
| **Pathograph builder / causal graphs** | [`src/dismech/graph.py`](../src/dismech/graph.py), [`src/dismech/export/pathograph_export.py`](../src/dismech/export/pathograph_export.py), [`scripts/pathograph_overlap.py`](../scripts/pathograph_overlap.py) | `just gen-pathographs` | pathophysiology `downstream` edges | §1.1, §1.2 |
| **Comorbidity signal tools (COHD)** — generate/insert EHR co-occurrence `association_signals` | [`scripts/cohd_pair_to_signal.py`](../scripts/cohd_pair_to_signal.py), [`scripts/cohd_add_signal_to_comorbidity.py`](../scripts/cohd_add_signal_to_comorbidity.py) | `just cohd-signal`, `just cohd-add-signal` | comorbidity YAML + COHD API | §4 |
| **GWAS gene→program→trait validators** — score Perturb-seq clusters/programs against curated genes | [`scripts/validate_tcell_clusters.py`](../scripts/validate_tcell_clusters.py), [`scripts/validate_k562_programs.py`](../scripts/validate_k562_programs.py); reports in [`docs/`](../docs/gwas-tcell-validation-report.md) | `python scripts/validate_tcell_clusters.py` | disorder genes + GO/cell-type terms | §5.1 |
| **Gene-set alignment** | [`src/dismech/genesets_align.py`](../src/dismech/genesets_align.py), [`src/dismech/structured_sources/`](../src/dismech/structured_sources/) | `just genesets-align`, `just genesets-rebuild` | disorder genes vs curated gene sets | §5.2 |
| **Grouping linter/evaluator** — audit/classify grouping membership (OWL-lite) | [`src/dismech/groupings.py`](../src/dismech/groupings.py) | `just check-groupings` | grouping + disorder YAML | §5.2 |
| **Structured-source ingest** — Orphanet/ClinGen/ICEES/NCIT/gene-sets → `references_cache/` | [`src/dismech/structured_sources/`](../src/dismech/structured_sources/) | `just structured-rebuild-orphanet`, `just clingen-rebuild`, `just icees-rebuild` | external DBs → citable rows | §7.3, §2.3, §4 |
| **Validation stack** — schema / term / reference anti-hallucination QC | `linkml-validate` + [`scripts/run_term_validator.sh`](../scripts/run_term_validator.sh), [`scripts/run_reference_validator.sh`](../scripts/run_reference_validator.sh), [`reference_cache_frontmatter.py`](../src/dismech/reference_cache_frontmatter.py) | `just qc`, `just validate <file>` | disorder YAML + cached refs | §9.2 |
| **Compliance & priority dashboards** — weighted scoring, curation triage | [`src/dismech/qc_dashboard.py`](../src/dismech/qc_dashboard.py), [`src/dismech/priority_dashboard.py`](../src/dismech/priority_dashboard.py) | `just compliance-all`, `just gen-dashboard` | all disorder YAML | §9.2 |
| **OHDSI/OMOP cohort → definition** — computable case-definition ingest | [`scripts/ohdsi_cohort_to_definition.py`](../scripts/ohdsi_cohort_to_definition.py) (`create-definitions-from-ohdsi` skill) | `python scripts/ohdsi_cohort_to_definition.py` | writes `definitions` blocks | §8.2 |
| **MONDO EHR / priority mapping** — MONDO-driven concept-set + candidate export | [`scripts/export_mondo_priority_candidates.py`](../scripts/export_mondo_priority_candidates.py), [`src/dismech/export/mondo_emc_export.py`](../src/dismech/export/mondo_emc_export.py) | `just export-mondo-tsv` | disorder MONDO mappings | §8.1 |
| **Reactome cross-reference** | [`scripts/fetch_reactome_disease.py`](../scripts/fetch_reactome_disease.py) | `python scripts/fetch_reactome_disease.py` | disorder ↔ Reactome pathways | §5.2 |
| **NCIT P302 treatment-indication audit** | [`scripts/ncit_p302_audit.py`](../scripts/ncit_p302_audit.py) | `just ncit-p302-audit` | treatments vs NCIT indications | §2.3 |
| **Disease inventory census** | [`src/dismech/export/disease_inventory.py`](../src/dismech/export/disease_inventory.py) | `just export-disease-inventory` | all disorder/subtype MONDO status | §5.2, §8.3 |

> Note: Phenoagent lives under `src/phenoagent/` (not `src/dismech/`) but is
> part of this repository and reads dismech disease models directly — it is the
> flagship worked example of a downstream consumer.

### B. Partial — script/schema scaffolding exists, full tool still forming

| Capability | What exists | Gap | Use-case § |
|------------|-------------|-----|-----------|
| Hypothesis-based EHR case-finding | schema slots (`derivation_basis`, `validation_status`) + [`scripts/hypothesis_deep_research.py`](../scripts/hypothesis_deep_research.py) | no end-to-end EHR query runner | §8.2 |
| Disease-trajectory mining | `disease-trajectories` skill + COHD tooling | no packaged DT ingester in-repo | §4 |
| G2P alignment | audit scripts + research artifacts under [`docs/research/`](../docs/research/) | no maintained mapping module | §5.2 |

### C. Aspirational — external dependency or scoping only (no in-repo code yet)

These are collaboration/alignment plans: the "tool" lives in another project or
doesn't exist yet, and DisMech is the intended knowledge substrate.

| Use case | Depends on | Source |
|----------|-----------|--------|
| Autonomous / self-driving labs | OpenScientist (external) | [`AUTONOMOUS_LABS`](AUTONOMOUS_LABS.md) (§6.1) |
| Tumor-microenvironment / digital-twin modeling | external ABM/RL simulators | [`TUMOR_MICROENVIRONMENT_MODELING`](TUMOR_MICROENVIRONMENT_MODELING.md) (§6.2) |
| Virtual-cell / single-cell FM alignment | CZI Virtual Cell, CELLxGENE | [`VIRTUAL_CELL`](VIRTUAL_CELL.md) (§6.3) |
| Structure-guided interpretation | PDB / AlphaFold workflows | [`STRUCTURAL_BIOLOGY`](STRUCTURAL_BIOLOGY.md) (§6.4) |
| Cross-organ fibrosis atlas integration | Saez-Rodriguez atlas | [`ORGAN_FIBROSIS_COLLABORATION`](ORGAN_FIBROSIS_COLLABORATION.md) (§11) |
| Rare-disease experimental-model bridge | Monarch NAMO | [`NAMO_RD_MODELS`](NAMO_RD_MODELS.md) (§5.3) |
| Space-health data alignment | NASA OSDR | [`SPACE_BIOLOGY`](SPACE_BIOLOGY.md) (§11) |
| Childhood-cancer / CCDI alignment | NCI CCDI ecosystem | [`CHILDHOOD_CANCER`](CHILDHOOD_CANCER.md) (§11) |

---

## 1. Clinical & Diagnostic Decision Support

### 1.1 Mechanism-aware differential diagnosis (Phenomatcher)
Given a patient phenotype profile (a GA4GH **Phenopacket**), match it against the
DisMech knowledge base to rank candidate diseases. Beyond flat HPO overlap, the
curated causal graphs add a **mechanistic dimension** that distinguishes diseases
sharing phenotypes (e.g. Fanconi Anemia vs. Diamond-Blackfan). Matching is
frequency-weighted and ontology-aware (exact / broader / narrower / related via
OAK), and non-matches get agentic, causal-graph-grounded explanations plus a
`pr_is_diagnosis` estimate.
*Sources: [slides — Application 1](../docs/slides/dismech-slides.md); [`docs/use-cases.md` "Differential Diagnosis Support"](../docs/use-cases.md). Implemented: [`src/phenoagent/`](../src/phenoagent/).*

### 1.2 Phenotype/complication explanation
Trace a presentation back through the causal graph (upstream molecular defect →
intermediate mechanism → phenotype), or forward to **predict downstream
complications**. This is what free-text LLM output lacks: traceable, PMID-backed
mechanistic reasoning.
*Sources: [slides — "For Clinical AI Systems"](../docs/slides/dismech-slides.md).*

### 1.3 Genotype-specific counseling
Context-specific annotations capture how a phenotype's presence/frequency changes
by genotype (e.g. pancytopenia is excluded in FANCD1/BRCA2 and FA-S/BRCA1
subtypes), supporting genotype-aware prognosis and counseling.
*Sources: [slides — provenance & clinical-AI sections](../docs/slides/dismech-slides.md).*

### 1.4 Clinical trial matching
With `clinical_trials`, `phenotypes`, and genetics all structured and
ontology-linked, patients can be matched to relevant trials from their
genotype–phenotype profile.
*Sources: [`docs/use-cases.md` "Clinical Trial Matching"](../docs/use-cases.md).*

### 1.5 Care-guideline coverage
Recent clinical **Practice Guideline** citations are mined to anchor and fill
phenotype/treatment gaps in disorder entries.
*Sources: [`CLINICAL_CARE_GUIDELINES`](CLINICAL_CARE_GUIDELINES.md).*

---

## 2. Precision Medicine & Therapeutics

### 2.1 Genotype-to-treatment pathway mapping
For entries with `genetic_basis` → `pathophysiology` → `treatments` chains
(especially cancers — BRAF V600E melanoma, ALK-rearranged NSCLC), DisMech encodes
the logic of precision oncology: specific mutations → specific targeted therapies.
Treatment `target_mechanisms` links a drug to the exact pathophysiology node it
acts on.
*Sources: [`docs/use-cases.md` "Genotype-to-Treatment Pathway Mapping"](../docs/use-cases.md); [`CHECKPOINT_INHIBITORS`](CHECKPOINT_INHIBITORS.md); [`CANCER`](CANCER.md).*

### 2.2 Treatment-mechanism (drug–bug / drug–virus / drug–fungus) design pattern
Conserved treatment-mechanism modules link antimicrobial/antiviral/antifungal
drugs to the molecular target they inhibit and the resistance branches that gate
drug choice — a reusable, machine-queryable therapy-mechanism layer.
*Sources: [`ANTIMICROBIAL`](ANTIMICROBIAL.md), [`ANTIVIRAL`](ANTIVIRAL.md), [`ANTIFUNGAL`](ANTIFUNGAL.md), [`CHECKPOINT_INHIBITORS`](CHECKPOINT_INHIBITORS.md).*

### 2.3 Treatment-indication & ontology alignment
Accepted therapeutic uses (NCIT P302) and MAXO-vs-NCIT treatment descriptor
choices make treatments queryable by action, agent, and indication.
*Sources: [`NCIT_TREATMENT_INDICATIONS`](NCIT_TREATMENT_INDICATIONS.md), [`MAXO_NCIT_TREATMENTS`](MAXO_NCIT_TREATMENTS.md). Implemented: [`scripts/ncit_p302_audit.py`](../scripts/ncit_p302_audit.py).*

---

## 3. Drug Discovery & Repurposing

### 3.1 Mechanism-based drug repurposing
Two diseases that share pathophysiology (same biological processes, same cell
types) but differ in treatment are cross-disease repurposing candidates. Curated
`pathophysiology`, `cell_types`, and `treatments` fields make the comparison
systematic, and multi-space embeddings surface non-obvious mechanism neighbors
(e.g. shared "Inflammatory Bone Marrow Microenvironment" or "Genomic Instability"
mechanisms across otherwise-unrelated diseases).
*Sources: [slides — "For Drug Discovery" & Application 2](../docs/slides/dismech-slides.md); [`docs/use-cases.md` "Mechanism-Based Drug Repurposing"](../docs/use-cases.md).*

### 3.2 Multi-space disease & mechanism embeddings
Four separate embedding spaces (pathophysiology, phenotype, treatment, cell type)
let diseases that cluster in phenotype space but diverge in mechanism space be
flagged — informative for repurposing and target selection. Individual
mechanisms are embedded too, enabling cross-disease pathophysiology similarity
search.
*Sources: [slides — Application 2 + Embedding appendix](../docs/slides/dismech-slides.md); [`docs/embeddings.md`](../docs/embeddings.md). Implemented: [`src/dismech/embed.py`](../src/dismech/embed.py), [`app/embeddings/`](../app/embeddings/).*

### 3.3 Comorbidity-informed multi-target design
Directional comorbidities suggest shared vulnerabilities exploitable for
multi-target drug design (see §4).
*Sources: [slides — "For Drug Discovery"](../docs/slides/dismech-slides.md).*

---

## 4. Comorbidity & Disease-Trajectory Discovery

Model **directional comorbidities** with mechanistic evidence, combining
EHR-derived Disease Trajectories (temporal directionality), literature PMIDs, GO
enrichment of shared mechanisms, and genetic-correlation overlap. Each comorbidity
page shows the **mechanistic overlap** between a disease pair — moving beyond
epidemiological correlation to mechanistic explanation, and generating novel
co-occurrence hypotheses.
*Sources: [slides — Application 3](../docs/slides/dismech-slides.md); [`COMORBIDITIES`](COMORBIDITIES.md); [`docs/use-cases.md` "Comorbidity Prediction"](../docs/use-cases.md). Implemented: [`scripts/cohd_pair_to_signal.py`](../scripts/cohd_pair_to_signal.py), [`scripts/cohd_add_signal_to_comorbidity.py`](../scripts/cohd_add_signal_to_comorbidity.py).*

---

## 5. Causal Genomics & Functional-Genomics Validation

### 5.1 Validating causal gene→program→trait pipelines
DisMech acts as a validation/interpretation layer for computational pipelines that
infer causal gene-to-trait relationships from GWAS + Perturb-seq (pilot: Ota et
al., *Nature* 2025). Pipeline edges are scored against curated knowledge as
CONFIRMED / PARTIAL / NOVEL / CONTRADICTED, with novel findings feeding back as
prioritized curation targets — a bidirectional improvement loop.
*Sources: [`GWAS_MECHANISMS`](GWAS_MECHANISMS.md); [slides — Application 4 + T-cell Perturb-seq case study](../docs/slides/dismech-slides.md); [`docs/gwas-tcell-validation-report.md`](../docs/gwas-tcell-validation-report.md), [`docs/k562-poc-validation.md`](../docs/k562-poc-validation.md). Implemented: [`scripts/validate_tcell_clusters.py`](../scripts/validate_tcell_clusters.py), [`scripts/validate_k562_programs.py`](../scripts/validate_k562_programs.py).*

### 5.2 Gene-set, pathway & gene-panel alignment
Cross-reference disease-associated genes/pathways with external catalogues
(Reactome disease pathways, Gene2Phenotype rows, curated gene sets) to drive
curation triage and coverage auditing.
*Sources: [`REACTOME_DISEASES`](REACTOME_DISEASES.md), [`G2P`](G2P.md), [`GENESETS`](GENESETS.md). Implemented: [`src/dismech/genesets_align.py`](../src/dismech/genesets_align.py), [`scripts/fetch_reactome_disease.py`](../scripts/fetch_reactome_disease.py), [`src/dismech/groupings.py`](../src/dismech/groupings.py).*

### 5.3 Experimental-model bridging
Bridge DisMech's disease-centric mechanisms to rare-disease experimental-model
resources (Monarch NAMO) without importing their full schemas.
*Sources: [`NAMO_RD_MODELS`](NAMO_RD_MODELS.md).*

---

## 6. Computational & Simulation Substrate

### 6.1 Autonomous / self-driving labs — experiment suggestion
DisMech + OpenScientist as an **auditable experiment-suggestion layer**: DisMech
stores a computable pathograph, OpenScientist ranks mechanistic gaps, and a
protocol layer turns selected gaps into standardized, human-reviewable experiments.
*Sources: [`AUTONOMOUS_LABS`](AUTONOMOUS_LABS.md).*

### 6.2 Tumor-microenvironment modeling & cancer digital twins
Structured mechanism models as a knowledge substrate for multiscale agent-based
TME simulators, RL-guided therapy optimization, and cancer digital-twin frameworks.
*Sources: [`TUMOR_MICROENVIRONMENT_MODELING`](TUMOR_MICROENVIRONMENT_MODELING.md).*

### 6.3 Virtual-cell / single-cell foundation-model alignment
Align disease-mechanism data with the CZI Virtual Cell initiative so it can
connect to single-cell foundation models (scGPT, UCE, TranscriptFormer, …) and the
CELLxGENE Census.
*Sources: [`VIRTUAL_CELL`](VIRTUAL_CELL.md).*

### 6.4 Structure-guided mechanism & variant interpretation
Diseases where experimental structure (X-ray, cryo-EM) or predicted structure
(AlphaFold) is key to understanding pathophysiology, enabling drug design, or
interpreting variant pathogenicity.
*Sources: [`STRUCTURAL_BIOLOGY`](STRUCTURAL_BIOLOGY.md).*

---

## 7. Knowledge-Graph & Data Integration

### 7.1 Biolink/KGX export → Monarch KG, Translator
Every assertion exports to Biolink Model KGX edges (disease→phenotype,
gene→disease, treatment, exposure→outcome) tagged with `primary_knowledge_source:
infores:dismech`, frequency qualifiers, and PMID supporting-text — ready for
integration with Monarch KG and Translator.
*Sources: [slides — Application 5](../docs/slides/dismech-slides.md); [`docs/use-cases.md` "Knowledge Graph Seeding"](../docs/use-cases.md); [`docs/cx2-ndex-publishing.md`](../docs/cx2-ndex-publishing.md). Implemented: [`kgx_export.py`](../src/dismech/export/kgx_export.py), [`hpoa_export.py`](../src/dismech/export/hpoa_export.py), [`cx2_export.py`](../src/dismech/export/cx2_export.py).*

### 7.2 Tabular export for analysis (DuckDB/TSV)
Flatten to relational tables (`disorders`, `assertions`, `descriptors`,
`evidence`) for SQL/statistical/ML feature analysis and cross-disease queries.
*Sources: [slides — Application 6](../docs/slides/dismech-slides.md). Implemented: [`src/dismech/export/tabular_export.py`](../src/dismech/export/tabular_export.py).*

### 7.3 Cross-ontology bridging
Each entry links MONDO ↔ HP ↔ GO ↔ CL ↔ UBERON ↔ MAXO ↔ CHEBI in one curated
record, creating implicit cross-ontology mappings that are otherwise hard to
derive automatically.
*Sources: [`docs/use-cases.md` "Cross-Ontology Bridging"](../docs/use-cases.md).*

### 7.4 Inheritance representation & ontology feedback
Enrich inheritance detail (de novo rate, penetrance, expressivity,
parent-of-origin) to inform how MONDO represents the inherited vs. de novo
distinction.
*Sources: [`INHERITANCE_ENRICHMENT`](INHERITANCE_ENRICHMENT.md).*

---

## 8. EHR & Clinical Data Integration

### 8.1 MONDO-driven EHR rare-disease mapping
Replace brittle hand-maintained SQL code lists with a reproducible MONDO-driven
pipeline that generates versioned SNOMED/ICD concept sets for OMOP queries.
*Sources: [`MONDO_EHR_MAPPINGS`](MONDO_EHR_MAPPINGS.md); [`docs/mondo-prioritizer.md`](../docs/mondo-prioritizer.md). Implemented: [`scripts/export_mondo_priority_candidates.py`](../scripts/export_mondo_priority_candidates.py), [`src/dismech/export/mondo_emc_export.py`](../src/dismech/export/mondo_emc_export.py).*

### 8.2 Hypothesis-based phenotype algorithms / trigger-provoked case-finding
Computable EHR/OMOP case-finding queries predicated on a mechanism (e.g. scan for
a new arrhythmia/seizure shortly after a fever to surface latent channelopathy
carriers), with epistemic grounding marked (established vs. mechanistic-hypothesis
vs. model-extrapolation).
*Sources: [`HYPOTHESIS_BASED_PHENOTYPE_ALGORITHMS`](HYPOTHESIS_BASED_PHENOTYPE_ALGORITHMS.md); [`docs/hypothesis-based-phenotype-algorithms.md`](../docs/hypothesis-based-phenotype-algorithms.md). Partial: [`scripts/ohdsi_cohort_to_definition.py`](../scripts/ohdsi_cohort_to_definition.py), [`scripts/hypothesis_deep_research.py`](../scripts/hypothesis_deep_research.py).*

### 8.3 ICD coverage-gap cataloguing
Catalogue rare MONDO diseases lacking ICD (especially ICD-11 Foundation) mappings
to prioritize coding-gap remediation.
*Sources: [`RARE_DISEASE_NO_ICD_CODE`](RARE_DISEASE_NO_ICD_CODE.md).*

---

## 9. AI/ML Benchmarking & Agentic Curation

### 9.1 Benchmark & training resource
~500 disorders with machine-readable, provenance-chained pathophysiology support
benchmarks for: causal-reasoning evaluation (do LLMs reproduce mechanism chains?),
claim verification (does a snippet support a claim given a PMID?), ontology
grounding (HP/GO/CL assignment), context-conditioned phenotype prediction, and
knowledge-graph completion.
*Sources: [slides — "For AI/ML Researchers"](../docs/slides/dismech-slides.md); [`docs/use-cases.md` "Ontology-Grounded NLP Benchmark", "LLM Hallucination Benchmarking"](../docs/use-cases.md).*

### 9.2 Agentic curation model & anti-hallucination validation
DisMech itself is a demonstration use case: human-directed AI agents read
literature, generate validated YAML, and submit PRs, gated by a deterministic
three-layer validation stack (schema / term / reference). This pattern and its
compliance-driven prioritization generalize to other biomedical knowledge bases.
*Sources: [slides — "The Agentic Curation Model" & validation stack](../docs/slides/dismech-slides.md); [`docs/use-cases.md` "Automated Curation Pipelines", "Compliance-Driven Prioritization"](../docs/use-cases.md); [`REFERENCE_EVIDENCE_VERIFICATION`](REFERENCE_EVIDENCE_VERIFICATION.md). Implemented: validation stack ([`run_term_validator.sh`](../scripts/run_term_validator.sh), [`run_reference_validator.sh`](../scripts/run_reference_validator.sh)), [`qc_dashboard.py`](../src/dismech/qc_dashboard.py), [`priority_dashboard.py`](../src/dismech/priority_dashboard.py).*

---

## 10. Education & Training

### 10.1 Interactive pathophysiology browser
The HTML rendering / faceted search is a teaching tool: students explore the full
mechanism chain from genetic variant → molecular dysfunction → cellular change →
clinical phenotype.
*Sources: [`docs/use-cases.md` "Interactive Pathophysiology Browser"](../docs/use-cases.md); [slides — browsing DisMech](../docs/slides/dismech-slides.md). Implemented: [`browser_export.py`](../src/dismech/export/browser_export.py), [`render.py`](../src/dismech/render.py).*

### 10.2 Evidence-literacy training
The evidence model (SUPPORT/REFUTE/PARTIAL with required PMID snippets) trains
learners to evaluate claims against primary literature rather than accept
statements at face value.
*Sources: [`docs/use-cases.md` "Evidence Literacy Training"](../docs/use-cases.md).*

---

## 11. Domain & Collaboration Use Cases

Domain-scoped applications that pair a curation focus with an external
data ecosystem or collaborator:

| Use case | What it demonstrates | Source |
|----------|----------------------|--------|
| **Space biology & disease mechanisms** | Microgravity/radiation/deconditioning insights; alignment with NASA OSDR datasets | [`SPACE_BIOLOGY`](SPACE_BIOLOGY.md) |
| **Cross-organ fibrosis atlas** | Integrate the shared/organ-specific fibrotic gene programs (Saez-Rodriguez lab) with the `fibrotic_response` module | [`ORGAN_FIBROSIS_COLLABORATION`](ORGAN_FIBROSIS_COLLABORATION.md) |
| **Childhood cancer / CCDI alignment** | Contribute structured pediatric-malignancy mechanisms to the NCI Childhood Cancer Data Initiative | [`CHILDHOOD_CANCER`](CHILDHOOD_CANCER.md) |
| **Rare-disease mechanism cataloguing** | Structured mechanism reference for poorly-documented ultra-rare diseases | [`docs/use-cases.md` "Rare Disease Mechanism Cataloging"](../docs/use-cases.md); [`LIPOYLATION`](LIPOYLATION.md) |
| **Microbiome integration** | Enrich infectious/gut conditions with microbiome (e.g. NMDC) data | [`docs/use-cases.md` "Microbiome Integration"](../docs/use-cases.md) |

---

## Case studies (worked examples from the talk)

- **Fanconi Anemia — deep curation**: the reference "full-depth" entry (19 mechanisms, 92 phenotypes, 25 genes, 24 subtypes, per-genotype context annotations), used to exercise Phenomatcher and the causal-graph applications.
- **Lipoylation disorders — ultra-rare**: shows that deep-research is unreliable for <20-patient Mendelian disorders (wrong disease returned for LIPT2); direct PubMed/OMIM curation is the quality driver.
- **NICU project — systematic domain curation**: demonstrates scaling to a domain-specific project with clear clinical scope.

*Source: [slides — Case Studies](../docs/slides/dismech-slides.md).*

---

## Source-to-use-case map

Quick traceability from each source project/doc to the section(s) above:

| Source | Use-case section(s) |
|--------|---------------------|
| [`docs/use-cases.md`](../docs/use-cases.md) | 1.1, 1.4, 3.1, 4, 7.1, 7.3, 9.1, 9.2, 10, 11 |
| [`docs/slides/dismech-slides.md`](../docs/slides/dismech-slides.md) | 1.1–1.3, 3.1–3.3, 4, 5.1, 6.*, 7.1–7.2, 9.*, 10.1 |
| [`GWAS_MECHANISMS`](GWAS_MECHANISMS.md) | 5.1 |
| [`AUTONOMOUS_LABS`](AUTONOMOUS_LABS.md) | 6.1 |
| [`TUMOR_MICROENVIRONMENT_MODELING`](TUMOR_MICROENVIRONMENT_MODELING.md) | 6.2 |
| [`VIRTUAL_CELL`](VIRTUAL_CELL.md) | 6.3 |
| [`STRUCTURAL_BIOLOGY`](STRUCTURAL_BIOLOGY.md) | 6.4 |
| [`COMORBIDITIES`](COMORBIDITIES.md) | 4 |
| [`MONDO_EHR_MAPPINGS`](MONDO_EHR_MAPPINGS.md) | 8.1 |
| [`HYPOTHESIS_BASED_PHENOTYPE_ALGORITHMS`](HYPOTHESIS_BASED_PHENOTYPE_ALGORITHMS.md) | 8.2 |
| [`RARE_DISEASE_NO_ICD_CODE`](RARE_DISEASE_NO_ICD_CODE.md) | 8.3 |
| [`REACTOME_DISEASES`](REACTOME_DISEASES.md), [`G2P`](G2P.md), [`GENESETS`](GENESETS.md) | 5.2 |
| [`NAMO_RD_MODELS`](NAMO_RD_MODELS.md) | 5.3 |
| [`INHERITANCE_ENRICHMENT`](INHERITANCE_ENRICHMENT.md) | 7.4 |
| [`ANTIMICROBIAL`](ANTIMICROBIAL.md), [`ANTIVIRAL`](ANTIVIRAL.md), [`ANTIFUNGAL`](ANTIFUNGAL.md), [`CHECKPOINT_INHIBITORS`](CHECKPOINT_INHIBITORS.md) | 2.2 |
| [`NCIT_TREATMENT_INDICATIONS`](NCIT_TREATMENT_INDICATIONS.md), [`MAXO_NCIT_TREATMENTS`](MAXO_NCIT_TREATMENTS.md) | 2.3 |
| [`CLINICAL_CARE_GUIDELINES`](CLINICAL_CARE_GUIDELINES.md) | 1.5 |
| [`CHILDHOOD_CANCER`](CHILDHOOD_CANCER.md) | 11 |
| [`ORGAN_FIBROSIS_COLLABORATION`](ORGAN_FIBROSIS_COLLABORATION.md) | 11 |
| [`SPACE_BIOLOGY`](SPACE_BIOLOGY.md) | 11 |
| [`REFERENCE_EVIDENCE_VERIFICATION`](REFERENCE_EVIDENCE_VERIFICATION.md) | 9.2 |

---

## Maintenance

This is a **living index**. When a new application-oriented project lands under
`projects/`, or a talk/report under `docs/` articulates a new application, add it
to the relevant section above and to the source-to-use-case map. Keep the
narrative catalogue in [`docs/use-cases.md`](../docs/use-cases.md) and this
project aligned — the doc is the prose "why", this project is the aggregated,
cross-linked "where" (including the tooling-maturity view of which use cases have
running code).
