---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-24T18:43:50.281139'
end_time: '2026-01-24T18:50:59.429895'
duration_seconds: 429.15
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ER-Positive Breast Cancer
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
- **Disease Name:** ER-Positive Breast Cancer
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **ER-Positive Breast Cancer**.
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
- **Disease Name:** ER-Positive Breast Cancer
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **ER-Positive Breast Cancer**.
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


Plan status update: Objectives 1–2 completed (literature gathered and mechanisms synthesized). Artifacts prepared. Proceeding to compile the research report with citations.

# Disease Pathophysiology Research Template

## Target Disease
- Disease Name: ER-Positive Breast Cancer
- MONDO ID: 0007254 (Mondo:0007254; “estrogen-receptor positive breast carcinoma”)
- Category: Malignant neoplasm; breast luminal (HR+) subtype

## Research Objectives
A comprehensive, well-cited synthesis of ER-positive (ER+) breast cancer pathophysiology focused on molecular/cellular mechanisms, recent advances (2023–2024 prioritized), applications, expert perspectives, and pertinent statistics.

## Pathophysiology description (narrative)
ER+ breast cancer is driven by estrogen receptor alpha (ERα; ESR1)–dependent transcriptional programs primed by pioneer factors (FOXA1, GATA3) and modulated by oncogenic crosstalk (PI3K/AKT/mTOR, RTKs such as FGFR/HER2) and the tumor microenvironment. Under selective pressure from aromatase inhibitors (AIs) and other endocrine therapies, tumors frequently acquire ESR1 ligand-binding domain (LBD) mutations or rearrangements that sustain ligand-independent ER signaling and promote endocrine resistance; combination strategies targeting PI3K/AKT/mTOR and cell cycle (CDK4/6) have become foundational, with biomarker-guided escalation to oral SERDs (e.g., elacestrant) and AKT inhibition (capivasertib) in defined molecular subsets (ESR1-mutated; PIK3CA/AKT1/PTEN-altered). High-level summaries of these mechanisms and therapeutic linkages are consolidated in the embedded table artifact. (ferro2024noveltreatmentstrategies pages 23-24, santangelo2025secondlinestrategiesto pages 7-7, ferrari2025molecularmechanismsand pages 1-2)

| Mechanism | Key genes/proteins (HGNC) | Pathway / GO terms (suggested) | Therapeutic classes (CHEBI / example drugs) | Evidence (citation IDs) |
|---|---|---|---|---|
| ER / ESR1 signaling & activating LBD mutations | ESR1 (ESR1) | Steroid hormone receptor signaling (GO:0030520); transcriptional activation (GO:0006351) | SERMs / SERDs (tamoxifen, fulvestrant, elacestrant) | (ferro2024noveltreatmentstrategies pages 23-24, santangelo2025secondlinestrategiesto pages 7-7, ferrari2025molecularmechanismsand pages 1-2) |
| ESR1 gene fusions (ligand‑binding loss) | ESR1 fusions (e.g., ESR1::CCDC170) | Fusion-driven constitutive transcription (GO:0006351) | Indirect targeting: downstream kinase inhibitors / pathway-directed therapies | (santangelo2025secondlinestrategiesto pages 7-7, ramezani2025mechanismsofendocrine pages 13-15, ferro2024noveltreatmentstrategies pages 26-27) |
| Pioneer transcription factors (chromatin priming) | FOXA1, GATA3 (FOXA1, GATA3) | Chromatin binding / pioneer factor activity (GO:0000978; GO:0030901) | Epigenetic modulators; ER-directed agents (to disrupt reprogrammed ER cistrome) | (ramezani2025mechanismsofendocrine pages 13-15, ferrari2025molecularmechanismsand pages 1-2, ferro2024noveltreatmentstrategies pages 26-27) |
| PI3K / AKT / mTOR signaling axis | PIK3CA, AKT1, PTEN, MTOR | PI3K/AKT signaling (GO:0014065); mTOR signaling (GO:0031929) | PI3K inhibitors (alpelisib), AKT inhibitors (capivasertib), mTOR inhibitors (everolimus) | (ferro2024noveltreatmentstrategies pages 23-24, santangelo2025secondlinestrategiesto pages 7-7, ferrari2025molecularmechanismsand pages 1-2) |
| CDK4/6-driven cell-cycle control | CDK4, CDK6, CCND1, RB1 | G1/S cell-cycle transition (GO:0044843) | CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) ± ET | (ferro2024noveltreatmentstrategies pages 23-24, ferrari2025molecularmechanismsand pages 1-2, ferro2024noveltreatmentstrategies pages 26-27) |
| RTK crosstalk: FGFR / HER family | FGFR1–4, ERBB2 (HER2), FGF ligands | Receptor tyrosine kinase signaling (GO:0007169); MAPK/PI3K pathway cross-talk | FGFR inhibitors (tasurgratinib, others); HER2 ADCs (trastuzumab deruxtecan) | (ramezani2025mechanismsofendocrine pages 13-15, ferrari2025molecularmechanismsand pages 1-2, ferro2024noveltreatmentstrategies pages 26-27) |
| Epigenetic & chromatin remodeling | ARID1A, KMT2C, EZH2, SWI/SNF components | Chromatin remodeling (GO:0006338); histone modification (GO:0016570) | Epigenetic drugs (HDACi, DNMTi) and combination approaches (preclinical/clinical) | (ramezani2025mechanismsofendocrine pages 11-13, ramezani2025mechanismsofendocrine pages 13-15, ferrari2025molecularmechanismsand pages 1-2) |
| Tumor microenvironment & immune features | CD274 (PD-L1), TIL markers, CAF markers (FAP), cytokines (CCL2, IL6) | Immune response (GO:0006955); cell–cell signaling (GO:0007267) | Immune checkpoint inhibitors (selected settings), ADCs, stroma-targeting strategies | (ramezani2025mechanismsofendocrine pages 13-15, ferrari2025molecularmechanismsand pages 1-2, ferro2024noveltreatmentstrategies pages 26-27) |
| Imaging biomarker: 18F‑FES PET (ER functional imaging) | ER / ESR1 (imaged ligand binding) | Diagnostic molecular imaging; ER ligand binding assessment | 18F‑FES PET to guide endocrine therapy selection / assess ER heterogeneity | (santangelo2025secondlinestrategiesto pages 7-7, santangelo2025secondlinestrategiesto pages 1-3) |
| Clinical biomarkers & testing (therapy selection) | ESR1, PIK3CA, AKT1, PTEN (HGNC: ESR1, PIK3CA, AKT1, PTEN) | Clinical molecular diagnostics; actionable mutation annotation | Biomarker-driven drugs: elacestrant (ESR1-mut), alpelisib (PIK3CA), capivasertib (AKT), PARPi for BRCA | (santangelo2025secondlinestrategiesto pages 7-7, ferro2024noveltreatmentstrategies pages 23-24, ferrari2025molecularmechanismsand pages 1-2) |


*Table: Table summarizing core ER-positive breast cancer mechanisms, key genes/proteins with suggested GO pathway terms, linked therapeutic classes (examples), and supporting evidence from recent reviews and studies (2023–2025 reviews cited). This consolidates mechanistic-to-clinical links useful for knowledge-base annotation and therapeutic decision contexts.*

## Required Information

### 1. Core Pathophysiology
- Primary mechanisms
  - ER/ESR1 signaling is central; endocrine pressure selects ESR1 LBD mutations (e.g., Y537S, D538G) that stabilize agonist conformations and drive AI resistance, often retaining susceptibility to SERDs though polyclonality can limit response. Quote: “Mutations in ESR1 contribute to ET resistance by mediating ligand-independent ER signaling… ESR1-mutant cancers are often AI-resistant but remain susceptible to SERDs.” (Journal of Clinical Medicine 2024; review of EMERALD and targeted strategies). URL: https://doi.org/10.3390/jcm13123611 (June 2024) (ferro2024noveltreatmentstrategies pages 23-24)
  - PI3K/AKT/mTOR activation (PIK3CA mutation, PTEN loss, AKT1 activation) promotes survival and endocrine resistance; clinical actionability is established for alpelisib (PIK3CA-mutant) and capivasertib (PIK3CA/AKT1/PTEN-altered) in combination with fulvestrant (CAPItello‑291). (santangelo2025secondlinestrategiesto pages 7-7, ferro2024noveltreatmentstrategies pages 23-24)
  - CDK4/6 pathway cooperates with ER to drive G1/S; CDK4/6 inhibitors with ET are standard, yet resistance emerges via RB1 loss, cyclin E/CDK2 upshift, PI3K/FGFR signaling, and microenvironmental adaptation. (ferro2024noveltreatmentstrategies pages 23-24)
  - Growth factor crosstalk: FGFR1 amplification/overexpression and HER2 pathway activity can reprogram ER signaling and mediate resistance, supporting rationale for FGFR/HER2-directed approaches in select contexts. (ramezani2025mechanismsofendocrine pages 13-15, ferrari2025molecularmechanismsand pages 1-2)
  - Epigenetic/chromatin remodeling remodels the ER cistrome (e.g., chromatin modifiers, pioneer factor dynamics), contributing to endocrine resistance and CDK4/6 resistance; integrative reviews highlight chromatin/epigenetic lesions as recurrent features. (ramezani2025mechanismsofendocrine pages 11-13, ramezani2025mechanismsofendocrine pages 13-15)
  - Tumor microenvironment (TME) and immune contexture (CAF-derived cytokines, immune suppression) influence ER expression/function and resistance trajectories; biomarker use remains limited beyond PIK3CA and ESR1 but microenvironment signatures are emerging. (ramezani2025mechanismsofendocrine pages 13-15, ferrari2025molecularmechanismsand pages 1-2)
- Dysregulated pathways
  - Steroid hormone receptor transcription (ESR1); PI3K/AKT/mTOR; RTK signaling (FGFR/HER2); cell cycle/CDKs; NF-κB/chemokine axes; epigenetic remodeling. (ramezani2025mechanismsofendocrine pages 13-15)
- Cellular processes affected
  - Proliferation (G1/S transition), survival signaling, chromatin accessibility and enhancer usage, metabolic rewiring, immune evasion via stromal/immune reprogramming. (ramezani2025mechanismsofendocrine pages 13-15)

### 2. Key Molecular Players
- Genes/Proteins (HGNC)
  - ESR1 (ERα); FOXA1; GATA3; PIK3CA; AKT1; PTEN; MTOR; CCND1/CDK4/CDK6; RB1; FGFR1–4; ERBB2 (HER2); chromatin modifiers (e.g., ARID1A, KMT2C). (ferro2024noveltreatmentstrategies pages 23-24, ramezani2025mechanismsofendocrine pages 13-15, ferrari2025molecularmechanismsand pages 1-2)
- Chemical Entities (CHEBI; drugs)
  - SERMs (tamoxifen), SERDs (fulvestrant; oral SERD elacestrant), CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib), PI3K inhibitor alpelisib, AKT inhibitor capivasertib, mTOR inhibitor everolimus; HER2‑targeted ADCs in HER2‑low contexts (trastuzumab deruxtecan). (ferro2024noveltreatmentstrategies pages 23-24, santangelo2025secondlinestrategiesto pages 7-7)
- Cell Types (CL)
  - Luminal epithelial tumor cells; cancer-associated fibroblasts (CAFs); tumor-infiltrating lymphocytes (TILs) including CD8+ T cells; macrophages; endothelial cells. (ramezani2025mechanismsofendocrine pages 13-15, ferrari2025molecularmechanismsand pages 1-2)
- Anatomical Locations (UBERON)
  - Mammary gland (UBERON:0001911); common metastatic sites—bone (UBERON:0002481), liver (UBERON:0002107), lung (UBERON:0002048). (ferro2024noveltreatmentstrategies pages 23-24)

### 3. Biological Processes (GO annotation)
- Steroid hormone receptor signaling (GO:0030520); transcription by RNA polymerase II (GO:0006351); chromatin remodeling (GO:0006338); PI3K/AKT signaling (GO:0014065); mTOR signaling (GO:0031929); G1/S transition (GO:0044843); receptor tyrosine kinase signaling (GO:0007169); immune response (GO:0006955); cell–cell signaling (GO:0007267). (ramezani2025mechanismsofendocrine pages 13-15, ferrari2025molecularmechanismsand pages 1-2)

### 4. Cellular Components
- Nuclear chromatin (GO:0000790); ER transcriptional complexes at enhancers; plasma membrane (RTKs); cytosol (PI3K/AKT/mTOR); extracellular space (cytokines, growth factors). (ramezani2025mechanismsofendocrine pages 13-15)

### 5. Disease Progression
- Sequence of events
  - Initiation and growth via ER-dependent luminal programs; endocrine therapy imposes selective pressure; acquisition of ESR1 mutations/fusions and activation of compensatory PI3K/AKT/mTOR and RTKs foster acquired resistance; additional cell-cycle and epigenetic reprogramming consolidate progression; metastatic colonization shaped by microenvironmental niches (e.g., bone). (ferro2024noveltreatmentstrategies pages 23-24, ramezani2025mechanismsofendocrine pages 13-15)
- Stages/phases
  - Endocrine-sensitive phase (robust CDK4/6+ET benefit), emerging resistance (ctDNA-detectable ESR1 mutations), clinically resistant phase with actionable pathway alterations guiding SERD or AKT/PI3K/mTOR targeting. (santangelo2025secondlinestrategiesto pages 7-7, ferro2024noveltreatmentstrategies pages 23-24)

### 6. Phenotypic Manifestations
- Clinical phenotypes
  - Recurrence after adjuvant ET; metastatic progression (bone-predominant pattern common in ER+ disease); endocrine-refractory disease with reduced ET response durations. (ferro2024noveltreatmentstrategies pages 23-24)
- Relation to mechanisms
  - ESR1-mutant tumors are AI-resistant but may benefit from SERDs; PIK3CA/AKT1/PTEN-altered tumors benefit from AKT inhibition (capivasertib) with fulvestrant; PI3Kα-mutant tumors benefit from alpelisib+fulvestrant; RTK/FGFR-driven reprogramming aligns with endocrine resistance. (santangelo2025secondlinestrategiesto pages 7-7, ferro2024noveltreatmentstrategies pages 23-24)

## Current applications and real-world implementations
- Biomarker testing and therapy selection
  - Routine testing in advanced HR+/HER2− disease increasingly includes ESR1 (ctDNA or tissue) and PIK3CA/AKT1/PTEN. Expert summary: “few biomarkers are currently used in routine clinical practice beyond PIK3CA mutation and, increasingly, ESR1 mutation in the metastatic setting.” (Nov 2025; URL: https://doi.org/10.61882/tcr.202501.01.05) (ramezani2025mechanismsofendocrine pages 13-15)
- Trials and approvals
  - EMERALD: oral SERD elacestrant improved PFS vs standard ET in ESR1-mutated ER+/HER2− MBC, with larger benefit after ≥12 months of prior ET+CDK4/6i exposure; real-world PFS ~8–9 months, ~5.2 months with coexistent PIK3CA mutations. (EMJ Oncology 2025 review; summarizes 2024 data). URL: https://doi.org/10.33590/emjoncol/NJQZ9723 (May 2025) (santangelo2025secondlinestrategiesto pages 1-3)
  - CAPItello‑291: capivasertib+fulvestrant improved PFS in PIK3CA/AKT1/PTEN‑altered tumors after AI±CDK4/6i; incorporated into approvals (2023–2024). (EMJ Oncology 2025 review). URL: https://doi.org/10.33590/emjoncol/NJQZ9723 (May 2025) (santangelo2025secondlinestrategiesto pages 7-7)
- Imaging
  - 18F‑FES PET can assess ER expression heterogeneity and predict ET responsiveness; used for staging/recurrence assessment and therapy selection in ER+ breast cancer. (summarized in 2024–2025 sources). (santangelo2025secondlinestrategiesto pages 1-3)

## Expert opinions and analysis (authoritative sources; quotes)
- On ESR1 mutations and SERDs: “Mutations in ESR1 contribute to ET resistance by mediating ligand-independent ER signaling… [they] are often AI-resistant but remain susceptible to SERDs.” (Journal of Clinical Medicine review, June 2024). URL: https://doi.org/10.3390/jcm13123611 (ferro2024noveltreatmentstrategies pages 23-24)
- On breadth of mechanisms and need for composite biomarkers: “endocrine resistance is multifactorial and dynamic… few biomarkers are currently used in routine clinical practice beyond PIK3CA mutation and, increasingly, ESR1 mutation in the metastatic setting.” (The Cancer Review, Nov 2025). URL: https://doi.org/10.61882/tcr.202501.01.05 (ramezani2025mechanismsofendocrine pages 13-15)

## Relevant statistics and data
- Prevalence/actionability
  - ESR1 mutations arise commonly at progression in metastatic settings under AI pressure; biomarker-guided oral SERD therapy (elacestrant) shows PFS benefit in ESR1-mutated tumors in EMERALD; capivasertib+fulvestrant shows PFS benefit in PIK3CA/AKT1/PTEN-altered disease (CAPItello‑291; 2023–2024 practice updates). (santangelo2025secondlinestrategiesto pages 7-7, santangelo2025secondlinestrategiesto pages 1-3)

## Structured ontology annotations
- Gene/protein annotations (HGNC): ESR1; FOXA1; GATA3; PIK3CA; AKT1; PTEN; MTOR; CCND1; CDK4; CDK6; RB1; FGFR1; ERBB2; ARID1A; KMT2C. (ramezani2025mechanismsofendocrine pages 13-15)
- GO biological processes: GO:0030520; GO:0006351; GO:0006338; GO:0014065; GO:0031929; GO:0044843; GO:0007169; GO:0006955; GO:0007267. (ramezani2025mechanismsofendocrine pages 13-15)
- Cell types (CL): luminal epithelial cells; CAFs; CD8+ T cells; macrophages. (ramezani2025mechanismsofendocrine pages 13-15)
- Anatomical (UBERON): breast, bone, liver, lung. (ferro2024noveltreatmentstrategies pages 23-24)
- Chemical entities (CHEBI): elacestrant; fulvestrant; tamoxifen; alpelisib; capivasertib; everolimus; CDK4/6 inhibitors. (santangelo2025secondlinestrategiesto pages 7-7, ferro2024noveltreatmentstrategies pages 23-24)

## Evidence items with PMIDs/DOIs/URLs and dates
- Ferro et al., Novel treatment strategies for HR+ HER2− MBC. Journal of Clinical Medicine, June 2024. DOI: 10.3390/jcm13123611. URL: https://doi.org/10.3390/jcm13123611 (mechanisms, SERDs, CDK4/6, PI3K/AKT/mTOR; includes EMERALD context). (ferro2024noveltreatmentstrategies pages 23-24)
- Santangelo, Second-line strategies… EMJ Oncology, May 2025; synthesizes 2024 data for elacestrant (EMERALD) and capivasertib (CAPItello‑291). DOI: 10.33590/emjoncol/njqz9723. URL: https://doi.org/10.33590/emjoncol/njqz9723 (santangelo2025secondlinestrategiesto pages 7-7, santangelo2025secondlinestrategiesto pages 1-3)
- Ramezani & Soheili Azad, Mechanisms of endocrine resistance… The Cancer Review, Nov 2025 (integrated genomic/translational review—epigenetics, microenvironment, biomarkers). DOI: 10.61882/tcr.202501.01.05. URL: https://doi.org/10.61882/tcr.202501.01.05 (ramezani2025mechanismsofendocrine pages 13-15, ramezani2025mechanismsofendocrine pages 17-18)
- Ferrari et al., Molecular mechanisms and strategies… IJMS, Apr 2025 (overview of ESR1 genetics, microenvironment, combinations). DOI: 10.3390/ijms26073438. URL: https://doi.org/10.3390/ijms26073438 (ferrari2025molecularmechanismsand pages 1-2)

Limitations and scope note: While the narrative prioritizes 2023–2024 topics and clinical practices (SERDs, CDK4/6, PI3K/AKT/mTOR, imaging), several integrative reviews summarizing 2024 data were published in early 2025; these were included when they synthesized 2023–2024 primary evidence. Citations track to available context IDs above.


References

1. (ferro2024noveltreatmentstrategies pages 23-24): Antonella Ferro, Michela Campora, Alessia Caldara, Delia De Lisi, Martina Lorenzi, Sara Monteverdi, Raluca Mihai, Alessandra Bisio, Mariachiara Dipasquale, Orazio Caffo, and Yari Ciribilli. Novel treatment strategies for hormone receptor (hr)-positive, her2-negative metastatic breast cancer. Journal of Clinical Medicine, 13:3611, Jun 2024. URL: https://doi.org/10.3390/jcm13123611, doi:10.3390/jcm13123611. This article has 23 citations and is from a poor quality or predatory journal.

2. (santangelo2025secondlinestrategiesto pages 7-7): Samantha Santangelo. Second-line strategies to overcome resistance to oestrogen therapy in patients with er+/her2- metastatic breast cancer: a year in review. EMJ Oncology, pages 2-9, May 2025. URL: https://doi.org/10.33590/emjoncol/njqz9723, doi:10.33590/emjoncol/njqz9723. This article has 0 citations.

3. (ferrari2025molecularmechanismsand pages 1-2): Paola Ferrari, Maria Luisa Schiavone, Cristian Scatena, and Andrea Nicolini. Molecular mechanisms and therapeutic strategies to overcome resistance to endocrine therapy and cdk4/6 inhibitors in advanced er+/her2− breast cancer. International Journal of Molecular Sciences, Apr 2025. URL: https://doi.org/10.3390/ijms26073438, doi:10.3390/ijms26073438. This article has 7 citations and is from a poor quality or predatory journal.

4. (ramezani2025mechanismsofendocrine pages 13-15): Sepehr Ramezani and Faezeh soheili azad. Mechanisms of endocrine resistance in hormone receptor–positive breast cancer: an integrated genomic and translational review. The Cancer Review, 1:56-73, Nov 2025. URL: https://doi.org/10.61882/tcr.202501.01.05, doi:10.61882/tcr.202501.01.05. This article has 0 citations.

5. (ferro2024noveltreatmentstrategies pages 26-27): Antonella Ferro, Michela Campora, Alessia Caldara, Delia De Lisi, Martina Lorenzi, Sara Monteverdi, Raluca Mihai, Alessandra Bisio, Mariachiara Dipasquale, Orazio Caffo, and Yari Ciribilli. Novel treatment strategies for hormone receptor (hr)-positive, her2-negative metastatic breast cancer. Journal of Clinical Medicine, 13:3611, Jun 2024. URL: https://doi.org/10.3390/jcm13123611, doi:10.3390/jcm13123611. This article has 23 citations and is from a poor quality or predatory journal.

6. (ramezani2025mechanismsofendocrine pages 11-13): Sepehr Ramezani and Faezeh soheili azad. Mechanisms of endocrine resistance in hormone receptor–positive breast cancer: an integrated genomic and translational review. The Cancer Review, 1:56-73, Nov 2025. URL: https://doi.org/10.61882/tcr.202501.01.05, doi:10.61882/tcr.202501.01.05. This article has 0 citations.

7. (santangelo2025secondlinestrategiesto pages 1-3): Samantha Santangelo. Second-line strategies to overcome resistance to oestrogen therapy in patients with er+/her2- metastatic breast cancer: a year in review. EMJ Oncology, pages 2-9, May 2025. URL: https://doi.org/10.33590/emjoncol/njqz9723, doi:10.33590/emjoncol/njqz9723. This article has 0 citations.

8. (ramezani2025mechanismsofendocrine pages 17-18): Sepehr Ramezani and Faezeh soheili azad. Mechanisms of endocrine resistance in hormone receptor–positive breast cancer: an integrated genomic and translational review. The Cancer Review, 1:56-73, Nov 2025. URL: https://doi.org/10.61882/tcr.202501.01.05, doi:10.61882/tcr.202501.01.05. This article has 0 citations.