---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-28T05:07:10.991023'
end_time: '2026-03-28T05:21:02.269146'
duration_seconds: 831.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Wilms Tumor
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Wilms Tumor
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Wilms Tumor**.
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
- **Disease Name:** Wilms Tumor
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Wilms Tumor**.
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


# Wilms Tumor (Nephroblastoma) Pathophysiology — Molecular and Cellular Mechanisms (2023–2024 emphasis)

## Target Disease
- **Disease name:** Wilms tumor (nephroblastoma)
- **MONDO ID:** **MONDO:0006058** (Open Targets disease mapping) (rastegar2026understandinganaplasticwilms pages 77-80)
- **Category:** Embryonal pediatric renal malignancy (kidney cancer) arising from disrupted renal development programs with triphasic histology (blastemal, epithelial, stromal) (perotti2024hallmarkdiscoveriesin pages 6-10, tiburcio2024drosharegulatesmesenchymal pages 1-3, neagu2025wilms’tumora pages 6-8)

## Executive summary (current understanding)
Wilms tumor is best understood as a **developmental cancer** in which aberrant fetal kidney programs persist or are reactivated, often via early embryonic events that create nephrogenic rests and/or clonal nephrogenesis, followed by acquisition of additional genetic/epigenetic driver events that lock cells into progenitor-like states and enable malignant growth (perotti2024hallmarkdiscoveriesin pages 6-10, perotti2024hallmarkdiscoveriesin pages 25-29). The dominant mechanistic axes supported by recent synthesis and primary studies include: **11p15 imprinting/IGF2 dysregulation**, **WT1 loss**, **WNT/β-catenin activation (CTNNB1; AMER1/WTX)**, **microRNA-processing defects (DROSHA/DGCR8/DICER1)**, **SIX1/SIX2 nephron progenitor dysregulation**, and (in high-risk subsets) **TP53-driven anaplasia** with additional genomic instability, including **1q gain** and **LOH 1p/16q** that are used in risk stratification (perotti2024hallmarkdiscoveriesin pages 10-14, perotti2024hallmarkdiscoveriesin pages 14-17, perotti2024hallmarkdiscoveriesin pages 17-21, cantoni2026tumormicroenvironmentand pages 2-4).

| Mechanism/pathway | Key genes/proteins (HGNC symbols) | Cellular process (GO-style phrase) | Cell types/anatomy (CL/UBERON terms as text) | Evidence highlights with quantitative stats | Key recent sources (author, year, journal) with URL | Evidence citation IDs (pqac-...) |
|---|---|---|---|---|---|---|
| 11p15 imprinting / IGF2-H19 dysregulation | IGF2, H19, KCNQ1OT1, KCNQ1, WT1 | genomic imprinting; regulation of IGF signaling; epigenetic regulation of gene expression | embryonic renal progenitor / nephrogenic rest-like cells; blastemal tumor cells; kidney (UBERON:kidney), chromosome 11p15.5 locus | 11p15 alterations are among the most frequent WT events; IGF2 overexpression occurs in up to 70% of sporadic tumors and is near-universal in blastemal-type tumors. In bilateral WT, 58/99 (58.6%) tumors had H19/ICR1 loss of imprinting and 25/99 (25.2%) had 11p15.5 LOH; 29/30 (96.7%) synchronous tumors were concordant for 11p15.5 status. In 18/19 (94.7%) LOH tumors, breakpoints overlapped WT1/11p13, supporting coupled WT1/IGF2 dysregulation. | Perotti et al., 2024, *Nat Rev Urol* — https://doi.org/10.1038/s41585-023-00824-0; Murphy et al., 2023, *Nat Commun* — https://doi.org/10.1038/s41467-023-43730-0; Nirgude et al., 2024, *Br J Cancer* — https://doi.org/10.1038/s41416-023-02538-x | (perotti2024hallmarkdiscoveriesin pages 10-14, murphy2023geneticandepigenetic pages 4-5, murphy2023geneticandepigenetic pages 1-2, nirgude2024cancerpredispositionsignaling pages 1-2) |
| WT1 tumor suppressor / developmental regulator | WT1, IGF2, CTNNB1 | kidney development; nephron progenitor differentiation; tumor suppressor activity; transcription regulation | metanephric mesenchyme / embryonic renal progenitors; nephrogenic rests; kidney (UBERON:kidney) | WT1 mutations occur in ~6–20% of sporadic tumors and define a classic predisposition pathway. In bilateral WT, germline WT1 variants were found in 9/61 (14.8%) patients, and all 14 tumors from these patients showed 11p15.5 LOH; CTNNB1 mutations occurred in 10/14 (71.4%) of this WT1-associated set, supporting a stereotyped WT1 → 11p LOH/IGF2 activation → CTNNB1 sequence. | Perotti et al., 2024, *Nat Rev Urol* — https://doi.org/10.1038/s41585-023-00824-0; Murphy et al., 2023, *Nat Commun* — https://doi.org/10.1038/s41467-023-43730-0 | (perotti2024hallmarkdiscoveriesin pages 6-10, murphy2023geneticandepigenetic pages 1-2, murphy2023geneticandepigenetic pages 7-9) |
| WNT/β-catenin activation | CTNNB1, AMER1, WT1 | canonical Wnt signaling; β-catenin stabilization; regulation of progenitor proliferation and myogenic differentiation | blastemal tumor cells; epithelial/prototubular elements; embryonic kidney (UBERON:kidney) | CTNNB1 activating mutations occur in ~15% of WTs; ~65% affect exon 3, causing loss of phosphorylation sites and β-catenin stabilization. There is a strong WT1-CTNNB1 association: 19/20 CTNNB1-mutant tumors also carried WT1 mutations (p = 3.6 × 10^-13). AMER1 inactivation has been reported in up to 30% of tumors in initial studies (additional screens 7–18%). | Perotti et al., 2024, *Nat Rev Urol* — https://doi.org/10.1038/s41585-023-00824-0 | (perotti2024hallmarkdiscoveriesin pages 14-17, perotti2024hallmarkdiscoveriesin pages 10-14) |
| miRNA processing defects and ferroptosis vulnerability | DROSHA, DGCR8, DICER1, XPO5, GPX4, ACSL4, CCND2 | miRNA biogenesis; post-transcriptional gene silencing; maintenance of mesenchymal progenitor state; regulation of ferroptotic cell death | self-renewing mesenchymal/blastemal tumor cells; embryonic renal progenitors; kidney (UBERON:kidney) | miRNA-processing gene mutations are enriched in blastemal WT: DROSHA/DGCR8 in ~18.2% of blastemal cases; DROSHA ~10% in favorable-histology WT; DGCR8 ~4.5%. In bilateral WT, DROSHA mutations were seen in 7/85 (8.2%) tumors and DGCR8 in 4/85 (4.7%). DROSHA loss de-represses miRNA targets, increases CCND2, and is associated with ACSL4/redox abnormalities that sensitize cells to GPX4 inhibition and ferroptosis. | Tiburcio et al., 2024, *Mol Cancer Res* — https://doi.org/10.1158/1541-7786.mcr-23-0930; Perotti et al., 2024, *Nat Rev Urol* — https://doi.org/10.1038/s41585-023-00824-0; Murphy et al., 2023, *Nat Commun* — https://doi.org/10.1038/s41467-023-43730-0 | (tiburcio2024drosharegulatesmesenchymal pages 1-3, perotti2024hallmarkdiscoveriesin pages 17-21, murphy2023geneticandepigenetic pages 4-5) |
| SIX1/SIX2 progenitor-state program | SIX1, SIX2 | maintenance of nephron progenitor cell population; regulation of cell cycle; kidney development; adhesion gene regulation | blastemal tumor cells; nephron progenitor/cap mesenchyme-like cells; kidney (UBERON:kidney) | Recurrent SIX1/SIX2 Q177R homeodomain mutations occur in 18.1% of blastemal cases and 4.3% overall. These are linked to a progenitor-like state, chemotherapy-resistant blastemal tumors, and altered cell-cycle, kidney-development, and adhesion programs. | Perotti et al., 2024, *Nat Rev Urol* — https://doi.org/10.1038/s41585-023-00824-0 | (perotti2024hallmarkdiscoveriesin pages 17-21, perotti2024hallmarkdiscoveriesin pages 14-17) |
| MYCN dysregulation | MYCN | positive regulation of cell proliferation; transcriptional amplification; oncogenic progenitor expansion | blastemal/anaplastic tumor cells; embryonic kidney-derived tumor compartments | MYCN gain/amplification and recurrent P44L mutation are described in WT; MYCN gain is associated with anaplastic histology and poor outcome. Reviews classify MYCN activation as one of the major transcriptional/mutational subclasses in WT. | Perotti et al., 2024, *Nat Rev Urol* — https://doi.org/10.1038/s41585-023-00824-0; Tiburcio et al., 2024, *Mol Cancer Res* — https://doi.org/10.1158/1541-7786.mcr-23-0930 | (perotti2024hallmarkdiscoveriesin pages 14-17, tiburcio2024drosharegulatesmesenchymal pages 1-3) |
| TP53 dysfunction and anaplasia | TP53 | DNA damage response; apoptotic signaling; anaplastic transformation | diffuse anaplastic tumor cells; high-risk Wilms tumor compartments; kidney tumor tissue | Diffuse anaplasia occurs in ~5–10% of WTs. TP53 is mutated in ~50–60% of diffuse anaplastic WTs, and TP53 immunopositivity is usually associated with anaplasia and poor prognosis. | Perotti et al., 2024, *Nat Rev Urol* — https://doi.org/10.1038/s41585-023-00824-0 | (perotti2024hallmarkdiscoveriesin pages 10-14) |
| Copy-number risk biomarkers | 1q gain; LOH 1p; LOH 16q; chromosome 12 gain | chromosomal instability; copy-number alteration-associated progression; relapse risk stratification | Wilms tumor tissue broadly; high-risk blastemal and anaplastic compartments | Combined LOH at 1p/16q is an established adverse biomarker in COG protocols. 1q gain occurs in ~20–30% of cases and is a strong predictor of poor outcome. In one 2024 genomic/modeling study, 1q gain was seen in 2 patients, combined LOH 1p/16q in 2 patients, and chromosome 12 gain (linked to relapse) in 2 patients. | Mittal et al., 2024, *Commun Biol* — https://doi.org/10.1038/s42003-024-06140-6; Cantoni et al., 2026, *Cancers* — https://doi.org/10.3390/cancers18060908; Lim & Loh, 2024, *Cancers* — https://doi.org/10.3390/cancers16173051 | (mittal2024targetingtrip13in pages 2-3, cantoni2026tumormicroenvironmentand pages 2-4, lim2024interethnicvariationsin pages 15-17) |
| XPO1 nuclear export dependency / selinexor vulnerability | XPO1, TRIP13 | nuclear export; regulation of cell survival; drug response | Wilms tumor cell lines and recurrent/refractory Wilms tumor; kidney tumor tissue | XPO1 was identified as a vulnerability in WT models; selinexor suppressed TRIP13 and synergized with doxorubicin in vivo/in vitro. A dedicated Phase II trial (NCT05985161) is recruiting for relapsed/refractory or high-risk Wilms tumor and other XPO1-dependent solid tumors; estimated enrollment ~45, with a Wilms-specific cohort and primary endpoint of overall response rate at 6 months. | Mittal et al., 2024, *Commun Biol* — https://doi.org/10.1038/s42003-024-06140-6; ClinicalTrials.gov NCT05985161 (2023) — https://clinicaltrials.gov/study/NCT05985161 | (mittal2024targetingtrip13in pages 2-3, NCT05985161 chunk 1, cantoni2026tumormicroenvironmentand pages 19-20) |


*Table: This table summarizes major molecular mechanisms, genes, cellular processes, anatomic context, and recent evidence for Wilms tumor pathophysiology. It is useful as a compact knowledge-base style overview linking mechanistic biology to quantitative biomarkers and emerging therapeutic vulnerabilities.*

## 1) Key concepts and definitions

### 1.1 Developmental origin and histology
Wilms tumor typically resembles fetal kidney and often contains a **triphasic** mixture of (i) **blastema** (undifferentiated metanephric mesenchyme), (ii) **epithelial cells** (prototubular/primitive tubules), and (iii) **stromal** elements (mesenchymal tissues). The blastemal compartment is often considered the aggressive and less-differentiated compartment and can be predominant in monophasic cases (neagu2025wilms’tumora pages 6-8, perotti2024hallmarkdiscoveriesin pages 6-10, tiburcio2024drosharegulatesmesenchymal pages 1-3).

### 1.2 Nephrogenic rests and clonal nephrogenesis
Wilms tumors frequently arise **within or adjacent to nephrogenic rests** (embryonic renal precursor remnants) (perotti2024hallmarkdiscoveriesin pages 6-10, tiburcio2024drosharegulatesmesenchymal pages 1-3). Perotti et al. (Nature Reviews Urology; online 2023, issue Oct 2024) further highlight that **intralobar nephrogenic rests (ILNR)** and **perilobar nephrogenic rests (PLNR)** associate with distinct molecular subsets; PLNR is enriched in tumor subsets with dysregulated nephrogenic-zone self-renewal/differentiation programs (perotti2024hallmarkdiscoveriesin pages 25-29).

### 1.3 Genomic imprinting in Wilms tumor
Perotti et al. explicitly define genomic imprinting as **parent-specific monoallelic expression** and describe Wilms tumor–predisposing lesions at **11p15** affecting imprint control regions for IGF2/H19 (perotti2024hallmarkdiscoveriesin pages 6-10, perotti2024hallmarkdiscoveriesin pages 10-14).

## 2) Core pathophysiology: dysregulated pathways and cellular processes

### 2.1 11p15 imprinting defects → IGF2-driven growth signaling
A major early and recurrent driver is abnormal imprinting/allelic imbalance at **11p15** (WT2 region), affecting **IGF2** (growth factor) and **H19**. Perotti et al. report **IGF2 overexpression in up to ~70% of sporadic tumors** and its presence in nephrogenic rests, supporting an early lesion that precedes frank malignancy in many cases (perotti2024hallmarkdiscoveriesin pages 10-14).

**Recent 2023–2024 developments (bilateral predisposition and mosaicism):** Murphy et al. (Nature Communications, Dec 2023; https://doi.org/10.1038/s41467-023-43730-0) provide strong evidence that bilateral disease frequently reflects **shared early 11p15.5 epigenetic/copy-number events** rather than a shared tumor clone. Across **99 bilateral tumor specimens**, they report **11p15.5 LOI (H19/ICR1 hypermethylation) in 58/99 (58.6%)**, **11p15.5 LOH in 25/99 (25.2%)**, and normal imprinting retention in 16/99 (16.1%) (murphy2023geneticandepigenetic pages 1-2). Synchronous paired tumors were **concordant for 11p15.5 status in 29/30 (96.7%)** yet usually lacked shared somatic variants, supporting **independent tumor origins** seeded by early predisposition events (murphy2023geneticandepigenetic pages 4-5).

In Beckwith–Wiedemann syndrome (BWS), Nirgude et al. (British Journal of Cancer, Dec 2024; https://doi.org/10.1038/s41416-023-02538-x) describe mosaic **11p15 LOH** due to paternal uniparental isodisomy and note that **LOH at 11p15 is present in at least 30% of Wilms tumors and is associated with higher staging** (nirgude2024cancerpredispositionsignaling pages 1-2).

**Cellular processes impacted:** growth factor signaling, epigenetic regulation, cell proliferation and survival, and maintenance of embryonic progenitor programs (perotti2024hallmarkdiscoveriesin pages 10-14, nirgude2024cancerpredispositionsignaling pages 1-2).

### 2.2 WT1 tumor suppressor loss and aberrant nephrogenesis
WT1 is a master developmental regulator in kidney organogenesis. Perotti et al. summarize WT1’s role in mesenchymal–epithelial transitions and note that Wilms tumors often arise adjacent to nephrogenic rests, consistent with early developmental disruption (perotti2024hallmarkdiscoveriesin pages 6-10). Murphy et al. report that **WT1 germline variants** were among the most common detectable predispositions in their bilateral cohort (**9/61, 14.8%**) (murphy2023geneticandepigenetic pages 1-2).

A key mechanistic pattern in WT1-predisposed disease is a stereotyped evolutionary sequence in which early **11p events** both (i) drive **biallelic WT1 inactivation** and (ii) activate the **IGF2** imprinting domain, followed by **WNT pathway activation**. Murphy et al. report that in WT1-predisposed tumors, **11p15.5 LOH was present in all tumors (14/14)** and **CTNNB1 exon 3 activating mutations occurred in 10/14 (71.4%)** of the WT1-associated set (murphy2023geneticandepigenetic pages 1-2).

### 2.3 WNT/β-catenin signaling (CTNNB1) and β-catenin destruction complex (AMER1/WTX)
Perotti et al. report **CTNNB1 activating mutations in ~15%** of Wilms tumors, with many affecting **exon 3** to stabilize β-catenin and activate canonical WNT signaling. They also report a very strong association between **WT1 and CTNNB1 mutations**: **19/20 CTNNB1-mutant tumors also had WT1 mutations** (p = 3.6 × 10−13) (perotti2024hallmarkdiscoveriesin pages 14-17). AMER1 (WTX) is described as part of the β-catenin destruction complex, with inactivation reported in up to ~30% in early screens (perotti2024hallmarkdiscoveriesin pages 14-17).

**Clinical/biologic implication:** this axis connects renal development programs to sustained progenitor proliferation and lineage mis-specification (perotti2024hallmarkdiscoveriesin pages 14-17).

### 2.4 MicroRNA-processing defects (DROSHA/DGCR8/DICER1) maintain progenitor/mesenchymal state and create metabolic vulnerabilities
A key modern concept is that a substantial subset of Wilms tumors are driven by disruption of **miRNA biogenesis**, which derepresses miRNA target programs controlling differentiation and proliferation.

- Perotti et al. report recurrent miRNA-processing pathway mutations in **DROSHA**, **DGCR8**, and **DICER1**, enriched in blastemal tumors; they cite DROSHA/DGCR8 in ~18.2% of blastemal cases and note DROSHA ~10% in favorable-histology tumors and DGCR8 ~4.5% (perotti2024hallmarkdiscoveriesin pages 17-21).
- Murphy et al. quantify these alterations in bilateral tumors (WES/WGS panel): **DROSHA 7/85 (8.2%)** and **DGCR8 4/85 (4.7%)**, and report pathway enrichment for **RNA/miRNA biogenesis**, **p53**, and transcription pathways (murphy2023geneticandepigenetic pages 4-5).

**Mechanistic primary evidence (2024):** Tiburcio et al. (Molecular Cancer Research, Apr 2024; https://doi.org/10.1158/1541-7786.mcr-23-0930) show that DROSHA mutations correlate with derepression of miRNA target genes and a self-renewing mesenchymal state. They also connect miRNA loss to redox/lipid biology: miRNA-deficient Wilms tumor cells show aberrant redox metabolism and are **sensitized to ferroptotic cell death through inhibition of GPX4**, which detoxifies lipid peroxides (tiburcio2024drosharegulatesmesenchymal pages 1-3).

### 2.5 SIX1/SIX2 (nephron progenitor program) and blastemal chemo-resistance
Perotti et al. report recurrent **SIX1/SIX2 Q177R** mutations in the homeodomain, frequent in blastemal tumors (**18.1% of blastemal cases; 4.3% overall**) and associated with a progenitor-like state and chemotherapy-resistant blastemal tumors (perotti2024hallmarkdiscoveriesin pages 17-21).

### 2.6 MYCN activation and high-risk biology
Perotti et al. describe MYCN gain/amplification and recurrent MYCN mutations (e.g., P44L), and specifically note that **MYCN gain is associated with anaplastic histology and poor outcome** (perotti2024hallmarkdiscoveriesin pages 14-17).

### 2.7 TP53-driven anaplasia (high-risk subtype)
Perotti et al. report that **diffuse anaplasia occurs in ~5–10%** of Wilms tumors and that **TP53 is mutated in ~50–60%** of diffuse anaplastic Wilms tumors; they further note that TP53 immunopositivity is used as a surrogate for mutation and correlates with poor prognosis (perotti2024hallmarkdiscoveriesin pages 10-14).

## 3) Key molecular players (genes/proteins, chemical entities, cell types, anatomy)

### 3.1 Genes/proteins (HGNC symbols; selected)
- **Tumor suppressors / developmental regulators:** WT1; TP53 (anaplasia); REST; TRIM28; CTR9 (PAF1 complex) (perotti2024hallmarkdiscoveriesin pages 21-25, perotti2024hallmarkdiscoveriesin pages 10-14, rastegar2026understandinganaplasticwilmsa pages 38-42)
- **Imprinting/growth signaling:** IGF2; H19; KCNQ1OT1; KCNQ1 (perotti2024hallmarkdiscoveriesin pages 10-14, nirgude2024cancerpredispositionsignaling pages 1-2, murphy2023geneticandepigenetic pages 6-7)
- **WNT/β-catenin:** CTNNB1; AMER1/WTX (perotti2024hallmarkdiscoveriesin pages 14-17)
- **miRNA biogenesis:** DROSHA; DGCR8; DICER1; XPO5 (perotti2024hallmarkdiscoveriesin pages 17-21, murphy2023geneticandepigenetic pages 4-5)
- **Nephron progenitor/renal development transcription factors:** SIX1; SIX2; OSR1; HOXA11 (perotti2024hallmarkdiscoveriesin pages 25-29, perotti2024hallmarkdiscoveriesin pages 17-21)
- **Oncogenic transcriptional amplifiers:** MYCN (perotti2024hallmarkdiscoveriesin pages 14-17)
- **Nuclear export dependency:** XPO1; downstream TRIP13 (mittal2024targetingtrip13in pages 2-3)

### 3.2 Chemical entities / small molecules (CHEBI-style; named entities)
Evidence in the retrieved corpus names drug-like agents (not formal CHEBI IDs):
- **Selinexor (KPT-330)**, an **XPO1 inhibitor**, tested in Wilms tumor (NCT05985161) (NCT05985161 chunk 1, cantoni2026tumormicroenvironmentand pages 19-20)
- **Tegavivint**, described as a **WNT/β-catenin inhibitor** in pediatric trials (NCT04851119) (cantoni2026tumormicroenvironmentand pages 19-20)
- **Doxorubicin**, used clinically and shown to synergize with nuclear export inhibition in a Wilms model system (mittal2024targetingtrip13in pages 2-3)
- **GPX4 inhibitors** (e.g., discussed mechanistically as GPX4 inhibition) to induce ferroptosis in miRNA-deficient subset (tiburcio2024drosharegulatesmesenchymal pages 1-3)

### 3.3 Cell types (CL terms as text) and microenvironment
- **Nephron progenitor/cap mesenchyme-like cells**; embryonic renal progenitors (developmental origin) (perotti2024hallmarkdiscoveriesin pages 25-29, tiburcio2024drosharegulatesmesenchymal pages 1-3)
- **Tumor compartments:** blastemal cells, epithelial prototubules/tubular cells, stromal/fibroblast-like cells (perotti2024hallmarkdiscoveriesin pages 6-10, perotti2024hallmarkdiscoveriesin pages 25-29)
- **Immune cells:** tumor-associated macrophages (TAMs; CD68+), skewed toward **M2-like macrophages** (Arg-1, CD163, CD206); neutrophils; mast cells; Tregs; low CD8+ T cells (cantoni2026tumormicroenvironmentand pages 6-7, rastegar2026understandinganaplasticwilmsa pages 38-42)

### 3.4 Anatomical locations (UBERON terms as text)
- **Kidney** (pediatric renal tumor)
- **Nephrogenic rests** (intralobar/perilobar) in kidney (perotti2024hallmarkdiscoveriesin pages 25-29, perotti2024hallmarkdiscoveriesin pages 6-10)
- **Chromosome 11p15.5 imprinting domain**; **11p13 WT1 locus** (perotti2024hallmarkdiscoveriesin pages 10-14, murphy2023geneticandepigenetic pages 4-5)

## 4) Biological processes (GO annotation candidates)
The following disrupted processes are directly supported by the evidence base above:
- **Genomic imprinting / epigenetic regulation of gene expression** (11p15.5; H19/ICR1 methylation) (perotti2024hallmarkdiscoveriesin pages 10-14, murphy2023geneticandepigenetic pages 1-2)
- **Regulation of growth factor signaling** (IGF2 axis) (perotti2024hallmarkdiscoveriesin pages 10-14)
- **Kidney development / nephron progenitor differentiation; mesenchymal–epithelial transition** (WT1, SIX programs; fetal kidney mapping) (perotti2024hallmarkdiscoveriesin pages 6-10, perotti2024hallmarkdiscoveriesin pages 25-29)
- **Canonical WNT signaling** (β-catenin stabilization from CTNNB1 exon 3 mutations; AMER1/WTX disruption) (perotti2024hallmarkdiscoveriesin pages 14-17)
- **miRNA-mediated gene silencing / miRNA biogenesis** (DROSHA/DGCR8/DICER1) (perotti2024hallmarkdiscoveriesin pages 17-21, murphy2023geneticandepigenetic pages 4-5)
- **Ferroptotic cell death / lipid peroxide detoxification** (GPX4 dependence in miRNA-deficient state) (tiburcio2024drosharegulatesmesenchymal pages 1-3)
- **DNA damage response / apoptotic signaling** (TP53 dysfunction in diffuse anaplasia) (perotti2024hallmarkdiscoveriesin pages 10-14)
- **Immune evasion / macrophage polarization** (M2-skewed TAMs; immune-cold features) (cantoni2026tumormicroenvironmentand pages 6-7, rastegar2026understandinganaplasticwilmsa pages 38-42)

## 5) Cellular components (cellular anatomy; GO-CC candidates)
- **Nucleus** (WT1 transcription/RNA metabolism roles; REST/TRIM28/CTR9 transcriptional regulation) (perotti2024hallmarkdiscoveriesin pages 6-10, perotti2024hallmarkdiscoveriesin pages 21-25)
- **miRNA microprocessor machinery** (functionally represented by DROSHA/DGCR8; plus DICER1 in cytoplasmic processing pathway) (perotti2024hallmarkdiscoveriesin pages 17-21, murphy2023geneticandepigenetic pages 4-5)
- **Plasma membrane and lipid peroxidation sites** relevant to ferroptosis (ACSL4-mediated PUFA incorporation; GPX4 detoxification of lipid peroxides) (tiburcio2024drosharegulatesmesenchymal pages 1-3)

## 6) Disease progression model (sequence of events)
A mechanistically supported progression model (not necessarily universal across all patients) is:
1. **Early developmental lesion** in fetal kidney lineages leading to nephrogenic rests and/or clonal nephrogenesis (perotti2024hallmarkdiscoveriesin pages 6-10, perotti2024hallmarkdiscoveriesin pages 25-29).
2. **Initiating epigenetic/copy-number event at 11p15.5** (LOI or LOH) resulting in increased IGF2 expression and altered imprinting balance; this is especially prominent in bilateral predisposition and BWS-associated cases (murphy2023geneticandepigenetic pages 1-2, nirgude2024cancerpredispositionsignaling pages 1-2).
3. **Acquisition of additional driver mutations** that enforce progenitor-like programs and proliferation:
   - WT1 inactivation and/or WNT activation (CTNNB1; AMER1/WTX) (perotti2024hallmarkdiscoveriesin pages 14-17, murphy2023geneticandepigenetic pages 1-2).
   - miRNA-processing loss (DROSHA/DGCR8/DICER1) causing widespread derepression of differentiation/proliferation programs and metabolic rewiring (tiburcio2024drosharegulatesmesenchymal pages 1-3, perotti2024hallmarkdiscoveriesin pages 17-21).
   - SIX1/SIX2 mutations sustaining nephron progenitor states and chemotherapy resistance in blastemal tumors (perotti2024hallmarkdiscoveriesin pages 17-21).
4. **Progression to high-risk phenotypes** via genomic instability and additional lesions:
   - **TP53** disruption associated with diffuse anaplasia (5–10% of tumors; TP53 mutated ~50–60% in diffuse anaplasia) (perotti2024hallmarkdiscoveriesin pages 10-14).
   - Copy-number alterations including **1q gain** and **LOH 1p/16q**, used for risk assessment and associated with relapse/poor outcome (cantoni2026tumormicroenvironmentand pages 2-4, mittal2024targetingtrip13in pages 2-3).

## 7) Phenotypic manifestations (HP term candidates; clinical-pathologic links)
The following phenotype elements are supported conceptually and/or explicitly described in the retrieved evidence:
- **Renal neoplasm / embryonal tumor of kidney** (disease entity)
- **Triphasic histology**: blastemal, epithelial, stromal components; blastemal predominance as aggressive phenotype (neagu2025wilms’tumora pages 6-8, perotti2024hallmarkdiscoveriesin pages 6-10)
- **Nephrogenic rests (preneoplastic lesions)**, including ILNR/PLNR; association of PLNR with specific molecular subsets (perotti2024hallmarkdiscoveriesin pages 25-29, tiburcio2024drosharegulatesmesenchymal pages 1-3)
- **Diffuse anaplasia**: nuclear enlargement/hyperchromasia and atypical multipolar mitoses; poor prognosis and TP53 association (perotti2024hallmarkdiscoveriesin pages 10-14, rastegar2026understandinganaplasticwilmsa pages 38-42)

## 8) Recent developments and latest research (prioritizing 2023–2024)

### 8.1 2023: Quantitative predisposition architecture in bilateral Wilms tumor (COG AREN18B5-Q)
Murphy et al. (Nature Communications, Dec 2023; https://doi.org/10.1038/s41467-023-43730-0) provide a modern framework in which bilateral disease is commonly driven by **either** detectable germline predisposition variants **or** post-zygotic mosaic imprinting defects at 11p15.5. Key statistics include LOI/LOH/ROI proportions across 99 tumors and high concordance of 11p15.5 status across synchronous tumors (murphy2023geneticandepigenetic pages 1-2, murphy2023geneticandepigenetic pages 4-5).

### 8.2 2024: miRNA-processing subclass mechanistically linked to ferroptosis sensitivity
Tiburcio et al. (Molecular Cancer Research, Apr 2024; https://doi.org/10.1158/1541-7786.mcr-23-0930) move beyond association to mechanism by showing DROSHA-driven transcriptional programs and demonstrating a **therapeutic vulnerability**: miRNA-deficient Wilms cells are sensitized to ferroptosis through **GPX4 inhibition** (tiburcio2024drosharegulatesmesenchymal pages 1-3).

### 8.3 2024: Consolidation of “hallmark” pathways and quantification of key high-risk features
Perotti et al. (Nature Reviews Urology; Oct 2024 issue; https://doi.org/10.1038/s41585-023-00824-0) synthesize the field with key quantitative statements that directly support knowledge-base assertions, including (i) IGF2 overexpression up to ~70% of sporadic tumors, (ii) CTNNB1 frequency (~15%) and tight association with WT1, (iii) SIX1/2 Q177R enrichment in blastemal tumors, and (iv) TP53 mutation frequency (~50–60%) in diffuse anaplasia (perotti2024hallmarkdiscoveriesin pages 10-14, perotti2024hallmarkdiscoveriesin pages 14-17, perotti2024hallmarkdiscoveriesin pages 17-21).

### 8.4 2024: Translational vulnerability—nuclear export (XPO1) and patient-derived models
Mittal et al. (Communications Biology, Apr 2024; https://doi.org/10.1038/s42003-024-06140-6) report clinically relevant genomic biomarkers in a small cohort (e.g., 1q gain, LOH 1p/16q) and identify XPO1 as a vulnerability, with nuclear export inhibitors synergizing with doxorubicin in vivo (mittal2024targetingtrip13in pages 2-3).

## 9) Current applications and real-world implementations

### 9.1 Molecular risk stratification and clinical decision-making
Evidence in the retrieved set supports several widely used stratification features:
- **Diffuse anaplasia and TP53:** Diffuse anaplasia is a high-risk subtype (~5–10%); TP53 is mutated in ~50–60% of diffuse anaplastic tumors, and TP53 IHC is used as a surrogate associated with poor prognosis (perotti2024hallmarkdiscoveriesin pages 10-14).
- **11p15 status:** LOH/LOI at 11p15 is common; in BWS-associated analysis, **11p15 LOH** is present in at least 30% of Wilms tumors and associated with higher staging (nirgude2024cancerpredispositionsignaling pages 1-2).
- **Copy-number biomarkers:** combined **LOH 1p/16q** and **1q gain** (20–30% overall) are adverse features; 1q gain is explicitly described as a poor prognostic factor in a 2024 cohort study (cantoni2026tumormicroenvironmentand pages 2-4, mittal2024targetingtrip13in pages 2-3).

### 9.2 Precision diagnostics and surveillance in predisposition
Murphy et al. show that post-zygotic mosaic 11p15.5 LOI can be detectable in non-tumor tissues (adjacent kidney; sometimes peripheral blood), emphasizing the need for **multi-tissue testing strategies** when evaluating predisposition in bilateral disease (murphy2023geneticandepigenetic pages 7-9, murphy2023geneticandepigenetic pages 5-6).

### 9.3 Targeted/experimental therapies and trials
- **XPO1 inhibitor selinexor (ClinicalTrials.gov):** NCT05985161 (registered 2023; https://clinicaltrials.gov/study/NCT05985161) is a **Phase II** study in relapsed/refractory Wilms tumor and other pediatric solid tumors. It includes a Wilms tumor cohort, uses weekly oral selinexor, and has a primary endpoint of overall response rate evaluated at 6 months (NCT05985161 chunk 1).
- **WNT/β-catenin inhibitor tegavivint:** A WNT/β-catenin inhibitor (Tegavivint; NCT04851119) is noted as investigational in pediatric trials (cantoni2026tumormicroenvironmentand pages 19-20).
- **IGF axis targeting:** Despite IGF2 prevalence, Perotti et al. state that preclinical models and a **phase 2 study of IGF-1R blockade were not effective**, suggesting pathway redundancy/bypass and the need for combination strategies (perotti2024hallmarkdiscoveriesin pages 10-14).
- **Immunotherapy direction:** Multi-tumor-associated antigen T cells targeting **WT1/PRAME/survivin** have been tested and reported safe with prolonged time-to-progression in early clinical experience; immune checkpoint inhibitors have had limited efficacy in unselected populations, consistent with an immune-cold phenotype (cantoni2026tumormicroenvironmentand pages 19-20, rastegar2026understandinganaplasticwilmsa pages 38-42).

## 10) Relevant statistics and data points (recent sources)
- **Bilateral predisposition tumor 11p15.5 states (Murphy 2023):** LOI 58/99 (58.6%); LOH 25/99 (25.2%); ROI 16/99 (16.1%); concordance across paired synchronous tumors 29/30 (96.7%) (murphy2023geneticandepigenetic pages 1-2, murphy2023geneticandepigenetic pages 4-5).
- **WT1 predisposition frequency in bilateral cohort:** WT1 germline variants 9/61 (14.8%) (murphy2023geneticandepigenetic pages 1-2).
- **WT1-associated progression data:** 11p15.5 LOH in all WT1-predisposed tumors analyzed (14/14); CTNNB1 exon 3 mutations 10/14 (71.4%) in WT1-associated set (murphy2023geneticandepigenetic pages 1-2).
- **Diffuse anaplasia and TP53:** diffuse anaplasia 5–10%; TP53 mutated ~50–60% in diffuse anaplastic tumors (perotti2024hallmarkdiscoveriesin pages 10-14).
- **Risk CNAs:** 1q gain present in ~20–30% (review-level estimate) and is a robust predictor of poor outcome; LOH 1p/16q adverse (cantoni2026tumormicroenvironmentand pages 2-4).

## 11) Expert opinions / authoritative synthesis (with direct quotes)
From Perotti et al. (Nature Reviews Urology; Oct 2024 issue):
- On origin: **“Modern molecular findings support the embryonic renal origins of Wilms tumours.”** (perotti2024hallmarkdiscoveriesin pages 21-25)
- On tumor composition: Wilms tumors include **“undifferentiated metanephric mesenchyme (blastema) and also more differentiated cells (stroma and tubular epithelial cells normally derived from metanephric mesenchyme)”** (perotti2024hallmarkdiscoveriesin pages 21-25).

These statements support the mainstream interpretation that Wilms tumor pathophysiology is primarily a failure of normal renal differentiation programs, with recurrent lesions targeting developmental transcriptional/epigenetic and post-transcriptional (miRNA) regulators (perotti2024hallmarkdiscoveriesin pages 21-25, perotti2024hallmarkdiscoveriesin pages 17-21).

## 12) Knowledge-base style annotations (ontology-ready; evidence-linked)

### 12.1 Pathophysiology description (narrative)
Wilms tumor arises when embryonic renal precursor cells (often within nephrogenic rests) experience early epigenetic/copy-number alterations—especially at 11p15.5—leading to dysregulated imprinting (IGF2 overexpression; H19 perturbation) and a growth-promoting, developmentally arrested state. Subsequent driver events (WT1 loss; CTNNB1/AMER1-mediated WNT activation; miRNA-processing defects; SIX1/SIX2 progenitor-program activation) reinforce progenitor self-renewal, impair differentiation, and remodel cellular metabolism. In a subset, additional genomic instability and TP53 defects drive diffuse anaplasia and therapy resistance. The tumor microenvironment is characterized by an inflammatory stromal compartment with M2-like macrophage dominance and generally low cytotoxic T-cell infiltration, contributing to immune evasion (perotti2024hallmarkdiscoveriesin pages 25-29, perotti2024hallmarkdiscoveriesin pages 10-14, perotti2024hallmarkdiscoveriesin pages 14-17, tiburcio2024drosharegulatesmesenchymal pages 1-3, cantoni2026tumormicroenvironmentand pages 6-7, rastegar2026understandinganaplasticwilmsa pages 38-42).

### 12.2 Gene/protein annotations (examples)
- **WT1 (HGNC:12796)** — kidney development; tumor suppressor; transcription/RNA regulation; associated with WT1→11p LOH→CTNNB1 evolutionary path in predisposed bilateral WT (murphy2023geneticandepigenetic pages 1-2, perotti2024hallmarkdiscoveriesin pages 6-10).
- **CTNNB1 (HGNC:2514)** — canonical WNT signaling activation (exon 3 stabilization); strongly co-mutates with WT1 (perotti2024hallmarkdiscoveriesin pages 14-17).
- **IGF2 (HGNC:5466) / H19 (HGNC:4713)** — imprinting dysregulation at 11p15 with IGF2 overexpression up to ~70% of sporadic tumors (perotti2024hallmarkdiscoveriesin pages 10-14).
- **DROSHA (HGNC:17179) / DGCR8 (HGNC:17233) / DICER1 (HGNC:17098)** — miRNA biogenesis defects; linked to mesenchymal progenitor state and GPX4-dependent ferroptosis vulnerability (perotti2024hallmarkdiscoveriesin pages 17-21, tiburcio2024drosharegulatesmesenchymal pages 1-3).
- **SIX1/SIX2 (HGNC:10888/10889)** — nephron progenitor program; Q177R enrichment in blastemal and chemo-resistant tumors (perotti2024hallmarkdiscoveriesin pages 17-21).
- **TP53 (HGNC:11998)** — diffuse anaplasia driver; mutation ~50–60% of diffuse anaplastic tumors (perotti2024hallmarkdiscoveriesin pages 10-14).

### 12.3 Cell type involvement (examples)
- Nephron progenitor / cap mesenchyme-like tumor cells (developmental origin) (perotti2024hallmarkdiscoveriesin pages 25-29, tiburcio2024drosharegulatesmesenchymal pages 1-3)
- Tumor-associated macrophages (M2-like) in stromal compartment; neutrophils; mast cells; Tregs; low CD8+ T cells (cantoni2026tumormicroenvironmentand pages 6-7, rastegar2026understandinganaplasticwilmsa pages 38-42)

### 12.4 Anatomical locations (examples)
- Kidney; nephrogenic rests (ILNR/PLNR) (perotti2024hallmarkdiscoveriesin pages 25-29, perotti2024hallmarkdiscoveriesin pages 6-10)
- Chromosome 11p15.5 imprinting locus; 11p13 WT1 locus (murphy2023geneticandepigenetic pages 4-5, perotti2024hallmarkdiscoveriesin pages 10-14)

### 12.5 Evidence items (IDs; publication info)
- Perotti et al. **“Hallmark discoveries in the biology of Wilms tumour.”** *Nature Reviews Urology* (Oct 2024 issue). DOI: https://doi.org/10.1038/s41585-023-00824-0 (perotti2024hallmarkdiscoveriesin pages 10-14, perotti2024hallmarkdiscoveriesin pages 14-17, perotti2024hallmarkdiscoveriesin pages 17-21, perotti2024hallmarkdiscoveriesin pages 25-29)
- Murphy et al. **“Genetic and epigenetic features of bilateral Wilms tumor predisposition…”** *Nature Communications* (Dec 2023). DOI: https://doi.org/10.1038/s41467-023-43730-0 (murphy2023geneticandepigenetic pages 1-2, murphy2023geneticandepigenetic pages 4-5)
- Tiburcio et al. **“DROSHA regulates mesenchymal gene expression in Wilms tumor.”** *Molecular Cancer Research* (Apr 2024). DOI: https://doi.org/10.1158/1541-7786.mcr-23-0930 (tiburcio2024drosharegulatesmesenchymal pages 1-3)
- Nirgude et al. **“Cancer predisposition signaling in Beckwith-Wiedemann Syndrome drives Wilms tumor development.”** *British Journal of Cancer* (Dec 2024). DOI: https://doi.org/10.1038/s41416-023-02538-x (nirgude2024cancerpredispositionsignaling pages 1-2)
- Mittal et al. **“Targeting TRIP13… nuclear export inhibitors…”** *Communications Biology* (Apr 2024). DOI: https://doi.org/10.1038/s42003-024-06140-6 (mittal2024targetingtrip13in pages 2-3)
- ClinicalTrials.gov **NCT05985161** (registered 2023): https://clinicaltrials.gov/study/NCT05985161 (NCT05985161 chunk 1)

## Notes on PMID availability
The retrieved evidence snippets did not include PubMed IDs explicitly for the 2023–2024 core sources; therefore, this report cites DOIs and ClinicalTrials.gov identifiers as stable primary references.


References

1. (rastegar2026understandinganaplasticwilms pages 77-80): B Rastegar. Understanding anaplastic wilms tumors: spatial insights into their evolution and clinical significance. Unknown journal, 2026.

2. (perotti2024hallmarkdiscoveriesin pages 6-10): Daniela Perotti, Richard D. Williams, Jenny Wegert, Jack Brzezinski, Mariana Maschietto, Sara Ciceri, David Gisselsson, Samantha Gadd, Amy L. Walz, Rhoikos Furtwaengler, Jarno Drost, Reem Al-Saadi, Nicholas Evageliou, Saskia L. Gooskens, Andrew L. Hong, Andrew J. Murphy, Michael V. Ortiz, Maureen J. O’Sullivan, Elizabeth A. Mullen, Marry M. van den Heuvel-Eibrink, Conrad V. Fernandez, Norbert Graf, Paul E. Grundy, James I. Geller, Jeffrey S. Dome, Elizabeth J. Perlman, Manfred Gessler, Vicki Huff, and Kathy Pritchard-Jones. Hallmark discoveries in the biology of wilms tumour. Nature reviews. Urology, 21:158-180, Oct 2024. URL: https://doi.org/10.1038/s41585-023-00824-0, doi:10.1038/s41585-023-00824-0. This article has 27 citations.

3. (tiburcio2024drosharegulatesmesenchymal pages 1-3): Patricia D.B. Tiburcio, Kavita Desai, Jiwoong Kim, Qinbo Zhou, Lei Guo, Xue Xiao, Li Zhou, Aysen Yuksel, Daniel R. Catchpoole, James F. Amatruda, Lin Xu, and Kenneth S. Chen. Drosha regulates mesenchymal gene expression in wilms tumor. Molecular cancer research : MCR, 22:711-720, Apr 2024. URL: https://doi.org/10.1158/1541-7786.mcr-23-0930, doi:10.1158/1541-7786.mcr-23-0930. This article has 9 citations.

4. (neagu2025wilms’tumora pages 6-8): Mihai Cristian Neagu, Vlad Laurenţiu David, Emil Radu Iacob, Sorin Dan Chiriac, Florin Lucian Muntean, and Eugen Sorin Boia. Wilms’ tumor: a review of clinical characteristics, treatment advances, and research opportunities. Medicina, 61:491, Mar 2025. URL: https://doi.org/10.3390/medicina61030491, doi:10.3390/medicina61030491. This article has 16 citations.

5. (perotti2024hallmarkdiscoveriesin pages 25-29): Daniela Perotti, Richard D. Williams, Jenny Wegert, Jack Brzezinski, Mariana Maschietto, Sara Ciceri, David Gisselsson, Samantha Gadd, Amy L. Walz, Rhoikos Furtwaengler, Jarno Drost, Reem Al-Saadi, Nicholas Evageliou, Saskia L. Gooskens, Andrew L. Hong, Andrew J. Murphy, Michael V. Ortiz, Maureen J. O’Sullivan, Elizabeth A. Mullen, Marry M. van den Heuvel-Eibrink, Conrad V. Fernandez, Norbert Graf, Paul E. Grundy, James I. Geller, Jeffrey S. Dome, Elizabeth J. Perlman, Manfred Gessler, Vicki Huff, and Kathy Pritchard-Jones. Hallmark discoveries in the biology of wilms tumour. Nature reviews. Urology, 21:158-180, Oct 2024. URL: https://doi.org/10.1038/s41585-023-00824-0, doi:10.1038/s41585-023-00824-0. This article has 27 citations.

6. (perotti2024hallmarkdiscoveriesin pages 10-14): Daniela Perotti, Richard D. Williams, Jenny Wegert, Jack Brzezinski, Mariana Maschietto, Sara Ciceri, David Gisselsson, Samantha Gadd, Amy L. Walz, Rhoikos Furtwaengler, Jarno Drost, Reem Al-Saadi, Nicholas Evageliou, Saskia L. Gooskens, Andrew L. Hong, Andrew J. Murphy, Michael V. Ortiz, Maureen J. O’Sullivan, Elizabeth A. Mullen, Marry M. van den Heuvel-Eibrink, Conrad V. Fernandez, Norbert Graf, Paul E. Grundy, James I. Geller, Jeffrey S. Dome, Elizabeth J. Perlman, Manfred Gessler, Vicki Huff, and Kathy Pritchard-Jones. Hallmark discoveries in the biology of wilms tumour. Nature reviews. Urology, 21:158-180, Oct 2024. URL: https://doi.org/10.1038/s41585-023-00824-0, doi:10.1038/s41585-023-00824-0. This article has 27 citations.

7. (perotti2024hallmarkdiscoveriesin pages 14-17): Daniela Perotti, Richard D. Williams, Jenny Wegert, Jack Brzezinski, Mariana Maschietto, Sara Ciceri, David Gisselsson, Samantha Gadd, Amy L. Walz, Rhoikos Furtwaengler, Jarno Drost, Reem Al-Saadi, Nicholas Evageliou, Saskia L. Gooskens, Andrew L. Hong, Andrew J. Murphy, Michael V. Ortiz, Maureen J. O’Sullivan, Elizabeth A. Mullen, Marry M. van den Heuvel-Eibrink, Conrad V. Fernandez, Norbert Graf, Paul E. Grundy, James I. Geller, Jeffrey S. Dome, Elizabeth J. Perlman, Manfred Gessler, Vicki Huff, and Kathy Pritchard-Jones. Hallmark discoveries in the biology of wilms tumour. Nature reviews. Urology, 21:158-180, Oct 2024. URL: https://doi.org/10.1038/s41585-023-00824-0, doi:10.1038/s41585-023-00824-0. This article has 27 citations.

8. (perotti2024hallmarkdiscoveriesin pages 17-21): Daniela Perotti, Richard D. Williams, Jenny Wegert, Jack Brzezinski, Mariana Maschietto, Sara Ciceri, David Gisselsson, Samantha Gadd, Amy L. Walz, Rhoikos Furtwaengler, Jarno Drost, Reem Al-Saadi, Nicholas Evageliou, Saskia L. Gooskens, Andrew L. Hong, Andrew J. Murphy, Michael V. Ortiz, Maureen J. O’Sullivan, Elizabeth A. Mullen, Marry M. van den Heuvel-Eibrink, Conrad V. Fernandez, Norbert Graf, Paul E. Grundy, James I. Geller, Jeffrey S. Dome, Elizabeth J. Perlman, Manfred Gessler, Vicki Huff, and Kathy Pritchard-Jones. Hallmark discoveries in the biology of wilms tumour. Nature reviews. Urology, 21:158-180, Oct 2024. URL: https://doi.org/10.1038/s41585-023-00824-0, doi:10.1038/s41585-023-00824-0. This article has 27 citations.

9. (cantoni2026tumormicroenvironmentand pages 2-4): Claudia Cantoni, Valerio Gaetano Vellone, Barbara Cafferata, Gabriele Gaggero, Martina Serra, Filippo Spreafico, Cristina Bottino, and Grazia Maria Spaggiari. Tumor microenvironment and immune response against wilms tumor: evasion mechanisms and implications for immunotherapeutic approaches. Cancers, 18:908, Mar 2026. URL: https://doi.org/10.3390/cancers18060908, doi:10.3390/cancers18060908. This article has 0 citations.

10. (murphy2023geneticandepigenetic pages 4-5): Andrew J. Murphy, Changde Cheng, Justin Williams, Timothy I. Shaw, Emilia M. Pinto, Karissa Dieseldorff-Jones, Jack Brzezinski, Lindsay A. Renfro, Brett Tornwall, Vicki Huff, Andrew L. Hong, Elizabeth A. Mullen, Brian Crompton, Jeffrey S. Dome, Conrad V. Fernandez, James I. Geller, Peter F. Ehrlich, Heather Mulder, Ninad Oak, Jamie Maciezsek, Carolyn M. Jablonowski, Andrew M. Fleming, Prahalathan Pichavaram, Christopher L. Morton, John Easton, Kim E. Nichols, Michael R. Clay, Teresa Santiago, Jinghui Zhang, Jun Yang, Gerard P. Zambetti, Zhaoming Wang, Andrew M. Davidoff, and Xiang Chen. Genetic and epigenetic features of bilateral wilms tumor predisposition in patients from the children’s oncology group aren18b5-q. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43730-0, doi:10.1038/s41467-023-43730-0. This article has 28 citations and is from a highest quality peer-reviewed journal.

11. (murphy2023geneticandepigenetic pages 1-2): Andrew J. Murphy, Changde Cheng, Justin Williams, Timothy I. Shaw, Emilia M. Pinto, Karissa Dieseldorff-Jones, Jack Brzezinski, Lindsay A. Renfro, Brett Tornwall, Vicki Huff, Andrew L. Hong, Elizabeth A. Mullen, Brian Crompton, Jeffrey S. Dome, Conrad V. Fernandez, James I. Geller, Peter F. Ehrlich, Heather Mulder, Ninad Oak, Jamie Maciezsek, Carolyn M. Jablonowski, Andrew M. Fleming, Prahalathan Pichavaram, Christopher L. Morton, John Easton, Kim E. Nichols, Michael R. Clay, Teresa Santiago, Jinghui Zhang, Jun Yang, Gerard P. Zambetti, Zhaoming Wang, Andrew M. Davidoff, and Xiang Chen. Genetic and epigenetic features of bilateral wilms tumor predisposition in patients from the children’s oncology group aren18b5-q. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43730-0, doi:10.1038/s41467-023-43730-0. This article has 28 citations and is from a highest quality peer-reviewed journal.

12. (nirgude2024cancerpredispositionsignaling pages 1-2): Snehal Nirgude, Natali S. Sobel Naveh, Sanam L. Kavari, Emily M. Traxler, and Jennifer M. Kalish. Cancer predisposition signaling in beckwith-wiedemann syndrome drives wilms tumor development. British Journal of Cancer, 130:638-650, Dec 2024. URL: https://doi.org/10.1038/s41416-023-02538-x, doi:10.1038/s41416-023-02538-x. This article has 9 citations and is from a domain leading peer-reviewed journal.

13. (murphy2023geneticandepigenetic pages 7-9): Andrew J. Murphy, Changde Cheng, Justin Williams, Timothy I. Shaw, Emilia M. Pinto, Karissa Dieseldorff-Jones, Jack Brzezinski, Lindsay A. Renfro, Brett Tornwall, Vicki Huff, Andrew L. Hong, Elizabeth A. Mullen, Brian Crompton, Jeffrey S. Dome, Conrad V. Fernandez, James I. Geller, Peter F. Ehrlich, Heather Mulder, Ninad Oak, Jamie Maciezsek, Carolyn M. Jablonowski, Andrew M. Fleming, Prahalathan Pichavaram, Christopher L. Morton, John Easton, Kim E. Nichols, Michael R. Clay, Teresa Santiago, Jinghui Zhang, Jun Yang, Gerard P. Zambetti, Zhaoming Wang, Andrew M. Davidoff, and Xiang Chen. Genetic and epigenetic features of bilateral wilms tumor predisposition in patients from the children’s oncology group aren18b5-q. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43730-0, doi:10.1038/s41467-023-43730-0. This article has 28 citations and is from a highest quality peer-reviewed journal.

14. (mittal2024targetingtrip13in pages 2-3): Karuna Mittal, Garrett W. Cooper, Benjamin P. Lee, Yongdong Su, Katie T. Skinner, Jenny Shim, Hunter C. Jonus, Won Jun Kim, Mihir Doshi, Diego Almanza, Bryan D. Kynnap, Amanda L. Christie, Xiaoping Yang, Glenn S. Cowley, Brittaney A. Leeper, Christopher L. Morton, Bhakti Dwivedi, Taylor Lawrence, Manali Rupji, Paula Keskula, Stephanie Meyer, Catherine M. Clinton, Manoj Bhasin, Brian D. Crompton, Yuen-Yi Tseng, Jesse S. Boehm, Keith L. Ligon, David E. Root, Andrew J. Murphy, David M. Weinstock, Prafulla C. Gokhale, Jennifer M. Spangle, Miguel N. Rivera, Elizabeth A. Mullen, Kimberly Stegmaier, Kelly C. Goldsmith, William C. Hahn, and Andrew L. Hong. Targeting trip13 in favorable histology wilms tumor with nuclear export inhibitors synergizes with doxorubicin. Communications Biology, Apr 2024. URL: https://doi.org/10.1038/s42003-024-06140-6, doi:10.1038/s42003-024-06140-6. This article has 6 citations and is from a peer-reviewed journal.

15. (lim2024interethnicvariationsin pages 15-17): Kia Teng Lim and Amos H. P. Loh. Inter-ethnic variations in the clinical, pathological, and molecular characteristics of wilms tumor. Cancers, 16:3051, Sep 2024. URL: https://doi.org/10.3390/cancers16173051, doi:10.3390/cancers16173051. This article has 6 citations.

16. (NCT05985161 chunk 1):  A Study of Selinexor in People With Wilms Tumors and Other Solid Tumors. Memorial Sloan Kettering Cancer Center. 2023. ClinicalTrials.gov Identifier: NCT05985161

17. (cantoni2026tumormicroenvironmentand pages 19-20): Claudia Cantoni, Valerio Gaetano Vellone, Barbara Cafferata, Gabriele Gaggero, Martina Serra, Filippo Spreafico, Cristina Bottino, and Grazia Maria Spaggiari. Tumor microenvironment and immune response against wilms tumor: evasion mechanisms and implications for immunotherapeutic approaches. Cancers, 18:908, Mar 2026. URL: https://doi.org/10.3390/cancers18060908, doi:10.3390/cancers18060908. This article has 0 citations.

18. (perotti2024hallmarkdiscoveriesin pages 21-25): Daniela Perotti, Richard D. Williams, Jenny Wegert, Jack Brzezinski, Mariana Maschietto, Sara Ciceri, David Gisselsson, Samantha Gadd, Amy L. Walz, Rhoikos Furtwaengler, Jarno Drost, Reem Al-Saadi, Nicholas Evageliou, Saskia L. Gooskens, Andrew L. Hong, Andrew J. Murphy, Michael V. Ortiz, Maureen J. O’Sullivan, Elizabeth A. Mullen, Marry M. van den Heuvel-Eibrink, Conrad V. Fernandez, Norbert Graf, Paul E. Grundy, James I. Geller, Jeffrey S. Dome, Elizabeth J. Perlman, Manfred Gessler, Vicki Huff, and Kathy Pritchard-Jones. Hallmark discoveries in the biology of wilms tumour. Nature reviews. Urology, 21:158-180, Oct 2024. URL: https://doi.org/10.1038/s41585-023-00824-0, doi:10.1038/s41585-023-00824-0. This article has 27 citations.

19. (rastegar2026understandinganaplasticwilmsa pages 38-42): B Rastegar. Understanding anaplastic wilms tumors: spatial insights into their evolution and clinical significance. Unknown journal, 2026.

20. (murphy2023geneticandepigenetic pages 6-7): Andrew J. Murphy, Changde Cheng, Justin Williams, Timothy I. Shaw, Emilia M. Pinto, Karissa Dieseldorff-Jones, Jack Brzezinski, Lindsay A. Renfro, Brett Tornwall, Vicki Huff, Andrew L. Hong, Elizabeth A. Mullen, Brian Crompton, Jeffrey S. Dome, Conrad V. Fernandez, James I. Geller, Peter F. Ehrlich, Heather Mulder, Ninad Oak, Jamie Maciezsek, Carolyn M. Jablonowski, Andrew M. Fleming, Prahalathan Pichavaram, Christopher L. Morton, John Easton, Kim E. Nichols, Michael R. Clay, Teresa Santiago, Jinghui Zhang, Jun Yang, Gerard P. Zambetti, Zhaoming Wang, Andrew M. Davidoff, and Xiang Chen. Genetic and epigenetic features of bilateral wilms tumor predisposition in patients from the children’s oncology group aren18b5-q. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43730-0, doi:10.1038/s41467-023-43730-0. This article has 28 citations and is from a highest quality peer-reviewed journal.

21. (cantoni2026tumormicroenvironmentand pages 6-7): Claudia Cantoni, Valerio Gaetano Vellone, Barbara Cafferata, Gabriele Gaggero, Martina Serra, Filippo Spreafico, Cristina Bottino, and Grazia Maria Spaggiari. Tumor microenvironment and immune response against wilms tumor: evasion mechanisms and implications for immunotherapeutic approaches. Cancers, 18:908, Mar 2026. URL: https://doi.org/10.3390/cancers18060908, doi:10.3390/cancers18060908. This article has 0 citations.

22. (murphy2023geneticandepigenetic pages 5-6): Andrew J. Murphy, Changde Cheng, Justin Williams, Timothy I. Shaw, Emilia M. Pinto, Karissa Dieseldorff-Jones, Jack Brzezinski, Lindsay A. Renfro, Brett Tornwall, Vicki Huff, Andrew L. Hong, Elizabeth A. Mullen, Brian Crompton, Jeffrey S. Dome, Conrad V. Fernandez, James I. Geller, Peter F. Ehrlich, Heather Mulder, Ninad Oak, Jamie Maciezsek, Carolyn M. Jablonowski, Andrew M. Fleming, Prahalathan Pichavaram, Christopher L. Morton, John Easton, Kim E. Nichols, Michael R. Clay, Teresa Santiago, Jinghui Zhang, Jun Yang, Gerard P. Zambetti, Zhaoming Wang, Andrew M. Davidoff, and Xiang Chen. Genetic and epigenetic features of bilateral wilms tumor predisposition in patients from the children’s oncology group aren18b5-q. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43730-0, doi:10.1038/s41467-023-43730-0. This article has 28 citations and is from a highest quality peer-reviewed journal.