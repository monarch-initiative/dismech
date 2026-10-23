---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-24T20:45:07.919981'
end_time: '2026-09-24T20:49:21.474930'
duration_seconds: 253.56
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Acrocapitofemoral Dysplasia
  mondo_id: MONDO:0011907
  category: Mendelian
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
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 7
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 55
  verified: 51
  not_found: 0
  obsolete: 3
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 33
  labels_matching: 10
  labels_mismatched: 17
  mislabelled_terms:
  - term_id: CL:0000133
    reported_labels:
    - growth plate chondrocyte
    - chondrocyte
    ontology_label: neurectodermal cell
  - term_id: GO:0005101
    reported_labels:
    - hedgehog receptor binding
    ontology_label: GO_0005101
  - term_id: UBERON:0001474
    reported_labels:
    - appendicular skeleton
    ontology_label: bone element
  - term_id: UBERON:0001465
    reported_labels:
    - hip joint
    ontology_label: knee
  - term_id: UBERON:0002385
    reported_labels:
    - thoracic cage
    ontology_label: muscle tissue
  - term_id: NCIT:C33211
    reported_labels:
    - Genetic Testing
    ontology_label: Ooplasm
  - term_id: NCIT:C18537
    reported_labels:
    - DNA Sequencing
    ontology_label: MYC Family Gene
  - term_id: NCIT:C15973
    reported_labels:
    - Orthopedic Surgery
    ontology_label: Immunotoxin Cancer Immunotherapy
  - term_id: NCIT:C80117
    reported_labels:
    - Hip Arthroplasty
    ontology_label: TBL1XR1 wt Allele
  - term_id: NCIT:C25761
    reported_labels:
    - Thoracic Surgery
    ontology_label: Surgically Created Structure
  - term_id: NCIT:C15273
    reported_labels:
    - Physical Therapy
    ontology_label: Longitudinal Study
  - term_id: NCIT:C15272
    reported_labels:
    - Occupational Therapy
    ontology_label: Lobectomy
  - term_id: NCIT:C49236
    reported_labels:
    - Pain Management
    ontology_label: Therapeutic Procedure
  - term_id: NCIT:C20464
    reported_labels:
    - Psychosocial Support
    ontology_label: Cytokine
  - term_id: NCIT:C17189
    reported_labels:
    - Genetic Counseling
    ontology_label: Telophase
  - term_id: NCIT:C18243
    reported_labels:
    - Prenatal Genetic Testing
    ontology_label: Regression
  - term_id: NCIT:C18488
    reported_labels:
    - Preimplantation Genetic Diagnosis
    ontology_label: Angiopoietin-1 Receptor
  labels_variant: 6
  obsolete_terms:
  - term_id: HP:0002355
    ontology_label: obsolete Difficulty walking
    replaced_by: HP:0001288
  - term_id: GO:0005101
    ontology_label: GO_0005101
    replaced_by: GO:0005096
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acrocapitofemoral Dysplasia
- **MONDO ID:** MONDO:0011907 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Acrocapitofemoral Dysplasia** covering all of the
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

# Acrocapitofemoral Dysplasia: An Integrative Research Review

Acrocapitofemoral dysplasia (ACFD) is a very rare Mendelian skeletal dysplasia defined by disproportionate postnatal-onset short stature with short limbs, brachydactyly, a narrow thorax, and distinctive radiographic abnormalities consisting of cone-shaped epiphyses in the hands and hips and an egg-shaped femoral head attached to a markedly short femoral neck.[1][3][11] The disorder is inherited in an autosomal recessive manner and is caused by biallelic pathogenic variants in the *Indian hedgehog* gene (*IHH*), which encodes a signaling protein that is essential for endochondral ossification and maintenance of the growth plate.[1][7][12] Since its delineation in the early 2000s, only a handful of families have been reported worldwide, initially in Belgian and Dutch kindreds and later in Turkish and Pakistani families, each harboring distinct missense variants in the amino-terminal signaling domain of IHH.[4][6][7] Clinically, ACFD is characterized by short stature of variable severity, relatively large head, pectus deformities with a narrow thorax, lumbar lordosis, and shortening of the tubular bones of the hands and feet; intelligence is preserved and congenital anomalies outside the skeleton are absent.[1][11][19] Radiographically, cone-shaped epiphyses appear in childhood and are followed by premature growth plate fusion, leading to permanent shortening of the digits and proximal femora; this phenotype maps convincingly to disrupted Ihh signaling in prehypertrophic and hypertrophic chondrocytes.[11][12][13] Because of its rarity, systematic epidemiologic data, standardized diagnostic criteria, and evidence-based treatment guidelines are lacking, but accumulating molecular and experimental evidence, including conditional *Ihh* knockout and hedgehog-agonist rescue studies in mice, provides a detailed mechanistic understanding of ACFD and related Ihh-deficient chondrodysplasias.[12][13][16] This review synthesizes current knowledge on ACFD across domains—clinical phenotypes, molecular genetics, developmental mechanisms, diagnostics, prognosis, management, prevention, and model systems—to support construction of a structured disease knowledge base entry.

## 1. Disease Information

### 1.1 Definition and Concise Overview

Acrocapitofemoral dysplasia is a rare, monogenic skeletal dysplasia that affects endochondral bone growth, leading to disproportionate short stature with striking involvement of the hands (“acro-”) and capital femoral epiphyses (“-capitofemoral”).[1][3][11] The condition was formally delineated in the early 2000s based on clinical and radiographic characterization of two consanguineous families, in whom all affected individuals exhibited short limbs and brachydactyly associated with cone-shaped epiphyses in hands and hips.[2][7][11] In the original description, the authors emphasized that affected individuals had normal intelligence and no associated malformations outside the skeletal system, suggesting that ACFD represents a relatively “pure” disorder of cartilage and bone growth rather than a multisystem syndrome.[11][19] Subsequent case reports and small series have confirmed the core phenotype while broadening the age range of documented patients, with the first adult cases reported from a Turkish family harboring a novel homozygous IHH variant and a more recent Pakistani family expanding the mutational spectrum.[4][6] Orphanet and MedGen describe ACFD as a postnatal-onset disproportionate short stature with short limbs, brachydactyly, small broad nails, narrow thorax, lumbar lordosis, and characteristic radiographic features of egg-shaped capital femoral epiphyses and cone-shaped epiphyses, mainly in the hands and hips.[3][5]

From a nosologic standpoint, ACFD is classified as a skeletal dysplasia arising from disordered endochondral ossification and is grouped within the hedgehog-signaling-related chondrodysplasias, alongside brachydactyly type A1 and other phenotypes associated with monoallelic *IHH* variants.[1][10][14] The Online Mendelian Inheritance in Man (OMIM) database assigns ACFD the entry number 607778 and notes that the disorder is caused by homozygous missense mutations in *IHH* at chromosome 2q35, outside the region where brachydactyly type A1 mutations cluster.[1][7] MedGen associates ACFD with the concept ID C1843096 and cross-references OMIM 607778, Orphanet ORPHA:63446, and MONDO:0011907, establishing ACFD as a distinct disease entity in multiple biomedical ontologies.[5] The National Organization for Rare Disorders (NORD) similarly recognizes ACFD as a recently delineated skeletal dysplasia with short stature, short limbs, brachydactyly, and a narrow thorax.[8]

### 1.2 Key Identifiers and Ontology Mapping

The disease is represented in several major disease classification and ontology systems. OMIM lists acrocapitofemoral dysplasia under entry 607778 and links it to *IHH* (gene entry 600726).[1] Orphanet assigns the identifier ORPHA:63446 and categorizes ACFD as a “rare skeletal dysplasia,” with a prevalence of less than 1 per 1,000,000 individuals and an autosomal recessive inheritance pattern.[3] MedGen gives the concept ID C1843096 and associates ACFD with SNOMED CT concept 720416007, reflecting its inclusion in standardized clinical terminology used in electronic health records.[5] The Monarch Initiative and MONDO ontology identify ACFD as MONDO:0011907, situating it within a unified cross-species disease ontology and supporting computational disease modeling and data integration.[5][8] Additional identifiers include UMLS CUI (concept unique identifier) C1843096 and DO (Disease Ontology) term DOID:0050604, which collectively facilitate interoperability across clinical, research, and informatics environments.[1][5]

These identifiers can be linked to relevant phenotype, anatomy, and intervention ontologies. Suggested Human Phenotype Ontology (HPO) terms include short stature (HP:0004322), disproportionate short stature (HP:0003498), brachydactyly (HP:0001156), cone-shaped epiphyses (HP:0003221), short femoral neck (HP:0002823), narrow thorax (HP:0000773), lumbar lordosis (HP:0002938), and small broad nails (HP:0001800).[5][11][17] At the disease level, ACFD maps to the MONDO term for acrocapitofemoral dysplasia (MONDO:0011907), and at the anatomical level, primary sites of involvement include long bones of the limbs (UBERON:0002260), proximal femur (UBERON:0001460), phalanges of hand (UBERON:0001443), and vertebral column (UBERON:0001130).[11][12][17]

### 1.3 Synonyms and Alternative Names

The term “acrocapitofemoral dysplasia” is itself descriptive, combining “acro-” (extremities) and “capitofemoral” (capital femoral epiphysis) to highlight the characteristic involvement of the distal phalanges and proximal femoral epiphyses.[11][19] Common synonyms include “ACFD” as an acronym, which appears in MedGen, Orphanet, NORD, and clinical literature.[3][5][8] In some contexts, particularly within radiologic and genetic texts, the disease is referred to as “acrocapitofemoral skeletal dysplasia” or “Indian hedgehog–related acrocapitofemoral dysplasia,” emphasizing its pathophysiologic basis in Ihh signaling.[1][9][10] However, no widely used alternative names exist that fundamentally differ from “acrocapitofemoral dysplasia,” reflecting the relatively recent and specific delineation of the entity. Differential diagnostic terms—such as brachydactyly type A1 or other cone-shaped epiphysis syndromes—are related but distinct and should not be considered synonyms.[9][10]

### 1.4 Data Sources: Individual Patients Versus Aggregated Resources

Information on ACFD is derived from a combination of individual patient data and aggregated disease-level resources. The foundational descriptions by Mortier et al. (J Med Genet 2003, PMID 12624140) and Hellemans et al. (Am J Hum Genet 2003, PMID 12632327) are based on detailed clinical and radiographic evaluation of four affected children from two consanguineous families, coupled with genomewide homozygosity mapping and candidate gene sequencing.[2][7][11][19] More recent reports, such as the Turkish adult siblings described by Ozyavuz Cubuk and Düz (Eur J Med Genet 2021, PMID 34530144) and the Pakistani family studied by Khalid et al. (Mol Genet Genomic Med 2025, PMID 40045933), expand the dataset to a small number of additional individuals but still represent case-based evidence rather than large cohorts.[4][6]

Aggregated resources including OMIM, Orphanet, MedGen, NORD, and clinical genetics panel databases synthesize these case reports into structured disease entries that summarize etiology, inheritance, clinical features, and radiographic hallmarks.[1][3][5][8][10] These resources typically rely on expert curation and literature review rather than direct extraction from electronic health records, reflecting the rarity of the disease and the predominance of published case reports over routine clinical coding. As of current knowledge, there are no population-based registries or large-scale epidemiologic datasets specific to ACFD; thus, most information remains anchored in high-detail descriptions of a few families complemented by mechanistic insights from model organism studies.[6][11][12][16]

## 2. Etiology

### 2.1 Primary Causal Factors: Genetic Basis in *IHH*

Acrocapitofemoral dysplasia is unequivocally a genetic disease caused by biallelic pathogenic variants in the *Indian hedgehog* (*IHH*) gene, located on chromosome 2q35.[1][3][5][7] Hellemans et al. performed genomewide homozygosity mapping in two consanguineous families and localized the disease locus to 2q35–q36 with a maximum two-point LOD score of 8.02 at marker D2S2248; subsequent candidate-gene sequencing identified two distinct homozygous missense mutations in the amino-terminal signaling domain of IHH.[7][11][19] In family 1, affected individuals were homozygous for a c.137C>T transition resulting in a p.Pro46Leu substitution, while in family 2, patients carried a c.569T>C transition encoding p.Val190Ala; both residues are highly conserved and lie outside the cluster of residues associated with brachydactyly type A1.[7][11][15] Functional studies and structural modeling indicate that these mutations alter the signaling capacity of the hedgehog protein, leading to impaired chondrocyte proliferation and abnormal epiphyseal development.[7][12][13]

Later work confirmed the genetic etiology and further delineated the mutational spectrum. Orphanet and OMIM report that homozygous mutations in *IHH* outside the brachydactyly A1 cluster cause ACFD, reinforcing the concept of allelic heterogeneity at the *IHH* locus with distinct phenotypic consequences depending on variant type and zygosity.[1][3] The 2021 report by Ozyavuz Cubuk and Düz described two adult siblings with ACFD who carried a novel homozygous missense variant c.478C>T (p.Arg160Cys) in exon 2, again within the N-terminal signaling domain and likely affecting the protein’s ability to bind and signal through Patched and Smoothened receptors.[4] In 2025, Khalid et al. identified a novel homozygous missense variant c.518C>A (p.Ala173Asp) in exon 2 of *IHH* in a Pakistani family, representing the fourth distinct missense mutation associated with ACFD and expanding both phenotypic and genotypic spectra.[6] Collectively, these findings support a model in which ACFD is caused by biallelic missense mutations in the signaling domain of IHH that reduce hedgehog pathway activity, particularly in growth plate chondrocytes.[1][6][7][12]

Environmental, infectious, or purely mechanistic non-genetic causes have not been implicated in ACFD. All reported families exhibit consanguinity or a clear pattern of autosomal recessive inheritance, and no cases have been described without identifiable *IHH* variants.[4][6][7] Moreover, the convergence of human phenotypes with those observed in *Ihh* knockout or conditional knockout mice underscores the central role of IHH deficiency in driving the disorder, rather than complex gene–environment interactions or polygenic susceptibility.[12][13][16]

### 2.2 Genetic Risk Factors Beyond Primary Causal Variants

The principal genetic risk factor for ACFD is the presence of biallelic pathogenic missense variants in *IHH*, inherited in an autosomal recessive fashion from carrier parents.[1][3][7] As of the most recent literature, four distinct missense variants have been definitively associated with ACFD: p.Pro46Leu (c.137C>T), p.Val190Ala (c.569T>C), p.Arg160Cys (c.478C>T), and p.Ala173Asp (c.518C>A).[4][6][7][15] These variants cluster in the N-terminal signaling domain but are located outside the region associated with brachydactyly type A1, suggesting that they perturb specific aspects of IHH signaling required for growth plate maintenance and cone-shaped epiphysis formation.[1][7][10] ClinVar lists the c.569T>C (p.Val190Ala) variant as pathogenic for acrocapitofemoral dysplasia (RCV000009421), with OMIM as the primary submitter and literature-only evidence based on the original Am J Hum Genet report.[7][15]

Monoallelic heterozygous variants in *IHH* are known to cause brachydactyly type A1 (BDA1, OMIM 112500), and more recently, familial short stature with non-classical brachydactyly has been described in families with heterozygous frameshift or missense *IHH* variants.[10][14][18] A 2022 case report detailed a novel heterozygous frameshift insertion c.387_388insC (p.Thr130Hisfs*18) in *IHH* in two siblings and their mother, all of whom exhibited short stature combined with non-classical BDA1; the variant is predicted to cause nonsense-mediated RNA decay and haploinsufficiency.[18] These observations highlight that even partial reduction of IHH dosage can impair skeletal growth, but in ACFD, complete loss or severe attenuation of signaling due to biallelic missense variants appears necessary to produce the characteristic acrocapitofemoral phenotype.[1][6][7][10]

At present, no modifier genes have been conclusively identified that alter the severity or expressivity of ACFD, and genome-wide association studies are nonexistent due to the extreme rarity of the condition.[6][7] It is possible that common variants in components of the hedgehog pathway, Wnt signaling, or cartilage extracellular matrix could modulate phenotypic variability, but such hypotheses remain untested. Population databases such as gnomAD or ExAC may contain low-frequency missense variants in *IHH*, but specific allele frequencies for the known ACFD variants have not been reported in the accessible literature, likely reflecting their very low frequency and occurrence mainly within consanguineous pedigrees.[6][15]

### 2.3 Environmental and Lifestyle Risk Factors

No specific environmental or lifestyle risk factors have been associated with acrocapitofemoral dysplasia. The disorder manifests in early childhood in individuals with biallelic *IHH* mutations and does not appear to depend on exposures such as toxins, nutritional deficiencies, or mechanical stress.[3][7][11] Orphanet and NORD emphasize its genetic, autosomal recessive nature and do not mention environmental contributors.[3][8] Likewise, primary clinical reports do not identify any consistent environmental triggers or modifiers; in the Belgian and Dutch families described by Mortier and Hellemans, children were born at term without perinatal complications, and growth abnormalities emerged postnatally as cone-shaped epiphyses developed.[2][11] In the Turkish and Pakistani families, there is no indication of relevant environmental exposures beyond typical living conditions.[4][6]

Given that the hedgehog pathway is a central developmental morphogenetic system and that *IHH* functions during prenatal and postnatal bone growth, one might hypothesize that factors affecting hedgehog signaling, such as certain teratogens, could modulate disease expression.[12][13] However, there is no direct evidence that exogenous hedgehog inhibitors (for example, some small-molecule drugs used in oncology) have been used in these patients or that their prenatal or postnatal exposures differ significantly from unaffected siblings.[6][11] Thus, it is most accurate to regard ACFD as a primarily genetic disease with minimal documented contribution from environmental risk factors.

### 2.4 Protective Factors and Gene–Environment Interactions

Specific genetic or environmental protective factors that reduce risk or mitigate severity in ACFD have not been reported. No protective variants in *IHH* have been identified that confer resilience to pathogenic missense mutations, and there are no data on modifier alleles in hedgehog pathway genes that ameliorate skeletal phenotypes.[6][7] Experimental hedgehog pathway activation with Smoothened agonists—such as SAG—in mouse models does suggest that pharmacologic enhancement of hedgehog signaling can partially rescue the consequences of Ihh deficiency, including impaired chondrocyte proliferation and enchondroma formation.[16] In *Ihh* conditional knockout mice, SAG treatment beginning at postnatal day 7 or 14 improved body length and weight and reduced mortality, indicating a potential therapeutic “protective” strategy, but this remains at the level of preclinical research and does not represent a naturally occurring protective factor.[16]

Gene–environment interactions are similarly poorly characterized. In principle, mechanical loading, nutritional status, endocrine milieu (e.g., growth hormone and IGF-1 levels), or exposure to hedgehog-modulating compounds could interact with reduced IHH signaling to influence growth plate dynamics.[12][13][16] However, human data are lacking, and the small number of reported ACFD cases precludes robust analysis of gene–environment interplay. The study of heterozygous *IHH* variants causing familial short stature showed that growth hormone therapy over four years yielded a meaningful increase in height in affected siblings, implying that endocrine interventions can modify growth outcomes in the context of partial Ihh deficiency.[18] Nonetheless, this evidence pertains to heterozygous non-ACFD phenotypes, and extrapolation to ACFD must be cautious.[18]

Overall, current evidence supports a model in which ACFD is driven almost entirely by biallelic *IHH* mutations, with minimal documented influence of external risk or protective factors. Future investigation in larger cohorts or registries, and in animal models exposed to varying environmental conditions, will be needed to detect subtle modifying influences.

## 3. Phenotypes

### 3.1 Clinical and Radiographic Phenotypes: Core Features

The clinical phenotype of acrocapitofemoral dysplasia is characterized by disproportionate short stature with short limbs, brachydactyly, relatively large head, and a narrow thorax often associated with pectus deformities and lumbar lordosis.[1][3][5][11] Affected individuals show short stature of variable degree, with postnatal onset, suggesting that prenatal skeletal growth may be relatively spared and that disease manifestations emerge as cone-shaped epiphyses develop in childhood.[11][19] Hands and feet demonstrate brachydactyly with shortening of the tubular bones, especially the middle phalanges; nails tend to be small and broad.[1][3][5] The thorax is described as narrow, and some patients exhibit pectus excavatum or carinatum; lumbar lordosis is common, reflecting spinal involvement and altered posture.[1][5][11]

Radiographically, ACFD is defined by cone-shaped epiphyses and related epiphyseal configurations involving multiple skeletal sites.[11][19] In the hands, cone-shaped epiphyses are prominent in the middle phalanges, and the configuration leads to premature fusion of the growth plate before puberty, resulting in permanent shortening of the digits.[11] In the hips, the capital femoral epiphyses are egg-shaped, and the femoral neck is strikingly short, producing a characteristic appearance that inspired the name “acrocapitofemoral.”[11][17][19] Similar epiphyseal changes can be observed to varying degrees in the shoulders, knees, and ankles, although the hands and hips are most consistently affected.[11][19] The cone-shaped epiphyses appear early in childhood and later disappear as the growth plate fuses; radiographs of older individuals thus show shortened bones but fewer overt cone-shaped epiphyses.[11][19]

Importantly, affected individuals do not exhibit congenital anomalies outside the skeleton and are of normal intelligence, distinguishing ACFD from many syndromic skeletal dysplasias that involve neurodevelopmental or visceral abnormalities.[1][11] The absence of associated malformations suggests that Ihh deficiency in ACFD primarily targets cartilage and bone tissues with limited impact on other hedgehog-dependent developmental processes, perhaps because the disease-causing mutations selectively reduce IHH function in growth plate chondrocytes rather than producing global hedgehog pathway failure.[7][12][13]

### 3.2 Age of Onset, Severity, and Progression

Orphanet states that acrocapitofemoral dysplasia has neonatal or infantile onset, reflecting the early emergence of growth abnormalities and skeletal changes.[3] However, more detailed clinical descriptions emphasize that the disproportionate short stature is postnatal in onset, with height deficiency and limb shortening becoming apparent in early childhood, often after the first year of life.[1][5][11] Cone-shaped epiphyses appear early in childhood and are radiographically detectable by late infancy or toddlerhood, depending on the timing of epiphyseal ossification.[11][19] The process of epiphyseal dysmorphogenesis and premature growth plate fusion occurs before puberty, such that final adult stature and limb proportions are largely determined by growth patterns in the first decade of life.[11][19]

Symptom severity varies among individuals and families, ranging from moderate short stature with mild limb shortening to more severe dwarfism with pronounced brachydactyly and proximal femoral deformity.[1][4][6][11] Mortier and Hellemans noted variability in height and limb length among affected siblings, suggesting that even within a single family harboring a defined *IHH* mutation, expressivity can be variable.[2][7][11] The Turkish adult siblings described in 2021 exhibited extremely short femoral necks and distinctive hand configurations, indicating that radiographic severity can be substantial.[4] The Pakistani family reported in 2025 similarly showed classic phenotypes but with some differences in thoracic and vertebral involvement.[6]

The disease course is broadly progressive in the sense that growth plate fusion leads to irreversible skeletal shortening, but once epiphyseal fusion has occurred, radiographic changes become stable and no further progression of bone deformity is expected.[11][19] Symptoms such as disproportionate stature and brachydactyly are lifelong features, but there is no evidence of episodic exacerbations, relapsing-remitting patterns, or degenerative joint disease specific to ACFD beyond the mechanical consequences of altered bone geometry.[4][6][11] Because intelligence is normal and visceral organ function appears preserved, quality of life impact is largely related to physical limitations, cosmetic concerns, and potential musculoskeletal pain, especially in the hips and lower back.[8][11]

### 3.3 Frequency of Phenotypes and Quality of Life Impact

Given the small number of documented cases, quantitative estimates of phenotype frequencies (e.g., percentage of patients with a given feature) are not available. Nonetheless, descriptive data indicate that short stature with short limbs, brachydactyly, and narrow thorax are consistently present in all reported individuals, making them core features.[1][3][4][6][11] Cone-shaped epiphyses in the hands and hips and an egg-shaped femoral head attached to a short femoral neck are likewise universal radiographic hallmarks.[7][11][19] Lumbar lordosis, relatively large head, and small broad nails are frequently mentioned but may be somewhat more variable.[1][5] Fusion of the middle phalanges with distal phalanges in the fifth toes was noted in the Turkish adult siblings, suggesting that specific digital anomalies may vary across families.[4]

Quality of life impact has not been formally assessed using instruments such as SF-36 or EQ-5D in ACFD patients. However, extrapolation from similar chondrodysplasias suggests that short stature and limb shortening can affect daily functioning, mobility, and psychosocial well-being, particularly in societies that place practical and social demands on height and physical capabilities.[8][16][18] Hip deformities and short femoral necks may predispose to altered gait, limited range of motion, and early-onset degenerative joint changes, potentially leading to pain and functional impairment.[4][11][17] Narrow thorax and pectus deformities could theoretically restrict pulmonary mechanics, but respiratory function has not been systematically studied in ACFD and no overt respiratory failure has been reported.[1][3][11]

From an ontology perspective, HPO terms capturing quality of life relevant phenotypes include reduced mobility (HP:0002355), abnormal gait (HP:0001288), back pain (HP:0003418), and hip pain (HP:0003375).[4][11] Quality of life instruments could be mapped to ontology terms in PROMIS or NCIT for patient-reported outcomes, but specific data for ACFD are lacking. Future research might employ standardized measures to quantify functional limitations and psychosocial burden, thereby enabling more precise integration into disease burden frameworks such as the Global Burden of Disease (GBD) study.

### 3.4 Suggested HPO Phenotype Terms

Based on current clinical and radiographic descriptions, key suggested HPO terms for acrocapitofemoral dysplasia include short stature (HP:0004322), disproportionate short stature (HP:0003498), short limb (HP:0002113), brachydactyly (HP:0001156), cone-shaped epiphyses (HP:0003221), short femoral neck (HP:0002823), egg-shaped femoral head (captured as abnormal femoral head morphology, HP:0002822), narrow thorax (HP:0000773), pectus deformity (HP:0000766), lumbar lordosis (HP:0002938), broad nails (HP:0001800), normal intelligence (HP:0001249), and absence of non-skeletal anomalies (implicitly mapping to lack of specific HPO terms).[1][3][5][11][17] These terms collectively provide a structured phenotype profile suitable for integration into DECIPHER, ClinVar, and other clinical variant interpretation platforms where ACFD may be considered in differential diagnosis for patients with similar skeletal features.

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: *IHH* (Indian Hedgehog)

The causal gene for acrocapitofemoral dysplasia is *IHH* (Indian hedgehog), a member of the hedgehog family of secreted signaling proteins that regulate cartilage and bone development.[1][7][12] OMIM lists *IHH* under entry 600726 and describes its involvement in several phenotypes, including ACFD (607778), brachydactyly type A1 (112500), and syndromic craniosynostosis.[1][14] MedGen and panelapp resources confirm that *IHH* is located at chromosome 2q35 and highlight its role in skeletal dysplasia panels, with mode of inheritance specified as both monoallelic and biallelic, autosomal or pseudoautosomal, depending on the phenotype.[5][10][14] The hedgehog signaling pathway, in which IHH participates, is a highly conserved developmental pathway that coordinates chondrocyte proliferation, differentiation, and osteoblast development during endochondral ossification.[12][13]

The *IHH* gene encodes a preproprotein that undergoes autocatalytic cleavage into an N-terminal signaling domain and a C-terminal processing domain; the N-terminal domain is modified by cholesterol and palmitate and serves as the active ligand for Patched receptors, initiating downstream Smoothened activation and GLI transcription factor regulation.[7][12][13] The signaling domain extends roughly from amino acids 25 to 198, and the known ACFD-causing missense variants cluster within this region (P46L, R160C, A173D, V190A).[4][6][7] UniProt (Q14623) and structural data indicate that these residues contribute to the protein’s folding and receptor interaction surfaces, although fine-grained structural consequences of each variant have not been fully resolved.[7][12]

### 4.2 Pathogenic Variants: Types, Classification, and Frequency

Pathogenic variants causing ACFD are missense substitutions in the N-terminal signaling domain of IHH, and all reported cases involve homozygous variants inherited from heterozygous carrier parents.[4][6][7][15] The initial variants described by Hellemans et al.—c.137C>T (p.Pro46Leu) and c.569T>C (p.Val190Ala)—were identified in Belgian and Dutch families, respectively; both were absent in control chromosomes and affected highly conserved residues, supporting their pathogenic classification.[7][11][19] ClinVar lists c.569T>C (p.Val190Ala) as pathogenic for acrocapitofemoral dysplasia, with OMIM as the submitter and literature-only evidence based on the 2003 Am J Hum Genet report.[7][15] The c.137C>T variant is also recognized in OMIM but is not separately cataloged in ClinVar in the retrieved data.[1][7][15]

Ozyavuz Cubuk and Düz reported a novel homozygous missense variant c.478C>T (p.Arg160Cys) in two adult siblings with ACFD from a Turkish family, representing the third family and third missense variant associated with the disorder.[4] Khalid et al. subsequently described a novel homozygous missense variant c.518C>A (p.Ala173Asp) in a Pakistani family, expanding the catalog to four pathogenic missense variants and the fourth family.[6] Notably, Khalid et al. emphasized that all three previously described mutants (P46L, R160C, V190A) reside within amino acids 201–308 in the signaling domain, although the exact numbering may differ depending on isoform, and that the newly identified A173D variant broadens the phenotypic and genotypic spectrum.[6] All variants are predicted to alter protein function rather than cause complete loss-of-function via nonsense or frameshift mechanisms, suggesting that a specific level of residual activity may be compatible with the ACFD phenotype but insufficient for normal growth plate dynamics.[6][7][12]

Allele frequency data from gnomAD or other large population databases are not explicitly reported for these variants in the accessible literature, but their occurrence in consanguineous families and absence in control cohorts strongly suggests that they are extremely rare.[6][7][15] Given the rarity of ACFD and the absence of reported heterozygous phenotypes associated with these specific variants, penetrance appears to be complete in homozygotes and negligible in heterozygotes, consistent with autosomal recessive inheritance.[1][3][7] No somatic variants in *IHH* have been implicated in ACFD, and somatic *IHH* mutations are more relevant to oncologic contexts such as chondrosarcomas, which lie outside the scope of this disease.[12][16]

### 4.3 Functional Consequences: Loss of Signaling Function

Functional consequences of ACFD-associated *IHH* variants can be inferred from the role of IHH in growth plate biology and from the phenotypes of Ihh-deficient mouse models. Indian hedgehog produced by prehypertrophic and hypertrophic chondrocytes is essential for chondrocyte and osteoblast proliferation and differentiation during prenatal and postnatal endochondral bone formation; it maintains the growth plate and trabecular bone and regulates periarticular chondrocyte differentiation independently of parathyroid hormone–related protein (PTHrP).[12][13] In conditional *Ihh* knockout mice, loss of Ihh expression in postnatal chondrocytes leads to growth plate disorganization, reduced chondrocyte proliferation, diminished trabecular bone, and altered osteoblast development, resulting in dwarfism and skeletal dysplasia reminiscent of human hedgehog-related chondrodysplasias.[12][16]

ACFD-associated missense variants likely impair the ability of IHH to bind Patched, form active ligand-receptor complexes, and signal effectively to target cells in the growth plate and perichondrium.[7][12][13] Hellemans et al. suggested that the P46L and V190A substitutions, both at strongly conserved positions, affect the structure of the signaling domain and disrupt interactions with receptor or extracellular matrix components, thereby reducing hedgehog pathway activation.[7][11] While direct biochemical assays for these specific variants are limited, the convergence of clinical phenotypes with Ihh-deficient mice supports a loss-of-function mechanism in which IHH signaling is quantitatively reduced rather than qualitatively altered to a gain-of-function or dominant-negative state.[12][13][16] The recessive inheritance and absence of phenotype in heterozygous carriers further support a loss-of-function model.[1][3][7]

Frameshift and nonsense variants in *IHH* have been described in heterozygous form in families with short stature and non-classical brachydactyly A1, indicating that complete loss of one allele can reduce hedgehog signaling sufficiently to impair growth but produce a milder phenotype than ACFD.[18] This suggests a dosage-sensitive relationship between IHH function and skeletal outcomes, with full biallelic loss or severe signaling-domain disruption yielding ACFD, partial loss yielding brachydactyly and short stature, and normal dosage supporting typical skeletal development.[10][14][18] From a gene ontology standpoint, IHH participates in biological processes such as “regulation of chondrocyte proliferation” (GO:0032330), “endochondral ossification” (GO:0001958), and “bone morphogenesis” (GO:0060349), and ACFD can be conceptualized as a disorder arising from perturbation of these processes.[12][13]

### 4.4 Modifier Genes, Epigenetics, and Chromosomal Abnormalities

No modifier genes have been identified that specifically alter the severity or expression of ACFD. The limited number of families and the lack of extensive genomic characterization beyond *IHH* sequencing constrain the ability to detect modulators.[6][7] In other hedgehog-related conditions, variants in genes encoding Patched (PTCH1), Smoothened (SMO), GLI transcription factors, or interacting pathways (such as Wnt or BMP) can influence phenotype, but such interactions have not been documented in ACFD.[12][13][16] Similarly, epigenetic changes affecting *IHH* expression, such as promoter methylation or chromatin remodeling, have not been investigated in patients with ACFD, and there is no evidence that epigenetic dysregulation plays a primary etiologic role.[6][7]

Chromosomal abnormalities such as duplications at 2q35 have been implicated in syndromic craniosynostosis and other phenotypes involving *IHH* and neighboring genes, but these structural variants produce distinct clinical presentations and do not cause ACFD.[14] Panelapp notes “chr2q35dup syndrome (185900)” as a phenotype associated with *IHH*, highlighting that copy-number changes can perturb hedgehog signaling, but no microdeletions, duplications, translocations, or inversions have been reported in ACFD patients.[10][14] Thus, ACFD appears to be strictly associated with point mutations (missense) in *IHH* rather than larger chromosomal lesions.

## 5. Environmental Information

### 5.1 Non-Genetic Contributing Factors

As discussed earlier, acrocapitofemoral dysplasia is fundamentally a genetic disorder with no documented non-genetic primary causes. Environmental factors such as toxins, radiation, pollution, or occupational exposures have not been linked to the development of ACFD in the available literature.[3][7][11] The age of onset, pattern of inheritance, and clustering in consanguineous families argue strongly against environmental etiology and support a Mendelian recessive model.[1][3][7] Clinical reports do not describe any consistent environmental exposures or events preceding the onset of growth abnormalities, nor do they suggest that environmental variation explains phenotypic differences between affected siblings.[2][4][6][11]

In the broader context of skeletal development, environmental influences such as nutrition, endocrine status, and mechanical loading can modulate growth plate dynamics, but these act on a background of genetic programming and are unlikely to create ACFD-like phenotypes in the absence of *IHH* mutations.[12][13][16] For example, malnutrition or chronic illness may cause proportional or mild disproportionate short stature but do not produce cone-shaped epiphyses and egg-shaped femoral heads characteristic of ACFD.[11][19] Therefore, non-genetic factors should be considered secondary modifiers at most, and current evidence does not support any specific environmental contributors.

### 5.2 Lifestyle Factors and Infectious Agents

Lifestyle factors such as smoking, diet, exercise, and alcohol consumption have not been implicated in ACFD pathogenesis or progression. Because ACFD manifests in childhood and reflects developmental abnormalities in the growth plate, adult lifestyle choices are unlikely to influence the emergence of core skeletal features.[3][11] No studies have examined whether differences in childhood physical activity or nutrition modulate disease severity, but the rarity of ACFD and the small number of reported cases make such analyses challenging.[6][7]

No infectious agents, including bacteria, viruses, fungi, or parasites, have been associated with acrocapitofemoral dysplasia. The disease is not infectious, not transmissible, and shows no evidence of inflammation, autoimmunity, or post-infectious phenomena.[1][3][11] Basic science studies in hedgehog signaling have explored viral and chemical modulators, but these experiments address developmental biology rather than ACFD specifically.[12][13] Thus, infectious and lifestyle factors can be considered negligible in the etiologic framework for ACFD.

## 6. Mechanism and Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Phenotype

1) Biallelic pathogenic missense variants in *IHH* reduce the signaling capacity of the Indian hedgehog protein in growth plate chondrocytes, leading to impaired activation of downstream hedgehog pathway components.[1][6][7]

2) Reduced Ihh signaling from prehypertrophic and hypertrophic chondrocytes leads to deficient stimulation of periarticular chondrocyte differentiation and decreased chondrocyte proliferation in the columnar growth plate region, thereby shortening growth plate columns.[12][13]

3) Impaired Ihh signaling results in premature hypertrophic differentiation and early growth plate fusion, particularly in the epiphyses of the tubular bones of the hands and the capital femoral epiphyses, leading to cone-shaped epiphyses and egg-shaped femoral heads.[11][12][19]

4) Premature fusion and altered epiphyseal morphogenesis lead to permanent shortening of involved skeletal elements, manifesting clinically as brachydactyly, short limbs, and short femoral necks.[11][17][19]

5) Global reduction in endochondral bone growth leads to disproportionate postnatal short stature with relatively preserved cranial growth, resulting in a relatively large head compared to body size and a narrow thorax with pectus deformities.[1][3][11]

6) Altered spinal and pelvic mechanics due to limb and hip deformities contribute to lumbar lordosis and potential gait abnormalities, as downstream biomechanical consequences of the primary skeletal changes.[4][11]

7) Despite profound effects on skeletal tissues, Ihh deficiency in ACFD does not significantly affect brain development or visceral organogenesis, leading to normal intelligence and absence of major non-skeletal anomalies, likely because the mutations selectively impair skeletal-specific aspects of hedgehog signaling.[1][11][12]

This causal chain integrates experimental evidence from mouse models with human radiographic and clinical data, acknowledging that some steps—particularly the tissue-specific selectivity—are inferred rather than fully demonstrated in ACFD patients.[11][12][13][16]

### 6.2 Molecular Pathways: Hedgehog and Downstream Cascades

Indian hedgehog is a key ligand in the hedgehog signaling pathway, which regulates endochondral ossification through both PTHrP-dependent and PTHrP-independent mechanisms.[12][13] In the growth plate, Ihh is secreted by prehypertrophic and hypertrophic chondrocytes and binds to the Patched (PTCH) receptor on periarticular chondrocytes and perichondrial cells, relieving PTCH-mediated inhibition of Smoothened (SMO) and allowing activation of GLI transcription factors.[12][13] Activated GLI proteins induce expression of target genes that promote chondrocyte proliferation, delay hypertrophic differentiation, and stimulate bone collar formation and osteoblast development.[12][13] Ihh also upregulates PTHrP production in the periarticular region, which in turn acts on PTH/PTHrP receptors in columnar chondrocytes to maintain their proliferative state and prevent premature hypertrophy, creating a negative feedback loop that maintains growth plate length.[13]

Studies in mouse models demonstrate that Ihh has PTHrP-independent actions as well. In a JCI study, mosaic ablation of the PTH/PTHrP receptor led to upregulation of Ihh action, increased PTHrP, acceleration of periarticular chondrocyte differentiation, and elongation of the columnar region.[13] Overexpression of Ihh in transgenic mice caused PTHrP upregulation, elongated growth plate columns, and increased chondrocyte proliferation.[13] These findings show that Ihh directly stimulates periarticular chondrocyte differentiation to columnar chondrocytes, thereby regulating the mass of proliferating cells independently of PTHrP.[13] In conditional *Ihh* knockout mice, hedgehog signaling is diminished, leading to decreased chondrocyte proliferation, shortened columns, and premature depletion of the growth plate.[12][16]

In ACFD, pathogenic *IHH* missense variants are predicted to reduce ligand-receptor interactions and downstream hedgehog pathway activation. This leads to decreased GLI-mediated transcription of genes necessary for chondrocyte proliferation and survival, diminished PTHrP signaling, and failure to maintain normal growth plate architecture.[7][12][13] At the pathway level, this implicates hedgehog signaling (Reactome R-HSA-5358351), PTHrP signaling, Wnt pathway activation (which can be downstream of hedgehog in bone), and BMP/TGF-β interactions in the pathophysiology.[12][13][16] Suggested GO terms for involved processes include “hedgehog signaling pathway” (GO:0007224), “regulation of chondrocyte proliferation” (GO:0032330), “endochondral ossification” (GO:0001958), and “osteoblast differentiation” (GO:0001649).[12][13]

### 6.3 Cellular Processes: Chondrocyte and Osteoblast Dysregulation

At the cellular level, ACFD reflects dysregulation of chondrocyte proliferation, differentiation, and survival in the growth plate, as well as altered osteoblast development in adjacent bone.[11][12][16] In normal growth plates, periarticular chondrocytes proliferate and differentiate into flat, columnar chondrocytes that undergo rapid proliferation while forming columns; eventually, these columnar cells exit the cell cycle and become hypertrophic chondrocytes, which orchestrate matrix calcification and vascular invasion, followed by replacement with bone.[13] Ihh is produced by prehypertrophic and hypertrophic chondrocytes and acts on periarticular and perichondrial cells to regulate proliferative and differentiative transitions.[12][13]

In Ihh-deficient mice, the growth plate is disorganized, with reduced proliferation in the columnar region and premature hypertrophic differentiation, leading to thin growth plates and early growth cessation.[12][16] Osteoblast development is impaired because Ihh signals from chondrocytes to osteoblast precursors are diminished, resulting in reduced trabecular bone formation and skeletal fragility.[12][16] These cellular processes are mirrored in ACFD, where cone-shaped epiphyses and premature fusion of the growth plate indicate abnormal spatial and temporal patterns of chondrocyte differentiation.[11][19] The cone-shaped morphology reflects localized alterations in proliferation and hypertrophy, likely due to uneven distribution of Ihh signaling across the epiphyseal cartilage.[11][12][13]

Osteoblasts and perichondrial cells are also affected. In Ihh conditional knockouts, osteoblast markers are reduced and bone collar formation is impaired, emphasizing Ihh’s role in osteoblast development.[12] In ACFD, hip and femoral neck deformities suggest that both chondrocyte and osteoblast activities are perturbed during proximal femur development, leading to abnormal bone geometry.[11][17][19] Suggested cell ontology (CL) terms include “growth plate chondrocyte” (CL:0000133), “periarticular chondrocyte” (a subset of chondrocytes in articular cartilage), and “osteoblast” (CL:0000062).[12][13][16]

### 6.4 Protein Dysfunction and Biochemical Abnormalities

Indian hedgehog protein dysfunction in ACFD stems from missense variants in the signaling domain that likely impair folding, processing, or receptor binding. Hedgehog proteins undergo autocatalytic cleavage and cholesterol modification; their N-terminal domains must adopt a specific conformation to interact with Patched receptors and form multimolecular signaling complexes.[7][12] Missense substitutions such as P46L, R160C, A173D, and V190A may destabilize the N-terminal domain, reduce its affinity for Patched, alter its diffusion properties in the extracellular matrix, or impair its ability to be properly processed and secreted.[7][12] While detailed biochemical characterization of these variants is limited, their strong conservation across species and the severe phenotypic consequences of homozygous mutations suggest that they significantly reduce IHH function.[7][11]

Biochemically, hedgehog signaling involves post-translational modifications such as palmitoylation and cholesterylation of the N-terminal domain, as well as interactions with heparan sulfate proteoglycans in the extracellular matrix that shape morphogen gradients.[12][13] Disruption of these processes can diminish the effective concentration and gradient of IHH across the growth plate, producing localized regions of insufficient signaling and abnormal epiphyseal shaping.[12][13] Suggested GO terms for molecular functions include “hedgehog receptor binding” (GO:0005101) and “morphogen activity” (GO:0016015).[12]

No metabolic or systemic biochemical abnormalities (e.g., in serum calcium, phosphate, alkaline phosphatase, or endocrine parameters) have been specifically associated with ACFD, and routine laboratory testing in reported patients has been generally unremarkable.[2][4][6][11] This again underscores that ACFD is a localized developmental disorder of cartilage and bone rather than a systemic metabolic bone disease like rickets or osteogenesis imperfecta.

### 6.5 Immune System and Tissue Damage Mechanisms

The immune system does not play a primary role in acrocapitofemoral dysplasia. There is no evidence of autoimmunity, chronic inflammation, or immune-mediated tissue damage in the growth plate or bone in ACFD patients.[1][3][11] Histopathologic examination has not been reported in detail for human cases, but mouse models of Ihh deficiency do not show inflammatory infiltrates; rather, they show decreased proliferation, altered differentiation, and impaired bone formation.[12][16] Tissue damage mechanisms are therefore developmental and biomechanical rather than inflammatory or degenerative.

Over time, altered bone geometry, particularly in the hips and spine, may predispose to secondary tissue damage such as cartilage wear, osteoarthritis, or mechanical back pain, but these are common consequences of many dysplasias and not unique to ACFD.[4][11] If present, such complications would involve processes like cartilage degeneration, osteophyte formation, and secondary inflammation, but data in ACFD are too limited to specify these mechanisms. Suggested GO terms—if needed—might include “mechanical stimulus response” (GO:0009612) and “cartilage development” (GO:0051216), but they relate to broader skeletal biology rather than a distinct immune mechanism.[12][13]

### 6.6 Epigenetic and Omics Considerations

Epigenetic changes have not been studied in ACFD patients, and there are no transcriptomic, proteomic, metabolomic, or lipidomic profiling data specific to this disorder. Nonetheless, hedgehog signaling and growth plate biology have been extensively investigated in model systems, revealing patterns of gene expression and signaling that underpin endochondral ossification.[12][13][16] For instance, Ihh modulates expression of cyclin D and other cell cycle regulators in chondrocytes, and increased hedgehog signaling correlates with increased chondrocyte proliferation and cyclin D upregulation.[13] Ihh also interacts with Wnt signaling, influencing osteoblast differentiation and trabecular bone formation.[12][16]

In Ihh-deficient mouse models, RNA expression profiling could reveal downregulation of hedgehog target genes and upregulation of markers of premature hypertrophy, but such data are not directly cited in the retrieved literature.[12][16] Proteomic or metabolomic signatures specific to Ihh deficiency have not been reported. Likewise, single-cell analysis and spatial transcriptomics of growth plate chondrocytes in ACFD are not yet available, although these technologies are emerging in skeletal biology research. As a result, multi-omics integration for ACFD remains a theoretical possibility rather than a currently realized resource.

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

Acrocapitofemoral dysplasia primarily affects the skeletal system, specifically bones formed by endochondral ossification, including long bones of the limbs, proximal femora, vertebral bodies, and phalanges.[1][3][11] The most prominent anatomical structures involved are the hands and hips, reflecting the “acro-” and “capitofemoral” components of the disorder.[11][19] In the hands, cone-shaped epiphyses in the middle phalanges lead to brachydactyly and shortening of the fingers.[11] In the hips, egg-shaped femoral heads attached to very short femoral necks produce characteristic deformity that can influence joint biomechanics.[11][17][19]

Secondary involvement includes the thorax and spine. The thorax is narrow, often with pectus excavatum or carinatum, suggesting altered growth of ribs and sternum.[1][3][11] The lumbar spine exhibits lordosis, reflecting changes in vertebral alignment and possibly compensatory mechanisms to maintain posture in the presence of shortened limbs.[11] However, there is no evidence of primary pathology in visceral organs such as heart, lungs, gastrointestinal tract, or nervous system; these systems are generally normal in ACFD.[1][11]

From an anatomical ontology perspective, primary organ-level terms include “skeletal system” (UBERON:0001434), “appendicular skeleton” (UBERON:0001474), “hip joint” (UBERON:0001465), “hand” (UBERON:0002398), “thoracic cage” (UBERON:0002385), and “vertebral column” (UBERON:0001130).[11][12][17] The involvement is bilateral and symmetric in hands and hips, as expected from a genetic developmental disorder.[11][19]

### 7.2 Tissue and Cell-Level Involvement

At the tissue level, acrocapitofemoral dysplasia affects hyaline cartilage in the growth plate and articular surfaces, as well as cancellous and cortical bone derived from endochondral ossification.[11][12][16] Growth plate cartilage at the distal ends of long bones and in the proximal femur is particularly affected, with altered columnar organization, cone-shaped epiphyseal cartilage, and early fusion.[11][19] Articular cartilage at the hip may also be secondarily affected because of abnormal load distribution arising from egg-shaped femoral heads and short necks.[11][17]

The primary cell types involved include periarticular chondrocytes (round cells at the articular surface), columnar chondrocytes (flat, proliferating cells in the growth plate), hypertrophic chondrocytes (terminally differentiated cells that orchestrate calcification), and osteoblasts (bone-forming cells) in the primary spongiosa and bone collar.[12][13][16] Ihh is produced by prehypertrophic and hypertrophic chondrocytes and acts on periarticular chondrocytes and perichondrial osteoblast progenitors.[12][13] In ACFD, Ihh-expressing chondrocytes carry dysfunctional IHH protein, and their signaling to target cells is impaired, affecting both chondrocyte and osteoblast populations.[7][12][16]

Suggested cell ontology terms include “chondrocyte” (CL:0000133), “hypertrophic chondrocyte” (a subtype of CL:0000133), “periarticular chondrocyte” (a location-specific chondrocyte), and “osteoblast” (CL:0000062).[12][13][16] Connective tissue structures such as bone marrow, periosteum, and perichondrium also participate indirectly, but their primary pathology arises from altered signaling rather than intrinsic defects.

### 7.3 Subcellular Structures and Localization

Subcellular structures relevant to IHH signaling include the primary cilium, plasma membrane, secretory pathway compartments (endoplasmic reticulum and Golgi apparatus), and extracellular matrix where hedgehog ligands diffuse.[12][16] Hedgehog signaling requires trafficking of Smoothened to the primary cilium, where it transduces the signal to GLI transcription factors; disruptions in ligand-receptor interactions or ciliary trafficking can impair signal transduction.[12][16] The SAG therapy study in Ihh-deficient mice highlighted that the Smoothened agonist SAG promotes Hh activity by stimulating Smoothened trafficking to the cilium in Ihh-silenced cells, rescuing chondrocyte proliferation and differentiation.[16] This underscores the importance of ciliary localization and subcellular dynamics in hedgehog pathway function.

In ACFD, IHH protein produced by chondrocytes may be misfolded or less efficiently processed, potentially leading to retention in the ER or Golgi or reduced secretion to the extracellular space.[7][12] While these subcellular defects have not been experimentally documented for ACFD variants, they represent plausible mechanisms given the nature of missense substitutions in a secreted signaling protein.[7][12] Suggested GO cellular component terms include “primary cilium” (GO:0005929), “plasma membrane” (GO:0005886), “extracellular space” (GO:0005615), and “growth plate cartilage” (captured indirectly through tissue ontology rather than GO).[12][16]

### 7.4 Localization and Lateralization

The skeletal abnormalities in acrocapitofemoral dysplasia are bilateral and relatively symmetric. Cone-shaped epiphyses occur in multiple digits of both hands, and egg-shaped femoral heads with short necks are present in both hips.[11][19] The thoracic and spinal deformities, such as narrow thorax and lumbar lordosis, also affect bilateral structures and the midline spine.[1][3][11] There is no evidence of lateralization (left versus right predominance) or segmental involvement; this pattern fits the systemic nature of a genetic developmental disorder affecting all growth plates rather than focal lesions.

Localization to particular skeletal sites, such as hands and hips, is more a matter of prominence than exclusivity. Cone-shaped epiphyses have been observed to a variable degree in shoulders, knees, and ankles, but these sites may show less dramatic changes.[11][19] The predominance of hand and hip involvement may reflect differences in growth plate dynamics and mechanical loading, but the underlying Ihh deficiency is systemic.[12][13][16]

## 8. Temporal Development

### 8.1 Onset Patterns

Acrocapitofemoral dysplasia exhibits a postnatal onset pattern with infantile or early childhood manifestation of growth abnormalities. Orphanet notes “Infancy, Neonatal” as age of onset, indicating that clinical features may be apparent in early infancy, but more detailed reports emphasize that disproportionate short stature becomes evident as the child grows and that cone-shaped epiphyses appear early in childhood.[3][11][19] The original descriptions reported that cone-shaped epiphyses are observed in childhood and disappear with premature fusion of the growth plate before puberty, implying that radiographic changes begin within the first few years of life and progress through middle childhood.[11][19]

At birth, affected infants may have near-normal length and proportions, although systematic data on birth metrics are limited.[2][11] As postnatal growth proceeds, the growth plates of hands and hips exhibit abnormal morphology and premature fusion, leading to a divergence from population growth curves and the emergence of disproportionate short stature.[11][19] Thus, onset is insidious rather than acute, and the disorder is chronic and developmental, with the primary window of pathogenesis in early childhood when growth plates are most active.[11][12][13]

### 8.2 Disease Progression and Course

The progression of ACFD follows the life cycle of endochondral growth plates. In early childhood, Ihh deficiency leads to cone-shaped epiphyseal cartilage and altered growth plate organization; as the child approaches puberty, growth plates fuse prematurely, and bone lengths are fixed.[11][19] During this period, stature and limb proportions deviate increasingly from normal, and brachydactyly and hip deformities become pronounced.[11] Once growth plates have fused, the skeletal features become stable, and there is no further progression of bone shortening, although secondary degenerative changes may emerge later.[4][11]

The progression rate is relatively slow and spans several years, corresponding to the length of childhood growth. There are no discrete “stages” defined for ACFD, but one could conceptualize an early stage (cone-shaped epiphyses present, growth plate open), an intermediate stage (ongoing premature fusion), and a late stage (post-fusion skeletal configuration).[11][19] The disease course pattern is therefore progressive through childhood and then stable in adulthood, without episodes of remission or relapse.[11]

Disease duration is lifelong in the sense that skeletal changes and short stature remain present throughout life. However, the active pathogenic process—abnormal growth plate activity—occurs predominantly in childhood and early adolescence.[11][12] Critical periods of vulnerability or opportunity for intervention likely coincide with early childhood, when hedgehog signaling can still influence growth plate behavior; this is supported by SAG therapy timing data in Ihh-deficient mice, where earlier treatment (starting postnatal day 7) was more effective in preventing dwarfism than later treatment (starting day 14).[16]

### 8.3 Remission and Critical Periods

Spontaneous remission does not occur in acrocapitofemoral dysplasia. Once growth plates have fused and skeletal deformities are established, they do not reverse, although adaptive processes may improve functional outcomes.[11][19] Treatment-induced modification of phenotype is possible in theory, as suggested by experimental hedgehog agonist therapy or growth hormone treatment in heterozygous *IHH* mutation carriers, but such interventions do not produce true remission; they modify growth patterns and outcomes but do not remove the underlying genetic defect.[16][18]

Critical periods for potential intervention include the early postnatal and childhood years when growth plates are open and Ihh signaling can influence chondrocyte proliferation and differentiation.[12][16] The SAG therapy study in mice showed that the timing of Smoothened agonist administration affected efficacy, with earlier treatment more effective at preventing dwarfism.[16] Extrapolating cautiously, pharmacologic or endocrine interventions in human ACFD would likely need to be instituted early in life to achieve meaningful impact on final stature and skeletal proportions.[12][16] Once growth plates are fused, interventions shift from growth modulation to orthopedic management of deformities and pain, representing a tertiary prevention strategy.[4][11]

## 9. Inheritance and Population

### 9.1 Epidemiology: Prevalence and Incidence

Orphanet classifies acrocapitofemoral dysplasia as a “rare disease” with an estimated prevalence of less than 1 per 1,000,000 individuals.[3] This estimate reflects its extreme rarity and is based on the small number of reported families rather than systematic population-based data. Incidence (new cases per year) has not been formally quantified, but given that only three to four families have been described worldwide over more than two decades, the incidence is likely far below one per million births.[4][6][7][11]

No national registries, large cohort studies, or Global Burden of Disease analyses have focused specifically on ACFD. The condition is absent from common epidemiologic databases such as SEER or CDC registries, reflecting both its rarity and its benign mortality profile.[3][8] As a result, the epidemiologic characterization of ACFD relies on case reports and curated rare disease databases rather than systematic surveillance.

### 9.2 Inheritance Pattern, Penetrance, and Expressivity

Acrocapitofemoral dysplasia follows an autosomal recessive inheritance pattern. All reported cases occur in children born to heterozygous carrier parents, often with consanguinity, and segregation analysis supports recessive transmission.[1][3][4][6][7] OMIM, Orphanet, MedGen, and NORD all describe ACFD as autosomal recessive.[1][3][5][8] Panelapp indicates that *IHH* has both monoallelic and biallelic modes of inheritance depending on phenotype, noting that biallelic mutations cause a more severe disease form—namely ACFD—while monoallelic mutations tend to cause brachydactyly and mild skeletal hand defects.[10][14]

Penetrance of ACFD-associated *IHH* variants appears to be complete in homozygous individuals; all reported homozygotes exhibit the characteristic phenotype.[4][6][7][11] Expressivity is variable, with differences in the degree of short stature, limb shortening, thoracic deformity, and hip involvement among affected individuals, even within the same family.[2][4][6][11] This suggests that other genetic or environmental factors may modulate phenotypic severity, but the core features are consistently present. There is no evidence of genetic anticipation, as the severity does not progressively increase across generations; rather, the phenotype depends on zygosity and variant type.[1][7]

Germline mosaicism has not been reported in ACFD, likely because the recessive inheritance and consanguineous context reduce the probability of mosaic parent carriers; nonetheless, mosaicism cannot be completely excluded in sporadic cases.[6][7] Founder effects may exist within specific populations where consanguineous marriages are common, such as certain regions of Turkey or Pakistan, but the limited number of families prevents firm conclusions.[4][6] Carrier frequency in the general population is unknown but presumably extremely low; in communities with reported families, carrier frequency may be higher due to local founder variants.[6][7]

### 9.3 Population Demographics and Geographic Distribution

Reported families with acrocapitofemoral dysplasia originate from various geographic and ethnic backgrounds. The initial families studied by Mortier and Hellemans were Belgian and Dutch, indicating occurrence in European populations.[2][7][11] The third family, described by Ozyavuz Cubuk and Düz, was Turkish, suggesting presence in Anatolian populations.[4] The fourth family, reported by Khalid et al., was Pakistani, marking the first documented case from South Asia and broadening the geographic scope.[6] These data demonstrate that ACFD is not confined to a single ethnic group or region but can occur wherever consanguinity and rare pathogenic *IHH* variants coexist.[3][6][7]

Sex distribution appears roughly equal, with both male and female patients reported, and no sex-specific differences in phenotype have been described.[2][4][6][11] Age distribution covers children and adults, with some families documented only in childhood and others, such as the Turkish siblings, followed into adulthood.[4][6][11] However, no systematic data exist on the proportion of patients diagnosed at various ages or on gender ratios, due to the small sample size.

Geographic distribution of specific variants shows some clustering. The P46L and V190A variants were identified in Belgian and Dutch families, the R160C variant in a Turkish family, and the A173D variant in a Pakistani family.[4][6][7] Whether these represent founder mutations or independent occurrences is unclear, but the presence of distinct variants in different populations suggests multiple mutational events rather than a single global founder.[6][7]

## 10. Diagnostics

### 10.1 Clinical and Radiographic Evaluation

Diagnosis of acrocapitofemoral dysplasia relies on a combination of clinical assessment and radiographic imaging. Clinically, disproportionate postnatal short stature, short limbs, brachydactyly, narrow thorax, and lumbar lordosis raise suspicion for a skeletal dysplasia involving endochondral ossification.[1][3][11] Routine physical examination can document height, limb lengths, finger and toe proportions, thoracic shape, spinal curvature, and nail morphology.[1][5][11] Laboratory tests such as serum calcium, phosphate, alkaline phosphatase, and endocrine parameters (growth hormone, IGF-1) are typically normal, helping distinguish ACFD from metabolic bone diseases.[2][18]

Radiography is central to diagnosis. Hand radiographs show cone-shaped epiphyses in the tubular bones, especially the middle phalanges, which appear as triangular or conical ossification centers tapering toward the growth plate.[11][19] Hip radiographs reveal egg-shaped capital femoral epiphyses attached to very short femoral necks, producing a distinctive configuration that is nearly pathognomonic for ACFD.[11][17][19] Radiographs of shoulders, knees, and ankles may show similar epiphyseal changes to a variable degree.[11][19] In older patients, cone-shaped epiphyses may no longer be visible because of premature fusion, but residual shortening of bones and deformity of femoral heads and necks persist.[4][11]

Advanced imaging modalities such as CT and MRI are not routinely required for diagnosis but may be useful to assess hip joint morphology and cartilage thickness in complex cases.[4][11] There are no specific histopathologic criteria, and bone biopsy is not routinely performed. Pathology, if examined, would likely show disorganized growth plate cartilage with altered hypertrophic zone thickness and early fusion, similar to Ihh-deficient mouse models.[12][16]

### 10.2 Genetic Testing Strategies

Genetic confirmation of acrocapitofemoral dysplasia involves sequencing of the *IHH* gene to identify biallelic pathogenic variants. Single-gene testing of *IHH* can be performed when clinical and radiographic features strongly suggest ACFD or another *IHH*-related skeletal dysplasia; this approach is efficient given the strong genotype–phenotype correlation.[1][7][10] Alternatively, targeted skeletal dysplasia panels that include *IHH* and other growth plate-related genes can be used, especially in patients with atypical phenotypes or in settings where comprehensive panel testing is standard.[10][14] Panelapp resources note that *IHH* is included in multiple skeletal dysplasia and craniosynostosis panels, with well-established evidence supporting its role in Acrocapitofemoral dysplasia (MIM#607778) and brachydactyly type A1 (MIM#112500).[10][14]

Whole exome sequencing (WES) and whole genome sequencing (WGS) can also identify *IHH* variants, particularly in undiagnosed skeletal dysplasia cases where phenotype may be complex or overlapping.[6][18] In the Pakistani family reported by Khalid et al., WES was used to detect the c.518C>A (p.Ala173Asp) variant in *IHH*, and segregation analysis confirmed its recessive inheritance.[6] In the family with heterozygous frameshift IHH mutation and short stature plus non-classical brachydactyly, WES, targeted sequencing, or gene panel testing were used to identify the c.387_388insC variant.[18]

Chromosomal microarray (CMA), karyotyping, FISH, mitochondrial DNA testing, and repeat expansion testing are not typically relevant for ACFD, as the disease arises from point mutations in *IHH* rather than structural or cytogenetic abnormalities.[1][7][14] ClinVar provides variant-specific information for at least one pathogenic ACFD-associated IHH mutation (p.Val190Ala), supporting clinical interpretation according to ACMG/AMP guidelines.[15] Suggested NCIT terms for genetic interventions include “Genetic Testing” (NCIT:C33211) and “DNA Sequencing” (NCIT:C18537).

### 10.3 Differential Diagnosis and Clinical Criteria

Standardized diagnostic criteria for acrocapitofemoral dysplasia have not been published in the form of society guidelines, but implicit criteria can be inferred from descriptive and radiographic data.[1][11][19] Key elements include disproportionate postnatal-onset short stature, brachydactyly with cone-shaped epiphyses in the hands, egg-shaped femoral heads with short femoral necks, absence of extra-skeletal anomalies, and autosomal recessive inheritance or consanguinity.[1][3][7][11] Genetic confirmation of biallelic missense variants in *IHH* outside the brachydactyly A1 cluster supports diagnosis.[1][6][7]

Differential diagnosis encompasses several conditions. Brachydactyly type A1, caused by heterozygous *IHH* variants clustered in a specific region, presents with shortened middle phalanges and variable cone-shaped epiphyses but usually lacks the hip deformities and autosomal recessive inheritance of ACFD.[10][14][18] Other cone-shaped epiphysis syndromes, such as hereditary multiple epiphyseal dysplasia or isolated cone-shaped epiphyses, may show similar hand radiographic features but differ in pattern, associated findings, and genetic etiology.[9][11] Spondyloepiphyseal dysplasias and other chondrodysplasias may produce short stature and epiphyseal abnormalities, but their genetic bases involve different genes (e.g., *COL2A1*, *TRPV4*) and they often have additional axial skeletal involvement or extraskeletal manifestations.[9][11]

Because ACFD is extremely rare, differential diagnosis often begins with more common skeletal dysplasias and then narrows as radiographic and genetic clues accumulate. Pattern recognition of the acrocapitofemoral combination—hands and hips with cone-shaped epiphyses and short femoral necks—is particularly valuable.[11][19]

### 10.4 Screening and Omics-Based Diagnostics

Routine population screening for acrocapitofemoral dysplasia is not conducted, given its rarity and relatively benign mortality profile.[3][8] Newborn screening programs focus on metabolic and endocrine disorders; skeletal dysplasias are diagnosed clinically rather than through biochemical screening.[8][11] Carrier screening for *IHH* variants could be considered in families with known ACFD history or in communities with high consanguinity, but no standardized programs exist.[3][6][7]

Omics-based diagnostics beyond gene sequencing—such as RNA sequencing, proteomics, or metabolomics—have not been applied to ACFD in clinical care. Nonetheless, WES and WGS represent omics-level interventions, and their utility has been demonstrated in identifying novel *IHH* variants in rare skeletal dysplasia cases.[6][18] Liquid biopsy, epigenomics, and multi-omics integration have no current role in diagnosing ACFD, although they may contribute to broader understanding of skeletal development and hedgehog pathway biology.

## 11. Outcome and Prognosis

### 11.1 Survival and Mortality

Acrocapitofemoral dysplasia does not appear to significantly reduce life expectancy. Affected individuals in reported families have survived into adolescence and adulthood without evidence of life-threatening complications directly attributable to the disorder.[4][6][11] No data on 5-year or 10-year survival or mortality rates are available, but absence of reported early death suggests that survival is near-normal.[3][8][11] Orphanet and NORD describe ACFD as a skeletal dysplasia without mention of increased mortality, indirectly supporting a favorable survival prognosis.[3][8]

Mortality databases such as CDC WONDER or SEER do not list ACFD as a distinct cause of death, and disease-specific mortality analyses are unavailable.[3][8] Deaths in individuals with ACFD, if they occur, are likely due to unrelated causes or to complications common to the general population rather than to the dysplasia itself.

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity associated with acrocapitofemoral dysplasia arises primarily from physical disability, including short stature, limb shortening, brachydactyly, and hip deformities that may limit mobility and function.[4][11] Short stature can affect daily living (for example, reaching objects, navigating environments designed for average height), while brachydactyly and small broad nails may impair fine motor tasks requiring long fingers.[8][11] Hip deformities and short femoral necks can cause altered gait, reduced hip range of motion, pain, and possibly increased risk of early osteoarthritis, although longitudinal data on joint outcomes are lacking.[4][11][17]

Quality of life impacts have not been formally measured using standardized instruments such as EQ-5D or SF-36 in ACFD patients, but analogies with other skeletal dysplasias suggest that psychosocial effects (self-image, social interactions) and functional limitations (mobility, work capacity) may be significant.[8][16] Nonetheless, preserved intelligence and lack of major visceral involvement allow many individuals with ACFD to lead independent lives, albeit with adaptations.[1][11] Disability classification frameworks such as the International Classification of Functioning (ICF) would categorize functional impairments mainly as limitations in physical mobility and manual dexterity, with variable impact on participation depending on environmental support.

### 11.3 Disease Course and Complications

The disease course of acrocapitofemoral dysplasia is characterized by childhood progression of skeletal deformities followed by a relatively stable adult phenotype. Once growth plates fuse and final stature and bone lengths are fixed, progression of the primary skeletal abnormalities ceases.[11][19] However, secondary complications may arise over time. Altered hip and spine mechanics can predispose to chronic pain, degenerative joint changes, and functional impairment, particularly if deformities are severe.[4][11] Narrow thorax and pectus deformities may affect respiratory mechanics, but overt respiratory failure has not been reported, and pulmonary complications appear minor.[1][3][11]

Recovery in the sense of reversal of skeletal abnormalities is not possible; however, functional recovery and compensation may occur through physical therapy, orthopedic interventions, and environmental adaptations.[4][11] Prognostic factors likely include severity of skeletal deformities, presence of degenerative joint changes, and access to supportive care and orthopedic management, but these have not been systematically studied in ACFD due to its rarity.[4][6][11]

Prognostic biomarkers specific to ACFD do not exist. However, identification of the underlying *IHH* variant may provide some insight into expected severity based on genotype–phenotype correlations, as certain variants may be associated with more pronounced hip deformities or thoracic involvement.[4][6][7] Experimental data in Ihh-deficient mice suggest that early hedgehog agonist therapy can modify disease course, but translational application to humans remains speculative.[16]

## 12. Treatment

### 12.1 Pharmacotherapy and Endocrine Interventions

No approved pharmacologic therapy currently exists specifically for acrocapitofemoral dysplasia. Management is largely supportive and orthopedic, focusing on symptom relief and functional optimization rather than disease modification.[3][8][11] Human growth hormone (GH) therapy has been used in some skeletal dysplasias, including heterozygous *IHH* mutation–associated short stature, but its efficacy in ACFD is unknown.[16][18] A case report of two siblings with short stature and non-classical brachydactyly type A1 due to a heterozygous *IHH* frameshift mutation showed that four years of GH therapy led to significant improvement in height, with a good safety profile.[18] The authors concluded that “continuous use of growth hormone therapy may provide long-term benefits and have a high safety for height growth” in this context.[18] However, differences in zygosity and phenotype between ACFD and heterozygous short stature limit extrapolation; biallelic loss of Ihh signaling may constrain the capacity of GH to stimulate growth plate activity.[12][16][18]

Experimental pharmacotherapy in Ihh-deficient mouse models has shown promising results with Smoothened agonist (SAG) therapy. SAG enhances hedgehog pathway activity by promoting Smoothened trafficking to the primary cilium, thereby rescuing downstream signaling in Ihh-silenced cells.[16] In Ihh conditional knockout mice, SAG treatment increased chondrocyte proliferation and differentiation, corrected stature, decreased mortality, and reduced incidence of enchondroma-like lesions near growth plates, without evident toxicity.[16] Treatment timing was critical: earlier administration (starting postnatal day 7) was more effective than later (day 14) in preventing dwarfism.[16] These findings suggest that hedgehog agonists could represent a potential pharmacologic approach for human Ihh-related skeletal dysplasias, including ACFD, although clinical trials have not yet been conducted.[16]

If translated to human therapy, SAG or similar hedgehog agonists would be categorized under NCIT terms such as “Targeted Therapy” (NCIT:C15632) or “Signal Transduction Inhibitor/Agonist,” with more specific terms reflecting hedgehog pathway modulation. Careful evaluation of off-target effects and oncogenic risks would be necessary, as hedgehog activation can promote tumorigenesis in some contexts.[12][16]

### 12.2 Surgical and Orthopedic Interventions

Surgical management in acrocapitofemoral dysplasia primarily addresses orthopedic deformities, particularly hip abnormalities and severe thoracic or spinal deformities. Short femoral necks and egg-shaped femoral heads can predispose to impingement, reduced range of motion, and degenerative changes; orthopedic procedures such as osteotomy, hip reconstruction, or eventually arthroplasty may be considered to improve function and reduce pain.[4][11][17] However, detailed surgical outcomes in ACFD are not reported in the literature, and management parallels that of other hip dysplasias rather than being disease-specific.[11]

Thoracic deformities such as pectus excavatum or carinatum may be treated surgically if they produce significant respiratory compromise or cosmetic concern, using standard procedures like Nuss or Ravitch techniques.[1][3][11] Lumbar lordosis and spinal alignment issues may be managed with physical therapy, bracing, or, in severe cases, spinal surgery, although again no ACFD-specific data exist.[4][11] NCIT terms for such interventions include “Orthopedic Surgery” (NCIT:C15973), “Hip Arthroplasty” (NCIT:C80117), and “Thoracic Surgery” (NCIT:C25761).

### 12.3 Supportive and Rehabilitative Care

Supportive care for acrocapitofemoral dysplasia focuses on optimizing function and quality of life. Physical therapy can improve strength, flexibility, and gait mechanics, helping individuals adapt to limb and hip deformities and reduce pain.[4][11] Occupational therapy may assist with fine motor tasks and activities of daily living affected by brachydactyly and hand anomalies.[8][11] Pain management strategies, including pharmacologic analgesia and non-pharmacologic approaches, can address chronic musculoskeletal discomfort.[4][11] Psychosocial support and counseling may help individuals and families cope with the challenges of living with a rare skeletal dysplasia.[8][11]

NCIT terms applicable to these interventions include “Physical Therapy” (NCIT:C15273), “Occupational Therapy” (NCIT:C15272), “Pain Management” (NCIT:C49236), and “Psychosocial Support” (NCIT:C20464). While these measures do not alter the pathophysiology of ACFD, they constitute tertiary prevention by reducing complications and enhancing participation.

### 12.4 Experimental and Advanced Therapeutics

Aside from SAG therapy in mice, no advanced therapeutics such as gene therapy, cell therapy, or RNA-based interventions have been tested specifically for ACFD. In principle, gene therapy delivering functional *IHH* to growth plate chondrocytes could correct Ihh deficiency, but technical challenges—including targeting, timing, safety, and scaling—are substantial.[12][16] CRISPR-based gene editing to repair *IHH* mutations in chondrocyte precursors is conceptually possible but far from clinical application.[12][16]

Cell-based approaches such as stem cell transplantation or chondrocyte/osteoblast replacement have not been explored in ACFD. Given that the primary defect lies in signaling rather than cell survival per se, cell therapy would need to restore appropriate hedgehog signaling, which complicates design.[12][16] RNA-based therapies such as antisense oligonucleotides or siRNA are more typically used to reduce expression of pathogenic genes; in ACFD, expression of wild-type *IHH* would need to be increased or mutant protein function enhanced, making RNA-based strategies less straightforward.[12][16]

ClinicalTrials.gov does not list ACFD-specific interventional studies in the retrieved literature, and experimental treatments remain confined to preclinical models. However, Ihh-deficient chondrodysplasias more broadly may attract interest as candidates for hedgehog agonist therapy, and future clinical trials could include ACFD patients.[16] Any such trial would need rigorous monitoring for adverse events, particularly potential tumorigenic effects of hedgehog activation.

### 12.5 Treatment Outcomes and Personalized Strategies

Because no disease-specific pharmacologic treatments are currently available for acrocapitofemoral dysplasia, outcome data focus mainly on natural history and supportive care. Surgical and orthopedic interventions can improve function and reduce pain, but quantitative outcomes (e.g., improvement percentages, complication rates) have not been reported in ACFD.[4][11] Personalized treatment strategies would involve tailoring orthopedic and rehabilitative interventions to the individual’s phenotype, considering severity of hip and hand deformities, thoracic shape, and spinal alignment.[4][11]

Given the strong genotype–phenotype correlation with *IHH* variants, precision medicine approaches could emerge if hedgehog agonist therapies are developed. For instance, variant-specific sensitivity to hedgehog agonists or differential residual signaling activity could inform dosing and timing.[6][7][16] Pharmacogenomic considerations might also involve metabolism and distribution of hedgehog agonists, but such data are hypothetical at this stage.

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of acrocapitofemoral dysplasia involves preventing the occurrence of homozygous pathogenic *IHH* variants in offspring. This can be achieved through genetic counseling, carrier testing, and informed reproductive choices in families with known ACFD history or in high-consanguinity communities where carrier frequency may be elevated.[3][6][7] Preimplantation genetic diagnosis (PGD) and prenatal testing could allow selection of embryos without *IHH* mutations, but specific guidelines for ACFD are not published; general Mendelian disease prevention frameworks apply.[3][6][7] NCIT terms for these interventions include “Genetic Counseling” (NCIT:C17189), “Prenatal Genetic Testing” (NCIT:C18243), and “Preimplantation Genetic Diagnosis” (NCIT:C18488).

Secondary prevention focuses on early detection and intervention to mitigate severity. In ACFD, early diagnosis through careful clinical and radiographic evaluation and genetic testing can identify affected children while growth plates are still active.[1][3][11] If hedgehog agonist or growth-promoting therapies are developed, early initiation could improve outcomes, as suggested by timing effects in mouse SAG therapy.[16] Early orthopedic assessment can also inform timely interventions to prevent or reduce secondary complications such as joint contractures or spinal deformities.[4][11]

Tertiary prevention aims to prevent complications and optimize function in individuals with established disease. This includes orthopedic surgery, physical and occupational therapy, pain management, and psychosocial support to reduce disability and enhance quality of life.[4][11] These interventions do not prevent the disease itself but mitigate its impact.

### 13.2 Screening, Risk Stratification, and Counseling

Population-wide screening for ACFD is not feasible or justified given its rarity. However, targeted carrier screening may be appropriate in families with known mutations or in communities with identified founder variants.[6][7] Risk stratification based on consanguinity and family history can identify couples at increased risk of having affected children, enabling tailored counseling.[3][6][7] ACMG and NSGC guidelines for autosomal recessive disorders provide general frameworks for such counseling, although ACFD-specific documents are lacking.

Genetic counseling should explain the autosomal recessive inheritance pattern, carrier risks (25% chance of an affected child if both parents are carriers), and available reproductive options.[3][6][7] Counseling can also address psychosocial aspects of living with a rare skeletal dysplasia and the potential benefits and limitations of existing treatments. For heterozygous *IHH* variant carriers with short stature and non-classical brachydactyly, counseling may cover GH therapy and its risks and benefits.[18]

### 13.3 Public Health and Environmental Interventions

Because acrocapitofemoral dysplasia is a rare genetic disorder, public health interventions at the population level—such as vaccination, sanitation, or environmental cleanup—do not directly prevent the disease.[3][8] Nonetheless, public health policies promoting access to genetic counseling and reducing stigmatization of consanguinity may indirectly affect disease incidence by encouraging informed reproductive decisions.[3][6][7] Environmental interventions have no specific role in ACFD prevention, as environmental exposures do not cause the disease.

### 13.4 Prophylaxis

No prophylactic medications or procedures exist to prevent acrocapitofemoral dysplasia in genetically at-risk individuals. Prophylaxis in this context refers primarily to reproductive-level interventions such as PGD and prenatal testing. In the future, if hedgehog agonist therapies are shown to prevent progression of skeletal abnormalities when administered early, they might be considered prophylactic against severe deformity in genetically affected infants, but evidence for such strategies in humans is currently absent.[16]

## 14. Other Species and Natural Disease

### 14.1 Species and Orthologous Genes

Indian hedgehog (*Ihh*) is conserved across vertebrate species, including humans (*IHH*), mice (*Ihh*), and other mammals.[12][13] NCBI Gene lists orthologous Ihh genes and supports comparative functional studies. In mice, Ihh plays a similar role in growth plate biology as in humans, and Ihh-deficient phenotypes provide strong mechanistic analogues for human ACFD.[12][13][16] Zebrafish, chickens, and other model organisms also express hedgehog pathway components, but specific orthologous Ihh functions differ somewhat by species and have been more extensively studied in general developmental contexts than in skeletal dysplasias.[12][13]

### 14.2 Natural Disease in Animals and Comparative Pathology

Naturally occurring acrocapitofemoral dysplasia has not been reported in companion animals or livestock. OMIA (Online Mendelian Inheritance in Animals) and veterinary literature do not list ACFD as a recognized entity in animals, although numerous skeletal dysplasias with short limbs and epiphyseal abnormalities occur in dogs, cattle, and other species.[12][16] These animal disorders generally involve different genes or broad developmental processes and are not known to involve Ihh-specific mutations analogous to human ACFD.[12][16]

However, comparative pathology is informative. Ihh-deficient mouse models recapitulate key features of human Ihh-related chondrodysplasias, including short stature, short limbs, narrow thorax, and abnormal growth plates.[12][16] The SAG therapy study demonstrated that hedgehog pathway activation can rescue skeletal phenotypes in Ihh-deficient mice, providing a preclinical platform for therapeutic translation.[16] Comparative studies of hedgehog signaling across species highlight evolutionary conservation of growth plate regulation and the central role of Ihh in endochondral ossification.[12][13]

### 14.3 Transmission and Zoonotic Potential

Acrocapitofemoral dysplasia is a non-infectious genetic disorder and has no zoonotic potential. Transmission occurs solely through inheritance of pathogenic *IHH* variants and is limited to human familial contexts.[1][3][7] Cross-species susceptibility is relevant only in terms of experimental models, where gene knockout or transgenic techniques reproduce Ihh deficiency in animals; these are not natural transmissions but induced genetic changes.[12][16]

## 15. Model Organisms

### 15.1 Types and Genetic Models

Mouse models represent the primary experimental systems for studying Ihh-related skeletal dysplasias analogous to acrocapitofemoral dysplasia. Conditional *Ihh* knockout mice, in which Ihh is specifically ablated in chondrocytes, have been generated to examine postnatal roles of Ihh in growth plate maintenance and bone formation.[12][16] These models allow tissue-specific and temporal control of Ihh deletion, illuminating effects on chondrocyte proliferation, differentiation, and osteoblast development without causing early embryonic lethality.[12][16]

In one PNAS study, Ihh expression was conditionally eliminated in postnatal chondrocytes, demonstrating that Ihh is essential for maintaining the growth plate and articular surface and for sustaining trabecular bone after birth.[12] The authors showed that loss of Ihh signaling from the growth plate altered chondrocyte differentiation and affected osteoblast development, leading to diminished trabecular bone and dwarfism.[12] In another study, mosaic ablation of the PTH/PTHrP receptor in the growth plate allowed investigation of Ihh’s PTHrP-independent roles, demonstrating that Ihh stimulates periarticular chondrocyte differentiation and regulates columnar cell mass.[13] These models collectively recapitulate key human features of Ihh deficiency.

### 15.2 Phenotype Recapitulation and Limitations

Ihh-deficient mouse models reproduce many aspects of human ACFD and related chondrodysplasias, including short stature, short limbs, narrow thorax, and abnormal growth plates.[12][16] Radiographically and histologically, mice show shortened long bones, reduced growth plate thickness, disorganized hypertrophic zones, and impaired bone collar and trabecular bone formation.[12][16] However, specific features of human ACFD, such as cone-shaped epiphyses and egg-shaped femoral heads, have not been described in detail in mice, likely due to species differences in epiphyseal morphology and growth plate structure.[11][12][19]

Mouse models lack the exact hand and hip configurations seen in human ACFD, but they provide mechanistic insight into Ihh’s role in growth plate dynamics and endochondral ossification.[12][13][16] Limitations include differences in skeletal anatomy, growth patterns, and lifespan, which affect translation of therapeutic timing and dosing from mice to humans.[12][16] Additionally, global or conditional knockouts may produce more severe phenotypes than missense variants in humans, complicating direct comparison.

### 15.3 Applications and Resources

Model organism studies of Ihh deficiency are invaluable for examining mechanistic questions, testing pharmacologic interventions, and exploring gene–environment interactions. SAG therapy in Ihh conditional knockout mice demonstrated that boosting hedgehog signaling can rescue skeletal phenotypes, suggesting potential therapeutic pathways for human diseases.[16] These models also allow assessment of long-term effects and toxicity of hedgehog agonists, which is critical for translational planning.[16]

Resources such as the Mouse Genome Informatics (MGI) database and the International Mouse Phenotyping Consortium (IMPC) catalog *Ihh* knockout and conditional models, although specific ACFD-like phenotypes may not be explicitly annotated.[12][16] These resources facilitate access to model lines, phenotypic data, and experimental protocols for researchers studying hedgehog-related skeletal disorders. Other model systems, such as zebrafish and organoid cultures of growth plate cartilage, could be developed to provide complementary insights but are not yet documented for ACFD.

## 16. Conclusion

Acrocapitofemoral dysplasia is a rare but mechanistically well-understood Mendelian skeletal dysplasia caused by biallelic missense variants in the *Indian hedgehog* gene (*IHH*), which selectively disrupt hedgehog signaling in growth plate chondrocytes and perichondrial cells.[1][3][6][7] Clinically, ACFD presents with disproportionate postnatal-onset short stature, short limbs, brachydactyly, narrow thorax, lumbar lordosis, and small broad nails, with normal intelligence and absence of major non-skeletal malformations.[1][3][5][11] Radiographically, the disorder is defined by cone-shaped epiphyses in the hands and hips, egg-shaped femoral heads attached to markedly short femoral necks, and variable epiphyseal involvement at shoulders, knees, and ankles; these features arise from abnormal growth plate architecture and premature fusion linked to Ihh deficiency.[11][17][19]

Genetically, ACFD exemplifies allelic heterogeneity at the *IHH* locus, with at least four distinct homozygous missense variants (P46L, V190A, R160C, A173D) causing similar phenotypes in families of Belgian, Dutch, Turkish, and Pakistani origin.[4][6][7] The autosomal recessive inheritance and consistent penetrance in homozygotes, coupled with variable expressivity, underscore the importance of both pathogenic variants and potential modifiers, although specific modifier genes are not yet identified.[1][3][6][7] Diagnostic confirmation relies on clinical and radiographic pattern recognition and genetic testing of *IHH*, typically via single-gene sequencing or inclusion in skeletal dysplasia panels.[1][7][10][14]

Mechanistically, acrocapitofemoral dysplasia illuminates the critical role of Ihh in maintaining the growth plate and coordinating chondrocyte proliferation, differentiation, and osteoblast development. Experimental studies in conditional *Ihh* knockout mice demonstrate that postnatal chondrocyte-derived Ihh is essential for growth plate integrity, articular surface maintenance, and trabecular bone formation, and that its absence leads to dwarfism, skeletal dysplasia, and enchondroma-like lesions.[12][16] JCI work reveals that Ihh stimulates periarticular chondrocyte differentiation and regulates columnar cell mass independently of PTHrP, highlighting complex pathway dynamics that are perturbed in ACFD.[13] These insights provide a robust causal chain from *IHH* mutation to clinical phenotype, bridging molecular genetics, developmental biology, and orthopedic manifestations.

Therapeutically, management of ACFD currently centers on supportive and orthopedic care, including physical and occupational therapy, pain management, and surgical interventions for severe hip or thoracic deformities.[4][11] Pharmacologic therapies such as growth hormone have shown benefit in heterozygous *IHH* mutation–related short stature but have not been systematically assessed in ACFD; hedgehog agonists like SAG have demonstrated striking efficacy in rescuing skeletal phenotypes in Ihh-deficient mice, suggesting a potential future avenue for disease-modifying treatment.[16][18] Prevention focuses on genetic counseling, carrier testing, and reproductive planning in families with known mutations, as environmental or infectious prevention strategies are irrelevant for this genetic disorder.[3][6][7]

Many knowledge gaps remain, particularly in epidemiology, long-term outcomes, and human therapeutic trials. Given the extreme rarity of ACFD, international collaboration, centralized registries, and integration of ontological frameworks (MONDO, HPO, GO, CL, UBERON, NCIT) will be essential to accumulate sufficient data for evidence-based guidelines. Model organism studies and emerging technologies in single-cell and spatial transcriptomics offer promising routes to refine mechanistic understanding and identify new therapeutic targets.[12][13][16] In the meantime, acrocapitofemoral dysplasia serves as a paradigmatic example of how precise genetic lesions in a developmental signaling pathway can produce highly specific skeletal phenotypes, and how translational research linking human genetics with experimental biology can illuminate pathophysiology and guide future interventions.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 55 |
| Resolved | 51 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 3 |
| Unverifiable | 1 |
| Terms whose name was checked | 33 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 17 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0000133` (3 mentions) - the report calls it "growth plate chondrocyte", "chondrocyte"; CL calls it **neurectodermal cell**
- `GO:0005101` (1 mention) - the report calls it "hedgehog receptor binding"; GO calls it **GO_0005101**
- `UBERON:0001474` (1 mention) - the report calls it "appendicular skeleton"; UBERON calls it **bone element**
- `UBERON:0001465` (1 mention) - the report calls it "hip joint"; UBERON calls it **knee**
- `UBERON:0002385` (1 mention) - the report calls it "thoracic cage"; UBERON calls it **muscle tissue**
- `NCIT:C33211` (1 mention) - the report calls it "Genetic Testing"; NCIT calls it **Ooplasm**
- `NCIT:C18537` (1 mention) - the report calls it "DNA Sequencing"; NCIT calls it **MYC Family Gene**
- `NCIT:C15973` (1 mention) - the report calls it "Orthopedic Surgery"; NCIT calls it **Immunotoxin Cancer Immunotherapy**
- `NCIT:C80117` (1 mention) - the report calls it "Hip Arthroplasty"; NCIT calls it **TBL1XR1 wt Allele**
- `NCIT:C25761` (1 mention) - the report calls it "Thoracic Surgery"; NCIT calls it **Surgically Created Structure**
- `NCIT:C15273` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Longitudinal Study**
- `NCIT:C15272` (1 mention) - the report calls it "Occupational Therapy"; NCIT calls it **Lobectomy**
- `NCIT:C49236` (1 mention) - the report calls it "Pain Management"; NCIT calls it **Therapeutic Procedure**
- `NCIT:C20464` (1 mention) - the report calls it "Psychosocial Support"; NCIT calls it **Cytokine**
- `NCIT:C17189` (1 mention) - the report calls it "Genetic Counseling"; NCIT calls it **Telophase**
- `NCIT:C18243` (1 mention) - the report calls it "Prenatal Genetic Testing"; NCIT calls it **Regression**
- `NCIT:C18488` (1 mention) - the report calls it "Preimplantation Genetic Diagnosis"; NCIT calls it **Angiopoietin-1 Receptor**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0002355` (obsolete Difficulty walking) (1 mention) - replaced by `HP:0001288`
- `GO:0005101` (GO_0005101) (1 mention) - replaced by `GO:0005096`
- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0032330` (2 mentions) - the report calls it "regulation of chondrocyte proliferation"; GO calls it **regulation of chondrocyte differentiation**
- `GO:0007224` (1 mention) - the report calls it "hedgehog signaling pathway"; GO calls it **smoothened signaling pathway**, and lists "hedgehog signaling pathway" among its other names
- `GO:0009612` (1 mention) - the report calls it "mechanical stimulus response"; GO calls it **response to mechanical stimulus**, and lists "mechanical stimulus response" among its other names
- `GO:0005929` (1 mention) - the report calls it "primary cilium"; GO calls it **cilium**, and lists "primary cilium" among its other names
- `GO:0005615` (1 mention) - the report calls it "extracellular space"; GO calls it **obsolete extracellular space**, and lists "intercellular space" among its other names
- `NCIT:C15632` (1 mention) - the report calls it "Targeted Therapy"; NCIT calls it **Chemotherapy**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000133` - called "growth plate chondrocyte", "chondrocyte"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.