---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-24T13:26:14.495677'
end_time: '2026-01-24T13:32:05.631432'
duration_seconds: 351.14
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Medullary Thyroid Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Medullary Thyroid Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Medullary Thyroid Carcinoma**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


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

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Medullary Thyroid Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Medullary Thyroid Carcinoma**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


# Disease Pathophysiology Research Report

## Target Disease
- Disease Name: Medullary Thyroid Carcinoma (MTC)
- MONDO ID: 
- Category: Neuroendocrine carcinoma of the thyroid gland

## Pathophysiology Description
Medullary thyroid carcinoma arises from parafollicular C-cells of neural crest origin and characteristically secretes calcitonin and often carcinoembryonic antigen (CEA). Approximately 25% of cases are hereditary due to germline RET mutations (MEN2 syndromes), while ~75% are sporadic with frequent somatic RET mutations; RAS family mutations (HRAS/KRAS/NRAS) are the predominant alternative drivers in RET-wild-type tumors (mutually exclusive with RET) (gild2023medullarythyroidcancer pages 1-2, lagana2023theevolvingtreatment pages 1-3). Constitutive activation of the RET receptor tyrosine kinase engages RAS/MAPK and PI3K/AKT/mTOR signaling, driving proliferation, survival, migration, and altered differentiation; RAS mutations similarly activate these pathways (gild2023medullarythyroidcancer pages 3-4, barletta2021genomicsandepigenomics pages 10-12, lagana2023theevolvingtreatment pages 1-3). Epigenetic dysregulation (DNA methylation changes, overexpression of EZH2 and SMYD3, and miRNA alterations such as miR-375) correlates with aggressive phenotypes and prognosis (sahakian2023molecularbasisand pages 13-15, barletta2021genomicsandepigenomics pages 10-12). 

Clinically, MTC exhibits hormone-mediated syndromes: calcitonin (and related peptides) are implicated in diarrhea and flushing; ectopic ACTH secretion can cause Cushing syndrome in a minority of patients. Surgical resection is the only curative option for localized disease; systemic therapy is reserved for progressive/symptomatic metastatic disease, where selective RET inhibitors (selpercatinib, pralsetinib) now provide high response rates and durable control with improved tolerability compared to multikinase inhibitors (MKIs) such as vandetanib and cabozantinib (lagana2023theevolvingtreatment pages 3-5, gild2023medullarythyroidcancer pages 1-2, lagana2023theevolvingtreatment pages 1-3, sahakian2023molecularbasisand pages 15-16).

Key recent expert consensus emphasizes universal germline RET testing for all MTC patients, somatic profiling to guide targeted therapy, and recognition of acquired resistance mechanisms (on-target RET mutations and bypass signaling) that motivate next-generation inhibitors and rational combinations (gild2023medullarythyroidcancer pages 1-2, gild2023medullarythyroidcancer pages 10-10, lagana2023theevolvingtreatment pages 1-3).

| Category | Entity (ontology / identifier) | Role in MTC Pathophysiology | Key Evidence (DOI URL, year; citation) |
|---|---|---|---|
| Driver oncogene | RET (HGNC:9967) | Germline and somatic activating point mutations, indels and fusions → constitutive RTK activity that drives proliferation, survival and migration via downstream RAS/MAPK and PI3K/AKT signaling | DOI: https://doi.org/10.1186/s12964-024-01837-x (2024); DOI: https://doi.org/10.3390/cancers15194865 (2023) (zhang2024moleculargeneticstherapeutics pages 5-6, sahakian2023molecularbasisand pages 1-2) |
| Oncogenes (mutually exclusive with RET) | HRAS / KRAS / NRAS (HGNC:5005, 6407, 7771) | Frequent drivers in RET-wild-type sporadic MTC; activate MAPK/PI3K pathways; associated with distinct biology and generally less aggressive phenotype vs RET M918T | DOI: https://doi.org/10.1007/s12022-021-09664-3 (2021); review summarizing prevalence (2023) (barletta2021genomicsandepigenomics pages 3-4, lagana2023theevolvingtreatment pages 1-3) |
| Cell type / origin | Parafollicular C-cell (CL:0000198) — Thyroid (UBERON:0002046) | Neuroendocrine origin; C-cells synthesize and secrete calcitonin and often CEA — used as sensitive tumor biomarkers and mediators of hormone-related symptoms (diarrhea, flushing) | DOI: https://doi.org/10.1210/endrev/bnad013 (2023); clinical summaries (2023) (gild2023medullarythyroidcancer pages 1-2, lagana2023theevolvingtreatment pages 1-3) |
| Secreted biomarkers / chemical entities | Calcitonin (UniProt P01258), CEA (protein) | Serum calcitonin highly sensitive for disease burden; rising CEA indicates progression/dedifferentiation and paraneoplastic syndromes (diarrhea, flushing, rare ectopic ACTH) | Clinical/guideline summaries (2023) (gild2023medullarythyroidcancer pages 1-2, lagana2023theevolvingtreatment pages 1-3) |
| Signaling pathway (GO) | GO:0007169 — transmembrane receptor protein tyrosine kinase signaling | Canonical RET signaling node initiating downstream cascades (PLCγ, Src, RAS/MAPK, PI3K/AKT) that mediate proliferation, survival and migration | Mechanistic reviews (2023–2024) DOI: https://doi.org/10.1210/endrev/bnad013 (2023), https://doi.org/10.1186/s12964-024-01837-x (2024) (gild2023medullarythyroidcancer pages 3-4, zhang2024moleculargeneticstherapeutics pages 5-6) |
| Signaling pathway (GO) | GO:0000187 — activation of MAPK activity | MAPK/ERK cascade is a principal downstream effector of RET and RAS mutations driving proliferation and tumor growth | Mechanistic reviews and genomic studies (2021–2023) (barletta2021genomicsandepigenomics pages 3-4, gild2023medullarythyroidcancer pages 3-4) |
| Signaling pathway (GO) | GO:0043491 — protein kinase B (AKT) signaling | PI3K→AKT→mTOR axis activated downstream of RET/RAS; implicated in survival, metabolism and therapeutic targeting (mTOR pathway activation in some MTC) | Genomic/functional reports (2021, 2023) (barletta2021genomicsandepigenomics pages 10-12, gild2023medullarythyroidcancer pages 3-4) |
| Epigenetic regulators | EZH2 (HGNC:3527), SMYD3 (HGNC:15564); DNA methylation (GO:0006306); miR-375 (miRNA) | Overexpression of EZH2/SMYD3 and DNA methylation changes associate with aggressive behavior; miR-375 deregulation linked to prognosis and drug sensitivity | Epigenomics reviews and studies DOI: https://doi.org/10.3390/cancers15194865 (2023); https://doi.org/10.1007/s12022-021-09664-3 (2021) (sahakian2023molecularbasisand pages 13-15, barletta2021genomicsandepigenomics pages 10-12) |
| Tumor microenvironment / immune | PSMA expression, low-TMB immune features; investigational CAR-T targeting CEA/calcitonin/RET | MTC shows variable immune features; targeted/theranostic approaches (PSMA PET/PRRT, CAR-T) and combined strategies under active investigation | Translational/theranostic reviews (2023) DOI: https://doi.org/10.1210/endrev/bnad013 (2023) (gild2023medullarythyroidcancer pages 10-10) |
| Approved multikinase inhibitors | Vandetanib (targets RET, VEGFR, EGFR) — clinical benefit: ZETA trial PFS ~30.5 vs 19.3 mo (placebo); notable off‑target AEs (diarrhea, rash, QT) | Multi-target blockade reduces tumor progression but causes dose-limiting off-target toxicity; better responses in RET‑positive cases | Summary review with trial metrics DOI: https://doi.org/10.3390/cancers15194865 (2023) (sahakian2023molecularbasisand pages 15-16) |
| Approved multikinase inhibitor | Cabozantinib (targets RET, MET, VEGFR2, others) — EXAM: PFS ~11.2 vs 4.0 mo (placebo); high rates of dose reduction | Broad kinase inhibition yields PFS benefit but frequent toxicity and limited OS benefit historically | Trial summary and review DOI: https://doi.org/10.3390/cancers15194865 (2023) (sahakian2023molecularbasisand pages 15-16) |
| Selective RET inhibitors | Selpercatinib (LOXO-292) — high ORR (≈69–82% in trials), durable responses and favorable tolerability; Pralsetinib (BLU-667) — ORR ~60–71% | Potent on-target RET inhibition with higher ORR/PFS and improved QoL vs MKIs; central to modern management of RET‑mutant MTC | Clinical trial reports and long-term updates DOI: https://doi.org/10.1056/NEJMoa2005651 (2020), long-term JCO update DOI: https://doi.org/10.1200/jco.23.02503 (2024); reviews (gild2023medullarythyroidcancer pages 10-10, sahakian2023molecularbasisand pages 15-16) |
| Resistance mechanisms | On-target (gatekeeper V804L/M, solvent-front), off‑target/bypass pathway activation, RTK indels/compound RET mutations | Resistance emerges via secondary RET kinase-domain mutations or activation of bypass pathways (e.g., MET/RAS/PI3K) — motivates next‑generation RET inhibitors and combination strategies | Resistance-focused reviews DOI: https://doi.org/10.1186/s12964-024-01837-x (2024); translational reviews (2023) (zhang2024moleculargeneticstherapeutics pages 5-6, gild2023medullarythyroidcancer pages 10-10) |


*Table: Concise reference table mapping key genes, pathways, cell types, epigenetic factors, microenvironment notes, approved therapies and resistance mechanisms in medullary thyroid carcinoma with primary evidence DOI links and recent review citations (2021–2024).*

## 1. Core Pathophysiology
- Primary mechanisms: Activating RET mutations (germline in MEN2; somatic in many sporadic cases) or, in RET-wild-type tumors, activating RAS mutations, produce constitutive receptor tyrosine kinase or downstream RAS pathway signaling. RET activates PLCγ/PKC, Src-related kinases, RAS/MAPK and PI3K/AKT pathways, driving oncogenic programs (gild2023medullarythyroidcancer pages 3-4, lagana2023theevolvingtreatment pages 1-3). RAS-mutant MTC shows mTOR pathway activation (barletta2021genomicsandepigenomics pages 10-12).
- Dysregulated pathways: RAS/MAPK (MAPK/ERK) and PI3K/AKT/mTOR; additional RET-linked nodes include PLCγ/PKC and Src (gild2023medullarythyroidcancer pages 3-4, barletta2021genomicsandepigenomics pages 10-12).
- Affected cellular processes: Cell proliferation, survival/apoptosis resistance, migration/invasion, and neuroendocrine differentiation/secretion (calcitonin/CEA) (gild2023medullarythyroidcancer pages 3-4, gild2023medullarythyroidcancer pages 1-2, lagana2023theevolvingtreatment pages 1-3).

Notable recent synthesis: “RET is… a receptor tyrosine kinase that activates multiple downstream pathways including… PI3K and MAPK; activating mutations… cause constitutive signaling” (Endocrine Reviews 2023) (gild2023medullarythyroidcancer pages 3-4). A 2024 review underscores RET as “the central initiating driver in hereditary and many sporadic MTCs,” with detailed mechanistic activation models and clinical-genetic correlations (Cell Communication and Signaling, Sep 2024) (zhang2024moleculargeneticstherapeutics pages 5-6).

## 2. Key Molecular Players
- Genes/Proteins (HGNC symbols):
  - RET (proto-oncogene receptor tyrosine kinase): germline (MEN2A/B, FMTC) and somatic mutations (e.g., M918T; gatekeeper V804L/M; indels). RET mutations associate with higher odds of nodal and distant metastasis, advanced stage, recurrence, and mortality; exon 15–16 mutations (e.g., M918T) confer worst outcomes (barletta2021genomicsandepigenomics pages 3-4).
  - RAS family: HRAS, KRAS, NRAS; frequent in RET-wild-type sporadic MTC and generally less aggressive than RET M918T–mutant disease (gild2023medullarythyroidcancer pages 3-4, barletta2021genomicsandepigenomics pages 3-4).
  - Epigenetic regulators: EZH2, SMYD3; overexpressed in aggressive tumors (barletta2021genomicsandepigenomics pages 10-12). miR-375 is a negative prognostic marker; miR-153-3p acts as a RET-regulated tumor suppressor (gild2023medullarythyroidcancer pages 10-10, barletta2021genomicsandepigenomics pages 10-12).
- Chemical Entities (selected): calcitonin (biomarker and symptom mediator), CEA (biomarker); drugs: vandetanib, cabozantinib (MKIs), selpercatinib, pralsetinib (selective RET inhibitors) (lagana2023theevolvingtreatment pages 3-5, lagana2023theevolvingtreatment pages 1-3, sahakian2023molecularbasisand pages 15-16).
- Cell Types (CL terms): Parafollicular C-cells (CL:0000198) (gild2023medullarythyroidcancer pages 1-2).
- Anatomical Locations (UBERON terms): Thyroid gland (UBERON:0002046) and regional/distant metastatic sites (cervical nodes, liver, lung, bone) (gild2023medullarythyroidcancer pages 1-2, lagana2023theevolvingtreatment pages 1-3).

Representative data points: “Somatic RET alterations occur in around 60% of sporadic MTC, with many of the remainder driven by RAS mutations… RAS-mutated tumors are described as less aggressive than tumors with RET p.Met918Thr” (Endocrine Reviews 2023) (gild2023medullarythyroidcancer pages 3-4).

## 3. Biological Processes (GO annotations)
- Transmembrane receptor protein tyrosine kinase signaling (GO:0007169) via RET (gild2023medullarythyroidcancer pages 3-4, lagana2023theevolvingtreatment pages 1-3).
- Activation of MAPK activity (GO:0000187) downstream of RET/RAS (gild2023medullarythyroidcancer pages 3-4, barletta2021genomicsandepigenomics pages 10-12, lagana2023theevolvingtreatment pages 1-3).
- Protein kinase B (AKT) signaling (GO:0043491) and mTOR pathway activation (barletta2021genomicsandepigenomics pages 10-12).
- DNA methylation (GO:0006306) changes associated with prognosis; chromatin modification via EZH2/SMYD3 (sahakian2023molecularbasisand pages 13-15, barletta2021genomicsandepigenomics pages 10-12).
- Neuroendocrine hormone secretion processes (calcitonin/CEA) contributing to systemic symptoms (gild2023medullarythyroidcancer pages 1-2, lagana2023theevolvingtreatment pages 1-3).

Directly supported elements include the RET-driven activation of MAPK and PI3K cascades (Endocrine Reviews 2023) and epigenetic alterations linked to aggressiveness (Endocrine Pathology 2021; Cancers 2023) (gild2023medullarythyroidcancer pages 3-4, barletta2021genomicsandepigenomics pages 10-12, sahakian2023molecularbasisand pages 13-15).

## 4. Cellular Components
- Plasma membrane: RET receptor localization and activation (gild2023medullarythyroidcancer pages 3-4).
- Cytoplasm: MAPK/ERK and PI3K/AKT/mTOR signaling cascades (barletta2021genomicsandepigenomics pages 10-12).
- Nucleus/chromatin: epigenetic regulation (EZH2/SMYD3), transcriptional responses; miRNA-mediated post-transcriptional control (barletta2021genomicsandepigenomics pages 10-12, gild2023medullarythyroidcancer pages 10-10).
- Extracellular space: calcitonin/CEA secretion and biomarker monitoring (gild2023medullarythyroidcancer pages 1-2, lagana2023theevolvingtreatment pages 1-3).

## 5. Disease Progression
- Sequence of events: In hereditary disease, diffuse C-cell hyperplasia (premalignant) can progress to microcarcinoma, invasive carcinoma, nodal metastases, and distant metastases. Somatic RET (often M918T) or RAS mutations drive sporadic tumorigenesis, with RET mutations correlating strongly with advanced stage and metastasis (barletta2021genomicsandepigenomics pages 10-12, lagana2023theevolvingtreatment pages 1-3). “Cervical nodal involvement at initial surgery carries a poor cure rate (~10%)” (Curr Treat Options Oncol 2023) (lagana2023theevolvingtreatment pages 3-5).
- Staging phases: localized intrathyroidal disease, regional nodal spread, and distant metastasis (liver, lung, bone) are typical trajectories; many metastatic cases exhibit indolent courses, necessitating careful selection for systemic therapy (lagana2023theevolvingtreatment pages 3-5, lagana2023theevolvingtreatment pages 1-3).

## 6. Phenotypic Manifestations
- Key clinical phenotypes (HP terms):
  - Chronic diarrhea (HP:0002014) and flushing (HP term for facial flushing), often linked to calcitonin and neuropeptides (lagana2023theevolvingtreatment pages 3-5, lagana2023theevolvingtreatment pages 1-3).
  - Ectopic ACTH secretion causing Cushing syndrome (HP:0003119) (lagana2023theevolvingtreatment pages 3-5).
  - Thyroid nodule and cervical lymphadenopathy; elevated serum calcitonin and CEA (biochemical phenotypes) (gild2023medullarythyroidcancer pages 1-2, lagana2023theevolvingtreatment pages 1-3).

“Systemic symptoms arise from hormonal secretion (calcitonin and calcitonin gene-related peptide) causing diarrhea and flushing; occasional ectopic ACTH/Cushing’s is described” (Curr Treat Options Oncol 2023) (lagana2023theevolvingtreatment pages 3-5).

## Expert Opinions and Authoritative Guidance
- Universal germline RET testing is recommended for all MTC patients to identify MEN2 and guide prophylactic and therapeutic decisions (Endocrine Reviews 2023) (gild2023medullarythyroidcancer pages 1-2).
- Somatic profiling (RET vs RAS) informs selection of selective RET inhibitors vs alternative strategies; selective RET inhibitors are preferred for RET-mutant disease due to higher efficacy and tolerability compared with MKIs (lagana2023theevolvingtreatment pages 1-3).
- Surveillance and local therapies are appropriate for indolent metastatic disease; systemic therapy is noncurative and reserved for symptomatic or RECIST-progressive disease (lagana2023theevolvingtreatment pages 3-5).

## Relevant Statistics and Data (recent)
- Genetics/epidemiology: Sporadic ~75% vs hereditary ~25% of MTC; somatic RET alterations ~60% of sporadic tumors; RET and RAS together account for ~90% of MTCs (Endocrine Reviews 2023; Curr Treat Options Oncol 2023) (gild2023medullarythyroidcancer pages 3-4, lagana2023theevolvingtreatment pages 1-3).
- Prognostic impact: Meta-analysis—RET mutations associate with higher odds of lymph node metastasis (OR 3.61), distant metastasis (OR 2.85), advanced stage (OR 3.25), recurrence (OR 3.01), mortality (OR 2.43); exons 15–16 (including M918T) confer worst outcomes (Endocrine Pathology 2021) (barletta2021genomicsandepigenomics pages 3-4).
- MKIs: Vandetanib (ZETA): PFS 30.5 vs 19.3 months (placebo); cabozantinib (EXAM): PFS 11.2 vs 4.0 months; notable off‑target toxicities and frequent dose modifications (Cancers 2023) (sahakian2023molecularbasisand pages 15-16).
- Selective RET inhibitors:
  - Selpercatinib (NEJM 2020; LIBRETTO-001): ORR 69% in previously treated RET-mutant MTC and 73% in MKI‑naïve; 1‑year PFS 82% and 92%, respectively; grade ≥3 AEs included hypertension (21%), elevated ALT (11%), AST (9%), hyponatremia (8%), diarrhea (6%); 2% discontinued for drug-related AEs (published Aug 2020; https://doi.org/10.1056/NEJMoa2005651) (barletta2021genomicsandepigenomics pages 6-7).
  - Long-term update (JCO 2024): ORR 82.5% among MKI‑naïve MTC; median PFS not reached (MKI‑naïve) and 41.4 months (pretreated); 3‑year PFS 75.2% (MKI‑naïve) (published Sep 2024; https://doi.org/10.1200/JCO.23.02503) (gild2023medullarythyroidcancer pages 10-10).
  - Patient-reported outcomes: clinically meaningful improvement in diarrhea in 43.5% overall (LIBRETTO‑001 PROs) (The Oncologist 2022; https://doi.org/10.1002/onco.13977) (lagana2023theevolvingtreatment pages 3-5).
  - Pralsetinib (ARROW): ORR 60% (pretreated) and 71% (treatment‑naïve); disease control rates 93–100% (Cancers 2023) (sahakian2023molecularbasisand pages 15-16).

## Therapy Mechanisms Linked to Biology, and Resistance
- MKIs (vandetanib, cabozantinib) inhibit RET and multiple other kinases (VEGFR, EGFR, MET), providing PFS benefit but with substantial off‑target toxicity; responses are higher in RET‑positive tumors (sahakian2023molecularbasisand pages 15-16).
- Selective RET inhibitors (selpercatinib, pralsetinib) provide potent on-target RET blockade with high response rates, prolonged PFS, and improved tolerability and HRQoL (barletta2021genomicsandepigenomics pages 6-7, gild2023medullarythyroidcancer pages 10-10, lagana2023theevolvingtreatment pages 3-5).
- Resistance mechanisms: on-target RET mutations (gatekeeper V804L/M, solvent-front) and off-target/bypass activation (e.g., MET/RAS/PI3K) are recognized; development of next-generation RET inhibitors and combinations is ongoing (Endocrine Reviews 2023; Cell Communication and Signaling 2024) (gild2023medullarythyroidcancer pages 10-10, zhang2024moleculargeneticstherapeutics pages 5-6).

## Structured Annotations
- Genes/Proteins (HGNC): RET; HRAS; KRAS; NRAS; EZH2; SMYD3; biomarkers calcitonin, CEA (gild2023medullarythyroidcancer pages 3-4, barletta2021genomicsandepigenomics pages 10-12, lagana2023theevolvingtreatment pages 1-3).
- GO Biological Processes: GO:0007169 (RTK signaling); GO:0000187 (activation of MAPK activity); GO:0043491 (protein kinase B signaling); GO:0006306 (DNA methylation) (gild2023medullarythyroidcancer pages 3-4, barletta2021genomicsandepigenomics pages 10-12).
- Cell Types (CL): Parafollicular C-cell (CL:0000198) (gild2023medullarythyroidcancer pages 1-2).
- Anatomical Locations (UBERON): Thyroid gland (UBERON:0002046); common metastatic sites (regional lymph nodes, liver, lung, bone) (gild2023medullarythyroidcancer pages 1-2, lagana2023theevolvingtreatment pages 1-3).
- Phenotypes (HP): Diarrhea (HP:0002014), Flushing, Cushing syndrome (HP:0003119) (lagana2023theevolvingtreatment pages 3-5).
- Chemical Entities (CHEBI examples): drugs—vandetanib, cabozantinib, selpercatinib, pralsetinib; hormones—calcitonin (sahakian2023molecularbasisand pages 15-16, barletta2021genomicsandepigenomics pages 6-7, gild2023medullarythyroidcancer pages 10-10).

## Evidence Items with URLs and Publication Dates
- Gild ML et al. Medullary Thyroid Cancer: Updates and Challenges. Endocrine Reviews. May 2023. URL: https://doi.org/10.1210/endrev/bnad013 (gild2023medullarythyroidcancer pages 1-2, gild2023medullarythyroidcancer pages 3-4, gild2023medullarythyroidcancer pages 10-10)
- Laganà M et al. The Evolving Treatment Landscape of MTC. Current Treatment Options in Oncology. Nov 18, 2023. URL: https://doi.org/10.1007/s11864-023-01145-5 (lagana2023theevolvingtreatment pages 1-3, lagana2023theevolvingtreatment pages 3-5)
- Sahakian N et al. Molecular Basis and Natural History of MTC. Cancers. Oct 5, 2023. URL: https://doi.org/10.3390/cancers15194865 (sahakian2023molecularbasisand pages 1-2, sahakian2023molecularbasisand pages 13-15, sahakian2023molecularbasisand pages 15-16)
- Barletta JA et al. Genomics and Epigenomics of MTC. Endocrine Pathology. Jan 2021. URL: https://doi.org/10.1007/s12022-021-09664-3 (barletta2021genomicsandepigenomics pages 10-12, barletta2021genomicsandepigenomics pages 3-4)
- Wirth LJ et al. Efficacy of Selpercatinib in RET‑Altered Thyroid Cancers. NEJM. Aug 27, 2020. URL: https://doi.org/10.1056/NEJMoa2005651 (barletta2021genomicsandepigenomics pages 6-7)
- Wirth LJ et al. Durability of Response With Selpercatinib (LIBRETTO‑001). J Clin Oncol. Sep 2024. URL: https://doi.org/10.1200/JCO.23.02503 (gild2023medullarythyroidcancer pages 10-10)
- Wirth LJ et al. Patient-Reported Outcomes With Selpercatinib (LIBRETTO‑001). The Oncologist. Sep 2022. URL: https://doi.org/10.1002/onco.13977 (lagana2023theevolvingtreatment pages 3-5)

Quoted statements
- “RET is… a receptor tyrosine kinase that activates multiple downstream pathways including… PI3K and MAPK; activating mutations… cause constitutive signaling” (Endocrine Reviews 2023) (gild2023medullarythyroidcancer pages 3-4).
- “Selpercatinib showed durable efficacy with mainly low-grade toxic effects” with ORR 69–73% and 1‑year PFS 82–92% in RET‑mutant MTC (NEJM 2020) (barletta2021genomicsandepigenomics pages 6-7).

## Current Applications and Real-World Implementations
- Diagnostics: universal germline RET testing; somatic profiling to select targeted therapy; calcitonin/CEA for disease burden and kinetics; 18F‑DOPA PET and 68Ga‑DOTATATE PET for lesion detection (gild2023medullarythyroidcancer pages 1-2).
- Therapeutics: MKIs (vandetanib, cabozantinib) for unselected progressive disease; selective RET inhibitors (selpercatinib, pralsetinib) for RET‑mutant tumors with superior ORR/PFS and HRQoL; bone metastasis supportive therapy (bisphosphonates/denosumab) (lagana2023theevolvingtreatment pages 3-5, lagana2023theevolvingtreatment pages 1-3, barletta2021genomicsandepigenomics pages 6-7, gild2023medullarythyroidcancer pages 10-10).
- Emerging strategies: next‑generation RET inhibitors to overcome resistance; immunotherapeutics (e.g., engineered T cells against CEA/calcitonin/RET) and theranostics (PSMA modalities) under investigation (gild2023medullarythyroidcancer pages 10-10).

## Expert Opinions and Analysis
Leading reviews emphasize that molecular stratification around RET and RAS status is central to prognosis and therapeutic decision-making, with selective RET inhibitors establishing a new standard for RET‑mutant MTC. However, acquired resistance is increasingly observed, necessitating vigilant monitoring and enrollment in trials of next‑generation inhibitors and combinations, especially where on‑target RET resistance mutations (e.g., V804L/M or solvent‑front changes) or bypass signaling are suspected (gild2023medullarythyroidcancer pages 1-2, gild2023medullarythyroidcancer pages 10-10, lagana2023theevolvingtreatment pages 1-3, zhang2024moleculargeneticstherapeutics pages 5-6).

## Plan status update
Scope defined; recent literature and trial data collated (2020–2024, prioritized 2023–2024); evidence extracted for mechanisms, applications, and statistics; ontology mappings provided; summary artifact embedded.


References

1. (gild2023medullarythyroidcancer pages 1-2): Matti L Gild, Roderick J Clifton-Bligh, Lori J Wirth, and Bruce G Robinson. Medullary thyroid cancer: updates and challenges. Endocrine Reviews, 44:934-946, May 2023. URL: https://doi.org/10.1210/endrev/bnad013, doi:10.1210/endrev/bnad013. This article has 90 citations and is from a domain leading peer-reviewed journal.

2. (lagana2023theevolvingtreatment pages 1-3): Marta Laganà, Valentina Cremaschi, Andrea Alberti, Danica M. Vodopivec Kuri, Deborah Cosentini, and Alfredo Berruti. The evolving treatment landscape of medullary thyroid cancer. Current Treatment Options in Oncology, 24:1815-1832, Nov 2023. URL: https://doi.org/10.1007/s11864-023-01145-5, doi:10.1007/s11864-023-01145-5. This article has 11 citations and is from a peer-reviewed journal.

3. (gild2023medullarythyroidcancer pages 3-4): Matti L Gild, Roderick J Clifton-Bligh, Lori J Wirth, and Bruce G Robinson. Medullary thyroid cancer: updates and challenges. Endocrine Reviews, 44:934-946, May 2023. URL: https://doi.org/10.1210/endrev/bnad013, doi:10.1210/endrev/bnad013. This article has 90 citations and is from a domain leading peer-reviewed journal.

4. (barletta2021genomicsandepigenomics pages 10-12): Justine A. Barletta, Vânia Nosé, and Peter M. Sadow. Genomics and epigenomics of medullary thyroid carcinoma: from sporadic disease to familial manifestations. Endocrine Pathology, 32:35-43, Jan 2021. URL: https://doi.org/10.1007/s12022-021-09664-3, doi:10.1007/s12022-021-09664-3. This article has 64 citations and is from a peer-reviewed journal.

5. (sahakian2023molecularbasisand pages 13-15): Nicolas Sahakian, Frédéric Castinetti, and Pauline Romanet. Molecular basis and natural history of medullary thyroid cancer: it is (almost) all in the ret. Cancers, 15:4865, Oct 2023. URL: https://doi.org/10.3390/cancers15194865, doi:10.3390/cancers15194865. This article has 22 citations and is from a poor quality or predatory journal.

6. (lagana2023theevolvingtreatment pages 3-5): Marta Laganà, Valentina Cremaschi, Andrea Alberti, Danica M. Vodopivec Kuri, Deborah Cosentini, and Alfredo Berruti. The evolving treatment landscape of medullary thyroid cancer. Current Treatment Options in Oncology, 24:1815-1832, Nov 2023. URL: https://doi.org/10.1007/s11864-023-01145-5, doi:10.1007/s11864-023-01145-5. This article has 11 citations and is from a peer-reviewed journal.

7. (sahakian2023molecularbasisand pages 15-16): Nicolas Sahakian, Frédéric Castinetti, and Pauline Romanet. Molecular basis and natural history of medullary thyroid cancer: it is (almost) all in the ret. Cancers, 15:4865, Oct 2023. URL: https://doi.org/10.3390/cancers15194865, doi:10.3390/cancers15194865. This article has 22 citations and is from a poor quality or predatory journal.

8. (gild2023medullarythyroidcancer pages 10-10): Matti L Gild, Roderick J Clifton-Bligh, Lori J Wirth, and Bruce G Robinson. Medullary thyroid cancer: updates and challenges. Endocrine Reviews, 44:934-946, May 2023. URL: https://doi.org/10.1210/endrev/bnad013, doi:10.1210/endrev/bnad013. This article has 90 citations and is from a domain leading peer-reviewed journal.

9. (zhang2024moleculargeneticstherapeutics pages 5-6): Ying Zhang, Wei-Hui Zheng, Shi-Hong Zhou, Jia-Lei Gu, Qing Yu, Yi-Zhou Zhu, Yu-Jie Yan, Zhi Zhu, and Jin-Biao Shang. Molecular genetics, therapeutics and ret inhibitor resistance for medullary thyroid carcinoma and future perspectives. Cell Communication and Signaling : CCS, Sep 2024. URL: https://doi.org/10.1186/s12964-024-01837-x, doi:10.1186/s12964-024-01837-x. This article has 16 citations.

10. (sahakian2023molecularbasisand pages 1-2): Nicolas Sahakian, Frédéric Castinetti, and Pauline Romanet. Molecular basis and natural history of medullary thyroid cancer: it is (almost) all in the ret. Cancers, 15:4865, Oct 2023. URL: https://doi.org/10.3390/cancers15194865, doi:10.3390/cancers15194865. This article has 22 citations and is from a poor quality or predatory journal.

11. (barletta2021genomicsandepigenomics pages 3-4): Justine A. Barletta, Vânia Nosé, and Peter M. Sadow. Genomics and epigenomics of medullary thyroid carcinoma: from sporadic disease to familial manifestations. Endocrine Pathology, 32:35-43, Jan 2021. URL: https://doi.org/10.1007/s12022-021-09664-3, doi:10.1007/s12022-021-09664-3. This article has 64 citations and is from a peer-reviewed journal.

12. (barletta2021genomicsandepigenomics pages 6-7): Justine A. Barletta, Vânia Nosé, and Peter M. Sadow. Genomics and epigenomics of medullary thyroid carcinoma: from sporadic disease to familial manifestations. Endocrine Pathology, 32:35-43, Jan 2021. URL: https://doi.org/10.1007/s12022-021-09664-3, doi:10.1007/s12022-021-09664-3. This article has 64 citations and is from a peer-reviewed journal.