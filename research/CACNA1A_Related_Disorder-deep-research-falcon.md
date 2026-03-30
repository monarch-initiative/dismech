---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-20T13:16:48.460568'
end_time: '2026-03-20T13:27:52.800430'
duration_seconds: 664.34
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CACNA1A-Related Disorder
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** CACNA1A-Related Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **CACNA1A-Related Disorder**.
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
- **Disease Name:** CACNA1A-Related Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **CACNA1A-Related Disorder**.
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


## Comprehensive Research Report: Pathophysiology of **CACNA1A-Related Disorder** (Mendelian)

### Scope and nomenclature
“CACNA1A-related disorder” is an umbrella term for a spectrum of allelic neurologic channelopathies caused by pathogenic variants in **CACNA1A**, including (classically) **episodic ataxia type 2 (EA2)**, **familial/sporadic hemiplegic migraine type 1 (FHM1/SHM1)**, **developmental and epileptic encephalopathy (DEE42)** and broader neurodevelopmental disorders (NDD), and **spinocerebellar ataxia type 6 (SCA6; polyQ expansion)** (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4, indelicato2023cacna1arelatedchannelopathiesclinical pages 4-7, indelicato2023cacna1arelatedchannelopathiesclinical pages 7-9).

**Key definition (molecular):** CACNA1A encodes the pore-forming **α1A** subunit of the **P/Q-type (CaV2.1)** voltage-gated calcium channel (VGCC) (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4).

**Primary functional concept:** At presynaptic terminals, depolarization opens CaV2.1 channels, permitting Ca2+ influx that “**triggers the vesicular neurotransmitter release**”; CaV2.1 Ca2+ currents also influence “**the gating of K+ channels, transcriptional activity as well as intracellular signalling pathways**” (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4).

**Key recent 2023–2024 reviews and translational perspectives** include Indelicato & Boesch (2023; https://doi.org/10.1007/164_2022_625) (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4), Szymanowicz et al. (May 2024; https://doi.org/10.3390/diseases12050090) (szymanowicz2024areviewof pages 8-9), and Fox et al. (Jan 2024; https://doi.org/10.1177/26330040241245725) (fox2024developingapathway pages 1-2).

---

## 1) Core pathophysiology (molecular → cellular → systems)

### 1.1 Presynaptic calcium entry and synaptic transmission dysfunction
Across the CACNA1A spectrum, a unifying mechanism is disturbed CaV2.1-dependent presynaptic Ca2+ entry that perturbs neurotransmitter release and circuit stability (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4, kessi2023thegenotype–phenotypecorrelations pages 1-2). CaV2.1 is described as abundant in cerebellar circuitry (notably Purkinje and granule layers) and present across multiple forebrain structures; one review explicitly places CaV2.1 in presynaptic regions of **cortex, thalamus, hypothalamus, hippocampus, and cerebellum** (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4, szymanowicz2024areviewof pages 3-4, fox2024developingapathway pages 2-3).

### 1.2 Gain-of-function (GOF) vs loss-of-function (LOF) as a central organizing principle
A major current framework stratifies CACNA1A variants by net electrophysiologic effect:

- **FHM1/SHM1** is typically driven by **GOF missense** variants that increase CaV2.1 opening and presynaptic Ca2+ influx, enhancing glutamatergic transmission and shifting excitation/inhibition balance (szymanowicz2024areviewof pages 8-9).
- **EA2** is typically driven by **LOF** variants (often truncating or deletions) that reduce channel function and impair cerebellar signaling (szymanowicz2024areviewof pages 11-12, indelicato2023cacna1arelatedchannelopathiesclinical pages 4-7).
- **DEE/NDD** can result from both GOF and LOF missense variants, including trafficking-dominant-negative LOF variants, with genotype–phenotype correlations emerging (kessi2023thegenotype–phenotypecorrelations pages 1-2, fox2024developingapathway pages 3-5).
- **SCA6** is caused by a **C-terminal polyglutamine (CAG) expansion** in CACNA1A and shows prominent degenerative pathology with additional downstream bioenergetic/mitochondrial contributions (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4, leung2024mitochondrialdamageand pages 1-2).

### 1.3 Migraine pathophysiology: cortical spreading depression (CSD)
Recent syntheses link CaV2.1 GOF to CSD propensity via enhanced presynaptic Ca2+ influx at active zones and increased glutamate release. Szymanowicz et al. (2024) describe FHM1-associated changes such as activation at more negative potentials and prolonged open times, increasing calcium influx in presynaptic terminals/active zones and promoting “elevated glutamate release,” such that “**The increase in excitatory synaptic activity leads to cortical spreading depression (CSD)**” (https://doi.org/10.3390/diseases12050090) (szymanowicz2024areviewof pages 8-9). Indelicato & Boesch (2023) similarly state that FHM1 GOF mutations increase Ca2+ currents and “**facilitate a cascade of events that results in cortical spreading depression**” (https://doi.org/10.1007/164_2022_625) (indelicato2023cacna1arelatedchannelopathiesclinical pages 4-7).

### 1.4 Epilepsy/DEE pathophysiology: thalamocortical and inhibitory circuit failure
Fox et al. (2024) emphasize that Cav2.1 is “**crucial for fast synaptic neurotransmission**” and link absence epilepsy mechanisms to thalamocortical circuitry disturbances including “**reduced synaptic release from layer VI pyramidal neurons projecting to the thalamus**,” “**increased thalamic excitability**,” and “enhanced cortical and limbic excitability due to failure of synaptic release from GABAergic interneurons” (https://doi.org/10.1177/26330040241245725) (fox2024developingapathway pages 1-2, fox2024developingapathway pages 3-5). This places CACNA1A disease mechanisms at the intersection of excitatory drive, thalamic bursting, and impaired inhibition.

### 1.5 SCA6 degeneration and organelle stress: mitochondria and impaired mitophagy as progression modifiers
A major 2024 advance is a disease-stage-resolved, mechanism-focused study of SCA6 showing that transcriptomic mitochondrial signatures precede physiological decline, and that impaired mitochondrial quality control emerges with progression.

Leung et al. (Acta Neuropathologica, Jan 2024; https://doi.org/10.1007/s00401-023-02680-z) report that at disease onset “**changes in mitochondrial structure preceded changes in function**,” with mitochondrial membrane potential “normal at disease onset but impaired later during disease progression” (leung2024mitochondrialdamageand pages 1-2). They further report increasing oxidative stress later in disease (“**increase in oxidative stress in cerebellar Purkinje cells at later disease stages although not at disease onset**”) and evidence of impaired mitophagy (“**a reduction of markers of both autophagosomes and mitophagosomes**”), concluding a “progressive reduction in mitophagy” that likely exacerbates mitochondrial dysfunction (leung2024mitochondrialdamageand pages 1-2). Importantly, pathology was not restricted to Purkinje cells (“not limited to cerebellar Purkinje cells but … also observed in molecular layer interneurons”) (leung2024mitochondrialdamageand pages 1-2).

---

## 2) Key molecular players, pathways, cell types, and anatomy

### 2.1 Genes/proteins (HGNC/UniProt-style annotations)
- **CACNA1A** (HGNC: “calcium voltage-gated channel subunit alpha1 A”; protein: CaV2.1 α1A pore-forming subunit) (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4, fox2024developingapathway pages 2-3).
- **α1ACT**: Kessi et al. note CACNA1A also encodes **α1ACT**, described as a transcription factor, supporting gene-regulatory contributions beyond ion flux (kessi2023thegenotype–phenotypecorrelations pages 1-2).

### 2.2 Dysregulated molecular pathways / cellular processes (GO-oriented)
Evidence-supported disrupted processes include:
- **Voltage-gated calcium channel activity** / depolarization-induced Ca2+ influx (szymanowicz2024areviewof pages 3-4).
- **Synaptic vesicle exocytosis / neurotransmitter release** (direct quote: “triggers the vesicular neurotransmitter release”) (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4).
- **Chemical synaptic transmission** and **synaptic plasticity** (szymanowicz2024areviewof pages 3-4, kessi2023thegenotype–phenotypecorrelations pages 1-2).
- **Regulation of membrane potential / neuronal excitability**, including E/I imbalance favoring excitation in migraine models (szymanowicz2024areviewof pages 8-9).
- **Regulation of gene expression/transcription** and **intracellular signaling pathways** (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4, fox2024developingapathway pages 2-3).
- For SCA6 progression: **mitochondrial organization and function**, **oxidative stress response**, **autophagy/mitophagy** (supported by downregulated mitochondrial GO terms and mitophagy marker reductions) (leung2024mitochondrialdamageand pages 1-2, leung2024mitochondrialdamageand pages 5-8).

### 2.3 Cell types (CL-oriented)
Primary implicated cell types (with strongest direct evidence in retrieved sources):
- **Cerebellar Purkinje cell** (key expression site; key degenerative cell type in SCA6 mitochondrial/oxidative stress findings) (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4, leung2024mitochondrialdamageand pages 1-2).
- **Cerebellar granule cell / granule layer neurons** (high expression emphasized in review) (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4).
- **Corticothalamic layer VI pyramidal neurons** (absence epilepsy mechanism via reduced synaptic release to thalamus) (fox2024developingapathway pages 3-5).
- **GABAergic interneurons** (failure of inhibitory synaptic release contributing to hyperexcitability) (fox2024developingapathway pages 3-5).
- **Molecular layer interneurons** (SCA6 progression: oxidative stress/mitochondrial dysfunction not limited to Purkinje cells) (leung2024mitochondrialdamageand pages 1-2).

### 2.4 Anatomical locations (UBERON-oriented)
- **Cerebellum** (including vermis); CACNA1A enrichment and cerebellar phenotypes across EA2/SCA6/NDD (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4, szymanowicz2024areviewof pages 15-16).
- **Cerebral cortex, hippocampus, thalamus, striatum** (broad expression and presynaptic localization used to explain epilepsy/migraine and cognitive/psychiatric features) (szymanowicz2024areviewof pages 3-4, fox2024developingapathway pages 2-3).

### 2.5 Chemical entities (CHEBI-oriented; clinically relevant)
- **Acetazolamide** (carbonic anhydrase inhibitor; classic EA2 prophylaxis; also used broadly across episodic CACNA1A symptoms) (szymanowicz2024areviewof pages 11-12, muth2021fampridineandacetazolamide pages 1-2).
- **Fampridine / 4-aminopyridine (4-AP)** (K+ channel blocker; used for EA2 and related episodic symptoms; supported by RCT evidence) (muth2021fampridineandacetazolamide pages 1-2).
- **Flunarizine, topiramate** (used as interval prophylaxis in natural history cohort) (indelicato2024naturalhistoryof pages 1-2).
- **Galcanezumab** (anti-CGRP monoclonal antibody; reported in a patient with therapy-resistant hemiplegic migraine) (indelicato2024naturalhistoryof pages 1-2).

---

## 3) Cellular components (subcellular localization)

The best-supported subcellular localization across sources is **presynaptic**:
- Indelicato & Boesch (2023) explicitly localize function to the “presynaptic terminal,” where Ca2+ entry triggers vesicular neurotransmitter release (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4).
- Szymanowicz et al. (2024) describe presynaptic “active zones of nerve endings” and increased presynaptic terminal Ca2+ influx in FHM1 GOF contexts (szymanowicz2024areviewof pages 8-9).

For SCA6 progression, implicated compartments include:
- **Mitochondria** (structure/function decline over time) (leung2024mitochondrialdamageand pages 1-2).
- **Autophagosome/mitophagosome–lysosome pathway** (marker reductions consistent with impaired mitophagy) (leung2024mitochondrialdamageand pages 1-2).

---

## 4) Disease progression model (sequence of events)

A unifying model can be expressed as a **variant class → circuit dysfunction → clinical phenotype** framework, with additional **progressive organelle stress** in degenerative SCA6:

1. **Primary trigger:** pathogenic CACNA1A variant causes altered CaV2.1 channel biophysics/abundance (LOF, GOF, or polyQ). (indelicato2023cacna1arelatedchannelopathiesclinical pages 4-7, indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4)
2. **Immediate cellular consequence:** altered depolarization-evoked presynaptic Ca2+ influx (szymanowicz2024areviewof pages 3-4) changes neurotransmitter release (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4) and network excitability.
3. **Circuit-level consequence:**
   - Migraine: increased excitatory synaptic transmission and CSD susceptibility (szymanowicz2024areviewof pages 8-9).
   - Epilepsy: thalamocortical release failure and inhibitory interneuron release failure → thalamic hyperexcitability and generalized seizure propensity (fox2024developingapathway pages 3-5).
   - Ataxia: cerebellar microcircuit dysfunction (Purkinje/granule), producing episodic/chronic cerebellar syndrome (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4, szymanowicz2024areviewof pages 11-12).
4. **Progression/degeneration (especially SCA6):** mitochondrial gene expression changes at onset, then later decline in mitochondrial membrane potential, rising oxidative stress, and impaired mitophagy that may accelerate late-stage cellular failure (leung2024mitochondrialdamageand pages 1-2, leung2024mitochondrialdamageand pages 5-8).

---

## 5) Phenotypic manifestations (HP-oriented), linked to mechanisms

**Core phenotypes** across the CACNA1A spectrum include:
- **Episodic ataxia / vertigo** (EA2), chronic gait ataxia, nystagmus, dysarthria—consistent with cerebellar circuit dysfunction (indelicato2024naturalhistoryof pages 2-4).
- **Hemiplegic migraine** (FHM1/SHM1), with aura and severe attacks consistent with GOF-driven CSD susceptibility (indelicato2023cacna1arelatedchannelopathiesclinical pages 4-7, szymanowicz2024areviewof pages 8-9).
- **Epilepsy and DEE**: febrile-triggered status epilepticus and seizure heterogeneity reflecting thalamocortical/interneuron release failures and variant-specific gating/trafficking changes (indelicato2023cacna1arelatedchannelopathiesclinical pages 7-9, fox2024developingapathway pages 3-5).
- **Neurodevelopmental delay/intellectual disability/autism spectrum** in subsets, consistent with widespread circuit dysfunction and gene-regulatory roles (kessi2023thegenotype–phenotypecorrelations pages 1-2, fox2024developingapathway pages 2-3).

**Quantitative epilepsy/NDD statistics (systematic aggregation through Feb 2023):** Kessi et al. compiled 130 epilepsy patients (83 variants) and found status epilepticus (n=64) as the most common manifestation; 57.80% (67/116 with seizure outcome data) remained refractory and 42.20% (49/116) had controlled seizures (https://doi.org/10.3389/fnmol.2023.1222321) (kessi2023thegenotype–phenotypecorrelations pages 1-2).

---

## 6) Recent developments (2023–2024) and “latest research” highlights

### 6.1 Precision phenotyping and genotype–phenotype correlations
A key 2023 step is the explicit linking of GOF vs LOF to distinct neurodevelopmental and epilepsy outcomes: GOF variants associate with severe–profound GDD/ID and status epilepticus; LOF variants associate with milder GDD/ID and absence seizures, and variant topography (S4–S6) correlates with status epilepticus (kessi2023thegenotype–phenotypecorrelations pages 1-2).

### 6.2 Trial-readiness infrastructure (real-world implementation of translational pipelines)
Fox et al. (2024) quantify the variant interpretation problem (“almost 1700 CACNA1A variants… reported in ClinVar, with over 400… Pathogenic or Likely Pathogenic, but with limited-to-no clinical or functional data”) and emphasize unmet need (“over half of CACNA1A-related epilepsies are refractory to current therapies”) (fox2024developingapathway pages 1-2). They describe real-world implementation of a translational ecosystem: patient-derived iPSCs, multiple animal models, natural history studies, and a global research network >60 scientists/clinicians (fox2024developingapathway pages 1-2, fox2024developingapathway pages 5-7).

### 6.3 Mechanistic progression biology in SCA6
Leung et al. (2024) provide a stage-specific mechanistic map in SCA6 linking early transcriptomic mitochondrial signatures with later oxidative stress and mitophagy impairment, motivating mitochondria/autophagy pathways as therapeutic target axes, particularly later in disease (leung2024mitochondrialdamageand pages 1-2, leung2024mitochondrialdamageand pages 5-8).

---

## 7) Current applications and real-world implementations

### 7.1 Symptom-targeted pharmacotherapy (implemented clinically)
**EA2 treatment evidence (randomized Phase III crossover RCT):** Muth et al. (Neurology Clinical Practice, Aug 2021; https://doi.org/10.1212/cpj.0000000000001017) randomized 30 EA2 patients to fampridine, acetazolamide, and placebo in a double-blind, double-dummy crossover. Compared with placebo, **fampridine reduced attacks to 63% (95% CI 54–74%)** and **acetazolamide to 52% (95% CI 46–60%)**; fampridine had fewer side effects than acetazolamide (muth2021fampridineandacetazolamide pages 1-2). This remains one of the highest-quality quantitative treatment datasets for episodic CACNA1A symptoms.

**Natural history cohort implementation (2004–2024, Austria):** In a prospective single-center cohort of 41 subjects with non-polyQ CACNA1A variants (Journal of Neurology, Aug 2024; https://doi.org/10.1007/s00415-024-12602-y), 66% (27/41) used interval prophylaxis (acetazolamide, flunarizine, 4-aminopyridine, topiramate), reported as efficacious at reducing episodic symptom burden; a single older patient’s resistant hemiplegic migraine improved with **galcanezumab** (migraine days 4→1/month) (indelicato2024naturalhistoryof pages 1-2).

### 7.2 Diagnostics and monitoring
- **Genetic diagnostics**: reviews emphasize broad CACNA1A phenotypes spanning paroxysmal and chronic features; this supports use of exome/panel testing beyond “classic” EA2/FHM1 presentations (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4).
- **Natural history datasets**: the Austrian cohort provides granular symptom frequencies and age-at-onset patterns, useful for endpoint selection and counseling (indelicato2024naturalhistoryof pages 2-4). Visual summaries appear in the paper’s Table/Figure (indelicato2024naturalhistoryof media 9fb4e801, indelicato2024naturalhistoryof media 5d2f1b14, indelicato2024naturalhistoryof media cc87ae80).

---

## 8) Relevant statistics and data (recent cohorts)

### 8.1 2024 Austrian non-polyQ CACNA1A natural history cohort
Indelicato et al. (Aug 2024; https://doi.org/10.1007/s00415-024-12602-y) report:
- **n=41** genetically confirmed non-polyQ CACNA1A; **93% familial**; mean age at first exam 35±22 years (indelicato2024naturalhistoryof pages 1-2).
- **Onset in childhood/adolescence:** 31/41 (76%) (indelicato2024naturalhistoryof pages 1-2).
- **Initial manifestation:** episodic symptoms 32/41 (78%); developmental delay 9/41 (22%) (indelicato2024naturalhistoryof pages 1-2).
- **Chronic cerebellar syndrome:** 35/41 (85%) (indelicato2024naturalhistoryof pages 1-2).
- **Cerebellar atrophy:** 30/36 imaged (83%) (indelicato2024naturalhistoryof pages 2-4).
- Episodic symptom examples and frequencies include speech disturbance 28/40 (70%), gait instability 25/40 (63%), headache 25/40 (63%) (indelicato2024naturalhistoryof pages 2-4).

These distributions are also summarized visually in the paper’s table/figure extracts (indelicato2024naturalhistoryof media 9fb4e801, indelicato2024naturalhistoryof media cc87ae80).

### 8.2 2023 systematic aggregation for CACNA1A-related neurodevelopmental phenotypes
Kessi et al. (Jul 2023; https://doi.org/10.3389/fnmol.2023.1222321) report:
- ~187 individuals with GDD/ID (123 variants); GOF variants correlate with severe–profound GDD/ID (p=0.001) (kessi2023thegenotype–phenotypecorrelations pages 1-2).
- Among epilepsy cases with reported outcomes, **57.80% refractory** (67/116) (kessi2023thegenotype–phenotypecorrelations pages 1-2).

---

## 9) Expert opinions and analysis (authoritative perspectives)

- **Mechanism-to-therapy framing (channelopathy):** Indelicato & Boesch (2023) frame CACNA1A disorders as “channelopathies” with genotype-dependent effects (GOF vs LOF vs polyQ), explicitly tying CaV2.1 presynaptic Ca2+ entry to neurotransmitter release and intracellular signaling, and linking GOF to CSD (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4, indelicato2023cacna1arelatedchannelopathiesclinical pages 4-7).
- **Translational gap assessment:** Fox et al. (2024) argue that despite a large ClinVar variant space and high refractory epilepsy burden, “current therapies… are primarily symptomatic and do not target disease-specific mechanisms,” motivating genotype-stratified development and clinical trial readiness (fox2024developingapathway pages 2-3).
- **Progression biology insight:** Leung et al. (2024) conclude that mitochondrial dysfunction and impaired mitochondrial degradation likely contribute to progression in SCA6, which is a shift from purely channel-centric models toward combined channel/organellar stress models for late disease stages (leung2024mitochondrialdamageand pages 1-2).

---

## Knowledge-base-ready structured annotations

### A) Pathophysiology description (narrative)
CACNA1A-related disorders arise from pathogenic variants in CACNA1A, which encodes the presynaptic P/Q-type CaV2.1 calcium channel α1A subunit. CaV2.1-mediated Ca2+ influx at presynaptic terminals triggers vesicular neurotransmitter release and influences potassium channel gating, transcription, and intracellular signaling. Variant class determines net excitability: GOF variants enhance presynaptic Ca2+ entry and excitatory transmission, promoting CSD and hemiplegic migraine; LOF variants reduce CaV2.1 function, predisposing to episodic cerebellar dysfunction (EA2) and certain seizure phenotypes (e.g., absence). In DEE/NDD, both GOF and LOF disrupt thalamocortical and inhibitory circuits, producing seizure refractoriness and developmental impairment. In SCA6, a C-terminal polyQ expansion is associated with Purkinje-centered degeneration, where early mitochondrial transcriptomic changes precede later mitochondrial functional decline, oxidative stress, and impaired mitophagy that likely contribute to disease progression.

### B) Gene/protein annotations (example GO mappings; names provided for GO curation)
- CACNA1A / CaV2.1: **voltage-gated calcium channel activity**, **presynaptic calcium ion influx**, **synaptic vesicle exocytosis**, **chemical synaptic transmission**, **synaptic plasticity**, **regulation of membrane potential/neuronal excitability**, **transcription/gene regulation** (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4, kessi2023thegenotype–phenotypecorrelations pages 1-2, fox2024developingapathway pages 2-3).
- SCA6 progression modifiers: **mitochondrial organization**, **mitochondrial membrane potential**, **reactive oxygen species/oxidative stress response**, **mitophagy/autophagy** (leung2024mitochondrialdamageand pages 1-2, leung2024mitochondrialdamageand pages 5-8).

### C) Cell type involvement (CL term suggestions)
- Purkinje cell; granule cell; cortical pyramidal neuron (layer VI corticothalamic); GABAergic interneuron; thalamic relay neuron; cerebellar molecular layer interneuron (leung2024mitochondrialdamageand pages 1-2, fox2024developingapathway pages 3-5, indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4).

### D) Anatomical locations (UBERON term suggestions)
- Cerebellum (incl. vermis), cerebral cortex, hippocampus, thalamus, striatum (szymanowicz2024areviewof pages 3-4, fox2024developingapathway pages 2-3, szymanowicz2024areviewof pages 15-16).

### E) Chemical entities (CHEBI term suggestions)
- Acetazolamide; 4-aminopyridine/fampridine; flunarizine; topiramate; galcanezumab (muth2021fampridineandacetazolamide pages 1-2, indelicato2024naturalhistoryof pages 1-2).

### F) Evidence items (with identifiers present in retrieved sources)
- Indelicato & Boesch. *CACNA1A-Related Channelopathies: Clinical Manifestations and Treatment Options* (Jan 2023). DOI/URL: https://doi.org/10.1007/164_2022_625 (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4).
- Fox et al. *Developing a pathway to clinical trials for CACNA1A-related epilepsies* (Jan 2024). DOI/URL: https://doi.org/10.1177/26330040241245725 (fox2024developingapathway pages 1-2).
- Indelicato et al. *Natural history of non-polyglutamine CACNA1A disease in Austria* (Aug 2024). DOI/URL: https://doi.org/10.1007/s00415-024-12602-y (indelicato2024naturalhistoryof pages 1-2).
- Leung et al. *Mitochondrial damage and impaired mitophagy contribute to disease progression in SCA6* (Jan 2024). DOI/URL: https://doi.org/10.1007/s00401-023-02680-z (leung2024mitochondrialdamageand pages 1-2).

**Note on PMID availability:** Several mechanistic summaries in the retrieved 2023–2024 sources do not display PMIDs in the provided excerpts; therefore, this report cites DOIs/URLs for those sources. Where PMIDs are required for downstream curation, the DOI-cited papers can be used as index sources to backfill PMIDs from PubMed.

---

## Summary table (mechanism-centric)
| Phenotype group | Typical variant class | Core mechanism | Key affected cells/tissues | Key citations with DOI and quoted phrases |
|---|---|---|---|---|
| EA2 | Usually **loss-of-function** variants, especially truncating/nonsense/frameshift/deletions; reduced CaV2.1/P/Q-channel activity | Reduced presynaptic **Ca2+ influx** impairs vesicular neurotransmitter release and cerebellar signaling; chronic cerebellar dysfunction likely reflects impaired Purkinje-cell pacemaking/network output. Review evidence states P/Q-channel activation “**triggers the vesicular neurotransmitter release**,” and EA2 “**typically arises from loss-of-function**” CACNA1A variants. | **Purkinje cells**, **granule cells**; cerebellar cortex/vermian circuitry; broader CNS presynaptic terminals | Indelicato & Boesch 2023, *Handb Exp Pharmacol*, DOI: https://doi.org/10.1007/164_2022_625 — “**triggers the vesicular neurotransmitter release**” and EA2 linked to LOF variants (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4, indelicato2023cacna1arelatedchannelopathiesclinical pages 4-7); Szymanowicz et al. 2024, *Diseases*, DOI: https://doi.org/10.3390/diseases12050090 — EA2 “**typically arises from loss-of-function**” and CaV2.1 is highly expressed in Purkinje/granule neurons (szymanowicz2024areviewof pages 11-12) |
| FHM1 / SHM1 | Predominantly **gain-of-function missense** variants (classic examples include **R192Q, T666M, S218L**) | Increased channel opening probability / activation at more negative potentials / prolonged open time increases presynaptic **Ca2+ influx**, promotes excess **glutamate release**, shifts excitation over inhibition, and lowers threshold for **cortical spreading depression (CSD)**. Review evidence: GOF changes “**facilitate a cascade of events that results in cortical spreading depression**.” | Cerebral **cortex**, presynaptic excitatory terminals, cortical interneuron/excitatory balance networks; cerebellum may also be involved in overlap phenotypes | Szymanowicz et al. 2024, *Diseases*, DOI: https://doi.org/10.3390/diseases12050090 — FHM1 variants increase opening probability/negative activation and promote glutamate release/CSD (szymanowicz2024areviewof pages 8-9, szymanowicz2024areviewof pages 3-4); Indelicato & Boesch 2023, DOI: https://doi.org/10.1007/164_2022_625 — FHM1 due to missense GOF mutations that “**facilitate a cascade of events that results in cortical spreading depression**” (indelicato2023cacna1arelatedchannelopathiesclinical pages 4-7); Schaare et al. 2023, *Genes*, DOI: https://doi.org/10.3390/genes14020400 — GOF variants may increase hyperexcitability and lower the threshold for CSD (schaare2023concomitantcalciumchannelopathies pages 2-3) |
| DEE / NDD | Both **GOF and LOF missense** variants; some severe cases from dominant-negative trafficking-defective LOF; rare **biallelic LOF** can cause very severe early-onset DEE | Disrupted CaV2.1-dependent synaptic transmission and neuronal excitability; disease mechanisms include **reduced synaptic release** in corticothalamic pathways, **increased thalamic excitability**, failure of GABAergic inhibitory release, and broader disturbance of network synchronization/neurodevelopment. GOF tends to associate with more severe GDD/ID and status epilepticus; LOF more with absence seizures. | **Corticothalamic layer VI pyramidal neurons**, **thalamic relay circuits**, **GABAergic interneurons**, cortex/hippocampus/cerebellum; developing neuronal networks | Kessi et al. 2023, *Front Mol Neurosci*, DOI: https://doi.org/10.3389/fnmol.2023.1222321 — GOF associated with severe–profound GDD/ID and status epilepticus; LOF with milder GDD/ID and absence seizures (kessi2023thegenotype–phenotypecorrelations pages 1-2); Fox et al. 2024, *Ther Adv Rare Dis*, DOI: https://doi.org/10.1177/26330040241245725 — Cav2.1 is “**crucial for fast synaptic neurotransmission**”; mechanisms include “**reduced synaptic release from layer VI pyramidal neurons projecting to the thalamus**,” “**increased thalamic excitability**,” and impaired GABAergic release (fox2024developingapathway pages 1-2, fox2024developingapathway pages 2-3, fox2024developingapathway pages 3-5) |
| SCA6 | **C-terminal polyglutamine (CAG) expansion** in CACNA1A | Progressive cerebellar degeneration centered on **Purkinje-cell dysfunction**; early transcriptomic downregulation of mitochondrial pathways, then later decline in mitochondrial membrane potential, increased oxidative stress, and **impaired mitophagy**. Key conclusion: “**changes in mitochondrial structure preceded changes in function**” and “**mitochondrial dysfunction and impaired mitochondrial degradation likely contribute to disease progression in SCA6**.” | **Purkinje cells** primarily; also **molecular layer interneurons** and granule layer/cerebellar vermis; mitochondria/autophagosome-lysosome compartments | Indelicato & Boesch 2023, DOI: https://doi.org/10.1007/164_2022_625 — SCA6 genotype is a CAG polyglutamine expansion in CACNA1A (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4); Leung et al. 2024, *Acta Neuropathologica*, DOI: https://doi.org/10.1007/s00401-023-02680-z — “**changes in mitochondrial structure preceded changes in function**,” oxidative stress rises later, and “**mitochondrial dysfunction and impaired mitochondrial degradation likely contribute to disease progression in SCA6**” (leung2024mitochondrialdamageand pages 1-2, leung2024pathologicalchangesin pages 32-36, leung2024pathologicalchangesin pages 49-53, leung2024mitochondrialdamageand pages 5-8) |


*Table: This table summarizes the main CACNA1A-related phenotype groups, their usual variant classes, core molecular/cellular mechanisms, and the principal affected cells and tissues. It is useful as a compact knowledge-base-ready overview linking genotype class to disease mechanism with source-backed citations.*

---

## Visual evidence (recent cohort phenotype frequencies)
The Austrian natural history cohort’s individual therapy exposures and phenotype frequency distributions are summarized in the extracted Table/Figure images (indelicato2024naturalhistoryof media 9fb4e801, indelicato2024naturalhistoryof media cc87ae80).


References

1. (indelicato2023cacna1arelatedchannelopathiesclinical pages 1-4): Elisabetta Indelicato and Sylvia Boesch. Cacna1a-related channelopathies: clinical manifestations and treatment options. Handbook of experimental pharmacology, pages 227-248, Jan 2023. URL: https://doi.org/10.1007/164\_2022\_625, doi:10.1007/164\_2022\_625. This article has 24 citations and is from a peer-reviewed journal.

2. (indelicato2023cacna1arelatedchannelopathiesclinical pages 4-7): Elisabetta Indelicato and Sylvia Boesch. Cacna1a-related channelopathies: clinical manifestations and treatment options. Handbook of experimental pharmacology, pages 227-248, Jan 2023. URL: https://doi.org/10.1007/164\_2022\_625, doi:10.1007/164\_2022\_625. This article has 24 citations and is from a peer-reviewed journal.

3. (indelicato2023cacna1arelatedchannelopathiesclinical pages 7-9): Elisabetta Indelicato and Sylvia Boesch. Cacna1a-related channelopathies: clinical manifestations and treatment options. Handbook of experimental pharmacology, pages 227-248, Jan 2023. URL: https://doi.org/10.1007/164\_2022\_625, doi:10.1007/164\_2022\_625. This article has 24 citations and is from a peer-reviewed journal.

4. (szymanowicz2024areviewof pages 8-9): Oliwia Szymanowicz, Artur Drużdż, Bartosz Słowikowski, Sandra Pawlak, Ewelina Potocka, Ulyana Goutor, Mateusz Konieczny, Małgorzata Ciastoń, Aleksandra Lewandowska, Paweł P. Jagodziński, Wojciech Kozubski, and Jolanta Dorszewska. A review of the cacna gene family: its role in neurological disorders. Diseases, 12:90, May 2024. URL: https://doi.org/10.3390/diseases12050090, doi:10.3390/diseases12050090. This article has 53 citations.

5. (fox2024developingapathway pages 1-2): Pangkong M. Fox, Sunitha Malepati, Lisa Manaster, Elsa Rossignol, and Jeffrey L. Noebels. Developing a pathway to clinical trials for cacna1a-related epilepsies: a patient organization perspective. Therapeutic Advances in Rare Disease, Jan 2024. URL: https://doi.org/10.1177/26330040241245725, doi:10.1177/26330040241245725. This article has 10 citations.

6. (kessi2023thegenotype–phenotypecorrelations pages 1-2): Miriam Kessi, Baiyu Chen, Nan Pang, Lifen Yang, Jing Peng, Fang He, and Fei Yin. The genotype–phenotype correlations of the cacna1a-related neurodevelopmental disorders: a small case series and literature reviews. Frontiers in Molecular Neuroscience, Jul 2023. URL: https://doi.org/10.3389/fnmol.2023.1222321, doi:10.3389/fnmol.2023.1222321. This article has 23 citations.

7. (szymanowicz2024areviewof pages 3-4): Oliwia Szymanowicz, Artur Drużdż, Bartosz Słowikowski, Sandra Pawlak, Ewelina Potocka, Ulyana Goutor, Mateusz Konieczny, Małgorzata Ciastoń, Aleksandra Lewandowska, Paweł P. Jagodziński, Wojciech Kozubski, and Jolanta Dorszewska. A review of the cacna gene family: its role in neurological disorders. Diseases, 12:90, May 2024. URL: https://doi.org/10.3390/diseases12050090, doi:10.3390/diseases12050090. This article has 53 citations.

8. (fox2024developingapathway pages 2-3): Pangkong M. Fox, Sunitha Malepati, Lisa Manaster, Elsa Rossignol, and Jeffrey L. Noebels. Developing a pathway to clinical trials for cacna1a-related epilepsies: a patient organization perspective. Therapeutic Advances in Rare Disease, Jan 2024. URL: https://doi.org/10.1177/26330040241245725, doi:10.1177/26330040241245725. This article has 10 citations.

9. (szymanowicz2024areviewof pages 11-12): Oliwia Szymanowicz, Artur Drużdż, Bartosz Słowikowski, Sandra Pawlak, Ewelina Potocka, Ulyana Goutor, Mateusz Konieczny, Małgorzata Ciastoń, Aleksandra Lewandowska, Paweł P. Jagodziński, Wojciech Kozubski, and Jolanta Dorszewska. A review of the cacna gene family: its role in neurological disorders. Diseases, 12:90, May 2024. URL: https://doi.org/10.3390/diseases12050090, doi:10.3390/diseases12050090. This article has 53 citations.

10. (fox2024developingapathway pages 3-5): Pangkong M. Fox, Sunitha Malepati, Lisa Manaster, Elsa Rossignol, and Jeffrey L. Noebels. Developing a pathway to clinical trials for cacna1a-related epilepsies: a patient organization perspective. Therapeutic Advances in Rare Disease, Jan 2024. URL: https://doi.org/10.1177/26330040241245725, doi:10.1177/26330040241245725. This article has 10 citations.

11. (leung2024mitochondrialdamageand pages 1-2): Tsz Chui Sophia Leung, Eviatar Fields, Namrata Rana, Ru Yi Louisa Shen, Alexandra E. Bernstein, Anna A. Cook, Daniel E. Phillips, and Alanna J. Watt. Mitochondrial damage and impaired mitophagy contribute to disease progression in sca6. Acta Neuropathologica, Jan 2024. URL: https://doi.org/10.1007/s00401-023-02680-z, doi:10.1007/s00401-023-02680-z. This article has 20 citations and is from a highest quality peer-reviewed journal.

12. (leung2024mitochondrialdamageand pages 5-8): Tsz Chui Sophia Leung, Eviatar Fields, Namrata Rana, Ru Yi Louisa Shen, Alexandra E. Bernstein, Anna A. Cook, Daniel E. Phillips, and Alanna J. Watt. Mitochondrial damage and impaired mitophagy contribute to disease progression in sca6. Acta Neuropathologica, Jan 2024. URL: https://doi.org/10.1007/s00401-023-02680-z, doi:10.1007/s00401-023-02680-z. This article has 20 citations and is from a highest quality peer-reviewed journal.

13. (szymanowicz2024areviewof pages 15-16): Oliwia Szymanowicz, Artur Drużdż, Bartosz Słowikowski, Sandra Pawlak, Ewelina Potocka, Ulyana Goutor, Mateusz Konieczny, Małgorzata Ciastoń, Aleksandra Lewandowska, Paweł P. Jagodziński, Wojciech Kozubski, and Jolanta Dorszewska. A review of the cacna gene family: its role in neurological disorders. Diseases, 12:90, May 2024. URL: https://doi.org/10.3390/diseases12050090, doi:10.3390/diseases12050090. This article has 53 citations.

14. (muth2021fampridineandacetazolamide pages 1-2): Carolin Muth, Julian Teufel, Ludger Schöls, Matthis Synofzik, Christiana Franke, Dagmar Timmann, Ulrich Mansmann, and Michael Strupp. Fampridine and acetazolamide in ea2 and related familial ea. Neurology Clinical Practice, Aug 2021. URL: https://doi.org/10.1212/cpj.0000000000001017, doi:10.1212/cpj.0000000000001017. This article has 52 citations.

15. (indelicato2024naturalhistoryof pages 1-2): Elisabetta Indelicato, Wolfgang Nachbauer, Matthias S. Amprosi, Sarah Maier, Iris Unterberger, Margarete Delazer, Katharina Kaltseis, Stefan Kiechl, Gregor Broessner, Matthias Baumann, and Sylvia Boesch. Natural history of non-polyglutamine cacna1a disease in austria. Journal of Neurology, 271:6618-6627, Aug 2024. URL: https://doi.org/10.1007/s00415-024-12602-y, doi:10.1007/s00415-024-12602-y. This article has 7 citations and is from a domain leading peer-reviewed journal.

16. (indelicato2024naturalhistoryof pages 2-4): Elisabetta Indelicato, Wolfgang Nachbauer, Matthias S. Amprosi, Sarah Maier, Iris Unterberger, Margarete Delazer, Katharina Kaltseis, Stefan Kiechl, Gregor Broessner, Matthias Baumann, and Sylvia Boesch. Natural history of non-polyglutamine cacna1a disease in austria. Journal of Neurology, 271:6618-6627, Aug 2024. URL: https://doi.org/10.1007/s00415-024-12602-y, doi:10.1007/s00415-024-12602-y. This article has 7 citations and is from a domain leading peer-reviewed journal.

17. (fox2024developingapathway pages 5-7): Pangkong M. Fox, Sunitha Malepati, Lisa Manaster, Elsa Rossignol, and Jeffrey L. Noebels. Developing a pathway to clinical trials for cacna1a-related epilepsies: a patient organization perspective. Therapeutic Advances in Rare Disease, Jan 2024. URL: https://doi.org/10.1177/26330040241245725, doi:10.1177/26330040241245725. This article has 10 citations.

18. (indelicato2024naturalhistoryof media 9fb4e801): Elisabetta Indelicato, Wolfgang Nachbauer, Matthias S. Amprosi, Sarah Maier, Iris Unterberger, Margarete Delazer, Katharina Kaltseis, Stefan Kiechl, Gregor Broessner, Matthias Baumann, and Sylvia Boesch. Natural history of non-polyglutamine cacna1a disease in austria. Journal of Neurology, 271:6618-6627, Aug 2024. URL: https://doi.org/10.1007/s00415-024-12602-y, doi:10.1007/s00415-024-12602-y. This article has 7 citations and is from a domain leading peer-reviewed journal.

19. (indelicato2024naturalhistoryof media 5d2f1b14): Elisabetta Indelicato, Wolfgang Nachbauer, Matthias S. Amprosi, Sarah Maier, Iris Unterberger, Margarete Delazer, Katharina Kaltseis, Stefan Kiechl, Gregor Broessner, Matthias Baumann, and Sylvia Boesch. Natural history of non-polyglutamine cacna1a disease in austria. Journal of Neurology, 271:6618-6627, Aug 2024. URL: https://doi.org/10.1007/s00415-024-12602-y, doi:10.1007/s00415-024-12602-y. This article has 7 citations and is from a domain leading peer-reviewed journal.

20. (indelicato2024naturalhistoryof media cc87ae80): Elisabetta Indelicato, Wolfgang Nachbauer, Matthias S. Amprosi, Sarah Maier, Iris Unterberger, Margarete Delazer, Katharina Kaltseis, Stefan Kiechl, Gregor Broessner, Matthias Baumann, and Sylvia Boesch. Natural history of non-polyglutamine cacna1a disease in austria. Journal of Neurology, 271:6618-6627, Aug 2024. URL: https://doi.org/10.1007/s00415-024-12602-y, doi:10.1007/s00415-024-12602-y. This article has 7 citations and is from a domain leading peer-reviewed journal.

21. (schaare2023concomitantcalciumchannelopathies pages 2-3): Donna Schaare, Sara M. Sarasua, Laina Lusk, Shridhar Parthasarathy, Liangjiang Wang, Ingo Helbig, and Luigi Boccuto. Concomitant calcium channelopathies involving cacna1a and cacna1f: a case report and review of the literature. Genes, 14:400, Feb 2023. URL: https://doi.org/10.3390/genes14020400, doi:10.3390/genes14020400. This article has 5 citations.

22. (leung2024pathologicalchangesin pages 32-36): TCS Leung. Pathological changes in the cerebellum of spinocerebellar ataxia type 6 (sca6): disease progression and selective vulnerability. Unknown journal, 2024.

23. (leung2024pathologicalchangesin pages 49-53): TCS Leung. Pathological changes in the cerebellum of spinocerebellar ataxia type 6 (sca6): disease progression and selective vulnerability. Unknown journal, 2024.