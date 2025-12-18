---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T23:28:17.863008'
end_time: '2025-12-17T23:36:48.246543'
duration_seconds: 510.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Fibromyalgia
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
- **Disease Name:** Fibromyalgia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Fibromyalgia**.
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
- **Disease Name:** Fibromyalgia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Fibromyalgia**.
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
- Disease Name: Fibromyalgia (FM)
- MONDO ID: (not definitively standardized across sources for FM; commonly referenced in ontologies as a complex, chronic pain syndrome)
- Category: Complex

Pathophysiology Description (Narrative)
Fibromyalgia is a prototypical nociplastic pain condition characterized by widespread pain, sensory amplification, fatigue, sleep and cognitive symptoms. Contemporary genetic and systems-biology evidence converge on a predominantly central nervous system (CNS) disorder with variable peripheral contributions from small-fiber pathology and immune-inflammation.

Large-scale genetics: A multi-ancestry GWAS meta-analysis across 2.56 million individuals (54,629 cases) identified 26 risk loci and reported that “heritability was exclusively enriched within brain tissues and neural cell types,” implicating neural genes (HTT, GPR52, DRD2/NCAM1, CAMKV, DCC, MDGA2, CELF4) and providing a biological framework that positions FM as a CNS disorder with strong genetic correlations to chronic pain and psychiatric comorbidities (rg > 0.7 with low back pain, PTSD and IBS) (MedRxiv, 2025-09-18; https://doi.org/10.1101/2025.09.18.25335914) (kerrebijn2025thegeneticarchitecture pages 1-2).

Central sensitization, neurotransmitter imbalance and neuroimmune interactions: Clinical and mechanistic reviews emphasize central sensitization driven by maladaptive neuroplasticity (excitatory/inhibitory imbalance involving glutamatergic and GABAergic transmission), altered monoamine signaling (serotonin, norepinephrine, dopamine), and neuroinflammation that sustain pain amplification and multisensory hypersensitivity in FM (Medicina, 2024-02; https://doi.org/10.3390/medicina60020272) (sharie2024unravelingthecomplex pages 4-6). Complementary integrative reviews highlight reduced inhibitory neurotransmission (e.g., decreased insular GABA) and immune-neuroinflammatory signatures (e.g., peripheral cytokines; altered interferon-related proteomics) as recurring findings (Biomedicines, 2023-04; https://doi.org/10.3390/biomedicines11041119) (ovrom2023acomprehensivereview pages 23-25, ovrom2023acomprehensivereview pages 22-23).

Peripheral small-fiber involvement: Approximately half of patients demonstrate small-fiber pathology (SFP) with reduced intraepidermal nerve fiber density (IENFD) and functional C-fiber abnormalities, often in a non–length-dependent or proximal-predominant pattern. A meta-analytic summary indicates about 50% prevalence; one series reported IENFD reduction in 63% of FM patients versus 10% in MDD with pain and 18% in healthy controls. Small-fiber loss correlates with more severe FM and with central MRI changes, supporting a synergy between peripheral input and CNS amplification (Pain Reports, 2025-12; https://doi.org/10.1097/pr9.0000000000001220) (sommer2025smallfiberpathology pages 1-2).

Immune–cytokine and metabolic signatures: Multiple cohorts show elevated pro-inflammatory cytokines (e.g., TNF-α, IL-1β, IL-6) in skin or serum correlating with symptom burden, as well as increased IL-17A in some studies. Metabolomic differences include elevated endocannabinoids (anandamide), oleoylethanolamide and palmitoylethanolamide, suggesting altered neuromodulatory tone. Proteomics reveal interferon signatures in B-cells, consistent with immune activation (Biomedicines, 2023-04; https://doi.org/10.3390/biomedicines11041119) (ovrom2023acomprehensivereview pages 14-15). Narrative syntheses further link inflammatory signaling, HPA-axis perturbation and oxidative stress, and highlight experimental data connecting neutrophil-driven neuroinflammation and chronic pain behaviors (Biomedicines, 2025-02; https://doi.org/10.3390/biomedicines13020503) (sedda2025fibromyalgiadepressionand pages 7-8).

Gut–immune axis and causal inference: A multi-omics bidirectional Mendelian randomization preprint identified Ruminococcus gauvreauii as a risk taxon and Enterorhabdus, Parabacteroides, Butyricicoccus, and Prevotella 9 as protective. MR also implicated inflammatory proteins (protective: CXCL5, S100A12, LIFR, CCL8; risk: CD244, IL-12β), supporting a causal role of gut-immune signaling and immune-regulatory pathways in FM (MedRxiv, 2024-09-13; https://doi.org/10.1101/2024.09.13.24313599) (niu2024amultiomicsbidirectional pages 1-5, niu2024amultiomicsbidirectional pages 16-20).

Key Concepts and Definitions
- Nociplastic pain: pain arising from altered nociception without clear tissue or nerve damage, with central sensitization a core mechanism (sharie2024unravelingthecomplex pages 4-6).
- Central sensitization: maladaptive neuroplasticity with increased excitability of central nociceptive circuits and impaired descending inhibition; linked to neurotransmitter imbalance (glutamate/GABA; monoamines) and neuroimmune activation (sharie2024unravelingthecomplex pages 4-6, ovrom2023acomprehensivereview pages 23-25).
- Small-fiber pathology (SFP): structural and functional abnormalities of thinly myelinated Aδ and unmyelinated C-fibers; in FM often proximal-predominant and present in ~50%, contributing to ongoing peripheral input (sommer2025smallfiberpathology pages 1-2).
- Immune-inflammation signature: elevated pro-inflammatory cytokines (e.g., TNF-α, IL-1β, IL-6; sometimes IL-17A), chemokines, and interferon-related proteomics alongside altered lipid mediators (endocannabinoids) (ovrom2023acomprehensivereview pages 14-15).

Recent Developments (2023–2024 priority)
- Genetics: CNS-enriched heritability and neural gene prioritization from a multi-ancestry GWAS (2025; methodologically central to current understanding) (kerrebijn2025thegeneticarchitecture pages 1-2).
- Gut–immune causal links: MR evidence for specific taxa and cytokine/chemokine proteins affecting FM risk (MedRxiv, 2024-09-13) (niu2024amultiomicsbidirectional pages 1-5, niu2024amultiomicsbidirectional pages 16-20).
- Small-fiber pathology consolidation: Meta-analytic and multimodal evidence reaffirm ~50% prevalence with generalization beyond length-dependent patterns; correlation with FM severity and central changes (Pain Reports, 2025-12) (sommer2025smallfiberpathology pages 1-2).
- Integrative immune-neurobiology: Reviews emphasize convergent inflammatory and neuroimmune processes (Biomedicines, 2023-04; 2025-02) (ovrom2023acomprehensivereview pages 23-25, sedda2025fibromyalgiadepressionand pages 7-8).

Current Applications and Real-World Implementations
- Diagnostic adjuncts: In suspected SFP, objective measures (IENFD via skin biopsy; corneal confocal microscopy) can document small-fiber loss and support phenotype stratification; recognition that SFP and proximal denervation are common in FM can refine clinical workups and management expectations (sommer2025smallfiberpathology pages 1-2).
- Biologically informed management: The CNS-centric architecture (genetics, central sensitization) supports prioritizing centrally acting analgesics and nonpharmacologic neuroplasticity-targeted interventions; immune-metabolic and gut–brain findings motivate lifestyle, anti-inflammatory, and microbiome-modulating strategies in comprehensive care (kerrebijn2025thegeneticarchitecture pages 1-2, ovrom2023acomprehensivereview pages 14-15, niu2024amultiomicsbidirectional pages 1-5, niu2024amultiomicsbidirectional pages 16-20).

Expert Opinions and Authoritative Analyses
- “Heritability [was] exclusively enriched within brain tissues and neural cell types,” defining FM as a CNS disorder and framing extensive comorbidities via shared genetic liabilities (MedRxiv GWAS, 2025) (kerrebijn2025thegeneticarchitecture pages 1-2).
- Narrative and integrative reviews converge on central sensitization with neurotransmitter dysregulation and neuroimmune activation as key sustaining mechanisms, while acknowledging heterogeneity and peripheral contributions (Medicina, 2024; Biomedicines, 2023, 2025) (sharie2024unravelingthecomplex pages 4-6, ovrom2023acomprehensivereview pages 23-25, sedda2025fibromyalgiadepressionand pages 7-8).

Relevant Statistics and Data from Recent Studies
- GWAS meta-analysis: N = 2,563,755 (54,629 cases; 2,509,126 controls); 26 loci; rg > 0.7 with low back pain, PTSD, IBS; strongest locus at HTT; neural gene prioritization; CNS heritability enrichment (MedRxiv, 2025) (kerrebijn2025thegeneticarchitecture pages 1-2).
- Small-fiber pathology prevalence: ~50% of FM patients with reduced IENFD; in one dataset, 63% of FM vs 10% MDD with pain vs 18% controls; generalized small-fiber loss and proximal predominance reported; functional C-fiber abnormalities on microneurography (Pain Reports, 2025) (sommer2025smallfiberpathology pages 1-2).
- Cytokine and proteomic signatures: Upregulated TNF-α, IL-1β, IL-6, sometimes IL-17A with symptom correlations; interferon signatures in B-cells; endocannabinoid and lipid mediator elevations (Biomedicines, 2023) (ovrom2023acomprehensivereview pages 14-15).
- Gut–immune MR: Risk taxon Ruminococcus gauvreauii; protective taxa Enterorhabdus, Parabacteroides, Butyricicoccus, Prevotella 9; protective proteins (CXCL5, S100A12, LIFR, CCL8) and risk proteins (CD244, IL-12β) (MedRxiv, 2024) (niu2024amultiomicsbidirectional pages 1-5, niu2024amultiomicsbidirectional pages 16-20).

Required Information
1) Core Pathophysiology
- Primary mechanisms: Central sensitization with excitatory–inhibitory imbalance (glutamate/GABA), altered monoamine signaling (serotonin/norepinephrine/dopamine), neuroimmune activation; variable peripheral small-fiber pathology augmenting nociceptive input (sharie2024unravelingthecomplex pages 4-6, ovrom2023acomprehensivereview pages 23-25, sommer2025smallfiberpathology pages 1-2).
- Dysregulated molecular pathways: Neural plasticity and synaptic signaling (HTT, GPR52, DRD2/NCAM1, CAMKV, DCC, MDGA2, CELF4); cytokine/chemokine signaling (IL-6, IL-1β, TNF-α, IL-17A); endocannabinoid and lipid mediator metabolism; interferon-related B-cell programs (kerrebijn2025thegeneticarchitecture pages 1-2, ovrom2023acomprehensivereview pages 14-15).
- Affected cellular processes: Synaptic potentiation and disinhibition; microglia/immune-mediated neuroinflammatory signaling; peripheral nociceptor sensitization; stress-response and metabolic signaling changes (sharie2024unravelingthecomplex pages 4-6, ovrom2023acomprehensivereview pages 23-25, ovrom2023acomprehensivereview pages 14-15, sommer2025smallfiberpathology pages 1-2).

2) Key Molecular Players
- Genes/Proteins (HGNC examples): HTT, GPR52, DRD2, NCAM1, DCC, CAMKV, MDGA2, CELF4 from GWAS prioritization (kerrebijn2025thegeneticarchitecture pages 1-2). Cytokines: IL6, IL1B, TNF, IL17A (ovrom2023acomprehensivereview pages 14-15). Chemokines: CCL8 (MCP-2), CXCL5, etc. (niu2024amultiomicsbidirectional pages 1-5, niu2024amultiomicsbidirectional pages 16-20).
- Chemical entities (CHEBI): Anandamide (CHEBI:28148), oleoylethanolamide (CHEBI:71464), palmitoylethanolamide (CHEBI:8063) elevated in plasma (ovrom2023acomprehensivereview pages 14-15).
- Cell types (CL): Microglia (CL:0000129); peripheral sensory neurons including C-fiber nociceptors (CL:0000099) (sommer2025smallfiberpathology pages 1-2, ovrom2023acomprehensivereview pages 23-25, ovrom2023acomprehensivereview pages 14-15).
- Anatomical locations (UBERON): Brain (UBERON:0000955), Skin (UBERON:0002097) with reduced IENFD; proximal patterning reported in FM (kerrebijn2025thegeneticarchitecture pages 1-2, sommer2025smallfiberpathology pages 1-2).

3) Biological Processes (GO annotation)
- CNS synaptic signaling and plasticity; glutamatergic signaling; GABAergic inhibitory transmission; dopaminergic modulation (GO: synaptic signaling) (sharie2024unravelingthecomplex pages 4-6, kerrebijn2025thegeneticarchitecture pages 1-2).
- Inflammatory response/chemokine-mediated signaling; Th17-related cytokine signaling (IL-17A) (ovrom2023acomprehensivereview pages 14-15, niu2024amultiomicsbidirectional pages 1-5).
- Nociception and peripheral nerve degeneration/regeneration processes in small-fiber pathology (sommer2025smallfiberpathology pages 1-2).
- Immune-regulatory processes suggested by MR-proteins (e.g., CXCL5, LIFR) (niu2024amultiomicsbidirectional pages 1-5, niu2024amultiomicsbidirectional pages 16-20).

4) Cellular Components
- Synapses and postsynaptic densities (central circuits); inhibitory interneuron networks and descending modulatory pathways (sharie2024unravelingthecomplex pages 4-6, kerrebijn2025thegeneticarchitecture pages 1-2).
- Peripheral nerve terminals in epidermis (IENFD) and cornea (CCM) (sommer2025smallfiberpathology pages 1-2).
- Microglial and immune cell compartments contributing to neuroinflammation (ovrom2023acomprehensivereview pages 23-25, sedda2025fibromyalgiadepressionand pages 7-8).

5) Disease Progression
- Putative sequence: Predisposing CNS-centric genetic architecture (neural gene risk; CNS enrichment) → triggers (stress, infections, injury) → central sensitization with E/I imbalance and impaired descending inhibition → neuroimmune activation (cytokines/chemokines) and variable peripheral SFP sustaining nociceptive input → symptom chronification with multisystem involvement (sleep, mood, cognition, autonomic features) (kerrebijn2025thegeneticarchitecture pages 1-2, sharie2024unravelingthecomplex pages 4-6, ovrom2023acomprehensivereview pages 14-15, sommer2025smallfiberpathology pages 1-2).
- Phases: Initiation (trigger/exacerbation), amplification (central sensitization with peripheral inputs), stabilization/chronification (network-level plasticity and immune-metabolic adaptation) (sharie2024unravelingthecomplex pages 4-6, ovrom2023acomprehensivereview pages 23-25, sommer2025smallfiberpathology pages 1-2).

6) Phenotypic Manifestations
- Clinical phenotypes: Widespread pain and hyperalgesia/allodynia; fatigue; non-restorative sleep; cognitive/affective symptoms (nociplastic pattern) (sharie2024unravelingthecomplex pages 4-6).
- Mechanistic links: Central sensitization explains sensory amplification; SFP explains neuropathic descriptors and autonomic features; cytokine/immune dysregulation links to sickness behaviors, fatigue, mood alterations; monoaminergic and endocannabinoid changes connect to pain modulation and affect (sommer2025smallfiberpathology pages 1-2, ovrom2023acomprehensivereview pages 14-15, sharie2024unravelingthecomplex pages 4-6).

Gene/Protein Annotations with Ontology Terms, Phenotypes, Cells, Anatomy, Chemicals, Evidence
| Entity Type | Name (with ontology ID) | Role / Annotation (GO/HP/CL/UBERON/CHEBI terms as applicable) | Mechanistic Notes | Evidence |
|---|---|---|---|---|
| Gene / Protein | HTT (HGNC:HTT) | GO: synaptic signaling; CNS development | Coding variant identified as strongest GWAS signal; implicates neural circuitry and CNS contribution to FM risk. | (kerrebijn2025thegeneticarchitecture pages 1-2) |
| Gene / Protein | GPR52 (HGNC:GPR52) | GO: G-protein coupled receptor activity; neuronal signaling | GWAS-prioritized regulator of HTT; suggests GPCR-mediated modulation of neural excitability in FM. | (kerrebijn2025thegeneticarchitecture pages 1-2) |
| Gene / Protein | DRD2 (HGNC:DRD2) / NCAM1 (HGNC:NCAM1) | GO: dopamine signaling; synaptic adhesion | Genetic prioritization implicates dopaminergic and cell-adhesion pathways linked to pain modulation and affective symptoms. | (kerrebijn2025thegeneticarchitecture pages 1-2) |
| Gene / Protein | DCC (HGNC:DCC) | GO: axon guidance; neural development | Risk locus with neural role, consistent with altered CNS connectivity and nociceptive processing. | (kerrebijn2025thegeneticarchitecture pages 1-2) |
| Gene / Protein | CAMKV (HGNC:CAMKV) | GO: synaptic plasticity; calcium/calmodulin-dependent processes | Implicates synaptic plasticity mechanisms (central sensitization) in FM pathophysiology. | (kerrebijn2025thegeneticarchitecture pages 1-2) |
| Gene / Protein | MDGA2 (HGNC:MDGA2) | GO: neuronal migration; synapse organization | Neural development/synapse gene prioritized by GWAS, supporting CNS-centric disease architecture. | (kerrebijn2025thegeneticarchitecture pages 1-2) |
| Gene / Protein | CELF4 (HGNC:CELF4) | GO: RNA binding; regulation of neuronal excitability | Neuronally expressed RNA-binding protein implicated by genetics; may affect expression of excitability-related transcripts. | (kerrebijn2025thegeneticarchitecture pages 1-2) |
| Cytokine / Immune | IL6 (Interleukin-6) | GO: inflammatory response; HP: increased circulating IL-6 | Frequently reported elevated in FM cohorts; correlates with pain severity and disability in multiple studies. | (ovrom2023acomprehensivereview pages 14-15) |
| Cytokine / Immune | CXCL8 / IL8 (CHEBI:IL8) | GO: chemokine-mediated signaling; neutrophil chemotaxis | Part of peripheral cytokine signature distinguishing FM from controls; associated with pain and tissue fat infiltration indices. | (ovrom2023acomprehensivereview pages 14-15) |
| Cytokine / Immune | TNF / TNF-alpha | GO: pro-inflammatory cytokine activity | Elevated in some FM cohorts; implicated in systemic low-grade inflammation that may amplify central sensitization. | (ovrom2023acomprehensivereview pages 14-15) |
| Cytokine / Immune | IL17A (Interleukin-17A) | GO: cytokine-mediated signaling pathway; Th17 responses | Reported increased in skin/serum in FM; links to immune-driven peripheral sensitization and comorbid autoimmune signals. | (ovrom2023acomprehensivereview pages 14-15) |
| Cell type | Nociceptor C-fibers (CL:0000099) | CL: peripheral sensory neuron; GO: nociception | Structural/functional small-fibre pathology (reduced IENFD, altered microneurography) present in ~50% of FM cohorts, contributing peripheral nociceptive input. | (sommer2025smallfiberpathology pages 1-2) |
| Cell type | Microglia (CL:0000129) | CL: microglial cell; GO: neuroinflammatory response | Microglial activation / neuroinflammation proposed to sustain central sensitization and pain amplification in FM. | (ovrom2023acomprehensivereview pages 14-15) |
| Anatomical location | Skin (UBERON:0002097) | UBERON: skin; GO: peripheral nerve innervation | Reduced intraepidermal nerve fibre density (IENFD) and proximal patterning reported in ~50% of FM patients; supports peripheral contribution to symptoms. | (sommer2025smallfiberpathology pages 1-2) |
| Anatomical location | Brain (UBERON:0000955) | UBERON: brain; GO: central nervous system development | GWAS tissue-enrichment and imaging implicate brain tissues and neural cell types as primary sites of genetic risk and altered function in FM. | (kerrebijn2025thegeneticarchitecture pages 1-2) |
| Chemical / Metabolite | Anandamide (CHEBI:28148) | CHEBI: endocannabinoid; GO: modulation of synaptic transmission | Elevated endocannabinoid (anandamide) and related lipids reported in plasma metabolomics, suggesting altered neuromodulatory tone in FM. | (ovrom2023acomprehensivereview pages 14-15) |


*Table: A compact, ontology-linked table summarizing genes, immune mediators, cell types, anatomical sites, and a key metabolite implicated in fibromyalgia pathophysiology, with concise mechanistic notes and primary evidence citations for knowledge-base use.*

Evidence Items (PMIDs/DOIs/URLs and dates)
- GWAS CNS enrichment and neural loci: Kerrebijn I et al. MedRxiv. 2025-09-18. https://doi.org/10.1101/2025.09.18.25335914 (kerrebijn2025thegeneticarchitecture pages 1-2)
- Central sensitization and neurotransmitter dysregulation: Sharie SA et al. Medicina. 2024-02. https://doi.org/10.3390/medicina60020272 (sharie2024unravelingthecomplex pages 4-6)
- Integrative genetic/epigenetic and immune-neurochemical evidence: Ovrom EA et al. Biomedicines. 2023-04. https://doi.org/10.3390/biomedicines11041119 (ovrom2023acomprehensivereview pages 23-25, ovrom2023acomprehensivereview pages 22-23, ovrom2023acomprehensivereview pages 14-15)
- Small-fiber pathology prevalence and characteristics: Sommer C, Üçeyler N. Pain Reports. 2025-12. https://doi.org/10.1097/pr9.0000000000001220 (sommer2025smallfiberpathology pages 1-2)
- Gut–immune MR links (taxa, cytokines/chemokines): Niu M et al. MedRxiv. 2024-09-13. https://doi.org/10.1101/2024.09.13.24313599 (niu2024amultiomicsbidirectional pages 1-5, niu2024amultiomicsbidirectional pages 16-20)
- Immune–neuroinflammation in FM, depression and autoimmune disorders: Sedda S et al. Biomedicines. 2025-02. https://doi.org/10.3390/biomedicines13020503 (sedda2025fibromyalgiadepressionand pages 7-8)

Notes and Limitations
- Some mechanistic domains remain under active investigation. For example, human neuroinflammation imaging (e.g., TSPO-PET) and specific biomarker panels (e.g., BDNF) are promising but require further replication and standardization; the present report prioritizes sources retrieved and directly evidenced in this synthesis (ovrom2023acomprehensivereview pages 23-25, sharie2024unravelingthecomplex pages 4-6, kerrebijn2025thegeneticarchitecture pages 1-2).


References

1. (kerrebijn2025thegeneticarchitecture pages 1-2): Isabel Kerrebijn, Gyda Bjornsdottir, Keon Arbabi, Lea Urpa, Hele Haapaniemi, Gudmar Thorleifsson, Lilja Stefansdottir, Stephan Frangakis, Jesse Valliere, Lovemore Kunorozva, Erik Abner, Caleb Ji, Bitten Aagaard, Henning Bliddal, Søren Brunak, Mie T Bruun, Maria Didriksen, Christian Erikstrup, Arni J Geirsson, Daniel F Gudbjartsson, Thomas F Hansen, Ingileif Jonsdottir, Stacey Knight, Kirk U Knowlton, Christina Mikkelsen, Lincoln D Nadauld, Thorunn A Olafsdottir, Sisse R Ostrowski, Ole BV Pedersen, Saedis Saevarsdottir, Astros T Skuladottir, Erik Sørensen, Hreinn Stefansson, Patrick Sulem, Olafur A Sveinsson, Gudny E Thorlacius, Unnur Thorsteinsdottir, Henrik Ullum, Arnor Vikingsson, Thomas M Werge, Richa Saxena, Kari Stefansson, Chad M Brummett, Bente Glintborg, Daniel J Clauw, Thorgeir E Thorgeirsson, Frances MK Williams, Nasa Sinnott-Armstrong, Hanna M Ollila, and Michael Wainberg. The genetic architecture of fibromyalgia across 2.5 million individuals. MedRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.09.18.25335914, doi:10.1101/2025.09.18.25335914. This article has 0 citations.

2. (sharie2024unravelingthecomplex pages 4-6): Sarah Al Sharie, Scott J. Varga, Lou’i Al-Husinat, Piercarlo Sarzi-Puttini, Mohammad Araydah, Batool Riyad Bal’awi, and Giustino Varrassi. Unraveling the complex web of fibromyalgia: a narrative review. Medicina, 60:272, Feb 2024. URL: https://doi.org/10.3390/medicina60020272, doi:10.3390/medicina60020272. This article has 48 citations and is from a poor quality or predatory journal.

3. (ovrom2023acomprehensivereview pages 23-25): Erik A. Ovrom, Karson A. Mostert, Shivani Khakhkhar, Daniel P. McKee, Padao Yang, and Yeng F. Her. A comprehensive review of the genetic and epigenetic contributions to the development of fibromyalgia. Biomedicines, 11:1119, Apr 2023. URL: https://doi.org/10.3390/biomedicines11041119, doi:10.3390/biomedicines11041119. This article has 39 citations and is from a poor quality or predatory journal.

4. (ovrom2023acomprehensivereview pages 22-23): Erik A. Ovrom, Karson A. Mostert, Shivani Khakhkhar, Daniel P. McKee, Padao Yang, and Yeng F. Her. A comprehensive review of the genetic and epigenetic contributions to the development of fibromyalgia. Biomedicines, 11:1119, Apr 2023. URL: https://doi.org/10.3390/biomedicines11041119, doi:10.3390/biomedicines11041119. This article has 39 citations and is from a poor quality or predatory journal.

5. (sommer2025smallfiberpathology pages 1-2): Claudia Sommer and Nurcan Üçeyler. Small fiber pathology in fibromyalgia syndrome. Pain Reports, 10:e1220, Dec 2025. URL: https://doi.org/10.1097/pr9.0000000000001220, doi:10.1097/pr9.0000000000001220. This article has 13 citations and is from a peer-reviewed journal.

6. (ovrom2023acomprehensivereview pages 14-15): Erik A. Ovrom, Karson A. Mostert, Shivani Khakhkhar, Daniel P. McKee, Padao Yang, and Yeng F. Her. A comprehensive review of the genetic and epigenetic contributions to the development of fibromyalgia. Biomedicines, 11:1119, Apr 2023. URL: https://doi.org/10.3390/biomedicines11041119, doi:10.3390/biomedicines11041119. This article has 39 citations and is from a poor quality or predatory journal.

7. (sedda2025fibromyalgiadepressionand pages 7-8): Stefania Sedda, Maria Piera L. Cadoni, Serenella Medici, Elena Aiello, Gian Luca Erre, Alessandra Matilde Nivoli, Ciriaco Carru, and Donatella Coradduzza. Fibromyalgia, depression, and autoimmune disorders: an interconnected web of inflammation. Biomedicines, 13:503, Feb 2025. URL: https://doi.org/10.3390/biomedicines13020503, doi:10.3390/biomedicines13020503. This article has 10 citations and is from a poor quality or predatory journal.

8. (niu2024amultiomicsbidirectional pages 1-5): Mengqi Niu, Jing Li, Victoria Sarafian, and Michael Maes. A multi-omics bidirectional mendelian randomization study and meta-analysis on the causal relationship between gut microbiota, inflammatory proteins, and fibromyalgia. MedRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.13.24313599, doi:10.1101/2024.09.13.24313599. This article has 2 citations.

9. (niu2024amultiomicsbidirectional pages 16-20): Mengqi Niu, Jing Li, Victoria Sarafian, and Michael Maes. A multi-omics bidirectional mendelian randomization study and meta-analysis on the causal relationship between gut microbiota, inflammatory proteins, and fibromyalgia. MedRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.13.24313599, doi:10.1101/2024.09.13.24313599. This article has 2 citations.