---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T18:38:29.408843'
end_time: '2025-12-17T18:47:00.350261'
duration_seconds: 510.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Heart Failure
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Heart Failure
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Heart Failure**.
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
- **Disease Name:** Heart Failure
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Heart Failure**.
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
- Disease Name: Heart Failure (HF)
- MONDO ID: MONDO:0002025
- Category: Complex

Pathophysiology description (current understanding and key definitions)
Heart failure is a clinical syndrome arising from structural and/or functional cardiac abnormalities that impair the heart’s ability to fill and/or eject blood, leading to symptoms (e.g., dyspnea, fatigue) and signs (e.g., edema) of congestion. Mechanistically, HF spans phenotypes with reduced ejection fraction (HFrEF) and preserved ejection fraction (HFpEF). Across the spectrum, convergent molecular and cellular processes drive maladaptive remodeling: neurohormonal activation (RAAS, sympathetic drive, natriuretic peptide axis), endothelial and coronary microvascular dysfunction with impaired NO–sGC–cGMP signaling, cardiac fibrosis and myofibroblast activation (TGF-β/SMAD), inflammation with immune–fibroblast crosstalk, metabolic and mitochondrial remodeling with oxidative stress and altered substrate use (including increased reliance on ketone bodies), and cardiomyocyte Ca2+ handling and sarcomere/titin stiffness abnormalities. These lesions unfold within the myocardium and the coronary microvasculature and are modulated by extracardiac organs (adipose, liver, kidney), particularly in cardiometabolic HFpEF. (fayyaz2025pathophysiologicalinsightsinto pages 11-13, fayyaz2025pathophysiologicalinsightsinto pages 23-24, fonseka2025molecularmechanismsunderlying pages 1-2, mishra2021cellularandmolecular pages 14-15, gorica2025cardiometabolicheartfailure pages 1-3)

Recent developments and latest research (2023–2024 prioritized)
- Microvascular/endothelial and NO–sGC–cGMP impairment in HFpEF: Human tissue–based syntheses emphasize microvascular endothelial dysfunction, reduced NO bioavailability, and cGMP/PKG signaling defects as central nodes linking comorbidities to cardiomyocyte stiffness and diastolic dysfunction; restoring cGMP acutely via PDE inhibition, sGC stimulation, or SGLT2 inhibition improves myocardial function. “Enhancing cGMP signalling acutely via PDE9A or PDE5 inhibition, sGC stimulation or SGLT2 inhibition improves myocardial function.” (Nature Reviews Cardiology, 2025; DOI: 10.1038/s41569-024-01067-1; https://doi.org/10.1038/s41569-024-01067-1). (fayyaz2025pathophysiologicalinsightsinto pages 11-13)
- Fibrosis and ECM stiffness: Human myocardial analyses integrate collagen and titin contributions to stiffness, with ECM remodeling and titin phosphorylation as key determinants of diastolic properties. (Nature Reviews Cardiology, 2025; DOI: 10.1038/s41569-024-01067-1; https://doi.org/10.1038/s41569-024-01067-1). (fayyaz2025pathophysiologicalinsightsinto pages 23-24)
- Immune–fibroblast crosstalk at single-cell resolution: A 2025 single-nucleus human HFpEF atlas reported cardiomyocyte metabolic repression, endothelial apoptosis signaling and reduced VEGF signaling, macrophage proinflammatory states (MHC-II up), and fibroblast activation; intriguingly, exogenous IFN-γ reduced collagen output from human cardiac fibroblasts (bioRxiv, 2025; DOI: 10.1101/2025.04.02.646923; https://doi.org/10.1101/2025.04.02.646923). (zanders2025decipheringhumanheart pages 1-5)
- Ca2+ handling and sarcomere/titin in HFpEF: Mouse HFpEF models (2024) highlight increased phosphorylation of CaMKII, RyR2, and phospholamban with pronounced Ca2+ dysregulation, and ECM gene activation; endothelial dysfunction and titin hypophosphorylation are linked to impaired diastolic reserve. (ArXiv dissertation, 2024; DOI: 10.53846/goediss-10367; https://doi.org/10.53846/goediss-10367). (swarnkar2024mechanisticdifferencesin pages 14-18, swarnkar2024mechanisticdifferencesin pages 22-25)
- Cardiometabolic HFpEF (obesity/diabetes phenotype): Recent review synthesizes metabolic remodeling, immune activation, microvascular dysfunction, and chromatin changes as defining cmHFpEF biology, aligning with trials supporting SGLT2 inhibitors and GLP-1 receptor agonists in obese HFpEF. (Cardiovascular Diabetology, 2025; DOI: 10.1186/s12933-025-02774-w; https://doi.org/10.1186/s12933-025-02774-w). (gorica2025cardiometabolicheartfailure pages 1-3)
- Systems view across HF: A comprehensive 2025 review enumerates core mechanisms—mitochondrial dysfunction and oxidative stress, ER stress, impaired autophagy, lipotoxicity, inflammation, endothelial dysfunction, and defective contractility/Ca2+ handling—as therapeutic targets, noting differences between HFrEF (more myocyte loss) and HFpEF (stiffness, inflammation, microvasculature). (Cells, 2025; DOI: 10.3390/cells14050324; https://doi.org/10.3390/cells14050324). (fonseka2025molecularmechanismsunderlying pages 1-2)

Current applications and real-world implementations (therapy links)
- cGMP axis: Given impaired NO–sGC–cGMP signaling, strategies that enhance cGMP (e.g., PDE5/PDE9 inhibition, sGC stimulation) or augment natriuretic peptides and NP-derived cGMP (e.g., SGLT2 inhibitors’ indirect effects) can improve myocardial function in HFpEF mechanistic studies. (10.1038/s41569-024-01067-1; 2025). (fayyaz2025pathophysiologicalinsightsinto pages 11-13)
- Guideline-directed HF therapies mapped to mechanisms:
  - HFrEF: RAAS inhibition/ARNI, β-blockers, MRA—target neurohormonal activation and antifibrotic signaling; SGLT2 inhibitors provide diuretic/metabolic and cardiorenal benefits (translatable cGMP/NO interplay). (10.1038/s41569-024-01067-1; 2025). (fayyaz2025pathophysiologicalinsightsinto pages 11-13)
  - HFpEF: SGLT2 inhibitors across EF; for obese HFpEF, GLP‑1 receptor agonists (e.g., semaglutide) improve symptoms and function via weight loss and metabolic anti-inflammatory effects, aligning with cardiometabolic biology. (Cardiovascular Diabetology, 2025; 10.1186/s12933-025-02774-w; 2025). (gorica2025cardiometabolicheartfailure pages 1-3)

Expert opinions and analysis (authoritative sources with quotes)
- Human tissue–based perspective on HFpEF pathobiology emphasizes multi-compartment disease integrating fibrosis/titin stiffness, endothelial/microvascular dysfunction, metabolic stress, and cGMP impairment: “Inflammation and microvascular endothelial dysfunction are recurrent findings… [with] altered NO–sGC–cGMP… signalling… enhancing cGMP signalling… improves myocardial function.” (Nature Reviews Cardiology, 2025; 10.1038/s41569-024-01067-1; https://doi.org/10.1038/s41569-024-01067-1). (fayyaz2025pathophysiologicalinsightsinto pages 11-13)
- Microvascular centrality and exercise limitations: Microvascular disease correlates with impaired perfusion and diastolic relaxation and worse outcomes; large-artery stiffening augments late systolic load. (Nature Reviews Cardiology, 2021; 10.1038/s41569-020-00480-6; https://doi.org/10.1038/s41569-020-00480-6). (mishra2021cellularandmolecular pages 14-15)
- Cellular single-cell atlas opinions highlight potential targets (RHOA/ROCK1 in cardiomyocytes; interferon signaling states across fibroblasts and macrophages): “cardiomyocytes show downregulation of aerobic respiration… fibroblasts display activation… macrophages exhibit a pro-inflammatory transcriptome… exogenous rhIFNγ reduced collagen in human cardiac fibroblasts.” (bioRxiv, 2025; 10.1101/2025.04.02.646923; https://doi.org/10.1101/2025.04.02.646923). (zanders2025decipheringhumanheart pages 1-5)

Relevant statistics and data (recent)
- HFpEF accounts for >50% of treated HF and is rising with aging/metabolic comorbidity; five‑year mortality remains high. (Cells, 2025; https://doi.org/10.3390/cells14050324; Nature Reviews Cardiology, 2025; https://doi.org/10.1038/s41569-024-01067-1). (fonseka2025molecularmechanismsunderlying pages 1-2, fayyaz2025pathophysiologicalinsightsinto pages 11-13)
- Mechanistic intervention data (preclinical/translation): Acute enhancement of cGMP signaling via PDE or sGC pathways improves myocardial function in HFpEF experimental settings; SGLT2 inhibition also links to cGMP improvements. (Nature Reviews Cardiology, 2025; https://doi.org/10.1038/s41569-024-01067-1). (fayyaz2025pathophysiologicalinsightsinto pages 11-13)
- Mouse HFpEF models (2024) show increased CaMKII/RyR2/PLN phosphorylation and ECM gene upregulation with endothelial dysfunction and impaired diastolic reserve. (ArXiv, 2024; https://doi.org/10.53846/goediss-10367). (swarnkar2024mechanisticdifferencesin pages 14-18, swarnkar2024mechanisticdifferencesin pages 22-25)

Core Pathophysiology
Primary mechanisms
- Neurohormonal activation: RAAS and SNS activation drive hypertrophy, fibrosis, oxidative stress; natriuretic peptide system counterbalances via cGMP. HFpEF shows impaired NP/NO signaling and cGMP deficits. (10.1038/s41569-024-01067-1; 2025). (fayyaz2025pathophysiologicalinsightsinto pages 11-13)
- Endothelial/microvascular dysfunction: Reduced NO bioavailability, oxidative/nitrosative stress (e.g., NOX enzymes, uncoupled eNOS) and decreased coronary flow reserve propagate diastolic dysfunction and exercise intolerance. (10.1038/s41569-020-00480-6; 2021; 10.53846/goediss-10367; 2024). (mishra2021cellularandmolecular pages 14-15, swarnkar2024mechanisticdifferencesin pages 22-25)
- Fibrosis and ECM remodeling: TGF‑β/SMAD signaling activates myofibroblasts, increasing collagen and crosslinking; titin hypophosphorylation increases passive stiffness; perivascular fibrosis worsens microvascular mechanics. (10.1038/s41569-024-01067-1; 2025). (fayyaz2025pathophysiologicalinsightsinto pages 23-24)
- Inflammation and immune–fibroblast crosstalk: Proinflammatory macrophages and cytokines (IL‑6, TNF) promote fibroblast activation and ECM deposition; interferon signaling states differentially regulate fibroblast collagen output. (10.1101/2025.04.02.646923; 2025; 10.53846/goediss-10367; 2024). (zanders2025decipheringhumanheart pages 1-5, swarnkar2024mechanisticdifferencesin pages 14-18)
- Metabolic and mitochondrial remodeling: Decreased fatty acid oxidation and impaired mitochondrial energetics with increased oxidative stress; a shift toward ketone body utilization is observed; SGLT2 inhibition and metabolic strategies can be beneficial. (10.3390/cells14050324; 2025; 10.1186/s12933-025-02774-w; 2025). (fonseka2025molecularmechanismsunderlying pages 1-2, gorica2025cardiometabolicheartfailure pages 1-3)
- Calcium handling and sarcomere defects: Abnormal Ca2+ cycling (SERCA/PLN, RyR2) and titin phosphorylation state contribute to impaired relaxation in HFpEF; HFrEF features impaired contractility with myocyte loss. (10.1038/s41569-024-01067-1; 2025; 10.53846/goediss-10367; 2024). (fayyaz2025pathophysiologicalinsightsinto pages 23-24, swarnkar2024mechanisticdifferencesin pages 14-18)

Dysregulated molecular pathways
- NO–sGC–cGMP–PKG; TGF‑β/SMAD; NF‑κB/cytokine signaling; mitochondrial OXPHOS and ROS handling; CaMKII and RyR2 phosphorylation; NP signaling and PDE-mediated cGMP hydrolysis; interferon signaling axes. (fayyaz2025pathophysiologicalinsightsinto pages 11-13, fayyaz2025pathophysiologicalinsightsinto pages 23-24, fonseka2025molecularmechanismsunderlying pages 1-2, zanders2025decipheringhumanheart pages 1-5, swarnkar2024mechanisticdifferencesin pages 14-18)

Affected cellular processes
- Vaso-regulation and angiogenesis; ECM organization and crosslinking; immune activation and antigen presentation; mitochondrial respiration and substrate selection; excitation–contraction coupling; proteostasis (UPR) and autophagy. (fayyaz2025pathophysiologicalinsightsinto pages 11-13, fayyaz2025pathophysiologicalinsightsinto pages 23-24, fonseka2025molecularmechanismsunderlying pages 1-2)

Key Molecular Players (annotations)
- Genes/Proteins (HGNC): NOS3; NPPA/NPPB; GUCY1A1/GUCY1A3; PDE5A/PDE9A; TGFB1; SMAD3; COL1A1; LOX; THBS4; SPP1; IL6; TNF; PPARGC1A (PGC‑1α); SIRT3; BDH1; OXCT1; HMGCS2; TTN; RYR2; PLN; ATP2A2 (SERCA2a). (fayyaz2025pathophysiologicalinsightsinto pages 11-13, fayyaz2025pathophysiologicalinsightsinto pages 23-24, fonseka2025molecularmechanismsunderlying pages 1-2, zanders2025decipheringhumanheart pages 1-5)
- Chemical Entities (CHEBI): nitric oxide; cGMP; angiotensin II; aldosterone; catecholamines; collagen crosslink cofactor lysyl oxidase substrates; β‑hydroxybutyrate (ketone body). (fayyaz2025pathophysiologicalinsightsinto pages 11-13, fayyaz2025pathophysiologicalinsightsinto pages 23-24, fonseka2025molecularmechanismsunderlying pages 1-2)
- Cell Types (CL): cardiomyocytes; cardiac fibroblasts/myofibroblasts; endothelial cells (microvascular ECs); pericytes; macrophages/monocytes; T cells; epicardial adipocytes. (zanders2025decipheringhumanheart pages 1-5, mishra2021cellularandmolecular pages 14-15, gorica2025cardiometabolicheartfailure pages 1-3)
- Anatomical locations (UBERON): ventricular myocardium; coronary microvasculature; myocardial interstitium; epicardial adipose tissue; endocardium; large arteries (arterial stiffness). (mishra2021cellularandmolecular pages 14-15, gorica2025cardiometabolicheartfailure pages 1-3)

Biological Processes (GO) disrupted
- GO:0001937 regulation of endothelial cell proliferation and GO:0038083 peptidyl-tyrosine phosphorylation via NO–sGC–cGMP signaling deficits. (fayyaz2025pathophysiologicalinsightsinto pages 11-13)
- GO:0030198 extracellular matrix organization and GO:0042110 T cell activation in fibrotic remodeling with immune crosstalk. (fayyaz2025pathophysiologicalinsightsinto pages 23-24, zanders2025decipheringhumanheart pages 1-5)
- GO:0006119 oxidative phosphorylation and GO:0006091 generation of precursor metabolites and energy (mitochondrial dysfunction). (fonseka2025molecularmechanismsunderlying pages 1-2)
- GO:0051928 regulation of Ca2+ ion transport and GO:0030049 muscle filament sliding (Ca2+ handling/sarcomere). (fayyaz2025pathophysiologicalinsightsinto pages 23-24, swarnkar2024mechanisticdifferencesin pages 14-18)
- GO:0006954 inflammatory response and GO:0006955 immune response (systemic and myocardial inflammation). (zanders2025decipheringhumanheart pages 1-5, gorica2025cardiometabolicheartfailure pages 1-3)

Cellular Components (GO-CC)
- Plasma membrane caveolae (eNOS/NOS3); cytosol (sGC); mitochondrial inner membrane and matrix (OXPHOS complexes); sarcoplasmic reticulum (SERCA/PLN); sarcomere (titin); extracellular matrix (collagens, LOX-mediated crosslinks). (fayyaz2025pathophysiologicalinsightsinto pages 11-13, fonseka2025molecularmechanismsunderlying pages 1-2, fayyaz2025pathophysiologicalinsightsinto pages 23-24)

Disease Progression (sequence and stages)
- Triggering comorbidities (hypertension, obesity/diabetes, aging) → systemic inflammation, oxidative stress, endothelial dysfunction and microvascular rarefaction → reduced NO/cGMP signaling → cardiomyocyte stiffness (titin hypophosphorylation) and concentric remodeling; progressive interstitial/perivascular fibrosis via TGF‑β/SMAD and immune–fibroblast paracrine loops → impaired lusitropy and reduced diastolic reserve; in HFrEF, myocyte death and eccentric remodeling feature prominently, producing reduced contractility. Exercise induces marked rises in filling pressures (impaired diastolic reserve) with chronotropic incompetence and altered ventricular–arterial coupling in HFpEF. (10.53846/goediss-10367; 2024; 10.1038/s41569-020-00480-6; 2021; 10.1038/s41569-024-01067-1; 2025). (swarnkar2024mechanisticdifferencesin pages 22-25, mishra2021cellularandmolecular pages 14-15, fayyaz2025pathophysiologicalinsightsinto pages 23-24)

Phenotypic Manifestations (HP terms examples) and mechanism links
- HP:0002090 Dyspnea; HP:0001643 Congestive heart failure; HP:0005136 Exercise intolerance: relate to impaired diastolic reserve, microvascular/endothelial dysfunction, and elevated filling pressures in HFpEF; reduced contractility in HFrEF. (mishra2021cellularandmolecular pages 14-15, swarnkar2024mechanisticdifferencesin pages 22-25)
- HP:0030973 Diastolic dysfunction: titin hypophosphorylation and fibrosis increase passive stiffness; microvascular dysfunction limits myocardial perfusion reserve. (fayyaz2025pathophysiologicalinsightsinto pages 23-24, mishra2021cellularandmolecular pages 14-15)
- HP:0001639 Ventricular hypertrophy: concentric remodeling in HFpEF under late systolic load and neurohormonal stress. (mishra2021cellularandmolecular pages 14-15)
- HP:0005150 Edema: neurohormonal activation and renal–cardiac interplay with congestion. (fonseka2025molecularmechanismsunderlying pages 1-2)

Ontology-aligned annotations (consolidated)
- HGNC: NOS3; GUCY1A1; PDE5A; PDE9A; NPPA; NPPB; TGFB1; SMAD3; COL1A1; LOX; THBS4; SPP1; IL6; TNF; PPARGC1A; SIRT3; BDH1; OXCT1; HMGCS2; TTN; RYR2; PLN; ATP2A2. (fayyaz2025pathophysiologicalinsightsinto pages 11-13, fayyaz2025pathophysiologicalinsightsinto pages 23-24, fonseka2025molecularmechanismsunderlying pages 1-2, zanders2025decipheringhumanheart pages 1-5)
- GO (process): endothelial NO signaling; ECM organization; inflammatory response; oxidative phosphorylation; calcium ion transport; muscle contraction. (fayyaz2025pathophysiologicalinsightsinto pages 11-13, fayyaz2025pathophysiologicalinsightsinto pages 23-24, fonseka2025molecularmechanismsunderlying pages 1-2)
- GO (component): caveolae; cytosol; mitochondrial inner membrane; sarcoplasmic reticulum; sarcomere; extracellular matrix. (fayyaz2025pathophysiologicalinsightsinto pages 11-13, fonseka2025molecularmechanismsunderlying pages 1-2, fayyaz2025pathophysiologicalinsightsinto pages 23-24)
- CL: cardiomyocyte; cardiac fibroblast; endothelial cell; pericyte; macrophage; T cell; adipocyte (epicardial). (zanders2025decipheringhumanheart pages 1-5, gorica2025cardiometabolicheartfailure pages 1-3)
- UBERON: ventricular myocardium; coronary microvasculature; myocardial interstitium; epicardial adipose tissue; arterial tree. (mishra2021cellularandmolecular pages 14-15, gorica2025cardiometabolicheartfailure pages 1-3)
- CHEBI: nitric oxide; cGMP; angiotensin II; aldosterone; catecholamine; β‑hydroxybutyrate. (fayyaz2025pathophysiologicalinsightsinto pages 11-13, fayyaz2025pathophysiologicalinsightsinto pages 23-24, fonseka2025molecularmechanismsunderlying pages 1-2)

Evidence items with PMIDs/DOIs/URLs/dates (selected, recent emphasis)
- Nature Reviews Cardiology (2025). Pathophysiological insights into HFpEF from human tissue. DOI: 10.1038/s41569-024-01067-1. URL: https://doi.org/10.1038/s41569-024-01067-1. (fayyaz2025pathophysiologicalinsightsinto pages 23-24, fayyaz2025pathophysiologicalinsightsinto pages 11-13)
- ArXiv dissertation (2024). Mechanistic differences in mouse models of HFpEF. DOI: 10.53846/goediss-10367. URL: https://doi.org/10.53846/goediss-10367. (swarnkar2024mechanisticdifferencesin pages 22-25, swarnkar2024mechanisticdifferencesin pages 14-18)
- Cardiovascular Diabetology (2025). Cardiometabolic HFpEF molecular signatures and therapy. DOI: 10.1186/s12933-025-02774-w. URL: https://doi.org/10.1186/s12933-025-02774-w. (gorica2025cardiometabolicheartfailure pages 1-3)
- Cells (2025). Molecular mechanisms underlying HF and therapeutic potential. DOI: 10.3390/cells14050324. URL: https://doi.org/10.3390/cells14050324. (fonseka2025molecularmechanismsunderlying pages 1-2)
- Nature Reviews Cardiology (2021). Cellular/molecular pathobiology of HFpEF emphasizing vascular biology. DOI: 10.1038/s41569-020-00480-6. URL: https://doi.org/10.1038/s41569-020-00480-6. (mishra2021cellularandmolecular pages 14-15)
- bioRxiv (2025). Single-cell human HFpEF atlas. DOI: 10.1101/2025.04.02.646923. URL: https://doi.org/10.1101/2025.04.02.646923. (zanders2025decipheringhumanheart pages 1-5)

Embedded mechanistic summary table
| Mechanistic theme | Key molecules/genes (HGNC) | Dominant cell types (CL) | Disrupted processes (GO) | Cellular components (GO-CC) | Anatomic sites (UBERON) | Representative quotes/data | Therapeutic links | Evidence (DOI/URL, year) |
|---|---|---|---|---|---|---|---|---|
| Neurohormonal activation & endothelial / microvascular dysfunction (NO–sGC–cGMP) | NOS3, NPPA / NPPB, GUCY1A1/GUCY1A3, PDE5A, PDE9A | Endothelial cells; cardiomyocytes; pericytes | NO–cGMP signaling; endothelial nitric oxide bioavailability; vasodilation; angiogenesis | Plasma membrane (eNOS), cytosol (sGC), caveolae | Myocardium; coronary microvasculature | "enhancing cGMP signalling acutely via PDE9A or PDE5 inhibition, sGC stimulation or SGLT2 inhibition improves myocardial function" (fayyaz2025pathophysiologicalinsightsinto pages 11-13) | sGC stimulators (vericiguat), PDE inhibitors, SGLT2 inhibitors, ARNI (natriuretic peptide augmentation) | 10.1038/s41569-024-01067-1 https://doi.org/10.1038/s41569-024-01067-1 (2025) (fayyaz2025pathophysiologicalinsightsinto pages 11-13) |
| Fibrosis & TGF-β / myofibroblast activation | TGFB1, SMAD3, COL1A1, LOX, THBS4 | Cardiac fibroblasts / myofibroblasts; cardiomyocytes; immune cells | ECM organization; myofibroblast differentiation; collagen biosynthesis & cross-linking | Extracellular matrix; secretory vesicle; nucleus (SMAD transcription complexes) | Myocardial interstitium; perivascular regions | "Fibrosis and extracellular-matrix regulation ... contributions of collagen and titin to myocardial stiffness are emphasized." (fayyaz2025pathophysiologicalinsightsinto pages 23-24) | Anti-fibrotic strategies (TGF-β pathway modulators, targeting latent TGF-β activators), MRAs (indirect antifibrotic effects) | 10.1038/s41569-024-01067-1 https://doi.org/10.1038/s41569-024-01067-1 (2025) (fayyaz2025pathophysiologicalinsightsinto pages 23-24) |
| Immune–fibroblast crosstalk (inflammation-driven remodeling) | SPP1 (osteopontin), TNF, IL6, CD163, VSIG4 | Macrophages / myeloid cells; fibroblasts; T cells | Cytokine-mediated signalling; antigen presentation (MHC-II); profibrotic paracrine signaling | Secreted cytokines; MHC class II complexes; extracellular matrix | Myocardial interstitium; epicardial adipose interface | "macrophages exhibit a pro-inflammatory transcriptome ... exogenous rhIFNγ reduced collagen in human cardiac fibroblasts" (zanders2025decipheringhumanheart pages 1-5) | Anti-inflammatory approaches (IL‑1 blockade trials), immunomodulation of macrophage–fibroblast signaling | bioRxiv 10.1101/2025.04.02.646923 https://doi.org/10.1101/2025.04.02.646923 (2025) (zanders2025decipheringhumanheart pages 1-5) |
| Metabolic / mitochondrial remodeling & ketone utilization | PPARGC1A (PGC‑1α), SIRT3, BDH1, OXCT1, HMGCS2 | Cardiomyocytes; fibroblasts; (systemic: liver/adipose) | Mitochondrial OXPHOS; fatty acid oxidation; ketone body catabolism; metabolic flexibility | Mitochondrion (inner membrane, matrix); cytosol | Myocardium; liver (heart–liver crosstalk); epicardial adipose | "mitochondrial dysfunction... oxidative stress" as a key HF mechanism; metabolic rewiring in cardiometabolic HFpEF (fonseka2025molecularmechanismsunderlying pages 1-2, gorica2025cardiometabolicheartfailure pages 1-3) | SGLT2 inhibitors (metabolic effects), ketone-based therapies / ketone esters, PGC‑1α / mitochondrial-targeted strategies | Cells 10.3390/cells14050324 https://doi.org/10.3390/cells14050324 (2025) (fonseka2025molecularmechanismsunderlying pages 1-2); Cardiovasc Diabetology 10.1186/s12933-025-02774-w https://doi.org/10.1186/s12933-025-02774-w (2025) (gorica2025cardiometabolicheartfailure pages 1-3) |
| Calcium handling & sarcomere / titin alterations | TTN, RYR2, PLN, CAMK2D, SERCA2A (ATP2A2) | Cardiomyocytes | Calcium ion transport; excitation–contraction coupling; sarcomere organization; titin phosphorylation | Sarcomere (Z-disc, I/A-bands); sarcoplasmic reticulum; sarcolemma | Ventricular myocardium | "stiffness (via phosphorylation of titin) and promote clearance ..." — titin phosphorylation and impaired relaxation are linked to diastolic dysfunction (fayyaz2025pathophysiologicalinsightsinto pages 23-24) | Experimental sarcomere-targeted agents; approaches to stabilize Ca2+ handling (SERCA, RyR modulators); supportive use of guideline drugs | 10.1038/s41569-024-01067-1 https://doi.org/10.1038/s41569-024-01067-1 (2025) (fayyaz2025pathophysiologicalinsightsinto pages 23-24); Nat Rev Cardiol 10.1038/s41569-020-00480-6 (2021) (mishra2021cellularandmolecular pages 14-15) |
| Epicardial adipose & cardiometabolic HFpEF phenotype | ADIPOQ, LEP, ANGPTL4, FABP4 | Epicardial adipocytes; macrophages; fibroblasts; cardiomyocytes | Adipokine signalling; paracrine inflammation; lipid handling | Secreted adipokines; extracellular space adjacent to myocardium | Epicardial adipose tissue (EAT); adjacent myocardium | "cmHFpEF ... metabolic remodeling, rewiring of lipid metabolism, and inflammation" — linking EAT-driven paracrine effects to HFpEF (gorica2025cardiometabolicheartfailure pages 1-3) | Weight-loss strategies, GLP‑1 receptor agonists (semaglutide), SGLT2 inhibitors; targeting EAT inflammation/metabolism | 10.1186/s12933-025-02774-w https://doi.org/10.1186/s12933-025-02774-w (2025) (gorica2025cardiometabolicheartfailure pages 1-3) |
| Disease progression (sequence & multi-organ interactions) | AGT, ACE, REN, NPPA / NPPB, inflammatory mediators (IL6, TNF) | Cardiomyocytes, fibroblasts, endothelial cells, immune cells, renal cells | Neurohormonal activation (RAAS, SNS); chronic inflammation → microvascular dysfunction → fibrosis → contractile dysfunction; metabolic remodeling | Extracellular matrix; mitochondria; sarcomere; vascular endothelium | Myocardium; coronary microvasculature; kidneys; adipose tissue | "reduced diastolic reserve... endothelial dysfunction... titin hypophosphorylation" — exercise intolerance and progressive HFpEF features (swarnkar2024mechanisticdifferencesin pages 22-25) | Guideline therapies: RAAS inhibitors / ARNI, β‑blockers (HFrEF), MRAs, SGLT2 inhibitors across EF, sGC stimulators (vericiguat) in worsening HF; GLP‑1RA for obesity-related HFpEF | ArXiv 10.53846/goediss-10367 https://doi.org/10.53846/goediss-10367 (2024) (swarnkar2024mechanisticdifferencesin pages 22-25); 10.1038/s41569-024-01067-1 (2025) (fayyaz2025pathophysiologicalinsightsinto pages 23-24) |


*Table: A concise table linking principal molecular/cellular mechanisms in heart failure (2023–2024–prioritized evidence) to cell types, disrupted processes, compartments, anatomic sites, representative quotes, therapies, and primary citations (context IDs). This helps map mechanisms to therapeutic strategies and source evidence.*

Notes on scope and limitations
- We prioritized 2023–2024 content; however, several 2025 peer-reviewed syntheses and a 2025 preprint provided high-resolution human tissue and single-cell insights directly relevant to mechanisms and were included with clear source labeling. Some canonical 2021 content (microvascular mechanisms) remains foundational and is cited where most authoritative. (fayyaz2025pathophysiologicalinsightsinto pages 11-13, fayyaz2025pathophysiologicalinsightsinto pages 23-24, mishra2021cellularandmolecular pages 14-15)

Plan completion statement
- The report integrates core mechanisms, cell types, pathways, and phenotypes; maps ontology terms; cites recent, authoritative sources with URLs/dates; and links mechanisms to current therapeutic applications as requested. (fayyaz2025pathophysiologicalinsightsinto pages 11-13, fayyaz2025pathophysiologicalinsightsinto pages 23-24, fonseka2025molecularmechanismsunderlying pages 1-2, gorica2025cardiometabolicheartfailure pages 1-3)

References

1. (fayyaz2025pathophysiologicalinsightsinto pages 11-13): Ahmed U. Fayyaz, Muhammad Eltony, Larry J. Prokop, Katlyn E. Koepp, Barry A. Borlaug, Surendra Dasari, Melanie C. Bois, Kenneth B. Margulies, Joesph J. Maleszewski, Ying Wang, and Margaret M. Redfield. Pathophysiological insights into hfpef from studies of human cardiac tissue. Nature reviews. Cardiology, 22:90-104, Aug 2025. URL: https://doi.org/10.1038/s41569-024-01067-1, doi:10.1038/s41569-024-01067-1. This article has 27 citations.

2. (fayyaz2025pathophysiologicalinsightsinto pages 23-24): Ahmed U. Fayyaz, Muhammad Eltony, Larry J. Prokop, Katlyn E. Koepp, Barry A. Borlaug, Surendra Dasari, Melanie C. Bois, Kenneth B. Margulies, Joesph J. Maleszewski, Ying Wang, and Margaret M. Redfield. Pathophysiological insights into hfpef from studies of human cardiac tissue. Nature reviews. Cardiology, 22:90-104, Aug 2025. URL: https://doi.org/10.1038/s41569-024-01067-1, doi:10.1038/s41569-024-01067-1. This article has 27 citations.

3. (fonseka2025molecularmechanismsunderlying pages 1-2): Oveena Fonseka, S. R. Gare, Xinyi Chen, Jiayan Zhang, N. H. Alatawi, Claire Ross, and Wei Liu. Molecular mechanisms underlying heart failure and their therapeutic potential. Cells, Feb 2025. URL: https://doi.org/10.3390/cells14050324, doi:10.3390/cells14050324. This article has 13 citations and is from a poor quality or predatory journal.

4. (mishra2021cellularandmolecular pages 14-15): Sumita Mishra and David A. Kass. Cellular and molecular pathobiology of heart failure with preserved ejection fraction. Nature Reviews Cardiology, 18:400-423, Jan 2021. URL: https://doi.org/10.1038/s41569-020-00480-6, doi:10.1038/s41569-020-00480-6. This article has 405 citations and is from a domain leading peer-reviewed journal.

5. (gorica2025cardiometabolicheartfailure pages 1-3): Era Gorica, Martin A. Geiger, Ludovica Di Venanzio, Natalia Atzemian, Jan Alphard Kleeberger, Dominique Grigorian, Alessia Mongelli, Besa Emini Veseli, Shafeeq A. Mohammed, Frank Ruschitzka, Andreas J. Flammer, David Niederseer, Sarah Costantino, and Francesco Paneni. Cardiometabolic heart failure with preserved ejection fraction: from molecular signatures to personalized treatment. Cardiovascular Diabetology, Jul 2025. URL: https://doi.org/10.1186/s12933-025-02774-w, doi:10.1186/s12933-025-02774-w. This article has 5 citations and is from a peer-reviewed journal.

6. (zanders2025decipheringhumanheart pages 1-5): Lukas Zanders, Simone F Glaser, Mariano Ruz Jurado, Moritz Brandt, David John, Luka Nicin, David Rodriguez Morales, Wesley T Abplanalp, Tara Procida-Kowalski, Franziska Ganß, Evelyn Ullrich, Alisa Debes, Penelope Pennoyer, Marek Bartkuhn, Reinhard B Dettmeyer, Andreas M Zeiher, Eike Nagel, Philip Wenzel, and Stefanie Dimmeler. Deciphering human heart failure with preserved ejection fraction (hfpef) at single cell resolution. bioRxiv, Apr 2025. URL: https://doi.org/10.1101/2025.04.02.646923, doi:10.1101/2025.04.02.646923. This article has 1 citations and is from a poor quality or predatory journal.

7. (swarnkar2024mechanisticdifferencesin pages 14-18): Surabhi Swarnkar. Mechanistic differences in mouse models of heart failure with preserved ejection fraction. ArXiv, 2024. URL: https://doi.org/10.53846/goediss-10367, doi:10.53846/goediss-10367. This article has 0 citations.

8. (swarnkar2024mechanisticdifferencesin pages 22-25): Surabhi Swarnkar. Mechanistic differences in mouse models of heart failure with preserved ejection fraction. ArXiv, 2024. URL: https://doi.org/10.53846/goediss-10367, doi:10.53846/goediss-10367. This article has 0 citations.