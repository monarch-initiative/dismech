---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-06T15:00:41.876283'
end_time: '2026-03-06T15:28:09.004912'
duration_seconds: 1647.13
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cholesteatoma
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 57
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Cholesteatoma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Cholesteatoma**.
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
- **Disease Name:** Cholesteatoma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Cholesteatoma**.
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


## Comprehensive Research Report: Cholesteatoma Pathophysiology (molecular & cellular mechanisms)

### 1) Disease definition and key concepts (current understanding)

**Definition.** Middle ear cholesteatoma is defined by the ectopic presence and expansion of keratinizing stratified squamous epithelium in normally non-keratinizing middle-ear/mastoid spaces. Popescu et al. (2024) define it as “**the presence of keratinized stratified squamous epithelium within the cavity**,” highlighting its destructive biology and propensity for bone erosion (published Nov 2024; https://doi.org/10.3390/jcm13226791) (popescu2024comprehensivemanagementof pages 1-2).

**Core histopathologic compartments (matrix/perimatrix model).** Contemporary mechanistic models distinguish:
- **Matrix**: hyperproliferative keratinizing epithelium.
- **Peri-matrix (perimatrix)**: inflamed subepithelial granulation/connective tissue rich in fibroblasts, vessels, and immune cells.
Rolesi et al. (2023) describe cholesteatoma as having keratin lamellae content, a **hyperproliferative keratinizing matrix**, and an **inflamed peri-matrix** with stromal/inflammatory elements (published Jul 2023; https://doi.org/10.3390/jpm13081189) (rolesi2023studyofangiogenic pages 2-4, rolesi2023studyofangiogenic pages 1-2).

**Etiologic classes.** Rolesi et al. (2023) summarize two principal clinical categories: **congenital** (often presenting as a pearly white mass behind an intact tympanic membrane and theorized to arise from ectodermal rests) versus **acquired** (commonly arising from retraction pockets due to chronic inflammation/dysventilation or via epithelial ingrowth through tympanic membrane defects) (rolesi2023studyofangiogenic pages 1-2).

**Bone erosion: enzymatic and inflammatory mechanisms dominate.** In a large contemporary clinical synthesis, Popescu et al. (2024) state: “**Enzymatic lysis is considered the primary explanation**” for bone erosion, citing collagenase detection in cholesteatoma tissue/adjacent skin and hypotheses locating erosive activity in the matrix or subepithelial granulation tissue (popescu2024comprehensivemanagementof pages 1-2). Additional mechanisms (pressure effects, osteoclast activation by inflammatory mediators, chronic osteomyelitis-like changes) are also discussed (popescu2024comprehensivemanagementof pages 24-26).

### 2) Core pathophysiology: dysregulated pathways and cellular processes

#### 2.1 Keratinocyte hyperproliferation and apoptosis resistance
Cholesteatoma matrix keratinocytes display **hyperproliferation** and altered differentiation programs. In adult acquired cholesteatoma, Dambergs et al. (2023) report increased **Ki-67 (MKI67)** and **NF-κB** immunostaining in cholesteatoma compared with control skin, supporting increased proliferative signaling and survival (Feb 2023; https://doi.org/10.3390/medicina59020306) (dambergs2023morphopathogenesisofadult pages 1-2, dambergs2023morphopathogenesisofadult pages 13-14). NF-κB correlated with Ki-67 (r=0.538, p=0.017), consistent with a coordinated pro-proliferative axis (dambergs2023morphopathogenesisofadult pages 13-14).

**GO/Process mapping (examples):** epithelial cell proliferation (GO:0050673), regulation of apoptotic process (GO:0042981), NF-kappaB signaling (GO:0043123) (dambergs2023morphopathogenesisofadult pages 1-2, dambergs2023morphopathogenesisofadult pages 13-14).

#### 2.2 Inflammatory cytokine networks and the peri-matrix “reactive stroma”
Rolesi et al. (2023) and Popescu et al. (2024) emphasize that cholesteatoma aggressiveness emerges from **bidirectional signaling** between matrix keratinocytes and peri-matrix stromal/immune cells, functioning like a chronic wound-healing microenvironment (rolesi2023studyofangiogenic pages 10-12, rolesi2023studyofangiogenic pages 2-4, popescu2024comprehensivemanagementof pages 24-26).

Rolesi et al. outline a cytokine/growth-factor loop in which keratinocyte-derived cytokines (e.g., IL-1 family, IL-6/IL-8) activate fibroblasts and other peri-matrix cells, driving additional mediators (EGF, TNF, PDGF, TGF-α, KGF, GM-CSF) that reinforce epithelial proliferation, angiogenesis, and remodeling (rolesi2023studyofangiogenic pages 10-12, rolesi2023studyofangiogenic pages 2-4).

**Quantitative biomarker evidence (2023):** Rolesi et al. measured optical density (OD) signals for key pathways and found markedly increased inflammatory/proliferative markers in **pediatric acquired** cholesteatoma (rolesi2023studyofangiogenic pages 8-10, rolesi2023studyofangiogenic pages 5-8):
- **pSTAT3** highest in pediatric acquired (mean OD 125.54±4.88) vs congenital (88.51±5.97) vs adult acquired (75.49±2.72). (rolesi2023studyofangiogenic pages 8-10)
- **IL-1β** peri-matrix OD: pediatric acquired 148.68±4.07 vs adult acquired 108.44±9.47 vs congenital peri-matrix 39.12±0.93 (many comparisons p<0.001). (rolesi2023studyofangiogenic pages 8-10, rolesi2023studyofangiogenic pages 5-8)

**GO/Process mapping (examples):** cytokine-mediated signaling pathway (GO:0019221), STAT cascade (GO:0097696), chronic inflammatory response (GO:0002544) (rolesi2023studyofangiogenic pages 8-10, rolesi2023studyofangiogenic pages 5-8).

#### 2.3 ECM remodeling, protease networks, and tissue invasion
A recurring mechanistic theme is dysregulation of **matrix metalloproteinases (MMPs)** and inhibitors (TIMPs) in the perimatrix, enabling extracellular matrix turnover, granulation tissue expansion, and coupling to bone resorption.

- Dambergs et al. (2023) report numerous intercorrelations among **MMP2, MMP9, TIMP2, TIMP4** and inflammatory/angiogenic markers (dambergs2023morphopathogenesisofadult pages 10-12).
- Dambergs et al. (2024) extend this with a correlation-rich framework linking remodeling factors with inflammatory mediators and NF-κB (Mar 2024; https://doi.org/10.3390/diagnostics14060662). For example, MMP-2 (matrix) correlated with MMP-2 (perimatrix) (children r=0.803, p=0.000), with TIMP-2 (children r=0.622, p=0.001), and with SHH (children r=0.786, p=0.000), suggesting tightly coupled remodeling and developmental signaling in the cholesteatoma microenvironment (dambergs2024comparisonoftissue pages 14-15).

Popescu et al. (2024) also emphasize perimatrix collagenases/metalloproteinases as major contributors to osteolysis (popescu2024comprehensivemanagementof pages 24-26).

**GO/Process mapping (examples):** extracellular matrix disassembly (GO:0022617), collagen catabolic process (GO:0030574) (dambergs2024comparisonoftissue pages 14-15, popescu2024comprehensivemanagementof pages 24-26).

#### 2.4 Osteoclastogenesis and bone resorption signaling
Bone destruction in cholesteatoma reflects both enzymatic matrix degradation and activation of osteoclast biology.

- Popescu et al. (2024) discuss osteoclast activation in the setting of inflammation and demineralization, and note that ossicular chain destruction is common (≈80% of cases) (popescu2024comprehensivemanagementof pages 1-2).
- A mechanistic immune-cell perspective summarized in Bologa et al. (2025) describes abundant immune infiltrates (CD68+ macrophages, CD3+ T cells, CD20+ B cells) and proposes that lymphocytes/macrophages produce pro-osteolytic mediators including **RANKL (TNFSF11)** acting via **NF-κB** to drive osteoclastogenesis; mast-cell mediators may further promote osteoclast genesis (Feb 2025; https://doi.org/10.47162/rjme.65.4.24) (bologa2025biologyofrecurrent pages 4-5).

**GO/Process mapping (examples):** osteoclast differentiation (GO:0030316), bone resorption (GO:0045453) (bologa2025biologyofrecurrent pages 4-5).

#### 2.5 Angiogenesis and vascular remodeling
The perimatrix is frequently described as a vascularized, reactive compartment that supports growth and tissue destruction.

**Quantitative biomarker evidence:** Rolesi et al. (2023) report strong increases in angiogenic signaling in pediatric acquired disease (rolesi2023studyofangiogenic pages 5-8):
- **VEGF-C (VEGFC)** peri-matrix OD: pediatric acquired 190.98±11.91 vs adult acquired 105.93±4.11 vs congenital 38.16±1.88.
- **PDGFr (PDGFRA/PDGFRB; reported as PDGFr)** peri-matrix OD: pediatric acquired 227.51±9.10 vs adult acquired 94.97±4.87 vs congenital 37.34±1.64.
Rolesi et al. further state VEGF/PDGFr signals were significantly higher in acquired versus congenital cases (p<0.001), greatest at the peri-matrix level, with higher values in pediatric cohorts (rolesi2023studyofangiogenic pages 10-12).

Dambergs et al. (2023) reported VEGF correlations with TIMP-2 and NF-κB (e.g., VEGF vs TIMP-2 r=0.581, p=0.009; VEGF vs NF-κB r=0.512, p=0.025), supporting coordinated remodeling/angiogenic signaling (dambergs2023morphopathogenesisofadult pages 13-14).

**GO/Process mapping:** angiogenesis (GO:0001525), VEGF signaling pathway (GO:0048010) (rolesi2023studyofangiogenic pages 5-8, dambergs2023morphopathogenesisofadult pages 13-14).

#### 2.6 Innate immune activation and antimicrobial peptides
Dambergs et al. (2023) report significant overexpression of **human β-defensin-2 (DEFB4A; HβD-2)** (p=0.004) in cholesteatoma and strong positive correlations with IL-1 (r=0.822, p=0.000) and NF-κB (r=0.692, p=0.001), consistent with inflammatory induction of epithelial antimicrobial responses (dambergs2023morphopathogenesisofadult pages 14-15).

**GO/Process mapping:** antimicrobial humoral response (GO:0019730), innate immune response (GO:0045087) (dambergs2023morphopathogenesisofadult pages 14-15).

#### 2.7 Partial epithelial–mesenchymal transition (p-EMT) and invasive phenotype programs (2024 development)
A notable recent development is the mechanistic framing of cholesteatoma as exhibiting a **partial EMT** phenotype linked to invasion and recurrence potential.

Zeng et al. (Mar 2024; Cell Cycle; https://doi.org/10.1080/15384101.2024.2345481) report that **osteopontin (SPP1/OPN)** is elevated in cholesteatoma and drives a **partial EMT** pattern: reduced epithelial features and increased mesenchymal markers (e.g., vimentin, fibronectin) without induction of canonical full-EMT markers such as N-cadherin/α-SMA, consistent with p-EMT (zeng2024osteopontindrivenpartialepithelialmesenchymal pages 1-2).

Mechanistically, the study identifies an **AKT–ZEB2** axis as mediating OPN-driven p-EMT and pro-migratory/pro-survival keratinocyte behavior, supported by functional rescue with ZEB2 knockdown and pathway readouts (zeng2024osteopontindrivenpartialepithelialmesenchymal media 37734d41).

### 3) Key molecular players, cell types, and anatomical locations

#### 3.1 Genes/Proteins (selected, mechanistically supported)
Key molecules repeatedly implicated across 2023–2024 studies include:
- **Inflammation / signaling:** IL1B, IL1A, STAT3 (pSTAT3), TGFB1, NFKB1 (rolesi2023studyofangiogenic pages 5-8, dambergs2023morphopathogenesisofadult pages 13-14, dambergs2024comparisonoftissue pages 14-15)
- **Angiogenesis:** VEGFC, PDGFR (reported as PDGFr), VEGF signaling (rolesi2023studyofangiogenic pages 5-8, rolesi2023studyofangiogenic pages 10-12)
- **ECM remodeling:** MMP2, MMP9, TIMP2, TIMP4 (dambergs2024comparisonoftissue pages 14-15, dambergs2023morphopathogenesisofadult pages 10-12)
- **Epithelial proliferation:** MKI67, PCNA (dambergs2023morphopathogenesisofadult pages 1-2, dambergs2023morphopathogenesisofadult pages 13-14)
- **Innate immunity:** DEFB4A (HβD-2), DEFB104A (HβD-4) (dambergs2023morphopathogenesisofadult pages 14-15)
- **p-EMT/invasion:** SPP1 (OPN), AKT, ZEB2 (zeng2024osteopontindrivenpartialepithelialmesenchymal pages 1-2, zeng2024osteopontindrivenpartialepithelialmesenchymal media 37734d41)
- **Developmental signaling:** SHH (dambergs2023morphopathogenesisofadult pages 14-15, dambergs2024comparisonoftissue pages 14-15)

#### 3.2 Chemical entities / small molecules
- **MESNA (sodium 2-mercaptoethanesulfonate)** is discussed as an adjunct potentially improving residual/recurrence outcomes in surgical cholesteatoma management (Bovi 2023) (bovi2023recurrenceincholesteatoma pages 6-7).

#### 3.3 Cell types (dominant actors)
- **Keratinocytes** (matrix) as proliferative/invasive epithelium (dambergs2023morphopathogenesisofadult pages 1-2, zeng2024osteopontindrivenpartialepithelialmesenchymal pages 1-2).
- **Fibroblasts** (peri-matrix) as cytokine-responsive stromal effectors (rolesi2023studyofangiogenic pages 10-12, rolesi2023studyofangiogenic pages 2-4).
- **T lymphocytes** and other immune cells as inflammatory drivers; Popescu notes predominance of T cells on immunohistochemistry (popescu2024comprehensivemanagementof pages 24-26).
- **Macrophages** and lymphocytes implicated in RANKL-mediated osteoclastogenesis (bologa2025biologyofrecurrent pages 4-5).
- **Endothelial cells** supporting peri-matrix neovascularization (rolesi2023studyofangiogenic pages 5-8).

#### 3.4 Anatomical locations
- **Middle ear cavity and mastoid air cell system** (temporal bone) as the primary site of lesion expansion and bone erosion (popescu2024comprehensivemanagementof pages 24-26, popescu2024comprehensivemanagementof pages 1-2).
- **Ossicular chain** frequently destroyed (≈80% of cases) (popescu2024comprehensivemanagementof pages 1-2).
- **Perimatrix** as an inflammatory/angiogenic compartment linked to aggressive disease (rolesi2023studyofangiogenic pages 10-12).

### 4) Biological processes (GO) and cellular components (cellular localization)

**GO biological processes (suggested for annotation; mechanistically supported):**
- Epithelial cell proliferation (GO:0050673) (dambergs2023morphopathogenesisofadult pages 1-2)
- Cytokine-mediated signaling pathway (GO:0019221) (rolesi2023studyofangiogenic pages 10-12)
- NF-κB signaling (GO:0043123) (dambergs2023morphopathogenesisofadult pages 13-14)
- Angiogenesis (GO:0001525) (rolesi2023studyofangiogenic pages 5-8)
- Extracellular matrix disassembly (GO:0022617) (dambergs2024comparisonoftissue pages 14-15)
- Osteoclast differentiation (GO:0030316) and bone resorption (GO:0045453) (bologa2025biologyofrecurrent pages 4-5)
- Epithelial to mesenchymal transition (GO:0001837) (zeng2024osteopontindrivenpartialepithelialmesenchymal pages 1-2)
- Biofilm formation (GO:0042710) (kanodia2024metagenomeanalysisof pages 6-9)

**Cellular components (where processes occur; suggested):**
- Extracellular space / extracellular matrix (MMP/TIMP activity; collagenases) (popescu2024comprehensivemanagementof pages 24-26, dambergs2024comparisonoftissue pages 14-15)
- Plasma membrane/cytosol/nucleus (NF-κB and STAT3 activation; ZEB2 transcriptional reprogramming) (rolesi2023studyofangiogenic pages 8-10, zeng2024osteopontindrivenpartialepithelialmesenchymal media 37734d41)

### 5) Disease progression: mechanistic sequence of events

A coherent, evidence-aligned sequence (acquired cholesteatoma) is:
1. **Trigger/initiators:** chronic middle-ear inflammation and dysventilation (retraction pockets), recurrent infection, and/or epithelial ingress through tympanic membrane defects (rolesi2023studyofangiogenic pages 1-2).
2. **Matrix establishment:** keratinizing epithelium accumulates keratin debris; DWI MRI is sensitive to characteristic keratinous content (popescu2024comprehensivemanagementof pages 2-3).
3. **Perimatrix activation:** inflammatory cytokines and fibroblast/immune activation create a chronic wound-like, angiogenic stroma (rolesi2023studyofangiogenic pages 10-12).
4. **Expansion and invasion:** hyperproliferation (MKI67/NF-κB), remodeling (MMP/TIMP), and angiogenesis (VEGF/PDGFr) support growth; partial EMT programs (OPN–AKT–ZEB2) may further enhance migration and persistence (dambergs2023morphopathogenesisofadult pages 13-14, dambergs2024comparisonoftissue pages 14-15, zeng2024osteopontindrivenpartialepithelialmesenchymal media 37734d41).
5. **Bone erosion:** enzymatic lysis/collagenases, inflammatory osteoclast activation, and microenvironmental factors drive osteolysis and ossicular destruction (popescu2024comprehensivemanagementof pages 1-2, popescu2024comprehensivemanagementof pages 24-26, bologa2025biologyofrecurrent pages 4-5).
6. **Clinical sequelae and recurrence:** persistent/recurrent inflammation and biofilm-associated microbiota contribute to chronicity and recidivism; residual disease after surgery is a key driver of recurrence (popescu2024comprehensivemanagementof pages 15-18, popescu2024comprehensivemanagementof pages 24-26).

### 6) Phenotypic manifestations and mechanism-to-phenotype links

**Key clinical phenotypes** (suggested Human Phenotype Ontology [HP] mapping; examples):
- **Conductive hearing loss (HP:0000405)** due to ossicular erosion and middle-ear mass effects (ossicular destruction ≈80%) (popescu2024comprehensivemanagementof pages 1-2).
- **Otorrhea (HP:0001738)** and chronic infection-related symptoms, often influenced by persistent microbiota/biofilm (popescu2024comprehensivemanagementof pages 24-26).
- **Temporal bone osteolysis / ossicular chain destruction** (phenotype framing supported by imaging and intraoperative descriptions) (popescu2024comprehensivemanagementof pages 7-10).
- **Facial nerve palsy risk / labyrinthine fistulae / intracranial complications** (recognized complications in clinical series) (popescu2024comprehensivemanagementof pages 15-18).

### 7) Recent developments (prioritizing 2023–2024)

**(i) Partial EMT as a mechanistic driver and therapeutic target (2024).** Zeng et al. provide evidence that **OPN/SPP1** promotes keratinocyte proliferation, survival, migration, and p-EMT via **AKT–ZEB2**, and that blockade of OPN signaling improves cholesteatoma-like symptoms in a rat model (zeng2024osteopontindrivenpartialepithelialmesenchymal pages 1-2, zeng2024osteopontindrivenpartialepithelialmesenchymal media 37734d41).

**(ii) Pediatric acquired cholesteatoma biomarker intensification (2023).** Rolesi et al. quantitatively show that pediatric acquired disease has substantially higher peri-matrix IL-1β and angiogenic signaling (VEGF-C/PDGFr) and stronger STAT3 activation than adult acquired or congenital forms (rolesi2023studyofangiogenic pages 5-8, rolesi2023studyofangiogenic pages 10-12).

**(iii) Microbiome/metagenome profiling (2024).** Kanodia et al. (Apr 2024; https://doi.org/10.1007/s12070-024-04678-9) report metagenomic compositions from 15 cholesteatoma samples, commonly dominated by **Proteobacteria** (up to ~95% reads in 9/15) with frequent **Pseudomonas/Klebsiella/Escherichia**, and Firmicutes-dominant profiles in a subset (kanodia2024metagenomeanalysisof pages 1-2, kanodia2024metagenomeanalysisof pages 6-9). These studies support a move from culture-based microbiology to sequencing-informed pathogen ecology in chronic ear disease.

**(iv) miRNA profiling as a regulatory layer (2024).** Xie et al. (Jun 2024; https://doi.org/10.1186/s12920-024-01932-5) report 121 differentially expressed miRNAs in cholesteatoma vs matched skin (56 up, 65 down), with top changes including miR-21-5p/miR-142-5p (up) and miR-508-3p/miR-509-3p/miR-211-5p (down), and predicted key targets (TGFBR2, MBNL1, NFAT5) (xie2024identificationofmirna pages 1-2). (Note: enriched GO/KEGG categories were not extractable from the available excerpt.)

### 8) Current applications and real-world implementations

**Surgery remains central.** Bovi et al. describe cholesteatoma as “**a surgical disease**,” emphasizing operative technique and follow-up strategy as key determinants of recidivism (Apr 2023; https://doi.org/10.14639/0392-100x-suppl.1-43-2023-06) (bovi2023recurrenceincholesteatoma pages 4-6).

**Technique selection impacts residual/recurrence risk.** In Bovi et al. (2023), CWU approaches show higher residual disease (average ~15%, range 3.8–21%) than CWD (average residual 6.5%; recurrence 5.1%), and CWU has ~2.87 relative risk of recurrent/residual disease compared to CWD in a meta-analysis (bovi2023recurrenceincholesteatoma pages 4-6, bovi2023recurrenceincholesteatoma pages 2-3).

**Imaging for postoperative detection (implementation).** Non–echo planar imaging diffusion-weighted MRI is highlighted as a high-performance tool to detect residual/recurrent disease; Bovi et al. report: “**the sensitivity and specificity of Non EPI DWI-MRI are 89.79% and 94.57%, respectively**” and it may allow avoidance of routine second-look surgery in some cases (bovi2023recurrenceincholesteatoma pages 4-6).

**Adjuncts to reduce recidivism.** Endoscopic ear surgery (EES), mastoid obliteration, and KTP lasers are noted as practical strategies; mastoid obliteration is associated with reduced recidivism (OR 0.45, 95% CI 0.26–0.8) (bovi2023recurrenceincholesteatoma pages 3-4). MESNA is noted as an adjunct with potential benefit across retrospective studies (bovi2023recurrenceincholesteatoma pages 6-7).

### 9) Relevant statistics (recent studies)

- **Ossicular chain destruction:** “Complete or partial destruction of the ossicular chain is observed in approximately **80%** of cholesteatoma cases” (Popescu 2024) (popescu2024comprehensivemanagementof pages 1-2).
- **Postoperative recurrence:** Popescu et al. report **1.55%** recurrence within two years in a 580-patient surgical cohort (popescu2024comprehensivemanagementof pages 15-18).
- **Familial risk:** Bonnard et al. (May 2023; https://doi.org/10.1001/jamaoto.2023.0048) report familial clustering with OR **3.9** (95% CI 3.1–4.8) for individuals with a first-degree relative surgically treated (bonnard2023theriskof pages 1-2).
- **Upper airway comorbidities:** Borgström et al. (Mar 2024; https://doi.org/10.1007/s00405-024-08567-3) report associations of chronic rhinitis/sinusitis/nasal polyposis (OR ~1.5–2.5) and particularly adenoid surgery (children OR 4.4, 95% CI 3.5–5.5) with cholesteatoma surgery (borgstrom2024occurrenceofmucosaaffecting pages 1-2, borgstrom2024occurrenceofmucosaaffecting pages 4-5).

### 10) Knowledge-base style structured annotations (draft)

**Disease entity:** Cholesteatoma (middle ear; acquired and congenital forms). MONDO ID was **not retrievable from the available literature excerpts in this run**.

**Anatomy (UBERON):** middle ear cavity/epithelium (UBERON:0001756); temporal bone/mastoid/ossicles (contextual; referenced clinically) (popescu2024comprehensivemanagementof pages 24-26, popescu2024comprehensivemanagementof pages 1-2).

**Cell types (CL):** keratinocyte (CL:0000312); fibroblast (CL:0000057); T cell (CL:0000084); macrophage (CL:0000235); endothelial cell (CL:0000115); osteoclast (CL:0000092) (popescu2024comprehensivemanagementof pages 24-26, bologa2025biologyofrecurrent pages 4-5, rolesi2023studyofangiogenic pages 5-8).

**Genes/proteins (HGNC examples):** SPP1, ZEB2, AKT1, STAT3, IL1B, TGFB1, NFKB1, MKI67, MMP2, MMP9, TIMP2, TIMP4, DEFB4A, SHH (zeng2024osteopontindrivenpartialepithelialmesenchymal media 37734d41, rolesi2023studyofangiogenic pages 5-8, dambergs2023morphopathogenesisofadult pages 10-12, dambergs2023morphopathogenesisofadult pages 14-15).

**Chemicals (CHEBI example):** MESNA (sodium 2-mercaptoethanesulfonate) (bovi2023recurrenceincholesteatoma pages 6-7).

**GO processes (examples):** epithelial proliferation (GO:0050673); angiogenesis (GO:0001525); ECM disassembly (GO:0022617); osteoclast differentiation (GO:0030316); EMT (GO:0001837); biofilm formation (GO:0042710) (dambergs2023morphopathogenesisofadult pages 13-14, rolesi2023studyofangiogenic pages 5-8, dambergs2024comparisonoftissue pages 14-15, zeng2024osteopontindrivenpartialepithelialmesenchymal pages 1-2, kanodia2024metagenomeanalysisof pages 6-9).

### 11) Evidence summary table

| Mechanistic Module | Key Molecules (HGNC) | Cell Types (CL) | Anatomy (UBERON) | Dysregulated Pathways / GO Terms | Key Evidence (Study, Year, DOI) | Quantitative / Statistical Highlights | Citation IDs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Keratinocyte Hyperproliferation & Survival** | **MKI67** (Ki-67), **NFKB1** (NF-κB), **PCNA**, **ID1** | Keratinocyte (CL:0000312) | Middle ear epithelium (UBERON:0001756) | Epithelial cell proliferation (GO:0050673); NF-kappaB signaling (GO:0043123); Anti-apoptosis | Dambergs et al. (2023) [doi:10.3390/medicina59020306]; Dambergs et al. (2024) [doi:10.3390/diagnostics14060662] | Ki-67 matrix vs skin epithelium: **p=0.000**. NF-κB matrix vs epithelium: **p=0.001**. NF-κB correlates with Ki-67 (**r=0.538, p=0.017**) suggesting proliferative role. | (dambergs2023morphopathogenesisofadult pages 1-2, dambergs2023morphopathogenesisofadult pages 13-14, dambergs2023morphopathogenesisofadult pages 14-15) |
| **Inflammation & Proliferative Signaling** | **IL1A**, **IL1B**, **IL6**, **TGFB1** (TGF-β), **STAT3** | T cell (CL:0000084), Fibroblast (CL:0000057) | Peri-matrix (Granulation tissue) | Cytokine-mediated signaling (GO:0019221); STAT cascade (GO:0097696); Wound healing | Rolesi et al. (2023) [doi:10.3390/jpm13081189]; Dambergs et al. (2023) [doi:10.3390/medicina59020306] | **pSTAT3** nuclear OD highest in pediatric acquired (**125.54**) vs adult (**75.49**). **IL-1β** peri-matrix OD: pediatric (**148.68**) vs adult (**108.44**) (**p<0.001**). IL-1 correlates with IL-10 (**r=0.820**). | (rolesi2023studyofangiogenic pages 8-10, rolesi2023studyofangiogenic pages 10-12, dambergs2023morphopathogenesisofadult pages 13-14) |
| **Partial EMT (p-EMT)** | **SPP1** (Osteopontin), **ZEB2**, **AKT1** | Keratinocyte (CL:0000312) | Middle ear epithelium | Epithelial to mesenchymal transition (GO:0001837); Cell migration (GO:0016477) | Zeng et al. (2024) [doi:10.1080/15384101.2024.2345481] | OPN treatment upregulates **Vimentin/Fibronectin** (mesenchymal) and downregulates epithelial markers; **siZEB2** abolishes these effects (in vitro). | (zeng2024osteopontindrivenpartialepithelialmesenchymal pages 1-2, zeng2024osteopontindrivenpartialepithelialmesenchymal media 37734d41) |
| **Matrix Remodeling & Bone Erosion** | **MMP2**, **MMP9**, **TIMP2**, **TIMP4** | Fibroblast, Macrophage | Temporal bone / Ossicles | Extracellular matrix disassembly (GO:0022617); Collagen catabolism | Dambergs et al. (2024) [doi:10.3390/diagnostics14060662]; Popescu et al. (2024) [doi:10.3390/jcm13226791] | **MMP-9** reduced in matrix vs skin (**p=0.008**). Strong correlation: MMP-2 matrix vs perimatrix (**r=0.803, p=0.000** in children). Enzymatic lysis confirmed as primary erosion driver. | (dambergs2023morphopathogenesisofadult pages 1-2, popescu2024comprehensivemanagementof pages 1-2, dambergs2024comparisonoftissue pages 14-15) |
| **Osteoclastogenesis** | **TNFSF11** (RANKL), **TNFRSF11B** (OPG), **TNF** (TNF-α) | Osteoclast (CL:0000092), T/B Lymphocytes | Mastoid bone / Ossicles | Osteoclast differentiation (GO:0030316); Bone resorption (GO:0045453) | Bologa et al. (2025) [doi:10.47162/rjme.65.4.24]; Popescu et al. (2024) [doi:10.3390/jcm13226791] | T- and B-cells identified as sources of **RANKL** driving osteolysis. Bone destruction observed in **~90%** of cases on imaging. | (bologa2025biologyofrecurrent pages 4-5, popescu2024comprehensivemanagementof pages 24-26, popescu2024comprehensivemanagementof pages 7-10) |
| **Angiogenesis** | **VEGFC**, **PDGFRA**, **VEGFA** | Endothelial cell (CL:0000115) | Peri-matrix (vascular stroma) | Angiogenesis (GO:0001525); VEGF signaling (GO:0048010) | Rolesi et al. (2023) [doi:10.3390/jpm13081189] | **VEGF-C** peri-matrix OD: pediatric (**190.98**) vs congenital (**38.16**) (**p<0.001**). **PDGFr** levels significantly higher in acquired vs congenital (**p<0.001**). | (rolesi2023studyofangiogenic pages 10-12, rolesi2023studyofangiogenic pages 5-8) |
| **Innate Immunity** | **DEFB4A** (HβD-2), **DEFB104A** (HβD-4) | Epithelial cell | Middle ear mucosa | Antimicrobial humoral response (GO:0019730); Innate immune response | Dambergs et al. (2023) [doi:10.3390/medicina59020306] | **HβD-2** significantly overexpressed in cholesteatoma vs control (**p=0.004**); correlates strongly with IL-1 (**r=0.822, p=0.000**). | (dambergs2023morphopathogenesisofadult pages 1-2, dambergs2023morphopathogenesisofadult pages 14-15) |
| **Developmental Signaling** | **SHH** (Sonic Hedgehog) | Fibroblast / Stromal cell | Peri-matrix | Tissue morphogenesis (GO:0048729); Cell differentiation | Dambergs et al. (2023) [doi:10.3390/medicina59020306] | **SHH** overexpressed in perimatrix vs control connective tissue (**p=0.000**); correlates with MMP-2 (**r=0.786**) and NF-κB (**r=0.753**). | (dambergs2023morphopathogenesisofadult pages 1-2, dambergs2024comparisonoftissue pages 14-15, dambergs2023morphopathogenesisofadult pages 14-15) |
| **Microbiome & Biofilm** | **Pseudomonas**, **Staphylococcus**, **Proteobacteria** | Bacteria (NCBI:txid2) | Middle ear cavity | Biofilm formation (GO:0042710) | Kanodia et al. (2024) [doi:10.1007/s12070-024-04678-9]; Popescu et al. (2024) [doi:10.3390/jcm13226791] | **Proteobacteria** dominated 9/15 samples (up to **95%** reads). Biofilms (S. aureus/P. aeruginosa) linked to persistence/recurrence. | (popescu2024comprehensivemanagementof pages 24-26, kanodia2024metagenomeanalysisof pages 1-2, kanodia2024metagenomeanalysisof pages 6-9) |


*Table: Summary of key pathophysiological modules in cholesteatoma, including hyperproliferation, inflammation, bone erosion, and angiogenesis, with quantitative evidence from 2023–2025 studies.*

### 12) Notes on evidence limitations

- Several sources in this run are open-access clinical reviews/observational studies with robust mechanistic discussion but do not always provide PMIDs in the extracted text; DOIs/URLs are provided for traceability.
- For miRNA-seq (Xie 2024) and metagenomics (Kanodia 2024), only limited details of GO/KEGG enrichment statistics and per-sample taxa tables were accessible in excerpts; full-text mining of the complete articles/tables would enable deeper extraction of specific enriched pathways and effect sizes (xie2024identificationofmirna pages 1-2, kanodia2024metagenomeanalysisof pages 6-9).

### Key source list (2023–2024 prioritized)
- Popescu C. et al. **2024-11**. *J Clin Med.* https://doi.org/10.3390/jcm13226791 (popescu2024comprehensivemanagementof pages 1-2)
- Zeng L. et al. **2024-03**. *Cell Cycle.* https://doi.org/10.1080/15384101.2024.2345481 (zeng2024osteopontindrivenpartialepithelialmesenchymal pages 1-2)
- Kanodia A. et al. **2024-04**. *Indian J Otolaryngol Head Neck Surg.* https://doi.org/10.1007/s12070-024-04678-9 (kanodia2024metagenomeanalysisof pages 1-2)
- Xie M. et al. **2024-06**. *BMC Med Genomics.* https://doi.org/10.1186/s12920-024-01932-5 (xie2024identificationofmirna pages 1-2)
- Borgström AM. et al. **2024-03**. *Eur Arch Otorhinolaryngol.* https://doi.org/10.1007/s00405-024-08567-3 (borgstrom2024occurrenceofmucosaaffecting pages 1-2)
- Rolesi R. et al. **2023-07**. *J Pers Med.* https://doi.org/10.3390/jpm13081189 (rolesi2023studyofangiogenic pages 8-10)
- Bonnard Å. et al. **2023-05**. *JAMA Otolaryngol Head Neck Surg.* https://doi.org/10.1001/jamaoto.2023.0048 (bonnard2023theriskof pages 1-2)
- Bovi C. et al. **2023-04**. *Acta Otorhinolaryngol Ital.* https://doi.org/10.14639/0392-100x-suppl.1-43-2023-06 (bovi2023recurrenceincholesteatoma pages 4-6)
- Dambergs K. et al. **2023-02**. *Medicina.* https://doi.org/10.3390/medicina59020306 (dambergs2023morphopathogenesisofadult pages 1-2)
- Dambergs K. et al. **2024-03**. *Diagnostics.* https://doi.org/10.3390/diagnostics14060662 (dambergs2024comparisonoftissue pages 14-15)


References

1. (popescu2024comprehensivemanagementof pages 1-2): Cristina Popescu, Renata Maria Văruț, Monica Puticiu, Vlad Ionut Belghiru, Mihai Banicioiu, Luciana Teodora Rotaru, Mihaela Popescu, Arsenie Cristian Cosmin, and Alin Iulian Silviu Popescu. Comprehensive management of cholesteatoma in otitis media: diagnostic challenges, imaging advances, and surgical outcome. Journal of Clinical Medicine, 13:6791, Nov 2024. URL: https://doi.org/10.3390/jcm13226791, doi:10.3390/jcm13226791. This article has 12 citations.

2. (rolesi2023studyofangiogenic pages 2-4): Rolando Rolesi, Fabiola Paciello, Gaetano Paludetti, Eugenio De Corso, Bruno Sergi, and Anna Fetoni. Study of angiogenic, pro-apoptotic, and pro-inflammatory factors in congenital and acquired cholesteatomas. Journal of Personalized Medicine, 13:1189, Jul 2023. URL: https://doi.org/10.3390/jpm13081189, doi:10.3390/jpm13081189. This article has 4 citations.

3. (rolesi2023studyofangiogenic pages 1-2): Rolando Rolesi, Fabiola Paciello, Gaetano Paludetti, Eugenio De Corso, Bruno Sergi, and Anna Fetoni. Study of angiogenic, pro-apoptotic, and pro-inflammatory factors in congenital and acquired cholesteatomas. Journal of Personalized Medicine, 13:1189, Jul 2023. URL: https://doi.org/10.3390/jpm13081189, doi:10.3390/jpm13081189. This article has 4 citations.

4. (popescu2024comprehensivemanagementof pages 24-26): Cristina Popescu, Renata Maria Văruț, Monica Puticiu, Vlad Ionut Belghiru, Mihai Banicioiu, Luciana Teodora Rotaru, Mihaela Popescu, Arsenie Cristian Cosmin, and Alin Iulian Silviu Popescu. Comprehensive management of cholesteatoma in otitis media: diagnostic challenges, imaging advances, and surgical outcome. Journal of Clinical Medicine, 13:6791, Nov 2024. URL: https://doi.org/10.3390/jcm13226791, doi:10.3390/jcm13226791. This article has 12 citations.

5. (dambergs2023morphopathogenesisofadult pages 1-2): Kristaps Dambergs, Gunta Sumeraga, and Māra Pilmane. Morphopathogenesis of adult acquired cholesteatoma. Medicina, 59:306, Feb 2023. URL: https://doi.org/10.3390/medicina59020306, doi:10.3390/medicina59020306. This article has 13 citations.

6. (dambergs2023morphopathogenesisofadult pages 13-14): Kristaps Dambergs, Gunta Sumeraga, and Māra Pilmane. Morphopathogenesis of adult acquired cholesteatoma. Medicina, 59:306, Feb 2023. URL: https://doi.org/10.3390/medicina59020306, doi:10.3390/medicina59020306. This article has 13 citations.

7. (rolesi2023studyofangiogenic pages 10-12): Rolando Rolesi, Fabiola Paciello, Gaetano Paludetti, Eugenio De Corso, Bruno Sergi, and Anna Fetoni. Study of angiogenic, pro-apoptotic, and pro-inflammatory factors in congenital and acquired cholesteatomas. Journal of Personalized Medicine, 13:1189, Jul 2023. URL: https://doi.org/10.3390/jpm13081189, doi:10.3390/jpm13081189. This article has 4 citations.

8. (rolesi2023studyofangiogenic pages 8-10): Rolando Rolesi, Fabiola Paciello, Gaetano Paludetti, Eugenio De Corso, Bruno Sergi, and Anna Fetoni. Study of angiogenic, pro-apoptotic, and pro-inflammatory factors in congenital and acquired cholesteatomas. Journal of Personalized Medicine, 13:1189, Jul 2023. URL: https://doi.org/10.3390/jpm13081189, doi:10.3390/jpm13081189. This article has 4 citations.

9. (rolesi2023studyofangiogenic pages 5-8): Rolando Rolesi, Fabiola Paciello, Gaetano Paludetti, Eugenio De Corso, Bruno Sergi, and Anna Fetoni. Study of angiogenic, pro-apoptotic, and pro-inflammatory factors in congenital and acquired cholesteatomas. Journal of Personalized Medicine, 13:1189, Jul 2023. URL: https://doi.org/10.3390/jpm13081189, doi:10.3390/jpm13081189. This article has 4 citations.

10. (dambergs2023morphopathogenesisofadult pages 10-12): Kristaps Dambergs, Gunta Sumeraga, and Māra Pilmane. Morphopathogenesis of adult acquired cholesteatoma. Medicina, 59:306, Feb 2023. URL: https://doi.org/10.3390/medicina59020306, doi:10.3390/medicina59020306. This article has 13 citations.

11. (dambergs2024comparisonoftissue pages 14-15): Kristaps Dambergs, Gunta Sumeraga, and Māra Pilmane. Comparison of tissue factors in the ontogenetic aspects of human cholesteatoma. Diagnostics, 14:662, Mar 2024. URL: https://doi.org/10.3390/diagnostics14060662, doi:10.3390/diagnostics14060662. This article has 4 citations.

12. (bologa2025biologyofrecurrent pages 4-5): Ramona Andreea Bologa, Florin Anghelina, Mihaela Roxana Mitroi, Mircea Sorin Ciolofan, Carmen Aurelia Mogoantă, Alina Nicoleta Căpitănescu, Alexandru Florian Grecu, Liliana Anghelina, and Mihai-Marius Botezat. Biology of recurrent cholesteatoma in a romanian young patient – a case report. Romanian Journal of Morphology and Embryology, 65:775-780, Feb 2025. URL: https://doi.org/10.47162/rjme.65.4.24, doi:10.47162/rjme.65.4.24. This article has 1 citations and is from a peer-reviewed journal.

13. (dambergs2023morphopathogenesisofadult pages 14-15): Kristaps Dambergs, Gunta Sumeraga, and Māra Pilmane. Morphopathogenesis of adult acquired cholesteatoma. Medicina, 59:306, Feb 2023. URL: https://doi.org/10.3390/medicina59020306, doi:10.3390/medicina59020306. This article has 13 citations.

14. (zeng2024osteopontindrivenpartialepithelialmesenchymal pages 1-2): Lingling Zeng, Li Xie, Jin Hu, Chao He, Aiguo Liu, Xiang Lu, and Wen Zhou. Osteopontin-driven partial epithelial-mesenchymal transition governs the development of middle ear cholesteatoma. Cell Cycle, 23:537-554, Mar 2024. URL: https://doi.org/10.1080/15384101.2024.2345481, doi:10.1080/15384101.2024.2345481. This article has 5 citations and is from a peer-reviewed journal.

15. (zeng2024osteopontindrivenpartialepithelialmesenchymal media 37734d41): Lingling Zeng, Li Xie, Jin Hu, Chao He, Aiguo Liu, Xiang Lu, and Wen Zhou. Osteopontin-driven partial epithelial-mesenchymal transition governs the development of middle ear cholesteatoma. Cell Cycle, 23:537-554, Mar 2024. URL: https://doi.org/10.1080/15384101.2024.2345481, doi:10.1080/15384101.2024.2345481. This article has 5 citations and is from a peer-reviewed journal.

16. (bovi2023recurrenceincholesteatoma pages 6-7): Chiara Bovi, Alberto Luchena, Rachele Bivona, Daniele Borsetto, Nathan Creber, and Giovanni Danesi. Recurrence in cholesteatoma surgery: what have we learnt and where are we going? a narrative review. Acta Otorhinolaryngologica Italica, 43:S48-S55, Apr 2023. URL: https://doi.org/10.14639/0392-100x-suppl.1-43-2023-06, doi:10.14639/0392-100x-suppl.1-43-2023-06. This article has 44 citations and is from a peer-reviewed journal.

17. (kanodia2024metagenomeanalysisof pages 6-9): Anupam Kanodia, Rabia Monga, Mohd Ilyas, Yash Verma, Sarita Mohapatra, Narayana Sudha Rao, Meenal Vyas, Kapil Sikka, and Krishnamohan Atmakuri. Metagenome analysis of cholesteatoma-associated bacteria: a pilot study. Indian journal of otolaryngology and head and neck surgery : official publication of the Association of Otolaryngologists of India, 76 4:3307-3318, Apr 2024. URL: https://doi.org/10.1007/s12070-024-04678-9, doi:10.1007/s12070-024-04678-9. This article has 0 citations.

18. (popescu2024comprehensivemanagementof pages 2-3): Cristina Popescu, Renata Maria Văruț, Monica Puticiu, Vlad Ionut Belghiru, Mihai Banicioiu, Luciana Teodora Rotaru, Mihaela Popescu, Arsenie Cristian Cosmin, and Alin Iulian Silviu Popescu. Comprehensive management of cholesteatoma in otitis media: diagnostic challenges, imaging advances, and surgical outcome. Journal of Clinical Medicine, 13:6791, Nov 2024. URL: https://doi.org/10.3390/jcm13226791, doi:10.3390/jcm13226791. This article has 12 citations.

19. (popescu2024comprehensivemanagementof pages 15-18): Cristina Popescu, Renata Maria Văruț, Monica Puticiu, Vlad Ionut Belghiru, Mihai Banicioiu, Luciana Teodora Rotaru, Mihaela Popescu, Arsenie Cristian Cosmin, and Alin Iulian Silviu Popescu. Comprehensive management of cholesteatoma in otitis media: diagnostic challenges, imaging advances, and surgical outcome. Journal of Clinical Medicine, 13:6791, Nov 2024. URL: https://doi.org/10.3390/jcm13226791, doi:10.3390/jcm13226791. This article has 12 citations.

20. (popescu2024comprehensivemanagementof pages 7-10): Cristina Popescu, Renata Maria Văruț, Monica Puticiu, Vlad Ionut Belghiru, Mihai Banicioiu, Luciana Teodora Rotaru, Mihaela Popescu, Arsenie Cristian Cosmin, and Alin Iulian Silviu Popescu. Comprehensive management of cholesteatoma in otitis media: diagnostic challenges, imaging advances, and surgical outcome. Journal of Clinical Medicine, 13:6791, Nov 2024. URL: https://doi.org/10.3390/jcm13226791, doi:10.3390/jcm13226791. This article has 12 citations.

21. (kanodia2024metagenomeanalysisof pages 1-2): Anupam Kanodia, Rabia Monga, Mohd Ilyas, Yash Verma, Sarita Mohapatra, Narayana Sudha Rao, Meenal Vyas, Kapil Sikka, and Krishnamohan Atmakuri. Metagenome analysis of cholesteatoma-associated bacteria: a pilot study. Indian journal of otolaryngology and head and neck surgery : official publication of the Association of Otolaryngologists of India, 76 4:3307-3318, Apr 2024. URL: https://doi.org/10.1007/s12070-024-04678-9, doi:10.1007/s12070-024-04678-9. This article has 0 citations.

22. (xie2024identificationofmirna pages 1-2): Mengyao Xie, Qi Tang, Shu Wang, Xiaowu Huang, Zhiyuan Wu, Zhijin Han, Chen Li, Bin Wang, Yingying Shang, and Hua Yang. Identification of mirna expression profile in middle ear cholesteatoma using small rna-sequencing. BMC Medical Genomics, Jun 2024. URL: https://doi.org/10.1186/s12920-024-01932-5, doi:10.1186/s12920-024-01932-5. This article has 3 citations and is from a peer-reviewed journal.

23. (bovi2023recurrenceincholesteatoma pages 4-6): Chiara Bovi, Alberto Luchena, Rachele Bivona, Daniele Borsetto, Nathan Creber, and Giovanni Danesi. Recurrence in cholesteatoma surgery: what have we learnt and where are we going? a narrative review. Acta Otorhinolaryngologica Italica, 43:S48-S55, Apr 2023. URL: https://doi.org/10.14639/0392-100x-suppl.1-43-2023-06, doi:10.14639/0392-100x-suppl.1-43-2023-06. This article has 44 citations and is from a peer-reviewed journal.

24. (bovi2023recurrenceincholesteatoma pages 2-3): Chiara Bovi, Alberto Luchena, Rachele Bivona, Daniele Borsetto, Nathan Creber, and Giovanni Danesi. Recurrence in cholesteatoma surgery: what have we learnt and where are we going? a narrative review. Acta Otorhinolaryngologica Italica, 43:S48-S55, Apr 2023. URL: https://doi.org/10.14639/0392-100x-suppl.1-43-2023-06, doi:10.14639/0392-100x-suppl.1-43-2023-06. This article has 44 citations and is from a peer-reviewed journal.

25. (bovi2023recurrenceincholesteatoma pages 3-4): Chiara Bovi, Alberto Luchena, Rachele Bivona, Daniele Borsetto, Nathan Creber, and Giovanni Danesi. Recurrence in cholesteatoma surgery: what have we learnt and where are we going? a narrative review. Acta Otorhinolaryngologica Italica, 43:S48-S55, Apr 2023. URL: https://doi.org/10.14639/0392-100x-suppl.1-43-2023-06, doi:10.14639/0392-100x-suppl.1-43-2023-06. This article has 44 citations and is from a peer-reviewed journal.

26. (bonnard2023theriskof pages 1-2): Åsa Bonnard, Cecilia Engmér Berglin, Josephine Wincent, Per Olof Eriksson, Eva Westman, Maria Feychting, and Hanna Mogensen. The risk of cholesteatoma in individuals with first-degree relatives surgically treated for the disease. JAMA Otolaryngology–Head &amp; Neck Surgery, 149:390, May 2023. URL: https://doi.org/10.1001/jamaoto.2023.0048, doi:10.1001/jamaoto.2023.0048. This article has 19 citations.

27. (borgstrom2024occurrenceofmucosaaffecting pages 1-2): Agnes Modée Borgström, Hanna Mogensen, Cecilia Engmér Berglin, Johan Knutsson, and Åsa Bonnard. Occurrence of mucosa-affecting diseases of the upper airways in middle ear cholesteatoma patients: a nationwide case–control study. European Archives of Oto-Rhino-Laryngology, 281:4081-4087, Mar 2024. URL: https://doi.org/10.1007/s00405-024-08567-3, doi:10.1007/s00405-024-08567-3. This article has 1 citations and is from a peer-reviewed journal.

28. (borgstrom2024occurrenceofmucosaaffecting pages 4-5): Agnes Modée Borgström, Hanna Mogensen, Cecilia Engmér Berglin, Johan Knutsson, and Åsa Bonnard. Occurrence of mucosa-affecting diseases of the upper airways in middle ear cholesteatoma patients: a nationwide case–control study. European Archives of Oto-Rhino-Laryngology, 281:4081-4087, Mar 2024. URL: https://doi.org/10.1007/s00405-024-08567-3, doi:10.1007/s00405-024-08567-3. This article has 1 citations and is from a peer-reviewed journal.