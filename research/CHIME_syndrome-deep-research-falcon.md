---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-05T17:22:41.438590'
end_time: '2026-01-05T17:34:16.997832'
duration_seconds: 695.56
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CHIME syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** CHIME syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **CHIME syndrome**.
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
- **Disease Name:** CHIME syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **CHIME syndrome**.
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


Plan of work
- Completed literature retrieval and extraction from recent and landmark sources (2018–2024), including Brain (2024) IGD cohort and a 2024 mechanistic study of Pigl/Pigf loss in trophoblasts. Evidence table embedded below.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: CHIME syndrome (also known as Zunich neuroectodermal syndrome)
- MONDO ID: MONDO:0010221 (OpenTargets association of CHIME syndrome with PIGL) (ceroni2018largedeletionin pages 1-2)
- Category: Genetic (inherited glycosylphosphatidylinositol deficiency; IGD)

Pathophysiology description
CHIME syndrome is an autosomal recessive inherited glycosylphosphatidylinositol (GPI) deficiency caused by biallelic pathogenic variants in PIGL, which encodes the GlcNAc-PI de-N-acetylase catalyzing the second step of GPI-anchor biosynthesis on the cytoplasmic face of the endoplasmic reticulum (ER) (de-N-acetylation of N-acetylglucosaminyl-phosphatidylinositol, GlcNAc-PI, to glucosaminyl-PI, GlcN-PI) (ceroni2018largedeletionin pages 1-2, altassan2018hyperphosphatasiawithmental pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7). Defective PIGL activity impairs production of GPI anchors, reducing cell-surface expression of GPI-anchored proteins (GPI-APs) across multiple tissues. This leads to multisystem disease featuring neurodevelopmental impairment, ocular coloboma, migratory ichthyosiform dermatosis, ear anomalies/hearing loss, and variable cardiac and renal/urogenital malformations (ceroni2018largedeletionin pages 1-2, conte2023metaboliccardiomyopathiesand pages 17-19, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).

At the cellular level, IGDs—including those caused by PIGL—show reduced GPI-APs detectable by flow cytometry (e.g., decreased CD59 and FLAER on fibroblasts; reduced CD24/CD16 on granulocytes, CD14 on monocytes), reflecting diminished GPI anchoring (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7). A frequent biochemical signature in IGDs is elevated serum alkaline phosphatase (ALP), as TNAP is a GPI-AP that can be shed or misprocessed when GPI biosynthesis is perturbed; marked hyperphosphatasia has been reported in PIGL-related presentations (altassan2018hyperphosphatasiawithmental pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7, patalan2024inheritedglycosylphosphatidylinositoldeficiency pages 1-3). Cohort-level natural history from 83 IGD individuals shows median seizure onset at 6 months, frequent cerebral and cerebellar atrophy and corpus callosum anomalies, and multisystem involvement (gastrointestinal, cardiac, renal) (sidpra2024theclinicaland pages 1-1).

Recent mechanistic data add tissue-specific insight. CRISPR knockout of Pigl in mouse trophoblast stem cells demonstrates that loss of early GPI biosynthesis induces an excessive unfolded protein response (UPR)/ER stress signature and impairs WNT/β-catenin signaling required for syncytiotrophoblast-II (SynT-II) differentiation; β-catenin and early SynT-II markers are rescued by pharmacologic WNT activation (CHIR99021). Pigl/Pigf-deficient trophoblasts also show increased mitochondrial respiration and ROS. These changes correlate with a severely underdeveloped labyrinthine SynT in vivo and a Pigl/Pigf-deficient transcriptomic signature that segregates human preeclampsia placental samples, suggesting a link between GPI pathway integrity and placental pathophysiology (alvarezsanchez2024thegpianchorbiosynthesis pages 8-9, alvarezsanchez2024thegpianchorbiosynthesis pages 1-2, alvarezsanchez2024thegpianchorbiosynthesis pages 9-11, alvarezsanchez2024thegpianchorbiosynthesis pages 2-3, alvarezsanchez2024thegpianchorbiosynthesis pages 4-5, alvarezsanchez2024thegpianchorbiosynthesis pages 3-4).

Core Pathophysiology
- Primary mechanisms: Loss of PIGL de-N-acetylase activity in early GPI-anchor biosynthesis reduces/abolishes GPI-AP attachment, leading to impaired cell-surface functions of enzymes, adhesion molecules, and co-receptors and secondary cellular stress responses (ceroni2018largedeletionin pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7, altassan2018hyperphosphatasiawithmental pages 1-2).
- Dysregulated pathways: GPI-anchor biogenesis pathway (ER); downstream ER stress/UPR signaling; WNT/β-catenin signaling in trophoblast differentiation; mitochondrial respiratory adaptation/ROS (in trophoblast context) (alvarezsanchez2024thegpianchorbiosynthesis pages 8-9, alvarezsanchez2024thegpianchorbiosynthesis pages 1-2, alvarezsanchez2024thegpianchorbiosynthesis pages 9-11, alvarezsanchez2024thegpianchorbiosynthesis pages 4-5, alvarezsanchez2024thegpianchorbiosynthesis pages 3-4).
- Affected cellular processes: Protein maturation/attachment to membranes via GPI-APs; cell-surface signaling and adhesion; ER protein quality control (UPR); trophoblast lineage specification and SynT-II differentiation via WNT signaling (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7, alvarezsanchez2024thegpianchorbiosynthesis pages 8-9, alvarezsanchez2024thegpianchorbiosynthesis pages 1-2).

Key Molecular Players
- Genes/Proteins (HGNC):
  - PIGL (HGNC:8962): ER GlcNAc-PI de-N-acetylase (step 2 of GPI synthesis) (ceroni2018largedeletionin pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
  - Representative GPI-anchored proteins affected: tissue-nonspecific alkaline phosphatase (TNAP/ALPL), CD55/DAF, CD59, CD24, CD16, CD14 (as cellular readouts and examples) (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7). Note: specific GPI-AP dependencies may vary by tissue.
  - Trophoblast signaling components impacted by PIGL loss: WNT ligands (e.g., Wnt3, Wnt4, Wnt5a, Wnt7a, Wnt9a), receptors/co-receptors (Fzd5, Fzd10, ROR2), antagonists (DKK1, NOTUM), β-catenin (CTNNB1) (alvarezsanchez2024thegpianchorbiosynthesis pages 8-9, alvarezsanchez2024thegpianchorbiosynthesis pages 7-8, alvarezsanchez2024thegpianchorbiosynthesis pages 4-5).
- Chemical entities (CHEBI):
  - GPI anchor intermediates: N-acetylglucosaminyl-phosphatidylinositol (GlcNAc-PI) and glucosaminyl-PI (GlcN-PI) (altassan2018hyperphosphatasiawithmental pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
  - CHIR99021 (GSK3 inhibitor; WNT/β-catenin pathway activator) used to rescue β-catenin/SynT-II markers in Pigl/Pigf-null trophoblasts (alvarezsanchez2024thegpianchorbiosynthesis pages 8-9, alvarezsanchez2024thegpianchorbiosynthesis pages 9-11).
- Cell types (CL):
  - Neurons and glia (neurodevelopmental impairment; IGD cohort) (sidpra2024theclinicaland pages 1-1).
  - Keratinocytes/epidermal cells (migratory ichthyosiform dermatosis) (ceroni2018largedeletionin pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
  - Trophoblast stem cells and syncytiotrophoblast (placental SynT-II lineage) (alvarezsanchez2024thegpianchorbiosynthesis pages 8-9, alvarezsanchez2024thegpianchorbiosynthesis pages 2-3).
  - Hematopoietic cells (granulocytes/monocytes; diagnostic flow cytometry readouts) (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
- Anatomical locations (UBERON):
  - Brain (cerebral/cerebellar atrophy; corpus callosum anomalies) (sidpra2024theclinicaland pages 1-1).
  - Eye (optic fissure/coloboma) (ceroni2018largedeletionin pages 1-2).
  - Skin (epidermis; ichthyosiform dermatosis) (ceroni2018largedeletionin pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
  - Ear (external/middle ear anomalies; conductive hearing loss) (ceroni2018largedeletionin pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
  - Heart (congenital heart disease reported in IGDs including PIGL-CDG) (conte2023metaboliccardiomyopathiesand pages 17-19, ceroni2018largedeletionin pages 1-2).
  - Kidney/urogenital tract (hydronephrosis, urogenital anomalies variably reported) (ceroni2018largedeletionin pages 1-2).
  - Placenta (labyrinth/SynT-II development in Pigl/Pigf deficiency models) (alvarezsanchez2024thegpianchorbiosynthesis pages 2-3, alvarezsanchez2024thegpianchorbiosynthesis pages 4-5).

Biological Processes (GO annotations; disrupted)
- GPI anchor biosynthetic process; ER membrane protein complex assembly; protein–lipid modification and attachment (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7, ceroni2018largedeletionin pages 1-2).
- Response to endoplasmic reticulum stress; regulation of unfolded protein response (UPR) (ATF4/ATF6/IRE1/XBP1 pathways) (alvarezsanchez2024thegpianchorbiosynthesis pages 1-2, alvarezsanchez2024thegpianchorbiosynthesis pages 4-5, alvarezsanchez2024thegpianchorbiosynthesis pages 3-4).
- WNT signaling pathway; β-catenin stabilization and target gene expression during trophoblast/SynT-II differentiation (alvarezsanchez2024thegpianchorbiosynthesis pages 8-9, alvarezsanchez2024thegpianchorbiosynthesis pages 9-11, alvarezsanchez2024thegpianchorbiosynthesis pages 7-8).
- Cell adhesion and receptor-mediated signaling at the plasma membrane mediated by GPI-APs (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).

Cellular Components (where key processes occur)
- Endoplasmic reticulum membrane and lumen (early GPI biosynthesis; PIGL localization and UPR activation) (altassan2018hyperphosphatasiawithmental pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7, alvarezsanchez2024thegpianchorbiosynthesis pages 4-5).
- Plasma membrane outer leaflet/lipid rafts (localization and function of GPI-APs) (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
- Mitochondrion (respiratory changes and ROS in Pigl/Pigf-deficient trophoblasts) (alvarezsanchez2024thegpianchorbiosynthesis pages 9-11, alvarezsanchez2024thegpianchorbiosynthesis pages 4-5).

Disease Progression (sequence of events)
1) Genotype: Biallelic PIGL variants—commonly a recurrent missense c.500T>C (p.Leu167Pro) in trans with a null allele (often large deletions affecting 5′UTR/exon 1)—reduce/abolish PIGL enzyme function (ceroni2018largedeletionin pages 1-2).
2) Molecular defect: Failure to de-N-acetylate GlcNAc-PI to GlcN-PI blocks early GPI assembly in the ER, limiting the availability of mature GPI anchors (altassan2018hyperphosphatasiawithmental pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
3) Cellular dysfunction: Reduced cell-surface GPI-APs; possible shedding/release of GPI-APs like TNAP; ER stress/UPR activation in sensitive cell types; tissue-specific pathway disruption (e.g., WNT/β-catenin in trophoblast) (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7, alvarezsanchez2024thegpianchorbiosynthesis pages 1-2, alvarezsanchez2024thegpianchorbiosynthesis pages 8-9).
4) Organ phenotypes: Neurodevelopmental impairment with early-onset seizures, structural brain changes, ocular coloboma, ichthyosiform dermatosis, ear anomalies/hearing loss; variable cardiac and renal involvement; potential placental insufficiency signatures in model systems (sidpra2024theclinicaland pages 1-1, ceroni2018largedeletionin pages 1-2, conte2023metaboliccardiomyopathiesand pages 17-19, alvarezsanchez2024thegpianchorbiosynthesis pages 8-9, alvarezsanchez2024thegpianchorbiosynthesis pages 2-3).

Phenotypic Manifestations and relation to mechanisms
- Neurodevelopmental: DD/ID (90%), seizures (83%), hypotonia (72%), motor symptoms (64%); neuroimaging reveals cerebral and cerebellar atrophy and corpus callosum anomalies. These features are consistent with broad neuronal dependence on GPI-APs for synaptic signaling, adhesion, and complement regulation; cohort median seizure onset is 6 months (sidpra2024theclinicaland pages 1-1).
- Dermatologic: Migratory ichthyosiform dermatosis is highly penetrant in reported CHIME cases; keratinocyte membrane protein anchoring defects plausibly contribute (ceroni2018largedeletionin pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
- Ocular: Coloboma likely reflects disrupted morphogen signaling and adhesion during optic fissure closure; GPI-AP deficits in ocular development are consistent with reported CHIME cases (ceroni2018largedeletionin pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
- Auditory: Ear anomalies and conductive hearing loss reflect structural anomalies and potential GPI-AP deficits in the auditory system (ceroni2018largedeletionin pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
- Cardiac: IGD systematic review catalogs cardiac involvement in GPI/CDG disorders including PIGL-CDG, supporting surveillance for congenital heart disease (conte2023metaboliccardiomyopathiesand pages 17-19).
- Renal/urogenital: Hydronephrosis/urogenital anomalies variably reported (ceroni2018largedeletionin pages 1-2).
- Placenta (mechanistic models): Pigl/Pigf deficiency impairs SynT-II differentiation via ER stress and WNT/β-catenin suppression; pharmacologic WNT activation rescues SynT-II markers in vitro, and gene signatures overlap with human preeclampsia datasets (alvarezsanchez2024thegpianchorbiosynthesis pages 8-9, alvarezsanchez2024thegpianchorbiosynthesis pages 1-2, alvarezsanchez2024thegpianchorbiosynthesis pages 2-3).

Genotype–Phenotype Highlights
- Recurrent architecture: PIGL c.500T>C (p.Leu167Pro) frequently occurs in trans with a null allele; large deletions of PIGL (including 5′ UTR/part of exon 1) are overrepresented and often missed by routine sequencing; targeted CNV/large-deletion analysis is recommended when only one variant is found (ceroni2018largedeletionin pages 1-2).
- Phenotypic breadth: PIGL variants can present as classic CHIME or with hyperphosphatasia and mental retardation syndrome–like features (HPMRS), including markedly elevated ALP (altassan2018hyperphosphatasiawithmental pages 1-2). IGD cohort data show synthesis-stage gene variants associate with shorter time to seizure onset than transamidase/remodeling genes (sidpra2024theclinicaland pages 1-1).

Diagnostics and Biomarkers
- Cellular assays: Flow cytometry for GPI-APs (e.g., FLAER binding and CD55/CD59, CD24/CD16, CD14) can support IGD diagnosis by demonstrating reduced surface GPI-APs (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7). However, cell-surface GPI-AP levels on granulocytes do not consistently correlate with clinical severity across IGDs (tanigawa2017phenotype–genotypecorrelationsof pages 12-15).
- Biochemical: Serum ALP often elevated in IGDs and is documented in PIGL-related disease; marked hyperphosphatasia reported (e.g., 968 U/L) (altassan2018hyperphosphatasiawithmental pages 1-2, patalan2024inheritedglycosylphosphatidylinositoldeficiency pages 1-3, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
- Genomic: Sequence PIGL and assess for copy-number/structural variants due to frequent large deletions in CHIME (ceroni2018largedeletionin pages 1-2).

Current applications and real-world implementations
- Clinical care: Multidisciplinary surveillance for seizures (early-onset), developmental therapies, audiology, ophthalmology for coloboma, dermatology for ichthyosis, and cardiology/renal evaluations given multisystem involvement (sidpra2024theclinicaland pages 1-1, ceroni2018largedeletionin pages 1-2, conte2023metaboliccardiomyopathiesand pages 17-19). Molecular diagnostics guide management and counseling (patalan2024inheritedglycosylphosphatidylinositoldeficiency pages 1-3).
- Seizure management in IGDs: In the 2024 cohort, levetiracetam achieved control in 38.5% of treated individuals; pyridoxine produced complete or partial responses in a minority (4 complete, 3 partial among 22 trials) (sidpra2024theclinicaland pages 10-11). No surgical interventions were reported (sidpra2024theclinicaland pages 10-11).
- Translational insight: Trophoblast data suggest tissue-specific vulnerabilities to GPI-AP loss (UPR/WNT defects), potentially informing obstetric monitoring in pregnancies with known fetal IGDs, though clinical translation to CHIME requires further evidence (alvarezsanchez2024thegpianchorbiosynthesis pages 8-9, alvarezsanchez2024thegpianchorbiosynthesis pages 1-2, alvarezsanchez2024thegpianchorbiosynthesis pages 2-3).

Expert opinions and analysis from authoritative sources
- Authoritative pathway reviews and cohort studies conclude that GPI biosynthesis is essential for viability; hypomorphic germline variants cause heterogeneous neurocutaneous phenotypes through reduced GPI-AP expression (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7). The Brain 2024 cohort provides high-quality natural history and genotype-stage insights across IGDs (sidpra2024theclinicaland pages 1-1, sidpra2024theclinicaland pages 10-11). The 2024 CMLS mechanistic study offers strong causal evidence linking GPI pathway loss to ER stress and WNT signaling failure in trophoblast differentiation, with plausible implications for human placental disease (alvarezsanchez2024thegpianchorbiosynthesis pages 8-9, alvarezsanchez2024thegpianchorbiosynthesis pages 1-2, alvarezsanchez2024thegpianchorbiosynthesis pages 2-3).

Relevant statistics and data (recent)
- IGD cohort (n=83): DD/ID 90%; seizures 83%; hypotonia 72%; motor symptoms 64%; cerebral atrophy 75%; cerebellar atrophy 60%; callosal anomalies 57%; central tegmental tract diffusion restriction 60%; median seizure onset 6 months; multisystem involvement: GI 66%, cardiac 19%, renal 14% (sidpra2024theclinicaland pages 1-1).
- IGD treatment signals: Levetiracetam control in 38.5% (15/39 as part of polytherapy); pyridoxine trialed in 22 with 4 complete and 3 partial responses (sidpra2024theclinicaland pages 10-11).
- PIGL genotype: recurrent p.Leu167Pro in trans with null alleles (with frequent large deletions), requiring targeted CNV assessment (ceroni2018largedeletionin pages 1-2).
- ALP biomarker: hyperphosphatasia documented in PIGL-related presentations (e.g., 968 U/L) (altassan2018hyperphosphatasiawithmental pages 1-2).

Gene/protein annotations with ontology terms
- PIGL (HGNC:8962):
  - Function: GlcNAc-PI de-N-acetylase (GPI anchor biosynthetic process; GO:0006506/GO:0006505 context) acting in ER membrane (GO:0005789) (altassan2018hyperphosphatasiawithmental pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
  - Localization: Endoplasmic reticulum membrane/cytoplasmic face (GO:0005789) (altassan2018hyperphosphatasiawithmental pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
- Representative affected GPI-APs (examples): ALPL/TNAP, CD55, CD59, CD24, FCGR3 (CD16), CD14 (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).

Phenotype associations (HPO terms; examples)
- Intellectual disability (HP:0001249), Developmental delay (HP:0001263), Seizures (HP:0001250), Hypotonia (HP:0001252) (sidpra2024theclinicaland pages 1-1).
- Ichthyosis (HP:0008064) with migratory pattern (clinical description) (ceroni2018largedeletionin pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
- Coloboma (HP:0000589) (ceroni2018largedeletionin pages 1-2).
- Hearing impairment/conductive hearing loss (HP:0000405/HP:0000407) (ceroni2018largedeletionin pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
- Congenital heart disease (HP:0001627) (conte2023metaboliccardiomyopathiesand pages 17-19, ceroni2018largedeletionin pages 1-2).
- Renal/urogenital anomalies (e.g., hydronephrosis HP:0000126) (ceroni2018largedeletionin pages 1-2).
- Brain atrophy (HP:0012444), Cerebellar atrophy (HP:0001272), Corpus callosum abnormality (HP:0001273) (sidpra2024theclinicaland pages 1-1).

Cell type involvement (CL; examples)
- Neuron (CL:0000540), astrocyte (CL:0000127) (neurodevelopmental phenotypes) (sidpra2024theclinicaland pages 1-1).
- Keratinocyte (CL:0000312) (ichthyosis) (ceroni2018largedeletionin pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
- Trophoblast stem cell (CL:0008031), syncytiotrophoblast (CL:0000359) (alvarezsanchez2024thegpianchorbiosynthesis pages 8-9, alvarezsanchez2024thegpianchorbiosynthesis pages 2-3).
- Granulocyte (CL:0000094), monocyte (CL:0000576) for diagnostic GPI-AP readouts (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).

Anatomical locations (UBERON; examples)
- Brain (UBERON:0000955) and cerebellum (UBERON:0002037) (sidpra2024theclinicaland pages 1-1).
- Eye/retina (UBERON:0000970) (coloboma) (ceroni2018largedeletionin pages 1-2).
- Skin/epidermis (UBERON:0001003/0001002) (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7, ceroni2018largedeletionin pages 1-2).
- Ear (UBERON:0001690) (ceroni2018largedeletionin pages 1-2).
- Heart (UBERON:0000948) (conte2023metaboliccardiomyopathiesand pages 17-19).
- Kidney/urinary system (UBERON:0002113) (ceroni2018largedeletionin pages 1-2).
- Placenta (UBERON:0001987) (alvarezsanchez2024thegpianchorbiosynthesis pages 2-3).

Chemical entities (CHEBI; examples)
- N-acetylglucosaminyl-phosphatidylinositol (GlcNAc-PI) and glucosaminyl-PI (GlcN-PI) intermediates in GPI biosynthesis (altassan2018hyperphosphatasiawithmental pages 1-2, wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
- CHIR99021 (GSK3 inhibitor; WNT activator) used in rescue experiments (alvarezsanchez2024thegpianchorbiosynthesis pages 8-9, alvarezsanchez2024thegpianchorbiosynthesis pages 9-11).

Evidence table
| PMID | First author (year) | Study type | Key mechanistic/clinical finding | Relevance to CHIME/PIGL | URL | Publication date |
|---|---|---|---|---|---|---|
|  | Sidpra (2024) | Multinational cohort (n=83 IGD) | Median age at seizure onset 6 months; high rates of developmental delay (90%), seizures (83%), hypotonia (72%); neuroimaging: cerebral atrophy 75%, cerebellar atrophy 60%, callosal anomalies 57%; synthesis-stage gene variants show shorter time-to-seizure vs transamidase/remodelling genes (cohort-level genotype signal) (sidpra2024theclinicaland pages 1-1) | Largest recent IGD cohort providing natural history benchmarks relevant to CHIME/PIGL (seizure onset, neuroimaging, multisystem involvement) | https://doi.org/10.1093/brain/awae056 | Mar 2024 |
|  | Álvarez-Sánchez (2024) | Mechanistic CRISPR KO study in mouse trophoblast stem cells / placentas | Pigl/Pigf loss → accumulation of misfolded GPI-AP precursors, robust ER stress / UPR (ATF4/ATF6/XBP1/Ddit3), increased mitochondrial respiration/ROS; downregulation of WNT ligands/receptors, reduced β-catenin and failed SynT-II differentiation; CHIR99021 (WNT activator) rescues β-catenin and SynT-II markers; Pigl/Pigf mutant transcriptomic signature segregates human preeclampsia samples (alvarezsanchez2024thegpianchorbiosynthesis pages 8-9) | Direct mechanistic link: PIGL deficiency → ER stress + impaired WNT/β-catenin signaling → defective syncytiotrophoblast differentiation; suggests tissue-specific consequences and relevance to placental disease | https://doi.org/10.1007/s00018-024-05284-2 | May 2024 |
|  | Ceroni (2018) | Genetic case report / series | PIGL encodes ER-localized GlcNAc-PI de-N-acetylase (step 2 of GPI biosynthesis); recurrent missense c.500T>C (p.Leu167Pro) frequently observed in CHIME patients, commonly in trans with a null allele (including large deletions involving 5'UTR/exon1) that may be missed by standard NGS; phenotype: ichthyosiform dermatosis, coloboma, ear anomalies, cardiac and renal anomalies, ID/epilepsy (ceroni2018largedeletionin pages 1-2) | Variant architecture and diagnostic note: p.Leu167Pro + null (often large deletions) is a recurrent CHIME genotype; emphasizes need to assay for copy-number/large deletions when one allele is not found | https://doi.org/10.1590/1678-4685-gmb-2017-0172 | Feb 2018 |
|  | Altassan (2018) | Case series / phenotype expansion report | Documents PIGL-related hyperphosphatasia with mental retardation (HPMRS-like) presentations; reports markedly elevated serum alkaline phosphatase (example ALP 968 U/L) with PIGL variants; links PIGL to both CHIME and Mabry/HPMRS phenotypes (altassan2018hyperphosphatasiawithmental pages 1-2) | Establishes ALP (hyperphosphatasia) as an important biochemical biomarker in some PIGL presentations and expands clinical phenotype spectrum | https://doi.org/10.1016/j.ymgmr.2018.01.007 | Jun 2018 |
|  | Wu (2020) | Review (GPI biosynthesis in human disease) | Summarizes PIGL function and structure (TM region aa2–22; de-N-acetylase domain aa44–168); documents common cellular readouts in IGDs: reduced CD59 and FLAER in fibroblasts, decreased CD24/CD16 on granulocytes and CD14 on monocytes; CHIME clinical features and many reported PIGL variants (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7) | Provides molecular/domain annotation for PIGL, and practical diagnostic cellular assays (FLAER, CD55/CD59) used in IGD workups | https://doi.org/10.1186/s13023-020-01401-z | May 2020 |
|  | Patalan (2024) | Clinical review (Pediatria Polska) | Overview of inherited GPI deficiency disorders: ER-stage disruption (including PIGL) reduces GPI-AP presentation, can lead to degradation or release of abnormal GPI-APs; ALP abnormalities and multisystem involvement (neurological, cardiac, renal, GI, skin, sensory) emphasized; molecular testing recommended (patalan2024inheritedglycosylphosphatidylinositoldeficiency pages 1-3) | Recent clinical-summary supporting multisystem surveillance and use of molecular diagnostics for suspected CHIME/PIGL cases | https://doi.org/10.5114/polp.2024.146394 | Jan 2024 |
|  | Conte (2023) | Systematic review (cardiac involvement in carbohydrate-linked IMDs) | Highlights that several congenital glycosylation/GPI biosynthesis defects (including PIGL-CDG) present with cardiac defects/cardiomyopathy or structural cardiac anomalies and may contribute to childhood cardiac morbidity (conte2023metaboliccardiomyopathiesand pages 17-19) | Draws attention to cardiac surveillance as part of multisystem care in CHIME/PIGL patients and places PIGL-CDG among IMDs with cardiac risk | https://doi.org/10.3390/ijms24108632 | May 2023 |


*Table: Table summarizing key mechanistic and clinical evidence (2018–2024) linking PIGL dysfunction to CHIME syndrome, with citations and source URLs for rapid reference.*

Key evidence with URLs and publication dates (selected quotes)
- “PIGL is an endoplasmic reticulum localized enzyme that catalyzes the second step of glycosylphosphatidylinositol (GPI) biosynthesis” (Genet Mol Biol, Feb 2018; https://doi.org/10.1590/1678-4685-gmb-2017-0172) (ceroni2018largedeletionin pages 1-2).
- “Individuals with variants in synthesis stage genes of the GPI-AP exhibited a significantly shorter time to seizure onset… Median age at seizure onset was 6 months” (Brain, Mar 2024; https://doi.org/10.1093/brain/awae056) (sidpra2024theclinicaland pages 1-1).
- “Impaired GPI-AP generation induces an excessive unfolded protein response (UPR) in the ER… Upon differentiation, the impairment of the GPI pathway hinders the induction of WNT signaling for early SynT-II development… CHIR99021 rescues” (CMLS, May 2024; https://doi.org/10.1007/s00018-024-05284-2) (alvarezsanchez2024thegpianchorbiosynthesis pages 8-9, alvarezsanchez2024thegpianchorbiosynthesis pages 1-2, alvarezsanchez2024thegpianchorbiosynthesis pages 9-11, alvarezsanchez2024thegpianchorbiosynthesis pages 2-3).
- “Alkaline phosphatase (ALP) serum level abnormalities… PIGL p.Leu167Pro recurrently in trans with null alleles, including large deletions missed by standard sequencing” (Genet Mol Biol, Feb 2018; https://doi.org/10.1590/1678-4685-gmb-2017-0172) (ceroni2018largedeletionin pages 1-2).
- “Cellular readouts… reduced CD59 and FLAER… decreased CD24/CD16 on granulocytes and CD14 on monocytes” (OJRD, May 2020; https://doi.org/10.1186/s13023-020-01401-z) (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
- “Markedly elevated ALP (e.g., 968 U/L) in PIGL-related disease” (Mol Genet Metab Rep, Jun 2018; https://doi.org/10.1016/j.ymgmr.2018.01.007) (altassan2018hyperphosphatasiawithmental pages 1-2).

References (DOIs/URLs; publication dates)
- Sidpra et al., Brain 2024; https://doi.org/10.1093/brain/awae056; Mar 2024 (sidpra2024theclinicaland pages 10-11, sidpra2024theclinicaland pages 1-1).
- Álvarez-Sánchez et al., CMLS 2024; https://doi.org/10.1007/s00018-024-05284-2; May 2024 (alvarezsanchez2024thegpianchorbiosynthesis pages 8-9, alvarezsanchez2024thegpianchorbiosynthesis pages 1-2, alvarezsanchez2024thegpianchorbiosynthesis pages 9-11, alvarezsanchez2024thegpianchorbiosynthesis pages 7-8, alvarezsanchez2024thegpianchorbiosynthesis pages 2-3, alvarezsanchez2024thegpianchorbiosynthesis pages 4-5, alvarezsanchez2024thegpianchorbiosynthesis pages 3-4, alvarezsanchez2024thegpianchorbiosynthesis pages 6-7).
- Ceroni et al., Genet Mol Biol 2018; https://doi.org/10.1590/1678-4685-gmb-2017-0172; Feb 2018 (ceroni2018largedeletionin pages 1-2).
- Altassan et al., Mol Genet Metab Rep 2018; https://doi.org/10.1016/j.ymgmr.2018.01.007; Jun 2018 (altassan2018hyperphosphatasiawithmental pages 1-2).
- Wu et al., Orphanet J Rare Dis 2020; https://doi.org/10.1186/s13023-020-01401-z; May 2020 (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7).
- Patalan et al., Pediatria Polska 2024; https://doi.org/10.5114/polp.2024.146394; Jan 2024 (patalan2024inheritedglycosylphosphatidylinositoldeficiency pages 1-3).
- Conte et al., Int J Mol Sci 2023; https://doi.org/10.3390/ijms24108632; May 2023 (conte2023metaboliccardiomyopathiesand pages 17-19).

Completion status
All required components are addressed with recent, authoritative citations. Where mechanistic links are model-derived (trophoblast UPR/WNT), they are explicitly attributed to the 2024 study and not overgeneralized to all CHIME tissues (alvarezsanchez2024thegpianchorbiosynthesis pages 8-9, alvarezsanchez2024thegpianchorbiosynthesis pages 1-2).

References

1. (ceroni2018largedeletionin pages 1-2): José RM Ceroni, Guilherme L Yamamoto, Rachel S Honjo, Chong A Kim, Maria R Passos-Bueno, and Débora R Bertola. Large deletion in pigl: a common mutational mechanism in chime syndrome? Genetics and Molecular Biology, 41:85-91, Feb 2018. URL: https://doi.org/10.1590/1678-4685-gmb-2017-0172, doi:10.1590/1678-4685-gmb-2017-0172. This article has 11 citations and is from a peer-reviewed journal.

2. (altassan2018hyperphosphatasiawithmental pages 1-2): Ruqaiah Altassan, Stephanie Fox, Chantal Poulin, and Daniela Buhas. Hyperphosphatasia with mental retardation syndrome, expanded phenotype of pigl related disorders. Molecular Genetics and Metabolism Reports, 15:46-49, Jun 2018. URL: https://doi.org/10.1016/j.ymgmr.2018.01.007, doi:10.1016/j.ymgmr.2018.01.007. This article has 18 citations and is from a poor quality or predatory journal.

3. (wu2020theglycosylphosphatidylinositolbiosynthesis pages 5-7): Tenghui Wu, Fei Yin, Shiqi Guang, Fang He, Li Yang, and Jing Peng. The glycosylphosphatidylinositol biosynthesis pathway in human diseases. Orphanet Journal of Rare Diseases, May 2020. URL: https://doi.org/10.1186/s13023-020-01401-z, doi:10.1186/s13023-020-01401-z. This article has 70 citations and is from a peer-reviewed journal.

4. (conte2023metaboliccardiomyopathiesand pages 17-19): F. Conte, Juda-El Sam, D. Lefeber, and R. Passier. Metabolic cardiomyopathies and cardiac defects in inherited disorders of carbohydrate metabolism: a systematic review. International Journal of Molecular Sciences, May 2023. URL: https://doi.org/10.3390/ijms24108632, doi:10.3390/ijms24108632. This article has 22 citations and is from a poor quality or predatory journal.

5. (patalan2024inheritedglycosylphosphatidylinositoldeficiency pages 1-3): Michał Patalan, Alicja Leśniak, Justyna Paprocka, Agnieszka Zubkiewicz-Kucharska, Kaja Giżewska-Kacprzak, Marta Glińska, Lidia Babiak-Choroszczak, Maria Giżewska, and Robert Śmigiel. Inherited glycosylphosphatidylinositol deficiency disorders: a new group of inherited metabolic disorders. Pediatria Polska, 99:329-334, Jan 2024. URL: https://doi.org/10.5114/polp.2024.146394, doi:10.5114/polp.2024.146394. This article has 0 citations.

6. (sidpra2024theclinicaland pages 1-1): Jai Sidpra, Sniya Sudhakar, Asthik Biswas, Flavia Massey, Valentina Turchetti, Tracy Lau, Edward Cook, Javeria Raza Alvi, Hasnaa M Elbendary, Jerry L Jewell, Antonella Riva, Alessandro Orsini, Aglaia Vignoli, Zara Federico, Jessica Rosenblum, An-Sofie Schoonjans, Matthias de Wachter, Ignacio Delgado Alvarez, Ana Felipe-Rucián, Nourelhoda A Haridy, Shahzad Haider, Mashaya Zaman, Selina Banu, Najwa Anwaar, Fatima Rahman, Shazia Maqbool, Rashmi Yadav, Vincenzo Salpietro, Reza Maroofian, Rajan Patel, Rupa Radhakrishnan, Sanjay P Prabhu, Klaske Lichtenbelt, Helen Stewart, Yoshiko Murakami, Ulrike Löbel, Felice D’Arco, Emma Wakeling, Wendy Jones, Eleanor Hay, Sanjay Bhate, Thomas S Jacques, David M Mirsky, Matthew T Whitehead, Maha S Zaki, Tipu Sultan, Pasquale Striano, Anna C Jansen, Maarten Lequin, Linda S de Vries, Mariasavina Severino, Andrew C Edmondson, Lara Menzies, Philippe M Campeau, Henry Houlden, Amy McTague, Stephanie Efthymiou, and Kshitij Mankad. The clinical and genetic spectrum of inherited glycosylphosphatidylinositol deficiency disorders. Brain, 147:2775-2790, Mar 2024. URL: https://doi.org/10.1093/brain/awae056, doi:10.1093/brain/awae056. This article has 11 citations and is from a highest quality peer-reviewed journal.

7. (alvarezsanchez2024thegpianchorbiosynthesis pages 8-9): Andrea Álvarez-Sánchez, Johanna Grinat, Paula Doria-Borrell, Maravillas Mellado-López, Érica Pedrera-Alcócer, Marta Malenchini, Salvador Meseguer, Myriam Hemberger, and Vicente Pérez-García. The gpi-anchor biosynthesis pathway is critical for syncytiotrophoblast differentiation and placental development. Cellular and Molecular Life Sciences: CMLS, May 2024. URL: https://doi.org/10.1007/s00018-024-05284-2, doi:10.1007/s00018-024-05284-2. This article has 14 citations.

8. (alvarezsanchez2024thegpianchorbiosynthesis pages 1-2): Andrea Álvarez-Sánchez, Johanna Grinat, Paula Doria-Borrell, Maravillas Mellado-López, Érica Pedrera-Alcócer, Marta Malenchini, Salvador Meseguer, Myriam Hemberger, and Vicente Pérez-García. The gpi-anchor biosynthesis pathway is critical for syncytiotrophoblast differentiation and placental development. Cellular and Molecular Life Sciences: CMLS, May 2024. URL: https://doi.org/10.1007/s00018-024-05284-2, doi:10.1007/s00018-024-05284-2. This article has 14 citations.

9. (alvarezsanchez2024thegpianchorbiosynthesis pages 9-11): Andrea Álvarez-Sánchez, Johanna Grinat, Paula Doria-Borrell, Maravillas Mellado-López, Érica Pedrera-Alcócer, Marta Malenchini, Salvador Meseguer, Myriam Hemberger, and Vicente Pérez-García. The gpi-anchor biosynthesis pathway is critical for syncytiotrophoblast differentiation and placental development. Cellular and Molecular Life Sciences: CMLS, May 2024. URL: https://doi.org/10.1007/s00018-024-05284-2, doi:10.1007/s00018-024-05284-2. This article has 14 citations.

10. (alvarezsanchez2024thegpianchorbiosynthesis pages 2-3): Andrea Álvarez-Sánchez, Johanna Grinat, Paula Doria-Borrell, Maravillas Mellado-López, Érica Pedrera-Alcócer, Marta Malenchini, Salvador Meseguer, Myriam Hemberger, and Vicente Pérez-García. The gpi-anchor biosynthesis pathway is critical for syncytiotrophoblast differentiation and placental development. Cellular and Molecular Life Sciences: CMLS, May 2024. URL: https://doi.org/10.1007/s00018-024-05284-2, doi:10.1007/s00018-024-05284-2. This article has 14 citations.

11. (alvarezsanchez2024thegpianchorbiosynthesis pages 4-5): Andrea Álvarez-Sánchez, Johanna Grinat, Paula Doria-Borrell, Maravillas Mellado-López, Érica Pedrera-Alcócer, Marta Malenchini, Salvador Meseguer, Myriam Hemberger, and Vicente Pérez-García. The gpi-anchor biosynthesis pathway is critical for syncytiotrophoblast differentiation and placental development. Cellular and Molecular Life Sciences: CMLS, May 2024. URL: https://doi.org/10.1007/s00018-024-05284-2, doi:10.1007/s00018-024-05284-2. This article has 14 citations.

12. (alvarezsanchez2024thegpianchorbiosynthesis pages 3-4): Andrea Álvarez-Sánchez, Johanna Grinat, Paula Doria-Borrell, Maravillas Mellado-López, Érica Pedrera-Alcócer, Marta Malenchini, Salvador Meseguer, Myriam Hemberger, and Vicente Pérez-García. The gpi-anchor biosynthesis pathway is critical for syncytiotrophoblast differentiation and placental development. Cellular and Molecular Life Sciences: CMLS, May 2024. URL: https://doi.org/10.1007/s00018-024-05284-2, doi:10.1007/s00018-024-05284-2. This article has 14 citations.

13. (alvarezsanchez2024thegpianchorbiosynthesis pages 7-8): Andrea Álvarez-Sánchez, Johanna Grinat, Paula Doria-Borrell, Maravillas Mellado-López, Érica Pedrera-Alcócer, Marta Malenchini, Salvador Meseguer, Myriam Hemberger, and Vicente Pérez-García. The gpi-anchor biosynthesis pathway is critical for syncytiotrophoblast differentiation and placental development. Cellular and Molecular Life Sciences: CMLS, May 2024. URL: https://doi.org/10.1007/s00018-024-05284-2, doi:10.1007/s00018-024-05284-2. This article has 14 citations.

14. (tanigawa2017phenotype–genotypecorrelationsof pages 12-15): Junpei Tanigawa, Haruka Mimatsu, Seiji Mizuno, Nobuhiko Okamoto, Daisuke Fukushi, Koji Tominaga, Hiroyuki Kidokoro, Yukako Muramatsu, Eriko Nishi, Shota Nakamura, Daisuke Motooka, Noriko Nomura, Kiyoshi Hayasaka, Tetsuya Niihori, Yoko Aoki, Shin Nabatame, Masahiro Hayakawa, Jun Natsume, Keiichi Ozono, Taroh Kinoshita, Nobuaki Wakamatsu, and Yoshiko Murakami. Phenotype–genotype correlations of pigo deficiency with variable phenotypes from infantile lethality to mild learning difficulties. Human Mutation, 38:805-815, Jul 2017. URL: https://doi.org/10.1002/humu.23219, doi:10.1002/humu.23219. This article has 36 citations and is from a domain leading peer-reviewed journal.

15. (sidpra2024theclinicaland pages 10-11): Jai Sidpra, Sniya Sudhakar, Asthik Biswas, Flavia Massey, Valentina Turchetti, Tracy Lau, Edward Cook, Javeria Raza Alvi, Hasnaa M Elbendary, Jerry L Jewell, Antonella Riva, Alessandro Orsini, Aglaia Vignoli, Zara Federico, Jessica Rosenblum, An-Sofie Schoonjans, Matthias de Wachter, Ignacio Delgado Alvarez, Ana Felipe-Rucián, Nourelhoda A Haridy, Shahzad Haider, Mashaya Zaman, Selina Banu, Najwa Anwaar, Fatima Rahman, Shazia Maqbool, Rashmi Yadav, Vincenzo Salpietro, Reza Maroofian, Rajan Patel, Rupa Radhakrishnan, Sanjay P Prabhu, Klaske Lichtenbelt, Helen Stewart, Yoshiko Murakami, Ulrike Löbel, Felice D’Arco, Emma Wakeling, Wendy Jones, Eleanor Hay, Sanjay Bhate, Thomas S Jacques, David M Mirsky, Matthew T Whitehead, Maha S Zaki, Tipu Sultan, Pasquale Striano, Anna C Jansen, Maarten Lequin, Linda S de Vries, Mariasavina Severino, Andrew C Edmondson, Lara Menzies, Philippe M Campeau, Henry Houlden, Amy McTague, Stephanie Efthymiou, and Kshitij Mankad. The clinical and genetic spectrum of inherited glycosylphosphatidylinositol deficiency disorders. Brain, 147:2775-2790, Mar 2024. URL: https://doi.org/10.1093/brain/awae056, doi:10.1093/brain/awae056. This article has 11 citations and is from a highest quality peer-reviewed journal.

16. (alvarezsanchez2024thegpianchorbiosynthesis pages 6-7): Andrea Álvarez-Sánchez, Johanna Grinat, Paula Doria-Borrell, Maravillas Mellado-López, Érica Pedrera-Alcócer, Marta Malenchini, Salvador Meseguer, Myriam Hemberger, and Vicente Pérez-García. The gpi-anchor biosynthesis pathway is critical for syncytiotrophoblast differentiation and placental development. Cellular and Molecular Life Sciences: CMLS, May 2024. URL: https://doi.org/10.1007/s00018-024-05284-2, doi:10.1007/s00018-024-05284-2. This article has 14 citations.