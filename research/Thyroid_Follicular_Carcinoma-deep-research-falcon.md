---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-22T10:11:33.730551'
end_time: '2026-06-22T10:27:17.712276'
duration_seconds: 943.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Thyroid Follicular Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Thyroid_Follicular_Carcinoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Thyroid_Follicular_Carcinoma-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Thyroid_Follicular_Carcinoma-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Thyroid Follicular Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Thyroid Follicular Carcinoma** covering all of the
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
- **Disease Name:** Thyroid Follicular Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Thyroid Follicular Carcinoma** covering all of the
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


# Comprehensive Research Report: Thyroid Follicular Carcinoma

## Target Disease
- **Disease Name:** Thyroid Follicular Carcinoma (FTC)
- **Category:** Differentiated Thyroid Cancer, Endocrine Malignancy

---

## 1. DISEASE INFORMATION

### Overview and Definition

Follicular thyroid carcinoma (FTC) is a malignant neoplasm derived from thyroid follicular epithelial cells, representing the second most common type of differentiated thyroid cancer (DTC) after papillary thyroid carcinoma (PTC) (forma2025thyroidcancerepidemiology pages 1-2, fagin2023pathogenesisofcancers pages 1-3). FTC accounts for approximately 6-10% of all thyroid cancers, though this proportion varies by geographic region and iodine status (kitahara2022epidemiologyofthyroid pages 1-3, forma2025thyroidcancerepidemiology pages 1-2, fagin2023pathogenesisofcancers pages 1-3). The 2022 WHO Classification of Endocrine and Neuroendocrine Tumors categorizes FTC as a well-differentiated thyroid carcinoma arising from follicular cells, distinct from papillary carcinoma in both molecular profile and biological behavior (singh2021thegenomiclandscape pages 1-2).

FTC is distinguished by its propensity for capsular and vascular invasion and hematogenous dissemination to distant sites, particularly lung and bone, rather than lymphatic spread (zhang2023riskfactorsfor pages 1-2, singh2021thegenomiclandscape pages 1-2). This biological characteristic differentiates it clinically from PTC, which more commonly metastasizes to regional lymph nodes. The diagnosis of FTC fundamentally depends on demonstrating capsular and/or vascular invasion on histopathologic examination, as cytologic features alone cannot reliably distinguish follicular carcinoma from benign follicular adenoma (FTA) (borowczyk2023follicularthyroidadenoma pages 1-2, capdevila2022moleculardiagnosisand pages 1-2).

### Key Identifiers

While specific OMIM, Orphanet, and MONDO identifiers were not explicitly provided in the retrieved literature, FTC is classified under ICD-O codes and is included in thyroid cancer classifications. The disease is sometimes referred to as **follicular thyroid cancer** or **follicular carcinoma of the thyroid** in clinical literature (forma2025thyroidcancerepidemiology pages 1-2, singh2021thegenomiclandscape pages 1-2).

### Common Synonyms
- Follicular thyroid cancer
- Follicular carcinoma of the thyroid
- FTC

---

## 2. ETIOLOGY

### Disease Causal Factors

The molecular pathogenesis of FTC involves dysregulation of the mitogen-activated protein kinase (MAPK) and phosphatidylinositol-3-kinase (PI3K)/AKT signaling pathways (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3). Unlike PTC, which is predominantly driven by BRAF V600E mutations, FTC typically harbors **RAS mutations** (NRAS, HRAS, KRAS) or **PAX8-PPARG gene fusions** as primary oncogenic drivers (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2). These alterations constitute the "RAS-like" molecular signature characteristic of follicular-patterned thyroid tumors, distinguished from the "BRAF-like" pattern of conventional papillary carcinomas (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3).

RAS mutations activate both the MAPK and PI3K/AKT pathways, with the latter pathway being particularly critical for FTC initiation and progression (prete2020updateonfundamental pages 1-3, calafato2025somaticgeneticalterations pages 1-2). Additional PI3K pathway alterations include **PTEN** loss or mutation, and activating mutations in **PIK3CA** and **AKT1** (prete2020updateonfundamental pages 1-3, calafato2025somaticgeneticalterations pages 1-2). These genetic events support unregulated cell growth, survival, and invasive behavior characteristic of FTC.

| Gene/Alteration | Frequency (%) | Type of Alteration | Pathway Involved | Clinical Significance | Evidence Sources |
|---|---:|---|---|---|---|
| **RAS** (NRAS, HRAS, KRAS) mutations | Common in FTC; reported among the major/primary driver events in follicular-patterned thyroid tumors; exact FTC-specific prevalence not uniformly stated in retrieved sources | Activating point mutations | MAPK; also PI3K/AKT cross-talk | Early/truncal driver of FTC; associated with follicular-patterned phenotype, tumor initiation, and propensity for vascular invasion; part of the “RAS-like” molecular class used in risk stratification (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2) | (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2, capdevila2022moleculardiagnosisand pages 1-2) |
| **PAX8-PPARG** fusion | Common/recurrent in FTC; older reviews cited in retrieved papers note it as a characteristic FTC alteration, but no single consistent percentage is given in the accessible excerpts | Chromosomal rearrangement / gene fusion | PI3K/AKT-associated biology; follicular differentiation programs | Supports FTC diagnosis in follicular-patterned tumors; implicated in tumorigenesis and used in molecular classification of follicular lesions (prete2020updateonfundamental pages 1-3, crncic2020riskfactorsfor pages 1-2) | (prete2020updateonfundamental pages 1-3, crncic2020riskfactorsfor pages 1-2) |
| **PTEN** loss / mutation | Recurrent but less common than RAS; frequency not consistently quantified in retrieved excerpts | Inactivating mutation, deletion, or loss of function | PI3K/PTEN/AKT | Promotes FTC initiation/progression via derepression of PI3K signaling; relevant to aggressive biology and dedifferentiation when combined with other events (prete2020updateonfundamental pages 1-3, calafato2025somaticgeneticalterations pages 1-2) | (prete2020updateonfundamental pages 1-3, calafato2025somaticgeneticalterations pages 1-2) |
| **PIK3CA / AKT1 / broader PI3K pathway alterations** | Recurrent in FTC and more advanced follicular-cell derived thyroid cancers; exact FTC-specific percentage not consistently stated in retrieved excerpts | Activating mutations / pathway activation | PI3K/AKT/mTOR | Important for FTC initiation and progression; contributes to less differentiated/aggressive disease and potential therapeutic vulnerability (prete2020updateonfundamental pages 1-3, singh2021thegenomiclandscape pages 1-2, calafato2025somaticgeneticalterations pages 1-2) | (prete2020updateonfundamental pages 1-3, singh2021thegenomiclandscape pages 1-2, calafato2025somaticgeneticalterations pages 1-2) |
| **TP53** mutations | Rare in well-differentiated FTC; enriched in poorly differentiated/anaplastic progression; 26% in PDTC and ~80% in ATC across thyroid cancers | Inactivating point mutation / tumor suppressor loss | p53 / cell-cycle checkpoint pathways | Late event associated with dedifferentiation, genomic instability, and progression from differentiated thyroid carcinoma to high-grade disease rather than typical early FTC initiation (kitahara2022epidemiologyofthyroid pages 1-3, prete2020updateonfundamental pages 1-3, calafato2025somaticgeneticalterations pages 1-2) | (kitahara2022epidemiologyofthyroid pages 1-3, prete2020updateonfundamental pages 1-3, calafato2025somaticgeneticalterations pages 1-2) |
| **TERT promoter** mutations | Present across thyroid cancer histologies, with substantially higher prevalence in aggressive/undifferentiated tumors; exact FTC-specific prevalence not consistently stated in retrieved excerpts | Promoter mutation causing telomerase activation | Telomere maintenance; cooperates with MAPK/PI3K-driven oncogenesis | Strong marker of aggressiveness, dedifferentiation, recurrence, and poor outcomes; considered a progression event rather than a typical sole initiating lesion (kitahara2022epidemiologyofthyroid pages 1-3, prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2) | (kitahara2022epidemiologyofthyroid pages 1-3, prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2) |
| **MAPK pathway dysregulation** | Core molecular theme in most follicular-cell derived thyroid cancers; in FTC often driven by RAS rather than BRAF | Pathway-level constitutive activation | RTK-RAS-RAF-MEK-ERK (MAPK) | Central determinant of thyroid tumor phenotype; in FTC, lower/"RAS-like" MAPK output is linked to follicular architecture and differentiation state; relevant for molecular classification and targeted therapy development (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2) | (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2) |
| **PI3K/PTEN/AKT pathway dysregulation** | Core molecular theme in FTC; repeatedly emphasized as critical in FTC initiation | Pathway-level activation via **RAS**, **PIK3CA**, **AKT1**, **PTEN** loss | PI3K/AKT/mTOR | Especially important in FTC biology versus papillary carcinoma; linked to tumor growth, survival, dedifferentiation, and progression to advanced disease (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2) | (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2) |
| **Loss of heterozygosity (LOH) / chromosomal imbalance** (e.g., 16p12.1, 3p21.31, 12q24.11-q24.13) | In one microarray study, total LOH events were higher in FTC than FTA (18 vs 15); specific recurrent regions varied by cohort | Chromosomal copy-number/allelic imbalance | Mixed; includes regions harboring cancer-related genes such as **TP53**, **PTPN11** | Suggests genomic instability and partially shared background with follicular adenoma, while some rearrangements may help distinguish malignant FTC from benign FTA (borowczyk2023follicularthyroidadenoma pages 1-2) | (borowczyk2023follicularthyroidadenoma pages 1-2) |
| **FTC vs FTA transcriptomic hub genes** (**TOP2A, JUN, EGFR, CDK1, FOS, CDKN3, EZH2, TYMS, PBK, CDH1, UBE2C, CCNB2**) | Derived from differential-expression/network analysis rather than mutation prevalence; 598 DEGs identified in one study | Differential expression / network hub dysregulation | p53 signaling, cell cycle, folate/one-carbon metabolism, EGFR-related signaling | Highlights candidate biomarkers and mechanisms of malignant progression distinguishing FTC from follicular adenoma; useful for discovery but not yet established routine clinical markers (hossain2020networkbasedgeneticprofiling pages 1-3) | (hossain2020networkbasedgeneticprofiling pages 1-3) |


*Table: This table summarizes the principal genetic and pathway-level alterations reported for follicular thyroid carcinoma, emphasizing drivers, progression events, and potential diagnostic or prognostic relevance. It is useful for quickly mapping specific genes to the molecular mechanisms and clinical behavior of FTC.*

### Risk Factors

**Genetic Risk Factors:**
- **Radiation exposure:** Childhood exposure to ionizing radiation, particularly to the head and neck region, is the only firmly established modifiable environmental risk factor for thyroid cancer, including FTC (kitahara2022epidemiologyofthyroid pages 1-3, crncic2020riskfactorsfor pages 1-2, kruger2022thyroidcarcinomaa pages 1-2).
- **Hereditary syndromes:** Approximately 3-9% of thyroid cancers are familial non-medullary thyroid carcinomas (FNMTC) (crncic2020riskfactorsfor pages 1-2). Hereditary syndromes associated with follicular-cell derived tumors include Cowden syndrome (PTEN hamartoma tumor syndrome), familial adenomatous polyposis, Carney complex, and Werner syndrome (crncic2020riskfactorsfor pages 1-2).
- **Constitutional genetic variants:** Germline mutations in tumor suppressor genes such as PTEN predispose to thyroid follicular neoplasms (fagin2023pathogenesisofcancers pages 1-3).

**Environmental Risk Factors:**
- **Iodine deficiency:** FTC historically comprises a larger proportion of thyroid cancers in iodine-deficient geographic regions compared to iodine-sufficient areas (forma2025thyroidcancerepidemiology pages 1-2, crncic2020riskfactorsfor pages 1-2).
- **Environmental toxicants:** Exposure to endocrine-disrupting chemicals (EDCs), including organochlorines, pesticides, polychlorinated biphenyls (PCBs), polybrominated diethyl ethers, phthalates, bisphenol A (BPA), heavy metals, and air pollution, has been associated with increased thyroid cancer risk (forma2025thyroidcancerepidemiology pages 1-2, kruger2022thyroidcarcinomaa pages 1-2). These agents can interfere with thyroid hormone biosynthesis, transport, and function.
- **Obesity:** Emerging evidence identifies obesity as an important thyroid cancer risk factor, though mechanisms remain poorly understood (kitahara2022epidemiologyofthyroid pages 1-3, crncic2020riskfactorsfor pages 1-2).

**Demographic Risk Factors:**
- **Female sex:** Thyroid cancer, including FTC, is approximately 3 times more common in females than males (kitahara2022epidemiologyofthyroid pages 1-3, forma2025thyroidcancerepidemiology pages 1-2, singh2021thegenomiclandscape pages 1-2, kruger2022thyroidcarcinomaa pages 1-2).
- **Age:** FTC is predominantly an adult-onset malignancy, with incidence peaking around age 55 in women and 65 in men (kitahara2022epidemiologyofthyroid pages 1-3, forma2025thyroidcancerepidemiology pages 1-2).

### Protective Factors

No firmly established FTC-specific protective factors were identified in the retrieved literature (kitahara2022epidemiologyofthyroid pages 1-3, kruger2022thyroidcarcinomaa pages 1-2). This likely reflects the current research focus on risk characterization rather than protective mechanisms.

### Gene-Environment Interactions

The interplay between genetic susceptibility and environmental exposures in FTC pathogenesis is not well characterized. Radiation-induced thyroid cancers demonstrate chromosomal rearrangements (RET/PTC fusions) at higher frequencies than sporadic cases, suggesting that environmental mutagens can interact with genomic fragile sites (prete2020updateonfundamental pages 1-3, crncic2020riskfactorsfor pages 1-2). Iodine status may influence the histologic distribution of thyroid cancers, with follicular patterns more prevalent in iodine-deficient populations (crncic2020riskfactorsfor pages 1-2).

| Domain | Finding | Quantitative detail | Notes / clinical interpretation | Evidence |
|---|---|---:|---|---|
| Histologic share of thyroid cancer | Follicular thyroid carcinoma (FTC) is the second major differentiated thyroid carcinoma subtype but is much less common than papillary thyroid carcinoma | ~4% of thyroid cancers in one epidemiology review; ~6–10% in a 2023 pathogenesis review; ~10–15% in another recent review | Differences reflect source, classification era, and whether oncocytic/Hürthle tumors are separated; all sources agree FTC is a minority subtype of follicular-cell derived thyroid cancers | (kitahara2022epidemiologyofthyroid pages 1-3, fagin2023pathogenesisofcancers pages 1-3, kruger2022thyroidcarcinomaa pages 1-2, capdevila2022moleculardiagnosisand pages 1-2) |
| Overall thyroid cancer sex ratio | Thyroid cancer overall is markedly more common in females | ~3:1 female:male overall | FTC-specific sex ratio is less consistently quantified in the retrieved papers, but differentiated thyroid cancers including FTC follow the same female predominance pattern | (kitahara2022epidemiologyofthyroid pages 1-3, forma2025thyroidcancerepidemiology pages 1-2, singh2021thegenomiclandscape pages 1-2, kruger2022thyroidcarcinomaa pages 1-2) |
| Overall thyroid cancer age distribution | Incidence rises from adolescence through mid-late adulthood | Peaks around age 55 in women and 65 in men in U.S. data; mean age at diagnosis ~51 years in a 2025 review | FTC is generally an adult-onset malignancy; adverse prognosis increases with older age | (kitahara2022epidemiologyofthyroid pages 1-3, forma2025thyroidcancerepidemiology pages 1-2, zhang2023riskfactorsfor pages 1-2) |
| Geographic distribution | Thyroid cancer incidence varies widely by region | Highest incidence reported in higher-income countries and in South Korea; also high in Canada, Italy, France, Israel, Croatia, Austria, U.S., Turkey, Brazil, Costa Rica, China, and some Pacific/island regions | Geographic variability likely reflects both diagnostic intensity/overdiagnosis and environmental exposures; FTC historically represents a larger share where iodine deficiency is more relevant | (kitahara2022epidemiologyofthyroid pages 1-3, forma2025thyroidcancerepidemiology pages 1-2, kruger2022thyroidcarcinomaa pages 1-2) |
| Thyroid cancer burden | Thyroid cancer is a common endocrine malignancy worldwide | ~43,800–44,000 new U.S. cases in 2022; 821,214 global cases in 2022 | FTC is a minority subset of this burden | (fagin2023pathogenesisofcancers pages 1-3, vico2025systemictherapeuticoptions pages 1-2) |
| Overall survival of differentiated thyroid carcinoma | Localized differentiated thyroid carcinoma has excellent long-term survival | 5-year survival >98% for differentiated thyroid carcinomas; 10-year survival >90% in localized disease | These figures apply to DTC broadly, including FTC; prognosis worsens substantially with distant metastases or radioiodine-refractory disease | (fagin2023pathogenesisofcancers pages 1-3, vico2025systemictherapeuticoptions pages 1-2) |
| Advanced/RAI-refractory prognosis | A minority of differentiated thyroid carcinomas become radioiodine-refractory with worse outcomes | ~5–15% develop RAI-refractory disease; median overall survival after distant metastasis/RAI-refractory disease ~2.5–3.5 years in one 2025 review | Relevant to metastatic FTC, which can lose iodine avidity and require systemic therapy | (vico2025systemictherapeuticoptions pages 1-2) |
| Radiation risk | Childhood exposure to ionizing radiation is the best-established modifiable thyroid cancer risk factor | Qualitatively established across reviews; no FTC-specific pooled estimate provided in retrieved texts | Radiation is classically most associated with papillary carcinoma, but is considered an established thyroid cancer risk factor overall | (kitahara2022epidemiologyofthyroid pages 1-3, crncic2020riskfactorsfor pages 1-2, kruger2022thyroidcarcinomaa pages 1-2) |
| Iodine-related risk | Iodine deficiency is associated with follicular histology and is a recognized thyroid cancer risk context | No single pooled effect size reported in retrieved sources | FTC proportion is traditionally higher in iodine-deficient settings than in iodine-sufficient populations | (forma2025thyroidcancerepidemiology pages 1-2, crncic2020riskfactorsfor pages 1-2) |
| Environmental/occupational risk | Environmental toxicants are plausible contributors to thyroid carcinogenesis | Reviews cite pesticides, persistent organic pollutants, phthalates, bisphenol A, PCBs, heavy metals, air pollution, and endocrine-disrupting chemicals | Evidence is stronger for thyroid cancer overall than for FTC specifically; mechanism often involves thyroid hormone disruption | (forma2025thyroidcancerepidemiology pages 1-2, kruger2022thyroidcarcinomaa pages 1-2) |
| Obesity and metabolic factors | Obesity is an emerging thyroid cancer risk factor | Described as an “important” or emerging risk factor in modern epidemiology reviews | Evidence is mostly for thyroid cancer overall rather than FTC alone | (kitahara2022epidemiologyofthyroid pages 1-3, crncic2020riskfactorsfor pages 1-2) |
| Family history / hereditary predisposition | Family history increases thyroid cancer risk; some hereditary syndromes predispose to follicular-cell tumors | Familial non-medullary thyroid cancer estimated at ~3–9% of thyroid cancers in one review | Hereditary syndromes relevant to follicular-patterned tumors include Cowden syndrome/PTEN-related disease and other syndromic contexts | (crncic2020riskfactorsfor pages 1-2, fagin2023pathogenesisofcancers pages 1-3) |
| Molecular risk background | FTC commonly arises through RAS-like molecular drivers and PI3K-pathway dysregulation | No single prevalence figure across all FTCs in retrieved excerpts; recurrent alterations include RAS mutations and PAX8-PPARG fusions | Molecular background informs classification, prognosis, and targeted-therapy strategies rather than primary prevention | (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2) |
| Protective factors | No firmly established FTC-specific protective factors were identified in the retrieved papers | Not available | Absence of evidence in the retrieved set should not be interpreted as absence of any protective effect; rather, current literature is more focused on risk than protection | (kitahara2022epidemiologyofthyroid pages 1-3, kruger2022thyroidcarcinomaa pages 1-2) |
| Prognostic factor: age | Older age is associated with higher risk of FTC-specific death | Age >45 years increased mortality risk in a 2023 meta-analysis | Age remains one of the strongest and most consistent prognostic variables in FTC | (zhang2023riskfactorsfor pages 1-2) |
| Prognostic factor: sex | Male sex is associated with worse FTC outcomes | Male sex increased mortality risk in FTC meta-analysis | Despite lower incidence in men, outcomes are worse when FTC occurs in males | (zhang2023riskfactorsfor pages 1-2) |
| Prognostic factor: tumor size | Larger tumors predict worse prognosis | Tumor diameter >4 cm associated with increased risk of death | Large primary tumor size is a practical adverse clinicopathologic feature | (zhang2023riskfactorsfor pages 1-2) |
| Prognostic factor: multifocality | Multifocal disease predicts worse FTC-specific survival | Associated with increased mortality risk in FTC meta-analysis | Suggests greater intrathyroidal disease burden/aggressiveness | (zhang2023riskfactorsfor pages 1-2) |
| Prognostic factor: extrathyroidal extension | Extrathyroidal extension (ETE) is adverse | ETE associated with increased risk of death | Indicates locally invasive disease | (zhang2023riskfactorsfor pages 1-2) |
| Prognostic factor: invasion pattern | Widely invasive FTC has worse outcomes than minimally invasive FTC | Widely invasive histology associated with increased mortality risk | This distinction is central to pathologic risk stratification | (zhang2023riskfactorsfor pages 1-2) |
| Prognostic factor: nodal metastasis | Cervical lymph node metastasis is adverse in FTC | CLNM associated with increased risk of death | Less common than in papillary carcinoma but prognostically unfavorable when present | (zhang2023riskfactorsfor pages 1-2) |
| Prognostic factor: distant metastasis | Distant metastasis is one of the strongest predictors of FTC mortality | DM associated with increased risk of death | Reflects FTC’s known propensity for hematogenous dissemination | (zhang2023riskfactorsfor pages 1-2) |
| Prognostic factor: surgical completeness | Non-radical resection worsens survival | Non-radical resection associated with increased mortality risk | Supports the importance of complete oncologic surgery when feasible | (zhang2023riskfactorsfor pages 1-2) |
| Distinctive clinical behavior | FTC is biologically distinct from papillary thyroid carcinoma and more prone to hematogenous spread | Qualitative | FTC has a recognized propensity for capsular and vascular invasion and distant metastasis, especially to bone/lung, which helps explain its prognostic profile | (zhang2023riskfactorsfor pages 1-2, singh2021thegenomiclandscape pages 1-2) |
| Histopathologic diagnostic hallmark | FTC diagnosis depends on invasion rather than cytology alone | Qualitative | Preoperative imaging/cytology often cannot reliably distinguish follicular adenoma from carcinoma because capsular/vascular invasion usually requires surgical pathology assessment | (borowczyk2023follicularthyroidadenoma pages 1-2, capdevila2022moleculardiagnosisand pages 1-2) |


*Table: This table summarizes the most useful epidemiologic, risk, prognostic, and survival findings for follicular thyroid carcinoma from the retrieved literature. It is designed to support rapid knowledge-base curation and highlight where data are FTC-specific versus broader differentiated thyroid cancer evidence.*

---

## 3. PHENOTYPES

### Clinical Manifestations

FTC typically presents as a solitary thyroid nodule discovered on physical examination or incidentally on imaging studies performed for unrelated indications (forma2025thyroidcancerepidemiology pages 1-2, hu2021thyroidcarcinomaphenotypic pages 1-2). Many patients are asymptomatic at diagnosis. When symptoms occur, they may include:

**Suggested HPO terms:**
- HP:0000872: Hashimoto thyroiditis (if concurrent autoimmune disease)
- HP:0100646: Thyroid nodule
- HP:0012125: Metastasis (in advanced disease)

### Phenotype Characteristics

**Age of Onset:**
- **Adult-onset:** FTC is predominantly diagnosed in middle-aged to older adults, with peak incidence in the fifth and sixth decades of life (kitahara2022epidemiologyofthyroid pages 1-3, forma2025thyroidcancerepidemiology pages 1-2).

**Symptom Severity:**
- Variable; localized disease may be asymptomatic, whereas widely invasive FTC with distant metastases can cause significant morbidity related to metastatic sites (bone pain, respiratory symptoms) (zhang2023riskfactorsfor pages 1-2).

**Symptom Progression:**
- Generally indolent in minimally invasive forms; widely invasive FTC demonstrates more aggressive progression with higher rates of distant metastasis and mortality (zhang2023riskfactorsfor pages 1-2).

**Frequency:**
- The proportion of thyroid cancers classified as FTC ranges from 4-15% depending on geographic region, iodine status, and classification schemes (kitahara2022epidemiologyofthyroid pages 1-3, forma2025thyroidcancerepidemiology pages 1-2, fagin2023pathogenesisofcancers pages 1-3).

### Quality of Life Impact

Advanced or metastatic FTC significantly impacts quality of life through disease burden and treatment-related morbidity. Systemic therapies for radioiodine-refractory disease, particularly multikinase inhibitors, are associated with substantial adverse events including fatigue, hypertension, gastrointestinal toxicity, hand-foot syndrome, and weight loss, necessitating dose reductions and careful quality-of-life considerations in treatment timing (vico2025systemictherapeuticoptions pages 1-2).

---

## 4. GENETIC/MOLECULAR INFORMATION

### Causal Genes

The primary genetic drivers of FTC include:

**RAS genes (NRAS, HRAS, KRAS):** RAS mutations are among the most frequent genetic alterations in FTC and constitute the molecular hallmark of "RAS-like" follicular-patterned thyroid tumors (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2). These point mutations constitutively activate both MAPK and PI3K/AKT signaling.

**PAX8-PPARG fusion:** This chromosomal rearrangement results from t(2;3)(q13;p25) translocation and is characteristic of FTC (prete2020updateonfundamental pages 1-3, calafato2025somaticgeneticalterations pages 1-2). The fusion gene product combines the DNA-binding domain of PAX8 (a thyroid-specific transcription factor) with the ligand-binding domain of the peroxisome proliferator-activated receptor gamma (PPARG), dysregulating cellular differentiation and metabolism.

### Pathogenic Variants

**RAS mutations:**
- **Affected genes:** NRAS, HRAS, KRAS (HGNC IDs: 7989, 5173, 6407)
- **Variant classification:** Pathogenic activating mutations
- **Variant type:** Point mutations (missense), typically at codons 12, 13, and 61
- **Origin:** Somatic
- **Functional consequence:** Gain of function; constitutive activation of RAS-MAPK and PI3K/AKT signaling
- **Clinical significance:** Truncal driver event in follicular-patterned tumors; associated with tumor initiation and vascular invasion (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2)

**PAX8-PPARG fusion:**
- **Variant type:** Structural rearrangement/gene fusion
- **Origin:** Somatic
- **Functional consequence:** Neomorphic function; aberrant transcriptional regulation
- **Clinical significance:** Supports FTC diagnosis; implicated in tumorigenesis (prete2020updateonfundamental pages 1-3, calafato2025somaticgeneticalterations pages 1-2)

**PTEN alterations:**
- **Variant classification:** Pathogenic inactivating mutations or deletions
- **Variant type:** Various (missense, nonsense, frameshift, deletion)
- **Allele frequency:** Low in general population; germline PTEN mutations define Cowden syndrome
- **Origin:** Somatic in sporadic FTC; germline in hereditary cases
- **Functional consequence:** Loss of function; derepression of PI3K/AKT signaling
- **Clinical significance:** Promotes FTC initiation and progression; relevant to aggressive biology (prete2020updateonfundamental pages 1-3, calafato2025somaticgeneticalterations pages 1-2)

**TP53 mutations:**
- **Variant classification:** Pathogenic
- **Origin:** Somatic
- **Functional consequence:** Loss of tumor suppressor function
- **Clinical significance:** Rare in well-differentiated FTC (~26% in PDTC, ~80% in ATC); associated with dedifferentiation and progression to high-grade disease (kitahara2022epidemiologyofthyroid pages 1-3, prete2020updateonfundamental pages 1-3, calafato2025somaticgeneticalterations pages 1-2)

**TERT promoter mutations:**
- **Variant type:** Promoter mutations
- **Origin:** Somatic
- **Functional consequence:** Telomerase activation
- **Clinical significance:** Strong marker of aggressiveness, dedifferentiation, recurrence, and poor outcomes; progression event rather than initiating lesion (kitahara2022epidemiologyofthyroid pages 1-3, prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2)

### Modifier Genes

No specific modifier genes unique to FTC were identified in the retrieved literature, though co-occurring mutations in TP53 and TERT promoter regions modify disease severity and progression (prete2020updateonfundamental pages 1-3, calafato2025somaticgeneticalterations pages 1-2).

### Epigenetic Information

Epigenetic alterations in FTC are less well characterized than genetic mutations. DNA methylation patterns and histone modifications likely contribute to disease pathogenesis, but specific epigenetic signatures for FTC were not detailed in the retrieved papers (prete2020updateonfundamental pages 1-3).

### Chromosomal Abnormalities

Comprehensive microarray analysis identified recurrent regions of loss of heterozygosity (LOH) in FTC, including:
- **16p12.1:** Most common LOH present in both FTC and FTA, encompassing cancer-related genes including TP53
- **3p21.31:** Recurrent LOH region
- **12q24.11-q24.13:** More frequently detected in FTC than FTA, overlapping FOXN4, MYL2, and PTPN11 genes
- **11p11.2-p11.12:** LOH present exclusively in FTA patients (56%) versus FTC (0%), suggesting a differentiating rearrangement (borowczyk2023follicularthyroidadenoma pages 1-2)

---

## 5. ENVIRONMENTAL INFORMATION

### Environmental Factors

As detailed in Section 2 (Etiology), environmental toxicants including organochlorines, pesticides, PCBs, phthalates, bisphenol A, heavy metals, and air pollution have been associated with thyroid cancer risk (forma2025thyroidcancerepidemiology pages 1-2, kruger2022thyroidcarcinomaa pages 1-2). These endocrine-disrupting chemicals can interfere with thyroid hormone synthesis, transport, and receptor binding, potentially contributing to thyroid carcinogenesis.

### Lifestyle Factors

**Obesity** has emerged as an important thyroid cancer risk factor, though underlying biological mechanisms remain incompletely understood (kitahara2022epidemiologyofthyroid pages 1-3, crncic2020riskfactorsfor pages 1-2). Other lifestyle factors such as smoking, diet, exercise, and alcohol consumption have not been consistently established as FTC-specific risk factors in the retrieved literature.

### Infectious Agents

No infectious agents are known to cause or trigger FTC. Thyroid follicular carcinomas are not associated with viral or bacterial pathogens.

---

## 6. MECHANISM / PATHOPHYSIOLOGY

### Molecular Pathways

The molecular pathogenesis of FTC fundamentally involves constitutive activation of two major signaling cascades:

**MAPK Pathway (RTK-RAS-RAF-MEK-ERK):**
RAS mutations in FTC activate the MAPK pathway, though typically to a lesser extent than BRAF V600E mutations in PTC (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2). This moderate "RAS-like" MAPK output is associated with the follicular architecture and more differentiated phenotype characteristic of FTC. The MAPK pathway regulates cell proliferation, differentiation, and survival.

**Suggested GO terms:**
- GO:0000165: MAPK cascade
- GO:0007265: Ras protein signal transduction

**PI3K/PTEN/AKT Pathway:**
PI3K pathway activation is particularly critical in FTC biology, driven by RAS mutations, PIK3CA/AKT1 activating mutations, and PTEN loss (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2). This pathway promotes cell growth, metabolism, survival, and invasive behavior. The PI3K/AKT pathway is more prominently dysregulated in FTC compared to PTC.

**Suggested GO terms:**
- GO:0014065: phosphatidylinositol 3-kinase signaling
- GO:0043491: protein kinase B signaling

### Cellular Processes

**Cell Proliferation and Cycle Dysregulation:**
Network analysis of FTC versus FTA identified differential expression of cell cycle regulators including CDK1, CCNB2, and TOP2A, suggesting dysregulated proliferation distinguishes malignant from benign follicular lesions (hossain2020networkbasedgeneticprofiling pages 1-3). p53 signaling pathway alterations also contribute to cell cycle checkpoint dysfunction in aggressive FTC (hossain2020networkbasedgeneticprofiling pages 1-3).

**Suggested GO terms:**
- GO:0007049: cell cycle
- GO:0008283: cell proliferation
- GO:0000278: mitotic cell cycle

**Apoptosis and Cell Survival:**
PI3K/AKT pathway activation promotes cell survival by inhibiting apoptotic pathways, contributing to tumor cell persistence and resistance to cell death signals (prete2020updateonfundamental pages 1-3, calafato2025somaticgeneticalterations pages 1-2).

**Suggested GO terms:**
- GO:0006915: apoptotic process
- GO:0008219: cell death

### Protein Dysfunction

**RAS Proteins:**
Mutant RAS proteins are locked in the active GTP-bound state, resulting in constitutive activation of downstream effectors including RAF kinases and PI3K (prete2020updateonfundamental pages 1-3, calafato2025somaticgeneticalterations pages 1-2).

**PAX8-PPARG Fusion Protein:**
The chimeric PAX8-PPARG protein exhibits neomorphic transcriptional activity, dysregulating genes involved in cellular differentiation, metabolism, and growth control (prete2020updateonfundamental pages 1-3, calafato2025somaticgeneticalterations pages 1-2).

**PTEN Loss:**
Loss of PTEN phosphatase function results in unopposed PI3K signaling and accumulation of phosphatidylinositol (3,4,5)-trisphosphate (PIP3), promoting AKT activation and downstream oncogenic effects (prete2020updateonfundamental pages 1-3, calafato2025somaticgeneticalterations pages 1-2).

### Metabolic Changes

One-carbon metabolism and folate pathway dysregulation were identified as differentially enriched in FTC compared to FTA, suggesting metabolic reprogramming contributes to malignant transformation (hossain2020networkbasedgeneticprofiling pages 1-3). Specific metabolomic signatures unique to FTC were not comprehensively detailed in the retrieved literature.

### Tissue Damage Mechanisms

FTC demonstrates characteristic **capsular and vascular invasion**, which defines its malignant behavior histopathologically (zhang2023riskfactorsfor pages 1-2, singh2021thegenomiclandscape pages 1-2, borowczyk2023follicularthyroidadenoma pages 1-2). Widely invasive FTC shows extensive vascular invasion and is associated with hematogenous dissemination to distant sites, particularly lung and bone (zhang2023riskfactorsfor pages 1-2).

### Biochemical Abnormalities

While FTC retains some degree of thyroid follicular cell differentiation, advanced or dedifferentiated tumors may lose expression of thyroid-specific genes including thyroglobulin (TG), thyroid peroxidase (TPO), and the sodium-iodide symporter (NIS), resulting in reduced radioiodine avidity and defining radioiodine-refractory disease (fagin2023pathogenesisofcancers pages 1-3, vico2025systemictherapeuticoptions pages 1-2).

### Molecular Profiling

**Transcriptomics:**
Gene expression profiling studies have identified differentially expressed genes (DEGs) between FTC and FTA, including 598 DEGs in one comprehensive microarray study (133 upregulated, 465 downregulated in FTC) (hossain2020networkbasedgeneticprofiling pages 1-3). Hub genes identified through protein-protein interaction analysis include TOP2A, JUN, EGFR, CDK1, FOS, CDKN3, EZH2, TYMS, PBK, CDH1, UBE2C, and CCNB2 (hossain2020networkbasedgeneticprofiling pages 1-3).

**Genomic Structural Features:**
Loss of heterozygosity (LOH) and copy number alterations are more frequent in FTC compared to FTA, suggesting genomic instability contributes to malignant progression (borowczyk2023follicularthyroidadenoma pages 1-2).

---

## 7. ANATOMICAL STRUCTURES AFFECTED

### Organ Level

**Primary Organ:**
- **Thyroid gland** (UBERON:0002046)

The thyroid gland is the primary site of FTC origin. The disease arises from thyroid follicular epithelial cells, which are the functional units responsible for thyroid hormone synthesis (forma2025thyroidcancerepidemiology pages 1-2, fagin2023pathogenesisofcancers pages 1-3, hu2021thyroidcarcinomaphenotypic pages 1-2).

**Secondary Organ Involvement:**
- **Lungs** (UBERON:0002048): Common site of hematogenous metastasis
- **Bone** (UBERON:0001474): Common site of hematogenous metastasis
- **Liver** (UBERON:0002107): Less common metastatic site
- **Brain** (UBERON:0000955): Rare metastatic site

FTC demonstrates a propensity for distant hematogenous spread, distinguishing it from PTC which more commonly metastasizes to regional lymph nodes (zhang2023riskfactorsfor pages 1-2, singh2021thegenomiclandscape pages 1-2).

### Tissue and Cell Level

**Tissue Types:**
- **Thyroid follicular epithelium:** The tissue of origin for FTC
- **Vascular tissues:** Sites of tumor invasion in FTC

**Cell Populations:**
- **Thyroid follicular cells** (CL:0000477): The cell type from which FTC arises
- **Thyroid follicular epithelial cells** produce thyroid hormones and are characterized by expression of thyroid-specific genes including thyroglobulin, thyroid peroxidase, and sodium-iodide symporter (fagin2023pathogenesisofcancers pages 1-3)

**Suggested Cell Ontology terms:**
- CL:0000477: thyroid follicular cell
- CL:0000066: epithelial cell

### Subcellular Level

Molecular alterations in FTC affect multiple cellular compartments:

**Plasma membrane:**
- Receptor tyrosine kinases (RTKs) and RAS proteins localize to the plasma membrane

**Cytoplasm:**
- MAPK and PI3K/AKT signaling cascades operate in the cytoplasm

**Nucleus:**
- Transcription factors including PAX8, PPARG, and downstream effectors of MAPK/AKT signaling regulate gene expression in the nucleus

**Suggested GO Cellular Component terms:**
- GO:0005886: plasma membrane
- GO:0005737: cytoplasm
- GO:0005634: nucleus

---

## 8. TEMPORAL DEVELOPMENT

### Onset

**Typical Age of Onset:**
- **Adult-onset:** FTC is predominantly diagnosed in adults, with peak incidence in the fifth to sixth decades of life (approximately age 55 in women and 65 in men) (kitahara2022epidemiologyofthyroid pages 1-3, forma2025thyroidcancerepidemiology pages 1-2, zhang2023riskfactorsfor pages 1-2).

**Onset Pattern:**
- **Insidious:** FTC typically develops slowly and is often detected incidentally or during evaluation of a thyroid nodule. Many patients are asymptomatic at diagnosis.

### Progression

**Disease Stages:**
FTC is staged according to the American Joint Committee on Cancer (AJCC) TNM staging system:
- **Stage I-II:** Localized disease confined to the thyroid
- **Stage III:** Regional lymph node involvement (less common in FTC than PTC)
- **Stage IV:** Distant metastatic disease

**Histopathologic Classification:**
- **Minimally invasive FTC:** Limited capsular and/or minimal vascular invasion; better prognosis
- **Widely invasive FTC:** Extensive vascular invasion; associated with higher rates of distant metastasis and mortality (zhang2023riskfactorsfor pages 1-2)
- **Poorly differentiated thyroid carcinoma (PDTC):** May arise from dedifferentiation of FTC
- **Anaplastic thyroid carcinoma (ATC):** Rare progression from FTC with complete loss of differentiation (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2)

**Progression Rate:**
- Variable; minimally invasive FTC often demonstrates indolent behavior, whereas widely invasive FTC progresses more rapidly with higher metastatic potential (zhang2023riskfactorsfor pages 1-2).

**Disease Course:**
- Generally chronic and progressive; some patients develop radioiodine-refractory disease (5-15% of DTC cases), which carries a poorer prognosis with median overall survival of 2.5-3.5 years after distant metastasis (vico2025systemictherapeuticoptions pages 1-2).

**Disease Duration:**
- Chronic lifelong; even treated patients require long-term surveillance for recurrence.

### Progression Molecular Events

Progression from well-differentiated FTC to poorly differentiated or anaplastic carcinoma involves acquisition of additional oncogenic alterations:
- **TP53 mutations:** Present in ~26% of PDTC and ~80% of ATC, rare in well-differentiated FTC (kitahara2022epidemiologyofthyroid pages 1-3, prete2020updateonfundamental pages 1-3, calafato2025somaticgeneticalterations pages 1-2)
- **TERT promoter mutations:** Strongly associated with disease dedifferentiation, recurrence, and poor outcomes (kitahara2022epidemiologyofthyroid pages 1-3, prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2)
- **Additional PI3K pathway alterations:** Further activation of PI3K/AKT signaling
- **Chromatin remodeling alterations:** Contribute to dedifferentiation (fagin2023pathogenesisofcancers pages 1-3)

### Patterns

**Remission:**
- Treatment-induced remission is possible with complete surgical resection and radioiodine ablation in iodine-avid disease.

**Recurrence:**
- Local recurrence and distant metastasis can occur years after initial treatment, necessitating long-term surveillance.

---

## 9. INHERITANCE AND POPULATION

### Epidemiology

**Prevalence and Incidence:**
- FTC accounts for approximately 6-10% of all thyroid cancers globally, with variation by geographic region and iodine status (kitahara2022epidemiologyofthyroid pages 1-3, forma2025thyroidcancerepidemiology pages 1-2, fagin2023pathogenesisofcancers pages 1-3, capdevila2022moleculardiagnosisand pages 1-2).
- Overall thyroid cancer incidence has risen dramatically over recent decades, though this increase is primarily attributable to increased detection of papillary microcarcinomas rather than FTC (kitahara2022epidemiologyofthyroid pages 1-3, forma2025thyroidcancerepidemiology pages 1-2).
- In 2022, an estimated 821,214 thyroid cancer cases were diagnosed worldwide, with FTC representing a minority subset (vico2025systemictherapeuticoptions pages 1-2).

### Population Demographics

**Sex Ratio:**
- Thyroid cancer overall is approximately **3 times more common in females than males** (kitahara2022epidemiologyofthyroid pages 1-3, forma2025thyroidcancerepidemiology pages 1-2, singh2021thegenomiclandscape pages 1-2, kruger2022thyroidcarcinomaa pages 1-2).
- However, **male sex is associated with worse FTC-specific outcomes** despite lower incidence (zhang2023riskfactorsfor pages 1-2).

**Age Distribution:**
- Incidence increases from adolescence through middle age, peaking around age 55 in women and 65 in men (kitahara2022epidemiologyofthyroid pages 1-3, forma2025thyroidcancerepidemiology pages 1-2).
- Mean age at thyroid cancer diagnosis is approximately 51 years (forma2025thyroidcancerepidemiology pages 1-2).

**Geographic Distribution:**
- Highest thyroid cancer incidence rates are reported in South Korea, Canada, Italy, France, Israel, Croatia, Austria, United States, Turkey, Brazil, Costa Rica, China, and Pacific island regions (kitahara2022epidemiologyofthyroid pages 1-3, forma2025thyroidcancerepidemiology pages 1-2, kruger2022thyroidcarcinomaa pages 1-2).
- FTC historically represents a larger proportion of thyroid cancers in iodine-deficient regions compared to iodine-sufficient areas (forma2025thyroidcancerepidemiology pages 1-2, crncic2020riskfactorsfor pages 1-2).

**Affected Populations:**
- Thyroid cancer incidence varies by ethnicity, with higher rates in white populations compared to Black individuals in the United States (forma2025thyroidcancerepidemiology pages 1-2).

### Inheritance Pattern

**Sporadic vs. Familial:**
- The vast majority (>90%) of FTC cases are sporadic, arising from somatic genetic alterations (crncic2020riskfactorsfor pages 1-2).
- Approximately **3-9% of thyroid cancers are familial non-medullary thyroid carcinoma (FNMTC)**, with PTC being the predominant histology in familial cases (crncic2020riskfactorsfor pages 1-2).

**Hereditary Syndromes:**
- **Cowden syndrome (PTEN hamartoma tumor syndrome):** Autosomal dominant; predisposes to follicular-patterned thyroid neoplasms
- **Familial adenomatous polyposis:** Autosomal dominant; associated with increased thyroid cancer risk
- **Carney complex:** Autosomal dominant; associated with thyroid neoplasms
- **Werner syndrome:** Autosomal recessive; associated with high neoplasm incidence including thyroid cancer (crncic2020riskfactorsfor pages 1-2)

**Penetrance:**
- For hereditary syndromes, penetrance varies by specific syndrome and mutation.

---

## 10. DIAGNOSTICS

### Clinical Tests

**Laboratory Tests:**
- **Thyroid function tests:** TSH, free T4, free T3 to assess thyroid function
- **Thyroglobulin (Tg):** Tumor marker used for surveillance after thyroidectomy; rising Tg levels may indicate recurrence
- **Thyroglobulin antibodies:** Measured to interpret Tg levels accurately
- **Calcitonin and CEA:** Not applicable to FTC (used for medullary thyroid carcinoma)

**Suggested LOINC terms:**
- LOINC:3016-3: Thyrotropin [Units/volume] in Serum or Plasma
- LOINC:3013-0: Thyroglobulin [Mass/volume] in Serum or Plasma

**Imaging Studies:**
- **Thyroid ultrasound:** Primary imaging modality for evaluating thyroid nodules; can assess nodule characteristics, size, vascularity, and cervical lymph nodes
- **Fine-needle aspiration (FNA) biopsy:** Gold standard for cytologic evaluation of thyroid nodules, though FNA alone cannot definitively distinguish follicular carcinoma from follicular adenoma due to reliance on histologic invasion criteria (borowczyk2023follicularthyroidadenoma pages 1-2, capdevila2022moleculardiagnosisand pages 1-2)
- **Radioiodine whole-body scan:** Used post-thyroidectomy to assess for residual thyroid tissue and metastatic disease in iodine-avid tumors
- **18F-FDG PET/CT:** Used in radioiodine-refractory disease to assess metabolic activity and extent of metastatic disease (vico2025systemictherapeuticoptions pages 1-2)
- **CT, MRI:** Cross-sectional imaging for staging and surveillance

**Biopsy Findings:**
- **Histopathology:** Definitive diagnosis of FTC requires demonstration of capsular invasion and/or vascular invasion on surgical pathology specimens
- **Minimally invasive FTC:** Shows limited capsular penetration or minimal vascular invasion
- **Widely invasive FTC:** Shows extensive vascular invasion
- **Cytology (FNA):** May show follicular-patterned cells, but cannot distinguish benign from malignant follicular lesions preoperatively (borowczyk2023follicularthyroidadenoma pages 1-2)

### Genetic Testing

**Molecular Testing:**
Modern molecular testing panels can identify genetic alterations in FTC, particularly useful for indeterminate thyroid nodules:

- **RAS mutations (NRAS, HRAS, KRAS):** Detected by targeted sequencing or gene panels
- **PAX8-PPARG fusion:** Detected by FISH or next-generation sequencing
- **PTEN mutations:** Particularly relevant in hereditary contexts
- **TP53 and TERT promoter mutations:** Markers of aggressive disease and dedifferentiation
- **Comprehensive genomic panels:** Next-generation sequencing (NGS) panels are increasingly used for molecular characterization (capdevila2022moleculardiagnosisand pages 1-2, capdevila2022moleculardiagnosisand pages 3-4)

**Suggested Resources:**
- Genetic Testing Registry (GTR)
- ClinVar
- ThyroSeq and other commercial thyroid nodule molecular testing panels

### Omics-Based Diagnostics

**Transcriptomics:**
Gene expression classifiers have been developed to aid in preoperative risk stratification of indeterminate thyroid nodules, though FTC-specific classifiers are less established than those for PTC (hossain2020networkbasedgeneticprofiling pages 1-3).

**Liquid Biopsy:**
Circulating tumor DNA and other liquid biopsy approaches are emerging as non-invasive tools for disease monitoring, though clinical application in FTC remains investigational (prete2020updateonfundamental pages 1-3).

### Clinical Criteria

**Diagnostic Criteria:**
- Histopathologic diagnosis of FTC based on demonstration of capsular and/or vascular invasion in a follicular-patterned thyroid neoplasm (borowczyk2023follicularthyroidadenoma pages 1-2, capdevila2022moleculardiagnosisand pages 1-2)

**Differential Diagnosis:**
- **Follicular thyroid adenoma (FTA):** Benign follicular neoplasm without capsular or vascular invasion; cannot be reliably distinguished from FTC by FNA cytology alone
- **Papillary thyroid carcinoma, follicular variant:** Distinguished by nuclear features of PTC
- **Hürthle cell (oncocytic) carcinoma:** Now classified separately from FTC in the 2022 WHO classification (hu2021thyroidcarcinomaphenotypic pages 1-2, singh2021thegenomiclandscape pages 1-2)
- **Hyperplastic/adenomatous nodule:** Benign proliferation

### Screening

**Newborn Screening:**
- Not applicable to FTC.

**Carrier Screening:**
- Genetic counseling and testing for individuals with family history of hereditary syndromes associated with thyroid cancer (e.g., Cowden syndrome) (crncic2020riskfactorsfor pages 1-2).

**Cascade Screening:**
- Evaluation of first-degree relatives of patients with hereditary thyroid cancer syndromes.

| Treatment modality | Typical indication in FTC | Key details / timing | Efficacy data | Important adverse events / limitations | Evidence |
|---|---|---|---|---|---|
| Lobectomy (hemithyroidectomy) | Selected localized, lower-risk differentiated thyroid carcinoma including some FTCs when disease is intrathyroidal and limited | Extent of surgery is determined by preoperative risk assessment; lobectomy may be used for selected lower-risk disease, whereas more extensive surgery is favored for higher-risk tumors. FTC often requires definitive histopathology to demonstrate capsular/vascular invasion because cytology cannot reliably distinguish adenoma from carcinoma | In an FTC meta-analysis, lobectomy itself was **not associated with increased risk of death** compared with more extensive surgery, suggesting appropriateness in carefully selected patients (zhang2023riskfactorsfor pages 1-2) | Limitation: may be insufficient if postoperative pathology shows higher-risk features requiring completion thyroidectomy; preoperative discrimination from follicular adenoma remains difficult (borowczyk2023follicularthyroidadenoma pages 1-2, capdevila2022moleculardiagnosisand pages 1-2) | (zhang2023riskfactorsfor pages 1-2, borowczyk2023follicularthyroidadenoma pages 1-2, capdevila2022moleculardiagnosisand pages 1-2) |
| Total thyroidectomy | Standard approach for many DTC/FTC cases with bilateral disease, larger tumors, invasive disease, or when postoperative radioactive iodine (RAI) is planned | Frequently followed by RAI ablation in DTC/FTC; preferred when disease burden or risk profile is higher and when surveillance with thyroglobulin/RAI is needed | Standard treatment for most higher-risk DTC; localized DTC treated with thyroidectomy ± RAI has **10-year survival >90%** in localized disease (broader DTC data) (vico2025systemictherapeuticoptions pages 1-2) | Risks include hypoparathyroidism and recurrent laryngeal nerve injury; does not prevent later RAI-refractory progression in a minority of patients | (capdevila2022moleculardiagnosisand pages 1-2, vico2025systemictherapeuticoptions pages 1-2) |
| Completion thyroidectomy / radical resection when indicated | Post-lobectomy high-risk pathology, residual disease, or non-radical initial surgery | Considered when final pathology reveals invasive FTC, multifocality, larger tumor, or features warranting RAI and more complete resection | FTC meta-analysis found **non-radical resection** associated with increased mortality risk, supporting complete oncologic surgery when feasible (zhang2023riskfactorsfor pages 1-2) | Surgical morbidity; decision individualized by tumor extent and patient factors | (zhang2023riskfactorsfor pages 1-2) |
| Radioactive iodine (RAI) therapy | Adjuvant or therapeutic use after thyroidectomy in iodine-avid differentiated thyroid carcinoma, including FTC | Cornerstone of DTC management because thyroid follicular cells retain iodide-handling machinery; best suited to iodine-avid residual, recurrent, or metastatic disease | Standard and often effective in DTC; however, approximately **5–15%** of DTC patients develop RAI-refractory disease with poorer prognosis (vico2025systemictherapeuticoptions pages 1-2) | Ineffective once tumors lose iodine avidity; repeated ineffective RAI should be avoided in true RAI-refractory disease | (fagin2023pathogenesisofcancers pages 1-3, capdevila2022moleculardiagnosisand pages 1-2, vico2025systemictherapeuticoptions pages 1-2) |
| Active surveillance | Indolent, asymptomatic, low-burden RAI-refractory or metastatic differentiated thyroid carcinoma, including selected FTC | Appropriate when tumor growth is slow, burden is low, and there is no threatening location or major symptom burden; local therapies can be used for oligoprogression | No response-rate metric because this is a monitoring strategy; recommended in reviews/guidelines for slowly progressive RAI-refractory disease (vico2025systemictherapeuticoptions pages 1-2) | Risk of under-treating patients with accelerating disease; requires serial imaging and multidisciplinary reassessment | (vico2025systemictherapeuticoptions pages 1-2) |
| Indications for systemic therapy in RAI-refractory disease | Progressive, symptomatic, multifocal, or organ-threatening RAI-refractory FTC/DTC | ATA/ESMO-style guidance in reviews recommends systemic treatment for **rapid and/or symptomatic progression involving multiple lesions or organs**, while reserving surveillance for indolent disease (vico2025systemictherapeuticoptions pages 1-2) | Systemic therapy improves progression-free survival but carries significant toxicity burden; timing should balance disease kinetics and QoL (vico2025systemictherapeuticoptions pages 1-2) | Hypertension, fatigue, GI toxicity, hand-foot effects, weight loss, dose reductions common with MKIs | (vico2025systemictherapeuticoptions pages 1-2) |
| Lenvatinib (multikinase inhibitor; first-line) | First-line systemic therapy for advanced progressive RAI-refractory DTC, including FTC | Often favored when disease is clearly progressive/symptomatic and tumor shrinkage is desired; used after thyroidectomy/RAI failure | Real-world multicenter DTC study: **disease control rate 97.7%**, **median PFS 21.8 months**, first objective response at **3.8 months** (vico2025systemictherapeuticoptions pages 1-2). Reviews identify lenvatinib as standard first-line therapy for RAI-R DTC (vico2025systemictherapeuticoptions pages 1-2) | In the Korean study, **all patients** had adverse events; **grade 3–4 AEs 23.2%**; common AE was fatigue/asthenia; dose reduction from 20 mg median start to 10 mg sustainable dose was common (vico2025systemictherapeuticoptions pages 1-2) | (vico2025systemictherapeuticoptions pages 1-2) |
| Sorafenib (multikinase inhibitor; first-line) | First-line option for advanced progressive RAI-refractory DTC, including FTC | Alternative to lenvatinib; may be selected based on comorbidity, clinician familiarity, and toxicity considerations | Established first-line option from DECISION-era evidence summarized in reviews; improves PFS versus placebo in RAI-R DTC, though no FTC-only metrics were provided in retrieved contexts (vico2025systemictherapeuticoptions pages 1-2) | Class toxicities include hand-foot skin reaction, diarrhea, fatigue, hypertension, weight loss; may be less tumor-shrinking than lenvatinib in practice | (vico2025systemictherapeuticoptions pages 1-2) |
| Cabozantinib (multikinase inhibitor; second-line) | Second-line therapy for RAI-refractory DTC/FTC after progression on VEGFR-targeted MKIs such as lenvatinib and/or sorafenib | Used after failure of first-line MKIs; now recognized as standard resistant-case option in reviews | Reviews state cabozantinib is the **standard second-line treatment** for RAI-R thyroid carcinoma after prior VEGFR-targeted therapy; specific ORR/PFS values were not provided in retrieved contexts (vico2025systemictherapeuticoptions pages 1-2) | Significant TKI toxicities; careful monitoring required | (vico2025systemictherapeuticoptions pages 1-2) |
| RET inhibitor: Selpercatinib | RET fusion-positive advanced thyroid cancer, including rare follicular-cell derived tumors with RET fusions | Requires molecular testing; suited for patients with actionable RET fusion, especially after RAI-refractory progression | In previously treated **RET fusion-positive thyroid cancer**, **ORR 78.9%** (2 CR, 13 PR); in treatment-naive RET-altered thyroid cancer, **ORR 100%** in a very small cohort (1 CR, 7 PR) (capdevila2022moleculardiagnosisand pages 3-4) | **94%** experienced at least one treatment-related AE; **28% grade 3** and **2% grade 4** treatment-related AEs in cited study summary (capdevila2022moleculardiagnosisand pages 3-4) | (capdevila2022moleculardiagnosisand pages 1-2, capdevila2022moleculardiagnosisand pages 3-4) |
| RET inhibitor: Pralsetinib | Advanced/metastatic RET fusion-positive thyroid cancer requiring systemic therapy; also RET-mutant MTC | Requires identification of RET fusion; another selective RET-targeted option | In PTC cohort summarized in review, **ORR 89%** (all PRs) for RET-altered thyroid cancer subgroup (capdevila2022moleculardiagnosisand pages 3-4) | **15%** experienced serious treatment-related adverse events in cited summary (capdevila2022moleculardiagnosisand pages 3-4) | (capdevila2022moleculardiagnosisand pages 1-2, capdevila2022moleculardiagnosisand pages 3-4) |
| NTRK inhibitor: Larotrectinib | NTRK fusion-positive advanced thyroid cancer including FTC | Requires molecular testing for NTRK1/2/3 fusion; tumor-agnostic targeted option | In **29 patients** with TRK fusion thyroid cancer (**FTC n=2**), among 28 evaluable patients **ORR 71%**; response rate **86% in DTC** and **29% in ATC** (capdevila2022moleculardiagnosisand pages 3-4) | Favorable safety profile; **7% grade 3** treatment-related AE in cited study summary (capdevila2022moleculardiagnosisand pages 3-4) | (capdevila2022moleculardiagnosisand pages 1-2, capdevila2022moleculardiagnosisand pages 3-4) |
| NTRK inhibitor: Entrectinib | NTRK fusion-positive advanced thyroid cancer | Alternative TRK inhibitor after fusion detection | In thyroid cancer cohort summarized in review, **ORR 53.8%** and median duration of response **13.2 months** (subtypes not fully specified) (capdevila2022moleculardiagnosisand pages 3-4) | Multi-target kinase profile may broaden off-target toxicities relative to highly selective TRK inhibition | (capdevila2022moleculardiagnosisand pages 1-2, capdevila2022moleculardiagnosisand pages 3-4) |
| BRAF/MEK-targeted therapy (dabrafenib + trametinib) | Primarily BRAF V600E-mutated ATC; relevance to FTC is limited because classic FTC is usually RAS-like rather than BRAF-driven | Important mainly for thyroid cancers with BRAF V600E; may also inform redifferentiation strategies in selected follicular-cell derived cancers | Review table reports high activity in BRAF V600E ATC (**ORR 69%**) and activity in PTC, but FTC-specific evidence was not provided in retrieved contexts (capdevila2022moleculardiagnosisand pages 3-4) | Not a standard FTC treatment absent a targetable BRAF alteration; molecular matching required | (capdevila2022moleculardiagnosisand pages 1-2, capdevila2022moleculardiagnosisand pages 3-4) |
| Redifferentiation therapy (e.g., sorafenib or trametinib plus RAI concepts) | Investigational strategy for RAI-refractory follicular-cell derived thyroid cancers that may regain iodine uptake | Intended to re-sensitize dedifferentiated tumors to RAI; discussed as promising but not yet definitive | Reviews note **promising, but not excellent** results, with sorafenib and trametinib included in redifferentiation protocols (vico2025systemictherapeuticoptions pages 1-2) | Experimental/selected-center use; benefit inconsistent and not yet routine standard of care | (vico2025systemictherapeuticoptions pages 1-2) |
| Immunotherapy / ICI-based approaches | Investigational or selected advanced RAI-refractory disease, often in combination strategies | Under study, especially combined with TKIs or in more aggressive dedifferentiated disease | Reviews describe ICIs as **promising** and under investigation rather than established standard therapy for FTC (vico2025systemictherapeuticoptions pages 1-2) | Response predictors and optimal combinations remain uncertain; immune toxicities apply | (fagin2023pathogenesisofcancers pages 1-3, vico2025systemictherapeuticoptions pages 1-2) |
| Local therapies in metastatic/RAI-refractory disease | Oligoprogression, symptomatic focal lesions, bone metastases, lesions threatening function | Surgery, radiotherapy, or other local ablative approaches may be used before or during systemic therapy; antiresorptives may be added for bone metastases | Useful for disease control in limited progressing sites; no pooled response metrics in retrieved contexts | Not a substitute for systemic therapy in diffuse rapid progression | (vico2025systemictherapeuticoptions pages 1-2) |


*Table: This table summarizes current treatment strategies for follicular thyroid carcinoma, emphasizing surgery, radioactive iodine, systemic therapy for RAI-refractory disease, and biomarker-matched targeted treatments. It highlights when each modality is used, what efficacy has been reported, and the main safety or practical limitations.*

---

## 11. OUTCOME/PROGNOSIS

### Survival and Mortality

**Survival Rates:**
- Differentiated thyroid carcinoma (DTC), including FTC, has an excellent overall **5-year survival rate >98%** when localized (fagin2023pathogenesisofcancers pages 1-3, vico2025systemictherapeuticoptions pages 1-2).
- **10-year survival rate >90%** for localized differentiated thyroid cancer (vico2025systemictherapeuticoptions pages 1-2).
- Prognosis is significantly worse for **radioiodine-refractory (RAI-R) disease**, with median overall survival of **2.5-3.5 years** after development of distant metastases (vico2025systemictherapeuticoptions pages 1-2).

**Mortality Rate:**
- Overall thyroid cancer mortality is relatively low at approximately **0.5 deaths per 100,000 population per year** (kitahara2022epidemiologyofthyroid pages 1-3).
- However, **10-30% mortality rate** has been reported specifically for FTC in some series (zhang2023riskfactorsfor pages 1-2).

### Prognostic Factors

A 2023 systematic review and meta-analysis identified the following significant risk factors associated with increased risk of death in FTC patients:

**Clinical and Demographic Factors:**
- **Age >45 years:** Strongly associated with increased mortality (zhang2023riskfactorsfor pages 1-2)
- **Male sex:** Associated with worse outcomes despite lower incidence (zhang2023riskfactorsfor pages 1-2)

**Tumor Characteristics:**
- **Tumor diameter >4 cm:** Adverse prognostic factor (zhang2023riskfactorsfor pages 1-2)
- **Multifocality:** Associated with increased mortality risk (zhang2023riskfactorsfor pages 1-2)
- **Extrathyroidal extension (ETE):** Adverse prognostic factor (zhang2023riskfactorsfor pages 1-2)
- **Widely invasive histology:** Worse outcomes compared to minimally invasive FTC (zhang2023riskfactorsfor pages 1-2)
- **Cervical lymph node metastasis (CLNM):** Associated with increased risk of death (less common in FTC than PTC) (zhang2023riskfactorsfor pages 1-2)
- **Distant metastases (DM):** Strongest predictor of mortality (zhang2023riskfactorsfor pages 1-2)

**Treatment-Related Factors:**
- **Non-radical tumor resection:** Associated with increased mortality risk (zhang2023riskfactorsfor pages 1-2)
- **Lobectomy vs. total thyroidectomy:** Lobectomy was NOT associated with increased death risk in appropriately selected patients (zhang2023riskfactorsfor pages 1-2)
- **No radioactive iodine (RAI) treatment:** Was NOT associated with increased death in the meta-analysis (zhang2023riskfactorsfor pages 1-2)

**Molecular Factors:**
- **TP53 mutations:** Associated with dedifferentiation and poor outcomes (kitahara2022epidemiologyofthyroid pages 1-3, prete2020updateonfundamental pages 1-3)
- **TERT promoter mutations:** Strong marker of aggressiveness and poor outcomes (kitahara2022epidemiologyofthyroid pages 1-3, prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3)
- **Co-occurring TP53 and TERT mutations:** Particularly adverse (kitahara2022epidemiologyofthyroid pages 1-3, prete2020updateonfundamental pages 1-3)

### Disease Course

**Complications:**
- **Distant metastases:** Lung and bone are most common sites; can cause respiratory compromise, pathologic fractures, and pain
- **Local recurrence:** Can cause compressive symptoms in the neck
- **Radioiodine-refractory disease:** Loss of iodine avidity necessitates alternative systemic therapies (vico2025systemictherapeuticoptions pages 1-2)
- **Progression to poorly differentiated or anaplastic thyroid carcinoma:** Rare but devastating complication (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3)

**Recovery Potential:**
- With complete surgical resection and radioiodine ablation (when iodine-avid), many patients achieve long-term disease-free survival.
- Radioiodine-refractory disease has limited recovery potential; systemic therapies can achieve disease control but rarely curative outcomes (vico2025systemictherapeuticoptions pages 1-2).

---

## 12. TREATMENT

### Pharmacotherapy

**Levothyroxine (Thyroid Hormone Replacement):**
- **Mechanism:** TSH suppression to reduce potential growth stimulus to residual thyroid cells
- **Indication:** All patients post-thyroidectomy require thyroid hormone replacement; degree of TSH suppression is risk-stratified

**Multikinase Inhibitors (MKIs) for RAI-Refractory Disease:**

**Lenvatinib:**
- **Mechanism:** Inhibitor of VEGFR1-3, FGFR1-4, PDGFRα, RET, and KIT
- **Indication:** First-line systemic therapy for advanced progressive RAI-refractory DTC, including FTC
- **Efficacy:** Real-world data showed **disease control rate 97.7%**, **median PFS 21.8 months**, first objective response at **3.8 months** (vico2025systemictherapeuticoptions pages 1-2)
- **Adverse Events:** **100% of patients** experienced adverse events; **grade 3-4 AEs in 23.2%**; most common AE was fatigue/asthenia; dose reduction from median starting dose of 20 mg to sustainable dose of 10 mg was common (vico2025systemictherapeuticoptions pages 1-2)
- **MAXO term suggestion:** MAXO:0000605 (tyrosine kinase inhibitor therapy)

**Sorafenib:**
- **Mechanism:** Inhibitor of VEGFR, PDGFR, RAF kinases
- **Indication:** First-line alternative to lenvatinib for advanced progressive RAI-refractory DTC
- **Efficacy:** Established efficacy from DECISION trial; improves PFS versus placebo
- **Adverse Events:** Hand-foot skin reaction, diarrhea, fatigue, hypertension, weight loss
- **MAXO term suggestion:** MAXO:0000605 (tyrosine kinase inhibitor therapy)

**Cabozantinib:**
- **Mechanism:** Inhibitor of VEGFR, MET, AXL, RET
- **Indication:** Second-line therapy for RAI-refractory DTC after progression on VEGFR-targeted MKIs
- **Efficacy:** Recognized as standard second-line treatment option (vico2025systemictherapeuticoptions pages 1-2)
- **MAXO term suggestion:** MAXO:0000605 (tyrosine kinase inhibitor therapy)

### Advanced Therapeutics

**Targeted Therapies for Molecular Alterations:**

**RET Inhibitors (Selpercatinib, Pralsetinib):**
- **Indication:** RET fusion-positive advanced thyroid cancer (rare in FTC)
- **Efficacy:** High objective response rates (78.9-100% in small cohorts) (capdevila2022moleculardiagnosisand pages 3-4)
- **MAXO term suggestion:** MAXO:0000605 (tyrosine kinase inhibitor therapy)

**NTRK Inhibitors (Larotrectinib, Entrectinib):**
- **Indication:** NTRK fusion-positive thyroid cancer (rare; NTRK fusions reported in 2.5-25.9% of thyroid cancers overall)
- **Efficacy:** **ORR 71%** in thyroid cancer cohort with larotrectinib; **86% response rate in DTC** (capdevila2022moleculardiagnosisand pages 3-4)
- **Safety:** Favorable profile; grade 3 AE rate 7% with larotrectinib (capdevila2022moleculardiagnosisand pages 3-4)
- **MAXO term suggestion:** MAXO:0000605 (tyrosine kinase inhibitor therapy)

**BRAF/MEK Inhibitors (Dabrafenib + Trametinib):**
- **Indication:** BRAF V600E-mutated thyroid cancers (rare in FTC; more relevant to PTC and ATC)
- **MAXO term suggestion:** MAXO:0000605 (tyrosine kinase inhibitor therapy)

**Redifferentiation Therapy:**
- **Concept:** Use of targeted agents (e.g., MEK inhibitors) to restore iodine uptake in dedifferentiated tumors, followed by RAI therapy
- **Status:** Investigational; **promising but not excellent results** reported (vico2025systemictherapeuticoptions pages 1-2)

### Immunotherapy

**Immune Checkpoint Inhibitors (ICIs):**
- **Status:** Under investigation, particularly in combination with tyrosine kinase inhibitors
- **Evidence:** Described as **promising** but not yet established standard therapy for FTC (vico2025systemictherapeuticoptions pages 1-2)
- **Suggested MAXO term:** MAXO:0001481 (immune checkpoint inhibitor therapy)

### Surgical Interventions

**Lobectomy (Hemithyroidectomy):**
- **Indication:** Selected localized, lower-risk differentiated thyroid carcinoma when disease is intrathyroidal and limited
- **Efficacy:** **Not associated with increased risk of death** compared with more extensive surgery in appropriately selected patients (zhang2023riskfactorsfor pages 1-2)
- **MAXO term suggestion:** MAXO:0000136 (lobectomy)

**Total Thyroidectomy:**
- **Indication:** Standard approach for most FTC cases, particularly with bilateral disease, larger tumors, invasive features, or when postoperative radioiodine therapy is planned
- **Efficacy:** Part of standard curative approach achieving **10-year survival >90%** in localized disease (vico2025systemictherapeuticoptions pages 1-2)
- **Complications:** Hypoparathyroidism, recurrent laryngeal nerve injury
- **MAXO term suggestion:** MAXO:0000137 (thyroidectomy)

**Completion Thyroidectomy:**
- **Indication:** Post-lobectomy high-risk pathology revealing invasive FTC, larger tumor, or features warranting RAI
- **Rationale:** **Non-radical resection** associated with increased mortality risk (zhang2023riskfactorsfor pages 1-2)
- **MAXO term suggestion:** MAXO:0000137 (thyroidectomy)

### Radioactive Iodine (RAI) Therapy

**Indication:**
- Adjuvant or therapeutic use after thyroidectomy in iodine-avid differentiated thyroid carcinoma
- Effective for residual, recurrent, or metastatic disease that concentrates iodine

**Efficacy:**
- Cornerstone of DTC management; contributes to excellent long-term survival
- However, approximately **5-15% of DTC patients** develop RAI-refractory disease with poorer prognosis (vico2025systemictherapeuticoptions pages 1-2)

**Limitations:**
- Ineffective once tumors lose iodine avidity; repeated ineffective RAI should be avoided in true RAI-refractory disease

**MAXO term suggestion:** MAXO:0000116 (radioactive iodine therapy)

### Supportive Care

**Active Surveillance:**
- **Indication:** Indolent, asymptomatic, low-burden RAI-refractory or metastatic DTC with slow tumor growth
- **Rationale:** Balances disease control with quality of life; avoids toxicity of systemic therapy in stable disease (vico2025systemictherapeuticoptions pages 1-2)

**Local Therapies:**
- **Surgery, radiotherapy, ablative procedures:** For oligoprogressive disease, symptomatic focal lesions, or organ-threatening metastases
- **Antiresorptive therapy:** For bone metastases

**Symptom Management:**
- Pain control, nutritional support, management of treatment-related adverse events

### Treatment Strategy

**Treatment Algorithms:**
ATA and ESMO clinical guidelines recommend:
- **Initial surgery:** Extent determined by preoperative risk assessment
- **Radioiodine ablation:** For iodine-avid disease post-thyroidectomy
- **Active surveillance:** For slow-growing, asymptomatic RAI-refractory disease
- **Systemic therapy:** For **rapid and/or symptomatic progression involving multiple lesions or organs** in RAI-refractory disease (vico2025systemictherapeuticoptions pages 1-2)

**Treatment Sequencing for RAI-Refractory Disease:**
- **First-line:** Lenvatinib or sorafenib
- **Second-line:** Cabozantinib after progression on VEGFR-targeted MKIs
- **Molecularly guided therapy:** RET inhibitors for RET fusions, NTRK inhibitors for NTRK fusions, BRAF/MEK inhibitors for BRAF V600E mutations (capdevila2022moleculardiagnosisand pages 1-2, capdevila2022moleculardiagnosisand pages 3-4, vico2025systemictherapeuticoptions pages 1-2)

**Personalized Medicine:**
- Next-generation sequencing to identify actionable mutations
- Molecular matching to appropriate targeted therapies
- Consideration of patient comorbidities, disease kinetics, and quality of life in timing of systemic therapy initiation

---

## 13. PREVENTION

### Primary Prevention

**Radiation Avoidance:**
- Minimize unnecessary childhood exposure to ionizing radiation, particularly to the head and neck region
- Appropriate use of diagnostic imaging modalities in children

**Iodine Supplementation:**
- Population-level iodine supplementation programs in iodine-deficient regions may influence thyroid cancer histologic distribution (crncic2020riskfactorsfor pages 1-2)

**Environmental Exposure Reduction:**
- Public health measures to reduce exposure to endocrine-disrupting chemicals, though specific interventions are not well established

### Secondary Prevention

**Screening Programs:**
- No population-based screening programs for thyroid cancer currently recommended
- Increased detection of incidental thyroid nodules through widespread use of imaging has raised concerns about overdiagnosis (kitahara2022epidemiologyofthyroid pages 1-3, forma2025thyroidcancerepidemiology pages 1-2)

**Genetic Screening:**
- **Carrier screening:** For individuals with family history of hereditary syndromes predisposing to thyroid cancer (e.g., Cowden syndrome)
- **Genetic counseling:** For patients with FNMTC or syndromic thyroid cancer
- **Cascade screening:** Evaluation of first-degree relatives of affected individuals (crncic2020riskfactorsfor pages 1-2)

### Tertiary Prevention

**Surveillance:**
- Long-term monitoring for recurrence after initial treatment
- Thyroglobulin measurements and neck ultrasound
- Whole-body radioiodine scans when indicated

**Optimal Treatment:**
- Complete surgical resection when feasible to minimize recurrence risk
- Appropriate use of radioiodine therapy to ablate residual disease

### Behavioral Interventions

No specific lifestyle modifications have been firmly established to reduce FTC risk, though maintaining healthy body weight may have some benefit given the association between obesity and thyroid cancer (crncic2020riskfactorsfor pages 1-2).

---

## 14. OTHER SPECIES / NATURAL DISEASE

### Taxonomy

Limited information on naturally occurring FTC in other species was identified in the retrieved literature. Thyroid tumors have been reported in companion animals and other mammals, though specific FTC data were not detailed (kitahara2022epidemiologyofthyroid pages 1-3).

### Comparative Biology

Thyroid follicular cells and thyroid hormone synthesis pathways are evolutionarily conserved across vertebrate species. However, comparative pathology and cross-species susceptibility to follicular thyroid carcinoma were not comprehensively addressed in the retrieved papers.

---

## 15. MODEL ORGANISMS

### Model Types

**Zebrafish (Danio rerio):**
Zebrafish have emerged as a model organism for thyroid research, including studies of thyroid development, thyroid hormone function, and effects of endocrine-disrupting chemicals on thyroid physiology (kitahara2022epidemiologyofthyroid pages 1-3). While zebrafish models of thyroid cancer were mentioned, specific FTC models were not detailed in the retrieved literature. Zebrafish thyroid follicles can be studied to assess effects of environmental toxicants on thyroid morphology and hormone levels (kitahara2022epidemiologyofthyroid pages 1-3).

**Mouse Models:**
Genetically engineered mouse models (GEMMs) have been developed to study thyroid cancer pathogenesis. Specific models mentioned include:
- **PAX8-PPARG fusion with PTEN loss:** Induces thyroid tumors in transgenic mice, enhancing understanding of FTC molecular pathogenesis (calafato2025somaticgeneticalterations pages 1-2)
- **RAS-mutant models:** Mouse models harboring oncogenic RAS mutations can develop follicular-patterned thyroid neoplasms

**Cell Lines:**
Thyroid cancer cell lines, though not extensively detailed in the retrieved papers, are used for in vitro studies of FTC biology, drug responses, and molecular mechanisms.

### Genetic Models

- **Knockout models:** PTEN knockout models relevant to thyroid tumorigenesis
- **Transgenic models:** Expression of oncogenic RAS or PAX8-PPARG fusions under thyroid-specific promoters
- **CRISPR/Cas9:** Emerging technology for generating precise genetic alterations in model systems

### Model Characteristics

**Phenotype Recapitulation:**
Mouse models expressing PAX8-PPARG fusions with PTEN loss develop thyroid tumors, suggesting they recapitulate some aspects of human FTC molecular pathology (calafato2025somaticgeneticalterations pages 1-2). However, the extent to which these models fully replicate the clinical and biological features of human FTC, including metastatic behavior, remains an area of ongoing research.

**Model Limitations:**
Specific limitations of FTC models, including differences in tumor microenvironment, immune responses, and metastatic patterns compared to human disease, were not comprehensively detailed in the retrieved literature.

### Resources

**Model Organism Databases:**
- Mouse Genome Informatics (MGI)
- Zebrafish Information Network (ZFIN)
- International Mouse Phenotyping Consortium (IMPC)

---

## SUMMARY AND ONTOLOGY TERM SUGGESTIONS

### Disease Classification
- **MONDO term suggestion:** MONDO:0015074 (follicular thyroid carcinoma)
- **ICD-11:** 2D10.1 (Follicular carcinoma of thyroid gland)

### Phenotype Ontology (HPO) Suggestions
- HP:0100646: Thyroid nodule
- HP:0012125: Metastasis
- HP:0012125: Distant metastasis
- HP:0030731: Carcinoma

### Gene Ontology (GO) Suggestions
**Biological Process:**
- GO:0000165: MAPK cascade
- GO:0007265: Ras protein signal transduction
- GO:0014065: phosphatidylinositol 3-kinase signaling
- GO:0043491: protein kinase B signaling
- GO:0007049: cell cycle
- GO:0008283: cell proliferation
- GO:0006915: apoptotic process

**Cellular Component:**
- GO:0005886: plasma membrane
- GO:0005737: cytoplasm
- GO:0005634: nucleus

### Cell Ontology (CL) Suggestions
- CL:0000477: thyroid follicular cell
- CL:0000066: epithelial cell

### UBERON Anatomical Terms
- UBERON:0002046: thyroid gland
- UBERON:0002048: lung (metastatic site)
- UBERON:0001474: bone tissue (metastatic site)

### Medical Action Ontology (MAXO) Suggestions
- MAXO:0000137: thyroidectomy
- MAXO:0000136: lobectomy
- MAXO:0000116: radioactive iodine therapy
- MAXO:0000605: tyrosine kinase inhibitor therapy
- MAXO:0001481: immune checkpoint inhibitor therapy

---

## EVIDENCE SUMMARY

This comprehensive report on thyroid follicular carcinoma synthesizes evidence from 30 scientific papers published between 2020 and 2025, with primary focus on high-quality reviews and recent research from authoritative sources. Key citations include:

- Epidemiology and clinical characteristics: (kitahara2022epidemiologyofthyroid pages 1-3, forma2025thyroidcancerepidemiology pages 1-2, zhang2023riskfactorsfor pages 1-2)
- Molecular pathogenesis and genetics: (prete2020updateonfundamental pages 1-3, fagin2023pathogenesisofcancers pages 1-3, calafato2025somaticgeneticalterations pages 1-2)
- Diagnostic approaches: (borowczyk2023follicularthyroidadenoma pages 1-2, capdevila2022moleculardiagnosisand pages 1-2)
- Treatment modalities: (capdevila2022moleculardiagnosisand pages 1-2, capdevila2022moleculardiagnosisand pages 3-4, vico2025systemictherapeuticoptions pages 1-2)
- Risk factors and etiology: (crncic2020riskfactorsfor pages 1-2, kruger2022thyroidcarcinomaa pages 1-2)

The information provided represents current understanding as of 2025, with recognition that ongoing research continues to refine our knowledge of FTC biology, diagnosis, and treatment. Three comprehensive tables summarizing genetic alterations, epidemiology/prognostic factors, and treatment modalities are provided as artifacts for quick reference.

**Note on Data Limitations:** While extensive literature was reviewed, some specific data points (e.g., precise FTC-specific incidence rates in all populations, comprehensive metabolomics data, detailed animal model characterizations) were not available in the retrieved literature. Where FTC-specific data were lacking, broader differentiated thyroid cancer evidence was cited with appropriate context.

References

1. (forma2025thyroidcancerepidemiology pages 1-2): Alicja Forma, Karolina Kłodnicka, Weronika Pająk, Jolanta Flieger, Barbara Teresińska, Jacek Januszewski, and Jacek Baj. Thyroid cancer: epidemiology, classification, risk factors, diagnostic and prognostic markers, and current treatment strategies. International Journal of Molecular Sciences, 26:5173, May 2025. URL: https://doi.org/10.3390/ijms26115173, doi:10.3390/ijms26115173. This article has 113 citations.

2. (fagin2023pathogenesisofcancers pages 1-3): James A. Fagin, Gnana P. Krishnamoorthy, and Iñigo Landa. Pathogenesis of cancers derived from thyroid follicular cells. Nature Reviews Cancer, 23:631-650, Jul 2023. URL: https://doi.org/10.1038/s41568-023-00598-y, doi:10.1038/s41568-023-00598-y. This article has 85 citations and is from a domain leading peer-reviewed journal.

3. (kitahara2022epidemiologyofthyroid pages 1-3): Cari M. Kitahara and Arthur B. Schneider. Epidemiology of thyroid cancer. Cancer epidemiology, biomarkers & prevention : a publication of the American Association for Cancer Research, cosponsored by the American Society of Preventive Oncology, 31 7:1284-1297, Jul 2022. URL: https://doi.org/10.1158/1055-9965.epi-21-1440, doi:10.1158/1055-9965.epi-21-1440. This article has 330 citations.

4. (singh2021thegenomiclandscape pages 1-2): Amandeep Singh, Jeehoon Ham, Joseph William Po, Navin Niles, Tara Roberts, and Cheok Soon Lee. The genomic landscape of thyroid cancer tumourigenesis and implications for immunotherapy. Cells, 10:1082, May 2021. URL: https://doi.org/10.3390/cells10051082, doi:10.3390/cells10051082. This article has 102 citations.

5. (zhang2023riskfactorsfor pages 1-2): Ting Zhang, Liang He, Zhihong Wang, Wenwu Dong, Wei Sun, Ping Zhang, and Hao Zhang. Risk factors for death of follicular thyroid carcinoma: a systematic review and meta-analysis. Endocrine, 82:457-466, Oct 2023. URL: https://doi.org/10.1007/s12020-023-03466-9, doi:10.1007/s12020-023-03466-9. This article has 32 citations and is from a peer-reviewed journal.

6. (borowczyk2023follicularthyroidadenoma pages 1-2): Martyna Borowczyk, Paula Dobosz, Ewelina Szczepanek-Parulska, Bartłomiej Budny, Szymon Dębicki, Dorota Filipowicz, Elżbieta Wrotkowska, Michalina Oszywa, Frederik A. Verburg, Małgorzata Janicka-Jedyńska, Katarzyna Ziemnicka, and Marek Ruchała. Follicular thyroid adenoma and follicular thyroid carcinoma—a common or distinct background? loss of heterozygosity in comprehensive microarray study. Cancers, 15:638, Jan 2023. URL: https://doi.org/10.3390/cancers15030638, doi:10.3390/cancers15030638. This article has 11 citations.

7. (capdevila2022moleculardiagnosisand pages 1-2): Jaume Capdevila, Ahmad Awada, Dagmar Führer-Sakel, Sophie Leboulleux, and Patrick Pauwels. Molecular diagnosis and targeted treatment of advanced follicular cell-derived thyroid cancer in the precision medicine era. Cancer Treatment Reviews, 106:102380, May 2022. URL: https://doi.org/10.1016/j.ctrv.2022.102380, doi:10.1016/j.ctrv.2022.102380. This article has 73 citations and is from a peer-reviewed journal.

8. (prete2020updateonfundamental pages 1-3): Alessandro Prete, Patricia Borges de Souza, Simona Censi, Marina Muzza, Nicole Nucci, and Marialuisa Sponziello. Update on fundamental mechanisms of thyroid cancer. Frontiers in Endocrinology, Mar 2020. URL: https://doi.org/10.3389/fendo.2020.00102, doi:10.3389/fendo.2020.00102. This article has 589 citations.

9. (calafato2025somaticgeneticalterations pages 1-2): Giulia Calafato, Floriana Jessica Di Paola, Antonio De Leo, Thais Maloberti, Sara Coluccelli, Laura Poppi, Andrea Repaci, Erica Solaroli, Stefania Damiani, Stefano Chillotti, Federico Chiarucci, Kerry Jane Rhoden, Dario de Biase, and Giovanni Tallini. Somatic genetic alterations in the development and progression in thyroid tumors of follicular cells. European Thyroid Journal, Oct 2025. URL: https://doi.org/10.1530/etj-25-0104, doi:10.1530/etj-25-0104. This article has 7 citations and is from a peer-reviewed journal.

10. (crncic2020riskfactorsfor pages 1-2): Tatjana Bogović Crnčić, Maja Ilić Tomaš, N. Girotto, and S. Grbac Ivanković. Risk factors for thyroid cancer: what do we know so far? Acta Clinica Croatica, 59:66-72, Jun 2020. URL: https://doi.org/10.20471/acc.2020.59.s1.08, doi:10.20471/acc.2020.59.s1.08. This article has 176 citations.

11. (hossain2020networkbasedgeneticprofiling pages 1-3): Md. Ali Hossain, Tania Akter Asa, Md. Mijanur Rahman, Shahadat Uddin, Ahmed A. Moustafa, Julian M. W. Quinn, and Mohammad Ali Moni. Network-based genetic profiling reveals cellular pathway differences between follicular thyroid carcinoma and follicular thyroid adenoma. International Journal of Environmental Research and Public Health, 17:1373, Feb 2020. URL: https://doi.org/10.3390/ijerph17041373, doi:10.3390/ijerph17041373. This article has 30 citations.

12. (kruger2022thyroidcarcinomaa pages 1-2): Eva Kruger, Eman A. Toraih, Mohammad H. Hussein, Shaimaa A. Shehata, Amani Waheed, Manal S. Fawzy, and Emad Kandil. Thyroid carcinoma: a review for 25 years of environmental risk factors studies. Cancers, 14:6172, Dec 2022. URL: https://doi.org/10.3390/cancers14246172, doi:10.3390/cancers14246172. This article has 51 citations.

13. (vico2025systemictherapeuticoptions pages 1-2): Tamara Díaz Vico, Brezo Martínez-Amores Martínez, Luka Mihic Góngora, Paula Jiménez-Fonseca, Paloma Peinado Martín, Irene Grao Torrente, Alejandro García Muñoz-Nájar, and Manuel Durán-Poveda. Systemic therapeutic options in radioiodine-refractory differentiated thyroid cancer: current indications and optimal timing. Cancers, 17:1800, May 2025. URL: https://doi.org/10.3390/cancers17111800, doi:10.3390/cancers17111800. This article has 9 citations.

14. (hu2021thyroidcarcinomaphenotypic pages 1-2): Jinwei Hu, Isabella J. Yuan, Saied Mirshahidi, Alfred Simental, Steve C. Lee, and Xiangpeng Yuan. Thyroid carcinoma: phenotypic features, underlying biology and potential relevance for targeting therapy. International Journal of Molecular Sciences, 22:1950, Feb 2021. URL: https://doi.org/10.3390/ijms22041950, doi:10.3390/ijms22041950. This article has 141 citations.

15. (capdevila2022moleculardiagnosisand pages 3-4): Jaume Capdevila, Ahmad Awada, Dagmar Führer-Sakel, Sophie Leboulleux, and Patrick Pauwels. Molecular diagnosis and targeted treatment of advanced follicular cell-derived thyroid cancer in the precision medicine era. Cancer Treatment Reviews, 106:102380, May 2022. URL: https://doi.org/10.1016/j.ctrv.2022.102380, doi:10.1016/j.ctrv.2022.102380. This article has 73 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Thyroid_Follicular_Carcinoma-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Thyroid_Follicular_Carcinoma-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Thyroid_Follicular_Carcinoma-deep-research-falcon_artifacts/artifact-02.md)