---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-24T12:42:15.539198'
end_time: '2026-01-24T12:47:35.445843'
duration_seconds: 319.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Retinoblastoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Retinoblastoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Retinoblastoma**.
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
- **Disease Name:** Retinoblastoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Retinoblastoma**.
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


Plan status update
- Objective 1 (assemble recent literature): Completed via targeted searches and evidence extraction (2022–2024 emphasis).
- Objective 2–6 (mechanisms, annotations, GO/CL/UBERON/CHEBI, progression/phenotypes, applications/statistics): Addressed below with citations.
- Objective 7 (create artifacts): Completed; see embedded artifact of key molecular players and ontology mappings.
- Objective 8 (final report): Submitted here.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Retinoblastoma
- MONDO ID: MONDO_0008380 (retinoblastoma); related: MONDO_0018160 (hereditary retinoblastoma), MONDO_0003073 (trilateral retinoblastoma) (OpenTargets metadata) (markovic2023geneticsinophthalmology pages 1-2)
- Category: Pediatric intraocular malignant embryonal tumor of the retina

1) Core Pathophysiology
- Initiation: Most retinoblastomas are initiated by biallelic inactivation of RB1 (Knudson’s two-hit). Patient-derived hiPSC retinal organoids with compound heterozygous RB1 mutations developed retinoblastoma-like tumors in vitro, providing direct experimental validation of the two-hit model (PNAS Nexus, 2022; URL: https://doi.org/10.1093/pnasnexus/pgac162; Aug 2022) (li2022secondhitimpels pages 12-13). A minority of tumors represent a MYCN-driven subgroup (some RB1-proficient), with MYCN activity promoting dedifferentiation and aggressive biology (Communications Biology, 2024; URL: https://doi.org/10.1038/s42003-024-06596-6; Jul 2024) (ryl2024amycndrivendedifferentiation pages 1-2).
- Cell-of-origin: Multiple lines of evidence implicate maturing cone photoreceptor precursors as the principal cell-of-origin in RB1-mutant disease; RB1 loss in ARR3+ cone precursors induces proliferation and tumor formation. MYCN-initiated RB arises from more immature cone precursors with lineage deconstraint (PNAS, 2022; URL: https://doi.org/10.1073/pnas.2200721119; Jul 2022). Spatial transcriptomics of human tumors confirms cone-precursor dominance among malignant populations (bioRxiv, 2024; URL: https://doi.org/10.1101/2024.02.05.578886; Feb 2024) (singh2022animmaturededifferentiated pages 10-10, wang2024spatialtranscriptomicprofiling pages 5-8, wang2024spatialtranscriptomicprofiling pages 1-5, li2022secondhitimpels pages 12-13).
- Dysregulated pathways: RB1/pRB–E2F cell-cycle checkpoint failure is central; downstream cooperation includes p53 pathway suppression through cone-programmed MDM2/MDM4, MYCN activation programs, and context-specific signaling (e.g., PI3K–AKT–mTOR; WNT/Notch/Hedgehog noted in RB literature) (IJMS, 2024; URL: https://doi.org/10.3390/ijms25136910; Jun 2024) (lisek2024histonedeacetylasesin pages 1-2, chavez2023pluripotentstemcellderived pages 56-60, ryl2024amycndrivendedifferentiation pages 1-2).
- Epigenetic dysregulation: DNA methylation patterns and enhancer-state changes define molecular subtypes; histone deacetylase activity is intertwined with pRB function and is dysregulated in RB (Communications Biology, 2024; IJMS, 2024) (ryl2024amycndrivendedifferentiation pages 1-2, lisek2024histonedeacetylasesin pages 1-2). Early RB1-deficient tumors can show differentiated histology with few genomic aberrations, followed by dedifferentiation and acquisition of non-cone features, consistent with progressive epigenetic remodeling (2023 organoid/model review) (chavez2023pluripotentstemcellderived pages 56-60).
- Microenvironment and hypoxia: Spatial profiling and prior single-cell analyses show tumor-associated macrophages (TAMs), glial cells, and cancer-associated fibroblasts. Hypoxia is relevant to metabolic and survival dependencies; RB1 loss creates a dependency on the nuclear receptor ESRRG, particularly pronounced in hypoxic tumor zones (Science Advances, 2022; URL: https://doi.org/10.1126/sciadv.abm8466; Aug 2022; bioRxiv spatial study 2024) (wang2024spatialtranscriptomicprofiling pages 5-8, wang2024spatialtranscriptomicprofiling pages 1-5, chavez2023pluripotentstemcellderived pages 56-60).
- Metabolism: RB exhibits glycolytic reprogramming; ALDOA (fructose-bisphosphate aldolase A) has been implicated as a modulator of tumorigenesis and tumor–macrophage interactions in RB at single-cell resolution (iScience, 2024; URL: https://doi.org/10.1016/j.isci.2024.110725; Sep 2024; 2023 review) (chavez2023pluripotentstemcellderived pages 56-60).

2) Key Molecular Players, Cell Types, Anatomy, and Chemicals
| Entity | Ontology ID | Type | Mechanistic role in RB pathophysiology (1–2 sentences) | Key supporting sources |
|---|---|---|---|---|
| RB1 | HGNC:9884 | Gene/Protein | Tumor suppressor whose biallelic inactivation (Knudson two‑hit) initiates most retinoblastomas by disabling pRB control of E2F, chromatin remodeling, differentiation and genome stability. | (markovic2023geneticsinophthalmology pages 1-2, li2022secondhitimpels pages 12-13, chavez2023pluripotentstemcellderived pages 56-60) |
| MYCN | HGNC:7553 | Gene/Oncogene | Oncogenic amplification drives a distinct RB1‑proficient aggressive subgroup by promoting dedifferentiation, protein synthesis and proliferation programs. | (ryl2024amycndrivendedifferentiation pages 1-2, singh2022animmaturededifferentiated pages 10-10, chavez2023pluripotentstemcellderived pages 56-60) |
| MDM2 | HGNC:6973 | Gene/Protein | E3 ligase and p53 inhibitor that is highly expressed in cone‑precursor circuitry, promoting proliferation and survival (supports MYCN translation and blunts p53 responses). | (chavez2023pluripotentstemcellderived pages 56-60, singh2022animmaturededifferentiated pages 10-10, wang2024spatialtranscriptomicprofiling pages 5-8) |
| MDM4 | HGNC:6975 | Gene/Protein | Negative regulator of p53 that cooperates with MDM2/p53 axis dysregulation in RB biology, contributing to impaired apoptosis in tumor cells. | (markovic2023geneticsinophthalmology pages 1-2, lisek2024histonedeacetylasesin pages 1-2, chavez2023pluripotentstemcellderived pages 56-60) |
| ESRRG | HGNC:3473 | Gene/Protein | Nuclear receptor identified as a dependency after RB1 loss; ESRRG supports retinogenesis/oxygen metabolism programs and its inhibition causes RB cell death, especially in hypoxia. | (chavez2023pluripotentstemcellderived pages 56-60, markovic2023geneticsinophthalmology pages 1-2) |
| E2F transcription factors | GO:0001078 | Pathway/Process (TF family) | E2F family are direct transcriptional targets restrained by pRB; when pRB is lost or E2F is overexpressed, E2F drives G1→S genes and uncontrolled proliferation. | (lisek2024histonedeacetylasesin pages 1-2, markovic2023geneticsinophthalmology pages 1-2, chavez2023pluripotentstemcellderived pages 56-60) |
| PI3K/AKT/mTOR signaling | GO:0014065, GO:0035556 | Pathway/Process | Growth‑ and survival‑promoting signaling cascade implicated in retinoblastoma cell survival and resistance mechanisms downstream of oncogenic drivers. | (lisek2024histonedeacetylasesin pages 1-2, wang2024spatialtranscriptomicprofiling pages 5-8) |
| WNT signaling | GO:0016055 | Pathway/Process | Developmental pathway involved in retinal development and reported as dysregulated in RB, contributing to proliferation/differentiation imbalance. | (lisek2024histonedeacetylasesin pages 1-2, markovic2023geneticsinophthalmology pages 1-2) |
| Notch signaling | GO:0007219 | Pathway/Process | Developmental signaling that can influence retinal cell fate decisions and has been implicated in RB‑related differentiation/proliferation changes. | (lisek2024histonedeacetylasesin pages 1-2, markovic2023geneticsinophthalmology pages 1-2) |
| Hedgehog signaling | GO:0007224 | Pathway/Process | Developmental morphogen pathway with potential roles in retinal progenitor behavior and tumor biology in RB contexts. | (lisek2024histonedeacetylasesin pages 1-2, markovic2023geneticsinophthalmology pages 1-2) |
| DNA methylation | GO:0006306 | Process (Epigenetic) | Altered CpG methylation and enhancer methylation distinguish RB subtypes and modulate photoreceptor gene programs and immune‑related gene expression. | (ryl2024amycndrivendedifferentiation pages 1-2, wang2024spatialtranscriptomicprofiling pages 5-8, chavez2023pluripotentstemcellderived pages 56-60) |
| Histone deacetylase activity / HDACs | GO:0004407 | Molecular function / Epigenetic regulators | HDACs interact with pRB and modulate chromatin states; dysregulated HDAC activity contributes to aberrant transcription, cell‑cycle control and survival in RB. | (lisek2024histonedeacetylasesin pages 1-2, markovic2023geneticsinophthalmology pages 1-2) |
| Cone photoreceptor precursor | CL:0011116 (or nearest) | Cell type | Principal cell‑of‑origin: maturing cone precursors (ARR3+/cone markers) are susceptible to RB1 loss and/or MYCN perturbation and give rise to cone‑like malignant cells. | (li2022secondhitimpels pages 12-13, singh2022animmaturededifferentiated pages 10-10, chavez2023pluripotentstemcellderived pages 56-60, wang2024spatialtranscriptomicprofiling pages 5-8) |
| Retina | UBERON:0000966 | Anatomy | Tissue of origin where RB1 inactivation or MYCN activation in developing retinal cells (cone precursors) initiates tumorigenesis. | (markovic2023geneticsinophthalmology pages 1-2, li2022secondhitimpels pages 12-13) |
| Tumor‑associated macrophage (TAM) | CL:0000863 | Cell type (TME) | TAMs are abundant in RB microenvironment and can create immunosuppressive niches, modulating invasion and therapeutic response. | (wang2024spatialtranscriptomicprofiling pages 5-8, chavez2023pluripotentstemcellderived pages 56-60, wang2024spatialtranscriptomicprofiling pages 1-5) |
| Cancer‑associated fibroblast (CAF) | CL:0002620 | Cell type (TME) | Minor stromal component in RB spatial maps that may support tumor architecture, signaling and extracellular matrix remodeling. | (wang2024spatialtranscriptomicprofiling pages 5-8) |
| ALDOA | HGNC:414 | Gene/Protein (metabolic enzyme) | Glycolytic enzyme linked to altered energy metabolism in RB; targeting ALDOA modulates tumorigenesis and tumor‑macrophage interactions. | (chavez2023pluripotentstemcellderived pages 56-60, wang2024spatialtranscriptomicprofiling pages 5-8) |
| Glycolytic process | GO:0006096 | Process / Metabolism | Metabolic reprogramming (enhanced glycolysis) supports proliferative/risky RB phenotypes and is associated with MYCN activity and energetic demands. | (chavez2023pluripotentstemcellderived pages 56-60, wang2024spatialtranscriptomicprofiling pages 5-8) |


*Table: Table summarizing principal genes, pathways, cell types and anatomical terms implicated in retinoblastoma pathophysiology, with ontology identifiers and supporting evidence (pqac IDs). This provides an at‑a‑glance annotation useful for knowledge‑base curation and mechanistic mapping.*

Additional notes and URLs:
- RB1 two-hit and pleiotropic pRB functions (Human Genomics, 2023; URL: https://doi.org/10.1186/s40246-023-00529-w; Sep 2023) (markovic2023geneticsinophthalmology pages 1-2).
- MYCN-driven RB subgroup and methylation-defined clusters (Communications Biology, 2024; URL above) (ryl2024amycndrivendedifferentiation pages 1-2).
- ESRRG dependency after RB1 loss (Science Advances, 2022; URL above) (chavez2023pluripotentstemcellderived pages 56-60).
- Spatial heterogeneity and trajectories (bioRxiv, 2024; URL above) (wang2024spatialtranscriptomicprofiling pages 5-8, wang2024spatialtranscriptomicprofiling pages 1-5).
- Organoid validation of the two-hit model (PNAS Nexus, 2022; URL above) (li2022secondhitimpels pages 12-13).

3) Biological Processes (GO) Disrupted
- Cell cycle G1/S transition via E2F de-repression (GO:0000082; GO:0051726), DNA replication (GO:0006260), mitotic cell cycle (GO:0000278) (lisek2024histonedeacetylasesin pages 1-2, markovic2023geneticsinophthalmology pages 1-2).
- Regulation of apoptosis and p53 signaling (GO:0043065; GO:0072331), influenced by MDM2/MDM4 elevation in cone circuitry (chavez2023pluripotentstemcellderived pages 56-60, singh2022animmaturededifferentiated pages 10-10).
- Photoreceptor differentiation programs and cone development pathways are subverted (GO:0001754, GO:0007601) as cone precursors become proliferative tumor cells (li2022secondhitimpels pages 12-13, singh2022animmaturededifferentiated pages 10-10, wang2024spatialtranscriptomicprofiling pages 5-8).
- Epigenetic regulation: DNA methylation (GO:0006306), histone deacetylation (GO:0016575), chromatin remodeling (GO:0006338) (ryl2024amycndrivendedifferentiation pages 1-2, lisek2024histonedeacetylasesin pages 1-2).
- Metabolic reprogramming: glycolytic process (GO:0006096) (chavez2023pluripotentstemcellderived pages 56-60).
- Pathway dysregulation: PI3K/AKT (GO:0014065), WNT (GO:0016055), Notch (GO:0007219), Hedgehog (GO:0007224) in RB contexts (lisek2024histonedeacetylasesin pages 1-2, markovic2023geneticsinophthalmology pages 1-2).

4) Cellular Components (GO/Anatomy)
- Nucleus (GO:0005634) and chromatin (GO:0000785): pRB–E2F control and epigenetic modifiers including HDACs (lisek2024histonedeacetylasesin pages 1-2, markovic2023geneticsinophthalmology pages 1-2).
- Mitochondrion and metabolic complexes (GO:0005739): ESRRG-regulated oxidative programs intersecting with hypoxia responses (chavez2023pluripotentstemcellderived pages 56-60).
- Retina (UBERON:0000966) with dominant malignant cone-precursor compartments; tumor niches containing TAMs and CAFs (wang2024spatialtranscriptomicprofiling pages 5-8, wang2024spatialtranscriptomicprofiling pages 1-5).

5) Disease Progression
- Heritable RB (germline RB1 mutation) typically presents earlier and often bilaterally; progression often follows an indolent retinoma stage (genomic instability, retinocytoma/retinoma) to invasive RB upon acquiring additional alterations and epigenetic dedifferentiation (PNAS, 2022; Human Genomics, 2023) (singh2022animmaturededifferentiated pages 10-10, markovic2023geneticsinophthalmology pages 1-2).
- Sporadic RB commonly involves somatic biallelic RB1 loss; a subset are MYCN-driven (some RB1-proficient) that rapidly transform from immature cone precursors and are more aggressive with dedifferentiated/stemness features (PNAS, 2022; Communications Biology, 2024) (singh2022animmaturededifferentiated pages 10-10, ryl2024amycndrivendedifferentiation pages 1-2).
- Spatial and single-cell pseudotime/velocity analyses show trajectories from cone-precursor-like states to highly proliferative/malignant clusters with increasing CNVs and cell-cycle gene expression (bioRxiv, 2024) (wang2024spatialtranscriptomicprofiling pages 5-8, wang2024spatialtranscriptomicprofiling pages 1-5).

6) Phenotypic Manifestations (HP terms and links to mechanisms)
- Leukocoria (HP:0001083) and strabismus (HP:0000486) as presenting signs are downstream of intraocular tumor mass arising from cone-precursor transformation (linked to RB1 loss/MYCN activity) (markovic2023geneticsinophthalmology pages 1-2).
- Bilateral disease (HP:0005247) in heritable cases due to germline RB1 mutation and independent second hits in both eyes (markovic2023geneticsinophthalmology pages 1-2, li2022secondhitimpels pages 12-13).
- Histologic heterogeneity including differentiated rosettes (Flexner–Wintersteiner) in early/differentiated tumors and dedifferentiated patterns in aggressive subtype 2 (ryl2024amycndrivendedifferentiation pages 1-2, markovic2023geneticsinophthalmology pages 1-2).

7) Current Applications and Implementations
- Organoid models: Human retinal organoids from patient-derived hiPSCs with engineered second-hit RB1 mutations recapitulate tumorigenesis, enabling mechanistic and drug response studies (PNAS Nexus, 2022; URL above) (li2022secondhitimpels pages 12-13).
- Spatial/single-cell profiling: Spatial transcriptomics has provided the first spatial gene atlas for RB, mapping subclonal architecture and TME interactions to inform targeted therapy strategies (bioRxiv, 2024; URL above) (wang2024spatialtranscriptomicprofiling pages 5-8, wang2024spatialtranscriptomicprofiling pages 1-5).
- Emerging dependencies/targets: ESRRG inhibitors as a potential therapeutic strategy in RB1-deficient RB, particularly under hypoxia (Science Advances, 2022; URL above) (chavez2023pluripotentstemcellderived pages 56-60). MYCN-targeted approaches could restore photoreceptor differentiation programs in MYCN-driven RB models (Communications Biology, 2024; URL above) (ryl2024amycndrivendedifferentiation pages 1-2). Epigenetic modulators (HDAC-focused strategies) are being explored preclinically (IJMS, 2024; URL above) (lisek2024histonedeacetylasesin pages 1-2). Metabolic targeting of ALDOA/glycolysis is emerging (iScience, 2024; URL above) (chavez2023pluripotentstemcellderived pages 56-60).
- Diagnostics: Cell-free tumor DNA from the anterior segment of the eye can be used for RB diagnostics/prognostics (Human Genomics, 2023; URL above) (markovic2023geneticsinophthalmology pages 1-2).

8) Expert Opinions, Statistics, and Data (2023–2024 emphasis)
- Global burden: “8,000 new cases … each year worldwide,” highlighting RB as the most frequent pediatric intraocular malignancy (Human Genomics, 2023; Sep 2023) (markovic2023geneticsinophthalmology pages 1-2).
- Molecular subtypes: Two major subtypes—Subtype 1 (differentiated photoreceptor signature; fewer additional alterations) and Subtype 2 (dedifferentiated cone states with neuronal/ganglion markers; frequent CNAs and MYCN activation)—inform risk and therapeutic strategies (Nature Communications synthesis cited within 2023 review; and Communications Biology, 2024) (markovic2023geneticsinophthalmology pages 1-2, ryl2024amycndrivendedifferentiation pages 1-2).
- Spatial heterogeneity: Ten spatially distinct tumor subpopulations with varying proliferative capacities; dominant cone-precursor lineage with glial and CAF contributions (bioRxiv, 2024) (wang2024spatialtranscriptomicprofiling pages 5-8, wang2024spatialtranscriptomicprofiling pages 1-5).

9) Evidence Items (select primary literature with PMIDs/DOIs/URLs)
- Li et al., PNAS Nexus, 2022 (two-hit validation in organoids). DOI: 10.1093/pnasnexus/pgac162; URL: https://doi.org/10.1093/pnasnexus/pgac162; Publication date: Aug 2022 (li2022secondhitimpels pages 12-13).
- Singh et al., PNAS, 2022 (MYCN-initiated RB cell-of-origin in immature cones). DOI: 10.1073/pnas.2200721119; URL: https://doi.org/10.1073/pnas.2200721119; Publication date: Jul 2022 (singh2022animmaturededifferentiated pages 10-10).
- Ryl et al., Communications Biology, 2024 (MYCN-driven subgroup and methylation-defined clusters). DOI: 10.1038/s42003-024-06596-6; URL: https://doi.org/10.1038/s42003-024-06596-6; Publication date: Jul 2024 (ryl2024amycndrivendedifferentiation pages 1-2).
- Field et al., Science Advances, 2022 (ESRRG dependency after RB1 loss; hypoxia). DOI: 10.1126/sciadv.abm8466; URL: https://doi.org/10.1126/sciadv.abm8466; Publication date: Aug 2022 (chavez2023pluripotentstemcellderived pages 56-60).
- Wang et al., bioRxiv, 2024 (spatial transcriptomics in human RB). DOI: 10.1101/2024.02.05.578886; URL: https://doi.org/10.1101/2024.02.05.578886; Publication date: Feb 2024 (wang2024spatialtranscriptomicprofiling pages 5-8, wang2024spatialtranscriptomicprofiling pages 1-5).
- Lisek et al., IJMS, 2024 (HDACs in RB). DOI: 10.3390/ijms25136910; URL: https://doi.org/10.3390/ijms25136910; Publication date: Jun 2024 (lisek2024histonedeacetylasesin pages 1-2).
- Marković et al., Human Genomics, 2023 (Genetics and subtypes, epidemiology). DOI: 10.1186/s40246-023-00529-w; URL: https://doi.org/10.1186/s40246-023-00529-w; Publication date: Sep 2023 (markovic2023geneticsinophthalmology pages 1-2).

Ontology Annotations (examples)
- HGNC: RB1 (HGNC:9884), MYCN (HGNC:7553), MDM2 (HGNC:6973), MDM4 (HGNC:6975), ESRRG (HGNC:3473), ALDOA (HGNC:414) (markovic2023geneticsinophthalmology pages 1-2, ryl2024amycndrivendedifferentiation pages 1-2, chavez2023pluripotentstemcellderived pages 56-60).
- GO Processes: cell cycle (GO:0007049), DNA methylation (GO:0006306), histone deacetylation (GO:0016575), glycolytic process (GO:0006096) (lisek2024histonedeacetylasesin pages 1-2, ryl2024amycndrivendedifferentiation pages 1-2, chavez2023pluripotentstemcellderived pages 56-60).
- CL: Cone photoreceptor precursor (CL:0011116); TAM (CL:0000863); CAF (CL:0002620) (li2022secondhitimpels pages 12-13, wang2024spatialtranscriptomicprofiling pages 5-8).
- UBERON: Retina (UBERON:0000966) (markovic2023geneticsinophthalmology pages 1-2).
- CHEBI: While specific chemotherapeutic entities are beyond the mechanistic scope here, metabolic substrates (e.g., D-glucose, CHEBI:17234) are relevant to glycolysis; metabolic targeting has focused on enzymes such as ALDOA (chavez2023pluripotentstemcellderived pages 56-60).

Expert synthesis
- The central unifying mechanism is RB1 loss disabling pRB’s control of E2F and chromatin, unleashing a cone-intrinsic proliferation circuitry augmented by MDM2/MDM4 and MYCN programs. Tumor evolution proceeds along cone-precursor lineages toward proliferative, CNV-rich states with progressive epigenetic dedifferentiation, while microenvironmental hypoxia and stromal cues (TAMs/CAFs) shape survival dependencies such as ESRRG. MYCN-driven, RB1-proficient disease reflects a distinct developmental susceptibility of immature cone states, with therapeutic implications for MYCN pathway inhibition and differentiation rescue (markovic2023geneticsinophthalmology pages 1-2, ryl2024amycndrivendedifferentiation pages 1-2, singh2022animmaturededifferentiated pages 10-10, wang2024spatialtranscriptomicprofiling pages 5-8, chavez2023pluripotentstemcellderived pages 56-60, lisek2024histonedeacetylasesin pages 1-2).


References

1. (markovic2023geneticsinophthalmology pages 1-2): Leon Marković, Anja Bukovac, Ana Maria Varošanec, Nika Šlaus, and Nives Pećina-Šlaus. Genetics in ophthalmology: molecular blueprints of retinoblastoma. Human Genomics, Sep 2023. URL: https://doi.org/10.1186/s40246-023-00529-w, doi:10.1186/s40246-023-00529-w. This article has 41 citations and is from a peer-reviewed journal.

2. (li2022secondhitimpels pages 12-13): Yan-Ping Li, Ya-Ting Wang, Wen Wang, Xiao Zhang, Ren-Juan Shen, Kangxin Jin, Li-Wen Jin, and Zi-Bing Jin. Second hit impels oncogenesis of retinoblastoma in patient-induced pluripotent stem cell-derived retinal organoids: direct evidence for knudson's theory. PNAS Nexus, Aug 2022. URL: https://doi.org/10.1093/pnasnexus/pgac162, doi:10.1093/pnasnexus/pgac162. This article has 27 citations and is from a peer-reviewed journal.

3. (ryl2024amycndrivendedifferentiation pages 1-2): Tatsiana Ryl, Elena Afanasyeva, Till Hartmann, Melanie Schwermer, Markus Schneider, Christopher Schröder, Maren Wagemanns, Arthur Bister, Deniz Kanber, Laura Steenpass, Kathrin Schramm, Barbara Jones, David T. W. Jones, Eva Biewald, Kathy Astrahantseff, Helmut Hanenberg, Sven Rahmann, Dietmar R. Lohmann, Alexander Schramm, and Petra Ketteler. A mycn-driven de-differentiation profile identifies a subgroup of aggressive retinoblastoma. Communications Biology, Jul 2024. URL: https://doi.org/10.1038/s42003-024-06596-6, doi:10.1038/s42003-024-06596-6. This article has 10 citations and is from a peer-reviewed journal.

4. (singh2022animmaturededifferentiated pages 10-10): Hardeep P. Singh, Dominic W. H. Shayler, G. Esteban Fernandez, Matthew E. Thornton, Cheryl Mae Craft, Brendan H. Grubbs, and David Cobrinik. An immature, dedifferentiated, and lineage-deconstrained cone precursor origin of n-myc–initiated retinoblastoma. Proceedings of the National Academy of Sciences of the United States of America, Jul 2022. URL: https://doi.org/10.1073/pnas.2200721119, doi:10.1073/pnas.2200721119. This article has 29 citations and is from a highest quality peer-reviewed journal.

5. (wang2024spatialtranscriptomicprofiling pages 5-8): Luozixian Wang, Sandy Hung, Daniel Urrutia-Cabrera, Roy C. K. Kong, Sandra Staffieri, Louise E. Ludlow, Xianzhong Lau, Peng-Yuan Wang, Alex W. Hewitt, and Raymond C.B. Wong. Spatial transcriptomic profiling of human retinoblastoma. bioRxiv, Feb 2024. URL: https://doi.org/10.1101/2024.02.05.578886, doi:10.1101/2024.02.05.578886. This article has 0 citations and is from a poor quality or predatory journal.

6. (wang2024spatialtranscriptomicprofiling pages 1-5): Luozixian Wang, Sandy Hung, Daniel Urrutia-Cabrera, Roy C. K. Kong, Sandra Staffieri, Louise E. Ludlow, Xianzhong Lau, Peng-Yuan Wang, Alex W. Hewitt, and Raymond C.B. Wong. Spatial transcriptomic profiling of human retinoblastoma. bioRxiv, Feb 2024. URL: https://doi.org/10.1101/2024.02.05.578886, doi:10.1101/2024.02.05.578886. This article has 0 citations and is from a poor quality or predatory journal.

7. (lisek2024histonedeacetylasesin pages 1-2): Malwina Lisek, Julia Tomczak, Julia Swiatek, Aleksandra Kaluza, and Tomasz Boczek. Histone deacetylases in retinoblastoma. International Journal of Molecular Sciences, 25:6910, Jun 2024. URL: https://doi.org/10.3390/ijms25136910, doi:10.3390/ijms25136910. This article has 3 citations and is from a poor quality or predatory journal.

8. (chavez2023pluripotentstemcellderived pages 56-60): R Cerna Chavez. Pluripotent stem cell-derived retinal organoids and retinal pigment epithelium as a model system for screening chemotherapeutic agents in retinoblastoma. Unknown journal, 2023.