---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2025-12-27T14:55:21.635157'
end_time: '2025-12-27T14:55:21.638259'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Traveler's Diarrhea
  mondo_id: ''
  category: Infectious
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
- **Disease Name:** Traveler's Diarrhea
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Traveler's Diarrhea**.
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
- **Disease Name:** Traveler's Diarrhea
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Traveler's Diarrhea**.
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
- Disease Name: Traveler’s Diarrhea (TD)
- MONDO ID: not specified in MONDO (as of current sources)
- Category: Infectious

Executive Summary
Traveler’s diarrhea arises predominantly from enterotoxigenic and enteropathogenic mechanisms that disrupt epithelial ion transport and barrier integrity, alongside inflammatory and enteric nervous system–mediated secretory reflexes. The core molecular pathways include cAMP- and cGMP-driven activation of CFTR chloride secretion, inhibition of apical Na+ absorption via NHE3 and DRA, tight-junction dysregulation by type III secretion system effectors, and Ca2+-dependent secretory signaling for certain viral etiologies. Recent work (2023–2024) highlights: (1) precise transporter-level derangements in EPEC, including NHE3, DRA/SLC26A3, SGLT1, MCT1 and SERT dysregulation; (2) ETEC STa/LT signaling into GC-C/cGMP and adenylate cyclase/cAMP converging on CFTR with NHE3 inhibition; (3) EAEC as a frequent TD etiology with high AMR carriage among travelers; and (4) a translational, mechanistically targeted antisecretory strategy—luminal Mg2+ activation of CaSR—to blunt cyclic nucleotide–mediated secretion in cell and mouse models (JCI 2024). (kaur2023pathophysiologyofenteropathogenic pages 11-12, kaur2023pathophysiologyofenteropathogenic pages 21-25, ye2024baicalinaluminumcomplexon pages 4-9, poh2025microbiologyandepidemiology pages 10-12, goncalves2024mg2+supplementationtreats pages 1-2, goncalves2024mg2+supplementationtreats pages 8-10)

Core Pathophysiology
- Secretory diarrhea via cyclic nucleotides: ETEC heat-labile toxin (LT) activates adenylate cyclase → cAMP/PKA → CFTR phosphorylation, while heat-stable toxin (STa) activates GC-C (GUCY2C) → cGMP/PKG with cross-activation of PKA, stimulating CFTR and inhibiting NHE3, producing net Cl− secretion and impaired Na+ absorption. In vitro, ETEC increases cellular cAMP/cGMP, upregulates CFTR mRNA, and inhibits NHEs; a 2024 epithelial study confirmed STa→GUCY2C→cGMP/PKG and LT→cAMP/PKA cascades converging on CFTR/NHE3 dysfunction. (URL: https://doi.org/10.1016/j.heliyon.2024.e33038, Jun 2024) (ye2024baicalinaluminumcomplexon pages 4-9)
- Tight-junction and transporter disruption (EPEC): EPEC T3SS effectors (EspF, Map, Tir, EspG, NleA) drive attaching-and-effacing lesions, microvillus effacement, tight-junction internalization (claudins, ZO-1/ZO-2), mitochondrial injury, and actin remodeling via N-WASP/Arp2/3. EPEC specifically inhibits NHE3 (SLC9A3), reduces apical DRA/SLC26A3 via EspG-dependent microtubule effects, suppresses SGLT1, and downregulates MCT1 and ASBT; SERT inhibition (via SHP2-mediated dephosphorylation) raises luminal 5-HT contributing to secretion. These changes impair electroneutral NaCl absorption and promote fluid loss. (URL: https://doi.org/10.5005/jp-journals-11002-0056, Apr 2023) (kaur2023pathophysiologyofenteropathogenic pages 11-12, kaur2023pathophysiologyofenteropathogenic pages 21-25)
- Inflammatory/ENS amplification: Innate activation (e.g., IL-8, NF-κB) recruits neutrophils; neutrophil-derived AMP is converted luminally to adenosine, a potent secretagogue that drives CFTR-dependent Cl− secretion. ENS secretomotor reflexes involving VIP, cholinergic transmitters, 5-HT, PGE2, and NO can sustain secretion in later phases of infection. (URL: https://doi.org/10.1152/ajpgi.2001.281.2.g303, Aug 2001) (morris2001viii.pathologicalconsequences pages 5-7)
- Viral mechanisms: Rotavirus NSP4 mobilizes intracellular Ca2+ and triggers early CFTR-independent secretion, with later ENS-mediated, cyclic nucleotide–dependent components; norovirus can drive ENS-linked secretory responses. (URL: https://doi.org/10.1152/ajpgi.2001.281.2.g303, Aug 2001) (morris2001viii.pathologicalconsequences pages 5-7)
- CEACAM interactions: Pathogenic E. coli adhesins (Afa/Dr family; FimH/type 1 pili) engage CEACAMs (notably CEACAM6), enhancing mucosal adherence; cyclic nucleotide signaling downstream of ETEC toxins converges on CFTR/NHE3 pathology. (URL: https://doi.org/10.3389/fimmu.2023.1120331, Feb 2023) (sheikh2023interactionsofpathogenic pages 2-3)

Recent Developments (2023–2024 highlights)
- EPEC transporter and barrier biology refined: 2023 review details inhibition of NHE3 and DRA, reduced SGLT1, MCT1, ASBT, and SERT dysregulation via SHP2, linking effector–host interactions to specific transporter defects and barrier loss. (Apr 2023) (kaur2023pathophysiologyofenteropathogenic pages 11-12, kaur2023pathophysiologyofenteropathogenic pages 21-25)
- ETEC signaling consolidated in epithelial models: 2024 experiments demonstrate STa (cGMP/PKG) and LT (cAMP/PKA) synergistically activate CFTR and inhibit NHE3; PKC/CaMKII and Ca2+-activated Cl− channels implicated for STb. (Jun 2024) (ye2024baicalinaluminumcomplexon pages 4-9)
- Mg2+-CaSR antisecretory strategy: 2024 JCI study shows luminal Mg2+ (10 mM) activates epithelial CaSR/Gq to drive PDE-mediated cAMP hydrolysis, suppressing CFTR Cl− secretion by ~65% in human T84 cells and ~50% against cholera toxin and ETEC ST, with in vivo efficacy (20 mM luminal Mg2+ reduced cholera toxin–induced fluid accumulation by ~40%; 10 mM converted net secretion to absorption in perfused mouse intestine). “Extracellular Mg2+…suppressed forskolin-induced Cl− secretion…by 65% at physiological levels…; Mg2+…also suppressed Cl− secretion induced by cholera toxin, heat-stable E. coli enterotoxin…by 50%…luminal Mg2+…inhibited cholera toxin–induced fluid accumulation by 40%…reversed net fluid transport from secretion to absorption.” (URL: https://doi.org/10.1172/jci171249, Jan 2024) (goncalves2024mg2+supplementationtreats pages 1-2, goncalves2024mg2+supplementationtreats pages 10-11, goncalves2024mg2+supplementationtreats pages 8-10, goncalves2024mg2+supplementationtreats pages 2-5)
- EAEC in travelers and AMR: Enhanced UK surveillance (2016–2023) shows EAEC diagnoses rose fivefold (93→524/year), with 1,402 notifications; 79% of cases with travel history had foreign travel within 7 days. AMR detected in 73.5% of isolates; common resistance to fluoroquinolones (57.8%) and β-lactams (57.6%); hybrid STEC/EAEC strains are a concern. (URL: https://doi.org/10.1099/jmm.0.002097, Nov 2025) (poh2025microbiologyandepidemiology pages 10-12)

Current Applications and Implementations
- Pathway-targeted therapies: The Mg2+-CaSR approach offers a mechanistically targeted, orally deliverable adjunct or modification to ORS for cyclic nucleotide–mediated secretory diarrheas (e.g., cholera, ETEC TD). Inclusion of ~10 mM Mg2+ in ORS suppressed CFTR-mediated secretion in perfused mouse intestine, with CaSR dependence demonstrated in epithelial-specific Casr knockout mice. (Jan 2024) (goncalves2024mg2+supplementationtreats pages 1-2, goncalves2024mg2+supplementationtreats pages 8-10)
- Supportive care optimization: Recognition that EPEC/ETEC impair Na+-coupled absorption (NHE3, SGLT1) and DRA underscores the rationale for glucose–electrolyte ORS and suggests potential benefit from butyrate/SCFA and bile acid transport modulation where appropriate. (Apr 2023; Jun 2024) (kaur2023pathophysiologyofenteropathogenic pages 11-12, ye2024baicalinaluminumcomplexon pages 4-9)
- Diagnostics/surveillance: Molecular panels detect EAEC/EPEC; surveillance highlights EAEC burden in travelers and high AMR, informing empiric therapy (e.g., azithromycin) and travel health guidance. (Nov 2025) (poh2025microbiologyandepidemiology pages 10-12)

Expert Opinions and Authoritative Analyses
- Mechanistic consolidation in EPEC pathogenesis emphasizes coordinated T3SS effector action targeting transport and barrier proteins, explaining malabsorptive and secretory components; this frames transporter-restorative and barrier-protective interventions as rational targets. (Apr 2023) (kaur2023pathophysiologyofenteropathogenic pages 11-12, kaur2023pathophysiologyofenteropathogenic pages 21-25)
- Translational antisecretory strategy: The 2024 JCI group positions CaSR as a central epithelial “brake” on cyclic nucleotide–driven secretion; Mg2+ appears to be the key physiological CaSR agonist at stool concentrations, providing a feasible, low-cost approach to mitigate CFTR-mediated fluid loss in TD. (Jan 2024) (goncalves2024mg2+supplementationtreats pages 1-2, goncalves2024mg2+supplementationtreats pages 2-5)
- EAEC epidemiology/AMR: National surveillance authors recommend adding EAEC to diagnostic algorithms given disease burden, traveler association, and high AMR prevalence, and warn about hybrid STEC/EAEC risk. (Nov 2025) (poh2025microbiologyandepidemiology pages 10-12)

Relevant Statistics and Data
- Mg2+-CaSR antisecretory efficacy: 10 mM Mg2+ reduced forskolin-induced CFTR-mediated Cl− secretion by ~65% in T84 cells; suppressed cholera toxin and ETEC ST responses by ~50%; luminal 20 mM Mg2+ lowered cholera loop fluid accumulation by ~40%; 10 mM Mg2+ in perfusate converted secretion to net absorption. (Jan 2024) (goncalves2024mg2+supplementationtreats pages 1-2, goncalves2024mg2+supplementationtreats pages 8-10)
- EAEC burden and AMR (UK 2016–2023): 1,402 EAEC notifications; fivefold increase in annual diagnoses (93→524); 79% of travel-history cases reported foreign travel within 7 days; AMR in 73.5% isolates, fluoroquinolone resistance 57.8%, β-lactam resistance 57.6%; travel to Indian subcontinent, Egypt, Morocco, Mexico common. (Nov 2025) (poh2025microbiologyandepidemiology pages 10-12)
- EPEC transporter impacts: Inhibition of NHE3 and DRA, SGLT1 suppression, SERT inhibition, reduced MCT1/ASBT—mechanistic basis for impaired NaCl absorption, reduced SCFA uptake, and enhanced 5-HT–driven secretion. (Apr 2023) (kaur2023pathophysiologyofenteropathogenic pages 11-12)

Mechanistic Map and Ontology-Linked Summary
| Pathogen/Trigger | Principal Toxins / Virulence | Primary Host Targets (HGNC where applicable) | Second Messengers | Key Cellular Processes (GO term names) | Affected Cell Types (CL term names) | Anatomical Sites (UBERON terms) | Notable Chemical Entities (CHEBI names) | Notes / Phenotypes (HP terms & evidence) |
|---|---|---|---|---|---|---|---|---|
| ETEC (STa / LT) | STa → GC-C activation; LT → ADP‑ribosylation → ↑cAMP; colonization fimbriae | GUCY2C (HGNC:4683); CFTR (HGNC:1884); SLC9A3 / NHE3 (HGNC:11076); SLC5A1 / SGLT1 (HGNC:11036) | cGMP (STa), cAMP (LT) | chloride transport; regulation of cAMP-mediated signaling; inhibition of Na+/H+ exchange; tight junction assembly (disruption) | enterocyte; intestinal goblet cell; submucosal secretomotor neuron | small intestine; jejunum; ileum | cGMP; cAMP; Ca2+ | Secretory watery diarrhea, NHE3 inhibition, dehydration (ye2024baicalinaluminumcomplexon pages 4-9, morris2001viii.pathologicalconsequences pages 5-7) |
| EAEC (AggR/AAF, Pic, EAST1) | Aggregative adherence fimbriae (AAFs), AggR-regulated factors; mucin/adhesion enzymes (Pic); EAST1 toxin in some strains | Host mucins/adhesion receptors (CEACAM family implicated in E. coli interactions); enterocyte surface glycoconjugates (no single HGNC) | Local signaling (NF-κB, IL-8), biofilm-associated signals | biofilm formation; actin cytoskeleton organization; inflammatory response | enterocyte; intestinal goblet cell; tuft cell | small intestine; colon | serotonin; bile acid | Prolonged/mucoid diarrhea, persistent colonization; high AMR carriage in EAEC from travellers (poh2025microbiologyandepidemiology pages 10-12) |
| EPEC (LEE / T3SS: EspF, Tir, Map, EspG) | Type III secretion effectors: Tir–intimin adhesion, EspF/Map/EspG disrupt junctions, mitochondrial and trafficking targets | CFTR (HGNC:1884) implicated indirectly; SLC9A3 / NHE3 (HGNC:11076) inhibited; SLC26A3 / DRA (HGNC:11059) reduced; SLC5A1 / SGLT1 (HGNC:11036) inhibited; NHERF2 interactions | Perturbation of local signaling (NF-κB), altered Ca2+-dependent cytoskeletal signaling | tight junction assembly (disruption); actin cytoskeleton organization; regulation of cAMP-mediated signaling; epithelial cell apoptosis | enterocyte; intestinal goblet cell; enteroendocrine cell | small intestine; jejunum; ileum | cAMP; cGMP; serotonin; bile acid | Attaching/effacing lesions, microvillus effacement, impaired NaCl absorption (NHE3/DRA/SGLT1), barrier loss → watery diarrhea (kaur2023pathophysiologyofenteropathogenic pages 11-12, kaur2023pathophysiologyofenteropathogenic pages 9-11) |
| Campylobacter jejuni | Invasion factors; cytolethal distending toxin (CDT); motility/adhesins → epithelial invasion and IL-8–driven neutrophilic inflammation | Tight junction proteins (claudins), epithelial receptors involved in invasion (no single HGNC), immune receptors on neutrophils | Proinflammatory mediators (IL-8), neutrophil-derived AMP → adenosine/secretagogue signaling | inflammatory response; epithelial cell apoptosis; actin cytoskeleton organization | enterocyte; neutrophil; submucosal secretomotor neuron | ileum; colon | adenosine; serotonin; bile acid | Inflammatory/bloody or inflammatory watery diarrhea; risk of post-infectious IBS (PI‑IBS) and sustained dysbiosis (morris2001viii.pathologicalconsequences pages 5-7, poh2025microbiologyandepidemiology pages 10-12) |
| Viral (Rotavirus NSP4; Norovirus) | Rotavirus NSP4 (viral enterotoxin → intracellular Ca2+ mobilization); noroviruses activate enteric secretion and ENS pathways | Enterocyte; enteric neurons; transporters are functionally affected (CFTR may be bypassed early) — CFTR (HGNC:1884) relevance varies | Ca2+ (NSP4); secondary cAMP/cGMP and ENS neurotransmitters (VIP, 5‑HT) | chloride transport; regulation of cAMP-mediated signaling; epithelial cell apoptosis; tight junction assembly (disruption) | enterocyte; enteroendocrine cell; submucosal secretomotor neuron | small intestine; jejunum | Ca2+; cAMP; cGMP; serotonin | Age-dependent secretory diarrhea (NSP4 Ca2+-dependent early phase; ENS-mediated later phase); NSP4 causes CFTR-independent secretion early (morris2001viii.pathologicalconsequences pages 5-7) |


*Table: Concise mechanism-to-ontology mapping for major travelers' diarrhea causes, summarizing toxins/virulence, host targets (HGNC), second messengers, GO processes, cell types (CL), anatomical sites (UBERON), key chemicals (CHEBI), and clinical phenotypes with source citations for each row.*

Key Molecular Players
- Genes/Proteins (HGNC): CFTR (HGNC:1884); GUCY2C/GC-C (HGNC:4683); SLC9A3/NHE3 (HGNC:11076); SLC26A3/DRA (HGNC:11059); SLC5A1/SGLT1 (HGNC:11036); CaSR (HGNC:1514). EPEC effectors: Tir, EspF, EspG, Map, NleA; ETEC toxins: LT (enterotoxin), STa (guanylin-mimetic); EAEC regulators/adhesins: AggR, aggregative adherence fimbriae (AAF). (kaur2023pathophysiologyofenteropathogenic pages 11-12, kaur2023pathophysiologyofenteropathogenic pages 21-25, ye2024baicalinaluminumcomplexon pages 4-9, goncalves2024mg2+supplementationtreats pages 1-2)
- Chemical entities (CHEBI): cAMP; cGMP; Ca2+; Mg2+; serotonin (5-HT); bile acid. (morris2001viii.pathologicalconsequences pages 5-7, ye2024baicalinaluminumcomplexon pages 4-9, goncalves2024mg2+supplementationtreats pages 1-2)
- Cell types (CL): enterocyte; intestinal goblet cell; enteroendocrine cell; submucosal secretomotor neuron; neutrophil. (morris2001viii.pathologicalconsequences pages 5-7, kaur2023pathophysiologyofenteropathogenic pages 11-12)
- Anatomical locations (UBERON): small intestine; jejunum; ileum; colon. (goncalves2024mg2+supplementationtreats pages 1-2, kaur2023pathophysiologyofenteropathogenic pages 11-12)

Biological Processes (GO annotations; disrupted)
- Chloride transport; regulation of cAMP-mediated signaling; regulation of cGMP-mediated signaling; positive regulation of CFTR activity; negative regulation of Na+/H+ exchange; tight junction assembly (disruption); actin cytoskeleton organization; inflammatory response; epithelial cell apoptosis; regulation of serotonin uptake. (kaur2023pathophysiologyofenteropathogenic pages 11-12, morris2001viii.pathologicalconsequences pages 5-7, ye2024baicalinaluminumcomplexon pages 4-9, goncalves2024mg2+supplementationtreats pages 1-2)

Cellular Components
- Apical plasma membrane (CFTR, NHE3, SGLT1); brush border/microvilli; tight junctions (claudins, ZO-1/ZO-2); basolateral K+ channels; endoplasmic reticulum (NSP4/Ca2+ mobilization); T3SS translocon at epithelial membrane. (kaur2023pathophysiologyofenteropathogenic pages 11-12, morris2001viii.pathologicalconsequences pages 5-7, goncalves2024mg2+supplementationtreats pages 1-2)

Disease Progression Model
- Exposure and colonization: Pathogen ingestion → mucosal adherence via fimbriae/adhesins (e.g., ETEC colonization factors; EAEC AAF; EPEC intimin/Tir). (kaur2023pathophysiologyofenteropathogenic pages 11-12, poh2025microbiologyandepidemiology pages 10-12)
- Toxin/effectors and signaling: ETEC STa/LT trigger cGMP/cAMP, activating CFTR and inhibiting NHE3; EPEC T3SS effectors disrupt junctions and transporters; viral NSP4 mobilizes Ca2+. (ye2024baicalinaluminumcomplexon pages 4-9, kaur2023pathophysiologyofenteropathogenic pages 11-12, morris2001viii.pathologicalconsequences pages 5-7)
- Barrier and transport failure: Reduced DRA/SLC26A3 and SGLT1 impair electroneutral NaCl and glucose-coupled absorption; SERT inhibition enhances 5-HT; microvillus effacement and junctional disassembly increase permeability. (kaur2023pathophysiologyofenteropathogenic pages 11-12)
- Amplification: ENS and inflammatory mediators (VIP, 5-HT, PGE2, NO; neutrophil-derived adenosine) sustain secretion. (morris2001viii.pathologicalconsequences pages 5-7)
- Clinical manifestation: Acute watery diarrhea (often voluminous), cramping, dehydration; EAEC can be prolonged/persistent. (poh2025microbiologyandepidemiology pages 10-12)

Phenotypic Manifestations (HP terms)
- Diarrhea (HP:0002014); Dehydration (HP:0001944); Abdominal cramping (HP:0002027); Intestinal malabsorption (HP:0002571); Increased intestinal fluid secretion (pathophysiologic phenotype). Mechanistic associations supported by transporter dysfunction (NHE3/DRA/SGLT1), CFTR activation, and ENS/inflammatory pathways. (kaur2023pathophysiologyofenteropathogenic pages 11-12, morris2001viii.pathologicalconsequences pages 5-7, ye2024baicalinaluminumcomplexon pages 4-9, goncalves2024mg2+supplementationtreats pages 1-2)

Evidence Items (selected, with URLs and dates)
- EPEC pathophysiology (transporters/barrier): Kaur & Dudeja, Newborn, Apr 2023. URL: https://doi.org/10.5005/jp-journals-11002-0056 (kaur2023pathophysiologyofenteropathogenic pages 11-12, kaur2023pathophysiologyofenteropathogenic pages 21-25)
- ETEC signaling and epithelial responses: Ye et al., Heliyon, Jun 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e33038 (ye2024baicalinaluminumcomplexon pages 4-9)
- Mg2+-CaSR antisecretory therapy: de Souza Goncalves et al., JCI, Jan 2024. URL: https://doi.org/10.1172/jci171249 (goncalves2024mg2+supplementationtreats pages 1-2, goncalves2024mg2+supplementationtreats pages 8-10, goncalves2024mg2+supplementationtreats pages 2-5)
- Viral/ENS mechanisms: Morris & Estes, AJP-GI, Aug 2001. URL: https://doi.org/10.1152/ajpgi.2001.281.2.g303 (morris2001viii.pathologicalconsequences pages 5-7)
- CEACAM interactions: Sheikh & Fleckenstein, Front. Immunol., Feb 2023. URL: https://doi.org/10.3389/fimmu.2023.1120331 (sheikh2023interactionsofpathogenic pages 2-3)
- EAEC epidemiology and AMR (travel-associated): Poh et al., J. Med. Microbiol., Nov 2025. URL: https://doi.org/10.1099/jmm.0.002097 (poh2025microbiologyandepidemiology pages 10-12)

Gaps and Open Questions
- Campylobacter- and norovirus-specific epithelial signaling in TD requires further recent primary studies to detail transporter-level effects and post-infectious sequelae risk in travelers; however, inflammatory and ENS-mediated mechanisms that amplify secretion are well-supported. (morris2001viii.pathologicalconsequences pages 5-7)

Conclusions
TD pathophysiology reflects convergent mechanisms that activate CFTR and disable NaCl/solute absorption, compounded by barrier injury and neuro-immune amplification. The 2023–2024 literature refines EPEC transporter pathobiology and consolidates ETEC cyclic-nucleotide signaling, while a 2024 translational study identifies Mg2+-CaSR activation as a promising, physiology-aligned antisecretory strategy suitable for ORS enhancement. Concurrently, EAEC remains a common, often travel-associated pathogen with substantial AMR burden, underscoring the need for sustained surveillance and judicious antimicrobial use. (kaur2023pathophysiologyofenteropathogenic pages 11-12, kaur2023pathophysiologyofenteropathogenic pages 21-25, ye2024baicalinaluminumcomplexon pages 4-9, poh2025microbiologyandepidemiology pages 10-12, goncalves2024mg2+supplementationtreats pages 1-2, goncalves2024mg2+supplementationtreats pages 8-10)

References

1. (kaur2023pathophysiologyofenteropathogenic pages 11-12): Prabhdeep Kaur and Pradeep K Dudeja. Pathophysiology of enteropathogenic escherichia coli-induced diarrhea. Newborn (Clarksville, Md.), 2:102-113, Apr 2023. URL: https://doi.org/10.5005/jp-journals-11002-0056, doi:10.5005/jp-journals-11002-0056. This article has 28 citations.

2. (kaur2023pathophysiologyofenteropathogenic pages 21-25): Prabhdeep Kaur and Pradeep K Dudeja. Pathophysiology of enteropathogenic escherichia coli-induced diarrhea. Newborn (Clarksville, Md.), 2:102-113, Apr 2023. URL: https://doi.org/10.5005/jp-journals-11002-0056, doi:10.5005/jp-journals-11002-0056. This article has 28 citations.

3. (ye2024baicalinaluminumcomplexon pages 4-9): Chun Ye, Yuqian Chen, Ruixue Yu, Ming Zhao, Ronghua Yin, Yinsheng Qiu, Shulin Fu, Yu Liu, and Zhongyuan Wu. Baicalin-aluminum complex on the regulation of ipec-1 infected with enterotoxigenic escherichia coli. Heliyon, 10:e33038, Jun 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e33038, doi:10.1016/j.heliyon.2024.e33038. This article has 4 citations and is from a peer-reviewed journal.

4. (poh2025microbiologyandepidemiology pages 10-12): Ching-Ying J. Poh, Ella V. Rodwell, David R. Greig, Satheesh Nair, Marie A. Chattaway, and Claire Jenkins. Microbiology and epidemiology of enteroaggregative escherichia coli isolated from uk residents in england, 2016–2023: what are the risks to public health? Journal of Medical Microbiology, Nov 2025. URL: https://doi.org/10.1099/jmm.0.002097, doi:10.1099/jmm.0.002097. This article has 0 citations and is from a peer-reviewed journal.

5. (goncalves2024mg2+supplementationtreats pages 1-2): Livia de Souza Goncalves, Tifany Chu, Riya Master, Parth D. Chhetri, Qi Gao, and Onur Cil. Mg2+ supplementation treats secretory diarrhea in mice by activating calcium-sensing receptor in intestinal epithelial cells. Journal of Clinical Investigation, Jan 2024. URL: https://doi.org/10.1172/jci171249, doi:10.1172/jci171249. This article has 9 citations and is from a highest quality peer-reviewed journal.

6. (goncalves2024mg2+supplementationtreats pages 8-10): Livia de Souza Goncalves, Tifany Chu, Riya Master, Parth D. Chhetri, Qi Gao, and Onur Cil. Mg2+ supplementation treats secretory diarrhea in mice by activating calcium-sensing receptor in intestinal epithelial cells. Journal of Clinical Investigation, Jan 2024. URL: https://doi.org/10.1172/jci171249, doi:10.1172/jci171249. This article has 9 citations and is from a highest quality peer-reviewed journal.

7. (morris2001viii.pathologicalconsequences pages 5-7): Andrew P. Morris and Mary K. Estes. Viii. pathological consequences of rotavirus infection and its enterotoxin. American Journal of Physiology-Gastrointestinal and Liver Physiology, 281:G303-G310, Aug 2001. URL: https://doi.org/10.1152/ajpgi.2001.281.2.g303, doi:10.1152/ajpgi.2001.281.2.g303. This article has 68 citations.

8. (sheikh2023interactionsofpathogenic pages 2-3): Alaullah Sheikh and James M. Fleckenstein. Interactions of pathogenic escherichia coli with ceacams. Frontiers in Immunology, Feb 2023. URL: https://doi.org/10.3389/fimmu.2023.1120331, doi:10.3389/fimmu.2023.1120331. This article has 12 citations and is from a peer-reviewed journal.

9. (goncalves2024mg2+supplementationtreats pages 10-11): Livia de Souza Goncalves, Tifany Chu, Riya Master, Parth D. Chhetri, Qi Gao, and Onur Cil. Mg2+ supplementation treats secretory diarrhea in mice by activating calcium-sensing receptor in intestinal epithelial cells. Journal of Clinical Investigation, Jan 2024. URL: https://doi.org/10.1172/jci171249, doi:10.1172/jci171249. This article has 9 citations and is from a highest quality peer-reviewed journal.

10. (goncalves2024mg2+supplementationtreats pages 2-5): Livia de Souza Goncalves, Tifany Chu, Riya Master, Parth D. Chhetri, Qi Gao, and Onur Cil. Mg2+ supplementation treats secretory diarrhea in mice by activating calcium-sensing receptor in intestinal epithelial cells. Journal of Clinical Investigation, Jan 2024. URL: https://doi.org/10.1172/jci171249, doi:10.1172/jci171249. This article has 9 citations and is from a highest quality peer-reviewed journal.

11. (kaur2023pathophysiologyofenteropathogenic pages 9-11): Prabhdeep Kaur and Pradeep K Dudeja. Pathophysiology of enteropathogenic escherichia coli-induced diarrhea. Newborn (Clarksville, Md.), 2:102-113, Apr 2023. URL: https://doi.org/10.5005/jp-journals-11002-0056, doi:10.5005/jp-journals-11002-0056. This article has 28 citations.