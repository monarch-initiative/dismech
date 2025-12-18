---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T18:30:11.413370'
end_time: '2025-12-17T18:36:57.870770'
duration_seconds: 406.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Coronary Artery Disease
  mondo_id: ''
  category: Complex
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
- **Disease Name:** Coronary Artery Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Coronary Artery Disease**.
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
- **Disease Name:** Coronary Artery Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Coronary Artery Disease**.
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
- Disease Name: Coronary Artery Disease (CAD)
- MONDO ID: MONDO:0004975
- Category: Complex

Pathophysiology description (current understanding, 2023–2024 focus)
Coronary artery disease arises from a chronic, maladaptive response of the arterial wall to cholesterol-rich apolipoprotein B lipoproteins and disturbed hemodynamic forces, culminating in inflammatory atherosclerotic plaque formation, fibroatheroma progression, calcification, and thrombotic complications. Endothelial glycocalyx loss and mechanotransduction alterations at low/disturbed shear sites initiate endothelial dysfunction, with flow-responsive programs (KLF2/eNOS) and mechanosensors (Piezo1; YAP/TAZ) governing endothelial metabolic and barrier states; disturbed flow promotes endothelial senescence and EndMT and primes the intima for leukocyte recruitment (adhesion molecule upregulation, NF-κB activation) (liu2025singlecellrnaseqanalysis pages 17-18). Single-cell analyses integrating mouse disturbed-flow models with human carotid plaques identified CD36+ senescent endothelial states, VEGFA+ macrophage expansion driving immature, leaky neovessels, and downregulation of SMC contractile genes (ACTA2/MYH11) with acquisition of fibroblast-like and osteogenic features, mechanistically linking hemodynamics to inflammation and calcification (Jul 2025; Scientific Reports) (liu2025singlecellrnaseqanalysis pages 15-16, liu2025singlecellrnaseqanalysis pages 17-18).

Atherogenic lipoproteins (LDL, remnants, and Lipoprotein(a), Lp(a)) enter, are retained, and become oxidatively modified within the intima, triggering endothelial activation and monocyte recruitment (e.g., MCP-1), macrophage differentiation and foam-cell formation via scavenger receptors, and amplification of local inflammation. The PCSK9–LDLR axis regulates LDL clearance and influences plaque lipid burden; Lp(a) contributes oxidized phospholipids and antifibrinolytic effects that foster plaque inflammation and calcification (Oct 2024; Journal of Clinical Medicine) (mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16).

Adaptive and innate immunity orchestrate lesion biology. Single-cell gene-regulatory network (GRN) mapping in advanced human plaques highlights proinflammatory macrophage states and Trem2-high lipid-associated macrophages, as well as osteogenic SMC programs. A smooth muscle cell network (GRN39) with key drivers FRZB and ALCAM promotes the transition from contractile to osteogenic phenotypes and associates with CAD heritability and symptomatic disease severity (May 2024; Circulation Research) (mocci2024singlecellgeneregulatorynetworks pages 1-2). Endothelial-to-mesenchymal transition (EndMT) clusters co-expressing EC and SMC markers show strong enrichment for CAD genetic risk and pro-inflammatory programs in single-cell omics meta-analyses (May 2025; Cells) (cetin2025understandingatheroscleroticplaque pages 2-3, cetin2025understandingatheroscleroticplaque pages 13-14).

Inflammasome signaling (NLRP3→IL‑1β/IL‑18) and cytokine networks (e.g., IL‑6, TNF family) couple lipid toxicity to leukocyte activation, SMC phenotypic switching, and calcification; VSMC osteochondrogenic reprogramming involves BMP/Wnt/Notch pathways and RUNX2, and is potentiated by hypoxia/HIF‑1α signaling in plaque microenvironments (Oct 2024; Journal of Clinical Medicine) (mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16). Plaque neovascularization from adventitial vasa vasorum produces fragile microvessels; intraplaque hemorrhage seeds additional lipid and iron, exacerbating inflammation and instability. Single-cell work identifies VEGFA+ macrophages as local angiogenic drivers and links immature neovessels to instability (liu2025singlecellrnaseqanalysis pages 15-16, liu2025singlecellrnaseqanalysis pages 17-18).

At the thrombotic interface, neutrophil extracellular traps (NETs) engage von Willebrand factor (VWF) and platelets to propagate immunothrombosis at rupture/erosion sites, bridging inflammation and occlusive thrombosis that causes myocardial infarction (MI). These processes are emphasized by integrative reviews and single-cell-informed analyses of plaque immunobiology (cetin2025understandingatheroscleroticplaque pages 2-3, mocci2024singlecellgeneregulatorynetworks pages 1-2).

Perivascular crosstalk adds further complexity: pericoronary epicardial adipose tissue (EAT) exhibits disease-associated subpopulations and an altered adipokine secretome; single-nucleus profiling in CAD implicates ANXA1 and SEMA3B as candidate adipokines modulating vascular inflammation and remodeling (Sep 2024 preprint; bioRxiv; May 2025; Cells) (traeuble2025integratedsinglecellatlas pages 30-34, cetin2025understandingatheroscleroticplaque pages 2-3).

Key recent multi-omic insights include: (1) large single-cell datasets of advanced plaques linking GRNs to CAD severity (16,588 cells profiled; three macrophage and three SMC clusters in symptomatic disease) (May 2024; Circulation Research) (mocci2024singlecellgeneregulatorynetworks pages 1-2); (2) disturbed-flow single-cell integration with human plaques identifying endothelial senescence, VEGFA+ macrophages, fibroblast osteogenic shifts, and SMC phenotypic switching (liu2025singlecellrnaseqanalysis pages 15-16, liu2025singlecellrnaseqanalysis pages 17-18); and (3) meta-analyses implicating EndMT ECs and SMC fibromyocytes/osteogenic states in CAD heritability (cetin2025understandingatheroscleroticplaque pages 2-3, cetin2025understandingatheroscleroticplaque pages 13-14).

Embedded summary table of entities and mechanisms
| Category | Entity (HGNC/CHEBI/CL/UBERON where applicable) | Role / Mechanism | Evidence highlights (quote or paraphrase) | Source (URL, date) |
|---|---|---|---|---|
| Endothelial glycocalyx / mechanotransduction | Glycocalyx / eNOS (NOS3) / KLF2 / Piezo1 | Shear-stress sensing → KLF2/eNOS protective program; Piezo1 and mechanotransduction alter endothelial metabolism and barrier; glycocalyx loss → endothelial activation | Flow-responsive KLF2 represses glycolysis and protects ECs; Piezo1 activation boosts mitochondrial respiration/glycolysis; glycocalyx and EC barrier changes central to disease (single-cell & mechanotransduction data) (liu2025singlecellrnaseqanalysis pages 17-18, cetin2025understandingatheroscleroticplaque pages 2-3) | https://doi.org/10.1038/s41598-025-07395-7 (Jul 2025); https://doi.org/10.3390/cells14110770 (May 2025) |
| Lipid handling and atherogenic lipoproteins | LDL (APOB), oxLDL / LDLR / PCSK9 (PCSK9) / LPA (Lipoprotein(a)) / SORT1 | Retention/oxidation of apoB particles → endothelial activation and monocyte recruitment; PCSK9/LDLR axis controls LDL clearance; Lp(a) carries oxidized phospholipids and is prothrombotic | LDL and small apoB particles drive initiation; PCSK9 and LDLR modulation affect plaque composition; Lp(a) linked to coronary calcification and ASCVD risk (mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16, cetin2025understandingatheroscleroticplaque pages 13-14) | https://doi.org/10.3390/jcm13216352 (Oct 2024); https://doi.org/10.1161/circresaha.123.323184 (May 2024); https://doi.org/10.3390/cells14110770 (May 2025) |
| Macrophage states & T cells | Macrophage subsets (TREM2-high LAMs; M1-like), plaque T cells (various CL phenotypes) | Heterogeneous macrophage programs: lipid-laden TREM2-high/foam-cell vs proinflammatory M1; T cells show effector/exhausted phenotypes and local antigen responses | Single-cell GRNs identify Trem2-high lipid-associated macrophages and M1 clusters enriched in symptomatic plaques; plaque T cells display effector memory/exhaustion signatures (mocci2024singlecellgeneregulatorynetworks pages 1-2, cetin2025understandingatheroscleroticplaque pages 2-3) | https://doi.org/10.1161/circresaha.123.323184 (May 2024); https://doi.org/10.3390/cells14110770 (May 2025) |
| NLRP3 inflammasome & innate cytokines | NLRP3 / IL1B / IL18 | Inflammasome activation → IL-1β/IL-18 release, driving local inflammation, VSMC and macrophage responses; therapeutic target for residual inflammatory risk | Inflammatory cascades including IL-1β/NF-κB promote plaque inflammation and link to calcification and progression (inflammation-to-plaque pathway summarized in reviews) (mitsis2024fromcellsto pages 15-16, mocci2024singlecellgeneregulatorynetworks pages 1-2) | https://doi.org/10.3390/jcm13216352 (Oct 2024); https://doi.org/10.1161/circresaha.123.323184 (May 2024) |
| SMC phenotypic switching & GRN39 | SMC markers: ACTA2 / MYH11; GRN39 key drivers: FRZB, ALCAM; osteogenic regulator RUNX2 | Contractile → synthetic / fibromyocyte / osteogenic transitions; GRN39 drives osteogenic SMC program that promotes symptomatic atherosclerosis | Single-cell GRN integration identified GRN39 as critical for contractile-to-osteogenic SMC transition; FRZB and ALCAM validated as key drivers (mocci2024singlecellgeneregulatorynetworks pages 1-2, liu2025singlecellrnaseqanalysis pages 15-16) | https://doi.org/10.1161/circresaha.123.323184 (May 2024); https://doi.org/10.1038/s41598-025-07395-7 (Jul 2025) |
| Calcification signaling | BMPs / WNT / Notch / RUNX2 / HIF1A | Inflammation + lipid stress + VSMC osteochondrogenic transdifferentiation → micro- and macro-calcification via BMP/Wnt/Notch pathways and hypoxia/HIF‑1α signaling | VSMC osteogenic programs (BMP2, RUNX2) and Notch/Wnt signaling drive intimal/medial calcification; systemic cytokines (IL‑6/IL‑18) amplify calcific reprogramming (mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16) | https://doi.org/10.3390/jcm13216352 (Oct 2024) |
| NETs, VWF and platelets (thromboinflammation) | Neutrophil extracellular traps (NETs) / VWF / platelets | NETs interact with VWF and platelets to amplify thromboinflammation at plaque rupture sites → occlusive thrombosis | NETs promote platelet adhesion and local coagulation, linking inflammation to thrombosis and acute coronary events (immune–thrombotic axis highlighted in plaque reviews) (cetin2025understandingatheroscleroticplaque pages 2-3, mocci2024singlecellgeneregulatorynetworks pages 1-2) | https://doi.org/10.3390/cells14110770 (May 2025); https://doi.org/10.1161/circresaha.123.323184 (May 2024) |
| Disturbed flow biomechanics | Flow sensors: KLF2 / YAP/TAZ / Piezo1 (endothelial mechanosensors) | Low/disturbed shear stress → EC phenotypic change, EndMT, local inflammation and SMC phenotypic switching; promotes lesion localization | Disturbed flow downregulates contractile SMC genes and induces EC senescence/EndMT; YAP/TAZ and KLF2 mediate metabolic and transcriptional responses to flow (liu2025singlecellrnaseqanalysis pages 15-16, liu2025singlecellrnaseqanalysis pages 17-18) | https://doi.org/10.1038/s41598-025-07395-7 (Jul 2025) |
| Pericoronary epicardial adipose tissue (EAT) | Adipokines: ANXA1, SEMA3B (adipokine candidates) / EAT depot (UBERON: epicardial adipose) | Perivascular EAT secretes adipokines that modulate local inflammation, angiogenesis and plaque biology; dysregulated secretome in CAD | Single-nucleus atlas identifies ANXA1 and SEMA3B as dysregulated EAT adipokines with altered secretome in CAD, implicating EAT–coronary crosstalk (single-nucleus and single-cell resources) (traeuble2025integratedsinglecellatlas pages 30-34, cetin2025understandingatheroscleroticplaque pages 2-3) | https://doi.org/10.1101/2024.09.11.612431 (preprint Sep 2024); https://doi.org/10.3390/cells14110770 (May 2025) |
| Clonal hematopoiesis (CHIP) | Driver genes: TET2, DNMT3A, JAK2 | Somatic hematopoietic mutations → proinflammatory myeloid phenotypes that accelerate atherosclerosis and augment thromboinflammatory risk | CHIP (TET2/DNMT3A/JAK2) linked to increased CAD events; mutant myeloid cells show proinflammatory signatures that exacerbate plaque inflammation (cited in single-cell / translational reviews) (traeuble2025integratedsinglecellatlas pages 30-34, mocci2024singlecellgeneregulatorynetworks pages 1-2) | https://doi.org/10.1101/2024.09.11.612431 (preprint Sep 2024); https://doi.org/10.1161/circresaha.123.323184 (May 2024) |
| Neovascularization / intraplaque hemorrhage | VEGFA (macrophage source) / immature microvessels | Plaque angiogenesis → fragile neovessels, intraplaque hemorrhage, erythrocyte lipid deposition and accelerated progression/instability | VEGFA+ macrophage expansion and immature/leaky intraplaque microvessels associate with inflammation, hemorrhage and plaque instability (liu2025singlecellrnaseqanalysis pages 15-16, liu2025singlecellrnaseqanalysis pages 17-18) | https://doi.org/10.1038/s41598-025-07395-7 (Jul 2025) |


*Table: A concise table summarizing core molecular players, cell types, mechanisms and 2023–2024 single‑cell/multi‑omic evidence for coronary artery disease pathophysiology; sources cite integrated single‑cell and review datasets (liu2025singlecellrnaseqanalysis pages 15-16, mocci2024singlecellgeneregulatorynetworks pages 1-2).*

Required Information
1) Core Pathophysiology
- Primary mechanisms:
  - Endothelial dysfunction at low/disturbed shear sites due to glycocalyx injury, altered mechanotransduction (KLF2/eNOS program suppression; Piezo1, YAP/TAZ), increased permeability/adhesion molecule expression, and EndMT (liu2025singlecellrnaseqanalysis pages 17-18, cetin2025understandingatheroscleroticplaque pages 13-14).
  - Intimal retention and oxidation of LDL and Lp(a), activation of innate immunity, and foam-cell formation via scavenger receptors; PCSK9–LDLR axis elevates circulating LDL and influences plaque lipid content (mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16).
  - Chronic inflammation orchestrated by macrophage and T cell subsets; NLRP3 inflammasome → IL‑1β/IL‑18; cytokine and chemokine networks drive leukocyte influx and SMC remodeling (mitsis2024fromcellsto pages 15-16, mocci2024singlecellgeneregulatorynetworks pages 1-2).
  - SMC phenotypic switching from contractile (ACTA2/MYH11) to synthetic/fibromyocyte and osteogenic states, under transcriptional control of a disease GRN (GRN39; FRZB, ALCAM) and pathways (Wnt/BMP/Notch/RUNX2) (mocci2024singlecellgeneregulatorynetworks pages 1-2, mitsis2024fromcellsto pages 3-5).
  - Plaque angiogenesis (VEGFA+ macrophages) and immature neovessels → intraplaque hemorrhage; hypoxia and HIF‑1α promote inflammatory and calcific remodeling (liu2025singlecellrnaseqanalysis pages 15-16, liu2025singlecellrnaseqanalysis pages 17-18, mitsis2024fromcellsto pages 3-5).
  - Thromboinflammation at disruption: NETs–VWF–platelet interactions drive occlusive thrombosis (cetin2025understandingatheroscleroticplaque pages 2-3, mocci2024singlecellgeneregulatorynetworks pages 1-2).

- Dysregulated pathways:
  - Mechanotransduction: KLF2/eNOS (NO signaling), Piezo1, YAP/TAZ; NF‑κB activation under disturbed flow (liu2025singlecellrnaseqanalysis pages 17-18, cetin2025understandingatheroscleroticplaque pages 13-14).
  - Lipid handling: LDLR–PCSK9 axis; foam-cell programs; Lp(a)-associated oxidized phospholipids (mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16).
  - Inflammation: NLRP3–IL‑1β/IL‑18; TREM2-high lipid-associated macrophages; chemokine axes (mocci2024singlecellgeneregulatorynetworks pages 1-2, mitsis2024fromcellsto pages 15-16).
  - Calcification: BMP2/SMAD, Wnt/β‑catenin, Notch/RBP-J, RUNX2; hypoxia/HIF‑1α (mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16).

- Affected cellular processes:
  - Endothelial barrier integrity, leukocyte adhesion/transendothelial migration, EndMT; macrophage lipid uptake and polarization; SMC migration/proliferation and osteogenic transdifferentiation; extracellular matrix remodeling; thrombosis/netosis (liu2025singlecellrnaseqanalysis pages 17-18, mocci2024singlecellgeneregulatorynetworks pages 1-2, mitsis2024fromcellsto pages 3-5, cetin2025understandingatheroscleroticplaque pages 2-3).

2) Key Molecular Players
- Genes/Proteins (HGNC):
  - NOS3 (eNOS), KLF2, PIEZO1, YAP1/WWTR1 (YAP/TAZ), VCAM1/ICAM1 (endothelial activation) (liu2025singlecellrnaseqanalysis pages 17-18, cetin2025understandingatheroscleroticplaque pages 13-14).
  - LDLR, PCSK9, APOB (LDL), LPA (Lp(a)), SORT1 (lipid sorting), TREM2 (lipid-associated macrophages) (mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16, mocci2024singlecellgeneregulatorynetworks pages 1-2).
  - NLRP3, IL1B, IL18, TNF, IL6 (inflammasome/cytokines) (mitsis2024fromcellsto pages 15-16).
  - SMC program: ACTA2, MYH11, TAGLN; GRN39 drivers FRZB, ALCAM; osteogenic RUNX2; pathway mediators BMP2, CTNNB1 (Wnt), NOTCH receptors (mocci2024singlecellgeneregulatorynetworks pages 1-2, mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16).
  - VEGFA (angiogenesis), HIF1A (hypoxia), VWF (thromboinflammation), PAD4 (NETosis effector by analogy in linked reviews) (liu2025singlecellrnaseqanalysis pages 15-16, liu2025singlecellrnaseqanalysis pages 17-18, cetin2025understandingatheroscleroticplaque pages 2-3).

- Chemical entities (CHEBI):
  - Nitric oxide (NO), oxidized LDL (oxLDL), oxidized phospholipids on Lp(a), reactive oxygen species (ROS) (mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16).

- Cell types (CL):
  - Endothelial cells (ECs; EndMT clusters), vascular smooth muscle cells (VSMCs; contractile/synthetic/osteogenic/fibromyocytes), macrophage subtypes (TREM2-high lipid-associated, M1-like inflammatory), T cells (effector/exhausted), neutrophils (NETosis), adventitial fibroblasts, adipocytes/macrophages in pericoronary EAT (mocci2024singlecellgeneregulatorynetworks pages 1-2, cetin2025understandingatheroscleroticplaque pages 13-14, liu2025singlecellrnaseqanalysis pages 15-16, cetin2025understandingatheroscleroticplaque pages 2-3).

- Anatomical locations (UBERON):
  - Coronary artery intima, media, adventitia; vasa vasorum; epicardial adipose tissue surrounding coronary arteries (pericoronary EAT) (traeuble2025integratedsinglecellatlas pages 30-34, liu2025singlecellrnaseqanalysis pages 15-16).

3) Biological Processes for GO annotation (examples with disrupted processes)
- Response to shear stress and regulation of endothelial cell proliferation and barrier function (GO:0007155 cell adhesion; GO:0008360 regulation of cell shape; GO:0071732 cellular response to nitric oxide) (liu2025singlecellrnaseqanalysis pages 17-18, cetin2025understandingatheroscleroticplaque pages 13-14).
- Lipid transport, uptake, and oxidation (GO:0030301 cholesterol transport; GO:0042157 lipoprotein metabolic process) (mitsis2024fromcellsto pages 3-5).
- Inflammatory response and inflammasome complex assembly (GO:0006954; GO:0061702) (mitsis2024fromcellsto pages 15-16).
- Macrophage activation and foam-cell differentiation (GO:0042116; GO:0097398) (mocci2024singlecellgeneregulatorynetworks pages 1-2).
- Smooth muscle cell differentiation and osteoblast differentiation programs (GO:0051145; GO:0001649 osteoblast differentiation; GO:0030198 extracellular matrix organization) (mocci2024singlecellgeneregulatorynetworks pages 1-2, mitsis2024fromcellsto pages 3-5).
- Angiogenesis and response to hypoxia (GO:0001525; GO:0001666) (liu2025singlecellrnaseqanalysis pages 15-16, liu2025singlecellrnaseqanalysis pages 17-18).
- Blood coagulation and neutrophil extracellular trap formation (GO:0007596; GO:0036338) (cetin2025understandingatheroscleroticplaque pages 2-3).

4) Cellular Components (where key processes occur)
- Endothelial glycocalyx and luminal plasma membrane (NOS3/eNOS localization), intercellular junctions (adherens/tight junctions), subendothelial extracellular matrix; foam-cell lipid droplets; SMC cytoskeleton (contractile apparatus) and nucleus (osteogenic transcriptional reprogramming); extracellular vesicles and matrix vesicles in calcification; NETs in the extracellular space; microvessel endothelium (intraplaque neovessels) (liu2025singlecellrnaseqanalysis pages 17-18, mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16, cetin2025understandingatheroscleroticplaque pages 2-3).

5) Disease Progression (sequence of events)
- Initiation: Disturbed flow + glycocalyx injury and endothelial dysfunction at branch points → increased permeability, adhesion molecule expression; subendothelial retention of LDL/Lp(a), oxidative modification; monocyte recruitment and differentiation into macrophages (liu2025singlecellrnaseqanalysis pages 17-18, mitsis2024fromcellsto pages 3-5).
- Early lesion: Foam-cell formation (macrophage and SMC-derived), chemokine/cytokine amplification; EC EndMT and SMC migration/proliferation modulate intimal thickening (cetin2025understandingatheroscleroticplaque pages 13-14, mitsis2024fromcellsto pages 3-5).
- Progression: SMC phenotypic switching to fibromyocytes and osteogenic states (GRN39), extracellular matrix remodeling, necrotic core growth, microcalcification; neovascularization with immature, leaky microvessels and intraplaque hemorrhage; hypoxia/HIF‑1α signaling (mocci2024singlecellgeneregulatorynetworks pages 1-2, liu2025singlecellrnaseqanalysis pages 15-16, liu2025singlecellrnaseqanalysis pages 17-18, mitsis2024fromcellsto pages 3-5).
- Complications: Fibrous cap thinning via proteases, microcalcification-induced stress, plaque rupture/erosion; thromboinflammation (NETs–VWF–platelets) leading to coronary thrombosis and MI (cetin2025understandingatheroscleroticplaque pages 2-3, mitsis2024fromcellsto pages 3-5).

6) Phenotypic Manifestations (clinical phenotypes and mechanistic links)
- Stable angina (fixed stenoses due to fibrocalcific plaques with SMC/ECM predominance) vs acute coronary syndromes (ACS) from rupture/erosion and thrombosis, often with lipid-rich necrotic cores, neovascularization, and inflammatory macrophage abundance (mitsis2024fromcellsto pages 3-5, mocci2024singlecellgeneregulatorynetworks pages 1-2).
- Coronary artery calcification (CAC) as a surrogate of atherosclerotic burden; microcalcification associates with instability; osteogenic SMC programs (RUNX2, BMP/Wnt/Notch) mechanistically link inflammation to calcification (mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16).
- Coronary microvascular dysfunction (EndMT/endothelial dysfunction, impaired NO bioavailability) contributing to ischemia even without obstructive CAD (cetin2025understandingatheroscleroticplaque pages 13-14).

Expert opinions and latest research (2023–2024 emphasis)
- Single-cell GRN integration across human plaques provides mechanistic, cell-type–resolved networks connecting SMC osteogenic transitions (GRN39; FRZB/ALCAM) and Trem2-high lipid-associated macrophages to CAD severity and heritability, highlighting actionable nodes in SMC plasticity and macrophage lipid handling (Circulation Research, May 2024; URL: https://doi.org/10.1161/circresaha.123.323184) (mocci2024singlecellgeneregulatorynetworks pages 1-2).
- Integrated disturbed-flow single-cell datasets identify flow-governed endothelial phenotypes (CD36+ senescence, YAP/TAZ–KLF2 axes), VEGFA+ macrophage-driven angiogenesis, fibroblast osteogenic shifts, and SMC de-differentiation, tying biomechanics to inflammatory and calcific remodeling (Scientific Reports, Jul 2025; URL: https://doi.org/10.1038/s41598-025-07395-7) (liu2025singlecellrnaseqanalysis pages 15-16, liu2025singlecellrnaseqanalysis pages 17-18).
- Reviews emphasize the lipid–inflammation–calcification triad, detailing LDL/Lp(a) biology, NLRP3/IL‑1β pathways, and SMC osteogenic reprogramming via BMP/Wnt/Notch and RUNX2; these mechanistic threads explain both plaque burden and propensity for destabilization (Journal of Clinical Medicine, Oct 2024; URLs: https://doi.org/10.3390/jcm13216352) (mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16).
- Single-cell meta-analyses underscore EndMT enrichment in plaques and link EndMT ECs to CAD genetic risk, suggesting EndMT as a disease-relevant, trackable state for precision targeting (Cells, May 2025; https://doi.org/10.3390/cells14110770) (cetin2025understandingatheroscleroticplaque pages 2-3, cetin2025understandingatheroscleroticplaque pages 13-14).

Relevant statistics and data
- Advanced symptomatic atherosclerosis single-cell dataset: 16,588 cells (SmartSeq2, ~8,000 genes/cell) from mouse and human plaques, identifying 3 SMC and 3 macrophage subtype clusters enriched in symptomatic lesions; 3 arterial-wall GRNs (GRN33 macrophage; GRN39 SMC; GRN122 macrophage) linked to CAD heritability and severity scores (Circulation Research, 2024) (mocci2024singlecellgeneregulatorynetworks pages 1-2).
- Disturbed-flow single-cell integration: identification of CD36+ EC senescence, VEGFA+ macrophage expansion, metabolic reprogramming in fibroblasts, and SMC switching; predicts crosstalk that promotes instability and calcification (Scientific Reports, 2025) (liu2025singlecellrnaseqanalysis pages 15-16, liu2025singlecellrnaseqanalysis pages 17-18).

Gene/protein annotations with ontology terms (selected examples)
- Endothelium: NOS3 (HGNC:7876) – nitric-oxide biosynthetic process (GO:0006809); KLF2 (HGNC:6346) – regulation of endothelial function under shear stress (process-level; mechanotransduction) (liu2025singlecellrnaseqanalysis pages 17-18, cetin2025understandingatheroscleroticplaque pages 13-14).
- Lipids: LDLR (HGNC:6547) – lipoprotein receptor activity (GO:0030228); PCSK9 (HGNC:20001) – regulation of LDLR catabolic process (GO:0032802); LPA (HGNC:6667) – oxidized phospholipid transport (process-level) (mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16).
- Immunity: NLRP3 (HGNC:16400) – inflammasome complex assembly (GO:0061702); TREM2 (HGNC:17761) – positive regulation of lipid catabolic process (GO:0050995) in lipid-associated macrophages (mocci2024singlecellgeneregulatorynetworks pages 1-2, mitsis2024fromcellsto pages 15-16).
- SMC reprogramming: ACTA2 (HGNC:130), MYH11 (HGNC:7585), TAGLN (HGNC:11573) – contractile apparatus; RUNX2 (HGNC:10471) – osteoblast differentiation (GO:0001649); FRZB (HGNC:3979), ALCAM (HGNC:404) – GRN39 key drivers (mocci2024singlecellgeneregulatorynetworks pages 1-2, mitsis2024fromcellsto pages 3-5).
- Angiogenesis/hypoxia: VEGFA (HGNC:12680) – angiogenesis (GO:0001525); HIF1A (HGNC:4910) – cellular response to hypoxia (GO:0071456) (liu2025singlecellrnaseqanalysis pages 15-16, liu2025singlecellrnaseqanalysis pages 17-18).
- Thromboinflammation: VWF (HGNC:12726) – platelet adhesion (GO:0030168); NETs (complex extracellular DNA-protein structures) – neutrophil extracellular trap formation (GO:0036338) (cetin2025understandingatheroscleroticplaque pages 2-3).

Phenotype associations (HPO terms; selected)
- Coronary artery calcification (HP:0031623) – correlates with plaque burden and SMC osteogenic programs (mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16).
- Myocardial infarction (HP:0001658) – consequence of thromboinflammation at plaque disruption (NETs–VWF–platelets) (cetin2025understandingatheroscleroticplaque pages 2-3).
- Angina pectoris (HP:0001681) – ischemia from obstructive fibrocalcific lesions and/or microvascular dysfunction (mitsis2024fromcellsto pages 3-5, cetin2025understandingatheroscleroticplaque pages 13-14).

Cell type involvement (CL terms; selected)
- CL:0000115 endothelial cell – EndMT subsets; CL:0000192 vascular smooth muscle cell – contractile/synthetic/osteogenic states; CL:0000235 macrophage – TREM2-high lipid-associated, M1-like; CL:0000775 T cell – effector/exhausted; CL:0000771 neutrophil – NETosis (mocci2024singlecellgeneregulatorynetworks pages 1-2, cetin2025understandingatheroscleroticplaque pages 2-3, liu2025singlecellrnaseqanalysis pages 15-16).

Anatomical locations (UBERON; selected)
- UBERON:0002049 coronary artery; UBERON:0002416 tunica intima; UBERON:0002415 tunica media; UBERON:0001634 adventitia; UBERON:0003688 vasa vasorum; UBERON:0014147 epicardial fat (pericoronary EAT) (traeuble2025integratedsinglecellatlas pages 30-34, liu2025singlecellrnaseqanalysis pages 15-16).

Chemical entities (CHEBI; selected)
- CHEBI:16480 nitric oxide; CHEBI:47774 oxidized LDL (class); CHEBI:26523 reactive oxygen species (mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16).

Evidence items (with PMIDs/URLs/dates)
- Mocci G, et al. Single-Cell Gene-Regulatory Networks of Advanced Symptomatic Atherosclerosis. Circulation Research. 2024-05; URL: https://doi.org/10.1161/circresaha.123.323184 (mocci2024singlecellgeneregulatorynetworks pages 1-2).
- Liu X, et al. Single-cell RNA-seq analysis of mouse carotid artery under disturbed flow and human carotid plaques identifies key cell populations in atherosclerosis development. Scientific Reports. 2025-07; URL: https://doi.org/10.1038/s41598-025-07395-7 (liu2025singlecellrnaseqanalysis pages 15-16, liu2025singlecellrnaseqanalysis pages 17-18).
- Mitsis A, et al. From Cells to Plaques: The Molecular Pathways of Coronary Artery Calcification and Disease. Journal of Clinical Medicine. 2024-10; URL: https://doi.org/10.3390/jcm13216352 (mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16).
- Cetin E, Raby A-C. Understanding Atherosclerotic Plaque Cellular Composition: Recent Advances Driven by Single Cell Omics. Cells. 2025-05; URL: https://doi.org/10.3390/cells14110770 (cetin2025understandingatheroscleroticplaque pages 2-3, cetin2025understandingatheroscleroticplaque pages 13-14).
- Traeuble K, et al. Integrated single-cell atlas of human atherosclerotic plaques. bioRxiv preprint. 2024-09-11; URL: https://doi.org/10.1101/2024.09.11.612431 (traeuble2025integratedsinglecellatlas pages 30-34).

Clinical and translational implications
- Cell-state GRNs nominate SMC (FRZB/ALCAM) and macrophage nodes as mechanistic targets to modulate plaque composition and stability (mocci2024singlecellgeneregulatorynetworks pages 1-2).
- Disturbed-flow signatures (KLF2/Piezo1/YAP-TAZ) and EC senescence/EndMT are candidate targets for biomechanical niche normalization; VEGFA+ macrophages and immature neovessels suggest anti-angiogenic stabilization strategies (liu2025singlecellrnaseqanalysis pages 17-18, liu2025singlecellrnaseqanalysis pages 15-16).
- Lipid-centric therapies (statins, ezetimibe, PCSK9 modulators) directly reduce LDL exposure; Lp(a)-targeted strategies are justified by mechanistic links to inflammation/calcification (mitsis2024fromcellsto pages 3-5, mitsis2024fromcellsto pages 15-16).
- Anti-inflammatory/interleukin axis interventions (e.g., IL‑1β pathway) address NLRP3-driven residual risk; NETs/VWF/platelet axes indicate anti-thromboinflammatory approaches at disruption (mitsis2024fromcellsto pages 15-16, cetin2025understandingatheroscleroticplaque pages 2-3).

Direct quotes (selected lines supporting key statements)
- “Advanced stages of atherosclerosis progression and symptomatic carotid plaques were largely characterized by… [an] extracellular matrix organization/osteogenic (SMC)… and Trem2-high lipid-associated (macrophage) phenotypes” (Circulation Research, 2024) (mocci2024singlecellgeneregulatorynetworks pages 1-2).
- “CD36+ endothelial cell states and endothelial senescence… expansion of VEGFA+ macrophages… immature/leaky intraplaque microvessels that promote hemorrhage and instability” (Scientific Reports, 2025) (liu2025singlecellrnaseqanalysis pages 15-16).
- “VSMCs… undergo osteogenic transdifferentiation driven by BMPs… RUNX2 and Wnt/Notch/TGF‑β pathways… inflammation and oxidative stress promote VSMC osteogenesis and calcification” (J Clin Med, 2024) (mitsis2024fromcellsto pages 3-5).

Limitations
Some specific quantitative effect sizes (e.g., absolute risk per lipid exposure or Lp(a) thresholds) and randomized clinical outcome data for several mechanistic targets (e.g., EndMT, VEGFA+ macrophage blockade) are not directly contained in these sources. However, the mechanistic synthesis is grounded in recent single-cell and translational literature (2023–2024 emphasis) and high-quality reviews.


References

1. (liu2025singlecellrnaseqanalysis pages 17-18): Xuyang Liu, Xu Li, Xin Wang, Jiawei Zhao, Chen Liu, Shaochi Wang, Zongping Xia, and Yuming Xu. Single-cell rna-seq analysis of mouse carotid artery under disturbed flow and human carotid plaques identifies key cell populations in atherosclerosis development. Scientific Reports, Jul 2025. URL: https://doi.org/10.1038/s41598-025-07395-7, doi:10.1038/s41598-025-07395-7. This article has 1 citations and is from a peer-reviewed journal.

2. (liu2025singlecellrnaseqanalysis pages 15-16): Xuyang Liu, Xu Li, Xin Wang, Jiawei Zhao, Chen Liu, Shaochi Wang, Zongping Xia, and Yuming Xu. Single-cell rna-seq analysis of mouse carotid artery under disturbed flow and human carotid plaques identifies key cell populations in atherosclerosis development. Scientific Reports, Jul 2025. URL: https://doi.org/10.1038/s41598-025-07395-7, doi:10.1038/s41598-025-07395-7. This article has 1 citations and is from a peer-reviewed journal.

3. (mitsis2024fromcellsto pages 3-5): Andreas Mitsis, Elina Khattab, Evi Christodoulou, Kimon Myrianthopoulos, Michael Myrianthefs, Stergios Tzikas, Antonios Ziakas, Nikolaos Fragakis, and George Kassimis. From cells to plaques: the molecular pathways of coronary artery calcification and disease. Journal of Clinical Medicine, 13:6352, Oct 2024. URL: https://doi.org/10.3390/jcm13216352, doi:10.3390/jcm13216352. This article has 7 citations and is from a poor quality or predatory journal.

4. (mitsis2024fromcellsto pages 15-16): Andreas Mitsis, Elina Khattab, Evi Christodoulou, Kimon Myrianthopoulos, Michael Myrianthefs, Stergios Tzikas, Antonios Ziakas, Nikolaos Fragakis, and George Kassimis. From cells to plaques: the molecular pathways of coronary artery calcification and disease. Journal of Clinical Medicine, 13:6352, Oct 2024. URL: https://doi.org/10.3390/jcm13216352, doi:10.3390/jcm13216352. This article has 7 citations and is from a poor quality or predatory journal.

5. (mocci2024singlecellgeneregulatorynetworks pages 1-2): Giuseppe Mocci, Katyayani Sukhavasi, Tiit Örd, Sean Bankier, Prosanta Singha, Uma Thanigai Arasu, Olayinka Oluwasegun Agbabiaje, Petri Mäkinen, Lijiang Ma, Chani J. Hodonsky, Redouane Aherrahrou, Lars Muhl, Jianping Liu, Sonja Gustafsson, Byambajav Byandelger, Ying Wang, Simon Koplev, Urban Lendahl, Gary K. Owens, Nicholas J. Leeper, Gerard Pasterkamp, Michael Vanlandewijck, Tom Michoel, Arno Ruusalepp, Ke Hao, Seppo Ylä-Herttuala, Marika Väli, Heli Järve, Michal Mokry, Mete Civelek, Clint J. Miller, Jason C. Kovacic, Minna U. Kaikkonen, Christer Betsholtz, and Johan L.M. Björkegren. Single-cell gene-regulatory networks of advanced symptomatic atherosclerosis. Circulation Research, 134:1405-1423, May 2024. URL: https://doi.org/10.1161/circresaha.123.323184, doi:10.1161/circresaha.123.323184. This article has 41 citations and is from a highest quality peer-reviewed journal.

6. (cetin2025understandingatheroscleroticplaque pages 2-3): Esra Cetin and Anne-Catherine Raby. Understanding atherosclerotic plaque cellular composition: recent advances driven by single cell omics. Cells, 14:770, May 2025. URL: https://doi.org/10.3390/cells14110770, doi:10.3390/cells14110770. This article has 3 citations and is from a poor quality or predatory journal.

7. (cetin2025understandingatheroscleroticplaque pages 13-14): Esra Cetin and Anne-Catherine Raby. Understanding atherosclerotic plaque cellular composition: recent advances driven by single cell omics. Cells, 14:770, May 2025. URL: https://doi.org/10.3390/cells14110770, doi:10.3390/cells14110770. This article has 3 citations and is from a poor quality or predatory journal.

8. (traeuble2025integratedsinglecellatlas pages 30-34): K. Traeuble, M. Munz, J. Pauli, N. Sachs, E. Vafadarnejad, T. Carrillo-Roa, L. Maegdefessel, P. Kastner, M. Heinig, and Tania Carrillo. Integrated single-cell atlas of human atherosclerotic plaques. bioRxiv, Sep 2025. URL: https://doi.org/10.1101/2024.09.11.612431, doi:10.1101/2024.09.11.612431. This article has 8 citations and is from a poor quality or predatory journal.