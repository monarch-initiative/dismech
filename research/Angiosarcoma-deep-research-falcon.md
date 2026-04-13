---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-04-11T22:13:01.348469'
end_time: '2026-04-11T22:13:01.356523'
duration_seconds: 0.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Angiosarcoma
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Angiosarcoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Angiosarcoma**.
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
- **Disease Name:** Angiosarcoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Angiosarcoma**.
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


# Angiosarcoma Pathophysiology Research Report (Cancer)

## Disease identifiers
- **Disease name:** Angiosarcoma
- **MONDO ID:** Not confirmed from the retrieved sources in this run (not reported in the cited texts).

## 1) Key concepts and definitions (current understanding)

Angiosarcoma is a rare, aggressive malignant neoplasm of **endothelial lineage** (blood and/or lymphatic endothelium) characterized by highly infiltrative growth, early hematogenous spread, and marked biologic heterogeneity across anatomic sites and etiologies (sporadic/primary vs secondary after radiation or chronic lymphedema). Molecularly, angiosarcoma is best conceptualized as a disease of **dysregulated angiogenesis and endothelial signaling**, with frequent activation of **VEGF/VEGFR**, **Angiopoietin–Tie**, and downstream **MAPK** and **PI3K/AKT/mTOR** axes, coupled to subtype-enriched oncogenic drivers (e.g., **MYC** amplification in secondary radiation/lymphedema-associated tumors; **KDR** and **PIK3CA** alterations in primary breast angiosarcoma; and **UV-driven hypermutation** in scalp/face cutaneous disease). (chen2020optimalclinicalmanagement pages 11-12, chen2020optimalclinicalmanagement pages 9-11, painter2020theangiosarcomaproject pages 4-7)

A concise mechanistic framing from a comprehensive molecular review is that angiosarcomas “often manifest through genetic mutations (KDR(VEGFR-2), PLCG1, PTPRB) … or amplification (FLT4(VEGFR-3))”, highlighting recurrent perturbations of endothelial receptor tyrosine kinase signaling and its proximal effectors. (chen2020optimalclinicalmanagement pages 5-7)

## 2) Core pathophysiology

### 2.1 Primary pathophysiological mechanisms

**(A) Pathologic angiogenesis/lymphangiogenesis as a central program**
- VEGF signaling is prominent in angiosarcoma biology. Immunohistochemistry data compiled in the molecular review show high expression of VEGF pathway components (e.g., VEGF-A/VEGFRs) across cases, consistent with a phenotype dependent on endothelial growth factor signaling. (chen2020optimalclinicalmanagement pages 9-11)
- The **Angiopoietin–Tie** axis contributes to vascular maturation/maintenance and appears biologically relevant in angiosarcoma; Tie/Ang proteins were detected in substantial fractions of cases by immunohistochemistry (e.g., Tie-2, Ang-1/2), and expression levels correlated with survival in at least one cohort. (chen2020optimalclinicalmanagement pages 11-12)

**(B) Oncogenic rewiring downstream of endothelial receptors**
- Downstream signaling nodes repeatedly implicated include **FAK**, **MAPK**, and **PI3K/AKT/mTOR**, which couple extracellular pro-angiogenic signals to proliferation, survival, migration, and invasion. (chen2020optimalclinicalmanagement pages 11-12, kumari2023primarycardiacangiosarcoma pages 3-4)

**(C) DNA damage/etiology-specific mutagenesis shapes subtype biology**
- **Radiation-associated angiosarcoma (RT-AS)** exhibits features of ionizing radiation damage and distinct genomic landscapes compared with sporadic angiosarcoma, with mutational patterns consistent with error-prone repair of DNA double-strand breaks (microhomology-mediated mechanisms and/or non-homologous end joining). (dermawan2023distinctgenomiclandscapes pages 8-10, dermawan2023distinctgenomiclandscapes pages 1-3)
- **UV-associated cutaneous angiosarcoma (scalp/face)** displays a UV mutational signature and high tumor mutational burden (TMB), supporting a causative role for UV damage in a clinically important subset. (painter2020theangiosarcomaproject pages 4-7, painter2020theangiosarcomaproject pages 7-11)

### 2.2 Dysregulated molecular pathways

**VEGF/VEGFR signaling (KDR/FLT4 and effectors)**
- Activating or recurrent alterations affecting VEGFR signaling include **KDR (VEGFR2)** mutations and **FLT4 (VEGFR3)** amplifications, with subtype-specific enrichment (e.g., KDR in primary breast; FLT4 often co-amplified with MYC in radiation-associated breast angiosarcoma). (chen2020optimalclinicalmanagement pages 9-11, chang2024clinicopathologicandmolecular pages 10-11)

**Angiopoietin–Tie / vascular stability signaling (TIE2 pathway)**
- Loss-of-function **PTPRB** mutations are proposed to deregulate Tie-2 and VEGFR2 signaling (removing phosphatase “braking” on endothelial receptor pathways). (chen2020optimalclinicalmanagement pages 11-12)

**MAPK pathway**
- **PLCG1** activating mutations (e.g., R707Q) can increase IP3 generation and activate MAPK signaling, and PLCG1 mutations may be mutually exclusive with VEGFR2/KDR mutations in some series—supporting alternative, convergent mechanisms to activate downstream growth pathways. (chen2020optimalclinicalmanagement pages 11-12)

**PI3K pathway**
- In primary breast angiosarcoma, activating **PIK3CA** mutations are strongly enriched and functionally activating, indicating PI3K pathway dependence in this subtype and a plausible vulnerability to PI3Kα inhibition. (painter2020theangiosarcomaproject pages 4-7)

**MYC-driven transcriptional/angiogenic programs (secondary disease)**
- Secondary angiosarcomas (especially radiation- or lymphedema-associated cutaneous/breast/chest wall tumors) show frequent high-level **MYC** amplification and MYC-associated transcriptional changes (including miRNA programs) linked to a pro-angiogenic state. (chen2020optimalclinicalmanagement pages 9-11, chang2024clinicopathologicandmolecular pages 10-11)

## 3) Key molecular players

### 3.1 Genes/proteins (HGNC symbols)

**Subtype-enriched genomic alterations with statistics**

**Primary breast angiosarcoma (sporadic)**
- **KDR (VEGFR2):** 8/12 (66.7%) in a 2024 breast angiosarcoma cohort, including hotspot p.T771 in multiple cases. (chang2024clinicopathologicandmolecular pages 10-11)
- **PIK3CA:** 5/12 (41.7%) in the same cohort; Angiosarcoma Project WES found primary breast angiosarcoma significantly enriched for PIK3CA mutations (9/18 vs 1/29; p=0.0003). (chang2024clinicopathologicandmolecular pages 10-11, painter2020theangiosarcomaproject pages 4-7)
- **TP53:** 3/12 (25%) in the same cohort. (chang2024clinicopathologicandmolecular pages 10-11)
- **Mechanistic interpretation:** Angiosarcoma Project identified **TP53 (25%; 9/36 patients)** and **KDR (22%; 8/36 patients)** as significantly mutated above background and **mutually exclusive** (p=0.02); KDR alterations were concentrated in primary breast tumors. (painter2020theangiosarcomaproject pages 4-7)

**Radiation-associated breast/chest wall angiosarcoma (secondary)**
- **MYC amplification:** 89/97 (91.8%) in a large 2024 breast radiation-associated series; in the neoadjuvant-treated subset, all 10 sequenced radiation-associated cases showed MYC amplification. (chang2024clinicopathologicandmolecular pages 10-11, chang2024clinicopathologicandmolecular pages 1-3)
- **FLT4 amplification:** 10/74 (13.5%) in the same report, often co-amplified with MYC. (chang2024clinicopathologicandmolecular pages 10-11)
- **PTPRB:** loss-of-function mutations reported in 10/39 secondary angiosarcomas in a prior mechanistic review. (chen2020optimalclinicalmanagement pages 11-12)
- **Distinct radiation-associated genomic landscape:** radiation-associated angiosarcoma was reported enriched for **MYC, FLT4, CRKL, HRAS, KMT2D** compared with sporadic angiosarcoma, whereas sporadic tumors were enriched for **TP53, KDR, ATM, ATRX**. (dermawan2023distinctgenomiclandscapes pages 1-3)

**UV-associated cutaneous angiosarcoma (head/neck/face/scalp; HNFS)**
- Angiosarcoma Project: HNFS tumors had much higher median TMB (20.7 muts/Mb vs 2.8 non-HNFS) and a dominant UV mutational signature in 10/12 HNFS samples. (painter2020theangiosarcomaproject pages 4-7)
- Exceptional immunotherapy responses were linked to very high TMB and UV signature in individual HNFS cases treated with pembrolizumab (durable >2 years off therapy). (painter2020theangiosarcomaproject pages 7-11)
- Spatial multi-omic profiling of Asian head/neck angiosarcoma reported recurrent mutations in **CSMD3 (18%)**, **LRP1B (18%)**, **MUC16 (18%)**, **POT1 (16%)**, **TP53 (16%)**, and higher TMB in UV-positive disease (p=0.0294). (loh2023spatialtranscriptomicsreveal pages 1-2)

**Other recurrent/functional drivers (across angiosarcoma)**
- **PLCG1 (e.g., R707Q):** reported recurrently (e.g., 3/34 in one cohort; also present in larger series), functionally de-repressing PLCγ1 and activating MAPK signaling; may confer resistance to therapies targeting VEGF/KDR in some contexts. (chen2020optimalclinicalmanagement pages 11-12, kumari2023primarycardiacangiosarcoma pages 3-4)
- **TP53:** variable alteration rates across series; functional role supported by animal/endothelial models where TP53 alterations can lead to angiosarcoma-like tumors. (chen2020optimalclinicalmanagement pages 9-11, chen2020optimalclinicalmanagement pages 7-8)

### 3.2 Chemical entities (therapeutically relevant; CHEBI)

Angiosarcoma treatments are not purely “pathophysiology,” but many clinical implementations directly target core dysregulated pathways:
- **Anti-angiogenic / VEGF-axis agents:** bevacizumab, sorafenib, pazopanib, regorafenib (and others) are used clinically; reported activity is modest in unselected disease (e.g., bevacizumab ORR 9% (2/23); sorafenib ORR 15–23% with median PFS ~3 months; pazopanib ORR ~20% in retrospective data). (chen2020optimalclinicalmanagement pages 5-7)
- **Immune checkpoint inhibitors (ICIs):** pembrolizumab and other anti–PD-1/PD-L1 regimens show notable activity in select cutaneous/UV-high disease and variable responses otherwise. (painter2020theangiosarcomaproject pages 7-11, chen2020optimalclinicalmanagement pages 5-7)

### 3.3 Cell types (CL) and anatomical locations (UBERON)

**Key cell types involved**
- **Endothelial tumor cells** (blood and/or lymphatic endothelium) are the malignant compartment. (chen2020optimalclinicalmanagement pages 11-12, kumari2023primarycardiacangiosarcoma pages 3-4)
- Immune microenvironment cell types repeatedly implicated include **CD8+ T cells**, **macrophages (CD68+)**, **neutrophils (CD15+)**, and **FOXP3+ regulatory T cells**, varying by immune-hot vs immune-cold spatial phenotypes. (loh2023spatialtranscriptomicsreveal pages 1-2)

**Common anatomical sites / subtype anchors**
- **Cutaneous/subcutaneous** disease dominates population incidence datasets (majority of cases). (wagner2024incidenceandpresenting pages 1-2)
- **Scalp/face (UV-exposed head/neck)** are key for the UV/TMB-high subtype. (painter2020theangiosarcomaproject pages 4-7, painter2020theangiosarcomaproject pages 7-11)
- **Breast/chest wall** are key for radiation-associated secondary angiosarcoma after breast irradiation. (wagner2024incidenceandpresenting pages 1-2, chang2024clinicopathologicandmolecular pages 10-11)

## 4) Biological processes (GO-oriented pathophysiology mapping)

The evidence supports disruption of the following GO-relevant process classes:
- **Angiogenesis / vasculature development** (VEGF/VEGFR, Ang/Tie). (chen2020optimalclinicalmanagement pages 11-12, chen2020optimalclinicalmanagement pages 9-11)
- **Endothelial cell proliferation, migration, and sprouting** driven by VEGF receptor activation and downstream PI3K/MAPK cascades. (kumari2023primarycardiacangiosarcoma pages 3-4)
- **Response to hypoxia** (e.g., endoglin upregulation under hypoxia; pro-angiogenic remodeling). (chen2020optimalclinicalmanagement pages 5-7)
- **DNA damage response / double-strand break repair** and mutational processes specific to radiation-associated tumors. (dermawan2023distinctgenomiclandscapes pages 8-10, dermawan2023distinctgenomiclandscapes pages 1-3)
- **Response to ultraviolet light / UV-induced mutagenesis** in HNFS tumors. (painter2020theangiosarcomaproject pages 4-7, painter2020theangiosarcomaproject pages 7-11)
- **Immune response / tumor inflammation programs** (immune-hot vs cold; tumor inflammation signature differences). (loh2023spatialtranscriptomicsreveal pages 1-2)

## 5) Cellular components (where key processes occur)

Mechanistic events described in the evidence primarily map to:
- **Plasma membrane receptor complexes** (VEGFR2/KDR, VEGFR3/FLT4, Tie receptors) initiating signaling. (kumari2023primarycardiacangiosarcoma pages 3-4, chen2020optimalclinicalmanagement pages 5-7)
- **Cytosolic signaling complexes** (PLCγ1-mediated phosphoinositide signaling, MAPK and PI3K/AKT/mTOR cascades). (chen2020optimalclinicalmanagement pages 11-12, kumari2023primarycardiacangiosarcoma pages 3-4)
- **Nuclear transcriptional programs** (MYC-driven transcription and miRNA programs). (chen2020optimalclinicalmanagement pages 9-11, chang2024clinicopathologicandmolecular pages 10-11)
- **Tumor microenvironment compartments** with spatially organized immune infiltration/exclusion patterns. (loh2023spatialtranscriptomicsreveal pages 1-2)

## 6) Disease progression model (sequence of events)

### 6.1 Etiology-dependent initiation → transformation
1. **Initiating insult or predisposition**
   - **UV exposure** for HNFS cutaneous angiosarcoma, associated with UV mutational signatures and high TMB. (painter2020theangiosarcomaproject pages 4-7, painter2020theangiosarcomaproject pages 7-11)
   - **Ionizing radiation** for secondary breast/chest wall angiosarcoma, with latency on the order of years and distinct genomic landscapes consistent with radiation-induced DNA damage and repair. (dermawan2023distinctgenomiclandscapes pages 1-3, wagner2024incidenceandpresenting pages 1-2)
   - **Chronic lymphedema** and other secondary contexts are recognized risk settings and molecularly associated with MYC amplification in secondary disease. (wagner2024incidenceandpresenting pages 1-2, chen2020optimalclinicalmanagement pages 9-11)

2. **Early molecular driver acquisition and lineage program**
   - Secondary radiation/lymphedema-associated lesions frequently acquire **MYC amplification**, driving a pro-angiogenic transcriptional program (including miRNA changes and reduced anti-angiogenic factors). (chen2020optimalclinicalmanagement pages 9-11, chang2024clinicopathologicandmolecular pages 10-11)
   - Primary breast tumors show **KDR** and **PIK3CA** activation, linking endothelial growth factor sensing directly to proliferative survival signaling (PI3K pathway). (painter2020theangiosarcomaproject pages 4-7, chang2024clinicopathologicandmolecular pages 10-11)

3. **Progression: signaling convergence, invasion, and metastasis**
   - Across subtypes, signaling converges on **MAPK** and **PI3K/AKT/mTOR** to support proliferation/survival and the invasive vascular phenotype. (chen2020optimalclinicalmanagement pages 11-12, kumari2023primarycardiacangiosarcoma pages 3-4)
   - Radiation-associated tumors may acquire additional co-alterations (e.g., FLT4, HRAS, KMT2D) consistent with progression and genomic instability. (dermawan2023distinctgenomiclandscapes pages 1-3, chang2024clinicopathologicandmolecular pages 10-11)

### 6.2 Distinct “immune phenotypes” influence clinical behavior and treatment sensitivity
- UV/TMB-high HNFS tumors can be particularly immunogenic, and exceptional responses to PD-1 blockade have been observed in that context, supporting immune selection/escape as part of progression. (painter2020theangiosarcomaproject pages 7-11)
- Spatial profiling reveals immune-hot cases may exhibit tumor-excluded inflammation (immune cells present but spatially segregated), potentially contributing to variable responses. (loh2023spatialtranscriptomicsreveal pages 1-2)

## 7) Phenotypic manifestations (HP-oriented)

Although detailed HP-term enumerations were not provided explicitly in the retrieved texts, the evidence supports the following phenotype classes:
- **Aggressive local infiltration and high recurrence risk**, particularly in cutaneous and radiation-associated breast/chest wall disease. (wagner2024incidenceandpresenting pages 1-2, chen2020optimalclinicalmanagement pages 5-7)
- **Early metastasis** with poor prognosis overall; cutaneous angiosarcoma review reports mean 5-year survival ~33.5%. (guan2023cutaneousangiosarcomaa pages 1-2)
- **Site-specific presentations:** UV-exposed scalp/face lesions (often misrecognized early) and post-radiation chest wall/breast cutaneous nodules in the irradiated field. (wagner2024incidenceandpresenting pages 1-2, dermawan2023distinctgenomiclandscapes pages 1-3)

## 8) Recent developments and latest research (prioritizing 2023–2024)

### 8.1 Population-level epidemiology (2024)
A US population-based analysis (USCS NPCR–SEER combined) identified **19,289** cases (2001–2020) and reported that **“angiosarcoma incidence doubled from 657 cases in 2001 to 1312 in 2019”**, with increasing incidence particularly driven by secondary breast/chest-wall disease in women. (JAMA Network Open, **2024-04**; https://doi.org/10.1001/jamanetworkopen.2024.6235) (wagner2024incidenceandpresenting pages 1-2)

### 8.2 High-resolution subtype genomics and precision targets (2023–2024)
- **Radiation-associated angiosarcoma** shows a distinct landscape compared with other radiation-associated sarcomas and compared with sporadic angiosarcoma, with enrichment for MYC/FLT4/HRAS/KMT2D and relative depletion of TP53 alterations in the radiation-associated setting. (The Journal of Pathology, **2023-06**; https://doi.org/10.1002/path.6137) (dermawan2023distinctgenomiclandscapes pages 1-3)
- **Breast angiosarcoma (2024)**: a large molecular cohort quantified near-ubiquitous MYC amplification in radiation-associated breast angiosarcoma (91.8%) and high prevalence of KDR and PIK3CA alterations in primary breast disease, strengthening the biologic separation of these entities and supporting subtype-tailored therapeutic hypotheses. (Genes Chromosomes Cancer, **2024-05**; https://doi.org/10.1002/gcc.23240) (chang2024clinicopathologicandmolecular pages 10-11)
- **Spatial transcriptomics in head/neck angiosarcoma (2023)**: defines immune-hot/intermediate/cold clusters and shows higher TMB in UV-positive cases, providing a framework for immunotherapy stratification beyond histology alone. (Communications Biology, **2023-04**; https://doi.org/10.1038/s42003-023-04856-5) (loh2023spatialtranscriptomicsreveal pages 1-2)

### 8.3 Immunotherapy biomarker synthesis (2023)
A 2023 review of checkpoint inhibitors in cutaneous angiosarcoma collates evidence that cAS can display **TMB-H**, **PD-L1 positivity**, **UV mutational signature**, **tertiary lymphoid structures**, and **abundant CD8+ TILs**, providing mechanistic rationale for immunotherapy in selected patients. (Frontiers in Medicine, **2023-03**; https://doi.org/10.3389/fmed.2023.1090168) (guan2023cutaneousangiosarcomaa pages 1-2)

## 9) Current applications and real-world implementations

### 9.1 Diagnostic and subclassification biomarkers
- **MYC amplification testing (FISH) and/or MYC IHC** is widely used to support diagnosis of **secondary radiation- or lymphedema-associated angiosarcoma** and to distinguish from benign/atypical post-radiation vascular lesions, consistent with the strong enrichment of MYC amplification in radiation-associated breast disease. (chen2020optimalclinicalmanagement pages 9-11, chang2024clinicopathologicandmolecular pages 10-11)
- Molecular subclassification has direct clinical implications: primary breast angiosarcoma (KDR/PIK3CA-driven) differs biologically and therapeutically from radiation-associated breast angiosarcoma (MYC-amplified). (painter2020theangiosarcomaproject pages 4-7, chang2024clinicopathologicandmolecular pages 10-11)

### 9.2 Therapeutic implementations linked to pathophysiology
- **VEGF/angiogenesis pathway targeting** is a rational strategy but shows heterogeneous and often modest efficacy in unselected populations (e.g., bevacizumab ORR 9%; sorafenib ORR 15–23%; pazopanib ORR ~20% in retrospective series), implying that pathway activation alone is insufficient as a biomarker and that subtype/driver selection is important. (chen2020optimalclinicalmanagement pages 5-7)
- **Immune checkpoint blockade** appears most compelling in **UV/TMB-high cutaneous HNFS** angiosarcoma, where durable, exceptional responses have been documented, consistent with the UV-driven hypermutated state and increased neoantigen burden. (painter2020theangiosarcomaproject pages 7-11)

## 10) Expert opinions and analysis (authoritative sources)

- The angiosarcoma field increasingly treats the disease as a **set of molecularly distinct entities** rather than one tumor type, supported by population-level subtype shifts (secondary breast/chest wall) and by strong subtype-enrichment of drivers such as MYC (secondary) vs KDR/PIK3CA (primary breast) vs UV/TMB-high HNFS disease. (wagner2024incidenceandpresenting pages 1-2, painter2020theangiosarcomaproject pages 4-7, chang2024clinicopathologicandmolecular pages 10-11)
- Mechanistic reviews emphasize **angiogenesis signaling** (VEGF/VEGFR, Tie/Ang) as central but also highlight why anti-angiogenic monotherapy is often insufficient: convergent downstream signaling (MAPK/PI3K), pathway redundancy, and genetically distinct etiologic subtypes. (chen2020optimalclinicalmanagement pages 11-12, chen2020optimalclinicalmanagement pages 5-7)

## 11) Relevant statistics and data (recent studies)

### Epidemiology and incidence
- US (2001–2020): **19,289** cases; incidence doubled from **657 (2001) to 1312 (2019)**; adjusted annual increase leading to **~3.3 per 1,000,000 person-years** (peak stated in the study excerpt), and most tumors were cutaneous/subcutaneous/breast (**72.3%**). (wagner2024incidenceandpresenting pages 1-2)

### Genomics and biomarkers (selected quantitative findings)
- Radiation-associated breast angiosarcoma: **MYC amplification 89/97 (91.8%)**; FLT4 amplification **10/74 (13.5%)**. (chang2024clinicopathologicandmolecular pages 10-11)
- Primary breast angiosarcoma: **KDR 8/12 (66.7%)**, **PIK3CA 5/12 (41.7%)**, **TP53 3/12 (25%)**. (chang2024clinicopathologicandmolecular pages 10-11)
- Angiosarcoma Project WES: **TP53 25% (9/36)**, **KDR 22% (8/36)**, mutually exclusive (p=0.02); HNFS median TMB **20.7 muts/Mb vs 2.8** non-HNFS; UV signature in **10/12** HNFS. (painter2020theangiosarcomaproject pages 4-7)
- Cutaneous head/neck angiosarcoma immune biomarker compilation: PD-L1 positivity **33%** (head/neck cAS in cited cohort) and UV signature **9/18** in one head/neck series. (guan2023cutaneousangiosarcomaa pages 1-2)

## 12) Knowledge base–ready annotation blocks

### 12.1 Pathophysiology description (narrative)
Angiosarcoma is an endothelial malignancy in which dysregulated angiogenesis/lymphangiogenesis is central. Key oncogenic events frequently occur at the level of endothelial receptor signaling (KDR/VEGFR2, FLT4/VEGFR3, Tie/Ang pathways) or in proximal effectors (PLCG1, PTPRB), converging on MAPK and PI3K/AKT/mTOR. Etiology strongly shapes pathophysiology: UV-driven HNFS tumors show UV mutational signatures and high TMB with immune responsiveness in select cases; radiation-associated breast/chest wall tumors show MYC amplification (often with FLT4 co-amplification) and radiation-associated mutational processes; and primary breast tumors are enriched for KDR and activating PIK3CA mutations. (chen2020optimalclinicalmanagement pages 5-7, painter2020theangiosarcomaproject pages 4-7, chang2024clinicopathologicandmolecular pages 10-11)

### 12.2 Gene/protein annotations (HGNC + mechanism + evidence)
- **MYC (HGNC:7553)** — amplification/overexpression in secondary (radiation-associated) angiosarcoma; linked to pro-angiogenic transcriptional and miRNA programs; near-ubiquitous in radiation-associated breast angiosarcoma cohorts. (chen2020optimalclinicalmanagement pages 9-11, chang2024clinicopathologicandmolecular pages 10-11)
- **KDR (HGNC:6307; VEGFR2)** — recurrent mutations enriched in primary breast angiosarcoma; significant driver in Angiosarcoma Project; activates angiogenic RTK signaling leading to PI3K/MAPK activation. (painter2020theangiosarcomaproject pages 4-7, chang2024clinicopathologicandmolecular pages 10-11, kumari2023primarycardiacangiosarcoma pages 3-4)
- **PIK3CA (HGNC:8975)** — activating mutations enriched in primary breast angiosarcoma and functionally activating; implies PI3K pathway dependence. (painter2020theangiosarcomaproject pages 4-7, chang2024clinicopathologicandmolecular pages 10-11)
- **FLT4 (HGNC:3767; VEGFR3)** — amplification in radiation-associated breast angiosarcoma (subset; often co-amplified with MYC), and in radiation-associated angiosarcoma more broadly. (chang2024clinicopathologicandmolecular pages 10-11, dermawan2023distinctgenomiclandscapes pages 1-3)
- **PTPRB (HGNC:9668)** — loss-of-function mutations in secondary angiosarcoma; proposed to deregulate Tie2/VEGFR2 signaling. (chen2020optimalclinicalmanagement pages 11-12)
- **PLCG1 (HGNC:9065)** — activating mutations (e.g., R707Q) increase phosphoinositide signaling and MAPK activation; may be mutually exclusive with KDR mutations in some cohorts. (chen2020optimalclinicalmanagement pages 11-12)
- **TP53 (HGNC:11998)** — recurrent driver, variable frequency by subtype; significant in Angiosarcoma Project and supported by animal models. (painter2020theangiosarcomaproject pages 4-7, chen2020optimalclinicalmanagement pages 7-8)

### 12.3 Cell-type involvement (CL)
- **Endothelial cell (blood/lymphatic)**: malignant compartment; angiogenic signaling dependence. (kumari2023primarycardiacangiosarcoma pages 3-4, chen2020optimalclinicalmanagement pages 5-7)
- **CD8+ T cell**, **macrophage**, **neutrophil**, **Treg (FOXP3+)**: immune microenvironment components with spatially organized “immune-hot/cold” patterns in head/neck disease. (loh2023spatialtranscriptomicsreveal pages 1-2)

### 12.4 Anatomical locations (UBERON)
- **Skin of scalp/face/head & neck**: enriched for UV signature/high TMB subtype. (painter2020theangiosarcomaproject pages 4-7, painter2020theangiosarcomaproject pages 7-11)
- **Breast/chest wall (irradiated field)**: enriched for radiation-associated MYC-amplified subtype. (wagner2024incidenceandpresenting pages 1-2, chang2024clinicopathologicandmolecular pages 10-11)

### 12.5 Chemical entities (CHEBI; examples linked to mechanisms)
- **Bevacizumab (anti-VEGF-A)**, **pazopanib/sorafenib/regorafenib (multi-kinase VEGFR inhibitors)** as real-world angiogenesis-directed agents with modest response rates in unselected populations. (chen2020optimalclinicalmanagement pages 5-7)
- **Pembrolizumab (anti–PD-1)** as an immunotherapy option with strongest mechanistic support in UV/TMB-high cutaneous HNFS disease. (painter2020theangiosarcomaproject pages 7-11, guan2023cutaneousangiosarcomaa pages 1-2)

## 13) Summary table (mechanisms, subtype biology, and immune features)

| Subtype/trigger | Key genomic alterations (with frequencies) | Dysregulated pathways/cellular processes | Immune/TME features | Clinical/phenotypic notes | Key references (PMID if known, otherwise DOI; year) |
|---|---|---|---|---|---|
| UV-associated cutaneous head/neck/face/scalp (HNFS/cAS) | TP53 25% overall cohort (9/36 patients) and KDR 22% (8/36) in Angiosarcoma Project; HNFS specifically showed dominant UV mutational signature in 10/12 cases and markedly higher median TMB 20.7 muts/Mb vs 2.8 in non-HNFS; in Asian AS-HN, recurrent mutations included CSMD3 18%, LRP1B 18%, MUC16 18%, POT1 16%, TP53 16%; review cites UV signatures in 9/18 head/neck cAS (painter2020theangiosarcomaproject pages 4-7, loh2023spatialtranscriptomicsreveal pages 1-2, guan2023cutaneousangiosarcomaa pages 1-2) | UV-mediated mutagenesis; high neoantigen load/TMB; endothelial malignant transformation with angiogenic dependence including VEGF signaling in angiosarcoma broadly (painter2020theangiosarcomaproject pages 7-11, guan2023cutaneousangiosarcomaa pages 1-2, chen2020optimalclinicalmanagement pages 5-7) | Immune-hot/intermediate/cold clusters identified; highest TIS in immune-hot tumors (7.82 vs 7.49 vs 5.90, p=0.00021); CD8+ T cells, neutrophils, macrophages, FOXP3+ Tregs correlated with immune clusters; PD-L1 positivity reported in 33% of head/neck cAS; tertiary lymphoid structures and abundant CD8+ TILs reported in cAS review (loh2023spatialtranscriptomicsreveal pages 1-2, guan2023cutaneousangiosarcomaa pages 1-2) | Commonly arises on sun-exposed scalp/face; older patients, median age 77 in cAS review; poor prognosis with mean 5-year survival ~33.5%; exceptional anti-PD-1 responses seen in very high-TMB/UV-signature HNFS tumors (2 durable responses among 3 HNFS treated off-label) (guan2023cutaneousangiosarcomaa pages 1-2, painter2020theangiosarcomaproject pages 7-11) | DOI:10.1038/s41591-019-0749-z (2020); DOI:10.1038/s42003-023-04856-5 (2023); DOI:10.3389/fmed.2023.1090168 (2023) |
| Radiation-associated breast/chest wall | MYC amplification is the hallmark: ~55-57% of secondary AS in review; 50-100% secondary AS in summary table; in breast RA-AS, MYC amplification 89/97 (91.8%); all 10 post-NACT RA-AS in sequenced subset had MYC amplification; FLT4 amplification 10/74 (13.5%), sometimes co-amplified with MYC; PTPRB loss-of-function 10/39 secondary AS; RT-AS enriched for MYC, FLT4, CRKL, HRAS, KMT2D, whereas sporadic AS enriched for TP53, KDR, ATM, ATRX (chen2020optimalclinicalmanagement pages 9-11, chang2024clinicopathologicandmolecular pages 10-11, chang2024clinicopathologicandmolecular pages 1-3, chen2020optimalclinicalmanagement pages 11-12, dermawan2023distinctgenomiclandscapes pages 1-3) | MYC-driven pro-angiogenic program with miR-17-92 upregulation and reduced THBS1/CTGF; dysregulated VEGF/VEGFR and Tie2 signaling; PTPRB loss may unleash Tie-2/VEGFR-2 signaling; radiation-associated transcriptomic profile shows lymphatic markers PDPN and PROX1; DNA damage/repair error signatures after ionizing radiation (chen2020optimalclinicalmanagement pages 9-11, chen2020optimalclinicalmanagement pages 11-12, dermawan2023distinctgenomiclandscapes pages 1-3) | Generally not characterized by high UV-TMB phenotype; RT-sarcomas show mutational signatures linked to DNA repair/replication defects and increased indel/substitution ratio; PD-L1 in cutaneous AS overall around 40% in older review, but subtype-specific RA-AS immune data remain limited in provided evidence (dermawan2023distinctgenomiclandscapes pages 1-3, chen2020optimalclinicalmanagement pages 5-7) | Typically high-grade cutaneous nodules of chest wall after breast irradiation; median latency ~8.0 years after radiation in RT-AS cohort and 64 months in single-institution RIBAS series; secondary breast angiosarcoma incidence rising; local recurrence frequent (77.8% in one recent series) (dermawan2023distinctgenomiclandscapes pages 1-3, wagner2024incidenceandpresenting pages 1-2) | DOI:10.1002/path.6137 (2023); DOI:10.1002/gcc.23240 (2024); DOI:10.3390/cancers12113321 (2020) |
| Primary breast angiosarcoma | KDR mutations enriched: 8/12 (66.7%) in one breast series, including five p.T771 cases; Angiosarcoma Project found KDR 22% overall and 89% of KDR missense mutations in primary breast AS; PIK3CA 5/12 (41.7%) in breast series and 9/18 primary breast AS in Angiosarcoma Project (significantly enriched vs non-breast, p=0.0003); TP53 3/12 (25%); both primary AS cases in post-NACT sequenced subset harbored KDR mutations (chang2024clinicopathologicandmolecular pages 10-11, painter2020theangiosarcomaproject pages 4-7, chang2024clinicopathologicandmolecular pages 5-6) | VEGFR2/KDR-driven angiogenic signaling; PI3K pathway activation via activating PIK3CA variants; downstream PI3K/AKT/mTOR and MAPK signaling implicated in angiosarcoma biology (painter2020theangiosarcomaproject pages 4-7, chen2020optimalclinicalmanagement pages 9-11, chen2020optimalclinicalmanagement pages 11-12) | Not a classic high-TMB/UV subtype; in breast NACT study, TMB was low (<10 mt/Mb) and did not correlate with response (chang2024clinicopathologicandmolecular pages 5-6) | Distinct from radiation-associated breast AS by younger age and lack of pervasive MYC amplification; primary breast tumors in NACT cohort had poor histologic response and high distant metastatic rate (chang2024clinicopathologicandmolecular pages 5-6, chang2024clinicopathologicandmolecular pages 10-11) | DOI:10.1038/s41591-019-0749-z (2020); DOI:10.1002/gcc.23240 (2024); DOI:10.3390/cancers12113321 (2020) |
| Other/secondary etiologies (lymphedema-associated, mixed secondary, non-breast/post-radiation) | MYC amplification characteristic of irradiation- and lymphedema-associated secondary AS; VEGFR3/FLT4 amplification 18-25% in secondary AS; PTPRB mutations 10/39 secondary AS; PLCG1 R707Q in 3/34 and 8/116 overall series; CIC missense mutations 8/100, mostly primary rather than secondary; RT-AS composition in one 120-case study: 61% primary, 28% radiation-associated, 11% lymphedema-associated (chen2020optimalclinicalmanagement pages 7-8, chen2020optimalclinicalmanagement pages 11-12) | Dysregulated angiogenesis centered on VEGF/VEGFR, Tie/Ang, MAPK, and PI3K/AKT/mTOR; PLCG1 activation increases IP3/MAPK signaling and may be mutually exclusive with VEGFR2 mutation; lymphedema/radiation-associated tumors may show lymphatic differentiation markers (PDPN, PROX1) (chen2020optimalclinicalmanagement pages 11-12, chen2020optimalclinicalmanagement pages 9-11) | Immune data are less well resolved by subtype in provided evidence; checkpoint responses appear variable outside UV-high cutaneous disease; occasional CD4+/CD8+ memory T cells reported across AS and PD-L1 around 40% in cutaneous AS overall (chen2020optimalclinicalmanagement pages 5-7) | Secondary angiosarcoma associated with chronic lymphedema/Stewart-Treves syndrome, prior radiotherapy, foreign material, and other carcinogenic exposures; molecular heterogeneity supports etiologic subclassification and biomarker-guided therapy (wagner2024incidenceandpresenting pages 1-2, chahardehi2024micrornasandangiosarcoma pages 3-4, chen2020optimalclinicalmanagement pages 11-12) | DOI:10.3390/cancers12113321 (2020); DOI:10.3389/fonc.2024.1385632 (2024); DOI:10.1001/jamanetworkopen.2024.6235 (2024) |


*Table: This table summarizes angiosarcoma pathophysiology by major etiologic and clinical subtypes, highlighting subtype-enriched genomic alterations, pathway dysregulation, immune features, and clinical correlates. It is useful for linking disease mechanisms to diagnostic stratification and therapeutic hypotheses.*

## 14) Evidence items (PMID-first, if available)

The retrieved full-text snippets frequently provided DOI/Journal/Year but **did not reliably include PMIDs** in the tool outputs for all sources. Key evidence items (with DOI and date):
- Wagner MJ et al. *JAMA Network Open* **2024-04**. “Incidence…US, 2001–2020.” https://doi.org/10.1001/jamanetworkopen.2024.6235 (wagner2024incidenceandpresenting pages 1-2)
- Chang H-Y et al. *Genes Chromosomes Cancer* **2024-05**. Breast angiosarcoma subtype genomics (MYC in radiation-associated; KDR/PIK3CA in primary). https://doi.org/10.1002/gcc.23240 (chang2024clinicopathologicandmolecular pages 10-11)
- Loh JW et al. *Communications Biology* **2023-04**. Spatial transcriptomics/immune landscapes in head & neck angiosarcoma. https://doi.org/10.1038/s42003-023-04856-5 (loh2023spatialtranscriptomicsreveal pages 1-2)
- Dermawan JK et al. *The Journal of Pathology* **2023-06**. Radiation-associated angiosarcoma genomic landscape. https://doi.org/10.1002/path.6137 (dermawan2023distinctgenomiclandscapes pages 1-3)
- Guan L et al. *Frontiers in Medicine* **2023-03**. Checkpoint inhibitor evidence in cutaneous angiosarcoma. https://doi.org/10.3389/fmed.2023.1090168 (guan2023cutaneousangiosarcomaa pages 1-2)
- Chen TWW et al. *Cancers* **2020-11**. Molecular biology and clinical management (VEGF/Tie, PTPRB/PLCG1, therapy response statistics). https://doi.org/10.3390/cancers12113321 (chen2020optimalclinicalmanagement pages 5-7)
- Painter CA et al. *Nature Medicine* **2020-02**. Angiosarcoma Project WES, UV/TMB findings, KDR/TP53/PIK3CA. https://doi.org/10.1038/s41591-019-0749-z (painter2020theangiosarcomaproject pages 4-7)

References

1. (chen2020optimalclinicalmanagement pages 11-12): Tom Wei-Wu Chen, Jessica Burns, Robin L. Jones, and Paul H. Huang. Optimal clinical management and the molecular biology of angiosarcomas. Cancers, 12:3321, Nov 2020. URL: https://doi.org/10.3390/cancers12113321, doi:10.3390/cancers12113321. This article has 27 citations.

2. (chen2020optimalclinicalmanagement pages 9-11): Tom Wei-Wu Chen, Jessica Burns, Robin L. Jones, and Paul H. Huang. Optimal clinical management and the molecular biology of angiosarcomas. Cancers, 12:3321, Nov 2020. URL: https://doi.org/10.3390/cancers12113321, doi:10.3390/cancers12113321. This article has 27 citations.

3. (painter2020theangiosarcomaproject pages 4-7): Corrie A. Painter, Esha Jain, Brett N. Tomson, Michael Dunphy, Rachel E. Stoddard, Beena S. Thomas, Alyssa L. Damon, Shahrayz Shah, Dewey Kim, Jorge Gómez Tejeda Zañudo, Jason L. Hornick, Yen-Lin Chen, Priscilla Merriam, Chandrajit P. Raut, George D. Demetri, Brian A. Van Tine, Eric S. Lander, Todd R. Golub, and Nikhil Wagle. The angiosarcoma project: enabling genomic and clinical discoveries in a rare cancer through patient-partnered research. Feb 2020. URL: https://doi.org/10.1038/s41591-019-0749-z, doi:10.1038/s41591-019-0749-z. This article has 291 citations and is from a highest quality peer-reviewed journal.

4. (chen2020optimalclinicalmanagement pages 5-7): Tom Wei-Wu Chen, Jessica Burns, Robin L. Jones, and Paul H. Huang. Optimal clinical management and the molecular biology of angiosarcomas. Cancers, 12:3321, Nov 2020. URL: https://doi.org/10.3390/cancers12113321, doi:10.3390/cancers12113321. This article has 27 citations.

5. (kumari2023primarycardiacangiosarcoma pages 3-4): Naina Kumari, Sagar Bhandari, Anzal Ishfaq, Samia Rauf R Butt, Chukwuyem Ekhator, Amanda Karski, Bijan Kadel, Mohamedalamin Alnoor Altayb Ismail, Tenzin N Sherpa, Ahmed Al Khalifa, Bashar Khalifah, Nhan Nguyen, Slobodan Lazarevic, Mohammad Uzair Zaman, Ashraf Ullah, and Vikas Yadav. Primary cardiac angiosarcoma: a review. Cureus, Jul 2023. URL: https://doi.org/10.7759/cureus.41947, doi:10.7759/cureus.41947. This article has 47 citations.

6. (dermawan2023distinctgenomiclandscapes pages 8-10): Josephine K Dermawan, Ping Chi, William D Tap, Evan Rosenbaum, Sandra D'Angelo, Kaled M Alektiar, and Cristina R Antonescu. Distinct genomic landscapes in radiation‐associated angiosarcoma compared with other radiation‐associated sarcoma histologies. The Journal of Pathology, 260:465-477, Jun 2023. URL: https://doi.org/10.1002/path.6137, doi:10.1002/path.6137. This article has 17 citations.

7. (dermawan2023distinctgenomiclandscapes pages 1-3): Josephine K Dermawan, Ping Chi, William D Tap, Evan Rosenbaum, Sandra D'Angelo, Kaled M Alektiar, and Cristina R Antonescu. Distinct genomic landscapes in radiation‐associated angiosarcoma compared with other radiation‐associated sarcoma histologies. The Journal of Pathology, 260:465-477, Jun 2023. URL: https://doi.org/10.1002/path.6137, doi:10.1002/path.6137. This article has 17 citations.

8. (painter2020theangiosarcomaproject pages 7-11): Corrie A. Painter, Esha Jain, Brett N. Tomson, Michael Dunphy, Rachel E. Stoddard, Beena S. Thomas, Alyssa L. Damon, Shahrayz Shah, Dewey Kim, Jorge Gómez Tejeda Zañudo, Jason L. Hornick, Yen-Lin Chen, Priscilla Merriam, Chandrajit P. Raut, George D. Demetri, Brian A. Van Tine, Eric S. Lander, Todd R. Golub, and Nikhil Wagle. The angiosarcoma project: enabling genomic and clinical discoveries in a rare cancer through patient-partnered research. Feb 2020. URL: https://doi.org/10.1038/s41591-019-0749-z, doi:10.1038/s41591-019-0749-z. This article has 291 citations and is from a highest quality peer-reviewed journal.

9. (chang2024clinicopathologicandmolecular pages 10-11): Hsin‐Yi Chang, Josephine K. Dermawan, Maria Gabriela Kuba, Aimee M. Crago, Samuel Singer, William Tap, Ping Chi, Sandra D'Angelo, Evan Rosenbaum, and Cristina R. Antonescu. Clinicopathologic and molecular correlates to neoadjuvant chemotherapy‐induced pathologic response in breast angiosarcoma. Genes, May 2024. URL: https://doi.org/10.1002/gcc.23240, doi:10.1002/gcc.23240. This article has 6 citations.

10. (chang2024clinicopathologicandmolecular pages 1-3): Hsin‐Yi Chang, Josephine K. Dermawan, Maria Gabriela Kuba, Aimee M. Crago, Samuel Singer, William Tap, Ping Chi, Sandra D'Angelo, Evan Rosenbaum, and Cristina R. Antonescu. Clinicopathologic and molecular correlates to neoadjuvant chemotherapy‐induced pathologic response in breast angiosarcoma. Genes, May 2024. URL: https://doi.org/10.1002/gcc.23240, doi:10.1002/gcc.23240. This article has 6 citations.

11. (loh2023spatialtranscriptomicsreveal pages 1-2): Jui Wan Loh, Jing Yi Lee, Abner Herbert Lim, Peiyong Guan, Boon Yee Lim, Bavani Kannan, Elizabeth Chun Yong Lee, Ning Xin Gu, Tun Kiat Ko, Cedric Chuan-Young Ng, Jeffrey Chun Tatt Lim, Joe Yeong, Jing Quan Lim, Choon Kiat Ong, Bin Tean Teh, and Jason Yongsheng Chan. Spatial transcriptomics reveal topological immune landscapes of asian head and neck angiosarcoma. Communications Biology, Apr 2023. URL: https://doi.org/10.1038/s42003-023-04856-5, doi:10.1038/s42003-023-04856-5. This article has 27 citations and is from a peer-reviewed journal.

12. (chen2020optimalclinicalmanagement pages 7-8): Tom Wei-Wu Chen, Jessica Burns, Robin L. Jones, and Paul H. Huang. Optimal clinical management and the molecular biology of angiosarcomas. Cancers, 12:3321, Nov 2020. URL: https://doi.org/10.3390/cancers12113321, doi:10.3390/cancers12113321. This article has 27 citations.

13. (wagner2024incidenceandpresenting pages 1-2): Michael J. Wagner, Vinod Ravi, Stephanie K. Schaub, Ed Y. Kim, Jeremy Sharib, Harveshp Mogal, Min Park, Michaela Tsai, Daniela Duarte-Bateman, Anthony Tufaro, Elizabeth T. Loggers, Lee D. Cranmer, Bonny Chau, Michael J. Hassett, Juneko Grilley-Olson, and Kelly G. Paulson. Incidence and presenting characteristics of angiosarcoma in the us, 2001-2020. JAMA Network Open, 7:e246235, Apr 2024. URL: https://doi.org/10.1001/jamanetworkopen.2024.6235, doi:10.1001/jamanetworkopen.2024.6235. This article has 38 citations and is from a peer-reviewed journal.

14. (guan2023cutaneousangiosarcomaa pages 1-2): Lucy Guan, Marisa Palmeri, and Roman Groisberg. Cutaneous angiosarcoma: a review of current evidence for treatment with checkpoint inhibitors. Frontiers in Medicine, Mar 2023. URL: https://doi.org/10.3389/fmed.2023.1090168, doi:10.3389/fmed.2023.1090168. This article has 28 citations.

15. (chang2024clinicopathologicandmolecular pages 5-6): Hsin‐Yi Chang, Josephine K. Dermawan, Maria Gabriela Kuba, Aimee M. Crago, Samuel Singer, William Tap, Ping Chi, Sandra D'Angelo, Evan Rosenbaum, and Cristina R. Antonescu. Clinicopathologic and molecular correlates to neoadjuvant chemotherapy‐induced pathologic response in breast angiosarcoma. Genes, May 2024. URL: https://doi.org/10.1002/gcc.23240, doi:10.1002/gcc.23240. This article has 6 citations.

16. (chahardehi2024micrornasandangiosarcoma pages 3-4): Amir Modarresi Chahardehi, Arya Afrooghe, Nikoo Emtiazi, Sajjad Rafiei, Negin Jafarkhanloo Rezaei, Sarvin Dahmardeh, Fatemeh Farz, Zahra Naderi, Reza Arefnezhad, and Hossein Motedayyen. Micrornas and angiosarcoma: are there promising reports? Frontiers in Oncology, May 2024. URL: https://doi.org/10.3389/fonc.2024.1385632, doi:10.3389/fonc.2024.1385632. This article has 5 citations.