---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-31T14:12:18.177638'
end_time: '2026-01-31T14:19:42.162343'
duration_seconds: 443.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neuromyelitis Optica
  mondo_id: ''
  category: Neurological Disorder
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
- **Disease Name:** Neuromyelitis Optica
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Neuromyelitis Optica**.
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
- **Disease Name:** Neuromyelitis Optica
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Neuromyelitis Optica**.
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
- Disease Name: Neuromyelitis Optica Spectrum Disorder (NMOSD; AQP4-IgG–positive form emphasized)
- MONDO ID: —
- Category: Neurological Disorder

Pathophysiology description
NMOSD is a primary autoimmune astrocytopathy driven in most patients by pathogenic IgG1 autoantibodies against the water channel aquaporin-4 (AQP4) concentrated on astrocyte endfeet at the blood–brain barrier (BBB). Binding of AQP4-IgG to AQP4 orthogonal arrays of particles on astrocytes activates the classical complement pathway, culminating in C5b-9 membrane attack complex (MAC)–mediated astrocyte injury with secondary demyelination and axonal damage; antibody-dependent cellular cytotoxicity (ADCC) may also contribute (Kinoshita & Okuno, 2023; NEMOS 2024) (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, kumpfel2024updateonthe pages 1-2). Complement split products (notably C5a) recruit and activate neutrophils, which are key effectors of early BBB disruption and lesion expansion; pharmacologic C5aR blockade attenuates astrocyte loss in vivo, underscoring this pathway (Winkler et al., 2021) (winkler2021bloodbrainbarrierresealing pages 1-2, winkler2021bloodbrainbarrierresealing pages 11-12). IL-6/Th17-axis signaling is integrally linked: ex vivo, AQP4-IgG/AQP4 immune complexes together with complement elicit IL-6 and IL-17A release from patient PBMCs, “prompt[ing] a Th17-biased response” (Nishiyama et al., 2024) (nishiyama2024antiaquaporin4immunecomplex pages 1-2). BBB dysfunction helps initiate CNS access for circulating AQP4-IgG and complement; neutrophils drive structural BBB breakdown, and autoantibodies to endothelial GRP78 have been implicated in BBB impairment, while astrocyte-derived IL-6 further increases permeability (Winkler et al., 2021; Shimizu & Nakamori, 2024) (winkler2021bloodbrainbarrierresealing pages 1-2, shimizu2024blood–brainbarrierdisruption pages 9-10). Peripheral priming may involve gut microbiota molecular mimicry: AQP4-specific T cells cross-react with homologous peptides from Clostridium perfringens, supporting a gut-brain axis in NMOSD (Yao et al., 2024) (yao2024theroleof pages 5-6).

Recent developments and latest research (2023–2024 prioritized)
- Mechanistic immunology: Complement-dependent induction of Th17 cytokines by AQP4-IgG/AQP4 immune complexes with complement (Nishiyama et al., 2024) (nishiyama2024antiaquaporin4immunecomplex pages 1-2). 2024 NEMOS recommendations reaffirm AQP4-IgG as a pathogenic driver and highlight approved targeted agents (Kümpfel et al., 2024) (kumpfel2024updateonthe pages 1-2).
- BBB biology: Newer reviews emphasize IL-6’s role in BBB permeability and the contribution of GRP78 autoantibodies to BBB dysfunction in NMOSD (Shimizu & Nakamori, 2024) (shimizu2024blood–brainbarrierdisruption pages 9-10).
- Microbiome: Molecular mimicry with C. perfringens peptides driving AQP4-reactive Th17 responses is synthesized in 2024 evidence (Yao et al., 2024) (yao2024theroleof pages 5-6).
- Complement patterns distinguishing NMOSD vs MOGAD: During attacks, AQP4+ NMOSD shows higher sC5b-9 (terminal complement complex) than MOGAD, whereas MOGAD exhibits greater upstream C3 degradation products (iC3b) and regulators (C1-INH, factor H), pointing to distinct complement biology (Cho et al., 2024) (cho2024differentiatedpatternof pages 6-9).

Current applications and real-world implementations
- Approved targeted therapies derive directly from mechanistic pathways: complement C5 inhibitors (eculizumab, ravulizumab), anti-CD19 B-cell depletion (inebilizumab), and IL-6 receptor blockade (satralizumab) reduce relapses in AQP4-IgG+ NMOSD—now embedded in consensus recommendations (Kümpfel et al., 2024) (kumpfel2024updateonthe pages 1-2). Mechanistic alignment: C5 blockade interrupts MAC formation and C5a chemotaxis; B-cell depletion reduces AQP4-IgG–secreting plasmablasts; IL-6R blockade dampens plasmablast survival and Th17 polarization (Nishiyama et al., 2024; Kinoshita & Okuno, 2023) (nishiyama2024antiaquaporin4immunecomplex pages 1-2, kinoshita2023autoimmunemediatedastrocytopathy pages 2-5). Clinical impact reported includes marked relapse risk reductions with C5 inhibitors (Nishiyama et al., 2024) (nishiyama2024antiaquaporin4immunecomplex pages 1-2).

Expert opinions and analysis (authoritative sources)
- 2024 NEMOS consensus emphasizes NMOSD as a severe astrocytopathy in which perivascular deposition of IgG and complement (C9neo) with granulocyte infiltrates is typical; management pivots on rapid attack therapy and long-term relapse prevention with targeted biologics (Kümpfel et al., 2024) (kumpfel2024updateonthe pages 1-2).
- Translational studies indicate neutrophils are principal BBB disruptors early in lesion formation, and C5a–C5aR1 signaling is a tractable target (Winkler et al., 2021) (winkler2021bloodbrainbarrierresealing pages 1-2, winkler2021bloodbrainbarrierresealing pages 11-12).

Relevant statistics and biomarker data (recent studies)
- Complement activation biomarkers: sC5b-9 is elevated during AQP4+ NMOSD attacks compared with MOGAD, while MOGAD shows higher iC3b and complement regulators (Cho et al., 2024) (cho2024differentiatedpatternof pages 6-9).
- Fluid biomarkers of injury and permeability: Albumin quotient (Qalb) rises during BBB breakdown; serum/CSF GFAP and NfL increase transiently during attacks and correlate with disability and relapse activity; IL-6 is elevated in CSF/serum and associates with disease activity (Shimizu & Nakamori, 2024) (shimizu2024blood–brainbarrierdisruption pages 9-10).
- Therapeutic effect sizes: C5 inhibition produced large reductions in relapse risk in clinical development (e.g., eculizumab/“PREVENT”, ravulizumab programs) summarized alongside mechanistic rationale (Nishiyama et al., 2024; NEMOS 2024) (nishiyama2024antiaquaporin4immunecomplex pages 1-2, kumpfel2024updateonthe pages 1-2).

Core Pathophysiology
Primary mechanisms
- AQP4-IgG–mediated astrocytopathy with complement activation (classical pathway via C1q, culminating in MAC) leading to astrocyte loss and secondary demyelination; ADCC likely contributes (Kinoshita & Okuno, 2023; NEMOS 2024) (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, kumpfel2024updateonthe pages 1-2).
- C5a-driven recruitment/activation of neutrophils; neutrophil proteases and MMPs disrupt BBB; C5aR blockade reduces lesion burden (Winkler et al., 2021) (winkler2021bloodbrainbarrierresealing pages 1-2, winkler2021bloodbrainbarrierresealing pages 11-12).
- IL-6/Th17 axis engagement: complement-dependent AQP4 immune complexes induce IL-6 and IL-17A, promoting Th17-biased inflammation (Nishiyama et al., 2024) (nishiyama2024antiaquaporin4immunecomplex pages 1-2).
- BBB disruption as an initiating and amplifying step; endothelial-targeted autoantibodies (GRP78) and IL-6 increase permeability (Shimizu & Nakamori, 2024; Winkler et al., 2021) (shimizu2024blood–brainbarrierdisruption pages 9-10, winkler2021bloodbrainbarrierresealing pages 1-2).
- Peripheral priming by microbiota molecular mimicry—AQP4 epitope homology in C. perfringens and Th17 responses (Yao et al., 2024) (yao2024theroleof pages 5-6).

Dysregulated pathways
- Complement cascade (C1q→C3→C5→C5b-9), chemokines/cytokines (IL-6, IL-17A, CXCL10, CXCL13, CCL2), NF-κB stress signaling in astrocytes/microglia (Kinoshita & Okuno, 2023; Nishiyama et al., 2024; NEMOS 2024) (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, nishiyama2024antiaquaporin4immunecomplex pages 1-2, kumpfel2024updateonthe pages 1-2).

Affected cellular processes
- Complement-dependent cytotoxicity, ADCC against astrocytes; neutrophil degranulation/NETosis; microglial activation via complement receptors; Th17 differentiation and cytokine release; BBB tight-junction disruption (Winkler et al., 2021; Kinoshita & Okuno, 2023; Nishiyama et al., 2024) (winkler2021bloodbrainbarrierresealing pages 1-2, kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, nishiyama2024antiaquaporin4immunecomplex pages 1-2).

Key Molecular Players
- Genes/Proteins: AQP4 (HGNC:AQP4), Complement C1q (HGNC:C1QA/B/C), C3 (HGNC:C3), C5/C5a (HGNC:C5), MAC/C5b-9; cytokines/chemokines IL-6 (HGNC:IL6), IL-17A (HGNC:IL17A), CXCL10 (HGNC:CXCL10), CXCL13 (HGNC:CXCL13), CCL2 (HGNC:CCL2); stress/inflammatory mediator CHI3L1 (HGNC:CHI3L1) (Kinoshita & Okuno, 2023; Nishiyama et al., 2024; NEMOS 2024) (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, nishiyama2024antiaquaporin4immunecomplex pages 1-2, kumpfel2024updateonthe pages 1-2).
- Chemical entities: ATP (danger signal; CHEBI:ATP), sC5b-9 (terminal complement complex) (Kinoshita & Okuno, 2023; Cho et al., 2024) (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, cho2024differentiatedpatternof pages 6-9).
- Cell types: Astrocytes (CL:astrocyte; primary target), B cells/plasmablasts (AQP4-IgG source), neutrophils and eosinophils (granulocyte effectors), microglia (innate amplification), Th17 CD4+ T cells (effector lineage) (Kinoshita & Okuno, 2023; Winkler et al., 2021; Nishiyama et al., 2024; NEMOS 2024) (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, winkler2021bloodbrainbarrierresealing pages 1-2, nishiyama2024antiaquaporin4immunecomplex pages 1-2, kumpfel2024updateonthe pages 1-2).
- Anatomical locations: Optic nerve, spinal cord (longitudinally extensive transverse myelitis), area postrema and hypothalamus—sites with characteristic lesion patterns (NEMOS 2024; Kinoshita & Okuno, 2023) (kumpfel2024updateonthe pages 1-2, kinoshita2023autoimmunemediatedastrocytopathy pages 2-5).

Biological Processes (GO-like annotation)
- Complement-dependent cytotoxicity (GO:complement-dependent cytotoxicity) against astrocytes (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, kumpfel2024updateonthe pages 1-2).
- Antibody-dependent cellular cytotoxicity (GO:antibody-dependent cellular cytotoxicity) (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5).
- NF-κB signaling (GO:NF-kappaB signaling) upregulated in antibody/complement-stressed astrocytes (nishiyama2024antiaquaporin4immunecomplex pages 1-2).
- Th17 cell differentiation (GO:Th17 cell differentiation) driven by IL-6 and complement signals (nishiyama2024antiaquaporin4immunecomplex pages 1-2).
- Blood–brain barrier disruption (GO:blood–brain barrier disruption) mediated by neutrophils and inflammatory mediators (winkler2021bloodbrainbarrierresealing pages 1-2, shimizu2024blood–brainbarrierdisruption pages 9-10).

Cellular Components
- Astrocyte plasma membrane/endfeet, perivascular space; complement deposition (C1q, C3 fragments) and terminal MAC on astrocyte membranes; extracellular space enriched in cytokines/chemokines (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, kumpfel2024updateonthe pages 1-2).

Disease Progression (sequence of events)
1) Peripheral priming: gut microbial mimicry primes AQP4-reactive T cells (C. perfringens epitope homology) and Th17 bias (Yao et al., 2024) (yao2024theroleof pages 5-6).
2) BBB entry: pre-existing inflammation and BBB loosening (neutrophil-mediated, IL-6–driven, GRP78 autoantibodies) allow serum AQP4-IgG and complement into the CNS (Winkler et al., 2021; Shimizu & Nakamori, 2024) (winkler2021bloodbrainbarrierresealing pages 1-2, shimizu2024blood–brainbarrierdisruption pages 9-10).
3) Astrocyte injury: AQP4-IgG binds AQP4, fixes complement (C1q→C5b-9), triggers astrocyte lysis and ADCC (Kinoshita & Okuno, 2023; NEMOS 2024) (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, kumpfel2024updateonthe pages 1-2).
4) Innate amplification: C5a recruits neutrophils; microglia are activated by complement fragments and danger signals (ATP), amplifying inflammation and BBB damage (Winkler et al., 2021; Kinoshita & Okuno, 2023) (winkler2021bloodbrainbarrierresealing pages 1-2, kinoshita2023autoimmunemediatedastrocytopathy pages 2-5).
5) Secondary tissue loss: oligodendrocyte/myelin injury and axonal dysfunction accrue downstream of astrocytopathy (NEMOS 2024) (kumpfel2024updateonthe pages 1-2).

Phenotypic Manifestations and Imaging Features
- Clinical phenotypes tightly map to astrocyte-rich regions: severe optic neuritis, longitudinally extensive transverse myelitis (central cord gray), area postrema syndrome (intractable vomiting/hiccups), and hypothalamic lesions; perivascular complement deposition and granulocyte infiltrates are typical (Kümpfel et al., 2024; Kinoshita & Okuno, 2023) (kumpfel2024updateonthe pages 1-2, kinoshita2023autoimmunemediatedastrocytopathy pages 2-5).
- Distinguishing from MOGAD/MS: AQP4+ NMOSD shows higher terminal pathway activity (sC5b-9) than MOGAD, which exhibits more upstream C3 degradation (iC3b)/regulatory signatures; clinical/MRI distribution differs from MS and MOGAD (Cho et al., 2024; NEMOS 2024) (cho2024differentiatedpatternof pages 6-9, kumpfel2024updateonthe pages 1-2).

Evidence quotes (selected)
- “Co-stimulation of PBMCs with AQP4-IgG/AQP4 immunocomplex and complement prompts a Th17-biased response” (Nishiyama et al., 2024) (nishiyama2024antiaquaporin4immunecomplex pages 1-2).
- In experimental NMOSD, “polymorphonuclear leukocytes (PMNs) are the main mediators of BBB disruption,” and C5aR antagonism reduced astrocyte loss (Winkler et al., 2021) (winkler2021bloodbrainbarrierresealing pages 1-2, winkler2021bloodbrainbarrierresealing pages 11-12).

Gene/Protein annotations with ontology terms (HGNC, GO)
- AQP4 (HGNC:AQP4): antigenic target; processes—complement-dependent cytotoxicity; cellular component—astrocyte endfeet (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, kumpfel2024updateonthe pages 1-2).
- IL6 (HGNC:IL6): promotes plasmablast survival and Th17 polarization; processes—Th17 differentiation, BBB permeability (nishiyama2024antiaquaporin4immunecomplex pages 1-2, shimizu2024blood–brainbarrierdisruption pages 9-10).
- IL17A (HGNC:IL17A): effector cytokine of Th17; processes—neuroinflammation amplification (nishiyama2024antiaquaporin4immunecomplex pages 1-2).
- C1q (HGNC:C1QA/B/C), C3 (HGNC:C3), C5 (HGNC:C5): complement activation cascade culminating in MAC (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, winkler2021bloodbrainbarrierresealing pages 11-12, kumpfel2024updateonthe pages 1-2).
- CXCL10 (HGNC:CXCL10), CXCL13 (HGNC:CXCL13), CCL2 (HGNC:CCL2): chemoattractants for T and B cells and myeloid cells (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, kumpfel2024updateonthe pages 1-2).

Phenotype associations (HP terms)
- Optic neuritis (HP term) and longitudinally extensive transverse myelitis; area postrema syndrome (intractable vomiting/hiccups)—clinical correlates of astrocytopathy (Kümpfel et al., 2024) (kumpfel2024updateonthe pages 1-2).

Cell type involvement (CL terms)
- CL:astrocyte; CL:neutrophil; CL:eosinophil; CL:B cell/CL:plasmablast; CL:CD4+ Th17 T cell; CL:microglial cell (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, winkler2021bloodbrainbarrierresealing pages 1-2, nishiyama2024antiaquaporin4immunecomplex pages 1-2, kumpfel2024updateonthe pages 1-2).

Anatomical locations (UBERON terms)
- UBERON:optic nerve; UBERON:spinal cord; UBERON:area postrema; UBERON:hypothalamus; UBERON:blood–brain barrier (kumpfel2024updateonthe pages 1-2, winkler2021bloodbrainbarrierresealing pages 1-2, shimizu2024blood–brainbarrierdisruption pages 9-10).

Chemical entities (CHEBI terms)
- CHEBI:ATP (danger signal); terminal complement complex (sC5b-9) as a biomarker of complement activation (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, cho2024differentiatedpatternof pages 6-9).

Mechanism-informed therapies (rationale with data)
- Complement C5 inhibitors (eculizumab, ravulizumab): block C5 cleavage to prevent C5a chemotaxis and MAC formation; associated with large relapse risk reductions in AQP4+ NMOSD (Nishiyama et al., 2024; NEMOS 2024) (nishiyama2024antiaquaporin4immunecomplex pages 1-2, kumpfel2024updateonthe pages 1-2).
- B-cell depletion (inebilizumab): targets CD19 lineage including plasmablasts producing AQP4-IgG; reduces relapse risk (NEMOS 2024) (kumpfel2024updateonthe pages 1-2).
- IL-6R blockade (satralizumab): interrupts IL-6–dependent plasmablast survival and Th17 polarization; reduces relapses (NEMOS 2024; Nishiyama et al., 2024) (kumpfel2024updateonthe pages 1-2, nishiyama2024antiaquaporin4immunecomplex pages 1-2).

Embedded structured summary (ontology-mapped)
| Entity | Type | Ontology (ID system) | Role in NMOSD pathophysiology (one sentence) | Key evidence | URL / Year |
|---|---|---:|---|---|---|
| AQP4 | Gene/Protein | HGNC:AQP4 | Water-channel on astrocyte endfeet and primary antigenic target; AQP4-IgG binding triggers complement activation and astrocyte lysis. | (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, kumpfel2024updateonthe pages 1-2) | https://doi.org/10.1186/s41232-023-00291-5 (2023) |
| IL6 | Cytokine | HGNC:IL6 | Pro-inflammatory cytokine elevated in serum/CSF during attacks; promotes plasmablast survival and Th17 polarization. | (nishiyama2024antiaquaporin4immunecomplex pages 1-2, correale2025inductionofimmune pages 3-4) | https://doi.org/10.1038/s41598-024-53661-5 (2024) |
| IL17A | Cytokine | HGNC:IL17A | Effector Th17 cytokine contributing to CNS inflammation downstream of complement-dependent stimulation. | (nishiyama2024antiaquaporin4immunecomplex pages 1-2) | https://doi.org/10.1038/s41598-024-53661-5 (2024) |
| CXCL10 | Cytokine/Chemokine | HGNC:CXCL10 | IFN-inducible chemokine raised in peripheral/lesional signatures that recruits T cells and associates with inflammatory signaling. | (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, kumpfel2024updateonthe pages 1-2) | https://doi.org/10.1007/s00415-023-11910-z (2024) |
| CXCL13 | Chemokine | HGNC:CXCL13 | B-cell/Tfh chemokine elevated in AQP4-NMOSD serum proteomics, indicating B-cell follicular activity. | (kumpfel2024updateonthe pages 1-2) | https://doi.org/10.1007/s00415-023-11910-z (2024) |
| CCL2 | Chemokine | HGNC:CCL2 | Astrocyte-derived chemoattractant that amplifies leukocyte recruitment and astrocyte injury in AQP4-IgG contexts. | (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, nishiyama2024antiaquaporin4immunecomplex pages 1-2) | https://doi.org/10.1186/s41232-023-00291-5 (2023) |
| CHI3L1 | Protein (chitinase-like) | HGNC:CHI3L1 | Astrocyte-intrinsic inflammatory amplifier implicated in promoting demyelination and upregulating complement/cytokine responses. | (nishiyama2024antiaquaporin4immunecomplex pages 1-2, kinoshita2023autoimmunemediatedastrocytopathy pages 2-5) | https://doi.org/10.1038/s41598-024-53661-5 (2024) |
| Complement C1q | Complement component | HGNC:C1QA/C1QB/C1QC | Classical pathway initiator that binds immune complexes and promotes downstream complement cascade activation in lesions. | (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, kumpfel2024updateonthe pages 1-2) | https://doi.org/10.1186/s41232-023-00291-5 (2023) |
| Complement C3 | Complement component | HGNC:C3 | Central complement protein whose cleavage/amplification (iC3b etc.) marks complement activation and opsonization in NMOSD. | (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, nishiyama2024antiaquaporin4immunecomplex pages 1-2) | https://doi.org/10.1186/s41232-023-00291-5 (2023) |
| Complement C5 / C5a | Complement component (anaphylatoxin) | HGNC:C5 | Terminal pathway mediator; C5a is a potent chemoattractant driving neutrophil recruitment and inflammation. | (winkler2021bloodbrainbarrierresealing pages 1-2, winkler2021bloodbrainbarrierresealing pages 11-12) | https://doi.org/10.1172/jci141694 (2021) |
| C5b-9 (MAC) | Complement complex | (Terminal complement complex / MAC) | Forms the membrane attack complex that causes astrocyte membrane damage and contributes to astrocytolysis. | (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, kumpfel2024updateonthe pages 1-2) | https://doi.org/10.1186/s41232-023-00291-5 (2023) |
| Microglia | Cell type | CL:microglial cell | CNS-resident innate immune cells activated by astrocyte injury and complement fragments (C3a/C5a), amplifying local inflammation. | (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, winkler2021bloodbrainbarrierresealing pages 1-2) | https://doi.org/10.1172/jci141694 (2021) |
| Neutrophils / NETs | Cell type / process | CL:neutrophil; GO:neutrophil extracellular trap formation | Early infiltrating granulocytes that contribute proteases, NETs and BBB disruption and are recruited by C5a and astrocyte-derived chemokines. | (winkler2021bloodbrainbarrierresealing pages 1-2, kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, nishiyama2024antiaquaporin4immunecomplex pages 1-2) | https://doi.org/10.1172/jci141694 (2021) |
| Eosinophils | Cell type | CL:eosinophil | Granulocytes found in perivascular NMOSD lesions that participate in inflammatory tissue damage alongside neutrophils. | (kumpfel2024updateonthe pages 1-2, kinoshita2023autoimmunemediatedastrocytopathy pages 2-5) | https://doi.org/10.1007/s00415-023-11910-z (2024) |
| B cells / Plasmablasts | Cell type | CL:B cell / CL:plasmablast | Source of pathogenic AQP4-IgG (peripheral and intrathecal plasmablasts), target of anti-CD20/CD19 therapies. | (nishiyama2024antiaquaporin4immunecomplex pages 1-2, kumpfel2024updateonthe pages 1-2) | https://doi.org/10.1038/s41598-024-53661-5 (2024) |
| Th17 cells | Cell type | CL:CD4-positive, alpha-beta T cell (Th17) | CD4+ Th17 lineage produces IL-17A and collaborates with IL-6-driven responses to mediate CNS inflammation in NMOSD. | (nishiyama2024antiaquaporin4immunecomplex pages 1-2, correale2025inductionofimmune pages 3-4) | https://doi.org/10.1038/s41598-024-53661-5 (2024) |
| Astrocytes | Cell type | CL:astrocyte | Primary cellular target (AQP4-rich endfeet) whose antibody-mediated necrosis initiates downstream demyelination and neuronal injury. | (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, winkler2021bloodbrainbarrierresealing pages 1-2) | https://doi.org/10.1186/s41232-023-00291-5 (2023) |
| Blood–brain barrier (BBB) | Anatomical / barrier structure | UBERON:blood–brain barrier | Disruption permits peripheral AQP4-IgG and complement to access astrocyte endfeet and is mediated early by PMNs and autoantibodies (e.g., anti-GRP78). | (winkler2021bloodbrainbarrierresealing pages 1-2, winkler2021bloodbrainbarrierresealing pages 11-12, kinoshita2023autoimmunemediatedastrocytopathy pages 2-5) | https://doi.org/10.1172/jci141694 (2021) |
| Optic nerve | Anatomical site | UBERON:optic nerve | A frequent clinical target producing severe optic neuritis; lesions reflect astrocyte loss, complement deposition and secondary axonal injury. | (kumpfel2024updateonthe pages 1-2, kinoshita2023autoimmunemediatedastrocytopathy pages 2-5) | https://doi.org/10.1007/s00415-023-11910-z (2024) |
| Spinal cord (LETM) | Anatomical site | UBERON:spinal cord (longitudinally extensive transverse myelitis) | Characteristic longitudinal central gray/cord lesions spanning ≥3 vertebral segments driven by astrocytopathy and complement-mediated injury. | (kumpfel2024updateonthe pages 1-2, kinoshita2023autoimmunemediatedastrocytopathy pages 2-5) | https://doi.org/10.1007/s00415-023-11910-z (2024) |
| Area postrema | Anatomical site | UBERON:area postrema | Brainstem region commonly affected in NMOSD (intractable vomiting/hiccups) due to local astrocyte-targeted inflammation. | (kumpfel2024updateonthe pages 1-2) | https://doi.org/10.1007/s00415-023-11910-z (2024) |
| Hypothalamus | Anatomical site | UBERON:hypothalamus | Reported site of involvement reflecting broader astrocyte vulnerability beyond optic nerve/spinal cord. | (kumpfel2024updateonthe pages 1-2, kinoshita2023autoimmunemediatedastrocytopathy pages 2-5) | https://doi.org/10.1007/s00415-023-11910-z (2024) |
| Complement-dependent cytotoxicity (CDC) | Process | GO:complement-dependent cytotoxicity | Mechanism by which AQP4-IgG fixes classical complement and drives MAC formation and astrocyte lysis. | (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, winkler2021bloodbrainbarrierresealing pages 11-12, kumpfel2024updateonthe pages 1-2) | https://doi.org/10.1172/jci141694 (2021) |
| Antibody-dependent cellular cytotoxicity (ADCC) | Process | GO:antibody-dependent cellular cytotoxicity | Fc-mediated engagement of innate effector cells (NK, neutrophils) by AQP4-IgG contributing to astrocyte injury. | (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5, nishiyama2024antiaquaporin4immunecomplex pages 1-2) | https://doi.org/10.1186/s41232-023-00291-5 (2023) |
| NF-κB signaling | Process / pathway | GO:NF-kappaB signaling | Upregulated in complement/antibody-driven astrocyte stress responses and linked to IL-6 transcription and inflammation. | (nishiyama2024antiaquaporin4immunecomplex pages 1-2, kinoshita2023autoimmunemediatedastrocytopathy pages 2-5) | https://doi.org/10.1038/s41598-024-53661-5 (2024) |
| Th17 polarization | Process | GO:Th17 cell differentiation | IL-6 and complement-dependent signals promote Th17 differentiation and IL-17A production that amplify CNS inflammation. | (nishiyama2024antiaquaporin4immunecomplex pages 1-2, correale2025inductionofimmune pages 3-4) | https://doi.org/10.1038/s41598-024-53661-5 (2024) |
| BBB disruption | Process | GO:blood–brain barrier disruption | Early event enabling pathogenic antibody/complement entry; driven by PMN recruitment, endothelial autoantibodies and inflammatory mediators. | (winkler2021bloodbrainbarrierresealing pages 1-2, winkler2021bloodbrainbarrierresealing pages 11-12) | https://doi.org/10.1172/jci141694 (2021) |
| ATP (danger signal) | Chemical / metabolite | CHEBI:ATP | Released from damaged astrocytes, ATP contributes to microglial activation and propagation of inflammatory signaling. | (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5) | https://doi.org/10.1186/s41232-023-00291-5 (2023) |


*Table: Concise ontology-mapped summary of key entities, processes and anatomical sites in AQP4-IgG-positive NMOSD pathophysiology with direct evidence citations (pqac IDs) and source links/years.*

Evidence items (with URLs and dates)
- Kinoshita M, Okuno T. Autoimmune-mediated astrocytopathy. Inflammation and Regeneration. 2023 Jul. https://doi.org/10.1186/s41232-023-00291-5 (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5)
- Nishiyama S, et al. Anti-aquaporin-4 immune complex stimulates complement-dependent Th17 cytokine release in NMOSD. Scientific Reports. 2024 Feb. https://doi.org/10.1038/s41598-024-53661-5 (nishiyama2024antiaquaporin4immunecomplex pages 1-2)
- Winkler A, et al. Blood-brain barrier resealing in neuromyelitis optica occurs independently of astrocyte regeneration. J Clin Invest. 2021 Mar. https://doi.org/10.1172/jci141694 (winkler2021bloodbrainbarrierresealing pages 1-2, winkler2021bloodbrainbarrierresealing pages 11-12)
- Kümpfel T, et al. NEMOS revised recommendations (Part II). Journal of Neurology. 2024 Sep. https://doi.org/10.1007/s00415-023-11910-z (kumpfel2024updateonthe pages 1-2)
- Shimizu F, Nakamori M. Blood–brain barrier disruption in neuroimmunological disease. IJMS. 2024 Oct. https://doi.org/10.3390/ijms251910625 (shimizu2024blood–brainbarrierdisruption pages 9-10)
- Yao S-Q, et al. The Role of Gut Microbiota in NMOSD. IJMS. 2024 Mar. https://doi.org/10.3390/ijms25063179 (yao2024theroleof pages 5-6)
- Cho E B, et al. Differentiated complement activation: MOGAD vs AQP4-NMOSD. Frontiers in Immunology. 2024 Mar. https://doi.org/10.3389/fimmu.2024.1320094 (cho2024differentiatedpatternof pages 6-9)

Notes and limitations
- While landmark historical studies (e.g., initial AQP4-IgG discoveries and PREVENT trial primary reports) predate 2023, this report prioritized 2023–2024 sources for mechanistic updates and consensus. Where exact biomarker thresholds are needed (e.g., quantitative GFAP cutoffs), readers should consult assay-specific studies; here we cite directionality and associations from recent reviews (shimizu2024blood–brainbarrierdisruption pages 9-10).


References

1. (kinoshita2023autoimmunemediatedastrocytopathy pages 2-5): Makoto Kinoshita and Tatsusada Okuno. Autoimmune-mediated astrocytopathy. Inflammation and Regeneration, Jul 2023. URL: https://doi.org/10.1186/s41232-023-00291-5, doi:10.1186/s41232-023-00291-5. This article has 4 citations.

2. (kumpfel2024updateonthe pages 1-2): T. Kümpfel, Katrin Giglhuber, O. Aktas, I. Ayzenberg, J. Bellmann-Strobl, Vivien Häußler, J. Havla, K. Hellwig, M. W. Hümmert, S. Jarius, I. Kleiter, Luisa Klotz, M. Krumbholz, Friedemann Paul, M. Ringelstein, K. Ruprecht, M. Senel, J. Stellmann, F. Bergh, C. Trebst, H. Tumani, C. Warnke, B. Wildemann, and A. Berthele. Update on the diagnosis and treatment of neuromyelitis optica spectrum disorders (nmosd) – revised recommendations of the neuromyelitis optica study group (nemos). part ii: attack therapy and long-term management. Journal of Neurology, 271:141-176, Sep 2024. URL: https://doi.org/10.1007/s00415-023-11910-z, doi:10.1007/s00415-023-11910-z. This article has 198 citations and is from a domain leading peer-reviewed journal.

3. (winkler2021bloodbrainbarrierresealing pages 1-2): Anne Winkler, Claudia Wrzos, Michael Haberl, Marie-Theres Weil, Ming Gao, Wiebke Möbius, Francesca Odoardi, Dietmar R. Thal, Mayland Chang, Ghislain Opdenakker, Jeffrey L. Bennett, Stefan Nessler, and Christine Stadelmann. Blood-brain barrier resealing in neuromyelitis optica occurs independently of astrocyte regeneration. The Journal of clinical investigation, Mar 2021. URL: https://doi.org/10.1172/jci141694, doi:10.1172/jci141694. This article has 50 citations.

4. (winkler2021bloodbrainbarrierresealing pages 11-12): Anne Winkler, Claudia Wrzos, Michael Haberl, Marie-Theres Weil, Ming Gao, Wiebke Möbius, Francesca Odoardi, Dietmar R. Thal, Mayland Chang, Ghislain Opdenakker, Jeffrey L. Bennett, Stefan Nessler, and Christine Stadelmann. Blood-brain barrier resealing in neuromyelitis optica occurs independently of astrocyte regeneration. The Journal of clinical investigation, Mar 2021. URL: https://doi.org/10.1172/jci141694, doi:10.1172/jci141694. This article has 50 citations.

5. (nishiyama2024antiaquaporin4immunecomplex pages 1-2): Shuhei Nishiyama, Jin Myong Seok, Amy E. Wright, Itay Lotan, Takahisa Mikami, Natalia C. Drosu, Natasha Bobrowski-Khoury, Monique R. Anderson, Philippe A. Bilodeau, Patrick Schindler, Friedemann Paul, Masashi Aoki, Michael R. Yeaman, Michael Levy, Jacinta M. Behne, Megan K. Behne, Jeffrey L. Bennett, Terrence F. Blaschke, Tanuja Chitnis, Lawrence J. Cook, Michael Levy, Sarah M. Planchon, Pavle Repovic, Claire S. Riley, Terry J. Smith, Anthony Traboulsee, and Michael R. Yeaman. Anti-aquaporin-4 immune complex stimulates complement-dependent th17 cytokine release in neuromyelitis optica spectrum disorders. Scientific Reports, Feb 2024. URL: https://doi.org/10.1038/s41598-024-53661-5, doi:10.1038/s41598-024-53661-5. This article has 17 citations and is from a peer-reviewed journal.

6. (shimizu2024blood–brainbarrierdisruption pages 9-10): Fumitaka Shimizu and Masayuki Nakamori. Blood–brain barrier disruption in neuroimmunological disease. International Journal of Molecular Sciences, 25:10625, Oct 2024. URL: https://doi.org/10.3390/ijms251910625, doi:10.3390/ijms251910625. This article has 41 citations and is from a poor quality or predatory journal.

7. (yao2024theroleof pages 5-6): Shi-Qi Yao, Xiayin Yang, Ling-Ping Cen, and Shaoying Tan. The role of gut microbiota in neuromyelitis optica spectrum disorder. International Journal of Molecular Sciences, 25:3179, Mar 2024. URL: https://doi.org/10.3390/ijms25063179, doi:10.3390/ijms25063179. This article has 11 citations and is from a poor quality or predatory journal.

8. (cho2024differentiatedpatternof pages 6-9): Eun Bin Cho, Ju-Hong Min, Patrick Waters, Miyoung Jeon, Eun-Seon Ju, Ho Jin Kim, Su-Hyun Kim, Ha Young Shin, Sa-Yoon Kang, Young-Min Lim, Sun-Young Oh, Hye Lim Lee, Eunhee Sohn, Sang-Soo Lee, Jeeyoung Oh, Sunyoung Kim, So-Young Huh, Joong-Yang Cho, Jin Myoung Seok, Byung-Jo Kim, and Byoung Joon Kim. Differentiated pattern of complement system activation between mog-igg-associated disease and aqp4-igg-positive neuromyelitis optica spectrum disorder. Frontiers in Immunology, Mar 2024. URL: https://doi.org/10.3389/fimmu.2024.1320094, doi:10.3389/fimmu.2024.1320094. This article has 7 citations and is from a peer-reviewed journal.

9. (correale2025inductionofimmune pages 3-4): J. Correale and Edgar Carnero Contentti. Induction of immune tolerance in nmosd and mogad. Therapeutic Advances in Neurological Disorders, Jan 2025. URL: https://doi.org/10.1177/17562864251357393, doi:10.1177/17562864251357393. This article has 3 citations and is from a peer-reviewed journal.