---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-06T03:39:27.656115'
end_time: '2026-03-06T03:54:42.107252'
duration_seconds: 914.45
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
citation_count: 49
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


## Multiple Myeloma (MM) Pathophysiology Research Report (molecular & cellular mechanisms)

### Target disease
- **Disease name:** Multiple Myeloma
- **MONDO ID:** Not retrieved in provided sources.
- **Disease category:** Complex hematologic malignancy.

### Evidence caveat (PMIDs)
The retrieved full-text excerpts predominantly contained DOIs/URLs and did not consistently expose PMIDs. Where PMIDs were not present in the excerpts, mechanistic claims are cited to the retrieved sources (with DOI/URL) and the internal evidence IDs.

---

## 1) Key concepts and definitions (current understanding)

Multiple myeloma is a clonal plasma-cell malignancy of the bone marrow and is clinically defined by tumor burden plus end-organ damage, commonly summarized as **CRAB** (hyperCalcemia, Renal dysfunction, Anemia, Bone disease). In a recent review, MM is described as “characterized by osteolytic bone lesions, anemia, hypercalcemia, renal failure, and the accumulation of malignant plasma cells.” (Lu et al., *Molecular Biomedicine*, **July 2024**, https://doi.org/10.1186/s43556-024-00188-w) (lu2024multiplemyelomasignaling pages 1-2)

MM typically evolves along a **biologic continuum** from precursor states **MGUS → SMM → symptomatic MM**, with an annual progression risk from MGUS of approximately **~1% per year**, and multistep genomic/epigenomic changes plus microenvironmental immune escape driving transformation. (Wang et al., *Frontiers in Immunology*, **Feb 2024**, https://doi.org/10.3389/fimmu.2024.1346211) (wang2024differentevasionstrategies pages 1-2)

A central current concept is that MM is not solely a tumor-cell intrinsic genomic disease, but a **bone-marrow-ecosystem disease**, in which malignant plasma cells (PCs) depend on and remodel the bone marrow microenvironment (BMME)—including stromal, immune, vascular, and bone lineages—to promote survival, immune evasion, bone destruction, and therapy resistance. (wang2024differentevasionstrategies pages 1-2, bhowmick2024pathwaystotherapy pages 13-15, xue2024tgfβanactive pages 1-2)

---

## 2) Core pathophysiology: primary mechanisms and dysregulated pathways

### 2.1 Bone marrow niche dependence and reciprocal signaling
The **interaction between MM cells and the bone marrow microenvironment** is repeatedly emphasized as mechanistically causal. For example, a 2024 review states that “The pathogenesis of MM involves the interaction between MM cells and the bone marrow microenvironment through soluble cytokines and cell adhesion molecules,” which activates key oncogenic pathways and promotes drug resistance. (Lu et al., **Jul 2024**) (lu2024multiplemyelomasignaling pages 1-2)

Microenvironmental “sheltering” is linked to drug resistance: the BMME provides “growth and survival signals” and “the niche’s residents and richness in growth and survival signals are important for myeloma progression, survival, and resistance to therapy.” (Bhowmick et al., *Heliyon*, **Jun 2024**, https://doi.org/10.1016/j.heliyon.2024.e33091) (bhowmick2024pathwaystotherapy pages 13-15)

### 2.2 Canonical dysregulated signaling networks
A 2024 synthesis identifies the core dysregulated signaling pathways as **PI3K/AKT/mTOR, RAS/MAPK, JAK/STAT, Wnt/β-catenin, and NF-κB**, stating that “Aberrant activation of these pathways contributes to the proliferation, survival, migration, and drug resistance of myeloma cells.” (Lu et al., **Jul 2024**) (lu2024multiplemyelomasignaling pages 1-2)

A mechanistic and clinically relevant genomic correlate is the high prevalence of RAS-pathway activation; Lu et al. report that RAS pathway mutations “present in 23–54% with a new diagnosis, but it increases to 45–81% in RRMM patients,” consistent with selection of MAPK-driven clones during disease evolution. (Lu et al., **Jul 2024**) (lu2024multiplemyelomasignaling pages 4-6)

**Visual evidence:** Lu et al. Figure 1 provides an integrated schematic of the PI3K/AKT/mTOR, RAS/MAPK, JAK/STAT, Wnt/β-catenin, and NF-κB pathways in MM pathogenesis. (lu2024multiplemyelomasignaling media f4696af9)

---

## 3) Key molecular players (genes/proteins), cell types, and anatomical locations

### 3.1 Tumor-cell intrinsic genetic drivers and high-risk lesions
Recent syntheses and single-cell reviews highlight initiating **IgH translocations (14q32)** that deregulate oncogenes such as **FGFR3, NSD2, CCND1/3, MAF/MAFB**, plus secondary copy-number and structural events (e.g., **gain(1q), del(17p)/TP53, MYC translocations**) that drive aggressive evolution and therapy resistance. (li2025multiplemyelomainsights pages 5-7, moscvin2023dissectingmolecularmechanisms pages 1-3)

### 3.2 Immune microenvironment dysfunction and immune escape
Immune escape is driven by a combination of:
- Expanded suppressive myeloid lineages (**MDSCs**, macrophage polarization),
- T-cell exhaustion/checkpoint expression,
- Immunosuppressive cytokines (notably **TGF-β**), and
- Tumor-mediated antigen and antigen-presentation alterations.

Moscvin et al. summarize that the MM immune ecosystem shows “marked dysfunction and skewing towards a tolerant environment” with increased **MDSCs**, M2-like macrophages, and lymphoid skewing toward **Th17 and Treg** with inhibition of cytotoxic T cells. (Moscvin et al., *J Cancer Metastasis Treat*, **May 2023**, https://doi.org/10.20517/2394-4722.2022.110) (moscvin2023dissectingmolecularmechanisms pages 1-3)

In addition, Botta et al. show at single-cell resolution that large T-cell clones in MM “expressed multiple immune checkpoints,” suggesting dysfunction; dual checkpoint targeting “PD-1 + LAG3 or PD-1 + TIGIT partially restored their function in mice.” (Botta et al., *Nature Communications*, **Sep 2023**, https://doi.org/10.1038/s41467-023-41562-6) (botta2023largetcell pages 1-2)

### 3.3 TGF-β as an immune-metabolic and bone remodeling hub (2024)
A focused 2024 review frames TGF-β as a pivotal cytokine in MM’s immune and metabolic microenvironment: it “controls various cells’ fates and influences numerous metabolic pathways, including inhibiting immune cells to infiltrate the tumors… facilitating more immunosuppressive cells, enhancing glucose and glutamine metabolism, dysregulating bone metabolism.” (Xue & Wei, *Annals of Hematology*, **Jun 2024**, https://doi.org/10.1007/s00277-024-05843-4) (xue2024tgfβanactive pages 1-2)

### 3.4 Core cell types and anatomical sites
- **Primary tissue niche:** bone marrow (BMME). (bhowmick2024pathwaystotherapy pages 13-15, lu2024multiplemyelomasignaling pages 1-2)
- **Key cell types:** malignant plasma cells; bone marrow stromal/mesenchymal stromal cells; osteoclasts/osteoblasts; T cells (especially exhausted CD8+ subsets); NK cells; suppressive myeloid lineages (MDSCs, macrophages). (moscvin2023dissectingmolecularmechanisms pages 1-3, xue2024tgfβanactive pages 1-2, botta2023largetcell pages 2-3)

---

## 4) Biological processes disrupted (GO-oriented) and cellular components

### 4.1 Disrupted biological processes (examples suitable for GO annotation)
Evidence supports disruption of:
- **Cell adhesion and microenvironment-mediated drug resistance** (CAM-DR) (bhowmick2024pathwaystotherapy pages 13-15, fotiou2025frombiologyto pages 2-4)
- **NF-κB signaling** driving survival and resistance (cui2024identificationoftherapyinduced pages 1-2)
- **PI3K-Akt signaling** downstream of cytokines and tumor-stroma interactions (lu2024multiplemyelomasignaling pages 2-4)
- **Immune checkpoint signaling / T-cell exhaustion programs** (PD-1, TIGIT, TOX) (botta2023largetcell pages 1-2, botta2023largetcell pages 2-3)
- **Fatty-acid oxidation** and broader metabolic rewiring in resistant minimal residual clones (cui2024identificationoftherapyinduced pages 1-2)
- **Angiogenesis** via myeloma exosomes and VEGF-centric mechanisms (xue2024tgfβanactive pages 2-4)

### 4.2 Cellular components (GO-CC oriented; high-level)
The mechanistic processes occur across:
- **Plasma membrane and immunological synapse** (T-cell redirection; antigen loss; checkpoint interactions). (letouze2024mechanismsofresistance pages 1-2, botta2023largetcell pages 1-2)
- **Nucleus / transcriptional programs** (NF-κB pathway activation; exhaustion transcription factors). (botta2023largetcell pages 2-3, cui2024identificationoftherapyinduced pages 1-2)
- **Extracellular space / ECM** (cytokines, TGF-β; exosomes; stromal remodeling). (xue2024tgfβanactive pages 1-2, xue2024tgfβanactive pages 2-4)

---

## 5) Disease progression and sequence of events (mechanistic staging)

### 5.1 MGUS → SMM → symptomatic MM
- MGUS to MM progression risk is ~**1% per year**, and the disease follows a “multi-step” evolution from MGUS to SMM to symptomatic MM with organ damage. (Wang et al., **Feb 2024**) (wang2024differentevasionstrategies pages 1-2)
- Symptomatic MM manifests CRAB features (anemia, osteolytic bone disease, hypercalcemia, renal impairment). (wang2024differentevasionstrategies pages 1-2, lu2024multiplemyelomasignaling pages 1-2)

### 5.2 Relapse and therapy-driven clonal evolution
Single-cell profiling of paired diagnosis and post-treatment BM samples demonstrates therapy-driven trajectories and resistance programming. Cui et al. report three post-treatment trajectories and explicitly highlight metabolic and pathway shifts: “We noted a metabolic shift toward fatty acid oxidation in cycling-resistant PCs, whereas selective PCs favored the NF-κB pathway.” (Cui et al., *Clinical Cancer Research*, **Jun 2024**, https://doi.org/10.1158/1078-0432.ccr-24-0545) (cui2024identificationoftherapyinduced pages 1-2)

### 5.3 Extramedullary myeloma (EMM) as an advanced progression phenotype
EMM is described as an aggressive form in which “malignant PCs become independent of the BM microenvironment and infiltrate other tissues and organs, creating soft tissue tumors,” and is associated with treatment resistance. (Jelinek et al., *Leukemia*, **Mar 2024**, https://doi.org/10.1038/s41375-024-02206-w) (jelinek2024beyondthemarrow pages 1-2)

A major recent genomic finding is the co-occurrence of **1q21 gain/amplification with MAPK pathway mutations** in **79%** of EMM samples, with a prognostic risk signal: patients with **mutated KRAS + 1q21 gain/amplification** at diagnosis have increased EMM risk (**HR = 2.4, p = 0.011**). (Jelinek et al., **Mar 2024**) (jelinek2024beyondthemarrow pages 1-2)

---

## 6) Phenotypic manifestations (clinical phenotypes) linked to mechanisms

### 6.1 CRAB phenotypes
CRAB phenotypes arise from tumor burden plus bone, kidney, and hematopoietic disruption. MM is clinically associated with “CRAB criteria… Calcium elevation (C), Renal dysfunction (R), Anemia (A), and Bone disease (B).” (Lu et al., **Jul 2024**) (lu2024multiplemyelomasignaling pages 1-2)

### 6.2 Bone disease and osteolysis
TGF-β and stromal signaling contribute to osteolytic remodeling; for example, BMSCs can drive osteolytic programs (including DKK1-associated effects) while creating an immunosuppressive microenvironment. (xue2024tgfβanactive pages 1-2)

---

## 7) Recent developments (prioritize 2023–2024) and authoritative expert synthesis

### 7.1 Signaling and targeted therapy (2024)
Lu et al. (2024) consolidate the pathway-centric view and therapeutic implications: the key signaling pathways “play crucial roles in promoting the proliferation, migration, expansion, survival, and drug resistance of malignant clones in MM,” supporting ongoing efforts to rationally combine pathway inhibitors with backbone regimens. (Lu et al., **Jul 2024**) (lu2024multiplemyelomasignaling pages 1-2)

### 7.2 Immune dysfunction and checkpoint-expressing clonotypes (2023)
Botta et al. provide direct single-cell evidence that TCR diversity is reduced and large T-cell clones in MM are checkpoint-rich and potentially exhausted; they report significant TCR diversity differences (e.g., Chao1 diversity index significantly higher in healthy vs MGUS/SMM vs MM). (Botta et al., **Sep 2023**) (botta2023largetcell pages 1-2)

### 7.3 Resistance biology in T-cell–redirecting therapy era (2024)
Letouzé et al. emphasize the clinical magnitude of resistance: “primary resistance occurs in about one-third of patients with RRMM.” (Letouzé et al., *Blood Advances*, **Jun 2024**) (letouze2024mechanismsofresistance pages 1-2)

Mechanistically, resistance includes tumor-intrinsic antigen loss (deletions, point mutations, epigenetic silencing), loss of MHC class I, and tumor-extrinsic immunosuppressive microenvironment and exhausted T-cell clones. (letouze2024mechanismsofresistance pages 1-2, letouze2024mechanismsofresistance pages 2-3)

---

## 8) Current applications and real-world implementations

### 8.1 MRD as a disease biology readout and clinical target
Cui et al. describe a shift in treatment goals “from achieving complete response… to realizing undetectable minimal residual disease (MRD−) status,” monitored with “next-generation flow (NGF) or next-generation sequencing technologies,” and note NGF sensitivity thresholds in the **10^-5 to 10^-6** range (depending on viable nucleated cells captured). (Cui et al., **Jun 2024**) (cui2024identificationoftherapyinduced pages 1-2, cui2024identificationoftherapyinduced pages 2-3)

### 8.2 T-cell redirecting immunotherapies (bispecific antibodies, CAR-T)
Letouzé et al. provide contemporary clinical efficacy benchmarks (heavily pretreated populations) that drive real-world adoption:
- ide-cel ORR **73%**, median PFS **8.8 months**
- cilta-cel ORR **97.9%**, median PFS **34.5 months**
- teclistamab ORR **63%**, median PFS **11.3 months**
- elranatamab ORR **61%**, median PFS ~**15 months**
- talquetamab ORR **72%**, median PFS **14 months** (n=145)
(Letouzé et al., **Jun 2024**) (letouze2024mechanismsofresistance pages 1-2)

The same review details actionable resistance mechanisms (e.g., **biallelic TNFRSF17/BCMA inactivation in 6/14**, 42.8% among progressors on BCMA-TCEs) that motivate tumor and immune-environment monitoring and rational sequencing. (letouze2024mechanismsofresistance pages 1-2)

### 8.3 Extramedullary disease risk stratification and target expression loss
Jelinek et al. report reduced expression of therapeutic targets (CD38, SLAMF7, GPRC5D, FCRH5) and downregulation of CXCR4 in EMM, potentially explaining diminished immunotherapy efficacy, and they propose EZH2 and CD70 as possible future targets. (Jelinek et al., **Mar 2024**) (jelinek2024beyondthemarrow pages 1-2)

---

## 9) Structured knowledge-base style annotations (genes, GO/CL/UBERON/HP/CHEBI)

The following embedded tables provide structured annotations suitable for a disease knowledge base.

| Pathway / Mechanism | Upstream Triggers | Key Genes/Proteins | Core Cellular Effects (GO Processes) | Evidence Quote | Source |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **PI3K/AKT/mTOR** | Soluble cytokines (e.g., IL-6), cell adhesion (BMSC interaction) | *PIK3CA*, *AKT1*, *MTOR*, *IGF1* | Cell proliferation, cell migration, negative regulation of apoptotic process, drug resistance | "Aberrant activation of these pathways contributes to the proliferation, survival, migration, and drug resistance of myeloma cells" (lu2024multiplemyelomasignaling pages 1-2) | Lu et al. 2024, *Mol Biomed* [URL](https://doi.org/10.1186/s43556-024-00188-w) |
| **RAS/MAPK** | Oncogenic mutations (KRAS/NRAS), growth factors | *KRAS*, *NRAS*, *BRAF*, *MAPK1* | Cell proliferation, survival, extramedullary progression | "We observed the co-occurrence of 1q21 gain/amplification and MAPK pathway mutations in 79% of EMM samples, suggesting that these are crucial mutational events in EMM development." (jelinek2024beyondthemarrow pages 1-2) | Jelinek et al. 2024, *Leukemia* [URL](https://doi.org/10.1038/s41375-024-02206-w) |
| **NF-κB** | Therapy selective pressure, TME interaction | *NFKB1*, *RELA*, *TNFRSF17* | Cell survival, therapeutic resistance, clonal evolution | "Selective [resistant] PCs favored the NF-κB pathway... Targeting therapy-induced resistance mechanisms may help to avert refractory disease" (cui2024identificationoftherapyinduced pages 1-2) | Cui et al. 2024, *Clin Cancer Res* [URL](https://doi.org/10.1158/1078-0432.ccr-24-0545) |
| **TGF-β Signaling** | Secretion by BMSCs, TME components | *TGFB1*, *DKK1*, *IL6* | Immune system process (suppression), bone remodeling, metabolic reprogramming | "TGF-β... controls various cells’ fates... including inhibiting immune cells to infiltrate the tumors... enhancing glucose and glutamine metabolism" (xue2024tgfβanactive pages 1-2) | Xue & Wei 2024, *Ann Hematol* [URL](https://doi.org/10.1007/s00277-024-05843-4) |
| **T-Cell Exhaustion / Checkpoints** | Chronic antigen exposure, TME interactions | *PDCD1*, *TIGIT*, *LAG3*, *TOX* | T cell exhaustion, immune response regulation, immune evasion | "Large T cell clones from patients with MM expressed multiple immune checkpoints... Dual targeting of PD-1 + LAG3 or PD-1 + TIGIT partially restored their function" (botta2023largetcell pages 1-2) | Botta et al. 2023, *Nat Commun* [URL](https://doi.org/10.1038/s41467-023-41562-6) |
| **Antigen Loss (Tumor-Intrinsic)** | Immunotherapy selective pressure (TCEs, CAR-T) | *TNFRSF17* (BCMA), *GPRC5D* | Immune evasion, drug resistance | "Resistance can arise from tumor-intrinsic... mechanisms... leading to the loss of the target antigen, such as... point mutations [in TNFRSF17], or epigenetic silencing [of GPRC5D]" (letouze2024mechanismsofresistance pages 1-2) | Letouzé et al. 2024, *Blood Adv* [URL](https://doi.org/10.1182/bloodadvances.2023012354) |
| **MDSC-Mediated Suppression** | MM-secreted CCL5, MIF | *ARG1*, *NOS2*, *CCL5* | T cell inhibition, production of reactive oxygen species, osteoclast differentiation | "MDSCs... suppress antitumor immunity via arginase-driven L-arginine depletion (causing CD3 ζ chain impairment), ROS and NO production" (moscvin2023dissectingmolecularmechanisms pages 3-4) | Moscvin et al. 2023, *J Cancer Metastasis Treat* [URL](https://doi.org/10.20517/2394-4722.2022.110) |
| **Metabolic Adaptation** | Therapy selective pressure (e.g. proteasome inhibitors) | *CPT1A* (implied for fatty acid oxidation) | Fatty acid oxidation, metabolic process, drug resistance | "We noted a metabolic shift toward fatty acid oxidation in cycling-resistant PCs" (cui2024identificationoftherapyinduced pages 1-2) | Cui et al. 2024, *Clin Cancer Res* [URL](https://doi.org/10.1158/1078-0432.ccr-24-0545) |


*Table: This table summarizes key signaling and immune pathways involved in multiple myeloma pathophysiology, highlighting upstream triggers, key genes, and cellular effects based on 2023-2024 literature.*

| Category | Entity Name | Ontology ID (approx) | Role in MM Pathophysiology | Evidence (Quote & Context) |
| :--- | :--- | :--- | :--- | :--- |
| **Gene** | *TNFRSF17* (BCMA) | HGNC:11913 | Target for immunotherapy; loss confers resistance | "Tumor-intrinsic resistance involves... loss of the target antigen... biallelic TNFRSF17 inactivation" (letouze2024mechanismsofresistance pages 1-2) |
| **Gene** | *GPRC5D* | HGNC:4501 | Target for bispecifics; silenced by epigenetic/genetic events | "Genetic or epigenetic inactivation of GPRC5D... leading to the complete loss of GPRC5D protein" (letouze2024mechanismsofresistance pages 2-3) |
| **Gene** | *TP53* | HGNC:11998 | High-risk driver; deletion promotes progression | "Chromosome 17 aneuploidy and TP53 deletion are associated with poor prognosis" (li2025multiplemyelomainsights pages 18-20) |
| **Gene** | *KRAS* | HGNC:6407 | Oncogenic driver; activates MAPK pathway | "Patients with mutated KRAS and 1q21 gain... have a significantly higher risk of EMM development" (jelinek2024beyondthemarrow pages 1-2) |
| **Gene** | *FGFR3* | HGNC:3690 | Oncogene; overexpressed in t(4;14) translocations | "IgH chromosomal translocations... deregulate oncogenes... FGFR3, NSD2" (li2025multiplemyelomainsights pages 5-7) |
| **Gene** | *NSD2* (WHSC1) | HGNC:12766 | Epigenetic modifier; t(4;14) partner | "NSD2 drives t(4;14) myeloma cell dependence on adenylate kinase 2" (li2025multiplemyelomainsights pages 18-20) |
| **Gene** | *DKK1* | HGNC:2890 | Inhibits osteoblastogenesis; causes bone lesions | "BMSCs secrete TGF-β, promoting myeloma cell survival and osteolytic bone diseases by expressing Dkk1" (xue2024tgfβanactive pages 1-2) |
| **Gene** | *PDCD1* (PD-1) | HGNC:8760 | Immune checkpoint; T-cell exhaustion marker | "Large T cell clones from patients with MM expressed multiple immune checkpoints [including PD-1]" (botta2023largetcell pages 1-2) |
| **Gene** | *TOX* | HGNC:11982 | Transcription factor driving T-cell exhaustion | "Potentially exhausted CD8+ TOX+ T cells... uniquely detected in the BM of MM patients" (botta2023largetcell pages 2-3) |
| **Cell Type** | Plasma cell | CL:0000786 | Malignant cell of origin | "Clonal proliferation of malignant plasma cells within bone marrow" (fotiou2025frombiologyto pages 2-4) |
| **Cell Type** | Bone marrow stromal cell | CL:0002563 | Niche support; secretes cytokines/adhesion factors | "Interaction between myeloma cells and BMSCs is central to MM progression and organ damage" (xue2024tgfβanactive pages 2-4) |
| **Cell Type** | Myeloid-derived suppressor cell | CL:0000775 | Suppresses anti-tumor immunity | "MM myeloid compartment is characterized by myeloid-derived suppressor cells... that promote immune evasion" (moscvin2023dissectingmolecularmechanisms pages 1-3) |
| **Cell Type** | CD8+ T cell | CL:0000625 | Cytotoxic effector; becomes exhausted/dysfunctional | "Inhibition of CD8+ cytotoxic... T cells... skewing towards a tolerant environment" (moscvin2023dissectingmolecularmechanisms pages 1-3) |
| **Cell Type** | Osteoclast | CL:0000092 | Mediate bone destruction | "Inhibiting TAK1... inhibits osteoclast (OC) genesis... and may revive osteoblastic activity" (xue2024tgfβanactive pages 1-2) |
| **Anatomy** | Bone marrow | UBERON:0002371 | Primary tumor niche; sanctuary site | "The sheltering effect of the bone marrow microenvironment to multiple myeloma cells" (bhowmick2024pathwaystotherapy pages 13-15) |
| **Anatomy** | Extramedullary site | UBERON:0000000 | Site of aggressive, independent progression | "Malignant PCs become independent of the BM microenvironment and infiltrate other tissues... creating soft tissue tumors" (jelinek2024beyondthemarrow pages 1-2) |
| **Phenotype** | Osteolytic bone lesion | HP:0002791 | Bone destruction due to OC/OB imbalance | "Characterized by osteolytic bone lesions... and the accumulation of malignant plasma cells" (lu2024multiplemyelomasignaling pages 1-2) |
| **Phenotype** | Hypercalcemia | HP:0003072 | CRAB criteria symptom | "Symptoms of MM are diverse but typically include elevated blood calcium... and bone destruction (CRAB)" (xue2024tgfβanactive pages 1-2) |
| **Phenotype** | Renal insufficiency | HP:0000083 | CRAB criteria symptom | "Symptoms... include elevated blood calcium, renal insufficiency, anemia" (xue2024tgfβanactive pages 1-2) |
| **Phenotype** | Anemia | HP:0001903 | CRAB criteria symptom | "Symptoms... include... anemia, and bone destruction" (xue2024tgfβanactive pages 1-2) |
| **Process** | Cell adhesion | GO:0007155 | Mediates drug resistance (CAM-DR) | "Cell adhesion–mediated drug resistance (CAM-DR) via adhesion molecules... supports survival" (fotiou2025frombiologyto pages 2-4) |
| **Process** | Fatty acid oxidation | GO:0019395 | Metabolic shift in resistant cells | "We noted a metabolic shift toward fatty acid oxidation in cycling-resistant PCs" (cui2024identificationoftherapyinduced pages 1-2) |
| **Process** | Angiogenesis | GO:0001525 | Induced by tumor; supports growth | "Exosomes from murine myeloma... boost angiogenesis and endothelial cell proliferation" (xue2024tgfβanactive pages 2-4) |
| **Process** | NF-kappaB signaling | GO:0043122 | Survival pathway; activated in resistant clones | "Selective PCs favored the NF-κB pathway" (cui2024identificationoftherapyinduced pages 1-2) |
| **Process** | PI3K-Akt signaling | GO:0042976 | Pro-survival pathway; cytokine activated | "Interaction... leads to the activation of... PI3K/AKT/mTOR... promoting the growth" (lu2024multiplemyelomasignaling pages 2-4) |
| **Drug** | Teclistamab | CHEBI:149567 | Bispecific antibody (BCMAxCD3) | "Teclistamab... targeting CD3 on T cells and BCMA on myeloma cells... approved for... RRMM" (letouze2024mechanismsofresistance pages 1-2) |
| **Drug** | Talquetamab | CHEBI:192667 | Bispecific antibody (GPRC5DxCD3) | "Talquetamab, another bispecific TCE targeting GPRC5D, has also been approved" (letouze2024mechanismsofresistance pages 1-2) |
| **Drug** | Bortezomib | CHEBI:31306 | Proteasome inhibitor | "BMSCs protect myeloma cells from bortezomib induced apoptosis" (bhowmick2024pathwaystotherapy pages 13-15) |


*Table: A structured mapping of key genes, cells, tissues, phenotypes, and processes involved in Multiple Myeloma to standard ontology categories, supported by recent (2023-2024) literature evidence.*

| Topic | Study Type | Key Quantitative Findings | Mechanistic Takeaway | Citation Details | Publication Date | Evidence Context ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Bispecific Antibody Resistance** | Review / Clinical Analysis | Primary resistance ~33% in RRMM; Biallelic *TNFRSF17* (BCMA) inactivation in 42.8% (6/14) of progressors; Talquetamab ORR 72% (n=145). | Resistance driven by tumor-intrinsic antigen loss (mutations/deletions) and extrinsic immune suppression (T-cell exhaustion). | Letouzé et al., *Blood Adv* [URL](https://doi.org/10.1182/bloodadvances.2023012354) | Jun 2024 | (letouze2024mechanismsofresistance pages 1-2) |
| **Signaling Pathways** | Review / Meta-analysis | *RAS* mutations prevalence: 23-54% in newly diagnosed vs. 45-81% in relapsed/refractory MM. | PI3K/AKT/mTOR and RAS/MAPK pathways are central to proliferation/survival; *RAS* mutations increase with disease progression. | Lu et al., *Mol Biomed* [URL](https://doi.org/10.1186/s43556-024-00188-w) | Jul 2024 | (lu2024multiplemyelomasignaling pages 4-6, lu2024multiplemyelomasignaling pages 1-2) |
| **T-Cell Exhaustion** | scRNA-seq / Flow Cytometry | TCR diversity significantly lower in MM vs. healthy (Chao1 index: 185 vs. 338, p=0.014). Large clones ratio CD4:CD8 shifts 1:1.2 → 1:2.1. | Large T-cell clones in MM are dysfunctional, expressing multiple checkpoints (PD-1, TIGIT) and showing exhaustion features. | Botta et al., *Nat Commun* [URL](https://doi.org/10.1038/s41467-023-41562-6) | Sep 2023 | (botta2023largetcell pages 1-2) |
| **Disease Progression** | Epidemiology Review | MGUS prevalence ~3-4% (>50yo), progression risk ~1%/yr. SMM progression risk ~10-15%/yr. | Progression from MGUS/SMM to MM is driven by genetic accumulation (e.g., *KRAS*, *TP53*) and microenvironmental support. | Larasati et al., *J La Medihealtico* [URL](https://doi.org/10.37899/journallamedihealtico.v6i3.2139) | Jul 2025 | (larasati2025fromsilentclones pages 3-5, larasati2025fromsilentclones pages 1-3) |
| **Extramedullary Disease** | Genomic Analysis (WES/RNA-seq) | Co-occurrence of 1q21 gain & MAPK pathway mutations in 79% of EMM samples. Risk HR=2.4 for EMM with *KRAS*+1q21. | EMM evolution involves specific genetic co-occurrences allowing independence from the bone marrow niche and therapy resistance. | Jelinek et al., *Leukemia* [URL](https://doi.org/10.1038/s41375-024-02206-w) | Mar 2024 | (jelinek2024beyondthemarrow pages 1-2) |
| **Clonal Evolution** | scRNA-seq | Identified 3 post-treatment trajectories: clonal elimination, stabilization, and selection. | Therapy selects for resistant subclones exhibiting metabolic shifts (fatty acid oxidation) and NF-κB pathway activation. | Cui et al., *Clin Cancer Res* [URL](https://doi.org/10.1158/1078-0432.ccr-24-0545) | Jun 2024 | (cui2024identificationoftherapyinduced pages 1-2) |
| **Genomic Complexity** | Multi-omics Review | Chemotherapy associated with >20% of nonsynonymous mutations in relapsed tumors. | Therapeutic pressure accelerates genomic complexity and clonal evolution, contributing to relapse and refractoriness. | Gong et al., *Cancers* [URL](https://doi.org/10.3390/cancers16030498) | Jan 2024 | (gong2024novelinsightsinto pages 10-12) |


*Table: This table summarizes pivotal quantitative data points and mechanistic insights from recent high-impact studies, covering therapy resistance, signaling dysregulation, immune evasion, and disease progression statistics.*

---

## 10) Expert interpretation (integrated analysis)

Across 2023–2024 evidence, MM progression can be interpreted as the convergence of:
1) **Early/initiating genomic lesions** (IgH translocations/hyperdiploidy),
2) **Secondary driver acquisition** (CNVs including 1q gain; TP53 loss; MAPK pathway lesions),
3) **Bone marrow niche co-option**, including cytokine and adhesion signaling that activates PI3K/AKT/mTOR, JAK/STAT, and NF-κB and drives CAM-DR, and
4) **Immune editing toward escape**, including MDSC expansion, T-cell checkpoint/exhaustion programs, and immunosuppressive cytokines like TGF-β,
5) **Therapy-imposed selection**, leading to resistant MRD clones that exhibit transcriptional and metabolic adaptations (e.g., fatty acid oxidation; NF-κB preference), and
6) In some patients, a transition toward **extramedullary independence**, exemplified by 1q21+MAPK co-occurrence and altered chemokine/target expression.

This framework is directly supported by: pathway-centric synthesis (Lu 2024), immune escape frameworks (Wang 2024; Moscvin 2023; Botta 2023), single-cell resistance biology (Cui 2024), and EMM genomic/transcriptomic profiling (Jelinek 2024). (lu2024multiplemyelomasignaling pages 1-2, wang2024differentevasionstrategies pages 1-2, moscvin2023dissectingmolecularmechanisms pages 1-3, botta2023largetcell pages 1-2, cui2024identificationoftherapyinduced pages 1-2, jelinek2024beyondthemarrow pages 1-2)


References

1. (lu2024multiplemyelomasignaling pages 1-2): Qizhong Lu, Donghui Yang, Hexian Li, Ting Niu, and Aiping Tong. Multiple myeloma: signaling pathways and targeted therapy. Molecular Biomedicine, Jul 2024. URL: https://doi.org/10.1186/s43556-024-00188-w, doi:10.1186/s43556-024-00188-w. This article has 70 citations and is from a peer-reviewed journal.

2. (wang2024differentevasionstrategies pages 1-2): Chaofan Wang, Wanting Wang, Moran Wang, Jun Deng, Chunyan Sun, Yu Hu, and Shanshan Luo. Different evasion strategies in multiple myeloma. Frontiers in Immunology, Feb 2024. URL: https://doi.org/10.3389/fimmu.2024.1346211, doi:10.3389/fimmu.2024.1346211. This article has 25 citations and is from a peer-reviewed journal.

3. (bhowmick2024pathwaystotherapy pages 13-15): Kuntal Bhowmick, Max von Suskil, Omar S. Al-Odat, Weam Othman Elbezanti, Subash C. Jonnalagadda, Tulin Budak-Alpdogan, and Manoj K. Pandey. Pathways to therapy resistance: the sheltering effect of the bone marrow microenvironment to multiple myeloma cells. Heliyon, 10:e33091, Jun 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e33091, doi:10.1016/j.heliyon.2024.e33091. This article has 14 citations.

4. (xue2024tgfβanactive pages 1-2): Han-Yue Xue and Fang Wei. Tgf-β: an active participant in the immune and metabolic microenvironment of multiple myeloma. Annals of Hematology, 103:4351-4362, Jun 2024. URL: https://doi.org/10.1007/s00277-024-05843-4, doi:10.1007/s00277-024-05843-4. This article has 13 citations and is from a peer-reviewed journal.

5. (lu2024multiplemyelomasignaling pages 4-6): Qizhong Lu, Donghui Yang, Hexian Li, Ting Niu, and Aiping Tong. Multiple myeloma: signaling pathways and targeted therapy. Molecular Biomedicine, Jul 2024. URL: https://doi.org/10.1186/s43556-024-00188-w, doi:10.1186/s43556-024-00188-w. This article has 70 citations and is from a peer-reviewed journal.

6. (lu2024multiplemyelomasignaling media f4696af9): Qizhong Lu, Donghui Yang, Hexian Li, Ting Niu, and Aiping Tong. Multiple myeloma: signaling pathways and targeted therapy. Molecular Biomedicine, Jul 2024. URL: https://doi.org/10.1186/s43556-024-00188-w, doi:10.1186/s43556-024-00188-w. This article has 70 citations and is from a peer-reviewed journal.

7. (li2025multiplemyelomainsights pages 5-7): Sihong Li, Jiahui Liu, Madeline Peyton, Olivia Lazaro, Sean D. McCabe, Xiaoqing Huang, Yunlong Liu, Zanyu Shi, Zhiqi Zhang, Brian A Walker, and Travis S. Johnson. Multiple myeloma insights from single-cell analysis: clonal evolution, the microenvironment, therapy evasion, and clinical implications. Cancers, Feb 2025. URL: https://doi.org/10.3390/cancers17040653, doi:10.3390/cancers17040653. This article has 7 citations.

8. (moscvin2023dissectingmolecularmechanisms pages 1-3): Maria Moscvin, Benjamin Evans, and Giada Bianchi. Dissecting molecular mechanisms of immune microenvironment dysfunction in multiple myeloma and precursor conditions. Journal of cancer metastasis and treatment, May 2023. URL: https://doi.org/10.20517/2394-4722.2022.110, doi:10.20517/2394-4722.2022.110. This article has 7 citations.

9. (botta2023largetcell pages 1-2): Cirino Botta, Cristina Perez, Marta Larrayoz, Noemi Puig, Maria-Teresa Cedena, Rosalinda Termini, Ibai Goicoechea, Sara Rodriguez, Aintzane Zabaleta, Aitziber Lopez, Sarai Sarvide, Laura Blanco, Daniele M. Papetti, Marco S. Nobile, Daniela Besozzi, Massimo Gentile, Pierpaolo Correale, Sergio Siragusa, Albert Oriol, Maria Esther González-Garcia, Anna Sureda, Felipe de Arriba, Rafael Rios Tamayo, Jose-Maria Moraleda, Mercedes Gironella, Miguel T. Hernandez, Joan Bargay, Luis Palomera, Albert Pérez-Montaña, Hartmut Goldschmidt, Hervé Avet-Loiseau, Aldo Roccaro, Alberto Orfao, Joaquin Martinez-Lopez, Laura Rosiñol, Juan-José Lahuerta, Joan Blade, Maria-Victoria Mateos, Jesús F. San-Miguel, Jose-Angel Martinez Climent, and Bruno Paiva. Large t cell clones expressing immune checkpoints increase during multiple myeloma evolution and predict treatment resistance. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41562-6, doi:10.1038/s41467-023-41562-6. This article has 42 citations and is from a highest quality peer-reviewed journal.

10. (botta2023largetcell pages 2-3): Cirino Botta, Cristina Perez, Marta Larrayoz, Noemi Puig, Maria-Teresa Cedena, Rosalinda Termini, Ibai Goicoechea, Sara Rodriguez, Aintzane Zabaleta, Aitziber Lopez, Sarai Sarvide, Laura Blanco, Daniele M. Papetti, Marco S. Nobile, Daniela Besozzi, Massimo Gentile, Pierpaolo Correale, Sergio Siragusa, Albert Oriol, Maria Esther González-Garcia, Anna Sureda, Felipe de Arriba, Rafael Rios Tamayo, Jose-Maria Moraleda, Mercedes Gironella, Miguel T. Hernandez, Joan Bargay, Luis Palomera, Albert Pérez-Montaña, Hartmut Goldschmidt, Hervé Avet-Loiseau, Aldo Roccaro, Alberto Orfao, Joaquin Martinez-Lopez, Laura Rosiñol, Juan-José Lahuerta, Joan Blade, Maria-Victoria Mateos, Jesús F. San-Miguel, Jose-Angel Martinez Climent, and Bruno Paiva. Large t cell clones expressing immune checkpoints increase during multiple myeloma evolution and predict treatment resistance. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41562-6, doi:10.1038/s41467-023-41562-6. This article has 42 citations and is from a highest quality peer-reviewed journal.

11. (fotiou2025frombiologyto pages 2-4): Despina Fotiou and Eirini Katodritou. From biology to clinical practice: the bone marrow microenvironment in multiple myeloma. Journal of Clinical Medicine, 14:327, Jan 2025. URL: https://doi.org/10.3390/jcm14020327, doi:10.3390/jcm14020327. This article has 11 citations.

12. (cui2024identificationoftherapyinduced pages 1-2): Jian Cui, Xiaoyun Li, Shuhui Deng, Chenxing Du, Huishou Fan, Wenqiang Yan, Jingyu Xu, Xiaoqing Li, Tengteng Yu, Shuaishuai Zhang, Rui Lv, Weiwei Sui, Mu Hao, Xin Du, Yan Xu, Shuhua Yi, Dehui Zou, Tao Cheng, Lugui Qiu, Xin Gao, and Gang An. Identification of therapy-induced clonal evolution and resistance pathways in minimal residual clones in multiple myeloma through single-cell sequencing. Clinical Cancer Research, 30:3919-3936, Jun 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-0545, doi:10.1158/1078-0432.ccr-24-0545. This article has 7 citations and is from a highest quality peer-reviewed journal.

13. (lu2024multiplemyelomasignaling pages 2-4): Qizhong Lu, Donghui Yang, Hexian Li, Ting Niu, and Aiping Tong. Multiple myeloma: signaling pathways and targeted therapy. Molecular Biomedicine, Jul 2024. URL: https://doi.org/10.1186/s43556-024-00188-w, doi:10.1186/s43556-024-00188-w. This article has 70 citations and is from a peer-reviewed journal.

14. (xue2024tgfβanactive pages 2-4): Han-Yue Xue and Fang Wei. Tgf-β: an active participant in the immune and metabolic microenvironment of multiple myeloma. Annals of Hematology, 103:4351-4362, Jun 2024. URL: https://doi.org/10.1007/s00277-024-05843-4, doi:10.1007/s00277-024-05843-4. This article has 13 citations and is from a peer-reviewed journal.

15. (letouze2024mechanismsofresistance pages 1-2): Eric Letouzé, Philippe Moreau, Nikhil Munshi, Mehmet Samur, Stéphane Minvielle, and Cyrille Touzeau. Mechanisms of resistance to bispecific t-cell engagers in multiple myeloma and their clinical implications. Blood Advances, 8:2952-2959, Jun 2024. URL: https://doi.org/10.1182/bloodadvances.2023012354, doi:10.1182/bloodadvances.2023012354. This article has 39 citations and is from a peer-reviewed journal.

16. (jelinek2024beyondthemarrow pages 1-2): T. Jelinek, D. Zihala, T. Sevcikova, A. Anilkumar Sithara, V. Kapustova, H. Sahinbegovic, O. Venglar, L. Muronova, L. Broskevicova, S. Nenarokov, D. Bilek, T. Popkova, H. Plonkova, J. Vrana, V. Zidlik, P. Hurnik, M. Havel, M. Hrdinka, Z. Chyra, G. Stracquadanio, M. Simicek, and R. Hajek. Beyond the marrow: insights from comprehensive next-generation sequencing of extramedullary multiple myeloma tumors. Leukemia, 38:1323-1333, Mar 2024. URL: https://doi.org/10.1038/s41375-024-02206-w, doi:10.1038/s41375-024-02206-w. This article has 42 citations and is from a highest quality peer-reviewed journal.

17. (letouze2024mechanismsofresistance pages 2-3): Eric Letouzé, Philippe Moreau, Nikhil Munshi, Mehmet Samur, Stéphane Minvielle, and Cyrille Touzeau. Mechanisms of resistance to bispecific t-cell engagers in multiple myeloma and their clinical implications. Blood Advances, 8:2952-2959, Jun 2024. URL: https://doi.org/10.1182/bloodadvances.2023012354, doi:10.1182/bloodadvances.2023012354. This article has 39 citations and is from a peer-reviewed journal.

18. (cui2024identificationoftherapyinduced pages 2-3): Jian Cui, Xiaoyun Li, Shuhui Deng, Chenxing Du, Huishou Fan, Wenqiang Yan, Jingyu Xu, Xiaoqing Li, Tengteng Yu, Shuaishuai Zhang, Rui Lv, Weiwei Sui, Mu Hao, Xin Du, Yan Xu, Shuhua Yi, Dehui Zou, Tao Cheng, Lugui Qiu, Xin Gao, and Gang An. Identification of therapy-induced clonal evolution and resistance pathways in minimal residual clones in multiple myeloma through single-cell sequencing. Clinical Cancer Research, 30:3919-3936, Jun 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-0545, doi:10.1158/1078-0432.ccr-24-0545. This article has 7 citations and is from a highest quality peer-reviewed journal.

19. (moscvin2023dissectingmolecularmechanisms pages 3-4): Maria Moscvin, Benjamin Evans, and Giada Bianchi. Dissecting molecular mechanisms of immune microenvironment dysfunction in multiple myeloma and precursor conditions. Journal of cancer metastasis and treatment, May 2023. URL: https://doi.org/10.20517/2394-4722.2022.110, doi:10.20517/2394-4722.2022.110. This article has 7 citations.

20. (li2025multiplemyelomainsights pages 18-20): Sihong Li, Jiahui Liu, Madeline Peyton, Olivia Lazaro, Sean D. McCabe, Xiaoqing Huang, Yunlong Liu, Zanyu Shi, Zhiqi Zhang, Brian A Walker, and Travis S. Johnson. Multiple myeloma insights from single-cell analysis: clonal evolution, the microenvironment, therapy evasion, and clinical implications. Cancers, Feb 2025. URL: https://doi.org/10.3390/cancers17040653, doi:10.3390/cancers17040653. This article has 7 citations.

21. (larasati2025fromsilentclones pages 3-5): Anjani Larasati, Visabella Rizky, and Nida Ghitha Aulia. From silent clones to myeloma: unraveling the genetic clues behind mgus and smoldering myeloma. Journal La Medihealtico, 6:803-812, Jul 2025. URL: https://doi.org/10.37899/journallamedihealtico.v6i3.2139, doi:10.37899/journallamedihealtico.v6i3.2139. This article has 0 citations.

22. (larasati2025fromsilentclones pages 1-3): Anjani Larasati, Visabella Rizky, and Nida Ghitha Aulia. From silent clones to myeloma: unraveling the genetic clues behind mgus and smoldering myeloma. Journal La Medihealtico, 6:803-812, Jul 2025. URL: https://doi.org/10.37899/journallamedihealtico.v6i3.2139, doi:10.37899/journallamedihealtico.v6i3.2139. This article has 0 citations.

23. (gong2024novelinsightsinto pages 10-12): Lixin Gong, Lugui Qiu, and Mu Hao. Novel insights into the initiation, evolution, and progression of multiple myeloma by multi-omics investigation. Cancers, 16:498, Jan 2024. URL: https://doi.org/10.3390/cancers16030498, doi:10.3390/cancers16030498. This article has 7 citations.