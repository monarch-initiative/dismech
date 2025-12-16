---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:13:26.457903'
end_time: '2025-12-15T09:18:46.084192'
duration_seconds: 319.63
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Jeavons Syndrome
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 14
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Jeavons Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Jeavons Syndrome**.
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
- **Disease Name:** Jeavons Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Jeavons Syndrome**.
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


# Disease Pathophysiology Research Template

## Target Disease
- Disease Name: Jeavons Syndrome (Epilepsy with Eyelid Myoclonia with Absences)
- MONDO ID: Not confirmed
- Category: Complex

## Pathophysiology description (current understanding)
Jeavons syndrome (JS), also termed epilepsy with eyelid myoclonia (EEM/EMA), is characterized by a reflex, visually triggered generalized epilepsy with a core electroclinical triad: eyelid myoclonia with absences, photosensitivity, and generalized epileptiform paroxysms specifically induced by eye closure and photic stimulation. Covanis summarizes: JS is defined by “eyelid myoclonia, absences/other generalized seizures, and EEG paroxysms… specifically induced by voluntary/on-command eye closure and by photosensitivity,” with events reliably evoked in light and absent in total darkness (URLs/DOIs below) (covanis2015jeavonssyndrome–updatedreview pages 1-2, covanis2015jeavonssyndrome–updatedreview pages 7-8). Vaudano et al. provide EEG–fMRI and morphometric evidence implicating occipital visual cortex and posterior thalamus (pulvinar) in eye-closure sensitivity (ECS), with increased BOLD responses to eye closure in visual cortex/pulvinar and gray-matter alterations in visual cortex and frontal eye fields (FEF), consistent with a network involving visual cortices, thalamus, and eye-movement control circuits (vaudano2014thevisualsystem pages 1-2).

Mechanistically, the initial trigger is voluntary/on-command slow eye closure in the presence of uninterrupted light; passive eye closure is not sufficient. Eye closure and intermittent photic stimulation (IPS) drive occipital cortical activation, rapidly generalizing via subcortical thalamo-cortical circuits to produce brief polyspike–wave or spike–wave discharges (≈3–6 Hz) and clinical eyelid myoclonia with behavioral arrest. Covanis notes the eye-closure trigger window “starts immediately after closing the eyes and only lasts up to 3 sec,” and paroxysms “do not occur in total darkness,” underscoring the necessity of light input and cortical visual processing (covanis2015jeavonssyndrome–updatedreview pages 7-8, covanis2015jeavonssyndrome–updatedreview pages 2-4). Vaudano et al. observed higher BOLD responses to eye closure in visual cortex and posterior thalamus and decreased gray matter in bilateral FEF, suggesting that voluntary eyelid closure engages FEF→occipital interactions that, in genetically predisposed brains, tip visual–thalamo-cortical networks into generalized discharges (vaudano2014thevisualsystem pages 1-2).

Genetically, JS is strongly predisposed but genetically heterogeneous. A 2021 literature review synthesizes candidate genes with EMA/JS phenotypes: SYNGAP1, NEXMIF/KIAA2022, RORB, and CHD2, with additional reports implicating SLC2A1, NAA10, and KCNB1 in EMA-like phenotypes; no single causative gene explains all cases (mayo2021candidategenesfor pages 1-2, mayo2021candidategenesfor pages 26-27). A 2025 case report proposes CSNK2B as a novel candidate based on a de novo variant in a child with primary eyelid myoclonia, with mechanistic discussion of CK2 signaling in neuronal development (he2025casereporta pages 3-7). Clinically, JS shows childhood onset (peak 6–8 years), female predominance, photosensitivity, and eye-closure–provoked generalized paroxysms; prevalence in idiopathic generalized epilepsies is reported around 7–13% in some series (tuac2017jeavonssyndrome12 pages 1-2).

| Domain | Item | Evidence Summary | Key Mechanistic Notes | Year | Source | DOI/URL | Citation ID |
|---|---|---|---|---|---|---|---|
| Clinical/Diagnostic | Diagnostic triad (eyelid myoclonia + absences + photosensitivity) | Jeavons syndrome is defined by a core triad of eyelid myoclonia with absences, photosensitivity, and EEG/paroxysms provoked by eye closure or IPS. | Reflex visual-triggered generalized EEG paroxysms underlie the syndrome. | 2015 | A. Covanis | https://doi.org/10.21307/joepi-2015-0033 | (covanis2015jeavonssyndrome–updatedreview pages 1-2) |
| Mechanism | Eye-closure-induced paroxysms | Voluntary/on-command slow eye closure in light reliably provokes brief bilateral spike/spike–wave discharges and eyelid jerks within ~0.5–4 s. | Eye-closure engages cortical circuits (occipital) and triggers generalized discharges via subcortical (thalamo-cortical) pathways. | 2015 | A. Covanis | https://doi.org/10.21307/joepi-2015-0033 | (covanis2015jeavonssyndrome–updatedreview pages 2-4) |
| Mechanism | Photosensitivity (light vs darkness) | Paroxysms require uninterrupted light: events do not occur in total darkness and IPS directly evokes occipital-driven discharges. | Photic input to occipital cortex (not brainstem photic blink) is necessary to trigger generalized responses. | 2015 | A. Covanis | https://doi.org/10.21307/joepi-2015-0033 | (covanis2015jeavonssyndrome–updatedreview pages 7-8) |
| Anatomy/Network | Visual cortex and pulvinar involvement | fMRI/EEG shows increased BOLD to eye closure in visual cortex and posterior thalamus (pulvinar) with gray-matter differences in occipital regions. | Occipital hyperexcitability and altered visual–thalamic connectivity facilitate reflex epileptogenesis. | 2014 | Vaudano et al. | https://doi.org/10.1002/ana.24236 | (vaudano2014thevisualsystem pages 1-2) |
| Mechanism/Network | Thalamo-cortical spread | Generalized discharges are proposed to spread from occipital cortex to frontal regions via subcortical/thalamo-cortical circuits. | Thalamo-cortical loops mediate rapid generalization of visually-triggered cortical discharges. | 2015 | A. Covanis | https://doi.org/10.21307/joepi-2015-0033 | (covanis2015jeavonssyndrome–updatedreview pages 7-8) |
| Anatomy/Network | Frontal eye fields (FEF) involvement | Structural/functional differences include decreased gray matter in bilateral frontal eye fields and engagement of eye-movement control networks during provocation. | Voluntary eye closure activates FEF which can trigger occipital cortex and downstream epileptic responses. | 2014 | Vaudano et al. | https://doi.org/10.1002/ana.24236 | (vaudano2014thevisualsystem pages 1-2) |
| Gene | SYNGAP1 | SYNGAP1 loss-of-function variants reported in EMA cases; SYNGAP1 encodes a synaptic Ras-GAP in NMDA receptor complexes affecting excitatory synaptic function. | Implicates excitatory synaptic dysfunction and altered dendritic spine/plasticity contributing to hyperexcitability. | 2021 | Mayo et al. | https://doi.org/10.3390/ijms22115609 | (mayo2021candidategenesfor pages 1-2) |
| Gene | NEXMIF (KIAA2022) | NEXMIF variants produce EMA-like phenotypes, often pharmacoresistant; X-linked gene with female-predominant effects via XCI/mosaicism hypotheses. | Synaptic/neurodevelopmental dysfunction from haploinsufficiency can produce myoclonic/absence seizures and early-onset EMA spectrum. | 2021 | Mayo et al. | https://doi.org/10.3390/ijms22115609 | (mayo2021candidategenesfor pages 26-27) |
| Gene | RORB | RORB alterations have been reported in some EMA cases and are proposed as candidate contributors to generalized photosensitive phenotypes. | RORB encodes a nuclear receptor involved in neuronal differentiation that may affect cortical network development/excitability. | 2021 | Mayo et al. | https://doi.org/10.3390/ijms22115609 | (mayo2021candidategenesfor pages 1-2) |
| Gene | CHD2 | CHD2 variants have been observed in a small number of EMA cases and are considered possible contributors, especially with GTCS comorbidity. | CHD2 chromatin remodeling dysfunction may perturb neuronal gene expression and cortical excitability. | 2021 | Mayo et al. | https://doi.org/10.3390/ijms22115609 | (mayo2021candidategenesfor pages 26-27) |
| Gene | SLC2A1 | SLC2A1 (GLUT1) alterations reported in isolated EMA cases; evidence insufficient to confirm causality but indicates metabolic contributions in some patients. | Impaired glucose transport can alter neuronal metabolism and seizure threshold in susceptible networks. | 2021 | Mayo et al. | https://doi.org/10.3390/ijms22115609 | (mayo2021candidategenesfor pages 26-27) |
| Gene | KCNB1 | Rare KCNB1 variants have been reported in EMA-like presentations, suggesting ion-channel dysfunction as a possible mechanism in select patients. | Voltage-gated potassium channel perturbation can change neuronal repolarization and network excitability. | 2021 | Mayo et al. | https://doi.org/10.3390/ijms22115609 | (mayo2021candidategenesfor pages 26-27) |
| Gene | NAA10 | NAA10 variants appear in a few EMA reports; causative role remains uncertain but may relate to broader neurodevelopmental perturbation. | N-terminal acetylation defects could impact multiple neuronal proteins and circuit development. | 2021 | Mayo et al. | https://doi.org/10.3390/ijms22115609 | (mayo2021candidategenesfor pages 26-27) |
| Gene/Case | CSNK2B (case report) | A de novo CSNK2B missense variant (p.Thr90Pro) was reported in a child presenting primarily with eyelid myoclonia, proposed as a likely pathogenic candidate. | CSNK2B (CK2 beta) influences neuronal development, Wnt/β-catenin signaling, and may affect network formation leading to hyperexcitability. | 2025 | He et al. | https://doi.org/10.3389/fped.2025.1583346 | (he2025casereporta pages 3-7) |
| Epidemiology/Clinical | Female predominance; prevalence among IGE (7–13%) | EMA shows female predominance and accounts for approximately 7–13% of idiopathic generalized epilepsies with absences in some series. | Demographics and familial aggregation support a genetic predisposition with sex-biased expression. | 2017 | Tuaç et al. | https://doi.org/10.14744/epilepsi.2016.88319 | (tuac2017jeavonssyndrome12 pages 1-2) |


*Table: Compact table summarizing pathophysiology, key genes, network anatomy, and epidemiology of Jeavons syndrome with evidence citations to source context IDs; useful for rapid inclusion in a disease knowledge base.*

## 1. Core Pathophysiology
- Primary mechanisms:
  - Reflex visual-triggered cortical hyperexcitability. Eye closure under light and IPS activate occipital cortex, with “eye-closure period”–linked paroxysms within 0.5–4 s and absence in total darkness (vaudano2014thevisualsystem pages 1-2, covanis2015jeavonssyndrome–updatedreview pages 7-8, covanis2015jeavonssyndrome–updatedreview pages 2-4).
  - Rapid thalamo-cortical generalization. Generalized discharges spread from occipital cortex to frontal regions “most likely through a subcortical circuit,” implicating thalamo-cortical loops and pulvinar (covanis2015jeavonssyndrome–updatedreview pages 7-8, vaudano2014thevisualsystem pages 1-2).
  - Eye-movement control network engagement. Decreased gray matter in bilateral frontal eye fields and BOLD engagement of saccade/pursuit networks during eye closure highlight FEF–visual cortex coupling in the reflex pathway (vaudano2014thevisualsystem pages 1-2).
- Dysregulated pathways:
  - Visual processing and thalamo-cortical oscillatory coupling (visual cortex–pulvinar–cortex). IPS and eye closure require light, indicating cortical visual pathway dependence rather than brainstem reflex pathways (covanis2015jeavonssyndrome–updatedreview pages 7-8, vaudano2014thevisualsystem pages 1-2).
  - Synaptic signaling in excitatory networks (NMDA receptor complex/SYNGAP1; chromatin remodeling/CHD2; nuclear receptor RORB influencing neuronal differentiation) inferred from candidate gene biology (mayo2021candidategenesfor pages 1-2, mayo2021candidategenesfor pages 26-27).
- Cellular processes affected:
  - Cortical network excitability and synchronization leading to generalized 3–6 Hz spike–wave bursts and eyelid myoclonia/absences (covanis2015jeavonssyndrome–updatedreview pages 1-2, covanis2015jeavonssyndrome–updatedreview pages 7-8).
  - Eye-closure motor program activation via FEF integrated with visual cortex drive (vaudano2014thevisualsystem pages 1-2).

## 2. Key Molecular Players
- Genes/Proteins (HGNC):
  - SYNGAP1 (HGNC:11494) – synaptic Ras GTPase-activating protein in NMDA receptor complex; LoF variants reported in EMA cases (mayo2021candidategenesfor pages 1-2, mayo2021candidategenesfor pages 26-27). DOI: https://doi.org/10.3390/ijms22115609 (2021-05).
  - NEXMIF/KIAA2022 (HGNC:28907) – X-linked; variants yield EMA-like phenotypes, often pharmacoresistant; XCI mosaicism posited in female predominance (mayo2021candidategenesfor pages 26-27). DOI: https://doi.org/10.3390/ijms22115609 (2021-05).
  - RORB (HGNC:10260) – nuclear receptor; implicated in some EMA cases; role in neuronal differentiation and cortical network maturation (mayo2021candidategenesfor pages 1-2). DOI: https://doi.org/10.3390/ijms22115609 (2021-05).
  - CHD2 (HGNC:2018) – chromatin remodeler; variants observed in EMA and photosensitive epilepsies (mayo2021candidategenesfor pages 26-27). DOI: https://doi.org/10.3390/ijms22115609 (2021-05).
  - SLC2A1 (HGNC:11005) – GLUT1; rare EMA reports suggest metabolic contributions (mayo2021candidategenesfor pages 26-27). DOI: https://doi.org/10.3390/ijms22115609 (2021-05).
  - KCNB1 (HGNC:6239) – Kv2.1 potassium channel; rare EMA-like presentations (mayo2021candidategenesfor pages 26-27). DOI: https://doi.org/10.3390/ijms22115609 (2021-05).
  - NAA10 (HGNC:13354) – N-terminal acetyltransferase; rare EMA reports (mayo2021candidategenesfor pages 26-27). DOI: https://doi.org/10.3390/ijms22115609 (2021-05).
  - CSNK2B (HGNC:2456) – Casein kinase 2 beta; de novo missense in a child with eyelid myoclonia; proposed novel candidate (he2025casereporta pages 3-7). DOI: https://doi.org/10.3389/fped.2025.1583346 (2025-09).
- Chemical entities (CHEBI) and therapeutics (contextual):
  - While not mechanistically proven for JS herein, broad generalized epilepsy management often uses valproic acid (CHEBI:39867), which was “most preferred” in one JS series; this reflects clinical practice rather than a mechanistic probe (tuac2017jeavonssyndrome12 pages 1-2).
- Cell types (CL):
  - Excitatory cortical pyramidal neurons (CL:0000624) within occipital cortex implicated by SYNGAP1/NMDA complex biology and visual-cortex driven fMRI activation (vaudano2014thevisualsystem pages 1-2, mayo2021candidategenesfor pages 1-2).
  - Thalamic relay neurons (CL:0000700), particularly pulvinar-associated relays, participate in visually driven thalamo-cortical propagation (vaudano2014thevisualsystem pages 1-2).
- Anatomical locations (UBERON):
  - Occipital lobe/visual cortex (UBERON:0000956) and primary visual cortex (V1; UBERON:0002436) show increased BOLD/gray-matter differences; posterior thalamus/pulvinar (UBERON:0001896) implicated; frontal eye fields (part of prefrontal/frontal cortex; UBERON:0006479) exhibit structural differences (vaudano2014thevisualsystem pages 1-2).

## 3. Biological Processes (GO terms; disrupted)
- Visual perception and photic stimulus processing: GO:0007601 (visual perception); GO:0009584 (detection of visible light). Eye-closure sensitivity requires light; absence in darkness indicates cortical visual pathway dependency (covanis2015jeavonssyndrome–updatedreview pages 7-8, covanis2015jeavonssyndrome–updatedreview pages 2-4).
- Thalamo-cortical rhythm generation and synchronization: GO:0021795 (cerebral cortex development; inferred), GO:0007268 (chemical synaptic transmission), GO:0019228 (neuronal action potential). Occipital-driven discharges generalize via thalamo-cortical circuits (covanis2015jeavonssyndrome–updatedreview pages 7-8, vaudano2014thevisualsystem pages 1-2).
- Glutamatergic synaptic signaling and plasticity: GO:0098978 (glutamatergic synaptic transmission), GO:0099578 (NMDA receptor signaling pathway). SYNGAP1 dysfunction implicates NMDA complex signaling and dendritic spine plasticity (mayo2021candidategenesfor pages 1-2, mayo2021candidategenesfor pages 26-27).
- Chromatin remodeling and neuronal gene expression: GO:0006338 (chromatin remodeling). CHD2 perturbation suggests altered neuronal transcriptional programs affecting excitability (mayo2021candidategenesfor pages 26-27).

## 4. Cellular Components (GO:CC)
- Postsynaptic density (GO:0014069) and NMDA receptor complex (GO: NMDA receptor complex; e.g., GO:0017147). SYNGAP1 localizes to PSD and NMDA complexes in excitatory synapses (mayo2021candidategenesfor pages 1-2).
- Thalamic nuclei (pulvinar) and occipital cortical laminae as circuit loci for initiation/propagation (anatomical evidence via fMRI/morphometry) (vaudano2014thevisualsystem pages 1-2).

## 5. Disease Progression
- Sequence of events:
  1) Genetic predisposition primes visual–thalamo-cortical circuits (covanis2015jeavonssyndrome–updatedreview pages 1-2).
  2) Voluntary/on-command slow eye closure in light initiates occipital cortical activation within 0.5–4 s (ECS window), often accompanied by upward gaze and eyelid jerks (vaudano2014thevisualsystem pages 1-2, covanis2015jeavonssyndrome–updatedreview pages 7-8).
  3) Occipital paroxysms rapidly generalize via thalamo-cortical circuits, producing brief 3–6 Hz spike–wave bursts (covanis2015jeavonssyndrome–updatedreview pages 7-8).
  4) Clinical eyelid myoclonia with behavioral arrest (absence) manifests; IPS can provoke similar paroxysms even with eyes open (covanis2015jeavonssyndrome–updatedreview pages 2-4).
  5) In some, generalized tonic–clonic seizures occur; photosensitivity contributes to self-induction behaviors (covanis2015jeavonssyndrome–updatedreview pages 7-8).
- Staging/phases: Childhood onset (2–14 years; peak 6–8), persistent photosensitivity, with variable persistence or remission; female predominance (tuac2017jeavonssyndrome12 pages 1-2).

## 6. Phenotypic Manifestations
- Key clinical phenotypes and HP terms:
  - Eyelid myoclonia (HP:0001265) and absence seizures (HP:0002121) temporally linked to eye closure and light (covanis2015jeavonssyndrome–updatedreview pages 1-2, covanis2015jeavonssyndrome–updatedreview pages 7-8).
  - Photosensitivity (HP:0007460) with photoparoxysmal response to IPS; lack of response in darkness (covanis2015jeavonssyndrome–updatedreview pages 7-8).
  - Eye-closure–induced epileptiform discharges (HP:0032393 analog; provoked within ≈0.5–4 s after eye closure) (vaudano2014thevisualsystem pages 1-2, covanis2015jeavonssyndrome–updatedreview pages 7-8).
  - Generalized 3–6 Hz spike–wave discharges (HP:0002353) often with frontal predominance during events (he2025casereporta pages 3-7, covanis2015jeavonssyndrome–updatedreview pages 1-2).
  - Female predominance and childhood onset (HP:0003674 for onset in first decade) (tuac2017jeavonssyndrome12 pages 1-2).

## Expert opinions and authoritative analysis
- Covanis emphasizes three necessary factors for clinical expression: “genetic predisposition,” “voluntary or on-command slow eye closure,” and “light input (photosensitivity/IPS)” (covanis2015jeavonssyndrome–updatedreview pages 2-4). The occipital cortex is “of crucial importance” in photosensitive epilepsies, with generalized spread via a “subcortical circuit” (covanis2015jeavonssyndrome–updatedreview pages 7-8).
- Vaudano et al. interpret fMRI/EEG data as demonstrating altered anatomo-functional properties of the visual system in EMA, with increased visual cortex/pulvinar responses and decreased frontal eye field gray matter, implicating visual–thalamo–FEF networks in pathophysiology (vaudano2014thevisualsystem pages 1-2).
- Genetic reviews highlight heterogeneity: “no single definitive causative gene,” but convergent synaptic/neurodevelopmental pathways (SYNGAP1, NEXMIF, RORB, CHD2) may modify excitability of visual–thalamo-cortical networks (mayo2021candidategenesfor pages 1-2, mayo2021candidategenesfor pages 26-27).

## Statistics and data from recent studies
- Epidemiology: EMA accounts for approximately 7–13% of idiopathic generalized epilepsies with absences; childhood onset (2–14 years; often 6–8), female predominance; blinking/eye closure more potent triggers than IPS in one series (tuac2017jeavonssyndrome12 pages 1-2).
- Temporal dynamics: Eye-closure–induced EEG paroxysms occur within 0.5–4 s of closing eyes and are absent in total darkness (vaudano2014thevisualsystem pages 1-2, covanis2015jeavonssyndrome–updatedreview pages 7-8).

## Gene/protein annotations (ontology-ready)
- SYNGAP1 (HGNC:11494): GO:0007268 (chemical synaptic transmission), GO:0099578 (NMDA receptor signaling), GO:0014069 (postsynaptic density); implicated in EMA (mayo2021candidategenesfor pages 1-2, mayo2021candidategenesfor pages 26-27).
- NEXMIF (HGNC:28907): GO:0007417 (central nervous system development), GO:0050808 (synapse organization) inferred from role in neurodevelopment; EMA-like phenotypes (mayo2021candidategenesfor pages 26-27).
- RORB (HGNC:10260): GO:0006355 (regulation of transcription, DNA-templated), GO:0022008 (neurogenesis); EMA cases reported (mayo2021candidategenesfor pages 1-2).
- CHD2 (HGNC:2018): GO:0006338 (chromatin remodeling); EMA cases reported (mayo2021candidategenesfor pages 26-27).
- SLC2A1 (HGNC:11005): GO:0005355 (glucose transmembrane transporter activity), GO:0006006 (glucose metabolic process); rare EMA (mayo2021candidategenesfor pages 26-27).
- KCNB1 (HGNC:6239): GO:0005267 (potassium channel activity), GO:0006813 (potassium ion transport); rare EMA-like (mayo2021candidategenesfor pages 26-27).
- NAA10 (HGNC:13354): GO:0006474 (N-terminal protein amino acid acetylation); rare EMA-like (mayo2021candidategenesfor pages 26-27).
- CSNK2B (HGNC:2456): GO:0006468 (protein phosphorylation), GO:0060070 (Wnt signaling pathway) per case discussion; proposed EMA candidate (he2025casereporta pages 3-7).

## Cell type involvement (CL)
- Cortical pyramidal neurons (CL:0000624) in occipital cortex; thalamic relay neurons in pulvinar (CL:0000700); cortical inhibitory interneurons (CL:0000099) are likely modulators of oscillatory balance though direct evidence in JS is not presented here (vaudano2014thevisualsystem pages 1-2, mayo2021candidategenesfor pages 1-2).

## Anatomical locations (UBERON)
- Primary/associative visual cortices (UBERON:0002436, UBERON:0000956); pulvinar/posterior thalamus (UBERON:0001896); frontal eye fields (UBERON:0006479) (vaudano2014thevisualsystem pages 1-2).

## Chemical entities (CHEBI)
- Valproic acid (CHEBI:39867) commonly used in clinical practice for generalized epilepsies; “most preferred” agent in small JS series (tuac2017jeavonssyndrome12 pages 1-2).

## Evidence items with PMIDs/DOIs and URLs
- Covanis A. Jeavons syndrome–updated review. 2015. DOI: 10.21307/joepi-2015-0033; URL: https://doi.org/10.21307/joepi-2015-0033 (covanis2015jeavonssyndrome–updatedreview pages 1-2, covanis2015jeavonssyndrome–updatedreview pages 2-4, covanis2015jeavonssyndrome–updatedreview pages 7-8).
- Vaudano AE et al. The visual system in eyelid myoclonia with absences. Ann Neurol. 2014;76:412–427. DOI: 10.1002/ana.24236; URL: https://doi.org/10.1002/ana.24236 (vaudano2014thevisualsystem pages 1-2).
- Tuaç ST et al. Jeavons Syndrome: 12 Cases. 2017. DOI: 10.14744/epilepsi.2016.88319; URL: https://doi.org/10.14744/epilepsi.2016.88319 (tuac2017jeavonssyndrome12 pages 1-2).
- Mayo S et al. Candidate Genes for Eyelid Myoclonia with Absences, Review of the Literature. Int J Mol Sci. 2021;22:5609. DOI: 10.3390/ijms22115609; URL: https://doi.org/10.3390/ijms22115609 (mayo2021candidategenesfor pages 1-2, mayo2021candidategenesfor pages 26-27).
- He Y et al. Case Report: CSNK2B variant with primary eyelid myoclonia. Front Pediatr. 2025. DOI: 10.3389/fped.2025.1583346; URL: https://doi.org/10.3389/fped.2025.1583346 (he2025casereporta pages 3-7).

## Notes on recency and limitations
This report prioritizes high-quality mechanistic sources; however, within the accessible evidence set, most detailed pathophysiological data derive from 2014–2017 studies and a 2021 genetic review. A 2025 single case is included for CSNK2B as a candidate. More recent 2023–2024 consensus and EEG/clinical analyses exist but were not available in the gathered context; thus, some sections are necessarily partial with respect to the latest consensus statements.


References

1. (covanis2015jeavonssyndrome–updatedreview pages 1-2): A Covanis. Jeavons syndrome–updated review. Unknown journal, 2015. URL: https://doi.org/10.21307/joepi-2015-0033, doi:10.21307/joepi-2015-0033.

2. (covanis2015jeavonssyndrome–updatedreview pages 7-8): A Covanis. Jeavons syndrome–updated review. Unknown journal, 2015. URL: https://doi.org/10.21307/joepi-2015-0033, doi:10.21307/joepi-2015-0033.

3. (vaudano2014thevisualsystem pages 1-2): Anna Elisabetta Vaudano, Andrea Ruggieri, Manuela Tondelli, Pietro Avanzini, Francesca Benuzzi, Giuliana Gessaroli, Gaetano Cantalupo, Massimo Mastrangelo, Aglaia Vignoli, Carlo Di Bonaventura, Maria Paola Canevini, Bernardo Dalla Bernardina, Paolo Frigio Nichelli, and Stefano Meletti. The visual system in eyelid myoclonia with absences. Annals of Neurology, 76:412-427, Sep 2014. URL: https://doi.org/10.1002/ana.24236, doi:10.1002/ana.24236. This article has 84 citations and is from a highest quality peer-reviewed journal.

4. (covanis2015jeavonssyndrome–updatedreview pages 2-4): A Covanis. Jeavons syndrome–updated review. Unknown journal, 2015. URL: https://doi.org/10.21307/joepi-2015-0033, doi:10.21307/joepi-2015-0033.

5. (mayo2021candidategenesfor pages 1-2): Sonia Mayo, Irene Gómez-Manjón, Fco. Javier Fernández-Martínez, Ana Camacho, Francisco Martínez, and Julián Benito-León. Candidate genes for eyelid myoclonia with absences, review of the literature. International Journal of Molecular Sciences, 22:5609, May 2021. URL: https://doi.org/10.3390/ijms22115609, doi:10.3390/ijms22115609. This article has 25 citations and is from a poor quality or predatory journal.

6. (mayo2021candidategenesfor pages 26-27): Sonia Mayo, Irene Gómez-Manjón, Fco. Javier Fernández-Martínez, Ana Camacho, Francisco Martínez, and Julián Benito-León. Candidate genes for eyelid myoclonia with absences, review of the literature. International Journal of Molecular Sciences, 22:5609, May 2021. URL: https://doi.org/10.3390/ijms22115609, doi:10.3390/ijms22115609. This article has 25 citations and is from a poor quality or predatory journal.

7. (he2025casereporta pages 3-7): Yuanyuan He, Qingqing Deng, Chen Chen, Zhanli Liu, and Lingwei Weng. Case report: a case of poirier–bienvenu neurodevelopmental syndrome manifesting primarily as eyelid myoclonia. Frontiers in Pediatrics, Sep 2025. URL: https://doi.org/10.3389/fped.2025.1583346, doi:10.3389/fped.2025.1583346. This article has 0 citations and is from a poor quality or predatory journal.

8. (tuac2017jeavonssyndrome12 pages 1-2): ST TUAÇ, C Yalcinkaya, and AV Demirbilek. Jeavons syndrome: 12 cases. Journal of the Turkish Epilepsi Society, 2017. URL: https://doi.org/10.14744/epilepsi.2016.88319, doi:10.14744/epilepsi.2016.88319. This article has 5 citations.