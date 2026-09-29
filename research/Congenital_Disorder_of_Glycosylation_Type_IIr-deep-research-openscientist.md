---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-22T16:58:06.093232'
end_time: '2026-09-22T17:44:01.738217'
duration_seconds: 2755.65
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Congenital Disorder of Glycosylation Type IIr
  mondo_id: MONDO:0026765
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
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 41
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 1
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: HP:0001397
    reported_labels:
    - Lab/imaging/clinical
    ontology_label: Hepatic steatosis
  - term_id: HP:0001399
    reported_labels:
    - Clinical sign
    ontology_label: Hepatic failure
  - term_id: HP:0001394
    reported_labels:
    - Clinical/pathology
    ontology_label: Cirrhosis
  - term_id: HP:0004313
    reported_labels:
    - Lab abnormality
    ontology_label: Decreased circulating immunoglobulin concentration
  - term_id: HP:0002719
    reported_labels:
    - Clinical
    ontology_label: Recurrent infections
  - term_id: HP:0000973
    reported_labels:
    - Physical manifestation
    ontology_label: Cutis laxa
  - term_id: HP:0001263
    reported_labels:
    - Behavioral/neuro
    ontology_label: Global developmental delay
  - term_id: HP:0001256
    reported_labels:
    - Behavioral
    ontology_label: Mild intellectual disability
  - term_id: HP:0001999
    reported_labels:
    - Physical
    ontology_label: Abnormal facial shape
  - term_id: HP:0001510
    reported_labels:
    - Clinical
    ontology_label: Growth delay
  - term_id: HP:0001903
    reported_labels:
    - Lab abnormality
    ontology_label: Anemia
  - term_id: HP:0001640
    reported_labels:
    - Clinical/imaging
    ontology_label: Cardiomegaly
  - term_id: UBERON:0002107
    reported_labels:
    - Liver
    - Primary organ:** **Liver
    ontology_label: liver
  labels_variant: 3
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
  path: Congenital_Disorder_of_Glycosylation_Type_IIr-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Disorder_of_Glycosylation_Type_IIr-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Disorder of Glycosylation Type IIr
- **MONDO ID:** MONDO:0026765 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Disorder of Glycosylation Type IIr** covering all of the
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

# Congenital Disorder of Glycosylation Type IIr (ATP6AP2-CDG / CDG2R)

**Target disease:** Congenital Disorder of Glycosylation, Type IIr
**MONDO:** MONDO:0026765 · **OMIM (phenotype):** 301045 · **Gene:** ATP6AP2
**Category:** Mendelian, X-linked recessive

> **IMPORTANT IDENTIFICATION NOTE.** The MONDO term MONDO:0026765 ("congenital disorder of glycosylation, type IIr", synonym **CDG2R**) is cross-referenced (MONDO:equivalentTo) to **OMIM 301045**, **MedGen C5393313 (UID 1717186)**, **GARD 0025491**, **UMLS C5393313**, and **DOID:0051048**. This is the **X-linked ATP6AP2-CDG** described by Rujano et al. 2017 (PMID 29127204). It is a **different disease** from CCDC115-CDG, which is CDG type **IIq** (OMIM 616828, autosomal recessive). This report covers ATP6AP2-CDG (the correct disease for MONDO:0026765). CCDC115-CDG and other V-ATPase-assembly CDGs (TMEM199-CDG/CDG-IIp, ATP6AP1-CDG, VMA21-CDG) are discussed only as differential/comparators.

---

## 1. Disease Information

**Overview.** ATP6AP2-CDG (CDG-IIr / CDG2R) is an ultra-rare, X-linked recessive multisystem congenital disorder of glycosylation caused by hypomorphic missense variants in *ATP6AP2*, which encodes an accessory subunit of the vacuolar-type H⁺-ATPase (V-ATPase), also known as the (pro)renin receptor. Affected males present in infancy with liver disease (hepatosteatosis progressing to cirrhosis/liver failure), immunodeficiency (hypogammaglobulinemia with recurrent infections), cutis laxa, and mild psychomotor/intellectual impairment, together with a combined N-/O-linked (Golgi/type 2) glycosylation defect.

**Key identifiers.**
- **MONDO:** MONDO:0026765
- **OMIM phenotype:** 301045 (CDG2R); **OMIM gene:** 300556 (ATP6AP2)
- **MedGen:** C5393313 / UID 1717186 · **GARD:** 0025491 · **UMLS:** C5393313 · **DOID:** 0051048
- **Orphanet:** Falls under the broad group "Congenital disorder of glycosylation" (ORPHA:137); a dedicated ATP6AP2-CDG ORPHA code is not consistently assigned (data not clearly available).
- **ICD-11:** 5C51.2 (Congenital disorders of glycosylation); **ICD-10:** E77.8. **MeSH:** Congenital Disorders of Glycosylation (D018981).

**Synonyms / alternative names:** ATP6AP2-CDG; CDG2R; CDG-IIr; Congenital disorder of glycosylation type 2R; ATP6AP2 congenital disorder of glycosylation; (in older literature grouped with "V-ATPase CDGs" and "autophagic liver disease").

**Data source type:** Disease-level knowledge aggregated from a small number of **individual patient case reports/series** (fewer than ~7 reported individuals with the CDG phenotype as of 2025), plus functional studies in cells and model organisms. No EHR/registry-scale data exist.

---

## 2. Etiology

**Primary cause — genetic.** Hemizygous (males) germline **loss-of-function/hypomorphic missense variants in *ATP6AP2*** (Xp11.4). The disease is monogenic and Mendelian; there is no environmental or infectious cause of the disorder itself (though the resulting immunodeficiency predisposes to infections — a *consequence*, not a cause).

**Genetic risk factors / causal variants (human clinical):**
- p.Arg71His (R71H) and p.Leu98Ser (L98S) — the two original missense variants (Rujano 2017, PMID 29127204).
- c.185G>A p.Gly62Glu (G62E) — third reported missense (Fang 2023, PMID 38075676).
- All lie in the **extracellular/luminal domain** of ATP6AP2; all are hypomorphic.

**Environmental risk factors:** None established. Being a monogenic X-linked disorder, the dominant "risk factor" is **male sex** (hemizygosity) and carrier-mother inheritance.

**Protective factors:** In females, the second (wild-type) *ATP6AP2* allele and X-inactivation generally protect heterozygous carriers (though a mildly affected female with a *splicing* variant has been reported — Raynor 2025, PMID 41131679). No dietary/environmental protective factors are known.

**Gene–environment interactions:** Not characterized. Because ATP6AP2 controls lysosomal acidification/autophagy and lipid handling, nutritional/metabolic state may modulate the steatotic phenotype (inferred from Drosophila lipid-metabolism findings, PMID 29127204), but this is not clinically demonstrated.

---

## 3. Phenotypes

Onset is **congenital/infantile**; the course is **severe and progressive**, dominated by liver disease. Frequencies are qualitative given the tiny cohort.

| Phenotype | Type | HPO term | Onset / severity / frequency |
|---|---|---|---|
| Hepatic steatosis / fatty liver | Lab/imaging/clinical | HP:0001397 | Infantile; consistent |
| Liver failure | Clinical sign | HP:0001399 | Infantile; severe; common |
| Cirrhosis | Clinical/pathology | HP:0001394 | Progressive |
| Elevated transaminases | Lab abnormality | HP:0002910 | Consistent |
| Jaundice / cholestasis | Clinical sign | HP:0000952 / HP:0001396 | Reported |
| Coagulopathy | Lab abnormality | HP:0001928 | Reported (Fang 2023) |
| Hypogammaglobulinemia | Lab abnormality | HP:0004313 | Common |
| Recurrent infections (immunodeficiency) | Clinical | HP:0002719 | Common |
| Cutis laxa | Physical manifestation | HP:0000973 | Characteristic |
| Global developmental delay / psychomotor impairment | Behavioral/neuro | HP:0001263 | Mild, variable |
| Intellectual disability, mild | Behavioral | HP:0001256 | Mild |
| Dysmorphic facial features | Physical | HP:0001999 | Some patients |
| Growth retardation | Clinical | HP:0001510 | Reported |
| Anemia | Lab abnormality | HP:0001903 | Reported |
| Cardiomegaly | Clinical/imaging | HP:0001640 | Reported (Fang 2023) |
| Abnormal transferrin glycosylation (type 2 pattern) | Lab biomarker | HP:0012345 (abnormal glycosylation) | Diagnostic hallmark |

**Quality-of-life impact:** Severe. Liver failure requiring transplantation, chronic immunodeficiency requiring immunoglobulin support, and developmental impairment substantially affect survival and daily functioning. Formal QoL instruments (EQ-5D/SF-36) have not been applied to this ultra-rare disease.

**Evidence quotes:** MedGen definition (per Rujano 2017): *"an X-linked recessive disorder characterized by infantile onset of liver failure, recurrent infections due to hypogammaglobulinemia, and cutis laxa. Some patients may also have mild intellectual impairment and dysmorphic features. Laboratory studies showed defective glycosylation of serum transferrin in a type 2 pattern."*

---

## 4. Genetic / Molecular Information

- **Causal gene:** *ATP6AP2* (ATPase H⁺ transporting accessory protein 2; a.k.a. (pro)renin receptor, PRR, ATP6IP2). **HGNC:18305**, **NCBI Gene 10159**, **Ensembl ENSG00000182220**, gene **OMIM 300556**, cytoband **Xp11.4** (GRCh37 chrX:40,440,146–40,465,889). RefSeq NM_005765. **UniProt O75787**.
- **Pathogenic variants (all germline, hemizygous, missense):**
  - p.Arg71His (R71H) — Rujano 2017 (PMID 29127204)
  - p.Leu98Ser (L98S) — Rujano 2017 (PMID 29127204)
  - c.185G>A p.Gly62Glu (G62E) — Fang 2023 (PMID 38075676)
  - All in the **luminal/extracellular domain**; **loss-of-function/hypomorphic** consequence.
- **Variant classification (ACMG/AMP):** the recurrent CDG missense variants are reported pathogenic/likely pathogenic in the primary literature; most other *ATP6AP2* variants in ClinVar are VUS or relate to the neurological allelic disorders.
- **Allele frequency:** Effectively absent from population databases (gnomAD) — consistent with a severe, ultra-rare X-linked disease.
- **Somatic vs germline:** Germline only.
- **Allelic disorders (same gene, different variant class/phenotype):**
  - *ATP6AP2* **splicing** variants → X-linked intellectual disability (Hedera type) and X-linked parkinsonism with spasticity (OMIM 300423 / 300911), acting via **exon-4 skipping (Δe4) and ~50% reduced full-length protein** (Edelman 2022, PMID 35779466; Raynor 2025, PMID 41131679).
- **Modifier genes:** None identified. **Epigenetic changes:** X-inactivation determines expression in carrier females; no disease-specific methylation signature reported. **Chromosomal abnormalities:** Not applicable (point mutations); the locus is Xp11.4.

**Quote (Raynor 2025, PMID 41131679):** *"ATP6AP2 missense variants lead to hepatopathy, immunological abnormalities, cutis laxa and only mild intellectual disability with N-/O-glycosylation defects (ATP6AP2-CDG; OMIM#301045)."*

---

## 5. Environmental Information

Not applicable as a cause. No toxins, radiation, lifestyle, or infectious agents cause ATP6AP2-CDG. Infections occur **secondary** to the intrinsic humoral immunodeficiency (hypogammaglobulinemia). CHEBI-relevant chemical entities implicated downstream include cholesterol (CHEBI:16113) and triglycerides/lipids accumulating in liver.

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A hemizygous **hypomorphic missense variant in the *ATP6AP2* extracellular/luminal domain** (R71H, L98S, G62E) **reduces functional ATP6AP2**, an ER-localized accessory subunit of the V-ATPase.
2. → **Impairs assembly/biogenesis of the V-ATPase proton pore (V0 sector) in the endoplasmic reticulum** (ATP6AP2 interacts with V0-assembly components; its ER localization is crucial for V-ATPase activity).
3. → **Reduces V-ATPase-dependent acidification of the endolysosomal system and Golgi.**
4. Branch **A (glycosylation):** abnormal Golgi luminal pH → **dysfunctional/mislocalized glycosyltransferases** → **combined N-/O-linked hypoglycosylation** (serum transferrin type 2 pattern) → cutis laxa (defective ELN/elastic-fiber glycoprotein processing, inferred) and multisystem glycoprotein dysfunction, including **hypogammaglobulinemia/immunodeficiency**.
5. Branch **B (autophagy/metabolism):** defective **lysosomal acidification** → **reduced mTOR signaling** and **dysregulated (impaired) autophagy** → failure of hepatic lipid turnover/lipophagy → **hepatosteatosis** → hepatocyte injury, **fibrosis, cirrhosis, and liver failure**; altered lipid metabolism (demonstrated in Drosophila fat body and by metabolomics in cell models).
6. → Clinical convergence: **infantile liver failure, immunodeficiency, cutis laxa, mild psychomotor/intellectual impairment.**

*Demonstrated vs inferred:* Steps 1–3 and 5 are experimentally supported (mouse liver, Drosophila fat body, patient cells). The precise Golgi glycosyltransferase step (4) is inferred by analogy to other V-ATPase/Golgi-pH CDGs; cutis-laxa causation is mechanistically inferred.

**Molecular pathways:** V-ATPase-dependent organelle acidification; **mTOR (MTORC1) signaling** (KEGG hsa04150); **macroautophagy/lysosomal degradation** (KEGG hsa04140); lipid metabolism. **Cellular processes / GO:** vacuolar acidification (GO:0007035), regulation of macroautophagy (GO:0016241), TORC1 signaling (GO:0038202), protein N-/O-glycosylation (GO:0006487 / GO:0006493), lysosomal lumen acidification (GO:0007042). **Protein dysfunction:** hypomorphic loss of function of an assembly accessory subunit (not aggregation). **Immune involvement:** humoral immunodeficiency (hypogammaglobulinemia). **Tissue damage:** hepatic steatosis → steatohepatitis-like injury → fibrosis/cirrhosis.

**Molecular profiling:** Untargeted metabolomics of G62E-expressing cells showed downregulation of lipid-metabolism metabolites (Fang 2023, PMID 38075676). Serum glycoproteomics: hypoglycosylated transferrin (type 2 CDG pattern) and abnormal apolipoprotein/O-glycan markers.

**Quote (Cannata Serio 2018, PMID 29388887):** *"these phenotypes are the result of a pathogenetic cascade that includes impaired V-ATPase assembly, defective lysosomal acidification, reduced MTOR signaling and autophagic misregulation."*

**Cell types (CL) / compartments (GO CC):** hepatocyte (CL:0000182), B cell / plasma cell (CL:0000236 / CL:0000786), fibroblast (CL:0000057); endoplasmic reticulum (GO:0005783), lysosome (GO:0005764), Golgi apparatus (GO:0005794), vacuolar proton-transporting V-ATPase complex (GO:0016471).

---

## 7. Anatomical Structures Affected

- **Primary organ:** **Liver** (UBERON:0002107) — steatosis, cirrhosis, failure.
- **Secondary/other systems:** **Immune system** (UBERON:0002405; hypogammaglobulinemia), **skin/connective tissue** (UBERON:0002097; cutis laxa), **central nervous system/brain** (UBERON:0000955; mild developmental/intellectual impairment), and occasionally **heart** (UBERON:0000948; cardiomegaly).
- **Body systems:** digestive/hepatobiliary, immune, integumentary/connective, nervous, (cardiovascular).
- **Tissue/cell level:** hepatic parenchyma (hepatocytes), antibody-producing B/plasma cells, dermal elastic connective tissue/fibroblasts.
- **Subcellular:** ER, lysosome, Golgi (V-ATPase complex) — see GO terms above.
- **Localization/lateralization:** systemic/bilateral (not lateralized).

---

## 8. Temporal Development

- **Onset:** Congenital defect; clinically **infantile** (liver disease often within the first months to first year of life; e.g., presentation at 11 months in Fang 2023).
- **Onset pattern:** subacute–chronic hepatic deterioration; recurrent infections from infancy.
- **Progression:** progressive hepatic disease (steatosis → cirrhosis → failure); developmental impairment relatively stable/mild.
- **Duration:** chronic, lifelong; potentially life-limiting without liver transplantation.
- **Critical period / intervention window:** early infancy — timely diagnosis enables immunoglobulin replacement and consideration of liver transplantation before decompensation.

---

## 9. Inheritance and Population

- **Inheritance:** **X-linked recessive.** Affected individuals are almost exclusively **hemizygous males**; heterozygous females are usually unaffected (a mildly affected female with a *splicing* variant is reported, PMID 41131679).
- **Penetrance:** high/complete in hemizygous males for reported pathogenic missense; **expressivity variable** (hepatic severity and neuro-involvement differ).
- **Epidemiology:** **Ultra-rare.** Only a handful of CDG-phenotype patients reported worldwide (≈3 males in the original two families plus subsequent individual case reports). Prevalence/incidence are not quantifiable (<< 1/1,000,000); no registry data.
- **Carrier frequency:** Not established; variants essentially absent from gnomAD.
- **Founder effect / consanguinity:** None reported (X-linked, transmitted through carrier mothers).
- **Sex ratio:** Strongly male-predominant (X-linked recessive).
- **Geographic distribution:** Reported cases from Europe (Germany/Portugal) and China — no geographic clustering; reflects sporadic ascertainment.

---

## 10. Diagnostics

- **First-line biomarker:** **Serum transferrin isoform analysis** (isoelectric focusing or capillary electrophoresis / mass spectrometry) showing a **CDG type 2 pattern** (loss of sialic acid/galactose from a Golgi defect). Combined with **abnormal O-glycosylation** markers (e.g., apolipoprotein C-III).
- **Laboratory tests:** elevated aminotransferases (ALT/AST), cholestatic markers/bilirubin, **low serum immunoglobulins (IgG)**, coagulopathy (reduced clotting factors), hypercholesterolemia/dyslipidemia, anemia.
- **Imaging:** hepatic ultrasound/MRI showing steatosis/hepatomegaly/cirrhosis; echocardiography if cardiomegaly.
- **Histopathology (liver biopsy):** steatosis, fibrosis/cirrhosis, autophagic/lysosomal abnormalities; immunohistochemistry for ATP6AP2.
- **Genetic testing (definitive):** **WES/WGS** or targeted **CDG/hepatopathy gene panels** including *ATP6AP2*; single-gene sequencing confirms hemizygous missense. **RNA-seq of patient fibroblasts** is valuable to characterize splicing variants (relevant for the allelic neurological disorders). CMA/karyotype/FISH not indicated for point mutations.
- **Functional confirmation:** demonstration of hypoglycosylation and, in research settings, V-ATPase/lysosomal-acidification and mTOR/autophagy assays; complementation studies.
- **Differential diagnosis:** **Wilson disease**, mitochondrial hepatopathies, Niemann-Pick C, other **V-ATPase-assembly CDGs** (ATP6AP1-CDG, TMEM199-CDG/CDG-IIp, CCDC115-CDG/CDG-IIq, VMA21-CDG), ARC syndrome and other cutis-laxa CDGs (ATP6V0A2-CDG), and primary immunodeficiencies with liver disease. Distinguishing feature: X-linked inheritance + CDG type 2 transferrin + the triad liver/immune/cutis laxa.
- **Screening:** No newborn-screening test (CDG type 2 is not captured by standard NBS). **Carrier testing** for at-risk female relatives and **cascade/prenatal testing** once the familial variant is known.

---

## 11. Outcome / Prognosis

- **Severity/mortality:** Serious; **liver failure is the principal life-threatening complication.** Death from hepatic failure has occurred in related V-ATPase CDGs; ATP6AP2-CDG patients have required **liver transplantation** (e.g., Fang 2023).
- **Life expectancy:** Reduced without treatment; can be extended by transplantation and immunoglobulin support. Precise survival statistics are unavailable (too few patients).
- **Morbidity/disability:** chronic liver disease, recurrent infections, developmental/intellectual impairment, connective-tissue (cutis laxa) manifestations.
- **Complications:** cirrhosis, portal hypertension, coagulopathy, infections, growth failure, cardiomegaly.
- **Recovery potential:** Liver transplantation addresses the hepatic phenotype but **does not correct the systemic glycosylation defect, immunodeficiency, or neurodevelopmental features.**
- **Prognostic factors:** age at diagnosis, hepatic reserve at presentation, timeliness of transplant, severity of immunodeficiency. **Prognostic biomarker:** degree of transferrin hypoglycosylation and hepatic synthetic function (albumin/coagulation).

---

## 12. Treatment

**No disease-specific/curative pharmacotherapy exists.** Management is **supportive and organ-directed** (NCIT: Supportive Care, C15277):

- **Hepatic:** management of chronic liver disease and, for end-stage disease, **orthotopic liver transplantation** (NCIT: Liver Transplantation, C15311) — performed in reported patients.
- **Immunologic:** **immunoglobulin (IgG) replacement therapy** (IVIG/SCIG) and infection prophylaxis/prompt treatment for hypogammaglobulinemia (NCIT: Immunoglobulin Therapy, C158353; Intravenous Immunoglobulin Therapy).
- **Nutritional/metabolic:** management of coagulopathy (vitamin K, factor support), dyslipidemia, and growth/nutrition.
- **Neurodevelopmental:** early intervention, physical/occupational/speech therapy for developmental delay.
- **Cardiac/other:** monitoring and symptomatic management as needed.

**Pharmacogenomics:** Not established. **Advanced therapeutics (gene/cell/RNA therapy, targeted therapy):** none approved or in trials; **no ClinicalTrials.gov entries specific to ATP6AP2-CDG** (as of 2025). Given the mechanism, mTOR/autophagy modulation is a conceptual research target (not clinically validated). **Treatment response/adverse events:** limited to individual case experience; transplantation carries standard surgical/immunosuppression risks.

---

## 13. Prevention

- **Primary prevention:** Not possible for a monogenic disorder; **genetic counseling** for carrier families (X-linked recurrence risk: carrier mother → 50% of sons affected, 50% of daughters carriers).
- **Secondary prevention:** early diagnosis via CDG screening in infants with unexplained liver disease + immunodeficiency + cutis laxa; **cascade genetic testing** of relatives.
- **Reproductive options:** **prenatal diagnosis** and **preimplantation genetic testing (PGT-M)** once the familial *ATP6AP2* variant is known; carrier testing of at-risk females.
- **Tertiary prevention:** immunoglobulin replacement to prevent infections; hepatology surveillance to time transplantation; developmental support.
- **Immunization / public-health / environmental measures:** standard vaccinations as tolerated within immunodeficiency management; no population-level or environmental prevention applies.

---

## 14. Other Species / Natural Disease

- **Orthologs (comparative/experimental, not natural disease):** mouse *Atp6ap2* (**NCBI Gene 70495**; NCBI Taxon 10090), rat *Atp6ap2*, zebrafish *atp6ap2*, *Drosophila melanogaster* ortholog (VhaPRR; Taxon 7227). ATP6AP2/V-ATPase function is **highly evolutionarily conserved** (yeast to human).
- **Natural disease in other species:** **None reported.** No naturally occurring ATP6AP2-CDG in companion animals/wildlife (OMIA: not listed). No breed-specific (VBO) associations.
- **Zoonotic potential / transmission:** Not applicable (genetic disease).

---

## 15. Model Organisms

- **Mouse (mammalian):** Liver-directed **Atp6ap2 deficiency** causes **hypoglycosylation of serum proteins and autophagy defects**, recapitulating hepatic/glycosylation features (Rujano 2017, PMID 29127204). *Atp6ap2* is essential; complete knockout is lethal, so conditional/tissue-specific approaches are used. Resource: MGI.
- ***Drosophila* (invertebrate):** Introduction of a human missense mutation caused **reduced survival and altered lipid metabolism**, with **defective lysosomal acidification and reduced mTOR signaling** and autophagic dysregulation in the liver-like **fat body** (PMID 29127204). Resource: FlyBase.
- **Cell / in vitro models:** **HEK293T** cells expressing p.Gly62Glu show dysregulated autophagy/mTOR and altered lipid metabolites (Fang 2023, PMID 38075676); **patient fibroblasts** (glycosylation + splicing/RNA-seq studies); **iPSC-derived neural progenitor cells** used for allelic splicing variants (Edelman 2022, PMID 35779466).
- **Phenotype recapitulation:** Models reproduce the **glycosylation, lysosomal-acidification, mTOR/autophagy, and lipid/steatosis** phenotypes well. **Limitations:** they incompletely capture the **immunodeficiency** and **cutis laxa** components of the human disease.

---

## Evidence Summary (Key PMIDs)

| PMID | Type | Contribution |
|---|---|---|
| 29127204 (Rujano 2017, *J Exp Med*) | Human + mouse + Drosophila | Landmark: identifies *ATP6AP2* missense (R71H, L98S) as cause; defines phenotype and mechanism |
| 29388887 (Cannata Serio 2018, *Autophagy*) | Review/commentary | Summarizes pathogenetic cascade (V-ATPase assembly → lysosomal acidification → mTOR → autophagy) |
| 38075676 (Fang 2023, *Front Genet*) | Human case + cell model | New variant G62E; liver transplant; metabolomics of lipid pathway |
| 41131679 (Raynor 2025) | Human | Missense-vs-splicing genotype–phenotype; first affected female; glycosylation in splicing variants |
| 35779466 (Edelman 2022) | Human + iPSC | Reduced-gene-dosage (Δe4) mechanism for splicing/neurological allelic disorders |

**Evidence-source classification:** predominantly **human clinical case reports** supported by **model-organism (mouse, Drosophila)** and **in vitro/cellular** functional studies; no computational-only claims relied upon.

---

## Limitations and Future Directions

- **Ultra-rare disease:** conclusions rest on <~7 CDG-phenotype patients; frequencies, prevalence, penetrance nuances, and survival statistics are imprecise.
- **Ontology/registry gaps:** a dedicated Orphanet code and standardized HPO-frequency annotations are limited.
- **Mechanistic gaps:** the exact link from V-ATPase/pH defect to cutis laxa and to B-cell/immunoglobulin failure is inferred, not fully proven; the puzzle of why missense→hepatic/immune while splicing→neurological remains open.
- **Therapeutics:** no targeted therapy; mTOR/autophagy modulation and gene-directed approaches are unexplored research avenues.


## Artifacts

- [OpenScientist final report](Congenital_Disorder_of_Glycosylation_Type_IIr-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Disorder_of_Glycosylation_Type_IIr-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 17 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001397` (1 mention) - the report calls it "Lab/imaging/clinical"; HP calls it **Hepatic steatosis**
- `HP:0001399` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hepatic failure**
- `HP:0001394` (1 mention) - the report calls it "Clinical/pathology"; HP calls it **Cirrhosis**
- `HP:0004313` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Decreased circulating immunoglobulin concentration**
- `HP:0002719` (1 mention) - the report calls it "Clinical"; HP calls it **Recurrent infections**
- `HP:0000973` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Cutis laxa**
- `HP:0001263` (1 mention) - the report calls it "Behavioral/neuro"; HP calls it **Global developmental delay**
- `HP:0001256` (1 mention) - the report calls it "Behavioral"; HP calls it **Mild intellectual disability**
- `HP:0001999` (1 mention) - the report calls it "Physical"; HP calls it **Abnormal facial shape**
- `HP:0001510` (1 mention) - the report calls it "Clinical"; HP calls it **Growth delay**
- `HP:0001903` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Anemia**
- `HP:0001640` (1 mention) - the report calls it "Clinical/imaging"; HP calls it **Cardiomegaly**
- `UBERON:0002107` (1 mention) - the report calls it "Liver", "Primary organ:** **Liver"; UBERON calls it **liver**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0026765` (4 mentions) - the report calls it "congenital disorder of glycosylation, type IIr", synonym **CDG2R"; MONDO calls it **congenital disorder of glycosylation, type IIr**
- `HP:0002910` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Elevated circulating hepatic transaminase concentration**, and lists "Abnormal liver enzymes" among its other names
- `HP:0001928` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Abnormality of coagulation**, and lists "Coagulation abnormality" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002107` - called "Liver", "Primary organ:** **Liver"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.