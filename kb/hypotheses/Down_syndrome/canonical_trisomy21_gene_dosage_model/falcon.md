---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-24T16:05:41.788488'
end_time: '2026-05-24T16:25:11.172982'
duration_seconds: 1169.38
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Down_syndrome
  category: Genetic
  hypothesis_group_id: canonical_trisomy21_gene_dosage_model
  hypothesis_label: Canonical Trisomy 21 Gene Dosage / Multisystem Dysregulation Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: canonical_trisomy21_gene_dosage_model\nhypothesis_label:\
    \ Canonical Trisomy 21 Gene Dosage / Multisystem Dysregulation Model\nstatus:\
    \ CANONICAL\ndescription: Down syndrome is caused by trisomy 21 (typically meiotic\
    \ non-disjunction), producing a third\n  copy of all ~225 protein-coding HSA21\
    \ genes. Gene-dosage imbalance \u2014 particularly of DYRK1A, DSCAM,\n  APP, RCAN1,\
    \ SOD1, ETS2, and the chromosome 21 miRNA cluster \u2014 perturbs neurogenesis,\
    \ synaptogenesis,\n  cardiac outflow tract development, hematopoiesis, and immune\
    \ regulation. The resulting multisystem phenotype\n  includes intellectual disability,\
    \ characteristic facies, congenital heart disease (~50% AV septal defects),\n\
    \  early-onset Alzheimer disease (APP-driven), increased TMD/AMKL leukemia risk\
    \ (GATA1 mutations on trisomic\n  21), autoimmune disorders, and characteristic\
    \ musculoskeletal features. Trisomy 21 mouse models (Ts65Dn,\n  Dp16) recapitulating\
    \ segmental HSA21 trisomy validate the gene- dosage model and have enabled mechanistic\n\
    \  dissection of individual HSA21-gene contributions.\nevidence:\n- reference:\
    \ PMID:39768129\n  reference_title: Down syndrome and brain development\n  supports:\
    \ SUPPORT\n  evidence_source: OTHER\n  snippet: This increase is due to a shift\
    \ from neuron to astrocyte differentiation during brain development.\n  explanation:\
    \ |\n    Existing canonical mechanism citation in the dismech knowledge base,\
    \ used as the seed for the hypothesis-search deep-research run."
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 95
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Down_syndrome
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** canonical_trisomy21_gene_dosage_model
- **Hypothesis Label:** Canonical Trisomy 21 Gene Dosage / Multisystem Dysregulation Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_trisomy21_gene_dosage_model
hypothesis_label: Canonical Trisomy 21 Gene Dosage / Multisystem Dysregulation Model
status: CANONICAL
description: Down syndrome is caused by trisomy 21 (typically meiotic non-disjunction), producing a third
  copy of all ~225 protein-coding HSA21 genes. Gene-dosage imbalance — particularly of DYRK1A, DSCAM,
  APP, RCAN1, SOD1, ETS2, and the chromosome 21 miRNA cluster — perturbs neurogenesis, synaptogenesis,
  cardiac outflow tract development, hematopoiesis, and immune regulation. The resulting multisystem phenotype
  includes intellectual disability, characteristic facies, congenital heart disease (~50% AV septal defects),
  early-onset Alzheimer disease (APP-driven), increased TMD/AMKL leukemia risk (GATA1 mutations on trisomic
  21), autoimmune disorders, and characteristic musculoskeletal features. Trisomy 21 mouse models (Ts65Dn,
  Dp16) recapitulating segmental HSA21 trisomy validate the gene- dosage model and have enabled mechanistic
  dissection of individual HSA21-gene contributions.
evidence:
- reference: PMID:39768129
  reference_title: Down syndrome and brain development
  supports: SUPPORT
  evidence_source: OTHER
  snippet: This increase is due to a shift from neuron to astrocyte differentiation during brain development.
  explanation: |
    Existing canonical mechanism citation in the dismech knowledge base, used as the seed for the hypothesis-search deep-research run.
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

### Curation Leads

Provide candidate updates for the KB, but label these as leads requiring curator
verification. Include:

- candidate evidence references and exact abstract snippets to verify
- candidate pathophysiology nodes or edges
- candidate ontology terms for cell types and biological processes
- candidate subtype restrictions or status changes
- candidate `knowledge_gaps` or discussion prompts for unresolved causal claims,
  conflicting evidence, or explicit source/data absences

If the provider supports artifacts, produce artifact-friendly outputs such as an
evidence matrix, mechanistic diagram, knowledge-gap table, or comparison table.
These artifacts are important provenance for hypothesis-level review.


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Down_syndrome
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** canonical_trisomy21_gene_dosage_model
- **Hypothesis Label:** Canonical Trisomy 21 Gene Dosage / Multisystem Dysregulation Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_trisomy21_gene_dosage_model
hypothesis_label: Canonical Trisomy 21 Gene Dosage / Multisystem Dysregulation Model
status: CANONICAL
description: Down syndrome is caused by trisomy 21 (typically meiotic non-disjunction), producing a third
  copy of all ~225 protein-coding HSA21 genes. Gene-dosage imbalance — particularly of DYRK1A, DSCAM,
  APP, RCAN1, SOD1, ETS2, and the chromosome 21 miRNA cluster — perturbs neurogenesis, synaptogenesis,
  cardiac outflow tract development, hematopoiesis, and immune regulation. The resulting multisystem phenotype
  includes intellectual disability, characteristic facies, congenital heart disease (~50% AV septal defects),
  early-onset Alzheimer disease (APP-driven), increased TMD/AMKL leukemia risk (GATA1 mutations on trisomic
  21), autoimmune disorders, and characteristic musculoskeletal features. Trisomy 21 mouse models (Ts65Dn,
  Dp16) recapitulating segmental HSA21 trisomy validate the gene- dosage model and have enabled mechanistic
  dissection of individual HSA21-gene contributions.
evidence:
- reference: PMID:39768129
  reference_title: Down syndrome and brain development
  supports: SUPPORT
  evidence_source: OTHER
  snippet: This increase is due to a shift from neuron to astrocyte differentiation during brain development.
  explanation: |
    Existing canonical mechanism citation in the dismech knowledge base, used as the seed for the hypothesis-search deep-research run.
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

### Curation Leads

Provide candidate updates for the KB, but label these as leads requiring curator
verification. Include:

- candidate evidence references and exact abstract snippets to verify
- candidate pathophysiology nodes or edges
- candidate ontology terms for cell types and biological processes
- candidate subtype restrictions or status changes
- candidate `knowledge_gaps` or discussion prompts for unresolved causal claims,
  conflicting evidence, or explicit source/data absences

If the provider supports artifacts, produce artifact-friendly outputs such as an
evidence matrix, mechanistic diagram, knowledge-gap table, or comparison table.
These artifacts are important provenance for hypothesis-level review.


# Hypothesis-Search Report: Canonical Trisomy 21 Gene Dosage / Multisystem Dysregulation Model (Down syndrome)

## Scope
This report evaluates a *mechanistic hypothesis* (not a general disease overview): trisomy 21 (T21) causes Down syndrome (DS) through gene-dosage imbalance of chr21 loci that perturb multiple developmental and homeostatic pathways, yielding multisystem phenotypes. Evidence is organized to support, refute, qualify, or compete with this model, prioritizing 2023–2024 primary studies.

---

## Executive Judgment
**Verdict: Supported, with major qualifications.**

**Reasoning.** The strongest support comes from **direct gene-dosage perturbation** experiments showing that correcting copy number of specific trisomic loci rescues DS-relevant phenotypes in vivo and in vitro. Notably, (i) correcting the **interferon receptor (IFNR) cluster** copy number in the Dp16 mouse rescues multiple DS-like phenotypes (developmental delay, cognition, craniofacial changes, and congenital heart malformations) and attenuates interferon hyperactivity, establishing a causal dosage-sensitive module (waugh2023triplicationofthe pages 7-8, waugh2023triplicationofthe pages 7-7, waugh2023triplicationofthe pages 28-29). (ii) Systematic mapping in the Dp1Tyb model identifies **DYRK1A triplication** as *necessary* for congenital heart defects (CHD) and ties this to cardiomyocyte proliferation and mitochondrial dysfunction; reducing Dyrk1a to two copies rescues defects (lanaelola2024increaseddosageof pages 1-3, lanaelola2024increaseddosageof pages 8-9, lanaelola2024increaseddosageof pages 6-8). (iii) In human trisomy 21 iPSC-derived neural lineages, chromosome-scale dosage correction with inducible **XIST** represses chr21 genes toward euploid levels and rescues a strong astrogenesis bias, supporting direct causality of dosage imbalance for at least some neurodevelopmental phenotypes (bansal2024adynamicin pages 12-13, bansal2024adynamicin pages 1-1).

**Caveats.** The model is **not fully explained by single-gene or single-locus dosage**. IFNR correction does not rescue all phenotypes (waugh2023triplicationofthe pages 7-8, waugh2023triplicationofthe pages 28-29), DYRK1A is necessary but not sufficient for all CHD contexts (implying additional interacting loci) (lanaelola2024increaseddosageof pages 9-11), and several DS-associated systemic signatures (e.g., heme/hypoxia/stress erythropoiesis) appear **independent of IFNR/JAK modulation**, indicating parallel trisomy-driven programs (donovan2024multimodalanalysisof pages 8-10, donovan2024multimodalanalysisof pages 23-29). Reviews and transcriptomic syntheses further indicate **genome-wide (trans) dysregulation and epigenetic remodeling** beyond chr21, which can amplify or reshape primary dosage effects (chapman2024geneexpressionstudies pages 8-9, maheshwari2024epigeneticsofdown pages 10-11).

---

## Key Concepts and Definitions (current understanding)

1. **Gene-dosage disorder.** DS is a prototypical gene-dosage disorder where triplication of chr21 (or orthologous segments in model systems) increases dosage of many genes and regulatory elements, often approximating ~1.5× transcript abundance but with substantial context-specific compensation and downstream trans effects (bansal2024adynamicin pages 12-13, bansal2024adynamicin pages 3-4).

2. **Dosage-sensitive loci vs. distributed architecture.** A historical “Down syndrome critical region (DSCR)” model posited a small chr21 segment as the main causal interval, but mouse genetic tests indicate DSCR triplication alone does not recapitulate key phenotypes and that **distributed multi-gene dosage and epistasis/compensation** better explain the phenotype (murphy2024downsyndromeand pages 6-7, murphy2024downsyndromeand pages 4-6).

3. **Module concept.** Recent perturbation studies support a modular view: specific dosage-sensitive loci (e.g., **IFNR cluster**, **DYRK1A**) are necessary for major sub-phenotypes, while other phenotypes arise from additional dosage-sensitive genes, trans effects, and epigenetic remodeling (waugh2023triplicationofthe pages 7-8, lanaelola2024increaseddosageof pages 1-3, maheshwari2024epigeneticsofdown pages 10-11).

---

## Strongest Direct Evidence for the Hypothesis (2023–2024 emphasis)

### A. IFNR locus triplication as a causal interferonopathy module
**Primary perturbation evidence (mouse).** Waugh et al. (Nature Genetics, 2023) used genome editing to normalize the **Ifnr gene cluster** copy number in the **Dp16** DS mouse model. This correction reduced interferon-pathway hyperactivity and was associated with rescue of multiple DS-like phenotypes, including **reduced incidence of heart malformations**, improved developmental milestones, partial rescue of cognitive phenotypes (contextual fear conditioning, Morris water maze), and attenuation of craniofacial and transcriptomic abnormalities (waugh2023triplicationofthe pages 7-8, waugh2023triplicationofthe pages 7-7, waugh2023triplicationofthe pages 28-29). This is among the strongest available *direct tests* of a specific gene-dosage locus driving DS phenotypes.

### B. DYRK1A triplication as a necessary driver of DS-associated CHD with mechanistic chain
**Primary perturbation evidence (mouse; mapped mechanism).** Lana-Elola et al. (Science Translational Medicine, 2024) show that **three copies of Dyrk1a** in the **Dp1Tyb** model are associated with CHD pathology and that **reducing Dyrk1a copy number from three to two rescues heart septation defects**, reversing cardiomyocyte proliferation and mitochondrial respiration deficits (lanaelola2024increaseddosageof pages 1-3, lanaelola2024increaseddosageof pages 6-8). The mechanistic chain is supported by molecular data: DYRK1A overdosage is linked to Cyclin D/RB1/E2F cell-cycle impairment and mitochondrial dysfunction; inhibitor experiments provide partial transcriptional rescue and limited CHD-frequency improvement, consistent with catalytic activity dependence (lanaelola2024increaseddosageof pages 8-9, lanaelola2024increaseddosageof pages 31-33).

### C. Chromosome-scale dosage correction (XIST) demonstrates causality and therapeutic-window logic
**Primary perturbation evidence (human iPSC neurogenesis).** Bansal et al. (Science Advances, 2024) generated isogenic T21 iPSCs with an inducible XIST transgene on one chr21 copy and demonstrated near-euploid repression of chr21 genes, durable silencing, and recruitment of repressive chromatin marks in neural lineages, including terminal neurons and astrocytes (bansal2024adynamicin pages 1-3, bansal2024adynamicin pages 3-3). Functionally, when XIST is induced before the neural progenitor stage, dosage correction suppresses a pronounced T21-associated **astrogenesis bias** (excess astrocytes at expense of neurons), linking neurodevelopmental lineage skew directly to chr21 dosage (bansal2024adynamicin pages 12-13, bansal2024adynamicin pages 9-10).

---

## Evidence that Qualifies, Limits, or Competes with the Hypothesis

### 1. No single “critical region” or single gene explains most phenotypes
Mouse genetics and review synthesis indicate that triplication of a proposed DSCR alone does not recapitulate key traits and that DSCR normalization can normalize certain behaviors, supporting **multigenic dosage and interactions** rather than a single causal interval (murphy2024downsyndromeand pages 6-7). This qualifies simplistic “one-region” versions of the gene-dosage model.

### 2. DYRK1A is necessary but not sufficient for CHD across contexts
Interval comparisons suggest DYRK1A dosage is **necessary** but **not sufficient** for all CHD/mitochondrial phenotypes (e.g., models with Dyrk1a triplication alone lacking CHD), implying at least one additional interacting trisomic locus for full expression of DS-CHD (lanaelola2024increaseddosageof pages 9-11, lanaelola2024increaseddosageof pages 31-33).

### 3. IFNR correction rescues many phenotypes but not all
Even strong single-locus corrections show incomplete rescue of DS-like phenotypes, implying parallel mechanisms beyond interferonopathy and beyond IFNR dosage (waugh2023triplicationofthe pages 7-8, waugh2023triplicationofthe pages 28-29).

### 4. Genome-wide trans dysregulation and epigenetic remodeling
Reviews of fetal tissue expression studies and epigenetics emphasize that DS expression changes occur widely outside chr21 and involve extensive non-21 methylation changes, consistent with trisomy-driven trans effects (chapman2024geneexpressionstudies pages 8-9, maheshwari2024epigeneticsofdown pages 10-11). This does not refute the canonical model (which begins with trisomy) but limits a strictly “direct 1.5× gene expression → phenotype” interpretation.

### 5. IFN-independent heme/hypoxia/stress erythropoiesis program
Donovan et al. (Cell Reports, 2024) report in ~400 DS participants consistent signatures of elevated heme metabolism and hypoxic (HIF1A) signaling with stress erythropoiesis markers (e.g., elevated EPO and GDF15, macrocytosis). Critically, these signatures were **not altered by tofacitinib** and **not attenuated by Ifnr copy-number normalization** in Dp16 mice, arguing for a major trisomy-driven program operating **in parallel** to IFNR/JAK-STAT mechanisms (donovan2024multimodalanalysisof pages 8-10, donovan2024multimodalanalysisof pages 23-29, donovan2024multimodalanalysisof pages 5-6).

---

## Current Applications and Real-World Implementations

1. **Targeting IFNR/JAK-STAT hyperactivity with JAK inhibition (clinical translation).** Rachubinski et al. (eLife, 2024) report an interim analysis of an open-label Phase II tofacitinib trial in DS (ClinicalTrials.gov **NCT04246372**). Among the first **10 participants** completing 16 weeks, treatment reduced interferon transcriptional scores and cytokine scores, decreased thyroid autoantibodies, and improved several autoimmune skin conditions; safety was acceptable with no serious adverse events and no overt immune suppression reported in this interim cohort (rachubinski2024jakinhibitiondecreases pages 14-15, rachubinski2024jakinhibitiondecreases pages 19-21, rachubinski2024jakinhibitiondecreases pages 1-2). This is a real-world implementation of the interferonopathy sub-hypothesis.

2. **DYRK1A as a therapeutic target in DS-CHD (preclinical translation).** Lana-Elola et al. tested pharmacologic inhibition (Leucettinib-21) in pregnancy and observed partial rescue of embryonic transcriptional signatures with an intermediate (non-significant) reduction in CHD frequency, suggesting target engagement but highlighting delivery and multigenic constraints (lanaelola2024increaseddosageof pages 8-9, lanaelola2024increaseddosageof pages 31-33).

3. **Chromosome silencing as a mechanistic tool (and distant therapeutic concept).** Inducible XIST-mediated chr21 silencing in human iPSCs provides a platform for testing which cell types and time windows remain reversible by dosage correction, informing therapeutic-window hypotheses even if whole-chromosome silencing is not currently deployable clinically (bansal2024adynamicin pages 1-1, bansal2024adynamicin pages 1-3).

---

## Relevant Statistics and Recent Data Points

### Immune dysregulation / intervention
- **Tofacitinib trial interim cohort:** 10 completers analyzed over 16 weeks; dosing 5 mg twice daily; improvements reported across autoimmune dermatologic conditions; decreases in IFN and cytokine scores and pathogenic autoantibodies; no serious adverse events in interim cohort (rachubinski2024jakinhibitiondecreases pages 14-15, rachubinski2024jakinhibitiondecreases pages 19-21, rachubinski2024jakinhibitiondecreases pages 15-18).

### Hematopoiesis and leukemia risk (review-synthesized quantitative data)
- **Relative leukemia risks:** AMKL ~**500-fold** increased risk; ALL ~**20-fold** increased risk in children with DS (mason2024downsyndromeassociatedleukaemias pages 1-1).
- **TAM incidence:** **5–30%** of liveborn infants with T21; **80–90%** resolve spontaneously within **3–4 months**; **~20–30%** progress to ML-DS (mason2024downsyndromeassociatedleukaemias pages 1-3, mason2024downsyndromeassociatedleukaemias pages 3-4).
- **Silent TAM:** GATA1-mutant clones detectable in **10–15%** of neonates without blasts; progression to ML-DS **<3%** (mason2024downsyndromeassociatedleukaemias pages 4-6).

### Heme/hypoxia/stress erythropoiesis (large cohort)
- Multi-omic study size: ~**400** participants with DS; reports macrocytosis (↑MCV, ↑MCH) alongside elevated EPO/GDF15 and heme/hypoxia transcriptomic signatures; not corrected by JAK inhibition and not rescued by Ifnr normalization in mice (donovan2024multimodalanalysisof pages 1-3, donovan2024multimodalanalysisof pages 5-6, donovan2024multimodalanalysisof pages 8-10).

### CHD (model-based quantitative)
- In Dp1Tyb embryos, CHD penetrance reported as ~**50% at E14.5** in the model system used for mapping DYRK1A contribution (lanaelola2024increaseddosageof pages 1-3).

---

## Evidence Matrix (artifact)
The following table provides one-row-per-evidence-item provenance, including publication dates and URLs.

| Citation | Publication date | URL | Evidence type | Supports/Refutes/Qualifies/Competing | Mechanistic claim tested | Key finding (1-2 sentences) | Context (tissue/cell type; stage) | Confidence | Limitations |
|---|---|---|---|---|---|---|---|---|---|
| Waugh et al., *Nat Genet* 2023; DOI: 10.1038/s41588-023-01399-7 | 2023-06 | https://doi.org/10.1038/s41588-023-01399-7 | mouse model | Supports | Triplication of the chr21-syntenic IFNR locus is a causal dosage-sensitive driver of major DS phenotypes. | In Dp16 mice, CRISPR normalization of Ifnr copy number reduced interferon-pathway hyperactivity and rescued multiple DS-like phenotypes, including lower CHD incidence, improved developmental milestones, better contextual fear/Morris water maze performance, and attenuation of craniofacial/transcriptomic abnormalities. | Dp16 and Dp16-2xIfnrs mice; embryonic heart (E12.5-E15.5), neonatal development, adult brain/behavior | High | Mouse-only causality test; not all phenotypes were rescued (e.g., some motor deficits), and human causal intervention evidence is indirect. (waugh2023triplicationofthe pages 7-8, waugh2023triplicationofthe pages 7-7, waugh2023triplicationofthe pages 28-29) |
| Lana-Elola et al., *Sci Transl Med* 2024; DOI: 10.1126/scitranslmed.add6883 | 2024-01 | https://doi.org/10.1126/scitranslmed.add6883 | mouse model | Supports | Increased DYRK1A dosage is necessary for DS-associated congenital heart defects via impaired cardiomyocyte proliferation and mitochondrial dysfunction. | In Dp1Tyb embryos, reducing Dyrk1a from 3 to 2 copies rescued septation/AVSD phenotypes and reversed mitochondrial respiration and cell-cycle defects; kinase-dead or inhibitor experiments further implicated DYRK1A catalytic activity. Human fetal DS hearts shared decreased oxidative phosphorylation/E2F-linked signatures. | Dp1Tyb embryonic hearts; cardiomyocytes/endocardial cells; E12.5-E15.5; human fetal DS heart transcriptomic comparison | High | DYRK1A was necessary but not fully sufficient in all mapping contexts, implying additional loci/modifiers; pharmacologic rescue was partial/non-significant. (lanaelola2024increaseddosageof pages 1-3, lanaelola2024increaseddosageof pages 8-9, lanaelola2024increaseddosageof pages 11-13, lanaelola2024increaseddosageof pages 9-11, lanaelola2024increaseddosageof pages 6-8) |
| Bansal et al., *Sci Adv* 2024; DOI: 10.1126/sciadv.adj0385 | 2024-06 | https://doi.org/10.1126/sciadv.adj0385 | iPSC | Supports | Chr21 overdosage directly drives neural lineage stress programs and astrogenic bias; chromosome-scale dosage correction can reverse at least some phenotypes. | Inducible XIST silenced one chr21 copy near-completely in trisomy 21 iPSCs and neural derivatives, shifting transcriptomes toward euploid controls. Early correction rescued excess astrogenesis/neurogenic loss and dampened stress, mitochondrial, apoptotic, translational, and some interferon-related abnormalities. | Human trisomy 21 iPSCs, NPCs, neurons, astrocytes; in vitro neurogenesis and postmitotic stages | High | In vitro system; some chr21 genes showed residual escape/incomplete correction in NPCs and neuronal survival rescue was less clearly demonstrated than lineage rescue. (bansal2024adynamicin pages 11-12, bansal2024adynamicin pages 12-13, bansal2024adynamicin pages 1-1, bansal2024adynamicin pages 1-3, bansal2024adynamicin pages 9-10, bansal2024adynamicin pages 3-3) |
| Rachubinski et al., *eLife* 2024; DOI: 10.7554/eLife.99323 | 2024-12 | https://doi.org/10.7554/eLife.99323 | human clinical | Supports | Trisomy-21-driven IFNR/JAK-STAT hyperactivity is clinically actionable and contributes to autoimmune/inflammatory burden in DS. | In an interim open-label Phase II trial (first 10 completers), tofacitinib lowered whole-blood IFN scores, cytokine scores, and thyroid autoantibodies, while improving several inflammatory skin conditions without serious adverse events or overt immune suppression. | DS participants aged 12-50 years with autoimmune/inflammatory skin disease; blood transcriptome/cytokines/autoantibodies; 16-week treatment | Med-High | Small interim cohort, open-label, no placebo control; tests downstream therapeutic modulation rather than direct chromosome/gene copy-number correction. (rachubinski2024jakinhibitiondecreases pages 18-19, rachubinski2024jakinhibitiondecreases pages 21-22, rachubinski2024jakinhibitiondecreases pages 14-15, rachubinski2024jakinhibitiondecreases pages 19-21, rachubinski2024jakinhibitiondecreases pages 1-2, rachubinski2024jakinhibitiondecreases pages 15-18) |
| Donovan et al., *Cell Rep* 2024; DOI: 10.1016/j.celrep.2024.114599 | 2024-08 | https://doi.org/10.1016/j.celrep.2024.114599 | human omics | Qualifies | Not all DS systemic phenotypes are best explained by IFNR-driven inflammation; additional trisomy-linked pathways affect erythropoiesis/heme/hypoxia biology. | Multi-omic profiling (~400 participants) identified elevated heme metabolism, HIF1A/hypoxia, EPO/GDF15, macrocytosis, and stress erythropoiesis signatures. These persisted despite JAK inhibition and were not rescued by Ifnr copy-number normalization in Dp16, arguing for IFN-independent mechanisms and additional chr21 drivers (e.g., ERG/MAP3K7CL correlations). | Human whole blood/plasma/CBC across lifespan; Dp16 spleen, heart, kidney, embryonic heart | High | Correlative for candidate chr21 genes; no single causal gene established and no direct oxygen-tension or perturbation proof for proposed drivers. (donovan2024multimodalanalysisof pages 8-10, donovan2024multimodalanalysisof pages 10-12, donovan2024multimodalanalysisof pages 6-8, donovan2024multimodalanalysisof pages 3-5, donovan2024multimodalanalysisof pages 23-29, donovan2024multimodalanalysisof pages 1-3, donovan2024multimodalanalysisof pages 5-6) |
| Abukhaled et al., *J Neurol* 2024; DOI: 10.1007/s00415-023-11890-0 | 2024-08 | https://doi.org/10.1007/s00415-023-11890-0 | review | Supports (review-level) | DSCAM and chr21 miRNA dosage contribute to neurodevelopmental/synaptic phenotypes in DS, beyond a purely global aneuploidy effect. | Review summarizes primary data that Ts65Dn interneuron presynaptic overgrowth is rescued by normalizing Dscam dosage, supporting DSCAM as a dosage-sensitive neuronal effector. It also summarizes miR-155 overexpression causing SNX27 downregulation and downstream glutamatergic/NMDA receptor deficits, linking chr21 miRNA dosage to synaptic dysfunction. | Ts65Dn mouse cortex/hippocampus; interneurons and glutamatergic synapses; neurodevelopmental context | Med | Secondary source only here; exact primary-study methods and effect sizes were not directly checked in context. (abukhaled2024understandingthegenetic pages 9-11) |
| Chapman et al., *Int J Mol Sci* 2024; DOI: 10.3390/ijms25052968 | 2024-03 | https://doi.org/10.3390/ijms25052968 | review | Qualifies | DS phenotypes arise from chr21 dosage but are propagated through widespread trans-effects, developmental specificity, and tissue-specific dysregulation. | Review-level synthesis notes that many chr21 genes/miRNAs are overexpressed, but transcriptomic studies show substantial genome-wide dysregulation outside chr21 across fetal tissues and brain regions. It also summarizes evidence for IFNR overexpression, Olig2-driven neurodevelopmental changes, and dataset-specific discordance/heterogeneity. | Human fetal tissues, placenta, brain, cardiac tissue; mouse models including Ts65Dn/Ts1Cje | Med | Review article; integrates older heterogeneous studies and some claims are dataset-dependent rather than uniformly replicated. (chapman2024geneexpressionstudies pages 8-9, chapman2024geneexpressionstudies pages 12-13) |
| Maheshwari & Singh, *Newborn* 2024; DOI: 10.5005/jp-journals-11002-0112 | 2024-12 | https://doi.org/10.5005/jp-journals-11002-0112 | review | Qualifies | The canonical gene-dosage model is modified by genome-wide epigenetic remodeling and tissue-specific methylation effects, not just direct 1.5x expression of chr21 genes. | Review summarizes EWAS data showing most DS-associated DMRs/CpGs occur on non-21 genes, implicating trans-acting epigenetic consequences of trisomy 21. It highlights dosage-sensitive methylation regulators (e.g., DNMT3L) and model-dependent DYRK1A/APP findings, arguing for chromosome-wide and tissue-specific epigenetic propagation of the primary dosage lesion. | Newborn blood, placenta, brain; mouse transgenic models | Med | Review-level evidence; mechanistic links from specific chr21 genes to specific methylation changes remain incompletely proven and can be model-specific. (maheshwari2024epigeneticsofdown pages 10-11) |
| Waugh et al., *Nat Genet* 2023; DOI: 10.1038/s41588-023-01399-7 | 2023-06 | https://doi.org/10.1038/s41588-023-01399-7 | mouse model | Qualifies | IFNR triplication is a major but partial contributor to canonical DS phenotypes rather than a complete explanation of all trisomy-21 effects. | While Ifnr correction attenuated many molecular and organismal phenotypes, rescue was incomplete and some abnormalities persisted, indicating additional trisomic genes and pathways act in parallel or downstream. | Dp16 adult behavior and embryonic heart/brain transcriptomes | High | Strong perturbation evidence, but explicitly shows scope limits of a single-locus explanation. (waugh2023triplicationofthe pages 7-8, waugh2023triplicationofthe pages 28-29) |
| Lana-Elola et al., *Sci Transl Med* 2024; DOI: 10.1126/scitranslmed.add6883 | 2024-01 | https://doi.org/10.1126/scitranslmed.add6883 | mouse model | Qualifies | DYRK1A is a major CHD driver, but CHD in DS is multigenic rather than caused by DYRK1A alone. | The study concluded DYRK1A dosage is necessary but not sufficient in all trisomic intervals, because models with three Dyrk1a copies alone did not fully reproduce CHD/mitochondrial defects, supporting at least one additional interacting locus. | Embryonic mouse heart; interval-mapping across DS mouse models | High | Constrains over-interpretation of single-gene causality within the canonical dosage model. (lanaelola2024increaseddosageof pages 9-11, lanaelola2024increaseddosageof pages 31-33) |


*Table: This table summarizes key supporting and qualifying evidence for the canonical trisomy 21 gene-dosage model in Down syndrome using only studies already present in context. It highlights where direct perturbation data strongly support causality and where newer omics and clinical studies limit the model's scope or point to parallel mechanisms.*

---

## Mechanistic Causal Chain (with evidence strength)

> Trisomy 21 / segmental Hsa21 ortholog triplication -> increased dosage of multiple chr21 genes and regulatory elements -> multisystem dysregulation model foundation [Strong for chromosomal cause; Strong for broad dosage correction effects in iPSC model] (bansal2024adynamicin pages 1-1, bansal2024adynamicin pages 1-3)
>
> Branch A: IFNR locus triplication -> increased IFN receptor expression -> heightened IFN-alpha/IFN-gamma signaling and JAK/STAT activation [Strong, direct copy-number correction in Dp16] (waugh2023triplicationofthe pages 3-4, waugh2023triplicationofthe pages 7-8, waugh2023triplicationofthe pages 7-7)
>
> Branch A: heightened IFN/JAK/STAT signaling -> chronic hypercytokinemia, immune remodeling, autoantibodies, autoimmune skin disease burden [Moderate in humans; strengthened by downstream therapeutic response] (rachubinski2024jakinhibitiondecreases pages 18-19, rachubinski2024jakinhibitiondecreases pages 21-22, rachubinski2024jakinhibitiondecreases pages 14-15, rachubinski2024jakinhibitiondecreases pages 19-21, rachubinski2024jakinhibitiondecreases pages 1-2)
>
> Branch A: IFNR-driven signaling in embryonic heart -> EMT/MYC/interferon transcriptional dysregulation and reduced proliferation -> increased congenital heart malformations [Strong in Dp16 with genetic rescue] (waugh2023triplicationofthe pages 7-8, waugh2023triplicationofthe pages 7-7)
>
> Branch A: IFNR-driven signaling in development/brain -> neonatal developmental delay, cognitive deficits, craniofacial abnormalities [Strong for contribution, but incomplete rescue indicates partial mechanism] (waugh2023triplicationofthe pages 7-8, waugh2023triplicationofthe pages 28-29)
>
> Branch B: DYRK1A triplication -> increased DYRK1A kinase activity/autophosphorylation [Strong] (lanaelola2024increaseddosageof pages 8-9, lanaelola2024increaseddosageof pages 6-8)
>
> Branch B: increased DYRK1A activity -> cyclin D loss, reduced RB1 phosphorylation, reduced E2F target expression, impaired G1-S progression [Strong in embryonic heart] (lanaelola2024increaseddosageof pages 8-9, lanaelola2024increaseddosageof pages 4-6, lanaelola2024increaseddosageof pages 11-13)
>
> Branch B: increased DYRK1A activity -> mitochondrial dysfunction, reduced membrane potential/respiration, abnormal morphology [Strong in Dp1Tyb heart] (lanaelola2024increaseddosageof pages 8-9, lanaelola2024increaseddosageof pages 4-6)
>
> Branch B: cell-cycle and mitochondrial defects -> septation defects / AVSD-spectrum congenital heart disease [Strong, genetic rescue by reducing Dyrk1a from 3 to 2 copies; kinase-dead allele protective] (lanaelola2024increaseddosageof pages 1-3, lanaelola2024increaseddosageof pages 11-13, lanaelola2024increaseddosageof pages 31-33, lanaelola2024increaseddosageof pages 6-8)
>
> Branch B: DYRK1A overdosage in hippocampal/cognitive circuits -> altered AMPAR signaling and associative-memory dysfunction [Moderate from region-specific mouse studies; direct rescue evidence exists at review level] (murphy2024downsyndromeand pages 6-7, canonica2024dissectingthecontribution pages 11-12, canonica2024dissectingthecontribution pages 8-11)
>
> Branch B qualifier: DYRK1A is necessary but not sufficient for all CHD/cognitive phenotypes; at least one additional trisomic locus is required [Strong qualifier] (lanaelola2024increaseddosageof pages 9-11, lanaelola2024increaseddosageof pages 31-33)
>
> Branch C: chr21-wide overdosage -> suppressed translation/ribosomal programs, mitochondrial pathway suppression, cellular stress/apoptotic activation in T21 iPSCs and neural lineages [Strong with inducible XIST correction] (bansal2024adynamicin pages 11-12, bansal2024adynamicin pages 1-1, bansal2024adynamicin pages 1-3)
>
> Branch C: chr21-wide dosage imbalance in neural progenitors -> shift from neurogenesis toward astrogenesis / excess astrocyte output at neuronal expense [Strong when corrected before NPC stage] (bansal2024adynamicin pages 12-13, bansal2024adynamicin pages 1-1, bansal2024adynamicin pages 1-3, bansal2024adynamicin pages 9-10)
>
> Branch C: persistent postmitotic chr21 repression is feasible, but full reversal of mature neuronal dysfunction remains incompletely shown [Moderate] (bansal2024adynamicin pages 11-12, bansal2024adynamicin pages 8-9, bansal2024adynamicin pages 3-3)
>
> Branch D: trisomy 21 in fetal hematopoiesis -> abnormal fetal liver hematopoietic stem/progenitor differentiation biased toward erythroid/megakaryocytic lineages with reduced B/NK output [Moderate, largely review-synthesized human/model evidence] (mason2024downsyndromeassociatedleukaemias pages 1-3, mason2024downsyndromeassociatedleukaemias pages 1-1, mason2024downsyndromeassociatedleukaemias pages 20-21)
>
> Branch D: trisomic hematopoietic context -> acquisition/selection of GATA1s-mutant clones -> transient abnormal myelopoiesis (TAM) [Moderate; GATA1s is an obligate early event, but mutation-acquisition mechanism remains unclear] (mason2024downsyndromeassociatedleukaemias pages 4-6, mason2024downsyndromeassociatedleukaemias pages 1-3, mason2024downsyndromeassociatedleukaemias pages 3-4, mason2024downsyndromeassociatedleukaemias pages 21-22)
>
> Branch D: TAM -> spontaneous resolution in most infants but progression in a subset -> ML-DS [Moderate with quantitative clinical support: TAM resolves in ~80-90%; ~20-30% of clinical TAM progresses] (mason2024downsyndromeassociatedleukaemias pages 4-6, mason2024downsyndromeassociatedleukaemias pages 1-3, mason2024downsyndromeassociatedleukaemias pages 3-4)
>
> Branch D: GATA1s clone persistence + additional hits (cohesin lesions, JAK pathway lesions, epigenetic regulators, miR-125b-2/ERG cooperation) -> ML-DS [Moderate] (mason2024downsyndromeassociatedleukaemias pages 4-6, mason2024downsyndromeassociatedleukaemias pages 1-3, mason2024downsyndromeassociatedleukaemias pages 3-4, mason2024downsyndromeassociatedleukaemias pages 20-21, mason2024downsyndromeassociatedleukaemias pages 21-22)
>
> Branch E: trisomy 21 -> elevated heme metabolism and HIF1A/hypoxia signatures, increased EPO/GDF15, macrocytosis, stress erythropoiesis [Moderate in large human multi-omics; modeled in Dp16] (donovan2024multimodalanalysisof pages 10-12, donovan2024multimodalanalysisof pages 6-8, donovan2024multimodalanalysisof pages 3-5, donovan2024multimodalanalysisof pages 23-29, donovan2024multimodalanalysisof pages 1-3, donovan2024multimodalanalysisof pages 5-6)
>
> Branch E: candidate chr21 dosage contributors to heme/hypoxia program (ERG, MAP3K7CL, ABCC13, TFF3; APP/BACE2-linked associations) -> altered erythroid regulation/hypoxic response [Weak to Moderate; correlation-based, no single causal driver confirmed] (donovan2024multimodalanalysisof pages 8-10, donovan2024multimodalanalysisof pages 10-12, donovan2024multimodalanalysisof pages 6-8)
>
> Branch E: heme/hypoxia/stress erythropoiesis program appears largely independent of IFNR-JAK hyperactivity because it is not corrected by tofacitinib or Ifnr normalization [Strong qualifier / competing downstream branch] (donovan2024multimodalanalysisof pages 8-10, donovan2024multimodalanalysisof pages 23-29, donovan2024multimodalanalysisof pages 1-3)
>
> Global qualifier: a single DS critical region is insufficient; multiple trisomic regions and gene-gene interactions/compensation shape phenotype expression across tissues and aging [Moderate to Strong, depending on model] (murphy2024downsyndromeand pages 7-9, murphy2024downsyndromeand pages 6-7, murphy2024downsyndromeand pages 4-6, canonica2024dissectingthecontribution pages 11-12, canonica2024dissectingthecontribution pages 8-11)


*Blockquote: This blockquote maps the canonical trisomy 21 gene-dosage hypothesis into major mechanistic branches and labels each causal link by evidentiary strength. It is useful for distinguishing well-supported perturbation-backed edges from review-level or correlation-based links that remain unresolved.*

---

## Alternative / Competing (or Complementary) Models
These are best interpreted as **modules** that compete for explanatory primacy for specific DS features, rather than mutually exclusive etiologies.

1. **IFNR-driven interferonopathy model (submodule of gene dosage).** IFNR triplication is necessary for multiple DS-like phenotypes in Dp16 mice and is therapeutically actionable via JAK inhibition in humans (waugh2023triplicationofthe pages 7-8, rachubinski2024jakinhibitiondecreases pages 19-21).

2. **DYRK1A-centered mitochondrial/cell-cycle dysfunction model (CHD-focused submodule).** DYRK1A triplication impairs cardiomyocyte proliferation and mitochondrial function via RB/E2F-linked programs and is necessary for CHD in Dp1Tyb (lanaelola2024increaseddosageof pages 8-9, lanaelola2024increaseddosageof pages 6-8). This model is more parsimonious than broad “all genes contribute equally” for DS-CHD, but is incomplete because additional loci are required (lanaelola2024increaseddosageof pages 9-11).

3. **Genome-wide trans-dysregulation / epigenetic remodeling model.** Trisomy triggers non-21 transcriptomic and methylation changes; epigenetic regulators on chr21 (e.g., DNMT3L as nominated in reviews) are proposed propagators, implying phenotype mechanisms extend beyond simple 1.5× expression for each trisomic gene (chapman2024geneexpressionstudies pages 8-9, maheshwari2024epigeneticsofdown pages 10-11).

4. **IFN-independent oxygen/erythropoiesis stress model.** DS exhibits a robust heme/hypoxia/stress-erythropoiesis signature independent of IFNR/JAK modulation, suggesting an additional core axis of trisomy-driven physiology (donovan2024multimodalanalysisof pages 8-10, donovan2024multimodalanalysisof pages 23-29).

5. **Distributed multigenic/epistatic architecture vs DSCR.** Mouse genetic evidence favors distributed gene dosage with epistasis/compensation over a single critical region, offering a competing framing to narrow DSCR-centric claims (murphy2024downsyndromeand pages 6-7).

---

## Knowledge Gaps (explicit) and Discriminating Tests

| Gap (missing edge/uncertainty) | Why it matters | What evidence checked | What is currently supported | What would resolve it (specific experiment/cohort/assay) | Priority |
|---|---|---|---|---|---|
| Incomplete rescue after IFNR copy-number correction | Tests whether IFNR triplication is a core driver or only one major branch of trisomy-21 pathobiology | Dp16 Ifnr normalization rescued CHD incidence, developmental delay, cognition, craniofacial abnormalities, and many transcriptomic changes, but some motor/other phenotypes persisted (waugh2023triplicationofthe pages 7-8, waugh2023triplicationofthe pages 7-7, waugh2023triplicationofthe pages 28-29) | IFNR dosage is causal for a substantial subset of DS phenotypes, but not sufficient to explain all systemic manifestations | Factorial genetics in Dp16 combining Ifnr normalization with correction of candidate parallel loci (e.g., Dyrk1a, App, Erg-containing intervals), plus multi-tissue single-cell RNA-seq/proteomics and longitudinal phenotyping | High |
| DYRK1A is necessary but not sufficient for congenital heart defects | Directly affects how strongly the canonical model can attribute DS-CHD to a single dosage-sensitive gene | Dyrk1a reduction rescues proliferation/mitochondrial defects and CHD in Dp1Tyb; kinase activity is required; however, Ts1Rhr/interval-mapping data imply additional locus/loci are needed (lanaelola2024increaseddosageof pages 1-3, lanaelola2024increaseddosageof pages 8-9, lanaelola2024increaseddosageof pages 11-13, lanaelola2024increaseddosageof pages 9-11, lanaelola2024increaseddosageof pages 31-33, lanaelola2024increaseddosageof pages 6-8) | Strong support that DYRK1A is a major necessary effector for a CHD program involving RB/E2F and mitochondrial dysfunction, but CHD remains multigenic | Fine-mapping by combinatorial interval engineering on Dp1Tyb background, CRISPR correction of top second-locus candidates in cardiac progenitors, and human fetal heart organoid perturb-seq with DYRK1A dosage titration ± candidate partner genes | High |
| Timing dependence of chr21-wide dosage correction and reversibility in postmitotic neural cells | Distinguishes developmental-lock-in models from persistent cell-autonomous dosage models and guides therapeutic windows | Inducible XIST in T21 iPSCs/NPCs/neurons robustly represses one chr21 copy and rescues astrogenic bias when induced before NPC stage; postmitotic repression is feasible, but extent of phenotypic reversibility in mature neurons is less clear (bansal2024adynamicin pages 11-12, bansal2024adynamicin pages 12-13, bansal2024adynamicin pages 1-1, bansal2024adynamicin pages 1-3, bansal2024adynamicin pages 8-9, bansal2024adynamicin pages 9-10, bansal2024adynamicin pages 3-3) | Early developmental lineage skew is dosage-sensitive and preventable; transcriptomic correction in mature cells is possible, but full rescue of survival/synaptic physiology after late correction remains unproven | Stage-staggered XIST induction in matched cortical assembloids and long-term neuronal cultures with electrophysiology, synapse imaging, live-cell survival, and single-cell multiome profiling before/after late correction | High |
| Residual escape/incomplete correction of some chr21 genes after XIST silencing | Limits interpretation of chromosome-wide correction as a definitive test of dosage causality | XIST silencing is near-complete overall, but some genes show residual excess expression or allelic escape depending on locus/cell state, including NPC contexts (bansal2024adynamicin pages 12-13, bansal2024adynamicin pages 3-4, bansal2024adynamicin pages 3-3) | Most chr21 dosage can be normalized, but not uniformly across all loci and differentiation states | Allele-specific long-read RNA-seq + CUT&Tag/CUT&RUN for XIST-associated marks across differentiation, followed by targeted CRISPRi of persistent escapees to test whether residual phenotypes depend on them | Med |
| IFN-independent heme/hypoxia/stress-erythropoiesis signatures | Challenges the idea that immune/interferon dysregulation is the dominant downstream mechanism for systemic DS phenotypes | Human multi-omics and Dp16 studies show elevated Heme/HIF1A/EPO/GDF15/macrocytosis signatures; these were not corrected by tofacitinib or Ifnr dosage normalization (donovan2024multimodalanalysisof pages 8-10, donovan2024multimodalanalysisof pages 10-12, donovan2024multimodalanalysisof pages 6-8, donovan2024multimodalanalysisof pages 3-5, donovan2024multimodalanalysisof pages 23-29, donovan2024multimodalanalysisof pages 1-3, donovan2024multimodalanalysisof pages 5-6) | Heme/hypoxia biology is a parallel trisomy-21 consequence, largely independent of IFNR-JAK hyperactivity | Prospective DS cohort integrating CBC, reticulocytes, EPO/GDF15, tissue oxygenation markers, and erythroid single-cell profiling; in parallel, gene-specific perturbation of correlated chr21 candidates in human erythroid differentiation systems and Dp16-derived HSPCs | High |
| Unclear causal drivers among correlated chr21 genes for erythroid/hypoxia phenotypes (e.g., ERG, MAP3K7CL, ABCC13, APP/BACE2 associations) | Correlation without causation leaves the canonical gene-dosage chain incomplete | Correlation analyses nominate ABCC13, ERG, MAP3K7CL, TFF3, APP/BACE2-linked associations; no single driver was established, and ABCC13 lacks a murine paralog (donovan2024multimodalanalysisof pages 8-10, donovan2024multimodalanalysisof pages 10-12, donovan2024multimodalanalysisof pages 6-8, donovan2024multimodalanalysisof pages 3-5) | Candidate-driver set has been narrowed, especially toward ERG/MAP3K7CL for Dp16-compatible testing, but source-to-target links remain unresolved | Pooled CRISPR dose-normalization/activation screen of chr21 candidates in T21 iPSC-derived erythroid progenitors with readouts for HIF1A score, fetal globin, colony output, mitochondrial respiration, and macrocytosis-like cell metrics; orthogonal in vivo Dp16 allele correction | High |
| Limitations of Ts65Dn as a mechanistic gold standard | Important because many canonical claims derive from Ts65Dn, yet model genetics may misattribute phenotypes | Reviews note Ts65Dn includes non-Hsa21 orthologs on Mmu17 and omits some human trisomic genes; some seizure/cognition findings may be confounded; newer models (TcMAC21, Dp1Tyb/Dp16, region-specific duplications) show differing phenotype spectra (stafstrom2024infantilespasmsin pages 13-14, murphy2024downsyndromeand pages 6-7, murphy2024downsyndromeand pages 4-6, canonica2024dissectingthecontribution pages 11-12, canonica2024dissectingthecontribution pages 8-11, canonica2024dissectingthecontribution pages 1-2, canonica2024dissectingthecontribution pages 2-3) | Ts65Dn remains useful but cannot alone validate gene-to-phenotype edges for human DS; region-specific and transchromosomic models provide necessary triangulation | Cross-model harmonized phenotyping and single-cell atlas across Ts65Dn, Dp16, Dp1Tyb, TcMAC21, and interval models, with genotype-aware mediation analysis to identify reproducible vs model-specific mechanisms | High |
| Whether a single Down syndrome critical region (DSCR) exists | Determines whether the canonical model should remain phrased as broad dosage imbalance versus focal critical-region causality | Review synthesis cites Ts1Rhr and rescue experiments showing DSCR triplication alone does not recapitulate full phenotypes and normalization can restore some traits, supporting epistasis/multi-gene effects instead of a single region (murphy2024downsyndromeand pages 7-9, murphy2024downsyndromeand pages 6-7, murphy2024downsyndromeand pages 4-6) | Evidence favors distributed dosage imbalance and gene-gene interaction over a single narrow DSCR | Systematic combinatorial duplication/correction across all Hsa21-syntenic intervals with standardized phenome and transcriptome readouts, analyzed for additivity vs epistasis | Med |
| Which Hsa21-syntenic regions explain which cognitive phenotypes across aging | Needed to subtype neurocognitive mechanisms instead of treating DS cognition as one unified pathway | Dp1Tyb (Mmu16) mainly affects object-in-place/hippocampal associative memory with elevated DYRK1A and altered AMPAR signaling; Dp(10)2Yey shows age-dependent novelty-memory decline; Dp(17)3Yey shows little deficit (canonica2024dissectingthecontribution pages 11-12, canonica2024dissectingthecontribution pages 8-11, canonica2024dissectingthecontribution pages 1-2, canonica2024dissectingthecontribution pages 2-3) | Cognitive dysfunction is region- and age-specific rather than attributable to one uniform trisomic mechanism | Longitudinal cross-model behavioral, circuit, and synaptosome proteomics from youth to aging, plus targeted normalization of Dyrk1a and Mmu10 candidates in the relevant interval backgrounds | Med |
| Mechanism by which trisomy 21 promotes acquisition of GATA1 mutations in TAM/ML-DS | Central missing causal step in the leukemia branch of the canonical model | Reviews state trisomy 21 perturbs fetal hematopoiesis and GATA1s is an obligate/early event, but exact mechanism of mutation acquisition remains unknown; additional hits (cohesin/JAK/epigenetic lesions, miR-125b-2) are implicated (mason2024downsyndromeassociatedleukaemias pages 4-6, mason2024downsyndromeassociatedleukaemias pages 1-3, mason2024downsyndromeassociatedleukaemias pages 3-4, mason2024downsyndromeassociatedleukaemias pages 20-21, mason2024downsyndromeassociatedleukaemias pages 21-22) | Multi-step model is supported: T21 fetal hematopoietic context → GATA1-mutant clones/TAM → additional hits → ML-DS, but mutation-origin mechanism is unconfirmed | Deep sequencing of prenatal and neonatal DS hematopoietic compartments, single-cell DNA+RNA lineage tracing, mutational signature analysis, and T21 fetal-liver organoid/iPSC models testing DYRK1A/ERG/RUNX1/oxidative-stress perturbations for GATA1 mutation rate or clonal selection | High |
| TAM diagnostic thresholds and risk stratification remain unsettled | Directly affects clinical interpretation of the hematopoietic arm of the model and biomarker implementation | Reviews report variable TAM definitions (>5% vs >10% blasts), silent TAM in 10–15%, clinical TAM progression ~20–30%, silent TAM progression <3%, and MRD at 12 weeks as predictive (mason2024downsyndromeassociatedleukaemias pages 4-6, mason2024downsyndromeassociatedleukaemias pages 1-3, mason2024downsyndromeassociatedleukaemias pages 3-4, mason2024downsyndromeassociatedleukaemias pages 1-1) | T21 + GATA1-mutant clone burden predicts leukemic risk, but diagnostic cutoffs and best biomarkers are not standardized | International prospective neonatal DS registry with uniform flow cytometry, GATA1 ultra-deep sequencing, MRD, and linked outcomes to derive evidence-based thresholds and risk models | High |
| How specific chr21 genes generate genome-wide epigenetic remodeling | Needed to connect primary trisomy to broad trans effects seen outside chr21 | Reviews summarize extensive non-chr21 DMRs/CpGs and nominate DNMT3L, N6AMT1, MIS18A, CBS/folate-SAM genes; direct mechanistic proof linking specific dosage-sensitive genes to tissue-specific methylation remains weak/model-dependent (maheshwari2024epigeneticsofdown pages 10-11, chapman2024geneexpressionstudies pages 8-9) | Strong evidence for widespread epigenetic remodeling in DS, weak evidence for exact upstream chr21 drivers and tissue-specific paths | Isogenic T21 human cell systems with single-gene dosage normalization (DNMT3L, CBS, DYRK1A, etc.) followed by methylome, hydroxymethylome, chromatin accessibility, and transcriptome profiling across blood, placenta-, brain-, and cardiac-lineage cells | High |
| Extent to which immune phenotypes in humans are directly due to IFNR copy number rather than broader trisomic immune remodeling | Important for judging whether IFNR is an alternative model or a submodule of the canonical model | Human DS shows constitutive hypercytokinemia and high IFN/JAK-STAT activity; tofacitinib lowers IFN/cytokine/autoantibody scores and improves skin autoimmunity, but this is a downstream intervention rather than direct IFNR gene correction in humans (rachubinski2024jakinhibitiondecreases pages 18-19, rachubinski2024jakinhibitiondecreases pages 21-22, rachubinski2024jakinhibitiondecreases pages 14-15, rachubinski2024jakinhibitiondecreases pages 19-21, rachubinski2024jakinhibitiondecreases pages 1-2, rachubinski2024jakinhibitiondecreases pages 6-7, rachubinski2024jakinhibitiondecreases pages 15-18) | Human data strongly support functional IFN-JAK dependence of part of the immune phenotype, but do not isolate IFNR copy number as the sole upstream cause in patients | Ex vivo human DS immune-cell CRISPR dose-normalization of IFNAR1/IFNAR2/IFNGR2/IL10RB with phospho-STAT, cytokine, and autoantibody-support assays; genotype-stratified clinical correlation of IFNR expression with outcomes | Med |
| APP/DYRK1A/other chr21 contributors to neurodegeneration vs development are not cleanly separated | Matters for whether early developmental and late neurodegenerative DS phenotypes share one dosage chain | Reviews and neuronal transcriptome studies implicate APP triplication, DYRK1A overexpression, and broad stress/neurodegeneration programs, but the relative contribution of each to developmental ID vs age-related degeneration remains unresolved in current context (murphy2024downsyndromeand pages 6-7, bansal2024adynamicin pages 11-12, alldred2024analysisofmicroisolated pages 1-6) | APP and DYRK1A remain strong candidates, but causal partitioning across life stages is incomplete | Longitudinal human iPSC and mouse studies with temporally controlled correction of APP vs DYRK1A dosage, measuring neurogenesis, synaptic physiology, amyloid/tau biology, and neuronal vulnerability over time | Med |


*Table: This table summarizes the main unresolved causal steps and scope limits for the canonical trisomy 21 gene-dosage model in Down syndrome. It also proposes specific experiments, cohorts, and assays that would most efficiently distinguish core dosage effects from parallel or downstream mechanisms.*

---

## Curation Leads (curator-verification required)

### Candidate evidence references to add/strengthen KB edges (with snippets to verify)
1. **IFNR copy-number correction rescues DS phenotypes (mouse causal evidence).**
   - Waugh et al. 2023 Nature Genetics (DOI: 10.1038/s41588-023-01399-7; 2023-06; https://doi.org/10.1038/s41588-023-01399-7). Candidate KB edges: *IFNR triplication → IFN hyperactivity/JAK-STAT activation → CHD/developmental delay/cognition/craniofacial phenotypes*; edge strength “strong” due to genetic correction (waugh2023triplicationofthe pages 7-8, waugh2023triplicationofthe pages 7-7).

2. **DYRK1A dosage causality for CHD via mitochondria/cell cycle.**
   - Lana-Elola et al. 2024 Science Translational Medicine (DOI: 10.1126/scitranslmed.add6883; 2024-01; https://doi.org/10.1126/scitranslmed.add6883). Candidate KB edges: *DYRK1A triplication → RB/E2F cell-cycle suppression → reduced cardiomyocyte proliferation → septation defects* and *DYRK1A triplication → mitochondrial dysfunction → CHD*; qualifier edge: *DYRK1A necessary but not sufficient* (lanaelola2024increaseddosageof pages 8-9, lanaelola2024increaseddosageof pages 9-11).

3. **Chr21-wide dosage correction rescues neurogenesis lineage skew.**
   - Bansal et al. 2024 Science Advances (DOI: 10.1126/sciadv.adj0385; 2024-06; https://doi.org/10.1126/sciadv.adj0385). Candidate KB edges: *chr21 dosage → stress/translation/mitochondrial suppression → neurogenesis-to-astrogenesis shift*; timing constraint: *early correction required for lineage outcome* (bansal2024adynamicin pages 12-13, bansal2024adynamicin pages 1-1).

4. **Human clinical translation of IFN/JAK module.**
   - Rachubinski et al. 2024 eLife (DOI: 10.7554/eLife.99323; 2024-12; https://doi.org/10.7554/elife.99323). Candidate KB clinical evidence: *JAK inhibition reduces IFN signature/cytokines/autoantibodies and improves autoimmune skin outcomes in DS*; Trial: **NCT04246372** (rachubinski2024jakinhibitiondecreases pages 14-15, rachubinski2024jakinhibitiondecreases pages 1-2).

5. **IFN-independent heme/hypoxia axis as parallel mechanism.**
   - Donovan et al. 2024 Cell Reports (DOI: 10.1016/j.celrep.2024.114599; 2024-08; https://doi.org/10.1016/j.celrep.2024.114599). Candidate KB module: *T21 → heme metabolism + HIF1A/hypoxia + stress erythropoiesis + macrocytosis; independent of IFNR/JAK* (donovan2024multimodalanalysisof pages 8-10, donovan2024multimodalanalysisof pages 5-6).

### Candidate ontology terms (leads)
- **Cell types:** cardiomyocyte; endocardial cell; neural progenitor cell; astrocyte; excitatory neuron; hematopoietic stem/progenitor cell; megakaryocyte progenitor.
- **Biological processes:** interferon signaling; JAK/STAT signaling; epithelial–mesenchymal transition; G1/S transition; mitochondrial oxidative phosphorylation; stress erythropoiesis; hypoxia/HIF1A signaling; DNA methylation.

### Candidate subtype restrictions / constraints
- **CHD:** multigenic; DYRK1A necessary but requires additional locus/loci for full penetrance (lanaelola2024increaseddosageof pages 9-11).
- **Immune/autoimmune manifestations:** enriched in individuals with high IFN/JAK activity; modifiable by JAK inhibition (rachubinski2024jakinhibitiondecreases pages 19-21).
- **Hematologic oxygen-related phenotypes:** appear not driven by IFNR dosage; treat as parallel module (donovan2024multimodalanalysisof pages 8-10).

---

## Summary
Direct perturbation studies in 2023–2024 strongly support the canonical DS gene-dosage model but also refine it into **multiple interacting dosage-sensitive modules** (IFNR/interferonopathy; DYRK1A/cell cycle–mitochondria; chr21-wide stress/translation/mitochondria programs) alongside **parallel IFN-independent systemic programs** (heme/hypoxia/stress erythropoiesis). The key curation need is to encode these as explicit branches with evidence strength and known scope limits, rather than as a single undifferentiated “all chr21 genes contribute equally” mechanism (waugh2023triplicationofthe pages 7-8, lanaelola2024increaseddosageof pages 8-9, bansal2024adynamicin pages 12-13, donovan2024multimodalanalysisof pages 8-10).


References

1. (waugh2023triplicationofthe pages 7-8): Katherine A. Waugh, Ross Minter, Jessica Baxter, Congwu Chi, Matthew D. Galbraith, Kathryn D. Tuttle, Neetha P. Eduthan, Kohl T. Kinning, Zdenek Andrysik, Paula Araya, Hannah Dougherty, Lauren N. Dunn, Michael Ludwig, Kyndal A. Schade, Dayna Tracy, Keith P. Smith, Ross E. Granrath, Nicolas Busquet, Santosh Khanal, Ryan D. Anderson, Liza L. Cox, Belinda Enriquez Estrada, Angela L. Rachubinski, Hannah R. Lyford, Eleanor C. Britton, Katherine A. Fantauzzo, David J. Orlicky, Jennifer L. Matsuda, Kunhua Song, Timothy C. Cox, Kelly D. Sullivan, and Joaquin M. Espinosa. Triplication of the interferon receptor locus contributes to hallmarks of down syndrome in a mouse model. Nature Genetics, 55:1034-1047, Jun 2023. URL: https://doi.org/10.1038/s41588-023-01399-7, doi:10.1038/s41588-023-01399-7. This article has 92 citations and is from a highest quality peer-reviewed journal.

2. (waugh2023triplicationofthe pages 7-7): Katherine A. Waugh, Ross Minter, Jessica Baxter, Congwu Chi, Matthew D. Galbraith, Kathryn D. Tuttle, Neetha P. Eduthan, Kohl T. Kinning, Zdenek Andrysik, Paula Araya, Hannah Dougherty, Lauren N. Dunn, Michael Ludwig, Kyndal A. Schade, Dayna Tracy, Keith P. Smith, Ross E. Granrath, Nicolas Busquet, Santosh Khanal, Ryan D. Anderson, Liza L. Cox, Belinda Enriquez Estrada, Angela L. Rachubinski, Hannah R. Lyford, Eleanor C. Britton, Katherine A. Fantauzzo, David J. Orlicky, Jennifer L. Matsuda, Kunhua Song, Timothy C. Cox, Kelly D. Sullivan, and Joaquin M. Espinosa. Triplication of the interferon receptor locus contributes to hallmarks of down syndrome in a mouse model. Nature Genetics, 55:1034-1047, Jun 2023. URL: https://doi.org/10.1038/s41588-023-01399-7, doi:10.1038/s41588-023-01399-7. This article has 92 citations and is from a highest quality peer-reviewed journal.

3. (waugh2023triplicationofthe pages 28-29): Katherine A. Waugh, Ross Minter, Jessica Baxter, Congwu Chi, Matthew D. Galbraith, Kathryn D. Tuttle, Neetha P. Eduthan, Kohl T. Kinning, Zdenek Andrysik, Paula Araya, Hannah Dougherty, Lauren N. Dunn, Michael Ludwig, Kyndal A. Schade, Dayna Tracy, Keith P. Smith, Ross E. Granrath, Nicolas Busquet, Santosh Khanal, Ryan D. Anderson, Liza L. Cox, Belinda Enriquez Estrada, Angela L. Rachubinski, Hannah R. Lyford, Eleanor C. Britton, Katherine A. Fantauzzo, David J. Orlicky, Jennifer L. Matsuda, Kunhua Song, Timothy C. Cox, Kelly D. Sullivan, and Joaquin M. Espinosa. Triplication of the interferon receptor locus contributes to hallmarks of down syndrome in a mouse model. Nature Genetics, 55:1034-1047, Jun 2023. URL: https://doi.org/10.1038/s41588-023-01399-7, doi:10.1038/s41588-023-01399-7. This article has 92 citations and is from a highest quality peer-reviewed journal.

4. (lanaelola2024increaseddosageof pages 1-3): Eva Lana-Elola, Rifdat Aoidi, Miriam Llorian, Dorota Gibbins, Callan Buechsenschuetz, Claudio Bussi, Helen Flynn, Tegan Gilmore, Sheona Watson-Scales, Marie Haugsten Hansen, Darryl Hayward, Ok-Ryul Song, Véronique Brault, Yann Herault, Emmanuel Deau, Laurent Meijer, Ambrosius P. Snijders, Maximiliano G. Gutierrez, Elizabeth M. C. Fisher, and Victor L. J. Tybulewicz. Increased dosage of dyrk1a leads to congenital heart defects in a mouse model of down syndrome. Science translational medicine, 16:eadd6883-eadd6883, Jan 2024. URL: https://doi.org/10.1126/scitranslmed.add6883, doi:10.1126/scitranslmed.add6883. This article has 48 citations and is from a highest quality peer-reviewed journal.

5. (lanaelola2024increaseddosageof pages 8-9): Eva Lana-Elola, Rifdat Aoidi, Miriam Llorian, Dorota Gibbins, Callan Buechsenschuetz, Claudio Bussi, Helen Flynn, Tegan Gilmore, Sheona Watson-Scales, Marie Haugsten Hansen, Darryl Hayward, Ok-Ryul Song, Véronique Brault, Yann Herault, Emmanuel Deau, Laurent Meijer, Ambrosius P. Snijders, Maximiliano G. Gutierrez, Elizabeth M. C. Fisher, and Victor L. J. Tybulewicz. Increased dosage of dyrk1a leads to congenital heart defects in a mouse model of down syndrome. Science translational medicine, 16:eadd6883-eadd6883, Jan 2024. URL: https://doi.org/10.1126/scitranslmed.add6883, doi:10.1126/scitranslmed.add6883. This article has 48 citations and is from a highest quality peer-reviewed journal.

6. (lanaelola2024increaseddosageof pages 6-8): Eva Lana-Elola, Rifdat Aoidi, Miriam Llorian, Dorota Gibbins, Callan Buechsenschuetz, Claudio Bussi, Helen Flynn, Tegan Gilmore, Sheona Watson-Scales, Marie Haugsten Hansen, Darryl Hayward, Ok-Ryul Song, Véronique Brault, Yann Herault, Emmanuel Deau, Laurent Meijer, Ambrosius P. Snijders, Maximiliano G. Gutierrez, Elizabeth M. C. Fisher, and Victor L. J. Tybulewicz. Increased dosage of dyrk1a leads to congenital heart defects in a mouse model of down syndrome. Science translational medicine, 16:eadd6883-eadd6883, Jan 2024. URL: https://doi.org/10.1126/scitranslmed.add6883, doi:10.1126/scitranslmed.add6883. This article has 48 citations and is from a highest quality peer-reviewed journal.

7. (bansal2024adynamicin pages 12-13): Prakhar Bansal, Erin C. Banda, Heather R. Glatt-Deeley, Christopher E. Stoddard, Jeremy W. Linsley, Neha Arora, Cécile Deleschaux, Darcy T. Ahern, Yuvabharath Kondaveeti, Rachael E. Massey, Michael Nicouleau, Shijie Wang, Miguel Sabariego-Navarro, Mara Dierssen, Steven Finkbeiner, and Stefan F. Pinter. A dynamic in vitro model of down syndrome neurogenesis with trisomy 21 gene dosage correction. Science Advances, Jun 2024. URL: https://doi.org/10.1126/sciadv.adj0385, doi:10.1126/sciadv.adj0385. This article has 15 citations and is from a highest quality peer-reviewed journal.

8. (bansal2024adynamicin pages 1-1): Prakhar Bansal, Erin C. Banda, Heather R. Glatt-Deeley, Christopher E. Stoddard, Jeremy W. Linsley, Neha Arora, Cécile Deleschaux, Darcy T. Ahern, Yuvabharath Kondaveeti, Rachael E. Massey, Michael Nicouleau, Shijie Wang, Miguel Sabariego-Navarro, Mara Dierssen, Steven Finkbeiner, and Stefan F. Pinter. A dynamic in vitro model of down syndrome neurogenesis with trisomy 21 gene dosage correction. Science Advances, Jun 2024. URL: https://doi.org/10.1126/sciadv.adj0385, doi:10.1126/sciadv.adj0385. This article has 15 citations and is from a highest quality peer-reviewed journal.

9. (lanaelola2024increaseddosageof pages 9-11): Eva Lana-Elola, Rifdat Aoidi, Miriam Llorian, Dorota Gibbins, Callan Buechsenschuetz, Claudio Bussi, Helen Flynn, Tegan Gilmore, Sheona Watson-Scales, Marie Haugsten Hansen, Darryl Hayward, Ok-Ryul Song, Véronique Brault, Yann Herault, Emmanuel Deau, Laurent Meijer, Ambrosius P. Snijders, Maximiliano G. Gutierrez, Elizabeth M. C. Fisher, and Victor L. J. Tybulewicz. Increased dosage of dyrk1a leads to congenital heart defects in a mouse model of down syndrome. Science translational medicine, 16:eadd6883-eadd6883, Jan 2024. URL: https://doi.org/10.1126/scitranslmed.add6883, doi:10.1126/scitranslmed.add6883. This article has 48 citations and is from a highest quality peer-reviewed journal.

10. (donovan2024multimodalanalysisof pages 8-10): Micah G. Donovan, Angela L. Rachubinski, Keith P. Smith, Paula Araya, Katherine A. Waugh, Belinda Enriquez-Estrada, Eleanor C. Britton, Hannah R. Lyford, Ross E. Granrath, Kyndal A. Schade, Kohl T. Kinning, Neetha Paul Eduthan, Kelly D. Sullivan, Matthew D. Galbraith, and Joaquin M. Espinosa. Multimodal analysis of dysregulated heme metabolism, hypoxic signaling, and stress erythropoiesis in down syndrome. Cell reports, 43:114599-114599, Aug 2024. URL: https://doi.org/10.1016/j.celrep.2024.114599, doi:10.1016/j.celrep.2024.114599. This article has 9 citations and is from a highest quality peer-reviewed journal.

11. (donovan2024multimodalanalysisof pages 23-29): Micah G. Donovan, Angela L. Rachubinski, Keith P. Smith, Paula Araya, Katherine A. Waugh, Belinda Enriquez-Estrada, Eleanor C. Britton, Hannah R. Lyford, Ross E. Granrath, Kyndal A. Schade, Kohl T. Kinning, Neetha Paul Eduthan, Kelly D. Sullivan, Matthew D. Galbraith, and Joaquin M. Espinosa. Multimodal analysis of dysregulated heme metabolism, hypoxic signaling, and stress erythropoiesis in down syndrome. Cell reports, 43:114599-114599, Aug 2024. URL: https://doi.org/10.1016/j.celrep.2024.114599, doi:10.1016/j.celrep.2024.114599. This article has 9 citations and is from a highest quality peer-reviewed journal.

12. (chapman2024geneexpressionstudies pages 8-9): Laura R. Chapman, Isabela V. P. Ramnarine, Dan Zemke, Arshad Majid, and Simon M. Bell. Gene expression studies in down syndrome: what do they tell us about disease phenotypes? International Journal of Molecular Sciences, 25:2968, Mar 2024. URL: https://doi.org/10.3390/ijms25052968, doi:10.3390/ijms25052968. This article has 23 citations.

13. (maheshwari2024epigeneticsofdown pages 10-11): Akhil Maheshwari and Srijan Singh. Epigenetics of down syndrome. Newborn, 3:263-280, Dec 2024. URL: https://doi.org/10.5005/jp-journals-11002-0112, doi:10.5005/jp-journals-11002-0112. This article has 3 citations.

14. (bansal2024adynamicin pages 3-4): Prakhar Bansal, Erin C. Banda, Heather R. Glatt-Deeley, Christopher E. Stoddard, Jeremy W. Linsley, Neha Arora, Cécile Deleschaux, Darcy T. Ahern, Yuvabharath Kondaveeti, Rachael E. Massey, Michael Nicouleau, Shijie Wang, Miguel Sabariego-Navarro, Mara Dierssen, Steven Finkbeiner, and Stefan F. Pinter. A dynamic in vitro model of down syndrome neurogenesis with trisomy 21 gene dosage correction. Science Advances, Jun 2024. URL: https://doi.org/10.1126/sciadv.adj0385, doi:10.1126/sciadv.adj0385. This article has 15 citations and is from a highest quality peer-reviewed journal.

15. (murphy2024downsyndromeand pages 6-7): Aidan J. Murphy, Steve D. Wilton, May T. Aung-Htut, and Craig S. McIntosh. Down syndrome and dyrk1a overexpression: relationships and future therapeutic directions. Frontiers in Molecular Neuroscience, Jul 2024. URL: https://doi.org/10.3389/fnmol.2024.1391564, doi:10.3389/fnmol.2024.1391564. This article has 21 citations.

16. (murphy2024downsyndromeand pages 4-6): Aidan J. Murphy, Steve D. Wilton, May T. Aung-Htut, and Craig S. McIntosh. Down syndrome and dyrk1a overexpression: relationships and future therapeutic directions. Frontiers in Molecular Neuroscience, Jul 2024. URL: https://doi.org/10.3389/fnmol.2024.1391564, doi:10.3389/fnmol.2024.1391564. This article has 21 citations.

17. (lanaelola2024increaseddosageof pages 31-33): Eva Lana-Elola, Rifdat Aoidi, Miriam Llorian, Dorota Gibbins, Callan Buechsenschuetz, Claudio Bussi, Helen Flynn, Tegan Gilmore, Sheona Watson-Scales, Marie Haugsten Hansen, Darryl Hayward, Ok-Ryul Song, Véronique Brault, Yann Herault, Emmanuel Deau, Laurent Meijer, Ambrosius P. Snijders, Maximiliano G. Gutierrez, Elizabeth M. C. Fisher, and Victor L. J. Tybulewicz. Increased dosage of dyrk1a leads to congenital heart defects in a mouse model of down syndrome. Science translational medicine, 16:eadd6883-eadd6883, Jan 2024. URL: https://doi.org/10.1126/scitranslmed.add6883, doi:10.1126/scitranslmed.add6883. This article has 48 citations and is from a highest quality peer-reviewed journal.

18. (bansal2024adynamicin pages 1-3): Prakhar Bansal, Erin C. Banda, Heather R. Glatt-Deeley, Christopher E. Stoddard, Jeremy W. Linsley, Neha Arora, Cécile Deleschaux, Darcy T. Ahern, Yuvabharath Kondaveeti, Rachael E. Massey, Michael Nicouleau, Shijie Wang, Miguel Sabariego-Navarro, Mara Dierssen, Steven Finkbeiner, and Stefan F. Pinter. A dynamic in vitro model of down syndrome neurogenesis with trisomy 21 gene dosage correction. Science Advances, Jun 2024. URL: https://doi.org/10.1126/sciadv.adj0385, doi:10.1126/sciadv.adj0385. This article has 15 citations and is from a highest quality peer-reviewed journal.

19. (bansal2024adynamicin pages 3-3): Prakhar Bansal, Erin C. Banda, Heather R. Glatt-Deeley, Christopher E. Stoddard, Jeremy W. Linsley, Neha Arora, Cécile Deleschaux, Darcy T. Ahern, Yuvabharath Kondaveeti, Rachael E. Massey, Michael Nicouleau, Shijie Wang, Miguel Sabariego-Navarro, Mara Dierssen, Steven Finkbeiner, and Stefan F. Pinter. A dynamic in vitro model of down syndrome neurogenesis with trisomy 21 gene dosage correction. Science Advances, Jun 2024. URL: https://doi.org/10.1126/sciadv.adj0385, doi:10.1126/sciadv.adj0385. This article has 15 citations and is from a highest quality peer-reviewed journal.

20. (bansal2024adynamicin pages 9-10): Prakhar Bansal, Erin C. Banda, Heather R. Glatt-Deeley, Christopher E. Stoddard, Jeremy W. Linsley, Neha Arora, Cécile Deleschaux, Darcy T. Ahern, Yuvabharath Kondaveeti, Rachael E. Massey, Michael Nicouleau, Shijie Wang, Miguel Sabariego-Navarro, Mara Dierssen, Steven Finkbeiner, and Stefan F. Pinter. A dynamic in vitro model of down syndrome neurogenesis with trisomy 21 gene dosage correction. Science Advances, Jun 2024. URL: https://doi.org/10.1126/sciadv.adj0385, doi:10.1126/sciadv.adj0385. This article has 15 citations and is from a highest quality peer-reviewed journal.

21. (donovan2024multimodalanalysisof pages 5-6): Micah G. Donovan, Angela L. Rachubinski, Keith P. Smith, Paula Araya, Katherine A. Waugh, Belinda Enriquez-Estrada, Eleanor C. Britton, Hannah R. Lyford, Ross E. Granrath, Kyndal A. Schade, Kohl T. Kinning, Neetha Paul Eduthan, Kelly D. Sullivan, Matthew D. Galbraith, and Joaquin M. Espinosa. Multimodal analysis of dysregulated heme metabolism, hypoxic signaling, and stress erythropoiesis in down syndrome. Cell reports, 43:114599-114599, Aug 2024. URL: https://doi.org/10.1016/j.celrep.2024.114599, doi:10.1016/j.celrep.2024.114599. This article has 9 citations and is from a highest quality peer-reviewed journal.

22. (rachubinski2024jakinhibitiondecreases pages 14-15): Angela L Rachubinski, Elizabeth Wallace, Emily Gurnee, Belinda A Enriquez-Estrada, Kayleigh R Worek, Keith P Smith, Paula Araya, Katherine A Waugh, Ross E Granrath, Eleanor Britton, Hannah R Lyford, Micah G Donovan, Neetha Paul Eduthan, Amanda A Hill, Barry Martin, Kelly D Sullivan, Lina Patel, Deborah J Fidler, Matthew D Galbraith, Cory A Dunnick, David A Norris, and Joaquín M Espinosa. Jak inhibition decreases the autoimmune burden in down syndrome. Dec 2024. URL: https://doi.org/10.7554/elife.99323, doi:10.7554/elife.99323. This article has 25 citations and is from a domain leading peer-reviewed journal.

23. (rachubinski2024jakinhibitiondecreases pages 19-21): Angela L Rachubinski, Elizabeth Wallace, Emily Gurnee, Belinda A Enriquez-Estrada, Kayleigh R Worek, Keith P Smith, Paula Araya, Katherine A Waugh, Ross E Granrath, Eleanor Britton, Hannah R Lyford, Micah G Donovan, Neetha Paul Eduthan, Amanda A Hill, Barry Martin, Kelly D Sullivan, Lina Patel, Deborah J Fidler, Matthew D Galbraith, Cory A Dunnick, David A Norris, and Joaquín M Espinosa. Jak inhibition decreases the autoimmune burden in down syndrome. Dec 2024. URL: https://doi.org/10.7554/elife.99323, doi:10.7554/elife.99323. This article has 25 citations and is from a domain leading peer-reviewed journal.

24. (rachubinski2024jakinhibitiondecreases pages 1-2): Angela L Rachubinski, Elizabeth Wallace, Emily Gurnee, Belinda A Enriquez-Estrada, Kayleigh R Worek, Keith P Smith, Paula Araya, Katherine A Waugh, Ross E Granrath, Eleanor Britton, Hannah R Lyford, Micah G Donovan, Neetha Paul Eduthan, Amanda A Hill, Barry Martin, Kelly D Sullivan, Lina Patel, Deborah J Fidler, Matthew D Galbraith, Cory A Dunnick, David A Norris, and Joaquín M Espinosa. Jak inhibition decreases the autoimmune burden in down syndrome. Dec 2024. URL: https://doi.org/10.7554/elife.99323, doi:10.7554/elife.99323. This article has 25 citations and is from a domain leading peer-reviewed journal.

25. (rachubinski2024jakinhibitiondecreases pages 15-18): Angela L Rachubinski, Elizabeth Wallace, Emily Gurnee, Belinda A Enriquez-Estrada, Kayleigh R Worek, Keith P Smith, Paula Araya, Katherine A Waugh, Ross E Granrath, Eleanor Britton, Hannah R Lyford, Micah G Donovan, Neetha Paul Eduthan, Amanda A Hill, Barry Martin, Kelly D Sullivan, Lina Patel, Deborah J Fidler, Matthew D Galbraith, Cory A Dunnick, David A Norris, and Joaquín M Espinosa. Jak inhibition decreases the autoimmune burden in down syndrome. Dec 2024. URL: https://doi.org/10.7554/elife.99323, doi:10.7554/elife.99323. This article has 25 citations and is from a domain leading peer-reviewed journal.

26. (mason2024downsyndromeassociatedleukaemias pages 1-1): Nicola R. Mason, Hilary Cahill, Yonatan Diamond, Karen McCleary, Rishi S. Kotecha, Glenn M. Marshall, and Marion K. Mateos. Down syndrome-associated leukaemias: current evidence and challenges. Therapeutic Advances in Hematology, Jan 2024. URL: https://doi.org/10.1177/20406207241257901, doi:10.1177/20406207241257901. This article has 11 citations and is from a peer-reviewed journal.

27. (mason2024downsyndromeassociatedleukaemias pages 1-3): Nicola R. Mason, Hilary Cahill, Yonatan Diamond, Karen McCleary, Rishi S. Kotecha, Glenn M. Marshall, and Marion K. Mateos. Down syndrome-associated leukaemias: current evidence and challenges. Therapeutic Advances in Hematology, Jan 2024. URL: https://doi.org/10.1177/20406207241257901, doi:10.1177/20406207241257901. This article has 11 citations and is from a peer-reviewed journal.

28. (mason2024downsyndromeassociatedleukaemias pages 3-4): Nicola R. Mason, Hilary Cahill, Yonatan Diamond, Karen McCleary, Rishi S. Kotecha, Glenn M. Marshall, and Marion K. Mateos. Down syndrome-associated leukaemias: current evidence and challenges. Therapeutic Advances in Hematology, Jan 2024. URL: https://doi.org/10.1177/20406207241257901, doi:10.1177/20406207241257901. This article has 11 citations and is from a peer-reviewed journal.

29. (mason2024downsyndromeassociatedleukaemias pages 4-6): Nicola R. Mason, Hilary Cahill, Yonatan Diamond, Karen McCleary, Rishi S. Kotecha, Glenn M. Marshall, and Marion K. Mateos. Down syndrome-associated leukaemias: current evidence and challenges. Therapeutic Advances in Hematology, Jan 2024. URL: https://doi.org/10.1177/20406207241257901, doi:10.1177/20406207241257901. This article has 11 citations and is from a peer-reviewed journal.

30. (donovan2024multimodalanalysisof pages 1-3): Micah G. Donovan, Angela L. Rachubinski, Keith P. Smith, Paula Araya, Katherine A. Waugh, Belinda Enriquez-Estrada, Eleanor C. Britton, Hannah R. Lyford, Ross E. Granrath, Kyndal A. Schade, Kohl T. Kinning, Neetha Paul Eduthan, Kelly D. Sullivan, Matthew D. Galbraith, and Joaquin M. Espinosa. Multimodal analysis of dysregulated heme metabolism, hypoxic signaling, and stress erythropoiesis in down syndrome. Cell reports, 43:114599-114599, Aug 2024. URL: https://doi.org/10.1016/j.celrep.2024.114599, doi:10.1016/j.celrep.2024.114599. This article has 9 citations and is from a highest quality peer-reviewed journal.

31. (lanaelola2024increaseddosageof pages 11-13): Eva Lana-Elola, Rifdat Aoidi, Miriam Llorian, Dorota Gibbins, Callan Buechsenschuetz, Claudio Bussi, Helen Flynn, Tegan Gilmore, Sheona Watson-Scales, Marie Haugsten Hansen, Darryl Hayward, Ok-Ryul Song, Véronique Brault, Yann Herault, Emmanuel Deau, Laurent Meijer, Ambrosius P. Snijders, Maximiliano G. Gutierrez, Elizabeth M. C. Fisher, and Victor L. J. Tybulewicz. Increased dosage of dyrk1a leads to congenital heart defects in a mouse model of down syndrome. Science translational medicine, 16:eadd6883-eadd6883, Jan 2024. URL: https://doi.org/10.1126/scitranslmed.add6883, doi:10.1126/scitranslmed.add6883. This article has 48 citations and is from a highest quality peer-reviewed journal.

32. (bansal2024adynamicin pages 11-12): Prakhar Bansal, Erin C. Banda, Heather R. Glatt-Deeley, Christopher E. Stoddard, Jeremy W. Linsley, Neha Arora, Cécile Deleschaux, Darcy T. Ahern, Yuvabharath Kondaveeti, Rachael E. Massey, Michael Nicouleau, Shijie Wang, Miguel Sabariego-Navarro, Mara Dierssen, Steven Finkbeiner, and Stefan F. Pinter. A dynamic in vitro model of down syndrome neurogenesis with trisomy 21 gene dosage correction. Science Advances, Jun 2024. URL: https://doi.org/10.1126/sciadv.adj0385, doi:10.1126/sciadv.adj0385. This article has 15 citations and is from a highest quality peer-reviewed journal.

33. (rachubinski2024jakinhibitiondecreases pages 18-19): Angela L Rachubinski, Elizabeth Wallace, Emily Gurnee, Belinda A Enriquez-Estrada, Kayleigh R Worek, Keith P Smith, Paula Araya, Katherine A Waugh, Ross E Granrath, Eleanor Britton, Hannah R Lyford, Micah G Donovan, Neetha Paul Eduthan, Amanda A Hill, Barry Martin, Kelly D Sullivan, Lina Patel, Deborah J Fidler, Matthew D Galbraith, Cory A Dunnick, David A Norris, and Joaquín M Espinosa. Jak inhibition decreases the autoimmune burden in down syndrome. Dec 2024. URL: https://doi.org/10.7554/elife.99323, doi:10.7554/elife.99323. This article has 25 citations and is from a domain leading peer-reviewed journal.

34. (rachubinski2024jakinhibitiondecreases pages 21-22): Angela L Rachubinski, Elizabeth Wallace, Emily Gurnee, Belinda A Enriquez-Estrada, Kayleigh R Worek, Keith P Smith, Paula Araya, Katherine A Waugh, Ross E Granrath, Eleanor Britton, Hannah R Lyford, Micah G Donovan, Neetha Paul Eduthan, Amanda A Hill, Barry Martin, Kelly D Sullivan, Lina Patel, Deborah J Fidler, Matthew D Galbraith, Cory A Dunnick, David A Norris, and Joaquín M Espinosa. Jak inhibition decreases the autoimmune burden in down syndrome. Dec 2024. URL: https://doi.org/10.7554/elife.99323, doi:10.7554/elife.99323. This article has 25 citations and is from a domain leading peer-reviewed journal.

35. (donovan2024multimodalanalysisof pages 10-12): Micah G. Donovan, Angela L. Rachubinski, Keith P. Smith, Paula Araya, Katherine A. Waugh, Belinda Enriquez-Estrada, Eleanor C. Britton, Hannah R. Lyford, Ross E. Granrath, Kyndal A. Schade, Kohl T. Kinning, Neetha Paul Eduthan, Kelly D. Sullivan, Matthew D. Galbraith, and Joaquin M. Espinosa. Multimodal analysis of dysregulated heme metabolism, hypoxic signaling, and stress erythropoiesis in down syndrome. Cell reports, 43:114599-114599, Aug 2024. URL: https://doi.org/10.1016/j.celrep.2024.114599, doi:10.1016/j.celrep.2024.114599. This article has 9 citations and is from a highest quality peer-reviewed journal.

36. (donovan2024multimodalanalysisof pages 6-8): Micah G. Donovan, Angela L. Rachubinski, Keith P. Smith, Paula Araya, Katherine A. Waugh, Belinda Enriquez-Estrada, Eleanor C. Britton, Hannah R. Lyford, Ross E. Granrath, Kyndal A. Schade, Kohl T. Kinning, Neetha Paul Eduthan, Kelly D. Sullivan, Matthew D. Galbraith, and Joaquin M. Espinosa. Multimodal analysis of dysregulated heme metabolism, hypoxic signaling, and stress erythropoiesis in down syndrome. Cell reports, 43:114599-114599, Aug 2024. URL: https://doi.org/10.1016/j.celrep.2024.114599, doi:10.1016/j.celrep.2024.114599. This article has 9 citations and is from a highest quality peer-reviewed journal.

37. (donovan2024multimodalanalysisof pages 3-5): Micah G. Donovan, Angela L. Rachubinski, Keith P. Smith, Paula Araya, Katherine A. Waugh, Belinda Enriquez-Estrada, Eleanor C. Britton, Hannah R. Lyford, Ross E. Granrath, Kyndal A. Schade, Kohl T. Kinning, Neetha Paul Eduthan, Kelly D. Sullivan, Matthew D. Galbraith, and Joaquin M. Espinosa. Multimodal analysis of dysregulated heme metabolism, hypoxic signaling, and stress erythropoiesis in down syndrome. Cell reports, 43:114599-114599, Aug 2024. URL: https://doi.org/10.1016/j.celrep.2024.114599, doi:10.1016/j.celrep.2024.114599. This article has 9 citations and is from a highest quality peer-reviewed journal.

38. (abukhaled2024understandingthegenetic pages 9-11): Yara Abukhaled, Kenana Hatab, Mohammad Awadhalla, and Hamdan Hamdan. Understanding the genetic mechanisms and cognitive impairments in down syndrome: towards a holistic approach. Journal of Neurology, 271:87-104, Aug 2024. URL: https://doi.org/10.1007/s00415-023-11890-0, doi:10.1007/s00415-023-11890-0. This article has 31 citations and is from a domain leading peer-reviewed journal.

39. (chapman2024geneexpressionstudies pages 12-13): Laura R. Chapman, Isabela V. P. Ramnarine, Dan Zemke, Arshad Majid, and Simon M. Bell. Gene expression studies in down syndrome: what do they tell us about disease phenotypes? International Journal of Molecular Sciences, 25:2968, Mar 2024. URL: https://doi.org/10.3390/ijms25052968, doi:10.3390/ijms25052968. This article has 23 citations.

40. (waugh2023triplicationofthe pages 3-4): Katherine A. Waugh, Ross Minter, Jessica Baxter, Congwu Chi, Matthew D. Galbraith, Kathryn D. Tuttle, Neetha P. Eduthan, Kohl T. Kinning, Zdenek Andrysik, Paula Araya, Hannah Dougherty, Lauren N. Dunn, Michael Ludwig, Kyndal A. Schade, Dayna Tracy, Keith P. Smith, Ross E. Granrath, Nicolas Busquet, Santosh Khanal, Ryan D. Anderson, Liza L. Cox, Belinda Enriquez Estrada, Angela L. Rachubinski, Hannah R. Lyford, Eleanor C. Britton, Katherine A. Fantauzzo, David J. Orlicky, Jennifer L. Matsuda, Kunhua Song, Timothy C. Cox, Kelly D. Sullivan, and Joaquin M. Espinosa. Triplication of the interferon receptor locus contributes to hallmarks of down syndrome in a mouse model. Nature Genetics, 55:1034-1047, Jun 2023. URL: https://doi.org/10.1038/s41588-023-01399-7, doi:10.1038/s41588-023-01399-7. This article has 92 citations and is from a highest quality peer-reviewed journal.

41. (lanaelola2024increaseddosageof pages 4-6): Eva Lana-Elola, Rifdat Aoidi, Miriam Llorian, Dorota Gibbins, Callan Buechsenschuetz, Claudio Bussi, Helen Flynn, Tegan Gilmore, Sheona Watson-Scales, Marie Haugsten Hansen, Darryl Hayward, Ok-Ryul Song, Véronique Brault, Yann Herault, Emmanuel Deau, Laurent Meijer, Ambrosius P. Snijders, Maximiliano G. Gutierrez, Elizabeth M. C. Fisher, and Victor L. J. Tybulewicz. Increased dosage of dyrk1a leads to congenital heart defects in a mouse model of down syndrome. Science translational medicine, 16:eadd6883-eadd6883, Jan 2024. URL: https://doi.org/10.1126/scitranslmed.add6883, doi:10.1126/scitranslmed.add6883. This article has 48 citations and is from a highest quality peer-reviewed journal.

42. (canonica2024dissectingthecontribution pages 11-12): Tara Canonica, Emma J Kidd, Dorota Gibbins, Eva Lana-Elola, Elizabeth M. C. Fisher, Victor L. J. Tybulewicz, and Mark A Good. Dissecting the contribution of human chromosome 21 syntenic regions to recognition memory processes in adult and aged mouse models of down syndrome. Frontiers in Behavioral Neuroscience, Jul 2024. URL: https://doi.org/10.3389/fnbeh.2024.1428146, doi:10.3389/fnbeh.2024.1428146. This article has 2 citations.

43. (canonica2024dissectingthecontribution pages 8-11): Tara Canonica, Emma J Kidd, Dorota Gibbins, Eva Lana-Elola, Elizabeth M. C. Fisher, Victor L. J. Tybulewicz, and Mark A Good. Dissecting the contribution of human chromosome 21 syntenic regions to recognition memory processes in adult and aged mouse models of down syndrome. Frontiers in Behavioral Neuroscience, Jul 2024. URL: https://doi.org/10.3389/fnbeh.2024.1428146, doi:10.3389/fnbeh.2024.1428146. This article has 2 citations.

44. (bansal2024adynamicin pages 8-9): Prakhar Bansal, Erin C. Banda, Heather R. Glatt-Deeley, Christopher E. Stoddard, Jeremy W. Linsley, Neha Arora, Cécile Deleschaux, Darcy T. Ahern, Yuvabharath Kondaveeti, Rachael E. Massey, Michael Nicouleau, Shijie Wang, Miguel Sabariego-Navarro, Mara Dierssen, Steven Finkbeiner, and Stefan F. Pinter. A dynamic in vitro model of down syndrome neurogenesis with trisomy 21 gene dosage correction. Science Advances, Jun 2024. URL: https://doi.org/10.1126/sciadv.adj0385, doi:10.1126/sciadv.adj0385. This article has 15 citations and is from a highest quality peer-reviewed journal.

45. (mason2024downsyndromeassociatedleukaemias pages 20-21): Nicola R. Mason, Hilary Cahill, Yonatan Diamond, Karen McCleary, Rishi S. Kotecha, Glenn M. Marshall, and Marion K. Mateos. Down syndrome-associated leukaemias: current evidence and challenges. Therapeutic Advances in Hematology, Jan 2024. URL: https://doi.org/10.1177/20406207241257901, doi:10.1177/20406207241257901. This article has 11 citations and is from a peer-reviewed journal.

46. (mason2024downsyndromeassociatedleukaemias pages 21-22): Nicola R. Mason, Hilary Cahill, Yonatan Diamond, Karen McCleary, Rishi S. Kotecha, Glenn M. Marshall, and Marion K. Mateos. Down syndrome-associated leukaemias: current evidence and challenges. Therapeutic Advances in Hematology, Jan 2024. URL: https://doi.org/10.1177/20406207241257901, doi:10.1177/20406207241257901. This article has 11 citations and is from a peer-reviewed journal.

47. (murphy2024downsyndromeand pages 7-9): Aidan J. Murphy, Steve D. Wilton, May T. Aung-Htut, and Craig S. McIntosh. Down syndrome and dyrk1a overexpression: relationships and future therapeutic directions. Frontiers in Molecular Neuroscience, Jul 2024. URL: https://doi.org/10.3389/fnmol.2024.1391564, doi:10.3389/fnmol.2024.1391564. This article has 21 citations.

48. (stafstrom2024infantilespasmsin pages 13-14): Carl E. Stafstrom and Li-Rong Shao. Infantile spasms in pediatric down syndrome: potential mechanisms driving therapeutic considerations. Children, 11:1513, Dec 2024. URL: https://doi.org/10.3390/children11121513, doi:10.3390/children11121513. This article has 4 citations.

49. (canonica2024dissectingthecontribution pages 1-2): Tara Canonica, Emma J Kidd, Dorota Gibbins, Eva Lana-Elola, Elizabeth M. C. Fisher, Victor L. J. Tybulewicz, and Mark A Good. Dissecting the contribution of human chromosome 21 syntenic regions to recognition memory processes in adult and aged mouse models of down syndrome. Frontiers in Behavioral Neuroscience, Jul 2024. URL: https://doi.org/10.3389/fnbeh.2024.1428146, doi:10.3389/fnbeh.2024.1428146. This article has 2 citations.

50. (canonica2024dissectingthecontribution pages 2-3): Tara Canonica, Emma J Kidd, Dorota Gibbins, Eva Lana-Elola, Elizabeth M. C. Fisher, Victor L. J. Tybulewicz, and Mark A Good. Dissecting the contribution of human chromosome 21 syntenic regions to recognition memory processes in adult and aged mouse models of down syndrome. Frontiers in Behavioral Neuroscience, Jul 2024. URL: https://doi.org/10.3389/fnbeh.2024.1428146, doi:10.3389/fnbeh.2024.1428146. This article has 2 citations.

51. (rachubinski2024jakinhibitiondecreases pages 6-7): Angela L Rachubinski, Elizabeth Wallace, Emily Gurnee, Belinda A Enriquez-Estrada, Kayleigh R Worek, Keith P Smith, Paula Araya, Katherine A Waugh, Ross E Granrath, Eleanor Britton, Hannah R Lyford, Micah G Donovan, Neetha Paul Eduthan, Amanda A Hill, Barry Martin, Kelly D Sullivan, Lina Patel, Deborah J Fidler, Matthew D Galbraith, Cory A Dunnick, David A Norris, and Joaquín M Espinosa. Jak inhibition decreases the autoimmune burden in down syndrome. Dec 2024. URL: https://doi.org/10.7554/elife.99323, doi:10.7554/elife.99323. This article has 25 citations and is from a domain leading peer-reviewed journal.

52. (alldred2024analysisofmicroisolated pages 1-6): Melissa J. Alldred, Harshitha Pidikiti, Kyrillos W. Ibrahim, Sang Han Lee, Adriana Heguy, Gabriel E. Hoffman, Panos Roussos, Thomas Wisniewski, Jerzy Wegiel, Grace E. Stutzmann, Elliott J. Mufson, and Stephen D. Ginsberg. Analysis of microisolated frontal cortex excitatory layer iii and v pyramidal neurons reveals a neurodegenerative phenotype in individuals with down syndrome. Acta neuropathologica, 148 1:16, Aug 2024. URL: https://doi.org/10.1007/s00401-024-02768-0, doi:10.1007/s00401-024-02768-0. This article has 8 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](falcon_artifacts/artifact-02.md)
