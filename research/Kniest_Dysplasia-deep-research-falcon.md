---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-02T15:45:39.743182'
end_time: '2026-04-02T16:06:13.249615'
duration_seconds: 1233.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Kniest Dysplasia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Kniest Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Kniest Dysplasia**.
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
- **Disease Name:** Kniest Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Kniest Dysplasia**.
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


## Comprehensive Pathophysiology Research Report: Kniest Dysplasia

### 0) Disease identifiers and definition
- **Disease**: Kniest dysplasia (a **type II collagenopathy**, Mendelian skeletal dysplasia). (sergouniotis2015ophthalmicandmolecular pages 1-2, niida2023streamlininggeneticdiagnosis pages 1-2)
- **MONDO**: **MONDO:0007987** (OpenTargets disease node for Kniest dysplasia). ()
- **OMIM**: **Kniest dysplasia #156550**; differential-diagnosis group includes other COL2A1-related disorders (e.g., SEDC #183900, SEMD Strudwick #184250, etc.). (sergouniotis2015ophthalmicandmolecular pages 1-2, weis1998structurallyabnormaltype pages 1-2)
- **Causal gene**: **COL2A1** (collagen type II alpha 1 chain; gene record cited as MIM #108300 in mutation-review literature). (barathouari2016mutationupdatefor pages 1-2)
- **Inheritance**: typically **autosomal dominant**, with **frequent de novo** occurrence in case series. (sergouniotis2015ophthalmicandmolecular pages 1-2)

### 1) Core pathophysiology (molecular and cellular mechanisms)
Kniest dysplasia is driven by **structural defects in type II collagen (procollagen-II)** that perturb collagen biosynthesis, folding, secretion, and extracellular matrix (ECM) assembly in cartilage and other COL2A1-expressing tissues.

#### 1.1 Primary molecular lesion: disrupted collagen II triple helix (dominant-negative)
Type II collagen’s triple helix requires a **Gly-X-Y repeating motif**. Many Kniest-causing variants are **in-frame deletions or splice-altering variants** that preserve the reading frame but **interrupt the triple helix** and produce shortened α1(II) chains that co-assemble with normal chains (dominant-negative effect).

- **Exon 12 cryptic splice donor activation**: Chen et al. (1996) showed that a C→T transition introduced a GT dinucleotide within exon 12, producing alternatively spliced COL2A1 mRNA lacking 21 nucleotides; this causes loss of residues Ala102–Lys108 and **interrupts the Gly-X-Y repeats required for helix formation**. The authors conclude: **“This study highlights the importance of dominant negative mutations of COL2A1 in producing Kniest dysplasia.”** (chen1996alternativesplicingof pages 1-2)

- **Exon 15 skipping**: Fernandes et al. (1998) identified a splice donor mutation causing an in-frame deletion (15 amino acids encoded by exon 15) in ~25% of α1(II) chains in cartilage, and concluded coassembly: **“This is best explained by the coassembly of normal and truncated α1(II) chains into heterotrimers.”** (fernandes1998incorporationofstructurally pages 1-2)

- **Exon 24 skipping**: Weis et al. (1998) described a splice donor mutation causing loss of 18 residues corresponding to exon 24. Their analysis supports incorporation of shortened chains into fibrils and a “loop-out” accommodation model for heterotrimers. (weis1998structurallyabnormaltype pages 1-2)

#### 1.2 Post-translational overmodification and defective fibrillogenesis
Abnormal chains can undergo **post-translational overmodification** (e.g., delayed folding allowing excess hydroxylation/glycosylation) and yield fibrils that are structurally abnormal.
- In exon 12-related disease, Kniest cartilage contained reduced pepsin-solubilized type II collagen with **“overmodified α1(II) chains”** with overmodifications extending to the carboxyl terminus. (chen1996alternativesplicingof pages 1-2)
- Weis et al. (1998) also inferred **post-translational overmodification** from retarded peptide mobility. (weis1998structurallyabnormaltype pages 1-2)

#### 1.3 Intracellular retention (ER storage) and organelle pathology
A recurring cellular hallmark is **intracellular retention of type II procollagen** and **dilated rough endoplasmic reticulum (rER)** in chondrocytes.
- Fernandes et al. (1998) summarizes prior ultrastructural observations: **“the chondrocytes contain pronounced dilated cisternae of the rough endoplasmic reticulum … filled with material that stains positively for type II procollagen.”** (fernandes1998incorporationofstructurally pages 1-2)
- Broader integrated evidence for COL2A1 collagenopathies indicates mutant collagen can be retained with **distended/dilated rER and Golgi** and cause sparse/abnormal ECM fibrils. (zhang2020integratedanalysisof pages 14-18)

#### 1.4 ECM-level failure: “Swiss cheese” cartilage and impaired mechanical integrity
At the tissue level, defective collagen II incorporation and fibril disorganization yields the characteristic diagnostic matrix phenotype.
- Weis et al. (1998) describes cartilage morphology termed **“Swiss cheese” cartilage**, with **sparse, thin collagen fibrils** in the perilacunar region and thickened fibrils peripherally. (weis1998structurallyabnormaltype pages 1-2)
- Fernandes et al. (1998) similarly notes a crumbly cartilage consistency and diagnostic Swiss-cheese appearance, supporting compromised mechanical strength. (fernandes1998incorporationofstructurally pages 1-2)

#### 1.5 Dysregulated pathways: ER stress / UPR is context- and mutation-dependent
Older collagenopathy literature and integrated analyses support that some mutant COL2A1 alleles can engage ER stress/UPR cascades; however, recent work suggests **some ER storage defects do not trigger canonical UPR**.
- A COL2A1 mouse model (p.Gly1170Ser) is cited as activating an **“ER stress–unfolding protein response–apoptosis cascade”** in some type II collagenopathies (referenced in integrated review). (zhang2020integratedanalysisof pages 24-26)
- **2023–2024 major mechanistic development (proteostasis nuance):** iPSC-derived human cartilage models show that mutant procollagen-II can accumulate in the ER without robust UPR activation:
  - Yammine et al. (bioRxiv preprint, Oct 2024 DOI; posted 2024) report **“ER procollagen storage defect without coupled unfolded protein response”** for Gly1170Ser in human iPSC-derived cartilage. (yammine2023erprocollagenstorage pages 1-5)
  - Yammine et al. (bioRxiv preprint, Nov 2024 DOI; posted later) show Arg719Cys causes ER distention and a defective matrix, but mutant collagen **“was not detectably recognized by the ER proteostasis network”** and fails to activate quality control responses including UPR—framed as **failed cellular surveillance**. (yammine2024humancartilagemodel pages 1-4)

### 2) Key molecular players
#### 2.1 Genes/proteins
- **COL2A1 (HGNC:2208)** is the primary causal gene. (barathouari2016mutationupdatefor pages 1-2)
- The pathogenic mechanism is typically **dominant-negative**, especially for **in-frame exon skipping/deletions** that produce mutant chains incorporated into fibrils (heterotrimers). (chen1996alternativesplicingof pages 1-2, fernandes1998incorporationofstructurally pages 1-2, weis1998structurallyabnormaltype pages 1-2)
- Recent functional work indicates mutant collagen can perturb ECM networks beyond collagen fibrils; e.g., p.Gly444Ser showed intracellular collagen-II accumulation and a **disorganized fibronectin network** in ECM assays. (marchionni2023clinicalandfunctional pages 1-2)

**Variant/statistics context (recently cited):**
- A 2016 mutation-update review reported **“Over 700 patients… harboring 415 different mutations”** in COL2A1 from LOVD plus curation. (barathouari2016mutationupdatefor pages 1-2)
- A 2023 functional paper states **“Over 600 pathogenic variants”** have been described in COL2A1. (marchionni2023clinicalandfunctional pages 1-2)
- A 2020 integrated analysis compiled **663 probands** and **460 distinct COL2A1 mutations** across 21 disorders (not Kniest-specific but provides spectrum context). (zhang2020integratedanalysisof pages 1-6)

#### 2.2 Chemical entities (metabolites/drugs/small molecules)
No disease-modifying small molecule is established for Kniest dysplasia in the retrieved evidence. Current management is largely supportive and surgical. (niida2023streamlininggeneticdiagnosis pages 1-2, yammine2024humancartilagemodel pages 1-4)
- Orthopedic end-stage interventions (joint replacement) are frequently required for severe early osteoarthritis COL2A1 phenotypes; Arg719Cys families are described as often needing multiple joint replacements. (yammine2024humancartilagemodel pages 1-4)

#### 2.3 Cell types
- **Chondrocytes (CL:0000138)** are the primary affected cell type, producing type II collagen and showing ER dilation, altered secretion, and abnormal ECM deposition. (fernandes1998incorporationofstructurally pages 1-2, zhang2020integratedanalysisof pages 14-18)

#### 2.4 Anatomical locations (tissues/organs)
Type II collagen is a major ECM component in:
- **Hyaline cartilage / growth plate cartilage** (skeletal dysplasia core). (fernandes1998incorporationofstructurally pages 1-2, weis1998structurallyabnormaltype pages 1-2)
- **Vitreous body** (ocular manifestations). (sergouniotis2015ophthalmicandmolecular pages 1-2)
- **Inner ear** (hearing impairment). (sergouniotis2015ophthalmicandmolecular pages 1-2)

### 3) Biological processes disrupted (GO-oriented)
The evidence supports disruption of:
- **Collagen fibril organization / extracellular matrix assembly** (mutant collagen incorporated into fibrils; abnormal fibril alignment and density; Swiss-cheese cartilage). (fernandes1998incorporationofstructurally pages 1-2, weis1998structurallyabnormaltype pages 1-2)
- **Protein folding and quality control in the ER** (ER storage; mutation-specific engagement or failure to engage proteostasis/UPR). (yammine2023erprocollagenstorage pages 1-5, yammine2024humancartilagemodel pages 1-4)
- **Collagen biosynthetic processing and trafficking (ER→Golgi)** (intracellular accumulation; Golgi vesicle localization in functional assays). (marchionni2023clinicalandfunctional pages 1-2)

### 4) Cellular components (where processes occur)
- **Rough endoplasmic reticulum (rER)**: pronounced dilation and storage of retained procollagen-II in chondrocytes. (fernandes1998incorporationofstructurally pages 1-2)
- **Golgi-associated vesicles/secretory pathway**: implicated in intracellular localization of collagen-II in recent functional assays. (marchionni2023clinicalandfunctional pages 1-2)
- **Extracellular space / cartilage ECM**: deposition of defective type II collagen network and disorganized fibrils. (weis1998structurallyabnormaltype pages 1-2, fernandes1998incorporationofstructurally pages 1-2)

### 5) Disease progression model (sequence of events)
1. **Heterozygous pathogenic COL2A1 variant** (often splice-altering or small in-frame deletion) produces a mutant α1(II) chain. (chen1996alternativesplicingof pages 1-2, fernandes1998incorporationofstructurally pages 1-2, weis1998structurallyabnormaltype pages 1-2)
2. **Defective triple-helix folding and/or delayed folding** leads to **overmodification** and a mixture of normal and shortened chains assembling into **heterotrimers** (dominant-negative). (chen1996alternativesplicingof pages 1-2, fernandes1998incorporationofstructurally pages 1-2, weis1998structurallyabnormaltype pages 1-2)
3. **Intracellular retention** of mutant procollagen-II causes **rER distention** (ER storage phenotype) in chondrocytes; depending on variant class, ER quality control may be activated or may fail to recognize the defect. (fernandes1998incorporationofstructurally pages 1-2, yammine2023erprocollagenstorage pages 1-5, yammine2024humancartilagemodel pages 1-4)
4. **Secretion and deposition of malformed collagen** and/or quantitative deficiency of a functional collagen network yields a **sparse, mechanically weak ECM** (“Swiss cheese” cartilage). (weis1998structurallyabnormaltype pages 1-2, fernandes1998incorporationofstructurally pages 1-2)
5. **Tissue and developmental consequences**: impaired endochondral ossification and skeletal growth; progressive joint abnormalities and secondary degenerative changes; extra-skeletal manifestations in vitreous and inner ear due to shared collagen dependence. (sergouniotis2015ophthalmicandmolecular pages 1-2, fernandes1998incorporationofstructurally pages 1-2)

### 6) Phenotypic manifestations (clinical features mapped to mechanisms)
Kniest dysplasia is multisystemic because COL2A1 is critical to cartilage and vitreous ECM.

**Skeletal**
- Disproportionate short stature / short-trunk dwarfism with kyphoscoliosis, enlarged joints and restricted mobility. (sergouniotis2015ophthalmicandmolecular pages 1-2, fernandes1998incorporationofstructurally pages 1-2)

**Ocular**
- High myopia and abnormal vitreous; high risk of retinal detachment. In an 8-person series, **6/7 tested were high myopes**, **7/7 had abnormal vitreous**, and one had bilateral retinal detachments in his twenties. (sergouniotis2015ophthalmicandmolecular pages 1-2)

**Auditory**
- Hearing impairment is common; in the same series **6/7** had significant hearing impairment. (sergouniotis2015ophthalmicandmolecular pages 1-2)

**Craniofacial / orofacial**
- Cleft palate and midface features; in the series **5/7** had clefting abnormalities. (sergouniotis2015ophthalmicandmolecular pages 1-2)

**Airway**
- Airway cartilage involvement (e.g., tracheomalacia) and neonatal respiratory compromise is reported in case-based literature, consistent with cartilage matrix fragility. (gilbertbarnes1996kniestdysplasiaradiologic pages 1-2, jhamb2019orthodontictreatmentin pages 1-2)

### 7) Recent developments and latest research (2023–2024 emphasis)
#### 7.1 Functional genomics and cell biology advances
- **COL2A1 p.Gly444Ser functional characterization (Dec 2023):** fibroblasts and in vitro chondrocyte differentiation demonstrated **intracellular collagen-II accumulation**, **Golgi vesicle localization**, and ECM network disorganization, supporting defective processing and fibril assembly. (marchionni2023clinicalandfunctional pages 1-2)
- **Human iPSC-derived cartilage models (2024 preprints):** mechanistically separate “ER storage” from canonical UPR activation and emphasize mutation-specific proteostasis engagement; these platforms are positioned for therapeutic discovery targeting collagen folding and quality control. (yammine2023erprocollagenstorage pages 1-5, yammine2024humancartilagemodel pages 1-4)

#### 7.2 Diagnostics and real-world implementation
- **Very long amplicon sequencing (vLAS; Dec 2023):** long-range PCR + short-read NGS to cover large genes like **COL2A1 (54 exons; ~31.5 kb)** as an implementable diagnostic workflow for type II collagenopathies. (niida2023streamlininggeneticdiagnosis pages 1-2)

### 8) Expert opinions / authoritative synthesis
- Mutation-update and spectrum papers emphasize that early diagnosis is critical for appropriate care and genetic counseling, and that COL2A1 mutation classes show broad phenotypic diversity. (barathouari2016mutationupdatefor pages 1-2, niida2023streamlininggeneticdiagnosis pages 1-2)
- Ophthalmology experts recommend regular ophthalmologic surveillance because ocular morbidity is substantial and resembles Stickler-like vitreoretinal risk. (sergouniotis2015ophthalmicandmolecular pages 1-2)

### 9) Statistics and data highlights (from retrieved sources)
- **Adult height expectation**: 100–140 cm (reported in Kniest dysplasia clinical context). (sergouniotis2015ophthalmicandmolecular pages 1-2)
- **Case series counts**: 8 unrelated individuals in a molecularly confirmed ophthalmology series. (sergouniotis2015ophthalmicandmolecular pages 1-2)
- **Ocular frequencies in that series**: high myopia 6/7; abnormal vitreous 7/7; retinal detachment reported in 1 case (bilateral, in 20s). (sergouniotis2015ophthalmicandmolecular pages 1-2)
- **Hearing impairment frequency**: 6/7 in the same series. (sergouniotis2015ophthalmicandmolecular pages 1-2)
- **Clefting frequency**: 5/7 in the same series. (sergouniotis2015ophthalmicandmolecular pages 1-2)
- **Variant/patient database scale**: >700 patients and 415 different COL2A1 mutations recorded in a curated LOVD-based review (2016). (barathouari2016mutationupdatefor pages 1-2)

### 10) Knowledge-base structured annotations (ontology-ready)
The following structured table provides a starter set of ontology mappings and evidence items.

| Entity type | Item | Ontology IDs | Role in disease | Key evidence | Source | PMID | URL | Context ID(s) |
|---|---|---|---|---|---|---|---|---|
| Gene/Protein | COL2A1 / Procollagen II | HGNC:2208 | Encodes the alpha-1 chain of type II procollagen; heterozygous dominant-negative mutations cause Kniest dysplasia. | Exon skipping/in-frame deletions (e.g., exons 12, 15, 24) and missense mutations disrupt the Gly-X-Y triple helix. | Weis et al., 1998, J Biol Chem; Chen et al., 1996, J Orthop Res | | https://doi.org/10.1074/jbc.273.8.4761 | (weis1998structurallyabnormaltype pages 1-2, chen1996alternativesplicingof pages 1-2) |
| Pathway/Process | Triple-helix folding & ECM assembly | GO:0032964 | Defective coassembly of normal and shortened alpha chains leads to structurally abnormal heterotrimeric collagen fibrils. | Mutant type II collagen is post-translationally overmodified, fails to stably incorporate, and mechanically disrupts the extracellular matrix. | Fernandes et al., 1998, Arch Biochem Biophys | | https://doi.org/10.1006/abbi.1998.0745 | (fernandes1998incorporationofstructurally pages 1-2) |
| Pathway/Process | ER storage / Proteostasis | GO:0034976 | Misfolded procollagen II is retained intracellularly, causing massive dilation of the rough endoplasmic reticulum. | Distended rER cisternae fill with granular material; uniquely, some retained mutant collagens fail to trigger canonical UPR, indicating failed cellular surveillance. | Yammine et al., 2024, bioRxiv; Zhang et al., 2020, Clin Genet | | https://doi.org/10.1101/2024.11.07.622468 | (zhang2020integratedanalysisof pages 14-18, yammine2024humancartilagemodel pages 1-4) |
| Cell type | Chondrocytes | CL:0000138 | Primary cartilage cells responsible for producing type II collagen; their metabolic function and survival are compromised. | Chondrocytes exhibit pronounced dilated rough ER, defective procollagen processing, and can undergo early apoptosis prior to hypertrophy. | Fernandes et al., 1998, Arch Biochem Biophys | | https://doi.org/10.1006/abbi.1998.0745 | (zhang2020integratedanalysisof pages 14-18, fernandes1998incorporationofstructurally pages 1-2) |
| Anatomy | Growth plate / Hyaline cartilage | UBERON:0001978 | Main skeletal tissue impaired, resulting in defective endochondral ossification, bone growth retardation, and enlarged joints. | Histology exhibits a diagnostic, crumbly 'Swiss cheese' matrix with vacuolar degeneration and sparse, disorganized collagen fibrils. | Weis et al., 1998, J Biol Chem; Gilbert-Barnes et al., 1996, Am J Med Genet | | https://doi.org/10.1074/jbc.273.8.4761 | (weis1998structurallyabnormaltype pages 1-2, gilbertbarnes1996kniestdysplasiaradiologic pages 1-2) |
| Anatomy | Vitreous body | UBERON:0002106 | Eye structure heavily reliant on type II collagen, leading to severe ocular phenotypes when its architecture is altered. | Abnormal vitreous architecture is observed on slit lamp examination in nearly all tested Kniest patients. | Sergouniotis et al., 2015, Eye | | https://doi.org/10.1038/eye.2014.334 | (sergouniotis2015ophthalmicandmolecular pages 1-2) |
| Anatomy | Inner ear | UBERON:0001835 | Tissue expressing type II collagen, whose disruption leads to sensorineural deafness and auditory complications. | Structural defects in the inner ear collagen network contribute to profound or significant early-onset hearing impairment. | Kaissi, 2022, J Orthop Sci Res; Sergouniotis et al., 2015, Eye | | https://doi.org/10.46889/josr.2022.3306 | (sergouniotis2015ophthalmicandmolecular pages 1-2, kaissi2022distinctiveskeletalphenotype pages 1-3) |
| Phenotype | Disproportionate short stature (Short-trunk dwarfism) | HP:0003521 | Core skeletal manifestation due to severe disruption of axial and appendicular bone elongation. | Reduced expected adult height (100-140 cm) resulting from delayed epiphyseal ossification and abnormal 'Swiss cheese' cartilage matrix. | Sergouniotis et al., 2015, Eye; Kaissi, 2022, J Orthop Sci Res | | https://doi.org/10.1038/eye.2014.334 | (sergouniotis2015ophthalmicandmolecular pages 1-2, kaissi2022distinctiveskeletalphenotype pages 3-7) |
| Phenotype | Kyphoscoliosis | HP:0002751 | Progressive spinal curvature driven by weakened vertebral cartilage and altered spine biomechanics. | Radiographs show moderate platyspondyly, characteristic coronal vertebral clefts, and severe trunk shortening from infancy. | Kaissi, 2022, J Orthop Sci Res; Weis et al., 1998, J Biol Chem | | https://doi.org/10.46889/josr.2022.3306 | (kaissi2022distinctiveskeletalphenotype pages 3-7, weis1998structurallyabnormaltype pages 1-2) |
| Phenotype | High myopia & Retinal detachment | HP:0011003, HP:0000541 | Major ocular complications arising from congenital vitreoretinal degeneration and loss of collagen integrity. | Mutant type II collagen in the vitreous causes syneresis and architectural abnormalities, drastically increasing retinal tear/detachment risk. | Sergouniotis et al., 2015, Eye | | https://doi.org/10.1038/eye.2014.334 | (sergouniotis2015ophthalmicandmolecular pages 1-2) |
| Phenotype | Hearing loss | HP:0000365 | Common sensorial defect, often sensorineural or mixed, affecting early childhood development and communication. | Present in the majority of individuals, resulting directly from structural defects in auditory tissues reliant on the type II collagen matrix. | Sergouniotis et al., 2015, Eye; Gilbert-Barnes et al., 1996, Am J Med Genet | | https://doi.org/10.1038/eye.2014.334 | (sergouniotis2015ophthalmicandmolecular pages 1-2, gilbertbarnes1996kniestdysplasiaradiologic pages 1-2) |
| Phenotype | Cleft palate | HP:0000175 | Orofacial anomaly linked to defective chondrogenesis and structural weakness in the developing midface. | Frequently observed alongside midface hypoplasia, flat face, depressed nasal bridge, and occasional tracheomalacia. | Jhamb et al., 2019, Cleft Palate Craniofac J; Sergouniotis et al., 2015, Eye | | https://doi.org/10.1177/1055665619854617 | (sergouniotis2015ophthalmicandmolecular pages 1-2, jhamb2019orthodontictreatmentin pages 1-2) |
| Diagnostic/Model | iPSC-derived human cartilage model |  | Scalable in vitro system used to study patient-specific COL2A1 mutations (e.g., p.Arg719Cys) and proteostasis mechanisms. | Recapitulates deficient collagen-II matrix and ER distention; demonstrates mutation-specific failure of UPR activation and cellular surveillance. | Yammine et al., 2024, bioRxiv | | https://doi.org/10.1101/2024.11.07.622468 | (yammine2024humancartilagemodel pages 1-4) |
| Diagnostic/Model | Long-range PCR-based NGS (vLAS) |  | Streamlined genetic sequencing approach for large, multi-exon genes like COL2A1. | Uses ~20 kb long PCR products to efficiently cover the 54 exons of COL2A1 (31.5 kb) for rapid diagnostic screening of collagenopathies. | Niida et al., 2023, Cureus | | https://doi.org/10.7759/cureus.50482 | (niida2023streamlininggeneticdiagnosis pages 1-2) |


*Table: A structured knowledge-base table mapping the molecular, cellular, and anatomical components of Kniest dysplasia to corresponding ontologies, phenotypes, and recent literature.*

### 11) Key visual evidence (figures/tables)
Weis et al. (1998) provides key primary visual evidence supporting exon-skipping and cartilage pathology:
- CB peptide gel showing α1(II)CB11 doublet (mutant + normal collagen peptides). (weis1998structurallyabnormaltype media 7bc63542)
- Histology/EM demonstrating “Swiss cheese” cartilage morphology. (weis1998structurallyabnormaltype media 52912b9b)
- RT-PCR confirming exon 24 skipping at the transcript level. (weis1998structurallyabnormaltype media b9b46098)

### 12) Evidence items list (PMID-focused; limitations)
The currently retrieved full texts and excerpts include DOIs and URLs but **often do not display PMIDs in the captured text snippets**. For completeness, PMIDs should be programmatically resolved from the DOIs for key mechanistic primary papers (e.g., Weis 1998 JBC; Fernandes 1998 Arch Biochem Biophys; Chen 1996 J Orthop Res; Sergouniotis 2015 Eye). Within this run, only PubMed IDs were explicitly returned by OpenTargets for COL2A1–Kniest evidence (e.g., 9091360; 10406661; 15895462; 7874117; 32867104), but the underlying statements from those specific PMIDs were not retrievable as full texts here. ()

---

### URLs and publication dates (selected key sources)
- Marchionni et al., **Dec 2023**, Bone Reports: https://doi.org/10.1016/j.bonr.2023.101728 (marchionni2023clinicalandfunctional pages 1-2)
- Niida et al., **Dec 13, 2023**, Cureus: https://doi.org/10.7759/cureus.50482 (niida2023streamlininggeneticdiagnosis pages 1-2)
- Yammine et al., **Oct 2024** (bioRxiv DOI), ER storage without UPR: https://doi.org/10.1101/2023.10.19.562780 (yammine2023erprocollagenstorage pages 1-5)
- Yammine et al., **Nov 2024** (bioRxiv DOI), Arg719Cys cellular surveillance failure: https://doi.org/10.1101/2024.11.07.622468 (yammine2024humancartilagemodel pages 1-4)
- Sergouniotis et al., **Jan 2015**, Eye: https://doi.org/10.1038/eye.2014.334 (sergouniotis2015ophthalmicandmolecular pages 1-2)
- Weis et al., **Feb 1998**, J Biol Chem: https://doi.org/10.1074/jbc.273.8.4761 (weis1998structurallyabnormaltype pages 1-2)
- Fernandes et al., **Jul 1998**, Arch Biochem Biophys: https://doi.org/10.1006/abbi.1998.0745 (fernandes1998incorporationofstructurally pages 1-2)
- Chen et al., **Sep 1996**, J Orthop Res: https://doi.org/10.1002/jor.1100140506 (chen1996alternativesplicingof pages 1-2)



References

1. (sergouniotis2015ophthalmicandmolecular pages 1-2): P. Sergouniotis, G. Fincham, A. McNinch, Corinne M. Spickett, A. Poulson, A. Richards, and M. Snead. Ophthalmic and molecular genetic findings in kniest dysplasia. Eye, 29:475-482, Jan 2015. URL: https://doi.org/10.1038/eye.2014.334, doi:10.1038/eye.2014.334. This article has 26 citations and is from a peer-reviewed journal.

2. (niida2023streamlininggeneticdiagnosis pages 1-2): Yo Niida, Sumihito Togi, and Hiroki Ura. Streamlining genetic diagnosis with long-range polymerase chain reaction (pcr)-based next-generation sequencing for type i and type ii collagenopathies. Cureus, Dec 2023. URL: https://doi.org/10.7759/cureus.50482, doi:10.7759/cureus.50482. This article has 3 citations.

3. (weis1998structurallyabnormaltype pages 1-2): Mary Ann Weis, Douglas J. Wilkin, Hyon J. Kim, William R. Wilcox, Ralph S. Lachman, David L. Rimoin, Daniel H. Cohn, and David R. Eyre. Structurally abnormal type ii collagen in a severe form of kniest dysplasia caused by an exon 24 skipping mutation*. The Journal of Biological Chemistry, 273:4761-4768, Feb 1998. URL: https://doi.org/10.1074/jbc.273.8.4761, doi:10.1074/jbc.273.8.4761. This article has 59 citations.

4. (barathouari2016mutationupdatefor pages 1-2): Mouna Barat-Houari, Guillaume Sarrabay, Vincent Gatinois, Aurélie Fabre, Bruno Dumont, David Genevieve, and Isabelle Touitou. Mutation update for col2a1 gene variants associated with type ii collagenopathies. Human Mutation, 37:7-15, Jan 2016. URL: https://doi.org/10.1002/humu.22915, doi:10.1002/humu.22915. This article has 171 citations and is from a domain leading peer-reviewed journal.

5. (chen1996alternativesplicingof pages 1-2): Luping Chen, Winnie Yang, and William G. Cole. Alternative splicing of exon 12 of the col2a1 gene interrupts the triple helix of type‐ii collagen in the kniest form of spondyloepiphyseal dysplasia. Journal of Orthopaedic Research, 14:712-721, Sep 1996. URL: https://doi.org/10.1002/jor.1100140506, doi:10.1002/jor.1100140506. This article has 20 citations and is from a domain leading peer-reviewed journal.

6. (fernandes1998incorporationofstructurally pages 1-2): Russell J. Fernandes, D. Wilkin, D. Wilkin, MaryAnn Weis, William R. Wilcox, William R. Wilcox, Daniel H. Cohn, Daniel H. Cohn, D. Rimoin, D. Rimoin, and D. Eyre. Incorporation of structurally defective type ii collagen into cartilage matrix in kniest chondrodysplasia. Archives of biochemistry and biophysics, 355 2:282-90, Jul 1998. URL: https://doi.org/10.1006/abbi.1998.0745, doi:10.1006/abbi.1998.0745. This article has 49 citations and is from a peer-reviewed journal.

7. (zhang2020integratedanalysisof pages 14-18): Boyan Zhang, Yue Zhang, Naichao Wu, Jianing Li, He Liu, and Jincheng Wang. Integrated analysis of <i>col2a1</i> variant data and classification of type ii collagenopathies. Clinical Genetics, 97:383-395, Dec 2020. URL: https://doi.org/10.1111/cge.13680, doi:10.1111/cge.13680. This article has 58 citations and is from a peer-reviewed journal.

8. (zhang2020integratedanalysisof pages 24-26): Boyan Zhang, Yue Zhang, Naichao Wu, Jianing Li, He Liu, and Jincheng Wang. Integrated analysis of <i>col2a1</i> variant data and classification of type ii collagenopathies. Clinical Genetics, 97:383-395, Dec 2020. URL: https://doi.org/10.1111/cge.13680, doi:10.1111/cge.13680. This article has 58 citations and is from a peer-reviewed journal.

9. (yammine2023erprocollagenstorage pages 1-5): Kathryn M. Yammine, Sophia Mirda Abularach, Seo-yeon Kim, Agata A. Bikovtseva, Jinia Lilianty, Vincent L. Butty, Richard P. Schiavoni, John F. Bateman, Shireen R. Lamandé, and Matthew D. Shoulders. Er procollagen storage defect without coupled unfolded protein response drives precocious arthritis. BioRxiv, Oct 2024. URL: https://doi.org/10.1101/2023.10.19.562780, doi:10.1101/2023.10.19.562780. This article has 5 citations.

10. (yammine2024humancartilagemodel pages 1-4): Kathryn M. Yammine, Sophia Mirda Abularach, Michael Xiong, Seo-yeon Kim, Agata A. Bikovtseva, Vincent L. Butty, Richard P. Schiavoni, John F. Bateman, Shireen R. Lamandé, and Matthew D. Shoulders. Human cartilage model of the precocious osteoarthritis-inducing<i>col2a1</i>p.arg719cys reveals pathology-driving matrix defects and a failure of the er proteostasis network to recognize the defective procollagen-ii. BioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.07.622468, doi:10.1101/2024.11.07.622468. This article has 1 citations.

11. (marchionni2023clinicalandfunctional pages 1-2): Enrica Marchionni, Maria Rosaria D'Apice, Viviana Lupo, Giovanna Lattanzi, Elisabetta Mattioli, Gina Lisignoli, Elena Gabusi, Gerardo Pepe, Manuela Helmer Citterich, Elena Campione, Anna Maria Nardone, Paola Spitalieri, Noemi Pucci, Dario Cocciadiferro, Eliseo Picchi, Francesco Garaci, Antonio Novelli, and Giuseppe Novelli. Clinical and functional characterization of col2a1 p.gly444ser variant: from a fetal phenotype to a previously undisclosed postnatal phenotype. Bone Reports, 19:101728, Dec 2023. URL: https://doi.org/10.1016/j.bonr.2023.101728, doi:10.1016/j.bonr.2023.101728. This article has 1 citations and is from a peer-reviewed journal.

12. (zhang2020integratedanalysisof pages 1-6): Boyan Zhang, Yue Zhang, Naichao Wu, Jianing Li, He Liu, and Jincheng Wang. Integrated analysis of <i>col2a1</i> variant data and classification of type ii collagenopathies. Clinical Genetics, 97:383-395, Dec 2020. URL: https://doi.org/10.1111/cge.13680, doi:10.1111/cge.13680. This article has 58 citations and is from a peer-reviewed journal.

13. (gilbertbarnes1996kniestdysplasiaradiologic pages 1-2): Enid Gilbert-Barnes, Leonard O. Langer, John M. Opitz, Renata Laxova, and Cirilo Sotelo-Arila. Kniest dysplasia: radiologic, histopathological, and scanning electronmicroscopic findings. American journal of medical genetics, 63 1:34-45, May 1996. URL: https://doi.org/10.1002/(sici)1096-8628(19960503)63:1<34::aid-ajmg9>3.0.co;2-s, doi:10.1002/(sici)1096-8628(19960503)63:1<34::aid-ajmg9>3.0.co;2-s. This article has 52 citations.

14. (jhamb2019orthodontictreatmentin pages 1-2): Tania Jhamb, Hayat Masood, Jeffrey Arigo, and P. Emile Rossouw. Orthodontic treatment in a patient with kniest dysplasia: a case study and review of literature. The Cleft Palate-Craniofacial Journal, 56:1393-1403, Jun 2019. URL: https://doi.org/10.1177/1055665619854617, doi:10.1177/1055665619854617. This article has 5 citations.

15. (kaissi2022distinctiveskeletalphenotype pages 1-3): Ali Al Kaissi. Distinctive skeletal phenotype in patients with kniest dysplasia. Journal of Orthopaedic Science and Research, pages 1-10, Dec 2022. URL: https://doi.org/10.46889/josr.2022.3306, doi:10.46889/josr.2022.3306. This article has 0 citations.

16. (kaissi2022distinctiveskeletalphenotype pages 3-7): Ali Al Kaissi. Distinctive skeletal phenotype in patients with kniest dysplasia. Journal of Orthopaedic Science and Research, pages 1-10, Dec 2022. URL: https://doi.org/10.46889/josr.2022.3306, doi:10.46889/josr.2022.3306. This article has 0 citations.

17. (weis1998structurallyabnormaltype media 7bc63542): Mary Ann Weis, Douglas J. Wilkin, Hyon J. Kim, William R. Wilcox, Ralph S. Lachman, David L. Rimoin, Daniel H. Cohn, and David R. Eyre. Structurally abnormal type ii collagen in a severe form of kniest dysplasia caused by an exon 24 skipping mutation*. The Journal of Biological Chemistry, 273:4761-4768, Feb 1998. URL: https://doi.org/10.1074/jbc.273.8.4761, doi:10.1074/jbc.273.8.4761. This article has 59 citations.

18. (weis1998structurallyabnormaltype media 52912b9b): Mary Ann Weis, Douglas J. Wilkin, Hyon J. Kim, William R. Wilcox, Ralph S. Lachman, David L. Rimoin, Daniel H. Cohn, and David R. Eyre. Structurally abnormal type ii collagen in a severe form of kniest dysplasia caused by an exon 24 skipping mutation*. The Journal of Biological Chemistry, 273:4761-4768, Feb 1998. URL: https://doi.org/10.1074/jbc.273.8.4761, doi:10.1074/jbc.273.8.4761. This article has 59 citations.

19. (weis1998structurallyabnormaltype media b9b46098): Mary Ann Weis, Douglas J. Wilkin, Hyon J. Kim, William R. Wilcox, Ralph S. Lachman, David L. Rimoin, Daniel H. Cohn, and David R. Eyre. Structurally abnormal type ii collagen in a severe form of kniest dysplasia caused by an exon 24 skipping mutation*. The Journal of Biological Chemistry, 273:4761-4768, Feb 1998. URL: https://doi.org/10.1074/jbc.273.8.4761, doi:10.1074/jbc.273.8.4761. This article has 59 citations.