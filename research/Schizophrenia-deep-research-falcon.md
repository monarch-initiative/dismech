---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:42:26.817717'
end_time: '2025-12-15T09:48:11.356081'
duration_seconds: 344.54
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Schizophrenia
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Schizophrenia
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Schizophrenia**.
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
- **Disease Name:** Schizophrenia
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Schizophrenia**.
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


Plan
- Identify and synthesize 2023–2024 evidence on molecular/cellular mechanisms in schizophrenia (neurotransmitters, immune–synapse pruning, myelin/oligodendrocytes, mitochondria/oxidative stress, calcium signaling), emphasizing expert reviews and mechanistic studies with URLs.
- Map key genes/proteins, metabolites, cell types, and regions with ontology terms and link them to disrupted GO processes and cellular components.
- Propose a staged disease progression model from neurodevelopment to clinical onset, connecting mechanisms to clinical phenotypes and available biomarkers.
- Summarize recent applications/therapeutics and expert perspectives; provide statistics where available.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Schizophrenia
- MONDO ID: MONDO:0005090
- Category: Psychiatric

1) Core Pathophysiology (current understanding)
- Polygenic liability and synaptic biology: Schizophrenia is highly polygenic; common variation now explains “more than 20% of the liability” in aggregate, with risk genes enriched in synaptic pathways and including DRD2, consistent with antipsychotic mechanisms (direct quote: “now we can explain more than 20% of the liability to schizophrenia by considering all analyzable common genetic variants,” Molecular Psychiatry, Mar 2023; URL: https://doi.org/10.1038/s41380-023-02005-2) (nakamura2023themolecularpathology pages 16-16).
- Dopamine and glutamate interplay with cortical E/I imbalance: Contemporary models integrate mesolimbic hyperdopaminergia (positive symptoms) with cortical NMDA receptor hypofunction on GABAergic/parvalbumin (PV) interneurons, producing disinhibition, excitatory/inhibitory (E/I) imbalance, and downstream dopaminergic dysregulation; ketamine/PCP reproduce psychosis-like states; D-serine (an NMDA co-agonist) and kynurenine/kynurenic acid metabolism abnormalities contribute to NMDA hypofunction (Int J Mol Sci, Oct 2024; URL: https://doi.org/10.3390/ijms251910668) (zhang2024advancesinthe pages 13-14, rawani2024theunderlyingneurobiological pages 4-5).
- Immune–microglial complement signaling and synaptic pruning: Genetic and experimental evidence implicate complement component C4A and microglial CR3 pathways in excessive synaptic elimination, with human and model-system data converging on complement-mediated pruning as a driver of synapse loss (Frontiers in Cellular Neuroscience, Mar 2024; URL: https://doi.org/10.3389/fncel.2024.1345349) (hartmann2024microglianeuroninteractionsin pages 16-16).
- Oligodendrocyte/myelin and network dysconnectivity: Myelin/oligodendrocyte abnormalities and white-matter changes are repeatedly observed and conceptually linked to dysconnectivity across brain regions (Antioxidants, Jun 2024; URL: https://doi.org/10.3390/antiox13060709) (rawani2024theunderlyingneurobiological pages 15-16, stanca2024thecellulardysfunction pages 1-2).
- Mitochondrial–oxidative stress axis: Bioenergetic deficits (e.g., complex I inhibition), decreased glutathione, increased lactate, and inflammatory cytokines support a feed-forward cycle linking mitochondrial dysfunction, oxidative/nitrosative stress, and neuroinflammation; excessive Ca2+ influx via NMDARs can overload mitochondria and trigger cell-death signaling (Antioxidants, Jun 2024; URL: https://doi.org/10.3390/antiox13060709) (rawani2024theunderlyingneurobiological pages 15-16, rawani2024theunderlyingneurobiological pages 4-5).
- Neurovascular/BBB dysfunction: Increased BBB permeability (elevated CSF albumin/immunoglobulins) and neurovascular unit abnormalities (endothelial cells, pericytes, astrocytes) are reported and positioned upstream of neurotransmitter dyshomeostasis (Int J Mol Sci, Jan 2024; URL: https://doi.org/10.3390/ijms25021250) (stanca2024thecellulardysfunction pages 1-2).

2) Key Molecular Players
- Genes/proteins (HGNC):
  - DRD2 (dopamine D2 receptor; antipsychotic target; GWAS-implicated) (Molecular Psychiatry, 2023; URL above) (nakamura2023themolecularpathology pages 16-16).
  - GRIN1/GRIN2A (NMDAR subunits), GAD1 (GAD67), RELN (Reelin) (NMDA/PV interneuron dysfunction and epigenetic regulation discussed) (Int J Mol Sci, 2024; URL above; Antioxidants, 2024; URL above) (zhang2024advancesinthe pages 13-14, rawani2024theunderlyingneurobiological pages 4-5, rawani2024theunderlyingneurobiological pages 25-26).
  - C4A (complement component 4A), C3, ITGAM/CD11b (CR3) (microglial complement-mediated synaptic pruning) (Frontiers in Cellular Neuroscience, 2024; URL above) (hartmann2024microglianeuroninteractionsin pages 16-16).
  - Myelin/oligodendrocyte-associated proteins (conceptual involvement; oligodendroglial/myelination deficits) (Antioxidants, 2024; URL above) (rawani2024theunderlyingneurobiological pages 15-16).
- Chemical entities (CHEBI):
  - Dopamine (CHEBI:18243), glutamate (CHEBI:29985), GABA (CHEBI:16865) (core neurotransmitters) (rawani2024theunderlyingneurobiological pages 4-5, correll2024whatremainsto pages 1-2).
  - D-serine (CHEBI:17115), kynurenic acid (CHEBI:17368), kynurenine (CHEBI:30785) (NMDAR co-agonist and KP metabolites) (Int J Mol Sci, 2024; URL above) (zhang2024advancesinthe pages 13-14).
- Cell types (CL):
  - PV interneurons (CL:0000099, parvalbumin-positive GABAergic interneurons; NMDA hypofunction/disinhibition) (Int J Mol Sci, 2024; URL above) (zhang2024advancesinthe pages 13-14).
  - Microglia (CL:0000129; complement-dependent synaptic pruning) (Frontiers in Cellular Neuroscience, 2024) (hartmann2024microglianeuroninteractionsin pages 16-16).
  - Astrocytes (CL:0000127), endothelial cells (CL:0000115), pericytes (CL:0000669) (neurovascular/BBB) (Int J Mol Sci, 2024; URL above) (stanca2024thecellulardysfunction pages 1-2).
  - Oligodendrocytes (CL:0000128) (myelin deficits) (Antioxidants, 2024; URL above) (rawani2024theunderlyingneurobiological pages 15-16).
- Anatomical locations (UBERON):
  - Prefrontal cortex (UBERON:0003126), hippocampus (UBERON:0001954), thalamus (UBERON:0001897) (regions linked to cognition and network communication; E/I imbalance, inflammation, and myelin changes) (rawani2024theunderlyingneurobiological pages 4-5, rawani2024theunderlyingneurobiological pages 15-16, stanca2024thecellulardysfunction pages 1-2).

3) Biological Processes (GO terms) disrupted
- Glutamatergic synaptic transmission and plasticity (GO:0098978; GO:0060291 LTP): NMDA hypofunction, co-agonist deficiency, and KP metabolite modulation (zhang2024advancesinthe pages 13-14).
- GABAergic synaptic transmission and interneuron-mediated inhibition (GO:0098982): PV interneuron dysfunction and cortical disinhibition/E/I imbalance (zhang2024advancesinthe pages 13-14, rawani2024theunderlyingneurobiological pages 4-5).
- Dopamine signaling (GO:0007212) and presynaptic modulation by cortical inputs (hyperdopaminergia in mesolimbic circuits) (correll2024whatremainsto pages 1-2, rawani2024theunderlyingneurobiological pages 4-5).
- Complement activation and synaptic pruning (GO:0006956; GO:0098883): microglia–CR3–C4/C3 pathways (hartmann2024microglianeuroninteractionsin pages 16-16).
- Myelination and axon ensheathment (GO:0042552; GO:0008366): oligodendrocyte disruption and dysconnectivity (rawani2024theunderlyingneurobiological pages 15-16).
- Mitochondrial electron transport/oxidative phosphorylation (GO:0006119) and cellular response to oxidative stress (GO:0034599) (rawani2024theunderlyingneurobiological pages 15-16).
- Regulation of blood–brain barrier permeability and endothelial junction organization (e.g., GO:0071605, GO:0005911 related components): BBB leakage and neurovascular unit dysfunction (stanca2024thecellulardysfunction pages 1-2).

4) Cellular Components (where key processes occur)
- Postsynaptic density (GO:0014069) and glutamatergic synapse (GO:0098978) for NMDA-dependent signaling (zhang2024advancesinthe pages 13-14).
- Presynaptic active zone (GO:0048786) and dopaminergic terminals (mesostriatal/mesolimbic) (correll2024whatremainsto pages 1-2).
- Microglial phagocytic machinery in perisynaptic microdomains; complement opsonins at synapses (hartmann2024microglianeuroninteractionsin pages 16-16).
- Myelin sheath (GO:0043209) and nodes of Ranvier (GO:0033268) for conduction/dysconnectivity (rawani2024theunderlyingneurobiological pages 15-16).
- Mitochondrion (GO:0005739) as a hub for redox-bioenergetics and Ca2+-induced injury (rawani2024theunderlyingneurobiological pages 15-16).
- Endothelial cell–cell junctions and astrocytic endfeet at BBB (stanca2024thecellulardysfunction pages 1-2).

5) Disease Progression (staged model)
- Neurodevelopmental priming: Genetic liability (common and rare) plus early-life immune/inflammatory exposures perturb cortical development, interneuron maturation, and synaptic/myelin programs; polygenic architecture “explains more than 20% of liability” (Molecular Psychiatry, 2023; URL above) (nakamura2023themolecularpathology pages 16-16). Epigenetic alterations impacting NMDARs, GABAergic markers (GAD67), and reelin are noted (Antioxidants, 2024; URL: https://doi.org/10.3390/antiox13060709) (rawani2024theunderlyingneurobiological pages 25-26).
- Adolescent critical period: Excessive complement-tagged synaptic pruning by microglia (C4A/C3–CR3) and NMDA hypofunction on PV interneurons drive cortical E/I imbalance; concurrent oligodendrocyte/myelin vulnerability and BBB changes may exacerbate dysconnectivity and neuroinflammation (Frontiers in Cellular Neuroscience, 2024; Int J Mol Sci, 2024; URLs above) (hartmann2024microglianeuroninteractionsin pages 16-16, stanca2024thecellulardysfunction pages 1-2, zhang2024advancesinthe pages 13-14).
- Prodrome to first-episode psychosis: Emergence of cognitive/negative symptoms with cortical disinhibition and glutamatergic dysregulation; mesolimbic hyperdopaminergia manifests as positive symptoms (Biomolecules, Jul 2024; URL: https://doi.org/10.3390/biom14080906) (correll2024whatremainsto pages 1-2, rawani2024theunderlyingneurobiological pages 4-5).
- Chronic course: Persistent synaptic loss, redox–mitochondrial stress, and myelin/white-matter alterations contribute to refractory negative and cognitive symptoms; ongoing low-grade inflammation and BBB dysfunction may maintain pathophysiology (Antioxidants, 2024; Int J Mol Sci, 2024; URLs above) (rawani2024theunderlyingneurobiological pages 15-16, stanca2024thecellulardysfunction pages 1-2).

6) Phenotypic Manifestations (linkage to mechanisms)
- Positive symptoms (hallucinations/delusions): Most directly related to striatal/mesolimbic dopamine excess; antipsychotics work as “postsynaptic dopamine antagonists” (Biomolecules, Jul 2024; URL above) (correll2024whatremainsto pages 1-2).
- Negative and cognitive symptoms: Associated with cortical NMDA hypofunction and PV interneuron-mediated disinhibition (E/I imbalance) leading to impairments in working memory/executive function; D-serine reduction and KP metabolite elevations (kynurenic acid) are implicated (Int J Mol Sci, Oct 2024; URL above) (zhang2024advancesinthe pages 13-14). “Ketamine/PCP” models reproduce cognitive and negative symptom domains via NMDAR blockade (rawani2024theunderlyingneurobiological pages 4-5).
- Functional dysconnectivity: Oligodendrocyte/myelin deficits and inflammation contribute to large-scale network dysconnectivity underlying broad symptom burden (Antioxidants, Jun 2024; URL above) (rawani2024theunderlyingneurobiological pages 15-16).

Applications and Real-World Implementations (biomarkers and therapeutics)
- Biomarkers:
  - CSF/metabolic redox markers: Increased lactate and decreased glutathione have been reported in brain/CSF in schizophrenia, consistent with bioenergetic–oxidative stress (Antioxidants, Jun 2024; URL above) (rawani2024theunderlyingneurobiological pages 15-16).
  - Neuroinflammatory cytokines (e.g., IL‑6, IL‑8, TNF‑α) are elevated in first-episode and chronic cases (Antioxidants, Jun 2024; URL above) (rawani2024theunderlyingneurobiological pages 4-5).
  - BBB leakage indices: Elevated CSF albumin/immunoglobulins indicating increased BBB permeability (Int J Mol Sci, Jan 2024; URL above) (stanca2024thecellulardysfunction pages 1-2).
- Therapeutic developments:
  - Dopaminergic antagonism remains the cornerstone for positive symptoms but leaves cognitive/negative symptoms insufficiently treated (Biomolecules, Jul 2024; URL above) (correll2024whatremainsto pages 1-2).
  - Glutamatergic strategies (e.g., NMDAR co-agonists, glycine transporter or D‑amino acid oxidase inhibitors, mGluR modulators) are being advanced to target cognition and negative symptoms (Int J Mol Sci, Oct 2024; URL above) (zhang2024advancesinthe pages 13-14).
  - Novel modalities: “Molecular polypharmacy” and biased signaling; KarXT (xanomeline + trospium) exemplifies circuit-/network-minded approaches beyond D2 antagonism (Biomolecules, Jul 2024; URL above) (correll2024whatremainsto pages 1-2).

Relevant Statistics and Data
- Prevalence: “approximately 1% of the global population,” emphasizing disability and unmet needs (Biomolecules, Jul 2024; URL above) (correll2024whatremainsto pages 1-2).
- Genetics: “now we can explain more than 20% of the liability” from common variants in aggregate; DRD2 is a validated GWAS target reflecting monoaminergic involvement (Molecular Psychiatry, Mar 2023; URL above) (nakamura2023themolecularpathology pages 16-16).

Expert Opinions and Analysis
- Therapeutic perspective: Correll et al. emphasize that “schizophrenia’s pathophysiology is not solely reliant on neurotransmitter–receptor interactions,” and promote circuit-level targets, biased agonism, and multi-target strategies to address cognitive/negative symptoms and treatment resistance (Biomolecules, Jul 2024; URL above) (correll2024whatremainsto pages 1-2).
- Mechanistic synthesis: Reviews converge that neurotransmission dysregulation (dopamine–glutamate–GABA), neuroinflammation (microglia/complement), redox–mitochondrial stress, and myelin/BBB pathology are interdependent domains that jointly drive clinical heterogeneity (Antioxidants, Jun 2024; URL above; Int J Mol Sci, Jan/Oct 2024; URLs above) (rawani2024theunderlyingneurobiological pages 15-16, stanca2024thecellulardysfunction pages 1-2, zhang2024advancesinthe pages 13-14).

Structured Annotations for Knowledge Base
- Gene/protein (HGNC): DRD2; GRIN1/GRIN2A; GAD1 (GAD67); RELN; C4A; C3; ITGAM (CR3/CD11b). Evidence: GWAS (DRD2) and mechanistic reviews (complement, NMDA, PV interneuron) (nakamura2023themolecularpathology pages 16-16, zhang2024advancesinthe pages 13-14, hartmann2024microglianeuroninteractionsin pages 16-16).
- Biological process (GO): glutamatergic synaptic transmission (GO:0098978); GABAergic synaptic transmission (GO:0098982); complement activation (GO:0006956); synaptic pruning (GO:0098883); myelination (GO:0042552); oxidative phosphorylation (GO:0006119); cellular response to oxidative stress (GO:0034599); regulation of BBB permeability (GO:0071605) (zhang2024advancesinthe pages 13-14, hartmann2024microglianeuroninteractionsin pages 16-16, rawani2024theunderlyingneurobiological pages 15-16, stanca2024thecellulardysfunction pages 1-2).
- Cellular component (GO): postsynaptic density (GO:0014069); glutamatergic synapse (GO:0098978); myelin sheath (GO:0043209); mitochondrion (GO:0005739); endothelial cell–cell junction (GO:0005911-related) (zhang2024advancesinthe pages 13-14, rawani2024theunderlyingneurobiological pages 15-16, stanca2024thecellulardysfunction pages 1-2).
- Cell types (CL): PV interneurons (CL:0000099); microglia (CL:0000129); astrocytes (CL:0000127); endothelial cells (CL:0000115); oligodendrocytes (CL:0000128) (zhang2024advancesinthe pages 13-14, hartmann2024microglianeuroninteractionsin pages 16-16, stanca2024thecellulardysfunction pages 1-2, rawani2024theunderlyingneurobiological pages 15-16).
- Anatomical locations (UBERON): prefrontal cortex (UBERON:0003126); hippocampus (UBERON:0001954); thalamus (UBERON:0001897) (rawani2024theunderlyingneurobiological pages 4-5, rawani2024theunderlyingneurobiological pages 15-16, stanca2024thecellulardysfunction pages 1-2).
- Phenotype associations (HP): Positive psychotic symptoms (HP:0031464); Negative symptoms (HP:0031466); Cognitive impairment (HP:0100543). Mechanistic links summarized above (zhang2024advancesinthe pages 13-14, correll2024whatremainsto pages 1-2, rawani2024theunderlyingneurobiological pages 4-5).
- Chemical entities (CHEBI): dopamine (CHEBI:18243); glutamate (CHEBI:29985); GABA (CHEBI:16865); D-serine (CHEBI:17115); kynurenic acid (CHEBI:17368); kynurenine (CHEBI:30785) (zhang2024advancesinthe pages 13-14, rawani2024theunderlyingneurobiological pages 4-5).

Directly quoted supporting statements
- “now we can explain more than 20% of the liability to schizophrenia by considering all analyzable common genetic variants” (Molecular Psychiatry, Mar 2023; URL: https://doi.org/10.1038/s41380-023-02005-2) (nakamura2023themolecularpathology pages 16-16).
- Postsynaptic dopamine antagonists have been “the cornerstone” of treatment, yet “significant challenges remain,” motivating network- and biased-signaling–based approaches (Biomolecules, Jul 2024; URL: https://doi.org/10.3390/biom14080906) (correll2024whatremainsto pages 1-2).

Limitations and gaps
- Many biomarker findings (e.g., cytokine panels, redox markers) require replication in large, medication-naïve cohorts. Complement-pruning mechanisms, while strongly supported, still need human in vivo biomarkers to stratify subtypes. Nonetheless, convergent 2023–2024 evidence corroborates multi-domain pathophysiology spanning neurotransmission, immune pruning, myelin/BBB, and redox–mitochondria.

References (URLs and dates)
- Nakamura T, Takata A. The molecular pathology of schizophrenia… Molecular Psychiatry, Mar 2023. URL: https://doi.org/10.1038/s41380-023-02005-2 (nakamura2023themolecularpathology pages 16-16).
- Zhang T et al. Advances in the treatment of cognitive impairment in schizophrenia: targeting NMDA receptor pathways. Int J Mol Sci, Oct 2024. URL: https://doi.org/10.3390/ijms251910668 (zhang2024advancesinthe pages 13-14).
- Correll CU et al. What remains to be discovered in schizophrenia therapeutics… Biomolecules, Jul 2024. URL: https://doi.org/10.3390/biom14080906 (correll2024whatremainsto pages 1-2).
- Rawani NS et al. The underlying neurobiological mechanisms of psychosis… Antioxidants, Jun 2024. URL: https://doi.org/10.3390/antiox13060709 (rawani2024theunderlyingneurobiological pages 15-16, rawani2024theunderlyingneurobiological pages 4-5, rawani2024theunderlyingneurobiological pages 25-26).
- Stanca S et al. The cellular dysfunction of the brain–blood barrier… Int J Mol Sci, Jan 2024. URL: https://doi.org/10.3390/ijms25021250 (stanca2024thecellulardysfunction pages 1-2).
- Hartmann S-M et al. Microglia–neuron interactions in schizophrenia. Frontiers in Cellular Neuroscience, Mar 2024. URL: https://doi.org/10.3389/fncel.2024.1345349 (hartmann2024microglianeuroninteractionsin pages 16-16).

References

1. (nakamura2023themolecularpathology pages 16-16): Takumi Nakamura and Atsushi Takata. The molecular pathology of schizophrenia: an overview of existing knowledge and new directions for future research. Molecular Psychiatry, 28:1868-1889, Mar 2023. URL: https://doi.org/10.1038/s41380-023-02005-2, doi:10.1038/s41380-023-02005-2. This article has 51 citations and is from a highest quality peer-reviewed journal.

2. (zhang2024advancesinthe pages 13-14): Ting Zhang, Chang Liu, Ning Zhong, Yichen Wang, Yiyun Huang, and Xiaoqin Zhang. Advances in the treatment of cognitive impairment in schizophrenia: targeting nmda receptor pathways. International Journal of Molecular Sciences, 25:10668, Oct 2024. URL: https://doi.org/10.3390/ijms251910668, doi:10.3390/ijms251910668. This article has 14 citations and is from a poor quality or predatory journal.

3. (rawani2024theunderlyingneurobiological pages 4-5): Neha S. Rawani, Allen W. Chan, Serdar M. Dursun, and Glen B. Baker. The underlying neurobiological mechanisms of psychosis: focus on neurotransmission dysregulation, neuroinflammation, oxidative stress, and mitochondrial dysfunction. Antioxidants, 13:709, Jun 2024. URL: https://doi.org/10.3390/antiox13060709, doi:10.3390/antiox13060709. This article has 55 citations and is from a poor quality or predatory journal.

4. (hartmann2024microglianeuroninteractionsin pages 16-16): Sophia-Marie Hartmann, Johanna Heider, Richard Wüst, Andreas J. Fallgatter, and Hansjürgen Volkmer. Microglia-neuron interactions in schizophrenia. Frontiers in Cellular Neuroscience, Mar 2024. URL: https://doi.org/10.3389/fncel.2024.1345349, doi:10.3389/fncel.2024.1345349. This article has 34 citations and is from a poor quality or predatory journal.

5. (rawani2024theunderlyingneurobiological pages 15-16): Neha S. Rawani, Allen W. Chan, Serdar M. Dursun, and Glen B. Baker. The underlying neurobiological mechanisms of psychosis: focus on neurotransmission dysregulation, neuroinflammation, oxidative stress, and mitochondrial dysfunction. Antioxidants, 13:709, Jun 2024. URL: https://doi.org/10.3390/antiox13060709, doi:10.3390/antiox13060709. This article has 55 citations and is from a poor quality or predatory journal.

6. (stanca2024thecellulardysfunction pages 1-2): Stefano Stanca, Martina Rossetti, Leona Bokulic Panichi, and Paolo Bongioanni. The cellular dysfunction of the brain–blood barrier from endothelial cells to astrocytes: the pathway towards neurotransmitter impairment in schizophrenia. International Journal of Molecular Sciences, 25:1250, Jan 2024. URL: https://doi.org/10.3390/ijms25021250, doi:10.3390/ijms25021250. This article has 17 citations and is from a poor quality or predatory journal.

7. (rawani2024theunderlyingneurobiological pages 25-26): Neha S. Rawani, Allen W. Chan, Serdar M. Dursun, and Glen B. Baker. The underlying neurobiological mechanisms of psychosis: focus on neurotransmission dysregulation, neuroinflammation, oxidative stress, and mitochondrial dysfunction. Antioxidants, 13:709, Jun 2024. URL: https://doi.org/10.3390/antiox13060709, doi:10.3390/antiox13060709. This article has 55 citations and is from a poor quality or predatory journal.

8. (correll2024whatremainsto pages 1-2): Christoph U. Correll, Massimo Tusconi, Mauro Giovanni Carta, and Serdar M. Dursun. What remains to be discovered in schizophrenia therapeutics: contributions by advancing the molecular mechanisms of drugs for psychosis and schizophrenia. Biomolecules, 14:906, Jul 2024. URL: https://doi.org/10.3390/biom14080906, doi:10.3390/biom14080906. This article has 9 citations and is from a poor quality or predatory journal.