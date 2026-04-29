---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-06T03:36:15.892706'
end_time: '2026-03-06T03:51:21.797267'
duration_seconds: 905.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pancreatic Ductal Adenocarcinoma
  mondo_id: ''
  category: Solid Tumor
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Pancreatic Ductal Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:** Solid Tumor

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Pancreatic Ductal Adenocarcinoma**.
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
- **Disease Name:** Pancreatic Ductal Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:** Solid Tumor

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Pancreatic Ductal Adenocarcinoma**.
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


## Comprehensive Research Report: Pathophysiology of Pancreatic Ductal Adenocarcinoma (PDAC)

### Target disease and identifiers
- **Disease:** Pancreatic ductal adenocarcinoma (PDAC)
- **MONDO ID:** **MONDO:0005184** (Open Targets disease record for “pancreatic ductal adenocarcinoma”) (vitorakis2024precisiontargetingstrategies pages 2-3)

---

## 1) Key concepts and definitions (current understanding)

### 1.1 Definition and core biological framing
PDAC is a malignant epithelial tumor arising from the pancreatic ductal system (or ductal-like cells derived from acinar reprogramming), characterized by (i) near-universal oncogenic KRAS pathway activation, (ii) frequent inactivation of a small set of core tumor suppressors, and (iii) a uniquely **fibro-inflammatory, desmoplastic tumor microenvironment (TME)** that strongly constrains perfusion, immune infiltration, and drug delivery (sherman2023tumormicroenvironmentin pages 4-6, finan2024challengesandopportunities pages 1-2).

A key modern concept is that PDAC is not purely a cancer-cell autonomous disease; rather, it is an **ecosystem-level disease** in which non-malignant stromal and immune compartments co-evolve with the neoplastic epithelium and meaningfully drive progression and therapy resistance (finan2024challengesandopportunities pages 1-2, sherman2023tumormicroenvironmentin pages 4-6).

### 1.2 Precursor lesions and progression model
Two major precursor lesion routes dominate contemporary models:
- **PanIN** lesions account for **~85–90%** of PDAC and
- **IPMN** lesions account for **~10–15%** (linehan2024targetingkrasmutations pages 2-4, terza2024transcriptionalandspatial pages 24-26).

These lesions acquire additional genetic/epigenetic alterations over time, culminating in invasive carcinoma with metastatic competence (graham2024fromprecursorto pages 8-9, sherman2023tumormicroenvironmentin pages 4-6).

---

## 2) Core pathophysiology (molecular and cellular mechanisms)

### 2.1 Cell-intrinsic oncogenic programs
#### KRAS-centered oncogenic signaling
KRAS is the dominant initiating oncogene in PDAC. Multiple recent reviews converge on the point that **KRAS mutation is an early event**, detectable in low-grade precursor lesions and present in the vast majority of PDAC tumors (linehan2024targetingkrasmutations pages 2-4).

Mechanistically, KRAS engages canonical downstream cascades:
- **MAPK/RAF–MEK–ERK**: “Activated KRAS ignites phosphorylation of RAF and subsequently… ERK 1 and 2” (linehan2024targetingkrasmutations pages 2-4).
- **PI3K–AKT**: “Activated PI3K phosphorylates… PIP3 promoting AKT phosphorylation” (linehan2024targetingkrasmutations pages 2-4).

These pathways support proliferation, survival, and transcriptional programs that enable malignant progression and plasticity, particularly in inflammatory contexts (sherman2023tumormicroenvironmentin pages 4-6, hashimoto2024plasticityandtumor pages 3-5).

#### Core tumor suppressor losses and malignant progression
Multiple 2024 syntheses summarize the canonical PDAC “four-driver” framework and provide quantitative prevalence estimates:
- “The driver genes in PDAC are four: KRAS…SMAD4…CDKN2A/p16…TP53” and “KRAS mutations are prevalent in **80–95%** of PDACs” (vitorakis2024precisiontargetingstrategies pages 2-3).
- CDKN2A/p16 inactivation occurs in “**more than 90%**” of PDAC (vitorakis2024precisiontargetingstrategies pages 2-3, reshkin2024geneticsignatureof pages 3-4).
- TP53 disruption occurs in about “**six out of ten**” tumors (~60%) (vitorakis2024precisiontargetingstrategies pages 2-3) and is also summarized as common in progression (graham2024fromprecursorto pages 8-9).
- SMAD4 loss is “prevalent in **half** of the cases” (~50%) (vitorakis2024precisiontargetingstrategies pages 2-3, reshkin2024geneticsignatureof pages 3-4).

Recent precursor-focused review work (2024) emphasizes the dual role of intrinsic alterations and extrinsic cues (inflammation, fibroblast activation, immune modulation) in driving PanIN progression to PDAC (graham2024fromprecursorto pages 8-9).

### 2.2 Cell-extrinsic programs: the desmoplastic, immunosuppressive ecosystem

#### Desmoplasia and ECM barriers
PDAC is strongly defined by extensive fibrosis and ECM deposition. A recent 2024 review states that PDAC stroma “can make up… **as much as 90%** of its volume” (vitorakis2024precisiontargetingstrategies pages 6-8). In another 2024 review, PDAC is described as an “ecosystem, with up to **80% of the mass** consisting of nontumor stromal cells and extracellular matrix (ECM)” (finan2024challengesandopportunities pages 1-2).

The ECM is biochemically dominated by:
- “hyaluronic acid (HA)” and
- “collagens type I, III, and IV” (vitorakis2024precisiontargetingstrategies pages 6-8).

These components are not merely structural: “lower levels of stromal HA and collagen are linked to improved survival rates” in observational analyses summarized in 2024 (vitorakis2024precisiontargetingstrategies pages 6-8). This provides a mechanistic rationale for ECM/HA-degrading approaches (see Applications).

#### CAF heterogeneity and immunoregulatory roles
A major advance in 2023–2024 is the consolidation of CAF heterogeneity into functionally distinct subsets. Belle et al. (Cancer Discovery; final publication July 1, 2024; DOI: **10.1158/2159-8290.CD-23-0428**; URL: https://doi.org/10.1158/2159-8290.CD-23-0428) describe PDAC TME as “dense collagen-rich extracellular matrix (ECM) harboring an abundance of carcinoma-associated fibroblasts (CAFs)” and note that PDAC has a “5-year survival rate of **12%**” (belle2024senescencedefinesa pages 1-3).

They also provide a clear scRNA-seq-derived CAF taxonomy:
- “Myofibroblastic CAFs (myCAFs) are enriched for ECM factors… (Acta2); Inflammatory CAFs (iCAF) are enriched for cytokines… like Il6; Antigen-presenting CAFs (apCAFs) express Cd74 and MHCII genes” (belle2024senescencedefinesa pages 1-3).

Critically, CAFs are not neutral; CAF subsets can directly impose immune exclusion/suppression. Belle et al. summarize that “FAP+ CAFs recruit immunosuppressive macrophages and spatially exclude CD8+ T cells… through **CXCL12/SDF1-CXCR4** sequestration” (belle2024senescencedefinesa pages 1-3). This mechanism is a central “pathophysiology-to-therapy” bridge in PDAC.

In the same work, senescence is elevated as a stromal state that shapes immunity and treatment response: “Senescence defines a distinct subset of myofibroblasts that… orchestrates immunosuppression in pancreatic cancer” (belle2024senescencedefinesa pages 1-3). Visual evidence for CAF subset structure and SenCAF-associated immunosuppressive circuitry is shown in Belle et al. figures (belle2024senescencedefinesa media 67220de1, belle2024senescencedefinesa media 1506df91).

#### Immunosuppressive leukocyte networks
A 2024 clinical/translational review lists major checkpoint regulators of CD8 T cells: “PD-1… CTLA-4… TIM-3… TIGIT” (finan2024challengesandopportunities pages 1-2). It also provides direct evidence that “Treg cells are recruited to tumors via… CCL2 and CCL5” and then suppress cytotoxic immunity through “IL-10, TGF-b, CTLA-4, granzyme B” (finan2024challengesandopportunities pages 1-2).

These immune suppressive programs are reinforced by oncogenic KRAS signaling and by physical/ecological restrictions imposed by the ECM-rich stroma (sherman2023tumormicroenvironmentin pages 4-6, finan2024challengesandopportunities pages 1-2).

### 2.3 Metabolic rewiring and immune–metabolic coupling

#### KRAS-driven glycolysis and hypoxia adaptation
Bonilla et al. (JCI Insight; Aug 2024; DOI: **10.1172/jci.insight.180114**; URL: https://doi.org/10.1172/jci.insight.180114) compile mechanistic evidence that oncogenic KRAS upregulates glycolysis programs in PDAC (e.g., “HK1/2… PFK1… LDHA”), increases glucose uptake via PI3K-Akt–mediated GLUT1 expression, and increases lactate generation (bonilla2024metaboliclandscapeof pages 21-25).

Hashimoto & Hashimoto (Cancers; Dec 2024; DOI: **10.3390/cancers16234094**; URL: https://doi.org/10.3390/cancers16234094) further emphasize hypoxia-driven metabolic switching: hypoxia/HIF-1α induces “GLUT1, LDHA and MCT4,” shifting from OXPHOS to glycolysis and exporting lactate; the resulting “acidic TME… inhibits CD8+ T-cells and NK cells” and promotes immunosuppressive macrophage states (hashimoto2024plasticityandtumor pages 8-9).

#### Glutamine dependence and nutrient scavenging
Recent reviews highlight PDAC “glutamine addiction” and scavenging programs. Hashimoto & Hashimoto note glutamine’s role in supporting the TCA cycle and redox, and report that glutaminase inhibition (BPTES) suppresses PDAC proliferation in cited work (hashimoto2024plasticityandtumor pages 8-9, hashimoto2024plasticityandtumor pages 9-10). 

Both Bonilla et al. and Hashimoto & Hashimoto emphasize **autophagy and macropinocytosis** as nutrient acquisition strategies in KRAS-mutant PDAC (bonilla2024metaboliclandscapeof pages 21-25, hashimoto2024plasticityandtumor pages 10-12). 

#### Autophagy as immune evasion
Gautam et al. (Molecular Cancer; Jul 2023; DOI: **10.1186/s12943-023-01813-y**; URL: https://doi.org/10.1186/s12943-023-01813-y) provide a specific mechanistic immune-evasion statement: “constitutively active KRasG12D regulates **autophagy-induced MHCI downregulation**” (gautam2023molecularandmetabolic pages 1-2). This connects oncogenic metabolism/trafficking to reduced antigen presentation.

---

## 3) Key molecular players, cell types, anatomical sites, and chemical entities

### 3.1 Genes/Proteins (HGNC; causality/implication)
Core driver set repeatedly emphasized in 2024 syntheses:
- **KRAS**, **TP53**, **CDKN2A**, **SMAD4** (vitorakis2024precisiontargetingstrategies pages 2-3, reshkin2024geneticsignatureof pages 3-4).

Additional mechanisms and mediators:
- **CXCL12–CXCR4** (CAF/PSC-mediated immune exclusion) (belle2024senescencedefinesa pages 1-3, vitorakis2024precisiontargetingstrategies pages 8-10).
- **Immune checkpoints:** PD-1, CTLA-4, TIM-3, TIGIT (finan2024challengesandopportunities pages 1-2).

### 3.2 Chemical entities (metabolites / ECM)
- **Hyaluronic acid (HA)**, **collagens** (I/III/IV) as dominant ECM components (vitorakis2024precisiontargetingstrategies pages 6-8).
- **Lactate** as a glycolytic end product shaping an acidic immunosuppressive microenvironment (hashimoto2024plasticityandtumor pages 8-9, bonilla2024metaboliclandscapeof pages 21-25).
- **Glutamine** as a major carbon/nitrogen source enabling growth in nutrient-restricted settings (hashimoto2024plasticityandtumor pages 8-9, bonilla2024metaboliclandscapeof pages 21-25).

### 3.3 Cell types (CL-style)
- CAF subsets: **myCAF**, **iCAF**, **apCAF**, plus senescent myCAF/SenCAF states (belle2024senescencedefinesa pages 1-3).
- Immune suppressive populations: **Tregs**, **TAMs**, **MDSCs** (finan2024challengesandopportunities pages 1-2, linehan2024targetingkrasmutations pages 2-4).
- **Pancreatic stellate cells (PSCs)** as major myofibroblast-like drivers of desmoplasia (vitorakis2024precisiontargetingstrategies pages 8-10).

### 3.4 Anatomical locations (UBERON-style)
- **Pancreas** and **pancreatic ductal system** as the primary site; PanIN lesions form in pancreatic epithelium context (graham2024fromprecursorto pages 8-9, sherman2023tumormicroenvironmentin pages 4-6).
- **Liver** as a major metastatic destination with distinct immune/metabolic niche properties (gautam2023molecularandmetabolic pages 1-2).

---

## 4) Biological processes (GO-style) and cellular components (GO-CC-style)

### 4.1 Disrupted biological processes
Representative GO-style processes supported by 2023–2024 evidence include:
- **Epithelial cell transformation / acinar-to-ductal metaplasia**, linked to KRAS and inflammatory priming (sherman2023tumormicroenvironmentin pages 4-6, graham2024fromprecursorto pages 8-9).
- **Extracellular matrix organization / collagen fibril organization / desmoplastic reaction** (vitorakis2024precisiontargetingstrategies pages 6-8, finan2024challengesandopportunities pages 1-2).
- **Immune evasion** via checkpoint regulation and antigen presentation suppression (MHC-I downregulation) (finan2024challengesandopportunities pages 1-2, gautam2023molecularandmetabolic pages 1-2).
- **Aerobic glycolysis**, **lactate production/export**, **glutamine metabolism**, **autophagy**, **macropinocytosis** (hashimoto2024plasticityandtumor pages 8-9, bonilla2024metaboliclandscapeof pages 21-25, hashimoto2024plasticityandtumor pages 10-12).

### 4.2 Key cellular components
- **Extracellular matrix (ECM)**: collagen-rich; HA-rich (belle2024senescencedefinesa pages 1-3, vitorakis2024precisiontargetingstrategies pages 6-8).
- **Autophagosome/lysosome system** (autophagy-mediated immune escape and nutrient recycling) (gautam2023molecularandmetabolic pages 1-2, hashimoto2024plasticityandtumor pages 10-12).
- **MHC class I complex / cell surface antigen presentation machinery**, functionally downregulated by KRAS-linked autophagy (gautam2023molecularandmetabolic pages 1-2).

---

## 5) Disease progression: sequence of events (trigger → clinical manifestations)

### 5.1 Initiation: genetic + inflammatory “two-lens” model
A central contemporary model is that KRAS mutation initiates neoplastic potential, but **inflammation/pancreatitis-like microenvironmental cues** collaborate with KRAS to enable PanIN formation and progression by bypassing intrinsic barriers such as senescence and by inducing transcriptional/epigenetic reprogramming (sherman2023tumormicroenvironmentin pages 4-6, graham2024fromprecursorto pages 8-9).

### 5.2 Pre-invasive lesions → invasive carcinoma
Precursor lesions (PanIN/IPMN) acquire sequential tumor suppressor alterations (CDKN2A, TP53, SMAD4) and additional chromosomal/epigenetic changes that coincide with rising dysplasia grade and invasive transition (graham2024fromprecursorto pages 8-9, reshkin2024geneticsignatureof pages 3-4).

### 5.3 Ecosystem maturation and therapy resistance
As PDAC develops, the stroma expands and diversifies, including CAF subsets and immunosuppressive leukocytes. This produces:
- physical barriers (HA/collagen),
- hypoxia and altered metabolite gradients,
- immune exclusion (CXCL12/CXCR4), and
- checkpoint-mediated T cell dysfunction (belle2024senescencedefinesa pages 1-3, finan2024challengesandopportunities pages 1-2).

### 5.4 Metastasis and pre-metastatic niche conditioning
A 2023 metastatic immunosuppression review describes dissemination “following chemokine and exosomal guidance” to organ-specific **pre-metastatic niches (PMNs)** composed of resident cells, fibroblasts, and suppressive immune cells such as “metastasis-associated macrophages, neutrophils, and myeloid-derived suppressor cells” (gautam2023molecularandmetabolic pages 1-2).

---

## 6) Phenotypic manifestations and clinical correlates

### 6.1 Survival and stage-at-diagnosis statistics (recent sources)
Recent 2024 sources report consistently poor outcomes:
- 5-year survival **~13%** (Finan et al., published Dec 18, 2024; DOI: 10.1200/OA-24-00050; URL: https://doi.org/10.1200/OA-24-00050) (finan2024challengesandopportunities pages 1-2).
- “only… about **13%** of PDAC patients does the overall survival exceed 5 years” (Poyia et al., Sep 2024; DOI: 10.3390/ijms25179555; URL: https://doi.org/10.3390/ijms25179555) (poyia2024theroleof pages 1-2).
- Belle et al. cite 5-year survival **12%** (Cancer Discovery 2024; DOI: 10.1158/2159-8290.CD-23-0428; URL: https://doi.org/10.1158/2159-8290.CD-23-0428) (belle2024senescencedefinesa pages 1-3).

### 6.2 Mutation frequencies and clinical phenotypes
- KRAS mutation frequency is reported as **80–95%** (vitorakis2024precisiontargetingstrategies pages 2-3) and also summarized as **~90%** (poyia2024theroleof pages 1-2).
- Tumor suppressor inactivation estimates vary by cohort and review: “50–80% have inactivating mutations in TP53, CDKN2A, and SMAD4” (poyia2024theroleof pages 1-2), whereas other 2024 compilations provide ~60% TP53 and ~50% SMAD4 (vitorakis2024precisiontargetingstrategies pages 2-3).

### 6.3 TME-driven phenotypes
The dense, HA/collagen-rich stroma produces hypoperfusion, high interstitial pressure, and immune exclusion, which clinically correspond to:
- chemoresistance,
- immunotherapy resistance (“cold” tumors), and
- aggressive local invasion and early metastatic spread (finan2024challengesandopportunities pages 1-2, vitorakis2024precisiontargetingstrategies pages 6-8).

---

## 7) Recent developments and latest research (prioritizing 2023–2024)

### 7.1 CAF subset refinement, senescence biology, and immunosuppression (2024)
A key 2024 advance is the identification of **senescent myofibroblastic CAFs (SenCAFs)** and evidence that senescent stromal depletion can “relieve immune suppression by macrophages, delay tumor progression and increase responsiveness to chemotherapy” in models (belle2024senescencedefinesa pages 1-3). The associated figures provide a mechanistic schematic for SenCAF→macrophage→CD8 T cell dysfunction (belle2024senescencedefinesa media 1506df91) and CAF subset structure (belle2024senescencedefinesa media 67220de1).

### 7.2 Ecosystem quantification and CAF lineages (2024)
Finan et al. quantify the stromal burden (up to 80% mass) and emphasize that CAFs are heterogeneous in both origin and function, with only “10%–15% of CAFs… derived from PSCs” (finan2024challengesandopportunities pages 1-2). They also note dynamic interconversion between iCAFs and myCAFs (finan2024challengesandopportunities pages 1-2).

### 7.3 Metabolic ecosystem mapping and immune metabolism (2024)
Bonilla et al. (Aug 2024) synthesize mechanistic evidence linking KRAS to glycolytic reprogramming, glutamine rewiring, autophagy/macropinocytosis, and immune dysfunction via nutrient competition (bonilla2024metaboliclandscapeof pages 21-25). Hashimoto & Hashimoto (Dec 2024) emphasize HIF-1α-driven lactate export and its immune suppressive consequences in acidic PDAC microenvironments (hashimoto2024plasticityandtumor pages 8-9).

### 7.4 Metastatic immunometabolic “hot spots” (2023)
A 2023 metastatic PDAC review emphasizes that metastatic immune ecosystems differ from primary tumors in “composition, functionality, and metabolism,” and formalizes PMN formation via “chemokine and exosomal guidance” (gautam2023molecularandmetabolic pages 1-2).

---

## 8) Current applications and real-world implementations

### 8.1 Stromal/ECM targeting (hyaluronan and related strategies)
A 2024 ASCO/clinical review summarizes ECM/hyaluronan-targeting efforts including **PEGPH20 (hyaluronidase)** in combinations:
- HALO 109-301,
- PEGPH20 + pembrolizumab (PCRT16-001),
- MORPHEUS platform (atezolizumab + PEGPH20) (finan2024challengesandopportunities pages 20-21).

These efforts are directly motivated by the pathophysiology that HA impairs vascular function and drug delivery in PDAC (finan2024challengesandopportunities pages 20-21, vitorakis2024precisiontargetingstrategies pages 6-8).

### 8.2 Immune targeting beyond PD-1/CTLA-4 (adenosine/CD73 axis)
A 2024 trial compendium highlights multiple trials targeting immunosuppressive adenosine biology, including:
- A2A/A2B antagonists (NCT04580485),
- anti-CD73 strategies (e.g., NCT04989387), and CD73 small-molecule inhibition with checkpoint blockade (zimberelimab + quemliclustat; NCT05688215) (do2024theroadahead pages 3-4).

### 8.3 Antigen/vaccine approaches including KRAS-directed vaccines (2024)
A 2024 review catalogs KRAS-directed vaccine efforts, including **ELI-002** (NCT04853017) containing “G12D and G12R mutant KRAS peptides” (do2024theroadahead pages 6-8).

### 8.4 Imaging/biomarkers that operationalize stromal biology: 68Ga-FAPI PET
A 2024 CAF-focused review describes **FAP** as a CAF marker leveraged for clinical imaging and notes that **Gallium-68 FAP inhibitor (68Ga-FAPI) PET/CT** has “promising diagnostic sensitivity and specificity” with low non-tumoral uptake and expected intensive uptake in PDAC (saudeconde2024cancerassociatedfibroblastsin pages 1-2). This is a direct real-world implementation grounded in PDAC’s CAF-rich desmoplasia.

---

## 9) Expert opinions and analysis (authoritative sources)

### 9.1 Why PDAC resists therapy
The 2024 ASCO review frames PDAC’s poor response as partially attributable to the “dense stroma and heterogeneous tumor microenvironment (TME)” and notes that many stromal-targeting trials “have failed to improve overall patient outcomes” when translated clinically, motivating combination and stratification strategies (finan2024challengesandopportunities pages 1-2).

### 9.2 Why CAF targeting is complex
Belle et al. explicitly note contradictory outcomes in CAF depletion studies and interpret this as evidence of “underappreciated phenotypic heterogeneity of CAFs,” arguing for subset- and state-specific targeting rather than global stromal ablation (belle2024senescencedefinesa pages 1-3).

---

## 10) Evidence-driven structured content for knowledge-base population

| Mechanism / Process | Key Molecular Players | Key Cell Types | Dysregulated Pathways | Key Findings & Evidence | Key Sources (2023-2024) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **KRAS-Driven Initiation & Progression** | **KRAS** (G12D/V/R), IL-33 | Acinar cells, Ductal cells | **MAPK/ERK**, PI3K-AKT, Ral | KRAS mutations (>90% of PDAC) are the initiating event, driving acinar-to-ductal metaplasia (ADM) and PanINs; requires inflammation (e.g., IL-33) to bypass senescence and amplify transformation. | (vitorakis2024precisiontargetingstrategies pages 2-3, linehan2024targetingkrasmutations pages 2-4, graham2024fromprecursorto pages 8-9, sherman2023tumormicroenvironmentin pages 4-6) |
| **Tumor Suppressor Inactivation** | **CDKN2A** (p16), **TP53**, **SMAD4**, BRCA2 | Neoplastic epithelial cells | Cell cycle (G1/S), DNA repair, TGF-β | Progressive accumulation: CDKN2A lost early (>90%); TP53 (~60-70%) and SMAD4 (~50%) lost in high-grade PanIN/invasive disease, driving genomic instability and malignancy. | (vitorakis2024precisiontargetingstrategies pages 2-3, linehan2024targetingkrasmutations pages 2-4, graham2024fromprecursorto pages 8-9, reshkin2024geneticsignatureof pages 3-4) |
| **Desmoplasia & ECM Barriers** | **Hyaluronan** (HA), Collagens (I, III, IV), Fibronectin | **PSCs** (Pancreatic Stellate Cells), CAFs | Hedgehog (SHH), TGF-β | Dense stroma (up to 90% tumor volume) creates high interstitial pressure, hypoxia, and a physical barrier to drugs/immune cells; driven by PSC activation. | (vitorakis2024precisiontargetingstrategies pages 6-8, finan2024challengesandopportunities pages 1-2, saudeconde2024cancerassociatedfibroblastsin pages 1-2, vitorakis2024precisiontargetingstrategies pages 8-10) |
| **CAF Heterogeneity & Function** | FAP, α-SMA, IL-6, MHC-II, **CXCL12** | **myCAF** (myofibroblastic), **iCAF** (inflammatory), **apCAF**, **SenCAF** | IL-1/JAK-STAT, TGF-β, **CXCL12/CXCR4** | Distinct subsets: myCAFs (ECM-producing, α-SMA high); iCAFs (IL-6 high); apCAF (antigen-presenting); **SenCAF** (senescent) accumulate with progression. FAP+ CAFs exclude CD8+ T cells via CXCL12. | (belle2024senescencedefinesa pages 1-3, finan2024challengesandopportunities pages 1-2, erreni2024depictingthecellular pages 12-13) |
| **Immune Evasion & Suppression** | PD-L1, CTLA-4, CCL2, CCL5, Galectin-1 | **Tregs**, **TAMs** (M2-like), MDSCs | Immune checkpoint, Chemokine signaling | "Cold" tumor phenotype; KRAS-driven GM-CSF/chemokines recruit MDSCs/Tregs. Autophagy downregulates MHC-I. TAMs support fibrosis and suppress CTLs. | (gautam2023molecularandmetabolic pages 1-2, belle2024senescencedefinesa pages 1-3, finan2024challengesandopportunities pages 1-2, finan2024challengesandopportunities pages 20-21) |
| **Metabolic Rewiring** | GLUT1, LDHA, Glutaminase (GLS) | PDAC cells, CAFs | **Glycolysis** (Warburg), Glutaminolysis, Mevalonate | KRAS drives glucose uptake/glycolysis and "glutamine addiction." Nutrient scavenging via **macropinocytosis** and **autophagy** (recycling) supports growth in nutrient-poor TME. | (hashimoto2024plasticityandtumor pages 8-9, hashimoto2024plasticityandtumor pages 9-10, bonilla2024metaboliclandscapeof pages 21-25) |
| **TME Metabolic Crosstalk** | Lactate, Lipids, Cholesterol | Tumor cells, Immune cells | HIF-1α (Hypoxia), mTORC1 | Hypoxia/HIF-1α shifts cells to glycolysis, exporting **lactate** which acidifies TME and suppresses T cells. TAMs/stroma engage in lipid/cholesterol exchange with tumor cells. | (hashimoto2024plasticityandtumor pages 8-9, bonilla2024metaboliclandscapeof pages 25-29, bonilla2024metaboliclandscapeof pages 21-25, bonilla2024metaboliclandscapeof pages 17-21) |
| **Metastatic Niche (PMN)** | Exosomes, Chemokines | Metastasis-Associated Macrophages (MAMs) | EMT, Exosomal guidance | Primary tumors secrete factors/exosomes to prime pre-metastatic niches (PMNs) in liver/lung; metastatic cells have distinct metabolic/immune profiles from primary. | (gautam2023molecularandmetabolic pages 1-2, sherman2023tumormicroenvironmentin pages 4-6) |


*Table: A structured summary of the primary pathophysiological mechanisms in Pancreatic Ductal Adenocarcinoma, highlighting the interplay between genetic drivers, the tumor microenvironment (TME), and metabolic alterations as described in 2023-2024 literature.*

| Entity Type | Identifier / Name | Role in PDAC | Evidence Snippet / Mechanism | Supporting Sources (2023-2024) |
| :--- | :--- | :--- | :--- | :--- |
| **Gene (HGNC)** | **KRAS** | Driver (Initiation) | "KRAS mutations are prevalent in 80–95% of PDACs" driving initiation/ADM. | (vitorakis2024precisiontargetingstrategies pages 2-3, linehan2024targetingkrasmutations pages 2-4) |
| **Gene (HGNC)** | **TP53** | Tumor Suppressor | Inactivation in ~60-70% contributes to genomic instability in progression. | (vitorakis2024precisiontargetingstrategies pages 2-3, reshkin2024geneticsignatureof pages 3-4) |
| **Gene (HGNC)** | **CDKN2A** (p16) | Tumor Suppressor | "CDKN2A/p16 deactivation... in more than 90% of PDACs." | (vitorakis2024precisiontargetingstrategies pages 2-3) |
| **Gene (HGNC)** | **SMAD4** | Tumor Suppressor | Loss associated with progression; "prevalent in half of the cases." | (vitorakis2024precisiontargetingstrategies pages 2-3, graham2024fromprecursorto pages 8-9) |
| **Cell Type (CL)** | **myCAF** | Stromal Remodeling | "aSMAhigh, ECM-producing myofibroblastic CAFs"; generate collagen barrier. | (belle2024senescencedefinesa pages 1-3, finan2024challengesandopportunities pages 1-2) |
| **Cell Type (CL)** | **iCAF** | Inflammation | "IL-6high inflammatory CAFs"; secrete cytokines, support immunosuppression. | (belle2024senescencedefinesa pages 1-3, finan2024challengesandopportunities pages 1-2) |
| **Cell Type (CL)** | **SenCAF** | Immunosuppression | "Senescent myofibroblastic CAFs... orchestrate immunosuppression" via CXCL12. | (belle2024senescencedefinesa pages 1-3) |
| **Cell Type (CL)** | **PSC** | Progenitor | "Pancreatic stellate cells... key myofibroblast-like drivers of desmoplasia." | (vitorakis2024precisiontargetingstrategies pages 8-10, finan2024challengesandopportunities pages 1-2) |
| **Bio Process (GO)** | **Glycolysis** | Metabolic Rewiring | KRAS upregulates GLUT1/LDHA; "hypoxia... enforces glycolytic programming." | (hashimoto2024plasticityandtumor pages 8-9, bonilla2024metaboliclandscapeof pages 21-25) |
| **Bio Process (GO)** | **Macropinocytosis** | Nutrient Scavenging | "KRAS-driven macropinocytosis supplies free amino acids" (scavenging). | (hashimoto2024plasticityandtumor pages 8-9, hashimoto2024plasticityandtumor pages 10-12) |
| **Bio Process (GO)** | **Autophagy** | Survival & Evasion | Recycles nutrients; "regulates autophagy-induced MHCI downregulation" (evasion). | (gautam2023molecularandmetabolic pages 1-2, hashimoto2024plasticityandtumor pages 10-12) |
| **Chemical (ChEBI)** | **Hyaluronan** (HA) | ECM Component | "Predominant component" of stroma; raises interstitial pressure, impairs drugs. | (vitorakis2024precisiontargetingstrategies pages 6-8, finan2024challengesandopportunities pages 20-21) |
| **Chemical (ChEBI)** | **Lactate** | Metabolite | Exported by tumor cells; "creates an acidic TME that inhibits cytotoxic CD8+." | (hashimoto2024plasticityandtumor pages 8-9, bonilla2024metaboliclandscapeof pages 21-25) |
| **Chemical (ChEBI)** | **Glutamine** | Metabolite | "Glutamine addiction"; fuels TCA cycle and lipid synthesis via reductive path. | (hashimoto2024plasticityandtumor pages 8-9, hashimoto2024plasticityandtumor pages 9-10) |
| **Anatomy (UBERON)** | **Liver** | Metastatic Site | Most common metastatic site; "metastatic immune microenvironment differs from primary." | (gautam2023molecularandmetabolic pages 1-2) |


*Table: A structured table mapping key PDAC entities (genes, cell types, processes, chemicals) to their specific pathophysiological roles and evidence, suitable for disease knowledge base integration.*

---

## 11) Visual evidence (figures/tables)

- Belle et al. 2024 provides figure evidence for CAF subset structure and SenCAF-associated immunosuppressive circuitry (CAF clusters/markers; schematic of SenCAF→macrophage→CD8 dysfunction) (belle2024senescencedefinesa media 67220de1, belle2024senescencedefinesa media 1506df91).

---

## 12) Evidence items (PMID notes)
Where possible, PMID was requested; however, many retrieved full texts and excerpts provided DOIs/URLs without explicit PMID strings in the extracted passages. A notable exception is that Open Targets evidence lists historical PubMed IDs for KRAS–PDAC associations (e.g., PMID: 29658583) but these are not the primary 2023–2024 mechanistic sources extracted here (vitorakis2024precisiontargetingstrategies pages 2-3). For the core 2023–2024 mechanistic statements, this report therefore cites **DOI/URL + publication date** and the exact extracted text evidence.


References

1. (vitorakis2024precisiontargetingstrategies pages 2-3): Nikolaos Vitorakis, Antonios N. Gargalionis, Kostas A. Papavassiliou, Christos Adamopoulos, and Athanasios G. Papavassiliou. Precision targeting strategies in pancreatic cancer: the role of tumor microenvironment. Cancers, 16:2876, Aug 2024. URL: https://doi.org/10.3390/cancers16162876, doi:10.3390/cancers16162876. This article has 17 citations.

2. (sherman2023tumormicroenvironmentin pages 4-6): Mara H. Sherman and Gregory L. Beatty. Tumor microenvironment in pancreatic cancer pathogenesis and therapeutic resistance. Annual Review of Pathology: Mechanisms of Disease, 18:123-148, Jan 2023. URL: https://doi.org/10.1146/annurev-pathmechdis-031621-024600, doi:10.1146/annurev-pathmechdis-031621-024600. This article has 415 citations and is from a domain leading peer-reviewed journal.

3. (finan2024challengesandopportunities pages 1-2): Jennifer M. Finan, Yifei Guo, Shaun M. Goodyear, and Jonathan R. Brody. Challenges and opportunities in targeting the complex pancreatic tumor microenvironment. JCO Oncology Advances, Dec 2024. URL: https://doi.org/10.1200/oa-24-00050, doi:10.1200/oa-24-00050. This article has 16 citations.

4. (linehan2024targetingkrasmutations pages 2-4): Anna Linehan, Mary O’Reilly, Ray McDermott, and Grainne M. O’Kane. Targeting kras mutations in pancreatic cancer: opportunities for future strategies. Frontiers in Medicine, Mar 2024. URL: https://doi.org/10.3389/fmed.2024.1369136, doi:10.3389/fmed.2024.1369136. This article has 47 citations.

5. (terza2024transcriptionalandspatial pages 24-26): F La Terza. Transcriptional and spatial analysis of il-1β+ tumor-associated macrophages in pancreatic ductal adenocarcinoma. Unknown journal, 2024.

6. (graham2024fromprecursorto pages 8-9): Sarah Graham, Mariia Dmitrieva, Debora Barbosa Vendramini-Costa, Ralph Francescone, Maria A Trujillo, Edna Cukierman, and Laura D Wood. From precursor to cancer: decoding the intrinsic and extrinsic pathways of pancreatic intraepithelial neoplasia progression. Carcinogenesis, 45:801-816, Nov 2024. URL: https://doi.org/10.1093/carcin/bgae064, doi:10.1093/carcin/bgae064. This article has 6 citations and is from a peer-reviewed journal.

7. (hashimoto2024plasticityandtumor pages 3-5): Ari Hashimoto and Shigeru Hashimoto. Plasticity and tumor microenvironment in pancreatic cancer: genetic, metabolic, and immune perspectives. Cancers, 16:4094, Dec 2024. URL: https://doi.org/10.3390/cancers16234094, doi:10.3390/cancers16234094. This article has 7 citations.

8. (reshkin2024geneticsignatureof pages 3-4): Stephan J. Reshkin, Rosa Angela Cardone, and Tomas Koltai. Genetic signature of human pancreatic cancer and personalized targeting. Cells, 13:602, Mar 2024. URL: https://doi.org/10.3390/cells13070602, doi:10.3390/cells13070602. This article has 10 citations.

9. (vitorakis2024precisiontargetingstrategies pages 6-8): Nikolaos Vitorakis, Antonios N. Gargalionis, Kostas A. Papavassiliou, Christos Adamopoulos, and Athanasios G. Papavassiliou. Precision targeting strategies in pancreatic cancer: the role of tumor microenvironment. Cancers, 16:2876, Aug 2024. URL: https://doi.org/10.3390/cancers16162876, doi:10.3390/cancers16162876. This article has 17 citations.

10. (belle2024senescencedefinesa pages 1-3): Jad I. Belle, Devashish Sen, John M. Baer, Xiuting Liu, Varintra E. Lander, Jiayu Ye, Blake E. Sells, Brett L. Knolhoff, Ahmad Faiz, Liang-I Kang, Guhan Qian, Ryan C. Fields, Li Ding, Hyun Kim, Paolo P. Provenzano, Sheila A. Stewart, and David G. DeNardo. Senescence defines a distinct subset of myofibroblasts that orchestrates immunosuppression in pancreatic cancer. Cancer discovery, 14:1324-1355, Apr 2024. URL: https://doi.org/10.1158/2159-8290.cd-23-0428, doi:10.1158/2159-8290.cd-23-0428. This article has 82 citations and is from a highest quality peer-reviewed journal.

11. (belle2024senescencedefinesa media 67220de1): Jad I. Belle, Devashish Sen, John M. Baer, Xiuting Liu, Varintra E. Lander, Jiayu Ye, Blake E. Sells, Brett L. Knolhoff, Ahmad Faiz, Liang-I Kang, Guhan Qian, Ryan C. Fields, Li Ding, Hyun Kim, Paolo P. Provenzano, Sheila A. Stewart, and David G. DeNardo. Senescence defines a distinct subset of myofibroblasts that orchestrates immunosuppression in pancreatic cancer. Cancer discovery, 14:1324-1355, Apr 2024. URL: https://doi.org/10.1158/2159-8290.cd-23-0428, doi:10.1158/2159-8290.cd-23-0428. This article has 82 citations and is from a highest quality peer-reviewed journal.

12. (belle2024senescencedefinesa media 1506df91): Jad I. Belle, Devashish Sen, John M. Baer, Xiuting Liu, Varintra E. Lander, Jiayu Ye, Blake E. Sells, Brett L. Knolhoff, Ahmad Faiz, Liang-I Kang, Guhan Qian, Ryan C. Fields, Li Ding, Hyun Kim, Paolo P. Provenzano, Sheila A. Stewart, and David G. DeNardo. Senescence defines a distinct subset of myofibroblasts that orchestrates immunosuppression in pancreatic cancer. Cancer discovery, 14:1324-1355, Apr 2024. URL: https://doi.org/10.1158/2159-8290.cd-23-0428, doi:10.1158/2159-8290.cd-23-0428. This article has 82 citations and is from a highest quality peer-reviewed journal.

13. (bonilla2024metaboliclandscapeof pages 21-25): Monica E. Bonilla, Megan D. Radyk, Matthew D. Perricone, Ahmed M. Elhossiny, Alexis C. Harold, Paola I. Medina-Cabrera, Padma Kadiyala, Jiaqi Shi, Timothy L. Frankel, Eileen S. Carpenter, Michael D. Green, Cristina Mitrea, Costas A. Lyssiotis, and Marina Pasca di Magliano. Metabolic landscape of the healthy pancreas and pancreatic tumor microenvironment. JCI Insight, Aug 2024. URL: https://doi.org/10.1172/jci.insight.180114, doi:10.1172/jci.insight.180114. This article has 7 citations and is from a domain leading peer-reviewed journal.

14. (hashimoto2024plasticityandtumor pages 8-9): Ari Hashimoto and Shigeru Hashimoto. Plasticity and tumor microenvironment in pancreatic cancer: genetic, metabolic, and immune perspectives. Cancers, 16:4094, Dec 2024. URL: https://doi.org/10.3390/cancers16234094, doi:10.3390/cancers16234094. This article has 7 citations.

15. (hashimoto2024plasticityandtumor pages 9-10): Ari Hashimoto and Shigeru Hashimoto. Plasticity and tumor microenvironment in pancreatic cancer: genetic, metabolic, and immune perspectives. Cancers, 16:4094, Dec 2024. URL: https://doi.org/10.3390/cancers16234094, doi:10.3390/cancers16234094. This article has 7 citations.

16. (hashimoto2024plasticityandtumor pages 10-12): Ari Hashimoto and Shigeru Hashimoto. Plasticity and tumor microenvironment in pancreatic cancer: genetic, metabolic, and immune perspectives. Cancers, 16:4094, Dec 2024. URL: https://doi.org/10.3390/cancers16234094, doi:10.3390/cancers16234094. This article has 7 citations.

17. (gautam2023molecularandmetabolic pages 1-2): S. Gautam, S. Batra, and Maneesh Jain. Molecular and metabolic regulation of immunosuppression in metastatic pancreatic ductal adenocarcinoma. Molecular Cancer, Jul 2023. URL: https://doi.org/10.1186/s12943-023-01813-y, doi:10.1186/s12943-023-01813-y. This article has 76 citations and is from a highest quality peer-reviewed journal.

18. (vitorakis2024precisiontargetingstrategies pages 8-10): Nikolaos Vitorakis, Antonios N. Gargalionis, Kostas A. Papavassiliou, Christos Adamopoulos, and Athanasios G. Papavassiliou. Precision targeting strategies in pancreatic cancer: the role of tumor microenvironment. Cancers, 16:2876, Aug 2024. URL: https://doi.org/10.3390/cancers16162876, doi:10.3390/cancers16162876. This article has 17 citations.

19. (poyia2024theroleof pages 1-2): Fotini Poyia, Christiana M. Neophytou, Maria-Ioanna Christodoulou, and Panagiotis Papageorgis. The role of tumor microenvironment in pancreatic cancer immunotherapy: current status and future perspectives. International Journal of Molecular Sciences, 25:9555, Sep 2024. URL: https://doi.org/10.3390/ijms25179555, doi:10.3390/ijms25179555. This article has 24 citations.

20. (finan2024challengesandopportunities pages 20-21): Jennifer M. Finan, Yifei Guo, Shaun M. Goodyear, and Jonathan R. Brody. Challenges and opportunities in targeting the complex pancreatic tumor microenvironment. JCO Oncology Advances, Dec 2024. URL: https://doi.org/10.1200/oa-24-00050, doi:10.1200/oa-24-00050. This article has 16 citations.

21. (do2024theroadahead pages 3-4): Chris T P Do, Jack Y Prochnau, Angel A. Dominguez, Pei Wang, and Manjeet Rao. The road ahead in pancreatic cancer: emerging trends and therapeutic prospects. Biomedicines, Sep 2024. URL: https://doi.org/10.3390/biomedicines12091979, doi:10.3390/biomedicines12091979. This article has 10 citations.

22. (do2024theroadahead pages 6-8): Chris T P Do, Jack Y Prochnau, Angel A. Dominguez, Pei Wang, and Manjeet Rao. The road ahead in pancreatic cancer: emerging trends and therapeutic prospects. Biomedicines, Sep 2024. URL: https://doi.org/10.3390/biomedicines12091979, doi:10.3390/biomedicines12091979. This article has 10 citations.

23. (saudeconde2024cancerassociatedfibroblastsin pages 1-2): Rita Saúde-Conde, Ayça Arçay Öztürk, Kosta Stosic, Oier Azurmendi Senar, Julie Navez, Christelle Bouchart, Tatjana Arsenijevic, Patrick Flamen, and Jean-Luc Van Laethem. Cancer-associated fibroblasts in pancreatic ductal adenocarcinoma or a metaphor for heterogeneity: from single-cell analysis to whole-body imaging. Biomedicines, 12:591, Mar 2024. URL: https://doi.org/10.3390/biomedicines12030591, doi:10.3390/biomedicines12030591. This article has 13 citations.

24. (erreni2024depictingthecellular pages 12-13): Marco Erreni, Maria Rita Fumagalli, Raffaella D’Anna, Mauro Sollai, Silvia Bozzarelli, Gennaro Nappo, Damiano Zanini, Raffaella Parente, Cecilia Garlanda, Lorenza Rimassa, Luigi Maria Terracciano, Subhra K. Biswas, Alessandro Zerbi, Alberto Mantovani, and Andrea Doni. Depicting the cellular complexity of pancreatic adenocarcinoma by imaging mass cytometry: focus on cancer-associated fibroblasts. Frontiers in Immunology, Nov 2024. URL: https://doi.org/10.3389/fimmu.2024.1472433, doi:10.3389/fimmu.2024.1472433. This article has 3 citations and is from a peer-reviewed journal.

25. (bonilla2024metaboliclandscapeof pages 25-29): Monica E. Bonilla, Megan D. Radyk, Matthew D. Perricone, Ahmed M. Elhossiny, Alexis C. Harold, Paola I. Medina-Cabrera, Padma Kadiyala, Jiaqi Shi, Timothy L. Frankel, Eileen S. Carpenter, Michael D. Green, Cristina Mitrea, Costas A. Lyssiotis, and Marina Pasca di Magliano. Metabolic landscape of the healthy pancreas and pancreatic tumor microenvironment. JCI Insight, Aug 2024. URL: https://doi.org/10.1172/jci.insight.180114, doi:10.1172/jci.insight.180114. This article has 7 citations and is from a domain leading peer-reviewed journal.

26. (bonilla2024metaboliclandscapeof pages 17-21): Monica E. Bonilla, Megan D. Radyk, Matthew D. Perricone, Ahmed M. Elhossiny, Alexis C. Harold, Paola I. Medina-Cabrera, Padma Kadiyala, Jiaqi Shi, Timothy L. Frankel, Eileen S. Carpenter, Michael D. Green, Cristina Mitrea, Costas A. Lyssiotis, and Marina Pasca di Magliano. Metabolic landscape of the healthy pancreas and pancreatic tumor microenvironment. JCI Insight, Aug 2024. URL: https://doi.org/10.1172/jci.insight.180114, doi:10.1172/jci.insight.180114. This article has 7 citations and is from a domain leading peer-reviewed journal.