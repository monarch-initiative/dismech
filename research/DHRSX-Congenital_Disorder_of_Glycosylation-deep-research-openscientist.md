---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T22:35:18.077128'
end_time: '2026-09-01T23:31:00.083751'
duration_seconds: 3342.01
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: DHRSX-Congenital Disorder of Glycosylation
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
citation_count: 14
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 7
  relevance_assessed: 16
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 32
  verified: 28
  not_found: 1
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.032
  labels_checked: 20
  labels_matching: 1
  labels_mismatched: 16
  mislabelled_terms:
  - term_id: MONDO:0015286
    reported_labels:
    - congenital disorder of glycosylation
    - grouping
    ontology_label: congenital disorder of glycosylation
  - term_id: HP:0001999
    reported_labels:
    - Physical manifestation
    ontology_label: Abnormal facial shape
  - term_id: HP:0001252
    reported_labels:
    - Clinical sign
    ontology_label: Hypotonia
  - term_id: HP:0001250
    reported_labels:
    - Clinical sign
    ontology_label: Seizure
  - term_id: HP:0000407
    reported_labels:
    - Laboratory/clinical
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0002650
    reported_labels:
    - Physical manifestation
    ontology_label: Scoliosis
  - term_id: HP:0002803
    reported_labels:
    - Physical manifestation
    ontology_label: Congenital contracture
  - term_id: HP:0001508
    reported_labels:
    - Clinical sign
    ontology_label: Failure to thrive
  - term_id: HP:0002093
    reported_labels:
    - Clinical sign
    ontology_label: Respiratory insufficiency
  - term_id: HP:0000478
    reported_labels:
    - Physical manifestation
    ontology_label: Abnormality of the eye
  - term_id: HP:0001272
    reported_labels:
    - Imaging/lab abnormality
    ontology_label: Cerebellar atrophy
  - term_id: UBERON:0002391
    reported_labels:
    - vertebral column
    ontology_label: lymph
  - term_id: UBERON:0001004
    reported_labels:
    - Lungs / airway (variable insufficiency)
    ontology_label: respiratory system
  - term_id: UBERON:0005409
    reported_labels:
    - GI tract (feeding difficulty, FTT)
    ontology_label: alimentary part of gastrointestinal system
  - term_id: NCIT:C15515
    reported_labels:
    - Physical Therapy
    ontology_label: Colony-Stimulating Factor Therapy
  - term_id: NCIT:C99290
    reported_labels:
    - Hearing Aid
    ontology_label: TCF3/HLF Fusion Protein
  labels_variant: 3
  unresolved_terms:
  - NCIT:C173379
  obsolete_terms:
  - term_id: GO:0019408
    ontology_label: obsolete dolichol biosynthetic process
    replaced_by: GO:0043048
  - term_id: GO:0019348
    ontology_label: obsolete dolichol metabolic process
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: DHRSX-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: DHRSX-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DHRSX-Congenital Disorder of Glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **DHRSX-Congenital Disorder of Glycosylation** covering all of the
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

# DHRSX-Congenital Disorder of Glycosylation (DHRSX-CDG / CDG type 1DD): Comprehensive Disease Report

**Disease:** DHRSX-Congenital Disorder of Glycosylation
**OMIM phenotype:** #301133 (Congenital disorder of glycosylation, type Idd; CDG1DD)
**Gene:** *DHRSX* (OMIM *301034)
**Category:** Mendelian (pseudoautosomal-recessive)
**MONDO:** No disorder-specific term yet; currently subsumed under MONDO:0015286 (congenital disorder of glycosylation)

---

## Summary

**DHRSX-CDG is an ultra-rare, severe multisystem congenital disorder of glycosylation (type I) first described in 2024, and it is notable as the first human disease shown to be inherited in a pseudoautosomal-recessive manner.** The causal gene, *DHRSX*, resides in pseudoautosomal region 1 (PAR1) at the tips of both the X (Xp22.33) and Y (Yp11.32) chromosomes, so both sexes carry two functional copies that recombine like an autosomal locus. Disease requires biallelic loss-of-function (missense) variants, and because PAR genes escape X-inactivation, males and females are affected equally ([PMID: 38821050](https://pubmed.ncbi.nlm.nih.gov/38821050/)).

Mechanistically, the discovery of DHRSX-CDG forced a revision of the textbook dolichol-biosynthesis pathway. The final conversion of polyprenol to dolichol — the lipid carrier essential for N-glycosylation — is not a single reduction performed by SRD5A3 (polyprenol reductase), as long believed, but a **three-step "detour"** involving additional metabolic intermediates. DHRSX catalyzes the first and third steps (an NAD⁺-dependent oxidation of polyprenol to polyprenal, and an NADPH-dependent reduction of dolichal to dolichol), while SRD5A3 is reassigned to catalyze only the intervening second step (reduction of polyprenal to dolichal). Loss of DHRSX function therefore blocks dolichol production, depletes the dolichol-phosphate carrier needed to assemble the lipid-linked oligosaccharide (LLO), and produces protein N-hypoglycosylation with a CDG type I biochemical signature ([PMID: 38821050](https://pubmed.ncbi.nlm.nih.gov/38821050/); [PMID: 39395802](https://pubmed.ncbi.nlm.nih.gov/39395802/)).

Clinically, the four reported patients (from three unrelated families) present with a severe congenital neurodevelopmental disorder: facial dysmorphism, hypotonia, profound intellectual disability, epilepsy, sensorineural hearing loss, scoliosis, joint contractures, and severe failure to thrive requiring tube feeding. Diagnosis rests on molecular sequencing with attention to the PAR1 locus, supported by a transferrin CDG-I pattern that can normalize with age (and may be normal in some affected individuals) and by polyisoprenoid profiling (elevated polyprenol without polyprenal accumulation, distinguishing DHRSX-CDG from SRD5A3-CDG). No disease-specific therapy exists; management is entirely supportive and multidisciplinary.

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** DHRSX-CDG is a congenital disorder of glycosylation of the N-linked type I (assembly/ER) class, caused by biallelic missense variants in *DHRSX*. It manifests as a severe, congenital-onset multisystem neurodevelopmental disorder. It was first delineated by Wilson et al. in 2024, who reported it under the description "a pseudoautosomal-recessive disease presenting as a congenital disorder of glycosylation in patients with missense variants in DHRSX (DHRSX-CDG)" ([PMID: 38821050](https://pubmed.ncbi.nlm.nih.gov/38821050/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM phenotype | #301133 (CDG type Idd; CDG1DD) |
| OMIM gene (DHRSX) | *301034 |
| OMIM gene (DHRSY paralog) | *400049 |
| HGNC | 18399 |
| NCBI Gene | 207063 |
| Ensembl | ENSG00000169084 |
| UniProtKB | Q8N5I4 (DHRSX_HUMAN) |
| MONDO | No disorder-specific term yet; maps to MONDO:0015286 (grouping) |
| Orphanet | Not yet assigned (2024 first description) |
| ICD-11 | Not yet assigned |

**Synonyms / alternative names:** DHRSX-CDG; CDG-Idd; CDG1DD; congenital disorder of glycosylation type Idd; dolichol synthesis defect (DHRSX). Gene aliases: DHRSY, DHRS5X/DHRS5Y, DHRSXY, SDR46C1, SDR7C6.

**Source of information.** All clinical knowledge derives from a single aggregated individual-patient report (Wilson et al. 2024) of 4 patients from 3 families, complemented by cell-model and biochemical studies. This is disease-level, primary-literature-derived information rather than EHR/registry aggregation. Importantly, no expanded cohort exists — reported fractions such as 9/10 or 6/7 in the CDG literature belong to a separate PMM2-CDG cohort and must not be attributed to DHRSX-CDG.

---

### 2. Etiology

**Causal factor:** Purely genetic. Biallelic (homozygous or compound-heterozygous) missense variants in *DHRSX* cause loss of enzyme function and blockade of dolichol synthesis. There is no known environmental, infectious, or acquired cause.

**Genetic risk factors.** The only established risk factor is inheritance of two pathogenic *DHRSX* alleles. Reported pathogenic variants:

| Patient | Sex | Genotype |
|---|---|---|
| Patient 1 | F | Homozygous c.541G>T, p.(Val181Phe) |
| Patient 2 | F | Homozygous c.146C>T, p.(Thr49Met) |
| Patients 3 & 4 (brothers) | M | Compound-het: c.541G>T p.(Val181Phe) (maternal, X) + c.643C>T p.(Leu215Phe) (paternal, Y) |

The brothers' genotype is the direct demonstration of pseudoautosomal-recessive inheritance: one pathogenic allele was transmitted on the maternal X and the other on the paternal Y ([PMID: 38821050](https://pubmed.ncbi.nlm.nih.gov/38821050/)).

**Environmental / lifestyle / infectious risk factors:** None identified or applicable. Consanguinity/homozygosity contributed in the two singleton families (homozygous variants).

**Protective factors:** None described. (Notably, in the analogous SRD5A3 pathway, an alternative/residual dolichol route can allow partial glycosylation — see Mechanism — but no protective allele or exposure is defined for DHRSX-CDG.)

**Gene–environment interactions:** None described.

---

### 3. Phenotypes

The clinical phenotype (n=4) is a severe congenital multisystem neurodevelopmental disorder. Because the cohort is tiny, frequencies are qualitative.

| Phenotype | Type | HPO suggestion | Onset / severity |
|---|---|---|---|
| Facial dysmorphism | Physical manifestation | HP:0001999 | Congenital |
| Muscular hypotonia | Clinical sign | HP:0001252 | Congenital, severe |
| Profound intellectual disability / developmental delay | Neurodevelopmental | HP:0002187 / HP:0001263 | Congenital, severe |
| Epilepsy / seizures | Clinical sign | HP:0001250 | Early-onset |
| Sensorineural hearing loss | Laboratory/clinical | HP:0000407 | Congenital/early |
| Scoliosis | Physical manifestation | HP:0002650 | Childhood |
| Joint contractures | Physical manifestation | HP:0002803 | Childhood, progressive |
| Severe failure to thrive (tube feeding) | Clinical sign | HP:0001508 | Neonatal/infantile, severe |
| Respiratory insufficiency (variable) | Clinical sign | HP:0002093 | Variable |
| Ocular involvement | Physical manifestation | HP:0000478 | Congenital/early |
| Cerebellar atrophy | Imaging/lab abnormality | HP:0001272 | Early |

**Age of onset:** congenital / neonatal. **Severity:** severe. **Progression:** static-encephalopathy with progressive orthopedic complications (scoliosis, contractures). **Quality of life:** profound — patients are non-verbal/severely disabled, require tube feeding and multidisciplinary care; daily functioning is severely impaired. Per-phenotype QoL instrument data are not available given the recency and size of the cohort.

---

### 4. Genetic / Molecular Information

**Causal gene:** *DHRSX* (dehydrogenase/reductase X-linked; HGNC:18399; OMIM *301034). A short-chain dehydrogenase/reductase (SDR) family oxidoreductase.

- **Location:** PAR1, Xp22.33, with a functional homolog on Yp11.32; escapes X-inactivation (expressed from both X and Y).
- **Structure:** 7 exons; 330-aa protein (~36.4 kDa) with a Rossmann-fold NAD(P)(H) coenzyme-binding site and a substrate-binding subdomain.
- **Enzyme activities:** polyprenol dehydrogenase and dolichal reductase [NAD(P)+]; dual substrate and cofactor specificity ("DHRSX has a unique dual substrate and cofactor specificity" — [PMID: 38821050](https://pubmed.ncbi.nlm.nih.gov/38821050/)).
- **Expression:** widely expressed, highest in pancreas.

**Pathogenic variants.** All reported disease alleles are **missense** (c.541G>T/p.Val181Phe; c.146C>T/p.Thr49Met; c.643C>T/p.Leu215Phe), classified as pathogenic/likely-pathogenic on functional and segregation grounds. **Functional consequence:** loss of function (loss of dolichol-synthesis enzyme activity). **Somatic vs germline:** germline. **Allele frequencies:** these are private/ultra-rare variants; not established at population scale in gnomAD for this disease.

**Modifier genes / epigenetics / chromosomal abnormalities:** None established. Of note, an unrelated observation ("DHRSX duplication" fusion) appears as a recurrent structural event in high-risk pediatric B-ALL RNA-seq data ([PMID: 38811988](https://pubmed.ncbi.nlm.nih.gov/38811988/)); this is a somatic oncologic finding and is **not** related to the germline DHRSX-CDG phenotype.

---

### 5. Environmental Information

Not applicable. DHRSX-CDG is a monogenic inborn error of metabolism with no environmental, lifestyle, toxic, or infectious contributing factors.

---

### 6. Mechanism / Pathophysiology

#### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic missense variants in *DHRSX*** (on X and/or Y PAR1) **lead to** loss of DHRSX oxidoreductase function.
2. Loss of DHRSX **results in** failure of step 1 of the revised dolichol pathway: polyprenol is no longer oxidized to polyprenal (NAD⁺-dependent dehydrogenase step).
3. Loss of DHRSX **also results in** failure of step 3: dolichal is no longer reduced to dolichol (NADPH-dependent reductase step). *(SRD5A3, the intervening step-2 polyprenal reductase, remains intact but cannot compensate because its substrate/product flow is interrupted upstream and downstream.)*
4. Blockade of steps 1 and 3 **leads to** accumulation of polyprenol (and depletion of dolichol), **without** accumulation of polyprenal — the biochemical fingerprint that distinguishes DHRSX deficiency from SRD5A3 deficiency (which accumulates polyprenal).
5. Dolichol depletion **results in** shortage of dolichol-phosphate, the obligate lipid carrier for activated sugars and the growing oligosaccharide. Accumulated polyprenol-phosphate is a poor substitute substrate for glycosyltransferases.
6. Carrier shortage **leads to** impaired assembly of the lipid-linked oligosaccharide (LLO) on the ER membrane.
7. Defective LLO assembly **results in** protein N-hypoglycosylation (CDG type I pattern), detectable as a hypoglycosylated serum transferrin profile.
8. Systemic hypoglycosylation of many glycoproteins **leads to** the multisystem clinical phenotype — with the developing nervous system, cochlea, skeleton, and other organs particularly vulnerable — manifesting as the congenital neurodevelopmental disorder. *(The tissue-specific vulnerability step is inferred by analogy to other dolichol-pathway CDGs rather than directly demonstrated for DHRSX.)*

#### The revised three-step "detour" pathway

```
   Polyprenol
      |   STEP 1: DHRSX  (NAD+-dependent oxidation of terminal -OH to aldehyde)
      v
   Polyprenal
      |   STEP 2: SRD5A3 (reduction of C2-C3 alkene) — "polyprenal reductase"
      v
   Dolichal
      |   STEP 3: DHRSX  (NADPH-dependent reduction of aldehyde to alcohol)
      v
   Dolichol  --->  Dolichol-P  --->  LLO assembly  --->  N-glycosylation
```

**Chemical rationale.** Oxidizing the terminal alcohol of polyprenol to an aldehyde (step 1) activates the adjacent C2–C3 double bond, making it far easier for SRD5A3 to reduce (step 2) than the alkene in polyprenol itself — explaining why a seemingly redundant oxidation/re-reduction "detour" exists. This resolves the long-standing puzzle of how dolichol is made and why SRD5A3-null patients retain residual glycosylation ([PMID: 22304929](https://pubmed.ncbi.nlm.nih.gov/22304929/)).

**Molecular pathway / GO annotations:**
- Dolichol biosynthetic process (GO:0019408); dolichol metabolic process (GO:0019348).
- Protein N-linked glycosylation via LLO assembly in the ER.
- Site of action: endoplasmic reticulum membrane (GO:0005789).
- Secondary/independent DHRSX function: positive regulation of autophagy (GO:0010508) — see below.

**Metabolic changes / biochemical abnormalities.** Elevated polyprenol and polyprenol derivatives, decreased dolichol and derivatives, unchanged polyprenal — the diagnostic metabolite signature of DHRSX deficiency: "Both cell lines showed increased levels of polyprenol and its derivatives, concomitant with decreased levels of dolichol and derivatives, but no change in polyprenal levels, suggesting DHRSX deficiency" ([PMID: 39395802](https://pubmed.ncbi.nlm.nih.gov/39395802/)).

**A second, independent DHRSX function.** Before its dolichol role was known, DHRSX was characterized as "a novel non-classical secretory protein involved in the positive regulation of starvation induced autophagy" ([PMID: 25076851](https://pubmed.ncbi.nlm.nih.gov/25076851/)). Overexpression or recombinant GST-DHRSX increased LC3-II and autophagic flux (reduced p62, polyQ80), while knockdown reduced LC3-II. Whether this secreted/autophagy function contributes to DHRSX-CDG pathophysiology, separate from the ER enzymatic role, is unresolved.

**Cell types / anatomy involved:** neurons (CL:0000540), cerebellar Purkinje cells (CL:0000121), and hepatocytes (CL:0000182) are plausibly affected by systemic hypoglycosylation, but cell-type-specific mechanistic data are not established for DHRSX-CDG.

---

### 7. Anatomical Structures Affected

| Level | Structure | Ontology suggestion |
|---|---|---|
| Organ / system — nervous | Brain, cerebellum (atrophy), CNS, peripheral nerves | UBERON:0002037 (cerebellum), UBERON:0001017 (CNS) |
| Organ / system — musculoskeletal | Vertebral column (scoliosis), joints (contractures) | UBERON:0002391 (vertebral column) |
| Organ / system — sensory | Cochlea / inner ear (SNHL), eyes | UBERON:0001846 (inner ear), UBERON:0000970 (eye) |
| Organ / system — respiratory | Lungs / airway (variable insufficiency) | UBERON:0001004 |
| Organ / system — gastrointestinal | GI tract (feeding difficulty, FTT) | UBERON:0005409 |
| Craniofacial | Facial skeleton (dysmorphism) | — |
| Subcellular | ER membrane (LLO assembly site) | GO:0005789 |

Involvement is **bilateral / systemic**, consistent with a generalized biochemical defect rather than a focal lesion.

---

### 8. Temporal Development

- **Onset:** congenital / neonatal; insidious-to-chronic course.
- **Progression:** the encephalopathy is essentially static (developmental), while orthopedic features (scoliosis, joint contractures) are progressive during childhood.
- **Disease course:** chronic, lifelong.
- **Notable temporal biomarker feature:** the serum transferrin CDG-I abnormality can **normalize with age** — Patient 3's profile normalized by 17 months and was normal in his brother (Patient 4) — so a normal transferrin screen does not exclude the diagnosis ([PMID: 38821050](https://pubmed.ncbi.nlm.nih.gov/38821050/)).
- **Critical periods / remission:** no spontaneous or treatment-induced clinical remission is described; the transferrin normalization is a biochemical, not clinical, phenomenon.

---

### 9. Inheritance and Population

- **Epidemiology:** Prevalence and incidence unknown; presumed ultra-rare (<1/1,000,000). Only 4 patients from 3 families reported worldwide (2024).
- **Inheritance pattern:** **pseudoautosomal-recessive** — the first described human disease of this class. Biallelic missense variants required; *DHRSX* lies in PAR1 of X and Y and escapes X-inactivation ("The first and third steps are performed by DHRSX, whose gene resides on the pseudoautosomal regions of the X and Y chromosomes" — [PMID: 38821050](https://pubmed.ncbi.nlm.nih.gov/38821050/)).
- **Penetrance / expressivity:** presumed complete penetrance for biallelic LoF; variable expressivity (e.g., transferrin normalization, variable respiratory involvement).
- **Sex ratio:** ~1:1 — both sexes affected equally because PAR genes are biallelically expressed in both males and females. Reported cohort included two girls and two boys.
- **Consanguinity / founder effects:** homozygosity (consistent with consanguinity) present in the two singleton families; no founder allele established.
- **Carrier frequency / affected populations / geographic distribution:** not established.

---

### 10. Diagnostics

**Biochemical screening.**
- Serum transferrin isoform analysis (IEF or HPLC/LC-MS): CDG **type I** pattern (defective ER-based N-glycan attachment) in patients 1–3. Caveat: can normalize with age or be normal (patient 4), so a normal screen does not rule out DHRSX-CDG ([PMID: 38821050](https://pubmed.ncbi.nlm.nih.gov/38821050/)).
- **Polyisoprenoid profiling** (fibroblasts/tissue): elevated polyprenol with decreased dolichol and **no** polyprenal accumulation — the key biochemical discriminator from SRD5A3-CDG (which accumulates polyprenal / has a high polyprenol/dolichol ratio) ([PMID: 39395802](https://pubmed.ncbi.nlm.nih.gov/39395802/); [PMID: 22304929](https://pubmed.ncbi.nlm.nih.gov/22304929/)).

**Genetic testing (definitive).** Exome or genome sequencing of *DHRSX*, with explicit attention to its **PAR1 (X/Y) location** — standard variant-calling pipelines may misannotate or under-cover pseudoautosomal loci. Single-gene/panel testing for CDG genes may include *DHRSX* going forward.

**Imaging:** brain MRI may show cerebellar atrophy (HP:0001272).

**Differential diagnosis:** other dolichol-pathway/CDG-I disorders, especially **SRD5A3-CDG** (cerebello-ocular syndrome with eye malformations; distinguished by polyprenal accumulation) ([PMID: 20852264](https://pubmed.ncbi.nlm.nih.gov/20852264/)); other CDG-I subtypes; and mitochondrial disorders, which clinically overlap with CDG ([PMID: 29502919](https://pubmed.ncbi.nlm.nih.gov/29502919/)).

**Screening:** No newborn or population screening exists; diagnosis is currently by clinical suspicion → genetic testing. Note: transferrin-based dried-blood-spot screening exists for CDG generally ([PMID: 30641270](https://pubmed.ncbi.nlm.nih.gov/30641270/)) but is limited here by the potentially normal transferrin profile.

---

### 11. Outcome / Prognosis

- **Severity/morbidity:** severe — profound intellectual disability, epilepsy, tube-dependent failure to thrive, sensorineural deafness, progressive scoliosis/contractures. High disease burden and dependency.
- **Survival / mortality:** long-term survival and mortality data are **not available** given the 2024 discovery and tiny cohort.
- **Prognostic factors / biomarkers:** none validated. Transferrin normalization is not known to predict clinical improvement.
- **Recovery:** no recovery of neurodevelopmental deficits; supportive care only.

---

### 12. Treatment

**No disease-specific or targeted therapy exists.** Management is supportive and multidisciplinary:

| Problem | Supportive intervention | NCIT suggestion |
|---|---|---|
| Seizures | Anti-epileptic drugs | NCIT:C264 (Anticonvulsant Agent) |
| Failure to thrive | Nutritional support / gastrostomy tube feeding | NCIT:C173379 (Enteral Nutrition) |
| Hypotonia / scoliosis / contractures | Physiotherapy, orthopedic/spinal management, bracing | NCIT:C15515 (Physical Therapy) |
| Sensorineural hearing loss | Hearing aids / audiologic support | NCIT:C99290 (Hearing Aid) |
| Developmental disability | Early intervention, special education | — |

**Pharmacogenomics, gene/cell/RNA therapy, surgery-as-cure:** none established. Unlike some CDG subtypes with dietary sugar therapy — **PGM1-CDG** (D-galactose; [PMID: 34043239](https://pubmed.ncbi.nlm.nih.gov/34043239/)), **MPI-CDG** (mannose), or **SLC39A8-CDG** (galactose/manganese; [PMID: 34246313](https://pubmed.ncbi.nlm.nih.gov/34246313/)) — dolichol-pathway CDGs including DHRSX-CDG have **no established sugar-supplement therapy**. Experimental/clinical-trial options are not yet available.

---

### 13. Prevention

- **Primary prevention:** not possible (monogenic congenital disorder).
- **Genetic counseling:** recommended for families. The pseudoautosomal-recessive mechanism has unusual implications — a pathogenic allele can be transmitted on either an X or a Y chromosome, and recurrence risk should be modeled accordingly (illustrated by the affected brothers who inherited one allele via the maternal X and one via the paternal Y).
- **Reproductive options:** prenatal diagnosis / preimplantation genetic testing are feasible in principle once familial variants are known, with careful handling of the PAR1 locus.
- **Secondary/tertiary prevention:** early multidisciplinary intervention to prevent complications (aspiration, contracture progression, scoliosis).

---

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** The revised three-step dolichol pathway is **evolutionarily conserved**. In *Saccharomyces cerevisiae*, the dual role of human DHRSX is split between **two dedicated enzymes, Env9 and Tda5**; deletion of *ENV9* and *TDA5* causes accumulation of polyisoprenoid intermediates, transfer of immature LLOs onto nascent proteins, and defective N-glycosylation ([PMID: 42201967](https://pubmed.ncbi.nlm.nih.gov/42201967/)).
- **Cellular model organism:** The classic **CHO Lec5 and Lec9** glycosylation-deficient mutants are natural DHRSX-null lines — the genomic region containing *DHRSX* is absent, and the defect is corrected by human *DHRSX* but not *SRD5A3* ([PMID: 39395802](https://pubmed.ncbi.nlm.nih.gov/39395802/); [PMID: 38948797](https://pubmed.ncbi.nlm.nih.gov/38948797/)).
- **Natural disease in companion animals / wildlife / zoonosis:** none described; not applicable.

---

### 15. Model Organisms

| Model | Type | Nature | Recapitulation | Reference |
|---|---|---|---|---|
| CHO Lec5 / Lec9 | Mammalian cell line | Natural DHRSX-null (genomic deletion) | Reproduces N-glycosylation defect, polyprenol↑/dolichol↓; rescued by DHRSX not SRD5A3 | [PMID: 39395802](https://pubmed.ncbi.nlm.nih.gov/39395802/); [PMID: 38948797](https://pubmed.ncbi.nlm.nih.gov/38948797/) |
| *S. cerevisiae env9Δ tda5Δ* | Invertebrate/fungal | Double knockout of the two DHRSX orthologs | Recapitulates polyisoprenoid accumulation, immature LLO transfer, defective N-glycosylation | [PMID: 42201967](https://pubmed.ncbi.nlm.nih.gov/42201967/) |
| DHRSX-KO cultured cells | In vitro | Engineered knockout | Reproduces metabolite signature (polyprenol↑, no polyprenal change) | [PMID: 38821050](https://pubmed.ncbi.nlm.nih.gov/38821050/) |

**Complementation evidence:** "N-glycan synthesis and changes in polyisoprenoid levels were corrected by complementation with human DHRSX but not with SRD5A3," and "Long-read whole genome sequencing of Lec5 and Lec9 cells did not reveal mutations in the ORF of SRD5A3, but the genomic region containing DHRSX was absent" ([PMID: 39395802](https://pubmed.ncbi.nlm.nih.gov/39395802/)).

**Limitations of models:** cellular and yeast models capture the biochemical glycosylation defect but not the organismal neurodevelopmental phenotype. No dedicated mouse model of DHRSX-CDG is yet reported. Because rodents lack the human PAR1 arrangement of *DHRSX*, faithfully modeling the pseudoautosomal-recessive inheritance in mice is non-trivial.

---

## Mechanistic Model / Interpretation

DHRSX-CDG unifies several previously disconnected observations into a single, coherent model that also rewrote a chapter of glycobiology. For decades, SRD5A3 was thought to be the sole "polyprenol reductase" converting polyprenol directly to dolichol. Two anomalies never fit: (1) SRD5A3-null patients retain substantial correctly glycosylated transferrin (~70%) and near-normal dolichol despite a supposed complete block ([PMID: 22304929](https://pubmed.ncbi.nlm.nih.gov/22304929/)), implying an alternative route; and (2) the CHO Lec5/Lec9 mutants had a dolichol-formation defect with no SRD5A3 lesion.

The 2024 discovery resolves both: dolichol is made via a **three-step detour** in which DHRSX brackets SRD5A3. DHRSX first oxidizes polyprenol to polyprenal (activating the alkene), SRD5A3 reduces the activated alkene to dolichal, and DHRSX then reduces dolichal to dolichol. As stated succinctly in the CHO study: "dolichol synthesis from polyprenol occurs in three steps consisting of the conversion of polyprenol to polyprenal by DHRSX, the reduction of polyprenal to dolichal by SRD5A3, and the reduction of dolichal to dolichol, again by DHRSX" ([PMID: 39395802](https://pubmed.ncbi.nlm.nih.gov/39395802/)). This reassigns SRD5A3 as a **polyprenal reductase** — a relabeling now echoed in SRD5A3-CDG proteomic studies ([PMID: 41732066](https://pubmed.ncbi.nlm.nih.gov/41732066/); [PMID: 39360848](https://pubmed.ncbi.nlm.nih.gov/39360848/)). The Lec5/Lec9 "mystery" is simply DHRSX-null CHO cells ([PMID: 38948797](https://pubmed.ncbi.nlm.nih.gov/38948797/)), and the yeast Env9/Tda5 pair shows the detour is ancient and conserved ([PMID: 42201967](https://pubmed.ncbi.nlm.nih.gov/42201967/)).

The **differential metabolite signatures** are the linchpin of both diagnosis and mechanism: DHRSX loss → polyprenol accumulates, polyprenal unchanged; SRD5A3 loss → polyprenal accumulates. This provides a clean biochemical discriminator between the two dolichol-pathway CDGs whose downstream glycosylation defects are otherwise indistinguishable.

Finally, the **genetics** are the most conceptually novel element. By residing in PAR1 on both X and Y and escaping X-inactivation, *DHRSX* behaves like an autosome but is physically sex-chromosomal — hence "pseudoautosomal-recessive." The affected brothers, carrying one variant from the maternal X and one from the paternal Y, are the definitive proof, and DHRSX-CDG is the first human disease established in this inheritance class.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [38821050](https://pubmed.ncbi.nlm.nih.gov/38821050/) | *A pseudoautosomal glycosylation disorder prompts the revision of dolichol biosynthesis* | **Landmark.** Defines DHRSX-CDG, the pseudoautosomal-recessive inheritance, the three-step detour, DHRSX dual specificity, and the 4-patient cohort |
| [39395802](https://pubmed.ncbi.nlm.nih.gov/39395802/) | *Absence of DHRSX leads to N-glycosylation defects in Lec5/Lec9 CHO cells* | Establishes Lec5/Lec9 as DHRSX-null models; defines the polyprenol↑/dolichol↓/polyprenal-unchanged signature |
| [38948797](https://pubmed.ncbi.nlm.nih.gov/38948797/) | *Lec5/Lec9 defect caused by absence of DHRSX* | Confirms genomic *DHRSX* absence in classic CHO mutants; restates the three enzymatic steps |
| [42201967](https://pubmed.ncbi.nlm.nih.gov/42201967/) | *Revised three-step detour conserved in budding yeast* | Evolutionary conservation; Env9/Tda5 as yeast DHRSX orthologs |
| [25076851](https://pubmed.ncbi.nlm.nih.gov/25076851/) | *DHRSX, a non-classical secretory protein associated with autophagy* | Documents DHRSX's second, enzyme-independent function in starvation-induced autophagy |
| [22304929](https://pubmed.ncbi.nlm.nih.gov/22304929/) | *Life with too much polyprenol: polyprenol reductase deficiency* | SRD5A3-CDG comparator; residual glycosylation implies an alternative dolichol route (now explained by the detour) |
| [20852264](https://pubmed.ncbi.nlm.nih.gov/20852264/) | *Cerebello-ocular syndrome due to dolichol metabolism (SRD5A3)* | Key differential diagnosis; dolichol-pathway CDG phenotype anchor |
| [41732066](https://pubmed.ncbi.nlm.nih.gov/41732066/) | *Hypoglycosylation of serum N-glycoproteins in SRD5A3 deficiency* | Supports SRD5A3's reassignment as polyprenal reductase; downstream glycoproteomic consequences |
| [39360848](https://pubmed.ncbi.nlm.nih.gov/39360848/) | *N-glycoproteomic/proteomic alterations in SRD5A3-deficient fibroblasts* | Illustrates systemic glycoprotein/organelle consequences of dolichol-pathway CDG |
| [40902550](https://pubmed.ncbi.nlm.nih.gov/40902550/) | *Genetic disorders of dolichol synthesis and utilization (review)* | Contextual review situating DHRSX-CDG among dolichol CDGs |
| [34043239](https://pubmed.ncbi.nlm.nih.gov/34043239/) | *D-galactose treatment monitoring in PGM1-CDG* | Contrast: treatable CDG subtype vs. untreatable dolichol CDGs |
| [34246313](https://pubmed.ncbi.nlm.nih.gov/34246313/) | *SLC39A8-CDG clinical/glycophenotype* | Contrast: treatable CDG (galactose/Mn); transferrin can normalize |
| [29502919](https://pubmed.ncbi.nlm.nih.gov/29502919/) | *CDG vs mitochondrial disorder overlap* | Differential-diagnosis context |
| [30641270](https://pubmed.ncbi.nlm.nih.gov/30641270/) | *Transferrin glycosylation from dried blood spots* | Screening methodology context |
| [28139241](https://pubmed.ncbi.nlm.nih.gov/28139241/) | *Population-based CDG diagnosis (Spain)* | Epidemiologic/diagnostic context for CDG broadly |
| [38811988](https://pubmed.ncbi.nlm.nih.gov/38811988/) | *RNA-seq in pediatric B-ALL (DHRSX duplication)* | Distinguishes an unrelated **somatic** DHRSX fusion from germline DHRSX-CDG |

---

## Limitations and Knowledge Gaps

1. **Tiny cohort.** All clinical data derive from 4 patients in 3 families ([PMID: 38821050](https://pubmed.ncbi.nlm.nih.gov/38821050/)). Phenotype frequencies, penetrance, expressivity, natural history, and prognosis are therefore provisional. No expanded series exists (a caution: 9/10- or 6/7-type fractions in the literature belong to a separate PMM2-CDG cohort, not DHRSX-CDG).
2. **No epidemiology.** Prevalence, incidence, carrier frequency, founder effects, and geographic/ethnic distribution are unknown.
3. **Diagnostic caveat.** The transferrin CDG-I marker can normalize with age or be normal — meaning biochemical screening can miss cases; molecular testing at the PAR1 locus is essential.
4. **No survival/mortality data.**
5. **No therapy.** No disease-specific treatment, and no sugar-supplement therapy applicable (unlike PGM1-/MPI-/SLC39A8-CDG).
6. **Ontology gaps.** No dedicated MONDO, Orphanet, or ICD-11 entry yet; HPO frequency annotations for DHRSX-CDG are not curated.
7. **Unresolved dual function.** The contribution (if any) of DHRSX's secreted/autophagy-regulating role ([PMID: 25076851](https://pubmed.ncbi.nlm.nih.gov/25076851/)) to disease pathophysiology, versus the ER dolichol-synthesis role, is unknown.
8. **No whole-organism animal model** faithfully reproducing the pseudoautosomal genetics and neurodevelopmental phenotype.

---

## Proposed Follow-up Experiments / Actions

1. **International case-finding.** Reanalyze CDG-I cohorts and unsolved neurodevelopmental exomes/genomes with PAR1-aware variant calling to identify additional DHRSX-CDG patients and build a natural-history registry.
2. **Diagnostic standardization.** Deploy polyisoprenoid profiling (polyprenol/polyprenal/dolichol ratios) as a confirmatory second-tier test that discriminates DHRSX-CDG from SRD5A3-CDG independent of the unreliable transferrin marker.
3. **Ontology curation.** Request dedicated MONDO, Orphanet, and ICD-11 identifiers and HPO frequency annotations for DHRSX-CDG.
4. **Structure–function.** Determine DHRSX structure (cryo-EM/X-ray or refine AlphaFold model) and map the p.Val181Phe, p.Thr49Met, and p.Leu215Phe residues onto the NAD(P)(H)-binding and substrate pockets to establish genotype–function correlations.
5. **Animal/organoid models.** Generate humanized or conditional mouse and/or iPSC-derived neural organoid models to study tissue-specific vulnerability and to serve as therapeutic testbeds.
6. **Therapeutic exploration.** Test whether dolichol or dolichal supplementation, or bypass strategies, can restore LLO assembly in DHRSX-null cells — a first step toward a substrate-replacement approach.
7. **Resolve the dual-function question.** Use catalytically dead vs. secretion-deficient DHRSX constructs to dissect the dolichol-synthesis role from the autophagy/secretory role in disease-relevant cells.


## Artifacts

- [OpenScientist final report](DHRSX-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](DHRSX-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 20 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 16 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0015286` (2 mentions) - the report calls it "congenital disorder of glycosylation", "grouping"; MONDO calls it **congenital disorder of glycosylation**
- `HP:0001999` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Abnormal facial shape**
- `HP:0001252` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hypotonia**
- `HP:0001250` (1 mention) - the report calls it "Clinical sign"; HP calls it **Seizure**
- `HP:0000407` (1 mention) - the report calls it "Laboratory/clinical"; HP calls it **Sensorineural hearing impairment**
- `HP:0002650` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Scoliosis**
- `HP:0002803` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Congenital contracture**
- `HP:0001508` (1 mention) - the report calls it "Clinical sign"; HP calls it **Failure to thrive**
- `HP:0002093` (1 mention) - the report calls it "Clinical sign"; HP calls it **Respiratory insufficiency**
- `HP:0000478` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Abnormality of the eye**
- `HP:0001272` (2 mentions) - the report calls it "Imaging/lab abnormality"; HP calls it **Cerebellar atrophy**
- `UBERON:0002391` (1 mention) - the report calls it "vertebral column"; UBERON calls it **lymph**
- `UBERON:0001004` (1 mention) - the report calls it "Lungs / airway (variable insufficiency)"; UBERON calls it **respiratory system**
- `UBERON:0005409` (1 mention) - the report calls it "GI tract (feeding difficulty, FTT)"; UBERON calls it **alimentary part of gastrointestinal system**
- `NCIT:C15515` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Colony-Stimulating Factor Therapy**
- `NCIT:C99290` (1 mention) - the report calls it "Hearing Aid"; NCIT calls it **TCF3/HLF Fusion Protein**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `NCIT:C173379` (1 mention), reported as "Enteral Nutrition" - NCIT does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0019408` (obsolete dolichol biosynthetic process) (1 mention) - replaced by `GO:0043048`
- `GO:0019348` (obsolete dolichol metabolic process) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0019408` (1 mention) - the report calls it "Dolichol biosynthetic process"; GO calls it **obsolete dolichol biosynthetic process**
- `GO:0005789` (2 mentions) - the report calls it "Site of action: endoplasmic reticulum membrane", "ER membrane (LLO assembly site)"; GO calls it **endoplasmic reticulum membrane**, and lists "ER membrane" among its other names
- `GO:0010508` (1 mention) - the report calls it "Secondary/independent DHRSX function: positive regulation of autophagy"; GO calls it **positive regulation of autophagy**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0015286` - called "congenital disorder of glycosylation", "grouping"
- `GO:0005789` - called "Site of action: endoplasmic reticulum membrane", "ER membrane (LLO assembly site)"
