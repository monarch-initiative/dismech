---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T02:05:32.316694'
end_time: '2026-09-30T02:21:20.271868'
duration_seconds: 947.96
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Pneumonia Caused By Pseudomonas Aeruginosa Infection
  mondo_id: MONDO:0037398
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
citation_count: 49
reference_validation:
  total_references: 49
  verified: 49
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 49
  on_topic: 28
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 29
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 2
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0001945
    reported_labels:
    - Common
    ontology_label: Fever
  - term_id: HP:0012735
    reported_labels:
    - Common
    ontology_label: Cough
  - term_id: HP:0002094
    reported_labels:
    - Common
    ontology_label: Dyspnea
  - term_id: HP:0025440
    reported_labels:
    - Common (VAP)
    ontology_label: Warm reactive autoantibody positivity
  - term_id: HP:0001974
    reported_labels:
    - Common
    ontology_label: Increased total leukocyte count
  - term_id: HP:0011227
    reported_labels:
    - 'Common (PMID: 42592972)'
    ontology_label: Elevated circulating C-reactive protein concentration
  - term_id: HP:0031977
    reported_labels:
    - Diagnostic
    ontology_label: Increased vertical cup-to-disc ratio - 0.9
  - term_id: HP:0033677
    reported_labels:
    - T3SS-driven subset
    ontology_label: Acute respiratory distress syndrome
  - term_id: UBERON:0002048
    reported_labels:
    - Primary organ:** Lung
    ontology_label: lung
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
  path: Pneumonia_Caused_By_Pseudomonas_Aeruginosa_Infection-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pneumonia_Caused_By_Pseudomonas_Aeruginosa_Infection-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pneumonia Caused By Pseudomonas Aeruginosa Infection
- **MONDO ID:** MONDO:0037398 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Pneumonia Caused By Pseudomonas Aeruginosa Infection** covering all of the
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

# Pneumonia Caused By *Pseudomonas aeruginosa* Infection — Comprehensive Disease Report

**Target disease:** Pneumonia Caused By *Pseudomonas aeruginosa* Infection
**MONDO ID:** MONDO:0037398 · **Category:** Infectious Disease
**Pathogen taxon:** *Pseudomonas aeruginosa* — NCBI:txid287 (species); genus *Pseudomonas* NCBI:txid286
**Investigation:** 5 iterations · 9 confirmed findings · 61 papers reviewed · Report date 2026-09-30

---

## Summary

Pneumonia caused by *Pseudomonas aeruginosa* is an **opportunistic Gram-negative lower-respiratory-tract infection** that predominantly afflicts hosts with compromised mechanical or immune barriers — mechanically ventilated ICU patients, neutropenic and immunocompromised patients, and people with structural lung disease such as cystic fibrosis (CF) and bronchiectasis. It is not a heritable Mendelian disorder; its "etiology" is infectious, with host genetics (most paradigmatically *CFTR* mutations) acting as susceptibility modifiers rather than causes. Clinically it is one of the leading causes of hospital-acquired pneumonia (HAP) and ventilator-associated pneumonia (VAP), and it is increasingly **multidrug-resistant (MDR)** and **carbapenem-resistant (CRPA)** — a WHO critical-priority pathogen.

The pathophysiology splits into two mechanistic branches. In **acute pneumonia**, the **Type III Secretion System (T3SS)** injects cytotoxic effectors (ExoU, ExoS, ExoT, ExoY) into host cells, while flagellin is sensed by **TLR5** on airway epithelium and the T3SS is sensed by the **NLRC4 inflammasome** in alveolar macrophages, driving IL-1β-mediated neutrophilic inflammation, alveolar–capillary barrier destruction, acute lung injury/ARDS and, frequently, death. In **chronic pneumonia** (the CF/bronchiectasis paradigm), conversion to a **mucoid, alginate-overproducing biofilm phenotype** evades opsonic and non-opsonic phagocytosis and establishes lifelong airway persistence with progressive lung-function decline.

Prognosis is dominated by two modifiable factors — **antimicrobial resistance** and **inappropriate initial empiric therapy** — both of which sharply raise mortality. VAP attributable mortality is roughly 30%, and 28-day all-cause mortality in ventilated HAP/VAP trials remains ~20–26%. First-line management uses anti-pseudomonal β-lactams; **ceftolozane/tazobactam** was non-inferior to meropenem in the phase 3 ASPECT-NP trial. Prevention rests on ventilator-care bundles (with several traditional components now questioned), and emerging therapies include inhaled antibiotics, anti-virulence monoclonal antibodies, DNA vaccines, and bacteriophage therapy.

---

## 1. Disease Information

**Overview.** *Pseudomonas aeruginosa* pneumonia is a lung parenchymal infection caused by the ubiquitous, aerobic, non-fermenting Gram-negative bacillus *P. aeruginosa*. It occurs mainly as **hospital-acquired pneumonia (HAP)** and **ventilator-associated pneumonia (VAP)**, and as chronic airway infection in structural lung disease. Acute *P. aeruginosa* pneumonia predominantly affects immunocompromised, neutropenic, and mechanically ventilated patients ([PMID: 25520826](https://pubmed.ncbi.nlm.nih.gov/25520826/), [PMID: 9570172](https://pubmed.ncbi.nlm.nih.gov/9570172/)).

**Key identifiers.**
- **MONDO:** MONDO:0037398
- **Causative organism — NCBI Taxonomy:** *Pseudomonas aeruginosa*, txid287
- **ICD-10:** J15.1 (Pneumonia due to *Pseudomonas*); **ICD-11:** bacterial pneumonia with *Pseudomonas* as the causal agent
- **MeSH:** "Pneumonia, Bacterial" + "Pseudomonas Infections" / "Pseudomonas aeruginosa"
- **OMIM/Orphanet:** Not applicable as a Mendelian entity (infectious disease); *CFTR*/cystic fibrosis (OMIM 219700; Orphanet ORPHA:586) is the relevant host-susceptibility entry.

**Synonyms / alternative names.** *Pseudomonas* pneumonia; *Pseudomonal* pneumonia; *P. aeruginosa* lower respiratory tract infection; *Pseudomonas aeruginosa* HAP/VAP; nosocomial *Pseudomonas* pneumonia.

**Data source type.** This report aggregates **disease-level resources** (surveillance cohorts, randomized trials, mechanistic model-organism and in-vitro studies, and registry data) rather than individual EHR-derived patient records.

---

## 2. Etiology

**Primary cause (infectious).** The disease is caused by infection with *P. aeruginosa*. It is fundamentally an **opportunistic** infection: host predisposition defines who develops disease.

**Risk factors (environmental / host).**
- **Mechanical ventilation / endotracheal intubation** — the dominant risk setting; VAP incidence is ~7–15% of ventilated patients ([PMID: 30390751](https://pubmed.ncbi.nlm.nih.gov/30390751/)), and prolonged ventilation, reintubation and elevated CRP associate with VAP ([PMID: 42592972](https://pubmed.ncbi.nlm.nih.gov/42592972/)).
- **Immunocompromise / neutropenia** — *P. aeruginosa* was the most frequent organism in bacteremic pneumonia in neutropenic cancer patients ([PMID: 9570172](https://pubmed.ncbi.nlm.nih.gov/9570172/)).
- **Structural lung disease** — cystic fibrosis and bronchiectasis (chronic branch).
- **Prior antibiotic exposure** — drives resistant strains and inappropriate initial therapy; associated with higher mortality (51.3% vs 34.0%, p<0.001) in Gram-negative severe sepsis ([PMID: 21499086](https://pubmed.ncbi.nlm.nih.gov/21499086/)).
- **Comorbidities** — diabetes (independently associated with MDR infection, adjusted OR 2.82), cardiovascular disease, COPD, hypertension ([PMID: 42393552](https://pubmed.ncbi.nlm.nih.gov/42393552/)); ECMO support ([PMID: 42685911](https://pubmed.ncbi.nlm.nih.gov/42685911/)); chest trauma with high injury-severity score and tracheostomy ([PMID: 41978407](https://pubmed.ncbi.nlm.nih.gov/41978407/)).

**Genetic (host susceptibility) risk factors.**
- **CFTR mutations (cystic fibrosis).** The paradigmatic host genetic risk factor for *chronic* pulmonary *P. aeruginosa* infection. CF produces progressive lung disease with chronic infection, mucus accumulation, airway inflammation and structural damage, with *P. aeruginosa* as a dominant chronic pathogen ([PMID: 38702073](https://pubmed.ncbi.nlm.nih.gov/38702073/), [PMID: 41010996](https://pubmed.ncbi.nlm.nih.gov/41010996/)). The most common allele is **F508del** ([PMID: 38742380](https://pubmed.ncbi.nlm.nih.gov/38742380/)).
- **Inflammasome variants.** Gain-of-function variants in **NLRP3/NLRC4** inflammasome genes have been associated with clinical outcomes in CF ([PMID: 33848452](https://pubmed.ncbi.nlm.nih.gov/33848452/)).

**Protective factors.** No validated protective genetic variant is established for this infectious disease. Environmental/behavioral protection is essentially **prevention of acquisition** (see §13): avoiding intubation, minimizing sedation, early extubation and mobilization ([PMID: 31585480](https://pubmed.ncbi.nlm.nih.gov/31585480/)). Innate effectors such as **Cmpk2** enhance neutrophil phagocytosis and host survival (model-organism evidence; [PMID: 40616692](https://pubmed.ncbi.nlm.nih.gov/40616692/)).

**Gene–environment interactions.** The clearest interaction is *CFTR* deficiency × environmental *P. aeruginosa* exposure → chronic mucoid airway infection. Prior-antibiotic environment × bacterial resistance genotype → inappropriate therapy → death is a second, treatment-relevant interaction.

---

## 3. Phenotypes

*P. aeruginosa* pneumonia presents as a bacterial pneumonia syndrome; phenotypes are acquired clinical manifestations, not congenital.

| Phenotype | Type | Onset | Severity / course | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Fever | Clinical sign | Adult-onset (acquired) | Variable | Common | HP:0001945 |
| Cough / productive cough | Symptom | Acquired | Variable | Common | HP:0012735 |
| Dyspnea | Symptom | Acquired, acute/subacute | Moderate–severe | Common | HP:0002094 |
| Hypoxemia / respiratory failure | Lab/physiologic | Acute | Severe | Frequent in ICU | HP:0012418 / HP:0002878 |
| Purulent sputum / tracheal secretions | Sign | Acquired | Variable | Common (VAP) | HP:0025440 |
| Leukocytosis | Lab abnormality | Acute | Variable | Common | HP:0001974 |
| Elevated CRP | Lab abnormality | Acute | Marker of burden (AUC 0.83 for VAP) | Common ([PMID: 42592972](https://pubmed.ncbi.nlm.nih.gov/42592972/)) | HP:0011227 |
| Bacteremia / sepsis / septic shock | Complication | Acute | Severe, high-mortality | Subset (poor outcome) | HP:0031273 / HP:0100806 |
| Pulmonary infiltrates / consolidation | Imaging sign | Acute | Variable | Diagnostic | HP:0031977 |
| ARDS / acute lung injury | Physiologic | Acute | Severe | T3SS-driven subset | HP:0033677 |

**Quality-of-life impact.** Acute *P. aeruginosa* pneumonia in ventilated patients prolongs mechanical ventilation (12.5 vs 7.3 days) and hospitalization (19.6 vs 12.2 days) ([PMID: 42592972](https://pubmed.ncbi.nlm.nih.gov/42592972/)). In the chronic CF branch, persistent infection drives progressive lung-function decline, exacerbations, and reduced survival ([PMID: 38702073](https://pubmed.ncbi.nlm.nih.gov/38702073/)).

---

## 4. Genetic / Molecular Information

**No human causal gene** produces *P. aeruginosa* pneumonia — it is infectious. Genetics operates on two axes:

**(a) Host susceptibility / modifier genes (human).**
- **CFTR** (HGNC:1884; OMIM 602421) — loss-of-function mutations (F508del most common) cause CF and predispose to chronic *P. aeruginosa* airway infection ([PMID: 38742380](https://pubmed.ncbi.nlm.nih.gov/38742380/), [PMID: 42774065](https://pubmed.ncbi.nlm.nih.gov/42774065/)). Variant classes include in-frame deletion (F508del), nonsense/stop-codon, splice, and gating variants; population-specific alleles (e.g., N1303K, G542X, 2789+5G>A enriched in Italy) exist ([PMID: 42370441](https://pubmed.ncbi.nlm.nih.gov/42370441/)).
- **NLRP3 / NLRC4** — inflammasome gain-of-function variants associated with CF outcomes ([PMID: 33848452](https://pubmed.ncbi.nlm.nih.gov/33848452/)).
- **TLR5, MUC1** — innate-sensing genes that modulate epithelial responses ([PMID: 16239509](https://pubmed.ncbi.nlm.nih.gov/16239509/), [PMID: 22250084](https://pubmed.ncbi.nlm.nih.gov/22250084/)).

**(b) Bacterial virulence & resistance loci (pathogen genome).**
- **T3SS effector genes:** *exoU* (phospholipase A2, most cytotoxic), *exoS* (ADP-ribosyltransferase + GAP), *exoT* (GAP), *exoY* (nucleotidyl cyclase); master regulator *exsA* ([PMID: 25520826](https://pubmed.ncbi.nlm.nih.gov/25520826/), [PMID: 15972518](https://pubmed.ncbi.nlm.nih.gov/15972518/)).
- **Alginate biosynthesis:** *algD* operon, regulator *mucA* (mucoid conversion) ([PMID: 37009499](https://pubmed.ncbi.nlm.nih.gov/37009499/)).
- **Flagellin:** *fliC* (TLR5 ligand) ([PMID: 16239509](https://pubmed.ncbi.nlm.nih.gov/16239509/)).
- **Resistance determinants:** carbapenemase and other AMR genes confirmed by whole-genome sequencing in high-risk clones ([PMID: 41751514](https://pubmed.ncbi.nlm.nih.gov/41751514/)).

**Epigenetics / chromosomal abnormalities:** Not applicable to the disease as an infectious entity in humans.

---

## 5. Environmental Information

**Infectious agent.** *Pseudomonas aeruginosa* (NCBI txid287), an aerobic, motile, non-fermenting Gram-negative bacillus. It is environmentally ubiquitous (water, moist surfaces, hospital reservoirs, medical devices) and forms biofilms on ventilator circuits and endotracheal tubes.

**Environmental / occupational factors.** Hospital and ICU environments, contaminated respiratory equipment, and indwelling devices are the principal reservoirs; >90% of MDR carbapenem-resistant *P. aeruginosa* isolates in one large UAE survey originated in hospitals ([PMID: 41826861](https://pubmed.ncbi.nlm.nih.gov/41826861/)).

**Lifestyle factors.** Not the primary drivers; smoking/COPD contribute to structural lung disease that raises susceptibility ([PMID: 42393552](https://pubmed.ncbi.nlm.nih.gov/42393552/)).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

**ACUTE CYTOTOXIC BRANCH (ventilated / immunocompromised host):**

1. *P. aeruginosa* colonizes the lower airway (aided by ventilation, impaired clearance) → **leads to** contact with alveolar epithelium and macrophages.
2. Bacterial **flagellin** is recognized by **TLR5** on the apical surface of airway epithelial cells → **results in** NF-κB activation and pro-inflammatory chemokine/cytokine transcription ([PMID: 16239509](https://pubmed.ncbi.nlm.nih.gov/16239509/)). *(MUC1 tethers to TLR5 and dampens this signal — a counter-regulatory branch; [PMID: 22250084](https://pubmed.ncbi.nlm.nih.gov/22250084/).)*
3. The **Type III Secretion System** injects effectors **ExoU/ExoS/ExoT/ExoY** into host cells → **causes** direct cytotoxicity; ExoU (phospholipase A2) is most cytotoxic and **induces mitochondrial damage** in macrophages ([PMID: 35130452](https://pubmed.ncbi.nlm.nih.gov/35130452/)).
4. Alveolar macrophages **detect the T3SS** → **activate the NLRC4 inflammasome** → caspase-1 → **IL-1β/IL-1α release** ([PMID: 42779855](https://pubmed.ncbi.nlm.nih.gov/42779855/)). NLRC4 activation also **attenuates macrophage phagocytosis**, worsening bacterial persistence (inferred causal link from model organism; [PMID: 33489931](https://pubmed.ncbi.nlm.nih.gov/33489931/)).
5. IL-1β-driven inflammation → **massive neutrophil recruitment** and alveolar–capillary barrier disruption → **increased permeability, pulmonary edema, protein-rich BALF** (demonstrated as ↑wet/dry ratio and ↑BALF protein in the T3SS-competent CHA strain vs *exsA*-null mutant) ([PMID: 15972518](https://pubmed.ncbi.nlm.nih.gov/15972518/)).
6. → **Acute lung injury / ARDS, hypoxemic respiratory failure, sepsis/septic shock** → death in a substantial fraction.

**CHRONIC PERSISTENCE BRANCH (CF / bronchiectasis host):**

1. Impaired mucociliary clearance (e.g., *CFTR* loss) → chronic airway colonization.
2. *mucA* mutation → **alginate overproduction** → conversion to **mucoid biofilm** phenotype.
3. Alginate **inhibits opsonic and non-opsonic phagocytosis** by human (THP-1) and murine (MH-S) macrophages, blocking CD11b/CD14 receptor–ligand interactions ([PMID: 37009499](https://pubmed.ncbi.nlm.nih.gov/37009499/)).
4. → **immune evasion, chronic persistent infection, antibiotic tolerance** → recurrent exacerbations, progressive lung-function decline, mortality ([PMID: 38702073](https://pubmed.ncbi.nlm.nih.gov/38702073/)).

```
                    P. aeruginosa in lower airway
                               |
             ┌─────────────────┴──────────────────┐
     ACUTE (T3SS+ / planktonic)          CHRONIC (mucoid / biofilm)
             |                                     |
   flagellin→TLR5→NF-κB (epi)          mucA → alginate overproduction
   T3SS→ExoU/S/T/Y (cytotoxic)         → blocks CD11b/CD14 phagocytosis
   T3SS→NLRC4 inflammasome→IL-1β        → immune evasion
             |                                     |
   neutrophil influx + barrier loss     chronic persistence, tolerance
             |                                     |
   ALI / ARDS / respiratory failure     progressive lung decline
             |                                     |
        high acute mortality            recurrent exacerbations, ↓survival
```

**Cell types & GO/CL terms.** Alveolar epithelial cells (CL:0000066; type II CL:0002063), **alveolar macrophages** (CL:0000583), **neutrophils** (CL:0000775). Biological processes: T3SS-dependent cytotoxicity, **inflammasome complex assembly (GO:0140738)**, **NLRC4 inflammasome activation**, **IL-1β production (GO:0032611)**, **TLR5 signaling (GO:0034146)**, **neutrophil chemotaxis (GO:0030593)**, **phagocytosis (GO:0006909)**. Subcellular: **mitochondrion (GO:0005739)** (ExoU damage), plasma membrane, extracellular alginate matrix.

**Molecular profiling.** Multi-omics of acute *P. aeruginosa* infection and mitochondrial gene-expression analysis of ARDS datasets (GEO) identified Cmpk2 as an innate-immune protective node enriched in neutrophils by scRNA-seq ([PMID: 40616692](https://pubmed.ncbi.nlm.nih.gov/40616692/), [PMID: 40216004](https://pubmed.ncbi.nlm.nih.gov/40216004/)).

---

## 7. Anatomical Structures Affected

- **Primary organ:** Lung (UBERON:0002048), lung parenchyma / alveoli (**alveolus UBERON:0002299**), respiratory system (UBERON:0001004).
- **Secondary involvement:** Bloodstream (bacteremia/sepsis), systemic multi-organ dysfunction in septic shock; ARDS affects the alveolar–capillary unit bilaterally.
- **Tissues:** Airway and alveolar **epithelium** (apical surface where TLR5 is expressed on human tracheal epithelium; [PMID: 16239509](https://pubmed.ncbi.nlm.nih.gov/16239509/)); pulmonary capillary endothelium; alveolar interstitium.
- **Cells (CL):** alveolar macrophages (CL:0000583), neutrophils (CL:0000775), alveolar type I/II epithelial cells (CL:0002062 / CL:0002063).
- **Subcellular (GO CC):** mitochondrion (GO:0005739), plasma membrane, cytosolic inflammasome.
- **Localization / lateralization:** Typically **bilateral** in VAP/ARDS; may be unilateral/multilobar in focal bronchopneumonia.

---

## 8. Temporal Development

- **Onset (acute branch):** Acute to subacute, developing over hours–days; VAP is defined as pneumonia arising **>48 h after intubation**, with early-onset (~58%) and late-onset (~42%) forms ([PMID: 41939663](https://pubmed.ncbi.nlm.nih.gov/41939663/)).
- **Onset (chronic branch):** Insidious, beginning in childhood in CF and progressing over decades ([PMID: 38702073](https://pubmed.ncbi.nlm.nih.gov/38702073/)).
- **Progression:** Acute disease can progress rapidly to ARDS, septic shock and death; the chronic branch follows a relapsing–remitting course of exacerbations superimposed on progressive decline.
- **Duration:** Acute pneumonia is treated over days–weeks; chronic *P. aeruginosa* airway infection is typically lifelong once mucoid biofilm is established.
- **Remission:** Acute disease can resolve with appropriate, timely antimicrobial therapy; chronic mucoid infection rarely eradicates. **Critical intervention window:** early appropriate empiric therapy (see §11) is the key modifiable determinant of outcome.

---

## 9. Inheritance and Population (Epidemiology)

**Inheritance:** Not applicable (infectious disease). Host susceptibility via *CFTR* is autosomal recessive.

**Epidemiology (frequency as HAP/VAP pathogen).**

| Setting / cohort | *P. aeruginosa* rank / frequency | Resistance | PMID |
|---|---|---|---|
| Chinese HAP, 37 hospitals (n=543) | 3rd, 13.73% (behind *A. baumannii* 24.89%, *K. pneumoniae* 21.57%); HAP mortality 15.8% | — | [41758741](https://pubmed.ncbi.nlm.nih.gov/41758741/) |
| Egyptian ICU VAP (n=120) | 47/120 (39.2%) | 85.1% MDR; 80% colistin-S, only 12.5% CAZ/AVI-S | [41877050](https://pubmed.ncbi.nlm.nih.gov/41877050/) |
| Saudi HA-GNB, 5-yr (n=377) | 2nd, 34.0% | meropenem-R 34.3%; ciprofloxacin-R 44.4% | [42393552](https://pubmed.ncbi.nlm.nih.gov/42393552/) |
| UAE MDR-CRO surveillance | MDR-CR *P. aeruginosa* period prevalence 12.9% | carbapenem-resistant | [41826861](https://pubmed.ncbi.nlm.nih.gov/41826861/) |
| Bosnian ICU VAP (n=118) | 2nd after *A. baumannii*; VAP 34.7% | Gram-neg ≈85% | [42592972](https://pubmed.ncbi.nlm.nih.gov/42592972/) |

**Chronic CF branch:** chronic *P. aeruginosa* infection affects ~30–37% of adults and ~5–7% of paediatric CF patients in the Italian CF Registry, declining with CFTR-modulator therapy ([PMID: 38742380](https://pubmed.ncbi.nlm.nih.gov/38742380/), [PMID: 42370441](https://pubmed.ncbi.nlm.nih.gov/42370441/)).

**Geographic distribution:** Global; MDR/CRPA burden is rising, with regional variation and WHO critical-priority status ([PMID: 42523687](https://pubmed.ncbi.nlm.nih.gov/42523687/)). **Sex/age:** Reflects the underlying ICU/comorbid population (older adults, male predominance in several cohorts).

---

## 10. Diagnostics

**Clinical/lab tests.**
- **Microbiology (gold standard):** culture of respiratory specimens — endotracheal aspirate (ETA) or bronchoalveolar lavage (BAL), with semi-quantitative thresholds (≥10⁵ CFU/mL for ETA) ([PMID: 41939663](https://pubmed.ncbi.nlm.nih.gov/41939663/), [PMID: 42801252](https://pubmed.ncbi.nlm.nih.gov/42801252/)). Antimicrobial susceptibility testing (CLSI) is essential given high MDR rates.
- **Inflammatory markers / biomarkers:** CRP discriminates VAP (AUC 0.83; [PMID: 42592972](https://pubmed.ncbi.nlm.nih.gov/42592972/)); leukocytosis; bronchoalveolar **IL-1β** correlates with bacterial burden and may mark ongoing/unresolved infection ([PMID: 12626989](https://pubmed.ncbi.nlm.nih.gov/12626989/)).
- **Molecular/genomic:** whole-genome sequencing profiles resistance and virulence ([PMID: 41751514](https://pubmed.ncbi.nlm.nih.gov/41751514/)); metagenomic next-generation sequencing aids complex cases ([PMID: 42661655](https://pubmed.ncbi.nlm.nih.gov/42661655/)).
- **Imaging:** chest radiograph/CT showing infiltrates/consolidation (used with clinical criteria).

**Clinical criteria.** Modified Clinical Pulmonary Infection Score (CPIS >6), CDC/NHSN surveillance definitions for HAP/VAP; VAP requires pneumonia >48 h post-intubation ([PMID: 41939663](https://pubmed.ncbi.nlm.nih.gov/41939663/), [PMID: 42393552](https://pubmed.ncbi.nlm.nih.gov/42393552/)).

**Differential diagnosis.** Other Gram-negative HAP/VAP pathogens (*A. baumannii*, *K. pneumoniae*), *S. aureus* pneumonia, aspiration pneumonitis, ARDS of non-infectious cause, pulmonary aspergillosis in the immunocompromised.

**Genetic testing.** Not for the infection itself; **CFTR sequencing / sweat chloride testing** is indicated when chronic *P. aeruginosa* infection suggests undiagnosed CF (diagnostic delay causes irreversible damage; [PMID: 42774065](https://pubmed.ncbi.nlm.nih.gov/42774065/)).

---

## 11. Outcome / Prognosis

**Mortality.**
- VAP attributable mortality ~**30%** ([PMID: 18060758](https://pubmed.ncbi.nlm.nih.gov/18060758/)).
- 28-day all-cause mortality in ventilated HAP/VAP (ASPECT-NP, Gram-negative pathogens): **20.1%** (ceftolozane/tazobactam) vs **25.8%** (meropenem) ([PMID: 35022730](https://pubmed.ncbi.nlm.nih.gov/35022730/)); ~23.7–24.0% with severe respiratory failure ([PMID: 36773112](https://pubmed.ncbi.nlm.nih.gov/36773112/)).
- Overall HA-GNB in-hospital mortality up to ~40% in high-comorbidity cohorts ([PMID: 42393552](https://pubmed.ncbi.nlm.nih.gov/42393552/)).

**Dominant prognostic factors (modifiable).**
1. **Carbapenem/multidrug resistance** — CR infections carry significantly higher mortality across pathogens including *P. aeruginosa* (multicentre Indian surveillance, 159,336 patients; [PMID: 42707186](https://pubmed.ncbi.nlm.nih.gov/42707186/)).
2. **Inappropriate initial therapy** — prior-antibiotic exposure → inappropriate empiric therapy (45.4% vs 21.2%) → higher hospital mortality (51.3% vs 34.0%) ([PMID: 21499086](https://pubmed.ncbi.nlm.nih.gov/21499086/)).
3. Shock/vasopressor use, severe organ failure (SOFA) ([PMID: 36773112](https://pubmed.ncbi.nlm.nih.gov/36773112/), [PMID: 36457059](https://pubmed.ncbi.nlm.nih.gov/36457059/)).

**Complications:** bacteremia, septic shock, ARDS, multi-organ failure; prolonged ventilation and hospitalization; in CF, progressive respiratory failure and death (median age at death in Italian CF registry 43–57 years) ([PMID: 38742380](https://pubmed.ncbi.nlm.nih.gov/38742380/), [PMID: 42370441](https://pubmed.ncbi.nlm.nih.gov/42370441/)).

---

## 12. Treatment

**First-line pharmacotherapy — anti-pseudomonal β-lactams.**
- **Ceftolozane/tazobactam** (3 g q8h) — non-inferior to meropenem in the phase 3 double-blind **ASPECT-NP** trial (NCT02070757) for ventilated HABP/VABP; for Gram-negative pathogens 28-day ACM 20.1% vs 25.8%, clinical cure 60.6% vs 57.1%, microbiologic eradication 73.0% vs 67.9%; *P. aeruginosa* comprised 25.0% of baseline LRT pathogens ([PMID: 35022730](https://pubmed.ncbi.nlm.nih.gov/35022730/)). Efficacy held across renal-clearance and organ-failure subgroups ([PMID: 34600585](https://pubmed.ncbi.nlm.nih.gov/34600585/), [PMID: 36773112](https://pubmed.ncbi.nlm.nih.gov/36773112/)). *(NCIT: Ceftolozane-Tazobactam.)*
- **Meropenem/carbapenems** — comparator standard ([PMID: 35022730](https://pubmed.ncbi.nlm.nih.gov/35022730/)). *(NCIT: Meropenem.)*
- Other anti-pseudomonal agents: piperacillin-tazobactam, cefepime, ceftazidime, ceftazidime-avibactam, aztreonam, fluoroquinolones, aminoglycosides (guided by susceptibility, given high resistance rates).

**For carbapenem-resistant *P. aeruginosa* (CRPA).** Indian ICU guidelines (GRADE) favor **non-polymyxin** regimens for CRPA where efficacy is comparable but polymyxin toxicity is higher (42.1% vs 17.9%) ([PMID: 42523687](https://pubmed.ncbi.nlm.nih.gov/42523687/)). Colistin remains active against many MDR isolates (80% colistin-S in an Egyptian VAP series) ([PMID: 41877050](https://pubmed.ncbi.nlm.nih.gov/41877050/)).

**Adjunctive / inhaled therapy.** High-dose inhaled colistin followed by inhaled amikacin/tobramycin plus systemic therapy achieved clinical improvement and microbiologic eradication in MDR *P. aeruginosa* HAP/VAP despite in-vitro resistance, via high intrapulmonary concentrations ([PMID: 42807670](https://pubmed.ncbi.nlm.nih.gov/42807670/), [PMID: 18060758](https://pubmed.ncbi.nlm.nih.gov/18060758/)).

**Experimental / advanced therapeutics.**
- **Anti-virulence monoclonal antibodies:** fully human antibody cocktail targeting PcrV (T3SS tip), exotoxin A, and PA0833 gave broad-spectrum protection ([PMID: 42662857](https://pubmed.ncbi.nlm.nih.gov/42662857/)); complement-activating CoMiX targeting Psl improved survival in murine pneumonia ([PMID: 40961506](https://pubmed.ncbi.nlm.nih.gov/40961506/)).
- **Bacteriophage therapy:** inhaled phage case series showed clinical/microbiological improvement without major adverse events ([PMID: 41887374](https://pubmed.ncbi.nlm.nih.gov/41887374/)); murine efficacy depends on synergy with neutrophils, and alveolar macrophages can limit phage density ([PMID: 40595615](https://pubmed.ncbi.nlm.nih.gov/40595615/)).

**Supportive care:** mechanical ventilation, oxygenation, hemodynamic support for sepsis, source control (device management), antimicrobial stewardship.

---

## 13. Prevention

**Primary prevention (avoid acquisition).** Ventilator-care bundles are central. The **2026 SIAARTI consensus** endorsed **subglottic secretion drainage** and **endotracheal cuff-pressure control**; it did **not** recommend routine chlorhexidine oral care (outside cardiac surgery) and questioned selective digestive decontamination (SDD) ([PMID: 42415225](https://pubmed.ncbi.nlm.nih.gov/42415225/)). Objectively beneficial measures include **avoiding intubation, minimizing sedation, spontaneous awakening/breathing trials, early extubation and mobilization**; oral chlorhexidine may increase mortality and stress-ulcer prophylaxis may facilitate pneumonia; SDD lowers VAP/mortality in low-resistance but not high-resistance ICUs ([PMID: 31585480](https://pubmed.ncbi.nlm.nih.gov/31585480/), [PMID: 28759469](https://pubmed.ncbi.nlm.nih.gov/28759469/), [PMID: 32486132](https://pubmed.ncbi.nlm.nih.gov/32486132/)).

**Secondary prevention.** Early recognition/risk stratification (ISS, tracheostomy timing, CRP, ventilation duration) ([PMID: 41978407](https://pubmed.ncbi.nlm.nih.gov/41978407/)); antimicrobial stewardship to preserve appropriate empiric therapy ([PMID: 42393552](https://pubmed.ncbi.nlm.nih.gov/42393552/)).

**Tertiary prevention.** Infection control to prevent MDR spread (>90% of MDR-CRPA hospital-sourced; [PMID: 41826861](https://pubmed.ncbi.nlm.nih.gov/41826861/)); CFTR-modulator therapy reduces chronic *P. aeruginosa* prevalence in CF ([PMID: 42370441](https://pubmed.ncbi.nlm.nih.gov/42370441/)).

**Immunization (experimental).** No licensed vaccine. An **OprF/PcrV bivalent DNA vaccine** with hydrogel delivery reduced bacterial burden and improved survival in a murine pneumonia model ([PMID: 38359491](https://pubmed.ncbi.nlm.nih.gov/38359491/)).

---

## 14. Other Species / Natural Disease

- **Taxonomy of pathogen:** *Pseudomonas aeruginosa* (NCBI txid287); broad host range.
- **Cross-species susceptibility:** *P. aeruginosa* pneumonia and infection occur across mammals; it is an opportunistic veterinary pathogen. Experimental infection is established in **mice**, **rats**, and **zebrafish** ([PMID: 15972518](https://pubmed.ncbi.nlm.nih.gov/15972518/), [PMID: 40616692](https://pubmed.ncbi.nlm.nih.gov/40616692/)).
- **Comparative mechanisms:** Innate sensing (TLR5, NLRC4 inflammasome) and T3SS-mediated cytotoxicity are conserved across mammalian hosts, enabling model-organism study.
- **Zoonotic potential:** Environmental/opportunistic rather than classically zoonotic.

---

## 15. Model Organisms

| Model | Type | Use / findings | PMID |
|---|---|---|---|
| Rat acute lung injury | Mammalian, in vivo | T3SS-competent CHA vs *exsA*-null CHA-D1: T3SS drives ↑wet/dry ratio, ↑BALF protein, ↑mortality | [15972518](https://pubmed.ncbi.nlm.nih.gov/15972518/) |
| Mouse acute pneumonia (intratracheal) | Mammalian, in vivo | Cmpk2-KO exacerbates ALI; NLRC4 inflammasome pathology; ASC/MSC, phage, mAb, vaccine efficacy | [40616692](https://pubmed.ncbi.nlm.nih.gov/40616692/), [33489931](https://pubmed.ncbi.nlm.nih.gov/33489931/), [38359491](https://pubmed.ncbi.nlm.nih.gov/38359491/), [40961506](https://pubmed.ncbi.nlm.nih.gov/40961506/) |
| Murine bone-marrow-derived macrophages | In vitro/ex vivo | ExoU induces mitochondrial damage | [35130452](https://pubmed.ncbi.nlm.nih.gov/35130452/) |
| Zebrafish embryo | Vertebrate | Bacterial burden/survival; Cmpk2/STING-dependent phagocytosis | [40616692](https://pubmed.ncbi.nlm.nih.gov/40616692/) |
| Human cell lines (A549, THP-1, MH-S, HEK293-TLR5) | In vitro | T3SS cytotoxicity (LDH), TLR5 signaling, alginate anti-phagocytosis | [15972518](https://pubmed.ncbi.nlm.nih.gov/15972518/), [37009499](https://pubmed.ncbi.nlm.nih.gov/37009499/), [16239509](https://pubmed.ncbi.nlm.nih.gov/16239509/) |

**Recapitulation & limitations:** Mouse/rat models faithfully reproduce acute T3SS-driven neutrophilic lung injury and inflammasome biology and are the workhorse for therapeutic testing; they less faithfully capture chronic human mucoid biofilm persistence, the full MDR resistance landscape, and human comorbidity context. Phage-therapy models further reveal immune–phage feedback (macrophages reduce phage density) that complicates translation ([PMID: 40595615](https://pubmed.ncbi.nlm.nih.gov/40595615/)).

---

## Key Findings (with statistical evidence)

**F001 — T3SS is the principal acute virulence determinant.** In a rat ALI model, the T3SS-expressing CHA strain caused significantly greater lung injury (higher wet/dry ratio and BALF protein at 12 h), increased A549 cytotoxicity, decreased clearance and increased mortality vs the isogenic *exsA*-null mutant CHA-D1. Four effectors — ExoS, ExoT, ExoU, ExoY — are canonical ([PMID: 15972518](https://pubmed.ncbi.nlm.nih.gov/15972518/), [PMID: 25520826](https://pubmed.ncbi.nlm.nih.gov/25520826/)). The T3SS *"is involved in lung injury, septic shock, and a poor patient outcome."*

**F002 — Leading MDR HAP/VAP pathogen.** 3rd-ranked HAP pathogen in a 37-hospital Chinese cohort (13.73%); 39.2% of ICU VAP with 85.1% MDR in an Egyptian series; 2nd-ranked (34.0%) in a Saudi HA-GNB cohort ([PMID: 41758741](https://pubmed.ncbi.nlm.nih.gov/41758741/), [PMID: 41877050](https://pubmed.ncbi.nlm.nih.gov/41877050/), [PMID: 42393552](https://pubmed.ncbi.nlm.nih.gov/42393552/)).

**F003 — Ceftolozane/tazobactam non-inferior; mortality ~20–26%.** ASPECT-NP: Gram-negative 28-day ACM 20.1% vs 25.8% (C/T vs meropenem); *P. aeruginosa* 25.0% of pathogens ([PMID: 35022730](https://pubmed.ncbi.nlm.nih.gov/35022730/)).

**F004 — Mucoid alginate/biofilm mediates immune evasion.** In mucoid FRD1 vs *algD* mutant, alginate inhibited opsonic and non-opsonic phagocytosis by human and murine macrophages ([PMID: 37009499](https://pubmed.ncbi.nlm.nih.gov/37009499/)).

**F005 — Prevention rests on modifiable bundles; some components questioned.** SIAARTI 2026 endorsed subglottic drainage and cuff-pressure control, not routine chlorhexidine; VAP incidence ~7–15% ([PMID: 42415225](https://pubmed.ncbi.nlm.nih.gov/42415225/), [PMID: 30390751](https://pubmed.ncbi.nlm.nih.gov/30390751/)).

**F006 — Host predisposition defines risk; CFTR/CF is the chronic paradigm.** ([PMID: 38702073](https://pubmed.ncbi.nlm.nih.gov/38702073/), [PMID: 9570172](https://pubmed.ncbi.nlm.nih.gov/9570172/), [PMID: 35927044](https://pubmed.ncbi.nlm.nih.gov/35927044/)).

**F007 — Resistance and inappropriate initial therapy dominate prognosis.** CR infections carry higher mortality across pathogens ([PMID: 42707186](https://pubmed.ncbi.nlm.nih.gov/42707186/)); inappropriate initial therapy → 51.3% vs 34.0% mortality ([PMID: 21499086](https://pubmed.ncbi.nlm.nih.gov/21499086/)); attributable VAP mortality ~30% ([PMID: 18060758](https://pubmed.ncbi.nlm.nih.gov/18060758/)).

**F008 — Emerging adjunctive/experimental therapies.** Inhaled antibiotics, anti-virulence mAbs (PcrV/ETA/PA0833), DNA vaccine (OprF/PcrV), and bacteriophage therapy ([PMID: 42807670](https://pubmed.ncbi.nlm.nih.gov/42807670/), [PMID: 42662857](https://pubmed.ncbi.nlm.nih.gov/42662857/), [PMID: 38359491](https://pubmed.ncbi.nlm.nih.gov/38359491/), [PMID: 41887374](https://pubmed.ncbi.nlm.nih.gov/41887374/)).

**F009 — Innate sensing via TLR5 and NLRC4 drives IL-1β neutrophilic injury.** TLR5 recognizes flagellin ([PMID: 16239509](https://pubmed.ncbi.nlm.nih.gov/16239509/)); alveolar macrophages detect T3SS → NLRC4 → IL-1β ([PMID: 42779855](https://pubmed.ncbi.nlm.nih.gov/42779855/)); ExoU damages mitochondria ([PMID: 35130452](https://pubmed.ncbi.nlm.nih.gov/35130452/)); NLRC4 activation attenuates phagocytosis and drives pulmonary damage ([PMID: 33489931](https://pubmed.ncbi.nlm.nih.gov/33489931/)).

---

## Mechanistic Model / Interpretation

The nine findings cohere into a **two-branch model** in which the *same* pathogen produces two clinically distinct diseases depending on host context and bacterial phenotype. The **acute branch** is a *cytotoxic + hyperinflammatory* process: T3SS injection (F001, F009) both directly kills epithelial/immune cells (ExoU phospholipase, mitochondrial damage) and triggers NLRC4-inflammasome IL-1β release, while flagellin–TLR5 amplifies NF-κB signaling. The convergent output is neutrophil-driven destruction of the alveolar–capillary barrier → ARDS → death. This branch dominates the ICU/ventilated/neutropenic population (F002, F006).

The **chronic branch** is an *immune-evasion + persistence* process: mucoid conversion (mucA→alginate) shields the biofilm from phagocytosis (F004), producing lifelong infection in structurally abnormal airways (CF/bronchiectasis; F006). Here the host genome (CFTR) is the key permissive factor.

Superimposed on both branches is the **resistance/therapy axis** (F002, F003, F007): outcomes are governed less by intrinsic virulence than by whether the organism is MDR/CRPA and whether initial empiric therapy is appropriate. This reframes prognosis as substantially *modifiable* through stewardship, rapid diagnostics, and next-generation agents (F003, F008). Prevention (F005) closes the loop by reducing acquisition upstream of all mechanisms.

---

## Evidence Base

| Domain | Key papers (PMID) | Contribution |
|---|---|---|
| Virulence / T3SS | 15972518, 25520826, 35130452 | Establish T3SS effectors as drivers of acute lung injury and mitochondrial damage |
| Innate sensing | 16239509, 42779855, 33489931, 22250084 | TLR5/flagellin and NLRC4/IL-1β inflammatory axis; MUC1 counter-regulation |
| Chronic persistence | 37009499, 38702073, 41010996, 42774065 | Mucoid alginate/biofilm immune evasion; CF host context |
| Epidemiology / MDR | 41758741, 41877050, 42393552, 41826861, 42523687 | Rank, frequency and resistance burden |
| Treatment | 35022730, 36773112, 36457059, 34600585, 42807670, 42523687 | RCT efficacy (ASPECT-NP); inhaled/CRPA strategies |
| Prognosis | 42707186, 21499086, 18060758 | Resistance and inappropriate therapy raise mortality |
| Prevention | 42415225, 31585480, 28759469, 30390751, 32486132 | Bundle components, incidence |
| Emerging therapy | 42662857, 40961506, 38359491, 41887374, 40595615, 40616692 | mAbs, vaccine, phage, host-directed |

---

## Limitations and Knowledge Gaps

- **No dedicated dataset was analyzed;** this is a literature-synthesis report, so all statistics derive from published cohorts/trials, each with their own design limitations (single-center retrospective series, subgroup analyses, non-inferiority framing).
- **Attribution vs association:** *P. aeruginosa*-attributable mortality is hard to isolate from severe underlying illness; the ~30% VAP figure is not pathogen-specific.
- **Mechanistic data are largely model-organism/in-vitro** (rat, mouse, zebrafish, cell lines). Human causal validation of the TLR5→NLRC4→IL-1β chain is inferential.
- **Host genetics** beyond *CFTR* and inflammasome variants are poorly defined; no robust human GWAS for *P. aeruginosa* pneumonia susceptibility was identified.
- **Emerging therapies** (mAbs, phage, DNA vaccine) rest on preclinical/case-series evidence without phase 3 RCT confirmation.
- **Ontology mappings** (ICD, HPO, GO, CL, UBERON, NCIT) are expert-suggested here and should be curator-verified.

---

## Proposed Follow-up Experiments / Actions

1. **Stratify prognosis by T3SS genotype (exoU vs exoS).** Prospectively test whether *exoU⁺* clinical isolates predict worse ARDS/mortality, linking F001 to human outcomes.
2. **Clinical validation of PcrV-targeted anti-virulence mAbs** in ventilated HABP/VABP RCTs, building on preclinical protection ([PMID: 42662857](https://pubmed.ncbi.nlm.nih.gov/42662857/)).
3. **Controlled trials of inhaled adjunctive antibiotics** for MDR/CRPA VAP with pharmacokinetic/pharmacodynamic endpoints ([PMID: 42807670](https://pubmed.ncbi.nlm.nih.gov/42807670/)).
4. **Phage–immune interaction studies** to define dosing that overcomes macrophage-mediated phage clearance ([PMID: 40595615](https://pubmed.ncbi.nlm.nih.gov/40595615/)).
5. **Biomarker-guided stewardship** using CRP/IL-1β and rapid resistance genotyping to shorten time to appropriate therapy (addresses F007).
6. **Host-directed therapy** targeting the NLRC4 inflammasome / Cmpk2–STING axis to rebalance protective vs damaging inflammation ([PMID: 33489931](https://pubmed.ncbi.nlm.nih.gov/33489931/), [PMID: 40616692](https://pubmed.ncbi.nlm.nih.gov/40616692/)).
7. **Advance OprF/PcrV vaccine** toward first-in-human trials in high-risk ICU/CF populations ([PMID: 38359491](https://pubmed.ncbi.nlm.nih.gov/38359491/)).

---

*Report compiled from 5 investigation iterations, 9 confirmed findings, and 61 reviewed papers. Evidence types span human clinical (surveillance cohorts, ASPECT-NP RCT), model organism (rat/mouse/zebrafish), in-vitro (A549/THP-1/MH-S/HEK293), and computational (multi-omics/GEO) sources.*


## Artifacts

- [OpenScientist final report](Pneumonia_Caused_By_Pseudomonas_Aeruginosa_Infection-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pneumonia_Caused_By_Pseudomonas_Aeruginosa_Infection-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 49 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 49 |
| On topic | 28 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 11 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001945` (1 mention) - the report calls it "Common"; HP calls it **Fever**
- `HP:0012735` (1 mention) - the report calls it "Common"; HP calls it **Cough**
- `HP:0002094` (1 mention) - the report calls it "Common"; HP calls it **Dyspnea**
- `HP:0025440` (1 mention) - the report calls it "Common (VAP)"; HP calls it **Warm reactive autoantibody positivity**
- `HP:0001974` (1 mention) - the report calls it "Common"; HP calls it **Increased total leukocyte count**
- `HP:0011227` (1 mention) - the report calls it "Common (PMID: 42592972)"; HP calls it **Elevated circulating C-reactive protein concentration**
- `HP:0031977` (1 mention) - the report calls it "Diagnostic"; HP calls it **Increased vertical cup-to-disc ratio - 0.9**
- `HP:0033677` (1 mention) - the report calls it "T3SS-driven subset"; HP calls it **Acute respiratory distress syndrome**
- `UBERON:0002048` (1 mention) - the report calls it "Primary organ:** Lung"; UBERON calls it **lung**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.