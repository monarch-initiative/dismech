---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-24T18:43:43.622945'
end_time: '2026-01-24T18:49:36.142030'
duration_seconds: 352.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: HER2-Positive Breast Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 19
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** HER2-Positive Breast Cancer
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **HER2-Positive Breast Cancer**.
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
- **Disease Name:** HER2-Positive Breast Cancer
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **HER2-Positive Breast Cancer**.
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


Plan and approach
We created a structured plan to (i) retrieve recent, authoritative literature (2023–2024 priority) and landmark references on HER2-positive breast cancer pathophysiology; (ii) extract mechanisms of signaling, resistance, immune effects, and CNS tropism; (iii) enumerate molecular players and ontology mappings; and (iv) synthesize a comprehensive, citable report. We prioritized reviews and analyses explicitly addressing HER2 signaling (HER2/HER3), PI3K/AKT/mTOR and RAS/MAPK cascades, resistance biology, brain metastases, and antibody–drug conjugate (ADC) mechanisms. This report cites only the evidence gathered.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: HER2-Positive Breast Cancer
- MONDO ID: MONDO:0007254 (breast carcinoma; HER2-positive is a molecularly defined subtype)
- Category: Malignant neoplasm; solid tumor, breast

Pathophysiology description
- Key concepts and definitions. HER2-positive breast cancer is driven by amplification/overexpression of ERBB2 (HER2), a receptor tyrosine kinase of the ErbB/EGFR family. HER2 lacks a soluble ligand and signals largely via homo- and heterodimers—particularly HER2/HER3—potently activating PI3K/AKT/mTOR and RAS/RAF/MEK/ERK pathways that regulate proliferation, survival, metabolism, and invasion (URL: https://doi.org/10.3390/genes15070903, Jul 2024). Quote: “HER2/HER3 heterodimer is highly potent in activating downstream signaling pathways, such as PI3K/AKT and MAPK.” (cheng2024acomprehensivereview pages 5-6)
- Dysregulated signaling. HER2 amplification increases receptor density (often to millions of receptors/cell), enhancing ligand-independent dimerization and downstream signaling. Trastuzumab blocks HER2 ECD IV, inhibits HER2–HER3-driven PI3K signaling, and promotes ADCC, highlighting the centrality of PI3K/AKT and MAPK cascades in disease biology (URL: https://doi.org/10.3390/cancers16152635, Jul 2024) (cai2024depictingbiomarkersfor pages 2-4). Reviews consistently identify HER2 amplification/overexpression and HER2 heterodimerization as initiating events that “disrupt the balance between cell proliferation and apoptosis” through PI3K/AKT/mTOR and Ras/Raf/MEK/ERK activation (URL: https://doi.org/10.3390/ijms252413376, Dec 2024) (zhong2024thebiologicalroles pages 2-4).
- Cellular processes. Hyperactive PI3K/AKT enhances survival, cell cycle progression, glucose and lipid metabolism, and EMT/invasion; RAS/MAPK promotes proliferation and transcriptional programs. PI3K/AKT also shapes an immunosuppressive microenvironment (e.g., PD-L1, TAM recruitment), contributing to metastasis and therapeutic resistance (URL: https://doi.org/10.3390/ijms252413376, Dec 2024) (zhong2024thebiologicalroles pages 2-4, zhong2024thebiologicalroles pages 14-16).
- Immune mechanisms. Anti-HER2 mAbs (trastuzumab) exert Fc-mediated effects including ADCC and macrophage ADCP in addition to signaling blockade (URL: https://doi.org/10.3390/cancers16152635, Jul 2024) (cai2024depictingbiomarkersfor pages 2-4). ADCs add cytotoxic payload delivery and, depending on linker/payload, “bystander” killing of neighboring cells (URL: https://doi.org/10.3390/ijms252413376, Dec 2024) (zhong2024thebiologicalroles pages 1-2).
- Clinical phenotype and CNS tropism. HER2-positive disease comprises ~15–25% of breast cancers and is clinically aggressive with a high risk of brain metastases; approximately 25–50% of patients with HER2-positive metastatic breast cancer develop brain metastases during the disease course (URL: https://doi.org/10.3390/biomedicines13051153, May 2025) (miski2025her2positivebreastcancer—current pages 1-2) (zhong2024thebiologicalroles pages 1-2, zhong2024thebiologicalroles pages 2-4).

1) Core Pathophysiology
- Primary pathophysiological mechanisms. HER2 gene amplification/overexpression drives constitutive HER2 signaling, particularly via HER2/HER3 heterodimers, activating PI3K/AKT/mTOR and RAS/RAF/MEK/ERK pathways that promote proliferation, survival, and invasion (URL: https://doi.org/10.3390/genes15070903, Jul 2024; https://doi.org/10.3390/ijms252413376, Dec 2024) (cheng2024acomprehensivereview pages 5-6, zhong2024thebiologicalroles pages 2-4).
- Dysregulated molecular pathways. Central: PI3K/AKT/mTOR (lipid signaling PIP2→PIP3; AKT activation via PDK1 and mTORC2), RAS/RAF/MEK/ERK (MAPK) (URL: https://doi.org/10.3390/ijms252413376, Dec 2024) (zhong2024thebiologicalroles pages 2-4). Crosstalk with ER signaling in HR+/HER2+ disease enables escape from anti-HER2 therapy (URL: https://doi.org/10.3390/ijms252413376, Dec 2024; https://doi.org/10.3390/genes15070903, Jul 2024) (zhong2024thebiologicalroles pages 14-16, cheng2024acomprehensivereview pages 5-6).
- Cellular processes affected. Cell cycle progression (cyclin/CDK activation), survival and anti-apoptosis (AKT signaling), EMT and invasion (e.g., integrin/FAK/PI3K/AKT; lipid mediators), metabolic rewiring (AKT-driven glucose/lipid metabolism), and microenvironmental immune suppression (TAMs, CAFs) (URL: https://doi.org/10.3390/ijms252413376, Dec 2024) (zhong2024thebiologicalroles pages 14-16).

2) Key Molecular Players
- Genes/Proteins (HGNC): ERBB2/HER2 (HGNC:3430), ERBB3/HER3 (HGNC:3431), EGFR/ERBB1 (HGNC:3236), PIK3CA (HGNC:8975), PTEN (HGNC:9588), AKT1 (HGNC:391), MAPK1 (HGNC:6871), MAPK3 (HGNC:6877), GRB7 (HGNC:4567), ESR1 (HGNC:3467). Mechanistically, trastuzumab blocks HER2 ECD IV and reduces HER3 phosphorylation and PI3K signaling; HER2/HER3 dimers are potent PI3K activators; PIK3CA mutations and PTEN loss increase PI3K output; GRB7 can maintain downstream ERK/AKT signaling and contribute to resistance (URLs: https://doi.org/10.3390/cancers16152635, Jul 2024; https://doi.org/10.3390/genes15070903, Jul 2024; https://doi.org/10.3390/ijms252413376, Dec 2024) (cai2024depictingbiomarkersfor pages 2-4, cheng2024acomprehensivereview pages 5-6, zhong2024thebiologicalroles pages 14-16).
- Chemical entities (selected): anti-HER2 mAbs and ADCs (trastuzumab; ado-trastuzumab emtansine/T-DM1; trastuzumab deruxtecan/T-DXd), and TKIs (lapatinib, neratinib, tucatinib, pyrotinib) that variably penetrate the CNS and inhibit HER2/EGFR family kinases (URLs: https://doi.org/10.3390/ijms252413376, Dec 2024; https://doi.org/10.3390/cancers16152635, Jul 2024) (zhong2024thebiologicalroles pages 1-2, cai2024depictingbiomarkersfor pages 2-4).
- Cell types (CL terms): breast carcinoma epithelial cells (CL:0000066-derived), tumor-associated macrophages (CL:0000235), CD8+ T cells (CL:0000625), cancer-associated fibroblasts/fibroblasts (CL:0000057). Microenvironmental TAMs and CAFs promote PI3K/AKT signaling, immunosuppression, and EMT (URL: https://doi.org/10.3390/ijms252413376, Dec 2024) (zhong2024thebiologicalroles pages 14-16).
- Anatomical locations (UBERON): breast (UBERON:0000310), lymph node (UBERON:0000029), brain (UBERON:0000955), bone (UBERON:0001474), liver (UBERON:0002107), lung (UBERON:0002048). High CNS metastasis propensity in HER2+ disease is well documented (URL: https://doi.org/10.3390/biomedicines13051153, May 2025) (miski2025her2positivebreastcancer—current pages 1-2).

3) Biological Processes (GO annotation)
- Signaling: transmembrane receptor protein tyrosine kinase signaling pathway (GO:0007169); phosphatidylinositol 3-kinase signaling (GO:0014065); MAPK cascade (GO:0000165/GO:0000187); regulation of ER signaling (cross-talk) (GO:0030520). Activation of PI3K/AKT and MAPK downstream of HER2/HER3 is the central driver (URLs: https://doi.org/10.3390/ijms252413376, Dec 2024; https://doi.org/10.3390/genes15070903, Jul 2024) (zhong2024thebiologicalroles pages 2-4, cheng2024acomprehensivereview pages 5-6).
- Cellular programs: positive regulation of cell proliferation (GO:0008284); epithelial to mesenchymal transition (GO:0001837); regulation of cell cycle (GO:0051726); apoptotic process (GO:0006915); glucose metabolic process (GO:0006006) and lipid metabolic process (GO:0006629) via AKT; immune response/ADCC-related processes (GO:0006955). PI3K/AKT contributes to EMT and immune evasion (URL: https://doi.org/10.3390/ijms252413376, Dec 2024) (zhong2024thebiologicalroles pages 14-16).
- Transport and trafficking: endocytosis and receptor internalization (GO:0006897), vesicle-mediated transport (GO:0016192), lysosomal degradation (GO:0009056 context), relevant for HER2 turnover and ADC processing (URL: https://doi.org/10.3390/genes15070903, Jul 2024) (cheng2024acomprehensivereview pages 5-6).

4) Cellular Components (GO:CC)
- Plasma membrane (GO:0005886) and receptor complex at the membrane; early/late endosomes (GO:0005768/GO:0005769) and lysosome (GO:0005764) for receptor downregulation and ADC trafficking; cytosol (GO:0005829) and nucleus (GO:0005634) for downstream signaling transcriptional responses; extracellular region (GO:0005576) for ADC bystander payload diffusion (URLs: https://doi.org/10.3390/genes15070903, Jul 2024; https://doi.org/10.3390/ijms252413376, Dec 2024) (cheng2024acomprehensivereview pages 5-6, zhong2024thebiologicalroles pages 1-2).

5) Disease Progression
- Sequence of events. (i) ERBB2 amplification → HER2 overexpression (40–100×; up to ~2 million receptors/cell) enables ligand-independent dimerization (notably with HER3); (ii) acute activation of PI3K/AKT/mTOR and MAPK cascades drives proliferation/survival; (iii) microenvironmental conditioning (TAM/CAF-driven immunosuppression, EMT) promotes invasion and dissemination; (iv) clinical metastasis with high CNS risk, reflecting both tumor-intrinsic biology and limited BBB penetration of large antibodies; (v) therapy-induced selective pressures yield resistance via PI3K/AKT reactivation (PIK3CA, PTEN), HER family rewiring (HER3 upregulation), ER crosstalk, and ADC- or TKI-specific mechanisms (URLs: https://doi.org/10.3390/cancers16152635, Jul 2024; https://doi.org/10.3390/ijms252413376, Dec 2024; https://doi.org/10.3390/biomedicines13051153, May 2025) (cai2024depictingbiomarkersfor pages 2-4, zhong2024thebiologicalroles pages 2-4, miski2025her2positivebreastcancer—current pages 1-2).
- Stages/phases. Early localized disease (HER2-driven proliferation), regional spread (lymph nodes), distant metastasis with tropism for brain/liver/lung/bone; brain metastases are frequent (25–50%) and a major cause of mortality (URL: https://doi.org/10.3390/biomedicines13051153, May 2025) (miski2025her2positivebreastcancer—current pages 1-2).

6) Phenotypic Manifestations (HP terms)
- Breast carcinoma (HP:0100013) with aggressive clinical course (Neoplasm aggressiveness, HP:0025315), high relapse risk without targeted therapy, and frequent brain metastases (HP:0031426) and leptomeningeal disease in advanced cases (HP:0031746). Neurologic symptoms in CNS involvement include headache, seizures, and focal deficits (clinical phenotype aligns with brain metastasis biology) (URL: https://doi.org/10.3390/biomedicines13051153, May 2025) (miski2025her2positivebreastcancer—current pages 1-2).

Resistance to anti-HER2 therapies (mechanisms and recent insights)
- PI3K/AKT pathway alterations. PIK3CA activating mutations and PTEN loss restore downstream signaling and drive resistance to trastuzumab, pertuzumab, TKIs, and ADCs; PI3K/AKT activation also promotes EMT and immune evasion (URL: https://doi.org/10.3390/ijms252413376, Dec 2024) (zhong2024thebiologicalroles pages 1-2, zhong2024thebiologicalroles pages 2-4, zhong2024thebiologicalroles pages 14-16).
- HER family rewiring. Upregulation of HER3 and maintenance of HER2–HER3 signaling sustain PI3K activation under HER2 blockade; ECD alterations and increased HER2 expression can reduce antibody efficacy (URL: https://doi.org/10.3390/ijms252413376, Dec 2024) (zhong2024thebiologicalroles pages 2-4).
- ER crosstalk (HR+/HER2+). Approximately half of HER2+ tumors express ER; bidirectional crosstalk allows ER-driven escape from anti-HER2 therapy, supporting combined endocrine plus anti-HER2 or PI3K/AKT/mTOR blockade (URLs: https://doi.org/10.3390/ijms252413376, Dec 2024; https://doi.org/10.3390/genes15070903, Jul 2024) (zhong2024thebiologicalroles pages 14-16, cheng2024acomprehensivereview pages 5-6).
- ADC-specific resistance. Mechanisms include reduced target antigen/heterogeneity, impaired internalization/trafficking, lysosomal dysfunction, drug efflux, and payload-specific alterations (e.g., TOP1 mutations with DXd). Design features (cleavable linkers, DAR, hydrophilic masking) modulate bystander effects and resistance profiles (URL: https://doi.org/10.3390/molecules30143026, Jul 2025) (li2025recentresearchadvances pages 15-17).
- BBB and brain metastasis biology. Large antibodies have poor BBB penetration, permitting CNS relapse even with systemic control; CNS-active TKIs (e.g., tucatinib, neratinib) and potent ADCs (e.g., T-DXd) have improved intracranial activity, changing management of HER2+ brain metastases (URL: https://doi.org/10.3390/biomedicines13051153, May 2025) (miski2025her2positivebreastcancer—current pages 1-2).

Immune mechanisms and ADC pharmacology
- ADCC/ADCP. Trastuzumab engages Fcγ receptors on NK cells and macrophages, mediating ADCC/ADCP and contributing significantly to efficacy; it also reduces HER2/HER3 signaling and can increase PTEN activity via Src inhibition (URL: https://doi.org/10.3390/cancers16152635, Jul 2024) (cai2024depictingbiomarkersfor pages 2-4).
- ADC bystander effect and cytotoxicity. Modern ADCs (e.g., T-DXd) use cleavable linkers and membrane-permeable payloads to produce bystander killing, enhancing efficacy in heterogeneous tumors; this property is repeatedly emphasized in recent reviews (URL: https://doi.org/10.3390/ijms252413376, Dec 2024) (zhong2024thebiologicalroles pages 1-2).

Recent developments and latest research (2023–2024 priority)
- Centrality of PI3K/AKT in resistance and therapeutic combinations. 2024 reviews summarize how PI3K/AKT alterations, microenvironmental crosstalk, and ER signaling sustain resistance, motivating rational combinations (e.g., anti-HER2 + endocrine ± PI3K/AKT/mTOR inhibitors) (URL: https://doi.org/10.3390/ijms252413376, Dec 2024) (zhong2024thebiologicalroles pages 1-2, zhong2024thebiologicalroles pages 14-16).
- Updated mechanistic reviews of HER2 biology. 2024 synthesis details HER2 regulation, HER2/HER3 potency, and post-translational control (e.g., ubiquitination, HSP90) relevant to receptor turnover and drug sensitivity (URL: https://doi.org/10.3390/genes15070903, Jul 2024) (cheng2024acomprehensivereview pages 5-6).
- Biomarkers of resistance. 2024 review catalogs predictive biomarkers for resistance across mAbs, TKIs, and ADCs, including PIK3CA/PTEN, HER family rewiring, and immune contexture, with treatment implications (URL: https://doi.org/10.3390/cancers16152635, Jul 2024) (cai2024depictingbiomarkersfor pages 1-2, cai2024depictingbiomarkersfor pages 2-4).

Current applications and real-world implementations
- Standard-of-care anti-HER2 backbones (trastuzumab + pertuzumab + taxane) and use of TKIs and ADCs in advanced settings remain central, with evolving adoption of CNS-active regimens for brain metastases (neratinib, tucatinib, T-DM1, T-DXd) (URL: https://doi.org/10.3390/biomedicines13051153, May 2025) (miski2025her2positivebreastcancer—current pages 1-2).

Expert opinions and analysis
- Reviews converge on: (i) HER2/HER3-driven PI3K/AKT as the dominant oncogenic axis; (ii) resistance via PI3K/AKT reactivation, HER3 upregulation, ER crosstalk, and ADC/TKI-specific mechanisms; (iii) need for rational combinations and CNS-active strategies due to BBB constraints and high BrM incidence (URLs: https://doi.org/10.3390/ijms252413376, Dec 2024; https://doi.org/10.3390/cancers16152635, Jul 2024; https://doi.org/10.3390/genes15070903, Jul 2024) (zhong2024thebiologicalroles pages 1-2, zhong2024thebiologicalroles pages 2-4, cai2024depictingbiomarkersfor pages 1-2, zhong2024thebiologicalroles pages 14-16, cheng2024acomprehensivereview pages 5-6, cai2024depictingbiomarkersfor pages 2-4).

Relevant statistics and data
- Incidence: HER2-positive constitutes ~15–25% of breast cancers (2024 reviews) (URLs: https://doi.org/10.3390/ijms252413376, Dec 2024; https://doi.org/10.3390/cancers16152635, Jul 2024) (zhong2024thebiologicalroles pages 1-2, cai2024depictingbiomarkersfor pages 1-2).
- Receptor abundance: HER2 amplification can yield ~25–50 copies of ERBB2 and ~40–100-fold increase in receptor number (≈2 million receptors/cell) (URL: https://doi.org/10.3390/cancers16152635, Jul 2024) (cai2024depictingbiomarkersfor pages 2-4).
- CNS risk: 25–50% of HER2-positive metastatic breast cancer patients develop brain metastases, a leading contributor to mortality (URL: https://doi.org/10.3390/biomedicines13051153, May 2025) (miski2025her2positivebreastcancer—current pages 1-2).

Ontology-linked annotations
- Genes/Proteins (HGNC): ERBB2 (HGNC:3430), ERBB3 (HGNC:3431), PIK3CA (HGNC:8975), PTEN (HGNC:9588), AKT1 (HGNC:391), MAPK1 (HGNC:6871), MAPK3 (HGNC:6877), ESR1 (HGNC:3467), GRB7 (HGNC:4567). Evidence: signaling and resistance roles as above (zhong2024thebiologicalroles pages 1-2, zhong2024thebiologicalroles pages 2-4, zhong2024thebiologicalroles pages 14-16, cheng2024acomprehensivereview pages 5-6, cai2024depictingbiomarkersfor pages 2-4).
- Biological Processes (GO): GO:0007169; GO:0014065; GO:0000165/GO:0000187; GO:0008284; GO:0001837; GO:0006915; GO:0006006; GO:0006629; GO:0006955; GO:0016192 (zhong2024thebiologicalroles pages 2-4, zhong2024thebiologicalroles pages 14-16, cheng2024acomprehensivereview pages 5-6).
- Cellular Components (GO:CC): GO:0005886; GO:0005768/GO:0005769; GO:0005764; GO:0005829; GO:0005634; GO:0005576 (cheng2024acomprehensivereview pages 5-6, zhong2024thebiologicalroles pages 1-2).
- Phenotype associations (HP): HP:0100013; HP:0025315; HP:0031426; HP:0031746 (miski2025her2positivebreastcancer—current pages 1-2).
- Cell types (CL): CL:0000066; CL:0000235; CL:0000625; CL:0000057 (zhong2024thebiologicalroles pages 14-16).
- Anatomical locations (UBERON): UBERON:0000310; UBERON:0000029; UBERON:0000955; UBERON:0001474; UBERON:0002107; UBERON:0002048 (miski2025her2positivebreastcancer—current pages 1-2).
- Chemical entities (CHEBI; selected metabolites central to signaling): PIP2 (CHEBI:18348), PIP3 (CHEBI:16618). Therapeutics are referenced by name due to inconsistent CHEBI coverage for biologics/ADCs (zhong2024thebiologicalroles pages 2-4).

Direct supporting quotations
- “HER2/HER3 heterodimer is highly potent in activating downstream signaling pathways, such as PI3K/AKT and MAPK.” (URL: https://doi.org/10.3390/genes15070903, Jul 2024) (cheng2024acomprehensivereview pages 5-6)
- “HER2-targeted therapies work by preventing receptor dimerization … and by inhibiting kinase activity … The PI3K/AKT pathway is frequently altered … and plays a central role in proliferation and drug resistance.” (URL: https://doi.org/10.3390/ijms252413376, Dec 2024) (zhong2024thebiologicalroles pages 1-2)
- “Trastuzumab … binds HER2 ECD IV … and [induces] ADCC … [and] inhibits PI3K/AKT signaling … by promoting PTEN activity (via Src inhibition).” (URL: https://doi.org/10.3390/cancers16152635, Jul 2024) (cai2024depictingbiomarkersfor pages 2-4)
- “Approximately 25–50% of patients with HER2-positive breast cancer experience brain metastases.” (URL: https://doi.org/10.3390/biomedicines13051153, May 2025) (miski2025her2positivebreastcancer—current pages 1-2)

Evidence items with URLs and dates
- Zhong et al., 2024, Int J Mol Sci (Dec 2024). PI3K/AKT centrality in resistance; mechanisms and combinations. URL: https://doi.org/10.3390/ijms252413376 (zhong2024thebiologicalroles pages 1-2, zhong2024thebiologicalroles pages 2-4, zhong2024thebiologicalroles pages 14-16)
- Cheng, 2024, Genes (Jul 2024). HER2 biology and HER2/HER3 potency and regulation. URL: https://doi.org/10.3390/genes15070903 (cheng2024acomprehensivereview pages 5-6)
- Cai et al., 2024, Cancers (Jul 2024). Biomarkers of resistance; clinical agents; mechanistic roles for ADCC/PI3K. URL: https://doi.org/10.3390/cancers16152635 (cai2024depictingbiomarkersfor pages 1-2, cai2024depictingbiomarkersfor pages 2-4)
- Miski et al., 2025, Biomedicines (May 2025). CNS tropism; 25–50% BrM; therapeutic landscape including CNS-active agents. URL: https://doi.org/10.3390/biomedicines13051153 (miski2025her2positivebreastcancer—current pages 1-2)
- Li et al., 2025, Molecules (Jul 2025). ADC design features and resistance modes; TOP1 payload context. URL: https://doi.org/10.3390/molecules30143026 (li2025recentresearchadvances pages 15-17)

Notes on scope and limitations
- Where possible, we prioritized 2023–2024 sources; several 2024 reviews directly address HER2 signaling and resistance. Some quantitative epidemiology (CNS risk) is from a 2025 synthesis but aligns with longstanding observations. Mechanistic details are consistent across multiple 2024 reviews. Future work can add primary PMIDs for individual molecular events (e.g., specific PIK3CA/PTEN mutations and clinical correlations) and incorporate guideline updates for HER2-low as new evidence is fully appraised.


References

1. (cheng2024acomprehensivereview pages 5-6): Xiaoqing Cheng. A comprehensive review of her2 in cancer biology and therapeutics. Genes, Jul 2024. URL: https://doi.org/10.3390/genes15070903, doi:10.3390/genes15070903. This article has 191 citations and is from a poor quality or predatory journal.

2. (cai2024depictingbiomarkersfor pages 2-4): Alvan Cai, Yuan Chen, Lily S. Wang, John K. Cusick, and Yihui Shi. Depicting biomarkers for her2-inhibitor resistance: implication for therapy in her2-positive breast cancer. Cancers, 16:2635, Jul 2024. URL: https://doi.org/10.3390/cancers16152635, doi:10.3390/cancers16152635. This article has 9 citations and is from a poor quality or predatory journal.

3. (zhong2024thebiologicalroles pages 2-4): Hanyi Zhong, Ziling Zhou, Han Wang, Ruo Wang, Kunwei Shen, Renhong Huang, and Zheng Wang. The biological roles and clinical applications of the pi3k/akt pathway in targeted therapy resistance in her2-positive breast cancer: a comprehensive review. International Journal of Molecular Sciences, 25:13376, Dec 2024. URL: https://doi.org/10.3390/ijms252413376, doi:10.3390/ijms252413376. This article has 26 citations and is from a poor quality or predatory journal.

4. (zhong2024thebiologicalroles pages 14-16): Hanyi Zhong, Ziling Zhou, Han Wang, Ruo Wang, Kunwei Shen, Renhong Huang, and Zheng Wang. The biological roles and clinical applications of the pi3k/akt pathway in targeted therapy resistance in her2-positive breast cancer: a comprehensive review. International Journal of Molecular Sciences, 25:13376, Dec 2024. URL: https://doi.org/10.3390/ijms252413376, doi:10.3390/ijms252413376. This article has 26 citations and is from a poor quality or predatory journal.

5. (zhong2024thebiologicalroles pages 1-2): Hanyi Zhong, Ziling Zhou, Han Wang, Ruo Wang, Kunwei Shen, Renhong Huang, and Zheng Wang. The biological roles and clinical applications of the pi3k/akt pathway in targeted therapy resistance in her2-positive breast cancer: a comprehensive review. International Journal of Molecular Sciences, 25:13376, Dec 2024. URL: https://doi.org/10.3390/ijms252413376, doi:10.3390/ijms252413376. This article has 26 citations and is from a poor quality or predatory journal.

6. (miski2025her2positivebreastcancer—current pages 1-2): Hanna Miski, Kamila Krupa, Michał Piotr Budzik, Andrzej Deptała, and Anna Badowska-Kozakiewicz. Her2-positive breast cancer—current treatment management and new therapeutic methods for brain metastasis. Biomedicines, 13:1153, May 2025. URL: https://doi.org/10.3390/biomedicines13051153, doi:10.3390/biomedicines13051153. This article has 1 citations and is from a poor quality or predatory journal.

7. (li2025recentresearchadvances pages 15-17): Junmin Li, Xue Li, Ruixin Fu, Yakun Fang, Chunmei Zhang, Bingbing Ma, Yanan Ding, CX Shi, and Qingfeng Zhou. Recent research advances in her2-positive breast cancer concerning targeted therapy drugs. Molecules, Jul 2025. URL: https://doi.org/10.3390/molecules30143026, doi:10.3390/molecules30143026. This article has 3 citations and is from a poor quality or predatory journal.

8. (cai2024depictingbiomarkersfor pages 1-2): Alvan Cai, Yuan Chen, Lily S. Wang, John K. Cusick, and Yihui Shi. Depicting biomarkers for her2-inhibitor resistance: implication for therapy in her2-positive breast cancer. Cancers, 16:2635, Jul 2024. URL: https://doi.org/10.3390/cancers16152635, doi:10.3390/cancers16152635. This article has 9 citations and is from a poor quality or predatory journal.