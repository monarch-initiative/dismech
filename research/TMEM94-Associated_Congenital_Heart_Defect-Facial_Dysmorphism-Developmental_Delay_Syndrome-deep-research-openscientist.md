---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T22:17:09.293654'
end_time: '2026-11-11T22:36:30.056078'
duration_seconds: 1160.76
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: TMEM94-Associated Congenital Heart Defect-Facial Dysmorphism-Developmental
    Delay Syndrome
  mondo_id: MONDO:0032672
  category: Mendelian
  causal_genes: TMEM94
  omim_id: OMIM:618316
  synonyms: IDDCDF
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
citation_count: 4
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.5.1
term_validation:
  total_terms: 29
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 2
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0032672
    reported_labels:
    - MONDO
    ontology_label: intellectual developmental disorder with cardiac defects and dysmorphic
      facies
  - term_id: HP:0000325
    reported_labels:
    - Congenital
    ontology_label: Triangular face
  - term_id: HP:0000490
    reported_labels:
    - Congenital
    ontology_label: Deeply set eye
  - term_id: HP:0000463
    reported_labels:
    - Congenital
    ontology_label: Anteverted nares
  - term_id: HP:0000998
    reported_labels:
    - Congenital
    ontology_label: Hypertrichosis
  - term_id: HP:0000307
    reported_labels:
    - Congenital
    ontology_label: Pointed chin
  - term_id: HP:0000316
    reported_labels:
    - Congenital
    ontology_label: Hypertelorism
  - term_id: HP:0001520
    reported_labels:
    - Prenatal/birth
    ontology_label: Large for gestational age
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: TMEM94-Associated_Congenital_Heart_Defect-Facial_Dysmorphism-Developmental_Delay_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: TMEM94-Associated_Congenital_Heart_Defect-Facial_Dysmorphism-Developmental_Delay_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TMEM94-Associated Congenital Heart Defect-Facial Dysmorphism-Developmental Delay Syndrome
- **MONDO ID:** MONDO:0032672 (if available)
- **Causal gene(s):** TMEM94
- **OMIM:** OMIM:618316
- **Synonyms:** IDDCDF
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **TMEM94-Associated Congenital Heart Defect-Facial Dysmorphism-Developmental Delay Syndrome** covering all of the
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

# TMEM94-Associated Congenital Heart Defect–Facial Dysmorphism–Developmental Delay Syndrome (IDDCDF)

**Disease:** Intellectual Developmental Disorder with Cardiac defects and Dysmorphic Facies (IDDCDF)
**MONDO:** MONDO:0032672 · **OMIM:** 618316 · **Causal gene:** **TMEM94** (17q25.1; HGNC:25151; UniProt Q12767; RefSeq NM_014738.6)
**Category:** Mendelian, autosomal recessive · **Inheritance:** Biallelic truncating loss-of-function

---

## Summary

**IDDCDF is an ultra-rare autosomal recessive multisystem syndrome caused by biallelic truncating (loss-of-function) variants in the gene TMEM94.** It is defined by a core clinical triad: (1) global developmental delay / intellectual disability, (2) congenital heart defects (present in ~90% of reported cases), and (3) a distinctive facial gestalt (triangular face, deep-set eyes, broad nasal root/tip, anteverted nostrils, thick arched eyebrows, hypertrichosis, pointed chin, and hypertelorism). The disorder was first delineated in 2018 by Stephen et al. in 10 affected individuals from 6 unrelated families of diverse ethnic backgrounds, and its gene–disease relationship has since been independently confirmed and extended to the prenatal/fetal phenotype and the overgrowth–intellectual-disability spectrum.

The molecular identity of the TMEM94 protein remained obscure until 2024, when Vishnu et al. demonstrated that **TMEM94 is "ERMA," an endoplasmic-reticulum–localized P-type ATPase that pumps magnesium (Mg²⁺) into the ER lumen.** This discovery provides the strongest available mechanistic explanation for the cardiac phenotype: loss of ERMA impairs ER Mg²⁺ refilling, disrupting intracellular Mg²⁺/Ca²⁺ homeostasis and producing abnormal cardiomyocyte Ca²⁺ cycling and cardiac dysfunction. In parallel, patient cells show reduced TMEM94 expression and broad transcriptional dysregulation of genes governing cell growth, proliferation, and survival — a plausible route to the neurodevelopmental and craniofacial features. The complete CRISPR/Cas9 knockout mouse is embryonic lethal, underscoring an essential developmental role.

A notable unresolved tension — a **dosage-sensitivity paradox** — emerges from the combined data. In mice, ERMA *haploinsufficiency* (Erma⁺/⁻) already causes cardiac dysfunction and homozygous nulls are embryonic lethal; yet in humans the disease is strictly recessive, with heterozygous carriers unaffected and gnomAD showing tolerance of heterozygous loss-of-function (pLI≈0, LOEUF=0.61). Management of IDDCDF is entirely supportive (cardiac surgical repair, developmental/rehabilitative therapies) with genetic counseling and prenatal/preimplantation options for prevention; no disease-specific or molecularly targeted therapy currently exists, although the ERMA/Mg²⁺ mechanism nominates magnesium homeostasis as a hypothesis-generating therapeutic avenue.

---

## 1. Disease Information

**Overview.** IDDCDF (Intellectual Developmental Disorder with Cardiac defects and Dysmorphic Facies) is a Mendelian, autosomal recessive neurodevelopmental syndrome with prominent congenital cardiac involvement and a recognizable facial gestalt. It is caused by biallelic truncating variants in **TMEM94**, which encodes a highly conserved multi-pass transmembrane protein now known to be the endoplasmic-reticulum magnesium transporter ERMA.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (disease) | 618316 |
| MONDO | MONDO:0032672 |
| Gene (HGNC) | TMEM94 / HGNC:25151 |
| Gene locus | 17q25.1 |
| UniProt | Q12767 |
| RefSeq transcript | NM_014738.6 |
| InterPro (protein domain) | IPR023298 (P-type ATPase, transmembrane-domain superfamily) |
| ICD-10 / ICD-11 | No specific code; subsumed under general congenital-malformation / intellectual-disability categories |
| MeSH | No specific descriptor |
| Orphanet | No dedicated ORPHAcode identified for the TMEM94-specific entity |

**Synonyms / alternative names.** IDDCDF; TMEM94-associated neurodevelopmental disorder; TMEM94-related congenital heart defect–facial dysmorphism–developmental delay syndrome.

**Information source.** Disease-level knowledge is derived from aggregated case reports and small cohort studies (individual-patient clinical and molecular data), not from large EHR-based or registry datasets. The evidence base is a small number of primary publications describing a total of roughly a dozen patients worldwide.

---

## 2. Etiology

**Primary cause (genetic).** IDDCDF is a monogenic disorder caused by **biallelic truncating loss-of-function (LoF) variants in TMEM94**. Both homozygous and compound-heterozygous genotypes have been reported. The founding study identified such variants in 10 affected individuals from 6 unrelated families "of different ethnic origins," with segregation consistent with autosomal recessive inheritance ([PMID: 30526868](https://pubmed.ncbi.nlm.nih.gov/30526868/)).

> *"we describe ten similarly affected individuals from six unrelated families of different ethnic origins having bi-allelic truncating variants in TMEM94, which encodes for an uncharacterized transmembrane nuclear protein that is highly conserved across mammals"* ([PMID: 30526868](https://pubmed.ncbi.nlm.nih.gov/30526868/)).

**Genetic risk factors.** The only established risk factor is possession of two pathogenic TMEM94 LoF alleles. **Consanguinity** increases the risk of homozygosity for rare recessive alleles and is relevant here, as several original families were consanguineous. There are no known common susceptibility loci or GWAS associations (not applicable to a rare Mendelian disorder).

**Modifier genes.** None established. Phenotypic variability (e.g., the single individual without CHD in the original cohort) is documented, but no modifier locus has been mapped.

**Environmental risk / protective factors and gene–environment interactions.** None identified. As a genotype-determined recessive Mendelian disorder, there are no established environmental risk or protective factors and no documented gene–environment interactions (not applicable / no data).

---

## 3. Phenotypes

The phenotype centers on a **triad**: developmental/cognitive impairment, congenital heart defects, and distinctive craniofacial dysmorphism, with additional multisystem features. Frequencies below derive from the original cohort (Stephen et al. 2018, n=10) ([PMID: 30526868](https://pubmed.ncbi.nlm.nih.gov/30526868/)), with supporting observations from Al-Hamed et al. 2020 ([PMID: 32825426](https://pubmed.ncbi.nlm.nih.gov/32825426/)) and Yüksel Ülker et al. 2023 ([PMID: 36919607](https://pubmed.ncbi.nlm.nih.gov/36919607/)).

| Phenotype | Type | Frequency | Onset | Suggested HPO term |
|---|---|---|---|---|
| Global developmental delay / intellectual disability | Behavioral/cognitive | All (10/10) | Neonatal–childhood | HP:0001263 / HP:0001249 |
| Congenital heart defect | Physical/structural | 9/10 (~90%) | Congenital | HP:0001627 |
| Triangular face | Craniofacial | Frequent | Congenital | HP:0000325 |
| Deep-set eyes | Craniofacial | Frequent | Congenital | HP:0000490 |
| Broad nasal root/tip | Craniofacial | Frequent | Congenital | HP:0000431 / HP:0000455 |
| Anteverted nares | Craniofacial | Frequent | Congenital | HP:0000463 |
| Thick, arched eyebrows | Craniofacial | Frequent | Congenital | HP:0000574 / HP:0002553 |
| Hypertrichosis | Integumentary | Frequent | Congenital | HP:0000998 |
| Pointed chin | Craniofacial | Frequent | Congenital | HP:0000307 |
| Hypertelorism | Craniofacial | Frequent | Congenital | HP:0000316 |
| Birthweight in upper-normal range / overgrowth tendency | Growth | Most | Prenatal/birth | HP:0001520 |

> *"global developmental delay/intellectual disability, and dysmorphic facial features including triangular face, deep set eyes, broad nasal root and tip and anteverted nostrils, thick arched eye brows, hypertrichosis, pointed chin, and hypertelorism. Birthweight in the upper normal range was observed in most, and all but one had congenital heart defects (CHD)"* ([PMID: 30526868](https://pubmed.ncbi.nlm.nih.gov/30526868/)).

**Severity, progression, and QoL.** The disorder is congenital and static in character (a malformation/neurodevelopmental syndrome rather than a progressive degenerative one). Severity is variable but generally moderate-to-severe given universal developmental delay plus structural heart disease. Quality-of-life impact is substantial — cognitive impairment affects education, communication, and independent living, while congenital heart disease carries surgical and functional morbidity. Formal QoL instruments (EQ-5D, SF-36, PROMIS) have not been applied to this ultra-rare disorder (no data).

**Phenotype expansion.** Al-Hamed et al. (2020) extended the spectrum to **prenatal/fetal anomalies** detectable on antenatal ultrasound, and Yüksel Ülker et al. (2023) detected a TMEM94 pathogenic variant in an **overgrowth–intellectual-disability (OGID)** cohort, nudging the phenotype toward the overgrowth/growth-pathway syndromes.

> *"expanded the phenotypes of very rare OGID syndromes caused by FIBP and TMEM94"* ([PMID: 36919607](https://pubmed.ncbi.nlm.nih.gov/36919607/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** TMEM94 (17q25.1; HGNC:25151; UniProt Q12767; reference transcript NM_014738.6). The encoded protein is 1,356 amino acids, a multi-pass (10 transmembrane segment) ER protein of the P-type ATPase superfamily (see Section 6).

**Pathogenic variants — all truncating LoF.** All reported pathogenic/likely-pathogenic variants are truncating (nonsense, frameshift, or canonical splice-site); **no pathogenic missense variant has been reported.** ClinVar (NM_014738.6) lists 8 pathogenic/likely-pathogenic variants:

| HGVS (coding) | Protein consequence | Variant class | Classification |
|---|---|---|---|
| c.3776G>A | p.Trp1259Ter | Nonsense | Pathogenic |
| c.1626C>G | p.Tyr542Ter | Nonsense | Likely pathogenic |
| c.657del | p.Phe220fs | Frameshift | Likely pathogenic |
| c.2129dup | p.Leu710fs | Frameshift | Likely pathogenic |
| c.2280_2281del | p.Gln761fs | Frameshift | Likely pathogenic |
| c.33_42del | p.Pro12fs | Frameshift | Likely pathogenic |
| c.410-2A>T | Splice acceptor | Splice-site | Likely pathogenic |
| c.273-1G>C | Splice acceptor | Splice-site | Likely pathogenic |

Among 404 ClinVar submissions for TMEM94, the majority are benign/likely-benign or VUS, consistent with a **loss-of-function-only** pathogenicity model in a recessive gene (F006).

**Functional consequence.** Loss of function via nonsense-mediated decay (NMD) of truncating transcripts. Patient cells show **reduced TMEM94 expression** — *"Gene expression analysis in available cells from affected individuals showed reduced expression of TMEM94"* ([PMID: 30526868](https://pubmed.ncbi.nlm.nih.gov/30526868/)). This is a classic recessive LoF mechanism; both alleles must be disrupted to cause disease.

**Allele frequency / constraint.** gnomAD shows TMEM94 to be tolerant of heterozygous LoF (pLI≈0; LOEUF/oe_lof_upper = 0.61; observed/expected LoF = 81/158.6), consistent with unaffected heterozygous carriers. Individual pathogenic alleles are ultra-rare or absent in population databases.

**Origin.** Germline. No somatic involvement reported (not applicable — not a cancer gene in this context).

**Modifier genes / epigenetics / chromosomal abnormalities.** No modifier loci, disease-specific epigenetic signatures, or recurrent chromosomal rearrangements described (no data). Chromosomal microarray was used diagnostically in the prenatal setting primarily to exclude CNVs.

---

## 5. Environmental Information

No environmental, lifestyle, toxicological, or infectious contributors are known or expected. IDDCDF is a purely genetic Mendelian disorder; environmental factors (toxins, radiation, diet, smoking, infectious agents) are **not applicable**. Consanguinity is a population-genetic, not environmental, risk amplifier.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic truncating variant in TMEM94** introduces a premature stop / frameshift / splice defect → **leads to** nonsense-mediated decay and **reduced/absent TMEM94 (ERMA) protein** (*demonstrated*: reduced patient-cell expression).
2. Loss of ERMA, an ER-localized P-type ATPase bearing a GMN motif, **results in** failure of **Mg²⁺ transport into the endoplasmic reticulum** (*demonstrated* biochemically for ERMA; *inferred* to apply to patient truncating alleles).
3. Impaired ER Mg²⁺ refilling **leads to** disrupted intracellular **Mg²⁺ homeostasis**, which **results in** abnormal **Ca²⁺ cycling** (Mg²⁺ and Ca²⁺ handling are coupled at the ER) (*demonstrated* in Erma⁺/⁻ cardiomyocytes and ERMA-silenced iPSC-cardiomyocytes).
4. **Branch A — Cardiac:** Abnormal cardiomyocyte Ca²⁺ cycling **leads to** contractile/electrical dysfunction and, developmentally, to **congenital heart defects** and cardiac dysfunction (*strongest mechanistic link*; demonstrated at cellular level, inferred for the structural CHD).
5. **Branch B — Growth/neurodevelopment:** Reduced ERMA **results in** broad transcriptional **dysregulation of cell-growth, proliferation, and survival genes** (*demonstrated* by microarray + RNA-seq), **predicted to impact** neurodevelopmental and hematological systems → contributing to **developmental delay / intellectual disability** and, plausibly, **craniofacial dysmorphism** (*inferred*).
6. **Branch C — Essentiality:** Complete loss (homozygous null in mouse) **leads to** **embryonic lethality**, establishing ERMA as developmentally essential; human viable states imply retained partial function (*demonstrated* in mouse; human residual function *inferred*).

```
TMEM94 biallelic truncation
          │ (NMD → reduced ERMA protein)
          ▼
Loss of ER Mg2+ P-type ATPase (ERMA) activity
          │
          ▼
Impaired ER Mg2+ refilling → disrupted Mg2+/Ca2+ homeostasis
          │
   ┌──────┴───────────┬────────────────────────┐
   ▼                  ▼                         ▼
Abnormal           Dysregulated             Embryonic
cardiomyocyte      growth/proliferation     essentiality
Ca2+ cycling       transcriptome            (null = lethal)
   │                  │
   ▼                  ▼
Congenital         Developmental delay / ID
heart defects      + facial dysmorphism (inferred)
```

### Supporting detail by category

- **Molecular pathways / protein function.** TMEM94 = **ERMA**, an ER multi-pass transmembrane P-type ATPase (UniProt Q12767; 1,356 aa; 10 TM segments; InterPro IPR023298). It possesses the canonical large cytosolic **actuator (A), nucleotide-binding (N), and phosphorylation (P) domains** of P-type ATPases and *"uniquely combines a P-type ATPase domain and a GMN motif for ER Mg²⁺ uptake"* ([PMID: 38513662](https://pubmed.ncbi.nlm.nih.gov/38513662/)). A conserved tyrosine is crucial for Mg²⁺ binding/activity; the mechanism is conserved from prokaryotic mgtA/mgtB.
- **Cellular processes.** Ion transport (Mg²⁺) across the ER membrane; ER ion homeostasis; coupled Ca²⁺ cycling; cell growth/proliferation/survival signaling (via the dysregulated transcriptome).
- **Metabolic / biochemical.** Mg²⁺ is a cofactor for hundreds of ATP-dependent enzymes; ER Mg²⁺ depletion plausibly perturbs ATPase/kinase activity and protein folding, though the downstream metabolic details in IDDCDF are not directly characterized (*inferred*).
- **Tissue damage.** Cardiomyocyte dysfunction via Ca²⁺ mishandling is the demonstrated injury mechanism; neuronal/craniofacial consequences are inferred from the transcriptomic data.
- **Molecular profiling.** *"Global transcriptome profiling using microarray and RNA sequencing revealed several dysregulated genes essential for cell growth, proliferation and survival that are predicted to have an impact on cardiotoxicity hematological system and neurodevelopment"* ([PMID: 30526868](https://pubmed.ncbi.nlm.nih.gov/30526868/)).
- **Functional validation.** *"Cardiac dysfunction by haploinsufficiency, abnormal Ca²⁺ cycling in mouse Erma⁺/⁻ cardiomyocytes, and ERMA mRNA silencing in human iPSC-cardiomyocytes collectively define ERMA as an essential component of ER Mg²⁺ uptake in eukaryotes"* ([PMID: 38513662](https://pubmed.ncbi.nlm.nih.gov/38513662/)).

**Suggested ontology terms.** GO: magnesium ion transmembrane transport (GO:1903830), calcium ion transport (GO:0006816), regulation of cardiac muscle contraction (GO:0055117), heart development (GO:0007507), endoplasmic reticulum membrane (GO:0005789). CL: cardiac muscle cell / cardiomyocyte (CL:0000746), neuron (CL:0000540). CHEBI: magnesium(2+) (CHEBI:18420), calcium(2+) (CHEBI:29108).

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Heart** (primary) — congenital structural defects and cardiac dysfunction. UBERON:0000948.
- **Brain / central nervous system** (primary) — developmental delay and intellectual disability. UBERON:0000955.
- **Craniofacial skeleton / face** (primary) — dysmorphism. UBERON:0001456 (face).
- **Hematological system** — predicted secondary involvement from transcriptomic analysis.

**Body systems:** cardiovascular, nervous, and musculoskeletal/craniofacial, with possible hematologic involvement.

**Tissue and cell level.** Cardiac muscle tissue and **cardiomyocytes** (CL:0000746) are the best-documented affected cell type (demonstrated Ca²⁺-cycling abnormalities). Neural tissue / **neurons** (CL:0000540) are implicated by the developmental phenotype (*inferred*).

**Subcellular level.** The **endoplasmic reticulum** (GO:0005783; ER membrane GO:0005789) is the key compartment, as ERMA resides in and functions at the ER membrane. The protein was originally described as a transmembrane nuclear-associated protein; the definitive, functionally validated localization is the ER.

**Localization / lateralization.** Cardiac defects and facial features are midline/bilateral congenital malformations; no consistent lateralization is reported.

---

## 8. Temporal Development

- **Onset:** Congenital. Structural heart defects and facial dysmorphism are present at birth (and detectable prenatally per Al-Hamed et al. 2020); developmental delay becomes apparent in infancy/early childhood.
- **Onset pattern:** Congenital/static (malformation syndrome), not acute or relapsing.
- **Progression:** Non-progressive in the degenerative sense; structural and cognitive features are fixed, though developmental trajectories and cardiac status evolve with growth and surgical intervention.
- **Course / duration:** Chronic, lifelong.
- **Critical period:** Embryonic/fetal cardiac and craniofacial morphogenesis is the window of vulnerability; the embryonic lethality of the complete mouse knockout underscores the essential early-developmental role. There is no established therapeutic window to reverse structural defects once formed.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive (biallelic truncating LoF). Heterozygous carriers are unaffected.
- **Penetrance / expressivity:** Appears high/complete for the core phenotype in biallelic individuals, with **variable expressivity** (e.g., 1/10 without CHD; variability in facial and growth features).
- **Epidemiology:** Ultra-rare. Prevalence and incidence are not formally quantified; the world literature comprises roughly a dozen reported individuals. No reliable per-100,000 estimate exists (no data).
- **Founder effects / geographic distribution:** No specific founder allele established; original families were of diverse ethnic origins, several consanguineous.
- **Consanguinity:** A relevant risk amplifier for homozygosity in affected families.
- **Carrier frequency:** Not formally established; gnomAD het-LoF tolerance (pLI≈0, LOEUF=0.61) indicates carriers exist in the general population without phenotype.
- **Sex ratio / age distribution:** No sex predilection reported (autosomal); affected individuals present from the prenatal period through childhood.

---

## 10. Diagnostics

**Genetic testing is the definitive diagnostic modality.**
- **Whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)**, typically as **trio** analysis, is the primary route to diagnosis; it identified the gene in all published cohorts. Trio-ES combined with chromosomal microarray was used in the prenatal setting ([PMID: 32825426](https://pubmed.ncbi.nlm.nih.gov/32825426/)).

> *"we used trio-exome sequencing (trio-ES) in conjunction with chromosomal microarray analysis (CMA) to identify two novel homozygous loss of function variants"* ([PMID: 32825426](https://pubmed.ncbi.nlm.nih.gov/32825426/)).

- **Gene panels / single-gene testing:** TMEM94 is included on broad intellectual-disability and congenital-heart-defect NGS panels; targeted single-gene testing is appropriate for familial variant confirmation.
- **Chromosomal microarray (CMA):** Useful to exclude CNVs, especially prenatally, but does not detect the point/indel LoF variants causal here.
- **Variant interpretation:** Per ACMG/AMP, truncating variants in this gene are classified pathogenic/likely-pathogenic (ClinVar, NM_014738.6).

**Clinical / imaging work-up.**
- **Echocardiography** (and fetal echocardiography/anomaly ultrasound prenatally) to define congenital heart defects.
- **Developmental assessment** for delay / intellectual disability.
- **Dysmorphology examination** for the characteristic facial gestalt.
- Brain MRI, ECG, and other studies as clinically indicated.

**Biomarkers / omics diagnostics.** No validated circulating biomarker exists. Research-level transcriptomic profiling has been mechanistically informative but is not a clinical diagnostic. The ERMA/Mg²⁺ biology raises the untested possibility of Mg²⁺-handling assays as future biomarkers (*speculative*).

**Differential diagnosis.** Other syndromic congenital-heart-defect-with-developmental-delay disorders (e.g., Kabuki syndrome, CHARGE syndrome, Noonan/RASopathies, Cornelia de Lange spectrum, and overgrowth–ID syndromes such as those caused by FIBP/SUZ12). The specific facial gestalt plus biallelic TMEM94 LoF genotype distinguishes IDDCDF.

**Screening.** Cascade carrier testing within affected families; prenatal/preimplantation testing where the familial variants are known. No population newborn-screening program exists for this ultra-rare disorder.

---

## 11. Outcome / Prognosis

Formal survival, mortality, and natural-history data are **not available** for this ultra-rare disorder. Prognosis is driven principally by the **severity of the congenital heart defect** (and its surgical correctability) and the **degree of developmental/intellectual impairment**. The complete-null state is embryonic lethal in mice, implying that viable patients retain partial gene function. Morbidity is substantial and lifelong, encompassing cognitive disability and cardiac disease. No validated prognostic biomarkers exist. Recovery of the structural/cognitive deficits is not expected; management aims at functional optimization.

---

## 12. Treatment

**No disease-specific or molecularly targeted therapy exists.** Management is **entirely supportive and symptom-directed**:

- **Cardiac:** Surgical/interventional repair of congenital heart defects; cardiology follow-up and heart-failure management as needed. (NCIT: Cardiac Surgical Procedure.)
- **Neurodevelopmental:** Early-intervention programs; physical, occupational, and speech therapy; special education. (NCIT: Physical Therapy; Occupational Therapy; Speech Therapy; Rehabilitation Therapy.)
- **Multidisciplinary care:** Genetics, cardiology, developmental pediatrics/neurology, and dysmorphology.
- **Genetic counseling:** For recurrence-risk assessment and family planning (25% recurrence risk for carrier couples). (NCIT: Genetic Counseling.)

**Pharmacotherapy / advanced therapeutics.** No approved pharmacologic, gene, cell, or RNA-based therapy. No pharmacogenomic guidance is established. The 2024 identification of ERMA as an ER Mg²⁺ transporter nominates **magnesium homeostasis** as a mechanistic hypothesis for future therapeutic exploration, but this is entirely untested and should be regarded as a research direction, not a recommendation.

**Experimental treatments / clinical trials.** None identified for IDDCDF (no NCT trials specific to TMEM94 disease).

---

## 13. Prevention

- **Primary prevention:** Not applicable to a genetic disorder beyond reproductive planning. **Genetic counseling** is the cornerstone; consanguinity counseling is relevant in at-risk populations.
- **Genetic/reproductive prevention:** **Carrier screening** of relatives, **prenatal diagnosis** (where familial variants are known), and **preimplantation genetic testing (PGT-M)** can prevent recurrence in known-carrier couples. Trio-ES plus CMA enabled prenatal detection ([PMID: 32825426](https://pubmed.ncbi.nlm.nih.gov/32825426/)).
- **Secondary/tertiary prevention:** Early echocardiographic and developmental assessment to guide timely cardiac surgery and early-intervention therapies, minimizing complications and optimizing function.
- **Immunization / behavioral / public-health / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** TMEM94/ERMA is **highly conserved across mammals**, and the Mg²⁺-transport mechanism is conserved down to prokaryotes (bacterial mgtA/mgtB P-type ATPases) ([PMID: 38513662](https://pubmed.ncbi.nlm.nih.gov/38513662/)). The mouse ortholog is *Tmem94/Erma* (NCBI Taxon: *Mus musculus*, 10090).
- **Natural disease in other species:** No naturally occurring companion-animal or wildlife disease attributable to TMEM94 has been catalogued (no OMIA entry identified). (No data.)
- **Comparative biology:** The deep evolutionary conservation of the P-type ATPase + GMN Mg²⁺-uptake mechanism underscores the fundamental, conserved role of ER Mg²⁺ homeostasis.

---

## 15. Model Organisms

| Model | Type | Key finding | Reference |
|---|---|---|---|
| CRISPR/Cas9 *Tmem94* knockout mouse (homozygous null) | Mammalian, germline KO | **Embryonic lethal** — establishes developmental essentiality | [PMID: 30526868](https://pubmed.ncbi.nlm.nih.gov/30526868/) |
| *Erma⁺/⁻* heterozygous mouse | Mammalian, haploinsufficient | **Cardiac dysfunction**; abnormal cardiomyocyte Ca²⁺ cycling | [PMID: 38513662](https://pubmed.ncbi.nlm.nih.gov/38513662/) |
| Human iPSC-derived cardiomyocytes, ERMA mRNA silencing | In vitro cellular | Recapitulates Ca²⁺-cycling/contractile defects | [PMID: 38513662](https://pubmed.ncbi.nlm.nih.gov/38513662/) |
| Patient-derived cells (expression/transcriptomics) | In vitro | Reduced TMEM94 expression; dysregulated growth/proliferation transcriptome | [PMID: 30526868](https://pubmed.ncbi.nlm.nih.gov/30526868/) |

**Phenotype recapitulation & limitations.** The mouse and iPSC models robustly recapitulate the **cardiac** dimension of the disorder, directly linking ERMA loss to cardiomyocyte Ca²⁺ dysfunction. However, the **homozygous-null mouse is embryonic lethal**, so it does not model the viable human phenotype, and no mouse model reproduces the full triad including the neurodevelopmental and craniofacial features. This is the key limitation and the source of the dosage paradox below.

---

## Mechanistic Model / Interpretation

The combined evidence supports a coherent model in which **IDDCDF is an ER-magnesium-homeostasis disorder.** Biallelic truncation of TMEM94 removes the ERMA P-type ATPase that pumps Mg²⁺ into the ER; the resulting failure to refill ER Mg²⁺ destabilizes coupled Mg²⁺/Ca²⁺ handling. In cardiomyocytes — exquisitely dependent on tight Ca²⁺ cycling — this produces the demonstrated contractile/electrical dysfunction and underlies the congenital heart defects (the best-supported causal branch). In parallel, loss of ERMA broadly dysregulates genes governing cell growth, proliferation, and survival, a plausible (though not mechanistically dissected) route to the neurodevelopmental delay and craniofacial dysmorphism. The embryonic lethality of the complete knockout confirms ERMA as developmentally essential, consistent with a congenital, multisystem syndrome.

### The dosage-sensitivity paradox (F007)

| Observation | Mouse | Human |
|---|---|---|
| Heterozygous LoF | Cardiac dysfunction (Erma⁺/⁻) | **Unaffected carrier** (gnomAD het-LoF tolerant, pLI≈0, LOEUF=0.61) |
| Biallelic / null | Embryonic lethal | **Viable with IDDCDF** (recessive) |

This cross-species discordance implies either (a) species differences in dosage sensitivity of ER Mg²⁺ transport, (b) residual/partial function from human truncating alleles (e.g., escape from NMD, truncated proteins retaining partial activity, or compensatory redundancy), or (c) differences in the mouse Erma⁺/⁻ cardiac-assay sensitivity versus human clinical thresholds. Resolving it is the central open mechanistic question.

---

## Evidence Base

| Paper | PMID | Role / contribution |
|---|---|---|
| *Bi-allelic TMEM94 Truncating Variants Are Associated with Neurodevelopmental Delay, Congenital Heart Defects, and Distinct Facial Dysmorphism* (Stephen et al., 2018) | [30526868](https://pubmed.ncbi.nlm.nih.gov/30526868/) | **Founding gene–disease paper.** Defines the triad in 10 patients/6 families; shows reduced TMEM94 expression, dysregulated growth/proliferation transcriptome, and embryonic-lethal KO mouse. |
| *Fetal Anomalies Associated with Novel Pathogenic Variants in TMEM94* (Al-Hamed et al., 2020) | [32825426](https://pubmed.ncbi.nlm.nih.gov/32825426/) | **Independent confirmation + prenatal expansion.** Two novel homozygous LoF variants via trio-ES + CMA; extends phenotype to the fetal period. |
| *An investigation of the etiology and follow-up findings in 35 children with overgrowth syndromes…* (Yüksel Ülker et al., 2023) | [36919607](https://pubmed.ncbi.nlm.nih.gov/36919607/) | **Phenotype expansion.** TMEM94 variant in 1/35 OGID children; broadens spectrum toward overgrowth–ID. |
| *ERMA (TMEM94) is a P-type ATPase transporter for Mg²⁺* (Vishnu et al., Mol Cell 2024) | [38513662](https://pubmed.ncbi.nlm.nih.gov/38513662/) | **Mechanistic keystone.** Identifies TMEM94 as the ER Mg²⁺ P-type ATPase ERMA; links its loss to cardiomyocyte Ca²⁺ dysfunction via mouse Erma⁺/⁻ and iPSC-CM silencing. |

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base.** ~12 patients across 4 papers; frequencies and prognosis are poorly quantified, and no formal epidemiology or natural-history data exist.
2. **Mechanistic gaps for brain and face.** The ERMA/Mg²⁺ mechanism is demonstrated for the heart; the causal path to developmental delay and craniofacial dysmorphism remains inferential (via transcriptomic dysregulation).
3. **Dosage paradox unresolved.** Mouse haploinsufficiency vs human recessive inheritance is not explained.
4. **No full-recapitulation animal model.** Homozygous-null mouse is embryonic lethal; no viable model reproduces the complete human triad.
5. **No biomarkers, no targeted therapy, no trials.** Management is empirical/supportive.
6. **Localization nuance.** Early description as a "nuclear" transmembrane protein vs the functionally validated ER localization should be reconciled in annotations (ER is the correct functional site).

---

## Proposed Follow-up Experiments / Actions

1. **Conditional/hypomorphic mouse models** (cardiac-, neural-crest-, and neuron-specific *Erma* conditional knockouts, plus hypomorphic alleles mimicking human truncations) to bypass embryonic lethality and model the full triad.
2. **Directly test ER Mg²⁺/Ca²⁺ handling in patient-derived iPSC cardiomyocytes and neurons/organoids**, and assess whether Mg²⁺ supplementation or Mg²⁺-channel modulation rescues Ca²⁺-cycling defects (tests the therapeutic hypothesis).
3. **Mechanistically link ERMA loss to craniofacial development** using neural-crest and cranial-cartilage models with single-cell transcriptomics.
4. **Resolve the dosage paradox** by quantifying residual function / NMD escape of human truncating alleles and comparing mouse vs human cardiac dosage sensitivity.
5. **Establish a patient registry / GeneMatcher-driven cohort** to quantify phenotype frequencies, natural history, and genotype–phenotype correlations and to formalize diagnostic and management guidelines.
6. **Reconcile subcellular-localization annotations** (nuclear vs ER) in UniProt/GO to reflect the functionally validated ER-membrane localization.

---

*Report compiled from 4 primary publications and public variant/constraint databases (ClinVar NM_014738.6; gnomAD). Evidence types: human clinical (cohort/case reports), model organism (mouse KO/heterozygote), in vitro (patient cells, iPSC-cardiomyocytes), and computational (population constraint).*


## Artifacts

- [OpenScientist final report](TMEM94-Associated_Congenital_Heart_Defect-Facial_Dysmorphism-Developmental_Delay_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](TMEM94-Associated_Congenital_Heart_Defect-Facial_Dysmorphism-Developmental_Delay_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 12 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032672` (2 mentions) - the report calls it "MONDO"; MONDO calls it **intellectual developmental disorder with cardiac defects and dysmorphic facies**
- `HP:0000325` (1 mention) - the report calls it "Congenital"; HP calls it **Triangular face**
- `HP:0000490` (1 mention) - the report calls it "Congenital"; HP calls it **Deeply set eye**
- `HP:0000463` (1 mention) - the report calls it "Congenital"; HP calls it **Anteverted nares**
- `HP:0000998` (1 mention) - the report calls it "Congenital"; HP calls it **Hypertrichosis**
- `HP:0000307` (1 mention) - the report calls it "Congenital"; HP calls it **Pointed chin**
- `HP:0000316` (1 mention) - the report calls it "Congenital"; HP calls it **Hypertelorism**
- `HP:0001520` (1 mention) - the report calls it "Prenatal/birth"; HP calls it **Large for gestational age**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001627` (1 mention) - the report calls it "Congenital"; HP calls it **Abnormal heart morphology**, and lists "Congenital heart defect" among its other names
- `CL:0000746` (2 mentions) - the report calls it "cardiomyocytes"; CL calls it **cardiac muscle cell**, and lists "cardiomyocyte" among its other names