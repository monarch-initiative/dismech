---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-28T12:05:40.550470'
end_time: '2026-05-28T12:54:01.089018'
duration_seconds: 2900.54
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Ewing Sarcoma
  category: ''
  hypothesis_group_id: cell_of_origin_context_model
  hypothesis_label: Permissive developmental cell-of-origin model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: cell_of_origin_context_model\nhypothesis_label:\
    \ Permissive developmental cell-of-origin model\nstatus: EMERGING\ndescription:\
    \ EWS-FLI1 transformation depends on developmental timing and progenitor state.\
    \ Neural crest-related\n  and embryonic mesenchymal progenitors are leading candidates,\
    \ but the decisive chromatin and differentiation-state\n  features remain unresolved.\n\
    evidence:\n- reference: PMID:41136396\n  reference_title: EWS::FLI1 expression\
    \ in human embryonic mesenchymal stem cells leads to transcriptional\n    reprograming,\
    \ defective DNA damage repair and Ewing sarcoma.\n  supports: SUPPORT\n  evidence_source:\
    \ IN_VITRO\n  snippet: is able to endow transforming capacity when expressed in\
    \ undifferentiated, early\n  explanation: Supports the developmental-context hypothesis\
    \ in embryonic mesenchymal stem cells."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
citation_count: 46
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Ewing Sarcoma
- **Category:**

## Target Hypothesis
- **Hypothesis ID:** cell_of_origin_context_model
- **Hypothesis Label:** Permissive developmental cell-of-origin model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: cell_of_origin_context_model
hypothesis_label: Permissive developmental cell-of-origin model
status: EMERGING
description: EWS-FLI1 transformation depends on developmental timing and progenitor state. Neural crest-related
  and embryonic mesenchymal progenitors are leading candidates, but the decisive chromatin and differentiation-state
  features remain unresolved.
evidence:
- reference: PMID:41136396
  reference_title: EWS::FLI1 expression in human embryonic mesenchymal stem cells leads to transcriptional
    reprograming, defective DNA damage repair and Ewing sarcoma.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: is able to endow transforming capacity when expressed in undifferentiated, early
  explanation: Supports the developmental-context hypothesis in embryonic mesenchymal stem cells.
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

# Permissive Developmental Cell-of-Origin Model for Ewing Sarcoma: Hypothesis Evaluation Report

**Hypothesis ID:** cell_of_origin_context_model
**Hypothesis Label:** Permissive developmental cell-of-origin model
**Status in KB:** EMERGING
**Report Date:** 2026-05-28
**Investigation:** 5 iterations, 23 confirmed findings, ~100 papers reviewed

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED, approaching ESTABLISHED for core claims.**

The permissive developmental cell-of-origin model posits that EWS-FLI1 transformation depends on developmental timing and progenitor state — specifically that neural crest-related and embryonic mesenchymal progenitors are the leading candidate cells of origin, but that the decisive chromatin and differentiation-state features enabling permissiveness remain unresolved. After systematic evaluation of ~100 primary research papers across 5 investigative iterations, we find **strong convergent evidence** supporting the core claims of this hypothesis from multiple independent experimental systems: zebrafish in vivo models demonstrating neural crest-specific permissiveness, human embryonic MSC transformation studies revealing a developmental timing gradient, germline GGAA microsatellite length-dependent susceptibility, and the recently discovered pubertal IGF-1/YAP1 cooperating mechanism. However, we recommend retaining the **EMERGING** status because three critical questions remain unresolved: (1) the precise chromatin features that define the permissive window, (2) whether adult-onset extraskeletal Ewing sarcomas arise from residual embryonic progenitors or represent a distinct pathogenic trajectory, and (3) the relative contributions of neural crest vs. mesoderm-derived MSCs across anatomic sites.

---

## Summary

Ewing sarcoma is an aggressive pediatric bone and soft tissue malignancy driven by the EWS-FLI1 fusion oncoprotein (arising from t(11;22)(q24;q12) in ~85% of cases). Unlike most cancers, Ewing sarcoma has an exceptionally low mutational burden (~0.15 mutations/Mb), suggesting that the fusion protein itself is the dominant oncogenic driver and that the cellular context in which it is expressed is critical. The permissive developmental cell-of-origin hypothesis addresses a fundamental paradox: EWS-FLI1 causes growth arrest or apoptosis in most differentiated cell types, yet drives aggressive oncogenesis in specific progenitor populations.

Our investigation identified 23 confirmed findings supported by 43 evidence matrix entries across the spectrum of evidence types — from zebrafish genetic models and human embryonic stem cell experiments to genome-wide association studies and single-cell multi-omic profiling of primary tumors. The strongest direct evidence comes from three landmark studies: (1) Vasileva et al. (2024/2025) demonstrating that neural crest-derived cells uniquely tolerate EWSR1-FLI1 and form tumors in zebrafish; (2) Hernandez-Munoz et al. (2025) showing that only human embryonic MSCs — not pediatric or adult MSCs — support full EWS-FLI1-driven transformation; and (3) Noorizadeh et al. (2025) identifying pubertal IGF-1 levels as the missing non-genetic cooperating signal that reprograms EWS-FLI1-expressing mesenchymal cells to stable transformation via YAP1/TEAD.

The evidence also reveals important qualifications and competing models. Adult-onset Ewing sarcoma (≥40 years, 13.8% of cases) presents predominantly as extraskeletal disease, challenging a purely embryonic origin. The competing "fusion-determines-phenotype" model, supported by Hu-Lieskovan et al. (2005), argues EWS-FLI1 itself drives the neural crest phenotype regardless of cell of origin — though this is counterbalanced by Staege et al. (2004) showing that the full Ewing transcriptional signature depends on the histogenetic background. The integration of these findings points toward a refined model where developmental progenitor state, GGAA microsatellite germline architecture, and pubertal growth factor signaling converge to create a narrow window of oncogenic permissiveness.

{{figure:integrated_model.png|caption=Integrative mechanistic model of the permissive developmental cell-of-origin hypothesis, incorporating the IGF-1/YAP1 cooperating mechanism identified in iterations 4-5}}

---

## Key Findings

### 1. Neural Crest Cells Are Uniquely Permissive for EWSR1-FLI1 In Vivo

The most compelling direct evidence for the cell-of-origin hypothesis comes from a zebrafish genetic model developed by Vasileva et al. ([PMID: 39554045](https://pubmed.ncbi.nlm.nih.gov/39554045/); [PMID: 41072418](https://pubmed.ncbi.nlm.nih.gov/41072418/)). This is the first vertebrate in vivo model demonstrating cell-type-specific permissiveness and actual tumor formation. Neural crest-derived cells uniquely tolerate EWSR1-FLI1 expression, and targeted expression in these cells generates lethal Ewing sarcomas. Single-cell analysis revealed that "EWSR1::FLI1 reprograms neural crest-derived cells to a mesoderm-like state, strikingly resulting in ectopic fins throughout the body" — directly demonstrating the developmental reprogramming mechanism. This work establishes that the neural crest lineage provides a uniquely permissive cellular context, and that the fusion oncogene hijacks developmental enhancers to execute neural crest-to-mesoderm reprogramming.

### 2. Human Embryonic MSCs — but Not Pediatric/Adult MSCs — Support Full Transformation

The seed paper for this hypothesis, Hernandez-Munoz et al. 2025 ([PMID: 41136396](https://pubmed.ncbi.nlm.nih.gov/41136396/)), provides the most direct demonstration of developmental timing specificity. EWS-FLI1 expression in human embryonic mesenchymal stem cells (heMSCs) results in acquisition of the Ewing sarcoma transcriptome, with EWS-FLI1 binding preferentially to intronic and intergenic microsatellites. Critically, "EWS-FLI1 expression in human pediatric mesenchymal stem cells (MSCs) induces a transcriptional response distinct from that of human adult MSCs, but fails to form tumors." Only the earliest, most undifferentiated embryonic MSCs support full EWS-FLI1-driven transformation, and "EWS-FLI1 enforces an aberrant transcriptome and solely is able to endow transforming capacity when expressed in undifferentiated, early heMSCs." This establishes a permissiveness gradient: embryonic MSCs > pediatric MSCs > adult MSCs, with full oncogenic capacity restricted to the embryonic stage.

Earlier work corroborates this pattern. Riggi et al. 2005 ([PMID: 16357154](https://pubmed.ncbi.nlm.nih.gov/16357154/)) first showed that "EWS-FLI-1 alone can transform primary bone marrow-derived mesenchymal progenitor cells and generate tumors that display hallmarks of Ewing's sarcoma" in mice. Riggi et al. 2008 ([PMID: 18381423](https://pubmed.ncbi.nlm.nih.gov/18381423/)) demonstrated that "expression of EWS-FLI-1 in human mesenchymal stem cells (hMSC) is not only stably maintained without inhibiting proliferation but also induces a gene expression profile bearing striking similarity to that of ESFT." Von Levetzow et al. 2011 ([PMID: 21559395](https://pubmed.ncbi.nlm.nih.gov/21559395/)) showed that "the molecular signature of established ESFT is more similar to hNCSC than any other normal tissue, including MSC, indicating that maintenance or reactivation of the NCSC program is a feature of ESFT pathogenesis."

### 3. EWS-FLI1 Reprograms the Epigenome via De Novo GGAA Microsatellite Enhancers

A core mechanistic pillar of the hypothesis is that EWS-FLI1 creates an entirely new enhancer landscape by exploiting GGAA microsatellite repeats. Riggi et al. 2014 ([PMID: 25453903](https://pubmed.ncbi.nlm.nih.gov/25453903/)) demonstrated that "at GGAA repeat elements, which lack evolutionary conservation and regulatory potential in other cell types, EWS-FLI1 multimers induce chromatin opening and create de novo enhancers that physically interact with target promoters." Conversely, EWS-FLI1 inactivates conserved enhancers containing canonical ETS motifs by displacing wild-type ETS factors. This dual mechanism activates oncogenes while silencing tumor suppressors and mesenchymal differentiation regulators. Grünewald et al. 2018 ([PMID: 29977059](https://pubmed.ncbi.nlm.nih.gov/29977059/)) confirmed that "EWSR1-FLI1 reprogrammes the epigenome by inducing de novo enhancers at GGAA microsatellites and by altering the state of gene regulatory elements, creating a unique epigenetic signature."

The GGAA microsatellite enhancer system shows critical repeat-length dependence. Johnson et al. 2017 ([PMID: 29091716](https://pubmed.ncbi.nlm.nih.gov/29091716/)) identified two classes (promoter-like and enhancer-like) with "EWS/FLI responsiveness dependent on microsatellite length." Boulay et al. 2018 ([PMID: 30042132](https://pubmed.ncbi.nlm.nih.gov/30042132/)) showed that "epigenome silencing of these repeat sites does not affect gene expression in unrelated cells, can prevent the induction of gene expression by EWS-FLI1." Tak et al. 2022 ([PMID: 35967079](https://pubmed.ncbi.nlm.nih.gov/35967079/)) demonstrated that "fusions between EWS and GGAA-repeat-targeted engineered zinc finger arrays (ZFAs) can function at least as efficiently as EWS-FLI1 for converting hundreds of GGAA repeats into active enhancers in a Ewing sarcoma precursor cell model."

### 4. Germline GGAA Repeat Length Directly Modulates Susceptibility

Lee/Machiela et al. 2023 ([PMID: 36787739](https://pubmed.ncbi.nlm.nih.gov/36787739/)) provided a direct germline-somatic interaction mechanism. Using targeted long-read sequencing at the 6p25.1 Ewing sarcoma susceptibility locus, they identified 50 microsatellite alleles and found that EwS-affected individuals had longer alleles (>135 bp) with more GGAA repeats. The microsatellite showed chromatin features of an EWSR1-FLI1 enhancer and regulated expression of RREB1, a transcription factor associated with RAS/MAPK signaling. RREB1 knockdown reduced proliferation and clonogenic potential. This provides a direct causal chain from germline architecture to oncogenic signaling: longer germline GGAA repeats → more EWSR1-FLI1 binding → stronger neo-enhancer activity → RREB1-mediated proliferation.

This finding, combined with ancestry-related variation in Ewing sarcoma incidence — "countries and subpopulations with predominately African, East Asian, and Southeast Asian ancestry had the lowest incidence rates, whereas Pacific Islanders and populations with predominantly European and North African/Middle Eastern ancestry had the highest" ([PMID: 33961701](https://pubmed.ncbi.nlm.nih.gov/33961701/)) — and GWAS-identified susceptibility loci suggesting "rare variation residing on common haplotypes are important contributors to EwS risk" ([PMID: 32881892](https://pubmed.ncbi.nlm.nih.gov/32881892/)), establishes that inherited germline GGAA microsatellite length is a critical determinant of whether EWS-FLI1 can establish its neo-enhancer program.

### 5. Cooperating Events Are Required: The IGF-1/YAP1 Breakthrough

Multiple mouse models have demonstrated that EWS-FLI1 alone is insufficient for tumor formation. Lin et al. 2008 ([PMID: 18974141](https://pubmed.ncbi.nlm.nih.gov/18974141/)) showed that "by itself, EWS-FLI1 did not induce the formation of tumors in the EF transgenic mice. However, in the setting of p53 deletion, EWS-FLI1 accelerated the formation of sarcomas from a median time of 50 to 21 weeks." Javaheri et al. 2016 ([PMID: 27735950](https://pubmed.ncbi.nlm.nih.gov/27735950/)) found that "mesenchymal stem cells (MSCs) expressing EF showed high self-renewal capacity and maintained an undifferentiated state despite high apoptosis. Blocking apoptosis through enforced BCL2 family member expression in MSCs promoted efficient and rapid sarcoma formation."

However, ~60-70% of Ewing sarcomas lack identifiable cooperating genetic mutations. The critical breakthrough came from Noorizadeh et al. 2025 ([PMID: 40080499](https://pubmed.ncbi.nlm.nih.gov/40080499/)), who discovered that "transient exposure to IGF-1 concentrations mimicking serum levels during puberty reprograms limb-derived mesenchymal cells of EWS::FLI1-mutant mice to stable transformation and tumorigenicity." They further identified "a modular mechanism of IGF-1-driven tumor promotion in the early steps of EwS pathogenesis, in which Yap1 plays a central role." Pharmacologic YAP1/TEAD inhibition reversed the transformed phenotype. This provides a non-genetic cooperating mechanism that elegantly explains: (a) why Ewing sarcoma peaks at puberty (ages 10-19), (b) why genetic cooperating mutations are rarely found, and (c) how the developmental timing window operates at the molecular level.

The YAP1/TEAD axis was independently validated by Chellini et al. 2025 ([PMID: 40414844](https://pubmed.ncbi.nlm.nih.gov/40414844/)), who identified a promoter-associated noncoding RNA whose "binding to TEAD impairs its interaction with YAP1, thus determining YAP1 translocation into the cytoplasm, its phosphorylation and degradation," exerting antitumor effects. This independent confirmation from a different research group strengthens the evidence for YAP1/TEAD as a pro-tumorigenic axis.

{{figure:evidence_summary.png|caption=Evidence landscape summary showing the distribution of supporting, qualifying, and competing evidence across evidence types}}

### 6. STAG2 Loss Reshapes the EWS-FLI1 Enhancer Landscape

STAG2 is the most commonly mutated gene in Ewing sarcoma (~17-21.5% of tumors). Eyunni et al. 2026 ([PMID: 41950086](https://pubmed.ncbi.nlm.nih.gov/41950086/)) demonstrated that "STAG2 loss eliminates over 40% of EWS-FLI1 binding sites, predominantly at enhancers containing short (1-4) GGAA repeats, while concurrently increasing binding at multimeric enhancers with ≥5 GGAA-repeat motifs." This selective amplification of EWS-FLI1 activity at multimeric microsatellite enhancers promotes tumor aggressiveness. Surdez et al. ([PMID: 39487368](https://pubmed.ncbi.nlm.nih.gov/39487368/)) confirmed that "cohesin-STAG2 facilitates communication between EWS::FLI1-bound long GGAA repeats, presumably acting as neoenhancers, and their target promoters." The low overall mutational burden was confirmed by two landmark WGS studies: Tirode et al. 2014 ([PMID: 25223734](https://pubmed.ncbi.nlm.nih.gov/25223734/)) showing "relatively few single-nucleotide variants, indels, structural variants, and copy-number alterations" across 112 samples, and Brohl et al. 2014 ([PMID: 25010205](https://pubmed.ncbi.nlm.nih.gov/25010205/)) quantifying "a very low mutational burden (0.15 mutations/Mb)."

### 7. EWS-FLI1 Silencing Reveals Underlying MSC Identity with Reversible Epigenetic State

Tirode et al. 2007 ([PMID: 17482132](https://pubmed.ncbi.nlm.nih.gov/17482132/)) showed that upon EWS-FLI1 silencing, "the profiles of different EWS-FLI1-silenced Ewing cell lines converge toward that of mesenchymal stem cells," and cells differentiate along adipogenic and osteogenic lineages. Suva et al. 2009 ([PMID: 19208848](https://pubmed.ncbi.nlm.nih.gov/19208848/)) identified "CD133+ tumor cells that display the capacity to initiate and sustain tumor growth through serial transplantation" with MSC properties including trilineage differentiation. This reversibility supports the model that EWS-FLI1 locks a progenitor cell in a specific developmental state rather than creating an irreversibly transformed phenotype, and is further supported by LSD1 inhibitor studies ([PMID: 24963049](https://pubmed.ncbi.nlm.nih.gov/24963049/)) showing "HCI2509 caused a dramatic reversal of both the up- and downregulated transcriptional profiles of EWS/FLI and EWS/ERG."

### 8. Intratumoral Heterogeneity and EWS-FLI1 Activity Fluctuation

Aynaud et al. 2020 ([PMID: 32049009](https://pubmed.ncbi.nlm.nih.gov/32049009/)) demonstrated at single-cell resolution that "cell proliferation and strong oxidative phosphorylation metabolism are associated with a well-defined range of EWSR1-FLI1 activity," while subpopulations at extreme activity levels show increased hypoxia. Waltner et al. 2025 ([PMID: 40667384](https://pubmed.ncbi.nlm.nih.gov/40667384/)) confirmed using multimodal single-cell RNA+ATAC-seq that "these same regulatory modules were variably enriched both across and within tumors, highlighting the existence of intratumoral heterogeneity." Bailey et al. 2019 ([PMID: 31164960](https://pubmed.ncbi.nlm.nih.gov/31164960/)) showed that "Ewing cells in the EWS-FLI1 low state demonstrate an increased propensity for metastasis," linking EWS-FLI1-low states to immune evasion via PD-L1/PD-L2 upregulation.

### 9. R-loop Accumulation Creates a Therapeutic Vulnerability

Gorthi et al. 2018 ([PMID: 29513652](https://pubmed.ncbi.nlm.nih.gov/29513652/)) showed that "Ewing sarcoma cells display alterations in regulation of damage-induced transcription, accumulation of R-loops and increased replication stress. In addition, homologous recombination is impaired in Ewing sarcoma owing to an enriched interaction between BRCA1 and the elongating transcription machinery." This creates sensitivity to PARP inhibitors, validated by Ramos et al. 2023 ([PMID: 37279093](https://pubmed.ncbi.nlm.nih.gov/37279093/)) who showed a bifunctional PARP-HDAC inhibitor "displayed enhanced cytotoxicity in Ewing sarcoma models" compared to single agents.

---

## Mechanistic Causal Chain

The hypothesis implies a multi-step causal chain from upstream developmental context to clinical manifestation. Below, we map each step and assess its evidentiary strength.

```
UPSTREAM TRIGGERS
├─ Germline GGAA microsatellite length variation ──── [STRONG evidence]
│  └─ Population-level susceptibility (ancestry-dependent)
├─ t(11;22) translocation → EWS-FLI1 fusion ──────── [ESTABLISHED]
│
PERMISSIVE CELL STATE (the core hypothesis)
├─ Neural crest / embryonic mesenchymal progenitor ── [STRONG evidence]
│  ├─ NC-derived cells uniquely tolerate EWS-FLI1 (zebrafish)
│  ├─ Embryonic MSCs permissive; pediatric/adult not (human)
│  └─ NCSC molecular signature closest to Ewing tumors
│
EPIGENOMIC REPROGRAMMING
├─ De novo enhancer creation at GGAA microsatellites ─ [STRONG evidence]
├─ Displacement of wild-type ETS factors ────────────── [STRONG]
├─ EZH2/polycomb-mediated differentiation silencing ─── [STRONG]
├─ LSD1-dependent tumor suppressor repression ─────── [STRONG]
│
COOPERATING EVENTS (required for full transformation)
├─ NON-GENETIC: Pubertal IGF-1 → YAP1/TEAD ─────── [STRONG, mouse]
│  └─ Explains pubertal age peak and lack of genetic cooperators
├─ GENETIC: p53 loss (7-17% of tumors) ──────────── [STRONG]
├─ GENETIC: CDKN2A deletion (12-14%) ────────────── [STRONG]
├─ GENETIC: STAG2 loss → enhancer reprogramming ──── [STRONG]
├─ ANTI-APOPTOTIC: BCL2 family upregulation ──────── [MODERATE]
│
TUMOR ESTABLISHMENT AND PROGRESSION
├─ R-loop accumulation / BRCA1 impairment ───────── [STRONG]
├─ Intratumoral EWS-FLI1 activity heterogeneity ──── [STRONG]
│  └─ EWS-FLI1-low cells: metastatic, immune-evasive
├─ Unified DNA methylation identity ──────────────── [STRONG]
│
CLINICAL MANIFESTATION
├─ Skeletal tumors in adolescents (peak ages 10-19) ── [ESTABLISHED]
├─ Extraskeletal tumors in adults ≥40 ───────────── [QUALIFYING]
├─ Anatomic site preference (pelvis, femur, humerus) ─ [MODERATE]
└─ Ancestry-dependent incidence patterns ───────────── [STRONG]
```

**Strongest links:** The GGAA microsatellite neo-enhancer mechanism, the neural crest permissiveness in zebrafish, and the requirement for cooperating events are all supported by multiple independent studies with convergent evidence.

**Weakest/missing links:** (1) The exact chromatin marks defining the permissive vs. non-permissive progenitor state remain uncharacterized. (2) The mechanism by which adult-onset extraskeletal Ewing sarcomas arise is unexplained. (3) The relative roles of neural crest-derived vs. mesoderm-derived MSCs across different anatomic sites have not been directly compared. (4) The IGF-1/YAP1 mechanism has not been validated in human cells.

{{figure:causal_chain.png|caption=Mechanistic causal chain diagram from developmental context through epigenomic reprogramming to clinical manifestation}}

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Mechanistic Claim Tested | Key Finding | Context | Confidence |
|---|----------|--------------|-----------|--------------------------|-------------|---------|------------|
| 1 | [PMID: 39554045](https://pubmed.ncbi.nlm.nih.gov/39554045/) | Model organism (zebrafish) | **Supports** | NC cells are permissive for EWS-FLI1 | EWSR1-FLI1 reprograms NC cells to mesoderm-like state; generates lethal tumors | In vivo, zebrafish | High — first vertebrate tumor model |
| 2 | [PMID: 41072418](https://pubmed.ncbi.nlm.nih.gov/41072418/) | Model organism (zebrafish) | **Supports** | NC cells uniquely tolerate EWS-FLI1 | Targeted NC expression generates Ewing sarcomas | In vivo, zebrafish | High |
| 3 | [PMID: 41136396](https://pubmed.ncbi.nlm.nih.gov/41136396/) | In vitro + xenograft | **Supports** | Developmental timing determines permissiveness | Embryonic MSCs transform; pediatric/adult MSCs do not | Human cells | High — direct stage comparison |
| 4 | [PMID: 16357154](https://pubmed.ncbi.nlm.nih.gov/16357154/) | In vitro + in vivo (mouse) | **Supports** | MSC progenitors are permissive | EWS-FLI1 alone transforms BM-derived MPCs into Ewing-like tumors | Mouse MPCs | High — foundational study |
| 5 | [PMID: 18381423](https://pubmed.ncbi.nlm.nih.gov/18381423/) | In vitro | **Supports** | MSCs tolerate EWS-FLI1 | Stable expression, Ewing-like gene profile in hMSCs | Human MSCs | High |
| 6 | [PMID: 21559395](https://pubmed.ncbi.nlm.nih.gov/21559395/) | In vitro + computational | **Supports** | NCSC signature closest to Ewing | ESFT molecular signature more similar to hNCSC than MSC | Human cells | Moderate |
| 7 | [PMID: 25453903](https://pubmed.ncbi.nlm.nih.gov/25453903/) | In vitro + ChIP-seq | **Supports** | GGAA neo-enhancer mechanism | EWS-FLI1 creates de novo enhancers at GGAA repeats | Ewing cell lines | High |
| 8 | [PMID: 29977059](https://pubmed.ncbi.nlm.nih.gov/29977059/) | Review | **Supports** | Core epigenomic mechanism | Confirms GGAA microsatellite neo-enhancer as core Ewing feature | Comprehensive review | Moderate — review-level |
| 9 | [PMID: 36787739](https://pubmed.ncbi.nlm.nih.gov/36787739/) | Genomic/clinical | **Supports** | Germline GGAA length determines susceptibility | Longer alleles → more binding → RREB1 activation | Human, 6p25.1 locus | High |
| 10 | [PMID: 40080499](https://pubmed.ncbi.nlm.nih.gov/40080499/) | Model organism (mouse) | **Supports** | Pubertal IGF-1 as cooperating signal | Transient IGF-1 at pubertal levels enables stable transformation via YAP1 | Mouse limb MSCs | High |
| 11 | [PMID: 40414844](https://pubmed.ncbi.nlm.nih.gov/40414844/) | In vitro | **Supports** | YAP1/TEAD is pro-tumorigenic in Ewing | pncRNA destabilizes YAP1, exerts antitumor effects | Ewing cell lines | Moderate — independent validation |
| 12 | [PMID: 18974141](https://pubmed.ncbi.nlm.nih.gov/18974141/) | Model organism (mouse) | **Qualifies** | EWS-FLI1 insufficient alone | No tumors from EWS-FLI1 alone; requires p53 loss | Mouse limb bud | High |
| 13 | [PMID: 27735950](https://pubmed.ncbi.nlm.nih.gov/27735950/) | Model organism (mouse) | **Qualifies** | Anti-apoptotic cooperating events needed | BCL2 expression enables sarcoma formation | Mouse MSCs | High |
| 14 | [PMID: 33326102](https://pubmed.ncbi.nlm.nih.gov/33326102/) | Model organism (mouse) | **Supports** | Embryonic chondrogenic progenitors are tolerant | Embryonic eSZ cells contain EWS-FLI1-tolerant precursors | Mouse embryonic cells | Moderate |
| 15 | [PMID: 41950086](https://pubmed.ncbi.nlm.nih.gov/41950086/) | In vitro + multi-omic | **Supports** | STAG2 loss reprograms enhancer landscape | >40% binding sites lost at short repeats; gain at long repeats | Ewing cell lines | High |
| 16 | [PMID: 39487368](https://pubmed.ncbi.nlm.nih.gov/39487368/) | In vitro | **Supports** | STAG2-cohesin at GGAA neo-enhancers | Cohesin-STAG2 facilitates EWS-FLI1 repeat-to-promoter communication | Ewing cell lines | High |
| 17 | [PMID: 25223734](https://pubmed.ncbi.nlm.nih.gov/25223734/) | Genomic/clinical | **Qualifies** | Low mutational burden | STAG2 (17%), CDKN2A (12%), TP53 (7%) only recurrent mutations | 112 WGS samples | High |
| 18 | [PMID: 25010205](https://pubmed.ncbi.nlm.nih.gov/25010205/) | Genomic/clinical | **Qualifies** | Low mutational burden quantified | 0.15 mutations/Mb; STAG2 21.5% | 101 EFT | High |
| 19 | [PMID: 15930281](https://pubmed.ncbi.nlm.nih.gov/15930281/) | In vitro | **Competing** | Fusion determines phenotype regardless of origin | EWS-FLI1 in RD cells induces neural crest phenotype | RD rhabdomyosarcoma | Moderate — single cell line |
| 20 | [PMID: 15548687](https://pubmed.ncbi.nlm.nih.gov/15548687/) | In vitro | **Supports** | Histogenetic background matters | EWS-FLI1 in HEK293 fails to induce complete Ewing signature | HEK293 cells | Moderate |
| 21 | [PMID: 22959474](https://pubmed.ncbi.nlm.nih.gov/22959474/) | Clinical/epidemiological | **Qualifies** | Adult-onset challenges embryonic model | Adults ≥40: 66.1% extraskeletal vs 31.7% in younger (p<0.001) | 2,780 patients | High |
| 22 | [PMID: 29263409](https://pubmed.ncbi.nlm.nih.gov/29263409/) | Clinical | **Qualifies** | Older adults differ | Patients ≥50: 76.6% soft tissue origin | 77 patients ≥50y | Moderate |
| 23 | [PMID: 26173989](https://pubmed.ncbi.nlm.nih.gov/26173989/) | Clinical/epidemiological | **Qualifies** | Infant Ewing differs | Infants: 81.6% soft tissue, more PNET-like histology | 39 infants | Moderate — small cohort |
| 24 | [PMID: 33961701](https://pubmed.ncbi.nlm.nih.gov/33961701/) | Epidemiological | **Supports** | Developmental/germline context | Peak incidence ages 10-19; strong ancestry variation | 15,874 cases | High |
| 25 | [PMID: 32881892](https://pubmed.ncbi.nlm.nih.gov/32881892/) | GWAS | **Supports** | Germline susceptibility variants | 6 common loci; rare variation on common haplotypes | 733 cases | High |
| 26 | [PMID: 19289832](https://pubmed.ncbi.nlm.nih.gov/19289832/) | In vitro | **Supports** | EZH2 maintains undifferentiated state | EWS-FLI1 → EZH2 → silencing of differentiation genes | Ewing cells + MSCs | High |
| 27 | [PMID: 25625846](https://pubmed.ncbi.nlm.nih.gov/25625846/) | In vitro + computational | **Supports** | Polycomb target dysregulation | Aberrant HOX gene upregulation upon EWS-FLI1 expression | Stem cells | Moderate |
| 28 | [PMID: 24963049](https://pubmed.ncbi.nlm.nih.gov/24963049/) | In vitro + in vivo | **Supports** | Epigenetic maintenance of transformed state | LSD1 inhibition globally reverses EWS-FLI1 program | Xenograft models | High |
| 29 | [PMID: 29513652](https://pubmed.ncbi.nlm.nih.gov/29513652/) | In vitro | **Supports** | EWS-FLI1 causes DNA damage vulnerability | R-loop accumulation, BRCA1 impairment | Ewing cells | High |
| 30 | [PMID: 37279093](https://pubmed.ncbi.nlm.nih.gov/37279093/) | In vitro | **Supports** | Dual DNA damage/epigenetic vulnerability | Bifunctional PARP-HDAC inhibitor enhanced cytotoxicity | Ewing models | Moderate |
| 31 | [PMID: 17482132](https://pubmed.ncbi.nlm.nih.gov/17482132/) | In vitro | **Supports** | Ewing cells retain MSC identity | EWS-FLI1 silencing → convergence to MSC profile | Ewing cell lines | High |
| 32 | [PMID: 19208848](https://pubmed.ncbi.nlm.nih.gov/19208848/) | In vitro + in vivo | **Supports** | Cancer stem cells with MSC properties | CD133+ cells: serial transplantation, trilineage differentiation | Ewing tumors | High |
| 33 | [PMID: 32049009](https://pubmed.ncbi.nlm.nih.gov/32049009/) | Single-cell | **Qualifies** | Intratumoral EWS-FLI1 heterogeneity | Defined activity range for proliferation; extreme → hypoxia | Primary tumors | Moderate |
| 34 | [PMID: 40667384](https://pubmed.ncbi.nlm.nih.gov/40667384/) | Single-cell multi-omic | **Qualifies** | Intratumoral regulatory heterogeneity | Variably enriched regulatory modules across and within tumors | Primary tumors | High |
| 35 | [PMID: 31164960](https://pubmed.ncbi.nlm.nih.gov/31164960/) | In vitro | **Qualifies** | EWS-FLI1-low cells are metastatic | Low state → metastasis + PD-L1/PD-L2 immune evasion | Ewing cell lines | Moderate |
| 36 | [PMID: 33479225](https://pubmed.ncbi.nlm.nih.gov/33479225/) | Computational/clinical | **Supports** | Unified epigenetic identity | DNA methylation classifier distinguishes Ewing from 61 other sarcomas | >1,000 tumors | High |
| 37 | [PMID: 29572501](https://pubmed.ncbi.nlm.nih.gov/29572501/) | Clinical/molecular | **Supports** | Methylation defines true Ewing | 14/30 translocation-negative tumors confirmed as Ewing by methylation | >1,000 tumors | High |
| 38 | [PMID: 26650116](https://pubmed.ncbi.nlm.nih.gov/26650116/) | Review | **Supports** | Site-specific embryonic origins of BMSCs | Craniofacial (NC origin) vs appendicular (mesoderm origin) | Conceptual | Moderate — review |
| 39 | [PMID: 31852510](https://pubmed.ncbi.nlm.nih.gov/31852510/) | In vivo (rat) | **Supports** | NC-derived cells persist in adult BM | Postmigratory NCCs isolated from adult rat bone marrow | Adult rat | Moderate |
| 40 | [PMID: 30845695](https://pubmed.ncbi.nlm.nih.gov/30845695/) | In vitro + clinical | **Supports** | Anatomic site specificity | Ewing sarcomas predominantly arise in pelvic and stylopod bones | Developmental context | Moderate |
| 41 | [PMID: 18556509](https://pubmed.ncbi.nlm.nih.gov/18556509/) | Model organism (chick) | **Qualifies** | Parent gene expression in development | EWS in neural crest; FLI1 in endothelium — neither predicts fusion context | Chick embryo | Moderate |
| 42 | [PMID: 30042132](https://pubmed.ncbi.nlm.nih.gov/30042132/) | In vitro + epigenomics | **Supports** | GGAA enhancers are Ewing-specific | Silencing GGAA repeats prevents EWS-FLI1-mediated gene induction | Ewing cells | High |
| 43 | [PMID: 29091716](https://pubmed.ncbi.nlm.nih.gov/29091716/) | In vitro | **Supports** | Repeat-length dependency | Two microsatellite classes; length-dependent binding/activation | Ewing cells | High |

{{figure:final_assessment.png|caption=Comprehensive assessment visualization summarizing evidence strength across all hypothesis components after 5 iterations of investigation}}

---

## Alternative and Competing Models

### 1. Fusion-Determines-Phenotype Model (Competing)

**Claim:** EWS-FLI1 itself drives the neural crest/neuroectodermal phenotype regardless of the cell of origin. Hu-Lieskovan et al. 2005 ([PMID: 15930281](https://pubmed.ncbi.nlm.nih.gov/15930281/)) showed that EWS-FLI1 expression in rhabdomyosarcoma cells (mesodermal origin) changed morphology and upregulated neural crest differentiation genes, concluding that "the neural phenotype of Ewing's tumors is attributable to the EWS-FLI1 expression and the resultant phenotype resembles developing neural crest." However, Staege et al. 2004 ([PMID: 15548687](https://pubmed.ncbi.nlm.nih.gov/15548687/)) showed that "the EFT-specific gene expression profile is not just a consequence of EWS-FLI1 expression but depends on the histogenetic background of the EFT stem cell."

**Assessment:** This model is partially compatible — EWS-FLI1 induces some neural crest features broadly, but the full oncogenic program requires a specific progenitor context. It is best understood as a **parallel mechanism** (the fusion contributes to the phenotype) rather than a true alternative to the cell-of-origin model.

### 2. Genetic Cooperator-Centric Model (Complementary/Downstream)

**Claim:** Secondary mutations (STAG2, TP53, CDKN2A) are the decisive events enabling transformation. While these are the only recurrent mutations identified in WGS studies ([PMID: 25223734](https://pubmed.ncbi.nlm.nih.gov/25223734/); [PMID: 25010205](https://pubmed.ncbi.nlm.nih.gov/25010205/)), ~60-70% of tumors lack any identifiable cooperating mutation. The IGF-1/YAP1 discovery ([PMID: 40080499](https://pubmed.ncbi.nlm.nih.gov/40080499/)) suggests non-genetic cooperating events explain the majority of cases.

**Assessment:** This is a **downstream consequence** model — genetic cooperators act within the permissive progenitor, but are neither necessary (most tumors lack them) nor sufficient (they don't work in non-permissive cells) without the right cell state.

### 3. STAG2-Enhancer Reprogramming Model (Downstream Progression)

**Claim:** STAG2 loss is a key progression event that reshapes the EWS-FLI1 enhancer landscape ([PMID: 41950086](https://pubmed.ncbi.nlm.nih.gov/41950086/)). **Assessment:** This is a **downstream progression mechanism** operating within already-transformed cells, not an alternative cell-of-origin model.

### 4. YAP1/TAZ-EWS-FLI1 Antagonism Model (Stage-Dependent Qualifier)

Rodriguez-Nunez et al. 2020 ([PMID: 31880317](https://pubmed.ncbi.nlm.nih.gov/31880317/)) observed that "YAP1/TAZ transcription activity is inversely correlated with the EWS-FLI1 transcriptional signature," suggesting transcriptional antagonism in established tumors. However, Noorizadeh et al. 2025 ([PMID: 40080499](https://pubmed.ncbi.nlm.nih.gov/40080499/)) showed YAP1 plays a central role in INITIAL transformation.

**Assessment:** YAP1 likely has **stage-dependent roles** — promoting initial transformation but potentially opposing the EWS-FLI1 program in established tumors. This is a **qualifying observation** requiring time-course experiments to resolve.

### 5. Endothelial/Vascular Origin Model (Historical Alternative)

Historical descriptions of Ewing sarcoma as "endothelioma of bone" and recent observations of molecular similarity between EWS-FLI1-silenced Ewing cells and endothelial cells ([PMID: 40850534](https://pubmed.ncbi.nlm.nih.gov/40850534/)) suggest a possible endothelial or vascular origin. Coles et al. 2008 ([PMID: 18556509](https://pubmed.ncbi.nlm.nih.gov/18556509/)) noted that FLI1 is restricted to developing endothelial cells.

**Assessment:** This is a **historical alternative** that has been largely superseded by the MSC/NCSC evidence, but the endothelial gene expression overlap deserves further investigation as it may reflect shared developmental lineage.

---

## Knowledge Gaps

{{figure:knowledge_gaps.png|caption=Summary of major knowledge gaps in the permissive developmental cell-of-origin hypothesis}}

### Gap 1: Chromatin Features Defining the Permissive Window
- **Scope:** The specific histone modifications, chromatin accessibility patterns, and transcription factor repertoire that distinguish permissive embryonic progenitors from non-permissive differentiated cells remain uncharacterized.
- **Why it matters:** This is the central unresolved question of the hypothesis. Without identifying these features, the model remains descriptive rather than predictive.
- **What was checked:** Multiple studies characterize EWS-FLI1 binding patterns in Ewing cells (PMID: 25453903, 41950086, 30042132), but none have compared the pre-existing chromatin state of permissive vs. non-permissive progenitors before EWS-FLI1 introduction.
- **Resolution:** Single-cell ATAC-seq + RNA-seq of human embryonic vs. pediatric vs. adult MSCs before and immediately after EWS-FLI1 expression.

### Gap 2: Adult-Onset Extraskeletal Ewing Sarcoma Origin
- **Scope:** 13.8% of Ewing sarcomas occur in patients ≥40 years, predominantly extraskeletal (66.1%), with worse prognosis (HR for death 2.04, 95% CI 1.63-2.54) ([PMID: 22959474](https://pubmed.ncbi.nlm.nih.gov/22959474/)).
- **Why it matters:** If these tumors arise from residual embryonic progenitors, the hypothesis holds; if from de-differentiated adult cells, the model requires significant revision.
- **What was checked:** Epidemiological data confirm clinical differences across age groups; no molecular studies have compared the cell-of-origin in age-stratified cohorts.
- **Resolution:** DNA methylation profiling and single-cell analysis of adult-onset vs. pediatric Ewing tumors to determine shared or divergent epigenetic origin.

### Gap 3: Neural Crest vs. Mesoderm-Derived MSC Contributions Across Anatomic Sites
- **Scope:** BMSCs from craniofacial sites are neural crest-derived, while appendicular BMSCs are mesoderm-derived ([PMID: 26650116](https://pubmed.ncbi.nlm.nih.gov/26650116/)). Persistent neural crest precursors exist in adult bone marrow ([PMID: 31852510](https://pubmed.ncbi.nlm.nih.gov/31852510/)).
- **Why it matters:** This could reconcile the longstanding NCSC vs. MSC debate — some MSCs in certain skeletal sites ARE neural crest-derived.
- **What was checked:** The conceptual framework is established, but no studies have directly tested EWS-FLI1 permissiveness in site-specific MSC populations.
- **Resolution:** Compare EWS-FLI1 transformation efficiency in BMSCs isolated from craniofacial vs. appendicular sites with lineage tracing.

### Gap 4: IGF-1/YAP1 Mechanism Validation in Human Systems
- **Scope:** The IGF-1/YAP1 cooperating mechanism was demonstrated in mouse models ([PMID: 40080499](https://pubmed.ncbi.nlm.nih.gov/40080499/)) but has not been validated in human cells.
- **Why it matters:** Species-specific differences in IGF-1 signaling or YAP1 regulation could limit translational relevance.
- **What was checked:** Mouse studies are compelling; no human replication found.
- **Resolution:** Repeat IGF-1 exposure experiments in human embryonic MSCs and iPSC-derived mesenchymal progenitors.

### Gap 5: No Prospective Longitudinal Studies of Progenitor-to-Tumor Transition
- **Scope:** All evidence comes from retrospective tumor analysis or experimental EWS-FLI1 introduction.
- **Why it matters:** Direct observation of the natural transformation process would definitively establish the cell of origin.
- **What was checked:** Searched for longitudinal or lineage-tracing studies; none found in human or mammalian systems that track natural initiation.
- **Resolution:** Single-cell lineage tracing in conditional EWS-FLI1 mouse models with inducible expression at different developmental stages.

### Gap 6: Stage-Dependent Role of YAP1
- **Scope:** YAP1 promotes initial transformation ([PMID: 40080499](https://pubmed.ncbi.nlm.nih.gov/40080499/)) but may oppose EWS-FLI1 in established tumors ([PMID: 31880317](https://pubmed.ncbi.nlm.nih.gov/31880317/)).
- **Why it matters:** This apparent contradiction must be resolved for therapeutic targeting of YAP1/TEAD.
- **What was checked:** Both studies are robust but address different temporal windows.
- **Resolution:** Time-course experiments comparing YAP1 function during transformation initiation vs. in established tumor maintenance.

### Gap 7: Source-Level Absences
- **What was checked:** No relevant GenCC or ClinGen entries for EWS-FLI1 cell-of-origin classification; no clinical trial data specifically testing cell-of-origin-based therapeutic stratification; no single-cell multi-omic atlas comparing Ewing tumors across developmental age groups.

---

## Discriminating Tests

### Test 1: Pre-Transformation Chromatin Atlas
- **Design:** ATAC-seq + CUT&Tag (H3K27ac, H3K4me1, H3K27me3) in human embryonic MSCs, pediatric MSCs, and adult MSCs BEFORE introducing EWS-FLI1, followed by time-course analysis post-introduction.
- **Model system:** Human primary cells + iPSC-derived mesenchymal progenitors at defined differentiation stages.
- **Expected result:** Permissive cells will have pre-existing open chromatin at GGAA microsatellites and developmental enhancers; non-permissive cells will lack these features.
- **Discriminates:** Cell-of-origin model (pre-existing chromatin determines fate) vs. fusion-determines-phenotype model (chromatin state irrelevant).

### Test 2: Site-Specific MSC Transformation Assay
- **Design:** Isolate BMSCs from craniofacial, axial, and appendicular sites; introduce EWS-FLI1; compare transformation efficiency, transcriptome, and tumorigenicity.
- **Biomarkers:** CD271 (LNGFR) for NC-derived MSCs vs. PDGFRα for mesoderm-derived MSCs.
- **Expected result:** NC-derived craniofacial MSCs will show highest permissiveness; appendicular MSCs will show intermediate permissiveness.
- **Discriminates:** Neural crest vs. generic mesenchymal origin.

### Test 3: IGF-1/YAP1 Validation in Human Progenitors
- **Design:** Expose human embryonic MSCs expressing EWS-FLI1 to IGF-1 at pubertal concentrations (400-800 ng/mL); assess YAP1 activation, transformation, and tumorigenicity ± YAP1/TEAD inhibitors (e.g., verteporfin or K-975).
- **Expected result:** IGF-1 will enable transformation in human embryonic MSCs; YAP1 inhibition will block it.
- **Discriminates:** IGF-1/YAP1 as the universal cooperating signal vs. mouse-specific artifact.

### Test 4: Age-Stratified Methylation Profiling
- **Design:** Illumina EPIC methylation arrays on pediatric skeletal (n≥20), pediatric extraskeletal (n≥20), adult (≥40) extraskeletal (n≥20), and adult skeletal (n≥10) Ewing sarcomas, analyzed by the validated sarcoma methylation classifier.
- **Expected result:** If all share the same methylation class, they likely share the same cell of origin; divergent methylation patterns would suggest distinct pathogenic routes for adult-onset disease.
- **Discriminates:** Unified cell-of-origin model vs. age-dependent dual-origin model.

### Test 5: Temporal YAP1 Function Analysis
- **Design:** Conditional YAP1 knockout or TEAD inhibition at defined time points: (a) during initial IGF-1-mediated transformation; (b) in established Ewing tumors in vivo.
- **Expected result:** YAP1 loss will prevent transformation (a) but potentially promote EWS-FLI1-driven programs in established tumors (b).
- **Discriminates:** Resolves the paradox of YAP1 as cooperating factor vs. EWS-FLI1 antagonist; determines therapeutic window for YAP1/TEAD inhibitors.

---

## Curation Leads

*All leads below require curator verification before KB integration.*

### Candidate Evidence References to Add

| PMID | Snippet for Verification | Direction | Explanation |
|------|--------------------------|-----------|-------------|
| [40080499](https://pubmed.ncbi.nlm.nih.gov/40080499/) | "transient exposure to IGF-1 concentrations mimicking serum levels during puberty reprograms limb-derived mesenchymal cells of EWS::FLI1-mutant mice to stable transformation and tumorigenicity" | SUPPORT | Identifies pubertal IGF-1 as non-genetic cooperating signal |
| [39554045](https://pubmed.ncbi.nlm.nih.gov/39554045/) | "Single-cell analysis of tumor initiation shows that EWSR1::FLI1 reprograms neural crest-derived cells to a mesoderm-like state" | SUPPORT | First in vivo vertebrate NC permissiveness model |
| [41950086](https://pubmed.ncbi.nlm.nih.gov/41950086/) | "STAG2 loss eliminates over 40% of EWS-FLI1 binding sites, predominantly at enhancers containing short (1-4) GGAA repeats" | SUPPORT/QUALIFY | STAG2 loss reshapes enhancer landscape |
| [36787739](https://pubmed.ncbi.nlm.nih.gov/36787739/) | "EwS-affected individuals had longer alleles (>135 bp) with more GGAA repeats" | SUPPORT | Germline-somatic interaction at susceptibility locus |
| [22959474](https://pubmed.ncbi.nlm.nih.gov/22959474/) | "Patients ≥40 years of age were more likely to have extra-skeletal tumors (66.1% vs. 31.7%; p < 0.001)" | QUALIFY | Adult-onset disease challenges purely embryonic model |

### Candidate Pathophysiology Nodes/Edges
- **New node:** YAP1/TEAD complex as cooperating factor in transformation
- **New edge:** Pubertal IGF-1 → YAP1 activation → EWS-FLI1 transformation
- **New edge:** STAG2 loss → GGAA repeat binding redistribution → enhanced multimeric enhancer activity
- **New edge:** Germline GGAA repeat length → EWSR1-FLI1 neo-enhancer strength → RREB1/RAS-MAPK signaling
- **New edge:** EWS-FLI1 → EZH2 upregulation → Polycomb-mediated differentiation silencing

### Candidate Ontology Terms
- **Cell types:** CL:0000134 (mesenchymal stem cell), CL:0000333 (neural crest cell), CL:0008019 (mesenchymal progenitor cell)
- **Biological processes:** GO:0045165 (cell fate commitment), GO:0016568 (chromatin modification), GO:0035556 (intracellular signal transduction — IGF-1/YAP1 axis)
- **Anatomic context:** UBERON:0002371 (bone marrow), UBERON:0001474 (bone element)

### Candidate Status Change
- **Current:** EMERGING
- **Recommended:** Retain EMERGING. Consider upgrade to ESTABLISHED once: (1) chromatin features defining permissiveness are characterized in human cells, and (2) the IGF-1/YAP1 mechanism is validated in human progenitors.

### Candidate Knowledge Gaps for KB Entry
1. Chromatin features defining the permissive progenitor state (central unknown)
2. Origin of adult-onset extraskeletal Ewing sarcoma (embryonic remnant vs. distinct pathway)
3. Stage-dependent role of YAP1 (transformation cooperator vs. established tumor suppressor)
4. Human validation of IGF-1/YAP1 cooperating mechanism
5. Site-specific MSC embryonic origins and transformation efficiency correlation
6. No clinical trial data for cell-of-origin-based therapeutic stratification

### Discussion Prompts for Curators
- Should the hypothesis description be updated to explicitly include IGF-1/YAP1 as a named cooperating mechanism?
- Should a sub-hypothesis node be created for "pubertal growth factor cooperating signal model"?
- Does the adult-onset extraskeletal Ewing sarcoma data warrant a qualifier node limiting the hypothesis scope to pediatric/adolescent skeletal disease?
- Should the GGAA microsatellite germline-somatic interaction be elevated to a separate linked hypothesis?

---

## Limitations of This Report

1. **Model system bias:** The strongest evidence (zebrafish, mouse) may not fully recapitulate human biology. The zebrafish neural crest model, while powerful, represents a phylogenetically distant species.
2. **Retrospective inference:** Most evidence for the cell of origin is inferred from expression profiling of established tumors or experimental introduction of EWS-FLI1 into candidate cells. No prospective longitudinal study has tracked the natural transformation process in any mammalian system.
3. **Publication bias:** Studies demonstrating permissiveness in specific cell types may be overrepresented compared to negative results where EWS-FLI1 fails to transform candidate populations.
4. **Small sample sizes:** The IGF-1/YAP1 study, while mechanistically compelling, has not been validated in large cohorts or human systems.
5. **Ewing-like sarcomas excluded:** This analysis focused on classical FET-ETS Ewing sarcoma. CIC-DUX4, BCOR-CCNB3, and other round cell sarcomas have distinct biology and were not systematically evaluated as they represent different molecular entities.
6. **Search scope:** Literature searches were conducted through PubMed; preprints, conference abstracts, and non-indexed journals were not systematically covered. The search date was May 2026.
