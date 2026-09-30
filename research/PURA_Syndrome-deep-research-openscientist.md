---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T01:14:20.852886'
end_time: '2026-09-30T01:29:09.504255'
duration_seconds: 888.65
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: PURA Syndrome
  mondo_id: MONDO:1060108
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
citation_count: 15
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 10
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 48
  verified: 45
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 28
  labels_matching: 15
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: HP:0011968
    reported_labels:
    - Very frequent
    ontology_label: Feeding difficulties
  - term_id: HP:0001250
    reported_labels:
    - Common
    ontology_label: Seizure
  - term_id: HP:0002072
    reported_labels:
    - dyskinesia
    ontology_label: Chorea
  - term_id: HP:0100585
    reported_labels:
    - hiccough
    ontology_label: Telangiectasia of the skin
  - term_id: HP:0002045
    reported_labels:
    - Frequent
    ontology_label: Hypothermia
  - term_id: HP:0001999
    reported_labels:
    - Frequent (more in deletion carriers)
    ontology_label: Abnormal facial shape
  - term_id: HP:0001627
    reported_labels:
    - Less common
    ontology_label: Abnormal heart morphology
  - term_id: HP:0000119
    reported_labels:
    - Less common
    ontology_label: Abnormality of the genitourinary system
  - term_id: HP:0000478
    reported_labels:
    - Less common
    ontology_label: Abnormality of the eye
  - term_id: HP:0000924
    reported_labels:
    - Less common
    ontology_label: Abnormality of the skeletal system
  - term_id: HP:0000818
    reported_labels:
    - Less common
    ontology_label: Abnormality of the endocrine system
  labels_variant: 2
  obsolete_terms:
  - term_id: HP:0100786
    ontology_label: obsolete Hypersomnia
    replaced_by: HP:0001262
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PURA_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PURA_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PURA Syndrome
- **MONDO ID:** MONDO:1060108 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PURA Syndrome** covering all of the
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

# PURA Syndrome: Comprehensive Disease Characteristics Report

**Disease:** PURA Syndrome (PURA-related neurodevelopmental disorder)
**Identifiers:** MONDO:0014601 · OMIM #616158 · Orphanet ORPHA:438213 · Gene: *PURA* (HGNC:9701), 5q31.3
**Category:** Mendelian, autosomal dominant, de novo

---

## Summary

PURA syndrome is a rare, highly penetrant, autosomal dominant neurodevelopmental disorder caused by **de novo heterozygous loss-of-function or protein-misfolding variants in *PURA***, the gene at chromosome 5q31.3 encoding the DNA/RNA-binding protein **Pur-alpha (Purα)**. The disorder was defined in 2014 when two independent whole-exome trio studies established that de novo *PURA* variants recapitulate the severe neurological phenotype previously attributed to the larger 5q31.3 microdeletion syndrome, identifying *PURA* as the phenocritical gene ([PMID: 25439098](https://pubmed.ncbi.nlm.nih.gov/25439098/); [PMID: 25342064](https://pubmed.ncbi.nlm.nih.gov/25342064/)). Pur-alpha is essential for postnatal neuronal proliferation, developmentally-timed dendrite formation, and the dendritic transport and local translation of mRNA; haploinsufficiency of this function disrupts brain development and produces the clinical syndrome.

The core clinical picture is one of a **multisystem disorder dominated by neurological features**: profound neonatal hypotonia, early feeding difficulties, global developmental delay progressing to moderate-to-severe intellectual disability with **near-universal absence of speech**, frequent non-ambulation, seizures and abnormal non-epileptic movements, hypersomnolence, and neonatal problems including excessive hiccups, recurrent apnea, and hypothermia. Less common but well-documented manifestations include congenital heart defects, urogenital malformations, and skeletal, ophthalmological, gastrointestinal, and endocrine anomalies ([PMID: 33275834](https://pubmed.ncbi.nlm.nih.gov/33275834/)). As of 2024, approximately **650 patients worldwide** had been reported ([PMID: 38655849](https://pubmed.ncbi.nlm.nih.gov/38655849/)).

Diagnosis is molecular — via whole-exome/genome sequencing, targeted *PURA* sequencing (the syndrome is clinically recognizable), or chromosomal microarray for 5q31.3 deletions. There is **no reliable genotype-phenotype correlation** and **no disease-modifying therapy**; management is lifelong, supportive, and multidisciplinary. Recurrence risk to siblings is low (~1%), attributable to possible parental germline mosaicism. The main life-limiting risk is respiratory complication, which caused death in the oldest reported patient at age 26 ([PMID: 26582469](https://pubmed.ncbi.nlm.nih.gov/26582469/)).

---

## 1. Disease Information

**Overview.** PURA syndrome is a Mendelian neurodevelopmental disorder characterized by moderate-to-severe developmental delay/intellectual disability, neonatal hypotonia, feeding difficulties, hypersomnolence, seizures or seizure-like movements, and a range of multisystem anomalies. It was first delineated as a distinct entity in 2014 and represents the phenocritical core of the previously described 5q31.3 microdeletion syndrome.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014601 (PURA-related severe neurodevelopmental disorder). Note: the template-supplied MONDO:1060108 is not the current primary ID. |
| OMIM | #616158 (Neurodevelopmental disorder with neonatal respiratory insufficiency, hypotonia, and feeding difficulties, NEDRIHF) |
| Orphanet | ORPHA:438213 |
| Gene | *PURA*, HGNC:9701, NCBI Gene 5813, UniProt Q00577 |
| Locus | 5q31.3 |
| ICD-10 / ICD-11 | No specific code; maps under developmental anomaly / G-code categories |

**Synonyms / alternative names.** PURA-related neurodevelopmental disorder; PURA-related severe neurodevelopmental disorder with neonatal respiratory insufficiency, hypotonia, and feeding difficulties (NEDRIHF); Pur-alpha syndrome; the phenocritical core of "5q31.3 microdeletion syndrome."

**Information source.** The disease-level knowledge is derived from **aggregated case series and cohort studies** (parent-child trio exome studies, multi-center clinical cohorts of 25–32 individuals, and international reviews), not from individual EHR mining. Patient registries maintained by the PURA Syndrome Foundation support ongoing aggregation.

---

## 2. Etiology

**Primary cause — genetic.** PURA syndrome is caused by **de novo heterozygous loss-of-function variants in *PURA***, or by deletions of 5q31.3 that encompass *PURA*. Two independent 2014 whole-exome trio studies established causation:

- Lalani et al. described **11 individuals** with clinical features of 5q31.3 microdeletion syndrome carrying de novo *PURA* mutations within the critical region, concluding: *"We describe 11 individuals with clinical features of 5q31.3 microdeletion syndrome and de novo mutations in PURA, encoding transcriptional activator protein Pur-α, within the critical region. These data implicate causative PURA mutations responsible for the severe neurological phenotypes observed in this syndrome"* ([PMID: 25439098](https://pubmed.ncbi.nlm.nih.gov/25439098/)).
- Hunt et al. (Deciphering Developmental Disorders study) identified **protein-altering de novo mutations in four trios**: *"Protein-altering de novo mutations in PURA were identified in four subjects. They include two different frameshifts, one inframe deletion and one missense mutation"* ([PMID: 25342064](https://pubmed.ncbi.nlm.nih.gov/25342064/)).

That *PURA* point mutations recapitulate the severe neurological phenotype of the larger 5q31.3 microdeletion confirms *PURA* as the phenocritical gene: *"The recent finding that de novo PURA point mutations are indeed sufficient to cause the severe neurological symptoms also observed in patients with 5q31.2q31.3 deletion further reinforces the gene's causative role in 5q31.3 microdeletion syndrome"* ([PMID: 26582469](https://pubmed.ncbi.nlm.nih.gov/26582469/)).

**Genetic risk factors.** The causal variant is essentially the sole determinant. Variants are almost always de novo (arising in the affected individual, not inherited). No susceptibility loci or established modifier genes have been identified. Disruption of Pur repeat III has been proposed to worsen outcome, but no robust modifier has been validated ([PMID: 25342064](https://pubmed.ncbi.nlm.nih.gov/25342064/)).

**Environmental risk factors.** None identified. Because variants are predominantly de novo, advanced parental age is a general (nonspecific) contributor to de novo mutation rate, but no specific environmental exposure, toxin, or lifestyle factor has been linked to PURA syndrome.

**Protective factors.** None identified (genetic or environmental).

**Gene-environment interactions.** None documented. PURA syndrome is a monogenic disorder with high penetrance; the phenotype is driven by the genetic lesion rather than gene-environment interaction.

---

## 3. Phenotypes

PURA syndrome is a multisystem disorder with a strong neurological predominance. Phenotype frequencies are drawn primarily from the 25-patient Chinese cohort ([PMID: 36376392](https://pubmed.ncbi.nlm.nih.gov/36376392/)), the 32-individual delineation ([PMID: 29097605](https://pubmed.ncbi.nlm.nih.gov/29097605/)), and the international review ([PMID: 33275834](https://pubmed.ncbi.nlm.nih.gov/33275834/)).

| Phenotype | Type | Onset | Frequency | Suggested HPO term |
|---|---|---|---|---|
| Global developmental delay / intellectual disability | Neurodevelopmental | Infancy | ~Universal (moderate–severe) | HP:0001263 / HP:0001249 |
| Neonatal hypotonia | Clinical sign | Neonatal | Very frequent (near-universal) | HP:0001319 / HP:0001252 |
| Absent/severely limited speech | Neurodevelopmental | Childhood | Nearly all patients | HP:0001344 (absent speech) |
| Feeding difficulties | Clinical sign | Neonatal | Very frequent | HP:0011968 |
| Seizures / seizure-like movements | Neurological | Neonatal–childhood | Common | HP:0001250 |
| Abnormal non-epileptic movements | Neurological | Early | Common | HP:0002072 (dyskinesia) |
| Hypersomnolence / excessive sleepiness | Behavioral/neuro | Neonatal–infancy | Prominent | HP:0002360 / HP:0100786 |
| Excessive hiccups | Clinical sign | Neonatal | Characteristic early sign | HP:0100585 (hiccough) |
| Recurrent apnea | Clinical sign | Neonatal | Frequent | HP:0002104 (apnea) |
| Hypothermia / temperature dysregulation | Clinical sign | Neonatal | Frequent | HP:0002045 |
| Non-ambulation / motor impairment | Physical | Childhood | Many | HP:0002505 (inability to walk) |
| Dysmorphic facial features | Physical | Congenital | Frequent (more in deletion carriers) | HP:0001999 |
| Congenital heart defects | Physical malformation | Congenital | Less common | HP:0001627 |
| Urogenital malformations | Physical malformation | Congenital | Less common | HP:0000119 |
| Ophthalmological anomalies | Physical | Variable | Less common | HP:0000478 |
| Skeletal anomalies | Physical | Variable | Less common | HP:0000924 |
| Endocrine anomalies (e.g., pituitary dysregulation, pubertal delay) | Laboratory/clinical | Variable | Less common | HP:0000818 |

**Characteristics.** Onset is overwhelmingly **neonatal to early infantile**. Severity is **moderate to severe** and variable. The course is chronic and largely **stable/non-progressive** in most, though at least one patient with a *PURA*-encompassing deletion showed adolescent-onset neurological deterioration, pubertal delay/primary amenorrhea, and progressive respiratory decline leading to death at 26 ([PMID: 26582469](https://pubmed.ncbi.nlm.nih.gov/26582469/)).

Key supporting quotes:
- *"Developmental delay/intellectual disability, neonatal hypotonia, neonatal feeding difficulties, hypersomnolence and dysmorphic features were prominent clinical features in PURA syndrome"* ([PMID: 36376392](https://pubmed.ncbi.nlm.nih.gov/36376392/)).
- *"moderate to severe neurodevelopmental delay with absence of speech in nearly all patients and lack of independent ambulation in many. Early-onset problems include excessive hiccups, hypotonia, hypersomnolence, hypothermia, feeding difficulties, recurrent apneas, epileptic seizures, and abnormal nonepileptic movements. Other less common manifestations comprise congenital heart defects, urogenital malformations, and various skeletal, ophthalmological, gastrointestinal, and endocrine anomalies"* ([PMID: 33275834](https://pubmed.ncbi.nlm.nih.gov/33275834/)).
- *"Neonatal hypotonia, early feeding difficulties and seizures, or 'seizure-like' movements, were also common"* ([PMID: 25342064](https://pubmed.ncbi.nlm.nih.gov/25342064/)).

**Quality of life impact.** Profound. Most patients are non-verbal and many are non-ambulatory, requiring lifelong caregiving, augmentative communication, feeding support, and management of seizures and sleep. Daily functioning is severely affected across communication, mobility, and self-care domains.

---

## 4. Genetic / Molecular Information

**Causal gene.** *PURA* (HGNC:9701; UniProt Q00577), a single-exon gene at 5q31.3 encoding Pur-alpha, a purine-rich element binding protein composed of repeated PUR domains.

**Pathogenic variants.**
- **Variant types:** frameshift (e.g., c.159dup p.(Leu54Alafs*147)), in-frame deletions (recurrent **c.697_699del p.(Phe233del)**), nonsense, missense, and whole-gene deletions (5q31.3 microdeletion). Both initial trios and later cohorts show a spectrum consistent with loss of function ([PMID: 25342064](https://pubmed.ncbi.nlm.nih.gov/25342064/); [PMID: 36376392](https://pubmed.ncbi.nlm.nih.gov/36376392/)).
- **Classification (ACMG/AMP):** the vast majority are pathogenic/likely pathogenic. As of 2021, **64 different pathogenic variants across 78 individuals** were reported ([PMID: 33275834](https://pubmed.ncbi.nlm.nih.gov/33275834/)).
- **Recurrent variants:** c.697_699del p.(Phe233del) and c.159dup p.(Leu54Alafs*147) ([PMID: 36376392](https://pubmed.ncbi.nlm.nih.gov/36376392/); [PMID: 37204304](https://pubmed.ncbi.nlm.nih.gov/37204304/)).
- **Allele frequency:** essentially absent from population databases (gnomAD) — consistent with de novo, highly penetrant, severe disease.
- **Origin:** germline, de novo. Somatic/mosaic events are rare but relevant to recurrence risk.
- **Functional consequence:** **loss of function / haploinsufficiency**. PURA-syndrome mutations impair the protein's 3D folding, disrupt RNA binding, and cause failure of PURA to localize to P-bodies ([PMID: 38655849](https://pubmed.ncbi.nlm.nih.gov/38655849/)).

**Modifier genes.** None validated. Disruption of Pur repeat III has been proposed to worsen outcome ([PMID: 25342064](https://pubmed.ncbi.nlm.nih.gov/25342064/)), but no reliable genotype-phenotype correlation exists ([PMID: 37204304](https://pubmed.ncbi.nlm.nih.gov/37204304/); [PMID: 29097605](https://pubmed.ncbi.nlm.nih.gov/29097605/)).

**Epigenetic information.** No disease-specific DNA-methylation episignature has been established for PURA syndrome to date (not available).

**Chromosomal abnormalities.** The 5q31.3 (5q31.2q31.3) microdeletion encompassing *PURA* produces a phenotype overlapping point-mutation cases; the smallest reported de novo deletion involving *PURA* helped confirm the gene's centrality ([PMID: 26582469](https://pubmed.ncbi.nlm.nih.gov/26582469/); [PMID: 25439098](https://pubmed.ncbi.nlm.nih.gov/25439098/)).

---

## 5. Environmental Information

- **Environmental factors:** None known to cause or modify PURA syndrome. It is a monogenic de novo disorder.
- **Lifestyle factors:** Not applicable.
- **Infectious agents:** Not applicable. (Of note, host Pur-alpha is exploited by certain viruses — HIV-1, JC virus — and a baculovirus encodes a PURα-like protein VP1054 [[PMID: 23720732](https://pubmed.ncbi.nlm.nih.gov/23720732/)] — but these are not causes of PURA syndrome.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **de novo heterozygous loss-of-function variant** (frameshift, nonsense, in-frame deletion, missense) or a **5q31.3 deletion** occurs in *PURA* → **leads to** reduced dosage and/or misfolded Pur-alpha protein (haploinsufficiency).
2. Mutations **impair the 3D folding of the PUR domains** → **result in** loss of the PC4-like β-β-β-β-α fold that mediates single-stranded DNA/RNA binding and duplex unwinding ([PMID: 38655849](https://pubmed.ncbi.nlm.nih.gov/38655849/); [PMID: 26744780](https://pubmed.ncbi.nlm.nih.gov/26744780/); [PMID: 32476604](https://pubmed.ncbi.nlm.nih.gov/32476604/)).
3. Misfolding **disrupts Pur-alpha's nucleic-acid binding** → **causes** failure of Pur-alpha to associate with P-bodies and RNP granules ([PMID: 38655849](https://pubmed.ncbi.nlm.nih.gov/38655849/)).
4. Loss of RNP/P-body function → **impairs** dendritic mRNA transport and local translation (Pur-alpha normally operates with **Staufen, FMRP, and BC1/BC200 non-coding RNA** at dendritic translation sites) ([PMID: 16511857](https://pubmed.ncbi.nlm.nih.gov/16511857/)).
5. Disrupted mRNA localization and translation → **impairs** developmentally-timed **dendrite formation** and **postnatal neuronal proliferation** (inferred from mouse loss-of-function models) ([PMID: 16511857](https://pubmed.ncbi.nlm.nih.gov/16511857/); [PMID: 22010047](https://pubmed.ncbi.nlm.nih.gov/22010047/)).
6. Abnormal neuronal proliferation and dendritic maturation → **result in** reduced neuron numbers and dendritic deficits (demonstrated in Purα +/− mice: reduced neurons in cerebellar vermis and hippocampal CA1–3) ([PMID: 27651147](https://pubmed.ncbi.nlm.nih.gov/27651147/)).
7. Structural/functional CNS deficits → **manifest as** neonatal hypotonia, feeding difficulties, developmental delay/intellectual disability, absent speech, seizures, movement abnormalities, hypersomnolence, and brainstem-related dysregulation (apnea, hypothermia, hiccups) ([PMID: 33275834](https://pubmed.ncbi.nlm.nih.gov/33275834/); [PMID: 25342064](https://pubmed.ncbi.nlm.nih.gov/25342064/)).

**Branch:** Pur-alpha also binds guanine-rich/G-quadruplex nucleic-acid elements; loss of this activity is a candidate contributor to translational dysregulation (mechanistically related to Pur biology in C9orf72 ALS/FTD, where increased Purα is protective) ([PMID: 32035967](https://pubmed.ncbi.nlm.nih.gov/32035967/)). Its relevance to PURA syndrome specifically is **inferred, not demonstrated**.

### Detail by category

**Molecular pathways / protein function.** Pur-alpha is a repeated **PUR-domain** protein; each ~60–80 aa domain adopts a PC4-like fold that binds ssDNA/RNA and can unwind duplex nucleic acids. The crystal structure of the DNA-/RNA-binding domain in complex with ssDNA *"reveals base-specific recognition and offers a molecular explanation for the effect of point mutations in the 5q31.3 microdeletion syndrome"* and identified a highly conserved phenylalanine essential for unwindase activity ([PMID: 26744780](https://pubmed.ncbi.nlm.nih.gov/26744780/)). The domain family is described in [PMID: 32476604](https://pubmed.ncbi.nlm.nih.gov/32476604/).

**Cellular processes.** Neuronal precursor proliferation, dendrite formation, and mRNA transport/local translation. *"the protein Purα ... is essential for neuronal proliferation, dendritic maturation, and the transportation of mRNA to translation sites"* ([PMID: 37204304](https://pubmed.ncbi.nlm.nih.gov/37204304/)).

**Protein dysfunction.** *"the mutations impair the protein's folding and thereby disrupt PURA's ability to bind RNA"* and *"in cells carrying PURA syndrome mutations, PURA failed to move adequately to P-bodies"* ([PMID: 38655849](https://pubmed.ncbi.nlm.nih.gov/38655849/)). This is a loss-of-function mechanism via misfolding.

**Dendritic mRNA transport machinery.** *"Pur alpha and Staufen are colocalized at dendritic sites of mRNA translation,"* and *"double-RNA immunoprecipitation places Pur alpha together with Staufen or FMRP on BC1 RNA and specific mRNA species in vivo"* ([PMID: 16511857](https://pubmed.ncbi.nlm.nih.gov/16511857/)). Microtubule disruption mislocalizes Pur-alpha to axons, indicating microtubule-dependent dendritic targeting.

**Suggested GO / CL terms.**
- Biological processes: GO:0016358 (dendrite development), GO:0050767 (regulation of neurogenesis), GO:0006417 (regulation of translation), GO:0008298 (intracellular mRNA localization), GO:0006355 (regulation of DNA-templated transcription).
- Molecular function: GO:0003697 (single-stranded DNA binding), GO:0003727 (single-stranded RNA binding).
- Cellular components: GO:0000932 (P-body), GO:0030425 (dendrite), GO:0005634 (nucleus).
- Cell types: CL:0000540 (neuron), CL:0000121 (cerebellar/Purkinje neuron), CL:0002608 (hippocampal neuron), CL:0011020 (neural progenitor cell).

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary:** Brain / central nervous system (UBERON:0000955 brain; UBERON:0002037 cerebellum; UBERON:0002421 hippocampal formation; brainstem UBERON:0002298).
- **Secondary / less common:** heart (congenital defects, UBERON:0000948), urogenital system (UBERON:0000990), skeleton (UBERON:0004288), eye (UBERON:0000970), gastrointestinal tract (UBERON:0001555), endocrine system including pituitary (UBERON:0000007).
- **Body systems:** nervous (predominant), musculoskeletal (hypotonia), respiratory (apnea, later restrictive decline), autonomic/thermoregulatory (hypothermia), endocrine.

**Tissue and cell level.** Nervous tissue is centrally affected. Cerebellar vermis neurons and hippocampal pyramidal neurons (CA1–CA3) show reduced numbers in the heterozygous mouse model ([PMID: 27651147](https://pubmed.ncbi.nlm.nih.gov/27651147/)). Cell Ontology: CL:0000540 (neuron), CL:0000121 (Purkinje/cerebellar neuron), CL:0002608 (hippocampal neuron), CL:0011020 (neural progenitor cell).

**Subcellular level.** Dendrites (GO:0030425), cytoplasmic P-bodies / mRNP granules (GO:0000932), and the nucleus (GO:0005634). Pur-alpha is specifically located in dendrites colocalized with MAP2 — not in axons ([PMID: 16511857](https://pubmed.ncbi.nlm.nih.gov/16511857/)).

**Localization / lateralization.** CNS involvement is bilateral and generalized. Brain MRI abnormalities are more common in 5q31.3-deletion carriers than in point-mutation patients ([PMID: 36376392](https://pubmed.ncbi.nlm.nih.gov/36376392/)); findings can include nonspecific white-matter and delayed-myelination changes.

---

## 8. Temporal Development

- **Onset:** Congenital / neonatal. Hypotonia, feeding difficulty, hiccups, apnea, hypothermia, and hypersomnolence present in the newborn period; developmental delay becomes apparent in infancy.
- **Onset pattern:** Chronic/insidious in most; the disorder is present from birth.
- **Progression:** Largely **stable/non-progressive** neurodevelopmental disability across most patients — delay is fixed rather than regressive. However, long-term follow-up documented **adolescent-onset deterioration** with pubertal delay/primary amenorrhea and progressive respiratory decline in a deletion patient, indicating that a progressive course can occur in some ([PMID: 26582469](https://pubmed.ncbi.nlm.nih.gov/26582469/)).
- **Disease course pattern:** Chronic, lifelong. Seizures may be episodic. Neonatal features (hiccups, apnea, hypothermia, hypersomnolence) tend to attenuate over the first months to years while cognitive/motor disability persists.
- **Duration:** Lifelong.
- **Critical periods:** The postnatal window of neuronal proliferation and dendritic maturation is the biologically critical period; this is when Pur-alpha function is most essential (inferred from mouse developmental phenotypes, [PMID: 22010047](https://pubmed.ncbi.nlm.nih.gov/22010047/); [PMID: 16511857](https://pubmed.ncbi.nlm.nih.gov/16511857/)).

---

## 9. Inheritance and Population

**Epidemiology.** No formal prevalence/incidence has been established. Reported patient numbers grew from **4 (2014)** → **32** ([PMID: 29097605](https://pubmed.ncbi.nlm.nih.gov/29097605/)) → **78 with 64 variants (2021)** ([PMID: 33275834](https://pubmed.ncbi.nlm.nih.gov/33275834/)) → **~650 worldwide (2024)** ([PMID: 38655849](https://pubmed.ncbi.nlm.nih.gov/38655849/)). *"PURA syndrome is a neurodevelopmental disorder that affects about 650 patients worldwide"* ([PMID: 38655849](https://pubmed.ncbi.nlm.nih.gov/38655849/)). PURA syndrome is a recognized contributor to unexplained neonatal hypotonia and early-onset developmental delay.

**Genetic etiology parameters.**
- **Inheritance:** Autosomal dominant, almost always de novo.
- **Penetrance:** High / near-complete — nearly every reported mutation causes symptoms ([PMID: 38655849](https://pubmed.ncbi.nlm.nih.gov/38655849/)).
- **Expressivity:** Variable, wide-ranging clinical spectrum ([PMID: 37204304](https://pubmed.ncbi.nlm.nih.gov/37204304/)).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Possible; underlies the low (~1%) sibling recurrence risk.
- **Founder effects / consanguinity:** Not applicable (de novo dominant).
- **Carrier frequency:** Not applicable.

**Population demographics.** No ethnic predilection; cases reported worldwide (Europe, North America, China, and elsewhere). No strong sex bias is established. Age distribution reflects pediatric ascertainment, though affected individuals survive into adulthood.

---

## 10. Diagnostics

**Recommended approach.** Molecular genetic testing is the diagnostic cornerstone. The original disease-defining diagnoses were made by **whole-exome sequencing of parent-child trios** ([PMID: 25342064](https://pubmed.ncbi.nlm.nih.gov/25342064/); [PMID: 25439098](https://pubmed.ncbi.nlm.nih.gov/25439098/)).

- **WES / WGS:** High-yield first-line for undiagnosed neonatal hypotonia + developmental delay; trio analysis identifies de novo status.
- **Gene panels:** Intellectual disability / epilepsy / hypotonia NGS panels that include *PURA*.
- **Single-gene / targeted Sanger sequencing:** Feasible because the syndrome is **clinically recognizable** — *"The identification of one individual through targeted Sanger sequencing points towards the clinical recognisability of the syndrome"* ([PMID: 29097605](https://pubmed.ncbi.nlm.nih.gov/29097605/)).
- **Chromosomal microarray (CMA):** Detects 5q31.3 (5q31.2q31.3) deletions encompassing *PURA* ([PMID: 25439098](https://pubmed.ncbi.nlm.nih.gov/25439098/); [PMID: 26582469](https://pubmed.ncbi.nlm.nih.gov/26582469/)).
- Karyotyping/FISH: lower yield; CMA preferred for copy-number detection. Mitochondrial DNA and repeat-expansion testing: not applicable.

**Variant interpretation.** Reijnders et al. classified mutations using **3D in silico crystal-structure models** and performed computational facial-photograph analysis; genotype-phenotype analysis showed *"no significant correlation between mutation classes and disease severity"* ([PMID: 29097605](https://pubmed.ncbi.nlm.nih.gov/29097605/)).

**Clinical / ancillary tests.** EEG (for seizures/seizure-like movements), brain MRI (often normal in point-mutation cases; more frequently abnormal in deletion carriers, [PMID: 36376392](https://pubmed.ncbi.nlm.nih.gov/36376392/)), swallow/feeding assessment, sleep and respiratory evaluation, echocardiography and renal/urogenital imaging when malformations are suspected, and endocrine workup (suspected anterior pituitary dysregulation, [PMID: 25342064](https://pubmed.ncbi.nlm.nih.gov/25342064/)).

**Biomarkers.** No specific circulating biomarker or metabolic signature; diagnosis is genetic. No methylation episignature established.

**Differential diagnosis.** Prader-Willi syndrome (neonatal hypotonia, feeding difficulty, hypersomnolence), Angelman syndrome, other genetic hypotonia/developmental-encephalopathy syndromes (e.g., *MECP2*, *FOXG1*, *TCF4*), congenital myopathies, and 5q31.3 microdeletion syndrome itself. The combination of neonatal hypotonia, hypersomnolence, excessive hiccups, and feeding difficulty is characteristic.

**Screening.** No newborn or carrier screening exists (de novo dominant disorder). Cascade testing of parents is generally uninformative for recurrence beyond germline-mosaicism counseling.

---

## 11. Outcome / Prognosis

- **Survival / life expectancy:** Many patients survive into adulthood; the oldest reported patient died at **age 26** from progressive respiratory failure ([PMID: 26582469](https://pubmed.ncbi.nlm.nih.gov/26582469/)). No formal survival curves exist given rarity.
- **Mortality:** Main life-limiting risk is **respiratory complication**: *"her respiratory problems increased and eventually became severe enough to cause her death"* ([PMID: 26582469](https://pubmed.ncbi.nlm.nih.gov/26582469/)). Neonatal apnea is a serious early risk.
- **Morbidity / disability:** Severe and lifelong. Most patients are **non-verbal**; many are **non-ambulatory**. Intellectual disability is moderate-to-severe.
- **Complications:** Seizures, aspiration/feeding failure (may require gastrostomy), recurrent apnea, orthopedic sequelae of hypotonia (scoliosis, hip issues), and organ-specific complications from congenital anomalies.
- **Recovery potential:** No recovery of core neurodevelopmental deficit; supportive care improves function and comfort. Some neonatal features (hiccups, apnea, hypothermia) attenuate with age.
- **Prognostic factors:** No validated molecular prognostic biomarker. Notably, **no genotype-phenotype correlation** guides prognosis ([PMID: 29097605](https://pubmed.ncbi.nlm.nih.gov/29097605/); [PMID: 37204304](https://pubmed.ncbi.nlm.nih.gov/37204304/)). Respiratory status is the most important clinical prognostic determinant.

---

## 12. Treatment

**There is no disease-modifying or curative therapy.** Management is entirely **supportive, symptomatic, and multidisciplinary**.

**Pharmacotherapy (symptomatic).**
- Anti-seizure medications for epilepsy (NCIT: Anticonvulsant Agent). Choice individualized; no PURA-specific regimen.
- Management of movement disorders and sleep as needed.
- No pharmacogenomic guidance specific to PURA syndrome.

**Advanced therapeutics.** No approved gene therapy, cell therapy, RNA-based therapy, or targeted therapy. Given the loss-of-function/haploinsufficiency mechanism and the essential dosage-sensitive role of Pur-alpha, **dosage-restoration strategies (gene supplementation, ASO-mediated upregulation)** are conceptually plausible future directions but remain preclinical/experimental (inferred).

**Surgical / interventional.** Gastrostomy for severe feeding difficulty (NCIT: Gastrostomy); corrective surgery for congenital heart or urogenital malformations; orthopedic intervention for scoliosis/hip.

**Supportive and rehabilitative (core of care).**
- Feeding support: thickened feeds, NG/gastrostomy (NCIT: Nutritional Support).
- Physical therapy for hypotonia/motor delay (NCIT: Physical Therapy).
- Occupational therapy (NCIT: Occupational Therapy).
- Speech therapy and **augmentative and alternative communication (AAC)** given near-universal absent speech (NCIT: Speech Therapy).
- Respiratory monitoring/support (apnea management, ventilatory support as needed).
- Sleep management for hypersomnolence.

**Experimental treatments / clinical trials.** No PURA-specific interventional trials with reported efficacy identified. Natural-history data collection and registries (PURA Syndrome Foundation) support future trial readiness.

**Treatment strategy.** Individualized, symptom-directed, delivered by a multidisciplinary team (neurology, genetics, gastroenterology, pulmonology, cardiology, PT/OT/speech, developmental pediatrics).

---

## 13. Prevention

- **Primary prevention:** Not possible — the disorder arises de novo. General reproductive-health measures do not prevent de novo mutation.
- **Secondary prevention:** Early molecular diagnosis enables early intervention (feeding support, apnea monitoring, developmental therapy, seizure management) that reduces morbidity.
- **Tertiary prevention:** Proactive management of complications — aspiration prevention, respiratory surveillance, seizure control, orthopedic monitoring.
- **Immunization / public health / environmental interventions:** Not applicable.
- **Genetic counseling:** Central. Explain de novo origin, **low (~1%) sibling recurrence risk** due to possible parental germline mosaicism, and reproductive options including **prenatal diagnosis and preimplantation genetic testing (PGT-M)** for a known familial variant.
- **Screening:** No population newborn or carrier screening (de novo dominant).

---

## 14. Other Species / Natural Disease

- **Orthologous gene:** Mouse *Pura* (NCBI Gene 19290); highly conserved across vertebrates. Pur-alpha is an evolutionarily conserved guanine-rich polynucleotide-binding protein; PC4-like PUR domains occur throughout all kingdoms of life ([PMID: 32476604](https://pubmed.ncbi.nlm.nih.gov/32476604/)).
- **Natural disease in other species:** No naturally occurring companion-animal or wildlife equivalent of PURA syndrome is documented (not identified in OMIA to date).
- **Comparative biology:** Disease mechanisms are studied via engineered models (below). Pur-alpha biology is deeply conserved; a baculovirus has acquired a functional PURα-like protein (VP1054) that binds GGN repeats, illustrating conservation of Pur nucleic-acid-binding function ([PMID: 23720732](https://pubmed.ncbi.nlm.nih.gov/23720732/)).
- **Transmission / zoonotic potential:** Not applicable (genetic disorder).

---

## 15. Model Organisms

**Mouse models** are the principal system and recapitulate key features.

| Model | Key phenotype | Human-relevant recapitulation | Reference |
|---|---|---|---|
| *Pura* heterozygous (+/−) | Decreased escape response to touch, limb/abdominal hypotonia, gait ataxia (wider steps, missteps), memory deficits (Barnes maze, novel object location), reduced neuron numbers in cerebellar vermis and hippocampal CA1–3 | Models hypotonia, motor deficits, cognitive impairment, neuronal loss — the best dosage-matched model of human haploinsufficiency | [PMID: 27651147](https://pubmed.ncbi.nlm.nih.gov/27651147/) |
| *Pura* null (−/−) | Born normal, then tremor at ~2 weeks, megalencephaly, axonal swellings, neurofilament hyperphosphorylation, prolonged postnatal proliferation of neuronal precursors (hippocampus, cerebellum), altered MAP2; some lines die postnatally | Models developmental/proliferation mechanism; more severe than human heterozygous state | [PMID: 22010047](https://pubmed.ncbi.nlm.nih.gov/22010047/) |

Supporting quotes:
- *"Standardized behavioral phenotyping revealed a decreased escape response to touch, limb and abdominal hypotonia, and gait abnormalities in heterozygous Pur-alpha (+/-) mice"* ([PMID: 27651147](https://pubmed.ncbi.nlm.nih.gov/27651147/)).
- *"revealed reduced numbers of neurons in general, as well as reduced numbers of Pur-alpha+-immunopositive neurons and dendrites in heterozygous Pur-alpha mice"* ([PMID: 27651147](https://pubmed.ncbi.nlm.nih.gov/27651147/)).
- *"lack of Purα prolongs the postnatal proliferation of neuronal precursor cells both in the hippocampus and in the cerebellum"* ([PMID: 22010047](https://pubmed.ncbi.nlm.nih.gov/22010047/)).

**In vitro / cellular models.** Patient-mutation cell systems demonstrated impaired PURA folding, disrupted RNA binding, and failed P-body localization ([PMID: 38655849](https://pubmed.ncbi.nlm.nih.gov/38655849/)). Structural biology (crystallography of the DNA/RNA-binding domain with ssDNA) provides atomic-level models of mutation effects ([PMID: 26744780](https://pubmed.ncbi.nlm.nih.gov/26744780/)).

**Model limitations.** The heterozygous mouse is milder than the human syndrome in some domains and does not fully capture absent speech, seizures, or the full multisystem spectrum. Null mice model developmental mechanisms but exceed the human haploinsufficient dosage state. iPSC-derived neurons/organoids are a promising, not-yet-exhaustively-characterized avenue (inferred).

**Resources.** MGI (*Pura*); Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

```
  De novo PURA LoF variant / 5q31.3 deletion
                 |  (haploinsufficiency)
                 v
  Misfolded PUR domain  --->  loss of ssDNA/RNA binding & duplex unwinding
                 |                        (PMID 26744780, 38655849, 32476604)
                 v
  Failure to associate with P-bodies / RNP granules  (PMID 38655849)
                 |
                 v
  Impaired dendritic mRNA transport & local translation
     (with Staufen, FMRP, BC1/BC200 ncRNA)  (PMID 16511857)
                 |
        +--------+---------+
        v                  v
 Reduced postnatal      Impaired dendrite
 neuronal proliferation formation / maturation
   (PMID 22010047)        (PMID 16511857, 27651147)
        |                  |
        +--------+---------+
                 v
  Reduced neuron numbers & dendritic deficits
   (cerebellar vermis, hippocampus)  (PMID 27651147)
                 v
  Clinical syndrome: neonatal hypotonia, feeding difficulty,
  hiccups/apnea/hypothermia, developmental delay/ID, absent speech,
  seizures, hypersomnolence, multisystem anomalies
   (PMID 33275834, 25342064, 36376392)
```

**Upstream vs downstream.** The upstream lesion is the *PURA* variant and consequent protein misfolding/dosage loss; the proximal molecular defect is loss of nucleic-acid binding and RNP-granule/P-body association; downstream are the neurodevelopmental cellular deficits (proliferation, dendritogenesis) and, most distally, the clinical phenotype. The absence of a genotype-phenotype correlation suggests that once Pur-alpha function drops below a critical threshold, the phenotype is driven by haploinsufficiency generally rather than by the specific variant class.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [25439098](https://pubmed.ncbi.nlm.nih.gov/25439098/) | Mutations in *PURA* cause profound neonatal hypotonia... in 5q31.3 microdeletion syndrome | Establishes de novo *PURA* mutations as causal within the critical region |
| [25342064](https://pubmed.ncbi.nlm.nih.gov/25342064/) | WES in family trios reveals de novo *PURA* mutations | Independent trio confirmation; core neonatal features; Pur repeat III hypothesis |
| [26582469](https://pubmed.ncbi.nlm.nih.gov/26582469/) | Long-term follow-up, smallest 5q31.2q31.3 deletion | Confirms phenocritical role; documents adolescent deterioration and respiratory mortality |
| [36376392](https://pubmed.ncbi.nlm.nih.gov/36376392/) | 25 Mainland Chinese cohort | Phenotype frequencies; recurrent variants; MRI differences deletion vs point mutation |
| [33275834](https://pubmed.ncbi.nlm.nih.gov/33275834/) | Expanding the phenotype (Phe233del) | Comprehensive multisystem phenotype; 78 individuals / 64 variants |
| [37204304](https://pubmed.ncbi.nlm.nih.gov/37204304/) | New case, recurrent Phe233del | No reliable genotype-phenotype correlation; Purα functions |
| [29097605](https://pubmed.ncbi.nlm.nih.gov/29097605/) | Clinical delineation in 32 individuals | Clinical recognizability; no genotype-phenotype correlation; 3D modeling |
| [38655849](https://pubmed.ncbi.nlm.nih.gov/38655849/) | Mutations impair PUR-domain integrity & P-body association | Molecular mechanism (misfolding, RNA binding, P-bodies); ~650 patients |
| [26744780](https://pubmed.ncbi.nlm.nih.gov/26744780/) | Structural basis of nucleic-acid recognition & unwinding | Crystal structure; molecular explanation of point mutations |
| [32476604](https://pubmed.ncbi.nlm.nih.gov/32476604/) | PC4-like domain family | PUR-domain fold and nucleic-acid-binding properties |
| [16511857](https://pubmed.ncbi.nlm.nih.gov/16511857/) | Role of Pur alpha in targeting mRNA in dendrites | Dendritic mRNA transport with Staufen/FMRP/BC1; essential for dendrite formation |
| [22010047](https://pubmed.ncbi.nlm.nih.gov/22010047/) | Lack of Pur-alpha alters brain development | Null-mouse developmental mechanism, megalencephaly, proliferation |
| [27651147](https://pubmed.ncbi.nlm.nih.gov/27651147/) | Memory deficits, gait ataxia, neuronal loss in Purα +/− mice | Heterozygous mouse recapitulation; neuronal loss |
| [32035967](https://pubmed.ncbi.nlm.nih.gov/32035967/) | Pur-based peptide & C9orf72 G-quadruplex | Pur G-quadruplex biology; therapeutic-concept context |
| [23720732](https://pubmed.ncbi.nlm.nih.gov/23720732/) | Baculovirus VP1054 as acquired PURα | Evolutionary conservation of Pur nucleic-acid-binding function |

---

## Limitations and Knowledge Gaps

1. **No formal epidemiology.** Prevalence/incidence are unknown; patient counts reflect ascertainment, not population frequency.
2. **No genotype-phenotype correlation.** Prognostic counseling cannot be refined by variant class ([PMID: 29097605](https://pubmed.ncbi.nlm.nih.gov/29097605/); [PMID: 37204304](https://pubmed.ncbi.nlm.nih.gov/37204304/)).
3. **Mechanism partly inferred from models.** The dendrite/proliferation defects and dosage sensitivity derive largely from mouse and in vitro systems; direct human neuropathology is limited.
4. **No biomarker.** No circulating, imaging, or epigenetic biomarker for diagnosis, severity, or progression.
5. **Limited long-term natural history.** Adult outcomes and the frequency of progressive respiratory decline are under-characterized (largely a single long-term case).
6. **No therapeutics.** No disease-modifying treatment or interventional trial data; dosage-restoration approaches are conceptual.
7. **Epigenetics / methylation signature** not established.
8. **iPSC/organoid human models** not yet exhaustively characterized.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective natural-history registry** (via PURA Syndrome Foundation) with standardized longitudinal capture of respiratory, seizure, feeding, communication, and mobility outcomes to define prognosis and trial endpoints.
2. **iPSC-derived neurons and cortical/cerebellar organoids** carrying patient variants to quantify dendritogenesis, P-body dynamics, and translational dysregulation in a human context, validating the mouse-derived mechanism.
3. **Transcriptome-wide identification of Pur-alpha-bound and dysregulated dendritic mRNAs** (CLIP-seq + ribosome profiling) in patient and model neurons to pinpoint downstream effectors.
4. **Dosage-restoration proof-of-concept:** test AAV gene supplementation or ASO-mediated upregulation of *PURA* in heterozygous mice, given the haploinsufficiency mechanism and dosage sensitivity.
5. **Structure-guided variant classification pipeline** using crystal-structure/AlphaFold models to standardize VUS interpretation and probe whether subtle folding-stability differences underlie the variable expressivity despite no categorical genotype-phenotype correlation.
6. **Respiratory-focused clinical surveillance protocol** and apnea/sleep studies to reduce the principal source of mortality.
7. **Search for a methylation episignature** across a PURA cohort to enable episignature-based diagnostic support.

---

*Report compiled from 8 confirmed findings across 15 reviewed primary papers. Evidence types: human clinical (cohorts, case series, trio exome studies), model organism (mouse knockout/heterozygous), in vitro (patient-mutation cell systems), and computational/structural (crystallography, 3D modeling).*


## Artifacts

- [OpenScientist final report](PURA_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PURA_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 28 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0011968` (1 mention) - the report calls it "Very frequent"; HP calls it **Feeding difficulties**
- `HP:0001250` (1 mention) - the report calls it "Common"; HP calls it **Seizure**
- `HP:0002072` (1 mention) - the report calls it "dyskinesia"; HP calls it **Chorea**
- `HP:0100585` (1 mention) - the report calls it "hiccough"; HP calls it **Telangiectasia of the skin**
- `HP:0002045` (1 mention) - the report calls it "Frequent"; HP calls it **Hypothermia**
- `HP:0001999` (1 mention) - the report calls it "Frequent (more in deletion carriers)"; HP calls it **Abnormal facial shape**
- `HP:0001627` (1 mention) - the report calls it "Less common"; HP calls it **Abnormal heart morphology**
- `HP:0000119` (1 mention) - the report calls it "Less common"; HP calls it **Abnormality of the genitourinary system**
- `HP:0000478` (1 mention) - the report calls it "Less common"; HP calls it **Abnormality of the eye**
- `HP:0000924` (1 mention) - the report calls it "Less common"; HP calls it **Abnormality of the skeletal system**
- `HP:0000818` (1 mention) - the report calls it "Less common"; HP calls it **Abnormality of the endocrine system**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0100786` (obsolete Hypersomnia) (1 mention) - replaced by `HP:0001262`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002505` (1 mention) - the report calls it "inability to walk"; HP calls it **Loss of ambulation**, and lists "Loss of ability to walk" among its other names
- `CL:0000121` (2 mentions) - the report calls it "cerebellar/Purkinje neuron", "Purkinje/cerebellar neuron"; CL calls it **Purkinje cell**, and lists "Purkinje neuron" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000121` - called "cerebellar/Purkinje neuron", "Purkinje/cerebellar neuron"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.