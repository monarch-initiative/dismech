---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T20:37:56.266812'
end_time: '2026-09-29T20:53:14.174860'
duration_seconds: 917.91
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: STT3A-Congenital Disorder of Glycosylation
  mondo_id: MONDO:0014270
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
citation_count: 15
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 31
  quotes_valid: 31
  relevance_assessed: 16
  on_topic: 9
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 25
  verified: 23
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 4
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: MONDO:0014270
    reported_labels:
    - MONDO
    ontology_label: STT3A-congenital disorder of glycosylation
  - term_id: HP:0001250
    reported_labels:
    - Clinical sign
    - Seizure
    ontology_label: Seizure
  - term_id: HP:0001249
    reported_labels:
    - Behavioral/cognitive
    - Intellectual disability
    ontology_label: Intellectual disability
  - term_id: HP:0001263
    reported_labels:
    - Clinical sign
    - Global developmental delay
    ontology_label: Global developmental delay
  - term_id: HP:0001252
    reported_labels:
    - Clinical sign
    - Hypotonia
    ontology_label: Hypotonia
  - term_id: HP:0001508
    reported_labels:
    - Clinical sign
    - Failure to thrive
    ontology_label: Failure to thrive
  - term_id: HP:0004322
    reported_labels:
    - Physical
    - Short stature
    ontology_label: Short stature
  - term_id: HP:0000256
    reported_labels:
    - Physical
    - Macrocephaly
    ontology_label: Macrocephaly
  - term_id: HP:0000924
    reported_labels:
    - Physical
    - Abnormal skeletal morphology
    ontology_label: Abnormality of the skeletal system
  - term_id: HP:0001276
    reported_labels:
    - Clinical sign
    - Hypertonia
    ontology_label: Hypertonia
  - term_id: HP:0001999
    reported_labels:
    - Physical
    ontology_label: Abnormal facial shape
  - term_id: HP:0003125
    reported_labels:
    - Laboratory
    - Factor VIII deficiency
    ontology_label: Reduced factor VIII activity
  - term_id: CHEBI:23509
    reported_labels:
    - Dolichol
    ontology_label: cysteine derivative
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0018279
    ontology_label: obsolete protein N-linked glycosylation via asparagine
    replaced_by: GO:0006487
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: STT3A-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: STT3A-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** STT3A-Congenital Disorder of Glycosylation
- **MONDO ID:** MONDO:0014270 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **STT3A-Congenital Disorder of Glycosylation** covering all of the
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

# STT3A-Congenital Disorder of Glycosylation (STT3A-CDG): Comprehensive Disease Characterization Report

**Disease:** STT3A-Congenital Disorder of Glycosylation (CDG type Iw)
**MONDO ID:** MONDO:0014270
**OMIM:** #615596 (autosomal recessive) and #619714 (autosomal dominant)
**Gene:** *STT3A* (HGNC:30591; NCBI Gene 3703; chr11q24.1; UniProt P46977; OMIM *601134)
**Category:** Mendelian inborn error of metabolism

---

## Summary

STT3A-CDG is an ultra-rare, multisystem inborn error of protein N-glycosylation caused by pathogenic variants in *STT3A*, the gene encoding the catalytic subunit of the co-translational oligosaccharyltransferase complex (OST-A). The OST-A complex, positioned adjacent to the Sec61 translocon in the endoplasmic reticulum (ER) membrane, transfers a pre-assembled Glc₃Man₉GlcNAc₂ oligosaccharide from a dolichol-pyrophosphate donor onto asparagine residues within N-X-S/T sequons of nascent polypeptides as they emerge into the ER. When OST-A activity is reduced, a subset of glycoproteins — particularly those whose sequons are glycosylated preferentially by STT3A during translation — become hypoglycosylated and destabilized, producing a **CDG type I** biochemical signature (an abnormal serum transferrin pattern with increased di- and a-sialotransferrin).

Clinically, STT3A-CDG is a predominantly neurodevelopmental and neuromuscular-skeletal disorder. The autosomal recessive form (first described in 2013) features seizures, developmental delay, intellectual disability, hypotonia, feeding problems/failure to thrive, and a type I transferrin pattern; some patients also have a coagulopathy (low Factor VIII and von Willebrand Factor). A distinct autosomal dominant form (defined in 2021 from 16 individuals across 9 families) is caused by heterozygous missense variants clustering in the catalytic active site and presents with skeletal anomalies, short stature, macrocephaly, dysmorphism, increased muscle tone/cramps, and intellectual disability in about half of cases. The two inheritance mechanisms — biallelic loss-of-function versus heterozygous dominant-negative active-site variants — represent one of the more unusual features of this disorder, reflected in dual OMIM entries.

Diagnosis rests on transferrin isoelectric focusing (or HPLC/capillary electrophoresis) followed by confirmatory exome/genome or targeted *STT3A* sequencing. There is no disease-specific or curative therapy; unlike certain treatable CDG subtypes (PGM1-CDG with galactose, MPI-CDG with mannose, TMEM165-CDG with galactose), the dietary sugar therapies do not apply to STT3A-CDG because it is an ER glycan-transfer defect rather than a Golgi processing defect. Management is supportive and multidisciplinary. Disease mechanism has been validated across yeast (*S. cerevisiae* STT3), zebrafish (CRISPR heterozygous knockdown), and human patient cell models, and gnomAD population-constraint metrics quantitatively corroborate that *STT3A* is strongly intolerant to both missense and loss-of-function variation.

---

## Key Findings

### Finding 1 — STT3A-CDG is caused by defects in the catalytic subunit of the OST-A complex

*STT3A* (chromosome 11q24.1; OMIM *601134) encodes the catalytic subunit of the STT3A-containing oligosaccharyltransferase (OST-A) complex, which co-translationally transfers the Glc₃Man₉GlcNAc₂ glycan from dolichol-pyrophosphate onto asparagine residues within N-X-S/T sequons. The original 2013 report by Shrimal, Ng, Losfeld, Gilmore, and Freeze identified a homozygous *STT3A* c.1877T>C variant (p.Val626Ala) causing a recessive CDG; the mutation impaired glycosylation of a GFP-based biomarker and was rescued by wild-type cDNA.

> "which are caused by mutations in different isoforms of the catalytic subunit of the oligosaccharyltransferase (OST)" — [PMID: 23842455](https://pubmed.ncbi.nlm.nih.gov/23842455/)

> "A homozygous mutation (c.1877T > C) in STT3A causes a p.Val626Ala change" — [PMID: 23842455](https://pubmed.ncbi.nlm.nih.gov/23842455/)

> "STT3A encodes the catalytic subunit of the STT3A-containing oligosaccharyltransferase (OST) complex, essential for protein N-glycosylation" — [PMID: 34653363](https://pubmed.ncbi.nlm.nih.gov/34653363/)

This establishes the fundamental molecular lesion: a defect in the enzyme that initiates the N-glycosylation of nascent proteins in the ER.

### Finding 2 — STT3A-CDG has both autosomal recessive and autosomal dominant forms

The recessive form (OMIM #615596, CDG-Iw) was first described in 2013 as an autosomal-recessive disorder with seizures, developmental delay, intellectual disability, and a type I transferrin pattern. In 2021, Wilson et al. reported 16 individuals from 9 families with inherited or de novo heterozygous missense variants clustering in the STT3A catalytic active site, defining a distinct autosomal-dominant CDG (OMIM #619714). Subsequent reports (2024–2026) confirmed and expanded the dominant spectrum, including a zebrafish-validated dominant missense variant (p.Asp167Tyr).

> "we here report the identification of 16 individuals from nine families who have either inherited or de novo heterozygous missense variants in STT3A, leading to an autosomal-dominant CDG" — [PMID: 34653363](https://pubmed.ncbi.nlm.nih.gov/34653363/)

> "all variants are located in the catalytic site of STT3A" — [PMID: 34653363](https://pubmed.ncbi.nlm.nih.gov/34653363/)

> "Previous studies have reported that STT3A-CDG is caused by autosomal recessive inheritance. However, in this study, we propose that STT3A-CDG can be pathogenic through autosomal dominant inheritance" — [PMID: 39891251](https://pubmed.ncbi.nlm.nih.gov/39891251/)

The clustering of dominant variants in the catalytic site supports a **dominant-negative** mechanism, whereby a mutant catalytic subunit incorporated into the OST-A complex poisons its activity.

### Finding 3 — Core clinical phenotype: neurodevelopmental impairment, seizures, and a type I transferrin pattern

Recessive STT3A-CDG is characterized by seizures, developmental delay, intellectual disability, hypotonia, failure to thrive/feeding problems, and a type I carbohydrate-deficient transferrin (CDT) pattern. A patient carrying p.Tyr360Ser additionally exhibited chronically low Factor VIII and von Willebrand Factor with hypoglycosylated vWF. The dominant form presents with variable skeletal anomalies, short stature, macrocephaly, dysmorphic features, intellectual disability in approximately 50%, and increased muscle tone with muscle cramps.

> "characterized by seizures, developmental delay, intellectual disability, and a type I carbohydrate deficient transferrin pattern" — [PMID: 30701557](https://pubmed.ncbi.nlm.nih.gov/30701557/)

> "chronically low Factor VIII (FVIII) and von Willebrand Factor (vWF) levels and activities" — [PMID: 30701557](https://pubmed.ncbi.nlm.nih.gov/30701557/)

> "Affected individuals presented with variable skeletal anomalies, short stature, macrocephaly, and dysmorphic features; half had intellectual disability. Additional features included increased muscle tone and muscle cramps" — [PMID: 34653363](https://pubmed.ncbi.nlm.nih.gov/34653363/)

### Finding 4 — Mechanism: STT3A mediates co-translational N-glycosylation coupled to the ER translocon

The STT3A OST complex is localized adjacent to the Sec61 protein translocation channel and catalyzes co-translational N-glycosylation using an N-terminal-to-C-terminal scanning mechanism. Accessory subunits DC2 (OSTC) and KCP2 mediate the STT3A–translocon interaction. The paralogous STT3B complex (containing the oxidoreductase MagT1) glycosylates sites skipped by STT3A, including cysteine-proximal sequons, providing partial functional redundancy that likely mitigates the severity of STT3A loss.

> "The STT3A complex interacts directly with the protein translocation channel to mediate glycosylation of proteins using an N-terminal-to-C-terminal scanning mechanism" — [PMID: 31433728](https://pubmed.ncbi.nlm.nih.gov/31433728/)

> "the STT3A isoform of the oligosaccharyltransferase is localized adjacent to the protein translocation channel to catalyze co-translational N-linked glycosylation of proteins in the endoplasmic reticulum" — [PMID: 28860277](https://pubmed.ncbi.nlm.nih.gov/28860277/)

> "the role of the STT3B complex in mediating cotranslational or posttranslocational glycosylation of acceptor sites that have been skipped by the STT3A complex" — [PMID: 25460543](https://pubmed.ncbi.nlm.nih.gov/25460543/)

### Finding 5 — Ultra-rare with two OMIM entries; part of the broader CDG group

Two OMIM phenotype entries exist: CDG type Iw autosomal recessive (#615596) and autosomal dominant (#619714). Only ~6 recessive cases were reported by 2019 (all p.Val626Ala except one p.Tyr360Ser); the dominant cohort added 16 individuals from 9 families in 2021, with further single/small reports since. No formal prevalence or incidence estimate exists for STT3A-CDG specifically. For context, CDG comprise ~200 disorders, of which PMM2-CDG is by far the most common (~60% of all CDG; incidence ~1 in 33,576 in North America/Europe).

> "Autosomal dominant congenital disorder of glycosylation (CDG) type Iw (OMIM# 619714)" — [PMID: 39435313](https://pubmed.ncbi.nlm.nih.gov/39435313/)

> "STT3A-CDG (OMIM# 615596) is an autosomal recessive N-linked glycosylation disorder" — [PMID: 30701557](https://pubmed.ncbi.nlm.nih.gov/30701557/)

> "Phosphomannomutase 2-congenital disorder of glycosylation (PMM2-CDG) accounts for about 60 % of all CDGs" — [PMID: 40737785](https://pubmed.ncbi.nlm.nih.gov/40737785/)

### Finding 6 — CDG natural history: multisystem disease with early-childhood mortality risk

In a Frontiers in CDG Consortium (FCDGC) natural-history cohort of 37 deceased CDG patients, all presented with multisystem features including neurological involvement; the majority died within the first three years of life, and about one-third died of cardiopulmonary failure (others from neurological progression, sepsis, or respiratory infection). CDG frequently cause coagulation abnormalities (antithrombin, protein C, factor XI deficiencies) with both bleeding and thrombosis risk. CDG prevalence in childhood epilepsy cohorts is notable (~4.4%), and transferrin isoelectric focusing is a recommended screen.

> "The majority of patients involved in this study died during the first three years of life" — [PMID: 39923392](https://pubmed.ncbi.nlm.nih.gov/39923392/)

> "All of the patients presented with multisystem features with involvement of the neurological system" — [PMID: 39923392](https://pubmed.ncbi.nlm.nih.gov/39923392/)

These mortality data are drawn from the broader CDG group; STT3A-CDG-specific mortality figures are not established.

### Finding 7 — Functional models recapitulate the glycosylation defect

In *S. cerevisiae*, expressing STT3 carrying variants homologous to patient alleles induced defective glycosylation of carboxypeptidase Y in a wild-type strain and worsened the defect in the hypomorphic *stt3-7* strain, supporting a dominant pathomechanism. CRISPR-Cas9 heterozygous-knockdown zebrafish modeling p.Asp167Tyr reproduced patient-like phenotypes: craniofacial dysmorphology (increased eye distance, altered ceratohyal angle), reduced mineralized bone, and abnormal locomotion/developmental delay. Patient fibroblasts and HeLa/HEK293T systems show hypoglycosylation of STT3A-specific reporters that is rescued by wild-type *STT3A* cDNA.

> "expression of STT3 containing variants homologous to those in affected individuals induced defective glycosylation of carboxypeptidase Y in a wild-type yeast strain" — [PMID: 34653363](https://pubmed.ncbi.nlm.nih.gov/34653363/)

> "Heterozygous knockdown zebrafish exhibit phenotypes similar to those of patients, including craniofacial dysmorphology" — [PMID: 39891251](https://pubmed.ncbi.nlm.nih.gov/39891251/)

### Finding 8 — Downstream consequence: selective hypoglycosylation and destabilization of specific glycoproteins

Selective exo-enzymatic labeling of STT3A/STT3B-deficient cells showed reduced cell-surface abundance of the insulin receptor and IGF-1 receptor (IGF-1R) when N-glycosylation was selectively impaired, linking OST subunit loss to defective receptor tyrosine kinase processing — a plausible molecular driver of the growth and skeletal phenotypes. Clinically, an STT3A-CDG patient exhibited hypoglycosylated von Willebrand Factor and undetectable Factor VIII, demonstrating that hypoglycosylation of specific STT3A-dependent substrates produces measurable protein deficiencies.

> "We show reduced abundance of two canonical tyrosine receptor kinases - the insulin receptor and insulin-like growth factor 1 receptor (IGF-1R) - at the cell surface" — [PMID: 31101650](https://pubmed.ncbi.nlm.nih.gov/31101650/)

> "VWF in our patient's plasma is present in a mildly hypoglycosylated form" — [PMID: 30701557](https://pubmed.ncbi.nlm.nih.gov/30701557/)

### Finding 9 — Diagnosis by type I transferrin screen followed by molecular sequencing; no dietary therapy available

STT3A-CDG produces a CDG type I serum transferrin pattern (loss of whole N-glycans → increased di-/a-sialotransferrin) detectable by transferrin isoelectric focusing (TIEF), HPLC, or capillary electrophoresis; confirmation requires exome/genome or targeted *STT3A* sequencing. Because STT3A-CDG is an ER assembly/transfer (CDG-I) defect rather than a Golgi galactosylation defect, dietary therapies effective in specific CDG types (PGM1-CDG galactose; MPI-CDG mannose; TMEM165-CDG galactose) are not applicable; no disease-specific or curative therapy exists, and management is supportive/multidisciplinary.

> "a type I carbohydrate deficient transferrin pattern" — [PMID: 30701557](https://pubmed.ncbi.nlm.nih.gov/30701557/)

> "Additional cases of STT3B-CDG may be missed by transferrin analysis and will require exome or genome sequencing" — [PMID: 23842455](https://pubmed.ncbi.nlm.nih.gov/23842455/)

> "There are >100 CDGs, but only specific types are treatable" — [PMID: 28323990](https://pubmed.ncbi.nlm.nih.gov/28323990/)

### Finding 10 — Ontology and inheritance annotations

Comprehensive ontology anchors are provided in the annotation tables below (Section 7 and the Ontology Appendix). The gene product identity and musculoskeletal features are supported by:

> "STT3A encodes the catalytic subunit of the STT3A-containing oligosaccharyltransferase (OST) complex, essential for protein N-glycosylation" — [PMID: 34653363](https://pubmed.ncbi.nlm.nih.gov/34653363/)

> "variable skeletal anomalies, short stature, macrocephaly, and dysmorphic features" — [PMID: 34653363](https://pubmed.ncbi.nlm.nih.gov/34653363/)

### Finding 11 — gnomAD constraint metrics confirm strong missense and LOF intolerance

gnomAD (GRCh38; gene ENSG00000134910; chr11:125,591,712–125,625,215) constraint for *STT3A*: **pLI = 0.894**, **LOEUF (oe_lof_upper) = 0.508**, observed/expected LoF = 0.381 (90% CI 0.290–0.508), **missense Z = 4.78** (oe_mis = 0.624), synonymous Z = 0.96. The high pLI (~0.9) and low LOEUF indicate intolerance to loss-of-function; the very high missense Z-score (>3.09 threshold) indicates strong selection against missense changes. This population-genetic evidence independently corroborates both disease mechanisms — LOF intolerance underpins the recessive (biallelic loss) form, and severe missense constraint is consistent with the dominant active-site missense variants being deleterious.

---

## Section-by-Section Report

### 1. Disease Information

STT3A-CDG is a Mendelian congenital disorder of glycosylation (CDG type Iw) caused by defective co-translational N-glycosylation. It is a multisystem disease dominated by neurodevelopmental and neuromuscular-skeletal features.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014270 |
| OMIM (phenotype, AR) | #615596 (CDG type Iw, autosomal recessive) |
| OMIM (phenotype, AD) | #619714 (CDG type Iw, autosomal dominant) |
| OMIM (gene) | *601134 (*STT3A*) |
| HGNC | HGNC:30591 |
| NCBI Gene | 3703 |
| Ensembl | ENSG00000134910 |
| UniProt | P46977 |
| Orphanet | Listed under STT3A-CDG / CDG-Iw |

**Synonyms / alternative names:** CDG-Iw; CDG type Iw; congenital disorder of glycosylation type Iw; STT3A-CDG; oligosaccharyltransferase catalytic subunit STT3A deficiency.

**Information source:** The disease-level knowledge is derived from aggregated resources (OMIM, Orphanet) and small case series/case reports of individual patients, plus in vitro and model-organism functional studies. Given ultra-rarity, most clinical knowledge comes from published individual patient descriptions rather than EHR-scale or registry-scale datasets.

### 2. Etiology

**Disease causal factors:** STT3A-CDG is entirely genetic (Mendelian). It is caused by pathogenic variants in *STT3A*. Two causal mechanisms operate:
- **Autosomal recessive** — biallelic loss-of-function/hypomorphic variants (e.g., homozygous p.Val626Ala; p.Tyr360Ser).
- **Autosomal dominant** — heterozygous missense variants clustering in the catalytic active site acting through a dominant-negative mechanism (e.g., p.Asp167Tyr).

**Genetic risk factors:** The causal variants are themselves the risk determinants. *STT3A* is strongly constrained against both LOF (pLI 0.894) and missense (Z = 4.78) variation, consistent with pathogenicity of the reported alleles.

**Environmental risk factors:** None established. As a Mendelian glycosylation defect, disease onset is determined by genotype, not exposure.

**Protective factors:** No genetic or environmental protective factors are established. Mechanistically, the partial functional redundancy provided by the paralogous STT3B/OST-B complex (which glycosylates some sites skipped by STT3A) may buffer the loss of STT3A activity and could contribute to phenotypic variability, but this is a mechanistic inference rather than a documented protective factor.

**Gene–environment interactions:** None documented for STT3A-CDG.

### 3. Phenotypes

Phenotypes differ between the recessive and dominant forms. All are congenital/early-onset; severity is variable; the neurodevelopmental component is generally non-progressive but with lifelong disability.

| Phenotype | Type | HPO term | Form / frequency | Onset |
|---|---|---|---|---|
| Seizures | Clinical sign | HP:0001250 | Recessive (core) | Neonatal/infantile |
| Intellectual disability | Behavioral/cognitive | HP:0001249 | Both; ~50% in dominant | Childhood |
| Global developmental delay | Clinical sign | HP:0001263 | Both (core) | Infantile |
| Hypotonia | Clinical sign | HP:0001252 | Recessive | Neonatal |
| Failure to thrive / feeding problems | Clinical sign | HP:0001508 | Recessive | Neonatal/infantile |
| Short stature | Physical | HP:0004322 | Dominant | Childhood |
| Macrocephaly | Physical | HP:0000256 | Dominant | Childhood |
| Skeletal anomalies/dysplasia | Physical | HP:0000924 | Dominant | Childhood |
| Increased muscle tone / cramps | Clinical sign | HP:0001276 | Dominant | Childhood |
| Dysmorphic facial features | Physical | HP:0001999 | Dominant | Congenital |
| Abnormal bleeding / coagulopathy | Laboratory/clinical | HP:0001928 / HP:0000132 | Recessive (subset) | Variable |
| Factor VIII deficiency | Laboratory | HP:0003125 | Recessive (subset) | Variable |
| Abnormal type I transferrin | Laboratory | — (CDG biomarker) | Both | Congenital |

**Quality of life impact:** Intellectual disability, seizures, and (in the dominant form) skeletal disease and muscle cramps materially impair daily functioning, communication, and mobility. Coagulopathy in the recessive form carries bleeding risk. Disease-specific QoL instrument data (EQ-5D/SF-36/PROMIS) are not available for this ultra-rare disorder.

### 4. Genetic / Molecular Information

**Causal gene:** *STT3A* (chr11q24.1; OMIM *601134). Encodes the catalytic subunit of the OST-A complex.

**Pathogenic variants (reported):**

| Variant (protein) | cDNA | Type | Inheritance | Mechanism |
|---|---|---|---|---|
| p.Val626Ala | c.1877T>C | Missense | Autosomal recessive (homozygous) | Loss/reduction of catalytic function |
| p.Tyr360Ser | — | Missense | Autosomal recessive | Loss of function; coagulopathy |
| p.Asp167Tyr | — | Missense (active site) | Autosomal dominant | Dominant-negative (zebrafish-validated) |
| Multiple active-site missense | — | Missense | Autosomal dominant | Dominant-negative (16 individuals/9 families) |

**Variant classification:** Reported disease alleles are classified pathogenic/likely pathogenic per ACMG/AMP; the strong missense constraint (Z = 4.78) and active-site clustering support functional deleteriousness.

**Allele frequency:** Pathogenic variants are absent or ultra-rare in gnomAD, consistent with a severe Mendelian disorder.

**Somatic vs germline:** All reported variants are germline (inherited or de novo).

**Functional consequence:** Recessive alleles = loss of function/hypomorphic; dominant active-site alleles = dominant-negative (mutant subunit incorporated into OST-A poisons complex activity).

**Modifier genes:** No formal modifiers established. The paralog *STT3B* (OST-B complex) provides partial substrate redundancy and is a plausible biological modifier of severity (mechanistic inference).

**Epigenetic information:** No disease-specific DNA methylation or histone-modification data available.

**Chromosomal abnormalities:** None associated; STT3A-CDG is a single-gene disorder, not a copy-number/structural disorder.

### 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents are implicated in STT3A-CDG. It is a purely genetic disorder.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A pathogenic *STT3A* variant (biallelic LOF in the recessive form, or a heterozygous active-site missense variant in the dominant form) **alters** the catalytic subunit of the OST-A complex.
2. In the dominant form, the mutant subunit is incorporated into the OST-A complex and **acts as a dominant-negative**, reducing complex activity below the ~50% expected from simple haploinsufficiency (inferred from active-site clustering and yeast data). In the recessive form, biallelic loss **directly reduces** OST-A catalytic output.
3. Reduced OST-A activity **impairs** co-translational transfer of the Glc₃Man₉GlcNAc₂ glycan from dolichol-PP onto N-X-S/T sequons of nascent polypeptides at the Sec61 translocon.
4. This **results in** substrate-selective hypoglycosylation — a subset of glycoproteins (those glycosylated preferentially by STT3A during translation) carry fewer N-glycans. The paralogous STT3B/OST-B complex partially compensates by post-translocationally glycosylating some skipped sites, **limiting** but not preventing the defect (branch: redundancy modulates severity).
5. Hypoglycosylation **destabilizes** or reduces the folding/surface expression of affected glycoproteins — demonstrated for von Willebrand Factor and Factor VIII (patient plasma) and for the insulin receptor and IGF-1R (cell models).
6. Loss of specific glycoprotein functions **leads to** the clinical phenotype:
   - Reduced RTK (insulin receptor, IGF-1R) surface expression → **contributes to** growth failure and skeletal/short-stature phenotype (inferred mechanistic link).
   - Hypoglycosylated coagulation factors (vWF, FVIII) → **produces** bleeding tendency/coagulopathy.
   - Impaired glycosylation of neuronal/CNS glycoproteins → **produces** seizures, developmental delay, intellectual disability, hypotonia (mechanism inferred; the precise CNS substrates are not fully mapped).
7. The abnormal transferrin glycoform (loss of whole N-glycans) **produces** the diagnostic **type I** serum transferrin pattern used for screening.

**Molecular pathways / processes:** Protein N-linked glycosylation via oligosaccharyltransferase (GO:0006487); dolichyl-diphosphooligosaccharide–protein glycotransferase activity (GO:0004579); co-translational protein N-linked glycosylation (GO:0018279). Downstream: receptor tyrosine kinase signaling (insulin/IGF-1R), coagulation cascade.

**Protein dysfunction:** Loss of function (recessive) or dominant-negative (dominant active-site variants) of the STT3A catalytic subunit; secondary misfolding/destabilization of hypoglycosylated client glycoproteins.

**Subcellular site:** Endoplasmic reticulum membrane (GO:0005789), adjacent to the Sec61 translocon.

**Cell types / GO terms:** Broadly all secretory cells, with clinically prominent effects in neurons (CL:0000540), osteoblasts/chondrocytes (skeletal), and hepatocytes/endothelium (coagulation-factor synthesis).

### 7. Anatomical Structures Affected

| Level | Structure | Ontology | Manifestation |
|---|---|---|---|
| Organ/system | Nervous system | UBERON:0001016 | Seizures, DD, ID, hypotonia |
| Organ | Brain | UBERON:0000955 | Neurodevelopmental impairment |
| System | Musculoskeletal | — | Short stature, skeletal anomalies, macrocephaly, muscle cramps |
| System | Hematologic/coagulation | — | Bleeding tendency, FVIII/vWF deficiency (recessive subset) |
| System | Growth/endocrine | — | Failure to thrive, growth failure |
| Tissue | Nervous tissue | — | CNS dysfunction |
| Tissue | Bone/cartilage | — | Reduced mineralization (zebrafish), skeletal dysplasia |
| Cell | Neuron | CL:0000540 | Impaired glycoprotein processing |
| Subcellular | ER membrane | GO:0005789 | Site of defective glycosylation |

**Lateralization:** Manifestations are systemic/bilateral, not lateralized.

### 8. Temporal Development

- **Onset:** Congenital/neonatal-to-infantile. The type I transferrin abnormality is present from birth; seizures, hypotonia, and feeding problems present in infancy in the recessive form; skeletal/growth and dysmorphic features become apparent in childhood in the dominant form.
- **Onset pattern:** Chronic, insidious (developmental).
- **Progression:** The neurodevelopmental disability is generally stable/non-progressive but lifelong; skeletal features evolve with growth. No defined disease "stages."
- **Disease course:** Chronic, lifelong. Within the broader CDG group, the most severe/multisystem presentations carry early-childhood mortality risk (majority of deceased CDG patients died in the first three years — [PMID: 39923392](https://pubmed.ncbi.nlm.nih.gov/39923392/)), though STT3A-CDG-specific survival data are not established.
- **Critical periods / remission:** No spontaneous remission; early developmental and rehabilitative intervention is the window of opportunity.

### 9. Inheritance and Population

- **Epidemiology:** Ultra-rare; ~6 recessive cases reported by 2019 and 16 dominant individuals (9 families) in 2021, with subsequent small reports. No formal prevalence/incidence estimate exists for STT3A-CDG. For context, PMM2-CDG (the most common CDG) has an incidence of ~1 in 33,576 in North America/Europe and accounts for ~60% of all CDG ([PMID: 40737785](https://pubmed.ncbi.nlm.nih.gov/40737785/)).
- **Inheritance:** Both autosomal recessive (OMIM #615596) and autosomal dominant (OMIM #619714).
- **Penetrance / expressivity:** Variable expressivity is documented (e.g., ~50% of dominant-form individuals have intellectual disability); penetrance appears high for the biochemical phenotype but variable for specific clinical features.
- **Anticipation:** Not applicable (no repeat expansion).
- **Founder effects / consanguinity:** The recurrent recessive p.Val626Ala allele appears in multiple unrelated recessive cases; consanguinity is relevant to recessive presentations, as with most rare AR disorders. No formally described founder population.
- **Carrier frequency:** Not established; pathogenic alleles are ultra-rare in gnomAD.
- **Demographics:** No specific ethnic predilection, geographic clustering, or sex bias reported; both sexes affected.

### 10. Diagnostics

**Biochemical screening:** Serum transferrin analysis by isoelectric focusing (TIEF), HPLC, or capillary electrophoresis shows a **CDG type I pattern** (increased di- and a-sialotransferrin from loss of whole N-glycans).

> "a type I carbohydrate deficient transferrin pattern" — [PMID: 30701557](https://pubmed.ncbi.nlm.nih.gov/30701557/)

**Molecular confirmation:** Exome/genome sequencing or targeted *STT3A* sequencing is required for definitive diagnosis; some OST-subunit CDG may be missed by transferrin analysis alone.

> "Additional cases of STT3B-CDG may be missed by transferrin analysis and will require exome or genome sequencing" — [PMID: 23842455](https://pubmed.ncbi.nlm.nih.gov/23842455/)

**Ancillary labs:** Coagulation studies (FVIII, vWF) in patients with bleeding; these may reveal hypoglycosylated coagulation factors.

**Genetic testing modalities:** WES and WGS are both high-yield; targeted single-gene testing or CDG/neurodevelopmental gene panels can be used once biochemically suspected. CMA, karyotyping, FISH, mtDNA testing, and repeat-expansion testing are not applicable (single-gene point-variant disorder).

**Differential diagnosis:** Other CDG type I disorders (PMM2-CDG, ALG-group, DDOST-CDG, RPN1-CDG, STT3B-CDG), which share the type I transferrin pattern and neurodevelopmental phenotype. Transferrin protein variants can produce misleading patterns ([PMID: 37876147](https://pubmed.ncbi.nlm.nih.gov/37876147/)); neuraminidase treatment helps resolve these. Diagnosis is refined by identifying the causal gene.

**Screening:** No routine newborn screening for STT3A-CDG. TIEF has been proposed as a useful screen in childhood epilepsy cohorts given the ~4.4% CDG prevalence in that population ([PMID: 34440401](https://pubmed.ncbi.nlm.nih.gov/34440401/)).

### 11. Outcome / Prognosis

- **Survival/mortality:** No STT3A-CDG-specific survival statistics. Within the CDG group broadly, severe multisystem presentations carry substantial early-childhood mortality (majority of deceased CDG patients died in the first three years, ~one-third from cardiopulmonary failure — [PMID: 39923392](https://pubmed.ncbi.nlm.nih.gov/39923392/)).
- **Morbidity/disability:** Lifelong neurodevelopmental disability (intellectual disability, seizures), skeletal disease and short stature (dominant form), and bleeding risk (recessive subset).
- **Complications:** Seizure-related morbidity, feeding/growth failure, bleeding events, orthopedic complications.
- **Prognostic factors:** Genotype (recessive vs dominant form; residual OST-A activity), presence of coagulopathy, and severity of neurological involvement. No validated prognostic biomarkers beyond the biochemical/genetic diagnosis.
- **Recovery potential:** No reversal of the underlying defect; supportive care and rehabilitation can improve function.

### 12. Treatment

There is **no disease-specific or curative therapy** for STT3A-CDG. Management is supportive and multidisciplinary:

- **Pharmacotherapy:** Symptomatic — anti-seizure medications for epilepsy; standard management of feeding/growth issues; hematologic management (e.g., factor replacement/DDAVP considerations) for bleeding in the recessive subset. (NCIT: anticonvulsant therapy; supportive care.)
- **Dietary sugar therapies do NOT apply.** Galactose (PGM1-CDG, TMEM165-CDG) and mannose (MPI-CDG) are effective only in specific CDG subtypes; STT3A-CDG is an ER glycan-transfer (CDG-I) defect not amenable to these.

  > "There are >100 CDGs, but only specific types are treatable" — [PMID: 28323990](https://pubmed.ncbi.nlm.nih.gov/28323990/)

- **Advanced/experimental therapeutics:** No approved gene, cell, or RNA-based therapy; no STT3A-CDG-specific clinical trials identified.
- **Supportive/rehabilitative care:** Physical, occupational, and speech therapy; developmental support; orthopedic and nutritional management; multidisciplinary metabolic clinic follow-up.
- **Personalized medicine:** Genotype (dominant vs recessive) informs genetic counseling and family planning but not, at present, a targeted pharmacologic strategy.

### 13. Prevention

- **Primary prevention:** Not possible for a Mendelian disorder beyond reproductive planning. Genetic counseling is central — recurrence risk is 25% for AR families and up to 50% for AD transmission (with de novo cases in the dominant form).
- **Secondary prevention:** Early biochemical (TIEF) and molecular diagnosis enables early developmental intervention and complication surveillance (seizures, bleeding, growth).
- **Tertiary prevention:** Anticipatory management of seizures, feeding/growth, bleeding risk, and orthopedic complications.
- **Genetic screening:** Carrier testing and prenatal/preimplantation genetic testing are available for families with a known pathogenic variant. No population-based newborn screening exists.
- **Immunization/public health/environmental:** Not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *STT3A* is deeply conserved. Orthologs and functional equivalents exist in mouse (*Stt3a*), zebrafish (*stt3a*), and the single *STT3* gene in *S. cerevisiae* (yeast). These orthologs are central to disease modeling (below).
- **Natural disease in other species:** No naturally occurring animal disease specifically attributed to *STT3A* variants is documented (no OMIA entry noted for STT3A-CDG). Disease knowledge in animals comes from engineered models, not spontaneous disease.
- **Comparative biology / conservation:** The strong evolutionary conservation of STT3 catalytic function — from yeast to human — underlies the ability to model patient variants in *S. cerevisiae* and zebrafish and validates conservation of the disease mechanism.
- **Transmission / zoonosis:** Not applicable (non-infectious genetic disorder).

### 15. Model Organisms

| Model | Type | Genetic strategy | Phenotype recapitulation | Reference |
|---|---|---|---|---|
| *S. cerevisiae* (yeast) | Cellular/in vivo | Express STT3 with patient-homologous variants; hypomorphic *stt3-7* background | Defective glycosylation of carboxypeptidase Y; dominance demonstrated | [PMID: 34653363](https://pubmed.ncbi.nlm.nih.gov/34653363/) |
| Zebrafish (*Danio rerio*) | Vertebrate | CRISPR-Cas9 heterozygous knockdown modeling p.Asp167Tyr | Craniofacial dysmorphology, reduced mineralized bone, abnormal locomotion/developmental delay — mirrors patient features | [PMID: 39891251](https://pubmed.ncbi.nlm.nih.gov/39891251/) |
| Human patient fibroblasts | In vitro | Endogenous patient variants | Hypoglycosylation of STT3A-specific reporters; rescued by WT *STT3A* cDNA | [PMID: 23842455](https://pubmed.ncbi.nlm.nih.gov/23842455/) |
| HeLa / HEK293T | In vitro cell line | STT3A/STT3B knockout; reporter constructs | Isoform-specific glycosylation defects; RTK surface loss | [PMID: 31101650](https://pubmed.ncbi.nlm.nih.gov/31101650/); [PMID: 29282902](https://pubmed.ncbi.nlm.nih.gov/29282902/) |

> "expression of STT3 containing variants homologous to those in affected individuals induced defective glycosylation of carboxypeptidase Y in a wild-type yeast strain" — [PMID: 34653363](https://pubmed.ncbi.nlm.nih.gov/34653363/)

> "Heterozygous knockdown zebrafish exhibit phenotypes similar to those of patients, including craniofacial dysmorphology" — [PMID: 39891251](https://pubmed.ncbi.nlm.nih.gov/39891251/)

**Model limitations:** Yeast lacks the STT3A/STT3B paralog split and multicellular phenotypes; zebrafish knockdown models capture skeletal/craniofacial and behavioral features but not the full neurodevelopmental/coagulation spectrum. No mouse knock-in model of a patient variant is established in the reviewed literature.

---

## Mechanistic Model / Interpretation

```
                 STT3A pathogenic variant
                  /                    \
       Biallelic LOF                Heterozygous active-site
       (recessive)                  missense (dominant)
            |                             |
            |                    mutant subunit incorporated
            |                    into OST-A complex
            |                             |
            v                             v
        Reduced OST-A catalytic activity (dominant-negative in AD)
                          |
                          v
   Impaired co-translational transfer of Glc3Man9GlcNAc2
   onto N-X-S/T sequons at the Sec61 translocon (ER membrane)
                          |
              [ STT3B/OST-B partial rescue — modulates severity ]
                          |
                          v
      Substrate-selective HYPOGLYCOSYLATION of STT3A clients
              /            |              \
             v             v               v
   Transferrin      vWF / FVIII      Insulin-R / IGF-1R
   (type I CDT      hypoglycosylated  reduced surface
   biomarker)       & destabilized    expression
             \            |               /
              v           v              v
       DIAGNOSTIC     BLEEDING        GROWTH FAILURE /
       SIGNATURE      TENDENCY        SKELETAL PHENOTYPE
                          |
                          v
   + Impaired glycosylation of CNS glycoproteins (inferred)
                          |
                          v
   SEIZURES, DEVELOPMENTAL DELAY, INTELLECTUAL DISABILITY, HYPOTONIA
```

**Upstream vs downstream:** The upstream lesion is the *STT3A* variant and consequent reduction of OST-A catalytic activity. Immediately downstream is substrate-selective hypoglycosylation, buffered by STT3B redundancy. Further downstream are the destabilization of specific client glycoproteins (transferrin — diagnostic; vWF/FVIII — coagulopathy; insulin-R/IGF-1R — growth/skeletal), and finally the clinical manifestations. The CNS phenotype is the least mechanistically resolved link (which specific neuronal glycoproteins mediate seizures and cognition remains inferred rather than demonstrated). Population-genetic constraint (pLI 0.894; missense Z 4.78) independently confirms that both loss-of-function and missense perturbation of this gene are under strong purifying selection — the molecular-genetic expectation for a dosage-sensitive, dominantly-and-recessively acting disease gene.

---

## Evidence Base

| PMID | Title (abbreviated) | Role in this report |
|---|---|---|
| [23842455](https://pubmed.ncbi.nlm.nih.gov/23842455/) | *Mutations in STT3A and STT3B cause two CDGs* | Landmark: identifies STT3A as OST catalytic subunit; original recessive p.Val626Ala; sequencing needed for diagnosis |
| [34653363](https://pubmed.ncbi.nlm.nih.gov/34653363/) | *Active site variants in STT3A cause a dominant type I CDG* | Landmark: defines the autosomal-dominant form (16 individuals/9 families); active-site clustering; yeast dominance |
| [39891251](https://pubmed.ncbi.nlm.nih.gov/39891251/) | *Heterozygous STT3A variation → dominant CDG; zebrafish validation* | Confirms dominant inheritance; zebrafish recapitulation of p.Asp167Tyr |
| [30701557](https://pubmed.ncbi.nlm.nih.gov/30701557/) | *Factor VIII and vWF deficiency in STT3A-CDG* | Recessive core phenotype; coagulopathy; hypoglycosylated vWF; OMIM #615596 |
| [31433728](https://pubmed.ncbi.nlm.nih.gov/31433728/) | *N-glycosylation not directly coupled to translocation* | STT3A translocon-coupled N→C scanning mechanism |
| [28860277](https://pubmed.ncbi.nlm.nih.gov/28860277/) | *DC2 and KCP2 mediate OST–translocon interaction* | STT3A localization adjacent to translocon; co-translational glycosylation |
| [25460543](https://pubmed.ncbi.nlm.nih.gov/25460543/) | *Cotranslational and posttranslocational N-glycosylation* | STT3B redundancy (glycosylates STT3A-skipped sites) |
| [25135935](https://pubmed.ncbi.nlm.nih.gov/25135935/) | *Oxidoreductase activity for cysteine-proximal sites* | STT3B/MagT1 mechanism explaining substrate selectivity |
| [31101650](https://pubmed.ncbi.nlm.nih.gov/31101650/) | *Selective inhibition of N-glycosylation impairs RTK processing* | Downstream: reduced insulin-R/IGF-1R surface abundance |
| [39435313](https://pubmed.ncbi.nlm.nih.gov/39435313/) | *Metabolomic profiling reveals AD CDG-Iw* | OMIM #619714 for the dominant form |
| [40737785](https://pubmed.ncbi.nlm.nih.gov/40737785/) | *Incidence/prevalence of PMM2-CDG* | Contextualizes STT3A-CDG rarity within CDG |
| [39923392](https://pubmed.ncbi.nlm.nih.gov/39923392/) | *Causes of mortality in CDG* | CDG natural history/mortality context |
| [34440401](https://pubmed.ncbi.nlm.nih.gov/34440401/) | *CDG prevalence in childhood epilepsy; TIEF* | TIEF as screening tool; CDG in epilepsy cohorts |
| [28323990](https://pubmed.ncbi.nlm.nih.gov/28323990/) | *Galactose in TMEM165-CDG* | Only specific CDGs are treatable → not STT3A-CDG |
| [37876147](https://pubmed.ncbi.nlm.nih.gov/37876147/) | *Misleading transferrin variants* | Diagnostic pitfall in transferrin screening |
| [29282902](https://pubmed.ncbi.nlm.nih.gov/29282902/) | *GFP mutant to monitor STT3B glycosylation* | Isoform-specific reporter methodology |

**Evidence-source types:** Human clinical (case series/reports: 23842455, 34653363, 30701557, 39435313); model organism (yeast 34653363; zebrafish 39891251); in vitro/cell biology (31101650, 25460543, 25135935, 28860277, 31433728, 29282902); computational/population-genetic (gnomAD constraint — Finding 11).

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity limits epidemiology.** No prevalence, incidence, penetrance quantification, carrier frequency, or survival statistics exist specifically for STT3A-CDG. Mortality data cited are from the pan-CDG group, not STT3A-CDG.
2. **Genotype–phenotype correlation is immature.** The number of reported patients (~a few dozen across both forms) is too small to define robust correlations between specific alleles/residual OST-A activity and clinical severity.
3. **The CNS mechanistic link is inferred, not demonstrated.** The specific neuronal glycoproteins whose hypoglycosylation causes seizures and cognitive impairment have not been mapped for STT3A-CDG.
4. **No mammalian knock-in model** of a patient variant was found in the reviewed literature; the mouse phenotype for patient alleles is undefined.
5. **No therapeutic pipeline.** No approved or trial-stage disease-specific therapy exists; the disorder is currently supportive-care only.
6. **Dominant-negative mechanism is supported by yeast/zebrafish and active-site clustering but not fully dissected biochemically** in the human OST-A complex (e.g., stoichiometry of mutant incorporation and quantitative activity reduction).
7. **Ontology annotations** (HPO/GO/UBERON/CL/CHEBI) are assembled from literature-reported features and standard mappings rather than curated disease-ontology cross-references, and should be verified against current MONDO/HPO releases.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an STT3A-CDG patient registry** within the FCDGC/GLYCEN networks to collect natural-history, survival, and genotype–phenotype data prospectively.
2. **Generate a knock-in mouse (or refine the zebrafish) carrying recurrent alleles** (p.Val626Ala recessive; p.Asp167Tyr dominant) to model the neurodevelopmental, skeletal, and coagulation phenotypes and to serve as a preclinical therapeutic platform.
3. **Map the STT3A-dependent glycoproteome of neural tissue** (glycoproteomics/glycomics on patient iPSC-derived neurons and organoids) to identify the specific hypoglycosylated CNS substrates driving seizures and cognitive impairment.
4. **Quantify the dominant-negative effect biochemically** by reconstituting OST-A complexes with defined ratios of wild-type and mutant STT3A and measuring transfer activity and complex assembly.
5. **Systematic coagulation-factor glycosylation study** across STT3A-CDG patients to determine the frequency and severity of the vWF/FVIII phenotype and inform bleeding-risk management.
6. **Explore proteostasis/chaperone modulators** (e.g., ER quality-control or STT3B-upregulation strategies) as candidate therapeutic approaches leveraging the STT3B redundancy branch.
7. **Refine and validate the ontology annotation set** (HPO frequencies, CL/UBERON/CHEBI/NCIT terms) against the latest MONDO, HPO, and Orphanet releases for knowledge-base ingestion.

---

## Ontology Appendix

| Category | Term | ID |
|---|---|---|
| Disease | STT3A-CDG | MONDO:0014270; OMIM #615596 (AR), #619714 (AD) |
| Gene | STT3A | HGNC:30591; NCBI Gene 3703; UniProt P46977; OMIM *601134 |
| Biological process | Protein N-linked glycosylation via OST | GO:0006487 |
| Molecular function | Dolichyl-diphosphooligosaccharide–protein glycotransferase | GO:0004579 |
| Biological process | Co-translational protein N-linked glycosylation | GO:0018279 |
| Cellular component | Endoplasmic reticulum membrane | GO:0005789 |
| Anatomy | Nervous system | UBERON:0001016 |
| Anatomy | Brain | UBERON:0000955 |
| Cell type | Neuron | CL:0000540 |
| Phenotype | Seizure | HP:0001250 |
| Phenotype | Intellectual disability | HP:0001249 |
| Phenotype | Global developmental delay | HP:0001263 |
| Phenotype | Hypotonia | HP:0001252 |
| Phenotype | Failure to thrive | HP:0001508 |
| Phenotype | Short stature | HP:0004322 |
| Phenotype | Macrocephaly | HP:0000256 |
| Phenotype | Abnormal skeletal morphology | HP:0000924 |
| Phenotype | Hypertonia | HP:0001276 |
| Phenotype | Factor VIII deficiency | HP:0003125 |
| Chemical | Dolichol | CHEBI:23509 |
| Chemical | Asparagine | CHEBI:22653 |
| Chemical | N-acetylglucosamine | CHEBI:506227 |

---

*Report compiled from 11 confirmed findings and 33 reviewed papers across a 5-iteration autonomous investigation. Evidence sources span human clinical case series, yeast and zebrafish model organisms, in vitro cell biology, and computational population-genetic constraint analysis.*


## Artifacts

- [OpenScientist final report](STT3A-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](STT3A-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 31 |
| Quoted claims found in source | 31 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 22 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014270` (3 mentions) - the report calls it "MONDO"; MONDO calls it **STT3A-congenital disorder of glycosylation**
- `HP:0001250` (2 mentions) - the report calls it "Clinical sign", "Seizure"; HP calls it **Seizure**
- `HP:0001249` (2 mentions) - the report calls it "Behavioral/cognitive", "Intellectual disability"; HP calls it **Intellectual disability**
- `HP:0001263` (2 mentions) - the report calls it "Clinical sign", "Global developmental delay"; HP calls it **Global developmental delay**
- `HP:0001252` (2 mentions) - the report calls it "Clinical sign", "Hypotonia"; HP calls it **Hypotonia**
- `HP:0001508` (2 mentions) - the report calls it "Clinical sign", "Failure to thrive"; HP calls it **Failure to thrive**
- `HP:0004322` (2 mentions) - the report calls it "Physical", "Short stature"; HP calls it **Short stature**
- `HP:0000256` (2 mentions) - the report calls it "Physical", "Macrocephaly"; HP calls it **Macrocephaly**
- `HP:0000924` (2 mentions) - the report calls it "Physical", "Abnormal skeletal morphology"; HP calls it **Abnormality of the skeletal system**
- `HP:0001276` (2 mentions) - the report calls it "Clinical sign", "Hypertonia"; HP calls it **Hypertonia**
- `HP:0001999` (1 mention) - the report calls it "Physical"; HP calls it **Abnormal facial shape**
- `HP:0003125` (2 mentions) - the report calls it "Laboratory", "Factor VIII deficiency"; HP calls it **Reduced factor VIII activity**
- `CHEBI:23509` (1 mention) - the report calls it "Dolichol"; CHEBI calls it **cysteine derivative**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0018279` (obsolete protein N-linked glycosylation via asparagine) (2 mentions) - replaced by `GO:0006487`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006487` (2 mentions) - the report calls it "Protein N-linked glycosylation via OST"; GO calls it **protein N-linked glycosylation**
- `GO:0004579` (2 mentions) - the report calls it "Dolichyl-diphosphooligosaccharide–protein glycotransferase"; GO calls it **dolichyl-diphosphooligosaccharide-protein glycotransferase activity**
- `GO:0018279` (2 mentions) - the report calls it "Co-translational protein N-linked glycosylation"; GO calls it **obsolete protein N-linked glycosylation via asparagine**
- `GO:0005789` (3 mentions) - the report calls it "ER membrane", "Endoplasmic reticulum membrane"; GO calls it **endoplasmic reticulum membrane**, and lists "ER membrane" among its other names
- `CHEBI:506227` (1 mention) - the report calls it "N-acetylglucosamine"; CHEBI calls it **N-acetyl-D-glucosamine**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001250` - called "Clinical sign", "Seizure"
- `HP:0001249` - called "Behavioral/cognitive", "Intellectual disability"
- `HP:0001263` - called "Clinical sign", "Global developmental delay"
- `HP:0001252` - called "Clinical sign", "Hypotonia"
- `HP:0001508` - called "Clinical sign", "Failure to thrive"
- `HP:0004322` - called "Physical", "Short stature"
- `HP:0000256` - called "Physical", "Macrocephaly"
- `HP:0000924` - called "Physical", "Abnormal skeletal morphology"
- `HP:0001276` - called "Clinical sign", "Hypertonia"
- `HP:0003125` - called "Laboratory", "Factor VIII deficiency"
- `GO:0005789` - called "ER membrane", "Endoplasmic reticulum membrane"