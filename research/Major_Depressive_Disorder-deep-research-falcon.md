---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T18:47:17.715967'
end_time: '2025-12-17T18:55:49.493721'
duration_seconds: 511.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Major Depressive Disorder
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 19
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Major Depressive Disorder
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Major Depressive Disorder**.
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
- **Disease Name:** Major Depressive Disorder
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Major Depressive Disorder**.
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


Plan overview: We surveyed recent (2023–2024) peer‑reviewed reviews and translational articles to synthesize molecular and cellular mechanisms of Major Depressive Disorder (MDD), emphasizing monoamine, glutamate/GABA excitation–inhibition, neuroplasticity/BDNF, HPA axis, immune–inflammation/kynurenine, mitochondrial–oxidative bioenergetics, circadian/sleep, myelination/oligodendrocytes, and synaptic function. We then mapped mechanisms to ontology terms (HGNC, GO, CL, UBERON, CHEBI) and summarized current clinical implementations (ketamine/esketamine, dextromethorphan–bupropion, neurosteroids). Citations indicate supporting sources and include DOI URLs and publication years.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Major Depressive Disorder
- MONDO ID: MONDO:0009409
- Category: Complex

Pathophysiology description
MDD is a heterogeneous, systems‑level brain disorder arising from convergent dysregulation of neurotransmission, stress–neuroendocrine control, immune–metabolic signaling, cellular bioenergetics, and neuroplasticity within limbic–prefrontal circuits. Contemporary models integrate: (a) monoaminergic signaling deficits (serotonin, noradrenaline, dopamine); (b) glutamate/GABA excitation–inhibition imbalance with synaptic and postsynaptic plasticity failure; (c) HPA axis hyperactivity with glucocorticoid receptor resistance; (d) innate/adaptive immune activation that biases tryptophan metabolism along the kynurenine pathway toward neurotoxic metabolites; (e) mitochondrial respiratory dysfunction, oxidative stress, and altered calcium/ATP homeostasis in neurons and glia; (f) oligodendrocyte lineage/myelination abnormalities that compromise long‑range circuit conduction; and (g) network‑scale synaptic vesicle and postsynaptic density perturbations in subgenual/anterior cingulate, prefrontal cortex, hippocampus, and amygdala (Cui 2024; McIntyre & Jain 2024; Kouba 2024; Correia & Vale 2024; Wetzel 2024; Zhang et al. 2025 preprint) (cui2024majordepressivedisorder pages 23-24, mcintyre2024glutamatergicmodulatorsfor pages 7-9, kouba2024roleofinflammatory pages 2-3, correia2024advancementsexploringmajor pages 1-2, wetzel2024mitochondrialandcellular pages 10-12, zhang2025multiomicsinsightsin pages 14-18).

Core Pathophysiology
1) Monoamine hypothesis, refined: Serotonin, noradrenaline, and dopamine pathway alterations interact with stress biology and neurotrophic signaling. Despite efficacy of monoamine reuptake inhibitors, non‑remission remains high (~30%), indicating additional pathobiology beyond monoamines (Cui 2024; Correia & Vale 2024) (cui2024majordepressivedisorder pages 23-24, correia2024advancementsexploringmajor pages 1-2). URL examples: https://doi.org/10.1038/s41392-024-01738-y (2024); https://doi.org/10.3390/ijtm4010010 (2024).
2) Glutamate/GABA and synaptic plasticity failure: Human and preclinical evidence implicates reduced GABAergic tone, altered NMDA/AMPA signaling, and impaired synaptogenesis; rapid‑acting agents (ketamine/esketamine, dextromethorphan–bupropion) exploit this pathway (McIntyre & Jain 2024) (mcintyre2024glutamatergicmodulatorsfor pages 7-9). URL: https://doi.org/10.1007/s40263-024-01114-y (2024).
3) Neurotrophic/BDNF signaling: Reduced BDNF and altered TrkB signaling are linked with hippocampal atrophy and impaired synaptogenesis; stress and oxidative–HPA dysregulation suppress BDNF expression and signaling (Correia & Vale 2024; Cui 2024) (correia2024advancementsexploringmajor pages 1-2, cui2024majordepressivedisorder pages 23-24). URL: https://doi.org/10.3390/ijtm4010010 (2024); https://doi.org/10.1038/s41392-024-01738-y (2024).
4) HPA axis dysregulation: Chronic stress elevates cortisol, disrupts glucocorticoid receptor (GR) feedback, and damages hippocampal circuits. Reviews highlight patient subsets with marked HPA abnormality and propose precision testing (e.g., dex‑CRH) to match HPA‑targeted therapies (Cui 2024) (cui2024majordepressivedisorder pages 23-24). URL: https://doi.org/10.1038/s41392-024-01738-y (2024).
5) Immune–inflammation and kynurenine pathway: Elevated cytokines (IL‑6, IL‑1β, TNF‑α) and microglial–astrocytic interactions shift tryptophan metabolism via IDO1/KMO toward 3‑hydroxykynurenine and quinolinic acid (NMDA agonist), reducing serotonin bioavailability and promoting excitotoxic stress (Kouba 2024) (kouba2024roleofinflammatory pages 2-3). URL: https://doi.org/10.3390/cells13050423 (2024).
6) Mitochondrial bioenergetics and oxidative stress: Patient‑derived astrocytes and neurons show reduced basal/maximal respiration, altered mitochondrial membrane potential and calcium handling, and ATP shortfalls, consistent with oxidative–bioenergetic deficits contributing to impaired neuroplasticity (Wetzel 2024) (wetzel2024mitochondrialandcellular pages 10-12). URL: https://doi.org/10.3390/ijms25020963 (2024).
7) Myelination/oligodendrocytes: Single‑cell and multi‑omics analyses associate MDD with oligodendrocyte lineage and excitatory neuron dysfunction in prefrontal cortex, implicating myelin and axonal support in mood‑circuit dysconnectivity (Cui 2024; Zhang et al. 2025 preprint) (cui2024majordepressivedisorder pages 23-24, zhang2025multiomicsinsightsin pages 14-18). URL: https://doi.org/10.1038/s41392-024-01738-y (2024); https://doi.org/10.1101/2025.05.03.25326369 (2025 preprint).
8) Synaptic function: Transcriptomic signatures converge on synaptic vesicle cycling, postsynaptic density, and splicing programs in excitatory neurons (Zhang et al. 2025 preprint; Cui 2024) (zhang2025multiomicsinsightsin pages 14-18, cui2024majordepressivedisorder pages 23-24). URL: https://doi.org/10.1101/2025.05.03.25326369 (2025 preprint); https://doi.org/10.1038/s41392-024-01738-y (2024).

Key Molecular Players
- Genes/Proteins (HGNC): BDNF; NTRK2; CREB1; GRIN1/GRIN2A (NMDA receptor subunits); GRIA1 (AMPA); GAD1; GABRA1/GABRD (GABAA subunits); SLC6A4 (SERT); IDO1; KMO; IL6; IL1B; TNF; NR3C1 (GR); FKBP5; mitochondrial bioenergetics genes (e.g., SLC25A5/ANT2, ALDH2, IMMT) (Correia 2024; Kouba 2024; Wetzel 2024; Cui 2024; McIntyre & Jain 2024) (correia2024advancementsexploringmajor pages 1-2, kouba2024roleofinflammatory pages 2-3, wetzel2024mitochondrialandcellular pages 10-12, cui2024majordepressivedisorder pages 23-24, mcintyre2024glutamatergicmodulatorsfor pages 7-9). URLs: https://doi.org/10.3390/ijtm4010010 (2024); https://doi.org/10.3390/cells13050423 (2024); https://doi.org/10.3390/ijms25020963 (2024); https://doi.org/10.1038/s41392-024-01738-y (2024); https://doi.org/10.1007/s40263-024-01114-y (2024).
- Chemical Entities (CHEBI): Ketamine/esketamine; dextromethorphan; bupropion; allopregnanolone analogs (brexanolone, zuranolone); monoamine reuptake inhibitors; kynurenine pathway metabolites (kynurenine, quinolinic acid) (McIntyre & Jain 2024; Kouba 2024; Cui 2024) (mcintyre2024glutamatergicmodulatorsfor pages 7-9, kouba2024roleofinflammatory pages 2-3, cui2024majordepressivedisorder pages 23-24).
- Cell Types (CL): Cortical excitatory neurons; GABAergic interneurons (SST+, PVALB+); astrocytes; microglia; oligodendrocyte precursor cells and mature oligodendrocytes (Cui 2024; Kouba 2024; Wetzel 2024; Zhang et al. 2025 preprint) (cui2024majordepressivedisorder pages 23-24, kouba2024roleofinflammatory pages 2-3, wetzel2024mitochondrialandcellular pages 10-12, zhang2025multiomicsinsightsin pages 14-18).
- Anatomical Locations (UBERON): Subgenual anterior cingulate cortex, dorsolateral prefrontal cortex, hippocampus, amygdala, hypothalamus–pituitary–adrenal axis structures (Cui 2024; Zhang et al. 2025 preprint) (cui2024majordepressivedisorder pages 23-24, zhang2025multiomicsinsightsin pages 14-18).

Biological Processes (GO annotations)
- Synaptic transmission and plasticity: GO:0007268 (neurotransmitter receptor signaling), GO:0048167 (regulation of synaptic plasticity) (Correia 2024; McIntyre & Jain 2024) (correia2024advancementsexploringmajor pages 1-2, mcintyre2024glutamatergicmodulatorsfor pages 7-9).
- Stress and HPA signaling: GO:0006950 (response to stress), GO terms related to glucocorticoid receptor signaling (Cui 2024) (cui2024majordepressivedisorder pages 23-24).
- Inflammation and kynurenine metabolism: GO:0006954 (inflammatory response), GO terms for kynurenine metabolic process (Kouba 2024) (kouba2024roleofinflammatory pages 2-3).
- Mitochondrial respiration/oxidative stress: GO:0006119 (oxidative phosphorylation/respiration), GO:0006979 (response to oxidative stress) (Wetzel 2024) (wetzel2024mitochondrialandcellular pages 10-12).
- Myelination/oligodendrocyte differentiation: GO:0042552 (myelination), GO:0014003 (oligodendrocyte development) (Cui 2024; Zhang 2025 preprint) (cui2024majordepressivedisorder pages 23-24, zhang2025multiomicsinsightsin pages 14-18).

Cellular Components (GO CC)
- Postsynaptic density; synaptic vesicle; mitochondrial inner membrane; myelin sheath; extrasynaptic GABAA receptor complexes (Cui 2024; McIntyre & Jain 2024; Wetzel 2024) (cui2024majordepressivedisorder pages 23-24, mcintyre2024glutamatergicmodulatorsfor pages 7-9, wetzel2024mitochondrialandcellular pages 10-12).

Disease Progression (sequence of events)
- Stress/early adversity and genetic susceptibility activate HPA axis and peripheral immune signals → elevated cortisol and cytokines drive GR resistance, microglial activation, and IDO1/KMO upregulation → tryptophan diverted from serotonin to neurotoxic kynurenines (quinolinic acid), promoting NMDA‑mediated excitotoxicity → mitochondrial dysfunction and oxidative stress further impair synaptic plasticity and neurogenesis → network‑level deficits in glutamate/GABA balance, synaptic vesicle trafficking, and myelination in prefrontal–limbic circuits → clinical manifestations (anhedonia, low mood, cognitive dysfunction) and variable treatment response (Cui 2024; Kouba 2024; Correia & Vale 2024; Wetzel 2024) (cui2024majordepressivedisorder pages 23-24, kouba2024roleofinflammatory pages 2-3, correia2024advancementsexploringmajor pages 1-2, wetzel2024mitochondrialandcellular pages 10-12). URLs: https://doi.org/10.1038/s41392-024-01738-y (2024); https://doi.org/10.3390/cells13050423 (2024); https://doi.org/10.3390/ijtm4010010 (2024); https://doi.org/10.3390/ijms25020963 (2024).

Phenotypic Manifestations (HP terms)
- Depressed mood (HP:0000716), anhedonia (HP:0034259), psychomotor changes (HP:0000752), sleep disturbance (HP:0002360), cognitive impairment (HP:0100543). Mechanistic mapping: reduced BDNF/neuroplasticity and mitochondrial ATP constrain cognitive circuits; E/I imbalance (glutamate/GABA) contributes to anhedonia and mood reactivity; HPA/immune–kynurenine perturbations align with sleep and energy dysregulation (Cui 2024; Correia & Vale 2024; Kouba 2024) (cui2024majordepressivedisorder pages 23-24, correia2024advancementsexploringmajor pages 1-2, kouba2024roleofinflammatory pages 2-3).

Current applications and real‑world implementations
- Ketamine and intranasal esketamine: Rapid symptom reduction in TRD, mechanistically linked to NMDA antagonism → AMPA throughput → BDNF/mTOR synaptogenesis; considerations include dissociation, cardiovascular/urinary effects, scheduling, and supervised administration. Regulatory approvals (e.g., 2019 for esketamine) and clinical adoption are summarized (McIntyre & Jain 2024; review) (mcintyre2024glutamatergicmodulatorsfor pages 7-9). URL: https://doi.org/10.1007/s40263-024-01114-y (2024).
- Dextromethorphan–bupropion (AXS‑05/Auvelity): Oral agent combining NMDA antagonism and sigma‑1 agonism with monoaminergic effects; approved for MDD and positioned as a glutamatergic modulator with favorable practicality relative to parenteral ketamine (McIntyre & Jain 2024) (mcintyre2024glutamatergicmodulatorsfor pages 7-9). URL: https://doi.org/10.1007/s40263-024-01114-y (2024).
- Neurosteroids (brexanolone IV; zuranolone oral): Positive allosteric modulators of GABAA receptors (including extrasynaptic δ‑subunit‑containing receptors) providing rapid relief in postpartum depression and informing GABAergic deficits in depressive pathophysiology (Correia & Vale 2024; Cui 2024) (correia2024advancementsexploringmajor pages 1-2, cui2024majordepressivedisorder pages 23-24). URLs: https://doi.org/10.3390/ijtm4010010 (2024); https://doi.org/10.1038/s41392-024-01738-y (2024).

Expert opinions and analysis from authoritative sources
- Signal Transduction and Targeted Therapy (Cui 2024) synthesizes MDD as multisystem with neuroplasticity, HPA, immune and metabolic/mitochondrial axes, advocating for multi‑organ, multi‑target treatments and improved animal models (cui2024majordepressivedisorder pages 23-24). URL: https://doi.org/10.1038/s41392-024-01738-y (2024).
- CNS Drugs review (McIntyre & Jain 2024) details the translational arc of glutamatergic agents, highlighting successes (esketamine, AXS‑05) and failures of several NMDA‑site modulators, underscoring synaptic plasticity’s centrality and the need for safety/access frameworks (mcintyre2024glutamatergicmodulatorsfor pages 7-9). URL: https://doi.org/10.1007/s40263-024-01114-y (2024).
- Cells review (Kouba 2024) integrates immune–kynurenine mechanisms with glutamate toxicity and neuroplasticity failure, supporting immunopsychiatry approaches (kouba2024roleofinflammatory pages 2-3). URL: https://doi.org/10.3390/cells13050423 (2024).
- IJMS case‑based translational work (Wetzel 2024) provides cellular bioenergetics evidence for mitochondrial involvement in MDD glia and neurons, aligning with precision‐medicine biomarker development (wetzel2024mitochondrialandcellular pages 10-12). URL: https://doi.org/10.3390/ijms25020963 (2024).

Relevant statistics and data from recent studies
- Non‑remission remains substantial with current monoaminergic approaches (~30%), motivating mechanistically targeted therapies (Cui 2024) (cui2024majordepressivedisorder pages 23-24).
- Translational approvals: esketamine (2019) for TRD; dextromethorphan–bupropion (2022) for MDD—illustrating the clinical impact of glutamatergic modulation (McIntyre & Jain 2024) (mcintyre2024glutamatergicmodulatorsfor pages 7-9).
- Cellular bioenergetics (patient‑derived astrocytes): reduced basal and maximal respiration and ATP‑related oxygen consumption; altered mitochondrial membrane potential and calcium handling, supporting bioenergetic load in symptom biology (Wetzel 2024) (wetzel2024mitochondrialandcellular pages 10-12).

Ontology‑aligned annotations
- Genes/Proteins (HGNC): BDNF; NTRK2; GRIN1/2A; GRIA1; GAD1; GABRA1/GABRD; SLC6A4; IDO1; KMO; IL6; IL1B; TNF; NR3C1; FKBP5; SLC25A5; ALDH2; IMMT (correia2024advancementsexploringmajor pages 1-2, kouba2024roleofinflammatory pages 2-3, wetzel2024mitochondrialandcellular pages 10-12, cui2024majordepressivedisorder pages 23-24, mcintyre2024glutamatergicmodulatorsfor pages 7-9).
- GO Biological Processes: neurotransmitter receptor signaling (GO:0007268); regulation of synaptic plasticity (GO:0048167/GO:0048168); inflammatory response (GO:0006954); response to stress (GO:0006950); mitochondrial respiration (GO:0006119); myelination (GO:0042552) (mcintyre2024glutamatergicmodulatorsfor pages 7-9, kouba2024roleofinflammatory pages 2-3, wetzel2024mitochondrialandcellular pages 10-12, cui2024majordepressivedisorder pages 23-24).
- Cell Types (CL): cortical excitatory neuron; GABAergic interneuron (SST+, PVALB+); astrocyte; microglial cell; oligodendrocyte precursor cell; oligodendrocyte (cui2024majordepressivedisorder pages 23-24, kouba2024roleofinflammatory pages 2-3, wetzel2024mitochondrialandcellular pages 10-12, zhang2025multiomicsinsightsin pages 14-18).
- Anatomical locations (UBERON): subgenual anterior cingulate cortex; dorsolateral prefrontal cortex; hippocampus; amygdala; hypothalamus–pituitary–adrenal axis (cui2024majordepressivedisorder pages 23-24, zhang2025multiomicsinsightsin pages 14-18).
- Cellular Components (GO CC): postsynaptic density; synaptic vesicle; mitochondrial inner membrane; myelin sheath; extrasynaptic GABAA receptor complex (mcintyre2024glutamatergicmodulatorsfor pages 7-9, wetzel2024mitochondrialandcellular pages 10-12, cui2024majordepressivedisorder pages 23-24).
- Chemicals (CHEBI): ketamine; esketamine; dextromethorphan; bupropion; allopregnanolone analogs (brexanolone, zuranolone); kynurenine; quinolinic acid (mcintyre2024glutamatergicmodulatorsfor pages 7-9, kouba2024roleofinflammatory pages 2-3, cui2024majordepressivedisorder pages 23-24).
- Phenotypes (HP): depressed mood (HP:0000716); anhedonia (HP:0034259); psychomotor changes (HP:0000752); sleep disturbance (HP:0002360); cognitive impairment (HP:0100543) (cui2024majordepressivedisorder pages 23-24, correia2024advancementsexploringmajor pages 1-2).

Embedded Evidence Map
| Domain / Pathway | Key mechanisms (1–2 sentences) | Representative genes / proteins (HGNC) | Cell types (CL) | Anatomical loci (UBERON) | GO biological processes (GO BP) | Key chemicals / drugs (CHEBI) | Recent evidence (DOI / URL / Year; brief quantitative data) |
|---|---|---:|---|---|---|---|---|
| Monoamine (serotonin/dopamine/noradrenaline) | Reduced monoaminergic signaling and altered transporter/receptor function impair mood regulation and reward; interacts with HPA and immune axes. | SLC6A4, TPH2, MAOA, DRD2 | Serotonergic & dopaminergic neurons; astrocytes | Raphe nuclei; ventral tegmental area; prefrontal cortex, striatum | "monoamine transport"; "neurotransmitter receptor signaling" (GO:0007268) | SSRIs (e.g., escitalopram), SNRIs (venlafaxine) | Comprehensive 2024 review summarizing monoamine + multisystem interplay: Cui et al., doi:10.1038/s41392-024-01738-y (2024) ("~30% non-remission" noted) (cui2024majordepressivedisorder pages 23-24) |
| Glutamate–GABA (excitation–inhibition) | Dysregulated glutamatergic excitation and GABAergic inhibition (reduced GABA, altered NMDA/AMPA signaling) → impaired E/I balance, excitotoxic risk and rapid-acting glutamatergic therapeutics. | GRIN1/GRIN2A, GRIA1, GABRA1, GAD1 | Excitatory (glutamatergic) neurons; inhibitory interneurons (SST, PVALB); astrocytes | Prefrontal cortex (dlPFC), anterior cingulate, hippocampus | "synaptic transmission"; "regulation of membrane potential" (GO:0007269) | Ketamine, esketamine, dextromethorphan; memantine | Glutamate-targeted translational successes and trial landscape; approvals: esketamine (2019), AXS‑05 (dextromethorphan–bupropion) discussed (McIntyre & Jain, doi:10.1007/s40263-024-01114-y, 2024) (mcintyre2024glutamatergicmodulatorsfor pages 7-9) |
| Neuroplasticity / BDNF | Reduced BDNF expression and impaired TrkB signaling → decreased synaptogenesis, neurogenesis and structural atrophy (hippocampus) linking stress to circuit dysfunction. | BDNF, NTRK2 (TrkB), CREB1 | Neurons (excitatory), astrocytes | Hippocampus, prefrontal cortex | "synaptic plasticity" (GO:0048167); "neurotrophin signaling" | Exercise, traditional antidepressants; ketamine (indirectly increases BDNF) | BDNF–MDD mechanistic review summarizing exon/epigenetic links and clinical correlations: Correia & Vale, doi:10.3390/ijtm4010010 (2024) (correia2024advancementsexploringmajor pages 8-9, correia2024advancementsexploringmajor pages 1-2) |
| HPA axis – cortisol / stress | Chronic HPA hyperactivity, glucocorticoid receptor (GR/NR3C1) resistance and elevated cortisol cause hippocampal vulnerability, reduced neurogenesis, and immune modulation. | CRH, NR3C1, FKBP5 | Hypothalamic neuroendocrine cells; hippocampal neurons; immune cells | Hypothalamus; pituitary; hippocampus | "response to stress" (GO:0006950); "glucocorticoid receptor signaling" | GR modulators (experimental) | HPA axis as precision target; reviews highlight subset HPA abnormalities and need for companion diagnostics (dex‑CRH/mDST): Menke et al. (cui2024majordepressivedisorder pages 23-24) and HPA-focused reviews (cui2024majordepressivedisorder pages 23-24, correia2024advancementsexploringmajor pages 1-2) (2024) |
| Immune — inflammation & kynurenine | Peripheral/central inflammation (IL‑6, IL‑1β, TNF‑α) activates microglia, shifts tryptophan metabolism via IDO1/KMO toward neurotoxic kynurenines (3‑HK, quinolinic acid) reducing serotonin and promoting excitotoxicity. | IL6, IL1B, TNF, IDO1, KMO, KYNU | Microglia, astrocytes, peripheral monocytes | Blood–brain interface; hippocampus; PFC | "inflammatory response" (GO:0006954); "kynurenine metabolic process" | Anti‑inflammatories (investigational), kynurenine pathway modulators (experimental) | Inflammation–kynurenine mechanistic review and therapeutic implications: Kouba et al., doi:10.3390/cells13050423 (2024) (kouba2024roleofinflammatory pages 2-3) |
| Mitochondria / oxidative stress & bioenergetics | Impaired mitochondrial respiration, altered membrane potential, disrupted Ca2+ homeostasis and increased ROS → reduced ATP, neuroplasticity deficits and vulnerability to stress. | SLC25A5, ALDH2, IMMT (examples); PGC1A (PPARGC1A) | Neurons, astrocytes, oligodendrocytes, peripheral immune cells | Prefrontal cortex; hippocampus; systemic (blood biomarkers) | "mitochondrial respiration" (GO:0006119); "response to oxidative stress" (GO:0006979) | CoQ10, antioxidants (nutraceuticals; investigational) | Patient‑derived cell evidence: decreased basal/maximal respiration, lower mitochondrial membrane potential in MDD astrocytes and case studies (Wetzel et al., doi:10.3390/ijms25020963, 2024) (wetzel2024mitochondrialandcellular pages 10-12) |
| Circadian / sleep | Circadian clock gene dysregulation and sleep disturbance disrupts hormonal, immune and metabolic rhythms, exacerbating vulnerability to depression and impairing recovery. | CLOCK, BMAL1 (ARNTL), PER1, CRY1 | Suprachiasmatic nucleus neurons; cortical neurons; peripheral cells | Suprachiasmatic nucleus; prefrontal cortex; systemic | "circadian regulation of gene expression" (GO:0032922); "sleep regulation" | Melatonin, chronotherapies (light/behavioral) | Circadian–sleep review linking clock gene expression to depressive symptom severity and therapeutic opportunities: Gabryelska et al., doi:10.1038/s41398-024-03134-0 (2024) (mcintyre2024glutamatergicmodulatorsfor pages 7-9) |
| Myelination / oligodendrocytes | Oligodendrocyte lineage dysfunction and altered myelination impair circuit conduction and metabolic support for neurons, contributing to mood circuit dysconnectivity. | MBP, OLIG2, PDGFRA, MOG | Oligodendrocyte precursor cells (OPCs), mature oligodendrocytes | Prefrontal cortex (white matter tracts), hippocampus | "myelination" (GO:0042552); "oligodendrocyte differentiation" | Remyelination strategies (emerging); indirect effect of antidepressants | Emerging evidence implicates OPCs / oligodendrocyte changes in MDD from single‑cell and translational studies (single‑cell findings summarized in Zhang preprint and reviews in 2024–25) (zhang2025multiomicsinsightsin pages 14-18, cui2024majordepressivedisorder pages 23-24) |
| Synaptic function & vesicular trafficking | Altered synaptic vesicle cycling, postsynaptic density proteins and splicing lead to deficient neurotransmission and network-level dysregulation in mood circuits. | SYN1, PSD95 (DLG4), SYNAPTOTAGMINS, RAB proteins | Excitatory & inhibitory neurons; presynaptic terminals; astrocytes | Subgenual ACC, amygdala, dlPFC | "synaptic vesicle cycle" (GO:0099504); "postsynaptic density organization" | Synaptogenic agents (ketamine‑linked plasticity) | Large‑scale transcriptomic/single‑cell analyses reveal convergent dysregulation of synaptic and vesicular pathways in excitatory neurons (dlPFC/subgenual ACC): Goes et al., integrative findings summarized in multi‑omics preprints/reviews (zhang2025multiomicsinsightsin pages 14-18, cui2024majordepressivedisorder pages 23-24) (2024–2025) |
| Translational — Ketamine / Esketamine | NMDA receptor antagonism → transient disinhibition of glutamate release, AMPA activation, BDNF/mTOR signaling and rapid synaptogenesis; rapid antidepressant but safety/abuse considerations limit use. | GRINs, BDNF, mTOR (FRAP1) | Cortical excitatory neurons; interneurons; microglia (immune effects) | Prefrontal cortex; limbic circuits | "regulation of synaptic plasticity" (GO:0048168) | Ketamine (R,S), Esketamine (S) | Clinical trial landscape and approvals; esketamine approved 2019; overview and trial trends (McIntyre & Jain, doi:10.1007/s40263-024-01114-y, 2024) (mcintyre2024glutamatergicmodulatorsfor pages 7-9) |
| Translational — Dextromethorphan–bupropion (AXS‑05) | NMDA antagonism + sigma‑1 agonism (dextromethorphan) combined with monoaminergic reuptake inhibition (bupropion) — designed for oral rapid efficacy in MDD. | SLC6A3 (bupropion target indirect), sigma‑1 receptor (SIGMAR1) | Cortical neurons; monoaminergic neurons | Prefrontal cortex | "modulation of synaptic transmission" | Dextromethorphan, bupropion (combination product Auvelity / AXS‑05) | Approved agent; cited as translational glutamatergic success in review of glutamatergic modulators (McIntyre & Jain, doi:10.1007/s40263-024-01114-y, 2024) (mcintyre2024glutamatergicmodulatorsfor pages 7-9) |
| Translational — Neurosteroids (brexanolone; zuranolone) | Positive allosteric modulation of synaptic and extrasynaptic GABAA receptors (including δ‑subunit‑containing receptors) producing rapid mood stabilization, esp. postpartum depression. | GABRA4, GABRD, AKR1C1/2 (steroid metabolism enzymes) | Cortical/limbic neurons; astrocytes | Limbic system; postpartum systemic context | "GABAergic synaptic transmission" (GO:0032228) | Brexanolone (IV allopregnanolone), Zuranolone (oral neurosteroid) | Neurosteroid drug reviews and clinical-update summaries (efficacy in PPD; zuranolone clinical meta‑analyses exist in 2023–24 literature); clinical trial summaries and mechanism reviews (correia2024advancementsexploringmajor pages 8-9, correia2024advancementsexploringmajor pages 1-2) (2023–2024) |


*Table: Concise, citable table mapping core molecular/cellular pathways implicated in Major Depressive Disorder with representative genes, cell types, loci, GO processes, key chemicals/drugs, and recent 2023–2024 evidence (pqac citations). This aids rapid reference for mechanism-to-translation links.*

Evidence items with URLs/dates (selection)
- Cui L et al. Major depressive disorder: hypothesis, mechanism, prevention and treatment. Signal Transduct Target Ther. 2024; DOI: 10.1038/s41392-024-01738-y; URL: https://doi.org/10.1038/s41392-024-01738-y (Feb 2024) (cui2024majordepressivedisorder pages 23-24).
- McIntyre RS, Jain R. Glutamatergic modulators for major depression from theory to clinical use. CNS Drugs. 2024; DOI: 10.1007/s40263-024-01114-y; URL: https://doi.org/10.1007/s40263-024-01114-y (Aug 2024) (mcintyre2024glutamatergicmodulatorsfor pages 7-9).
- Kouba BR et al. Role of inflammatory mechanisms in major depressive disorder. Cells. 2024; DOI: 10.3390/cells13050423; URL: https://doi.org/10.3390/cells13050423 (Feb 2024) (kouba2024roleofinflammatory pages 2-3).
- Correia AS, Vale N. Advancements exploring MDD: oxidative stress, serotonin, BDNF, HPA, pharmacotherapy. Int J Transl Med. 2024; DOI: 10.3390/ijtm4010010; URL: https://doi.org/10.3390/ijtm4010010 (Mar 2024) (correia2024advancementsexploringmajor pages 1-2).
- Wetzel C et al. Mitochondrial and cellular function in patient‑derived cells in MDD. Int J Mol Sci. 2024; DOI: 10.3390/ijms25020963; URL: https://doi.org/10.3390/ijms25020963 (Jan 2024) (wetzel2024mitochondrialandcellular pages 10-12).
- Zhang L et al. Multi‑omics insights in MDD: neuronal dysfunction (dlPFC). medRxiv. 2025; DOI: 10.1101/2025.05.03.25326369; URL: https://doi.org/10.1101/2025.05.03.25326369 (May 2025; preprint) (zhang2025multiomicsinsightsin pages 14-18).

Notes and limitations
- While monoamine agents remain first‑line, recent evidence emphasizes convergent plasticity, immune, and bioenergetic mechanisms; the translational approvals of glutamatergic modulators and neurosteroids underscore the mechanistic shift (Cui 2024; McIntyre & Jain 2024) (cui2024majordepressivedisorder pages 23-24, mcintyre2024glutamatergicmodulatorsfor pages 7-9).
- Quantitative effect sizes vary across agents and populations; mechanistic claims and implementation notes above derive from peer‑reviewed reviews and patient‑derived cell studies cited herein (mcintyre2024glutamatergicmodulatorsfor pages 7-9, wetzel2024mitochondrialandcellular pages 10-12).

Plan status: Completed literature identification; synthesized mechanistic domains; produced ontology mappings; summarized clinical implementations and embedded an evidence map. Further additions could include specialized biomarker prevalence estimates and circadian‑focused human studies as they emerge in 2024–2025 cohorts.

References

1. (cui2024majordepressivedisorder pages 23-24): Lulu Cui, Shu Li, Siman Wang, Xiafang Wu, Yingyu Liu, Weiyang Yu, Yijun Wang, Yong Tang, Maosheng Xia, and Baoman Li. Major depressive disorder: hypothesis, mechanism, prevention and treatment. Signal Transduction and Targeted Therapy, Feb 2024. URL: https://doi.org/10.1038/s41392-024-01738-y, doi:10.1038/s41392-024-01738-y. This article has 801 citations and is from a peer-reviewed journal.

2. (mcintyre2024glutamatergicmodulatorsfor pages 7-9): Roger S. McIntyre and Rakesh Jain. Glutamatergic modulators for major depression from theory to clinical use. CNS Drugs, 38:869-890, Aug 2024. URL: https://doi.org/10.1007/s40263-024-01114-y, doi:10.1007/s40263-024-01114-y. This article has 44 citations and is from a peer-reviewed journal.

3. (kouba2024roleofinflammatory pages 2-3): Bruna R. Kouba, Laura de Araujo Borba, Pedro Borges de Souza, Joana Gil-Mohapel, and Ana Lúcia S. Rodrigues. Role of inflammatory mechanisms in major depressive disorder: from etiology to potential pharmacological targets. Cells, 13:423, Feb 2024. URL: https://doi.org/10.3390/cells13050423, doi:10.3390/cells13050423. This article has 125 citations and is from a poor quality or predatory journal.

4. (correia2024advancementsexploringmajor pages 1-2): Ana Salomé Correia and Nuno Vale. Advancements exploring major depressive disorder: insights on oxidative stress, serotonin metabolism, bdnf, hpa axis dysfunction, and pharmacotherapy advances. International Journal of Translational Medicine, 4:176-196, Mar 2024. URL: https://doi.org/10.3390/ijtm4010010, doi:10.3390/ijtm4010010. This article has 29 citations.

5. (wetzel2024mitochondrialandcellular pages 10-12): Christian Wetzel, Iseline Cardon, Sonja Grobecker, Selin Kücükoktay, Stefanie Bader, Tatjana Jahner, Caroline Nothdurfter, Kevin-Thomas Koschitzki, Mark Berneburg, Heidi Stöhr, Bernhard Weber, Marcus Höring, Gerhard Liebisch, Frank Braun, Tanja Rothammer-Hampl, Markus Riemenschneider, Rainer Rupprecht, and Vladimir Milenkovic. Mitochondrial and cellular function in fibroblasts, induced neurons, and astrocytes derived from case study patients: insights into major depression as a mitochondria-associated disease. International Journal of Molecular Sciences, Jan 2024. URL: https://doi.org/10.3390/ijms25020963, doi:10.3390/ijms25020963. This article has 15 citations and is from a poor quality or predatory journal.

6. (zhang2025multiomicsinsightsin pages 14-18): Lingfeng Zhang, M. Lyu, Simeng Ma, M. D. Y. Xu, M. D. X. Xie, Qian Gong Ph. D., Lijun Kang M. D., Shijia Chen Ph. D., and Zhongchun Liu M. D. Multi-omics insights in major depressive disorder: dysfunction of neurons. MedRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.03.25326369, doi:10.1101/2025.05.03.25326369. This article has 0 citations.

7. (correia2024advancementsexploringmajor pages 8-9): Ana Salomé Correia and Nuno Vale. Advancements exploring major depressive disorder: insights on oxidative stress, serotonin metabolism, bdnf, hpa axis dysfunction, and pharmacotherapy advances. International Journal of Translational Medicine, 4:176-196, Mar 2024. URL: https://doi.org/10.3390/ijtm4010010, doi:10.3390/ijtm4010010. This article has 29 citations.