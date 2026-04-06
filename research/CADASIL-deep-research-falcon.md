---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-06T15:01:59.896402'
end_time: '2026-02-06T15:15:31.098968'
duration_seconds: 811.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CADASIL
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** CADASIL
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **CADASIL**.
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
- **Disease Name:** CADASIL
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **CADASIL**.
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
- Disease Name: CADASIL (Cerebral Autosomal Dominant Arteriopathy with Subcortical Infarcts and Leukoencephalopathy)
- Category: Mendelian

Plan overview
We first clarified core concepts and definitions, then prioritized 2023–2024 primary studies and reviews on molecular and cellular mechanisms, genotype–phenotype relationships, and biomarkers, and assembled ontology-linked annotations for key entities. We synthesized evidence into a structured pathophysiology narrative and mapped mechanisms to standardized ontologies, embedding a summary artifact.

1) Core Pathophysiology: current understanding
- Etiologic mechanism. CADASIL is caused predominantly by heterozygous cysteine-altering missense variants in EGFr domains (2–24) of NOTCH3 that change cysteine number, disrupting disulfide bonds, misfolding the NOTCH3 extracellular domain (N3ECD), and promoting its extracellular aggregation in the walls of small arteries and arterioles. Granular osmiophilic material (GOM) is the ultrastructural correlate and pathological hallmark; N3ECD is a principal GOM component localized to the VSMC basement membrane/plasma membrane interface (review) (mizuta2024progresstoclarify pages 1-2, mizuta2024progresstoclarify pages 2-4). URL (Mizuta 2024 Biomolecules): https://doi.org/10.3390/biom14010127 (Jan 2024).
- Aggregation-driven toxicity. In state-of-the-art mouse models and quantitative vascular imaging, “wild-type Notch3ECD coaggregated with mutant Notch3ECD,” and reducing wild-type Notch3 gene dosage mitigated N3ECD accumulation and arterial SMC pathology, while Notch3 target-gene expression remained largely unchanged—supporting a toxic aggregation/co-aggregation mechanism rather than simple signaling loss (Dupré et al., 2024 JCI) (dupre2024proteinaggregatescontaining pages 1-2, dupre2024proteinaggregatescontaining pages 5-6). URL: https://doi.org/10.1172/jci175789 (Feb 2024).
- Extracellular matrix (ECM) co-aggregates and matrisome remodeling. Excess NOTCH3 ECD abnormally recruits ECM proteins into vessel-wall deposits (TIMP3, vitronectin; also LTBP-1 and clusterin reported), and CADASIL vessels show a “HTRA1 loss-of-function profile,” implicating impaired proteostasis of matrisome proteins (2023–2024 evidence and proteomics) (hack2023threetieredegfrdomain pages 14-15, zhao2025mechanisticadvancesin pages 2-4, menendezvalladares2024asearchfor pages 17-18, menendezvalladares2024asearchfor pages 7-11). URL (Hack 2023 Brain): https://doi.org/10.1093/brain/awac486 (Dec 2023).
- Vascular mural cell degeneration and arteriopathy. The small-artery media shows loss of vascular smooth muscle cells (VSMCs) and pericyte involvement; deposits localize to the extracellular/basement membrane and associate with medial fibrosis and luminal stenosis (mouse and human) (dupre2024proteinaggregatescontaining pages 1-2, zhao2025mechanisticadvancesin pages 2-4, mizuta2024progresstoclarify pages 2-4). URL (Dupré 2024 JCI): https://doi.org/10.1172/jci175789 (Feb 2024).
- Inflammation and complement at the vessel wall; endothelial/BBB dysfunction. CADASIL cerebral vessels exhibit ER-stress–linked immunopathology with robust upregulation of ICAM-1 and IL-6 in NOTCH3-mutant VSMCs, induction of endothelial inflammatory mediators in co-culture, and activation of the alternative complement pathway in situ (Factor B, C3d, C5–9/MAC deposition in ~65–75% of microvessels). These data articulate a mural cell–to–endothelium inflammatory axis and complement-mediated injury (Panahi et al., 2023) (panahi2023erstressinduced pages 11-14, panahi2023erstressinduced pages 18-19). URL: https://doi.org/10.1186/s40478-023-01558-1 (May 2023).
- White matter injury and microhemorrhages. Neuropathology demonstrates increased hemosiderin/iron deposits across brain regions and perivascular leakage, concordant with cerebral microbleeds and small-vessel fragility seen on MRI in CADASIL (Magaki et al., 2023) (hack2023threetieredegfrdomain pages 7-10). URL: https://doi.org/10.1093/jnen/nlad004 (Jan 2023).

2) Key molecular players
- Causal gene/protein: NOTCH3 (HGNC:7881). Pathogenic EGFr cysteine-altering variants drive N3ECD misfolding, aggregation, and GOM, with co-aggregation of wild-type N3ECD (dupre2024proteinaggregatescontaining pages 1-2, zhao2025mechanisticadvancesin pages 2-4, mizuta2024progresstoclarify pages 2-4). 
- ECM and co-aggregates: TIMP3, vitronectin, LTBP-1, clusterin; HTRA1 protease activity profile is reduced in CADASIL vessels, consistent with sequestration/inactivation (hack2023threetieredegfrdomain pages 14-15, zhao2025mechanisticadvancesin pages 2-4, menendezvalladares2024asearchfor pages 17-18). 
- Inflammatory/complement mediators: ICAM1, IL6, complement C3, factor B (CFB), and C5b-9 (MAC) are implicated in vessel wall pathology (panahi2023erstressinduced pages 11-14, panahi2023erstressinduced pages 18-19).
- Cell types: Vascular smooth muscle cells and pericytes are primary targets; endothelial cells participate in BBB dysfunction; microglia/macrophages accumulate perivascularly; oligodendrocytes are vulnerable in deep white matter leading to myelin loss (dupre2024proteinaggregatescontaining pages 1-2, zhao2025mechanisticadvancesin pages 2-4, panahi2023erstressinduced pages 11-14, hack2023threetieredegfrdomain pages 7-10).
- Anatomical locations: Small penetrating cerebral arteries/arterioles and leptomeningeal arteries; white matter; characteristic MRI involvement of anterior temporal poles and external capsule; skin dermal arterioles for diagnostic biopsy (mizuta2024progresstoclarify pages 2-4, mizuta2024progresstoclarify pages 1-2, zhao2025mechanisticadvancesin pages 2-4).

Ontology-linked summary table
| Category | Item (standard name) | Ontology ID | Role / Notes | Key Evidence (citation IDs) |
|---|---|---|---|---|
| Genes / Proteins | NOTCH3 (HGNC:7881); HTRA1 (HGNC:5325); TIMP3 (HGNC:11820); VTN (vitronectin, HGNC:12683); CLU/clusterin (HGNC:2095); LTBP1 (HGNC:6718); ICAM1 (HGNC:5344); IL6 (HGNC:6018); C3 (HGNC:1330); CFB/factor B (HGNC:822); C5b-9 (MAC) | HGNC:7881; HGNC:5325; HGNC:11820; HGNC:12683; HGNC:2095; HGNC:6718; HGNC:5344; HGNC:6018; HGNC:1330; HGNC:822; (C5b-9: complex) | NOTCH3 = causal gene; pathogenic cysteine-altering variants → NOTCH3 ECD misfolding, vascular ECD aggregation and GOM formation; ECM proteins (TIMP3, VTN, LTBP1, CLU) co-recruited into deposits; inflammatory/complement components (C3, CFB, C5b-9) and endothelial activation (ICAM1/IL6) implicated in vessel injury. | (dupre2024proteinaggregatescontaining pages 1-2, hack2023threetieredegfrdomain pages 7-10, zhao2025mechanisticadvancesin pages 2-4, panahi2023erstressinduced pages 11-14, menendezvalladares2024asearchfor pages 7-11) |
| Cell types | Vascular smooth muscle cell (VSMC) (CL:0000187); Pericyte (CL:0000669); Endothelial cell (CL:0000115); Oligodendrocyte (CL:0000128); Microglia (CL:0000129) | CL:0000187; CL:0000669; CL:0000115; CL:0000128; CL:0000129 | Primary cellular targets: mural cell (VSMC/pericyte) degeneration drives arteriopathy; endothelial dysfunction / BBB impairment; oligodendrocyte vulnerability → myelin loss; microglial/perivascular macrophage activation associated with vessel lesions. | (dupre2024proteinaggregatescontaining pages 1-2, zhao2025mechanisticadvancesin pages 2-4, muino2021genomewidetranscriptomestudy pages 1-2, hack2023threetieredegfrdomain pages 7-10, panahi2023erstressinduced pages 11-14) |
| Anatomical locations | Cerebral small artery / arteriole (UBERON:0001621); White matter (UBERON:0002436); Anterior temporal pole (UBERON:0001871); External capsule (UBERON:0002310); Skin dermal arteriole (UBERON:0002067) | UBERON:0001621; UBERON:0002436; UBERON:0001871; UBERON:0002310; UBERON:0002067 | Sites of pathological NOTCH3 ECD / GOM deposition and clinical imaging biomarkers: cerebral arterioles (histopathology), characteristic WMH topography (anterior temporal pole / external capsule) and skin biopsies for NOTCH3/GOM. | (mizuta2024progresstoclarify pages 2-4, hack2023threetieredegfrdomain pages 7-10, muino2021genomewidetranscriptomestudy pages 1-2, dupre2024proteinaggregatescontaining pages 1-2, zhao2025mechanisticadvancesin pages 2-4) |
| Biological processes (GO) | Notch signaling pathway (GO:0007219); Extracellular matrix organization (GO:0030198); Protein aggregation / misfolding (GO:0006457); Complement activation, alternative pathway (GO:0006957); Inflammatory response (GO:0006954); Regulation of blood–brain barrier permeability (GO:1903764); Myelination (GO:0042552); Autophagy (GO:0006914) | GO:0007219; GO:0030198; GO:0006457; GO:0006957; GO:0006954; GO:1903764; GO:0042552; GO:0006914 | Dysregulated pathways in CADASIL: mutant NOTCH3 ECD aggregation and aberrant NOTCH3 processing; ECM remodeling and sequestration of matrisome proteins; complement-mediated vascular inflammation; BBB breakdown; oligodendrocyte/myelin injury and altered autophagy/vesicular pathways. | (zhao2025mechanisticadvancesin pages 2-4, dupre2024proteinaggregatescontaining pages 1-2, panahi2023erstressinduced pages 11-14, menendezvalladares2024asearchfor pages 7-11, muino2021genomewidetranscriptomestudy pages 1-2, song2025rolesofneuroimaging pages 5-6) |
| Cellular components | Extracellular region (GO:0005576); Basement membrane (GO:0005604); Plasma membrane (GO:0005886); GOM deposits (extracellular aggregates; no GO ID); Smooth muscle cell layer (no GO ID); Blood–brain barrier (GO:0060627) | GO:0005576; GO:0005604; GO:0005886; (GOM: extracellular aggregates); (SMC layer: n/a); GO:0060627 | Localization of pathological deposits and structural targets: NOTCH3 ECD and ECM co-aggregates localize to vessel extracellular region / basement membrane (GOM); vascular SMC layer is degenerating; NVU/BBB components show dysfunction. | (dupre2024proteinaggregatescontaining pages 1-2, zhao2025mechanisticadvancesin pages 2-4, panahi2023erstressinduced pages 11-14, mizuta2024progresstoclarify pages 2-4) |
| Phenotypes (HP) | Migraine with aura (HP:0002076); Subcortical ischemic strokes (HP:0007303); Cognitive impairment (HP:0100543); Apathy (HP:0000741); White matter hyperintensities (HP:0031258); Lacunes (HP:0012543); Cerebral microbleeds (HP:0031881) | HP:0002076; HP:0007303; HP:0100543; HP:0000741; HP:0031258; HP:0012543; HP:0031881 | Core clinical and imaging manifestations of CADASIL across disease stages: early migraine, mid-life recurrent lacunar strokes, progressive cognitive decline and characteristic MRI lesions (WMH, anterior temporal pole/external capsule, lacunes, microbleeds). | (mizuta2024progresstoclarify pages 2-4, muino2021genomewidetranscriptomestudy pages 1-2, hack2023threetieredegfrdomain pages 1-2, hack2023threetieredegfrdomain pages 7-10, song2025rolesofneuroimaging pages 5-6) |
| Chemicals / Biomarkers | Neurofilament light (NfL) — fluid neuronal-injury marker (no CHEBI ID listed); Homocysteine (CHEBI:17230); hs-CRP (CHEBI:35644); RSPO1 / FGF-19 (proteomic candidates); K-7174 (experimental VCAM1 blocker) | — (NfL); CHEBI:17230; CHEBI:35644; (RSPO1/FGF19: proteins); (K-7174: experimental compound) | Candidate and validated biomarkers: plasma/serum proteomic signals (RSPO1, FGF-19, others) and sNfL for neuronal injury; inflammatory markers (hs-CRP, homocysteine) appear in CSVD studies; experimental compounds (K-7174) modulate endothelial/BBB pathways in models. | (menendezvalladares2024asearchfor pages 7-11, song2025rolesofneuroimaging pages 5-6, menendezvalladares2024asearchfor pages 17-18, panahi2023erstressinduced pages 11-14) |


*Table: A compact, ontology-mapped table that summarizes key genes/proteins, cell types, anatomical sites, biological processes, cellular components, phenotypes and biomarkers in CADASIL pathophysiology with supporting recent evidence citations.*

3) Biological processes (for GO annotation)
- Notch signaling and receptor processing (GO:0007219): mutant NOTCH3 ECD misfolding and abnormal proteolysis/fragmentation; many CADASIL variants do not markedly reduce canonical signaling in vivo, consistent with neomorphic aggregation toxicity (dupre2024proteinaggregatescontaining pages 1-2, hack2023threetieredegfrdomain pages 14-15). 
- Protein aggregation/misfolding and extracellular matrix organization (GO:0006457; GO:0030198): NOTCH3 ECD aggregation, GOM formation, recruitment of matrisome proteins (TIMP3, VTN, LTBP-1, CLU) (zhao2025mechanisticadvancesin pages 2-4, hack2023threetieredegfrdomain pages 14-15). 
- Complement activation, alternative pathway (GO:0006957) and inflammatory response (GO:0006954): Factor B, C3d, C5-9 deposition; ICAM1/IL6 upregulation and endothelial activation (panahi2023erstressinduced pages 11-14, panahi2023erstressinduced pages 18-19). 
- Regulation of blood–brain barrier permeability (GO:1903764) and neurovascular unit dysfunction: evidence for endothelial inflammatory signaling and barrier compromise (panahi2023erstressinduced pages 11-14). 
- Myelination (GO:0042552), autophagy/vesicular machinery (GO:0006914): white matter pathology and transcriptomic enrichment for autophagy/vesicular and vascular development terms in CADASIL skin and brain tissues (muino2021genomewidetranscriptomestudy pages 1-2).

4) Cellular components
- Extracellular region and basement membrane (GO:0005576; GO:0005604): sites of NOTCH3 ECD and ECM co-aggregation (GOM) around VSMCs/pericytes (mizuta2024progresstoclarify pages 2-4, zhao2025mechanisticadvancesin pages 2-4). 
- Blood–brain barrier (GO:0060627): endothelial activation and complement-linked perivascular injury (panahi2023erstressinduced pages 11-14). 
- Vascular smooth muscle cell layer: locus of mural degeneration and arterial remodeling (dupre2024proteinaggregatescontaining pages 1-2).

5) Disease progression: sequence from molecular trigger to phenotype
- Initiation: NOTCH3 EGFr cysteine-altering variant → N3ECD misfolding and altered proteolysis → extracellular accumulation in small-artery walls, with co-aggregation of wild-type N3ECD (dupre2024proteinaggregatescontaining pages 1-2).
- Propagation: Recruitment/sequestration of matrisome proteins (TIMP3, VTN; HTRA1 LOF signature) → ECM remodeling and fibrosis; mural-cell dysfunction and loss (VSMC/pericyte) (hack2023threetieredegfrdomain pages 14-15, zhao2025mechanisticadvancesin pages 2-4). 
- Inflammatory amplification: ER stress and mural cell–to–endothelium signaling (ICAM1/IL6), activation of alternative complement pathway (C3d, Factor B, C5–9) at the vessel wall; BBB involvement (panahi2023erstressinduced pages 11-14, panahi2023erstressinduced pages 18-19). 
- Tissue injury: Chronic hypoperfusion, small infarcts/lacunes, myelin injury, and susceptibility to microbleeds/iron deposition; progressive white-matter network damage (hack2023threetieredegfrdomain pages 7-10, mizuta2024progresstoclarify pages 2-4). 
- Clinical emergence: Migraine with aura in early adulthood → recurrent lacunar strokes (often midlife), cognitive decline (executive dysfunction), mood/apathy; imaging shows characteristic WMH patterns (temporal pole/external capsule), lacunes, and microbleeds (mizuta2024progresstoclarify pages 2-4, mizuta2024progresstoclarify pages 1-2).

6) Phenotypic manifestations and their mechanistic links
- Migraine with aura (common prodrome), transient ischemic attacks and subcortical ischemic strokes, mood disturbance/apathy, and progressive cognitive impairment with prominent executive dysfunction are typical; these manifestations track with small-artery arteriopathy, white-matter ischemia/myelin loss, and microvascular fragility (mizuta2024progresstoclarify pages 2-4, mizuta2024progresstoclarify pages 1-2). URL: https://doi.org/10.3390/biom14010127 (Jan 2024).
- Microbleeds/iron deposition reflect microvascular wall injury and perivascular leakage (neuropathology) (hack2023threetieredegfrdomain pages 7-10). URL: https://doi.org/10.1093/jnen/nlad004 (Jan 2023).

Recent developments (2023–2024 priority)
- Wild-type and mutant NOTCH3 ECD co-aggregation as a key disease driver with dose sensitivity to wild-type NOTCH3, supporting NOTCH3-lowering strategies (Dupré et al., 2024 JCI) (dupre2024proteinaggregatescontaining pages 1-2, dupre2024proteinaggregatescontaining pages 5-6). URL: https://doi.org/10.1172/jci175789 (Feb 2024).
- EGFr domain–based genotype risk stratification refined: high-risk domains include 1–6 and newly 8, 11, and 26; vascular NOTCH3 aggregation load correlates with domain risk and clinical/MRI severity across cohorts (Hack et al., 2023 Brain) (hack2023threetieredegfrdomain pages 1-2, hack2023threetieredegfrdomain pages 7-10). URL: https://doi.org/10.1093/brain/awac486 (Dec 2023).
- Vessel-wall immunopathology complementary to aggregation: ER-stress–linked mural cell activation, endothelial pro-inflammatory signaling, and alternative complement activation documented in patient tissues and mutant VSMCs (Panahi et al., 2023) (panahi2023erstressinduced pages 11-14, panahi2023erstressinduced pages 18-19). URL: https://doi.org/10.1186/s40478-023-01558-1 (May 2023).
- Proteomic plasma signatures point to fibrosis/matrisome and inflammatory pathways (including complement) as systemic reflections of CADASIL biology (Menéndez‑Valladares et al., 2024 J Clin Med) (menendezvalladares2024asearchfor pages 7-11, menendezvalladares2024asearchfor pages 17-18). URL: https://doi.org/10.3390/jcm13113138 (May 2024).

Current applications and real-world implementations
- Molecular diagnosis: Sequencing of NOTCH3 remains the standard. EGFr domain mapping informs variant interpretation and prognostication; high-risk EGFr domains track with NOTCH3 aggregation load and higher odds of stroke and greater WMH/lacunar burden (odds ratio for stroke 10.81 for HR-EGFr vs LR; P-values significant across imaging metrics) (hack2023threetieredegfrdomain pages 7-10, hack2023threetieredegfrdomain pages 1-2). URL: https://doi.org/10.1093/brain/awac486 (Dec 2023).
- Pathology/biopsy: Skin biopsy with N3ECD immunostaining and electron microscopy for GOM is supportive in challenging cases. Reported sensitivity ranges roughly 45–96% and specificity ~100% for NOTCH3 ECD immunostaining in prior series; GOM detection remains a definitive hallmark (supporting review and transcriptomic study) (muino2021genomewidetranscriptomestudy pages 1-2, mizuta2024progresstoclarify pages 2-4). URL: https://doi.org/10.1038/s41598-021-86349-1 (Jun 2021); https://doi.org/10.3390/biom14010127 (Jan 2024).
- Imaging biomarkers: Characteristic MRI shows WMH in anterior temporal poles and external capsule, plus lacunes and microbleeds; temporal-pole WMH has high sensitivity/specificity in CADASIL (review) (mizuta2024progresstoclarify pages 2-4). URL: https://doi.org/10.3390/biom14010127 (Jan 2024).
- Fluid biomarkers: Neurofilament light (NfL) is an informative neuronal-injury marker in CSVD cohorts, associating with processing speed and outcomes, and is increasingly used alongside imaging for disease monitoring in small-vessel disease contexts (review) (song2025rolesofneuroimaging pages 5-6). URL: https://doi.org/10.3389/fneur.2025.1483842 (May 2025).

Expert opinions and analyses
- Aggregation-centric mechanism with matrisome sequestration and a “HTRA1 loss-of-function profile” in CADASIL vessels has been highlighted in recent high-impact and consensus-driven analyses (2023–2024) (hack2023threetieredegfrdomain pages 14-15). URL: https://doi.org/10.1093/brain/awac486 (Dec 2023).
- Contemporary reviews emphasize that while canonical NOTCH3 signaling defects may occur for specific variants, the bulk of evidence in CADASIL points toward extracellular N3ECD aggregation and co-aggregate toxicity as a primary driver, with downstream mural cell loss and vascular fibrosis (mizuta2024progresstoclarify pages 1-2). URL: https://doi.org/10.3390/biom14010127 (Jan 2024).
- Vessel-wall inflammation/complement activation is increasingly recognized as a potential therapeutic axis in CADASIL arteriopathy (panahi2023erstressinduced pages 11-14, panahi2023erstressinduced pages 18-19). URL: https://doi.org/10.1186/s40478-023-01558-1 (May 2023).

Relevant statistics and data (recent)
- Genotype–phenotype severity by EGFr domain: High-risk EGFr domains (1–6, 8, 11, 26) confer substantially elevated stroke risk (OR 10.81, 95% CI 5.46–21.37) and higher diffusion MRI injury (PSMD), WMH volume, and lacune volume compared with low-risk domains; NOTCH3 aggregation scores are higher in HR-EGFr and correlate with NVFOR (P = 0.003) (hack2023threetieredegfrdomain pages 7-10, hack2023threetieredegfrdomain pages 1-2). URL: https://doi.org/10.1093/brain/awac486 (Dec 2023).
- Vessel-wall complement deposition: Immunohistochemistry shows intense C3d and Factor B and MAC (C5–9) staining in approximately two-thirds to three-quarters of CADASIL arterioles/microvessels, indicating alternative pathway activation (panahi2023erstressinduced pages 11-14). URL: https://doi.org/10.1186/s40478-023-01558-1 (May 2023).
- Microbleed neuropathology: CADASIL brains have significantly increased hemosiderin/iron deposition across cortex, white matter, basal ganglia, and cerebellum relative to controls; perivascular hemosiderin is prominent around small/medium arterioles (Magaki et al., 2023) (hack2023threetieredegfrdomain pages 7-10). URL: https://doi.org/10.1093/jnen/nlad004 (Jan 2023).

Evidence quotations (selected)
- “Protein aggregates containing wild-type and mutant NOTCH3 are major drivers of arterial pathology in CADASIL,” with co-aggregation and gene-dose effects on pathology (dupre2024proteinaggregatescontaining pages 1-2). URL: https://doi.org/10.1172/jci175789 (Feb 2024).
- “Abnormal recruitment of extracellular matrix proteins by excess Notch3 ECD” and a “HTRA1 loss-of-function profile” in CADASIL-related vessels underline matrisome dysregulation (hack2023threetieredegfrdomain pages 14-15). URL: https://doi.org/10.1093/brain/awac486 (Dec 2023).
- “Immunohistochemical staining revealed intense immunoreactivity of complement factors B, C3d and C5-9” in CADASIL arterioles; NOTCH3 Arg133Cys VSMCs showed markedly increased ICAM-1 and IL-6 (panahi2023erstressinduced pages 11-14). URL: https://doi.org/10.1186/s40478-023-01558-1 (May 2023).
- “Temporal pole and external capsule” WMH are characteristic CADASIL MRI hallmarks; GOM is a “validated pathological hallmark,” with N3ECD localized in GOM on VSMCs (mizuta2024progresstoclarify pages 2-4). URL: https://doi.org/10.3390/biom14010127 (Jan 2024).

Gene/protein annotations and ontology terms
- HGNC: NOTCH3 (7881); HTRA1 (5325); TIMP3 (11820); VTN (12683); CLU (2095); LTBP1 (6718); ICAM1 (5344); IL6 (6018); C3 (1330); CFB (822). Mapped biological processes/components as in the embedded artifact (hack2023threetieredegfrdomain pages 14-15, zhao2025mechanisticadvancesin pages 2-4, panahi2023erstressinduced pages 11-14).

Phenotype associations (HP terms)
- HP:0002076 (Migraine with aura); HP:0007303 (Subcortical ischemic stroke); HP:0100543 (Cognitive impairment); HP:0000741 (Apathy); HP:0031258 (White matter hyperintensities); HP:0012543 (Lacunes); HP:0031881 (Cerebral microbleeds) (mizuta2024progresstoclarify pages 2-4, hack2023threetieredegfrdomain pages 7-10).

Cell type involvement (CL terms)
- CL:0000187 (VSMC), CL:0000669 (Pericyte), CL:0000115 (Endothelial cell), CL:0000128 (Oligodendrocyte), CL:0000129 (Microglia) (dupre2024proteinaggregatescontaining pages 1-2, zhao2025mechanisticadvancesin pages 2-4, panahi2023erstressinduced pages 11-14, hack2023threetieredegfrdomain pages 7-10).

Anatomical locations (UBERON)
- UBERON:0001621 (Cerebral small artery/arteriole), UBERON:0002436 (White matter), UBERON:0001871 (Temporal pole), UBERON:0002310 (External capsule), UBERON:0002067 (Dermal arteriole) (mizuta2024progresstoclarify pages 2-4, zhao2025mechanisticadvancesin pages 2-4).

Chemical entities (CHEBI)
- CHEBI:17230 (Homocysteine), CHEBI:35644 (C-reactive protein, high-sensitivity assays used), alongside protein biomarkers (NfL) used clinically in CSVD contexts (song2025rolesofneuroimaging pages 5-6, menendezvalladares2024asearchfor pages 7-11).

Diagnostic and biomarker notes with implementation details
- Genetic testing is definitive when a pathogenic NOTCH3 variant is identified; domain-based risk stratification (HR vs MR/LR EGFr) refines prognosis and can inform counseling (hack2023threetieredegfrdomain pages 7-10, hack2023threetieredegfrdomain pages 1-2).
- Skin biopsy with N3ECD immunostaining and/or EM for GOM is appropriate in atypical presentations or VUS scenarios; reported sensitivity 45–96% and specificity ~100% for N3ECD immunostaining (muino2021genomewidetranscriptomestudy pages 1-2). URL: https://doi.org/10.1038/s41598-021-86349-1 (Jun 2021).
- MRI hallmark distribution (temporal poles/external capsule), lacunes, microbleeds guide diagnosis and staging; neuropathological studies confirm microbleed substrates (mizuta2024progresstoclarify pages 2-4, hack2023threetieredegfrdomain pages 7-10).
- Plasma/serum proteomics (matrisome/inflammation) and NfL are being explored and can complement imaging in disease monitoring (menendezvalladares2024asearchfor pages 7-11, song2025rolesofneuroimaging pages 5-6).

References (URLs and dates in-line above; all citations correspond to context IDs)
- Dupré et al., 2024, Journal of Clinical Investigation (dupre2024proteinaggregatescontaining pages 1-2, dupre2024proteinaggregatescontaining pages 5-6). 
- Hack et al., 2023, Brain (hack2023threetieredegfrdomain pages 7-10, hack2023threetieredegfrdomain pages 14-15, hack2023threetieredegfrdomain pages 1-2). 
- Panahi et al., 2023, Acta Neuropathologica Communications (panahi2023erstressinduced pages 11-14, panahi2023erstressinduced pages 18-19). 
- Mizuta et al., 2024, Biomolecules (mizuta2024progresstoclarify pages 1-2, mizuta2024progresstoclarify pages 2-4). 
- Magaki et al., 2023, Journal of Neuropathology and Experimental Neurology (hack2023threetieredegfrdomain pages 7-10). 
- Menéndez‑Valladares et al., 2024, Journal of Clinical Medicine (menendezvalladares2024asearchfor pages 7-11, menendezvalladares2024asearchfor pages 17-18). 
- Muiño et al., 2021, Scientific Reports (muino2021genomewidetranscriptomestudy pages 1-2). 
- Song et al., 2025, Frontiers in Neurology (song2025rolesofneuroimaging pages 5-6).

Concluding perspective
Converging 2023–2024 evidence supports a mechanistic cascade in which cysteine-altering NOTCH3 variants drive extracellular N3ECD aggregation (including wild-type co-aggregation), recruitment/sequestration of ECM proteins with matrisome/HTRA1 dysregulation, mural cell loss, and vessel-wall immunopathology (endothelial inflammation and alternative-pathway complement), culminating in white-matter ischemic injury and microbleeds. Genotype (EGFr domain) strongly modulates aggregation load and clinical/imaging severity. These data refine diagnosis and stratification, and suggest therapeutic entry points such as NOTCH3-lowering, matrix/co-aggregate disruption, and vessel-wall immunomodulation (dupre2024proteinaggregatescontaining pages 1-2, hack2023threetieredegfrdomain pages 7-10, panahi2023erstressinduced pages 11-14).

References

1. (mizuta2024progresstoclarify pages 1-2): Ikuko Mizuta, Yumiko Nakao-Azuma, Hideki Yoshida, Masamitsu Yamaguchi, and Toshiki Mizuno. Progress to clarify how notch3 mutations lead to cadasil, a hereditary cerebral small vessel disease. Biomolecules, 14:127, Jan 2024. URL: https://doi.org/10.3390/biom14010127, doi:10.3390/biom14010127. This article has 18 citations and is from a poor quality or predatory journal.

2. (mizuta2024progresstoclarify pages 2-4): Ikuko Mizuta, Yumiko Nakao-Azuma, Hideki Yoshida, Masamitsu Yamaguchi, and Toshiki Mizuno. Progress to clarify how notch3 mutations lead to cadasil, a hereditary cerebral small vessel disease. Biomolecules, 14:127, Jan 2024. URL: https://doi.org/10.3390/biom14010127, doi:10.3390/biom14010127. This article has 18 citations and is from a poor quality or predatory journal.

3. (dupre2024proteinaggregatescontaining pages 1-2): Nicolas Dupré, Florian Gueniot, Valérie Domenga-Denier, Virginie Dubosclard, Christelle Nilles, David Hill-Eubanks, Christelle Morgenthaler-Roth, Mark T. Nelson, Céline Keime, Lydia Danglot, and Anne Joutel. Protein aggregates containing wild-type and mutant notch3 are major drivers of arterial pathology in cadasil. The Journal of Clinical Investigation, Feb 2024. URL: https://doi.org/10.1172/jci175789, doi:10.1172/jci175789. This article has 31 citations.

4. (dupre2024proteinaggregatescontaining pages 5-6): Nicolas Dupré, Florian Gueniot, Valérie Domenga-Denier, Virginie Dubosclard, Christelle Nilles, David Hill-Eubanks, Christelle Morgenthaler-Roth, Mark T. Nelson, Céline Keime, Lydia Danglot, and Anne Joutel. Protein aggregates containing wild-type and mutant notch3 are major drivers of arterial pathology in cadasil. The Journal of Clinical Investigation, Feb 2024. URL: https://doi.org/10.1172/jci175789, doi:10.1172/jci175789. This article has 31 citations.

5. (hack2023threetieredegfrdomain pages 14-15): Remco J Hack, Gido Gravesteijn, Minne N Cerfontaine, Mark A Santcroos, Laura Gatti, Anna Kopczak, Anna Bersano, Marco Duering, Julie W Rutten, and Saskia A J Lesnik Oberstein. Three-tiered egfr domain risk stratification for individualized notch3-small vessel disease prediction. Brain, 146:2913-2927, Dec 2023. URL: https://doi.org/10.1093/brain/awac486, doi:10.1093/brain/awac486. This article has 48 citations and is from a highest quality peer-reviewed journal.

6. (zhao2025mechanisticadvancesin pages 2-4): Ying Zhao, YaRu Lu, FengYu Wang, YaDan Wang, YaQiong Li, RuiHua Sun, JunKui Shang, Chao Jiang, and Jiewen Zhang. Mechanistic advances in factors influencing phenotypic variability in cerebral autosomal dominant arteriopathy with subcortical infarcts and leukoencephalopathy: a review. Frontiers in Neurology, May 2025. URL: https://doi.org/10.3389/fneur.2025.1573052, doi:10.3389/fneur.2025.1573052. This article has 1 citations and is from a peer-reviewed journal.

7. (menendezvalladares2024asearchfor pages 17-18): Paloma Menéndez-Valladares, Rosa Acevedo Aguilera, David Núñez-Jurado, Cristina López Azcárate, Ana María Domínguez Mayoral, Alejandro Fernández-Vega, Soledad Pérez-Sánchez, Marcel Lamana Vallverdú, María Isabel García-Sánchez, María Morales Bravo, Teresa Busquier, and Joan Montaner. A search for new biological pathways in cerebral autosomal dominant arteriopathy with subcortical infarcts and leukoencephalopathy by proteomic research. Journal of Clinical Medicine, 13:3138, May 2024. URL: https://doi.org/10.3390/jcm13113138, doi:10.3390/jcm13113138. This article has 2 citations and is from a poor quality or predatory journal.

8. (menendezvalladares2024asearchfor pages 7-11): Paloma Menéndez-Valladares, Rosa Acevedo Aguilera, David Núñez-Jurado, Cristina López Azcárate, Ana María Domínguez Mayoral, Alejandro Fernández-Vega, Soledad Pérez-Sánchez, Marcel Lamana Vallverdú, María Isabel García-Sánchez, María Morales Bravo, Teresa Busquier, and Joan Montaner. A search for new biological pathways in cerebral autosomal dominant arteriopathy with subcortical infarcts and leukoencephalopathy by proteomic research. Journal of Clinical Medicine, 13:3138, May 2024. URL: https://doi.org/10.3390/jcm13113138, doi:10.3390/jcm13113138. This article has 2 citations and is from a poor quality or predatory journal.

9. (panahi2023erstressinduced pages 11-14): Mahmod Panahi, Yoshiki Hase, Xavier Gallart-Palau, Sumonto Mitra, Atsushi Watanabe, Roger C Low, Yumi Yamamoto, Diego Sepulveda-Falla, Atticus H Hainsworth, Masafumi Ihara, Siu Kwan Sze, Matti Viitanen, Homira Behbahani, and Raj N Kalaria. Er stress induced immunopathology involving complement in cadasil: implications for therapeutics. Acta Neuropathologica Communications, May 2023. URL: https://doi.org/10.1186/s40478-023-01558-1, doi:10.1186/s40478-023-01558-1. This article has 17 citations and is from a peer-reviewed journal.

10. (panahi2023erstressinduced pages 18-19): Mahmod Panahi, Yoshiki Hase, Xavier Gallart-Palau, Sumonto Mitra, Atsushi Watanabe, Roger C Low, Yumi Yamamoto, Diego Sepulveda-Falla, Atticus H Hainsworth, Masafumi Ihara, Siu Kwan Sze, Matti Viitanen, Homira Behbahani, and Raj N Kalaria. Er stress induced immunopathology involving complement in cadasil: implications for therapeutics. Acta Neuropathologica Communications, May 2023. URL: https://doi.org/10.1186/s40478-023-01558-1, doi:10.1186/s40478-023-01558-1. This article has 17 citations and is from a peer-reviewed journal.

11. (hack2023threetieredegfrdomain pages 7-10): Remco J Hack, Gido Gravesteijn, Minne N Cerfontaine, Mark A Santcroos, Laura Gatti, Anna Kopczak, Anna Bersano, Marco Duering, Julie W Rutten, and Saskia A J Lesnik Oberstein. Three-tiered egfr domain risk stratification for individualized notch3-small vessel disease prediction. Brain, 146:2913-2927, Dec 2023. URL: https://doi.org/10.1093/brain/awac486, doi:10.1093/brain/awac486. This article has 48 citations and is from a highest quality peer-reviewed journal.

12. (muino2021genomewidetranscriptomestudy pages 1-2): Elena Muiño, Olga Maisterra, Joan Jiménez-Balado, Natalia Cullell, Caty Carrera, Nuria P Torres-Aguila, Jara Cárcel-Márquez, Cristina Gallego-Fábrega, Miquel Lledós, Jonathan González-Sánchez, Ferran Olmos-Alpiste, Eva Espejo, Álvaro March, Ramón Pujol, Ana Rodríguez-Campello, Gemma Romeral, Jurek Krupinski, Joan Martí-Fábregas, Joan Montaner, Jaume Roquer, and Israel Fernández-Cadenas. Genome-wide transcriptome study in skin biopsies reveals an association of e2f4 with cadasil and cognitive impairment. Scientific Reports, Jun 2021. URL: https://doi.org/10.1038/s41598-021-86349-1, doi:10.1038/s41598-021-86349-1. This article has 12 citations and is from a peer-reviewed journal.

13. (song2025rolesofneuroimaging pages 5-6): Xiaoqian Song, Chenyang Jin, Moxin Luan, and Xueping Zheng. Roles of neuroimaging markers and biomarkers in cerebral small vessel disease and their associations with cognitive function. Frontiers in Neurology, May 2025. URL: https://doi.org/10.3389/fneur.2025.1483842, doi:10.3389/fneur.2025.1483842. This article has 2 citations and is from a peer-reviewed journal.

14. (hack2023threetieredegfrdomain pages 1-2): Remco J Hack, Gido Gravesteijn, Minne N Cerfontaine, Mark A Santcroos, Laura Gatti, Anna Kopczak, Anna Bersano, Marco Duering, Julie W Rutten, and Saskia A J Lesnik Oberstein. Three-tiered egfr domain risk stratification for individualized notch3-small vessel disease prediction. Brain, 146:2913-2927, Dec 2023. URL: https://doi.org/10.1093/brain/awac486, doi:10.1093/brain/awac486. This article has 48 citations and is from a highest quality peer-reviewed journal.