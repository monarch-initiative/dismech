---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-06T03:52:46.705805'
end_time: '2026-03-06T04:10:12.680494'
duration_seconds: 1045.97
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Multiple Myeloma
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Multiple Myeloma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Multiple Myeloma**.
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
- **Disease Name:** Multiple Myeloma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Multiple Myeloma**.
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


# Multiple Myeloma (MM) Pathophysiology — Comprehensive Research Report (2023–2024 emphasis)

## 0. Disease identifiers and scope
**Disease:** Multiple Myeloma (MM) — malignant plasma cell neoplasm primarily residing in the **bone marrow** with systemic end-organ damage. (moscvin2023dissectingmolecularmechanisms pages 1-3, bhowmick2024pathwaystotherapy pages 1-3)

**MONDO ID:** Not retrieved in the provided evidence; Open Targets disease identifier returned was **EFO_0001378** (“multiple myeloma”). ()

**Precursor conditions:** **Monoclonal gammopathy of undetermined significance (MGUS)** and **Smoldering multiple myeloma (SMM)** are clinically recognized antecedent states. (kansal2024towardprecisionmedicine pages 2-3, moscvin2023dissectingmolecularmechanisms pages 1-3, liotti2024investigationonthe pages 9-13)

---

## 1. Key concepts and definitions (current understanding)

### 1.1 Core definition
Multiple myeloma is characterized by clonal expansion of malignant plasma cells in the bone marrow and is clinically defined by myeloma-defining events and/or end-organ damage (classically “CRAB”: hyperCalcemia, Renal failure, Anemia, Bone lesions). (liotti2024investigationonthe pages 9-13, moscvin2023dissectingmolecularmechanisms pages 1-3)

### 1.2 Multi-step evolution model
MM is widely described as a **multi-step disease** evolving from MGUS → SMM → symptomatic MM → more aggressive forms (including extramedullary disease/plasma cell leukemia), with increasing genomic complexity and microenvironmental remodeling over time. (liotti2024investigationonthe pages 9-13, gong2024novelinsightsinto pages 10-12)

### 1.3 Diagnostic/progression-defining biomarkers (SLiM-CRAB)
Recent clinical models incorporate **myeloma-defining biomarkers** (SLiM-CRAB) that predict near-term progression and justify treatment initiation.
* **Bone marrow plasmacytosis ≥60%** is associated with rapid progression. (kansal2024towardprecisionmedicine pages 2-3)
* **Serum free light chain (FLC) ratio** thresholds (e.g., FLC >100 associated with ~79% progression) are used as high-risk markers. (kansal2024towardprecisionmedicine pages 2-3)
* **>1 focal lesion on whole-body MRI** predicts progression. (kansal2024towardprecisionmedicine pages 2-3)

---

## 2. Core pathophysiology (molecular/cellular mechanisms)

MM pathophysiology emerges from the convergence of (i) intrinsic tumor genomic/epigenomic programs and (ii) an extrinsic **bone marrow niche** that supplies survival cues, immune escape, and therapy resistance.

### 2.1 Primary genomic events and clonal evolution
Primary initiating events often involve **hyperdiploidy** or **IgH locus translocations** (14q32) that juxtapose oncogenes to immunoglobulin enhancers; these primary events are detectable already in precursor states. (lemonakis2024factorsaffectingprognosis pages 24-28, kansal2024towardprecisionmedicine pages 2-3, liotti2024investigationonthe pages 9-13)

Progression is associated with accumulation of secondary hits (copy-number alterations, mutations, epigenetic changes) and selection of resistant subclones, especially under treatment pressure; chemotherapy can contribute a substantial fraction of nonsynonymous mutations and relapse may arise from a surviving propagating cell. (gong2024novelinsightsinto pages 10-12)

### 2.2 Dysregulated signaling pathways
#### (a) RAS/MAPK pathway
**KRAS/NRAS/BRAF** alterations are common, and a 2024 synthesis reports **RAS mutations present in ~50% of MM patients**, consistent with MAPK pathway dependence in many cases. (ram2024thegeneticand pages 25-26)

#### (b) NF-κB (non-canonical) and oncogenic chromatin wiring
A 2024 mechanistic study demonstrates that constitutive **non-canonical NF-κB** signaling via **p52 (NFKB2)** reprograms the MM epigenome: p52 binds and activates typical enhancers/super-enhancers, reshaping 3D enhancer–promoter interactions and sustaining expression of myeloma dependency genes (e.g., **BCL2, IL6ST, RGS1**). (ang2024aberrantnoncanonicalnfκb pages 7-8)

#### (c) TP53 pathway disruption and aggressive biology
In a 2024 review of genetic drivers in relapsed/refractory MM, **TP53 pathway inactivation** is reported in **~45%** of patients in the summarized cohort(s), with complex “double-hit” contexts (e.g., 17p LOH with 1q alterations) emerging during progression. (ram2024thegeneticand pages 20-22)

#### (d) Proteostasis/UPR and stress adaptation
Myeloma cells face extreme secretory stress; proteostasis adaptation (including heat shock programs) is implicated in relapse biology and in resistance, including links between NF-κB activation and proteasome inhibitor resistance. (ram2024thegeneticand pages 20-22)

### 2.3 Bone marrow microenvironment (BMME) as a driver of survival and resistance
The BMME supplies growth factors, adhesion-mediated signaling, and immune suppression.

A 2024 review explicitly frames microenvironmental “sheltering” and notes elevated stromal-derived growth factors (e.g., **SCF, VEGF, IL-6**) in MM marrow niches. (bhowmick2024pathwaystotherapy pages 1-3)

**Environment-mediated drug resistance (EMDR)** is reinforced by spatial proximity to stromal/bone compartments and bone-derived factors. A 2024 hybrid modeling + in vivo validation study supports a mechanism where bone microenvironment protection increases the probability and heterogeneity of resistant clones during therapy. (bishop2024theboneecosystem media ec296c58, bishop2024theboneecosystem media ea2ecb8d)

### 2.4 Immune microenvironment dysfunction and immune escape
Immune alterations begin early and evolve toward an immune-tolerant marrow environment.

A 2023 review states that innate and adaptive effectors “**show marked dysfunction and skewing towards a tolerant environment that favors disease progression**,” with increased MDSCs and M2-like macrophages and lymphoid skewing toward Th17/Treg with inhibition of cytotoxic/effector T cells. (moscvin2023dissectingmolecularmechanisms pages 1-3)

Quantitative immune profiling (CyTOF/multi-omics) supports early and stage-specific shifts:
* **HLA-DR is reduced** in CD16+ monocytes and plasmacytoid dendritic cells, with dendritic-cell stress/immune-response programs downregulated. (cheng2024multiomicsrevealimmune pages 1-2)
* CyTOF-reported changes include **65% decrease of immature granulocytes in MGUS vs normal BM**, **53% decrease of pDCs in SMM** (and 51% in NDMM), and **increases in CD16+ monocytes** of 5.6-fold (MGUS), 2.0-fold (SMM), and 1.6-fold (NDMM). (cheng2024multiomicsrevealimmune pages 1-2)

In rapid-progressing MM, single-cell RNA-seq showed significantly higher enrichment of **exhausted CD8+ T cells (GZMK+, TIGIT+)** with **P = 0.022**, along with decreased cytolytic gene expression (PRF1, GZMB, GNLY), and a higher ratio of exhausted T cells (P = 0.049). (pilcher2023crosscentersinglecell pages 1-2)

Expert analysis emphasizes that immune status and spatial contexture influence outcomes of modern immunotherapies (CAR-T, bispecifics), and proposes distinct “spatial immune types” (immune depleted/permissive/excluded/suppressed/resistant) to guide patient selection. (dhodapkar2024immunestatusand pages 2-3)

---

## 3. Key molecular players (genes/proteins, chemicals, cell types, anatomy)

### 3.1 Genes/proteins implicated in progression and phenotype generation
Key categories supported by recent evidence include:
* **MAPK drivers:** KRAS/NRAS/BRAF. (ram2024thegeneticand pages 25-26)
* **Non-canonical NF-κB chromatin drivers:** NFKB2 (p52) and associated regulators (e.g., TRAF3/CYLD context in broader genomic models). (ang2024aberrantnoncanonicalnfκb pages 7-8, ram2024thegeneticand pages 22-23)
* **Tumor suppressor disruption:** TP53 pathway inactivation enriched in advanced disease. (ram2024thegeneticand pages 20-22)
* **Bone disease mediators:** FLT3L/STAT3/DKK1; CCL3/HMGB1/RANKL; MMP13/VSIR (PD-1H/VISTA). (shin2024elucidationofmolecular pages 1-2, anloague2024anovelccl3hmgb1 pages 13-14, fu2023thecheckpointinhibitor pages 1-2)

### 3.2 Chemical entities and cytokines (ChEBI-style labels in text)
Supported mediators include **IL-6**, **VEGF**, **CXCL12/SDF-1**, **RANKL**, and WNT antagonists such as **DKK1**, plus inflammatory mediators (IL-1β, TNF-α, MIP-1α/CCL3). (bhowmick2024pathwaystotherapy pages 1-3, shin2024elucidationofmolecular pages 1-2)

### 3.3 Cell types (CL-style labels)
Prominent involved cell types include:
* **Bone marrow plasma cells** (malignant clone). (moscvin2023dissectingmolecularmechanisms pages 1-3, bhowmick2024pathwaystotherapy pages 1-3)
* **Mesenchymal stromal cells (MSCs)** as niche architects with impaired osteogenic and hematopoietic support functions. (bogun2024stromalalterationsin pages 1-2, bogun2024stromalalterationsin pages 11-12)
* **Osteoclasts / osteocytes / osteoblast-lineage cells** mediating bone remodeling imbalance. (fu2023thecheckpointinhibitor pages 1-2, anloague2024anovelccl3hmgb1 pages 13-14, shin2024elucidationofmolecular pages 1-2)
* **CD8+ T cells, NK cells, monocytes/DCs**, and suppressor populations such as **MDSCs** and **Tregs**. (pilcher2023crosscentersinglecell pages 1-2, cheng2024multiomicsrevealimmune pages 1-2, moscvin2023dissectingmolecularmechanisms pages 1-3)

### 3.4 Anatomical locations (UBERON-style labels)
The central site is **bone marrow**, with major pathological consequences in **bone** (osteolytic disease). (moscvin2023dissectingmolecularmechanisms pages 1-3, shin2024elucidationofmolecular pages 1-2)

---

## 4. Biological processes disrupted (GO-style biological processes)
Evidence-supported disrupted biological processes include:

* **Non-canonical NF-κB signaling and chromatin regulation** (enhancer activation/super-enhancer formation; altered enhancer–promoter looping). (ang2024aberrantnoncanonicalnfκb pages 7-8)
* **MAPK cascade / cell proliferation signaling** (RAS/MAPK activation). (ram2024thegeneticand pages 25-26)
* **Immune evasion and T-cell exhaustion** (TIGIT+ exhausted CD8 T cells; impaired antigen presentation via HLA-DR reduction). (pilcher2023crosscentersinglecell pages 1-2, cheng2024multiomicsrevealimmune pages 1-2)
* **Bone remodeling imbalance**: increased osteoclastogenesis/bone resorption and impaired osteoblast-mediated bone formation (via DKK1/WNT suppression; RANKL upregulation). (shin2024elucidationofmolecular pages 1-2, anloague2024anovelccl3hmgb1 pages 13-14)
* **Stromal senescence and niche dysfunction** with BMP/TGF pathway dysregulation, reduced osteogenesis and reduced hematopoietic support. (bogun2024stromalalterationsin pages 1-2, bogun2024stromalalterationsin pages 11-12)

---

## 5. Cellular components (GO-style cellular component)
Mechanisms operate across:

* **Nucleus/chromatin** (p52-driven enhancer activation and 3D chromatin interactions). (ang2024aberrantnoncanonicalnfκb pages 7-8)
* **Plasma membrane / cell–cell contact** (immune checkpoints; osteoclast receptor PD-1H/VSIR binding MMP-13). (fu2023thecheckpointinhibitor pages 1-2, dhodapkar2024immunestatusand pages 2-3)
* **Extracellular space** (cytokines IL-6/VEGF/CXCL12; FLT3L; HMGB1; RANKL). (bhowmick2024pathwaystotherapy pages 1-3, shin2024elucidationofmolecular pages 1-2, anloague2024anovelccl3hmgb1 pages 13-14)

---

## 6. Disease progression: sequence of events and phases

### 6.1 From precursor states to symptomatic disease
MGUS and SMM are clinically defined precursor states that can progress to MM. (liotti2024investigationonthe pages 9-13, moscvin2023dissectingmolecularmechanisms pages 1-3)

Evidence-supported progression risk statistics:
* MGUS: approximately **~1% annual progression risk** to malignancy. (liotti2024investigationonthe pages 9-13, barakat2023investigatingtcell pages 14-17)
* SMM: approximately **~10% per year for the first 5 years**, then **3% for the next 5**, then **~1% thereafter** (reviewed summary). (liotti2024investigationonthe pages 9-13)

### 6.2 Microenvironmental remodeling during progression
Stromal alterations are “already imprinted” at asymptomatic stages and become more pronounced across MGUS → SMM → MM, including BMP/TGF signaling perturbations, senescence, reduced osteogenesis, and impaired hematopoietic support. (bogun2024stromalalterationsin pages 1-2, bogun2024stromalalterationsin pages 11-12)

Immune remodeling begins early: antigen presentation defects and skewing toward immunosuppressive/exhausted states are detectable in MGUS and evolve with progression. (cheng2024multiomicsrevealimmune pages 1-2, moscvin2023dissectingmolecularmechanisms pages 11-13)

---

## 7. Phenotypic manifestations and mechanistic links

### 7.1 Bone disease (osteolysis)
Bone disease arises from increased osteoclast activity and impaired osteoblast function. (shin2024elucidationofmolecular pages 1-2)

Recent mechanistic advances include:
* **FLT3L→STAT3(pY705)→DKK1**, with DKK1 inhibiting WNT signaling and nuclear β-catenin translocation, suppressing osteoblast-mediated bone formation; FLT3L is higher in MM than AML/ALL and higher in MM with bone lesions. (Haematologica, Jan 2024; https://doi.org/10.3324/haematol.2023.283784). (shin2024elucidationofmolecular pages 1-2, shin2024elucidationofmolecular pages 2-3)
* **CCL3 induces osteocyte RANKL upregulation**, and CCL3 triggers osteocyte **HMGB1 release** which “may act as a propagating pro-osteoclastogenic signal in neighboring osteocytes.” (Haematologica, Nov 2024; https://doi.org/10.3324/haematol.2024.286484). (anloague2024anovelccl3hmgb1 pages 13-14)
* **MMP-13/PD-1H (VISTA/VSIR) axis in osteoclasts:** PD-1H is identified as the receptor for MMP-13, enabling enhanced osteoclast fusion and sealing-zone formation; PD-1H deficiency attenuates myeloma-induced bone destruction in vivo. (Nature Communications, Jul 2023; https://doi.org/10.1038/s41467-023-39769-8). (fu2023thecheckpointinhibitor pages 1-2)

Real-world implementation: antiresorptive agents are discussed, including bisphosphonates (pamidronate/zoledronate) and **denosumab (RANKL inhibitor)**, with awareness of complications such as BRONJ. (shin2024elucidationofmolecular pages 9-10)

### 7.2 Renal involvement and light-chain toxicity
MM plasma cells produce monoclonal immunoglobulins and free light chains; excess FLC can cause **renal failure**, and FLC ratios are used for progression risk stratification. (liotti2024investigationonthe pages 9-13, kansal2024towardprecisionmedicine pages 2-3)

### 7.3 Anemia and marrow failure
End-organ damage includes anemia, and stromal dysfunction includes reduced hematopoietic support (twofold reduction in MGUS/SMM and larger reductions in MM MSCs), providing a mechanistic link between niche failure and cytopenias. (moscvin2023dissectingmolecularmechanisms pages 1-3, bogun2024stromalalterationsin pages 11-12)

---

## 8. Recent developments (2023–2024) and “latest research” highlights

### 8.1 Epigenomic rewiring by non-canonical NF-κB (2024)
A 2024 mechanistic study shows sustained p52 (non-canonical NF-κB) remodels enhancer landscapes and 3D chromatin loops to maintain myeloma dependency transcriptional programs—moving beyond pathway “activation” to **cis-regulatory architecture** as a driver. (BioRxiv Jan 2024; https://doi.org/10.1101/2024.01.09.574787). (ang2024aberrantnoncanonicalnfκb pages 7-8)

### 8.2 Immune microenvironment quantification across precursors (2024)
Multi-omics profiling supports that immune remodeling starts in precursor states, with quantitative changes in granulocytes, pDCs, and CD16+ monocytes, and increased TIM3/TIGIT inhibitory markers during progression. (Blood Cancer Journal, Nov 2024; https://doi.org/10.1038/s41408-024-01172-x). (cheng2024multiomicsrevealimmune pages 1-2)

### 8.3 Stromal (MSC) reprogramming and BMP/TGF signaling as interception targets (2024)
A 2024 Blood Advances study highlights stromal alterations already in MGUS, with BMP/TGF pathway dysregulation, senescence (e.g., CDKN2A/p16 upregulation), reduced osteogenesis, and diminished hematopoietic support; the use of a TGF-βRI inhibitor (SD208) to restore osteogenic capacity suggests a niche-targeted prevention concept. (May 2024; https://doi.org/10.1182/bloodadvances.2023011632). (bogun2024stromalalterationsin pages 1-2, bogun2024stromalalterationsin pages 11-12)

### 8.4 Bone–ecosystem modeling of relapse and EMDR (2024)
A 2024 Nature Communications study integrates a spatiotemporal model and in vivo testing to show that bone microenvironment-mediated resistance increases the heterogeneity and probability of resistant clones—supporting “ecological” strategies to delay relapse. (Mar 2024; https://doi.org/10.1038/s41467-024-46594-0). (bishop2024theboneecosystem media ec296c58, bishop2024theboneecosystem media ea2ecb8d)

---

## 9. Current applications and real-world implementations

### 9.1 Therapeutic classes that map onto pathophysiology
Real-world MM management uses agents that target both tumor-intrinsic programs and microenvironment/immune axes.

* **Proteasome inhibitors (PIs)** (e.g., bortezomib, carfilzomib) map onto the proteostasis vulnerability of plasma cells, while resistance may involve NF-κB activation and stress response programs. (ram2024thegeneticand pages 20-22, ram2024thegeneticand pages 25-26)
* **Microenvironment/cytokine targeting**: IL-6/IL-6R axis is explicitly cited as a TME-driven proliferative pathway and is pharmacologically targetable (siltuximab/tocilizumab examples in review). (ram2024thegeneticand pages 25-26)
* **Immune-based therapies**: CAR-T cells and bispecific antibodies rely on T-cell status; immune contexture and exhaustion-associated states (e.g., TOX+ CD8+ cells) correlate with outcomes and motivate immune-status-based selection frameworks. (dhodapkar2024immunestatusand pages 2-3)
* **Bone-targeted therapies**: bisphosphonates and denosumab are standard antiresorptives; newer mechanistic axes (FLT3L–STAT3–DKK1; PD-1H–MMP13; CCL3–HMGB1–RANKL) suggest future niche/bone interception targets. (shin2024elucidationofmolecular pages 9-10, fu2023thecheckpointinhibitor pages 1-2, anloague2024anovelccl3hmgb1 pages 13-14)

### 9.2 Risk stratification and early interception
High-risk SMM identification using SLiM biomarkers (FLC ratio, marrow plasmacytosis, imaging lesions) is a current clinical application of biology-informed progression risk. (kansal2024towardprecisionmedicine pages 2-3)

---

## 10. Expert opinions and authoritative analyses (selected)

* Immune dysfunction is not confined to the tumor mass: clinical malignancy “originates in the setting of systemic immune alterations that begin early in myelomagenesis and regional changes in immunity affected by spatial contexture,” and immune-status variation is “emerging as a major determinant” of immune-therapy efficacy—supporting spatially informed patient selection. (Blood Advances, May 2024; https://doi.org/10.1182/bloodadvances.2023011242). (dhodapkar2024immunestatusand pages 2-3)

* A 2023 immunopathology review emphasizes that MM progression is accompanied by skewing toward an immune-tolerant environment; it highlights MDSCs, DC alterations, M2-like macrophages, and Th17/Treg shifts as a coherent immune-escape system. (May 2023; https://doi.org/10.20517/2394-4722.2022.110). (moscvin2023dissectingmolecularmechanisms pages 1-3)

---

## 11. Recent statistics and data (2023–2024 evidence)

### 11.1 Progression risks
* MGUS progression risk: ~**1% per year**. (liotti2024investigationonthe pages 9-13, barakat2023investigatingtcell pages 14-17)
* SMM progression risk: ~**10%/year for first 5 years**, then **3%/year for next 5**, then **~1%/year**. (liotti2024investigationonthe pages 9-13)

### 11.2 Immune microenvironment quantitative shifts
* Rapid progressors: exhausted CD8 T cells (GZMK+, TIGIT+) enriched with **P = 0.022**; higher exhausted T-cell ratio **P = 0.049**; decreased cytolytic gene expression (PRF1, GZMB, GNLY). (pilcher2023crosscentersinglecell pages 1-2)
* Across MGUS/SMM/NDMM: **65% decrease of immature granulocytes in MGUS**, **53% decrease of pDCs in SMM**, and CD16+ monocytes increased **5.6-fold in MGUS** vs normal BM (CyTOF). (cheng2024multiomicsrevealimmune pages 1-2)

### 11.3 Genomic statistics
* RAS mutations reported in **~50%** of MM patients (review synthesis). (ram2024thegeneticand pages 25-26)
* TP53 pathway inactivation reported in **~45%** of patients in summarized relapsed/refractory contexts. (ram2024thegeneticand pages 20-22)

---

## 12. Knowledge-base ready artifacts

| Mechanism / Pathway | Key Genes & Molecules | Cellular Context | Clinical Phenotype | Representative Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **FLT3L-STAT3-DKK1 Axis** | *FLT3L*, *STAT3* (pY705), *DKK1* | Plasma Cells → Osteoblasts (Bone Marrow) | **Osteolytic Bone Lesions**: Inhibition of WNT-mediated bone formation; high FLT3L links to poor prognosis. | (shin2024elucidationofmolecular pages 9-10, shin2024elucidationofmolecular pages 1-2, shin2024elucidationofmolecular pages 2-3) |
| **Osteocyte-Driven Osteoclastogenesis** | *CCL3* (MIP-1α), *HMGB1*, *TNFSF11* (RANKL) | Plasma Cells → Osteocytes | **Bone Resorption**: CCL3 induces osteocyte HMGB1 release and RANKL upregulation, amplifying osteoclast activity. | (anloague2024anovelccl3hmgb1 pages 13-14, anloague2024anovelccl3hmgb1 pages 14-15) |
| **Non-Canonical NF-κB Activation** | *NFKB2* (p52), *TRAF3*, *CYLD*, *NIK* | Plasma Cells | **Tumor Progression**: Epigenetic rewiring of enhancers drives oncogenic transcriptomes and survival. | (ang2024aberrantnoncanonicalnfκb pages 7-8, ram2024thegeneticand pages 22-23) |
| **T-Cell Exhaustion & Checkpoints** | *TIGIT*, *LAG3*, *PDCD1* (PD-1), *GZMK* vs *GZMB* | CD8+ T Cells, NK Cells (Bone Marrow) | **Immune Evasion**: Rapid progression linked to TIGIT+/GZMK+ exhausted T cells and loss of cytolytic function. | (pilcher2023crosscentersinglecell pages 1-2, cheng2024multiomicsrevealimmune pages 1-2, barakat2023investigatingtcell pages 66-70) |
| **Stromal Senescence & TGF-β** | *TGFB1*, *BMP2*, *CDKN2A* (p16) | Mesenchymal Stromal Cells (MSCs) | **Niche Dysfunction**: Impaired osteogenesis and hematopoietic support; promotes progression from MGUS/SMM. | (bogun2024stromalalterationsin pages 1-2, bogun2024stromalalterationsin pages 11-12, bogun2024stromalalterationsin pages 6-8) |
| **PD-1H (VISTA) Signaling** | *VSIR* (PD-1H), *MMP13* | Osteoclasts | **Bone Destruction**: PD-1H acts as a receptor for MMP-13 to drive osteoclast fusion and resorption. | (fu2023thecheckpointinhibitor pages 1-2) |
| **RAS/MAPK Pathway** | *KRAS*, *NRAS*, *BRAF* | Plasma Cells | **Therapy Resistance**: Mutations drive proliferation and are enriched in relapsed/refractory disease. | (ram2024thegeneticand pages 20-22, ram2024thegeneticand pages 25-26) |
| **Microenvironment-Mediated Resistance** | *IL6*, *CXCL12*, *VEGF*, Fibronectin | BM Stromal Cells, MDSCs | **Drug Resistance**: Stromal adhesion and soluble factors shelter tumor cells from therapy (EMDR). | (bhowmick2024pathwaystotherapy pages 1-3, bishop2024theboneecosystem media ec296c58) |


*Table: A summary of key molecular pathways, cellular interactions, and genetic drivers identified in 2023-2024 literature that contribute to multiple myeloma progression, bone disease, and therapy resistance.*

| Gene/Protein (HGNC) | GO Biological Process | GO Cellular Component | Cell Type (CL) | Anatomy (UBERON) | Chemical/Drug (ChEBI) | Phenotype (HPO) | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *FLT3L*, *STAT3*, *DKK1* | negative regulation of ossification; Wnt signaling pathway | extracellular space | osteoblast; plasma cell | bone marrow | - | Osteolytic defects; Skeletal dysplasia | (shin2024elucidationofmolecular pages 9-10, shin2024elucidationofmolecular pages 1-2, shin2024elucidationofmolecular pages 2-3) |
| *CCL3* (MIP-1α), *HMGB1*, *TNFSF11* (RANKL) | osteoclast differentiation; positive regulation of bone resorption | extracellular space | osteocyte; plasma cell | bone | RANKL; denosumab | Osteolysis; Bone pain | (anloague2024anovelccl3hmgb1 pages 13-14, anloague2024anovelccl3hmgb1 pages 14-15) |
| *NFKB2* (p52), *TRAF3*, *CYLD* | chromatin remodeling; non-canonical NF-kappaB signal transduction | nucleus; chromatin | plasma cell | bone marrow | - | Neoplasm | (ang2024aberrantnoncanonicalnfκb pages 7-8, ram2024thegeneticand pages 22-23) |
| *TIGIT*, *LAG3*, *PDCD1* | T cell exhaustion; immune response-inhibiting signal transduction | plasma membrane | CD8-positive alpha-beta T cell; NK cell | bone marrow | - | Recurrent infections; Progression | (pilcher2023crosscentersinglecell pages 1-2, cheng2024multiomicsrevealimmune pages 1-2, barakat2023investigatingtcell pages 66-70) |
| *TGFB1*, *BMP2*, *CXCL12* | cell differentiation; regulation of immune system process | extracellular space | mesenchymal stromal cell | bone marrow | TGF-beta; SD208 (TGFβRI inhibitor) | Anemia; Bone marrow failure | (bogun2024stromalalterationsin pages 1-2, bogun2024stromalalterationsin pages 12-13, bogun2024stromalalterationsin pages 11-12, bogun2024stromalalterationsin pages 13-14) |
| *KRAS*, *NRAS*, *BRAF* | cell population proliferation; MAPK cascade | cytoplasm; nucleus | plasma cell | bone marrow | bortezomib; carfilzomib | Multiple myeloma; Drug resistance | (ram2024thegeneticand pages 20-22, ram2024thegeneticand pages 25-26) |
| *VSIR* (PD-1H), *MMP13* | cell fusion; bone resorption | plasma membrane | osteoclast | bone | - | Osteolytic defects | (fu2023thecheckpointinhibitor pages 1-2) |
| *IL6*, *IL10* | inflammatory response; positive regulation of cell population proliferation | extracellular space | myeloid-derived suppressor cell; macrophage | bone marrow | IL-6; lenalidomide | Plasmacytosis; Inflammation | (bhowmick2024pathwaystotherapy pages 1-3, barakat2023investigatingtcell pages 17-21, radhakrishnan2024roleofimmune pages 4-5) |


*Table: A structured annotation table mapping key molecular players, disrupted biological processes, involved cell types, and clinical phenotypes in Multiple Myeloma to ontology-compliant terms, supported by recent evidence.*

---

## 13. Visual evidence
Bishop et al. (Nature Communications, Mar 2024; https://doi.org/10.1038/s41467-024-46594-0) provide a schematic of the MM–bone “vicious cycle” and a hybrid model capturing **environment-mediated drug resistance (EMDR)** via spatial proximity to stroma/bone-derived factors, supporting the concept of minimal residual disease reservoirs in protective bone niches. (bishop2024theboneecosystem media ec296c58, bishop2024theboneecosystem media ea2ecb8d)

---

## 14. Evidence items (PMIDs)
Primary claims above are mainly supported by full-text/DOI evidence in the retrieved excerpts; **PMIDs were often not present in the retrieved text snippets** for many 2024 papers. Where PMIDs were programmatically available from Open Targets evidence lists (and not necessarily directly tied to specific mechanistic claims above), examples include: **23480694** (CRBN association evidence) and several older FGFR3-related PMIDs (e.g., 9207791, 10568829, 11290605, 11429702, 19381019, 20439987, 22869148). ()

---

## References (URLs / dates from retrieved metadata)
* Shin D et al. *Haematologica* **Jan 2024**. “Elucidation of molecular basis of osteolytic bone lesions in advanced multiple myeloma.” https://doi.org/10.3324/haematol.2023.283784 (shin2024elucidationofmolecular pages 1-2)
* Fu J et al. *Nature Communications* **Jul 2023**. “The checkpoint inhibitor PD-1H/VISTA controls osteoclast-mediated multiple myeloma bone disease.” https://doi.org/10.1038/s41467-023-39769-8 (fu2023thecheckpointinhibitor pages 1-2)
* Bogun L et al. *Blood Advances* **May 2024**. “Stromal alterations in patients with MGUS, smoldering myeloma, and multiple myeloma.” https://doi.org/10.1182/bloodadvances.2023011632 (bogun2024stromalalterationsin pages 1-2)
* Cheng Y et al. *Blood Cancer Journal* **Nov 2024**. “Multi-omics reveal immune microenvironment alterations in multiple myeloma and its precursor stages.” https://doi.org/10.1038/s41408-024-01172-x (cheng2024multiomicsrevealimmune pages 1-2)
* Pilcher W et al. *npj Genomic Medicine* **Jan 2023**. “Cross center single-cell RNA sequencing study of the immune microenvironment in rapid progressing multiple myeloma.” https://doi.org/10.1038/s41525-022-00340-x (pilcher2023crosscentersinglecell pages 1-2)
* Dhodapkar MV. *Blood Advances* **May 2024**. “Immune status and selection of patients for immunotherapy in myeloma: a proposal.” https://doi.org/10.1182/bloodadvances.2023011242 (dhodapkar2024immunestatusand pages 2-3)
* Bishop RT et al. *Nature Communications* **Mar 2024**. “The bone ecosystem facilitates multiple myeloma relapse and the evolution of heterogeneous drug resistant disease.” https://doi.org/10.1038/s41467-024-46594-0 (bishop2024theboneecosystem media ea2ecb8d)
* Gong L et al. *Cancers* **Jan 2024**. “Novel Insights into the Initiation, Evolution, and Progression of Multiple Myeloma by Multi-Omics Investigation.” https://doi.org/10.3390/cancers16030498 (gong2024novelinsightsinto pages 10-12)
* Ang DA et al. *bioRxiv* **Jan 2024**. “Aberrant non-canonical NF-κB signalling reprograms the epigenome landscape to drive oncogenic transcriptomes in multiple myeloma.” https://doi.org/10.1101/2024.01.09.574787 (ang2024aberrantnoncanonicalnfκb pages 7-8)
* Bhowmick K et al. *Heliyon* **Jun 2024**. “Pathways to therapy resistance: The sheltering effect of the bone marrow microenvironment to multiple myeloma cells.” https://doi.org/10.1016/j.heliyon.2024.e33091 (bhowmick2024pathwaystotherapy pages 1-3)


References

1. (moscvin2023dissectingmolecularmechanisms pages 1-3): Maria Moscvin, Benjamin Evans, and Giada Bianchi. Dissecting molecular mechanisms of immune microenvironment dysfunction in multiple myeloma and precursor conditions. Journal of cancer metastasis and treatment, May 2023. URL: https://doi.org/10.20517/2394-4722.2022.110, doi:10.20517/2394-4722.2022.110. This article has 7 citations.

2. (bhowmick2024pathwaystotherapy pages 1-3): Kuntal Bhowmick, Max von Suskil, Omar S. Al-Odat, Weam Othman Elbezanti, Subash C. Jonnalagadda, Tulin Budak-Alpdogan, and Manoj K. Pandey. Pathways to therapy resistance: the sheltering effect of the bone marrow microenvironment to multiple myeloma cells. Heliyon, 10:e33091, Jun 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e33091, doi:10.1016/j.heliyon.2024.e33091. This article has 14 citations.

3. (kansal2024towardprecisionmedicine pages 2-3): Rina Kansal. Toward precision medicine for patients with multiple myeloma. Journal of Clinical Haematology, 5:12-33, Jan 2024. URL: https://doi.org/10.33696/haematology.5.058, doi:10.33696/haematology.5.058. This article has 1 citations.

4. (liotti2024investigationonthe pages 9-13): Romano Liotti. Investigation on the potential of liquid biopsies in multiple myeloma and its presymptomatic stages. Unknown, May 2024. URL: https://doi.org/10.25434/liotti-romano\_phd2024-05-30, doi:10.25434/liotti-romano\_phd2024-05-30. This article has 0 citations.

5. (gong2024novelinsightsinto pages 10-12): Lixin Gong, Lugui Qiu, and Mu Hao. Novel insights into the initiation, evolution, and progression of multiple myeloma by multi-omics investigation. Cancers, 16:498, Jan 2024. URL: https://doi.org/10.3390/cancers16030498, doi:10.3390/cancers16030498. This article has 7 citations.

6. (lemonakis2024factorsaffectingprognosis pages 24-28): K Lemonakis. Factors affecting prognosis of mgus and multiple myeloma. Unknown journal, 2024.

7. (ram2024thegeneticand pages 25-26): Meghana Ram, Molly Fraser, Junia Vieira dos Santos, Rafail Tasakis, Ariana Islam, Jannah Abo-Donia, Samir Parekh, and Alessandro Lagana. The genetic and molecular drivers of multiple myeloma: current insights, clinical implications, and the path forward. Pharmacogenomics and Personalized Medicine, 17:573-609, Dec 2024. URL: https://doi.org/10.2147/pgpm.s350238, doi:10.2147/pgpm.s350238. This article has 8 citations and is from a peer-reviewed journal.

8. (ang2024aberrantnoncanonicalnfκb pages 7-8): Daniel A. Ang, Jean-Michel Carter, Kamalakshi Deka, Joel H.L. Tan, Jianbiao Zhou, Qingfeng Chen, Wee Joo Chng, Nathan Harmston, and Yinghui Li. Aberrant non-canonical nf-κb signalling reprograms the epigenome landscape to drive oncogenic transcriptomes in multiple myeloma. BioRxiv, Jan 2024. URL: https://doi.org/10.1101/2024.01.09.574787, doi:10.1101/2024.01.09.574787. This article has 8 citations.

9. (ram2024thegeneticand pages 20-22): Meghana Ram, Molly Fraser, Junia Vieira dos Santos, Rafail Tasakis, Ariana Islam, Jannah Abo-Donia, Samir Parekh, and Alessandro Lagana. The genetic and molecular drivers of multiple myeloma: current insights, clinical implications, and the path forward. Pharmacogenomics and Personalized Medicine, 17:573-609, Dec 2024. URL: https://doi.org/10.2147/pgpm.s350238, doi:10.2147/pgpm.s350238. This article has 8 citations and is from a peer-reviewed journal.

10. (bishop2024theboneecosystem media ec296c58): Ryan T. Bishop, Anna K. Miller, Matthew Froid, Niveditha Nerlakanti, Tao Li, Jeremy S. Frieling, Mostafa M. Nasr, Karl J. Nyman, Praneeth R. Sudalagunta, Rafael R. Canevarolo, Ariosto Siqueira Silva, Kenneth H. Shain, Conor C. Lynch, and David Basanta. The bone ecosystem facilitates multiple myeloma relapse and the evolution of heterogeneous drug resistant disease. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46594-0, doi:10.1038/s41467-024-46594-0. This article has 15 citations and is from a highest quality peer-reviewed journal.

11. (bishop2024theboneecosystem media ea2ecb8d): Ryan T. Bishop, Anna K. Miller, Matthew Froid, Niveditha Nerlakanti, Tao Li, Jeremy S. Frieling, Mostafa M. Nasr, Karl J. Nyman, Praneeth R. Sudalagunta, Rafael R. Canevarolo, Ariosto Siqueira Silva, Kenneth H. Shain, Conor C. Lynch, and David Basanta. The bone ecosystem facilitates multiple myeloma relapse and the evolution of heterogeneous drug resistant disease. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46594-0, doi:10.1038/s41467-024-46594-0. This article has 15 citations and is from a highest quality peer-reviewed journal.

12. (cheng2024multiomicsrevealimmune pages 1-2): Yan Cheng, Fumou Sun, Daisy V. Alapat, Visanu Wanchai, David E. Mery, Eric Siegel, Hongwei Xu, Sarah K. Johnson, Wancheng Guo, Clyde Bailey, Cody Ashby, Michael Anton Bauer, Samer Al Hadidi, Carolina Schinke, Sharmilan Thanendrarajan, Maurizio Zangari, Frits van Rhee, Guido Tricot, Jr John D Shaughnessy, and Fenghuang Zhan. Multi-omics reveal immune microenvironment alterations in multiple myeloma and its precursor stages. Blood Cancer Journal, 14:4729-4729, Nov 2024. URL: https://doi.org/10.1038/s41408-024-01172-x, doi:10.1038/s41408-024-01172-x. This article has 27 citations and is from a domain leading peer-reviewed journal.

13. (pilcher2023crosscentersinglecell pages 1-2): William Pilcher, Beena E. Thomas, Swati S. Bhasin, Reyka G. Jayasinghe, Lijun Yao, Edgar Gonzalez-Kozlova, Surendra Dasari, Seunghee Kim-Schulze, Adeeb Rahman, Jonathan Patton, Mark Fiala, Giulia Cheloni, Taxiarchis Kourelis, Madhav V. Dhodapkar, Ravi Vij, Shaadi Mehr, Mark Hamilton, Hearn Jay Cho, Daniel Auclair, David E. Avigan, Shaji K. Kumar, Sacha Gnjatic, Li Ding, and Manoj Bhasin. Cross center single-cell rna sequencing study of the immune microenvironment in rapid progressing multiple myeloma. npj Genomic Medicine, Jan 2023. URL: https://doi.org/10.1038/s41525-022-00340-x, doi:10.1038/s41525-022-00340-x. This article has 42 citations and is from a peer-reviewed journal.

14. (dhodapkar2024immunestatusand pages 2-3): Madhav V. Dhodapkar. Immune status and selection of patients for immunotherapy in myeloma: a proposal. May 2024. URL: https://doi.org/10.1182/bloodadvances.2023011242, doi:10.1182/bloodadvances.2023011242. This article has 16 citations and is from a peer-reviewed journal.

15. (ram2024thegeneticand pages 22-23): Meghana Ram, Molly Fraser, Junia Vieira dos Santos, Rafail Tasakis, Ariana Islam, Jannah Abo-Donia, Samir Parekh, and Alessandro Lagana. The genetic and molecular drivers of multiple myeloma: current insights, clinical implications, and the path forward. Pharmacogenomics and Personalized Medicine, 17:573-609, Dec 2024. URL: https://doi.org/10.2147/pgpm.s350238, doi:10.2147/pgpm.s350238. This article has 8 citations and is from a peer-reviewed journal.

16. (shin2024elucidationofmolecular pages 1-2): Dongyeop Shin, Myung-Jin Kim, Soyeon Chun, Dongchan Kim, Chansu Lee, Kwang-Sung Ahn, Eunyoung Jung, Dayeon Kim, Byung-Chul Lee, Dae-Ryong Hwang, Yonghwan Kim, and Sung-Soo Yoon. Elucidation of molecular basis of osteolytic bone lesions in advanced multiple myeloma. Haematologica, 109:2207-2218, Jan 2024. URL: https://doi.org/10.3324/haematol.2023.283784, doi:10.3324/haematol.2023.283784. This article has 8 citations.

17. (anloague2024anovelccl3hmgb1 pages 13-14): Aric Anloague, Hayley M. Sabol, Japneet Kaur, Sharmin Khan, Cody Ashby, Carolina Schinke, C. Lowry Barnes, Farah Alturkmani, Elena Ambrogini, Michael Tveden Gundesen, Thomas Lund, Anne Kristine Amstrup, Thomas Levin Andersen, Marta Diaz-delCastillo, G. David Roodman, Teresita Bellido, and Jesus Delgado-Calle. A novel ccl3-hmgb1 signaling axis regulating osteocyte rankl expression in multiple myeloma. Haematologica, 110:952-966, Nov 2024. URL: https://doi.org/10.3324/haematol.2024.286484, doi:10.3324/haematol.2024.286484. This article has 10 citations.

18. (fu2023thecheckpointinhibitor pages 1-2): Jing Fu, Shirong Li, Huihui Ma, Jun Yang, Gabriel M. Pagnotti, Lewis M. Brown, Stephen J. Weiss, Markus Y. Mapara, and Suzanne Lentzsch. The checkpoint inhibitor pd-1h/vista controls osteoclast-mediated multiple myeloma bone disease. Nature Communications, Jul 2023. URL: https://doi.org/10.1038/s41467-023-39769-8, doi:10.1038/s41467-023-39769-8. This article has 21 citations and is from a highest quality peer-reviewed journal.

19. (bogun2024stromalalterationsin pages 1-2): Lucienne Bogun, Annemarie Koch, Bo Scherer, Roland Fenk, Uwe Maus, Felix Bormann, Karl Köhrer, Patrick Petzsch, Thorsten Wachtmeister, Romans Zukovs, Sascha Dietrich, Rainer Haas, Thomas Schroeder, Paul Jäger, and Stefanie Geyh. Stromal alterations in patients with monoclonal gammopathy of undetermined significance, smoldering myeloma, and multiple myeloma. Blood Advances, 8:2575-2588, May 2024. URL: https://doi.org/10.1182/bloodadvances.2023011632, doi:10.1182/bloodadvances.2023011632. This article has 10 citations and is from a peer-reviewed journal.

20. (bogun2024stromalalterationsin pages 11-12): Lucienne Bogun, Annemarie Koch, Bo Scherer, Roland Fenk, Uwe Maus, Felix Bormann, Karl Köhrer, Patrick Petzsch, Thorsten Wachtmeister, Romans Zukovs, Sascha Dietrich, Rainer Haas, Thomas Schroeder, Paul Jäger, and Stefanie Geyh. Stromal alterations in patients with monoclonal gammopathy of undetermined significance, smoldering myeloma, and multiple myeloma. Blood Advances, 8:2575-2588, May 2024. URL: https://doi.org/10.1182/bloodadvances.2023011632, doi:10.1182/bloodadvances.2023011632. This article has 10 citations and is from a peer-reviewed journal.

21. (barakat2023investigatingtcell pages 14-17): Elie Barakat. Investigating t cell exhaustion in multiple myeloma. Other, Apr 2023. URL: https://doi.org/10.11575/prism/dspace/40968, doi:10.11575/prism/dspace/40968. This article has 0 citations.

22. (moscvin2023dissectingmolecularmechanisms pages 11-13): Maria Moscvin, Benjamin Evans, and Giada Bianchi. Dissecting molecular mechanisms of immune microenvironment dysfunction in multiple myeloma and precursor conditions. Journal of cancer metastasis and treatment, May 2023. URL: https://doi.org/10.20517/2394-4722.2022.110, doi:10.20517/2394-4722.2022.110. This article has 7 citations.

23. (shin2024elucidationofmolecular pages 2-3): Dongyeop Shin, Myung-Jin Kim, Soyeon Chun, Dongchan Kim, Chansu Lee, Kwang-Sung Ahn, Eunyoung Jung, Dayeon Kim, Byung-Chul Lee, Dae-Ryong Hwang, Yonghwan Kim, and Sung-Soo Yoon. Elucidation of molecular basis of osteolytic bone lesions in advanced multiple myeloma. Haematologica, 109:2207-2218, Jan 2024. URL: https://doi.org/10.3324/haematol.2023.283784, doi:10.3324/haematol.2023.283784. This article has 8 citations.

24. (shin2024elucidationofmolecular pages 9-10): Dongyeop Shin, Myung-Jin Kim, Soyeon Chun, Dongchan Kim, Chansu Lee, Kwang-Sung Ahn, Eunyoung Jung, Dayeon Kim, Byung-Chul Lee, Dae-Ryong Hwang, Yonghwan Kim, and Sung-Soo Yoon. Elucidation of molecular basis of osteolytic bone lesions in advanced multiple myeloma. Haematologica, 109:2207-2218, Jan 2024. URL: https://doi.org/10.3324/haematol.2023.283784, doi:10.3324/haematol.2023.283784. This article has 8 citations.

25. (anloague2024anovelccl3hmgb1 pages 14-15): Aric Anloague, Hayley M. Sabol, Japneet Kaur, Sharmin Khan, Cody Ashby, Carolina Schinke, C. Lowry Barnes, Farah Alturkmani, Elena Ambrogini, Michael Tveden Gundesen, Thomas Lund, Anne Kristine Amstrup, Thomas Levin Andersen, Marta Diaz-delCastillo, G. David Roodman, Teresita Bellido, and Jesus Delgado-Calle. A novel ccl3-hmgb1 signaling axis regulating osteocyte rankl expression in multiple myeloma. Haematologica, 110:952-966, Nov 2024. URL: https://doi.org/10.3324/haematol.2024.286484, doi:10.3324/haematol.2024.286484. This article has 10 citations.

26. (barakat2023investigatingtcell pages 66-70): Elie Barakat. Investigating t cell exhaustion in multiple myeloma. Other, Apr 2023. URL: https://doi.org/10.11575/prism/dspace/40968, doi:10.11575/prism/dspace/40968. This article has 0 citations.

27. (bogun2024stromalalterationsin pages 6-8): Lucienne Bogun, Annemarie Koch, Bo Scherer, Roland Fenk, Uwe Maus, Felix Bormann, Karl Köhrer, Patrick Petzsch, Thorsten Wachtmeister, Romans Zukovs, Sascha Dietrich, Rainer Haas, Thomas Schroeder, Paul Jäger, and Stefanie Geyh. Stromal alterations in patients with monoclonal gammopathy of undetermined significance, smoldering myeloma, and multiple myeloma. Blood Advances, 8:2575-2588, May 2024. URL: https://doi.org/10.1182/bloodadvances.2023011632, doi:10.1182/bloodadvances.2023011632. This article has 10 citations and is from a peer-reviewed journal.

28. (bogun2024stromalalterationsin pages 12-13): Lucienne Bogun, Annemarie Koch, Bo Scherer, Roland Fenk, Uwe Maus, Felix Bormann, Karl Köhrer, Patrick Petzsch, Thorsten Wachtmeister, Romans Zukovs, Sascha Dietrich, Rainer Haas, Thomas Schroeder, Paul Jäger, and Stefanie Geyh. Stromal alterations in patients with monoclonal gammopathy of undetermined significance, smoldering myeloma, and multiple myeloma. Blood Advances, 8:2575-2588, May 2024. URL: https://doi.org/10.1182/bloodadvances.2023011632, doi:10.1182/bloodadvances.2023011632. This article has 10 citations and is from a peer-reviewed journal.

29. (bogun2024stromalalterationsin pages 13-14): Lucienne Bogun, Annemarie Koch, Bo Scherer, Roland Fenk, Uwe Maus, Felix Bormann, Karl Köhrer, Patrick Petzsch, Thorsten Wachtmeister, Romans Zukovs, Sascha Dietrich, Rainer Haas, Thomas Schroeder, Paul Jäger, and Stefanie Geyh. Stromal alterations in patients with monoclonal gammopathy of undetermined significance, smoldering myeloma, and multiple myeloma. Blood Advances, 8:2575-2588, May 2024. URL: https://doi.org/10.1182/bloodadvances.2023011632, doi:10.1182/bloodadvances.2023011632. This article has 10 citations and is from a peer-reviewed journal.

30. (barakat2023investigatingtcell pages 17-21): Elie Barakat. Investigating t cell exhaustion in multiple myeloma. Other, Apr 2023. URL: https://doi.org/10.11575/prism/dspace/40968, doi:10.11575/prism/dspace/40968. This article has 0 citations.

31. (radhakrishnan2024roleofimmune pages 4-5): Vijay Radhakrishnan, Upendarrao Golla, and Avinash Kundadka Kudva. Role of immune cells and immunotherapy in multiple myeloma. Life, 14:461, Apr 2024. URL: https://doi.org/10.3390/life14040461, doi:10.3390/life14040461. This article has 17 citations.