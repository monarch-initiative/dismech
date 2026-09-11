---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T18:52:51.398026'
end_time: '2026-09-03T19:04:06.868854'
duration_seconds: 675.47
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Chromosome 3q29 Microduplication Syndrome
  mondo_id: MONDO:0012761
  category: Chromosomal Disorder
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
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 16
  validator_version: 0.2.1
term_validation:
  total_terms: 42
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 6
  confabulation_rate: 0.0
  labels_checked: 26
  labels_matching: 4
  labels_mismatched: 16
  mislabelled_terms:
  - term_id: HP:0000750
    reported_labels:
    - Childhood
    ontology_label: Delayed speech and language development
  - term_id: HP:0001328
    reported_labels:
    - Childhood
    ontology_label: Specific learning disability
  - term_id: HP:0001249
    reported_labels:
    - Childhood
    ontology_label: Intellectual disability
  - term_id: HP:0000252
    reported_labels:
    - Congenital/childhood
    ontology_label: Microcephaly
  - term_id: HP:0000256
    reported_labels:
    - Childhood
    ontology_label: Macrocephaly
  - term_id: HP:0000478
    reported_labels:
    - Congenital/childhood
    ontology_label: Abnormality of the eye
  - term_id: HP:0001250
    reported_labels:
    - Childhood
    ontology_label: Seizure
  - term_id: HP:0002011
    reported_labels:
    - Variable
    ontology_label: Morphological central nervous system abnormality
  - term_id: HP:0001513
    reported_labels:
    - Childhood
    ontology_label: Obesity
  - term_id: HP:0000175
    reported_labels:
    - Congenital
    ontology_label: Cleft palate
  - term_id: HP:0011842
    reported_labels:
    - Childhood
    ontology_label: Abnormal skeletal morphology
  - term_id: HP:0000164
    reported_labels:
    - Childhood
    ontology_label: Abnormality of the dentition
  - term_id: HP:0001252
    reported_labels:
    - Infancy
    ontology_label: Hypotonia
  - term_id: HP:0000717
    reported_labels:
    - Childhood
    ontology_label: Autism
  - term_id: HP:0002719
    reported_labels:
    - Variable
    ontology_label: Recurrent infections
  - term_id: UBERON:0000970
    reported_labels:
    - Secondary organ involvement:** eye
    ontology_label: eye
  labels_variant: 6
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
  path: Chromosome_3q29_Microduplication_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Chromosome_3q29_Microduplication_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chromosome 3q29 Microduplication Syndrome
- **MONDO ID:** MONDO:0012761 (if available)
- **Category:** Chromosomal Disorder

## Research Objectives

Please provide a comprehensive research report on **Chromosome 3q29 Microduplication Syndrome** covering all of the
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

# Chromosome 3q29 Microduplication Syndrome — Comprehensive Disease Characterization

**MONDO:** MONDO:0012761 · **Category:** Chromosomal (genomic copy-number) disorder
**Report basis:** Aggregated primary literature (case series, cohorts, reviews). No individual EHR data used.
**Date:** 2026-09-03

> **Evidence note.** This is a rare disorder described almost entirely through case reports and small cohorts. The largest single cohort to date is 46 patients (PMID 38421086). Frequencies below are indicative, not population-validated, and most mechanistic claims are inferred from gene content and from the better-studied reciprocal **3q29 deletion**. Statements are flagged where they derive from the deletion rather than the duplication.

---

## 1. Disease Information

**Overview.** Chromosome 3q29 microduplication syndrome is a rare genomic disorder caused by a recurrent copy-number **gain** of ~1.6 Mb at chromosome band 3q29 (hg19 chr3:~195,700,000–197,350,000). It is the reciprocal of the better-characterized 3q29 microdeletion syndrome. The clinical picture is a **variable, generally mild neurodevelopmental disorder**: developmental/speech delay, learning disability or mild–moderate intellectual disability, and a range of accessory features (dysmorphism, ocular and cardiac anomalies, micro- or macrocephaly, obesity). Many carriers are only mildly affected and the duplication is often inherited from a similarly mild parent, so it behaves partly as a **susceptibility factor** rather than a fully penetrant syndrome (PMID 38421086, 33039685, 39739615).

**Key identifiers.**
- **MONDO:** MONDO:0012761
- **OMIM:** 611936 (Chromosome 3q29 microduplication syndrome)
- **Orphanet:** ORPHA:284169 (3q29 microduplication syndrome)
- **ICD-11:** LD44 (chromosomal duplication category); **ICD-10:** Q92.3 (partial trisomy)
- **Reciprocal disorder:** 3q29 microdeletion syndrome — OMIM 609425, Orphanet ORPHA:66634

**Synonyms / alternative names:** 3q29 duplication syndrome; 3q29 microduplication; trisomy 3q29; dup(3)(q29); 3q29 microduplication syndrome (reciprocal to 3q29 deletion).

**Information source type:** Disease-level aggregated resources plus published individual case reports; not derived from a single EHR system. A patient registry exists for the reciprocal deletion (3q29deletion.org, PMID 37691301).

---

## 2. Etiology

**Primary cause — genetic (structural).** A recurrent interstitial **duplication of ~1.6 Mb at 3q29** containing ~21 protein-coding genes (PMID 37165454). Reported duplications range from ~448 kb to ~2.3 Mb, classically spanning **TFRC → BDH1** (PMID 29501613). Origin is **non-allelic homologous recombination (NAHR)** between flanking segmental duplications (low-copy repeats): in 89% (16/18) of probands breakpoints fell within paralogous 20-kbp segments inside the 3q29 SDs (PMID 37165454).

**Genetic risk factors.**
- The recurrent CNV itself is the causal lesion.
- **Second-hit CNVs / additional variants** act as risk/modifier factors and were frequent in cohorts (PMID 33039685); additional contributory genetic findings were present in 11/46 patients (PMID 38421086).
- Local **segmental-duplication architecture and haplotype diversity** at 3q29 modulate NAHR risk (PMID 37165454).

**Environmental risk factors:** None established. No toxin, infectious, dietary, or occupational exposure is implicated in causing the CNV. Parental age effects are not established for this locus.

**Protective factors:** None specifically identified. Reduced penetrance implies protective genetic-background/modifier effects exist but are uncharacterized.

**Gene–environment interactions:** No specific GxE interaction documented. Variable expressivity is currently best explained by **genetic modifiers / second-hit variants** (oligogenic model), not by environment (PMID 33039685, 38421086).

---

## 3. Phenotypes

Phenotype frequencies are approximate (small cohorts, ascertainment bias toward NDD). Duplication features are consistently **less frequent and milder** than in the reciprocal deletion (PMID 39739615).

| Phenotype | Type | Frequency (indicative) | Onset | Suggested HPO |
|---|---|---|---|---|
| Speech/language delay | developmental | Common (most frequent) | Childhood | HP:0000750 |
| Global developmental delay | developmental | Common | Infancy/childhood | HP:0001263 |
| Learning disability | cognitive | High (isolated dup) | Childhood | HP:0001328 |
| Intellectual disability (mild–moderate) | cognitive | Lower than in deletion | Childhood | HP:0001249 |
| Microcephaly | physical | ~50% of reported patients | Congenital/childhood | HP:0000252 |
| Macrocephaly | physical | Subset | Childhood | HP:0000256 |
| Facial dysmorphism | physical sign | Common | Congenital | HP:0001999 / HP:0000271 |
| Ocular abnormalities | physical | Frequent | Congenital/childhood | HP:0000478 |
| Congenital heart defect | physical | Frequent | Congenital | HP:0001627 |
| Epilepsy/seizures | neurological | Subset | Childhood | HP:0001250 |
| Structural brain anomaly (e.g., gray-matter heterotopia, cortical atrophy) | imaging | Subset | Variable | HP:0002011 |
| Generalized obesity / overweight | metabolic | Subset (mirror trait) | Childhood | HP:0001513 |
| Cleft palate | physical | Uncommon | Congenital | HP:0000175 |
| Musculoskeletal anomalies | physical | Subset | Childhood | HP:0011842 |
| Dental anomalies | physical | Subset | Childhood | HP:0000164 |
| Hypotonia | neurological | Subset | Infancy | HP:0001252 |
| ASD / autistic features | behavioral | Subset | Childhood | HP:0000717 |
| Recurrent infections | immunologic | Reported (case) | Variable | HP:0002719 |

- **Phenotype characteristics:** onset predominantly **congenital-to-childhood**; a notable **late-onset (age 34) presentation** with progressive cortical atrophy and recurrent mucosal infections has been reported (PMID 32874693). Severity is **variable/mild**; course generally **stable** (developmental), though brain-atrophy and epilepsy subsets may progress.
- **Quality-of-life impact:** driven mainly by cognitive/learning and speech impairment affecting education and daily functioning; cardiac/ocular anomalies may need intervention. No syndrome-specific EQ-5D/SF-36 data published for the duplication.

Core spectrum quote: *"clinical features that include intellectual disability, language delay, epilepsy, structural brain anomalies, micro/macrocephaly, generalized obesity, ocular abnormalities, distinctive facial features, cleft palate, and musculoskeletal anomalies"* (PMID 33039685).

**Psychiatric distinction (important).** Large schizophrenia case-control CNV studies associate the **3q29 deletion** — not the duplication — with schizophrenia (PMID 24776740, 22130109). The **duplication** is instead a recurrent susceptibility locus for **autism spectrum disorder and developmental delay** (PMID 22900207, 39080272), with schizophrenia and generalized anxiety being phenotypes unique to deletion carriers (PMID 39739615). Counseling should reflect this dosage-direction asymmetry.

---

## 4. Genetic / Molecular Information

**Causal lesion:** recurrent 3q29 duplication (dosage gain), not a point mutation. **Variant class:** structural — copy-number gain (tandem/interstitial duplication). **ACMG/AMP CNV classification:** recurrent 1.6-Mb 3q29 duplication is generally **VUS to likely pathogenic / pathogenic with reduced penetrance** depending on inheritance and second hits; many are inherited from unaffected/mildly affected parents (PMID 38421086).

**Genes in the recurrent interval (~21 protein-coding), key candidates:**
- **DLG1** (HGNC:2900; SAP97) — synaptic MAGUK scaffolding protein; strongest candidate (PMID 29501613, 24838842).
- **BDH1** (HGNC:1027) — mitochondrial 3-hydroxybutyrate dehydrogenase (ketone-body/energy metabolism); smallest single-gene critical region defined (PMID 39739615, 29501613).
- **PAK2** (HGNC:8591) — p21-activated kinase; cytoskeletal/synaptic signaling (PMID 24838842).
- **FBXO45** (HGNC:29148) — synaptic ubiquitin-ligase adaptor, neuronal development (PMID 24838842).
**Full verified gene inventory (Ensembl GRCh37, chr3:195,700,000–197,350,000; 22 protein-coding genes, this analysis):** BDH1, CEP19, DLG1, FBXO45, MFI2/MELTF, NCBP2, NRROS/LRRC33, PAK2, PCYT1A, PIGX, PIGZ, RNF168, SENP5, SLC51A/OSTA, SMCO1, TCTEX1D2, TFRC, TM4SF19, UBXN7, WDR53, ZDHHC19 (+1 putative transcript). This matches the literature "~21 genes" (PMID 37165454).

**Contiguous-gene / dosage-pleiotropy links (candidate):** beyond the neurodevelopmental core (DLG1, PAK2, FBXO45, BDH1), the interval carries genes with independent Mendelian disease relevance that plausibly contribute to the pleiotropic phenotype: **CEP19** (recessive morbid obesity / ciliopathy → obesity), **PCYT1A** (retinal dystrophy with spondylometaphyseal dysplasia → ocular anomalies), **RNF168** (RIDDLE-syndrome DNA-damage response → immune/radiosensitivity), **TFRC** (transferrin receptor; combined immunodeficiency → recurrent infections). These are hypothesized dosage contributors, not proven for the duplication.

**Minimal critical region:** progressively refined from DLG1+BDH1 (448 kb; PMID 29501613) to **BDH1 alone** (single-gene duplications associated with ASD, heart defects, biliary tract dysfunction, obesity; PMID 39739615).

**Functional consequence:** presumed **gain-of-dosage (increased gene expression)** of dosage-sensitive synaptic/metabolic genes; not loss-of-function.

**Allele frequency:** rare; the recurrent CNV is essentially absent/very rare in gnomAD-SV controls and enriched in NDD cohorts (~1:5000 among NDD patients; PMID 39739615).

**Somatic vs germline:** germline; both **de novo and inherited** (most inherited; PMID 38421086). Post-zygotic occurrence documented as a discordant CNV in monozygotic twins with psychosis (PMID 39080272).

**Modifier genes / epigenetics:** second-hit CNVs modify severity (PMID 33039685); no locus-specific methylation/histone signature (episignature) is established for the duplication. **Chromosomal abnormality:** dup(3)(q29), submicroscopic — karyotype normal, detected by microarray.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious agent is known to cause or trigger 3q29 microduplication syndrome. It is a constitutional genomic disorder. (Obesity within the phenotype may be modulated by diet/lifestyle as in the general population, but this is not disease-specific.) Infectious agents: not applicable.

---

## 6. Mechanism / Pathophysiology

**Causal chain (initiating lesion → clinical manifestation):**

1. **Segmental duplications flanking 3q29** provide high sequence identity that **predisposes to misalignment** during meiosis (PMID 37165454).
2. Misalignment **leads to** non-allelic homologous recombination (NAHR) between paralogous ~20-kbp SD segments (PMID 37165454).
3. NAHR **results in** a recurrent ~1.6-Mb **duplication** (3 copies) of ~21 genes, transmitted in the germline.
4. Extra gene copies **lead to** increased dosage/expression of dosage-sensitive genes — notably **DLG1, BDH1, PAK2, FBXO45** (inferred; PMID 29501613, 24838842).
5. Elevated **DLG1/PAK2/FBXO45** dosage **is inferred to perturb** synapse assembly, glutamatergic scaffolding and neuronal cytoskeletal signaling (inferred from gene function; PMID 24838842).
6. Elevated **BDH1** dosage **is inferred to alter** ketone-body/mitochondrial energy metabolism, potentially affecting neuronal and biliary function (inferred; PMID 39739615).
7. Synaptic + metabolic perturbation **leads to** altered neurodevelopment → developmental/speech delay, learning disability, variable ID, seizures, brain structural anomalies (PMID 33039685, 29501613).
8. **Branch:** presence of a **second-hit variant/CNV** shifts the outcome toward more severe/syndromic disease (e.g., cerebral palsy, severe ID); its absence **results in** the common mild phenotype (PMID 33039685, 38421086).
9. Reduced penetrance: in a permissive genetic background the dosage gain **may produce** no or minimal clinical effect (inherited-from-unaffected-parent scenario; PMID 38421086).

**Molecular pathways (candidate):** glutamatergic synaptic scaffolding via DLG1/PSD-95 family (MAGUK); PAK2-mediated Rho-GTPase/cytoskeletal signaling; ketone-body metabolism via BDH1. **Cellular processes:** synapse organization, dendritic/spine development, neuronal migration (heterotopia reported, PMID 29501613). **Metabolic changes:** possible ketone/energy-metabolism shift via BDH1 (interconverts acetoacetate ↔ D-3-hydroxybutyrate; CHEBI:17968 (R)-3-hydroxybutyrate, CHEBI:13705 acetoacetate), and biliary tract dysfunction (PMID 39739615); SLC51A/OSTA in the interval is a bile-acid transporter, offering a candidate link to the reported biliary phenotype. **Immune involvement:** recurrent infections in isolated cases (PMID 32874693) — not a core feature.

**Model-organism support:** direct duplication models are lacking. **Deletion Df/+ mice** show neurodevelopmental/behavioral abnormalities and reduced paraventricular oxytocin neurons, with social deficits rescued by oxytocin (PMID 35346312) — informative for the locus but reflecting loss, not gain, of dosage.

**Suggested ontology terms:** GO:0050808 (synapse organization), GO:0007268 (chemical synaptic transmission), GO:0007612/GO:0007611 (learning/memory), GO:0046951 (ketone body biosynthesis); CL:0000540 (neuron), CL:0000679 (glutamatergic neuron).

---

## 7. Anatomical Structures Affected

- **Primary organ/system:** central nervous system (UBERON:0001017) — brain (UBERON:0000955); cerebral cortex, lateral ventricles (periventricular heterotopia, PMID 29501613), cortical atrophy (PMID 32874693).
- **Secondary organ involvement:** eye (UBERON:0000970) — ocular anomalies; heart (UBERON:0000948) — congenital heart defects; craniofacial skeleton — dysmorphism, cleft palate (UBERON:0001716 secondary palate); musculoskeletal system; teeth; biliary tract (case-level, PMID 39739615); adipose/metabolic (obesity).
- **Body systems:** nervous, cardiovascular, ocular/visual, musculoskeletal, craniofacial, endocrine/metabolic.
- **Cell/tissue level:** neurons and synapses (nervous tissue) are the principal targets.
- **Subcellular:** postsynaptic density/synapse (GO:0014069), mitochondria (GO:0005739, via BDH1), nucleus.
- **Lateralization:** generally bilateral/symmetric; the reported heterotopia was unilateral (right lateral ventricle, PMID 29501613).

---

## 8. Temporal Development

- **Onset:** congenital to early childhood; developmental delay usually recognized in infancy/toddlerhood. A **late-onset adult** presentation (34 y) is documented (PMID 32874693). Onset pattern: **insidious/chronic** (developmental).
- **Progression:** developmental features are generally **stable** over time; most carriers are non-progressive. Subsets show **progressive** features (cortical atrophy, epilepsy) (PMID 32874693). Duration: **lifelong**.
- **Course pattern:** static/chronic; not relapsing-remitting.
- **Critical periods:** prenatal/early-childhood neurodevelopment is the key window; several diagnoses were made **prenatally** by microarray (PMID 33039685), enabling early developmental intervention.

---

## 9. Inheritance and Population

- **Epidemiology:** rare; estimated **~1:5000 among patients with a neurodevelopmental phenotype** (PMID 39739615). General-population prevalence is not firmly established; only ~60+ patients are described in the literature (16 early cases + 11 [PMID 33039685] + 46-patient cohort [PMID 38421086] + others).
- **Inheritance pattern:** autosomal, **dominant with reduced penetrance and variable expressivity**; **most cases inherited** from a mildly affected/unaffected parent, some de novo (PMID 38421086).
- **Penetrance:** incomplete/reduced (PMID 39739615). **Expressivity:** highly variable (PMID 32874693).
- **Anticipation:** not established. **Germline/post-zygotic mosaicism:** post-zygotic origin documented in an MZ-twin pair discordant for psychosis (PMID 39080272). **Founder effects/consanguinity:** not relevant (recurrent NAHR event, not a founder mutation). **Carrier frequency:** not defined.
- **Population demographics:** no strong ethnic predilection; cohorts from Europe (France, Romania, Italy), North America, China. **Sex ratio:** roughly balanced/slight male excess in NDD cohorts (~56–62% male in related 3q29 series, PMID 37691301, 35297118). **Age distribution:** predominantly children at ascertainment.

---

## 10. Diagnostics

- **First-line test:** **chromosomal microarray analysis (CMA / aCGH / SNP-array)** — the diagnostic gold standard; detects the submicroscopic ~1.6-Mb gain (PMID 33039685, 32874693). **Karyotype is normal** (lesion below cytogenetic resolution).
- **Confirmation/segregation:** qPCR and **FISH**; parental testing to assess inheritance (PMID 39739615).
- **Sequencing:** **WES/WGS** recommended when presentation is **severe or syndromic**, to detect modifying second-hit variants (PMID 38421086). Long-read/optical mapping resolves complex SD architecture and breakpoints (research; PMID 37165454).
- **Prenatal:** CMA on chorionic villus/amniocentesis samples — several 3q29 duplications identified prenatally (PMID 33039685).
- **Adjunct workup by phenotype:** brain MRI (heterotopia, atrophy; PMID 29501613, 32874693), echocardiography (CHD), ophthalmologic exam, developmental/cognitive assessment.
- **Biomarkers:** no specific molecular biomarker; diagnosis is genomic.
- **Differential diagnosis:** other recurrent NDD-associated CNVs (16p11.2, 22q11.2, 1q21.1), 3q29 **deletion** syndrome, and overlapping trisomy 3q / adjacent CNVs (e.g., 1q43q44 overlap, PMID 30263904; OAVS-associated proximal 3q29 dup, PMID 25735547). Co-occurring monogenic disease can confound (e.g., AMeD/ADH5-ALDH2, PMID 41039406).
- **Screening:** not part of newborn screening; **cascade testing** of relatives is appropriate given frequent inheritance.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** the syndrome is **not intrinsically life-limiting**; no reduced life expectancy documented for isolated duplications. Mortality risk depends on associated anomalies (e.g., severe congenital heart disease).
- **Morbidity/function:** dominated by **learning disability, speech/language impairment and variable ID**; global adaptive-function deficits are well documented in the reciprocal deletion (PMID 37740553) and, more mildly, expected here. Most isolated-duplication patients have **mild NDD** (PMID 38421086).
- **Complications:** epilepsy, structural brain anomalies, cardiac and ocular disease, obesity, musculoskeletal issues; psychiatric comorbidity possible but **less than in the deletion** (schizophrenia/GAD were unique to deletion carriers, PMID 39739615).
- **Recovery/course:** developmental features are stable/chronic; early intervention (speech/OT/PT, special education) improves functional outcome.
- **Prognostic factors:** **presence of a second-hit variant** and additional structural anomalies predict a more severe outcome (PMID 33039685, 38421086); isolated duplication predicts milder outcome.

---

## 12. Treatment

No disease-specific or curative therapy exists; management is **symptomatic, multidisciplinary and supportive**.

- **Developmental/behavioral:** early intervention — speech therapy, occupational therapy, physical therapy, special education; behavioral support for ASD/ADHD features (NCIT: Rehabilitation Therapy).
- **Neurologic:** standard **antiseizure medication** for epilepsy (NCIT: Anticonvulsant Agent).
- **Psychiatric:** treat comorbid ADHD/anxiety/psychosis per standard guidelines if present (more relevant to the reciprocal deletion).
- **Cardiac:** surgical/interventional correction of congenital heart defects as indicated (e.g., valvuloplasty) (NCIT: Cardiac Surgery); reciprocal-deletion literature includes balloon valvuloplasty for pulmonary stenosis (PMID 36305444).
- **Ophthalmologic/orthopedic/dental:** treat specific anomalies (strabismus/refractive correction, scoliosis/pectus management, dental care).
- **Metabolic:** weight/obesity management.
- **Pharmacogenomics / advanced therapeutics (gene, cell, RNA, targeted, immuno):** none established or in trials specific to this CNV. **Oxytocin** rescued social deficits in the deletion mouse model (PMID 35346312) — hypothesis-generating, not a duplication therapy.
- **Genetic counseling:** essential given frequent parental inheritance and reduced penetrance.

---

## 13. Prevention

- **Primary prevention:** none possible (constitutional germline CNV). **Genetic counseling** for recurrence risk (up to ~50% transmission from a carrier parent, though penetrance is reduced) (PMID 38421086).
- **Reproductive options:** **prenatal CMA** (documented prenatal diagnoses, PMID 33039685) and **preimplantation genetic testing** for known familial CNV.
- **Secondary prevention:** early developmental screening and intervention; surveillance for treatable anomalies (cardiac, ocular, seizures).
- **Tertiary prevention:** multidisciplinary follow-up to limit complications (educational support, epilepsy control, cardiac monitoring).
- **Cascade screening** of at-risk relatives.
- Immunization / public-health / environmental interventions: not applicable to etiology.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens* (NCBI:txid9606). No naturally occurring 3q29-duplication disease is described in companion animals or wildlife (OMIA: none specific).
- **Orthologous genes:** the human 3q29 genes have conserved mouse orthologs (Dlg1, Bdh1, Pak2, Fbxo45) enabling engineered models. **Evolutionary conservation:** synaptic scaffolding (DLG1) and PAK signaling are deeply conserved across vertebrates.
- **Comparative biology:** the syntenic region has been engineered in mouse (deletion Df/+; PMID 35346312). **Zoonotic potential / transmission:** not applicable.

---

## 15. Model Organisms

- **Available models:** **mouse** is the principal system. A **3q29 deletion mouse (Df/+)** recapitulates neurodevelopmental/behavioral abnormalities with high construct and face validity and shows reduced hypothalamic oxytocin neurons (PMID 35346312). A dedicated **duplication (gain-of-dosage) mouse model is, to the best of current literature, lacking** — a key gap.
- **Model types:** engineered chromosomal-region models (deletion); single-gene transgenic/knock-in models of DLG1, PAK2, BDH1 exist in general neuroscience literature and could serve as candidate-gene overexpression models.
- **Phenotype recapitulation:** deletion Df/+ mice reproduce social/behavioral deficits (face validity) but model the opposite dosage direction to the duplication; caution in interpretation.
- **Applications:** dissecting synaptic and oxytocinergic mechanisms; testing candidate interventions (e.g., oxytocin, PMID 35346312).
- **Resources:** MGI (mouse orthologs Dlg1, Bdh1, Pak2, Fbxo45); IMPC/IMSR for single-gene alleles.

---

## Key References (PMID)
- 33039685 — Coyan & Dyer 2020: 11 new cases + literature; second-hit modifiers; prenatal cases.
- 38421086 — Massier et al. 2024: cohort of 46 patients; mild inherited NDD; SRO uncertain.
- 39739615 — Kashevarova et al. 2025: review + BDH1 single-gene critical region; dup vs del comparison; 1:5000.
- 29501613 — Tassano et al. 2018: 448-kb DLG1+BDH1 critical region; heterotopia.
- 24838842 — Fernández-Jaén et al. 2014: severe case; PAK2/DLG1/BDH1/FBXO45 candidates.
- 32874693 — Streata et al. 2020: phenotype heterogeneity; late-onset case.
- 37165454 — Yilmaz et al. 2023: NAHR mechanism, segmental duplications, 21 genes.
- 30263904 — Kessi et al. 2018: overlapping CNV case.
- 25735547 — Guida et al. 2015: proximal 3q29 dup with OAVS.
- 39080272 — Ormond et al. 2024: post-zygotic 3q29 dup in MZ twins.
- 41039406 — 2025: 3q29 dup co-occurring with AMeD (ADH5/ALDH2) syndrome.
- 35346312 — Takemoto et al. 2022: 3q29 **deletion** mouse; oxytocin rescue.
- 36305444 — Kaba & Çelik 2022: reciprocal 3q29 **deletion** case (diagnostic/differential context).
- 37691301 — Pollak et al. 2023: 3q29 registry/musculoskeletal (deletion; registry context).
- 24776740 — Szatkiewicz et al. 2014: Swedish schizophrenia CNV study; 3q29 **deletion** associated with SCZ.
- 22130109 — Grozeva et al. 2012: UK WTCCC CNV frequencies; 3q29 **deletion** enriched in SCZ.
- 22900207 — Nomura & Takumi 2012: review of CNV-based psychiatric animal models; 3q29 among ASD/SCZ loci.
- Ensembl GRCh37 REST (computational, this analysis): 22 protein-coding genes in chr3:195.70–197.35 Mb.

## Limitations & Future Directions
- Evidence is dominated by case reports/small cohorts; frequencies are indicative and ascertainment-biased toward NDD.
- The smallest region of overlap and the true driver gene(s) remain unresolved (BDH1 vs DLG1 debated).
- No duplication-specific animal model, no episignature, and no locus-specific therapy exist.
- Priorities: large genotype–phenotype registries for the duplication, dosage-gain mouse/organoid models, functional dissection of DLG1/BDH1 overexpression, and quantification of penetrance/recurrence risk for counseling.


## Artifacts

- [OpenScientist final report](Chromosome_3q29_Microduplication_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Chromosome_3q29_Microduplication_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 6 |
| Terms whose name was checked | 26 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 16 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000750` (1 mention) - the report calls it "Childhood"; HP calls it **Delayed speech and language development**
- `HP:0001328` (1 mention) - the report calls it "Childhood"; HP calls it **Specific learning disability**
- `HP:0001249` (1 mention) - the report calls it "Childhood"; HP calls it **Intellectual disability**
- `HP:0000252` (1 mention) - the report calls it "Congenital/childhood"; HP calls it **Microcephaly**
- `HP:0000256` (1 mention) - the report calls it "Childhood"; HP calls it **Macrocephaly**
- `HP:0000478` (1 mention) - the report calls it "Congenital/childhood"; HP calls it **Abnormality of the eye**
- `HP:0001250` (1 mention) - the report calls it "Childhood"; HP calls it **Seizure**
- `HP:0002011` (1 mention) - the report calls it "Variable"; HP calls it **Morphological central nervous system abnormality**
- `HP:0001513` (1 mention) - the report calls it "Childhood"; HP calls it **Obesity**
- `HP:0000175` (1 mention) - the report calls it "Congenital"; HP calls it **Cleft palate**
- `HP:0011842` (1 mention) - the report calls it "Childhood"; HP calls it **Abnormal skeletal morphology**
- `HP:0000164` (1 mention) - the report calls it "Childhood"; HP calls it **Abnormality of the dentition**
- `HP:0001252` (1 mention) - the report calls it "Infancy"; HP calls it **Hypotonia**
- `HP:0000717` (1 mention) - the report calls it "Childhood"; HP calls it **Autism**
- `HP:0002719` (1 mention) - the report calls it "Variable"; HP calls it **Recurrent infections**
- `UBERON:0000970` (1 mention) - the report calls it "Secondary organ involvement:** eye"; UBERON calls it **eye**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001263` (1 mention) - the report calls it "Infancy/childhood"; HP calls it **Global developmental delay**, and lists "Developmental delay in early childhood" among its other names
- `HP:0001627` (1 mention) - the report calls it "Congenital"; HP calls it **Abnormal heart morphology**, and lists "Congenital heart defect" among its other names
- `GO:0007611` (1 mention) - the report calls it "learning/memory"; GO calls it **learning or memory**
- `GO:0046951` (1 mention) - the report calls it "ketone body biosynthesis"; GO calls it **ketone body biosynthetic process**, and lists "ketone body biosynthesis" among its other names
- `UBERON:0001017` (1 mention) - the report calls it "Primary organ/system:** central nervous system"; UBERON calls it **central nervous system**
- `GO:0014069` (1 mention) - the report calls it "Subcellular:** postsynaptic density/synapse"; GO calls it **postsynaptic density**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.