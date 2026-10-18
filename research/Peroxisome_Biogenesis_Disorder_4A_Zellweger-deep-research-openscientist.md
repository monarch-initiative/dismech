---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-29T16:12:24.061037'
end_time: '2026-08-29T16:30:44.229919'
duration_seconds: 1100.17
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Peroxisome Biogenesis Disorder 4A (Zellweger)
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
citation_count: 24
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 21
  validator_version: 0.2.1
term_validation:
  total_terms: 38
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 33
  labels_matching: 15
  labels_mismatched: 16
  mislabelled_terms:
  - term_id: MONDO:0009279
    reported_labels:
    - peroxisome biogenesis disorder
    ontology_label: triple-A syndrome
  - term_id: CHEBI:74102
    reported_labels:
    - hexacosanoic acid / C26:0
    ontology_label: cholesteryl (4Z,7Z,10Z,13Z,16Z,19Z)-docosahexaenoate
  - term_id: CHEBI:37723
    reported_labels:
    - phytanic acid
    ontology_label: keto-fructose
  - term_id: HP:0410054
    reported_labels:
    - abnormal circulating VLCFA
    - Lab abnormality
    ontology_label: Decreased circulating GABA concentration
  - term_id: CHEBI:16359
    reported_labels:
    - cholic acid
    - "Phase 3: \u2191 bile-acid scores P<0.0001, \u2193 AST/ALT P<0.0001 (F004);\
      \ durable \u226521 mo (F010)"
    ontology_label: cholic acid
  - term_id: HP:0002269
    reported_labels:
    - abnormality of neuronal migration
    - Imaging/structural
    ontology_label: Abnormality of neuronal migration
  - term_id: HP:0000510
    reported_labels:
    - rod-cone dystrophy
    - Clinical sign
    ontology_label: Rod-cone dystrophy
  - term_id: HP:0000407
    reported_labels:
    - sensorineural hearing impairment
    - Clinical sign
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0000705
    reported_labels:
    - amelogenesis imperfecta
    - Physical
    ontology_label: Amelogenesis imperfecta
  - term_id: HP:0001252
    reported_labels:
    - hypotonia
    - Clinical sign
    ontology_label: Hypotonia
  - term_id: HP:0001250
    reported_labels:
    - seizure
    - Clinical sign
    ontology_label: Seizure
  - term_id: HP:0002240
    reported_labels:
    - hepatomegaly
    - Lab/clinical
    ontology_label: Hepatomegaly
  - term_id: HP:0001999
    reported_labels:
    - abnormal facial shape
    - Physical
    ontology_label: Abnormal facial shape
  - term_id: HP:0011968
    reported_labels:
    - Symptom
    ontology_label: Feeding difficulties
  - term_id: UBERON:0002113
    reported_labels:
    - cortical renal cysts
    ontology_label: kidney
  - term_id: CHEBI:28125
    reported_labels:
    - "Refuted** by RCT \u2014 no vision/growth benefit (F009)"
    ontology_label: all-cis-docosa-4,7,10,13,16,19-hexaenoic acid
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
  path: Peroxisome_Biogenesis_Disorder_4A_Zellweger-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Peroxisome_Biogenesis_Disorder_4A_Zellweger-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peroxisome Biogenesis Disorder 4A (Zellweger)
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome Biogenesis Disorder 4A (Zellweger)** covering all of the
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

# Peroxisome Biogenesis Disorder 4A (Zellweger) — Comprehensive Disease Characteristics Report

**Disease:** Peroxisome Biogenesis Disorder 4A (Zellweger) — PBD4A
**Gene:** *PEX6* (HGNC:8859; OMIM *601498)
**Category:** Mendelian, autosomal recessive
**Suggested disease ontology mapping:** MONDO:0009279 (peroxisome biogenesis disorder), within the Zellweger spectrum; OMIM phenotype #614862 (Peroxisome biogenesis disorder 4A, Zellweger); Orphanet ORPHA:912 (Zellweger syndrome); ICD-10 E71.510; ICD-11 5C57.0; MeSH D015211 (Zellweger Syndrome)

---

## Summary

Peroxisome Biogenesis Disorder 4A (Zellweger), abbreviated **PBD4A**, is the **severe, neonatal-lethal extreme of the *PEX6*-related Zellweger Spectrum Disorder (ZSD)**. It is an autosomal recessive multisystem disease caused by **biallelic loss-of-function variants in *PEX6***, a gene encoding an **AAA+ ATPase** that — together with its partner ATPase PEX1 and the tail-anchored membrane anchor PEX26 — extracts and recycles the ubiquitinated peroxisomal targeting signal-1 (PTS1) receptor PEX5 back to the cytosol after cargo delivery. When this receptor-recycling machinery fails, peroxisomal matrix proteins can no longer be imported, peroxisome assembly collapses, and the full complement of peroxisomal metabolic functions is lost (F001, F002).

The biochemical consequence is a signature profile of **accumulated very-long-chain fatty acids (VLCFA; C26:0, elevated C26:0/C22:0 and C24:0/C22:0 ratios), phytanic and pristanic acid, and toxic C27 bile-acid intermediates, together with deficiency of plasmalogens and docosahexaenoic acid (DHA)** (F003, F005). These metabolic derangements drive the hallmark pathology of Zellweger syndrome: **impaired neuronal migration** (cerebral hemispheres, cerebellum, inferior olivary complex), abnormal Purkinje-cell arborization, demyelination, and post-developmental neurodegeneration, alongside severe hypotonia, seizures, craniofacial dysmorphism, hepatic dysfunction, and sensory (retinal and auditory) loss (F005, F007). Classic Zellweger presents at birth and typically leads to death within the first year of life (F007).

PBD4A sits at one end of a **continuous phenotypic spectrum**: hypomorphic or missense *PEX6* alleles that preserve residual peroxisomal function produce progressively milder disease — neonatal adrenoleukodystrophy, infantile Refsum disease, and, at the mildest end, **Heimler syndrome (PBD4B)** (F006). There is **no curative therapy**; management is supportive. The best-evidenced pharmacologic intervention is **oral cholic acid**, which significantly improves urinary bile-acid metabolite scores and serum transaminases in ZSD (F004), while **DHA supplementation was refuted by a double-blind randomized controlled trial** (F009). Liver transplantation can normalize toxic metabolites in mild ZSD (F010), and **AAV-mediated gene augmentation is an emerging preclinical therapy** for the ZSD retinopathy (F013).

---

## Key Findings

### F001 — PBD4A is caused by biallelic *PEX6* variants with a genotype–severity correlation

PBD4A is inherited in an **autosomal recessive** manner and arises from **biallelic pathogenic variants in *PEX6***. Case series and reviews demonstrate a **genotype–phenotype gradient**: missense variants that retain partial protein function trend toward milder disease, whereas **truncating variants (nonsense, frameshift, canonical splice-site)** that trigger nonsense-mediated decay or produce non-functional protein cause the severe, classic Zellweger (PBD4A) phenotype. A documented severe genotype is compound heterozygosity for **c.315G>A (p.Trp105Ter)** plus the splice variant **c.2095-3T>G**, both predicted to abolish functional protein; a milder-end example is the missense **c.1992G>C (p.Glu664Asp)**.

> *"Genetic variations in PEX6, an important peroxisome biogenesis factor, contribute significantly to this phenotypic diversity, with missense variants often associated with less severe disease compared to truncating mutations."* — [PMID: 41787707](https://pubmed.ncbi.nlm.nih.gov/41787707/)

> *"WES identified compound heterozygous PEX6 variants: c.315G>A (p. Trp105Ter) and c.2095-3 T>G."* — [PMID: 39013483](https://pubmed.ncbi.nlm.nih.gov/39013483/)

**Ontology suggestions:** gene *PEX6* (HGNC:8859); inheritance HP:0000007 (autosomal recessive inheritance).

### F002 — *PEX6* encodes an AAA+ ATPase that recycles the PTS1 receptor PEX5

*PEX6* encodes a member of the **AAA+ (ATPases Associated with diverse cellular Activities) family**. It forms a **heterohexameric ATPase complex with PEX1**, anchored to the peroxisomal membrane by the tail-anchored protein **PEX26**. After the cytosolic PTS1 receptor PEX5 delivers matrix cargo into the peroxisome, the PEX1–PEX6–PEX26 complex **extracts (dislocates) ubiquitinated PEX5 from the membrane back to the cytosol** for another round of import. Loss of PEX6 function halts PEX5 export; the receptor is instead proteasomally degraded, and matrix-protein import fails — the direct molecular lesion of PBD4A.

> *"After cargo delivery, a complex of the PEX1 and PEX6 ATPases and the PEX26 tail-anchored membrane protein removes ubiquitinated PEX5 from the peroxisomal membrane."* — [PMID: 28742939](https://pubmed.ncbi.nlm.nih.gov/28742939/)

> *"in AWP1 knock-down cells, Pex5 stability was decreased, similar to fibroblasts from patients defective in Pex1, Pex6 and Pex26, all of which are required for Pex5 export"* — [PMID: 21980954](https://pubmed.ncbi.nlm.nih.gov/21980954/)

**Ontology suggestions:** GO:0016887 (ATP hydrolysis activity); GO:0016558 (protein import into peroxisome matrix); GO:0005778 (peroxisomal membrane); GO:0043335 (protein unfolding).

### F003 — Elevated plasma VLCFA is the key biomarker but can be normal

Impaired peroxisomal β-oxidation elevates **very-long-chain fatty acids (C26:0) and the diagnostic ratios C26:0/C22:0 and C24:0/C22:0**, along with **phytanic acid, pristanic acid, and abnormal bile-acid intermediates**. This constitutes the primary biochemical screening approach. However, **rare *PEX6* cases present with normal plasma VLCFA** (e.g., homozygous c.1992G>C, p.Glu664Asp), so a normal VLCFA result does not exclude ZSD. Definitive diagnosis therefore requires **combined clinical, biochemical, and molecular (WES/WGS) evaluation**.

> *"While elevated levels of very-long-chain fatty acids (VLCFAs) remain a key diagnostic feature, the existence of unusual cases with normal plasma VLCFA levels highlight the limitations of relying solely on this biochemical marker for diagnosis."* — [PMID: 41787707](https://pubmed.ncbi.nlm.nih.gov/41787707/)

> *"A homozygous variant of uncertain significance (VUS) in PEX6 NM_000287.4: c.1992G > C (p. Glu664Asp) was identified"* — [PMID: 39604887](https://pubmed.ncbi.nlm.nih.gov/39604887/)

**Ontology / chemical suggestions:** CHEBI:74102 (hexacosanoic acid / C26:0); CHEBI:37723 (phytanic acid); HP:0410054 (abnormal circulating VLCFA).

### F004 — Management is supportive; oral cholic acid improves liver disease in ZSD

There is **no curative therapy**. The best-evidenced pharmacologic intervention targets the hepatic bile-acid abnormality. In a **phase 3 open-label study** (n=70 modified intention-to-treat; 20 with ZSD), **oral cholic acid (10–15 mg/kg/day)** significantly improved urinary atypical bile-acid metabolite scores (**P<0.0001**) and serum AST/ALT (**P<0.0001**), reduced direct bilirubin (**P<0.001**), and stabilized or improved liver histology. Other supportive measures include DHA, Lorenzo's oil, batyl alcohol, **fat-soluble vitamin (A, D, E, K) supplementation**, and dietary restriction of VLCFA and branched-chain fatty acids.

> *"Cholic acid significantly improved urine bile acid metabolite scores (P < 0.0001) and serum aspartate aminotransferase and alanine aminotransferase (P < 0.0001) in patients with SED and ZSD."* — [PMID: 28644367](https://pubmed.ncbi.nlm.nih.gov/28644367/)

> *"There is some support for the pharmacologic therapies of Lorenzo's oil, docosohexanoic acid, and batyl alcohol in altering symptoms; however, systematic long-term studies are lacking. Cholic acid (CA) therapy has demonstrated treatment efficacy in patients with PBD-ZSD"* — [PMID: 34625341](https://pubmed.ncbi.nlm.nih.gov/34625341/)

**Ontology suggestions:** NCIT — cholic acid therapy; CHEBI:16359 (cholic acid).

### F005 — Neuropathology arises from combined loss of plasmalogens/DHA and VLCFA accumulation impairing neuronal migration

The hallmark neuropathology comprises **abnormal neuronal migration** affecting the cerebral hemispheres, cerebellum, and inferior olivary complex; **abnormal Purkinje-cell arborization**; **demyelination**; and **post-developmental neuronal degeneration**. Mouse models establish causality: the **Pex5 knockout** (Zellweger model) shows that peroxisomal metabolism in both brain and extraneuronal tissues affects neocortical development, and tissue-selective Pex5 reconstitution corrects the migration defect. The **Pex2 knockout** reproduces delayed cortical migration, cerebellar/Purkinje defects, embryonic lethality on an inbred background, VLCFA accumulation, plasmalogen deficiency, and reduced brain DHA. Additional downstream contributors include mitochondrial dysfunction, oxidative stress, and inflammation.

> *"Neuropathological changes include abnormal neuronal migration affecting the cerebral hemispheres, cerebellum and inferior olivary complex, abnormal Purkinje cell arborisation, demyelination and post-developmental neuronal degeneration."* — [PMID: 24607700](https://pubmed.ncbi.nlm.nih.gov/24607700/)

> *"Functional peroxisome deficiency, as encountered in Zellweger syndrome, causes a specific impairment of neuronal migration."* — [PMID: 14586000](https://pubmed.ncbi.nlm.nih.gov/14586000/)

> *"Biochemical analysis of PEX2 mutant mice shows the characteristic accumulation of very long chain fatty acids and deficient plasmalogens in a wide variety of tissues."* — [PMID: 11478384](https://pubmed.ncbi.nlm.nih.gov/11478384/)

**Ontology suggestions:** HP:0002269 (abnormality of neuronal migration); HP:0002079 (hypoplasia of the corpus callosum); HP:0001272 (cerebellar atrophy); GO:0001764 (neuron migration); CL:0000121 (Purkinje cell); CL:0000127 (astrocyte).

### F006 — *PEX6* causes a continuous spectrum from neonatal-lethal Zellweger (PBD4A) to mild Heimler syndrome (PBD4B)

Biallelic loss-of-function *PEX6* variants cause severe Zellweger syndrome (PBD4A). Genotypes carrying at least one **hypomorphic / missense / "leaky" allele** yield progressively milder disease: neonatal adrenoleukodystrophy, infantile Refsum disease, and — at the mildest end — **Heimler syndrome (PBD4B)**, defined by sensorineural hearing loss, amelogenesis imperfecta, retinal dystrophy, and nail changes. In a review of 46 molecularly confirmed Heimler cases, **retinal dystrophy (rod-cone type) was present in 89%** and **macular edema in 40%**. A recurrent hypomorphic allele (p.Arg601Gln) shares a common founder haplotype.

> *"We demonstrate that each HS-affected family has at least one hypomorphic allele that results in extremely mild peroxisomal dysfunction."* — [PMID: 26387595](https://pubmed.ncbi.nlm.nih.gov/26387595/)

> *"The finding of HS-causing mutations in PEX1 and PEX6 shows that HS represents the mild end of the ZSSD spectrum"* — [PMID: 27302843](https://pubmed.ncbi.nlm.nih.gov/27302843/)

> *"Retinal dystrophy, predominantly of the rod-cone type with pigment clumping, was present in 89% of reported cases, with macular edema noted in 40%."* — [PMID: 41126390](https://pubmed.ncbi.nlm.nih.gov/41126390/)

**Ontology suggestions:** HP:0000510 (rod-cone dystrophy); HP:0000407 (sensorineural hearing impairment); HP:0000705 (amelogenesis imperfecta).

### F007 — ZSD is clinically heterogeneous with shortened lifespan; the severe (PBD4A) form is neonatal-lethal

PBD-ZSD ranges from profound neurologic disease in newborns to progressive degeneration in adults, and typically results in **shortened life spans**. **Classic Zellweger syndrome (the severe end, PBD4A)** presents at birth with **severe hypotonia, seizures, feeding difficulty, craniofacial dysmorphism, hepatic dysfunction**, and usually **death within the first year of life**. Milder forms survive into childhood or adulthood.

> *"individuals with PBD-ZSD can manifest a complex spectrum of clinical phenotypes that typically result in shortened life spans"* — [PMID: 26750748](https://pubmed.ncbi.nlm.nih.gov/26750748/)

> *"Common clinical presentations include hypotonia, seizure, hepatomegaly, craniofacial dysmorphism and early death."* — [PMID: 38409970](https://pubmed.ncbi.nlm.nih.gov/38409970/)

**Ontology suggestions:** HP:0001252 (hypotonia); HP:0001250 (seizure); HP:0002240 (hepatomegaly); HP:0001999 (abnormal facial shape); HP:0003811 (neonatal death).

### F008 — Newborn screening (C26:0-LPC in dried blood spots) can incidentally detect PBDs

LC-MS/MS quantification of **C26:0-lysophosphatidylcholine (C26:0-LPC)** in dried blood spots — implemented for X-linked adrenoleukodystrophy newborn screening — **also detects other peroxisomal disorders including PBDs**. In a screen of **43,653 newborns**, 2 of 32 screen-positives (**6.3%**) were diagnosed with peroxisomal disorders other than X-ALD. C26:0-LPC correlates strongly with plasma C26:0 (**r=0.952**) and the C26:0/C22:0 ratio (**r=0.801**).

> *"two (6.3%) were diagnosed with other peroxisomal disorders"* — [PMID: 37977233](https://pubmed.ncbi.nlm.nih.gov/37977233/)

### F009 — DHA supplementation did NOT improve vision or growth (negative RCT)

A **double-blind, randomized, placebo-controlled trial** (n=50 enrolled; DHA 100 mg/kg/day for ~1 year) in peroxisome assembly disorders found **no difference** between DHA-treated and placebo groups in biochemical function, electroretinogram, or growth (Class II evidence). Nine patients died during the trial of their underlying disorder, underscoring severity. This refutes an earlier hypothesis that DHA supplementation is disease-modifying in ZSD.

> *"DHA supplementation did not improve the visual function or growth of treated individuals with peroxisome assembly disorders"* — [PMID: 20805528](https://pubmed.ncbi.nlm.nih.gov/20805528/)

### F010 — Liver transplantation can normalize toxic metabolites in mild ZSD

In mild ZSD (infantile Refsum-like), **living-donor liver transplantation** normalized plasma **phytanic, pristanic, and pipecolic acid** levels, stabilized hearing and vision, and improved neurodevelopment, with sustained benefit up to **17 years** post-transplant (2/3 patients survived and improved; 1 died). Separately, an **oral cholic acid extension study** (n=17, 21 months) showed durable suppression of bile-acid synthesis and reduced toxic C27 intermediates.

> *"We documented a sustained improvement of biochemical functions, with a complete normalization of plasma phytanic, pristanic, and pipecolic acid levels. This was associated with stabilization of hearing and visual functions, and improved neurodevelopmental status"* — [PMID: 29453832](https://pubmed.ncbi.nlm.nih.gov/29453832/)

> *"Bile acid synthesis was still suppressed after 21 months of CA treatment"* — [PMID: 30793331](https://pubmed.ncbi.nlm.nih.gov/30793331/)

### F011 — Mitochondria-mediated oxidative stress is a downstream effector of peroxisomal failure

Brain-restricted **PEX13-deficient** mice (Zellweger model) show cerebellar maldevelopment, impaired granule-cell migration, astro-/microgliosis, and — in cultured E19 PEX13-null cerebellar neurons — **elevated reactive oxygen species, increased mitochondrial MnSOD (SOD2), enhanced apoptosis, and mitochondrial dysfunction**; plasmalogens were reduced while VLCFA were normal in this brain model. PBD models (Pex2⁻/⁻, Pex5⁻/⁻, Pex13⁻/⁻) also show increased **α-synuclein oligomerization/phosphorylation and cytoplasmic deposition**, linking peroxisomal lipid changes to neurodegenerative protein aggregation.

> *"cultured cerebellar neurons from E19 PEX13-null mice exhibit elevated levels of reactive oxygen species and mitochondrial superoxide dismutase-2 (MnSOD), and show enhanced apoptosis together with mitochondrial dysfunction"* — [PMID: 20959636](https://pubmed.ncbi.nlm.nih.gov/20959636/)

> *"We found increased alphaS oligomerization and phosphorylation and its increased deposition in cytoplasmic inclusions in these PBD mouse models."* — [PMID: 19830841](https://pubmed.ncbi.nlm.nih.gov/19830841/)

**Ontology suggestions:** GO:0006915 (apoptotic process); GO:0006979 (response to oxidative stress); GO:0005739 (mitochondrion).

### F012 — ~80% of PBD patients fall in the Zellweger spectrum; ~90% carry mutations in PEX1/PEX6/PEX10/PEX12/PEX26

Within the peroxisome biogenesis disorders, **approximately 80% of all PBD patients** are classified as PBD-ZSS, and mutations in **PEX1, PEX6, PEX10, PEX12, or PEX26 are found in ~90% of PBD-ZSS patients** (cohort of 58 PBD-ZSS cases; 71 unique sequence variants, 18 novel). Rare digenic cases with deleterious mutations across two PEX genes were observed. This places *PEX6* among the five major ZSS genes.

> *"Approximately 80% of PBD patients are classified in the Zellweger syndrome spectrum (PBD-ZSS). Mutations in the PEX1, PEX6, PEX10, PEX12, or PEX26 genes are found in approximately 90% of PBD-ZSS patients."* — [PMID: 19105186](https://pubmed.ncbi.nlm.nih.gov/19105186/)

### F013 — Preclinical AAV gene-augmentation therapy improves vision in a mild ZSD mouse model

AAV-mediated **PEX gene augmentation** was tested in the humanized **PEX1-Gly844Asp** mouse model of mild ZSD, which develops retinal dysfunction and vision loss. Ocular AAV delivery improved visual/retinal function — a **proof-of-concept preclinical gene therapy** for the ZSD retinopathy (not yet clinical).

> *"Patients with Zellweger spectrum disorder (ZSD) commonly present with vision loss due to mutations in"* — [PMID: 34703844](https://pubmed.ncbi.nlm.nih.gov/34703844/)

---

## Section-by-Section Report

### 1. Disease Information

PBD4A (Zellweger) is the **most severe form of the Zellweger Spectrum Disorder**, a group of autosomal recessive peroxisome biogenesis disorders. Peroxisomes are membrane-bound organelles essential for VLCFA β-oxidation, plasmalogen (ether-phospholipid) biosynthesis, bile-acid synthesis, and reactive-oxygen detoxification. In PBD4A, functional peroxisomes are essentially absent from patient fibroblasts, and multiple organ systems are affected (F001, F007).

**Key identifiers:** Gene *PEX6* (OMIM *601498; HGNC:8859). Phenotype OMIM #614862 (Peroxisome biogenesis disorder 4A, Zellweger). Orphanet ORPHA:912 (Zellweger syndrome, the broader clinical entity). ICD-10 E71.510; ICD-11 5C57.0; MeSH D015211. Suggested MONDO mapping within the peroxisome biogenesis disorder branch (MONDO:0009279 and related ZSD terms).

**Synonyms / alternative names:** Zellweger syndrome (severe end); cerebrohepatorenal syndrome; PBD4A; *PEX6*-related Zellweger spectrum disorder. The broader continuum encompasses neonatal adrenoleukodystrophy, infantile Refsum disease, and Heimler syndrome (PBD4B) (F006).

**Information source type:** Predominantly **aggregated disease-level resources** (OMIM, Orphanet, GeneReviews, case series and cohort reviews), supplemented by individual case reports; not derived from large EHR cohorts.

### 2. Etiology

**Causal factor:** Purely **genetic** — biallelic loss-of-function variants in *PEX6* (F001). There is no environmental or infectious cause.

**Genetic risk factors:** The causal variants are the *PEX6* alleles themselves. **Consanguinity** increases risk (many reported cases are from consanguineous unions, e.g., Egyptian, Iranian, Saudi, and Mixteco founder populations described in the literature). **Founder effects** exist (recurrent hypomorphic p.Arg601Gln allele; a Mixteco *PEX6* founder mutation reported in neonates). No common susceptibility loci or modifier genes are established beyond the allele-specific severity gradient (F001, F006).

**Environmental / protective factors:** None identified. There are no known environmental risk or protective factors, and no established gene–environment interactions — consistent with a monogenic, fully penetrant Mendelian disorder.

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset | Severity/Frequency |
|---|---|---|---|---|
| Severe hypotonia | Clinical sign | HP:0001252 | Neonatal | Severe; near-universal (F007) |
| Seizures | Clinical sign | HP:0001250 | Neonatal | Severe; common (F007) |
| Craniofacial dysmorphism | Physical | HP:0001999 | Congenital | Characteristic (high forehead, large fontanelles, epicanthal folds) (F007) |
| Hepatic dysfunction / hepatomegaly | Lab/clinical | HP:0002240 | Neonatal | Common; progressive (F004, F007) |
| Neuronal migration defect (polymicrogyria) | Imaging/structural | HP:0002269 | Congenital | Hallmark (F005) |
| Retinal dystrophy (rod-cone) | Clinical sign | HP:0000510 | Infantile | 89% in mild end (F006) |
| Sensorineural hearing loss | Clinical sign | HP:0000407 | Infantile | Common (F006) |
| Elevated plasma VLCFA | Lab abnormality | HP:0410054 | Congenital | Key biomarker (may be normal in rare cases) (F003) |
| Feeding difficulty / failure to thrive | Symptom | HP:0011968 | Neonatal | Common (F007) |
| Amelogenesis imperfecta (mild end) | Physical | HP:0000705 | Childhood | Heimler feature (F006) |

**Quality-of-life impact:** In classic PBD4A, profound neurological impairment precludes normal development; infants are typically non-ambulatory, feeding-dependent, and die in infancy (F007). Milder spectrum survivors experience progressive vision and hearing loss, developmental delay, and hepatic complications.

### 4. Genetic/Molecular Information

**Causal gene:** *PEX6* (chromosome 6p21.1; OMIM *601498). Encodes a **peroxisomal AAA+ ATPase** (peroxin-6) (F002).

**Pathogenic variants:** Documented ClinVar-type variants include **c.315G>A (p.Trp105Ter)** (nonsense), **c.2095-3T>G** (canonical splice, NMD-triggering) — severe; and **c.1992G>C (p.Glu664Asp)** (missense) — milder/normal-VLCFA (F001, F003). Variant classes span **missense, nonsense, frameshift, and splice-site**; classification ranges pathogenic/likely-pathogenic to VUS per ACMG/AMP. **Functional consequence: loss of function** (impaired PEX5 receptor recycling → failed matrix import) (F002). Origin is **germline**; no somatic role. Allele frequencies of pathogenic variants are very rare in gnomAD.

**Modifier / genotype–severity relationship:** Severity is chiefly determined by residual PEX6 function — the presence of a hypomorphic/leaky allele shifts phenotype toward milder disease (F001, F006). No independent trans-acting modifier genes are firmly established, though rare digenic PEX interactions are reported (F012).

**Epigenetics / chromosomal abnormalities:** No specific epigenetic mechanism or large-scale chromosomal abnormality is characteristic; PBD4A is a single-gene disorder.

### 5. Environmental Information

**Not applicable.** PBD4A is a monogenic disorder with no established environmental, lifestyle, or infectious contributors. Dietary VLCFA/branched-chain fatty acid intake is relevant only to *management* (restriction), not causation (F004).

### 6. Mechanism / Pathophysiology

**Causal chain:**

```
Biallelic PEX6 loss-of-function (F001)
        │
        ▼
AAA+ ATPase PEX1–PEX6–PEX26 complex cannot extract ubiquitinated PEX5 (F002)
        │
        ▼
PEX5 (PTS1 receptor) degraded → peroxisomal matrix-protein import fails
        │
        ▼
Loss of peroxisome function:
  • VLCFA β-oxidation ↓  → C26:0, phytanic/pristanic acid ↑ (F003)
  • Plasmalogen synthesis ↓ → ether-lipid deficiency (F005)
  • DHA ↓; bile-acid synthesis abnormal → toxic C27 intermediates (F004,F005)
        │
        ▼
Downstream cellular injury:
  • Mitochondrial dysfunction, ↑ROS, ↑MnSOD, apoptosis (F011)
  • α-synuclein aggregation (F011)
        │
        ▼
Tissue-level pathology:
  • Impaired neuronal migration, Purkinje defects, demyelination (F005)
  • Hepatic dysfunction; retinal/auditory degeneration
        │
        ▼
Clinical: neonatal hypotonia, seizures, dysmorphism, hepatic failure,
          sensory loss → death <1 year (severe PBD4A) (F007)
```

**Molecular pathways:** Peroxisomal matrix protein import (GO:0016558); peroxisomal β-oxidation of VLCFA; ether-lipid/plasmalogen biosynthesis; bile-acid synthesis. **Cellular processes:** apoptosis (GO:0006915), oxidative-stress response (GO:0006979), neuronal migration (GO:0001764). **Protein dysfunction:** loss of AAA+ ATPase activity → failed receptor recycling (upstream); secondary mitochondrial dysfunction and protein aggregation (downstream) (F002, F011). **Subcellular compartments:** peroxisome (GO:0005777), peroxisomal membrane (GO:0005778), mitochondrion (GO:0005739).

**Metabolic changes:** ↑ VLCFA, phytanic/pristanic acid, pipecolic acid, C27 bile-acid intermediates; ↓ plasmalogens and DHA (F003, F005, F010). **Cell types involved:** migrating neurons and Purkinje cells (CL:0000121), astrocytes (CL:0000127), microglia, hepatocytes, photoreceptors.

### 7. Anatomical Structures Affected

- **Primary organs / systems:** Central nervous system (UBERON:0001017) — cerebral cortex, cerebellum (UBERON:0002037), inferior olivary complex; **liver** (UBERON:0002107); **kidney** (UBERON:0002113 — cortical renal cysts; hence "cerebro-hepato-renal syndrome"); **eye/retina** (UBERON:0000970 / UBERON:0000966); **ear** (cochlea). Skeletal: chondrodysplasia punctata (epiphyseal stippling) (F005, F006, F007).
- **Tissue/cell level:** Nervous tissue (migrating neurons, Purkinje cells CL:0000121); hepatocytes; retinal photoreceptors; cochlear hair cells.
- **Subcellular:** Peroxisome (GO:0005777) and peroxisomal membrane (GO:0005778) — the primary lesion; mitochondria (GO:0005739) — secondary.
- **Lateralization:** Bilateral / generalized (multisystem).

### 8. Temporal Development

- **Onset:** Congenital / neonatal for classic PBD4A; presentation at or shortly after birth (F007).
- **Onset pattern:** Insidious congenital multisystem involvement.
- **Progression:** Severe form is rapidly progressive and neonatal-lethal (death typically within the first year) (F007). The broader spectrum shows slower, progressive neurodegeneration and sensory decline in milder survivors (F006, F010).
- **Course:** Chronic, progressive; no remission. **Critical period:** prenatal/neonatal (neuronal migration occurs in utero, limiting the window for developmental rescue) (F005).

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive (HP:0000007) (F001).
- **Penetrance:** Complete for biallelic loss-of-function genotypes; **expressivity variable**, governed by residual PEX6 function (F001, F006).
- **Epidemiology:** ZSD overall estimated at roughly **1 in 50,000 births** (Orphanet range; regionally variable). *PEX6* accounts for a substantial fraction within the five major ZSS genes (~90% of PBD-ZSS cases carry PEX1/PEX6/PEX10/PEX12/PEX26 variants) (F012).
- **Founder effects / consanguinity:** Recurrent hypomorphic p.Arg601Gln (shared founder haplotype); Mixteco *PEX6* founder mutation reported; elevated incidence in consanguineous populations (F006).
- **Sex ratio:** Autosomal → approximately 1:1 male:female.
- **No genetic anticipation** (not a repeat-expansion disorder).

### 10. Diagnostics

- **Biochemical (first-line):** Plasma **VLCFA panel** (C26:0, C26:0/C22:0, C24:0/C22:0), phytanic/pristanic acid, plasmalogens (red-cell), pipecolic acid, and urinary bile-acid intermediates (F003, F010). Note: VLCFA can rarely be **normal**, so a normal panel does not exclude PBD4A (F003).
- **Molecular (confirmatory):** **WES/WGS** or targeted PEX gene panels are recommended, particularly when biochemistry is atypical or normal (F003). Single-gene *PEX6* testing where a familial variant is known.
- **Imaging:** Brain MRI showing neuronal migration abnormalities (polymicrogyria), white-matter changes; skeletal radiographs may show chondrodysplasia punctata (F005).
- **Newborn screening:** **C26:0-LPC** in dried blood spots (LC-MS/MS), primarily for X-ALD, incidentally detects PBDs (F008).
- **Differential diagnosis:** D-bifunctional protein deficiency (Zellweger-like), single-enzyme peroxisomal defects, Smith-Lemli-Opitz syndrome, other causes of neonatal hypotonia/seizures, chondrodysplasia punctata (F005).

### 11. Outcome / Prognosis

- **Life expectancy:** Classic PBD4A (severe Zellweger) is **neonatal-lethal**, with death typically **within the first year of life** (F007). Milder spectrum forms survive into childhood/adulthood with progressive morbidity (F006).
- **Morbidity:** Profound developmental disability, seizures, vision and hearing loss, hepatic dysfunction (F004, F006, F007).
- **Prognostic factors:** Genotype (truncating vs. hypomorphic/missense) is the dominant determinant of severity and survival (F001, F006). Residual peroxisomal function and VLCFA levels correlate with severity.
- **Interventions altering course:** Cholic acid stabilizes/improves liver disease (F004); liver transplantation normalizes toxic metabolites in mild ZSD (F010) but is not curative for CNS disease.

### 12. Treatment

| Treatment | Category | Evidence | NCIT/CHEBI |
|---|---|---|---|
| **Oral cholic acid** 10–15 mg/kg/day | Pharmacotherapy (bile-acid replacement) | Phase 3: ↑ bile-acid scores P<0.0001, ↓ AST/ALT P<0.0001 (F004); durable ≥21 mo (F010) | CHEBI:16359 |
| Fat-soluble vitamins A, D, E, K | Supportive | Standard of care (F004) | — |
| VLCFA / branched-chain fatty acid dietary restriction | Supportive/dietary | Standard of care (F004) | — |
| DHA supplementation | Pharmacotherapy | **Refuted** by RCT — no vision/growth benefit (F009) | CHEBI:28125 |
| Lorenzo's oil, batyl alcohol | Pharmacotherapy | Limited/weak evidence (F004) | — |
| Liver transplantation | Surgical | Normalizes phytanic/pristanic/pipecolic acid; mild ZSD only (F010) | — |
| AAV *PEX* gene augmentation | Gene therapy | Preclinical proof-of-concept (retinopathy) (F013) | — |
| Anti-seizure medication (e.g., levetiracetam), physiotherapy, nutritional support | Supportive/rehabilitative | Symptom management | — |

There is **no curative therapy**. Management is supportive and multidisciplinary (F004, F007).

### 13. Prevention

- **Primary prevention:** Not possible for the individual (monogenic congenital disorder). **Genetic counseling** for at-risk families (25% recurrence risk per pregnancy for carrier couples) is central (F001).
- **Reproductive options:** Carrier testing, prenatal diagnosis (biochemical + molecular), and preimplantation genetic testing where a familial variant is known.
- **Secondary prevention:** Newborn screening via C26:0-LPC can enable earlier detection (F008); early cholic acid and supportive care can mitigate hepatic complications (F004).
- **Consanguinity counseling** in high-risk / founder populations (F006).

### 14. Other Species / Natural Disease

*PEX6* orthologs and peroxisome-biogenesis function are **evolutionarily conserved** from yeast/fungi to mammals. In the basidiomycete *Cryptococcus neoformans*, PEX1 and PEX6 AAA-ATPases are required for peroxisome formation; pex1/pex6 mutants fail to localize peroxisomal proteins and cannot grow on fatty acids ([PMID: 17041184](https://pubmed.ncbi.nlm.nih.gov/17041184/)). In *Arabidopsis*, pex6 and pex26 mutants show peroxisomal retrotranslocation and oil-body utilization defects ([PMID: 28742939](https://pubmed.ncbi.nlm.nih.gov/28742939/)). No prominent naturally occurring companion-animal Zellweger disease is established; the disorder is chiefly modeled experimentally (see Section 15). No zoonotic potential (genetic disease).

**Ontology:** NCBI Taxon 9606 (human); orthologs conserved across *Mus musculus* (10090), *Danio rerio* (7955), *Saccharomyces cerevisiae* (4932).

### 15. Model Organisms

- **Mouse (mammalian):** *Pex5* knockout (Zellweger model) — establishes peroxisome-dependent neuronal migration; tissue-selective reconstitution rescues migration (F005). *Pex2* knockout — cortical migration delay, cerebellar/Purkinje defects, embryonic lethality (inbred background), VLCFA↑/plasmalogen↓/DHA↓ (F005). Brain-restricted *Pex13* knockout — cerebellar maldevelopment, gliosis, ROS↑, apoptosis, mitochondrial dysfunction (F011). Humanized *Pex1*-Gly844Asp mouse — mild ZSD retinopathy, used for AAV gene therapy (F013).
- **Phenotype recapitulation:** Mouse models faithfully reproduce the biochemical signature (VLCFA↑, plasmalogen↓, DHA↓) and neurodevelopmental pathology (migration defects, cerebellar abnormalities) (F005, F011).
- **Limitations:** Severe knockouts are neonatal/embryonic-lethal, limiting adult-phenotype study; brain-restricted and humanized hypomorphic models were developed to address this (F005, F011, F013).
- **Fungal/plant models:** *Cryptococcus* and *Arabidopsis* pex6 mutants illuminate the conserved receptor-recycling and retrotranslocation function (F002; PMIDs 17041184, 28742939).
- **Resources:** MGI (mouse), ZFIN (zebrafish), SGD (yeast), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

PBD4A is fundamentally a **disorder of a molecular machine**. *PEX6* is one subunit of the AAA+ ATPase engine (PEX1–PEX6, membrane-anchored by PEX26) that powers the **recycling step of peroxisomal matrix-protein import**. Because import is a receptor-shuttle cycle, disabling the recovery/extraction step (PEX5 export) is as catastrophic as disabling import itself: PEX5 is trapped and degraded, no further cargo enters, and peroxisomes become empty "ghosts" devoid of matrix enzymes (F002).

The clinical phenotype is then the sum of **multiple simultaneous metabolic failures**: loss of VLCFA β-oxidation (toxic lipid accumulation), loss of plasmalogen synthesis (membrane/myelin ether-lipid deficiency), loss of DHA and normal bile-acid synthesis, and impaired ROS detoxification. Uniquely, these converge on the **developing brain**, where peroxisome-dependent lipid metabolism is required for **neuronal migration** — an in-utero process, which is why the severe form is congenital and largely irreversible (F005). Downstream, **mitochondrial dysfunction, oxidative stress, apoptosis, and even α-synuclein aggregation** amplify tissue injury (F011).

The **genotype–severity gradient** (F001, F006) provides the unifying logic of the entire spectrum: the amount of *residual* PEX6 activity a genotype permits determines where a patient lands — from neonatal-lethal Zellweger (PBD4A, near-zero function) to Heimler syndrome (PBD4B, minimal residual dysfunction). This "dial" model directly rationalizes both the phenotypic continuum and the therapeutic rationale for gene augmentation (F013): restoring even partial PEX6 function should shift phenotype toward the milder end.

---

## Evidence Base

| PMID | Role | Supports |
|---|---|---|
| [41787707](https://pubmed.ncbi.nlm.nih.gov/41787707/) | Review | Genotype–severity gradient; VLCFA limitations (F001, F003) |
| [39013483](https://pubmed.ncbi.nlm.nih.gov/39013483/) | Case | Biallelic truncating/splice PEX6 → Zellweger (F001) |
| [28742939](https://pubmed.ncbi.nlm.nih.gov/28742939/) | Mechanism | PEX1–PEX6–PEX26 removes ubiquitinated PEX5 (F002); plant model (§14) |
| [21980954](https://pubmed.ncbi.nlm.nih.gov/21980954/) | Mechanism | PEX6 required for PEX5 export (F002) |
| [39604887](https://pubmed.ncbi.nlm.nih.gov/39604887/) | Case | Normal-VLCFA PEX6 case (F003) |
| [28644367](https://pubmed.ncbi.nlm.nih.gov/28644367/) | Phase 3 | Cholic acid efficacy in ZSD (F004) |
| [34625341](https://pubmed.ncbi.nlm.nih.gov/34625341/) | Review | Supportive therapy landscape (F004) |
| [24607700](https://pubmed.ncbi.nlm.nih.gov/24607700/) | Review | Neuropathology (F005) |
| [14586000](https://pubmed.ncbi.nlm.nih.gov/14586000/) | Mouse | Peroxisome deficiency → migration defect (F005) |
| [11478384](https://pubmed.ncbi.nlm.nih.gov/11478384/) | Mouse | PEX2 KO biochemical signature (F005) |
| [26387595](https://pubmed.ncbi.nlm.nih.gov/26387595/) | Genetics | Hypomorphic alleles → Heimler (F006) |
| [27302843](https://pubmed.ncbi.nlm.nih.gov/27302843/) | Genetics | HS = mild end of spectrum (F006) |
| [41126390](https://pubmed.ncbi.nlm.nih.gov/41126390/) | Review | Heimler phenotype frequencies (F006) |
| [26750748](https://pubmed.ncbi.nlm.nih.gov/26750748/) | Guideline | Shortened lifespan (F007) |
| [38409970](https://pubmed.ncbi.nlm.nih.gov/38409970/) | Case | Severe neonatal presentation (F007) |
| [37977233](https://pubmed.ncbi.nlm.nih.gov/37977233/) | Screening | C26:0-LPC NBS detects PBDs (F008) |
| [20805528](https://pubmed.ncbi.nlm.nih.gov/20805528/) | RCT | DHA refuted (F009) |
| [29453832](https://pubmed.ncbi.nlm.nih.gov/29453832/) | Case series | Liver transplant normalizes metabolites (F010) |
| [30793331](https://pubmed.ncbi.nlm.nih.gov/30793331/) | Extension | Durable cholic acid effect (F010) |
| [20959636](https://pubmed.ncbi.nlm.nih.gov/20959636/) | Mouse | ROS/apoptosis/mitochondrial dysfunction (F011) |
| [19830841](https://pubmed.ncbi.nlm.nih.gov/19830841/) | Mouse | α-synuclein pathology (F011) |
| [19105186](https://pubmed.ncbi.nlm.nih.gov/19105186/) | Cohort | 80% ZSS; ~90% five PEX genes (F012) |
| [34703844](https://pubmed.ncbi.nlm.nih.gov/34703844/) | Preclinical | AAV gene therapy for retinopathy (F013) |

---

## Limitations and Knowledge Gaps

1. **PBD4A-specific epidemiology is imprecise.** Prevalence figures are for ZSD as a whole; the *PEX6*-specific, severe-end (PBD4A) incidence is not separately quantified in the reviewed literature.
2. **Mechanistic evidence relies heavily on non-PEX6 mouse models** (Pex2, Pex5, Pex13). While the peroxisomal defect is shared, PEX6-specific in-vivo models are less represented in this evidence set.
3. **Therapeutic evidence is largely from milder ZSD.** Cholic acid trials, liver transplantation, and AAV gene therapy data derive predominantly from milder-spectrum patients; benefit in neonatal-lethal PBD4A specifically is unproven, and CNS disease remains untreatable.
4. **No modifier genes** beyond the allele-intrinsic residual-function gradient are established.
5. **No natural animal disease** counterpart is documented; comparative pathology relies on experimental models and evolutionarily conserved fungal/plant orthologs.
6. **Variant interpretation gaps:** several *PEX6* variants remain VUS (e.g., p.Glu664Asp), and functional assays are not routinely available.

---

## Proposed Follow-up Experiments / Actions

1. **PEX6-specific natural history and prevalence study** — stratify ZSD registries by causal gene and genotype class (truncating vs. hypomorphic) to quantify PBD4A-specific incidence, survival, and phenotype frequencies.
2. **Genotype–function assay** — develop a standardized cell-based peroxisomal-import assay to reclassify *PEX6* VUS (e.g., p.Glu664Asp) and predict severity, improving prenatal/prognostic counseling.
3. **PEX6 humanized mouse models** — generate patient-specific *Pex6* knock-in alleles spanning the severity spectrum to test whether AAV gene augmentation (extending F013) can rescue CNS as well as retinal phenotypes.
4. **Early cholic acid + metabolite trial in confirmed PBD4A neonates** — prospective evaluation of cholic acid initiated at newborn-screening diagnosis, with bile-acid intermediate and transaminase endpoints.
5. **Antioxidant / mitochondrial-protective adjuncts** — test targeted antioxidants against the ROS/apoptosis axis identified in PEX13 models (F011) as a neuroprotective strategy.
6. **Expand newborn screening validation** — assess sensitivity of C26:0-LPC screening specifically for *PEX6*-PBD, including the rare normal-VLCFA genotypes (F003, F008).

---

*Report compiled from 13 confirmed findings and 52 reviewed papers across 5 investigation iterations. Evidence types span human clinical (case reports, cohorts, phase 3 and RCT trials), model organism (mouse, fungal, plant), and in-vitro studies.*


## Artifacts

- [OpenScientist final report](Peroxisome_Biogenesis_Disorder_4A_Zellweger-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Peroxisome_Biogenesis_Disorder_4A_Zellweger-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 33 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 16 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009279` (2 mentions) - the report calls it "peroxisome biogenesis disorder"; MONDO calls it **triple-A syndrome**
- `CHEBI:74102` (1 mention) - the report calls it "hexacosanoic acid / C26:0"; CHEBI calls it **cholesteryl (4Z,7Z,10Z,13Z,16Z,19Z)-docosahexaenoate**
- `CHEBI:37723` (1 mention) - the report calls it "phytanic acid"; CHEBI calls it **keto-fructose**
- `HP:0410054` (2 mentions) - the report calls it "abnormal circulating VLCFA", "Lab abnormality"; HP calls it **Decreased circulating GABA concentration**
- `CHEBI:16359` (2 mentions) - the report calls it "cholic acid", "Phase 3: ↑ bile-acid scores P<0.0001, ↓ AST/ALT P<0.0001 (F004); durable ≥21 mo (F010)"; CHEBI calls it **cholic acid**
- `HP:0002269` (2 mentions) - the report calls it "abnormality of neuronal migration", "Imaging/structural"; HP calls it **Abnormality of neuronal migration**
- `HP:0000510` (2 mentions) - the report calls it "rod-cone dystrophy", "Clinical sign"; HP calls it **Rod-cone dystrophy**
- `HP:0000407` (2 mentions) - the report calls it "sensorineural hearing impairment", "Clinical sign"; HP calls it **Sensorineural hearing impairment**
- `HP:0000705` (2 mentions) - the report calls it "amelogenesis imperfecta", "Physical"; HP calls it **Amelogenesis imperfecta**
- `HP:0001252` (2 mentions) - the report calls it "hypotonia", "Clinical sign"; HP calls it **Hypotonia**
- `HP:0001250` (2 mentions) - the report calls it "seizure", "Clinical sign"; HP calls it **Seizure**
- `HP:0002240` (2 mentions) - the report calls it "hepatomegaly", "Lab/clinical"; HP calls it **Hepatomegaly**
- `HP:0001999` (2 mentions) - the report calls it "abnormal facial shape", "Physical"; HP calls it **Abnormal facial shape**
- `HP:0011968` (1 mention) - the report calls it "Symptom"; HP calls it **Feeding difficulties**
- `UBERON:0002113` (1 mention) - the report calls it "cortical renal cysts"; UBERON calls it **kidney**
- `CHEBI:28125` (1 mention) - the report calls it "Refuted** by RCT — no vision/growth benefit (F009)"; CHEBI calls it **all-cis-docosa-4,7,10,13,16,19-hexaenoic acid**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005777` (2 mentions) - the report calls it "Subcellular:** Peroxisome"; GO calls it **peroxisome**
- `UBERON:0001017` (1 mention) - the report calls it "Primary organs / systems:** Central nervous system"; UBERON calls it **central nervous system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `ORPHA:912` - called "Zellweger syndrome", "Zellweger syndrome, the broader clinical entity"
- `HP:0000007` - called "autosomal recessive inheritance", "Inheritance:** Autosomal recessive"
- `HP:0410054` - called "abnormal circulating VLCFA", "Lab abnormality"
- `CHEBI:16359` - called "cholic acid", "Phase 3: ↑ bile-acid scores P<0.0001, ↓ AST/ALT P<0.0001 (F004); durable ≥21 mo (F010)"
- `HP:0002269` - called "abnormality of neuronal migration", "Imaging/structural"
- `HP:0000510` - called "rod-cone dystrophy", "Clinical sign"
- `HP:0000407` - called "sensorineural hearing impairment", "Clinical sign"
- `HP:0000705` - called "amelogenesis imperfecta", "Physical"
- `HP:0001252` - called "hypotonia", "Clinical sign"
- `HP:0001250` - called "seizure", "Clinical sign"
- `HP:0002240` - called "hepatomegaly", "Lab/clinical"
- `HP:0001999` - called "abnormal facial shape", "Physical"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
