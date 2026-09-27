---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-12T12:53:16.544570'
end_time: '2026-09-12T13:24:17.879119'
duration_seconds: 1861.33
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Infantile Cerebellar-Retinal Degeneration
  mondo_id: MONDO:0013802
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
citation_count: 23
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 23
  on_topic: 16
  validator_version: 0.2.1
term_validation:
  total_terms: 38
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 0
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: MONDO:0013802
    reported_labels:
    - MONDO
    ontology_label: infantile cerebellar-retinal degeneration
  - term_id: HP:0008936
    reported_labels:
    - Clinical sign
    ontology_label: Axial hypotonia
  - term_id: HP:0002078
    reported_labels:
    - Clinical sign
    ontology_label: Truncal ataxia
  - term_id: HP:0000648
    reported_labels:
    - Physical/ophthalmologic
    ontology_label: Optic atrophy
  - term_id: HP:0000565
    reported_labels:
    - Clinical sign
    ontology_label: Esotropia
  - term_id: HP:0000556
    reported_labels:
    - Physical
    ontology_label: Retinal dystrophy
  - term_id: HP:0001250
    reported_labels:
    - Clinical sign
    ontology_label: Seizure
  - term_id: HP:0001249
    reported_labels:
    - Cognitive
    ontology_label: Intellectual disability
  - term_id: HP:0001272
    reported_labels:
    - Imaging
    ontology_label: Cerebellar atrophy
  - term_id: HP:0002059
    reported_labels:
    - Imaging
    ontology_label: Cerebral atrophy
  - term_id: HP:0001344
    reported_labels:
    - Behavioral
    ontology_label: Absent speech
  - term_id: HP:0009830
    reported_labels:
    - Clinical sign
    ontology_label: Peripheral neuropathy
  - term_id: HP:0000580
    reported_labels:
    - Physical
    ontology_label: Pigmentary retinopathy
  labels_variant: 1
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
  path: Infantile_Cerebellar-Retinal_Degeneration-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Infantile_Cerebellar-Retinal_Degeneration-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Infantile Cerebellar-Retinal Degeneration
- **MONDO ID:** MONDO:0013802 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Infantile Cerebellar-Retinal Degeneration** covering all of the
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

# Infantile Cerebellar-Retinal Degeneration (ICRD): A Comprehensive Disease Characterization Report

**Disease:** Infantile Cerebellar-Retinal Degeneration
**MONDO ID:** MONDO:0013802 · **OMIM:** #614559 · **Orphanet:** ORPHA:314629
**Category:** Mendelian (autosomal recessive neurometabolic disorder)
**Causal gene:** *ACO2* (mitochondrial aconitase; HGNC:118; UniProt Q99798)

---

## Summary

Infantile Cerebellar-Retinal Degeneration (ICRD) is an ultra-rare, autosomal recessive, infantile-onset neurometabolic and neurodegenerative disorder caused by **biallelic loss-of-function variants in *ACO2***, the nuclear-encoded gene for mitochondrial aconitase — the second enzyme of the tricarboxylic acid (TCA)/Krebs cycle, which interconverts citrate and isocitrate via a catalytic [4Fe-4S] iron–sulfur cluster. Disease was first defined in 2012 by homozygosity mapping and whole-exome sequencing in two families sharing a homozygous p.Ser112Arg (c.336C>G) founder mutation, with severely reduced aconitase activity in patient lymphoblasts and failure of the mutant human enzyme to rescue a yeast aconitase-null strain ([PMID: 22405087](https://pubmed.ncbi.nlm.nih.gov/22405087/)).

Clinically, ICRD presents in early infancy (typically 2–6 months) with severe truncal hypotonia, truncal ataxia, evolving microcephaly, variable seizures, and progressive ophthalmologic disease — esotropia and optic atrophy followed by retinal dystrophy. Brain MRI is usually normal in the first months but develops progressive global atrophy that is predominantly cerebellar. Most patients remain nonambulatory and nonverbal, though the phenotype is a genuine spectrum: at the severe end, infantile death; at the mild end, **isolated optic atrophy 9 (OPA9)** with preserved cognition and normal lifespan. This allelic-series relationship (severe ICRD ↔ mild OPA9) is a defining feature of *ACO2* disease.

Mechanistically, aconitase deficiency produces a coherent causal chain: (1) mutation damages the catalytic [4Fe-4S] cluster or substrate-binding residues → (2) loss of citrate→isocitrate conversion → (3) TCA-cycle/bioenergetic failure with secondary mitochondrial DNA depletion and deficient respiration → (4) toxic citrate accumulation that activates the integrated stress response (ISR) → (5) caspase-3–mediated apoptosis and reduced histone-acetylation–driven autophagy suppression → (6) preferential death of high-energy-demand neurons (cerebellar, retinal, optic) → (7) the clinical phenotype. Management is currently supportive; anaplerotic **triheptanoin** (an odd-chain C7 triglyceride that refills TCA intermediates downstream of the aconitase block) has been trialed in two brothers as a rational but still-unproven disease-directed therapy.

---

## Section 1 — Disease Information

**Overview.** ICRD is a Mendelian mitochondrial-adjacent (nuclear gene, mitochondrial enzyme) neurodegenerative disease of infancy defined by the triad of progressive cerebellar degeneration, retinal/optic degeneration, and global developmental delay/regression. It is a distinct clinical entity within the broader group of *ACO2*-related disorders.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0013802 |
| OMIM | #614559 (Infantile cerebellar-retinal degeneration) |
| Orphanet | ORPHA:314629 |
| Gene (HGNC) | *ACO2*, HGNC:118 |
| Gene OMIM | *100850* |
| UniProt (protein) | Q99798 (Aconitate hydratase, mitochondrial) |
| Ensembl | ENSG00000100412 |

**Synonyms / alternative names.** ICRD; *ACO2*-related infantile cerebellar-retinal degeneration; mitochondrial aconitase deficiency; aconitase 2 (ACO2) deficiency. The allelic milder disorder is **Optic Atrophy 9 (OPA9)**.

**Source of information.** The knowledge base entry is derived from **aggregated disease-level resources** (OMIM, Orphanet) and from **individual-patient primary literature** — small case series and cohorts (the largest being 16 patients, [PMID: 30689204](https://pubmed.ncbi.nlm.nih.gov/30689204/)) and single case reports. No EHR-scale population data exist given disease rarity.

---

## Section 2 — Etiology

**Primary cause (genetic).** ICRD is caused exclusively by **biallelic (homozygous or compound heterozygous) pathogenic variants in *ACO2***. There is no environmental or infectious etiology. The founding study established causality through homozygosity mapping plus WES, biochemical demonstration of severely reduced aconitase activity, and a yeast complementation assay in which mutant human ACO2 failed to rescue an *ACO1*-deletion strain ([PMID: 22405087](https://pubmed.ncbi.nlm.nih.gov/22405087/)). A 16-patient multicenter cohort confirmed biallelic pathogenic *ACO2* variants as the recurrent cause ([PMID: 30689204](https://pubmed.ncbi.nlm.nih.gov/30689204/)).

**Genetic risk factors.** The causal variants themselves are the risk factor. A recurrent **founder allele c.336C>G (p.Ser112Arg)** appeared in 10 of 16 patients in the largest cohort ([PMID: 30689204](https://pubmed.ncbi.nlm.nih.gov/30689204/)). *ACO2* is highly constrained against variation in gnomAD (pLI 0.97; missense-Z 4.58; LoF-Z 4.94), consistent with an essential gene whose complete loss is not tolerated (Finding F004).

**Environmental / protective factors, gene–environment interactions.** None established. As a fully penetrant Mendelian recessive disorder, there are no recognized environmental risk factors, protective alleles, or GxE interactions. Consanguinity elevates recurrence risk of the recessive genotype but is not a disease cause per se.

---

## Section 3 — Phenotypes

Phenotypes are drawn chiefly from the 16-patient cohort ([PMID: 30689204](https://pubmed.ncbi.nlm.nih.gov/30689204/)) and the founding cohort ([PMID: 22405087](https://pubmed.ncbi.nlm.nih.gov/22405087/)). Onset is neonatal-to-early-infantile; course is **progressive**.

| Phenotype | Type | HPO term | Onset / severity / frequency |
|---|---|---|---|
| Truncal hypotonia | Clinical sign | HP:0008936 | Early infancy; severe; most patients |
| Truncal ataxia | Clinical sign | HP:0002078 | Infancy; severe; most patients |
| Optic atrophy | Physical/ophthalmologic | HP:0000648 | Infancy→childhood; dominant feature |
| Esotropia | Clinical sign | HP:0000565 | Infancy; most dominant ocular sign |
| Retinal dystrophy/degeneration | Physical | HP:0000556 | Later than optic atrophy; progressive |
| Seizures | Clinical sign | HP:0001250 | Variable; subset of patients |
| Microcephaly (evolving/acquired) | Physical | HP:0000252 / HP:0005484 | Postnatal, progressive |
| Global developmental delay | Behavioral/cognitive | HP:0001263 | Infancy; severe; most patients |
| Intellectual disability | Cognitive | HP:0001249 | Severe–profound (variable) |
| Cerebellar atrophy | Imaging | HP:0001272 | Develops after normal early MRI |
| Cerebral (cortical) atrophy | Imaging | HP:0002059 | Progressive |
| Absent speech/language | Behavioral | HP:0001344 | Most remain nonverbal |
| Peripheral neuropathy | Clinical sign | HP:0009830 | Reported in longer-surviving cases (PMID 28545339) |
| Pigmentary retinopathy | Physical | HP:0000580 | Reported in moderate/older cases |

**Characteristics summary (F008):** Most patients present in early infancy with "severe truncal hypotonia, truncal ataxia, variable seizures, evolving microcephaly, and ophthalmological abnormalities of which the most dominant are esotropia and optic atrophy with later development of retinal dystrophy" ([PMID: 30689204](https://pubmed.ncbi.nlm.nih.gov/30689204/)). "Brain magnetic resonance imaging (MRI) is typically normal within the first months but global atrophy gradually develops affecting predominantly the cerebellum" (same source). The founding study documented onset at 2–6 months with survival up to 18 years ([PMID: 22405087](https://pubmed.ncbi.nlm.nih.gov/22405087/)).

**Severity spectrum.** Severe (infantile death) → moderate (increased survival with partly preserved cognition; a patient able to "speak full sentences and follow commands," [PMID: 28545339](https://pubmed.ncbi.nlm.nih.gov/28545339/)) → mild isolated optic atrophy (OPA9).

**Quality-of-life impact.** Profound in classic ICRD: most patients are nonambulatory, nonverbal, visually impaired, and fully dependent for daily activities, with high caregiver burden. No formal EQ-5D/SF-36 instruments have been applied given rarity.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *ACO2* (aconitase 2, mitochondrial), HGNC:118, chr22q13.2 (GRCh38 chr22:41,447,830–41,529,273), Ensembl ENSG00000100412, protein UniProt Q99798 (780 aa).

**Representative pathogenic variants.**

| Variant (protein) | cDNA | Type | Significance | Note / PMID |
|---|---|---|---|---|
| p.Ser112Arg | c.336C>G | Missense (founder) | Pathogenic | First ICRD variant; 10/16 cohort; [22405087](https://pubmed.ncbi.nlm.nih.gov/22405087/), [30689204](https://pubmed.ncbi.nlm.nih.gov/30689204/) |
| p.Cys448Ser | — | Missense | Pathogenic | Removes [4Fe-4S] cluster ligand; [32713659](https://pubmed.ncbi.nlm.nih.gov/32713659/) |
| p.Met393Ile | — | Missense | Likely pathogenic | Adjacent to Cys385 cluster ligand; [32713659](https://pubmed.ncbi.nlm.nih.gov/32713659/) |

**Variant classification & type.** Variants are predominantly **missense**, classified pathogenic/likely-pathogenic by ACMG/AMP criteria supported by functional enzyme assays. Nonsense/frameshift alleles also occur. Given strong LoF constraint (gnomAD LoF-Z 4.94, pLI 0.97), complete biallelic null genotypes may be embryonic-lethal, which is consistent with the missense-heavy spectrum observed in survivors.

**Allele frequency.** Pathogenic alleles are ultra-rare in gnomAD; overall *ACO2* is strongly depleted of both missense and LoF variation (Finding F004).

**Origin & functional consequence.** All disease alleles are **germline**; there is no somatic/cancer role. The molecular consequence is **loss of function** — reduced aconitase catalytic activity (patient fibroblasts <20% of control; [PMID: 26992325](https://pubmed.ncbi.nlm.nih.gov/26992325/)), reduced cellular respiration, and secondary mitochondrial DNA depletion, all rescued by reintroducing wild-type *ACO2* (same study).

**Structural basis (F005).** UniProt Q99798 annotates an N-terminal mitochondrial transit peptide (aa 1–27), substrate-binding residues (99, 192–194, 474, 479, 607, 670–671), and three **[4Fe-4S] cluster-coordinating cysteines at 385, 448, 451**. p.Cys448Ser eliminates one cluster ligand; p.Met393Ile sits immediately adjacent to Cys385 — providing a direct structural explanation for enzyme failure.

**Modifier genes / epigenetics / chromosomal abnormalities.** No specific modifier genes are established; residual aconitase activity (allele-dependent) is the principal severity determinant. Notably, **LONP1** protease regulates ACO2 turnover/stability ([PMID: 42302976](https://pubmed.ncbi.nlm.nih.gov/42302976/)), a plausible modifier axis. Downstream epigenetic dysregulation (histone acetylation) is a consequence, not a cause (see Section 6). No recurrent large chromosomal abnormalities are associated with ICRD.

---

## Section 5 — Environmental Information

Not applicable. ICRD is a monogenic recessive disorder with **no environmental, lifestyle, toxic, or infectious contributors**. General mitochondrial stressors (oxidative stress, aminoglycoside-class mitochondrial toxins) are theoretical aggravators of any bioenergetic disorder but have no disease-specific evidence in ICRD. Aconitase is intrinsically redox-sensitive (its [4Fe-4S] cluster is inactivated by superoxide, H₂O₂, NO, ONOO⁻; [PMID: 9171919](https://pubmed.ncbi.nlm.nih.gov/9171919/), [PMID: 24266943](https://pubmed.ncbi.nlm.nih.gov/24266943/)), so oxidative burden could in principle worsen residual enzyme activity, but this is inferred, not demonstrated in patients.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic *ACO2* mutation** damages a substrate-binding residue or a [4Fe-4S] cluster-coordinating cysteine (e.g., Cys448Ser) → **leads to** loss/instability of the catalytic iron–sulfur cluster. *(Demonstrated: enzyme activity <20% of control; F003, F005.)*
2. Cluster/enzyme failure → **results in** inability to convert **citrate → cis-aconitate → isocitrate** in the TCA cycle. *(Demonstrated: altered plasma cis-aconitate, isocitrate, α-ketoglutarate; F003.)*
3. TCA-cycle block → **leads to** impaired NADH/FADH₂ supply and **bioenergetic (ATP) failure**, with **deficient cellular respiration** and **secondary mitochondrial DNA depletion**. *(Demonstrated in fibroblasts; F003, [PMID: 26992325](https://pubmed.ncbi.nlm.nih.gov/26992325/).)*
4. Branch A — **Citrate accumulation** (failure of citrate clearance) → **activates the integrated stress response (ISR)** and impairs cell fitness; reversible by blocking citrate production or promoting citrate efflux. *(Demonstrated in cells and kidney in vivo; F007, [PMID: 41763199](https://pubmed.ncbi.nlm.nih.gov/41763199/).)*
5. Branch B — Energy/metabolic stress → **reduced histone acetylation (H3K9, H4K5)** → **downregulation of autophagy genes LC3/Atg5** → impaired autophagic clearance. *(Demonstrated in ACO2-deficient PD model; F007, [PMID: 38007539](https://pubmed.ncbi.nlm.nih.gov/38007539/).)*
6. ISR + energy failure + defective autophagy → **caspase-3–mediated apoptosis** of vulnerable cells. *(Demonstrated: Active Caspase-3 up, muscle Aco2-KO; F007, [PMID: 41331265](https://pubmed.ncbi.nlm.nih.gov/41331265/).)*
7. Preferential loss of **high-energy-demand, post-mitotic neurons** — cerebellar (Purkinje/granule) neurons, retinal photoreceptors/ganglion cells, optic nerve axons → **results in** progressive cerebellar atrophy, retinal degeneration, optic atrophy, hypotonia, ataxia, seizures, and developmental regression (the ICRD phenotype). *(Clinical–imaging correlation; F008.)*

```
ACO2 mutation ([4Fe-4S] ligand loss)
        │
        ▼
 Aconitase activity ↓↓ (<20%)
        │
        ▼
 Citrate ⇢ isocitrate block  ──► TCA metabolite shift (cis-aconitate↑, isocitrate/α-KG altered)
        │                                   │
        ▼                                   ▼
 Respiration ↓, ATP ↓                 Citrate accumulation
 mtDNA depletion                            │
        │                                   ▼
        │                          Integrated Stress Response (ISR)
        │                                   │
        ├──────────────┬────────────────────┤
        ▼              ▼                     ▼
 Histone acetyl↓   Autophagy↓           Caspase-3 apoptosis
 (H3K9/H4K5)       (LC3/Atg5↓)
        └──────────────┴────────────────────┘
                        │
                        ▼
   Death of high-energy neurons (cerebellum, retina, optic nerve)
                        │
                        ▼
   Progressive cerebellar/retinal degeneration → ICRD phenotype
```

**Molecular pathways.** TCA/Krebs cycle (KEGG hsa00020), oxidative phosphorylation, iron–sulfur cluster biogenesis, integrated stress response. **Cellular processes (GO):** TCA cycle (GO:0006099), aconitate hydratase activity (GO:0003994), 4Fe-4S cluster binding (GO:0051539), generation of precursor metabolites and energy (GO:0006091), autophagy (GO:0006914), apoptotic process (GO:0006915), response to oxidative stress (GO:0006979). **Protein dysfunction:** loss-of-function via cluster destabilization/misassembly. **Metabolic changes:** TCA intermediate flux disruption (diagnostic plasma fingerprint — cis-aconitate, isocitrate, α-KG, phosphoenolpyruvate, hydroxybutyrate; [PMID: 28463998](https://pubmed.ncbi.nlm.nih.gov/28463998/)); elevated glutamate reported ([PMID: 32713659](https://pubmed.ncbi.nlm.nih.gov/32713659/)). **Tissue damage:** oxidative-stress-sensitive enzyme, bioenergetic starvation, apoptosis. **Immune involvement:** none primary (mtDNA release can secondarily engage cGAS-STING inflammation via LONP1 axis — inferred, [PMID: 42302976](https://pubmed.ncbi.nlm.nih.gov/42302976/)).

**Subcellular localization (GO Cellular Component):** mitochondrion (GO:0005739), mitochondrial matrix (GO:0005759). **Cell types (CL):** cerebellar Purkinje cell (CL:0000121), cerebellar granule cell (CL:0001031), retinal photoreceptor (CL:0000210), retinal ganglion cell (CL:0000740). **Anatomy (UBERON):** cerebellum (UBERON:0002037), retina (UBERON:0000966), optic nerve (UBERON:0000941).

**Comparison to related disease.** In Friedreich ataxia, frataxin loss secondarily impairs Fe-S enzymes including aconitase, producing mitochondrial iron accumulation and Fe-S enzyme deficiency ([PMID: 9326946](https://pubmed.ncbi.nlm.nih.gov/9326946/)) — a mechanistic cousin (Fe-S/aconitase failure) reached by a different primary lesion.

---

## Section 7 — Anatomical Structures Affected

- **Primary organs/systems:** central nervous system (nervous system) — **cerebellum** (predominant), cerebral cortex, optic nerve, and **retina/eye**.
- **Secondary involvement:** peripheral nerves (neuropathy in longer survivors), skeletal muscle (hypotonia; muscle maturation depends on ACO2 in models).
- **Tissue level:** nervous tissue (neurons and their axons), retinal neuroepithelium.
- **Cell populations (CL):** cerebellar Purkinje cells (CL:0000121), granule cells (CL:0001031), retinal photoreceptors (CL:0000210), retinal ganglion cells (CL:0000740), optic nerve axons.
- **Subcellular (GO CC):** mitochondrion (GO:0005739), mitochondrial matrix (GO:0005759).
- **Localization / lateralization:** **bilateral, symmetric** CNS atrophy; bilateral optic atrophy and retinal degeneration. UBERON: cerebellum UBERON:0002037, retina UBERON:0000966, optic nerve UBERON:0000941, cerebral cortex UBERON:0000956.

---

## Section 8 — Temporal Development

- **Onset:** congenital-to-early-infantile; typical symptomatic onset **2–6 months** of age ([PMID: 22405087](https://pubmed.ncbi.nlm.nih.gov/22405087/)); pattern insidious then progressive.
- **Progression:** **progressive neurodegeneration**. MRI is characteristically **normal in the first months**, then develops **progressive global atrophy, predominantly cerebellar** ([PMID: 30689204](https://pubmed.ncbi.nlm.nih.gov/30689204/)). Rate is variable and genotype-dependent.
- **Course:** chronic, lifelong, non-remitting. Severe end → death in infancy; moderate → survival into teens (up to 18 years documented) with preserved-but-limited function; mild (OPA9) → normal lifespan.
- **Critical period:** the early-infantile window before irreversible cerebellar/retinal cell loss is the theoretical target for any future disease-modifying (e.g., anaplerotic or gene) therapy.

---

## Section 9 — Inheritance and Population

- **Inheritance:** **autosomal recessive** (biallelic *ACO2*). The allelic dominant disorder (isolated optic atrophy) exists separately ([PMID: 34056600](https://pubmed.ncbi.nlm.nih.gov/34056600/)).
- **Penetrance:** effectively **complete** for biallelic pathogenic genotypes.
- **Expressivity:** **highly variable** — an allelic series from OPA9 (mild) to lethal infantile ICRD, largely reflecting residual enzyme activity.
- **Founder effect:** yes — c.336C>G (p.Ser112Arg) recurrent (10/16 cohort; [PMID: 30689204](https://pubmed.ncbi.nlm.nih.gov/30689204/)).
- **Consanguinity:** contributes (homozygous founder cases identified by homozygosity mapping).
- **Anticipation / germline mosaicism:** not reported / not applicable.
- **Epidemiology:** **ultra-rare**; fewer than ~40 patients/families reported worldwide (initial reports noted only ~6 families/5 unique mutations; [PMID: 28545339](https://pubmed.ncbi.nlm.nih.gov/28545339/)). No reliable prevalence/incidence estimates; Orphanet lists it as <1/1,000,000.
- **Sex ratio / demographics:** no strong sex bias (autosomal recessive); reported across multiple ethnicities (Middle Eastern founder families, Chinese, European cases).

---

## Section 10 — Diagnostics

**Genetic testing (definitive).** Diagnosis rests on identifying **biallelic pathogenic *ACO2* variants** by **whole-exome (WES)** or **whole-genome sequencing (WGS)**, or a mitochondrial/cerebellar-ataxia/retinal-dystrophy **gene panel** that includes *ACO2*; targeted testing for the founder c.336C>G in relevant populations. Sanger confirmation and parental segregation establish compound heterozygosity ([PMID: 32713659](https://pubmed.ncbi.nlm.nih.gov/32713659/), [PMID: 22405087](https://pubmed.ncbi.nlm.nih.gov/22405087/)).

**Biochemical / functional tests.** Reduced **aconitase enzyme activity** in lymphoblasts/fibroblasts (<20% control) supports pathogenicity; **mtDNA copy number** (depletion) and cellular respiration assays are confirmatory research tools ([PMID: 26992325](https://pubmed.ncbi.nlm.nih.gov/26992325/)).

**Metabolomic biomarker.** A **plasma metabolomic fingerprint** — altered cis-aconitate, isocitrate, α-ketoglutarate, phosphoenolpyruvate, and hydroxybutyrate — serves as a diagnostic signature ([PMID: 28463998](https://pubmed.ncbi.nlm.nih.gov/28463998/)).

**Imaging.** Brain **MRI** — serial imaging shows evolving global atrophy predominantly cerebellar; optic nerve atrophy ([PMID: 30689204](https://pubmed.ncbi.nlm.nih.gov/30689204/)). **Ophthalmologic workup** — fundoscopy (optic atrophy, pigmentary retinopathy), visual electrophysiology (ERG/VEP) demonstrating optic atrophy and retinal dysfunction ([PMID: 40210596](https://pubmed.ncbi.nlm.nih.gov/40210596/)).

**Differential diagnosis.** Other infantile cerebellar-atrophy-plus-retinopathy syndromes: neuronal ceroid lipofuscinoses (CLN6, MFSD8/CLN7; [PMID: 39108195](https://pubmed.ncbi.nlm.nih.gov/39108195/)), spinocerebellar ataxia type 7 (ATXN7 repeat; [PMID: 37283503](https://pubmed.ncbi.nlm.nih.gov/37283503/)), Norrie disease ([PMID: 39965923](https://pubmed.ncbi.nlm.nih.gov/39965923/)), Friedreich ataxia, other mitochondrial/Fe-S disorders, and PKAN. *ACO2* sequencing plus the TCA metabolite fingerprint distinguishes ICRD.

**Screening.** Carrier/cascade testing in founder-carrying families; prenatal/preimplantation testing where the familial variants are known. Not part of standard newborn-screening panels.

---

## Section 11 — Outcome / Prognosis

- **Survival:** highly variable by genotype. Severe cases → death in infancy/early childhood; classic cases survive into childhood/teens (up to 18 years reported; [PMID: 22405087](https://pubmed.ncbi.nlm.nih.gov/22405087/), [PMID: 28545339](https://pubmed.ncbi.nlm.nih.gov/28545339/)); OPA9 → normal lifespan.
- **Morbidity / function:** severe in classic ICRD — most patients are nonambulatory, nonverbal, cortically/optically visually impaired, with intractable epilepsy in a subset and profound intellectual disability; fully care-dependent.
- **Complications:** seizures, aspiration/feeding difficulty from hypotonia, contractures, vision loss, and secondary infections typical of severe neurodisability.
- **Recovery potential:** none — the disease is progressive and neurodegenerative; supportive care is stabilizing at best.
- **Prognostic factors:** **residual aconitase activity/genotype** is the dominant determinant (missense with partial function → longer survival and partial cognition, e.g., [PMID: 28545339](https://pubmed.ncbi.nlm.nih.gov/28545339/)); degree/rate of cerebellar atrophy on serial MRI; seizure burden.

---

## Section 12 — Treatment

**No disease-specific approved therapy exists.** Management is **supportive and multidisciplinary**: antiepileptic drugs for seizures, physical/occupational/speech therapy for hypotonia and developmental support, nutritional support (gastrostomy where needed), low-vision services and ophthalmologic management, and orthopedic care for contractures. (NCIT: supportive care NCIT:C133397; anticonvulsant therapy NCIT:C15229; physical therapy NCIT:C15304.)

**Experimental disease-directed therapy — anaplerosis.** **Triheptanoin** (an odd-chain C7 triglyceride) was administered to **two brothers with aconitase 2 deficiency** — the first reported disease-directed metabolic intervention for ACO2 deficiency ([PMID: 38668366](https://pubmed.ncbi.nlm.nih.gov/38668366/)). Rationale: triheptanoin is metabolized to propionyl-CoA → succinyl-CoA, refilling TCA-cycle intermediates **downstream of the aconitase block** (anaplerosis), theoretically bypassing the citrate→isocitrate lesion. Efficacy remains unproven pending controlled data.

**Mechanistically-motivated (preclinical/speculative) targets:** promoting mitochondrial citrate efflux or limiting citrate production (reverses ISR/fitness defects in cell/kidney models; [PMID: 41763199](https://pubmed.ncbi.nlm.nih.gov/41763199/)); the ACO2-metabolite derivative 4-octyl itaconate rescued mitochondrial dysfunction/apoptosis from ACO2 deficiency in a lung model ([PMID: 41637882](https://pubmed.ncbi.nlm.nih.gov/41637882/)); antioxidant strategies given cluster redox sensitivity (theoretical). **Gene therapy/gene replacement** is a rational future direction (WT-*ACO2* reintroduction fully rescues the cellular phenotype in vitro; [PMID: 26992325](https://pubmed.ncbi.nlm.nih.gov/26992325/)) but not yet clinical.

**Pharmacogenomics / immunotherapy / surgery:** not applicable as disease-modifying modalities.

---

## Section 13 — Prevention

- **Primary prevention:** not possible for a germline recessive disorder beyond reproductive planning.
- **Genetic counseling & reproductive options:** the mainstay — carrier testing for at-risk couples (especially consanguineous families and founder-allele populations), **prenatal diagnosis** and **preimplantation genetic testing (PGT)** when familial variants are known, and cascade testing of relatives.
- **Secondary/tertiary prevention:** early recognition (metabolite fingerprint + genetics) enables early supportive intervention, seizure control, and complication prevention (aspiration, contractures) — no intervention halts neurodegeneration.
- **Immunization / public-health / environmental measures:** not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Orthologs:** *ACO2* is deeply conserved. Mouse *Aco2* (NCBI Gene 11429); *Drosophila* ortholog *mAcon1*; yeast *ACO1* (functional complementation used to prove human causality, [PMID: 22405087](https://pubmed.ncbi.nlm.nih.gov/22405087/)). Bacterial aconitases (E. coli AcnA/AcnB) share the [4Fe-4S] cluster architecture with the mammalian mitochondrial enzyme ([PMID: 10585860](https://pubmed.ncbi.nlm.nih.gov/10585860/)).
- **Natural disease in other species:** no well-characterized spontaneous *ACO2*-deficiency disorder in companion animals/wildlife is reported (OMIA); disease knowledge is from engineered models.
- **Comparative biology:** aconitase's dual role (TCA catalysis + Fe-S/iron sensing) and its redox sensitivity are conserved from bacteria to humans ([PMID: 24266943](https://pubmed.ncbi.nlm.nih.gov/24266943/), [PMID: 17205209](https://pubmed.ncbi.nlm.nih.gov/17205209/)), making cross-species mechanistic inference robust.
- **Zoonosis:** not applicable.

---

## Section 15 — Model Organisms

| Model | Type | Key findings | PMID |
|---|---|---|---|
| Constitutive/skeletal-muscle *Aco2* knockout mouse | Mammalian, KO | Mice **die shortly after birth**; muscle fiber atrophy, disrupted sarcomeres, **increased Active Caspase-3** (apoptosis); aconitase essential for muscle maturation | [41331265](https://pubmed.ncbi.nlm.nih.gov/41331265/) |
| *ACO2* A252T knock-in mouse | Mammalian, KI | Aggravated dopaminergic neurodegeneration; downregulated autophagy (LC3, Atg5) via reduced H3K9/H4K5 histone acetylation | [38007539](https://pubmed.ncbi.nlm.nih.gov/38007539/) |
| *Drosophila* (*mAcon1*) | Invertebrate | Pan-neuronal knockdown/overexpression reduces longevity, locomotion, activity; disrupts sleep/circadian rhythm; eye mis-expression → impaired visual synaptic transmission and neurodegeneration — mirrors human ICRD | [40210596](https://pubmed.ncbi.nlm.nih.gov/40210596/) |
| Patient fibroblasts | In vitro (cellular) | Aconitase activity <20%, deficient respiration, mtDNA depletion; **fully rescued by WT-*ACO2* reintroduction** | [26992325](https://pubmed.ncbi.nlm.nih.gov/26992325/) |
| Yeast (*ACO1*Δ) complementation | Cellular | Mutant human ACO2 fails to rescue aconitase-null yeast — proves loss of function | [22405087](https://pubmed.ncbi.nlm.nih.gov/22405087/) |

**Phenotype recapitulation:** the *Drosophila* model recapitulates neuronal dysfunction, visual/retinal degeneration, and locomotor decline; the knock-in mouse recapitulates the metabolism→epigenetics→autophagy→neurodegeneration axis. **Limitations:** constitutive KO is lethal (limiting adult CNS study without conditional alleles), and no model perfectly reproduces the full human cerebellar-retinal-cognitive triad.

---

## Key Findings (with statistical evidence)

**F001 — ICRD is caused by biallelic *ACO2* variants.** Homozygosity mapping + WES in 8 individuals from 2 families identified homozygous p.Ser112Arg (c.336C>G); patient lymphoblast aconitase activity was severely reduced, and mutant human ACO2 failed to complement a yeast *ACO1* deletion. *"Homozygosity mapping followed by whole-exome sequencing disclosed a Ser112Arg mutation in ACO2, encoding mitochondrial aconitase… Specific aconitase activity in the individuals' lymphoblasts was severely reduced"* ([PMID: 22405087](https://pubmed.ncbi.nlm.nih.gov/22405087/)). A 16-patient cohort confirmed biallelic pathogenic variants ([PMID: 30689204](https://pubmed.ncbi.nlm.nih.gov/30689204/)).

**F002 — Phenotypic spectrum from OPA9 to severe ICRD.** *"Biallelic variants in ACO2 are purported to cause two distinct disorders: infantile cerebellar-retinal degeneration (ICRD)… and optic atrophy 9 (OPA9), characterized by isolated ophthalmologic phenotypes"* ([PMID: 32449285](https://pubmed.ncbi.nlm.nih.gov/32449285/)). Dominant *ACO2* variants also cause isolated optic atrophy ([PMID: 34056600](https://pubmed.ncbi.nlm.nih.gov/34056600/)).

**F003 — Metabolomic fingerprint and cellular energy defects.** *"…metabolites with affected plasma concentrations including the tricarboxylic acid cycle metabolites cis-aconitate, isocitrate and alpha-ketoglutarate, as well as phosphoenolpyruvate and hydroxybutyrate"* ([PMID: 28463998](https://pubmed.ncbi.nlm.nih.gov/28463998/)). *"ACO2 enzyme activity was <20% of that observed in control cells… deficiency in cellular respiration and, for the first time,… mitochondrial DNA depletion"* — rescued by gene reintroduction ([PMID: 26992325](https://pubmed.ncbi.nlm.nih.gov/26992325/)).

**F004 — Strong gnomAD constraint.** *ACO2* (ENSG00000100412): pLI 0.97, LOEUF 0.495 (o/e LoF 0.367), missense-Z 4.58, LoF-Z 4.94 — an essential, constraint-heavy gene, consistent with recessive ICRD and dominant optic-atrophy mechanisms.

**F005 — Variants strike catalytic Fe-S residues.** UniProt Q99798 annotates [4Fe-4S] ligands Cys385/448/451; p.Cys448Ser removes a ligand and p.Met393Ile lies adjacent to Cys385 ([PMID: 32713659](https://pubmed.ncbi.nlm.nih.gov/32713659/)).

**F006 — Triheptanoin anaplerotic therapy trialed.** First disease-directed metabolic intervention: *"Anaplerotic Therapy Using Triheptanoin in Two Brothers Suffering from Aconitase 2 Deficiency"* ([PMID: 38668366](https://pubmed.ncbi.nlm.nih.gov/38668366/)).

**F007 — Citrate accumulation → ISR → apoptosis; KO lethal.** *"Disrupting citrate catabolism activates the integrated stress response and impairs cell fitness… reversed by preventing citrate production or promoting mitochondrial citrate efflux. In vivo, ACO2 deficiency induces citrate accumulation and triggers tubular degeneration in the kidney"* ([PMID: 41763199](https://pubmed.ncbi.nlm.nih.gov/41763199/)). Muscle *Aco2*-KO mice *"died shortly after birth"* with caspase-3 apoptosis ([PMID: 41331265](https://pubmed.ncbi.nlm.nih.gov/41331265/)). *"…autophagy-related genes LC3 and Atg5 was significantly downregulated via inhibited histone acetylation at the H3K9 and H4K5 sites"* ([PMID: 38007539](https://pubmed.ncbi.nlm.nih.gov/38007539/)).

**F008 — Characteristic clinical/MRI course.** *"Most patients present in early infancy with severe truncal hypotonia, truncal ataxia, variable seizures, evolving microcephaly, and ophthalmological abnormalities of which the most dominant are esotropia and optic atrophy with later development of retinal dystrophy"* and *"Brain MRI is typically normal within the first months but global atrophy gradually develops affecting predominantly the cerebellum"* ([PMID: 30689204](https://pubmed.ncbi.nlm.nih.gov/30689204/)).

---

## Mechanistic Model / Interpretation

ICRD is best understood as a **primary bioenergetic + citrate-toxicity disorder** of neurons. The single enzymatic lesion (aconitase failure) produces two converging insults: (i) an **energy-supply deficit** (TCA flux ↓, respiration ↓, mtDNA depletion), and (ii) a **toxic-substrate accumulation** (citrate build-up) that actively triggers the integrated stress response, apoptosis, and epigenetically-mediated autophagy suppression. These converge on the death of post-mitotic, high-energy-demand cells — cerebellar neurons, retinal photoreceptors and ganglion cells, and optic nerve axons — explaining the disease's signature cerebellar-retinal predilection. The **allelic series** (OPA9 ↔ ICRD) is naturally explained by a residual-activity model: variants with partial function spare the CNS and manifest only in the exquisitely oxidative-metabolism-dependent optic system, while near-null biallelic genotypes produce lethal multisystem disease. The finding that citrate efflux, blocking citrate production, or 4-octyl itaconate can reverse cellular phenotypes, and that WT-*ACO2* fully rescues fibroblasts, identifies **actionable, druggable nodes downstream of the mutation**.

---

## Evidence Base

| PMID | Contribution | Source type |
|---|---|---|
| [22405087](https://pubmed.ncbi.nlm.nih.gov/22405087/) | Establishes *ACO2* causality; founder variant; yeast complementation | Human + in vitro |
| [30689204](https://pubmed.ncbi.nlm.nih.gov/30689204/) | Largest cohort (n=16); clinical/MRI delineation; founder frequency | Human clinical |
| [32449285](https://pubmed.ncbi.nlm.nih.gov/32449285/) | ICRD↔OPA9 spectrum | Human clinical |
| [34056600](https://pubmed.ncbi.nlm.nih.gov/34056600/) | Dominant *ACO2* optic atrophy | Human clinical |
| [26992325](https://pubmed.ncbi.nlm.nih.gov/26992325/) | Enzyme <20%, respiration defect, mtDNA depletion, gene rescue | In vitro |
| [28463998](https://pubmed.ncbi.nlm.nih.gov/28463998/) | Plasma metabolomic diagnostic fingerprint | Human biomarker |
| [32713659](https://pubmed.ncbi.nlm.nih.gov/32713659/) | Cys448Ser / Met393Ile — Fe-S cluster structural basis | Human + structural |
| [28545339](https://pubmed.ncbi.nlm.nih.gov/28545339/) | Moderate phenotype, preserved cognition, longer survival | Human clinical |
| [41763199](https://pubmed.ncbi.nlm.nih.gov/41763199/) | Citrate clearance → ISR → cell fitness (2026) | In vitro + mouse |
| [41331265](https://pubmed.ncbi.nlm.nih.gov/41331265/) | *Aco2* KO lethal; caspase-3 apoptosis (2025) | Mouse |
| [38007539](https://pubmed.ncbi.nlm.nih.gov/38007539/) | Metabolism→histone-acetylation→autophagy axis | Mouse + fly |
| [40210596](https://pubmed.ncbi.nlm.nih.gov/40210596/) | *Drosophila* ICRD model recapitulating neuro/visual phenotypes | Invertebrate |
| [38668366](https://pubmed.ncbi.nlm.nih.gov/38668366/) | Triheptanoin anaplerotic therapy | Human (n=2) |
| [9326946](https://pubmed.ncbi.nlm.nih.gov/9326946/) | Aconitase/Fe-S deficiency in Friedreich ataxia (comparator) | Human |

---

## Limitations and Knowledge Gaps

- **Ultra-rarity:** Total reported patients number in the low dozens; no prevalence/incidence, no natural-history registry, no formal QoL data.
- **Genotype–phenotype correlations** are inferred from small cohorts; the residual-activity model is plausible but not quantitatively validated across the allelic series.
- **No CNS-specific animal model** fully recapitulates the human cerebellar-retinal-cognitive triad; constitutive KO lethality limits adult neuro-study without conditional alleles.
- **Therapeutics unproven:** triheptanoin evidence is anecdotal (n=2, no controls); downstream targets (citrate efflux, 4-OI, antioxidants) are preclinical only; no gene therapy in trials.
- **Mechanistic branches** (ISR, epigenetic-autophagy, apoptosis) are largely demonstrated in non-neuronal or non-human systems and inferred for the patient CNS.
- Some causal steps (oxidative-stress aggravation, immune/cGAS-STING involvement) remain **inferred, not demonstrated**, in ICRD patients.

---

## Proposed Follow-up Experiments / Actions

1. **Patient-derived iPSC cerebellar and retinal organoids** carrying defined *ACO2* alleles to directly test the citrate-toxicity/ISR/apoptosis chain in the affected human cell types and to correlate residual enzyme activity with degeneration rate.
2. **Conditional (neuron- and photoreceptor-specific) *Aco2* knockout / knock-in mice** to bypass embryonic lethality and model CNS/retinal disease longitudinally.
3. **Controlled anaplerosis trial:** formal evaluation of triheptanoin (and comparison with citrate-efflux promotion or 4-octyl itaconate) using the plasma TCA-metabolite fingerprint as a pharmacodynamic biomarker.
4. **AAV-mediated *ACO2* gene replacement** proof-of-concept in models, leveraging the demonstrated full cellular rescue by WT-*ACO2*.
5. **Prospective natural-history study and registry** with standardized serial MRI (cerebellar volumetrics), ERG/VEP, and developmental metrics to define progression and trial endpoints.
6. **Structure-guided variant classification:** map all reported variants onto the aconitase [4Fe-4S] and substrate-binding architecture (Q99798) and correlate predicted structural impact with clinical severity to formalize the residual-activity model.

---

*Report compiled from 8 confirmed findings and 32 reviewed papers across 5 investigation iterations. Evidence types are distinguished as human clinical, model organism, in vitro/cellular, and computational/structural throughout.*


## Artifacts

- [OpenScientist final report](Infantile_Cerebellar-Retinal_Degeneration-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Infantile_Cerebellar-Retinal_Degeneration-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 23 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013802` (2 mentions) - the report calls it "MONDO"; MONDO calls it **infantile cerebellar-retinal degeneration**
- `HP:0008936` (1 mention) - the report calls it "Clinical sign"; HP calls it **Axial hypotonia**
- `HP:0002078` (1 mention) - the report calls it "Clinical sign"; HP calls it **Truncal ataxia**
- `HP:0000648` (1 mention) - the report calls it "Physical/ophthalmologic"; HP calls it **Optic atrophy**
- `HP:0000565` (1 mention) - the report calls it "Clinical sign"; HP calls it **Esotropia**
- `HP:0000556` (1 mention) - the report calls it "Physical"; HP calls it **Retinal dystrophy**
- `HP:0001250` (1 mention) - the report calls it "Clinical sign"; HP calls it **Seizure**
- `HP:0001249` (1 mention) - the report calls it "Cognitive"; HP calls it **Intellectual disability**
- `HP:0001272` (1 mention) - the report calls it "Imaging"; HP calls it **Cerebellar atrophy**
- `HP:0002059` (1 mention) - the report calls it "Imaging"; HP calls it **Cerebral atrophy**
- `HP:0001344` (1 mention) - the report calls it "Behavioral"; HP calls it **Absent speech**
- `HP:0009830` (1 mention) - the report calls it "Clinical sign"; HP calls it **Peripheral neuropathy**
- `HP:0000580` (1 mention) - the report calls it "Physical"; HP calls it **Pigmentary retinopathy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001263` (1 mention) - the report calls it "Behavioral/cognitive"; HP calls it **Global developmental delay**, and lists "Cognitive delay" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.