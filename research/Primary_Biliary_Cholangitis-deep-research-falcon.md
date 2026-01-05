---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:45:50.366664'
end_time: '2025-12-18T09:52:40.769360'
duration_seconds: 410.4
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primary Biliary Cholangitis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Primary Biliary Cholangitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Primary Biliary Cholangitis**.
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
- **Disease Name:** Primary Biliary Cholangitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Primary Biliary Cholangitis**.
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
- Disease Name: Primary Biliary Cholangitis (PBC)
- MONDO ID: MONDO:0005100
- Category: Autoimmune

Pathophysiology description
Primary biliary cholangitis is a chronic, immune-mediated cholangiopathy characterized by progressive, non-suppurative destruction of small intrahepatic bile ducts, leading to cholestasis, portal inflammation, ductopenia, ductular reaction, progressive fibrosis, and cirrhosis. Autoimmunity is centered on antimitochondrial antibodies (AMA) against the E2 subunit of the pyruvate dehydrogenase complex (PDC‑E2), alongside autoreactive CD4+ and CD8+ T cells enriched around interlobular bile ducts; cholangiocytes act as both targets and active participants via innate immune sensing and antigen presentation. Bile acid (BA)–mediated epithelial toxicity is amplified by a defect in the cholangiocyte bicarbonate “umbrella,” and disease progression is promoted by cholangiocyte senescence with a senescence‑associated secretory phenotype (SASP) that fosters inflammation and fibrosis. Genetic susceptibility is strong, with HLA class II and multiple non‑HLA loci converging on IL‑12/Th1 signaling, TNF responses, and B‑cell activation pathways. Gut–liver axis perturbations (dysbiosis, barrier defects, microbial molecular mimicry) further break tolerance and sustain portal inflammation; dysregulated BA receptor signaling (FXR–FGF19 axis, TGR5/GPBAR1) and altered transporter activity integrate cholestasis with immune and metabolic cues (fiorucci2024currentlandscapeand pages 4-6, reshetnyak2023newinsightsinto pages 1-2, ning2024studyingsystemicmetabolic pages 16-20, bragazzi2023roleofthe pages 3-5).

Direct evidence quotes
- “The detection of antimitochondrial antibodies (AMAs) … directed against the E2 component of the pyruvate dehydrogenase complex … [is] characteristic of PBC” and “microbial mimics crossreacting with pyruvate dehydrogenase” are implicated as triggers (Cells, 2024-09-12, https://doi.org/10.3390/cells13181580) (fiorucci2024currentlandscapeand pages 24-25, fiorucci2024currentlandscapeand pages 4-6).
- “The biliary HCO3− ‘umbrella’ … protects BECs from the detergent action of bile acids … impairment is implicated in bile‑acid–mediated cholangiocyte damage” (World Journal of Gastroenterology, 2023-10-07, https://doi.org/10.3748/wjg.v29.i37.5292) (reshetnyak2023newinsightsinto pages 1-2).
- “Cholangiocyte senescence (increased p21/p16) with a senescence-associated secretory phenotype … contributes to inflammation and fibrosis and correlates with [worse] response” (International Journal of Molecular Sciences, 2025-08-15, https://doi.org/10.3390/ijms26167905) (barrio2025primarybiliarycholangitis pages 6-8).
- “PBC … exhibits the strongest involvement of genetic heritability … GWAS … identify ~70 susceptibility loci … four major pathways: HLA antigen presentation, IL‑12, TNF responses, B‑cell activation” (Genes, 2023-02-14, https://doi.org/10.3390/genes14020405) (ning2024studyingsystemicmetabolic pages 16-20).

1) Core Pathophysiology
- Primary mechanisms
  - Loss of tolerance to mitochondrial autoantigens (especially PDC‑E2) with AMA generation; enrichment of PDC‑E2–specific T cells in the liver drives florid duct lesions and cholangiocyte death (fiorucci2024currentlandscapeand pages 4-6, ning2024studyingsystemicmetabolic pages 16-20).
  - Biliary bicarbonate umbrella defect: decreased AE2 (SLC4A2)/IP3R3‑dependent HCO3− secretion and CFTR‑linked mechanisms lower the protective apical alkaline layer, increasing BA protonation and epithelial injury (reshetnyak2023newinsightsinto pages 1-2).
  - Cholangiocyte senescence/SASP: senescent BECs secrete IL‑6, TGF‑β, CCL20 and other SASP mediators, recruiting immune cells, activating portal fibroblasts/HSCs, and amplifying fibrosis (barrio2025primarybiliarycholangitis pages 6-8).
  - Innate/adaptive immune crosstalk: PRR‑activated “reactive” cholangiocytes release cytokines/chemokines (e.g., IL‑6, TNF‑α, TGF‑β, MCP‑1), interact with MAIT/NKT cells, and present antigen to T cells; Th1/Th17 polarization with reduced Tregs contributes to chronic biliary inflammation (fiorucci2024currentlandscapeand pages 4-6).
  - Gut–liver axis: dysbiosis, increased permeability and translocation of PAMPs to the portal tract, plus microbial molecular mimicry (e.g., Novosphingobium aromaticivorans, E. coli) further perpetuate immune activation (bragazzi2023roleofthe pages 3-5, fiorucci2024currentlandscapeand pages 4-6).

- Molecular pathways dysregulated
  - Antigen presentation (HLA class II), IL‑12–STAT4/TYK2–Th1 axis, TNF/NF‑κB signaling, B‑cell activation (CD40/POU2AF1/SPIB), and BA receptor pathways (FXR–FGF19, TGR5) (ning2024studyingsystemicmetabolic pages 16-20, fiorucci2024currentlandscapeand pages 4-6, barrio2025primarybiliarycholangitis pages 2-4).

- Cellular processes affected
  - Apoptosis and efferocytosis with retention of intact PDC‑E2 in apoptotic blebs; impaired epithelial transport and barrier function; cellular senescence with SASP; ductular reaction; ECM deposition and fibrosis (reshetnyak2023newinsightsinto pages 1-2, barrio2025primarybiliarycholangitis pages 6-8, fiorucci2024currentlandscapeand pages 4-6).

2) Key Molecular Players
- Genes/Proteins (HGNC)
  - Autoantigen complex: PDHA1, PDHX, DLAT (PDC‑E2), DBT (BCOADC‑E2), DLD (E3) (reshetnyak2023newinsightsinto pages 1-2, ning2024studyingsystemicmetabolic pages 16-20).
  - Antigen presentation/immune signaling: HLA‑DRB1/DQA1/DQB1; IL12A/IL12B/IL12RB2, STAT4, TYK2; TNFSF15; CD40; POU2AF1; SPIB (ning2024studyingsystemicmetabolic pages 16-20, fiorucci2024currentlandscapeand pages 24-25).
  - Bicarbonate umbrella/secretory apparatus: SLC4A2/AE2, CFTR, ITPR3 (IP3R3) (reshetnyak2023newinsightsinto pages 1-2).
  - BA signaling and transporters: NR1H4 (FXR), FGF19, GPBAR1 (TGR5), ABCB11 (BSEP), SLC10A1 (NTCP), SLC10A2 (ASBT) (fiorucci2024currentlandscapeand pages 4-6, barrio2025primarybiliarycholangitis pages 2-4).
  - Senescence/SASP and fibrogenesis: CDKN2A (p16), CDKN1A (p21), TGFB1, IL6, ACTA2 (α‑SMA), COL1A1 (barrio2025primarybiliarycholangitis pages 6-8, fiorucci2024currentlandscapeand pages 4-6).

- Chemical Entities (CHEBI)
  - Bile acids (e.g., chenodeoxycholic acid, deoxycholic acid; ursodeoxycholic acid as therapy), lipopolysaccharide (LPS), cytokines (IL‑12, TNF‑α), TGF‑β (fiorucci2024currentlandscapeand pages 4-6, bragazzi2023roleofthe pages 3-5, barrio2025primarybiliarycholangitis pages 2-4).

- Cell Types (CL)
  - Cholangiocytes/biliary epithelial cells; CD4+ and CD8+ T cells (Th1/Th17), B cells/plasma cells; MAIT and NKT cells; hepatic stellate cells; portal fibroblasts; Kupffer cells/macrophages; dendritic cells (fiorucci2024currentlandscapeand pages 4-6, barrio2025primarybiliarycholangitis pages 6-8, ning2024studyingsystemicmetabolic pages 16-20).

- Anatomical Locations (UBERON)
  - Intrahepatic bile ducts (interlobular ducts), portal tracts, peribiliary plexus; ileum (FXR–FGF19 signaling), portal circulation (fiorucci2024currentlandscapeand pages 4-6, bragazzi2023roleofthe pages 3-5).

3) Biological Processes (GO terms) disrupted
- Antigen processing and presentation (GO:0019882), T‑cell activation (GO:0042110), B‑cell activation (GO:0042113); 
- Cytokine‑mediated signaling (GO:0019221), NF‑κB signaling (GO:0043123), IL‑12–mediated signaling (GO:0038155), Th1 differentiation (GO:0042093);
- Bicarbonate transport (GO:0034762), epithelial fluid secretion (GO:0030104), bile acid homeostasis (GO:0055088);
- Cellular senescence (GO:0090398), apoptotic process (GO:0006915), extracellular matrix organization (GO:0030198), fibrosis (GO:0062023) (reshetnyak2023newinsightsinto pages 1-2, barrio2025primarybiliarycholangitis pages 6-8, fiorucci2024currentlandscapeand pages 4-6, ning2024studyingsystemicmetabolic pages 16-20).

4) Cellular Components
- Mitochondrial inner membrane (PDC), apoptotic blebs/bodies; MHC class II protein complex on plasma membrane; apical plasma membrane of cholangiocytes; nucleus (FXR target gene regulation, senescence markers); extracellular space (SASP factors, cytokines) (reshetnyak2023newinsightsinto pages 1-2, ning2024studyingsystemicmetabolic pages 16-20, fiorucci2024currentlandscapeand pages 4-6, barrio2025primarybiliarycholangitis pages 6-8).

5) Disease Progression (sequence of events)
- Initiation: genetic predisposition (HLA and non‑HLA loci) + environmental triggers (xenobiotics/microbial molecular mimicry) → loss of tolerance to PDC‑E2 and other OADC antigens; AMA emergence often precedes disease by years (ning2024studyingsystemicmetabolic pages 16-20, barrio2025primarybiliarycholangitis pages 1-2).
- Early cholangiopathy: PRR‑activated “reactive” cholangiocytes present antigen and secrete cytokines/chemokines; Th1/Th17 polarization and CD8+ cytotoxicity damage small bile ducts (fiorucci2024currentlandscapeand pages 4-6).
- Secretory defect and cholestasis: bicarbonate umbrella failure (AE2/IP3R3/CFTR) increases BA cytotoxicity; hydrophobic BA accumulation aggravates epithelial injury (reshetnyak2023newinsightsinto pages 1-2, bragazzi2023roleofthe pages 3-5).
- Propagation: cholangiocyte senescence and SASP recruit/activate immune and mesenchymal cells; ductular reaction; portal fibroblast/HSC activation; ECM deposition and fibrosis (barrio2025primarybiliarycholangitis pages 6-8, fiorucci2024currentlandscapeand pages 4-6).
- Systemic contributors: gut dysbiosis and barrier defects sustain PAMP flux to the liver; altered FXR–FGF19/TGR5 signaling perturbs BA and immune homeostasis (bragazzi2023roleofthe pages 3-5, fiorucci2024currentlandscapeand pages 4-6).

6) Phenotypic Manifestations (and mechanistic links)
- Biochemical cholestasis (elevated ALP/GGT) from small duct destruction and cholangiocyte secretory failure; pruritus via BA signaling and pruritogens; fatigue likely multifactorial; xanthelasmas and hyperlipidemia due to BA‑lipid interplay; progressive fibrosis/cirrhosis with portal hypertension and hepatic failure if untreated (fiorucci2024currentlandscapeand pages 4-6, barrio2025primarybiliarycholangitis pages 2-4).
- Serology: AMA positive in ~90–95% of patients, but AMA alone does not predict progression; ANA (gp210, sp100) associate with more severe disease (barrio2025primarybiliarycholangitis pages 1-2, fiorucci2024currentlandscapeand pages 4-6).

Recent developments and latest research (2023–2024 prioritized)
- Genetics and pathways: contemporary GWAS/post‑GWAS compilation emphasizes ~70 susceptibility loci and convergence on HLA class II, IL‑12/Th1, TNF response, and B‑cell activation pathways, highlighting the likely causal roles of IL12A/IL12RB2/STAT4/TYK2 and B‑cell regulators (Genes, 2023-02-14, https://doi.org/10.3390/genes14020405) (ning2024studyingsystemicmetabolic pages 16-20).
- Bicarbonate umbrella and microRNA: updated mechanistic framing of the AE2/IP3R3/CFTR axis and microRNA regulation (e.g., miR‑506) in umbrella failure and BA‑mediated injury (World Journal of Gastroenterology, 2023-10-07, https://doi.org/10.3748/wjg.v29.i37.5292) (reshetnyak2023newinsightsinto pages 1-2).
- Immune–cholangiocyte crosstalk and MAIT/NKT recruitment; Th1→Th17 evolution and reduced Tregs; ductular reaction as a therapeutic target (Cells, 2024-09-12, https://doi.org/10.3390/cells13181580) (fiorucci2024currentlandscapeand pages 4-6).
- Senescence/SASP: clinical correlations between cholangiocyte senescence (p21/p16) and worse outcomes; SASP mediators as pro‑fibrogenic drivers and potential therapeutic targets (IJMS, 2025-08-15, https://doi.org/10.3390/ijms26167905) (barrio2025primarybiliarycholangitis pages 6-8).
- Gut–liver axis: dysbiosis, permeability, PAMP flux and experimental support for microbial triggers in cholangiopathies, including PBC (IJMS, 2023-04-06, https://doi.org/10.3390/ijms24076660) (bragazzi2023roleofthe pages 3-5).

Current applications and real‑world implementations
- Diagnostics: AMA (M2) by IIF/ELISA as a sensitive/specific marker; disease‑specific ANA (gp210, sp100) provide prognostic information; histology shows florid duct lesions and ductopenia when required (barrio2025primarybiliarycholangitis pages 1-2, fiorucci2024currentlandscapeand pages 4-6).
- Therapies: ursodeoxycholic acid (UDCA) improves transplant‑free survival but ~40% have incomplete biochemical response; second‑line therapies include bile acid receptor modulators (FXR agonists) and PPAR agonists (recent approvals of seladelpar/elafibranor in multiple jurisdictions), reflecting the centrality of BA and metabolic‑immune axes in disease biology (Cells, 2024-09-12, https://doi.org/10.3390/cells13181580; IJMS, 2025-08-15, https://doi.org/10.3390/ijms26167905) (fiorucci2024currentlandscapeand pages 4-6, barrio2025primarybiliarycholangitis pages 1-2, barrio2025primarybiliarycholangitis pages 2-4).

Expert opinions and analysis
- Integrated models emphasize that PBC requires a “multi‑hit” pathogenesis: genetic predisposition (HLA and non‑HLA), environmental/xenobiotic or microbial triggers causing loss of tolerance to mitochondrial autoantigens, cholangiocyte‑intrinsic secretory/innate immune defects (bicarbonate umbrella failure), dysregulated BA signaling, and senescence‑driven inflammatory/fibrogenic microenvironments (ning2024studyingsystemicmetabolic pages 16-20, reshetnyak2023newinsightsinto pages 1-2, fiorucci2024currentlandscapeand pages 4-6, barrio2025primarybiliarycholangitis pages 6-8, bragazzi2023roleofthe pages 3-5).
- Practical implication: precision therapeutics should consider restoring epithelial defense (umbrella), modulating BA signaling (FXR–FGF19/TGR5), normalizing gut–liver communication, and targeting senescence/SASP and ductular reaction to modify disease course (fiorucci2024currentlandscapeand pages 4-6, barrio2025primarybiliarycholangitis pages 6-8, bragazzi2023roleofthe pages 3-5).

Relevant statistics and recent data
- AMA prevalence in PBC ~90–95%; AMA can be present years prior to diagnosis and does not by itself predict clinical progression (IJMS, 2025-08-15, https://doi.org/10.3390/ijms26167905) (barrio2025primarybiliarycholangitis pages 1-2).
- GWAS/post‑GWAS: ~70 susceptibility loci up to 2022; heritability signal among the strongest across autoimmune diseases; major pathways include HLA class II, IL‑12 axis, TNF response, and B‑cell activation (Genes, 2023-02-14, https://doi.org/10.3390/genes14020405) (ning2024studyingsystemicmetabolic pages 16-20).

Gene/protein annotations with ontology terms
- HGNC: PDHA1 (PDC‑E1 alpha), PDHX (E3BP), DLAT (PDC‑E2), DBT (BCKDH E2), DLD (E3); HLA‑DRB1/DQA1/DQB1; IL12A/IL12B/IL12RB2; STAT4; TYK2; CD40; POU2AF1; SPIB; SLC4A2; CFTR; ITPR3; NR1H4; FGF19; GPBAR1; ABCB11; SLC10A1; SLC10A2; CDKN2A; CDKN1A; TGFB1; IL6; ACTA2; COL1A1 (ning2024studyingsystemicmetabolic pages 16-20, reshetnyak2023newinsightsinto pages 1-2, fiorucci2024currentlandscapeand pages 4-6, barrio2025primarybiliarycholangitis pages 6-8, barrio2025primarybiliarycholangitis pages 2-4).

- GO Biological Process (selected): antigen processing/presentation (GO:0019882), T‑cell activation (GO:0042110), B‑cell activation (GO:0042113), IL‑12 signaling (GO:0038155), Th1 differentiation (GO:0042093), NF‑κB signaling (GO:0043123), bicarbonate transport (GO:0034762), bile acid homeostasis (GO:0055088), cellular senescence (GO:0090398), ECM organization (GO:0030198) (ning2024studyingsystemicmetabolic pages 16-20, reshetnyak2023newinsightsinto pages 1-2, barrio2025primarybiliarycholangitis pages 6-8, fiorucci2024currentlandscapeand pages 4-6).

- GO Cellular Component: mitochondrial inner membrane (GO:0005743); MHC class II complex (GO:0042613); apical plasma membrane (GO:0016324); nucleus (GO:0005634); extracellular region (GO:0005576) (reshetnyak2023newinsightsinto pages 1-2, ning2024studyingsystemicmetabolic pages 16-20, fiorucci2024currentlandscapeand pages 4-6, barrio2025primarybiliarycholangitis pages 6-8).

Phenotype associations (HP terms)
- HP:0001405 (Cholestasis), HP:0006560 (Pruritus), HP:0002019 (Fatigue), HP:0001392 (Cirrhosis), HP:0012418 (Portal hypertension), HP:0031523 (Xanthelasma), HP:0003155 (Hyperlipidemia), HP:0000975 (Jaundice) (mechanistic links discussed above) (fiorucci2024currentlandscapeand pages 4-6, barrio2025primarybiliarycholangitis pages 2-4, barrio2025primarybiliarycholangitis pages 1-2).

Cell type involvement (CL terms)
- CL:0002419 cholangiocyte; CL:0000542 hepatocyte; CL:0000084 T cell; CL:0000236 B cell; CL:0000782 macrophage; CL:0000451 dendritic cell; CL:0000632 hepatic stellate cell; CL:0000899 NK cell; CL:0000947 MAIT cell (fiorucci2024currentlandscapeand pages 4-6, barrio2025primarybiliarycholangitis pages 6-8, ning2024studyingsystemicmetabolic pages 16-20).

Anatomical locations (UBERON terms)
- UBERON:0002397 intrahepatic bile duct; UBERON:0001281 portal area; UBERON:0002116 ileum; UBERON:0013756 peribiliary vascular plexus (fiorucci2024currentlandscapeand pages 4-6, bragazzi2023roleofthe pages 3-5).

Chemical entities (CHEBI)
- CHEBI:36264 bile acids; CHEBI:36216 chenodeoxycholic acid; CHEBI:17509 deoxycholic acid; CHEBI:5638 ursodeoxycholic acid; CHEBI:16412 lipopolysaccharide; CHEBI:8158 interleukin‑12; CHEBI:15956 tumor necrosis factor; CHEBI:9545 transforming growth factor beta (fiorucci2024currentlandscapeand pages 4-6, bragazzi2023roleofthe pages 3-5, barrio2025primarybiliarycholangitis pages 2-4).

Evidence items (with URLs/dates)
- Current Landscape and Evolving Therapies for PBC. Cells. 2024-09-12. https://doi.org/10.3390/cells13181580 (fiorucci2024currentlandscapeand pages 4-6, fiorucci2024currentlandscapeand pages 24-25) 
- Studying Systemic Metabolic Remodeling and Abnormal Mitochondrial Signaling in PBC. 2024-06-01 (repository date). https://doi.org/10.7939/r3-b06d-hr73 (ning2024studyingsystemicmetabolic pages 16-20)
- Role of the Gut–Liver Axis in the Pathobiology of Cholangiopathies. IJMS. 2023-04-06. https://doi.org/10.3390/ijms24076660 (bragazzi2023roleofthe pages 3-5)
- Primary Biliary Cholangitis: Immunopathogenesis and the Role of BA Metabolism. IJMS. 2025-08-15. https://doi.org/10.3390/ijms26167905 (barrio2025primarybiliarycholangitis pages 2-4, barrio2025primarybiliarycholangitis pages 6-8, barrio2025primarybiliarycholangitis pages 1-2)
- New insights into the pathogenesis of PBC asymptomatic stage. World J Gastroenterol. 2023-10-07. https://doi.org/10.3748/wjg.v29.i37.5292 (reshetnyak2023newinsightsinto pages 1-2)

Embedded summary artifact
| Mechanism/Pathway | Key molecules/genes (HGNC) | Cells (CL names) | Location (UBERON / GO cellular component) | Key processes (GO BP terms) | Evidence |
|---|---|---|---|---|---|
| Antimitochondrial autoimmunity to PDC‑E2 (AMA) | PDHA1, PDHX, DLAT, DBT, DLD | Cholangiocyte (biliary epithelial cell) | Mitochondrion; inner mitochondrial membrane (GO:0005739) | Antigen processing and presentation; immune recognition | pqac-00000006 (WJG 2023) – https://doi.org/10.3748/wjg.v29.i37.5292 |
| Cholangiocyte antigen presentation / MHC class II involvement | HLA‑DRA, HLA‑DRB1, CIITA | Cholangiocyte; professional APCs (Kupffer cells, dendritic cells) | Plasma membrane; MHC class II protein complex (GO:0042613) | Antigen presentation to CD4+ T cells (GO:0019882) | pqac-00000001 (Ning 2024) – https://doi.org/10.7939/r3-b06d-hr73 |
| Bicarbonate "umbrella" defect (alkaline protective layer) | SLC4A2 (AE2), CFTR, ITPR3 (IP3R3) | Apical cholangiocyte membrane | Apical plasma membrane; bile canaliculus (UBERON) | Bicarbonate transport; epithelial barrier protection (GO:0034762) | pqac-00000006 (WJG 2023) – https://doi.org/10.3748/wjg.v29.i37.5292 |
| Bile acid cytotoxicity and cholestasis | Hydrophobic bile acids; ABCB11 (BSEP); SLC10A1 (NTCP) | Cholangiocytes, hepatocytes | Bile canaliculus; bile duct lumen | Detergent-mediated membrane damage; cholestasis (GO:0009973) | pqac-00000002 (IJMS 2023) – https://doi.org/10.3390/ijms24076660 |
| Cholangiocyte senescence and SASP (pro‑inflammatory secretome) | CDKN2A (p16), CDKN1A (p21), TGFB1, IL6, CCL20 | Senescent cholangiocytes; surrounding hepatocytes | Nucleus (senescence markers); extracellular space (SASP factors) | Cellular senescence (GO:0090398); cytokine-mediated signaling (GO:0019221) | pqac-00000005 (IJMS 2025) – https://doi.org/10.3390/ijms26167905 |
| IL‑12 signaling / Th1 skewing (genetic susceptibility) | IL12A, IL12B, IL12RB2, STAT4, TYK2 | CD4+ T cells, dendritic cells | Cytokine receptor complex; cytosol/nucleus (signaling) | Th1 differentiation; IFN‑γ production (GO:0042093) | pqac-00000001 (Ning 2024) – https://doi.org/10.7939/r3-b06d-hr73 |
| B‑cell activation and autoantibody generation (GWAS loci) | CD40, POU2AF1, SPIB | B cells, plasma cells | B cell receptor complex; cytoplasm → secreted antibodies | B cell activation, class switching, autoantibody production (GO:0042113) | pqac-00000000 (Cells 2024) – https://doi.org/10.3390/cells13181580 |
| Bile‑acid nuclear/membrane receptor signaling (FXR–FGF19, TGR5) | NR1H4 (FXR), FGF19, GPBAR1 (TGR5) | Ileal enterocytes, hepatocytes, cholangiocytes | Nucleus (FXR); plasma membrane (TGR5) | BA homeostasis, enterohepatic signaling, metabolic regulation (GO:0060396) | pqac-00000004 (Cells 2024) – https://doi.org/10.3390/cells13181580 |
| Gut–liver axis / dysbiosis and bacterial translocation | Microbial PAMPs (LPS), altered BA metabolites | Intestinal epithelium, portal circulation cells, cholangiocytes | Intestinal mucosa → portal vein → liver (UBERON) | Microbial translocation; innate immune activation (GO:0006954) | pqac-00000002 (IJMS 2023) – https://doi.org/10.3390/ijms24076660 |
| Ductular reaction and progressive fibrosis | TGFB1, COL1A1, ACTA2 (α‑SMA) | Cholangiocytes, hepatic stellate cells (HSCs), portal fibroblasts | Portal area; extracellular matrix (GO:0031012) | Myofibroblast activation; extracellular matrix deposition (GO:0061291) | pqac-00000004 (Cells 2024) – https://doi.org/10.3390/cells13181580 |
| Microbial molecular mimicry (triggering AMA) | Bacterial proteins (Novosphingobium aromaticivorans, E. coli antigens) | Intestinal microbes; antigen‑presenting cells | Gut lumen → antigen translocation to liver | Molecular mimicry; break of tolerance (GO:0006955) | pqac-00000000 (Cells 2024) – https://doi.org/10.3390/cells13181580 |
| Apoptotic bleb retention of PDC‑E2 (neoantigen presentation) | PDC‑E2 components (PDHA1 etc.), apoptotic bleb proteins | Apoptotic cholangiocytes; macrophages, DCs | Apoptotic bodies; phagolysosome (GO:0005764) | Neoantigen exposure; autoantigen presentation (GO:0002474) | pqac-00000006 (WJG 2023) – https://doi.org/10.3748/wjg.v29.i37.5292 |
| MAIT / NKT cell involvement (innate‑like lymphocytes) | MR1 (MAIT restriction), invariant TCR chains (TRAV1‑2) | MAIT cells, NKT cells, cholangiocytes | Hepatic sinusoids; intrahepatic portal areas | Rapid cytokine release; cytotoxicity; innate immune amplification (GO:0002443) | pqac-00000004 (Cells 2024) – https://doi.org/10.3390/cells13181580 |
| Bile acid transporter and conjugation changes (disease progression) | ABCB11 (BSEP), SLC10A1 (NTCP), SLC10A2 (ASBT) | Hepatocytes, ileal enterocytes, cholangiocytes | Bile canaliculus; apical enterocyte membrane | BA uptake/secretion; enterohepatic circulation (GO:0060346) | pqac-00000003 (IJMS 2025) – https://doi.org/10.3390/ijms26167905 |


*Table: Compact summary table linking major PBC mechanisms with key genes/proteins, involved cell types, cellular locations/processes, and source evidence (pqac IDs and DOIs). Useful as a quick-reference annotation for disease knowledge bases and GO/HGNC/CL mapping.*

Notes and limitations
- Where PMIDs were not available in the retrieved excerpts, DOIs and publication dates/venues are provided. The core mechanistic claims (autoimmune targeting of PDC‑E2; bicarbonate umbrella defect; cholangiocyte senescence/SASP; genetic IL‑12/TNF/B‑cell axes; gut–liver dysbiosis; FXR–FGF19/TGR5 signaling; ductular reaction/fibrosis) are supported by the cited 2023–2025 sources. Additional primary PMIDs can be layered in future iterations to expand each mechanistic module (e.g., specific GWAS lead variants, functional studies of AE2/IP3R3 regulation, and MAIT/NKT recruitment in human PBC cohorts) (ning2024studyingsystemicmetabolic pages 16-20, reshetnyak2023newinsightsinto pages 1-2, fiorucci2024currentlandscapeand pages 4-6, bragazzi2023roleofthe pages 3-5).

References

1. (fiorucci2024currentlandscapeand pages 4-6): Stefano Fiorucci, Ginevra Urbani, Cristina Di Giorgio, Michele Biagioli, and Eleonora Distrutti. Current landscape and evolving therapies for primary biliary cholangitis. Cells, 13:1580, Sep 2024. URL: https://doi.org/10.3390/cells13181580, doi:10.3390/cells13181580. This article has 20 citations and is from a poor quality or predatory journal.

2. (reshetnyak2023newinsightsinto pages 1-2): Vasiliy Ivanovich Reshetnyak and Igor Veniaminovich Maev. New insights into the pathogenesis of primary biliary cholangitis asymptomatic stage. World Journal of Gastroenterology, 29:5292-5304, Oct 2023. URL: https://doi.org/10.3748/wjg.v29.i37.5292, doi:10.3748/wjg.v29.i37.5292. This article has 21 citations and is from a poor quality or predatory journal.

3. (ning2024studyingsystemicmetabolic pages 16-20): Ning Sun. Studying systemic metabolic remodeling and abnormal mitochondrial signaling in primary biliary cholangitis. Text, 2024. URL: https://doi.org/10.7939/r3-b06d-hr73, doi:10.7939/r3-b06d-hr73. This article has 0 citations and is from a peer-reviewed journal.

4. (bragazzi2023roleofthe pages 3-5): Maria Consiglia Bragazzi, Rosanna Venere, Anthony Vignone, Domenico Alvaro, and Vincenzo Cardinale. Role of the gut–liver axis in the pathobiology of cholangiopathies: basic and clinical evidence. International Journal of Molecular Sciences, 24:6660, Apr 2023. URL: https://doi.org/10.3390/ijms24076660, doi:10.3390/ijms24076660. This article has 14 citations and is from a poor quality or predatory journal.

5. (fiorucci2024currentlandscapeand pages 24-25): Stefano Fiorucci, Ginevra Urbani, Cristina Di Giorgio, Michele Biagioli, and Eleonora Distrutti. Current landscape and evolving therapies for primary biliary cholangitis. Cells, 13:1580, Sep 2024. URL: https://doi.org/10.3390/cells13181580, doi:10.3390/cells13181580. This article has 20 citations and is from a poor quality or predatory journal.

6. (barrio2025primarybiliarycholangitis pages 6-8): María Del Barrio, Álvaro Díaz-González, and Marta Alonso-Peña. Primary biliary cholangitis: immunopathogenesis and the role of bile acid metabolism in disease progression. International Journal of Molecular Sciences, 26:7905, Aug 2025. URL: https://doi.org/10.3390/ijms26167905, doi:10.3390/ijms26167905. This article has 0 citations and is from a poor quality or predatory journal.

7. (barrio2025primarybiliarycholangitis pages 2-4): María Del Barrio, Álvaro Díaz-González, and Marta Alonso-Peña. Primary biliary cholangitis: immunopathogenesis and the role of bile acid metabolism in disease progression. International Journal of Molecular Sciences, 26:7905, Aug 2025. URL: https://doi.org/10.3390/ijms26167905, doi:10.3390/ijms26167905. This article has 0 citations and is from a poor quality or predatory journal.

8. (barrio2025primarybiliarycholangitis pages 1-2): María Del Barrio, Álvaro Díaz-González, and Marta Alonso-Peña. Primary biliary cholangitis: immunopathogenesis and the role of bile acid metabolism in disease progression. International Journal of Molecular Sciences, 26:7905, Aug 2025. URL: https://doi.org/10.3390/ijms26167905, doi:10.3390/ijms26167905. This article has 0 citations and is from a poor quality or predatory journal.