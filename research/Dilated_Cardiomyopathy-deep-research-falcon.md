---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-06T04:11:21.371034'
end_time: '2026-03-06T04:24:09.427570'
duration_seconds: 768.06
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dilated Cardiomyopathy
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Dilated Cardiomyopathy**.
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
- **Disease Name:** Dilated Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Dilated Cardiomyopathy**.
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


## Comprehensive Research Report: Dilated Cardiomyopathy (DCM) Pathophysiology (Molecular & Cellular)

### Disease identifiers
- **Disease name:** Dilated cardiomyopathy (DCM)
- **Category:** Complex (heterogeneous; monogenic + polygenic + acquired contributors)
- **Ontology examples in recent resources:** Open Targets uses **EFO:0000407 (dilated cardiomyopathy)** and **HP:0001644 (Dilated cardiomyopathy phenotype)** (not a MONDO mapping in the retrieved evidence). (arnautu2024geneticsandmolecular pages 5-7)

---

## 1) Key concepts and definitions (current understanding)

### Clinical definition (phenotype-level)
DCM is characterized by **left-ventricular or biventricular dilatation and systolic dysfunction** not explained by abnormal loading conditions or ischemic heart disease (non-ischemic DCM definitions are explicitly stated in the CMR risk meta-analysis). (eichhorn2024riskstratificationin pages 1-2)

### Genetic architecture: monogenic → oligogenic/polygenic spectrum
Recent authoritative reviews emphasize that DCM frequently reflects a **final common pathway** reached through diverse genetic and acquired perturbations, and that many cases fall on a **monogenic-to-polygenic continuum**.
- Eldemire et al. note that **“Up to 50% of nonischemic DCM is genetic or idiopathic”** and that **gene–environment interactions** modify phenotypic expression. (eldemire2024geneticsofdilated pages 1-3)
- Newman & Burke frame DCM genetics as a spectrum: **“a complex genetic spectrum ranging from monogenic to polygenic”** and state that prevalence estimates derived from population imaging support a higher background burden than historically recognized. (newman2024dilatedcardiomyopathya pages 1-2)
- Oligogenic contributions are highlighted: **“20–38% of DCM may have an oligogenic basis”** (multiple rare variants contributing to similar phenotype). (eldemire2024geneticsofdilated pages 1-3)

### Epidemiology (recently updated estimates)
Population estimates have been revised upward compared with older registry estimates.
- Newman & Burke summarize that revised population estimates place prevalence **near 1:250 (0.4%)**, with **UK Biobank cardiac MRI ~1 in 220 (0.45%, 95% CI 0.39–0.53%)**. (newman2024dilatedcardiomyopathya pages 1-2)

---

## 2) Core pathophysiology: primary mechanisms and dysregulated pathways

DCM progression is driven by **contractile failure and maladaptive remodeling**, typically involving (i) impaired force generation and/or transmission, (ii) stress-response pathway activation, and (iii) myocardial remodeling with fibrosis and arrhythmogenic substrate.

### 2.1 Sarcomere dysfunction and mechanosensing failure (central mechanism)
A unifying mechanism across many genetic DCM forms is depressed tension generation with altered mechanotransduction.
- Solaro et al. summarize the prevailing concept: variants in sarcomeric/cytoskeletal proteins **“cause a decrease in tension by the myofilaments,”** leading to signaling abnormalities and later **“structural and functional maladaptations, leading to heart failure.”** (solaro2024emergingconceptsof pages 1-2)

**TTN truncating variants (TTNtv)** are the most common monogenic contributors in adult DCM and are strongly tied to sarcomere integrity and mechanosensing.
- In a human explanted-heart cohort (n=127 DCM samples), Kellermayer et al. report: **“The occurrence of TTNtv was found to be 15% in the DCM cohort.”** They also report reduced full-length titin in TTNtv+ samples and show sarcomere-localization evidence using proteomics and STED microscopy. (kellermayer2024truncatedtitinis pages 1-2)
- Their abstract summarizes a key mechanistic inference: sarcomeric epitope analyses pointed to **“possible structural defects in the I/A junction and the M-band of TTNtv+ sarcomeres, which probably contribute, possibly via faulty mechanosensor function, to the development of manifest DCM.”** (kellermayer2024truncatedtitinis pages 1-2)

**Direct visual evidence:** STED super-resolution microscopy images show preserved gross sarcomeric registry in TTNtv+ tissue compared with TTNtv− and controls, supporting structural integration of titin epitopes in sarcomeres rather than diffuse mislocalization. (kellermayer2024truncatedtitinis media 0d428a5a, kellermayer2024truncatedtitinis media 3e1be5e2)

### 2.2 RNA processing and alternative splicing dysregulation (RBM20 axis)
RBM20 cardiomyopathy illustrates how gene-expression regulation can drive DCM by altering protein isoforms (notably titin).
- Gregorich et al. describe that pathogenic RBM20 variants are **“linked to aggressive dilated cardiomyopathy with early onset heart failure and high mortality.”** Mechanistically, certain variants **“not only disrupt splicing but also hinder nucleocytoplasmic transport and lead to the formation of RBM20 biomolecular condensates in the sarcoplasm.”** (gregorich2024mechanismsofrbm20 pages 1-3)
- Newman & Burke further connect RBM20 dysfunction to titin isoforms and arrhythmia mechanisms, noting RBM20-mediated splicing changes shift titin toward more compliant isoforms and affect Ca2+ handling genes (e.g., CACNA1C, CAMK2D). (newman2024dilatedcardiomyopathya pages 7-8)

### 2.3 Nuclear envelope / mechanotransduction defects (LMNA axis)
Nuclear structural instability and altered mechanotransduction contribute to arrhythmia-prone and progressive DCM.
- Newman & Burke characterize LMNA cardiomyopathy as **“the most malignant genetic DCM,”** with **“a high burden of conduction system disease… malignant VAs,”** and **“very high rates of progression to end-stage HF.”** (newman2024dilatedcardiomyopathya pages 13-14)

### 2.4 Inflammation and immune activation (especially inflammatory DCM / myocarditis transition)
Immune-mediated injury can be causal (primary) or act as an accelerator of remodeling.
- Xu et al. outline a canonical myocarditis-to-DCM progression model with **three phases**, stating that chronic phases **“can last from months to years”** and that **“chronic cardiac inflammation can finally result in the incidence of DCM.”** (xu2024constructionandevaluation pages 1-2)
- Vicenzetto et al. note that virus-negative and/or virus-positive inflammatory cardiomyopathy has drawn attention because of emerging etiologic treatments, linking inflammatory cardiomyopathy to the **“onset and progression of dilated cardiomyopathy (DCM).”** (vicenzetto2024theroleof pages 1-2)

### 2.5 Fibrosis and adverse myocardial remodeling (ECM + scar as a downstream integrator)
Fibrosis (replacement and interstitial) is a common downstream consequence across genetic and acquired DCM, contributing to systolic dysfunction and arrhythmogenesis.
- In the largest recent quantitative synthesis, a JAMA systematic review/meta-analysis (103 studies; 29,687 patients) reported that **late gadolinium enhancement (LGE)** is strongly prognostic: LGE presence associated with **all-cause mortality (HR 1.81)** and **arrhythmic events (HR 2.69)**, among other outcomes. (eichhorn2024riskstratificationin pages 1-2)

### 2.6 Polygenic mechanisms and myocardial resilience (GWAS-era insights)
Recent 2024 Nature Genetics GWAS analyses reinforce that cardiomyocytes and the contractile apparatus are central, while also identifying non-cardiomyocyte states and intercellular signaling.
- Jurgens et al. performed GWAS/MTAG with **9,365 cases and 946,368 controls**, finding **70 genome-wide significant loci**; enrichment analyses highlighted **“the central role of the cardiomyocyte and contractile apparatus.”** (jurgens2024genomewideassociationstudy pages 1-2)
- Zheng et al. identified **80 loci (59 genome-wide + 21 FDR 1%)** and used single-nucleus transcriptomics of end-stage DCM hearts to identify noncardiomyocyte states and pathway signals (e.g., Ephrin-B/BMP6 pathway involvement). (zheng2024genomewideassociationanalysis pages 10-11)

---

## 3) Key molecular players, cell types, and anatomical locations

### 3.1 Genes/proteins (representative, evidence-supported)
Key gene classes include sarcomere/contractility (TTN, MYH7, troponins), nuclear envelope (LMNA), RNA splicing (RBM20), cytoskeleton/desmosome (FLNC, DSP, DES), protein quality control (BAG3), and ion handling. (newman2024dilatedcardiomyopathya pages 4-6, newman2024dilatedcardiomyopathya pages 13-14, gregorich2024mechanismsofrbm20 pages 1-3, newman2024dilatedcardiomyopathya pages 7-8)

### 3.2 Cell types
- **Cardiomyocytes** are central (contractile and mechanosensing enrichment in GWAS; sarcomere defects; nuclear/splicing pathology). (jurgens2024genomewideassociationstudy pages 1-2, kellermayer2024truncatedtitinis pages 1-2)
- **Immune cells (T cells, macrophages, neutrophils)** contribute particularly in inflammatory DCM/myocarditis-associated DCM; computational deconvolution reported differences in activated CD4 memory T cells, Tregs, and neutrophils. (xu2024constructionandevaluation pages 1-2)

### 3.3 Anatomical locations
- Predominant phenotype arises in the **left ventricle**, often biventricular; this is reflected in imaging-based phenotyping and outcomes. (eichhorn2024riskstratificationin pages 1-2)

### 3.4 Chemical entities
- **Calcium ion (Ca2+)** is mechanistically implicated through excitation–contraction coupling and splicing effects (RBM20 targets) and arrhythmogenesis. (newman2024dilatedcardiomyopathya pages 7-8)
- **Gadolinium** contrast is used for CMR LGE, a fibrosis surrogate with strong prognostic hazard ratios in DCM. (eichhorn2024riskstratificationin pages 1-2)

---

## 4) Biological processes (GO-style) disrupted (for knowledge-base annotation)
A minimal, evidence-aligned GO-style set includes:
- **Sarcomere organization / muscle contraction / mechanosensing** (TTN, MYH7 and sarcomeric tension model). (solaro2024emergingconceptsof pages 1-2, kellermayer2024truncatedtitinis pages 1-2)
- **Alternative splicing / mRNA processing** (RBM20). (gregorich2024mechanismsofrbm20 pages 1-3, newman2024dilatedcardiomyopathya pages 7-8)
- **Immune response / cytokine-mediated signaling** (myocarditis transition to DCM; immune infiltration signatures). (vicenzetto2024theroleof pages 1-2, xu2024constructionandevaluation pages 1-2)
- **Extracellular matrix organization / fibrosis (scar formation)** (LGE-associated outcomes). (eichhorn2024riskstratificationin pages 1-2)

---

## 5) Cellular components (GO-CC style) where key processes occur
- **Sarcomere substructures (I/A junction; M-band)**: implicated as structurally perturbed regions in TTNtv+ DCM sarcomeres. (kellermayer2024truncatedtitinis pages 1-2)
- **Sarcoplasm**: site of RBM20 biomolecular condensates in certain pathogenic variants. (gregorich2024mechanismsofrbm20 pages 1-3)
- **Nuclear envelope / nuclear lamina**: LMNA-driven disease mechanism (nuclear structure/function). (newman2024dilatedcardiomyopathya pages 13-14)

---

## 6) Disease progression: sequence of events (trigger → phenotype)

### Stage model (integrated)
1. **Initial trigger**: rare pathogenic variant (e.g., TTNtv, LMNA, RBM20) and/or acquired injury (e.g., viral myocarditis, toxins), often with gene–environment interaction and sometimes oligogenic background. (eldemire2024geneticsofdilated pages 1-3, newman2024dilatedcardiomyopathya pages 13-14)
2. **Primary cellular dysfunction**:
   - Reduced tension generation and altered mechanotransduction (sarcomere dysfunction). (solaro2024emergingconceptsof pages 1-2, kellermayer2024truncatedtitinis pages 1-2)
   - Spliceopathy with altered titin isoforms and potentially Ca2+ handling gene splicing (RBM20). (gregorich2024mechanismsofrbm20 pages 1-3, newman2024dilatedcardiomyopathya pages 7-8)
   - Nuclear envelope dysfunction and conduction/arrhythmia susceptibility (LMNA). (newman2024dilatedcardiomyopathya pages 13-14)
   - Immune activation and chronic inflammatory injury (myocarditis-to-DCM phases). (xu2024constructionandevaluation pages 1-2)
3. **Maladaptive remodeling**: ventricular dilatation, wall thinning, fibrosis, electrical remodeling → arrhythmogenic substrate. (solaro2024emergingconceptsof pages 1-2, eichhorn2024riskstratificationin pages 1-2)
4. **Clinical syndrome**: progressive HF, arrhythmias, thromboembolism risk, and in advanced cases transplantation/VAD. Pediatric outcomes can be severe early (nearly 40% transplant/death within 2 years in pediatric DCM review). (malinow2024pediatricdilatedcardiomyopathy pages 1-2)

---

## 7) Phenotypic manifestations (clinical phenotypes linked to mechanisms)
- **Systolic dysfunction with chamber dilation** (definitional phenotype). (eichhorn2024riskstratificationin pages 1-2)
- **Arrhythmias and sudden cardiac death risk**, particularly in arrhythmogenic genetic subtypes (e.g., LMNA, FLNC, RBM20). (newman2024dilatedcardiomyopathya pages 13-14, gregorich2024mechanismsofrbm20 pages 1-3)
- **Fibrosis/scar** detectable by CMR LGE, strongly associated with mortality and arrhythmic outcomes. (eichhorn2024riskstratificationin pages 1-2)

---

## 8) Recent developments (prioritizing 2023–2024)

### 8.1 Human-tissue mechanistic resolution of TTNtv controversy (2024)
Kellermayer et al. used NGS + proteomics + STED microscopy in human DCM myocardium, supporting sarcomere integration of truncated titin and pointing to I/A junction and M-band defects as mechanistic contributors. (kellermayer2024truncatedtitinis pages 1-2, kellermayer2024truncatedtitinis media 0d428a5a, kellermayer2024truncatedtitinis media 3e1be5e2)

### 8.2 RBM20 condensates as a candidate disease mechanism (2024)
RBM20 pathogenic variants may act beyond splice disruption, involving altered nucleocytoplasmic transport and formation of sarcoplasmic condensates, with ongoing debate on which mechanism is causal. (gregorich2024mechanismsofrbm20 pages 1-3)

### 8.3 GWAS and single-nucleus transcriptomics define pathways and cell states (2024)
Large-scale GWAS/MTAG (2024) identifies dozens of loci and reinforces cardiomyocyte contractile apparatus enrichment; complementary analyses implicate noncardiomyocyte states and signaling pathways in end-stage myocardium. (jurgens2024genomewideassociationstudy pages 1-2, zheng2024genomewideassociationanalysis pages 10-11)

### 8.4 Imaging biomarkers outrank LVEF for certain endpoints (2024)
In nonischemic DCM, LGE presence/extent is consistently associated with mortality and arrhythmic outcomes, while LVEF was not significantly associated with mortality/arrhythmic endpoints in the meta-analysis. (eichhorn2024riskstratificationin pages 1-2)

---

## 9) Current applications and real-world implementations

### 9.1 Genetic evaluation, counseling, and cascade screening
- Eldemire et al. emphasize genetic testing as integral to **diagnosis, prognostication, and treatment**, alongside detailed family history and rhythm monitoring. (eldemire2024geneticsofdilated pages 1-3, eldemire2024geneticsofdilated pages 3-5)
- Newman & Burke report real-world testing yield and implementation considerations (VUS burden; cost-effectiveness of cascade testing vs periodic surveillance; society-level guideline differences). (newman2024dilatedcardiomyopathya pages 14-17)

### 9.2 CMR tissue characterization for risk stratification
- Eldemire et al. describe CMRI as a gold standard for volumes/function and tissue characterization, while outcome associations for LGE are emphasized. (eldemire2024geneticsofdilated pages 3-5)
- The 2024 JAMA meta-analysis provides quantitative risk estimates supporting LGE-based stratification. (eichhorn2024riskstratificationin pages 1-2)

### 9.3 Precision medicine direction: genotype-informed management
- Reviews emphasize the move toward mechanism-specific therapies and genotype-informed decisions (e.g., LMNA-associated device decisions; potential future polygenic risk integration). (eldemire2024geneticsofdilated pages 1-3, newman2024dilatedcardiomyopathya pages 13-14)

---

## 10) Key statistics and recent quantitative findings (selected)
- **Prevalence (revised):** ~1:250 overall; UK Biobank CMR ~1 in 220. (newman2024dilatedcardiomyopathya pages 1-2)
- **Familial/genetic:** ~40% of familial DCM has an identifiable genetic cause. (eldemire2024geneticsofdilated pages 1-3)
- **Oligogenic basis:** 20–38% may be oligogenic. (eldemire2024geneticsofdilated pages 1-3)
- **TTNtv in human DCM myocardium:** 15% in 127 explanted DCM samples. (kellermayer2024truncatedtitinis pages 1-2)
- **TTNtv frequencies in cohorts:** ~11–15% sporadic adult DCM; 23–27% familial DCM (review synthesis). (newman2024dilatedcardiomyopathya pages 7-8)
- **CMR outcomes:** LGE presence HR 1.81 (all-cause mortality) and HR 2.69 (arrhythmic events) in 29,687-patient meta-analysis. (eichhorn2024riskstratificationin pages 1-2)
- **GWAS scale:** 9,365 cases/946,368 controls; 70 loci; 63 prioritized genes (2024). (jurgens2024genomewideassociationstudy pages 1-2)

---

## Knowledge-base-ready structured artifacts

### Mechanisms summary table
| Mechanism | Key Genes/Proteins (HGNC) | Affected Cell Types (CL) | Dysregulated Processes (GO-like) | Evidence/Data Points | Key Citations |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Sarcomere Dysfunction** | *TTN*, *MYH7*, *TNNT2*, *TNNC1* | Cardiomyocyte | Muscle contraction, sarcomere organization, mechanosensing | *TTN* truncations (TTNtv) found in 15-25% of familial DCM; truncated titin integrates into sarcomeres ("poison peptide" effect) causing structural defects; altered length-dependent activation. | (arnautu2024geneticsandmolecular pages 5-7, kellermayer2024truncatedtitinis pages 1-2, newman2024dilatedcardiomyopathya pages 7-8, kellermayer2024truncatedtitinis pages 6-7) |
| **Nuclear Envelope Instability** | *LMNA* | Cardiomyocyte, Fibroblast | Nuclear organization, chromatin regulation, mechanotransduction | *LMNA* variants found in 4-8% of all DCM and up to 30% of familial cases with conduction disease; associated with "malignant" phenotype: high fibrosis, arrhythmias, and progression to end-stage HF. | (arnautu2024geneticsandmolecular pages 5-7, arnautu2024geneticsandmolecular pages 7-8, newman2024dilatedcardiomyopathya pages 13-14) |
| **Defective RNA Splicing** | *RBM20* | Cardiomyocyte | mRNA processing, alternative splicing | *RBM20* dysfunction causes aberrant splicing of *TTN* (shift to compliant N2BA isoform) and Ca2+ handling genes (*CAMK2D*, *CACNA1C*); forms toxic sarcoplasmic ribonucleoprotein condensates. | (arnautu2024geneticsandmolecular pages 5-7, gregorich2024mechanismsofrbm20 pages 1-3, newman2024dilatedcardiomyopathya pages 7-8) |
| **Cytoskeletal & Desmosomal Integrity** | *DES*, *FLNC*, *DSP*, *PKP2* | Cardiomyocyte | Intermediate filament organization, cell-cell adhesion | *FLNC* variants linked to high arrhythmic risk even with mild LV dysfunction; *DSP* variants found in ~13% of transplant cases; disruption leads to cell death and fibrofatty replacement. | (arnautu2024geneticsandmolecular pages 5-7, arnautu2024geneticsandmolecular pages 7-8, newman2024dilatedcardiomyopathya pages 13-14) |
| **Fibrosis & Structural Remodeling** | Polygenic loci (e.g., *HSPB7*, *BAG3*) | Fibroblast, Cardiomyocyte | Extracellular matrix organization, tissue fibrosis | Presence of Late Gadolinium Enhancement (LGE) on CMR is a strong predictor of adverse outcomes: HR 1.81 for all-cause mortality, HR 2.69 for arrhythmic events. | (jurgens2024genomewideassociationstudy pages 1-2, zheng2024genomewideassociationanalysis pages 10-11, eichhorn2024riskstratificationin pages 1-2) |
| **Immune & Inflammatory Activation** | *HLA* alleles, Cytokines | T cell (CD3+), Macrophage | Innate/adaptive immune response, cytokine production | Persistence of viral genome or autoimmune reaction triggers chronic inflammation; single-cell transcriptomics reveal distinct immune cell states (e.g., exhausted CD8+ T cells) in DCM hearts. | (vicenzetto2024theroleof pages 1-2, xu2024constructionandevaluation pages 1-2) |
| **Ion Channel Dysregulation** | *SCN5A*, *PLN* | Cardiomyocyte | Cardiac conduction, calcium ion transport | *PLN* and *SCN5A* variants disrupt excitation-contraction coupling and impulse propagation, significantly increasing the risk of ventricular arrhythmias and sudden cardiac death. | (arnautu2024geneticsandmolecular pages 5-7, newman2024dilatedcardiomyopathya pages 4-6) |


*Table: A summary of core mechanistic pathways in DCM, linking genetic and molecular drivers to specific cellular consequences and clinical evidence from recent literature (2023–2024).*

### Ontology-style entity mapping table
| Category | Entity (Symbol/ID) | Mechanism & Role in DCM | Supporting Contexts |
| :--- | :--- | :--- | :--- |
| **Gene** | *TTN* (HGNC:12403) | **Titin**: Giant sarcomeric protein. Truncating variants (TTNtv) occur in 15–25% of familial DCM. Mechanisms include haploinsufficiency and a "poison peptide" effect where truncated proteins integrate into the sarcomere, causing structural defects and altered mechanosensing. | (arnautu2024geneticsandmolecular pages 5-7, kellermayer2024truncatedtitinis pages 1-2, newman2024dilatedcardiomyopathya pages 7-8, kellermayer2024truncatedtitinis pages 6-7) |
| **Gene** | *LMNA* (HGNC:6636) | **Lamin A/C**: Nuclear envelope protein. Variants cause "malignant" DCM with high risks of conduction disease, arrhythmia, and sudden death (SCD); prevalence 4–8% overall, up to 30% in familial cases with conduction defects. | (arnautu2024geneticsandmolecular pages 5-7, arnautu2024geneticsandmolecular pages 7-8, newman2024dilatedcardiomyopathya pages 13-14) |
| **Gene** | *RBM20* (HGNC:9907) | **RNA Binding Motif 20**: Splicing regulator. Dysfunction leads to aberrant splicing of *TTN* (shift to compliant N2BA isoform) and Ca2+ handling genes (*CAMK2D*, *CACNA1C*); formation of toxic sarcoplasmic ribonucleoprotein condensates. | (solaro2024emergingconceptsof pages 1-2, gregorich2024mechanismsofrbm20 pages 1-3, newman2024dilatedcardiomyopathya pages 7-8) |
| **Gene** | *MYH7* (HGNC:7577) | **Myosin Heavy Chain 7**: Sarcomere motor protein. Variants alter contractile force generation; high penetrance (~90% by age 60); associated with LV noncompaction overlap. | (arnautu2024geneticsandmolecular pages 5-7, newman2024dilatedcardiomyopathya pages 13-14) |
| **Gene** | *FLNC* (HGNC:3754) | **Filamin C**: Cytoskeletal crosslinker. Truncations linked to high arrhythmic risk (ventricular arrhythmias) and fibrosis, even with mild LV dysfunction. | (arnautu2024geneticsandmolecular pages 5-7, arnautu2024geneticsandmolecular pages 7-8, newman2024dilatedcardiomyopathya pages 13-14) |
| **Gene** | *DSP* (HGNC:3052) | **Desmoplakin**: Desmosomal plaque protein. Variants impair cell-cell adhesion; found in ~13% of end-stage DCM/transplant cases; overlap with arrhythmogenic cardiomyopathy. | (arnautu2024geneticsandmolecular pages 5-7, arnautu2024geneticsandmolecular pages 7-8) |
| **Gene** | *BAG3* (HGNC:937) | **BAG Cochaperone 3**: Chaperone involved in protein quality control/autophagy. Variants cause rapid progression and high penetrance (>80% by age 40). | (arnautu2024geneticsandmolecular pages 5-7, newman2024dilatedcardiomyopathya pages 13-14) |
| **Cell Type** | Cardiomyocyte (CL:0000746) | Primary affected cell type; central to GWAS enrichment signals; site of sarcomere/nuclear/splicing defects leading to contractile failure. | (jurgens2024genomewideassociationstudy pages 1-2, malinow2024pediatricdilatedcardiomyopathy pages 1-2) |
| **Cell Type** | T cell (CL:0000084) | Immune infiltration (CD3+, CD4+, CD8+) observed in inflammatory DCM/myocarditis; exhausted/cytotoxic subtypes identified by single-cell sequencing. | (vicenzetto2024theroleof pages 1-2, xu2024constructionandevaluation pages 1-2) |
| **Anatomy** | Left Ventricle (UBERON:0002084) | Site of primary phenotype: dilation and reduced systolic function (LVEF); remodeling correlates with genetic drivers. | (zheng2024genomewideassociationanalysis pages 10-11, eichhorn2024riskstratificationin pages 1-2) |
| **Process** | Sarcomere Organization (GO:0045214) | Disrupted by *TTN*, *MYH7*, *TNNT2* variants; leads to impaired tension generation and faulty mechanotransduction. | (solaro2024emergingconceptsof pages 1-2, kellermayer2024truncatedtitinis pages 1-2, kellermayer2024truncatedtitinis pages 6-7) |
| **Process** | Alternative Splicing (GO:0000380) | Dysregulated by *RBM20* defects; affects protein isoforms determining myocardial stiffness (*TTN*) and excitation-contraction coupling. | (gregorich2024mechanismsofrbm20 pages 1-3, newman2024dilatedcardiomyopathya pages 7-8) |
| **Component**| Nuclear Lamina (GO:0005652) | Structural support for nucleus; compromised by *LMNA* mutations leading to nuclear fragility and altered gene expression. | (arnautu2024geneticsandmolecular pages 3-5, newman2024dilatedcardiomyopathya pages 4-6) |
| **Component**| Sarcoplasm (GO:0016528) | Site of mutant *RBM20* accumulation into biomolecular condensates (processing bodies/granules), interfering with normal physiology. | (gregorich2024mechanismsofrbm20 pages 1-3) |
| **Chemical** | Calcium Ion (CHEBI:29108) | Intracellular handling disrupted by *PLN* and *RBM20*-spliced targets (*CACNA1C*, *CAMK2D*); central to arrhythmia mechanism. | (arnautu2024geneticsandmolecular pages 5-7, newman2024dilatedcardiomyopathya pages 7-8) |
| **Chemical** | Gadolinium (CHEBI:37402) | Contrast agent for CMR. Late Gadolinium Enhancement (LGE) marks fibrosis; predicts mortality (HR 1.81) and arrhythmic events (HR 2.69). | (eichhorn2024riskstratificationin pages 1-2) |


*Table: A structured overview of major genes, cell types, anatomical structures, and processes implicated in DCM pathophysiology, mapped to ontology categories and supported by recent evidence.*

---

## Evidence items (PMID-first requirement: limitation note)
The retrieved full-text excerpts used in this run primarily exposed **DOIs and URLs** but did **not consistently include PMIDs** in the extracted snippets for the key 2023–2024 mechanistic papers (e.g., JCI 2024 TTNtv; JAMA 2024 CMR meta-analysis; Nature Genetics 2024 GWAS; Circ Genom Precis Med 2024 RBM20). Therefore, the report provides **publication dates and DOIs/URLs** from the retrieved sources, while citing mechanistic claims using the context evidence IDs above. (kellermayer2024truncatedtitinis pages 1-2, eichhorn2024riskstratificationin pages 1-2, gregorich2024mechanismsofrbm20 pages 1-3, jurgens2024genomewideassociationstudy pages 1-2, zheng2024genomewideassociationanalysis pages 10-11)

---

## Source URLs and publication dates (2023–2024 priority)
- Eldemire et al. **Genetics of Dilated Cardiomyopathy**. *Annual Review of Medicine*. **Published Jan 29, 2024**. https://doi.org/10.1146/annurev-med-052422-020535 (eldemire2024geneticsofdilated pages 1-3)
- Kellermayer et al. **Truncated titin is structurally integrated into the human dilated cardiomyopathic sarcomere**. *J Clin Invest*. **Published Jan 16, 2024**. https://doi.org/10.1172/JCI169753 (kellermayer2024truncatedtitinis pages 1-2)
- Gregorich et al. **Mechanisms of RBM20 Cardiomyopathy**. *Circ Genom Precis Med*. **Feb 2024 issue (manuscript indicates Jan 2024 availability)**. https://doi.org/10.1161/CIRCGEN.123.004355 (gregorich2024mechanismsofrbm20 pages 1-3)
- Eichhorn et al. **Risk Stratification in Nonischemic Dilated Cardiomyopathy Using CMR Imaging**. *JAMA*. **Published online Sep 19, 2024**. https://doi.org/10.1001/jama.2024.13946 (eichhorn2024riskstratificationin pages 1-2)
- Jurgens et al. **GWAS reveals mechanisms underlying DCM and myocardial resilience**. *Nature Genetics*. **Nov 2024**. https://doi.org/10.1038/s41588-024-01975-5 (jurgens2024genomewideassociationstudy pages 1-2)
- Zheng et al. **GWAS analysis provides insights into the molecular etiology of DCM**. *Nature Genetics*. **Nov 2024**. https://doi.org/10.1038/s41588-024-01952-y (zheng2024genomewideassociationanalysis pages 10-11)
- Xu et al. **Immune-related diagnostic model in idiopathic DCM HF**. *BMC Cardiovascular Disorders*. **Feb 2024**. https://doi.org/10.1186/s12872-023-03666-1 (xu2024constructionandevaluation pages 1-2)
- Vicenzetto et al. **Immune system in myocarditis pathobiology/therapy**. *Biomedicines*. **Published May 23, 2024**. https://doi.org/10.3390/biomedicines12061156 (vicenzetto2024theroleof pages 1-2)
- Solaro et al. **Mechanisms controlling cardiac tension in familial DCM**. *Biomedicines*. **May 2024**. https://doi.org/10.3390/biomedicines12050999 (solaro2024emergingconceptsof pages 1-2)
- Malinow et al. **Pediatric DCM pathogenesis review**. *Frontiers in Pediatrics*. **Jun 19, 2024**. https://doi.org/10.3389/fped.2024.1404942 (malinow2024pediatricdilatedcardiomyopathy pages 1-2)


References

1. (arnautu2024geneticsandmolecular pages 5-7): Diana-Aurora Arnautu, Octavian-Marius Cretu, Daniel Florin Lighezan, Minodora Andor, Ioana Citu, Dragoș Cozma, Brenda-Cristiana Bernad, Adrian-Pavel Trifa, Diana Lighezan, Elena-Silvia Bernad, Dragos Catalin Jianu, Cristian Oancea, Ioan-Radu Lala, Sergiu-Florin Arnautu, and Mirela-Cleopatra Tomescu. Genetics and molecular mechanisms of idiopathic dilated cardiomyopathy, a possible guide to individualized management. Apr 2024. URL: https://doi.org/10.20944/preprints202404.1054.v1, doi:10.20944/preprints202404.1054.v1.

2. (eichhorn2024riskstratificationin pages 1-2): Christian Eichhorn, David Koeckerling, Rohin K Reddy, Maddalena Ardissino, Marek Rogowski, Bernadette Coles, Lukas Hunziker, Simon Greulich, Isaac Shiri, Norbert Frey, Jens Eckstein, Stephan Windecker, Raymond Y Kwong, George C M Siontis, and Christoph Gräni. Risk stratification in nonischemic dilated cardiomyopathy using cmr imaging: a systematic review and meta-analysis. JAMA, Sep 2024. URL: https://doi.org/10.1001/jama.2024.13946, doi:10.1001/jama.2024.13946. This article has 34 citations.

3. (eldemire2024geneticsofdilated pages 1-3): Ramone Eldemire, Luisa Mestroni, and Matthew R.G. Taylor. Genetics of dilated cardiomyopathy. Annual Review of Medicine, 75:417-426, Jan 2024. URL: https://doi.org/10.1146/annurev-med-052422-020535, doi:10.1146/annurev-med-052422-020535. This article has 57 citations and is from a domain leading peer-reviewed journal.

4. (newman2024dilatedcardiomyopathya pages 1-2): Noah A. Newman and Michael A. Burke. Dilated cardiomyopathy: a genetic journey from past to future. International Journal of Molecular Sciences, 25:11460, Oct 2024. URL: https://doi.org/10.3390/ijms252111460, doi:10.3390/ijms252111460. This article has 19 citations.

5. (solaro2024emergingconceptsof pages 1-2): R. Solaro, Paul Goldspink, and Beata Wolska. Emerging concepts of mechanisms controlling cardiac tension: focus on familial dilated cardiomyopathy (dcm) and sarcomere-directed therapies. Biomedicines, 12:999, May 2024. URL: https://doi.org/10.3390/biomedicines12050999, doi:10.3390/biomedicines12050999. This article has 5 citations.

6. (kellermayer2024truncatedtitinis pages 1-2): Dalma Kellermayer, Hedvig Tordai, Balázs Kiss, György Török, Dániel M. Péter, Alex Ali Sayour, Miklós Pólos, István Hartyánszky, Bálint Szilveszter, Siegfried Labeit, Ambrus Gángó, Gábor Bedics, Csaba Bödör, Tamás Radovits, Béla Merkely, and Miklós S.Z. Kellermayer. Truncated titin is structurally integrated into the human dilated cardiomyopathic sarcomere. Journal of Clinical Investigation, Jan 2024. URL: https://doi.org/10.1172/jci169753, doi:10.1172/jci169753. This article has 26 citations and is from a highest quality peer-reviewed journal.

7. (kellermayer2024truncatedtitinis media 0d428a5a): Dalma Kellermayer, Hedvig Tordai, Balázs Kiss, György Török, Dániel M. Péter, Alex Ali Sayour, Miklós Pólos, István Hartyánszky, Bálint Szilveszter, Siegfried Labeit, Ambrus Gángó, Gábor Bedics, Csaba Bödör, Tamás Radovits, Béla Merkely, and Miklós S.Z. Kellermayer. Truncated titin is structurally integrated into the human dilated cardiomyopathic sarcomere. Journal of Clinical Investigation, Jan 2024. URL: https://doi.org/10.1172/jci169753, doi:10.1172/jci169753. This article has 26 citations and is from a highest quality peer-reviewed journal.

8. (kellermayer2024truncatedtitinis media 3e1be5e2): Dalma Kellermayer, Hedvig Tordai, Balázs Kiss, György Török, Dániel M. Péter, Alex Ali Sayour, Miklós Pólos, István Hartyánszky, Bálint Szilveszter, Siegfried Labeit, Ambrus Gángó, Gábor Bedics, Csaba Bödör, Tamás Radovits, Béla Merkely, and Miklós S.Z. Kellermayer. Truncated titin is structurally integrated into the human dilated cardiomyopathic sarcomere. Journal of Clinical Investigation, Jan 2024. URL: https://doi.org/10.1172/jci169753, doi:10.1172/jci169753. This article has 26 citations and is from a highest quality peer-reviewed journal.

9. (gregorich2024mechanismsofrbm20 pages 1-3): Zachery R. Gregorich, Yanghai Zhang, Timothy J. Kamp, Henk L. Granzier, and Wei Guo. Mechanisms of rbm20 cardiomyopathy: insights from model systems. Circulation: Genomic and Precision Medicine, Feb 2024. URL: https://doi.org/10.1161/circgen.123.004355, doi:10.1161/circgen.123.004355. This article has 21 citations.

10. (newman2024dilatedcardiomyopathya pages 7-8): Noah A. Newman and Michael A. Burke. Dilated cardiomyopathy: a genetic journey from past to future. International Journal of Molecular Sciences, 25:11460, Oct 2024. URL: https://doi.org/10.3390/ijms252111460, doi:10.3390/ijms252111460. This article has 19 citations.

11. (newman2024dilatedcardiomyopathya pages 13-14): Noah A. Newman and Michael A. Burke. Dilated cardiomyopathy: a genetic journey from past to future. International Journal of Molecular Sciences, 25:11460, Oct 2024. URL: https://doi.org/10.3390/ijms252111460, doi:10.3390/ijms252111460. This article has 19 citations.

12. (xu2024constructionandevaluation pages 1-2): Sichi Xu, Zhaogui Wu, and Haihua Chen. Construction and evaluation of immune-related diagnostic model in patients with heart failure caused by idiopathic dilated cardiomyopathy. BMC Cardiovascular Disorders, Feb 2024. URL: https://doi.org/10.1186/s12872-023-03666-1, doi:10.1186/s12872-023-03666-1. This article has 6 citations and is from a peer-reviewed journal.

13. (vicenzetto2024theroleof pages 1-2): Cristina Vicenzetto, Andrea Giordani, Caterina Menghi, Anna Baritussio, Maria Peloso Cattini, Elena Pontara, Elisa Bison, Stefania Rizzo, Monica De Gaspari, Cristina Basso, Gaetano Thiene, Sabino Iliceto, Renzo Marcolongo, and Alida Caforio. The role of the immune system in pathobiology and therapy of myocarditis: a review. Biomedicines, 12:1156, May 2024. URL: https://doi.org/10.3390/biomedicines12061156, doi:10.3390/biomedicines12061156. This article has 13 citations.

14. (jurgens2024genomewideassociationstudy pages 1-2): S. Jurgens, Joel T. Rämö, D. Kramarenko, L. Wijdeveld, Jan Haas, M. Chaffin, S. Garnier, L. Gaziano, L. Weng, Alex Lipov, S. Zheng, Albert Henry, J. Huffman, Saketh Challa, Frank Rühle, Carmen Diaz Verdugo, C. Krijger Juárez, Shinwan Kany, C. A. van Orsouw, K. Biddinger, Edwin Poel, Amanda L Elliott, Xin Wang, C. Francis, Richard Ruan, Satoshi Koyama, L. Beekman, Dominic S Zimmerman, J. Deleuze, E. Villard, D. Trégouët, Richard Isnard, Joel T. Amanda L. Juha Teemu Jari Aarno Mark Rämö Elliott Sinisalo Niiranen Laukkanen Palotie D, J. Sinisalo, T. Niiranen, J. Laukkanen, A. Palotie, Mark Daly, Jennifer E. Kyong-Mi Philip S. Krishna G. Huffman Chang Tsao Aragam, Kyong-Mi Chang, Phil Tsao, Krishna G. Aragam, Sean L. Albert Kiran James S. R. Thomas Patrick T. Kris Zheng Henry Biddinger Ware Lumbers Ellinor Aragam, James S. Ware, R. Lumbers, P. Ellinor, D. Boomsma, E. D. de Geus, R. Tadros, Y. Pinto, A. Wilde, J. Hottenga, Roddy Walsh, A. F. Schmidt, Seung Hoan Choi, P. Matthews, S. N. van der Crabben, Ahmad S. Amin, P. Charron, Benjamin Meder, and C. Bezzina. Genome-wide association study reveals mechanisms underlying dilated cardiomyopathy and myocardial resilience. Nature Genetics, 56:2636-2645, Nov 2024. URL: https://doi.org/10.1038/s41588-024-01975-5, doi:10.1038/s41588-024-01975-5. This article has 42 citations and is from a highest quality peer-reviewed journal.

15. (zheng2024genomewideassociationanalysis pages 10-11): Sean L. Zheng, Albert Henry, Douglas Cannie, Michael Lee, David Miller, Kathryn A. McGurk, Isabelle Bond, Xiao Xu, Hanane Issa, Catherine Francis, Antonio De Marvao, Pantazis I. Theotokis, Rachel J. Buchan, Doug Speed, Erik Abner, Lance Adams, Krishna G. Aragam, Johan Ärnlöv, Anna Axelsson Raja, Joshua D. Backman, John Baksi, Paul J. R. Barton, Kiran J. Biddinger, Eric Boersma, Jeffrey Brandimarto, Søren Brunak, Henning Bundgaard, David J. Carey, Philippe Charron, James P. Cook, Stuart A. Cook, Spiros Denaxas, Jean-François Deleuze, Alexander S. Doney, Perry Elliott, Christian Erikstrup, Tõnu Esko, Eric H. Farber-Eger, Chris Finan, Sophie Garnier, Jonas Ghouse, Vilmantas Giedraitis, Daniel F. Guðbjartsson, Christopher M. Haggerty, Brian P. Halliday, Anna Helgadottir, Harry Hemingway, Hans L. Hillege, Isabella Kardys, Lars Lind, Cecilia M. Lindgren, Brandon D. Lowery, Charlotte Manisty, Kenneth B. Margulies, James C. Moon, Ify R. Mordi, Michael P. Morley, Andrew D. Morris, Andrew P. Morris, Lori Morton, Mahdad Noursadeghi, Sisse R. Ostrowski, Anjali T. Owens, Colin N. A. Palmer, Antonis Pantazis, Ole B. V. Pedersen, Sanjay K. Prasad, Akshay Shekhar, Diane T. Smelser, Sundararajan Srinivasan, Kari Stefansson, Garðar Sveinbjörnsson, Petros Syrris, Mari-Liis Tammesoo, Upasana Tayal, Maris Teder-Laving, Guðmundur Thorgeirsson, Unnur Thorsteinsdottir, Vinicius Tragante, David-Alexandre Trégouët, Thomas A. Treibel, Henrik Ullum, Ana M. Valdes, Jessica van Setten, Marion van Vugt, Abirami Veluchamy, W. M. Monique Verschuren, Eric Villard, Yifan Yang, Mahdad Noursadeghi, Ole B. V. Pedersen, Kari Stefansson, Unnur Thorsteinsdottir, Henrik Ullum, Folkert W. Asselbergs, Antonio De Marvao, Marie-Pierre Dube, Michael E. Dunn, Patrick T. Ellinor, Sophie Garnier, Chim C. Lang, Andrew P. Morris, Lori Morton, Colin N. A. Palmer, Nilesh J. Samani, Svati H. Shah, Akshay Shekhar, J. Gustav Smith, Sundarajan Srinivasan, Guðmundur Thorgeirsson, Ramachandran S. Vasan, Jessica van Setten, Marion van Vugt, Abirami Veluchamy, W. M. Monique Verschuuren, Eric Villard, Quinn Wells, Folkert W. Asselbergs, Thomas P. Cappola, Marie-Pierre Dube, Michael E. Dunn, Patrick T. Ellinor, Aroon D. Hingorani, Chim C. Lang, Nilesh J. Samani, Svati H. Shah, J. Gustav Smith, Ramachandran S. Vasan, Declan P. O’Regan, Hilma Holm, Michela Noseda, Quinn Wells, James S. Ware, and R. Thomas Lumbers. Genome-wide association analysis provides insights into the molecular etiology of dilated cardiomyopathy. Nature Genetics, 56:2646-2658, Nov 2024. URL: https://doi.org/10.1038/s41588-024-01952-y, doi:10.1038/s41588-024-01952-y. This article has 46 citations and is from a highest quality peer-reviewed journal.

16. (newman2024dilatedcardiomyopathya pages 4-6): Noah A. Newman and Michael A. Burke. Dilated cardiomyopathy: a genetic journey from past to future. International Journal of Molecular Sciences, 25:11460, Oct 2024. URL: https://doi.org/10.3390/ijms252111460, doi:10.3390/ijms252111460. This article has 19 citations.

17. (malinow2024pediatricdilatedcardiomyopathy pages 1-2): Ian Malinow, Daniel C. Fong, Matthew Miyamoto, Sarah Badran, and Charles C. Hong. Pediatric dilated cardiomyopathy: a review of current clinical approaches and pathogenesis. Frontiers in Pediatrics, Jun 2024. URL: https://doi.org/10.3389/fped.2024.1404942, doi:10.3389/fped.2024.1404942. This article has 23 citations.

18. (eldemire2024geneticsofdilated pages 3-5): Ramone Eldemire, Luisa Mestroni, and Matthew R.G. Taylor. Genetics of dilated cardiomyopathy. Annual Review of Medicine, 75:417-426, Jan 2024. URL: https://doi.org/10.1146/annurev-med-052422-020535, doi:10.1146/annurev-med-052422-020535. This article has 57 citations and is from a domain leading peer-reviewed journal.

19. (newman2024dilatedcardiomyopathya pages 14-17): Noah A. Newman and Michael A. Burke. Dilated cardiomyopathy: a genetic journey from past to future. International Journal of Molecular Sciences, 25:11460, Oct 2024. URL: https://doi.org/10.3390/ijms252111460, doi:10.3390/ijms252111460. This article has 19 citations.

20. (kellermayer2024truncatedtitinis pages 6-7): Dalma Kellermayer, Hedvig Tordai, Balázs Kiss, György Török, Dániel M. Péter, Alex Ali Sayour, Miklós Pólos, István Hartyánszky, Bálint Szilveszter, Siegfried Labeit, Ambrus Gángó, Gábor Bedics, Csaba Bödör, Tamás Radovits, Béla Merkely, and Miklós S.Z. Kellermayer. Truncated titin is structurally integrated into the human dilated cardiomyopathic sarcomere. Journal of Clinical Investigation, Jan 2024. URL: https://doi.org/10.1172/jci169753, doi:10.1172/jci169753. This article has 26 citations and is from a highest quality peer-reviewed journal.

21. (arnautu2024geneticsandmolecular pages 7-8): Diana-Aurora Arnautu, Octavian-Marius Cretu, Daniel Florin Lighezan, Minodora Andor, Ioana Citu, Dragoș Cozma, Brenda-Cristiana Bernad, Adrian-Pavel Trifa, Diana Lighezan, Elena-Silvia Bernad, Dragos Catalin Jianu, Cristian Oancea, Ioan-Radu Lala, Sergiu-Florin Arnautu, and Mirela-Cleopatra Tomescu. Genetics and molecular mechanisms of idiopathic dilated cardiomyopathy, a possible guide to individualized management. Apr 2024. URL: https://doi.org/10.20944/preprints202404.1054.v1, doi:10.20944/preprints202404.1054.v1.

22. (arnautu2024geneticsandmolecular pages 3-5): Diana-Aurora Arnautu, Octavian-Marius Cretu, Daniel Florin Lighezan, Minodora Andor, Ioana Citu, Dragoș Cozma, Brenda-Cristiana Bernad, Adrian-Pavel Trifa, Diana Lighezan, Elena-Silvia Bernad, Dragos Catalin Jianu, Cristian Oancea, Ioan-Radu Lala, Sergiu-Florin Arnautu, and Mirela-Cleopatra Tomescu. Genetics and molecular mechanisms of idiopathic dilated cardiomyopathy, a possible guide to individualized management. Apr 2024. URL: https://doi.org/10.20944/preprints202404.1054.v1, doi:10.20944/preprints202404.1054.v1.