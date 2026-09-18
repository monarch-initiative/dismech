---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-08-29T06:13:57.673790'
end_time: '2026-08-29T06:18:15.112892'
duration_seconds: 257.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Papillon-Lefevre Disease
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 17
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMID:19882040
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 71
  verified: 65
  not_found: 3
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.043
  labels_checked: 60
  labels_matching: 28
  labels_mismatched: 27
  mislabelled_terms:
  - term_id: CL:0000094
    reported_labels:
    - neutrophil
    ontology_label: granulocyte
  - term_id: HP:0003610
    reported_labels:
    - Erythematous plaques
    ontology_label: Fibroblast metachromasia
  - term_id: HP:0000977
    reported_labels:
    - Hyperhidrosis
    ontology_label: Soft skin
  - term_id: HP:0003795
    reported_labels:
    - Alveolar bone loss
    ontology_label: Short middle phalanx of toe
  - term_id: HP:0006802
    reported_labels:
    - Intracranial calcification
    ontology_label: Abnormal anterior horn cell morphology
  - term_id: NCIT:C12219
    reported_labels:
    - Health Behavior
    ontology_label: Anatomic Structure, System, or Substance
  - term_id: NCIT:C17010
    reported_labels:
    - Socioeconomic Factors
    ontology_label: Prevalence
  - term_id: GO:0016500
    reported_labels:
    - activation of proenzyme
    ontology_label: protein-hormone receptor activity
  - term_id: UBERON:0001838
    reported_labels:
    - gingiva
    ontology_label: sublingual duct
  - term_id: UBERON:0002503
    reported_labels:
    - periodontal ligament
    ontology_label: greater trochanter
  - term_id: UBERON:0004707
    reported_labels:
    - alveolar process of maxilla
    ontology_label: pharyngula stage
  - term_id: UBERON:0004705
    reported_labels:
    - alveolar process of mandible
    ontology_label: fenestra
  - term_id: CL:0000683
    reported_labels:
    - osteoclast
    ontology_label: ependymoglial cell
  - term_id: NCIT:C16693
    reported_labels:
    - Gene Frequency
    ontology_label: Non-Histone Chromosomal Protein HMG-17
  - term_id: NCIT:C94258
    reported_labels:
    - Consanguinity
    ontology_label: Expanded Access Study Protocol Intervention Or Procedure
  - term_id: NCIT:C17890
    reported_labels:
    - Genetic Testing
    ontology_label: DNA Footprinting
  - term_id: NCIT:C20160
    reported_labels:
    - DNA Sequencing
    ontology_label: NCI Center for Cancer Research
  - term_id: NCIT:C62047
    reported_labels:
    - Retinoid Therapy
    ontology_label: Mexiletine
  - term_id: NCIT:C62791
    reported_labels:
    - Topical Corticosteroid Therapy
    ontology_label: Pegdinetanib
  - term_id: NCIT:C29428
    reported_labels:
    - Keratolytic Agent
    ontology_label: Shared Anti-Idiotype-AB-S016
  - term_id: NCIT:C102887
    reported_labels:
    - Dimethyl Fumarate
    ontology_label: LIM Domain-Binding Protein 1
  - term_id: NCIT:C15295
    reported_labels:
    - Periodontal Therapy
    ontology_label: Chemotherapeutic Perfusion
  - term_id: NCIT:C6708
    reported_labels:
    - Antibiotic Therapy
    ontology_label: Stage IVB Bone Sarcoma AJCC v7
  - term_id: NCIT:C51942
    reported_labels:
    - Tooth Extraction
    ontology_label: Papanicolaou Test
  - term_id: NCIT:C51945
    reported_labels:
    - Dental Implant Placement
    ontology_label: Ambulatory Surgical Facility
  - term_id: NCIT:C15986
    reported_labels:
    - Multidisciplinary Treatment Approach
    ontology_label: Pharmacotherapy
  - term_id: NCIT:C15481
    reported_labels:
    - Supportive Care
    ontology_label: Antiandrogen Therapy
  labels_variant: 5
  unresolved_terms:
  - HP:0004600
  - HP:0002976
  - UBERON:0004278
  obsolete_terms:
  - term_id: NCIT:C51942
    ontology_label: Papanicolaou Test
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Papillon-Lefevre Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Papillon-Lefevre Disease** covering all of the
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

# Papillon–Lefevre Disease (Papillon–Lefèvre Syndrome): An Integrated Research Overview

Papillon–Lefevre disease, more commonly termed Papillon–Lefèvre syndrome (PLS), is a paradigmatic rare genodermatosis that links a single lysosomal protease—cathepsin C—to an unusually specific constellation of dermatologic and periodontal phenotypes, including diffuse palmoplantar keratoderma, aggressive early-onset periodontitis, and premature loss of both primary and permanent dentition.[1][3][6][15] It is transmitted as an autosomal recessive trait caused by biallelic loss-of-function variants in the CTSC gene on chromosome 11q14, with more than seventy distinct pathogenic mutations reported to date and a global prevalence estimated at one to four cases per million individuals.[1][5][10][16] The syndrome is now classed within the broader spectrum of ectodermal dysplasias, and its clinical picture is further complicated by variable immunologic abnormalities—particularly defects in neutrophil and natural killer (NK) cell function—that predispose to recurrent pyogenic infections and may contribute directly to the rapid periodontal tissue destruction characteristic of the disease.[3][6][15] Despite major advances in defining the genetic basis of PLS and clarifying aspects of CTSC physiology, the exact mechanistic chain linking CTSC deficiency to skin hyperkeratosis and severe periodontitis remains incompletely understood, underscoring the value of this disorder as a model for host–microbe interactions, immune protease cascades, and tissue-specific manifestations of monogenic defects.[3][4][10] Clinically, PLS demands multidisciplinary management, combining systemic and topical dermatologic therapies (such as keratolytics, emollients, and retinoids), intensive preventive and restorative dental care (including possible early extraction of teeth and prosthetic rehabilitation), and aggressive infection control, while genetic counseling and, increasingly, molecular diagnostics provide a framework for primary and secondary prevention in at-risk families.[3][8][13][15][16]  

---

## 1. Disease Information

### 1.1 Definitions and Clinical Overview

Papillon–Lefèvre syndrome is a rare inherited disorder of keratinization and periodontal tissue integrity that presents in early childhood with diffuse erythematous palmoplantar hyperkeratosis and rapidly progressive periodontitis leading to premature exfoliation of both primary and permanent teeth.[1][3][5][6][15] The condition was first delineated in 1924 by the French physicians Papillon and Lefèvre in siblings who exhibited the combination of palmoplantar keratoderma and early-onset destructive periodontitis, a clinical pairing that has since been regarded as pathognomonic for the syndrome.[3][6][16][15] Modern nosological frameworks categorize PLS as an ectodermal dysplasia, emphasizing that the primary tissues affected—skin adnexa and teeth—derive from ectodermal lineages and that the syndrome manifests as a developmental abnormality of ectodermal structures rather than a purely inflammatory or infectious disease.[2][14][15]  

The core clinical definition of PLS includes three principal characteristics: diffuse palmoplantar keratoderma typically beginning between ages one and four; severe, generalized periodontitis affecting both deciduous and permanent teeth with onset around three to four years of age; and resultant premature edentulism, often by adolescence.[3][5][6][8][16] Many patients also experience recurrent cutaneous or systemic pyogenic infections, and a subset exhibit additional features such as hyperhidrosis, arachnodactyly, intracranial calcifications, and variable cognitive impairment, though these are not universally present and likely reflect either pleiotropic consequences of CTSC deficiency or coincident conditions.[3][6][16]  

The etiologic hallmark of PLS is autosomal recessive loss-of-function mutation in CTSC, the gene encoding the lysosomal cysteine protease cathepsin C (also known as dipeptidyl peptidase I), which plays a central role in activating a suite of immune cell serine proteases and is highly expressed in the specific epithelial and immune cell populations implicated in PLS pathology.[1][4][6][10][15] At the level of disease classification, PLS is therefore considered a monogenic Mendelian disorder with a well-defined genetic cause, and its clinical variability is largely interpreted in light of different CTSC alleles, environmental factors such as oral microbiota composition, and host immune response rather than complex polygenic predisposition.[4][10][15]  

From the standpoint of clinical practice and research evidence, most information about PLS is derived from aggregated disease-level resources—such as OMIM, Orphanet, and rare disease registries—and from case reports, case series, and small mechanistic studies, rather than from large-scale cohort or randomized trial data.[1][2][3][5][6][10][15][16] The rarity of the syndrome has constrained population-based epidemiologic analyses, and much of the clinical spectrum has been reconstructed from detailed individual patient descriptions, including family pedigrees, longitudinal dental and dermatologic follow-up, and targeted genetic analyses. This reliance on observational data emphasizes the need for careful critical appraisal of evidence but also highlights the consistency of core features across diverse ethnic and geographic backgrounds, reinforcing the robustness of the current disease definition.[3][5][6][10][15][16]  

### 1.2 Nosology, Ontology Identifiers, and Synonyms

Papillon–Lefèvre syndrome is indexed in multiple biomedical ontologies and disease classification systems, reflecting its recognition as a distinct clinical entity and facilitating interoperability between databases and computational tools. In the OMIM catalog of Mendelian disorders, PLS is entry #245000 and is annotated under the name “Papillon-Lefevre syndrome; PALS,” with the disease mapped to chromosome 11q14.2 and linked to the CTSC gene (OMIM 602365).[1] Orphanet, a European resource dedicated to rare diseases, assigns PLS the Orphanet ID 678 and describes it as “a rare ectodermal dysplasia characterized by palmoplantar keratoderma associated with early-onset periodontitis.”[2] The MONDO ontology, which integrates multiple disease ontologies, lists PLS as MONDO:0009490 and gives an essentially identical definitional phrase, underscoring the consensus around its core phenotypic description.[14]  

In clinical terminologies, PLS is represented by SNOMED CT concept 40158001 and is cross-referenced to Orphanet 678 and Disease Ontology DOID:3389, capturing its characterization as a rare genetic palmoplantar keratoderma associated with early-onset periodontitis.[1][2][14] ICD-10 and ICD-11 do not provide a unique code exclusively for PLS; rather, affected individuals are typically coded under categories for hereditary palmoplantar keratoderma and aggressive periodontitis or other specified hereditary disorders, reflecting the granularity limits of these systems for rare diseases. MeSH (Medical Subject Headings) and MedDRA similarly do not include PLS as a primary descriptor but index relevant literature under headings such as “Keratoderma, palmoplantar,” “Periodontitis,” and “Genetic Diseases, Inborn,” with PLS appearing as a keyword or supplementary concept in many indexed records.[3][5][6][15]  

Synonymous and alternative names for the condition include “Papillon-Lefevre disease,” “Papillon-Lefèvre syndrome,” “Papillon-Lefèvre disease,” and occasionally “Papillon–Lefèvre ectodermal dysplasia,” although the term “syndrome” remains the most widely used in both clinical and genetic contexts.[3][5][6][15] Historical literature sometimes refers to PLS as “Papillon–Lefèvre keratoderma with periodontitis,” emphasizing the cutaneous component, and early dental reports describe it under headings such as “familial juvenile periodontitis with palmoplantar keratosis.”[3][16] Ontologically, PLS is subclassed under hereditary palmoplantar keratoderma and under ectodermal dysplasias, and it shares close proximity with Haim-Munk syndrome (HMS) and aggressive periodontitis type 1 (AP1), both of which are allelic to PLS and also caused by CTSC mutations.[1][10][15]  

### 1.3 Data Sources and Evidence Types

The knowledge base for PLS integrates several layers of evidence, ranging from clinical case descriptions and genealogical analyses to molecular genetic studies and immunologic investigations. OMIM provides a curated summary of clinical features, inheritance, and genetic etiology, drawing on primary literature including linkage and positional cloning studies that mapped PLS to 11q14–q21 and identified CTSC as the causal gene.[1][4][10] Orphanet aggregates expert-reviewed data on prevalence, inheritance, age of onset, and main manifestations, while MONDO and other ontologies distill these insights into standardized definitional statements suitable for computational reasoning.[2][14][15]  

Primary genetic evidence arises from positional cloning and sequencing studies, notably Hart et al. (1999, Journal of Medical Genetics, PMID:10593994), which first reported CTSC mutations in consanguineous Turkish families with PLS; this landmark study demonstrated that PLS patients were homozygous for truncating CTSC variants, whereas heterozygous relatives were clinically unaffected.[4] Subsequent work by Nagy et al. (2014, Human Mutation, PMID:24711138) and others systematically cataloged CTSC mutations in PLS, HMS, and AP1, defining a spectrum of nonsense, frameshift, missense, and splice site variants and highlighting recurrent alleles in specific populations.[10]  

Clinical evidence is dominated by case reports and small case series, such as Ahmad et al. (2009, Indian Journal of Dermatology, PMID:19882040) and more recent compilations including a 2024 case series of multiple patients with PLS.[5][6] These reports provide detailed phenotypic descriptions, radiographic findings, treatment responses, and family histories, often supported by CTSC sequencing. Immunologic and mechanistic evidence comes from functional studies of neutrophil and NK cell activity in PLS patients, as summarized by the 2015 review by Patel et al. (PMCID:PMC4507741) and others, which detail defects in polymorphonuclear leukocyte chemotaxis and phagocytosis, reduced CTSC enzymatic activity, and impaired NK cell cytotoxic function.[3][6][15]  

More recently, microbiome-based investigations have contributed to understanding the oral environment in PLS, including a 2021 study characterizing the salivary microbiome of three sisters with PLS and demonstrating distinctive bacterial and archaeal communities associated with advanced periodontitis and hyposalivation.[9] On the therapeutic side, dermatologic case reports and small series describe the use of systemic retinoids (etretinate, acitretin, isotretinoin) and, more recently, dimethyl fumarate, while dental literature evaluates prophylactic antibiotics, early tooth extraction, and implant-based rehabilitation.[7][8][13] Overall, PLS exemplifies a rare disease where high-quality mechanistic insight is available despite small patient numbers, but where many aspects of natural history and optimal management still rely on expert consensus rather than randomized trial data.[3][5][8][15]  

---

## 2. Etiology

### 2.1 Genetic Etiology: CTSC and its Function

The primary etiologic factor in Papillon–Lefèvre syndrome is autosomal recessive inheritance of biallelic loss-of-function mutations in CTSC, the gene encoding the lysosomal cysteine protease cathepsin C (dipeptidyl peptidase I).[1][4][6][10][15] Genetic linkage studies by multiple independent groups in the late 1990s mapped the major susceptibility locus for PLS to a 2.8 cM interval on chromosome 11q14–q21, and correlation of physical and genetic maps revealed several candidate genes, including CTSC, whose expression and function were consistent with the tissue specificity of PLS.[4][10][15] Hart et al. subsequently sequenced CTSC in affected members of five consanguineous Turkish families and identified four different truncating mutations that segregated with the disease, establishing CTSC as the causal gene.[4]  

The OMIM entry for PLS notes that a “number sign (#) is used with this entry because Papillon-Lefevre syndrome (PALS) is caused by homozygous or compound heterozygous mutation in the cathepsin C gene (CTSC, or DPPI; 602365) on chromosome 11q14,” and emphasizes that CTSC mutations also underlie Haim-Munk syndrome and aggressive periodontitis type 1.[1] This autosomal recessive pattern means that affected individuals typically inherit one mutant CTSC allele from each carrier parent, leading to either complete absence of functional cathepsin C protein or severely reduced enzymatic activity, whereas heterozygous carriers are clinically unaffected and exhibit only partial reductions in CTSC function.[4][6][10][15]  

Cathepsin C is a lysosomal exopeptidase that removes dipeptides from the N-terminus of protein substrates and is critically involved in the activation of serine proteases in neutrophils, mast cells, and cytotoxic lymphocytes, including neutrophil elastase, cathepsin G, proteinase 3, and granzymes.[4][6][10][15] Hart et al. reported that CTSC mRNA is expressed at high levels in polymorphonuclear leukocytes, macrophages, and their precursors, as well as in epithelial regions commonly affected by PLS—palms, soles, knees, and oral keratinized gingiva—providing a clear link between CTSC deficiency and the tissue distribution of disease manifestations.[4][6][15] In the words of Ahmad et al., “Papillon-Lefevre syndrome is a rare autosomal recessive disorder caused by cathepsin C gene mutation leading to the deficiency of cathepsin C enzymatic activity,” an assertion supported by biochemical assays showing more than 90% reduction in CTSC activity in PLS patients.[6][3]  

Because CTSC is required for proteolytic activation of multiple immune cell serine proteases, its deficiency is predicted to impair key effector pathways in innate and adaptive immunity, including neutrophil-mediated bacterial killing, NK cell cytotoxicity, and cytotoxic T lymphocyte-induced apoptosis.[3][6][10][15] These immune defects are thought to contribute to the severe periodontal tissue destruction and increased susceptibility to infections observed in PLS, although the precise quantitative relationship between CTSC activity, protease activation, and clinical phenotypes remains an active area of investigation.[3][6][10][15] At present, no non-CTSC genetic cause of classical PLS has been convincingly documented; individuals with PLS-like features but without CTSC mutations are generally reclassified as having other forms of palmoplantar keratoderma or nonsyndromic tooth abnormalities.[10][15]  

### 2.2 Pathogenic Variants and Genotype–Phenotype Correlations

The spectrum of CTSC mutations associated with PLS is broad, encompassing nonsense, frameshift, missense, and splice-site variants distributed across the two coding exons and occasionally in regulatory sequences.[4][10][11] Hart et al. described an exon 1 nonsense mutation (856C→T) that introduces a premature stop codon at amino acid 286, as well as three exon 2 variants: a single nucleotide deletion (2692delA) in codon 349, causing a frameshift and premature termination; a two-base pair deletion (2673–2674delCT) producing a stop codon at amino acid 343; and a G→A substitution in codon 429 (2931G→A), introducing a premature termination at amino acid 429.[4] All affected individuals in that study were homozygous for one of these mutations, traceable to common ancestors in each family, while heterozygous relatives showed no signs of palmoplantar hyperkeratosis or severe early onset periodontitis.[4]  

Subsequent mutation screening in multiple populations revealed additional pathogenic CTSC alleles, and a 2014 review by Nagy and colleagues noted that “to date, a total of 75 different disease-causing mutations have been published for the CTSC gene,” with PLS, HMS, and AP1 collectively representing the phenotypic spectrum of CTSC-related disorders.[10] These mutations include canonical loss-of-function variants—such as nonsense and frameshift changes that truncate the protein and abolish enzymatic activity—as well as missense substitutions that alter critical residues in the catalytic domain or disrupt protein folding. ClinVar archives individual CTSC variants, such as NM_001814.6(CTSC):c.1141del (p.Leu381fs), classified as pathogenic by GeneDx based on clinical testing; this deletion at cytogenetic location 11q14.2 results in a frameshift leading to an abnormal L381fs truncated protein, consistent with loss-of-function.[11]  

Genotype–phenotype correlations within CTSC-related disease are only partially understood. Most PLS-causing mutations appear to completely abolish cathepsin C activity, and there is no clear evidence that particular variant types (e.g., nonsense vs frameshift) confer systematically different severity of palmoplantar keratoderma or periodontitis.[3][4][6][10][15] However, some missense mutations may allow residual CTSC activity, and it has been suggested that such alleles could be associated with milder or more localized keratoderma or with isolated aggressive periodontitis without full PLS features, as in AP1.[10][15] Furthermore, certain founder mutations have been observed in specific populations (for example, Turkish families studied by Hart et al.), and these may define local genotype–phenotype clusters.[4][10]  

At the variant classification level, CTSC mutations associated with PLS are overwhelmingly categorized as “pathogenic” under ACMG/AMP criteria, given strong segregation with disease, functional data demonstrating reduced or absent CTSC activity, and absence or extreme rarity of the variants in general population databases such as gnomAD.[10][11][12] There is no evidence for somatic CTSC mutations contributing to PLS; all reported variants are germline and inherited in a Mendelian fashion, although CTSC variants have been explored in other contexts (e.g., tumor genomics) without clear linkage to Papillon–Lefèvre-like phenotypes.[11][12]  

### 2.3 Non-genetic and Environmental Contributors

Although CTSC mutations are necessary and sufficient for the manifestation of classical PLS, environmental and microbial factors modulate the severity and timing of disease expression, particularly in the oral cavity. Dental and periodontology literature consistently implicates Gram-negative anaerobic pathogens such as *Aggregatibacter actinomycetemcomitans* (formerly *Actinobacillus actinomycetemcomitans*) and *Capnocytophaga* species as major contributors to the aggressive periodontitis observed in PLS.[3][8] These organisms colonize the subgingival environment early in life, and their virulence factors—leukotoxins, proteases, and inflammatory mediators—interact with the host’s compromised immune defenses to drive rapid breakdown of periodontal tissues.[3][8]  

A recent salivary microbiome study of three sisters with PLS provides more granular evidence of microbial heterogeneity and its potential role in modulating phenotypes.[9] The sister with advanced periodontitis (PLST) showed domination of the salivary microbiota by uncultured *Bacterioidales* (F0058), *Fusobacterium*, *Treponema*, and *Sulfophobococcus* (Archaea), reflecting a dysbiotic community enriched in proteolytic and inflammatory taxa.[9] In contrast, her sister PLSTL1 had microbiota dominated by *Streptococcus*, *Haemophilus*, and *Caldivirga* (Archaea), while PLSTL2 showed higher abundances of *Lactobacillus* and *Porphyromonas*, suggesting that even within a single family with shared CTSC mutations, differences in oral microbial composition may influence periodontal disease severity.[9]  

Lifestyle and environmental factors such as oral hygiene practices, access to dental care, smoking status, diet, and socioeconomic conditions likely also modulate disease expression, although systematic data specific to PLS are limited.[3][5][8][15] Anecdotal reports suggest that rigorous oral hygiene combined with early and sustained prophylactic antibiotic therapy may slow the progression of periodontal destruction and delay tooth loss, whereas poor dental care and persistent exposure to pathogenic biofilms accelerate tissue breakdown.[3][8][15] Similarly, cutaneous manifestations may be exacerbated by mechanical friction, exposure to irritants, and secondary infections, although palmoplantar keratoderma tends to remain prominent even with standard dermatologic care.[3][6][8][13]  

Consanguinity operates as an epidemiologic risk factor rather than an environmental cause per se, but it is highly relevant to PLS etiology. Multiple case series have reported parental consanguinity in approximately one-third of PLS cases, and one study estimated consanguinity rates of 20–40%, reflecting the high likelihood of homozygosity for rare CTSC mutations in consanguineous populations.[5][16] This observation underscores the importance of genetic counseling and carrier testing in communities where consanguineous marriage is common, as such practices increase the probability of autosomal recessive disorders like PLS but do not directly modify the effect of CTSC mutations at the cellular or molecular level.[5][16]  

### 2.4 Gene–Environment Interactions

The interplay between CTSC-mediated genetic susceptibility and environmental exposure, particularly to oral and cutaneous microbes, represents a critical gene–environment axis in PLS pathogenesis. CTSC deficiency disrupts the activation of neutrophil and NK cell serine proteases that normally mediate rapid clearance of bacterial infections and regulation of local inflammatory responses, thereby enhancing the pathogenic impact of periodontal microorganisms.[3][6][15] In a typical individual, colonization by *A. actinomycetemcomitans* and other periodontal pathogens may lead to chronic or episodic periodontitis, but in PLS patients, the same organisms encounter an immune environment in which key proteolytic effectors are inactive, allowing unchecked proliferation and deeper invasion into periodontal tissues.[3][8][15]  

Patel et al. highlighted that “loss of CTSC function and subsequent inactivity of neutrophil serine proteinases may cause deregulation of localized PMNs’ response in inflamed periodontal tissues, leading to the severe tissue destruction in PLS,” emphasizing that the local leukocyte response is not simply diminished but qualitatively altered.[3] Immune cells may still be recruited to sites of infection, but their effector repertoire is compromised, potentially leading to prolonged inflammation, excessive release of non-proteolytic mediators, and collateral damage to periodontal ligaments and alveolar bone.[3][6][15] This scenario exemplifies a gene–environment interaction wherein the inherited defect in a protease cascade amplifies the tissue-damaging potential of environmental microbes beyond what would be seen in genetically intact hosts.  

Similarly, in the skin, environmental and mechanical factors interact with CTSC deficiency to shape keratoderma severity. Cathepsin C is expressed in palmoplantar keratinocytes and is believed to participate in desquamation and terminal differentiation pathways; its absence may render the stratum corneum more susceptible to thickening and hyperkeratosis in response to mechanical stress, friction, or minor injuries.[4][6][10][15] While palmoplantar keratoderma develops even in children who are not exposed to unusual mechanical workloads, the degree of plaque formation, fissuring, and extension onto the dorsal surfaces of hands and feet can be influenced by activity patterns, footwear, and occlusive conditions.[3][6][8][16]  

No formal gene–environment interaction studies (e.g., GxE analyses using genome-wide methods) have been conducted in PLS, and the rarity of the disease makes such approaches challenging.[3][10][15] Nevertheless, the conceptual framework is clear: CTSC loss-of-function provides a necessary genetic substrate, and environmental exposures—especially to specific oral pathogens and mechanical stressors—modulate the phenotypic manifestation through additive and possibly synergistic effects on immune and epithelial biology. In ontology terms, relevant gene–environment interactions may be captured under GO biological processes such as “response to bacterium” (GO:0009617) and “regulation of inflammatory response” (GO:0050727), with cell types including neutrophils (CL:0000094), NK cells (CL:0000623), and keratinocytes (CL:0000312) acting as central mediators.  

---

## 3. Phenotypes and Clinical Spectrum

### 3.1 Dermatologic Manifestations: Palmoplantar Keratoderma

The dermatologic hallmark of PLS is diffuse palmoplantar hyperkeratosis, clinically manifesting as erythematous, thickened plaques on the palms and soles that often extend onto the dorsal surfaces of hands and feet.[3][5][6][8][16] This palmoplantar keratoderma typically appears between one and four years of age, often coinciding with or shortly preceding the onset of periodontal symptoms, and persists throughout life, although its severity may fluctuate.[3][5][6][8][16] In Ahmad et al.’s description, “Palmoplantar hyperkeratosis typically starts between 1–4 years of age. The erythematous keratotic plaques may be focal or diffuse and are characterized by transgradient extension of keratoderma to the dorsal surface of palms and soles,” highlighting the characteristic “transgradient” spread beyond classic palmoplantar boundaries.[6]  

Clinically, affected skin appears thickened, scaly, and often fissured, with accompanying erythema and, in many cases, hyperhidrosis. Patients frequently complain of pain, burning, and discomfort when walking or grasping objects, and the hyperkeratotic plaques may interfere with fine motor tasks and weight-bearing activities.[3][6][16] Secondary infections—most often bacterial but occasionally fungal—can complicate the keratoderma, leading to pustules, erosions, and malodor, especially when plaques become macerated or cracked.[3][6][13] The keratoderma is generally symmetric and involves both palms and soles, although focal variations and involvement of other pressure-bearing or flexural sites (such as knees and elbows) have been reported.[4][6][16]  

From a phenotypic ontology perspective, palmoplantar keratoderma in PLS can be annotated using HPO terms such as “Palmoplantar keratoderma” (HP:0000982), “Erythematous plaques” (HP:0003610), and “Hyperhidrosis” (HP:0000977). The age of onset can be tagged with “Childhood onset” (HP:0003593), and the transgradient spread may be captured by “Extensor involvement” or “Keratoderma extending onto dorsal surfaces,” though the latter is more descriptive than formally codified.[6][16] Severity spans mild to severe; in many cases, plaques are thick enough to significantly impair mobility, representing a serious quality-of-life burden. The course is chronic and relatively stable, with possible partial improvement during adolescence or with effective treatment, but complete resolution is rare.[3][6][8][13]  

Quality-of-life impact of palmoplantar keratoderma in PLS is substantial. Painful fissures and thickened skin impair walking and standing, leading to limitations in participation in school, work, and recreational activities.[3][6][16] The conspicuous appearance of hyperkeratotic plaques on hands can provoke social stigma and self-consciousness, particularly in adolescents and young adults, contributing to psychosocial stress and, in some cases, anxiety or depressive symptoms. Moreover, heat intolerance and discomfort due to hyperhidrosis can interfere with daily functioning, especially in warm climates.[3][6][16] These consequences underscore the importance of integrating dermatologic management into overall care plans and justify ontology annotations linking palmoplantar keratoderma to functional domains such as “Mobility” and “Self-care” in ICF (International Classification of Functioning) frameworks.  

### 3.2 Periodontal Disease and Dentition Abnormalities

Aggressive, early-onset periodontitis is the second cardinal manifestation of PLS and is arguably the most disabling feature, given its profound impact on dentition and oral function.[3][5][6][8][15][16] Periodontal disease in PLS usually begins soon after eruption of the primary dentition, often at three to four years of age, and rapidly progresses to severe gingival inflammation, bleeding, suppuration, deep periodontal pocket formation, and extensive alveolar bone resorption.[3][5][6][8][16] Deciduous teeth typically become mobile and are shed prematurely, sometimes by age four or five, and similar destructive processes recur upon eruption of permanent teeth, leading to eventual loss of nearly all dentition by adolescence.[3][5][6][8][16]  

Patel et al. summarized this clinical picture as follows: “Papillon–Lefèvre syndrome (PLS) is a rare autosomal recessive disorder, characterized by diffuse palmoplantar keratoderma and precocious aggressive periodontitis, leading to premature loss of deciduous and permanent dentition at a very young age.”[3] The OMIM entry echoes this, noting that “both the milk teeth and the permanent teeth are lost prematurely,” and that severe periodontitis is integral to the PLS phenotype.[1] Radiographic evaluations typically reveal generalized horizontal and vertical bone loss around affected teeth, with a “floating teeth” appearance due to marked alveolar resorption.[3][5][6][16] Orthopantomographs and intraoral periapical radiographs are often used to document this pattern and to monitor disease progression or treatment effects.[3]  

Clinically, the periodontal phenotype in PLS fits the category of “advanced periodontitis as a manifestation of systemic disease, stage IV, grade C,” as noted in the salivary microbiome study by Marques et al., where one sister (PLST) presented with gingival bleeding, suppuration, and severe tooth mobility.[9] HPO terms such as “Periodontitis” (HP:0004600), “Premature loss of teeth” (HP:0006480), “Alveolar bone loss” (HP:0003795), and “Gingivitis” (HP:0002976) capture major aspects of this phenotype. The age of onset is “Early childhood,” the severity is “Severe,” and the course is “Progressive,” with episodic exacerbations corresponding to peaks of infection and inflammation.[3][5][6][8][9][16]  

The impact of periodontal disease and resulting edentulism on quality of life is profound. Children with PLS experience pain, difficulty chewing, and bleeding gums, and may avoid eating certain foods, leading to nutritional compromise.[3][5][6][16] Loss of teeth affects speech articulation and aesthetic appearance, which can be particularly distressing in school-age children and adolescents, resulting in social isolation, low self-esteem, and psychosocial distress.[3][5][16] Adults with PLS may require extensive prosthodontic rehabilitation, including removable dentures or dental implants, and face ongoing challenges in maintaining oral hygiene and dealing with dry mouth or altered salivary function.[8][9] In terms of functional classification, PLS-related periodontitis and tooth loss intersect with ICF domains of “Communication,” “Self-care,” “Social interactions,” and “Participation in employment or education.”  

### 3.3 Infectious Susceptibility and Immunologic Features

Increased susceptibility to cutaneous and systemic infections is a recognized, though variably expressed, component of PLS. Approximately 20% of patients exhibit recurrent pyogenic skin infections, abscesses, or systemic infections such as pneumonia or sepsis, often caused by common bacterial pathogens but occurring with unusual frequency or severity.[6][16] Ahmad et al. noted that “About 20% patients with Papillon-Lefevre syndrome have an increased susceptibility to infections due to some dysfunction of the immune system,” linking clinical observations to underlying immunologic abnormalities.[6]  

Mechanistic studies have documented impaired chemotactic and phagocytic function of polymorphonuclear leukocytes (PMNs) in several PLS cohorts, as well as reduced CTSC activity in neutrophils and monocytes.[3] Patel et al. described “an impaired chemotactic and phagocytic function of polymorphonuclear leukocytes (PMNs) in several studies,” and highlighted that CTSC-deficient neutrophils fail to properly activate serine proteinases, altering their antibacterial capacity.[3] More recently, the same review reported that “impairment of natural killer cell cytotoxic function is the first consistent immune dysfunction in PLS,” suggesting a broader impact on cytotoxic lymphocyte pathways beyond neutrophils.[3] Ahmad et al. similarly emphasized that CTSC is essential for granzyme B activation and NK cell cytolytic activity, and that its deficiency may underlie the propensity for recurrent pyogenic infections.[6]  

Clinically, infections in PLS often involve the skin (impetigo, folliculitis, abscesses), mucosal surfaces, and occasionally deeper tissues. HPO terms such as “Recurrent skin infections” (HP:0001581), “Recurrent respiratory infections” (HP:0002205), and “Increased susceptibility to bacterial infections” (HP:0002718) may be appropriate annotations. The age of onset is typically early childhood, concurrent with skin and periodontal manifestations, and severity ranges from mild recurrent superficial infections to life-threatening systemic episodes, although the latter are relatively rare.[3][6][16]  

Quality-of-life impact of recurrent infections includes pain, fever, and missed school or work, as well as anxiety about health and potential complications. Families often become vigilant in monitoring for signs of infection, and some individuals may require repeated courses of antibiotics or hospitalizations, contributing to healthcare burden and psychosocial stress.[3][6][16] The immune phenotype invites further ontological annotation with GO processes such as “immune response” (GO:0006955), “neutrophil-mediated immunity” (GO:0002446), and “NK cell mediated cytotoxicity” (GO:0002228), and cell types including neutrophils (CL:0000094) and NK cells (CL:0000623).  

### 3.4 Neurologic and Developmental Features

Neurologic and developmental features in PLS are less common and more variable than dermatologic and periodontal manifestations, but have been reported in several case descriptions. Patel et al. and Ahmad et al. cite earlier literature documenting intracranial calcifications and mental retardation (intellectual disability) in a subset of PLS patients, often in association with more severe systemic involvement.[3][6] The pathophysiologic basis for these findings is unclear, and they may reflect either direct consequences of CTSC deficiency in neural tissues or secondary effects of repeated infections and systemic inflammation.  

Intracranial calcifications, when present, are typically detected by neuroimaging and have been described as involving basal ganglia or cortical structures, though detailed neuroanatomic mapping in PLS is limited. HPO terms such as “Intracranial calcification” (HP:0006802) and “Intellectual disability” (HP:0001249) can be used to annotate these features, with age of onset generally in childhood. Expressivity appears highly variable; many PLS patients have normal cognitive development and neurologic examinations, while others exhibit mild to moderate learning difficulties or developmental delays.[3][6][16]  

Quality-of-life impact of neurologic features depends on severity. Intellectual disability and intracranial calcifications can contribute to educational challenges, reduced independence, and increased caregiving needs, amplifying the overall disease burden. However, due to limited systematic data and potential confounding by other factors, caution is warranted in attributing neurologic deficits solely to PLS; ontological annotations should reflect these features as “occasional” or “variable” rather than core components of the syndrome.  

### 3.5 Psychosocial and Quality-of-life Impact

Although not always explicitly detailed in case reports, the psychosocial impact of PLS is substantial, arising from visible skin lesions, early loss of teeth, recurrent infections, and associated functional limitations. Children and adolescents with PLS may experience bullying or social isolation due to their appearance, and edentulism can profoundly affect self-image and interpersonal interactions.[3][5][6][16] Speech difficulties and altered facial aesthetics may contribute to embarrassment and reluctance to engage in social activities, while chronic skin discomfort and infection-related morbidity can lead to fatigue and decreased participation in school or work.[3][6][16]  

There are no PLS-specific validated quality-of-life instruments, and formal studies using generic tools such as EQ-5D or SF-36 are lacking. However, extrapolation from related conditions (palmoplantar keratoderma, aggressive periodontitis, ectodermal dysplasias) suggests that domains of physical functioning, bodily pain, social functioning, and mental health are particularly affected.[3][5][8][16] For example, early complete edentulism is associated with reduced oral health-related quality of life, while palmoplantar keratoderma limits physical functioning and may cause chronic pain and embarrassment.  

Ontology frameworks such as HPO can capture some aspects of psychosocial impact through phenotypes like “Anxiety” (HP:0000739) or “Depression” (HP:0000716), but more granular classification requires linkage to ICF domains and patient-reported outcome measures. Clinicians and researchers should therefore be encouraged to document psychosocial outcomes in future PLS cohorts, enabling more systematic characterization of quality-of-life trajectories and informing comprehensive care strategies.  

---

## 4. Genetic and Molecular Information

### 4.1 CTSC Gene Structure, Expression, and Protein Biology

The CTSC gene encodes cathepsin C, also known as dipeptidyl peptidase I (DPPI), a lysosomal cysteine protease of the papain family that plays a central role in activating serine proteases within immune cells and certain epithelial tissues.[1][4][6][10][15] Hart et al. described CTSC as a 4.7 kb gene consisting of two exons and reported that its mRNA is expressed at high levels in polymorphonuclear leukocytes, macrophages, and their precursors, as well as in epithelial regions commonly affected by PLS, including palms, soles, knees, and oral keratinized gingiva.[4]  

Structurally, cathepsin C is synthesized as a preproenzyme that undergoes multiple processing steps to yield an active tetramer composed of heavy and light chains, each containing a catalytic site. The enzyme resides in lysosomes and specialized granules of neutrophils, mast cells, and cytotoxic lymphocytes, where it removes dipeptides from the N-terminus of protein substrates, thereby enabling activation of pro-serine proteases such as neutrophil elastase, cathepsin G, proteinase 3, and granzymes A and B.[3][4][6][10][15]  

UniProt and structural databases (not specifically cited in the provided search results but widely referenced in the literature) classify cathepsin C under GO molecular function “dipeptidyl-peptidase activity” (GO:0008238) and GO cellular component “lysosome” (GO:0005764), with broad expression in immune cells and certain epithelial compartments. Ahmad et al. emphasized that CTSC is “essential for granzyme B activation and NK cell cytolytic activity,” underscoring its role in cytotoxic lymphocyte function.[6]  

The CTSC locus at 11q14.2 lies in a genomic region that has been the focus of constraint metrics analyses in large population sequencing databases such as gnomAD. Although CTSC-specific constraint scores are not detailed in the provided gnomAD v4.1.1 release summary, the update notes that gene constraint metrics—such as the loss-of-function observed/expected upper bound fraction (LOEUF)—are calculated for all coding loci to estimate mutational intolerance and aid in variant interpretation.[12] Given the rarity of PLS and the predominance of truncating CTSC variants in affected individuals, CTSC is likely moderately intolerant to homozygous loss-of-function, but shows tolerance for heterozygous loss-of-function, consistent with the clinically unaffected status of carriers.[4][10][12]  

### 4.2 Spectrum of Pathogenic Variants

As noted earlier, at least 75 distinct disease-causing mutations have been reported in CTSC, comprising nonsense, frameshift, missense, and splice-site changes distributed across both exons and occasionally involving intronic or regulatory regions.[10] Hart et al.’s initial report identified four truncating mutations in consanguineous Turkish families.[4] Subsequent studies across diverse populations have added numerous variants, some recurrent and some unique.  

ClinVar provides rich variant-level annotation, including the frameshift deletion NM_001814.6(CTSC):c.1141del (p.Leu381fs), located at cytogenetic band 11q14.2 and classified as pathogenic based on clinical testing.[11] The variant leads to a frameshift at codon 381, producing an aberrant protein predicted to undergo nonsense-mediated decay or to lack catalytic activity. CTSC variants associated with Haim-Munk syndrome and aggressive periodontitis type 1 often reside in the same gene, further supporting CTSC as a central node in a phenotypic spectrum and reminding clinicians that CTSC mutations can manifest with overlapping but distinct clinical patterns.[1][10][15]  

From a structural and functional standpoint, pathogenic CTSC variants generally disrupt the enzyme’s active site, its dimerization or tetramerization interface, or its trafficking to lysosomes, resulting in absent or severely reduced enzymatic activity.[3][4][6][10][15] Nonsense and frameshift variants produce truncated proteins that cannot fold correctly or are degraded rapidly, while missense variants may alter key catalytic residues or destabilize the protein. Splice-site mutations can lead to exon skipping or intron retention, again yielding nonfunctional or partially functional proteins.  

Variant classification under ACMG/AMP guidelines for CTSC is facilitated by strong segregation data, functional assays documenting reduced CTSC activity, and absence of pathogenic variants in large population datasets. For example, variants that have been observed only in PLS patients, show clear segregation in multiple affected family members, and have supportive functional data—such as those described by Hart et al. and Nagy et al.—are classified as “pathogenic.”[4][10][11] Variants with less extensive evidence may be designated “likely pathogenic” or “VUS” (variants of uncertain significance), but such categorization is rare in the context of classical PLS, where CTSC truncating variants are generally clear-cut.[10][11]  

### 4.3 Molecular Consequences and Loss-of-function Mechanisms

The molecular consequences of CTSC mutations in PLS are dominated by loss-of-function effects. Enzymatic assays in PLS patients consistently show profound reductions—often more than 90%—in CTSC activity, and obligate carriers show partial reductions consistent with haploinsufficiency.[3][4][6][10][15] Patel et al. summarized that “Various studies in PLS patients have shown more than 90% reduction in CTSC activity with resultant reduced host response against bacteria,” linking biochemical deficits to immunologic vulnerability.[3]  

Functionally, CTSC loss-of-function impairs activation of neutrophil serine proteases, including neutrophil elastase, cathepsin G, and proteinase 3, as well as granzymes in NK cells and cytotoxic T lymphocytes.[3][4][6][10][15] These proteases are critical for degradation of invading pathogens, regulation of inflammatory responses, and execution of cytotoxic killing, and their inactive proforms accumulate in CTSC-deficient cells. As a result, neutrophils and NK cells in PLS patients show defective bactericidal activity and reduced cytotoxicity, respectively, while local inflammatory responses become dysregulated.[3][6][15]  

As Patel et al. note, “loss of CTSC function and subsequent inactivity of neutrophil serine proteinases may cause deregulation of localized PMNs’ response in inflamed periodontal tissues, leading to the severe tissue destruction in PLS.”[3] This suggests that the absence of regulated protease activity leads not simply to immune deficiency but to maladaptive inflammation, with neutrophils releasing abnormal patterns of cytokines, reactive oxygen species, and other mediators that cause collateral damage to periodontal ligaments and alveolar bone. In NK cells and cytotoxic T lymphocytes, impaired granzyme activation compromises killing of infected cells, potentially allowing persistent, low-level infections that maintain chronic inflammation.[3][6]  

In keratinocytes, the role of CTSC is less well defined, but its expression in palmoplantar epithelium suggests involvement in keratinocyte differentiation, desquamation, or turnover of structural proteins. CTSC deficiency may disrupt proteolytic processing of substrates involved in cornified envelope formation or in desquamation, leading to accumulation of hyperkeratotic plaques. GO terms such as “keratinocyte differentiation” (GO:0030216) and “epidermis development” (GO:0008544) may capture these processes, although specific CTSC substrates in the skin remain to be fully identified.[4][6][10][15]  

To date, there is no evidence for CTSC gain-of-function mutations causing PLS or related conditions, nor for dominant-negative effects within CTSC tetramers. All known PLS-causing variants behave as loss-of-function alleles, and CTSC-related disease follows a recessive pattern consistent with the requirement for both alleles to be disrupted to abolish enzymatic activity.[1][4][10][11][15]  

### 4.4 Modifier Genes, Epigenetics, and Chromosomal Context

Modifier genes that influence PLS severity or expressivity have not been definitively identified. Differences in periodontal disease severity and skin manifestations between individuals with identical CTSC mutations suggest the existence of genetic or epigenetic modifiers, but systematic studies are lacking due to the rarity of the syndrome and the small size of available cohorts.[3][9][10][15] Potential candidates include genes involved in innate immunity, cytokine signaling, and keratinization pathways, as well as genetic variants affecting oral microbiome composition and local tissue responses.  

Epigenetic information specific to PLS is not available in the current literature; no DNA methylation, histone modification, or chromatin structure studies have been reported in PLS patients or CTSC-deficient tissues.[3][10][15] However, cathepsin C functions within lysosomes, and its activity is influenced by cellular metabolic status, lysosomal pH, and trafficking pathways, which can be modulated by epigenetic and environmental factors. It is conceivable that epigenetic regulation of CTSC expression or of downstream targets affects disease severity, but this remains speculative.  

Chromosomal abnormalities are not implicated in PLS. The CTSC locus resides on 11q14.2–q14.3, and PLS is caused by sequence-level mutations rather than large-scale deletions, duplications, translocations, or inversions.[1][10][11][15] Chromosomal microarray or karyotyping in PLS patients is typically normal, and absence of CTSC mutations in individuals with palmoplantar keratoderma or aggressive periodontitis suggests other causes rather than structural rearrangements involving CTSC.[10][15]  

Ontology suggestions for genetic and molecular aspects include HGNC:2516 (CTSC), OMIM:602365 (CTSC gene), GO:0008238 (dipeptidyl-peptidase activity), GO:0005764 (lysosome), and MONDO:0009490 (Papillon–Lefèvre syndrome).  

---

## 5. Environmental and Lifestyle Contributors

### 5.1 Oral Microbiome and Periodontal Pathogens

The oral microbiome plays an essential environmental role in PLS-related periodontitis, interacting with CTSC-deficient immune responses to drive aggressive tissue destruction. Classical periodontitis in the general population involves a polymicrobial biofilm of predominantly Gram-negative anaerobes, and in PLS, specific taxa such as *Aggregatibacter actinomycetemcomitans* and *Capnocytophaga* spp. have been repeatedly associated with disease.[3][8] These bacteria produce leukotoxins and proteases that impair host defenses and degrade connective tissue, and their presence in the subgingival environment of PLS patients may be especially deleterious given underlying defects in neutrophil and NK cell function.[3][8][15]  

The 2021 salivary microbiome study of three sisters with PLS provides detailed insight into the heterogeneity of oral microbial communities and their potential linkage to disease severity.[9] The sister with advanced periodontitis (PLST) had salivary microbiota dominated by uncultured *Bacterioidales* (F0058), *Fusobacterium*, *Treponema*, and *Sulfophobococcus* (Archaea), organisms frequently associated with severe periodontal disease.[9] Her siblings showed different dominant taxa, including *Streptococcus*, *Haemophilus*, *Caldivirga*, *Lactobacillus*, and *Porphyromonas*, suggesting that community composition may modulate clinical expression even among genetically identical individuals.[9] All three sisters exhibited hyposalivation, potentially exacerbating periodontal vulnerability by reducing mechanical cleansing and buffering capacity.[9]  

Environmental factors such as diet, oral hygiene, and antibiotic exposure shape the oral microbiome and may influence disease trajectory in PLS. High-sugar diets, poor brushing and flossing habits, and lack of regular dental care favor pathogenic biofilm development, whereas meticulous oral hygiene, regular professional cleanings, and strategically timed antibiotic courses can reduce bacterial load and alter community composition.[3][8][15] In addition, smoking and systemic conditions such as diabetes—while not systematically studied in PLS—are known risk factors for periodontitis in the general population and may act synergistically with CTSC deficiency.  

Ontology annotations relevant to the oral microbiome include bacterial taxa (NCBI Taxonomy IDs), HPO terms such as “Hyposalivation” (HP:0000217), and CHEBI entries corresponding to antibiotic agents used for prophylaxis (e.g., CHEBI:18224 for amoxicillin, CHEBI:6821 for metronidazole). GO biological processes such as “response to bacterium” (GO:0009617) and “regulation of inflammatory response” (GO:0050727) capture host side interactions with the microbiome.  

### 5.2 Lifestyle and Socio-environmental Factors

Lifestyle factors, including hygiene practices, footwear choices, occupational exposures, and nutrition, likely influence PLS manifestations, especially keratoderma and periodontal disease, although formal studies are limited.[3][5][8][15] In palmoplantar keratoderma, mechanical stress and occlusion (e.g., heavy labor, tight or non-breathable footwear) can exacerbate plaque formation and fissuring, while regular emollient application, avoidance of irritants, and appropriate footwear can mitigate symptoms.[3][6][8][13] Socioeconomic context may determine access to dermatologic care and keratolytic treatments, thereby indirectly affecting severity.  

Nutritional status may also contribute to overall immune competence and tissue repair capacity. Deficiencies in micronutrients important for immune function and skin integrity—such as vitamin A, vitamin D, zinc, and protein—could worsen PLS manifestations, though this remains largely theoretical. Conversely, balanced nutrition and avoidance of extreme diets may support better outcomes. No specific dietary protective factors have been identified for PLS, and current management focuses on general healthy diet recommendations.  

From a socio-environmental perspective, PLS patients often face barriers to care due to the rarity of the condition, lack of local expertise, and financial constraints. In settings with limited dental and dermatologic services, aggressive periodontitis and keratoderma may remain untreated, leading to worse functional outcomes. Conversely, in resource-rich environments, early diagnosis and multidisciplinary management can substantially improve quality of life. These gradients underscore the importance of public health and health systems factors as environmental contributors, even when the underlying genetic etiology is uniform.  

In ontology terms, lifestyle and socio-environmental factors intersect with NCIT concepts such as “Health Behavior” (NCIT:C12219) and “Socioeconomic Factors” (NCIT:C17010), and can be incorporated into disease knowledge bases as contextual modifiers rather than primary etiologic agents.  

---

## 6. Mechanisms and Pathophysiology

### 6.1 CTSC-Dependent Protease Cascades in Immunity

At the core of PLS pathophysiology lies disruption of CTSC-dependent protease cascades in immune cells. Cathepsin C is responsible for activating a family of serine proteases by removing N-terminal dipeptides from proenzymes, a step required for maturation and full enzymatic activity.[3][4][6][10][15] In neutrophils, these proteases include neutrophil elastase, cathepsin G, and proteinase 3, all stored in azurophilic granules and deployed to degrade invading pathogens and modulate inflammatory responses.[3][4][6][10][15] In NK cells and cytotoxic T lymphocytes, CTSC activates granzymes A and B, which are essential for inducing apoptosis in infected or malignant target cells.[6][15]  

In CTSC-deficient PLS patients, these proteases remain in inactive pro-forms, profoundly altering the functional repertoire of neutrophils and cytotoxic lymphocytes. As Ahmad et al. noted, “patient may have impaired function of the immunological system, associated most probably with insufficiency of cathepsin C, which is essential for granzyme B activation and NK cell cytolytic activity,” and this insufficiency manifests clinically as susceptibility to infections.[6] Patel et al. added that “impairment of natural killer cell cytotoxic function is the first consistent immune dysfunction in PLS,” suggesting that NK cell defects may be especially central to disease pathogenesis.[3]  

GO terms capturing these processes include “neutrophil degranulation” (GO:0043312), “neutrophil mediated immunity” (GO:0002446), “NK cell mediated cytotoxicity” (GO:0002228), and “activation of proenzyme” (GO:0016500). Cell ontology terms encompass neutrophils (CL:0000094), NK cells (CL:0000623), and cytotoxic T cells (CL:0000910).  

It is important to note that PLS does not typically present with global immunodeficiency; many patients control infections relatively well, and opportunistic infections common in severe immunodeficiencies (e.g., Pneumocystis pneumonia, disseminated fungal infections) are not characteristic.[3][6][16] The immune defect in PLS is thus selective and tissue-specific, most prominently affecting periodontal tissues and palmoplantar skin, likely due to specific microenvironmental factors and the unique demands placed on neutrophils and NK cells in these niches.  

### 6.2 Pathogenesis of Aggressive Periodontitis

The pathogenesis of aggressive periodontitis in PLS involves a complex interplay between CTSC-deficient neutrophils and NK cells, a dysbiotic oral microbiome, and the unique structure of periodontal tissues. Periodontal health depends on a delicate balance between commensal and pathogenic microbes in the gingival sulcus and the host’s immune response; in PLS, this balance is disrupted.[3][8][9][15]  

CTSC-deficient neutrophils exhibit defective protease-mediated bacterial killing and altered chemotactic and phagocytic activity, allowing periodontal pathogens such as *A. actinomycetemcomitans* and *Capnocytophaga* spp. to proliferate in subgingival plaque.[3][8][15] These bacteria produce leukotoxins and other virulence factors that further impair neutrophil function and induce release of pro-inflammatory cytokines. NK cell defects compromise killing of infected or stressed gingival epithelial cells, prolonging microbial persistence and contributing to chronic inflammatory stimuli.[3][6][15]  

The result is a persistent inflammatory infiltrate in periodontal tissues, composed of neutrophils, macrophages, and lymphocytes, with elevated levels of cytokines such as IL-1β, TNF-α, and IL-6, and matrix metalloproteinases that degrade collagen and other components of the periodontal ligament.[3][8][15] In CTSC-deficiency, neutrophil serine proteases are inactive, altering the normal regulation of these inflammatory mediators and potentially tipping the balance toward destructive pathways. Alveolar bone resorption is driven by osteoclast activation and RANKL signaling, processes that are enhanced in chronic inflammation and may be further dysregulated in PLS.[3][8][15]  

Marques et al.’s microbiome study exemplifies the endpoint of these processes: advanced periodontitis with bone loss and premature tooth loss, associated with a salivary microbiome dominated by anaerobic pathogens and archaea.[9] The clinical staging as “advanced periodontitis as a manifestation of systemic disease, stage IV, grade C” underscores that PLS-related periodontitis represents one of the most severe forms of periodontal breakdown.[9]  

GO terms relevant to this pathogenesis include “inflammatory response” (GO:0006954), “osteoclast differentiation” (GO:0030316), and “regulation of bone resorption” (GO:0045124). Anatomical ontology terms involve periodontal tissues such as the gingiva (UBERON:0001838), periodontal ligament (UBERON:0002503), and alveolar bone (UBERON:0004732).  

### 6.3 Pathogenesis of Palmoplantar Keratoderma

The pathogenesis of palmoplantar keratoderma in PLS is less well defined than that of periodontitis, but is generally interpreted as a consequence of CTSC deficiency in palmoplantar keratinocytes and associated structures. CTSC expression in palms, soles, and knees suggests a role in epidermal differentiation or desquamation, and its absence may disrupt proteolytic processing of structural proteins or corneodesmosomes, leading to retention hyperkeratosis and plaque formation.[4][6][10][15]  

Palmoplantar skin is subjected to high mechanical stress, and keratinocytes in these regions have specialized differentiation programs that produce thick, protective stratum corneum. CTSC may regulate turnover of this layer by activating proteases that degrade corneodesmosomes and facilitate shedding of corneocytes. Loss of CTSC could lead to accumulation of corneocytes and thickening of the stratum corneum, resulting in clinically evident hyperkeratosis.[4][6][10][15]  

Furthermore, local immune interactions likely contribute to keratoderma. Palmoplantar skin is rich in resident immune cells and exposed to environmental microbes and irritants; neutrophil and NK cell dysfunction could alter local inflammatory responses and cytokine milieu, affecting keratinocyte behavior. For example, chronic low-level inflammation might stimulate hyperproliferation or aberrant differentiation of keratinocytes, exacerbating plaque formation.[3][6][15]  

GO terms relevant to skin pathogenesis include “keratinocyte differentiation” (GO:0030216), “epidermis development” (GO:0008544), and “cornification” (GO:0070268). Anatomical ontology terms include “skin of palm” (UBERON:0004278) and “skin of sole of foot” (UBERON:0004262). HPO phenotypes capture clinical manifestations, but mechanistic details at the molecular level (e.g., specific CTSC substrates) remain to be fully elucidated.  

### 6.4 Systems-level Immune and Inflammatory Mechanisms

Beyond localized effects in periodontal tissues and palmoplantar skin, CTSC deficiency has systems-level consequences for immune function and inflammation. CTSC-deficient neutrophils and NK cells circulate throughout the body and may contribute to broader susceptibility to infections and altered inflammatory responses.[3][6][16] It is noteworthy, however, that PLS patients do not generally exhibit catastrophic systemic immunodeficiency; rather, they show a selective pattern of vulnerability, with particular predilection for infections in skin and mucosa.[3][6][16]  

Patel et al. summarized immunologic insights as follows: “Therefore, deficiency of CTSC function will result in loss of immunological response, leading to liability of infection. Recent advances reported that the impairment of natural killer cell cytotoxic function is the first consistent immune dysfunction in PLS.”[3] This statement underscores that while neutrophil defects are documented, the most reproducible immune abnormality appears in NK cell activity, which may have far-reaching effects on viral and bacterial clearance and on regulation of inflammation.  

Chronic inflammation in PLS takes a toll on tissues, particularly periodontal and cutaneous structures. Persistent inflammatory signaling and altered protease activity can promote fibrosis, tissue remodeling, and sometimes scarring. Systemic inflammatory markers (e.g., CRP) may be mildly elevated during infection episodes, and repeated bouts of inflammation could theoretically contribute to long-term cardiovascular or metabolic risks, although this has not been systematically studied in PLS.  

GO terms capturing systemic immune phenomena include “immune system process” (GO:0002376), “innate immune response” (GO:0045087), and “regulation of cytokine production” (GO:0001817). Cell types such as monocytes (CL:0000576), macrophages (CL:0000235), and T cells (CL:0000084) participate in these processes alongside neutrophils and NK cells.  

### 6.5 Unresolved Mechanistic Questions and Emerging Hypotheses

Despite significant progress in understanding CTSC biology and PLS phenotypes, several mechanistic questions remain unresolved. Chief among these is the precise causal chain linking CTSC deficiency to specific tissue manifestations—why palmoplantar skin and periodontal tissues are so prominently affected, while other CTSC-expressing tissues show minimal clinical involvement.[3][4][10][15]  

Patel et al. acknowledged that “despite these advances in characterizing the genetic basis of the syndrome, the pathogenic mechanisms leading to the periodontal involvement remain elusive.”[3] This statement reflects ongoing uncertainty about how CTSC-deficient neutrophils, NK cells, and keratinocytes interact with local microenvironmental factors to produce the observed patterns of tissue destruction and hyperkeratosis. For instance, the relative contributions of bacterial virulence, host cytokine responses, and mechanical stress in driving periodontal and cutaneous disease are not fully quantified.  

Another unresolved area concerns potential systemic effects of CTSC deficiency beyond PLS. CTSC is expressed in multiple tissues, including bone marrow and other epithelial surfaces, and yet PLS manifestations are strikingly focused. This selectivity implies either redundancy in CTSC-related pathways in other tissues or unique vulnerability of palmoplantar skin and periodontium, perhaps due to their high exposure to mechanical and microbial stress and their specialized epithelial and connective tissue architecture.[4][6][10][15]  

Emerging hypotheses include roles for CTSC in regulating local cell death pathways, in modulating the skin and oral epithelial barrier function, and in fine-tuning inflammatory resolution processes. Future multi-omics studies—integrating transcriptomics, proteomics, and metabolomics in PLS tissues—may unravel these mechanisms, but to date, such data are scant.[3][10][15] The 2021 microbiome study represents a first step in applying high-throughput approaches to PLS, and similar technologies applied to skin and immune cells could further refine mechanistic models.[9]  

---

## 7. Anatomical, Tissue, and Cellular Involvement

### 7.1 Organ- and System-level Anatomy

PLS primarily affects the integumentary and dental systems, with secondary involvement of immune and, occasionally, neurologic systems. Organ-level structures prominently involved include the skin of palms and soles, gingiva, periodontal ligaments, alveolar bone of the jaws, and teeth.[3][5][6][8][15][16] UBERON terms appropriate for these structures include “skin of palm” (UBERON:0004278), “skin of sole of foot” (UBERON:0004262), “gingiva” (UBERON:0001838), “periodontal ligament” (UBERON:0002503), “alveolar process of maxilla” (UBERON:0004707), and “alveolar process of mandible” (UBERON:0004705).  

The integumentary involvement is restricted predominantly to palmoplantar skin but can extend to other areas, such as knees and elbows, with diffuse or focal keratoderma. The dental involvement encompasses both primary and permanent dentitions, affecting crown stability, root support, and surrounding alveolar bone. The immune system’s involvement is systemic, reflecting CTSC expression in neutrophils, macrophages, NK cells, and other immune lineages.[4][6][10][15] Neurologic involvement, when present, concerns intracranial calcifications and cognitive function, but these remain infrequent and are not considered primary organ-level manifestations.[3][6]  

Body systems implicated in PLS include the integumentary system (skin and associated structures), digestive system (oral cavity and mastication), immune system (innate and cytotoxic pathways), and, occasionally, nervous system. Cardiovascular, respiratory, endocrine, and other systems are generally unaffected, except indirectly through infection or inflammation.  

### 7.2 Tissue-level Pathology

At the tissue level, PLS manifests in stratified squamous epithelium, connective tissues, and bone. Palmoplantar keratoderma involves thickening of the stratum corneum, hyperkeratosis, parakeratosis, and sometimes acanthosis. Histologic descriptions in related literature show marked orthokeratotic or parakeratotic hyperkeratosis with underlying papillary dermal inflammation and occasional epidermal hyperplasia.[3][6][13] These features are typical of hereditary palmoplantar keratodermas and likely apply to PLS, although PLS-specific histopathologic series are limited.  

Periodontal tissue pathology includes chronic inflammatory infiltrates in gingiva, destruction of collagen fibers in the periodontal ligament, and alveolar bone resorption. Radiographically, bone loss is evident as decreased height of alveolar bone and increased periodontal pocket depth.[3][5][6][16] Histologic descriptions from aggressive periodontitis literature, while not always specific to PLS, document infiltration by neutrophils, macrophages, and lymphocytes, especially plasma cells, with increased vascularity and degenerative changes in connective tissue.  

The interplay between epithelial barriers and underlying connective tissue is critical. In PLS, gingival epithelium may be more susceptible to microbial invasion due to altered local immunity and epithelial cell function, while palmoplantar epidermis may respond to mechanical and environmental stressors with exaggerated hyperproliferation and delayed desquamation, producing hyperkeratotic plaques.  

### 7.3 Cellular and Subcellular Localization

Cellular populations centrally involved in PLS include keratinocytes in palmoplantar skin, neutrophils and macrophages in peripheral blood and tissue infiltrates, NK cells and cytotoxic T lymphocytes, and osteoclasts in alveolar bone. CTSC expression has been documented in keratinocytes of palms, soles, and gingiva, as well as in neutrophils, macrophages, and their precursors.[4][6][10][15]  

Cell ontology terms relevant here include “keratinocyte” (CL:0000312), “neutrophil” (CL:0000094), “macrophage” (CL:0000235), “natural killer cell” (CL:0000623), “cytotoxic T cell” (CL:0000910), and “osteoclast” (CL:0000683). These cells occupy anatomical sites in palmoplantar skin and periodontal tissues and mediate immune responses, tissue maintenance, and bone resorption.  

Subcellularly, CTSC localizes to lysosomes and specialized granules in immune cells, with GO cellular component “lysosome” (GO:0005764) capturing this aspect. In neutrophils, CTSC resides in azurophilic granules along with pro-serine proteases; in NK cells and cytotoxic T cells, it localizes in lytic granules that also contain granzymes. In keratinocytes, CTSC’s lysosomal localization suggests roles in protein turnover and epidermal differentiation.  

The subcellular defect in PLS—loss of CTSC activity within lysosomes—impairs the maturation of proteases and possibly influences lysosomal function more broadly, although general lysosomal storage features are not observed in PLS, indicating a relatively focused functional deficit.  

---

## 8. Temporal Natural History

### 8.1 Age of Onset and Early Disease Course

PLS is a pediatric-onset disorder, with palmoplantar keratoderma and periodontitis typically emerging in early childhood. Most studies concur that palmoplantar keratoderma begins between ages one and four, often coinciding with increased ambulation and hand use.[3][5][6][8][16] Ahmad et al. stated that “Palmoplantar hyperkeratosis typically starts between 1–4 years of age,” and this timeframe is echoed in multiple case series.[6][5][16]  

Periodontitis usually emerges shortly after eruption of the primary dentition, around three to four years of age. The palmoplantar keratoderma commonly has its onset between ages one and four, “with severe periodontitis initiating at 3 or 4 years old,” as described in a recent case series.[5] Gingival inflammation, bleeding, and initial attachment loss appear rapidly, and without intervention, deep periodontal pockets and increased tooth mobility follow within a few years.[3][5][6][16]  

In early disease course, children with PLS may initially present to dermatologists with palmoplantar keratoderma or to dentists with unexplained severe periodontitis. The combination of both features within a narrow age range is a key diagnostic clue. Some cases are identified through family screening when an older sibling is diagnosed.  

### 8.2 Longitudinal Progression and Staging

Longitudinally, PLS follows a chronic, progressive course with stages corresponding to dentition and skin evolution. In the first decade of life, palmoplantar keratoderma establishes and stabilizes, and primary teeth undergo rapid periodontal destruction and premature loss. As permanent teeth erupt, similar processes recur, often beginning early in the mixed dentition stage.[3][5][6][8][16]  

Without aggressive dental management, most permanent teeth in PLS patients suffer severe attachment loss and mobility, leading to premature exfoliation by adolescence. Radiographic staging shows progressive alveolar bone loss, culminating in partial or complete edentulism. Skin manifestations persist, occasionally intensifying during adolescence, but sometimes showing partial improvement in adulthood.[3][6][8][13][16]  

Disease course may be modified by treatment. Early extraction of severely affected teeth, combined with prophylactic antibiotics and rigorous hygiene, can arrest local inflammation and prevent further bone loss, though at the cost of edentulism.[3][8][15] Systemic retinoids and other dermatologic therapies may reduce keratoderma severity and improve comfort.[8][13]  

There is no universally accepted staging system for PLS analogous to cancer staging, but clinical descriptions often refer to early, intermediate, and advanced stages based on extent of bone loss and number of teeth affected, as well as severity of keratoderma. Terms such as “Stage IV, Grade C periodontitis” have been applied to advanced dental disease in PLS.[9]  

### 8.3 Critical Windows for Intervention

Critical windows for intervention in PLS revolve around the timing of tooth eruption and early keratoderma development. For periodontal disease, the period shortly after eruption of primary teeth and again after eruption of permanent teeth represents key windows during which prophylactic measures can alter long-term outcomes.[3][5][6][8][15] Early diagnosis of PLS before severe bone loss has occurred allows for preventive strategies, including meticulous hygiene, regular professional cleanings, antimicrobial mouth rinses, and targeted antibiotic therapy, which may delay or mitigate destructive periodontitis.[3][8][15]  

Some clinicians advocate early extraction of severely affected permanent teeth in PLS to extinguish local inflammatory stimuli and protect residual bone for future prosthodontic rehabilitation. Such decisions are best made during late childhood or early adolescence, balancing functional needs and long-term prognosis.[3][8][15]  

In dermatologic management, early initiation of keratolytic agents, emollients, and systemic retinoids during initial keratoderma development may reduce plaque formation and prevent fissuring, improving quality of life.[8][13] A 4–6 week course of retinoids has been reported to produce maximal improvement, with relapse upon cessation, indicating that ongoing treatment may be necessary to maintain results.[8][13]  

These critical periods should be incorporated into clinical pathways and patient education, emphasizing that early recognition and timely intervention can substantially modify disease trajectories, particularly for periodontal outcomes.  

---

## 9. Inheritance, Epidemiology, and Population Genetics

### 9.1 Inheritance Pattern, Penetrance, and Expressivity

PLS follows a classic autosomal recessive inheritance pattern. Both parents of affected individuals are generally phenotypically normal carriers of one mutant CTSC allele, and for each pregnancy, there is a 25% chance of having an affected child, a 50% chance of a carrier child, and a 25% chance of a non-carrier child.[3][5][6][15][16] As Patel et al. noted, “PLS is inherited as an autosomal recessive disorder and if both parents are carriers of the defective gene there is a 25% risk for their children to be affected.”[3]  

Penetrance of CTSC loss-of-function alleles appears to be essentially complete; individuals with biallelic pathogenic CTSC mutations consistently manifest classic PLS features, including palmoplantar keratoderma and aggressive periodontitis, although severity and presence of additional features (e.g., infections, neurologic manifestations) may vary.[4][10][15][16] Expressivity is thus variable, reflecting differences in environmental factors, oral microbiota, and possibly modifier genes, but the core triad of palmoplantar keratoderma, periodontitis, and premature tooth loss is highly consistent among affected individuals.[3][5][6][15][16]  

There is no evidence of genetic anticipation—progressively earlier onset or increased severity across generations—nor of germline mosaicism as a significant contributor to PLS cases, consistent with its recessive, fully penetrant nature.[1][4][10][15]  

### 9.2 Prevalence, Incidence, and Demographics

PLS is an extremely rare disorder, with estimated prevalence of one to four cases per million people.[1][3][5][6][10][16] Laass (1997) and subsequent reviews have cited this figure, and more recent case series confirm the rarity of the syndrome, with approximately 200–300 cases reported worldwide.[1][5][10][16] OMIM notes that “Laass (1997) stated that the frequency of PLS is approximately 1 to 4 per million,” and Nagy et al. report that “more than 300 cases have been reported worldwide.”[1][10]  

Incidence data are less precisely defined due to the absence of large-scale registries, but given the stable prevalence and autosomal recessive inheritance, incidence is presumed to be extremely low and roughly proportional to carrier frequency and consanguinity rates. Case reports originate from diverse geographic regions, including Europe, the Middle East, South Asia, and the Americas, indicating that PLS is globally distributed rather than confined to particular ethnic groups.[3][5][6][10][15][16]  

Sex distribution appears equal; multiple reviews state that males and females are equally affected, with no sex predilection.[3][5][6][16] Racial or ethnic predilection has not been demonstrated; PLS occurs across populations, although consanguinity patterns may lead to localized clusters in regions where consanguineous marriage is common.[5][10][16] Age distribution largely reflects pediatric onset and lifelong persistence, with most diagnoses made in childhood or adolescence, though some adults are diagnosed retrospectively based on characteristic features and genetic testing.  

### 9.3 Consanguinity, Founder Mutations, and Carrier Frequency

Consanguinity plays a significant role in PLS epidemiology, increasing the likelihood of homozygosity for rare CTSC mutations. Multiple case series report parental consanguinity in approximately one-third of PLS patients, and one study demonstrates consanguinity in 20–40% of cases.[5][16] This pattern is consistent with the autosomal recessive inheritance of PLS and underscores the importance of genetic counseling in populations where consanguineous marriage is common.  

Founder mutations have been identified in certain populations. Hart et al.’s study of five consanguineous Turkish families revealed that all PLS patients were homozygous for CTSC mutations inherited from a common ancestor, indicating founder effects.[4] Nagy et al. similarly report recurrent CTSC mutations in Hungarian and other cohorts, suggesting that specific alleles have elevated frequencies in some groups due to historical founder events.[10]  

Carrier frequency for CTSC pathogenic variants is difficult to estimate precisely due to rarity and population heterogeneity. One early estimate cited a gene frequency of 0.001 for the autosomal gene causing PLS, implying that approximately one in 1,000 individuals may be carriers in general populations.[5] This figure must be interpreted cautiously, as it predates modern population genomics studies; however, the principle that CTSC pathogenic variants are rare but present at non-zero frequencies in most populations remains valid.[10][12]  

Large-scale population databases such as gnomAD provide carrier frequency estimates for specific CTSC variants, but detailed data for PLS-specific alleles are not included in the provided search results. Nevertheless, CTSC is not among the most constrained genes in terms of heterozygous loss-of-function, consistent with the clinical normality of carriers.[12] Ontology annotations for population genetics include NCIT concepts such as “Gene Frequency” (NCIT:C16693) and “Consanguinity” (NCIT:C94258).  

---

## 10. Diagnosis and Differential Diagnosis

### 10.1 Clinical Recognition and Diagnostic Criteria

Diagnosis of PLS is primarily clinical, based on recognition of the characteristic triad of diffuse palmoplantar keratoderma, aggressive early-onset periodontitis affecting both primary and permanent teeth, and premature tooth loss, in the context of autosomal recessive family history.[1][3][5][6][15][16] Patel et al. state that “PLS was first described in 1924 as a condition characterized clinically by palmoplantar hyperkeratosis and inflammatory destruction of periodontal tissues which results in premature primary and permanent teeth loss,” and this description serves as the core diagnostic criterion.[15]  

Dermatologic examination reveals erythematous, hyperkeratotic plaques on palms and soles, often extending onto dorsal surfaces and accompanied by fissuring and hyperhidrosis.[3][6][16] Dental examination shows severe gingival inflammation, bleeding, deep pockets, tooth mobility, and radiographic evidence of alveolar bone loss disproportionate to age.[3][5][6][8][16] Family history may reveal similarly affected siblings, often in consanguineous families, with unaffected parents.  

Formal diagnostic criteria or scoring systems specific to PLS are not widely published, but clinical consensus emphasizes the combination of skin and dental features and CTSC mutation confirmation. The presence of both palmoplantar keratoderma and premature loss of both primary and permanent teeth differentiates PLS from other palmoplantar keratodermas and aggressive periodontitis without skin involvement.[3][6][15][16]  

### 10.2 Laboratory, Imaging, and Functional Testing

Several investigations support PLS diagnosis and characterize disease extent. Patel et al. list potential diagnostic investigations, including hematological tests, hormone assays, height and weight calculation, urine analysis, alkaline phosphatase measurement, radiological investigations (orthopantomograph, intraoral periapical radiographs, lateral cephalogram), neutrophil function tests, and conventional polymerase chain reaction for microbiological analysis.[3]  

Hematologic tests may reveal mild leukocytosis during infections but are generally unremarkable. Hormone assays and metabolic panels help exclude other systemic conditions. Radiographs show generalized alveolar bone loss and “floating teeth” appearance, confirming aggressive periodontitis and guiding dental management.[3][5][6][16] Lateral cephalograms can assess craniofacial development and plan prosthodontic rehabilitation.  

Neutrophil function tests, including assays of chemotaxis, phagocytosis, and oxidative burst, have demonstrated functional impairment in PLS patients in several studies.[3] These tests can provide mechanistic insight but are not routinely required for diagnosis. Microbiological analysis by PCR or culture identifies periodontal pathogens, such as *A. actinomycetemcomitans* and *Capnocytophaga* spp., and informs antibiotic selection.[3][8]  

Skin biopsy, while not essential, may show characteristic hyperkeratosis and parakeratosis consistent with hereditary palmoplantar keratoderma. Histopathologic findings are often nonspecific, overlapping with other keratodermas.  

### 10.3 Genetic Testing Strategies

Genetic testing has become integral to definitive diagnosis of PLS, particularly for differential diagnosis and family counseling. The recommended approach is targeted sequencing of the CTSC gene, including all coding exons and flanking intronic regions, using Sanger or next-generation sequencing.[10][15] Nagy et al. note that mutation screening for CTSC in Hungary has been available since 2011, with direct sequencing of all coding regions and flanking introns performed for suspected PLS, HMS, or AP1 cases.[10]  

Once a putative causative variant is identified in a patient, available clinically symptom-free family members and unrelated healthy controls may be tested to confirm segregation and carrier status, thereby solidifying diagnosis and guiding counseling.[10] Identification of a CTSC mutation gives a definite diagnosis of PLS, HMS, or AP1 depending on the presented clinical symptoms, whereas absence of CTSC mutation suggests alternative diagnoses, such as other palmoplantar keratodermas or nonsyndromic tooth anomalies.[10][15]  

Whole exome or genome sequencing can also detect CTSC mutations, particularly in undiagnosed ectodermal dysplasia cohorts, but targeted CTSC sequencing remains efficient and cost-effective for classical PLS. Chromosomal microarray and karyotyping are generally unremarkable and are not frontline tests for PLS. FISH and mitochondrial DNA testing are not relevant to CTSC-related disease.  

ClinVar and other variant databases support interpretation of CTSC variants and classification under ACMG/AMP guidelines.[11] Genetic testing registry (GTR) entries likely include CTSC panels, although specific details are beyond the provided search results. Ontology descriptors include NCIT terms such as “Genetic Testing” (NCIT:C17890) and “DNA Sequencing” (NCIT:C20160).  

### 10.4 Differential Diagnosis and Overlapping Syndromes

Differential diagnosis of PLS includes several palmoplantar keratodermas and syndromic conditions, as well as aggressive periodontitis without skin involvement. Key entities include Haim-Munk syndrome (HMS), another CTSC-related disorder characterized by palmoplantar keratoderma, periodontitis, and additional skeletal anomalies; aggressive periodontitis type 1 (AP1), an allelic condition presenting with severe periodontitis but minimal or absent keratoderma; and nonsyndromic hereditary palmoplantar keratodermas such as Unna-Thost disease.[1][10][15]  

Clinically, HMS differs from PLS by the presence of arachnodactyly, acroosteolysis, and onychogryphosis, while AP1 lacks palmoplantar keratoderma. CTSC mutation analysis helps distinguish these conditions and confirm allelic relationships.[1][10][15] Other ectodermal dysplasias, such as those involving hair, nails, and teeth, may present with overlapping features; however, the specific combination of diffuse palmoplantar keratoderma and aggressive early-onset periodontitis is strongly suggestive of PLS.[3][6][15][16]  

Aggressive periodontitis in otherwise healthy individuals must be differentiated from PLS and AP1, with attention to age of onset, distribution of bone loss, family history, and presence of palmoplantar keratoderma. Idiopathic or multifactorial keratodermas without dental involvement can be distinguished by normal dentition and absence of severe periodontitis.  

### 10.5 Screening and Early Detection

There are no population-wide screening programs for PLS due to its rarity. However, targeted screening may be considered in families with known CTSC mutations, particularly in consanguineous communities. Carrier testing and prenatal or preimplantation genetic diagnosis can be offered to at-risk couples once familial CTSC variants are identified.[10][15]  

Clinical screening for early detection involves heightened awareness among pediatricians, dermatologists, and dentists. Children presenting with palmoplantar keratoderma or unusually severe periodontitis should be evaluated for PLS, including detailed family history and consideration of CTSC testing.[3][5][6][15][16] Identifying PLS at an early stage allows prompt intervention to protect periodontal and skeletal structures and to manage keratoderma.  

Newborn screening is not applicable to PLS, and no standardized carrier screening programs exist outside of specific high-risk populations. Nonetheless, inclusion of PLS and CTSC in rare disease awareness initiatives may support earlier recognition in clinical practice.  

---

## 11. Outcome, Prognosis, and Disease Burden

### 11.1 Survival, Mortality, and Major Complications

PLS is not typically associated with reduced life expectancy. With appropriate infection management and supportive care, most individuals have normal survival.[3][6][16] Severe infections, such as sepsis or pneumonia, can be life-threatening, but these are relatively rare and usually occur in contexts of delayed diagnosis or limited access to healthcare. There is limited published data on mortality rates specific to PLS, reflecting the rarity of the condition and the absence of large cohorts.[3][6][16]  

Major complications include complete edentulism, chronic pain and functional limitations due to keratoderma, and recurrent infections requiring hospitalizations or advanced antibiotic therapy. In some cases, neurologic complications such as intracranial calcifications and intellectual disability contribute to morbidity.[3][6][16]  

Because PLS does not primarily affect vital organs such as heart, lungs, or kidneys, disease burden is more about chronic disability and quality-of-life impairment than mortality.  

### 11.2 Functional Outcomes and Disability

Functional outcomes in PLS are heavily influenced by dental and dermatologic consequences. Early loss of teeth impairs mastication and can lead to nutritional deficiencies, speech difficulties, and aesthetic concerns. Prosthodontic rehabilitation with dentures or implants can restore function but requires ongoing care and may be complicated by bone loss.[3][5][8][16]  

Palmoplantar keratoderma limits mobility and manual dexterity, especially when plaques are thick and fissured. Painful lesions interfere with walking and weight-bearing, and hyperhidrosis may cause discomfort and embarrassment. These factors can restrict participation in daily activities, including education, employment, and recreation.[3][6][16]  

Overall disability is individualized; some patients adapt well with appropriate interventions, while others experience major limitations. ICF domains of mobility, self-care, communication, and social participation are relevant to disability assessment in PLS.  

### 11.3 Quality of Life and Psychosocial Consequences

Quality of life in PLS is impacted by physical, psychological, and social factors. Physical discomfort from keratoderma and infections, combined with functional limitations from edentulism, contributes to bodily pain and reduced physical functioning. Psychological consequences include anxiety, depression, and low self-esteem, particularly in adolescents coping with appearance differences and social stigma.[3][5][6][16]  

Although formal quality-of-life studies using EQ-5D, SF-36, or PROMIS instruments are not reported specifically for PLS, observations from related conditions support the expectation of reduced scores in domains such as physical functioning, social functioning, and mental health. Long-term psychosocial support and counseling may be necessary for some individuals and families.  

### 11.4 Prognostic Factors and Biomarkers

Prognostic factors in PLS include age at diagnosis, timing and quality of dental interventions, adherence to dermatologic therapies, and overall infection control. Early diagnosis and aggressive periodontal management can preserve bone and delay tooth loss, while prompt treatment of infections reduces risk of serious complications.[3][8][15][16]  

No specific molecular prognostic biomarkers have been identified for PLS, beyond CTSC genotype itself. The presence of certain periodontal pathogens, such as high levels of *A. actinomycetemcomitans*, may predict more aggressive periodontal destruction, but such associations remain largely extrapolated from general periodontitis literature.[3][8][9] Functional assays of neutrophil and NK cell activity could theoretically serve as mechanistic biomarkers but are not routinely used.  

---

## 12. Treatment and Management

### 12.1 Dermatologic Management

Dermatologic management of PLS focuses on alleviating palmoplantar keratoderma through topical and systemic therapies. Topical treatments include emollients to soften plaques, keratolytic agents such as salicylic acid to reduce thickness, and corticosteroids to manage inflammation.[7][8][13] These agents are applied regularly and tailored to plaque severity and patient tolerance.  

Systemic retinoids have been the most extensively reported systemic therapy for PLS keratoderma. Case reports document the use of etretinate, acitretin, and isotretinoin at dosages of 0.5–1.0 mg/kg/day, with “excellent efficacy” and “maximum improvement occurring by 4–6 weeks,” although relapse typically occurs after discontinuation.[8][13] Nguyen et al. described two young women with PLS treated with isotretinoin at 0.5–1.0 mg/kg/day, noting highly effective reduction of keratoderma.[13] Other authors report successful treatment with acitretin, and one report describes complete remission of pyogenic infections in four individuals treated with etretinate over 21 months.[13]  

Dimethyl fumarate has recently emerged as a potential systemic therapy for PLS keratoderma, based on a case report in JAAD Case Reports. The authors noted that “current management options for keratoderma include topicals such as steroids, salicylic acid, and emollients. Meanwhile, systemic options…” include retinoids, and they described successful use of dimethyl fumarate with improvement in keratoderma.[7] Dimethyl fumarate, an immunomodulatory agent, may modulate inflammatory pathways in skin, though its mechanism in PLS remains speculative.  

Side effects of systemic retinoids include mucocutaneous dryness, hyperlipidemia, liver enzyme elevation, and teratogenicity, necessitating careful monitoring and adherence to pregnancy prevention protocols. Dimethyl fumarate can cause flushing, gastrointestinal symptoms, and lymphopenia. Clinicians must weigh benefits against risks and consider long-term management strategies.  

NCIT ontology terms relevant to dermatologic treatment include “Retinoid Therapy” (NCIT:C62047), “Topical Corticosteroid Therapy” (NCIT:C62791), “Keratolytic Agent” (NCIT:C29428), and “Dimethyl Fumarate” (NCIT:C102887).  

### 12.2 Dental and Periodontal Management

Dental and periodontal management is central to PLS care. Primary goals include controlling infection, preserving alveolar bone as much as possible, maintaining function and aesthetics, and preparing for prosthodontic rehabilitation.[3][8][15][16]  

Good dental care and oral hygiene are essential. Daily brushing with fluoride toothpaste, interdental cleaning, and regular professional cleanings help reduce plaque accumulation. Prophylactic antibiotics—often targeting Gram-negative anaerobes, such as amoxicillin combined with metronidazole—may be used to minimize progression of periodontitis and tooth loss.[8][15] The ScienceDirect overview emphasizes that “Good dental care and oral hygiene, and prophylactic antibiotics, may minimize the progression of periodontitis and teeth loss,” underscoring the role of preventive strategies.[8]  

Permanent teeth with advanced periodontal disease should be extracted to eliminate persistent infection foci and halt ongoing bone loss.[8][15] Early extraction may preserve alveolar bone for future implant placement. Modern dental implants offer therapeutic and aesthetic alternatives, enabling restoration of function and appearance, although implant success may be influenced by bone quality and infection control.[8]  

Orthodontic and prosthodontic planning is crucial. Removable dentures may be used in younger patients, while implants are considered in adolescents and adults once bone growth stabilizes. Treatment plans should be individualized, considering patient preferences, resources, and local expertise.  

NCIT terms relevant to dental management include “Periodontal Therapy” (NCIT:C15295), “Antibiotic Therapy” (NCIT:C6708), “Tooth Extraction” (NCIT:C51942), and “Dental Implant Placement” (NCIT:C51945).  

### 12.3 Management of Infections and Immune Dysfunction

Management of infections in PLS involves prompt recognition, appropriate antibiotic therapy, and, in some cases, prophylactic strategies. Recurrent skin infections and systemic infections should be treated according to standard clinical guidelines, adjusted for local resistance patterns.[3][6][16] Prophylactic antibiotics may be considered in individuals with frequent infections, especially those with severe periodontal disease or extensive keratoderma.[3][8][15]  

Immunologic management is not standardized, as PLS is not associated with global immunodeficiency. However, vaccination against common pathogens (e.g., pneumococcus, influenza) should follow general recommendations, and clinicians should remain alert to atypically severe infections. Functional assays of neutrophil and NK cell activity may guide individualized management, though such testing is specialized and not widely available.[3][6][15]  

Adjunctive therapies such as immunomodulators or granulocyte colony-stimulating factor (G-CSF) have not been systematically studied in PLS; their use remains speculative. Dimethyl fumarate may have immunomodulatory effects, but its precise role in infection management is unclear.[7]  

### 12.4 Experimental and Emerging Therapies

Experimental therapies for PLS are at an early stage. Gene therapy targeting CTSC is theoretically feasible but has not yet been attempted in clinical trials. Challenges include delivering CTSC to relevant tissues (immune cells and keratinocytes), ensuring regulated expression, and overcoming immune barriers.  

Cell-based therapies, such as hematopoietic stem cell transplantation, have not been reported in PLS and may carry significant risks relative to benefits. RNA-based therapies (e.g., mRNA delivery of CTSC) are conceptually possible but remain in preclinical realms.  

Targeted therapies focusing on downstream pathways of CTSC deficiency, such as modulators of neutrophil or NK cell function, may offer future avenues. For example, agents that enhance non-protease-dependent bacterial killing or regulate inflammatory responses could theoretically ameliorate periodontal damage, but specific candidates have not been identified for PLS.  

Dimethyl fumarate represents an emerging immunomodulatory therapy, with initial case report evidence of benefit for keratoderma.[7] Further research is needed to validate efficacy and safety in larger cohorts.  

### 12.5 Personalized and Multidisciplinary Care Pathways

Given its multisystem involvement, PLS requires multidisciplinary care involving dermatologists, dentists/periodontists, geneticists, immunologists, and psychosocial support providers.[3][5][8][15][16] Personalized care pathways should integrate genetic findings (specific CTSC variant), environmental factors (oral microbiome, lifestyle), and individual preferences.  

Key elements include early diagnosis, genetic counseling, individualized dermatologic and dental treatment plans, infection surveillance, and psychosocial support. Coordinated care improves outcomes, as early dental interventions and ongoing dermatologic management can substantially mitigate functional impairment and enhance quality of life.  

NCIT terms capturing multidisciplinary care include “Multidisciplinary Treatment Approach” (NCIT:C15986) and “Supportive Care” (NCIT:C15481).  

---

## 13. Prevention and Genetic Counseling

### 13.1 Primary and Secondary Prevention

Primary prevention of PLS, in the sense of preventing disease occurrence, is only possible through reproductive decision-making, given its genetic etiology. Carrier screening and genetic counseling for at-risk couples can inform choices such as avoidance of consanguineous unions or use of assisted reproductive technologies with preimplantation genetic diagnosis (PGD).[10][15]  

Secondary prevention involves early detection and intervention to reduce disease severity and complications. Recognizing PLS early in childhood allows timely initiation of dental and dermatologic management to preserve function and reduce morbidity.[3][5][6][15][16] Screening siblings of affected individuals and performing CTSC testing can identify asymptomatic carriers and early-stage patients.  

### 13.2 Tertiary Prevention and Long-term Disease Management

Tertiary prevention focuses on preventing complications and optimizing quality of life in individuals with established PLS. Key strategies include preventing further bone loss through dental interventions, managing keratoderma to reduce pain and functional limitations, and preventing recurrent infections through timely treatment and, where appropriate, prophylaxis.[3][6][8][15][16]  

Regular follow-up with dermatology and dentistry, combined with individualized rehabilitative interventions (physical therapy for gait issues, speech therapy for articulation), may be necessary. Psychological counseling and social support can mitigate psychosocial consequences.  

### 13.3 Genetic Counseling and Reproductive Options

Genetic counseling is essential for families affected by PLS. Counselors should explain autosomal recessive inheritance, carrier risks, and reproductive options. Each child of two carrier parents has a 25% risk of being affected, a 50% risk of being a carrier, and a 25% risk of being unaffected and non-carrier.[3][5][6][15][16]  

Couples may choose options such as prenatal diagnosis via chorionic villus sampling or amniocentesis, PGD with in vitro fertilization, or use of donor gametes. Counseling should be non-directive and respect cultural and personal values.  

NSGC and ACMG guidelines for counseling in autosomal recessive conditions provide frameworks, although PLS is not specifically highlighted. CTSC variant identification enables precise risk assessment for family members and informs cascade testing.  

---

## 14. Comparative Aspects and Natural Disease in Other Species

### 14.1 CTSC Orthologs and Comparative Immunology

CTSC orthologs exist in multiple species, including mice, rats, and other mammals, where cathepsin C performs similar roles in activating serine proteases in immune cells. Mouse models with Ctse or Ctsc knockout have been studied to elucidate CTSC function, showing defects in neutrophil serine protease activation and altered immune responses.[3][4][10][15]  

Comparative biology analyses in CTSC-deficient animals demonstrate increased susceptibility to certain infections and altered inflammatory responses, paralleling aspects of PLS. However, overt palmoplantar keratoderma and human-like aggressive periodontitis are not typically observed, reflecting species differences in skin and dental anatomy.  

Evolutionary conservation of CTSC emphasizes its fundamental role in immunity across vertebrates. HomoloGene and other orthology databases (not directly cited) support CTSC as a conserved gene with similar protein domain architecture across species.  

### 14.2 Natural PLS-like Conditions in Animals

No naturally occurring animal condition fully analogous to PLS has been documented. While periodontal disease and palmoplantar keratoderma-like lesions occur in dogs, cats, and other animals, these are generally multifactorial and not linked to CTSC mutations. OMIA (Online Mendelian Inheritance in Animals) does not list a direct PLS equivalent, indicating that CTSC-related genodermatosis with combined keratoderma and aggressive periodontitis is unique to humans.  

Veterinary relevance of CTSC-deficient models lies primarily in immunology and protease biology research rather than direct clinical analogs.  

---

## 15. Model Organisms and Experimental Systems

### 15.1 CTSC-deficient Mouse Models

Mouse models with Ctsc knockout provide valuable systems for studying CTSC biology and aspects of PLS pathogenesis. Ctsc−/− mice exhibit defective activation of neutrophil serine proteases and granzymes, leading to altered immune responses and susceptibility to infections.[3][4][10][15] These models have been used to investigate neutrophil-mediated immunity, NK cell cytotoxicity, and inflammatory regulation.  

Phenotypic recapitulation of human PLS in mice is partial. While immune defects are present, overt palmoplantar keratoderma and aggressive periodontitis are not consistently observed, likely due to species differences in skin thickness, mechanical loading, and oral microbiome composition. Nevertheless, Ctsc-deficient mice offer platforms to study host–microbe interactions, inflammatory signaling, and potential interventions targeting immune protease pathways.  

Model limitations include differences in dental anatomy, lack of human-like periodontal structures, and species-specific immune regulation. Translating findings from mice to human PLS thus requires careful contextualization.  

### 15.2 Other Experimental Systems

Other experimental systems relevant to PLS include in vitro cell culture models of CTSC-deficient keratinocytes or immune cells, where gene knockdown or CRISPR-mediated knockout can mimic CTSC loss-of-function. These models enable mechanistic studies of protease activation, cell signaling, and responses to microbial stimuli.  

Organotypic skin models and oral mucosa models may be adapted to study CTSC-related defects, but specific PLS-focused applications are not yet reported. Multi-omics profiling of CTSC-deficient cells and tissues in such models could illuminate downstream pathways and potential therapeutic targets.  

---

## Conclusion

Papillon–Lefèvre syndrome exemplifies a rare, yet mechanistically illuminating, monogenic disorder in which biallelic loss-of-function mutations in CTSC disrupt immune protease activation and epithelial homeostasis, yielding a distinctive combination of diffuse palmoplantar keratoderma, aggressive early-onset periodontitis, and premature loss of both primary and permanent dentition.[1][3][4][6][10][15][16] Its autosomal recessive inheritance, with complete penetrance but variable expressivity, underscores the importance of CTSC for immune and epithelial function, while the syndrome’s tissue selectivity—predominantly affecting palmoplantar skin and periodontal structures—raises intriguing questions about local microenvironmental factors and gene–environment interactions.  

Mechanistically, CTSC deficiency impairs activation of neutrophil serine proteases and granzymes, compromising bacterial killing and cytotoxic function and leading to deregulated inflammatory responses, especially in periodontal tissues.[3][6][10][15] In the skin, CTSC likely contributes to keratinocyte differentiation and desquamation, and its absence, coupled with mechanical stress and local immune alterations, manifests as palmoplantar hyperkeratosis with transgradient extension.[4][6][10][15] The oral microbiome, particularly Gram-negative anaerobes such as *A. actinomycetemcomitans* and *Capnocytophaga* spp., interacts with CTSC-deficient host defenses to drive severe periodontitis, while differences in salivary microbiota among PLS siblings suggest that microbial community composition modulates disease severity.[3][8][9]  

Clinically, PLS imposes substantial morbidity, with chronic pain and functional limitations from keratoderma and profound impacts on oral function, nutrition, speech, and psychosocial well-being due to early edentulism.[3][5][6][16] Lifelong susceptibility to infections in a subset of patients adds to the burden, though overall survival is generally normal when infections are properly managed.[3][6][16]  

Diagnosis relies on recognition of the characteristic triad and confirmation of CTSC mutations via genetic testing, supported by radiographic and functional studies.[1][3][5][6][10][15][16] Management is multidisciplinary and personalized, integrating topical and systemic dermatologic therapies (notably retinoids and, more recently, dimethyl fumarate), intensive periodontal and dental care—including prophylactic antibiotics, early extraction of severely affected teeth, and prosthodontic rehabilitation—and vigilant infection control.[3][7][8][13][15] Genetic counseling is essential for affected families, providing guidance on autosomal recessive risk, carrier testing, and reproductive options.[3][5][6][10][15][16]  

Despite advances in genetic and immunologic understanding, important gaps remain. The exact causal chain linking CTSC deficiency to tissue-specific manifestations, the role of modifier genes and epigenetic factors, and the long-term systemic consequences of chronic inflammation in PLS require further investigation.[3][10][15] Emerging technologies, including multi-omics profiling, high-throughput microbiome analyses, and CTSC-deficient model systems, hold promise for unraveling these complexities. At the same time, pragmatic efforts to improve early diagnosis, expand access to multidisciplinary care, and document quality-of-life outcomes in PLS cohorts can yield immediate benefits for affected individuals.  

In translational terms, PLS offers a unique window into the biology of immune protease cascades, host–microbe interactions in periodontal disease, and mechanisms of hereditary keratoderma. Continued integration of clinical observation, molecular genetics, immunology, and microbiology, grounded in robust ontological annotation and curated evidence, will enhance disease knowledge bases and support more precise, compassionate, and effective care for individuals living with this rare but instructive syndrome.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 7 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:19882040` (1 mention) - Depigmentation along lymphatic channels following intralesional corticosteroid injection.
  - shared terms: none

Weighed against this report's own most characteristic terms: `pls`, `ctsc`, `keratoderma`, `palmoplantar`, `disease`, `periodontal`, `periodontitis`, `infection`, `include`, `skin`, `cell`, `function`, `immune`, `neutrophil`, `tissue`, `clinical`, `patient`, `loss`, `genetic`, `aggressive`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 71 |
| Resolved | 65 |
| Unresolved (possible confabulation) | 3 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 60 |
| Terms named correctly | 28 |
| Terms named as a **different** term | 27 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0000094` (4 mentions) - the report calls it "neutrophil"; CL calls it **granulocyte**
- `HP:0003610` (1 mention) - the report calls it "Erythematous plaques"; HP calls it **Fibroblast metachromasia**
- `HP:0000977` (1 mention) - the report calls it "Hyperhidrosis"; HP calls it **Soft skin**
- `HP:0003795` (1 mention) - the report calls it "Alveolar bone loss"; HP calls it **Short middle phalanx of toe**
- `HP:0006802` (1 mention) - the report calls it "Intracranial calcification"; HP calls it **Abnormal anterior horn cell morphology**
- `NCIT:C12219` (1 mention) - the report calls it "Health Behavior"; NCIT calls it **Anatomic Structure, System, or Substance**
- `NCIT:C17010` (1 mention) - the report calls it "Socioeconomic Factors"; NCIT calls it **Prevalence**
- `GO:0016500` (1 mention) - the report calls it "activation of proenzyme"; GO calls it **protein-hormone receptor activity**
- `UBERON:0001838` (2 mentions) - the report calls it "gingiva"; UBERON calls it **sublingual duct**
- `UBERON:0002503` (2 mentions) - the report calls it "periodontal ligament"; UBERON calls it **greater trochanter**
- `UBERON:0004707` (1 mention) - the report calls it "alveolar process of maxilla"; UBERON calls it **pharyngula stage**
- `UBERON:0004705` (1 mention) - the report calls it "alveolar process of mandible"; UBERON calls it **fenestra**
- `CL:0000683` (1 mention) - the report calls it "osteoclast"; CL calls it **ependymoglial cell**
- `NCIT:C16693` (1 mention) - the report calls it "Gene Frequency"; NCIT calls it **Non-Histone Chromosomal Protein HMG-17**
- `NCIT:C94258` (1 mention) - the report calls it "Consanguinity"; NCIT calls it **Expanded Access Study Protocol Intervention Or Procedure**
- `NCIT:C17890` (1 mention) - the report calls it "Genetic Testing"; NCIT calls it **DNA Footprinting**
- `NCIT:C20160` (1 mention) - the report calls it "DNA Sequencing"; NCIT calls it **NCI Center for Cancer Research**
- `NCIT:C62047` (1 mention) - the report calls it "Retinoid Therapy"; NCIT calls it **Mexiletine**
- `NCIT:C62791` (1 mention) - the report calls it "Topical Corticosteroid Therapy"; NCIT calls it **Pegdinetanib**
- `NCIT:C29428` (1 mention) - the report calls it "Keratolytic Agent"; NCIT calls it **Shared Anti-Idiotype-AB-S016**
- `NCIT:C102887` (1 mention) - the report calls it "Dimethyl Fumarate"; NCIT calls it **LIM Domain-Binding Protein 1**
- `NCIT:C15295` (1 mention) - the report calls it "Periodontal Therapy"; NCIT calls it **Chemotherapeutic Perfusion**
- `NCIT:C6708` (1 mention) - the report calls it "Antibiotic Therapy"; NCIT calls it **Stage IVB Bone Sarcoma AJCC v7**
- `NCIT:C51942` (1 mention) - the report calls it "Tooth Extraction"; NCIT calls it **Papanicolaou Test**
- `NCIT:C51945` (1 mention) - the report calls it "Dental Implant Placement"; NCIT calls it **Ambulatory Surgical Facility**
- `NCIT:C15986` (1 mention) - the report calls it "Multidisciplinary Treatment Approach"; NCIT calls it **Pharmacotherapy**
- `NCIT:C15481` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Antiandrogen Therapy**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0004600` (1 mention), reported as "Periodontitis" - HP does not contain this term
- `HP:0002976` (1 mention), reported as "Gingivitis" - HP does not contain this term
- `UBERON:0004278` (2 mentions), reported as "skin of palm" - UBERON does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C51942` (Papanicolaou Test) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003593` (1 mention) - the report calls it "Childhood onset"; HP calls it **Infantile onset**
- `GO:0002228` (2 mentions) - the report calls it "NK cell mediated cytotoxicity"; GO calls it **natural killer cell mediated immunity**, and lists "NK cell mediated immunity" among its other names
- `GO:0008238` (2 mentions) - the report calls it "dipeptidyl-peptidase activity"; GO calls it **exopeptidase activity**
- `HP:0000217` (1 mention) - the report calls it "Hyposalivation"; HP calls it **Xerostomia**, and lists "Reduced salivation" among its other names
- `UBERON:0004262` (2 mentions) - the report calls it "skin of sole of foot"; UBERON calls it **upper leg skin**, and lists "skin of thigh" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0002446` - called "neutrophil-mediated immunity", "neutrophil mediated immunity"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.