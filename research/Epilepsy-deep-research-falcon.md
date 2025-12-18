---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T18:47:17.715957'
end_time: '2025-12-17T18:55:38.487872'
duration_seconds: 500.77
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Epilepsy
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Epilepsy**.
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
- **Disease Name:** Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Epilepsy**.
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
- Disease Name: Epilepsy
- MONDO ID: MONDO:0005151
- Category: Complex

## Pathophysiology description (current understanding, 2023–2024 updates)
Epilepsy arises from converging molecular and cellular mechanisms that increase network excitability and synchrony. Core drivers include: (i) excitation–inhibition (E/I) imbalance due to ion channelopathies (e.g., SCN1A, KCNQ2/3, multiple Kv genes) and impaired GABAergic synaptic inhibition; (ii) glial mechanisms of neuroinflammation (microglia, astrocytes), including TLR/NF-κB and inflammasome-related signaling; (iii) blood–brain barrier (BBB) dysfunction with extravasation of serum proteins (e.g., albumin) and downstream TGF-β–astrocytic signaling; (iv) mTORC1 hyperactivation in “mTORopathies” (e.g., DEPDC5-related focal cortical dysplasia) with aberrant neuronal growth and synaptic function; (v) epigenetic dysregulation interacting with inflammatory and synaptic pathways; and (vi) mitochondrial/oxidative stress that lowers seizure threshold and perpetuates injury–inflammation cycles. Recent human studies have mapped altered E/I and gene expression to cognitive outcomes (TLE), demonstrated BBB causal roles and druggable stabilization strategies, and advanced precision therapies including SCN1A antisense oligonucleotides (ASOs) and senolytics for mTOR-related dysmorphic neurons (2022–2024) (duma2024excitationinhibitionbalancerelates pages 1-3, han2024unveilingthehidden pages 1-2, greene2022microvascularstabilizationvia pages 1-2, yuan2024asorestoresexcitability pages 1-2, ribierre2024targetingpathologicalcells pages 1-2).

URLs: 
- E/I mapping in TLE (Brain Communications, 2024): https://doi.org/10.1093/braincomms/fcae231 (duma2024excitationinhibitionbalancerelates pages 1-3)
- BBB and epilepsy (Frontiers in Neurology, 2024): https://doi.org/10.3389/fneur.2024.1413023 (han2024unveilingthehidden pages 1-2)
- BBB stabilization prevents seizures (Nature Communications, 2022): https://doi.org/10.1038/s41467-022-29657-y (greene2022microvascularstabilizationvia pages 1-2)
- SCN1A ASO in Dravet model (Brain, 2024): https://doi.org/10.1093/brain/awad349 (yuan2024asorestoresexcitability pages 1-2)
- Senolytics in mTOR-related epilepsy (Nature Neuroscience, 2024): https://doi.org/10.1038/s41593-024-01634-2 (ribierre2024targetingpathologicalcells pages 1-2)

## 1. Core Pathophysiology
- E/I imbalance and ion channelopathies: In TLE, noninvasive EEG aperiodic exponent mapping identified regional E/I shifts that correlate with cognitive deficits and cortical expression of GABRA1, GRIN2A, GABRD, GABRG2, KCNA2, and PDYN, directly linking E/I to molecular architecture (Brain Communications 2024) (duma2024excitationinhibitionbalancerelates pages 1-3). Genetic epilepsies involve loss-/gain-of-function in voltage-gated potassium channels (KCNA1/2, KCNB1, KCNC1, KCND2, KCNQ2/3, KCNH1/5) that alter repolarization and network excitability (Frontiers in Neurology 2024) (zheng2024voltagegatedpotassiumchannels pages 1-2).
- Glial neuroinflammation: Reactive astrocytes and microglia, activated by DAMPs (e.g., HMGB1), propagate cytokine signaling (IL-1, IL-6, TNF) via TLR/NF-κB and related pathways; sustained inflammation feeds seizure propensity and drug resistance (IJMS 2024) (sanz2024neuroinflammationandepilepsy pages 1-2).
- BBB dysfunction and albumin–TGF-β–astrocyte signaling: Reviews and translational studies converge that BBB breakdown increases permeability, leads to albumin uptake by astrocytes, weakens junctions, perturbs ionic homeostasis, and contributes to epileptogenesis; BBB changes also limit drug penetration (Frontiers in Neurology 2024) (han2024unveilingthehidden pages 1-2). Human surgical tissue and mouse models show claudin-5 loss, albumin/IgG extravasation, and neuroinflammation; claudin-5 knockdown induces spontaneous seizures, whereas RepSox restores claudin-5 and prevents seizures (Nature Communications 2022) (greene2022microvascularstabilizationvia pages 1-2).
- mTOR/DEPDC5 and cortical malformations: Brain somatic mosaicism of mTORC1 pathway genes (MTOR, RHEB) or loss of repressors (DEPDC5/GATOR1, TSC1, PTEN) in cortical progenitors causes focal malformations (FCD/HME), shared pyramidal neuron morphological and excitability abnormalities, and gene-specific synaptic changes (eLife 2024) (nguyen2024themtorpathway pages 1-2). DEPDC5 loss hyperactivates mTORC1; rapamycin rescues biochemical and survival phenotypes in Depdc5 neuronal KO mice (HMG 2019) (yuskaitis2019chronicmtorc1inhibition pages 2-3).
- Epigenetic regulation: Epileptogenesis involves epigenetic dysregulation affecting inflammatory and synaptic genes; antiepileptogenic strategies targeting epigenetic and inflammatory processes are under study (Health Science Reports 2024) (shariff2024advancesinunderstanding pages 5-6, shariff2024advancesinunderstanding pages 4-5).
- Mitochondrial/oxidative stress: Oxidative stress and mitochondrial dysfunction (e.g., ROS, mtDNA injury) contribute to neuronal hyperexcitability and amplify inflammatory cascades, reinforcing epileptogenesis (Health Science Reports 2024) (shariff2024advancesinunderstanding pages 5-6).

## 2. Key Molecular Players
- Genes/Proteins (HGNC):
  - SCN1A (Nav1.1): GABAergic interneuron haploinsufficiency → impaired inhibition (ASO upregulates Scn1a; restores PV-IN sodium currents and GABA signaling) (yuan2024asorestoresexcitability pages 1-2).
  - GABRA1/GABRG2: GABA-A receptor subunits; human E/I mapping correlates with cortical expression; mutations reduce inhibitory currents (duma2024excitationinhibitionbalancerelates pages 1-3).
  - KCNQ2/KCNQ3 (Kv7.2/7.3): M-current reduction drives neonatal DEEs; channelopathies underpin hyperexcitability (zheng2024voltagegatedpotassiumchannels pages 1-2).
  - KCNA2 and other Kv genes: diverse LOF/GOF epilepsies shaping excitability (zheng2024voltagegatedpotassiumchannels pages 1-2).
  - DEPDC5 (GATOR1): mTORC1 disinhibition → cortical malformations and focal epilepsy (nguyen2024themtorpathway pages 1-2, yuskaitis2019chronicmtorc1inhibition pages 2-3).
  - MTOR/RHEB/PTEN/TSC1: mTORC1 axis; mutations drive “mTORopathies” (nguyen2024themtorpathway pages 1-2).
  - CLDN5 (claudin-5): endothelial tight junction; loss associates with BBB leakage and seizures (greene2022microvascularstabilizationvia pages 1-2).
  - HMGB1/TLR4: DAMP–TLR signaling in neuroinflammation (sanz2024neuroinflammationandepilepsy pages 1-2).

- Chemical Entities (ChEBI):
  - γ-aminobutyric acid (GABA; CHEBI:16865); L-glutamate (CHEBI:29988) – neurotransmitters of inhibitory/excitatory balance (duma2024excitationinhibitionbalancerelates pages 1-3).
  - Albumin (CHEBI:16580) – extravasated BBB cargo activating astrocytic TGF-β signaling (han2024unveilingthehidden pages 1-2).
  - Everolimus/rapamycin (mTOR inhibitors; CHEBI:68478, CHEBI:9168) – mTORopathy-directed therapies (yuskaitis2019chronicmtorc1inhibition pages 2-3, nguyen2024themtorpathway pages 1-2).
  - Dasatinib (CHEBI:467849) + Quercetin (CHEBI:16243) – senolytic regimen reducing seizures in mTOR-FCD model (ribierre2024targetingpathologicalcells pages 1-2).
  - Cannabidiol (CHEBI:69478) – precision adjunct with syndrome-specific benefit (context of precision care) (li2025progressingenetic pages 3-4).
  - RepSox (ALK5/TGF-β signaling modulator) – BBB stabilization and seizure prevention in mice (greene2022microvascularstabilizationvia pages 1-2).

- Cell Types (CL):
  - Parvalbumin-positive (PV) GABAergic interneurons – selectively impaired in SCN1A; ASO restores function (yuan2024asorestoresexcitability pages 1-2).
  - Excitatory cortical pyramidal neurons – altered morphology/excitability in mTORopathy models (nguyen2024themtorpathway pages 1-2).
  - Astrocytes – albumin uptake, TGF-β signaling; glutamate/GABA homeostasis; inflammatory mediators (han2024unveilingthehidden pages 1-2, sanz2024neuroinflammationandepilepsy pages 1-2).
  - Microglia – innate immune activation (TLR/NLR), cytokine release; network effects (sanz2024neuroinflammationandepilepsy pages 1-2).
  - Endothelial cells/pericytes – BBB structural components (han2024unveilingthehidden pages 1-2).

- Anatomical Locations (UBERON):
  - Hippocampus (temporal lobe) – human TLE focus, BBB disruption (greene2022microvascularstabilizationvia pages 1-2).
  - Neocortex (focal cortical dysplasia) – mTOR-related malformations and epileptogenic nodes (nguyen2024themtorpathway pages 1-2).
  - Cerebral microvasculature – BBB (han2024unveilingthehidden pages 1-2).

## 3. Biological Processes (GO terms; disrupted in epilepsy)
- Synaptic transmission, GABAergic (GO:0051932); inhibitory postsynaptic potential (GABA-A complex) (duma2024excitationinhibitionbalancerelates pages 1-3).
- Synaptic transmission, glutamatergic (GO:0035249) and regulation of postsynaptic membrane potential (duma2024excitationinhibitionbalancerelates pages 1-3).
- Regulation of membrane potential/action potential (GO:0042391; GO:0001508) via Na+ and K+ channels (zheng2024voltagegatedpotassiumchannels pages 1-2, yuan2024asorestoresexcitability pages 1-2).
- Blood–brain barrier establishment/maintenance (GO:1903160) and endothelial cell–cell adhesion (greene2022microvascularstabilizationvia pages 1-2, han2024unveilingthehidden pages 1-2).
- mTORC1 signaling (GO:0031931), regulation of translation and cell growth (nguyen2024themtorpathway pages 1-2, yuskaitis2019chronicmtorc1inhibition pages 2-3).
- Innate immune response, TLR signaling (GO:0002224), NF-κB signaling, cytokine production (sanz2024neuroinflammationandepilepsy pages 1-2).
- Response to oxidative stress/ROS and mitochondrial processes (GO:0006979) (shariff2024advancesinunderstanding pages 5-6).

## 4. Cellular Components (GO)
- Axon initial segment; voltage-gated sodium/potassium channel complexes (yuan2024asorestoresexcitability pages 1-2, zheng2024voltagegatedpotassiumchannels pages 1-2).
- GABA-A receptor complex; postsynaptic density (duma2024excitationinhibitionbalancerelates pages 1-3).
- Tight junction (endothelial) at BBB (greene2022microvascularstabilizationvia pages 1-2).
- Lysosomal surface/cytosol (mTORC1 localization and regulation) (nguyen2024themtorpathway pages 1-2).
- Extracellular space (HMGB1 as DAMP upon release) (sanz2024neuroinflammationandepilepsy pages 1-2).

## 5. Disease Progression (sequence of events)
- Initiation: genetic predisposition (e.g., ion channel or mTOR pathway variants) or acquired injury (TBI, infection) → acute seizures, BBB opening, and DAMP release (han2024unveilingthehidden pages 1-2, nguyen2024themtorpathway pages 1-2, shariff2024advancesinunderstanding pages 4-5).
- Latency/epileptogenesis: BBB leakage (albumin/IgG), astrocytic TGF-β signaling, microglial activation, cytokine cascades, oxidative stress, and synaptic/network remodeling (han2024unveilingthehidden pages 1-2, greene2022microvascularstabilizationvia pages 1-2, sanz2024neuroinflammationandepilepsy pages 1-2, shariff2024advancesinunderstanding pages 5-6).
- Chronic epilepsy: stabilized network hyperexcitability with E/I imbalance (regional), persistent neuroinflammation, structural lesions (FCD/HME) in mTORopathies; cognitive comorbidity correlates with E/I maps (duma2024excitationinhibitionbalancerelates pages 1-3, nguyen2024themtorpathway pages 1-2).

## 6. Phenotypic Manifestations (HPO) and links to mechanisms
- Seizures (HP:0001250) and status epilepticus (HP:0002133): emergent property of E/I imbalance, BBB dysfunction, and inflammatory signaling (han2024unveilingthehidden pages 1-2, greene2022microvascularstabilizationvia pages 1-2, sanz2024neuroinflammationandepilepsy pages 1-2).
- Cognitive impairment (HP:0100543), memory deficits (HP:0002354): correlate with E/I changes in entorhinal/dorsolateral prefrontal cortices in TLE (duma2024excitationinhibitionbalancerelates pages 1-3).
- Developmental delay (HP:0001263) and epileptic encephalopathy (HP:0200134): channelopathies (SCN1A, KCNQ2/3) and mTORopathies (DEPDC5/TSC1) (yuan2024asorestoresexcitability pages 1-2, zheng2024voltagegatedpotassiumchannels pages 1-2, nguyen2024themtorpathway pages 1-2).

## Key evidence items with PMIDs/DOIs, URLs, dates (quotes where available)
- E/I mapping in human TLE: “EEG aperiodic exponent maps the E/I balance non-invasively... correlation between the exponent and the cortical expression of GABRA1, GRIN2A, GABRD, GABRG2, KCNA2 and PDYN” (Brain Communications, 2024-02-23; https://doi.org/10.1093/braincomms/fcae231) (duma2024excitationinhibitionbalancerelates pages 1-3).
- Kv channelopathies: “Both gain and loss-of-function of Kv channels lead to epilepsy with similar phenotypes through different mechanisms” (Frontiers in Neurology, 2024-10-14; https://doi.org/10.3389/fneur.2024.1466075) (zheng2024voltagegatedpotassiumchannels pages 1-2).
- Neuroinflammation cascade: “DAMPs such as HMGB1… activate PRRs (TLRs, NLRs) → NF-κB… reactive glia release cytokines/ROS” (IJMS, 2024-04-09; https://doi.org/10.3390/ijms25084161) (sanz2024neuroinflammationandepilepsy pages 1-2).
- BBB roles and mechanisms: “Disruption of the blood–brain barrier… increased leakage… albumin is taken up into astrocytes” (Frontiers in Neurology, 2024-08-21; https://doi.org/10.3389/fneur.2024.1413023) (han2024unveilingthehidden pages 1-2).
- BBB stabilization as therapy: “Claudin-5 levels are diminished in TLE; inducible knockdown leads to spontaneous seizures… RepSox… can prevent seizure activity” (Nature Communications, 2022-04-13; https://doi.org/10.1038/s41467-022-29657-y) (greene2022microvascularstabilizationvia pages 1-2).
- mTOR/DEPDC5 mechanisms: “Somatic mutations in mTORC1 genes… produce shared alterations… but different changes in excitatory synaptic transmission” (eLife, 2024-02-23; https://doi.org/10.7554/eLife.91010.3) (nguyen2024themtorpathway pages 1-2). “mTORC1 inhibitor rapamycin… prolonged survival of Depdc5cc+ mice and rescued downstream mTORC1 hyperactivity” (HMG, 2019-05-24; https://doi.org/10.1093/hmg/ddz123) (yuskaitis2019chronicmtorc1inhibition pages 2-3).
- Senolytics for FCD/mTOR: “Dysmorphic neurons exhibit senescence signatures… dasatinib/quercetin decreased senescent cells and reduced seizure frequency” (Nature Neuroscience, 2024-05-27; https://doi.org/10.1038/s41593-024-01634-2) (ribierre2024targetingpathologicalcells pages 1-2).
- SCN1A ASO precision therapy: “ASO-84 restored action potential firing, sodium current density, and GABAergic signaling in PV+ interneurons” (Brain, 2024-10-01; https://doi.org/10.1093/brain/awad349) (yuan2024asorestoresexcitability pages 1-2).

## Current applications and real-world implementations
- Precision neuromodulation of E/I: EEG aperiodic exponent can noninvasively map E/I and relate to cognition and cortical gene expression, suggesting utility for stratification and monitoring in TLE (duma2024excitationinhibitionbalancerelates pages 1-3).
- BBB-directed interventions: Imaging/evidence of BBB disruption in human refractory epilepsy; preclinical evidence supports targeting tight junctions (claudin-5 upregulation with RepSox) as a seizure-preventive strategy (greene2022microvascularstabilizationvia pages 1-2, han2024unveilingthehidden pages 1-2).
- mTOR-targeted therapy: Rapamycin/everolimus are clinically used in TSC and supported as rational strategies for DEPDC5-related epilepsies by preclinical mechanistic rescue (yuskaitis2019chronicmtorc1inhibition pages 2-3, nguyen2024themtorpathway pages 1-2).
- Senotherapy: Early preclinical evidence for senolytics (dasatinib/quercetin) reducing seizures in mTOR-related FCD models (ribierre2024targetingpathologicalcells pages 1-2).
- Gene-directed therapy: SCN1A ASO (poison exon skipping) restores PV interneuron function in Dravet mice; serves as mechanistic basis for clinical translation (yuan2024asorestoresexcitability pages 1-2).

## Expert perspectives (authoritative sources)
- E/I imbalance in humans is quantifiable and genetically anchored in cortex, linking physiology to gene expression and cognition (Brain Communications 2024) (duma2024excitationinhibitionbalancerelates pages 1-3).
- The BBB is not merely a bystander but a mechanistic contributor and drug resistance modulator; claudin-5 represents a tractable target (Nature Communications 2022; Frontiers in Neurology 2024) (greene2022microvascularstabilizationvia pages 1-2, han2024unveilingthehidden pages 1-2).
- mTORopathies converge on mTORC1 hyperactivation but diverge in synaptic transmission, implying gene-specific precision strategies beyond “class-wide” mTOR inhibition (eLife 2024) (nguyen2024themtorpathway pages 1-2).
- Reactive gliosis and innate immune sensors (HMGB1–TLR) are central to epileptogenesis; anti-inflammatory/immune-modulatory approaches remain promising adjuncts (IJMS 2024) (sanz2024neuroinflammationandepilepsy pages 1-2).

## Relevant statistics and data
- TLE patients displayed significantly larger EEG aperiodic exponent values (inhibition-directed E/I), with regional exponents correlating with worse verbal memory (quantitative correlation) and with expression of GABRA1, GRIN2A, GABRD, GABRG2, KCNA2, PDYN (duma2024excitationinhibitionbalancerelates pages 1-3).
- Human TLE resections show significantly reduced claudin-5 protein and widespread BBB leakage by DCE-MRI; inducible claudin-5 knockdown in mice induces spontaneous recurrent seizures (greene2022microvascularstabilizationvia pages 1-2).
- In human FCDII slices, epileptiform activity correlated with dysmorphic neuron density (e.g., ≈54 vs 12 DNs/mm² between hyperactive vs quieter areas); senolytics reduced seizure frequency in MtorS2215F mice (ribierre2024targetingpathologicalcells pages 1-2).

## Gene/protein annotations with ontology terms (selected)

| HGNC symbol | Full name | Primary mechanism in epilepsy (1–2 lines) | Pathway(s) | GO Biological Process (examples) | GO Cellular Component (examples) | Key cell types (CL names) | Key anatomy (UBERON names) | Anchor citations |
|---|---|---|---|---|---|---|---|---|
| SCN1A | Sodium voltage-gated channel alpha subunit 1 | Haploinsufficiency/LOF in GABAergic interneurons → reduced inhibition, network hyperexcitability | Voltage-gated sodium channel / action potential generation | Regulation of membrane potential; action potential; sodium ion transmembrane transport | Axon initial segment; plasma membrane; voltage-gated sodium channel complex | GABAergic interneurons (parvalbumin-positive, somatostatin-positive) | Cerebral cortex; hippocampus | (yuan2024asorestoresexcitability pages 1-2, zhang2025dravetsyndromenovel pages 15-16) |
| GABRA1 | GABA A receptor alpha1 subunit | LOF/reduced surface expression → impaired inhibitory synaptic currents and reduced GABAergic tone | GABAergic synaptic transmission | Inhibitory synaptic transmission; chloride transport; synaptic transmission | Postsynaptic membrane; GABA-A receptor complex; synapse | Pyramidal neuron postsynaptic sites; interneuron synapses | Cortex; hippocampus | (duma2024excitationinhibitionbalancerelates pages 1-3, sanz2024neuroinflammationandepilepsy pages 1-2) |
| GABRG2 | GABA A receptor gamma2 subunit | Mutations impair receptor biogenesis/clustering → decreased synaptic inhibition and DEE phenotypes | GABA-A receptor assembly and synaptic localization | Inhibitory synaptic transmission; receptor trafficking | Postsynaptic density; plasma membrane; GABA-A receptor complex | GABAergic synapses; interneuron→pyramidal neuron synapses | Cortex; hippocampus | (duma2024excitationinhibitionbalancerelates pages 1-3, sanz2024neuroinflammationandepilepsy pages 1-2) |
| KCNQ2 | Potassium voltage-gated channel subfamily Q member 2 (Kv7.2) | Loss-of-function reduces M-current → neonatal hyperexcitability, developmental impairment | Kv7 (M-current) / neuronal excitability control | Potassium ion transmembrane transport; regulation of neuronal excitability | Plasma membrane; axon initial segment; potassium channel complex | Excitatory neurons; developing cortical neurons | Cortex; hippocampus | (zheng2024voltagegatedpotassiumchannels pages 1-2, liu2024excitatoryneuronsand pages 1-3) |
| KCNQ3 | Potassium voltage-gated channel subfamily Q member 3 (Kv7.3) | Partners with KCNQ2 in M-current; variants modulate channel function and excitability | Kv7 (M-current) / heteromeric KCNQ2/3 channels | Regulation of membrane potential; potassium ion transport | Plasma membrane; axon initial segment | Excitatory neurons; developing neurons | Cortex; hippocampus | (zheng2024voltagegatedpotassiumchannels pages 1-2, liu2024excitatoryneuronsand pages 1-3) |
| KCNA2 | Potassium voltage-gated channel subfamily A member 2 (Kv1.2) | Kv channel dysfunction (LOF/GOF) alters repolarization → network hyperexcitability or aberrant firing | Kv1 family / action potential repolarization | Potassium ion transmembrane transport; regulation of action potential | Plasma membrane; presynaptic terminal; ion channel complex | Excitatory neurons; inhibitory interneurons | Cortex; hippocampus | (duma2024excitationinhibitionbalancerelates pages 1-3, zheng2024voltagegatedpotassiumchannels pages 1-2) |
| DEPDC5 | DEP domain containing 5 (GATOR1 complex subunit) | LOF → loss of GATOR1 repression → mTORC1 hyperactivation; somatic/germline variants cause FCD and focal epilepsy | GATOR1 → mTORC1 regulation | Regulation of mTOR signaling; cell growth; autophagy regulation | Cytosol; lysosomal membrane (mTORC1 localization) | Excitatory neuronal progenitors / cortical neurons | Focal cortex (cortical malformations, FCD) | (yuskaitis2019chronicmtorc1inhibition pages 2-3, nguyen2024themtorpathway pages 1-2, ribierre2024targetingpathologicalcells pages 1-2) |
| MTOR | Mechanistic target of rapamycin kinase | mTORC1 hyperactivation → abnormal neuronal growth/plasticity, epileptogenesis in mTORopathies | mTORC1 signaling / protein synthesis and growth | Regulation of translation; cell growth; synaptic plasticity | Cytosol; lysosomal membrane; mTORC1 complex | Neurons (excitatory), progenitors, glia | Cortex (FCD), hippocampus | (nguyen2024themtorpathway pages 1-2, yuskaitis2019chronicmtorc1inhibition pages 2-3) |
| RHEB | Ras homolog enriched in brain | Small GTPase activator of mTORC1; gain-of-function → mTORC1 activation in cortical development | mTORC1 activation via Rheb-GTP | Positive regulation of mTOR signaling; regulation of cell growth | Cytosol; lysosomal membrane | Neuronal progenitors; excitatory neurons | Cortex; developing telencephalon | (nguyen2024themtorpathway pages 1-2) |
| PTEN | Phosphatase and tensin homolog | Loss reduces PI3K/AKT inhibition → increased mTOR signaling and altered neuronal morphology/excitability | PI3K-AKT- mTOR pathway regulation | Negative regulation of PI3K signaling; cell growth control | Cytosol; plasma membrane; nucleus | Neurons; glia; progenitors | Cortex; hippocampus | (nguyen2024themtorpathway pages 1-2) |
| TSC1 | Tuberous sclerosis 1 | Part of TSC1/TSC2 complex suppressing mTORC1; loss → mTORC1-driven cortical dysplasia and seizures | TSC complex → mTORC1 inhibition | Negative regulation of mTOR signaling; cell growth; autophagy | Cytosol; lysosomal membrane | Neuronal progenitors; neurons | Cortex (tuberous sclerosis lesions), hippocampus | (yuskaitis2019chronicmtorc1inhibition pages 2-3, nguyen2024themtorpathway pages 1-2) |
| CLDN5 | Claudin-5 | Tight junction protein; decreased expression → BBB leakage, albumin extravasation and seizure susceptibility | Tight junction / BBB integrity | Establishment of blood–brain barrier; cell–cell adhesion | Tight junction; endothelial cell membrane | Brain endothelial cells; pericytes; astrocyte end-feet | Cerebral microvasculature; hippocampus | (greene2022microvascularstabilizationvia pages 1-2) |
| HMGB1 | High mobility group box 1 | Damage-associated molecular pattern (DAMP) released after injury/seizures → activates innate immunity and promotes epileptogenesis | DAMP signaling → TLR/NF-κB / inflammasome activation | Release of DAMPs; positive regulation of inflammatory response; cytokine production | Nucleus (normal); extracellular space (released DAMP) | Microglia; astrocytes; neurons | Hippocampus; cortex | (sanz2024neuroinflammationandepilepsy pages 1-2) |
| TLR4 | Toll-like receptor 4 | Pattern recognition receptor sensing HMGB1/LPS → NF-κB activation, cytokine release, neuroinflammation linked to seizure propagation | TLR signaling → NF-κB / inflammasome pathways | Innate immune response; cytokine-mediated signaling; inflammatory response | Plasma membrane; endosome (signaling) | Microglia; astrocytes; endothelial cells | Hippocampus; cortex | (sanz2024neuroinflammationandepilepsy pages 1-2) |


*Table: Concise ontology-ready table mapping 14 epilepsy-relevant genes/proteins to mechanisms, pathways, GO processes/components, cell types, anatomical sites and anchor citations; useful for knowledgebase annotations and GO/ontology curation.*

## Phenotype associations (HPO), Cell types (CL), Anatomy (UBERON), Chemicals (ChEBI)
- HPO: HP:0001250 Seizure; HP:0002133 Status epilepticus; HP:0100543 Cognitive impairment; HP:0002354 Memory impairment (duma2024excitationinhibitionbalancerelates pages 1-3, han2024unveilingthehidden pages 1-2, greene2022microvascularstabilizationvia pages 1-2).
- CL: PV GABAergic interneuron; astrocyte; microglial cell; brain endothelial cell; pericyte (yuan2024asorestoresexcitability pages 1-2, sanz2024neuroinflammationandepilepsy pages 1-2, han2024unveilingthehidden pages 1-2).
- UBERON: hippocampus; cerebral cortex (temporal neocortex); cerebral microvasculature (greene2022microvascularstabilizationvia pages 1-2, nguyen2024themtorpathway pages 1-2, han2024unveilingthehidden pages 1-2).
- ChEBI: GABA (CHEBI:16865), L-glutamate (CHEBI:29988), albumin (CHEBI:16580), rapamycin/sirolimus (CHEBI:9168), everolimus (CHEBI:68478), dasatinib (CHEBI:467849), quercetin (CHEBI:16243), cannabidiol (CHEBI:69478) (han2024unveilingthehidden pages 1-2, greene2022microvascularstabilizationvia pages 1-2, ribierre2024targetingpathologicalcells pages 1-2, yuan2024asorestoresexcitability pages 1-2, yuskaitis2019chronicmtorc1inhibition pages 2-3, nguyen2024themtorpathway pages 1-2, li2025progressingenetic pages 3-4).

## Single-cell/spatial transcriptomics in human epilepsy
- Multimodal single-nucleus RNA/ATAC profiling of human FCD IIIa temporal neocortex revealed selective dysregulation of excitatory neurons (including a DAB1high subpopulation with immune signatures) and activated OPCs, with aberrant EN–OPC communication validated by protein assays (Clinical and Translational Medicine, 2024-10-15; https://doi.org/10.1002/ctm2.70072) (liu2024excitatoryneuronsand pages 1-3).

## Precision therapeutics—summary of opportunities
- SCN1A ASOs (poison-exon modulation) restore PV interneuron excitability, sodium current density, and GABAergic drive in Dravet mice; supports translation to mechanism-guided trials (yuan2024asorestoresexcitability pages 1-2).
- mTOR inhibition (rapamycin/everolimus) rational in TSC and mechanistically supported for DEPDC5-related epilepsies; gene-specific differences suggest combining with synapse-focused strategies (yuskaitis2019chronicmtorc1inhibition pages 2-3, nguyen2024themtorpathway pages 1-2).
- BBB stabilization (targeting claudin-5/TGF-β signaling modulators such as RepSox) prevents seizures in models; motivates biomarker-driven patient selection in DRE with BBB leakage (greene2022microvascularstabilizationvia pages 1-2, han2024unveilingthehidden pages 1-2).
- Senolytics (dasatinib/quercetin) reduce seizure burden in mTOR-FCD models by ablating senescent dysmorphic neurons; a candidate disease-modifying approach needing careful safety evaluation (ribierre2024targetingpathologicalcells pages 1-2).

## Evidence list (citable items)
- Duma et al., Brain Communications, 2024-02-23. URL: https://doi.org/10.1093/braincomms/fcae231 (duma2024excitationinhibitionbalancerelates pages 1-3).
- Han et al., Frontiers in Neurology, 2024-08-21. URL: https://doi.org/10.3389/fneur.2024.1413023 (han2024unveilingthehidden pages 1-2).
- Greene et al., Nature Communications, 2022-04-13. URL: https://doi.org/10.1038/s41467-022-29657-y (greene2022microvascularstabilizationvia pages 1-2).
- Zheng & Chen, Frontiers in Neurology, 2024-10-14. URL: https://doi.org/10.3389/fneur.2024.1466075 (zheng2024voltagegatedpotassiumchannels pages 1-2).
- Sanz et al., IJMS, 2024-04-09. URL: https://doi.org/10.3390/ijms25084161 (sanz2024neuroinflammationandepilepsy pages 1-2).
- Nguyen et al., eLife, 2024-02-23. URL: https://doi.org/10.7554/eLife.91010.3 (nguyen2024themtorpathway pages 1-2).
- Yuskaitis et al., Human Molecular Genetics, 2019-05-24. URL: https://doi.org/10.1093/hmg/ddz123 (yuskaitis2019chronicmtorc1inhibition pages 2-3).
- Ribierre et al., Nature Neuroscience, 2024-05-27. URL: https://doi.org/10.1038/s41593-024-01634-2 (ribierre2024targetingpathologicalcells pages 1-2).
- Yuan et al., Brain, 2024-10-01. URL: https://doi.org/10.1093/brain/awad349 (yuan2024asorestoresexcitability pages 1-2).
- Liu et al., Clinical and Translational Medicine, 2024-10-15. URL: https://doi.org/10.1002/ctm2.70072 (liu2024excitatoryneuronsand pages 1-3).
- Shariff et al., Health Science Reports, 2024-02. URL: https://doi.org/10.1002/hsr2.1896 (shariff2024advancesinunderstanding pages 5-6, shariff2024advancesinunderstanding pages 4-5).



References

1. (duma2024excitationinhibitionbalancerelates pages 1-3): Gian Marco Duma, Simone Cuozzo, Luc Wilson, Alberto Danieli, Paolo Bonanni, and Giovanni Pellegrino. Excitation/inhibition balance relates to cognitive function and gene expression in temporal lobe epilepsy: a high density eeg assessment with aperiodic exponent. Brain Communications, Feb 2024. URL: https://doi.org/10.1093/braincomms/fcae231, doi:10.1093/braincomms/fcae231. This article has 25 citations and is from a peer-reviewed journal.

2. (han2024unveilingthehidden pages 1-2): Jinkun Han, Ying Wang, Penghu Wei, Di Lu, and Yongzhi Shan. Unveiling the hidden connection: the blood-brain barrier’s role in epilepsy. Frontiers in Neurology, Aug 2024. URL: https://doi.org/10.3389/fneur.2024.1413023, doi:10.3389/fneur.2024.1413023. This article has 6 citations and is from a peer-reviewed journal.

3. (greene2022microvascularstabilizationvia pages 1-2): Chris Greene, Nicole Hanley, Cristina R. Reschke, Avril Reddy, Maarja A. Mäe, Ruairi Connolly, Claire Behan, Eoin O’Keeffe, Isobel Bolger, Natalie Hudson, Conor Delaney, Michael A. Farrell, Donncha F. O’Brien, Jane Cryan, Francesca M. Brett, Alan Beausang, Christer Betsholtz, David C. Henshall, Colin P. Doherty, and Matthew Campbell. Microvascular stabilization via blood-brain barrier regulation prevents seizure activity. Nature Communications, Apr 2022. URL: https://doi.org/10.1038/s41467-022-29657-y, doi:10.1038/s41467-022-29657-y. This article has 145 citations and is from a highest quality peer-reviewed journal.

4. (yuan2024asorestoresexcitability pages 1-2): Yukun Yuan, Luis Lopez-Santiago, Nicholas Denomme, Chunling Chen, Heather A O'Malley, Samantha L Hodges, Sophina Ji, Zhou Han, Anne Christiansen, and Lori L Isom. Aso restores excitability, gaba signalling and sodium current density in a model of dravet syndrome. Brain : a journal of neurology, 147:1231-1246, Oct 2024. URL: https://doi.org/10.1093/brain/awad349, doi:10.1093/brain/awad349. This article has 36 citations.

5. (ribierre2024targetingpathologicalcells pages 1-2): Théo Ribierre, Alexandre Bacq, Florian Donneger, Marion Doladilhe, Marina Maletic, Delphine Roussel, Isabelle Le Roux, Francine Chassoux, Bertrand Devaux, Homa Adle-Biassette, Sarah Ferrand-Sorbets, Georg Dorfmüller, Mathilde Chipaux, Sara Baldassari, Jean-Christophe Poncer, and Stéphanie Baulac. Targeting pathological cells with senolytic drugs reduces seizures in neurodevelopmental mtor-related epilepsy. Nature Neuroscience, 27:1125-1136, May 2024. URL: https://doi.org/10.1038/s41593-024-01634-2, doi:10.1038/s41593-024-01634-2. This article has 35 citations and is from a highest quality peer-reviewed journal.

6. (zheng2024voltagegatedpotassiumchannels pages 1-2): Yiting Zheng and Jing Chen. Voltage-gated potassium channels and genetic epilepsy. Frontiers in Neurology, Oct 2024. URL: https://doi.org/10.3389/fneur.2024.1466075, doi:10.3389/fneur.2024.1466075. This article has 22 citations and is from a peer-reviewed journal.

7. (sanz2024neuroinflammationandepilepsy pages 1-2): Pascual Sanz, Teresa Rubio, and Maria Adelaida Garcia-Gimeno. Neuroinflammation and epilepsy: from pathophysiology to therapies based on repurposing drugs. International Journal of Molecular Sciences, 25:4161, Apr 2024. URL: https://doi.org/10.3390/ijms25084161, doi:10.3390/ijms25084161. This article has 62 citations and is from a poor quality or predatory journal.

8. (nguyen2024themtorpathway pages 1-2): Lena H Nguyen, Youfen Xu, Maanasi Nair, and Angelique Bordey. The mtor pathway genes mtor, rheb, depdc5, pten, and tsc1 have convergent and divergent impacts on cortical neuron development and function. eLife, Feb 2024. URL: https://doi.org/10.7554/elife.91010.3, doi:10.7554/elife.91010.3. This article has 33 citations and is from a domain leading peer-reviewed journal.

9. (yuskaitis2019chronicmtorc1inhibition pages 2-3): Christopher J Yuskaitis, Leigh-Ana Rossitto, Sarika Gurnani, Elizabeth Bainbridge, Annapurna Poduri, and Mustafa Sahin. Chronic mtorc1 inhibition rescues behavioral and biochemical deficits resulting from neuronal depdc5 loss in mice. Human molecular genetics, 28:2952-2964, May 2019. URL: https://doi.org/10.1093/hmg/ddz123, doi:10.1093/hmg/ddz123. This article has 58 citations and is from a domain leading peer-reviewed journal.

10. (shariff2024advancesinunderstanding pages 5-6): Sanobar Shariff, Halah A. Nouh, Samuel Inshutiyimana, Charbel Kachouh, Maya M. Abdelwahab, Abubakar Nazir, Magda Wojtara, and Olivier Uwishema. Advances in understanding the pathogenesis of epilepsy: unraveling the molecular mechanisms: a cross‐sectional study. Health Science Reports, Feb 2024. URL: https://doi.org/10.1002/hsr2.1896, doi:10.1002/hsr2.1896. This article has 21 citations and is from a peer-reviewed journal.

11. (shariff2024advancesinunderstanding pages 4-5): Sanobar Shariff, Halah A. Nouh, Samuel Inshutiyimana, Charbel Kachouh, Maya M. Abdelwahab, Abubakar Nazir, Magda Wojtara, and Olivier Uwishema. Advances in understanding the pathogenesis of epilepsy: unraveling the molecular mechanisms: a cross‐sectional study. Health Science Reports, Feb 2024. URL: https://doi.org/10.1002/hsr2.1896, doi:10.1002/hsr2.1896. This article has 21 citations and is from a peer-reviewed journal.

12. (li2025progressingenetic pages 3-4): Yang Li, Xiaojie Hu, Xueqing Chen, Yawei Cheng, Yanhong Jiang, and Xingchen Wang. Progress in genetic mechanisms and precise treatment of neurocutaneous syndrome-related epilepsy. Frontiers in Neurology, Sep 2025. URL: https://doi.org/10.3389/fneur.2025.1642299, doi:10.3389/fneur.2025.1642299. This article has 0 citations and is from a peer-reviewed journal.

13. (zhang2025dravetsyndromenovel pages 15-16): Guirui Zhang, Shupeng Huang, Mingzhen Wei, Yongmo Wu, Zhengyi Xie, and Jin Wang. Dravet syndrome: novel insights into scn1a-mediated epileptic neurodevelopmental disorders within the molecular diagnostic-therapeutic framework. Frontiers in Neuroscience, Jul 2025. URL: https://doi.org/10.3389/fnins.2025.1634718, doi:10.3389/fnins.2025.1634718. This article has 3 citations and is from a peer-reviewed journal.

14. (liu2024excitatoryneuronsand pages 1-3): Yingying Liu, Yinchao Li, Yaqian Zhang, Yubao Fang, Lei Lei, Jiabin Yu, Hongping Tan, Lisen Sui, Qiang Guo, and Liemin Zhou. Excitatory neurons and oligodendrocyte precursor cells are vulnerable to focal cortical dysplasia type iiia as suggested by single‐nucleus multiomics. Clinical and Translational Medicine, Oct 2024. URL: https://doi.org/10.1002/ctm2.70072, doi:10.1002/ctm2.70072. This article has 3 citations and is from a peer-reviewed journal.