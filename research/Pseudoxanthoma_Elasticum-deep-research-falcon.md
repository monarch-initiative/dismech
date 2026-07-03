---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T22:14:57.791150'
end_time: '2026-06-18T22:30:22.311763'
duration_seconds: 924.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pseudoxanthoma Elasticum
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 4
artifact_sources:
  edison_answer_artifacts: 4
artifacts:
- filename: artifact-00.md
  path: Pseudoxanthoma_Elasticum-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Pseudoxanthoma_Elasticum-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Pseudoxanthoma_Elasticum-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
- filename: artifact-03.md
  path: Pseudoxanthoma_Elasticum-deep-research-falcon_artifacts/artifact-03.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-03
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pseudoxanthoma Elasticum
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Pseudoxanthoma Elasticum** covering all of the
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
- **Disease Name:** Pseudoxanthoma Elasticum
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Pseudoxanthoma Elasticum** covering all of the
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


# Comprehensive Research Report: Pseudoxanthoma Elasticum (PXE)

## 1. Disease Information

### Disease Definition and Overview

Pseudoxanthoma elasticum (PXE; OMIM #264800) is a rare, genetic, autosomal recessive metabolic disease characterized by progressive ectopic mineralization affecting elastic tissues in the skin, eyes, and cardiovascular system (stumpf2021therapyofpseudoxanthoma pages 1-2, germain2017pseudoxanthomaelasticum pages 1-2). The disease manifests with deposition of calcium hydroxyapatite crystals that accumulate in the mid-dermal elastic fibers, Bruch's membrane of the eye, and arterial blood vessels (luo2020therapeuticsdevelopmentfor pages 1-3, kauffenstein2024thepurinergicnature pages 1-2). PXE is the prototype of heritable ectopic mineralization disorders, distinguished by its multisystem clinical manifestations that usually appear around the second decade of life (luo2020therapeuticsdevelopmentfor pages 1-3, germain2017pseudoxanthomaelasticum pages 1-2).

### Key Identifiers

- **OMIM**: #264800 (stumpf2021therapyofpseudoxanthoma pages 1-2, germain2017pseudoxanthomaelasticum pages 1-2)
- **Orphanet**: ORPHA #758 (germain2017pseudoxanthomaelasticum pages 1-2)
- **ICD-10**: Q82.8 (germain2017pseudoxanthomaelasticum pages 1-2)
- **Alternative Names**: Grönblad-Strandberg syndrome (germain2017pseudoxanthomaelasticum pages 1-2, marconi2015pseudoxanthomaelasticumand pages 1-2)
- **MONDO ID**: Not explicitly provided in retrieved literature

### Data Source Classification

Information is derived from aggregated disease-level resources including peer-reviewed clinical studies, systematic reviews, case series, and controlled clinical trials in PXE patient cohorts, complemented by animal model research and cellular studies (germain2017pseudoxanthomaelasticum pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2, kranenburg2018etidronateforprevention pages 1-2).

---

## 2. Etiology

### Disease Causal Factors

PXE is a genetic disorder caused by mutations in the **ABCC6 gene** (ATP-binding cassette subfamily C member 6), discovered in 2000 (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 4-5). The ABCC6 gene is located on chromosome 16p13.11 and consists of 31 exons encoding a 1503-amino acid protein (molecular weight approximately 165–170 kDa) (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 4-5). ABCC6 functions as an ATP-dependent transmembrane efflux transporter expressed predominantly in the liver and kidneys (stumpf2021therapyofpseudoxanthoma pages 1-2, kauffenstein2024thepurinergicnature pages 1-2, verschuere2020frommembraneto pages 1-5). Although the precise substrate(s) of ABCC6 remain uncertain, it facilitates the cellular efflux of ATP, which is sequentially hydrolyzed by ectonucleotidases ENPP1 and CD73 into pyrophosphate (PPi) and adenosine, both potent endogenous inhibitors of calcification (kauffenstein2024thepurinergicnature pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2).

The unifying pathomechanistic feature of PXE is **reduced plasma levels of inorganic pyrophosphate (PPi)**, a powerful anti-mineralization factor. ABCC6 deficiency leads to approximately 60% reduction in plasma PPi levels in both humans and mice (leftheriotis2022relationshipsbetweenplasma pages 1-2, zedde2025abcc6involvementin pages 1-2, verschuere2020frommembraneto pages 8-10). This PPi deficiency results in an imbalance of the physiological Pi/PPi ratio in connective tissues, promoting ectopic calcification (kauffenstein2024thepurinergicnature pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2).

### Risk Factors

**Genetic Risk Factors:**
- Biallelic pathogenic variants in **ABCC6** are the primary genetic cause. Over 300 distinct loss-of-function mutations have been reported, with recurrent variants **p.R1141X** and **g.del23-29** accounting for up to ~45% of all pathogenic mutations (li2019pseudoxanthomaelasticumas pages 1-6, marconi2015pseudoxanthomaelasticumand pages 1-2, plumers2023matrixmetalloproteinasescontribute pages 1-2).
- Variant types include missense, nonsense, frameshift, splice-site mutations, and structural rearrangements (deletions, duplications) (marconi2015pseudoxanthomaelasticumand pages 1-2, verschuere2020frommembraneto pages 8-10, germain2017pseudoxanthomaelasticum pages 4-5).
- Rare modifier variants in genes related to calcium homeostasis, vascular disease, apoptosis, and purinergic signaling (e.g., NLRP1, SELE, TRPV1, CSF1R) may alter cardiovascular disease severity (vilder2021raremodifiervariants pages 1-2).
- Heterozygous carriers of ABCC6 mutations may have an increased risk of cardiovascular calcification and premature coronary artery disease, although classic PXE typically requires biallelic pathogenic variants (germain2017pseudoxanthomaelasticum pages 2-4, germain2017pseudoxanthomaelasticum pages 4-5).

**Environmental Risk Factors:**
- Age is a major determinant of disease severity and calcification burden; time (i.e., age) appears to be the principal driver of progressive arterial calcification independent of plasma PPi levels (leftheriotis2022relationshipsbetweenplasma pages 1-2).
- Traditional cardiovascular risk factors such as smoking, dyslipidemia, and hypertension may additively worsen vascular complications (stumpf2021therapyofpseudoxanthoma pages 1-2, zedde2025abcc6involvementin pages 1-2).

### Protective Factors

Specific genetic protective factors have not been definitively established in retrieved literature. However, higher serum magnesium levels were associated with higher serum calcification propensity T50 (indicative of lower calcification risk), suggesting magnesium may have a protective role (nollet2022serumcalcificationpropensity pages 1-2). Lifestyle modifications reducing cardiovascular risk factors are recommended as supportive measures but do not reverse underlying mineralization (germain2017pseudoxanthomaelasticum pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2).

### Gene-Environment Interactions

PXE pathophysiology reflects a complex interplay between genetic ABCC6 deficiency and environmental/age-related factors. While ABCC6 mutations cause systemic PPi deficiency, environmental contributors such as dietary phosphate, oxidative stress, and aging accelerate or modulate the mineralization process (germain2017pseudoxanthomaelasticum pages 4-5). Specific gene-environment interaction data are limited in retrieved studies.

---

## 3. Phenotypes

| Organ System | Specific Manifestation | Age of Onset | Frequency in PXE Patients | Severity | Progression Pattern | HPO Terms (suggested) | Quality of Life Impact |
|---|---|---|---|---|---|---|---|
| Integumentary / Skin | Small yellow papules on neck and flexural areas | Typically childhood to adolescence; often first clinical sign (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4) | Common / usually initial presenting sign; “almost always” first clinical sign in review literature (germain2017pseudoxanthomaelasticum pages 1-2) | Usually mild medically, cosmetically significant | Progressive: isolated papules coalesce into plaques over time (germain2017pseudoxanthomaelasticum pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3, germain2017pseudoxanthomaelasticum pages 2-4) | HP:0000987 Skin papule; HP:0010783 Abnormality of the skin of the neck; HP:0000978 Bruising susceptibility not applicable; HP:0001065 Generalized lax skin not initial | Cosmetic burden; may cause distress and social/self-image impact, but usually less disabling than ocular/vascular disease (luo2020therapeuticsdevelopmentfor pages 1-3, marconi2015pseudoxanthomaelasticumand pages 1-2) |
| Integumentary / Skin | Lax, wrinkled, redundant skin in flexural areas | Usually follows papules, often from adolescence/early adulthood onward (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4) | Common in established disease; qualitative frequency high in clinical descriptions (germain2017pseudoxanthomaelasticum pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3) | Mild to moderate | Progressive chronic change with loss of recoil and leathery/sagging skin (luo2020therapeuticsdevelopmentfor pages 1-3, germain2017pseudoxanthomaelasticum pages 2-4) | HP:0000973 Wrinkled skin; HP:0001007 Redundant skin; HP:0001513 Cutis laxa-like skin changes | Mainly cosmetic and psychosocial impact; may affect body image and clothing comfort (luo2020therapeuticsdevelopmentfor pages 1-3, marconi2015pseudoxanthomaelasticumand pages 1-2) |
| Ophthalmologic | Peau d’orange / early Bruch’s membrane change | Often precedes angioid streaks; can occur in young patients | Observed in 96% of patients with skin signs in one study cited by review (germain2017pseudoxanthomaelasticum pages 2-4) | Usually mild initially | Early marker that may precede more vision-threatening retinal disease (germain2017pseudoxanthomaelasticum pages 2-4, risseeuw2020areflectivitymeasure pages 1-2) | HP:0030937 Abnormality of Bruch membrane; HP:0100012 Retinal abnormality | Usually limited direct impact initially, but clinically important as precursor of later visual morbidity (germain2017pseudoxanthomaelasticum pages 2-4, risseeuw2020areflectivitymeasure pages 1-2) |
| Ophthalmologic | Angioid streaks | Usually years after skin changes; often early adult life (germain2017pseudoxanthomaelasticum pages 2-4) | Characteristic ocular feature; common in affected adults (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4) | Moderate to severe because of risk of CNV and vision loss | Progressive; may become symptomatic when approaching fovea (germain2017pseudoxanthomaelasticum pages 2-4) | HP:0007932 Angioid streaks of the fundus | Major threat to vision; central visual tasks and reading/driving may become impaired (germain2017pseudoxanthomaelasticum pages 2-4) |
| Ophthalmologic | Choroidal neovascularization (CNV) | Usually after angioid streaks, often adulthood | Common complication of calcified Bruch’s membrane in progressing disease; exact percentage not given in retrieved sources (germain2017pseudoxanthomaelasticum pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3) | Severe | Progressive/episodic with hemorrhage and scarring if untreated (luo2020therapeuticsdevelopmentfor pages 1-3, germain2017pseudoxanthomaelasticum pages 2-4) | HP:0007754 Choroidal neovascularization | High impact; anti-VEGF treatment burden and risk of central vision loss reduce daily functioning (germain2017pseudoxanthomaelasticum pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3) |
| Ophthalmologic | Progressive loss of visual acuity / central vision loss / blindness in late-stage disease | Often adulthood, with severe impairment potentially by 40s if untreated (luo2020therapeuticsdevelopmentfor pages 1-3) | Important late complication; exact prevalence not provided in retrieved contexts (germain2017pseudoxanthomaelasticum pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3) | Severe | Progressive due to hemorrhage, scarring, and macular atrophy (luo2020therapeuticsdevelopmentfor pages 1-3, risseeuw2020areflectivitymeasure pages 1-2) | HP:0000505 Visual impairment; HP:0000529 Progressive visual loss; HP:0000618 Blindness | Very high impact; vision-related quality of life is markedly reduced, and visual impairment was associated with major degradation in vision-related QoL (germain2017pseudoxanthomaelasticum pages 2-4) |
| Cardiovascular / Vascular | Arterial calcification (including lower-limb and coronary calcification) | Usually becomes apparent years after skin/ocular changes; increases with age (leftheriotis2022relationshipsbetweenplasma pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4) | Common hallmark in adult PXE; severity strongly age-dependent (leftheriotis2022relationshipsbetweenplasma pages 1-2, kranenburg2018etidronateforprevention pages 1-2) | Moderate to severe | Progressive, chronic, age-related accumulation; major determinant appears to be time/age (leftheriotis2022relationshipsbetweenplasma pages 1-2) | HP:0004958 Arterial calcification; HP:0005117 Vascular calcification | Contributes to vascular morbidity, reduced exercise capacity, and anxiety about cardiovascular events (stumpf2021therapyofpseudoxanthoma pages 1-2, leftheriotis2022relationshipsbetweenplasma pages 1-2) |
| Cardiovascular / Vascular | Peripheral artery disease (PAD) | Typically adulthood after earlier skin/eye findings (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4) | Major cause of morbidity; common qualitative feature (leftheriotis2022relationshipsbetweenplasma pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4) | Moderate to severe | Progressive chronic vascular disease; may require intervention in advanced stages (vilder2021raremodifiervariants pages 1-2) | HP:0004939 Peripheral arterial insufficiency | Limits walking and physical activity; contributes to reduced participation in social/occupational activities (stumpf2021therapyofpseudoxanthoma pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4) |
| Cardiovascular / Vascular | Intermittent claudication | Usually adulthood | Cardinal symptom of lower-extremity arterial disease; common qualitative feature (luo2020therapeuticsdevelopmentfor pages 1-3, germain2017pseudoxanthomaelasticum pages 2-4) | Moderate | Progressive with worsening PAD; exertional symptom burden (luo2020therapeuticsdevelopmentfor pages 1-3, germain2017pseudoxanthomaelasticum pages 2-4) | HP:0002579 Intermittent claudication | Substantial mobility limitation and exercise intolerance; important contributor to reduced QoL (stumpf2021therapyofpseudoxanthoma pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4) |
| Cardiovascular / Vascular | Hypertension | Usually adulthood | Reported but less consistently emphasized than calcification/PAD; exact percentage not provided (luo2020therapeuticsdevelopmentfor pages 1-3, plumers2023matrixmetalloproteinasescontribute pages 1-2) | Mild to moderate, can contribute to vascular risk | Chronic; may coexist with arterial disease (plumers2023matrixmetalloproteinasescontribute pages 1-2) | HP:0000822 Hypertension | Adds long-term cardiovascular risk and treatment burden (luo2020therapeuticsdevelopmentfor pages 1-3, plumers2023matrixmetalloproteinasescontribute pages 1-2) |
| Neurologic / Cerebrovascular | Ischemic stroke risk / cerebrovascular disease | Usually older adults; risk appears elevated relative to general population (germain2017pseudoxanthomaelasticum pages 2-4, zedde2025abcc6involvementin pages 1-2) | 15% in one cohort of 38 PXE patients; 7% in another cohort of 100, relative risk 3.6 vs general population (germain2017pseudoxanthomaelasticum pages 2-4) | Severe | Episodic vascular complication on background of progressive vasculopathy (germain2017pseudoxanthomaelasticum pages 2-4, zedde2025abcc6involvementin pages 1-2) | HP:0002140 Ischemic stroke; HP:0001297 Cerebrovascular accident | Potentially devastating disability; major anxiety source and contributor to long-term morbidity (germain2017pseudoxanthomaelasticum pages 2-4, zedde2025abcc6involvementin pages 1-2) |
| Gastrointestinal | Gastrointestinal bleeding (especially stomach) | Usually adulthood | Around 15% of PXE patients vs ~0.1% in general population, according to review summary (germain2017pseudoxanthomaelasticum pages 2-4) | Moderate to severe; potentially acute | Episodic complication | HP:0002239 Gastrointestinal hemorrhage; HP:0002573 Hematemesis if present | Acute morbidity, hospitalization risk, and anxiety regarding bleeding events (germain2017pseudoxanthomaelasticum pages 2-4) |


*Table: This table summarizes the major clinical manifestations of pseudoxanthoma elasticum across skin, ocular, vascular, neurologic, and gastrointestinal systems. It highlights onset, frequency, progression, suggested HPO annotations, and likely quality-of-life effects for knowledge base curation.*

The table above summarizes the major clinical manifestations across organ systems. Key phenotypes include:

### Cutaneous Manifestations
- **Small yellow papules** on the neck and flexural areas (axillae, antecubital fossae, inguinal regions), typically the first clinical sign appearing in childhood or adolescence (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4).
- **Lax, wrinkled, redundant skin** with loss of elasticity, giving a cobblestone or peau d'orange appearance (germain2017pseudoxanthomaelasticum pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3, germain2017pseudoxanthomaelasticum pages 2-4).
- **HPO Terms**: HP:0000987 (Skin papule), HP:0000973 (Wrinkled skin), HP:0001007 (Redundant skin).

### Ophthalmological Manifestations
- **Peau d'orange** retinal changes often precede angioid streaks; observed in 96% of patients with skin signs (germain2017pseudoxanthomaelasticum pages 2-4).
- **Angioid streaks** reflecting breaks in calcified Bruch's membrane, characteristic of PXE (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4).
- **Choroidal neovascularization (CNV)** leading to hemorrhage, scarring, and progressive central vision loss if untreated (luo2020therapeuticsdevelopmentfor pages 1-3, germain2017pseudoxanthomaelasticum pages 2-4).
- **Visual impairment and blindness** in late-stage disease, typically by the 40s without treatment (luo2020therapeuticsdevelopmentfor pages 1-3).
- **HPO Terms**: HP:0007932 (Angioid streaks of the fundus), HP:0007754 (Choroidal neovascularization), HP:0000505 (Visual impairment), HP:0000529 (Progressive visual loss).

### Cardiovascular and Vascular Manifestations
- **Arterial calcification** affecting medium and small arteries, strongly age-dependent (leftheriotis2022relationshipsbetweenplasma pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4, kranenburg2018etidronateforprevention pages 1-2).
- **Peripheral artery disease (PAD)** with intermittent claudication as the cardinal symptom (luo2020therapeuticsdevelopmentfor pages 1-3, germain2017pseudoxanthomaelasticum pages 2-4).
- **Hypertension** (luo2020therapeuticsdevelopmentfor pages 1-3, plumers2023matrixmetalloproteinasescontribute pages 1-2).
- **Ischemic stroke risk** elevated relative to general population; 15% in one cohort of 38 patients, 7% in another cohort of 100 (relative risk 3.6 vs general population) (germain2017pseudoxanthomaelasticum pages 2-4).
- **HPO Terms**: HP:0004958 (Arterial calcification), HP:0004939 (Peripheral arterial insufficiency), HP:0002579 (Intermittent claudication), HP:0002140 (Ischemic stroke), HP:0000822 (Hypertension).

### Gastrointestinal Manifestations
- **Gastrointestinal bleeding**, especially from the stomach, occurs in approximately 15% of PXE patients versus ~0.1% in the general population (germain2017pseudoxanthomaelasticum pages 2-4).
- **HPO Terms**: HP:0002239 (Gastrointestinal hemorrhage).

### Quality of Life Impact
Visual impairment is associated with major degradation in vision-related quality of life measured by the Impact of Vision Impairment questionnaire (germain2017pseudoxanthomaelasticum pages 2-4). Cardiovascular complications have relatively less measured impact on health-related QoL according to SF-36 surveys, though intermittent claudication significantly limits mobility and social/occupational participation (germain2017pseudoxanthomaelasticum pages 2-4, stumpf2021therapyofpseudoxanthoma pages 1-2).

---

## 4. Genetic/Molecular Information

| Gene Name | Gene Symbol | Chromosome Location | Protein Name | Protein Size | Protein Function | Common Pathogenic Variants | Variant Types | Mode of Inheritance | Penetrance | Key Molecular Pathways |
|---|---|---|---|---|---|---|---|---|---|---|
| ATP-binding cassette subfamily C member 6 | **ABCC6** | **16p13.11 / 16p13.1** | ABCC6 / MRP6 | **1503 aa**, ~**165–170 kDa** glycoprotein | ATP-dependent transmembrane efflux transporter, expressed predominantly in **liver** and **kidney**; promotes extracellular **ATP efflux**, which is converted by ENPP1 and CD73 to **PPi** and adenosine; major upstream regulator of anti-mineralization homeostasis (verschuere2020frommembraneto pages 1-5, germain2017pseudoxanthomaelasticum pages 1-2, verschuere2020frommembraneto pages 8-10, kauffenstein2024thepurinergicnature pages 1-2) | Recurrent loss-of-function variants include **p.R1141X** and **del23-29 / g.del23-29**, together accounting for up to ~45% of pathogenic alleles in some cohorts; >300 variants reported overall, now ~400 in newer summaries (li2019pseudoxanthomaelasticumas pages 1-6, marconi2015pseudoxanthomaelasticumand pages 1-2, plumers2023matrixmetalloproteinasescontribute pages 1-2) | Missense, nonsense, splice-site, small insertions/deletions, multiexon deletions/structural variants; predominantly **loss-of-function** (marconi2015pseudoxanthomaelasticumand pages 1-2, germain2017pseudoxanthomaelasticum pages 4-5, verschuere2020frommembraneto pages 8-10) | **Autosomal recessive** PXE; ABCC6 variants can also cause some **GACI type 2** cases (germain2017pseudoxanthomaelasticum pages 1-2, jacobs2022inz‐701arecombinant pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2) | Generally high for **biallelic pathogenic variants** with **age-dependent** and **variable expressivity**; heterozygotes usually unaffected but may show subclinical or partial manifestations and elevated vascular calcification risk in some reports (germain2017pseudoxanthomaelasticum pages 4-5, germain2017pseudoxanthomaelasticum pages 2-4) | **ABCC6 → extracellular ATP efflux → ENPP1 → PPi + AMP → CD73/NT5E → adenosine; TNAP opposes PPi by hydrolysis; purinergic signaling / Pi:PPi balance / ectopic calcification inhibition** (kauffenstein2024thepurinergicnature pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2, verschuere2020frommembraneto pages 8-10) |
| Ectonucleotide pyrophosphatase/phosphodiesterase 1 | **ENPP1** | **Not specified in retrieved PXE contexts** | ENPP1 / NPP1 | **Not specified in retrieved PXE contexts** | Principal ectoenzyme generating extracellular **PPi** from ATP; core anti-calcification enzyme downstream of ABCC6. ENPP1 deficiency causes classic **GACI**, and some ENPP1-mutated patients can present PXE-like features or overlap phenotypes (jacobs2022inz‐701arecombinant pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2, kauffenstein2024thepurinergicnature pages 1-2) | Specific recurrent ENPP1 variants were **not detailed** in retrieved PXE contexts; disease-causing ENPP1 variants underlie most classic GACI and can overlap phenotypically with PXE (jacobs2022inz‐701arecombinant pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2) | Loss-of-function variants, including missense, nonsense, splice, and other disruptive alleles causing reduced/absent ENPP1 activity; exact spectrum not detailed in retrieved contexts (jacobs2022inz‐701arecombinant pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2) | **Autosomal recessive** for GACI; overlap with PXE spectrum recognized (luo2020therapeuticsdevelopmentfor pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2) | High for biallelic ENPP1 deficiency, but phenotype may range from severe infantile vascular calcification to PXE-like overlap; detailed penetrance not specified in retrieved contexts (luo2020therapeuticsdevelopmentfor pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2) | **Extracellular ATP hydrolysis to AMP + PPi**; central PPi-generating step in the **ABCC6–ENPP1–CD73–TNAP** pathway regulating ectopic mineralization (kauffenstein2024thepurinergicnature pages 1-2, jacobs2022inz‐701arecombinant pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2) |
| 5'-nucleotidase ecto / CD73 | **NT5E** | **Not specified in retrieved PXE contexts** | CD73 | **Not specified in retrieved PXE contexts** | Converts **AMP to adenosine** in the extracellular space; adenosine indirectly inhibits calcification, in part by suppressing **TNAP**, thereby preserving PPi-mediated anti-calcification effects (kauffenstein2024thepurinergicnature pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2) | Specific recurrent NT5E pathogenic variants were **not detailed** in retrieved PXE contexts; NT5E mutations cause **CALJA/ACDC**, an overlapping ectopic calcification disorder (kauffenstein2024thepurinergicnature pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2) | Loss-of-function variants causing reduced/absent CD73 activity; exact variant spectrum not detailed in retrieved contexts (kauffenstein2024thepurinergicnature pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2) | **Autosomal recessive** for CALJA/ACDC; part of the PXE–GACI–CALJA disease continuum (kauffenstein2024thepurinergicnature pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2) | Detailed penetrance not specified in retrieved PXE contexts; phenotype is generally adult/late-onset in CALJA compared with PXE and GACI (luo2020therapeuticsdevelopmentfor pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2) | **AMP → adenosine**, with downstream reduction of **TNAP** activity and support of anti-mineralization purinergic signaling; final shared branch of the **ABCC6–ENPP1–CD73–TNAP** axis (kauffenstein2024thepurinergicnature pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2) |


*Table: This table summarizes the core genes and pathway biology relevant to pseudoxanthoma elasticum and related PPi-deficiency calcification disorders. It highlights ABCC6 as the primary PXE gene and places ENPP1 and NT5E within the shared extracellular ATP-PPi-adenosine anti-mineralization pathway.*

### Causal Genes and Pathogenic Variants

The primary causal gene is **ABCC6** (OMIM *603234), located on chromosome 16p13.11 (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 4-5). The gene encodes a 1503-amino acid transmembrane protein predominantly expressed in hepatocytes and renal tissues (verschuere2020frommembraneto pages 1-5, verschuere2020frommembraneto pages 8-10). More than 300–400 distinct pathogenic variants have been identified, including:

- **p.R1141X** (recurrent nonsense mutation)
- **g.del23-29** (multiexon deletion)
- Missense, frameshift, splice-site, and structural variants (li2019pseudoxanthomaelasticumas pages 1-6, marconi2015pseudoxanthomaelasticumand pages 1-2, plumers2023matrixmetalloproteinasescontribute pages 1-2, verschuere2020frommembraneto pages 8-10).

**Variant Classification**: Most ABCC6 variants are classified as pathogenic or likely pathogenic loss-of-function alleles per ACMG/AMP guidelines. Functional studies in HEK293 cells and patient fibroblasts support loss-of-function consequences (verschuere2020frommembraneto pages 8-10, germain2017pseudoxanthomaelasticum pages 4-5).

**Allele Frequency**: PXE is rare, with estimated carrier frequency up to 1 in 80 for heterozygous ABCC6 mutations in the general population (germain2017pseudoxanthomaelasticum pages 2-4).

**Germline vs Somatic**: All reported PXE-causing ABCC6 variants are germline (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 4-5).

### Related Genes

**ENPP1** (ectonucleotide pyrophosphatase/phosphodiesterase 1): Mutations cause classic GACI (Generalized Arterial Calcification of Infancy), and some ENPP1-deficient patients present PXE-like features (luo2020therapeuticsdevelopmentfor pages 1-3, jacobs2022inz‐701arecombinant pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2).

**NT5E** (CD73): Mutations cause CALJA/ACDC (Calcification of Joints and Arteries / Arterial Calcification Due to CD73 Deficiency), part of the ectopic mineralization disease continuum (kauffenstein2024thepurinergicnature pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2).

### Modifier Genes

Rare modifier variants in genes involved in calcium homeostasis (e.g., TRPV1), vascular disease (e.g., SELE, CSF1R), and apoptosis (e.g., NLRP1) may collectively influence cardiovascular phenotype severity through IL-1B signaling pathways (vilder2021raremodifiervariants pages 1-2).

### Epigenetic Information

Limited specific epigenetic data are available in retrieved PXE literature. Oxidative stress has been shown to inhibit ABCC6 gene expression in human cell lines, suggesting possible environmental or epigenetic modulation (germain2017pseudoxanthomaelasticum pages 4-5).

### Chromosomal Abnormalities

The ABCC6 locus on 16p13.11 is prone to genomic rearrangements due to abundance of repetitive elements and flanking pseudogenes (ABCC6-Ψ1 and ABCC6-Ψ2) with ~99% sequence identity to the functional gene (verschuere2020frommembraneto pages 8-10).

---

## 5. Environmental Information

### Environmental Factors

PXE is primarily a genetic disorder. However, oxidative stress from iron overload (as seen in β-thalassemia) can induce PXE-like syndrome, suggesting environmental oxidative damage may interact with genetic susceptibility (germain2017pseudoxanthomaelasticum pages 4-5).

### Lifestyle Factors

Smoking, diet, and traditional cardiovascular risk factors (dyslipidemia, hypertension) may additively worsen vascular complications, although they do not directly cause PXE (stumpf2021therapyofpseudoxanthoma pages 1-2, zedde2025abcc6involvementin pages 1-2).

### Infectious Agents

Not applicable; PXE is not caused by infectious agents.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

The central pathophysiological pathway in PXE is the **ABCC6 → extracellular ATP → ENPP1 → PPi + AMP → CD73 → adenosine** purinergic cascade (kauffenstein2024thepurinergicnature pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2, verschuere2020frommembraneto pages 8-10):

1. **ABCC6** facilitates ATP efflux from hepatocytes into the extracellular space (kauffenstein2024thepurinergicnature pages 1-2, verschuere2020frommembraneto pages 8-10).
2. **ENPP1** hydrolyzes extracellular ATP to AMP and PPi (kauffenstein2024thepurinergicnature pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2).
3. **CD73/NT5E** converts AMP to adenosine (kauffenstein2024thepurinergicnature pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2).
4. **PPi** directly inhibits hydroxyapatite crystal nucleation and growth (shimada2021abcc6pyrophosphateand pages 1-2).
5. **Adenosine** indirectly inhibits calcification by suppressing tissue non-specific alkaline phosphatase (TNAP), which degrades PPi (kauffenstein2024thepurinergicnature pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2).

ABCC6 deficiency reduces plasma PPi by approximately 60% in humans and mice, lowering the Pi/PPi ratio and permitting ectopic mineralization (leftheriotis2022relationshipsbetweenplasma pages 1-2, zedde2025abcc6involvementin pages 1-2, verschuere2020frommembraneto pages 8-10).

### Cellular Processes

- **Elastic fiber fragmentation and calcification**: Mid-dermal elastic fibers become short, fragmented, clumped, and progressively calcified (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4).
- **Extracellular matrix (ECM) remodeling**: PXE fibroblasts exhibit dysregulated ECM remodeling with elevated matrix metalloproteinases (MMPs), particularly MMP2, MMP9, and a cluster of MMPs on chromosome 11q21-23 (plumers2023matrixmetalloproteinasescontribute pages 1-2).
- **Oxidative stress**: PXE patients show biochemical signs of oxidative stress, and oxidative damage may contribute to elastic fiber degeneration (germain2017pseudoxanthomaelasticum pages 4-5).
- **Cellular senescence**: PXE fibroblasts display senescence-related features and altered lipid metabolism (plumers2023matrixmetalloproteinasescontribute pages 1-2).

**GO Terms**: GO:0030574 (collagen catabolic process), GO:0031012 (extracellular matrix), GO:0006874 (cellular calcium ion homeostasis), GO:0001503 (ossification).

### Protein Dysfunction

ABCC6 loss-of-function mutations result in absent or severely reduced ATP efflux activity, impairing the upstream supply of substrate for PPi generation (kauffenstein2024thepurinergicnature pages 1-2, verschuere2020frommembraneto pages 8-10). The exact transported substrate(s) remain uncertain, though ATP is strongly implicated (verschuere2020frommembraneto pages 8-10, germain2017pseudoxanthomaelasticum pages 4-5).

### Metabolic Changes

- **Reduced plasma PPi** (approximately 40–60% of normal levels) (leftheriotis2022relationshipsbetweenplasma pages 1-2, verschuere2020frommembraneto pages 8-10).
- **Altered lipid metabolism**: Metabolomic studies in ABCC6-deficient models show changes in fatty acids, glycerophospholipids, and cholesterol metabolism (verschuere2020frommembraneto pages 8-10).
- **Dysregulated nucleotide metabolism**: Significant changes in nucleoside, nucleotide mono/di/triphosphate, and nucleotide sugar levels in ABCC6-transfected cells (verschuere2020frommembraneto pages 8-10).

### Tissue Damage Mechanisms

- **Dystrophic calcification**: Abnormal accumulation of calcium/phosphate complexes in elastic tissues with normal serum calcium and phosphate levels (germain2017pseudoxanthomaelasticum pages 1-2, li2019pseudoxanthomaelasticumas pages 1-6).
- **Elastic fiber degradation**: MMPs make elastic fibers accessible to controlled, osteopontin-dependent calcium deposition (plumers2023matrixmetalloproteinasescontribute pages 1-2).
- **Vascular stiffness and occlusion**: Arterial medial calcification leads to increased pulse wave velocity, peripheral artery disease, and stroke risk (stumpf2021therapyofpseudoxanthoma pages 1-2, zedde2025abcc6involvementin pages 1-2).

### Biochemical Abnormalities

- **PPi deficiency** is the central biochemical defect (shimada2021abcc6pyrophosphateand pages 1-2).
- **Reduced ENPP1 expression** in peripheral tissues (dermal fibroblasts, liver) further compromises PPi production (plumers2023matrixmetalloproteinasescontribute pages 1-2).
- **Elevated osteopontin (OPN/SPP1)**: A mineralization-associated protein that may inhibit apatite crystal growth and colocalizes with calcification deposits (plumers2023matrixmetalloproteinasescontribute pages 1-2).

### Molecular Profiling

**Transcriptomics**: RNA sequencing of PXE fibroblasts and Abcc6-/- mouse tissue reveals overexpression of MMPs (MMP2, MMP9, and an 11q21-23 cluster) and dysregulation of calcification-related genes (plumers2023matrixmetalloproteinasescontribute pages 1-2).

**Proteomics**: Secretome studies show that fibroblasts from calcified vs non-calcified skin areas differentially express pro- and anti-calcifying proteoglycans, glycoproteins, and elastic fiber-associated proteins (nollet2022serumcalcificationpropensity pages 1-2).

**Metabolomics**: Untargeted metabolomics in ABCC6-transfected cells and patient samples document alterations in purinergic metabolites, lipids, and mineralization-related small molecules (verschuere2020frommembraneto pages 8-10).

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary Organs**:
- **Skin**: Mid-dermal elastic fibers in neck, flexural areas (axillae, inguinal, popliteal regions) (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4).
- **Eyes**: Bruch's membrane in the retina (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4).
- **Cardiovascular system**: Small and medium-sized arteries, particularly lower extremity vessels, coronary arteries, and cerebral vasculature (germain2017pseudoxanthomaelasticum pages 2-4, zedde2025abcc6involvementin pages 1-2).

**Secondary Organs**:
- **Kidneys, breasts, pancreas, testicles, liver, spleen**: Calcification has been observed variably; clinical impact generally minor except kidneys (germain2017pseudoxanthomaelasticum pages 2-4).
- **Gastrointestinal tract**: Vascular involvement leading to bleeding (germain2017pseudoxanthomaelasticum pages 2-4).

**Body Systems**: Integumentary, ocular, cardiovascular, nervous (secondary via cerebrovascular disease), gastrointestinal.

**UBERON Terms**: UBERON:0000014 (skin of body), UBERON:0010230 (Bruch's membrane), UBERON:0001637 (artery), UBERON:0000947 (aorta), UBERON:0001621 (coronary artery).

### Tissue and Cell Level

**Tissue Types**:
- **Elastic connective tissue** (mid-dermis, arterial media, Bruch's membrane) (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4).
- **Vascular smooth muscle** within arterial walls (germain2017pseudoxanthomaelasticum pages 2-4).

**Cell Populations**:
- **Dermal fibroblasts**: Show pro-calcification phenotype and altered ECM remodeling (plumers2023matrixmetalloproteinasescontribute pages 1-2).
- **Hepatocytes**: Primary site of ABCC6 expression and ATP efflux; deficiency here drives systemic PPi depletion (verschuere2020frommembraneto pages 8-10, germain2017pseudoxanthomaelasticum pages 4-5).
- **Renal tubular cells**: Secondary site of ABCC6 expression contributing to PPi homeostasis (verschuere2020frommembraneto pages 8-10).

**Cell Ontology Terms**: CL:0000057 (fibroblast), CL:0000182 (hepatocyte), CL:0000501 (epithelial cell of proximal tubule).

### Subcellular Level

ABCC6 localizes to the **basolateral plasma membrane** of hepatocytes (germain2017pseudoxanthomaelasticum pages 4-5). Some reports suggest mitochondria-associated membrane localization in mice, but primary evidence supports plasma membrane function (germain2017pseudoxanthomaelasticum pages 4-5).

**GO Cellular Component Terms**: GO:0016323 (basolateral plasma membrane), GO:0005886 (plasma membrane).

---

## 8. Temporal Development

### Onset

- **Typical age of onset**: Second decade of life (germain2017pseudoxanthomaelasticum pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3); skin changes often first appear in **childhood to adolescence** (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4).
- **Onset pattern**: Insidious/chronic; rarely presents at birth, though rare neonatal or early childhood presentations occur (marconi2015pseudoxanthomaelasticumand pages 1-2).

### Progression

- **Disease stages**: Early (dermal papules, peau d'orange), intermediate (angioid streaks, arterial calcification), advanced (CNV, severe PAD, vision loss, stroke) (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4).
- **Progression rate**: Slow, progressive over decades (germain2017pseudoxanthomaelasticum pages 1-2, leftheriotis2022relationshipsbetweenplasma pages 1-2); **age is the major determinant** of calcification severity (leftheriotis2022relationshipsbetweenplasma pages 1-2).
- **Disease course**: Chronic, progressive; no spontaneous remission reported (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4).
- **Duration**: Lifelong chronic disease (germain2017pseudoxanthomaelasticum pages 1-2).

### Patterns

- **Remission**: Not applicable; no spontaneous or treatment-induced remission of underlying mineralization (germain2017pseudoxanthomaelasticum pages 1-2).
- **Critical periods**: Visual complications may become severe in 40s if untreated; cardiovascular events increase with advancing age (luo2020therapeuticsdevelopmentfor pages 1-3, germain2017pseudoxanthomaelasticum pages 2-4).

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence**: Estimated at **1 per 25,000 to 1 per 100,000** in the general population (stumpf2021therapyofpseudoxanthoma pages 1-2, germain2017pseudoxanthomaelasticum pages 1-2, marconi2015pseudoxanthomaelasticumand pages 1-2).
- **Incidence**: Specific annual incidence data not provided in retrieved literature.
- **Sex ratio**: Slight female predominance (approximately 2:1 female:male) (marconi2015pseudoxanthomaelasticumand pages 1-2, germain2017pseudoxanthomaelasticum pages 1-2).

### Inheritance Pattern

- **Mode of inheritance**: **Autosomal recessive** (germain2017pseudoxanthomaelasticum pages 1-2, marconi2015pseudoxanthomaelasticumand pages 1-2, germain2017pseudoxanthomaelasticum pages 4-5).
- **Penetrance**: High for biallelic pathogenic variants, with age-dependent and variable expressivity (germain2017pseudoxanthomaelasticum pages 4-5, germain2017pseudoxanthomaelasticum pages 2-4).
- **Expressivity**: Variable inter- and intra-familial phenotypic variability without clear genotype-phenotype correlations (marconi2015pseudoxanthomaelasticumand pages 1-2, vilder2021raremodifiervariants pages 1-2).
- **Genetic anticipation**: Not reported in PXE.
- **Germline mosaicism**: Not emphasized in retrieved literature.
- **Founder effects**: Specific population founder mutations not detailed in retrieved contexts, though recurrent variants (p.R1141X, g.del23-29) suggest possible founder contributions.
- **Consanguinity**: Increases risk as in any autosomal recessive disorder (marconi2015pseudoxanthomaelasticumand pages 1-2).
- **Carrier frequency**: Up to 1 in 80 for heterozygous ABCC6 mutations (germain2017pseudoxanthomaelasticum pages 2-4).

### Population Demographics

- **Affected populations**: No strong ethnic predilection reported in retrieved literature; disease described in diverse populations (germain2017pseudoxanthomaelasticum pages 1-2, zedde2025abcc6involvementin pages 1-2).
- **Geographic distribution**: Worldwide; no endemic regions identified (germain2017pseudoxanthomaelasticum pages 1-2).

---

## 10. Diagnostics

### Clinical Tests

**Laboratory Tests**:
- **Plasma PPi measurement**: Reduced levels (approximately 40–60% of normal) are characteristic but not routinely used diagnostically (leftheriotis2022relationshipsbetweenplasma pages 1-2, verschuere2020frommembraneto pages 8-10).
- **Serum calcification propensity (T50 test)**: Shorter T50 (indicative of higher calcification propensity) associated with more severe ocular, vascular, and overall disease; emerging as a potential biomarker (nollet2022serumcalcificationpropensity pages 1-2).
- **Serum fetuin-A, phosphorus, magnesium**: Determinants of T50; may provide mechanistic insights (nollet2022serumcalcificationpropensity pages 1-2).

**Biomarkers**:
- **Plasma PPi**: Low levels confirm PPi deficiency but show weak correlation with calcification severity and do not predict progression well (leftheriotis2022relationshipsbetweenplasma pages 1-2).
- **T50 serum calcification propensity**: Inversely correlates with disease severity (nollet2022serumcalcificationpropensity pages 1-2).
- **Desmosine and isodesmosine**: Biomarkers of elastin degradation (nollet2022serumcalcificationpropensity pages 1-2).

**Imaging Studies**:
- **Optical coherence tomography (OCT)**: Increased RPE-Bruch's membrane peak reflectivity in PXE patients (median 67.5 vs 32.7 in controls, p=2.43×10⁻⁵) with high discriminative value (AUC 0.85) for quantifying Bruch's membrane calcification (risseeuw2020areflectivitymeasure pages 1-2).
- **Fundus autofluorescence and near-infrared imaging**: Identify peau d'orange and angioid streaks (risseeuw2020areflectivitymeasure pages 1-2).
- **Computed tomography (CT)**: Quantifies arterial calcification (coronary, lower limb) (kranenburg2018etidronateforprevention pages 1-2, leftheriotis2022relationshipsbetweenplasma pages 1-2).
- **18F-NaF PET**: Measures active arterial mineralization; used in clinical trials as a sensitive endpoint (kranenburg2018etidronateforprevention pages 1-2).

**Functional Tests**:
- **Ankle-brachial index (ABI)**: Abnormally low in PXE due to arterial wall remodeling, independently of traditional cardiovascular risk factors (germain2017pseudoxanthomaelasticum pages 2-4).
- **Pulmonary function testing**: Some patients show reduced carbon monoxide diffusing capacity, suggesting preclinical interstitial lung involvement (germain2017pseudoxanthomaelasticum pages 2-4).

**Pathology Findings**:
- **Skin biopsy**: Accumulation of pleomorphic elastotic material in mid-dermis visualized by Verhoeff-van Gieson or Orcein stains; calcification demonstrated by von Kossa or Alizarin red staining (luo2020therapeuticsdevelopmentfor pages 1-3, marconi2015pseudoxanthomaelasticumand pages 1-2).
- **Electron microscopy**: Bulky, needle-like mineral deposits disrupting elastic fibers (germain2017pseudoxanthomaelasticum pages 1-2).

### Genetic Testing

**Recommended Approach**:
- **Whole exome sequencing (WES)** or **targeted ABCC6 gene sequencing** is the primary diagnostic approach when PXE is clinically suspected (germain2017pseudoxanthomaelasticum pages 1-2, verschuere2020frommembraneto pages 8-10).
- **Gene panels** including ABCC6, ENPP1, and NT5E can capture the ectopic mineralization disease spectrum (shimada2021abcc6pyrophosphateand pages 1-2).

**Single Gene Testing**:
- **ABCC6 sequencing**: Identifies pathogenic variants in >95% of clinically diagnosed PXE cases when both alleles are analyzed (marconi2015pseudoxanthomaelasticumand pages 1-2, verschuere2020frommembraneto pages 8-10).
- **Challenges**: Presence of two ABCC6 pseudogenes (ABCC6-Ψ1, ABCC6-Ψ2) with ~99% sequence identity complicates sequencing and requires specialized strategies to distinguish functional gene from pseudogenes (verschuere2020frommembraneto pages 8-10).

**Chromosomal Microarray and Structural Variant Detection**:
- **MLPA (multiplex ligation-dependent probe amplification)** or array CGH can detect multiexon deletions such as g.del23-29 (verschuere2020frommembraneto pages 8-10).

### Clinical Criteria

**Diagnostic Criteria (Plomp et al., revised)**:
Diagnosis based on combination of:
1. Characteristic skin findings with histopathology showing mid-dermal elastic fiber calcification.
2. Ocular findings (angioid streaks, peau d'orange).
3. Family history and/or demonstration of biallelic pathogenic ABCC6 variants (leftheriotis2022relationshipsbetweenplasma pages 1-2, risseeuw2020areflectivitymeasure pages 1-2, germain2017pseudoxanthomaelasticum pages 1-2).

**Differential Diagnosis**:
- **PXE-like disorders**: β-thalassemia-associated PXE-like syndrome (acquired, oxidative stress-mediated, without ABCC6 mutations) (germain2017pseudoxanthomaelasticum pages 4-5).
- **GACI (ENPP1 or ABCC6 mutations)**: More severe, early-onset arterial calcification (luo2020therapeuticsdevelopmentfor pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2).
- **CALJA/ACDC (NT5E mutations)**: Late-onset juxta-articular and arterial calcification (kauffenstein2024thepurinergicnature pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2).
- **Cutis laxa**: Lax skin without characteristic calcification (germain2017pseudoxanthomaelasticum pages 1-2).
- **Other causes of angioid streaks**: Sickle cell disease, thalassemia, Ehlers-Danlos syndrome (germain2017pseudoxanthomaelasticum pages 2-4).

### Screening

- **Cascade screening**: Genetic testing of at-risk family members (siblings, offspring of affected individuals) is recommended for early diagnosis and surveillance (germain2017pseudoxanthomaelasticum pages 1-2).
- **Newborn screening**: Not currently standard for PXE.

---

## 11. Outcome/Prognosis

### Survival and Mortality

- **Life expectancy**: Generally near-normal lifespan for many patients, though cardiovascular complications can reduce life expectancy in some cases (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4).
- **Mortality rate**: Cardiac complications (myocardial infarction, angina) and strokes are occasional causes of premature mortality, but are thought to be relatively rare (germain2017pseudoxanthomaelasticum pages 2-4).
- **Disease-specific mortality**: Not quantitatively specified in retrieved contexts; cardiovascular events and gastrointestinal bleeding are potential life-threatening complications (germain2017pseudoxanthomaelasticum pages 2-4).

### Morbidity and Function

- **Morbidity**: High due to visual impairment, peripheral artery disease, intermittent claudication, and stroke risk (germain2017pseudoxanthomaelasticum pages 2-4, stumpf2021therapyofpseudoxanthoma pages 1-2).
- **Disability outcomes**: Severe visual impairment and blindness can occur by the 40s without treatment; mobility limitations from PAD (luo2020therapeuticsdevelopmentfor pages 1-3, germain2017pseudoxanthomaelasticum pages 2-4).
- **Quality of life**: Visual impairment causes major degradation in vision-related QoL; vascular disease contributes to reduced social/occupational participation; cardiovascular complications show relatively less impact on general health-related QoL measures than visual complications (germain2017pseudoxanthomaelasticum pages 2-4).

### Disease Course and Complications

- **Complications**: Choroidal neovascularization with bleeding/scarring, central vision loss, peripheral artery disease, intermittent claudication, ischemic stroke, gastrointestinal bleeding, potential for myocardial infarction (germain2017pseudoxanthomaelasticum pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4).
- **Recovery potential**: No spontaneous recovery; anti-VEGF therapy can stabilize or improve vision if CNV is detected early (germain2017pseudoxanthomaelasticum pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3).

### Prognostic Factors

- **Age**: Major determinant of calcification severity; older age correlates with more extensive arterial calcification and ocular disease (leftheriotis2022relationshipsbetweenplasma pages 1-2, germain2017pseudoxanthomaelasticum pages 2-4).
- **Sex**: Females may have higher plasma PPi levels and lower lower-limb arterial calcification than males, suggesting sex-related modulation (leftheriotis2022relationshipsbetweenplasma pages 1-2).
- **Serum T50**: Shorter T50 (higher calcification propensity) independently predicts more severe ocular, vascular, and overall disease severity (nollet2022serumcalcificationpropensity pages 1-2).

---

## 12. Treatment

| Treatment Category | Specific Treatment/Intervention | Mechanism of Action | Evidence Level | Outcome/Efficacy | Side Effects/Safety | Status | MAXO terms (suggested) |
|---|---|---|---|---|---|---|---|
| Ophthalmologic pharmacotherapy | Intravitreal anti-VEGF therapy (e.g., ranibizumab, bevacizumab, aflibercept class) | Inhibits VEGF-driven choroidal neovascularization secondary to breaks/calcification in Bruch’s membrane | Established clinical practice; supported by review-level clinical evidence (germain2017pseudoxanthomaelasticum pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3, kauffenstein2024thepurinergicnature pages 1-2) | Main symptomatic treatment for ophthalmic PXE; can prevent progression to hemorrhage/scarring and preserve central vision when CNV is treated promptly (germain2017pseudoxanthomaelasticum pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3) | Standard intravitreal injection risks not detailed in retrieved contexts; no PXE-specific major safety signal highlighted in retrieved sources (germain2017pseudoxanthomaelasticum pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3) | Standard-of-care symptomatic treatment; not disease-curative (germain2017pseudoxanthomaelasticum pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3) | MAXO: anti-VEGF therapy; intravitreal injection; treatment of choroidal neovascularization |
| Anti-mineralization pharmacotherapy | Etidronate (cyclical oral bisphosphonate) | Stable pyrophosphate analog; inhibits hydroxyapatite crystal growth and ectopic mineralization | Randomized placebo-controlled clinical trial in PXE (n=74) (kranenburg2018etidronateforprevention pages 1-2) | Over 12 months, arterial calcification decreased 4% (IQR -11% to 7%) with etidronate versus increased 8% (IQR -1% to 20%) with placebo (p=0.001); fewer subretinal neovascularization events (1 vs 9; p=0.007) (kranenburg2018etidronateforprevention pages 1-2) | No major safety issues in trial; hyperphosphatemia in 48.6% vs 0% placebo, recovered spontaneously; hypocalcemia infrequent; bone density change not significantly different (kranenburg2018etidronateforprevention pages 1-2) | Investigational / off-label disease-modifying candidate; not specifically approved for PXE (kranenburg2018etidronateforprevention pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2) | MAXO: bisphosphonate therapy; ectopic calcification prevention; oral drug administration |
| Anti-mineralization pharmacotherapy | Bisphosphonates (class concept beyond etidronate) | PPi analogs that inhibit calcium phosphate crystal formation/deposition | Preclinical + review evidence; class discussed as therapeutic strategy (plumers2023matrixmetalloproteinasescontribute pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2) | Considered promising because PXE is a PPi-deficiency disorder; strongest direct human evidence among class is etidronate trial (kranenburg2018etidronateforprevention pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2) | Class-related safety issues not detailed in retrieved PXE contexts beyond etidronate findings (kranenburg2018etidronateforprevention pages 1-2) | Investigational / off-label in PXE (shimada2021abcc6pyrophosphateand pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2) | MAXO: bisphosphonate therapy |
| Enzyme replacement / pathway restoration | INZ-701 (recombinant ENPP1) | Restores extracellular ENPP1 activity, raising plasma PPi by using circulating ATP substrate | Preclinical mouse study in Abcc6-/- PXE model (jacobs2022inz‐701arecombinant pages 1-3) | Increased steady-state plasma ENPP1 activity and PPi; significantly reduced ectopic calcification in muzzle skin biomarker tissue after 8 weeks (jacobs2022inz‐701arecombinant pages 1-3) | Human safety not available in retrieved PXE contexts; preclinical study supports therapeutic potential (jacobs2022inz‐701arecombinant pages 1-3) | Preclinical / investigational for PXE (jacobs2022inz‐701arecombinant pages 1-3) | MAXO: enzyme replacement therapy; recombinant protein therapy; pyrophosphate restoration |
| Nutritional / metabolic support | Magnesium supplementation / increased magnesium | May reduce calcification propensity by influencing mineral buffering and crystal formation; magnesium associated with higher T50 (calcification resistance) (nollet2022serumcalcificationpropensity pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2) | Biomarker association + review/preclinical rationale (nollet2022serumcalcificationpropensity pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2) | Not proven as definitive therapy in retrieved human PXE trials; biologically plausible adjunct because magnesium was a determinant of serum T50 (p=0.034) (nollet2022serumcalcificationpropensity pages 1-2) | Specific PXE safety data not detailed in retrieved contexts (nollet2022serumcalcificationpropensity pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2) | Supportive / investigational adjunct (nollet2022serumcalcificationpropensity pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2) | MAXO: magnesium supplementation; dietary mineral supplementation |
| Lifestyle / risk reduction | Lifestyle modification and vascular risk-factor control | Reduces additive cardiovascular risk in a disease with arterial calcification/PAD and stroke risk | Review/guideline-style clinical recommendation (germain2017pseudoxanthomaelasticum pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2, zedde2025abcc6involvementin pages 1-2) | Recommended as part of standard management; aimed at reducing vascular complications rather than reversing PXE (germain2017pseudoxanthomaelasticum pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2) | Generally safe; details not quantified in retrieved contexts (germain2017pseudoxanthomaelasticum pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2) | Standard supportive care (germain2017pseudoxanthomaelasticum pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2) | MAXO: lifestyle modification; cardiovascular risk reduction; smoking avoidance; exercise counseling |
| Lipid-lowering / vascular prevention | Lipid-lowering measures | Addresses cardiovascular risk burden and possible dyslipidemia contribution | Review-level clinical recommendation (germain2017pseudoxanthomaelasticum pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2, zedde2025abcc6involvementin pages 1-2) | Used to reduce vascular risk factors; not shown in retrieved contexts to reverse mineralization directly (germain2017pseudoxanthomaelasticum pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2) | Drug-specific adverse effects not detailed in retrieved PXE contexts (germain2017pseudoxanthomaelasticum pages 1-2) | Supportive standard care when indicated (germain2017pseudoxanthomaelasticum pages 1-2) | MAXO: lipid-lowering therapy |
| Surgical / interventional vascular care | Vascular surgery / endovascular intervention for severe PAD or arterial lesions | Revascularization or treatment of advanced vascular stenosis/occlusion | Clinical practice / symptomatic management (germain2017pseudoxanthomaelasticum pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2) | Reserved for severe cardiovascular manifestations; may be necessary in advanced stages of PAD (germain2017pseudoxanthomaelasticum pages 1-2, vilder2021raremodifiervariants pages 1-2) | Success may be affected by distal vessel involvement/calcification; careful vascular assessment recommended (germain2017pseudoxanthomaelasticum pages 2-4) | Standard symptomatic intervention when indicated (germain2017pseudoxanthomaelasticum pages 1-2) | MAXO: vascular surgery; endovascular procedure; peripheral revascularization |
| Dermatologic / cosmetic management | Management of skin lesions / cosmetic care | Addresses lax redundant skin and cosmetic burden rather than underlying metabolic defect | Review-level clinical experience (marconi2015pseudoxanthomaelasticumand pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2) | Cutaneous findings are primarily cosmetic concern; treatment does not address systemic disease (luo2020therapeuticsdevelopmentfor pages 1-3, marconi2015pseudoxanthomaelasticumand pages 1-2) | Safety depends on procedure; specific PXE data limited in retrieved contexts (marconi2015pseudoxanthomaelasticumand pages 1-2) | Supportive / symptomatic (marconi2015pseudoxanthomaelasticumand pages 1-2) | MAXO: dermatologic care; cosmetic intervention |
| Experimental small-molecule therapy | Minocycline | DDR/PARP1-modulating effects; proposed anticalcifying activity in PXE pathogenesis | Preclinical proof-of-concept in Abcc6-/- mice (jacobs2022inz‐701arecombinant pages 1-3) | Oral minocycline reduced ectopic calcification by 43.4% (p<0.0001) in Abcc6-/- mice; supported by H2AX evidence of DDR activation at calcification sites (jacobs2022inz‐701arecombinant pages 1-3) | Favorable human safety profile noted generally in paper abstract, but no PXE clinical safety data provided (jacobs2022inz‐701arecombinant pages 1-3) | Preclinical / investigational repurposing candidate (jacobs2022inz‐701arecombinant pages 1-3) | MAXO: tetracycline therapy; DNA-damage-response modulation |
| Experimental anti-crystallization therapy | SNF472 / CSL525 (hexasodium fytate) | Direct inhibitor of calcium phosphate crystallization | Preclinical animal studies (zebrafish, mouse, rat models) (kranenburg2018etidronateforprevention pages 1-2) | Reduced calcified area by ~40% in abcc6a-/- zebrafish larvae; inhibited muzzle calcification by 57% in abcc6-/- mice; inhibited rat skin calcification by 60% (kranenburg2018etidronateforprevention pages 1-2) | Human PXE safety not available in retrieved contexts (kranenburg2018etidronateforprevention pages 1-2) | Preclinical / investigational (kranenburg2018etidronateforprevention pages 1-2) | MAXO: calcification inhibitor therapy; phytate therapy |
| Gene-based therapy | Gene therapy / gene editing / liver-directed correction of ABCC6 | Restores ABCC6 function in liver, the main source of systemic anti-calcification signaling | Review/future perspective in PXE; preclinical direction supported broadly (germain2017pseudoxanthomaelasticum pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2) | Considered a plausible future disease-modifying approach; no approved human PXE gene therapy in retrieved contexts (germain2017pseudoxanthomaelasticum pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2) | Clinical safety not established for PXE in retrieved contexts (germain2017pseudoxanthomaelasticum pages 1-2) | Investigational / conceptual-preclinical (germain2017pseudoxanthomaelasticum pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2) | MAXO: gene therapy; genome editing; liver-directed gene transfer |
| Pharmacologic chaperone strategy | Pharmacologic chaperone therapy for selected ABCC6 variants | Aims to rescue trafficking/function of misfolded but potentially rescuable ABCC6 protein | Review/future perspective (germain2017pseudoxanthomaelasticum pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2) | Potentially useful for certain variant classes; no established clinical efficacy in retrieved contexts (germain2017pseudoxanthomaelasticum pages 1-2) | Safety unknown in PXE clinical practice from retrieved contexts (germain2017pseudoxanthomaelasticum pages 1-2) | Investigational / conceptual-preclinical (germain2017pseudoxanthomaelasticum pages 1-2) | MAXO: pharmacologic chaperone therapy |
| Supportive care / monitoring | Regular ophthalmologic, dermatologic, and vascular surveillance | Early detection and management of CNV, PAD, calcification progression, and complications | Standard clinical management supported by natural history/diagnostic literature (leftheriotis2022relationshipsbetweenplasma pages 1-2, risseeuw2020areflectivitymeasure pages 1-2, germain2017pseudoxanthomaelasticum pages 1-2) | Important because progression is chronic and age-dependent; enables timely anti-VEGF and vascular intervention (leftheriotis2022relationshipsbetweenplasma pages 1-2, risseeuw2020areflectivitymeasure pages 1-2, germain2017pseudoxanthomaelasticum pages 1-2) | Low procedural risk from surveillance itself; burden of repeated monitoring not quantified (leftheriotis2022relationshipsbetweenplasma pages 1-2, risseeuw2020areflectivitymeasure pages 1-2) | Standard supportive care (germain2017pseudoxanthomaelasticum pages 1-2, leftheriotis2022relationshipsbetweenplasma pages 1-2) | MAXO: clinical surveillance; ophthalmologic monitoring; vascular monitoring |
| Biomarker-guided trial support | OCT Bruch’s membrane reflectivity; serum T50 as trial/monitoring biomarkers | Imaging/serum endpoints to quantify retinal calcification and systemic calcification propensity | Observational biomarker studies (risseeuw2020areflectivitymeasure pages 1-2, nollet2022serumcalcificationpropensity pages 1-2) | OCT RPE-BM peak reflectivity discriminated PXE from controls with AUC 0.85; shorter T50 associated with more severe ocular, vascular, and overall disease (risseeuw2020areflectivitymeasure pages 1-2, nollet2022serumcalcificationpropensity pages 1-2) | Biomarkers themselves are low-risk; clinical utility for routine treatment decisions still emerging (nollet2022serumcalcificationpropensity pages 1-2, risseeuw2020areflectivitymeasure pages 1-2) | Investigational as outcome measures / companion tools (nollet2022serumcalcificationpropensity pages 1-2, risseeuw2020areflectivitymeasure pages 1-2) | MAXO: biomarker monitoring; optical coherence tomography; serum assay monitoring |


*Table: This table summarizes current, investigational, and preclinical treatment strategies for pseudoxanthoma elasticum, including mechanisms, evidence strength, outcomes, safety considerations, and suggested MAXO mappings. It is useful for quickly comparing symptomatic care versus emerging disease-modifying approaches.*

### Pharmacotherapy

**Ophthalmologic**:
- **Anti-VEGF therapy** (ranibizumab, bevacizumab, aflibercept): Standard of care for choroidal neovascularization; prevents progression to hemorrhage and vision loss (germain2017pseudoxanthomaelasticum pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3, kauffenstein2024thepurinergicnature pages 1-2).

**Anti-Mineralization**:
- **Etidronate (bisphosphonate)**: A randomized placebo-controlled trial (n=74) showed reduced arterial calcification (−4% vs +8% placebo, p=0.001) and fewer subretinal neovascularization events (1 vs 9, p=0.007) over 12 months, without major safety issues (kranenburg2018etidronateforprevention pages 1-2).

**Investigational Enzyme Replacement**:
- **INZ-701 (recombinant ENPP1)**: Preclinical study in Abcc6-/- mice showed increased plasma PPi and significantly reduced muzzle skin calcification after 8 weeks (jacobs2022inz‐701arecombinant pages 1-3).

### Advanced Therapeutics

**Gene Therapy**:
- **Liver-directed ABCC6 gene therapy/editing**: Conceptual future approach; no approved clinical trials in retrieved contexts (germain2017pseudoxanthomaelasticum pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2).

**Experimental Small Molecules**:
- **Minocycline**: Reduced ectopic calcification by 43.4% (p<0.0001) in Abcc6-/- mice via DNA-damage-response modulation; favorable safety profile suggests repurposing potential (jacobs2022inz‐701arecombinant pages 1-3).
- **SNF472/CSL525 (hexasodium fytate)**: Direct calcification inhibitor reduced calcification by 40–60% in zebrafish, mouse, and rat models (kranenburg2018etidronateforprevention pages 1-2).

### Supportive and Rehabilitative Care

- **Lifestyle modification and cardiovascular risk reduction**: Recommended to mitigate additional vascular risk (smoking cessation, lipid control, blood pressure management) (germain2017pseudoxanthomaelasticum pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2).
- **Vascular surgery**: Reserved for severe PAD; success may be affected by distal vessel calcification (germain2017pseudoxanthomaelasticum pages 1-2, vilder2021raremodifiervariants pages 1-2).
- **Regular ophthalmologic, vascular, and dermatologic surveillance**: Enables early detection and treatment of CNV and PAD (germain2017pseudoxanthomaelasticum pages 1-2, leftheriotis2022relationshipsbetweenplasma pages 1-2, risseeuw2020areflectivitymeasure pages 1-2).

### Treatment Outcomes

- **Etidronate trial**: Reduced arterial calcification and CNV events; hyperphosphatemia was common but self-limited (kranenburg2018etidronateforprevention pages 1-2).
- **Anti-VEGF**: Standard symptomatic treatment preserving vision when CNV is treated promptly (germain2017pseudoxanthomaelasticum pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3).

### MAXO Terms

Suggested MAXO terms are included in artifact-02 for each treatment category.

---

## 13. Prevention

### Prevention Levels

**Primary Prevention**:
- Not applicable for this genetic disorder; genetic counseling and carrier screening in at-risk families can guide reproductive decisions (germain2017pseudoxanthomaelasticum pages 1-2).

**Secondary Prevention**:
- **Early detection via cascade screening** of at-risk family members enables earlier surveillance and intervention (germain2017pseudoxanthomaelasticum pages 1-2).
- **Regular ophthalmologic surveillance** to detect CNV early and initiate anti-VEGF therapy (germain2017pseudoxanthomaelasticum pages 1-2, risseeuw2020areflectivitymeasure pages 1-2).

**Tertiary Prevention**:
- **Management of cardiovascular risk factors** (lifestyle, lipid-lowering, antihypertensives) to reduce additive vascular complications (germain2017pseudoxanthomaelasticum pages 1-2, stumpf2021therapyofpseudoxanthoma pages 1-2).
- **Anti-VEGF therapy** for CNV to prevent blindness (germain2017pseudoxanthomaelasticum pages 1-2, luo2020therapeuticsdevelopmentfor pages 1-3).

### Genetic Screening and Counseling

- **Carrier screening**: Heterozygous carriers identified in families can inform genetic counseling and reproductive planning (germain2017pseudoxanthomaelasticum pages 1-2).
- **Genetic counseling**: Risk assessment and family planning guidance for affected individuals and carrier families (germain2017pseudoxanthomaelasticum pages 1-2, vilder2021raremodifiervariants pages 1-2).

### Behavioral Interventions

- **Smoking cessation, healthy diet, regular exercise**: Reduce cardiovascular risk burden (stumpf2021therapyofpseudoxanthoma pages 1-2, germain2017pseudoxanthomaelasticum pages 1-2).

---

## 14. Other Species / Natural Disease

Limited information on naturally occurring PXE in other species was retrieved. PXE is primarily a human genetic disorder. However, animal models (discussed below) are critical for research.

---

## 15. Model Organisms

| Model Type | Species/Model Name | Genetic Background | Phenotype Recapitulation | Research Applications | Model Advantages | Model Limitations | Key Resources/References |
|---|---|---|---|---|---|---|---|
| Mammalian knockout model | **Abcc6-/- mouse** | Targeted deletion of **Abcc6**; widely used knockout line, including congenic strains; earliest calcification readout is the connective tissue sheath of vibrissae/muzzle skin (jacobs2022inz‐701arecombinant pages 1-3, verschuere2020frommembraneto pages 8-10) | Recapitulates ectopic calcification in **skin, vasculature, ocular tissues, and kidneys**; mineralization of vibrissae capsule is a robust biomarker; mirrors PPi deficiency and progressive soft-tissue mineralization seen in human PXE (leftheriotis2022relationshipsbetweenplasma pages 1-2, jacobs2022inz‐701arecombinant pages 1-3, verschuere2020frommembraneto pages 8-10) | Pathomechanism studies of **PPi deficiency**, testing anti-calcification therapies (etidronate, INZ-701, minocycline), biomarker development, natural-history studies, and tissue-level histopathology (jacobs2022inz‐701arecombinant pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2, leftheriotis2022relationshipsbetweenplasma pages 1-2) | Best-established mammalian PXE model; strong face validity for systemic calcification; supports longitudinal intervention studies and quantitative histology/biochemistry (jacobs2022inz‐701arecombinant pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2) | Does not fully capture all human chronic ocular/vascular outcomes; vibrissae calcification is a convenient biomarker but not a direct human anatomical correlate; murine disease course differs from human timing/severity (leftheriotis2022relationshipsbetweenplasma pages 1-2, shimada2021abcc6pyrophosphateand pages 1-2) | INZ-701 prevention study; minocycline proof-of-concept; general PXE pathway reviews (jacobs2022inz‐701arecombinant pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2, li2019pseudoxanthomaelasticumas pages 1-6) |
| Mammalian rat model | **Abcc6-/- rat** | Rat knockout for **Abcc6**; cited as sharing many commonalities with human ABCC6 deficiency (verschuere2020frommembraneto pages 8-10) | Shows ectopic mineralization of **blood vessels, Bruch's membrane, and skin**, with hallmark **vibrissae sheath mineralization** similar to mouse; also shows reduced plasma PPi and kidney PPi excretion data (verschuere2020frommembraneto pages 8-10) | Comparative mammalian physiology, systemic PPi biology, ocular histology, and validation of liver-kidney contributions to mineralization homeostasis (verschuere2020frommembraneto pages 8-10) | Larger size may benefit imaging, tissue sampling, and some physiology studies; closer procedural flexibility than mouse for some assays (verschuere2020frommembraneto pages 8-10) | Much less extensively characterized than the mouse in retrieved PXE literature; fewer intervention datasets and fewer standardized community resources noted here (verschuere2020frommembraneto pages 8-10) | ABCC6 cross-species review and comparative biology discussion (verschuere2020frommembraneto pages 8-10) |
| Zebrafish genetic model | **abcc6a-/- zebrafish** | Loss of **abcc6a**, regarded as the most likely zebrafish ortholog of human **ABCC6**; abcc6a expressed locally by osteoblast-like cells at craniofacial and skeletal mineralization sites (verschuere2020frommembraneto pages 8-10) | Recapitulates **aberrant mineralization**, though with a more skeletal/local developmental pattern than classic human hepatic-systemic PXE; used as calcification-readout model for anti-mineralization compounds (jacobs2022inz‐701arecombinant pages 1-3, verschuere2020frommembraneto pages 8-10) | Rapid in vivo screening of anti-calcification compounds such as **minocycline** and **SNF472/CSL525**; developmental mineralization studies; pathway probing (jacobs2022inz‐701arecombinant pages 1-3, kranenburg2018etidronateforprevention pages 1-2, verschuere2020frommembraneto pages 8-10) | Fast, scalable, transparent vertebrate model suitable for higher-throughput drug screening and early mechanism studies (jacobs2022inz‐701arecombinant pages 1-3, kranenburg2018etidronateforprevention pages 1-2) | Mineralization pattern is not fully homologous to human PXE because zebrafish **abcc6a** acts more locally in skeletal mineralization than mammalian liver-driven systemic PXE; limited direct translation for skin/eye phenotypes (verschuere2020frommembraneto pages 8-10) | Comparative ABCC6 review; drug-testing studies using zebrafish mineralization endpoints (verschuere2020frommembraneto pages 8-10, kranenburg2018etidronateforprevention pages 1-2, jacobs2022inz‐701arecombinant pages 1-3) |
| Zebrafish paralog model / comparative system | **abcc6b(1/2) zebrafish** | Zebrafish paralogs **abcc6b1/abcc6b2**; **abcc6b** expressed in renal proximal tubules, with function less clearly defined (verschuere2020frommembraneto pages 8-10) | No fully defined PXE-like phenotype summarized in retrieved contexts; mainly relevant as a comparative paralog system for understanding tissue-specific ABCC6 evolution and function (verschuere2020frommembraneto pages 8-10) | Comparative genomics, functional dissection of paralog specialization, and kidney-related ABCC6 biology (verschuere2020frommembraneto pages 8-10) | Useful for evolutionary and orthology questions that cannot be addressed in mammalian single-gene systems (verschuere2020frommembraneto pages 8-10) | Unclear disease validity for human PXE; limited direct phenotypic application in retrieved studies (verschuere2020frommembraneto pages 8-10) | ABCC6 phylogenetics and zebrafish paralog discussion (verschuere2020frommembraneto pages 8-10) |
| Primary cellular model | **PXE patient dermal fibroblasts** | Fibroblasts isolated from lesional or non-lesional skin of individuals with biallelic **ABCC6** pathogenic variants; often compared with control dermal fibroblasts (plumers2023matrixmetalloproteinasescontribute pages 1-2, nollet2022serumcalcificationpropensity pages 1-2) | Show **pro-calcification phenotype**, lower cytosolic/extracellular PPi, lower **ENPP1** expression, altered ECM remodeling, elevated **MMPs**, altered lipid metabolism/senescence-related features, and skin microenvironment differences between calcified and non-calcified areas (plumers2023matrixmetalloproteinasescontribute pages 1-2, nollet2022serumcalcificationpropensity pages 1-2) | ECM remodeling studies, secretome analysis, MMP biology, calcification induction assays, biomarker discovery, testing inhibitors such as **Marimastat** and mechanistic work on local dermal drivers of mineralization (plumers2023matrixmetalloproteinasescontribute pages 1-2, nollet2022serumcalcificationpropensity pages 1-2) | Human patient-derived system captures cell-autonomous and microenvironmental features of PXE skin; useful for mechanistic and translational in vitro assays (plumers2023matrixmetalloproteinasescontribute pages 1-2, nollet2022serumcalcificationpropensity pages 1-2) | Peripheral fibroblasts express much lower ABCC6 than liver, so they do not model the full systemic liver-driven component of PXE; culture artifacts and inter-patient variability can be substantial (germain2017pseudoxanthomaelasticum pages 4-5, plumers2023matrixmetalloproteinasescontribute pages 1-2) | MMP overexpression study; fibroblast secretome study; older pathophysiology review (plumers2023matrixmetalloproteinasescontribute pages 1-2, nollet2022serumcalcificationpropensity pages 1-2, germain2017pseudoxanthomaelasticum pages 4-5) |
| Engineered cell system | **HEK293 cells expressing human or rat ABCC6** | Heterologous overexpression of **hABCC6** or **rABCC6** in HEK293 cells for transport/metabolomic studies (verschuere2020frommembraneto pages 8-10, germain2017pseudoxanthomaelasticum pages 4-5) | Does not model tissue calcification directly; demonstrates **ABCC6-associated extracellular nucleotide changes** and supports the link between ABCC6 activity, ATP-related efflux, and PPi biology (verschuere2020frommembraneto pages 8-10, germain2017pseudoxanthomaelasticum pages 4-5) | Transport assays, substrate discovery, untargeted metabolomics, mechanistic analysis of ATP/PPi-related signaling, and variant-function interrogation (verschuere2020frommembraneto pages 8-10, germain2017pseudoxanthomaelasticum pages 4-5) | Highly manipulable system for biochemical and transport-focused studies; useful for dissecting upstream molecular function of ABCC6 (verschuere2020frommembraneto pages 8-10) | Low physiological context; no connective tissue matrix or whole-organism mineralization phenotype; substrate identity remains unresolved despite these systems (verschuere2020frommembraneto pages 8-10, germain2017pseudoxanthomaelasticum pages 4-5) | ABCC6 transport/function reviews and mechanistic summaries (verschuere2020frommembraneto pages 8-10, germain2017pseudoxanthomaelasticum pages 4-5, kauffenstein2024thepurinergicnature pages 1-2) |


*Table: This table summarizes the main in vivo and in vitro model systems used in pseudoxanthoma elasticum research, including what parts of the human disease they capture and where they are most useful. It helps compare mammalian, zebrafish, and cellular platforms for mechanism, biomarker, and therapeutic studies.*

### Key Model Systems

**Abcc6-/- mouse**: Most established mammalian model; recapitulates systemic calcification with vibrissae sheath mineralization as a robust biomarker; widely used for therapeutic testing (INZ-701, etidronate, minocycline) (jacobs2022inz‐701arecombinant pages 1-3, shimada2021abcc6pyrophosphateand pages 1-2, leftheriotis2022relationshipsbetweenplasma pages 1-2).

**Abcc6-/- rat**: Shares many features with mouse; provides kidney PPi excretion data and comparative mammalian physiology (verschuere2020frommembraneto pages 8-10).

**abcc6a-/- zebrafish**: Rapid, scalable model for screening anti-calcification compounds; skeletal/local mineralization pattern differs from hepatic-systemic human PXE (verschuere2020frommembraneto pages 8-10, kranenburg2018etidronateforprevention pages 1-2, jacobs2022inz‐701arecombinant pages 1-3).

**PXE patient fibroblasts**: Human-derived system for studying ECM remodeling, MMPs, secretome, and calcification induction; captures cell-autonomous and microenvironmental features (plumers2023matrixmetalloproteinasescontribute pages 1-2, nollet2022serumcalcificationpropensity pages 1-2).

**HEK293-hABCC6**: Heterologous expression system for transport assays, substrate discovery, and metabolomics; does not model tissue calcification (verschuere2020frommembraneto pages 8-10, germain2017pseudoxanthomaelasticum pages 4-5).

---

## Conclusion

Pseudoxanthoma elasticum is a well-characterized genetic metabolic disorder caused by biallelic ABCC6 mutations leading to systemic PPi deficiency and progressive ectopic calcification in skin, eyes, and cardiovascular tissues. Recent advances include identification of the ABCC6-ENPP1-CD73 purinergic pathway, development of biomarkers (serum T50, OCT Bruch's membrane reflectivity), and emerging therapies such as etidronate, INZ-701, and minocycline. Comprehensive surveillance and early anti-VEGF treatment remain the mainstay of clinical management, with promising disease-modifying therapies in preclinical and early clinical development.

---

## References

All cited information is supported by the context IDs provided throughout this report, corresponding to peer-reviewed publications from 2015–2025.

References

1. (stumpf2021therapyofpseudoxanthoma pages 1-2): Max Jonathan Stumpf, Nadjib Schahab, Georg Nickenig, Dirk Skowasch, and Christian Alexander Schaefer. Therapy of pseudoxanthoma elasticum: current knowledge and future perspectives. Biomedicines, 9:1895, Dec 2021. URL: https://doi.org/10.3390/biomedicines9121895, doi:10.3390/biomedicines9121895. This article has 39 citations.

2. (germain2017pseudoxanthomaelasticum pages 1-2): Dominique P. Germain. Pseudoxanthoma elasticum. Orphanet Journal of Rare Diseases, May 2017. URL: https://doi.org/10.1186/s13023-017-0639-8, doi:10.1186/s13023-017-0639-8. This article has 246 citations and is from a peer-reviewed journal.

3. (luo2020therapeuticsdevelopmentfor pages 1-3): Hongbin Luo, Qiaoli Li, Yi Cao, and Jouni Uitto. Therapeutics development for pseudoxanthoma elasticum and related ectopic mineralization disorders: update 2020. Journal of Clinical Medicine, 10:114, Dec 2020. URL: https://doi.org/10.3390/jcm10010114, doi:10.3390/jcm10010114. This article has 44 citations.

4. (kauffenstein2024thepurinergicnature pages 1-2): Gilles Kauffenstein, Ludovic Martin, and Olivier Le Saux. The purinergic nature of pseudoxanthoma elasticum. Biology, Jan 2024. URL: https://doi.org/10.3390/biology13020074, doi:10.3390/biology13020074. This article has 9 citations.

5. (marconi2015pseudoxanthomaelasticumand pages 1-2): Barbara Marconi, Ivan Bobyr, Anna Campanati, Elisa Molinelli, Veronica Consales, Valerio Brisigotti, Marina Scarpelli, Stefano Racchini, and Annamaria Offidani. Pseudoxanthoma elasticum and skin: clinical manifestations, histopathology, pathomechanism, perspectives of treatment. Intractable & rare diseases research, 4 3:113-22, Jul 2015. URL: https://doi.org/10.5582/irdr.2015.01014, doi:10.5582/irdr.2015.01014. This article has 161 citations.

6. (kranenburg2018etidronateforprevention pages 1-2): Guido Kranenburg, Pim A. de Jong, Jonas W. Bartstra, Suzanne J. Lagerweij, Marnix G. Lam, Jeannette Ossewaarde-van Norel, Sara Risseeuw, Redmer van Leeuwen, Saskia M. Imhof, Harald J. Verhaar, Job J. de Vries, Riemer H.J.A. Slart, Gert Luurtsema, Annemarie M. den Harder, Frank L.J. Visseren, Willem P. Mali, and Wilko Spiering. Etidronate for prevention of ectopic mineralization in patients with pseudoxanthoma elasticum. Journal of the American College of Cardiology, 71 10:1117-1126, Mar 2018. URL: https://doi.org/10.1016/j.jacc.2017.12.062, doi:10.1016/j.jacc.2017.12.062. This article has 140 citations and is from a highest quality peer-reviewed journal.

7. (germain2017pseudoxanthomaelasticum pages 4-5): Dominique P. Germain. Pseudoxanthoma elasticum. Orphanet Journal of Rare Diseases, May 2017. URL: https://doi.org/10.1186/s13023-017-0639-8, doi:10.1186/s13023-017-0639-8. This article has 246 citations and is from a peer-reviewed journal.

8. (verschuere2020frommembraneto pages 1-5): Shana Verschuere, Matthias Van Gils, Lukas Nollet, and Olivier M. Vanakker. From membrane to mineralization: the curious case of the abcc6 transporter. FEBS Letters, 594:4109-4133, Nov 2020. URL: https://doi.org/10.1002/1873-3468.13981, doi:10.1002/1873-3468.13981. This article has 21 citations and is from a peer-reviewed journal.

9. (shimada2021abcc6pyrophosphateand pages 1-2): Briana K. Shimada, Viola Pomozi, Janna Zoll, Sheree Kuo, Ludovic Martin, and Olivier Le Saux. Abcc6, pyrophosphate and ectopic calcification: therapeutic solutions. International Journal of Molecular Sciences, 22:4555, Apr 2021. URL: https://doi.org/10.3390/ijms22094555, doi:10.3390/ijms22094555. This article has 64 citations.

10. (leftheriotis2022relationshipsbetweenplasma pages 1-2): Georges Leftheriotis, Nastassia Navasiolava, Laetitia Clotaire, Christophe Duranton, Olivier Le Saux, Saïd Bendahhou, Audrey Laurain, Isabelle Rubera, and Ludovic Martin. Relationships between plasma pyrophosphate, vascular calcification and clinical severity in patients affected by pseudoxanthoma elasticum. Journal of Clinical Medicine, 11:2588, May 2022. URL: https://doi.org/10.3390/jcm11092588, doi:10.3390/jcm11092588. This article has 28 citations.

11. (zedde2025abcc6involvementin pages 1-2): Marialuisa Zedde and Rosario Pascarella. Abcc6 involvement in cerebral small vessel disease: potential mechanisms and associations. Genes, 16:728, Jun 2025. URL: https://doi.org/10.3390/genes16070728, doi:10.3390/genes16070728. This article has 4 citations.

12. (verschuere2020frommembraneto pages 8-10): Shana Verschuere, Matthias Van Gils, Lukas Nollet, and Olivier M. Vanakker. From membrane to mineralization: the curious case of the abcc6 transporter. FEBS Letters, 594:4109-4133, Nov 2020. URL: https://doi.org/10.1002/1873-3468.13981, doi:10.1002/1873-3468.13981. This article has 21 citations and is from a peer-reviewed journal.

13. (li2019pseudoxanthomaelasticumas pages 1-6): Qiaoli Li, Koen van de Wetering, and Jouni Uitto. Pseudoxanthoma elasticum as a paradigm of heritable ectopic mineralization disorders: pathomechanisms and treatment development. The American journal of pathology, 189 2:216-225, Feb 2019. URL: https://doi.org/10.1016/j.ajpath.2018.09.014, doi:10.1016/j.ajpath.2018.09.014. This article has 79 citations.

14. (plumers2023matrixmetalloproteinasescontribute pages 1-2): Ricarda Plümers, Christopher Lindenkamp, Michel Robin Osterhage, Cornelius Knabbe, and Doris Hendig. Matrix metalloproteinases contribute to the calcification phenotype in pseudoxanthoma elasticum. Biomolecules, 13:672, Apr 2023. URL: https://doi.org/10.3390/biom13040672, doi:10.3390/biom13040672. This article has 10 citations.

15. (vilder2021raremodifiervariants pages 1-2): Eva Y. G. De Vilder, Ludovic Martin, Georges Lefthériotis, Paul Coucke, Filip Van Nieuwerburgh, and Olivier M. Vanakker. Rare modifier variants alter the severity of cardiovascular disease in pseudoxanthoma elasticum: identification of novel candidate modifier genes and disease pathways through mixture of effects analysis. Frontiers in Cell and Developmental Biology, Jun 2021. URL: https://doi.org/10.3389/fcell.2021.612581, doi:10.3389/fcell.2021.612581. This article has 14 citations.

16. (germain2017pseudoxanthomaelasticum pages 2-4): Dominique P. Germain. Pseudoxanthoma elasticum. Orphanet Journal of Rare Diseases, May 2017. URL: https://doi.org/10.1186/s13023-017-0639-8, doi:10.1186/s13023-017-0639-8. This article has 246 citations and is from a peer-reviewed journal.

17. (nollet2022serumcalcificationpropensity pages 1-2): Lukas Nollet, Matthias Van Gils, Suzanne Fischer, Laurence Campens, Swapna Karthik, Andreas Pasch, Julie De Zaeytijd, Bart P. Leroy, Daniel Devos, Tine De Backer, Paul J. Coucke, and Olivier M. Vanakker. Serum calcification propensity t50 associates with disease severity in patients with pseudoxanthoma elasticum. Journal of Clinical Medicine, 11:3727, Jun 2022. URL: https://doi.org/10.3390/jcm11133727, doi:10.3390/jcm11133727. This article has 11 citations.

18. (risseeuw2020areflectivitymeasure pages 1-2): Sara Risseeuw, Edwin Bennink, Maarten G. Poirot, Pim A. de Jong, Wilko Spiering, Saskia M. Imhof, Redmer van Leeuwen, and Jeannette Ossewaarde-van Norel. A reflectivity measure to quantify bruch's membrane calcification in patients with pseudoxanthoma elasticum using optical coherence tomography. Jul 2020. URL: https://doi.org/10.1167/tvst.9.8.34, doi:10.1167/tvst.9.8.34. This article has 17 citations and is from a peer-reviewed journal.

19. (jacobs2022inz‐701arecombinant pages 1-3): Ida Joely Jacobs, Zhiliang Cheng, Douglas Ralph, Kevin O'Brien, Lisa Flaman, Jennifer Howe, David Thompson, Jouni Uitto, Qiaoli Li, and Yves Sabbagh. <scp>inz</scp>‐701, a recombinant <scp>enpp1</scp> enzyme, prevents ectopic calcification in an <i>abcc6</i><sup>−/−</sup> mouse model of pseudoxanthoma elasticum. Experimental Dermatology, 31:1095-1101, May 2022. URL: https://doi.org/10.1111/exd.14587, doi:10.1111/exd.14587. This article has 21 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Pseudoxanthoma_Elasticum-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Pseudoxanthoma_Elasticum-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Pseudoxanthoma_Elasticum-deep-research-falcon_artifacts/artifact-02.md)
- [Edison artifact artifact-03](Pseudoxanthoma_Elasticum-deep-research-falcon_artifacts/artifact-03.md)