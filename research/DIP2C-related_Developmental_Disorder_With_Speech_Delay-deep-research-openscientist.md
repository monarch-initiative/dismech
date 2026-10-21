---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T18:13:20.466587'
end_time: '2026-10-16T18:45:07.906445'
duration_seconds: 1907.44
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: DIP2C-related Developmental Disorder With Speech Delay
  mondo_id: MONDO:0700356
  category: Mendelian
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
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 19
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 10
  off_topic: 3
  off_topic_references:
  - PMID:35766356
  - PMID:40327034
  - PMID:28465232
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 38
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 11
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: MONDO:0700356
    reported_labels:
    - MONDO
    ontology_label: DIP2C-related developmental disorder with speech delay
  - term_id: HP:0001263
    reported_labels:
    - Common
    ontology_label: Global developmental delay
  - term_id: HP:0001270
    reported_labels:
    - 10/10 (deletion cohort)
    ontology_label: Motor delay
  - term_id: HP:0001999
    reported_labels:
    - 9/12 (deletion); minor/inconsistent (intragenic)
    ontology_label: Abnormal facial shape
  - term_id: HP:0001252
    reported_labels:
    - 7/11 (deletion cohort)
    ontology_label: Hypotonia
  - term_id: HP:0012443
    reported_labels:
    - 4/6 (deletion cohort)
    ontology_label: Abnormal brain morphology
  - term_id: HP:0001250
    reported_labels:
    - 3/7 (deletion); focal infantile epilepsy reported
    ontology_label: Seizure
  - term_id: NCIT:C15376
    reported_labels:
    - Speech Therapy
    ontology_label: Transcendental Meditation Therapy
  - term_id: NCIT:C15277
    reported_labels:
    - Physical Therapy
    ontology_label: Mastectomy
  - term_id: NCIT:C15312
    reported_labels:
    - Supportive Care
    ontology_label: Radiation Dosimetry
  - term_id: NCIT:C49237
    reported_labels:
    - Echocardiography
    ontology_label: Chemistry Test
  - term_id: NCIT:C15431
    reported_labels:
    - Nutritional Support
    ontology_label: Hematopoietic Cell Transplantation
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: DIP2C-related_Developmental_Disorder_With_Speech_Delay-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: DIP2C-related_Developmental_Disorder_With_Speech_Delay-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DIP2C-related Developmental Disorder With Speech Delay
- **MONDO ID:** MONDO:0700356 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **DIP2C-related Developmental Disorder With Speech Delay** covering all of the
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

# DIP2C-related Developmental Disorder With Speech Delay — Comprehensive Disease Report

**MONDO ID:** MONDO:0700356 · **Gene:** *DIP2C* (Disco-interacting protein 2 homolog C) · **Locus:** 10p15.3 · **OMIM gene:** 611380 · **HGNC:** 29150 · **Category:** Mendelian (autosomal dominant)

---

## Summary

**DIP2C-related Developmental Disorder With Speech Delay is an ultra-rare, autosomal-dominant neurodevelopmental disorder caused by heterozygous loss-of-function (haploinsufficiency) of *DIP2C* at chromosome 10p15.3.** Its defining and most penetrant feature is a **developmental delay that preferentially affects expressive language and speech articulation**, frequently accompanied by variable global developmental delay, hypotonia, cognitive/behavioral differences, minor craniofacial dysmorphism, and — in a minority — seizures and congenital heart defects. The disorder was delineated as a discrete entity by Ha et al. (2024), who reported 23 individuals with heterozygous *DIP2C* variants ([PMID: 38421105](https://pubmed.ncbi.nlm.nih.gov/38421105/)). *DIP2C* is also one of the two critical-region genes (alongside *ZMYND11*) of the overlapping **10p15.3 microdeletion syndrome** ([PMID: 22847950](https://pubmed.ncbi.nlm.nih.gov/22847950/)).

**The molecular mechanism is dosage sensitivity of a conserved lipid-metabolic enzyme.** DIP2C belongs to the DISCO-interacting protein 2 (DIP2) family, which carries a DMAP1-binding domain, acyl-CoA synthetase domain, and AMP-binding (fatty-acyl-AMP-ligase, FAAL-like) sites. Across yeast, fly, worm, zebrafish, and mouse models, DIP2 proteins act as homeostatic regulators of a chemically distinct subset of **diacylglycerols (DAG)**, redirecting DAG flux into triacylglycerol, balancing *de novo* phospholipid synthesis, and controlling a DAG→PKC signaling axis. Loss of this function perturbs **axon bifurcation/guidance, axon maintenance/regeneration, and myelination**, providing a plausible causal chain from lipid dysregulation to disrupted corticolinguistic circuit maturation. gnomAD constraint metrics (pLI ≈ 1.0, LOEUF = 0.149, observed/expected LoF = 0.079) place *DIP2C* among the most loss-of-function-intolerant genes in the genome, quantitatively corroborating the haploinsufficiency model.

**Clinically, the disorder is diagnosed molecularly** — via chromosomal microarray (for 10p15.3 deletions) or exome/genome sequencing (for intragenic variants) — as there is no specific biochemical biomarker or imaging signature. Inheritance is autosomal dominant with both *de novo* and inherited variants (frequently from mildly or subclinically affected parents), with **incomplete penetrance and variable expressivity**. The core phenotype is **non-progressive and compatible with a normal lifespan**; morbidity derives from developmental disability and, in a subset, from cardiac defects or seizures. There is **no disease-specific or gene-targeted therapy** (0 registered clinical trials); management is entirely supportive, centered on early speech-language therapy, developmental support, and cardiac/seizure surveillance where indicated.

---

## 1. Disease Information

**Overview.** DIP2C-related Developmental Disorder With Speech Delay is a Mendelian neurodevelopmental disorder in which heterozygous loss-of-function of *DIP2C* produces developmental delay with a characteristic predilection for expressive speech and language. It exists on a phenotypic continuum with the contiguous-gene **10p15.3 microdeletion syndrome**, in which *DIP2C* is co-deleted with the neighbouring *ZMYND11* gene.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0700356 |
| Gene (OMIM) | *DIP2C* 611380 |
| HGNC | 29150 |
| Ensembl | ENSG00000151240 |
| Entrez Gene (human) | 22982 |
| Cytogenetic locus | 10p15.3 (GRCh37 chr10:320,130–735,683) |
| Related syndrome | 10p15.3 microdeletion syndrome (co-gene *ZMYND11*, OMIM 608668) |

**Synonyms / alternative names.** DIP2C-related developmental disorder; DIP2C haploinsufficiency; expressive speech delay associated with DIP2C variants; (overlapping) 10p15.3 microdeletion syndrome; Disco-interacting protein 2 homolog C-related disorder.

**Nature of information.** The evidence base is derived from **aggregated individual case reports and small cohorts** (not EHR-scale datasets). The anchor dataset is a 23-individual cohort with intragenic variants ([PMID: 38421105](https://pubmed.ncbi.nlm.nih.gov/38421105/)), supplemented by ~19 individuals with 10p15.3 deletions ([PMID: 22847950](https://pubmed.ncbi.nlm.nih.gov/22847950/)) and scattered prenatal/postnatal case reports.

---

## 2. Etiology

**Primary cause — genetic.** The disorder is caused by **heterozygous loss-of-function of *DIP2C*** through either intragenic variants (nonsense, frameshift, splice, and some missense) or contiguous 10p15.3 microdeletions encompassing *DIP2C*. The mechanism is **haploinsufficiency** — a single functional allele is insufficient for normal neurodevelopment. Ha et al. describe *"23 individuals with heterozygous DIP2C variants, all manifesting developmental delays that primarily affect expressive language and speech articulation"* ([PMID: 38421105](https://pubmed.ncbi.nlm.nih.gov/38421105/)).

**Genetic risk factors.** In the defining cohort, the variant spectrum comprised *"Eight patients had de novo variants predicting loss-of-function in the DIP2C gene, two patients had de novo missense variants, three had paternally inherited loss of function variants and six had maternally inherited loss-of-function variants, while inheritance was unknown for four variants"* ([PMID: 38421105](https://pubmed.ncbi.nlm.nih.gov/38421105/)). In 10p15.3 deletion cohorts, deletions were *de novo* in 7/9 tested ([PMID: 22847950](https://pubmed.ncbi.nlm.nih.gov/22847950/)). A **family history** of a mildly affected parent is itself a risk indicator, reflecting incomplete penetrance (e.g., paternal transmission of a 10p15.3 deletion from a father with mild language impairment, [PMID: 39696561](https://pubmed.ncbi.nlm.nih.gov/39696561/)).

**Environmental risk / protective factors.** No environmental risk or protective factors are established for this monogenic disorder; no modifier alleles or protective variants have been identified. Mendelian randomization in a mouse-centred study suggested a *positive causal relationship between linoleic acid and developmental disorders* ([PMID: 41054236](https://pubmed.ncbi.nlm.nih.gov/41054236/)), but this is hypothesis-generating and not clinically actionable.

**Gene–environment interactions.** None demonstrated.

---

## 3. Phenotypes

The phenotype is **neurodevelopmental and multisystem**, with a strong predilection for expressive speech. The table integrates data from the intragenic cohort ([PMID: 38421105](https://pubmed.ncbi.nlm.nih.gov/38421105/)) and the 10p15.3 deletion cohort ([PMID: 22847950](https://pubmed.ncbi.nlm.nih.gov/22847950/)). In the deletion series, *"Common features among these 12 individuals include: cognitive/behavioral/developmental differences (11/11), speech delay/language disorder (10/10), motor delay (10/10), craniofacial dysmorphism (9/12), hypotonia (7/11), brain anomalies (4/6) and seizures (3/7)"* ([PMID: 22847950](https://pubmed.ncbi.nlm.nih.gov/22847950/)).

| Phenotype | Type | Frequency | Suggested HPO term |
|---|---|---|---|
| Expressive language / speech-articulation delay | Behavioral / developmental | Core / near-universal (23/23 intragenic; 10/10 deletion) | HP:0002474 (Expressive language delay); HP:0000750 |
| Global developmental delay | Developmental | Common | HP:0001263 |
| Cognitive / intellectual / behavioral differences | Behavioral | 11/11 (deletion cohort) | HP:0001249; HP:0000708 |
| Motor delay | Developmental | 10/10 (deletion cohort) | HP:0001270 |
| Craniofacial dysmorphism (high anterior hairline/long forehead, broad nasal tip, ear anomalies) | Physical | 9/12 (deletion); minor/inconsistent (intragenic) | HP:0001999 |
| Hypotonia | Clinical sign | 7/11 (deletion cohort) | HP:0001252 |
| Brain anomalies (imaging) | Clinical sign | 4/6 (deletion cohort) | HP:0012443 |
| Seizures | Clinical sign | 3/7 (deletion); focal infantile epilepsy reported | HP:0001250 |
| Congenital heart defects (HCM, ASD, bicuspid aortic valve) | Physical | 4/23 (intragenic cohort) | HP:0001627; HP:0001631; HP:0001647 |
| Autistic-like traits / ASD | Behavioral | Reported subset | HP:0000729 |

**Phenotype characteristics.** Onset is **congenital/early-childhood**; severity is **variable (mild to moderate)**; progression is **stable/non-progressive**. Expressive speech delay is the most consistent and penetrant feature; the remaining features show incomplete penetrance and variable expressivity. The cardiac component is documented: *"Four patients had cardiac defects (hypertrophic cardiomyopathy, atrial septal defects, and bicuspid aortic valve)"* ([PMID: 38421105](https://pubmed.ncbi.nlm.nih.gov/38421105/)).

**Quality-of-life impact.** The dominant QoL burden stems from **communication impairment** (expressive speech/language), affecting education, socialization, and independence; motor delay and behavioral/cognitive issues add functional burden. No disease-specific QoL instrument (EQ-5D/SF-36/PROMIS) data exist.

---

## 4. Genetic / Molecular Information

**Causal gene.** *DIP2C* (Disco-interacting protein 2 homolog C), OMIM 611380, HGNC:29150, Ensembl ENSG00000151240, chromosome 10p15.3. In the contiguous deletion syndrome, *ZMYND11* (OMIM 608668) is co-deleted and contributes to the shared phenotype ([PMID: 22847950](https://pubmed.ncbi.nlm.nih.gov/22847950/), [PMID: 34818214](https://pubmed.ncbi.nlm.nih.gov/34818214/)). DeScipio et al. established that *"Molecular mapping of the 19 individuals reported in this study has identified two genes, ZMYND11 (OMIM 608668) and DIP2C (OMIM 611380) ... mapping within 10p15.3 which are most commonly deleted"* ([PMID: 22847950](https://pubmed.ncbi.nlm.nih.gov/22847950/)).

**Pathogenic variants.**
- **Types:** loss-of-function predominates — nonsense, frameshift, canonical splice-site — plus *de novo* missense and whole-/partial-gene deletions. A specific *de novo* splice variant **NM_014974.3:c.1057+2T>G** (minigene-confirmed 80-bp exon-8 skip) was reported in focal infantile epilepsy ([PMID: 34617658](https://pubmed.ncbi.nlm.nih.gov/34617658/)).
- **Classification:** truncating variants in this highly constrained gene are generally pathogenic/likely pathogenic by ACMG criteria (PVS1-applicable for LoF); missense variants require case-by-case evaluation.
- **Allele frequency:** pathogenic variants are ultra-rare/absent in population databases; *DIP2C* is strongly depleted of LoF variants in gnomAD.
- **Origin:** germline (both *de novo* and inherited).
- **Functional consequence:** **loss of function / haploinsufficiency.**

**Constraint (gnomAD, GRCh37).** pLI = 1.00 (0.99999999); LOEUF (oe_lof upper 90% CI) = **0.149**; observed/expected LoF = **0.079** (7 observed vs 88.1 expected PTVs); LoF Z = 8.01. The gene is also **missense-constrained** (missense Z = 4.67, oe_mis = 0.58). *DIP2C* sits in the most LoF-constrained decile of the genome — quantitative support for haploinsufficiency (Finding F005).

**Protein architecture.** DIP2 proteins *"contain a DNA methyltransferase-associated protein 1 (DMAP1) binding domain, Acyl-CoA synthetase domain and AMP-binding sites"* ([PMID: 38421105](https://pubmed.ncbi.nlm.nih.gov/38421105/)). The AMP-synthetase/FAAL-like domains confer catalytic activity on fatty acids/acyl-CoA: *"the AMP-synthetase domains of DIP2 are essential for its function, which may involve exerting a catalytic activity that modifies fatty acids"* ([PMID: 27908785](https://pubmed.ncbi.nlm.nih.gov/27908785/)).

**Modifier genes.** None established. In the deletion syndrome, co-deletion of *ZMYND11* (a chromatin reader / transcriptional regulator) likely modifies and augments the phenotype.

**Epigenetic information.** The DMAP1-binding domain links DIP2C to a chromatin-associated complex, but no disease-specific DNA-methylation signature (episignature) has been validated.

**Chromosomal abnormalities.** 10p15.3 submicroscopic microdeletions (ranging from intragenic to multi-megabase) involving *DIP2C* ± *ZMYND11*; also described in the context of ring chromosome 10 / monosomy 10 mosaicism ([PMID: 40049822](https://pubmed.ncbi.nlm.nih.gov/40049822/)) and inv dup del(10p) ([PMID: 31542096](https://pubmed.ncbi.nlm.nih.gov/31542096/)).

---

## 5. Environmental Information

This is a **monogenic disorder with no established environmental, lifestyle, or infectious contribution.** No toxins, exposures, dietary, or behavioral factors are known to cause or trigger it. Infectious agents are not applicable.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Heterozygous LoF variant or 10p15.3 deletion** reduces *DIP2C* gene dosage → **leads to** ~50% reduction in functional DIP2C protein (haploinsufficiency; gnomAD pLI ≈ 1.0, LOEUF 0.149).
2. Reduced DIP2C (a FAAL-like acyl-CoA/AMP-binding enzyme) → **results in** impaired homeostatic regulation of a chemically distinct **diacylglycerol (DAG)** subset. DIP2 is *"a homeostatic regulator of a chemically distinct subset of DAGs using yeast, fly, and mouse models"* ([PMID: 35766356](https://pubmed.ncbi.nlm.nih.gov/35766356/)).
3. Impaired DAG handling → **leads to** two coupled consequences:
   - **(3a)** reduced redirection of DAG flux into triacylglycerol — *"the fatty acyl-AMP ligase-like domains of DIP2 are essential for the redirection of the flux of DAG subspecies to storage lipid, triacylglycerols"* ([PMID: 35766356](https://pubmed.ncbi.nlm.nih.gov/35766356/)) — risking toxic DAG/ER stress; and
   - **(3b)** dysregulation of a specific DAG pool required for **PKC activation**: *"Dip2, a conserved DAG regulator across Fungi and Animalia, has emerged as a modulator of PKC signalling"* ([PMID: 40327034](https://pubmed.ncbi.nlm.nih.gov/40327034/)).
4. Loss of DIP2 lipid control → **results in** failure to counterbalance *de novo* **phospholipid (Kennedy-pathway) synthesis**: *"loss of function in dip-2 led to suppression of the axon regrowth phenotype observed in either cept-2 or ept-2 mutants, suggesting that DIP-2 acts to counterbalance phospholipid synthesis"* ([PMID: 39974891](https://pubmed.ncbi.nlm.nih.gov/39974891/)).
5. Perturbed membrane-lipid/DAG/PKC signaling → **leads to** defective **axon bifurcation and guidance**: *"DISCO Interacting Protein 2 (DIP2) is required for precise axonal bifurcation in Drosophila mushroom body (MB) neurons by suppressing ectopic bifurcation and regulating the guidance of sister axons"* ([PMID: 27908785](https://pubmed.ncbi.nlm.nih.gov/27908785/)), acting partly through the downstream phospholipase-D-superfamily effector **Glaikit** ([PMID: 28465232](https://pubmed.ncbi.nlm.nih.gov/28465232/)).
6. *Branch (mouse cortex):* DIP2C deficiency → **results in** *"a significant upregulation of sphingolipid metabolism in the cortex, accompanied by elevated oligodendrogenesis and myelination"* (via increased serine palmitoyltransferase, the rate-limiting enzyme) ([PMID: 41054236](https://pubmed.ncbi.nlm.nih.gov/41054236/)).
7. Aggregate disruption of axonal wiring and myelination during cortical development → **leads to** abnormal maturation of **corticolinguistic/cognitive circuits** → **expressive speech/language delay, developmental delay, cognitive/behavioral differences** (inferred mechanistic link bridging animal-model lipid/axon phenotypes and the human phenotype).
8. *Parallel branch (cardiac/craniofacial):* DIP2C deficiency during development → **results in** congenital heart defects and craniofacial malformations, directly demonstrated by *dip2ca* knockdown in zebrafish — *"developmental defects ... include decreased body length, craniofacial malformations, and heart defects, including pericardial edema, a linear heart tube, looping defects, and arrhythmia"*, rescued by wild-type *dip2ca* ([PMID: 40915331](https://pubmed.ncbi.nlm.nih.gov/40915331/)).

### Detail by category

- **Molecular pathways:** DAG homeostasis → DAG→**PKC** signaling; **Kennedy pathway** (de novo phospholipid synthesis) counterbalance; **sphingolipid biosynthesis** (serine palmitoyltransferase); glycerolipid/triacylglycerol storage flux.
- **Cellular processes:** axon bifurcation/guidance, axon maintenance/regeneration, oligodendrocyte differentiation/myelination, lipid storage, ER-stress avoidance.
- **Protein dysfunction:** haploinsufficiency / loss of function of a FAAL-like acyl-CoA/AMP-binding enzyme — reduced catalytic lipid-modifying activity rather than a toxic gain of function.
- **Metabolic changes:** altered diacylglycerol, triacylglycerol, phospholipid, acyl-CoA, and sphingolipid pools; abnormal lipid metabolism documented in homozygous mutant mice.
- **Subcellular localization:** DIP2 localizes to **mitochondria–vacuole contact sites** ([PMID: 35766356](https://pubmed.ncbi.nlm.nih.gov/35766356/)).
- **Immune / tissue-damage mechanisms:** not a primary feature; IMPC heterozygous mice showed incidental immune readouts (increased monocytes, altered lymphoid organ size) of uncertain relevance.

**Suggested GO terms:** GO:0046339 (diacylglycerol metabolic process), GO:0006654 (phosphatidic acid biosynthetic process), GO:0030148 (sphingolipid biosynthetic process), GO:0042552 (myelination), GO:0007411 (axon guidance), GO:0007409 (axonogenesis).
**Suggested CL terms:** CL:0000540 (neuron), CL:0000128 (oligodendrocyte), CL:0000679 (glutamatergic neuron).

---

## 7. Anatomical Structures Affected

- **Organ level — primary:** **brain / central nervous system** (UBERON:0000955 brain; UBERON:0001950 neocortex). Secondary/variable: **heart** (UBERON:0000948) with congenital defects.
- **Body systems:** nervous system (primary); cardiovascular system (subset); craniofacial/skeletal (dysmorphism); gastrointestinal (atypical gastroparesis reported in one adult with 10p15.3 deletion, [PMID: 39958070](https://pubmed.ncbi.nlm.nih.gov/39958070/)).
- **Tissue / cell level:** nervous tissue — cortical neurons and **oligodendrocytes** (myelination); affected lipid metabolism in neural cells.
- **Subcellular level (GO Cellular Component):** mitochondrion (GO:0005739), ER membrane (GO:0005789), mitochondria-associated/contact sites; cytoplasmic lipid storage.
- **Localization / lateralization:** CNS involvement is **bilateral/diffuse**; cardiac and craniofacial involvement are structure-specific.

---

## 8. Temporal Development

- **Onset:** **congenital / early childhood**; developmental delays become apparent as speech and motor milestones are missed. Seizures, when present, can be infantile-onset ([PMID: 34617658](https://pubmed.ncbi.nlm.nih.gov/34617658/)).
- **Onset pattern:** insidious/developmental.
- **Progression:** the core neurodevelopmental phenotype is **stable / non-progressive** — a static developmental difference rather than a neurodegenerative process. Children typically make developmental progress with intervention.
- **Disease course / duration:** **chronic, lifelong** developmental disability of variable severity; lifespan is generally normal absent severe cardiac disease.
- **Critical periods:** the **early-childhood window** for speech/language and motor development is the key period for therapeutic intervention.

---

## 9. Inheritance and Population

- **Epidemiology:** **ultra-rare.** The literature comprises ~23 individuals with intragenic *DIP2C* variants plus scattered 10p15.3-deletion cases. True prevalence and incidence are **unknown**; no reliable per-100,000 estimate exists.
- **Inheritance pattern:** **autosomal dominant.** Both *de novo* and inherited (paternal and maternal) LoF variants occur.
- **Penetrance:** **incomplete** — mildly or subclinically affected transmitting parents are documented: *"Parental CMA analysis revealed that the 10p15.3 microdeletion was inherited from the father, who displayed mild language impairment"* ([PMID: 39696561](https://pubmed.ncbi.nlm.nih.gov/39696561/)).
- **Expressivity:** **variable** (from mild isolated speech delay to multisystem involvement with cardiac defects/seizures).
- **Genetic anticipation / repeat expansion:** not applicable.
- **Germline mosaicism / founder effects / consanguinity:** no established role; not an AR disorder, so consanguinity and carrier-frequency metrics are not applicable.
- **Population demographics:** no ethnic predilection established; cases reported across multiple populations (European, Chinese Han, others). **Sex ratio:** no predilection established. **Age distribution:** diagnosed in childhood.

---

## 10. Diagnostics

**Diagnosis is molecular/genomic.** There is **no specific biochemical biomarker or imaging signature.**

- **Chromosomal microarray (CMA):** first-line for detecting 10p15.3 microdeletions involving *DIP2C* ± *ZMYND11* — *"We describe 19 unrelated individuals with submicroscopic deletions involving 10p15.3 characterized by chromosomal microarray (CMA)"* ([PMID: 22847950](https://pubmed.ncbi.nlm.nih.gov/22847950/), also [PMID: 39696561](https://pubmed.ncbi.nlm.nih.gov/39696561/), [PMID: 30950019](https://pubmed.ncbi.nlm.nih.gov/30950019/)).
- **Exome / genome sequencing (WES/WGS):** detects intragenic SNVs/indels (nonsense, frameshift, splice, missense), used to delineate the cohort and identify the epilepsy-associated splice variant ([PMID: 38421105](https://pubmed.ncbi.nlm.nih.gov/38421105/), [PMID: 34617658](https://pubmed.ncbi.nlm.nih.gov/34617658/), [PMID: 38300321](https://pubmed.ncbi.nlm.nih.gov/38300321/)).
- **Prenatal testing:** CMA on amniocytes has detected 10p15.3 deletions prenatally ([PMID: 39696561](https://pubmed.ncbi.nlm.nih.gov/39696561/), [PMID: 40049822](https://pubmed.ncbi.nlm.nih.gov/40049822/), [PMID: 31542096](https://pubmed.ncbi.nlm.nih.gov/31542096/)); karyotyping/FISH characterize structural rearrangements (ring 10, inv dup del(10p)).
- **Functional confirmation:** minigene splice assays confirmed the pathogenic splice effect of c.1057+2T>G ([PMID: 34617658](https://pubmed.ncbi.nlm.nih.gov/34617658/)).
- **Adjunct evaluations:** brain MRI (variable anomalies), echocardiography (for cardiac defects), EEG (if seizures), developmental/speech assessment.

**Clinical criteria / differential diagnosis.** No formal consensus diagnostic criteria exist; diagnosis rests on a compatible neurodevelopmental phenotype plus a pathogenic *DIP2C* variant/deletion. Differential diagnosis includes other causes of childhood apraxia of speech / expressive language disorder and other contiguous-gene/neurodevelopmental syndromes; within 10p15.3 deletions, the overlapping contribution of *ZMYND11* must be considered.

**Screening.** No population newborn or carrier screening exists; cascade testing of relatives is appropriate once a familial variant is identified.

---

## 11. Outcome / Prognosis

- **Survival / life expectancy:** generally **normal lifespan**; the core speech/developmental phenotype is non-life-limiting. Prognosis may be modified by severity of congenital heart disease in the minority affected.
- **Morbidity / disability:** chronic developmental disability dominated by **communication impairment**, with variable cognitive, motor, and behavioral contributions. Many children improve with early intervention.
- **Complications:** seizures (subset), congenital heart defects (subset, ~4/23 in the intragenic cohort), feeding difficulties, and rare gastrointestinal dysmotility (gastroparesis) in deletion cases.
- **Recovery potential:** the disorder is static; targeted therapies (speech, OT/PT) improve function but do not cure the underlying developmental difference.
- **Prognostic factors:** extent of the genomic lesion (intragenic variant vs large deletion co-involving *ZMYND11*), presence of structural brain anomalies, cardiac defects, and seizures. No validated molecular prognostic biomarker exists.

---

## 12. Treatment

**No disease-specific or gene-targeted therapy exists.** A ClinicalTrials.gov search returned **0 studies** for "DIP2C" or "10p15.3 microdeletion." Management is **supportive and multidisciplinary**:

| Intervention | Purpose | Suggested NCIT concept |
|---|---|---|
| Speech-language therapy | Address core expressive speech/language delay | NCIT:C15376 (Speech Therapy) |
| Occupational / physical therapy | Motor delay, hypotonia, daily function | NCIT:C15277 (Physical Therapy); Occupational Therapy |
| Developmental / behavioral / educational support | Cognitive and behavioral needs, ASD traits | NCIT:C15312 (Supportive Care) |
| Antiseizure medication | For the seizure subset | NCIT:C264 (Anticonvulsant Agent) |
| Cardiac evaluation/management (echocardiography; surgery if indicated) | Congenital heart defects | NCIT:C49237 (Echocardiography) |
| Nutritional / GI management | Feeding difficulty, dysmotility | NCIT:C15431 (Nutritional Support) |

- **Pharmacotherapy / pharmacogenomics:** none specific.
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** none; all theoretical at present.
- **Treatment strategy:** individualized early-intervention program plus surveillance for cardiac and seizure complications.

---

## 13. Prevention

- **Primary prevention:** not applicable for a *de novo* genetic disorder beyond general preconception counseling.
- **Secondary prevention:** early developmental surveillance and prompt initiation of therapy to optimize outcomes.
- **Tertiary prevention:** cardiac and seizure surveillance to prevent complications.
- **Genetic counseling:** **key preventive measure.** Given autosomal-dominant inheritance with incomplete penetrance, counsel on up-to-50% recurrence risk when a parent carries the variant, the possibility of mildly affected carriers, and options including prenatal diagnosis and preimplantation genetic testing once a familial variant is known. Cascade testing of at-risk relatives is appropriate.
- **Immunization / public-health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *DIP2C* orthologs are broadly conserved and expressed in the developing nervous system from *Drosophila* to human. Orthologs: mouse *Dip2c* (mouse ortholog in MGI), zebrafish *dip2ca*, *C. elegans dip-2*, *Drosophila* DIP2, and yeast family members. DIP2 was studied as a conserved family *"using yeast, fly, and mouse models"* ([PMID: 35766356](https://pubmed.ncbi.nlm.nih.gov/35766356/)).
- **Natural disease in other species:** no naturally occurring companion-animal or wildlife disease is catalogued (no OMIA entry noted); the animal evidence is from engineered models (below).
- **Comparative biology / conservation:** the neurodevelopmental axon-branching role and the DAG-lipid-homeostasis function are **evolutionarily conserved** across yeast, fly, worm, zebrafish, and mouse ([PMID: 35766356](https://pubmed.ncbi.nlm.nih.gov/35766356/), [PMID: 27908785](https://pubmed.ncbi.nlm.nih.gov/27908785/)).
- **Transmission / zoonosis:** not applicable.

---

## 15. Model Organisms

| Model | Type | Key phenotype / finding | Reference |
|---|---|---|---|
| **Mouse** (het & homozygous *Dip2c* mutants) | Mammalian, genetic | Homozygotes: weight loss, hyperlocomotion, cognitive impairment, abnormal lipid metabolism; heterozygotes: mild cognitive impairment — **recapitulating the dosage-sensitive human phenotype**; cortical sphingolipid-metabolism upregulation with elevated oligodendrogenesis/myelination | [PMID: 41054236](https://pubmed.ncbi.nlm.nih.gov/41054236/) |
| **Mouse** (IMPC knockout) | Mammalian, genetic | 11 significant genotype–phenotype associations; homozygotes: incomplete-penetrance preweaning lethality (MP:0011110), enlarged adrenal glands (MP:0000642), germ-cell defect, abnormal sternum; heterozygotes: small thymus, enlarged bladder/lymph nodes, abnormal uterus, increased monocytes (p=1.5e-6). **No behavioral/neurological deficit reached significance in the primary screen** | IMPC (Finding F007) |
| **Mouse ES cells** | Cellular, genetic | CRISPR/Cas9 *Dip2c* knockout to study early embryo development | [PMID: 33813174](https://pubmed.ncbi.nlm.nih.gov/33813174/) |
| **Zebrafish** (*dip2ca* morpholino knockdown) | Vertebrate, induced | Decreased body length, craniofacial malformations, pericardial edema, linear heart tube, looping defects, arrhythmia; **rescued by wild-type *dip2ca*** — validates cardiac/craniofacial causality | [PMID: 40915331](https://pubmed.ncbi.nlm.nih.gov/40915331/) |
| ***Drosophila*** (DIP2 mutant/RNAi) | Invertebrate, genetic | Ectopic axonal bifurcation and guidance defects in mushroom-body α/β neurons; downstream effector **Glaikit** (phospholipase D superfamily) | [PMID: 27908785](https://pubmed.ncbi.nlm.nih.gov/27908785/), [PMID: 28465232](https://pubmed.ncbi.nlm.nih.gov/28465232/) |
| ***C. elegans*** (*dip-2*) | Invertebrate, genetic | Required for axon maintenance/regeneration; counterbalances de novo phospholipid (Kennedy pathway; CEPT-2/EPT-1) synthesis | [PMID: 39974891](https://pubmed.ncbi.nlm.nih.gov/39974891/) |
| **Yeast / fly / mouse** (DIP2 family) | Cross-species | DIP2 as conserved homeostatic regulator of a DAG subset; FAAL-like domains redirect DAG→triacylglycerol; mitochondria–vacuole contact-site localization | [PMID: 35766356](https://pubmed.ncbi.nlm.nih.gov/35766356/) |

**Phenotype recapitulation.** The **Chai et al. mouse** is the strongest model of the human disorder, reproducing dosage-sensitive cognitive impairment and providing the sphingolipid/myelination mechanism: *"Homozygous mutant mice exhibited weight loss, hyperlocomotion, cognitive impairment, and abnormal lipid metabolism, whereas heterozygous mutant mice displayed only mild cognitive impairment, recapitulating the dosage-sensitive phenotype observed in human 10p15.3 microdeletion syndrome"* ([PMID: 41054236](https://pubmed.ncbi.nlm.nih.gov/41054236/)). The **zebrafish** model validates the cardiac/craniofacial branch. Invertebrate models establish the conserved axon-development/lipid mechanism.
**Limitations.** The IMPC primary screen did not detect speech/cognitive-relevant neurobehavioral deficits; no model captures human expressive-speech phenotypes directly (an intrinsic cross-species limitation).

---

## Mechanistic Model / Interpretation

```
 Heterozygous DIP2C LoF variant OR 10p15.3 microdeletion (± ZMYND11)
                         │  (haploinsufficiency; gnomAD pLI≈1.0, LOEUF 0.149)
                         ▼
        ~50% loss of DIP2C (FAAL-like acyl-CoA/AMP-binding enzyme)
                         │
                         ▼
     Dysregulated homeostasis of a specific DIACYLGLYCEROL (DAG) pool
        ┌────────────────┼─────────────────────────────┐
        ▼                ▼                             ▼
  ↓ DAG→TAG flux     Dysregulated DAG→PKC        Imbalanced de novo
  (ER-stress risk)   signaling axis              phospholipid synthesis
        └────────────────┼─────────────────────────────┘
                         ▼
     Defective AXON bifurcation/guidance, axon maintenance
         + (mouse cortex) ↑ sphingolipid synthesis (↑SPT)
           → ↑ oligodendrogenesis / aberrant MYELINATION
                         │
         ┌───────────────┴────────────────┐
         ▼                                ▼
 Disrupted cortico-linguistic/        Parallel developmental branch:
 cognitive circuit maturation          cardiac + craniofacial
         ▼                                ▼
 EXPRESSIVE SPEECH/LANGUAGE DELAY,      Congenital heart defects,
 developmental delay, cognitive/        craniofacial dysmorphism
 behavioral differences, ± seizures     (zebrafish-validated)
```

The unifying interpretation is that **DIP2C is a dosage-sensitive lipid-metabolic enzyme**; halving its dose destabilizes a narrow DAG/phospholipid/sphingolipid homeostatic set-point that neurons (and developing cardiac/craniofacial tissue) depend on for correct axon wiring and myelination. Because expressive-language circuits appear especially sensitive, the most penetrant clinical signal is speech delay, while the remaining features reflect variable expressivity of the same lipid-developmental perturbation. Upstream = the mutation and lipid dysregulation; downstream = axon/myelination defects and the clinical phenotype. The human→animal mechanistic bridge (step 7) remains **inferred** rather than directly demonstrated in human neurons.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [38421105](https://pubmed.ncbi.nlm.nih.gov/38421105/) | *De novo variants predicting haploinsufficiency for DIP2C are associated with expressive speech delay* | **Defining cohort** (23 individuals); phenotype, variant spectrum, inheritance, cardiac defects, protein domains |
| [22847950](https://pubmed.ncbi.nlm.nih.gov/22847950/) | *Subtelomeric deletion of chromosome 10p15.3* | Establishes *DIP2C*/*ZMYND11* critical region; deletion-cohort phenotype frequencies; CMA diagnosis |
| [34818214](https://pubmed.ncbi.nlm.nih.gov/34818214/) | *Intragenic deletion of ZMYND11 in 10p15.3* | Supports haploinsufficiency mechanism and shared deletion phenotype |
| [39696561](https://pubmed.ncbi.nlm.nih.gov/39696561/) | *Prenatal diagnosis of pure 10p15.3 microdeletion* | Inheritance from a mildly affected parent → incomplete penetrance |
| [35766356](https://pubmed.ncbi.nlm.nih.gov/35766356/) | *DIP2 is a unique regulator of diacylglycerol lipid homeostasis* | Core enzymatic mechanism (DAG→TAG, FAAL-like domains, mito-vacuole sites) |
| [40327034](https://pubmed.ncbi.nlm.nih.gov/40327034/) | *Emergence of Dip2-mediated DAG-based PKC signalling* | DAG→PKC signaling axis |
| [39974891](https://pubmed.ncbi.nlm.nih.gov/39974891/) | *C. elegans DIP-2 / phospholipid synthesis* | Axon maintenance/regeneration via phospholipid balance |
| [27908785](https://pubmed.ncbi.nlm.nih.gov/27908785/) | *DIP2 regulates axonal bifurcation in Drosophila MB neurons* | Conserved axon-branching/guidance role; FAAL domains essential |
| [28465232](https://pubmed.ncbi.nlm.nih.gov/28465232/) | *Glaikit downstream of DIP2* | Downstream effector of DIP2 axon pathway |
| [41054236](https://pubmed.ncbi.nlm.nih.gov/41054236/) | *DIP2C deficiency leads to abnormal sphingolipid metabolism in mice* | Dosage-sensitive cognitive phenotype + sphingolipid/myelination mechanism |
| [40915331](https://pubmed.ncbi.nlm.nih.gov/40915331/) | *DIP2C deficiency and congenital heart defects* | Zebrafish-validated cardiac/craniofacial causality |
| [35987071](https://pubmed.ncbi.nlm.nih.gov/35987071/) | *DIP2C polymorphisms and ASD* | ASD susceptibility association |
| [34617658](https://pubmed.ncbi.nlm.nih.gov/34617658/) | *Novel DIP2C splice variant in focal infantile epilepsy* | Epilepsy phenotype; variant c.1057+2T>G |
| [33813174](https://pubmed.ncbi.nlm.nih.gov/33813174/) | *Knockout of Dip2c in murine ES cells* | ES-cell model resource |
| [30950019](https://pubmed.ncbi.nlm.nih.gov/30950019/) | *10p15.3 microdeletion by WES* | Deletion-case phenotype; diagnostic modality |
| [40049822](https://pubmed.ncbi.nlm.nih.gov/40049822/) | *r(10)/monosomy 10 mosaicism* | Structural-abnormality context; prenatal growth restriction |
| [31542096](https://pubmed.ncbi.nlm.nih.gov/31542096/) | *Inv dup del(10p)* | Structural-rearrangement context |

Beyond the core speech-delay phenotype, DIP2C is implicated across the neurodevelopmental continuum: *"Disco-interacting protein 2 C (DIP2C) has recently been reported as a new susceptibility gene for autism spectrum disorder (ASD) in a genome-wide association study"* ([PMID: 35987071](https://pubmed.ncbi.nlm.nih.gov/35987071/)), and in focal infantile epilepsy where *"The de novo variation (NM_014974.3: c.1057+2T>G) in DIP2C was uncovered through whole-exome sequencing"* ([PMID: 34617658](https://pubmed.ncbi.nlm.nih.gov/34617658/)).

**Evidence-type mix:** human clinical (cohorts/case reports), model organism (mouse, zebrafish, fly, worm, yeast), in vitro (minigene, ES cells), and computational (gnomAD constraint, Mendelian randomization). The human phenotype rests on **aggregated small cohorts**; the mechanism rests heavily on **model-organism and biochemical** data.

---

## Limitations and Knowledge Gaps

1. **Small sample size.** The entire human evidence base is ~23 intragenic cases plus scattered deletion reports — insufficient for robust penetrance, genotype–phenotype, or prevalence estimates.
2. **Contiguous-gene confound.** In 10p15.3 deletions, *ZMYND11* co-deletion contaminates phenotype attribution; only intragenic *DIP2C* variants cleanly isolate the *DIP2C* contribution.
3. **Human→mechanism gap.** The causal link from lipid/axon/myelination defects (animal data) to human expressive-speech delay is **inferred**, not demonstrated in human neurons or patient-derived cells.
4. **No biomarker.** There is no biochemical or imaging biomarker; no validated episignature despite the DMAP1-binding domain.
5. **Incomplete model coverage.** The IMPC primary screen did not surface neurobehavioral/speech-relevant deficits; no model captures the human language phenotype.
6. **Unknown epidemiology.** Prevalence, incidence, sex ratio, and ethnic/geographic distribution are undefined.
7. **No therapeutics.** Zero registered trials; no gene-targeted or lipid-pathway-directed therapy evaluated.

---

## Proposed Follow-up Experiments / Actions

1. **Expand the human cohort** via GeneMatcher/registries to refine penetrance, expressivity, genotype–phenotype correlation (LoF vs missense; intragenic vs deletion), and derive frequency estimates for each HPO feature.
2. **Patient-derived iPSC neurons/organoids** to test whether DIP2C haploinsufficiency perturbs DAG/sphingolipid pools, axon branching, and myelination in a human context — closing the human→mechanism gap.
3. **Targeted lipidomics** (DAG, TAG, phospholipid, sphingolipid species) in patient fibroblasts/plasma to search for a candidate biochemical biomarker and to test the serine-palmitoyltransferase/sphingolipid axis clinically.
4. **Conditional, brain-specific *Dip2c* mouse models** with language-relevant behavioral batteries (ultrasonic vocalization, learning) to better model the speech/cognitive phenotype absent from the IMPC screen.
5. **Systematic cardiac and EEG screening** across the cohort to quantify true frequencies of congenital heart defects and seizures and define surveillance guidelines.
6. **Mechanism-guided therapeutic exploration** — test whether modulating DAG→PKC signaling or sphingolipid biosynthesis (e.g., serine-palmitoyltransferase) rescues neurodevelopmental phenotypes in zebrafish/mouse models.
7. **Methylation/episignature study** leveraging the DMAP1-binding domain to determine whether *DIP2C* LoF produces a reproducible epigenetic classifier usable diagnostically.

---

*Report compiled from 10 confirmed findings and 17 reviewed papers across 5 investigation iterations. Evidence sources span human clinical cohorts, model organisms (mouse, zebrafish, Drosophila, C. elegans, yeast), in vitro systems, and computational constraint analysis.*


## Artifacts

- [OpenScientist final report](DIP2C-related_Developmental_Disorder_With_Speech_Delay-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](DIP2C-related_Developmental_Disorder_With_Speech_Delay-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 10 |
| Off topic | 3 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:35766356` (14 mentions) - DIP2 is a unique regulator of diacylglycerol lipid homeostasis in eukaryotes.
  - shared terms: model
- `PMID:40327034` (4 mentions) - Emergence of Dip2-mediated specific DAG-based PKC signalling axis in eukaryotes.
  - shared terms: none
- `PMID:28465232` (6 mentions) - Identification of glaikit in a genome-wide expression profiling for axonal bifurcation of the mushroom body in Drosophila.
  - shared terms: none

Weighed against this report's own most characteristic terms: `dip2c`, `speech`, `p15`, `deletion`, `cardiac`, `defect`, `phenotype`, `delay`, `variant`, `disorder`, `developmental`, `intragenic`, `language`, `novo`, `seizure`, `myelination`, `heart`, `microdeletion`, `human`, `model`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 23 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 12 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0700356` (2 mentions) - the report calls it "MONDO"; MONDO calls it **DIP2C-related developmental disorder with speech delay**
- `HP:0001263` (1 mention) - the report calls it "Common"; HP calls it **Global developmental delay**
- `HP:0001270` (1 mention) - the report calls it "10/10 (deletion cohort)"; HP calls it **Motor delay**
- `HP:0001999` (1 mention) - the report calls it "9/12 (deletion); minor/inconsistent (intragenic)"; HP calls it **Abnormal facial shape**
- `HP:0001252` (1 mention) - the report calls it "7/11 (deletion cohort)"; HP calls it **Hypotonia**
- `HP:0012443` (1 mention) - the report calls it "4/6 (deletion cohort)"; HP calls it **Abnormal brain morphology**
- `HP:0001250` (1 mention) - the report calls it "3/7 (deletion); focal infantile epilepsy reported"; HP calls it **Seizure**
- `NCIT:C15376` (1 mention) - the report calls it "Speech Therapy"; NCIT calls it **Transcendental Meditation Therapy**
- `NCIT:C15277` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Mastectomy**
- `NCIT:C15312` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Radiation Dosimetry**
- `NCIT:C49237` (1 mention) - the report calls it "Echocardiography"; NCIT calls it **Chemistry Test**
- `NCIT:C15431` (1 mention) - the report calls it "Nutritional Support"; NCIT calls it **Hematopoietic Cell Transplantation**