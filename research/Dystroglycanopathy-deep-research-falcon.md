---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-07T05:44:54.189240'
end_time: '2026-03-07T06:03:16.380507'
duration_seconds: 1102.19
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dystroglycanopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 53
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Dystroglycanopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Dystroglycanopathy**.
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
- **Disease Name:** Dystroglycanopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Dystroglycanopathy**.
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


# Dystroglycanopathy Pathophysiology Research Report (2023–2024 emphasis)

## 0. Scope and identifiers
**Target disease:** Dystroglycanopathy (a spectrum of disorders caused by functional defects of dystroglycan—most commonly impaired glycosylation of α-dystroglycan). (cubilla2023dystroglycanopathiesgeneticbases pages 4-5, cubilla2023dystroglycanopathiesgeneticbases pages 3-4)

**MONDO ID:** Not directly present in the retrieved full-text sources. The Open Targets evidence snapshot used in this run indicates MONDO_0018276 (“muscular dystrophy-dystroglycanopathy”) and MONDO_0018282 (“neuromuscular disease caused by qualitative or quantitative defects of alpha-dystroglycan”), but those identifiers were returned as database output rather than as citable literature context in this report. Therefore, MONDO IDs should be confirmed via MONDO/Orphanet ontology lookup for production use. (benarroch2024the2024version pages 8-9, cubilla2023dystroglycanopathiesgeneticbases pages 4-5)

## 1. Key concepts, definitions, and current understanding
### 1.1 Definition and classification
Dystroglycanopathies are muscular dystrophies caused by abnormal O-glycosylation of **α-dystroglycan (α-DG)**, a core component of the **dystrophin glycoprotein complex (DGC)** that connects the extracellular matrix (ECM) to the intracellular actin cytoskeleton. (cubilla2023dystroglycanopathiesgeneticbases pages 3-4, cubilla2023dystroglycanopathiesgeneticbases pages 4-5)

A common nosologic division is:
- **Primary dystroglycanopathy**: pathogenic variants in **DAG1** (dystroglycan itself). (cubilla2023dystroglycanopathiesgeneticbases pages 4-5)
- **Secondary dystroglycanopathy**: variants in the ≈20+ genes needed for α-DG functional glycosylation (O-mannosylation, nucleotide-sugar synthesis, glycan extension, and in some cases Golgi trafficking). (cubilla2023dystroglycanopathiesgeneticbases pages 4-5, cubilla2023dystroglycanopathiesgeneticbases pages 3-4)

### 1.2 Clinical spectrum (phenotype continuum)
The dystroglycanopathy spectrum spans **severe congenital multisystem disease** to **later-onset limb-girdle muscular dystrophy** phenotypes:
- **Walker–Warburg syndrome (WWS)** is described as among the most severe forms, often detectable prenatally, featuring congenital muscular dystrophy plus major brain and eye anomalies. (cubilla2023dystroglycanopathiesgeneticbases pages 8-9)
- **Muscle-eye-brain (MEB) / Fukuyama congenital muscular dystrophy (FCMD)** are classic congenital α-dystroglycanopathy syndromes with prominent CNS/ocular involvement. (cubilla2023dystroglycanopathiesgeneticbases pages 7-8)
- **Limb-girdle muscular dystrophy forms** such as **LGMD2I/R9 (FKRP-related)** represent milder ends of the same mechanistic axis. (cubilla2023dystroglycanopathiesgeneticbases pages 8-9, unnikrishnan2023phenotypegenotypecharacterization pages 1-3)

## 2. Core pathophysiology: molecular → cellular → tissue mechanisms
### 2.1 Central biochemical lesion: loss of functional matriglycan on α-dystroglycan
In dystroglycanopathies, mutations reduce or abolish assembly of a specialized O-mannose–derived glycan culminating in **matriglycan**, a repeating disaccharide polymer on α-DG ([-3Xyl-α1,3-GlcA-β1-]n). This “functional glycan” is the key determinant of α-DG binding to ECM laminin-G (LG) domain proteins. (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, koff2023proteinomannosylationone pages 2-4)

Matriglycan mediates α-DG interactions with ECM ligands such as **laminin**, **agrin**, **perlecan**, and **pikachurin**, enabling mechanical stability and signaling functions across tissues (skeletal muscle, brain, eye, heart). (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, lu2024breakdownof pages 1-2)

### 2.2 Core M3 / matriglycan biosynthesis pathway (current pathway model)
Recent reviews synthesize the pathway as: 
1) **ER initiation** by **POMT1/POMT2** (O-mannosylation). (koff2023proteinomannosylationone pages 2-4, koff2023proteinomannosylationone pages 5-6)
2) **Core M3 elaboration** (e.g., POMGNT2, B3GALNT2). (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, koff2023proteinomannosylationone pages 2-4)
3) **Phosphorylation** by **POMK**, generating the phosphorylated “nucleus” needed for downstream steps. (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, koff2023proteinomannosylationone pages 5-6)
4) **Ribitol-phosphate pathway**: **ISPD/CRPPA** generates CDP-ribitol; **FKTN** and **FKRP** transfer ribitol-5-phosphate, enabling later LARGE1-dependent extension. (lu2024breakdownof pages 1-2, lu2024breakdownof pages 9-10)
5) **Primer/linker assembly** (e.g., TMEM5/RXYLT1 and B4GAT1) and finally
6) **Polymerization** by **LARGE1**, which extends matriglycan. (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, koff2023proteinomannosylationone pages 2-4)

Mechanistic consequence: reduction of matriglycan decreases α-DG ligand binding, disrupting the DGC-mediated ECM–cytoskeleton linkage and causing contraction-induced injury and downstream inflammation/fibrosis/regeneration cycles in muscle. (lu2024breakdownof pages 1-2, unnikrishnan2023phenotypegenotypecharacterization pages 1-3)

### 2.3 Tissue-level mechanisms
#### Skeletal muscle
Loss of functional α-DG glycosylation weakens the sarcolemma–basal lamina connection, contributing to muscle fiber fragility and dystrophic degeneration. FKRP encodes a ribitol-5-phosphate transferase required for functional laminin-binding glycosylation on the sarcolemma. (lu2024breakdownof pages 1-2, unnikrishnan2023phenotypegenotypecharacterization pages 1-3)

#### Brain development, basement membranes, and neuronal migration
Defective O-mannosylation (e.g., POMT loss) abolishes α-DG–ECM interactions required for pial basement membrane integrity, contributing to brain malformations and migration defects (cobblestone lissencephaly spectrum). (koff2023proteinomannosylationone pages 5-6, NCT00313677 chunk 2)

#### Synapses and excitability (seizure biology)
A 2024 eLife study provides strong mechanistic evidence that **severe dystroglycan glycosylation loss in forebrain** disrupts development and function of **CCK+/CB1R+ inhibitory basket synapses** onto hippocampal pyramidal neurons and reduces seizure threshold. (jahncke2024inhibitorycck+basket pages 1-2, jahncke2024inhibitorycck+basket pages 15-16)

Quantitatively, seizure susceptibility (flurothyl) tracks with glycosylation severity: generalized tonic-clonic seizure latency reductions were ~40.9% (Emx1Cre:Dag1 cKO), ~42.9% (Emx1Cre:Pomt2 cKO), and ~33.6% (Dag1cyto/-), while milder hypoglycosylation models showed smaller or no effects. (jahncke2024inhibitorycck+basket pages 13-15)

#### Retina and axon guidance
A 2024 Human Molecular Genetics zebrafish POMT1 loss model shows that loss of α-DG glycosylation causes **retinal synapse defects** (outer plexiform layer abnormalities, photoreceptor pedicle retraction) and **axon guidance defects**; importantly, these phenotypes depend on **maternal pomt1 mRNA contribution**, which can transiently sustain glycosylation early in development. (karas2024removalofpomt1 pages 6-7, karas2024removalofpomt1 pages 1-1)

## 3. Key molecular players (genes/proteins, chemicals, cells, anatomy)
### 3.1 Genes/proteins (causal/implicated)
| Module/Step | Gene (HGNC) | Protein/Function | Mechanistic Consequence | Key Citations |
| :--- | :--- | :--- | :--- | :--- |
| **Dystroglycan Core** | *DAG1* | Core glycoprotein substrate ($\alpha$/$\beta$ subunits) | Primary dystroglycanopathy; loss of ECM linkage scaffold | (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, cubilla2023dystroglycanopathiesgeneticbases pages 4-5, cubilla2023dystroglycanopathiesgeneticbases pages 23-24) |
| **Sugar Metabolism** | *GMPPB* | GDP-mannose pyrophosphorylase B; GDP-Man synthesis | Reduces GDP-mannose pool; limits substrate for O-mannosylation | (wang2024geneticallyengineeredmouse pages 37-41) |
| **ER O-Mannosylation** | *POMT1* / *POMT2* | Protein O-mannosyltransferases; initiate O-mannosylation | Abolishes initial O-mannose attachment; severe WWS/CMD phenotype | (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, koff2023proteinomannosylationone pages 2-4, karas2024removalofpomt1 pages 1-1, koff2023proteinomannosylationone pages 5-6) |
| **Core M3 Elaboration** | *POMGNT2* (GTDC2) | GlcNAc transferase; forms Core M3 (GlcNAc-$\beta$1,4-Man) | Prevents formation of Core M3; blocks functional glycosylation | (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, koff2023proteinomannosylationone pages 2-4, lu2024breakdownof pages 1-2) |
| **Core M3 Elaboration** | *B3GALNT2* | GalNAc transferase; extends Core M3 | Defective Core M3 structure; prevents phosphorylation | (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, koff2023proteinomannosylationone pages 2-4, ma2024deepmutationalscanning pages 30-32) |
| **Phosphorylation** | *POMK* (SGK196) | Kinase; phosphorylates Mannose-C6 on Core M3 | Lack of phospho-mannose "nucleus" for ribitol addition | (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, koff2023proteinomannosylationone pages 5-6, ma2024saturationmutagenesisreinforcedfunctional pages 26-27) |
| **CDP-Ribitol Synthesis** | *ISPD* (CRPPA) | CDP-L-ribitol pyrophosphorylase; synthesizes CDP-Rbo | Depletes sugar donor for FKTN/FKRP; severe hypoglycosylation | (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, lu2024breakdownof pages 1-2, cubilla2023dystroglycanopathiesgeneticbases pages 22-23) |
| **Ribitol Transfer** | *FKTN* | Fukutin; first Ribitol-5-phosphate transferase | Fails to add first ribitol-P; blocks matriglycan initiation | (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, lu2024breakdownof pages 1-2, ma2024saturationmutagenesisreinforcedfunctional pages 26-27, lu2024breakdownof pages 9-10) |
| **Ribitol Transfer** | *FKRP* | Fukutin-related protein; second Ribitol-5-P transferase | Fails to add second ribitol-P; LGMD2I to WWS spectrum | (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, lu2024breakdownof pages 1-2, lu2024breakdownof pages 9-10) |
| **Linker/Primer** | *RXYLT1* (TMEM5) | Ribitol-xylosyltransferase; adds Xylose to RboP | Disrupts glycan primer required for LARGE1 recognition | (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, lu2024breakdownof pages 1-2, ma2024saturationmutagenesisreinforcedfunctional pages 26-27) |
| **Linker/Primer** | *B4GAT1* | Glucuronyltransferase; adds GlcA to Xylose | Incomplete primer prevents LARGE1 binding/elongation | (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, koff2023proteinomannosylationone pages 5-6, ma2024saturationmutagenesisreinforcedfunctional pages 26-27) |
| **Matriglycan Polymerization** | *LARGE1* | Bifunctional glycosyltransferase (Xyl/GlcA) | Loss of laminin-binding matriglycan polymer; MDC1D | (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, ma2024deepmutationalscanning pages 30-32, ma2024saturationmutagenesisreinforcedfunctional pages 26-27) |
| **Adaptor Function** | *POMGNT1* | Glycosyltransferase (M1) & FKTN recruiter (M3) | M3 defect due to failure to recruit FKTN; MEB disease | (koff2023proteinomannosylationone pages 2-4, koff2023proteinomannosylationone pages 5-6) |


*Table: This table summarizes the core molecular machinery involved in the O-mannosylation pathway and matriglycan synthesis, mapping specific genes to their enzymatic functions and the mechanistic consequences of their disruption.*

### 3.2 Chemical entities (relevance)
- **Ribitol (BBP-418)**: substrate-supplementation strategy intended to boost ribitol-5P/CDP-ribitol availability and thereby improve α-DG functional glycosylation in FKRP-related disease. (NCT04800874 chunk 1, NCT05775848 chunk 1)
- **CHIR-99021 (GSK3 inhibitor; Wnt pathway agonist)**: in a 2024 GMPPB dystroglycanopathy mouse model preprint, Wnt activation is reported to alleviate impaired myogenic differentiation/regeneration in GMPPB-deficient systems. (wang2024geneticallyengineeredmouse pages 37-41)

### 3.3 Key cell types (examples)
- **Skeletal muscle satellite cells**: impaired differentiation/regeneration implicated in GMPPB-associated dystroglycanopathy models. (wang2024geneticallyengineeredmouse pages 37-41)
- **CCK+/CB1R+ inhibitory interneurons** and **hippocampal pyramidal neurons**: synapse targeting and inhibitory transmission are selectively disrupted in severe dystroglycanopathy models. (jahncke2024inhibitorycck+basket pages 15-16, jahncke2024inhibitorycck+basket pages 1-2)
- **Photoreceptors**: retinal synapse architecture is disrupted with POMT1 loss in zebrafish. (karas2024removalofpomt1 pages 6-7, karas2024removalofpomt1 pages 10-11)

### 3.4 Anatomical locations
- Skeletal muscle (sarcolemma/basal lamina interface). (lu2024breakdownof pages 1-2)
- Hippocampus CA1 (perisomatic inhibitory synapses; seizure susceptibility). (jahncke2024inhibitorycck+basket pages 13-15)
- Retina outer plexiform layer (photoreceptor synapses). (karas2024removalofpomt1 pages 6-7, karas2024removalofpomt1 pages 10-11)

## 4. Biological processes and cellular components (ontology-ready)
| Category | Term Label (ID) | Evidence/Justification | Key Citations |
| :--- | :--- | :--- | :--- |
| **GO: Bio Process** | protein O-linked mannosylation (GO:0035269) | Core defect; failure to add O-mannose or extend matriglycan on $\alpha$-DG. | (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, koff2023proteinomannosylationone pages 2-4) |
| **GO: Bio Process** | cell-matrix adhesion (GO:0007160) | Matriglycan mediates binding to laminin/agrin; loss disrupts ECM linkage. | (koff2023proteinomannosylationone pages 2-4, lu2024breakdownof pages 1-2) |
| **GO: Bio Process** | skeletal muscle regeneration (GO:0043403) | Impaired satellite cell differentiation (GMPPB model); revertant fibers. | (wang2024geneticallyengineeredmouse pages 37-41, lu2024breakdownof pages 4-6) |
| **GO: Bio Process** | axon guidance (GO:0007411) | Defective retinal/brain axon targeting in *pomt1* zebrafish and mouse models. | (karas2024removalofpomt1 pages 1-1, karas2024removalofpomt1 pages 6-7) |
| **GO: Bio Process** | chemical synaptic transmission (GO:0007268) | Functional defects in inhibitory CCK+ basket synapses; increased excitability. | (jahncke2024inhibitorycck+basket pages 15-16, jahncke2024inhibitorycck+basket pages 13-15) |
| **GO: Bio Process** | Wnt signaling pathway (GO:0016055) | Downregulated in GMPPB-deficient muscle; activation rescues myogenesis. | (wang2024geneticallyengineeredmouse pages 37-41) |
| **GO: Cell Comp** | dystrophin-associated glycoprotein complex (GO:0016010) | $\alpha$-DG is the central extracellular receptor of this complex. | (lu2024breakdownof pages 1-2, koff2023proteinomannosylationone pages 5-6) |
| **GO: Cell Comp** | sarcolemma (GO:0042383) | Primary site of pathology; loss of integrity leads to CK leak. | (unnikrishnan2023phenotypegenotypecharacterization pages 1-3, wang2024geneticallyengineeredmouse pages 37-41) |
| **GO: Cell Comp** | neuromuscular junction (GO:0031594) | Structural defects; reduced $\alpha$-bungarotoxin staining in *pomt1* mutants. | (wang2024geneticallyengineeredmouse pages 37-41, karas2024removalofpomt1 pages 10-11) |
| **GO: Cell Comp** | Golgi apparatus (GO:0005794) | Site of ribitol addition (FKRP) and matriglycan elongation (LARGE1). | (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, lu2024breakdownof pages 9-10) |
| **Cell Type (CL)** | skeletal muscle satellite cell (CL:0000594) | Defective differentiation and regeneration in GMPPB and FKRP models. | (wang2024geneticallyengineeredmouse pages 37-41, lu2024breakdownof pages 4-6) |
| **Cell Type (CL)** | GABAergic interneuron (CL:0000617) | Specifically CCK+/CB1R+ basket cells show axon targeting/synapse defects. | (jahncke2024inhibitorycck+basket pages 15-16, jahncke2024inhibitorycck+basket pages 1-2) |
| **Cell Type (CL)** | photoreceptor cell (CL:0000210) | Synapse loss and degeneration in *pomt1* zebrafish models. | (karas2024removalofpomt1 pages 3-4, karas2024removalofpomt1 pages 10-11) |
| **Anatomy (UBERON)** | hippocampus CA1 (UBERON:0003881) | Locus of inhibitory synapse defects and seizure genesis in models. | (jahncke2024inhibitorycck+basket pages 13-15, jahncke2024inhibitorycck+basket pages 10-11) |
| **Anatomy (UBERON)** | retina outer plexiform layer (UBERON:0005393) | Discontinuous synaptic staining and pedicle retraction in *pomt1* mutants. | (karas2024removalofpomt1 pages 6-7, karas2024removalofpomt1 pages 10-11) |
| **Phenotype (HP)** | Muscular dystrophy (HP:0003560) | Progressive weakness, histology of degeneration/regeneration. | (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, unnikrishnan2023phenotypegenotypecharacterization pages 1-3) |
| **Phenotype (HP)** | Seizures (HP:0001250) | Increased susceptibility/reduced latency in hypoglycosylated mice. | (jahncke2024inhibitorycck+basket pages 15-16, jahncke2024inhibitorycck+basket pages 13-15) |
| **Phenotype (HP)** | Global developmental delay (HP:0001263) | Common initial presentation in FKRP and severe CMD cohorts. | (unnikrishnan2023phenotypegenotypecharacterization pages 1-3) |
| **Phenotype (HP)** | Elevated serum creatine kinase (HP:0003236) | Marker of membrane leak; observed in GMPPB mice and human cohorts. | (wang2024geneticallyengineeredmouse pages 37-41, unnikrishnan2023phenotypegenotypecharacterization pages 1-3) |
| **Phenotype (HP)** | Cobblestone lissencephaly (HP:0007260) | Associated with migration defects and pial basement membrane rupture. | (koff2023proteinomannosylationone pages 5-6, NCT00313677 chunk 2) |


*Table: This table maps key pathophysiological mechanisms, cellular locations, and clinical features of dystroglycanopathy to standardized ontology terms (GO, CL, UBERON, HP), supported by recent evidence.*

## 5. Disease progression model (sequence of events)
### 5.1 Initiating event
Biallelic variants in DAG1 or α-DG glycosylation pathway genes reduce matriglycan synthesis, decreasing ECM ligand binding. (cubilla2023dystroglycanopathiesgeneticbases pages 4-5, cubilla2023dystroglycanopathiesgeneticbases pages 7-8)

### 5.2 Early molecular/cellular consequences
- Reduced α-DG ligand binding (laminin/agrin/perlecan/pikachurin/neurexin binding axis). (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, lu2024breakdownof pages 1-2)
- Failure of synaptic organizing functions in specific neural circuits when glycosylation loss is severe (CCK+/CB1R+ synapses). (jahncke2024inhibitorycck+basket pages 15-16, jahncke2024inhibitorycck+basket pages 13-15)

### 5.3 Tissue remodeling and clinical emergence
- In muscle, repeated contraction-induced injury triggers cycles of degeneration and regeneration; FKRP-related disease exhibits **mosaic/heterogeneous matriglycan** with **revertant/regenerating fibers**, complicating biopsy-based biomarker-to-phenotype correlation. (lu2024breakdownof pages 1-2, lu2024breakdownof pages 2-4)
- In zebrafish POMT1 loss, maternal transcript buffering delays onset; complete loss of α-DG glycosylation correlates with phenotype onset and reduced survival (e.g., KOHet begin dying by ~30 dpf with no survivors past ~70 days). (karas2024removalofpomt1 pages 7-8)

## 6. Phenotypic manifestations (mechanism-linked)
### 6.1 Musculoskeletal
FKRP cohort (India, 2023): among **9** unrelated patients with FKRP mutations, **CK ranged 2,793–32,396 U/L (mean 12,120 U/L)**; **3** had lost ambulation by last follow-up (median age ~7 years, range 6.5–9), and **3** never achieved independent ambulation, showing clinically meaningful variability even within one gene. (unnikrishnan2023phenotypegenotypecharacterization pages 1-3)

### 6.2 Neurologic
Seizure susceptibility in severe murine forebrain dystroglycanopathy models aligns with selective inhibitory synapse defects; seizure latency reductions of ~33–43% are reported depending on genotype (see Section 2.3). (jahncke2024inhibitorycck+basket pages 13-15, jahncke2024inhibitorycck+basket pages 15-16)

### 6.3 Ocular
Retinal synapse loss and photoreceptor structural defects are demonstrated after POMT1 loss in zebrafish, consistent with the role of matriglycan-dependent α-DG interactions in eye development and synapse maintenance. (karas2024removalofpomt1 pages 6-7, karas2024removalofpomt1 pages 10-11)

## 7. Recent developments (2023–2024) and latest research
| Year | Citation | Title (Short) | Type | Key Contribution | PMID | URL | Supporting Citations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2024 | Lam et al. | *Dual FKRP/FST gene therapy...* | Primary Study | Dual AAV-FKRP/Follistatin therapy restores $\alpha$-DG glycosylation and increases muscle mass in LGMDR9 mice. | - | [10.1016/j.ymthe.2024.06.028](https://doi.org/10.1016/j.ymthe.2024.06.028) | (lam2024dualfkrpfstgene pages 1-2, lam2024dualfkrpfstgene pages 7-8, lam2024dualfkrpfstgene media f92354a7) |
| 2024 | Karas et al. | *Removal of pomt1 in zebrafish...* | Primary Study | Validated *pomt1* null zebrafish; showed maternal mRNA delays brain/eye/muscle phenotypes until >5 dpf. | - | [10.1093/hmg/ddae006](https://doi.org/10.1093/hmg/ddae006) | (karas2024removalofpomt1 pages 1-1, karas2024removalofpomt1 pages 6-7, karas2024removalofpomt1 pages 1-2) |
| 2024 | Jahncke et al. | *Inhibitory CCK+ basket synapse...* | Primary Study | Glycosylation defects specifically disrupt CCK+/CB1R+ inhibitory synapses, increasing seizure susceptibility. | - | [10.7554/elife.87965](https://doi.org/10.7554/elife.87965) | (jahncke2024inhibitorycck+basket pages 15-16, jahncke2024inhibitorycck+basket pages 1-2, jahncke2024inhibitorycck+basket pages 10-11) |
| 2024 | Rajasingham et al. | *Validation of a novel western blot...* | Method Validation | Validated quantitative multiplex fluorescent Western blot for $\alpha$-DG glycosylation (IIH6/Core) in muscle biopsies. | - | [10.1007/s10974-024-09670-y](https://doi.org/10.1007/s10974-024-09670-y) | (rajasingham2024validationofa pages 2-4, rajasingham2024validationofa pages 1-2, rajasingham2024validationofa pages 8-10) |
| 2024 | Lu et al. | *Break Down of the Complexity...* | Review | Addresses FKRP genotype-phenotype disconnect; highlights regeneration-associated matriglycan variability in biopsies. | - | [10.3233/jnd-230205](https://doi.org/10.3233/jnd-230205) | (lu2024breakdownof pages 1-2, lu2024breakdownof pages 4-6) |
| 2024 | Wang et al. | *Genetically Engineered Mouse Models...* | Primary (Preprint) | GMPPB loss depletes GDP-mannose, impairs satellite cell differentiation via Wnt, rescued by AAV-GMPPB. | - | [10.21203/rs.3.rs-4502560/v1](https://doi.org/10.21203/rs.3.rs-4502560/v1) | (wang2024geneticallyengineeredmouse pages 37-41) |
| 2023 | Cubilla et al. | *Dystroglycanopathies: Genetic Bases...* | Review | Comprehensive classification of primary vs secondary dystroglycanopathies and O-mannosylation genes. | - | [10.1590/2326-4594-jiems-2022-0005](https://doi.org/10.1590/2326-4594-jiems-2022-0005) | (cubilla2023dystroglycanopathiesgeneticbases pages 7-8, cubilla2023dystroglycanopathiesgeneticbases pages 4-5, cubilla2023dystroglycanopathiesgeneticbases pages 3-4) |
| 2023 | ML Bio Solutions | *Study to Evaluate... BBP-418* | Clinical Trial (Ph3) | Phase 3 trial (NCT05775848) testing oral Ribitol (BBP-418) efficacy in LGMD2I/R9; primary endpoint NSAD. | - | [NCT05775848](https://clinicaltrials.gov/study/NCT05775848) | (NCT05775848 chunk 1) |


*Table: This table summarizes significant primary studies, reviews, and clinical trials from 2023 and 2024 that have advanced the understanding of dystroglycanopathy pathophysiology, diagnosis, and treatment.*

Key themes from 2023–2024 literature:
1) **Circuit-level neurobiology**: severe dystroglycan glycosylation loss causes selective inhibitory synapse defects (CCK+/CB1R+) and seizure vulnerability, separating synapse-organizing roles from gross migration defects in some contexts. (jahncke2024inhibitorycck+basket pages 15-16, jahncke2024inhibitorycck+basket pages 17-18)
2) **Developmental timing**: maternal mRNA/protein contribution can mask early phenotypes in zebrafish; true maternal-zygotic knockouts reveal early retinal/axon guidance and NMJ deficits. (karas2024removalofpomt1 pages 6-7, karas2024removalofpomt1 pages 1-1)
3) **Biomarker modernization**: validated quantitative multiplex fluorescence western blot provides a practical method to measure glycosylated vs core α-DG in small biopsies, supporting trials/longitudinal monitoring. (rajasingham2024validationofa pages 1-2, rajasingham2024validationofa pages 12-13)
4) **Mechanisms beyond ECM linkage**: GMPPB deficiency links glycosylation defects to altered intracellular programs (Ca2+ handling, Wnt/β-catenin signaling) and impaired myogenic differentiation, highlighting modifiers and downstream targets. (wang2024geneticallyengineeredmouse pages 37-41)

## 8. Current applications and real-world implementations
### 8.1 Diagnostics and biomarkers
A 2024 validated assay quantifies glycosylated and core α-DG from tibialis anterior biopsies using dual-channel fluorescence western blot with **IIH6C4** (functional matriglycan epitope) and a core α-DG antibody, with calibration curves and an estimated LLOQ of ~1 µg total protein (estimated detection ~13 pg α-DG). (rajasingham2024validationofa pages 2-4, rajasingham2024validationofa pages 12-13)

### 8.2 Therapeutic development (clinical trials)
**Ribitol (BBP-418)**
- Phase 3, randomized placebo-controlled trial in LGMD2I/R9: **NCT05775848** (start **2023-05-31**), **Phase 3**, **81** planned participants, primary endpoint: change from baseline in **North Star Assessment for Limb Girdle Muscular Dystrophy at 36 months**; key secondary outcomes include 10m walk velocity and FVC%. (NCT05775848 chunk 1)
- Phase 2 open-label trial: **NCT04800874** (start **2021-02-18**), **14** participants; includes PK/PD and biopsy-based assessments (including N-terminal α-DG measures and tibialis anterior biopsy). (NCT04800874 chunk 1)

**FKRP gene therapy (AAV9-based; examples)**
- **ATA-100 (GNT0006)**: **NCT05224505**, Phase 1, open dose-escalation, **6** participants, start **2022-09-01**, endpoints include safety plus functional tests, MRI, and biopsy glycosylation measures. (NCT05224505 chunk 1)
- **AB-1003 (LION-101)**: **NCT05230459**, recruiting; includes Phase 1 dose escalation and adaptive Phase 2, start **2023-05-15**, estimated **10** participants, primary endpoint safety over 52 weeks. (NCT05230459 chunk 1)

### 8.3 Therapeutic development (preclinical implementation)
A 2024 Molecular Therapy study demonstrates a dual-gene AAV approach (FKRP + follistatin) in FKRP P448L mice:
- Restores IIH6-detected α-DG glycosylation with band shift toward ~156 kDa and increased IIH6-positive fibers in diaphragm/heart with dual therapy versus FKRP alone (with reported significance for diaphragm). (lam2024dualfkrpfstgene pages 7-8, lam2024dualfkrpfstgene media f92354a7)
- Quantitatively, at 6 months the high-dose dual vector increased muscle FKRP protein from ~9.7±1.4-fold (FKRP alone) to **109±59-fold** (dual), and increased serum human follistatin to **39.7±8.0 ng/mL** (dual) versus ~6.4±2.2 ng/mL (FST alone). (lam2024dualfkrpfstgene pages 7-8)

## 9. Expert analysis and interpretation (mechanistic uncertainties and consensus)
### 9.1 Why matriglycan level is an imperfect severity biomarker (FKRP example)
A 2024 review argues that many FKRP missense variants retain partial function, and matriglycan expression may be preserved or re-expressed during later development and especially during regeneration, creating mosaic patterns and sampling bias in biopsies; this can produce weak or inconsistent correlations between matriglycan levels and clinical severity. (lu2024breakdownof pages 1-2, lu2024breakdownof pages 2-4)

The same review recommends fiber-level quantification (e.g., ImageJ Multi Point membrane intensity measures, exclusion/stratification of regenerating fibers, ≥100 fibers) alongside complementary bulk approaches (western blot) to improve interpretability for trials. (lu2024breakdownof pages 6-8, lu2024breakdownof pages 8-9)

### 9.2 Threshold model for neurologic phenotypes
The 2024 eLife study supports a “glycosylation threshold” concept where severe hypoglycosylation (forebrain Dag1 or Pomt2 loss) yields functional inhibitory synapse defects and seizure vulnerability, whereas partial hypoglycosylation can preserve synaptic function. (jahncke2024inhibitorycck+basket pages 15-16, jahncke2024inhibitorycck+basket pages 13-15)

## 10. Evidence items (PMIDs and direct quotes)
### 10.1 PMIDs
Most 2023–2024 sources retrieved here did not include PMIDs in the extracted text, and this RAG run did not retrieve PubMed metadata fields for them. One indirect PMID signal exists via Open Targets evidence (e.g., POMT1 association including PMID 38272461), but those outputs are not part of the citable paper text context for this report. Therefore, PMIDs should be added by external PubMed lookup using the DOIs/URLs provided in this report. (benarroch2024the2024version pages 8-9)

### 10.2 Direct quote (example)
A 2024 FKRP review emphasizes the interpretability issue of biopsy matriglycan: biopsies can show “fibers of very weak matriglycan and clusters of RFs with strong matriglycan expression,” highlighting mosaicism and the need for robust quantification. (lu2024breakdownof pages 8-9)

## Appendix A. Key figures (visual evidence)
- Western blot IIH6 restoration band shift and tissue quantification panels for dual FKRP/FST gene therapy are provided in the Lam et al. 2024 figures captured here. (lam2024dualfkrpfstgene media f92354a7, lam2024dualfkrpfstgene media 72380d56)



References

1. (cubilla2023dystroglycanopathiesgeneticbases pages 4-5): M.A. Cubilla, G.M. Papazoglu, and C.G. Asteggiano. Dystroglycanopathies: genetic bases of muscular dystrophies due to alteration in the o-glycosylation of α-dystroglycan. Journal of Inborn Errors of Metabolism and Screening, Apr 2023. URL: https://doi.org/10.1590/2326-4594-jiems-2022-0005, doi:10.1590/2326-4594-jiems-2022-0005. This article has 3 citations.

2. (cubilla2023dystroglycanopathiesgeneticbases pages 3-4): M.A. Cubilla, G.M. Papazoglu, and C.G. Asteggiano. Dystroglycanopathies: genetic bases of muscular dystrophies due to alteration in the o-glycosylation of α-dystroglycan. Journal of Inborn Errors of Metabolism and Screening, Apr 2023. URL: https://doi.org/10.1590/2326-4594-jiems-2022-0005, doi:10.1590/2326-4594-jiems-2022-0005. This article has 3 citations.

3. (benarroch2024the2024version pages 8-9): Louise Benarroch, Gisèle Bonne, François Rivier, and Dalil Hamroun. The 2024 version of the gene table of neuromuscular disorders (nuclear genome). Neuromuscular Disorders, 34:126-170, Jan 2024. URL: https://doi.org/10.1016/j.nmd.2023.12.007, doi:10.1016/j.nmd.2023.12.007. This article has 32 citations and is from a peer-reviewed journal.

4. (cubilla2023dystroglycanopathiesgeneticbases pages 8-9): M.A. Cubilla, G.M. Papazoglu, and C.G. Asteggiano. Dystroglycanopathies: genetic bases of muscular dystrophies due to alteration in the o-glycosylation of α-dystroglycan. Journal of Inborn Errors of Metabolism and Screening, Apr 2023. URL: https://doi.org/10.1590/2326-4594-jiems-2022-0005, doi:10.1590/2326-4594-jiems-2022-0005. This article has 3 citations.

5. (cubilla2023dystroglycanopathiesgeneticbases pages 7-8): M.A. Cubilla, G.M. Papazoglu, and C.G. Asteggiano. Dystroglycanopathies: genetic bases of muscular dystrophies due to alteration in the o-glycosylation of α-dystroglycan. Journal of Inborn Errors of Metabolism and Screening, Apr 2023. URL: https://doi.org/10.1590/2326-4594-jiems-2022-0005, doi:10.1590/2326-4594-jiems-2022-0005. This article has 3 citations.

6. (unnikrishnan2023phenotypegenotypecharacterization pages 1-3): Gopikrishnan Unnikrishnan, Kiran Polavarapu, Mainak Bardhan, Saraswati Nashi, Seena Vengalil, Veeramani Preethish-Kumar, Ravi Kiran Valasani, Akshata Huddar, Vikas Nishadham, Bevinahalli Nanjegowda Nandeesh, and Atchayaram Nalini. Phenotype genotype characterization of fkrp-related muscular dystrophy among indian patients. Journal of Neuromuscular Diseases, 10:615-626, May 2023. URL: https://doi.org/10.3233/jnd-221618, doi:10.3233/jnd-221618. This article has 7 citations and is from a peer-reviewed journal.

7. (koff2023proteinomannosylationone pages 2-4): Melissa Koff, Pedro Monagas-Valentin, Boris Novikov, Ishita Chandel, and Vladislav Panin. Protein o-mannosylation: one sugar, several pathways, many functions. Glycobiology, 33:911-926, Aug 2023. URL: https://doi.org/10.1093/glycob/cwad067, doi:10.1093/glycob/cwad067. This article has 17 citations and is from a peer-reviewed journal.

8. (lu2024breakdownof pages 1-2): Qi L. Lu, Molly C. Holbrook, Marcela P. Cataldi, and Anthony Blaeser. Break down of the complexity and inconsistency between levels of matriglycan and disease phenotype in fkrp-related dystroglycanopathies: a review and model of interpretation. Journal of Neuromuscular Diseases, 11:275-284, Jan 2024. URL: https://doi.org/10.3233/jnd-230205, doi:10.3233/jnd-230205. This article has 2 citations and is from a peer-reviewed journal.

9. (koff2023proteinomannosylationone pages 5-6): Melissa Koff, Pedro Monagas-Valentin, Boris Novikov, Ishita Chandel, and Vladislav Panin. Protein o-mannosylation: one sugar, several pathways, many functions. Glycobiology, 33:911-926, Aug 2023. URL: https://doi.org/10.1093/glycob/cwad067, doi:10.1093/glycob/cwad067. This article has 17 citations and is from a peer-reviewed journal.

10. (lu2024breakdownof pages 9-10): Qi L. Lu, Molly C. Holbrook, Marcela P. Cataldi, and Anthony Blaeser. Break down of the complexity and inconsistency between levels of matriglycan and disease phenotype in fkrp-related dystroglycanopathies: a review and model of interpretation. Journal of Neuromuscular Diseases, 11:275-284, Jan 2024. URL: https://doi.org/10.3233/jnd-230205, doi:10.3233/jnd-230205. This article has 2 citations and is from a peer-reviewed journal.

11. (NCT00313677 chunk 2): Katherine Mathews. Clinical Trial Readiness for the Dystroglycanopathies. Katherine Mathews. 2006. ClinicalTrials.gov Identifier: NCT00313677

12. (jahncke2024inhibitorycck+basket pages 1-2): Jennifer N Jahncke, Daniel S Miller, Milana Krush, Eric Schnell, and Kevin M Wright. Inhibitory cck+ basket synapse defects in mouse models of dystroglycanopathy. eLife, Jan 2024. URL: https://doi.org/10.7554/elife.87965, doi:10.7554/elife.87965. This article has 8 citations and is from a domain leading peer-reviewed journal.

13. (jahncke2024inhibitorycck+basket pages 15-16): Jennifer N Jahncke, Daniel S Miller, Milana Krush, Eric Schnell, and Kevin M Wright. Inhibitory cck+ basket synapse defects in mouse models of dystroglycanopathy. eLife, Jan 2024. URL: https://doi.org/10.7554/elife.87965, doi:10.7554/elife.87965. This article has 8 citations and is from a domain leading peer-reviewed journal.

14. (jahncke2024inhibitorycck+basket pages 13-15): Jennifer N Jahncke, Daniel S Miller, Milana Krush, Eric Schnell, and Kevin M Wright. Inhibitory cck+ basket synapse defects in mouse models of dystroglycanopathy. eLife, Jan 2024. URL: https://doi.org/10.7554/elife.87965, doi:10.7554/elife.87965. This article has 8 citations and is from a domain leading peer-reviewed journal.

15. (karas2024removalofpomt1 pages 6-7): Brittany F Karas, Kristin R Terez, Shorbon Mowla, Namarata Battula, Kyle P Flannery, Brian M Gural, Grace Aboussleman, Numa Mubin, and M Chiara Manzini. Removal of <i>pomt1</i> in zebrafish leads to loss of α-dystroglycan glycosylation and dystroglycanopathy phenotypes. Human Molecular Genetics, 33:709-723, Jan 2024. URL: https://doi.org/10.1093/hmg/ddae006, doi:10.1093/hmg/ddae006. This article has 8 citations and is from a domain leading peer-reviewed journal.

16. (karas2024removalofpomt1 pages 1-1): Brittany F Karas, Kristin R Terez, Shorbon Mowla, Namarata Battula, Kyle P Flannery, Brian M Gural, Grace Aboussleman, Numa Mubin, and M Chiara Manzini. Removal of <i>pomt1</i> in zebrafish leads to loss of α-dystroglycan glycosylation and dystroglycanopathy phenotypes. Human Molecular Genetics, 33:709-723, Jan 2024. URL: https://doi.org/10.1093/hmg/ddae006, doi:10.1093/hmg/ddae006. This article has 8 citations and is from a domain leading peer-reviewed journal.

17. (cubilla2023dystroglycanopathiesgeneticbases pages 23-24): M.A. Cubilla, G.M. Papazoglu, and C.G. Asteggiano. Dystroglycanopathies: genetic bases of muscular dystrophies due to alteration in the o-glycosylation of α-dystroglycan. Journal of Inborn Errors of Metabolism and Screening, Apr 2023. URL: https://doi.org/10.1590/2326-4594-jiems-2022-0005, doi:10.1590/2326-4594-jiems-2022-0005. This article has 3 citations.

18. (wang2024geneticallyengineeredmouse pages 37-41): Yuxiang Wang, Ziwei fu, Wangtong Wang, Yanyan Chen, Chenyang Zhang, Ju Yang, Hua Yang, Bing Yan, Baoming Gong, Weiqiao Lu, Ying Liu, Lei Sun, Hao Jiang, Zhao Zhang, Bo Chen, and Xiuping Liu. Genetically engineered mouse models unveil mechanisms and therapeutic strategies for gmppb-associated dystroglycanopathy. Aug 2024. URL: https://doi.org/10.21203/rs.3.rs-4502560/v1, doi:10.21203/rs.3.rs-4502560/v1.

19. (ma2024deepmutationalscanning pages 30-32): Kaiyue Ma, Shushu Huang, Kenneth K. Ng, N. Lake, Soumya Joseph, Jenny Xu, A. Lek, Lin Ge, KG Woodman, K. Koczwara, Justin Cohen, Vincent Ho, Christine L. O’Connor, M. Brindley, Kevin P. Campbell, and M. Lek. Deep mutational scanning in disease-related genes with saturation mutagenesis-reinforced functional assays (smurf). Dataset, Aug 2024. URL: https://doi.org/10.17632/fgn9myv746.1, doi:10.17632/fgn9myv746.1. This article has 3 citations.

20. (ma2024saturationmutagenesisreinforcedfunctional pages 26-27): Kaiyue Ma, Shushu Huang, Kenneth K. Ng, Nicole J. Lake, Soumya Joseph, Jenny Xu, Angela Lek, Lin Ge, Keryn G. Woodman, Katherine E. Koczwara, Justin Cohen, Vincent Ho, Christine L. O’Connor, Melinda A. Brindley, Kevin P. Campbell, and Monkol Lek. Saturation mutagenesis-reinforced functional assays for disease-related genes. Cell, 187:6707-6724.e22, Nov 2024. URL: https://doi.org/10.1016/j.cell.2024.08.047, doi:10.1016/j.cell.2024.08.047. This article has 17 citations and is from a highest quality peer-reviewed journal.

21. (cubilla2023dystroglycanopathiesgeneticbases pages 22-23): M.A. Cubilla, G.M. Papazoglu, and C.G. Asteggiano. Dystroglycanopathies: genetic bases of muscular dystrophies due to alteration in the o-glycosylation of α-dystroglycan. Journal of Inborn Errors of Metabolism and Screening, Apr 2023. URL: https://doi.org/10.1590/2326-4594-jiems-2022-0005, doi:10.1590/2326-4594-jiems-2022-0005. This article has 3 citations.

22. (NCT04800874 chunk 1):  Study of BBP-418 in Patients With LGMD2I. ML Bio Solutions, Inc.. 2021. ClinicalTrials.gov Identifier: NCT04800874

23. (NCT05775848 chunk 1):  Study to Evaluate the Efficacy and Safety of BBP-418 (Ribitol) in Patients With Limb Girdle Muscular Dystrophy 2I (LGMD2I). ML Bio Solutions, Inc.. 2023. ClinicalTrials.gov Identifier: NCT05775848

24. (karas2024removalofpomt1 pages 10-11): Brittany F Karas, Kristin R Terez, Shorbon Mowla, Namarata Battula, Kyle P Flannery, Brian M Gural, Grace Aboussleman, Numa Mubin, and M Chiara Manzini. Removal of <i>pomt1</i> in zebrafish leads to loss of α-dystroglycan glycosylation and dystroglycanopathy phenotypes. Human Molecular Genetics, 33:709-723, Jan 2024. URL: https://doi.org/10.1093/hmg/ddae006, doi:10.1093/hmg/ddae006. This article has 8 citations and is from a domain leading peer-reviewed journal.

25. (lu2024breakdownof pages 4-6): Qi L. Lu, Molly C. Holbrook, Marcela P. Cataldi, and Anthony Blaeser. Break down of the complexity and inconsistency between levels of matriglycan and disease phenotype in fkrp-related dystroglycanopathies: a review and model of interpretation. Journal of Neuromuscular Diseases, 11:275-284, Jan 2024. URL: https://doi.org/10.3233/jnd-230205, doi:10.3233/jnd-230205. This article has 2 citations and is from a peer-reviewed journal.

26. (karas2024removalofpomt1 pages 3-4): Brittany F Karas, Kristin R Terez, Shorbon Mowla, Namarata Battula, Kyle P Flannery, Brian M Gural, Grace Aboussleman, Numa Mubin, and M Chiara Manzini. Removal of <i>pomt1</i> in zebrafish leads to loss of α-dystroglycan glycosylation and dystroglycanopathy phenotypes. Human Molecular Genetics, 33:709-723, Jan 2024. URL: https://doi.org/10.1093/hmg/ddae006, doi:10.1093/hmg/ddae006. This article has 8 citations and is from a domain leading peer-reviewed journal.

27. (jahncke2024inhibitorycck+basket pages 10-11): Jennifer N Jahncke, Daniel S Miller, Milana Krush, Eric Schnell, and Kevin M Wright. Inhibitory cck+ basket synapse defects in mouse models of dystroglycanopathy. eLife, Jan 2024. URL: https://doi.org/10.7554/elife.87965, doi:10.7554/elife.87965. This article has 8 citations and is from a domain leading peer-reviewed journal.

28. (lu2024breakdownof pages 2-4): Qi L. Lu, Molly C. Holbrook, Marcela P. Cataldi, and Anthony Blaeser. Break down of the complexity and inconsistency between levels of matriglycan and disease phenotype in fkrp-related dystroglycanopathies: a review and model of interpretation. Journal of Neuromuscular Diseases, 11:275-284, Jan 2024. URL: https://doi.org/10.3233/jnd-230205, doi:10.3233/jnd-230205. This article has 2 citations and is from a peer-reviewed journal.

29. (karas2024removalofpomt1 pages 7-8): Brittany F Karas, Kristin R Terez, Shorbon Mowla, Namarata Battula, Kyle P Flannery, Brian M Gural, Grace Aboussleman, Numa Mubin, and M Chiara Manzini. Removal of <i>pomt1</i> in zebrafish leads to loss of α-dystroglycan glycosylation and dystroglycanopathy phenotypes. Human Molecular Genetics, 33:709-723, Jan 2024. URL: https://doi.org/10.1093/hmg/ddae006, doi:10.1093/hmg/ddae006. This article has 8 citations and is from a domain leading peer-reviewed journal.

30. (lam2024dualfkrpfstgene pages 1-2): Patricia Lam, Deborah A. Zygmunt, Anna Ashbrook, Macey Bennett, Tatyana A. Vetter, and Paul T. Martin. Dual fkrp/fst gene therapy normalizes ambulation, increases strength, decreases pathology, and amplifies gene expression in lgmdr9 mice. Molecular Therapy, 32:2604-2623, Aug 2024. URL: https://doi.org/10.1016/j.ymthe.2024.06.028, doi:10.1016/j.ymthe.2024.06.028. This article has 3 citations and is from a highest quality peer-reviewed journal.

31. (lam2024dualfkrpfstgene pages 7-8): Patricia Lam, Deborah A. Zygmunt, Anna Ashbrook, Macey Bennett, Tatyana A. Vetter, and Paul T. Martin. Dual fkrp/fst gene therapy normalizes ambulation, increases strength, decreases pathology, and amplifies gene expression in lgmdr9 mice. Molecular Therapy, 32:2604-2623, Aug 2024. URL: https://doi.org/10.1016/j.ymthe.2024.06.028, doi:10.1016/j.ymthe.2024.06.028. This article has 3 citations and is from a highest quality peer-reviewed journal.

32. (lam2024dualfkrpfstgene media f92354a7): Patricia Lam, Deborah A. Zygmunt, Anna Ashbrook, Macey Bennett, Tatyana A. Vetter, and Paul T. Martin. Dual fkrp/fst gene therapy normalizes ambulation, increases strength, decreases pathology, and amplifies gene expression in lgmdr9 mice. Molecular Therapy, 32:2604-2623, Aug 2024. URL: https://doi.org/10.1016/j.ymthe.2024.06.028, doi:10.1016/j.ymthe.2024.06.028. This article has 3 citations and is from a highest quality peer-reviewed journal.

33. (karas2024removalofpomt1 pages 1-2): Brittany F Karas, Kristin R Terez, Shorbon Mowla, Namarata Battula, Kyle P Flannery, Brian M Gural, Grace Aboussleman, Numa Mubin, and M Chiara Manzini. Removal of <i>pomt1</i> in zebrafish leads to loss of α-dystroglycan glycosylation and dystroglycanopathy phenotypes. Human Molecular Genetics, 33:709-723, Jan 2024. URL: https://doi.org/10.1093/hmg/ddae006, doi:10.1093/hmg/ddae006. This article has 8 citations and is from a domain leading peer-reviewed journal.

34. (rajasingham2024validationofa pages 2-4): Thulashitha Rajasingham, Hector M. Rodriguez, Andreas Betz, Douglas M. Sproule, and Uma Sinha. Validation of a novel western blot assay to monitor patterns and levels of alpha dystroglycan in skeletal muscle of patients with limb girdle muscular dystrophies. Journal of Muscle Research and Cell Motility, 45:123-138, Apr 2024. URL: https://doi.org/10.1007/s10974-024-09670-y, doi:10.1007/s10974-024-09670-y. This article has 3 citations and is from a peer-reviewed journal.

35. (rajasingham2024validationofa pages 1-2): Thulashitha Rajasingham, Hector M. Rodriguez, Andreas Betz, Douglas M. Sproule, and Uma Sinha. Validation of a novel western blot assay to monitor patterns and levels of alpha dystroglycan in skeletal muscle of patients with limb girdle muscular dystrophies. Journal of Muscle Research and Cell Motility, 45:123-138, Apr 2024. URL: https://doi.org/10.1007/s10974-024-09670-y, doi:10.1007/s10974-024-09670-y. This article has 3 citations and is from a peer-reviewed journal.

36. (rajasingham2024validationofa pages 8-10): Thulashitha Rajasingham, Hector M. Rodriguez, Andreas Betz, Douglas M. Sproule, and Uma Sinha. Validation of a novel western blot assay to monitor patterns and levels of alpha dystroglycan in skeletal muscle of patients with limb girdle muscular dystrophies. Journal of Muscle Research and Cell Motility, 45:123-138, Apr 2024. URL: https://doi.org/10.1007/s10974-024-09670-y, doi:10.1007/s10974-024-09670-y. This article has 3 citations and is from a peer-reviewed journal.

37. (jahncke2024inhibitorycck+basket pages 17-18): Jennifer N Jahncke, Daniel S Miller, Milana Krush, Eric Schnell, and Kevin M Wright. Inhibitory cck+ basket synapse defects in mouse models of dystroglycanopathy. eLife, Jan 2024. URL: https://doi.org/10.7554/elife.87965, doi:10.7554/elife.87965. This article has 8 citations and is from a domain leading peer-reviewed journal.

38. (rajasingham2024validationofa pages 12-13): Thulashitha Rajasingham, Hector M. Rodriguez, Andreas Betz, Douglas M. Sproule, and Uma Sinha. Validation of a novel western blot assay to monitor patterns and levels of alpha dystroglycan in skeletal muscle of patients with limb girdle muscular dystrophies. Journal of Muscle Research and Cell Motility, 45:123-138, Apr 2024. URL: https://doi.org/10.1007/s10974-024-09670-y, doi:10.1007/s10974-024-09670-y. This article has 3 citations and is from a peer-reviewed journal.

39. (NCT05224505 chunk 1):  ATA-100 (Formerly GNT0006) Gene Therapy Trial in Patients With LGMDR9. Atamyo Therapeutics. 2022. ClinicalTrials.gov Identifier: NCT05224505

40. (NCT05230459 chunk 1):  A Study to Evaluate the Safety of AB-1003 (Previously LION-101) in Subjects With Genetic Confirmation of LGMD2I/R9 (Part1). AskBio Inc. 2023. ClinicalTrials.gov Identifier: NCT05230459

41. (lu2024breakdownof pages 6-8): Qi L. Lu, Molly C. Holbrook, Marcela P. Cataldi, and Anthony Blaeser. Break down of the complexity and inconsistency between levels of matriglycan and disease phenotype in fkrp-related dystroglycanopathies: a review and model of interpretation. Journal of Neuromuscular Diseases, 11:275-284, Jan 2024. URL: https://doi.org/10.3233/jnd-230205, doi:10.3233/jnd-230205. This article has 2 citations and is from a peer-reviewed journal.

42. (lu2024breakdownof pages 8-9): Qi L. Lu, Molly C. Holbrook, Marcela P. Cataldi, and Anthony Blaeser. Break down of the complexity and inconsistency between levels of matriglycan and disease phenotype in fkrp-related dystroglycanopathies: a review and model of interpretation. Journal of Neuromuscular Diseases, 11:275-284, Jan 2024. URL: https://doi.org/10.3233/jnd-230205, doi:10.3233/jnd-230205. This article has 2 citations and is from a peer-reviewed journal.

43. (lam2024dualfkrpfstgene media 72380d56): Patricia Lam, Deborah A. Zygmunt, Anna Ashbrook, Macey Bennett, Tatyana A. Vetter, and Paul T. Martin. Dual fkrp/fst gene therapy normalizes ambulation, increases strength, decreases pathology, and amplifies gene expression in lgmdr9 mice. Molecular Therapy, 32:2604-2623, Aug 2024. URL: https://doi.org/10.1016/j.ymthe.2024.06.028, doi:10.1016/j.ymthe.2024.06.028. This article has 3 citations and is from a highest quality peer-reviewed journal.