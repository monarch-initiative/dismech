---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T20:58:13.138893'
end_time: '2026-10-16T21:23:07.184325'
duration_seconds: 1494.05
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: FBXW7-Related Neurodevelopmental Disorder
  mondo_id: MONDO:0859280
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
citation_count: 15
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 9
  validator_version: 0.3.0
term_validation:
  total_terms: 42
  verified: 41
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 10
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: HP:0001252
    reported_labels:
    - Clinical sign
    ontology_label: Hypotonia
  - term_id: HP:0001263
    reported_labels:
    - Clinical sign
    ontology_label: Global developmental delay
  - term_id: HP:0000750
    reported_labels:
    - Clinical sign
    ontology_label: Delayed speech and language development
  - term_id: HP:0001249
    reported_labels:
    - Clinical sign
    ontology_label: Intellectual disability
  - term_id: HP:0001273
    reported_labels:
    - Imaging/structural
    ontology_label: Abnormal corpus callosum morphology
  - term_id: HP:0001317
    reported_labels:
    - Imaging/structural
    ontology_label: Abnormal cerebellum morphology
  - term_id: HP:0002500
    reported_labels:
    - Imaging/structural
    ontology_label: Abnormal cerebral white matter morphology
  - term_id: HP:0002019
    reported_labels:
    - Symptom (GI)
    ontology_label: Constipation
  - term_id: HP:0002788
    reported_labels:
    - Clinical sign
    ontology_label: Recurrent upper respiratory tract infections
  - term_id: NCIT:C15265
    reported_labels:
    - Rehabilitation Therapy
    ontology_label: Kidney Transplantation
  - term_id: NCIT:C258
    reported_labels:
    - Laxative
    ontology_label: Antibiotic
  - term_id: NCIT:C15277
    reported_labels:
    - Behavioral Therapy
    ontology_label: Mastectomy
  - term_id: NCIT:C15417
    reported_labels:
    - Genetic Counseling
    ontology_label: Randomized Clinical Trial
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: FBXW7-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: FBXW7-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** FBXW7-Related Neurodevelopmental Disorder
- **MONDO ID:** MONDO:0859280 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FBXW7-Related Neurodevelopmental Disorder** covering all of the
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

# FBXW7-Related Neurodevelopmental Disorder: Comprehensive Disease Characteristics Report

**Disease:** FBXW7-Related Neurodevelopmental Disorder
**MONDO ID:** MONDO:0859280
**Gene:** *FBXW7* (HGNC:13618; NCBI Gene 55294; OMIM gene 606278); chromosome 4q31.3
**Category:** Mendelian, autosomal dominant

---

## Summary

FBXW7-Related Neurodevelopmental Disorder (FBXW7-NDD) is a rare, recently delineated autosomal dominant Mendelian syndrome caused by **monoallelic loss-of-function variants in *FBXW7***, the substrate-recognition subunit of the SCF (SKP1–CUL1–F-box) E3 ubiquitin ligase. The disorder was formally established in 2022 by Stephenson and colleagues, who assembled a cohort of 35 affected individuals harboring de novo and inherited chromosomal deletions, nonsense, frameshift, splice-site, and missense variants ([PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/)). The core clinical phenotype comprises **global developmental delay, borderline-to-severe intellectual disability, hypotonia, and gastrointestinal issues**, with variable structural brain abnormalities affecting the cerebellum, corpus callosum, and white matter. Epilepsy (frequently absence-type), behavioral difficulties, and recurrent respiratory/otolaryngological infections are additional recurring features.

Mechanistically, FBXW7 normally drives phosphorylation-dependent ubiquitination and proteasomal degradation of a set of growth-promoting substrates — most importantly **NOTCH1, CYCLIN E1/E2, c-Jun, c-MYC, mTOR, and BRAF**. Pathogenic variants impair this activity: truncating variants and 4q31.3 deletions reduce protein dosage (haploinsufficiency), WD40-domain missense variants cluster at the substrate-binding surface and reduce substrate affinity, and F-box-domain missense variants disrupt assembly of the SCF complex via impaired SKP1 binding. The downstream consequence — **accumulation of undegraded substrates and aberrant NOTCH/c-Jun/MYC signaling** — dysregulates neural stem cell proliferation, differentiation, and migration. This mechanism is strongly corroborated across evolutionarily conserved model systems (mouse, zebrafish, *Drosophila*).

Clinically important secondary features include a **Wilms tumor predisposition** operating through a classic two-hit tumor-suppressor mechanism (germline first hit plus a somatic second hit in renal tissue), which warrants renal ultrasound surveillance in individuals with constitutional/germline variants. The disorder shows **incomplete penetrance and variable, partly domain-dependent expressivity** — F-box-domain variants can produce a strikingly mild phenotype (isolated drug-responsive absence epilepsy without intellectual disability), whereas WD40-domain variants and structural lesions tend to produce more severe, multisystem presentations. Management is currently supportive: early developmental therapies, anti-seizure medication, management of constipation and infections, tumor surveillance, and genetic counseling. No targeted or disease-modifying therapy exists.

---

## Section 1 — Disease Information

**Overview.** FBXW7-NDD is a monogenic neurodevelopmental disorder caused by heterozygous loss-of-function of *FBXW7*, which encodes the F-box/WD-repeat protein that serves as the substrate-recognition component of an SCF-type Cullin-RING E3 ubiquitin ligase. Because *FBXW7* is a canonical tumor suppressor, the disorder bridges two domains: a neurodevelopmental syndrome and a cancer (Wilms tumor) predisposition.

**Key identifiers.**
- **MONDO:** MONDO:0859280
- **Gene:** *FBXW7* — HGNC:13618; NCBI Gene 55294; OMIM gene 606278; locus 4q31.3
- **OMIM / ICD / Orphanet / MeSH:** Specific OMIM phenotype, ICD-10/ICD-11, and Orphanet numbers were not definitively confirmed within this investigation and should be verified against OMIM and Orphanet directly. The disorder is sometimes catalogued under broad "autosomal dominant intellectual disability" ICD rubrics.

**Synonyms / alternative names.** FBXW7 neurodevelopmental syndrome; FBXW7-related neurodevelopmental disorder; FBX(W7)-related neurodevelopmental syndrome (as used in the CNV literature). The gene itself has aliases including *CDC4*, *SEL10*, *hCDC4*, and *FBW7*.

**Information source.** The knowledge base is derived from **aggregated disease-level resources** — principally a multicenter cohort study ([PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/)), subsequent multicenter case series ([PMID: 42432493](https://pubmed.ncbi.nlm.nih.gov/42432493/)), a dedicated review ([PMID: 42111496](https://pubmed.ncbi.nlm.nih.gov/42111496/)), individual case reports, and model-organism studies — rather than from individual EHR mining.

---

## Section 2 — Etiology

**Primary cause — genetic.** FBXW7-NDD is caused by **monoallelic (heterozygous) loss-of-function variants in *FBXW7***. Stephenson et al. documented the full loss-of-function spectrum: chromosomal deletions, nonsense, frameshift, splice-site, and missense variants, arising both de novo and inherited ([PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/)): *"35 individuals harboring de novo and inherited FBXW7 germline monoallelic chromosomal deletions and nonsense, frameshift, splice-site, and missense variants associated with a neurodevelopmental syndrome."* Structural/regulatory lesions at 4q31.3 (deletions, duplications, translocations with position effects) are an additional causal class (see Section 4).

**Genetic risk factors.** The causal variant itself is the risk factor; there are no established susceptibility loci or polygenic contributors beyond the primary *FBXW7* lesion. Domain location of missense variants modulates severity (modifier-like effect — see Section 9). A somatic *FBXW7* second-hit variant is the proximate risk factor for Wilms tumor in germline carriers.

**Environmental risk factors.** None established. The disorder is Mendelian; no toxin, infectious, lifestyle, or occupational exposure has been linked to causation. Many cases are de novo, implicating spontaneous germline mutation (for which advanced parental age is a general, non-specific risk factor for de novo mutation).

**Protective factors.** None identified (genetic or environmental). This has not been systematically studied given the rarity of the disorder.

**Gene–environment interactions.** None documented. The two-hit tumor mechanism is a gene–(somatic)gene interaction rather than a gene–environment interaction.

---

## Section 3 — Phenotypes

FBXW7-NDD is a multisystem but neurologically-dominant disorder. The table below consolidates phenotype frequencies, drawing principally on the 2026 multicenter case series of 7 individuals ([PMID: 42432493](https://pubmed.ncbi.nlm.nih.gov/42432493/)) and the foundational cohort ([PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/)).

| Phenotype | Type | Suggested HPO term | Frequency (case series) | Onset / severity |
|---|---|---|---|---|
| Hypotonia | Clinical sign | HP:0001252 | 7/7 (100%) | Neonatal/infantile; variable |
| Global developmental delay | Clinical sign | HP:0001263 | 6/7 (~86%) | Early childhood |
| Language/speech impairment | Clinical sign | HP:0000750 | 6/7 (~86%) | Childhood |
| Intellectual disability | Clinical sign | HP:0001249 | 4/7 (~57%); borderline–severe | Childhood; variable |
| Epileptic seizures (incl. absence) | Clinical sign | HP:0001250 / HP:0002121 | 4/7 (~57%) | Childhood; often drug-responsive |
| Corpus callosum anomaly | Imaging/structural | HP:0001273 | 2/6 on MRI | Congenital |
| Cerebellar abnormality | Imaging/structural | HP:0001317 | Variable | Congenital |
| White matter abnormality | Imaging/structural | HP:0002500 | Variable | Congenital |
| Constipation | Symptom (GI) | HP:0002019 | Common extracerebral feature | Variable |
| Recurrent respiratory/ENT infections | Clinical sign | HP:0002788 | Common extracerebral feature | Childhood |
| Behavioral difficulties | Behavioral | HP:0000708 | Variable (can predominate) | Childhood |
| Wilms tumor (predisposition) | Neoplasm | HP:0002667 | Rare but recurrent | Childhood |

From the case series ([PMID: 42432493](https://pubmed.ncbi.nlm.nih.gov/42432493/)): *"Neurodevelopmental involvement was present in six individuals and was characterized by global developmental delay and language impairment; hypotonia was observed in all seven. Formal intellectual disability was documented in four cases."* Epilepsy frequency: *"Epileptic seizures occurred in four individuals, whereas three had no history of epilepsy."* Extracerebral features: *"Extracerebral features were variably reported, most commonly constipation and recurrent respiratory/otolaryngological infections."*

**Severity and progression.** The neurodevelopmental deficits are **static/non-progressive** (a developmental, not neurodegenerative, disorder), though functional impact is lifelong. Severity is **highly variable**, ranging from preserved cognition with isolated behavioral difficulties or isolated absence epilepsy, to severe intellectual disability with structural brain anomalies. The 2022 cohort described the spectrum as *"borderline to severe intellectual disability"* ([PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/)).

**Quality-of-life impact.** No disease-specific EQ-5D/SF-36/PROMIS data exist. Impact is inferred from phenotype: intellectual disability, language impairment, and epilepsy substantially affect daily functioning, education, communication, and independence; hypotonia and GI issues add care burden. Milder (F-box-variant) individuals may have near-normal functioning.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *FBXW7* (F-box and WD repeat domain containing 7); HGNC:13618; NCBI Gene 55294; OMIM gene 606278; locus **4q31.3**. The protein has three functional regions relevant to disease: an N-terminal dimerization domain, an **F-box domain** (binds SKP1 to assemble the SCF complex), and a C-terminal **WD40 β-propeller domain** (binds phosphorylated substrates via a conserved phosphodegron, CPD).

**Variant spectrum and classification.** All variant classes consistent with loss of function have been reported — **nonsense, frameshift, splice-site, missense, and whole/partial-gene deletions** — most classified pathogenic/likely pathogenic per ACMG/AMP criteria ([PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/)). Representative missense: c.926G>C p.(Arg309Pro) in the F-box domain ([PMID: 41685408](https://pubmed.ncbi.nlm.nih.gov/41685408/)).

**Functional consequences — loss of function (haploinsufficiency).** Several lines of evidence converge on loss of function:
- Truncating variants and deletions reduce gene dosage.
- WD40 missense variants cluster at the substrate-binding surface: *"A crystal-structure model of FBXW7 predicted that missense variants were clustered at the substrate-binding surface of the WD40 domain and that these might reduce FBXW7 substrate binding affinity"* ([PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/)).
- Direct functional assay: *"Expression of recombinant FBXW7 missense variants in cultured cells demonstrated impaired CYCLIN E1 and CYCLIN E2 turnover"* ([PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/)).
- Position-effect lesion: *"FBXW7 expression in the immortalized lymphoblasts of the patient was reduced compared to that in controls"* ([PMID: 39123068](https://pubmed.ncbi.nlm.nih.gov/39123068/)).

**Allele frequency.** Pathogenic variants are absent or ultra-rare in gnomAD, consistent with a highly penetrant, deleterious disorder; *FBXW7* is strongly constrained against loss-of-function variation (high pLI), supporting haploinsufficiency as the disease mechanism.

**Somatic vs germline.** FBXW7-NDD is caused by **germline (constitutional)** variants. In Wilms tumor, a **somatic second-hit** variant on the other allele is detected in tumor DNA, consistent with Knudson's two-hit model ([PMID: 39414990](https://pubmed.ncbi.nlm.nih.gov/39414990/)). *FBXW7* is also one of the most commonly somatically mutated tumor-suppressor genes across sporadic cancers.

**Modifier genes.** No formal modifier genes identified. The principal determinant of expressivity appears to be the **affected protein domain** (F-box vs WD40 — see Section 9).

**Epigenetic information.** No disease-specific DNA-methylation episignature has been established for FBXW7-NDD. (In cancer contexts FBXW7 can be downregulated epigenetically, but this is not documented as a germline-disorder mechanism.)

**Chromosomal abnormalities.** Large-scale lesions at 4q31.3 cause the disorder:
- De novo **deletion and duplication** affecting the FBXW7 regulatory region/TAD boundary, with Hi-C-confirmed rewiring in neural progenitors ([PMID: 38780184](https://pubmed.ncbi.nlm.nih.gov/38780184/)): *"two patients with a de novo deletion and a duplication in chromosome 4q31, potentially causing FBX-related neurodevelopmental syndrome by affecting the regulatory region of FBXW7."*
- A de novo **translocation t(3;4)(q27;q31.2)** producing a downstream position effect that reduced FBXW7 expression ([PMID: 39123068](https://pubmed.ncbi.nlm.nih.gov/39123068/)).

---

## Section 5 — Environmental Information

**Environmental factors.** None established as causal or contributory. FBXW7-NDD is a Mendelian disorder.

**Lifestyle factors.** Not applicable to disease causation.

**Infectious agents.** None. (Recurrent respiratory/ENT infections are a *consequence/feature* of the disorder, not a cause.)

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. A **monoallelic loss-of-function lesion in *FBXW7*** (truncating variant, WD40 missense, F-box missense, 4q31.3 deletion/duplication, or position-effect translocation) **reduces functional FBXW7 protein or impairs its activity**.
   - *Branch A (truncating / deletion / position effect):* reduced FBXW7 **dosage** (haploinsufficiency).
   - *Branch B (WD40 missense):* intact protein with **reduced substrate-binding affinity** (crystal-structure modeling; [PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/)).
   - *Branch C (F-box missense):* impaired **SKP1 binding → defective SCF complex assembly** ([PMID: 41685408](https://pubmed.ncbi.nlm.nih.gov/41685408/)).
2. Impaired FBXW7 function **results in decreased phosphodegron-dependent ubiquitination** of its substrates by the SCF(FBXW7) E3 ligase.
3. This **leads to reduced proteasomal degradation and accumulation** of substrate oncoproteins — **NOTCH1, CYCLIN E1/E2, c-Jun, c-MYC, mTOR, BRAF, MCL-1** (demonstrated for CYCLIN E1/E2 in patient variants; demonstrated for NOTCH1 and c-Jun in mouse).
4. Substrate accumulation **results in aberrant activation of downstream signaling** — chiefly **NOTCH signaling** and **c-Jun/MYC/mTOR-driven proliferation** (with cross-talk to PI3K/AKT and Wnt/β-catenin).
5. Dysregulated signaling **disrupts neural stem/progenitor cell proliferation, differentiation, migration, and apoptosis** (demonstrated in mouse cerebellum and zebrafish spinal cord; *inferred* for human brain).
6. This **leads to the developmental structural and functional CNS defects** — cerebellar hypoplasia/Purkinje cell loss, corpus callosum and white-matter anomalies, abnormal cortical/neuronal function.
7. These **manifest clinically** as global developmental delay, intellectual disability, hypotonia, epilepsy, and behavioral difficulties.
8. *Parallel branch (tumor):* in renal (and other) tissue, the germline first hit plus a **somatic second-hit *FBXW7* variant** causes biallelic inactivation → unchecked CYCLIN E/NOTCH-driven proliferation → **Wilms tumor**.

### Supporting detail

**Molecular pathways.** FBXW7 is *"a member of the F-box protein family within the ubiquitin-proteasome system [that] performs an indispensable role in orchestrating cellular processes through ubiquitination and degradation of its substrates, such as c-MYC, mTOR, MCL-1, Notch, and cyclin E"* ([PMID: 35515121](https://pubmed.ncbi.nlm.nih.gov/35515121/)). It *"serves a role in phosphorylation-dependent ubiquitination and proteasome degradation of oncoproteins"* ([PMID: 35346215](https://pubmed.ncbi.nlm.nih.gov/35346215/)). Dysregulated pathways therefore include **NOTCH, MYC, mTOR, Wnt/β-catenin, and PI3K/AKT**. Suggested GO terms: GO:0016567 (protein ubiquitination), GO:0043161 (proteasome-mediated ubiquitin-dependent protein catabolic process), GO:0007219 (Notch signaling pathway), GO:0008285 (negative regulation of cell proliferation).

**Cellular processes.** Cell-cycle regulation (via CYCLIN E), neural stem cell differentiation vs self-renewal (via NOTCH), apoptosis and stress response (via c-Jun, MCL-1), and progenitor migration. *"Fbw7 is highly expressed in the nervous system and controls neural stem cell differentiation and apoptosis via Notch and c-Jun during embryonic development"* ([PMID: 21827743](https://pubmed.ncbi.nlm.nih.gov/21827743/)).

**Protein dysfunction.** Loss of function dominates: reduced abundance (truncating/deletion), reduced substrate binding (WD40 missense), or failed SCF assembly (F-box missense). FBXW7 functions as a dimer; some missense variants may additionally act in a dominant-negative fashion on the wild-type allele, although the predominant model is haploinsufficiency/loss of function.

**Subcellular localization.** FBXW7 isoforms localize to the **nucleus (α), cytoplasm/nucleoplasm (β), and nucleolus (γ)**; substrate degradation occurs via the **26S proteasome**. Suggested GO cellular component terms: GO:0019005 (SCF ubiquitin ligase complex), GO:0005634 (nucleus), GO:0005730 (nucleolus).

**Metabolic / immune / biochemical.** No specific metabolic defect or primary immune abnormality is established. Recurrent infections are likely secondary (e.g., hypotonia-related aspiration, structural ENT factors) rather than a primary immunodeficiency. The core biochemical defect is deficient E3-ligase-mediated substrate turnover.

**Model-organism evidence (cross-species convergence on NOTCH).**
- **Mouse:** Conditional cerebellar *Fbxw7* knockout → *"decreased cerebellar size, reduced Purkinje cell number and defects in axonal arborisation … supranumeral fissures and aberrant progenitor cell migration"*, with *"Notch1 and N-terminally phosphorylated c-Jun … upregulated"* ([PMID: 21827743](https://pubmed.ncbi.nlm.nih.gov/21827743/)). Concomitant c-Jun deletion rescued Purkinje cell number.
- **Zebrafish:** *"Notch signaling activity was elevated in spinal cord precursors of fbxw7 mutant zebrafish and inhibition of Notch signaling suppressed formation of excess OPCs"* ([PMID: 22554084](https://pubmed.ncbi.nlm.nih.gov/22554084/)).
- **Drosophila:** *"Pan-neuronal knockdown of the Drosophila ortholog, archipelago, impaired learning and neuronal function"* ([PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/)).

**Cell types involved (CL suggestions):** neural stem/progenitor cells (CL:0000047), radial glial cells (CL:0000681), cerebellar Purkinje cells (CL:0000121), oligodendrocyte precursor cells (CL:0002453), neurons (CL:0000540).

---

## Section 7 — Anatomical Structures Affected

**Organ / system level.** The **central nervous system (UBERON:0001017)** is the primary affected system. Within the brain, affected structures include:
- **Cerebellum (UBERON:0002037)** — hypoplasia, supernumerary fissures (strong mouse and human evidence).
- **Corpus callosum (UBERON:0002336)** — thinning/anomalies (2/6 on MRI in the case series).
- **Cerebral white matter (UBERON:0002316)** — abnormalities.
- **Cerebral cortex (UBERON:0000956)** — functional involvement (epilepsy, intellectual disability).

**Secondary organ / system involvement.** **Digestive system (UBERON:0001007)** — constipation; **respiratory/ENT (UBERON:0001004)** — recurrent infections; **kidney (UBERON:0002113)** — Wilms tumor (nephroblastoma arising from renal blastema). The 2024 CNV cases additionally reported **cardiac and limb** abnormalities and facial dysmorphism ([PMID: 38780184](https://pubmed.ncbi.nlm.nih.gov/38780184/)), and a translocation case showed growth failure and skeletal manifestations ([PMID: 39123068](https://pubmed.ncbi.nlm.nih.gov/39123068/)).

**Tissue / cell level.** Nervous tissue is primarily affected — neural stem/progenitor cells, radial glia, cerebellar Purkinje cells, and oligodendrocyte precursor cells (see CL terms above). In Wilms tumor, renal blastemal (metanephric) cells are the neoplastic population.

**Subcellular level.** Nucleus, nucleolus, cytoplasm, and the SCF ubiquitin-ligase/proteasome machinery (GO:0019005, GO:0005634, GO:0005730).

**Lateralization.** CNS involvement is **bilateral** (developmental, midline, and generalized), not lateralized.

---

## Section 8 — Temporal Development

**Onset.** **Congenital / early childhood.** Structural brain anomalies are present from birth; hypotonia is typically neonatal/infantile; developmental delay becomes evident in infancy/early childhood; epilepsy onset is typically in childhood (e.g., early-onset childhood absence epilepsy in the F-box-variant case; [PMID: 41685408](https://pubmed.ncbi.nlm.nih.gov/41685408/)). Onset pattern is **insidious/developmental**, not acute.

**Progression.** The disorder is **static (non-progressive)** at the neurological level — a neurodevelopmental, not neurodegenerative, condition. Deficits persist lifelong but do not typically worsen mechanistically; developmental trajectories reflect delay rather than regression. Epilepsy may be episodic and is often drug-responsive. Wilms tumor, if it occurs, follows the childhood timeline typical of nephroblastoma.

**Patterns / critical periods.** The critical period of vulnerability is **embryonic/early postnatal neurogenesis**, when FBXW7-dependent control of neural progenitor proliferation and differentiation is essential (mouse neural-lineage deletion is perinatal lethal; [PMID: 21827743](https://pubmed.ncbi.nlm.nih.gov/21827743/)). This also defines the window in which the structural brain phenotype is established, before clinical diagnosis is typically possible.

---

## Section 9 — Inheritance and Population

**Epidemiology.** FBXW7-NDD is **ultra-rare**; precise prevalence/incidence are not established. Fewer than ~50 individuals are reported in the literature across the foundational cohort (35; [PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/)), the 7-individual case series ([PMID: 42432493](https://pubmed.ncbi.nlm.nih.gov/42432493/)), and additional single-case reports. No Orphanet point-prevalence figure was confirmed in this investigation.

**Inheritance.** **Autosomal dominant**, monoallelic. Most cases are **de novo** (e.g., 6/7 de novo in the case series; [PMID: 42432493](https://pubmed.ncbi.nlm.nih.gov/42432493/)), but **inherited** cases from mildly affected or apparently unaffected parents occur ([PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/)).

**Penetrance and expressivity.** Transmission from mildly/unaffected parents and a reported constitutional mosaic variant indicate **incomplete penetrance and variable expressivity**. Expressivity is partly **domain-dependent**:

| Variant class / domain | Representative variant | Phenotype severity | Molecular mechanism |
|---|---|---|---|
| WD40-domain missense | clustered substrate-binding surface variants | More severe (ID, structural brain anomalies) | Reduced substrate-binding affinity ([PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/)) |
| F-box-domain missense | c.926G>C p.(Arg309Pro) | Milder (isolated drug-responsive absence epilepsy, no ID) | Impaired SKP1 binding/SCF assembly ([PMID: 41685408](https://pubmed.ncbi.nlm.nih.gov/41685408/)) |
| Truncating / deletion | nonsense, frameshift, 4q31.3 del | Variable; often significant | Haploinsufficiency ([PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/)) |
| Regulatory / structural | 4q31.3 CNV, t(3;4) position effect | Severe, multisystem (cardiac, limb, skeletal, growth) | Reduced/dysregulated FBXW7 expression ([PMID: 38780184](https://pubmed.ncbi.nlm.nih.gov/38780184/), [PMID: 39123068](https://pubmed.ncbi.nlm.nih.gov/39123068/)) |

The F-box case author's summary captures the contrast: *"unlike prior cases predominantly associated with WD40 domain variants and severe phenotypes, our patient exhibited a much milder clinical presentation consisting of isolated, drug-responsive absence seizures without intellectual disability"* ([PMID: 41685408](https://pubmed.ncbi.nlm.nih.gov/41685408/)).

**Genetic anticipation.** Not applicable (not a repeat-expansion disorder). **Germline mosaicism:** possible (a constitutional mosaic variant has been reported); relevant to recurrence-risk counseling. **Founder effects / consanguinity / carrier frequency:** not applicable — a dominant disorder, predominantly de novo, with no reported founder variants.

**Population demographics.** No ethnic/geographic predilection established; cases are reported worldwide (Europe, North America, Asia, India). **Sex ratio:** no strong skew documented (case series: 5 male, 2 female — too small to infer). **Age distribution:** primarily identified in pediatric populations.

---

## Section 10 — Diagnostics

**Diagnostic approach — molecular.** Diagnosis is genetic. **Trio exome sequencing (WES) or genome sequencing (WGS)** is first-line and detects SNVs/indels; because many cases are de novo, trio testing maximizes yield. **Chromosomal microarray (CMA)** detects 4q31.3 deletions/duplications ([PMID: 38780184](https://pubmed.ncbi.nlm.nih.gov/38780184/)). **Karyotyping / long-read WGS** is needed for cryptic balanced rearrangements and position effects ([PMID: 39123068](https://pubmed.ncbi.nlm.nih.gov/39123068/)). Single-gene *FBXW7* testing is appropriate when the phenotype is strongly suggestive. The gene appears on broad intellectual-disability gene panels used in neurodevelopmental cohorts ([PMID: 38114583](https://pubmed.ncbi.nlm.nih.gov/38114583/)).

**Clinical/laboratory tests and biomarkers.** There is **no specific biochemical biomarker** and **no newborn-screening test**. Research assays (e.g., CYCLIN E1/E2 turnover in patient cells, lymphoblast *FBXW7* expression) support variant interpretation but are not routine. Immunohistochemistry can show mosaic/loss of FBXW7 protein in tumor tissue.

**Imaging / electrophysiology.** **Brain MRI** characterizes cerebellar, corpus callosum, and white-matter anomalies (though it is normal in a substantial minority — 4/6 in the case series; [PMID: 42432493](https://pubmed.ncbi.nlm.nih.gov/42432493/)). **EEG** characterizes seizures (e.g., generalized spike-wave in absence epilepsy). **Renal/abdominal ultrasound** is used for tumor surveillance.

**Clinical criteria / differential diagnosis.** There are no formal consensus diagnostic criteria beyond molecular confirmation in a compatible phenotype. Differential diagnosis includes other monogenic intellectual-disability/hypotonia syndromes and, given the NOTCH/MYC axis, syndromes affecting the same pathway (e.g., *MYCN*-related megalencephaly-polydactyly, which acts through FBXW7-dependent MYCN degradation; [PMID: 37710961](https://pubmed.ncbi.nlm.nih.gov/37710961/)).

**Screening.** Cascade testing of at-risk relatives after a proband variant is identified; tumor surveillance (below) functions as secondary prevention.

---

## Section 11 — Outcome / Prognosis

**Survival / mortality.** No disease-specific mortality or survival data are available. The neurodevelopmental disorder itself is **not inherently life-limiting**; life expectancy is most influenced by severity of complications (e.g., epilepsy control, aspiration/infection risk) and by Wilms tumor outcomes (nephroblastoma generally has favorable survival with modern therapy, though this depends on stage and histology).

**Morbidity / function.** The principal burden is **chronic neurodevelopmental disability** — intellectual disability, language impairment, hypotonia, and epilepsy — with lifelong impact on independence, education, and communication. Morbidity is highly variable, from near-normal functioning (mild F-box variants) to severe multisystem involvement (structural/regulatory lesions).

**Disease course / complications.** Complications include epilepsy, GI dysfunction (constipation), recurrent respiratory/ENT infections, and the Wilms tumor risk. Recovery is not expected (static developmental disorder), but supportive therapy improves functional outcomes.

**Prognostic factors.** The strongest prognostic indicator identified is **variant/domain type** — F-box-domain variants portend milder outcomes than WD40-domain variants and structural/regulatory lesions. Presence of structural brain anomalies, early refractory epilepsy, and multisystem CNV/translocation lesions predict more severe courses. No validated molecular prognostic biomarker exists.

---

## Section 12 — Treatment

**No targeted or disease-modifying therapy exists.** Management is **symptomatic and supportive**, individualized to the phenotype.

| Domain | Intervention | NCIT suggestion |
|---|---|---|
| Developmental | Early intervention — physical, occupational, speech therapy | NCIT:C15265 (Rehabilitation Therapy) |
| Epilepsy | Anti-seizure medication (absence seizures often drug-responsive; [PMID: 41685408](https://pubmed.ncbi.nlm.nih.gov/41685408/)) | NCIT:C264 (Anticonvulsant Agent) |
| Gastrointestinal | Management of constipation (diet, laxatives) | NCIT:C258 (Laxative) |
| Infections | Treatment/prevention of recurrent respiratory/ENT infections | NCIT antimicrobial classes as indicated |
| Oncologic | Wilms tumor surveillance; standard nephroblastoma therapy if tumor arises | NCIT:C17024 (Screening); NCIT:C15431 (Antineoplastic therapy) |
| Behavioral | Behavioral/psychological support | NCIT:C15277 (Behavioral Therapy) |
| Counseling | Genetic counseling | NCIT:C15417 (Genetic Counseling) |

**Pharmacogenomics / advanced therapeutics / surgery.** No pharmacogenomic guidance, gene therapy, cell therapy, RNA therapy, or disease-specific surgical intervention is established. Surgery is relevant only for Wilms tumor (nephrectomy) or complication management.

**Experimental directions.** Because the disorder is driven by substrate accumulation in the NOTCH/MYC/CYCLIN E axis, pathway-targeted strategies (e.g., NOTCH inhibition) are mechanistically plausible but **entirely preclinical/unproven** for this germline disorder. In cancer contexts, FBXW7 loss is **synthetic lethal with CDC7 inhibition** ([PMID: 37866880](https://pubmed.ncbi.nlm.nih.gov/37866880/)) — relevant to tumor therapeutics, not to the neurodevelopmental phenotype.

---

## Section 13 — Prevention

**Primary prevention.** Not possible for de novo cases. For families with a known variant, reproductive options include **prenatal diagnosis** and **preimplantation genetic testing (PGT-M)**.

**Secondary prevention — tumor surveillance.** This is the most actionable prevention measure. Given the two-hit Wilms tumor risk, **renal/abdominal ultrasound surveillance** is recommended for individuals with constitutional/germline *FBXW7* pathogenic variants: *"Wilms tumor screening should be considered in individuals with constitutional or germline pathogenic variants in FBXW7 and associated neurodevelopmental syndrome"* ([PMID: 38169111](https://pubmed.ncbi.nlm.nih.gov/38169111/)). Surveillance protocols typically follow established cancer-predisposition guidelines (e.g., periodic ultrasound through early childhood).

**Tertiary prevention.** Proactive management of epilepsy, aspiration/infection risk, constipation, and developmental support to prevent secondary complications and optimize function.

**Counseling and screening.** **Genetic counseling** addresses autosomal dominant inheritance, incomplete penetrance, variable (domain-dependent) expressivity, de novo vs inherited/mosaic origin, recurrence risk, and reproductive options. **Cascade genetic testing** identifies at-risk relatives who may warrant tumor surveillance.

**Immunization / public health / environmental.** No disease-specific immunization or public-health/environmental prevention applies (Mendelian disorder).

---

## Section 14 — Other Species / Natural Disease

**Taxonomy and orthologs.** FBXW7 is deeply evolutionarily conserved. Orthologs:
- **Mouse** (*Mus musculus*, NCBI Taxon 10090): *Fbxw7* / *Fbw7* (NCBI Gene 50754)
- **Zebrafish** (*Danio rerio*, NCBI Taxon 7955): *fbxw7*
- **Fruit fly** (*Drosophila melanogaster*, NCBI Taxon 7227): *archipelago* (*ago*)
- **Nematode** (*Caenorhabditis elegans*, NCBI Taxon 6239): *sel-10*

**Natural disease / veterinary relevance.** No naturally occurring FBXW7-NDD-equivalent disorder in companion animals or wildlife is documented in OMIA within this investigation. *FBXW7* is studied experimentally across species but is not a recognized spontaneous veterinary disease.

**Comparative biology / evolutionary conservation.** The disease mechanism — loss of FBXW7 function → NOTCH/substrate accumulation → neural precursor dysregulation — is **conserved across vertebrates and invertebrates**, as demonstrated by the mouse cerebellar, zebrafish spinal-cord, and *Drosophila* learning phenotypes (Section 6; [PMID: 21827743](https://pubmed.ncbi.nlm.nih.gov/21827743/), [PMID: 22554084](https://pubmed.ncbi.nlm.nih.gov/22554084/), [PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/)). *"fbxw7 … encodes the substrate recognition component of a ubiquitin ligase that targets Notch and other proteins for degradation"* ([PMID: 22554084](https://pubmed.ncbi.nlm.nih.gov/22554084/)).

**Transmission.** Not applicable (non-infectious, non-zoonotic).

---

## Section 15 — Model Organisms

| Model | System / allele | Key phenotype | Human relevance | Reference |
|---|---|---|---|---|
| **Mouse** (cerebellar conditional KO, *Fbw7^ΔCb*) | Mammalian, conditional knockout | ↓Cerebellar size, ↓Purkinje cells, defective axonal arborisation, supernumerary fissures, aberrant progenitor migration; ↑Notch1 & p-c-Jun; rescued by c-Jun deletion | Recapitulates human cerebellar anomalies; confirms substrate-accumulation mechanism | [PMID: 21827743](https://pubmed.ncbi.nlm.nih.gov/21827743/) |
| **Mouse** (neural-lineage KO) | Mammalian, conditional knockout | Perinatal lethal; controls NSC differentiation/apoptosis via Notch & c-Jun | Establishes essential developmental role | [PMID: 21827743](https://pubmed.ncbi.nlm.nih.gov/21827743/) |
| **Zebrafish** (*fbxw7* mutant, vu56) | Vertebrate, germline mutant | Elevated Notch in spinal-cord precursors; excess oligodendrocyte progenitors; suppressible by Notch inhibition | Demonstrates Notch-dependent precursor-fate defect | [PMID: 22554084](https://pubmed.ncbi.nlm.nih.gov/22554084/) |
| **Drosophila** (*archipelago* knockdown) | Invertebrate, pan-neuronal RNAi | Impaired learning and neuronal function | Links ortholog loss to behavioral/cognitive deficit | [PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/) |
| **Cultured cells** (recombinant variant expression) | In vitro | Impaired CYCLIN E1/E2 turnover with patient missense variants | Functional validation of pathogenicity | [PMID: 35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/) |
| **MYCN gain-of-function mouse** | Mammalian | Megalencephaly/polydactyly via reduced FBXW7-mediated MYCN degradation | Illustrates FBXW7–substrate axis in brain growth (reciprocal direction) | [PMID: 37710961](https://pubmed.ncbi.nlm.nih.gov/37710961/) |

**Genetic model types available.** Knockout (constitutive embryonic-lethal), **conditional/tissue-specific knockout** (cerebellar, neural-lineage), germline mutant (zebrafish), and RNAi knockdown (Drosophila). Humanized/knock-in patient-variant models are not yet established but are a logical next step.

**Recapitulation and limitations.** Models faithfully reproduce the **cerebellar/neural-precursor and NOTCH/c-Jun-accumulation** core mechanism. Limitations: constitutive null is embryonic/perinatal lethal, requiring conditional approaches; models do not fully capture the human cognitive/behavioral spectrum, the domain-dependent expressivity, or the two-hit Wilms-tumor predisposition in a germline-heterozygous context. iPSC-derived neural organoids carrying patient variants would address human-specific developmental questions.

---

## Mechanistic Model / Interpretation

```
  Germline monoallelic FBXW7 lesion
  (truncating | WD40 missense | F-box missense | 4q31.3 CNV | position effect)
                 |
   ┌─────────────┼───────────────┬───────────────────┐
   ▼             ▼               ▼                   ▼
 ↓dosage     ↓substrate       ↓SCF assembly     ↓/dysreg. expression
 (haploinsuff) binding(WD40)   (SKP1, F-box)    (regulatory/TAD)
   └─────────────┴───────────────┴───────────────────┘
                 ▼
   ↓ SCF(FBXW7) ubiquitination of phosphodegron substrates
                 ▼
   ↑ NOTCH1, ↑CYCLIN E1/2, ↑c-Jun, ↑c-MYC, ↑mTOR, ↑BRAF, ↑MCL-1
                 ▼
   Aberrant NOTCH / MYC / c-Jun / mTOR signaling
                 ▼
   Dysregulated neural stem/progenitor proliferation,
   differentiation, migration, apoptosis
         │                                   │
         ▼ (CNS)                             ▼ (kidney + somatic 2nd hit)
  Cerebellar hypoplasia, corpus callosum/         Biallelic FBXW7 loss
  white-matter anomalies, abnormal neuronal        → Wilms tumor
  function
         ▼
  GDD, intellectual disability, hypotonia,
  epilepsy, behavioral difficulties, GI issues
```

The unifying theme is that **FBXW7 is a dosage-sensitive negative regulator of growth-promoting signaling in neural progenitors**. Any lesion that lowers functional FBXW7 — whether by reducing protein amount (truncating/deletion/position effect), crippling substrate capture (WD40 missense), or preventing ligase assembly (F-box missense) — converges on the same downstream outcome of **substrate accumulation and signaling excess**. The degree of residual function plausibly explains the phenotypic gradient, with F-box assembly-defect variants retaining more activity (milder phenotype) than WD40 substrate-binding variants. The same loss-of-function biology, when completed by a somatic second hit in renal tissue, explains the Wilms tumor predisposition — making FBXW7-NDD a rare example of a disorder that is simultaneously a neurodevelopmental syndrome and a cancer-predisposition syndrome.

---

## Evidence Base

| PMID | Study type | Contribution |
|---|---|---|
| [35395208](https://pubmed.ncbi.nlm.nih.gov/35395208/) | Human cohort (n=35) + in vitro + Drosophila | **Foundational paper.** Defines core phenotype, variant spectrum, WD40 structural modeling, CYCLIN E1/E2 functional assay, Drosophila learning deficit |
| [42432493](https://pubmed.ncbi.nlm.nih.gov/42432493/) | Human case series (n=7, 2026) | Phenotype frequencies (hypotonia 100%, GDD/language 86%, ID 57%, epilepsy 57%); extracerebral features; expanding variability |
| [42111496](https://pubmed.ncbi.nlm.nih.gov/42111496/) | Review | Clinical spectrum, molecular mechanisms, and tumor predisposition overview |
| [21827743](https://pubmed.ncbi.nlm.nih.gov/21827743/) | Mouse conditional KO | Cerebellar phenotype; Notch1/c-Jun accumulation; c-Jun rescue; NSC role |
| [22554084](https://pubmed.ncbi.nlm.nih.gov/22554084/) | Zebrafish mutant | Notch-dependent neural precursor fate defect; conserved FBXW7 function |
| [35515121](https://pubmed.ncbi.nlm.nih.gov/35515121/) | Review | FBXW7 substrate network (c-MYC, mTOR, MCL-1, Notch, cyclin E) in ubiquitin-proteasome system |
| [35346215](https://pubmed.ncbi.nlm.nih.gov/35346215/) | Review | Phosphodegron-dependent ubiquitination mechanism; LoF in cancer |
| [38169111](https://pubmed.ncbi.nlm.nih.gov/38169111/) | Human case report | Germline FBXW7 → NDD + Wilms tumor; surveillance recommendation |
| [39414990](https://pubmed.ncbi.nlm.nih.gov/39414990/) | Human case report | Somatic second-hit in tumor DNA; two-hit model for Wilms tumor |
| [41685408](https://pubmed.ncbi.nlm.nih.gov/41685408/) | Human case report | F-box-domain variant → mild phenotype; SKP1/SCF-assembly mechanism |
| [38780184](https://pubmed.ncbi.nlm.nih.gov/38780184/) | Human case report + Hi-C | 4q31.3 regulatory CNVs; TAD/dosage mechanism |
| [39123068](https://pubmed.ncbi.nlm.nih.gov/39123068/) | Human case report | Translocation position effect reduces FBXW7 expression (haploinsufficiency) |
| [37710961](https://pubmed.ncbi.nlm.nih.gov/37710961/) | Human + mouse | MYCN GoF escapes FBXW7 degradation → megalencephaly; validates FBXW7–substrate brain axis |
| [37866880](https://pubmed.ncbi.nlm.nih.gov/37866880/) | CRISPR screen (cancer) | FBXW7 loss synthetic-lethal with CDC7 inhibition (therapeutic concept) |
| [38114583](https://pubmed.ncbi.nlm.nih.gov/38114583/) | Human cohort (India) | FBXW7 among de novo ID genes on neurodevelopmental panels |

**Evidence source distribution:** The clinical phenotype rests on **human cohort and case-series data**; the mechanism rests on **model-organism (mouse, zebrafish, Drosophila) and in vitro** data plus human functional/structural modeling; the tumor link rests on **human case reports with molecular tumor analysis**.

---

## Limitations and Knowledge Gaps

1. **Small sample sizes.** The entire literature comprises <50 reported individuals. Phenotype frequencies (from a 7-person series) have wide confidence intervals and may not generalize.
2. **Penetrance and prevalence unquantified.** True population prevalence, incidence, penetrance, and the proportion of inherited vs de novo cases are not precisely known.
3. **Genotype–phenotype correlation is preliminary.** The F-box-vs-WD40 severity contrast rests largely on single cases; a systematic domain-stratified analysis is lacking.
4. **No validated biomarker or episignature.** Diagnosis is purely molecular; no biochemical marker, imaging signature, or methylation episignature aids diagnosis or prognosis.
5. **Tumor risk magnitude unknown.** The absolute lifetime Wilms tumor risk (and whether other tumors occur) is unquantified, so surveillance intensity/duration is not evidence-based.
6. **Missing ontology/registry identifiers.** OMIM phenotype number, Orphanet number, and ICD codes were not confirmed in this investigation and need direct verification.
7. **Mechanistic gaps in human brain.** Human-specific neurodevelopmental consequences are inferred from animal models; iPSC/organoid data are absent.
8. **No therapeutics evaluated.** No clinical trials; pathway-targeted strategies are purely hypothetical.

---

## Proposed Follow-up Experiments / Actions

1. **Build a prospective patient registry** to quantify penetrance, phenotype frequencies, natural history, and absolute Wilms tumor risk — directly informing surveillance guidelines.
2. **Systematic domain-stratified genotype–phenotype analysis** (F-box vs WD40 vs truncating vs regulatory) across all reported variants, with standardized functional assays (substrate turnover, SCF assembly) to test the residual-function–severity hypothesis quantitatively.
3. **Patient-derived iPSC neural organoids** carrying representative variants to measure NOTCH/CYCLIN E/c-Jun accumulation and progenitor-fate defects in a human developmental context.
4. **Develop a DNA-methylation episignature** from patient blood to provide a diagnostic/variant-classification aid.
5. **Define evidence-based tumor surveillance** (ultrasound frequency, age range) via multicenter data pooling, modeled on existing cancer-predisposition protocols.
6. **Verify and register ontology identifiers** (OMIM, Orphanet, ICD-11, HPO annotations with frequencies) for knowledge-base completeness.
7. **Preclinical pathway-rescue studies** (e.g., NOTCH or c-Jun modulation) in conditional mouse and zebrafish models to assess whether developmental defects are reversible within critical windows.

---

## Consensus Answer

FBXW7-Related Neurodevelopmental Disorder (MONDO:0859280) is a rare autosomal dominant Mendelian syndrome caused by monoallelic loss-of-function variants (truncating, WD40- or F-box-domain missense, deletions, or 4q31.3 regulatory lesions) in *FBXW7*, the substrate-recognition subunit of the SCF E3 ubiquitin ligase; impaired ubiquitination and degradation of substrates such as NOTCH1, CYCLIN E1/2, and c-Jun dysregulates neural progenitor proliferation and differentiation, producing global developmental delay, intellectual disability, hypotonia, epilepsy, variable cerebellar/corpus-callosum/white-matter anomalies, and gastrointestinal issues. The disorder shows incomplete penetrance and variable, partly domain-dependent expressivity (F-box variants milder than WD40), carries a Wilms-tumor predisposition via a germline-plus-somatic two-hit mechanism warranting renal ultrasound surveillance, and is managed supportively with no targeted therapy currently available.


## Artifacts

- [OpenScientist final report](FBXW7-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](FBXW7-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 27 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001252` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hypotonia**
- `HP:0001263` (1 mention) - the report calls it "Clinical sign"; HP calls it **Global developmental delay**
- `HP:0000750` (1 mention) - the report calls it "Clinical sign"; HP calls it **Delayed speech and language development**
- `HP:0001249` (1 mention) - the report calls it "Clinical sign"; HP calls it **Intellectual disability**
- `HP:0001273` (1 mention) - the report calls it "Imaging/structural"; HP calls it **Abnormal corpus callosum morphology**
- `HP:0001317` (1 mention) - the report calls it "Imaging/structural"; HP calls it **Abnormal cerebellum morphology**
- `HP:0002500` (1 mention) - the report calls it "Imaging/structural"; HP calls it **Abnormal cerebral white matter morphology**
- `HP:0002019` (1 mention) - the report calls it "Symptom (GI)"; HP calls it **Constipation**
- `HP:0002788` (1 mention) - the report calls it "Clinical sign"; HP calls it **Recurrent upper respiratory tract infections**
- `NCIT:C15265` (1 mention) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Kidney Transplantation**
- `NCIT:C258` (1 mention) - the report calls it "Laxative"; NCIT calls it **Antibiotic**
- `NCIT:C15277` (1 mention) - the report calls it "Behavioral Therapy"; NCIT calls it **Mastectomy**
- `NCIT:C15417` (1 mention) - the report calls it "Genetic Counseling"; NCIT calls it **Randomized Clinical Trial**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000708` (1 mention) - the report calls it "Behavioral"; HP calls it **Atypical behavior**, and lists "Behavioral changes" among its other names
- `HP:0002667` (1 mention) - the report calls it "Neoplasm"; HP calls it **Nephroblastoma**
- `GO:0008285` (1 mention) - the report calls it "negative regulation of cell proliferation"; GO calls it **negative regulation of cell population proliferation**, and lists "negative regulation of cell proliferation" among its other names
- `UBERON:0002316` (1 mention) - the report calls it "Cerebral white matter"; UBERON calls it **white matter**, and lists "neuronal white matter" among its other names