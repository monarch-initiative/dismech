---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-19T23:52:16.367891'
end_time: '2026-03-20T00:05:25.052529'
duration_seconds: 788.68
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Kleefstra Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Kleefstra Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Kleefstra Syndrome**.
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
- **Disease Name:** Kleefstra Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Kleefstra Syndrome**.
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


## Comprehensive Research Report: Kleefstra Syndrome Pathophysiology (EHMT1 haploinsufficiency)

### 0. Disease identifiers and scope
**Disease**: Kleefstra syndrome (classically “Kleefstra syndrome 1”, due to 9q34.3 microdeletion including **EHMT1** or intragenic pathogenic **EHMT1** variants). (frega2019neuronalnetworkdysfunction pages 1-2, morison2024expandingthephenotype pages 5-7)  
**MONDO ID**: **MONDO:0012455** (Open Targets disease entity “Kleefstra syndrome”). (balogh2024establishmentofhuman media 76d9168d)  
**Genetic category**: Mendelian (autosomal dominant; typically de novo). (frega2019neuronalnetworkdysfunction pages 1-2, morison2024expandingthephenotype pages 5-7)  

This report focuses on molecular/cellular mechanisms linked to **EHMT1 haploinsufficiency** and its downstream neurodevelopmental consequences, emphasizing 2023–2024 literature while incorporating key mechanistic primary studies that define core pathways.

---

## 1) Key concepts and definitions (current understanding)

### 1.1 Core genetic and epigenetic mechanism
**EHMT1 (euchromatic histone lysine methyltransferase 1)** encodes a chromatin-modifying enzyme that functions with **EHMT2 (G9a)** to methylate histone H3 lysine 9, producing repressive marks **H3K9me1/H3K9me2** associated with transcriptional silencing and chromatin compaction. (frega2019neuronalnetworkdysfunction pages 1-2, hnizda2025denovoheterozygous pages 1-6)  
Kleefstra syndrome results from **heterozygous loss-of-function of EHMT1** (haploinsufficiency), causing reduced EHMT1 dosage and broad transcriptional dysregulation during neurodevelopment. (frega2019neuronalnetworkdysfunction pages 1-2, rots2024comprehensiveehmt1variants pages 1-3)  

### 1.2 Pathophysiology as a “chromatinopathy” → circuit disorder
A recurring conceptual model is: **epigenetic dysregulation → altered neuronal differentiation/maturation programs → synaptic dysfunction → network-level dysfunction → neurodevelopmental phenotypes** (ID/ASD, speech/language impairment, hypotonia, epilepsy, etc.). Direct evidence for the circuit step is strong in human iPSC-derived neuronal network models and in Ehmt1+/− mice. (frega2019neuronalnetworkdysfunction pages 1-2, balogh2024establishmentofhumana pages 1-2)

### 1.3 Molecular biomarker concept: DNA methylation episignature
Because EHMT1 affects chromatin and gene regulation, peripheral blood **DNA methylation (DNAm) “episignatures”** can serve as molecular fingerprints aiding diagnosis and variant interpretation. A large 2024 AJHG cohort used DNAm signatures to reclassify variants and refine genotype–phenotype relationships. (rots2024comprehensiveehmt1variants pages 1-3)

---

## 2) Core pathophysiology: primary mechanisms, dysregulated pathways, cellular processes

### 2.1 Loss of H3K9me2 repression and specific promoter de-repression (GRIN1)
A key mechanistic link is the **EHMT1 → H3K9me2 → GRIN1/NMDAR1** axis. In a human iPSC-derived excitatory cortical neuron model, Kleefstra syndrome neuronal networks showed a distinctive bursting phenotype, and the authors report:

- **Direct quote (abstract)**: “We show that these changes are mediated by upregulation of NMDA receptor (NMDAR) subunit 1 correlating with reduced deposition of the repressive H3K9me2 mark, the catalytic product of EHMT1, at the GRIN1 promoter.” (Frega et al., Nat Commun 2019; DOI: https://doi.org/10.1038/s41467-019-12947-3; PMID: **31695196**) (frega2019neuronalnetworkdysfunction pages 1-2)

Thus, EHMT1 deficiency can de-repress specific neuronal genes via reduced local H3K9me2, providing a concrete example of how chromatin dysregulation becomes a synaptic/circuit phenotype.

### 2.2 Neuronal network dysfunction and excitatory/inhibitory balance
**Network-level phenotypes** in KS human iPSC-derived neuronal networks include **reduced burst rate, longer burst duration, and increased temporal irregularity**, with causal evidence from CRISPR-engineered EHMT1 disruption and pharmacological rescue by NMDAR antagonism. (frega2019neuronalnetworkdysfunction pages 1-2, frega2019neuronalnetworkdysfunction pages 5-6)  
In addition to NMDAR-driven effects, homeostatic plasticity adaptations are implicated: in KS networks, transient NMDAR blockade triggered homeostatic changes consistent with synaptic upscaling involving GluA2-lacking AMPAR insertion (inferred from Naspm sensitivity during recovery). (frega2019neuronalnetworkdysfunction pages 5-6)

### 2.3 REST/NRSF–miRNA axis: dysregulated neuronal gene repression and developmental timing
A second major mechanism links EHMT1 to the neuron-specific transcriptional repressor **REST (NRSF)** through microRNA-mediated regulation. Alsaqati et al. show that EHMT1 inhibition or haploinsufficiency leads to **derepression of multiple miRNAs that target REST**, reducing REST protein and de-repressing neuronal gene programs prematurely.

- Quantitative regulatory features include: **56 miRNAs upregulated >2.5-fold** after EHMT1 inhibition; **11** of these were predicted REST-targeting miRNAs (including miR-142, miR-153-1, miR-26a-2). (Alsaqati et al., Transl Psychiatry 2022; DOI: https://doi.org/10.1038/s41398-022-02199-z; PMID: **36241675**) (alsaqati2022nrsfrestliesat pages 3-5)
- Mechanistic detail: ChIP-qPCR did **not** show H3K9me2 at the REST promoter, but did detect H3K9me2 at miRNA TSSs (e.g., miR-142/153/26a), consistent with EHMT1 controlling REST indirectly via miRNA repression. (alsaqati2022nrsfrestliesat pages 3-5)
- Functional rescue: expressing a miRNA-insensitive REST transcript (REST-ΔUTR) prevented aberrant REST-target activation, supporting causality. (alsaqati2022nrsfrestliesat pages 3-5)

This axis provides a molecular explanation for **altered neurodevelopmental timing** (premature neuronal gene expression and differentiation trajectories) and a bridge between epigenetic and post-transcriptional regulation. (alsaqati2022nrsfrestliesat pages 1-2, alsaqati2022nrsfrestliesat pages 3-5)

### 2.4 Synaptogenesis/connectivity deficits despite neurite overgrowth
In a 2024 iPSC-derived 3D cortical neurosphere (“corticoid”) model of KS, neurite outgrowth was increased, yet synaptic protein markers indicated reduced synaptic maturation/connectivity:
- **PSD95** and **synaptophysin (SYP)** expression in neurites were lower in KS; PSD95 reduction reached significance (**p = 0.01**). (Balogh et al., Sci Rep 2024; DOI: https://doi.org/10.1038/s41598-024-72791-4) (balogh2024establishmentofhumana pages 5-7)

This supports a concept of **mis-timed or mis-specified neurodevelopment**: neuronal projections may form exuberantly while synapse assembly/stabilization is impaired.

### 2.5 Metabolic/oxidative stress vulnerability as a modifier mechanism
Balogh et al. extended KS pathophysiology into metabolic/toxicant sensitivity, with two notable results:
1) KS neural cultures showed differential toxicant sensitivity depending on developmental stage (NPC vs mature 3D spheroids), and KS 3D spheroids were particularly sensitive to paraquat. (balogh2024establishmentofhumana pages 5-7, balogh2024establishmentofhuman media d449cbce)  
2) **LDHA** transcript was significantly downregulated in KS NPCs (**p = 0.03**) and KS 3D spheroids (**p = 0.002**), suggesting altered metabolic adaptation to oxidative stress conditions. (balogh2024establishmentofhumana pages 7-8)

These findings motivate investigation of **energy metabolism and oxidative stress response** as potential contributors to variable neurodevelopmental outcomes and environmental sensitivity.

---

## 3) Key molecular players (genes/proteins, chemicals, cells, anatomy)

### 3.1 Genes/proteins (causal and mechanistic)
- **EHMT1 (HGNC: EHMT1)**: causal gene; H3K9 methyltransferase; key epigenetic regulator. (frega2019neuronalnetworkdysfunction pages 1-2, rots2024comprehensiveehmt1variants pages 1-3)
- **EHMT2 (G9a)**: functional partner; shared enzymatic complex with EHMT1. (frega2019neuronalnetworkdysfunction pages 1-2, hnizda2025denovoheterozygous pages 1-6)
- **GRIN1 / NMDAR1**: de-repressed in EHMT1 deficiency; drives network dysfunction and pharmacologically rescuable hyperfunction. (frega2019neuronalnetworkdysfunction pages 1-2)
- **REST/NRSF**: reduced at protein level via miRNA derepression in EHMT1 deficiency; de-represses neuronal target genes and shifts neurodevelopmental timing. (alsaqati2022nrsfrestliesat pages 3-5, alsaqati2022nrsfrestliesat pages 1-2)
- **BDNF**: increased expression associated with altered neurite outgrowth in KS spheroids and referenced as REST-linked. (balogh2024establishmentofhumana pages 7-8)
- Synaptic markers: **DLG4 (PSD95)**, **SYP**. (balogh2024establishmentofhumana pages 5-7)
- Metabolic genes: **LDHA**, **LDHB** (LDHA downregulated in KS). (balogh2024establishmentofhumana pages 7-8)

Additionally, Open Targets lists **KMT2C** as strongly associated with the Kleefstra syndrome spectrum (reflecting “Kleefstra syndrome 2” concept in literature), although canonical KS is EHMT1-driven. (balogh2024establishmentofhuman media 76d9168d)

### 3.2 Chemical entities and small molecules relevant to mechanisms
- **NMDAR antagonists** used experimentally for rescue: D-AP5/APV (experimental reagent); NMDA pathway involvement. (frega2019neuronalnetworkdysfunction pages 5-6, frega2019neuronalnetworkdysfunction pages 1-2)
- Toxicants for differential sensitivity assays: **paraquat**, **rotenone**, **bardoxolone methyl (CDDO-Me)**, **doxorubicin**. (balogh2024establishmentofhumana pages 5-7, balogh2024establishmentofhuman media d449cbce)

### 3.3 Cell types (primary affected/implicated)
Mechanistic studies implicate **human excitatory cortical neurons** and developing neural progenitors, with evidence for neuronal subtype shifts in 3D systems:
- excitatory cortical neurons derived from iPSCs (network phenotypes). (frega2019neuronalnetworkdysfunction pages 1-2)
- cortical spheroids enriched for **VGLUT1/2+ glutamatergic** and **ChAT+ cholinergic** neurons, with underrepresentation of **TH+ catecholaminergic** neurons. (balogh2024establishmentofhumana pages 1-2, balogh2024establishmentofhumana pages 7-8)

### 3.4 Anatomical systems and tissues
- Central nervous system emphasis: **cerebral cortex** (most direct model evidence) and broader brain networks. (frega2019neuronalnetworkdysfunction pages 1-2, balogh2024establishmentofhumana pages 1-2)
- Multi-system involvement in patients includes cardiac conditions and sensory impairments, consistent with pleiotropic roles of EHMT1. (morison2024expandingthephenotype pages 5-7)

---

## 4) Biological processes and cellular components (GO-oriented)

Ontology-oriented candidate annotations are summarized in the embedded table below.

| Mechanism | Key gene/protein (HGNC) | Suggested pathway/process (GO BP) | Cellular component (GO CC) | Principal cell type(s) (CL) | Anatomy (UBERON) | Key chemicals/small molecules (CHEBI) | Supporting evidence + PMID |
|---|---|---|---|---|---|---|---|
| EHMT1 haploinsufficiency reduces EHMT1/EHMT2-mediated H3K9me2 repression, altering transcriptional control | **EHMT1**, **EHMT2**, Histone H3, **GRIN1** | histone H3-K9 dimethylation; negative regulation of transcription by RNA polymerase II; chromatin organization | nucleus; chromatin; nucleoplasm | excitatory cortical neuron (CL:0000540) | cerebral cortex (UBERON:0000956); brain (UBERON:0000955) | S-adenosyl-L-methionine / SAM (CHEBI:15414) | KS iNeurons show reduced H3K9me2; EHMT1 is causal for KLEFS and functions with EHMT2 as H3K9 methyltransferase (frega2019neuronalnetworkdysfunction pages 1-2, hnizda2025denovoheterozygous pages 1-6, rots2024comprehensiveehmt1variants pages 1-3) PMID: 31695196 |
| **GRIN1/NMDAR1** upregulation drives abnormal network bursting; NMDAR antagonism rescues network phenotype | **GRIN1**, **EHMT1** | regulation of postsynaptic membrane potential; synaptic signaling; neuronal network activity; homeostatic synaptic plasticity | postsynaptic density; glutamatergic synapse; neuronal cell body | excitatory neuron (CL:0000540) | cerebral cortex (UBERON:0000956) | NMDA (CHEBI:16261); D-AP5/APV (CHEBI not established here); Naspm (CHEBI not established here) | “reduced deposition of the repressive H3K9me2 mark… at the GRIN1 promoter” with reduced burst rate, longer duration, irregularity; D-AP5 suppressed KS network bursting and rescued phenotype (frega2019neuronalnetworkdysfunction pages 1-2, frega2019neuronalnetworkdysfunction pages 5-6, balogh2024establishmentofhumana pages 1-2) PMID: 31695196 |
| EHMT1 loss decreases **REST/NRSF** via miRNA derepression, causing abnormal neuronal gene expression and altered neurodevelopmental timing | **EHMT1**, **REST** (NRSF), miRNAs | negative regulation of neuron differentiation; regulation of miRNA-mediated gene silencing; regulation of transcription by RNA polymerase II | nucleus; chromatin; miRISC-associated cytoplasmic compartments | induced pluripotent stem cell-derived neuron; neural progenitor cell | forebrain (UBERON:0001890); brain (UBERON:0000955) | microRNA (CHEBI:33697) | Reduced EHMT1 activity decreases REST/NRSF protein indirectly through miRNA repression defects, altering neuronal gene expression/progression of neurodevelopment (wood2024theepigeneticnetwork pages 1-5, tzetis2025anovelframeshift pages 4-6, ren2024clinicalcharacteristicsand pages 12-12) PMID: 36241675 |
| **BDNF** promoter hypomethylation/increased expression is linked to excessive neurite outgrowth | **BDNF**, **EHMT1**, **REST** | axonogenesis; neuron projection development; regulation of neurotrophin signaling pathway | neuronal projection; growth cone; nucleus | cortical neuron (CL:0000540) | cerebral cortex (UBERON:0000956); hippocampus (UBERON:0002421) | brain-derived neurotrophic factor / BDNF (protein; no CHEBI); acetylcholine (CHEBI:15355) | KS spheroids had longer/more branched neurites and higher BDNF; cited evidence links Ehmt1 loss to BDNF promoter hypomethylation and REST-target derepression (balogh2024establishmentofhumana pages 7-8, balogh2024establishmentofhumana pages 1-2) PMID: not provided in retrieved texts |
| Synaptogenesis/connectivity deficit with reduced **PSD95** and **SYP** despite increased neurite outgrowth | **DLG4** (PSD95), **SYP**, **EHMT1** | synapse organization; chemical synaptic transmission; postsynapse assembly | postsynaptic density; synaptic vesicle membrane; excitatory synapse | cortical neuron (CL:0000540) | cerebral cortex (UBERON:0000956) | none specifically established | In KS neurites, PSD95 and SYP were lower, with PSD95 significant (p=0.01), indicating impaired synaptogenesis/connectivity despite neurite overgrowth (balogh2024establishmentofhumana pages 5-7, balogh2024establishmentofhumana pages 7-8) PMID: not provided in retrieved texts |
| Altered neuronal subtype balance: excess glutamatergic/cholinergic markers and reduced catecholaminergic neurons | **SLC17A7/SLC17A6** (VGLUT1/2), **CHAT**, **TH**, **GRIN1** | neuron differentiation; neurotransmitter transport; regulation of excitatory postsynaptic potential | synapse; synaptic vesicle; postsynaptic membrane | glutamatergic neuron (CL:0000679); cholinergic neuron (CL:0000108); catecholaminergic neuron (CL:0000700) | cerebral cortex (UBERON:0000956) | glutamate (CHEBI:29985); acetylcholine (CHEBI:15355); dopamine/catecholamine-related small molecules (CHEBI:18243 for dopamine) | KS spheroids were enriched for VGLUT1/2+ and ChAT+ neurons, with TH+ neurons underrepresented; NMDAR1 high as a KS marker (balogh2024establishmentofhumana pages 1-2, balogh2024establishmentofhumana pages 7-8) PMID: not provided in retrieved texts |
| Oxidative-stress vulnerability and metabolic adaptation defects with **LDHA** downregulation | **LDHA**, **LDHB**, **EHMT1** | response to oxidative stress; pyruvate metabolic process; lactate metabolic process | cytosol; mitochondrion | neural progenitor cell (CL:0000031); cortical spheroid neuron | cerebral cortex (UBERON:0000956); developing brain (UBERON:0001016) | paraquat (CHEBI:34905); rotenone (CHEBI:28262); bardoxolone methyl/CDDO-Me (CHEBI not established here); doxorubicin (CHEBI:28748); lactate (CHEBI:24996); pyruvate (CHEBI:15361) | KS spheroids showed greater toxicant sensitivity, especially paraquat (EC50 4.8 vs 23.7 µM control) and rotenone (0.11 vs 0.23 µM), and **LDHA** was downregulated in NPCs (p=0.03) and 3D spheroids (p=0.002) (balogh2024establishmentofhumana pages 5-7, balogh2024establishmentofhumana pages 7-8, balogh2024establishmentofhuman media d449cbce) PMID: not provided in retrieved texts |
| DNA methylation episignature as a molecular biomarker; variant/domain effects refine mechanism and diagnosis | **EHMT1**, **EHMT2** | DNA methylation; epigenetic regulation of gene expression; chromatin organization | chromatin; nucleus; peripheral blood leukocyte nucleus | leukocyte (CL:0000738) | blood (UBERON:0000178) | 5-methylcytosine (CHEBI:49108) | 2024 AJHG study of 209 individuals used DNAm signatures to classify EHMT1 variants; ankyrin-reader disruption could yield KLEFS1 episignature, whereas SET-only loss did not consistently produce canonical DNAm signature/phenotype (rots2024comprehensiveehmt1variants pages 1-3, barrero2024ehmt2lossoffunctionalterations pages 4-7) PMID: not provided in retrieved texts |


*Table: This table summarizes core molecular and cellular mechanisms implicated in Kleefstra syndrome, linking each mechanism to genes, ontology-ready biological processes and compartments, affected cell types and anatomy, relevant chemicals, and evidence sources. It is useful as a compact knowledge-base scaffold for annotation and evidence tracking.*

Key GO biological-process themes supported by evidence include:
- Histone H3K9 methylation and negative regulation of transcription (EHMT1/EHMT2). (frega2019neuronalnetworkdysfunction pages 1-2)
- Regulation of synaptic signaling and homeostatic synaptic plasticity, including NMDAR-dependent network activity. (frega2019neuronalnetworkdysfunction pages 1-2, frega2019neuronalnetworkdysfunction pages 5-6)
- miRNA-mediated post-transcriptional regulation affecting neuronal differentiation timing (REST axis). (alsaqati2022nrsfrestliesat pages 3-5)

Cellular component themes include nucleus/chromatin (epigenetic regulation) and synaptic compartments such as postsynaptic density (PSD95) and glutamatergic synapses (NMDAR1). (balogh2024establishmentofhumana pages 5-7, frega2019neuronalnetworkdysfunction pages 1-2)

---

## 5) Disease progression model (sequence of events)

A synthesis consistent with current data:
1) **Initial trigger**: heterozygous loss-of-function in **EHMT1** (or deletion of 9q34.3 including EHMT1) → reduced EHMT1 dosage. (frega2019neuronalnetworkdysfunction pages 1-2, morison2024expandingthephenotype pages 5-7)  
2) **Primary molecular event**: reduced EHMT1/EHMT2 complex activity and/or altered reader/writer functions → reduced local or global repressive chromatin marks (e.g., H3K9me2) and altered transcriptional regulation; plus indirect effects via miRNA networks. (frega2019neuronalnetworkdysfunction pages 1-2, alsaqati2022nrsfrestliesat pages 3-5, rots2024comprehensiveehmt1variants pages 1-3)  
3) **Developmental program disruption**: premature or aberrant expression of neuronal genes due to REST reduction and altered miRNA dynamics; altered neuronal subtype specification and/or maturation timing. (alsaqati2022nrsfrestliesat pages 3-5, balogh2024establishmentofhumana pages 7-8)  
4) **Synaptic/circuit dysfunction**: reduced synaptic marker expression (PSD95/SYP), abnormal glutamatergic signaling with **NMDAR1 upregulation**, abnormal bursting patterns and compensatory homeostatic plasticity. (balogh2024establishmentofhumana pages 5-7, frega2019neuronalnetworkdysfunction pages 1-2, frega2019neuronalnetworkdysfunction pages 5-6)  
5) **Clinical manifestation**: neurodevelopmental disorder phenotype—ID, severe speech disorder, autistic traits, hypotonia, epilepsy and multi-system features. (morison2024expandingthephenotype pages 5-7, morison2024expandingthephenotype pages 1-3)

A key unresolved issue is developmental critical windows (prenatal vs postnatal) for reversibility, which remains an area of active research and is emphasized as a major translational question for histone methyltransferase-related NDDs. (roth2023histonelysinemethyltransferaserelated pages 7-9)

---

## 6) Phenotypic manifestations and mechanistic links (with 2024 statistics)

A large 2024 cohort (n=103) provides updated, actionable phenotype frequencies and functional-impact measures:
- **Epilepsy**: 12/103 (12%). (Morison et al., J Med Genet 2024; DOI: https://doi.org/10.1136/jmg-2023-109702) (morison2024expandingthephenotype pages 5-7)
- **Sleep disturbance**: 65/103 (63%). (morison2024expandingthephenotype pages 5-7)
- **Cardiac conditions**: 33/103 (32%). (morison2024expandingthephenotype pages 5-7)
- **MRI abnormalities**: 38/79 (48%). (morison2024expandingthephenotype pages 5-7)
- **Cognitive distribution (n=79 assessed)**: 67/79 (85%) had ID (mild 20%, moderate 48%, severe 15%); 12/79 (15%) had average cognitive ability. (morison2024expandingthephenotype pages 5-7, morison2024expandingthephenotype pages 7-8)
- **Language distribution (n=90 assessed)**: average 10/90 (11%); severe impairment 53/90 (59%). (morison2024expandingthephenotype pages 1-3)
- **Speech disorder among verbal individuals**: 48/49 (98%) had a speech disorder; dysarthria 34/49 (69%); childhood apraxia of speech 29/49 (59%). (morison2024expandingthephenotype pages 8-10)
- **Regression**: 11/80 (14%), often involving language and psychosocial domains; potential triggers included illness and seizures. (morison2024expandingthephenotype pages 7-8)
- **AAC use**: 61/103 (59%), emphasizing real-world implementation of communication supports. (morison2024expandingthephenotype pages 1-3)

Mechanistic alignment: high burden of speech disorder and neurodevelopmental variability is consistent with EHMT1-dependent disruption of neuronal gene programs and network function (REST/miRNA and NMDAR axes). (alsaqati2022nrsfrestliesat pages 3-5, frega2019neuronalnetworkdysfunction pages 1-2)

---

## 7) Recent developments (2023–2024) and latest research themes

### 7.1 2024: Variant interpretation, genotype–mechanism insights, and episignatures
A major 2024 AJHG study recruited **209** individuals with rare EHMT1 variants and reclassified **191** as likely pathogenic/pathogenic using combined in silico/in vitro evidence and DNAm signature analysis. (Rots et al., AJHG 2024; DOI: https://doi.org/10.1016/j.ajhg.2024.06.008) (rots2024comprehensiveehmt1variants pages 1-3)
Key mechanistic interpretation from this cohort: disruption of EHMT1 functional domains (e.g., ankyrin repeat “reader” vs SET “writer” effects) can associate with differing DNAm signature presence and phenotype severity, supporting a more nuanced model than “global loss of methyltransferase activity alone.” (rots2024comprehensiveehmt1variants pages 1-3)

### 7.2 2024: Human 3D cortical neurosphere models for pathomechanisms and screening
Balogh et al. established a patient-derived cortical spheroid model that recapitulates disease-associated traits and is positioned for drug/toxicant screening. (Balogh et al., Sci Rep 2024; DOI: https://doi.org/10.1038/s41598-024-72791-4) (balogh2024establishmentofhumana pages 1-2)
Quantitative toxicant data include EC50 shifts in KS vs control, especially in 3D spheroids (Table 1/Figure 4). For example:
- **Paraquat EC50 (3D spheroids)**: control 23.7 µM vs KS 4.8 µM. (balogh2024establishmentofhuman media d449cbce)
- **Rotenone EC50 (3D spheroids)**: control 0.23 µM vs KS 0.11 µM. (balogh2024establishmentofhuman media d449cbce)

### 7.3 2023: Therapeutic concept reviews for histone methyltransferase haploinsufficiency disorders
A 2023 Frontiers review highlights emerging interest in **gene-upregulation strategies** (e.g., RNA activation / saRNA) as a conceptual match for haploinsufficiency disorders (contrasting with oncology, where inhibitors dominate). The review emphasizes key barriers—particularly delivery to brain—and recommends patient-derived neuronal 2D/3D models for preclinical testing. (Roth et al., Front Cell Dev Biol 2023; DOI: https://doi.org/10.3389/fcell.2023.1090046) (roth2023histonelysinemethyltransferaserelated pages 7-9, roth2023histonelysinemethyltransferaserelated pages 6-7)

---

## 8) Current applications and real-world implementations

### 8.1 Clinical phenotyping and care
The 2024 cohort shows very high utilization of supportive therapies:
- occupational therapy 87/101 (86%), physiotherapy 90/101 (89%), speech therapy 100/103 (97%). (morison2024expandingthephenotype pages 7-8)
AAC use in 59% of individuals reflects real-world implementation of assistive communication as a core management component. (morison2024expandingthephenotype pages 1-3)

### 8.2 Molecular diagnostics: episignatures / EpiSign-style approaches
The 2024 AJHG variant study explicitly integrates DNAm signatures to support diagnosis and variant classification, representing a practical implementation of clinical epigenomics in KS. (rots2024comprehensiveehmt1variants pages 1-3)

### 8.3 Disease modeling for mechanism and screening
Human iPSC-derived excitatory cortical neuron networks and 3D cortical spheroids are now well-established platforms for:
- mechanistic dissection (e.g., GRIN1 promoter repression and NMDAR hyperfunction), (frega2019neuronalnetworkdysfunction pages 1-2)
- pharmacologic rescue assays (NMDAR antagonism), (frega2019neuronalnetworkdysfunction pages 1-2)
- toxicant/drug sensitivity profiling with quantitative EC50 endpoints. (balogh2024establishmentofhuman media d449cbce)

---

## 9) Expert opinions and analysis (authoritative interpretations)

1) **Mechanistic targeting of NMDAR signaling**: Frega et al. conclude a “direct link” between EHMT1 deficiency and NMDAR hyperfunction and show pharmacological rescue of network phenotypes, supporting NMDAR pathway modulation as a rational, mechanism-based intervention concept (preclinical). (frega2019neuronalnetworkdysfunction pages 1-2)

2) **Systems-level epigenetic-to-developmental timing effects**: Alsaqati et al. frame EHMT1 as controlling REST/NRSF through miRNA repression, connecting chromatin regulation to neuronal gene program timing and to broader neuropsychiatric risk architecture (ID/schizophrenia enrichment in EHMT1-regulated miRNA sets). (alsaqati2022nrsfrestliesat pages 1-2, alsaqati2022nrsfrestliesat pages 3-5)

3) **Therapeutic development constraints**: Roth et al. emphasize that for HKMT-related NDDs, a major barrier is brain delivery and timing, arguing for rigorous testing in advanced human neuronal models (organoids/assembloids, BBB inclusion) to evaluate efficacy and safety of gene-activation approaches. (roth2023histonelysinemethyltransferaserelated pages 7-9)

---

## 10) Evidence items (PMIDs) and priority references (with URLs and dates)

**High-priority mechanistic primary studies**
- Frega M. et al. *Nature Communications* (2019-10). “Neuronal network dysfunction in a model for Kleefstra syndrome mediated by enhanced NMDAR signaling.” DOI: https://doi.org/10.1038/s41467-019-12947-3. PMID: **31695196**. (frega2019neuronalnetworkdysfunction pages 1-2)
- Alsaqati M. et al. *Translational Psychiatry* (2022-10). “NRSF/REST lies at the intersection between epigenetic regulation, miRNA-mediated gene control and neurodevelopmental pathways…” DOI: https://doi.org/10.1038/s41398-022-02199-z. PMID: **36241675**. (alsaqati2022nrsfrestliesat pages 1-2)

**Recent (2023–2024) sources prioritized**
- Balogh A. et al. *Scientific Reports* (2024-09). “Establishment of human pluripotent stem cell-derived cortical neurosphere model…” DOI: https://doi.org/10.1038/s41598-024-72791-4. (PMID not available in retrieved text). (balogh2024establishmentofhumana pages 1-2)
- Morison L.D. et al. *Journal of Medical Genetics* (2024-01). “Expanding the phenotype of Kleefstra syndrome: speech, language and cognition in 103 individuals.” DOI: https://doi.org/10.1136/jmg-2023-109702. (PMID not available in retrieved text). (morison2024expandingthephenotype pages 1-3)
- Roth C. et al. *Frontiers in Cell and Developmental Biology* (2023-02). “Histone lysine methyltransferase-related neurodevelopmental disorders: current knowledge and saRNA future therapies.” DOI: https://doi.org/10.3389/fcell.2023.1090046. (PMID not available in retrieved text). (roth2023histonelysinemethyltransferaserelated pages 2-3)
- Rots D. et al. *American Journal of Human Genetics* (2024-08). “Comprehensive EHMT1 variants analysis…” DOI: https://doi.org/10.1016/j.ajhg.2024.06.008. (PMID not available in retrieved text). (rots2024comprehensiveehmt1variants pages 1-3)

---

## 11) Limitations of this synthesis
Some 2024 papers in the retrieved corpus did not include PubMed identifiers in the extracted text; where PMIDs are absent above, they were not available from provided tool context and should be cross-checked in PubMed for knowledge-base ingestion. (balogh2024establishmentofhumana pages 1-2, rots2024comprehensiveehmt1variants pages 1-3, morison2024expandingthephenotype pages 1-3)

---

### Figures/tables used
Balogh et al. 2024 Figure 4 and Table 1 (dose-response curves and EC50 values) were extracted as cropped images for quantitative support of toxicant sensitivity differences. (balogh2024establishmentofhuman media d449cbce, balogh2024establishmentofhuman media 76d9168d)


References

1. (frega2019neuronalnetworkdysfunction pages 1-2): Monica Frega, Katrin Linda, Jason M. Keller, Güvem Gümüş-Akay, Britt Mossink, Jon-Ruben van Rhijn, Moritz Negwer, Teun Klein Gunnewiek, Katharina Foreman, Nine Kompier, Chantal Schoenmaker, Willem van den Akker, Ilse van der Werf, Astrid Oudakker, Huiqing Zhou, Tjitske Kleefstra, Dirk Schubert, Hans van Bokhoven, and Nael Nadif Kasri. Neuronal network dysfunction in a model for kleefstra syndrome mediated by enhanced nmdar signaling. Nature Communications, Oct 2019. URL: https://doi.org/10.1038/s41467-019-12947-3, doi:10.1038/s41467-019-12947-3. This article has 164 citations and is from a highest quality peer-reviewed journal.

2. (morison2024expandingthephenotype pages 5-7): Lottie D. Morison, Milou G.P. Kennis, Dmitrijs Rots, Arianne Bouman, Joost Kummeling, Elizabeth Palmer, Adam P. Vogel, Frederique Liegeois, Amanda Brignell, Siddharth Srivastava, Zoe Frazier, Di Milnes, Himanshu Goel, David J. Amor, Ingrid E. Scheffer, Tjitske Kleefstra, and Angela T. Morgan. Expanding the phenotype of kleefstra syndrome: speech, language and cognition in 103 individuals. Journal of Medical Genetics, 61(6):578-585, Jan 2024. URL: https://doi.org/10.1136/jmg-2023-109702, doi:10.1136/jmg-2023-109702. This article has 21 citations and is from a domain leading peer-reviewed journal.

3. (balogh2024establishmentofhuman media 76d9168d): Andrea Balogh, Mária Bódi-Jakus, Vivien Réka Karl, Tamás Bellák, Balázs Széky, János Farkas, Federica Lamberto, David Novak, Anita Fehér, Melinda Zana, and András Dinnyés. Establishment of human pluripotent stem cell-derived cortical neurosphere model to study pathomechanisms and chemical toxicity in kleefstra syndrome. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-72791-4, doi:10.1038/s41598-024-72791-4. This article has 3 citations and is from a peer-reviewed journal.

4. (hnizda2025denovoheterozygous pages 1-6): Aleš Hnízda, Beatriz Martinez-Delgado, Diana Sanchez-Ponce, Javier Alonso, Jeanne Amiel, Tania Attie-Bitach, Ariadna Bada-Navarro, Beatriz Baladron, Eva Bermejo-Sanchez, Vítězslav Brinsa, Ivana Buková, Rosario Cazorla-Calleja, Sylvie Červenková, Shanshan Chow, Petr Dušek, Marta Fernandez, Sourav Ghosh, Gema Gomez-Mariano, Andrea Gřegořová, Mark James Hamilton, Hana Hartmannová, Esther Hernandez-San Miguel, Marina Herrero-Matesanz, Kateřina Hodaňová, Alan Kádek, Jennifer Kerkhof, Tjitske Kleefstra, Didier Lacombe, Michael A. Levy, Estrella Lopez-Martin, Ruaud Lyse, Petr Man, Purificacion Marin-Reina, Ellen F. Macnamara, Haley McConkey, Petra Melenovská, Lidia M. Mielu, David Moore, Lenka Mrázová, Karolína Musilová, Petr Nickl, Martina Pavlíková, Lea Pavlovičová, Manuel Posada, Jan Procházka, Kateryna Pysanenko, Sheila Ramos del Saz, Dmitrijs Rots, Jessica Rzasa, Radislav Sedláček, Viktor Stránecký, František Špoutil, Matthew L. Tedder, Louise Thompson, Cynthia J. Tifft, Frederic Tran Mau-Them, Helena Trešlová, Antonio Vitobello, Bekim Sadikovic, Jakub Sikora, Stanislav Kmoch, Maria J. Barrero, and Lenka Nosková. De novo heterozygous variants in ehmt2 genocopy kleefstra syndrome via loss of g9a methyltransferase activity. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.09.25.678439, doi:10.1101/2025.09.25.678439. This article has 0 citations.

5. (rots2024comprehensiveehmt1variants pages 1-3): Dmitrijs Rots, Arianne Bouman, Ayumi Yamada, Michael Levy, Alexander J.M. Dingemans, Bert B.A. de Vries, Martina Ruiterkamp-Versteeg, Nicole de Leeuw, Charlotte W. Ockeloen, Rolph Pfundt, Elke de Boer, Joost Kummeling, Bregje van Bon, Hans van Bokhoven, Nael Nadif Kasri, Hanka Venselaar, Marielle Alders, Jennifer Kerkhof, Haley McConkey, Alma Kuechler, Bart Elffers, Rixje van Beeck Calkoen, Susanna Hofman, Audrey Smith, Maria Irene Valenzuela, Siddharth Srivastava, Zoe Frazier, Isabelle Maystadt, Carmelo Piscopo, Giuseppe Merla, Meena Balasubramanian, Gijs W.E. Santen, Kay Metcalfe, Soo-Mi Park, Laurent Pasquier, Siddharth Banka, Dian Donnai, Daniel Weisberg, Gertrud Strobl-Wildemann, Annemieke Wagemans, Maaike Vreeburg, Diana Baralle, Nicola Foulds, Ingrid Scurr, Nicola Brunetti-Pierri, Johanna M. van Hagen, Emilia K. Bijlsma, Anna H. Hakonen, Carolina Courage, David Genevieve, Lucile Pinson, Francesca Forzano, Charu Deshpande, Maria L. Kluskens, Lindsey Welling, Astrid S. Plomp, Els K. Vanhoutte, Louisa Kalsner, Janna A. Hol, Audrey Putoux, Johanna Lazier, Pradeep Vasudevan, Elizabeth Ames, Jessica O'Shea, Damien Lederer, Julie Fleischer, Mary O'Connor, Melissa Pauly, Georgia Vasileiou, André Reis, Catherine Kiraly-Borri, Arjan Bouman, Chris Barnett, Marjan Nezarati, Lauren Borch, Gea Beunders, Kübra Özcan, Stéphanie Miot, Catharina M.L. Volker-Touw, Koen L.I. van Gassen, Gerarda Cappuccio, Katrien Janssens, Nofar Mor, Inna Shomer, Dan Dominissini, Matthew L. Tedder, Alison M. Muir, Bekim Sadikovic, Han G. Brunner, Lisenka E.L.M. Vissers, Yoichi Shinkai, and Tjitske Kleefstra. Comprehensive ehmt1 variants analysis broadens genotype-phenotype associations and molecular mechanisms in kleefstra syndrome. The American Journal of Human Genetics, 111:1605-1625, Aug 2024. URL: https://doi.org/10.1016/j.ajhg.2024.06.008, doi:10.1016/j.ajhg.2024.06.008. This article has 23 citations.

6. (balogh2024establishmentofhumana pages 1-2): Andrea Balogh, Mária Bódi-Jakus, Vivien Réka Karl, Tamás Bellák, Balázs Széky, János Farkas, Federica Lamberto, David Novak, Anita Fehér, Melinda Zana, and András Dinnyés. Establishment of human pluripotent stem cell-derived cortical neurosphere model to study pathomechanisms and chemical toxicity in kleefstra syndrome. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-72791-4, doi:10.1038/s41598-024-72791-4. This article has 3 citations and is from a peer-reviewed journal.

7. (frega2019neuronalnetworkdysfunction pages 5-6): Monica Frega, Katrin Linda, Jason M. Keller, Güvem Gümüş-Akay, Britt Mossink, Jon-Ruben van Rhijn, Moritz Negwer, Teun Klein Gunnewiek, Katharina Foreman, Nine Kompier, Chantal Schoenmaker, Willem van den Akker, Ilse van der Werf, Astrid Oudakker, Huiqing Zhou, Tjitske Kleefstra, Dirk Schubert, Hans van Bokhoven, and Nael Nadif Kasri. Neuronal network dysfunction in a model for kleefstra syndrome mediated by enhanced nmdar signaling. Nature Communications, Oct 2019. URL: https://doi.org/10.1038/s41467-019-12947-3, doi:10.1038/s41467-019-12947-3. This article has 164 citations and is from a highest quality peer-reviewed journal.

8. (alsaqati2022nrsfrestliesat pages 3-5): Mouhamed Alsaqati, Brittany A. Davis, Jamie Wood, Megan M. Jones, Lora Jones, Aishah Westwood, Olena Petter, Anthony R. Isles, David Linden, Marianne Van den Bree, Michael Owen, Jeremy Hall, and Adrian J. Harwood. Nrsf/rest lies at the intersection between epigenetic regulation, mirna-mediated gene control and neurodevelopmental pathways associated with intellectual disability (id) and schizophrenia. Translational Psychiatry, Oct 2022. URL: https://doi.org/10.1038/s41398-022-02199-z, doi:10.1038/s41398-022-02199-z. This article has 19 citations and is from a peer-reviewed journal.

9. (alsaqati2022nrsfrestliesat pages 1-2): Mouhamed Alsaqati, Brittany A. Davis, Jamie Wood, Megan M. Jones, Lora Jones, Aishah Westwood, Olena Petter, Anthony R. Isles, David Linden, Marianne Van den Bree, Michael Owen, Jeremy Hall, and Adrian J. Harwood. Nrsf/rest lies at the intersection between epigenetic regulation, mirna-mediated gene control and neurodevelopmental pathways associated with intellectual disability (id) and schizophrenia. Translational Psychiatry, Oct 2022. URL: https://doi.org/10.1038/s41398-022-02199-z, doi:10.1038/s41398-022-02199-z. This article has 19 citations and is from a peer-reviewed journal.

10. (balogh2024establishmentofhumana pages 5-7): Andrea Balogh, Mária Bódi-Jakus, Vivien Réka Karl, Tamás Bellák, Balázs Széky, János Farkas, Federica Lamberto, David Novak, Anita Fehér, Melinda Zana, and András Dinnyés. Establishment of human pluripotent stem cell-derived cortical neurosphere model to study pathomechanisms and chemical toxicity in kleefstra syndrome. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-72791-4, doi:10.1038/s41598-024-72791-4. This article has 3 citations and is from a peer-reviewed journal.

11. (balogh2024establishmentofhuman media d449cbce): Andrea Balogh, Mária Bódi-Jakus, Vivien Réka Karl, Tamás Bellák, Balázs Széky, János Farkas, Federica Lamberto, David Novak, Anita Fehér, Melinda Zana, and András Dinnyés. Establishment of human pluripotent stem cell-derived cortical neurosphere model to study pathomechanisms and chemical toxicity in kleefstra syndrome. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-72791-4, doi:10.1038/s41598-024-72791-4. This article has 3 citations and is from a peer-reviewed journal.

12. (balogh2024establishmentofhumana pages 7-8): Andrea Balogh, Mária Bódi-Jakus, Vivien Réka Karl, Tamás Bellák, Balázs Széky, János Farkas, Federica Lamberto, David Novak, Anita Fehér, Melinda Zana, and András Dinnyés. Establishment of human pluripotent stem cell-derived cortical neurosphere model to study pathomechanisms and chemical toxicity in kleefstra syndrome. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-72791-4, doi:10.1038/s41598-024-72791-4. This article has 3 citations and is from a peer-reviewed journal.

13. (wood2024theepigeneticnetwork pages 1-5): J Wood. The epigenetic network mediated by ehmt1 and its role in neurodevelopment disorders. Unknown journal, 2024.

14. (tzetis2025anovelframeshift pages 4-6): Maria Tzetis, Anastasios Mitrakos, Ioanna Papathanasiou, Vasiliki Koute, Konstantina Kosma, Roser Pons, Aspasia Michoula, Ioanna Grivea, and Aspasia Tsezou. A novel frameshift variant and a partial ehmt1 microdeletion in kleefstra syndrome 1 patients resulting in variable phenotypic severity and literature review. Genes, 16:521, Apr 2025. URL: https://doi.org/10.3390/genes16050521, doi:10.3390/genes16050521. This article has 0 citations.

15. (ren2024clinicalcharacteristicsand pages 12-12): Rong Ren, Yedan Liu, Peipei Liu, Jing Zhao, Mei Hou, Shuo Li, Zongbo Chen, and Aiyun Yuan. Clinical characteristics and genetic analysis of four pediatric patients with kleefstra syndrome. BMC Medical Genomics, Dec 2024. URL: https://doi.org/10.1186/s12920-024-02065-5, doi:10.1186/s12920-024-02065-5. This article has 4 citations and is from a peer-reviewed journal.

16. (barrero2024ehmt2lossoffunctionalterations pages 4-7): Maria Barrero, Beatriz Martínez-Delgado, Estrella López-Martín, Jennifer Kerkhof, Beatriz Baladron, Lidia Mielu, Diana Sanchez-Ponce, Ariadna Bada-Navarro, Marina Herrero Matesanz, Lidia Lopez-Jimenez, Jesica Rzasa, Dmitrijs Rots, Marta Fernandez-Prieto, Esther Hernandez-SanMiguel, Gema Gómez-Mariano, Purificacion Marin-Reina, Rosario Cazorla-Calleja, Javier Alonso, Tjitske Kleefstra, Manuel Posada, Eva Bermejo-Sánchez, and Bekim Sadikovic. Ehmt2 loss-of-function alterations cause a kleefstra-like syndrome. Unknown journal, Feb 2024. URL: https://doi.org/10.21203/rs.3.rs-3893528/v1, doi:10.21203/rs.3.rs-3893528/v1.

17. (morison2024expandingthephenotype pages 1-3): Lottie D. Morison, Milou G.P. Kennis, Dmitrijs Rots, Arianne Bouman, Joost Kummeling, Elizabeth Palmer, Adam P. Vogel, Frederique Liegeois, Amanda Brignell, Siddharth Srivastava, Zoe Frazier, Di Milnes, Himanshu Goel, David J. Amor, Ingrid E. Scheffer, Tjitske Kleefstra, and Angela T. Morgan. Expanding the phenotype of kleefstra syndrome: speech, language and cognition in 103 individuals. Journal of Medical Genetics, 61(6):578-585, Jan 2024. URL: https://doi.org/10.1136/jmg-2023-109702, doi:10.1136/jmg-2023-109702. This article has 21 citations and is from a domain leading peer-reviewed journal.

18. (roth2023histonelysinemethyltransferaserelated pages 7-9): Charlotte Roth, Helena Kilpinen, Manju A. Kurian, and Serena Barral. Histone lysine methyltransferase-related neurodevelopmental disorders: current knowledge and sarna future therapies. Frontiers in Cell and Developmental Biology, Feb 2023. URL: https://doi.org/10.3389/fcell.2023.1090046, doi:10.3389/fcell.2023.1090046. This article has 9 citations.

19. (morison2024expandingthephenotype pages 7-8): Lottie D. Morison, Milou G.P. Kennis, Dmitrijs Rots, Arianne Bouman, Joost Kummeling, Elizabeth Palmer, Adam P. Vogel, Frederique Liegeois, Amanda Brignell, Siddharth Srivastava, Zoe Frazier, Di Milnes, Himanshu Goel, David J. Amor, Ingrid E. Scheffer, Tjitske Kleefstra, and Angela T. Morgan. Expanding the phenotype of kleefstra syndrome: speech, language and cognition in 103 individuals. Journal of Medical Genetics, 61(6):578-585, Jan 2024. URL: https://doi.org/10.1136/jmg-2023-109702, doi:10.1136/jmg-2023-109702. This article has 21 citations and is from a domain leading peer-reviewed journal.

20. (morison2024expandingthephenotype pages 8-10): Lottie D. Morison, Milou G.P. Kennis, Dmitrijs Rots, Arianne Bouman, Joost Kummeling, Elizabeth Palmer, Adam P. Vogel, Frederique Liegeois, Amanda Brignell, Siddharth Srivastava, Zoe Frazier, Di Milnes, Himanshu Goel, David J. Amor, Ingrid E. Scheffer, Tjitske Kleefstra, and Angela T. Morgan. Expanding the phenotype of kleefstra syndrome: speech, language and cognition in 103 individuals. Journal of Medical Genetics, 61(6):578-585, Jan 2024. URL: https://doi.org/10.1136/jmg-2023-109702, doi:10.1136/jmg-2023-109702. This article has 21 citations and is from a domain leading peer-reviewed journal.

21. (roth2023histonelysinemethyltransferaserelated pages 6-7): Charlotte Roth, Helena Kilpinen, Manju A. Kurian, and Serena Barral. Histone lysine methyltransferase-related neurodevelopmental disorders: current knowledge and sarna future therapies. Frontiers in Cell and Developmental Biology, Feb 2023. URL: https://doi.org/10.3389/fcell.2023.1090046, doi:10.3389/fcell.2023.1090046. This article has 9 citations.

22. (roth2023histonelysinemethyltransferaserelated pages 2-3): Charlotte Roth, Helena Kilpinen, Manju A. Kurian, and Serena Barral. Histone lysine methyltransferase-related neurodevelopmental disorders: current knowledge and sarna future therapies. Frontiers in Cell and Developmental Biology, Feb 2023. URL: https://doi.org/10.3389/fcell.2023.1090046, doi:10.3389/fcell.2023.1090046. This article has 9 citations.