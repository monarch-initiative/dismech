---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T06:10:32.669177'
end_time: '2026-09-03T06:26:55.770345'
duration_seconds: 983.1
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Brugada syndrome 7
  mondo_id: ''
  category: Genetic
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
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 31
  on_topic: 21
  validator_version: 0.2.1
term_validation:
  total_terms: 34
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 4
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0013481
    reported_labels:
    - brugada syndrome 7
    ontology_label: chromosome 13q14 deletion syndrome
  - term_id: HP:0031650
    reported_labels:
    - ECG sign
    ontology_label: Abnormal atrioventricular valve physiology
  - term_id: HP:0001279
    reported_labels:
    - Symptom
    ontology_label: Syncope
  - term_id: HP:0001645
    reported_labels:
    - Outcome
    ontology_label: Sudden cardiac death
  - term_id: HP:0005110
    reported_labels:
    - Clinical sign
    ontology_label: Atrial fibrillation
  - term_id: HP:0012722
    reported_labels:
    - ECG sign
    ontology_label: Heart block
  - term_id: NCIT:C50032
    reported_labels:
    - Implantable Cardioverter-Defibrillator
    ontology_label: Limiter Device
  - term_id: NCIT:C371
    reported_labels:
    - Isoproterenol
    ontology_label: Chromomycin Antineoplastic Antibiotic
  - term_id: NCIT:C99521
    reported_labels:
    - Catheter Ablation
    ontology_label: Percutaneous Coronary Intervention
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
  path: Brugada_Syndrome_7-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Brugada_Syndrome_7-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Brugada syndrome 7
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Brugada syndrome 7** covering all of the
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

# Brugada Syndrome 7 (BrS7): A Comprehensive Disease Characterization Report

**Disease:** Brugada syndrome 7 · **Gene:** *SCN3B* (Navβ3) · **OMIM:** #613120 · **Category:** Genetic (cardiac channelopathy)
**Evidence status:** *SCN3B* has "limited" gene–disease validity for Brugada syndrome (SCN5A is the sole "definitive" gene)

*Autonomous literature-based investigation. Evidence types are flagged as [human clinical], [in vitro], [model organism], [computational], or [database]. Where primary data specific to the SCN3B/BrS7 subtype are lacking, general Brugada-syndrome (BrS) evidence is used and labeled as such.*

---

## Summary

**Brugada syndrome 7 (BrS7; OMIM #613120) is a rare, autosomal-dominant cardiac sodium channelopathy attributed to loss-of-function variants in *SCN3B*, the gene encoding the auxiliary β3 subunit (Navβ3) of the cardiac voltage-gated sodium channel.** Mutant β3 fails to properly chaperone and modulate the pore-forming Nav1.5 (SCN5A) α-subunit, reducing its cell-surface expression and cardiac sodium current (I<sub>Na</sub>) [in vitro, PMID 23257389]. The reduced inward sodium current unmasks transient-outward-current (I<sub>to</sub>)-mediated repolarization heterogeneity in the right ventricular outflow tract (RVOT), which generates the diagnostic type-1 (coved) Brugada ECG pattern and creates a phase-2-reentry substrate for polymorphic ventricular tachycardia (VT), ventricular fibrillation (VF), and sudden cardiac death (SCD) [in vitro, PMID 24657694].

Clinically, BrS7 is indistinguishable from other Brugada subtypes. It presents predominantly in adult males (~95% male, mean age ~51 years), is unmasked or triggered by fever, sodium-channel-blocking drugs, enhanced vagal tone, and electrolyte imbalance, and is managed with implantable cardioverter-defibrillators (ICDs), quinidine, isoproterenol/adrenaline for electrical storms, epicardial RVOT substrate ablation, and trigger avoidance. There is no gene-specific therapy for the *SCN3B* subtype.

**A critical caveat governs the entire entity:** evidence-based gene-curation (ClinGen-style reappraisal by Hosseini et al., 2018) classified *SCN3B* as having only **"limited"** clinical validity for Brugada syndrome, with *SCN5A* being the only gene reaching "definitive" evidence [PMID 29959160]. Contemporary expert consensus reinforces that *SCN5A* "remains the sole gene with definitive disease association" and that BrS displays complex, oligogenic/polygenic inheritance [PMID 41738055]. BrS7 is therefore best regarded as a rare, disputed monogenic subtype nested within a broader genetic architecture. This report is compiled from aggregated disease-level resources (OMIM, HGNC, UniProt) and primary literature (human clinical cohorts, in-vitro electrophysiology, and a *Scn3b*-knockout mouse), not individual EHR data.

---

## Key Findings

### Finding 1 — BrS7 is caused by loss-of-function *SCN3B* variants that reduce cardiac sodium current via impaired Nav1.5 trafficking

BrS7 (OMIM #613120) is caused by heterozygous mutations in *SCN3B*, encoding the auxiliary β3 subunit (Navβ3) of the cardiac sodium channel. In the seminal functional study of the Japanese *SCN3B*-V110I variant, transfected cells showed decreased Nav1.5 cell-surface expression and significantly reduced sodium current — a clear loss-of-function effect. As the authors reported, *"The SCN3B mutation impaired the cytoplasmic trafficking of Nav1.5, the cell surface expression of which was decreased in transfected cells,"* and *"Whole-cell patch clamp recordings of the transfected cells revealed that the sodium currents were significantly reduced by the SCN3B mutation"* [in vitro, PMID 23257389]. A newly characterized in-frame deletion (p.T138del, 2025) confirms ongoing identification of BrS-associated *SCN3B* variants; the paper *"identify and characterise a novel SCN3B variant encoding the regulatory β3-subunit of the cardiac voltage-gated sodium channel"* [human/in vitro, PMID 39761910]. This establishes the core molecular lesion: reduced I<sub>Na</sub> from a defective auxiliary subunit.

### Finding 2 — *SCN3B* is a rare cause of SCN5A-negative Brugada syndrome (~1.7% in a Japanese cohort)

Among 181 unrelated SCN5A-negative BrS patients (178 Japanese, 3 Korean), the *SCN3B* Val110Ile variant was found in only 3 of 178 (1.7%) Japanese patients and was absent from 480 Japanese controls: *"A mutation, Val110Ile, was identified in 3 of 178 (1.7%) Japanese patients, but was not found in 480 Japanese controls"* [human, PMID 23257389]. Set against the broader diagnostic landscape — *"A pathogenic/likely pathogenic variant can be found in 20% to 25% of patients with Brugada syndrome (BrS) and a pathogenic/likely pathogenic variant in SCN5A is associated with a worse prognosis"* [human clinical, PMID 38426305] — *SCN3B* accounts for a small fraction of the minor BrS genes.

### Finding 3 — The *Scn3b*-knockout mouse recapitulates conduction slowing and atrial arrhythmia susceptibility

*Scn3b(−/−)* mice showed slower heart rates, longer P-wave durations, and prolonged PR intervals versus wild-type, plus abnormal atrial electrophysiology and inducible atrial tachycardia/fibrillation on burst pacing. As reported, *"Lead I electrocardiograms from Scn3b(-/-) mice showed slower heart rates, longer P wave durations and prolonged PR intervals than WT hearts,"* and *"Atrial burst pacing protocols induced atrial tachycardia and fibrillation in all Scn3b(-/-) but hardly any WT hearts"* [model organism, PMID 19796257]. Because *Scn1b* and *Scn5a* mRNA were unchanged, the phenotype is attributable specifically to β3 loss.

### Finding 4 — The BrS arrhythmia substrate arises from RVOT epicardial repolarization heterogeneity and concealed phase-2 reentry

In coronary-perfused canine RV wedge preparations pharmacologically mimicking the BrS genotype (I<sub>to</sub>-agonist NS5806 + Ca-channel blocker verapamil), *"Fractionated electrical activity was observed in RV epicardium, but not in endocardium, as a consequence of heterogeneities in the appearance of the second upstroke of the epicardial action potential, and discrete high-frequency spikes developed as a result of concealed phase 2 re-entry"* [in vitro, PMID 24657694]. Contemporary consensus reframes BrS as a microstructural–electrical continuum: *"BrS, once viewed as a purely electrical disorder, is now recognized along a microstructural-electrical continuum, with sodium-channel dysfunction and subtle epicardial fibrosis of the right ventricular outflow tract as key contributors"* [human clinical, PMID 41738055].

### Finding 5 — Fever, sodium-channel-blocking drugs, vagal tone, and electrolyte imbalance unmask the type-1 pattern and trigger arrhythmias

Fever is a well-established trigger that unmasks the coved type-1 ECG and precipitates VF, including as a first manifestation across ages. Reviews list precipitating factors succinctly: *"Brugada syndrome could be precipitated by various factors, such as fever, electrolyte imbalances, and drugs"* [human clinical, PMID 42411811], and *"Fever is a well-known trigger for malignant ventricular arrhythmias in predisposed patients"* [human clinical, PMID 42200267]. This is the paradigmatic gene–environment interaction of the disease.

### Finding 6 — Management centers on ICD and quinidine, with epicardial RVOT substrate ablation as an emerging therapy

*"For decades, treatment centered on implantable cardioverter-defibrillators and quinidine, both limited by availability, tolerance, and device complications. More recently, epicardial substrate ablation has emerged as a transformative therapy"* [human clinical, PMID 41738055]. Quinidine efficacy is quantified in an Israeli survey with *"inducible ventricular fibrillation (VF) in 10, which was prevented by quinidine in 9/10 patients"* [human clinical, PMID 29761670]. There is no gene-specific therapy for SCN3B-related BrS7.

### Finding 7 — BrS is strongly male-predominant with mid-adult presentation; *SCN5A* is the only definitively validated gene

Large Japanese prospective registries report cohorts of ~95% men with mean age ~51 years: *"We analyzed 510 patients with BrS (mean age 51 ± 14 years; 95% men)"* [human clinical, PMID 41819241]. Expert consensus states *"SCN5A remains the sole gene with definitive disease association, while polygenic susceptibility materially modulates risk, underscoring complex inheritance"* [human clinical, PMID 41738055] — implying minor genes including *SCN3B* have limited monogenic validity.

### Finding 8 — *SCN3B* has only LIMITED clinical validity as a Brugada syndrome gene

In the evidence-based reappraisal of BrS genes (ClinGen-style semiquantitative scoring, three independent curation teams + clinical domain expert panel), *"Of 21 genes curated for clinical validity, biocurators classified only 1 gene (SCN5A) as definitive evidence, whereas all other genes were classified as limited evidence"* [computational/curation, PMID 29959160]. *SCN3B* (the basis of the BrS7/#613120 designation) falls among the limited-evidence genes.

### Finding 9 — *SCN3B* loss-of-function variants also cause early-onset lone atrial fibrillation (an allelic phenotype)

Olesen et al. sequenced *SCN3B* in 192 unrelated lone AF patients and found three non-synonymous mutations (R6K, L10P, M161T), absent from 432 control alleles, all affecting conserved residues: *"The three mutations in SCN3B were investigated electrophysiologically and all led to loss of function in the sodium current, supporting the hypothesis that decreased sodium current enhances AF suscepti[bility]"* [in vitro/human, PMID 21051419]. Separately, GATA4-regulated 5′UTR/promoter *SCN3B* variants were linked to lone AF via a gain-of-function increase in expression [in vitro, PMID 36362949], illustrating context-dependent directionality.

### Finding 10 — Diagnosis rests on the type-1 ECG (spontaneous or drug-provoked) and the Shanghai score

Diagnosis requires a coved-type (type-1) ST-elevation ECG in leads V1–V2, spontaneous or unmasked by sodium-channel-blocker provocation (ajmaline/flecainide). A large drug-provocation study *"involved 698 patients with drug-induced type 1 BrS, confirmed via pharmacologic challenge (flecainide or ajmaline), from 21 centers in Italy and Switzerland"* [human clinical, PMID 40996547]. In that cohort, *"SCN5A pathogenic variants were a significant predictor of primary endpoint in the possible BrS group (OR: 12.5)"* — showing *SCN5A*, not minor genes like *SCN3B*, drives prognostic weight.

### Finding 11 — *SCN3B* encodes Navβ3, a single-pass glycoprotein with an extracellular Ig domain that chaperones and modulates Nav1.5

*SCN3B* (HGNC:10592; gene OMIM 608214; 11q24.1; UniProt Q9NY72) encodes an auxiliary single-transmembrane protein with an extracellular immunoglobulin (Ig)-like fold and short intracellular tail. It associates non-covalently with Nav1.5, modulating gating and promoting surface trafficking. Reports confirm *"the VGSC β3 subunit (the product of SCN3B gene)... its extracellular immunoglobulin domain (β3 Ig)"* [in vitro, PMID 40245999] and that *"a mutation in SCN3B for a small subunit of sodium channel, Navβ3, has been recently reported"* [in vitro, PMID 23257389].

---

## Section-by-Section Characterization

### 1. Disease Information

BrS7 is a genetic subtype of Brugada syndrome — a primary inherited arrhythmia syndrome characterized by ST-segment elevation in the right precordial ECG leads (V1–V2) and increased SCD risk in a structurally near-normal heart.

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #613120 (Brugada syndrome 7) |
| Gene / Gene OMIM | *SCN3B* / *608214 |
| MONDO (suggested) | MONDO:0013481 (brugada syndrome 7) |
| Orphanet | ORPHA:130 (parent entity; no separate subtype code) |
| ICD-10 / ICD-11 | I49.8 / BC65.0 (Brugada syndrome) |
| MeSH | D053840 (Brugada Syndrome) |
| HGNC / UniProt | HGNC:10592 / Q9NY72 |
| NCBI Gene / Ensembl | 55800 / ENSG00000149575 |
| Cytoband | 11q24.1 |

**Synonyms:** Brugada syndrome type 7; BRGDA7; SCN3B-related Brugada syndrome. Historical/allelic clinical descriptors: sudden unexplained nocturnal death syndrome (SUNDS), "Lai Tai," "Bangungut" [human clinical, PMID 24529773]. **Data provenance:** aggregated disease-level resources plus individual case reports and small functional studies (subtype-specific evidence is sparse).

### 2. Etiology

**Primary cause (genetic):** heterozygous variants in *SCN3B* (Navβ3) [PMID 23257389; 39761910]. **Genetic risk factors:** V110I (recurrent in Japan), L10P, T138del, A195T (VUS); polygenic background near *SCN5A-SCN10A* and *HEY2* modulates risk [PMID 41738055; 41458990]. **Environmental triggers** (unmask rather than cause): fever (most important), sodium-channel-blocking drugs, propofol/local anaesthetics, enhanced vagal tone, electrolyte abnormalities, alcohol, cocaine, and male sex [PMID 42411811; 42200267; 41819241]. **Protective factors:** no validated protective allele; trigger avoidance (aggressive fever control, avoiding contraindicated drugs) is the principal modifiable protection; female sex/older age associate with lower event rates [PMID 40130219]. **Gene–environment interaction:** the temperature-sensitive mutant channel loses further function during fever, deepening the epicardial repolarization gradient [PMID 42200267].

### 3. Phenotypes

| Phenotype | Type | HPO (suggested) | Onset / severity / frequency |
|---|---|---|---|
| Type-1 coved ST elevation V1–V2 | ECG sign | HP:0031650 | Adult; hallmark; may be intermittent/concealed |
| Syncope | Symptom | HP:0001279 | ~20–30%; episodic |
| Ventricular fibrillation / polymorphic VT | Clinical sign | HP:0001663 / HP:0004756 | Severe; life-threatening; often nocturnal |
| Sudden cardiac death / aborted arrest | Outcome | HP:0001645 | Mean ~40 yr; may be first manifestation |
| Atrial fibrillation (allelic) | Clinical sign | HP:0005110 | Common comorbidity; prominent for *SCN3B* |
| Conduction abnormality (↑PR/P-wave) | ECG sign | HP:0012722 | Consistent with reduced I<sub>Na</sub> |
| Palpitations / dizziness | Symptom | HP:0001962 / HP:0002321 | Presenting complaint in an SCN3B case |

**Onset:** predominantly adult (3rd–5th decade); pediatric and elderly first presentations occur. **Severity/progression:** highly variable and episodic; most carriers asymptomatic; risk lifelong. **QoL impact:** anxiety about SCD, activity/occupational restrictions, ICD-related psychological burden and inappropriate shocks (ICD complications ~20% in a pediatric cohort) [PMID 31748893]. No disease-specific QoL instrument; generic EQ-5D/SF-36 apply.

### 4. Genetic / Molecular Information

**Causal gene:** *SCN3B* (Navβ3). **Reported variants (germline, heterozygous):**

| Variant | Type | Functional consequence | Notes |
|---|---|---|---|
| c.328G>A p.Val110Ile | Missense | Loss of function; ↓Nav1.5 surface, ↓I<sub>Na</sub> | 3/178 (1.7%) Japanese BrS; absent in 480 controls |
| p.Thr138del | In-frame deletion | Disrupted function; normal surface expression | Novel 2025 report; implies gating mechanism |
| p.Leu10Pro / R6K / M161T | Missense | Loss of function | Reported in lone AF & BrS spectrum |
| p.Ala195Thr | Missense | VUS | SUNDS cohort |
| c.-324C>A / c.-303C>T (5′UTR) | Regulatory | Gain of function (↑expression) | GATA4-dependent; AF context |

**ACMG classification:** most variants VUS/limited-evidence given disputed gene validity [PMID 29959160]. **Allele frequency:** rare/absent in controls (check gnomAD per variant). **Functional consequence:** predominantly loss of function; regulatory gain-of-function branch for AF [PMID 36362949]. **Modifier genes:** *SCN5A* genotype + polygenic background [PMID 41738055]. **Epigenetics:** GATA4 transcriptionally regulates *SCN3B* [PMID 36362949]; no disease-specific methylation signature or characteristic chromosomal abnormality.

### 5. Environmental Information

Sodium-channel-blocking drugs, anaesthetics (propofol, bupivacaine), cocaine, and certain tyrosine-kinase inhibitors can unmask the pattern (a Brugada phenocopy was reported with avapritinib during febrile illness) [PMID 42165456; 42411811]. Large meals, alcohol, and dehydration/electrolyte shifts provoke events. **Infectious agents:** none causative; febrile infections (any cause, e.g., influenza) are a major arrhythmic trigger by unmasking the type-1 pattern [PMID 42647943].

### 6. Mechanism / Pathophysiology

**Ordered causal chain (mutation → clinical manifestation):**

1. A heterozygous **SCN3B (Navβ3) variant** alters the auxiliary β3 subunit [DEMONSTRATED in vitro, PMID 23257389]. →
2. Mutant β3 **fails to chaperone/modulate Nav1.5**, *leading to* reduced Nav1.5 surface expression [DEMONSTRATED, PMID 23257389; 39761910]. →
3. This *results in* **reduced peak cardiac sodium current (I<sub>Na</sub>)** — a loss-of-function channelopathy [DEMONSTRATED by patch clamp, PMID 23257389]. →
4. Reduced I<sub>Na</sub> **allows the I<sub>to</sub>-mediated phase-1 notch to dominate the epicardial action potential**, most prominently in RVOT epicardium (highest I<sub>to</sub>), *leading to* loss of the AP dome at some sites [INFERRED from wedge models, PMID 24657694]. →
5. Heterogeneous dome loss **creates transmural/epicardial dispersion of repolarization**, *producing* the coved type-1 ST elevation and **concealed phase-2 reentry** [PMID 24657694]. →
6. Phase-2 reentry **triggers closely coupled premature beats initiating polymorphic VT/VF** [PMID 24657694]. →
7. VF *results in* syncope, aborted arrest, or **SCD** [PMID 41738055].
   - **Modulating branch:** fever / Na-blockers further reduce I<sub>Na</sub> at step 3 [PMID 42200267].
   - **Structural branch:** subtle RVOT epicardial fibrosis contributes (microstructural–electrical continuum) [PMID 41738055].
   - **Atrial branch:** the same reduced-I<sub>Na</sub> lesion promotes AF and conduction slowing [PMID 21051419; 19796257].

**Supporting detail.** *Molecular pathway/biochemical defect:* cardiac Nav (Nav1.5 + β subunits) dysfunction — an ion-channel defect, not metabolic/enzymatic. *Suggested GO:* GO:0005248 (voltage-gated sodium channel activity), GO:0086010 (membrane depolarization during action potential), GO:0001518 (voltage-gated sodium channel complex), GO:0086067 (bundle of His cell–Purkinje conduction), GO:0086091 (regulation of heart rate by cardiac conduction). *Protein dysfunction:* loss-of-function via impaired trafficking and altered gating; β3 uses its extracellular Ig domain for α-subunit interaction [PMID 40245999]. *Cell types (CL):* ventricular cardiomyocyte (CL:0002131), RVOT epicardial myocytes, Purkinje/conduction cells (CL:0000731/CL:0002068), SA-node cells (CL:1000488). *Immune/metabolic:* not primary. *Omics:* no established disease-specific transcriptomic/proteomic/metabolomic signature for BrS7.

### 7. Anatomical Structures Affected

- **Organ:** heart (UBERON:0000948); system: cardiovascular (UBERON:0004535).
- **Primary site:** RVOT / RV epicardium (UBERON:0004125; UBERON:0002082) — locus of the arrhythmic substrate [PMID 24657694]. Secondary: atria (UBERON:0002081) and conduction system (UBERON:0004146) — AF and conduction slowing.
- **Secondary organ:** brain (hypoxic-ischaemic injury from arrest) — a complication.
- **Tissue/cell:** cardiac muscle tissue (working ventricular/atrial + conduction myocytes); limited epicardial fibrosis (connective).
- **Subcellular (GO CC):** plasma membrane/sarcolemma, intercalated disc (GO:0014704), voltage-gated sodium channel complex (GO:0001518), endoplasmic reticulum (trafficking, GO:0005783).
- **Lateralization:** predominantly right-sided (RVOT); biventricular substrate can occur [PMID 42359113].

### 8. Temporal Development

Congenital genetic defect but clinically **adult-onset** (mean event age ~40 yr; late presentation to the 8th decade under febrile stress) [PMID 42200267]. Arrhythmia onset is acute/episodic (often at rest/sleep). The ECG substrate is chronic/lifelong; arrhythmic risk is episodic, not progressive; no defined "stages." Event incidence ~1.5%/yr (non-elderly) vs ~0.7%/yr (elderly) [PMID 40130219]. Critical vulnerable windows: febrile illness and administration of contraindicated drugs.

### 9. Inheritance and Population

**Epidemiology (BrS overall):** prevalence ~1 in 2,000–5,000, higher in Southeast/East Asia; BrS7/*SCN3B* is very rare (isolated families/probands). **Inheritance:** autosomal dominant with incomplete, age-dependent penetrance and variable expressivity [PMID 41458990]. **Founder effects/consanguinity:** none established; V110I recurs in Japan without a defined founder haplotype. **Carrier frequency:** not defined; individual variants rare in gnomAD. **Demographics:** strong male predominance (~8–9:1; ~95% men), attributed to testosterone-dependent I<sub>to</sub>; mean age ~51 yr [PMID 41819241; 40130219]; geographic skew toward Asian populations.

### 10. Diagnostics

Cornerstone: spontaneous or drug-provoked **type-1 coved ST-elevation ≥2 mm in ≥1 right precordial lead (V1–V2)**, including high lead placement [PMID 41738055]. Provocation with ajmaline/flecainide unmasks concealed cases (ajmaline positive in 76% of a suspected pediatric cohort) [PMID 42669184; 40996547]. **Shanghai Score System** integrates ECG, symptoms, family history, and genetics (≥3.5 = probable/definite) [PMID 40996547]; multiparametric models (Sieira, Brugada-Risk, PAT) [PMID 40314213]. **Genetic testing:** multigene NGS panel/WES including *SCN5A*, *SCN1B–4B* (incl. *SCN3B*), etc.; *SCN5A* highest-yield/most actionable, *SCN3B* findings usually VUS; overall P/LP yield ~20–25% [PMID 38426305]; cascade familial testing recommended [PMID 26230511]. **Imaging:** echo/CMR to exclude structural disease (ARVC, scar) [PMID 42359113]. **Biomarkers/omics:** none established. **Differential diagnosis:** Brugada phenocopies (fever, hyperkalaemia, ischemia, drugs), ARVC, early repolarization syndrome, RVOT-VT, athlete's ECG, atypical RBBB [PMID 42359113; 25548613]. **Screening:** no newborn/population screening; cascade ECG + genetic screening of first-degree relatives.

### 11. Outcome / Prognosis

Principal risk is SCD from VF; annual major-arrhythmic-event rate ~1.5%/yr (non-elderly) vs ~0.7%/yr (elderly), ~11% over long follow-up [PMID 40130219; 41819241]. **Higher-risk factors:** prior aborted arrest/VF, arrhythmic syncope, spontaneous (vs drug-induced) type-1 ECG, notched P wave/atrial conduction delay, *SCN5A* pathogenic variant; asymptomatic patients are lower-risk [PMID 41819241; 40996547]. *SCN3B* genotype is not an established independent prognostic marker. **Morbidity:** VF-related anoxic injury, ICD complications (inappropriate shocks, lead failure ~20% pediatric), electrical storms, AF [PMID 31748893]. **Life expectancy:** near-normal if high-risk individuals are protected (ICD) and triggers avoided; chronic/lifelong without cure.

### 12. Treatment

*Genotype-agnostic; no SCN3B-specific therapy.*

| Modality | Agent/procedure | Mechanism | Suggested NCIT |
|---|---|---|---|
| Device | **ICD** (transvenous/subcutaneous) | Terminates VF; SCD prevention | Implantable Cardioverter-Defibrillator (NCIT:C50032) |
| Pharmacotherapy | **Quinidine** | I<sub>to</sub> blocker; suppresses VF/storms | Quinidine (NCIT:C793; CHEBI:28593) |
| Acute storm | **Isoproterenol** / low-dose **adrenaline** | β-agonist ↑I<sub>Ca-L</sub>, restores dome | Isoproterenol (NCIT:C371) |
| Adjunct | **Cilostazol / milrinone** (PDE3i) | Restore electrical homogeneity | — |
| Interventional | **Epicardial RVOT substrate ablation** | Eliminates late-potential substrate | Catheter Ablation (NCIT:C99521) |
| Supportive | Antipyresis; avoid contraindicated drugs; correct electrolytes | Removes triggers | — |

Evidence: quinidine prevented inducible VF in 9/10 [PMID 29761670]; epicardial ablation is transformative for high-risk/recurrent patients [PMID 41738055; 40088219]; isoproterenol/adrenaline rescue for electrical storms [PMID 40800556]. No approved gene/cell/RNA therapy; gene therapy/precision ablation are aspirational goals [PMID 40505939]. Personalized medicine is by risk score/phenotype, not *SCN3B* genotype.

### 13. Prevention

**Primary:** trigger avoidance (fever→antipyretics, avoid BrS-contraindicated drugs, moderate alcohol) [PMID 42411811]; no relevant immunization. **Secondary:** cascade ECG + genetic screening of first-degree relatives; risk stratification (Shanghai/Sieira) to select ICD candidates [PMID 40996547; 40314213]. **Tertiary:** ICD, quinidine, epicardial ablation [PMID 40088219]. **Genetic counseling:** AD 50% transmission risk; preimplantation genetic testing available for inherited cardiac disease, though limited-validity genes like *SCN3B* complicate variant-based PGT [PMID 38516780]. **Public health:** region-dependent pre-participation ECG screening and sports-eligibility guidance [PMID 40116545].

### 14. Other Species / Natural Disease

*SCN3B* orthologs: mouse *Scn3b* (NCBI Gene 235281; MGI), rat *Scn3b* (RGD), and orthologs in most vertebrates; β3's I<sub>Na</sub>-modulatory function is evolutionarily conserved [PMID 19796257]. No naturally occurring *SCN3B* "Brugada" disease is catalogued in OMIA for companion animals/livestock; inherited ventricular arrhythmia/SCD syndromes exist in dogs (e.g., German Shepherd inherited ventricular arrhythmia) but are not *SCN3B*-defined. The reduced-I<sub>Na</sub> → conduction/arrhythmia mechanism is conserved and validated in mouse. Zoonotic/transmission concepts are not applicable (non-infectious genetic disease).

### 15. Model Organisms

**Mouse — *Scn3b*-knockout** [PMID 19796257]: constitutive KO showing slower heart rate, longer P-wave, prolonged PR interval, abnormal sinoatrial/atrial electrophysiology, prolonged sinus-node recovery, and inducible atrial tachycardia/fibrillation (in essentially all KO vs almost no WT); *Scn1b/Scn5a* mRNA unchanged, isolating the β3 effect. *Limitations:* emphasizes atrial/conduction phenotypes; the human ventricular RVOT phase-2-reentry VF and spontaneous type-1 ECG are not straightforwardly reproduced (species differences in I<sub>to</sub> distribution). *Applications:* SA-node function, atrial conduction, AF susceptibility.

**In-vitro/cellular:** heterologous expression (HEK-293/CHO) co-expressing Nav1.5 + mutant β3 for patch-clamp I<sub>Na</sub> and trafficking/biotinylation assays [PMID 23257389; 39761910]; β-subunit-eliminated human haploid (BeHAPe) cells to study subunit regulation [PMID 37544648]. Patient-derived iPSC-cardiomyocytes are used broadly for BrS but no *SCN3B*-specific iPSC model was identified. **Resources:** MGI (*Scn3b*), IMPC, RGD.

---

## Mechanistic Model / Interpretation

```
 SCN3B loss-of-function variant (V110I / L10P / T138del)
                 │  alters Navβ3 auxiliary subunit
                 ▼
 Impaired β3 chaperone/modulatory function          [DEMONSTRATED in HEK293]
                 ▼
 ↓ Nav1.5 (SCN5A) trafficking → ↓ cell-surface channels   [DEMONSTRATED]
                 ▼
 ↓ Peak cardiac sodium current (I_Na)  ◄── fever / Na-blocker drugs / vagal tone (TRIGGERS)
                 │  [INFERRED for RVOT ventricle from canine wedge models]
                 ▼
 I_to dominance in RV epicardium → loss of AP dome (accentuated notch)
                 │
                 ├──► Transmural + epicardial repolarization heterogeneity
                 │            └► Type-1 coved ST elevation (V1–V2)  ── DIAGNOSIS
                 │
                 └──► Concealed PHASE-2 REENTRY (extrasystoles)
                                   │
                                   ▼
                    Polymorphic VT / VF  ──►  Syncope / SCD
                                   ▲
       (+ subtle epicardial RVOT fibrosis: microstructural–electrical continuum)

 Atrial branch: same ↓I_Na lesion → conduction slowing + inducible AF  [KO mouse; human AF variants]
```

**Upstream vs downstream:** the mutation and I<sub>Na</sub> reduction are upstream; the I<sub>to</sub>/repolarization imbalance, phase-2 reentry, and VF are downstream. Fever and drugs amplify anywhere along the I<sub>Na</sub> axis. The unifying principle is a **reduced-inward-current → repolarization-gradient → reentry** cascade localized to the RVOT epicardium — the same final common pathway as *SCN5A*-related BrS, which is why BrS7 is clinically indistinguishable.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role |
|---|---|---|---|
| [23257389](https://pubmed.ncbi.nlm.nih.gov/23257389/) | *Novel SCN3B mutation … trafficking and function of Nav1.5* | In vitro/human | **Supports** — V110I ↓Nav1.5 surface & ↓I<sub>Na</sub>; 1.7% of SCN5A-neg BrS |
| [39761910](https://pubmed.ncbi.nlm.nih.gov/39761910/) | *Novel SCN3B in-frame codon deletion (T138del) in BrS* | In vitro/human | **Supports** — expands variant spectrum; β3 is regulatory subunit |
| [19796257](https://pubmed.ncbi.nlm.nih.gov/19796257/) | *Scn3b knockout mice … conduction properties* | Model organism | **Supports** — conduction slowing & atrial arrhythmia |
| [24657694](https://pubmed.ncbi.nlm.nih.gov/24657694/) | *Abnormal repolarization … late potentials in BrS models* | In vitro | **Supports** — epicardial phase-2 reentry substrate |
| [41738055](https://pubmed.ncbi.nlm.nih.gov/41738055/) | *Contemporary Perspectives on J-Wave Syndromes (consensus)* | Human/consensus | **Supports & qualifies** — microstructural–electrical continuum; SCN5A sole definitive gene; therapy |
| [29959160](https://pubmed.ncbi.nlm.nih.gov/29959160/) | *Reappraisal of Reported Genes … Gene Validity for BrS* | Computational/curation | **Challenges** — SCN3B = limited evidence |
| [38426305](https://pubmed.ncbi.nlm.nih.gov/38426305/) | *Genetic Testing in BrS: A 30-Year Experience* | Human clinical | **Supports** — P/LP variant in 20–25%; SCN5A worse prognosis |
| [21051419](https://pubmed.ncbi.nlm.nih.gov/21051419/) | *SCN3B mutations … early-onset lone AF* | In vitro/human | **Supports** — SCN3B LOF also causes AF |
| [36362949](https://pubmed.ncbi.nlm.nih.gov/36362949/) | *Two novel functional mutations in promoter of SCN3B* | In vitro | **Supports** — GATA4 regulates SCN3B; 5′UTR gain-of-function in AF |
| [40996547](https://pubmed.ncbi.nlm.nih.gov/40996547/) | *Predictive value of Shanghai score (drug-induced type-1)* | Human clinical | **Supports** — flecainide/ajmaline confirmation; SCN5A OR 12.5 |
| [29761670](https://pubmed.ncbi.nlm.nih.gov/29761670/) | *ISRABRU-VF nationwide survey* | Human clinical | **Supports** — quinidine prevented inducible VF in 9/10 |
| [41819241](https://pubmed.ncbi.nlm.nih.gov/41819241/) | *Notched P wave … BrS multicenter study* | Human clinical | **Supports** — 510 patients, mean 51±14 yr, 95% men |
| [40130219](https://pubmed.ncbi.nlm.nih.gov/40130219/) | *Risk stratification of elderly BrS (Japan)* | Human clinical | **Supports** — 0.7% vs 1.5%/yr; prior VF key risk factor |
| [40088219](https://pubmed.ncbi.nlm.nih.gov/40088219/) | *ICD Therapy in BrS: 30-Year Experience* | Human clinical | **Supports** — ICD outcomes; epicardial ablation benefit |
| [42200267](https://pubmed.ncbi.nlm.nih.gov/42200267/) | *Fever-induced VF in hidden BrS (73-y-o)* | Human clinical | **Supports** — fever trigger; late-onset presentation |
| [42411811](https://pubmed.ncbi.nlm.nih.gov/42411811/) | *Brugada syndrome in pregnancy* | Human clinical | **Supports** — fever/electrolyte/drug precipitants |
| [40245999](https://pubmed.ncbi.nlm.nih.gov/40245999/) | *VGSC β3 subunit … immunoglobulin domain* | In vitro | **Supports** — SCN3B encodes β3 with extracellular Ig domain |

---

## Supported vs Refuted Hypotheses

**Supported:**
- *SCN3B* loss-of-function reduces I<sub>Na</sub> via impaired Nav1.5 trafficking → BrS ECG [PMID 23257389].
- The BrS substrate is RVOT epicardial repolarization heterogeneity with phase-2 reentry [PMID 24657694].
- *Scn3b* loss causes conduction slowing/atrial arrhythmia in vivo [PMID 19796257].
- *SCN3B* is also an allelic cause/susceptibility gene for atrial fibrillation [PMID 21051419].

**Refuted / down-weighted:**
- The premise that *SCN3B* is a robustly validated monogenic BrS gene is **not supported**; evidence-based curation rates it "limited," with *SCN5A* the only definitive gene [PMID 29959160; 41738055].

---

## Limitations and Knowledge Gaps

1. **Disputed gene validity** — *SCN3B* has only "limited" clinical validity; the BrS7 designation rests on few families/variants, and some historical assignments may be reclassified.
2. **Sparse subtype-specific data** — penetrance, prevalence, sex ratio, and prognosis are extrapolated from general BrS cohorts; no large *SCN3B*-specific natural-history study exists.
3. **Model–human gap** — the *Scn3b*-KO mouse reproduces atrial/conduction phenotypes but not the human RVOT ventricular VF substrate; canine wedge models are pharmacological, not *SCN3B*-genotype-specific.
4. **Mechanistic gaps** — the T138del variant showed normal surface expression, implying additional (gating/microdomain) mechanisms beyond trafficking [PMID 39761910].
5. **No genotype-specific therapy or biomarker** — management is generic BrS care; risk models carry high bias.
6. **Directionality complexity** — *SCN3B* shows loss-of-function (BrS, AF) and gain-of-function (promoter, AF) in different contexts, complicating variant interpretation.

---

## Proposed Follow-up Experiments / Actions

1. **Patient-derived iPSC-cardiomyocytes** carrying *SCN3B* variants (± isogenic correction) with I<sub>Na</sub>/I<sub>to</sub> phenotyping and optical mapping in engineered RVOT-like tissue — to test the human ventricular substrate directly.
2. **Formal ClinGen re-curation** of *SCN3B* incorporating post-2018 variants (e.g., T138del), segregation, and functional data to update gene-validity classification.
3. **Population-scale variant assessment** in gnomAD/TOPMed to establish allele frequencies and refine ACMG classification of reported BrS7 variants.
4. **Genotype-stratified cohort analysis** pooling *SCN3B* carriers across international BrS registries to estimate penetrance, event rates, and therapy response versus *SCN5A* and gene-negative patients.
5. **Structural biology** of the β3 Ig domain–Nav1.5 interface (cryo-EM / AlphaFold-Multimer) to map how V110I/T138del disrupt trafficking and gating.
6. **Systematic drug-safety curation** of I<sub>Na</sub>-blocking agents and emerging triggers (e.g., tyrosine-kinase inhibitors) for carrier avoidance lists.

---

*Report compiled from ~61 PubMed records. Key PMIDs: 23257389, 39761910, 19796257, 24657694, 41738055, 29959160, 21051419, 40996547, 40088219, 29761670, 42411811, 42200267, 41819241, 40130219, 38426305, 40245999, 36362949. Evidence source legend: human clinical (cohorts, case reports, consensus), in-vitro electrophysiology (HEK293 heterologous expression, canine wedge), model organism (Scn3b-KO mouse), computational/curation (ClinGen gene validity).*


## Artifacts

- [OpenScientist final report](Brugada_Syndrome_7-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Brugada_Syndrome_7-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 31 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 15 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013481` (1 mention) - the report calls it "brugada syndrome 7"; MONDO calls it **chromosome 13q14 deletion syndrome**
- `HP:0031650` (1 mention) - the report calls it "ECG sign"; HP calls it **Abnormal atrioventricular valve physiology**
- `HP:0001279` (1 mention) - the report calls it "Symptom"; HP calls it **Syncope**
- `HP:0001645` (1 mention) - the report calls it "Outcome"; HP calls it **Sudden cardiac death**
- `HP:0005110` (1 mention) - the report calls it "Clinical sign"; HP calls it **Atrial fibrillation**
- `HP:0012722` (1 mention) - the report calls it "ECG sign"; HP calls it **Heart block**
- `NCIT:C50032` (1 mention) - the report calls it "Implantable Cardioverter-Defibrillator"; NCIT calls it **Limiter Device**
- `NCIT:C371` (1 mention) - the report calls it "Isoproterenol"; NCIT calls it **Chromomycin Antineoplastic Antibiotic**
- `NCIT:C99521` (1 mention) - the report calls it "Catheter Ablation"; NCIT calls it **Percutaneous Coronary Intervention**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0086067` (1 mention) - the report calls it "bundle of His cell–Purkinje conduction"; GO calls it **AV node cell to bundle of His cell communication**
- `UBERON:0000948` (1 mention) - the report calls it "Organ:** heart"; UBERON calls it **heart**, and lists "branchial heart" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.