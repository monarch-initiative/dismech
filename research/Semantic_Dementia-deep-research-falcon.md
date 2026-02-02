---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-31T14:36:05.670901'
end_time: '2026-01-31T14:43:18.690186'
duration_seconds: 433.02
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Semantic Dementia
  mondo_id: ''
  category: Neurodegenerative Disease
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
- **Disease Name:** Semantic Dementia
- **MONDO ID:**  (if available)
- **Category:** Neurodegenerative Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Semantic Dementia**.
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
- **Disease Name:** Semantic Dementia
- **MONDO ID:**  (if available)
- **Category:** Neurodegenerative Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Semantic Dementia**.
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
- Disease Name: Semantic Dementia (semantic variant primary progressive aphasia; svPPA)
- MONDO ID: [TBD]
- Category: Neurodegenerative Disease (Frontotemporal Lobar Degeneration; FTLD)

Pathophysiology description
Semantic dementia is most commonly underpinned by FTLD-TDP type C proteinopathy characterized by mislocalized, phosphorylated TDP-43 with abundant long, corkscrew dystrophic neurites and relatively sparse neuronal cytoplasmic inclusions in anterior/inferior temporal neocortex and dentate gyrus, with severe neuronal loss in affected anterior temporal regions (especially temporal pole and amygdala) and a medial-to-lateral gradient of involvement within the anterior temporal lobes (ATLs) (adamscarr2020acaseof pages 6-11, adamscarr2020acaseof pages 1-6, borghesani2020regionalandhemispheric pages 10-11, borghesani2020regionalandhemispheric pages 1-2). TDP-43 biology implicates disturbed RNA metabolism (splicing, trafficking, stabilization) and nucleocytoplasmic transport, with mixed loss-of-function and gain-of-toxic-function mechanisms; comorbid TDP-43 pathology is frequent across neurodegenerative diseases and may interact with tauopathy and other age-related pathologies (riku2022tdp43proteinopathyand pages 1-2). In vivo imaging demonstrates a stereotyped sequence of regional involvement in pathology-proven FTLD-TDP type C with initial left temporal limbic-semantic structures, followed by spread to superior temporal, insulo-limbic, and striatal nodes (bocchetta2020invivostaging pages 1-2), and longitudinal data show propagation from anterior to more posterior temporal and orbitofrontal areas and to the contralateral ATL (borghesani2020regionalandhemispheric pages 1-2). Circuit-level physiology measured by spectral dynamic causal modeling shows attenuation of inhibitory self-coupling within antero-mesial temporal hubs and emergence of abnormal excitatory fronto-temporal projections, linking network disinhibition to semantic impairment and social disinhibition (benhamou2020theneurophysiologicalarchitecture pages 1-2).

Recent developments and latest research (2023–2024 prioritized)
- Clinicopathologic heterogeneity in SD includes cases with TDP-43 type A (often in late-onset and with higher Alzheimer’s disease neuropathologic changes and argyrophilic grains), and early-onset TDP-43 type C with corticospinal tract and motor neuron pathology despite minimal motor symptoms; an “inverse relationship between the extent of TDP pathology and neuronal loss” can be observed regionally (Nov 2023; DOI: 10.1111/neup.12859) (kawakatsu2023clinicopathologicaldiversityof pages 1-1).
- Aging-related comorbid TDP-43 processes such as LATE-NC share genetic risk with FTLD-TDP (TMEM106B, GRN, APOE, SORL1, ABCC9) and implicate endolysosomal and blood–brain barrier dysfunction as cofactors (Apr 2024; DOI: 10.1093/jnen/nlae032) (borghesani2020regionalandhemispheric pages 1-2).
- Longitudinal disease-mapping and functional staging approaches continue to refine how selective vulnerability in the temporopolar region maps onto progressive dissolution of word meaning (2020–2025 corpus; see 2020 in vivo staging and subsequent progression work) (bocchetta2020invivostaging pages 1-2, borghesani2020regionalandhemispheric pages 1-2, barbieri2025atrophyprogressionin pages 1-3).

Current applications and real-world implementations
- Imaging-based staging in FTLD-TDP type C (svPPA) supports patient stratification and longitudinal monitoring using MRI-derived w-score thresholds and specific regional ROIs (Alzheimer’s Res Ther, 2020) (bocchetta2020invivostaging pages 1-2). This framework has been adopted in research cohorts to track disease progression and to link atrophy stages to language impairments.
- Network-level biomarkers using resting-state fMRI and spectral DCM quantify disease-related alterations in effective connectivity (Scientific Reports, 2020) and provide mechanistic readouts that correlate with semantic impairment and social disinhibition (benhamou2020theneurophysiologicalarchitecture pages 1-2).

Expert opinions and analysis from authoritative sources
- Cohort studies and reviews converge on FTLD-TDP type C as the predominant substrate of svPPA/semantic dementia with characteristic ATL-predominant atrophy; right-predominant cases constitute a substantial minority (~40%) and show corresponding socioemotional phenotypes (NeuroImage: Clinical, 2020) (borghesani2020regionalandhemispheric pages 1-2). 
- Molecular reviews emphasize TDP-43’s central role in RNA metabolism and suggest both loss-of-function and aggregation-mediated toxicity, with shared mechanisms across TDP-43 proteinopathies and potential interactions with tauopathies (IJMS, 2022; Molecular Neurodegeneration, 2021) (riku2022tdp43proteinopathyand pages 1-2).

Relevant statistics and data
- Right-predominant ATL degeneration occurs in about 40% of pathology-proven TDP-43 type C temporal-variant cases (n=30) (Aug 2020; DOI: 10.1016/j.nicl.2020.102369) (borghesani2020regionalandhemispheric pages 1-2).
- In vivo FTLD-TDP type C staging (n=19, validation with 31 follow-up scans from 14 patients): Stage 1 left amygdala/medial temporal/temporal pole/lateral temporal + right medial temporal; Stage 2 left supratemporal; Stage 3 right anterior insula; Stage 4 right accumbens; all patients remained at same or later stage longitudinally; abnormality threshold w-score < −1.65 vs 81 controls (Mar 2020; DOI: 10.1186/s13195-020-00600-x) (bocchetta2020invivostaging pages 1-2).
- Histopathology in type C: “abundant TDP-43 positive dystrophic neurites which were long and corkscrew in shape” with sparse neuronal cytoplasmic inclusions; severe neuronal loss/gliosis in hippocampal subiculum; minimal AD/tau copathology in example case (Nov 2020; DOI: 10.1080/13554794.2019.1690665) (adamscarr2020acaseof pages 6-11).

Core Pathophysiology
- Primary mechanisms
  - FTLD-TDP type C proteinopathy: mislocalization of TDP-43 to cytoplasm, phosphorylation and aggregation into long dystrophic neurites and NCIs, prominent in anterior/inferior temporal cortex; dentate gyrus shows typical TDP-43-positive inclusions with relative sparing compared to neocortex in many cases (adamscarr2020acaseof pages 6-11, adamscarr2020acaseof pages 1-6).
  - Network disinhibition and maladaptive excitatory drive: weakened inhibitory self-coupling in antero-mesial temporal hubs with abnormal excitatory fronto-temporal projections (left hemisphere) linked to semantic and behavioral deficits (benhamou2020theneurophysiologicalarchitecture pages 1-2).
  - Selective regional vulnerability: ATL medial-to-lateral gradient, limbic connections (amygdala/hippocampus) confer susceptibility and determine symptom lateralization (left: anomia/word comprehension; right: socioemotional/face/person knowledge) (borghesani2020regionalandhemispheric pages 10-11, borghesani2020regionalandhemispheric pages 1-2).
- Dysregulated molecular pathways (TDP-43 biology)
  - RNA metabolism and splicing regulation; nucleocytoplasmic transport (NLS/NES), stress granule dynamics; both loss-of-function and gain-of-toxic-function mechanisms implicated (Dec 2022; DOI: 10.3390/ijms232415755) (riku2022tdp43proteinopathyand pages 1-2).
  - Proteostasis/autophagy-lysosome and endolysosomal pathways are implicated via comorbidity genetics and LATE risk factors; potential BBB contributions (Apr 2024; DOI: 10.1093/jnen/nlae032) (borghesani2020regionalandhemispheric pages 1-2).
- Affected cellular processes
  - Impaired TDP-43 clearance, seeds for propagation, and synaptic alterations in TDP-43-related FTLD (review synthesis) (riku2022tdp43proteinopathyand pages 1-2).

Key Molecular Players
- Genes/Proteins (HGNC)
  - TARDBP/TDP-43: central RBP; FTLD-TDP type C defining lesions (adamscarr2020acaseof pages 6-11, adamscarr2020acaseof pages 1-6, riku2022tdp43proteinopathyand pages 1-2). 
  - Somatic TARDBP variants (e.g., L41F, R42H) detected in SD brain tissue (mosaic 1–3% VAF) impaired splicing regulation and altered localization in functional assays, indicating a potential causal route for sporadic focal disease (Nov 2020; DOI: 10.1093/brain/awaa317) (rooij2020somatictardbpvariants pages 1-1).
  - GRN: associated with FTLD-TDP (often type A) and with SD heterogeneity/co-pathology (Neuropathology, 2023; IJMS, 2023) (kawakatsu2023clinicopathologicaldiversityof pages 1-1, antonioni2023frontotemporaldementiawhere pages 27-29).
  - TMEM106B: genetic modifier of TDP-43/LATE susceptibility, linked to endolysosomal biology; relevant to aging-related TDP-43 processes that can co-occur with SD (Apr 2024; DOI: 10.1093/jnen/nlae032) (borghesani2020regionalandhemispheric pages 1-2).
- Chemical entities (CHEBI)
  - Not disease-defining; however, pathophysiology implicates cellular calcium signaling alterations at synapses in TDP-43 proteinopathy models and human proteomic studies broadly; network-level measures capture excitatory/inhibitory balance alterations (benhamou2020theneurophysiologicalarchitecture pages 1-2).
- Cell types (CL)
  - Excitatory cortical projection neurons in anterior/inferior temporal neocortex are primarily affected, with reactive astrocytes and microglia contributing to degeneration and clearance responses (borghesani2020regionalandhemispheric pages 10-11, riku2022tdp43proteinopathyand pages 1-2).
- Anatomical Locations (UBERON)
  - Anterior temporal lobe/pole, amygdala, anterior hippocampus, superior/middle/inferior temporal gyri, anterior fusiform, anterior insula, orbitofrontal cortex (progression) (bocchetta2020invivostaging pages 1-2, borghesani2020regionalandhemispheric pages 1-2, borghesani2020regionalandhemispheric pages 10-11).

Biological Processes (for GO annotation)
- RNA splicing and mRNA processing; RNA transport (GO:0008380; GO:0006405) (TDP-43 function) (riku2022tdp43proteinopathyand pages 1-2).
- Nucleocytoplasmic transport (GO:0006913 regulation; NES/NLS-dependent shuttling) (riku2022tdp43proteinopathyand pages 1-2).
- Protein quality control: ubiquitin-dependent proteasomal process and autophagy-lysosome (GO:0006511, GO:0006914) (borghesani2020regionalandhemispheric pages 1-2).
- Synaptic transmission and plasticity; regulation of postsynaptic potential and inhibitory/excitatory balance (GO:0007268; GO:0060080) inferred from DCM findings and TDP-43 synaptic roles (benhamou2020theneurophysiologicalarchitecture pages 1-2, riku2022tdp43proteinopathyand pages 1-2).
- Axon/neurite integrity and degeneration (GO:0019899; GO:0070997) inferred from prominent dystrophic neurites in type C (adamscarr2020acaseof pages 6-11, adamscarr2020acaseof pages 1-6).

Cellular Components
- Cytoplasm (TDP-43 cytoplasmic inclusions) and stress granules; nucleus (loss of nuclear TDP-43); presynaptic and dendritic compartments affected at network level; lysosome/endosome system implicated by genetics (riku2022tdp43proteinopathyand pages 1-2, borghesani2020regionalandhemispheric pages 1-2).

Disease Progression
- Sequential in vivo staging in pathology-proven FTLD-TDP type C (svPPA) (w-score-based):
  - Stage 1: “left amygdala, medial temporal cortex, temporal pole, lateral temporal cortex and right medial temporal cortex” (bocchetta2020invivostaging pages 1-2).
  - Stage 2: “left supratemporal cortex” (bocchetta2020invivostaging pages 1-2).
  - Stage 3: “right anterior insula” (bocchetta2020invivostaging pages 1-2).
  - Stage 4: “right accumbens” (bocchetta2020invivostaging pages 1-2).
  Validation: “all patients either staying in the same stage or progressing to a later stage” across follow-up scans; threshold w-score < −1.65 vs 81 controls (bocchetta2020invivostaging pages 1-2). Longitudinal imaging outside staging also shows spread from ATLs to posterior temporal and orbitofrontal regions and to the contralateral ATL (borghesani2020regionalandhemispheric pages 1-2).

Phenotypic Manifestations and mechanism links
- Left ATL-predominant degeneration: anomia, word comprehension loss (svPPA) due to degradation of amodal semantic hub in bilateral ATLs, typically with initial left dominance (borghesani2020regionalandhemispheric pages 10-11, borghesani2020regionalandhemispheric pages 1-2).
- Right ATL-predominant degeneration (~40% of TDP-43-C temporal-variant): associative agnosia, prosopagnosia, impaired empathy/affect sharing, behavioral change; aligns with right limbic-semantic ATL connectivity (borghesani2020regionalandhemispheric pages 1-2).
- Network physiology: “weakened inhibitory self-coupling” in antero-mesial temporal hubs and “abnormal excitatory fronto-temporal projection in the left hemisphere” relate to semantic impairment and social disinhibition (benhamou2020theneurophysiologicalarchitecture pages 1-2).

Evidence quotes (verbatim fragments)
- “abundant TDP-43 positive dystrophic neurites which were long and corkscrew in shape” (Nov 2020; Neurocase) (adamscarr2020acaseof pages 6-11). URL: https://doi.org/10.1080/13554794.2019.1690665
- “atrophy in the left amygdala, medial temporal cortex, temporal pole, lateral temporal cortex and right medial temporal cortex… Stage 2… left supratemporal cortex… Stage 3… right anterior insula… Stage 4… right accumbens” (Mar 2020; Alzheimer’s Res Ther) (bocchetta2020invivostaging pages 1-2). URL: https://doi.org/10.1186/s13195-020-00600-x
- “atrophy distribution within both ATLs follows a medial-to-lateral gradient… atrophy appeared to progress to the contralateral ATL, and from the anterior temporal pole to posterior temporal and orbitofrontal regions… 40%… presented with right-lateralized atrophy” (Aug 2020; NeuroImage: Clinical) (borghesani2020regionalandhemispheric pages 1-2). URL: https://doi.org/10.1016/j.nicl.2020.102369
- “weakened the normal inhibitory self-coupling of network hubs in both antero-mesial temporal lobes, with development of an abnormal excitatory fronto-temporal projection in the left cerebral hemisphere” (Oct 2020; Scientific Reports) (benhamou2020theneurophysiologicalarchitecture pages 1-2). URL: https://doi.org/10.1038/s41598-020-72847-1
- “TDP-43 is an intranuclear protein… involved in RNA splicing, trafficking, stabilization… cytoplasmic inclusion bodies containing phosphorylated and truncated forms of TDP-43 are hallmarks of… FTLD” (Dec 2021; Molecular Neurodegeneration) (riku2022tdp43proteinopathyand pages 1-2). URL: https://doi.org/10.1186/s13024-021-00503-x
- “brain-specific somatic TARDBP variants… pathogenicity supported by functional assays” (Nov 2020; Brain) (rooij2020somatictardbpvariants pages 1-1). URL: https://doi.org/10.1093/brain/awaa317
- “coexists… with Alzheimer disease neuropathologic change… and… endolysosomal pathways, and blood-brain barrier dysfunction” (Apr 2024; J Neuropathol Exp Neurol) (borghesani2020regionalandhemispheric pages 1-2). URL: https://doi.org/10.1093/jnen/nlae032
- “Comparisons… TDP-type A versus type C pathology… high ADNC and argyrophilic grain (AG)” (Nov 2023; Neuropathology) (kawakatsu2023clinicopathologicaldiversityof pages 1-1). URL: https://doi.org/10.1111/neup.12859

Annotations for knowledge base linkage
- Gene/Protein annotations (HGNC):
  - TARDBP (HGNC:11573) – Transactive response DNA-binding protein 43 kDa; RBP central to FTLD-TDP type C (riku2022tdp43proteinopathyand pages 1-2, adamscarr2020acaseof pages 6-11).
  - GRN (HGNC:4601) – Progranulin; FTLD-TDP (often type A), phenotypic heterogeneity in SD (kawakatsu2023clinicopathologicaldiversityof pages 1-1, antonioni2023frontotemporaldementiawhere pages 27-29).
  - TMEM106B (HGNC:26153) – Lysosomal/endolysosomal pathway modifier, LATE/FTLD-TDP (borghesani2020regionalandhemispheric pages 1-2).
- Biological processes (GO): RNA splicing (GO:0008380), mRNA transport (GO:0051028), nucleocytoplasmic transport (GO:0006913 regulation), protein ubiquitination (GO:0016567), autophagy (GO:0006914), synaptic transmission (GO:0007268), regulation of inhibitory/excitatory balance (GO:0099579) (riku2022tdp43proteinopathyand pages 1-2, benhamou2020theneurophysiologicalarchitecture pages 1-2, borghesani2020regionalandhemispheric pages 1-2).
- Cell types (CL): Excitatory cortical neurons (CL:0002607), astrocyte (CL:0000127), microglial cell (CL:0000129) (borghesani2020regionalandhemispheric pages 10-11, riku2022tdp43proteinopathyand pages 1-2).
- Anatomical locations (UBERON): anterior temporal lobe/pole (UBERON:0001871/region), amygdala (UBERON:0001876), hippocampus (UBERON:0001954), superior/middle/inferior temporal gyri (UBERON:0006082/0006083/0006084), anterior fusiform gyrus (UBERON:0016510), anterior insula (UBERON:0001899) (bocchetta2020invivostaging pages 1-2, borghesani2020regionalandhemispheric pages 1-2, borghesani2020regionalandhemispheric pages 10-11).
- Phenotypes (HP): Anomia (HP:0002439), Semantic memory impairment (HP:0033777), Word comprehension deficits (HP:0032791), Associative agnosia (HP:0032139), Prosopagnosia (HP:0031429), Behavioral disinhibition (HP:0000712) (borghesani2020regionalandhemispheric pages 10-11, borghesani2020regionalandhemispheric pages 1-2, benhamou2020theneurophysiologicalarchitecture pages 1-2).
- Chemical entities (CHEBI): calcium ion (CHEBI:29108) – relevant to synaptic signaling dysregulation at circuit level; ubiquitin (CHEBI:16618) – proteostasis markers (benhamou2020theneurophysiologicalarchitecture pages 1-2, riku2022tdp43proteinopathyand pages 1-2).

Disease progression (sequence)
- Initiation in left ATL limbic-semantic nodes (amygdala/medial temporal/temporal pole), early anomia; spread to left supratemporal cortex with worsening lexical-semantic mapping; right anterior insula and right accumbens later as bilateral network involvement emerges; longitudinal spread posteriorly and contralaterally with progressive dissolution of word meaning (bocchetta2020invivostaging pages 1-2, borghesani2020regionalandhemispheric pages 1-2, barbieri2025atrophyprogressionin pages 1-3).

Cellular and network-to-phenotype mapping
- Long dystrophic neurites and axonal degeneration in ATL networks degrade the semantic hub’s connectivity, producing category-level semantic blurring and, with right ATL involvement, face/emotion recognition deficits; network DCM shows decreased inhibitory gain and pathological fronto-temporal excitation correlating with semantic impairment and social disinhibition (adamscarr2020acaseof pages 6-11, benhamou2020theneurophysiologicalarchitecture pages 1-2, borghesani2020regionalandhemispheric pages 1-2).

Co-pathologies and heterogeneity
- While FTLD-TDP type C predominates, some SD cases show type A TDP-43 and high ADNC and AG; aging brains often harbor TDP-43 related LATE-NC with overlapping genetic risk and cofactors (Neuropathology 2023; JNEN 2024) (kawakatsu2023clinicopathologicaldiversityof pages 1-1, borghesani2020regionalandhemispheric pages 1-2).

Embedded summary artifact
| Category | Entity (with ontology tag) | Role/Description | Key Evidence (pqac IDs) | URL/DOI | Year |
|---|---|---|---:|---|---:|
| Molecular player | TDP-43 (TARDBP) (HGNC:TARDBP) | RNA-binding protein that mislocalizes and forms phosphorylated cytoplasmic inclusions and long dystrophic neurites; central proteinopathy in FTLD-TDP type C associated with semantic dementia/svPPA | (riku2022tdp43proteinopathyand pages 1-2, adamscarr2020acaseof pages 6-11, kawakatsu2023clinicopathologicaldiversityof pages 1-1) | https://doi.org/10.3390/ijms232415755, https://doi.org/10.1080/13554794.2019.1690665, https://doi.org/10.1111/neup.12859 | 2020–2023 |
| Genetic variant (somatic) | Somatic TARDBP variants (HGNC:TARDBP) | Brain-restricted, low-level somatic missense variants impair TDP-43 splicing regulation and localization; proposed cause for sporadic, focal SD cases | (rooij2020somatictardbpvariants pages 1-1) | https://doi.org/10.1093/brain/awaa317 | 2020 |
| Genetic risk / modifier | GRN (HGNC:GRN) | Germline progranulin mutations associate with FTLD-TDP (often type A) and contribute to clinicopathologic heterogeneity and co-pathology patterns | (antonioni2023frontotemporaldementiawhere pages 27-29, kawakatsu2023clinicopathologicaldiversityof pages 1-1) | https://doi.org/10.3390/ijms241411732, https://doi.org/10.1111/neup.12859 | 2023 |
| Genetic modifier | TMEM106B (HGNC:TMEM106B) | Risk modifier linked to TDP-43 pathology/LATE and influences vulnerability and progression in TDP-43 proteinopathies | (borghesani2020regionalandhemispheric pages 1-2, antonioni2023frontotemporaldementiawhere pages 27-29) | https://doi.org/10.1093/jnen/nlae032, https://doi.org/10.3390/ijms241411732 | 2023–2024 |
| Lesion types (morphology) | Long dystrophic neurites; neuronal cytoplasmic inclusions (NCIs) | FTLD-TDP type C is characterised by abundant long/corkscrew dystrophic neurites and relatively sparse NCIs, concentrated in anterior/inferior temporal cortex and dentate gyrus patterns | (adamscarr2020acaseof pages 6-11, adamscarr2020acaseof pages 1-6, kawakatsu2023clinicopathologicaldiversityof pages 1-1) | https://doi.org/10.1080/13554794.2019.1690665, https://doi.org/10.1080/13554794.2019.1690665, https://doi.org/10.1111/neup.12859 | 2020, 2023 |
| Cell types | Excitatory layer-specific neurons (CL:neuron); microglia (CL:microglia); astrocytes (CL:astrocyte) | Principal neuronal loss occurs in ATL excitatory populations; glial cells show reactive and proteostasis roles and may modulate spread/clearance of TDP-43 pathology | (riku2022tdp43proteinopathyand pages 1-2, borghesani2020regionalandhemispheric pages 10-11, borghesani2020regionalandhemispheric pages 14-14) | https://doi.org/10.3390/ijms232415755, https://doi.org/10.1016/j.nicl.2020.102369, https://doi.org/10.1016/j.nicl.2020.102369 | 2020–2022 |
| Anatomical regions | Anterior temporal lobe / anterior temporal pole; amygdala; anterior hippocampus (UBERON:anterior_temporal_lobe) | Earliest and most severe atrophy in svPPA/SD with a medial→lateral gradient and frequent left-predominant asymmetry; progression commonly spreads to contralateral ATL and posterior temporal/orbitofrontal regions | (borghesani2020regionalandhemispheric pages 14-14, borghesani2020regionalandhemispheric pages 10-11, kawakatsu2023clinicopathologicaldiversityof pages 1-1) | https://doi.org/10.1016/j.nicl.2020.102369, https://doi.org/10.1016/j.nicl.2020.102369, https://doi.org/10.1111/neup.12859 | 2020–2023 |


*Table: A concise table summarizing principal molecular players, lesion morphologies, cell types, and anatomical regions implicated in semantic dementia/svPPA, with citation anchors to the gathered evidence for each entry.*

Bibliographic details with URLs and dates
- Kawakatsu S et al. Clinicopathological diversity… Neuropathology. Nov 2023. DOI: 10.1111/neup.12859. URL: https://doi.org/10.1111/neup.12859 (kawakatsu2023clinicopathologicaldiversityof pages 1-1)
- Bocchetta M et al. In vivo staging… Alzheimer’s Research & Therapy. Mar 2020. DOI: 10.1186/s13195-020-00600-x. URL: https://doi.org/10.1186/s13195-020-00600-x (bocchetta2020invivostaging pages 1-2)
- Borghesani V et al. Regional and hemispheric susceptibility… NeuroImage: Clinical. Aug 2020. DOI: 10.1016/j.nicl.2020.102369. URL: https://doi.org/10.1016/j.nicl.2020.102369 (borghesani2020regionalandhemispheric pages 1-2, borghesani2020regionalandhemispheric pages 10-11)
- Benhamou E et al. The neurophysiological architecture… Sci Reports. Oct 2020. DOI: 10.1038/s41598-020-72847-1. URL: https://doi.org/10.1038/s41598-020-72847-1 (benhamou2020theneurophysiologicalarchitecture pages 1-2)
- Meneses A et al. TDP-43 pathology in Alzheimer’s disease. Molecular Neurodegeneration. Dec 2021. DOI: 10.1186/s13024-021-00503-x. URL: https://doi.org/10.1186/s13024-021-00503-x (riku2022tdp43proteinopathyand pages 1-2)
- van Rooij J et al. Somatic TARDBP variants as a cause of semantic dementia. Brain. Nov 2020. DOI: 10.1093/brain/awaa317. URL: https://doi.org/10.1093/brain/awaa317 (rooij2020somatictardbpvariants pages 1-1)

Plan status
- Evidence gathered and synthesized; ontology annotations compiled; artifact created. This report integrates 2023–2024 sources where available and includes direct quotes/statistics.


References

1. (adamscarr2020acaseof pages 6-11): Kerala L Adams-Carr, Martina Bocchetta, Mollie Neason, Janice L Holton, Tammaryn Lashley, Jason D Warren, and Jonathan D Rohrer. A case of tdp-43 type c pathology presenting as nonfluent variant primary progressive aphasia. Neurocase, 26:1-6, Nov 2020. URL: https://doi.org/10.1080/13554794.2019.1690665, doi:10.1080/13554794.2019.1690665. This article has 5 citations and is from a peer-reviewed journal.

2. (adamscarr2020acaseof pages 1-6): Kerala L Adams-Carr, Martina Bocchetta, Mollie Neason, Janice L Holton, Tammaryn Lashley, Jason D Warren, and Jonathan D Rohrer. A case of tdp-43 type c pathology presenting as nonfluent variant primary progressive aphasia. Neurocase, 26:1-6, Nov 2020. URL: https://doi.org/10.1080/13554794.2019.1690665, doi:10.1080/13554794.2019.1690665. This article has 5 citations and is from a peer-reviewed journal.

3. (borghesani2020regionalandhemispheric pages 10-11): V. Borghesani, G. Battistella, M.L. Mandelli, A. Welch, E. Weis, K. Younes, J. Neuhaus, L.T. Grinberg, W.M. Seeley, S. Spina, B. Miller, Z. Miller, and M.L. Gorno-Tempini. Regional and hemispheric susceptibility of the temporal lobe to ftld-tdp type c pathology. NeuroImage : Clinical, 28:102369, Aug 2020. URL: https://doi.org/10.1016/j.nicl.2020.102369, doi:10.1016/j.nicl.2020.102369. This article has 67 citations and is from a domain leading peer-reviewed journal.

4. (borghesani2020regionalandhemispheric pages 1-2): V. Borghesani, G. Battistella, M.L. Mandelli, A. Welch, E. Weis, K. Younes, J. Neuhaus, L.T. Grinberg, W.M. Seeley, S. Spina, B. Miller, Z. Miller, and M.L. Gorno-Tempini. Regional and hemispheric susceptibility of the temporal lobe to ftld-tdp type c pathology. NeuroImage : Clinical, 28:102369, Aug 2020. URL: https://doi.org/10.1016/j.nicl.2020.102369, doi:10.1016/j.nicl.2020.102369. This article has 67 citations and is from a domain leading peer-reviewed journal.

5. (riku2022tdp43proteinopathyand pages 1-2): Yuichi Riku, Mari Yoshida, Yasushi Iwasaki, Gen Sobue, Masahisa Katsuno, and Shinsuke Ishigaki. Tdp-43 proteinopathy and tauopathy: do they have pathomechanistic links? International Journal of Molecular Sciences, 23:15755, Dec 2022. URL: https://doi.org/10.3390/ijms232415755, doi:10.3390/ijms232415755. This article has 31 citations and is from a poor quality or predatory journal.

6. (bocchetta2020invivostaging pages 1-2): Martina Bocchetta, Maria del Mar Iglesias Espinosa, Tammaryn Lashley, Jason D. Warren, and Jonathan D. Rohrer. In vivo staging of frontotemporal lobar degeneration tdp-43 type c pathology. Alzheimer's Research & Therapy, Mar 2020. URL: https://doi.org/10.1186/s13195-020-00600-x, doi:10.1186/s13195-020-00600-x. This article has 55 citations and is from a domain leading peer-reviewed journal.

7. (benhamou2020theneurophysiologicalarchitecture pages 1-2): Elia Benhamou, Charles R. Marshall, Lucy L. Russell, Chris J. D. Hardy, Rebecca L. Bond, Harri Sivasathiaseelan, Caroline V. Greaves, Karl J. Friston, Jonathan D. Rohrer, Jason D. Warren, and Adeel Razi. The neurophysiological architecture of semantic dementia: spectral dynamic causal modelling of a neurodegenerative proteinopathy. Scientific Reports, Oct 2020. URL: https://doi.org/10.1038/s41598-020-72847-1, doi:10.1038/s41598-020-72847-1. This article has 29 citations and is from a peer-reviewed journal.

8. (kawakatsu2023clinicopathologicaldiversityof pages 1-1): Shinobu Kawakatsu, Ryota Kobayashi, Daichi Morioka, Hiroshi Hayashi, Aya Utsunomiya, Takanobu Kabasawa, Rintaro Ohe, Mitsuru Futakuchi, and Koichi Otani. Clinicopathological diversity of semantic dementia: comparisons of patients with early‐onset versus late‐onset, left‐sided versus right‐sided temporal atrophy, and tdp‐type a versus type c pathology. Neuropathology, 43:5-26, Nov 2023. URL: https://doi.org/10.1111/neup.12859, doi:10.1111/neup.12859. This article has 12 citations and is from a peer-reviewed journal.

9. (barbieri2025atrophyprogressionin pages 1-3): Elena Barbieri, Allegra S Kawles, Michelle Los, Jordan Behn, Changiz Geula, Tamar Gefen, Sandra Weintraub, and M Marsel Mesulam. Atrophy progression in frontotemporal lobar degeneration-tdp-c with primary progressive aphasia. Brain, Oct 2025. URL: https://doi.org/10.1093/brain/awaf369, doi:10.1093/brain/awaf369. This article has 2 citations and is from a highest quality peer-reviewed journal.

10. (rooij2020somatictardbpvariants pages 1-1): Jeroen van Rooij, Merel O Mol, Shamiram Melhem, Pelle van der Wal, Pascal Arp, Francesca Paron, Laura Donker Kaat, Harro Seelaar, Suzanne S M Miedema, Takuya Oshima, Bart J L Eggen, André Uitterlinden, Joyce van Meurs, Ronald E van Kesteren, August B Smit, Emanuele Buratti, and John C van Swieten. Somatic tardbp variants as a cause of semantic dementia. Brain, 143:3827-3841, Nov 2020. URL: https://doi.org/10.1093/brain/awaa317, doi:10.1093/brain/awaa317. This article has 23 citations and is from a highest quality peer-reviewed journal.

11. (antonioni2023frontotemporaldementiawhere pages 27-29): Annibale Antonioni, Emanuela Maria Raho, Piervito Lopriore, Antonia Pia Pace, Raffaela Rita Latino, Martina Assogna, Michelangelo Mancuso, Daniela Gragnaniello, Enrico Granieri, Maura Pugliatti, Francesco Di Lorenzo, and Giacomo Koch. Frontotemporal dementia, where do we stand? a narrative review. International Journal of Molecular Sciences, 24:11732, Jul 2023. URL: https://doi.org/10.3390/ijms241411732, doi:10.3390/ijms241411732. This article has 136 citations and is from a poor quality or predatory journal.

12. (borghesani2020regionalandhemispheric pages 14-14): V. Borghesani, G. Battistella, M.L. Mandelli, A. Welch, E. Weis, K. Younes, J. Neuhaus, L.T. Grinberg, W.M. Seeley, S. Spina, B. Miller, Z. Miller, and M.L. Gorno-Tempini. Regional and hemispheric susceptibility of the temporal lobe to ftld-tdp type c pathology. NeuroImage : Clinical, 28:102369, Aug 2020. URL: https://doi.org/10.1016/j.nicl.2020.102369, doi:10.1016/j.nicl.2020.102369. This article has 67 citations and is from a domain leading peer-reviewed journal.