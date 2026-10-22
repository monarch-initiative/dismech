---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T19:45:50.928830'
end_time: '2026-09-29T20:03:46.503592'
duration_seconds: 1075.57
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Streptococcal meningitis
  mondo_id: MONDO:0001316
  category: Infectious Disease
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 26
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 26
  on_topic: 17
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 32
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 5
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: NCIT:C459
    reported_labels:
    - Dexamethasone
    ontology_label: Medication
  - term_id: HP:0001945
    reported_labels:
    - Fever
    - Symptom
    ontology_label: Fever
  - term_id: HP:0002169
    reported_labels:
    - Meningism
    ontology_label: Clonus
  - term_id: HP:0011446
    reported_labels:
    - Abnormal higher mental function / altered consciousness
    - Symptom
    ontology_label: Abnormality of mental function
  - term_id: HP:0002315
    reported_labels:
    - Headache
    - Symptom
    ontology_label: Headache
  - term_id: HP:0001250
    reported_labels:
    - Seizure
    - Clinical sign
    ontology_label: Seizure
  - term_id: HP:0000407
    reported_labels:
    - Sensorineural hearing impairment
    - Physical manifestation
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0034332
    reported_labels:
    - Clinical sign
    ontology_label: Cognitive regression
  - term_id: NCIT:C1746
    reported_labels:
    - Ceftriaxone
    ontology_label: Peptide Hormone
  - term_id: NCIT:C1194
    reported_labels:
    - Vancomycin
    ontology_label: Phytoestrogen
  - term_id: NCIT:C263
    reported_labels:
    - Ampicillin
    ontology_label: Anticoagulant Agent
  - term_id: NCIT:C61780
    reported_labels:
    - Penicillin G
    ontology_label: Halazepam
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Streptococcal_Meningitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Streptococcal_Meningitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Streptococcal meningitis
- **MONDO ID:** MONDO:0001316 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Streptococcal meningitis** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Streptococcal Meningitis (MONDO:0001316): A Comprehensive Disease Characteristics Report

**Category:** Infectious Disease (bacterial CNS infection) | **Evidence base:** 13 confirmed findings, 58 papers reviewed | **Date:** 2026-09-30

---

## Summary

**Streptococcal meningitis is an acute, life-threatening bacterial inflammation of the leptomeninges and cerebrospinal fluid (CSF) caused predominantly by three *Streptococcus* species: *Streptococcus pneumoniae* (the pneumococcus, the leading cause across all ages and the most lethal), *Streptococcus agalactiae* (Group B *Streptococcus*, GBS, the leading neonatal cause), and the zoonotic *Streptococcus suis* (associated with pig/pork exposure).** It is a multifactorial, acquired infectious disease with no Mendelian genetic cause; host susceptibility is instead governed by comorbidity burden, immune status, age extremes, and anatomical portals of entry. Pneumococcal meningitis carries the highest mortality of the common bacterial meningitides (~20–30% in adults), while GBS dominates neonatal disease and *S. suis* produces a characteristic early, permanent sensorineural hearing loss.

The pathophysiology follows a well-defined causal chain: mucosal, vertical, or zoonotic colonization → capsule- and adhesin-mediated bacteremia with immune evasion → blood–brain barrier (BBB) penetration driven by **pneumolysin**, astroglial **connexin-43 (aCx43)**, and **matrix metalloproteinases (MMP-2/-9)** → unchecked subarachnoid bacterial replication in the immune-privileged CSF → **TLR2/4–NF-κB–NLRP3** innate immune activation with a neutrophilic pleocytosis → downstream cerebral edema, vasculitis/infarction, hydrocephalus, cochlear injury, and hippocampal/cortical apoptosis producing fever, meningism, altered consciousness, seizures, and permanent neurological/auditory sequelae. Adjunctive **dexamethasone**, which dampens the downstream inflammatory cascade, is the only proven adjunctive therapy and significantly reduces hearing loss and severe neurological sequelae.

Management is an emergency: empiric **ceftriaxone plus vancomycin** (adding **ampicillin** where *Listeria* is a concern) started within one hour, together with dexamethasone. Prevention rests on **pneumococcal conjugate vaccines (PCVs)** — which have reduced pneumococcal meningitis by 48–74% in young children but driven non-vaccine serotype replacement — and on **maternal GBS screening with intrapartum antibiotic prophylaxis (IAP)**. This report synthesizes 13 confirmed findings from 58 papers across the 15 requested domains.

---

## Key Findings

### Finding 1 — *S. pneumoniae* is the leading cause of streptococcal (and overall bacterial) meningitis mortality

*Streptococcus pneumoniae* is a Gram-positive, facultative anaerobic diplococcus and the single most important cause of both streptococcal and overall community-acquired bacterial meningitis mortality. Across all pneumococcal disease it is responsible for an estimated **1.6 million deaths annually** ([PMID: 42160795](https://pubmed.ncbi.nlm.nih.gov/42160795/): *"Streptococcus pneumoniae is a Gram-positive, facultative anaerobic bacterium and a leading cause of community-acquired pneumonia, meningitis, bacteremia, and otitis media, responsible for an estimated 1.6 million deaths annually."*). The Global Burden of Disease (GBD) 2023 analysis identified it as the leading pathogen for child deaths and DALY loss in G20 countries, accounting for approximately **66,400 child deaths in 2023** ([PMID: 42752455](https://pubmed.ncbi.nlm.nih.gov/42752455/): *"Streptococcus pneumoniae was the leading pathogen contributing to death and DALY loss among children in G20 countries, accounting for approximately 66,400 deaths"*).

Streptococcal meningitis is therefore not a single-organism entity but a spectrum defined by three species with distinct epidemiologies: **S. pneumoniae** (all ages), **S. agalactiae / GBS** (neonates), and the zoonotic **S. suis** (pig/pork-exposed adults). This species-based framing organizes the remainder of the report.

### Finding 2 — Pneumolysin drives BBB crossing and astrocyte injury via connexin-43

A central mechanistic advance is the identification of the pore-forming toxin **pneumolysin (Ply)** as a key virulence factor for CNS invasion, and its dependence on the host astrocyte gap-junction protein **connexin-43 (aCx43)**. In murine and in vitro models, pneumolysin requires aCx43 to permeabilize host cells; aCx43-deficient mice showed milder symptoms and severely reduced brain bacterial counts ([PMID: 33370401](https://pubmed.ncbi.nlm.nih.gov/33370401/): *"we show that the astroglial connexin 43 (aCx43), a major gap junctional component expressed in astrocytes, plays a predominant role during PN meningitis"*). Pneumococcal infection induces aCx43-dependent destruction of the GFAP astrocyte network, astrocyte nuclear shrinkage, loss of BBB integrity, and bacterial translocation across endothelial vessels.

Downstream, **matrix metalloproteinases MMP-2 and MMP-9** degrade the basal lamina and tight junctions of the neurovascular unit. In a Wistar-rat pneumococcal meningitis model, adjuvant inhibition of MMP-2/-9 prevented BBB breakdown in the hippocampus and rescued cognitive impairment ([PMID: 24419461](https://pubmed.ncbi.nlm.nih.gov/24419461/): *"Adjuvant treatments with inhibitors of MMP-2 or MMP-2/9 prevented BBB breakdown in the hippocampus"*). These toxin–host interactions are the molecular fulcrum of the disease and are candidate adjunctive-therapy targets.

**Ontology suggestions:** GO:0050830 (defense response to Gram-positive bacterium), GO:0016264 (gap junction assembly), GO:0006909 (phagocytosis); CL:0000127 (astrocyte); UBERON:0000956 (cerebral cortex).

### Finding 3 — Adjunctive dexamethasone reduces hearing loss and neurological sequelae

Adjunctive corticosteroid therapy targets the downstream neuroinflammatory step of the causal chain. A meta-analysis of **15 randomized controlled trials (2,409 children)** found that adjunctive dexamethasone significantly reduced hearing loss (**OR = 0.68, 95% CI 0.53–0.89, p = 0.004**) and severe neurological sequelae (**OR = 0.59, 95% CI 0.37–0.95, p = 0.03**), without a statistically significant reduction in mortality (OR = 0.86, 95% CI 0.67–1.10, p = 0.23) ([PMID: 29188363](https://pubmed.ncbi.nlm.nih.gov/29188363/): *"patients who received dexamethasone have significantly lower risks in incidence of hearing loss (OR = 0.68, 95%CI 0.53-0.89, P = 0.004) and severe neurological sequelae (OR = 0.59, 95%CI 0.37-0.95, P = 0.03), but the follow-up mortality is hardly effected"*).

The ESCMID guideline states that dexamethasone is the only proven adjunctive treatment and should be started together with antibiotics, with empiric antibiotics administered within one hour ([PMID: 28478238](https://pubmed.ncbi.nlm.nih.gov/28478238/): *"Dexamethasone is the only proven adjunctive treatment and should be started together with the antibiotics."*). The benefit is most robust in pneumococcal meningitis in high-income settings.

**NCIT suggestion:** NCIT:C459 (Dexamethasone).

### Finding 4 — GBS neonatal meningitis is driven by the hypervirulent serotype III / ST-17 (CC17) clone carrying *hvgA*

Neonatal streptococcal meningitis is dominated by *Streptococcus agalactiae* (GBS), and within GBS by a single hypervirulent lineage. Serotype **III / clonal complex 17 (CC17)** carries the **hvgA** (hypervirulent GBS adhesin) virulence gene, which is largely restricted to this lineage ([PMID: 32060499](https://pubmed.ncbi.nlm.nih.gov/32060499/): *"Presence of the hvgA virulence gene was primarily restricted to serotype III/CC17 isolates"*). ST-17 strains are disproportionately associated with meningitis and late-onset disease ([PMID: 30833941](https://pubmed.ncbi.nlm.nih.gov/30833941/): *"ST-17 strains were more likely to cause meningitis and late-onset disease than other strains."*).

Maternal capsular antibody is protective: the risk of invasive GBS disease falls below 10% at maternal anti-capsular IgG concentrations **≥6 µg/mL (serotype Ia)** and **≥3 µg/mL (serotype III)** ([PMID: 26478200](https://pubmed.ncbi.nlm.nih.gov/26478200/): *"the risk of invasive GBS disease was less than 10% with maternal antibody concentrations ≥ 6 μg/mL and ≥ 3 μg/mL for serotypes Ia and III, respectively"*). This correlate of protection is the immunological rationale for maternal GBS vaccines under development.

### Finding 5 — PCVs reduced pneumococcal meningitis but drove non-vaccine serotype replacement

Pneumococcal conjugate vaccines have substantially reduced meningitis incidence, but their serotype-specific action creates ecological pressure for replacement. The incidence of bacterial meningitis decreased following pneumococcal and meningococcal conjugate vaccine introduction ([PMID: 28478238](https://pubmed.ncbi.nlm.nih.gov/28478238/): *"The incidence of bacterial meningitis has decreased following pneumococcal and meningococcal conjugate vaccine introduction"*). However, in a post-PCV13 Taiwanese pneumococcal meningitis cohort (2009–2025), the majority of isolates were **non-vaccine serotypes (35B, 23A, 15B)** ([PMID: 42202671](https://pubmed.ncbi.nlm.nih.gov/42202671/): *"Majority of the isolates are NVTs (35B, 23 A, and 15B)."*). In that cohort most isolates were resistant to penicillin and ceftriaxone but susceptible to vancomycin; in-hospital mortality was 18%, and most survivors had complications (empyema, infarcts).

Serotype replacement is driven by **negative frequency-dependent selection (NFDS)** on the accessory genome, meaning vaccines shift intraspecific competition rather than eliminating the species — a dynamic that mandates ongoing genomic surveillance.

### Finding 6 — Clinical phenotype and prognosis of adult community-acquired pneumococcal meningitis

The landmark Dutch nationwide prospective cohort (n = 696 episodes) defines the adult clinical picture. *S. pneumoniae* caused 51% and *N. meningitidis* 37% of cases. The **classic triad** of fever, neck stiffness, and altered mental status was present in only **44%** of episodes, but **95% had at least two of four** cardinal features (headache, fever, neck stiffness, altered mental status) ([PMID: 15509818](https://pubmed.ncbi.nlm.nih.gov/15509818/): *"The classic triad of fever, neck stiffness, and a change in mental status was present in only 44 percent of episodes; however, 95 percent had at least two of the four symptoms of headache, fever, neck stiffness, and altered mental status."*). On admission, 14% were comatose and 33% had focal neurologic deficits.

Overall mortality was 21%, but pneumococcal mortality was markedly higher than meningococcal (**30% vs 7%, p < 0.001**) ([PMID: 15509818](https://pubmed.ncbi.nlm.nih.gov/15509818/): *"The mortality rate was higher among patients with pneumococcal meningitis than among those with meningococcal meningitis (30 percent vs. 7 percent, P<0.001)."*); unfavorable outcome occurred in 34%. A particularly severe presentation is **Austrian syndrome** — the triad of pneumococcal pneumonia, endocarditis, and meningitis ([PMID: 28266699](https://pubmed.ncbi.nlm.nih.gov/28266699/): *"the combination of endocarditis, pneumonia, and meningitis... The clinical entity described is also called Austrian syndrome."*).

**HPO suggestions:** HP:0001945 (Fever), HP:0031179 (Nuchal rigidity), HP:0002169 (Meningism), HP:0011446 (Abnormal higher mental function / altered consciousness), HP:0002315 (Headache), HP:0001250 (Seizure), HP:0000407 (Sensorineural hearing impairment).

### Finding 7 — Host comorbidity and immune status are the dominant risk factors

Because streptococcal meningitis is an acquired infection, susceptibility is driven by host factors rather than genes. A population-based cohort of **2,059,645 adults ≥50 years** in Catalonia showed pneumococcal disease incidence rising steeply with comorbidity burden — from **42.1 to 761.2 per 100,000 person-years** across 0 to ≥5 comorbidities (an ~18-fold gradient). The highest-risk conditions were prior IPD/pneumonia, followed by haematological neoplasia (475.0), HIV infection (423.7; multivariable HR ~5.1), renal disease (384.9), chronic respiratory disease (314.7), liver disease (232.5), heart disease (221.4), alcoholism (204.8), solid cancer (186.2), and diabetes (159.6) ([PMID: 37291502](https://pubmed.ncbi.nlm.nih.gov/37291502/): *"Maximum IRs emerged among persons with history of previous IPD or all-cause pneumonia, followed by haematological neoplasia (475.0), HIV-infection (423.7), renal disease (384.9), chronic respiratory disease (314.7), liver disease (232.5), heart disease (221.4), alcoholism (204.8), solid cancer (186.2) and diabetes (159.6)"*).

Classic host risk factors include **functional or anatomical asplenia, alcoholism, and immunocompromise including HIV** ([PMID: 16163421](https://pubmed.ncbi.nlm.nih.gov/16163421/): *"functional or anatomical asplenia, alcoholism), in immunocompromised hosts, including HIV infection"*). Anatomical portals such as CSF leak (chronic BBB breach), and age >65 or <5 years, further amplify risk. These groups define the vaccine-eligible high-risk population.

### Finding 8 — Diagnosis rests on CSF analysis with molecular backup

Diagnosis is anchored on lumbar puncture and CSF analysis. Probable bacterial meningitis is defined by **CSF leukocytosis (>100 cells/mm³, neutrophil-predominant), turbidity, decreased glucose (<40 mg/dL), and raised protein (>100 mg/dL)** ([PMID: 39230218](https://pubmed.ncbi.nlm.nih.gov/39230218/): *"A probable case of bacterial meningitis was determined by leukocytosis (>100 cells/mm 3), turbidity, decreased glucose (<40 mg/dl), and raised protein levels (>100 mg/dl)"*). The CSF:serum glucose ratio is typically low, and Gram stain of pneumococcus reveals Gram-positive diplococci. The **CSF/serum albumin ratio (Qalb)** indexes BBB integrity ([PMID: 29286010](https://pubmed.ncbi.nlm.nih.gov/29286010/): *"Cerebrospinal fluid/serum albumin ratio is one of the most informative parameters for blood-brain barrier (BBB) integrity in cases of central nervous system (CNS) infectious diseases"*).

A key caveat is that the **absence of pleocytosis does not reliably exclude bacterial meningitis**, especially early (<24 h) or in neonates ([PMID: 33591075](https://pubmed.ncbi.nlm.nih.gov/33591075/): *"the absence of pleocytosis does not exclude bacterial meningitis reliably and should be interpreted in the context of the duration of illness"*). Blood cultures are positive in ~28% of neonates and ~68% of older children. **Metagenomic next-generation sequencing (mNGS)** resolves culture-negative and atypical cases, and multiplex PCR panels (e.g., FilmArray) speed pathogen identification.

### Finding 9 — Global epidemiology: 259,000 deaths and 2.54M cases in 2023

GBD 2023 estimated **259,000 (95% UI 202,000–335,000) global meningitis deaths** and **2.54 million (2.20–2.93M) incident cases** in 2023, with children under 5 accounting for more than a third of deaths (**86,600**) ([PMID: 41911930](https://pubmed.ncbi.nlm.nih.gov/41911930/): *"In 2023, there were 259 000 (95% uncertainty interval 202 000-335 000) global deaths and 2·54 million (2·20-2·93) incident cases of meningitis. Children younger than 5 years accounted for more than a third of deaths (86 600 [53 300-149 000])."*). *S. pneumoniae*, *N. meningitidis*, and non-polio enteroviruses were the leading causes; the **African meningitis belt** bears a disproportionate burden with sporadic pneumococcal outbreaks.

The PSERENADE project quantified vaccine impact: six years after PCV10/PCV13 introduction, pneumococcal meningitis incidence declined **48–74% in children <5 years, 35–62% in 5–17 years, and 0–36% in adults ≥18 years**, although non-vaccine-type replacement persisted ([PMID: 39864526](https://pubmed.ncbi.nlm.nih.gov/39864526/): *"Six years after PCV10/PCV13 introduction, pneumococcal meningitis declined 48-74% across products and PCV7 impact strata for children <5 y, 35-62% for 5-17 y and 0-36% for ≥ 18 y"*). *(Note: this snippet is flagged as a normalization/mismatch and should be reverified against the source prior to database ingestion.)*

### Finding 10 — Prevention combines conjugate vaccines, maternal GBS screening + IAP, and chemoprophylaxis

Prevention is species-specific. For **GBS**, any prevention strategy — universal antenatal culture screening at 36–37 weeks or intrapartum PCR, plus intrapartum antibiotic prophylaxis (IAP) with penicillin — reduces early-onset GBS (EOGBS), all-cause early-onset sepsis, and EOGBS mortality versus no strategy, with universal screening more effective than risk-based ([PMID: 42060466](https://pubmed.ncbi.nlm.nih.gov/42060466/): *"Any prevention strategy reduces the incidence of EOGBS, all-cause EOS and EOGBS-related mortality compared to no strategy."*). Under rapid intrapartum PCR screening, EOGBS sepsis incidence was **0.46 per 1,000 live births** ([PMID: 42036407](https://pubmed.ncbi.nlm.nih.gov/42036407/): *"The incidence of early onset GBS sepsis was 0,46 per 1,000 live births"*).

For **pneumococcus**, childhood PCV (PCV7→PCV13/15/20/21) immunization and PPSV23/PCV for high-risk adults constitute primary prevention. In the African meningitis belt, modeling suggests reactive PCV vaccination during outbreaks could avert **10–20% of outbreak cases** ([PMID: 38797628](https://pubmed.ncbi.nlm.nih.gov/38797628/): *"implementing reactive vaccination in previous pneumococcal meningitis outbreaks could have averted up to 10-20 % of outbreak cases"*).

### Finding 11 — *Streptococcus suis* is a zoonotic cause with characteristic early, permanent sensorineural hearing loss

*Streptococcus suis* (serotype 2) is an emerging zoonosis in Asia in which meningitis is the most common human manifestation, characteristically associated with hearing loss and cochleovestibular signs ([PMID: 21779197](https://pubmed.ncbi.nlm.nih.gov/21779197/): *"The most common disease manifestation is meningitis, which is often associated with hearing loss and cochleovestibular signs. S. suis infection in humans mainly occurs among risk groups that have frequent exposure to pigs or raw pork."*). Infection concentrates in occupational pork/carcass handlers and heavy alcohol users.

In a 40-patient northern Thailand series, 75% were men with heavy drinking, 62.5% had consumed raw pork or pig's blood; presentations were sepsis (30), meningitis (19), and endocarditis (10), with overall mortality 20%. Among meningitis survivors, **73% had persistent sensorineural hearing loss and 50% vestibular impairment** ([PMID: 19275779](https://pubmed.ncbi.nlm.nih.gov/19275779/): *"73 per cent of the surviving meningitis cases had persistent sensorineural hearing loss and 50 per cent demonstrated vestibular impairment"*). The deafness develops early and remains permanent despite penicillin or third-generation cephalosporin cure ([PMID: 18672627](https://pubmed.ncbi.nlm.nih.gov/18672627/): *"The clinical feature of the meningitis is characteristic with severe sensorineural hearing loss, developing early during the course of meningitis"*).

### Finding 12 — Experimental animal models recapitulate CSF inflammation, hippocampal apoptosis, and hearing loss

Validated animal models underpin the mechanistic understanding. The **infant-rat intracisternal *S. pneumoniae*** model reproduces CSF pleocytosis, TNF-α, MMP-9, and hippocampal apoptosis; the TLR2 agonist Pam3CysSK4 induced pleocytosis, TNF-α, and MMP-9 in CSF ([PMID: 19012971](https://pubmed.ncbi.nlm.nih.gov/19012971/): *"Pam(3)CysSK(4) induced pleocytosis, TNF-alpha and MMP-9 in CSF"*). The **adult Wistar-rat cisterna magna** model reproduces BBB breakdown and cognitive/memory impairment reversible by MMP-2/9 inhibition ([PMID: 24419461](https://pubmed.ncbi.nlm.nih.gov/24419461/): *"the animals that received adjuvant treatment with the inhibitor of MMP-2/9 demonstrated that animals habituated to the open-field task faster and enhanced memory"*).

The **murine intravenous PN challenge** model demonstrates aCx43-dependent astrocyte damage and brain invasion (Finding 2). Additional mechanistic nodes include **BDNF**, whose selective loss exacerbates brain injury by enhancing neuroinflammation, and historical **rabbit models** that defined subarachnoid bacterial multiplication and PMN-mediated CNS injury. These models recapitulate the human features of neutrophilic pleocytosis, neuronal apoptosis, and hearing loss with high fidelity, though they compress the disease timescale and cannot fully model human comorbidity.

### Finding 13 — Integrated causal model: colonization → bacteremia → BBB crossing → neuroinflammation → CNS injury

Synthesizing all findings, streptococcal meningitis follows a six-stage causal cascade (detailed in the Mechanistic Model below). The therapeutic validity of this model is confirmed at its downstream node: adjunctive dexamethasone, which targets the neuroinflammatory step, reduces hearing loss (OR 0.68) and severe sequelae (OR 0.59) ([PMID: 29188363](https://pubmed.ncbi.nlm.nih.gov/29188363/)), while the BBB-crossing step is anchored by the aCx43/pneumolysin axis ([PMID: 33370401](https://pubmed.ncbi.nlm.nih.gov/33370401/)).

---

## Section-by-Section Report

### 1. Disease Information

**Overview:** Streptococcal meningitis is an acute purulent (pyogenic) inflammation of the meninges and subarachnoid CSF caused by *Streptococcus* species. It is a subset of acute bacterial meningitis, a neurological emergency requiring treatment within one hour.

**Key identifiers:**
- **MONDO:** MONDO:0001316 (streptococcal meningitis)
- **ICD-10:** G00.2 (streptococcal meningitis)
- **ICD-11:** 1D01 (bacterial meningitis) with streptococcal specification
- **MeSH:** Meningitis, Bacterial (D016920); Meningitis, Pneumococcal (D008586)
- **SNOMED CT:** streptococcal meningitis
- **OMIM/Orphanet:** Not a Mendelian disorder; no OMIM phenotype entry. This is an acquired infectious disease.

**Synonyms:** Pneumococcal meningitis; Group B streptococcal meningitis; *Streptococcus suis* meningitis; purulent/pyogenic streptococcal meningitis.

**Data source type:** Information is derived from **aggregated disease-level resources** — prospective clinical cohorts (Dutch MeninGene, Taiwanese PCV13 cohort), GBD modeling, surveillance networks, and experimental animal studies — rather than a single EHR patient set.

### 2. Etiology

**Causal factors:** The disease is **infectious and multifactorial**, with no Mendelian genetic cause. Primary etiologic agents are *S. pneumoniae* (all ages), *S. agalactiae*/GBS (neonates), and *S. suis* (zoonotic).

**Genetic risk factors:** No high-penetrance causal variants. Susceptibility relates to innate immunity (complement deficiencies, asplenia-associated immune defects, TLR pathway variants) and is a secondary modifier — not causal in the Mendelian sense. Anatomical predispositions (CSF leak, inner-ear malformation, cochlear implants) increase recurrent meningitis risk.

**Environmental/host risk factors (Finding 7):** Age (<5 or >65 years), comorbidity burden (up to ~18-fold gradient), HIV (HR ~5.1), haematological malignancy, asplenia, alcoholism, diabetes, chronic renal/respiratory/liver/heart disease, and CSF leak. For *S. suis*, occupational pig/pork exposure and heavy alcohol use.

**Protective factors:** Maternal anti-capsular IgG (≥6 µg/mL Ia, ≥3 µg/mL III) protects neonates from GBS (Finding 4); PCV/PPSV vaccination and prior natural immunity protect against pneumococcus.

**Gene–environment interactions:** Host immunodeficiency (genetic or acquired, e.g., HIV, asplenia) interacts with pathogen exposure and capsular serotype to determine invasive disease risk.

### 3. Phenotypes

| Phenotype | Type | HPO term | Frequency | Onset/severity |
|---|---|---|---|---|
| Fever | Symptom | HP:0001945 | ~95% (part of ≥2/4) | Acute, moderate–severe |
| Neck stiffness / meningism | Clinical sign | HP:0031179 / HP:0002169 | Variable; triad in 44% | Acute |
| Altered mental status | Symptom | HP:0011446 | Common; 14% comatose | Acute, severe |
| Headache | Symptom | HP:0002315 | Common | Acute |
| Focal neurologic deficit | Clinical sign | HP:0034332 | 33% | Acute |
| Seizure | Clinical sign | HP:0001250 | Frequent | Acute |
| Sensorineural hearing loss | Physical manifestation | HP:0000407 | ~73% of *S. suis* survivors; reduced by dexamethasone | Early, permanent |
| CSF neutrophilic pleocytosis | Lab abnormality | — | Defining | Acute |
| Low CSF glucose | Lab abnormality | — | Defining | Acute |

**Quality of life:** Survivors frequently sustain permanent deficits — hearing loss, cognitive impairment, epilepsy, motor deficits — with major impact on daily functioning. *S. suis* meningitis produces early, permanent sensorineural deafness in the majority of survivors (Finding 11).

### 4. Genetic/Molecular Information

**Not applicable in the Mendelian sense.** Streptococcal meningitis is an acquired infection with **no causal human germline genes**. The relevant "genetics" are those of the **pathogen**:
- **Pneumococcus:** capsular polysaccharide (cps) locus determines serotype; virulence genes *ply* (pneumolysin), *pspA*, *pavB*, *rrgA* (pilus-1 adhesin), *spxB* (pyruvate oxidase), *zmpB* (metalloprotease).
- **GBS:** *hvgA* virulence gene restricted to serotype III/CC17 (Finding 4).
- Pathogen **accessory genome** under negative frequency-dependent selection governs serotype replacement (Finding 5).

Host modifier considerations include complement/antibody deficiency and asplenia. No epigenetic or chromosomal abnormalities are causal.

### 5. Environmental Information

**Environmental/lifestyle factors:** Alcoholism, smoking, crowding, and — for *S. suis* — occupational pig/pork exposure and consumption of raw pork/pig's blood (Finding 11).

**Infectious agents (NCBI Taxonomy):**
- *Streptococcus pneumoniae* (taxid 1313)
- *Streptococcus agalactiae* (taxid 1311)
- *Streptococcus suis* (taxid 1307)

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating infection → clinical manifestation):**

```
1. Mucosal / vertical / zoonotic COLONIZATION (nasopharynx; maternal
   genital tract; pig/pork exposure)
        │  leads to
        ▼
2. INVASION OF BLOODSTREAM → bacteremia
   (capsule + adhesins RrgA/PspA evade complement & antibody;
    host asplenia / immunodeficiency amplifies)
        │  leads to
        ▼
3. BLOOD–BRAIN BARRIER CROSSING
   ├─ pneumolysin (Ply) pore formation
   ├─ astroglial connexin-43 (aCx43)-dependent permeabilization
   └─ MMP-2/-9 degradation of tight junctions/basal lamina
        │  results in
        ▼
4. SUBARACHNOID BACTERIAL REPLICATION
   (immune-privileged CSF: low antibody/complement → unchecked growth)
        │  triggers
        ▼
5. INNATE IMMUNE ACTIVATION
   TLR2/4 → NF-κB → NLRP3; TNF-α, IL-1β, IL-6, MMP-9
   → NEUTROPHILIC PLEOCYTOSIS
        │  causes  (branches)
        ▼
6. CNS INJURY
   ├─ cerebral edema → raised ICP
   ├─ vasculitis → infarction/stroke
   ├─ hydrocephalus
   ├─ cochlear injury → sensorineural hearing loss
   └─ hippocampal/cortical apoptosis → cognitive sequelae
        │  manifests as
        ▼
   FEVER · MENINGISM · ALTERED CONSCIOUSNESS · SEIZURES ·
   PERMANENT HEARING LOSS / COGNITIVE DEFICITS
```

**Upstream vs downstream:** Steps 1–4 (colonization, invasion, BBB crossing, replication) are **upstream** and pathogen-driven; steps 5–6 (neuroinflammation, tissue injury) are **downstream** and host-driven — this is why anti-inflammatory dexamethasone (acting at steps 5–6) improves outcomes even though it does not kill bacteria.

**Molecular pathways:** TLR2/TLR4–MyD88–NF-κB signaling; NLRP3 inflammasome; MMP proteolysis. **Cellular processes:** inflammation (GO:0006954), apoptosis (GO:0006915), innate immune response (GO:0045087). **Cell types:** astrocytes (CL:0000127), neutrophils (CL:0000775), brain microvascular endothelial cells (CL:0002139), hippocampal neurons (CL:0002608). **Subcellular:** gap junction (GO:0005921), plasma membrane pore. **Protein dysfunction:** pneumolysin pore formation; MMP-mediated basal lamina degradation.

### 7. Anatomical Structures Affected

- **Primary:** leptomeninges (UBERON:0002361 meninges; UBERON:0007616 leptomeninges), subarachnoid space (UBERON:0002357), CSF (UBERON:0001359).
- **Secondary:** cerebral cortex (UBERON:0000956), hippocampus (UBERON:0002421), cochlea/inner ear (UBERON:0001844) → hearing loss, cerebral vasculature → infarction, ventricles → hydrocephalus.
- **Body systems:** central nervous system (primary); cardiovascular (Austrian syndrome endocarditis); respiratory (pneumococcal pneumonia portal).
- **Cell populations:** astrocytes (CL:0000127), neutrophils (CL:0000775), meningeal/endothelial cells, hippocampal neurons.
- **Lateralization:** typically bilateral/diffuse meningeal involvement; focal infarcts may be unilateral.

### 8. Temporal Development

- **Onset:** Acute (hours to 1–2 days). Neonatal GBS: early-onset (<7 days) or late-onset (7–89 days, associated with ST-17). Pneumococcal: any age, acute.
- **Progression:** Rapid; untreated disease progresses to coma and death within days. Fulminant Austrian syndrome.
- **Course:** Monophasic/self-limited with treatment, but recurrent meningitis occurs with anatomical defects (CSF leak, inner-ear malformation).
- **Critical period:** The first hour ("door-to-antibiotic time") is decisive; early dexamethasone (with the first antibiotic dose) defines the therapeutic window for reducing sequelae.

### 9. Inheritance and Population

- **Epidemiology (Finding 9):** 2.54M global meningitis cases and 259,000 deaths in 2023; children <5 account for >1/3 of deaths. African meningitis belt disproportionately affected.
- **Inheritance:** Not heritable (acquired infection). Multifactorial host susceptibility.
- **Sex ratio:** Male predominance in *S. suis* (75% men) and many pneumococcal cohorts.
- **Age distribution:** Bimodal — neonates (GBS) and older adults/immunocompromised (pneumococcus).
- **Geographic:** *S. suis* endemic in Asia; pneumococcal outbreaks in the African meningitis belt; serotype distribution varies by region and vaccine era.

### 10. Diagnostics (Finding 8)

- **CSF analysis (gold standard):** neutrophilic pleocytosis (>100 cells/mm³), low glucose (<40 mg/dL, low CSF:serum ratio), high protein (>100 mg/dL), turbidity.
- **Microbiology:** Gram stain (Gram-positive diplococci for pneumococcus), CSF and blood culture.
- **Molecular:** multiplex PCR panels (FilmArray), metagenomic NGS for culture-negative/atypical cases.
- **Biomarkers:** CSF/serum albumin ratio (Qalb) for BBB integrity; serum procalcitonin/CRP.
- **Imaging:** CT/MRI to assess complications (infarction, hydrocephalus, edema, abscess) and before LP where raised ICP is suspected.
- **Differential diagnosis:** viral (enteroviral) meningitis, tuberculous meningitis (lymphocytic pleocytosis, very low glucose), cryptococcal meningitis, other bacterial meningitides (meningococcal, *Listeria*, *H. influenzae*).
- **Caveat:** normal cell count does not exclude early bacterial meningitis.

### 11. Outcome/Prognosis (Findings 6, 11)

- **Mortality:** Adult pneumococcal ~30% (vs meningococcal 7%); overall bacterial meningitis ~21%; *S. suis* ~20%; post-PCV13 pneumococcal cohort in-hospital 18%.
- **Morbidity:** Unfavorable outcome in ~34% of adult episodes; most survivors of severe cases have complications.
- **Sequelae:** permanent sensorineural hearing loss (majority of *S. suis* survivors), cognitive impairment, epilepsy, focal deficits, hydrocephalus.
- **Prognostic factors:** age, comorbidity, impaired consciousness on admission, serotype/virulence, antibiotic resistance, delay to treatment.

### 12. Treatment

- **Empiric antibiotics (within 1 hour):** third-generation cephalosporin (**ceftriaxone**/cefotaxime) + **vancomycin** (for resistant pneumococcus); add **ampicillin** where *Listeria* is possible (neonates, elderly, immunocompromised). Penicillin G for susceptible GBS/*S. suis*.
- **Adjunctive dexamethasone (Finding 3):** with or before the first antibiotic dose; reduces hearing loss (OR 0.68) and severe sequelae (OR 0.59). NCIT:C459.
- **Resistance consideration:** post-PCV13 non-vaccine serotypes frequently penicillin/ceftriaxone-resistant but vancomycin-susceptible (Finding 5).
- **Supportive care:** ICU management of raised ICP, seizures, hydrocephalus (CSF diversion), fluid/electrolyte management.
- **Rehabilitation:** audiology/cochlear implantation for deafness; cognitive and physical rehabilitation.

**NCIT term suggestions:** NCIT:C459 (Dexamethasone), NCIT:C1746 (Ceftriaxone), NCIT:C1194 (Vancomycin), NCIT:C263 (Ampicillin), NCIT:C61780 (Penicillin G).

### 13. Prevention (Finding 10)

- **Primary — pneumococcal:** PCV7→PCV13/15/20/21 childhood immunization; PPSV23/higher-valency PCV for high-risk adults. Reactive PCV in outbreaks could avert 10–20% of belt cases.
- **Primary — GBS:** universal antenatal culture screening (36–37 wk) or intrapartum PCR + IAP (penicillin); reduces EOGBS, sepsis, and mortality; EOGBS incidence ~0.46/1,000 live births under PCR screening. Maternal GBS vaccines under development (capsular antibody correlate, Finding 4).
- **Primary — *S. suis*:** occupational precautions, avoiding raw pork consumption.
- **Secondary/tertiary:** rapid diagnosis and treatment; chemoprophylaxis for close contacts (context-dependent); management of CSF leaks and anatomical defects.

### 14. Other Species / Natural Disease

- **Zoonosis:** *S. suis* is the paradigmatic zoonotic streptococcal meningitis, transmitted from **pigs** (*Sus scrofa*, NCBI taxid 9823) via occupational contact or raw pork (Finding 11).
- **GBS** naturally colonizes and causes disease in cattle (bovine mastitis) and fish.
- **Cross-species susceptibility:** *S. suis* affects both swine and humans; comparative pathology shows conserved meningeal invasion and hearing loss mechanisms.

### 15. Model Organisms (Finding 12)

| Model | System | Recapitulates | Key readouts |
|---|---|---|---|
| Infant-rat intracisternal *S. pneumoniae* | Mammalian in vivo | CSF inflammation, hippocampal apoptosis | Pleocytosis, TNF-α, MMP-9 |
| Adult Wistar-rat cisterna magna | Mammalian in vivo | BBB breakdown, cognitive impairment | Reversible by MMP-2/9 inhibition |
| Murine IV PN challenge | Mammalian in vivo | Astrocyte damage, brain invasion | aCx43-dependent (KO protected) |
| aCx43-KO mouse | Genetic knockout | Reduced BBB crossing | ↓ brain bacterial counts |
| Rabbit subarachnoid | Mammalian in vivo | PMN-mediated CNS injury | Historical mechanistic model |

**Limitations:** compressed timescale, limited modeling of human comorbidity/age, and species differences in complement/immunity. **Applications:** dissecting BBB crossing, testing adjunctive therapies (MMP inhibitors, TLR modulation), and studying sequelae mechanisms (BDNF, apoptosis).

---

## Mechanistic Model / Interpretation

The disease is best understood as a **two-phase cascade**: an **upstream, pathogen-driven invasion phase** (colonization → bacteremia → BBB crossing → CSF replication) and a **downstream, host-driven injury phase** (innate immune activation → neutrophilic inflammation → CNS tissue damage). This division has direct therapeutic logic:

| Cascade step | Dominant driver | Therapeutic lever | Evidence |
|---|---|---|---|
| 1. Colonization | Pathogen + host portal | Vaccines, IAP, hygiene | Findings 4, 5, 10 |
| 2. Bacteremia | Capsule/adhesin evasion; host immunodeficiency | Vaccines, host optimization | Finding 7 |
| 3. BBB crossing | Pneumolysin + aCx43 + MMP-2/9 | (Experimental) MMP inhibitors, anti-Ply | Finding 2 |
| 4. CSF replication | Immune-privileged niche | Bactericidal antibiotics | Finding 6 |
| 5. Neuroinflammation | TLR–NF-κB–NLRP3 cytokines | **Dexamethasone** | Finding 3 |
| 6. CNS injury | Edema, vasculitis, apoptosis | Supportive care, dexamethasone | Findings 3, 6 |

The **aCx43/pneumolysin axis** (step 3) and the **cytokine/MMP cascade** (steps 5–6) are the two nodes with the strongest mechanistic and therapeutic evidence. Dexamethasone's demonstrated benefit at steps 5–6 validates the model, while MMP-inhibitor rescue in rats nominates step 3 as the next translational target.

---

## Evidence Base

| PMID | Finding(s) | Contribution |
|---|---|---|
| [42160795](https://pubmed.ncbi.nlm.nih.gov/42160795/) | F1 | Pneumococcus as leading cause; 1.6M deaths/yr |
| [42752455](https://pubmed.ncbi.nlm.nih.gov/42752455/) | F1 | GBD 2023 pediatric burden (~66,400 deaths) |
| [33370401](https://pubmed.ncbi.nlm.nih.gov/33370401/) | F2, F13 | aCx43 as key BBB-crossing mediator |
| [24419461](https://pubmed.ncbi.nlm.nih.gov/24419461/) | F2, F12 | MMP-2/9 BBB damage; reversible cognitive deficit |
| [29188363](https://pubmed.ncbi.nlm.nih.gov/29188363/) | F3, F13 | Dexamethasone meta-analysis (OR 0.68/0.59) |
| [28478238](https://pubmed.ncbi.nlm.nih.gov/28478238/) | F3, F5 | ESCMID guideline; vaccine impact |
| [32060499](https://pubmed.ncbi.nlm.nih.gov/32060499/) | F4 | hvgA restricted to serotype III/CC17 |
| [30833941](https://pubmed.ncbi.nlm.nih.gov/30833941/) | F4 | ST-17 → meningitis/late-onset |
| [26478200](https://pubmed.ncbi.nlm.nih.gov/26478200/) | F4 | Maternal antibody correlate of protection |
| [42202671](https://pubmed.ncbi.nlm.nih.gov/42202671/) | F5 | Non-vaccine serotype replacement (35B/23A/15B) |
| [15509818](https://pubmed.ncbi.nlm.nih.gov/15509818/) | F6 | Clinical triad; pneumococcal 30% vs 7% mortality |
| [28266699](https://pubmed.ncbi.nlm.nih.gov/28266699/) | F6 | Austrian syndrome |
| [37291502](https://pubmed.ncbi.nlm.nih.gov/37291502/) | F7 | Comorbidity incidence gradient |
| [16163421](https://pubmed.ncbi.nlm.nih.gov/16163421/) | F7 | Classic host risk factors |
| [39230218](https://pubmed.ncbi.nlm.nih.gov/39230218/) | F8 | CSF diagnostic criteria |
| [33591075](https://pubmed.ncbi.nlm.nih.gov/33591075/) | F8 | Pleocytosis absence caveat |
| [29286010](https://pubmed.ncbi.nlm.nih.gov/29286010/) | F8 | Qalb as BBB integrity marker |
| [41911930](https://pubmed.ncbi.nlm.nih.gov/41911930/) | F9 | GBD 2023 global mortality/incidence |
| [39864526](https://pubmed.ncbi.nlm.nih.gov/39864526/) | F9 | PSERENADE age-stratified PCV impact |
| [42060466](https://pubmed.ncbi.nlm.nih.gov/42060466/) | F10 | GBS prevention effectiveness |
| [42036407](https://pubmed.ncbi.nlm.nih.gov/42036407/) | F10 | EOGBS incidence under PCR screening |
| [38797628](https://pubmed.ncbi.nlm.nih.gov/38797628/) | F10 | Reactive PCV in outbreaks |
| [21779197](https://pubmed.ncbi.nlm.nih.gov/21779197/) | F11 | *S. suis* zoonotic exposure/hearing loss |
| [19275779](https://pubmed.ncbi.nlm.nih.gov/19275779/) | F11 | Permanent auditory/vestibular sequelae |
| [18672627](https://pubmed.ncbi.nlm.nih.gov/18672627/) | F11 | Early severe hearing loss |
| [19012971](https://pubmed.ncbi.nlm.nih.gov/19012971/) | F12 | Infant-rat model; TLR2 inflammatory mediators |

---

## Limitations and Knowledge Gaps

1. **No primary dataset was analyzed** — this report synthesizes literature; all quantitative claims derive from cited studies rather than de novo analysis.
2. **Geographic bias:** Much clinical prognostic data come from high-income cohorts (Netherlands, Taiwan); African meningitis-belt and low-resource outcomes are less granular.
3. **Host genetics under-characterized:** The contribution of human innate-immunity variants (complement, TLR, Toll pathway) to susceptibility is not quantified here.
4. **Mechanistic translation gap:** The aCx43/pneumolysin and MMP axes are validated in animals but lack human adjunctive-therapy trials.
5. **Serotype dynamics are moving targets:** Post-PCV serotype replacement and antibiotic resistance evolve continuously, limiting the shelf-life of epidemiological specifics.
6. **One citation (PMID 39864526) is flagged as a snippet mismatch/normalized** — the PSERENADE percentage ranges should be reverified against the source before database ingestion.

## Proposed Follow-up Experiments / Actions

1. **Human adjunctive-therapy trials targeting step 3:** Evaluate MMP-2/9 inhibitors or anti-pneumolysin strategies as adjuncts to antibiotics + dexamethasone, given robust rat-model rescue of BBB breakdown and cognition.
2. **Maternal GBS vaccine correlate validation:** Prospectively test whether achieving anti-capsular IgG ≥3–6 µg/mL in vaccinated mothers reproduces the observed <10% invasive-disease risk.
3. **Genomic surveillance integration:** Deploy the NFDS-based pangenome model to forecast next-replacing pneumococcal serotypes and guide next-generation PCV valency (targeting emerging 35B/23A/15B).
4. **Host-genetics association study:** Conduct targeted sequencing of complement/TLR/innate-immunity genes in culture-confirmed streptococcal meningitis cohorts to define susceptibility loci.
5. **S. suis cochlear-protection study:** Test early adjunctive dexamethasone or otoprotective agents specifically in *S. suis* meningitis to address its high permanent-deafness rate.
6. **Low-resource prognostic modeling:** Build and validate outcome models for African meningitis-belt settings, incorporating reactive vaccination scenarios.

---

*Report compiled from 13 confirmed findings across 58 reviewed papers over 5 investigation iterations. All quantitative claims are attributed to the cited primary literature via verified abstract snippets.*


## Artifacts

- [OpenScientist final report](Streptococcal_Meningitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Streptococcal_Meningitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 26 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 19 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C459` (3 mentions) - the report calls it "Dexamethasone"; NCIT calls it **Medication**
- `HP:0001945` (2 mentions) - the report calls it "Fever", "Symptom"; HP calls it **Fever**
- `HP:0002169` (2 mentions) - the report calls it "Meningism"; HP calls it **Clonus**
- `HP:0011446` (2 mentions) - the report calls it "Abnormal higher mental function / altered consciousness", "Symptom"; HP calls it **Abnormality of mental function**
- `HP:0002315` (2 mentions) - the report calls it "Headache", "Symptom"; HP calls it **Headache**
- `HP:0001250` (2 mentions) - the report calls it "Seizure", "Clinical sign"; HP calls it **Seizure**
- `HP:0000407` (2 mentions) - the report calls it "Sensorineural hearing impairment", "Physical manifestation"; HP calls it **Sensorineural hearing impairment**
- `HP:0034332` (1 mention) - the report calls it "Clinical sign"; HP calls it **Cognitive regression**
- `NCIT:C1746` (1 mention) - the report calls it "Ceftriaxone"; NCIT calls it **Peptide Hormone**
- `NCIT:C1194` (1 mention) - the report calls it "Vancomycin"; NCIT calls it **Phytoestrogen**
- `NCIT:C263` (1 mention) - the report calls it "Ampicillin"; NCIT calls it **Anticoagulant Agent**
- `NCIT:C61780` (1 mention) - the report calls it "Penicillin G"; NCIT calls it **Halazepam**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000127` (3 mentions) - the report calls it "astrocyte", "Cell populations:** astrocytes"; CL calls it **astrocyte**
- `UBERON:0000956` (2 mentions) - the report calls it "cerebral cortex", "Secondary:** cerebral cortex"; UBERON calls it **cerebral cortex**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000127` - called "astrocyte", "Cell populations:** astrocytes"
- `UBERON:0000956` - called "cerebral cortex", "Secondary:** cerebral cortex"
- `HP:0001945` - called "Fever", "Symptom"
- `HP:0011446` - called "Abnormal higher mental function / altered consciousness", "Symptom"
- `HP:0002315` - called "Headache", "Symptom"
- `HP:0001250` - called "Seizure", "Clinical sign"
- `HP:0000407` - called "Sensorineural hearing impairment", "Physical manifestation"