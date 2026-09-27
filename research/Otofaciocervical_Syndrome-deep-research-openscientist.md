---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-29T10:06:05.068040'
end_time: '2026-08-29T10:34:32.762960'
duration_seconds: 1707.69
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Otofaciocervical Syndrome
  mondo_id: ''
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
citation_count: 25
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMID:8558563
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 41
  verified: 38
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 1
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: MONDO:0008159
    reported_labels:
    - type 1
    ontology_label: postmenopausal osteoporosis
  - term_id: MONDO:0014434
    reported_labels:
    - type 2
    ontology_label: Bardet-Biedl syndrome 5
  - term_id: HP:0000405
    reported_labels:
    - Clinical sign
    ontology_label: Conductive hearing impairment
  - term_id: HP:0000356
    reported_labels:
    - Physical
    ontology_label: Abnormality of the outer ear
  - term_id: HP:0004467
    reported_labels:
    - Physical
    ontology_label: Preauricular pit
  - term_id: HP:0009025
    reported_labels:
    - Physical
    ontology_label: Increased connective tissue
  - term_id: HP:0000218
    reported_labels:
    - Physical
    ontology_label: High palate
  - term_id: HP:0200023
    reported_labels:
    - winged scapula
    ontology_label: Priapism
  - term_id: HP:0000889
    reported_labels:
    - Physical
    ontology_label: Abnormal clavicle morphology
  - term_id: HP:0004322
    reported_labels:
    - Physical
    ontology_label: Short stature
  - term_id: HP:0001256
    reported_labels:
    - Behavioral/cognitive
    ontology_label: Mild intellectual disability
  - term_id: HP:0000829
    reported_labels:
    - Lab
    ontology_label: Hypoparathyroidism
  - term_id: HP:0001627
    reported_labels:
    - Clinical sign
    ontology_label: Abnormal heart morphology
  labels_variant: 2
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
  path: Otofaciocervical_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Otofaciocervical_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Otofaciocervical Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Otofaciocervical Syndrome** covering all of the
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

# Otofaciocervical Syndrome (OFCS / OTFCS): A Comprehensive Disease Characteristics Report

---

## Summary

**Otofaciocervical syndrome (OFCS; also OTFCS)** is a rare congenital malformation disorder of the branchial arches / pharyngeal pouches, arising from disruption of the **PAX–SIX–EYA–DACH developmental network (PSEDN)**. Its cardinal features are facial dysmorphism (long face, narrow nose), external/middle/inner-ear anomalies with predominantly conductive hearing loss, branchial/cervical defects (cervical fistulae, long neck), and a highly characteristic shoulder-girdle and vertebral malformation complex (sloping shoulders, low-set winged scapulae, clavicular anomalies), frequently accompanied by mild intellectual disability and short stature. Clinically it is difficult to separate from the branchiootorenal (BOR) spectrum, and molecular data now indicate the two overlap substantially.

The disease is genetically and mechanistically **bipartite**. **Type 1 (OTFCS1; OMIM 166780)** is **autosomal dominant**, caused by haploinsufficiency of **EYA1** (8q13.3) through point mutations or contiguous-gene microdeletions. **Type 2 (OTFCS2; OMIM 615560)** is **autosomal recessive**, caused by **biallelic loss-of-function or hypofunctional mutations of PAX1** (20p11.22). The two arms diverge sharply in their most consequential complication: the PAX1 (type 2) arm produces a **DiGeorge-like thymic-stromal defect** with thymic aplasia/hypoplasia, severe combined immunodeficiency (SCID) or combined immunodeficiency (CID), hypoparathyroidism, and congenital heart defects, whereas the EYA1 (type 1) arm is now regarded as part of a **single branchiootorenal allelic continuum** in which renal anomalies are effectively obligatory and mandate surveillance.

The mechanistic distinction has direct clinical consequences. Because the OTFCS2 immune defect is **thymic-stromal (epithelial) rather than hematopoietic-cell-intrinsic**, it is not corrected by hematopoietic stem cell transplantation (HSCT); the definitive therapy is **cultured thymus tissue transplantation (CTTI)**, which restores a diverse naïve T-cell repertoire. Otherwise, management is genotype-specific supportive care: hearing rehabilitation, branchial-fistula/cervical surgery, and organ-specific surveillance (renal in the EYA1 arm; parathyroid, cardiac, and immune in the PAX1 arm). This report synthesizes findings across the PSEDN literature, primary case series, and functional/model-organism studies, and flags the substantial knowledge gaps that remain for this ultra-rare condition (fewer than ~10 reported OTFCS2 families worldwide).

---

## Key Findings

### Finding 1 — Two genetic subtypes with distinct inheritance (EYA1/AD vs PAX1/AR)

Otofaciocervical syndrome is not a single-gene disorder. It comprises **two molecularly and clinically distinguishable subtypes**:

- **OTFCS1 (OMIM 166780)** — **autosomal dominant**, caused by heterozygous point mutations or deletions of **EYA1** at chromosome **8q13.3**.
- **OTFCS2 (OMIM 615560)** — **autosomal recessive**, caused by **biallelic PAX1** (chromosome **20p11.22**) loss-of-function or hypofunctional variants.

This dual architecture is stated explicitly in the recent literature: *"It is caused by biallelic or monoallelic mutations in PAX1 or EYA1 genes, respectively"* ([PMID: 37924468](https://pubmed.ncbi.nlm.nih.gov/37924468/)). Reported PAX1 variants span the mutational spectrum, including the hypofunctional missense **c.497G>T (p.Gly166Val)** — *"identified only a single novel homozygous variant, c.497G>T, located in PAX1 that co-segregated with the disease"* ([PMID: 23851939](https://pubmed.ncbi.nlm.nih.gov/23851939/)) — nonsense/null alleles ([PMID: 28657137](https://pubmed.ncbi.nlm.nih.gov/28657137/)), and frameshifts such as **c.1212dup (p.Gly405Argfs\*51)** ([PMID: 37924468](https://pubmed.ncbi.nlm.nih.gov/37924468/)). OTFCS2 remains ultra-rare, with fewer than ~10 families reported worldwide.

### Finding 2 — Biallelic null PAX1 causes thymic aplasia and SCID (OTFCS2)

PAX1 is essential for the development of the pharyngeal-pouch-derived **thymic epithelium**. Biallelic null PAX1 mutations therefore produce **thymic aplasia/hypoplasia** and profound impairment of T-cell immunity (SCID/CID), which is lethal if untreated: *"bi-allelic null PAX1 mutations may lead to a multi-system autosomal recessive disorders, where SCID might represent the main feature"* ([PMID: 28657137](https://pubmed.ncbi.nlm.nih.gov/28657137/)). The underlying developmental role is confirmed by the observation that *"PAX1 is essential for development and function of the human thymus"* ([PMID: 32111619](https://pubmed.ncbi.nlm.nih.gov/32111619/)).

Critically, the immune lesion is a defect of the **thymic stroma, not of the hematopoietic progenitor**. In a cohort of six OTFCS2 patients, HSCT gave **poor immune reconstitution** with absent naïve T cells, whereas **thymus transplantation restored T-cell immunity**: *"Hematopoietic stem cell transplantation resulted in poor immune reconstitution with absent naïve T cells, contrasting with the superior recovery of T cell immunity after thymus transplantation"* ([PMID: 37689091](https://pubmed.ncbi.nlm.nih.gov/37689091/)).

### Finding 3 — PAX1 mechanism: repression of canonical Wnt signaling

PAX1 is a paired-box transcription factor that functions, in part, by **repressing canonical Wnt/β-catenin signaling**. It does so by competing with the SUMO E3 ligase PIASy for binding to **TCF7L2**, thereby reducing TCF7L2 SUMOylation, transcriptional activity, and stability: *"we show that PAX1 represses canonical Wnt signaling pathway in vertebrate cells"* and *"PAX1 competes with SUMO E3 ligase PIASy to bind to TCF7L2, thus perturbing TCF7L2 SUMOylation level"* ([PMID: 38664733](https://pubmed.ncbi.nlm.nih.gov/38664733/)). PAX1 plays dual roles in hESC-derived definitive and foregut/pharyngeal endoderm, the lineages that give rise to thymic epithelium. In mouse, Pax1 directly transactivates the *Nkx3-2* promoter, and the OFCS G166V mutant shows reduced transactivation/DNA-binding ([PMID: 23851939](https://pubmed.ncbi.nlm.nih.gov/23851939/)). Mouse *Pax1* loss (the classic *undulated* allele) causes vertebral/skeletal and thymic defects, recapitulating the human skeletal and immune phenotypes.

### Finding 4 — EYA1 mechanism: haploinsufficiency within the EYA1–SIX1 network; loss of induction and apoptosis of primordia

**EYA1** encodes a transcriptional **co-activator/phosphatase** with a conserved C-terminal **Eya Domain** (271 amino acids) that partners with **SIX1** DNA-binding transcription factors: *"EYA1, a transcriptional co-activator has a conserved, 271-amino acid, C-terminal known as the Eya Domain"* ([PMID: 17238186](https://pubmed.ncbi.nlm.nih.gov/17238186/)). Haploinsufficiency causes dominant branchiootorenal/branchiootic syndrome and the allelic OTFCS1. The developmental mechanism is defined by the mouse knockout: *"Eya1 homozygotes lack ears and kidneys due to defective inductive tissue interactions and apoptotic regression of the organ primordia"* ([PMID: 10471511](https://pubmed.ncbi.nlm.nih.gov/10471511/)), with inner-ear arrest at the otic-vesicle stage and Six (not Pax) expression being Eya1-dependent. These genes *"act within a genetic network of EYA and PAX genes to regulate organogenesis"* ([PMID: 15141091](https://pubmed.ncbi.nlm.nih.gov/15141091/)). Eya1 cofactors Sipl1/Rbck1 enhance Six coactivation; their knockdown produces BOR-like ear/branchial-arch defects in zebrafish ([PMID: 20956555](https://pubmed.ncbi.nlm.nih.gov/20956555/)).

### Finding 5 — EYA1-related OTFCS and BOR spectrum form a single allelic continuum; renal anomalies are present

A 2025 integrated literature analysis of all published EYA1-related disorders (plus a novel de novo 8q13.2q13.3 microdeletion case) concluded that *"all EYA1 variant types (truncating, missense, CNV, etc.) can cause BORSD, OTFCS, or hybrid phenotypes, firmly supporting their status as allelic disorders"* and — revising a long-standing assumption — that *"all reported OTFCS patients with EYA1 variants had renal anomalies, a feature previously considered a hallmark of BORSD"*, such that *"BORSD and OTFCS constitute a single EYA1-related diagnostic continuum"* ([PMID: 41300719](https://pubmed.ncbi.nlm.nih.gov/41300719/)). This mandates integrated renal, otologic, and skeletal surveillance in EYA1-positive patients. (Note: historically, sporadic OFCS cases were "split" from BOR on the basis of absent renal malformations — [PMID: 8558563](https://pubmed.ncbi.nlm.nih.gov/8558563/) — so the reclassification represents a genuine update.)

### Finding 6 — PAX1 deficiency shows DiGeorge-overlapping features and a thymic-stromal (not hematopoietic-intrinsic) defect

In six PAX1-deficient OTFCS2 patients, features overlapping DiGeorge syndrome included **primary hypoparathyroidism (5/6)** and **congenital heart defects (2/6)**: *"New overlapping features with DiGeorge syndrome included primary hypoparathyroidism"* ([PMID: 37689091](https://pubmed.ncbi.nlm.nih.gov/37689091/)). Penetrance was variable, and 4/6 required corrective treatment. The hematopoietic compartment is intact — *"Normal ex vivo differentiation of PAX1-deficient CD34[+ cells into mature T cells]"* ([PMID: 37689091](https://pubmed.ncbi.nlm.nih.gov/37689091/)) — confirming the lesion is thymic-stromal. Patient-derived iPSCs differentiated into thymic epithelial progenitor cells show an altered transcriptional profile for thymus/pharyngeal-pouch genes; mutant PAX1 proteins have altered paired-box-domain conformation/flexibility and reduced transcriptional activity, establishing *"biallelic, loss-of-function PAX1 mutations as the cause of a syndromic form of SCID due to altered thymus development"* ([PMID: 32111619](https://pubmed.ncbi.nlm.nih.gov/32111619/)).

### Finding 7 — Integrated synthesis: a two-arm PSEDN branchial-arch disorder

Integrating all evidence, OFCS is a **two-gene PSEDN branchial-arch disorder** with an **EYA1 (BOR-continuum) arm** and a **PAX1 (DiGeorge-like, thymus-treatable) arm**. The EYA1 arm acts via loss of EYA1–SIX1 co-activation → failed inductive signaling and apoptotic regression of otic/branchial/renal primordia. The PAX1 arm is a pharyngeal-pouch field defect driven by loss of PAX1-mediated Wnt repression → abnormal thymic-epithelial development → SCID/CID, hypoparathyroidism, and cardiac defects, correctable by cultured thymus tissue transplantation rather than HSCT ([PMID: 37689091](https://pubmed.ncbi.nlm.nih.gov/37689091/), [PMID: 34362576](https://pubmed.ncbi.nlm.nih.gov/34362576/)).

---

## Mechanistic Model / Interpretation

The two arms of OFCS both funnel through the PAX–SIX–EYA–DACH network but at different nodes and with opposite inheritance logic (dominant haploinsufficiency vs recessive loss of function).

```
                    PAX–SIX–EYA–DACH developmental network (PSEDN)
                    (patterns branchial arches / pharyngeal pouches)
                                        │
          ┌─────────────────────────────┴──────────────────────────────┐
          │                                                             │
   EYA1 (8q13.3)                                                  PAX1 (20p11.22)
   autosomal DOMINANT                                           autosomal RECESSIVE
   haploinsufficiency                                        biallelic LOF / hypofunction
          │                                                             │
   loss of EYA1–SIX1                                        loss of PAX1-mediated
   transcriptional co-activation                           canonical Wnt repression
   (Eya Domain + SIX1 DNA binding)                         (PAX1 vs PIASy for TCF7L2;
          │                                                  ↓ TCF7L2 SUMOylation)
   failed inductive tissue                                            │
   interactions + APOPTOTIC                                abnormal foregut/pharyngeal
   regression of organ primordia                          endoderm → thymic epithelium
          │                                                            │
   ┌──────┴───────┐                                        ┌───────────┴───────────┐
   ear/otic       renal                                  thymic aplasia    parathyroid /
   branchial      primordia                              → SCID / CID      cardiac field
   arch defects   (→ renal anomalies)                    (thymic-STROMAL,   defects
   + skeletal     ← now obligatory                        NOT hematopoietic) (DiGeorge-like)
   (scapula/                                                     │
   clavicle)                                              CORRECTED by cultured
          │                                               thymus tissue transplant,
   OTFCS1 = EYA1 / BOR continuum                          NOT by HSCT
          │                                                     │
          └──────── shared: facial dysmorphism, ear ─────────── OTFCS2 = PAX1 /
                    anomalies + hearing loss, cervical           DiGeorge-like
                    /branchial defects, vertebral + shoulder-
                    girdle malformation, mild intellectual
                    disability, short stature
```

### Comparison of the two subtypes

| Feature | OTFCS1 (EYA1) | OTFCS2 (PAX1) |
|---|---|---|
| OMIM | 166780 | 615560 |
| Gene / locus | *EYA1* / 8q13.3 | *PAX1* / 20p11.22 |
| Inheritance | Autosomal dominant | Autosomal recessive |
| Protein class | Transcriptional co-activator / phosphatase (Eya Domain; SIX1 partner) | Paired-box transcription factor (Wnt repressor) |
| Core mechanism | Loss of EYA1–SIX1 co-activation → failed induction + apoptosis of primordia | Loss of Wnt repression → abnormal thymic-epithelial development |
| Renal anomalies | Present (BOR continuum; surveillance mandatory) | Not the defining feature |
| Immune phenotype | Not characteristic | Thymic aplasia → SCID/CID (thymic-stromal) |
| DiGeorge overlap | No | Yes (hypoparathyroidism 5/6; CHD 2/6) |
| Definitive immune therapy | N/A | Cultured thymus tissue transplantation (not HSCT) |
| Key PMIDs | 17238186, 10471511, 15141091, 41300719 | 23851939, 28657137, 32111619, 37689091, 38664733 |

The unifying interpretation is that **both genes are required for the correct morphogenesis of pharyngeal-arch and otic-placode derivatives**, but EYA1 haploinsufficiency biases toward the ear–renal–skeletal (BOR-like) axis via apoptosis of primordia, whereas complete PAX1 loss additionally collapses the third/fourth pharyngeal-pouch thymic-epithelial and parathyroid program, producing a DiGeorge-like immuno-endocrine phenotype. This explains why the two arms share the otofaciocervical core but diverge in their life-threatening complications and their treatment.

---

## Report by Section

### 1. Disease Information
- **Overview:** Rare congenital branchial-arch (pharyngeal-pouch) malformation syndrome of the PSEDN, characterized by facial dysmorphism, external/middle/inner-ear anomalies with hearing loss, branchial/cervical defects, shoulder-girdle (sloping shoulders, low-set winged scapulae, clavicular anomalies) and vertebral malformations, short stature, and mild intellectual disability ([PMID: 27240490](https://pubmed.ncbi.nlm.nih.gov/27240490/), [PMID: 8558563](https://pubmed.ncbi.nlm.nih.gov/8558563/)).
- **Key identifiers:** OMIM **166780** (OTFCS1) and **615560** (OTFCS2); Orphanet ORPHA:2792 (Otofaciocervical syndrome); MeSH — no dedicated descriptor (indexed under branchial-region/first-arch anomalies); MONDO — MONDO:0008159 (type 1) / MONDO:0014434 (type 2) suggested.
- **Synonyms:** Otofaciocervical syndrome; OFC syndrome; OTFCS; Fara-Chlupackova syndrome (historical); OTFCS1 / OTFCS2 for the two genetic types.
- **Data source:** Derived from **aggregated disease-level resources** (OMIM, Orphanet) plus **individual case reports/small series** — there is no EHR-scale cohort; fewer than ~10 OTFCS2 families are reported.

### 2. Etiology
- **Causal factors:** Purely **genetic/Mendelian.** No environmental or infectious cause. Two genes: **EYA1** (dominant, haploinsufficiency) and **PAX1** (recessive, biallelic LOF) ([PMID: 37924468](https://pubmed.ncbi.nlm.nih.gov/37924468/)).
- **Genetic risk factors:** Causal variants in EYA1 (truncating, missense, CNV/microdeletion) and PAX1 (missense hypofunctional e.g. p.G166V, nonsense null, frameshift). No established human modifier loci; in mouse, the *kkt* locus is a closely linked modifier of the *Pax1* skeletal phenotype ([PMID: 10656775](https://pubmed.ncbi.nlm.nih.gov/10656775/)).
- **Environmental risk factors:** None identified. **Consanguinity** is a strong contributor to OTFCS2 (recessive) — several families are consanguineous ([PMID: 35595062](https://pubmed.ncbi.nlm.nih.gov/35595062/)).
- **Protective factors:** None described (no data).
- **Gene–environment interactions:** None established.

### 3. Phenotypes

| Phenotype | Type | HPO term (suggested) | Frequency / notes |
|---|---|---|---|
| Conductive hearing loss | Clinical sign | HP:0000405 | Common; from middle/inner-ear malformation |
| External ear malformation / dysmorphic ears | Physical | HP:0000356 | Characteristic |
| Inner-ear / cochlear malformation | Imaging/sign | HP:0011389 / HP:0000375 | e.g. cochlear malformation ([PMID: 8558563](https://pubmed.ncbi.nlm.nih.gov/8558563/)) |
| Preauricular pits (variable; more BOR-typical) | Physical | HP:0004467 | Variable |
| Branchial/cervical fistula or cyst | Physical | HP:0009025 | Present in original family; "otofaciocervical" |
| Long face / narrow nose | Physical | HP:0000276 / HP:0000460 | Facial dysmorphism |
| High-arched palate | Physical | HP:0000218 | Reported |
| Sloping shoulders, low-set winged scapulae | Physical | HP:0200023 (winged scapula) | **Distinctive** shoulder-girdle feature |
| Clavicular anomalies | Physical | HP:0000889 | Distinctive of OFCS |
| Vertebral anomalies | Physical | HP:0003468 / HP:0000925 | Common |
| Short stature | Physical | HP:0004322 | Reported ([PMID: 35595062](https://pubmed.ncbi.nlm.nih.gov/35595062/)) |
| Mild intellectual disability | Behavioral/cognitive | HP:0001256 | Mild, variable |
| Thymic aplasia/hypoplasia → SCID/CID | Lab/immune | HP:0010515 / HP:0004430 | **OTFCS2 only** |
| Primary hypoparathyroidism | Lab | HP:0000829 | 5/6 OTFCS2 ([PMID: 37689091](https://pubmed.ncbi.nlm.nih.gov/37689091/)) |
| Congenital heart defect (e.g. TOF) | Clinical sign | HP:0001627 | 2/6 OTFCS2; TOF also in one OTFCS1 case ([PMID: 8558563](https://pubmed.ncbi.nlm.nih.gov/8558563/)) |
| Renal anomalies | Imaging/sign | HP:0000077 / HP:0000107 | Reported in EYA1-related OTFCS ([PMID: 41300719](https://pubmed.ncbi.nlm.nih.gov/41300719/)) |

- **Onset:** Congenital. Immunodeficiency presents in the **neonatal period** (OTFCS2). **Severity** ranges mild→severe/lethal (SCID). **Progression** of malformations is stable/non-progressive; hearing loss may be stable. **Expressivity is highly variable** ([PMID: 27240490](https://pubmed.ncbi.nlm.nih.gov/27240490/), [PMID: 35879406](https://pubmed.ncbi.nlm.nih.gov/35879406/)).
- **Quality of life:** Driven by hearing loss (communication/education), skeletal deformity, and — in OTFCS2 — recurrent life-threatening infections. No formal EQ-5D/SF-36 data exist for this ultra-rare disease.

### 4. Genetic / Molecular Information
- **Causal genes:** **EYA1** (HGNC:3519; OMIM 601653; 8q13.3) and **PAX1** (HGNC:8615; OMIM 167411; 20p11.22).
- **Pathogenic variants:**
  - *PAX1:* c.497G>T p.Gly166Val (hypofunctional missense, [PMID: 23851939](https://pubmed.ncbi.nlm.nih.gov/23851939/)); homozygous null/nonsense ([PMID: 28657137](https://pubmed.ncbi.nlm.nih.gov/28657137/)); frameshift c.1212dup p.Gly405Argfs\*51 ([PMID: 37924468](https://pubmed.ncbi.nlm.nih.gov/37924468/)); novel homozygous small insertion ([PMID: 29681087](https://pubmed.ncbi.nlm.nih.gov/29681087/)). A heterozygous frameshift null allele can also cause a milder dominant oculo-auriculo-vertebral (OAVS) phenotype ([PMID: 35879406](https://pubmed.ncbi.nlm.nih.gov/35879406/)).
  - *EYA1:* truncating, missense, splice-site, and CNV/microdeletion; all types can cause BORSD/OTFCS/hybrid ([PMID: 41300719](https://pubmed.ncbi.nlm.nih.gov/41300719/)); e.g. splice-site c.1475+1G>C in BOR ([PMID: 23506628](https://pubmed.ncbi.nlm.nih.gov/23506628/)).
- **Classification:** Reported alleles are ACMG **pathogenic/likely pathogenic**; recessive variants require biallelic status. Allele frequencies in gnomAD are rare/absent (consistent with severity/rarity).
- **Origin:** **Germline.** Functional consequence: **loss of function** for both genes (EYA1 haploinsufficiency; PAX1 biallelic LOF/hypofunction). No gain-of-function.
- **Modifier genes:** Human — none confirmed; mouse — *kkt* modifies *Pax1* ([PMID: 10656775](https://pubmed.ncbi.nlm.nih.gov/10656775/)).
- **Epigenetics:** No disease-specific methylation/chromatin data. (PAX1 promoter methylation is a cervical-cancer biomarker but unrelated to OFCS — [PMID: 27705080](https://pubmed.ncbi.nlm.nih.gov/27705080/).)
- **Chromosomal abnormalities:** Contiguous-gene **microdeletions** at 8q13 (EYA1) cause OTFCS1; a familial 6q23 deletion including *EYA4* has been associated with an OTFCS-like phenotype ([PMID: 31379922](https://pubmed.ncbi.nlm.nih.gov/31379922/)).

### 5. Environmental Information
No environmental, lifestyle, or infectious etiologic factors. **Not applicable** — the disease is monogenic. (Infections in OTFCS2 are opportunistic *consequences* of immunodeficiency, not causes.)

### 6. Mechanism / Pathophysiology
- **Molecular pathways:** PAX1 arm — **canonical Wnt/β-catenin** repression via PAX1–PIASy competition for TCF7L2 SUMOylation ([PMID: 38664733](https://pubmed.ncbi.nlm.nih.gov/38664733/)). EYA1 arm — **EYA1–SIX1 transcriptional co-activation** (PSEDN organogenesis network) ([PMID: 15141091](https://pubmed.ncbi.nlm.nih.gov/15141091/)). Suggested GO: GO:0060070 (canonical Wnt signaling), GO:0006357 (regulation of transcription by Pol II), GO:0048704 (embryonic skeletal system morphogenesis).
- **Cellular processes:** Defective inductive tissue interactions and **apoptotic regression of organ primordia** (GO:0006915 apoptotic process) in the EYA1 arm ([PMID: 10471511](https://pubmed.ncbi.nlm.nih.gov/10471511/)); failed thymic-epithelial specification/differentiation in the PAX1 arm ([PMID: 32111619](https://pubmed.ncbi.nlm.nih.gov/32111619/)).
- **Protein dysfunction:** EYA1 — loss of Eya Domain co-activator/phosphatase function ([PMID: 17238186](https://pubmed.ncbi.nlm.nih.gov/17238186/)); PAX1 — altered paired-box-domain conformation/flexibility, reduced DNA binding and transactivation (e.g. of *Nkx3-2*) ([PMID: 23851939](https://pubmed.ncbi.nlm.nih.gov/23851939/), [PMID: 32111619](https://pubmed.ncbi.nlm.nih.gov/32111619/)).
- **Immune involvement:** **Immunodeficiency** (thymic-stromal SCID/CID) in OTFCS2; hematopoietic compartment intact ([PMID: 37689091](https://pubmed.ncbi.nlm.nih.gov/37689091/)).
- **Transcriptomics:** iPSC-derived thymic epithelial progenitors from OTFCS2 patients show altered expression of thymus/pharyngeal-pouch genes ([PMID: 32111619](https://pubmed.ncbi.nlm.nih.gov/32111619/)).
- **Cell types (CL):** thymic epithelial cell (CL:0002293), neural crest-derived pharyngeal mesenchyme, otic placode/vesicle cells, chondrocytes (skeletal). GO cellular component: nucleus (GO:0005634).

### 7. Anatomical Structures Affected
- **Organ level (primary):** ear (external/middle/inner; UBERON:0001690), neck/branchial apparatus (UBERON:0000974), shoulder girdle — scapula (UBERON:0006849), clavicle (UBERON:0001105), vertebral column (UBERON:0001130), thymus (UBERON:0002370, OTFCS2), parathyroid gland (UBERON:0001132, OTFCS2), heart (UBERON:0000948), kidney (UBERON:0002113, EYA1 arm).
- **Body systems:** auditory, musculoskeletal, immune, endocrine (parathyroid), cardiovascular, renal.
- **Tissue/cell level:** epithelial (thymic/pharyngeal-pouch), connective/cartilage (skeletal), neural-crest derivatives.
- **Subcellular:** nucleus (transcription factors EYA1/SIX1/PAX1).
- **Localization:** **bilateral** ear and skeletal involvement typical.

### 8. Temporal Development
- **Onset:** **Congenital**; immunodeficiency manifests **neonatally** (OTFCS2). Onset pattern is developmental/insidious for malformations, potentially acute for infection.
- **Progression:** Structural malformations are **stable/non-progressive**; hearing loss generally stable. Untreated OTFCS2 SCID is **rapidly life-threatening** in infancy.
- **Course/duration:** Chronic, lifelong. **Critical period** for OTFCS2 is early infancy — timely recognition of the thymic defect and thymus transplantation before fatal infection ([PMID: 33815417](https://pubmed.ncbi.nlm.nih.gov/33815417/), [PMID: 34362576](https://pubmed.ncbi.nlm.nih.gov/34362576/)).

### 9. Inheritance and Population
- **Epidemiology:** Prevalence unknown; **<1/1,000,000** (Orphanet "unknown"). OTFCS2: fewer than ~10 families reported ([PMID: 35595062](https://pubmed.ncbi.nlm.nih.gov/35595062/)).
- **Inheritance:** OTFCS1 **autosomal dominant** (EYA1); OTFCS2 **autosomal recessive** (PAX1).
- **Penetrance/expressivity:** Highly **variable expressivity**; full penetrance reported for a PAX1 null allele with variable facial/ear expressivity ([PMID: 35879406](https://pubmed.ncbi.nlm.nih.gov/35879406/)).
- **Consanguinity:** Major factor for OTFCS2 (recessive); several homozygous cases from consanguineous unions ([PMID: 35595062](https://pubmed.ncbi.nlm.nih.gov/35595062/), [PMID: 29681087](https://pubmed.ncbi.nlm.nih.gov/29681087/)).
- **Founder effects / carrier frequency / sex ratio:** No established founder mutation; carrier frequency not determined; no clear sex bias. Anticipation and germline mosaicism: not reported.

### 10. Diagnostics
- **Clinical/lab:** Immune workup for OTFCS2 — low/absent naïve T cells, **abnormal newborn TREC screen** (low T-cell receptor excision circles) flags athymia ([PMID: 32431714](https://pubmed.ncbi.nlm.nih.gov/32431714/), [PMID: 33815417](https://pubmed.ncbi.nlm.nih.gov/33815417/)); serum calcium/PTH (hypoparathyroidism).
- **Imaging:** Temporal-bone CT (cochlear/inner-ear malformation), skeletal radiographs (scapula/clavicle/vertebrae), renal ultrasound (EYA1 arm), echocardiography (CHD), thymic imaging.
- **Audiology:** Formal hearing assessment (conductive loss).
- **Genetic testing:** **WES/WGS or gene-agnostic trio exome** is the recommended, high-yield approach — panel testing may miss cases ([PMID: 35595062](https://pubmed.ncbi.nlm.nih.gov/35595062/)); **chromosomal microarray/CMA** to detect EYA1 (8q13) or contiguous deletions; single-gene/targeted testing of **EYA1** and **PAX1** confirmed by ClinVar/OMIM.
- **Clinical criteria & differential diagnosis:** Distinguish from **branchiootorenal (BOR) syndrome** (now overlapping continuum for EYA1), **DiGeorge/22q11.2 deletion**, **CHARGE**, **Nude/FOXN1 SCID**, and **oculo-auriculo-vertebral spectrum (OAVS)** ([PMID: 32431714](https://pubmed.ncbi.nlm.nih.gov/32431714/), [PMID: 35595062](https://pubmed.ncbi.nlm.nih.gov/35595062/)).
- **Screening:** Newborn TREC screening is key for early detection of the OTFCS2 immune defect ([PMID: 33815417](https://pubmed.ncbi.nlm.nih.gov/33815417/)).

### 11. Outcome / Prognosis
- **OTFCS1 (EYA1):** Generally compatible with normal lifespan; morbidity from hearing loss, skeletal deformity, and renal anomalies (surveillance-dependent).
- **OTFCS2 (PAX1):** Prognosis dominated by **SCID** — high early mortality if untreated. With **cultured thymus tissue transplantation**, Kaplan–Meier survival in congenital athymia cohorts is ~**77% at 1 year and 76% at 2 years** ([PMID: 34362576](https://pubmed.ncbi.nlm.nih.gov/34362576/)); most deaths occur before immune reconstitution (6–12 months post-CTTI) and are infection-related. HSCT gives poorer immune reconstitution for this stromal defect ([PMID: 37689091](https://pubmed.ncbi.nlm.nih.gov/37689091/)).
- **Complications:** Recurrent/opportunistic infections (incl. disseminated NTM in athymia — [PMID: 36860874](https://pubmed.ncbi.nlm.nih.gov/36860874/)), autoimmunity/immune dysregulation, hypocalcemia (hypoparathyroidism), cardiac complications.
- **Prognostic factors:** Genotype (PAX1 null → SCID), timing of thymus transplant, pre-transplant infection burden.

### 12. Treatment
- **Definitive (OTFCS2 immune):** **Cultured thymus tissue transplantation / implantation (CTTI)** — restores diverse naïve T cells; superior to HSCT for thymic-stromal defects ([PMID: 37689091](https://pubmed.ncbi.nlm.nih.gov/37689091/), [PMID: 34362576](https://pubmed.ncbi.nlm.nih.gov/34362576/), [PMID: 33815417](https://pubmed.ncbi.nlm.nih.gov/33815417/)). Suggested NCIT: Thymus Transplantation. Non-conditioned cord-blood HCT can serve as **bridging** infection control in athymia ([PMID: 38078568](https://pubmed.ncbi.nlm.nih.gov/38078568/)).
- **Supportive:** Anti-infective prophylaxis and immunoglobulin (pre-reconstitution); calcium/vitamin-D management for hypoparathyroidism; cardiac management (CHD); audiologic rehabilitation (hearing aids/cochlear implantation as indicated); surgical repair of branchial/cervical fistulae and cardiac defects; orthopedic/PT management of skeletal deformity; speech and educational support.
- **Pharmacogenomics / gene therapy / RNA therapy:** None specific/approved.
- **Experimental:** Engineered/organoid thymus tissue is under development ([PMID: 33815417](https://pubmed.ncbi.nlm.nih.gov/33815417/)).

### 13. Prevention
- **Primary:** No population prevention (monogenic). **Genetic counseling** — recessive 25% recurrence risk (OTFCS2); dominant 50% (OTFCS1); counsel consanguineous families.
- **Secondary:** **Newborn TREC screening** enables pre-symptomatic detection of athymia and timely thymus transplantation ([PMID: 33815417](https://pubmed.ncbi.nlm.nih.gov/33815417/)). Carrier/cascade testing and prenatal/preimplantation genetic diagnosis available once the familial variant is known.
- **Tertiary:** Infection prophylaxis, organ-specific surveillance (renal, parathyroid, cardiac, audiologic).

### 14. Other Species / Natural Disease
- **Taxonomy:** *Mus musculus* (NCBI:txid10090), *Danio rerio* (NCBI:txid7955) used as models; no reported spontaneous companion-animal/wildlife OFCS.
- **Orthologs:** mouse *Eya1* (NCBI Gene 14048), mouse *Pax1* (NCBI Gene 18503); zebrafish *eya1*, *pax1a/b*.
- **Natural disease / OMIA:** No specific naturally occurring animal OFCS entry established; the classic mouse *undulated* (*Pax1*) allele is a spontaneous/induced model, not a naturally circulating veterinary disease.
- **Conservation:** PSEDN and PAX1's role in skeleton and thymus are evolutionarily conserved across mouse and zebrafish ([PMID: 20956555](https://pubmed.ncbi.nlm.nih.gov/20956555/), [PMID: 32431714](https://pubmed.ncbi.nlm.nih.gov/32431714/)). Not zoonotic.

### 15. Model Organisms
- **Mouse:** *Eya1* knockout — heterozygotes model BOR (conductive hearing loss, renal anomalies), homozygotes lack ears/kidneys with apoptosis of primordia ([PMID: 10471511](https://pubmed.ncbi.nlm.nih.gov/10471511/)); *Pax1* *undulated* — vertebral/skeletal and thymic defects (recapitulates skeletal + immune arms); *kkt* insertional mutant — closely linked *Pax1* skeletal modifier ([PMID: 10656775](https://pubmed.ncbi.nlm.nih.gov/10656775/)). Resource: MGI.
- **Zebrafish:** *eya1* and cofactor *sipl1/rbck1* morphants — BOR-like ear/branchial-arch defects ([PMID: 20956555](https://pubmed.ncbi.nlm.nih.gov/20956555/)). Resource: ZFIN.
- **In vitro / iPSC:** Patient-derived iPSC → thymic epithelial progenitor differentiation models the OTFCS2 thymic-stromal defect ([PMID: 32111619](https://pubmed.ncbi.nlm.nih.gov/32111619/)); hESC endoderm differentiation reveals PAX1's dual role and Wnt repression ([PMID: 38664733](https://pubmed.ncbi.nlm.nih.gov/38664733/)).
- **Recapitulation/limitations:** Models capture skeletal, otic, renal, and thymic phenotypes well; human facial dysmorphism and mild intellectual disability are less directly modeled.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [37924468](https://pubmed.ncbi.nlm.nih.gov/37924468/) | *Novel truncating PAX1 mutation causes OTFCS without immunodeficiency* | Anchors two-gene architecture; PAX1 frameshift; phenotype variability |
| [23851939](https://pubmed.ncbi.nlm.nih.gov/23851939/) | *Hypofunctional PAX1 mutation causes AR OTFCS* | First PAX1 causation; p.G166V hypofunctional; *Nkx3-2* transactivation |
| [28657137](https://pubmed.ncbi.nlm.nih.gov/28657137/) | *Novel PAX1 null homozygous mutation with SCID* | Biallelic null → SCID as main feature |
| [32111619](https://pubmed.ncbi.nlm.nih.gov/32111619/) | *PAX1 essential for human thymus* | Thymic-stromal mechanism; iPSC-TEC transcriptomics; LOF → SCID |
| [37689091](https://pubmed.ncbi.nlm.nih.gov/37689091/) | *Expanding PAX1-deficient SCID/CID phenotypes* | DiGeorge overlap (hypoPTH 5/6, CHD 2/6); thymus transplant > HSCT; normal CD34+ differentiation |
| [38664733](https://pubmed.ncbi.nlm.nih.gov/38664733/) | *PAX1 represses canonical Wnt* | Core PAX1 molecular mechanism (PIASy/TCF7L2 SUMOylation) |
| [17238186](https://pubmed.ncbi.nlm.nih.gov/17238186/) | *Branchio-oto-renal syndrome* | EYA1 protein / Eya Domain / SIX1 partnership |
| [10471511](https://pubmed.ncbi.nlm.nih.gov/10471511/) | *Eya1-deficient mice* | EYA1 developmental mechanism: induction failure + apoptosis |
| [15141091](https://pubmed.ncbi.nlm.nih.gov/15141091/) | *SIX1 mutations cause BOR* | EYA1–SIX1–DNA complex; EYA/PAX network |
| [20956555](https://pubmed.ncbi.nlm.nih.gov/20956555/) | *Sipl1/Rbck1 Eya1-binding proteins* | EYA1 cofactors; zebrafish BOR-like defects |
| [41300719](https://pubmed.ncbi.nlm.nih.gov/41300719/) | *OTFCS overlap with BOR spectrum (2025)* | Allelic continuum; renal anomalies in EYA1-OTFCS |
| [34362576](https://pubmed.ncbi.nlm.nih.gov/34362576/) | *Cultured thymus tissue in 105 children* | CTTI survival (~77%/1yr); athymia treatment |
| [33815417](https://pubmed.ncbi.nlm.nih.gov/33815417/) | *Therapy for thymic stromal cell defects* | OTFCS2 among athymia; TREC screening; thymus transplant not HSCT |
| [32431714](https://pubmed.ncbi.nlm.nih.gov/32431714/) | *Thymic hypoplasia animal models* | Differential dx (DiGeorge/CHARGE/Nude); TREC |
| [35595062](https://pubmed.ncbi.nlm.nih.gov/35595062/) | *PAX1 OTFCS2 differential diagnosis* | <5 families; trio exome utility; consanguinity |
| [29681087](https://pubmed.ncbi.nlm.nih.gov/29681087/) | *Novel PAX1 insertion OTFCS2* | Third family; WES diagnosis |
| [35879406](https://pubmed.ncbi.nlm.nih.gov/35879406/) | *Dominant PAX1 variant → OAVS* | Monoallelic PAX1 milder phenotype; expressivity |
| [8558563](https://pubmed.ncbi.nlm.nih.gov/8558563/) | *Sporadic OFCS supports splitting from BOR* | Historical clinical phenotype; TOF; splitting debate |
| [27240490](https://pubmed.ncbi.nlm.nih.gov/27240490/) | *OFCS + metachondromatosis* | Variable expressivity; clavicle/scapula distinctive |
| [31379922](https://pubmed.ncbi.nlm.nih.gov/31379922/) | *6q23 deletion incl. EYA4 with OTFCS* | Additional locus/CNV; genetic heterogeneity |
| [23506628](https://pubmed.ncbi.nlm.nih.gov/23506628/) | *BOR with EYA1 splice mutation + FSGS* | EYA1 splice variant; renal pathology |
| [10656775](https://pubmed.ncbi.nlm.nih.gov/10656775/) | *kkt modifier of Pax1* | Mouse skeletal modifier; model |
| [38078568](https://pubmed.ncbi.nlm.nih.gov/38078568/) | *Non-conditioned CBT in athymic CHARGE* | Bridging HCT for athymia infection control |
| [36860874](https://pubmed.ncbi.nlm.nih.gov/36860874/) | *NTM in complete DiGeorge* | Complication spectrum of athymia post-CTTI |
| [27705080](https://pubmed.ncbi.nlm.nih.gov/27705080/) | *Pax1/PAX1 monoclonal antibodies* | Reagent; PAX1 in skeleton/thymus; methylation-marker context |

**Evidence source types:** human clinical case reports/series (OTFCS1/2 families, thymus-transplant cohorts), model organism (mouse *Eya1*/*Pax1*, zebrafish), and in vitro/computational (iPSC-TEC transcriptomics, hESC endoderm Wnt assays, protein-structure modeling).

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity.** OTFCS2 has fewer than ~10 reported families; OTFCS1 case numbers are also small. All frequency, penetrance, and prognosis estimates are based on case reports/series, not population cohorts. There are **no formal quality-of-life (EQ-5D/SF-36) or natural-history registry data.**
2. **No true epidemiology.** Prevalence/incidence, sex ratio, carrier frequency, and geographic distribution are essentially undetermined.
3. **Genotype–phenotype correlation is incomplete.** The same PAX1 or EYA1 variant class can yield markedly different severity (e.g. OTFCS2 with vs without immunodeficiency; monoallelic PAX1 → OAVS). Human modifier loci are unproven.
4. **Reclassification uncertainty.** The 2025 conclusion that all EYA1-related OTFCS patients have renal anomalies and form one BOR continuum ([PMID: 41300719](https://pubmed.ncbi.nlm.nih.gov/41300719/)) rests on a literature meta-analysis of small numbers and contradicts earlier "splitting" reports ([PMID: 8558563](https://pubmed.ncbi.nlm.nih.gov/8558563/)); it needs prospective validation. Several supporting quotes for this paper in the underlying knowledge state were flagged as paraphrase and should be re-verified against the primary text.
5. **Mechanistic gaps.** How PAX1-mediated Wnt de-repression specifically translates into thymic-epithelial failure vs skeletal defects, and why hypoparathyroidism/CHD penetrance varies, is not resolved. Epigenetic contributions are unstudied.
6. **Therapeutic evidence** for CTTI derives largely from broader congenital-athymia cohorts (DiGeorge/CHARGE/FOXN1), with only a handful of PAX1-specific outcomes.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international OTFCS registry** (EYA1 and PAX1 arms) to obtain penetrance, expressivity, sex ratio, renal-anomaly frequency, and natural-history data — directly addressing the epidemiology and reclassification gaps.
2. **Systematic genotype–phenotype study** stratifying EYA1 (truncating vs missense vs CNV) and PAX1 (null vs hypomorphic; biallelic vs monoallelic) against organ involvement, immune status, and DiGeorge-overlap features.
3. **Prospective renal and immune surveillance protocol validation:** test whether all EYA1-related OTFCS patients truly harbor renal anomalies, and whether newborn TREC screening reliably captures OTFCS2 pre-symptomatically.
4. **Mechanistic dissection of PAX1 in thymic epithelium:** patient-iPSC → thymic-organoid models with rescue and Wnt-pathway modulation to test whether restoring PAX1-mediated Wnt repression corrects the epithelial defect (druggable-target discovery).
5. **CTTI outcome analysis restricted to PAX1-deficient patients**, comparing engineered vs postnatal cultured thymus tissue and defining the optimal transplant window relative to infection burden.
6. **Re-verify all citation snippets** flagged as paraphrase against primary abstracts and correct knowledge-base evidence items where needed (especially [PMID: 41300719](https://pubmed.ncbi.nlm.nih.gov/41300719/) and the hypoparathyroidism quote from [PMID: 37689091](https://pubmed.ncbi.nlm.nih.gov/37689091/)).
7. **Search OMIA/veterinary databases** to confirm the (currently negative) status of naturally occurring animal OFCS and formalize the model-organism annotation set (MGI, ZFIN).

---

*Report compiled from 5 discovery iterations, 7 confirmed findings, and 28 reviewed papers. Evidence spans human clinical, model-organism, in vitro, and computational sources. Ontology suggestions (OMIM, MONDO, HPO, GO, CL, UBERON, NCIT) are provided inline for knowledge-base ingestion.*


## Artifacts

- [OpenScientist final report](Otofaciocervical_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Otofaciocervical_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 7 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:8558563` (12 mentions) - Otofaciocervical syndrome: a sporadic patient supports splitting from the branchio-oto-renal syndrome.
  - shared terms: renal

Weighed against this report's own most characteristic terms: `otfcs2`, `pax1`, `eya1`, `defect`, `thymus`, `loss`, `renal`, `thymic`, `skeletal`, `immune`, `otfcs1`, `scid`, `ofcs`, `anomalie`, `phenotype`, `hypoparathyroidism`, `tissue`, `dominant`, `cell`, `otfc`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 16 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008159` (1 mention) - the report calls it "type 1"; MONDO calls it **postmenopausal osteoporosis**
- `MONDO:0014434` (1 mention) - the report calls it "type 2"; MONDO calls it **Bardet-Biedl syndrome 5**
- `HP:0000405` (1 mention) - the report calls it "Clinical sign"; HP calls it **Conductive hearing impairment**
- `HP:0000356` (1 mention) - the report calls it "Physical"; HP calls it **Abnormality of the outer ear**
- `HP:0004467` (1 mention) - the report calls it "Physical"; HP calls it **Preauricular pit**
- `HP:0009025` (1 mention) - the report calls it "Physical"; HP calls it **Increased connective tissue**
- `HP:0000218` (1 mention) - the report calls it "Physical"; HP calls it **High palate**
- `HP:0200023` (1 mention) - the report calls it "winged scapula"; HP calls it **Priapism**
- `HP:0000889` (1 mention) - the report calls it "Physical"; HP calls it **Abnormal clavicle morphology**
- `HP:0004322` (1 mention) - the report calls it "Physical"; HP calls it **Short stature**
- `HP:0001256` (1 mention) - the report calls it "Behavioral/cognitive"; HP calls it **Mild intellectual disability**
- `HP:0000829` (1 mention) - the report calls it "Lab"; HP calls it **Hypoparathyroidism**
- `HP:0001627` (1 mention) - the report calls it "Clinical sign"; HP calls it **Abnormal heart morphology**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0060070` (1 mention) - the report calls it "canonical Wnt signaling"; GO calls it **canonical Wnt signaling pathway**
- `GO:0006357` (1 mention) - the report calls it "regulation of transcription by Pol II"; GO calls it **regulation of transcription by RNA polymerase II**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.