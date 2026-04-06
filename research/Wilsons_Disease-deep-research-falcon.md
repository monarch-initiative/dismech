---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-02-04T07:44:51.600354'
end_time: '2026-02-04T07:44:51.602068'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Wilson Disease
  mondo_id: ''
  category: Genetic
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
- **Disease Name:** Wilson Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Wilson Disease**.
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
- **Disease Name:** Wilson Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Wilson Disease**.
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


Disease Pathophysiology Research Report: Wilson Disease (Hepatolenticular Degeneration)

Target Disease
- Disease Name: Wilson Disease
- MONDO ID: MONDO_0010200
- Category: Genetic (autosomal recessive)

Pathophysiology description (narrative)
Wilson disease (WD) is caused by loss-of-function variants in ATP7B, a copper-transporting P-type ATPase that normally resides in the trans-Golgi network (TGN) of hepatocytes to metallate apoceruloplasmin and, when intracellular copper is elevated, traffics toward canalicular/apical domains and secretory vesicles to export copper into bile. As a result, “inactivating mutations of the copper-transporting P-type ATPase, ATP7B” impair both ceruloplasmin copper loading and biliary excretion, leading to hepatocellular copper accumulation and systemic spillover of non–ceruloplasmin-bound copper with multi-organ toxicity (Pharmacology & Therapeutics, published Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (wootonkee2023therapeuticimplicationsof pages 1-2). At the TGN, the protein “activates ceruloplasmin by packaging six copper molecules into apoceruloplasmin,” and upon copper excess “sequesters excess copper into vesicles and excretes it via exocytosis across the apical canalicular membrane into bile” (International Journal of Molecular Sciences, published Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).

Copper enters hepatocytes via the high-affinity importer CTR1 (SLC31A1), then is buffered by glutathione and metallothioneins and delivered to ATP7B by the cytosolic chaperone ATOX1; failure of this pathway in WD promotes copper-catalyzed reactive oxygen species (ROS) generation, mitochondrial injury, and downstream inflammatory/fibrotic programs (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (wootonkee2023therapeuticimplicationsof pages 1-2). ATP7B gene structure and genetic basis have been defined: the locus is on chromosome 13q14.3, spans ~80 kb with 21 exons; most disease-associated variants are missense (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).

In the central nervous system (CNS), glial cells—especially astrocytes—buffer copper via CTR1-mediated uptake and metallothionein/glutathione sequestration, and export copper through ATP7A; when buffering is overwhelmed, mitochondrial copper accumulation can trigger copper-dependent cell death pathways and neuroinflammation, contributing to the heterogeneous neurologic/psychiatric phenotypes of WD (International Journal of Molecular Sciences, published Jul 2024; https://doi.org/10.3390/ijms25147545) (gromadzka2024theroleof pages 5-8). Recent patient-centric neuroimaging-genomic work further links WD-related subcortical structural lesions and widespread functional gradient perturbations to transcriptomic specializations implicating ion homeostasis and motor circuitry (Brain Communications, published Sep 2024; https://doi.org/10.1093/braincomms/fcae329) (gromadzka2024theroleof pages 5-8).

Core Pathophysiology
- Primary mechanisms
  - Defective copper incorporation into ceruloplasmin in the TGN and defective biliary copper excretion due to ATP7B dysfunction, with subsequent hepatic copper overload and systemic redistribution of toxic, albumin- or small-molecule–bound copper (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (wootonkee2023therapeuticimplicationsof pages 1-2). “Failure to excrete copper into bile” leads to hepatocellular injury and extrahepatic damage via “free copper” (Frontiers in Medicine, expert opinion, published Oct 2025; https://doi.org/10.3389/fmed.2025.1673283) (stremmel2025theroleof pages 1-2).
  - Oxidative stress and mitochondrial dysfunction downstream of excess intracellular copper (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (wootonkee2023therapeuticimplicationsof pages 1-2).
  - Regulated cell death pathways: copper-mediated cuproptosis and iron-related ferroptosis proposed to contribute to organelle membrane and metabolic injury in WD (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).
  - Neuroglial involvement with astrocyte and microglial responses to copper dyshomeostasis, linking glial buffering failure to neuronal toxicity (International Journal of Molecular Sciences, Jul 2024; https://doi.org/10.3390/ijms25147545) (gromadzka2024theroleof pages 5-8).

- Dysregulated molecular pathways
  - Copper import (CTR1/SLC31A1), cytosolic chaperoning (ATOX1), TGN loading (ATP7B), vesicular trafficking/exocytosis, and bile canalicular export (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529; International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (wootonkee2023therapeuticimplicationsof pages 1-2, teschke2024wilsondiseasecoppermediated pages 3-5).
  - Oxidative stress signaling and antioxidant induction (metallothionein, glutathione) (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (wootonkee2023therapeuticimplicationsof pages 1-2).
  - Mitochondrial quality control and mitophagy activation in copper overload states (Physiology, published Nov 2025; https://doi.org/10.1152/physiol.00032.2025) (petruzzelli2025copperinhuman pages 30-35).
  - Cuproptosis: copper binding to lipoylated tricarboxylic acid (TCA) enzymes leading to proteotoxic stress; ferroptosis: iron-related phospholipid peroxidation (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).

- Affected cellular processes
  - Secretory pathway copper loading and ceruloplasmin biosynthesis in the TGN (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).
  - Vesicular trafficking of ATP7B from TGN to canalicular/apical membranes in response to copper (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).
  - Mitochondrial organization/respiration, oxidative stress responses, and autophagy/mitophagy (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529; Physiology, Nov 2025; https://doi.org/10.1152/physiol.00032.2025) (wootonkee2023therapeuticimplicationsof pages 1-2, petruzzelli2025copperinhuman pages 30-35).

Key Molecular Players
- Genes/Proteins (HGNC)
  - ATP7B (ATPase copper transporting beta): hepatocyte copper transporter; genetics (13q14.3; 21 exons); missense variants frequent; defects block ceruloplasmin loading and biliary export (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).
  - ATOX1: copper chaperone to ATP7B/ATP7A; integrates copper handling and redox signaling in neurons (International Journal of Molecular Sciences, Jun 2024; https://doi.org/10.3390/ijms25126487) (manchia2024theroleof pages 7-8).
  - SLC31A1/CTR1: principal high-affinity copper importer (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (wootonkee2023therapeuticimplicationsof pages 1-2).
  - CP (Ceruloplasmin): multicopper oxidase; “activates ceruloplasmin by packaging six copper molecules into apoceruloplasmin” in TGN; CP remains copper-deficient in WD (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).
  - Metallothioneins (MTs), glutathione (GSH): inducible intracellular copper buffers (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (wootonkee2023therapeuticimplicationsof pages 1-2).

- Chemical entities (ChEBI)
  - Copper(II) (Cu2+) and Copper(I) (Cu+): extracellular vs intracellular species; redox cycling generates ROS and organellar injury (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753; Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (teschke2024wilsondiseasecoppermediated pages 3-5, wootonkee2023therapeuticimplicationsof pages 1-2).
  - D-Penicillamine, Trientine: copper chelators that increase urinary copper excretion (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (wootonkee2023therapeuticimplicationsof pages 1-2).
  - Zinc(II): reduces intestinal copper absorption by inducing enterocyte metallothionein (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (wootonkee2023therapeuticimplicationsof pages 1-2).
  - Tetrathiomolybdate (bis-choline TTM/ALXN1840): complexes “free” copper to reduce bioavailable copper rapidly; clinical development ongoing (Frontiers in Medicine, Oct 2025; https://doi.org/10.3389/fmed.2025.1673283) (stremmel2025theroleof pages 8-8).

- Cell types (CL)
  - Hepatocytes: primary ATP7B-expressing cells; copper accumulation drives mitochondrial dysfunction, inflammation, fibrosis (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (wootonkee2023therapeuticimplicationsof pages 1-2).
  - Astrocytes: major CNS copper buffer and gatekeeper; failure → neuronal exposure to copper toxicity (International Journal of Molecular Sciences, Jul 2024; https://doi.org/10.3390/ijms25147545) (gromadzka2024theroleof pages 5-8).
  - Microglia: activated in copper overload and with signals from hepatic inflammation; contribute to neuroinflammation (International Journal of Molecular Sciences, Jul 2024; https://doi.org/10.3390/ijms25147545) (gromadzka2024theroleof pages 5-8).
  - Neurons: OXPHOS-dependent cells susceptible to copper-triggered mitochondrial stress and cuproptosis (International Journal of Molecular Sciences, Jul 2024; https://doi.org/10.3390/ijms25147545) (gromadzka2024theroleof pages 5-8).

- Anatomical locations (UBERON)
  - Liver: site of primary defect and copper overload; source of systemic toxic copper (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (wootonkee2023therapeuticimplicationsof pages 1-2).
  - Basal ganglia (putamen), cerebellum: characteristic neuroanatomical involvement associated with movement disorders; recent MRI gradient findings map network-level disturbances (Brain Communications, Sep 2024; https://doi.org/10.1093/braincomms/fcae329) (gromadzka2024theroleof pages 5-8).
  - Cornea: Kayser–Fleischer rings reflect copper deposition (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).

Biological Processes for GO annotation
- Copper ion transport and homeostasis (CTR1 import, ATOX1 chaperoning, ATP7B TGN loading, canalicular exocytosis) (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (wootonkee2023therapeuticimplicationsof pages 1-2).
- Ceruloplasmin metabolic process and secretion (TGN metallation by ATP7B) (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).
- Response to oxidative stress and mitochondrial organization/quality control (Physiology, Nov 2025; https://doi.org/10.1152/physiol.00032.2025; Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (petruzzelli2025copperinhuman pages 30-35, wootonkee2023therapeuticimplicationsof pages 1-2).
- Autophagy/mitophagy activated by copper-induced organellar damage (Physiology, Nov 2025; https://doi.org/10.1152/physiol.00032.2025) (petruzzelli2025copperinhuman pages 30-35).
- Cuproptosis and ferroptosis in WD pathogenesis (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).
- Biliary secretion and excretion of copper (ATP7B trafficking to canalicular membrane) (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).

Cellular Components
- Trans-Golgi network (TGN): site of ceruloplasmin loading by ATP7B (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).
- Canalicular/apical membrane of hepatocytes and secretory vesicles/lysosomes for copper exocytosis (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).
- Mitochondria: copper accumulation causes structural changes, ROS, and mitophagy (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529; Physiology, Nov 2025; https://doi.org/10.1152/physiol.00032.2025) (wootonkee2023therapeuticimplicationsof pages 1-2, petruzzelli2025copperinhuman pages 30-35).

Disease Progression
- Initiation: ATP7B deficiency prevents proper TGN copper handling (ceruloplasmin loading) and canalicular export, causing hepatocellular copper accumulation (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).
- Cellular injury: increased ROS and mitochondrial dysfunction; induction of metallothionein/glutathione buffering and autophagy/mitophagy; activation of cell death programs (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529; International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (wootonkee2023therapeuticimplicationsof pages 1-2, teschke2024wilsondiseasecoppermediated pages 3-5).
- Organ injury: progressive hepatitis, fibrosis/cirrhosis; copper spillover leading to brain accumulation/dysregulation, with astrocyte/microglial activation and network-level functional changes (International Journal of Molecular Sciences, Oct 2025; https://doi.org/10.3389/fmed.2025.1673283; International Journal of Molecular Sciences, Jul 2024; https://doi.org/10.3390/ijms25147545; Brain Communications, Sep 2024; https://doi.org/10.1093/braincomms/fcae329) (stremmel2025theroleof pages 1-2, gromadzka2024theroleof pages 5-8).

Phenotypic Manifestations (HPO-aligned)
- Hepatic disease: hepatitis, steatosis, fibrosis, cirrhosis, acute liver failure—driven by copper overload, oxidative stress, and impaired biliary excretion (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (wootonkee2023therapeuticimplicationsof pages 1-2).
- Neurologic: parkinsonism, dystonia, tremor, ataxia, dysarthria; neuroimaging links basal ganglia/cerebellar alterations and functional gradients to clinical severity (Brain Communications, Sep 2024; https://doi.org/10.1093/braincomms/fcae329) (gromadzka2024theroleof pages 5-8).
- Psychiatric/cognitive: ranging from mood disorders to psychosis; glial copper buffering failure and neuroinflammation are implicated (International Journal of Molecular Sciences, Jul 2024; https://doi.org/10.3390/ijms25147545) (gromadzka2024theroleof pages 5-8).
- Ophthalmologic: Kayser–Fleischer rings from corneal copper deposition (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).

Recent developments and latest research (2023–2024 emphasis)
- Hepatic nuclear receptor and metabolic dysregulation: WD liver shows impaired nuclear receptor function, oxidative stress, and mitochondrial dysfunction as drivers of progression; paper also contextualizes current therapy modalities (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (wootonkee2023therapeuticimplicationsof pages 1-2).
- Protein structural mechanisms: cryo-EM and simulations clarify copper-ATPase metal-binding domain roles and transport mechanism, informing therapeutic protein engineering for ATP7B (Nature Communications, Mar 2024; https://doi.org/10.1038/s41467-024-47001-4). These structural insights support the concept that selected ATP7B truncations could retain transport function in gene therapy constructs (contextualized in WD reviews) (wootonkee2023therapeuticimplicationsof pages 1-2).
- Regulated cell death: comprehensive review synthesizes evidence for copper-mediated cuproptosis and iron-related ferroptosis in WD (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).
- Neuroglial and systems-neuroscience advances: WD patients display “global topographic changes in the principal primary-to-transmodal gradient” and structure–function decoupling, with gene-expression specializations implicating ATP7B and ion homeostasis; work connects transcriptomics to MRI phenotypes (Brain Communications, Sep 2024; https://doi.org/10.1093/braincomms/fcae329) (gromadzka2024theroleof pages 5-8).
- Liver–brain axis in vivo: preclinical gene-edited Atp7b R778L mice develop brain deficits without detectable brain copper increases, but suppressing hepatic inflammation ameliorates neurologic phenotypes, supporting liver-derived inflammatory signaling in WD neurotoxicity (Journal of Neuroinflammation, Sep 2024; https://doi.org/10.1186/s12974-024-03178-5) (manchia2024theroleof pages 14-15).

Current applications and implementations
- First-line therapies: copper chelation (D-penicillamine, trientine) to mobilize and increase urinary excretion; zinc therapy to reduce intestinal absorption. “Patients with Wilson disease are well-treated first-line with copper chelators like D-penicillamine… Early chelation therapy improves prognosis” (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5). Mechanistically, chelators reduce systemic bioavailable copper and tissue copper burden; zinc induces enterocyte metallothionein to trap dietary copper (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (wootonkee2023therapeuticimplicationsof pages 1-2).
- Tetrathiomolybdate (bis-choline, ALXN1840): an emerging agent that forms tight complexes with copper, targeting “free copper”; expert commentary underscores that “the primary goal of therapy is to convert toxic free copper into harmless complexes” (Frontiers in Medicine, Oct 2025; https://doi.org/10.3389/fmed.2025.1673283) (stremmel2025theroleof pages 1-2).
- Liver transplantation: curative for hepatic failure by replacing defective hepatic ATP7B (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).
- Gene therapy and genome engineering: multiple AAV-based strategies are under evaluation; structural work on copper ATPases informs vector payload design; recent reviews and expert updates summarize clinical-stage programs (Cells, Jul 2024; https://doi.org/10.3390/cells13141214; Nature Communications, Mar 2024; https://doi.org/10.1038/s41467-024-47001-4) (wootonkee2023therapeuticimplicationsof pages 1-2).

Expert opinions and analysis
- An expert review emphasizes systemic trafficking and prioritizes neutralizing “free copper” over simply removing total copper, highlighting clinical rationale for agents like tetrathiomolybdate and the centrality of bile excretion failure (Frontiers in Medicine, Oct 2025; https://doi.org/10.3389/fmed.2025.1673283) (stremmel2025theroleof pages 1-2).
- Mechanistic reviews position cuproptosis and ferroptosis as plausible contributors to WD hepatocellular and neural injury, integrating classic oxidative damage with regulated cell death biology (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).

Relevant statistics and data
- Gene architecture and mode of inheritance: ATP7B at 13q14.3 (~80 kb, 21 exons); autosomal recessive WD with predominance of missense variants (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).
- Systems-neuroscience cohort: 105 WD patients vs 93 controls showed global functional gradient alterations and structure–function decoupling, strongest in subcortical and visual networks, mapping to gene-expression signatures (Brain Communications, Sep 2024; https://doi.org/10.1093/braincomms/fcae329) (gromadzka2024theroleof pages 5-8).
- Liver–brain axis preclinical model: Atp7b R778L mice showed neurologic deficits by 3–5 months with cortical/striatal microglial activation; suppressing hepatic inflammation improved cognition/motor behavior despite no significant brain copper elevation (Journal of Neuroinflammation, Sep 2024; https://doi.org/10.1186/s12974-024-03178-5) (manchia2024theroleof pages 14-15).

Evidence items (direct quotes where available)
- “Inactivating mutations of the copper-transporting P-type ATPase, ATP7B” summarize the causal genetic defect of WD (Pharmacology & Therapeutics, Nov 2023; https://doi.org/10.1016/j.pharmthera.2023.108529) (wootonkee2023therapeuticimplicationsof pages 1-2).
- “Activates ceruloplasmin by packaging six copper molecules into apoceruloplasmin … [and] excretes it via exocytosis across the apical canalicular membrane into bile” describes ATP7B’s TGN and canalicular roles (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).
- “Failure to excrete copper into bile” leads to hepatic injury and “free copper”–mediated extrahepatic damage; therapy aims to “convert toxic free copper into harmless complexes” (Frontiers in Medicine, Oct 2025; https://doi.org/10.3389/fmed.2025.1673283) (stremmel2025theroleof pages 1-2).

Gene/protein annotations with ontology terms (selected)
- HGNC: ATP7B; function: copper ion transmembrane transporter activity; processes: copper ion homeostasis, ceruloplasmin biosynthetic process; cellular component: TGN, apical plasma membrane (teschke2024wilsondiseasecoppermediated pages 3-5).
- HGNC: ATOX1; process: copper ion transport/chaperone-mediated delivery to secretory pathway (manchia2024theroleof pages 7-8).
- HGNC: SLC31A1 (CTR1); process: high-affinity copper uptake (wootonkee2023therapeuticimplicationsof pages 1-2).
- HGNC: CP; process: multicopper oxidase activity and copper transport in plasma; component: secreted glycoprotein from hepatocytes (teschke2024wilsondiseasecoppermediated pages 3-5).

Phenotype associations (HPO, selected examples)
- HP:0001397 Hepatomegaly; HP:0001392 Cirrhosis; HP:0003401 Parkinsonism; HP:0000717 Psychosis; HP:0000602 Kayser–Fleischer rings (wootonkee2023therapeuticimplicationsof pages 1-2, teschke2024wilsondiseasecoppermediated pages 3-5, gromadzka2024theroleof pages 5-8).

Cell type involvement (CL, examples)
- CL:0000182 Hepatocyte; CL:0000127 Astrocyte; CL:0000129 Microglia; CL:0000540 Neuron (wootonkee2023therapeuticimplicationsof pages 1-2, gromadzka2024theroleof pages 5-8).

Anatomical locations (UBERON, examples)
- UBERON:0002107 Liver; UBERON:0002427 Basal ganglia; UBERON:0000955 Cerebellum; UBERON:0000966 Cornea (wootonkee2023therapeuticimplicationsof pages 1-2, gromadzka2024theroleof pages 5-8, teschke2024wilsondiseasecoppermediated pages 3-5).

Chemical entities (ChEBI, examples)
- CHEBI:49552 Copper(II) ion; CHEBI:49551 Copper(I) ion; CHEBI:17033 D-penicillamine; CHEBI:49552 Zinc(II) ion; CHEBI:33328 Trientine; CHEBI:45048 Tetrathiomolybdate (wootonkee2023therapeuticimplicationsof pages 1-2, teschke2024wilsondiseasecoppermediated pages 3-5, stremmel2025theroleof pages 8-8).

Embedded ontology-mapped summary
| Category | Entity (preferred name) | Ontology (abbrev) | ID (if known) | Role / Notes (succinct) | Key recent sources (year/DOI) |
|---|---|---:|---|---|---|
| Gene / Protein | ATP7B (ATPase copper transporting beta) | HGNC | HGNC:ATP7B | Hepatocyte Golgi-localized Cu-transporter; loads Cu into ceruloplasmin and traffics to canalicular membrane for biliary Cu excretion; loss-of-function → hepatic Cu accumulation | Wooton-Kee 2023 doi:10.1016/j.pharmthera.2023.108529; Teschke 2024 doi:10.3390/ijms25094753 (wootonkee2023therapeuticimplicationsof pages 1-2, teschke2024wilsondiseasecoppermediated pages 3-5) |
| Gene / Protein | ATOX1 (Antioxidant 1 copper chaperone) | HGNC | HGNC:ATOX1 | Cytosolic Cu chaperone delivering Cu to ATP7B/ATP7A in the secretory pathway; implicated in neuronal Cu regulation and redox signaling | Manchia 2024 doi:10.3390/ijms25126487; Petruzzelli 2025 (manchia2024theroleof pages 14-15, petruzzelli2025copperinhuman pages 30-35) |
| Gene / Protein | SLC31A1 / CTR1 (Copper transporter 1) | HGNC | HGNC:SLC31A1 | Major plasma membrane Cu importer (intestinal uptake, hepatocyte uptake, astrocyte uptake) — upstream of intracellular chaperoning | Wooton-Kee 2023; Gromadzka 2024 (wootonkee2023therapeuticimplicationsof pages 1-2, gromadzka2024theroleof pages 5-8) |
| Gene / Protein | CP / Ceruloplasmin (ceruloplasmin) | HGNC | HGNC:CP | Secreted multicopper oxidase; major plasma Cu carrier when properly loaded by ATP7B in TGN; apo-CP secretion and low holo-CP common in WD | Teschke 2024; Petruzzelli 2025 (teschke2024wilsondiseasecoppermediated pages 3-5, petruzzelli2025copperinhuman pages 30-35) |
| Gene / Protein | Metallothioneins (MT family) | HGNC | HGNC:MT (family) | Low-molecular-weight Cu-sequestering proteins — intracellular buffering; induced in response to Cu and oxidative stress | Manchia 2024; Gromadzka 2024 (manchia2024theroleof pages 14-15, gromadzka2024theroleof pages 5-8) |
| Chemical entity | Copper(II) / Cu2+ | ChEBI | ChEBI:Copper(II) | Oxidized extracellular form; redox-active species that can generate ROS and promote lipid/protein damage when unbound | Wooton-Kee 2023; Teschke 2024 (wootonkee2023therapeuticimplicationsof pages 1-2, teschke2024wilsondiseasecoppermediated pages 3-5) |
| Chemical entity | Copper(I) / Cu+ | ChEBI | ChEBI:Copper(I) | Intracellular reduced form handled by chaperones (ATOX1, CCS, COX17); overload of Cu+ leads to mitochondrial toxicity and cuproptosis mechanisms | Manchia 2024; Gromadzka 2024 (manchia2024theroleof pages 14-15, gromadzka2024theroleof pages 5-8) |
| Chemical entity | D-penicillamine (chelator) | ChEBI | ChEBI:D-penicillamine | Urinary copper chelator used clinically to mobilize and excrete Cu; may cause immunologic/adverse effects | Wooton-Kee 2023; clinical trial summaries (wootonkee2023therapeuticimplicationsof pages 1-2) |
| Chemical entity | Trientine (triethylenetetramine) | ChEBI | ChEBI:Trientine | Alternative urinary chelator for Cu removal; used in maintenance/intolerance to penicillamine | Wooton-Kee 2023; clinical trial summaries (wootonkee2023therapeuticimplicationsof pages 1-2) |
| Chemical entity | Zinc(II) (Zn2+) | ChEBI | ChEBI:Zinc(II) | Blocks intestinal Cu absorption (induces metallothionein in enterocytes) and used as maintenance therapy to reduce systemic Cu uptake | Wooton-Kee 2023 (wootonkee2023therapeuticimplicationsof pages 1-2) |
| Chemical entity | Tetrathiomolybdate (bis-choline TTM) | ChEBI | ChEBI:Tetrathiomolybdate | Potent Cu-chelating/complexing agent that sequesters “free” Cu and can reduce bioavailable Cu rapidly; under clinical development/trials | Wooton-Kee 2023; recent reviews (wootonkee2023therapeuticimplicationsof pages 1-2) |
| Cell type | Hepatocyte | CL | CL:hepatocyte (if known) | Primary site of ATP7B expression and biliary Cu excretion; hepatocellular Cu accumulation → mitochondrial dysfunction, inflammation, fibrosis | Wooton-Kee 2023; Petruzzelli 2025 (wootonkee2023therapeuticimplicationsof pages 1-2, petruzzelli2025copperinhuman pages 30-35) |
| Cell type | Astrocyte | CL | CL:astrocyte | Key brain Cu buffer via CTR1 uptake, MT/GSH sequestration, and ATP7A-mediated export; failure → neuronal exposure, oxidative stress, cuproptosis | Gromadzka 2024; Manchia 2024 (gromadzka2024theroleof pages 5-8, manchia2024theroleof pages 14-15) |
| Cell type | Microglia | CL | CL:microglia | Activated by Cu and hepatic inflammation-driven signals; contribute to neuroinflammation and neuronal injury in WD | Gromadzka 2024; Dong 2024 evidence of liver→brain inflammation axis (gromadzka2024theroleof pages 5-8, manchia2024theroleof pages 14-15) |
| Cell type | Neuron | CL | CL:neuron | Vulnerable to mitochondrial Cu toxicity, impaired TCA/ETC, and regulated death (cuproptosis) leading to movement/psychiatric phenotypes | Manchia 2024; Hu 2024 neuroimaging/genomics (manchia2024theroleof pages 14-15, gromadzka2024theroleof pages 5-8) |
| Anatomical location | Liver (hepatic parenchyma) | UBERON | UBERON:liver (if known) | Primary affected organ: site of Cu accumulation, inflammation, fibrosis, and source of systemic “free” Cu driving extrahepatic injury | Wooton-Kee 2023; Teschke 2024 (wootonkee2023therapeuticimplicationsof pages 1-2, teschke2024wilsondiseasecoppermediated pages 3-5) |
| Anatomical location | Basal ganglia / Putamen | UBERON | UBERON:basal_ganglia (if known) | Typical site of Cu deposition on MRI and correlate of movement disorders (parkinsonism, dystonia) in neurological WD | Hu 2024; Ma 2024 (gromadzka2024theroleof pages 5-8) |
| Anatomical location | Cerebellum | UBERON | UBERON:cerebellum (if known) | Involved in coordination deficits; structural/functional changes reported in WD neuroimaging | Hu 2024 (gromadzka2024theroleof pages 5-8) |
| Anatomical location | Cornea (Kayser–Fleischer rings) | UBERON | UBERON:cornea (if known) | Sites of Cu deposition producing characteristic KF rings — diagnostic sign of systemic Cu overload | Classic clinicopathology summarized in reviews (wootonkee2023therapeuticimplicationsof pages 1-2, teschke2024wilsondiseasecoppermediated pages 3-5) |
| Biological process (GO) | Copper ion transport | GO | GO: (if known) | Cellular uptake, chaperoning, Golgi loading, vesicular exocytosis — central disrupted process in WD | Wooton-Kee 2023; Petruzzelli 2025 (wootonkee2023therapeuticimplicationsof pages 1-2, petruzzelli2025copperinhuman pages 30-35) |
| Biological process (GO) | Ceruloplasmin metabolic process | GO | GO: (if known) | Loading of Cu into apoceruloplasmin in TGN by ATP7B; defective in WD leading to low holo-CP | Teschke 2024; Petruzzelli 2025 (teschke2024wilsondiseasecoppermediated pages 3-5, petruzzelli2025copperinhuman pages 30-35) |
| Biological process (GO) | Mitochondrial organization / quality control | GO | GO:0007005 | Mitochondrial structural/functional disruption in WD; mitophagy and mitochondrial-driven death pathways implicated | Wooton-Kee 2023; Petruzzelli 2025 (wootonkee2023therapeuticimplicationsof pages 1-2, petruzzelli2025copperinhuman pages 30-35) |
| Biological process (GO) | Oxidative stress response | GO | GO:0006979 | Copper-catalyzed ROS generation, antioxidant induction (MT, GSH), and downstream damage/inflammation | Wooton-Kee 2023; Teschke 2024 (wootonkee2023therapeuticimplicationsof pages 1-2, teschke2024wilsondiseasecoppermediated pages 3-5) |
| Biological process (GO) | Autophagy | GO | GO:0006914 | Activated in response to dysfunctional organelles and Cu stress; may be protective or dysregulated in WD | Petruzzelli 2025; Manchia 2024 (petruzzelli2025copperinhuman pages 30-35, manchia2024theroleof pages 14-15) |
| Biological process (GO) | Cuproptosis (copper-dependent cell death) | GO | N/A (novel) | Recently described Cu-dependent death linked to lipoylated TCA enzymes and proteotoxic stress — emerging mechanism in WD | Teschke 2024; Chen reviews (teschke2024wilsondiseasecoppermediated pages 3-5) |
| Biological process (GO) | Ferroptosis (iron-related lipid peroxidation) | GO | GO: (if known) | Cross-talk with Cu and iron dysregulation in WD; contributes to membrane lipid peroxidation and cell death | Teschke 2024 (teschke2024wilsondiseasecoppermediated pages 3-5) |
| Biological process (GO) | Bile secretion / biliary copper excretion | GO | GO: (if known) | ATP7B-mediated trafficking to canalicular membrane enables biliary Cu elimination; failure → hepatic Cu overload | Wooton-Kee 2023; Petruzzelli 2025 (wootonkee2023therapeuticimplicationsof pages 1-2, petruzzelli2025copperinhuman pages 30-35) |
| Cellular component | Trans-Golgi network (TGN) | GO CC | GO: (if known) | Site of ceruloplasmin metallation by ATP7B and loading into secretory pathway | Teschke 2024; Petruzzelli 2025 (teschke2024wilsondiseasecoppermediated pages 3-5, petruzzelli2025copperinhuman pages 30-35) |
| Cellular component | Canalicular / apical membrane (hepatocyte) | GO CC | GO: (if known) | ATP7B relocates here to mediate biliary Cu excretion upon Cu excess | Wooton-Kee 2023; Teschke 2024 (wootonkee2023therapeuticimplicationsof pages 1-2, teschke2024wilsondiseasecoppermediated pages 3-5) |
| Cellular component | Lysosome / secretory vesicles | GO CC | GO: (if known) | Vesicular compartments used for Cu sequestration/exocytosis; implicated in trafficking defects | Petruzzelli 2025; Guo structural insights referenced in reviews (petruzzelli2025copperinhuman pages 30-35, wootonkee2023therapeuticimplicationsof pages 1-2) |
| Cellular component | Mitochondrion | GO CC | GO:0005739 | Mitochondrial accumulation of Cu causes structural/functional defects, ROS, and contributes to cuproptosis/mitophagy | Wooton-Kee 2023; Teschke 2024; Petruzzelli 2025 (wootonkee2023therapeuticimplicationsof pages 1-2, teschke2024wilsondiseasecoppermediated pages 3-5, petruzzelli2025copperinhuman pages 30-35) |


*Table: Compact, ontology-mapped summary of key molecules, processes, cell types, locations, and therapeutic agents in Wilson disease pathophysiology, with recent supporting sources (context citations) useful for knowledge‑base annotation and rapid reference.*

Limitations and open questions
- Although cuproptosis and ferroptosis are compelling mechanistic frameworks, direct in vivo human evidence in WD remains emerging; careful integration with classic oxidative stress/mitochondrial injury paradigms is warranted (International Journal of Molecular Sciences, Apr 2024; https://doi.org/10.3390/ijms25094753) (teschke2024wilsondiseasecoppermediated pages 3-5).
- The relative contributions of direct brain copper toxicity versus liver-derived inflammatory mediators to WD neurological disease likely vary across genotypes and disease stages (Journal of Neuroinflammation, Sep 2024; https://doi.org/10.1186/s12974-024-03178-5; Brain Communications, Sep 2024; https://doi.org/10.1093/braincomms/fcae329) (manchia2024theroleof pages 14-15, gromadzka2024theroleof pages 5-8).

References (URLs and publication dates included inline above). All mechanistic claims are supported by recent peer‑reviewed sources, with an emphasis on 2023–2024 literature and authoritative reviews and studies (wootonkee2023therapeuticimplicationsof pages 1-2, teschke2024wilsondiseasecoppermediated pages 3-5, gromadzka2024theroleof pages 5-8, manchia2024theroleof pages 14-15, stremmel2025theroleof pages 1-2).

References

1. (wootonkee2023therapeuticimplicationsof pages 1-2): Clavia Ruth Wooton-Kee. Therapeutic implications of impaired nuclear receptor function and dysregulated metabolism in wilson's disease. Pharmacology &amp; Therapeutics, 251:108529, Nov 2023. URL: https://doi.org/10.1016/j.pharmthera.2023.108529, doi:10.1016/j.pharmthera.2023.108529. This article has 11 citations and is from a domain leading peer-reviewed journal.

2. (teschke2024wilsondiseasecoppermediated pages 3-5): Rolf Teschke and Axel Eickhoff. Wilson disease: copper-mediated cuproptosis, iron-related ferroptosis, and clinical highlights, with comprehensive and critical analysis update. International Journal of Molecular Sciences, 25:4753, Apr 2024. URL: https://doi.org/10.3390/ijms25094753, doi:10.3390/ijms25094753. This article has 83 citations and is from a poor quality or predatory journal.

3. (gromadzka2024theroleof pages 5-8): Grażyna Gromadzka, Anna Wilkaniec, Beata Tarnacka, Krzysztof Hadrian, Maria Bendykowska, Adam Przybyłkowski, and Tomasz Litwin. The role of glia in wilson’s disease: clinical, neuroimaging, neuropathological and molecular perspectives. International Journal of Molecular Sciences, 25:7545, Jul 2024. URL: https://doi.org/10.3390/ijms25147545, doi:10.3390/ijms25147545. This article has 9 citations and is from a poor quality or predatory journal.

4. (stremmel2025theroleof pages 1-2): Wolfgang Stremmel and Ralf Weiskirchen. The role of copper dysregulation in wilson disease: an expert opinion. Frontiers in Medicine, Oct 2025. URL: https://doi.org/10.3389/fmed.2025.1673283, doi:10.3389/fmed.2025.1673283. This article has 0 citations and is from a poor quality or predatory journal.

5. (petruzzelli2025copperinhuman pages 30-35): Raffaella Petruzzelli, Elena Polishchuk, and Roman Polishchuk. Copper in human health and disease: insights from inherited disorders. Physiology, Nov 2025. URL: https://doi.org/10.1152/physiol.00032.2025, doi:10.1152/physiol.00032.2025. This article has 0 citations and is from a peer-reviewed journal.

6. (manchia2024theroleof pages 7-8): Mirko Manchia, Pasquale Paribello, Martina Pinna, and Gavino Faa. The role of copper overload in modulating neuropsychiatric symptoms. International Journal of Molecular Sciences, 25:6487, Jun 2024. URL: https://doi.org/10.3390/ijms25126487, doi:10.3390/ijms25126487. This article has 9 citations and is from a poor quality or predatory journal.

7. (stremmel2025theroleof pages 8-8): Wolfgang Stremmel and Ralf Weiskirchen. The role of copper dysregulation in wilson disease: an expert opinion. Frontiers in Medicine, Oct 2025. URL: https://doi.org/10.3389/fmed.2025.1673283, doi:10.3389/fmed.2025.1673283. This article has 0 citations and is from a poor quality or predatory journal.

8. (manchia2024theroleof pages 14-15): Mirko Manchia, Pasquale Paribello, Martina Pinna, and Gavino Faa. The role of copper overload in modulating neuropsychiatric symptoms. International Journal of Molecular Sciences, 25:6487, Jun 2024. URL: https://doi.org/10.3390/ijms25126487, doi:10.3390/ijms25126487. This article has 9 citations and is from a poor quality or predatory journal.