---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-24T18:43:44.278509'
end_time: '2026-01-24T18:51:59.968998'
duration_seconds: 495.69
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ALK-Rearranged Non-Small Cell Lung Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** ALK-Rearranged Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **ALK-Rearranged Non-Small Cell Lung Cancer**.
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
- **Disease Name:** ALK-Rearranged Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **ALK-Rearranged Non-Small Cell Lung Cancer**.
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


Disease Pathophysiology Research Report

Target Disease
- Disease Name: ALK-Rearranged Non-Small Cell Lung Cancer (NSCLC)
- MONDO ID: Not retrieved in this evidence set
- Category: Thoracic oncology; lung adenocarcinoma subtype driven by ALK gene rearrangements

Plan (concise)
1) Aggregate recent primary reviews and mechanistic studies (emphasis 2023–2024). 2) Extract core pathophysiology, downstream signaling, cellular programs, TME features, co-alterations, resistance mechanisms, and clinical correlates. 3) Compile ontology-grounded annotations. 4) Synthesize progression and phenotype links. 5) Produce tables for ontology mapping and provide fully cited narrative. (testa2024alkrearrangedlungadenocarcinoma pages 1-2, parvaresh2024unravelingthepotential pages 24-27, lucia2025nonsmallcelllung pages 2-3)

Pathophysiology description (narrative)
Definition and driver biology
ALK-rearranged NSCLC is defined by chromosomal rearrangements that fuse the ALK tyrosine kinase domain to partner genes, most commonly EML4, creating a ligand-independent oncoprotein that constitutively activates receptor tyrosine kinase signaling and drives lung adenocarcinogenesis (approx. 2–8% of LUAD; commonly 2–3%) (Testa et al., Tumori, 2024; DOI:10.1177/03008916231202149; URL: https://doi.org/10.1177/03008916231202149) (testa2024alkrearrangedlungadenocarcinoma pages 1-2). “EML4-ALK arises from different EML4 breakpoints producing main variants—variant 1, variant 2, and variant 3” with variant architecture influencing stability and localization (testa2024alkrearrangedlungadenocarcinoma pages 1-2). Variant biology shapes oncogenic output: all variants retain EML4’s trimerization domain enabling ALK autophosphorylation; V1/V2 have incomplete TAPE domains (HSP90 dependency), whereas V3 is a short variant that co-localizes with microtubules and shows distinct signaling condensates (bioRxiv summary, 2025, variant overview) (jimenez2025unravelingtherapeuticstrategies pages 31-34).

Downstream molecular pathways
EML4-ALK engages canonical RTK cascades that mediate proliferation, survival, motility, and adaptive resistance, notably: RAS/RAF/MEK/ERK (MAPK), PI3K/AKT/mTOR, JAK/STAT (especially STAT3), and PLCγ-driven DAG/IP3 signaling; adaptor proteins (e.g., GRB2, SHC, IRS-1) propagate these signals (2024–2025 reviews) (jimenez2025unravelingtherapeuticstrategies pages 28-31, parvaresh2024unravelingthepotential pages 9-11). Preclinical and integrative reviews emphasize that co-inhibition of ALK with MEK or STAT3 can lower survivin, increase BIM, and resensitize resistant cells; ALK post-translational methylation by SMYD2 promotes downstream AKT activation and can be blocked to reduce ALK phosphorylation and tumor growth (Biomedicines, 2024; DOI:10.3390/biomedicines12020297; URL: https://doi.org/10.3390/biomedicines12020297) (parvaresh2024unravelingthepotential pages 13-14, parvaresh2024unravelingthepotential pages 11-13).

Cellular programs affected
- Proliferation and survival: constitutive ALK signaling upregulates pro-survival programs via STAT3 (BCL2 family, survivin) and PI3K–AKT, while MAPK promotes mitogenic transcription (parvaresh2024unravelingthepotential pages 11-13, parvaresh2024unravelingthepotential pages 9-11).
- EMT, migration, invasion: EMT is linked to specific resistance states; for example, “The EML4‑ALK G1202R on-target mutation induces EMT…increasing migration/invasion via STAT3/Slug,” and MMP9-mediated ALK cleavage can enhance motility via β-catenin nuclear effects (Biomedicines 2024) (parvaresh2024unravelingthepotential pages 13-14, parvaresh2024unravelingthepotential pages 9-11).
- Chromatin/transcriptional remodeling and plasticity: YAP/TAZ programs (with AXL/EGFR/TGFBR2 upregulation) and lineage plasticity are implicated in bypass resistance and histologic transformation (jimenez2025unravelingtherapeuticstrategies pages 42-46, parvaresh2024unravelingthepotential pages 13-14).

Tumor microenvironment (TME) and immunobiology
ALK+ NSCLC generally exhibits an immunosuppressive TIME with relatively low effective CD8+ T-cell activity and enrichment of suppressive subsets (Tregs and/or M2 macrophages), contributing to poor response to PD-1/PD-L1 blockade; TKI initiation can transiently increase CD8+ T cells, but longer-term treatment fosters immunosuppressive remodeling (Frontiers in Immunology 2025; JITC 2024) (lucia2025nonsmallcelllung pages 2-3, parvaresh2024unravelingthepotential pages 13-14). Clinically relevant correlates include low-to-variable PD-L1 expression and typically low tumor mutational burden (TMB), aligning with reduced ICI efficacy; emphasis is shifting to alternative immunomodulatory approaches (adoptive cells, vaccines) (lucia2025nonsmallcelllung pages 2-3, parvaresh2024unravelingthepotential pages 24-27). Importantly, CNS tropism is frequent at baseline (≈20% present with brain metastases), guiding the use of CNS-penetrant TKIs (jimenez2025unravelingtherapeuticstrategies pages 34-37).

Key molecular players (with ontology references) and co-alterations
- Genes/Proteins (HGNC): ALK (driver kinase), EML4 (fusion partner), TP53 (~30% co-altered, associated with inferior TKI outcomes), MET (amplification as bypass), EGFR (ligand-driven activation as bypass), CDKN2A/B (co-deletions), NF2 (loss → mTOR activation), KRAS (copy-number gains/reactivation of MAPK), PTPN11/SHP2 (RAS node dependency), SRC (adaptive resistance), STAT3, MYC, YAP1/WWTR1 (TAZ), AXL, TGFBR2, SMYD2, CDK9, MMP9 (testa2024alkrearrangedlungadenocarcinoma pages 1-2, jimenez2025unravelingtherapeuticstrategies pages 34-37, jimenez2025unravelingtherapeuticstrategies pages 42-46, parvaresh2024unravelingthepotential pages 13-14).
- Chemical entities (CHEBI): first-/second-/third-generation ALK TKIs (crizotinib, ceritinib, alectinib, brigatinib, lorlatinib) and next-wave inhibitors under development (e.g., 4th-generation concepts NVL‑655, TPX‑0131), and pathway co-inhibitors (EGFR, MEK, PARP) (testa2024alkrearrangedlungadenocarcinoma pages 1-2, parvaresh2024unravelingthepotential pages 24-27, parvaresh2024unravelingthepotential pages 13-14).
- Cell types (CL): CD8+ T cells (often functionally constrained), regulatory T cells (Tregs), and M2 macrophages (immunosuppressive) (lucia2025nonsmallcelllung pages 2-3, parvaresh2024unravelingthepotential pages 13-14).
- Anatomical locations (UBERON): lung alveolus (primary) and brain parenchyma (frequent metastasis) (testa2024alkrearrangedlungadenocarcinoma pages 1-2, jimenez2025unravelingtherapeuticstrategies pages 34-37).

Embedded ontology mapping table
| Category | Item (standardized term) | Ontology | Identifier | Role in disease (1-2 lines) | Key evidence (DOI/URL) | Year |
|---|---|---|---:|---|---|---:|
| Gene / Protein | ALK | HGNC | HGNC:ALK | Oncogenic fusion kinase driving constitutive RTK signaling (growth/survival). Primary target of ALK-TKIs. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | EML4 | HGNC | HGNC:EML4 | Fusion partner that provides oligomerization domains; variant structure (V1/V2/V3) alters localization/stability and influences oncogenicity and resistance. | https://doi.org/10.1177/03008916231202149 (testa2024alkrearrangedlungadenocarcinoma pages 1-2), https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | TP53 | HGNC | HGNC:TP53 | Frequent co-mutation; associated with worse TKI responses and shorter PFS/OS in ALK+ NSCLC. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | MET | HGNC | HGNC:MET | Bypass driver via amplification/reactivation causing ALK-independent resistance; targetable in combo strategies. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | EGFR | HGNC | HGNC:EGFR | Can act as bypass pathway (ligand-driven phosphorylation) in ALK-TKI resistance; rationale for combination EGFR+ALK in select cases. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | CDKN2A | HGNC | HGNC:CDKN2A | Tumor suppressor co-altered in some ALK+ tumors; implicates cell-cycle deregulation and worse prognosis. | https://doi.org/10.1177/03008916231202149 (testa2024alkrearrangedlungadenocarcinoma pages 1-2) | 2024 |
| Gene / Protein | CDKN2B | HGNC | HGNC:CDKN2B | Co-deletion with CDKN2A in subsets; contributes to cell-cycle control loss. | https://doi.org/10.1177/03008916231202149 (testa2024alkrearrangedlungadenocarcinoma pages 1-2) | 2024 |
| Gene / Protein | NF2 | HGNC | HGNC:NF2 | Loss can activate mTOR signaling and mediate lorlatinib resistance; suggests mTOR-targeted strategies. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | KRAS | HGNC | HGNC:KRAS | Rare co-alteration; RAS/MAPK reactivation via copy-number gain/reactivation can bypass ALK inhibition. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | PTPN11 (SHP2) | HGNC | HGNC:PTPN11 | Functional node upstream of RAS—identified as dependency in bypass resistance; combined SHP2+ALK inhibition under evaluation. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | SRC | HGNC | HGNC:SRC | Src-family kinase implicated in adaptive resistance/tolerance; Src inhibitors show preclinical synergy with ALK-TKIs. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | STAT3 | HGNC | HGNC:STAT3 | Downstream effector of ALK; mediates survival, EMT and resistance phenotypes (combination ALK+STAT3 can restore sensitivity). | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | MYC | HGNC | HGNC:MYC | ALK-driven transcriptional programs can upregulate MYC; MYC suppression sensitizes ALK+ cells to TKIs in preclinical data. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | YAP1 | HGNC | HGNC:YAP1 | YAP-driven transcription links to bypass (AXL/EGFR/TGFBR2) and lineage-plasticity-mediated resistance. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | WWTR1 (TAZ) | HGNC | HGNC:WWTR1 | Hippo-pathway effector (TAZ) cooperating with YAP in remodeling resistance-associated transcriptional programs. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | AXL | HGNC | HGNC:AXL | RTK upregulated via YAP/TAZ; contributes to EMT and bypass signaling. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | TGFBR2 | HGNC | HGNC:TGFBR2 | TGF-β receptor linked to EMT/lineage plasticity and resistance programs. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | SMYD2 | HGNC | HGNC:SMYD2 | Methyltransferase that post-translationally modifies ALK to promote AKT activation; SMYD2 inhibition synergizes with ALK-TKIs preclinically. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | CDK9 | HGNC | HGNC:CDK9 | ALK phosphorylation of CDK9 links to homologous recombination and PARP-inhibitor resistance; rationale for ALK+PARP combinations. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Gene / Protein | MMP9 | HGNC | HGNC:MMP9 | Mediates proteolytic ALK cleavage affecting β-catenin release and motility; implicated in invasion/migration. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Biological Process | MAPK cascade (RAS-RAF-MEK-ERK) | GO | GO:MAPK_cascade | Major mitogenic pathway downstream of ALK; reactivation (KRAS, DUSP6 loss) is common bypass route. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Biological Process | PI3K-AKT-mTOR signaling | GO | GO:PI3K-AKT_mTOR | Promotes survival and anti-apoptosis; NF2 loss → mTOR activation mediates lorlatinib resistance. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Biological Process | JAK-STAT cascade | GO | GO:JAK-STAT | STAT3-driven survival and EMT programs downstream of ALK; contributes to resistance and prosurvival gene expression. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Biological Process | Phospholipase C-activating receptor signaling (PLCγ) | GO | GO:PLC_gamma_pathway | ALK activates PLCγ → PKC/Ca2+ signaling affecting proliferation and cytoskeletal dynamics. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Biological Process | Epithelial–mesenchymal transition (EMT) | GO | GO:EMT | EMT is induced by certain ALK mutations (e.g., G1202R) and correlates with invasion and therapeutic resistance. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Biological Process | Cell proliferation | GO | GO:cell_proliferation | Core oncogenic outcome of ALK signaling via MAPK/PI3K pathways. | https://doi.org/10.1177/03008916231202149 (testa2024alkrearrangedlungadenocarcinoma pages 1-2) | 2024 |
| Biological Process | Regulation of apoptosis / survival | GO | GO:apoptosis_regulation | ALK signaling upregulates BCL2/survivin and suppresses pro-apoptotic factors; key determinant of TKI response. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Biological Process | Chromatin remodeling / transcriptional reprogramming | GO | GO:chromatin_remodeling | Drives lineage plasticity, immunophenotype changes and SCLC/mesenchymal transformations on therapy pressure. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Biological Process | Cell migration / invasion | GO | GO:cell_migration_invasion | Downstream of EMT, MMP9 activity and cytoskeletal reorganization promoted by ALK fusions. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Biological Process | Immune suppression in TME | GO | GO:immune_suppression_TME | ALK+ tumors often display immunosuppressive TIME (low CD8, high Tregs/M2), limiting ICI responses. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Cellular Component | Plasma membrane | GO | GO:plasma_membrane | Location of RTK signaling complexes and receptor interactions (bypass RTKs). | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Cellular Component | Cytoplasm | GO | GO:cytoplasm | Subcellular compartment for many ALK fusion signaling events and cytosolic adaptor recruitment. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Cellular Component | Microtubules | GO | GO:microtubule | EML4 contribution to microtubule binding (variant-specific localization, e.g., V3) influencing signaling granules. | https://doi.org/10.1177/03008916231202149 (testa2024alkrearrangedlungadenocarcinoma pages 1-2) | 2024 |
| Cellular Component | Membraneless cytoplasmic granules | GO | GO:membraneless_granules | Variant-specific condensates concentrate RAS-MAPK components and modulate signaling strength. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Cellular Component | Nucleus | GO | GO:nucleus | Nuclear translocation of transcriptional effectors (β-catenin, MYC) mediates proliferation/invasion programs. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Cell Type | CD8+ T cell | CL | CL:CD8+_T_cell | Key antitumor effector; typically reduced/inactive in ALK+ TIME but can be transiently increased after TKI. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Cell Type | Regulatory T cell (Treg) | CL | CL:Treg | Enriched in ALK+ TIME in some studies, contributing to immunosuppression. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Cell Type | M2 macrophage | CL | CL:M2_macrophage | Immunosuppressive macrophage phenotype associated with ALK+ brain metastases and resistance milieu. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Cell Type | B cell | CL | CL:B_cell | Reduced/variable B cell infiltration reported; role in ALK+ TIME remains under study. | https://doi.org/10.1177/03008916231202149 (testa2024alkrearrangedlungadenocarcinoma pages 1-2) | 2024 |
| Anatomical Location | Lung alveolus (primary) | UBERON | UBERON:lung_alveolus | Primary site of tumorigenesis in lung adenocarcinoma harboring ALK fusions. | https://doi.org/10.1177/03008916231202149 (testa2024alkrearrangedlungadenocarcinoma pages 1-2) | 2024 |
| Anatomical Location | Brain parenchyma (metastasis) | UBERON | UBERON:brain_parenchyma | ALK+ NSCLC shows CNS tropism; brain metastases common and influence choice of CNS-penetrant TKIs. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Chemical Entity | Lorlatinib | CHEBI | CHEBI:Lorlatinib | Third-generation, CNS-penetrant ALK-TKI active against many single ALK mutations; resistance via compound mutations/bypass emerges. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Chemical Entity | Alectinib | CHEBI | CHEBI:Alectinib | Second-generation ALK inhibitor with superior CNS control vs crizotinib; frontline option. | https://doi.org/10.1177/03008916231202149 (testa2024alkrearrangedlungadenocarcinoma pages 1-2) | 2024 |
| Chemical Entity | Brigatinib | CHEBI | CHEBI:Brigatinib | Second-generation ALK-TKI with CNS activity; part of sequencing strategies. | https://doi.org/10.1177/03008916231202149 (testa2024alkrearrangedlungadenocarcinoma pages 1-2) | 2024 |
| Chemical Entity | Ceritinib | CHEBI | CHEBI:Ceritinib | Second-generation ALK inhibitor active post-crizotinib; resistance patterns include ALK mutations. | https://doi.org/10.1177/03008916231202149 (testa2024alkrearrangedlungadenocarcinoma pages 1-2) | 2024 |
| Chemical Entity | Crizotinib | CHEBI | CHEBI:Crizotinib | First-generation ALK/MET/ROS1 inhibitor; foundational TKI with earlier resistance patterns. | https://doi.org/10.1177/03008916231202149 (testa2024alkrearrangedlungadenocarcinoma pages 1-2) | 2024 |
| Chemical Entity | NVL-655 | CHEBI | CHEBI:NVL-655 | Fourth-generation ALK inhibitor in development with activity against lorlatinib-resistant compound mutations (preclinical/early clinical data). | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Chemical Entity | TPX-0131 | CHEBI | CHEBI:TPX-0131 | 4th-gen ALK inhibitor designed to overcome compound mutations; development-stage therapeutic strategy. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Chemical Entity | PARP inhibitors | CHEBI | CHEBI:PARP_inhibitor | Combination rationale with ALK inhibitors due to ALK→CDK9→HR axis; preclinical synergy reported. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Chemical Entity | MEK inhibitors | CHEBI | CHEBI:MEK_inhibitor | Target downstream MAPK reactivation in bypass resistance; ALK+MEK combos show preclinical promise. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |
| Chemical Entity | EGFR inhibitors | CHEBI | CHEBI:EGFR_inhibitor | Employed to target EGFR-driven bypass activation in select ALK-TKI resistant contexts. | https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14) | 2024 |


*Table: A compact ontology-mapped table linking genes, processes, compartments, cell types, locations and key drugs to their roles in ALK‑rearranged NSCLC, with evidence citations to recent reviews (2024). This aids database annotation and mechanistic curation.*

GO-aligned biological processes and cellular components
- Disrupted processes (GO): MAPK cascade; PI3K–AKT–mTOR signaling; JAK–STAT signaling; phospholipase C–activating signaling; epithelial–mesenchymal transition; regulation of apoptosis/survival; chromatin remodeling/transcriptional reprogramming; cell migration/invasion; immune suppression in TME. Evidence: synthesis from 2024–2025 mechanistic reviews indicating ALK→STAT3/ERK/AKT/PLCγ axes, EMT with G1202R, and TME suppression (jimenez2025unravelingtherapeuticstrategies pages 28-31, parvaresh2024unravelingthepotential pages 9-11, parvaresh2024unravelingthepotential pages 13-14, parvaresh2024unravelingthepotential pages 11-13).
- Cellular components (GO): plasma membrane (RTK complexes/bypass RTKs), cytoplasm (signalosomes), microtubules (variant V3 localization), membraneless cytoplasmic granules (condensates concentrating RAS-MAPK components), and nucleus (transcriptional effectors) (jimenez2025unravelingtherapeuticstrategies pages 31-34, parvaresh2024unravelingthepotential pages 9-11).

Disease progression: sequence of events
1) Initiation: ALK fusion formation (most commonly EML4‑ALK), generating a constitutively active ALK kinase chimera through EML4-mediated oligomerization and autophosphorylation (testa2024alkrearrangedlungadenocarcinoma pages 1-2, jimenez2025unravelingtherapeuticstrategies pages 31-34).
2) Early tumorigenesis: Oncogene addiction to ALK with activation of MAPK/PI3K/STAT3/PLCγ signaling, promoting proliferation, survival, and invasion programs (jimenez2025unravelingtherapeuticstrategies pages 28-31, parvaresh2024unravelingthepotential pages 11-13).
3) Clinical presentation: Often in younger, light/never-smokers; significant CNS tropism at diagnosis; relative immunologically “cold” TME (jimenez2025unravelingtherapeuticstrategies pages 34-37, lucia2025nonsmallcelllung pages 2-3).
4) Treatment phase: High sensitivity to ALK TKIs; CNS-penetrant agents (alectinib, brigatinib, lorlatinib) improve brain control versus crizotinib (testa2024alkrearrangedlungadenocarcinoma pages 1-2, bearz2025eml4alkupdateon pages 4-6).
5) Acquired resistance evolution: On-target ALK kinase-domain mutations (e.g., L1196M, I1171X, F1174X, G1269A, G1202R), frequently “compound” mutations after lorlatinib; ALK-independent bypass (MET amplification; EGFR/HER signaling; RAS/MAPK reactivation through SHP2, KRAS CN gains, DUSP6 loss; SRC activation); phenotypic plasticity including EMT and histologic transformation (squamous or small-cell) (jimenez2025unravelingtherapeuticstrategies pages 42-46, parvaresh2024unravelingthepotential pages 13-14).
6) Late-stage dynamics: Progressive TME immunosuppression during prolonged TKI exposure; potential opportunities for immunomodulatory strategies beyond PD-1/PD-L1 monotherapy (lucia2025nonsmallcelllung pages 2-3, parvaresh2024unravelingthepotential pages 24-27).

Phenotypic manifestations and clinical correlates
- Key clinical phenotypes: Lung adenocarcinoma with high likelihood of brain metastases at baseline and over the disease course; strong initial TKI responses with eventual resistance; generally limited benefit from standalone immune checkpoint blockade (jimenez2025unravelingtherapeuticstrategies pages 34-37, lucia2025nonsmallcelllung pages 2-3).
- Variant-specific risk: V3 is frequently associated with more aggressive clinical behavior and enrichment of G1202R upon resistance; V1 more often selects for L1196M/F1174C (2025 synthesis drawing on earlier variant literature) (jimenez2025unravelingtherapeuticstrategies pages 42-46, jimenez2025unravelingtherapeuticstrategies pages 31-34).
- PD-L1/TMB: Typically low TMB and variable PD-L1; immunosuppressive TIME features (Tregs, M2 macrophages) likely contribute to modest ICI efficacy (lucia2025nonsmallcelllung pages 2-3, parvaresh2024unravelingthepotential pages 13-14).

Recent developments and latest research (prioritized 2023–2024)
- Consolidated fusion/variant biology and clinical implications updated through 2024 Tumori review (Testa et al.), including major EML4‑ALK variants and therapeutic framing (Sep 2024; https://doi.org/10.1177/03008916231202149) (testa2024alkrearrangedlungadenocarcinoma pages 1-2).
- Mechanistic advances detailing ALK-driven pathways, EMT linkage to G1202R, ALK methylation by SMYD2→AKT activation, and multi-target combination strategies (ALK+MEK; ALK+STAT3; ALK+EGFR; ALK+PARP) (Biomedicines, Jan 2024; https://doi.org/10.3390/biomedicines12020297) (parvaresh2024unravelingthepotential pages 13-14, parvaresh2024unravelingthepotential pages 11-13).
- Resistance in the second-/third-generation era: reviews and syntheses underscore the prevalence of ALK-independent resistance without kinase-domain mutations after earlier TKIs (~50–70% post-crizotinib; ~50% post-2G), with MET, EGFR, YAP/TAZ, SRC, SHP2/RAS reactivation and NF2/mTOR signaling as recurrent routes; after lorlatinib, complex on-target compound mutations and bypass co-emerge (2025 synthesis of 2023–2024 observations) (jimenez2025unravelingtherapeuticstrategies pages 42-46).
- Tumor microenvironment dynamics under TKIs: short-term TKI can transiently enhance antitumor immunity (CD8+), whereas long-term therapy fosters an immunosuppressive TME—guiding timing and design of combinations (JITC, Jun 2024; DOI:10.1136/jitc-2024-009165) (lucia2025nonsmallcelllung pages 2-3, parvaresh2024unravelingthepotential pages 13-14).
- Brain metastasis management: later-generation TKIs (alectinib, brigatinib, lorlatinib) provide superior CNS control relative to crizotinib and inform frontline selection (IJMS update table, 2025; but CNS emphasis consistent with 2024 landscape) (bearz2025eml4alkupdateon pages 4-6, testa2024alkrearrangedlungadenocarcinoma pages 1-2).

Current applications and implementations
- Frontline therapy: alectinib, brigatinib, and lorlatinib as CNS-active first-line options; selection guided by comorbidities, CNS disease, and anticipated resistance patterns (testa2024alkrearrangedlungadenocarcinoma pages 1-2, bearz2025eml4alkupdateon pages 4-6).
- Resistance-guided therapy: molecular re-biopsy/ctDNA to define on-target mutations versus bypass mechanisms; lorlatinib for many single mutations; development of 4th‑generation ALK inhibitors (e.g., NVL‑655, TPX‑0131) and rational combinations (ALK+SHP2/MEK/mTOR/EGFR; ALK+PARP) for compound and bypass resistance (parvaresh2024unravelingthepotential pages 24-27, jimenez2025unravelingtherapeuticstrategies pages 42-46, parvaresh2024unravelingthepotential pages 13-14).
- Immunotherapy strategies: limited efficacy of PD-1/PD-L1 monotherapy; exploration of ALK vaccines and adoptive cellular strategies to overcome immunosuppression (parvaresh2024unravelingthepotential pages 24-27, lucia2025nonsmallcelllung pages 2-3).

Expert opinions and authoritative analyses
- Testa et al. (Tumori 2024) conclude that while “ALK-TKIs have improved outcomes…resistance mechanisms greatly limit durability,” and new strategies aim for long-term remission, underscoring the need for variant-aware and resistance-agnostic approaches (testa2024alkrearrangedlungadenocarcinoma pages 1-2).
- Cross-review synthesis highlights that a substantial fraction of progression events are ALK-independent, elevating the importance of bypass-pathway cotargeting (SHP2/RAS-MAPK, MET, EGFR) and vigilance for lineage transformation (jimenez2025unravelingtherapeuticstrategies pages 42-46).
- Immunology-focused analyses emphasize immunosuppressive TME characteristics in ALK+ disease and the dynamic remodeling under TKIs, supporting time-sensitive combinations rather than ICI monotherapy (lucia2025nonsmallcelllung pages 2-3, parvaresh2024unravelingthepotential pages 24-27).

Statistics and recent data points
- Prevalence: ALK fusions approximately 2–8% of LUAD (often cited 2–3%) (Sep 2024) (testa2024alkrearrangedlungadenocarcinoma pages 1-2).
- Variant distribution (ranges vary by cohort): V1 ~33–43%, V3 ~29–42% (2025 synthesis of variant literature; consistent with historical patterns) (jimenez2025unravelingtherapeuticstrategies pages 31-34, jimenez2025unravelingtherapeuticstrategies pages 34-37).
- Co-alterations: TP53 is the most frequent (~30% of EML4‑ALK) and is generally associated with worse TKI outcomes (2025 synthesis; 2024 updates) (jimenez2025unravelingtherapeuticstrategies pages 34-37).
- Resistance spectra: A large fraction of resistance after crizotinib and second-generation TKIs lacks detectable ALK kinase-domain mutations (~50–70% and ~50%, respectively), indicating prominent bypass resistance; lorlatinib resistance frequently involves compound ALK mutations plus bypass alterations (2025 synthesis summarizing 2023–2024 observations) (jimenez2025unravelingtherapeuticstrategies pages 42-46).
- CNS involvement: approximately 20% present with brain metastases at diagnosis (jimenez2025unravelingtherapeuticstrategies pages 34-37).

Evidence items (PMIDs/DOIs/URLs, publication dates)
- Testa U, Castelli G, Pelosi E. Alk‑rearranged lung adenocarcinoma: From molecular genetics to therapeutic targeting. Tumori. Sep 2024. DOI:10.1177/03008916231202149. URL: https://doi.org/10.1177/03008916231202149 (testa2024alkrearrangedlungadenocarcinoma pages 1-2).
- Parvaresh H, et al. Unraveling the Potential of ALK-Targeted Therapies in NSCLC. Biomedicines. Jan 2024. DOI:10.3390/biomedicines12020297. URL: https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14, parvaresh2024unravelingthepotential pages 11-13, parvaresh2024unravelingthepotential pages 9-11).
- De Lucia A, et al. NSCLC and the tumor microenvironment. Frontiers in Immunology. Feb 2025. DOI:10.3389/fimmu.2025.1515748. URL: https://doi.org/10.3389/fimmu.2025.1515748 (lucia2025nonsmallcelllung pages 2-3).
- Variant and resistance synthesis (EML4‑ALK V1/V3; on-target vs bypass; SHP2/MAPK/NF2‑mTOR; transformation). 2025 synthesis (bioRxiv-based and review integrations) (jimenez2025unravelingtherapeuticstrategies pages 34-37, jimenez2025unravelingtherapeuticstrategies pages 42-46, jimenez2025unravelingtherapeuticstrategies pages 28-31, jimenez2025unravelingtherapeuticstrategies pages 31-34).
- Clinical CNS control and first-line comparisons including post‑crizotinib sequences (summary table). IJMS 2025 update; aligns with 2024 practice trends (bearz2025eml4alkupdateon pages 4-6).

Ontology-grounded annotations
- Genes/Proteins (HGNC): ALK (HGNC:ALK); EML4 (HGNC:EML4); TP53 (HGNC:TP53); MET (HGNC:MET); EGFR (HGNC:EGFR); CDKN2A (HGNC:CDKN2A); CDKN2B (HGNC:CDKN2B); NF2 (HGNC:NF2); KRAS (HGNC:KRAS); PTPN11/SHP2 (HGNC:PTPN11); SRC (HGNC:SRC); STAT3 (HGNC:STAT3); MYC (HGNC:MYC); YAP1 (HGNC:YAP1); WWTR1/TAZ (HGNC:WWTR1); AXL (HGNC:AXL); TGFBR2 (HGNC:TGFBR2); SMYD2 (HGNC:SMYD2); CDK9 (HGNC:CDK9); MMP9 (HGNC:MMP9). Roles summarized above (testa2024alkrearrangedlungadenocarcinoma pages 1-2, parvaresh2024unravelingthepotential pages 13-14, jimenez2025unravelingtherapeuticstrategies pages 42-46).
- Biological Processes (GO): MAPK cascade; PI3K–AKT–mTOR signaling; JAK–STAT cascade; PLCγ-activating signaling; EMT; proliferation; apoptosis regulation; chromatin remodeling; migration/invasion; immune suppression in TME (jimenez2025unravelingtherapeuticstrategies pages 28-31, parvaresh2024unravelingthepotential pages 9-11, parvaresh2024unravelingthepotential pages 13-14).
- Cellular Components (GO): plasma membrane; cytoplasm; microtubules; membraneless cytoplasmic granules; nucleus (jimenez2025unravelingtherapeuticstrategies pages 31-34, parvaresh2024unravelingthepotential pages 9-11).
- Cell Types (CL): CD8+ T cell; regulatory T cell; M2 macrophage; B cell (lucia2025nonsmallcelllung pages 2-3, parvaresh2024unravelingthepotential pages 13-14, testa2024alkrearrangedlungadenocarcinoma pages 1-2).
- Anatomical Locations (UBERON): lung alveolus; brain parenchyma (testa2024alkrearrangedlungadenocarcinoma pages 1-2, jimenez2025unravelingtherapeuticstrategies pages 34-37).
- Chemical Entities (CHEBI): crizotinib, ceritinib, alectinib, brigatinib, lorlatinib, NVL‑655, TPX‑0131, EGFR inhibitors, MEK inhibitors, PARP inhibitors (testa2024alkrearrangedlungadenocarcinoma pages 1-2, parvaresh2024unravelingthepotential pages 24-27, bearz2025eml4alkupdateon pages 4-6, parvaresh2024unravelingthepotential pages 13-14).

Direct supporting quotes
- “EML4‑ALK arises from different EML4 breakpoints producing main variants—variant 1 (EML4 exon13::ALK exon20), variant 2 … and variant 3 (EML4 exon6a/6b::ALK exon20)” (Testa 2024) (testa2024alkrearrangedlungadenocarcinoma pages 1-2).
- “The EML4‑ALK G1202R on-target mutation induces EMT, increasing migration/invasion via STAT3 and Slug; combined ALK+STAT3 inhibition can restore TKI sensitivity” (Biomedicines 2024) (parvaresh2024unravelingthepotential pages 13-14).
- “A large fraction of patients progressing on crizotinib or second-generation inhibitors lack detectable kinase-domain point mutations…indicating widespread ALK-independent resistance” (2025 synthesis summarizing 2023–2024 observations) (jimenez2025unravelingtherapeuticstrategies pages 42-46).

Limitations
Some 2025 syntheses are used to summarize 2023–2024 findings where accessible; primary 2024 peer‑reviewed sources (Tumori; Biomedicines) support core mechanisms, while 2025 immunology and mechanistic syntheses are used for TME and resistance contextualization. Where possible, URLs and DOIs are provided.

References (with URLs/dates) mapped to context IDs
- Testa U, Castelli G, Pelosi E. Tumori. Sep 2024. https://doi.org/10.1177/03008916231202149 (testa2024alkrearrangedlungadenocarcinoma pages 1-2)
- Parvaresh H, et al. Biomedicines. Jan 2024. https://doi.org/10.3390/biomedicines12020297 (parvaresh2024unravelingthepotential pages 13-14, parvaresh2024unravelingthepotential pages 11-13, parvaresh2024unravelingthepotential pages 9-11)
- De Lucia A, et al. Frontiers in Immunology. Feb 2025. https://doi.org/10.3389/fimmu.2025.1515748 (lucia2025nonsmallcelllung pages 2-3)
- Diaz-Jimenez A. 2025 synthesis: variant distribution; resistance spectrum and bypass pathways including SHP2/RAS-MAPK, MET, EGFR, NF2/mTOR; lineage transformation (jimenez2025unravelingtherapeuticstrategies pages 34-37, jimenez2025unravelingtherapeuticstrategies pages 42-46, jimenez2025unravelingtherapeuticstrategies pages 28-31, jimenez2025unravelingtherapeuticstrategies pages 31-34)
- Bearz A, et al. IJMS update table (first-line/CNS control; sequencing context). Jan 2025. https://doi.org/10.3390/ijms26010308 (bearz2025eml4alkupdateon pages 4-6)

Citations for claims in text are provided at the end of the relevant sentences above using context IDs.

References

1. (testa2024alkrearrangedlungadenocarcinoma pages 1-2): Ugo Testa, Germana Castelli, and Elvira Pelosi. Alk-rearranged lung adenocarcinoma: from molecular genetics to therapeutic targeting. Tumori, 110:88-95, Sep 2024. URL: https://doi.org/10.1177/03008916231202149, doi:10.1177/03008916231202149. This article has 17 citations and is from a peer-reviewed journal.

2. (parvaresh2024unravelingthepotential pages 24-27): Hannaneh Parvaresh, Ghazaal Roozitalab, Fatemeh Golandam, Payam Behzadi, and Parham Jabbarzadeh Kaboli. Unraveling the potential of alk-targeted therapies in non-small cell lung cancer: comprehensive insights and future directions. Biomedicines, 12:297, Jan 2024. URL: https://doi.org/10.3390/biomedicines12020297, doi:10.3390/biomedicines12020297. This article has 42 citations and is from a poor quality or predatory journal.

3. (lucia2025nonsmallcelllung pages 2-3): Anna De Lucia, Lucia Mazzotti, Anna Gaimari, Matteo Zurlo, Roberta Maltoni, Claudio Cerchione, Sara Bravaccini, Angelo Delmonte, Lucio Crinò, Patricia Borges de Souza, Luigi Pasini, Fabio Nicolini, Fabrizio Bianchi, Manel Juan, Hugo Calderon, Chiara Magnoni, Luca Gazzola, Paola Ulivi, and Massimiliano Mazza. Non-small cell lung cancer and the tumor microenvironment: making headway from targeted therapies to advanced immunotherapy. Frontiers in Immunology, Feb 2025. URL: https://doi.org/10.3389/fimmu.2025.1515748, doi:10.3389/fimmu.2025.1515748. This article has 10 citations and is from a peer-reviewed journal.

4. (jimenez2025unravelingtherapeuticstrategies pages 31-34): A Diaz Jimenez. Unraveling therapeutic strategies and tumor suppressor functions in eml4-alk-driven lung tumorigenesis. Unknown journal, 2025.

5. (jimenez2025unravelingtherapeuticstrategies pages 28-31): A Diaz Jimenez. Unraveling therapeutic strategies and tumor suppressor functions in eml4-alk-driven lung tumorigenesis. Unknown journal, 2025.

6. (parvaresh2024unravelingthepotential pages 9-11): Hannaneh Parvaresh, Ghazaal Roozitalab, Fatemeh Golandam, Payam Behzadi, and Parham Jabbarzadeh Kaboli. Unraveling the potential of alk-targeted therapies in non-small cell lung cancer: comprehensive insights and future directions. Biomedicines, 12:297, Jan 2024. URL: https://doi.org/10.3390/biomedicines12020297, doi:10.3390/biomedicines12020297. This article has 42 citations and is from a poor quality or predatory journal.

7. (parvaresh2024unravelingthepotential pages 13-14): Hannaneh Parvaresh, Ghazaal Roozitalab, Fatemeh Golandam, Payam Behzadi, and Parham Jabbarzadeh Kaboli. Unraveling the potential of alk-targeted therapies in non-small cell lung cancer: comprehensive insights and future directions. Biomedicines, 12:297, Jan 2024. URL: https://doi.org/10.3390/biomedicines12020297, doi:10.3390/biomedicines12020297. This article has 42 citations and is from a poor quality or predatory journal.

8. (parvaresh2024unravelingthepotential pages 11-13): Hannaneh Parvaresh, Ghazaal Roozitalab, Fatemeh Golandam, Payam Behzadi, and Parham Jabbarzadeh Kaboli. Unraveling the potential of alk-targeted therapies in non-small cell lung cancer: comprehensive insights and future directions. Biomedicines, 12:297, Jan 2024. URL: https://doi.org/10.3390/biomedicines12020297, doi:10.3390/biomedicines12020297. This article has 42 citations and is from a poor quality or predatory journal.

9. (jimenez2025unravelingtherapeuticstrategies pages 42-46): A Diaz Jimenez. Unraveling therapeutic strategies and tumor suppressor functions in eml4-alk-driven lung tumorigenesis. Unknown journal, 2025.

10. (jimenez2025unravelingtherapeuticstrategies pages 34-37): A Diaz Jimenez. Unraveling therapeutic strategies and tumor suppressor functions in eml4-alk-driven lung tumorigenesis. Unknown journal, 2025.

11. (bearz2025eml4alkupdateon pages 4-6): Alessandra Bearz, Elisa Bertoli, Brigida Stanzione, Elisa De Carlo, Alessandro Del Conte, Martina Bortolot, Sara Torresan, Eleonora Berto, Valentina Da Ros, Giulia Maria Pelin, Kelly Fassetta, Silvia Rossetto, and Michele Spina. Eml4-alk: update on alk inhibitors. International Journal of Molecular Sciences, 26:308, Jan 2025. URL: https://doi.org/10.3390/ijms26010308, doi:10.3390/ijms26010308. This article has 7 citations and is from a poor quality or predatory journal.