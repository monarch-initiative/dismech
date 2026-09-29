---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T12:31:33.354749'
end_time: '2026-09-01T13:10:55.368346'
duration_seconds: 2362.01
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: ALPK3-Related Hypertrophic Cardiomyopathy
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
citation_count: 17
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 23
  on_topic: 15
  validator_version: 0.2.1
term_validation:
  total_terms: 44
  verified: 43
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 8
  labels_mismatched: 15
  mislabelled_terms:
  - term_id: HP:0001639
    reported_labels:
    - Clinical sign
    - apical variant
    ontology_label: Hypertrophic cardiomyopathy
  - term_id: HP:0001644
    reported_labels:
    - Clinical sign
    ontology_label: Dilated cardiomyopathy
  - term_id: HP:0025169
    reported_labels:
    - LV aneurysm
    ontology_label: Left ventricular systolic dysfunction
  - term_id: HP:0001707
    reported_labels:
    - Physical manifestation
    ontology_label: Abnormal right ventricle morphology
  - term_id: HP:0001637
    reported_labels:
    - Laboratory/imaging
    ontology_label: Abnormal myocardium morphology
  - term_id: HP:0005162
    reported_labels:
    - Clinical sign
    ontology_label: Abnormal left ventricular function
  - term_id: HP:0001723
    reported_labels:
    - Clinical sign
    ontology_label: Restrictive cardiomyopathy
  - term_id: HP:0005110
    reported_labels:
    - Clinical sign
    ontology_label: Atrial fibrillation
  - term_id: HP:0004758
    reported_labels:
    - Clinical sign
    ontology_label: Effort-induced polymorphic ventricular tachycardia
  - term_id: HP:0001645
    reported_labels:
    - Clinical outcome
    ontology_label: Sudden cardiac death
  - term_id: GO:0031430
    reported_labels:
    - 'GO cellular component: M band'
    - sarcomeric M-band
    ontology_label: M band
  - term_id: NCIT:C2496
    reported_labels:
    - Beta-adrenergic blockers
    ontology_label: Anti-VEGF Monoclonal Antibody
  - term_id: NCIT:C51899
    reported_labels:
    - septal myectomy
    - "Septal reduction therapy** \u2014 surgical **septal myectomy"
    ontology_label: Radical Cystoprostatectomy
  - term_id: NCIT:C50077
    reported_labels:
    - Implantable cardioverter-defibrillator (ICD)
    ontology_label: Motor Device
  - term_id: NCIT:C15328
    reported_labels:
    - Heart transplantation
    ontology_label: Splenectomy
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ALPK3-Related_Hypertrophic_Cardiomyopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ALPK3-Related_Hypertrophic_Cardiomyopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ALPK3-Related Hypertrophic Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ALPK3-Related Hypertrophic Cardiomyopathy** covering all of the
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

# ALPK3-Related Hypertrophic Cardiomyopathy: Comprehensive Disease Report

## Summary

**ALPK3-related hypertrophic cardiomyopathy (HCM)** is a Mendelian sarcomeric/M-band cardiomyopathy caused by loss-of-function (LoF) variants in *ALPK3* (alpha-protein kinase 3), located at chromosome **15q25.3** (HGNC:17870; NCBI Gene 57538; OMIM gene *617608*; disease MIM *618052*, **CMH27**). ALPK3 encodes a **catalytically-dead atypical α-kinase** that functions as a **structural M-band scaffold** of the cardiac sarcomere, anchoring myomesins (MYOM1/2), MuRF (muscle ring-finger) E3 ubiquitin ligases, and the autophagy adaptor SQSTM1/p62 to maintain thick-filament proteostasis. It is a distinctive disease because it exhibits a **dose-dependent, zygosity-driven severity gradient**: biallelic (recessive) LoF causes a severe, often lethal prenatal/pediatric cardiomyopathy with syndromic extracardiac features, whereas heterozygous (dominant) protein-truncating variants (ALPK3tv) cause an incompletely penetrant adult-onset HCM that accounts for roughly **1–4% of adult HCM**.

The core mechanism is now well supported: ALPK3 loss displaces myomesins from the M-band, driving **thick-filament protein aggregation, sarcomere and intercalated-disc disarray, abnormal calcium handling, and hypercontractility**. In model systems, these defects were partially corrected by the myosin inhibitor **mavacamten**, and durable phenotypic rescue was achieved in global knockout mice using **AAV-delivered ALPK3**, establishing two genotype-directed therapeutic proof-of-concept fronts that remain preclinical. Clinically, the adult heterozygous phenotype has a characteristic morphology — **apical/septal hypertrophy, apical aneurysm, right-ventricular involvement, and myocardial fibrosis** — and ALPK3 has emerged as one of the leading (frequently the second most common) genotypes identified in apical HCM cohorts.

Management currently follows **standard HCM guidelines** (beta-blockers, disopyramide, septal reduction therapy, ICD for sudden-cardiac-death [SCD] prevention, and transplantation for end-stage disease), with **cardiac MRI late gadolinium enhancement (LGE)** serving as a key risk-stratification marker particularly relevant to the fibrosis- and aneurysm-prone ALPK3 phenotype. ALPK3 now carries **established gene–disease validity for HCM with recognized dual (recessive and dominant) inheritance** per the ClinGen Hereditary Cardiovascular Disease Gene Curation Expert Panel.

---

## 1. Disease Information

**Overview.** ALPK3-related cardiomyopathy is an inherited cardiac muscle disease presenting predominantly as hypertrophic cardiomyopathy, but with a broad phenotypic spectrum that also includes dilated cardiomyopathy (DCM), a neonatal DCM-to-hypertrophy transition, and restrictive/mixed physiology. The disease exists as a **spectrum defined by zygosity**: severe recessive pediatric disease at one pole and penetrance-limited adult dominant HCM at the other.

**Key identifiers.**

| Resource | Identifier |
|----------|------------|
| Gene symbol | *ALPK3* (α-protein kinase 3; formerly *MIDORI*) |
| HGNC | HGNC:17870 |
| NCBI Gene | 57538 |
| Cytogenetic locus | 15q25.3 |
| OMIM (gene) | *617608* |
| OMIM (disease) | *618052* — Cardiomyopathy, familial hypertrophic, 27 (CMH27) |
| MONDO | Cardiomyopathy, familial hypertrophic, 27 (maps to OMIM 618052) |
| ICD-10 | I42.1 (obstructive HCM) / I42.2 (other HCM) |
| ICD-11 | BC43.0 (hypertrophic cardiomyopathy) |
| MeSH | D002312 (Cardiomyopathy, Hypertrophic) |

**Synonyms / alternative names:** ALPK3 cardiomyopathy; ALPK3-related HCM; CMH27; alpha-kinase 3 cardiomyopathy; biallelic ALPK3 pediatric cardiomyopathy (recessive form); ALPK3tv HCM (heterozygous truncating-variant form).

**Information source.** Evidence is derived from **aggregated disease-level and patient-level literature** — systematic variant curations, multicentric cohorts (French, Swedish, Chinese), individual case reports, and functional model-organism/iPSC studies — rather than from a single EHR dataset.

---

## 2. Etiology

**Primary causal factor: genetic.** ALPK3-related cardiomyopathy is a **monogenic disorder** caused by loss-of-function variants in *ALPK3*. There is no established environmental or infectious cause. The disease displays a **dose-dependent relationship between ALPK3 gene dosage and phenotype severity** (Finding F001; Finding F007).

**Genetic risk factors.**
- **Biallelic LoF variants** (homozygous or compound heterozygous nonsense, frameshift, or splice variants) → severe, often lethal, prenatal/early-onset cardiomyopathy with extracardiac involvement (recessive).
- **Heterozygous protein-truncating variants** (nonsense/frameshift/splice) → adult-onset dominant HCM explaining ≈1–4% of adult HCM.
- As stated in the integrative review ([PMID: 41221624](https://pubmed.ncbi.nlm.nih.gov/41221624/)): *"Biallelic loss-of-function variants lead to severe, often lethal cardiomyopathy with prenatal or early onset presentation and extracardiac involvement. Heterozygous protein-truncating variants, defined as nonsense or frameshift (resulting from insertion/deletion events or splicing mutations), explain ≈1% to 4% of adult hypertrophic cardiomyopathy."*

**Environmental / demographic risk factors.** No specific toxic, occupational, or infectious triggers are established. **Male predominance** is reported among heterozygous ALPK3tv HCM patients, and **age** is a strong modifier given the late onset and age-dependent penetrance ([PMID: 41645375](https://pubmed.ncbi.nlm.nih.gov/41645375/)). **Consanguinity** is an important contextual factor for the recessive form — the founding families were consanguineous ([PMID: 26846950](https://pubmed.ncbi.nlm.nih.gov/26846950/)).

**Protective factors.** No specific genetic or environmental protective alleles are established for ALPK3 cardiomyopathy. The **incomplete penetrance** of heterozygous variants (~20% in the founding family; even lower in later cohorts) implies the existence of unidentified genetic/environmental modifiers that buffer disease expression.

**Gene–environment interactions.** Not specifically characterized. The variable expressivity within families carrying identical variants (e.g., a mother with severe obstructive HCM and an asymptomatic brother carrying the same variant; [PMID: 41645375](https://pubmed.ncbi.nlm.nih.gov/41645375/)) points to modifier effects, but specific gene–environment interactions have not been mapped.

---

## 3. Phenotypes

ALPK3 cardiomyopathy has distinct **cardiac** and **extracardiac** phenotype clusters, with the extracardiac cluster largely confined to the biallelic (recessive) pediatric form.

### Cardiac phenotypes

| Phenotype | Type | HPO term (suggested) | Onset | Frequency / notes |
|-----------|------|----------------------|-------|-------------------|
| Hypertrophic cardiomyopathy | Clinical sign | HP:0001639 | Neonatal (biallelic) to adult (heterozygous) | Predominant phenotype; 26/31 adults in French cohort |
| Dilated cardiomyopathy / neonatal DCM | Clinical sign | HP:0001644 | Neonatal | 8/18 (44.4%; 95% CI 21.5–69.2%) biallelic live-borns had neonatal DCM transitioning to hypertrophy |
| Apical hypertrophy | Physical manifestation | HP:0001639 (apical variant) | Adult | Frequent in heterozygous ALPK3tv; ALPK3 a leading ApHCM genotype |
| Apical aneurysm | Physical manifestation | HP:0025169 (LV aneurysm) | Adult | ~17.2% in ApHCM cohort |
| Right ventricular involvement | Physical manifestation | HP:0001707 | Adult | Reported in heterozygous form |
| Myocardial fibrosis (LGE) | Laboratory/imaging | HP:0001637 | Adult | Prominent; prognostically important |
| Left ventricular systolic dysfunction | Clinical sign | HP:0005162 | Pediatric | E.g., patient 2, PMID 40447126 |
| Restrictive physiology / hypertrabeculation | Clinical sign | HP:0001723 | Adult | Overlap phenotype (PMID 36660067) |
| Atrial fibrillation | Clinical sign | HP:0005110 | Adult | 41.4% in ApHCM cohort |
| Non-sustained ventricular tachycardia | Clinical sign | HP:0004758 | Adult | 29.3% in ApHCM cohort |
| Sudden cardiac death / HCM-related events | Clinical outcome | HP:0001645 | Any | 36.2% had HCM-related events in ApHCM cohort |

### Extracardiac phenotypes (biallelic/recessive form — syndromic)

| Phenotype | HPO term (suggested) | Notes |
|-----------|----------------------|-------|
| Facial dysmorphism | HP:0001999 | Recurrent triad component |
| Cleft palate | HP:0000175 | Reported in Tunisian case (PMID 30046096) |
| Pectus excavatum / carinatum | HP:0000767 / HP:0000768 | Thoracic deformity |
| Scoliosis | HP:0002650 | PMID 40447126 |
| Joint contractures | HP:0002803 | PMID 40447126 |
| Short stature | HP:0004322 | Multiple biallelic cases |
| Webbed neck | HP:0000465 | PMID 40447126 |
| Hand/foot skeletal deformities | HP:0001155 / HP:0001760 | PMID 30046096 |

**Onset, severity, progression:** Biallelic disease is **neonatal/prenatal-onset, severe, and often lethal** (progressive; frequent early death). Heterozygous disease is **adult-onset (delayed ~10 years vs. sarcomeric HCM), variable severity, slowly progressive** with age-dependent penetrance. **Quality-of-life impact** ranges from catastrophic (perinatal heart failure, death, transplantation in the biallelic form) to variable in adults (exertional symptoms, arrhythmia burden, ICD, and SCD risk).

---

## 4. Genetic / Molecular Information

**Causal gene.** *ALPK3* (HGNC:17870; NCBI Gene 57538; OMIM *617608*), 15q25.3. Encodes alpha-protein kinase 3, an atypical α-kinase that is **catalytically dead** and functions structurally.

**Pathogenic variant spectrum.** The disease is driven overwhelmingly by **truncating / loss-of-function** variants:
- **Nonsense** (e.g., p.Arg1173*, p.Ser653*)
- **Frameshift** (e.g., c.1531_1532delAA p.Lys511Argfs*12; c.109del p.R37Gfs*72; c.2757dup p.T920Hfs*14; c.3272del p.G1091Vfs*43; c.1550dupC p.Pro518ThrfsTer53)
- **Splice-site** variants
- **Contiguous gene deletion** of 15q25.2q25.3 has been reported in a biallelic context (PMID 37671554)
- Some **missense** variants (e.g., p.Arg1164Gln) appear in overlap/adult phenotypes (PMID 36660067)

Documented patient-level variants exceed 150 in systematic curation (156 variants; Finding F001).

**Variant classification (ACMG/AMP).** Truncating variants are generally classified **Pathogenic / Likely Pathogenic**; classification for heterozygotes was historically complicated because ALPK3 was initially annotated as autosomal recessive — re-analysis after dominant inheritance was established upgraded several variants (PMID 41645375). Bayesian/segregation evidence has supported Likely Pathogenic calls for recurrent truncating variants.

**Allele frequency.** Heterozygous ALPK3 truncating variants are rare but present in population databases (gnomAD); their appreciable heterozygous frequency combined with incomplete penetrance underlies the ~1–4% contribution to adult HCM.

**Somatic vs. germline.** All disease-associated variants are **germline**. No somatic mechanism is implicated.

**Functional consequence.** **Loss of function** (haploinsufficiency in heterozygotes; complete loss in biallelic patients) — loss of the M-band scaffolding function of ALPK3.

**Modifier genes / epigenetics.** No specific Mendelian modifier genes are established. Notably, **microRNA-384-5p** regulates the ALPK3 pathway in hypertrophy models (Finding F009): *"miR-384-5p was notably decreased in cardiac hypertrophic tissues and cells, and overexpression of miR-384-5p could ameliorate pressure overload"* ([PMID: 35510648](https://pubmed.ncbi.nlm.nih.gov/35510648/)). This provides an epigenetic/post-transcriptional regulatory axis. Chromosomal abnormalities are limited to the reported 15q25 contiguous deletion.

---

## 5. Environmental Information

ALPK3 cardiomyopathy is a **monogenic disease with no established environmental, lifestyle, or infectious etiology**. No toxins, radiation, pollutants, dietary factors, or pathogens are implicated as causes or triggers. As with HCM generally, **strenuous competitive exercise** may modulate SCD risk and symptom burden, and standard HCM lifestyle counseling applies, but these are not ALPK3-specific causal factors. Age and male sex act as demographic modifiers of penetrance in the heterozygous form (see Section 2).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Loss-of-function variant in *ALPK3*** (biallelic → complete loss; heterozygous → haploinsufficiency) **leads to** reduced/absent functional ALPK3 protein at the sarcomeric M-band.
2. Loss of ALPK3 **results in** failure of its scaffolding function — it can no longer anchor **myomesins (MYOM1/2), MuRF E3 ubiquitin ligases, and SQSTM1/p62** at the M-band.
3. Displacement of myomesins and loss of the proteostasis hub **leads to** impaired thick-filament protein turnover and **thick-filament protein aggregation**.
4. Aggregation and scaffold failure **result in** **disordered sarcomeres and intercalated discs** (ultrastructural disarray).
5. Sarcomere disarray **leads to** **abnormal calcium handling** (elevated diastolic calcium) and altered myosin mechanochemistry — a **reduced super-relaxed (SRX) myosin fraction**, prolonged relaxation, and **hypercontractility** (demonstrated in the K201X knock-in mouse).
6. Reduced PKA phosphorylation of cardiac troponin I and impaired relaxation **result in** **diastolic dysfunction and contractile impairment**.
7. Chronic contractile/proteostatic stress **leads to** **myocyte hypertrophy, myocardial fibrosis, and (in neonates) a dilated-to-hypertrophic transition** → clinical **HCM/DCM, apical aneurysm, arrhythmia, heart failure, and SCD risk**.

*Branch:* In the **neonatal biallelic** context, the initial manifestation is often **dilated cardiomyopathy that subsequently transitions to hypertrophy** — a developmentally distinct branch, consistent with ALPK3's essential role in early cardiomyocyte differentiation ([PMID: 26846950](https://pubmed.ncbi.nlm.nih.gov/26846950/); [PMID: 32480058](https://pubmed.ncbi.nlm.nih.gov/32480058/)).

*Inferred vs. demonstrated:* Steps 2–5 are **directly demonstrated** in iPSC-CM/ESC-CM models and mouse knock-ins (PMID 27106955, 40128237, 40135575). The downstream fibrosis/arrhythmia/SCD steps (step 7) are **inferred** from clinical cohorts and general HCM pathophysiology.

### Supporting detail

**Molecular pathways & protein dysfunction.** ALPK3 is a **catalytically-dead M-band scaffold** (Finding F002): *"ALPK3 lacks catalytic activity and maintains sarcomeric proteostasis by scaffolding MYOMs (myomesins), MuRF (muscle ring-finger protein) E3 ligases, and SQSTM1 (sequestosome-1)/p62. Loss of this scaffolding function displaces MYOMs, drives thick-filament protein aggregation, and precipitates severe contractile dysfunction"* ([PMID: 41221624](https://pubmed.ncbi.nlm.nih.gov/41221624/)). The relevant pathway is **sarcomere/myofilament assembly and the ubiquitin–proteasome/autophagy quality-control system** (MuRF ligases, p62). The founding study additionally described ALPK3 as a **nuclear kinase essential for early cardiomyocyte differentiation** ([PMID: 26846950](https://pubmed.ncbi.nlm.nih.gov/26846950/)), and the α-kinase-3 mouse work supports **a scaffold model recruiting machinery for thick-filament protein turnover** ([PMID: 40135575](https://pubmed.ncbi.nlm.nih.gov/40135575/)).

**Cellular processes.** Disrupted **sarcomeric proteostasis, autophagy/protein turnover, and calcium homeostasis** in cardiomyocytes. Ultrastructural evidence: *"Ultra-structural analysis of cardiomyocytes derived from patient-specific and human ESC-derived stem cell lines lacking ALPK3 revealed disordered sarcomeres and intercalated discs"* ([PMID: 27106955](https://pubmed.ncbi.nlm.nih.gov/27106955/)).

**Metabolic/biochemical abnormalities.** Reduced SRX myosin fraction (an energy-conserving myosin state), elevated diastolic calcium, and reduced PKA-mediated troponin I phosphorylation — collectively producing **hypercontractility and impaired relaxation** ([PMID: 40128237](https://pubmed.ncbi.nlm.nih.gov/40128237/)).

**Tissue damage.** Chronic myofibrillar stress → **myocardial fibrosis** (prominent LGE), apical aneurysm formation, and arrhythmogenic substrate.

**Suggested ontology terms.**
- GO biological process: sarcomere organization (GO:0045214); myofibril assembly (GO:0030239); cardiac muscle hypertrophy (GO:0003300); regulation of protein catabolic process (GO:0042176); regulation of the force of heart contraction (GO:0002026); cardiac muscle cell differentiation (GO:0055007).
- GO cellular component: M band (GO:0031430); sarcomere (GO:0030017); myofibril (GO:0030016); nucleus (GO:0005634).
- CL cell types: cardiac muscle cell / cardiomyocyte (CL:0000746); regular cardiac myocyte (CL:0002098).

---

## 7. Anatomical Structures Affected

**Organ level.** Primary organ: the **heart** (UBERON:0000948), specifically the **cardiac ventricles** — left ventricle (UBERON:0002084) with frequent **apex** and **interventricular septum** involvement, and **right ventricle** (UBERON:0002080) in the heterozygous form. Secondary involvement: **cardiac atria** (atrial fibrillation), pulmonary/systemic circulation via heart failure. Body system: **cardiovascular system** (UBERON:0004535). In the biallelic syndromic form, additional systems affected: **musculoskeletal system** (skeleton, thoracic cage), **craniofacial structures** (palate), and skeletal/integumentary features (short stature, joint contractures).

**Tissue and cell level.** **Cardiac (striated) muscle tissue** (UBERON:0001133); target cell = **cardiomyocyte** (CL:0000746). Fibrosis reflects **cardiac fibroblast** (CL:0002548) activation and extracellular matrix expansion.

**Subcellular level.** The **sarcomeric M-band** (GO:0031430) is the primary locus of dysfunction, with secondary involvement of the **sarcomere/myofibril** (GO:0030017), and **nucleus** (GO:0005634, reflecting ALPK3's reported nuclear localization and differentiation role).

**Localization / lateralization.** Cardiac involvement is **biventricular/bilateral** with a characteristic **apical predilection** in heterozygotes; hypertrophy may be asymmetric (septal) or concentric/apical.

---

## 8. Temporal Development

**Onset.**
- **Biallelic (recessive):** **congenital/prenatal to neonatal/early-childhood** onset; acute and severe.
- **Heterozygous (dominant):** **adult-onset**, insidious/chronic; onset delayed by ~10 years relative to sarcomeric-gene-positive HCM ([PMID: 41645375](https://pubmed.ncbi.nlm.nih.gov/41645375/)).

**Progression.**
- Biallelic disease is **rapidly progressive**; three founding-cohort patients died of heart failure within the first week of life ([PMID: 26846950](https://pubmed.ncbi.nlm.nih.gov/26846950/)). A characteristic **neonatal DCM → ventricular hypertrophy transition** occurs in ~44% of live-born biallelic patients ([PMID: 32480058](https://pubmed.ncbi.nlm.nih.gov/32480058/)).
- Heterozygous disease is **slowly progressive/chronic-lifelong**, with left ventricular wall thickness positively correlating with age (notably in female patients).

**Patterns.** Disease is **progressive, not relapsing-remitting**; no spontaneous remission. **Critical windows:** the perinatal period (biallelic lethality) and adult mid-life (penetrance onset in heterozygotes) represent the key vulnerability windows and — for preclinical gene/pharmacotherapy — potential intervention windows.

---

## 9. Inheritance and Population

**Inheritance — dual.** ALPK3 shows **both recessive (biallelic) and dominant (heterozygous truncating)** disease mechanisms, now formally recognized by ClinGen (Finding F010): *"Existing genes were curated for new inheritance patterns where evidence existed"* ([PMID: 39971408](https://pubmed.ncbi.nlm.nih.gov/39971408/)). ALPK3 carries **established (definitive/strong/moderate) gene–disease validity for HCM**.

**Penetrance & expressivity.** Heterozygous penetrance is **incomplete and age-dependent** — **~20% (2 of 10 heterozygous family members)** in the founding family ([PMID: 26846950](https://pubmed.ncbi.nlm.nih.gov/26846950/)); later cohorts suggest even lower penetrance. Expressivity is **variable**, with identical variants producing severe obstructive HCM in one relative and no phenotype in another ([PMID: 41645375](https://pubmed.ncbi.nlm.nih.gov/41645375/)).

**Epidemiology.** No ALPK3-specific prevalence figure exists. Contextually, **HCM affects ~1 in 500** ([PMID: 39971408](https://pubmed.ncbi.nlm.nih.gov/39971408/); [PMID: 39132495](https://pubmed.ncbi.nlm.nih.gov/39132495/)), and heterozygous ALPK3tv account for **~1–4% of adult HCM**, giving a rough order-of-magnitude estimate. In apical HCM specifically, ALPK3 is over-represented: **28.6% of genotype-positive apical HCM** in a Swedish cohort (2nd most common after MYH7) ([PMID: 40428316](https://pubmed.ncbi.nlm.nih.gov/40428316/)).

**Founder effects / consanguinity.** The recessive form was first identified in **consanguineous families** via homozygosity mapping ([PMID: 26846950](https://pubmed.ncbi.nlm.nih.gov/26846950/)); consanguinity elevates biallelic risk. No specific founder variants are broadly established.

**Sex ratio.** **Male predominance** among heterozygous ALPK3tv HCM patients ([PMID: 41645375](https://pubmed.ncbi.nlm.nih.gov/41645375/)).

**Carrier frequency.** Heterozygous truncating ALPK3 variants are present at low frequency in gnomAD; precise carrier frequencies are population-dependent.

---

## 10. Diagnostics

**Imaging (cornerstone).**
- **Echocardiography** — detects ventricular hypertrophy, apical morphology, systolic/diastolic dysfunction, outflow obstruction.
- **Cardiac MRI (CMR) with late gadolinium enhancement (LGE)** — critical for detecting **apical aneurysm, RV involvement, and fibrosis burden**, all characteristic of ALPK3 HCM, and central to SCD risk stratification (Finding F006). *"Late gadolinium enhancement (LGE) was present in 80% of patients and LGE% independently predi[cted events]"* ([PMID: 41759724](https://pubmed.ncbi.nlm.nih.gov/41759724/)). Combined markers stratify risk: *"Patients with LVWT ≥30 mm and LGE ≥15% had a greater risk of SCD (subdistribution hazard ratio, 5.60; 95% confidence interval, 1.90-16.5, P = .002)"* ([PMID: 40317285](https://pubmed.ncbi.nlm.nih.gov/40317285/)).

**Electrophysiology.** **ECG** shows left ventricular hypertrophy patterns (more prevalent in ALPK3tv than sarcomeric HCM); Holter monitoring detects AF and NSVT.

**Genetic testing (definitive for etiology).**
- **Whole-exome sequencing (WES)** and **whole-genome sequencing (WGS)** are the primary discovery tools and identified nearly all reported variants.
- **HCM/cardiomyopathy gene panels** should **include *ALPK3***; historically ALPK3 was omitted or mis-annotated as recessive-only, causing missed diagnoses — periodic **re-analysis/re-annotation** is essential ([PMID: 41645375](https://pubmed.ncbi.nlm.nih.gov/41645375/)).
- **Single-gene / targeted testing** and **cascade family testing** for known variants; **trio segregation (Sanger)** to establish compound-heterozygous configuration in pediatric cases ([PMID: 40447126](https://pubmed.ncbi.nlm.nih.gov/40447126/)).
- **Chromosomal microarray** may be needed to detect contiguous 15q25 deletions (PMID 37671554).

**Clinical criteria & differential diagnosis.** Diagnosis follows standard HCM criteria (unexplained LV wall thickness ≥15 mm, or ≥13 mm with family history). Differential diagnosis includes sarcomeric HCM (MYH7, MYBPC3), infiltrative/storage cardiomyopathies (Fabry, amyloid), athlete's heart, and syndromic causes (RASopathies) — especially relevant given the extracardiac features of the biallelic form.

**Screening.** **Cascade genetic and clinical (imaging) screening** of at-risk relatives; prenatal/reproductive counseling for consanguineous families at risk of biallelic disease.

---

## 11. Outcome / Prognosis

**Biallelic (recessive) form:** **Poor prognosis** — severe, often lethal in utero, at birth, or in early childhood; heart transplantation, refractory heart failure, and cardiac arrest are reported outcomes; several founding-cohort neonates died within the first week of life ([PMID: 26846950](https://pubmed.ncbi.nlm.nih.gov/26846950/); [PMID: 38356193](https://pubmed.ncbi.nlm.nih.gov/38356193/)).

**Heterozygous (dominant) form:** **Variable, generally more favorable but with meaningful arrhythmic risk.** In the apical HCM cohort where ALPK3 is prominent, **36.2% experienced HCM-related events**, apical aneurysm occurred in **17.2%**, AF in **41.4%**, and NSVT in **29.3%** ([PMID: 40428316](https://pubmed.ncbi.nlm.nih.gov/40428316/)).

**Prognostic factors.** **LV wall thickness, LGE burden/fibrosis, apical aneurysm, and NSVT** are the principal risk markers for SCD. Guideline-based SCD risk algorithms have modest discriminatory power (AUC ~0.58–0.63; [PMID: 39713197](https://pubmed.ncbi.nlm.nih.gov/39713197/)), and there is **low inter-guideline agreement** for primary-prevention ICD recommendations (Fleiss' kappa 0.340; [PMID: 39557320](https://pubmed.ncbi.nlm.nih.gov/39557320/)) — reinforcing the value of **CMR-LGE** as an additional stratifier for the fibrosis-prone ALPK3 phenotype.

**Complications.** Heart failure, atrial and ventricular arrhythmias, thromboembolism (AF), apical aneurysm with thrombus, and sudden cardiac death.

---

## 12. Treatment

There is **no ALPK3-specific approved therapy**; management follows **standard HCM guidelines**, with genotype-directed therapies in preclinical development.

**Pharmacotherapy (guideline HCM care; NCIT terms suggested).**
- **Beta-adrenergic blockers** (NCIT:C2496) — first-line for symptoms/obstruction.
- **Non-dihydropyridine calcium-channel blockers** (e.g., verapamil).
- **Disopyramide** — for obstruction.
- Standard heart-failure therapy for the DCM/systolic-dysfunction phenotype.
- **Anticoagulation** for AF.

**Genotype-directed / advanced therapeutics (preclinical proof-of-concept; Finding F003).**
- **Mavacamten** (cardiac myosin inhibitor; NCIT:C171741) — *"Contractile and calcium handling defects were partly corrected by treatment with mavacamten, a novel myosin inhibitor"* ([PMID: 40128237](https://pubmed.ncbi.nlm.nih.gov/40128237/)). Targets the hypercontractility/SRX defect central to ALPK3 pathophysiology.
- **AAV-based gene replacement therapy** — *"durable phenotypic rescue in global knockout mice using an adeno-associated virus"* delivering ALPK3 ([PMID: 41221624](https://pubmed.ncbi.nlm.nih.gov/41221624/)). Directly addresses the LoF mechanism.
- **miR-384-5p modulation** — a candidate therapeutic axis based on amelioration of pressure-overload hypertrophy via the ALPK3 pathway ([PMID: 35510648](https://pubmed.ncbi.nlm.nih.gov/35510648/)).

**Surgical / interventional.**
- **Septal reduction therapy** — surgical **septal myectomy** (NCIT:C51899) or **alcohol septal ablation** for obstruction.
- **Implantable cardioverter-defibrillator (ICD)** (NCIT:C50077) for primary/secondary SCD prevention, guided by CMR-LGE-informed risk stratification.
- **Heart transplantation** (NCIT:C15328) for end-stage disease (used in severe pediatric/biallelic cases).

**Supportive care.** Symptom management, exercise counseling, arrhythmia management, and heart-failure supportive therapy.

---

## 13. Prevention

**Primary prevention.** Because ALPK3 cardiomyopathy is monogenic, primary prevention is **reproductive/genetic**: carrier identification, **genetic counseling** (especially for consanguineous couples at risk of biallelic disease), and reproductive options including **preimplantation genetic testing (PGT)** and prenatal diagnosis.

**Secondary prevention.** **Cascade genetic testing** and **serial clinical/imaging surveillance** of at-risk relatives to detect subclinical disease early — important given incomplete, age-dependent penetrance. Periodic re-analysis of previously "negative" HCM genetic tests to capture ALPK3 as knowledge of its dominant mechanism has matured ([PMID: 41645375](https://pubmed.ncbi.nlm.nih.gov/41645375/)).

**Tertiary prevention.** Prevention of complications in diagnosed patients: **ICD for SCD prevention** (CMR-LGE-informed), anticoagulation for AF-related thromboembolism, heart-failure management, and activity modification.

**Counseling.** Genetic counseling should address **dual inheritance** — recessive risk in consanguineous unions and dominant, incompletely penetrant risk for offspring of heterozygotes.

No immunization or public-health/environmental prevention is applicable (non-infectious, non-environmental disease).

---

## 14. Other Species / Natural Disease

**Taxonomy & orthologs.** ALPK3 is highly conserved. **Mouse *Alpk3*** (NCBI Gene 116904; *Mus musculus*, NCBI Taxon 10090) is the principal experimental ortholog. Human *ALPK3* is NCBI Gene 57538 (*Homo sapiens*, NCBI Taxon 9606). The gene was originally described as *Midori*, a differentiation-associated cardiac gene.

**Natural disease in other species.** No well-characterized naturally occurring ALPK3 cardiomyopathy in companion animals or wildlife is documented in the reviewed literature (no OMIA entry established in this investigation). Disease knowledge derives from **engineered** rather than spontaneous animal models.

**Comparative biology & conservation.** The **M-band scaffold function and requirement for cardiac function are evolutionarily conserved** — mouse knockouts recapitulate neonatal and adult cardiac dysfunction ([PMID: 40135575](https://pubmed.ncbi.nlm.nih.gov/40135575/)), supporting conserved disease mechanisms across mammals.

**Transmission.** Not applicable — genetic, non-zoonotic, non-transmissible.

---

## 15. Model Organisms

ALPK3 cardiomyopathy is supported by a **robust set of complementary models** spanning mouse and human cellular systems.

| Model | Type | Key features | Reference |
|-------|------|--------------|-----------|
| *Alpk3* global knockout mouse | Mammalian, constitutive KO | Neonatal and adult cardiac dysfunction; scaffold model for thick-filament turnover; **AAV-ALPK3 rescue** | [PMID: 40135575](https://pubmed.ncbi.nlm.nih.gov/40135575/); [PMID: 41221624](https://pubmed.ncbi.nlm.nih.gov/41221624/) |
| Inducible cardiac-specific *Alpk3* KO | Mammalian, conditional | Dissects neonatal vs. adult requirement for ALPK3 | [PMID: 40135575](https://pubmed.ncbi.nlm.nih.gov/40135575/) |
| K201X (truncation) knock-in mouse | Mammalian, knock-in | Reduced SRX myosin, elevated diastolic Ca²⁺, reduced PKA-cTnI phosphorylation; **partial mavacamten rescue** | [PMID: 40128237](https://pubmed.ncbi.nlm.nih.gov/40128237/) |
| Patient-derived iPSC-cardiomyocytes | In vitro, human | Disordered sarcomeres/intercalated discs; abnormal calcium handling | [PMID: 27106955](https://pubmed.ncbi.nlm.nih.gov/27106955/) |
| ALPK3-mutant human ESC-derived CMs | In vitro, human | Establishes ALPK3 deficiency underlies familial cardiomyopathy | [PMID: 27106955](https://pubmed.ncbi.nlm.nih.gov/27106955/) |

**Phenotype recapitulation.** Models faithfully reproduce the **core cellular phenotype** (sarcomere disarray, thick-filament aggregation, calcium mishandling, hypercontractility) and the **age-staged cardiac dysfunction**. **Limitations:** models less completely capture the human **syndromic extracardiac features** (facial/skeletal/palate anomalies) and the **age-dependent incomplete penetrance** of the human heterozygous form. **Applications:** mechanism dissection (M-band proteostasis), developmental staging of ALPK3 requirement, and **preclinical testing of mavacamten and AAV gene therapy**.

---

## Mechanistic Model / Interpretation

```
   ALPK3 loss-of-function variant
   (biallelic = complete loss | heterozygous = haploinsufficiency)
                 |
                 v
   Loss of catalytically-dead M-band SCAFFOLD
                 |
                 v
   Failure to anchor MYOM1/2 + MuRF E3 ligases + p62/SQSTM1
                 |
                 v
   Impaired thick-filament protein turnover -> AGGREGATION
                 |
                 v
   Sarcomere + intercalated-disc DISARRAY
                 |
        +--------+---------------------------+
        v                                    v
  Ca2+ mishandling                   Reduced SRX myosin,
  (elevated diastolic Ca2+)          low PKA-cTnI phosphorylation
        |                                    |
        +----------------+-------------------+
                         v
              HYPERCONTRACTILITY + impaired relaxation
                         |
        +----------------+----------------------------+
        v (neonatal branch)                           v (adult branch)
  Dilated CM -> transition to                 Late-onset HCM: apical/septal
  hypertrophy; severe, often                  hypertrophy, apical aneurysm,
  lethal; +/- syndromic features              RV involvement, fibrosis
        |                                            |
        +----------------+---------------------------+
                         v
        Heart failure, arrhythmia (AF/NSVT), SCD risk
                         |
      Rescue points: mavacamten (hypercontractility),
                     AAV-ALPK3 (restores scaffold)
```

The unifying interpretation is that **ALPK3 is a structural (not enzymatic) linchpin of M-band proteostasis**, and disease severity scales with **residual ALPK3 dosage**. This single mechanism parsimoniously explains the entire clinical spectrum — from perinatal lethal recessive disease to penetrance-limited adult dominant HCM — and rationalizes two mechanistically distinct therapeutic strategies (myosin inhibition to relieve the downstream hypercontractile consequence; gene replacement to restore the upstream scaffold).

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|------|-----------------|---------------------|
| [26846950](https://pubmed.ncbi.nlm.nih.gov/26846950/) | Biallelic truncating mutations cause severe pediatric CM | **Founding study**: recessive causation, perinatal lethality, nuclear kinase role, ~20% heterozygote penetrance (F007) |
| [41221624](https://pubmed.ncbi.nlm.nih.gov/41221624/) | ALPK3 Cardiomyopathy: Integrative Review | Zygosity–severity relationship, M-band scaffold mechanism, AAV/mavacamten proof-of-concept (F001, F002, F003, F004) |
| [32480058](https://pubmed.ncbi.nlm.nih.gov/32480058/) | Expanding clinical/genetic spectrum | Neonatal DCM→hypertrophy transition (44.4%), adult heterozygous phenotypes (F001) |
| [27106955](https://pubmed.ncbi.nlm.nih.gov/27106955/) | ALPK3-deficient iPSC/ESC cardiomyocytes | Ultrastructural disarray, abnormal calcium handling (F002) |
| [40128237](https://pubmed.ncbi.nlm.nih.gov/40128237/) | ALPK3tv rescued by mavacamten | SRX/Ca²⁺ defects, partial mavacamten rescue (F003) |
| [40135575](https://pubmed.ncbi.nlm.nih.gov/40135575/) | ALPK3 essential for neonatal/adult cardiac function | Mouse KO models, scaffold-for-turnover model (Sections 6, 15) |
| [38356193](https://pubmed.ncbi.nlm.nih.gov/38356193/) | French multicentric cohort | 31 adults heterozygous, HCM main phenotype (26/31), 15% apical/concentric (F004) |
| [39606411](https://pubmed.ncbi.nlm.nih.gov/39606411/) / [40469041](https://pubmed.ncbi.nlm.nih.gov/40469041/) | Heterozygous ALPK3tv late-onset HCM | Apical involvement and apical aneurysm signature (F004, F008) |
| [30046096](https://pubmed.ncbi.nlm.nih.gov/30046096/) | Tunisian case, facio-thoraco-skeletal | Syndromic biallelic features, specific frameshift variant (F005) |
| [40447126](https://pubmed.ncbi.nlm.nih.gov/40447126/) | Compound-het pediatric HCM | Novel truncating variants, extracardiac features (F005) |
| [40428316](https://pubmed.ncbi.nlm.nih.gov/40428316/) | Swedish apical HCM cohort | ALPK3 = 2nd most common ApHCM genotype (28.6%), aneurysm 17.2% (F008) |
| [41645375](https://pubmed.ncbi.nlm.nih.gov/41645375/) | Chinese pedigree re-analysis | Dominant inheritance, delayed onset, male predominance, re-annotation importance (Sections 2, 8, 10) |
| [35510648](https://pubmed.ncbi.nlm.nih.gov/35510648/) | miR-384-5p protects via ALPK3 | Post-transcriptional regulation of ALPK3 pathway (F009) |
| [40317285](https://pubmed.ncbi.nlm.nih.gov/40317285/) | SCD prediction after myectomy | LVWT≥30 mm + LGE≥15% → HR 5.60 for SCD (F006) |
| [41759724](https://pubmed.ncbi.nlm.nih.gov/41759724/) | Risk stratification / LGE | LGE independent SCD predictor (F006) |
| [39713197](https://pubmed.ncbi.nlm.nih.gov/39713197/) | Guideline validation | Modest guideline discrimination (AUC 0.58–0.63) (Section 11) |
| [39557320](https://pubmed.ncbi.nlm.nih.gov/39557320/) | Guideline agreement | Low inter-guideline ICD agreement (kappa 0.340) (Section 11) |
| [39971408](https://pubmed.ncbi.nlm.nih.gov/39971408/) / [39132495](https://pubmed.ncbi.nlm.nih.gov/39132495/) | ClinGen HCM gene reappraisal | Dual-inheritance curation, HCM ~1 in 500 (F010) |
| 36660067 | Overlapping adult-onset phenotype | Restrictive/overlap phenotype, missense variants (Sections 3, 4) |
| 37671554 | Contiguous 15q25 deletion | Structural-variant biallelic mechanism (Section 4) |
| 33076350 | HCM + skeletal muscle features | Skeletal muscle involvement (Section 3) |

---

## Limitations and Knowledge Gaps

1. **No ALPK3-specific epidemiology.** Prevalence/incidence are inferred from HCM-wide figures (~1 in 500) and the ~1–4% ALPK3 contribution; no direct registry estimate exists.
2. **Penetrance uncertainty.** The ~20% figure derives from a single founding family; population-scale penetrance of heterozygous ALPK3tv is likely lower and imprecisely quantified. Modifier genes and gene–environment interactions remain unidentified.
3. **Therapies are preclinical.** Mavacamten rescue and AAV gene therapy are shown only in mouse/iPSC models; no human trials specific to ALPK3 exist. Standard HCM management is extrapolated, not ALPK3-validated.
4. **Mechanistic gaps.** The relative contributions of ALPK3's nuclear (differentiation) role versus its cytoplasmic M-band scaffold role are not fully resolved, and how catalytic-dead α-kinase architecture confers scaffolding specificity is incompletely defined.
5. **Extracardiac pathogenesis.** The mechanism linking ALPK3 loss to craniofacial/skeletal malformations in the biallelic form is unexplained.
6. **Variant interpretation.** Historical mis-annotation of ALPK3 as recessive-only led to under-diagnosis; many gene panels and archived tests may still under-call ALPK3.
7. **Model limitations.** Animal/cellular models under-represent the syndromic extracardiac phenotype and age-dependent adult penetrance.

---

## Proposed Follow-up Experiments / Actions

1. **Population penetrance study.** Leverage large biobanks (e.g., the biobank gene–disease association approach of PMID 41893039) to estimate age-specific penetrance and lifetime HCM risk for heterozygous ALPK3 truncating variants.
2. **Prospective natural-history registry.** Establish an ALPK3-specific longitudinal registry capturing apical aneurysm incidence, arrhythmia burden, LGE progression, and SCD to build an ALPK3-tailored risk model (given weak performance of generic guidelines).
3. **Clinical translation of genotype-directed therapy.** Advance AAV-ALPK3 gene replacement and evaluate mavacamten in ALPK3tv patients via biomarker-driven early-phase trials; define the therapeutic window (neonatal vs. adult).
4. **Modifier discovery.** GWAS/whole-genome and multi-omics analysis of penetrant vs. non-penetrant heterozygous carriers to identify genetic/epigenetic modifiers (including the miR-384-5p axis).
5. **Structural biology.** Determine the ALPK3 M-band interactome structure (with MYOM, MuRF, p62) via cryo-EM/AlphaFold-guided modeling to rationalize truncating-variant effects and design stabilizing therapeutics.
6. **Panel/curation updates.** Ensure all clinical HCM gene panels include ALPK3 with dual-inheritance interpretation, and systematically re-analyze archived "gene-negative" HCM cases.
7. **Mechanism of extracardiac disease.** Use conditional/humanized models to dissect the developmental basis of the syndromic facio-thoraco-skeletal features in biallelic disease.

---

*Report compiled from 5 investigation iterations, 10 confirmed findings, and 24 reviewed papers. Evidence types: human clinical cohorts and case reports, model-organism (mouse) studies, in vitro human iPSC/ESC-cardiomyocyte studies, and expert-panel gene curation.*


## Artifacts

- [OpenScientist final report](ALPK3-Related_Hypertrophic_Cardiomyopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ALPK3-Related_Hypertrophic_Cardiomyopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 23 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 29 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 15 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001639` (2 mentions) - the report calls it "Clinical sign", "apical variant"; HP calls it **Hypertrophic cardiomyopathy**
- `HP:0001644` (1 mention) - the report calls it "Clinical sign"; HP calls it **Dilated cardiomyopathy**
- `HP:0025169` (1 mention) - the report calls it "LV aneurysm"; HP calls it **Left ventricular systolic dysfunction**
- `HP:0001707` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Abnormal right ventricle morphology**
- `HP:0001637` (1 mention) - the report calls it "Laboratory/imaging"; HP calls it **Abnormal myocardium morphology**
- `HP:0005162` (1 mention) - the report calls it "Clinical sign"; HP calls it **Abnormal left ventricular function**
- `HP:0001723` (1 mention) - the report calls it "Clinical sign"; HP calls it **Restrictive cardiomyopathy**
- `HP:0005110` (1 mention) - the report calls it "Clinical sign"; HP calls it **Atrial fibrillation**
- `HP:0004758` (1 mention) - the report calls it "Clinical sign"; HP calls it **Effort-induced polymorphic ventricular tachycardia**
- `HP:0001645` (1 mention) - the report calls it "Clinical outcome"; HP calls it **Sudden cardiac death**
- `GO:0031430` (2 mentions) - the report calls it "GO cellular component: M band", "sarcomeric M-band"; GO calls it **M band**
- `NCIT:C2496` (1 mention) - the report calls it "Beta-adrenergic blockers"; NCIT calls it **Anti-VEGF Monoclonal Antibody**
- `NCIT:C51899` (1 mention) - the report calls it "septal myectomy", "Septal reduction therapy** — surgical **septal myectomy"; NCIT calls it **Radical Cystoprostatectomy**
- `NCIT:C50077` (1 mention) - the report calls it "Implantable cardioverter-defibrillator (ICD)"; NCIT calls it **Motor Device**
- `NCIT:C15328` (1 mention) - the report calls it "Heart transplantation"; NCIT calls it **Splenectomy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002803` (1 mention) - the report calls it "Joint contractures"; HP calls it **Congenital contracture**, and lists "congenital contractures" among its other names
- `GO:0045214` (1 mention) - the report calls it "GO biological process: sarcomere organization"; GO calls it **sarcomere organization**
- `GO:0030017` (2 mentions) - the report calls it "sarcomere/myofibril"; GO calls it **sarcomere**
- `CL:0000746` (2 mentions) - the report calls it "CL cell types: cardiac muscle cell / cardiomyocyte", "cardiomyocyte"; CL calls it **cardiac muscle cell**
- `UBERON:0001133` (1 mention) - the report calls it "Cardiac (striated) muscle tissue"; UBERON calls it **cardiac muscle tissue**, and lists "cardiac muscle muscle tissue" among its other names
- `CL:0002548` (1 mention) - the report calls it "cardiac fibroblast"; CL calls it **fibroblast of cardiac tissue**, and lists "cardiac fibroblast" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001639` - called "Clinical sign", "apical variant"
- `GO:0031430` - called "GO cellular component: M band", "sarcomeric M-band"
- `CL:0000746` - called "CL cell types: cardiac muscle cell / cardiomyocyte", "cardiomyocyte"
- `NCIT:C51899` - called "septal myectomy", "Septal reduction therapy** — surgical **septal myectomy"