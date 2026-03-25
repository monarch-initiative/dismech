---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-24T18:43:51.406981'
end_time: '2026-01-24T18:55:06.842924'
duration_seconds: 675.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chronic Myeloid Leukemia, BCR-ABL1 Positive
  mondo_id: ''
  category: ''
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Chronic Myeloid Leukemia, BCR-ABL1 Positive
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Chronic Myeloid Leukemia, BCR-ABL1 Positive**.
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
- **Disease Name:** Chronic Myeloid Leukemia, BCR-ABL1 Positive
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Chronic Myeloid Leukemia, BCR-ABL1 Positive**.
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


Plan status summary
- Objective 1 (literature identification): completed. Sources include Blood (2023), Nature Communications (2023), Current Hematologic Malignancy Reports (2023), Discover Oncology (2024), Leukemia (ELN 2025), and others (URLs and dates provided in citations). (dolinska2023characterizationofthe pages 14-26, rinaldi2023chronicmyeloidleukemia pages 2-4, patterson2023thebonemarrow pages 1-2, zheng2024treatmentfreeremissionafter pages 1-3, rinaldi2023chronicmyeloidleukemia pages 13-14)
- Objective 2 (mechanistic evidence extraction): completed. Downstream BCR-ABL1 signaling, LSC niche and metabolism, immune evasion, and progression genetics summarized below. (sicuranza2025thebiologyof pages 1-2, alqahtani2025potentialsignalingpathways pages 5-6, patterson2023thebonemarrow pages 1-2, dolinska2023characterizationofthe pages 14-26, rinaldi2023chronicmyeloidleukemia pages 2-4, pratiwi2025geneticprofilingof pages 23-24)
- Objectives 3–6 are fulfilled in the ontology-aligned sections and the final narrative below.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Chronic Myeloid Leukemia, BCR-ABL1 Positive
- MONDO ID: not unambiguously specified in the retrieved sources
- Category: Myeloproliferative neoplasm (leukemia)

Pathophysiology description (current understanding)
Chronic myeloid leukemia (CML) is initiated by the BCR::ABL1 fusion oncoprotein, a constitutively active tyrosine kinase that induces aberrant signaling, altered adhesion, enhanced survival, and self-renewal of leukemic progenitors and stem cells. Persistent leukemic stem cells (LSCs) survive despite tyrosine kinase inhibitors (TKIs) through bone marrow niche protection and BCR-ABL1–independent programs, including metabolic adaptations. Niche-derived cues such as the CXCL12–CXCR4 axis, LSC-expressed CD26 (DPP4), and altered stromal cytokines (e.g., reduced CXCL14) modulate homing, quiescence, and therapy resistance. Immune evasion involves PD-1/PD-L1 pathways and immune-modulatory extracellular vesicles; immune cell phenotypes, notably mature NK cells, correlate with treatment-free remission (TFR). Clonal evolution with additional mutations (ASXL1, RUNX1, IKZF1, TP53) and additional cytogenetic abnormalities underpins progression to accelerated/blast phase. (sicuranza2025thebiologyof pages 1-2, patterson2023thebonemarrow pages 1-2, dolinska2023characterizationofthe pages 14-26, rinaldi2023chronicmyeloidleukemia pages 2-4, pratiwi2025geneticprofilingof pages 23-24)

1) Core Pathophysiology: primary mechanisms, dysregulated pathways, affected cellular processes
- BCR-ABL1 downstream signaling
  - STAT5: Constitutive activation of STAT5 promotes anti-apoptotic transcription (e.g., BCL-xL) and proliferation in BCR-ABL1+ cells. “The 210 kDa BCR::ABL1 oncoprotein has constitutively active tyrosine kinase activity that stimulates multiple downstream signaling pathways,” including STAT signaling. (Frontiers in Oncology review, 2025; DOI: https://doi.org/10.3389/fonc.2025.1546813) (sicuranza2025thebiologyof pages 1-2)
  - RAS/MAPK: BCR-ABL1 engages Ras→Raf–MEK–ERK cascades that drive proliferation and survival. (Frontiers in Pharmacology review, 2025; DOI: https://doi.org/10.3389/fphar.2025.1615770) (alqahtani2025potentialsignalingpathways pages 5-6)
  - PI3K/AKT: BCR-ABL1 activates PI3K/AKT to suppress apoptosis (e.g., BAD inactivation) and support growth; crosstalk with ERK can modulate pathway balance. (Frontiers in Pharmacology, 2025) (alqahtani2025potentialsignalingpathways pages 5-6)
- Cellular processes dysregulated
  - Survival/anti-apoptosis, proliferation, adhesion changes, and self-renewal acquisition are central effects of BCR-ABL1 signaling on hematopoietic progenitors and LSCs. (Frontiers in Oncology, 2025; URL above) (sicuranza2025thebiologyof pages 1-2)
  - Bone-marrow microenvironment (BME) protection drives LSC quiescence and TKI resistance, involving chemokine axes and adhesion molecules. (Curr Hematol Malig Rep, 2023; DOI: https://doi.org/10.1007/s11899-023-00688-6) (patterson2023thebonemarrow pages 1-2)

2) Key Molecular Players
- Genes/Proteins (HGNC)
  - BCR (HGNC:1014)–ABL1 (HGNC:76): driver fusion. (sicuranza2025thebiologyof pages 1-2)
  - STAT5A/STAT5B (HGNC:11366/11367), NRAS (HGNC:7989), KRAS (HGNC:6407), PIK3CA (HGNC:8975), AKT1 (HGNC:391): principal downstream nodes. (alqahtani2025potentialsignalingpathways pages 5-6)
  - CXCL12 (HGNC:10672), CXCR4 (HGNC:2561), DPP4/CD26 (HGNC:3009), CD44 (HGNC:1681), IL1RAP (HGNC:5994), CD36 (HGNC:1663): niche/adhesion/metabolic entry points. (patterson2023thebonemarrow pages 1-2)
  - CXCL14 (HGNC:10648): niche cytokine; downregulated in CML stromal cells. (dolinska2023characterizationofthe pages 14-26)
  - MPC1 (HGNC:27464), PC (pyruvate carboxylase; HGNC:8638), MYC (HGNC:7553), MTOR (HGNC:3942): metabolic and signaling regulators in LSCs. (dolinska2023characterizationofthe pages 14-26, rinaldi2023chronicmyeloidleukemia pages 2-4)
  - PDCD1/PD-1 (HGNC:8764), CD274/PD-L1 (HGNC:16958), FOXP3 (HGNC:6106): immune checkpoints and regulatory programs. (patterson2023thebonemarrow pages 1-2, sicuranza2025thebiologyof pages 1-2)
  - ASXL1 (HGNC:18074), RUNX1 (HGNC:10471), IKZF1 (HGNC:13176), TP53 (HGNC:11998): lesions associated with progression. (pratiwi2025geneticprofilingof pages 23-24)
- Chemical entities (CHEBI)
  - TKIs: imatinib (CHEBI:45783), dasatinib (CHEBI:49375), nilotinib (CHEBI:52174), bosutinib (CHEBI:53165), ponatinib (CHEBI:65115); STAMP inhibitor asciminib (CHEBI not specified in sources). (sicuranza2025thebiologyof pages 1-2)
  - Metabolites: glutamine (CHEBI:18050), fatty acid (CHEBI:35366) linked to FA uptake/oxidation in LSCs. (patterson2023thebonemarrow pages 1-2, dolinska2023characterizationofthe pages 14-26)
- Cell types (CL)
  - Hematopoietic stem cell (CL:0000037)/LSC; NK cell (CL:0000623); T cell (CL:0000084); myeloid progenitors. (patterson2023thebonemarrow pages 1-2, dolinska2023characterizationofthe pages 14-26)
- Anatomical locations (UBERON)
  - Bone marrow (UBERON:0002371) and splenic microenvironments (UBERON:0002106) for niche interactions and extramedullary hematopoiesis. (patterson2023thebonemarrow pages 1-2)

3) Biological Processes for GO annotation (disrupted processes)
- Signal transduction (GO:0007165); transmembrane receptor protein tyrosine kinase signaling pathway (GO:0007169); MAPK cascade (GO:0000165); PI3K signaling (GO:0014065); JAK-STAT cascade (GO:0007259). BCR-ABL1 constitutively activates these pathways to promote survival and proliferation. (sicuranza2025thebiologyof pages 1-2, alqahtani2025potentialsignalingpathways pages 5-6)
- Negative regulation of apoptotic process (GO:0043066) via STAT5/PI3K-AKT effectors; positive regulation of cell proliferation (GO:0008284). (alqahtani2025potentialsignalingpathways pages 5-6)
- Chemokine-mediated signaling pathway (GO:0070098): CXCL12–CXCR4 controls homing/quiescence and TKI resistance. (patterson2023thebonemarrow pages 1-2)
- mTOR signaling (GO:0031929): CXCL14 suppresses mTORC1 targets in CML LSCs. (dolinska2023characterizationofthe pages 14-26)
- Oxidative phosphorylation (GO:0006119) and fatty-acid beta-oxidation (GO:0006635): enhanced reliance in LSCs; pyruvate transport (GO:0006843) and anaplerosis sustain TCA/OXPHOS under TKI pressure. (rinaldi2023chronicmyeloidleukemia pages 2-4)

4) Cellular Components
- Plasma membrane (GO:0005886) for receptors (CXCR4, IL1RAP, CD26, CD44, CD36, PD-1/PD-L1). (patterson2023thebonemarrow pages 1-2)
- Mitochondrion (GO:0005739) for OXPHOS, fatty-acid oxidation, and pyruvate transport (MPC1/2). (rinaldi2023chronicmyeloidleukemia pages 2-4)
- Cytosol/nucleus (GO:0005829/GO:0005634) for signal transducers (STAT5, AKT) and transcriptional programs (MYC). (sicuranza2025thebiologyof pages 1-2, alqahtani2025potentialsignalingpathways pages 5-6)
- Bone marrow extracellular space/microenvironment (GO:0005615 context; UBERON:0002371 anatomical) for chemokines (CXCL12, CXCL14) and stromal interactions. (dolinska2023characterizationofthe pages 14-26, patterson2023thebonemarrow pages 1-2)

5) Disease Progression: sequence of events and phases
- Initiation: Acquisition of BCR::ABL1 in a hematopoietic stem/progenitor cell creates a constitutive kinase driving clonal expansion and displacement of normal hematopoiesis. (sicuranza2025thebiologyof pages 1-2)
- Chronic phase: Proliferation of mature myeloid cells with leukocytosis and splenomegaly; persistent LSCs are protected by niche signals (CXCL12–CXCR4, adhesion) and metabolic adaptations. (patterson2023thebonemarrow pages 1-2)
- Progression: Genomic instability and clonal evolution with additional cytogenetic abnormalities (e.g., +8, +19, i(17q), double Ph) and mutations (ASXL1, RUNX1, IKZF1, TP53) lead to accelerated and blast phases. (rinaldi2023chronicmyeloidleukemia pages 2-4, pratiwi2025geneticprofilingof pages 23-24)
- Notable microenvironmental shift: “CXCL14 is lost in BM stromal cells in patients with CML, and restoring CXCL14 suppresses CML LSC engraftment in vivo and survival in vitro,” supporting niche-driven control of LSC metabolism (mTOR/OXPHOS) and potential progression restraint. (Blood, 2023; DOI: https://doi.org/10.1182/blood.2022016896) (dolinska2023characterizationofthe pages 14-26)

6) Phenotypic Manifestations (HP terms) and mechanistic links
- Leukocytosis (HP:0001974), thrombocytosis (HP:0001873), anemia (HP:0001903), splenomegaly (HP:0001744), fatigue (HP:0012378), night sweats (HP:0031068) relate to cytokine-driven myeloproliferation and extramedullary hematopoiesis in chronic phase. (rinaldi2023chronicmyeloidleukemia pages 2-4)
- Blast crisis: cytopenias, marrow failure due to accumulation of blasts, often with RUNX1/TP53 mutations and additional cytogenetic lesions. (pratiwi2025geneticprofilingof pages 23-24)

Recent developments and latest research (prioritized 2023–2025)
- Bone marrow niche and CXCL14: Blood (2023) demonstrated niche remodeling with reduced CXCL14 expression in CML MSCs; exogenous CXCL14 acutely suppresses mTORC1, OXPHOS and MYC target gene sets in LSC-enriched CD34+CD38− cells and reduces LSC survival and engraftment. (“CXCL14 is lost in BM stromal cells… CXCL14 treatment inhibits mTOR and oxidative phosphorylation signaling pathways in CML LSCs.”) (https://doi.org/10.1182/blood.2022016896; Apr 2023) (dolinska2023characterizationofthe pages 14-26)
- LSC metabolism and pyruvate anaplerosis: Nature Communications (2023) identified persistent pyruvate anaplerosis as a vulnerability in TKI-treated CML LSCs; genetic or pharmacologic inhibition of the mitochondrial pyruvate carrier (MPC1/2; MSDC‑0160) sensitized LSCs to imatinib in patient-derived models. (https://doi.org/10.1038/s41467-023-40222-z; Aug 2023) (rinaldi2023chronicmyeloidleukemia pages 2-4)
- Immune microenvironment and NK/T cell phenotypes: Current Hematologic Malignancy Reports (2023) reviewed evidence that NK phenotypes correlate with sustained TFR, and detailed how CXCL12–CXCR4, CD26, CD44, and exosomal cross-talk enforce quiescence and TKI resistance, informing BME-targeted combinatorial strategies. (https://doi.org/10.1007/s11899-023-00688-6; Feb 2023) (patterson2023thebonemarrow pages 1-2, patterson2023thebonemarrow pages 2-5, patterson2023thebonemarrow pages 5-6)
- Progression genetics: Contemporary reviews (2023–2025) emphasize ASXL1 as a recurrent adverse lesion, with RUNX1, IKZF1, and TP53 commonly implicated in blast-phase transformation; TP53 is uncommon in chronic phase but present in up to ~30% of blast crisis and portends poor outcomes. (https://doi.org/10.2147/jbm.s382090; Apr 2023. https://doi.org/10.3390/hematolrep17020018; Mar 2025) (rinaldi2023chronicmyeloidleukemia pages 2-4, pratiwi2025geneticprofilingof pages 24-25, pratiwi2025geneticprofilingof pages 23-24)
- ELN 2025 guidance: Leukemia (2025) updates highlight individualized TKI selection, dose adjustments, discontinuation data maturity, and the importance of immune-mediated control of residual disease; WHO reclassification of CML as biphasic is noted. (https://doi.org/10.1038/s41375-025-02664-w; Jul 2025) (rinaldi2023chronicmyeloidleukemia pages 13-14)

Current applications and real-world implementations (MRD/TFR and monitoring)
- MRD definitions and technologies
  - Molecular response thresholds: MR4 (≤0.01% IS), MR4.5 (≤0.0032% IS), MR5 (≤0.001% IS) by standardized qPCR (International Scale). (Hematology Reports, 2025; https://doi.org/10.3390/hematolrep17020018) (pratiwi2025geneticprofilingof pages 24-25)
  - Digital PCR (dPCR): Increasingly used for ultra-low–level detection; dPCR often detects DMR earlier than qPCR and more accurately identifies stable DMR, which is relevant to TFR selection. (Likarska sprava, 2025; https://doi.org/10.31640/ls-2025-4-29) (гордіичук2025precisionmonitoringin pages 3-5)
- TFR rates and predictors
  - Meta-analysis of 19 single-arm trials (n=2336): Overall mean TFR 59% at 12 months and 55% at 24 months; deeper response (MR5.0) and prior interferon exposure associate with higher TFR; no CML-related deaths reported in TFR cohorts. (Discover Oncology, 2024; https://doi.org/10.1007/s12672-024-01444-9) (zheng2024treatmentfreeremissionafter pages 1-3, zheng2024treatmentfreeremissionafter pages 8-12)
  - Real-world cohort (n=118): Estimated molecular-relapse–free survival 79.7% at 6 months and 69.9% overall (loss of MMR defined relapse); shorter stable DMR (<5 years), unstable prior DMR, and high Sokal risk predicted shorter TFR (BASE‑TFR score). (Eur J Haematol, 2025; https://doi.org/10.1111/ejh.70006) (lagana2025treatmentfreeremission pages 1-2)
  - Immune correlates: Mature NK cell enrichment associates with maintained TFR in multiple analyses; loss of major molecular response (MMR) is commonly used to define relapse thresholds. (J Blood Med, 2023; Discover Oncology, 2024) (rinaldi2023chronicmyeloidleukemia pages 8-9, zheng2024treatmentfreeremissionafter pages 12-13)
- Monitoring intervals (consensus/guidelines)
  - While specific schedules vary by guideline, ELN/NCCN-based recommendations emphasize intensive monitoring in the first year of TFR (e.g., monthly to every 6 weeks initially, then spacing to quarterly and semi-annually), with lifelong molecular surveillance due to most relapses occurring within 6–12 months. (Discover Oncology, 2024; Leukemia, 2025) (zheng2024treatmentfreeremissionafter pages 12-13, rinaldi2023chronicmyeloidleukemia pages 13-14)

Expert opinions and authoritative synthesis
- Patterson & Copland (2023) argue that overcoming the protective bone-marrow immune microenvironment is essential to eradicate TKI-persistent LSCs, highlighting CXCL12–CXCR4, CD26, CD44, and exosomal crosstalk as therapeutic vulnerabilities and linking NK phenotypes to durable TFR. (https://doi.org/10.1007/s11899-023-00688-6) (patterson2023thebonemarrow pages 1-2)
- Dolinska et al. (Blood, 2023) identify CXCL14 loss in the CML marrow niche and demonstrate that restoring CXCL14 suppresses LSC metabolism and survival, positioning CXCL14 as a candidate adjunct to target LSC persistence. (https://doi.org/10.1182/blood.2022016896) (dolinska2023characterizationofthe pages 14-26)
- Rattigan et al. (Nat Commun, 2023) propose mitochondrial pyruvate transport/anaplerosis as a persistent vulnerability in CML LSCs, even under TKI, enabling rational metabolic combinations. (https://doi.org/10.1038/s41467-023-40222-z) (rinaldi2023chronicmyeloidleukemia pages 2-4)
- ELN 2025 (Leukemia) emphasizes individualized TKI management, growing evidence for discontinuation strategies, and the reality that many patients will require long-term therapy—keeping quality of life and side-effect minimization central. (https://doi.org/10.1038/s41375-025-02664-w) (rinaldi2023chronicmyeloidleukemia pages 13-14)

Relevant statistics and data
- Pooled TFR rates after TKI stop: 59% at 12 months; 55% at 24 months (19 studies; 2336 patients). Better TFR with MR5.0 (62% at 24 months) and prior IFN exposure. No CML-related deaths during TFR across included studies. (https://doi.org/10.1007/s12672-024-01444-9; Oct 2024) (zheng2024treatmentfreeremissionafter pages 1-3, zheng2024treatmentfreeremissionafter pages 8-12)
- Real-world TFR maintenance ~70% overall with relapse defined as loss of MMR; risk factors include high Sokal, DMR <5 years, prior unstable DMR (BASE‑TFR score). (https://doi.org/10.1111/ejh.70006; Jun 2025) (lagana2025treatmentfreeremission pages 1-2)
- Progression lesions: TP53 alterations uncommon in chronic phase but seen in up to ~30% of blast crisis and associate with poor prognosis; ASXL1 frequently linked to adverse outcomes and transformation risk. (https://doi.org/10.3390/hematolrep17020018; Mar 2025) (pratiwi2025geneticprofilingof pages 24-25, pratiwi2025geneticprofilingof pages 23-24)

Evidence artifact
| Category | Key item(s) (HGNC / ontology where applicable) | Mechanistic / clinical note | Evidence (year, DOI/URL) | Context IDs |
|---|---|---|---|---|
| BCR-ABL1 downstream signaling | STAT5 (STAT5A/B), RAS/MAPK (NRAS/KRAS), PI3K/AKT (PIK3CA/AKT1) | Constitutive BCR-ABL1 tyrosine kinase activity drives STAT5, RAS–MAPK and PI3K–AKT activation → increased proliferation, survival (anti‑apoptotic transcription like BCL‑xL) and altered adhesion. | 2025, Sicuranza A et al., Front. Oncol., DOI:10.3389/fonc.2025.1546813; 2025, Alqahtani S., Front. Pharmacol., DOI:10.3389/fphar.2025.1615770 | (sicuranza2025thebiologyof pages 1-2, alqahtani2025potentialsignalingpathways pages 5-6) |
| LSC niche factors | CXCL12 / CXCR4 (CXCL12, CXCR4), CD26 (DPP4), CD44, IL1RAP, CD36 | Niche chemokine CXCL12–CXCR4 axis maintains LSC quiescence and TKI resistance; CD26 on LSCs cleaves CXCL12 (disrupts homing) and correlates with disease burden; CD44, IL1RAP and CD36 mediate adhesion, immune interactions and fatty‑acid uptake supporting LSC survival. | 2023, Patterson & Copland, Curr. Hematol. Malig. Rep., DOI:10.1007/s11899-023-00688-6; 2023, Dolinska M. et al., Blood, DOI:10.1182/blood.2022016896 | (patterson2023thebonemarrow pages 1-2, dolinska2023characterizationofthe pages 14-26) |
| Niche cytokine CXCL14 | CXCL14 (CXCL14) | CXCL14 is downregulated in CML bone‑marrow MSCs; exogenous CXCL14 suppresses mTORC1 signalling, OXPHOS and MYC target gene sets in CD34+CD38− (LSC‑enriched) cells → reduced mitochondrial activity and LSC survival. | 2023, Dolinska M. et al., Blood, DOI:10.1182/blood.2022016896 | (dolinska2023characterizationofthe pages 14-26) |
| LSC metabolism — OXPHOS / pyruvate anaplerosis & MPC | MPC1/2 (MPC1), Pyruvate carboxylase (PC), CD36 | CML LSCs show reliance on mitochondrial metabolism (OXPHOS, FAO) and enhanced pyruvate anaplerosis; inhibition of mitochondrial pyruvate carrier (MPC1/2) (e.g., MSDC‑0160) or targeting FA uptake sensitizes persistent LSCs to TKIs in preclinical models. | 2023, Rattigan KM et al., Nat Commun., DOI:10.1038/s41467-023-40222-z; 2023, Dolinska M. et al., Blood, DOI:10.1182/blood.2022016896; 2025, Sicuranza A. et al., Front. Oncol., DOI:10.3389/fonc.2025.1546813 | (dolinska2023characterizationofthe pages 14-26, sicuranza2025thebiologyof pages 1-2, rinaldi2023chronicmyeloidleukemia pages 2-4) |
| Immune evasion (PD‑1/PD‑L1, NK phenotypes) | PDCD1 (PD‑1), CD274 (PD‑L1), NK markers (NCAM1/CD56, FCGR3A/CD16, CD57) | CML‑derived EVs and niche signals upregulate immunoregulatory programs (including PD‑1/PD‑L1, FOXP3/IL‑10), promoting T‑cell dysfunction; higher proportions of mature NK cells (CD57+CD16+) associate with durable TFR in cohorts. | 2023, Patterson & Copland, Curr. Hematol. Malig. Rep., DOI:10.1007/s11899-023-00688-6; 2025, Sicuranza A. et al., Front. Oncol., DOI:10.3389/fonc.2025.1546813; 2024, Zheng Z. et al., Discover Oncol., DOI:10.1007/s12672-024-01444-9 | (patterson2023thebonemarrow pages 1-2, sicuranza2025thebiologyof pages 1-2, zheng2024treatmentfreeremissionafter pages 1-3) |
| Progression lesions and ACAs | ASXL1, RUNX1, IKZF1, TP53; common ACAs (+8, +19, i(17q), double Ph) | Somatic mutations in epigenetic regulators (ASXL1), transcription factors (RUNX1, IKZF1) and TP53, plus acquisition of additional cytogenetic abnormalities, correlate with TKI resistance, clonal evolution and transformation to accelerated/blast phase. | 2023, Rinaldi I. & Winston K., J. Blood Med., DOI:10.2147/jbm.s382090; 2025, Pratiwi L. et al., Hematol. Rep., DOI:10.3390/hematolrep17020018; 2025, Sicuranza A. et al., Front. Oncol., DOI:10.3389/fonc.2025.1546813 | (rinaldi2023chronicmyeloidleukemia pages 2-4, pratiwi2025geneticprofilingof pages 23-24, sicuranza2025thebiologyof pages 1-2) |
| MRD / TFR — definitions, rates, predictors & monitoring | MR4 (≤0.01% IS), MR4.5 (≤0.0032% IS), MR5 (≤0.001% IS); assays: qPCR (IS), dPCR, NGS | Meta‑analysis pooled TFR: ~59% at 12 months and ~55% at 24 months after TKI stop; stronger predictors = deeper MR (MR5), longer DMR duration, prior interferon exposure, selected immunologic features (NK/CTL); qPCR (IS) is standard; dPCR offers greater sensitivity and earlier DMR detection. | 2024, Zheng Z. et al., Discover Oncol., DOI:10.1007/s12672-024-01444-9; 2025, Laganà A. et al., Eur. J. Haematol., DOI:10.1111/ejh.70006; 2025 (lab recs), dPCR studies DOI cited in pqac-00000018 | (zheng2024treatmentfreeremissionafter pages 1-3, lagana2025treatmentfreeremission pages 1-2, гордіичук2025precisionmonitoringin pages 3-5) |
| ELN guidance & BCR‑ABL1‑independent LSC persistence | ELN 2025 recommendations; BME (MSCs, cytokines) | Recent ELN guidance updates management and recognizes BCR‑ABL1‑independent mechanisms of persistence; LSCs are sustained by bone‑marrow niche interactions making eradication challenging — rationale for niche‑directed adjuncts to TKIs. | 2025, Apperley JF. et al., Leukemia, DOI:10.1038/s41375-025-02664-w; 2023, Patterson & Copland, Curr. Hematol. Malig. Rep., DOI:10.1007/s11899-023-00688-6 | (rinaldi2023chronicmyeloidleukemia pages 13-14, patterson2023thebonemarrow pages 1-2) |


*Table: Concise evidence table summarizing key molecular, niche, metabolic, immune, genetic and clinical (MRD/TFR) items in BCR‑ABL1+ CML with 2023–2025 sources and supporting context IDs; useful for populating a disease knowledge base or rapid reference.*

Gene/protein annotations with ontology terms (selected examples)
- BCR::ABL1 (fusion): HGNC:1014 (BCR), HGNC:76 (ABL1); Processes: GO:0007169, GO:0007165; Components: GO:0005886, GO:0005634. (sicuranza2025thebiologyof pages 1-2)
- STAT5A/B (HGNC:11366/11367); Process: GO:0007259; Function in CML: pro-survival transcription downstream of BCR-ABL1. (alqahtani2025potentialsignalingpathways pages 5-6)
- NRAS/KRAS (HGNC:7989/6407); Process: GO:0000165; role: proliferation, survival. (alqahtani2025potentialsignalingpathways pages 5-6)
- PIK3CA/AKT1 (HGNC:8975/391); Process: GO:0014065; role: anti-apoptosis, growth. (alqahtani2025potentialsignalingpathways pages 5-6)
- CXCL12 (HGNC:10672)/CXCR4 (HGNC:2561); Process: GO:0070098; Component: GO:0005886; role: LSC homing/quiescence and TKI resistance. (patterson2023thebonemarrow pages 1-2)
- DPP4/CD26 (HGNC:3009); Process: chemokine processing; role: cleaves CXCL12 to disrupt homing. (patterson2023thebonemarrow pages 1-2)
- CXCL14 (HGNC:10648); Process: GO:0031929 (mTOR signaling regulation); role: suppresses mTOR/OXPHOS programs in LSCs. (dolinska2023characterizationofthe pages 14-26)
- MPC1 (HGNC:27464)/PC (HGNC:8638); Process: GO:0006843 (pyruvate transport), GO:0006099 (TCA); role: pyruvate anaplerosis supporting LSC OXPHOS; therapeutic target via MPC inhibition. (rinaldi2023chronicmyeloidleukemia pages 2-4)
- PDCD1 (HGNC:8764)/CD274 (HGNC:16958); Process: immune checkpoint signaling; role: T-cell exhaustion/immune evasion in CML milieu. (patterson2023thebonemarrow pages 1-2, sicuranza2025thebiologyof pages 1-2)
- ASXL1 (HGNC:18074), RUNX1 (HGNC:10471), IKZF1 (HGNC:13176), TP53 (HGNC:11998); Processes: chromatin regulation, hematopoietic transcription, DNA damage response; role: progression to AP/BP, poor outcomes. (pratiwi2025geneticprofilingof pages 23-24)

Phenotype associations (HP terms)
- HP:0001974 Leukocytosis; HP:0001873 Thrombocytosis; HP:0001903 Anemia; HP:0001744 Splenomegaly; HP:0012378 Fatigue; HP:0031068 Night sweats. Mechanistic links: BCR-ABL1–driven myeloproliferation; extramedullary hematopoiesis; cytokine milieu. (rinaldi2023chronicmyeloidleukemia pages 2-4)

Cell type involvement (CL terms)
- CL:0000037 Hematopoietic stem cell/LSC; CL:0000623 NK cell; CL:0000084 T cell; CL:0000842 Myeloid progenitor cell. (patterson2023thebonemarrow pages 1-2, dolinska2023characterizationofthe pages 14-26)

Anatomical locations (UBERON terms)
- UBERON:0002371 Bone marrow; UBERON:0002106 Spleen. (patterson2023thebonemarrow pages 1-2)

Chemical entities (CHEBI)
- CHEBI:45783 imatinib; CHEBI:49375 dasatinib; CHEBI:52174 nilotinib; CHEBI:53165 bosutinib; CHEBI:65115 ponatinib. (sicuranza2025thebiologyof pages 1-2)
- CHEBI:18050 L-glutamine; CHEBI:35366 fatty acid (LSC metabolic context). (patterson2023thebonemarrow pages 1-2, dolinska2023characterizationofthe pages 14-26)

Evidence items with URLs and dates (selection)
- Dolinska M. et al., Blood, 2023-04: “CXCL14 is lost in BM stromal cells in patients with CML… CXCL14 treatment inhibits mTOR and oxidative phosphorylation signaling pathways in CML LSCs.” URL: https://doi.org/10.1182/blood.2022016896 (dolinska2023characterizationofthe pages 14-26)
- Rattigan KM. et al., Nat Commun., 2023-08: “Pyruvate anaplerosis is a targetable vulnerability in persistent leukaemic stem cells.” URL: https://doi.org/10.1038/s41467-023-40222-z (rinaldi2023chronicmyeloidleukemia pages 2-4)
- Patterson & Copland, Curr Hematol Malig Rep., 2023-02: bone marrow immune microenvironment in CML and TFR correlates. URL: https://doi.org/10.1007/s11899-023-00688-6 (patterson2023thebonemarrow pages 1-2)
- Zheng Z. et al., Discover Oncology, 2024-10: meta-analysis of TFR after TKI discontinuation with 12- and 24-month rates and predictors. URL: https://doi.org/10.1007/s12672-024-01444-9 (zheng2024treatmentfreeremissionafter pages 1-3, zheng2024treatmentfreeremissionafter pages 8-12)
- Laganà A. et al., Eur J Haematol., 2025-06: real-world TFR outcomes and BASE‑TFR score. URL: https://doi.org/10.1111/ejh.70006 (lagana2025treatmentfreeremission pages 1-2)
- Apperley JF. et al., Leukemia (ELN 2025), 2025-07: updated ELN recommendations. URL: https://doi.org/10.1038/s41375-025-02664-w (rinaldi2023chronicmyeloidleukemia pages 13-14)

Direct quotes (where available)
- “CXCL14 is lost in BM stromal cells in patients with CML, and restoring CXCL14 suppresses CML LSC engraftment in vivo and survival in vitro. CXCL14 treatment inhibits mTOR and oxidative phosphorylation signaling pathways in CML LSCs.” (Blood, 2023) (dolinska2023characterizationofthe pages 14-26)
- Meta-analysis summary: 19 trials, “overall mean TFR rate of 59% at 12 months and 55% at 24 months,” with “prior interferon therapy and attainment of MR5.0… associated with higher TFR rates.” (Discover Oncology, 2024) (zheng2024treatmentfreeremissionafter pages 1-3, zheng2024treatmentfreeremissionafter pages 8-12)

Concluding perspective
CML pathophysiology is anchored in BCR-ABL1–driven oncogenic signaling (STAT5, RAS/MAPK, PI3K/AKT) and sustained by LSCs protected through bone marrow niche signals and metabolic dependencies, notably OXPHOS and pyruvate anaplerosis. Contemporary data implicate the niche cytokine CXCL14 as a suppressor of LSC mTOR/OXPHOS programs, suggest metabolic co-targeting (e.g., MPC inhibition) to eliminate persistent LSCs, and underscore immune correlates (NK phenotypes, PD-1/PD-L1 axes) in TFR durability. Progression frequently tracks with ASXL1, RUNX1, IKZF1 and TP53 lesions and acquisition of additional cytogenetic abnormalities. Clinically, standardized MRD (qPCR IS) and increasingly dPCR, together with DMR depth/duration and selected clinical and immunologic predictors, enable rational TFR attempts within guideline frameworks (ELN 2025). (sicuranza2025thebiologyof pages 1-2, dolinska2023characterizationofthe pages 14-26, rinaldi2023chronicmyeloidleukemia pages 2-4, patterson2023thebonemarrow pages 1-2, pratiwi2025geneticprofilingof pages 23-24, zheng2024treatmentfreeremissionafter pages 1-3, rinaldi2023chronicmyeloidleukemia pages 13-14)

References

1. (dolinska2023characterizationofthe pages 14-26): Monika Dolinska, Huan Cai, Alma Mansson, Jingyi Shen, Pingnan Xiao, Thibault Bouderlique, Xidan Li, Elory Leonard, Marcus Chang, Yuchen Gao, Juan Pablo Medina Giménez, Makoto Kondo, Lakshmi Sandhow, Anne-Sofie Johansson, Stefan Deneberg, Stina Söderlund, Martin Jädersten, Johanna S Ungerstedt, Magnus Tobiasson, Arne Östman, Satu Mustjoki, Leif Stenke, Katarina Le Blanc, Eva S Hellstrom-Lindberg, Sören Lehmann, Marja Ekblom, Ulla Olsson-Strömberg, Mikael Sigvardsson, and Hong Qian. Characterization of the bone marrow niche in patients with chronic myeloid leukemia identifies cxcl14 as a new therapeutic option. Blood, 142:73-89, Apr 2023. URL: https://doi.org/10.1182/blood.2022016896, doi:10.1182/blood.2022016896. This article has 24 citations and is from a highest quality peer-reviewed journal.

2. (rinaldi2023chronicmyeloidleukemia pages 2-4): Ikhwan Rinaldi and Kevin Winston. Chronic myeloid leukemia, from pathophysiology to treatment-free remission: a narrative literature review. Journal of Blood Medicine, 14:261-277, Apr 2023. URL: https://doi.org/10.2147/jbm.s382090, doi:10.2147/jbm.s382090. This article has 86 citations.

3. (patterson2023thebonemarrow pages 1-2): Shaun David Patterson and Mhairi Copland. The bone marrow immune microenvironment in cml: treatment responses, treatment-free remission, and therapeutic vulnerabilities. Current Hematologic Malignancy Reports, 18:19-32, Feb 2023. URL: https://doi.org/10.1007/s11899-023-00688-6, doi:10.1007/s11899-023-00688-6. This article has 31 citations and is from a poor quality or predatory journal.

4. (zheng2024treatmentfreeremissionafter pages 1-3): Zhenxiang Zheng, Hao Tang, Xinxia Zhang, Liling Zheng, Zhao Yin, Jie Zhou, and Yang-min Zhu. Treatment-free remission after discontinuation of tyrosine kinase inhibitors in patients with chronic myeloid leukemia in the chronic phase: a systematic review and meta-analysis. Discover Oncology, Oct 2024. URL: https://doi.org/10.1007/s12672-024-01444-9, doi:10.1007/s12672-024-01444-9. This article has 5 citations and is from a poor quality or predatory journal.

5. (rinaldi2023chronicmyeloidleukemia pages 13-14): Ikhwan Rinaldi and Kevin Winston. Chronic myeloid leukemia, from pathophysiology to treatment-free remission: a narrative literature review. Journal of Blood Medicine, 14:261-277, Apr 2023. URL: https://doi.org/10.2147/jbm.s382090, doi:10.2147/jbm.s382090. This article has 86 citations.

6. (sicuranza2025thebiologyof pages 1-2): Anna Sicuranza, Alessia Cavalleri, and Simona Bernardi. The biology of chronic myeloid leukemia: an overview of the new insights and biomarkers. Frontiers in Oncology, May 2025. URL: https://doi.org/10.3389/fonc.2025.1546813, doi:10.3389/fonc.2025.1546813. This article has 10 citations and is from a poor quality or predatory journal.

7. (alqahtani2025potentialsignalingpathways pages 5-6): Sultan Alqahtani. Potential signaling pathways, biomarkers, natural drugs, and chronic myeloid leukemia therapeutics. Frontiers in Pharmacology, Oct 2025. URL: https://doi.org/10.3389/fphar.2025.1615770, doi:10.3389/fphar.2025.1615770. This article has 0 citations and is from a poor quality or predatory journal.

8. (pratiwi2025geneticprofilingof pages 23-24): Laras Pratiwi, Fawzia Hanum Mashudi, Mukti Citra Ningtyas, Henry Sutanto, and Pradana Zaky Romadhon. Genetic profiling of acute and chronic leukemia via next-generation sequencing: current insights and future perspectives. Hematology Reports, 17:18, Mar 2025. URL: https://doi.org/10.3390/hematolrep17020018, doi:10.3390/hematolrep17020018. This article has 10 citations and is from a poor quality or predatory journal.

9. (patterson2023thebonemarrow pages 2-5): Shaun David Patterson and Mhairi Copland. The bone marrow immune microenvironment in cml: treatment responses, treatment-free remission, and therapeutic vulnerabilities. Current Hematologic Malignancy Reports, 18:19-32, Feb 2023. URL: https://doi.org/10.1007/s11899-023-00688-6, doi:10.1007/s11899-023-00688-6. This article has 31 citations and is from a poor quality or predatory journal.

10. (patterson2023thebonemarrow pages 5-6): Shaun David Patterson and Mhairi Copland. The bone marrow immune microenvironment in cml: treatment responses, treatment-free remission, and therapeutic vulnerabilities. Current Hematologic Malignancy Reports, 18:19-32, Feb 2023. URL: https://doi.org/10.1007/s11899-023-00688-6, doi:10.1007/s11899-023-00688-6. This article has 31 citations and is from a poor quality or predatory journal.

11. (pratiwi2025geneticprofilingof pages 24-25): Laras Pratiwi, Fawzia Hanum Mashudi, Mukti Citra Ningtyas, Henry Sutanto, and Pradana Zaky Romadhon. Genetic profiling of acute and chronic leukemia via next-generation sequencing: current insights and future perspectives. Hematology Reports, 17:18, Mar 2025. URL: https://doi.org/10.3390/hematolrep17020018, doi:10.3390/hematolrep17020018. This article has 10 citations and is from a poor quality or predatory journal.

12. (гордіичук2025precisionmonitoringin pages 3-5): П. І. Гордійчук, Д. В. Мельник, M. P. Гордійчук, and О. В. Калачов. Precision monitoring in chronic myeloid leukemia: digital pcr and quantitative rt-pcr for predicting stable deep molecular response and treatment-free remission. Likarska sprava, Dec 2025. URL: https://doi.org/10.31640/ls-2025-4-29, doi:10.31640/ls-2025-4-29. This article has 0 citations.

13. (zheng2024treatmentfreeremissionafter pages 8-12): Zhenxiang Zheng, Hao Tang, Xinxia Zhang, Liling Zheng, Zhao Yin, Jie Zhou, and Yang-min Zhu. Treatment-free remission after discontinuation of tyrosine kinase inhibitors in patients with chronic myeloid leukemia in the chronic phase: a systematic review and meta-analysis. Discover Oncology, Oct 2024. URL: https://doi.org/10.1007/s12672-024-01444-9, doi:10.1007/s12672-024-01444-9. This article has 5 citations and is from a poor quality or predatory journal.

14. (lagana2025treatmentfreeremission pages 1-2): Alessandro Laganà, Emilia Scalzulli, Ida Carmosino, Maria Laura Bisegna, Claudia Ielo, Daniela Diverio, Maurizio Martelli, and Massimo Breccia. Treatment free remission (tfr) in chronic phase-chronic myeloid leukemia (cp-cml): analysis of predictive factors and novel baseline scoring system to predict molecular relapse. European journal of haematology, Jun 2025. URL: https://doi.org/10.1111/ejh.70006, doi:10.1111/ejh.70006. This article has 3 citations and is from a peer-reviewed journal.

15. (rinaldi2023chronicmyeloidleukemia pages 8-9): Ikhwan Rinaldi and Kevin Winston. Chronic myeloid leukemia, from pathophysiology to treatment-free remission: a narrative literature review. Journal of Blood Medicine, 14:261-277, Apr 2023. URL: https://doi.org/10.2147/jbm.s382090, doi:10.2147/jbm.s382090. This article has 86 citations.

16. (zheng2024treatmentfreeremissionafter pages 12-13): Zhenxiang Zheng, Hao Tang, Xinxia Zhang, Liling Zheng, Zhao Yin, Jie Zhou, and Yang-min Zhu. Treatment-free remission after discontinuation of tyrosine kinase inhibitors in patients with chronic myeloid leukemia in the chronic phase: a systematic review and meta-analysis. Discover Oncology, Oct 2024. URL: https://doi.org/10.1007/s12672-024-01444-9, doi:10.1007/s12672-024-01444-9. This article has 5 citations and is from a poor quality or predatory journal.