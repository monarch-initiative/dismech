---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-31T17:28:14.740980'
end_time: '2026-01-31T17:37:07.263328'
duration_seconds: 532.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Renal Cell Carcinoma
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Renal Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Renal Cell Carcinoma**.
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
- **Disease Name:** Renal Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Renal Cell Carcinoma**.
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
- Disease Name: Renal Cell Carcinoma (RCC)
- MONDO ID: MONDO:0005070
- Category: Cancer

## Pathophysiology Description (Narrative)

Renal cell carcinoma comprises biologically distinct subtypes with shared themes of oxygen/nutrient-sensing deregulation, profound metabolic rewiring, and an immunosuppressive tumor microenvironment. In clear cell RCC (ccRCC), loss of VHL on chromosome 3p stabilizes HIF-α subunits, especially HIF‑2α (EPAS1), driving angiogenesis, glycolysis, lipid storage, and immune escape programs; these changes underlie responsiveness to VEGF pathway inhibitors and, more recently, to direct HIF‑2α antagonism (belzutifan) (nguyen2024novelapproacheswith pages 1-2, coffey2024metabolicalterationsin pages 30-32). Multi-omic and single-cell studies corroborate ccRCC intratumoral heterogeneity, with tumor subpopulations enriched for EMT and inflammation programs and distinct chromatin-accessibility consequences of PBRM1 versus BAP1 mutations (coffey2024metabolicalterationsin pages 30-32). Whole‑genome sequencing of >700 ccRCC further refines driver landscapes and links structural copy alterations and canonical genes (VHL, PBRM1, SETD2, BAP1) to outcomes and immune infiltration, supporting immunotherapy rationales (coffey2024metabolicalterationsin pages 30-32).

Metabolically, ccRCC is a prototype metabolic cancer: in vivo isotope tracing shows suppressed TCA labeling and ETC activity in primary tumors but a metabolic shift toward enhanced TCA flux in metastases; mouse experiments demonstrate that stimulating mitochondrial respiration or NADH recycling promotes metastasis, whereas complex I inhibition suppresses it (bezwada2024mitochondrialcomplexi pages 1-2). High OXPHOS transcriptional programs correlate with resistance to immune checkpoint inhibition; experimentally dampening complex I (Ndufb8 knockdown) reduces hypoxia, increases functional CD8+ T‑cell infiltration, and improves anti‑PD‑L1 efficacy in vivo (tian2024targetingoxidativephosphorylation pages 1-2). Beyond glucose, ccRCC exhibits glutamine dependence, ferroptosis sensitivity controlled by glutathione/GPX4 systems, and extensive lipid/cholesterol rewiring including SR‑BI (SCARB1) upregulation and tryptophan–kynurenine pathway activation that fosters immune suppression (coffey2024metabolicalterationsin pages 11-13, coffey2024metabolicalterationsin pages 19-21, coffey2024metabolicalterationsin pages 30-32, coffey2024metabolicalterationsin pages 36-38).

In papillary RCC (pRCC), type 1 commonly harbors MET activation, while type 2 includes FH deficiency and transcription factor (MiT/TFE) fusions, producing oncometabolite accumulation (fumarate/succinate), dioxygenase inhibition (pseudohypoxia), CIMP hypermethylation, EMT, and vulnerabilities to PARP inhibition and arginine deprivation (coffey2024metabolicalterationsin pages 25-26, coffey2024metabolicalterationsin pages 8-9). Chromophobe RCC (chRCC) presents widespread chromosomal losses, mtDNA depletion, diminished ETC protein levels, and elevated glutathione, reflecting distinctive mitochondrial/redox states compared to oncocytoma and suggesting ferroptosis/redox-targeting opportunities (coffey2024metabolicalterationsin pages 11-13, zhang2025thepathogenesisand pages 9-9).

The RCC tumor microenvironment (TME) features exhausted CD8+ T cells, Tregs, M2‑like TAMs, aberrant vasculature, and metabolite gradients (lactate, hypoxia) that shape immune evasion. Spatial/single-cell profiling of bone metastases reveals MDSC→TAM trajectories, MRC1+FOLR2+ TAMs, and CD47+ T‑cell niches; these data illuminate pre‑metastatic/metastatic niche biology and therapeutic targets (coffey2024metabolicalterationsin pages 30-32). Collectively, genotype–epigenotype–metabolism–immunity couplings drive RCC initiation, progression, metastasis, and therapy response.

| Category | Entity (HGNC / Label) | Primary mechanism / role (concise) | Major subtype(s) | Key pathway / process (GO term label) | Subcellular location (GO-CC) | Sources |
|---|---|---|---|---|---|---|
| Gene | VHL | E3 ligase for HIFα; tumor suppressor | ccRCC | response to hypoxia (GO:0001666) | cytosol / nucleus | (coffey2024metabolicalterationsin pages 30-32, nguyen2024novelapproacheswith pages 1-2) |
| Gene | EPAS1 (HIF2A) | Hypoxia transcription factor; drives angiogenesis, lipids | ccRCC | HIF signaling / angiogenesis | nucleus | (nguyen2024novelapproacheswith pages 1-2, coffey2024metabolicalterationsin pages 30-32) |
| Gene | HIF1A | Hypoxia TF; induces glycolytic program | ccRCC | glycolytic process (GO:0006096) | nucleus | (coffey2024metabolicalterationsin pages 30-32, nguyen2024novelapproacheswith pages 1-2) |
| Gene | PBRM1 | SWI/SNF chromatin remodeler; tumor suppressor | ccRCC | chromatin organization (GO:0006325) | nucleus / chromatin | (coffey2024metabolicalterationsin pages 30-32) |
| Gene | BAP1 | Deubiquitinase; chromatin modifier, prognosis marker | ccRCC | chromatin modification (GO:0016570) | nucleus | (coffey2024metabolicalterationsin pages 30-32) |
| Gene | SETD2 | H3K36 methyltransferase; DNA repair/epigenetic regulator | ccRCC | histone methylation (GO:0018024) | nucleus | (coffey2024metabolicalterationsin pages 30-32) |
| Gene | MET | Receptor tyrosine kinase; growth and EMT driver | pRCC (type 1) | HGF/MET signaling (GO label) | plasma membrane | (coffey2024metabolicalterationsin pages 25-26) |
| Gene | FH | TCA enzyme; fumarate accumulation (oncometabolite) | pRCC type 2 / HLRCC | tricarboxylic acid cycle (GO:0006099) | mitochondrion | (coffey2024metabolicalterationsin pages 8-9) |
| Gene | SDHB/SDHC/SDHD | Complex II subunits; SDH-deficient oncometabolism | SDH-deficient RCC | electron transport chain / TCA | mitochondrion | (coffey2024metabolicalterationsin pages 8-9, coffey2024metabolicalterationsin pages 11-13) |
| Gene | PTEN | PI3K pathway suppressor; mTOR regulator | chRCC, others | PI3K-AKT signaling (GO:0008286) | cytosol / membrane | (coffey2024metabolicalterationsin pages 36-38, coffey2024metabolicalterationsin pages 30-32) |
| Gene | PPARGC1A (PGC-1α) | Mitochondrial biogenesis regulator; often suppressed | ccRCC | mitochondrial biogenesis (GO:0007005) | nucleus / mitochondrial | (zhang2025thepathogenesisand pages 9-9, bezwada2024mitochondrialcomplexi pages 1-2) |
| Gene | GLS1 (GLS) | Glutaminase; drives glutamine catabolism | ccRCC | glutamine metabolic process (GO label) | mitochondrion | (zhang2025thepathogenesisand pages 11-11, coffey2024metabolicalterationsin pages 19-21) |
| Gene | LDHA | Lactate dehydrogenase A; glycolysis effector | ccRCC, pRCC | glycolytic process (GO:0006096) | cytosol | (coffey2024metabolicalterationsin pages 11-13, coffey2024metabolicalterationsin pages 25-26) |
| Gene | SCARB1 | HDL receptor; mediates cholesterol uptake, lipid storage | ccRCC | cholesterol transport (GO:0015918) | plasma membrane | (coffey2024metabolicalterationsin pages 36-38, coffey2024metabolicalterationsin pages 30-32) |
| Cell type | Proximal tubule epithelial cell (CL) | Renal epithelial origin of many RCCs | ccRCC origin | epithelial differentiation (GO:0030855) | apical membrane / cytoplasm | (coffey2024metabolicalterationsin pages 30-32) |
| Cell type | Tumor-associated macrophage (CL) | Immunosuppressive, pro-tumor M2-like activity | all RCC TMEs | regulation of immune response (GO:0050776) | extracellular / TME | (coffey2024metabolicalterationsin pages 36-38, zhang2025thepathogenesisand pages 11-11) |
| Cell type | Regulatory T cell (Treg) (CL) | Suppresses CD8+ antitumor responses; cancer-promoting subset | ccRCC | negative regulation immune response (GO:0002683) | nucleus / cytosol | (coffey2024metabolicalterationsin pages 36-38, zhang2025thepathogenesisand pages 11-11) |
| Cell type | Endothelial cell (CL) | Drives angiogenesis and pre-metastatic niche formation | ccRCC | angiogenesis (GO:0001525) | plasma membrane | (zhang2025thepathogenesisand pages 8-9, nguyen2024novelapproacheswith pages 1-2) |
| Anatomical site | Kidney cortex (UBERON) | Primary site; tubular epithelium origin | primary RCC | renal tubular processes (GO label) | tissue compartment | (coffey2024metabolicalterationsin pages 30-32) |
| Anatomical site | Bone (UBERON) | Frequent metastatic site; osteolytic niche | metastatic RCC | bone resorption (GO:0045121) | bone tissue | (bezwada2024mitochondrialcomplexi pages 1-2, zhang2025thepathogenesisand pages 8-9) |
| Chemical | Glutamine (CHEBI) | Metabolic fuel; supports glutaminolysis | ccRCC metabolic dependency | amino-acid metabolism (GO label) | cytosol / mitochondrion | (zhang2025thepathogenesisand pages 11-11, coffey2024metabolicalterationsin pages 19-21) |
| Chemical | Lactate (CHEBI) | Oncometabolite; acidifies TME, immunosuppressive | ccRCC TME | lactate metabolic process (GO:0019752) | extracellular | (coffey2024metabolicalterationsin pages 11-13, zhang2025thepathogenesisand pages 11-11) |
| Chemical | Belzutifan (CHEBI) | Small-molecule HIF-2α inhibitor; approved therapy | VHL-associated & sporadic mRCC | inhibition of HIF-2α activity (GO label) | cytosol / nucleus target | (nguyen2024novelapproacheswith pages 1-2, coffey2024metabolicalterationsin pages 30-32) |
| Chemical | Fumarate (CHEBI) | Oncometabolite; inhibits αKG-dioxygenases (epigenetic) | FH-deficient RCC | prolyl hydroxylase inhibition / CIMP | mitochondrion / cytosol | (coffey2024metabolicalterationsin pages 8-9) |


*Table: Compact two-part table mapping key RCC genes/proteins to mechanisms, subtypes, GO processes and locations, plus cell types, anatomical sites, chemicals and disrupted processes — with source IDs for reference.; useful for ontology annotation and rapid mechanistic lookup.*

## 1. Core Pathophysiology
- Primary mechanisms: VHL loss → HIF stabilization (HIF‑2α>HIF‑1α) → angiogenesis (VEGF), glycolysis, lipid storage, c‑Myc/cell‑cycle programs; immune evasion via PD‑L1 and kynurenine pathway (nguyen2024novelapproacheswith pages 1-2, coffey2024metabolicalterationsin pages 30-32, coffey2024metabolicalterationsin pages 36-38).
- Dysregulated pathways: HIF signaling; PI3K/AKT/mTOR; MET/HGF in pRCC; TCA/ETC remodeling with context-dependent OXPHOS; amino-acid metabolism (glutamine, tryptophan); ferroptosis control (GPX4/glutathione) (nguyen2024novelapproacheswith pages 1-2, coffey2024metabolicalterationsin pages 8-9, bezwada2024mitochondrialcomplexi pages 1-2, coffey2024metabolicalterationsin pages 11-13, coffey2024metabolicalterationsin pages 30-32).
- Affected cellular processes: chromatin remodeling and DNA repair (PBRM1, BAP1, SETD2); EMT and invasion; angiogenesis; metabolic plasticity; T‑cell exhaustion and myeloid reprogramming (coffey2024metabolicalterationsin pages 30-32, bezwada2024mitochondrialcomplexi pages 1-2, tian2024targetingoxidativephosphorylation pages 1-2).

Key quotes/data:
- “ccRCC metastases unexpectedly have enhanced TCA cycle labelling… stimulating respiration or NADH recycling… promotes metastasis… inhibiting complex I decreases metastasis” (Nature, 14 Aug 2024, doi:10.1038/s41586-024-07812-3) (bezwada2024mitochondrialcomplexi pages 1-2).
- “High OXPHOS levels are risk factors for ICI [failure]… shNdufb8 tumors had higher CD8+ T cells, less hypoxia, and improved responses to anti‑PD‑L1” (JITC, Feb 2024, doi:10.1136/jitc-2023-008226) (tian2024targetingoxidativephosphorylation pages 1-2).

## 2. Key Molecular Players
- Genes/Proteins (HGNC): VHL, EPAS1(HIF2A), HIF1A, PBRM1, BAP1, SETD2, MET, FH, SDHB/SDHC/SDHD, PTEN, PPARGC1A(PGC‑1α), GLS, LDHA, SCARB1; see embedded table for roles and GO/CC context (nguyen2024novelapproacheswith pages 1-2, coffey2024metabolicalterationsin pages 30-32, coffey2024metabolicalterationsin pages 8-9, coffey2024metabolicalterationsin pages 11-13, coffey2024metabolicalterationsin pages 36-38).
- Chemical entities (CHEBI): belzutifan (HIF‑2α inhibitor), fumarate/succinate (oncometabolites), glutamine, lactate; functions in metabolism/therapy (nguyen2024novelapproacheswith pages 1-2, coffey2024metabolicalterationsin pages 8-9, coffey2024metabolicalterationsin pages 11-13, coffey2024metabolicalterationsin pages 36-38).
- Cell types (CL): proximal tubule epithelium (cell of origin), TAMs (MRC1+FOLR2+), Tregs, exhausted CD8+ T cells (coffey2024metabolicalterationsin pages 30-32, tian2024targetingoxidativephosphorylation pages 1-2).
- Anatomical locations (UBERON): kidney cortex (primary site), bone (common metastatic niche with osteolytic biology) (bezwada2024mitochondrialcomplexi pages 1-2, zhang2025thepathogenesisand pages 8-9).

## 3. Biological Processes (for GO annotation)
- Response to hypoxia; HIF signaling; angiogenesis; glycolytic process; oxidative phosphorylation; glutamine metabolic process; tryptophan/kynurenine pathway; chromatin organization; histone methylation; EMT; regulation of immune response; ferroptosis regulation (nguyen2024novelapproacheswith pages 1-2, coffey2024metabolicalterationsin pages 30-32, tian2024targetingoxidativephosphorylation pages 1-2, coffey2024metabolicalterationsin pages 11-13, coffey2024metabolicalterationsin pages 8-9).

## 4. Cellular Components
- Nucleus (HIF transcriptional effects; chromatin remodelers PBRM1/BAP1/SETD2). Mitochondrion (TCA/ETC, GLS1, OXPHOS, mtDNA depletion in chRCC). Plasma membrane (MET, SCARB1; PD‑L1). Extracellular space (lactate, IDO/kynurenine signaling) (coffey2024metabolicalterationsin pages 30-32, coffey2024metabolicalterationsin pages 11-13, coffey2024metabolicalterationsin pages 8-9, tian2024targetingoxidativephosphorylation pages 1-2).

## 5. Disease Progression
- Initiation: 3p loss (VHL±PBRM1/BAP1/SETD2) in ccRCC; MET activation in pRCC; FH/SDH loss in hereditary/Type 2 pRCC (coffey2024metabolicalterationsin pages 30-32, coffey2024metabolicalterationsin pages 8-9, coffey2024metabolicalterationsin pages 25-26).
- Early growth: HIF‑2α–driven angiogenesis and metabolic rewiring (glycolysis, lipid storage; glutamine use); immune modulation (PD‑L1, IDO) (nguyen2024novelapproacheswith pages 1-2, coffey2024metabolicalterationsin pages 36-38).
- Progression/metastasis: EMT/inflammation subclones, chromatin remodeling divergence; metastases adopt higher TCA/ETC flux; pre‑metastatic niche priming and organotropism (bone) with myeloid and endothelial remodeling (coffey2024metabolicalterationsin pages 30-32, bezwada2024mitochondrialcomplexi pages 1-2).

## 6. Phenotypic Manifestations (HP terms)
- Hypervascular renal mass, paraneoplastic cachexia/hypercalcemia (HIF‑related), anemia, immune cold/excluded phenotypes, osteolytic bone lesions in metastasis, variable responses to ICIs dependent on OXPHOS/TME state (nguyen2024novelapproacheswith pages 1-2, tian2024targetingoxidativephosphorylation pages 1-2, bezwada2024mitochondrialcomplexi pages 1-2).

## Recent Developments and Latest Research (2023–2024 prioritized)
- Nature 2024: Primary ccRCC has suppressed TCA/ETC; metastases increase TCA flux; complex I inhibition curtails metastasis—shifting views on mitochondrial targeting in advanced RCC (Aug 14, 2024; https://doi.org/10.1038/s41586-024-07812-3) (bezwada2024mitochondrialcomplexi pages 1-2).
- JITC 2024: High OXPHOS programs predict ICI resistance; targeting complex I alleviates hypoxia and reinvigorates CD8+ T cells, suggesting combinatorial strategies (Feb 2024; https://doi.org/10.1136/jitc-2023-008226) (tian2024targetingoxidativephosphorylation pages 1-2).
- Nat Rev Nephrol 2024: Integrative review codifies RCC as a metabolic disease across subtypes; details MET/pRCC, FH/SDH oncometabolism, ferroptosis liabilities, tryptophan metabolism–immune links (Jan 2024; https://doi.org/10.1038/s41581-023-00800-2) (coffey2024metabolicalterationsin pages 11-13, coffey2024metabolicalterationsin pages 19-21, coffey2024metabolicalterationsin pages 25-26, coffey2024metabolicalterationsin pages 30-32, coffey2024metabolicalterationsin pages 36-38).

## Current Applications and Real‑World Implementations
- Targeted therapy: HIF‑2α inhibitor belzutifan approved for VHL‑associated and sporadic mRCC; mechanistic basis in VHL/HIF biology (Jan 31, 2024; https://doi.org/10.3390/cancers16030601) (nguyen2024novelapproacheswith pages 1-2).
- Therapeutic strategy design: OXPHOS/complex I inhibition combined with PD‑(L)1 to overcome hypoxia‑driven T cell dysfunction (tian2024targetingoxidativephosphorylation pages 1-2). VEGF pathway inhibition guided by angiogenic HIF programs; MET inhibitors in pRCC type 1 (coffey2024metabolicalterationsin pages 25-26, nguyen2024novelapproacheswith pages 1-2).

## Expert Opinions and Authoritative Analyses
- Coffey & Simon 2024 (Nature Reviews Nephrology) synthesize hereditary/sporadic RCC metabolic mechanisms, highlighting shared vulnerabilities and the need for subtype‑specific modeling (Jan 2024; https://doi.org/10.1038/s41581-023-00800-2) (coffey2024metabolicalterationsin pages 11-13, coffey2024metabolicalterationsin pages 19-21, coffey2024metabolicalterationsin pages 25-26, coffey2024metabolicalterationsin pages 30-32, coffey2024metabolicalterationsin pages 36-38).

## Relevant Statistics and Data
- >80 patients: intraoperative 13C infusions demonstrate suppressed TCA labeling in primary ccRCC vs adjacent kidney; higher TCA labeling in metastases; complex I inhibition decreases metastasis in mice (Nature, 2024) (bezwada2024mitochondrialcomplexi pages 1-2).
- High OXPHOS signature associates with poorer ICI responses across CheckMate/JAVELIN datasets; shNdufb8 tumors show increased CD8+ T cell infiltration and function under anti‑PD‑L1 therapy (JITC, 2024) (tian2024targetingoxidativephosphorylation pages 1-2).

## Gene/Protein Annotations with Ontology Terms
- VHL (HGNC:12687): GO:0001666 response to hypoxia; GO:0006511 ubiquitin-dependent protein catabolic process; nucleus/cytosol (nguyen2024novelapproacheswith pages 1-2, coffey2024metabolicalterationsin pages 30-32).
- EPAS1/HIF2A (HGNC:3373): GO:0001525 angiogenesis; GO:0006355 regulation of transcription; nucleus (nguyen2024novelapproacheswith pages 1-2).
- PBRM1 (HGNC:30022): GO:0006338 chromatin remodeling; nucleus/chromatin (coffey2024metabolicalterationsin pages 30-32).
- BAP1 (HGNC:949): GO:0016570 histone deubiquitination; nucleus (coffey2024metabolicalterationsin pages 30-32).
- SETD2 (HGNC:15920): GO:0018024 histone lysine methylation (H3K36me3); nucleus (coffey2024metabolicalterationsin pages 30-32).
- MET (HGNC:7029): GO:0007167 enzyme linked receptor protein signaling; plasma membrane (coffey2024metabolicalterationsin pages 25-26).
- FH (HGNC:3700): GO:0006108 malate metabolic process; mitochondrion (coffey2024metabolicalterationsin pages 8-9).

## Phenotype Associations (HP terms)
- HP:0009725 Renal cell carcinoma; HP:0002664 Anemia; HP:0003002 Cachexia; HP:0031286 Hypercalcemia; HP:0100244 Osteolytic bone lesions; HP:0031351 Immunodeficiency due to T‑cell dysfunction (nguyen2024novelapproacheswith pages 1-2, bezwada2024mitochondrialcomplexi pages 1-2, tian2024targetingoxidativephosphorylation pages 1-2).

## Cell Type Involvement (CL terms)
- CL:0002328 Proximal tubule epithelial cell (cell of origin in many RCCs). CL:0000738 Regulatory T cell. CL:0000235 Macrophage (MRC1+FOLR2+ TAMs). CL:0000625 Endothelial cell (coffey2024metabolicalterationsin pages 30-32, tian2024targetingoxidativephosphorylation pages 1-2).

## Anatomical Locations (UBERON terms)
- UBERON:0001225 Kidney cortex (primary). UBERON:0001474 Bone (metastatic niche) (bezwada2024mitochondrialcomplexi pages 1-2).

## Chemical Entities (CHEBI)
- CHEBI:19508 Fumarate (oncometabolite in FH‑deficiency). CHEBI:30744 Glutamine (metabolic fuel). CHEBI:16651 L‑lactate (TME metabolite). Belzutifan (HIF‑2α inhibitor; drug entity) (coffey2024metabolicalterationsin pages 8-9, coffey2024metabolicalterationsin pages 11-13, coffey2024metabolicalterationsin pages 30-32, nguyen2024novelapproacheswith pages 1-2).

## Evidence Items (with URLs and dates)
- Bezwada et al., Nature, 14 Aug 2024. “Mitochondrial complex I promotes kidney cancer metastasis.” https://doi.org/10.1038/s41586-024-07812-3 (bezwada2024mitochondrialcomplexi pages 1-2).
- Tian et al., J Immunother Cancer, Feb 2024. “Targeting oxidative phosphorylation to increase the efficacy of immune‑combination therapy in RCC.” https://doi.org/10.1136/jitc-2023-008226 (tian2024targetingoxidativephosphorylation pages 1-2).
- Coffey & Simon, Nat Rev Nephrol, Jan 2024. “Metabolic alterations in hereditary and sporadic RCC.” https://doi.org/10.1038/s41581-023-00800-2 (coffey2024metabolicalterationsin pages 11-13, coffey2024metabolicalterationsin pages 19-21, coffey2024metabolicalterationsin pages 25-26, coffey2024metabolicalterationsin pages 30-32, coffey2024metabolicalterationsin pages 36-38).
- Nguyen et al., Cancers, 31 Jan 2024. “Novel approaches with HIF‑2α targeted therapies in mRCC.” https://doi.org/10.3390/cancers16030601 (nguyen2024novelapproacheswith pages 1-2).
- Wu et al., Nature Communications, 20 Mar 2023. “Epigenetic and transcriptomic characterization…ccRCC.” https://doi.org/10.1038/s41467-023-37211-7 (coffey2024metabolicalterationsin pages 30-32).

## Expert Synthesis and Implications
- Mechanistic integration indicates: (i) VHL/HIF‑2α is foundational in ccRCC, (ii) chromatin remodelers modulate EMT/inflammation programs and TME engagement, (iii) metabolic states are stage‑dependent (primary vs metastatic), with therapeutic windows differing across disease phases, and (iv) immunometabolic features (OXPHOS/hypoxia, tryptophan metabolism) condition ICI responses. These insights argue for phase‑adapted metabolic targeting (e.g., complex I inhibition in metastatic settings) and rational ICI combinations guided by OXPHOS hypoxia signatures and spatial immune readouts (bezwada2024mitochondrialcomplexi pages 1-2, tian2024targetingoxidativephosphorylation pages 1-2, coffey2024metabolicalterationsin pages 36-38).


References

1. (nguyen2024novelapproacheswith pages 1-2): Charles B. Nguyen, Eugene Oh, Piroz Bahar, Ulka N. Vaishampayan, Tobias Else, and Ajjai S. Alva. Novel approaches with hif-2α targeted therapies in metastatic renal cell carcinoma. Cancers, 16:601, Jan 2024. URL: https://doi.org/10.3390/cancers16030601, doi:10.3390/cancers16030601. This article has 24 citations and is from a poor quality or predatory journal.

2. (coffey2024metabolicalterationsin pages 30-32): Nathan J. Coffey and M. Celeste Simon. Metabolic alterations in hereditary and sporadic renal cell carcinoma. Nature reviews. Nephrology, 20:233-250, Jan 2024. URL: https://doi.org/10.1038/s41581-023-00800-2, doi:10.1038/s41581-023-00800-2. This article has 36 citations.

3. (bezwada2024mitochondrialcomplexi pages 1-2): Divya Bezwada, Luigi Perelli, Nicholas P. Lesner, Ling Cai, Bailey Brooks, Zheng Wu, Hieu S. Vu, Varun Sondhi, Daniel L. Cassidy, Stacy Kasitinon, Sherwin Kelekar, Feng Cai, Arin B. Aurora, McKenzie Patrick, Ashley Leach, Rashed Ghandour, Yuanyuan Zhang, Duyen Do, Phyllis McDaniel, Jessica Sudderth, Dennis Dumesnil, Sara House, Tracy Rosales, Alan M. Poole, Yair Lotan, Solomon Woldu, Aditya Bagrodia, Xiaosong Meng, Jeffrey A. Cadeddu, Prashant Mishra, Javier Garcia-Bermudez, Ivan Pedrosa, Payal Kapur, Kevin D. Courtney, Craig R. Malloy, Giannicola Genovese, Vitaly Margulis, and Ralph J. DeBerardinis. Mitochondrial complex i promotes kidney cancer metastasis. Nature, 633:923-931, Aug 2024. URL: https://doi.org/10.1038/s41586-024-07812-3, doi:10.1038/s41586-024-07812-3. This article has 86 citations and is from a highest quality peer-reviewed journal.

4. (tian2024targetingoxidativephosphorylation pages 1-2): Jihua Tian, Jing Luo, Xing Zeng, Chunjin Ke, Yanan Wang, Zhenghao Liu, Le Li, Yangjun Zhang, Zhiquan Hu, and Chunguang Yang. Targeting oxidative phosphorylation to increase the efficacy of immune-combination therapy in renal cell carcinoma. Journal for Immunotherapy of Cancer, 12:e008226, Feb 2024. URL: https://doi.org/10.1136/jitc-2023-008226, doi:10.1136/jitc-2023-008226. This article has 19 citations and is from a domain leading peer-reviewed journal.

5. (coffey2024metabolicalterationsin pages 11-13): Nathan J. Coffey and M. Celeste Simon. Metabolic alterations in hereditary and sporadic renal cell carcinoma. Nature reviews. Nephrology, 20:233-250, Jan 2024. URL: https://doi.org/10.1038/s41581-023-00800-2, doi:10.1038/s41581-023-00800-2. This article has 36 citations.

6. (coffey2024metabolicalterationsin pages 19-21): Nathan J. Coffey and M. Celeste Simon. Metabolic alterations in hereditary and sporadic renal cell carcinoma. Nature reviews. Nephrology, 20:233-250, Jan 2024. URL: https://doi.org/10.1038/s41581-023-00800-2, doi:10.1038/s41581-023-00800-2. This article has 36 citations.

7. (coffey2024metabolicalterationsin pages 36-38): Nathan J. Coffey and M. Celeste Simon. Metabolic alterations in hereditary and sporadic renal cell carcinoma. Nature reviews. Nephrology, 20:233-250, Jan 2024. URL: https://doi.org/10.1038/s41581-023-00800-2, doi:10.1038/s41581-023-00800-2. This article has 36 citations.

8. (coffey2024metabolicalterationsin pages 25-26): Nathan J. Coffey and M. Celeste Simon. Metabolic alterations in hereditary and sporadic renal cell carcinoma. Nature reviews. Nephrology, 20:233-250, Jan 2024. URL: https://doi.org/10.1038/s41581-023-00800-2, doi:10.1038/s41581-023-00800-2. This article has 36 citations.

9. (coffey2024metabolicalterationsin pages 8-9): Nathan J. Coffey and M. Celeste Simon. Metabolic alterations in hereditary and sporadic renal cell carcinoma. Nature reviews. Nephrology, 20:233-250, Jan 2024. URL: https://doi.org/10.1038/s41581-023-00800-2, doi:10.1038/s41581-023-00800-2. This article has 36 citations.

10. (zhang2025thepathogenesisand pages 9-9): Yifan Zhang, Shengli Zhang, Hongbin Sun, and Luwei Xu. The pathogenesis and therapeutic implications of metabolic reprogramming in renal cell carcinoma. Cell Death Discovery, Apr 2025. URL: https://doi.org/10.1038/s41420-025-02479-9, doi:10.1038/s41420-025-02479-9. This article has 27 citations and is from a peer-reviewed journal.

11. (zhang2025thepathogenesisand pages 11-11): Yifan Zhang, Shengli Zhang, Hongbin Sun, and Luwei Xu. The pathogenesis and therapeutic implications of metabolic reprogramming in renal cell carcinoma. Cell Death Discovery, Apr 2025. URL: https://doi.org/10.1038/s41420-025-02479-9, doi:10.1038/s41420-025-02479-9. This article has 27 citations and is from a peer-reviewed journal.

12. (zhang2025thepathogenesisand pages 8-9): Yifan Zhang, Shengli Zhang, Hongbin Sun, and Luwei Xu. The pathogenesis and therapeutic implications of metabolic reprogramming in renal cell carcinoma. Cell Death Discovery, Apr 2025. URL: https://doi.org/10.1038/s41420-025-02479-9, doi:10.1038/s41420-025-02479-9. This article has 27 citations and is from a peer-reviewed journal.