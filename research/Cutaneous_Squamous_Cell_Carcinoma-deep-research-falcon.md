---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-06T03:39:33.518764'
end_time: '2026-03-06T03:47:46.241824'
duration_seconds: 492.72
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cutaneous Squamous Cell Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Cutaneous Squamous Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Cutaneous Squamous Cell Carcinoma**.
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
- **Disease Name:** Cutaneous Squamous Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Cutaneous Squamous Cell Carcinoma**.
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


# Cutaneous Squamous Cell Carcinoma (cSCC): Pathophysiology Research Report (molecular/cellular mechanisms)

## Disease identifiers and scope
- **Disease name:** Cutaneous squamous cell carcinoma (cSCC)
- **Ontology IDs:** **EFO: EFO_1001927 (cutaneous squamous cell carcinoma)**; related broader term **MONDO: MONDO_0002529 (skin squamous cell carcinoma)** (ontology linkage noted via Open Targets disease listing; mechanistic content below focuses on cSCC in skin). (hosseini2024themutationaland pages 1-2)
- **Category:** Keratinocyte-derived non-melanoma skin cancer (NMSC). cSCC is described as the “second most common subtype of non-melanoma skin cancer” and responsible for ~20% of skin cancers. (hosseini2024themutationaland pages 1-2)

## 1) Key concepts and definitions (current understanding)
### 1.1 Definition and cellular origin
cSCC arises from malignant proliferation of **epidermal keratinocytes**, with a strong association to chronic sun exposure/UV radiation as a leading preventable risk factor. (corchadocobos2023cutaneoussquamouscell pages 1-3, hosseini2024themutationaland pages 1-2)

### 1.2 Field cancerization (foundational concept)
**Field cancerization** in skin refers to a region that can appear clinically/morphologically normal while harboring **mutated keratinocyte clones** that expand under chronic UV exposure, creating a “field” predisposed to multiple actinic keratoses (AK) and cSCC. (camillo2024exvivoanalysis pages 1-2)

A 2024 ex vivo study frames this explicitly as: “**cutaneously field cancerization (CFC) refers to a skin region containing mutated cells’ clones**… arising from chronic exposure to ultraviolet radiation (UVR)” and associated with increased risk for AK and cSCC. (camillo2024exvivoanalysis pages 1-2)

### 1.3 Disease continuum / progression state shift
Recent transcriptomic profiling supports a **continuum** across: **normal sun-exposed skin → AK → primary cSCC → metastasis**, characterized by a shift “**from a differentiated to a progenitor-like state**,” with suppression of epidermal differentiation regulators, remodeling of immune landscape, and increased tumor-specific keratinocytes. (bailey2023drivergenecombinations pages 1-2, bailey2023drivergenecombinations media 6aac691f, bailey2023drivergenecombinations media 983dee4c)

## 2) Core pathophysiology (primary mechanisms, pathways, processes)
### 2.1 UV-driven DNA damage and mutational signatures
**UVB exposure** is repeatedly emphasized as the central preventable etiologic driver, inducing characteristic UV mutational patterns in keratinocytes and precursors. (hosseini2024themutationaland pages 1-2)

Mechanistically:
- UV causes DNA mutations (often repaired by **nucleotide excision repair (NER)**); defective repair can contribute to tumorigenesis. (hosseini2024themutationaland pages 1-2)
- Reported UV signatures include **C>T substitutions at dipyrimidine sites** and **CC>TT dinucleotide substitutions**; newer work also identifies frequent **T>C substitutions** with specific sequence motifs. (hosseini2024themutationaland pages 1-2)

**Clinical/biological implication:** cSCC has a very high tumor mutational burden; one 2024 review reports median **~45.2 mutations/Mb** for cSCC, consistent with UV etiopathogenesis and immunogenicity. (sol2024therapeuticapproachesfor pages 2-3)

### 2.2 Early driver events + altered epidermal homeostasis
A 2024 review describes cSCC tumorigenesis as a “disruption of epidermal homeostasis” driven by **UV-induced DNA damage, gene mutations, and tumor microenvironment changes**. (hosseini2024themutationaland pages 1-2)

Key early events include **TP53** and **NOTCH** pathway disruption:
- TP53 is repeatedly cited as among the most frequently mutated drivers; importantly, TP53 mutations also appear in AK and even normal sun-exposed skin, supporting field cancerization and complicating “driver vs passenger” assignment. (hosseini2024themutationaland pages 4-6, hosseini2024themutationaland pages 1-2)
- NOTCH family genes (NOTCH1/2/3) show frequent mutations in normal sun-exposed skin; one review quantifies NOTCH alterations averaging **83 driver mutations/cm²** in normal skin, and TP53 **~9.5 driver mutations/cm²**. (hosseini2024themutationaland pages 1-2)

### 2.3 AK→cSCC transition: pathway activation and selection
Although AK and normal sun-exposed skin share many mutations, **progression is associated with coordinated transcriptomic and microenvironmental changes**, including:
- suppression of epidermal differentiation programs and induction of progenitor-like programs (differentiated→progenitor axis). (bailey2023drivergenecombinations pages 1-2, bailey2023drivergenecombinations media 6aac691f)
- evidence that **PI3K/AKT/mTOR** signaling is “consistently activated in cSCC but not in AK,” implicating it as a transition-associated pathway (e.g., PTEN loss, PIK3CA activation). (hosseini2024themutationaland pages 4-6)

### 2.4 Tumor microenvironment (TME) and immune evasion
Multiple 2023–2024 sources emphasize that cSCC progression involves active immune manipulation and immune-evasive TMEs:
- Advanced cSCC TMEs have increased **TGF-β**, **IL-10**, and **regulatory T cells (Tregs)** and reduced plasmacytoid dendritic cells (pDCs), consistent with suppression of anti-tumor immunity. (jiang2024cutaneoussquamouscell pages 1-2)
- A TME-focused review details pro-tumor immune cell polarization and stromal remodeling: M2 tumor-associated macrophages (TAMs) and cancer-associated fibroblasts (CAFs) contribute to angiogenesis/ECM remodeling and immunosuppression, including CAF secretion of **MMPs**, **VEGF**, and **IL-6**, and TAM secretion of MMP-9/11 with increased lymphatic density. (chiang2023reviewofthe pages 6-8)

### 2.5 Inflammation, oxidative stress, and DNA damage in precancer fields
Cutaneous field cancerization can exhibit measurable molecular changes prior to overt tumor:
- UVR can cause DNA damage directly and indirectly via ROS, inducing oxidative lesions such as **8-hydroxy-2′-deoxyguanosine (8-OHdG)**, and can upregulate **iNOS** and inflammatory responses. (camillo2024exvivoanalysis pages 1-2)
- Ex vivo analyses report **downregulation of p53**, increased proliferation markers (**Ki67**, **p16**), altered keratinocyte differentiation markers, increased **iNOS**, **IL-6**, **IL-8**, and “early signs of DNA damage… oxidative stress… abnormal cell proliferation and differentiation” in CFC tissue. (camillo2024exvivoanalysis pages 1-2)

## 3) Key molecular players (genes/proteins, pathways, cell types, anatomy, chemicals)

| Category | Item | Mechanistic Role in cSCC | Example Evidence Statement | Evidence Type | PMID(s) | Publication | URL | Citation ID |
|---|---|---|---|---|---|---|---|---|
| Driver Gene | **TP53** | Defective apoptosis and unchecked proliferation of DNA-damaged keratinocytes; early event. | "TP53 is one of the most frequently mutated driver genes in cSCC... 54–95% of cases" | Review | Not in excerpt | Hosseini et al. (2024) | [Link](https://doi.org/10.3390/cancers16162904) | (hosseini2024themutationaland pages 4-6) |
| Driver Gene | **NOTCH1/2** | Loss-of-function disrupts differentiation; found in normal skin fields. | "Loss-of-function mutated in cSCC (around 50–80%)... NOTCH1 is commonly mutated in normal skin (~20% of cells)" | Review | Not in excerpt | Hosseini et al. (2024) | [Link](https://doi.org/10.3390/cancers16162904) | (hosseini2024themutationaland pages 4-6) |
| Driver Gene | **CDKN2A** | Altered cell-cycle control; inactivation leads to unrestrained growth. | "Altered early and, when co-mutated with TP53, associates with worse outcomes and metastasis risk" | Review | Not in excerpt | Hosseini et al. (2024) | [Link](https://doi.org/10.3390/cancers16162904) | (hosseini2024themutationaland pages 4-6) |
| Driver Gene | **RAS/HRAS** | Oncogenic activation drives proliferation; cooperates with tumor suppressor loss. | "Combinatorial sequential inactivation of... Tgfbr2, Trp53 and Notch1 coupled with activation of Ras signalling" | Primary | Not in excerpt | Bailey et al. (2023) | [Link](https://doi.org/10.1038/s41467-023-40822-9) | (bailey2023drivergenecombinations pages 1-2) |
| Driver Gene | **EGFR** | Dysregulation activates Ras-Raf-MEK-ERK and PI3K pathways driving proliferation. | "EGFR dysregulation activates Ras-Raf-MEK-ERK and PI3K pathways, driving proliferation" | Review | Not in excerpt | Sol et al. (2024) | [Link](https://doi.org/10.3390/ijms25137056) | (sol2024therapeuticapproachesfor pages 2-3) |
| Pathway | **PI3K/AKT/mTOR** | Consistently activated in cSCC but not AK; mediates growth/survival. | "Consistently activated in cSCC but not in AK, implicating it in the AK→cSCC transition" | Review | Not in excerpt | Hosseini et al. (2024) | [Link](https://doi.org/10.3390/cancers16162904) | (hosseini2024themutationaland pages 4-6) |
| Pathway | **TGF-β/TGFBR2** | Tumor suppressor loss promotes progression; expression promotes immune evasion. | "Increased TGF-β... attenuat[ing] anti-tumor immune responses" | Review | Not in excerpt | Jiang et al. (2024) | [Link](https://doi.org/10.3390/cancers16101800) | (jiang2024cutaneoussquamouscell pages 1-2) |
| Driver Gene | **FAT1** | Loss promotes epithelial-mesenchymal transition (EMT), stemness, and metastasis. | "FAT1 loss promotes EMT, increasing invasion, stemness, and metastatic potential" | Review | Not in excerpt | Jiang et al. (2024) | [Link](https://doi.org/10.3390/cancers16101800) | (jiang2024cutaneoussquamouscell pages 1-2) |
| Driver Gene | **COL11A1** | Mutations alter extracellular matrix architecture to promote invasion. | "COL11A1 mutations alter extracellular matrix to promote invasion" | Review | Not in excerpt | Jiang et al. (2024) | [Link](https://doi.org/10.3390/cancers16101800) | (jiang2024cutaneoussquamouscell pages 1-2) |
| Field Marker | **iNOS, IL-6, IL-8** | Inflammatory mediators upregulated in field cancerization. | "Increased expression of iNOS and proinflammatory cytokines IL-6 and IL-8" | Primary | Not in excerpt | Camillo et al. (2024) | [Link](https://doi.org/10.3390/ijms25115775) | (camillo2024exvivoanalysis pages 1-2) |
| TME Factor | **Tregs** | Create immunosuppressive milieu; suppress effector T cells. | "Create an immunosuppressive environment by downregulating effector CD4+ and CD8+ T cells" | Review | Not in excerpt | Chiang et al. (2023) | [Link](https://doi.org/10.3390/cancers15092453) | (chiang2023reviewofthe pages 6-8) |
| TME Factor | **pDCs** | Plasmacytoid dendritic cells; reduced in cSCC, impairing anti-tumor immunity. | "Reduced plasmacytoid dendritic cells, favoring immune evasion" | Review | Not in excerpt | Jiang et al. (2024) | [Link](https://doi.org/10.3390/cancers16101800) | (jiang2024cutaneoussquamouscell pages 1-2) |
| TME Factor | **M2 TAMs / CAFs** | M2 Macs stimulate angiogenesis; CAFs secrete MMPs/VEGF. | "CAFs secrete MMPs, VEGF, and IL-6; TAMs secrete MMP-9/11" | Review | Not in excerpt | Chiang et al. (2023) | [Link](https://doi.org/10.3390/cancers15092453) | (pqac-000011) |
| Mechanism | **UV Signatures** | Specific mutations (C>T, CC>TT) caused by UVB exposure. | "C>T substitution mutations... CC>TT dinucleotide substitutions... frequent T>C substitutions" | Review | Not in excerpt | Hosseini et al. (2024) | [Link](https://doi.org/10.3390/cancers16162904) | (hosseini2024themutationaland pages 1-2) |
| Mechanism | **Field Cancerization** | Morphologically normal skin containing mutated clones (e.g. TP53, NOTCH1). | "Skin regions appearing morphologically normal but containing clones of mutated cells" | Primary | Not in excerpt | Camillo et al. (2024) | [Link](https://doi.org/10.3390/ijms25115775) | (camillo2024exvivoanalysis pages 1-2) |
| Statistic | **Mutational Burden** | High burden reflects UV etiology. | "Median mutations/Mb: cSCC 45.2" | Review | Not in excerpt | Sol et al. (2024) | [Link](https://doi.org/10.3390/ijms25137056) | (sol2024therapeuticapproachesfor pages 2-3) |
| Statistic | **AK Progression** | Rate of individual AKs becoming invasive cSCC. | "Fewer than 0.1% of individual AKs progress to cSCC" | Primary | Not in excerpt | Bailey et al. (2023) | [Link](https://doi.org/10.1038/s41467-023-40822-9) | (bailey2023drivergenecombinations pages 1-2) |
| Statistic | **Metastasis Rate** | Overall metastatic risk for primary cSCC. | "3–5% of primary cSCC may progress to life-threatening metastatic disease" | Primary | Not in excerpt | Bailey et al. (2023) | [Link](https://doi.org/10.1038/s41467-023-40822-9) | (bailey2023drivergenecombinations pages 1-2) |
| Statistic | **Nodal Metastasis** | Risk in high-stage tumors (BWH T2b/T3). | "BWH staging notes T2b and T3 have >20% risk of nodal metastases" | Review | Not in excerpt | Jiang et al. (2024) | [Link](https://doi.org/10.3390/cancers16101800) | (jiang2024cutaneoussquamouscell pages 4-5) |


*Table: This table aggregates critical genes (e.g., TP53, NOTCH1), pathways, tumor microenvironment (TME) components, and clinical statistics defining cSCC pathophysiology, derived from 2023-2024 literature.*

### 3.1 Genes/proteins (HGNC symbols; representative roles)
- **TP53**: DNA damage response/apoptosis; loss enables proliferation of damaged keratinocytes; frequently mutated in cSCC and present in fields/AK. (hosseini2024themutationaland pages 4-6, corchadocobos2023cutaneoussquamouscell pages 1-3)
- **NOTCH1/NOTCH2**: differentiation/tumor suppressor roles; frequently mutated; also found in normal sun-exposed skin. (hosseini2024themutationaland pages 4-6, hosseini2024themutationaland pages 1-2, corchadocobos2023cutaneoussquamouscell pages 1-3)
- **CDKN2A**: cell-cycle control; alterations contribute to “unrestrained cell cycling and uncontrolled cell growth.” (corchadocobos2023cutaneoussquamouscell pages 1-3)
- **RAS (incl. HRAS)**: proliferative signaling; progression can be driven by Ras activation with sequential tumor suppressor inactivation (TGFβ/TP53/NOTCH). (bailey2023drivergenecombinations pages 1-2)
- **EGFR**: downstream activation of MAPK and PI3K signaling cascades. (sol2024therapeuticapproachesfor pages 2-3)
- **PIK3CA/PTEN; AKT/mTOR**: implicated in AK→cSCC transition and growth/survival programs. (hosseini2024themutationaland pages 4-6)
- **FAT1** and **COL11A1**: invasion/EMT and ECM remodeling signals in aggressive disease. (jiang2024cutaneoussquamouscell pages 1-2)

### 3.2 Cell types (CL terms; primary involvement)
Representative cell types implicated by the TME literature include:
- **Keratinocytes** (tumor cells; CL: keratinocyte)
- **Regulatory T cells (Tregs)** (CL: regulatory T cell)
- **CD8+ T cells** (CL: CD8-positive, alpha-beta T cell)
- **Plasmacytoid dendritic cells (pDCs)** (CL: plasmacytoid dendritic cell)
- **Langerhans cells / dendritic cells** (CL: Langerhans cell; dendritic cell)
- **Tumor-associated macrophages (M2-like TAMs)** (CL: macrophage)
- **Tumor-associated neutrophils (TANs)** (CL: neutrophil)
- **Cancer-associated fibroblasts (CAFs)** (CL: fibroblast)

These are reported as functionally shaping immunosuppression, angiogenesis, ECM remodeling, and metastatic potential. (chiang2023reviewofthe pages 6-8, jiang2024cutaneoussquamouscell pages 1-2)

### 3.3 Anatomical locations (UBERON)
- **Skin / epidermis** (UBERON: skin; epidermis): primary site; sun-exposed epidermis is the initiating compartment for UV mutagenesis and field cancerization. (hosseini2024themutationaland pages 1-2, camillo2024exvivoanalysis pages 1-2)

### 3.4 Chemical entities (CHEBI; representative)
- **Reactive oxygen species (ROS)** (CHEBI: reactive oxygen species) and oxidative DNA lesions such as **8-OHdG** are implicated in UV-mediated field effects and carcinogenesis. (camillo2024exvivoanalysis pages 1-2)
- **Cytokines** (not CHEBI; protein entities) relevant to inflammatory TME states include **TGF-β, IL-6, IL-8, IL-10**. (chiang2023reviewofthe pages 6-8, jiang2024cutaneoussquamouscell pages 1-2, camillo2024exvivoanalysis pages 1-2)

## 4) Biological processes disrupted (GO-oriented)
Representative disrupted biological processes supported by cited evidence include:
- **DNA damage response** / DNA repair (UV damage; NER involvement). (hosseini2024themutationaland pages 1-2)
- **Keratinocyte differentiation / epidermis development**: suppression of differentiation programs across the continuum and shift to progenitor-like state. (bailey2023drivergenecombinations pages 1-2, bailey2023drivergenecombinations media 6aac691f)
- **Cell proliferation / cell-cycle progression**: p53 dysregulation, Ki67 upregulation in fields, CDKN2A pathway disruption. (camillo2024exvivoanalysis pages 1-2, corchadocobos2023cutaneoussquamouscell pages 1-3)
- **Inflammatory response and cytokine-mediated signaling** (IL-6/IL-8/iNOS; TGF-β-driven immune polarization). (camillo2024exvivoanalysis pages 1-2, chiang2023reviewofthe pages 6-8)
- **Extracellular matrix organization and remodeling** (CAFs, MMPs; COL11A1 effects). (chiang2023reviewofthe pages 6-8, jiang2024cutaneoussquamouscell pages 1-2)
- **Immune evasion / negative regulation of anti-tumor immunity** (Tregs, reduced antigen-presenting/DC populations, TGF-β/IL-10). (chiang2023reviewofthe pages 6-8, jiang2024cutaneoussquamouscell pages 1-2)

## 5) Cellular components (where key processes occur)
Evidence-supported cellular/anatomical compartments include:
- **Epidermal layers and keratinocyte compartments** where differentiation proceeds and is progressively disrupted along the cSCC continuum. (bailey2023drivergenecombinations pages 1-2)
- **Extracellular space / ECM** where CAF-derived MMPs/VEGF and COL11A1-linked matrix changes contribute to invasion. (chiang2023reviewofthe pages 6-8, jiang2024cutaneoussquamouscell pages 1-2)
- **Nuclear DNA** as the substrate for UV-induced mutations and oxidative DNA lesions. (hosseini2024themutationaland pages 1-2, camillo2024exvivoanalysis pages 1-2)

## 6) Disease progression model (sequence of events)
1. **Chronic UV exposure** induces DNA damage, UV-signature mutations, and oxidative stress/inflammation in sun-exposed epidermis; many mutated clones persist in clinically normal skin (field cancerization). (hosseini2024themutationaland pages 1-2, camillo2024exvivoanalysis pages 1-2)
2. **Precancer lesions** (AK; SCC in situ) arise within mutated fields; early driver events include TP53 and NOTCH alterations, with widespread clonal expansion. (bailey2023drivergenecombinations pages 1-2, hosseini2024themutationaland pages 4-6, camillo2024exvivoanalysis pages 1-2)
3. **Invasive primary cSCC** emerges through additional pathway activation and state shifts (loss of differentiation, acquisition of progenitor-like programs), including PI3K/AKT/mTOR activation relative to AK. (bailey2023drivergenecombinations pages 1-2, hosseini2024themutationaland pages 4-6)
4. **Advanced/metastatic progression** is accompanied by immune landscape remodeling and immune evasion; clinically, only a minority progress to metastasis. (bailey2023drivergenecombinations pages 1-2, hosseini2024themutationaland pages 1-2)

## 7) Phenotypic manifestations and clinicopathologic correlates
- cSCC is often curable by excision, but a subset becomes locally advanced or metastatic. (hosseini2024themutationaland pages 1-2, bailey2023drivergenecombinations pages 1-2)
- High-risk clinicopathologic features correlate with recurrence/metastasis and can be conceptualized as downstream manifestations of invasive programs and TME remodeling (e.g., deep invasion, perineural invasion, immunosuppression-associated aggressiveness). (jiang2024cutaneoussquamouscell pages 4-5, chiang2023reviewofthe pages 6-8)

## 8) Recent developments (prioritizing 2023–2024)
### 8.1 2023 primary multi-stage transcriptomics (disease continuum)
A 2023 Nature Communications study provides a high-resolution **continuum map** across normal sun-exposed skin, AK, primary and metastatic cSCC and experimentally supports progression driven by **combinatorial sequential inactivation** of tumor suppressors (**Tgfbr2, Trp53, Notch1**) plus **Ras activation**, aligning mechanistic events with observed transcriptomic state change. (bailey2023drivergenecombinations pages 1-2)

Figures summarizing this continuum and driver patterns are shown in the study’s **Figure 1 and Figure 4** (progression signatures and oncoprint of drivers). (bailey2023drivergenecombinations media 6aac691f, bailey2023drivergenecombinations media 983dee4c)

### 8.2 2024 emphasis on “mutations in normal skin” and driver detection limits
A 2024 review emphasizes that many key drivers in cSCC are also common in normal sun-exposed skin, complicating driver identification; it provides quantitative mutation densities for NOTCH and TP53 in normal skin. (hosseini2024themutationaland pages 1-2)

### 8.3 2024 ex vivo evidence for molecularly abnormal but clinically normal fields
The 2024 field cancerization ex vivo study provides measurable biomarker changes (p53, Ki67, p16; iNOS; IL-6/IL-8; oxidative DNA damage) supporting the concept that preclinical fields contain actionable pathophysiology. (camillo2024exvivoanalysis pages 1-2)

## 9) Current applications and real-world implementations
- **Standard of care:** surgery and/or radiotherapy for most primary cSCC; systemic therapies are used for locally advanced/metastatic disease. (bailey2023drivergenecombinations pages 1-2, hosseini2024themutationaland pages 1-2)
- **Immunotherapy:** anti-PD1 checkpoint therapy is described as first-line in advanced disease, but “50% of individuals fail to respond,” underscoring the need for predictive biomarkers and combination strategies. (bailey2023drivergenecombinations pages 1-2)
- **Targeted therapy:** EGFR pathway dysregulation supports use of EGFR inhibitors, though responses may be limited. (bailey2023drivergenecombinations pages 1-2, sol2024therapeuticapproachesfor pages 2-3)
- **Field cancerization challenge:** therapies aimed at AK/SCC lesions may not eradicate mutated clones within the field, enabling recurrence and de novo lesions, motivating field-directed prevention strategies. (camillo2024exvivoanalysis pages 1-2)

## 10) Relevant statistics and data (recent sources, with context)
- **Metastatic cSCC frequency:** ~5% of cases, per a 2024 review. (hosseini2024themutationaland pages 1-2)
- **AK progression to cSCC:** “fewer than 0.1% of individual AKs will progress to cSCC,” per the 2023 Nature Communications study (reflecting current estimates). (bailey2023drivergenecombinations pages 1-2)
- **Primary cSCC to life-threatening metastasis:** estimated **3–5%**. (bailey2023drivergenecombinations pages 1-2)
- **Mutational burden:** median **~45.2 mutations/Mb** (reported for cSCC in a 2024 review). (sol2024therapeuticapproachesfor pages 2-3)
- **Nodal metastasis and mortality (historical clinical summary within a seminal review):** lymph node metastases ~4% and mortality ~2% are reported in an established review excerpt used here for mechanistic framing. (corchadocobos2023cutaneoussquamouscell pages 1-3)
- **High-risk staging statistic:** BWH T2b/T3 associated with **>20% risk of nodal metastases**. (jiang2024cutaneoussquamouscell pages 4-5)

## 11) Expert opinions / authoritative analysis (from cited sources)
- The cSCC literature increasingly frames disease biology as an **interplay of UV mutagenesis and microenvironmental/immune factors**, not solely tumor-intrinsic mutations. (hosseini2024themutationaland pages 1-2)
- The “differentiated-to-progenitor-like” axis provides an organizing principle linking keratinocyte state, inflammation, and immune escape across progression. (bailey2023drivergenecombinations pages 1-2, bailey2023drivergenecombinations pages 10-11)

## 12) Evidence items with PMIDs (limitations)
**Important limitation of this tool-based evidence set:** the retrieved full-text excerpts used here (mostly open-access reviews and one primary paper) **do not display PubMed IDs in the captured passages**, so PMIDs cannot be reliably attached to many mechanistic statements from the excerpts without introducing uncited external lookup. Accordingly, PMIDs are marked “not in excerpt” in the structured table. (sol2024therapeuticapproachesfor pages 2-3, hosseini2024themutationaland pages 1-2, jiang2024cutaneoussquamouscell pages 1-2, bailey2023drivergenecombinations pages 1-2)

---

## Appendix: Curated source list (URLs + publication dates)
- Bailey P. et al. **Driver gene combinations dictate cutaneous squamous cell carcinoma disease continuum progression.** *Nature Communications* (Accepted 2023-08-08; published 2023). https://doi.org/10.1038/s41467-023-40822-9 (bailey2023drivergenecombinations pages 1-2)
- Hosseini TM. et al. **The Mutational and Microenvironmental Landscape of Cutaneous Squamous Cell Carcinoma: A Review.** *Cancers* (Published 2024-08-21). https://doi.org/10.3390/cancers16162904 (hosseini2024themutationaland pages 1-2)
- Jiang R. et al. **Cutaneous Squamous Cell Carcinoma: An Updated Review.** *Cancers* (Published 2024-05; issue 10). https://doi.org/10.3390/cancers16101800 (jiang2024cutaneoussquamouscell pages 1-2)
- Camillo L. et al. **Ex Vivo Analysis of Cell Differentiation, Oxidative Stress, Inflammation, and DNA Damage on Cutaneous Field Cancerization.** *Int. J. Mol. Sci.* (Published 2024-05-26). https://doi.org/10.3390/ijms25115775 (camillo2024exvivoanalysis pages 1-2)
- Sol S. et al. **Therapeutic Approaches for Non-Melanoma Skin Cancer: Standard of Care and Emerging Modalities.** *Int. J. Mol. Sci.* (Published 2024-06). https://doi.org/10.3390/ijms25137056 (sol2024therapeuticapproachesfor pages 2-3)
- Chiang E. et al. **Review of the Tumor Microenvironment in Basal and Squamous Cell Carcinoma.** *Cancers* (Published 2023-04). https://doi.org/10.3390/cancers15092453 (chiang2023reviewofthe pages 6-8)


References

1. (hosseini2024themutationaland pages 1-2): Tara M. Hosseini, Soo J. Park, and Theresa W Guo. The mutational and microenvironmental landscape of cutaneous squamous cell carcinoma: a review. Cancers, 16:2904, Aug 2024. URL: https://doi.org/10.3390/cancers16162904, doi:10.3390/cancers16162904. This article has 16 citations.

2. (corchadocobos2023cutaneoussquamouscell pages 1-3): Roberto Corchado-Cobos, Natalia García-Sancha, Rogelio González-Sarmiento, Jesús Pérez-Losada, and Javier Cañueto. Cutaneous squamous cell carcinoma: from biology to therapy. International Journal of Molecular Sciences, 21:2956, Apr 2023. URL: https://doi.org/10.3390/ijms21082956, doi:10.3390/ijms21082956. This article has 270 citations.

3. (camillo2024exvivoanalysis pages 1-2): Lara Camillo, Elisa Zavattaro, Federica Veronese, Laura Cristina Gironi, Ottavio Cremona, and Paola Savoia. Ex vivo analysis of cell differentiation, oxidative stress, inflammation, and dna damage on cutaneous field cancerization. International Journal of Molecular Sciences, 25:5775, May 2024. URL: https://doi.org/10.3390/ijms25115775, doi:10.3390/ijms25115775. This article has 3 citations.

4. (bailey2023drivergenecombinations pages 1-2): Peter Bailey, Rachel A. Ridgway, Patrizia Cammareri, Mairi Treanor-Taylor, Ulla-Maja Bailey, Christina Schoenherr, Max Bone, Daniel Schreyer, Karin Purdie, Jason Thomson, William Rickaby, Rene Jackstadt, Andrew D. Campbell, Emmanouil Dimonitsas, Alexander J. Stratigos, Sarah T. Arron, Jun Wang, Karen Blyth, Charlotte M. Proby, Catherine A. Harwood, Owen J. Sansom, Irene M. Leigh, and Gareth J. Inman. Driver gene combinations dictate cutaneous squamous cell carcinoma disease continuum progression. Nature Communications, Aug 2023. URL: https://doi.org/10.1038/s41467-023-40822-9, doi:10.1038/s41467-023-40822-9. This article has 42 citations and is from a highest quality peer-reviewed journal.

5. (bailey2023drivergenecombinations media 6aac691f): Peter Bailey, Rachel A. Ridgway, Patrizia Cammareri, Mairi Treanor-Taylor, Ulla-Maja Bailey, Christina Schoenherr, Max Bone, Daniel Schreyer, Karin Purdie, Jason Thomson, William Rickaby, Rene Jackstadt, Andrew D. Campbell, Emmanouil Dimonitsas, Alexander J. Stratigos, Sarah T. Arron, Jun Wang, Karen Blyth, Charlotte M. Proby, Catherine A. Harwood, Owen J. Sansom, Irene M. Leigh, and Gareth J. Inman. Driver gene combinations dictate cutaneous squamous cell carcinoma disease continuum progression. Nature Communications, Aug 2023. URL: https://doi.org/10.1038/s41467-023-40822-9, doi:10.1038/s41467-023-40822-9. This article has 42 citations and is from a highest quality peer-reviewed journal.

6. (bailey2023drivergenecombinations media 983dee4c): Peter Bailey, Rachel A. Ridgway, Patrizia Cammareri, Mairi Treanor-Taylor, Ulla-Maja Bailey, Christina Schoenherr, Max Bone, Daniel Schreyer, Karin Purdie, Jason Thomson, William Rickaby, Rene Jackstadt, Andrew D. Campbell, Emmanouil Dimonitsas, Alexander J. Stratigos, Sarah T. Arron, Jun Wang, Karen Blyth, Charlotte M. Proby, Catherine A. Harwood, Owen J. Sansom, Irene M. Leigh, and Gareth J. Inman. Driver gene combinations dictate cutaneous squamous cell carcinoma disease continuum progression. Nature Communications, Aug 2023. URL: https://doi.org/10.1038/s41467-023-40822-9, doi:10.1038/s41467-023-40822-9. This article has 42 citations and is from a highest quality peer-reviewed journal.

7. (sol2024therapeuticapproachesfor pages 2-3): Stefano Sol, Fabiana Boncimino, Kristina Todorova, Sarah Elizabeth Waszyn, and Anna Mandinova. Therapeutic approaches for non-melanoma skin cancer: standard of care and emerging modalities. International Journal of Molecular Sciences, 25:7056, Jun 2024. URL: https://doi.org/10.3390/ijms25137056, doi:10.3390/ijms25137056. This article has 35 citations.

8. (hosseini2024themutationaland pages 4-6): Tara M. Hosseini, Soo J. Park, and Theresa W Guo. The mutational and microenvironmental landscape of cutaneous squamous cell carcinoma: a review. Cancers, 16:2904, Aug 2024. URL: https://doi.org/10.3390/cancers16162904, doi:10.3390/cancers16162904. This article has 16 citations.

9. (jiang2024cutaneoussquamouscell pages 1-2): Rina Jiang, Mike Fritz, and Syril Keena T. Que. Cutaneous squamous cell carcinoma: an updated review. Cancers, 16:1800, May 2024. URL: https://doi.org/10.3390/cancers16101800, doi:10.3390/cancers16101800. This article has 53 citations.

10. (chiang2023reviewofthe pages 6-8): Elizabeth Chiang, Haleigh Stafford, Jane Buell, Uma Ramesh, Moran Amit, Priyadharsini Nagarajan, Michael Migden, and Dan Yaniv. Review of the tumor microenvironment in basal and squamous cell carcinoma. Cancers, 15:2453, Apr 2023. URL: https://doi.org/10.3390/cancers15092453, doi:10.3390/cancers15092453. This article has 32 citations.

11. (jiang2024cutaneoussquamouscell pages 4-5): Rina Jiang, Mike Fritz, and Syril Keena T. Que. Cutaneous squamous cell carcinoma: an updated review. Cancers, 16:1800, May 2024. URL: https://doi.org/10.3390/cancers16101800, doi:10.3390/cancers16101800. This article has 53 citations.

12. (bailey2023drivergenecombinations pages 10-11): Peter Bailey, Rachel A. Ridgway, Patrizia Cammareri, Mairi Treanor-Taylor, Ulla-Maja Bailey, Christina Schoenherr, Max Bone, Daniel Schreyer, Karin Purdie, Jason Thomson, William Rickaby, Rene Jackstadt, Andrew D. Campbell, Emmanouil Dimonitsas, Alexander J. Stratigos, Sarah T. Arron, Jun Wang, Karen Blyth, Charlotte M. Proby, Catherine A. Harwood, Owen J. Sansom, Irene M. Leigh, and Gareth J. Inman. Driver gene combinations dictate cutaneous squamous cell carcinoma disease continuum progression. Nature Communications, Aug 2023. URL: https://doi.org/10.1038/s41467-023-40822-9, doi:10.1038/s41467-023-40822-9. This article has 42 citations and is from a highest quality peer-reviewed journal.