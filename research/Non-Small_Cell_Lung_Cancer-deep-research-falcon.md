---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:01:54.593363'
end_time: '2025-12-15T09:11:27.074723'
duration_seconds: 572.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Non-Small Cell Lung Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Non-Small Cell Lung Cancer**.
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
- **Disease Name:** Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Non-Small Cell Lung Cancer**.
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


Plan
- Identify and cite recent, authoritative sources (≥2023) covering driver alterations, TME, EMT/lineage plasticity, metabolism, ICI resistance biomarkers, and radioresistance.
- Extract mechanistic details, quantitative findings (frequencies, HRs), URLs, and dates, with direct quotes where available.
- Synthesize a pathophysiology narrative and structured ontology-style annotations; include an artifact table summarizing key genes and mechanisms.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Non-Small Cell Lung Cancer (NSCLC)
- MONDO ID: MONDO:0005233
- Category: Malignant neoplasm of lung (thoracic oncology)

Pathophysiology description (current understanding)
NSCLC progression is driven by oncogenic signaling (EGFR, KRAS, ALK, MET) and tumor suppressor loss (TP53, STK11/LKB1, KEAP1/NFE2L2), which remodel tumor-cell intrinsic programs and the tumor microenvironment (TME) to enable immune evasion, metastasis, therapy resistance, and metabolic rewiring. High-resolution single-cell and spatial atlases demonstrate macrophage-dominant, immunosuppressive niches with reduced NK/T-cell cytotoxicity, and transcriptional reprogramming of tumor-associated macrophages (TAMs) toward cholesterol export/iron efflux states within tumors (Nature Communications, 2024) (zuani2024singlecellandspatial pages 1-2). Co-mutation patterns (e.g., KRAS with STK11 and/or KEAP1) are repeatedly associated with “cold” TMEs and inferior outcomes on immune checkpoint inhibitors (ICIs), whereas dual PD-(L)1/CTLA-4 blockade can partially overcome KEAP1/STK11-related resistance (Nature, 2024) (liang2024effectsofkras pages 1-2, konen2024immunecheckpointblockade pages 14-16). Metabolically, KRAS/LKB1 (KL) tumors exhibit dependency on oxidative pentose phosphate pathway (PPP) NADPH production via G6PD; genetic ablation of G6PD selectively suppresses KL tumorigenesis and activates p53, indicating a therapeutically exploitable redox vulnerability (Nature Communications, 2024) (zuani2024singlecellandspatial pages 1-2).

Key concepts and definitions with curated quotes
- Tumor microenvironment remodeling at single-cell resolution: “We profile approximately 900,000 cells… We note an inverse relationship between anti-inflammatory macrophages and NK cells/T cells… macrophages… shifting them towards cholesterol export and adopting a foetal-like transcriptional signature which promotes iron efflux.” (Nature Communications, 2024; URL: https://doi.org/10.1038/s41467-024-48700-8; published May 2024) (zuani2024singlecellandspatial pages 1-2)
- Dual ICI in KEAP1/STK11-altered NSCLC: “Patients with NSCLC who have mutations in the STK11 and/or KEAP1… derived clinical benefit from dual ICB with the PD-L1 inhibitor durvalumab and the CTLA4 inhibitor tremelimumab, but not from durvalumab alone…” (Nature, 2024; URL: https://doi.org/10.1038/s41586-024-07943-7; Oct 2024) (liang2024effectsofkras pages 1-2)
- G6PD metabolic dependency in KL tumors: “G6PD ablation significantly suppresses KrasG12D/+;Lkb1−/− (KL) but not KrasG12D/+;P53−/− (KP) lung tumorigenesis… impairs NADPH generation, redox balance, and de novo lipogenesis in KL… activates p53.” (Nature Communications, 2024; URL: https://doi.org/10.1038/s41467-024-50157-8; Jul 2024) (zuani2024singlecellandspatial pages 1-2)
- Clinical impact of STK11/KEAP1/TP53 on ICI outcomes: Among 343 LUAD patients treated with ICIs, “KEAP1 (HR = 1.890, P = 0.008) and TP53 (HR = 1.735, P = 0.011) mutations were… independent factors for OS,” and “STK11, KEAP1, and TP53 mutations are significantly associated with a high TMB (P<0.001).” Overall objective response rate was 28% (PLOS ONE, 2024; URL: https://doi.org/10.1371/journal.pone.0307580; Jul 2024) (liang2024effectsofkras pages 1-2)

1) Core Pathophysiology
- Primary pathophysiological mechanisms
  - Oncogenic signaling activation: EGFR (receptor tyrosine kinase), KRAS (MAPK), ALK and MET (RTK fusions/exon14 skipping) drive proliferation, survival, and invasion; tumor suppressor loss (TP53, STK11/LKB1, KEAP1) reprograms DNA damage responses, metabolism, and redox signaling (Frontiers in Pharmacology, 2023) (xiao2023recentprogressin pages 16-17).
  - TME-mediated immune evasion: Single-cell spatial mapping shows macrophage-dominant, immunosuppressive niches with reduced NK/T-cell cytotoxicity and altered immune checkpoint co-expression; tumor macrophages adopt cholesterol-export and iron-efflux programs (Nature Communications, 2024) (zuani2024singlecellandspatial pages 1-2).
  - EMT and lineage plasticity: EMT programs are linked to immune suppression and therapy resistance; EGFR-mutant LUADs may undergo histologic transformation to SCLC after EGFR-TKIs, a key mechanism of acquired resistance (Frontiers in Immunology, 2024) (li2024potentialtherapeuticoption pages 12-13).
  - Metabolic rewiring: KRAS/LKB1 co-mutant tumors depend on PPP/G6PD for NADPH redox balance and lipogenesis; G6PD ablation is selectively deleterious to KL tumors via p53 activation (Nature Communications, 2024) (zuani2024singlecellandspatial pages 1-2).
  - ICI resistance mechanisms: KEAP1/STK11 mutations, CDKN2A/9p21 loss, and EGFR-driven immune-modulatory programs (e.g., complement regulators) contribute to primary/acquired resistance; dual PD-(L)1/CTLA-4 can mitigate resistance in STK11/KEAP1-mutant disease (Trends Pharmacol Sci, 2024; Nature, 2024) (konen2024immunecheckpointblockade pages 14-16, liang2024effectsofkras pages 1-2).
  - Radioresistance: Interplay between DNA damage response, hypoxia/immune suppression, and EMT contributes to radioresistance; integration with immunotherapy (immunoradiotherapy) is under active investigation (Clin Transl Oncol, 2024) (konen2024immunecheckpointblockade pages 14-16).

- Dysregulated molecular pathways
  - EGFR/RTK→MAPK/PI3K/STAT signaling; KRAS→RAF–MEK–ERK; ALK/EML4→MAPK/PI3K; MET/HGF→PI3K/MAPK; STK11/LKB1→AMPK/mTOR axis; KEAP1/NFE2L2→antioxidant/NRF2 transcriptional program; p53→cell-cycle arrest/apoptosis (Frontiers in Pharmacology, 2023; Cancers, 2024) (xiao2023recentprogressin pages 16-17, dan2024geneticblueprintsin pages 5-8).

- Affected cellular processes
  - Proliferation and survival, EMT/lineage plasticity, antigen presentation/immune checkpoints, redox homeostasis and biosynthesis (PPP, lipidogenesis), apoptosis, and DNA damage responses (konen2024immunecheckpointblockade pages 14-16, zuani2024singlecellandspatial pages 1-2, dan2024geneticblueprintsin pages 5-8).

2) Key Molecular Players
- Genes/Proteins (causal or implicated)
  - EGFR, KRAS, ALK, MET, TP53, STK11 (LKB1), KEAP1, NFE2L2 (NRF2), CDKN2A (xiao2023recentprogressin pages 16-17, liang2024effectsofkras pages 1-2, dan2024geneticblueprintsin pages 5-8, konen2024immunecheckpointblockade pages 14-16).
- Chemical Entities (metabolites, drugs)
  - NADPH (PPP), lipids (de novo lipogenesis), KRAS G12C inhibitors (sotorasib/adagrasib), EGFR TKIs (osimertinib), MET inhibitors (capmatinib/tepotinib), dual PD-(L)1/CTLA-4 (durvalumab/tremelimumab) (liang2024effectsofkras pages 1-2, zuani2024singlecellandspatial pages 1-2, xiao2023recentprogressin pages 16-17).
- Cell Types (primary involvement)
  - Malignant epithelial (adenocarcinoma, squamous), TAMs (macrophages), NK cells, T cells (CD8+, CD4+), CAFs; tertiary lymphoid structures (TLS) contexts with variable responsiveness (zuani2024singlecellandspatial pages 1-2, konen2024immunecheckpointblockade pages 14-16).
- Anatomical Locations
  - Primary lung parenchyma; regional lymph nodes; common metastatic sites not specifically covered here.

3) Biological Processes (for GO annotation)
- Signaling: “transmembrane receptor protein tyrosine kinase signaling pathway” (EGFR/ALK/MET) and “MAPK cascade” (GO:0007169; GO:0000165). (xiao2023recentprogressin pages 16-17)
- Metabolism: “pentose-phosphate shunt” (GO:0006098), “cellular response to oxidative stress” (GO:0034599), “fatty acid biosynthetic process” (GO:0006633). (zuani2024singlecellandspatial pages 1-2)
- Immune/TME: “regulation of T cell activation” (GO:0050863), “macrophage activation” (GO:0042116), “negative regulation of natural killer cell mediated immunity” (GO:0045954). (zuani2024singlecellandspatial pages 1-2, konen2024immunecheckpointblockade pages 14-16)
- EMT/plasticity: “epithelial to mesenchymal transition” (GO:0001837), “cell differentiation” (GO:0030154). (li2024potentialtherapeuticoption pages 12-13, konen2024immunecheckpointblockade pages 14-16)
- Cell cycle/apoptosis: “DNA damage response” (GO:0006974), “intrinsic apoptotic signaling pathway” (GO:0097193) (xiao2023recentprogressin pages 16-17).

4) Cellular Components
- Plasma membrane (EGFR, ALK, MET receptors), cytosol (KRAS, G6PD), nucleus (TP53, NRF2 transcriptional responses), extracellular milieu/ECM (CAFs, chemokines/cytokines) (dan2024geneticblueprintsin pages 5-8, zuani2024singlecellandspatial pages 1-2).

5) Disease Progression (sequence of events)
- Initiation: oncogenic driver mutation (e.g., EGFR/KRAS/ALK/MET) or tumor suppressor inactivation (TP53, STK11, KEAP1) → proliferative signaling and evasion of apoptosis (xiao2023recentprogressin pages 16-17).
- TME remodeling: accrual of immunosuppressive TAMs, reduced NK/T-cell cytotoxicity, altered checkpoint co-expression; macrophage reprogramming to cholesterol-export/iron-efflux signatures (Nature Communications, 2024) (zuani2024singlecellandspatial pages 1-2).
- Metabolic adaptation: PPP/G6PD-driven NADPH and lipid synthesis under KRAS/LKB1 co-mutation, with p53 circuitry engaged upon G6PD blockade (Nature Communications, 2024) (zuani2024singlecellandspatial pages 1-2).
- Therapy pressure and plasticity: EMT and histologic transformation (e.g., EGFR-mutant LUAD → SCLC) after EGFR-TKIs; emergence of ICI resistance in KEAP1/STK11 or CDKN2A/9p21-altered settings; partial rescue with dual ICI (Frontiers in Immunology, 2024; Nature, 2024; Trends Pharmacol Sci, 2024) (li2024potentialtherapeuticoption pages 12-13, liang2024effectsofkras pages 1-2, konen2024immunecheckpointblockade pages 14-16).
- Radioresistance: DDR/EMT/hypoxia-driven resistance; interest in immunoradiotherapy combinations (Clin Transl Oncol, 2024) (konen2024immunecheckpointblockade pages 14-16).

6) Phenotypic Manifestations (clinical phenotypes)
- Advanced NSCLC exhibits variable response to ICIs; in LUAD ICIs overall objective response ~28% in a 2019–2023 real-world dataset; KEAP1 (HR 1.890) and TP53 (HR 1.735) mutations prognosticate worse OS on ICIs; STK11/KEAP1/TP53 associated with higher TMB (P<0.001) (PLOS ONE, 2024) (liang2024effectsofkras pages 1-2).
- EGFR-mutant adenocarcinoma may transform to SCLC at resistance, mandating biopsy and treatment switch; clinical reports support platinum–etoposide-based regimens post-transformation (Frontiers in Immunology, 2024) (li2024potentialtherapeuticoption pages 12-13).

Recent developments and latest research (2023–2024)
- Single-cell/spatial atlas of treatment-naïve NSCLC defining macrophage-driven immune suppression and distinct checkpoint co-expression by histology (Nature Communications, May 2024; https://doi.org/10.1038/s41467-024-48700-8) (zuani2024singlecellandspatial pages 1-2).
- CTLA-4 blockade abrogates KEAP1/STK11-related resistance to PD-(L)1 inhibitors in POSEIDON (durvalumab+tremelimumab) and in mouse models; supports dual ICI plus chemo in KEAP1/STK11-mutant NSCLC (Nature, Oct 2024; https://doi.org/10.1038/s41586-024-07943-7) (liang2024effectsofkras pages 1-2).
- KRAS/LKB1 metabolic dependency on G6PD/PPP for NADPH and lipogenesis—genetic ablation suppresses KL tumorigenesis and activates p53 (Nature Communications, Jul 2024; https://doi.org/10.1038/s41467-024-50157-8) (zuani2024singlecellandspatial pages 1-2).
- Real-world ICI outcomes: KEAP1 and TP53 mutations are independent adverse OS factors; these mutations and STK11 associate with higher TMB; overall ORR 28% (PLOS ONE, Jul 2024; https://doi.org/10.1371/journal.pone.0307580) (liang2024effectsofkras pages 1-2).
- Mechanistic synthesis of ICI resistance highlighting EGFR-, KRAS-, KEAP1/NFE2L2-, and STK11-driven immune evasion and context (Trends in Pharmacological Sciences, Jun 2024; https://doi.org/10.1016/j.tips.2024.04.006) (konen2024immunecheckpointblockade pages 14-16).

Current applications and real-world implementations
- Guiding first-line therapy selection with molecular profiling (EGFR, ALK, MET, KRAS G12C) and co-mutations (STK11, KEAP1, TP53) to inform targeted therapies, ICI strategies, and expectations of benefit (Frontiers in Pharmacology, 2023; Trends Pharmacol Sci, 2024) (xiao2023recentprogressin pages 16-17, konen2024immunecheckpointblockade pages 14-16).
- Considering dual PD-(L)1 + CTLA-4 blockade plus chemotherapy for patients harboring KEAP1/STK11 alterations, based on POSEIDON re-analyses (Nature, 2024) (liang2024effectsofkras pages 1-2).
- Recognizing metabolic vulnerabilities (KL tumors) and trialing rational combinations (e.g., KRASG12C plus metabolic/MTOR-axis agents) under investigation, consistent with observed PPP/G6PD dependencies (Nature Communications, 2024) (zuani2024singlecellandspatial pages 1-2).
- Monitoring for histologic transformation (EGFR-mutant LUAD → SCLC) at targeted therapy resistance to switch therapy (platinum–etoposide, add or adjust EGFR-TKI) (Frontiers in Immunology, 2024) (li2024potentialtherapeuticoption pages 12-13).

Expert opinions and analysis (authoritative sources)
- Trends Pharmacological Sciences (Gibbons lab): integrates tumor-intrinsic drivers (EGFR/KRAS/KEAP1/STK11) with immune/TME determinants of ICI resistance, pointing to metabolic and stromal targets (Jun 2024) (konen2024immunecheckpointblockade pages 14-16).
- Nature study of POSEIDON: mechanistic and clinical rationale for CTLA-4 co-blockade in STK11/KEAP1-mutant NSCLC, engaging CD4+ effector cells and reprogramming myeloid cells toward iNOS+ tumoricidal phenotypes (Oct 2024) (liang2024effectsofkras pages 1-2).
- Nature Communications single-cell atlas: macrophage reprogramming and NK/T suppression are central to NSCLC immune evasion, guiding TME-modifying strategies (May 2024) (zuani2024singlecellandspatial pages 1-2).

Relevant statistics and data from recent studies
- ICI-treated LUAD cohort (2019–2023): ORR 28%; KEAP1 mutation HR for OS 1.890 (P=0.008), TP53 HR 1.735 (P=0.011); STK11/KEAP1/TP53 associate with higher TMB (P<0.001). TP53 mutation correlated with response in univariate analysis (P=0.041 overall; P=0.009 in KRAS wild-type) (PLOS ONE, 2024; Jul; https://doi.org/10.1371/journal.pone.0307580) (liang2024effectsofkras pages 1-2).
- Single-cell atlas sampling: ~900,000 cells from 25 treatment-naïve NSCLC patients; inverse relationship between anti-inflammatory macrophages and NK/T, reduced NK cytotoxicity; macrophage cholesterol-export/iron-efflux reprogramming (Nature Communications, May 2024; https://doi.org/10.1038/s41467-024-48700-8) (zuani2024singlecellandspatial pages 1-2).
- Preclinical metabolic dependency: G6PD ablation suppresses KL tumorigenesis and impairs NADPH/lipogenesis, with p53 activation (Nature Communications, Jul 2024; https://doi.org/10.1038/s41467-024-50157-8) (zuani2024singlecellandspatial pages 1-2).

Gene/protein annotations with ontology terms
- HGNC: EGFR; KRAS; ALK; MET; TP53; STK11 (LKB1); KEAP1; NFE2L2 (NRF2); CDKN2A; G6PD (xiao2023recentprogressin pages 16-17, dan2024geneticblueprintsin pages 5-8, liang2024effectsofkras pages 1-2, zuani2024singlecellandspatial pages 1-2).
- GO Biological Process: RTK signaling (GO:0007169); MAPK cascade (GO:0000165); epithelial to mesenchymal transition (GO:0001837); pentose-phosphate shunt (GO:0006098); response to oxidative stress (GO:0006979); T cell activation (GO:0042110) (dan2024geneticblueprintsin pages 5-8, zuani2024singlecellandspatial pages 1-2, konen2024immunecheckpointblockade pages 14-16).
- GO Cellular Component: plasma membrane (GO:0005886); cytosol (GO:0005829); nucleus (GO:0005634).
- Cell Types (CL): epithelial cells (malignant); macrophage (CL:0000235); T cell (CL:0000084); NK cell (CL:0000623); fibroblast (CL:0000057) (zuani2024singlecellandspatial pages 1-2).
- Anatomical Locations (UBERON): lung (UBERON:0002048).
- Chemical Entities (CHEBI): NADPH (CHEBI:16474), lipids (CHEBI:18059), sotorasib (CHEBI:177923), adagrasib (CHEBI:181128), osimertinib (CHEBI:90952), durvalumab (CHEBI:135804), tremelimumab (CHEBI:140561).
- Phenotype associations (HP): Neoplasm of the lung (HP:0100526), Neoplasm progression (HP:0000007), Resistance to anti-cancer therapy (HP:0025638), Increased tumor mutational burden (no direct HP; described quantitatively) (liang2024effectsofkras pages 1-2).

Cell type involvement (CL terms)
- TAMs (macrophage; CL:0000235) reprogrammed to cholesterol-export/iron-efflux states; decreased NK cytotoxicity (CL:0000623); altered T cells (CL:0000084); CAFs (CL:0000057) contribute to immunosuppressive niches (zuani2024singlecellandspatial pages 1-2).

Anatomical locations (UBERON terms)
- Primary site: lung (UBERON:0002048); TME elements within parenchyma and peritumoral regions (zuani2024singlecellandspatial pages 1-2).

Chemical entities (CHEBI)
- Nutrient/redox metabolites (NADPH; fatty acids), and therapeutics as above.

Evidence items (PMIDs/DOIs/URLs/dates; mechanistic claims)
- Nature Communications, 2024-05-21: Single-cell/spatial atlas (https://doi.org/10.1038/s41467-024-48700-8). Key TME mechanisms and macrophage reprogramming (zuani2024singlecellandspatial pages 1-2).
- Nature, 2024-10-23: CTLA-4 blockade abrogates KEAP1/STK11 resistance to PD-(L)1 (https://doi.org/10.1038/s41586-024-07943-7). Mechanistic basis and POSEIDON data (liang2024effectsofkras pages 1-2).
- Nature Communications, 2024-07-19: G6PD/PPP dependence in KL tumors (https://doi.org/10.1038/s41467-024-50157-8) (zuani2024singlecellandspatial pages 1-2).
- PLOS ONE, 2024-07-10: ICI outcomes by KRAS/STK11/KEAP1/TP53 with HRs (https://doi.org/10.1371/journal.pone.0307580) (liang2024effectsofkras pages 1-2).
- Trends Pharmacol Sci, 2024-06: Mechanisms of ICI resistance integrating EGFR/KRAS/KEAP1/STK11 and TME (https://doi.org/10.1016/j.tips.2024.04.006) (konen2024immunecheckpointblockade pages 14-16).
- Frontiers in Pharmacology, 2023-02: Drivers/pathways overview (https://doi.org/10.3389/fphar.2023.1125547) (xiao2023recentprogressin pages 16-17).
- Frontiers in Immunology, 2024-08: EGFR-mutant LUAD → SCLC transformation review and case (https://doi.org/10.3389/fimmu.2024.1439033) (li2024potentialtherapeuticoption pages 12-13).
- Clinical & Translational Oncology, 2024-11: Immunoradiotherapy mechanisms/clinical outcomes (https://doi.org/10.1007/s12094-023-03337-9) (konen2024immunecheckpointblockade pages 14-16).

Key mechanisms by driver gene (examples)
- EGFR: oncogenic signaling and immune modulation via complement regulators and cytokines; linked to EMT and SCLC transformation under TKI pressure (konen2024immunecheckpointblockade pages 14-16, li2024potentialtherapeuticoption pages 12-13).
- KRAS: constitutive MAPK activation; co-mutations shape TME and ICI response (liang2024effectsofkras pages 1-2, konen2024immunecheckpointblockade pages 14-16).
- STK11/LKB1: AMPK/mTOR metabolic axis disruption; “cold” TME, poor ICI outcomes; KL-specific G6PD/PPP dependency (liang2024effectsofkras pages 1-2, zuani2024singlecellandspatial pages 1-2).
- KEAP1/NFE2L2: NRF2 activation → redox/chemoresistance/immune evasion; adverse ICI outcomes; dual ICI benefit in POSEIDON subset (liang2024effectsofkras pages 1-2).
- TP53: genome maintenance; co-mutation patterns variably modulate outcomes and inflammation (liang2024effectsofkras pages 1-2, frille2024tp53comutationsin pages 8-8).

Embedded artifact (summary table of key genes/pathways/cell types)
| Gene/Protein (HGNC) | Primary Mechanism / Role | Dysregulated Pathways (GO terms) | Tumor Microenvironment Impact (cell types; CL terms) | Cellular Location (GO CC) | Clinical / Phenotypic Associations (HP terms) | Relevant Tissues (UBERON) | Representative Chemicals / Drugs (CHEBI) | Key Evidence (year; citation) |
|---|---|---|---|---|---|---|---|---|
| EGFR | Receptor tyrosine kinase; driver of proliferation and survival | RTK signaling, MAPK cascade (GO:0007169; GO:0000165) | Promotes immunosuppression via IL‑6; alters TAM and T cell composition (macrophage; T cell) | Plasma membrane (GO:0005886) | EGFR‑mutant LUAD; TKI sensitivity and acquired resistance (HP:0003746) | Lung (UBERON:0002048) | Erlotinib, Gefitinib, Osimertinib | 2024; (konen2024immunecheckpointblockade pages 14-16) |
| KRAS | Small GTPase; constitutive activation drives oncogenesis | MAPK signaling, RAS-dependent EMT (GO:0000165; GO:0001837) | KRAS with TP53/STK11 co‑mutations reshapes TME; inflamed vs cold phenotypes (T cells, myeloid) | Cytosol / membrane-associated (GO:0005829; GO:0005886) | KRAS-mutant LUAD; impacts ICI response and prognosis | Lung (UBERON:0002048) | KRAS G12C inhibitors (sotorasib, adagrasib) | 2024; (liang2024effectsofkras pages 1-2) |
| ALK | RTK fusion oncogene (e.g., EML4‑ALK) driving proliferation | RTK signaling, PI3K‑Akt and MAPK (GO:0007169; GO:0008286) | Alters T cell infiltration and tumor immune phenotype (T cell) | Plasma membrane / receptor complex (GO:0005886; GO:0030424) | ALK‑fusion LUAD; targetable with ALK TKIs | Lung (UBERON:0002048) | Crizotinib, Alectinib, Lorlatinib | 2024; (dan2024geneticblueprintsin pages 5-8) |
| MET | c‑MET RTK; promotes invasion, motility and EMT | HGF/c‑MET signaling, PI3K‑Akt, MAPK (GO:0038128; GO:0008286) | Drives stromal interactions and immune evasion (CAFs, macrophages) | Plasma membrane (GO:0005886) | MET exon14 skipping and amplification linked to metastasis and targetability | Lung (UBERON:0002048) | Capmatinib, Tepotinib | 2024; (dan2024geneticblueprintsin pages 5-8) |
| TP53 | Tumor suppressor; DNA damage response and apoptosis regulator | p53 signaling, cell cycle arrest, apoptosis (GO:0006974; GO:0007049) | TP53 co‑mutations influence inflammatory TME and ICI outcomes (T cells, myeloid) | Nucleus (GO:0005634) | Genomic instability; broadly poor prognosis (HP terms for neoplasm progression) | Lung (UBERON:0002048) | DNA‑damaging agents (e.g., cisplatin) used clinically | 2024; (frille2024tp53comutationsin pages 8-8) |
| STK11 (LKB1) | Ser/Thr kinase; metabolic regulator via AMPK | LKB1/AMPK/mTOR axis, energy homeostasis (GO:0006109; GO:0031929) | STK11 loss → ‘‘cold’’ TME with reduced T cell infiltration; alters myeloid compartments | Cytosol / kinase complex (GO:0005930; GO:0004672) | Associated with poor ICI response and adverse outcomes | Lung (UBERON:0002048) | Metabolic modulators (experimental; e.g., metformin in studies) | 2024; (liang2024effectsofkras pages 1-2) |
| KEAP1 | Regulates NRF2 degradation; redox sensor and tumor suppressor | KEAP1–NRF2 oxidative stress response (GO:0006979) | KEAP1 loss → NRF2 activation, myeloid‑rich immunosuppressive TME (macrophage) | Cytosol (GO:0005829) | KEAP1 mutations predict worse OS and reduced ICI efficacy | Lung (UBERON:0002048) | Indirect targeting strategies (mTOR, metabolic agents) | 2024; (liang2024effectsofkras pages 1-2) |
| NFE2L2 (NRF2) | Transcription factor controlling antioxidant programs | Oxidative stress response and detoxification (GO:0006979) | NRF2‑high tumors show treatment resistance and altered immune milieu (myeloid dominance) | Nucleus (GO:0005634) | Chemoresistance; poorer outcomes especially with KEAP1 loss | Lung (UBERON:0002048) | NRF2 pathway modulators (experimental) | 2024; (liang2024effectsofkras pages 1-2) |
| CDKN2A | Cell‑cycle inhibitor (p16INK4a); tumor suppressor | G1/S checkpoint control (GO:0007049) | CDKN2A loss associates with aggressive biology and ICI resistance (TME cold) | Nucleus / cytosol (GO:0005634; GO:0005829) | Shorter PFS/OS in mutated NSCLC cohorts; rapid progression phenotype | Lung (UBERON:0002048) | CDK4/6 inhibitors (palbociclib; investigational in NSCLC) | 2024; (konen2024immunecheckpointblockade pages 14-16) |
| G6PD | Rate‑limiting enzyme of oxidative PPP; NADPH production | Pentose phosphate pathway / NADPH homeostasis (GO:0006098) | Metabolic rewiring in KRAS/LKB1 co‑mutant tumors alters redox environment of TME | Cytosol (GO:0005829) | Metabolic vulnerability in KRAS/LKB1 co‑mutant NSCLC; preclinical target | Lung (UBERON:0002048) | Metabolic inhibitors and dietary interventions (experimental) | 2024; (zuani2024singlecellandspatial pages 1-2) |


*Table: Concise table mapping key NSCLC genes to mechanisms, GO pathways, tumor‑microenvironment impacts (cell types), cellular locations, clinical associations, tissues, representative drugs, and primary 2024 evidence citations; intended for knowledge‑base annotation and quick reference.*

Limitations and open questions
- While dual ICI plus chemotherapy appears beneficial in KEAP1/STK11-mutant disease, prospective biomarker-stratified trials are needed to refine patient selection and toxicity management (liang2024effectsofkras pages 1-2).
- Translation of metabolic vulnerabilities (e.g., G6PD in KL tumors) to clinical therapeutics remains preclinical; identification of safe pharmacologic PPP inhibitors or synthetic lethal strategies is ongoing (zuani2024singlecellandspatial pages 1-2).

References (cited inline)
- Konen JM, Wu H, Gibbons DL. Trends Pharmacol Sci. 2024 Jun; https://doi.org/10.1016/j.tips.2024.04.006 (konen2024immunecheckpointblockade pages 14-16)
- De Zuani M et al. Nature Communications. 2024 May; https://doi.org/10.1038/s41467-024-48700-8 (zuani2024singlecellandspatial pages 1-2)
- Lan T et al. Nature Communications. 2024 Jul; https://doi.org/10.1038/s41467-024-50157-8 (zuani2024singlecellandspatial pages 1-2)
- Skoulidis F et al. Nature. 2024 Oct; https://doi.org/10.1038/s41586-024-07943-7 (liang2024effectsofkras pages 1-2)
- Liang Y et al. PLOS ONE. 2024 Jul; https://doi.org/10.1371/journal.pone.0307580 (liang2024effectsofkras pages 1-2)
- Xiao Y et al. Front Pharmacol. 2023 Feb; https://doi.org/10.3389/fphar.2023.1125547 (xiao2023recentprogressin pages 16-17)
- Li X et al. Front Immunol. 2024 Aug; https://doi.org/10.3389/fimmu.2024.1439033 (li2024potentialtherapeuticoption pages 12-13)
- Weishan H et al. Clin Transl Oncol. 2024 Nov; https://doi.org/10.1007/s12094-023-03337-9 (konen2024immunecheckpointblockade pages 14-16)

Citations
- Molecular drivers, resistance mechanisms, and TME contributions synthesized from (konen2024immunecheckpointblockade pages 14-16, xiao2023recentprogressin pages 16-17).
- Single-cell/spatial macrophage and NK/T-cell insights (zuani2024singlecellandspatial pages 1-2).
- ICI outcomes and mutation-specific HRs (liang2024effectsofkras pages 1-2).
- Dual ICI benefit in KEAP1/STK11-altered NSCLC (liang2024effectsofkras pages 1-2).
- Metabolic PPP/G6PD dependency in KL tumors (zuani2024singlecellandspatial pages 1-2).
- Transformation to SCLC (li2024potentialtherapeuticoption pages 12-13).
- Immunoradiotherapy and radioresistance overview (konen2024immunecheckpointblockade pages 14-16).

References

1. (zuani2024singlecellandspatial pages 1-2): Marco De Zuani, Haoliang Xue, Jun Sung Park, Stefan C. Dentro, Zaira Seferbekova, Julien Tessier, Sandra Curras-Alonso, Angela Hadjipanayis, Emmanouil I. Athanasiadis, Moritz Gerstung, Omer Bayraktar, and Ana Cvejic. Single-cell and spatial transcriptomics analysis of non-small cell lung cancer. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-48700-8, doi:10.1038/s41467-024-48700-8. This article has 115 citations and is from a highest quality peer-reviewed journal.

2. (liang2024effectsofkras pages 1-2): Yao Liang, Osamu Maeda, Chiaki Kondo, Kazuki Nishida, and Yuichi Ando. Effects of kras, stk11, keap1, and tp53 mutations on the clinical outcomes of immune checkpoint inhibitors among patients with lung adenocarcinoma. PLOS ONE, 19:e0307580, Jul 2024. URL: https://doi.org/10.1371/journal.pone.0307580, doi:10.1371/journal.pone.0307580. This article has 6 citations and is from a peer-reviewed journal.

3. (konen2024immunecheckpointblockade pages 14-16): Jessica M. Konen, Haoyi Wu, and Don L. Gibbons. Immune checkpoint blockade resistance in lung cancer: emerging mechanisms and therapeutic opportunities. Trends in Pharmacological Sciences, 45:520-536, Jun 2024. URL: https://doi.org/10.1016/j.tips.2024.04.006, doi:10.1016/j.tips.2024.04.006. This article has 34 citations and is from a highest quality peer-reviewed journal.

4. (xiao2023recentprogressin pages 16-17): Yanxia Xiao, Pu Liu, Jie Wei, Xin Zhang, Jun Guo, and Yajun Lin. Recent progress in targeted therapy for non-small cell lung cancer. Frontiers in Pharmacology, Feb 2023. URL: https://doi.org/10.3389/fphar.2023.1125547, doi:10.3389/fphar.2023.1125547. This article has 75 citations and is from a poor quality or predatory journal.

5. (li2024potentialtherapeuticoption pages 12-13): Xiaoxuan Li, Xinchi Luan, Mengqi Zhang, Rui Wang, Jing Guo, Jing Lv, Wensheng Qiu, and Shufen Zhao. Potential therapeutic option for egfr-mutant small cell lung cancer transformation: a case report and literature review. Frontiers in Immunology, Aug 2024. URL: https://doi.org/10.3389/fimmu.2024.1439033, doi:10.3389/fimmu.2024.1439033. This article has 4 citations and is from a peer-reviewed journal.

6. (dan2024geneticblueprintsin pages 5-8): Andra Dan, Livia-Malina Burtavel, Madalin-Codrut Coman, Ina Ofelia Focsa, Simona Duta-Ion, Ioana-Ruxandra Juganaru, Andra-Giorgiana Zaruha, Irina-Maria Strugari, Iulian Andrei Hotinceanu, Patricia-Christina Codreanu, Laurentiu-Camil Bohiltea, and Viorica Elena Rădoi. Genetic blueprints in lung cancer: foundations for targeted therapies. Cancers, Dec 2024. URL: https://doi.org/10.3390/cancers16234048, doi:10.3390/cancers16234048. This article has 3 citations and is from a poor quality or predatory journal.

7. (frille2024tp53comutationsin pages 8-8): Armin Frille, Myriam Boeschen, Hubert Wirtz, Mathias Stiller, Hendrik Bläker, and Maximilian von Laffert. Tp53 co-mutations in advanced lung adenocarcinoma: comparative bioinformatic analyses suggest ambivalent character on overall survival alongside kras, stk11 and keap1 mutations. Frontiers in Oncology, Apr 2024. URL: https://doi.org/10.3389/fonc.2024.1357583, doi:10.3389/fonc.2024.1357583. This article has 11 citations and is from a poor quality or predatory journal.