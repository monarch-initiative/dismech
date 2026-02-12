---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-01T12:46:39.401518'
end_time: '2026-02-01T12:53:11.362853'
duration_seconds: 391.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Frontotemporal Dementia
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Frontotemporal Dementia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Frontotemporal Dementia**.
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
- **Disease Name:** Frontotemporal Dementia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Frontotemporal Dementia**.
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
- Disease Name: Frontotemporal Dementia (FTD)
- MONDO ID: 
- Category: Complex

Pathophysiology description
Frontotemporal dementia (FTD) encompasses frontotemporal lobar degeneration (FTLD) driven by distinct proteinopathies and convergent cellular stress pathways. The principal pathological classes are FTLD–TDP (abnormal TDP-43), FTLD–tau (abnormal MAPT/tau), and less commonly FTLD–FUS (abnormal FUS/FET proteins). Across genetic and sporadic forms, early synaptic failure—particularly at the presynapse—emerges as a convergent mechanism, followed by progressive neuronal loss and network disintegration in frontal and temporal cortices (paralimbic fronto–insular–striatal circuits) (overview; proportions and convergence on presynaptic dysfunction) (https://doi.org/10.1093/brain/awae074, Mar 2024) (clayton2024synaptopathypresynapticconvergence pages 1-2). Molecularly, risk genes and causal mutations perturb proteostasis (aggregation, phase transitions), RNA metabolism (splicing/transport), autophagy–lysosomal homeostasis, nucleocytoplasmic transport, and innate immune signaling. These processes interact: genetic and proteostatic stressors (e.g., C9orf72 repeat expansions, GRN haploinsufficiency, TMEM106B variation) drive TDP-43 dysfunction and synaptic failure; MAPT mutations drive tau misfolding with axonal and synaptic compromise; and glial activation amplifies neurodegeneration (https://doi.org/10.1186/s40035-024-00429-6 is a tau-focused background review; mechanistic points here from cited sources below) (huber2024mechanismsofneurodegeneration pages 57-60, saloner2025largescalenetworkanalysis pages 1-7, hsiaonakamoto2024alterationsinlysosomal pages 1-5, huber2024mechanismsofneurodegenerationa pages 79-82).

Recent systems–level CSF proteomics across autosomal-dominant FTLD (C9orf72, GRN, MAPT) shows increased RNA-splicing modules (notably in C9orf72, GRN), increased extracellular matrix modules (MAPT), and decreased synaptic/neuronal and autophagy modules, aligning in vivo fluid signatures with core mechanisms and suggesting hub proteins as potential biomarkers/targets (https://doi.org/10.21203/rs.3.rs-4103685/v1, Mar 2025) (saloner2025largescalenetworkanalysis pages 1-7).

1) Core Pathophysiology
- Primary mechanisms
  - Proteinopathies: FTLD–TDP (~about half of cases), FTLD–tau (large fraction), FTLD–FUS (~minority) (synaptopathy review; mechanistic overview) (clayton2024synaptopathypresynapticconvergence pages 1-2, huber2024mechanismsofneurodegeneration pages 57-60).
  - Synaptic dysfunction: Early, convergent presynaptic deficits in vesicle priming, recycling, and local translation; TDP-43 loss-of-function reduces UNC13A and impairs priming, linking RNA-binding protein pathology to synaptic failure (https://doi.org/10.1093/brain/awae074, 2024; mechanistic synthesis) (clayton2024synaptopathypresynapticconvergence pages 1-2, huber2024mechanismsofneurodegeneration pages 57-60, huber2024mechanismsofneurodegenerationb pages 57-60).
  - Autophagy–lysosome dysfunction: GRN haploinsufficiency and TMEM106B risk alleles disrupt autophagosome–lysosome maturation, acidification and cargo clearance; in FTLD, autophagy modules are reduced in CSF network analyses (https://doi.org/10.1186/s12974-024-03039-1, Feb 2024; https://doi.org/10.21203/rs.3.rs-4103685/v1, Mar 2025) (sung2024progranulinhaploinsufficiencymediates pages 1-2, huber2024mechanismsofneurodegeneration pages 57-60, saloner2025largescalenetworkanalysis pages 1-7).
  - Nucleocytoplasmic transport impairment: Particularly in C9orf72 repeat expansion disease (loss-of-function and toxic gain-of-function via RNA foci and dipeptide repeat proteins) with downstream TDP-43 dyshomeostasis (https://doi.org/10.21203/rs.3.rs-4103685/v1, Mar 2025) (saloner2025largescalenetworkanalysis pages 1-7).
  - Neuroinflammation: Microglial and astrocytic activation; in GRN-related FTD, microglia show TDP-43 cytoplasmic aggregation with lysosomal abnormalities and complement C1q activation; glial biomarkers are elevated in biofluids (https://doi.org/10.1186/s12974-024-03039-1, Feb 2024; biofluid/tissue biomarker study) (sung2024progranulinhaploinsufficiencymediates pages 1-2, hsiaonakamoto2024alterationsinlysosomal pages 1-5, hsiaonakamoto2024alterationsinlysosomal pages 30-33).

- Dysregulated pathways
  - RNA splicing/processing, synaptic transmission, autophagy/lysosome, extracellular matrix remodeling; decreased synaptic and autophagy modules with increased RNA-splicing signatures in FTLD CSF proteomes (https://doi.org/10.21203/rs.3.rs-4103685/v1, Mar 2025) (saloner2025largescalenetworkanalysis pages 1-7).
  - TMEM106B–lysosome axis modulates TDP-43 dysfunction and C9orf72 DPR burden; UNC13A–synapse axis mediates TDP-43 loss-of-function at the presynapse (mechanistic consolidation) (huber2024mechanismsofneurodegeneration pages 57-60, huber2024mechanismsofneurodegenerationb pages 57-60, huber2024mechanismsofneurodegenerationa pages 57-60).

- Cellular processes affected
  - Presynaptic vesicle priming/recycling, local translation, long-range axonal transport; autophagosome–lysosome fusion and acidification; nucleocytoplasmic shuttling; complement-mediated synapse/glia crosstalk (clayton2024synaptopathypresynapticconvergence pages 1-2, huber2024mechanismsofneurodegeneration pages 57-60, sung2024progranulinhaploinsufficiencymediates pages 1-2, hsiaonakamoto2024alterationsinlysosomal pages 1-5).

2) Key Molecular Players
- Genes/Proteins (HGNC symbols)
  - GRN (progranulin): Haploinsufficiency causes lysosomal dysfunction and microglial activation; human microglia from GRN-FTD show cytoplasmic TDP-43 aggregation, lipid droplet accumulation, and profound lysosomal abnormalities with complement C1q activation (https://doi.org/10.1186/s12974-024-03039-1, Feb 2024) (sung2024progranulinhaploinsufficiencymediates pages 1-2).
  - C9orf72: Hexanucleotide repeat expansions cause combined loss-of-function and gain-of-function (RNA foci, dipeptide-repeat proteins) that impair RNA metabolism, nucleocytoplasmic transport, proteostasis and lead to TDP-43 aggregation (https://doi.org/10.21203/rs.3.rs-4103685/v1, Mar 2025) (saloner2025largescalenetworkanalysis pages 1-7).
  - MAPT (tau): Mutations drive tau aggregation, extracellular matrix and synaptic signaling alterations (CSF proteomics) and axonal/synaptic compromise in FTLD–tau (https://doi.org/10.21203/rs.3.rs-4103685/v1, Mar 2025) (saloner2025largescalenetworkanalysis pages 1-7).
  - TARDBP (TDP-43): Aggregation and nuclear loss-of-function disrupt RNA splicing/transport; presynaptic effects via UNC13A dysregulation (review evidence) (huber2024mechanismsofneurodegeneration pages 57-60, clayton2024synaptopathypresynapticconvergence pages 1-2).
  - FUS: Defines a minority FTLD–FUS class (overview) (clayton2024synaptopathypresynapticconvergence pages 1-2, huber2024mechanismsofneurodegeneration pages 57-60).
  - TMEM106B: Genetic modifier in FTLD–TDP; risk alleles/filament accumulation associate with endolysosomal defects, impaired RNA transport/local translation, and heightened TDP-43 dysfunction; knockdown increases DPR accumulation and disrupts autophagosome–lysosome maturation (mechanistic synthesis) (huber2024mechanismsofneurodegeneration pages 57-60, huber2024mechanismsofneurodegenerationb pages 57-60, huber2024mechanismsofneurodegenerationa pages 57-60).
  - UNC13A: Presynaptic vesicle priming factor; TDP-43–dependent cryptic exon inclusion and poly-PR decrease UNC13A, linking TDP-43 pathology to synaptic failure (huber2024mechanismsofneurodegeneration pages 57-60, huber2024mechanismsofneurodegenerationb pages 57-60).

- Chemical entities (CHEBI terms; selected)
  - Glucosylsphingosine (GlcSph), ganglioside GM2, globoside GB3: Lysosomal lipid biomarkers increased in brain regions affected by GRN and sporadic FTD; plasma GlcSph elevated in asymptomatic GRN carriers (https://doi.org/10.1101/2024.02.09.579529, Feb 2024) (hsiaonakamoto2024alterationsinlysosomal pages 1-5, hsiaonakamoto2024alterationsinlysosomal pages 30-33).
  - Neurofilament light (NfL): Axonal injury biomarker elevated across genetic and sporadic FTD; correlates with clinical severity and progression (https://doi.org/10.1101/2024.02.09.579529, Feb 2024) (hsiaonakamoto2024alterationsinlysosomal pages 1-5, huber2024mechanismsofneurodegenerationa pages 79-82).
  - GFAP (astroglial), YKL-40 (CHI3L1): Glial biomarkers elevated in asymptomatic GRN carriers and symptomatic FTD groups (pattern varies by genotype); tissue YKL-40 increased in affected regions (https://doi.org/10.1101/2024.02.09.579529, 2024) (hsiaonakamoto2024alterationsinlysosomal pages 1-5, hsiaonakamoto2024alterationsinlysosomal pages 30-33).
  - Synaptic proteins NPTX2, NPTXR (neuronal pentraxins), VGF: Reduced in CSF across FTD, most pronounced in MAPT carriers; some correlate with disease severity (https://doi.org/10.1101/2024.02.09.579529, 2024) (hsiaonakamoto2024alterationsinlysosomal pages 1-5, hsiaonakamoto2024alterationsinlysosomal pages 30-33).

- Cell Types (CL terms; selected)
  - Neurons (principal cortical pyramidal neurons): primary degenerating cells with early synaptic failure (clayton2024synaptopathypresynapticconvergence pages 1-2).
  - Microglia: show disease-associated activation; in GRN deficiency, cell-intrinsic TDP-43 aggregation and lysosomal defects with complement activation; glial biomarkers elevated (sung2024progranulinhaploinsufficiencymediates pages 1-2, hsiaonakamoto2024alterationsinlysosomal pages 1-5).
  - Astrocytes: reactive in FTLD; GFAP elevated in plasma/CSF; contribute to neuroinflammation and synaptic environment (hsiaonakamoto2024alterationsinlysosomal pages 1-5, hsiaonakamoto2024alterationsinlysosomal pages 30-33).
  - Oligodendrocytes: can harbor inclusions in FTLD–TDP subtypes (overview) (huber2024mechanismsofneurodegeneration pages 57-60).

- Anatomical locations (UBERON terms; selected)
  - Frontal and temporal cortices with prominent involvement of paralimbic fronto–insular–striatal (salience-related) networks; selective vulnerability of anterior temporal and insular regions underlies bvFTD and language variants (https://doi.org/10.15496/publikation-94419, May 2024) (reinermann2024thefunctionalconnectivity pages 14-17).

3) Biological Processes (for GO annotation; selected disrupted processes)
- Protein aggregation, phase separation and inclusion formation (TDP-43, tau, FUS) (huber2024mechanismsofneurodegeneration pages 57-60, clayton2024synaptopathypresynapticconvergence pages 1-2).
- RNA splicing/processing and RNA transport (TDP-43 loss-of-function; global RNA splicing module increases in CSF proteomics) (saloner2025largescalenetworkanalysis pages 1-7, huber2024mechanismsofneurodegeneration pages 57-60).
- Nucleocytoplasmic transport (impaired in C9orf72 expansion disease) (saloner2025largescalenetworkanalysis pages 1-7).
- Autophagy and lysosome organization/acidification; cargo trafficking (GRN/TMEM106B axis) (sung2024progranulinhaploinsufficiencymediates pages 1-2, huber2024mechanismsofneurodegeneration pages 57-60).
- Synaptic vesicle priming/exocytosis and presynaptic homeostasis (UNC13A, vesicle cycle) (clayton2024synaptopathypresynapticconvergence pages 1-2, huber2024mechanismsofneurodegeneration pages 57-60).
- Complement activation and innate immune signaling in glia (C1q, YKL-40 elevation; microglial activation) (sung2024progranulinhaploinsufficiencymediates pages 1-2, hsiaonakamoto2024alterationsinlysosomal pages 1-5, hsiaonakamoto2024alterationsinlysosomal pages 30-33).
- Extracellular matrix remodeling (MAPT-associated CSF modules) (saloner2025largescalenetworkanalysis pages 1-7).

4) Cellular Components (selected)
- Presynapse/synaptic vesicle pool; active zone (UNC13A-dependent priming) (clayton2024synaptopathypresynapticconvergence pages 1-2, huber2024mechanismsofneurodegeneration pages 57-60).
- Lysosomes, late endosomes, autophagosomes and autolysosomes (GRN/TMEM106B-dependent maturation and acidification) (sung2024progranulinhaploinsufficiencymediates pages 1-2, huber2024mechanismsofneurodegeneration pages 57-60).
- Stress granules and ribonucleoprotein assemblies (RNA-binding proteinopathies; overview) (huber2024mechanismsofneurodegeneration pages 57-60).
- Nucleus and cytoplasm (TDP-43 nucleocytoplasmic mislocalization) (huber2024mechanismsofneurodegeneration pages 57-60, saloner2025largescalenetworkanalysis pages 1-7).

5) Disease Progression
- Sequence of events (typical mechanistic cascade): genetic risk/trigger (e.g., C9orf72 expansion; GRN loss; MAPT mutation; TMEM106B risk) → proteinopathy (TDP-43/tau/FUS misfolding and mislocalization) → early presynaptic dysfunction (vesicle priming/turnover; local translation) → impaired autophagy–lysosome clearance and nucleocytoplasmic transport → reactive glial responses and complement signaling → progressive neuronal/synaptic loss and network disintegration in frontal/temporal systems, manifesting as bvFTD or PPA variants (synthesis from reviews and biomarker/proteomics data) (clayton2024synaptopathypresynapticconvergence pages 1-2, huber2024mechanismsofneurodegeneration pages 57-60, saloner2025largescalenetworkanalysis pages 1-7, hsiaonakamoto2024alterationsinlysosomal pages 1-5).
- Subtypes/stages: FTLD–TDP subtyping (A–D) and mixed pathologies occur; autosomal-dominant FTLD shows genotype-associated CSF module shifts (e.g., RNA splicing↑ in GRN/C9; ECM↑ in MAPT) and synaptic/autophagy module↓; these shifts mirror progression toward synaptic failure and lysosomal compromise (https://doi.org/10.21203/rs.3.rs-4103685/v1, 2025) (saloner2025largescalenetworkanalysis pages 1-7, hsiaonakamoto2024alterationsinlysosomal pages 1-5).

6) Phenotypic Manifestations
- Core clinical phenotypes: behavioral variant FTD (bvFTD: disinhibition, apathy, loss of empathy, compulsions), and primary progressive aphasia variants (semantic and non-fluent/agrammatic), reflecting selective degeneration of salience/semantic networks in frontal/anterior temporal systems (network-level account) (https://doi.org/10.15496/publikation-94419, 2024) (reinermann2024thefunctionalconnectivity pages 14-17).
- Clinicopathological links and mechanisms: presynaptic synaptopathy correlates with early cognitive/behavioral dysfunction; TDP-43 loss-of-function impacts synaptic genes (UNC13A), while GRN and TMEM106B lysosome biology contributes to neuroinflammation and clearance failure; in MAPT, synaptic/ECM alterations are prominent (synthesis) (clayton2024synaptopathypresynapticconvergence pages 1-2, huber2024mechanismsofneurodegeneration pages 57-60, saloner2025largescalenetworkanalysis pages 1-7, hsiaonakamoto2024alterationsinlysosomal pages 1-5).

Gene/protein annotations with ontology terms (examples)
- GRN (HGNC:4601): lysosomal protein; processes: lysosome organization, regulation of inflammatory response, autophagy; components: lysosome, late endosome; evidence: human microglia TDP-43 aggregation with lysosomal abnormalities, complement activation in GRN haploinsufficiency (https://doi.org/10.1186/s12974-024-03039-1, 2024) (sung2024progranulinhaploinsufficiencymediates pages 1-2).
- C9orf72 (HGNC:28339): GTPase regulator/trafficking; processes: nucleocytoplasmic transport, RNA metabolism, proteostasis; components: nucleus, cytoplasm, nuclear pore; evidence: combined loss- and gain-of-function with TDP-43 aggregation (https://doi.org/10.21203/rs.3.rs-4103685/v1, 2025) (saloner2025largescalenetworkanalysis pages 1-7).
- MAPT (HGNC:6893): microtubule-associated protein; processes: microtubule stabilization, synaptic signaling; components: axon, somatodendritic compartments; evidence: ECM↑ and synaptic signaling alterations in MAPT FTLD CSF networks (https://doi.org/10.21203/rs.3.rs-4103685/v1, 2025) (saloner2025largescalenetworkanalysis pages 1-7).
- TARDBP/TDP-43 (HGNC:11577): RNA-binding protein; processes: RNA splicing/transport; components: nucleus, cytoplasm; evidence: presynaptic synaptopathy via UNC13A dysregulation (review) (huber2024mechanismsofneurodegeneration pages 57-60, clayton2024synaptopathypresynapticconvergence pages 1-2).
- FUS (HGNC:4010): RNA-binding; processes: RNA metabolism, stress granules; components: nucleus, stress granules; evidence: minority FTLD–FUS class (overview) (huber2024mechanismsofneurodegeneration pages 57-60, clayton2024synaptopathypresynapticconvergence pages 1-2).
- TMEM106B (HGNC:24797): lysosomal membrane protein; processes: autophagosome–lysosome fusion, lysosomal acidification; components: lysosome, endolysosomal system; evidence: genetic modifier; DPR clearance; endolysosomal disruption (huber2024mechanismsofneurodegeneration pages 57-60, huber2024mechanismsofneurodegenerationb pages 57-60).
- UNC13A (HGNC:12535): presynaptic priming; processes: synaptic vesicle exocytosis; components: active zone; evidence: TDP-43–dependent vulnerability and synaptic dysfunction (huber2024mechanismsofneurodegeneration pages 57-60, huber2024mechanismsofneurodegenerationb pages 57-60).

Phenotype associations (examples; HP terms)
- Behavioral disinhibition, apathy, loss of empathy, compulsive behaviors, executive dysfunction; expressive language deficits (semantic variant, non-fluent variant) (network/clinical synthesis) (reinermann2024thefunctionalconnectivity pages 14-17).

Cell type involvement (examples; CL terms)
- Neuron (principal excitatory neuron), microglial cell, astrocyte, oligodendrocyte; endothelial/vascular involvement is under active study but not established by the evidence set cited here (clayton2024synaptopathypresynapticconvergence pages 1-2, sung2024progranulinhaploinsufficiencymediates pages 1-2, hsiaonakamoto2024alterationsinlysosomal pages 1-5).

Anatomical locations (UBERON terms)
- Frontal lobe, temporal lobe, insula, anterior temporal pole; paralimbic fronto–insular–striatal network elements (reinermann2024thefunctionalconnectivity pages 14-17).

Chemical entities (CHEBI terms)
- Glucosylsphingosine (GlcSph), ganglioside GM2, globoside GB3; NfL (protein biomarker), GFAP, YKL-40; neuronal pentraxins (NPTX2/NPTXR); VGF (hsiaonakamoto2024alterationsinlysosomal pages 1-5, hsiaonakamoto2024alterationsinlysosomal pages 30-33, huber2024mechanismsofneurodegenerationa pages 79-82).

Evidence items and key statistics
- Pathological classes and convergence: Most FTD belongs to FTLD–TDP or FTLD–tau; FTLD–FUS is less common. Early presynaptic dysfunction is a convergent, likely initiating mechanism across genetic backgrounds (https://doi.org/10.1093/brain/awae074, 2024) (clayton2024synaptopathypresynapticconvergence pages 1-2, huber2024mechanismsofneurodegeneration pages 57-60).
- TMEM106B modifies FTLD–TDP: risk alleles/filaments link to TDP-43 dysfunction and endolysosomal impairment; knockdown increases C9 DPRs and blocks autophagosome–lysosome maturation (mechanistic evidence compiled) (huber2024mechanismsofneurodegeneration pages 57-60, huber2024mechanismsofneurodegenerationb pages 57-60, huber2024mechanismsofneurodegenerationa pages 57-60).
- GRN haploinsufficiency: human microglia from GRN-FTD show cytoplasmic TDP-43 aggregation, lysosomal abnormalities, complement C1q activation, and impaired phagocytosis (https://doi.org/10.1186/s12974-024-03039-1, Feb 2024) (sung2024progranulinhaploinsufficiencymediates pages 1-2).
- CSF proteomics in genetic FTLD (n≈116 carriers vs 39 controls): RNA-splicing modules↑ (C9orf72, GRN), ECM modules↑ (MAPT), synaptic/neuronal and autophagy modules↓; signatures generalize to independent cohorts (https://doi.org/10.21203/rs.3.rs-4103685/v1, Mar 2025) (saloner2025largescalenetworkanalysis pages 1-7).
- Biofluid/tissue biomarkers across FTD: plasma/CSF NfL↑ across forms (severity correlation); plasma GFAP↑ and CSF YKL-40↑ (notably in GRN and MAPT); CSF NPTX2/NPTXR↓ and VGF↓ (synaptic loss), strongest in MAPT; lysosomal lipids (GlcSph, GM2, GB3)↑ in disease-affected cortex; some markers (e.g., NPTXR) correlate with CDR+NACC FTLD severity (https://doi.org/10.1101/2024.02.09.579529, Feb 2024) (hsiaonakamoto2024alterationsinlysosomal pages 1-5, hsiaonakamoto2024alterationsinlysosomal pages 30-33, hsiaonakamoto2024alterationsinlysosomal pages 33-38).

Applications and real‑world implementations
- Biomarker applications: NfL (plasma/CSF) as a prognostic and pharmacodynamic marker across FTLD; plasma GFAP and CSF YKL‑40 for glial activation; CSF neuronal pentraxins (NPTX2/NPTXR) for synaptic integrity; genotype‑specific lysosomal lipids (e.g., plasma GlcSph in GRN) for stratification and presymptomatic monitoring; AD biomarkers (Aβ42/40, p‑tau) to exclude AD copathology in differential diagnosis (https://doi.org/10.1101/2024.02.09.579529, 2024; biomarker review perspective) (hsiaonakamoto2024alterationsinlysosomal pages 1-5, huber2024mechanismsofneurodegenerationa pages 79-82).
- Therapeutic directions informed by mechanisms: Targeting lysosomal biology (GRN replacement/augmentation; TMEM106B modulation), nucleocytoplasmic transport (C9orf72 pathways), and synaptic resilience (UNC13A/synaptic vesicle cycle) are rational avenues suggested by convergent mechanisms and CSF network signatures (https://doi.org/10.21203/rs.3.rs-4103685/v1, 2025; mechanistic syntheses) (saloner2025largescalenetworkanalysis pages 1-7, huber2024mechanismsofneurodegeneration pages 57-60, clayton2024synaptopathypresynapticconvergence pages 1-2).

Expert opinions and analysis from authoritative sources
- A 2024 Brain review synthesizes convergent presynaptic synaptopathy across ALS–FTD, arguing it is an early and targetable hub across genetic backgrounds (https://doi.org/10.1093/brain/awae074, Mar 2024) (clayton2024synaptopathypresynapticconvergence pages 1-2).
- Mechanistic syntheses emphasize TMEM106B and UNC13A as central modulators linking lysosomal/autophagy and presynaptic machinery to TDP‑43 pathology, recommending pathway‑focused biomarker development (huber2024mechanismsofneurodegeneration pages 57-60, huber2024mechanismsofneurodegenerationb pages 57-60).
- Systems proteomics in genetic FTLD recommends network‑based biomarker panels and highlights RNA splicing, ECM, synaptic, and autophagy modules as translational anchors (https://doi.org/10.21203/rs.3.rs-4103685/v1, 2025) (saloner2025largescalenetworkanalysis pages 1-7).

Ontology‑ready annotations (examples)
- Genes/Proteins (HGNC): GRN; C9orf72; MAPT; TARDBP; FUS; TMEM106B; UNC13A (sung2024progranulinhaploinsufficiencymediates pages 1-2, saloner2025largescalenetworkanalysis pages 1-7, huber2024mechanismsofneurodegeneration pages 57-60).
- GO Biological Process: protein aggregation; RNA splicing; nucleocytoplasmic transport; autophagy; lysosome organization; synaptic vesicle exocytosis; microglial activation; complement activation (saloner2025largescalenetworkanalysis pages 1-7, huber2024mechanismsofneurodegeneration pages 57-60, sung2024progranulinhaploinsufficiencymediates pages 1-2, hsiaonakamoto2024alterationsinlysosomal pages 1-5).
- GO Cellular Component: presynapse; synaptic vesicle; lysosome; autophagosome; nucleus; cytoplasm (clayton2024synaptopathypresynapticconvergence pages 1-2, huber2024mechanismsofneurodegeneration pages 57-60, sung2024progranulinhaploinsufficiencymediates pages 1-2).
- Cell Types (CL): neuron; microglial cell; astrocyte; oligodendrocyte (clayton2024synaptopathypresynapticconvergence pages 1-2, sung2024progranulinhaploinsufficiencymediates pages 1-2, hsiaonakamoto2024alterationsinlysosomal pages 1-5, huber2024mechanismsofneurodegeneration pages 57-60).
- Anatomical (UBERON): frontal lobe; temporal lobe; insula; anterior temporal pole (reinermann2024thefunctionalconnectivity pages 14-17).
- Chemicals (CHEBI): glucosylsphingosine; ganglioside GM2; globoside GB3; neurofilament light; GFAP; YKL‑40; NPTX2; NPTXR; VGF (hsiaonakamoto2024alterationsinlysosomal pages 1-5, hsiaonakamoto2024alterationsinlysosomal pages 30-33, huber2024mechanismsofneurodegenerationa pages 79-82).

Notes on prevalence/incidence
- Epidemiology varies by study/region; mechanistic reviews emphasize FTD as a leading cause of young‑onset dementia with high heritability and frequent autosomal‑dominant forms (network/overview context) (huber2024mechanismsofneurodegenerationa pages 33-38, reinermann2024thefunctionalconnectivity pages 14-17). Because robust, region‑specific incidence statistics were not directly available in the evidence set cited here, summary rates are not included; readers should refer to contemporary epidemiologic consortia for region‑specific denominators.

Cited sources (URLs and publication dates embedded above; ID mapping for statements)
- Presynaptic convergence in ALS–FTD: Brain (Mar 2024): https://doi.org/10.1093/brain/awae074 (clayton2024synaptopathypresynapticconvergence pages 1-2).
- Mechanism-focused syntheses with TMEM106B/UNC13A, FTLD class overview: 2024 synaptic–mechanism review (huber2024mechanismsofneurodegeneration pages 57-60, huber2024mechanismsofneurodegenerationb pages 57-60, huber2024mechanismsofneurodegenerationa pages 57-60).
- GRN microglia TDP-43 aggregation and lysosomal abnormalities: J Neuroinflammation (Feb 2024): https://doi.org/10.1186/s12974-024-03039-1 (sung2024progranulinhaploinsufficiencymediates pages 1-2).
- Systems CSF proteomics in genetic FTLD: Research Square (Mar 2025): https://doi.org/10.21203/rs.3.rs-4103685/v1 (saloner2025largescalenetworkanalysis pages 1-7).
- Biofluid/tissue biomarkers across sporadic and genetic FTD (lysosomal lipids, glial and synaptic markers): bioRxiv (Feb 2024): https://doi.org/10.1101/2024.02.09.579529 (hsiaonakamoto2024alterationsinlysosomal pages 1-5, hsiaonakamoto2024alterationsinlysosomal pages 30-33, hsiaonakamoto2024alterationsinlysosomal pages 33-38).
- Network/anatomical locus emphasis: doctoral thesis (May 2024): https://doi.org/10.15496/publikation-94419 (reinermann2024thefunctionalconnectivity pages 14-17).

Direct quotes (selected)
- “iMGs from FTD–GRN patients with PGRN deficiency exhibited… cytoplasmic TDP-43 aggregation and… lysosomal abnormalities… mediated by complement C1q activation” (J Neuroinflammation, Feb 2024) (sung2024progranulinhaploinsufficiencymediates pages 1-2).
- “This evidence indicates that presynaptic synaptopathy is an early and convergent event in frontotemporal dementia and amyotrophic lateral sclerosis” (Brain, Mar 2024) (clayton2024synaptopathypresynapticconvergence pages 1-2).

Limitations and gaps
- Pathology-specific in vivo biomarkers (e.g., direct assays for TDP-43 or DPRs) remain under development; NfL and glial/synaptic markers offer staging and monitoring but are not pathology-specific. Future work should integrate network proteomics, genotype‑specific lipidomics, and synaptic panels to enhance differential diagnosis and target engagement (huber2024mechanismsofneurodegenerationa pages 79-82, saloner2025largescalenetworkanalysis pages 1-7, hsiaonakamoto2024alterationsinlysosomal pages 1-5).


References

1. (clayton2024synaptopathypresynapticconvergence pages 1-2): Emma L Clayton, Laura Huggon, Michael A Cousin, and Sarah Mizielinska. Synaptopathy: presynaptic convergence in frontotemporal dementia and amyotrophic lateral sclerosis. Brain, 147:2289-2307, Mar 2024. URL: https://doi.org/10.1093/brain/awae074, doi:10.1093/brain/awae074. This article has 19 citations and is from a highest quality peer-reviewed journal.

2. (huber2024mechanismsofneurodegeneration pages 57-60): N Huber. Mechanisms of neurodegeneration in frontotemporal dementia: focus on synaptic dysfunction. Unknown journal, 2024.

3. (saloner2025largescalenetworkanalysis pages 1-7): Rowan Saloner, Adam Staffaroni, Eric Dammer, Erik C.B. Johnson, Emily Paolillo, Amy Wise, Hilary Heuer, Leah Forsberg, Argentina Lario Lago, Julia Webb, Jacob Vogel, Alexander Santillo, Oskar Hansson, Joel Kramer, Bruce Miller, Jingyao Li, Joseph Loureiro, Rajeev Sivasankaran, Kathleen Worringer, Nicholas Seyfried, Jennifer Yokoyama, William Seeley, Salvatore Spina, Lea Grinberg, Lawren VandeVrede, Peter Ljubenkov, Ece Bayram, Andrea Bozoki, Danielle Brushaber, Ciaran Considine, Gregory Day, Bradford Dickerson, Kimiko Domoto-Reilly, Kelley Faber, Douglas Galasko, Daniel Geschwind, Nupur Ghoshal, Neill Graff-Radford, Chadwick Hales, Lawrence Honig, Ging-Yuek Hsiung, Edward Huey, John Kornak, Walter Kremers, Maria Lapid, Suzee Lee, Irene Litvan, Corey McMillan, Mario Mendez, Toji Miyagawa, Alexander Pantelyat, Belen Pascual, Henry Paulson, Leonard Petrucelli, Peter Pressman, Eliana Ramos, Katya Rascovsky, Erik Roberson, Rodolfo Savica, Allison Snyder, A. Campbell Sullivan, Carmela Tartaglia, Marijne Vandebergh, Bradley Boeve, Howie Rosen, Julio Rojas, Adam Boxer, and Kaitlin Casaletto. Large-scale network analysis of the cerebrospinal fluid proteome identifies molecular signatures of frontotemporal lobar degeneration. Research Square, Mar 2025. URL: https://doi.org/10.21203/rs.3.rs-4103685/v1, doi:10.21203/rs.3.rs-4103685/v1. This article has 19 citations.

4. (hsiaonakamoto2024alterationsinlysosomal pages 1-5): Jennifer Hsiao-Nakamoto, Chi-Lu Chiu, Lawren VandeVrede, Ritesh Ravi, Brittany Vandenberg, Jack De Groot, Buyankhishig Tsogtbaatar, Meng Fang, Paul Auger, Neal S. Gould, Filippo Marchioni, Casey A. Powers, Sonnet S. Davis, Jung H. Suh, Jamal Alkabsh, Hilary W. Heuer, Argentina Lario Lago, Kimberly Scearce-Levie, William W. Seeley, Bradley F. Boeve, Howard J. Rosen, Amy Berger, Richard Tsai, Gilbert Di Paolo, Adam L. Boxer, Akhil Bhalla, and Fen Huang. Alterations in lysosomal, glial and neurodegenerative biomarkers in patients with sporadic and genetic forms of frontotemporal dementia. bioRxiv, Feb 2024. URL: https://doi.org/10.1101/2024.02.09.579529, doi:10.1101/2024.02.09.579529. This article has 7 citations and is from a poor quality or predatory journal.

5. (huber2024mechanismsofneurodegenerationa pages 79-82): N Huber. Mechanisms of neurodegeneration in frontotemporal dementia: focus on synaptic dysfunction. Unknown journal, 2024.

6. (huber2024mechanismsofneurodegenerationb pages 57-60): N Huber. Mechanisms of neurodegeneration in frontotemporal dementia: focus on synaptic dysfunction. Unknown journal, 2024.

7. (sung2024progranulinhaploinsufficiencymediates pages 1-2): Wonjae Sung, Min-Young Noh, Minyeop Nahm, Yong Sung Kim, Chang-Seok Ki, Young-Eun Kim, Hee-Jin Kim, and Seung Hyun Kim. Progranulin haploinsufficiency mediates cytoplasmic tdp-43 aggregation with lysosomal abnormalities in human microglia. Journal of Neuroinflammation, Feb 2024. URL: https://doi.org/10.1186/s12974-024-03039-1, doi:10.1186/s12974-024-03039-1. This article has 20 citations and is from a peer-reviewed journal.

8. (hsiaonakamoto2024alterationsinlysosomal pages 30-33): Jennifer Hsiao-Nakamoto, Chi-Lu Chiu, Lawren VandeVrede, Ritesh Ravi, Brittany Vandenberg, Jack De Groot, Buyankhishig Tsogtbaatar, Meng Fang, Paul Auger, Neal S. Gould, Filippo Marchioni, Casey A. Powers, Sonnet S. Davis, Jung H. Suh, Jamal Alkabsh, Hilary W. Heuer, Argentina Lario Lago, Kimberly Scearce-Levie, William W. Seeley, Bradley F. Boeve, Howard J. Rosen, Amy Berger, Richard Tsai, Gilbert Di Paolo, Adam L. Boxer, Akhil Bhalla, and Fen Huang. Alterations in lysosomal, glial and neurodegenerative biomarkers in patients with sporadic and genetic forms of frontotemporal dementia. bioRxiv, Feb 2024. URL: https://doi.org/10.1101/2024.02.09.579529, doi:10.1101/2024.02.09.579529. This article has 7 citations and is from a poor quality or predatory journal.

9. (huber2024mechanismsofneurodegenerationa pages 57-60): N Huber. Mechanisms of neurodegeneration in frontotemporal dementia: focus on synaptic dysfunction. Unknown journal, 2024.

10. (reinermann2024thefunctionalconnectivity pages 14-17): Leonie Isabelle Reinermann. The functional connectivity of cortical degenerations that are relevant to apraxia in patients with genetic ftd. Unknown, May 2024. URL: https://doi.org/10.15496/publikation-94419, doi:10.15496/publikation-94419. This article has 0 citations.

11. (hsiaonakamoto2024alterationsinlysosomal pages 33-38): Jennifer Hsiao-Nakamoto, Chi-Lu Chiu, Lawren VandeVrede, Ritesh Ravi, Brittany Vandenberg, Jack De Groot, Buyankhishig Tsogtbaatar, Meng Fang, Paul Auger, Neal S. Gould, Filippo Marchioni, Casey A. Powers, Sonnet S. Davis, Jung H. Suh, Jamal Alkabsh, Hilary W. Heuer, Argentina Lario Lago, Kimberly Scearce-Levie, William W. Seeley, Bradley F. Boeve, Howard J. Rosen, Amy Berger, Richard Tsai, Gilbert Di Paolo, Adam L. Boxer, Akhil Bhalla, and Fen Huang. Alterations in lysosomal, glial and neurodegenerative biomarkers in patients with sporadic and genetic forms of frontotemporal dementia. bioRxiv, Feb 2024. URL: https://doi.org/10.1101/2024.02.09.579529, doi:10.1101/2024.02.09.579529. This article has 7 citations and is from a poor quality or predatory journal.

12. (huber2024mechanismsofneurodegenerationa pages 33-38): N Huber. Mechanisms of neurodegeneration in frontotemporal dementia: focus on synaptic dysfunction. Unknown journal, 2024.