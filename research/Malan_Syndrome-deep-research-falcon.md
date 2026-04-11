---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-28T00:41:22.029940'
end_time: '2026-03-28T00:51:59.375753'
duration_seconds: 637.35
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Malan Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 50
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Malan Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Malan Syndrome**.
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
- **Disease Name:** Malan Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Malan Syndrome**.
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


## Comprehensive Research Report: Malan Syndrome (Malan overgrowth syndrome)

### Disease identifiers and definition
Malan syndrome (also referred to historically as “Sotos syndrome 2”) is an ultra-rare, autosomal dominant overgrowth–neurodevelopmental disorder caused by heterozygous loss of function of **NFIX** (HGNC:7892; “nuclear factor I X”). (priolo2024nfixrelatedmalansyndrome pages 19-21, priolo2024nfixrelatedmalansyndromeb pages 19-21, priolo2024nfixrelatedmalansyndromea pages 19-21)

- **MONDO ID:** **MONDO:0013885** (“Malan overgrowth syndrome”; OpenTargets association evidence). (makker2024apatientcase pages 12-13)
- **OMIM/MIM:** **614753** (Malan syndrome), as cited in the 2024 AJMG paper describing Malan syndrome mechanisms and variant classes. (zhao2024novelmolecularmechanism pages 3-5)

### Executive pathophysiology summary (current understanding)
The core disease mechanism is **NFIX haploinsufficiency**, typically resulting from nonsense/frameshift/splice variants that introduce premature termination codons and are predicted to undergo **nonsense-mediated decay (NMD)**, or from 19p13.2 microdeletions that remove NFIX; pathogenic missense variants cluster in NFIX’s **DNA-binding/dimerization domain** and are predicted to impair DNA binding and transcriptional regulation. (priolo2024nfixrelatedmalansyndromeb pages 19-21, priolo2024nfixrelatedmalansyndrome pages 21-23, priolo2024nfixrelatedmalansyndrome pages 7-9)

At the molecular/cellular level, reduced functional NFIX disrupts transcriptional programs controlling (i) **neural stem/progenitor proliferation vs differentiation timing**, (ii) **intermediate progenitor production**, and (iii) **glial lineage specification/maturation (astrocyte maturation vs oligodendrogenesis)**—providing a mechanistic route from altered neurodevelopment to **megalencephaly/macrocephaly**, **abnormal brain connectivity**, and **intellectual disability/behavioral phenotypes**. (piper2019nuclearfactorone pages 3-5, piper2019nuclearfactorone pages 5-7, piper2019nuclearfactorone pages 1-2, oishi2019heterozygosityfornuclear pages 1-2)

### 1) Core pathophysiology
#### Primary pathophysiological mechanisms
**A. NFIX loss-of-function via NMD and/or impaired DNA binding**
NFIX encodes an NFI-family transcription factor that binds a palindromic DNA motif as homo-/heterodimers and has an N-terminal DNA-binding/dimerization domain and a C-terminal transactivation/repression domain. Malan syndrome-associated variants largely map to the DNA-binding/dimerization domain, with many truncating variants predicted to trigger NMD (haploinsufficiency) and missense variants predicted to impair DNA binding. (priolo2024nfixrelatedmalansyndrome pages 19-21, priolo2024nfixrelatedmalansyndromea pages 19-21, priolo2024nfixrelatedmalansyndrome pages 21-23)

**B. Neurodevelopmental dysregulation of progenitor dynamics and lineage choice**
In brain development, NFIX promotes differentiation of neural stem/progenitor cells and influences lineage outputs; NFIX loss delays differentiation of radial glia/neural stem cells and is associated with brain overgrowth (megalencephaly). (piper2019nuclearfactorone pages 3-5, piper2019nuclearfactorone pages 5-7)

Mechanistically, NFIX supports intermediate progenitor generation by transcriptionally activating **inscuteable (Insc/INSC)**, which affects apical–basal spindle orientation and intermediate progenitor formation. (piper2019nuclearfactorone pages 3-5)

**C. Glial maturation defects and altered gliogenesis**
NFIX regulates astrocyte gene-expression programs (e.g., astrocyte marker **GFAP**) and restrains oligodendrogenic programs; NFIX loss is associated with a shift toward oligodendrogenesis in neural stem/progenitor contexts. (piper2019nuclearfactorone pages 5-7, kooblall2024identificationofcellular pages 2-3, piper2019nuclearfactorone pages 1-2)

#### Dysregulated molecular pathways (evidence-grounded)
The evidence base supports transcriptional dysregulation affecting:
- **Neurogenesis / intermediate progenitor generation** (INSC target). (piper2019nuclearfactorone pages 3-5)
- **Cell-cycle progression control in neural progenitors** (NFIX repression of **BBX**; BBX promotes G1→S progression). (kooblall2024identificationofcellular pages 2-3)
- **Astrocyte differentiation and intermediate filament biology** (NFIX activation of **GFAP**). (piper2019nuclearfactorone pages 5-7, kooblall2024identificationofcellular pages 2-3)
- **Retinoic-acid handling / retinoid-binding biology** via **CRABP2**, identified as a direct NFIX-regulated gene (promoter regulation confirmed by luciferase assay in a mouse/MEF-based systems study). (kooblall2024identificationofcellular pages 2-3)

### 2) Key molecular players
#### Genes / proteins
- **NFIX (HGNC:7892)**: causal gene; transcription factor; dosage-sensitive. (priolo2024nfixrelatedmalansyndromeb pages 19-21, makker2024apatientcase pages 12-13)
- **INSC**: NFIX activates Insc to promote intermediate progenitor generation. (piper2019nuclearfactorone pages 3-5)
- **GFAP**: NFIX binds/activates GFAP promoter in astrocytes; links NFIX to astrocyte maturation. (piper2019nuclearfactorone pages 5-7, kooblall2024identificationofcellular pages 2-3)
- **BBX (Bobby Sox)**: NFIX binds a BBX enhancer to suppress BBX transcription in neural progenitors (cell-cycle implications). (kooblall2024identificationofcellular pages 2-3)
- **CRABP2** and **VCAM1**: identified as misregulated downstream genes in NFIX-related skeletal dysplasia models; NFIX directly regulates CRABP2 promoter activity. (kooblall2024identificationofcellular pages 2-3)

Variant mechanism nuance (allelic series context): Malan syndrome is typically haploinsufficiency, while Marshall–Smith syndrome involves truncating variants that may escape NMD and act via a distinct mechanism; recent Malan syndrome molecular work explicitly frames this distinction. (zhao2024novelmolecularmechanism pages 3-5, priolo2024nfixrelatedmalansyndrome pages 7-9)

#### Chemical entities (metabolites/drugs/small molecules)
- **Retinoic acid (CHEBI:15367)** is mechanistically implicated through NFIX regulation of **CRABP2** (cellular retinoic acid binding protein 2), which modulates retinoid biology; this identifies retinoid-handling pathways as a potential mechanistic node for skeletal phenotypes and suggests potential druggability concepts (exploratory). (kooblall2024identificationofcellular pages 2-3)

No established disease-specific pharmacotherapy for Malan syndrome was identified in the retrieved 2023–2024 clinical literature; discussions of future therapeutics remain exploratory. (makker2024apatientcase pages 12-13)

#### Cell types primarily affected (CL terms; evidence-driven)
Key cell types implicated by expression/function evidence include:
- **Neural stem cells / neural progenitor cells (CL:0000047 / CL:0011020)**, including **radial glia**. (piper2019nuclearfactorone pages 3-5, piper2019nuclearfactorone pages 1-2)
- **Intermediate neural progenitors (intermediate progenitor cells; CL term varies by ontology release)** via INSC regulation. (piper2019nuclearfactorone pages 3-5)
- **Astrocyte lineage cells (CL:0000127)** and astrocyte maturation programs (GFAP regulation). (piper2019nuclearfactorone pages 5-7, kooblall2024identificationofcellular pages 2-3)
- **Oligodendrocyte lineage cells (CL:0000128)** (NFIX restrains oligodendrogenic bias). (piper2019nuclearfactorone pages 5-7, piper2019nuclearfactorone pages 1-2)
- **Ependymal cells (CL:0000065)** (ependymal structure defects described in NFIX loss). (piper2019nuclearfactorone pages 1-2)

#### Anatomical locations / tissues (UBERON terms; evidence-driven)
- **Brain (UBERON:0000955)** with prominent involvement of **neocortex**, **hippocampus**, ventricular/SVZ regions, and commissural tracts. (piper2019nuclearfactorone pages 1-2, oishi2019heterozygosityfornuclear pages 3-4)
- **Corpus callosum (UBERON:0001876)** and other commissures (microstructure/tract density abnormalities in Nfix+/−). (oishi2019heterozygosityfornuclear pages 1-2, oishi2019heterozygosityfornuclear pages 7-9, oishi2019heterozygosityfornuclear pages 3-4)
- **Eye / optic nerve (UBERON:0000970 / UBERON:0000987)** (optic nerve hypoplasia/atrophy and other ophthalmologic complications are common). (priolo2024nfixrelatedmalansyndromeb pages 5-7, makker2024apatientcase pages 11-12)
- **Skeletal system and growth plate cartilage (e.g., UBERON:0000982; UBERON:0001972)**: NFIX expression in skeletal primordia and growth plate chondrocytes in mouse; clinical skeletal dysplasia features. (malan2010distincteffectsof pages 4-5, priolo2024nfixrelatedmalansyndromeb pages 5-7)

### 3) Biological processes disrupted (GO-style annotations)
Evidence-supported disrupted processes suitable for GO mapping include:
- **Regulation of transcription by RNA polymerase II** / sequence-specific DNA binding transcription factor activity (NFIX core function). (priolo2024nfixrelatedmalansyndrome pages 19-21, priolo2024nfixrelatedmalansyndromeb pages 19-21)
- **Neurogenesis and neural stem cell differentiation** (delayed differentiation; intermediate progenitor generation; hippocampal neurogenesis effects). (piper2019nuclearfactorone pages 3-5, piper2019nuclearfactorone pages 5-7)
- **Gliogenesis / astrocyte differentiation** (GFAP regulation; later-stage astrocyte maturation). (piper2019nuclearfactorone pages 5-7, kooblall2024identificationofcellular pages 2-3)
- **Oligodendrocyte differentiation / fate specification** (bias toward oligodendrogenesis with NFIX loss). (piper2019nuclearfactorone pages 5-7, piper2019nuclearfactorone pages 1-2)
- **Cell cycle regulation in progenitors** (BBX repression; BBX promotes G1→S). (kooblall2024identificationofcellular pages 2-3)
- **Retinoid metabolic/transport processes** (CRABP2 regulation; retinoic-acid binding pathway connection). (kooblall2024identificationofcellular pages 2-3)

### 4) Cellular components (where key processes occur)
Key cellular locations/components implied by mechanism:
- **Nucleus (GO:0005634)**: NFIX DNA-binding transcriptional regulation. (priolo2024nfixrelatedmalansyndrome pages 19-21, priolo2024nfixrelatedmalansyndromeb pages 19-21)
- **Chromatin / enhancers**: NFI factors preferentially bind highly expressed genes and associate with active chromatin marks including distal binding sites (enhancer-like regulation). (piper2019nuclearfactorone pages 9-10)

### 5) Disease progression (sequence of events)
1. **Germline heterozygous NFIX loss-of-function** (de novo in most cases) → reduced NFIX dosage and impaired transcriptional regulation; truncating variants commonly act via NMD. (priolo2024nfixrelatedmalansyndromeb pages 19-21, priolo2024nfixrelatedmalansyndrome pages 21-23)
2. **Developmental dysregulation of neural progenitor programs** → prolonged progenitor self-renewal and delayed differentiation, altered intermediate progenitor generation (INSC), and altered gliogenesis (astrocyte maturation programs such as GFAP; oligodendrogenesis bias). (piper2019nuclearfactorone pages 3-5, piper2019nuclearfactorone pages 5-7, piper2019nuclearfactorone pages 1-2)
3. **Systems-level brain phenotypes** → megalencephaly/macrocephaly, altered commissural tract microstructure/connectomics, and downstream cognitive/behavioral phenotypes, supported by Nfix+/− mouse model data. (oishi2019heterozygosityfornuclear pages 1-2, oishi2019heterozygosityfornuclear pages 7-9, oishi2019heterozygosityfornuclear pages 3-4)
4. **Multisystem manifestations** (ocular, musculoskeletal, neurologic, psychobehavioral) evolve across childhood into adulthood; adult natural history demonstrates high rates of ongoing psychobehavioral, musculoskeletal, and vision complications. (macchiaiolo2022adeepphenotyping pages 1-2, makker2024apatientcase pages 11-12)

### 6) Phenotypic manifestations and mechanistic links
#### High-confidence core phenotypes (with statistics)
From large compiled cohorts (≥100 individuals), key frequencies include **macrocephaly 100%**, **developmental delay/intellectual disability 100%**, and distinctive facial features 100%. (priolo2024nfixrelatedmalansyndromeb pages 3-5, priolo2024nfixrelatedmalansyndrome media 09fd8188)

From the same frequency summaries: postnatal height >2 SD was reported at ~56%; hypotonia ~65%; epilepsy/EEG anomalies ~63%; autonomic signs ~25%; and ocular issues are frequent (refractive errors ~75%, strabismus ~63%, optic nerve hypoplasia ~25%), while major cardiac anomalies are uncommon (~4%). (priolo2024nfixrelatedmalansyndromeb pages 5-7, priolo2024nfixrelatedmalansyndromea pages 5-7, priolo2024nfixrelatedmalansyndrome pages 3-5, priolo2024nfixrelatedmalansyndrome media 09fd8188)

A clinical “expert summary” statement in the 2024 chapter emphasizes intellectual disability severity: **“normal intellectual development has never been reported in MALNS and mild ID is rarely observed.”** (priolo2024nfixrelatedmalansyndromea pages 9-11)

#### Adult natural history (2024; real-world progression)
A 2024 adult survey (n=28) characterized adulthood as multisystemic, with **psychobehavioral comorbidities 96%**, **musculoskeletal involvement 96%**, **vision impairment 96%**, and **neurological complications 86%**. (makker2024apatientcase pages 11-12)

#### Mechanistic links
- **Macrocephaly/megalencephaly** is consistent with experimental evidence that NFIX influences neural progenitor self-renewal vs differentiation and developmental timing in the brain. (piper2019nuclearfactorone pages 5-7, piper2019nuclearfactorone pages 1-2)
- **Cognitive/behavioral phenotypes** are consistent with hippocampal neurogenesis defects and connectome/commissural tract abnormalities reported in Nfix+/− models. (piper2019nuclearfactorone pages 5-7, oishi2019heterozygosityfornuclear pages 7-9)
- **Ocular phenotypes** (optic nerve hypoplasia/atrophy) likely reflect developmental transcriptional dysregulation, though direct NFIX→optic-nerve mechanistic studies were not retrieved in this search; clinical evidence supports frequent ophthalmologic involvement. (priolo2024nfixrelatedmalansyndromeb pages 5-7, makker2024apatientcase pages 11-12)

## Recent developments and latest research (prioritizing 2023–2024)
### 2024: Novel molecular mechanism—NFIX intragenic duplication with RNA-seq confirmation
Zhao et al. (American Journal of Medical Genetics Part A; Jan 2024; https://doi.org/10.1002/ajmg.a.63516) reported the first Malan syndrome case caused by an intragenic NFIX tandem duplication (exons 6–7) and used exon-level microarray plus RNA-seq to show ~50% NFIX transcript levels and absence of the mutant transcript, supporting NMD-mediated haploinsufficiency. (zhao2024novelmolecularmechanism pages 3-5)

**Clinical implementation implication:** small intragenic CNVs can be missed by standard tests, motivating genome/exon-level CNV approaches and RNA confirmation in unresolved cases. (zhao2024novelmolecularmechanism pages 3-5)

### 2024: Downstream targets and potential druggability concepts (CRABP2/VCAM1)
Kooblall et al. (JBMR Plus; May 2024; https://doi.org/10.1093/jbmrpl/ziae060) used RNA-seq/proteomics across Nfix mouse models and patient fibroblasts to identify misregulated genes and validated **CRABP2** as a **direct NFIX-regulated** gene (promoter regulation), suggesting downstream pathway nodes (retinoid biology) that might be leveraged therapeutically in NFIX-related skeletal dysplasias (conceptual at present). (kooblall2024identificationofcellular pages 2-3)

### 2024: Adult natural history and standards-of-care needs
Huynh et al. (Orphanet Journal of Rare Diseases; Jul 2024; https://doi.org/10.1186/s13023-024-03288-6) surveyed 28 adults and documented high prevalence of psychobehavioral, musculoskeletal, vision, and neurologic complications, emphasizing the need to extend management guidance beyond pediatrics. (makker2024apatientcase pages 11-12)

### 2024: Longitudinal clinical management case (15-year follow-up)
Makker et al. (Journal of Clinical Medicine; Nov 2024; https://doi.org/10.3390/jcm13216575) presented a long-term follow-up case and reinforced the centrality of NFIX dosage sensitivity (“haploinsufficiency”) to multisystem neurodevelopmental disease; the paper also discussed exploratory RNA-targeted strategies to increase NFIX translation rather than traditional overexpression approaches, due to dose sensitivity. (makker2024apatientcase pages 12-13)

## Current applications and real-world implementations
### Diagnostics
- **Primary application is genetic diagnosis** using exome/genome sequencing and copy-number variant detection for 19p13.2 deletions and intragenic NFIX variants; exon-level CNV and RNA analyses can be important in atypical/negative cases. (zhao2024novelmolecularmechanism pages 3-5, priolo2024nfixrelatedmalansyndrome pages 7-9)

### Multidisciplinary surveillance and management
A single-center deep phenotyping/surveillance program (Orphanet J Rare Dis; Jun 2022; https://doi.org/10.1186/s13023-022-02384-9) proposed a minimal dataset for follow-up and highlighted complications requiring active monitoring, including childhood fracture risk, neurovegetative symptoms, noise sensitivity, and Chiari I malformation. (macchiaiolo2022adeepphenotyping pages 1-2)

## Expert opinions and analysis (authoritative sources)
- The 2024 NFIX-related Malan syndrome chapter provides a consensus-style synthesis of variant mechanisms (NMD-driven haploinsufficiency; DNA-binding domain missense hotspots) and consolidates cohort-level phenotype frequencies. (priolo2024nfixrelatedmalansyndrome pages 19-21, priolo2024nfixrelatedmalansyndromeb pages 5-7)
- A high-impact cell biology review (Trends in Cell Biology; Jan 2019; https://doi.org/10.1016/j.tcb.2018.09.003) provides mechanistic framing for NFIX’s context-dependent roles in neural stem/progenitor biology, astrocyte maturation, and lineage specification, explaining how dosage changes can alter neurodevelopmental trajectories relevant to Malan syndrome. (piper2019nuclearfactorone pages 5-7, piper2019nuclearfactorone pages 1-2)

## Key statistics and data (recent cohorts)
- **Macrocephaly:** 100%; ≥77% of adults have head circumference >2 SD. (priolo2024nfixrelatedmalansyndrome pages 3-5, priolo2024nfixrelatedmalansyndromeb pages 3-5, priolo2024nfixrelatedmalansyndrome media 09fd8188)
- **Developmental delay / intellectual disability:** 100%; typically moderate to severe. (priolo2024nfixrelatedmalansyndrome pages 3-5, priolo2024nfixrelatedmalansyndromeb pages 3-5, priolo2024nfixrelatedmalansyndromea pages 9-11)
- **Postnatal height >2 SD:** ~56%. (priolo2024nfixrelatedmalansyndrome pages 3-5, priolo2024nfixrelatedmalansyndromeb pages 3-5)
- **Hypotonia:** ~65%. (priolo2024nfixrelatedmalansyndrome pages 3-5, priolo2024nfixrelatedmalansyndromeb pages 3-5)
- **Epilepsy/EEG anomalies:** ~63% in one deep-phenotyping cohort; risk may be higher with contiguous deletions including nearby genes. (priolo2024nfixrelatedmalansyndrome pages 3-5, priolo2024nfixrelatedmalansyndrome pages 7-9)
- **Adult complications (n=28):** psychobehavioral comorbidity 96%, musculoskeletal involvement 96%, vision impairment 96%, neurological complications 86%. (makker2024apatientcase pages 11-12)

## Knowledge-base–ready annotation block
### Pathophysiology description (narrative)
Malan syndrome is caused by heterozygous loss-of-function of NFIX, most commonly via truncating variants that are predicted to trigger NMD and create NFIX haploinsufficiency, or via missense variants in the DNA-binding/dimerization domain that impair DNA binding. Reduced NFIX dosage disrupts transcriptional regulation of developmental programs governing neural stem/progenitor differentiation timing, intermediate progenitor generation (via INSC), cell-cycle exit (via repression of BBX), and glial lineage specification and astrocyte maturation (via GFAP and broader astrocyte programs), leading to megalencephaly/macrocephaly and downstream neurodevelopmental deficits; animal models further link NFIX haploinsufficiency to altered commissural tract microstructure/connectome organization and learning/social behavior abnormalities. (priolo2024nfixrelatedmalansyndromeb pages 19-21, piper2019nuclearfactorone pages 3-5, piper2019nuclearfactorone pages 5-7, kooblall2024identificationofcellular pages 2-3, oishi2019heterozygosityfornuclear pages 3-4)

### Gene/protein annotations
- **NFIX (HGNC:7892)**: sequence-specific DNA-binding transcription factor; haploinsufficiency mechanism via NMD for many truncating alleles. (priolo2024nfixrelatedmalansyndromeb pages 19-21, priolo2024nfixrelatedmalansyndrome pages 21-23)
- **Downstream targets (evidence):** INSC, GFAP, BBX, CRABP2, VCAM1. (piper2019nuclearfactorone pages 3-5, kooblall2024identificationofcellular pages 2-3)

### Phenotype associations (HPO examples; evidence-supported)
- **Macrocephaly (HP:0000256)**. (priolo2024nfixrelatedmalansyndrome pages 3-5, priolo2024nfixrelatedmalansyndrome media 09fd8188)
- **Intellectual disability (HP:0001249)** / **global developmental delay (HP:0001263)**. (priolo2024nfixrelatedmalansyndrome pages 3-5, priolo2024nfixrelatedmalansyndromea pages 9-11)
- **Hypotonia (HP:0001252)**. (priolo2024nfixrelatedmalansyndrome pages 3-5)
- **Strabismus (HP:0000486)** / **refractive error (HP:0000517)** / **optic nerve hypoplasia (HP:0000609)**. (priolo2024nfixrelatedmalansyndromeb pages 5-7, makker2024apatientcase pages 11-12)
- **Seizures (HP:0001250)** / abnormal EEG. (priolo2024nfixrelatedmalansyndrome pages 3-5)
- **Scoliosis (HP:0002650)** / skeletal anomalies. (priolo2024nfixrelatedmalansyndromeb pages 5-7, makker2024apatientcase pages 11-12)
- **Chiari malformation type I (HP:0007099)**. (macchiaiolo2022adeepphenotyping pages 1-2, makker2024apatientcase pages 11-12)

### Cell type involvement (CL examples)
- Neural stem/progenitor cells and radial glia; intermediate progenitors; astrocyte lineage; oligodendrocyte lineage; ependymal cells; mature cortical neurons. (piper2019nuclearfactorone pages 3-5, piper2019nuclearfactorone pages 1-2, piper2019nuclearfactorone pages 2-3)

### Anatomical locations (UBERON examples)
- Cerebral cortex/neocortex; hippocampus/dentate gyrus; corpus callosum/anterior commissure; optic nerve; skeletal primordia/growth plate. (oishi2019heterozygosityfornuclear pages 3-4, oishi2019heterozygosityfornuclear pages 7-9, malan2010distincteffectsof pages 4-5)

### Chemical entities (CHEBI examples)
- **Retinoic acid (CHEBI:15367)** via CRABP2 pathway linkage (mechanistic node; not established as therapy). (kooblall2024identificationofcellular pages 2-3)

## Evidence table (compact)
The following table compiles genetics, mechanisms, targets, phenotypes, statistics, and applications with traceable citations.

| Category | Key points | Representative evidence & statistics | Key sources with year | DOI/URL | PMID |
|---|---|---|---|---|---|
| Genetics | Malan syndrome / Malan overgrowth syndrome is an autosomal dominant NFIX-related disorder caused by heterozygous loss-of-function variants or 19p13.2 deletions; MONDO:0013885. Mechanistically, disease is primarily due to NFIX haploinsufficiency, usually from truncating/splice variants predicted to trigger nonsense-mediated decay (NMD); missense variants in the DNA-binding/dimerization domain likely impair DNA binding. Most cases are de novo. Distinct from Marshall-Smith syndrome, where 3′ truncating variants may escape NMD and act differently. (priolo2024nfixrelatedmalansyndrome pages 19-21, priolo2024nfixrelatedmalansyndromeb pages 19-21, priolo2024nfixrelatedmalansyndromea pages 19-21, priolo2024nfixrelatedmalansyndrome pages 7-9) | At least ~25% of affected individuals have 19p13.2 deletions including NFIX; larger deletions can include CACNA1A and raise seizure risk. Historical review of 20 published patients found 14 deletions, 3 truncating variants, and 3 missense/in-frame variants. (klaassens2015malansyndromesotoslike pages 4-5, priolo2024nfixrelatedmalansyndrome pages 7-9) | Malan et al., 2010; Klaassens et al., 2015; Priolo, 2024; Zhao et al., 2024 | https://doi.org/10.1016/j.ajhg.2010.07.001; https://doi.org/10.1038/ejhg.2014.162; https://doi.org/10.1002/ajmg.a.63516 |  |
| Mechanism | NFIX is a dose-sensitive transcription factor of the NFI family that binds a palindromic DNA motif as homo-/heterodimers. Haploinsufficiency disrupts developmental transcriptional programs controlling neural progenitor cell-cycle exit, intermediate progenitor generation, gliogenesis, astrocyte maturation, and repression of oligodendroglial fate; this provides a mechanistic basis for megalencephaly, neurodevelopmental disability, and multisystem developmental abnormalities. (priolo2024nfixrelatedmalansyndromeb pages 19-21, piper2019nuclearfactorone pages 9-10, piper2019nuclearfactorone pages 3-5, piper2019nuclearfactorone pages 5-7, piper2019nuclearfactorone pages 1-2) | Primary developmental mechanism: delayed differentiation of radial glia/NSCs, reduced neuronal/glial differentiation late in embryogenesis, prolonged progenitor self-renewal, and altered lineage choice toward oligodendrogenesis. NFIX also regulates stem-cell proliferation, quiescence, and differentiation across tissues. (makker2024apatientcase pages 12-13, piper2019nuclearfactorone pages 3-5, piper2019nuclearfactorone pages 5-7, piper2019nuclearfactorone pages 1-2) | Piper et al., 2019; Oishi et al., 2019; Priolo, 2024; Makker et al., 2024 | https://doi.org/10.1016/j.tcb.2018.09.003; https://doi.org/10.1016/j.ebiom.2018.11.044; https://doi.org/10.3390/jcm13216575 |  |
| Downstream targets | Validated or reported NFIX downstream targets include **INSC** (intermediate progenitor generation), **GFAP** (astrocyte differentiation), **BBX/Bobby Sox** (cell-cycle progression repression in neural progenitors), and more recently **CRABP2** and **VCAM1** in fibroblast/MEF models. NFIX can act as activator or repressor in a context-dependent manner. (piper2019nuclearfactorone pages 3-5, piper2019nuclearfactorone pages 5-7, kooblall2024identificationofcellular pages 2-3) | INSC activation links NFIX to spindle orientation and intermediate progenitor production; GFAP activation links NFIX to astrocyte maturation; BBX repression links NFIX to G1→S control and progenitor exit. Multi-omics in 2024 identified 191 misregulated transcripts and 815 misregulated proteins in Nfix mutant MEFs, with CRABP2 directly regulated at promoter level and altered in 60%–100% of MSS fibroblasts. (piper2019nuclearfactorone pages 3-5, piper2019nuclearfactorone pages 5-7, kooblall2024identificationofcellular pages 2-3) | Piper et al., 2019; Kooblall et al., 2024 | https://doi.org/10.1016/j.tcb.2018.09.003; https://doi.org/10.1093/jbmrpl/ziae060 |  |
| Cell types & tissues | Key affected cell types include radial glia / neural stem cells, intermediate progenitors, astrocyte-lineage cells, oligodendrocyte-lineage cells, ependymal cells, neuroblasts, mature cortical neurons, and fibroblasts/MEFs used for mechanistic studies. Principal tissues are developing brain (neocortex, hippocampus, SVZ/RMS, cerebellum), optic system, skeleton/bone, and connective/musculoskeletal tissues. (piper2019nuclearfactorone pages 9-10, piper2019nuclearfactorone pages 3-5, piper2019nuclearfactorone pages 5-7, piper2019nuclearfactorone pages 1-2, piper2019nuclearfactorone pages 2-3, malan2010distincteffectsof pages 4-5) | NFIX expression is reported in embryonic germinal zones, radial glia, intermediate progenitors, cortical plate, dentate gyrus, ventricular zones, cerebellar granule progenitors, ependymal cells, and about half of mature neocortical neurons. During development, skeletal primordia and growth-plate chondrocytes also express NFIX. (piper2019nuclearfactorone pages 3-5, piper2019nuclearfactorone pages 1-2, piper2019nuclearfactorone pages 2-3, malan2010distincteffectsof pages 4-5) | Piper et al., 2019; Malan et al., 2010; Kooblall et al., 2024 | https://doi.org/10.1016/j.tcb.2018.09.003; https://doi.org/10.1016/j.ajhg.2010.07.001; https://doi.org/10.1093/jbmrpl/ziae060 |  |
| Mouse model evidence | Nfix+/− mice model NFIX haploinsufficiency and reproduce key Malan syndrome features including megalencephaly, abnormal forebrain commissures/connectivity, and learning/social deficits. Nfix−/− mice show more severe developmental phenotypes including megalencephaly, delayed cortical differentiation, altered oligodendrogenesis, skeletal defects, failure to thrive, and early death. (oishi2019heterozygosityfornuclear pages 1-2, piper2019nuclearfactorone pages 5-7, piper2019nuclearfactorone pages 3-5, oishi2019heterozygosityfornuclear pages 7-9, piper2019nuclearfactorone pages 1-2, malan2010distincteffectsof pages 4-5) | In adult Nfix+/− mice, total brain volume was 532.34 ± 22.61 vs 457.75 ± 20.63 in WT (p<0.0001), with 19/20 brain subregions enlarged; largest increases: corpus callosum 25.46%, neocortex 23.11%, anterior commissure 17.52%. Diffusion MRI showed reduced tract density and abnormal commissural microstructure; behavioral testing showed impaired spatial memory and abnormal sociability. (oishi2019heterozygosityfornuclear pages 1-2, oishi2019heterozygosityfornuclear pages 7-9, oishi2019heterozygosityfornuclear pages 3-4) | Oishi et al., 2019; Piper et al., 2019; Malan et al., 2010 | https://doi.org/10.1016/j.ebiom.2018.11.044; https://doi.org/10.1016/j.tcb.2018.09.003; https://doi.org/10.1016/j.ajhg.2010.07.001 |  |
| Clinical frequencies | Core phenotype is consistent across cohorts: distinctive facial features, developmental delay/intellectual disability, and macrocephaly are essentially universal; overgrowth is common but variable. Vision, musculoskeletal, behavioral, and neurologic complications are frequent. (priolo2024nfixrelatedmalansyndromeb pages 5-7, priolo2024nfixrelatedmalansyndromea pages 5-7, priolo2024nfixrelatedmalansyndrome pages 5-7, priolo2024nfixrelatedmalansyndrome pages 3-5, priolo2024nfixrelatedmalansyndromeb pages 3-5, priolo2024nfixrelatedmalansyndrome media 09fd8188) | Reported frequencies include: distinctive facial features 100%; macrocephaly 100% with ≥77% of adults >2 SD; developmental delay/ID 100%; postnatal height >2 SD 56%; hypotonia ~65%; neurobehavioral features ~67%; epilepsy/EEG anomalies 63%; autonomic signs 25%; slender habitus 100% (16/16); advanced bone age 76%; abnormal spine curvature 75%; pes planus 69%; refractive error 75%; strabismus 63%; optic nerve hypoplasia 25%; cardiac anomalies uncommon (~4%). Adult survey (n=28): psychobehavioral 96%, musculoskeletal 96%, vision impairment 96%, neurologic complications 86%; anxiety 79%, hypotonia 75%, movement difficulty 75%, scoliosis 64%, constipation 54%, optic atrophy 32%. (priolo2024nfixrelatedmalansyndromeb pages 5-7, priolo2024nfixrelatedmalansyndromea pages 5-7, priolo2024nfixrelatedmalansyndrome pages 5-7, makker2024apatientcase pages 11-12, priolo2024nfixrelatedmalansyndrome pages 3-5, priolo2024nfixrelatedmalansyndromeb pages 3-5) | Macchiaiolo et al., 2022; Huynh et al., 2024; Priolo, 2024; Makker et al., 2024 | https://doi.org/10.1186/s13023-022-02384-9; https://doi.org/10.1186/s13023-024-03288-6; https://doi.org/10.3390/jcm13216575 |  |
| Recent developments | 2024 studies materially advanced mechanism and natural history. A novel intragenic NFIX duplication (exons 6–7) was shown by GS/exon-array/RNA-seq to cause haploinsufficiency via NMD; adult natural-history data refined syndrome progression; and multi-omics identified CRABP2 as a direct NFIX target with therapeutic relevance. (zhao2024novelmolecularmechanism pages 3-5, makker2024apatientcase pages 12-13) | The 2024 AJMG case showed ~50% NFIX transcript level with absence of mutant transcript in fibroblasts, supporting NMD-mediated haploinsufficiency. The 2024 adult survey enrolled 28 adults and highlighted evolving burden of psychobehavioral, musculoskeletal, vision, and neurologic complications. The 2024 longitudinal case emphasized developmental gains with early intervention and discussed future RNA-based therapeutic concepts. (zhao2024novelmolecularmechanism pages 3-5, makker2024apatientcase pages 12-13, makker2024apatientcase pages 11-12) | Zhao et al., 2024; Huynh et al., 2024; Makker et al., 2024; Kooblall et al., 2024 | https://doi.org/10.1002/ajmg.a.63516; https://doi.org/10.1186/s13023-024-03288-6; https://doi.org/10.3390/jcm13216575; https://doi.org/10.1093/jbmrpl/ziae060 |  |
| Applications & management | Real-world implementation is currently centered on molecular diagnosis and multidisciplinary surveillance. Evidence supports using exome/genome sequencing plus CNV-sensitive methods and, when needed, RNA studies because small intragenic rearrangements may be missed by routine tests. Clinical management focuses on ophthalmologic, neurologic, behavioral, musculoskeletal, and developmental monitoring. (zhao2024novelmolecularmechanism pages 3-5, macchiaiolo2022adeepphenotyping pages 1-2, makker2024apatientcase pages 12-13) | Single-center surveillance proposed a minimal follow-up dataset and identified complications warranting active monitoring, including fractures, neurovegetative symptoms, noise sensitivity, and Chiari I malformation. Adult natural-history work proposed additional adult recommendations. Future therapy discussion is exploratory: because NFIX is dose-sensitive, AAV overexpression may be risky; RNA-targeted approaches such as antisense strategies to increase translation were proposed, but no disease-specific clinical therapies are established. (macchiaiolo2022adeepphenotyping pages 1-2, makker2024apatientcase pages 12-13) | Macchiaiolo et al., 2022; Huynh et al., 2024; Makker et al., 2024; Zhao et al., 2024 | https://doi.org/10.1186/s13023-022-02384-9; https://doi.org/10.1186/s13023-024-03288-6; https://doi.org/10.3390/jcm13216575; https://doi.org/10.1002/ajmg.a.63516 |  |


*Table: This table summarizes the key genetics, mechanisms, downstream targets, model systems, phenotype frequencies, and 2024 developments relevant to Malan syndrome pathophysiology. It is designed as a compact evidence-traceable reference for a disease knowledge base entry.*

## Key visual evidence
A cohort frequency table for Malan syndrome clinical features is provided in the 2024 chapter (Table 2; cropped), supporting reported frequencies for macrocephaly, developmental delay/ID, hypotonia, epilepsy/EEG anomalies, and ocular/musculoskeletal involvement. (priolo2024nfixrelatedmalansyndrome media 09fd8188, priolo2024nfixrelatedmalansyndrome media c2ca2dc8)

## Limitations and gaps
Despite clear evidence for NFIX haploinsufficiency as the proximal cause, the **full downstream transcriptional network** and tissue-specific target sets in human neurodevelopment remain incompletely mapped, and no disease-specific molecular therapy is yet established in clinical practice; current care is therefore surveillance- and support-focused. (makker2024apatientcase pages 12-13, piper2019nuclearfactorone pages 9-10)

## Source URLs and publication dates (selected)
- Zhao J et al. *Am J Med Genet A* (Jan 2024). https://doi.org/10.1002/ajmg.a.63516 (zhao2024novelmolecularmechanism pages 3-5)
- Kooblall KG et al. *JBMR Plus* (May 2024). https://doi.org/10.1093/jbmrpl/ziae060 (kooblall2024identificationofcellular pages 2-3)
- Huynh TN et al. *Orphanet J Rare Dis* (Jul 2024). https://doi.org/10.1186/s13023-024-03288-6 (makker2024apatientcase pages 11-12)
- Makker S et al. *J Clin Med* (Nov 2024). https://doi.org/10.3390/jcm13216575 (makker2024apatientcase pages 12-13)
- Piper M et al. *Trends Cell Biol* (Jan 2019). https://doi.org/10.1016/j.tcb.2018.09.003 (piper2019nuclearfactorone pages 3-5)
- Oishi S et al. *EBioMedicine* (Jan 2019). https://doi.org/10.1016/j.ebiom.2018.11.044 (oishi2019heterozygosityfornuclear pages 3-4)



References

1. (priolo2024nfixrelatedmalansyndrome pages 19-21): M Priolo. Nfix-related malan syndrome. Unknown journal, 2024.

2. (priolo2024nfixrelatedmalansyndromeb pages 19-21): M Priolo. Nfix-related malan syndrome. Unknown journal, 2024.

3. (priolo2024nfixrelatedmalansyndromea pages 19-21): M Priolo. Nfix-related malan syndrome. Unknown journal, 2024.

4. (makker2024apatientcase pages 12-13): Simran Makker, Bernadine R. Gagnon, Isabella Trew, Vivian Mougios, Anne Hanna, Jessica M. Cale, and Craig S. McIntosh. A patient case of malan syndrome involving 19p13.2 deletion of nfix with longitudinal follow-up and future prospectives. Journal of Clinical Medicine, 13:6575, Nov 2024. URL: https://doi.org/10.3390/jcm13216575, doi:10.3390/jcm13216575. This article has 3 citations.

5. (zhao2024novelmolecularmechanism pages 3-5): Jian Zhao, Nicola Longo, Robert G. Lewis, Thomas J. Nicholas, Steven E. Boyden, Ashley Andrews, Austin Larson, Pinar Bayrak‐Toydemir, Lorenzo D. Botto, and Rong Mao. Novel molecular mechanism in malan syndrome uncovered through genome sequencing reanalysis, exon‐level array, and rna sequencing. American Journal of Medical Genetics Part A, Jan 2024. URL: https://doi.org/10.1002/ajmg.a.63516, doi:10.1002/ajmg.a.63516. This article has 4 citations.

6. (priolo2024nfixrelatedmalansyndrome pages 21-23): M Priolo. Nfix-related malan syndrome. Unknown journal, 2024.

7. (priolo2024nfixrelatedmalansyndrome pages 7-9): M Priolo. Nfix-related malan syndrome. Unknown journal, 2024.

8. (piper2019nuclearfactorone pages 3-5): Michael Piper, Richard Gronostajski, and Graziella Messina. Nuclear factor one x in development and disease. Trends in cell biology, 29 1:20-30, Jan 2019. URL: https://doi.org/10.1016/j.tcb.2018.09.003, doi:10.1016/j.tcb.2018.09.003. This article has 68 citations and is from a domain leading peer-reviewed journal.

9. (piper2019nuclearfactorone pages 5-7): Michael Piper, Richard Gronostajski, and Graziella Messina. Nuclear factor one x in development and disease. Trends in cell biology, 29 1:20-30, Jan 2019. URL: https://doi.org/10.1016/j.tcb.2018.09.003, doi:10.1016/j.tcb.2018.09.003. This article has 68 citations and is from a domain leading peer-reviewed journal.

10. (piper2019nuclearfactorone pages 1-2): Michael Piper, Richard Gronostajski, and Graziella Messina. Nuclear factor one x in development and disease. Trends in cell biology, 29 1:20-30, Jan 2019. URL: https://doi.org/10.1016/j.tcb.2018.09.003, doi:10.1016/j.tcb.2018.09.003. This article has 68 citations and is from a domain leading peer-reviewed journal.

11. (oishi2019heterozygosityfornuclear pages 1-2): Sabrina Oishi, Danyon Harkins, Nyoman D. Kurniawan, Maria Kasherman, Lachlan Harris, Oressia Zalucki, Richard M. Gronostajski, Thomas H.J. Burne, and Michael Piper. Heterozygosity for nuclear factor one x in mice models features of malan syndrome. EBioMedicine, 39:388-400, Jan 2019. URL: https://doi.org/10.1016/j.ebiom.2018.11.044, doi:10.1016/j.ebiom.2018.11.044. This article has 21 citations and is from a peer-reviewed journal.

12. (kooblall2024identificationofcellular pages 2-3): Kreepa G Kooblall, Mark Stevenson, Raphael Heilig, Michelle Stewart, Benjamin Wright, Helen Lockstone, David Buck, Roman Fischer, Sara Wells, Kate E Lines, Lydia Teboul, Raoul C Hennekam, and Rajesh V Thakker. Identification of cellular retinoic acid binding protein 2 (crabp2) as downstream target of nuclear factor i/x (nfix): implications for skeletal dysplasia syndromes. JBMR Plus, May 2024. URL: https://doi.org/10.1093/jbmrpl/ziae060, doi:10.1093/jbmrpl/ziae060. This article has 3 citations and is from a peer-reviewed journal.

13. (oishi2019heterozygosityfornuclear pages 3-4): Sabrina Oishi, Danyon Harkins, Nyoman D. Kurniawan, Maria Kasherman, Lachlan Harris, Oressia Zalucki, Richard M. Gronostajski, Thomas H.J. Burne, and Michael Piper. Heterozygosity for nuclear factor one x in mice models features of malan syndrome. EBioMedicine, 39:388-400, Jan 2019. URL: https://doi.org/10.1016/j.ebiom.2018.11.044, doi:10.1016/j.ebiom.2018.11.044. This article has 21 citations and is from a peer-reviewed journal.

14. (oishi2019heterozygosityfornuclear pages 7-9): Sabrina Oishi, Danyon Harkins, Nyoman D. Kurniawan, Maria Kasherman, Lachlan Harris, Oressia Zalucki, Richard M. Gronostajski, Thomas H.J. Burne, and Michael Piper. Heterozygosity for nuclear factor one x in mice models features of malan syndrome. EBioMedicine, 39:388-400, Jan 2019. URL: https://doi.org/10.1016/j.ebiom.2018.11.044, doi:10.1016/j.ebiom.2018.11.044. This article has 21 citations and is from a peer-reviewed journal.

15. (priolo2024nfixrelatedmalansyndromeb pages 5-7): M Priolo. Nfix-related malan syndrome. Unknown journal, 2024.

16. (makker2024apatientcase pages 11-12): Simran Makker, Bernadine R. Gagnon, Isabella Trew, Vivian Mougios, Anne Hanna, Jessica M. Cale, and Craig S. McIntosh. A patient case of malan syndrome involving 19p13.2 deletion of nfix with longitudinal follow-up and future prospectives. Journal of Clinical Medicine, 13:6575, Nov 2024. URL: https://doi.org/10.3390/jcm13216575, doi:10.3390/jcm13216575. This article has 3 citations.

17. (malan2010distincteffectsof pages 4-5): Valérie Malan, Diana Rajan, Sophie Thomas, Adam C. Shaw, Hélène Louis dit Picard, Valérie Layet, Marianne Till, Arie van Haeringen, Geert Mortier, Sheela Nampoothiri, Silvija Pušeljić, Laurence Legeai-Mallet, Nigel P. Carter, Michel Vekemans, Arnold Munnich, Raoul C. Hennekam, Laurence Colleaux, and Valérie Cormier-Daire. Distinct effects of allelic nfix mutations on nonsense-mediated mrna decay engender either a sotos-like or a marshall-smith syndrome. American journal of human genetics, 87 2:189-98, Aug 2010. URL: https://doi.org/10.1016/j.ajhg.2010.07.001, doi:10.1016/j.ajhg.2010.07.001. This article has 187 citations and is from a highest quality peer-reviewed journal.

18. (piper2019nuclearfactorone pages 9-10): Michael Piper, Richard Gronostajski, and Graziella Messina. Nuclear factor one x in development and disease. Trends in cell biology, 29 1:20-30, Jan 2019. URL: https://doi.org/10.1016/j.tcb.2018.09.003, doi:10.1016/j.tcb.2018.09.003. This article has 68 citations and is from a domain leading peer-reviewed journal.

19. (macchiaiolo2022adeepphenotyping pages 1-2): Marina Macchiaiolo, Filippo M. Panfili, Davide Vecchio, Michaela V. Gonfiantini, Fabiana Cortellessa, Cristina Caciolo, Marcella Zollino, Maria Accadia, Marco Seri, Marcello Chinali, Corrado Mammì, Marco Tartaglia, Andrea Bartuli, Paolo Alfieri, and Manuela Priolo. A deep phenotyping experience: up to date in management and diagnosis of malan syndrome in a single center surveillance report. Orphanet Journal of Rare Diseases, Jun 2022. URL: https://doi.org/10.1186/s13023-022-02384-9, doi:10.1186/s13023-022-02384-9. This article has 25 citations and is from a peer-reviewed journal.

20. (priolo2024nfixrelatedmalansyndromeb pages 3-5): M Priolo. Nfix-related malan syndrome. Unknown journal, 2024.

21. (priolo2024nfixrelatedmalansyndrome media 09fd8188): M Priolo. Nfix-related malan syndrome. Unknown journal, 2024.

22. (priolo2024nfixrelatedmalansyndromea pages 5-7): M Priolo. Nfix-related malan syndrome. Unknown journal, 2024.

23. (priolo2024nfixrelatedmalansyndrome pages 3-5): M Priolo. Nfix-related malan syndrome. Unknown journal, 2024.

24. (priolo2024nfixrelatedmalansyndromea pages 9-11): M Priolo. Nfix-related malan syndrome. Unknown journal, 2024.

25. (piper2019nuclearfactorone pages 2-3): Michael Piper, Richard Gronostajski, and Graziella Messina. Nuclear factor one x in development and disease. Trends in cell biology, 29 1:20-30, Jan 2019. URL: https://doi.org/10.1016/j.tcb.2018.09.003, doi:10.1016/j.tcb.2018.09.003. This article has 68 citations and is from a domain leading peer-reviewed journal.

26. (klaassens2015malansyndromesotoslike pages 4-5): Merel Klaassens, Deborah Morrogh, Elisabeth M Rosser, Fatima Jaffer, Maaike Vreeburg, Levinus A Bok, Tim Segboer, Martine van Belzen, Ros M Quinlivan, Ajith Kumar, Jane A Hurst, and Richard H Scott. Malan syndrome: sotos-like overgrowth with de novo nfix sequence variants and deletions in six new patients and a review of the literature. European Journal of Human Genetics, 23:610-615, Aug 2015. URL: https://doi.org/10.1038/ejhg.2014.162, doi:10.1038/ejhg.2014.162. This article has 95 citations and is from a domain leading peer-reviewed journal.

27. (priolo2024nfixrelatedmalansyndrome pages 5-7): M Priolo. Nfix-related malan syndrome. Unknown journal, 2024.

28. (priolo2024nfixrelatedmalansyndrome media c2ca2dc8): M Priolo. Nfix-related malan syndrome. Unknown journal, 2024.