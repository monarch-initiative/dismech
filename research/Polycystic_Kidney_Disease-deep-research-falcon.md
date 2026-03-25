---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-08T21:56:31.742821'
end_time: '2026-01-08T22:04:09.817602'
duration_seconds: 458.07
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Polycystic Kidney Disease
  mondo_id: ''
  category: Mendelian
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
- **Disease Name:** Polycystic Kidney Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Polycystic Kidney Disease**.
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
- **Disease Name:** Polycystic Kidney Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Polycystic Kidney Disease**.
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
- Disease Name: Polycystic Kidney Disease (PKD)
- MONDO ID: —
- Category: Mendelian (autosomal dominant and recessive forms)

Pathophysiology description
Polycystic kidney disease is a systemic ciliopathy in which inherited defects in cilia-associated proteins of renal tubular epithelia trigger cyst initiation, clonal expansion, and progressive remodeling of kidney architecture, culminating in chronic kidney disease and end-stage renal disease. In autosomal dominant PKD (ADPKD), loss-of-function mutations in PKD1 (polycystin‑1, PC1) or PKD2 (polycystin‑2, PC2) compromise primary-cilium mechanosensation and calcium flux, elevating cAMP and activating proliferative kinase networks (MAPK/ERK and PI3K–AKT–mTOR). These signals reprogram epithelial metabolism toward glycolysis, drive chloride/water secretion into cyst lumens via CFTR, and promote epithelial‑initiated fibrogenesis and interstitial inflammation that together accelerate cyst growth and nephron loss (https://doi.org/10.3390/genes15010091; https://doi.org/10.3390/ijms25137173) (satariano2024thepathophysiologyof pages 8-10, song2024reprogrammingofenergy pages 1-2). In autosomal recessive PKD (ARPKD), PKHD1 (fibrocystin, FPC) and DZIP1L mutations perturb ciliary/transition-zone function and EGFR/cAMP signaling, producing collecting-duct cysts and hepato-biliary fibrosis; DZIP1L dysfunction also impairs PC1/PC2 ciliary trafficking (https://doi.org/10.3390/genes15010091) (satariano2024thepathophysiologyof pages 8-10).

Core Pathophysiology
1) Ciliary dysfunction and mechanotransduction
- PC1/PC2 reside at the primary cilium; loss of either reduces intraciliary/cytosolic Ca2+ and disrupts mechanosensory control of downstream growth pathways and polarity cues. Somatic “second hits” are frequent in cyst-lining cells, consistent with a two‑hit model (https://doi.org/10.3390/genes15010091) (satariano2024thepathophysiologyof pages 8-10).
- Experimental genetic deletion identifies Aurora kinase A (AURKA) as a feed‑forward driver of cystogenesis via AKT; Aurka deletion prevented cyst formation in Pkd1- and Inpp5e‑driven mouse PKD, linking ciliary control, cell-cycle regulation, and AKT signaling (https://doi.org/10.1038/s41467-023-44410-9; published Jan 2024) (tham2024deletionofaurora pages 1-2).

2) Ca2+/cAMP axis and chloride/fluid secretion
- Lowered Ca2+ disinhibits adenylyl cyclases (AC5/6), raising cAMP; PKA then activates B‑Raf–MEK–ERK and PI3K–AKT and enhances CFTR-mediated Cl− secretion that drives osmotic fluid accumulation and cyst expansion (https://doi.org/10.3390/ijms25137173) (song2024reprogrammingofenergy pages 1-2).
- Compartmentalized cAMP nanodomains likely exist; a 2024 thesis highlights PDE3 as a regulator of a potentially cyst-protective cAMP pool and suggests PDE3–PC2 interactions at ER–mitochondria contacts, motivating selective modulation beyond V2R blockade (Paolocci 2024; doctoral thesis) (paolocci2024campsignallingand pages 13-17, paolocci2024campsignallingand pages 1-7).

3) Proliferative kinase signaling
- cAMP/PKA cooperates with receptor and integrin inputs to activate B‑Raf–MEK–ERK and PI3K–AKT–mTORC1, which promote proliferation and growth programs central to cyst enlargement. AURKA physically interacts with and regulates AKT, completing a loop that sustains cyst growth and ciliary disassembly; pharmacologic AURKA inhibition with alisertib paradoxically stabilized AURKA protein in vivo, cautioning on target modality (https://doi.org/10.1038/s41467-023-44410-9; Jan 2024) (tham2024deletionofaurora pages 1-2). 

4) Hippo–YAP/TAZ and RhoA–MRTF fibrosis coupling
- Hippo pathway dysregulation in PKD permits nuclear YAP/TAZ and c‑MYC-driven transcription that amplifies proliferative and fibrotic responses (https://doi.org/10.3390/cells13110984; 5 Jun 2024) (lichner2024myocardinrelatedtranscriptionfactor pages 1-2).
- Loss of PC1/PC2 activates RhoA, actin remodeling, and nuclear translocation of myocardin-related transcription factors (MRTF-A/B), which reprogram the cyst epithelium into a profibrotic epithelial phenotype and paracrine-prime fibroblast-to-myofibroblast transition (https://doi.org/10.3390/cells13110984; 2024) (lichner2024myocardinrelatedtranscriptionfactor pages 1-2).

5) Wnt/planar cell polarity (PCP)
- Noncanonical Wnt/PCP defects disturb oriented cell division and tubule architecture, contributing to dilatation and cyst initiation in inherited cystic diseases (https://doi.org/10.3390/genes15010091; 2024) (satariano2024thepathophysiologyof pages 8-10).

6) Metabolic reprogramming and mitochondrial dysfunction
- Human PKD1 cyst transcriptomics show Warburg-like shifts: increased glucose uptake and lactate production with broad suppression of FAO, TCA, and OXPHOS; predicted mTORC1/HIF‑1α/MYC activation and AMPK/PGC‑1α suppression provide a regulatory scaffold for these changes (https://doi.org/10.3390/ijms25137173; 26 Jun 2024) (song2024reprogrammingofenergy pages 1-2).

7) Inflammation/immune pathways
- Cystic epithelium and interstitium exhibit immune infiltration with cytokine network activation (e.g., IL‑12/23 family; STAT3), contributing to proliferation and fibrosis; STING and TWEAK/Fn14 axes are implicated as amplifiers (review synthesis) (https://doi.org/10.3390/genes15010091; 2024) (satariano2024thepathophysiologyof pages 8-10).
- Interstitial fibrosis is further supported by fibroblast–macrophage crosstalk and WNT/β‑catenin signaling in CKD, consistent with profibrotic programs in cystic kidneys (contextualized to PKD) (https://doi.org/10.3390/genes15010091; 2024) (satariano2024thepathophysiologyof pages 8-10).

8) Extracellular matrix remodeling and fibrosis
- Epithelial RhoA–MRTF signaling induces ECM/matricellular genes and secreted mediators that remodel the interstitium; epithelial MRTF is necessary for priming myofibroblast differentiation in PKD models (https://doi.org/10.3390/cells13110984; 2024) (lichner2024myocardinrelatedtranscriptionfactor pages 1-2).

Key Molecular Players
Genes/Proteins (HGNC symbol; role)
- PKD1 (PC1) and PKD2 (PC2): ciliary mechanosensory complex controlling Ca2+ homeostasis; causal in ADPKD (https://doi.org/10.3390/genes15010091) (satariano2024thepathophysiologyof pages 8-10).
- PKHD1 (FPC): ciliary membrane/transition-zone protein; causal in ARPKD; DZIP1L: ciliary trafficking; ARPKD modulator (https://doi.org/10.3390/genes15010091) (satariano2024thepathophysiologyof pages 8-10).
- CFTR: apical Cl− channel driving fluid secretion in cysts under cAMP control (https://doi.org/10.3390/ijms25137173) (song2024reprogrammingofenergy pages 1-2).
- AURKA: kinase/ciliogenesis regulator forming a feed‑forward loop with AKT driving cystogenesis; genetic deletion prevents cysts in mice (https://doi.org/10.1038/s41467-023-44410-9) (tham2024deletionofaurora pages 1-2).
- BRAF–MEK–ERK; PI3K–AKT–mTOR: proliferative/growth pathways activated by cAMP and growth cues (https://doi.org/10.1038/s41467-023-44410-9; https://doi.org/10.3390/ijms25137173) (tham2024deletionofaurora pages 1-2, song2024reprogrammingofenergy pages 1-2).
- Hippo effectors YAP1/WWTR1 (TAZ) and RHOA–MRTFA(MKL1)/SRF: proliferation–fibrosis coupling in cyst epithelium (https://doi.org/10.3390/cells13110984) (lichner2024myocardinrelatedtranscriptionfactor pages 1-2).
- STAT3: activated in cystic epithelia and inflammation networks (https://doi.org/10.3390/genes15010091) (satariano2024thepathophysiologyof pages 8-10).
- PDE3, AC5/6: cAMP compartmentalization and synthesis/breakdown influencing cystogenesis (Paolocci 2024 thesis) (paolocci2024campsignallingand pages 13-17, paolocci2024campsignallingand pages 1-7).

Chemical entities (CHEBI)
- Calcium ion (CHEBI:29108); cAMP (CHEBI:17489); chloride ion (CHEBI:17996); glucose (CHEBI:17234); lactate (CHEBI:24996); vasopressin V2 receptor antagonist tolvaptan (drug; cAMP-lowering in ADPKD) (https://doi.org/10.3390/ijms25137173) (song2024reprogrammingofenergy pages 1-2).

Cell types (CL)
- Renal tubular epithelial cells (collecting duct and nephron segments): cyst-lining epithelium (CL term category: epithelial cell) (https://doi.org/10.1038/s41467-023-44410-9; https://doi.org/10.3390/genes15010091) (tham2024deletionofaurora pages 1-2, satariano2024thepathophysiologyof pages 8-10).
- Interstitial fibroblasts and myofibroblasts (CL: fibroblast lineage): ECM deposition (https://doi.org/10.3390/cells13110984) (lichner2024myocardinrelatedtranscriptionfactor pages 1-2).
- Macrophages (CL:0000235): inflammatory crosstalk, pro-fibrotic signaling (https://doi.org/10.3390/genes15010091) (satariano2024thepathophysiologyof pages 8-10).

Anatomical locations (UBERON)
- Kidney (parenchyma); renal tubule and collecting duct (cyst origin); interstitium; liver/biliary tree (ARPKD, polycystic liver disease) (https://doi.org/10.3390/genes15010091) (satariano2024thepathophysiologyof pages 8-10).

Biological Processes (GO) disrupted
- Cilium organization and ciliary signaling; mechanosensation; calcium ion homeostasis; cAMP signaling; chloride transport; MAPK cascade; PI3K–AKT–mTOR signaling; Hippo signaling; Wnt/PCP pathway; epithelial cell proliferation; epithelial fluid secretion; mitochondrial electron transport and fatty-acid β‑oxidation; extracellular matrix organization; inflammatory response and JAK–STAT cascade (https://doi.org/10.3390/genes15010091; https://doi.org/10.3390/ijms25137173; https://doi.org/10.3390/cells13110984; https://doi.org/10.1038/s41467-023-44410-9) (satariano2024thepathophysiologyof pages 8-10, song2024reprogrammingofenergy pages 1-2, lichner2024myocardinrelatedtranscriptionfactor pages 1-2, tham2024deletionofaurora pages 1-2).

Cellular Components (GO-CC)
- Primary cilium, ciliary membrane, basal body; apical plasma membrane (CFTR); endoplasmic reticulum and mitochondrion (Ca2+ exchange and metabolism); extracellular region/extracellular matrix (https://doi.org/10.3390/genes15010091; https://doi.org/10.3390/ijms25137173) (satariano2024thepathophysiologyof pages 8-10, song2024reprogrammingofenergy pages 1-2).

Disease Progression (sequence of events)
- Genetic lesion and second hit: germline PKD1/PKD2 (ADPKD) or PKHD1/DZIP1L (ARPKD) mutations with somatic inactivation in individual tubular cells initiate cysts (https://doi.org/10.3390/genes15010091) (satariano2024thepathophysiologyof pages 8-10).
- Cyst initiation: ciliary Ca2+ signaling failure increases cAMP; polarity/PCP cues are disturbed; early luminal fluid accumulation occurs via CFTR-mediated Cl− secretion (https://doi.org/10.3390/ijms25137173; https://doi.org/10.3390/genes15010091) (song2024reprogrammingofenergy pages 1-2, satariano2024thepathophysiologyof pages 8-10).
- Cyst expansion: PKA–ERK and AKT–mTORC1 drive epithelial proliferation and growth; metabolic reprogramming supports biomass and energy; AURKA–AKT feed‑forward loop and Hippo/YAP amplify proliferation; RhoA–MRTF primes fibrosis (https://doi.org/10.1038/s41467-023-44410-9; https://doi.org/10.3390/ijms25137173; https://doi.org/10.3390/cells13110984) (tham2024deletionofaurora pages 1-2, song2024reprogrammingofenergy pages 1-2, lichner2024myocardinrelatedtranscriptionfactor pages 1-2).
- Tissue remodeling: interstitial inflammation and fibroblast activation produce fibrosis; nephron dropout and vascular rarefaction ensue, causing progressive GFR decline (https://doi.org/10.3390/genes15010091; https://doi.org/10.3390/cells13110984) (satariano2024thepathophysiologyof pages 8-10, lichner2024myocardinrelatedtranscriptionfactor pages 1-2).
- ARPKD distinctions: collecting-duct–predominant cysts with congenital hepatic fibrosis; fibrocystin C-terminal signaling restrains Src/STAT3 and secretory phenotypes in model systems, consistent with heightened STAT3 signaling when FPC is deficient (https://doi.org/10.3390/genes15010091) (satariano2024thepathophysiologyof pages 8-10).

Phenotypic Manifestations (HP terms)
- Renal cysts (HP:0000107), Enlarged kidneys (HP:0000105), Hypertension (HP:0000822), Hematuria (HP:0000790), Flank/abdominal pain; Hepatic cysts (HP:0001407) and congenital hepatic fibrosis (ARPKD); Intracranial aneurysm risk (HP:0002617). These manifestations reflect tubular cyst burden, interstitial fibrosis/inflammation, and systemic vascular/ductal involvement (https://doi.org/10.3390/genes15010091) (satariano2024thepathophysiologyof pages 8-10).

Recent developments and latest research (2023–2024 priority)
- AURKA–AKT feed‑forward loop as a master regulator: Aurka deletion prevented PKD across two genetic models; the data highlight non-kinase functions and caution that alisertib can stabilize AURKA in vivo, informing drug design (Nature Communications, 10 Jan 2024; https://doi.org/10.1038/s41467-023-44410-9) (tham2024deletionofaurora pages 1-2).
- Human PKD1 cyst metabolic atlas: Systems biology analysis mapped a Warburg shift with predicted mTORC1/HIF‑1α/MYC activation and suppressed AMPK/PGC‑1α, concretizing metabolism-targeted therapies (IJMS, 26 Jun 2024; https://doi.org/10.3390/ijms25137173) (song2024reprogrammingofenergy pages 1-2).
- Epithelial-initiated fibrogenesis: PKD epithelium activates RhoA–MRTF programs that prime myofibroblast transition, providing epithelial targets for anti-fibrotic intervention (Cells, 5 Jun 2024; https://doi.org/10.3390/cells13110984) (lichner2024myocardinrelatedtranscriptionfactor pages 1-2).
- ARPKD gene and pathway synthesis: Updated review integrates PKHD1/DZIP1L ciliary biology with EGFR/cAMP and ECM remodeling, clarifying pediatric hepato-renal disease mechanisms (Genes, 5 Jan 2024; https://doi.org/10.3390/genes15010091) (satariano2024thepathophysiologyof pages 8-10).
- cAMP compartmentalization: New experimental work proposes PDE3 as a modulator of organelle cAMP nanodomains and potential PC2 interactor at ER–mitochondrial contacts (doctoral thesis, 2024) (paolocci2024campsignallingand pages 13-17, paolocci2024campsignallingand pages 1-7).

Current applications and implementations
- Disease-modifying therapy: Tolvaptan (V2R antagonist) is approved to slow ADPKD progression by reducing cAMP; translational metabolism strategies (e.g., ketogenic interventions, AMPK activation) are supported by the human cyst metabolic signatures but require rigorous trials (https://doi.org/10.3390/ijms25137173) (song2024reprogrammingofenergy pages 1-2).
- Emerging targets: AURKA–AKT axis, RhoA–MRTF signaling, Hippo/YAP, and cytokine–STAT3 pathways represent testable targets; the in vivo genetic validation of AURKA strengthens prioritization (https://doi.org/10.1038/s41467-023-44410-9; https://doi.org/10.3390/cells13110984) (tham2024deletionofaurora pages 1-2, lichner2024myocardinrelatedtranscriptionfactor pages 1-2).

Expert opinions and analysis
- 2024 syntheses argue that PKD integrates ciliary signaling failure with proliferative and metabolic rewiring; epithelial cells both initiate cystogenesis and act as paracrine organizers of interstitial fibrosis, implying dual-acting therapies that combine cAMP reduction, proliferation blockade, and anti-fibrotic reprogramming may be required for durable benefit (https://doi.org/10.3390/ijms25137173; https://doi.org/10.3390/cells13110984; https://doi.org/10.3390/genes15010091) (song2024reprogrammingofenergy pages 1-2, lichner2024myocardinrelatedtranscriptionfactor pages 1-2, satariano2024thepathophysiologyof pages 8-10).

Relevant statistics and data from recent studies
- Genetic architecture: ADPKD due to PKD1 (~75–85%) or PKD2 (~15–25%); ARPKD due to PKHD1 with DZIP1L as a rarer cause/modifier (2024 review synthesis) (https://doi.org/10.3390/genes15010091) (satariano2024thepathophysiologyof pages 8-10).
- Metabolic pathways: In human PKD1 cysts, gene sets for FAO, OXPHOS, BCAA degradation, and TCA cycle were downregulated, while glycolysis and lactate transporters were upregulated, aligning with predicted mTORC1/HIF‑1α/MYC activation and AMPK inhibition (IJMS 2024) (https://doi.org/10.3390/ijms25137173) (song2024reprogrammingofenergy pages 1-2).
- In vivo mechanistic validation: Aurka deletion blocked cyst initiation and growth in two independent mouse PKD models and revealed AKT–AURKA physical interaction and a feed‑forward loop (Nature Communications 2024) (https://doi.org/10.1038/s41467-023-44410-9) (tham2024deletionofaurora pages 1-2).

Gene/protein annotations with ontology terms
- HGNC: PKD1, PKD2, PKHD1, DZIP1L, CFTR, AURKA, BRAF, MAP2K1 (MEK1), MAPK1 (ERK2), PIK3CA, AKT1, MTOR, YAP1, WWTR1 (TAZ), RHOA, MRTFA (MKL1), SRF, STAT3, ADCY5/6, PDE3A/B (tham2024deletionofaurora pages 1-2, song2024reprogrammingofenergy pages 1-2, satariano2024thepathophysiologyof pages 8-10, lichner2024myocardinrelatedtranscriptionfactor pages 1-2).
- GO BP: cilium organization; calcium ion homeostasis; cAMP signaling; chloride transport; MAPK cascade; PI3K–AKT signaling; mTOR signaling; Hippo signaling; Wnt/PCP; epithelial cell proliferation; epithelial fluid secretion; mitochondrial electron transport chain; fatty acid β-oxidation; extracellular matrix organization; inflammatory response; JAK–STAT cascade (tham2024deletionofaurora pages 1-2, song2024reprogrammingofenergy pages 1-2, satariano2024thepathophysiologyof pages 8-10, lichner2024myocardinrelatedtranscriptionfactor pages 1-2).
- GO CC: primary cilium; ciliary membrane; basal body; apical plasma membrane; endoplasmic reticulum; mitochondrion; extracellular matrix (song2024reprogrammingofenergy pages 1-2, satariano2024thepathophysiologyof pages 8-10).

Phenotype associations (HP terms)
- Renal cysts (HP:0000107); Enlarged kidneys (HP:0000105); Hypertension (HP:0000822); Hematuria (HP:0000790); Hepatic cysts (HP:0001407); Intracranial aneurysm (HP:0002617) (satariano2024thepathophysiologyof pages 8-10).

Cell type involvement (CL terms)
- Renal tubular epithelial cell (cyst-lining); fibroblast/myofibroblast; macrophage (tham2024deletionofaurora pages 1-2, satariano2024thepathophysiologyof pages 8-10, lichner2024myocardinrelatedtranscriptionfactor pages 1-2).

Anatomical locations (UBERON terms)
- Kidney; renal tubule; collecting duct; renal interstitium; liver/biliary tree (satariano2024thepathophysiologyof pages 8-10).

Chemical entities (CHEBI)
- Calcium ion; cAMP; chloride ion; glucose; lactate; tolvaptan (drug) (song2024reprogrammingofenergy pages 1-2).

Evidence items (PMIDs/DOIs and dates)
- Tham et al., Nature Communications, 10 Jan 2024. “Deletion of Aurora kinase A prevents the development of polycystic kidney disease in mice.” https://doi.org/10.1038/s41467-023-44410-9 (tham2024deletionofaurora pages 1-2).
- Song et al., International Journal of Molecular Sciences, 26 Jun 2024. “Reprogramming of Energy Metabolism in Human PKD1 Polycystic Kidney Disease.” https://doi.org/10.3390/ijms25137173 (song2024reprogrammingofenergy pages 1-2).
- Lichner et al., Cells, 5 Jun 2024. “Myocardin-Related Transcription Factor Mediates Epithelial Fibrogenesis in PKD.” https://doi.org/10.3390/cells13110984 (lichner2024myocardinrelatedtranscriptionfactor pages 1-2).
- Satariano et al., Genes, 5 Jan 2024. “The Pathophysiology of Inherited Renal Cystic Diseases.” https://doi.org/10.3390/genes15010091 (satariano2024thepathophysiologyof pages 8-10).
- Paolocci E., 2024 thesis. “cAMP signalling and phosphodiesterase activity in cystogenesis of ADPKD.” (paolocci2024campsignallingand pages 13-17, paolocci2024campsignallingand pages 1-7).

Summary artifact
| Mechanistic domain | Key findings (1–2 sentences) | Principal molecules/genes | Cell types | 2023–2024 sources (journal, year, URL/DOI) |
|---|---|---|---|---|
| Ciliary dysfunction & mechanotransduction | Loss or dysfunction of PC1/PC2 in primary cilia impairs ciliary Ca2+ mechanosensing, disrupting downstream signaling and promoting cyst initiation; somatic "second hits" in cysts are common. | PKD1 (PC1), PKD2 (PC2), IFT/KIF genes | Renal tubular epithelial cells (collecting duct, nephron epithelia) | Nature Communications, 2024, https://doi.org/10.1038/s41467-023-44410-9 (tham2024deletionofaurora pages 1-2); Genes, 2024, https://doi.org/10.3390/genes15010091 (satariano2024thepathophysiologyof pages 8-10) |
| Ca2+/cAMP and CFTR-mediated Cl- secretion | Reduced intraciliary/cytosolic Ca2+ disinhibits adenylyl cyclases increasing cAMP; cAMP/PKA promotes epithelial proliferation and CFTR-mediated chloride/fluid secretion that expands cysts; V2R antagonism (tolvaptan) lowers cAMP clinically. | AC5/6, cAMP, PDE3, CFTR, AVPR2 (V2R) | Cyst-lining epithelial cells | Unknown journal, 2024 (Paolocci thesis) (paolocci2024campsignallingand pages 13-17); IJMS, 2024, https://doi.org/10.3390/ijms25137173 (song2024reprogrammingofenergy pages 1-2) |
| Proliferative signaling (MAPK/ERK, PI3K/AKT/mTOR) | cAMP/PKA and growth-receptor signaling activate B-Raf→MEK→ERK and PI3K→AKT→mTORC1, driving cell cycle entry, growth and metabolic programs that sustain cyst growth. | BRAF/MEK/ERK, PI3K, AKT, mTOR, c-MYC | Tubular epithelial cells (cyst epithelium) | Nature Communications, 2024, https://doi.org/10.1038/s41467-023-44410-9 (tham2024deletionofaurora pages 1-2); IJMS, 2024, https://doi.org/10.3390/ijms25137173 (song2024reprogrammingofenergy pages 1-2) |
| Hippo — YAP/TAZ | Dysregulated Hippo signaling permits nuclear YAP/TAZ activity, promoting transcriptional programs (e.g., c-MYC) that increase proliferation and link to fibrogenic responses. | YAP, TAZ, LATS1/2, MST1/2 | Cyst-lining epithelial cells; epithelial progenitors | Cells, 2024, https://doi.org/10.3390/cells13110984 (lichner2024myocardinrelatedtranscriptionfactor pages 1-2); Genes, 2024, https://doi.org/10.3390/genes15010091 (satariano2024thepathophysiologyof pages 8-10) |
| Wnt / Planar cell polarity (PCP) | Defects in Wnt/PCP signaling disrupt oriented cell division and tubule architecture, contributing to abnormal tubule dilation and cyst formation. | WNT ligands, VANGL/CELSR, DVL | Tubular epithelial cells | Genes, 2024, https://doi.org/10.3390/genes15010091 (satariano2024thepathophysiologyof pages 8-10) |
| Metabolic reprogramming & mitochondria | Cystic epithelia show a Warburg-like shift (↑glycolysis, ↑lactate) with suppressed FAO and OXPHOS, AMPK inhibition and mTOR activation, supporting proliferation and survival. | GLUTs, HK1/2, LDHA, PDK1, AMPK, PGC‑1α | Cyst-lining epithelial cells | IJMS, 2024, https://doi.org/10.3390/ijms25137173 (song2024reprogrammingofenergy pages 1-2) |
| Inflammation & immune (JAK/STAT, cytokines) | Immune cell infiltration and cytokine dysregulation (e.g., IL‑family) activate JAK/STAT and NF‑κB pathways, amplifying epithelial proliferation and fibrotic remodeling. | IL family (IL‑12/23), JAK/STAT3, NF‑κB, STING, TWEAK/Fn14 | Macrophages, epithelial cells, fibroblasts | Genes, 2024, https://doi.org/10.3390/genes15010091 (satariano2024thepathophysiologyof pages 8-10); Cells, 2024, https://doi.org/10.3390/cells13110984 (lichner2024myocardinrelatedtranscriptionfactor pages 1-2) |
| ECM remodeling & fibrosis (MRTF; fibroblast–macrophage crosstalk) | Epithelial RhoA activation drives MRTF nuclear translocation and profibrotic gene expression, priming fibroblast→myofibroblast transition; reciprocal Wnt–macrophage–fibroblast crosstalk promotes interstitial fibrosis. | RHOA, MRTF‑A/B, SRF, collagen, TGF‑β, WNT | Tubular epithelial cells, interstitial fibroblasts, macrophages | Cells, 2024, https://doi.org/10.3390/cells13110984 (lichner2024myocardinrelatedtranscriptionfactor pages 1-2); Genes, 2024, https://doi.org/10.3390/genes15010091 (satariano2024thepathophysiologyof pages 8-10) |
| Cell cycle / ciliogenesis regulators (AURKA) | AURKA is upregulated in PKD, promotes proliferation and ciliary disassembly and forms a feed‑forward loop with AKT; genetic deletion of Aurka prevents cyst formation in mouse PKD models. | AURKA, AKT | Collecting-duct and tubular epithelial cells | Nature Communications, 2024, https://doi.org/10.1038/s41467-023-44410-9 (tham2024deletionofaurora pages 1-2) |


*Table: Compact 2023–2024 evidence map summarizing major molecular/cellular mechanisms in ADPKD/ARPKD, with principal genes, affected cell types, and primary sources; useful as a quick reference linking mechanisms to recent literature (context citations included).*

Direct quotes supporting key statements
- “Deletion of the Aurora Kinase A gene… prevents cyst formation in both disease models… AURKA and AKT physically interact… creating a feed-forward loop driving renal cystogenesis.” (Nature Communications, 2024) (tham2024deletionofaurora pages 1-2).
- “Gene expression profiles of PKD1 renal cysts were consistent with the Warburg effect… mitochondrial energy metabolism was globally depressed… activation of mTORC1 and… HIF-1α and MYC… AMPK inhibition was predicted in renal cysts.” (IJMS, 2024) (song2024reprogrammingofenergy pages 1-2).
- “The loss of PC1 or PC2… activated RhoA… robust nuclear MRTF translocation… epithelial MRTF was necessary for the paracrine priming of the fibroblast–myofibroblast transition.” (Cells, 2024) (lichner2024myocardinrelatedtranscriptionfactor pages 1-2).

Conclusion
PKD pathogenesis is best understood as an integrated network linking primary-cilium dysfunction and Ca2+/cAMP derangements to proliferative signaling, metabolic reprogramming, and fibrotic/inflammatory remodeling. Recent 2024 studies provide in vivo mechanistic validation (AURKA–AKT) and human cyst metabolic maps (Warburg shift), while epithelial RhoA–MRTF signaling emerges as a nexus between cystogenesis and fibrosis. These insights nominate combined strategies—precise cAMP modulation, anti-proliferative pathway inhibition, and anti-fibrotic reprogramming—as rational avenues to slow disease progression beyond current V2R antagonism (https://doi.org/10.1038/s41467-023-44410-9; https://doi.org/10.3390/ijms25137173; https://doi.org/10.3390/cells13110984) (tham2024deletionofaurora pages 1-2, song2024reprogrammingofenergy pages 1-2, lichner2024myocardinrelatedtranscriptionfactor pages 1-2).

References

1. (satariano2024thepathophysiologyof pages 8-10): Matthew Satariano, Shaarav Ghose, and Rupesh Raina. The pathophysiology of inherited renal cystic diseases. Genes, 15:91, Jan 2024. URL: https://doi.org/10.3390/genes15010091, doi:10.3390/genes15010091. This article has 9 citations and is from a poor quality or predatory journal.

2. (song2024reprogrammingofenergy pages 1-2): Xuewen Song, Lauren Pickel, Hoon-Ki Sung, James W. Scholey, and York Pei. Reprogramming of energy metabolism in human pkd1 polycystic kidney disease: a systems biology analysis. International Journal of Molecular Sciences, 25:7173, Jun 2024. URL: https://doi.org/10.3390/ijms25137173, doi:10.3390/ijms25137173. This article has 8 citations and is from a poor quality or predatory journal.

3. (tham2024deletionofaurora pages 1-2): Ming Shen Tham, Denny L. Cottle, Allara K. Zylberberg, Kieran M. Short, Lynelle K. Jones, Perkin Chan, Sarah E. Conduit, Jennifer M. Dyson, Christina A. Mitchell, and Ian M. Smyth. Deletion of aurora kinase a prevents the development of polycystic kidney disease in mice. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44410-9, doi:10.1038/s41467-023-44410-9. This article has 15 citations and is from a highest quality peer-reviewed journal.

4. (paolocci2024campsignallingand pages 13-17): E Paolocci. Camp signalling and phosphodiesterase activity in cystogenesis of autosomal dominant polycystic kidney disease. Unknown journal, 2024.

5. (paolocci2024campsignallingand pages 1-7): E Paolocci. Camp signalling and phosphodiesterase activity in cystogenesis of autosomal dominant polycystic kidney disease. Unknown journal, 2024.

6. (lichner2024myocardinrelatedtranscriptionfactor pages 1-2): Zsuzsanna Lichner, Mei Ding, Tarang Khare, Qinghong Dan, Raquel Benitez, Mercédesz Praszner, Xuewen Song, Rola Saleeb, Boris Hinz, York Pei, Katalin Szászi, and András Kapus. Myocardin-related transcription factor mediates epithelial fibrogenesis in polycystic kidney disease. Cells, 13:984, Jun 2024. URL: https://doi.org/10.3390/cells13110984, doi:10.3390/cells13110984. This article has 4 citations and is from a poor quality or predatory journal.