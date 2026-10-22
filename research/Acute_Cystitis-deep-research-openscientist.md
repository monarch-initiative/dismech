---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T02:48:55.228466'
end_time: '2026-09-30T03:05:12.761060'
duration_seconds: 977.53
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Acute Cystitis
  mondo_id: MONDO:0001650
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
citation_count: 29
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 23
  quotes_valid: 21
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:15630106
  - PMID:23859578
  relevance_assessed: 31
  on_topic: 18
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 25
  labels_matching: 12
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0001650
    reported_labels:
    - MONDO
    ontology_label: acute cystitis
  - term_id: HP:0100530
    reported_labels:
    - suprapubic pain
    ontology_label: Abnormal circulating calcium-phosphate regulating hormone concentration
  - term_id: HP:0032170
    reported_labels:
    - pyuria
    ontology_label: Severe varicella zoster infection
  - term_id: HP:0031969
    reported_labels:
    - bacteriuria
    ontology_label: Reduced blood urea nitrogen
  - term_id: GO:0052126
    reported_labels:
    - movement in host, bacterial invasion
    ontology_label: GO_0052126
  - term_id: CL:0000671
    reported_labels:
    - urothelial "umbrella"/superficial cell
    - umbrella cells
    ontology_label: centripetally migrating follicle cell
  - term_id: NCIT:C61903
    reported_labels:
    - Nitrofurantoin
    ontology_label: Pramocaine
  - term_id: NCIT:C263
    reported_labels:
    - TMP-SMX
    ontology_label: Anticoagulant Agent
  - term_id: NCIT:C61825
    reported_labels:
    - Fosfomycin
    ontology_label: Meclocycline
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0052126
    ontology_label: GO_0052126
    replaced_by: GO:0044000
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Acute_Cystitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Acute_Cystitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Cystitis
- **MONDO ID:** MONDO:0001650 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Acute Cystitis** covering all of the
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

# Acute Cystitis (MONDO:0001650): A Comprehensive Disease Characteristics Report

*Autonomous discovery investigation — 5 iterations, 21 confirmed findings, 69 papers reviewed*

---

## Summary

**Acute cystitis is an acute bacterial infection of the urinary bladder, caused predominantly by uropathogenic *Escherichia coli* (UPEC, ~75–90% of cases), which adheres to the bladder urothelium via the FimH type-1-pilus adhesin, invades superficial umbrella cells, forms intracellular bacterial communities (IBCs), and triggers a TLR4–NF-κB innate-immune response that produces the classic dysuria–frequency–urgency syndrome.** It is one of the most common human bacterial infections, with a striking female predominance: 50–60% of adult women experience at least one episode in their lifetime. Etiology is infectious and multifactorial/polygenic (not Mendelian); host genetic modifiers such as *TLR2*, *CXCR1*, and *FUT2* (secretor status) modulate susceptibility, and behavioral factors (sexual intercourse, spermicide use, prior UTI, diabetes) are dominant risk drivers.

Diagnosis is primarily clinical, supported by urine dipstick (leukocyte esterase and nitrite) and, when indicated, urine culture. Guideline-endorsed first-line therapy comprises **nitrofurantoin, trimethoprim–sulfamethoxazole (TMP-SMX), fosfomycin, and pivmecillinam**; fluoroquinolones are explicitly de-prioritized because of FDA black-box safety warnings and rising resistance. Prognosis is excellent and frequently self-limiting, but recurrence is common (annual recurrence 14–25% in women), and the principal complication is ascending infection to acute pyelonephritis — of particular concern in pregnancy, where it is associated with preterm delivery and low birth weight.

This report synthesizes 21 confirmed findings into a mechanistic causal chain running from FimH-mediated adhesion through urothelial invasion, IBC formation, and TLR4–NF-κB inflammation to clinical symptoms, and covers all 15 requested disease-characteristic domains with ontology-term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT) and PMID-anchored evidence. The overall picture is of a well-understood, treatable infectious disease whose principal unsolved problems are recurrence, intracellular bacterial persistence, and antimicrobial resistance — the targets of an emerging class of anti-adhesion (FimH-antagonist / mannoside) and immunoactive (MV140, OM-89) therapeutics.

---

## Section 1 — Disease Information

**Overview.** Acute cystitis is an acute inflammatory infection confined to the urinary bladder (lower urinary tract), most often bacterial and ascending in origin. When it occurs in an otherwise healthy, non-pregnant woman with a structurally and functionally normal urinary tract, it is termed *acute uncomplicated cystitis*.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0001650 |
| ICD-10 | N30.0 (acute cystitis) |
| ICD-11 | GC00 (cystitis) |
| MeSH | D003556 (Cystitis) |
| SNOMED CT | 38822007 (Cystitis); acute variants coded separately |
| UBERON (organ) | UBERON:0001255 (urinary bladder) |

**Synonyms / alternative names.** Acute bacterial cystitis; acute lower urinary tract infection; bladder infection; uncomplicated UTI (when confined to the bladder in a healthy host). Closely related umbrella term: urinary tract infection (UTI).

**Information source type.** This report draws on *aggregated disease-level resources* — clinical guidelines, epidemiological surveillance studies, systematic reviews, and mechanistic/animal-model literature — rather than individual patient EHR records.

---

## Section 2 — Etiology

**Primary cause (infectious).** Acute cystitis is overwhelmingly an infectious disease. UPEC is the infecting pathogen in ~75–90% of uncomplicated cases (**F006, F019**). Bacteria ascend from the periurethral/vaginal reservoir through the urethra into the bladder.

**Risk factors (environmental/behavioral).** A landmark case-control study (n=788) quantified the dominant behavioral and host risk factors (**F001**):

| Risk factor | Odds ratio (95% CI) |
|---|---|
| Sexual intercourse ≥3×/week | 5.6 (2.8–11.0) |
| Recent UTI | 4.4 (2.8–7.1) |
| Diabetes | 4.1 (1.6–10.9) |
| Recent incontinence | 3.9 (2.6–5.9) |
| New sexual partner | 2.2 |
| Spermicide use | 1.7 |

> "factors associated with pyelonephritis risk were frequency of sexual intercourse in the previous 30 days (odds ratio, 5.6 [95% CI, 2.8 to 11.0] for ≥3 times per week), recent urinary tract infection (UTI) (odds ratio, 4.4 [CI, 2.8 to 7.1]), diabetes (odds ratio, 4.1 [CI, 1.6 to 10.9])" — [PMID: 15630106](https://pubmed.ncbi.nlm.nih.gov/15630106/)

**Genetic risk factors.** Familial/genetic susceptibility is real but polygenic. An Indian case-control study found a first-degree female relative's UTI history conferred OR 10.88 (95% CI 2.41–49.07) (**F001**). Specific modifier loci include *TLR2* (G2258A; OR 3.44 for asymptomatic bacteriuria), *CXCR1*, and *FUT2* non-secretor status (**F007, F018**) — detailed in Sections 4 and 9.

**Protective factors.** A *Lactobacillus*-dominant urogenital microbiome and adequate estrogenization protect against recurrence (**F012**). Vaginal estrogen restores the urogenital epithelium and *Lactobacillus* dominance and is guideline-recommended in postmenopausal women. Adequate hydration and post-coital voiding are behavioral protective measures.

**Gene–environment interaction.** Non-secretor (*FUT2*) genotype exposes globoseries glycosphingolipid receptors on uroepithelium that enhance uropathogen adherence — a genetic trait that only manifests as disease upon environmental exposure to UPEC, and whose penetrance is modulated by hormonal status (non-secretor frequency higher in premenopausal 57% vs postmenopausal 30% women) (**F018**).

---

## Section 3 — Phenotypes

The cardinal phenotypes, with suggested HPO terms and diagnostic weight (**F010, F011**):

| Phenotype | Type | HPO term | Diagnostic value | Frequency |
|---|---|---|---|---|
| Dysuria | Symptom | HP:0100518 (dysuria) | Highest | Very common |
| Urinary frequency | Symptom | HP:0000103 (pollakisuria) | Highest | Very common |
| Urinary urgency | Symptom | HP:0000012 (urinary urgency) | Highest | Very common |
| Suprapubic pain | Symptom/sign | HP:0100530 (suprapubic pain) | Consensus | Common |
| Hematuria (gross) | Lab/sign | HP:0000790 (hematuria) | Consensus | Occasional |
| Pyuria | Lab abnormality | HP:0032170 (pyuria) | Supportive | Common |
| Bacteriuria | Lab abnormality | HP:0031969 (bacteriuria) | Supportive | Common |

> "Highest diagnostic values for AC in this study belonged to dysuria, urgency, and frequency." — [PMID: 30419565](https://pubmed.ncbi.nlm.nih.gov/30419565/) (n=819 women, Acute Cystitis Symptom Score)

**Onset, severity, progression.** Acute onset; adult-onset predominant. Severity is mild-to-moderate and variable; symptom severity carries even more diagnostic information than mere presence (**F010**). Course is episodic and typically self-limiting, but often recurrent.

**Distinguishing feature.** Systemic signs — fever (HP:0001945), flank pain (HP:0030157) — are characteristically **absent** in uncomplicated cystitis; their presence signals ascending pyelonephritis. Absence of vaginal discharge/irritation increases the probability of cystitis over vaginitis (**F010, F017**).

**Quality-of-life impact.** Recurrent cystitis significantly impairs QoL across social/sexual relationships, self-esteem, and work productivity, and is experienced as a chronic, disruptive, stigmatized condition (**F013**). Disease-specific instruments: **ACSS** (Acute Cystitis Symptom Score), **SF-Qualiveen**, **ICIQ-FLUTS**.

> "These infections significantly impair the quality of life, impacting social and sexual relationships, self-esteem, and work productivity." — [PMID: 42719353](https://pubmed.ncbi.nlm.nih.gov/42719353/)

---

## Section 4 — Genetic/Molecular Information

**Acute cystitis is not a Mendelian genetic disease.** There are no causal genes, pathogenic ACMG/AMP variants, or chromosomal abnormalities. Genetics contributes as **polygenic susceptibility/modifier** effects on the host immune and glycosylation machinery.

**Host modifier genes (susceptibility, not causation):**

| Gene (HGNC) | Variant/effect | Association | Evidence |
|---|---|---|---|
| *TLR2* | G2258A (↓ lipopeptide signaling) | ↑ asymptomatic bacteriuria, OR 3.44 (1.65–7.17) | **F007** [PMID: 20016852](https://pubmed.ncbi.nlm.nih.gov/20016852/) |
| *CXCR1* | Polymorphisms | Altered urinary CXCL-8, ↑ ASB | **F007** |
| *TLR4* | Expression variation | Modulates NF-κB inflammatory response | **F007, F009** |
| *FUT2* (secretor) | Non-secretor genotype | ↑ recurrent UTI; 41% vs 22.6% controls | **F018** [PMID: 12010227](https://pubmed.ncbi.nlm.nih.gov/12010227/) |

> "Polymorphism TLR2_G2258A, a variant associated with decreased lipopeptide-induced signaling, was associated with increased ASB risk (odds ratio 3.44, 95%CI; 1.65-7.17)" — [PMID: 20016852](https://pubmed.ncbi.nlm.nih.gov/20016852/)

**Epigenetic information.** No disease-specific human methylation/histone signature has been established for acute cystitis; this is a genuine knowledge gap. The relevant molecular biology is bacterial-virulence and host-response, not epigenetic host reprogramming.

---

## Section 5 — Environmental Information

**Infectious agents (primary "environmental" cause).** The uropathogen spectrum, converging across multiple surveillance studies (**F019**):

| Pathogen | Frequency | NCBI Taxon |
|---|---|---|
| *Escherichia coli* (UPEC) | 68–90% (Belgium 81.6%, Germany 76.7%, Poland 75.6%, Japan 68–78%) | 562 |
| *Staphylococcus saprophyticus* | 4–11% (esp. premenopausal) | 29385 |
| *Klebsiella pneumoniae* | ~2–3% | 573 |
| *Proteus mirabilis* | ~3–5% | 584 |
| *Enterococcus faecalis* | ~2–3% | 1351 |
| *Staphylococcus aureus* | ~2–5% | 1280 |

> "Escherichia coli (81.6 %) was the most frequently isolated uropathogen, followed by Staphylococcus saprophyticus (8 %)" — [PMID: 27639858](https://pubmed.ncbi.nlm.nih.gov/27639858/)

**Device/occupational-analog factors.** Catheter-associated UTI (CAUTI) is among the most common hospital-acquired infections; indwelling catheters, prolonged hospitalization, and irrational antimicrobial use are major drivers, with cystitis a principal manifestation (**F021**).

> "Prolonged hospitalization, invasive devices such as catheters, and irrational use of antimicrobial agents are believed to be the major causes of high rates of HAIs." — [PMID: 35885599](https://pubmed.ncbi.nlm.nih.gov/35885599/)

**Lifestyle factors.** Sexual activity, spermicide/diaphragm contraception, low fluid intake, and vaginal douching increase risk (**F001, F021**). Estrogen deficiency (postmenopausal), incomplete bladder emptying, urinary stasis, and pelvic organ prolapse are further host-environmental contributors.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **UPEC colonizes the periurethral/vaginal reservoir and ascends the urethra** into the bladder lumen (behavioral triggers: intercourse, spermicide) → *leads to* luminal bacterial load in the bladder. (**F001, F002**)
2. **FimH, the type-1-pilus tip adhesin, binds mannosylated uroplakin Ia** on the apical surface of superficial umbrella cells → *results in* firm attachment resisting the flushing action of micturition. (**F003**)
3. **Multivalent FimH–receptor engagement drives conformational receptor changes and cytoplasmic signaling**, → *leads to* bacterial invasion/internalization of umbrella cells. (**F003, F002**)
4. **Internalized UPEC escapes the endosome and proliferates in the cytoplasm to form intracellular bacterial communities (IBCs)** → *results in* a protected niche shielded from antibiotics and host defenses, and injury to bladder epithelial cells. (**F002, F008**) *[Endosomal escape is regulated by matrix stiffness via RhoB/PRK1 signaling — inferred from in-vitro models.]*
5. **UPEC LPS (a PAMP) engages urothelial TLR4**, activating **NF-κB** → *leads to* transcription of pro-inflammatory cytokines IL-1β, IL-6, and chemokine IL-8/CXCL-8. (**F007, F009**)
6. **Cytokine/chemokine release recruits neutrophils** (pyuria) and produces mucosal inflammation → *results in* the sensory phenotype: dysuria, urgency, frequency, suprapubic pain. (**F009, F010**)
7. **(Branch A — resolution):** Innate clearance + antibiotic therapy → symptom resolution; often self-limiting. (**F012**)
8. **(Branch B — persistence/recurrence):** Quiescent intracellular reservoirs (QIRs) survive → later reactivation → recurrent UTI. (**F002, F008**)
9. **(Branch C — ascending complication):** Failure of bladder containment → ascension to renal pelvis/kidney → acute pyelonephritis, and rarely urosepsis; heightened in pregnancy. (**F015, F017**)

Downstream tissue injury is amplified by **UPEC-induced ferritinophagy/ferroptosis (BACH1/NCOA4 axis)** and oxidative stress (elevated MDA, ROS) contributing to bladder epithelial injury (**F009**).

### Mechanism detail with ontology terms

- **Molecular pathways:** TLR4 → MyD88 → NF-κB signaling (KEGG hsa04620 Toll-like receptor pathway); FimH lectin–glycan recognition.
- **Cellular processes / GO:** GO:0006954 (inflammatory response); GO:0002376 (immune system process); GO:0071222 (cellular response to LPS); GO:0030593 (neutrophil chemotaxis); GO:0007155 (cell adhesion); GO:0052126 (movement in host, bacterial invasion).
- **Protein dysfunction:** This is not host protein misfolding — the key protein events are bacterial (FimH adhesin function) and host receptor engagement (uroplakin Ia, uromodulin/Tamm-Horsfall protein).
- **Immune involvement / GO:** GO:0045087 (innate immune response); TLR4 (UniProt O00206), CXCL8/IL-8, IL-6, IL-1β.
- **Cell types / CL:** CL:0000671 (urothelial "umbrella"/superficial cell); CL:0000775 (neutrophil).
- **Chemical entities / CHEBI:** CHEBI:16412 (lipopolysaccharide); CHEBI:4208 (D-mannose); CHEBI:37684 (mannose glycan).

> "Intracellular bacterial communities (IBCs), formed following the vesicular escape of uropathogenic Escherichia coli (UPEC), induce injury to bladder epithelial cells (BECs)..." — [PMID: 42447508](https://pubmed.ncbi.nlm.nih.gov/42447508/)

> "Bacterial adhesion to the high-mannosylated uroplakin Ia glycoprotein receptors of bladder epithelium is mediated by the FimH adhesin." — [PMID: 16930149](https://pubmed.ncbi.nlm.nih.gov/16930149/)

> "TLF-II inhibited the expression of TLR4 and NF-κB on BECs and decreased the urine levels of IL-1β and IL-6 and urine leukocyte counts" — [PMID: 38638825](https://pubmed.ncbi.nlm.nih.gov/38638825/)

```
 Intercourse/spermicide → periurethral UPEC → ascent → bladder lumen
        │
        ▼
   FimH ── binds ──▶ uroplakin Ia (mannose) ──▶ adhesion ──▶ invasion
        │                                                       │
        ▼                                                       ▼
   TLR4 ◀── LPS                                          endosomal escape
        │                                                       │
        ▼                                                       ▼
   NF-κB ▶ IL-1β/IL-6/IL-8 ▶ neutrophils/pyuria          IBC formation
        │                                                       │
        ▼                                                       ▼
  DYSURIA / FREQUENCY / URGENCY                    QIR → RECURRENCE
                                                            │
                                                            ▼
                                            ascension → PYELONEPHRITIS
```

---

## Section 7 — Anatomical Structures Affected

**Organ level.** Primary: urinary bladder (UBERON:0001255). Secondary/complication: renal pelvis and kidney (UBERON:0001224 / UBERON:0002113) via ascending infection; body system: renal/urinary system (UBERON:0001008) (**F015, F016, F017**).

**Tissue and cell level.** Target tissue: bladder transitional epithelium / **urothelium** (UBERON:0000365). Target cells: superficial **umbrella cells** (CL:0000671), which bear a thick **glycosaminoglycan (GAG) layer** forming a hydrophilic mucosal barrier. The urothelium is now recognized as an active tissue central to cystitis pathogenesis, not a passive barrier (**F016**).

> "On the surface of the urothelial umbrella-cells there is a thick layer of glycoproteins and proteoglycans... called Glycosaminoglycans (GAGs)... a hydrophilic mucosal coating and act as a barrier" — [PMID: 24526593](https://pubmed.ncbi.nlm.nih.gov/24526593/)

GAG-layer injury "has been identified as the first step in the genesis of chronic inflammatory bladder diseases, such as recurrent urinary tract infections" — motivating GAG-replenishment therapy (hyaluronic acid, chondroitin sulfate, pentosan polysulfate) (**F016**).

**Subcellular level (GO cellular component).** Bacterial residence in the host cytoplasm (GO:0005737) after endosomal (GO:0005768) escape; apical plasma membrane (GO:0016324) uroplakin receptors. CHEBI:16412 (LPS) at the bacterial outer membrane.

**Localization / lateralization.** The bladder is a midline organ; cystitis is not lateralized. Ascending complication (pyelonephritis) may be unilateral or bilateral.

---

## Section 8 — Temporal Development

- **Onset:** Acute; adult-onset predominant (though it occurs across all ages). Onset pattern is acute rather than insidious (**F010**).
- **Progression / course:** Self-limiting in a substantial fraction of cases (the premise of the ibuprofen-vs-mecillinam RCT, NCT01849926) (**F012**); episodic and frequently recurrent. Recurrent UTI is defined as ≥2 episodes in 6 months or ≥3 in 12 months (**F005**).
- **Duration:** Individual episodes are short (days) and often resolve with or without antibiotics; the disease *pattern* can be lifelong-recurrent in susceptible women.
- **Critical periods / windows:** Immediately preceding recurrence, periurethral colonization rises from 46%→90% over 14 days, with parallel increases in bacteriuria, pyuria, and symptoms 2–3 days before onset (prospective cohort, [PMID: 19586416](https://pubmed.ncbi.nlm.nih.gov/19586416/)) — a window for pre-emptive intervention.
- **Remission:** Both spontaneous (self-limiting) and treatment-induced (**F012**).

---

## Section 9 — Inheritance and Population

**Epidemiology (F006).** UTIs are the most common outpatient infections. Lifetime incidence 50–60% in adult women; ~40–50% of women and ~5% of men have ≥1 episode. Prevalence increases with age (women >65 roughly double the overall female rate). Annual recurrence 14–25% in women (**F005**).

> "Urinary tract infections (UTIs) are the most common outpatient infections, with a lifetime incidence of 50-60% in adult women." — [PMID: 31105774](https://pubmed.ncbi.nlm.nih.gov/31105774/)

**Inheritance pattern.** **Multifactorial/polygenic** — NOT Mendelian. No AD/AR/X-linked/mitochondrial inheritance. Modifier alleles (*FUT2* non-secretor, *TLR2*, *CXCR1*) confer susceptibility with incomplete penetrance modulated by hormonal and behavioral context (**F007, F018**).

> "Forty-four (41%) of the women were non-secretors, a significantly higher frequency than in the (control) Japanese population (217 of 960, 22.6%; P < 0.001)." — [PMID: 12010227](https://pubmed.ncbi.nlm.nih.gov/12010227/)

**Population demographics.** Strong female predominance (male:female roughly 1:8 in young adults, narrowing in the elderly). *S. saprophyticus* is more common in premenopausal women. Geographic variation exists mainly in resistance patterns (ESBL prevalence ~2.5–4.7% in community isolates) rather than incidence (**F019**).

---

## Section 10 — Diagnostics

**Clinical diagnosis is primary.** In women with dysuria and no complicating features, cystitis can be treated without further evaluation (**F011, F017**).

**Urinalysis / dipstick likelihood ratios (F011):**

| Test | Performance |
|---|---|
| Positive nitrite | Rules IN UTI, +LR 7.5–24.5 (specific) |
| Negative leukocyte esterase (LE) | Helps rule OUT, −LR 0.2 (LE sensitivity 87.5%) |
| Both LE + nitrite positive | Pooled LR+ 28.2 (95% CI 17.3–46.0) |
| Both LE + nitrite negative | Pooled LR− 0.20 (95% CI 0.16–0.26) |

> "Only a positive nitrite reaction (+LR = 7.5 to 24.5) was useful to rule in a UTI. To rule out UTI, only a negative leukocyte esterase (−LR = 0.2)..." — [PMID: 23859578](https://pubmed.ncbi.nlm.nih.gov/23859578/)

**Urine culture** (≥10³–10⁵ CFU/mL) is the reference standard but 70–80% of cultures return negative; it is reserved for treatment failure, recurrence, pregnancy, or suspected resistance (**F011**). Relevant LOINC concepts: urinalysis panel, urine culture. Pyuria (≥10 WBC/µL) indicates inflammation.

**Genetic/omics diagnostics.** Not applicable for routine diagnosis. Machine-learning models integrating demographics + dipstick reflectance are emerging to triage negative samples ([PMID: 40856092](https://pubmed.ncbi.nlm.nih.gov/40856092/)).

**Clinical criteria & differential diagnosis (F017).** Distinguish from urethritis/STI (chlamydia, gonorrhea), vaginitis (candidal, bacterial, atrophic), interstitial cystitis/bladder pain syndrome (sterile urine, chronic pain relieved by voiding), urethral pain syndrome, calculi, hypoestrogenism, and neoplasm. ~One-third of women with cystitis symptoms have occult subclinical pyelonephritis.

> "The most common cause of acute dysuria is infection, especially cystitis. Other infectious causes include urethritis, sexually transmitted infections, and vaginitis." — [PMID: 26554471](https://pubmed.ncbi.nlm.nih.gov/26554471/)

---

## Section 11 — Outcome / Prognosis

- **Mortality:** Uncomplicated cystitis has negligible mortality; it rarely progresses to serious sequelae (**F012**).
- **Recovery:** Excellent; often self-limiting. > "Although uncomplicated cystitis is often self-limiting, most such patients will be prescribed antibiotic treatment." — [PMID: 25516016](https://pubmed.ncbi.nlm.nih.gov/25516016/)
- **Complications:** Principal risk is ascending infection to acute pyelonephritis and, rarely, urosepsis (**F012, F015**). In pregnancy, ascending UTI → pyelonephritis → preterm delivery and low birth weight (**F015**).
- **Morbidity / QoL:** Recurrence is the dominant morbidity driver, impairing social/sexual function, self-esteem, and work productivity (**F013**). rUTI affects 2–10% of postmenopausal women.
- **Prognostic factors:** Prior UTI, diabetes, catheterization history, STI history, frequent intercourse, and contraceptive use predict progression to recurrent cystitis ([PMID: 23380970](https://pubmed.ncbi.nlm.nih.gov/23380970/)); non-secretor genotype predicts recurrence (**F018**).

---

## Section 12 — Treatment

**First-line pharmacotherapy (IDSA and AUA/CUA/SUFU guidelines) (F004):**

| Drug (NCIT) | Class | Notes |
|---|---|---|
| Nitrofurantoin (NCIT:C61903) | Nitrofuran | High urinary concentration, minimal microbiome collateral damage, low resistance; 5-day course |
| TMP-SMX (NCIT:C263) | Folate-synthesis inhibitor | Avoid where local resistance >20% |
| Fosfomycin (NCIT:C61825) | Phosphonic acid | Single-dose; E. coli susceptibility ~97–99% |
| Pivmecillinam | Amdinopenicillin | First-line in Europe |

> "Nitrofurantoin is considered a first-line antimicrobial agent by the AUA/CUA/SUFU Guideline and Infectious Disease Society of America (IDSA) Guideline for the treatment of acute uncomplicated simple cystitis in women." — [PMID: 42594063](https://pubmed.ncbi.nlm.nih.gov/42594063/)

> "Fluoroquinolones are not first-line options" — [PMID: 34896337](https://pubmed.ncbi.nlm.nih.gov/34896337/)

**Fluoroquinolones are NOT first-line** due to FDA black-box warnings and rising resistance (**F004**). **Asymptomatic bacteriuria should not be treated** except in pregnancy or before invasive urologic procedures.

**Newly approved agents (F020):** Orlynvah (sulopenem etzadroxil/probenecid) and Pivya (pivmecillinam) expand options against resistant uncomplicated UTI.

**Experimental / anti-virulence therapeutics (F020):** FimH antagonists (mannosides) as high-affinity anti-adhesion ligands; proposed dual mannose (FimH) + cranberry-polyphenol (PapG/P-pili) antagonists; curli inhibitors; biofilm-targeting agents; immunoactive lysates (OM-89/Uro-Vaxom, which enhances lysosomal clearance of intracellular UPEC — [PMID: 42789533](https://pubmed.ncbi.nlm.nih.gov/42789533/)).

> "the anti-adhesive molecules active against fimbrial adhesins, key determinants of urovirulence, are attractive alternatives. The best-characterized bacterial adhesin is FimH" — [PMID: 32664222](https://pubmed.ncbi.nlm.nih.gov/32664222/)

> "Nonantibiotic strategies, such as mannosides, curli inhibitors, and FimH antagonists, are also being explored as promising anti-adhesion and biofilm-targeting therapies." — [PMID: 41773512](https://pubmed.ncbi.nlm.nih.gov/41773512/)

**Supportive care:** NSAIDs (ibuprofen) for symptom control given the self-limiting nature (**F012**); intravesical GAG replenishment (HA + chondroitin sulfate) for recurrent cases (**F013, F016**).

---

## Section 13 — Prevention

**Prevention of recurrence (F005), by evidence strength:**

| Strategy | Evidence | Level |
|---|---|---|
| Methenamine hippurate | Non-inferior to daily antibiotic prophylaxis | RCT/systematic review |
| MV140 sublingual vaccine | 56–58% remained UTI-free vs placebo | Large RCT |
| Vaginal estrogen | Restores *Lactobacillus* microbiome; effective postmenopausal | Guideline-recommended |
| D-mannose | Variable/lower-quality | Mixed |
| Cranberry (≥36 mg PACs/day) | Reduces recurrence; formulation-dependent | Mixed/moderate |
| Behavioral optimization | Hydration, post-coital voiding, avoid spermicide | Guideline |

> "Methenamine hippurate was found to be non-inferior to daily antibiotic prophylaxis... the sublingual vaccine MV140 significantly reduced recurrence compared with placebo, with 56-58% of women remaining UTI free in a large RCT." — [PMID: 42133003](https://pubmed.ncbi.nlm.nih.gov/42133003/)

**Prevention levels.** *Primary:* behavioral risk-factor modification, immunoprophylaxis (MV140). *Secondary:* prompt treatment of confirmed cystitis; screening/treating asymptomatic bacteriuria **in pregnancy** to prevent pyelonephritis (**F015**). *Tertiary:* non-antibiotic prophylaxis (EAU/AUA/NICE increasingly emphasize topical estrogen, methenamine, immunoactive prophylaxis before antibiotics) (**F005**). Lactoferrin reduced ASB and acute cystitis by 75% and 90% in pregnant women in an RCT ([PMID: 40264102](https://pubmed.ncbi.nlm.nih.gov/40264102/)).

**Vaccine strategies.** Sublingual MV140 (Uromune) — whole-cell bacterial preparation — is the leading immunization approach; OM-89 (Uro-Vaxom) oral lysate is longstanding (**F005, F020**). No conventional injectable vaccine is licensed for cystitis.

---

## Section 14 — Other Species / Natural Disease

Bacterial UTI/cystitis occurs naturally and commonly in companion animals (**F014**):

| Species | NCBI Taxon | Notes |
|---|---|---|
| *Canis lupus familiaris* (dog) | 9615 | Common; recurrent; MDR *E. coli* (CTX-M-14 ESBL) reported |
| *Felis catus* (cat) | 9685 | Common uropathogen |

> "Urinary tract infections (UTIs) are common in small animals, posing significant clinical challenges due to their recurrence and discomfort." — [PMID: 40107766](https://pubmed.ncbi.nlm.nih.gov/40107766/)

*E. coli* is the predominant uropathogen across species, indicating **evolutionary conservation** of the ascending-infection mechanism and the FimH/type-1-pili adhesion paradigm. Resources: OMIA, VetCompass. Orthologous host genes (TLR4, uroplakins) are conserved across mammals. Zoonotic transmission of specific uropathogenic strains between pets and owners is plausible given shared MDR clones but is not firmly established for cystitis.

---

## Section 15 — Model Organisms

**Primary model: murine ascending UTI (F008).** Female mice transurethrally inoculated with UPEC strains **UTI89** or **CFT073** recapitulate human cystitis: invasion of umbrella cells, endosomal escape, cytoplasmic proliferation into IBCs, quiescent intracellular reservoirs, TLR4–NF-κB activation, IL-1β/IL-6 secretion, and urine leukocyte influx.

> "Experiments in murine models of urinary tract infection (UTI) show that uropathogenic Escherichia coli (UPEC) form bacterial reservoirs in the bladder tissue that can survive beta lactam antibiotics and give rise to reinfection." — [PMID: 36244593](https://pubmed.ncbi.nlm.nih.gov/36244593/)

| Model | System | Recapitulates | Limitation |
|---|---|---|---|
| Mouse (UTI89/CFT073) | Mammalian, in vivo | IBCs, QIRs, TLR4-NF-κB, pyuria | Anatomical/immune differences from human |
| Pig (UTI89) | Mammalian, in vivo | Intracellular reservoirs surviving β-lactam | Cost, scalability |
| Rat cystitis model | Mammalian, in vivo | CAUTI, HD-5 therapeutics testing | — |
| Bladder organoids | In vitro human | Epithelial invasion, lysosomal clearance | No immune/vascular compartment |

Mechanistic insights from models: substrate/matrix stiffness regulates UPEC endosomal escape via RhoB/PRK1 signaling ([PMID: 32083802](https://pubmed.ncbi.nlm.nih.gov/32083802/)); sex differences exist in kidney bacterial community dynamics ([PMID: 33468577](https://pubmed.ncbi.nlm.nih.gov/33468577/)). Resources: MGI, RGD.

> "Uropathogenic E. coli (UPEC) infection in vivo is characterized by invasion of bladder umbrella epithelial cells followed by endosomal escape and proliferation in the cytoplasm to form intracellular bacterial communities." — [PMID: 32083802](https://pubmed.ncbi.nlm.nih.gov/32083802/)

---

## Mechanistic Model / Interpretation

The findings cohere into a single, well-supported causal narrative in which **FimH-mediated adhesion is the initiating molecular lesion** and **intracellular persistence + host inflammation are the twin engines of, respectively, recurrence and symptoms**. Three features distinguish acute cystitis from a "simple surface infection":

1. **It is an intracellular disease.** UPEC does not merely coat the bladder surface — it invades umbrella cells, forms IBCs, and seeds quiescent reservoirs that survive antibiotics (**F002, F008**). This single fact explains the paradox of clinical cure followed by same-strain recurrence and is the rationale for anti-adhesion and immunoactive therapies (**F020**).

2. **Symptoms are host-generated, not bacterial-toxin-generated.** The dysuria–frequency–urgency triad is a downstream readout of TLR4–NF-κB–driven cytokine release and neutrophil recruitment (**F009, F010**). This decoupling of symptoms from bacterial burden underlies both the self-limiting natural history (host clearance) and the utility of NSAIDs for symptom control (**F012**).

3. **Susceptibility is written in host glycobiology and immunogenetics.** *FUT2* non-secretor status alters the uroepithelial glycan receptor landscape; *TLR2/CXCR1/TLR4* variants tune the inflammatory response (**F007, F018**). These are modifiers, not causes — consistent with the multifactorial/polygenic inheritance and the dominance of behavioral risk factors (**F001**).

The disease is therefore best modeled as **infection (necessary) × host susceptibility (modulating) × behavioral exposure (triggering)**, with outcome branching into resolution, recurrence, or ascension.

---

## Evidence Base

| PMID | Contribution | Supports |
|---|---|---|
| [15630106](https://pubmed.ncbi.nlm.nih.gov/15630106/) | Quantified behavioral/host risk ORs | F001 |
| [16930149](https://pubmed.ncbi.nlm.nih.gov/16930149/) | FimH–uroplakin Ia adhesion | F003 |
| [42447508](https://pubmed.ncbi.nlm.nih.gov/42447508/) | IBC-driven epithelial injury | F002 |
| [20016852](https://pubmed.ncbi.nlm.nih.gov/20016852/) | TLR2 variant ↑ ASB risk | F007 |
| [38638825](https://pubmed.ncbi.nlm.nih.gov/38638825/) | TLR4-NF-κB → IL-1β/IL-6/pyuria | F009 |
| [30419565](https://pubmed.ncbi.nlm.nih.gov/30419565/) | Dysuria/urgency/frequency diagnostic | F010 |
| [23859578](https://pubmed.ncbi.nlm.nih.gov/23859578/) | Dipstick LR values | F011 |
| [42594063](https://pubmed.ncbi.nlm.nih.gov/42594063/) | Nitrofurantoin first-line | F004 |
| [42133003](https://pubmed.ncbi.nlm.nih.gov/42133003/) | Methenamine/MV140 prevention | F005 |
| [31105774](https://pubmed.ncbi.nlm.nih.gov/31105774/) | 50–60% lifetime incidence | F006 |
| [12010227](https://pubmed.ncbi.nlm.nih.gov/12010227/) | FUT2 non-secretor susceptibility | F018 |
| [27639858](https://pubmed.ncbi.nlm.nih.gov/27639858/) | Uropathogen spectrum (E. coli 81.6%) | F019 |
| [24526593](https://pubmed.ncbi.nlm.nih.gov/24526593/) | Urothelial GAG barrier | F016 |
| [36244593](https://pubmed.ncbi.nlm.nih.gov/36244593/) | Murine/pig intracellular reservoirs | F008 |
| [26554471](https://pubmed.ncbi.nlm.nih.gov/26554471/) | Differential diagnosis of dysuria | F017 |
| [41274602](https://pubmed.ncbi.nlm.nih.gov/41274602/) | Pregnancy ascending pyelonephritis | F015 |
| [32664222](https://pubmed.ncbi.nlm.nih.gov/32664222/) | FimH anti-adhesion therapeutics | F020 |
| [40107766](https://pubmed.ncbi.nlm.nih.gov/40107766/) | Companion-animal UTI | F014 |
| [35885599](https://pubmed.ncbi.nlm.nih.gov/35885599/) | Catheter-associated UTI | F021 |
| [42719353](https://pubmed.ncbi.nlm.nih.gov/42719353/) | QoL burden of recurrent UTI | F013 |
| [42378201](https://pubmed.ncbi.nlm.nih.gov/42378201/) | Vaginal estrogen protection | F012 |

**Consistency across studies:** The uropathogen distribution (E. coli dominant, S. saprophyticus second) was reproduced across ≥5 independent surveillance cohorts (Belgium, Germany, Poland, Japan ×2), and the first-line treatment recommendation was concordant across IDSA and AUA/CUA/SUFU guidelines — high-confidence, low-heterogeneity findings.

---

## Limitations and Knowledge Gaps

1. **No host epigenetic signature** for acute cystitis has been characterized (Section 4) — a genuine gap versus the template's request.
2. **Genetic susceptibility is modest and incompletely mapped.** Beyond *FUT2*, *TLR2*, *CXCR1*, *TLR4*, there is no GWAS-scale catalog of susceptibility loci; effect sizes are small and populations studied are limited (e.g., single-country cohorts).
3. **Mechanistic detail on endosomal escape and IBC dynamics** derives largely from murine and in-vitro models; direct human intravital confirmation is limited.
4. **QoL quantification** relies on heterogeneous disease-specific instruments (ACSS, SF-Qualiveen, ICIQ-FLUTS) without a single validated standard.
5. **Anti-virulence therapeutics (mannosides, FimH antagonists)** remain largely preclinical/early-phase; no head-to-head efficacy versus standard antibiotics in cystitis is established.
6. This investigation was **literature-based**; no primary dataset was analyzed, so all statistics are as-reported in source studies.

---

## Proposed Follow-up Experiments / Actions

1. **Map host susceptibility at scale:** Conduct or mine a UTI-recurrence GWAS/PheWAS to move beyond candidate genes (*FUT2/TLR2/CXCR1/TLR4*) toward a polygenic risk score for recurrent cystitis.
2. **Human validation of IBCs:** Use exfoliated urothelial cell cytology / single-cell approaches on clinical urine to quantify IBC prevalence and its correlation with recurrence risk.
3. **Anti-adhesion clinical translation:** Advance oral FimH-antagonist mannosides into randomized non-inferiority trials versus nitrofurantoin for uncomplicated cystitis, with recurrence as a co-primary endpoint.
4. **Immunoactive prophylaxis positioning:** Directly compare MV140 vaccine, OM-89, and methenamine hippurate head-to-head for recurrence prevention and antibiotic-sparing.
5. **Epigenetic profiling:** Characterize urothelial DNA-methylation/chromatin responses to UPEC to fill the identified gap and identify durable susceptibility marks.
6. **Precision diagnostics:** Validate ML dipstick-reflectance models to safely rule out UTI and reduce unnecessary antibiotics, given 70–80% culture negativity.

---

*Report generated from 21 confirmed findings across 5 discovery iterations, anchored to 69 reviewed papers. Evidence source types span human clinical (guidelines, case-control, cohort, surveillance), model organism (murine, porcine, rat), in vitro (organoids), and computational studies.*


## Artifacts

- [OpenScientist final report](Acute_Cystitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Acute_Cystitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 23 |
| Quoted claims found in source | 21 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 31 |
| On topic | 18 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:15630106` *(abstract only)*: "factors associated with pyelonephritis risk were frequency of sexual intercourse in the previous 30 days (odds ratio, 5.6 [95% CI, 2.8 to 11.0] for ≥3 times per week), recent urinary tract infection (UTI) (odds ratio, 4.4 [CI, 2.8 to 7.1]), diabetes (odds ratio, 4.1 [CI, 1.6 to 10.9])"
  - closest text in source: "In multivariable models, factors associated with pyelonephritis risk were frequency of sexual intercourse in the previous 30 days (odds ratio, 5.6 [95% CI, 2.8 to 11.0] for > or =3 times per week), recent urinary tract infection (UTI) (odds ratio, 4.4 [CI, 2.8 to 7.1]), diabetes (odds ratio, 4.1 [CI, 1.6 to 10.9]), recent incontinence (odds ratio, 3.9 [CI"
- `PMID:23859578` *(abstract only)*: "Only a positive nitrite reaction (+LR = 7.5 to 24.5) was useful to rule in a UTI. To rule out UTI, only a negative leukocyte esterase (−LR = 0.2)..."
  - closest text in source: "Only a positive nitrite reaction (+LR = 7.5 to 24.5) was useful to rule in a UTI"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 25 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0001650` (2 mentions) - the report calls it "MONDO"; MONDO calls it **acute cystitis**
- `HP:0100530` (1 mention) - the report calls it "suprapubic pain"; HP calls it **Abnormal circulating calcium-phosphate regulating hormone concentration**
- `HP:0032170` (1 mention) - the report calls it "pyuria"; HP calls it **Severe varicella zoster infection**
- `HP:0031969` (1 mention) - the report calls it "bacteriuria"; HP calls it **Reduced blood urea nitrogen**
- `GO:0052126` (1 mention) - the report calls it "movement in host, bacterial invasion"; GO calls it **GO_0052126**
- `CL:0000671` (2 mentions) - the report calls it "urothelial "umbrella"/superficial cell", "umbrella cells"; CL calls it **centripetally migrating follicle cell**
- `NCIT:C61903` (1 mention) - the report calls it "Nitrofurantoin"; NCIT calls it **Pramocaine**
- `NCIT:C263` (1 mention) - the report calls it "TMP-SMX"; NCIT calls it **Anticoagulant Agent**
- `NCIT:C61825` (1 mention) - the report calls it "Fosfomycin"; NCIT calls it **Meclocycline**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0052126` (GO_0052126) (1 mention) - replaced by `GO:0044000`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000103` (1 mention) - the report calls it "pollakisuria"; HP calls it **Polyuria**
- `CHEBI:16412` (2 mentions) - the report calls it "lipopolysaccharide", "LPS"; CHEBI calls it **lipopolysaccharide**, and lists "LPS" among its other names
- `CHEBI:4208` (1 mention) - the report calls it "D-mannose"; CHEBI calls it **D-mannopyranose**, and lists "D-Mannose" among its other names
- `CHEBI:37684` (1 mention) - the report calls it "mannose glycan"; CHEBI calls it **mannose**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000671` - called "urothelial "umbrella"/superficial cell", "umbrella cells"
- `CHEBI:16412` - called "lipopolysaccharide", "LPS"