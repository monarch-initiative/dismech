---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:02:03.390852'
end_time: '2025-12-15T09:10:07.320535'
duration_seconds: 483.93
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primary Ciliary Dyskinesia
  mondo_id: ''
  category: Genetic
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
- **Disease Name:** Primary Ciliary Dyskinesia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Primary Ciliary Dyskinesia**.
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
- **Disease Name:** Primary Ciliary Dyskinesia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Primary Ciliary Dyskinesia**.
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
- Objective 1 (core pathophysiology): in-progress and synthesized from 2024 Pediatrics review and 2024 ERJ multinational genotype–phenotype analysis (details below) (wee2024primaryciliarydyskinesia. pages 1-3, raidt2024analysesof1236 pages 8-10).
- Objective 2 (key molecular players): completed via curated list and embedded artifact table below (wee2024primaryciliarydyskinesia. pages 3-4, despotes2024primaryciliarydyskinesia pages 16-17, raidt2024analysesof1236 pages 8-10, a.2025primaryciliarydyskinesia pages 2-3).
- Objective 3 (GO/ontology mapping): embedded within narrative and table; processes and components mapped to ciliary motility/assembly terms (wee2024primaryciliarydyskinesia. pages 3-4, despotes2024primaryciliarydyskinesia pages 16-17).
- Objective 4 (disease progression): described linking molecular defects → mucociliary failure → infection/inflammation → bronchiectasis and systemic phenotypes (wee2024primaryciliarydyskinesia. pages 3-4, wee2024primaryciliarydyskinesia. pages 1-3).
- Objective 5 (phenotypes/cell types/anatomy/chemicals): enumerated with HPO/CL/UBERON/CHEBI-style terms and evidence (wee2024primaryciliarydyskinesia. pages 1-3, despotes2024primaryciliarydyskinesia pages 16-17, raidt2024analysesof1236 pages 8-10).
- Objective 6 (recent research 2023–2024; expert/guidelines): prioritized Pediatrics 2024, ERJ 2024, Cells 2024; included URLs and dates (wee2024primaryciliarydyskinesia. pages 1-3, raidt2024analysesof1236 pages 8-10, despotes2024primaryciliarydyskinesia pages 16-17).
- Objective 7 (artifact): created; see embedded table summarizing key genes, roles, ontology-style components/processes, and evidence.
- Objective 8/9: deliver comprehensive report below and submit.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Primary Ciliary Dyskinesia (PCD)
- MONDO ID: not confidently resolved here; will populate upon ontology verification from MONDO database.
- Category: Genetic (motile ciliopathy)

Pathophysiology description
Primary ciliary dyskinesia is a motile ciliopathy caused by mutations affecting axonemal structures (outer/inner dynein arms, radial spokes, central pair apparatus, nexin–dynein regulatory complex) or the multiciliogenesis program, resulting in abnormal or absent motile cilia and impaired mucociliary clearance; nodal motile cilia dysfunction during embryogenesis underlies laterality defects (e.g., situs inversus/ambiguus) (URL: https://doi.org/10.1542/peds.2023-063064; May 2024) (wee2024primaryciliarydyskinesia. pages 1-3). “Mutations impair axonemal dynein arms, dynein regulatory/nexin complexes, or ciliogenesis factors, producing defective or absent motile cilia and impaired mucociliary clearance” (URL: https://doi.org/10.1542/peds.2023-063064; May 2024) (wee2024primaryciliarydyskinesia. pages 3-4). Clinically, impaired clearance leads to neonatal respiratory distress, chronic wet cough, persistent rhinosinusitis/otitis media, progressive bronchiectasis, and subfertility; laterality defects reflect embryonic nodal cilia malfunction (URL: https://doi.org/10.1542/peds.2023-063064; May 2024) (wee2024primaryciliarydyskinesia. pages 1-3). No single diagnostic gold standard exists; multimodal testing with nasal nitric oxide (nNO), high-speed videomicroscopy (HSVM), transmission electron microscopy (TEM), immunofluorescence (IF), and genetics is recommended (URL: https://doi.org/10.3390/cells13110974; Jun 2024) (despotes2024primaryciliarydyskinesia pages 16-17).

Key concepts and definitions
- Motile cilium axoneme (cellular component): canonical 9+2 microtubule doublets with outer dynein arms (ODA), inner dynein arms (IDA), radial spokes (RS), central pair (CP), nexin–dynein regulatory complex (N-DRC); coordinated beating generates mucociliary transport (URL: https://doi.org/10.1542/peds.2023-063064; May 2024) (wee2024primaryciliarydyskinesia. pages 1-3).
- Multiciliogenesis (biological process): centriole amplification and motile cilia generation driven by transcriptional regulators (FOXJ1, MCIDAS) and cell cycle–linked factors (e.g., CCNO); defects cause oligocilia/aplasia (URL: https://doi.org/10.1542/peds.2023-063064; May 2024; URL: https://doi.org/10.3390/cells13110974; Jun 2024) (wee2024primaryciliarydyskinesia. pages 1-3, despotes2024primaryciliarydyskinesia pages 16-17).
- Nodal cilia: motile 9+0 cilia generating embryonic leftward flow; defects randomize L–R patterning (URL: https://doi.org/10.3390/cells13110974; Jun 2024) (despotes2024primaryciliarydyskinesia pages 1-2).

1) Core Pathophysiology
- Primary mechanisms: loss or misassembly of ODA/IDA complexes, defects of RS/CP/N‑DRC, and failure of ODA docking or dynein assembly cause abnormal waveform, reduced beat frequency, or immotility; multiciliogenesis defects cause markedly reduced cilia number (URL: https://doi.org/10.1542/peds.2023-063064; May 2024; URL: https://doi.org/10.3390/cells13110974; Jun 2024) (wee2024primaryciliarydyskinesia. pages 3-4, wee2024primaryciliarydyskinesia. pages 1-3, despotes2024primaryciliarydyskinesia pages 16-17).
- Downstream cellular consequences: impaired mucociliary clearance → mucus stasis, recurrent bacterial infection, epithelial injury, chronic neutrophilic inflammation, and progressive airway remodeling/bronchiectasis (URL: https://doi.org/10.1542/peds.2023-063064; May 2024) (wee2024primaryciliarydyskinesia. pages 3-4).
- Developmental mechanism: nodal cilia dysfunction drives laterality defects (situs inversus/ambiguus), present in a substantial subset (URL: https://doi.org/10.1542/peds.2023-063064; May 2024) (wee2024primaryciliarydyskinesia. pages 1-3).

2) Key Molecular Players (genes/proteins; ontology-ready summary)
| Gene (HGNC) | Category | Axonemal / assembly role | Key cellular component (GO-style) | Disrupted biological process (GO-style) | Representative phenotype associations | Evidence (citation, DOI/URL) |
|---|---|---|---|---|---|---|
| DNAH5 | ODA (outer dynein arm) | Major axonemal heavy chain generating motile force | Axonemal outer dynein arm | Cilium movement; axoneme function | Recurrent airway infections, bronchiectasis; laterality defects common | (raidt2024analysesof1236 pages 8-10) https://doi.org/10.1183/13993003.01769-2023 |
| DNAI1 | ODA (intermediate chain) | Structural/intermediate chain required for ODA integrity and docking | Axonemal outer dynein arm | Outer dynein arm assembly; cilium movement | Chronic wet cough, bronchiectasis; neonatal respiratory distress; situs inversus | (a.2025primaryciliarydyskinesia pages 2-3) https://doi.org/10.17615/qgfk-y329, (raidt2024analysesof1236 pages 8-10) https://doi.org/10.1183/13993003.01769-2023 |
| DNAH11 | ODA (heavy chain) | Heavy chain with functional role; often causes dyskinetic beating with near-normal TEM | Axonemal dynein arm | Ciliary beating regulation; cilium movement | Variable lung function (milder FEV1 reduction); atypical/normal TEM; respiratory symptoms | (raidt2024analysesof1236 pages 8-10) https://doi.org/10.1183/13993003.01769-2023, (wee2024primaryciliarydyskinesia. pages 3-4) https://doi.org/10.1542/peds.2023-063064 |
| CCDC39 | N-DRC / assembly scaffold | Scaffolding for inner dynein arms and nexin-dynein regulatory complex assembly | Nexin-dynein regulatory complex; inner dynein arm | Axoneme assembly; dynein arm docking | Severe early lung disease; low FEV1; neonatal distress; bronchiectasis | (raidt2024analysesof1236 pages 8-10) https://doi.org/10.1183/13993003.01769-2023, (wee2024primaryciliarydyskinesia. pages 1-3) https://doi.org/10.1542/peds.2023-063064 |
| CCDC40 | N-DRC / assembly scaffold | Partners with CCDC39 to position IDAs and N-DRC during axoneme assembly | Nexin-dynein regulatory complex; axoneme | Axoneme assembly; microtubule organization | Severe lung function decline (low FEV1); bronchiectasis; congenital heart disease association noted | (raidt2024analysesof1236 pages 8-10) https://doi.org/10.1183/13993003.01769-2023, (despotes2024primaryciliarydyskinesia pages 16-17) https://doi.org/10.3390/cells13110974 |
| RSPH1 | Radial spoke head | Radial spoke head component coordinating CP–dynein regulation | Radial spoke (axoneme) | Regulation of axonemal dynein activity; central pair organization | Central-pair related defects; typical respiratory disease; laterality less associated | (despotes2024primaryciliarydyskinesia pages 16-17) https://doi.org/10.3390/cells13110974, (raidt2024analysesof1236 pages 8-10) https://doi.org/10.1183/13993003.01769-2023 |
| RSPH4A | Radial spoke head | Radial spoke protein required for RS integrity and coordinated beating | Radial spoke (axoneme) | Regulation of ciliary beating; central pair-dependent signaling | Respiratory disease, sinusitis, possible hearing involvement reported in case series | (despotes2024primaryciliarydyskinesia pages 16-17) https://doi.org/10.3390/cells13110974, (despotes2024primaryciliarydyskinesia pages 1-2) https://doi.org/10.3390/cells13110974 |
| RSPH9 | Radial spoke head | Radial spoke head subunit impacting CP–RS interactions | Radial spoke (axoneme) | Regulation of dynein-driven motility; cilium movement | Respiratory symptoms; genotype-specific laterality patterns (less frequent) | (raidt2024analysesof1236 pages 8-10) https://doi.org/10.1183/13993003.01769-2023, (despotes2024primaryciliarydyskinesia pages 16-17) https://doi.org/10.3390/cells13110974 |
| CCNO | Ciliogenesis / multiciliogenesis | Required for centriole amplification and generation of multiple motile cilia | Basal bodies / centrioles; apical cytoplasm | Multiciliogenesis; cilium assembly | Oligocilia / reduced cilia number; severe early disease, very low FEV1 (worse prognosis) | (raidt2024analysesof1236 pages 8-10) https://doi.org/10.1183/13993003.01769-2023, (despotes2024primaryciliarydyskinesia pages 16-17) https://doi.org/10.3390/cells13110974 |
| FOXJ1 | Ciliogenesis transcription factor | Master regulator of motile ciliogenesis (transcriptional control) | Nucleus (transcription regulator controlling cilium assembly) | Regulation of cilium assembly; multiciliogenesis | Oligocilia/absent cilia phenotypes; laterality defects; autosomal-dominant presentations described | (wee2024primaryciliarydyskinesia. pages 1-3) https://doi.org/10.1542/peds.2023-063064, (a.2025primaryciliarydyskinesia pages 2-3) https://doi.org/10.17615/qgfk-y329 |
| MCIDAS | Ciliogenesis / multiciliated cell differentiation | Drives multiciliated cell differentiation and centriole biogenesis program | Nucleus; transcriptional complex controlling centriole amplification | Multiciliogenesis; centriole assembly | Reduced cilia number, neonatal distress, chronic airway disease | (despotes2024primaryciliarydyskinesia pages 16-17) https://doi.org/10.3390/cells13110974, (wee2024primaryciliarydyskinesia. pages 1-3) https://doi.org/10.1542/peds.2023-063064 |
| ODAD1 | ODA docking / assembly factor | Factor involved in ODA docking/assembly to doublet microtubules | Outer dynein arm docking complex | Outer dynein arm docking; axonemal assembly | Respiratory disease with relatively milder FEV1 impact vs severe scaffold defects | (raidt2024analysesof1236 pages 8-10) https://doi.org/10.1183/13993003.01769-2023 |


*Table: Compact ontology-ready table listing key PCD genes, their axonemal/assembly roles, affected cellular components and processes, representative phenotypes, and primary evidence (context citations with DOIs) to support integration into a knowledge base.*
Narrative notes:
- ODA heavy and intermediate chain genes (DNAH5, DNAI1) and the ODA heavy chain DNAH11 are among the most frequent PCD genotypes in international cohorts (URL: https://doi.org/10.1183/13993003.01769-2023; Jun 2024) (raidt2024analysesof1236 pages 8-10).
- IDA/N‑DRC scaffolds CCDC39 and CCDC40 are associated with severe phenotypes and lower lung function (URL: https://doi.org/10.1183/13993003.01769-2023; Jun 2024) (raidt2024analysesof1236 pages 8-10).
- Radial spoke head proteins (RSPH1, RSPH4A, RSPH9) affect CP–RS regulation and are linked to distinctive ultrastructural or functional signatures, often without laterality defects (URL: https://doi.org/10.3390/cells13110974; Jun 2024) (despotes2024primaryciliarydyskinesia pages 16-17).
- Multiciliogenesis genes (FOXJ1, MCIDAS, CCNO) yield oligocilia/immotile phenotypes; FOXJ1 can present in autosomal dominant fashion (URL: https://doi.org/10.1542/peds.2023-063064; May 2024) (wee2024primaryciliarydyskinesia. pages 1-3).
- Additional docking/assembly factors (e.g., ODAD1, CCDC103, CCDC114, ZMYND10, DRC1/CCDC164, HYDIN) contribute to dynein assembly/docking or CP integrity; defects can yield typical respiratory PCD with variable diagnostic signatures (URL: https://doi.org/10.17615/qgfk-y329; 2025) (a.2025primaryciliarydyskinesia pages 2-3).

3) Biological Processes (GO-style) disrupted
- Cilium movement; microtubule-based movement; mucociliary clearance (respiratory epithelium) (wee2024primaryciliarydyskinesia. pages 1-3).
- Axoneme assembly; dynein arm assembly (ODA/IDA); radial spoke organization; central apparatus organization; ODA docking (despotes2024primaryciliarydyskinesia pages 16-17, a.2025primaryciliarydyskinesia pages 2-3).
- Multiciliogenesis and centriole amplification; cilium morphogenesis (wee2024primaryciliarydyskinesia. pages 1-3, despotes2024primaryciliarydyskinesia pages 16-17).
- Embryonic left–right pattern specification via nodal flow (despotes2024primaryciliarydyskinesia pages 1-2).

4) Cellular Components (GO-style)
- Axoneme (9+2); outer dynein arm; inner dynein arm; radial spoke; central pair apparatus; nexin–dynein regulatory complex; outer dynein arm docking complex; basal bodies/centrioles (wee2024primaryciliarydyskinesia. pages 1-3, despotes2024primaryciliarydyskinesia pages 16-17, a.2025primaryciliarydyskinesia pages 2-3).

5) Disease Progression
- Molecular defect (axonemal structure or ciliogenesis program) → abnormal/absent ciliary beating or oligocilia → impaired mucociliary clearance → persistent sino-oto-pulmonary infections and neutrophilic inflammation → airway remodeling with bronchiectasis and progressive lung function decline; concurrent nodal cilia dysfunction in embryogenesis leads to situs inversus/ambiguus; sperm flagellar defects contribute to subfertility (URL: https://doi.org/10.1542/peds.2023-063064; May 2024) (wee2024primaryciliarydyskinesia. pages 1-3).
- Quote: “Diagnosis relies on a combination of tests… including nasal nitric oxide (nNO) measurements, high-speed videomicroscopy analysis (HSVMA), immunofluorescent staining, axonemal ultrastructure analysis via transmission electron microscopy (TEM), and genetic testing. Notably, there is no single gold standard” (Cells; Jun 2024; URL: https://doi.org/10.3390/cells13110974) (despotes2024primaryciliarydyskinesia pages 16-17).

6) Phenotypic Manifestations (HPO-style)
- Chronic wet cough, recurrent lower respiratory tract infections, bronchiectasis (HP:0002206), chronic rhinosinusitis (HP:0011107), chronic otitis media with effusion and conductive hearing loss (HP:0000407), neonatal respiratory distress (HP:0002643), laterality defects—situs inversus totalis (HP:0001696), situs ambiguus (HP:0003364), subfertility/infertility (HP:0000789) (wee2024primaryciliarydyskinesia. pages 1-3, despotes2024primaryciliarydyskinesia pages 16-17).

Genotype–phenotype correlations, statistics, and expert analyses (2023–2024 priority)
- Multinational ERJ 2024 cohort (n=1,236; 19 countries; 908 distinct pathogenic variants, 46 genes) reported: “The prevalence of laterality defects… varied widely among countries… The prevalence of laterality defects was significantly lower in PCD individuals without pathognomonic ciliary ultrastructure defects (18%). … Median FEV1 z-scores were significantly lower in CCNO (−3.26), CCDC39 (−2.49) and CCDC40 (−2.96)… milder in DNAH11 (−0.83) and ODAD1 (−0.85)” (URL: https://doi.org/10.1183/13993003.01769-2023; Jun 2024) (raidt2024analysesof1236 pages 8-10).
- Frequent genes in international datasets include DNAH5, DNAH11, CCDC40, DNAI1, CCDC39 (URL: https://doi.org/10.1183/13993003.01769-2023; Jun 2024) (raidt2024analysesof1236 pages 8-10).
- Clinical spectrum and evolving diagnostics summarized by Pediatrics 2024: “PCD is a rare, genetic disease characterized by dysfunctional motile cilia and abnormal mucociliary clearance, resulting in chronic sino-oto-pulmonary disease, neonatal respiratory distress, subfertility, and organ laterality defects” (URL: https://doi.org/10.1542/peds.2023-063064; May 2024) (wee2024primaryciliarydyskinesia. pages 1-3).

Diagnostics and real-world implementation
- nNO: ATS-endorsed adjunctive test from age ≥5 years; very low nNO is highly suggestive but normal nNO does not exclude PCD; chemiluminescence methods and threshold use are discussed in Pediatrics 2024 (URL: https://doi.org/10.1542/peds.2023-063064; May 2024) (wee2024primaryciliarydyskinesia. pages 3-4, wee2024primaryciliarydyskinesia. pages 1-3).
- HSVM: analysis of ciliary beat frequency and waveform from nasal brushings complements TEM and genetics (URL: https://doi.org/10.3390/cells13110974; Jun 2024) (despotes2024primaryciliarydyskinesia pages 16-17).
- TEM and IF: TEM detects hallmark ultrastructural class 1/2 defects in many but not all genotypes; IF for axonemal proteins (e.g., DNAH5, DNAI2) increases diagnostic sensitivity and speed (URL: https://doi.org/10.3390/cells13110974; Jun 2024; URL: https://doi.org/10.14288/1.0445067; Jan 2025) (despotes2024primaryciliarydyskinesia pages 16-17, weir2025radiantcilia pages 115-118). Quote: an immunofluorescence panel “can increase sensitivity, reduce cost and time, and will also allow for the earlier diagnosis of PCD,” though it is “insensitive to ciliogenesis defects (CCNO, MCIDAS, and FOXJ1)” (URL: https://doi.org/10.14288/1.0445067; Jan 2025) (weir2025radiantcilia pages 115-118).
- Genetics: >50 causative genes; first gene DNAI1; genetics now central to diagnosis with ~70–80% yield depending on panels and CNV detection (URL: https://doi.org/10.1542/peds.2023-063064; May 2024; URL: https://doi.org/10.3390/cells13110974; Jun 2024) (wee2024primaryciliarydyskinesia. pages 1-3, despotes2024primaryciliarydyskinesia pages 16-17).
- Real-world diagnostic performance: multimodal pathways combining HSVM, TEM, nNO, and genetics are required; in large clinical series, a substantial minority may have normal TEM; genetic and functional assays help close gaps (URL: https://doi.org/10.1007/s40291-025-00801-w; Jul 2025) (carreterovilarroig2025clinicalgeneticmorphological pages 1-2).

Recent developments and latest research (2023–2024)
- State-of-the-art overview (Pediatrics 2024) highlighting expanded phenotype spectrum, “novel diagnostics, genotype-phenotype correlations, long term morbidity, and innovative therapeutics” (URL: https://doi.org/10.1542/peds.2023-063064; May 2024) (wee2024primaryciliarydyskinesia. pages 1-3).
- ERJ 2024 multinational registry analysis (n=1,236) providing robust genotype–phenotype correlations (laterality, lung function) and regional founder variants; a key resource for precision diagnostics/prognosis (URL: https://doi.org/10.1183/13993003.01769-2023; Jun 2024) (raidt2024analysesof1236 pages 8-10).
- Clinical review (Cells 2024) consolidating structural biology, genetics (>50 genes), and multi-test diagnostics; emphasizes no gold standard and ongoing management trials (URL: https://doi.org/10.3390/cells13110974; Jun 2024) (despotes2024primaryciliarydyskinesia pages 16-17).

Current applications and models
- Patient-derived airway sampling for HSVM/TEM/IF/genetics is routine in specialized centers; early diagnosis improves outcomes (URL: https://doi.org/10.3390/cells13110974; Jun 2024; URL: https://doi.org/10.14288/1.0445067; Jan 2025) (despotes2024primaryciliarydyskinesia pages 16-17, weir2025radiantcilia pages 115-118).
- Emerging in vitro models: reviews emphasize air–liquid interface and organoid-based respiratory models to study ciliary dysfunction and test therapies; these platforms are increasingly applied across airway diseases (URL: https://doi.org/10.29057/mjmr.v12i24.12347; Jul 2024) (raidt2024analysesof1236 pages 8-10, despotes2024primaryciliarydyskinesia pages 16-17). Note: general airway model insights support PCD translational research but are not PCD-specific in the cited review (raidt2024analysesof1236 pages 8-10).

Expert opinions and guideline-aligned analysis
- Pediatrics 2024 and Cells 2024 reviews (including authors from leading PCD centers) stress a multimodal diagnostic algorithm and the heterogeneity of clinical manifestations; both advocate timely referral and comprehensive genetics to guide prognosis and research enrollment (URLs above) (wee2024primaryciliarydyskinesia. pages 1-3, despotes2024primaryciliarydyskinesia pages 16-17).
- Quote: “There is no gold standard to diagnose PCD” (Cells 2024) underscoring the need for integrated testing and expert interpretation (URL: https://doi.org/10.3390/cells13110974; Jun 2024) (despotes2024primaryciliarydyskinesia pages 16-17).

Relevant statistics and data (recent)
- 1,236 genotyped individuals; 908 variants in 46 genes; laterality overall 42%, but 18% in those without pathognomonic TEM defects (ERJ; Jun 2024) (raidt2024analysesof1236 pages 8-10).
- Lung function by genotype: CCNO, CCDC39, CCDC40 show lowest median FEV1 z-scores (−3.26, −2.49, −2.96 respectively), DNAH11 and ODAD1 comparatively milder reductions (−0.83, −0.85) (ERJ; Jun 2024) (raidt2024analysesof1236 pages 8-10).

Ontology-style annotations for knowledge base integration
- Gene/protein annotations: see embedded table for HGNC symbols and roles (raidt2024analysesof1236 pages 8-10, wee2024primaryciliarydyskinesia. pages 1-3, despotes2024primaryciliarydyskinesia pages 16-17, a.2025primaryciliarydyskinesia pages 2-3).
- Biological processes (GO-style): cilium movement; axoneme assembly; dynein arm assembly and docking; radial spoke organization; multiciliogenesis; embryonic left–right patterning (wee2024primaryciliarydyskinesia. pages 1-3, despotes2024primaryciliarydyskinesia pages 16-17, despotes2024primaryciliarydyskinesia pages 1-2).
- Cellular components (GO-style): axoneme; outer/inner dynein arm; radial spoke; central pair apparatus; nexin–dynein regulatory complex; outer dynein arm docking complex; basal body/centriole (wee2024primaryciliarydyskinesia. pages 1-3, despotes2024primaryciliarydyskinesia pages 16-17, a.2025primaryciliarydyskinesia pages 2-3).
- Cell types (CL-style): multiciliated epithelial cell of the respiratory tract; ependymal multiciliated cell; fallopian tube epithelium; spermatid/sperm flagellated cell (wee2024primaryciliarydyskinesia. pages 1-3, despotes2024primaryciliarydyskinesia pages 16-17).
- Anatomical locations (UBERON-style): nasal cavity, paranasal sinus, eustachian tube/middle ear, trachea/bronchi, lung, embryonic node, fallopian tube, ventricular ependyma (wee2024primaryciliarydyskinesia. pages 1-3, despotes2024primaryciliarydyskinesia pages 16-17).
- Phenotypes (HPO-style): neonatal respiratory distress; chronic wet cough; chronic rhinosinusitis; otitis media with hearing loss; bronchiectasis; situs inversus/ambiguus; male infertility (wee2024primaryciliarydyskinesia. pages 1-3, despotes2024primaryciliarydyskinesia pages 16-17).
- Chemical entities (CHEBI-style, examples used in management/research): nitric oxide (nNO biomarker); macrolide (azithromycin) for exacerbation reduction in RCTs cited by reviews; antibiotic/airway clearance adjuncts (despotes2024primaryciliarydyskinesia pages 16-17, wee2024primaryciliarydyskinesia. pages 1-3).

Emerging therapies and future directions
- Reviews emphasize lack of approved cilia-restorative therapies; management focuses on airway clearance, infection control, and, in some settings, macrolides to reduce exacerbations; ongoing advances in genetics and cell models aim to enable genotype-directed therapies (URL: https://doi.org/10.3390/cells13110974; Jun 2024; URL: https://doi.org/10.1542/peds.2023-063064; May 2024) (despotes2024primaryciliarydyskinesia pages 16-17, wee2024primaryciliarydyskinesia. pages 1-3).

Evidence Items (with URLs and dates)
- Wee WB et al. Primary Ciliary Dyskinesia. Pediatrics. May 2024. URL: https://doi.org/10.1542/peds.2023-063064 (wee2024primaryciliarydyskinesia. pages 1-3, wee2024primaryciliarydyskinesia. pages 3-4) (wee2024primaryciliarydyskinesia. pages 1-3, wee2024primaryciliarydyskinesia. pages 3-4).
- Raidt J et al. ERJ. Analyses of 1,236 genotyped PCD individuals… Jun 2024. URL: https://doi.org/10.1183/13993003.01769-2023 (raidt2024analysesof1236 pages 8-10).
- Despotes KA et al. Cells. Primary ciliary dyskinesia: a clinical review. Jun 2024. URL: https://doi.org/10.3390/cells13110974 (despotes2024primaryciliarydyskinesia pages 16-17, despotes2024primaryciliarydyskinesia pages 1-2).
- Zariwala MA et al. Primary Ciliary Dyskinesia (UNC Text). 2025. URL: https://doi.org/10.17615/qgfk-y329 (a.2025primaryciliarydyskinesia pages 2-3).
- Weir M. Radiant cilia: advancing North American PCD diagnosis with immunofluorescence. Jan 2025. URL: https://doi.org/10.14288/1.0445067 (weir2025radiantcilia pages 115-118).
- Carretero-Vilarroig L et al. Molecular Diagnosis & Therapy. Jul 2025. URL: https://doi.org/10.1007/s40291-025-00801-w (carreterovilarroig2025clinicalgeneticmorphological pages 1-2).

Direct supporting quotes
- “PCD is a rare, genetic disease characterized by dysfunctional motile cilia and abnormal mucociliary clearance, resulting in chronic sino-oto-pulmonary disease, neonatal respiratory distress, subfertility, and organ laterality defects” (Pediatrics 2024; URL above) (wee2024primaryciliarydyskinesia. pages 1-3).
- “There is no gold standard to diagnose PCD” (Cells 2024; URL above) (despotes2024primaryciliarydyskinesia pages 16-17).
- “The prevalence of laterality defects was significantly lower in PCD individuals without pathognomonic ciliary ultrastructure defects (18%). … Median FEV1 z-scores were significantly lower in CCNO (−3.26), CCDC39 (−2.49) and CCDC40 (−2.96)… milder in DNAH11 (−0.83) and ODAD1 (−0.85)” (ERJ 2024; URL above) (raidt2024analysesof1236 pages 8-10).

Limitations and gaps
- While airway organoid/ALI and genetic therapy concepts are promising, PCD-specific interventional data remain limited in the cited 2023–2024 sources; ongoing registries and translational platforms are expected to enable genotype-targeted trials (wee2024primaryciliarydyskinesia. pages 1-3, despotes2024primaryciliarydyskinesia pages 16-17).


References

1. (wee2024primaryciliarydyskinesia. pages 1-3): Wallace B. Wee, BreAnna Kinghorn, Stephanie D. Davis, Thomas W. Ferkol, and Adam J. Shapiro. Primary ciliary dyskinesia. Pediatrics, May 2024. URL: https://doi.org/10.1542/peds.2023-063064, doi:10.1542/peds.2023-063064. This article has 27 citations and is from a highest quality peer-reviewed journal.

2. (raidt2024analysesof1236 pages 8-10): Johanna Raidt, Sarah Riepenhausen, Petra Pennekamp, Heike Olbrich, Israel Amirav, Rodrigo A. Athanazio, Micha Aviram, Juan E. Balinotti, Ophir Bar-On, Sebastian F.N. Bode, Mieke Boon, Melissa Borrelli, Siobhan B. Carr, Suzanne Crowley, Eleonora Dehlink, Sandra Diepenhorst, Peter Durdik, Bernd Dworniczak, Nagehan Emiralioğlu, Ela Erdem, Rossella Fonnesu, Serena Gracci, Jörg Große-Onnebrink, Karolina Gwozdziewicz, Eric G. Haarman, Christine R. Hansen, Claire Hogg, Mathias G. Holgersen, Eitan Kerem, Robert W. Körner, Karsten Kötz, Panayiotis Kouis, Michael R. Loebinger, Natalie Lorent, Jane S. Lucas, Debora Maj, Marcus A. Mall, June K. Marthin, Vendula Martinu, Henryk Mazurek, Hannah M. Mitchison, Tabea Nöthe-Menchen, Ugur Özçelik, Massimo Pifferi, Andrzej Pogorzelski, Felix C. Ringshausen, Jobst F. Roehmel, Sandra Rovira-Amigo, Nisreen Rumman, Anne Schlegtendal, Amelia Shoemark, Synne Sperstad Kennelly, Ben O. Staar, Sivagurunathan Sutharsan, Simon Thomas, Nicola Ullmann, Julian Varghese, Sandra von Hardenberg, Woolf T. Walker, Martin Wetzke, Michal Witt, Panayiotis Yiallouros, Anna Zschocke, Ewa Ziętkiewicz, Kim G. Nielsen, and Heymut Omran. Analyses of 1236 genotyped primary ciliary dyskinesia individuals identify regional clusters of distinct dna variants and significant genotype–phenotype correlations. European Respiratory Journal, 64:2301769, Jun 2024. URL: https://doi.org/10.1183/13993003.01769-2023, doi:10.1183/13993003.01769-2023. This article has 51 citations and is from a highest quality peer-reviewed journal.

3. (wee2024primaryciliarydyskinesia. pages 3-4): Wallace B. Wee, BreAnna Kinghorn, Stephanie D. Davis, Thomas W. Ferkol, and Adam J. Shapiro. Primary ciliary dyskinesia. Pediatrics, May 2024. URL: https://doi.org/10.1542/peds.2023-063064, doi:10.1542/peds.2023-063064. This article has 27 citations and is from a highest quality peer-reviewed journal.

4. (despotes2024primaryciliarydyskinesia pages 16-17): Katherine A. Despotes, Maimoona A. Zariwala, Stephanie D. Davis, and Thomas W. Ferkol. Primary ciliary dyskinesia: a clinical review. Cells, 13:974, Jun 2024. URL: https://doi.org/10.3390/cells13110974, doi:10.3390/cells13110974. This article has 64 citations and is from a poor quality or predatory journal.

5. (a.2025primaryciliarydyskinesia pages 2-3): Maimoona A. Zariwala, Peadar G. Noone, and Jason Lobo. Primary ciliary dyskinesia. Text, 2025. URL: https://doi.org/10.17615/qgfk-y329, doi:10.17615/qgfk-y329. This article has 243 citations and is from a peer-reviewed journal.

6. (despotes2024primaryciliarydyskinesia pages 1-2): Katherine A. Despotes, Maimoona A. Zariwala, Stephanie D. Davis, and Thomas W. Ferkol. Primary ciliary dyskinesia: a clinical review. Cells, 13:974, Jun 2024. URL: https://doi.org/10.3390/cells13110974, doi:10.3390/cells13110974. This article has 64 citations and is from a poor quality or predatory journal.

7. (weir2025radiantcilia pages 115-118): Madison Weir. Radiant cilia : advancing north american pcd diagnosis with immunofluorescence. Text, Jan 2025. URL: https://doi.org/10.14288/1.0445067, doi:10.14288/1.0445067. This article has 0 citations and is from a peer-reviewed journal.

8. (carreterovilarroig2025clinicalgeneticmorphological pages 1-2): Lidón Carretero-Vilarroig, Rosana Blanco-Máñez, Noelia Muñoz-Fernández, Isabel Ibáñez, Alba Berzal-Serrano, Ana Reula, Belén García-Bohórquez, Elena Aller, Gema García-García, Jose M. Millán, Miguel Armengot-Carceller, and Teresa Jaijo. Clinical, genetic, morphological and functional correlations in a large series of patients with primary ciliary dyskinesia: a heterogeneous disease with a controversial diagnosis. Molecular diagnosis & therapy, Jul 2025. URL: https://doi.org/10.1007/s40291-025-00801-w, doi:10.1007/s40291-025-00801-w. This article has 0 citations and is from a peer-reviewed journal.