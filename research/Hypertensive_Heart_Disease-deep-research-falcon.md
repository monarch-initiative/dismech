---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:13:24.218179'
end_time: '2025-12-15T09:26:05.581992'
duration_seconds: 761.36
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypertensive Heart Disease
  mondo_id: ''
  category: Cardiovascular
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 52
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Hypertensive Heart Disease
- **MONDO ID:**  (if available)
- **Category:** Cardiovascular

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hypertensive Heart Disease**.
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
- **Disease Name:** Hypertensive Heart Disease
- **MONDO ID:**  (if available)
- **Category:** Cardiovascular

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hypertensive Heart Disease**.
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


# Disease Pathophysiology Research Template

## Target Disease
- Disease Name: Hypertensive Heart Disease (HHD)
- MONDO ID: Not specified
- Category: Cardiovascular

## Pathophysiology description (2023–2024 synthesis)
Hypertensive heart disease is now defined as a spectrum of myocardial and vascular remodeling driven by chronic systemic hypertension, encompassing macro- and microvascular changes, ventricular and atrial remodeling, interstitial and perivascular fibrosis, electrophysiologic alterations, and progression to heart failure phenotypes (HFpEF/HFrEF) and arrhythmias. The field emphasizes that HHD is not synonymous with LV hypertrophy alone; microvascular dysfunction/rarefaction and matrix remodeling are central, and clinical progression is non‑linear. Recent classification proposals integrate vascular features, atrial/ventricular structure–function, biomarkers, and advanced imaging (strain/CMR), rather than relying solely on LVH or EF strata (URL: https://doi.org/10.3390/jcm13020505, Jan 2024; URL: https://doi.org/10.31083/j.rcm2503093, Mar 2024) (nemtsova2024hypertensiveheartdisease pages 1-2, nemtsova2024hypertensiveheartdisease pages 17-19, huang2024hypertensiveheartdisease pages 1-2, nemtsova2024hypertensiveheartdisease pages 15-17, kadoglou2024challengesinechocardiography pages 2-4).

Mechanistically, sustained afterload activates neurohumoral pathways (RAAS/Ang II via AT1R; sympathetic signaling), mechano-transduction (integrin–FAK/MAPK, RhoA/ROCK, YAP/TAZ), oxidative stress (NOX2/NOX4), mitochondrial dysfunction, endothelial dysfunction with coronary microvascular inflammation and rarefaction, and fibroblast activation via TGF‑β/SMAD, culminating in ECM accumulation and stiffness with impaired relaxation and perfusion. Inflammasome signaling (NLRP3→IL‑1β/IL‑18) amplifies inflammation, hypertrophy, and fibrosis in pressure-overload models. These processes are interdependent: reduced NO bioavailability and arterial stiffness increase afterload, while rarefaction and perivascular fibrosis impair coronary flow reserve and oxygen delivery, promoting ischemia and progression to HFpEF/HFrEF (URLs: https://doi.org/10.3390/ijms25126661, Jun 2024; https://doi.org/10.3390/ijms252413294, Dec 2024; https://doi.org/10.3390/antiox14010038, Dec 2024; https://doi.org/10.3390/ijms25105372, May 2024; https://doi.org/10.1038/s41569-023-00946-3, Nov 2024) (gallo2024hypertensionandheart pages 2-4, durante2024systemicandcardiac pages 1-3, zhang2024decipheringoxidativestress pages 7-9, vlachakis2024theroleof pages 2-4, nemtsova2024hypertensiveheartdisease pages 4-5, wang2023endothelialcellmediatedmechanismof pages 1-2, nemtsova2024hypertensiveheartdisease pages 2-4, wrobelnowicka2024theroleof pages 3-5, vlachakis2024theroleof pages 9-11).

Embed: key entities and mechanisms
| Category | Term | Mechanistic role in HHD (concise) | Supporting 2023–2024 sources |
|---|---|---|---|
| Gene/Protein | AGTR1 (Ang II–AT1R) | Mediates Ang II signalling → cardiomyocyte hypertrophy, ROS production and induction of profibrotic mediators (TGF‑β). | (huang2024hypertensiveheartdisease pages 1-2, gallo2024hypertensionandheart pages 2-4) |
| Pathway/Process | TGF‑β / SMAD signaling (GO) | Drives fibroblast→myofibroblast transition and increased Collagen I/III deposition → myocardial stiffening. | (gaydarski2025morphometricandmolecular pages 6-8, gaydarski2025morphometricandmolecular pages 1-2) |
| Gene/Protein | Collagen I / Collagen III, MMP2 | ECM proteins (I/III) increase stiffness; MMP2 mediates ECM turnover and remodelling imbalance. | (gaydarski2025morphometricandmolecular pages 1-2, gaydarski2025morphometricandmolecular pages 5-6) |
| Gene/Protein | NOX2 / NOX4 (NADPH oxidases) | Major enzymatic ROS sources linking mechanical/Ang II stimuli to oxidative stress, endothelial dysfunction and mitochondrial damage. | (zhang2024decipheringoxidativestress pages 7-9, wrobelnowicka2024theroleof pages 3-5) |
| Pathway/Process | NLRP3 inflammasome → IL‑1β (pathway/protein) | Inflammasome activation promotes IL‑1β/IL‑18 release, pyroptosis and inflammation that amplify fibrosis and adverse remodelling. | (vlachakis2024theroleof pages 2-4, zhang2024decipheringoxidativestress pages 7-9) |
| Cell Type (CL) | Cardiac fibroblast (CL) | Principal ECM-producing cell; activation → myofibroblast, proliferative and profibrotic states revealed by single‑cell atlases. | (patrick2024integrationmappingof pages 1-2, huang2024hypertensiveheartdisease pages 17-18) |
| Cell Type (CL) | Cardiomyocyte (CL) | Hypertrophy, impaired energetics and Ca2+ handling; source and target of ROS/inflammatory signalling in HHD. | (gallo2024hypertensionandheart pages 2-4, wrobelnowicka2024theroleof pages 3-5) |
| Cell Type (CL) | Endothelial cell (CL) | Endothelial dysfunction reduces NO, impairs angiogenesis and promotes microvascular dysfunction/rarefaction. | (durante2024systemicandcardiac pages 1-3, wang2023endothelialcellmediatedmechanismof pages 1-2) |
| Cell Type (CL) | Pericyte (CL) | Pericyte loss/dysfunction contributes to capillary rarefaction and impaired microvascular stability in HHD. | (nemtsova2024hypertensiveheartdisease pages 4-5) |
| Anatomical (UBERON) | Left ventricle myocardium (UBERON) | Primary site of concentric hypertrophy, interstitial/perivascular fibrosis and contractile reserve loss. | (huang2024hypertensiveheartdisease pages 1-2) |
| Anatomical (UBERON) | Coronary microvasculature (UBERON) | Microvascular dysfunction and rarefaction reduce coronary flow reserve → ischemia, promoting fibrosis and HFpEF phenotype. | (durante2024systemicandcardiac pages 1-3, wang2023endothelialcellmediatedmechanismof pages 1-2) |
| Pathway/Process | Extracellular matrix organization (GO) | Dysregulated ECM synthesis/degradation (↑collagen, altered TIMP/MMP balance) → increased myocardial stiffness. | (gaydarski2025morphometricandmolecular pages 1-2, patrick2024integrationmappingof pages 1-2) |
| Pathway/Process | Oxidative stress response (GO) | ROS-mediated signalling damages mitochondria, oxidizes RyR/Ca2+ handling proteins and activates pro‑fibrotic/inflammatory transcription (NF‑κB). | (zhang2024decipheringoxidativestress pages 7-9, wrobelnowicka2024theroleof pages 3-5) |
| Pathway/Process | Endothelial activation & angiogenesis (GO) | Impaired VEGF/NO signalling → maladaptive angiogenesis or rarefaction, worsening oxygen delivery to hypertrophied myocardium. | (durante2024systemicandcardiac pages 1-3, gaydarski2025morphometricandmolecular pages 5-6) |
| Pathway/Process | Mitochondrial organization / respiration (GO) | Mitochondrial dysfunction → reduced ATP, increased ROS, impaired energetic reserve and progression toward HF. | (zhang2024decipheringoxidativestress pages 7-9, huang2024hypertensiveheartdisease pages 1-2) |
| Pathway/Process | Mechanotransduction / focal adhesion signaling (FAK, YAP/TAZ, RhoA/ROCK) | Pressure overload/mechanical stretch activates integrin‑FAK/MAPK/YAP pathways in fibroblasts and myocytes → hypertrophy & fibrosis. | (gaydarski2025morphometricandmolecular pages 6-8, huang2024hypertensiveheartdisease pages 17-18) |
| Chemical / Drug | SGLT2 inhibitors (empagliflozin, dapagliflozin) | Demonstrated LV‑mass reduction and anti‑fibrotic effects in trials/preclinical models; act via AMPK, reduced oxidative stress and anti‑inflammation. | (huang2024hypertensiveheartdisease pages 1-2, rolski2025cardiacfibrosismechanistic pages 4-6) |
| Chemical / Drug | ACEI / ARB / MRA (drug classes) | RAAS blockade reduces Ang II/MR-driven hypertrophy, oxidative stress and fibrosis; cornerstone therapy to prevent HHD progression. | (huang2024hypertensiveheartdisease pages 1-2, gaydarski2025morphometricandmolecular pages 5-6) |


*Table: Compact knowledge‑base table mapping key genes/pathways, cell types, anatomical sites and drugs to their mechanistic roles in hypertensive heart disease, with supporting 2023–2024 source IDs for rapid reference.*

## 1. Core Pathophysiology
- Primary mechanisms: chronic pressure overload and neurohumoral activation (RAAS/Ang II→AT1R) induce cardiomyocyte hypertrophy and fibroblast activation; oxidative stress via NADPH oxidases and mitochondrial dysfunction propagates redox-sensitive signaling (NF‑κB, CaMKII), calcium mishandling, and energetic failure; endothelial dysfunction and coronary microvascular remodeling (decreased NO, increased ROS, increased stiffness) culminate in impaired coronary flow reserve and microvascular rarefaction; inflammasome activation (NLRP3/caspase‑1) promotes IL‑1β/IL‑18 release, pyroptosis, and fibrosis; mechano-signaling (integrin–FAK/MAPK, RhoA/ROCK, YAP/TAZ) drives hypertrophy and matrix deposition under sustained wall stress (URLs: https://doi.org/10.3390/ijms25126661; https://doi.org/10.3390/antiox14010038; https://doi.org/10.3390/medicina60050760) (gallo2024hypertensionandheart pages 2-4, zhang2024decipheringoxidativestress pages 7-9, wrobelnowicka2024theroleof pages 3-5).
- Dysregulated pathways: RAAS–TGF‑β/SMAD axis, oxidative stress (NOX2/NOX4), mitochondrial respiratory impairment, endothelial NO signaling, inflammasome/IL‑1 family, mechano-transduction cascades (URLs: https://doi.org/10.3390/ph17030267, Feb 2024; https://doi.org/10.1126/sciadv.adk8501, Jun 2024) (gaydarski2025morphometricandmolecular pages 6-8, patrick2024integrationmappingof pages 1-2).
- Affected cellular processes: fibroblast–myofibroblast transition and ECM synthesis; cardiomyocyte hypertrophic growth and Ca2+ dysregulation; endothelial activation and reduced angiogenesis; pericyte dysfunction; extracellular matrix organization/crosslinking; mitochondrial bioenergetics decline and ROS production; inflammasome-mediated pyroptosis (URLs: https://doi.org/10.1007/s10741-022-10224-y, Mar 2023; https://doi.org/10.3390/ijms25105372, May 2024) (wang2023endothelialcellmediatedmechanismof pages 1-2, vlachakis2024theroleof pages 2-4).

## 2. Key Molecular Players
- Genes/Proteins (HGNC): AGTR1 (AT1R): Ang II receptor mediating hypertrophy signaling; TGF‑β/SMAD2/3: profibrotic transcriptional program; COL1A1/COL3A1 (Collagen I/III) and MMP2: ECM remodeling; NOX2 (CYBB) and NOX4: ROS sources; NLRP3, CASP1, IL1B: inflammasome/IL‑1β; CaMKII, NF‑κB: redox-driven signaling (URLs: https://doi.org/10.31083/j.rcm2503093; https://doi.org/10.3390/ijms25126661; https://doi.org/10.3390/antiox14010038) (huang2024hypertensiveheartdisease pages 1-2, gallo2024hypertensionandheart pages 2-4, zhang2024decipheringoxidativestress pages 7-9, wrobelnowicka2024theroleof pages 3-5, vlachakis2024theroleof pages 2-4).
- Chemical entities (CHEBI/Drugs): Angiotensin II; SGLT2 inhibitors (empagliflozin, dapagliflozin) with anti-fibrotic, LV mass–reducing signals; ACE inhibitors, ARBs, MRAs (RAAS blockade). Emerging anti-fibrotic strategies target TGF‑β axis and integrin activation (URLs: https://doi.org/10.3390/ph17030267; https://doi.org/10.3390/ph18030313) (gaydarski2025morphometricandmolecular pages 6-8, rolski2025cardiacfibrosismechanistic pages 4-6, huang2024hypertensiveheartdisease pages 1-2).
- Cell types (CL): Cardiac fibroblasts/myofibroblasts (activation programs mapped by single-cell integration), cardiomyocytes, endothelial cells, pericytes, macrophages (immune crosstalk) (URLs: https://doi.org/10.1126/sciadv.adk8501; https://doi.org/10.1007/s10741-022-10224-y) (patrick2024integrationmappingof pages 1-2, wang2023endothelialcellmediatedmechanismof pages 1-2).
- Anatomical locations (UBERON): Left ventricular myocardium; coronary microvasculature; perivascular space/matrix (URLs: https://doi.org/10.3390/jcm13020505; https://doi.org/10.31083/j.rcm2503093) (nemtsova2024hypertensiveheartdisease pages 1-2, huang2024hypertensiveheartdisease pages 1-2).

## 3. Biological Processes (GO annotation)
- Extracellular matrix organization; collagen fibril organization; fibroblast proliferation/differentiation (TGF‑β/SMAD) (gaydarski2025morphometricandmolecular pages 6-8, gaydarski2025morphometricandmolecular pages 1-2).
- Response to oxidative stress; superoxide metabolic process (NOX2/NOX4), mitochondrial electron transport/respiration (zhang2024decipheringoxidativestress pages 7-9, wrobelnowicka2024theroleof pages 3-5).
- Endothelial cell activation; angiogenesis; regulation of nitric oxide biosynthetic process; coronary microvascular function (durante2024systemicandcardiac pages 1-3, wang2023endothelialcellmediatedmechanismof pages 1-2, nemtsova2024hypertensiveheartdisease pages 2-4).
- Mechanotransduction; focal adhesion assembly; RhoA/ROCK and YAP/TAZ signaling in fibroblasts/myocytes (gaydarski2025morphometricandmolecular pages 6-8).
- Inflammasome complex assembly; interleukin‑1β production; pyroptosis (vlachakis2024theroleof pages 2-4).

## 4. Cellular Components
- Key locales: extracellular matrix and perivascular space (fibrosis); sarcolemma/ T‑tubules and sarcoplasmic reticulum (Ca2+ handling); mitochondria (ROS, bioenergetics); endothelial glycocalyx and intercellular junctions (barrier function); inflammasome complex (cytosolic) (wrobelnowicka2024theroleof pages 3-5, zhang2024decipheringoxidativestress pages 7-9, vlachakis2024theroleof pages 2-4).

## 5. Disease Progression
- Sequence of events: Chronic BP elevation → neurohumoral activation (RAAS/SNS) and mechano-stress → cardiomyocyte hypertrophy and metabolic/mitochondrial stress → endothelial dysfunction, increased arterial stiffness, and coronary microvascular inflammation → functional then structural rarefaction and reduced CFR → subendocardial ischemia with perivascular/interstitial fibrosis (TGF‑β/SMAD, ECM accumulation) → diastolic dysfunction and HFpEF; with ongoing injury, transition to chamber dilatation and HFrEF; atrial remodeling predisposes to AF (URLs: https://doi.org/10.3390/ijms25126661; https://doi.org/10.3390/jcm13092708; https://doi.org/10.3390/jcm13020505) (gallo2024hypertensionandheart pages 2-4, kadoglou2024challengesinechocardiography pages 2-4, nemtsova2024hypertensiveheartdisease pages 1-2, nemtsova2024hypertensiveheartdisease pages 2-4).
- Distinct stages: Early diastolic dysfunction ± LVH; concentric remodeling with diffuse interstitial fibrosis and preserved EF; clinical HFpEF with CMD; late systolic failure with LV dilation in a subset (URLs: https://doi.org/10.31083/j.rcm2503093) (huang2024hypertensiveheartdisease pages 1-2).

## 6. Phenotypic Manifestations
- Clinical phenotypes: Concentric LVH with diastolic dysfunction (HFpEF) and microvascular angina; progression to HFrEF in some; atrial enlargement/fibrosis leading to AF; subclinical troponin elevation, increased LAVI, increased arterial stiffness (URLs: https://doi.org/10.3390/jcm13092708; https://doi.org/10.3390/jcm13020505) (kadoglou2024challengesinechocardiography pages 2-4, nemtsova2024hypertensiveheartdisease pages 17-19).
- Microvascular phenotype: Reduced CFR/MRR and rarefaction in HTN/HFpEF without epicardial stenosis; perivascular fibrosis increases oxygen diffusion distance and impairs supply–demand matching (URLs: https://doi.org/10.3390/ijms252413294; https://doi.org/10.3390/jcm13020505) (durante2024systemicandcardiac pages 1-3, nemtsova2024hypertensiveheartdisease pages 4-5, nemtsova2024hypertensiveheartdisease pages 2-4).

## Expert opinions and analysis
- Updated HHD definition and matrix classification emphasize heterogeneity and the need for integrated biomarker–imaging strategies; natriuretic peptides remain most validated but multi-marker panels and advanced echo/CMR (GLS, ECV) are advocated for earlier detection and staging (URL: https://doi.org/10.3390/jcm13020505, Jan 2024) (nemtsova2024hypertensiveheartdisease pages 15-17, nemtsova2024hypertensiveheartdisease pages 1-2, nemtsova2024hypertensiveheartdisease pages 17-19).
- Mechanistic consensus: RAAS–TGF‑β/SMAD, oxidative stress (NOX2/NOX4), endothelial dysfunction with CMD/rarefaction, and inflammasome signaling converge to drive hypertensive remodeling; mitochondrial dysfunction integrates metabolic stress and ROS production in both myocardium and endothelium (URLs: https://doi.org/10.3390/ijms25126661; https://doi.org/10.3390/antiox14010038) (gallo2024hypertensionandheart pages 2-4, zhang2024decipheringoxidativestress pages 7-9, durante2024systemicandcardiac pages 1-3).
- Direct quotes (illustrative): “Hypertension causes microvascular remodeling and rarefaction… contributing to end‑organ damage” (Durante et al., Dec 2024; URL above) (durante2024systemicandcardiac pages 1-3). “Inflammasome activation… promotes fibrosis and impaired neovascularization in pressure‑overload models” (Vlachakis et al., May 2024; URL above) (vlachakis2024theroleof pages 2-4).

## Current applications and real-world implementations
- Guideline-directed RAAS blockade (ACEI/ARB/MRA) and BP control reduce progression of LVH/fibrosis and improve outcomes in hypertensive remodeling (gallo2024hypertensionandheart pages 2-4).
- Imaging applications: Speckle-tracking GLS/pressure–strain loops for early dysfunction; CMR ECV mapping for diffuse fibrosis; CFR/MRR by PET or invasive measures to document CMD in HTN/HFpEF (kadoglou2024challengesinechocardiography pages 2-4, nemtsova2024hypertensiveheartdisease pages 4-5).
- Pharmacologic developments: SGLT2 inhibitors show reductions in LV mass and fibrosis markers in cardiometabolic cohorts, with anti-inflammatory/anti-fibrotic mechanisms (AMPK, reduced TGF‑β/SMAD) being actively investigated (URL: https://doi.org/10.3390/ph18030313, Feb 2025; note mechanistic translational context) (rolski2025cardiacfibrosismechanistic pages 4-6, huang2024hypertensiveheartdisease pages 1-2).

## Relevant statistics and data (recent)
- LVH affects >20% of hypertensive individuals; HFpEF prevalence and incidence are rising relative to HFrEF, with CMD/rarefaction implicated mechanistically (URLs: https://doi.org/10.31083/j.rcm2503093; https://doi.org/10.1007/s10741-022-10224-y) (huang2024hypertensiveheartdisease pages 1-2, wang2023endothelialcellmediatedmechanismof pages 1-2).
- Evidence of CMD in hypertension: reduced CFR/MRR documented in HTN/HFpEF even without epicardial disease; microvascular rarefaction correlates with hypertrophy severity and adverse outcomes (URLs: https://doi.org/10.3390/jcm13020505; https://doi.org/10.3390/ijms252413294) (nemtsova2024hypertensiveheartdisease pages 2-4, durante2024systemicandcardiac pages 1-3).

## Structured ontology annotations
- Genes/Proteins (HGNC): AGTR1; TGFB1/SMAD2/3; COL1A1/COL3A1; MMP2; CYBB (NOX2); NOX4; NLRP3; CASP1; IL1B; CAMK2D; NFKB1 (huang2024hypertensiveheartdisease pages 1-2, gaydarski2025morphometricandmolecular pages 6-8, gaydarski2025morphometricandmolecular pages 1-2, wrobelnowicka2024theroleof pages 3-5, vlachakis2024theroleof pages 2-4).
- GO Biological Processes: extracellular matrix organization; collagen fibril organization; response to oxidative stress; mitochondrial electron transport; angiogenesis; endothelial cell activation; regulation of nitric oxide biosynthetic process; inflammasome complex assembly; interleukin‑1β production; mechanotransduction/focal adhesion (gaydarski2025morphometricandmolecular pages 6-8, zhang2024decipheringoxidativestress pages 7-9, durante2024systemicandcardiac pages 1-3, vlachakis2024theroleof pages 2-4).
- Cell Types (CL): cardiac fibroblast; myofibroblast; cardiomyocyte; endothelial cell; pericyte; macrophage (patrick2024integrationmappingof pages 1-2, wang2023endothelialcellmediatedmechanismof pages 1-2, nemtsova2024hypertensiveheartdisease pages 4-5).
- Anatomical Locations (UBERON): left ventricular myocardium; coronary microvasculature; perivascular connective tissue (nemtsova2024hypertensiveheartdisease pages 1-2, nemtsova2024hypertensiveheartdisease pages 2-4).
- Chemical Entities (CHEBI/Drugs): Angiotensin II; empagliflozin; dapagliflozin; ACE inhibitors; ARBs; MRAs (huang2024hypertensiveheartdisease pages 1-2, rolski2025cardiacfibrosismechanistic pages 4-6).
- Phenotypes (HP terms): Left ventricular hypertrophy; diastolic dysfunction; reduced coronary flow reserve; microvascular angina; atrial fibrillation (kadoglou2024challengesinechocardiography pages 2-4, nemtsova2024hypertensiveheartdisease pages 4-5, wang2023endothelialcellmediatedmechanismof pages 1-2).

## Evidence items with URLs and publication dates
- Nemtsova et al., Jan 2024, Journal of Clinical Medicine. Updated HHD definition, vascular–matrix focus, classification matrix. URL: https://doi.org/10.3390/jcm13020505 (nemtsova2024hypertensiveheartdisease pages 1-2, nemtsova2024hypertensiveheartdisease pages 17-19, nemtsova2024hypertensiveheartdisease pages 2-4).
- Huang et al., Mar 2024, Reviews in Cardiovascular Medicine. Mechanisms, diagnosis, treatment; staging continuum and LVH epidemiology; SGLT2i LV mass signals. URL: https://doi.org/10.31083/j.rcm2503093 (huang2024hypertensiveheartdisease pages 1-2, huang2024hypertensiveheartdisease pages 17-18).
- Gallo & Savoia, Jun 2024, IJMS. RAAS–oxidative stress–microvascular pathways linking HTN to HF; CMD/rarefaction and HFpEF. URL: https://doi.org/10.3390/ijms25126661 (gallo2024hypertensionandheart pages 2-4).
- Durante et al., Dec 2024, IJMS. Systemic and cardiac microvascular dysfunction in hypertension; rarefaction and endothelial dysfunction mechanisms. URL: https://doi.org/10.3390/ijms252413294 (durante2024systemicandcardiac pages 1-3).
- Patrick et al., Jun 2024, Science Advances. Integrated single-cell mapping of cardiac fibroblast activation across ischemic and pressure-overload cardiomyopathies. URL: https://doi.org/10.1126/sciadv.adk8501 (patrick2024integrationmappingof pages 1-2).
- Vlachakis et al., May 2024, IJMS. Inflammasomes in HF; NLRP3/IL‑1β in pressure overload remodeling and fibrosis; early clinical translation. URL: https://doi.org/10.3390/ijms25105372 (vlachakis2024theroleof pages 2-4, vlachakis2024theroleof pages 9-11).
- Zhang & Guo, Dec 2024, Antioxidants. Oxidative stress blueprint; mitochondrial/NOX sources; inflammasome triggers. URL: https://doi.org/10.3390/antiox14010038 (zhang2024decipheringoxidativestress pages 7-9).
- Wróbel‑Nowicka et al., May 2024, Medicina. Oxidative stress/inflammation in HF; NOX1/2/4, CaMKII, MMPs. URL: https://doi.org/10.3390/medicina60050760 (wrobelnowicka2024theroleof pages 3-5).
- Wang et al., Mar 2023, Heart Failure Reviews. Endothelial-cell mechanisms of CMD leading to HFpEF; links to HTN, inflammatory cytokines, reduced CFR. URL: https://doi.org/10.1007/s10741-022-10224-y (wang2023endothelialcellmediatedmechanismof pages 1-2).

Limitations and open questions: While 2024 sources substantiate key mechanisms (RAAS–TGF‑β, oxidative stress, CMD/rarefaction, inflammasome, fibroblast programs), high‑quality prospective human data isolating pathway-specific contributions in pure hypertension (independent of comorbidities) remain limited; ongoing work integrates single‑cell/spatial omics with deep phenotyping to refine HHD endotypes and targeted therapies (patrick2024integrationmappingof pages 1-2, nemtsova2024hypertensiveheartdisease pages 1-2).


References

1. (nemtsova2024hypertensiveheartdisease pages 1-2): Valeriya Nemtsova, Annina S. Vischer, and Thilo Burkard. Hypertensive heart disease: a narrative review series—part 3: vasculature, biomarkers and the matrix of hypertensive heart disease. Journal of Clinical Medicine, 13:505, Jan 2024. URL: https://doi.org/10.3390/jcm13020505, doi:10.3390/jcm13020505. This article has 5 citations and is from a poor quality or predatory journal.

2. (nemtsova2024hypertensiveheartdisease pages 17-19): Valeriya Nemtsova, Annina S. Vischer, and Thilo Burkard. Hypertensive heart disease: a narrative review series—part 3: vasculature, biomarkers and the matrix of hypertensive heart disease. Journal of Clinical Medicine, 13:505, Jan 2024. URL: https://doi.org/10.3390/jcm13020505, doi:10.3390/jcm13020505. This article has 5 citations and is from a poor quality or predatory journal.

3. (huang2024hypertensiveheartdisease pages 1-2): Xuewei Huang, Lizhi Hu, Zhuojun Long, Xinyao Wang, Junru Wu, and Jingjing Cai. Hypertensive heart disease: mechanisms, diagnosis and treatment. Reviews in Cardiovascular Medicine, Mar 2024. URL: https://doi.org/10.31083/j.rcm2503093, doi:10.31083/j.rcm2503093. This article has 14 citations and is from a peer-reviewed journal.

4. (nemtsova2024hypertensiveheartdisease pages 15-17): Valeriya Nemtsova, Annina S. Vischer, and Thilo Burkard. Hypertensive heart disease: a narrative review series—part 3: vasculature, biomarkers and the matrix of hypertensive heart disease. Journal of Clinical Medicine, 13:505, Jan 2024. URL: https://doi.org/10.3390/jcm13020505, doi:10.3390/jcm13020505. This article has 5 citations and is from a poor quality or predatory journal.

5. (kadoglou2024challengesinechocardiography pages 2-4): Nikolaos P. E. Kadoglou, Angeliki Mouzarou, Nikoleta Hadjigeorgiou, Ioannis Korakianitis, and Michael M. Myrianthefs. Challenges in echocardiography for the diagnosis and prognosis of non-ischemic hypertensive heart disease. Journal of Clinical Medicine, 13:2708, May 2024. URL: https://doi.org/10.3390/jcm13092708, doi:10.3390/jcm13092708. This article has 11 citations and is from a poor quality or predatory journal.

6. (gallo2024hypertensionandheart pages 2-4): Giovanna Gallo and Carmine Savoia. Hypertension and heart failure: from pathophysiology to treatment. International Journal of Molecular Sciences, 25:6661, Jun 2024. URL: https://doi.org/10.3390/ijms25126661, doi:10.3390/ijms25126661. This article has 49 citations and is from a poor quality or predatory journal.

7. (durante2024systemicandcardiac pages 1-3): Alessandro Durante, Alessandro Mazzapicchi, and Martina Baiardo Redaelli. Systemic and cardiac microvascular dysfunction in hypertension. International Journal of Molecular Sciences, 25:13294, Dec 2024. URL: https://doi.org/10.3390/ijms252413294, doi:10.3390/ijms252413294. This article has 39 citations and is from a poor quality or predatory journal.

8. (zhang2024decipheringoxidativestress pages 7-9): Zhaoshan Zhang and Jiawei Guo. Deciphering oxidative stress in cardiovascular disease progression: a blueprint for mechanistic understanding and therapeutic innovation. Antioxidants, 14:38, Dec 2024. URL: https://doi.org/10.3390/antiox14010038, doi:10.3390/antiox14010038. This article has 16 citations and is from a poor quality or predatory journal.

9. (vlachakis2024theroleof pages 2-4): Panayotis K. Vlachakis, Panagiotis Theofilis, Ioannis Kachrimanidis, Konstantinos Giannakopoulos, Maria Drakopoulou, Anastasios Apostolos, Athanasios Kordalis, Ioannis Leontsinis, Konstantinos Tsioufis, and Dimitris Tousoulis. The role of inflammasomes in heart failure. International Journal of Molecular Sciences, 25:5372, May 2024. URL: https://doi.org/10.3390/ijms25105372, doi:10.3390/ijms25105372. This article has 17 citations and is from a poor quality or predatory journal.

10. (nemtsova2024hypertensiveheartdisease pages 4-5): Valeriya Nemtsova, Annina S. Vischer, and Thilo Burkard. Hypertensive heart disease: a narrative review series—part 3: vasculature, biomarkers and the matrix of hypertensive heart disease. Journal of Clinical Medicine, 13:505, Jan 2024. URL: https://doi.org/10.3390/jcm13020505, doi:10.3390/jcm13020505. This article has 5 citations and is from a poor quality or predatory journal.

11. (wang2023endothelialcellmediatedmechanismof pages 1-2): Yong Wang, Juan Zhang, Zhen Wang, Cheng Wang, and Dufang Ma. Endothelial-cell-mediated mechanism of coronary microvascular dysfunction leading to heart failure with preserved ejection fraction. Heart Failure Reviews, 28:169-178, Mar 2023. URL: https://doi.org/10.1007/s10741-022-10224-y, doi:10.1007/s10741-022-10224-y. This article has 34 citations and is from a peer-reviewed journal.

12. (nemtsova2024hypertensiveheartdisease pages 2-4): Valeriya Nemtsova, Annina S. Vischer, and Thilo Burkard. Hypertensive heart disease: a narrative review series—part 3: vasculature, biomarkers and the matrix of hypertensive heart disease. Journal of Clinical Medicine, 13:505, Jan 2024. URL: https://doi.org/10.3390/jcm13020505, doi:10.3390/jcm13020505. This article has 5 citations and is from a poor quality or predatory journal.

13. (wrobelnowicka2024theroleof pages 3-5): Karolina Wróbel-Nowicka, Celina Wojciechowska, Wojciech Jacheć, Marzena Zalewska, and Ewa Romuk. The role of oxidative stress and inflammatory parameters in heart failure. Medicina, 60:760, May 2024. URL: https://doi.org/10.3390/medicina60050760, doi:10.3390/medicina60050760. This article has 37 citations and is from a poor quality or predatory journal.

14. (vlachakis2024theroleof pages 9-11): Panayotis K. Vlachakis, Panagiotis Theofilis, Ioannis Kachrimanidis, Konstantinos Giannakopoulos, Maria Drakopoulou, Anastasios Apostolos, Athanasios Kordalis, Ioannis Leontsinis, Konstantinos Tsioufis, and Dimitris Tousoulis. The role of inflammasomes in heart failure. International Journal of Molecular Sciences, 25:5372, May 2024. URL: https://doi.org/10.3390/ijms25105372, doi:10.3390/ijms25105372. This article has 17 citations and is from a poor quality or predatory journal.

15. (gaydarski2025morphometricandmolecular pages 6-8): Lyubomir Gaydarski, Kristina Petrova, Stancho Stanchev, Dimitar Pelinkov, Alexandar Iliev, Iva N. Dimitrova, Vidin Kirkov, Boycho Landzhov, and Nikola Stamenov. Morphometric and molecular interplay in hypertension-induced cardiac remodeling with an emphasis on the potential therapeutic implications. International Journal of Molecular Sciences, 26:4022, Apr 2025. URL: https://doi.org/10.3390/ijms26094022, doi:10.3390/ijms26094022. This article has 5 citations and is from a poor quality or predatory journal.

16. (gaydarski2025morphometricandmolecular pages 1-2): Lyubomir Gaydarski, Kristina Petrova, Stancho Stanchev, Dimitar Pelinkov, Alexandar Iliev, Iva N. Dimitrova, Vidin Kirkov, Boycho Landzhov, and Nikola Stamenov. Morphometric and molecular interplay in hypertension-induced cardiac remodeling with an emphasis on the potential therapeutic implications. International Journal of Molecular Sciences, 26:4022, Apr 2025. URL: https://doi.org/10.3390/ijms26094022, doi:10.3390/ijms26094022. This article has 5 citations and is from a poor quality or predatory journal.

17. (gaydarski2025morphometricandmolecular pages 5-6): Lyubomir Gaydarski, Kristina Petrova, Stancho Stanchev, Dimitar Pelinkov, Alexandar Iliev, Iva N. Dimitrova, Vidin Kirkov, Boycho Landzhov, and Nikola Stamenov. Morphometric and molecular interplay in hypertension-induced cardiac remodeling with an emphasis on the potential therapeutic implications. International Journal of Molecular Sciences, 26:4022, Apr 2025. URL: https://doi.org/10.3390/ijms26094022, doi:10.3390/ijms26094022. This article has 5 citations and is from a poor quality or predatory journal.

18. (patrick2024integrationmappingof pages 1-2): Ralph Patrick, Vaibhao Janbandhu, Vikram Tallapragada, Shannon S. M. Tan, Emily E. McKinna, Osvaldo Contreras, Shila Ghazanfar, David T. Humphreys, Nicholas J. Murray, Yen T. H. Tran, Robert D. Hume, James J. H. Chong, and Richard P. Harvey. Integration mapping of cardiac fibroblast single-cell transcriptomes elucidates cellular principles of fibrosis in diverse pathologies. Science Advances, Jun 2024. URL: https://doi.org/10.1126/sciadv.adk8501, doi:10.1126/sciadv.adk8501. This article has 39 citations and is from a highest quality peer-reviewed journal.

19. (huang2024hypertensiveheartdisease pages 17-18): Xuewei Huang, Lizhi Hu, Zhuojun Long, Xinyao Wang, Junru Wu, and Jingjing Cai. Hypertensive heart disease: mechanisms, diagnosis and treatment. Reviews in Cardiovascular Medicine, Mar 2024. URL: https://doi.org/10.31083/j.rcm2503093, doi:10.31083/j.rcm2503093. This article has 14 citations and is from a peer-reviewed journal.

20. (rolski2025cardiacfibrosismechanistic pages 4-6): Filip Rolski and Michał Mączewski. Cardiac fibrosis: mechanistic discoveries linked to sglt2 inhibitors. Pharmaceuticals, 18:313, Feb 2025. URL: https://doi.org/10.3390/ph18030313, doi:10.3390/ph18030313. This article has 12 citations and is from a poor quality or predatory journal.