---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-14T23:39:35.155711'
end_time: '2025-12-14T23:45:00.601504'
duration_seconds: 325.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pulmonary hypertension
  mondo_id: ''
  category: Cardiovascular Disorder
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 15
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Pulmonary hypertension
- **MONDO ID:**  (if available)
- **Category:** Cardiovascular Disorder

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Pulmonary hypertension**.
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
- **Disease Name:** Pulmonary hypertension
- **MONDO ID:**  (if available)
- **Category:** Cardiovascular Disorder

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Pulmonary hypertension**.
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
- Disease Name: Pulmonary hypertension (PH); Pulmonary arterial hypertension (PAH)
- MONDO ID: MONDO_0005149 (pulmonary hypertension); PAH (EFO_0001361)
- Category: Cardiovascular Disorder

Pathophysiology description (narrative)
Pulmonary hypertension is a syndrome defined hemodynamically by mean pulmonary arterial pressure (mPAP) >20 mmHg and increased pulmonary vascular resistance, culminating in right-ventricular (RV) failure. In PAH (Group 1), the small distal pulmonary arteries develop “proliferative, fibrotic, and plexogenic” remodeling on a background of endothelial dysfunction, vasoconstriction, and thrombosis, driven by crosstalk among BMPR2/TGF-β superfamily signaling, inflammation/immune activation, metabolic reprogramming, mitochondrial dysfunction, hypoxia/HIF signaling, ion channel dysregulation, and epigenetic/transcriptional programs. These mechanisms involve pulmonary artery endothelial cells (PAECs), smooth muscle cells (PASMCs), fibroblasts/pericytes, and infiltrating immune cells, and are increasingly considered tractable therapeutic targets, including rebalancing of activin versus BMP signaling (e.g., sotatercept) and inhibition of PDGFRβ signaling (e.g., imatinib/seralutinib) (Sep 2023; American Journal of Respiratory and Critical Care Medicine) (johnson2023pulmonaryhypertensiona pages 1-2, johnson2023pulmonaryhypertensiona pages 2-4). A 2024 time-course transcriptomic study in rat experimental PH emphasizes the centrality of cell-cycle activation and proliferative programs during progression (Jun 2024; Scientific Reports) (luo2024transcriptomicprofilinghighlights pages 10-11). Recent pathway syntheses also underscore roles for hypoxia/HIF, NF-κB/NLRP3 inflammasome signaling, mitochondrial dysfunction, and endothelial-to-mesenchymal transition as drivers of remodeling and vasculopathy (Signal Transduction and Targeted Therapy, 2025) (aduamankwaah2025signalingpathwaysand pages 1-2, aduamankwaah2025signalingpathwaysand pages 29-30, aduamankwaah2025signalingpathwaysand pages 31-32).

Key concepts and definitions
- Hemodynamic definition: PH as mPAP >20 mmHg with elevated PVR; lowered thresholds emphasize early detection (Sep 2023; Am J Respir Crit Care Med) (johnson2023pulmonaryhypertensiona pages 1-2).
- Five clinical groups (ESC/ERS 2022): PAH (Group 1), left-heart disease (Group 2), lung disease/hypoxia (Group 3), chronic thromboembolic PH (Group 4), and miscellaneous (Group 5); shared and distinct mechanisms across groups (overview and mechanistic framing) (2025 synthesis citing 2022 guidelines) (aduamankwaah2025signalingpathwaysand pages 1-2).

1) Core Pathophysiology
- Primary mechanisms: endothelial dysfunction with apoptosis and clonal expansion; vasoconstriction; proliferative/plexiform arteriopathy; ECM deposition/fibrosis; in situ thrombosis; RV maladaptation (Sep 2023; Am J Respir Crit Care Med) (johnson2023pulmonaryhypertensiona pages 1-2, johnson2023pulmonaryhypertensiona pages 2-4).
- Dysregulated molecular pathways: imbalance in TGF-β superfamily tuning of BMP versus activin signaling (BMPR2 axis); growth factor/RTK signaling (e.g., PDGFRβ) driving PASMC/pericyte proliferation; hypoxia/HIF stabilization; inflammatory NF-κB/NLRP3 signaling; metabolic reprogramming (glycolytic shift, mTOR); mitochondrial dysfunction; ion-channel remodeling; epigenetic/transcription factor dysregulation (Sep 2023; Am J Respir Crit Care Med; 2025 pathway synthesis) (johnson2023pulmonaryhypertensiona pages 1-2, johnson2023pulmonaryhypertensiona pages 2-4, aduamankwaah2025signalingpathwaysand pages 1-2, aduamankwaah2025signalingpathwaysand pages 29-30, aduamankwaah2025signalingpathwaysand pages 31-32).
- Affected cellular processes: cell-cycle activation and apoptosis resistance in PASMCs and PAECs; EndMT; fibroblast activation; immune cell recruitment and cytokine/growth-factor secretion; ECM remodeling (Sep 2023; Am J Respir Crit Care Med; Jun 2024 Scientific Reports) (johnson2023pulmonaryhypertensiona pages 2-4, luo2024transcriptomicprofilinghighlights pages 10-11).

2) Key Molecular Players
- Genes/Proteins (HGNC):
  - BMPR2 (HGNC:1071) and BMP ligands (BMP9/BMP10) with downstream SMAD1/5/9: loss-of-function variants and signaling impairment are central in heritable and idiopathic PAH; restoration of SMAD1/5 signaling can rescue cellular phenotypes in models (Sep 2023) (johnson2023pulmonaryhypertensiona pages 2-4).
  - SMAD9 (HGNC:6765), ACVRL1 (ALK1; HGNC:171), ENG (endoglin; HGNC:3349): TGF-β/BMP axis components implicated in PAH (Sep 2023) (johnson2023pulmonaryhypertensiona pages 2-4).
  - EIF2AK4 (GCN2; HGNC:3255): causally linked to PVOD/PCH (Group 1’); recognized in PH genetics expansions (Sep 2023) (johnson2023pulmonaryhypertensiona pages 1-2).
  - KCNK3 (TASK-1; HGNC:11840): ion-channel mutations/aberrant function contribute to vasoconstriction and proliferation (Sep 2023) (johnson2023pulmonaryhypertensiona pages 1-2, johnson2023pulmonaryhypertensiona pages 2-4).
  - TBX4 (HGNC:11574), SOX17 (HGNC:11191): transcriptional regulators contributing to developmental and adult-onset PAH; SOX17 variants associated with severe phenotype (Sep 2023) (johnson2023pulmonaryhypertensiona pages 1-2, johnson2023pulmonaryhypertensiona pages 2-4).
  - CAV1 (HGNC:1527): caveolae/endothelial signaling, implicated in vascular dysfunction (Sep 2023) (johnson2023pulmonaryhypertensiona pages 2-4).
- Chemical Entities (CHEBI)/Drugs relevant to mechanisms and trials:
  - Sotatercept (ligand trap for activins/ActRIIA-Fc): rebalances pro-proliferative activin signaling, advancing outcomes in PAH (2023) (johnson2023pulmonaryhypertensiona pages 1-2).
  - PDGFR inhibitors: imatinib and inhaled seralutinib are highlighted mechanistically as anti-proliferative approaches targeting PASMC/pericyte expansion (2023) (johnson2023pulmonaryhypertensiona pages 1-2).
- Cell Types (CL): PAECs (CL:0000115); PASMCs (CL:0000746); adventitial fibroblasts (CL:0002553); pericytes (CL:0000669); macrophages and other immune cells (multiple CL terms) (mechanistic framing) (johnson2023pulmonaryhypertensiona pages 1-2, aduamankwaah2025signalingpathwaysand pages 1-2).
- Anatomical Locations (UBERON): small pulmonary arterioles (UBERON:0001981), pulmonary artery (UBERON:0002114), right ventricle (UBERON:0002080) (johnson2023pulmonaryhypertensiona pages 2-4).

3) Biological Processes (GO) disrupted
- TGF-β receptor signaling pathway; BMP signaling (GO:0007179, GO:0030509)
- Positive regulation of cell proliferation; cell cycle process (GO:0042127, GO:0022402) supported by in vivo transcriptomics in progressive PH (Jun 2024) (luo2024transcriptomicprofilinghighlights pages 10-11)
- Endothelial to mesenchymal transition (GO:0001837); regulation of apoptosis (GO:0042981) (aduamankwaah2025signalingpathwaysand pages 1-2, johnson2023pulmonaryhypertensiona pages 1-2)
- Response to hypoxia; HIF signaling (GO:0001666) (aduamankwaah2025signalingpathwaysand pages 1-2)
- Inflammatory response; NF-κB signaling; NLRP3 inflammasome activation (GO:0006954; pathway-level evidence) (aduamankwaah2025signalingpathwaysand pages 31-32)
- Mitochondrial organization; oxidative phosphorylation vs glycolysis switch (GO:0007005; GO:0006119/GO:0006096) (aduamankwaah2025signalingpathwaysand pages 1-2)
- Ion transmembrane transport (K+ channel activity; GO:0005267) (johnson2023pulmonaryhypertensiona pages 2-4)
- Epigenetic regulation of gene expression (GO:0040029) and lncRNA-mediated regulation (mechanistic overview, 2024) (liu2024rolesoflncrnas pages 1-2)

4) Cellular Components (GOCC)
- Plasma membrane/caveolae (CAV1) (GO:0005886; GO:0005901) (johnson2023pulmonaryhypertensiona pages 2-4)
- Cytosol and nucleus (SMAD translocation; transcription factor activity) (johnson2023pulmonaryhypertensiona pages 2-4)
- Mitochondrion (metabolic/ROS signaling) (aduamankwaah2025signalingpathwaysand pages 1-2)
- Extracellular space/ECM (fibrosis/remodeling) (johnson2023pulmonaryhypertensiona pages 2-4)

5) Disease Progression (sequence of events)
- Initiation: endothelial injury and apoptosis with loss of BMPR2/BMP protective signaling; early vasoconstriction from ion-channel changes and NO/prostacyclin–endothelin imbalance (Sep 2023) (johnson2023pulmonaryhypertensiona pages 1-2, johnson2023pulmonaryhypertensiona pages 2-4).
- Propagation: EndMT; PASMC and fibroblast proliferation and survival (cell-cycle activation); ECM deposition and occlusive (“plexiform”) lesions; perivascular immune infiltration fueling cytokine/growth-factor loops; metabolic reprogramming and mitochondrial dysfunction reinforce proliferation and apoptosis resistance (Sep 2023; Jun 2024) (johnson2023pulmonaryhypertensiona pages 2-4, luo2024transcriptomicprofilinghighlights pages 10-11).
- Clinical manifestation: progressive elevation of PVR and mPAP, RV hypertrophy/dysfunction and failure (Sep 2023) (johnson2023pulmonaryhypertensiona pages 1-2, johnson2023pulmonaryhypertensiona pages 2-4).

6) Phenotypic Manifestations (HP terms)
- Dyspnea on exertion (HP:0002875), fatigue (HP:0012378), syncope (HP:0001279), chest pain (HP:0100749), peripheral edema (HP:0002615), cyanosis (HP:0000979), right heart failure (HP:0001631). These phenotypes mechanistically reflect increased RV afterload from pulmonary vasculopathy and vasoconstriction (Sep 2023) (johnson2023pulmonaryhypertensiona pages 1-2, johnson2023pulmonaryhypertensiona pages 2-4).

Recent developments and latest research (2023–2024 priority) with therapeutic implications
- Activin-BMP axis and disease modification: “sotatercept is presented as a first-in-class activin signaling inhibitor that rebalances TGF-β signaling by inhibiting proproliferative activins,” and has demonstrated clinical benefit in PAH on background therapy (Sep 2023, Am J Respir Crit Care Med; DOI: https://doi.org/10.1164/rccm.202302-0327so) (johnson2023pulmonaryhypertensiona pages 1-2).
- PDGFRβ signaling and anti-proliferative strategies: PDGFRβ signaling is implicated in PASMC/pericyte proliferation and apoptosis resistance; “PDGFRβ inhibitors such as imatinib and seralutinib are noted as promising therapeutic approaches” (Sep 2023; DOI above) (johnson2023pulmonaryhypertensiona pages 1-2).
- Cell-cycle and proliferative programs in progression: longitudinal lung RNA-seq in monocrotaline rat PH shows progressive upregulation of proliferation markers (e.g., PCNA, Ccna2, Top2a) and enrichment of cell-cycle/innate immune pathways (Jun 2024; DOI: https://doi.org/10.1038/s41598-024-64251-w) (luo2024transcriptomicprofilinghighlights pages 10-11).
- Epigenetics/lncRNAs: lncRNAs are differentially expressed in PH and influence PAEC/PASMC proliferation, apoptosis, EndMT, mitochondrial function, and inflammation, supporting their roles as biomarkers and mechanistic targets (Jun 2024; Reviews in Cardiovasc Med; DOI: https://doi.org/10.31083/j.rcm2506217) (liu2024rolesoflncrnas pages 1-2).

Current applications and real-world implementations (selected examples with pathophysiology links)
- Pathway-directed therapy beyond vasodilators: clinical advances with sotatercept (activin signaling trap) reflect targeting of a core disease pathway (TGF-β superfamily imbalance) (Sep 2023) (johnson2023pulmonaryhypertensiona pages 1-2). Anti-proliferative RTK inhibition (PDGFRβ) is an active area (imatinib/seralutinib) (johnson2023pulmonaryhypertensiona pages 1-2).
- Mechanistic targets under study/preclinical support: NF-κB/NLRP3 inflammasome inhibition, PI3K/Akt/mTOR modulation, and HIF pathway interventions are recurrent strategies in preclinical/early translational literature (2025 synthesis of 20+ pathways) (aduamankwaah2025signalingpathwaysand pages 1-2, aduamankwaah2025signalingpathwaysand pages 29-30, aduamankwaah2025signalingpathwaysand pages 31-32).

Expert opinions and analysis from authoritative sources
- A 2023 state-of-the-art review (Am J Respir Crit Care Med) synthesizes PH pathogenesis across endothelial dysfunction, inflammation/immunity, metabolism/oxidant stress, hypoxia signaling, mitochondrial dysfunction, ion channels, and epigenetics/transcription, and highlights disease-modifying therapeutic concepts (e.g., sotatercept) (Sep 2023; DOI: https://doi.org/10.1164/rccm.202302-0327so) (johnson2023pulmonaryhypertensiona pages 1-2, johnson2023pulmonaryhypertensiona pages 2-4).
- A comprehensive translational pathway review (Signal Transduction and Targeted Therapy, 2025) catalogs approximately twenty signaling axes implicated in PH and aligns multiple therapeutic modalities (gene, cell, pharmacological) to these pathways (Jul 2025; DOI: https://doi.org/10.1038/s41392-025-02287-8) (aduamankwaah2025signalingpathwaysand pages 1-2, aduamankwaah2025signalingpathwaysand pages 29-30, aduamankwaah2025signalingpathwaysand pages 31-32).

Relevant statistics and data from recent studies
- Transcriptomics in experimental PH: progressive DEGs rising from 1,038 at week 1 to 3,125 at week 3 (P<0.05; |log2FC|>log2 1.5), with validation of proliferation markers (PCNA, Ccna2, Top2a) by Western blot and immunofluorescence, supporting a central role for cell proliferation in PH progression (Jun 2024; GEO GSE229361; DOI: https://doi.org/10.1038/s41598-024-64251-w) (luo2024transcriptomicprofilinghighlights pages 10-11).

Evidence items (selected with PMIDs/URLs/dates)
- Johnson et al., 2023. Pulmonary Hypertension: A Contemporary Review. Am J Respir Crit Care Med. Sep 1, 2023. DOI: https://doi.org/10.1164/rccm.202302-0327so (johnson2023pulmonaryhypertensiona pages 1-2, johnson2023pulmonaryhypertensiona pages 2-4)
  • Quote (framing): PAH involves “proliferative, fibrotic, and plexogenic remodeling of distal pulmonary arterioles,” with genetic/epigenetic drivers and dysregulated TGF-β/BMP signaling; activin inhibition (sotatercept) rebalances TGF-β signaling; PDGFRβ signaling in PASMC/pericytes is a therapeutic target (johnson2023pulmonaryhypertensiona pages 1-2, johnson2023pulmonaryhypertensiona pages 2-4).
- Luo et al., 2024. Transcriptomic profiling highlights cell proliferation in the progression of experimental pulmonary hypertension in rats. Scientific Reports. Jun 2024. DOI: https://doi.org/10.1038/s41598-024-64251-w (luo2024transcriptomicprofilinghighlights pages 10-11)
  • Data: stepwise increase in significant DEGs (1,038 → 1,244 → 3,125 over weeks 1–3), enrichment for cell-cycle/innate immune pathways; validation of PCNA, Ccna2, Top2a upregulation (luo2024transcriptomicprofilinghighlights pages 10-11).
- Liu et al., 2024. Roles of LncRNAs in the Pathogenesis of Pulmonary Hypertension. Reviews in Cardiovascular Medicine. Jun 17, 2024. DOI: https://doi.org/10.31083/j.rcm2506217 (liu2024rolesoflncrnas pages 1-2)
  • Quote (summary): lncRNAs “are differentially expressed in PH” and regulate PAEC/PASMC proliferation, apoptosis resistance, EndMT, mitochondrial function and inflammation, suggesting biomarker and therapeutic potential (liu2024rolesoflncrnas pages 1-2).
- Adu‑Amankwaah et al., 2025. Signaling pathways and targeted therapy for pulmonary hypertension. Signal Transduction and Targeted Therapy. Jul 2025. DOI: https://doi.org/10.1038/s41392-025-02287-8 (aduamankwaah2025signalingpathwaysand pages 1-2, aduamankwaah2025signalingpathwaysand pages 29-30, aduamankwaah2025signalingpathwaysand pages 31-32)
  • Quote (overview): targeting aberrant signaling hubs across HIF, NF‑κB/NLRP3, BMPR2/SMAD and others offers “great potential for mitigating PH pathology,” with qualitative reductions in mPAP/RVSP across preclinical interventions (aduamankwaah2025signalingpathwaysand pages 1-2, aduamankwaah2025signalingpathwaysand pages 31-32).

Ontology-structured annotations
- Gene/protein annotations (HGNC → process/location):
  • BMPR2 (HGNC:1071): BMP signaling; SMAD1/5/9 activation; plasma membrane→nucleus; negative regulation of PASMC proliferation (johnson2023pulmonaryhypertensiona pages 2-4)
  • SMAD9 (HGNC:6765): BMP pathway transcription factor; nucleus; regulation of transcription (johnson2023pulmonaryhypertensiona pages 2-4)
  • ACVRL1/ENG (HGNC:171/3349): endothelial TGF-β/BMP signaling; plasma membrane/caveolae; vascular development (johnson2023pulmonaryhypertensiona pages 2-4)
  • EIF2AK4 (HGNC:3255): integrated stress response kinase; PVOD/PCH genetics; cytosol (johnson2023pulmonaryhypertensiona pages 1-2)
  • KCNK3 (HGNC:11840): K+ leak channel; ion transport; membrane potential; PASMC contraction/proliferation (johnson2023pulmonaryhypertensiona pages 1-2, johnson2023pulmonaryhypertensiona pages 2-4)
  • TBX4 (HGNC:11574), SOX17 (HGNC:11191): transcriptional control of vascular development; nucleus (johnson2023pulmonaryhypertensiona pages 1-2, johnson2023pulmonaryhypertensiona pages 2-4)
  • CAV1 (HGNC:1527): caveolae scaffolding protein; endothelial signaling; caveolae (johnson2023pulmonaryhypertensiona pages 2-4)
- Cell type involvement (CL): PAECs (CL:0000115), PASMCs (CL:0000746), adventitial fibroblasts (CL:0002553), pericytes (CL:0000669), macrophages (CL:0000235) (johnson2023pulmonaryhypertensiona pages 1-2, aduamankwaah2025signalingpathwaysand pages 1-2)
- Anatomical locations (UBERON): small pulmonary artery/arteriole (UBERON:0001981), pulmonary artery (UBERON:0002114), right ventricle (UBERON:0002080) (johnson2023pulmonaryhypertensiona pages 2-4)
- Chemical entities (CHEBI) relevant to mechanisms: prostacyclin analogs, endothelin receptor antagonists, PDE5 inhibitors (standard of care; class framing) and disease-modifying examples (sotatercept; PDGFR inhibitors) (johnson2023pulmonaryhypertensiona pages 1-2)

Notes and limitations
- Where possible, we prioritized 2023–2024 primary and review sources. For pathway breadth and preclinical intervention mapping, we cited a 2025 comprehensive synthesis when 2023–2024 sources did not explicitly enumerate comparable cross-pathway tables (aduamankwaah2025signalingpathwaysand pages 1-2, aduamankwaah2025signalingpathwaysand pages 31-32). Additional quantitative clinical-trial effect sizes (e.g., for TORREY seralutinib, Phase 3 sotatercept) were not detailed here because those specific datasets were not among the retrieved texts; however, mechanistic and trial‑framing statements are supported (johnson2023pulmonaryhypertensiona pages 1-2).

References (with persistent links)
- Johnson et al., 2023. Am J Respir Crit Care Med. DOI: https://doi.org/10.1164/rccm.202302-0327so (Sep 1, 2023) (johnson2023pulmonaryhypertensiona pages 1-2, johnson2023pulmonaryhypertensiona pages 2-4)
- Luo et al., 2024. Scientific Reports. DOI: https://doi.org/10.1038/s41598-024-64251-w (Jun 2024) (luo2024transcriptomicprofilinghighlights pages 10-11)
- Liu et al., 2024. Reviews in Cardiovascular Medicine. DOI: https://doi.org/10.31083/j.rcm2506217 (Jun 17, 2024) (liu2024rolesoflncrnas pages 1-2)
- Adu‑Amankwaah et al., 2025. Signal Transduction and Targeted Therapy. DOI: https://doi.org/10.1038/s41392-025-02287-8 (Jul 2025) (aduamankwaah2025signalingpathwaysand pages 1-2, aduamankwaah2025signalingpathwaysand pages 29-30, aduamankwaah2025signalingpathwaysand pages 31-32)

References

1. (johnson2023pulmonaryhypertensiona pages 1-2): Shelsey Johnson, Natascha Sommer, Katherine Cox-Flaherty, Norbert Weissmann, Corey E. Ventetuolo, and Bradley A. Maron. Pulmonary hypertension: a contemporary review. American Journal of Respiratory and Critical Care Medicine, 208:528-548, Sep 2023. URL: https://doi.org/10.1164/rccm.202302-0327so, doi:10.1164/rccm.202302-0327so. This article has 130 citations and is from a highest quality peer-reviewed journal.

2. (johnson2023pulmonaryhypertensiona pages 2-4): Shelsey Johnson, Natascha Sommer, Katherine Cox-Flaherty, Norbert Weissmann, Corey E. Ventetuolo, and Bradley A. Maron. Pulmonary hypertension: a contemporary review. American Journal of Respiratory and Critical Care Medicine, 208:528-548, Sep 2023. URL: https://doi.org/10.1164/rccm.202302-0327so, doi:10.1164/rccm.202302-0327so. This article has 130 citations and is from a highest quality peer-reviewed journal.

3. (luo2024transcriptomicprofilinghighlights pages 10-11): Ang Luo, Rongrong Hao, Xia Zhou, Yangfan Jia, Changlei Bao, Lei Yang, Lirong Zhou, Chenxin Gu, Ankit A. Desai, Haiyang Tang, and Ai-ai Chu. Transcriptomic profiling highlights cell proliferation in the progression of experimental pulmonary hypertension in rats. Scientific Reports, Jun 2024. URL: https://doi.org/10.1038/s41598-024-64251-w, doi:10.1038/s41598-024-64251-w. This article has 5 citations and is from a peer-reviewed journal.

4. (aduamankwaah2025signalingpathwaysand pages 1-2): J. Adu-Amankwaah, Yue Shi, Hequn Song, Yixuan Ma, Jia Liu, Hao Wang, Jinxiang Yuan, Kun Sun, Qinghua Hu, and Rubin Tan. Signaling pathways and targeted therapy for pulmonary hypertension. Signal Transduction and Targeted Therapy, Jul 2025. URL: https://doi.org/10.1038/s41392-025-02287-8, doi:10.1038/s41392-025-02287-8. This article has 10 citations and is from a peer-reviewed journal.

5. (aduamankwaah2025signalingpathwaysand pages 29-30): J. Adu-Amankwaah, Yue Shi, Hequn Song, Yixuan Ma, Jia Liu, Hao Wang, Jinxiang Yuan, Kun Sun, Qinghua Hu, and Rubin Tan. Signaling pathways and targeted therapy for pulmonary hypertension. Signal Transduction and Targeted Therapy, Jul 2025. URL: https://doi.org/10.1038/s41392-025-02287-8, doi:10.1038/s41392-025-02287-8. This article has 10 citations and is from a peer-reviewed journal.

6. (aduamankwaah2025signalingpathwaysand pages 31-32): J. Adu-Amankwaah, Yue Shi, Hequn Song, Yixuan Ma, Jia Liu, Hao Wang, Jinxiang Yuan, Kun Sun, Qinghua Hu, and Rubin Tan. Signaling pathways and targeted therapy for pulmonary hypertension. Signal Transduction and Targeted Therapy, Jul 2025. URL: https://doi.org/10.1038/s41392-025-02287-8, doi:10.1038/s41392-025-02287-8. This article has 10 citations and is from a peer-reviewed journal.

7. (liu2024rolesoflncrnas pages 1-2): Ting Liu, Shuang-Lan Xu, Jiao Yang, and Xiqian Xing. Roles of lncrnas in the pathogenesis of pulmonary hypertension. Reviews in Cardiovascular Medicine, Jun 2024. URL: https://doi.org/10.31083/j.rcm2506217, doi:10.31083/j.rcm2506217. This article has 1 citations and is from a peer-reviewed journal.