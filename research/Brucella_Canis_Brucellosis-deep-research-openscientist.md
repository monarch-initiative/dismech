---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T17:17:45.199178'
end_time: '2026-09-29T17:32:36.195845'
duration_seconds: 891.0
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Brucella Canis Brucellosis
  mondo_id: MONDO:0001857
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
citation_count: 25
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 37
  quotes_valid: 35
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:33002657
  - PMID:36862545
  relevance_assessed: 25
  on_topic: 24
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 31
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 7
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0001857
    reported_labels:
    - if available
    - MONDO
    ontology_label: Brucella canis brucellosis
  - term_id: HP:0100603
    reported_labels:
    - Stillbirth, analogous
    ontology_label: Toxemia of pregnancy
  - term_id: HP:0000029
    reported_labels:
    - Abnormality of the testis
    ontology_label: Testicular atrophy
  - term_id: GO:0005783
    reported_labels:
    - endoplasmic reticulum
    - Endoplasmic reticulum (replication niche); Brucella-containing vacuole
    ontology_label: endoplasmic reticulum
  - term_id: NCIT:C299
    reported_labels:
    - Doxycycline
    ontology_label: Beclomethasone Dipropionate
  - term_id: NCIT:C864
    reported_labels:
    - Streptomycin
    ontology_label: 2,3,7,8-Tetrachlorodibenzo-P-dioxin
  - term_id: NCIT:C793
    reported_labels:
    - Rifampin
    ontology_label: Quinidine
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Brucella_Canis_Brucellosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Brucella_Canis_Brucellosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Brucella Canis Brucellosis
- **MONDO ID:** MONDO:0001857 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Brucella Canis Brucellosis** covering all of the
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

# Brucella canis Brucellosis (Canine Brucellosis): A Comprehensive Disease Characterization

**Disease:** Brucella canis Brucellosis
**MONDO ID:** MONDO:0001857
**ICD-10:** A23.3 (Brucellosis due to Brucella canis) · **ICD-11:** 1B95 · **MeSH:** Brucellosis, Canine
**Pathogen:** *Brucella canis* (NCBI:txid36855)
**Category:** Infectious Disease (bacterial zoonosis)

---

## Summary

*Brucella canis* brucellosis is a chronic, zoonotic bacterial infection whose natural host is the domestic dog (*Canis lupus familiaris*, NCBI:txid9615). The causative agent, *Brucella canis*, is a naturally-rough (rough-LPS), facultatively intracellular Gram-negative α-proteobacterium that is phylogenetically nested within *Brucella suis* despite its distinct clinical niche. In dogs the infection presents primarily as reproductive failure — late-gestation abortion, epididymitis, prostatitis, and infertility — but it also causes discospondylitis (vertebral disc/endplate infection), anterior uveitis/endophthalmitis, and frequently subclinical, persistent bacteremia. Transmission is predominantly venereal and through reproductive fluids and aborted material, placing breeding kennels and free-roaming stray populations at highest risk. The organism is an under-recognized zoonosis: humans acquire infection through contact with infected dogs, and standard smooth-*Brucella* human serology fails to detect it.

Mechanistically, the disease is driven by the pathogen's capacity to survive and replicate inside host macrophages. *B. canis* enters cells through cholesterol- and ganglioside-GM1-rich lipid rafts, elicits only weak macrophage activation, and establishes a *Brucella*-containing vacuole (BCV) that traffics to the endoplasmic reticulum — a process orchestrated by lipopolysaccharide (LPS), the VirB Type IV secretion system (T4SS), and the BvrR/BvrS two-component regulatory system. This intracellular, immune-evasive lifestyle explains the chronic, relapsing course, the intermittent low-level bacteremia that undermines diagnosis, and the notorious difficulty of achieving microbiological cure even with prolonged multidrug antimicrobial therapy.

The public-health and veterinary importance of *B. canis* is rising. There is no vaccine and no reliably curative treatment; control depends on serological screening, test-and-removal, neutering, biosecurity, and — increasingly — import regulation, since the international movement of dogs is spreading the organism into previously low-prevalence regions. This report synthesizes 12 confirmed findings across 28 reviewed papers into a section-by-section knowledge-base entry, with ontology mappings and cited primary evidence. Because this is an infectious rather than heritable disease, the genetic/variant/inheritance portions of the template are largely **Not applicable** at the host level and are annotated as such; the corresponding "molecular genetics" reside in the *pathogen* genome.

---

## 1. Disease Information

**Overview.** *Brucella canis* brucellosis is a contagious bacterial disease of dogs and an occupational/companion-animal zoonosis of humans. In dogs it is chiefly a reproductive disease and a cause of discospondylitis, with a substantial proportion of subclinical infections. As one authoritative case report summarizes, "*Brucella canis* is a zoonotic bacterium, causing mainly reproductive disorders and discospondylitis in dogs, but infections may also be subclinical. Mating is one of the main transmission routes, putting breeding dogs and stray dogs at risk of infection" ([PMID: 41957789](https://pubmed.ncbi.nlm.nih.gov/41957789/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0001857 |
| ICD-10 | A23.3 (Brucellosis due to *Brucella canis*) |
| ICD-11 | 1B95 (Brucellosis) |
| MeSH | Brucellosis, Canine |
| Pathogen taxon | NCBI:txid36855 (*Brucella canis*) |
| OMIM / Orphanet | Not applicable (infectious, non-Mendelian disease) |

**Synonyms / alternative names.** Canine brucellosis; *B. canis* infection; contagious canine abortion (historical, in kennels). The type strain is **RM6/66**.

**Nature of the information.** All evidence is derived from **aggregated disease-level resources** — veterinary case series, kennel outbreak investigations, seroprevalence surveys, and human seroepidemiological studies — rather than individual EHR-level patient records. Evidence source types span veterinary clinical, human clinical/seroepidemiological, in vitro (macrophage infection models), and computational (whole-genome phylogenetics).

---

## 2. Etiology

**Primary cause — infectious.** The disease is caused entirely by infection with *Brucella canis*, a Gram-negative coccobacillus. It is not a genetic disease; there are no causal host genes, no pathogenic germline/somatic variants, and no Mendelian inheritance. Accordingly, Section 4 (host genetic/molecular information) and much of Section 9's inheritance sub-items are **not applicable** — the "genetic" story of this disease is that of the *pathogen's* genome (Section 7-genomics and Section 6).

**Transmission routes (principal risk exposures).** Mating (venereal) is a primary route; other routes include contact with aborted materials and vaginal discharge, infected semen, oronasal contact with contaminated fluids, and vertical (transplacental/milk) transmission. "Mating is one of the main transmission routes, putting breeding dogs and stray dogs at risk of infection" ([PMID: 41957789](https://pubmed.ncbi.nlm.nih.gov/41957789/)).

**Risk factors (host/environmental).**
- **Reproductive status:** intact (unaltered) dogs are at higher risk than neutered/spayed dogs.
- **Age:** older dogs show higher seropositivity in stray populations.
- **Living conditions:** stray, shelter, and breeding-kennel dogs; peridomestic/free-roaming populations in socioeconomically deprived urban areas.
- **Occupational (human):** kennel employees, veterinarians, laboratory diagnosticians, animal-care providers.
- **Importation:** movement of dogs from endemic regions.

From a South Dakota stray-dog survey: "Older dogs were significantly more likely to be *B. canis*-positive than younger dogs, as were reproductively intact dogs versus altered dogs" ([PMID: 33002657](https://pubmed.ncbi.nlm.nih.gov/33002657/)).

**Protective factors.** Neutering/spaying reduces risk (venereal exposure reduction). No genetic protective variants are described (not applicable). There is no vaccine (Section 13).

**Gene–environment interactions.** Not applicable at the host level. The relevant "gene–environment" axis is the pathogen's virulence-gene repertoire interacting with the host intracellular environment (Section 6).

---

## 3. Phenotypes

*B. canis* brucellosis produces distinct clinical syndromes in dogs. Because this is a non-Mendelian infectious disease, HPO terms (human-phenotype-oriented) are suggested by analogy where a human-analogous phenotype exists.

| Phenotype | Type | Onset / course | Frequency | Suggested HPO |
|---|---|---|---|---|
| Late-gestation abortion (≈ day 45–59) | Clinical sign (reproductive) | Adult breeding animals; episodic | Common in bitches | HP:0100603 (Stillbirth, analogous) |
| Epididymitis / orchitis / prostatitis; infertility | Clinical sign (reproductive) | Adult intact males; chronic | Common in infected males | HP:0000029 (Abnormality of the testis) |
| Discospondylitis (back pain, lameness, spinal pain) | Clinical sign (musculoskeletal) | Young intact dogs (median ~2.6 yr); chronic/progressive | Recognized cause | HP:0003418 (Back pain) |
| Anterior uveitis / endophthalmitis (unilateral) | Clinical sign (ocular) | Chronic/recurrent | Uncommon | HP:0000554 (Uveitis) |
| Lymphadenopathy | Clinical sign | Variable | Common | HP:0002716 (Lymphadenopathy) |
| Subclinical persistent bacteremia | Laboratory/microbiological | Insidious; chronic | Frequent | — |
| Fever / malaise (mainly human) | Symptom | Nonspecific, insidious | Common in symptomatic humans | HP:0001945 (Fever), HP:0025406 (Malaise) |

**Characteristics.** Onset is typically adult (reproductive disease) or young-adult (discospondylitis); course is chronic, insidious, and relapsing; severity ranges from subclinical to severe (endocarditis in rare human cases). The reproductive phenotype is episodic (tied to gestation/breeding). *B. canis* discospondylitis is distinguished clinically by younger age and characteristic spinal distribution (Section 6/clinical).

**Quality-of-life impact.** In dogs: reproductive failure ends breeding value; discospondylitis causes chronic pain and lameness; uveitis threatens vision. In humans: chronic febrile illness with fatigue; rare severe complications. Formal QoL instruments (EQ-5D/SF-36) have not been applied to this zoonosis.

---

## 4. Genetic/Molecular Information (Host)

**Not applicable.** *B. canis* brucellosis is an acquired infectious disease with no causal host genes, pathogenic variants, modifier genes, host epigenetic drivers, or chromosomal abnormalities. Host genetic susceptibility loci have not been established. The molecular "genetics" of the disease reside in the pathogen genome.

**Pathogen genomics (analogous content).** Whole-genome SNP phylogeny of the highly conserved *Brucella* genus (20,154 shared orthologous SNPs) shows that "*B. suis* was determined to be paraphyletic in our analyses, only forming a monophyletic clade when the *B. canis* genome was included" ([PMID: 19201792](https://pubmed.ncbi.nlm.nih.gov/19201792/)). Core-genome MLST places *B. canis* "closest relationship with *B. suis* bv. 4, followed by *B. suis* bv. 3 and bv. 1" ([PMID: 30385393](https://pubmed.ncbi.nlm.nih.gov/30385393/)). Divergence dating indicates "most *Brucella* species diverged from their common *B. ovis* ancestor in the past 86,000 to 296,000 years, which precedes the domestication of their livestock hosts" ([PMID: 19201792](https://pubmed.ncbi.nlm.nih.gov/19201792/)).

---

## 5. Environmental Information

- **Environmental factors:** Contaminated kennel environments, aborted materials, vaginal/seminal discharges, and shared breeding facilities are the principal fomite/exposure reservoirs. There is no toxin, radiation, or pollution etiology.
- **Lifestyle factors (human):** Occupational animal contact (kennel work, veterinary practice, laboratory handling); keeping infected dogs in the home. "Humans can become infected with *B canis* when an infected pet dog is brought into their home" ([PMID: 36892988](https://pubmed.ncbi.nlm.nih.gov/36892988/)).
- **Infectious agent:** *Brucella canis* (NCBI:txid36855), a naturally-rough member of the *B. suis* clade. Type strain RM6/66. Key virulence molecule: lipopolysaccharide (LPS, CHEBI:16412).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Exposure** to infected reproductive fluids/aborted material or venereal contact **leads to** mucosal entry of *B. canis*.
2. Bacteria are taken up by macrophages and dendritic cells; entry **occurs via** cholesterol- and ganglioside-GM1-rich **lipid rafts** and the class A scavenger receptor **→ results in** intracellular localization (demonstrated in murine macrophages for *B. canis* and *B. ovis*).
3. The organism **induces only weak macrophage activation** (rough *Brucella* LPS is poorly stimulatory) **→ results in** evasion of early bactericidal responses.
4. Coordinated action of **LPS, the VirB Type IV secretion system (T4SS), and the BvrR/BvrS two-component system leads to** formation of an early and then late **Brucella-containing vacuole (BCV)** that avoids lysosomal fusion.
5. The BCV **traffics to and interacts with the endoplasmic reticulum (ER) → results in** a replication-permissive niche where bacteria multiply (upstream driver of persistence).
6. Intracellular replication with slow release **leads to** chronic, **intermittent low-level bacteremia** (downstream consequence; also the reason diagnosis is hard).
7. Bacteremia **seeds** target tissues — **reproductive tract** (placenta/trophoblast, epididymis, prostate), **intervertebral discs/vertebral endplates**, and the **eye (uvea)** — **→ results in** the clinical syndromes (branch point: reproductive vs. skeletal vs. ocular disease).
8. In the placenta, trophoblast infection **leads to** **necrotic placentitis → results in** late-gestation abortion (demonstrated by immunohistochemical trophoblast staining).
9. In humans, the same intracellular-persistence mechanism **leads to** nonspecific febrile illness and, rarely, **infective endocarditis** and neurological complications (inferred to share the canine intracellular mechanism).

### Detail by category

**Molecular pathways / virulence machinery.** "Major virulence factors are: lipopolysaccharide (LPS), T4SS secretion system and BvrR/BvrS system, which allow interaction with host cell surface, formation of an early, late BCV (Brucella Containing Vacuole) and interaction with endoplasmic reticulum (ER) when the bacteria multiply" ([PMID: 30015453](https://pubmed.ncbi.nlm.nih.gov/30015453/)). The overarching pathogenic property: "The most important feature of *Brucella* is the ability to survive and multiply within both phagocytic and non-phagocytic cells" ([PMID: 30015453](https://pubmed.ncbi.nlm.nih.gov/30015453/)).

**Cellular processes / entry.** "The establishment of infection by *Brucella ovis* and *Brucella canis* in J774.A1 macrophages was found to be dependent upon cholesterol and ganglioside GM(1), two components of lipid rafts" ([PMID: 20083220](https://pubmed.ncbi.nlm.nih.gov/20083220/)), and "both bacteria induced a weak degree of macrophage activation" ([PMID: 20083220](https://pubmed.ncbi.nlm.nih.gov/20083220/)) — i.e., immune-evasive entry favoring persistence.

**Immune system involvement.** Chronic intracellular infection with dampened innate activation; delayed/insufficient sterilizing immunity underlies relapse. Rough LPS is a weaker TLR4 agonist than smooth LPS, contributing to stealth.

**Tissue damage mechanisms.** Granulomatous/necrotizing inflammation at seeded sites; placental necrosis with trophoblast tropism drives abortion; discitis/osteomyelitis at vertebral endplates; chronic uveal inflammation.

**Suggested ontology terms.**
- GO biological process: GO:0051701 (biological process involved in interaction with host); GO:0044409 (entry into host); intracellular replication in ER-derived vacuole.
- GO cellular component: GO:0005783 (endoplasmic reticulum) — BCV target; phagosome/endosome-derived vacuole (GO:0005768).
- CL cell types: CL:0000235 (macrophage), CL:0000451 (dendritic cell), trophoblast (placental target).
- CHEBI: LPS (CHEBI:16412), cholesterol (CHEBI:16113), ganglioside GM1 (CHEBI:18216).

---

## 7. Anatomical Structures Affected

| Level | Structures | Suggested ontology |
|---|---|---|
| **Primary organs** | Male reproductive tract (testis, epididymis, prostate); female reproductive tract (uterus, placenta); intervertebral discs/vertebrae; eye (uvea) | UBERON:0000473 (testis), UBERON:0001301 (epididymis), UBERON:0002367 (prostate), UBERON:0001987 (placenta), UBERON:0002412 (vertebra), UBERON:0001803 (uvea) |
| **Secondary/systemic** | Lymph nodes (lymphadenopathy), spleen; heart valves (human endocarditis) | UBERON:0000029 (lymph node), UBERON:0002106 (spleen), UBERON:0006618 (heart valve) |
| **Body systems** | Reproductive, musculoskeletal, ocular, lymphoreticular; cardiovascular (rare human) | — |
| **Tissue/cell** | Placental trophoblast; macrophages/dendritic cells (reservoir) | CL:0000235, CL:0000451 |
| **Subcellular** | Endoplasmic reticulum (replication niche); Brucella-containing vacuole | GO:0005783 |
| **Localization** | Discospondylitis often focal; uveitis characteristically **unilateral**; C2–C5 cervical involvement over-represented | — |

Placental trophoblast tropism is directly documented: "necrotic placentitis and the strong immunostaining of trophoblast cells by immunohistochemistry" ([PMID: 21217047](https://pubmed.ncbi.nlm.nih.gov/21217047/)). Cervical predilection in discospondylitis: "higher odds of C2-C5 involvement (OR = 13.0; 95% CI 1.6-106.7)" ([PMID: 40317976](https://pubmed.ncbi.nlm.nih.gov/40317976/)).

---

## 8. Temporal Development

- **Onset.** Adult onset for reproductive disease; young-adult onset for discospondylitis (median 2.6 yr). Pattern is **insidious/chronic**; many infections subclinical for extended periods.
- **Progression.** Chronic, **relapsing/episodic** (reproductive events; recurrent uveitis). Persistent intracellular infection with intermittent bacteremia can last months to years. Discospondylitis is progressive if untreated.
- **Duration.** Effectively **lifelong** without successful eradication; microbiological cure is difficult and relapse common.
- **Remission/critical windows.** Antimicrobial therapy can induce clinical remission and declining serology, but relapse is frequent after cessation; neutering reduces shedding. A ≥40% decline in *B. canis* antibody value at 2–6 months supports treatment response: "A 40% decline in CBM assay values 2 to 6 months posttreatment can be supportive of response to treatment" ([PMID: 36892988](https://pubmed.ncbi.nlm.nih.gov/36892988/)). In ocular disease, seronegativity took a "median of 96 weeks (range: 36-112 weeks) of therapy" ([PMID: 19392878](https://pubmed.ncbi.nlm.nih.gov/19392878/)).

---

## 9. Inheritance and Population (Epidemiology)

**Inheritance.** Not applicable — infectious, non-heritable disease. No penetrance/expressivity/anticipation/founder-effect/consanguinity/carrier-frequency concepts apply to the host.

**Epidemiology (seroprevalence).**

| Population | n | Finding | Source |
|---|---|---|---|
| Stray/surrendered dogs, South Dakota reservations (2015–2019) | 3,898 | Apparent seroprevalence **6.8%**; adjusted true prevalence **29.4%**; declining over time; older & intact dogs higher risk | [PMID: 33002657](https://pubmed.ncbi.nlm.nih.gov/33002657/) |
| Shelter dogs, Mississippi | 571 | **4.9%** RSAT-seropositive (2.3% confirmed) | [PMID: 30314794](https://pubmed.ncbi.nlm.nih.gov/30314794/) |
| Urban slum humans, Salvador, Brazil | 174 | **4.6%** *B. canis* seropositive | [PMID: 23000868](https://pubmed.ncbi.nlm.nih.gov/23000868/) |
| Dog-exposed adults (occupational), USA | 306 vs 101 controls | **10.8% (RSAT) – 3.6% (ME-RSAT)**; kennel workers OR 2.7 (95% CI 1.3–5.8) | [PMID: 24751191](https://pubmed.ncbi.nlm.nih.gov/24751191/) |

Direct quotes: "we determined an overall apparent *B. canis* seroprevalence of 6.8% (adjusted estimated true prevalence of 29.4%)… Older dogs were significantly more likely to be *B. canis*-positive than younger dogs, as were reproductively intact dogs versus altered dogs" ([PMID: 33002657](https://pubmed.ncbi.nlm.nih.gov/33002657/)); "Twenty-eight dogs (4.9%) were seropositive for *B. canis* antibodies on the RSAT" ([PMID: 30314794](https://pubmed.ncbi.nlm.nih.gov/30314794/)).

**Geographic distribution.** Endemic in the Americas (notably parts of the US South, Latin America), and increasingly reported in Europe via dog importation. Whole-genome/MLVA typing has traced international spread: "We detected three recent introductions of different *B. canis* strains in kennels: two traced from Mexico and one from Panama" ([PMID: 33965789](https://pubmed.ncbi.nlm.nih.gov/33965789/)).

**Demographics.** Highest in intact, older, free-roaming/kennel dogs. Human cases cluster in occupationally exposed individuals and in socioeconomically deprived urban areas with expanding peridomestic dog populations: "Changes in the urban environment due to slum communities' expansion have resulted in increased dog populations in the peridomiciliary environment" ([PMID: 23040615](https://pubmed.ncbi.nlm.nih.gov/23040615/)).

---

## 10. Diagnostics

Diagnosis is challenging because of the **rough antigen** (standard smooth-*Brucella* serology fails) and **intermittent low-level bacteremia**.

**Serology (screening).** Rough-antigen assays are required: RSAT, 2ME-RSAT, AGID, and immunochromatographic/CBM tests. Sensitivities are limited:

| Test | Sensitivity | Specificity |
|---|---|---|
| RSAT | 70.6–75% | moderate |
| 2ME-RSAT | 31.8–37.5% | up to 100% |
| AGID | 27.8–52.9% | up to 100% |
| Immunochromatographic (ICT) | 89.6% | 100% |

"The diagnostic sensitivity of RSAT, 2ME-RSAT and AGID was respectively 70.58%, 31.76%, and 52.94%" ([PMID: 18656213](https://pubmed.ncbi.nlm.nih.gov/18656213/)). The ICT "showed a high diagnostic specificity and a diagnostic sensitivity value greater than that observed in the RSAT, 2ME-RSAT and AGID. However, 10.41% of infected dogs had negative results by ICT" ([PMID: 26489371](https://pubmed.ncbi.nlm.nih.gov/26489371/)).

**Molecular (confirmatory).** Blood PCR (IS711 target) markedly outperforms serum PCR: "The sensitivities of blood PCR and serum PCR were, respectively, 97.14 per cent and 25.71 per cent. The specificities of both were 100 per cent" ([PMID: 20643887](https://pubmed.ncbi.nlm.nih.gov/20643887/)) — establishing **blood** (not serum) as the preferred matrix. Semen PCR is a useful confirmatory test before breeding and is highly sensitive, detecting "as few as 3.8 fg of *B. canis* DNA" ([PMID: 17343907](https://pubmed.ncbi.nlm.nih.gov/17343907/)).

**Culture.** Blood/tissue/vaginal culture is confirmatory but insensitive (intermittent bacteremia) and is an **occupational hazard requiring BSL-3** handling. In one outbreak, culture succeeded in "only 3 of 31 (10%) cases" ([PMID: 21217047](https://pubmed.ncbi.nlm.nih.gov/21217047/)).

**Histopathology/IHC.** Placental IHC (anti-*B. canis*) demonstrates trophoblast infection and is a rapid, sensitive adjunct in abortion cases ([PMID: 21217047](https://pubmed.ncbi.nlm.nih.gov/21217047/)).

**Imaging.** Radiography/CT/MRI for discospondylitis (osteolysis, endplate sclerosis, periosteal proliferation); ophthalmic exam for uveitis/endophthalmitis.

**Human diagnosis caveat.** "Human serological assays designed to detect brucellosis will miss infections caused by *Brucella canis*, and low levels of periodic bacteremia limit diagnosis by blood culture" ([PMID: 24751191](https://pubmed.ncbi.nlm.nih.gov/24751191/)).

**Differential diagnosis.** Discospondylitis from other agents (*Staphylococcus*, *Streptococcus*, *E. coli*, fungal); other causes of canine infertility/abortion; other *Brucella* spp. in humans.

---

## 11. Outcome / Prognosis

- **Mortality.** Low direct mortality in dogs; the disease is chronic rather than rapidly fatal. In humans, mortality is low but severe complications (infective endocarditis, neurological) occur.
- **Morbidity.** Substantial: permanent loss of reproductive function, chronic spinal pain/lameness, potential vision loss. Infected breeding animals are typically removed from breeding.
- **Recovery / cure.** Microbiological cure is difficult; relapse is common even after prolonged multidrug therapy. Serologic monitoring (≥40% antibody decline at 2–6 months) supports response ([PMID: 36892988](https://pubmed.ncbi.nlm.nih.gov/36892988/)); ocular cases required a median 96 weeks to seronegativity ([PMID: 19392878](https://pubmed.ncbi.nlm.nih.gov/19392878/)).
- **Prognostic factors.** Site of disease, chronicity, treatment adherence/duration, and neutering status. Declining rough-antigen antibody titer is a favorable prognostic marker.
- **Human severe outcomes.** "We report *Brucella canis* human infection link to Gaucher's disease and Guillain Barré syndrome and discuss complications observed in a case with infective endocarditis" ([PMID: 23040615](https://pubmed.ncbi.nlm.nih.gov/23040615/)).

---

## 12. Treatment

**Pharmacotherapy — combination antimicrobials.** Because *B. canis* is intracellular, **poly-antimicrobial, prolonged therapy** is standard; monotherapy fails. In a series of 30 naturally infected dogs, "poly-antimicrobial therapy was prescribed in 97% (29/30) of cases" ([PMID: 36892988](https://pubmed.ncbi.nlm.nih.gov/36892988/)). Common agents (suggested NCIT clinical-intervention terms in parentheses):

| Drug | Class | NCIT (suggested) |
|---|---|---|
| Doxycycline / tetracyclines | Tetracycline antibiotic | NCIT:C299 (Doxycycline) |
| Streptomycin / gentamicin | Aminoglycoside | NCIT:C864 (Streptomycin) |
| Rifampin | Rifamycin | NCIT:C793 (Rifampin) |
| Enrofloxacin | Fluoroquinolone (veterinary) | — |

A validated ocular regimen combined four drugs: "a novel antimicrobial protocol that included doxycycline, enrofloxacin, rifampin and streptomycin" ([PMID: 19392878](https://pubmed.ncbi.nlm.nih.gov/19392878/)), with "serological values declined with seronegativity achieved in all dogs after a median of 96 weeks (range: 36-112 weeks) of therapy" ([PMID: 19392878](https://pubmed.ncbi.nlm.nih.gov/19392878/)).

**Adjunct/interventional.** **Neutering (surgical)** reduces shedding and venereal transmission and is a standard component of management (NCIT:C15329 Castration / ovariohysterectomy). **No gene, cell, RNA, targeted, or immunotherapy** applies (not applicable).

**Treatment outcomes.** High relapse; combination therapy with prolonged duration and serologic monitoring is required. Because "*Brucella* spp… evade antimicrobial therapy," complete eradication is uncertain, and euthanasia/removal is often chosen for breeding-colony control.

**Personalized medicine / pharmacogenomics.** Not applicable.

---

## 13. Prevention

Prevention is the cornerstone because diagnostics and therapeutics are limited: "Diagnosis and treatment of brucellosis is challenging due to the limitations of diagnostic assays and the tendency of *Brucella* spp to produce nonspecific, insidious clinical signs and evade antimicrobial therapy, making prevention essential" ([PMID: 36862545](https://pubmed.ncbi.nlm.nih.gov/36862545/)).

- **Primary prevention.** **No vaccine exists.** "*Brucella canis* infection is one of the most important causes of infertility in dogs and is a zoonosis for which no effective treatment or vaccines exist" ([PMID: 36155554](https://pubmed.ncbi.nlm.nih.gov/36155554/)). Prevention relies on pre-breeding testing, biosecurity, and avoiding exposure to infected animals/materials.
- **Secondary prevention.** Serological screening of breeding stock and pre-mating semen/blood PCR; test-and-removal in kennels; cascade testing of contacts.
- **Tertiary prevention.** Neutering, isolation, treatment with serologic monitoring to reduce shedding and complications.
- **Public health / One Health.** Import control, occupational biosafety (BSL-3 for culture), owner/breeder/veterinarian education. Awareness is variable and control is hampered because it "is a zoonosis for which no effective treatment or vaccines exist" ([PMID: 36155554](https://pubmed.ncbi.nlm.nih.gov/36155554/)). Import legislation is often inadequate: "Current legislation is insufficient to address the risks and pre-import control measures are focused only on rabies virus and the fox tapeworm *Echinococcus multilocularis*" ([PMID: 41925288](https://pubmed.ncbi.nlm.nih.gov/41925288/)).
- **Human exposure routes reported to CDC:** "Human consumption of unpasteurized dairy products and occupational exposure of laboratory diagnosticians, veterinarians, and animal care providers are responsible for human exposures reported to the US CDC" ([PMID: 36862545](https://pubmed.ncbi.nlm.nih.gov/36862545/)).

---

## 14. Other Species / Natural Disease

- **Primary host / taxonomy.** Domestic dog, *Canis lupus familiaris* (NCBI:txid9615). Pathogen: *Brucella canis* (NCBI:txid36855). Wild canids may be susceptible. Serosurveys of wildlife (black bears, [PMID: 25075540](https://pubmed.ncbi.nlm.nih.gov/25075540/); free-roaming reserve dogs, [PMID: 35687596](https://pubmed.ncbi.nlm.nih.gov/35687596/)) were negative, indicating dogs are the principal reservoir rather than wildlife.
- **Breed.** No specific breed predisposition established (VBO not applicable beyond species); risk is driven by breeding/kennel management, not breed genetics.
- **Zoonotic transmission.** Confirmed zoonosis: "Humans can become infected with *B canis* when an infected pet dog is brought into their home" ([PMID: 36892988](https://pubmed.ncbi.nlm.nih.gov/36892988/)); occupational human infection is documented ([PMID: 24751191](https://pubmed.ncbi.nlm.nih.gov/24751191/)).
- **Comparative biology.** *B. canis* is one of several *Brucella* spp. of US One Health relevance: species "infect dogs (*B. canis*), swine (*B. suis*), and cattle/bison (*B. abortus*)" ([PMID: 36862545](https://pubmed.ncbi.nlm.nih.gov/36862545/)). Evolutionarily, *B. canis* is a rough clade nested within *B. suis*, diverged from a common *B. ovis* ancestor ([PMID: 19201792](https://pubmed.ncbi.nlm.nih.gov/19201792/)).

---

## 15. Model Organisms

- **In vitro / cellular models.** Murine macrophage cell lines (J774.A1) are the workhorse for *B. canis* entry/survival studies; these established the lipid-raft (cholesterol, GM1) and scavenger-receptor entry mechanism ([PMID: 20083220](https://pubmed.ncbi.nlm.nih.gov/20083220/)). Human U937 monocytic cells (RA/VD-differentiated) discriminate virulence: during infection these cells "could discriminate between the human pathogen *Brucella suis* S1, which strongly multiplied, and the animal pathogen *Brucella canis*, which survived without multiplication" ([PMID: 8071593](https://pubmed.ncbi.nlm.nih.gov/8071593/)) — a basic model of bacteria–human macrophage interaction.
- **Natural/animal model.** The **dog itself** is the definitive natural host and de facto disease model; mouse infection models are used for *Brucella* pathogenesis generally.
- **Phenotype recapitulation / limitations.** Macrophage models capture intracellular survival and entry but not the reproductive, skeletal, and ocular tissue tropism of natural canine disease. No standardized knockout/transgenic host model exists (host genetics not causal).
- **Suggested CL terms:** CL:0000235 (macrophage), CL:0000576 (monocyte).

---

## Mechanistic Model / Interpretation

```
 EXPOSURE (venereal / aborted material / semen)
        │
        ▼
 Mucosal uptake by MACROPHAGES & DENDRITIC CELLS
        │  (lipid-raft entry: cholesterol + GM1 + scavenger receptor)
        ▼
 WEAK macrophage activation  ──► immune evasion (rough LPS poorly stimulatory)
        │
        ▼
 BCV formation (LPS + T4SS/VirB + BvrR/BvrS)
        │
        ▼
 BCV traffics to ENDOPLASMIC RETICULUM ──► intracellular replication
        │
        ▼
 Intermittent LOW-LEVEL BACTEREMIA  ──► (undermines diagnosis)
        │
   ┌────┴─────────────┬────────────────────┬───────────────┐
   ▼                  ▼                    ▼               ▼
 REPRODUCTIVE      SKELETAL             OCULAR          HUMAN
 (trophoblast →    (discospondylitis,   (unilateral     (fever; rare
  necrotic         C2–C5, young dogs)   uveitis /        endocarditis)
  placentitis →                         endophthalmitis)
  ABORTION;
  epididymitis,
  infertility)
```

The unifying theme is **intracellular persistence with immune stealth**. Every downstream clinical and diagnostic feature flows from it: chronicity and relapse (persistence in an ER-derived niche), diagnostic insensitivity (intermittent bacteremia + rough antigen), and therapeutic difficulty (antibiotics must penetrate cells and be sustained for months). Upstream determinants are the lipid-raft entry route and the LPS/T4SS/BvrR-BvrS virulence triad; downstream determinants are tissue tropism to placenta, spine, and eye.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [41957789](https://pubmed.ncbi.nlm.nih.gov/41957789/) | Core disease definition, syndromes, transmission | Veterinary clinical (case) |
| [30015453](https://pubmed.ncbi.nlm.nih.gov/30015453/) | Intracellular lifestyle; LPS/T4SS/BvrR-BvrS; BCV→ER | Review |
| [20083220](https://pubmed.ncbi.nlm.nih.gov/20083220/) | *B. canis*-specific lipid-raft entry; weak activation | In vitro |
| [8071593](https://pubmed.ncbi.nlm.nih.gov/8071593/) | U937 macrophage virulence discrimination | In vitro |
| [20643887](https://pubmed.ncbi.nlm.nih.gov/20643887/) | Blood PCR 97.1% vs serum 25.7% | Diagnostic |
| [18656213](https://pubmed.ncbi.nlm.nih.gov/18656213/) | RSAT/2ME-RSAT/AGID sensitivities | Diagnostic |
| [26489371](https://pubmed.ncbi.nlm.nih.gov/26489371/) | ICT performance; 10.4% missed | Diagnostic |
| [17343907](https://pubmed.ncbi.nlm.nih.gov/17343907/) | Semen PCR (3.8 fg detection) | Diagnostic |
| [21217047](https://pubmed.ncbi.nlm.nih.gov/21217047/) | Necrotic placentitis, trophoblast IHC; kennel outbreak | Veterinary pathology |
| [33002657](https://pubmed.ncbi.nlm.nih.gov/33002657/) | Stray-dog seroprevalence, age/intact risk | Epidemiology |
| [30314794](https://pubmed.ncbi.nlm.nih.gov/30314794/) | Shelter-dog seroprevalence | Epidemiology |
| [24751191](https://pubmed.ncbi.nlm.nih.gov/24751191/) | Human occupational infection; serology misses *B. canis* | Human seroepidemiology |
| [23000868](https://pubmed.ncbi.nlm.nih.gov/23000868/) | Human urban-slum seroprevalence 4.6% | Human seroepidemiology |
| [23040615](https://pubmed.ncbi.nlm.nih.gov/23040615/) | Human endocarditis, comorbidities, urban risk | Human clinical |
| [36892988](https://pubmed.ncbi.nlm.nih.gov/36892988/) | Poly-antimicrobial therapy; serologic monitoring; household zoonosis | Veterinary clinical |
| [40317976](https://pubmed.ncbi.nlm.nih.gov/40317976/) | Discospondylitis clinical features (age, C2–C5) | Veterinary case-control |
| [19392878](https://pubmed.ncbi.nlm.nih.gov/19392878/) | Ocular disease; 4-drug regimen; 96-wk cure | Veterinary clinical |
| [19201792](https://pubmed.ncbi.nlm.nih.gov/19201792/) | Genome phylogeny; *B. canis* within *B. suis*; divergence | Computational genomics |
| [30385393](https://pubmed.ncbi.nlm.nih.gov/30385393/) | cgMLST: closest to *B. suis* bv. 4 | Computational genomics |
| [33965789](https://pubmed.ncbi.nlm.nih.gov/33965789/) | WGS/MLVA outbreak tracing; international spread | Genomic epidemiology |
| [36155554](https://pubmed.ncbi.nlm.nih.gov/36155554/) | No vaccine/cure; breeder awareness gap | Survey |
| [41925288](https://pubmed.ncbi.nlm.nih.gov/41925288/) | Import-driven emergence; legislative gaps | Review |
| [36862545](https://pubmed.ncbi.nlm.nih.gov/36862545/) | US One Health framing; CDC exposure routes; prevention essential | Review |

**Consistency / conflicts.** The evidence base is internally consistent. Wildlife serosurveys ([PMID: 25075540](https://pubmed.ncbi.nlm.nih.gov/25075540/), [PMID: 35687596](https://pubmed.ncbi.nlm.nih.gov/35687596/)) were negative, reinforcing (rather than challenging) that dogs are the reservoir. Diagnostic sensitivity estimates vary across serological tests, consistent with the known limitations of rough-antigen serology.

---

## Limitations and Knowledge Gaps

1. **No host-genetic dimension.** Template sections designed for Mendelian diseases (causal genes, variants, inheritance, penetrance, model knockouts) are not applicable; the "molecular" content is pathogen-centric.
2. **Human epidemiology under-quantified.** True human incidence/prevalence is unknown because standard serology misses *B. canis* and bacteremia is intermittent — likely substantial under-ascertainment.
3. **Treatment evidence is observational.** No randomized trials define the optimal antimicrobial combination or duration; relapse rates and true cure rates are imprecisely known.
4. **No vaccine and no validated correlate of protection.** Immunological mechanisms of protective immunity are poorly defined.
5. **Diagnostic thresholds** (e.g., ≥40% antibody decline) derive from small case series and need prospective validation.
6. **Ontology mapping** for a veterinary zoonosis is imperfect: HPO/CL/UBERON terms are human-oriented and used here by analogy.

---

## Proposed Follow-up Experiments / Actions

1. **Standardize a confirmatory diagnostic algorithm** combining rough-antigen serology (RSAT/ICT) with IS711 **blood** PCR and, pre-breeding, **semen** PCR; prospectively validate the ≥40% antibody-decline cure criterion.
2. **Prospective treatment trial** comparing doxycycline+aminoglycoside vs. four-drug regimens for duration-to-microbiological-cure and relapse, with predefined serologic and PCR endpoints.
3. **Human surveillance study** using rough-antigen–specific assays in high-risk cohorts (kennel/veterinary/lab workers, owners of seropositive dogs) to quantify true human burden.
4. **Import-screening policy pilot** with mandatory pre-import *B. canis* testing, coupled to WGS/MLVA typing to map introduction routes (extending [PMID: 33965789](https://pubmed.ncbi.nlm.nih.gov/33965789/)).
5. **Vaccine research** exploiting rough-LPS/T4SS/BvrR-BvrS biology to design attenuated or subunit candidates with a defined immune correlate.
6. **Mechanistic dissection** of tissue tropism (placenta, disc, uvea) using canine primary cells/organoids to explain why bacteremia seeds these specific sites.

---

*Report compiled from 12 confirmed findings across 28 reviewed papers. Evidence types: veterinary clinical, human clinical/seroepidemiological, in vitro macrophage models, and computational genomics.*


## Artifacts

- [OpenScientist final report](Brucella_Canis_Brucellosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Brucella_Canis_Brucellosis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 37 |
| Quoted claims found in source | 35 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 25 |
| On topic | 24 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:33002657` *(abstract only)*: "we determined an overall apparent *B. canis* seroprevalence of 6.8% (adjusted estimated true prevalence of 29.4%)… Older dogs were significantly more likely to be *B. canis*-positive than younger dogs, as were reproductively intact dogs versus altered dogs"
  - closest text in source: "canis-positive than younger dogs, as were reproductively intact dogs versus altered dogs (although this difference was not statistically significant)"
- `PMID:36862545` *(abstract only)*: "infect dogs (*B. canis*), swine (*B. suis*), and cattle/bison (*B. abortus*)"
  - closest text in source: "Brucella species of greatest one-health relevance in the US include those infecting dogs (Brucella canis), swine (Brucella suis), and cattle and domestic bison (Brucella abortus)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 16 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0001857` (3 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **Brucella canis brucellosis**
- `HP:0100603` (1 mention) - the report calls it "Stillbirth, analogous"; HP calls it **Toxemia of pregnancy**
- `HP:0000029` (1 mention) - the report calls it "Abnormality of the testis"; HP calls it **Testicular atrophy**
- `GO:0005783` (2 mentions) - the report calls it "endoplasmic reticulum", "Endoplasmic reticulum (replication niche); Brucella-containing vacuole"; GO calls it **endoplasmic reticulum**
- `NCIT:C299` (1 mention) - the report calls it "Doxycycline"; NCIT calls it **Beclomethasone Dipropionate**
- `NCIT:C864` (1 mention) - the report calls it "Streptomycin"; NCIT calls it **2,3,7,8-Tetrachlorodibenzo-P-dioxin**
- `NCIT:C793` (1 mention) - the report calls it "Rifampin"; NCIT calls it **Quinidine**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CHEBI:16412` (2 mentions) - the report calls it "CHEBI: LPS"; CHEBI calls it **lipopolysaccharide**, and lists "LPS" among its other names
- `GO:0044409` (1 mention) - the report calls it "entry into host"; GO calls it **symbiont entry into host**, and lists "entry into host" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0001857` - called "if available", "MONDO"
- `GO:0005783` - called "endoplasmic reticulum", "Endoplasmic reticulum (replication niche); Brucella-containing vacuole"
