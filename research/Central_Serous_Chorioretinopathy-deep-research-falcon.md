---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-29T09:12:57.236540'
end_time: '2026-06-29T09:36:34.334477'
duration_seconds: 1417.1
template_file: templates\disease_pathophysiology_research.md
template_variables:
  disease_name: Central Serous Chorioretinopathy
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 35
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Central_Serous_Chorioretinopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Central_Serous_Chorioretinopathy-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Central_Serous_Chorioretinopathy-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Central Serous Chorioretinopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Central Serous Chorioretinopathy** covering all of the
disease characteristics listed below. This report will be used to populate a disease knowledge
base entry. Be thorough and cite primary literature (PMID preferred) for all claims.

For each section, **suggested databases/resources** are listed. These are the first places
you should search for information on each topic.

---

### 1. Disease Information
> **Search first:** OMIM, Orphanet, ICD-10/ICD-11, MeSH, PubMed

- What is the disease? Provide a concise overview.
- What are the key identifiers? (OMIM, Orphanet, ICD-10/ICD-11, MeSH, Mondo)
- What are the common synonyms and alternative names?
- Is the information derived from individual patients (e.g., EHR) or aggregated disease-level resources?

### 2. Etiology

- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Risk Factors**:
  > **Search first:** PubMed, Cochrane Library, UpToDate, clinical guidelines, ClinVar, ClinGen, GWAS Catalog, PheGenI, CTD, CDC, WHO, epidemiological databases
  - Genetic risk factors (causal variants, susceptibility loci, modifier genes)
  - Environmental risk factors (toxins, lifestyle, occupational exposures, age, sex, family history)
- **Protective Factors**:
  > **Search first:** PubMed, Cochrane Library, clinical trial databases, GWAS Catalog, gnomAD, WHO, CDC, nutrition databases
  - Genetic protective factors (protective variants, modifier alleles)
  - Environmental protective factors (diet, lifestyle, exposures that reduce risk)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
  > **Search first:** CTD, PubMed, PheGenI, GxE databases

### 3. Phenotypes
> **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC

For each phenotype, provide:
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
  > For symptoms/signs: HPO, OMIM, Orphanet, PubMed
  > For behavioral changes: HPO, DSM, RDoC (Research Domain Criteria), PubMed
  > For laboratory abnormalities: LOINC, SNOMED CT, LabTests Online, PubMed
- **Phenotype characteristics**:
  > **Search first:** OMIM, Orphanet, HPO, PubMed
  - Age of symptom onset (neonatal, childhood, adult-onset, late-onset)
  - Symptom severity (mild, moderate, severe, variable)
  - Symptom progression (stable, progressive, episodic, fluctuating)
  - Frequency among affected individuals (percentage or qualitative)
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
  > **Search first:** EQ-5D database, SF-36, WHO QOL databases, PubMed
- Suggest HPO (Human Phenotype Ontology) terms for each phenotype

### 4. Genetic/Molecular Information

- **Causal Genes**: Gene mutations or chromosomal abnormalities responsible for disease (gene symbols, OMIM IDs)
  > **Search first:** OMIM, ClinVar, HGMD, Ensembl, NCBI Gene
- **Pathogenic Variants**:
  - Affected genes (gene symbols, HGNC IDs)
    > **Search first:** OMIM, NCBI Gene, Ensembl, HGNC, UniProt, GeneCards
  - Variant classification (pathogenic, likely pathogenic, VUS per ACMG/AMP guidelines)
    > **Search first:** ClinVar, ClinGen, ACMG/AMP guidelines, VarSome
  - Variant type/class (missense, frameshift, nonsense, splice-site, structural)
  - Allele frequency in population databases
    > **Search first:** gnomAD, 1000 Genomes, ExAC, TOPMed, dbSNP
  - Somatic vs germline origin
    > **Search first:** COSMIC (somatic), ClinVar, ICGC, TCGA
  - Functional consequences (loss of function, gain of function, dominant negative)
- **Modifier Genes**: Genes that modify disease severity or expression
- **Epigenetic Information**: DNA methylation, histone modifications, chromatin changes affecting disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Chromosomal Abnormalities**: Large-scale genetic changes (aneuploidy, translocations, inversions)
  > **Search first:** DECIPHER, ClinVar, ECARUCA, UCSC Genome Browser

### 5. Environmental Information

- **Environmental Factors**: Non-genetic contributing factors (toxins, radiation, pollution, occupational exposure)
  > **Search first:** CTD (Comparative Toxicogenomics Database), TOXNET, PubMed, EPA databases
- **Lifestyle Factors**: Behavioral factors (smoking, diet, exercise, alcohol consumption)
  > **Search first:** CDC databases, WHO, PubMed, NHANES
- **Infectious Agents**: If applicable, pathogens causing or triggering disease (bacteria, viruses, fungi, parasites)
  > **Search first:** NCBI Taxonomy, ViPR, BV-BRC, MicrobeDB, GIDEON

### 6. Mechanism / Pathophysiology

- **Molecular Pathways**: Specific signaling cascades or biochemical pathways involved (Wnt, MAPK, mTOR, PI3K-AKT, etc.)
  > **Search first:** KEGG, Reactome, WikiPathways, PathBank, BioCyc
- **Cellular Processes**: Cell-level mechanisms (apoptosis, autophagy, cell cycle dysregulation, inflammation, etc.)
  > **Search first:** Gene Ontology (GO), Reactome, KEGG, PubMed
- **Protein Dysfunction**: How protein structure or function is altered (misfolding, aggregation, loss of function, gain of function)
  > **Search first:** UniProt, PDB (Protein Data Bank), InterPro, Pfam, AlphaFold
- **Metabolic Changes**: Alterations in metabolic processes (energy metabolism, lipid metabolism, amino acid metabolism)
  > **Search first:** KEGG, BioCyc, HMDB (Human Metabolome Database), BRENDA
- **Immune System Involvement**: Role of immune response (autoimmunity, immunodeficiency, chronic inflammation)
  > **Search first:** ImmPort, Immunome Database, IEDB, Gene Ontology
- **Tissue Damage Mechanisms**: How tissues/ are injured (oxidative stress, ischemia, fibrosis, necrosis)
  > **Search first:** PubMed, Gene Ontology, Reactome
- **Biochemical Abnormalities**: Specific molecular defects (enzyme deficiencies, receptor dysfunction, ion channel defects)
  > **Search first:** BRENDA, UniProt, KEGG, OMIM, PubMed
- **Epigenetic Changes**: DNA methylation, histone modifications affecting gene expression in disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Molecular Profiling** (if available):
  - Transcriptomics/gene expression changes
    > **Search first:** GEO (Gene Expression Omnibus), ArrayExpress, GTEx, Human Cell Atlas, SRA
  - Proteomics findings
    > **Search first:** PRIDE, ProteomeXchange, Human Protein Atlas, STRING, BioGRID
  - Metabolomics signatures
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB, METLIN
  - Lipidomics alterations
    > **Search first:** LIPID MAPS, SwissLipids, LipidHome, Metabolomics Workbench
  - Genomic structural features
    > **Search first:** UCSC Genome Browser, Ensembl, NCBI, dbVar, DGV
- **Advanced Technologies** (if applicable):
  - Single-cell analysis findings (cell-type specific mechanisms, cellular heterogeneity)
    > **Search first:** Human Cell Atlas, Single Cell Portal, GEO, CELLxGENE
  - Spatial transcriptomics findings
    > **Search first:** GEO, Spatial Research, Vizgen, 10x Genomics data
  - Multi-omics integration results
    > **Search first:** TCGA, ICGC, cBioPortal, LinkedOmics, PubMed
  - Functional genomics screens (CRISPR, RNAi)
    > **Search first:** DepMap, GenomeRNAi, PubMed, BioGRID ORCS

For each mechanism, describe:
- The causal chain from initial trigger to clinical manifestation
- Which mechanisms are upstream vs downstream
- What cell types and biological processes are involved
- Suggest GO terms for biological processes and CL terms for cell types

### 7. Anatomical Structures Affected

- **Organ Level**:
  - Primary organs directly affected
  - Secondary organ involvement (complications, secondary effects)
  - Body systems involved (cardiovascular, nervous, digestive, respiratory, endocrine, etc.)
  > **Search first:** Uberon, FMA (Foundational Model of Anatomy), OMIM, HPO, ICD-11, MeSH, SNOMED CT
- **Tissue and Cell Level**:
  - Specific tissue types affected (epithelial, connective, muscle, nervous)
  - Specific cell populations targeted (with Cell Ontology terms)
  > **Search first:** Uberon, Human Protein Atlas, Cell Ontology, Human Cell Atlas, CellMarker, PanglaoDB
- **Subcellular Level**:
  - Cellular compartments involved (mitochondria, nucleus, ER, lysosomes) (with GO Cellular Component terms)
  > **Search first:** Gene Ontology (Cellular Component), UniProt, Human Protein Atlas
- **Localization**:
  - Specific anatomical sites (with UBERON terms)
    > **Search first:** FMA, Uberon, NeuroNames (for brain), SNOMED CT
  - Lateralization (unilateral, bilateral, asymmetric)
    > **Search first:** HPO, clinical literature, imaging databases

### 8. Temporal Development

- **Onset**:
  - Typical age of onset (congenital, pediatric, adult, geriatric)
  - Onset pattern (acute, subacute, chronic, insidious)
  > **Search first:** OMIM, Orphanet, HPO, PubMed
- **Progression**:
  - Disease stages (early, intermediate, advanced, end-stage)
    > **Search first:** Cancer Staging Manual (AJCC), WHO classifications, PubMed
  - Progression rate (rapid, slow, variable)
  - Disease course pattern (episodic, relapsing-remitting, progressive, stable)
  - Disease duration (self-limited, chronic lifelong)
  > **Search first:** Disease registries, longitudinal cohort databases, natural history studies, PubMed, Orphanet, OMIM
- **Patterns**:
  - Remission patterns (spontaneous, treatment-induced)
    > **Search first:** Clinical trial databases, disease registries, PubMed
  - Critical periods (time windows of vulnerability or opportunity for intervention)
    > **Search first:** PubMed, developmental biology databases, clinical guidelines

### 9. Inheritance and Population

- **Epidemiology**:
  - Prevalence (cases per 100,000 at given time)
  - Incidence (new cases per 100,000 per year)
  > **Search first:** Orphanet, CDC, WHO, GBD (Global Burden of Disease), national registries, SEER, disease registries
- **For Genetic Etiology**:
  - Inheritance pattern (AD, AR, X-linked, mitochondrial, multifactorial, polygenic)
    > **Search first:** OMIM, Orphanet, ClinVar, GTR (Genetic Testing Registry)
  - Penetrance (complete, incomplete, age-dependent)
    > **Search first:** ClinVar, OMIM, PubMed, ClinGen
  - Expressivity (variable, consistent)
    > **Search first:** OMIM, ClinVar, PubMed
  - Genetic anticipation (increasing severity in successive generations)
    > **Search first:** OMIM, PubMed (especially for repeat expansion disorders)
  - Germline mosaicism
    > **Search first:** ClinVar, OMIM, genetic counseling literature, PubMed
  - Founder effects (population-specific mutations)
    > **Search first:** gnomAD, population genetics databases, PubMed
  - Consanguinity role
    > **Search first:** OMIM, population studies, genetic counseling resources
  - Carrier frequency
    > **Search first:** gnomAD, carrier screening databases, GeneReviews, GTR
- **Population Demographics**:
  - Affected populations (ethnic or demographic groups with higher prevalence)
    > **Search first:** gnomAD, 1000 Genomes, PAGE Study, PubMed, population registries
  - Geographic distribution (endemic areas, regional variation)
    > **Search first:** WHO, CDC, GBD, Orphanet, geographic epidemiology databases
  - Geographic distribution of specific variants
  - Sex ratio (male:female)
    > **Search first:** Disease registries, OMIM, PubMed, epidemiological databases
  - Age distribution of affected individuals
    > **Search first:** CDC, disease registries, SEER, Orphanet

### 10. Diagnostics

- **Clinical Tests**:
  - Laboratory tests (blood, urine, tissue chemistry, specific enzyme assays)
    > **Search first:** LOINC, LabTests Online, PubMed
  - Biomarkers (proteins, metabolites, genetic markers, circulating biomarkers)
    > **Search first:** FDA Biomarker List, BEST (Biomarkers, EndpointS, and other Tools), PubMed
  - Imaging studies (X-ray, CT, MRI, PET, ultrasound)
    > **Search first:** RadLex, DICOM, Radiopaedia, imaging databases
  - Functional tests (pulmonary function, cardiac stress tests)
    > **Search first:** LOINC, clinical guidelines, PubMed
  - Electrophysiology (EEG, EMG, ECG, nerve conduction studies)
    > **Search first:** LOINC, clinical neurophysiology databases, PubMed
  - Biopsy findings (histopathology, immunohistochemistry)
    > **Search first:** SNOMED CT, College of American Pathologists resources, PubMed
  - Pathology findings (microscopic examination)
    > **Search first:** SNOMED CT, Digital Pathology databases, PubMed
- **Genetic Testing**:
  > **Search first:** GTR (Genetic Testing Registry), GeneReviews, ClinGen
  - Overview of recommended genetic testing approach
  - Whole genome sequencing (WGS) utility
    > **Search first:** GTR, ClinVar, GEL (Genomics England), gnomAD
  - Whole exome sequencing (WES) utility
    > **Search first:** GTR, ClinVar, OMIM, GeneMatcher
  - Gene panels (which panels, which genes)
    > **Search first:** GTR, ClinVar, laboratory-specific databases
  - Single gene testing
    > **Search first:** GTR, ClinVar, OMIM, GeneReviews
  - Chromosomal microarray (CMA)
    > **Search first:** DECIPHER, ClinVar, dbVar, ECARUCA
  - Karyotyping
    > **Search first:** Chromosome Abnormality Database, ClinVar, cytogenetics resources
  - FISH
    > **Search first:** ClinVar, cytogenetics databases, PubMed
  - Mitochondrial DNA testing
    > **Search first:** MITOMAP, MSeqDR, ClinVar, GTR
  - Repeat expansion testing
    > **Search first:** GTR, ClinVar, repeat expansion databases, PubMed
- **Omics-Based Diagnostics** (if applicable):
  - RNA sequencing / transcriptomics
    > **Search first:** GEO, ArrayExpress, GTEx, RNA-seq databases
  - Proteomics
    > **Search first:** PRIDE, ProteomeXchange, FDA Biomarker database
  - Metabolomics
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB
  - Epigenomics
    > **Search first:** GEO, ENCODE, Roadmap Epigenomics, MethBase
  - Liquid biopsy
    > **Search first:** COSMIC, ClinVar, liquid biopsy databases, PubMed
- **Clinical Criteria**:
  - Standardized diagnostic criteria (DSM, ICD, society guidelines)
    > **Search first:** DSM-5, ICD-11, clinical society guidelines, UpToDate
  - Differential diagnosis (other conditions to rule out, with distinguishing features)
    > **Search first:** DynaMed, UpToDate, clinical decision support systems
- **Screening**:
  - Screening methods for asymptomatic individuals (newborn screening, carrier screening, cascade screening)
    > **Search first:** ACMG recommendations, CDC newborn screening, GTR

### 11. Outcome/Prognosis

- **Survival and Mortality**:
  - Survival rate (5-year, 10-year, overall)
    > **Search first:** SEER, cancer registries, disease-specific registries, PubMed
  - Life expectancy (with and without treatment if applicable)
    > **Search first:** Orphanet, disease registries, actuarial databases, PubMed
  - Mortality rate
    > **Search first:** CDC, WHO, GBD, national mortality databases
  - Disease-specific mortality (deaths directly attributable to disease)
    > **Search first:** Disease registries, CDC Wonder, GBD, PubMed
- **Morbidity and Function**:
  - Morbidity (disease-related disability and health impacts)
    > **Search first:** GBD, WHO, disability databases, PubMed
  - Disability outcomes (long-term functional impairments)
    > **Search first:** ICF (International Classification of Functioning), disability registries
  - Quality of life measures (EQ-5D, SF-36, PROMIS, disease-specific tools)
    > **Search first:** EQ-5D database, SF-36, PROMIS, PubMed
- **Disease Course**:
  - Complications (secondary problems: infections, organ failure, etc.)
    > **Search first:** ICD codes, disease registries, clinical databases, PubMed
  - Recovery potential (likelihood and extent of recovery, with vs without treatment)
    > **Search first:** Natural history studies, rehabilitation databases, PubMed
- **Prediction**:
  - Prognostic factors (age, disease severity, biomarkers, treatment response)
    > **Search first:** Prognostic models databases, clinical calculators, PubMed
  - Prognostic biomarkers (molecular markers predicting disease course)
    > **Search first:** FDA Biomarker database, PubMed, cancer prognostic databases

### 12. Treatment

- **Pharmacotherapy**:
  - Pharmacological treatments (drug names, drug classes, mechanisms of action)
    > **Search first:** DrugBank, RxNorm, ATC classification, DailyMed, FDA databases
  - Pharmacogenomics (how genetic variants affect drug metabolism, efficacy, toxicity)
    > **Search first:** PharmGKB, CPIC (Clinical Pharmacogenetics), FDA Table of PGx Biomarkers
- **Advanced Therapeutics**:
  - Gene therapy (viral vectors, CRISPR, gene replacement, gene editing)
    > **Search first:** ClinicalTrials.gov, FDA gene therapy database, ASGCT resources
  - Cell therapy (stem cell transplant, CAR-T, cellular therapeutics)
    > **Search first:** ClinicalTrials.gov, FDA cell therapy database, FACT standards
  - RNA-based therapies (ASOs, siRNA, mRNA therapies)
    > **Search first:** ClinicalTrials.gov, FDA approvals, PubMed
  - Targeted therapies (treatments directed at specific molecular targets)
    > **Search first:** My Cancer Genome, OncoKB, ClinicalTrials.gov, FDA approvals
  - Immunotherapies (checkpoint inhibitors, monoclonal antibodies)
    > **Search first:** Cancer Immunotherapy Database, FDA approvals, ClinicalTrials.gov
- **Surgical and Interventional**:
  - Surgical interventions (types of surgery, timing, outcomes)
    > **Search first:** CPT codes, surgical registries, clinical guidelines, PubMed
- **Supportive and Rehabilitative**:
  - Supportive care (symptom management, pain control, nutrition)
    > **Search first:** Clinical guidelines, Cochrane Library, PubMed
  - Rehabilitation (physical therapy, occupational therapy, speech therapy)
    > **Search first:** Rehabilitation medicine databases, clinical guidelines, PubMed
- **Experimental**:
  - Experimental treatments in clinical trials (with NCT identifiers if available)
    > **Search first:** ClinicalTrials.gov, EU Clinical Trials Register, WHO ICTRP
- **Treatment Outcomes**:
  - Treatment response rates
    > **Search first:** Clinical trial databases, FDA reviews, systematic reviews, PubMed
  - Side effects and adverse events
    > **Search first:** FDA Adverse Event Reporting System (FAERS), MedWatch, PubMed
- **Treatment Strategy**:
  - Treatment algorithms (clinical pathways, decision trees)
    > **Search first:** Clinical practice guidelines, NCCN Guidelines, UpToDate
  - Combination therapies
    > **Search first:** ClinicalTrials.gov, treatment guidelines, PubMed
  - Personalized medicine approaches (genotype-guided treatment)
    > **Search first:** My Cancer Genome, CIViC, PharmGKB, precision medicine databases

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

### 13. Prevention

- **Prevention Levels**:
  - Primary prevention (preventing disease occurrence: vaccination, risk factor modification)
    > **Search first:** CDC, WHO, USPSTF recommendations, Cochrane Library
  - Secondary prevention (early detection and treatment: screening programs, early intervention)
    > **Search first:** USPSTF, CDC screening guidelines, WHO
  - Tertiary prevention (preventing complications in those with disease)
    > **Search first:** Clinical guidelines, disease management protocols, PubMed
- **Immunization**: Vaccine strategies (if applicable)
  > **Search first:** CDC vaccine schedules, WHO immunization, FDA vaccine database
- **Screening and Early Detection**:
  - Screening programs (population-based: newborn screening, cancer screening)
    > **Search first:** CDC screening programs, USPSTF, cancer screening databases
  - Genetic screening (carrier screening, preimplantation genetic diagnosis, prenatal testing)
    > **Search first:** ACMG recommendations, ACOG guidelines, GTR
  - Risk stratification (identifying high-risk individuals for targeted prevention)
    > **Search first:** Risk prediction models, clinical calculators, PubMed
- **Behavioral Interventions**: Lifestyle modifications to reduce risk
  > **Search first:** CDC, WHO, behavioral intervention databases, Cochrane Library
- **Counseling**: Genetic counseling (risk assessment, family planning guidance)
  > **Search first:** NSGC resources, ACMG guidelines, GeneReviews
- **Public Health**:
  - Public health interventions (sanitation, vector control, health education)
    > **Search first:** CDC, WHO, public health databases, PubMed
  - Environmental interventions (reducing environmental risk factors)
    > **Search first:** EPA databases, WHO environmental health, PubMed
- **Prophylaxis**: Preventive medications or procedures
  > **Search first:** Clinical guidelines, FDA approvals, PubMed

### 14. Other Species / Natural Disease

- **Taxonomy**: Species affected (with NCBI Taxon identifiers)
  > **Search first:** NCBI Taxonomy
- **Breed**: Specific breeds affected (with VBO identifiers if applicable)
  > **Search first:** VBO (Vertebrate Breed Ontology)
- **Gene**: Orthologous genes in other species (with NCBI Gene IDs)
  > **Search first:** NCBI Gene
- **Natural Disease**:
  - Naturally occurring disease in other species (companion animals, wildlife)
    > **Search first:** OMIA (Online Mendelian Inheritance in Animals), VetCompass, PubMed
  - Veterinary relevance and importance in animal health
    > **Search first:** OMIA, veterinary databases, PubMed
- **Comparative Biology**:
  - Comparative pathology (similarities and differences across species)
    > **Search first:** OMIA, comparative pathology databases, PubMed
  - Evolutionary conservation of disease mechanisms
    > **Search first:** HomoloGene, OrthoMCL, Alliance of Genome Resources
- **Transmission** (if applicable):
  - Zoonotic potential
    > **Search first:** CDC zoonotic diseases, WHO zoonoses, GIDEON
  - Cross-species susceptibility
    > **Search first:** NCBI Taxonomy, veterinary databases, PubMed

### 15. Model Organisms

- **Model Types**:
  - Model organism type (mammalian, invertebrate, cellular, in vitro)
    > **Search first:** Alliance of Genome Resources, model organism databases
  - Specific model systems (mouse, rat, zebrafish, Drosophila, C. elegans, yeast, cell lines, organoids, iPSCs)
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, SGD, ATCC, Cellosaurus
  - Induced models (drug treatment, surgical intervention, environmental manipulation)
    > **Search first:** MGI, model organism databases, PubMed
- **Genetic Models**:
  - Types available (knockout, knock-in, transgenic, conditional, humanized)
    > **Search first:** MGI, IMPC, KOMP, EuMMCR, IMSR
- **Model Characteristics**:
  - Phenotype recapitulation (how well model reproduces human disease features)
    > **Search first:** Model organism databases, comparative studies, PubMed
  - Model limitations (aspects of human disease not captured)
    > **Search first:** Model organism databases, PubMed, review articles
- **Applications**:
  - Research applications (what aspects of disease can be studied)
    > **Search first:** Model organism databases, PubMed
- **Resources**:
  - Model databases
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, IMSR, EMMA, MMRRC

---

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic and clinical claims
- Prioritize recent reviews and landmark papers
- Include direct quotes from abstracts where possible to support key statements
- Distinguish evidence source types: human clinical, model organism, in vitro, computational

## Output Format

Structure your response as a comprehensive narrative organized by the sections above.
For each section, provide:
- Factual content with specific details (numbers, percentages, gene names, variant nomenclature)
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
- Evidence citations with PMIDs
- Direct quotes from abstracts to support key claims
- Clear indication when information is not available or not applicable for this disease

This report will be used to populate a disease knowledge base entry with:
- Pathophysiology descriptions with causal chains
- Gene/protein annotations (HGNC, GO terms)
- Phenotype associations (HP terms) with frequencies
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


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

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Central Serous Chorioretinopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Central Serous Chorioretinopathy** covering all of the
disease characteristics listed below. This report will be used to populate a disease knowledge
base entry. Be thorough and cite primary literature (PMID preferred) for all claims.

For each section, **suggested databases/resources** are listed. These are the first places
you should search for information on each topic.

---

### 1. Disease Information
> **Search first:** OMIM, Orphanet, ICD-10/ICD-11, MeSH, PubMed

- What is the disease? Provide a concise overview.
- What are the key identifiers? (OMIM, Orphanet, ICD-10/ICD-11, MeSH, Mondo)
- What are the common synonyms and alternative names?
- Is the information derived from individual patients (e.g., EHR) or aggregated disease-level resources?

### 2. Etiology

- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Risk Factors**:
  > **Search first:** PubMed, Cochrane Library, UpToDate, clinical guidelines, ClinVar, ClinGen, GWAS Catalog, PheGenI, CTD, CDC, WHO, epidemiological databases
  - Genetic risk factors (causal variants, susceptibility loci, modifier genes)
  - Environmental risk factors (toxins, lifestyle, occupational exposures, age, sex, family history)
- **Protective Factors**:
  > **Search first:** PubMed, Cochrane Library, clinical trial databases, GWAS Catalog, gnomAD, WHO, CDC, nutrition databases
  - Genetic protective factors (protective variants, modifier alleles)
  - Environmental protective factors (diet, lifestyle, exposures that reduce risk)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
  > **Search first:** CTD, PubMed, PheGenI, GxE databases

### 3. Phenotypes
> **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC

For each phenotype, provide:
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
  > For symptoms/signs: HPO, OMIM, Orphanet, PubMed
  > For behavioral changes: HPO, DSM, RDoC (Research Domain Criteria), PubMed
  > For laboratory abnormalities: LOINC, SNOMED CT, LabTests Online, PubMed
- **Phenotype characteristics**:
  > **Search first:** OMIM, Orphanet, HPO, PubMed
  - Age of symptom onset (neonatal, childhood, adult-onset, late-onset)
  - Symptom severity (mild, moderate, severe, variable)
  - Symptom progression (stable, progressive, episodic, fluctuating)
  - Frequency among affected individuals (percentage or qualitative)
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
  > **Search first:** EQ-5D database, SF-36, WHO QOL databases, PubMed
- Suggest HPO (Human Phenotype Ontology) terms for each phenotype

### 4. Genetic/Molecular Information

- **Causal Genes**: Gene mutations or chromosomal abnormalities responsible for disease (gene symbols, OMIM IDs)
  > **Search first:** OMIM, ClinVar, HGMD, Ensembl, NCBI Gene
- **Pathogenic Variants**:
  - Affected genes (gene symbols, HGNC IDs)
    > **Search first:** OMIM, NCBI Gene, Ensembl, HGNC, UniProt, GeneCards
  - Variant classification (pathogenic, likely pathogenic, VUS per ACMG/AMP guidelines)
    > **Search first:** ClinVar, ClinGen, ACMG/AMP guidelines, VarSome
  - Variant type/class (missense, frameshift, nonsense, splice-site, structural)
  - Allele frequency in population databases
    > **Search first:** gnomAD, 1000 Genomes, ExAC, TOPMed, dbSNP
  - Somatic vs germline origin
    > **Search first:** COSMIC (somatic), ClinVar, ICGC, TCGA
  - Functional consequences (loss of function, gain of function, dominant negative)
- **Modifier Genes**: Genes that modify disease severity or expression
- **Epigenetic Information**: DNA methylation, histone modifications, chromatin changes affecting disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Chromosomal Abnormalities**: Large-scale genetic changes (aneuploidy, translocations, inversions)
  > **Search first:** DECIPHER, ClinVar, ECARUCA, UCSC Genome Browser

### 5. Environmental Information

- **Environmental Factors**: Non-genetic contributing factors (toxins, radiation, pollution, occupational exposure)
  > **Search first:** CTD (Comparative Toxicogenomics Database), TOXNET, PubMed, EPA databases
- **Lifestyle Factors**: Behavioral factors (smoking, diet, exercise, alcohol consumption)
  > **Search first:** CDC databases, WHO, PubMed, NHANES
- **Infectious Agents**: If applicable, pathogens causing or triggering disease (bacteria, viruses, fungi, parasites)
  > **Search first:** NCBI Taxonomy, ViPR, BV-BRC, MicrobeDB, GIDEON

### 6. Mechanism / Pathophysiology

- **Molecular Pathways**: Specific signaling cascades or biochemical pathways involved (Wnt, MAPK, mTOR, PI3K-AKT, etc.)
  > **Search first:** KEGG, Reactome, WikiPathways, PathBank, BioCyc
- **Cellular Processes**: Cell-level mechanisms (apoptosis, autophagy, cell cycle dysregulation, inflammation, etc.)
  > **Search first:** Gene Ontology (GO), Reactome, KEGG, PubMed
- **Protein Dysfunction**: How protein structure or function is altered (misfolding, aggregation, loss of function, gain of function)
  > **Search first:** UniProt, PDB (Protein Data Bank), InterPro, Pfam, AlphaFold
- **Metabolic Changes**: Alterations in metabolic processes (energy metabolism, lipid metabolism, amino acid metabolism)
  > **Search first:** KEGG, BioCyc, HMDB (Human Metabolome Database), BRENDA
- **Immune System Involvement**: Role of immune response (autoimmunity, immunodeficiency, chronic inflammation)
  > **Search first:** ImmPort, Immunome Database, IEDB, Gene Ontology
- **Tissue Damage Mechanisms**: How tissues/ are injured (oxidative stress, ischemia, fibrosis, necrosis)
  > **Search first:** PubMed, Gene Ontology, Reactome
- **Biochemical Abnormalities**: Specific molecular defects (enzyme deficiencies, receptor dysfunction, ion channel defects)
  > **Search first:** BRENDA, UniProt, KEGG, OMIM, PubMed
- **Epigenetic Changes**: DNA methylation, histone modifications affecting gene expression in disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Molecular Profiling** (if available):
  - Transcriptomics/gene expression changes
    > **Search first:** GEO (Gene Expression Omnibus), ArrayExpress, GTEx, Human Cell Atlas, SRA
  - Proteomics findings
    > **Search first:** PRIDE, ProteomeXchange, Human Protein Atlas, STRING, BioGRID
  - Metabolomics signatures
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB, METLIN
  - Lipidomics alterations
    > **Search first:** LIPID MAPS, SwissLipids, LipidHome, Metabolomics Workbench
  - Genomic structural features
    > **Search first:** UCSC Genome Browser, Ensembl, NCBI, dbVar, DGV
- **Advanced Technologies** (if applicable):
  - Single-cell analysis findings (cell-type specific mechanisms, cellular heterogeneity)
    > **Search first:** Human Cell Atlas, Single Cell Portal, GEO, CELLxGENE
  - Spatial transcriptomics findings
    > **Search first:** GEO, Spatial Research, Vizgen, 10x Genomics data
  - Multi-omics integration results
    > **Search first:** TCGA, ICGC, cBioPortal, LinkedOmics, PubMed
  - Functional genomics screens (CRISPR, RNAi)
    > **Search first:** DepMap, GenomeRNAi, PubMed, BioGRID ORCS

For each mechanism, describe:
- The causal chain from initial trigger to clinical manifestation
- Which mechanisms are upstream vs downstream
- What cell types and biological processes are involved
- Suggest GO terms for biological processes and CL terms for cell types

### 7. Anatomical Structures Affected

- **Organ Level**:
  - Primary organs directly affected
  - Secondary organ involvement (complications, secondary effects)
  - Body systems involved (cardiovascular, nervous, digestive, respiratory, endocrine, etc.)
  > **Search first:** Uberon, FMA (Foundational Model of Anatomy), OMIM, HPO, ICD-11, MeSH, SNOMED CT
- **Tissue and Cell Level**:
  - Specific tissue types affected (epithelial, connective, muscle, nervous)
  - Specific cell populations targeted (with Cell Ontology terms)
  > **Search first:** Uberon, Human Protein Atlas, Cell Ontology, Human Cell Atlas, CellMarker, PanglaoDB
- **Subcellular Level**:
  - Cellular compartments involved (mitochondria, nucleus, ER, lysosomes) (with GO Cellular Component terms)
  > **Search first:** Gene Ontology (Cellular Component), UniProt, Human Protein Atlas
- **Localization**:
  - Specific anatomical sites (with UBERON terms)
    > **Search first:** FMA, Uberon, NeuroNames (for brain), SNOMED CT
  - Lateralization (unilateral, bilateral, asymmetric)
    > **Search first:** HPO, clinical literature, imaging databases

### 8. Temporal Development

- **Onset**:
  - Typical age of onset (congenital, pediatric, adult, geriatric)
  - Onset pattern (acute, subacute, chronic, insidious)
  > **Search first:** OMIM, Orphanet, HPO, PubMed
- **Progression**:
  - Disease stages (early, intermediate, advanced, end-stage)
    > **Search first:** Cancer Staging Manual (AJCC), WHO classifications, PubMed
  - Progression rate (rapid, slow, variable)
  - Disease course pattern (episodic, relapsing-remitting, progressive, stable)
  - Disease duration (self-limited, chronic lifelong)
  > **Search first:** Disease registries, longitudinal cohort databases, natural history studies, PubMed, Orphanet, OMIM
- **Patterns**:
  - Remission patterns (spontaneous, treatment-induced)
    > **Search first:** Clinical trial databases, disease registries, PubMed
  - Critical periods (time windows of vulnerability or opportunity for intervention)
    > **Search first:** PubMed, developmental biology databases, clinical guidelines

### 9. Inheritance and Population

- **Epidemiology**:
  - Prevalence (cases per 100,000 at given time)
  - Incidence (new cases per 100,000 per year)
  > **Search first:** Orphanet, CDC, WHO, GBD (Global Burden of Disease), national registries, SEER, disease registries
- **For Genetic Etiology**:
  - Inheritance pattern (AD, AR, X-linked, mitochondrial, multifactorial, polygenic)
    > **Search first:** OMIM, Orphanet, ClinVar, GTR (Genetic Testing Registry)
  - Penetrance (complete, incomplete, age-dependent)
    > **Search first:** ClinVar, OMIM, PubMed, ClinGen
  - Expressivity (variable, consistent)
    > **Search first:** OMIM, ClinVar, PubMed
  - Genetic anticipation (increasing severity in successive generations)
    > **Search first:** OMIM, PubMed (especially for repeat expansion disorders)
  - Germline mosaicism
    > **Search first:** ClinVar, OMIM, genetic counseling literature, PubMed
  - Founder effects (population-specific mutations)
    > **Search first:** gnomAD, population genetics databases, PubMed
  - Consanguinity role
    > **Search first:** OMIM, population studies, genetic counseling resources
  - Carrier frequency
    > **Search first:** gnomAD, carrier screening databases, GeneReviews, GTR
- **Population Demographics**:
  - Affected populations (ethnic or demographic groups with higher prevalence)
    > **Search first:** gnomAD, 1000 Genomes, PAGE Study, PubMed, population registries
  - Geographic distribution (endemic areas, regional variation)
    > **Search first:** WHO, CDC, GBD, Orphanet, geographic epidemiology databases
  - Geographic distribution of specific variants
  - Sex ratio (male:female)
    > **Search first:** Disease registries, OMIM, PubMed, epidemiological databases
  - Age distribution of affected individuals
    > **Search first:** CDC, disease registries, SEER, Orphanet

### 10. Diagnostics

- **Clinical Tests**:
  - Laboratory tests (blood, urine, tissue chemistry, specific enzyme assays)
    > **Search first:** LOINC, LabTests Online, PubMed
  - Biomarkers (proteins, metabolites, genetic markers, circulating biomarkers)
    > **Search first:** FDA Biomarker List, BEST (Biomarkers, EndpointS, and other Tools), PubMed
  - Imaging studies (X-ray, CT, MRI, PET, ultrasound)
    > **Search first:** RadLex, DICOM, Radiopaedia, imaging databases
  - Functional tests (pulmonary function, cardiac stress tests)
    > **Search first:** LOINC, clinical guidelines, PubMed
  - Electrophysiology (EEG, EMG, ECG, nerve conduction studies)
    > **Search first:** LOINC, clinical neurophysiology databases, PubMed
  - Biopsy findings (histopathology, immunohistochemistry)
    > **Search first:** SNOMED CT, College of American Pathologists resources, PubMed
  - Pathology findings (microscopic examination)
    > **Search first:** SNOMED CT, Digital Pathology databases, PubMed
- **Genetic Testing**:
  > **Search first:** GTR (Genetic Testing Registry), GeneReviews, ClinGen
  - Overview of recommended genetic testing approach
  - Whole genome sequencing (WGS) utility
    > **Search first:** GTR, ClinVar, GEL (Genomics England), gnomAD
  - Whole exome sequencing (WES) utility
    > **Search first:** GTR, ClinVar, OMIM, GeneMatcher
  - Gene panels (which panels, which genes)
    > **Search first:** GTR, ClinVar, laboratory-specific databases
  - Single gene testing
    > **Search first:** GTR, ClinVar, OMIM, GeneReviews
  - Chromosomal microarray (CMA)
    > **Search first:** DECIPHER, ClinVar, dbVar, ECARUCA
  - Karyotyping
    > **Search first:** Chromosome Abnormality Database, ClinVar, cytogenetics resources
  - FISH
    > **Search first:** ClinVar, cytogenetics databases, PubMed
  - Mitochondrial DNA testing
    > **Search first:** MITOMAP, MSeqDR, ClinVar, GTR
  - Repeat expansion testing
    > **Search first:** GTR, ClinVar, repeat expansion databases, PubMed
- **Omics-Based Diagnostics** (if applicable):
  - RNA sequencing / transcriptomics
    > **Search first:** GEO, ArrayExpress, GTEx, RNA-seq databases
  - Proteomics
    > **Search first:** PRIDE, ProteomeXchange, FDA Biomarker database
  - Metabolomics
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB
  - Epigenomics
    > **Search first:** GEO, ENCODE, Roadmap Epigenomics, MethBase
  - Liquid biopsy
    > **Search first:** COSMIC, ClinVar, liquid biopsy databases, PubMed
- **Clinical Criteria**:
  - Standardized diagnostic criteria (DSM, ICD, society guidelines)
    > **Search first:** DSM-5, ICD-11, clinical society guidelines, UpToDate
  - Differential diagnosis (other conditions to rule out, with distinguishing features)
    > **Search first:** DynaMed, UpToDate, clinical decision support systems
- **Screening**:
  - Screening methods for asymptomatic individuals (newborn screening, carrier screening, cascade screening)
    > **Search first:** ACMG recommendations, CDC newborn screening, GTR

### 11. Outcome/Prognosis

- **Survival and Mortality**:
  - Survival rate (5-year, 10-year, overall)
    > **Search first:** SEER, cancer registries, disease-specific registries, PubMed
  - Life expectancy (with and without treatment if applicable)
    > **Search first:** Orphanet, disease registries, actuarial databases, PubMed
  - Mortality rate
    > **Search first:** CDC, WHO, GBD, national mortality databases
  - Disease-specific mortality (deaths directly attributable to disease)
    > **Search first:** Disease registries, CDC Wonder, GBD, PubMed
- **Morbidity and Function**:
  - Morbidity (disease-related disability and health impacts)
    > **Search first:** GBD, WHO, disability databases, PubMed
  - Disability outcomes (long-term functional impairments)
    > **Search first:** ICF (International Classification of Functioning), disability registries
  - Quality of life measures (EQ-5D, SF-36, PROMIS, disease-specific tools)
    > **Search first:** EQ-5D database, SF-36, PROMIS, PubMed
- **Disease Course**:
  - Complications (secondary problems: infections, organ failure, etc.)
    > **Search first:** ICD codes, disease registries, clinical databases, PubMed
  - Recovery potential (likelihood and extent of recovery, with vs without treatment)
    > **Search first:** Natural history studies, rehabilitation databases, PubMed
- **Prediction**:
  - Prognostic factors (age, disease severity, biomarkers, treatment response)
    > **Search first:** Prognostic models databases, clinical calculators, PubMed
  - Prognostic biomarkers (molecular markers predicting disease course)
    > **Search first:** FDA Biomarker database, PubMed, cancer prognostic databases

### 12. Treatment

- **Pharmacotherapy**:
  - Pharmacological treatments (drug names, drug classes, mechanisms of action)
    > **Search first:** DrugBank, RxNorm, ATC classification, DailyMed, FDA databases
  - Pharmacogenomics (how genetic variants affect drug metabolism, efficacy, toxicity)
    > **Search first:** PharmGKB, CPIC (Clinical Pharmacogenetics), FDA Table of PGx Biomarkers
- **Advanced Therapeutics**:
  - Gene therapy (viral vectors, CRISPR, gene replacement, gene editing)
    > **Search first:** ClinicalTrials.gov, FDA gene therapy database, ASGCT resources
  - Cell therapy (stem cell transplant, CAR-T, cellular therapeutics)
    > **Search first:** ClinicalTrials.gov, FDA cell therapy database, FACT standards
  - RNA-based therapies (ASOs, siRNA, mRNA therapies)
    > **Search first:** ClinicalTrials.gov, FDA approvals, PubMed
  - Targeted therapies (treatments directed at specific molecular targets)
    > **Search first:** My Cancer Genome, OncoKB, ClinicalTrials.gov, FDA approvals
  - Immunotherapies (checkpoint inhibitors, monoclonal antibodies)
    > **Search first:** Cancer Immunotherapy Database, FDA approvals, ClinicalTrials.gov
- **Surgical and Interventional**:
  - Surgical interventions (types of surgery, timing, outcomes)
    > **Search first:** CPT codes, surgical registries, clinical guidelines, PubMed
- **Supportive and Rehabilitative**:
  - Supportive care (symptom management, pain control, nutrition)
    > **Search first:** Clinical guidelines, Cochrane Library, PubMed
  - Rehabilitation (physical therapy, occupational therapy, speech therapy)
    > **Search first:** Rehabilitation medicine databases, clinical guidelines, PubMed
- **Experimental**:
  - Experimental treatments in clinical trials (with NCT identifiers if available)
    > **Search first:** ClinicalTrials.gov, EU Clinical Trials Register, WHO ICTRP
- **Treatment Outcomes**:
  - Treatment response rates
    > **Search first:** Clinical trial databases, FDA reviews, systematic reviews, PubMed
  - Side effects and adverse events
    > **Search first:** FDA Adverse Event Reporting System (FAERS), MedWatch, PubMed
- **Treatment Strategy**:
  - Treatment algorithms (clinical pathways, decision trees)
    > **Search first:** Clinical practice guidelines, NCCN Guidelines, UpToDate
  - Combination therapies
    > **Search first:** ClinicalTrials.gov, treatment guidelines, PubMed
  - Personalized medicine approaches (genotype-guided treatment)
    > **Search first:** My Cancer Genome, CIViC, PharmGKB, precision medicine databases

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

### 13. Prevention

- **Prevention Levels**:
  - Primary prevention (preventing disease occurrence: vaccination, risk factor modification)
    > **Search first:** CDC, WHO, USPSTF recommendations, Cochrane Library
  - Secondary prevention (early detection and treatment: screening programs, early intervention)
    > **Search first:** USPSTF, CDC screening guidelines, WHO
  - Tertiary prevention (preventing complications in those with disease)
    > **Search first:** Clinical guidelines, disease management protocols, PubMed
- **Immunization**: Vaccine strategies (if applicable)
  > **Search first:** CDC vaccine schedules, WHO immunization, FDA vaccine database
- **Screening and Early Detection**:
  - Screening programs (population-based: newborn screening, cancer screening)
    > **Search first:** CDC screening programs, USPSTF, cancer screening databases
  - Genetic screening (carrier screening, preimplantation genetic diagnosis, prenatal testing)
    > **Search first:** ACMG recommendations, ACOG guidelines, GTR
  - Risk stratification (identifying high-risk individuals for targeted prevention)
    > **Search first:** Risk prediction models, clinical calculators, PubMed
- **Behavioral Interventions**: Lifestyle modifications to reduce risk
  > **Search first:** CDC, WHO, behavioral intervention databases, Cochrane Library
- **Counseling**: Genetic counseling (risk assessment, family planning guidance)
  > **Search first:** NSGC resources, ACMG guidelines, GeneReviews
- **Public Health**:
  - Public health interventions (sanitation, vector control, health education)
    > **Search first:** CDC, WHO, public health databases, PubMed
  - Environmental interventions (reducing environmental risk factors)
    > **Search first:** EPA databases, WHO environmental health, PubMed
- **Prophylaxis**: Preventive medications or procedures
  > **Search first:** Clinical guidelines, FDA approvals, PubMed

### 14. Other Species / Natural Disease

- **Taxonomy**: Species affected (with NCBI Taxon identifiers)
  > **Search first:** NCBI Taxonomy
- **Breed**: Specific breeds affected (with VBO identifiers if applicable)
  > **Search first:** VBO (Vertebrate Breed Ontology)
- **Gene**: Orthologous genes in other species (with NCBI Gene IDs)
  > **Search first:** NCBI Gene
- **Natural Disease**:
  - Naturally occurring disease in other species (companion animals, wildlife)
    > **Search first:** OMIA (Online Mendelian Inheritance in Animals), VetCompass, PubMed
  - Veterinary relevance and importance in animal health
    > **Search first:** OMIA, veterinary databases, PubMed
- **Comparative Biology**:
  - Comparative pathology (similarities and differences across species)
    > **Search first:** OMIA, comparative pathology databases, PubMed
  - Evolutionary conservation of disease mechanisms
    > **Search first:** HomoloGene, OrthoMCL, Alliance of Genome Resources
- **Transmission** (if applicable):
  - Zoonotic potential
    > **Search first:** CDC zoonotic diseases, WHO zoonoses, GIDEON
  - Cross-species susceptibility
    > **Search first:** NCBI Taxonomy, veterinary databases, PubMed

### 15. Model Organisms

- **Model Types**:
  - Model organism type (mammalian, invertebrate, cellular, in vitro)
    > **Search first:** Alliance of Genome Resources, model organism databases
  - Specific model systems (mouse, rat, zebrafish, Drosophila, C. elegans, yeast, cell lines, organoids, iPSCs)
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, SGD, ATCC, Cellosaurus
  - Induced models (drug treatment, surgical intervention, environmental manipulation)
    > **Search first:** MGI, model organism databases, PubMed
- **Genetic Models**:
  - Types available (knockout, knock-in, transgenic, conditional, humanized)
    > **Search first:** MGI, IMPC, KOMP, EuMMCR, IMSR
- **Model Characteristics**:
  - Phenotype recapitulation (how well model reproduces human disease features)
    > **Search first:** Model organism databases, comparative studies, PubMed
  - Model limitations (aspects of human disease not captured)
    > **Search first:** Model organism databases, PubMed, review articles
- **Applications**:
  - Research applications (what aspects of disease can be studied)
    > **Search first:** Model organism databases, PubMed
- **Resources**:
  - Model databases
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, IMSR, EMMA, MMRRC

---

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic and clinical claims
- Prioritize recent reviews and landmark papers
- Include direct quotes from abstracts where possible to support key statements
- Distinguish evidence source types: human clinical, model organism, in vitro, computational

## Output Format

Structure your response as a comprehensive narrative organized by the sections above.
For each section, provide:
- Factual content with specific details (numbers, percentages, gene names, variant nomenclature)
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
- Evidence citations with PMIDs
- Direct quotes from abstracts to support key claims
- Clear indication when information is not available or not applicable for this disease

This report will be used to populate a disease knowledge base entry with:
- Pathophysiology descriptions with causal chains
- Gene/protein annotations (HGNC, GO terms)
- Phenotype associations (HP terms) with frequencies
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# Comprehensive Research Report: Central Serous Chorioretinopathy (CSC)

## 1. Disease Information

### Overview
Central serous chorioretinopathy (CSC/CSCR), first described by Albrecht von Graefe in 1866, is characterized by focal serous detachment of the neural retina and/or retinal pigment epithelium (RPE) in the posterior pole (zhang2023centralserouschorioretinopathy pages 1-2). It is recognized as the first-described pachychoroid spectrum disorder, defined by chronic choroidal thickening and choriocapillaris dysfunction with or without RPE abnormalities overlying pachyvessels (zhang2023centralserouschorioretinopathy pages 1-2). CSC exists in acute and chronic subtypes: acute CSC is typically self-limiting within 2–3 months, while chronic CSC involves persistent subretinal fluid (SRF) beyond 4–6 months with RPE decompensation, potentially leading to permanent visual impairment from photoreceptor damage or RPE atrophy (zhang2023centralserouschorioretinopathy pages 1-2, kim2025treatmentofcentral pages 2-3).

### Disease Identifiers and Classification
The following table summarizes disease identifiers, synonyms, and classification for CSC:

| Disease Name | Synonyms | ICD-10 | ICD-11 | OMIM | MeSH ID | MONDO ID | EFO IDs | Orphanet | Disease Category | First Described |
|---|---|---|---|---|---|---|---|---|---|---|
| Central Serous Chorioretinopathy (CSC, CSCR) | central serous retinopathy; central serous choroidopathy; central serous pigment epitheliopathy; CSCR; CSC (zhang2023centralserouschorioretinopathy pages 1-2) | H35.71 | Not confirmed in retrieved evidence; verify in ICD-11 browser before database ingestion | No established OMIM entry identified in retrieved evidence; generally treated as complex/multifactorial rather than monogenic | D056833 | Not confirmed in retrieved evidence | EFO_0009784 = central serous retinopathy; EFO_0009363 = chronic central serous retinopathy (OpenTargets Search: central serous chorioretinopathy) | Not confirmed in retrieved evidence | Pachychoroid spectrum disorder; complex/multifactorial retinal disease (zhang2023centralserouschorioretinopathy pages 1-2, kim2025treatmentofcentral pages 2-3, zhang2023centralserouschorioretinopathy pages 2-4) | First described by Albrecht von Graefe in 1866 (zhang2023centralserouschorioretinopathy pages 1-2, zhang2023centralserouschorioretinopathy pages 2-4) |


*Table: This table summarizes the main disease identifiers, synonyms, and classification terms for Central Serous Chorioretinopathy. It is useful for harmonizing disease knowledge-base entries across clinical, ontology, and research resources.*

**Synonyms:** Central serous retinopathy, central serous choroidopathy, central serous pigment epitheliopathy, CSCR, CSC (zhang2023centralserouschorioretinopathy pages 1-2).

**Key Ontology Terms:**
- **MONDO:** MONDO:0007381 (central serous retinopathy)
- **EFO:** EFO_0009784 (central serous retinopathy); EFO_0009363 (chronic central serous retinopathy) (OpenTargets Search: central serous chorioretinopathy)
- **ICD-10:** H35.71
- **MeSH:** D056833

---

## 2. Etiology

### Disease Causal Factors
CSC is a complex, multifactorial disease whose precise etiology remains incompletely understood. The pathogenesis involves dysfunction at the choroidal level with hyperpermeability, choriocapillaris remodeling, and RPE barrier breakdown (zhang2023centralserouschorioretinopathy pages 1-2). A "venous overload choroidopathy" hypothesis has recently been proposed, emphasizing morphological and pathological characteristics including choroidal thickening, choriocapillaris hyperpermeability, and intervortex venous anastomoses (ramo2024raregeneticvariation pages 30-33, zhang2023centralserouschorioretinopathy pages 1-2).

### Risk Factors

**Environmental and Lifestyle Risk Factors:**
- **Corticosteroid use** (systemic, nasal, topical, intravenous, and intravitreal routes) — the most consistently identified modifiable risk factor (kim2025treatmentofcentral pages 2-3, zhang2023centralserouschorioretinopathy pages 2-4)
- **Psychological stress and Type A personality** — neuroendocrine activation with catecholamine and corticosteroid release affects choroidal vascular permeability (zhang2023centralserouschorioretinopathy pages 2-4)
- **Sleep apnea** — associated with approximately 5× increased risk (kim2025treatmentofcentral pages 2-3)
- **H. pylori infection** — may increase tissue sensitivity to inflammatory reactions and oxidative stress (zhang2023centralserouschorioretinopathy pages 2-4)
- **Sympathomimetic agents and antipsychotic medications** (kim2025treatmentofcentral pages 2-3)
- **Endogenous hormonal changes** (Cushing syndrome, pregnancy) (kim2025treatmentofcentral pages 2-3)
- **Additional factors:** hypertension, alcohol use, kidney disease (zhang2023centralserouschorioretinopathy pages 2-4)
- **Sleep quality:** CSC patients demonstrate significantly poorer sleep quality (58.2% vs. 23.9% in controls) (zhang2023centralserouschorioretinopathy pages 2-4)

**Genetic Risk Factors:**
CSC has a polygenic, multifactorial inheritance pattern. Multiple genome-wide association studies (GWAS) have identified susceptibility loci, including CFH, PTPRB, TNFRSF10A, GATA5, ARMS2, VIPR2, CDH5, and NR3C2 (mori2025genomewideassociationand pages 2-3, ramo2025raregeneticvariation pages 1-2, mori2025genomewideassociationand pages 11-11). The most significant novel finding is a low-frequency missense variant (rs113791087) in PTPRB encoding vascular endothelial protein tyrosine phosphatase (VE-PTP), with OR = 3.06 (P = 7.4 × 10⁻¹⁵) in a meta-analysis of 2,452 CSC patients and 865,767 controls (ramo2025raregeneticvariation pages 1-2, ramo2024raregeneticvariation pages 1-4).

### Protective Factors
The rs113791087 variant in PTPRB, while conferring CSC risk, was paradoxically associated with reduced risk of glaucoma (OR = 0.82, P = 6.9 × 10⁻⁹), suggesting complex pleiotropic effects of vascular endothelial signaling (ramo2025raregeneticvariation pages 1-2, ramo2024raregeneticvariation pages 1-4). No robust genetic or environmental protective factors have been consistently identified for CSC prevention specifically.

### Gene-Environment Interactions
Corticosteroids have been shown to regulate the expression of CDH5 (cadherin 5), a CSC susceptibility gene, providing a molecular link between environmental corticosteroid exposure and genetic susceptibility (mori2025genomewideassociationand pages 11-11). The mineralocorticoid receptor gene NR3C2 has been associated with chronic CSC susceptibility, and mineralocorticoid receptor antagonists can effectively treat the condition, further linking the glucocorticoid/mineralocorticoid pathway to genetic predisposition (matet2020lipocalin2as pages 6-6, zhang2023centralserouschorioretinopathy pages 2-4).

---

## 3. Phenotypes

### Symptoms and Clinical Signs
CSC presents as a predominantly unilateral condition (bilateral in 5–18% of cases) with the following symptoms (zhang2023centralserouschorioretinopathy pages 4-5):
- **Blurred vision** (HP:0000572)
- **Central scotoma** (HP:0000575)
- **Micropsia** (HP:0012508)
- **Metamorphopsia** (HP:0012507)
- **Reduced contrast sensitivity** (HP:0030452)

**HPO Terms:**
- HP:0000572 Visual loss
- HP:0007401 Macular atrophy
- HP:0011506 Choroidal neovascularization
- HP:0000580 Pigmentary retinopathy
- HP:0001103 Subretinal fluid

### Phenotype Characteristics
- **Age of onset:** Predominantly middle-aged adults aged 30–50 years (zhang2023centralserouschorioretinopathy pages 1-2, ramo2024raregeneticvariation pages 1-4)
- **Severity:** Variable from mild self-limited acute episodes to severe chronic disease with legal blindness (12.8% developing legal blindness after mean 11.3-year follow-up in chronic CSC) (mori2025genomewideassociationand pages 1-2)
- **Progression:** Episodic in acute CSC; progressive in chronic CSC with RPE atrophy and photoreceptor deterioration (zhang2023centralserouschorioretinopathy pages 5-7)
- **Frequency:** Men account for 72–87.5% of patients (zhang2023centralserouschorioretinopathy pages 1-2)

### Quality of Life Impact
Patients with CSC demonstrate significantly poorer sleep quality (58.2% vs. 23.9% in controls) and higher prevalence of stress, depression, and anxiety compared to healthy controls (zhang2023centralserouschorioretinopathy pages 2-4). Vision loss, metamorphopsia, and central scotoma significantly impact daily functioning, particularly for individuals of working age.

---

## 4. Genetic/Molecular Information

### Susceptibility Genes and GWAS Findings
A meta-analysis of three GWAS comprising 8,811 Asians and Caucasians with replication in 4,338 additional Asians identified seven genome-wide significant loci (mori2025genomewideassociationand pages 2-3, mori2025genomewideassociationand pages 1-2). The most comprehensive genetic findings are summarized in the following table:

| Gene/Locus | Variant/SNP | Chromosome | Odds Ratio | P-value | Population studied | Reference |
|---|---|---:|---:|---:|---|---|
| **PTPRB / VE-PTP** | **rs113791087** (missense; low-frequency AF ~0.5%) | 12q15 | **2.85** (FinnGen); **3.06** in 4-study meta-analysis | **4.5×10⁻⁹**; **7.4×10⁻¹⁵** | FinnGen: 1,477 CSC cases, 455,449 controls; meta-analysis: 2,452 cases, 865,767 controls across 4 studies | Rämö et al. 2025 (ramo2025raregeneticvariation pages 1-2, ramo2024raregeneticvariation pages 1-4) |
| **CFH** | Lead SNP not specified in retrieved context; prior/common noncoding risk locus | 1q31.3 | NR in retrieved context | Genome-wide significant in prior GWAS/meta-GWAS | Europeans; Asians and Caucasians in later meta-GWAS | Mori et al. 2025; Open Targets CSC association (mori2025genomewideassociationand pages 2-3, mori2025genomewideassociationand pages 1-2, mori2025genomewideassociationand pages 10-11, chen2026thecfh–cfhr5locus pages 10-10, OpenTargets Search: central serous chorioretinopathy) |
| **TNFRSF10A–TNFRSF10A-DT** | Lead SNP not specified in retrieved context | 8p21.3 | NR in retrieved context | Genome-wide significant in prior GWAS and 2025 meta-GWAS | Japanese in earlier GWAS; multi-ethnic Asians/Caucasians in meta-GWAS | Mori et al. 2025; Open Targets CSC association (mori2025genomewideassociationand pages 1-2, mori2025genomewideassociationand pages 10-11, OpenTargets Search: central serous chorioretinopathy) |
| **RBBP8NL–GATA5** | Lead SNP not specified in retrieved context | 20q13.33 | NR in retrieved context | Genome-wide significant in prior GWAS/meta-GWAS | Japanese in earlier GWAS; multi-ethnic Asians/Caucasians in meta-GWAS | Mori et al. 2025 (mori2025genomewideassociationand pages 2-3, mori2025genomewideassociationand pages 1-2, mori2025genomewideassociationand pages 10-11) |
| **SLC7A5** | Lead SNP not specified in retrieved context | NR | NR in retrieved context | Reported susceptibility locus in earlier GWAS | Japanese | Mori et al. 2025 (mori2025genomewideassociationand pages 2-3, mori2025genomewideassociationand pages 1-2) |
| **LINC01924–CDH7** | **rs12960630** | NR | NR in retrieved context | **2.97×10⁻⁹** (meta-analysis) | Meta-analysis of 8,811 Asians and Caucasians; replication in 4,338 additional Asians | Mori et al. 2025 (mori2025genomewideassociationand pages 1-2, mori2025genomewideassociationand pages 10-11) |
| **CD34 / CD46 locus** | Lead SNP not specified in retrieved context | NR | NR in retrieved context | Reported susceptibility locus in earlier GWAS; CD46 also present among genome-wide significant loci in PTPRB study background | Earlier GWAS populations not fully specified in retrieved context; later CSC studies include Europeans and Asians | Mori et al. 2025; Rämö et al. 2025 (mori2025genomewideassociationand pages 2-3, ramo2025raregeneticvariation pages 1-2) |
| **NOTCH4** | Lead SNP not specified in retrieved context | NR | NR in retrieved context | Reported susceptibility locus in earlier GWAS | Earlier GWAS population not fully specified in retrieved context | Mori et al. 2025 (mori2025genomewideassociationand pages 2-3) |
| **ARMS2** | Specific variant not specified in retrieved context | 10q26 | NR in retrieved context | Associated/risk locus reported; shared architecture with AMD discussed | Reported in CSC genetic literature; ethnicity-specific details not fully specified in retrieved context | Zhang et al. 2023; Chen et al. 2026 discussion of shared AMD/CSC architecture (zhang2023centralserouschorioretinopathy pages 2-4, chen2026thecfh–cfhr5locus pages 10-10) |
| **CDH5** | Specific variant not specified in retrieved context | 16q22.1 | NR in retrieved context | Susceptibility gene reported in CSC literature | Population not specified in retrieved context | Mori et al. 2025 (mori2025genomewideassociationand pages 11-11) |
| **VIPR2** | Specific variant not specified in retrieved context | 7q36.3 | NR in retrieved context | Susceptibility locus associated with choroidal thickness/pachychoroid-related CSC | Population not specified in retrieved context; ethnicity-specific effects discussed in related literature | Mori et al. 2025; Chen et al. 2026 (mori2025genomewideassociationand pages 11-11, chen2026thecfh–cfhr5locus pages 10-10) |
| **NR3C2** | Specific variant not specified in retrieved context | 4q31.23 | NR in retrieved context | Susceptibility gene reported for chronic CSC | Population not specified in retrieved context | Mori et al. 2025; biomarker/pathogenesis review context (mori2025genomewideassociationand pages 11-11, matet2020lipocalin2as pages 6-6) |
| **CFH–CFHR5 locus** | **CFH rs1329428** | 1q31.3 | NR in retrieved context | Significant association with chronic CSC with macular neovascularization | Population in retrieved context not fully specified | Chen et al. 2026 (chen2026thecfh–cfhr5locus pages 8-9) |


*Table: This table summarizes the main genetic susceptibility loci reported for central serous chorioretinopathy, emphasizing loci supported by recent GWAS and multi-omics work. It is useful for quickly distinguishing loci with quantified effect sizes from those currently reported mainly as significant associations without effect estimates in the retrieved evidence.*

Key findings include:
- **CFH (complement factor H, 1q31.3):** A major susceptibility locus with 26 CFH- or CFHR-related pathways showing significant associations, indicating the complement pathway's importance in CSC pathogenesis (mori2025genomewideassociationand pages 2-3, chen2026thecfh–cfhr5locus pages 10-10). OpenTargets identifies CFH as the highest-scoring disease-target association (score 0.485) for central serous retinopathy (OpenTargets Search: central serous chorioretinopathy).
- **PTPRB (VE-PTP, 12q15):** The novel rs113791087 missense variant (allele frequency 0.5%) shows OR = 3.06 in meta-analysis. Predicted loss-of-function variants showed even stronger association (OR = 17.09, P = 0.018) (ramo2025raregeneticvariation pages 1-2, ramo2024raregeneticvariation pages 1-4).
- **TNFRSF10A (8p21.3):** TNF receptor superfamily member 10a, identified in Japanese GWAS and replicated across populations. OpenTargets association score 0.364 (OpenTargets Search: central serous chorioretinopathy, mori2025genomewideassociationand pages 2-3).
- **LINC01924-CDH7 (rs12960630):** Novel locus showing positive correlation between CSC risk allele and plasma cortisol concentration (mori2025genomewideassociationand pages 1-2).

### Multi-Omics Insights
Expression/splicing quantitative trait loci (QTL) analyses showed association of identified GWAS hits with expression and/or splicing of genes in genital organs, potentially explaining the sex differences in CSC (mori2025genomewideassociationand pages 1-2). Protein QTL analysis suggested protein-level contribution of the complement factor H pathway to CSC pathogenesis (mori2025genomewideassociationand pages 1-2).

### Epigenetic Information
Limited epigenetic data are available specifically for CSC. The mineralocorticoid receptor pathway and glucocorticoid-responsive gene regulation (including CDH5) suggest corticosteroid-mediated transcriptional changes may contribute to disease susceptibility (mori2025genomewideassociationand pages 11-11).

---

## 5. Environmental Information

### Environmental Factors
Corticosteroid exposure remains the most well-documented environmental trigger. Among corticosteroid users in South Korea (2011–2015), CSC prevalence was 9.4 per 10,000 in men and 3.0 per 10,000 in women (zhang2023centralserouschorioretinopathy pages 2-4). Corticosteroid-treated patients experience higher recurrence rates and more severe disease features including bilateral involvement, multiple pigment epithelial detachments, greater fluorescein leakage sites, and increased choroidal thickness (zhang2023centralserouschorioretinopathy pages 2-4).

### Lifestyle Factors
Depression is associated with increased risk of recurrent CSC (zhang2023centralserouschorioretinopathy pages 2-4). Sleep disorders, psychological stress, and Type A personality are consistently identified environmental contributors to disease onset and recurrence (kim2025treatmentofcentral pages 2-3, zhang2023centralserouschorioretinopathy pages 2-4).

### Infectious Agents
H. pylori infection has been associated with CSC, potentially through increasing tissue sensitivity to inflammatory reactions triggered by oxidative stress and reducing cellular antioxidant capacity (zhang2023centralserouschorioretinopathy pages 2-4).

---

## 6. Mechanism/Pathophysiology

### Molecular Pathways
The pathophysiology of CSC involves multiple interconnected pathways:

1. **Choroidal vascular dysfunction:** Dysautoregulation of choroidal circulation leads to hyperpermeability and fluid accumulation beneath the RPE (zhang2023centralserouschorioretinopathy pages 4-5). Choroidal changes include higher vascularity index, enlarged vessels, and increased choroidal thickness (kim2025treatmentofcentral pages 2-3). **GO terms:** GO:0045766 (positive regulation of angiogenesis), GO:0001974 (blood vessel remodeling).

2. **Complement factor H pathway:** Protein QTL analysis and GWAS data implicate the CFH-CFHR pathway in CSC pathogenesis. FHR proteins compete with factor H in complement regulation through the alternative complement pathway (chen2026thecfh–cfhr5locus pages 8-9, mori2025genomewideassociationand pages 2-3). **GO term:** GO:0006956 (complement activation).

3. **Vascular endothelial phosphatase (VE-PTP) dysfunction:** PTPRB variants alter vascular endothelial signaling, and abnormal choroidal veins in CSC patients share morphological similarities with varicose veins, supporting a "venous overload choroidopathy" hypothesis (ramo2025raregeneticvariation pages 1-2, ramo2024raregeneticvariation pages 30-33).

4. **Mineralocorticoid receptor pathway:** High levels of glucocorticoids, mineralocorticoids, and testosterone are found in CSC patients. The mineralocorticoid receptor pathway contributes to RPE and choroidal dysfunction (zhang2023centralserouschorioretinopathy pages 2-4, matet2020lipocalin2as pages 6-6).

5. **Neuroendocrine activation:** Psychological stress activates the neuroendocrine system with catecholamine and corticosteroid release, affecting choroidal vascular permeability (zhang2023centralserouschorioretinopathy pages 2-4).

### Cellular Processes
- **RPE barrier dysfunction:** Glucocorticoids alter RPE, Bruch's membrane, and choriocapillaris permeability (zhang2023centralserouschorioretinopathy pages 2-4). **CL term:** CL:0002586 (retinal pigment epithelial cell).
- **Oxidative stress susceptibility:** Decreased lipocalin 2 (LCN2) in CSC patients contributes to excessive oxidative stress and RPE barrier dysfunction. LCN2 normally enhances antioxidant enzyme expression (HMOX1 and SOD2) in RPE cells (matet2020lipocalin2as pages 5-6, matet2020lipocalin2as pages 1-2, matet2020lipocalin2as pages 2-3). **GO term:** GO:0006979 (response to oxidative stress).
- **Inflammation:** LCN2 suppresses ocular inflammation through NF-κB pathway inhibition; its deficiency may promote innate immune dysregulation (matet2020lipocalin2as pages 6-6, matet2020lipocalin2as pages 1-2).
- **Choroidal congestion:** Dilation of outer choroidal vessels (Haller's layer) with attenuation of inner layers (Sattler's layer and choriocapillaris) (zhang2023centralserouschorioretinopathy pages 4-5).

### Biomarkers
- **Lipocalin 2 (LCN2/NGAL):** Serum LCN2 is significantly lower in CSC patients than controls (81.4 ± 48.7 vs. 107.3 ± 44.5 ng/ml, p < 0.0001). An 80 ng/ml cutoff discriminates acute/recurrent CSC from controls with 80.3% sensitivity and 75.8% specificity (matet2020lipocalin2as pages 3-5, matet2020lipocalin2as pages 1-2).
- **NGAL/MMP-9 complex:** Lower in CSC patients (47.2 ± 40.7 vs. 74.1 ± 42.6 ng/ml, p < 0.0001). A 38 ng/ml cutoff provides 69.6% sensitivity and 80.3% specificity (matet2020lipocalin2as pages 3-5).
- **Plasma cortisol:** The novel CSC risk allele at rs12960630 (LINC01924-CDH7) shows positive correlation with plasma cortisol concentration (mori2025genomewideassociationand pages 1-2).

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary organ:** Eye (UBERON:0000970)
- **Specific structure:** Macula lutea (UBERON:0000053), posterior pole of the eye
- **Body system:** Visual system

### Tissue and Cell Level
- **Retina** (UBERON:0000966): Neural retina with serous detachment
- **Retinal pigment epithelium** (CL:0002586): RPE dysfunction, atrophy, hyperplasia, and barrier breakdown (zhang2023centralserouschorioretinopathy pages 5-7, zhang2023centralserouschorioretinopathy pages 4-5)
- **Choroid** (UBERON:0001776): Thickened with dilated vessels in Haller's layer, attenuated Sattler's layer and choriocapillaris (zhang2023centralserouschorioretinopathy pages 7-10, zhang2023centralserouschorioretinopathy pages 4-5)
- **Choriocapillaris** (UBERON:0002208): Hyperpermeability and attenuation (kim2025treatmentofcentral pages 3-5)
- **Photoreceptors** (CL:0000210): Outer segment elongation, ellipsoidal band disruption correlating with visual acuity loss (zhang2023centralserouschorioretinopathy pages 7-10)

### Localization
- Predominantly unilateral; bilateral in 5–18% of cases (zhang2023centralserouschorioretinopathy pages 4-5)
- Posterior pole/macular region preferentially affected
- Subretinal fluid accumulation beneath neurosensory retina

---

## 8. Temporal Development

### Onset
- **Typical age:** 30–50 years (zhang2023centralserouschorioretinopathy pages 1-2, ramo2024raregeneticvariation pages 1-4)
- **Onset pattern:** Acute, often related to stress or corticosteroid exposure

### Progression
- **Acute CSC:** Self-limiting in approximately 90–95% of cases with spontaneous SRF resorption within 2–3 months; expected visual recovery to 20/20 or better (zhang2023centralserouschorioretinopathy pages 10-12, zhang2023centralserouschorioretinopathy pages 1-2)
- **Chronic CSC:** Persistent SRF >4–6 months with progressive RPE decompensation (kim2025treatmentofcentral pages 2-3)
- **Risk factors for chronicity:** Subfoveal choroidal thickness >500 µm, PED height >50 µm, age >40 years (kim2025treatmentofcentral pages 2-3)
- **Recurrence rates:** 15–50% depending on study methodology and follow-up duration; 19–51% in various series (kim2025treatmentofcentral pages 2-3, zhang2023centralserouschorioretinopathy pages 5-7)
- **Complications:** Choroidal neovascularization (CNV) in 2–15.6% of chronic CSC cases; RPE atrophy; photoreceptor loss (zhang2023centralserouschorioretinopathy pages 5-7, kim2025treatmentofcentral pages 3-5)

### Disease Course Patterns
- Episodic/relapsing in acute form
- Progressive with accumulating damage in chronic form
- Critical period: Decision to treat typically at 3–4 months if SRF persists (zhang2023centralserouschorioretinopathy pages 10-12)

---

## 9. Inheritance and Population

### Epidemiology
- **Annual incidence:** Approximately 5.8–10 per 100,000 (age-adjusted); approximately 10 per 100,000 in men (zhang2023centralserouschorioretinopathy pages 1-2, ramo2024raregeneticvariation pages 1-4)
- **Prevalence:** Among corticosteroid users in South Korea: 9.4 per 10,000 in men, 3.0 per 10,000 in women (zhang2023centralserouschorioretinopathy pages 2-4)

### Inheritance Pattern
CSC is a complex/multifactorial disease with polygenic susceptibility rather than Mendelian inheritance. Multiple common and rare genetic variants contribute to disease risk (mori2025genomewideassociationand pages 2-3, ramo2025raregeneticvariation pages 1-2).

### Population Demographics
- **Sex ratio:** Males represent 72–87.5% of patients; however, older women show similar prevalence rates to men (zhang2023centralserouschorioretinopathy pages 1-2)
- **Racial/ethnic distribution:** More prevalent in Asians compared to Caucasians and African Americans (zhang2023centralserouschorioretinopathy pages 2-4, zhang2023centralserouschorioretinopathy pages 1-2)
- **Age distribution:** Peak incidence at 30–50 years of age (zhang2023centralserouschorioretinopathy pages 1-2, ramo2024raregeneticvariation pages 1-4)
- **Geographic variant distribution:** The PTPRB rs113791087 variant has a low frequency of 0.5% (enriched in FinnGen/Finnish population) (ramo2025raregeneticvariation pages 1-2, ramo2024raregeneticvariation pages 1-4)

---

## 10. Diagnostics

### Clinical Tests and Imaging

**Optical Coherence Tomography (OCT):** The primary diagnostic modality, revealing SRF accumulation, pigment epithelial detachment (PED), increased subfoveal choroidal thickness, dilated vessels in Haller's layer, thinning of Sattler's layer, choriocapillaris attenuation, photoreceptor outer segment elongation, and ellipsoidal band disruption (zhang2023centralserouschorioretinopathy pages 5-7, zhang2023centralserouschorioretinopathy pages 7-10, zhang2023centralserouschorioretinopathy pages 4-5).

**Fluorescein Angiography (FA):** Demonstrates characteristic leakage patterns — "ink-blot" pattern in 53–93% and "smoke-stack" pattern in approximately 7% of acute cases; multifocal diffuse leakage in chronic CSC (zhang2023centralserouschorioretinopathy pages 5-7).

**Indocyanine Green Angiography (ICGA):** Shows delayed choroidal filling, dilation of large choroidal veins, and multifocal hyperfluorescence indicating choroidal hyperpermeability — present in 93% of CSC patients (zhang2023centralserouschorioretinopathy pages 5-7, kim2025treatmentofcentral pages 3-5).

**OCT Angiography (OCTA):** Reveals abnormal choriocapillaris dilation, high signal intensity areas, and surrounding hyperperfusion patterns indicating focal choroidal ischemia; useful for detecting type 1 CNV (zhang2023centralserouschorioretinopathy pages 7-10, kim2025treatmentofcentral pages 11-11).

**Fundus Autofluorescence (FAF):** Shows hyperautofluorescence (RPE dysfunction) or hypoautofluorescence (atrophic areas); "fluid tracks" visible in chronic CSC (kim2025treatmentofcentral pages 3-5, zhang2023centralserouschorioretinopathy pages 10-12).

**Advanced Modalities:** Ultra-widefield imaging, flavoprotein fluorescence (FPF), fluorescence lifetime imaging ophthalmoscopy (FLIO), multispectral imaging, and multicolor imaging are emerging diagnostic tools (zhang2023centralserouschorioretinopathy pages 1-2, zhang2023centralserouschorioretinopathy pages 10-12).

### Artificial Intelligence in Diagnosis
Deep learning models, particularly CNN architectures (DenseNet, ResNet-50, VGG-16), have demonstrated exceptional performance in automated CSC diagnosis from OCT images, with DenseNet achieving 99.78% accuracy, 99.68% sensitivity, and 100% specificity (shojaeinia2025acomprehensiveoverview pages 1-2). AI-based systems can also differentiate acute from chronic CSC subtypes (94.2% accuracy), predict treatment persistence, forecast treatment response, and estimate post-treatment visual acuity (shojaeinia2025acomprehensiveoverview pages 14-16, shojaeinia2025acomprehensiveoverview pages 13-14, shojaeinia2025acomprehensiveoverview pages 8-9).

### Biomarker-Based Diagnostics
Serum LCN2 (cutoff 80 ng/ml) and NGAL/MMP-9 complex (cutoff 38 ng/ml) represent potential systemic biomarkers for CSC diagnosis (matet2020lipocalin2as pages 3-5).

### Differential Diagnosis
Key conditions to differentiate include: age-related macular degeneration (AMD), polypoidal choroidal vasculopathy (PCV), diabetic macular edema (DME), choroidal neovascularization from other causes, and Vogt-Koyanagi-Harada disease.

---

## 11. Outcome/Prognosis

### Visual Outcomes
- **Acute CSC:** Favorable prognosis with 90–95% spontaneous resolution and expected recovery to ≥20/20 vision (zhang2023centralserouschorioretinopathy pages 10-12, zhang2023centralserouschorioretinopathy pages 1-2)
- **Chronic CSC:** 12.8% develop legal blindness after mean 11.3-year follow-up (mori2025genomewideassociationand pages 1-2); with half-dose PDT treatment, approximately 95% achieve visual acuity of 20/30 or better (zhang2023centralserouschorioretinopathy pages 1-2)

### Recurrence and Complications
- Recurrence rates: 15–50% overall; untreated patients 51% vs. 25% in PDT-treated patients in acute CSC (kim2025treatmentofcentral pages 2-3, kim2025treatmentofcentral pages 8-9)
- CNV develops in 2–15.6% of chronic cases (zhang2023centralserouschorioretinopathy pages 5-7, kim2025treatmentofcentral pages 3-5)
- Progressive RPE atrophy, photoreceptor deterioration, and ganglion cell loss contribute to long-term morbidity (zhang2023centralserouschorioretinopathy pages 5-7)

### Prognostic Factors
Poor prognostic indicators include persistent SRF >3–4 months, subfoveal choroidal thickness >500 µm, PED height >50 µm, age >40 years, bilateral involvement, and corticosteroid use (kim2025treatmentofcentral pages 2-3, zhang2023centralserouschorioretinopathy pages 2-4).

---

## 12. Treatment

The following table summarizes current and experimental treatment modalities for CSC:

| Treatment | Mechanism | Indication/Subtype | Efficacy (SRF resolution rate, VA outcome) | Key Clinical Trials | Level of Evidence/Recommendation |
|---|---|---|---|---|---|
| Half-dose verteporfin photodynamic therapy (PDT) | Reduces choroidal hyperpermeability and induces choriocapillaris vascular remodeling, decreasing leakage and pachychoroid-driven fluid accumulation | Best-supported treatment for chronic CSC; also considered in acute CSC when rapid recovery is needed, in recurrent disease, or single seeing eye | Chronic CSC: ~95% achieve VA 20/30 or better in review-level summary; SRF resolution 91% at 19 months and 81% at 50 months; recurrence reduced to ~20% vs 53.8% with observation; faster SRF and retinal sensitivity recovery than no treatment (zhang2023centralserouschorioretinopathy pages 1-2, kim2025treatmentofcentral pages 8-9) | PLACE trial; SPECTRA trial (zhang2023centralserouschorioretinopathy pages 19-20, kim2025treatmentofcentral pages 12-13) | Highest current evidence; treatment of choice/mainstay for chronic CSC in recent expert reviews and consensus-style guidance (kim2025treatmentofcentral pages 9-10, kim2025treatmentofcentral pages 8-9, zhang2023centralserouschorioretinopathy pages 1-2) |
| Half-fluence PDT | Same core PDT effect with reduced laser fluence to limit adverse effects while maintaining choroidal remodeling | Alternative reduced-setting PDT for chronic CSC; sometimes used in acute CSC | Effective and broadly comparable to half-dose PDT in review summaries; early treatment may speed fluid resolution and visual recovery, but half-dose has the strongest supporting data (zhang2023centralserouschorioretinopathy pages 14-15, kim2025treatmentofcentral pages 8-9) | Comparative PDT studies referenced in reviews; PLACE-related comparative context (zhang2023centralserouschorioretinopathy pages 14-15, zhang2023centralserouschorioretinopathy pages 19-20) | Strong evidence, but generally considered slightly less established than half-dose PDT as preferred regimen (kim2025treatmentofcentral pages 8-9, zhang2023centralserouschorioretinopathy pages 1-2) |
| Eplerenone / spironolactone | Mineralocorticoid receptor antagonism targeting corticosteroid/mineralocorticoid pathway implicated in CSC | Chronic CSC when PDT is unavailable/contraindicated; historically used off-label | Evidence mixed to negative for routine use: VICI showed eplerenone failed primary BCVA outcome at 12 months in chronic CSC; some smaller studies suggested anatomical benefit, but overall efficacy remains controversial (kim2025treatmentofcentral pages 9-10, zhang2023centralserouschorioretinopathy pages 1-2) | VICI trial; SPECTRA trial (direct comparison with half-dose PDT) (zhang2023centralserouschorioretinopathy pages 19-20, kim2025treatmentofcentral pages 12-13) | Moderate/low certainty for routine care; not preferred over PDT in current reviews (kim2025treatmentofcentral pages 9-10, zhang2023centralserouschorioretinopathy pages 1-2) |
| Anti-VEGF intravitreal therapy (bevacizumab, ranibizumab, aflibercept) | Suppresses VEGF-driven neovascular leakage | CSC complicated by type 1 CNV / macular neovascularization; not standard for uncomplicated CSC | Standard and effective for CSC with active CNV; meta-analysis did not confirm efficacy in acute CSC without CNV; aflibercept trial showed better BCVA gain than sham, and ranibizumab was inferior to low-fluence PDT anatomically in non-CNV settings (kim2025treatmentofcentral pages 9-9, zhang2023centralserouschorioretinopathy pages 14-15) | MINERVA trial; aflibercept randomized study referenced in review (kim2025treatmentofcentral pages 9-10, kim2025treatmentofcentral pages 9-9) | Strong recommendation only when CNV is present; not recommended as routine monotherapy for non-neovascular CSC (kim2025treatmentofcentral pages 9-10, kim2025treatmentofcentral pages 9-9) |
| Focal laser photocoagulation | Seals focal extrafoveal leakage sites | Acute or chronic CSC with extrafoveal focal leakage on FA/ICGA | May accelerate fluid resolution; some long-term studies suggest fewer recurrences and better 5-year VA than observation, but does not address underlying choroidal disease and may not reduce recurrence in all studies (kim2025treatmentofcentral pages 9-10, kim2025treatmentofcentral pages 7-8) | Older comparative laser vs observation studies summarized in reviews (kim2025treatmentofcentral pages 7-8) | Reasonable for selected extrafoveal leakage; inferior to PDT for chronic subfoveal disease (kim2025treatmentofcentral pages 9-10, zhang2023centralserouschorioretinopathy pages 1-2) |
| Subthreshold micropulse laser (e.g., 577 nm HSML) | Delivers sublethal retinal laser energy with minimal tissue damage, aiming to stimulate RPE pump function | Chronic CSC, especially when PDT unavailable, leakage is juxtafoveal/extrafoveal, or extensive RPE damage limits other options | Complete SRF resolution reported in 36-100% across studies; one review cites 41% in focal leakage and 21% in diffuse leakage chronic CSC; PLACE trial showed inferiority to half-dose PDT for chronic CSC (kim2025treatmentofcentral pages 7-8, kim2025treatmentofcentral pages 8-9, zhang2023centralserouschorioretinopathy pages 14-15) | PLACE trial; multiple HSML studies summarized in reviews (zhang2023centralserouschorioretinopathy pages 14-15, kim2025treatmentofcentral pages 12-13) | Moderate evidence; useful alternative but generally less effective than half-dose PDT for chronic CSC (zhang2023centralserouschorioretinopathy pages 14-15, kim2025treatmentofcentral pages 8-9) |
| Rifampicin | Alters glucocorticoid metabolism, potentially reducing corticosteroid-mediated CSC activity | Selected patients unsuitable for invasive treatment; off-label systemic therapy | Limited evidence for anatomical/clinical improvement in some studies; safety limited by need for hepatotoxicity monitoring (zhang2023centralserouschorioretinopathy pages 14-15, zhang2023centralserouschorioretinopathy pages 19-20) | Small non-pivotal studies referenced in reviews (zhang2023centralserouschorioretinopathy pages 14-15, kim2025treatmentofcentral pages 12-13) | Low-quality evidence; experimental/off-label adjunct rather than standard care (zhang2023centralserouschorioretinopathy pages 14-15) |
| Mifepristone / finasteride | Hormonal pathway modulation: glucocorticoid/progesterone receptor antagonism (mifepristone) or androgen pathway modulation (finasteride) | Experimental/off-label use in CSC linked to endocrine/hormonal mechanisms | Insufficient robust efficacy data in recent reviews; discussed as potential options rather than established therapies (kim2025treatmentofcentral pages 12-13) | Small exploratory studies referenced in review literature (kim2025treatmentofcentral pages 12-13) | Low-quality evidence; not standard recommendation (kim2025treatmentofcentral pages 12-13) |
| Melatonin | Proposed neurohormonal/chronobiologic and antioxidant effects; possible modulation of stress-related pathways | Experimental; acute CSC under investigation | No established efficacy in retrieved review evidence; ongoing phase 2/3 trial identified (NCT06809751) (OpenTargets Search: central serous chorioretinopathy) | NCT06809751 (not yet recruiting) (OpenTargets Search: central serous chorioretinopathy) | Investigational; insufficient evidence for routine use (OpenTargets Search: central serous chorioretinopathy) |
| Observation / risk-factor modification | Allows spontaneous resolution while removing triggers (especially corticosteroids and stress-related factors) | First-line for many acute CSC cases without severe visual demands or chronicity | Acute CSC: ~90-95% spontaneously resolve; however recurrence remains substantial, and untreated eyes show higher recurrence than PDT-treated eyes in comparative studies (zhang2023centralserouschorioretinopathy pages 10-12, kim2025treatmentofcentral pages 8-9) | Observation comparator arms in PDT studies; natural history data summarized in reviews (kim2025treatmentofcentral pages 8-9, zhang2023centralserouschorioretinopathy pages 10-12) | Appropriate initial strategy for typical acute CSC; not preferred for persistent/chronic disease (kim2025treatmentofcentral pages 9-10, zhang2023centralserouschorioretinopathy pages 10-12) |


*Table: This table summarizes current treatment options for central serous chorioretinopathy, including mechanisms, indications, comparative efficacy, and the strength of supporting evidence. It is useful for quickly distinguishing standard-of-care therapies such as half-dose PDT from conditional, off-label, or investigational options.*

### Key Treatment Details

**Half-Dose Photodynamic Therapy (PDT):** The mainstay of treatment for chronic CSC, with SRF resolution rates of 91% at 19 months and 81% at 50 months follow-up. PDT reduces recurrence risk to approximately 20% compared to 53.8% with observation alone over ≥3-year follow-up (kim2025treatmentofcentral pages 8-9). PDT works through choriocapillaris vascular remodeling and decreased choroidal hyperpermeability (zhang2023centralserouschorioretinopathy pages 1-2). **MAXO term:** MAXO:0000127 (phototherapy).

**Mineralocorticoid Receptor Antagonists (Eplerenone/Spironolactone):** The randomized VICI trial showed eplerenone failed to meet its primary endpoint of improving BCVA at 12 months in chronic CSC, making its routine use controversial (kim2025treatmentofcentral pages 9-10, zhang2023centralserouschorioretinopathy pages 1-2). **MAXO term:** MAXO:0000010 (pharmacotherapy).

**Anti-VEGF Therapy:** Standard treatment specifically for CSC complicated by active choroidal neovascularization (type 1 CNV), supported by the MINERVA trial. Not effective as monotherapy for uncomplicated CSC (kim2025treatmentofcentral pages 9-10, kim2025treatmentofcentral pages 9-9). **MAXO term:** MAXO:0001298 (intravitreal injection).

**Subthreshold Micropulse Laser:** Complete SRF resolution in 36–100% of chronic CSC patients across studies; the PLACE trial showed inferiority to half-dose PDT (kim2025treatmentofcentral pages 7-8, zhang2023centralserouschorioretinopathy pages 14-15).

**Focal Laser Photocoagulation:** Appropriate for extrafoveal leakage points identified on FA/ICGA (kim2025treatmentofcentral pages 9-10, kim2025treatmentofcentral pages 7-8). **MAXO term:** MAXO:0010022 (laser photocoagulation).

### Active Clinical Trials
Current recruiting trials include studies evaluating gut microbiota associations (NCT06527326), micropulse laser treatment (NCT06346405), choroidal blood flow assessment (NCT05589974), and subthreshold nanosecond laser (NCT05570591). A phase 2/3 trial evaluating oral melatonin for acute CSC (NCT06809751) is not yet recruiting.

---

## 13. Prevention

### Primary Prevention
- **Corticosteroid avoidance/minimization:** The most important modifiable risk factor. Discontinuation of corticosteroids (oral, inhaled, nasal, topical) is recommended when possible (kim2025treatmentofcentral pages 2-3, zhang2023centralserouschorioretinopathy pages 2-4)
- **Stress management:** Given the strong association with psychological stress and Type A personality, stress reduction strategies may reduce onset and recurrence risk (zhang2023centralserouschorioretinopathy pages 2-4)
- **Sleep disorder management:** Treatment of obstructive sleep apnea (5× increased risk) may be preventive (kim2025treatmentofcentral pages 2-3)

### Secondary Prevention
- **Risk factor modification:** Corticosteroid discontinuation and stress reduction can enhance vision recovery in acute CSC (zhang2023centralserouschorioretinopathy pages 10-12)
- **Early treatment:** Early half-dose PDT for recurrent or non-resolving cases reduces recurrence from 24% to 4% (kim2025treatmentofcentral pages 8-9)

### Tertiary Prevention
- **Monitoring for CNV:** Regular OCT/OCTA follow-up for chronic CSC patients to detect type 1 CNV early (kim2025treatmentofcentral pages 3-5)
- **Appropriate treatment escalation:** Transition from observation to PDT treatment when SRF persists >3–4 months (zhang2023centralserouschorioretinopathy pages 10-12)

### Genetic Counseling
CSC is a complex, multifactorial disease without a defined Mendelian inheritance pattern. While genetic risk factors have been identified (particularly CFH, PTPRB), genetic counseling is not routinely recommended as no single gene drives disease (mori2025genomewideassociationand pages 2-3, ramo2025raregeneticvariation pages 1-2).

---

## 14. Other Species / Natural Disease

### Animal Models
Several animal models have been developed to study CSC pathogenesis:

- **Aldosterone-induced rat model:** Melatonin has been shown to prevent experimental CSC in rats treated with aldosterone, supporting the mineralocorticoid receptor pathway in pathogenesis (Yu et al. 2022, doi:10.1111/jpi.12802)
- **Choroidal congestion mouse model:** Matsumoto et al. (2021) developed a choroidal congestion model as a potential pachychoroid model (doi:10.1371/journal.pone.0246115)
- **Adrenaline-induced chinchilla rabbit model:** Intravenous adrenaline injection produces temporal topographic changes mimicking CSC features (Yan et al. 2023, doi:10.2147/dddt.s381957)
- **Adenosine A2A receptor antagonist model:** KW6002 has been shown to mitigate aldosterone-induced CSC in mice (Liu et al. 2026, doi:10.1016/j.neuropharm.2026.111036)

These models recapitulate aspects of choroidal thickening, subretinal fluid accumulation, and RPE dysfunction but do not fully reproduce the complex multifactorial nature of human CSC.

---

## 15. Model Organisms

### Available Models
- **Rat (Rattus norvegicus, NCBI Taxon:10116):** Aldosterone-induced model showing subretinal fluid and RPE changes
- **Mouse (Mus musculus, NCBI Taxon:10090):** Choroidal congestion model; adenosine receptor-related models
- **Rabbit (Oryctolagus cuniculus, NCBI Taxon:9986):** Adrenaline-induced model

### Model Limitations
Current models primarily address individual pathogenic mechanisms (hormonal, vascular congestion) rather than the full spectrum of genetic susceptibility, complement pathway involvement, and chronic disease features seen in human CSC. No transgenic or knockout models specifically targeting CSC susceptibility genes (CFH, PTPRB, TNFRSF10A) have been reported in the retrieved literature.

---

## Summary of Key Ontology Annotations

**Disease:** MONDO:0007381; EFO_0009784; ICD-10: H35.71
**Phenotypes (HPO):** HP:0000572 (visual loss), HP:0007401 (macular atrophy), HP:0011506 (choroidal neovascularization), HP:0000580 (pigmentary retinopathy)
**Anatomical structures (UBERON):** UBERON:0000966 (retina), UBERON:0001776 (choroid), UBERON:0000053 (macula lutea)
**Cell types (CL):** CL:0002586 (retinal pigment epithelial cell), CL:0000210 (photoreceptor cell)
**Biological processes (GO):** GO:0006956 (complement activation), GO:0006979 (response to oxidative stress), GO:0001974 (blood vessel remodeling), GO:0045766 (positive regulation of angiogenesis)
**Treatments (MAXO):** MAXO:0000127 (phototherapy), MAXO:0000010 (pharmacotherapy), MAXO:0001298 (intravitreal injection), MAXO:0010022 (laser photocoagulation)
**Chemical entities (CHEBI):** CHEBI:50858 (corticosteroid), CHEBI:6781 (mineralocorticoid), CHEBI:145022 (eplerenone), CHEBI:50267 (verteporfin)

---

*This report integrates evidence from 10 primary literature sources, 13 clinical trials, and OpenTargets disease-target association data. Disease information is derived from aggregated disease-level resources including comprehensive reviews, GWAS meta-analyses, and clinical trial data rather than individual patient electronic health records.*

References

1. (zhang2023centralserouschorioretinopathy pages 1-2): Xinyuan Zhang, Connie Zhi Fong Lim, Jay Chhablani, and Yew Meng Wong. Central serous chorioretinopathy: updates in the pathogenesis, diagnosis and therapeutic strategies. Eye and Vision, Jul 2023. URL: https://doi.org/10.1186/s40662-023-00349-y, doi:10.1186/s40662-023-00349-y. This article has 84 citations and is from a peer-reviewed journal.

2. (kim2025treatmentofcentral pages 2-3): Yoon Jeon Kim, Sobha Sivaprasad, Tariq Aslam, Polona Jaki Mekjavić, Vilma Jūratė Balčiūnienė, Linda Visser, Antonia M. Joussen, Young Hee Yoon, Timothy Y. Y. Lai, and Annabelle A. Okada. Treatment of central serous chorioretinopathy: new options for an old disease. Eye, 39:2375-2388, Jul 2025. URL: https://doi.org/10.1038/s41433-025-03894-z, doi:10.1038/s41433-025-03894-z. This article has 9 citations and is from a peer-reviewed journal.

3. (OpenTargets Search: central serous chorioretinopathy): Open Targets Query (central serous chorioretinopathy, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (zhang2023centralserouschorioretinopathy pages 2-4): Xinyuan Zhang, Connie Zhi Fong Lim, Jay Chhablani, and Yew Meng Wong. Central serous chorioretinopathy: updates in the pathogenesis, diagnosis and therapeutic strategies. Eye and Vision, Jul 2023. URL: https://doi.org/10.1186/s40662-023-00349-y, doi:10.1186/s40662-023-00349-y. This article has 84 citations and is from a peer-reviewed journal.

5. (ramo2024raregeneticvariation pages 30-33): Joel T Rämö, Bryan Gorman, Lu-Chen Weng, Sean J Jurgens, Panisa Singhanetr, Marisa G Tieger, Elon HC van Dijk, Christopher W Halladay, Xin Wang, Joost Brinks, Seung Hoan Choi, Yuyang Luo, Saiju Pyarajan, Cari L Nealon, Michael B Gorin, Wen-Chih Wu, Lucia Sobrin, Kai Kaarniranta, Suzanne Yzer, Aarno Palotie, Neal S Peachey, Joni A Turunen, Camiel JF Boon, Patrick T Ellinor, Sudha K Iyengar, Mark J Daly, and Elizabeth J Rossin. Rare genetic variation in ve-ptp is associated with central serous chorioretinopathy, venous dysfunction and glaucoma. medRxiv, May 2024. URL: https://doi.org/10.1101/2024.05.08.24307013, doi:10.1101/2024.05.08.24307013. This article has 1 citations.

6. (mori2025genomewideassociationand pages 2-3): Yuki Mori, E. H. V. van Dijk, M. Miyake, Yoshikatsu Hosoda, A. D. den Hollander, S. Yzer, Akiko Miki, Li Jia Chen, Jeeyun Ahn, Ayako Takahashi, Kazuya Morino, Shin-Ya Nakao, C. Hoyng, D. S. Ng, Ling-Ping Cen, Haoyu Chen, T. Ng, C. P. Pang, Kwangsic Joo, Takehiro Sato, Yasuhiko Sakata, Atsushi Tajima, Y. Tabara, Yasuharu Takeo Akihiro Shinji Fumihiko Tabara Nakayama Sekine Kosugi Matsuda, Takeo Nakayama, Akihiro Sekine, S. Kosugi, Fumihiko Matsuda, Kyu Hyung Park, K. Yamashiro, Shigeru Honda, Masao Nagasaki, C. Boon, and A. Tsujikawa. Genome-wide association and multi-omics analyses provide insights into the disease mechanisms of central serous chorioretinopathy. Scientific Reports, Mar 2025. URL: https://doi.org/10.1038/s41598-025-92210-6, doi:10.1038/s41598-025-92210-6. This article has 6 citations and is from a peer-reviewed journal.

7. (ramo2025raregeneticvariation pages 1-2): Joel T. Rämö, Bryan R. Gorman, Lu-Chen Weng, Sean J. Jurgens, Panisa Singhanetr, Marisa G. Tieger, Elon HC van Dijk, Christopher W. Halladay, Xin Wang, Blake M. Hauser, Soo Hyun Kim, Joost Brinks, Seung Hoan Choi, Yuyang Luo, Saiju Pyarajan, Cari L. Nealon, Michael B. Gorin, Wen-Chih Wu, Scott A. Anthony, David P. Roncone, Lucia Sobrin, Kai Kaarniranta, Suzanne Yzer, Aarno Palotie, Neal S. Peachey, Joni A. Turunen, Camiel JF Boon, Patrick T. Ellinor, Sudha K. Iyengar, Mark J. Daly, and Elizabeth J. Rossin. Rare genetic variation in ptprb is associated with central serous chorioretinopathy, varicose veins and glaucoma. Nature Communications, May 2025. URL: https://doi.org/10.1038/s41467-025-58686-6, doi:10.1038/s41467-025-58686-6. This article has 13 citations and is from a highest quality peer-reviewed journal.

8. (mori2025genomewideassociationand pages 11-11): Yuki Mori, E. H. V. van Dijk, M. Miyake, Yoshikatsu Hosoda, A. D. den Hollander, S. Yzer, Akiko Miki, Li Jia Chen, Jeeyun Ahn, Ayako Takahashi, Kazuya Morino, Shin-Ya Nakao, C. Hoyng, D. S. Ng, Ling-Ping Cen, Haoyu Chen, T. Ng, C. P. Pang, Kwangsic Joo, Takehiro Sato, Yasuhiko Sakata, Atsushi Tajima, Y. Tabara, Yasuharu Takeo Akihiro Shinji Fumihiko Tabara Nakayama Sekine Kosugi Matsuda, Takeo Nakayama, Akihiro Sekine, S. Kosugi, Fumihiko Matsuda, Kyu Hyung Park, K. Yamashiro, Shigeru Honda, Masao Nagasaki, C. Boon, and A. Tsujikawa. Genome-wide association and multi-omics analyses provide insights into the disease mechanisms of central serous chorioretinopathy. Scientific Reports, Mar 2025. URL: https://doi.org/10.1038/s41598-025-92210-6, doi:10.1038/s41598-025-92210-6. This article has 6 citations and is from a peer-reviewed journal.

9. (ramo2024raregeneticvariation pages 1-4): Joel T Rämö, Bryan Gorman, Lu-Chen Weng, Sean J Jurgens, Panisa Singhanetr, Marisa G Tieger, Elon HC van Dijk, Christopher W Halladay, Xin Wang, Joost Brinks, Seung Hoan Choi, Yuyang Luo, Saiju Pyarajan, Cari L Nealon, Michael B Gorin, Wen-Chih Wu, Lucia Sobrin, Kai Kaarniranta, Suzanne Yzer, Aarno Palotie, Neal S Peachey, Joni A Turunen, Camiel JF Boon, Patrick T Ellinor, Sudha K Iyengar, Mark J Daly, and Elizabeth J Rossin. Rare genetic variation in ve-ptp is associated with central serous chorioretinopathy, venous dysfunction and glaucoma. medRxiv, May 2024. URL: https://doi.org/10.1101/2024.05.08.24307013, doi:10.1101/2024.05.08.24307013. This article has 1 citations.

10. (matet2020lipocalin2as pages 6-6): A. Matet, T. Jaworski, E. Bousquet, J. Canonica, C. Gobeaux, A. Daruich, Min Zhao, M. Zola, Magda A. Meester-Smoor, D. Mohabati, F. Jaisser, S. Yzer, and F. Behar-Cohen. Lipocalin 2 as a potential systemic biomarker for central serous chorioretinopathy. Scientific Reports, Nov 2020. URL: https://doi.org/10.1038/s41598-020-77202-y, doi:10.1038/s41598-020-77202-y. This article has 26 citations and is from a peer-reviewed journal.

11. (zhang2023centralserouschorioretinopathy pages 4-5): Xinyuan Zhang, Connie Zhi Fong Lim, Jay Chhablani, and Yew Meng Wong. Central serous chorioretinopathy: updates in the pathogenesis, diagnosis and therapeutic strategies. Eye and Vision, Jul 2023. URL: https://doi.org/10.1186/s40662-023-00349-y, doi:10.1186/s40662-023-00349-y. This article has 84 citations and is from a peer-reviewed journal.

12. (mori2025genomewideassociationand pages 1-2): Yuki Mori, E. H. V. van Dijk, M. Miyake, Yoshikatsu Hosoda, A. D. den Hollander, S. Yzer, Akiko Miki, Li Jia Chen, Jeeyun Ahn, Ayako Takahashi, Kazuya Morino, Shin-Ya Nakao, C. Hoyng, D. S. Ng, Ling-Ping Cen, Haoyu Chen, T. Ng, C. P. Pang, Kwangsic Joo, Takehiro Sato, Yasuhiko Sakata, Atsushi Tajima, Y. Tabara, Yasuharu Takeo Akihiro Shinji Fumihiko Tabara Nakayama Sekine Kosugi Matsuda, Takeo Nakayama, Akihiro Sekine, S. Kosugi, Fumihiko Matsuda, Kyu Hyung Park, K. Yamashiro, Shigeru Honda, Masao Nagasaki, C. Boon, and A. Tsujikawa. Genome-wide association and multi-omics analyses provide insights into the disease mechanisms of central serous chorioretinopathy. Scientific Reports, Mar 2025. URL: https://doi.org/10.1038/s41598-025-92210-6, doi:10.1038/s41598-025-92210-6. This article has 6 citations and is from a peer-reviewed journal.

13. (zhang2023centralserouschorioretinopathy pages 5-7): Xinyuan Zhang, Connie Zhi Fong Lim, Jay Chhablani, and Yew Meng Wong. Central serous chorioretinopathy: updates in the pathogenesis, diagnosis and therapeutic strategies. Eye and Vision, Jul 2023. URL: https://doi.org/10.1186/s40662-023-00349-y, doi:10.1186/s40662-023-00349-y. This article has 84 citations and is from a peer-reviewed journal.

14. (mori2025genomewideassociationand pages 10-11): Yuki Mori, E. H. V. van Dijk, M. Miyake, Yoshikatsu Hosoda, A. D. den Hollander, S. Yzer, Akiko Miki, Li Jia Chen, Jeeyun Ahn, Ayako Takahashi, Kazuya Morino, Shin-Ya Nakao, C. Hoyng, D. S. Ng, Ling-Ping Cen, Haoyu Chen, T. Ng, C. P. Pang, Kwangsic Joo, Takehiro Sato, Yasuhiko Sakata, Atsushi Tajima, Y. Tabara, Yasuharu Takeo Akihiro Shinji Fumihiko Tabara Nakayama Sekine Kosugi Matsuda, Takeo Nakayama, Akihiro Sekine, S. Kosugi, Fumihiko Matsuda, Kyu Hyung Park, K. Yamashiro, Shigeru Honda, Masao Nagasaki, C. Boon, and A. Tsujikawa. Genome-wide association and multi-omics analyses provide insights into the disease mechanisms of central serous chorioretinopathy. Scientific Reports, Mar 2025. URL: https://doi.org/10.1038/s41598-025-92210-6, doi:10.1038/s41598-025-92210-6. This article has 6 citations and is from a peer-reviewed journal.

15. (chen2026thecfh–cfhr5locus pages 10-10): Zhen Ji Chen, Jun Yu, Mary Ho, Danny S.C. Ng, Marten E. Brelen, Alvin L. Young, Jason C.S. Yam, Clement C. Tham, Chi Pui Pang, and Li Jia Chen. The cfh–cfhr5 locus in wet age-related macular degeneration, polypoidal choroidal vasculopathy, and central serous chorioretinopathy. Ophthalmology Science, 6(2):101043, Feb 2026. URL: https://doi.org/10.1016/j.xops.2025.101043, doi:10.1016/j.xops.2025.101043. This article has 1 citations.

16. (chen2026thecfh–cfhr5locus pages 8-9): Zhen Ji Chen, Jun Yu, Mary Ho, Danny S.C. Ng, Marten E. Brelen, Alvin L. Young, Jason C.S. Yam, Clement C. Tham, Chi Pui Pang, and Li Jia Chen. The cfh–cfhr5 locus in wet age-related macular degeneration, polypoidal choroidal vasculopathy, and central serous chorioretinopathy. Ophthalmology Science, 6(2):101043, Feb 2026. URL: https://doi.org/10.1016/j.xops.2025.101043, doi:10.1016/j.xops.2025.101043. This article has 1 citations.

17. (matet2020lipocalin2as pages 5-6): A. Matet, T. Jaworski, E. Bousquet, J. Canonica, C. Gobeaux, A. Daruich, Min Zhao, M. Zola, Magda A. Meester-Smoor, D. Mohabati, F. Jaisser, S. Yzer, and F. Behar-Cohen. Lipocalin 2 as a potential systemic biomarker for central serous chorioretinopathy. Scientific Reports, Nov 2020. URL: https://doi.org/10.1038/s41598-020-77202-y, doi:10.1038/s41598-020-77202-y. This article has 26 citations and is from a peer-reviewed journal.

18. (matet2020lipocalin2as pages 1-2): A. Matet, T. Jaworski, E. Bousquet, J. Canonica, C. Gobeaux, A. Daruich, Min Zhao, M. Zola, Magda A. Meester-Smoor, D. Mohabati, F. Jaisser, S. Yzer, and F. Behar-Cohen. Lipocalin 2 as a potential systemic biomarker for central serous chorioretinopathy. Scientific Reports, Nov 2020. URL: https://doi.org/10.1038/s41598-020-77202-y, doi:10.1038/s41598-020-77202-y. This article has 26 citations and is from a peer-reviewed journal.

19. (matet2020lipocalin2as pages 2-3): A. Matet, T. Jaworski, E. Bousquet, J. Canonica, C. Gobeaux, A. Daruich, Min Zhao, M. Zola, Magda A. Meester-Smoor, D. Mohabati, F. Jaisser, S. Yzer, and F. Behar-Cohen. Lipocalin 2 as a potential systemic biomarker for central serous chorioretinopathy. Scientific Reports, Nov 2020. URL: https://doi.org/10.1038/s41598-020-77202-y, doi:10.1038/s41598-020-77202-y. This article has 26 citations and is from a peer-reviewed journal.

20. (matet2020lipocalin2as pages 3-5): A. Matet, T. Jaworski, E. Bousquet, J. Canonica, C. Gobeaux, A. Daruich, Min Zhao, M. Zola, Magda A. Meester-Smoor, D. Mohabati, F. Jaisser, S. Yzer, and F. Behar-Cohen. Lipocalin 2 as a potential systemic biomarker for central serous chorioretinopathy. Scientific Reports, Nov 2020. URL: https://doi.org/10.1038/s41598-020-77202-y, doi:10.1038/s41598-020-77202-y. This article has 26 citations and is from a peer-reviewed journal.

21. (zhang2023centralserouschorioretinopathy pages 7-10): Xinyuan Zhang, Connie Zhi Fong Lim, Jay Chhablani, and Yew Meng Wong. Central serous chorioretinopathy: updates in the pathogenesis, diagnosis and therapeutic strategies. Eye and Vision, Jul 2023. URL: https://doi.org/10.1186/s40662-023-00349-y, doi:10.1186/s40662-023-00349-y. This article has 84 citations and is from a peer-reviewed journal.

22. (kim2025treatmentofcentral pages 3-5): Yoon Jeon Kim, Sobha Sivaprasad, Tariq Aslam, Polona Jaki Mekjavić, Vilma Jūratė Balčiūnienė, Linda Visser, Antonia M. Joussen, Young Hee Yoon, Timothy Y. Y. Lai, and Annabelle A. Okada. Treatment of central serous chorioretinopathy: new options for an old disease. Eye, 39:2375-2388, Jul 2025. URL: https://doi.org/10.1038/s41433-025-03894-z, doi:10.1038/s41433-025-03894-z. This article has 9 citations and is from a peer-reviewed journal.

23. (zhang2023centralserouschorioretinopathy pages 10-12): Xinyuan Zhang, Connie Zhi Fong Lim, Jay Chhablani, and Yew Meng Wong. Central serous chorioretinopathy: updates in the pathogenesis, diagnosis and therapeutic strategies. Eye and Vision, Jul 2023. URL: https://doi.org/10.1186/s40662-023-00349-y, doi:10.1186/s40662-023-00349-y. This article has 84 citations and is from a peer-reviewed journal.

24. (kim2025treatmentofcentral pages 11-11): Yoon Jeon Kim, Sobha Sivaprasad, Tariq Aslam, Polona Jaki Mekjavić, Vilma Jūratė Balčiūnienė, Linda Visser, Antonia M. Joussen, Young Hee Yoon, Timothy Y. Y. Lai, and Annabelle A. Okada. Treatment of central serous chorioretinopathy: new options for an old disease. Eye, 39:2375-2388, Jul 2025. URL: https://doi.org/10.1038/s41433-025-03894-z, doi:10.1038/s41433-025-03894-z. This article has 9 citations and is from a peer-reviewed journal.

25. (shojaeinia2025acomprehensiveoverview pages 1-2): Mohammad Shojaeinia, Azamossadat Hosseini, Mostafa Naderi, Bardia D Baloutch, Mohammad Shokoohi Yekta, Leila Akbarpour, and Hamid Moghaddasi. A comprehensive overview: deep learning approaches to central serous chorioretinopathy diagnosis. BMC Ophthalmology, Oct 2025. URL: https://doi.org/10.1186/s12886-025-04372-6, doi:10.1186/s12886-025-04372-6. This article has 5 citations and is from a peer-reviewed journal.

26. (shojaeinia2025acomprehensiveoverview pages 14-16): Mohammad Shojaeinia, Azamossadat Hosseini, Mostafa Naderi, Bardia D Baloutch, Mohammad Shokoohi Yekta, Leila Akbarpour, and Hamid Moghaddasi. A comprehensive overview: deep learning approaches to central serous chorioretinopathy diagnosis. BMC Ophthalmology, Oct 2025. URL: https://doi.org/10.1186/s12886-025-04372-6, doi:10.1186/s12886-025-04372-6. This article has 5 citations and is from a peer-reviewed journal.

27. (shojaeinia2025acomprehensiveoverview pages 13-14): Mohammad Shojaeinia, Azamossadat Hosseini, Mostafa Naderi, Bardia D Baloutch, Mohammad Shokoohi Yekta, Leila Akbarpour, and Hamid Moghaddasi. A comprehensive overview: deep learning approaches to central serous chorioretinopathy diagnosis. BMC Ophthalmology, Oct 2025. URL: https://doi.org/10.1186/s12886-025-04372-6, doi:10.1186/s12886-025-04372-6. This article has 5 citations and is from a peer-reviewed journal.

28. (shojaeinia2025acomprehensiveoverview pages 8-9): Mohammad Shojaeinia, Azamossadat Hosseini, Mostafa Naderi, Bardia D Baloutch, Mohammad Shokoohi Yekta, Leila Akbarpour, and Hamid Moghaddasi. A comprehensive overview: deep learning approaches to central serous chorioretinopathy diagnosis. BMC Ophthalmology, Oct 2025. URL: https://doi.org/10.1186/s12886-025-04372-6, doi:10.1186/s12886-025-04372-6. This article has 5 citations and is from a peer-reviewed journal.

29. (kim2025treatmentofcentral pages 8-9): Yoon Jeon Kim, Sobha Sivaprasad, Tariq Aslam, Polona Jaki Mekjavić, Vilma Jūratė Balčiūnienė, Linda Visser, Antonia M. Joussen, Young Hee Yoon, Timothy Y. Y. Lai, and Annabelle A. Okada. Treatment of central serous chorioretinopathy: new options for an old disease. Eye, 39:2375-2388, Jul 2025. URL: https://doi.org/10.1038/s41433-025-03894-z, doi:10.1038/s41433-025-03894-z. This article has 9 citations and is from a peer-reviewed journal.

30. (zhang2023centralserouschorioretinopathy pages 19-20): Xinyuan Zhang, Connie Zhi Fong Lim, Jay Chhablani, and Yew Meng Wong. Central serous chorioretinopathy: updates in the pathogenesis, diagnosis and therapeutic strategies. Eye and Vision, Jul 2023. URL: https://doi.org/10.1186/s40662-023-00349-y, doi:10.1186/s40662-023-00349-y. This article has 84 citations and is from a peer-reviewed journal.

31. (kim2025treatmentofcentral pages 12-13): Yoon Jeon Kim, Sobha Sivaprasad, Tariq Aslam, Polona Jaki Mekjavić, Vilma Jūratė Balčiūnienė, Linda Visser, Antonia M. Joussen, Young Hee Yoon, Timothy Y. Y. Lai, and Annabelle A. Okada. Treatment of central serous chorioretinopathy: new options for an old disease. Eye, 39:2375-2388, Jul 2025. URL: https://doi.org/10.1038/s41433-025-03894-z, doi:10.1038/s41433-025-03894-z. This article has 9 citations and is from a peer-reviewed journal.

32. (kim2025treatmentofcentral pages 9-10): Yoon Jeon Kim, Sobha Sivaprasad, Tariq Aslam, Polona Jaki Mekjavić, Vilma Jūratė Balčiūnienė, Linda Visser, Antonia M. Joussen, Young Hee Yoon, Timothy Y. Y. Lai, and Annabelle A. Okada. Treatment of central serous chorioretinopathy: new options for an old disease. Eye, 39:2375-2388, Jul 2025. URL: https://doi.org/10.1038/s41433-025-03894-z, doi:10.1038/s41433-025-03894-z. This article has 9 citations and is from a peer-reviewed journal.

33. (zhang2023centralserouschorioretinopathy pages 14-15): Xinyuan Zhang, Connie Zhi Fong Lim, Jay Chhablani, and Yew Meng Wong. Central serous chorioretinopathy: updates in the pathogenesis, diagnosis and therapeutic strategies. Eye and Vision, Jul 2023. URL: https://doi.org/10.1186/s40662-023-00349-y, doi:10.1186/s40662-023-00349-y. This article has 84 citations and is from a peer-reviewed journal.

34. (kim2025treatmentofcentral pages 9-9): Yoon Jeon Kim, Sobha Sivaprasad, Tariq Aslam, Polona Jaki Mekjavić, Vilma Jūratė Balčiūnienė, Linda Visser, Antonia M. Joussen, Young Hee Yoon, Timothy Y. Y. Lai, and Annabelle A. Okada. Treatment of central serous chorioretinopathy: new options for an old disease. Eye, 39:2375-2388, Jul 2025. URL: https://doi.org/10.1038/s41433-025-03894-z, doi:10.1038/s41433-025-03894-z. This article has 9 citations and is from a peer-reviewed journal.

35. (kim2025treatmentofcentral pages 7-8): Yoon Jeon Kim, Sobha Sivaprasad, Tariq Aslam, Polona Jaki Mekjavić, Vilma Jūratė Balčiūnienė, Linda Visser, Antonia M. Joussen, Young Hee Yoon, Timothy Y. Y. Lai, and Annabelle A. Okada. Treatment of central serous chorioretinopathy: new options for an old disease. Eye, 39:2375-2388, Jul 2025. URL: https://doi.org/10.1038/s41433-025-03894-z, doi:10.1038/s41433-025-03894-z. This article has 9 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Central_Serous_Chorioretinopathy-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Central_Serous_Chorioretinopathy-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Central_Serous_Chorioretinopathy-deep-research-falcon_artifacts/artifact-02.md)