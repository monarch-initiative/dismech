---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-24T18:43:44.192911'
end_time: '2026-01-24T18:51:50.113603'
duration_seconds: 485.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: EGFR-Mutant Non-Small Cell Lung Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** EGFR-Mutant Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **EGFR-Mutant Non-Small Cell Lung Cancer**.
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
- **Disease Name:** EGFR-Mutant Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **EGFR-Mutant Non-Small Cell Lung Cancer**.
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


Disease Pathophysiology Research Template

Target Disease
- Disease Name: EGFR-Mutant Non-Small Cell Lung Cancer (NSCLC)
- MONDO ID: MONDO:0010860 (non-small cell lung carcinoma); EGFR-mutant subset under molecularly defined NSCLC
- Category: Thoracic oncology; solid tumor, lung adenocarcinoma predominant

Research Objectives: Pathophysiology of EGFR-Mutant NSCLC focusing on molecular and cellular mechanisms underlying disease progression

Pathophysiology description
EGFR-mutant NSCLC is driven by activating mutations in EGFR (most commonly exon 19 deletions and exon 21 L858R), which cause constitutive kinase activation, ligand-independent dimerization, and chronic propagation of key oncogenic cascades including RAS/RAF/MEK/ERK (MAPK), PI3K/AKT/mTOR, and JAK/STAT (notably STAT3). These programs enforce proliferation, survival, and metastatic competence and establish oncogene addiction to EGFR signaling, explaining the initial sensitivity to EGFR tyrosine kinase inhibitors (TKIs) (first/second/third generation). Resistance emerges via on-target tertiary EGFR mutations (e.g., C797S after osimertinib), activation of bypass receptor tyrosine kinases (RTKs; MET and ERBB2/HER2 amplification), downstream pathway alterations, oncogenic fusions, and lineage plasticity (epithelial–mesenchymal transition [EMT] and histologic transformation). The tumor microenvironment (TME) is characteristically immunosuppressed, with impaired antigen presentation (HLA-I), enrichment of regulatory T cells (Tregs), and myeloid programs that collectively underlie the relatively poor efficacy of PD-1/PD-L1 blockade in this genotype. Recent work highlights epitranscriptomic and immune-checkpoint–driven mechanisms of primary and acquired resistance (NSUN2/YBX1/QSOX1 m5C axis; PD-L1–induced autophagy; PD-L2 upregulation), and a distinct biology of EGFR exon 20 insertions (ex20ins) that are less responsive to classical TKIs but targetable with newer agents and bispecific antibodies. (halder2023targetingtheegfr pages 4-6, zhang2024overcomingegfrtkiresistance pages 1-2, lim2025targetingthetumor pages 2-3, romaniello2025strategiestoovercome pages 1-2, li2025multimodalomicsanalysis pages 1-2)

| Category | Entity (symbol/name) | Ontology IDs | Role in EGFRm NSCLC | Key 2023–2024 Evidence (DOI URL, year) |
|---|---|---|---|---|
| Receptor (driver) | EGFR (EGFR) | HGNC:3236; GO:0007169 | Primary oncogenic driver; oncogene addiction; target of successive-generation TKIs | https://doi.org/10.1080/14728222.2023.2218613 (2023) (halder2023targetingtheegfr pages 4-6) |
| Pathway (proliferation) | MAPK cascade (RAS/RAF/MEK/ERK) | GO:0000165 | Mediates proliferation & differentiation downstream of EGFR | https://doi.org/10.1080/14728222.2023.2218613 (2023) (halder2023targetingtheegfr pages 4-6) |
| Pathway (survival/metabolism) | PI3K–AKT–mTOR | GO:0014065 | Promotes survival, metabolic rewiring and contributes to TKI resistance when reactivated | https://doi.org/10.1016/j.pccm.2024.08.002 (2024) (zhang2024overcomingegfrtkiresistance pages 1-2) |
| Pathway (inflammatory/survival) | JAK–STAT (STAT3) | GO:0007259; HGNC:11364 | Drives pro-survival / immune-modulatory programs downstream of EGFR | https://doi.org/10.1080/14728222.2023.2218613 (2023) (halder2023targetingtheegfr pages 4-6) |
| Bypass RTK (resistance) | MET (MET) | HGNC:7029 | MET amplification/overexpression is a frequent EGFR‑independent bypass causing osimertinib resistance; targetable clinically | https://doi.org/10.1016/j.pccm.2024.08.002 (2024) (zhang2024overcomingegfrtkiresistance pages 1-2) |
| Bypass RTK (resistance) | ERBB2 / HER2 (ERBB2) | HGNC:3430 | HER2 amplification or activation can bypass EGFR inhibition and drive progression | https://doi.org/10.1080/14728222.2023.2218613 (2023) (halder2023targetingtheegfr pages 4-6) |
| RTK (EMT driver) | AXL (AXL) | HGNC:905 | Promotes EMT, drug tolerance and cooperates with YAP-driven programs to confer resistance | https://doi.org/10.1080/14728222.2023.2218613 (2023) (halder2023targetingtheegfr pages 4-6) |
| Hippo effector | YAP1 / WWTR1 (YAP1 / TAZ) | HGNC:16252 / 12791 | YAP/TAZ activation induces transcriptional programs (e.g., AXL) that support EMT, stemness and TKI resistance | https://doi.org/10.1080/14728222.2023.2218613 (2023) (halder2023targetingtheegfr pages 4-6) |
| Lineage plasticity marker | NKX2-1 loss (basal-shift) | (NKX2-1 loss) | Loss can drive basal-shift / lineage transformation (LUAD → squamous/SCLC-like) associated with TKI resistance | https://doi.org/10.62347/wtmu5537 (2025) (yuan2025newadvancesin pages 22-22) |
| Tumor suppressors (cell cycle) | CDKN2A / CDKN2B loss | (CDKN2A/B loss) | Co‑loss often seen with lineage transformation and denotes aggressive, TKI‑resistant clones | https://doi.org/10.62347/wtmu5537 (2025) (yuan2025newadvancesin pages 22-22) |
| Apoptosis regulator | BIM / BCL2L11 | HGNC:994 | BIM deletion/polymorphism impairs TKI‑induced apoptosis and contributes to intrinsic resistance | https://doi.org/10.1080/14728222.2023.2218613 (2023) (halder2023targetingtheegfr pages 4-6) |
| Immune checkpoint | PD-L1 / CD274 | HGNC:17635 | Elevated PD-L1 can induce autophagy and associate with primary resistance to EGFR‑TKIs and immune evasion | https://doi.org/10.1080/14728222.2023.2218613 (2023) (halder2023targetingtheegfr pages 4-6) |
| Immune checkpoint | PD-L2 / PDCD1LG2 | HGNC:17636 | Upregulation linked to dynamic immune escape during EGFR‑TKI therapy and poorer immune responses | https://doi.org/10.1016/j.pccm.2024.08.002 (2024) (zhang2024overcomingegfrtkiresistance pages 1-2) |
| Antigen presentation | HLA class I downregulation | GO:0042612 | Reduced HLA‑I peptide presentation in EGFR‑mutant tumors impairs CD8+ T‑cell recognition and ICI efficacy | https://doi.org/10.1016/j.pccm.2024.08.002 (2024) (zhang2024overcomingegfrtkiresistance pages 1-2) |
| Epitranscriptomic axis | NSUN2–YBX1–QSOX1 (m5C) | HGNC: NSUN2:14274; YBX1:8014; QSOX1:22524 | Aberrant m5C hypermethylation (NSUN2) enhances QSOX1 translation via YBX1 and mediates intrinsic gefitinib resistance | https://doi.org/10.3892/ol.2025.15121 (2025) (tian2025egfrmutationsin pages 6-7) |
| Chemokine axis / Tregs | CCL17 / CCL22 → CCR4 | (chemokine–receptor axis) | Tumor recruitment of Tregs via CCL17/CCL22–CCR4 creates an immune‑excluded microenvironment in EGFR‑mutant LUAD | https://doi.org/10.3892/ol.2025.15121 (2025) (tian2025egfrmutationsin pages 6-7) |
| Cellular program | Epithelial–mesenchymal transition (EMT) | GO:0001837 | EMT underlies invasion, drug tolerance, and facilitates phenotypic transformation after TKIs | https://doi.org/10.1080/14728222.2023.2218613 (2023) (halder2023targetingtheegfr pages 4-6) |
| EGFR class (uncommon) | EGFR exon 20 insertions (ex20ins) | (EGFR ex20ins subgroup) | Structurally distinct activating mutations; historically TKI‑insensitive—new agents (amivantamab, mobocertinib, sunvozertinib) show activity | https://doi.org/10.3390/biomedicines13020470 (2025) (lim2025targetingthetumor pages 20-22) |
| On‑target resistance | EGFR C797S (tertiary) | (EGFR C797S) | Tertiary substitution that prevents irreversible binding of osimertinib; motivates 4th‑gen TKIs / PROTACs / bispecific strategies | https://doi.org/10.1080/14728222.2023.2218613 (2023) (halder2023targetingtheegfr pages 4-6) |
| Therapeutic (approved / key) | Osimertinib (3rd‑gen EGFR‑TKI) | (drug) | Standard first‑line/EGFR T790M‑active agent; improved PFS but eventual resistance via on‑ and off‑target mechanisms | https://doi.org/10.3390/ijms26072957 (2025) (romaniello2025strategiestoovercome pages 1-2) |
| Therapeutic (bispecific / exon20) | Amivantamab (EGFR–MET bispecific) | (drug) | Antibody strategy active against exon‑20 and MET‑driven resistance; used alone or in combination with chemo/TKIs | https://doi.org/10.3390/biomedicines13020470 (2025) (lim2025targetingthetumor pages 20-22) |


*Table: Compact reference table of key genes, pathways, cellular processes, resistance mechanisms and representative therapeutics in EGFR‑mutant NSCLC, with 2023–2024 (and closely related) literature evidence to support mechanistic annotations and experimental/clinical decision points.*

1) Core Pathophysiology
- Primary mechanisms: Constitutive EGFR activation drives MAPK, PI3K-AKT-mTOR, and JAK-STAT signaling, conferring proliferation and survival with oncogene addiction; apoptosis is counteracted in part by BIM (BCL2L11) loss/polymorphisms; resistance to TKIs is inevitable via on-target (C797S) and off-target mechanisms (MET/HER2 amplification, downstream nodes, RTK fusions, EMT/lineage shift). (halder2023targetingtheegfr pages 4-6, zhang2024overcomingegfrtkiresistance pages 1-2, romaniello2025strategiestoovercome pages 1-2)
- Dysregulated pathways: MAPK cascade (GO:0000165), PI3K signaling (GO:0014065), JAK-STAT (GO:0007259); immune pathways involving HLA-I antigen presentation are altered during treatment and resistance. (zhang2024overcomingegfrtkiresistance pages 1-2, halder2023targetingtheegfr pages 4-6)
- Affected cellular processes: Cell-cycle progression, survival, metabolic rewiring, migration/invasion (EMT), immune evasion (downregulated antigen presentation; Treg recruitment). (zhang2024overcomingegfrtkiresistance pages 1-2, halder2023targetingtheegfr pages 4-6, tian2025egfrmutationsin pages 6-7)

2) Key Molecular Players
- Genes/Proteins (HGNC): EGFR (HGNC:3236); MET (HGNC:7029); ERBB2/HER2 (HGNC:3430); AXL (HGNC:905); YAP1 (HGNC:16252) and WWTR1/TAZ (HGNC:12791) in Hippo signaling; STAT3 (HGNC:11364); BCL2L11/BIM (HGNC:994); CD274/PD-L1 (HGNC:17635); PDCD1LG2/PD-L2 (HGNC:17636); NSUN2 (HGNC:14274), YBX1 (HGNC:8014), QSOX1 (HGNC:22524). Mechanistic roles detailed in the embedded table. (halder2023targetingtheegfr pages 4-6, zhang2024overcomingegfrtkiresistance pages 1-2, tian2025egfrmutationsin pages 6-7)
- Chemical Entities (CHEBI/examples): Gefitinib (CHEBI:49342), Erlotinib (CHEBI:114785), Afatinib (CHEBI:85026), Dacomitinib (CHEBI:72596), Osimertinib (CHEBI:90959); Mobocertinib (CHEBI:187375); Bispecific antibody Amivantamab (EGFR/MET). (romaniello2025strategiestoovercome pages 1-2, lim2025targetingthetumor pages 20-22, zhang2024overcomingegfrtkiresistance pages 1-2)
- Cell Types (CL): Epithelial tumor cells (adenocarcinoma lineage), cancer-associated fibroblasts (CL:0002620), M2-like tumor-associated macrophages (~CL:0000863), CD8+ T cells (CL:0000625), regulatory T cells (CL:0000815). (zhang2024overcomingegfrtkiresistance pages 1-2, tian2025egfrmutationsin pages 6-7)
- Anatomical locations (UBERON): Lung (UBERON:0002048), alveolar regions; frequent CNS involvement during progression (clinical context). (zhang2024overcomingegfrtkiresistance pages 1-2)

3) Biological Processes (GO annotation)
- EGFR signaling pathway (GO:0038127); MAPK cascade (GO:0000165); PI3K signaling (GO:0014065); regulation of apoptotic process (GO:0042981); epithelial to mesenchymal transition (GO:0001837); antigen processing and presentation of peptide antigen via MHC class I (GO:0002474); negative regulation of T cell activation (GO:0050868). (halder2023targetingtheegfr pages 4-6, zhang2024overcomingegfrtkiresistance pages 1-2, tian2025egfrmutationsin pages 6-7)

4) Cellular Components
- Plasma membrane receptor complexes (EGFR/RTKs); cytosolic kinase cascades; nucleus (YAP/TAZ-TEAD transcriptional programs); endosomal/lysosomal compartments (autophagy); MHC class I peptide-loading complex. (halder2023targetingtheegfr pages 4-6, zhang2024overcomingegfrtkiresistance pages 1-2)

5) Disease Progression (sequence of events)
- Initiation: Acquisition of sensitizing EGFR mutation (e.g., exon 19 del, L858R) → constitutive EGFR kinase activation → chronic MAPK/PI3K/STAT signaling → adenocarcinoma development with oncogene addiction. (halder2023targetingtheegfr pages 4-6)
- Early treatment response: EGFR-TKIs induce tumor regression; median PFS ~9–13 months for first/second-generation TKIs; ~10–18.9 months for osimertinib depending on line; with combination chemotherapy in FLAURA2 PFS ~25.5 months. (zhang2024overcomingegfrtkiresistance pages 1-2, li2025multimodalomicsanalysis pages 1-2)
- Resistance emergence: On-target EGFR mutations (C797S most common post-osimertinib), bypass RTK activation (MET amplification ~7–25% reports), HER2 amplification, downstream node activation, fusions, and lineage plasticity (EMT; histologic transformation, 3–10% to SCLC or squamoid/basal-shift) leading to progression. (halder2023targetingtheegfr pages 4-6, zhang2024overcomingegfrtkiresistance pages 1-2)
- Immune evasion dynamics: Downregulated HLA-I and TME reprogramming with Treg recruitment and myeloid suppression reduce PD-1/PD-L1 benefit; PD-L1–induced autophagy and PD-L2 upregulation contribute to TKI resistance. (zhang2024overcomingegfrtkiresistance pages 1-2, halder2023targetingtheegfr pages 4-6)

6) Phenotypic Manifestations (HP terms)
- Lung adenocarcinoma (HP:0030078); cough, dyspnea, weight loss, and chest pain typical of NSCLC; frequent brain metastases during TKI resistance; paraneoplastic phenomena uncommon. Histologic transformation in a minority presents as small-cell lung cancer phenotype with neuroendocrine features. (zhang2024overcomingegfrtkiresistance pages 1-2, halder2023targetingtheegfr pages 4-6)

Recent developments and latest research (2023–2024 priority)
- Resistance catalogs and on-/off-target mechanisms: Comprehensive 2023 synthesis enumerating osimertinib resistance mutations at C797/G796/L792/L718/G724 and exon 20 changes with parallel bypass via MET/HER2 and EMT/AXL programs; emphasizes combination strategies and fourth-generation inhibitors in development (URL: https://doi.org/10.1080/14728222.2023.2218613). (halder2023targetingtheegfr pages 4-6)
- Tumor microenvironment rewiring during/after EGFR-TKI: 2024 review details primary versus acquired resistance, C797S predominance after osimertinib, and immunogenic shifts with impaired antigen processing/presentation as resistance develops (URL: https://doi.org/10.1016/j.pccm.2024.08.002). (zhang2024overcomingegfrtkiresistance pages 1-2)
- Immunologic features explaining poor ICI activity: Narrative review of EGFR-mutant TME immunology (2024) highlighting low immunogenicity, Treg/myeloid dominance, and limited PD-1/PD-L1 efficacy (URL: https://doi.org/10.1016/j.jncc.2024.06.004). (lim2025targetingthetumor pages 2-3)
- Hippo/YAP–AXL axis in EMT and resistance: 2024 review links YAP/TAZ activation to AXL upregulation and EMT-mediated TKI resistance (URL: https://doi.org/10.1038/s41417-024-00761-z). (halder2023targetingtheegfr pages 4-6)
- Epitranscriptomic resistance: RNA m5C hypermethylation via NSUN2 enhancing QSOX1 translation through YBX1 mediates intrinsic gefitinib resistance (2023) (URL: https://doi.org/10.1186/s12943-023-01780-4). (tian2025egfrmutationsin pages 6-7)
- Checkpoint-driven resistance: PD-L1 induces autophagy and primary EGFR-TKI resistance through MAPK signaling (2024) (URL: https://doi.org/10.1038/s41419-024-06945-7). PD-L2 upregulation dynamically contributes to EGFR-TKI resistance (2024) (URL: https://doi.org/10.1038/s41418-024-01317-2). (zhang2024overcomingegfrtkiresistance pages 1-2)
- Exon 20 insertions biology and therapies: 2023–2024 reviews summarize heterogeneity of ex20ins and efficacy of amivantamab, mobocertinib, and newer TKIs (URLs: https://doi.org/10.21037/tlcr-23-98; https://doi.org/10.3390/ijms25115917). (lim2025targetingthetumor pages 20-22)
- Combination/next-generation strategies: Fourth-generation EGFR inhibitors targeting C797S and biomarker-driven combination regimens (e.g., MET inhibitors with osimertinib) are focal; FLAURA2 (2023) and MARIPOSA (2024) support TKI+chemo and antibody+TKI strategies (URL: https://doi.org/10.32604/or.2025.059311). (li2025multimodalomicsanalysis pages 1-2)

Current applications and real-world implementations
- Standard of care: Osimertinib is first-line for sensitizing EGFR mutations, with subsequent strategy guided by resistance mechanisms (re-biopsy/NGS). (zhang2024overcomingegfrtkiresistance pages 1-2)
- MET-driven resistance: Dual EGFR/MET targeting (amivantamab) or MET TKIs combined with osimertinib (e.g., SAVANNAH/TATTON) are active approaches. (li2025multimodalomicsanalysis pages 1-2, zhang2024overcomingegfrtkiresistance pages 1-2)
- Exon 20 insertions: Amivantamab and mobocertinib are in use; newer TKIs (e.g., sunvozertinib/others) show promise in trials. (lim2025targetingthetumor pages 20-22)
- Immunotherapy: Single-agent PD-1/PD-L1 generally underperforms; combined strategies remain investigational given TME constraints. (lim2025targetingthetumor pages 2-3, zhang2024overcomingegfrtkiresistance pages 1-2)

Expert opinions and analysis
- Experts emphasize that resistance after osimertinib is “almost inevitable,” necessitating mechanism-directed therapy (fourth-generation TKIs, bispecifics, ADCs, MET/HER2 combinations, and TME-targeting). (romaniello2025strategiestoovercome pages 1-2)
- Multi-omics integration and trial platforms (e.g., ORCHARD) are advocated to tailor combinations to resistance profiles and to address the substantial fraction of “unknown mechanism” resistance after osimertinib (30–50%). (li2025multimodalomicsanalysis pages 1-2, zhang2024overcomingegfrtkiresistance pages 1-2)

Relevant statistics and data
- NSCLC comprises ~85% of lung cancers; EGFR mutations occur in ~10–20% of Western and ~30–50% of Asian patients; exon 19/L858R account for ~80–90% of common EGFR mutations. (romaniello2025strategiestoovercome pages 1-2, li2025multimodalomicsanalysis pages 1-2, zhang2024overcomingegfrtkiresistance pages 1-2)
- Median PFS: first/second-generation TKIs 9–13 months; osimertinib 10.1–18.9 months (line-dependent); FLAURA2 reported PFS 25.5 months for osimertinib+chemotherapy. (zhang2024overcomingegfrtkiresistance pages 1-2, li2025multimodalomicsanalysis pages 1-2)
- Resistance mechanism prevalence: Post–early TKIs T790M ~50%; post-osimertinib MET amplification commonly detected, reported ~7–25% across series; histologic transformation 3–10%. (halder2023targetingtheegfr pages 4-6, zhang2024overcomingegfrtkiresistance pages 1-2)

Evidence items with PMIDs/DOIs and URLs (selected)
- Halder et al., 2023. Targeting the EGFR signaling pathway in cancer therapy: What’s new in 2023? Expert Opin Ther Targets. DOI: 10.1080/14728222.2023.2218613. URL: https://doi.org/10.1080/14728222.2023.2218613 (mechanisms, resistance catalog, combinations). (halder2023targetingtheegfr pages 4-6)
- Zhang et al., 2024. Overcoming EGFR-TKI resistance by targeting the tumor microenvironment. PCCM. DOI: 10.1016/j.pccm.2024.08.002. URL: https://doi.org/10.1016/j.pccm.2024.08.002 (TME, resistance taxonomy, HLA changes). (zhang2024overcomingegfrtkiresistance pages 1-2)
- Dong et al., 2024. Immunological features of EGFR-mutant NSCLC. J Natl Cancer Center. DOI: 10.1016/j.jncc.2024.06.004. URL: https://doi.org/10.1016/j.jncc.2024.06.004 (TME immunology and ICI underperformance). (lim2025targetingthetumor pages 2-3)
- Liang et al., 2024. Hippo pathway in NSCLC. Cancer Gene Ther. DOI: 10.1038/s41417-024-00761-z. URL: https://doi.org/10.1038/s41417-024-00761-z (YAP/TAZ–AXL–EMT). (halder2023targetingtheegfr pages 4-6)
- Wang et al., 2023. NSUN2/YBX1/QSOX1 mediates intrinsic gefitinib resistance. Mol Cancer. DOI: 10.1186/s12943-023-01780-4. URL: https://doi.org/10.1186/s12943-023-01780-4 (epitranscriptomic mechanism). (tian2025egfrmutationsin pages 6-7)
- Li et al., 2024. PD-L1 induces autophagy and primary TKI resistance via MAPK. Cell Death Dis. DOI: 10.1038/s41419-024-06945-7. URL: https://doi.org/10.1038/s41419-024-06945-7 (checkpoint–autophagy link). (zhang2024overcomingegfrtkiresistance pages 1-2)
- Wang et al., 2024. PD-L2 drives resistance to EGFR-TKIs. Cell Death Differ. DOI: 10.1038/s41418-024-01317-2. URL: https://doi.org/10.1038/s41418-024-01317-2. (zhang2024overcomingegfrtkiresistance pages 1-2)
- Sentana‑Lledó et al., 2023. EGFR exon 20 insertions & ERBB2 mutations: targeted therapies. Transl Lung Cancer Res. DOI: 10.21037/tlcr-23-98. URL: https://doi.org/10.21037/tlcr-23-98 (ex20ins landscape). (lim2025targetingthetumor pages 20-22)
- Seo & Lim, 2024. Targeted therapies for EGFR exon 20 insertion. IJMS. DOI: 10.3390/ijms25115917. URL: https://doi.org/10.3390/ijms25115917 (ex20ins agents). (lim2025targetingthetumor pages 20-22)
- Romaniello et al., 2025. Strategies to overcome resistance to osimertinib. IJMS. DOI: 10.3390/ijms26072957. URL: https://doi.org/10.3390/ijms26072957 (strategy overview). (romaniello2025strategiestoovercome pages 1-2)
- Li et al., 2025 (multi-omics synthesis; includes FLAURA2/MARIPOSA context). Oncology Research. DOI: 10.32604/or.2025.059311. URL: https://doi.org/10.32604/or.2025.059311. (li2025multimodalomicsanalysis pages 1-2)

Gene/protein annotations with ontology terms (examples)
- EGFR (HGNC:3236): GO:0038127 (EGFR signaling), GO:0000165 (MAPK cascade), GO:0014065 (PI3K), GO:0007259 (JAK-STAT). Evidence: Halder 2023; Zhang 2024. (halder2023targetingtheegfr pages 4-6, zhang2024overcomingegfrtkiresistance pages 1-2)
- MET (HGNC:7029): GO:0007169 (signal transduction), resistance via amplification post‑osimertinib; clinical implication: MET inhibitor combinations. (zhang2024overcomingegfrtkiresistance pages 1-2, li2025multimodalomicsanalysis pages 1-2)
- ERBB2 (HGNC:3430): bypass activation leading to resistance; therapeutic implication: dual targeting/bispecifics. (halder2023targetingtheegfr pages 4-6)
- AXL (HGNC:905) and YAP1/WWTR1: GO:0001837 (EMT) regulation; resistance program. (halder2023targetingtheegfr pages 4-6)
- BCL2L11/BIM (HGNC:994): GO:0008630 (intrinsic apoptotic signaling). (halder2023targetingtheegfr pages 4-6)
- CD274/PD-L1 (HGNC:17635) & PDCD1LG2 (HGNC:17636): GO:0050868 (negative regulation of T cell activation); resistance via autophagy/immune evasion. (zhang2024overcomingegfrtkiresistance pages 1-2)
- NSUN2 (HGNC:14274), YBX1 (HGNC:8014), QSOX1 (HGNC:22524): RNA methylation (m5C) axis influencing translation and intrinsic resistance. (tian2025egfrmutationsin pages 6-7)

Phenotype associations (HP), cell types (CL), anatomical locations (UBERON), chemical entities (CHEBI)
- HP:0030078 Lung adenocarcinoma; HP:0004375 Brain neoplasm (metastatic predisposition in progression); HP:0002092 Dyspnea; HP:0002019 Weight loss. (zhang2024overcomingegfrtkiresistance pages 1-2)
- CL:0000625 CD8+ T cell; CL:0000815 Regulatory T cell; CL:0002620 Cancer-associated fibroblast; CL:0000863 macrophage (M2-like). (zhang2024overcomingegfrtkiresistance pages 1-2, tian2025egfrmutationsin pages 6-7)
- UBERON:0002048 Lung; UBERON:0000915 Pleura (metastatic involvement). (zhang2024overcomingegfrtkiresistance pages 1-2)
- CHEBI: Gefitinib 49342; Erlotinib 114785; Afatinib 85026; Dacomitinib 72596; Osimertinib 90959; Mobocertinib 187375. (halder2023targetingtheegfr pages 4-6, lim2025targetingthetumor pages 20-22)

Direct quotes (selected)
- “On-target mechanisms of resistance include new mutations (e.g., C797S) in the kinase domain of EGFR, while among the off-target mechanisms, amplification of MET or HER2… and phenotypic changes (e.g., EMT) have been described.” (IJMS 2025; URL: https://doi.org/10.3390/ijms26072957). (romaniello2025strategiestoovercome pages 1-2)
- “EGFR‑mutant tumors show altered antigen‑presentation… TKI treatment… resistance is accompanied by global inhibition of HLA peptide processing.” (PCCM 2024; URL: https://doi.org/10.1016/j.pccm.2024.08.002). (zhang2024overcomingegfrtkiresistance pages 1-2)
- “PD‑L1… promoted proliferation and autophagy and inhibited apoptosis… upregulation of PD‑L1 was critical in inducing autophagy… developing gefitinib resistance.” (Cell Death Dis 2024; URL: https://doi.org/10.1038/s41419-024-06945-7). (zhang2024overcomingegfrtkiresistance pages 1-2)

Caveats
- Some resistance mechanism prevalence estimates vary by cohort, assay (FISH vs NGS), and line of therapy. Re‑biopsy and comprehensive NGS are essential to guide targeted combinations and clinical trial enrollment. (zhang2024overcomingegfrtkiresistance pages 1-2, li2025multimodalomicsanalysis pages 1-2)

References (with URLs; 2023–2024 prioritized)
- Halder S et al., 2023. Expert Opin Ther Targets. https://doi.org/10.1080/14728222.2023.2218613 (halder2023targetingtheegfr pages 4-6)
- Zhang J et al., 2024. PCCM. https://doi.org/10.1016/j.pccm.2024.08.002 (zhang2024overcomingegfrtkiresistance pages 1-2)
- Dong Y et al., 2024. J Natl Cancer Center. https://doi.org/10.1016/j.jncc.2024.06.004 (lim2025targetingthetumor pages 2-3)
- Liang H et al., 2024. Cancer Gene Ther. https://doi.org/10.1038/s41417-024-00761-z (halder2023targetingtheegfr pages 4-6)
- Wang Y et al., 2023. Mol Cancer. https://doi.org/10.1186/s12943-023-01780-4 (tian2025egfrmutationsin pages 6-7)
- Li N et al., 2024. Cell Death Dis. https://doi.org/10.1038/s41419-024-06945-7 (zhang2024overcomingegfrtkiresistance pages 1-2)
- Wang S et al., 2024. Cell Death Differ. https://doi.org/10.1038/s41418-024-01317-2 (zhang2024overcomingegfrtkiresistance pages 1-2)
- Sentana‑Lledó D et al., 2023. TLCR. https://doi.org/10.21037/tlcr-23-98 (lim2025targetingthetumor pages 20-22)
- Seo D & Lim JH, 2024. IJMS. https://doi.org/10.3390/ijms25115917 (lim2025targetingthetumor pages 20-22)
- Romaniello D et al., 2025. IJMS. https://doi.org/10.3390/ijms26072957 (romaniello2025strategiestoovercome pages 1-2)
- Li Y et al., 2025. Oncology Research. https://doi.org/10.32604/or.2025.059311 (li2025multimodalomicsanalysis pages 1-2)

References

1. (halder2023targetingtheegfr pages 4-6): Sushanta Halder, Soumi Basu, Shobhit P. Lall, Apar K. Ganti, Surinder K. Batra, and Parthasarathy Seshacharyulu. Targeting the egfr signaling pathway in cancer therapy: what’s new in 2023? Expert Opinion on Therapeutic Targets, 27:305-324, May 2023. URL: https://doi.org/10.1080/14728222.2023.2218613, doi:10.1080/14728222.2023.2218613. This article has 78 citations and is from a peer-reviewed journal.

2. (zhang2024overcomingegfrtkiresistance pages 1-2): Jinsong Zhang, Natalie Vokes, Man Li, Jiachen Xu, Hua Bai, Jie Wang, Zhijie Wang, and Jianjun Zhang. Overcoming egfr-tki resistance by targeting the tumor microenvironment. Chinese Medical Journal Pulmonary and Critical Care Medicine, 2:151-161, Sep 2024. URL: https://doi.org/10.1016/j.pccm.2024.08.002, doi:10.1016/j.pccm.2024.08.002. This article has 22 citations.

3. (lim2025targetingthetumor pages 2-3): Jeong Uk Lim, Junyang Jung, Yeon Wook Kim, Chi Young Kim, Sang Hoon Lee, Dong Won Park, Sue In Choi, Wonjun Ji, Chang Dong Yeo, and Seung Hyeun Lee. Targeting the tumor microenvironment in egfr-mutant lung cancer: opportunities and challenges. Biomedicines, 13:470, Feb 2025. URL: https://doi.org/10.3390/biomedicines13020470, doi:10.3390/biomedicines13020470. This article has 8 citations and is from a poor quality or predatory journal.

4. (romaniello2025strategiestoovercome pages 1-2): Donatella Romaniello, Alessandra Morselli, and Ilaria Marrocco. Strategies to overcome resistance to osimertinib in egfr-mutated lung cancer. International Journal of Molecular Sciences, 26:2957, Mar 2025. URL: https://doi.org/10.3390/ijms26072957, doi:10.3390/ijms26072957. This article has 7 citations and is from a poor quality or predatory journal.

5. (li2025multimodalomicsanalysis pages 1-2): YUZHENG LI, LILI YU, SHIYAO ZHOU, HUA ZHOU, and QIBIAO WU. Multimodal omics analysis of the egfr signaling pathway in non-small cell lung cancer and emerging therapeutic strategies. Oncology Research, 33:1363-1376, May 2025. URL: https://doi.org/10.32604/or.2025.059311, doi:10.32604/or.2025.059311. This article has 5 citations and is from a peer-reviewed journal.

6. (yuan2025newadvancesin pages 22-22): Chun Yuan, Jun-Yan Yu, Chuanxiu Zeng, Mengchao Wang, Shao Zhang, Yan-Bo Huang, Xue-Song Yu, Fan-Ming Kong, and Liwei Chen. New advances in the treatment of egfr exon20ins mutant advanced nsclc. American journal of cancer research, 15 4:1852-1873, Jan 2025. URL: https://doi.org/10.62347/wtmu5537, doi:10.62347/wtmu5537. This article has 4 citations and is from a poor quality or predatory journal.

7. (tian2025egfrmutationsin pages 6-7): Zhe Tian, Lilan Cen, Feng Wei, Jue Dong, Yulan Huang, Yi Han, Zhibo Wang, Junhua Deng, and Yujie Jiang. Egfr mutations in non-small cell lung cancer: classification, characteristics and resistance to third-generation egfr-tyrosine kinase inhibitors (review). Oncology Letters, 30:1-11, Jun 2025. URL: https://doi.org/10.3892/ol.2025.15121, doi:10.3892/ol.2025.15121. This article has 5 citations and is from a peer-reviewed journal.

8. (lim2025targetingthetumor pages 20-22): Jeong Uk Lim, Junyang Jung, Yeon Wook Kim, Chi Young Kim, Sang Hoon Lee, Dong Won Park, Sue In Choi, Wonjun Ji, Chang Dong Yeo, and Seung Hyeun Lee. Targeting the tumor microenvironment in egfr-mutant lung cancer: opportunities and challenges. Biomedicines, 13:470, Feb 2025. URL: https://doi.org/10.3390/biomedicines13020470, doi:10.3390/biomedicines13020470. This article has 8 citations and is from a poor quality or predatory journal.