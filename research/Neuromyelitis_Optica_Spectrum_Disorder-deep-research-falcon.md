---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-06T08:21:35.977868'
end_time: '2026-01-06T08:27:48.090484'
duration_seconds: 372.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neuromyelitis Optica Spectrum Disorder
  mondo_id: ''
  category: Neurological Disorder
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 10
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Neuromyelitis Optica Spectrum Disorder
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Neuromyelitis Optica Spectrum Disorder**.
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
- **Disease Name:** Neuromyelitis Optica Spectrum Disorder
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Neuromyelitis Optica Spectrum Disorder**.
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
- Disease Name: Neuromyelitis Optica Spectrum Disorder (NMOSD)
- MONDO ID: MONDO:0013524 (if using OBO Foundry conventions; to be verified in downstream curation)
- Category: Neurological Disorder

## Research Objectives: Pathophysiology of NMOSD (AQP4-IgG–positive focus)

### 1. Core Pathophysiology
NMOSD is an autoimmune astrocytopathy in which circulating IgG1 autoantibodies against the astrocytic water channel aquaporin‑4 (AQP4) gain access to the central nervous system (CNS), bind AQP4—preferentially in M23-driven orthogonal arrays of particles (OAPs)—and trigger complement-dependent cytotoxicity (CDC) and antibody-dependent cellular cytotoxicity (ADCC), leading to perivascular astrocyte loss, secondary demyelination, and neuronal injury. Initiation often involves blood–brain barrier (BBB) disruption or entry through circumventricular organs such as the area postrema. Complement activation generates C3a/C5a that recruit neutrophils/eosinophils and amplify inflammation; astrocyte-derived cytokines/chemokines (notably IL‑6 and CCL2) further promote leukocyte trafficking and Th17 polarization. Clinical efficacy of C5 inhibition and IL‑6 receptor blockade substantiates these mechanisms. (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4, shimizu2024blood–brainbarrierdisruption pages 9-10, shimizu2024blood–brainbarrierdisruption pages 10-12, nishiyama2024antiaquaporin4immunecomplex pages 1-2)

Directly supported statements:
- “At the onset of NMOSD, increased permeability of the BBB causes the entry of circulating AQP4 autoantibodies into the CNS” (International Journal of Molecular Sciences, Oct 2024; https://doi.org/10.3390/ijms251910625). (shimizu2024blood–brainbarrierdisruption pages 9-10)
- AQP4‑IgG/AQP4 immune complexes plus complement “prompt a Th17-biased response consistent with the inflammatory paradigm observed in NMOSD,” elevating IL‑17A and IL‑6 ex vivo (Scientific Reports, Feb 2024; https://doi.org/10.1038/s41598-024-53661-5). (nishiyama2024antiaquaporin4immunecomplex pages 1-2)

### 2. Key Molecular Players
- Genes/Proteins: AQP4 (astrocytic water channel, target antigen); complement components C1q, C3, C5 and MAC; Fcγ receptors (e.g., FCGR3A/CD16A) mediating ADCC; cytokines IL‑6, IL‑17A; chemokines CCL2 and CXCL8/IL‑8; transcription factor STAT3 (Th17/B-cell support); astrocytic marker GFAP (injury biomarker). (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4, nishiyama2024antiaquaporin4immunecomplex pages 1-2, shimizu2024blood–brainbarrierdisruption pages 9-10, shimizu2024blood–brainbarrierdisruption pages 20-22)
- Chemical Entities and Therapeutics: Complement fragment C5a (chemoattractant); eculizumab/ravulizumab (C5 inhibitors); satralizumab (IL‑6R blocker); inebilizumab (anti‑CD19 B‑cell depleter). Clinical efficacy reported in trials and summarized in recent literature. (nishiyama2024antiaquaporin4immunecomplex pages 1-2, shimizu2024blood–brainbarrierdisruption pages 20-22)
- Cell Types: Astrocytes (primary target); neutrophils, eosinophils, macrophages/microglia (innate effectors); NK/NKT cells (ADCC and cytokine production); B lineage cells including plasmablasts (AQP4‑IgG source); Th17 cells (IL‑17A producers). (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4, nishiyama2024antiaquaporin4immunecomplex pages 1-2, castagno2024identifyingneutrophilrelatedpathogenic pages 14-16, shimizu2024blood–brainbarrierdisruption pages 20-22)
- Anatomical Locations: Perivascular astrocyte endfeet at BBB; optic nerve, spinal cord, and area postrema (circumventricular organ with physiologically weak BBB). (shimizu2024blood–brainbarrierdisruption pages 10-12, xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4)

### 3. Biological Processes (GO-like)
- Complement activation, classical pathway, and MAC-mediated lysis of astrocytes upon C1q binding to AQP4‑IgG immune complexes. (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4)
- Antibody-dependent cellular cytotoxicity via FcγR (e.g., CD16A) on NK/NKT cells, neutrophils and macrophages. (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4, nishiyama2024antiaquaporin4immunecomplex pages 6-7)
- IL‑6–mediated signaling promoting plasmablast survival and Th17 polarization; Th17 differentiation/IL‑17A production; endothelial activation and enhanced BBB permeability. (nishiyama2024antiaquaporin4immunecomplex pages 1-2, shimizu2024blood–brainbarrierdisruption pages 20-22)
- Astrocyte chemokine production (CCL2, CXCL8) and C3 upregulation that activates microglia via C3aR; microglial C1q/C3 pathways contribute to synaptic/neuronal injury. (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4)
- Neutrophil recruitment and potential NET formation contributing to tissue injury; eosinophil participation in perivascular infiltrates. (castagno2024identifyingneutrophilrelatedpathogenic pages 14-16, masciocchi2025conformationalantibodiesto pages 12-17)
- AQP4 internalization and disturbance of astrocytic glutamate handling leading to excitotoxic oligodendrocyte and neuronal damage. (masciocchi2025conformationalantibodiesto pages 12-17, xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4)

### 4. Cellular Components
- Astrocyte endfeet at perivascular interfaces (AQP4 enrichment). (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4)
- AQP4 M23-driven OAPs on the astrocyte plasma membrane (higher avidity binding). (masciocchi2025conformationalantibodiesto pages 12-17)
- Membrane attack complex (MAC) deposition on astrocytes; extracellular milieu where C3a/C5a signal. (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4)

### 5. Disease Progression: Sequence of Events
- Initiation: BBB disruption (mechanical/inflammatory) and/or entry via circumventricular organs; endothelial autoantibodies (e.g., anti‑GRP78) decrease tight junction proteins and increase permeability, enabling AQP4‑IgG entry. “Monoclonal non-AQP4 antibodies bound BBB endothelium… GRP78-specific… increased BBB permeability in vivo.” (IJMS 2024; https://doi.org/10.3390/ijms251910625). (shimizu2024blood–brainbarrierdisruption pages 10-12)
- Target engagement and injury: AQP4‑IgG binds astrocytic AQP4, favoring M23 OAPs; C1q engagement triggers classical complement leading to MAC and CDC; parallel ADCC via FcγRs; astrocyte C3, IL‑6, and chemokine release. (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4, masciocchi2025conformationalantibodiesto pages 12-17)
- Effector recruitment and amplification: C3a/C5a and chemokines recruit neutrophils/eosinophils/macrophages; PBMC models show complement-dependent IL‑6/Th17 cytokine responses to AQP4 immune complexes, especially in treatment‑naïve patients. (nishiyama2024antiaquaporin4immunecomplex pages 1-2, castagno2024identifyingneutrophilrelatedpathogenic pages 14-16)
- Tissue injury and demyelination: Astrocyte loss disrupts glutamate/ion homeostasis and oligodendrocyte support, causing perivascular demyelination and axonal injury; microglial activation via C3 contributes to neuronal loss. (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4, masciocchi2025conformationalantibodiesto pages 12-17)
- Clinical manifestations: Lesions localize to optic nerve, spinal cord (LETM), and area postrema; biomarkers include CSF GFAP elevation and increased albumin quotient (Qalb). (shimizu2024blood–brainbarrierdisruption pages 20-22)

Quantitative/observational data where available:
- “Markedly increased CSF interleukin-6 levels” and correlation with disability; elevated CSF neutrophils in ~60% of acute untreated AQP4‑IgG+ cases cited in IJMS 2024 review. (https://doi.org/10.3390/ijms251910625). (shimizu2024blood–brainbarrierdisruption pages 9-10)
- Ex vivo PBMC stimulation: significant IL‑17A and IL‑6 elevations only when AQP4 immune complexes were co-stimulated with complement; rituximab-treated patients lacked IL‑17A rise (Scientific Reports 2024; https://doi.org/10.1038/s41598-024-53661-5). (nishiyama2024antiaquaporin4immunecomplex pages 1-2)

Therapeutic implications aligning with mechanisms:
- Complement C5 blockade (eculizumab/ravulizumab) and IL‑6R blockade (satralizumab) reduce relapses; B‑cell depletion modifies cytokine program and autoantibody source. The Scientific Reports 2024 article summarizes the clinical impact and mechanistic rationale. (nishiyama2024antiaquaporin4immunecomplex pages 1-2, shimizu2024blood–brainbarrierdisruption pages 20-22)

### 6. Differences vs MOGAD
- Target and primary lesion: NMOSD is astrocyte-targeted with prominent perivascular complement deposition and astrocyte loss; MOGAD is primarily an oligodendrocyte/myelin-targeted demyelinating process with relatively preserved astrocytes and less extensive complement deposition. (castagno2024identifyingneutrophilrelatedpathogenic pages 14-16, shimizu2024blood–brainbarrierdisruption pages 10-12)
- Immune infiltrate: NMOSD lesions show neutrophils and eosinophils prominently; MOGAD infiltrates are often CD4+ T‑cell predominant. (shimizu2024blood–brainbarrierdisruption pages 10-12)
- Pathophysiologic triggers: BBB entry of AQP4‑IgG (aided by anti‑GRP78 and CVO access) is central to NMOSD; MOG‑IgG can be directly pathogenic in EAE when administered intrathecally, indicating different access/effector dynamics. (shimizu2024blood–brainbarrierdisruption pages 10-12)

### 7. Phenotypic Manifestations and Mechanistic Links
- Optic neuritis (UBERON:0000940): visual loss linked to astrocyte-targeted injury and secondary demyelination in optic pathways. (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4)
- Longitudinally extensive transverse myelitis (LETM; UBERON:0002240): motor/sensory deficits from extensive astrocytopathy and demyelination in spinal cord. (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4)
- Area postrema syndrome (UBERON:0002768): intractable vomiting/hiccups from lesioning at a CVO with weak BBB. (shimizu2024blood–brainbarrierdisruption pages 10-12)
- Biomarkers: Elevated CSF GFAP (astrocyte injury) and increased Qalb indicating BBB disruption. (shimizu2024blood–brainbarrierdisruption pages 20-22)

### Embedded Ontology Mappings
| Category | Entity | Ontology (namespace) | ID | Role in NMOSD pathophysiology | Notes |
|---|---|---:|---:|---|---|
| Gene/Protein | AQP4 | HGNC | HGNC:633 | Target of pathogenic IgG1 leading to astrocyte injury via complement and ADCC (binding favored to M23/OAPs) (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4, masciocchi2025conformationalantibodiesto pages 12-17) | Enriched on astrocyte endfeet; forms orthogonal arrays of particles (OAPs) that enhance antibody binding |
| Gene/Protein | IL6 | HGNC | HGNC:6018 | Central cytokine promoting plasmablast/Th17 responses and BBB permeability (nishiyama2024antiaquaporin4immunecomplex pages 1-2, shimizu2024blood–brainbarrierdisruption pages 20-22) | Elevated in CSF/serum; therapeutic target of IL-6R blockade (satralizumab) |
| Gene/Protein | C3 | HGNC | HGNC:1318 | Complement component produced by astrocytes after AQP4-IgG binding; drives microglial activation (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4) | Astrocyte-derived C3 amplifies local inflammation via C3a/C3aR |
| Gene/Protein | C5 | HGNC | HGNC:1241 | Terminal complement component; C5 cleavage products (C5a) recruit immune cells and MAC causes astrocyte lysis (nishiyama2024antiaquaporin4immunecomplex pages 1-2, shimizu2024blood–brainbarrierdisruption pages 20-22) | C5 inhibition (eculizumab/ravulizumab) markedly reduces relapses |
| Gene/Protein | FCGR3A / CD16A | HGNC | HGNC:3617 | FcγR mediating ADCC by NK/NKT and other effector cells; implicated in immune-complex driven cytokine release (nishiyama2024antiaquaporin4immunecomplex pages 6-7, nishiyama2024antiaquaporin4immunecomplex pages 1-2) | CD16A engagement on NKT/NK cells potentiates effector responses to AQP4-immunocomplexes |
| Gene/Protein | CCL2 | HGNC | HGNC:10618 | Chemokine from astrocytes that recruits monocytes/neutrophils and amplifies inflammation (shimizu2024blood–brainbarrierdisruption pages 10-12) | Blocking astrocyte CCL2 reduces AQP4-IgG–induced damage in models |
| Gene/Protein | CXCL8 / IL8 | HGNC | HGNC:6025 | Neutrophil chemoattractant elevated in NMOSD and distinguishes inflammatory signatures (nishiyama2024antiaquaporin4immunecomplex pages 6-7, nishiyama2024antiaquaporin4immunecomplex pages 1-2) | Contributes to neutrophil recruitment and activation |
| Gene/Protein | C1QA | HGNC | HGNC:7087 | Initiator of classical complement pathway binding to IgG–antigen complexes (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4, castagno2024identifyingneutrophilrelatedpathogenic pages 14-16) | C1q binding to AQP4-IgG Fc triggers downstream complement cascade |
| Gene/Protein | STAT3 | HGNC | HGNC:11364 | Transcription factor downstream of IL-6/IL-21 supporting Th17 and B-cell differentiation (nishiyama2024antiaquaporin4immunecomplex pages 6-7, nishiyama2024antiaquaporin4immunecomplex pages 1-2) | Facilitates pathogenic Th17 cytokine program and plasmablast support |
| Gene/Protein | GFAP | HGNC | HGNC:4235 | Astrocytic structural protein released into CSF as a marker of astrocyte damage (shimizu2024blood–brainbarrierdisruption pages 20-22) | CSF GFAP correlates with astrocytopathy severity |
| Biological Process (GO) | complement activation | GO | GO:0006956 | Activation of complement cascade leading to MAC formation and astrocyte injury (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4, nishiyama2024antiaquaporin4immunecomplex pages 1-2) | Central effector mechanism in AQP4-IgG+ lesions |
| Biological Process (GO) | complement activation, classical pathway | GO | GO:0006958 | Classical pathway initiated by C1q binding to AQP4-IgG immune complexes (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4) | Drives C3/C5 cleavage, C5a chemoattraction, and MAC assembly |
| Biological Process (GO) | antibody-dependent cell-mediated cytotoxicity | GO | GO:0001788 | FcγR-mediated killing by neutrophils, macrophages, NK/NKT cells contributing to astrocyte injury (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4, castagno2024identifyingneutrophilrelatedpathogenic pages 14-16) | ADCC complements CDC as an astrocytopathy mechanism |
| Biological Process (GO) | interleukin-6-mediated signaling pathway | GO | GO:0070102 | IL-6 signaling promotes plasmablast/Th17 responses and BBB dysfunction (nishiyama2024antiaquaporin4immunecomplex pages 1-2, shimizu2024blood–brainbarrierdisruption pages 20-22) | Therapeutic target (IL-6R blockade) |
| Biological Process (GO) | T-helper 17 cell differentiation | GO | GO:0042093 | Th17 polarization (IL-6/IL-21/IL-23/STAT3 axis) contributes to inflammation and BBB disruption (nishiyama2024antiaquaporin4immunecomplex pages 1-2, nishiyama2024antiaquaporin4immunecomplex pages 6-7) | Th17 cytokines (IL-17A) noted in patient and ex vivo models |
| Biological Process (GO) | regulation of blood–brain barrier permeability | GO | GO:1901990 | BBB breach allows peripheral AQP4-IgG entry; mediated by endothelial autoantibodies (e.g., anti-GRP78), VEGF/MMPs and cytokines (shimizu2024blood–brainbarrierdisruption pages 10-12, shimizu2024blood–brainbarrierdisruption pages 20-22) | Explains lesion localization (CVOs like area postrema) and triggers |
| Biological Process (GO) | receptor-mediated endocytosis | GO | GO:0006898 | AQP4 internalization after antibody binding can modulate pathogenic outcomes (masciocchi2025conformationalantibodiesto pages 12-17, xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4) | Internalization may influence complement vs non-complement injury balance |
| Biological Process (GO) | glutamate secretion | GO | GO:0014047 | Perturbation of astrocyte glutamate handling contributes to excitotoxic oligodendrocyte/neuron injury (masciocchi2025conformationalantibodiesto pages 12-17, xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4) | Links astrocytopathy to secondary demyelination/neuronal loss |
| Biological Process (GO) | microglial cell activation | GO | GO:0001774 | Microglial activation downstream of astrocyte injury and complement (C3 signaling) driving neuroinflammation (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4) | Microglia amplify synaptic/neuronal damage via C1q/C3 pathways |
| Biological Process (GO) | neutrophil extracellular trap formation | GO | GO:0036349 | NETs and neutrophil proteases contribute to tissue injury and inflammation in NMOSD (castagno2024identifyingneutrophilrelatedpathogenic pages 14-16) | Neutrophil-related pathways are therapeutic targets in NMOSD/MOGAD comparisons |
| Cellular Component (GO-CC) | astrocyte endfoot | GO | GO:0044324 | Site of AQP4 enrichment and initial antibody binding at perivascular interface (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4, shimizu2024blood–brainbarrierdisruption pages 20-22) | Localization explains perivascular complement deposition |
| Cellular Component (note) | orthogonal arrays of particles (OAPs) | — | — | Higher-order AQP4 assemblies (M23-driven) that enhance antibody binding and complement activation (masciocchi2025conformationalantibodiesto pages 12-17) | No standard GO id; use as structural note for AQP4 organization |
| Cellular Component (GO-CC) | plasma membrane | GO | GO:0005886 | Location of AQP4 and immune complex formation on astrocytes (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4) | Membrane-localized events lead to CDC/ADCC |
| Cellular Component (GO-CC) | membrane attack complex | GO | GO:0005579 | MAC deposition on astrocytes causing lytic injury (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4) | Downstream effector of classical complement activation |
| Cellular Component (GO-CC) | extracellular region | GO | GO:0005576 | Space where complement fragments (C3a/C5a) and cytokines act to recruit immune cells (nishiyama2024antiaquaporin4immunecomplex pages 1-2) | Mediates cell recruitment and vascular effects |
| Cellular Component (anatomy note) | perivascular space | UBERON note | UBERON:— (map to perivascular compartments) | Common site of vasculocentric complement deposition and immune infiltrates (masciocchi2025conformationalantibodiesto pages 12-17) | Use UBERON mappings for perivascular compartments when available |
| Cell Type (CL) | astrocyte | CL | CL:0000127 | Primary target cell expressing AQP4; astrocytopathy central to disease (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4, shimizu2024blood–brainbarrierdisruption pages 20-22) | Loss of astrocytes releases GFAP and dysregulates homeostasis |
| Cell Type (CL) | microglial cell | CL | CL:0000129 | CNS-resident effector amplifying complement/C3-mediated neuroinflammation (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4) | Activated microglia contribute to demyelination and neuronal injury |
| Cell Type (CL) | neutrophil | CL | CL:0000775 | Early infiltrating innate effector releasing proteases, ROS and NETs (castagno2024identifyingneutrophilrelatedpathogenic pages 14-16) | Prominent in histopathology and implicated in lesion extension |
| Cell Type (CL) | eosinophil | CL | CL:0000771 | Frequently observed in perivascular infiltrates; contribute to tissue damage (masciocchi2025conformationalantibodiesto pages 12-17) | Eosinophil granule proteins implicated in pathology |
| Cell Type (CL) | NK cell | CL | CL:0000623 | Mediate ADCC via FcγR engagement against antibody-bound astrocytes (nishiyama2024antiaquaporin4immunecomplex pages 1-2) | NK involvement supports non-complement cytotoxic mechanisms |
| Cell Type (CL) | NKT cell | CL | CL:0000814 | Identified as responders to AQP4-immunocomplex + complement producing IL-6/Th17 cytokines (nishiyama2024antiaquaporin4immunecomplex pages 6-7) | Bridge innate/adaptive responses in peripheral PBMC models |
| Cell Type (CL) | plasmablast | CL | CL:0000980 | Peripheral/plasmablast-derived AQP4-IgG production; linked to relapse biology (shimizu2024blood–brainbarrierdisruption pages 20-22) | Targeted by B-cell/plasma-cell directed therapies (e.g., inebilizumab) |
| Cell Type (CL) | B cell | CL | CL:0000236 | Source of AQP4 autoantibodies; antigen presentation and cytokine support roles (shimizu2024blood–brainbarrierdisruption pages 20-22) | B-cell depletion reduces relapse risk |
| Cell Type (CL) | T helper 17 cell | CL | CL:0000894 | Th17 cells contribute IL-17A-driven endothelial activation and inflammation (nishiyama2024antiaquaporin4immunecomplex pages 1-2) | Th17 axis implicated in BBB dysfunction and pathology |
| Anatomy (UBERON) | optic nerve | UBERON | UBERON:0000940 | Frequent clinical target producing optic neuritis in NMOSD (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4) | High AQP4 expression associated with visual loss |
| Anatomy (UBERON) | spinal cord | UBERON | UBERON:0002240 | Site of longitudinally extensive transverse myelitis (LETM) typical of NMOSD (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4) | Astrocyte loss and demyelination drive motor/sensory deficits |
| Anatomy (UBERON) | area postrema | UBERON | UBERON:0002768 | Circumventricular organ with weak BBB enabling symptom-predominant lesions (e.g., intractable vomiting) (shimizu2024blood–brainbarrierdisruption pages 10-12) | CVOs are portals for antibody access to CNS |
| Anatomy (UBERON) | blood–brain barrier | UBERON | UBERON:0002107 | Gatekeeper whose disruption permits peripheral AQP4-IgG entry (shimizu2024blood–brainbarrierdisruption pages 10-12, shimizu2024blood–brainbarrierdisruption pages 20-22) | Target for therapies that stabilize barrier integrity |
| Chemical / Drug (ChEBI / note) | complement C5a | ChEBI? | CHEBI:64038 (if available) | Anaphylatoxin recruiting neutrophils and enhancing inflammation (nishiyama2024antiaquaporin4immunecomplex pages 1-2) | Small fragment of C5; key chemoattractant in lesions |
| Chemical / Drug (note) | eculizumab | — | — | Anti-C5 monoclonal antibody that prevents MAC formation and reduces relapse risk (nishiyama2024antiaquaporin4immunecomplex pages 1-2, shimizu2024blood–brainbarrierdisruption pages 20-22) | Clinical C5 inhibitor with high efficacy in AQP4+ NMOSD |
| Chemical / Drug (note) | ravulizumab | — | — | Long-acting anti-C5 with similar mechanism to eculizumab (nishiyama2024antiaquaporin4immunecomplex pages 1-2) | Approved/used in NMOSD complement blockade contexts |
| Chemical / Drug (note) | satralizumab | — | — | IL-6R blocker reducing relapse risk by attenuating IL-6–driven plasmablast/Th17 activity (nishiyama2024antiaquaporin4immunecomplex pages 1-2, shimizu2024blood–brainbarrierdisruption pages 20-22) | Targets IL-6 signaling pathway |
| Chemical / Drug (note) | inebilizumab | — | — | Anti-CD19 B-cell depleting antibody reducing AQP4-IgG production and relapses (masciocchi2025conformationalantibodiesto pages 12-17, shimizu2024blood–brainbarrierdisruption pages 20-22) | Broad B-lineage depletion therapeutic |


*Table: A concise ontology mapping table linking genes/proteins, GO processes, cellular components, cell types, anatomical regions, and relevant drugs/chemicals to their roles in AQP4-IgG+ NMOSD, with source citations for mechanistic claims (castagno2024identifyingneutrophilrelatedpathogenic pages 14-16, nishiyama2024antiaquaporin4immunecomplex pages 6-7).*

### Evidence Items with Citations (PMID/DOI/URL, date) and Direct Quotes
- Shimizu F, Nakamori M. Blood–Brain Barrier Disruption in Neuroimmunological Disease. IJMS. Oct 2024. DOI: 10.3390/ijms251910625. URL: https://doi.org/10.3390/ijms251910625. Statements include: “At the onset of NMOSD, increased permeability of the BBB causes the entry of circulating AQP4 autoantibodies into the CNS”; and GRP78 autoantibodies “increased BBB permeability in vivo,” with clinical association to more severe myelitis. (shimizu2024blood–brainbarrierdisruption pages 9-10, shimizu2024blood–brainbarrierdisruption pages 10-12)
- Nishiyama S, et al. Anti-aquaporin-4 immune complex stimulates complement-dependent Th17 cytokine release in NMOSD. Scientific Reports. Feb 2024. DOI: 10.1038/s41598-024-53661-5. URL: https://doi.org/10.1038/s41598-024-53661-5. Findings: AQP4‑IgG/AQP4 immune complexes plus complement induced IL‑17A and IL‑6 ex vivo; rituximab blunted IL‑17A. Includes the model that immune complexes engage “CD16A on NKT cells” and complement C5a to drive IL‑6/Th17 responses. (nishiyama2024antiaquaporin4immunecomplex pages 1-2, nishiyama2024antiaquaporin4immunecomplex pages 6-7)
- Xu L, Xu H, Tang C. Aquaporin‑4‑IgG‑seropositive NMOSD: progress of experimental models. Neural Regeneration Research. Jan 2024. DOI: 10.4103/nrr.nrr-d-23-01325. URL: https://doi.org/10.4103/nrr.nrr-d-23-01325. Summarizes: classical complement activation (C1q→MAC) and ADCC by FcγR-expressing neutrophils/macrophages/NK cells; astrocyte C3 upregulation activating microglia; isoform-specific AQP4 internalization. (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4)
- Castagno MES. Identifying neutrophil-related pathogenic pathways in NMOSD and MOGAD. 2024. Highlights neutrophil ROS/proteases, delayed apoptosis, and NET-related pathways; contrasts astrocytopathy/complement in NMOSD vs primary demyelination in MOGAD. (castagno2024identifyingneutrophilrelatedpathogenic pages 14-16)
- Masciocchi S. Conformational antibodies define subgroups... 2025. Summarizes AQP4 M23 OAPs increasing pathogenic binding; neuropathology shows “pronounced loss of astrocytes with vasculocentric complement deposition, and eosinophilic/ neutrophil infiltration,” and implicates glutamate excitotoxicity and ADCC in lesions. (masciocchi2025conformationalantibodiesto pages 12-17)

### Current Applications and Real-World Implementations
- Approved targeted therapies reflect mechanism: C5 inhibitors (eculizumab/ravulizumab), IL‑6R blocker (satralizumab), and B‑cell depleter (inebilizumab). Their clinical success aligns with central roles for complement, IL‑6 signaling, and B‑lineage autoantibody production. (nishiyama2024antiaquaporin4immunecomplex pages 1-2, shimizu2024blood–brainbarrierdisruption pages 20-22)

### Expert Opinions and Synthesis
- The convergent data from 2024 ex vivo immune-complex studies, BBB-focused reviews, and experimental model syntheses support a unifying model of antibody-mediated astrocytopathy with complement and Th17 amplification. The reproducible efficacy of C5 and IL‑6R blockade provides interventional proof-of-mechanism. Emerging BBB-reactive autoantibodies such as anti‑GRP78 likely modulate attack risk/location by transiently increasing barrier permeability, explaining area postrema-predominant syndromes and the vasculocentric pattern of pathology. (shimizu2024blood–brainbarrierdisruption pages 10-12, nishiyama2024antiaquaporin4immunecomplex pages 1-2, xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4)

### Structured Annotations for Knowledge Base Integration
- Genes/Proteins (HGNC): AQP4 (HGNC:633); IL6 (HGNC:6018); C1QA (HGNC:7087); C3 (HGNC:1318); C5 (HGNC:1241); FCGR3A/CD16A (HGNC:3617); CCL2 (HGNC:10618); CXCL8/IL8 (HGNC:6025); STAT3 (HGNC:11364); GFAP (HGNC:4235). (castagno2024identifyingneutrophilrelatedpathogenic pages 14-16, masciocchi2025conformationalantibodiesto pages 12-17, shimizu2024blood–brainbarrierdisruption pages 9-10, shimizu2024blood–brainbarrierdisruption pages 20-22, nishiyama2024antiaquaporin4immunecomplex pages 1-2, xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4, nishiyama2024antiaquaporin4immunecomplex pages 6-7)
- Biological Processes (GO): complement activation (GO:0006956); classical pathway (GO:0006958); ADCC (GO:0001788); IL‑6 signaling (GO:0070102); Th17 differentiation (GO:0042093); regulation of BBB permeability (GO:1901990); receptor-mediated endocytosis (GO:0006898); glutamate secretion (GO:0014047); microglial activation (GO:0001774); NET formation (GO:0036349). (castagno2024identifyingneutrophilrelatedpathogenic pages 14-16, shimizu2024blood–brainbarrierdisruption pages 10-12, nishiyama2024antiaquaporin4immunecomplex pages 1-2, xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4)
- Cellular Components (GO-CC): astrocyte endfoot (GO:0044324); plasma membrane (GO:0005886); membrane attack complex (GO:0005579); extracellular region (GO:0005576); OAPs noted as structural assemblies on astrocyte membranes. (masciocchi2025conformationalantibodiesto pages 12-17, xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4)
- Cell Types (CL): astrocyte (CL:0000127); microglial cell (CL:0000129); neutrophil (CL:0000775); eosinophil (CL:0000771); NK cell (CL:0000623); NKT cell (CL:0000814); plasmablast (CL:0000980); B cell (CL:0000236); Th17 cell (CL:0000894). (castagno2024identifyingneutrophilrelatedpathogenic pages 14-16, nishiyama2024antiaquaporin4immunecomplex pages 1-2, xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4, nishiyama2024antiaquaporin4immunecomplex pages 6-7)
- Anatomy (UBERON): optic nerve (UBERON:0000940); spinal cord (UBERON:0002240); area postrema (UBERON:0002768); blood–brain barrier (UBERON:0002107). (shimizu2024blood–brainbarrierdisruption pages 10-12, xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4)
- Chemicals/Drugs (ChEBI/notes): C5a (CHEBI:64038); eculizumab, ravulizumab, satralizumab, inebilizumab (therapeutics). (nishiyama2024antiaquaporin4immunecomplex pages 1-2, shimizu2024blood–brainbarrierdisruption pages 20-22)

Notes and limitations
- Several key sources are 2024 peer-reviewed articles; where review quality is variable, claims were cross-validated across multiple items. Further precision (e.g., exact MONDO ID confirmation and additional PMIDs for clinical trial efficacy statistics) can be added in subsequent curation passes. (shimizu2024blood–brainbarrierdisruption pages 9-10, shimizu2024blood–brainbarrierdisruption pages 20-22, nishiyama2024antiaquaporin4immunecomplex pages 1-2)

References

1. (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 2-4): Li Xu, Huiming Xu, and Changyong Tang. Aquaporin-4-igg-seropositive neuromyelitis optica spectrum disorders: progress of experimental models based on disease pathogenesis. Neural Regeneration Research, 20:354-365, Jan 2024. URL: https://doi.org/10.4103/nrr.nrr-d-23-01325, doi:10.4103/nrr.nrr-d-23-01325. This article has 13 citations and is from a peer-reviewed journal.

2. (shimizu2024blood–brainbarrierdisruption pages 9-10): Fumitaka Shimizu and Masayuki Nakamori. Blood–brain barrier disruption in neuroimmunological disease. International Journal of Molecular Sciences, 25:10625, Oct 2024. URL: https://doi.org/10.3390/ijms251910625, doi:10.3390/ijms251910625. This article has 35 citations and is from a poor quality or predatory journal.

3. (shimizu2024blood–brainbarrierdisruption pages 10-12): Fumitaka Shimizu and Masayuki Nakamori. Blood–brain barrier disruption in neuroimmunological disease. International Journal of Molecular Sciences, 25:10625, Oct 2024. URL: https://doi.org/10.3390/ijms251910625, doi:10.3390/ijms251910625. This article has 35 citations and is from a poor quality or predatory journal.

4. (nishiyama2024antiaquaporin4immunecomplex pages 1-2): Shuhei Nishiyama, Jin Myong Seok, Amy E. Wright, Itay Lotan, Takahisa Mikami, Natalia C. Drosu, Natasha Bobrowski-Khoury, Monique R. Anderson, Philippe A. Bilodeau, Patrick Schindler, Friedemann Paul, Masashi Aoki, Michael R. Yeaman, Michael Levy, Jacinta M. Behne, Megan K. Behne, Jeffrey L. Bennett, Terrence F. Blaschke, Tanuja Chitnis, Lawrence J. Cook, Michael Levy, Sarah M. Planchon, Pavle Repovic, Claire S. Riley, Terry J. Smith, Anthony Traboulsee, and Michael R. Yeaman. Anti-aquaporin-4 immune complex stimulates complement-dependent th17 cytokine release in neuromyelitis optica spectrum disorders. Scientific Reports, Feb 2024. URL: https://doi.org/10.1038/s41598-024-53661-5, doi:10.1038/s41598-024-53661-5. This article has 17 citations and is from a peer-reviewed journal.

5. (shimizu2024blood–brainbarrierdisruption pages 20-22): Fumitaka Shimizu and Masayuki Nakamori. Blood–brain barrier disruption in neuroimmunological disease. International Journal of Molecular Sciences, 25:10625, Oct 2024. URL: https://doi.org/10.3390/ijms251910625, doi:10.3390/ijms251910625. This article has 35 citations and is from a poor quality or predatory journal.

6. (castagno2024identifyingneutrophilrelatedpathogenic pages 14-16): ME Schroeder Castagno. Identifying neutrophil-related pathogenic pathways involved in nmosd and mogad. Unknown journal, 2024.

7. (nishiyama2024antiaquaporin4immunecomplex pages 6-7): Shuhei Nishiyama, Jin Myong Seok, Amy E. Wright, Itay Lotan, Takahisa Mikami, Natalia C. Drosu, Natasha Bobrowski-Khoury, Monique R. Anderson, Philippe A. Bilodeau, Patrick Schindler, Friedemann Paul, Masashi Aoki, Michael R. Yeaman, Michael Levy, Jacinta M. Behne, Megan K. Behne, Jeffrey L. Bennett, Terrence F. Blaschke, Tanuja Chitnis, Lawrence J. Cook, Michael Levy, Sarah M. Planchon, Pavle Repovic, Claire S. Riley, Terry J. Smith, Anthony Traboulsee, and Michael R. Yeaman. Anti-aquaporin-4 immune complex stimulates complement-dependent th17 cytokine release in neuromyelitis optica spectrum disorders. Scientific Reports, Feb 2024. URL: https://doi.org/10.1038/s41598-024-53661-5, doi:10.1038/s41598-024-53661-5. This article has 17 citations and is from a peer-reviewed journal.

8. (masciocchi2025conformationalantibodiesto pages 12-17): S Masciocchi. Conformational antibodies to proteolipid protein-1 and its peripheral isoform dm20 define clinical subgroups within cns autoimmune demyelinating diseases. Unknown journal, 2025.