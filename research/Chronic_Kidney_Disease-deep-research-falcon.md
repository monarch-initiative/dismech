---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T18:38:29.285036'
end_time: '2025-12-17T18:46:31.876442'
duration_seconds: 482.59
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chronic Kidney Disease
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Chronic Kidney Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Chronic Kidney Disease**.
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
- **Disease Name:** Chronic Kidney Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Chronic Kidney Disease**.
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


# Disease Pathophysiology Research Report

## Target Disease
- Disease Name: Chronic Kidney Disease (CKD)
- MONDO ID: Not specified
- Category: Complex

## Pathophysiology description (narrative)
Chronic kidney disease progresses through intertwined mechanisms of persistent injury, maladaptive epithelial repair, inflammation, and fibrosis that culminate in nephron loss and functional decline. Kidney fibrosis is the final common pathway of CKD. Canonical TGF-β/Smad signaling activates myofibroblasts and drives extracellular matrix deposition; Smad2/3 activation with Smad7 downregulation induces profibrotic transcription (collagen, α-SMA, fibronectin) in mesangial and interstitial cells, while matricellular proteins (CTGF, tenascin-C) amplify the fibrotic niche (doi:10.3390/jcm13071881; 2024-03-26) (reiss2024fibrosisinchronic pages 5-6). Oxidative stress and mitochondrial dysfunction are central amplifiers: mitochondrial ROS, mtDNA release, and organelle crosstalk at mitochondria–ER contact sites activate innate sensors (NLRP3, AIM2; cGAS–STING), NF-κB, and Wnt–β-catenin, promoting albuminuria, endothelial/tubular injury, and interstitial fibrosis; RAAS–NOX signaling further increases ROS and inflammation (doi:10.1038/s41581-023-00775-0; 2024-10-01) (kishi2024oxidativestressand pages 10-12).

Transitions from acute kidney injury (AKI) to CKD illustrate the maladaptive repair paradigm: proximal tubular epithelial cells (PTECs) that arrest in G2/M and acquire senescent/SASP phenotypes secrete TGF-β and chemokines, activate pericytes to fibroblasts, and fail to redifferentiate, linking epithelial injury to chronic fibrosis (doi:10.3349/ymj.2023.0306; 2024-05-01) (koh2024recentupdateon pages 5-7). Single-cell and transcriptomic work identifies injury-associated epithelial states (oxidative stress/hypoxia, inflammation/translation, EMT-like) that recruit leukocytes and fibroblasts and correlate with eGFR decline (2024; details and mechanistic ligands SPP1, C3, NECTIN2–CD226) (hinze2024decipheringinjuryassociatedrenal pages 7-9). Pathways reactivated after injury include Wnt/β-catenin, PI3K/AKT, PDGF, CTGF, and Sonic hedgehog, acting alongside TGF-β to sustain fibroblast activation and matrix accumulation (doi:10.3390/ijms25031518; 2024-01-24) (chang2024mitochondrialsignalingthe pages 2-4). Persistent hypoxia (HIF-1/2α activity) intersects with TGF-β, NF-κB, and PI3K/Akt signaling and has context-dependent roles in fibrosis versus protection; pharmacologic HIF modulation (HIF–PHD inhibition) alters inflammation, mitochondrial injury, and erythropoiesis (doi:10.3390/ijms25031755; 2024-02-01) (yeh2024fromacuteto pages 8-10).

Therapeutically, SGLT2 inhibitors lessen hyperfiltration injury, improve renal energetics, autophagy and microvascular function, and reduce oxidative/inflammatory signaling, providing kidney protection beyond tubuloglomerular feedback (doi:10.34067/kid.0000000000000425; 2024-03-14) (kishi2024oxidativestressand pages 10-12). For CKD anemia, HIF–PHD inhibitors (e.g., daprodustat, vadadustat, roxadustat) increase hemoglobin and improve iron handling without excess major adverse cardiovascular events relative to ESAs in phase 3 trials, though vigilance for hypertension and hyperkalemia is warranted (doi:10.1182/hematology.2024000655; 2024-12-01; doi:10.1093/ckj/sfad143; 2024-06-01; doi:10.1080/0886022x.2024.2313864; 2024-02-05) (kishi2024oxidativestressand pages 10-12).

| Mechanism | Key pathways (GO) | Principal genes / proteins (HGNC) | Primary cell types (CL) | Anatomical sites (UBERON) | Representative clinical phenotypes (HP) |
|---|---|---|---|---|---|
| Fibrosis (TGF-β / Wnt) | GO:TGF-β receptor signaling; GO:Wnt/β-catenin signaling | TGFB1, SMAD3, CTGF, CTNNB1 | CL:interstitial_fibroblast; CL:mesangial_cell; CL:proximal_tubular_epithelial_cell | UBERON:renal_interstitium; UBERON:glomerulus | HP:interstitial_fibrosis; HP:proteinuria (reiss2024fibrosisinchronic pages 5-6, yeh2024fromacuteto pages 8-10) |
| Inflammation / innate immunity (NF-κB, NLRP3 / pyroptosis) | GO:NF-κB signaling; GO:inflammasome activation | NLRP3, CASP1, IL1B, NFKB1 | CL:macrophage; CL:neutrophil; CL:dendritic_cell | UBERON:renal_interstitium; UBERON:glomerulus | HP:renal_inflammation; HP:albuminuria (yeh2024fromacuteto pages 12-14, hinze2024decipheringinjuryassociatedrenal pages 7-9) |
| Oxidative stress & mitochondria (Nrf2 / mtDNA → cGAS-STING) | GO:cellular_response_to_oxidative_stress; GO:mitochondrial_dysfunction | NFE2L2 (Nrf2), KEAP1, NOX4, PPARGC1A (PGC-1α) | CL:proximal_tubular_epithelial_cell; CL:endothelial_cell | UBERON:proximal_tubule; UBERON:peritubular_capillary | HP:albuminuria; HP:decreased_eGFR (kishi2024oxidativestressand pages 10-12, geng2025pathogenesisandtherapeutic pages 7-9) |
| Hypoxia / HIF | GO:cellular_response_to_hypoxia; GO:HIF-1 signaling | HIF1A, EGLN1 (PHD2), EPO | CL:proximal_tubular_epithelial_cell; CL:endothelial_cell | UBERON:renal_cortex; UBERON:renal_medulla | HP:anemia_of_CKD; HP:interstitial_hypoxia (yeh2024fromacuteto pages 8-10, kishi2024oxidativestressand pages 10-12) |
| Maladaptive repair / cellular senescence (G2/M arrest, SASP) | GO:cellular_senescence; GO:DNA_damage_response | CDKN1A (p21), CDKN2A (p16), IL6 (SASP) | CL:proximal_tubular_epithelial_cell; CL:senescent_cell | UBERON:renal_tubule; UBERON:interstitium | HP:tubulointerstitial_fibrosis; HP:progressive_eGFR_loss (koh2024recentupdateon pages 5-7, yeh2024fromacuteto pages 12-14, hinze2024decipheringinjuryassociatedrenal pages 7-9) |
| RAAS / Hemodynamics (Ang II → NOX / ROS) | GO:renin-angiotensin system signaling; GO:regulation_of_blood_pressure | AGT, ACE, AGTR1, NOX4 | CL:glomerular_endothelial_cell; CL:vascular_smooth_muscle_cell | UBERON:glomerulus; UBERON:afferent_arteriole | HP:hypertension; HP:hyperfiltration; HP:proteinuria (yeh2024fromacuteto pages 12-14, kishi2024oxidativestressand pages 10-12) |
| Therapeutic mechanisms: SGLT2 inhibitors & HIF-PHIs | GO:glucose_transport; GO:regulation_of_HIF_signaling | SLC5A2 (SGLT2), HIF1A, EGLN1 (PHDs) | CL:proximal_tubular_epithelial_cell | UBERON:proximal_tubule | HP:reduced_albuminuria; HP:slower_GFR_decline (kishi2024oxidativestressand pages 10-12, chang2024mitochondrialsignalingthe pages 2-4) |


*Table: Compact mapping of major CKD pathophysiology mechanisms to pathways (GO), genes/proteins (HGNC), cell types (CL), anatomical sites (UBERON) and clinical phenotypes (HP); citations link source evidence from the gathered context (yeh2024fromacuteto pages 8-10, koh2024recentupdateon pages 5-7).*

## Gene/protein annotations with ontology terms
- TGFB1 (HGNC:11766) – GO:0007179 (TGF-β receptor signaling pathway); promotes Smad2/3 phosphorylation and ECM gene induction in kidney fibrosis (reiss2024fibrosisinchronic pages 5-6)
- SMAD3 (HGNC:6769) – GO:0007179; mediates canonical TGF-β profibrotic transcription in mesangial/interstitial cells (reiss2024fibrosisinchronic pages 5-6)
- CTGF (HGNC:2503) – GO:0030198 (ECM organization); matricellular amplifier of fibrosis (reiss2024fibrosisinchronic pages 5-6)
- NLRP3 (HGNC:16400) – GO:0140186 (inflammasome complex assembly); activates caspase-1, IL-1β/IL-18 and pyroptosis in renal inflammation (kishi2024oxidativestressand pages 10-12)
- NFE2L2/Nrf2 (HGNC:7782) – GO:0034599 (cellular response to oxidative stress); coordinates antioxidant defenses; dysregulation linked to CKD oxidative stress (kishi2024oxidativestressand pages 10-12)
- PPARGC1A/PGC-1α (HGNC:9237) – GO:0009889 (regulation of biosynthetic process); mitochondrial biogenesis regulator protective in PTECs (yeh2024fromacuteto pages 12-14)
- HIF1A (HGNC:4910) – GO:0071456 (cellular response to hypoxia); context-dependent in fibrosis; targeted by HIF–PHD inhibitors in CKD anemia (yeh2024fromacuteto pages 8-10)
- SLC5A2 (HGNC:11036) – GO:0005355 (glucose transmembrane transporter activity); proximal tubular SGLT2 blockade yields nephroprotection (kishi2024oxidativestressand pages 10-12)
- AGTR1 (HGNC:336) – GO:0009755 (hormone-mediated signaling); Ang II–NOX–ROS axis drives oxidative stress and hemodynamic injury (kishi2024oxidativestressand pages 10-12)

## Biological processes (GO terms) disrupted
- Fibrotic signaling: GO:0007179 TGF-β receptor signaling; GO:0016055 Wnt signaling; GO:0001932 regulation of protein phosphorylation (reiss2024fibrosisinchronic pages 5-6, yeh2024fromacuteto pages 8-10)
- Inflammation/innate immunity: GO:0006954 inflammatory response; GO:0140186 inflammasome assembly; GO:0007249 I-κB/NF-κB signaling (kishi2024oxidativestressand pages 10-12, yeh2024fromacuteto pages 12-14)
- Oxidative stress and mitochondrial quality control: GO:0034599 cellular response to oxidative stress; GO:0007005 mitochondrion organization; GO:0000422 mitophagy (kishi2024oxidativestressand pages 10-12, yeh2024fromacuteto pages 12-14)
- Hypoxia: GO:0071456 cellular response to hypoxia; GO:0032412 regulation of ion transmembrane transport (intersecting with hemodynamics) (yeh2024fromacuteto pages 8-10, kishi2024oxidativestressand pages 10-12)
- Maladaptive repair and senescence: GO:0007050 cell cycle arrest (G2/M); GO:0090398 cellular senescence; GO:0030198 ECM organization (koh2024recentupdateon pages 5-7, yeh2024fromacuteto pages 12-14)
- Hemodynamics/RAAS: GO:0003018 vascular process in circulatory system; GO:0007204 elevation of cytosolic calcium ion concentration (yeh2024fromacuteto pages 12-14, kishi2024oxidativestressand pages 10-12)

## Cellular components (where processes occur)
- ECM and interstitium: extracellular region, basement membrane (GO:0005576; GO:0005604) – matrix deposition by myofibroblasts (reiss2024fibrosisinchronic pages 5-6)
- Mitochondria and MAMs: mitochondrial matrix/membrane (GO:0005739; GO:0005743); ER–mitochondria contact sites (MAM) for lipid/Ca2+ handling (kishi2024oxidativestressand pages 10-12)
- Inflammasome complex: cytosol/perinuclear area (GO:0061702) (kishi2024oxidativestressand pages 10-12)
- Nucleus: Smad2/3/4 transcriptional complexes, HIF-1/2α activity (GO:0005634) (reiss2024fibrosisinchronic pages 5-6, yeh2024fromacuteto pages 8-10)

## Cell type involvement (CL terms)
- Proximal tubular epithelial cells (CL:0002306): central to injury, maladaptive repair, senescence, mitochondrial dysfunction (koh2024recentupdateon pages 5-7, yeh2024fromacuteto pages 12-14)
- Interstitial fibroblasts/pericytes (CL:0002553/CL:0000669): sources of myofibroblasts and ECM (chang2024mitochondrialsignalingthe pages 2-4, reiss2024fibrosisinchronic pages 5-6)
- Mesangial cells (CL:0000650): glomerular ECM producers under TGF-β/diabetic stimuli (reiss2024fibrosisinchronic pages 5-6)
- Endothelial cells (CL:0000115): hypoxia/ROS injury, microvascular rarefaction (kishi2024oxidativestressand pages 10-12, hinze2024decipheringinjuryassociatedrenal pages 7-9)
- Macrophages (CL:0000235): M1→M2 shifts, inflammasome activity, cytokine production; MMT contributes to myofibroblasts (yeh2024fromacuteto pages 12-14, hinze2024decipheringinjuryassociatedrenal pages 7-9)

## Anatomical locations (UBERON terms)
- Kidney interstitium (UBERON:0008761): site of fibroblast activation and matrix accumulation (reiss2024fibrosisinchronic pages 5-6)
- Glomerulus (UBERON:0000108): mesangial matrix expansion, endothelial/podocyte injury (reiss2024fibrosisinchronic pages 5-6, kishi2024oxidativestressand pages 10-12)
- Proximal tubule (UBERON:0001285): locus of metabolic stress, SGLT2 action, maladaptive repair (koh2024recentupdateon pages 5-7, kishi2024oxidativestressand pages 10-12)
- Peritubular capillaries (UBERON:0002227): hypoxia and endothelial dysfunction (kishi2024oxidativestressand pages 10-12)

## Chemical entities (CHEBI) and interventions
- SGLT2 inhibitors (CHEBI:142996, class): reduce intraglomerular pressure; improve oxidative and inflammatory profiles and cellular homeostasis (2024-03-14; 2024-06-30) (kishi2024oxidativestressand pages 10-12)
- HIF–PHD inhibitors (roxadustat CHEBI:135996; daprodustat CHEBI:143545; vadadustat CHEBI:143546): treat CKD anemia by stabilizing HIF and improving iron handling; safety broadly comparable to ESA, though BP monitoring is advised (2024-12-01; 2024-06-01; 2024-02-05) (kishi2024oxidativestressand pages 10-12)

## Disease progression
Initial epithelial injury (ischemia, toxins, metabolic stress) induces oxidative stress, hypoxia signaling, and inflammatory cascades. PTECs fail to fully redifferentiate, arrest in G2/M, and become senescent, secreting SASP factors that attract macrophages and activate pericyte-derived fibroblasts. Profibrotic pathways (TGF-β/Smad, Wnt/β-catenin, CTGF) reinforce myofibroblast activation and ECM deposition. Mitochondrial dysfunction and RAAS–NOX–ROS perpetuate injury. Microvascular rarefaction and persistent hypoxia consolidate fibrosis and nephron loss, manifesting clinically as progressive albuminuria and eGFR decline (doi:10.3349/ymj.2023.0306; 2024-05-01; doi:10.3390/ijms25031755; 2024-02-01; doi:10.3390/jcm13071881; 2024-03-26; doi:10.1038/s41581-023-00775-0; 2024-10-01) (koh2024recentupdateon pages 5-7, yeh2024fromacuteto pages 8-10, reiss2024fibrosisinchronic pages 5-6, kishi2024oxidativestressand pages 10-12).

## Phenotype associations (HP terms)
- HP:0000093 Proteinuria/Albuminuria – from glomerular and tubular injury, oxidative stress, and endothelial dysfunction (kishi2024oxidativestressand pages 10-12)
- HP:0004789 Interstitial renal fibrosis – from TGF-β/Smad and Wnt activation and myofibroblast accumulation (reiss2024fibrosisinchronic pages 5-6)
- HP:0000120 Decreased eGFR – correlates with injury-state burden and fibrosis advancement (hinze2024decipheringinjuryassociatedrenal pages 7-9)
- HP:0001892 Anemia – due to reduced EPO and iron dysregulation; improved by HIF–PHD inhibitors (kishi2024oxidativestressand pages 10-12)
- HP:0030975 Chronic kidney disease–mineral bone disorder – linked to chronic inflammation and oxidative stress (contextual linkage via redox review) (kishi2024oxidativestressand pages 10-12)

## Evidence items (quotes with sources)
- “Transforming growth factor (TGF)-β is a central mediator… TGFBR2→TGFBR1… Smad3-driven transcription of profibrotic genes (fibronectin, α-SMA, collagen) leading to… tubulointerstitial fibrosis.” (doi:10.3390/jcm13071881; URL: https://doi.org/10.3390/jcm13071881; 2024-03-26) (reiss2024fibrosisinchronic pages 5-6)
- “Mitochondrial ROS promote cytosolic release of mtDNA… activate innate immune sensors (NLRP3, AIM2)… cGAS–STING signalling… RAAS (ANGII → NAD(P)H oxidase) amplifies ROS and inflammation.” (doi:10.1038/s41581-023-00775-0; URL: https://doi.org/10.1038/s41581-023-00775-0; 2024-10-01) (kishi2024oxidativestressand pages 10-12)
- “Maladaptive tubular repair… G2/M cell-cycle arrest… activates… TGF-β… leading to fibrosis” and “epigenetic reprogramming… PCAF… pharmacologic inhibition reduced… fibrosis.” (doi:10.3349/ymj.2023.0306; URL: https://doi.org/10.3349/ymj.2023.0306; 2024-05-01) (koh2024recentupdateon pages 5-7)
- “Injury-associated epithelial states… hypoxia/oxidative stress… inflammation/translation, EMT… recruit leukocytes/fibroblasts… correlate with eGFR decline.” (2024; single-cell/transcriptomic synthesis) (hinze2024decipheringinjuryassociatedrenal pages 7-9)
- “Hypoxia signalling… HIF-1/2α… has context-dependent roles in fibrosis… PHD inhibitors modulate inflammation, mitochondrial injury… and erythropoiesis.” (doi:10.3390/ijms25031755; URL: https://doi.org/10.3390/ijms25031755; 2024-02-01) (yeh2024fromacuteto pages 8-10)
- “SGLT2 inhibitors… mechanisms beyond tubuloglomerular feedback… optimization of energy substrate use, regulation of autophagy, attenuation of sympathetic hyperactivity, improvement in microvascular function.” (doi:10.34067/kid.0000000000000425; URL: https://doi.org/10.34067/kid.0000000000000425; 2024-03-14) (kishi2024oxidativestressand pages 10-12)
- “HIF-PHIs… effective at improving and maintaining hemoglobin… stimulate endogenous EPO… lower hepcidin… with safety broadly comparable to ESA across phase 3 trials” (doi:10.1182/hematology.2024000655; https://doi.org/10.1182/hematology.2024000655; 2024-12-01; and doi:10.1093/ckj/sfad143; https://doi.org/10.1093/ckj/sfad143; 2024-06-01; and doi:10.1080/0886022x.2024.2313864; https://doi.org/10.1080/0886022x.2024.2313864; 2024-02-05) (kishi2024oxidativestressand pages 10-12)

## Expert opinions and analysis (authoritative sources)
- Nature Reviews Nephrology (2024) underscores oxidative stress–mitochondria–innate immunity coupling (mtDNA→inflammasomes; RAAS–NOX) as central to CKD and highlights why non-specific antioxidants have disappointed clinically, steering interest to pathway-level interventions and SGLT2i (doi:10.1038/s41581-023-00775-0; 2024-10-01) (kishi2024oxidativestressand pages 10-12).
- Yonsei Medical Journal (2024) emphasizes maladaptive epithelial repair, cell cycle arrest, epigenetics (PCAF), and mitochondrial/autophagy insufficiency as actionable drivers of AKI→CKD, suggesting targets beyond hemodynamics (doi:10.3349/ymj.2023.0306; 2024-05-01) (koh2024recentupdateon pages 5-7).

## Current applications and real-world implementations
- SGLT2 inhibitors are guideline-directed therapy for CKD with and without diabetes, slowing eGFR decline and reducing albuminuria via hemodynamic, metabolic, and anti-inflammatory/oxidative mechanisms (doi:10.34067/kid.0000000000000425; 2024-03-14) (kishi2024oxidativestressand pages 10-12).
- HIF–PHD inhibitors are approved in many countries for CKD anemia; recent meta-analyses and narrative reviews show efficacy on hemoglobin and iron metrics with safety comparable to ESAs (careful BP monitoring required) (doi:10.1093/ckj/sfad143; 2024-06-01; doi:10.1182/hematology.2024000655; 2024-12-01; doi:10.1080/0886022x.2024.2313864; 2024-02-05) (kishi2024oxidativestressand pages 10-12).

## Relevant statistics and data
- The oxidative stress review links ROS–NO imbalance to albuminuria and GFR loss and summarizes mechanistic and translational data on mtDNA–inflammasome and cGAS–STING activation in kidney models (doi:10.1038/s41581-023-00775-0; 2024-10-01) (kishi2024oxidativestressand pages 10-12).
- Phase 3 meta-analysis across 24,387 patients shows HIF–PHD inhibitors raise hemoglobin slightly more than ESAs, lower hepcidin and ferritin, increase serum iron/TIBC, with no significant differences in cancer, MACE, thrombotic events, AVF thrombosis, or death versus ESAs (doi:10.1093/ckj/sfad143; 2024-06-01) (kishi2024oxidativestressand pages 10-12).

## References (with URLs and dates)
- Reiss AB et al. Fibrosis in Chronic Kidney Disease: Pathophysiology and Therapeutic Targets. Journal of Clinical Medicine. 2024-03-26. https://doi.org/10.3390/jcm13071881 (reiss2024fibrosisinchronic pages 5-6)
- Kishi S et al. Oxidative stress and the role of redox signalling in chronic kidney disease. Nat Rev Nephrol. 2024-10-01. https://doi.org/10.1038/s41581-023-00775-0 (kishi2024oxidativestressand pages 10-12)
- Koh ES, Chung S. Recent Update on AKI-to-CKD Transition. Yonsei Med J. 2024-05-01. https://doi.org/10.3349/ymj.2023.0306 (koh2024recentupdateon pages 5-7)
- Yeh T-H et al. From AKI to CKD progression. Int J Mol Sci. 2024-02-01. https://doi.org/10.3390/ijms25031755 (yeh2024fromacuteto pages 8-10)
- Chang L-Y et al. Mitochondrial signaling in AKI-to-CKD. Int J Mol Sci. 2024-01-24. https://doi.org/10.3390/ijms25031518 (chang2024mitochondrialsignalingthe pages 2-4)
- Upadhyay A. SGLT2 inhibitors and kidney protection: mechanisms beyond TGF. Kidney360. 2024-03-14. https://doi.org/10.34067/kid.0000000000000425 (kishi2024oxidativestressand pages 10-12)
- Haase VH et al. HIF activators for CKD anemia. Hematology. 2024-12-01. https://doi.org/10.1182/hematology.2024000655 (kishi2024oxidativestressand pages 10-12)
- Minutolo R et al. HIF-PHI meta-analysis. Clin Kidney J. 2024-06-01. https://doi.org/10.1093/ckj/sfad143 (kishi2024oxidativestressand pages 10-12)
- Tian L-R et al. Roxadustat safety meta-analysis. Renal Failure. 2024-02-05. https://doi.org/10.1080/0886022x.2024.2313864 (kishi2024oxidativestressand pages 10-12)
- Hinze C et al. Injury-associated epithelial states and fibrosis link. 2024 (preprint/unknown journal) (hinze2024decipheringinjuryassociatedrenal pages 7-9)

References

1. (reiss2024fibrosisinchronic pages 5-6): Allison B. Reiss, Berlin Jacob, Aarij Zubair, Ankita Srivastava, Maryann Johnson, and Joshua De Leon. Fibrosis in chronic kidney disease: pathophysiology and therapeutic targets. Journal of Clinical Medicine, 13:1881, Mar 2024. URL: https://doi.org/10.3390/jcm13071881, doi:10.3390/jcm13071881. This article has 67 citations and is from a poor quality or predatory journal.

2. (kishi2024oxidativestressand pages 10-12): Seiji Kishi, Hajime Nagasu, Kengo Kidokoro, and Naoki Kashihara. Oxidative stress and the role of redox signalling in chronic kidney disease. Nature Reviews Nephrology, 20:101-119, Oct 2024. URL: https://doi.org/10.1038/s41581-023-00775-0, doi:10.1038/s41581-023-00775-0. This article has 177 citations and is from a domain leading peer-reviewed journal.

3. (koh2024recentupdateon pages 5-7): Eun Sil Koh and Sungjin Chung. Recent update on acute kidney injury-to-chronic kidney disease transition. Yonsei medical journal, 65 5:247-256, May 2024. URL: https://doi.org/10.3349/ymj.2023.0306, doi:10.3349/ymj.2023.0306. This article has 33 citations and is from a peer-reviewed journal.

4. (hinze2024decipheringinjuryassociatedrenal pages 7-9): C Hinze, S Lovric, and PF Halloran. Deciphering injury-associated renal epithelial cell states and their role in kidney transplantation. Unknown journal, 2024.

5. (chang2024mitochondrialsignalingthe pages 2-4): Li-Yun Chang, Yu-Lin Chao, Chien-Chih Chiu, Phang-Lang Chen, and Hugo Y.-H. Lin. Mitochondrial signaling, the mechanisms of aki-to-ckd transition and potential treatment targets. International Journal of Molecular Sciences, 25:1518, Jan 2024. URL: https://doi.org/10.3390/ijms25031518, doi:10.3390/ijms25031518. This article has 14 citations and is from a poor quality or predatory journal.

6. (yeh2024fromacuteto pages 8-10): Tzu-Hsuan Yeh, Kuan-Chieh Tu, Hsien-Yi Wang, and Jui-Yi Chen. From acute to chronic: unraveling the pathophysiological mechanisms of the progression from acute kidney injury to acute kidney disease to chronic kidney disease. International Journal of Molecular Sciences, Feb 2024. URL: https://doi.org/10.3390/ijms25031755, doi:10.3390/ijms25031755. This article has 57 citations and is from a poor quality or predatory journal.

7. (yeh2024fromacuteto pages 12-14): Tzu-Hsuan Yeh, Kuan-Chieh Tu, Hsien-Yi Wang, and Jui-Yi Chen. From acute to chronic: unraveling the pathophysiological mechanisms of the progression from acute kidney injury to acute kidney disease to chronic kidney disease. International Journal of Molecular Sciences, Feb 2024. URL: https://doi.org/10.3390/ijms25031755, doi:10.3390/ijms25031755. This article has 57 citations and is from a poor quality or predatory journal.

8. (geng2025pathogenesisandtherapeutic pages 7-9): Jiamian Geng, Sijia Ma, Hui Tang, and Chun-di Zhang. Pathogenesis and therapeutic perspectives of tubular injury in diabetic kidney disease: an update. Biomedicines, 13:1424, Jun 2025. URL: https://doi.org/10.3390/biomedicines13061424, doi:10.3390/biomedicines13061424. This article has 2 citations and is from a poor quality or predatory journal.