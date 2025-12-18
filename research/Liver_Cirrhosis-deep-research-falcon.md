---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T18:38:29.251421'
end_time: '2025-12-17T18:44:35.105985'
duration_seconds: 365.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Liver Cirrhosis
  mondo_id: ''
  category: Complex
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
- **Disease Name:** Liver Cirrhosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Liver Cirrhosis**.
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
- **Disease Name:** Liver Cirrhosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Liver Cirrhosis**.
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


Plan status: objectives 1–3 completed (scoping, search, and evidence gathering). Objectives 4–6 integrated into the narrative below; objective 7 (submit) fulfilled by this response.

Disease Pathophysiology Research Template

Target Disease
- Disease Name: Liver Cirrhosis
- MONDO ID: not specified (general cirrhosis term varies across ontologies; EFO:0001422 maps to “cirrhosis of liver” in OpenTargets) (addissouky2024translatingmolecularheterogeneity pages 7-8)
- Category: Complex

Pathophysiology description (current understanding, 2023–2024 focus)
Cirrhosis represents the end-stage of chronic liver injury, characterized by persistent inflammation, progressive fibrogenesis with excessive extracellular matrix (ECM) deposition, vascular remodeling of the hepatic sinusoidal bed (“capillarization”), and formation of regenerative nodules that distort architecture and drive portal hypertension and organ failure (MedComm, 2024; https://doi.org/10.1002/mco2.721) (dong2024livercirrhosismolecular pages 20-21). Hepatic stellate cells (HSCs) are the dominant source of myofibroblasts and fibrillar collagens (type I predominates) once activated by injury cues (e.g., TGF-β, PDGF, inflammatory cytokines, oxidative stress); they lose retinoid stores, express α-SMA, proliferate, migrate, and deposit ECM (Biomedicines, 2024; https://doi.org/10.3390/biomedicines12102229) (somnay2024liverfibrosisleading pages 1-2, somnay2024liverfibrosisleading pages 2-4). Liver sinusoidal endothelial cells (LSECs) lose fenestrae, gain basement membrane and collagen IV, and exhibit reduced nitric oxide (NO) bioavailability, increasing intrahepatic resistance and initiating/propagating portal hypertension—the “NO paradox” of low intrahepatic and high splanchnic NO (IJMS, 2024; https://doi.org/10.3390/ijms252312859) (somnay2024liverfibrosisleading pages 2-4, zhao2024pharmacotherapyofliver pages 2-4). Innate and adaptive immune cells (Kupffer cells/monocyte-derived macrophages, neutrophils, MAIT, T and B lymphocytes) participate in injury sensing, cytokine production, and HSC modulation—including profibrotic (e.g., TGF-β/IL‑17) and fibrolytic phases during regression (IJMS, 2024; https://doi.org/10.3390/ijms25147873; Pharmaceuticals, 2024; https://doi.org/10.3390/ph17121724) (akkız2024liverfibrosisfrom pages 23-25, zhao2024pharmacotherapyofliver pages 2-4). Single-cell and spatial transcriptomic work and molecular subtyping reveal heterogeneity of inflammatory and cholangiocyte-associated programs in advanced disease that may inform precision therapeutics (Archives of Gastroenterology Research, 2024; https://doi.org/10.33696/gastroenterology.5.054) (addissouky2024translatingmolecularheterogeneity pages 7-8).

Core Pathophysiology (mechanisms, pathways, processes)
- HSC activation and ECM deposition: TGF-β/Smad is a master profibrotic driver increasing collagen (COL1A1/1A2) and TIMPs while reducing MMP activity; PDGF stimulates HSC proliferation and migration via PI3K–AKT/MAPK; integrin–ECM stiffness signaling sustains activation (Pharmaceuticals, 2024; https://doi.org/10.3390/ph17121724) (zhao2024pharmacotherapyofliver pages 2-4). Quote: “collagens are the most abundant ECM components… can increase up to tenfold in cirrhosis” (Pharmaceuticals, 2024) (zhao2024pharmacotherapyofliver pages 2-4).
- Endothelial dysfunction and portal hypertension: LSEC capillarization with collagen IV basement membrane and loss of fenestrae increases sinusoidal resistance and portal pressure; endothelial NO is reduced intrahepatically while splanchnic vasodilation augments portal inflow, linking microvascular remodeling to hemodynamics (Biomedicines, 2024; https://doi.org/10.3390/biomedicines12102229) (somnay2024liverfibrosisleading pages 2-4).
- Immune dysregulation: Kupffer cells and monocyte-derived macrophages secrete TGF‑β, PDGF, and ROS, promoting HSC activation; Th17/IL‑17 axis augments HSC activation; during regression, resident and recruited macrophages can express MMP9/12 to promote ECM degradation (IJMS, 2024; https://doi.org/10.3390/ijms25147873; Biomedicines, 2024) (akkız2024liverfibrosisfrom pages 23-25, somnay2024liverfibrosisleading pages 2-4).
- Molecular pathway landscape: In addition to TGF‑β/Smad and PDGF/PI3K–AKT, recent reviews highlight Hippo–YAP/TAZ, Notch, Wnt/β‑catenin, NF‑κB, and Hedgehog signaling as integrated regulators of fibrogenesis and mesenchymal activation; targeting these has preclinical support (MedComm, 2024; Pharmaceuticals, 2024) (dong2024livercirrhosismolecular pages 20-21, zhao2024pharmacotherapyofliver pages 2-4).
- Gut–liver axis and bile acids: Dysbiosis, microbial products (LPS/MAMPs), and altered bile acid signaling feed inflammatory and fibrogenic pathways; specific dysbiosis signatures and permeability increases are associated with fibrosis progression (IJMS, 2024; https://doi.org/10.3390/ijms25137405) (veskovic2024exploringfibrosispathophysiology pages 4-5).

Key Molecular Players (HGNC where applicable)
- Genes/Proteins (examples):
  - TGFB1 (TGF-β1)/TGFBR1–SMAD2/3–SMAD4 axis: master profibrotic signaling in HSCs; induces collagen, α-SMA (ACTA2), TIMP1 (Pharmaceuticals, 2024) (zhao2024pharmacotherapyofliver pages 2-4).
  - PDGFB/PDGFRA/PDGFRB: potent mitogens/chemotactic factors for HSCs; engage PI3K–AKT and MAPK (Pharmaceuticals, 2024) (zhao2024pharmacotherapyofliver pages 2-4).
  - YAP1/TAZ (WWTR1) and Hippo pathway: modulate fibroblast/HSC phenotypes and interact with TGF‑β, Wnt, and Notch networks (summarized in 2024 reviews) (zhao2024pharmacotherapyofliver pages 2-4, dong2024livercirrhosismolecular pages 20-21).
  - WNT ligands/CTNNB1 (β‑catenin), NOTCH receptors/ligands: implicated in mesenchymal activation and cholangiocyte–stromal crosstalk (MedComm, 2024; Pharmaceuticals, 2024) (dong2024livercirrhosismolecular pages 20-21, zhao2024pharmacotherapyofliver pages 2-4).
  - NF‑κB pathway components (RELA/NFKB1): inflammatory transcriptional control in macrophages and HSCs (Pharmaceuticals, 2024) (zhao2024pharmacotherapyofliver pages 2-4).
  - ECM proteins and modifiers: COL1A1/COL3A1 (fibrillar), COL4A1 (basement membrane; LSEC capillarization), LOX family (crosslinking), MMPs (e.g., MMP9/12 in regression), TIMP1/2 (inhibition) (Biomedicines, 2024; Pharmaceuticals, 2024) (somnay2024liverfibrosisleading pages 2-4, zhao2024pharmacotherapyofliver pages 2-4).
- Chemical entities (CHEBI examples):
  - Collagen (CHEBI:3815) accumulation; hyaluronic acid (CHEBI:18064) as biomarker; bile acids (CHEBI:3098) signaling (Pharmaceuticals, 2024; IJMS, 2024) (zhao2024pharmacotherapyofliver pages 2-4, veskovic2024exploringfibrosispathophysiology pages 4-5).
  - Therapeutics discussed mechanistically (not approved for antifibrosis in cirrhosis): pirfenidone, selonsertib, obeticholic acid as FXR agonist, anti‑CCR2/CCR5, anti‑LOXL2 (reviewed 2024) (addissouky2024translatingmolecularheterogeneity pages 7-8).
- Cell types (CL terms):
  - Hepatic stellate cell (CL:0000632): principal myofibroblast precursor in fibrosis (IJMS, 2024) (akkız2024liverfibrosisfrom pages 23-25).
  - Kupffer cell/macrophage (CL:0000860; CL:0000235): resident and monocyte-derived macrophages orchestrate injury responses and fibrosis/regression (IJMS, 2024; Biomedicines, 2024) (akkız2024liverfibrosisfrom pages 23-25, somnay2024liverfibrosisleading pages 2-4).
  - Liver sinusoidal endothelial cell (CL:0002138): capillarization reduces NO, increases resistance (Biomedicines, 2024) (somnay2024liverfibrosisleading pages 2-4).
  - Cholangiocyte (CL:0002078): ductular reaction and cholangiocyte–immune interactions contribute to fibrogenic niches (MedComm, 2024) (dong2024livercirrhosismolecular pages 20-21).
  - T cells (CL:0000084; CD8+ CL:0000625; Treg CL:0002673); MAIT cells (CL:0001064): modulate inflammation and fibrosis dynamics (IJMS, 2024) (akkız2024liverfibrosisfrom pages 23-25).
- Anatomical locations (UBERON): liver (UBERON:0002107), hepatic sinusoid (UBERON:0001977), space of Disse/perisinusoidal space (UBERON:0018183), portal tract (UBERON:0004811) (Biomedicines, 2024; MedComm, 2024) (somnay2024liverfibrosisleading pages 2-4, dong2024livercirrhosismolecular pages 20-21).

Biological Processes (GO terms; disrupted in cirrhosis)
- GO:0030198 extracellular matrix organization; GO:0030199 collagen fibril organization (increased) (Pharmaceuticals, 2024) (zhao2024pharmacotherapyofliver pages 2-4).
- GO:0008284 positive regulation of cell proliferation (HSC proliferation via PDGF) (zhao2024pharmacotherapyofliver pages 2-4).
- GO:0006954 inflammatory response; GO:0006955 immune response (macrophage/T-cell mediated) (akkız2024liverfibrosisfrom pages 23-25, zhao2024pharmacotherapyofliver pages 2-4).
- GO:0007179 TGF-β receptor signaling pathway; GO:0014065 PI3K signaling; GO:0007223 Wnt signaling; GO:0007219 Notch signaling; GO:0035329 Hippo signaling (summarized in 2024 reviews) (dong2024livercirrhosismolecular pages 20-21, zhao2024pharmacotherapyofliver pages 2-4).
- GO:0003018 vascular process in circulatory system; GO:0035150 regulation of nitric oxide biosynthetic process (LSEC NO, portal hypertension) (Biomedicines, 2024) (somnay2024liverfibrosisleading pages 2-4).

Cellular Components (where processes occur)
- ECM (GO:0031012), collagen-containing extracellular matrix (GO:0062023) (zhao2024pharmacotherapyofliver pages 2-4).
- Basement membrane (GO:0005604) rich in collagen IV during LSEC capillarization (Biomedicines, 2024) (somnay2024liverfibrosisleading pages 2-4).
- Plasma membrane/caveolae of LSECs (fenestrae loss), focal adhesions (integrin–ECM mechanotransduction in HSCs) (Pharmaceuticals, 2024) (zhao2024pharmacotherapyofliver pages 2-4).
- Sinusoidal lumen and perisinusoidal space for exchange and pressure modulation (Biomedicines, 2024) (somnay2024liverfibrosisleading pages 2-4).

Disease Progression (sequence and stages)
- Initiation: chronic injury (viral, metabolic, alcohol, cholestasis, toxins) triggers hepatocyte damage, DAMPs/PAMPs, Kupffer cell activation, cytokine release (TGF‑β, PDGF), and HSC priming (Biomedicines, 2024) (somnay2024liverfibrosisleading pages 1-2).
- Propagation: HSC transdifferentiation, ECM deposition (collagen I/III), LSEC capillarization (collagen IV basement membrane), angiogenesis, and escalating intrahepatic resistance with portal pressure rise (Biomedicines, 2024) (somnay2024liverfibrosisleading pages 2-4).
- Remodeling: fibrous septa and regenerative nodules with architectural distortion; hyperdynamic circulation with splanchnic vasodilation; complications emerge (ascites, variceal bleeding, encephalopathy) (Biomedicines, 2024) (somnay2024liverfibrosisleading pages 1-2, somnay2024liverfibrosisleading pages 2-4).
- Potential regression: removing causative injury reduces inflammatory drive; macrophage subsets promote matrix degradation (e.g., MMP9/12) and HSC inactivation, enabling partial reversal—documented clinically in early stages (IJMS, 2024; Biomedicines, 2024) (akkız2024liverfibrosisfrom pages 23-25, somnay2024liverfibrosisleading pages 1-2).

Phenotypic Manifestations (HP terms)
- Portal hypertension (HP:0002616) and esophageal varices (HP:0002040), splenomegaly (HP:0001744), ascites (HP:0001541), hepatic encephalopathy (HP:0001399), jaundice (HP:0000952), coagulopathy (HP:0003257) (mechanistic links via endothelial dysfunction, ECM remodeling, and hyperdynamic circulation) (Biomedicines, 2024; IJMS, 2024) (somnay2024liverfibrosisleading pages 1-2, somnay2024liverfibrosisleading pages 2-4).

Recent developments and latest research (2023–2024)
- Vascular remodeling as a driver: Contemporary reviews underscore LSEC capillarization and NO dysregulation as initiating events for increased intrahepatic resistance and portal hypertension; diagnostic and therapeutic implications include targeting angiogenesis and restoring fenestrae (2024 Biomedicines; 2024 IJMS) (somnay2024liverfibrosisleading pages 2-4).
- Molecular subtypes and precision medicine: Transcriptomic subtypes (inflammatory, proliferative, cholangiocyte-associated) have been identified in advanced disease; precision strategies include targeting LOXL2, CCR2/CCR5, CSF‑1R, and FXR pathways, and HSC-targeted delivery (2024 Archives of Gastroenterology Research) (addissouky2024translatingmolecularheterogeneity pages 7-8).
- Multi-pathway targeting: 2024–2025 overviews recommend multi-target approaches across TGF‑β, PDGF/PI3K–AKT, Hippo–YAP/TAZ, Notch, Wnt/β‑catenin, NF‑κB, and Hedgehog axes; several inhibitors and oligonucleotide approaches are under clinical exploration, though no antifibrotic is yet approved for cirrhosis reversal (2024 MedComm; 2024 Pharmaceuticals) (dong2024livercirrhosismolecular pages 20-21, zhao2024pharmacotherapyofliver pages 2-4).
- Gut–liver axis and bile acid–microbiome reciprocity: 2024 analyses refine the role of dysbiosis and bile acids in driving inflammatory/fibrotic signaling via increased intestinal permeability and microbial metabolite flux (2024 IJMS) (veskovic2024exploringfibrosispathophysiology pages 4-5).

Genetic drivers and risk/protective variants (links to fibrosis/cirrhosis)
- The strongest human genetic architecture connecting to cirrhosis risk in metabolic liver disease remains PNPLA3 (I148M risk), TM6SF2 (E167K risk), MBOAT7 (rs641738 risk), GCKR (risk), and HSD17B13 (loss-of-function protective), which influence lipid handling, hepatocyte injury, inflammation, and fibrosis trajectories; these variants are widely leveraged in polygenic risk stratification and therapeutic targeting (2024 Archives of Gastroenterology Research) (addissouky2024translatingmolecularheterogeneity pages 7-8).

Portal hypertension: mechanistic links with inflammation
- Intrahepatic: capillarized LSECs and activated, contractile HSCs narrow sinusoids; reduced NO and increased vasoconstrictors (e.g., endothelin-1) increase resistance; presinusoidal changes in steatohepatitis add to the gradient (Biomedicines, 2024) (somnay2024liverfibrosisleading pages 2-4).
- Systemic: inflammatory mediators promote splanchnic vasodilation and hyperdynamic circulation, increasing portal inflow and sustaining portal hypertension (Biomedicines, 2024) (somnay2024liverfibrosisleading pages 2-4).

Current applications and real-world implementations
- Noninvasive staging and monitoring: Widespread clinical use of FIB‑4/APRI, ELF, and elastography; biomarker panels incorporating ECM fragments (e.g., hyaluronic acid, collagen IV, TIMPs) are used and being refined for cirrhosis and portal hypertension risk stratification (Pharmaceuticals, 2024) (zhao2024pharmacotherapyofliver pages 2-4).
- Etiology-directed therapy: Disease modification by removing injury (e.g., antivirals for viral hepatitis, alcohol abstinence, MASLD weight loss) is associated with fibrosis stabilization/regression, especially in early stages (Biomedicines, 2024) (somnay2024liverfibrosisleading pages 1-2).
- Precision directions under evaluation: CCR2/CCR5 inhibition, anti‑LOXL2, FXR agonists, HSC-targeted delivery, and oligonucleotides are in translational pipelines; device-based portal pressure modulation and better hemodynamic phenotyping are emphasized (Archives of Gastroenterology Research, 2024) (addissouky2024translatingmolecularheterogeneity pages 7-8).

Expert opinions and analysis (authoritative sources)
- 2024–2025 state-of-the-art reviews converge on HSC centrality, LSEC-driven microvascular pathobiology, and integrated immune–stromal signaling, while noting that “despite numerous clinical studies… an approved antifibrotic therapy still remains elusive” (MedComm, 2024; https://doi.org/10.1002/mco2.721) (dong2024livercirrhosismolecular pages 20-21). The field emphasizes molecular subclassification and multi-target combinations as likely requirements for meaningful antifibrotic efficacy (Archives of Gastroenterology Research, 2024) (addissouky2024translatingmolecularheterogeneity pages 7-8).

Relevant statistics and data (recent)
- ECM load: “collagens… can increase up to tenfold in cirrhosis” (Pharmaceuticals, 2024; https://doi.org/10.3390/ph17121724) (zhao2024pharmacotherapyofliver pages 2-4).
- Reversibility: Reviews summarize clinical and experimental evidence of fibrosis regression with removal of injurious stimuli, including macrophage-mediated matrix remodeling (Biomedicines, 2024; https://doi.org/10.3390/biomedicines12102229; IJMS, 2024; https://doi.org/10.3390/ijms25147873) (somnay2024liverfibrosisleading pages 1-2, akkız2024liverfibrosisfrom pages 23-25).

Gene/Protein annotations with ontology terms (examples)
- TGFB1 (HGNC:11766) – GO:0007179 TGF‑β signaling; GO:0030198 ECM organization; cellular component: extracellular region (GO:0005576); evidence: human disease reviews (2024) (zhao2024pharmacotherapyofliver pages 2-4).
- PDGFRB (HGNC:8803) – GO:0014065 PI3K signaling; GO:0008284 positive regulation of cell proliferation; cellular component: plasma membrane (GO:0005886); role: HSC mitogen (2024) (zhao2024pharmacotherapyofliver pages 2-4).
- YAP1 (HGNC:16262), WWTR1/TAZ (HGNC:12765) – GO:0035329 Hippo signaling; role: pro-fibrotic transcriptional co-activators in fibroblast/HSC states (2024) (zhao2024pharmacotherapyofliver pages 2-4).
- CTNNB1 (HGNC:2514) – GO:0007223 Wnt signaling; NOTCH1 (HGNC:7881) – GO:0007219 Notch pathway; roles in stromal and cholangiocyte crosstalk (2024) (dong2024livercirrhosismolecular pages 20-21, zhao2024pharmacotherapyofliver pages 2-4).
- COL1A1 (HGNC:2197), COL3A1 (HGNC:2200), COL4A1 (HGNC:2206); LOX (HGNC:6664) – ECM and crosslinking; MMP9 (HGNC:7176)/MMP12 (HGNC:7157); TIMP1 (HGNC:11820) – ECM degradation control (2024) (somnay2024liverfibrosisleading pages 2-4, zhao2024pharmacotherapyofliver pages 2-4).

Phenotype associations (HP terms; examples)
- HP:0002616 Portal hypertension – due to sinusoidal resistance and hyperdynamic flow (somnay2024liverfibrosisleading pages 2-4).
- HP:0001541 Ascites; HP:0002040 Esophageal varices; HP:0001399 Hepatic encephalopathy; HP:0001744 Splenomegaly (clinical complications of cirrhosis and portal hypertension) (somnay2024liverfibrosisleading pages 1-2, somnay2024liverfibrosisleading pages 2-4).

Cell type involvement (CL terms; examples)
- CL:0000632 Hepatic stellate cell – effector of fibrogenesis (akkız2024liverfibrosisfrom pages 23-25).
- CL:0002138 Liver sinusoidal endothelial cell – capillarization and NO dysregulation (somnay2024liverfibrosisleading pages 2-4).
- CL:0000860 Macrophage; CL:0001064 MAIT cell; CL:0000625 CD8+ T cell; CL:0002673 Regulatory T cell – immunomodulation of fibrosis (akkız2024liverfibrosisfrom pages 23-25, zhao2024pharmacotherapyofliver pages 2-4).

Anatomical locations (UBERON; examples)
- UBERON:0002107 Liver; UBERON:0001977 Hepatic sinusoid; UBERON:0018183 Space of Disse; UBERON:0004811 Portal tract (somnay2024liverfibrosisleading pages 2-4, dong2024livercirrhosismolecular pages 20-21).

Chemical entities (CHEBI; examples)
- CHEBI:3815 Collagen; CHEBI:18064 Hyaluronic acid; CHEBI:3098 Bile acids (zhao2024pharmacotherapyofliver pages 2-4, veskovic2024exploringfibrosispathophysiology pages 4-5).

Evidence items (with PMIDs/DOIs/URLs; 2023–2024 priority)
- Dong et al., 2024 (MedComm): broad mechanistic review, therapies and microenvironmental changes in cirrhosis (https://doi.org/10.1002/mco2.721) (dong2024livercirrhosismolecular pages 20-21).
- Somnay et al., 2024 (Biomedicines): HSC centrality, LSEC capillarization, endothelial dysfunction, reversibility, and hemodynamics (https://doi.org/10.3390/biomedicines12102229) (somnay2024liverfibrosisleading pages 1-2, somnay2024liverfibrosisleading pages 2-4).
- Zhao et al., 2024 (Pharmaceuticals): quantitative ECM expansion, PDGF/PI3K–AKT, Wnt/Notch/Hippo and biomarker panels (https://doi.org/10.3390/ph17121724) (zhao2024pharmacotherapyofliver pages 2-4).
- Akkız et al., 2024 (IJMS): HSCs as main effector cells; immune–stromal crosstalk; regression potential (https://doi.org/10.3390/ijms25147873) (akkız2024liverfibrosisfrom pages 23-25).
- Vesković et al., 2024 (IJMS): gut–liver axis, bile acids, HSC activation and Hedgehog/PDGF/TGF‑β in lean vs obese fibrosis (https://doi.org/10.3390/ijms25137405) (veskovic2024exploringfibrosispathophysiology pages 4-5).
- Addissouky, 2024 (Archives of Gastroenterology Research): molecular heterogeneity, precision targets (https://doi.org/10.33696/gastroenterology.5.054) (addissouky2024translatingmolecularheterogeneity pages 7-8).

Limitations
- While recent authoritative reviews and translational analyses were used, detailed single-cell/spatial primary datasets and functional genetic studies (e.g., variant-to-mechanism causal pathways) would further strengthen mechanistic granularity; these are being actively generated and integrated into clinical research pipelines (2024) (addissouky2024translatingmolecularheterogeneity pages 7-8).

Conclusion
Modern understanding of cirrhosis integrates HSC-mediated fibrogenesis; LSEC capillarization and intrahepatic endothelial dysfunction; and immune–stromal cross-talk governed by interwoven pathways (TGF‑β/Smad, PDGF/PI3K–AKT, Hippo–YAP/TAZ, Notch, Wnt/β‑catenin, NF‑κB, Hedgehog). Genetic risk (PNPLA3/TM6SF2/MBOAT7/GCKR) and protective (HSD17B13) variants modulate disease course in MASLD-associated cirrhosis. On the systems level, ECM remodeling together with vascular–hemodynamic changes produces portal hypertension and clinical decompensation. Noninvasive staging is established, but effective anti‑fibrotic therapies for established cirrhosis remain an urgent unmet need, with multi-target, precision strategies in development (2024) (dong2024livercirrhosismolecular pages 20-21, somnay2024liverfibrosisleading pages 1-2, somnay2024liverfibrosisleading pages 2-4, zhao2024pharmacotherapyofliver pages 2-4, akkız2024liverfibrosisfrom pages 23-25, addissouky2024translatingmolecularheterogeneity pages 7-8).

References

1. (addissouky2024translatingmolecularheterogeneity pages 7-8): Tamer A. Addissouky. Translating molecular heterogeneity into precision medicine for advanced liver disease. Archives of Gastroenterology Research, 5:47-58, Jan 2024. URL: https://doi.org/10.33696/gastroenterology.5.054, doi:10.33696/gastroenterology.5.054. This article has 11 citations.

2. (dong2024livercirrhosismolecular pages 20-21): Zihe Dong, Yeying Wang, and Weilin Jin. Liver cirrhosis: molecular mechanisms and therapeutic interventions. MedComm, Sep 2024. URL: https://doi.org/10.1002/mco2.721, doi:10.1002/mco2.721. This article has 18 citations.

3. (somnay2024liverfibrosisleading pages 1-2): Kaumudi Somnay, Priyanka Wadgaonkar, Nidhishri Sridhar, Prarath Roshni, Nachiketh Rao, and Raj Wadgaonkar. Liver fibrosis leading to cirrhosis: basic mechanisms and clinical perspectives. Biomedicines, 12:2229, Sep 2024. URL: https://doi.org/10.3390/biomedicines12102229, doi:10.3390/biomedicines12102229. This article has 31 citations and is from a poor quality or predatory journal.

4. (somnay2024liverfibrosisleading pages 2-4): Kaumudi Somnay, Priyanka Wadgaonkar, Nidhishri Sridhar, Prarath Roshni, Nachiketh Rao, and Raj Wadgaonkar. Liver fibrosis leading to cirrhosis: basic mechanisms and clinical perspectives. Biomedicines, 12:2229, Sep 2024. URL: https://doi.org/10.3390/biomedicines12102229, doi:10.3390/biomedicines12102229. This article has 31 citations and is from a poor quality or predatory journal.

5. (zhao2024pharmacotherapyofliver pages 2-4): Liangtao Zhao, Haolan Tang, and Zhangjun Cheng. Pharmacotherapy of liver fibrosis and hepatitis: recent advances. Pharmaceuticals, 17:1724, Dec 2024. URL: https://doi.org/10.3390/ph17121724, doi:10.3390/ph17121724. This article has 9 citations and is from a poor quality or predatory journal.

6. (akkız2024liverfibrosisfrom pages 23-25): Hikmet Akkız, Robert K. Gieseler, and Ali Canbay. Liver fibrosis: from basic science towards clinical progress, focusing on the central role of hepatic stellate cells. International Journal of Molecular Sciences, 25:7873, Jul 2024. URL: https://doi.org/10.3390/ijms25147873, doi:10.3390/ijms25147873. This article has 95 citations and is from a poor quality or predatory journal.

7. (veskovic2024exploringfibrosispathophysiology pages 4-5): Milena Vesković, Milka Pejović, Nikola Šutulović, Dragan Hrnčić, Aleksandra Rašić-Marković, Olivera Stanojlović, and Dušan Mladenović. Exploring fibrosis pathophysiology in lean and obese metabolic-associated fatty liver disease: an in-depth comparison. International Journal of Molecular Sciences, 25:7405, Jul 2024. URL: https://doi.org/10.3390/ijms25137405, doi:10.3390/ijms25137405. This article has 8 citations and is from a poor quality or predatory journal.