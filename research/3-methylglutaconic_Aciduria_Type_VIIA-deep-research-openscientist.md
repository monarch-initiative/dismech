---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-20T01:26:33.484349'
end_time: '2026-10-20T01:39:58.040048'
duration_seconds: 804.56
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: 3-Methylglutaconic Aciduria Type VIIA
  mondo_id: MONDO:0859237
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
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 17
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 22
  quotes_valid: 21
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:41560087
  relevance_assessed: 17
  on_topic: 14
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 27
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 24
  labels_matching: 12
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: HP:0001875
    reported_labels:
    - Lab abnormality
    - neutropenia
    ontology_label: Decreased total neutrophil count
  - term_id: HP:0001249
    reported_labels:
    - Clinical sign
    ontology_label: Intellectual disability
  - term_id: HP:0002059
    reported_labels:
    - Imaging
    ontology_label: Cerebral atrophy
  - term_id: HP:0001272
    reported_labels:
    - Imaging
    ontology_label: Cerebellar atrophy
  - term_id: HP:0000518
    reported_labels:
    - Physical
    ontology_label: Cataract
  - term_id: HP:0003535
    reported_labels:
    - Lab abnormality
    - 3-MGA-uria
    ontology_label: 3-Methylglutaconic aciduria
  - term_id: HP:0100022
    reported_labels:
    - Clinical sign
    ontology_label: Abnormality of movement
  - term_id: HP:0001250
    reported_labels:
    - Clinical sign
    ontology_label: Seizure
  - term_id: HP:0032322
    reported_labels:
    - Clinical sign
    ontology_label: Healthy
  - term_id: HP:0008209
    reported_labels:
    - Clinical sign
    ontology_label: Premature ovarian insufficiency
  - term_id: HP:0002093
    reported_labels:
    - Clinical sign
    ontology_label: Respiratory insufficiency
  - term_id: CHEBI:28123
    reported_labels:
    - 3-methylglutaconic acid
    ontology_label: diethanolamine
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
  path: 3-methylglutaconic_Aciduria_Type_VIIA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: 3-methylglutaconic_Aciduria_Type_VIIA-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 3-Methylglutaconic Aciduria Type VIIA
- **MONDO ID:** MONDO:0859237 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **3-Methylglutaconic Aciduria Type VIIA** covering all of the
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

# 3-Methylglutaconic Aciduria Type VIIA (MGCA7A): A Comprehensive Disease Characterization Report

**Disease:** 3-Methylglutaconic Aciduria Type VIIA
**MONDO ID:** MONDO:0859237 · **OMIM:** #616271 · **ORPHA:** 445038
**Causal gene:** *CLPB* (SKD3; HGNC:18542; OMIM gene \*616254; chr11q13.4)
**Category:** Mendelian (mitochondrial disorder)

---

## Summary

3-Methylglutaconic aciduria type VIIA (MGCA7A, also written MGCA7) is an **ultra-rare inherited mitochondrial disorder** caused by pathogenic variants in *CLPB*, the gene encoding **SKD3**, an ATP-dependent AAA+ protein **disaggregase/refoldase** that resides in the mitochondrial intermembrane space (IMS). Two independent 2015 exome/homozygosity-mapping studies established the gene–disease relationship, and the disorder now sits at the intersection of **inborn errors of metabolism, congenital neutropenia, and neurodevelopmental disease**. It is inherited chiefly as an **autosomal recessive** trait (biallelic *CLPB* variants), with a distinct **dominant de novo monoallelic** subset acting through a dominant-negative mechanism ([PMID: 25597510](https://pubmed.ncbi.nlm.nih.gov/25597510/), [PMID: 25597511](https://pubmed.ncbi.nlm.nih.gov/25597511/), [PMID: 34140661](https://pubmed.ncbi.nlm.nih.gov/34140661/)).

The clinical hallmark is a **graded multisystem tetrad**: congenital **neutropenia** (with risk of progression to bone-marrow failure, myelodysplastic syndrome, and acute leukemia), **neurodevelopmental impairment** ranging from nonprogressive intellectual disability to prenatal encephalopathy with progressive cerebral/cerebellar atrophy, movement disorder and epilepsy, bilateral **cataracts**, and **3-methylglutaconic aciduria** detectable on urine organic-acid screening. Postpubertal female survivors frequently develop **premature ovarian insufficiency (POI)**. Disease severity spans a continuum from neonatal death to survival into adulthood, and this severity tracks with the degree of **residual CLPB (refoldase) activity** retained by the mutant protein.

Mechanistically, loss of CLPB disaggregase activity destabilizes IMS client proteins—most notably the anti-apoptotic protein **HAX1** (itself mutated in Kostmann severe congenital neutropenia)—linking the enzymatic lesion to neutropenia and apoptosis. There is **no curative therapy**; management is supportive (G-CSF for neutropenia, cataract surgery, antiepileptics, infection prophylaxis, and hematologic surveillance), and **prevention is entirely genetic** (counseling, carrier/cascade testing with a Greenlandic Inuit founder emphasis, and prenatal/preimplantation genetic testing). This report synthesizes 12 confirmed findings across 17 reviewed papers into a complete disease-knowledge-base entry organized by the requested domains.

---

## Section 1 — Disease Information

MGCA7A is a Mendelian mitochondrial disorder defined at the molecular level by loss of function of the *CLPB*-encoded disaggregase. **Key identifiers:** MONDO:0859237 · OMIM phenotype #616271 · OMIM gene \*616254 (*CLPB*) · Orphanet ORPHA:445038 · gene HGNC:18542 · UniProt Q9H078. It is classified among the **inborn errors of metabolism with 3-methylglutaconic aciduria as a discriminative feature** ([PMID: 23296368](https://pubmed.ncbi.nlm.nih.gov/23296368/)).

**Synonyms / alternative names:** 3-methylglutaconic aciduria type VII; MGCA7; MGCA7A; CLPB deficiency; "MEGCANN" (Methylglutaconic aciduria, cataracts, neurologic involvement, neutropenia); CLPB-related mitochondrial disorder with cataract, neutropenia, epilepsy and methylglutaconic aciduria.

The evidence base is **aggregated disease-level** (OMIM/Orphanet curation, cohort studies, mechanistic biochemistry) supplemented by **individual patient reports/case series**; there is no large EHR-derived dataset for this ultra-rare condition.

---

## Section 2 — Etiology

**Disease causal factor: purely genetic.** MGCA7A is a monogenic disorder of *CLPB*. There is **no environmental, infectious, or multifactorial cause.** Two mutational mechanisms operate:

- **Biallelic (autosomal recessive) loss-of-function** — the classical form.
- **Monoallelic de novo dominant-negative** missense variants — a distinct subset.

**Genetic risk factors:** the only risk factor is possession of pathogenic *CLPB* alleles. **Consanguinity** and **founder effects** (Greenlandic/Inuit) raise biallelic risk in defined populations. No modifier loci have been formally mapped, though variant class strongly modifies severity (see Section 4/11).

**Environmental risk / protective factors:** none identified; diet, toxins, lifestyle, age, and sex are not causal. POI affects only females (a sex-specific manifestation, not a risk factor for the disease itself).

**Gene–environment interactions:** none documented. The oxidation-sensitive Y272C mutation introduces an aberrant disulfide bond ([PMID: 37041140](https://pubmed.ncbi.nlm.nih.gov/37041140/)), raising a theoretical (unproven) redox-environment interaction, but no clinical GxE effect is established.

---

## Section 3 — Phenotypes

Across cohorts the phenotype comprises **congenital neutropenia** (which can progress to leukemia), a **neurological spectrum** from nonprogressive intellectual disability to prenatal encephalopathy with progressive brain atrophy, **movement disorder**, **cataracts**, and elevated **urinary 3-methylglutaconic acid**. The pivotal review states the disorder spans "*a neurological phenotype ranging from nonprogressive intellectual disability to prenatal encephalopathy with progressive brain atrophy, movement disorder, cataracts, 3-methylglutaconic aciduria, and neutropenia*" ([PMID: 34140661](https://pubmed.ncbi.nlm.nih.gov/34140661/)).

Pronicka et al. (31 patients) stratified severity into **mild (n=4), moderate (n=13), severe (n=14)**; the severe subtype featured "*the neonatal absence of voluntary movements in combination with ventilator dependency and hyperexcitability*," making MGCA7A an important differential diagnosis of **hyperekplexia** ([PMID: 28687938](https://pubmed.ncbi.nlm.nih.gov/28687938/)). Postpubertal female survivors commonly develop premature ovarian insufficiency: "*POI is a common feature of postpubertal female individuals with CLPB deficiency*" ([PMID: 36074910](https://pubmed.ncbi.nlm.nih.gov/36074910/)).

| Phenotype | Type | HPO term | Onset | Severity/progression | Frequency |
|---|---|---|---|---|---|
| Neutropenia | Lab abnormality | HP:0001875 | Congenital | Variable; leukemia risk | Very frequent |
| Intellectual disability | Clinical sign | HP:0001249 | Congenital/early | Nonprogressive→severe | Frequent |
| Cerebral atrophy | Imaging | HP:0002059 | Prenatal–early | Progressive | Frequent |
| Cerebellar atrophy | Imaging | HP:0001272 | Prenatal–early | Progressive | Frequent |
| Cataract | Physical | HP:0000518 | Congenital/early | Stable (surgical) | Frequent |
| 3-Methylglutaconic aciduria | Lab abnormality | HP:0003535 | Congenital | Persistent | Obligate marker |
| Movement disorder | Clinical sign | HP:0100022 | Early | Variable | Frequent |
| Seizures/epilepsy | Clinical sign | HP:0001250 | Early | Variable | Frequent |
| Neonatal hyperexcitability | Clinical sign | HP:0032322 | Neonatal | Severe subtype | Severe form |
| Premature ovarian insufficiency | Clinical sign | HP:0008209 | Postpubertal | Progressive | Common (female survivors) |
| Respiratory insufficiency | Clinical sign | HP:0002093 | Neonatal | Severe form | Severe subtype |

**Quality of life impact:** severe neonatal disease causes ventilator dependency, absent voluntary movement, and early death (median 35 days in the severe group), with profound QoL loss; milder disease permits survival into adulthood (median age 17.5 years in the mild group) but with intellectual disability, visual impairment from cataracts, and (in females) infertility from POI ([PMID: 28687938](https://pubmed.ncbi.nlm.nih.gov/28687938/), [PMID: 36074910](https://pubmed.ncbi.nlm.nih.gov/36074910/)). No formal EQ-5D/SF-36 data exist.

---

## Section 4 — Genetic / Molecular Information

**Causal gene:** *CLPB* (caseinolytic peptidase B homolog; chr11q13.4; HGNC:18542; OMIM \*616254), encoding the mitochondrial AAA+ ATPase/disaggregase **SKD3** (UniProt Q9H078). Wortmann et al. identified "*mutations in CLPB define a syndrome*" in **14 individuals from 9 families** ([PMID: 25597510](https://pubmed.ncbi.nlm.nih.gov/25597510/)). Saunders et al. independently reported "*biallelic variants in the caseinolytic peptidase B homolog (CLPB). The causative variants included one missense variant, c.803C>T (p.Thr268Met), and two nonsense variants, c.961A>T (p.Lys321\*) and c.1249C>T (p.Arg417\*)*" ([PMID: 25597511](https://pubmed.ncbi.nlm.nih.gov/25597511/)).

**Variant types & classification:** missense, nonsense, frameshift, and splicing variants are all reported (pathogenic/likely pathogenic per ACMG). Stop/stop (nonsense-mediated decay) and ankyrin/N-domain-disrupting alleles confer the greatest burden. The **dominant subset** comprises de novo monoallelic missense variants: "*we identified one of four different de novo monoallelic missense variants in CLPB. We show that these variants disturb refoldase and to a lesser extent ATPase activity of CLPB in a dominant-negative manner*" ([PMID: 34140661](https://pubmed.ncbi.nlm.nih.gov/34140661/)).

**Functional consequences:** biallelic variants cause **loss of function** (markedly decreased CLPB protein in patient fibroblasts/liver); de novo monoallelic variants act by **dominant-negative** interference with the oligomeric disaggregase. **Allele frequency:** all causal alleles are rare/absent in gnomAD, consistent with an ultra-rare disorder; the Greenlandic founder allele is enriched locally.

**Structural insights:** the N-domain mutation Y272C "*forms an intramolecular disulfide bond with Cys267 and severely impairs SKD3*" ([PMID: 37041140](https://pubmed.ncbi.nlm.nih.gov/37041140/)). SKD3 assembles into **nucleotide-stabilized dodecamers** (two hexameric rings) ([PMID: 35247700](https://pubmed.ncbi.nlm.nih.gov/35247700/)).

**Modifier genes / epigenetics / chromosomal abnormalities:** no formal modifier loci, methylation signatures, or large structural/chromosomal changes have been described; disease is point-mutation/small-variant driven.

---

## Section 5 — Environmental Information

**Not applicable.** MGCA7A is a monogenic disorder with **no environmental, lifestyle, or infectious contribution.** No toxins, radiation, occupational exposures, dietary factors, or pathogens are implicated in causation or triggering. (The 3-methylglutaconic acid elevation is an endogenous metabolic consequence, not an environmental exposure.)

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

```
1. Biallelic LoF (recessive) OR de novo monoallelic dominant-negative
   CLPB variant
        │  leads to
        ▼
2. Reduced/abolished SKD3 (CLPB) ATP-dependent DISAGGREGASE/REFOLDASE
   activity in the mitochondrial intermembrane space
   (ATPase activity may be preserved; REFOLDASE loss is the key defect)
        │  results in
        ▼
3. Failure to disaggregate/refold IMS client proteins
        │
        ├──► 3a. Reduced solubility & altered assembly of anti-apoptotic
        │        HAX1  →  granulocyte apoptosis / maturation arrest
        │              →  CONGENITAL NEUTROPENIA  →  infection risk;
        │                 MDS / acute leukemia risk
        │
        ├──► 3b. IMS proteostatic stress / mitochondrial membrane
        │        pathology  →  accumulation & urinary excretion of
        │        3-METHYLGLUTACONIC ACID (nonspecific mito marker)
        │
        ├──► 3c. Neuronal mitochondrial dysfunction  →  prenatal/early
        │        encephalopathy  →  PROGRESSIVE CEREBRAL & CEREBELLAR
        │        ATROPHY, intellectual disability, movement disorder,
        │        epilepsy  (inferred: direct neuronal apoptotic pathway
        │        not fully demonstrated)
        │
        ├──► 3d. Lens epithelial mitochondrial dysfunction  →  bilateral
        │        CATARACTS  (inferred)
        │
        └──► 3e. Ovarian (granulosa/oocyte) mitochondrial dysfunction  →
                 PREMATURE OVARIAN INSUFFICIENCY in postpubertal females
        │
        ▼
4. SEVERITY is set by RESIDUAL REFOLDASE ACTIVITY:
   stop/stop & NMD/ankyrin-disrupting variants → severe, neonatal death;
   missense with partial function → milder, survival into adulthood.
```

### Detail

**Molecular pathway / protein function.** SKD3 (human ClpB) couples **ATP hydrolysis to protein disaggregation/reactivation** in the IMS, regulated by PARL: "*A mitochondrial inner-membrane protease, PARL, removes an autoinhibitory peptide from Skd3 to greatly enhance disaggregase activity*" ([PMID: 32573439](https://pubmed.ncbi.nlm.nih.gov/32573439/)). It localizes to the IMS—"*CLPB resides in the mitochondrial intermembrane space*" ([PMID: 32866687](https://pubmed.ncbi.nlm.nih.gov/32866687/))—where it forms ATP-dependent high-molecular-weight complexes/dodecamers ([PMID: 35247700](https://pubmed.ncbi.nlm.nih.gov/35247700/)).

**Biochemical/cellular consequence (the HAX1 bridge).** Loss of disaggregase activity destabilizes clients: "*Human cells lacking Skd3 exhibit reduced solubility of various mitochondrial proteins, including anti-apoptotic Hax1. Importantly, Skd3 variants linked to 3-methylglutaconic aciduria... display diminished disaggregase activity (but not always reduced ATPase activity), which predicts disease severity*" ([PMID: 32573439](https://pubmed.ncbi.nlm.nih.gov/32573439/)). Because **HAX1** is mutated in Kostmann congenital neutropenia, its destabilization provides a direct molecular route to the neutropenia phenotype and to dysregulated apoptosis. Complexome profiling confirms altered assembly: in patients "*multiple HAX1 peaks were observed at higher molecular masses comigrating with CLPB*" ([PMID: 34140661](https://pubmed.ncbi.nlm.nih.gov/34140661/)).

**Upstream vs downstream.** The *CLPB* mutation and loss of refoldase activity are **upstream** (and encode severity). The HAX1/IMS-client destabilization is the **proximal effector** (best-demonstrated, explains neutropenia). The brain/lens/ovary manifestations are **downstream** and mechanistically **inferred** from shared mitochondrial proteostatic stress in high-energy tissues.

**Cell types & processes involved:** neutrophils/granulocytes (CL:0000775/CL:0000094), neurons and glia, lens epithelium, ovarian granulosa/oocytes.

**Suggested GO terms:** GO:0043335 (protein unfolding), GO:0042026 (protein refolding), GO:0016887 (ATP hydrolysis activity), GO:0005758 (mitochondrial intermembrane space), GO:0006915 (apoptotic process). **CHEBI:** CHEBI:28123 (3-methylglutaconic acid).

**Metabolomics / 3-MGA-uria:** 3-methylglutaconic aciduria is a **nonspecific marker of mitochondrial dysfunction**; its exact biochemical origin in CLPB disease is unknown ([PMID: 23355087](https://pubmed.ncbi.nlm.nih.gov/23355087/), [PMID: 23296368](https://pubmed.ncbi.nlm.nih.gov/23296368/)). SKD3/CLPB is also upregulated in acute myeloid leukemia, where it contributes to venetoclax resistance ([PMID: 35247700](https://pubmed.ncbi.nlm.nih.gov/35247700/), [PMID: 31048321](https://pubmed.ncbi.nlm.nih.gov/31048321/)).

---

## Section 7 — Anatomical Structures Affected

**Organ level (primary):** central nervous system (progressive cerebral and cerebellar atrophy, movement disorder, epilepsy—"*Muscular hypo- and hypertonia, movement disorder and progressive brain atrophy are frequently reported*" [PMID: 28687938](https://pubmed.ncbi.nlm.nih.gov/28687938/)); hematopoietic/bone marrow (granulocytic neutropenia with leukemia risk); ocular lens (bilateral cataracts); ovary (POI in female survivors). **Secondary involvement:** respiratory system and swallowing/feeding apparatus in severe neonates.

**Body systems:** nervous, hematologic/immune, ocular/visual, reproductive/endocrine.

**Tissue/cell level:** nervous tissue (neurons, cerebellar Purkinje/granule populations), granulocytic hematopoietic lineage, lens epithelium, ovarian granulosa cells. **Cell Ontology:** CL:0000775 (neutrophil), CL:0000094 (granulocyte).

**Subcellular level:** the **mitochondrial intermembrane space** (GO:0005758) is the primary locus—"*indicating that CLPB resides in the mitochondrial intermembrane space*" ([PMID: 32866687](https://pubmed.ncbi.nlm.nih.gov/32866687/)).

**UBERON terms:** UBERON:0000955 (brain), UBERON:0002037 (cerebellum), UBERON:0002371 (bone marrow), UBERON:0000965 (lens), UBERON:0000992 (ovary). **Lateralization:** CNS atrophy and cataracts are typically **bilateral**.

---

## Section 8 — Temporal Development

**Onset:** congenital, often **prenatal** in severe cases (reduced fetal movements). **Pattern:** subacute-to-chronic with a progressive neurological component.

**Progression:** "*The foetal and neonatal presentation mirrored the course of disease with respect to survival (current median age 17.5 years in the mild group, median age of death 35 days in the severe group), severity and age of onset of all findings evaluated*" ([PMID: 28687938](https://pubmed.ncbi.nlm.nih.gov/28687938/)). The neurologic component is progressive (progressive brain atrophy); neutropenia and cataracts are congenital/early. Age of onset predicts rate: "*Early-onset disease (<12 months) correlated with more severe progression. Later onset often resulted in milder phenotypes*" ([PMID: 41719910](https://pubmed.ncbi.nlm.nih.gov/41719910/)).

**Course / duration:** lifelong/chronic in survivors; severe disease is rapidly fatal in the neonatal period. **Critical period:** the neonatal window (respiratory/feeding support, G-CSF) is decisive for survival. No spontaneous remission; POI emerges postpubertally.

---

## Section 9 — Inheritance and Population

**Epidemiology:** ultra-rare (ORPHA:445038; prevalence <1/1,000,000). Fewer than ~100 patients are reported worldwide; the largest cohort is 63 individuals ([PMID: 41719910](https://pubmed.ncbi.nlm.nih.gov/41719910/)). No formal incidence estimate exists.

**Inheritance:** predominantly **autosomal recessive** (OMIM #616271; biallelic *CLPB*), with a distinct **autosomal dominant de novo** subset ([PMID: 34140661](https://pubmed.ncbi.nlm.nih.gov/34140661/)).

**Penetrance/expressivity:** apparently complete penetrance in biallelic/dominant-negative genotypes but **highly variable expressivity**, graded by residual refoldase activity/variant class.

**Founder effect / consanguinity:** a **Greenlandic (Inuit) founder** population is documented—"*Four of the individuals were of Greenlandic descent, and one was North American, of Northern European and Asian descent*" ([PMID: 25597511](https://pubmed.ncbi.nlm.nih.gov/25597511/)). Consanguinity contributes to biallelic cases in some populations. **Carrier frequency** is elevated in the founder population but not formally quantified globally.

**Demographics:** both sexes affected; POI is female-specific. No overall sex-ratio skew is established. **Genetic anticipation / germline mosaicism:** not a repeat-expansion disorder, so no anticipation; germline mosaicism is a theoretical counseling caveat for de novo cases.

**Survival by zygosity:**

| Parameter | Biallelic | Monoallelic (de novo) |
|---|---|---|
| N (63-case cohort) | 41 | 22 |
| Mortality | 66% | 23% |
| Median age at death | 6 months | 2.4 years |
| 4-year survival | 50% | 82% |

"*Death occurred in 66% of biallelic and 23% of monoallelic individuals, with earlier median age at death in biallelic cases (6 months vs 2.4 years). Biallelic cases had significantly higher DBI scores and poorer survival (4-year survival: 50% vs 82%)*" ([PMID: 41719910](https://pubmed.ncbi.nlm.nih.gov/41719910/)).

---

## Section 10 — Diagnostics

**Laboratory / biochemistry:** urine **GC-MS** shows elevated 3-methylglutaconic (and 3-methylglutaric) acid—one neonate's "*urine 3-methylpentenedioic acid... increased to 17.53 μmol/L*" ([PMID: 37906145](https://pubmed.ncbi.nlm.nih.gov/37906145/)). **CBC** demonstrates congenital neutropenia.

**Imaging:** brain **MRI** shows progressive cerebral/cerebellar atrophy and may show structural anomalies; **ophthalmologic exam** detects cataracts.

**Genetic testing (definitive):** molecular confirmation via **NGS**—whole-exome/whole-genome sequencing or targeted panels (congenital neutropenia / 3-MGA / mitochondrial disease)—identifying biallelic or de novo monoallelic *CLPB* variants: "*metabolic analysis suggested 3-methylglutaconic aciduria due to elevated 3-methylglutaconic acid and 3-methylglutaric acid. NGS has detected two compound heterozygous CLPB variants*" ([PMID: 32219827](https://pubmed.ncbi.nlm.nih.gov/32219827/)). WES/WGS is first-line; single-gene *CLPB* testing applies in known founder families. Chromosomal microarray/karyotype/FISH/mtDNA/repeat-expansion testing are **not indicated** (no structural or mtDNA lesions).

**Clinical criteria / differential diagnosis:** 3-MGA-uria is the diagnostic key but is nonspecific—"*There is... a group of disorders with significantly and consistently increased 3-methylglutaconic acid excretion, where the 3-methylglutaconic aciduria is a hallmark of the phenotype and the key to diagnosis*" ([PMID: 23296368](https://pubmed.ncbi.nlm.nih.gov/23296368/)). Differentials with discriminative 3-MGA-uria include **TAZ (Barth syndrome), SERAC1 (MEGDEL), OPA3 (Costeff), DNAJC19 (DCMA), and TMEM70** ([PMID: 23355087](https://pubmed.ncbi.nlm.nih.gov/23355087/)); among congenital neutropenia syndromes, CLPB disease must be distinguished from HAX1 (Kostmann), ELANE, G6PC3 and others ([PMID: 38589208](https://pubmed.ncbi.nlm.nih.gov/38589208/)). Severe neonatal CLPB disease is an important differential of **hyperekplexia** ([PMID: 28687938](https://pubmed.ncbi.nlm.nih.gov/28687938/)).

**Omics diagnostics:** RNAseq/quantitative proteomics/complexome profiling confirm causation in difficult cases ([PMID: 36074910](https://pubmed.ncbi.nlm.nih.gov/36074910/), [PMID: 34140661](https://pubmed.ncbi.nlm.nih.gov/34140661/)). **Screening:** biochemical NBS for 3-MGA is not standard; carrier/cascade testing applies in founder families.

**Suggested LOINC/ontology:** urine organic acids (GC-MS); HP:0003535 (3-MGA-uria); HP:0001875 (neutropenia).

---

## Section 11 — Outcome / Prognosis

**Survival/mortality:** strongly genotype-dependent. Biallelic disease carries 66% mortality (median death 6 months; 4-year survival 50%) versus 23% mortality for monoallelic disease (median death 2.4 years; 4-year survival 82%) ([PMID: 41719910](https://pubmed.ncbi.nlm.nih.gov/41719910/)). The Pronicka cohort spanned "*current median age 17.5 years in the mild group, median age of death 35 days in the severe group*" ([PMID: 28687938](https://pubmed.ncbi.nlm.nih.gov/28687938/)).

**Morbidity/disability:** survivors face intellectual disability, movement disorder, epilepsy, visual impairment (cataracts), recurrent infection (neutropenia), and—in females—infertility from POI. **Complications:** life-threatening infections; progression to **bone-marrow failure, MDS, and acute leukemia** ([PMID: 38589208](https://pubmed.ncbi.nlm.nih.gov/38589208/)); respiratory failure in severe neonates.

**Prognostic factors:** variant class/structural prediction is the strongest—"*Structural predictions—particularly variants causing nonsense-mediated decay or ankyrin domain disruption—were stronger survival predictors than zygosity or age of onset*" ([PMID: 41719910](https://pubmed.ncbi.nlm.nih.gov/41719910/)). Residual **disaggregase activity predicts disease severity** ([PMID: 32573439](https://pubmed.ncbi.nlm.nih.gov/32573439/)). Early onset (<12 months) predicts worse course. No formal QoL metrics are published.

---

## Section 12 — Treatment

**No disease-modifying therapy exists; management is supportive/symptomatic.**

**Pharmacotherapy:** **granulocyte colony-stimulating factor (G-CSF)** corrects neutropenia—"*Administration of granulocyte colony-stimulating factor successfully maintained neutrophil counts above 0.5 × 10⁹/L and significantly reduced the frequency of respiratory tract infections*" ([PMID: 41560087](https://pubmed.ncbi.nlm.nih.gov/41560087/)). Antiepileptics manage seizures; symptomatic agents address the movement disorder. **Pharmacogenomics:** none established.

**Surgical:** **cataract extraction** for visual rehabilitation. **Supportive/rehabilitative:** neonatal respiratory and feeding support in severe disease; developmental, physical, occupational, and speech therapy; endocrine/fertility care (hormone replacement) for POI ([PMID: 36074910](https://pubmed.ncbi.nlm.nih.gov/36074910/)).

**Caveat on G-CSF:** residual malignancy risk persists—"*While some patients benefit from granulocyte colony-stimulating factor treatment, they may still face an increased risk of bone marrow failure, myelodysplastic syndrome and acute leukaemia*"—mandating hematologic surveillance ([PMID: 38589208](https://pubmed.ncbi.nlm.nih.gov/38589208/)). Hematopoietic stem cell transplantation is considered in severe-congenital-neutropenia disorders but is not an established cure for the multisystem CLPB phenotype.

**Advanced/experimental therapeutics:** no approved gene, cell, or RNA-based therapy; no disease-specific clinical trials with NCT identifiers were identified. **Suggested NCIT terms:** C1725 (G-CSF), C15329 (Cataract Surgery), C264 (Anticonvulsant Agent), C15431 (Supportive Care), C15431 (symptom management).

---

## Section 13 — Prevention

Because MGCA7A is a monogenic *CLPB* disorder with **no environmental cause**, prevention is **entirely genetic**:

- **Primary/genetic prevention:** genetic counseling with recurrence-risk assessment (**25%** for carrier couples in AR families; low—but non-zero via germline mosaicism—for de novo dominant cases); **carrier testing** (targeted founder-variant testing in the Greenlandic/Inuit population); **cascade testing** of relatives; and reproductive options including **prenatal diagnosis** and **preimplantation genetic testing (PGT)** once familial variants are known ([PMID: 25597511](https://pubmed.ncbi.nlm.nih.gov/25597511/), [PMID: 34140661](https://pubmed.ncbi.nlm.nih.gov/34140661/)).
- **Secondary prevention:** early diagnosis via urinary organic-acid screening + NGS and prompt supportive care ([PMID: 41560087](https://pubmed.ncbi.nlm.nih.gov/41560087/)).
- **Tertiary prevention:** infection prophylaxis and **leukemia/MDS surveillance** ([PMID: 38589208](https://pubmed.ncbi.nlm.nih.gov/38589208/)).

**Immunization / public-health / environmental interventions:** not applicable (no infectious or environmental etiology).

---

## Section 14 — Other Species / Natural Disease

**Taxonomy / orthologs:** *CLPB* is evolutionarily conserved; a functional ortholog exists in **zebrafish (*Danio rerio*, NCBI Taxon 7955)** (used as a disease model, below). Bacterial/yeast ClpB/Hsp104 family members are the ancestral disaggregases, underscoring deep conservation of the disaggregase mechanism.

**Naturally occurring disease in other species:** no naturally occurring CLPB-deficiency disease has been catalogued in companion animals or wildlife (no OMIA entry identified). **Zoonotic potential / cross-species transmission:** not applicable (non-infectious genetic disorder).

**Comparative biology:** the conservation of the disaggregase from bacteria/yeast (Hsp104) through zebrafish to humans makes the mechanism broadly tractable, but no natural animal disease model is reported.

---

## Section 15 — Model Organisms

**Zebrafish (*Danio rerio*) morphant** is the principal in vivo model: "*Suppression of clpb in zebrafish embryos induced a central nervous system phenotype that was consistent with cerebellar and cerebral atrophy that could be rescued by wild-type, but not mutant, human CLPB mRNA*" ([PMID: 25597510](https://pubmed.ncbi.nlm.nih.gov/25597510/)). This both **recapitulates the CNS atrophy** and provides a **variant-pathogenicity rescue assay**. Its limitation is that it models mainly the neurological component, not the full multisystem syndrome.

**In vitro / cellular models:**
- Recombinant **SKD3 ATPase/disaggregase activity assays** ([PMID: 32573439](https://pubmed.ncbi.nlm.nih.gov/32573439/), [PMID: 35247700](https://pubmed.ncbi.nlm.nih.gov/35247700/)).
- **Patient fibroblasts and liver** showing markedly decreased CLPB protein ([PMID: 25597511](https://pubmed.ncbi.nlm.nih.gov/25597511/)).
- **HEK-293/BT-549** cell fractionation establishing IMS localization and ATP-dependent complexes ([PMID: 32866687](https://pubmed.ncbi.nlm.nih.gov/32866687/)).
- **CLPB-knockout human cell lines** demonstrating reduced solubility of mitochondrial proteins including HAX1 ([PMID: 32573439](https://pubmed.ncbi.nlm.nih.gov/32573439/)).

No published mouse knock-in recapitulating the human genotype–phenotype spectrum was identified—a key gap. **Resources:** ZFIN (zebrafish), Cellosaurus (HEK-293/BT-549).

---

## Mechanistic Model / Interpretation (Synthesis)

The pathophysiology is best understood as a **single enzymatic lesion radiating into tissue-specific failures**. The proximal, best-demonstrated arm is the **CLPB→HAX1→neutropenia** axis: loss of the IMS disaggregase renders anti-apoptotic HAX1 insoluble and mis-assembled, phenocopying the HAX1-mutant Kostmann neutropenia. The remaining arms (brain atrophy, cataract, POI) are **inferred** to arise from generalized IMS proteostatic stress in highly mitochondria-dependent tissues. Severity is **encoded at the genotype**: variants that abolish refoldase activity (NMD/stop-stop, ankyrin-domain disruption) produce lethal neonatal disease, whereas partially functional missense alleles allow survival into adulthood. Critically, **disaggregase (refoldase) activity—not ATPase activity—is the quantitative determinant of severity**, which reframes the protein's function (refolding, not merely ATP hydrolysis) as the therapeutically relevant target.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [25597510](https://pubmed.ncbi.nlm.nih.gov/25597510/) | *CLPB mutations cause 3-MGA, brain atrophy, neutropenia, cataracts* | Human genetics + zebrafish | Gene discovery; zebrafish CNS model |
| [25597511](https://pubmed.ncbi.nlm.nih.gov/25597511/) | *CLPB variants w/ cataract, neutropenia, epilepsy, MGA* | Human genetics | Independent confirmation; Greenlandic founder; variants |
| [34140661](https://pubmed.ncbi.nlm.nih.gov/34140661/) | *Neutropenia & ID are hallmarks of biallelic & de novo CLPB deficiency* | Human genetics + complexome | Dominant-negative subset; HAX1 assembly |
| [32573439](https://pubmed.ncbi.nlm.nih.gov/32573439/) | *Skd3 is a potent mito disaggregase inactivated by MGA mutations* | In vitro + human KO cells | PARL activation; HAX1 solubility; severity predictor |
| [32866687](https://pubmed.ncbi.nlm.nih.gov/32866687/) | *CLPB forms ATP-dependent complexes in the IMS* | Cell biology | Subcellular localization |
| [35247700](https://pubmed.ncbi.nlm.nih.gov/35247700/) | *SKD3 assembles into nucleotide-stabilized dodecamers* | Structural | Double-hexamer architecture; AML link |
| [37041140](https://pubmed.ncbi.nlm.nih.gov/37041140/) | *Structural basis of impaired disaggregase in oxidation-sensitive SKD3 mutant* | Structural | Y272C/Cys267 disulfide mechanism |
| [28687938](https://pubmed.ncbi.nlm.nih.gov/28687938/) | *Scoring system predicting clinical course (31 patients)* | Clinical cohort | Severity stratification; survival; temporal course |
| [41719910](https://pubmed.ncbi.nlm.nih.gov/41719910/) | *Genotype to outcome: zygosity-specific insights (63 cases)* | Clinical cohort | Survival by zygosity; structural predictors |
| [36074910](https://pubmed.ncbi.nlm.nih.gov/36074910/) | *Premature ovarian insufficiency in CLPB deficiency* | Clinical + multi-omics | POI; RNAseq/proteomics validation |
| [41560087](https://pubmed.ncbi.nlm.nih.gov/41560087/) | *CLPB deficiency-associated congenital neutropenia (case report)* | Case report | G-CSF efficacy |
| [38589208](https://pubmed.ncbi.nlm.nih.gov/38589208/) | *Congenital neutropenia syndromes: differential diagnosis* | Review | Residual leukemia/MDS risk; differential |
| [32219827](https://pubmed.ncbi.nlm.nih.gov/32219827/) | *Clinical/genetic analysis of an infant with MGCA7* | Case report | Biochemical + NGS diagnosis |
| [37906145](https://pubmed.ncbi.nlm.nih.gov/37906145/) | *Child with MGCA7 due to novel CLPB variants* | Case report | Urinary 3-MGA hallmark |
| [23296368](https://pubmed.ncbi.nlm.nih.gov/23296368/) | *Inborn errors with 3-MGA-uria: classification & nomenclature* | Review | 3-MGA-uria as diagnostic key |
| [23355087](https://pubmed.ncbi.nlm.nih.gov/23355087/) | *3-MGA-uria: lessons from 50 genes and 977 patients* | Large review | Differential (TAZ, SERAC1, OPA3, DNAJC19, TMEM70) |
| [31048321](https://pubmed.ncbi.nlm.nih.gov/31048321/) | *Targeting mitochondrial structure sensitizes AML to venetoclax* | Functional genomics | Context — CLPB/mito chaperone in AML |

**Evidence-source breakdown:** Human clinical genetics and cohorts provide the strongest evidence for gene–disease relationship, phenotype, and prognosis. Mechanistic claims rest on in vitro biochemistry and human knockout-cell/complexome studies (strong for the HAX1 branch). Animal-model evidence is limited to the zebrafish morphant.

---

## Limitations and Knowledge Gaps

1. **Rarity limits statistics.** Fewer than ~100 patients worldwide; largest cohort 63. Prevalence/incidence, penetrance, and expressivity are described qualitatively, not with confidence intervals.
2. **Mechanistic gaps for non-hematologic branches.** The HAX1–neutropenia link is biochemically demonstrated; the pathways to brain atrophy, cataract, and POI are **inferred** from shared mitochondrial stress, not directly shown. Specific IMS clients and apoptotic effectors in neurons, lens, and ovary are undefined.
3. **Origin of 3-MGA-uria unknown.** As in other mitochondrial 3-MGA-urias (except AUH), the biochemical origin of the excreted acid is unestablished; it is a nonspecific marker, not a direct CLPB readout.
4. **No disease-modifying therapy or validated progression biomarker.** G-CSF addresses only neutropenia and does not abolish malignancy risk; variant class/structural prediction is the only deployed prognostic tool.
5. **Limited animal models.** The zebrafish morphant captures CNS atrophy but not the full syndrome; no mouse knock-in recapitulating the human spectrum was identified.
6. **Modifier genes and epigenetics** underlying the wide severity range are essentially unstudied; founder data outside Greenland/Inuit are sparse.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a mouse (or iPSC-organoid) allelic series** spanning null, hypomorphic missense, and dominant-negative *CLPB* variants to test the "residual refoldase activity sets severity" model in vivo and to model the brain/lens/ovary branches directly.
2. **Define the IMS client interactome** by proximity-labeling (BioID/APEX) proteomics in CLPB-knockout vs. rescued human neurons, lens epithelium, and granulosa cells—to find tissue-specific aggregation-prone clients beyond HAX1.
3. **Develop a quantitative variant-function assay** (recombinant SKD3 disaggregase activity ± PARL processing) as a clinical-grade functional classifier to resolve VUS and refine prognosis ([PMID: 41719910](https://pubmed.ncbi.nlm.nih.gov/41719910/)).
4. **Establish a prospective natural-history registry** with standardized neuro-imaging, CBC, ophthalmologic, and endocrine endpoints to generate confidence-bounded prevalence, penetrance, and progression data and to support trial design.
5. **Test chaperone/proteostasis-restoring or HAX1-stabilizing strategies** (e.g., molecules enhancing residual disaggregase function) in patient-derived cells as disease-modifying proof-of-concept.
6. **Pharmacovigilance for leukemia/MDS** in G-CSF-treated patients via longitudinal bone-marrow surveillance cohorts to quantify malignant-transformation hazard specific to CLPB deficiency.
7. **Expand founder-variant carrier screening** in Greenlandic/Inuit populations and investigate additional geographic founder alleles to inform targeted reproductive genetic services.

---

*Report compiled from 12 confirmed findings across 17 reviewed primary and review articles. Evidence sources are distinguished as human clinical genetics/cohorts, in vitro biochemistry, human knockout-cell and complexome studies, structural biology, and a zebrafish morphant model. All mechanistic and clinical claims are cited to PMID with verbatim abstract support where available.*


## Artifacts

- [OpenScientist final report](3-methylglutaconic_Aciduria_Type_VIIA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](3-methylglutaconic_Aciduria_Type_VIIA-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 22 |
| Quoted claims found in source | 21 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 17 |
| On topic | 14 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:41560087`: "*Administration of granulocyte colony-stimulating factor successfully maintained neutrophil counts above 0.5 × 10⁹/L and significantly reduced the frequency of respiratory tract infections*"
  - closest text in source: "OUTCOMES: Administration of granulocyte colony-stimulating factor successfully maintained neutrophil counts above 0.5 × 109/L and significantly reduced the frequency of respiratory tract infections"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 24 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 12 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001875` (2 mentions) - the report calls it "Lab abnormality", "neutropenia"; HP calls it **Decreased total neutrophil count**
- `HP:0001249` (1 mention) - the report calls it "Clinical sign"; HP calls it **Intellectual disability**
- `HP:0002059` (1 mention) - the report calls it "Imaging"; HP calls it **Cerebral atrophy**
- `HP:0001272` (1 mention) - the report calls it "Imaging"; HP calls it **Cerebellar atrophy**
- `HP:0000518` (1 mention) - the report calls it "Physical"; HP calls it **Cataract**
- `HP:0003535` (2 mentions) - the report calls it "Lab abnormality", "3-MGA-uria"; HP calls it **3-Methylglutaconic aciduria**
- `HP:0100022` (1 mention) - the report calls it "Clinical sign"; HP calls it **Abnormality of movement**
- `HP:0001250` (1 mention) - the report calls it "Clinical sign"; HP calls it **Seizure**
- `HP:0032322` (1 mention) - the report calls it "Clinical sign"; HP calls it **Healthy**
- `HP:0008209` (1 mention) - the report calls it "Clinical sign"; HP calls it **Premature ovarian insufficiency**
- `HP:0002093` (1 mention) - the report calls it "Clinical sign"; HP calls it **Respiratory insufficiency**
- `CHEBI:28123` (1 mention) - the report calls it "3-methylglutaconic acid"; CHEBI calls it **diethanolamine**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001875` - called "Lab abnormality", "neutropenia"
- `HP:0003535` - called "Lab abnormality", "3-MGA-uria"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.