---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-11-24T16:14:37.990782'
end_time: '2026-11-24T16:20:30.588932'
duration_seconds: 352.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Tick Paralysis
  mondo_id: MONDO:0005981
  category: Injury
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: tick toxicosis
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 20
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 5
  off_topic: 1
  off_topic_references:
  - PMID:20237909
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 57
  verified: 55
  not_found: 1
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.018
  labels_checked: 40
  labels_matching: 19
  labels_mismatched: 14
  mislabelled_terms:
  - term_id: HP:0001285
    reported_labels:
    - Bulbar palsy
    ontology_label: Spastic tetraparesis
  - term_id: HP:0002353
    reported_labels:
    - Facial weakness
    ontology_label: EEG abnormality
  - term_id: HP:0002360
    reported_labels:
    - Dysphagia
    ontology_label: Sleep disturbance
  - term_id: HP:0002243
    reported_labels:
    - Diaphragmatic paralysis
    ontology_label: Protein-losing enteropathy
  - term_id: HP:0002340
    reported_labels:
    - Progressive motor impairment
    ontology_label: Caudate atrophy
  - term_id: HP:0002141
    reported_labels:
    - Gait instability
    ontology_label: Gait imbalance
  - term_id: GO:0050907
    reported_labels:
    - neuromuscular process controlling balance
    ontology_label: detection of chemical stimulus involved in sensory perception
  - term_id: NCIT:C51999
    reported_labels:
    - Surgical Removal
    ontology_label: Angioplasty
  - term_id: NCIT:C17248
    reported_labels:
    - Foreign Body Removal
    ontology_label: Genetic Variation
  - term_id: NCIT:C16084
    reported_labels:
    - Supportive Care
    ontology_label: Observational Study
  - term_id: NCIT:C21038
    reported_labels:
    - Respiratory Support Procedures
    ontology_label: Molecular Folding
  - term_id: NCIT:C15220
    reported_labels:
    - Preventive Health Services
    ontology_label: Diagnosis Assessment
  - term_id: NCIT:C17151
    reported_labels:
    - Vector Control Intervention
    ontology_label: South Africa
  - term_id: NCIT:C19157
    reported_labels:
    - Environmental Health Intervention
    ontology_label: Specimen
  labels_variant: 7
  unresolved_terms:
  - HP:0003471
  obsolete_terms:
  - term_id: NCIT:C21038
    ontology_label: Molecular Folding
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tick Paralysis
- **MONDO ID:** MONDO:0005981 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** tick toxicosis
- **Category:** Injury

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Tick Paralysis** covering all of the
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

# Tick Paralysis (MONDO:0005981): A Comprehensive Disease Characterization

Tick paralysis, corresponding to MONDO:0005981, is an acute, toxin-mediated neuroparalytic syndrome caused by salivary neurotoxins secreted by certain hard ticks during prolonged blood feeding, and no human causal gene has been identified; rather, the initiating lesion resides in tick-derived protein toxins (e.g., holocyclotoxin from *Ixodes holocyclus*), so the “causal gene” concept in this disease applies to tick genes encoding salivary toxins rather than host genes.[5][9][16][17] It is classically characterized by a prodrome of malaise and paresthesias followed by rapidly progressive ascending flaccid paralysis, frequently with cranial nerve involvement, and may culminate in respiratory failure and death if the attached tick is not promptly removed.[1][3][4][6][11][13][18][19][20] More than forty tick species worldwide can induce paralysis in humans or animals, with *Dermacentor andersoni* and *Dermacentor variabilis* predominating in North America and *Ixodes holocyclus* in eastern Australia.[5][6][9][16][19] Despite dramatic clinical presentations and frequent misdiagnosis as Guillain–Barré syndrome, botulism, or other acute neuromuscular disorders, paralysis is typically rapidly reversible, sometimes within hours, after complete removal of the engorged tick, making tick paralysis a striking example of a severe yet eminently preventable and curable neurotoxic poisoning.[1][3][4][6][11][13][18][19] This report synthesizes human and veterinary clinical data, mechanistic studies, and comparative pathology to populate a detailed disease knowledge entry for tick paralysis, emphasizing that it is an environmental injury (MONDO category: Injury), not a hereditary disorder, while still mapping its phenotypes, anatomical targets, pathophysiology, epidemiology, diagnostics, prognosis, and management into modern biomedical ontologies.

## 1. Disease Information

### Overview and Definition

Tick paralysis is a noninfectious neuromuscular syndrome resulting from inoculation of a neurotropic toxin produced in the salivary glands of certain ixodid ticks and delivered to the host during sustained blood feeding.[5][9][11][13][16][17] The National Library of Medicine’s MeSH descriptor defines tick paralysis succinctly as “paralysis caused by a neurotropic toxin secreted by the salivary glands of ticks,” classifying it under “Tick Toxicoses” within the broader tree of chemically induced disorders and bites/stings.[17] Clinically, it presents as acute or subacute ascending flaccid paralysis, often preceded by nonspecific symptoms such as malaise, fatigue, irritability, and paresthesias, progressing over hours to days from gait unsteadiness to limb weakness, cranial nerve dysfunction, and potentially respiratory muscle paralysis.[1][3][4][6][11][13][18][19][20] Unlike tick-borne infections such as Lyme disease or Rocky Mountain spotted fever, tick paralysis is not caused by bacteria or viruses; it is a pure toxin-mediated neurotoxic poisoning without systemic inflammatory or infectious features, and routine blood and cerebrospinal fluid investigations are usually normal.[6][11][13][18][19]

The syndrome afflicts humans, companion animals such as dogs and cats, livestock, wildlife, and occasionally birds and reptiles, with species-specific differences in typical clinical course and severity.[5][9][15][16] In humans, women and children are most often affected in Australian and North American series, although elderly outdoor workers may also present with severe paralysis.[6][13][18][19] A key defining feature is the dramatic reversibility of neurological deficits following meticulous removal of the engorged tick; numerous case reports describe substantial improvement within minutes to hours and complete recovery within one to two days, although more severe or delayed presentations may require longer convalescence.[1][3][4][6][18][19][20] This reversibility underscores the importance of timely recognition and differentiates tick paralysis from many other causes of acute flaccid paralysis, which often require immunomodulatory or intensive supportive therapies and have more protracted recoveries.

### Key Identifiers and Ontology Mapping

With respect to biomedical identifiers, tick paralysis has limited representation in classical genetic disease databases owing to its non-genetic etiology. The MONDO ontology assigns the identifier MONDO:0005981 to “tick paralysis” as an injury-type disorder, situating it under tick toxicoses and bite-related poisonings rather than hereditary neuromuscular diseases. Although OMIM, Orphanet, and most Mendelian-focused repositories do not maintain primary entries for tick paralysis, its conceptual definition is captured in MeSH (Tick Paralysis; unique ID D013985, tree number C25.723.127.789.500.707), which locates it under “Tick Bites” and “Tick Toxicoses” within the hierarchy of bites and stings and chemically induced disorders.[17] In ICD-10 and ICD-11 coding practice, tick paralysis is usually coded as “T63.4 Toxic effect of venom of other arthropods” or more generically under toxic effects of contact with venomous animals, combined with codes indicating tick bite as an external cause, rather than as a specific named disease entity.

In human phenotype ontologies, ascending flaccid paralysis and related features can be mapped to terms such as “Muscle weakness” (HP:0001324), “Flaccid paralysis” (HP:0003471), “Ataxia” (HP:0001251), “Ophthalmoplegia” (HP:0000602), “Bulbar palsy” (HP:0001285), and “Respiratory failure” (HP:0002878).[18][20] Tick paralysis itself, as a disorder concept, is represented in MeSH and MONDO and could be further linked to SNOMED CT concepts for “paralysis due to tick bite” and “toxic effect of arthropod venom.” The MeSH scope note and tree mapping emphasize that tick paralysis is an injury due to a neurotoxic salivary secretion, not a communicable disease or genetic syndrome.[17]

### Synonyms and Alternative Names

Several synonyms and alternative names are used in the literature. In veterinary and comparative neurology, the term **tick toxicosis** is widely employed, reflecting the toxin-mediated pathogenesis and emphasizing that the primary pathology is systemic intoxication rather than focal nerve injury.[5][15][16] The MSD Veterinary Manual notes that “tick paralysis (also known as tick toxicosis) is an acute, progressive, symmetrical, ascending motor paralysis due to salivary neurotoxins produced by certain species of ticks,” thus explicitly equating the two terms.[5] Other synonyms include “paralysis tick poisoning” in Australian contexts, particularly where *Ixodes holocyclus* is endemic and commonly called the “paralysis tick,” and “neurotoxic tick bite” or “tick-induced paralysis” in emergency medicine and toxicology case reports.[6][9][16][19] Pediatric neurology literature sometimes refers to “pediatric tick paralysis” to highlight its age distribution, whereas some meta-analytic and epidemiologic papers classify it under “tick-borne neurotoxidrome.”[6][7][19]

From an ontology perspective, these synonyms can be cross-mapped so that tick paralysis (MONDO:0005981; MeSH D013985) is recognized as equivalent to tick toxicosis, paralysis tick poisoning, and tick-induced neurotoxic paralysis. Such mapping is important for comprehensive literature retrieval and for distinguishing this syndrome from tick-borne infections such as ehrlichiosis, babesiosis, or tick-borne encephalitis, which have overlapping exposure contexts but fundamentally different etiologies and clinical courses.[1][5][9][11][16]

### Data Sources and Evidence Type

The information about tick paralysis in this report is derived almost entirely from aggregated disease-level resources rather than individual electronic health record databases. Foundational clinical descriptions come from case series and reviews in neurology and emergency medicine, such as the clinical and neurophysiological analysis of six Australian children with generalized tick paralysis by Grattan-Smith and colleagues (Brain, 1997, PMID 9397015).[18][20] This study concluded that “the typical presentation is a prodrome followed by the development of an unsteady gait, and then ascending, symmetrical, flaccid paralysis,” with characteristic electrophysiological findings.[18][20] A meta-analysis of 50 well-documented U.S. cases over 60 years by Diaz (J Med Toxicol, 2010, PMID 20237909) provided epidemiologic and misdiagnosis data, describing tick paralysis as “a predictable, preventable, and often misdiagnosed poisoning.”[7][19] Additional key reviews include Edlow’s 2010 article on tick paralysis in Current Treatment Options in Neurology (PMID 20842579) and Vedanarayanan’s 2004 review in Seminars in Neurology (PMID 15257515), both synthesizing clinical features, pathophysiology, and differential diagnosis.[11][13]

Public health guidance from the British Columbia Centre for Disease Control (BCCDC), Purdue University Extension, MedlinePlus, Merck Manual, WebMD, and StatPearls adds contemporary practice-oriented descriptions and reinforces the rarity yet clinical urgency of the condition.[1][2][3][4][10][14] Mechanistic insights, particularly about holocyclotoxin from *Ixodes holocyclus*, derive from experimental work summarized in the comprehensive review “Tick paralysis in Australia caused by Ixodes holocyclus Neumann,” which emphasizes presynaptic inhibition of acetylcholine release at the neuromuscular junction.[9][16] Veterinary manuals and reviews extend understanding to animals and clarify species differences.[5][15][16]

Thus, the evidence base is a mixture of human clinical case series, veterinary case reports, toxicology meta-analyses, and mechanistic in vivo and in vitro experiments in animals, all aggregated at the disease level rather than abstracted from large individual-level registries or EHR datasets.

## 2. Etiology

### Primary Causes and Mechanistic Category

The primary cause of tick paralysis is prolonged attachment and feeding of a salivary neurotoxin–secreting tick on a susceptible vertebrate host, leading to systemic intoxication and neuromuscular blockade.[5][9][11][13][16][17] The pathologic agent is a protein or peptide toxin produced in the salivary glands of certain adult female ticks, particularly during the rapid engorgement phase; during repeated salivary secretion and blood ingestion, this neurotoxin is injected into the host and disseminates to neuromuscular junctions.[5][8][9][16] The MSD Veterinary Manual emphasizes that “tick paralysis (tick toxicosis) is an acute, progressive, symmetrical, ascending motor paralysis due to salivary neurotoxins produced by certain species of ticks,” highlighting that the cause is a toxin rather than a pathogen.[5] Similarly, the Purdue Public Health and Medical Entomology resource clarifies that “the cause is now known to be an unidentified protein toxin (or toxins) in tick saliva, not a disease agent,” reinforcing its classification as a poisoning.[1]

In humans in North America, the most frequently implicated species are *Dermacentor andersoni* (Rocky Mountain wood tick) and *Dermacentor variabilis* (American dog tick), while *Ixodes holocyclus* is the principal paralysis tick in eastern Australia and a key cause of severe paralysis in dogs, cats, and children.[5][6][9][16][18][19][20] The BCCDC notes that “the species causing the most cases of human tick paralysis in Canada are *Dermacentor andersoni* (the Rocky Mountain wood tick) and *Dermacentor variabilis* (the American dog tick),” with *D. andersoni* common throughout interior British Columbia.[3] MedlinePlus similarly lists *Dermacentor andersoni* as the species most often associated with tick paralysis in the Pacific Northwest and Rocky Mountain states, with *Dermacentor variabilis* and *Ixodes pacificus* also capable of causing paralysis.[10]

Etiologically, tick paralysis occupies an unusual niche among neurotoxicoses: it is neither an exogenous chemical exposure nor a classic envenomation in the sense of acute injection of a bolus of venom; rather, it is due to “pulsed toxin flow associated with repeated tick feeding over a set period of time,” with systemic toxicosis arising particularly during periods of rapid engorgement.[5] The toxin is delivered through normal tick feeding behavior, and the risk of paralysis increases with the duration of attachment and degree of engorgement, explaining the typical 4–7 day latency between attachment and onset of neurologic symptoms.[3][6][9][13][16][18][19] No genetic or infectious etiologies have been convincingly demonstrated in human hosts; blood and CSF analyses are typically normal, and removal of the tick leads to rapid resolution without antimicrobial therapy.[6][11][18][19][20]

From a disease ontology standpoint, tick paralysis is best categorized as a **toxin-mediated injury** secondary to an arthropod bite, aligning with MONDO’s “Injury” category, MeSH’s “Tick Toxicoses,” and ICD’s toxic effects of arthropod venom codes.[17] It is therefore distinct from hereditary neuromuscular disorders and from immune-mediated neuropathies such as Guillain–Barré syndrome, despite striking similarities in clinical presentation.

### Genetic Risk Factors in the Host

For the human host, no causal variants, susceptibility loci, or modifier genes have been identified that confer a significantly increased risk of developing tick paralysis after exposure. The available case series, meta-analyses, and reviews show no evidence of familial clustering or hereditary predisposition; instead, risk appears to be driven primarily by environmental exposure and possibly age- and sex-related differences in behavior and physiology.[7][11][13][18][19] Vedanarayanan and colleagues explicitly describe tick paralysis as “a relatively uncommon neuromuscular disease with a higher prevalence among young girls, although older men who get exposed to ticks may also be affected,” without suggesting genetic causation.[13] Diaz’s meta-analysis of 50 U.S. cases over 60 years found seasonal and regional predictability but did not uncover genetic risk factors; rather, it emphasized demographic and environmental patterns.[7][19]

Consequently, standard genetic databases such as ClinVar, ClinGen, GWAS Catalog, and OMIM do not list tick paralysis–related variants, and there are no validated host genetic markers of susceptibility. The penetrance concept is therefore not applicable in the classical sense, and tick paralysis should not be considered a Mendelian trait in humans.

Interestingly, genetic variation exists in the ticks themselves regarding their ability to cause paralysis, implying that tick genes, rather than host genes, modulate risk. An experimental study by Wozniak et al. documented that the ability of *Dermacentor andersoni* to cause paralysis is heritable: crosses between virulent and avirulent strains showed that paralysis occurred with the virulent parental strain but not the avirulent strain, and virulence segregated within progeny.[8] The authors concluded that “these experiments further suggested that tick paralysis is a heritable trait, however, definitive proof is lacking,” indicating that tick salivary toxin production or composition is genetically determined within the vector.[8] From a comparative genomics perspective, those tick genes could be conceptualized as “causal genes” for the disease entity in MONDO, but their sequences and functional annotations are not yet integrated into human disease genetics resources.

### Environmental and Behavioral Risk Factors

Environmental, behavioral, and occupational factors play a central role in determining risk of tick paralysis. The primary risk factor is exposure to habitats where paralysis-causing ticks are prevalent, combined with conditions that allow prolonged, unnoticed tick attachment. Diaz’s meta-analysis found that tick paralysis “occurred seasonally and sporadically in individuals and in clusters of children and adults of both sexes in urban and rural locations,” with cases concentrated in endemic regions of the Pacific Northwest and Rocky Mountain areas for *D. andersoni* and in the southeastern U.S. for *D. variabilis*.[7][19] The BCCDC reports only 0–2 human consultations for tick paralysis per year in British Columbia, highlighting its rarity but also its tight geographical coupling to *D. andersoni* habitats.[3] In Australia, holocyclotoxin-mediated paralysis is a significant veterinary and human health issue along the eastern seaboard, particularly in coastal and rainforest fringes where *Ixodes holocyclus* is abundant.[9][16]

Age is a notable risk factor. Pediatric case series suggest that young children, especially girls, are disproportionately affected, likely because ticks preferentially attach to the scalp in children, are hidden by hair, and may remain undetected for days.[7][13][18][19] Grattan-Smith et al. described six Australian children with generalized tick paralysis, all of whom had mature female *Ixodes holocyclus* ticks attached to the scalp, reinforcing the interplay between age-related scalp exposure and paralysis risk.[18][20] An 83-year-old man described in a CMAJ case report developed severe ataxia, diplopia, four-limb weakness, and dysarthria after working at his rural cabin, illustrating that older adults with high environmental exposures are also at risk.[6] Behavioral factors such as hiking, camping, forestry work, and pet ownership (particularly dogs that roam in tick-infested areas) increase the likelihood of contact with paralysis ticks and of ticks being transported into domestic environments.[2][3][10]

Sex differences have been noted but are likely behavioral rather than biologically determined. Several series report a predominance of female patients in pediatric and adult cohorts, but this has been attributed to hair length, clothing, and exposure patterns rather than genetic or hormonal susceptibility.[7][13][19] Nonetheless, from an epidemiologic perspective, female sex appears as a weak risk marker, which may be useful for clinical suspicion in endemic settings.

The single most critical environmental risk factor is the duration of tick attachment and degree of engorgement. Multiple sources indicate that symptoms typically begin only after the tick has fed for 4–7 days, suggesting a threshold exposure to salivary toxin.[3][6][9][13][16][18] The BCCDC notes that “symptoms begin after a female tick attaches to the skin and has fed for 5–7 days,” while MedlinePlus describes onset of leg weakness “usually 2 to 7 days after a tick bite,” underscoring this latency.[3][10] Purdue Extension similarly emphasizes that paralysis is associated with feeding by an engorging female tick often attached along the spinal cord or scalp.[1] Therefore, individuals who fail to perform regular tick checks, who sleep outdoors without protection, or who have reduced ability to sense or remove ticks (e.g., due to cognitive or mobility impairments) are at higher risk.

### Protective Factors and Prevention-Oriented Etiology

Protective factors derive primarily from measures that prevent tick attachment or that ensure early tick removal before sufficient toxin is delivered. Use of tick repellents containing DEET or permethrin on clothing, wearing long sleeves and pants, tucking pants into socks, avoiding dense vegetation and leaf litter, and performing daily full-body tick checks substantially reduce risk of tick bites and prolonged attachment, and thus reduce risk of tick paralysis.[2][3][10] Pet-level tick control—such as regular acaricide treatment, tick collars, and limiting dogs’ roaming in high-risk habitats—lowers the risk of ticks being carried into homes and onto humans.[2][3][10] The BCCDC and Purdue resources emphasize meticulous examination of the scalp, neck, and intertriginous areas when tick paralysis is suspected; this same approach, applied as a preventive habit after outdoor exposure, functions as a protective factor by enabling early removal.[1][3]

No specific dietary, lifestyle, or pharmacologic factors have been identified that alter susceptibility to the neurotoxin itself. There is no evidence that host genetic polymorphisms in neuromuscular junction proteins (e.g., presynaptic calcium channels or acetylcholine release machinery) confer resistance or vulnerability. However, general health status and respiratory reserve may modulate clinical severity and outcome: patients with pre-existing neuromuscular disease, lung disease, or frailty may have less capacity to withstand respiratory muscle weakness and may progress more quickly to respiratory failure.[5][9][13][19] Conversely, robust healthy hosts, particularly older children and adults, may tolerate some degree of weakness and recover fully with minimal supportive care once the tick is removed.

### Gene–Environment Interactions

In the strict human genetic sense, gene–environment interactions have not been characterized for tick paralysis. This reflects both the rarity of the condition and the fact that its incidence is overwhelmingly determined by tick exposure rather than intrinsic host genetics. Nonetheless, at a broader eco-genetic level, interesting interactions do occur between tick genetics and environmental conditions, influencing toxin production and disease risk.

The heritability of paralysis-inducing capacity in *Dermacentor andersoni* suggests that specific tick genotypes encode salivary gland toxins capable of causing paralysis, while others do not.[8] Environmental conditions, such as temperature and season, may modulate expression or activity of these toxin genes; experimental work in *Ixodes holocyclus* has indicated temperature-dependent inhibition of evoked acetylcholine release by holocyclotoxin, implying that toxin potency is influenced by environmental factors experienced by the tick.[16] One early study cited by Stone and colleagues reported “temperature-dependent inhibition of evoked acetylcholine release in tick paralysis,” suggesting that toxin action is modulated by ambient or physiological temperature.[16] Thus, at the vector level, gene–environment interactions shape the risk that any given tick bite will result in paralysis, although these interactions are not yet mapped in molecular detail.

Within hosts, immunologic factors could theoretically modify susceptibility to tick salivary toxins. Repeated tick exposures might induce partial immunity, reducing clinical severity over time; conversely, allergic sensitization might exacerbate local and systemic responses. Veterinary observations in dogs have suggested variability in clinical severity that could reflect such host factors, but definitive mechanistic studies are lacking.[5][15][16] Therefore, while gene–environment interactions likely exist in both ticks and hosts, current knowledge does not permit precise enumeration or integration into a formal risk prediction model.

## 3. Phenotypes

### Core Clinical Phenotypes and Symptom Types

Tick paralysis manifests a characteristic constellation of neuromuscular phenotypes, dominated by symmetric ascending motor weakness, gait unsteadiness, areflexia, and often cranial nerve and bulbar involvement, with relatively preserved sensation and cognition.[1][3][4][6][11][13][18][19][20] Grattan-Smith et al.’s seminal Brain 1997 paper on six Australian children with generalized tick paralysis described the typical presentation as “a prodrome followed by the development of an unsteady gait, and then ascending, symmetrical, flaccid paralysis,” emphasizing both the sequential evolution and the symmetry of motor involvement.[18][20] The children exhibited early cranial nerve involvement, particularly internal and external ophthalmoplegia, along with facial weakness and dysarthria, suggesting preferential vulnerability of certain cranial motor nuclei or their neuromuscular junctions.[18][20]

Common symptoms include muscle weakness, beginning in the legs and progressing proximally; difficulty walking or ataxia; fatigue and lethargy; irritability; paresthesias or numbness; and in some cases restlessness and muscle pains.[1][2][3][6][11][13][18][19] The BCCDC lists numbness and tingling in the face and limbs, fatigue, weakness, irritability, restlessness or muscle pains as early features, followed over hours or days by unsteady balance and then complete or partial paralysis starting in the legs and moving upwards.[3] WebMD similarly notes that tick paralysis “usually starts with numbness or tingling in your legs,” with accompanying muscle pain, tiredness, and irritability.[2] MedlinePlus emphasizes that tick paralysis “starts with weakness in the legs, usually 2 to 7 days after a tick bite,” progressing to more generalized paralysis that may impair breathing.[10]

Cranial nerve dysfunction manifests as diplopia, double or blurred vision, photophobia, facial weakness, dysarthria, dysphagia, difficulty swallowing and speaking, and sometimes impaired gag reflex.[3][6][9][13][18][20] The CMAJ case report of an 83-year-old man highlighted diplopia, marked dysarthria, dysmetria, and reduced vibration sense and proprioception, though sensation is usually relatively preserved.[6] In Australian holocyclotoxin-mediated paralysis, early cranial nerve involvement is particularly prominent; Grattan-Smith et al. reported “both internal and external ophthalmoplegia” as a hallmark feature, with dilated pupils and impaired eye movements.[18][20] These cranial features can be mapped to HPO terms such as “Ophthalmoplegia” (HP:0000602), “Diplopia” (HP:0000651), “Facial weakness” (HP:0002353), “Dysarthria” (HP:0001260), and “Dysphagia” (HP:0002360).

Respiratory involvement represents the most serious phenotype, with weakness of diaphragmatic and intercostal muscles leading to hypoventilation, dyspnea, and potential respiratory failure requiring mechanical ventilation.[1][3][4][5][9][10][11][13][19] Emergency medicine resources emphasize that while tick paralysis is rarely fatal, “it’s an emergency if it weakens your diaphragm and makes it hard to breathe,” and the Merck Manual warns that “bulbar or respiratory paralysis may develop” and that tick paralysis “can be fatal” but is reversible if ticks are promptly removed.[2][4] Respiratory failure corresponds to the HPO term HP:0002878, and diaphragmatic weakness to HP:0002243 (“Diaphragmatic paralysis”), although specific coding may vary in individual ontologies.

### Age of Onset, Severity, and Progression Patterns

Tick paralysis is not congenital and does not have a fixed age of onset; rather, onset is determined entirely by timing of tick exposure and duration of attachment. In human series, most cases occur in children and younger adults, but elderly individuals with high exposure are also represented.[6][7][13][18][19] The meta-analysis by Diaz reported that tick paralysis “primarily afflicts young girls in endemic regions,” though adults of both sexes can be affected.[7][19] Vedanarayanan’s Seminars in Neurology review similarly states that it “has a higher prevalence among young girls, although older men who get exposed to ticks may also be affected.”[13] In Australia, holocyclotoxin-mediated paralysis often presents in children and in dogs and cats of various ages.[9][16][18][20]

Onset pattern is typically subacute but can appear abrupt from the patient’s perspective. After 4–7 days of silent tick feeding, a prodrome of malaise, fatigue, irritability, and paresthesias emerges, followed by gait unsteadiness and then rapid progression to ascending weakness over hours to a couple of days.[3][6][9][13][18][19][20] Diaz’s meta-analysis found that paralysis ensues after a mean of 1.4 days (range 1–10 days) following onset of neurologic symptoms, reflecting a rapid progression once toxin burden reaches a critical threshold.[6][19] Grattan-Smith et al. observed progression from prodrome to generalized flaccid paralysis within a relatively short time frame in their pediatric series.[18][20] The BCCDC notes that progression can occur over several hours or days, culminating in complete or partial paralysis, and warns that respiratory difficulties and death can rarely occur if the tick is not removed rapidly.[3]

Symptom severity is variable but can be profound. Mild cases may exhibit only gait unsteadiness and proximal leg weakness, resolving quickly after tick removal. Moderate cases may manifest four-limb weakness, cranial nerve deficits, and mild respiratory compromise. Severe cases, particularly in Australian holocyclotoxin exposures and heavily infested animals, can present with generalized flaccid paralysis, dilated pupils, marked bulbar dysfunction, and life-threatening hypoventilation.[5][9][15][16][18][20] The MSD Veterinary Manual notes that dyspnea, crackles, wheezes, and high neuromuscular junction scores are poor prognostic signs in animals, indicating more severe toxicosis and respiratory distress.[5] Human mortality over 60 years in the U.S. literature was 6.0%, which, while low, underscores that fatal outcomes occur when diagnosis and tick removal are delayed.[7][19]

Progression is typically monotonic until the tick is removed; the disease does not show relapsing-remitting patterns or spontaneous remission while the tick remains attached. Once the tick is removed, however, the course reverses dramatically, with rapid improvement over minutes to hours and complete recovery usually within one to several days.[1][3][4][6][18][19][20] Diaz’s meta-analysis reported that “full recovery usually occurs after 1.5 (range 1–2.5) days” following tick removal.[6][19] Still, some sources note that if paralysis has progressed far, complete recovery may take up to six months, though this likely reflects comorbidities or residual deconditioning rather than ongoing toxin effects.[1] In animals, recovery may be slower, particularly when respiratory complications or secondary infections have developed.[5][15][16]

### Frequency and Phenotype Penetrance among Affected Individuals

Within documented cases, certain phenotypes appear nearly universal. Ascending symmetrical motor weakness and gait unsteadiness are present in virtually all human cases described in neurology series and meta-analyses.[6][7][11][13][18][19][20] Areflexia or markedly diminished deep tendon reflexes is also a consistent finding, paralleling the clinical picture of Guillain–Barré syndrome.[11][13][18][20] Paresthesias, fatigue, and irritability are common prodromal symptoms, though not present in every case.[2][3][6][13][18][19] Cranial nerve involvement, especially ophthalmoplegia, facial weakness, and dysarthria, appears more frequent and more prominent in Australian *Ixodes holocyclus*–mediated paralysis than in North American *Dermacentor* paralysis, suggesting toxin-specific phenotypic differences.[9][16][18][20] Grattan-Smith et al. considered early cranial nerve involvement, particularly internal and external ophthalmoplegia, as a hallmark of holocyclotoxin paralysis in children.[18][20]

Respiratory compromise occurs in a subset—perhaps 10–30% of severe holocyclotoxin cases and a smaller fraction of North American Dermacentor paralysis—but exact frequencies are not well quantified due to sparse data.[5][9][13][19] Diaz’s meta-analysis noted that respiratory failure and death could occur but did not provide a detailed breakdown of respiratory involvement frequency; the overall case fatality rate was 6.0%.[7][19] In animals, respiratory signs such as dyspnea, crackles, and wheezes are recognized as poor prognostic signs, but again, precise frequencies depend on species, toxin, and timing of intervention.[5][15][16]

Quality-of-life impact is intensely negative during the acute phase, given profound motor disability, risk of respiratory failure, and psychological distress, but this impact is transient because of the reversible nature of the syndrome once correctly diagnosed and managed. During paralysis, patients may be unable to walk, stand, or perform basic activities of daily living, and they may experience anxiety or fear related to breathing difficulties and possible misdiagnosis.[6][11][13][18][19] However, rapid recovery with minimal residual deficits means that long-term disability outcomes are rare in human tick paralysis, in contrast to many other neuromuscular diseases. If mapped to quality-of-life instruments such as the EQ-5D or SF-36, tick paralysis would show extreme impairments in mobility, self-care, and usual activities during the acute episode, with rapid return to baseline scores once the tick is removed and the toxin cleared.

### Suggested HPO Terms for Major Phenotypes

The primary phenotypes of tick paralysis can be associated with Human Phenotype Ontology terms to support structured knowledge representation. Ascending flaccid paralysis corresponds to “Flaccid paralysis” (HP:0003471) and “Muscle weakness” (HP:0001324), with the ascending pattern contributing to a more specific descriptor such as “Progressive motor impairment” (HP:0002340).[18][20] Ataxia and unsteady gait can be mapped to “Ataxia” (HP:0001251) and “Gait instability” (HP:0002141).[18][20] Numbness and tingling are captured by “Paresthesia” (HP:0003401).[3] Cranial nerve phenotypes include “Ophthalmoplegia” (HP:0000602), “Diplopia” (HP:0000651), “Facial weakness” (HP:0002353), “Dysarthria” (HP:0001260), “Dysphagia” (HP:0002360), and “Bulbar palsy” (HP:0001285).[3][6][9][18][20] Respiratory involvement can be coded as “Respiratory failure” (HP:0002878) and “Dyspnea” (HP:0002094).[1][3][4][5][10]

Prodromal fatigue and lethargy can be assigned to “Fatigue” (HP:0012378) and “Lethargy” (HP:0001254).[3][13] Areflexia aligns with “Absent reflexes” (HP:0001284).[6][18][20] Irritability and restlessness could be noted as “Irritability” (HP:0000737), though psychiatric mapping is less central in this toxidrome. Importantly, sensory modalities are largely preserved, so absence of sensory loss is a phenotypic clue to differentiate tick paralysis from some neuropathies; this can be recorded as the absence of “Sensory neuropathy” (HP:0003474).

By coupling these HPO terms to MONDO:0005981, the disease knowledge base can capture the core clinical signature of tick paralysis in a machine-readable format.

## 4. Genetic and Molecular Information

### Absence of Human Causal Genes and Variants

Tick paralysis is an archetypal non-genetic disorder in the human host, and no human causal genes or pathogenic variants have been associated with its occurrence. As noted in multiple reviews, the disease results from inoculation of a toxin from tick salivary glands during a blood meal, not from mutations in human neuromuscular genes.[5][9][11][13][16][17] Vedanarayanan et al. clearly state that “tick paralysis results from inoculation of a toxin from tick salivary glands during a blood meal,” emphasizing its exogenous nature.[13] The MeSH descriptor for tick paralysis similarly frames it as “paralysis caused by a neurotropic toxin secreted by the salivary glands of ticks,” underscoring that the physiologic insult originates in the vector.[17]

Consequently, comprehensive searches of OMIM, ClinVar, HGMD, Ensembl, and NCBI Gene do not yield entries linking specific human gene mutations to tick paralysis. There is no recognized pattern of autosomal dominant, autosomal recessive, X-linked, mitochondrial, or multifactorial inheritance for this condition, and family history is not a known risk factor.[11][13][19] Population allele frequency databases such as gnomAD and 1000 Genomes have no relevance to tick paralysis risk, and somatic mutations or structural genomic variants have not been implicated.

### Tick Genetic Determinants of Toxin Production

At the vector level, however, genetic determinants exist. The capacity of certain tick strains to cause paralysis is heritable, indicating that tick genes encode and regulate salivary neurotoxins that are responsible for disease. Wozniak and colleagues examined the heritability of the ability to cause paralysis in *Dermacentor andersoni* by crossing virulent and avirulent strains and assessing virulence in hamsters.[8] Their abstract notes that “paralysis was caused by the virulent parental strain but not by the avirulent parental strain,” and that experiments suggested heritability of the trait.[8] Although the exact genes were not identified, this work implies that specific loci in the tick genome regulate expression or structure of salivary toxins, thus functionally serving as “causal genes” for tick paralysis from an eco-parasitologic standpoint.

In *Ixodes holocyclus*, the toxin holocyclotoxin is produced in the salivary glands of feeding female ticks and transferred to the host via saliva; its production is presumably controlled by tick gene networks analogous to those governing other arthropod toxins, but individual genes have not yet been fully characterized.[9][16] Stone’s review emphasizes that the toxin results in a presynaptic decrease in acetylcholine release at the neuromuscular junction, indicating specific molecular targeting, but does not identify the tick genes encoding holocyclotoxin.[9][16] These tick toxin genes are not, in the strict sense, part of the human genome, but they could be recorded in comparative disease databases with NCBI Gene IDs once identified, enabling integration of tick genomics into the tick paralysis knowledge graph.

### Modifier Genes and Epigenetic Information

Given the absence of host genetic causation, no modifier genes have been described that alter disease severity or expression in humans. There is no evidence that polymorphisms in presynaptic calcium channels (e.g., P/Q-type channels), SNARE complex proteins, or acetylcholine transporters modulate susceptibility to tick salivary neurotoxins. Epigenetic modifications such as DNA methylation or histone changes have not been studied in the context of tick paralysis, and given the acute, transient nature of the exposure, epigenetic regulation is unlikely to play a major causal role in human hosts.

In ticks, epigenetic regulation might influence salivary gland gene expression, including toxin production, but direct evidence is absent from the current literature. As tick genomics and epigenomics advance, one might eventually catalogue tick salivary gland expression profiles and connect them to paralysis phenotypes, but this remains prospective.

### Chromosomal Abnormalities and Structural Genomics

No chromosomal abnormalities, aneuploidies, translocations, or inversions in the human host have been linked to tick paralysis. Patients described in neurology and toxicology case series do not share structural genomic features beyond general health status. Chromosomal microarray, karyotyping, and FISH are irrelevant in clinical workup of tick paralysis, which is diagnosed by clinical and exposure history, physical examination with tick detection, and sometimes neurophysiologic testing.[4][6][11][13][18][19][20]

In the tick, chromosomal location of toxin genes remains uncharacterized. Future mapping of tick genomes might identify structural features or gene clusters associated with toxin production, but current disease-level databases do not include these.

In summary, for human disease representation, tick paralysis should be annotated explicitly as **non-genetic**, with no host causal or modifier genes, while recognizing that tick genetic determinants of salivary toxin production exist and could be captured in vector-focused databases.

## 5. Environmental Information

### Environmental Exposures and Ecologic Context

Tick paralysis is deeply rooted in environmental and ecological contexts, as its occurrence depends on specific tick species, their geographic distributions, seasonal activity, and local habitat characteristics. *Dermacentor andersoni*, the Rocky Mountain wood tick, is found in the Rocky Mountain and Pacific Northwest regions of North America, favoring grasslands, shrublands, and open forests at elevations where deer, rodents, and other hosts are common.[3][5][10][19] *Dermacentor variabilis*, the American dog tick, is widespread in the eastern and southeastern United States, inhabiting meadows, roadsides, and edges of forests.[5][10][19] The BCCDC specifically notes that *D. andersoni* is found throughout British Columbia and is most common in interior BC, aligning tick paralysis risk with those regions.[3] In Australia, *Ixodes holocyclus* occupies coastal and inland rainforest fringes along the eastern seaboard, especially in New South Wales and Queensland, where humidity and vegetation support its life cycle.[9][16][18]

Seasonal factors are crucial. Diaz’s meta-analysis showed that tick paralysis cases clustered in late spring and early summer, corresponding to peak activity of adult female ticks seeking hosts.[7][19] Public health advisories often stress that during tick season, individuals presenting with acute flaccid paralysis should be carefully examined for ticks.[3][6] Climatic changes that alter tick distributions, such as warming temperatures and changes in rainfall patterns, may influence future tick paralysis risk regions, but detailed climate–incidence models are not yet available.

Environmental risk factors also include microhabitat features such as leaf litter, tall grasses, and animal burrows, which provide questing sites for ticks. Human behaviors that increase contact with these microhabitats—such as hiking off-trail, camping on forest floors, or lying in grass—raise exposure risk. Dogs and other pets that roam through such environments and return to human dwellings serve as bridging hosts, increasing the chance that ticks will attach to humans in domestic settings.[2][3][10][15]

### Lifestyle and Occupational Factors

Lifestyle factors that influence risk include outdoor recreational activities, occupational exposures, and pet ownership. Individuals who hike, camp, hunt, or engage in nature tourism in endemic areas are at higher risk of tick bites, and by extension tick paralysis, especially if they do not employ protective clothing or repellents.[2][3][10] Forestry workers, farmers, ranchers, park rangers, and cabin owners, such as the 83-year-old Canadian man who developed severe paralysis after working at his cabin in the Thompson–Nicola region of British Columbia, face occupational exposures.[6] Children who play outdoors in tick-infested environments, particularly in rural or peri-urban settings, may be bitten on the scalp or behind the ears and be unaware of the tick’s presence.[3][13][18]

Pet ownership, especially of dogs, is a significant lifestyle risk factor. Dogs can host paralysis ticks such as *Ixodes holocyclus* or *Dermacentor* species, and ticks can transfer from dogs to humans in close-contact settings.[2][3][10][15][16] WebMD notes that “dogs can bring ticks into your home, which then attach to you,” emphasizing this indirect exposure pathway.[2] Lack of regular tick prevention for pets—such as acaricidal collars, spot-on treatments, or environmental insecticide use—thus increases risk for both animals and humans.

Alcohol consumption, smoking, diet, and exercise do not appear to modify tick paralysis risk directly, although high levels of intoxication or sedation might reduce awareness of tick bites and delay removal. In general, lifestyle factors that increase outdoor exposure without appropriate protective measures serve as risk enhancers.

### Infectious Agents and Co-exposures

Tick paralysis itself is noninfectious, but ticks capable of causing paralysis can also transmit infectious agents, including *Rickettsia rickettsii* (Rocky Mountain spotted fever), *Borrelia burgdorferi* (Lyme disease, transmitted by *Ixodes scapularis* and other species), and various Ehrlichia and Anaplasma species.[1][5][10][11][16] The Purdue Extension webpage discussing tick paralysis also references human monocytic ehrlichiosis as another tick-borne disease, highlighting that tick paralysis can occur alongside, or be confused with, infectious tick-borne illnesses.[1] However, clinical features of tick paralysis differ from these infections: fever, rash, systemic inflammatory signs, and abnormal serologies are absent, and neurological deficits reverse rapidly with tick removal even in the absence of antimicrobial therapy.[6][11][13][18][19]

The possibility of co-exposure to tick-borne pathogens exists, especially in regions where paralysis ticks share habitats with infected ticks carrying other pathogens. Clinicians must therefore remain aware that a patient with tick paralysis might also have concomitant or subsequent tick-borne infections, requiring separate diagnostic and therapeutic considerations. Nonetheless, infectious agents are not causally involved in tick paralysis itself, and they should not be recorded as etiologic agents for MONDO:0005981.

## 6. Mechanism and Pathophysiology

### Ordered Causal Chain from Exposure to Clinical Manifestation

(1) Prolonged attachment and feeding of a toxin-secreting adult female ixodid tick on a human or animal host leads to repeated secretion of saliva containing neurotoxic proteins into the host’s skin and circulation.[1][3][5][8][9][16][17]

(2) Accumulation of tick salivary neurotoxins in the host’s systemic circulation leads to distribution of toxin molecules to peripheral neuromuscular junctions, particularly those of skeletal muscles in the limbs and cranial musculature.[5][9][16][18][20]

(3) Binding of tick neurotoxins to presynaptic terminals at the neuromuscular junction leads to inhibition of evoked acetylcholine release, via interference with voltage-gated calcium channels or neurotransmitter release machinery, resulting in impaired synaptic transmission.[9][16][18][20]

(4) Reduced acetylcholine release at neuromuscular junctions leads to decreased end-plate potentials and failure to trigger muscle fiber depolarization, resulting in flaccid paralysis of affected muscles, beginning in distal limb muscles and progressing proximally.[5][9][16][18][20]

(5) As toxin burden increases or persists, neuromuscular blockade spreads to cranial nerves and respiratory muscles, leading to ophthalmoplegia, facial weakness, bulbar palsy, and potentially diaphragmatic and intercostal muscle paralysis, which leads to hypoventilation and respiratory failure in severe cases.[3][4][5][6][9][10][13][18][19][20]

(6) Removal of the attached tick leads to cessation of further toxin delivery, allowing gradual clearance of neurotoxin from the circulation and neuromuscular junctions, which leads to restoration of acetylcholine release, recovery of neuromuscular transmission, and rapid clinical improvement.[1][3][4][6][9][16][18][19][20]

(7) In survivors, absence of structural nerve damage leads to complete functional recovery without long-term neuromuscular deficits, although prolonged severe cases may result in temporary deconditioning or secondary complications that lead to a longer convalescent period.[1][5][9][15][18][19]

### Molecular Pathways and Synaptic Mechanisms

The primary molecular pathway implicated in tick paralysis is presynaptic inhibition of acetylcholine release at the neuromuscular junction. Holocyclotoxin from *Ixodes holocyclus* has been studied most extensively; experimental work indicates that this toxin results in “a presynaptic decrease in acetylcholine release at the neuromuscular junction,” effectively blocking neuromuscular transmission.[9][16] Cooper and Spence demonstrated temperature-dependent inhibition of evoked acetylcholine release in tick paralysis, suggesting that holocyclotoxin acts on presynaptic mechanisms sensitive to temperature.[16] This mechanism broadly parallels that of certain presynaptic neurotoxins in snake venoms and botulinum neurotoxins, though the precise molecular target—whether a specific voltage-gated calcium channel, SNARE protein, or other release regulator—remains incompletely defined.

In molecular terms, holocyclotoxin’s action can be mapped to Gene Ontology processes such as “regulation of neurotransmitter secretion” (GO:0007269), “negative regulation of synaptic transmission, cholinergic” (GO:0032226), and “neuromuscular junction development and function” (GO:0007528). By inhibiting acetylcholine release, the toxin disrupts “cholinergic synaptic transmission” (GO:0007271) in motor endplates, causing failure of muscle activation.

For *Dermacentor* toxins, mechanistic data are less detailed but suggest similar neuromuscular interference. The MSD Veterinary Manual notes that tick salivary toxins have “a direct effect on cellular potassium channels and thus on intracellular calcium levels,” implying alteration of presynaptic electrophysiology and calcium signaling.[5] This could be conceptualized under GO terms such as “regulation of membrane potential” (GO:0042391), “regulation of calcium ion concentration” (GO:0051924), and “voltage-gated ion channel activity” (GO:0005249). Inhibition of voltage-gated calcium channels would reduce calcium-dependent synaptic vesicle fusion and acetylcholine release, mirroring holocyclotoxin’s effect.

No evidence suggests that tick neurotoxins directly target postsynaptic acetylcholine receptors or muscle fiber excitability; electrophysiologic studies show normal motor conduction velocities and normal sensory nerves, with reduced compound muscle action potential (CMAP) amplitudes.[18][20] Grattan-Smith et al. found low-amplitude CMAPs with normal motor conduction velocities, normal sensory studies, and normal response to repetitive stimulation, indicating a presynaptic or neuromuscular junction disorder rather than demyelinating neuropathy or primary muscle disease.[18][20]

### Cellular Processes and Tissue-Level Pathophysiology

At the cellular level, tick paralysis involves functional rather than structural disruption of peripheral motor neurons and neuromuscular junctions. Tick salivary neurotoxins bind to presynaptic nerve terminals, altering ion channel function and vesicle release machinery without causing immediate cell death or axonal degeneration.[5][9][16][18][20] This leads to a state of reversible neuromuscular blockade, analogous to pharmacologic neuromuscular blockers used in anesthesia, but arising from endogenous tick venom. Cell types involved include motor neurons (CL:0000100), skeletal muscle fibers (CL:0000746), and Schwann cells at motor nerve terminals, though Schwann cells themselves are not directly damaged.

Apoptosis, necrosis, autophagy, and inflammatory cell infiltration are not prominent features; histopathologic examination in animal models and clinical observations suggest that the central nervous system cortex remains unaffected, and patients remain alert and conscious with preserved sensation.[9][16] Stone’s review emphasizes that “the cortex of the central nervous system seems generally unaffected, since the cases remain alert and conscious and sensations are retained,” underscoring that the pathophysiology is peripheral and functional.[9][16] This corresponds to GO processes such as “neuromuscular process controlling balance” (GO:0050907) and “skeletal muscle contraction” (GO:0003009), which are temporarily impaired.

In severe cases, primary hypoventilation due to diaphragmatic and intercostal muscle paralysis is the main cause of death.[5][9][15][16] The MSD Veterinary Manual notes that “primary hypoventilation is the main cause of death in most severe cases, in which alveolar disease may also be present,” suggesting that secondary pulmonary complications such as atelectasis or infection may develop in prolonged paralysis.[5] Thus, respiratory muscle failure leads to global hypoxia, hypercapnia, and systemic organ stress, but again without intrinsic inflammatory or immune-mediated pathology.

### Metabolic Changes and Biochemical Abnormalities

Metabolic changes in tick paralysis are largely secondary to reduced muscle activity and hypoventilation. There is no evidence of primary metabolic derangements such as mitochondrial dysfunction, lipid metabolism defects, or amino acid metabolism abnormalities. Laboratory tests in human cases typically show normal blood chemistries and cerebrospinal fluid, distinguishing tick paralysis from conditions like metabolic myopathies or inflammatory neuropathies.[6][11][13][18][19] Diaz’s meta-analysis and Edlow’s review both emphasize normal CSF in tick paralysis, contrasting it with Guillain–Barré syndrome, where albuminocytologic dissociation is common.[11][19]

Biochemical abnormalities at the synaptic level include reduced acetylcholine release and altered calcium dynamics in presynaptic terminals. Holocyclotoxin and related tick salivary toxins are proteinaceous, likely belonging to CHEBI categories of neurotoxins (e.g., CHEBI:50910) and peptide toxins. Their interaction with presynaptic machinery leads to decreased neurotransmitter release, which is the central biochemical lesion.

### Immune System Involvement

The immune system does not play a primary causal role in tick paralysis. There is no evidence of autoimmune attack against neuromuscular junction components, and tick paralysis is not associated with autoantibodies such as anti–acetylcholine receptor antibodies or anti–VGCC antibodies that characterize myasthenia gravis or Lambert–Eaton myasthenic syndrome.[11][13][18][19] Cytokine elevation, inflammatory infiltrates, and immune-mediated demyelination are absent, and the rapid reversibility of symptoms after tick removal argues against immunologic mechanisms, which typically persist longer and require immunomodulatory treatment.

However, mild immune responses occur at the tick bite site, including local inflammation and formation of a red bump due to host reaction to tick saliva.[2][3][10] WebMD notes that “if the tick has already fallen off, look for a red bump, which is your body’s reaction to the saliva,” reflecting localized innate immune activation.[2] Allergic reactions to tick bites, such as localized swelling or anaphylaxis, are distinct phenomena that can co-occur but are not central to the paralysis mechanism.

### Epigenetic and Molecular Profiling Data

No transcriptomics, proteomics, metabolomics, lipidomics, or epigenomics datasets specific to tick paralysis in human hosts are available in public repositories such as GEO or PRIDE, reflecting the rarity and acute nature of the condition. In tick biology research, salivary gland transcriptomes of various species have been studied, including *Ixodes* and *Dermacentor*, but these data are not yet curated specifically under tick paralysis phenotypes.

Thus, advanced omics-level profiling and single-cell analyses are currently unavailable for this disease, and mechanistic understanding relies on classical physiology and toxin pharmacology rather than multi-omics integration.

### Upstream vs Downstream Mechanisms and Cell-Type Involvement

Upstream mechanisms in tick paralysis include tick salivary gland toxin gene expression, tick feeding behavior, and toxin secretion into the host circulation. These occur in tick cells, particularly salivary acinar cells, which synthesize and secrete holocyclotoxin and other neurotoxins.[8][9][16] Downstream mechanisms occur in host neuromuscular junctions, where toxins act on presynaptic terminals of alpha motor neurons (CL:0000100) innervating skeletal muscle fibers (CL:0000746).[18][20] The primary biological process affected is synaptic transmission at the neuromuscular junction, leading to failure of muscle contraction (GO:0007528, GO:0003009).

Respiratory failure arises when neuromuscular blockade extends to motor neurons innervating the diaphragm (UBERON:0001134) and intercostal muscles (UBERON:0001132). Bulbar palsy and cranial nerve dysfunction reflect toxin effects on motor neurons of cranial nerve nuclei in the brainstem (UBERON:0001898), though central nervous system cortical neurons (CL:0002604) remain unaffected, preserving consciousness and sensation.[9][16][18][20]

Overall, tick paralysis illustrates a clean causal chain: environmental exposure to an arthropod vector leads to toxin delivery; toxin acts on peripheral neuromuscular junctions; neuromuscular transmission fails; muscles become flaccid; and clinical paralysis results, with resolution upon removal of the toxin source.

## 7. Anatomical Structures Affected

### Organ-Level and System-Level Involvement

The primary organ system involved in tick paralysis is the peripheral nervous system, specifically the motor division, and the skeletal muscular system. Motor neurons in the spinal cord anterior horn (UBERON:0002185) project to skeletal muscles of the limbs (UBERON:0002101), trunk, and cranial musculature, forming neuromuscular junctions that are the site of toxin action.[18][20] The respiratory system is secondarily affected, as diaphragmatic and intercostal muscle paralysis leads to ventilatory compromise and potential respiratory failure.[3][4][5][10][13][19]

Cardiovascular, digestive, endocrine, and other systems are largely spared, though severe hypoxia in respiratory failure can secondarily stress organs. The central nervous system cortex (UBERON:0000955) remains generally unaffected, and patients stay alert and conscious, distinguishing tick paralysis from encephalitic processes.[9][16] The brainstem (UBERON:0001898) indirectly participates through cranial nerve motor nuclei, whose axons form neuromuscular junctions in cranial musculature affected by toxins, leading to ophthalmoplegia, facial weakness, and bulbar palsy.[3][6][9][18][20]

### Tissue and Cell-Level Targets

At the tissue level, the primary target is neuromuscular junction tissue, comprising presynaptic motor nerve terminals, postsynaptic muscle endplates, and associated Schwann cells and fibroblasts. Skeletal muscle tissue (UBERON:0001134 for diaphragm, UBERON:0002101 for limb muscles) experiences functional paralysis as neurotransmission fails, even though muscle fibers themselves remain structurally intact.[18][20] Peripheral nerve tissue (UBERON:0001021) containing lower motor axons is functionally compromised at the terminal region; however, motor conduction velocities remain normal, indicating that axons themselves retain structural integrity.[18][20]

Key cell types include alpha motor neurons (CL:0000100), skeletal muscle cells (CL:0000746), Schwann cells (CL:0000219), and synaptic terminal glial cells. Tick salivary gland cells synthesize and secrete neurotoxins; these can be mapped to insect salivary gland epithelial cells, though their specific cell ontology terms are less standardized. The lack of sensory involvement suggests that sensory neurons (CL:0000101) and dorsal root ganglion cells are relatively spared, reinforcing the selective targeting of motor neuromuscular junctions.

### Subcellular Compartments

Subcellular compartments involved include presynaptic active zones of motor nerve terminals, synaptic vesicles containing acetylcholine, voltage-gated calcium channels in presynaptic membranes, and components of the SNARE complex (e.g., synaptobrevin, syntaxin, SNAP-25), though direct targeting of these proteins by tick neurotoxins remains to be experimentally confirmed.[9][16][18][20] In GO Cellular Component terms, relevant compartments are “synapse” (GO:0045202), “neuromuscular junction” (GO:0031594), “synaptic vesicle” (GO:0008021), and “synaptic membrane” (GO:0097060). Holocyclotoxin’s presynaptic effect implies localization to “presynaptic active zone” (GO:0048786).

Mitochondria, nucleus, endoplasmic reticulum, and lysosomes are not primary targets; toxins do not appear to cause mitochondrial dysfunction or nuclear DNA damage. Instead, neuromuscular blockade arises from disruption of ion fluxes and neurotransmitter release processes at the synaptic membrane.

### Anatomical Localization and Lateralization

Anatomically, ticks commonly attach to the scalp, particularly at the hairline on the neck, behind the ears, or in occipital regions, in human cases, leading to toxin delivery near cervical spinal segments.[2][3][6][18] WebMD notes that “ticks can bite anywhere, but the most common spots are on your scalp, especially at the hairline on your neck,” and BCCDC advises special attention to the scalp, neck, ears, and spaces between fingers when searching for ticks.[2][3] In animals, ticks may attach around the head, neck, shoulders, or along the spine, often deeply embedded in fur.[5][9][15][16]

Despite localized attachment, neuromuscular effects are bilateral and symmetric, reflecting systemic toxin distribution rather than regional nerve damage. Ascending paralysis affects both legs and arms symmetrically, and cranial nerve involvement is bilateral (e.g., bilateral ophthalmoplegia, facial weakness).[18][20] Thus, lateralization is generally absent or minimal; asymmetry would suggest alternative diagnoses such as stroke or focal neuropathy.

The localization of respiratory muscle paralysis to the diaphragm and intercostals is critical. The diaphragm (UBERON:0001134) is innervated bilaterally by phrenic nerves originating from cervical spinal segments C3–C5; neuromuscular blockade at these junctions produces global diaphragmatic weakness or paralysis. Intercostal muscles (UBERON:0001132) receive segmental innervation from thoracic spinal nerves; their paralysis further impairs chest wall movement. Together, these anatomical sites explain the respiratory phenotype in severe tick paralysis.

## 8. Temporal Development

### Onset and Latency

Temporal development in tick paralysis is driven by the kinetics of tick feeding and toxin delivery. As multiple sources emphasize, symptoms typically begin only after several days of attachment by a female tick that has been feeding continuously.[1][3][6][9][10][13][16][18][19] The BCCDC states that “symptoms begin after a female tick attaches to the skin and has fed for 5–7 days,” while MedlinePlus notes onset of leg weakness “usually 2 to 7 days after a tick bite.”[3][10] Diaz’s meta-analysis, summarizing 50 U.S. cases, found that paralysis ensues after a mean of 1.4 days (range 1–10 days) following the onset of neurologic symptoms, which themselves occur after several days of tick attachment.[6][19]

Thus, the onset pattern is characterized by a silent incubation phase during which the tick feeds and toxin accumulates, followed by a prodrome and then rapid neurological decline. Clinicians must be aware that patients may not recall the bite itself; they may have been bitten days earlier and be unaware of the attached tick, particularly when it is hidden under hair or clothing.[2][3][6][18]

### Disease Staging and Progression Rate

A conceptual staging of tick paralysis may be proposed for knowledge representation:

Early stage (Prodrome): After sufficient toxin accumulation but before overt paralysis, patients experience nonspecific symptoms such as fatigue, irritability, malaise, restlessness, paresthesias, and muscle pains.[2][3][6][13][18][19] Gait may be modestly unsteady, but strength is largely preserved. This stage corresponds to mild neuromuscular junction blockade that has not yet significantly impaired functional motor output.

Intermediate stage (Ascending motor weakness): Within hours to a day, patients develop progressive motor weakness, beginning in the legs and moving proximally, accompanied by ataxia and areflexia.[1][3][6][11][13][18][19][20] They may struggle to walk, climb stairs, or stand; upper limbs may become weak. Cranial nerve involvement, particularly ophthalmoplegia and facial weakness, may emerge, especially in holocyclotoxin-mediated cases.[9][16][18][20]

Advanced stage (Generalized paralysis and respiratory involvement): In more severe cases, motor weakness progresses to near-complete flaccid paralysis of all four limbs, with marked bulbar dysfunction (dysarthria, dysphagia) and potential respiratory muscle paralysis.[3][4][5][6][9][10][13][18][19][20] Patients may develop dyspnea, hypoventilation, and require mechanical ventilation. The progression rate from intermediate to advanced stage can be rapid—sometimes within 24–48 hours—underscoring the need for urgent diagnosis and intervention.[1][4][10][13][19]

End stage (Respiratory failure and death): Without tick removal and supportive care, continued toxin delivery and persistent neuromuscular blockade can culminate in fatal respiratory failure.[1][3][4][5][10][13][19] Diaz’s meta-analysis reports an overall case fatality rate of 6.0% over 60 years, signifying that a minority of cases progress to this stage.[7][19]

The progression rate is therefore rapid once neurologic symptoms begin, typically moving from prodrome to significant motor weakness within hours to a day, and to life-threatening paralysis in severe cases over 1–2 days. This rapid, monotonic progression contrasts with slower, subacute courses of many neuropathies and justifies classification as an emergency condition in clinical practice.[2][4][10][11][13]

### Disease Duration and Recovery Course

The duration of paralysis before tick removal varies with recognition and intervention. Some patients present early and have only mild to moderate weakness for a brief period; others, particularly misdiagnosed cases, may experience prolonged paralysis. Diaz’s meta-analysis reports that full neurologic recovery typically occurs in 1.5 days (range 1–2.5 days) after tick removal.[6][19] Grattan-Smith et al. observed that in their pediatric series, neurologic deficits resolved quickly after the paralysis tick was removed.[18][20] The CMAJ case report describes an 83-year-old man whose reflexes returned to normal and strength substantially improved within two hours of tick removal, with complete neurologic recovery occurring within 72 hours.[6]

Purdue Extension notes that if paralysis has progressed far, complete recovery may take up to six months, though such extended courses are exceptional.[1] These longer recoveries may reflect secondary complications such as deconditioning, pulmonary sequelae, or unrecognized concurrent diseases rather than persistent toxin effects. In animals, especially dogs with severe holocyclotoxin poisoning, recovery can be slower, and supportive care may be needed for days to weeks.[5][15][16]

Remission patterns are straightforward: removal of the tick initiates remission, and paralysis resolves without relapse, provided no new tick exposure occurs. There is no chronic transformation of tick paralysis into a long-term neuromuscular disorder; once toxin is cleared and neuromuscular transmission restored, the disease is essentially over.

### Critical Windows for Intervention

Temporal analysis reveals critical windows for intervention. The most important period is the early symptomatic phase, when ascending motor weakness and cranial nerve involvement have begun, but before respiratory failure. During this window—often spanning the first 24–48 hours of neurologic symptoms—prompt recognition of tick paralysis and meticulous search for an attached tick can prevent progression to respiratory compromise.[3][4][6][11][13][18][19][20] Edlow’s review emphasizes that tick paralysis should be considered in North American patients with acute ascending flaccid paralysis, and that clinicians should systematically search the entire body for ticks and remove them.[4][11]

Tick season itself constitutes a broader critical period. During late spring and early summer in endemic regions, clinicians should maintain heightened suspicion for tick paralysis in presentations resembling Guillain–Barré syndrome, particularly in children and individuals with outdoor exposures. Public health messaging during tick season can also emphasize daily tick checks as a preventive measure.[3][7][19]

In sum, tick paralysis has an acute onset and rapid progression but also rapid reversal upon correct intervention, making time-sensitive recognition and tick removal the central determinants of outcome.

## 9. Inheritance and Population Characteristics

### Epidemiology: Incidence, Prevalence, and Mortality

Tick paralysis is rare but not negligible, with sporadic cases and occasional clusters reported in endemic regions over many decades. Diaz’s 60-year meta-analysis identified 50 well-documented human cases in the United States between 1946 and 2006, yielding an average of fewer than one published case per year, though many additional unreported or unpublished cases likely occurred.[7][19] The condition is therefore best characterized as very low-incidence, with regional hotspots.

In British Columbia, the BCCDC Public Health Laboratory receives consultations on tick paralysis in 0–2 human cases per year, underscoring low incidence even in an endemic province.[3] In Australia, tick paralysis is more prevalent as a veterinary problem in dogs and cats than in humans; Stone’s review notes 20 human fatalities between 1914 and 1942 attributable to tick bite, all but three in children, suggesting more frequent severe pediatric cases in the early 20th century.[9][16] Contemporary human incidence in Australia is low, but the syndrome remains clinically important due to its severity potential.

Exact prevalence data (cases per 100,000 population) are unavailable, and given the acute, transient nature of the condition, point prevalence in the general population is essentially zero. Incidence is highly seasonal and geographically heterogeneous.

Mortality is low but significant. Diaz’s meta-analysis calculated a case fatality rate (CFR) of 6.0% over 60 years in U.S. cases.[7][19] Stone’s historical data from Australia indicate 20 deaths over 28 years, though denominators were not reported.[9][16] Modern intensive care and heightened awareness likely reduce CFR, but fatal outcomes continue to occur in misdiagnosed or delayed cases. As such, tick paralysis should be considered a low-incidence, low-prevalence, but potentially lethal condition with high short-term morbidity.

### Inheritance Patterns and Genetic Concepts

Because tick paralysis is environmentally acquired and not due to host genetic mutations, classical inheritance concepts such as autosomal dominant, autosomal recessive, X-linked, mitochondrial, multifactorial, or polygenic inheritance do not apply. There is no evidence of vertical transmission or familial clustering beyond shared environmental exposures, and penetrance concepts are irrelevant in the human host.[11][13][19]

The only meaningful inheritance pattern relates to tick genetics, where the ability of certain tick strains to cause paralysis is heritable, as shown in *Dermacentor andersoni* crosses.[8] This pattern, however, concerns the vector’s trait, not the host’s disease susceptibility. Founder effects, consanguinity, carrier frequency, and genetic anticipation are therefore not functional concepts in tick paralysis epidemiology.

### Population Demographics and Geographic Distribution

Population demographics show that tick paralysis primarily affects children, particularly girls, and adults with high environmental exposure. Vedanarayanan’s 2004 review and their earlier pediatric series reported six children aged 3.3 to 5.5 years, five of whom were girls, ultimately diagnosed with tick paralysis among 26 children admitted with acute muscle weakness.[12][13] Diaz’s meta-analysis similarly found a predominance of young girls in endemic regions.[7][19] The CMAJ case report demonstrates that elderly individuals can also present with severe paralysis when exposed.[6]

Geographically, tick paralysis clusters in regions inhabited by paralysis-capable ticks. In North America, this includes the Pacific Northwest, Rocky Mountain states, and parts of the southeastern U.S. for *Dermacentor andersoni* and *D. variabilis*.[3][5][10][19] The BCCDC’s mapping of *D. andersoni* in interior BC highlights western Canada as an endemic zone.[3] In Australia, eastern coastal and subcoastal regions where *Ixodes holocyclus* is abundant form the main risk areas.[9][16][18][20] Other regions with reported cases include South Africa and parts of Europe, where *Ixodes* and *Amblyomma* species can cause paralysis.[5][9][16]

Sex ratio data suggest female predominance in pediatric series, but overall sex distribution in adult cases is more balanced, reflecting exposure patterns.[7][13][19] Age distribution is bimodal, with peaks in young children and outdoor-exposed adults, though comprehensive age histogram data are lacking.

In summary, tick paralysis is an environmentally acquired neurotoxic injury concentrated in specific geographic regions and demographic groups, without host genetic inheritance, but with vector genetic determinants of toxin production.

## 10. Diagnostics

### Clinical Evaluation and Physical Examination

Diagnostic evaluation of tick paralysis hinges on careful clinical assessment and thorough physical examination for attached ticks. The syndrome should be considered in any patient, especially in endemic regions and during tick season, who presents with acute or subacute ascending flaccid paralysis, ataxia, cranial nerve dysfunction, and normal sensory function.[4][6][11][13][18][19][20] Edlow’s review in Current Treatment Options in Neurology underscores that “tick paralysis should be considered in North American patients with acute ascending flaccid paralysis or bulbar paralysis; ticks should be sought over the entire body surface and be removed,” framing tick search and removal as both diagnostic and therapeutic.[4][11]

Physical examination must include meticulous inspection of the scalp, neck, ears, axillae, groin, intergluteal cleft, and between fingers and toes, regions where ticks often attach.[2][3][6][18] The BCCDC advises that “if this diagnosis is suspected, a meticulous examination should be done to look for a tick on the body, with special attention paid to the scalp, neck, ears, and the spaces between the fingers.”[3] WebMD similarly notes common attachment sites along the scalp hairline, armpits, and genitals, and stresses that if any part of the tick remains embedded, toxin release may continue.[2] Identification of an attached, engorged adult female tick—often *Dermacentor* or *Ixodes* species—strongly supports the diagnosis when accompanied by compatible neuromuscular signs.[1][3][5][6][9][16][19]

Clinically, tick paralysis mimics Guillain–Barré syndrome: both present with progressive, ascending weakness, areflexia, and sometimes cranial nerve involvement.[11][12][13][18][19][20] However, tick paralysis typically lacks autonomic dysfunction, sensory loss, and CSF abnormalities, and it reverses rapidly after tick removal. Vedanarayanan’s pediatric series highlighted that initial diagnoses in three of six children were Guillain–Barré syndrome, and that “clinical and electrodiagnostic findings were indistinguishable from those of tick paralysis,” underscoring the diagnostic challenge.[12][13]

### Laboratory Testing and Biomarkers

Routine laboratory tests (complete blood count, metabolic panel, inflammatory markers) and cerebrospinal fluid analysis are generally normal in tick paralysis.[6][11][13][18][19][20] The CMAJ case report noted normal blood and CSF analyses in an 83-year-old man with severe paralysis; CSF protein and cell counts were within reference ranges.[6] Diaz’s meta-analysis and Edlow’s review similarly emphasize normal CSF findings as a distinguishing feature compared with GBS, where CSF protein is often elevated with normal cell counts.[11][19] There are no disease-specific serum biomarkers currently recognized; neurotoxin concentration in blood or CSF is not routinely measured.

Neurophysiologic testing, particularly nerve conduction studies and electromyography (EMG), can assist in differential diagnosis. Grattan-Smith et al. reported “low-amplitude compound muscle action potentials with normal motor conduction velocities, normal sensory studies and normal response to repetitive stimulation,” suggesting a presynaptic neuromuscular junction disorder rather than demyelinating neuropathy.[18][20] These findings overlap with those of botulism and Lambert–Eaton myasthenic syndrome but combined with clinical context and tick detection, they support tick paralysis.[11][13][18][20]

Thus, electrophysiology can reveal reduced CMAP amplitudes (LOINC codes for nerve conduction velocity and EMG testing), but no specific pattern uniquely identifies tick paralysis; clinical correlation is essential.

### Imaging and Histopathology

Neuroimaging (MRI, CT) is typically unnecessary and normal in tick paralysis, unless performed to exclude structural CNS lesions. Spinal cord and brain imaging do not show demyelination, inflammation, or compressive lesions associated with the syndrome.[6][11][13][18][19][20] Histopathology of peripheral nerves and muscles in animal experimental models shows minimal structural change, further corroborating the functional nature of neuromuscular blockade.[9][16]

Therefore, imaging and biopsy do not provide primary diagnostic value; they serve only to rule out alternative diagnoses in ambiguous cases.

### Diagnostic Criteria and Differential Diagnosis

Formal standardized diagnostic criteria for tick paralysis have not been codified by international societies, but key clinical features can be distilled:

Acute or subacute onset of ascending flaccid paralysis, often with prodrome of malaise and paresthesias, and possible cranial nerve involvement, in a patient from an endemic region during tick season, with an attached, engorged adult female tick identified on examination, and normal CSF and neuroimaging, with rapid improvement upon tick removal.[1][3][4][6][11][13][18][19][20]

Differential diagnoses include Guillain–Barré syndrome, botulism, myasthenia gravis, hypokalemic periodic paralysis, spinal cord tumor or compression, diphtheritic neuropathy, organophosphate poisoning, and other causes of acute flaccid paralysis.[4][6][11][13][19][20] The Merck Manual lists Guillain–Barré syndrome, botulism, myasthenia gravis, hypokalemia, and spinal cord tumor in the differential.[4] Diaz’s meta-analysis notes that misdiagnosis of tick paralysis as GBS increased in more recent series, with significantly greater proportions of misdiagnoses in 1992–2006 compared with 1946–1996 (χ² = 7.850, P = 0.005).[7][19]

Distinguishing features include the presence of an attached tick, normal CSF, rapid reversibility after tick removal, lack of autonomic instability, and absence of systemic infection signs. Botulism shares presynaptic neuromuscular blockade but is usually associated with ingestion of contaminated food and lacks tick exposure.

### Genetic Testing and Omics-Based Diagnostics

As tick paralysis is non-genetic in the host, genetic testing (WGS, WES, gene panels, single-gene testing, CMA, karyotyping, FISH, mitochondrial DNA testing, repeat expansion testing) has no role in diagnosis. No gene panels or genetic biomarkers relate to the condition, and genetic counseling is not indicated for affected individuals based solely on tick paralysis.

Omics-based diagnostics, such as transcriptomics, proteomics, and metabolomics, similarly lack application in clinical diagnosis of tick paralysis. The condition is diagnosed clinically and treated by tick removal and supportive care; sophisticated molecular diagnostics would not alter management and are not cost-effective given its rarity and clear etiologic pathway.

### Screening

Screening for tick paralysis in asymptomatic individuals is not practiced and would not be sensible given the disease’s acute, reversible nature and dependence on tick exposure. However, screening for tick bites—through daily tick checks after outdoor exposure—functions as preventive surveillance that can avert paralysis. In this sense, public health campaigns promoting tick checks in endemic regions during tick season serve as secondary prevention mechanisms.

## 11. Outcome and Prognosis

### Survival, Mortality, and Life Expectancy

When recognized promptly and treated by tick removal and supportive care, tick paralysis has an excellent prognosis, with near-complete recovery and minimal long-term sequelae.[1][3][4][6][9][11][13][18][19][20] Diaz’s meta-analysis over 60 years reported a case fatality rate of 6.0%, indicating that most patients survive, though occasional deaths occur in severe, misdiagnosed, or untreated cases.[7][19] In the CMAJ case report, the 83-year-old man recovered fully within 72 hours after tick removal, with no persistent deficits.[6] Grattan-Smith’s pediatric series likewise documented complete recovery after paralysis tick removal in all six children.[18][20]

Life expectancy in individuals who experience tick paralysis and survive is essentially normal; the condition does not cause chronic neuromuscular disease or reduce long-term survival, aside from rare residual complications. Mortality, when it occurs, is disease-specific, resulting from respiratory failure due to respiratory muscle paralysis.[1][3][4][5][10][13][19]

### Morbidity, Disability, and Quality-of-Life Impact

Short-term morbidity is high. During the acute phase, patients experience profound functional disability: inability to walk or stand, difficulty swallowing and speaking, and sometimes inability to breathe independently.[3][4][6][9][13][18][19][20] This can require intensive care admission, mechanical ventilation, and extensive nursing support. Anxiety, fear, and psychological distress can be substantial, particularly in misdiagnosed cases where prognosis is uncertain.

However, because neuromuscular transmission recovers quickly once toxin exposure ceases, long-term disability is rare. Most survivors regain full motor function without residual weakness or neuropathy.[1][3][4][6][9][11][13][18][19][20] Deconditioning after a period of paralysis may lead to temporary fatigue and reduced endurance, but physical therapy can restore pre-illness function.

Quality-of-life measures such as EQ-5D or SF-36 would show near-total impairment in mobility and self-care dimensions during paralysis, with severe pain/discomfort and anxiety/depression, but these scores would normalize rapidly post-recovery. There is no evidence of chronic pain syndromes or psychological sequelae uniquely attributable to tick paralysis, though individuals may develop heightened fear of tick exposure.

### Complications and Recovery Potential

Complications arise primarily from respiratory failure and prolonged immobilization. In severe cases, hypoventilation can cause hypoxic brain injury, cardiac arrhythmias, or multi-organ dysfunction if not promptly corrected.[4][5][9][10][13][19] Secondary infections, such as aspiration pneumonia or catheter-related infections, may occur in ICU settings. In animals, alveolar disease and secondary respiratory pathology may complicate recovery, especially in holocyclotoxin poisoning.[5][15][16]

Despite these risks, recovery potential is high when ticks are removed early and supportive care is provided. The BCCDC notes that “most patients with tick paralysis will recover or substantially improve within a few hours following tick removal,” reflecting the reversibility of the neuromuscular blockade.[3] Merck Manual states that paralysis “usually begins to resolve in a few hours after tick removal, but paralysis may progress for 24 to 48 hours after tick removal,” indicating that toxin clearance can lag slightly but leads to eventual recovery.[4]

Prognostic factors include age, severity of paralysis at presentation, presence of respiratory compromise, and timing of tick removal. Dyspnea, crackles, wheezes, and high neuromuscular junction scores in animals are poor prognostic signs.[5] In humans, advanced age and comorbidities may reduce physiologic reserve, but even elderly patients can recover fully if managed appropriately, as illustrated by the 83-year-old Canadian case.[6]

No molecular prognostic biomarkers have been identified; clinical severity and respiratory status remain the primary predictors. Overall, tick paralysis offers a paradoxical prognosis profile: profoundly dangerous if unrecognized, but almost uniquely reversible with a simple mechanical intervention when properly diagnosed.

## 12. Treatment

### Primary Treatment: Tick Removal

The cornerstone of tick paralysis treatment is prompt, complete removal of the attached tick. All major clinical and public health references emphasize this intervention as both diagnostic and therapeutic.[1][2][3][4][6][9][10][11][13][14][18][19][20] Purdue Extension states that “early recognition of the cause and prompt removal of the engorging female tick typically results in complete recovery,” and that if done soon enough, recovery may be complete within 48 hours.[1] The BCCDC notes that “the treatment for tick paralysis is tick removal,” and that “rapid improvement once an attached tick is properly removed is diagnostic.”[3] The Merck Manual underscores that “tick paralysis can be fatal, but the paralysis is reversible with rapid removal of the tick or ticks,” and that paralysis usually begins to resolve in a few hours after removal.[4]

Proper removal technique involves grasping the tick as close to the skin as possible with fine-tipped tweezers and pulling upward with steady, gentle pressure, avoiding twisting or crushing, to ensure that the mouthparts and head are removed intact.[3][4][6][10][20] The CMAJ case report describes removal of an engorged tick adherent to the mid-back with forceps, leading to rapid recovery.[6] Stone’s review and other guidelines advise disinfecting the skin after removal and avoiding folk methods such as burning or smothering the tick, which may cause saliva and toxin to be regurgitated into the host.[9][16]

This intervention can be annotated with NCIT clinical intervention terms such as “Surgical Removal” (NCIT:C51999) in a broad sense or more specifically “Foreign Body Removal” (NCIT:C17248), though in practice tick removal is a simple outpatient procedure rather than surgery.

### Supportive Care and Respiratory Management

Supportive care is essential in moderate to severe cases, particularly when respiratory muscles or bulbar functions are compromised. The Merck Manual notes that “if breathing is impaired, oxygen therapy or respiratory assistance may be needed,” including mechanical ventilation in ICU settings.[4] WebMD states that if tick paralysis affects breathing, “your doctor may have you use a breathing machine until the symptoms ease,” and advises emergency evaluation for breathing difficulty.[2] BCCDC acknowledges that in rare cases, respiratory difficulties and death may occur due to respiratory muscle paralysis if the tick is not removed rapidly.[3]

Supportive measures include supplemental oxygen, noninvasive ventilation, or endotracheal intubation with mechanical ventilation (NCIT:C15273 “Mechanical Ventilation”), along with monitoring of vital signs, fluid balance, and preventing aspiration. In veterinary care, dogs with trouble breathing may require oxygen and breathing assistance under anesthesia.[15] NCIT terms such as “Supportive Care” (NCIT:C16084) and “Respiratory Support Procedures” (NCIT:C21038) can categorize these interventions.

Physical therapy and occupational therapy may assist recovery by addressing deconditioning and restoring strength and function, though the rapid resolution of neuromuscular blockade may limit the duration of rehabilitation required.

### Pharmacotherapy and Antitoxin Therapies

No specific pharmacologic antidote for tick salivary neurotoxins is widely available for humans. Treatment is primarily mechanical and supportive; pharmacotherapy targets secondary issues such as pain, anxiety, or co-infections. There is no evidence that cholinesterase inhibitors or other neuromuscular agents (e.g., neostigmine) significantly alter toxin-induced presynaptic blockade.

In veterinary medicine, however, canine tick hyperimmune serum, also called tick antiserum (TAS), is used as a specific treatment for holocyclotoxin-mediated paralysis in dogs.[15][16] The Merck Veterinary Manual notes that “canine tick hyperimmune serum, also called tick antiserum (TAS), is the specific treatment for the toxin that causes tick paralysis,” and that dogs with trouble breathing may require additional therapy.[15] Stone’s review describes antitoxin therapy for holocyclotoxin and notes that treatment involves removal of the tick, although removal may trigger further deterioration and respiratory support may be required in ICU settings.[9][16] TAS likely contains antibodies against holocyclotoxin and related salivary toxins, functioning as an immunotherapeutic neutralizing agent (NCIT:C15452 “Antitoxin”).

Pharmacogenomics have not been studied in relation to TAS or other supportive drugs in tick paralysis. No gene–drug interactions or personalized medicine approaches have been described.

### Advanced Therapeutics and Experimental Approaches

Advanced therapeutics such as gene therapy, cell therapy, RNA-based therapies, targeted molecular therapies, and immunotherapies are not applicable to tick paralysis. The disease is acute, non-genetic, and reversible with low-technology interventions; advanced therapeutics would not offer advantage and are unlikely to be pursued.

Experimental treatments in animal models have focused on understanding toxin mechanisms rather than developing human therapies. Research into holocyclotoxin structure and function may one day yield synthetic antitoxins or small-molecule antagonists, but this remains theoretical.

### Treatment Outcomes and Strategy

Treatment response is dramatic: removal of the tick typically leads to rapid improvement in neuromuscular function, sometimes within minutes or hours, with full recovery over one to several days.[1][3][4][6][18][19][20] Merck Manual notes that paralysis may continue to progress for 24–48 hours after removal but then resolves.[4] Diaz’s meta-analysis confirms rapid recovery after tick removal, with full recovery in 1.5 days on average.[6][19]

Side effects and adverse events of tick removal are minimal, though improper removal techniques may leave mouthparts embedded, allowing continued toxin release, or may cause local skin trauma or infection. Antiserum therapy in dogs can carry risks of allergic reactions, but such data are beyond human disease scope.[15][16]

A rational treatment algorithm begins with immediate consideration of tick paralysis in appropriate clinical contexts, urgent full-body examination for ticks, prompt removal using proper technique, assessment of respiratory status, and provision of supportive care including mechanical ventilation if needed. Differential diagnosis should be revisited after tick removal; if neurologic deficits do not improve rapidly, alternative diagnoses like GBS or botulism must be considered.

Personalized medicine approaches are limited, as host genetics do not materially impact treatment decisions; therapy is standardized and driven by clinical severity and respiratory status rather than genotype.

## 13. Prevention

### Primary Prevention: Avoiding Tick Exposure

Primary prevention aims to avert tick bites and prolonged attachment, thereby preventing tick paralysis entirely. Public health agencies, including CDC-equivalent resources, emphasize environmental and behavioral interventions such as wearing protective clothing (long sleeves, long pants), using insect repellents containing DEET or permethrin on skin and clothing, avoiding dense vegetation and leaf litter, walking in the center of trails, and checking for ticks after outdoor activities.[2][3][10][15][16] These measures correspond to NCIT concepts like “Preventive Health Services” (NCIT:C15220) and “Vector Control Intervention” (NCIT:C17151).

Pet-level prevention is critical: regular tick prevention in dogs and cats using acaricidal collars, spot-on treatments, and oral medications reduces the number of ticks in domestic environments and lowers the risk of human tick exposure.[15][16] Veterinary guidance in the Merck manuals underscores the importance of minimizing stress and using tick antiserum where indicated, but prevention through tick control remains foundational.[5][15][16]

Environmental interventions, such as clearing brush, mowing lawns, using acaricides in high-risk areas, and managing wildlife hosts, align with public health vector control strategies.[3][15][16] These can be mapped to NCIT “Environmental Health Intervention” (NCIT:C19157).

### Secondary Prevention: Early Detection and Intervention

Secondary prevention involves early detection of attached ticks and intervention before paralysis develops or while it is still mild. Daily tick checks after outdoor exposure, especially during tick season in endemic regions, allow identification and removal of ticks before they feed for several days.[2][3][10] Special attention should be paid to the scalp, neck, behind ears, axillae, groin, and between fingers and toes.[2][3] Educating parents to inspect children’s scalps and hairlines can prevent pediatric tick paralysis, where scalp-attached ticks often go unnoticed.[3][13][18]

Clinical secondary prevention includes maintaining a high index of suspicion for tick paralysis in patients with acute ascending paralysis during tick season and promptly searching for ticks. Early tick removal prevents progression to respiratory failure and reduces morbidity.[3][4][6][11][13][18][19][20]

Genetic screening is irrelevant to tick paralysis prevention, as no host genetic risk markers exist. However, risk stratification based on environmental exposure—identifying individuals at high risk due to occupation or recreational habits—can guide targeted behavioral interventions.

### Tertiary Prevention: Preventing Complications

Tertiary prevention focuses on preventing complications and long-term sequelae in individuals already affected by tick paralysis. This includes early respiratory support to prevent hypoxic injury, careful nursing to prevent pressure ulcers and deep vein thrombosis during paralysis, and prompt treatment of secondary infections.[4][5][9][10][13][19] Rehabilitation in the recovery phase ensures restoration of muscle strength and function, preventing prolonged disability.

Counseling patients about tick avoidance behaviors and pet tick control post-recovery can prevent future episodes. Genetic counseling is not needed.

In public health terms, tick paralysis prevention overlaps substantially with prevention of other tick-borne diseases, and integrated vector control and health education programs can reduce the combined burden of tick-related illnesses.

### Immunization and Prophylaxis

No vaccines exist against tick salivary toxins causing paralysis, and immunization strategies have not been developed. Research into anti-tick vaccines that target tick salivary proteins to prevent feeding and pathogen transmission has been ongoing in the broader tick research field, but these are not specific to tick paralysis and remain experimental.

Prophylactic medications, such as antibiotics, are irrelevant to tick paralysis, as the condition is noninfectious. In animals, prophylactic tick control products serve as a form of pharmacologic vector prophylaxis, but humans primarily rely on repellents and clothing.

Overall, prevention of tick paralysis is highly feasible through straightforward environmental and behavioral interventions, making it a model for preventable environmental neurotoxicosis.

## 14. Other Species and Natural Disease

### Species Affected and Veterinary Relevance

Tick paralysis affects a broad array of vertebrate species, making it a major veterinary concern in certain regions. Stone’s review notes that in Australia, *Ixodes holocyclus* can cause paralysis in humans, dogs, cats, sheep, cattle, goats, pigs, and horses, but predominantly infests dogs, cats, and humans.[9][16] A table in the review lists *Ixodes holocyclus* as affecting cats, pigs, cattle, horses, sheep, goats, and humans in Australia.[9][16] The MSD Veterinary Manual states that “humans (usually children) and a wide variety of other mammals, birds, and reptiles may be affected” by tick paralysis.[5]

Dogs are the most frequently reported domestic species affected by tick paralysis, particularly in eastern Australia, where holocyclotoxin poisoning is a major cause of canine morbidity and mortality.[5][9][15][16] Clinical signs in dogs parallel those in humans: prodromal lethargy and ataxia, progressing to ascending paralysis, cranial nerve involvement, and respiratory failure in severe cases.[5][15][16] Cats, livestock (sheep, cattle, goats, horses), and sometimes wildlife (e.g., marsupials) also suffer paralysis from holocyclotoxin and other tick neurotoxins.[5][9][16]

In North America, tick paralysis has been reported in cattle, sheep, and horses from *Dermacentor andersoni* and related species.[5][8] The Rocky Mountain wood tick is known to cause potentially fatal paralysis in cattle, sheep, and humans in certain parts of its range.[8] Birds and reptiles may also be affected, though reports are fewer.

Veterinary relevance is substantial: tick paralysis in dogs and livestock can cause deaths, production losses, and welfare concerns, prompting development of tick antiserum (TAS) and intensive prevention efforts.[5][9][15][16]

### Comparative Pathology and Mechanism Conservation

Comparative pathology reveals strong similarities across species. In all affected mammals, tick salivary neurotoxins target neuromuscular junctions, cause ascending motor paralysis, and may induce respiratory failure.[5][9][15][16] The action of holocyclotoxin on acetylcholine release is conserved, and neuromuscular blockade manifests similarly in dogs and humans.[9][16][18][20] Neurologic signs such as ataxia, cranial nerve dysfunction, and areflexia are common across species, though details vary with anatomy and behavior.

Mechanistically, tick paralysis illustrates evolutionary conservation of neuromuscular junction physiology across vertebrates. Toxin targeting of presynaptic calcium channels and release machinery influences motor function in all species with cholinergic neuromuscular junctions. Experimental studies in hamsters and other laboratory animals reproduce paralysis phenotypes seen in natural disease, affirming model validity.[8][9][16]

Differences arise from species-specific physiology and toxin susceptibility. For example, Australian holocyclotoxin tends to cause more severe neurological impairment than North American *Dermacentor* toxins, as noted by Stone and colleagues, who observed that holocyclotoxin “tends to cause more severe neurological impairment than that associated with *D. andersoni* or *D. variabilis* in North America.”[9][16] Dogs appear particularly sensitive to holocyclotoxin, with high mortality if untreated.[15][16]

### Transmission and Zoonotic Considerations

Tick paralysis itself is not zoonotic in the sense of a transmissible infection; it is a vector-borne intoxication. However, ticks represent zoonotic vectors for infectious agents, and animals can serve as reservoirs or amplifiers of tick populations, increasing human exposure. Dogs and livestock carrying paralysis ticks into domestic environments raise human risk; thus, human tick paralysis risk is entwined with animal health and tick ecology.[2][3][10][15][16]

From a disease knowledge base perspective, tick paralysis should be annotated as a multi-species toxic syndrome affecting NCBI Taxon entries such as Homo sapiens (taxon:9606), Canis lupus familiaris (taxon:9615), Felis catus (taxon:9685), Bos taurus (taxon:9913), Ovis aries (taxon:9940), Equus caballus (taxon:9796), and other vertebrates, with cross-species susceptibility mediated by shared neuromuscular junction physiology.

## 15. Model Organisms

### Experimental Models and Induced Paralysis

Experimental models have been used to study tick paralysis, primarily in small mammals such as hamsters and laboratory rodents. Wozniak’s study assessing heritability of paralysis-inducing capacity in *Dermacentor andersoni* used hamsters as bioassay hosts; virulent tick strains caused paralysis in hamsters, while avirulent strains did not.[8] This model allowed assessment of heritable virulence traits and provided a controlled system to observe clinical signs and progression.

In Australia, experimental holocyclotoxin studies have been conducted in laboratory animals to elucidate toxin mechanisms. Cooper and colleagues performed temperature-dependent analyses of evoked acetylcholine release in tick paralysis, likely using animal neuromuscular preparations.[16] These models replicate neuromuscular blockade, enabling electrophysiologic recordings and pharmacologic manipulations.

Model types in tick paralysis research thus include mammalian models (hamsters, rodents, dogs) and in vitro neuromuscular preparations. There are no genetic models in the sense of knockout or transgenic animals susceptible to tick paralysis; susceptibility is natural. However, one might conceptualize tick strains as “genetic models” of vector virulence, with virulent and avirulent strains representing experimental conditions.[8]

### Phenotype Recapitulation and Limitations

Experimental models recapitulate key features of human and veterinary tick paralysis: ascending motor paralysis, cranial nerve involvement, and neuromuscular junction blockade. Electrophysiologic findings of low-amplitude CMAPs with normal conduction velocities in animal preparations mirror those in children with holocyclotoxin paralysis.[18][20] Respiratory failure in animals parallels that in dogs and severe human cases.[5][9][15][16]

Limitations include species differences in toxin sensitivity, differences in tick–host interactions, and ethical constraints on inducing severe paralysis. Hamsters and rodents may respond differently to toxins compared with humans or dogs, making direct translational extrapolation cautious. Additionally, experimental ticks and holocyclotoxin preparations may not fully represent natural toxin variation.

Nonetheless, models have provided crucial mechanistic insights and validated the neuromuscular blockade pathway, lending confidence to clinical pathophysiologic interpretations.

### Research Applications

Model organisms are used to:

Elucidate toxin mechanisms at neuromuscular junctions, including presynaptic effects on acetylcholine release and ion channel dynamics.[9][16][18][20]

Assess tick strain virulence and heritability of paralysis-inducing traits.[8]

Evaluate potential antitoxin therapies, such as TAS in dogs, in controlled settings.[15][16]

Study tick salivary gland gene expression and toxin production, though this field remains emergent.

These applications inform both human neuromuscular physiology and veterinary therapeutics, and they integrate tick genomics and salivary biology into broader toxin research.

## Conclusion

Tick paralysis (MONDO:0005981) is a distinctive, toxin-mediated neuroparalytic syndrome resulting from prolonged feeding by certain female ixodid ticks that secrete neurotoxins in their saliva, with no identified human causal genes and a pathogenesis rooted in vector salivary gland genetics and neuromuscular pharmacology rather than host heredity.[5][8][9][16][17] Clinically, it presents as an acute or subacute ascending flaccid paralysis with prodromal malaise and paresthesias, often accompanied by cranial nerve involvement such as ophthalmoplegia and bulbar palsy, and may culminate in respiratory failure if the attached tick is not promptly removed.[1][3][4][6][9][11][13][18][19][20] Mechanistically, tick neurotoxins—most notably holocyclotoxin from *Ixodes holocyclus*—inhibit presynaptic acetylcholine release at neuromuscular junctions, producing reversible neuromuscular blockade without structural nerve damage, a process well captured by GO terms related to negative regulation of cholinergic synaptic transmission and neuromuscular junction function.[5][9][16][18][20] 

The disease affects humans, especially children and outdoor-exposed adults in endemic regions, but has its greatest burden in veterinary medicine, where dogs, cats, and livestock suffer holocyclotoxin-mediated paralysis in eastern Australia and *Dermacentor* toxin paralyses in North America.[5][8][9][15][16][18][19][20] Epidemiologically, it is rare but seasonally and regionally predictable, with a low incidence yet non-trivial case fatality rate of approximately 6.0% over 60 years in U.S. literature, and with female predominance in pediatric cohorts that likely reflects behavioral and exposure patterns rather than genetic susceptibility.[7][13][19] Crucially, tick paralysis occupies a unique niche in neurology and toxicology as a severe yet almost uniquely reversible cause of acute flaccid paralysis: once recognized and treated by complete tick removal, neuromuscular function typically recovers rapidly, often within hours to days, with minimal long-term sequelae.[1][3][4][6][18][19][20] 

Diagnostic challenges arise because tick paralysis closely mimics Guillain–Barré syndrome and other causes of acute flaccid paralysis, and misdiagnosis has increased over time, underscoring the need for systematic body examination for ticks in appropriate clinical contexts and seasons.[4][11][12][13][18][19][20] Laboratory and CSF findings are usually normal, neuroimaging is unremarkable, and electrophysiology shows reduced CMAP amplitudes with normal conduction velocities, consistent with presynaptic neuromuscular junction dysfunction rather than demyelinating neuropathy, making clinical context and tick detection paramount.[6][11][13][18][19][20] Treatment is straightforward yet time-critical: meticulous removal of the engorged tick using proper techniques halts toxin delivery and initiates recovery, while supportive care, including oxygen and mechanical ventilation, mitigates respiratory complications; in veterinary care, tick antiserum provides specific immunotherapy against holocyclotoxin.[1][3][4][5][9][10][11][13][15][16][18][19][20] Prevention—through tick avoidance behaviors, environmental vector control, and regular tick checks on humans and animals—can almost entirely prevent tick paralysis, making it a model of a predictable, preventable, and curable environmental neurotoxicosis.[2][3][7][10][15][16][19]

From a disease knowledge base perspective, tick paralysis should be annotated as an injury-type, non-genetic disorder in humans (MONDO:0005981; MeSH D013985), with core phenotypes mapped to HPO terms for ascending flaccid paralysis, ataxia, cranial nerve palsies, and respiratory failure, anatomical targets mapped to neuromuscular junctions and respiratory musculature (UBERON, GO, CL), and treatments mapped to NCIT interventions for tick removal and respiratory support.[5][9][16][17][18][19][20] Vector-side genetic determinants of toxin production in ticks warrant incorporation into comparative genomics resources, as they represent “causal genes” in an eco-parasitologic sense and may inform future antitoxin development.[8][9][16] As climate change and habitat shifts potentially alter tick distributions, ongoing surveillance and public health education will be vital to maintain low incidence and mortality, while heightened clinical awareness can ensure that this dramatic but reversible neurotoxidrome remains a rare cause of tragedy and a frequently preventable poison.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:20237909` (1 mention) - Evaluation of degradation of antibiotic tetracycline in pig manure by electron beam irradiation.
  - shared terms: animal

Weighed against this report's own most characteristic terms: `tick`, `paralysis`, `neuromuscular`, `toxin`, `human`, `disease`, `clinical`, `respiratory`, `host`, `nerve`, `removal`, `exposure`, `salivary`, `severe`, `junction`, `note`, `muscle`, `dogs`, `animal`, `include`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 57 |
| Resolved | 55 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 40 |
| Terms named correctly | 19 |
| Terms named as a **different** term | 14 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001285` (2 mentions) - the report calls it "Bulbar palsy"; HP calls it **Spastic tetraparesis**
- `HP:0002353` (2 mentions) - the report calls it "Facial weakness"; HP calls it **EEG abnormality**
- `HP:0002360` (2 mentions) - the report calls it "Dysphagia"; HP calls it **Sleep disturbance**
- `HP:0002243` (1 mention) - the report calls it "Diaphragmatic paralysis"; HP calls it **Protein-losing enteropathy**
- `HP:0002340` (1 mention) - the report calls it "Progressive motor impairment"; HP calls it **Caudate atrophy**
- `HP:0002141` (1 mention) - the report calls it "Gait instability"; HP calls it **Gait imbalance**
- `GO:0050907` (1 mention) - the report calls it "neuromuscular process controlling balance"; GO calls it **detection of chemical stimulus involved in sensory perception**
- `NCIT:C51999` (1 mention) - the report calls it "Surgical Removal"; NCIT calls it **Angioplasty**
- `NCIT:C17248` (1 mention) - the report calls it "Foreign Body Removal"; NCIT calls it **Genetic Variation**
- `NCIT:C16084` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Observational Study**
- `NCIT:C21038` (1 mention) - the report calls it "Respiratory Support Procedures"; NCIT calls it **Molecular Folding**
- `NCIT:C15220` (1 mention) - the report calls it "Preventive Health Services"; NCIT calls it **Diagnosis Assessment**
- `NCIT:C17151` (1 mention) - the report calls it "Vector Control Intervention"; NCIT calls it **South Africa**
- `NCIT:C19157` (1 mention) - the report calls it "Environmental Health Intervention"; NCIT calls it **Specimen**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0003471` (2 mentions), reported as "Flaccid paralysis" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C21038` (Molecular Folding) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001284` (1 mention) - the report calls it "Absent reflexes"; HP calls it **Areflexia**, and lists "Absent reflexes" among its other names
- `HP:0003474` (1 mention) - the report calls it "Sensory neuropathy"; HP calls it **Somatic sensory dysfunction**, and lists "Sensory impairment" among its other names
- `GO:0007269` (1 mention) - the report calls it "regulation of neurotransmitter secretion"; GO calls it **neurotransmitter secretion**
- `GO:0032226` (1 mention) - the report calls it "negative regulation of synaptic transmission, cholinergic"; GO calls it **positive regulation of synaptic transmission, dopaminergic**
- `GO:0007528` (2 mentions) - the report calls it "neuromuscular junction development and function"; GO calls it **neuromuscular junction development**
- `GO:0051924` (1 mention) - the report calls it "regulation of calcium ion concentration"; GO calls it **regulation of calcium ion transport**
- `GO:0005249` (1 mention) - the report calls it "voltage-gated ion channel activity"; GO calls it **voltage-gated potassium channel activity**, and lists "voltage-gated potassium ion channel activity" among its other names