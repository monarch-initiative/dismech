---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-04T23:54:24.381188'
end_time: '2026-11-05T00:49:18.267476'
duration_seconds: 3293.89
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hypomagnesemia, Seizures, and Intellectual Disability 1
  mondo_id: MONDO:0020787
  category: Mendelian
  causal_genes: CNNM2
  omim_id: OMIM:616418
  synonyms: HOMGSMR1; CNNM2-related hypomagnesemia
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
citation_count: 19
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 22
  on_topic: 11
  off_topic: 1
  off_topic_references:
  - PMID:27856537
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 33
  verified: 30
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 7
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0020787
    reported_labels:
    - MONDO
    ontology_label: hypomagnesemia, seizures, and impaired intellectual development
      1
  - term_id: HP:0002917
    reported_labels:
    - Very frequent (core; occasionally absent)
    ontology_label: Hypomagnesemia
  - term_id: HP:0001250
    reported_labels:
    - Frequent (core)
    ontology_label: Seizure
  - term_id: HP:0000750
    reported_labels:
    - Common
    ontology_label: Delayed speech and language development
  - term_id: HP:0001270
    reported_labels:
    - Common
    ontology_label: Motor delay
  - term_id: HP:0002011
    reported_labels:
    - Subset (can occur w/o hypomagnesemia)
    ontology_label: Morphological central nervous system abnormality
  - term_id: HP:0002353
    reported_labels:
    - Common with seizures
    ontology_label: EEG abnormality
  - term_id: HP:0001410
    reported_labels:
    - Single reports
    ontology_label: Decreased liver function
  labels_variant: 2
  obsolete_terms:
  - term_id: NCIT:C29236
    ontology_label: Murine Monoclonal Antibody (LYM-1)
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hypomagnesemia_Seizures_And_Intellectual_Disability_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hypomagnesemia_Seizures_And_Intellectual_Disability_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypomagnesemia, Seizures, and Intellectual Disability 1
- **MONDO ID:** MONDO:0020787 (if available)
- **Causal gene(s):** CNNM2
- **OMIM:** OMIM:616418
- **Synonyms:** HOMGSMR1; CNNM2-related hypomagnesemia
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Hypomagnesemia, Seizures, and Intellectual Disability 1** covering all of the
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

# Hypomagnesemia, Seizures, and Intellectual Disability 1 (HOMGSMR1): A Comprehensive Disease Characterization

**Disease:** Hypomagnesemia, Seizures, and Intellectual Disability 1 (HOMGSMR1 / HSMR)
**Causal gene:** **CNNM2** (Cyclin M2; cyclin and CBS domain divalent metal cation transport mediator 2; HGNC:2020; NCBI Gene 54805; locus 10q24.32)
**Identifiers:** MONDO:0020787 · OMIM:616418 · Orphanet (hypomagnesemia–seizures group)
**Category:** Mendelian monogenic disorder

> **Evidence-source key:** [H] human clinical/genetic · [M] model organism · [V] in vitro/biochemical/structural · [C] computational. PMIDs cited throughout. This report concerns the **CNNM2**-related disorder, *not* the similarly named TRPM6- or CNNM4-related magnesium disorders.

---

## Summary

Hypomagnesemia, Seizures, and Intellectual Disability 1 (HOMGSMR1) is a rare Mendelian neurodevelopmental and renal electrolyte disorder caused by pathogenic variants in **CNNM2** (Cyclin M2), a magnesium-handling protein expressed on the **basolateral membrane of the renal distal convoluted tubule (DCT)**. CNNM2 contains intracellular **CBS/Bateman domains** that sense cytosolic **Mg-ATP**, and it regulates cellular Mg²⁺ flux—both basolateral extrusion in the kidney and, in cells, uptake through the TRPM7 Mg²⁺-permeable channel. Loss of CNNM2 function impairs renal Mg²⁺ reabsorption (producing renal Mg²⁺ wasting and hypomagnesemia) and disrupts brain development, yielding the disease's core triad: **hypomagnesemia, seizures, and intellectual disability/developmental delay** [H, [PMID: 21397062](https://pubmed.ncbi.nlm.nih.gov/21397062/); [PMID: 24699222](https://pubmed.ncbi.nlm.nih.gov/24699222/)].

The disorder shows an **allelic-dose (genotype–phenotype) gradient**. Heterozygous, frequently *de novo*, missense or truncating variants cause the classic autosomal-dominant disorder with moderate intellectual disability; biallelic/recessive variants cause a more severe phenotype with brain malformation and severe intellectual disability, and in some cases the neurological phenotype occurs even without overt hypomagnesemia [H, [PMID: 24699222](https://pubmed.ncbi.nlm.nih.gov/24699222/); [PMID: 34490037](https://pubmed.ncbi.nlm.nih.gov/34490037/)]. Population-genetics constraint data strongly reinforce a haploinsufficiency mechanism: in gnomAD v2.1.1, CNNM2 is extremely loss-of-function intolerant (pLI ≈ 1.0, LOEUF = 0.29, missense Z = 5.77).

This report integrates five convergent layers of evidence—human genetics, population genetics, structural biology, cell biology, and animal models—into a coherent mechanistic model. Management is supportive: **oral/intravenous/subcutaneous magnesium supplementation** plus **antiseizure therapy**; no curative or gene-directed therapy exists. The disorder is ultra-rare (only ~24 pediatric HSMR cases reported by 2022; largest cohort ~34), which constrains firm epidemiological, prognostic, and treatment-outcome estimates.

---

## Key Findings

1. **CNNM2 is the causal gene.** Positional/candidate cloning in two unrelated families with dominant hypomagnesemia identified CNNM2 variants [[PMID: 21397062](https://pubmed.ncbi.nlm.nih.gov/21397062/)]: *"we identified CNNM2 as a gene involved in renal Mg(2+) handling in patients of two unrelated families with unexplained dominant hypomagnesemia."* CNNM2 localizes to the basolateral membrane of distal tubular segments.
2. **The CBS/Bateman domains sense Mg-ATP and are essential for Mg²⁺ handling.** CBS-domain deletion abolishes Mg²⁺ efflux; a disease-associated CBS substitution *"abrogates Mg(2+) efflux"* and ATP binding [[PMID: 24706765](https://pubmed.ncbi.nlm.nih.gov/24706765/)].
3. **A structural allosteric switch is disrupted by T568I.** Nucleotide binding triggers a *"twisted towards a flat disc-like"* CBS-module conformation; the dominant mutation **T568I mimics the nucleotide-bound state** [[PMID: 25184538](https://pubmed.ncbi.nlm.nih.gov/25184538/)].
4. **CNNM2 regulates TRPM7-mediated Mg²⁺ uptake.** CNNM2 *"increases cellular Mg2+ uptake in HEK293 cells … through regulation of the Mg(2+)-permeable cation channel TRPM7"*; mutants fail to do so [[PMID: 24699222](https://pubmed.ncbi.nlm.nih.gov/24699222/)].
5. **Allelic-dose genotype–phenotype gradient.** *"patients with recessive CNNM2 mutations suffer from brain malformations and severe intellectual disability,"* whereas heterozygous *de novo* missense patients have moderate disability [[PMID: 24699222](https://pubmed.ncbi.nlm.nih.gov/24699222/)].
6. **CNNM2 is extremely LoF-intolerant** (gnomAD v2.1.1: pLI ≈ 1.0, LOEUF = 0.29, 12 observed vs 66.9 expected LoF, mis_Z = 5.77), supporting haploinsufficiency [C].
7. **Animal models recapitulate both axes.** Mouse *Cnnm2* KO is embryonic-lethal (homozygous) and hypomagnesemic (heterozygous/kidney-specific); zebrafish knockdown produces disturbed brain development [[PMID: 33859252](https://pubmed.ncbi.nlm.nih.gov/33859252/); [PMID: 28033128](https://pubmed.ncbi.nlm.nih.gov/28033128/); [PMID: 24699222](https://pubmed.ncbi.nlm.nih.gov/24699222/)].

---

## 1. Disease Information

**Overview.** HOMGSMR1 (also "Hypomagnesemia, Seizures, and Mental Retardation syndrome," HSMR) is a rare autosomal-dominant (occasionally recessive) Mendelian neurodevelopmental and renal-electrolyte disorder. Loss-of-function/dominant-negative variants in **CNNM2** impair basolateral Mg²⁺ extrusion in the renal DCT, producing renal Mg²⁺ wasting (serum Mg²⁺ <0.7 mmol/L) combined with seizures and intellectual disability/developmental delay [H, [PMID: 21397062](https://pubmed.ncbi.nlm.nih.gov/21397062/); [PMID: 33600043](https://pubmed.ncbi.nlm.nih.gov/33600043/)].

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0020787 |
| OMIM (phenotype) | 616418 |
| OMIM (gene) | 607803 |
| Gene / HGNC | CNNM2 / HGNC:2020 |
| NCBI Gene | 54805 |
| Ensembl | ENSG00000148842 (canonical ENST00000369878) |
| UniProt | Q9H8M5 |
| Locus | 10q24.32 (chr10:102,918,294–103,090,222, GRCh38) |
| ICD-10 / ICD-11 | E83.4 / 5C64.4 (disorders of magnesium metabolism — no CNNM2-specific code) |
| MeSH (closest) | Magnesium Deficiency (D008275); Intellectual Disability (D008607); Seizures (D012640) |

**Synonyms:** HOMGSMR1; HSMR syndrome; CNNM2-related hypomagnesemia; Hypomagnesemia, seizures, and impaired intellectual development 1; Cyclin M2 deficiency.

**Information source:** A mix of **individual-patient case reports and small cohorts** (landmark multi-family studies Stuiver 2011 [PMID 21397062], Arjona 2014 [PMID 24699222], the largest cohort Franken 2021 [PMID 33600043]) plus mechanistic/biochemical/animal studies—and **aggregated disease-level resources** (OMIM, Orphanet, gnomAD). There is no large population registry or EHR-scale dataset.

---

## 2. Etiology

**Primary cause (genetic).** Pathogenic variants in **CNNM2**—there is no infectious or environmental cause. The gene was originally identified in two unrelated families with dominant hypomagnesemia [H, [PMID: 21397062](https://pubmed.ncbi.nlm.nih.gov/21397062/)].

**Genetic risk factors.** Causal variants are heterozygous (frequently *de novo*) missense and truncating variants, with biallelic variants in severe recessive forms (see §4, §9). The 10q24 locus also carries GWAS signals for serum Mg²⁺ concentration and for schizophrenia (zebrafish *cnnm2* mutants show altered forebrain development, [PMID 30929901])—these are quantitative-trait/susceptibility associations distinct from the Mendelian disorder. CNNM2's extreme LoF intolerance (pLI ≈ 1.0) indicates heterozygous LoF alleles are under strong negative selection.

**Environmental / lifestyle factors.** None causal. Acquired hypomagnesemia (not HOMGSMR1) is driven by alcoholism, type-2 diabetes, proton-pump inhibitors, calcineurin inhibitors, and thiazide diuretics [H, [PMID: 38871680](https://pubmed.ncbi.nlm.nih.gov/38871680/)]; these can exacerbate but not cause the syndrome.

**Protective factors.** No validated protective alleles. Dietary/supplemental Mg²⁺ is therapeutically mitigating but does not fully correct the neurological phenotype.

**Gene–environment interactions.** Dietary Mg²⁺ intake and Mg²⁺-wasting medications modulate the degree of hypomagnesemia on top of the genetic lesion; no formal GxE model exists for CNNM2.

---

## 3. Phenotypes

Core triad plus associated features (frequencies qualitative; cohorts small, N≈24–34) [H, [PMID: 35170241](https://pubmed.ncbi.nlm.nih.gov/35170241/); [PMID: 33600043](https://pubmed.ncbi.nlm.nih.gov/33600043/)].

| Phenotype | Type | Onset | Frequency | HPO term |
|---|---|---|---|---|
| Hypomagnesemia (serum Mg²⁺ <0.7 mmol/L) | Lab abnormality | Neonatal/infantile–childhood | Very frequent (core; occasionally absent) | HP:0002917 |
| Seizures / epilepsy (can be intractable) | Clinical sign | Neonatal–infancy | Frequent (core) | HP:0001250 |
| Intellectual disability / developmental delay | Behavioral/cognitive | Childhood | Frequent (core) | HP:0001249; HP:0001263 |
| Speech / language delay | Behavioral | Childhood | Common | HP:0000750 |
| Motor impairment / delay | Clinical sign | Infancy–childhood | Common | HP:0001270 |
| Brain malformation | Imaging | Congenital | Subset (can occur w/o hypomagnesemia) | HP:0002011 |
| EEG abnormalities | Electrophysiology | Variable | Common with seizures | HP:0002353 |
| Congenital heart disease (ASD), sinus arrhythmia | Clinical sign | Congenital | Reported subset | HP:0001631; HP:0011675 |
| Hepatic (liver function) dysfunction | Lab abnormality | Variable | Single reports | HP:0001410 |

Key quotes: *"only 24 children with HSMR have been reported, mainly manifested as hypomagnesemia, mental retardation, seizures, and language and motor impairment"* [[PMID: 35170241](https://pubmed.ncbi.nlm.nih.gov/35170241/)]. Neurological disease can occur **without** overt hypomagnesemia: *"CNNM2 Mutations Cause Damaged Brain Development and Intractable Epilepsy in a Patient Without Hypomagnesemia"* [[PMID: 34490037](https://pubmed.ncbi.nlm.nih.gov/34490037/)].

**Severity/progression.** Variable expressivity; seizures may be intractable; intellectual disability is typically stable (non-progressive) but lifelong; hypomagnesemia is chronic.

**Quality-of-life impact.** Intellectual disability, epilepsy, and speech/motor impairment substantially reduce daily functioning, independence, and schooling; chronic Mg²⁺ supplementation causes GI side effects (diarrhea). No disease-specific EQ-5D/SF-36 data exist.

---

## 4. Genetic / Molecular Information

**Causal gene.** **CNNM2** (OMIM 607803; HGNC:2020; UniProt Q9H8M5) encodes Cyclin M2, a ~875-aa integral membrane protein with an extracellular N-terminus and intracellular C-terminus; the ~64-aa N-terminal signal peptide is cleaved and the protein is N-glycosylated at Asn-112, stabilizing it at the plasma membrane [V, [PMID: 22399287](https://pubmed.ncbi.nlm.nih.gov/22399287/)]. It contains a DUF21 transmembrane domain, a cytosolic **CBS/Bateman module** (residues ~429–584) that binds Mg-ATP and undergoes a twisted→flat switch [V, [PMID: 25184538](https://pubmed.ncbi.nlm.nih.gov/25184538/)], and a cyclic-nucleotide-binding-homology domain. Two isoforms (CNNM2a/CNNM2b) heterodimerize [V, [PMID: 22399287](https://pubmed.ncbi.nlm.nih.gov/22399287/)].

**Pathogenic variants.** Predominantly **heterozygous *de novo* missense or truncating**, with biallelic genotypes in severe cases:

| Variant (cDNA / protein) | Type | Classification | Inheritance | Reference |
|---|---|---|---|---|
| p.Thr568Ile (T568I) | Missense (CBS/Bateman) | Pathogenic (founding dominant variant) | Dominant | [PMID: 25184538](https://pubmed.ncbi.nlm.nih.gov/25184538/) |
| c.1448delT (p.Val483GlyfsTer29) | Frameshift/truncating | Pathogenic (ACMG), *de novo* | Dominant | [PMID: 37532502](https://pubmed.ncbi.nlm.nih.gov/37532502/) |
| c.566A>G (p.Tyr189Cys) | Missense | Pathogenic (ACMG), *de novo*, parents WT | Dominant | [PMID: 35170241](https://pubmed.ncbi.nlm.nih.gov/35170241/) |
| p.E298del | In-frame deletion | Novel, pathogenic (functional study) | — | [PMID: 40612795](https://pubmed.ncbi.nlm.nih.gov/40612795/) |
| p.P360R | Missense | Novel, pathogenic (functional study) | — | [PMID: 40612795](https://pubmed.ncbi.nlm.nih.gov/40612795/) |
| 11 novel variants (cohort) | Mixed | Across 9 sporadic + 2 families | Mixed | [PMID: 33600043](https://pubmed.ncbi.nlm.nih.gov/33600043/) |

**Classification (ACMG/AMP):** pathogenic/likely pathogenic, commonly using PVS1 (truncating), PS2 (*de novo*), PM2 (absent/rare in gnomAD), PP4 (phenotype match) [H, [PMID: 37532502](https://pubmed.ncbi.nlm.nih.gov/37532502/)].

**Allele frequency / constraint (gnomAD v2.1.1, queried via GraphQL API):** pathogenic variants are absent/ultra-rare (PM2-supporting). CNNM2 is extremely LoF-intolerant: **pLI = 0.99999998 (≈1.0)**, **oe_lof = 0.179 (90% CI 0.115–0.291; LOEUF = 0.29)**, only **12 observed vs 66.9 expected LoF**, **missense Z = 5.77**, synonymous Z = −1.47 (unconstrained). A LOEUF of 0.29 places CNNM2 in the most-constrained decile, consistent with haploinsufficiency and dominant (often *de novo*) inheritance [C, finding F009].

**Origin:** germline; frequently *de novo*. No somatic-cancer disease role for the syndrome (though CNNM–PRL interactions are oncogenic in tumor biology—see §6).

**Functional consequence:** **loss of function** (reduced Mg²⁺-sensitive Na⁺ currents; abolished Mg²⁺ efflux for CBS-domain variants) [V, [PMID: 21397062](https://pubmed.ncbi.nlm.nih.gov/21397062/); [PMID: 24706765](https://pubmed.ncbi.nlm.nih.gov/24706765/)]; dominant-negative action is plausible given heterodimerization and dominant inheritance.

**Functional partners / modifier genes.** **TRPM7**—CNNM2 promotes cellular Mg²⁺ uptake through regulating TRPM7; mutant CNNM2 fails to do so [V, [PMID: 24699222](https://pubmed.ncbi.nlm.nih.gov/24699222/)]. Co-functioning DCT transporters (apical TRPM6; basolateral SLC41A3) and the transcriptional regulator PCBD1 could plausibly modify phenotype [H, [PMID: 38871680](https://pubmed.ncbi.nlm.nih.gov/38871680/); [PMID: 26446763](https://pubmed.ncbi.nlm.nih.gov/26446763/)]. No formal clinical modifier gene is established.

**Epigenetic / chromosomal.** No disease-specific methylation/histone signature or characteristic chromosomal abnormality; HOMGSMR1 is a single-gene disorder.

---

## 5. Environmental Information

- **Environmental/toxin factors:** none causal for HOMGSMR1.
- **Lifestyle:** dietary Mg²⁺ intake modulates severity; Mg²⁺-depleting behaviors/conditions worsen hypomagnesemia [H, [PMID: 38871680](https://pubmed.ncbi.nlm.nih.gov/38871680/)].
- **Infectious agents:** none; non-infectious genetic disorder.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A germline **CNNM2 variant** (CBS/DUF21 missense or truncating) **leads to** a structurally/functionally defective Cyclin M2 protein (reduced stability / disrupted Mg-ATP binding) [V/C, [PMID: 22399287](https://pubmed.ncbi.nlm.nih.gov/22399287/)]. *(Demonstrated.)*
2. The defective CBS module **results in** loss of Mg²⁺-dependent ATP sensing and distortion of the twisted↔flat allosteric switch (T568I locks the flat/nucleotide-bound state): *"the substitution of one amino acid residue in the CBS domains of CNNM2 … abrogates Mg(2+) efflux"* [V, [PMID: 24706765](https://pubmed.ncbi.nlm.nih.gov/24706765/); [PMID: 25184538](https://pubmed.ncbi.nlm.nih.gov/25184538/)]. *(Demonstrated — crystallography.)*
3. This **leads to** impaired basolateral **Mg²⁺ extrusion** in DCT epithelial cells (diminished Mg²⁺-sensitive Na⁺ currents in mutants) and loss of regulation of **TRPM7-mediated uptake** [V, [PMID: 21397062](https://pubmed.ncbi.nlm.nih.gov/21397062/); [PMID: 24699222](https://pubmed.ncbi.nlm.nih.gov/24699222/)]. *(Demonstrated.)*
4. Reduced DCT Mg²⁺ handling **results in** decreased transcellular Mg²⁺ reabsorption (the nephron's final fine-tuning step) → renal **Mg²⁺ wasting** → systemic **hypomagnesemia** [H, [PMID: 21397062](https://pubmed.ncbi.nlm.nih.gov/21397062/); [PMID: 38871680](https://pubmed.ncbi.nlm.nih.gov/38871680/)]. *(Demonstrated.)*
5. **Branch A (systemic):** Hypomagnesemia **leads to** neuronal/neuromuscular hyperexcitability (loss of NMDA-receptor Mg²⁺ block; membrane destabilization) → **seizures**, tetany, cardiac arrhythmia [H, [PMID: 21397062](https://pubmed.ncbi.nlm.nih.gov/21397062/)]. *(Demonstrated/clinical.)*
6. **Branch B (Mg²⁺-independent neurodevelopmental):** CNNM2 is expressed in brain and required for normal forebrain/neurodevelopment; loss **leads to** abnormal brain development and intellectual disability/epilepsy **even when serum Mg²⁺ is normal** [H/M, [PMID: 34490037](https://pubmed.ncbi.nlm.nih.gov/34490037/); [PMID: 30929901](https://pubmed.ncbi.nlm.nih.gov/30929901/)]; zebrafish *cnnm2* knockdown causes disturbed brain development [M, [PMID: 24699222](https://pubmed.ncbi.nlm.nih.gov/24699222/)]. *(Inferred in humans; demonstrated in zebrafish.)*

```
 CNNM2 variant (LoF / allosteric, e.g. T568I)
            │
            ▼
 Defective Mg-ATP sensing (CBS "twisted→flat" switch; T568I locks flat)
            │
            ▼
 Impaired Mg2+ efflux + loss of TRPM7 regulation
       ┌────────────┴─────────────┐
       ▼                          ▼
 Renal DCT: reduced          Brain: disrupted
 basolateral Mg2+ handling   neurodevelopment
       │                          │
       ▼                          ▼
 Renal Mg2+ wasting →        Intellectual disability,
 HYPOMAGNESEMIA              brain malformation (recessive)
       │                          │
       ▼                          │
 Neuromuscular hyperexcitability ◄┘
       ▼
 SEIZURES
```

### Supporting detail

- **Molecular pathways / biochemistry:** The CBS/Bateman module binds **ATP (not AMP) Mg²⁺-dependently**; *"Mg(2+) favours ATP binding by alleviating the otherwise negative charge repulsion existing between acidic residues and the polyphosphate group of ATP"* [V, [PMID: 25184538](https://pubmed.ncbi.nlm.nih.gov/25184538/)]. Activity is regulated by **PRL (phosphatase of regenerating liver)** phosphatases binding the Bateman module, raising intracellular Mg²⁺ (oncogenic in cancer); the PRL-1·CNNM2 structure is solved and a **phosphocysteine** intermediate mediates the switch [V, [PMID: 27899452](https://pubmed.ncbi.nlm.nih.gov/27899452/); [PMID: 27856537](https://pubmed.ncbi.nlm.nih.gov/27856537/)].
- **Protein dysfunction / structure:** Nucleotide binding triggers *"a conformational change in the CBS module from a twisted towards a flat disc-like structure"*, and *"the T568I mutation, which causes dominant hypomagnesaemia, mimics the structural effect induced by nucleotide binding"* [V, [PMID: 25184538](https://pubmed.ncbi.nlm.nih.gov/25184538/)].
- **Transport directionality nuance:** CNNM2 is reported both as a basolateral Mg²⁺ **extruder** [V, [PMID: 21397062](https://pubmed.ncbi.nlm.nih.gov/21397062/)] and as promoting **uptake via TRPM7** [V, [PMID: 24699222](https://pubmed.ncbi.nlm.nih.gov/24699222/)]; whether it is a direct transporter or an Mg²⁺ sensor/regulator remains debated [PMID 33859252]. All data converge on loss of CNNM2-dependent Mg²⁺ handling as the pathogenic event.
- **Metabolic relevance:** Mg²⁺ is a cofactor for >600 enzymes as Mg-ATP, so deficiency broadly impairs energy metabolism, muscle contraction, and neurotransmission [H, [PMID: 38871680](https://pubmed.ncbi.nlm.nih.gov/38871680/)].

**GO terms:** GO:0015693 (magnesium ion transport); GO:0010960 (magnesium ion homeostasis); GO:0015095 (magnesium ion transmembrane transporter activity); GO:0005524 (ATP binding); GO:0007420 (brain development).
**CL terms:** CL:1000849 (kidney distal convoluted tubule epithelial cell); CL:0000540 (neuron).
**CHEBI:** CHEBI:18420 (magnesium(2+)); CHEBI:30616 (ATP).

---

## 7. Anatomical Structures Affected

- **Organ level — primary:** kidney (distal convoluted tubule; UBERON:0001292 nephron tubule, UBERON:0005097/UBERON:0004135 distal convoluted tubule) and brain (UBERON:0000955). Secondary/associated: heart (ASD, arrhythmia; UBERON:0000948), liver (UBERON:0002107; single reports).
- **Body systems:** urinary/renal, central nervous, cardiovascular, endocrine-metabolic.
- **Tissue/cell level:** renal **DCT epithelial cells** (CNNM2 *"predominantly found along the basolateral membrane of distal tubular segments involved in Mg(2+) reabsorption"* [[PMID: 21397062](https://pubmed.ncbi.nlm.nih.gov/21397062/)]); CNS **neurons** (forebrain/pallium, hypothalamus, tectum in zebrafish [[PMID: 30929901](https://pubmed.ncbi.nlm.nih.gov/30929901/)]).
- **Subcellular level:** **basolateral plasma membrane** (GO:0016323); **endoplasmic reticulum** (signal-peptide cleavage/processing, GO:0005789); cytosolic CBS-module interface [V, [PMID: 22399287](https://pubmed.ncbi.nlm.nih.gov/22399287/)].
- **Laterality:** bilateral (systemic renal wasting and generalized CNS involvement).

---

## 8. Temporal Development

- **Onset:** congenital to neonatal/infantile; seizures often in the first months of life (e.g., 4-month-old, 1 y 7 m cases) [H, [PMID: 35170241](https://pubmed.ncbi.nlm.nih.gov/35170241/); [PMID: 37532502](https://pubmed.ncbi.nlm.nih.gov/37532502/)]. Acute seizure presentation on a chronic metabolic/developmental background.
- **Progression:** hypomagnesemia chronic/lifelong; intellectual disability generally static but permanent; epilepsy ranges controllable→intractable.
- **Course:** chronic, lifelong; no spontaneous remission of the genetic defect; seizures may be controlled with Mg²⁺ correction + antiseizure medication.
- **Critical period:** early neurodevelopment (prenatal/infancy) is the key window; early Mg²⁺ correction may limit neurological sequelae (inferred from analogous Mg²⁺-wasting disorders, [PMID 32369769](https://pubmed.ncbi.nlm.nih.gov/32369769/)).

---

## 9. Inheritance and Population

- **Epidemiology:** very rare; ~24 pediatric cases by 2022 [H, [PMID: 35170241](https://pubmed.ncbi.nlm.nih.gov/35170241/)], largest cohort ~34 [[PMID: 33600043](https://pubmed.ncbi.nlm.nih.gov/33600043/)]. No reliable prevalence/incidence (ultra-rare, <1/1,000,000 order of magnitude).
- **Inheritance:** predominantly **autosomal dominant**, frequently **de novo** heterozygous variants [H, [PMID: 21397062](https://pubmed.ncbi.nlm.nih.gov/21397062/); [PMID: 37532502](https://pubmed.ncbi.nlm.nih.gov/37532502/); [PMID: 35170241](https://pubmed.ncbi.nlm.nih.gov/35170241/)]; severe early-onset forms with brain malformation are **autosomal recessive** (biallelic): *"For the first time, a recessive mode of inheritance of CNNM2 mutations was observed. Importantly, patients with recessive CNNM2 mutations suffer from brain malformations and severe intellectual disability"* [H, [PMID: 24699222](https://pubmed.ncbi.nlm.nih.gov/24699222/)].
- **Genotype–phenotype:** allelic-dose gradient — biallelic/recessive → severe ID + brain malformation; monoallelic *de novo* missense → moderate ID.
- **Penetrance/expressivity:** high but **variable expressivity** (severity and even presence of hypomagnesemia vary) [[PMID: 33600043](https://pubmed.ncbi.nlm.nih.gov/33600043/); [PMID: 34490037](https://pubmed.ncbi.nlm.nih.gov/34490037/)].
- **Anticipation:** not applicable (not a repeat-expansion disorder).
- **Germline mosaicism / founder effects:** not established. **Consanguinity** relevant for recessive forms.
- **Carrier frequency / constraint:** no established carrier frequency; CNNM2 highly LoF-intolerant (pLI ≈ 1.0, LOEUF = 0.29), so truncating variants are very rare in the general population [C, gnomAD v2.1.1].
- **Population/sex/geography:** cases reported worldwide (Europe, China, etc.); no strong ethnic predilection or established sex bias.

---

## 10. Diagnostics

- **Laboratory:** low **serum magnesium** (<0.7 mmol/L; LOINC 19123-9); inappropriately high **urinary Mg²⁺ / FE-Mg²⁺** indicating renal wasting; typically normal/variable serum calcium and PTH (distinguishing from TRPM6/FHSH which causes secondary hypocalcemia, [PMID 32369769](https://pubmed.ncbi.nlm.nih.gov/32369769/)).
- **Imaging:** brain MRI may show developmental/structural abnormalities in a subset [[PMID: 34490037](https://pubmed.ncbi.nlm.nih.gov/34490037/)].
- **Electrophysiology:** EEG for seizure characterization; ECG may show arrhythmia/QT changes with severe hypomagnesemia.
- **Genetic testing (gold standard):** trio **whole-exome sequencing (WES)**, confirmed by Sanger [H, [PMID: 37532502](https://pubmed.ncbi.nlm.nih.gov/37532502/); [PMID: 35170241](https://pubmed.ncbi.nlm.nih.gov/35170241/)]; targeted hypomagnesemia **gene panels** (CNNM2, TRPM6, FXYD2, KCNA1, EGF, SLC12A3, CLDN16/19, HNF1B/PCBD1) and single-gene CNNM2 testing are alternatives. Functional assays (Mg²⁺ flux, TRPM7 regulation, Western/immunofluorescence) support novel-variant interpretation [[PMID: 40612795](https://pubmed.ncbi.nlm.nih.gov/40612795/)].
- **Differential diagnosis:** other hereditary hypomagnesemias — TRPM6 (FHSH with secondary hypocalcemia, [PMID 32369769](https://pubmed.ncbi.nlm.nih.gov/32369769/)), CNNM4 (Jalili syndrome), FXYD2, EGF, KCNA1, Gitelman (SLC12A3), Claudin-16/19 (FHHNC), HNF1B/PCBD1; plus non-genetic causes (PPIs, diuretics, alcohol, GI losses, vitamin-D-deficient hypocalcemic seizures [PMID 41869998]) [H, [PMID: 38871680](https://pubmed.ncbi.nlm.nih.gov/38871680/)].
- **Screening:** cascade genetic testing of relatives once a familial variant is identified; no population newborn screening.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** generally not life-limiting if hypomagnesemia is controlled; risk from severe acute hypomagnesemia (seizures, arrhythmia) [H, [PMID: 21397062](https://pubmed.ncbi.nlm.nih.gov/21397062/)]. Homozygous loss is embryonic-lethal in mice [[PMID: 33859252](https://pubmed.ncbi.nlm.nih.gov/33859252/)].
- **Morbidity/function:** lifelong intellectual disability, epilepsy, and speech/motor impairment dominate the disability burden; chronic reliance on Mg²⁺ supplementation.
- **Complications:** intractable epilepsy, cardiac arrhythmia, GI intolerance of oral Mg²⁺.
- **Recovery potential:** biochemical correction is achievable but **established neurodevelopmental deficits are not reversible**.
- **Prognostic factors:** genotype (allelic dose), seizure intractability, degree of developmental delay, presence of brain malformation, and timeliness of Mg²⁺ correction. Neurological outcome does not strictly correlate with serum Mg²⁺ [[PMID: 34490037](https://pubmed.ncbi.nlm.nih.gov/34490037/)].

---

## 12. Treatment

**No curative therapy exists; management is symptomatic/supportive.**

- **Magnesium supplementation** (NCIT:C29236 Magnesium): oral Mg²⁺ salts (magnesium oxide/sulfate) first-line; renal wasting makes normalization difficult and high doses cause dose-limiting **diarrhea**. Severe/refractory cases require **IV magnesium sulfate**, and continuous **subcutaneous Mg²⁺ infusion** has normalized levels and improved symptoms in refractory renal-wasting hypomagnesemia: *"achieved near-normal serum magnesium levels with subcutaneous magnesium infusions"* [H, [PMID: 36941847](https://pubmed.ncbi.nlm.nih.gov/36941847/)]. CNNM2 hypomagnesemia is typically only partially Mg²⁺-responsive.
- **Antiseizure medication** (NCIT:C264 Anticonvulsant Agent) for epilepsy, alongside Mg²⁺ correction.
- **Potassium-sparing diuretics** (e.g., amiloride) are used in some renal Mg²⁺-wasting disorders to reduce urinary losses (adjunct; limited CNNM2-specific evidence).
- **Supportive/rehabilitative:** developmental/educational support, speech therapy, physiotherapy, occupational therapy; cardiology follow-up where CHD/arrhythmia is present.
- **Advanced/experimental therapeutics (gene, cell, RNA, targeted):** none in clinical use; no CNNM2-specific trials. Emerging general hypomagnesemia approaches (prebiotic fibers, SGLT2 inhibitors) are **not validated for HOMGSMR1** [[PMID: 38871680](https://pubmed.ncbi.nlm.nih.gov/38871680/)]. Pharmacogenomics: not applicable.

---

## 13. Prevention

- **Primary prevention:** not possible (genetic); genetic counseling for families with a known variant.
- **Secondary prevention:** early recognition—*"We suggest testing for CNNM2 mutation in patients with neurological impairment and hypomagnesemia"* [[PMID: 34515155](https://pubmed.ncbi.nlm.nih.gov/34515155/)]—and early Mg²⁺ correction to limit neurological sequelae.
- **Tertiary prevention:** ongoing Mg²⁺ maintenance and seizure control to prevent complications.
- **Reproductive options:** carrier/variant testing, prenatal diagnosis, preimplantation genetic testing where a familial variant is known.
- **Public-health/immunization/environmental measures:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** CNNM2 is evolutionarily conserved [V, [PMID: 24706765](https://pubmed.ncbi.nlm.nih.gov/24706765/)]. Orthologs: mouse *Cnnm2* (NCBI Taxon 10090), rat *Cnnm2*, zebrafish *cnnm2* (NCBI Taxon 7955). The CNNM family is ancient/conserved ("Ancient Conserved Domain Protein").
- **Natural disease in animals:** no well-documented spontaneous CNNM2 disease in companion animals/wildlife (no established OMIA entry); ruminant hypomagnesemia ("grass tetany") is nutritional, not CNNM2-genetic. Hypomagnesemia from other causes occurs (e.g., refeeding syndrome in a cat, [PMID 35818515](https://pubmed.ncbi.nlm.nih.gov/35818515/)).
- **Comparative biology:** conserved Mg²⁺-handling mechanism across CNNM1–4 paralogs; CNNM4 defects cause Jalili syndrome, underscoring family-wide conservation. **No zoonotic potential** (non-infectious).

---

## 15. Model Organisms

| Model | Genotype | Key phenotype | Recapitulation | Reference |
|---|---|---|---|---|
| **Mouse** (*Cnnm2*) | Homozygous KO | **Embryonic lethal**; developmental defects | Confirms essentiality | [PMID: 33859252](https://pubmed.ncbi.nlm.nih.gov/33859252/) |
| **Mouse** | Systemic heterozygous KO | **Hypomagnesemia**; viable | Models dominant human disorder | [PMID: 28033128](https://pubmed.ncbi.nlm.nih.gov/28033128/) |
| **Mouse** | Kidney-specific homozygous KO | Hypomagnesemia; basolateral DCT localization; reduced BP (SBP ~121.7 WT vs ~110 mmHg) | Confirms renal DCT role | [PMID: 28033128](https://pubmed.ncbi.nlm.nih.gov/28033128/) |
| **Zebrafish** (*cnnm2*) | Morpholino knockdown | Disturbed brain development, increased spontaneous contractions, weak touch-evoked escape, reduced body Mg²⁺ | Models neuro + Mg²⁺ phenotype | [PMID: 24699222](https://pubmed.ncbi.nlm.nih.gov/24699222/) |
| **Zebrafish** (*cnnm2*) | Orthologue mutation (schizophrenia-gene screen) | Altered forebrain development, decreased prepulse inhibition | Supports neurodevelopmental role | [PMID: 30929901](https://pubmed.ncbi.nlm.nih.gov/30929901/) |
| **HEK293 / epithelial cells** | CNNM2 overexpression / mutant | WT increases ²⁵Mg²⁺ uptake via TRPM7; mutant does not; basolateral localization; Mg²⁺-sensitive Na⁺ currents diminished in mutant | Defines cellular mechanism | [PMID: 24699222](https://pubmed.ncbi.nlm.nih.gov/24699222/); [PMID: 21397062](https://pubmed.ncbi.nlm.nih.gov/21397062/) |

**Recapitulation & limitations.** Mouse and zebrafish models reproduce both the renal (hypomagnesemia) and neurological (brain-development) axes, strongly validating causality. Homozygous mouse lethality precludes adult homozygous CNS modeling; morpholino knockdown carries off-target caveats; cell models capture molecular transport but not cognition/seizures. **Resources:** MGI (mouse), ZFIN (zebrafish), Cellosaurus (HEK293).

---

## Mechanistic Model / Interpretation

The evidence converges on a single, coherent **five-layer model**:

| Layer | Evidence | Conclusion |
|---|---|---|
| Human genetics | Heterozygous *de novo* + biallelic CNNM2 variants cause disease | CNNM2 causal; allelic-dose gradient ([PMID: 21397062](https://pubmed.ncbi.nlm.nih.gov/21397062/); [PMID: 24699222](https://pubmed.ncbi.nlm.nih.gov/24699222/); [PMID: 33600043](https://pubmed.ncbi.nlm.nih.gov/33600043/)) |
| Population genetics | pLI ≈ 1.0, LOEUF = 0.29, mis_Z = 5.77 | Haploinsufficiency; dominant LoF |
| Structural biology | Mg-ATP drives twisted→flat CBS switch; T568I locks it | Allosteric gating defect ([PMID: 25184538](https://pubmed.ncbi.nlm.nih.gov/25184538/)) |
| Cell biology | Basolateral DCT Mg²⁺ handling; regulates TRPM7 | Transport/sensing defect ([PMID: 21397062](https://pubmed.ncbi.nlm.nih.gov/21397062/); [PMID: 24699222](https://pubmed.ncbi.nlm.nih.gov/24699222/)) |
| Animal models | Mouse KO (hypomagnesemic/lethal), zebrafish (brain defects) | Recapitulate renal + neuro phenotypes ([PMID: 33859252](https://pubmed.ncbi.nlm.nih.gov/33859252/); [PMID: 28033128](https://pubmed.ncbi.nlm.nih.gov/28033128/); [PMID: 24699222](https://pubmed.ncbi.nlm.nih.gov/24699222/)) |

A key interpretive nuance: the neurological phenotype is **partially dissociable** from systemic hypomagnesemia. Cases with brain malformation and intractable epilepsy **without** hypomagnesemia [[PMID: 34490037](https://pubmed.ncbi.nlm.nih.gov/34490037/)], plus zebrafish brain-development defects, argue for a **cell-autonomous CNS requirement** for CNNM2 in addition to the downstream effects of low serum Mg²⁺. This explains why Mg²⁺ supplementation corrects biochemistry and aids seizure control but does not reverse cognitive deficits.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [21397062](https://pubmed.ncbi.nlm.nih.gov/21397062/) | *CNNM2 … mutated in dominant hypomagnesemia* | Establishes causality; basolateral DCT localization |
| [24699222](https://pubmed.ncbi.nlm.nih.gov/24699222/) | *CNNM2 mutations cause impaired brain development and seizures* | Recessive inheritance; TRPM7 mechanism; zebrafish |
| [24706765](https://pubmed.ncbi.nlm.nih.gov/24706765/) | *Mg²⁺-dependent ATP binding to CBS domains* | CBS domains sense Mg-ATP; disease variant abolishes efflux |
| [25184538](https://pubmed.ncbi.nlm.nih.gov/25184538/) | *Nucleotide-triggered CBS conformational change* | Twisted→flat switch; T568I mimics nucleotide-bound state |
| [33600043](https://pubmed.ncbi.nlm.nih.gov/33600043/) | *Phenotypic/genetic spectrum (largest cohort)* | 11 novel variants; phenotype spectrum |
| [33859252](https://pubmed.ncbi.nlm.nih.gov/33859252/) | *Cnnm2 KO mice* | Hypomagnesemia, developmental defects, lethality |
| [28033128](https://pubmed.ncbi.nlm.nih.gov/28033128/) | *Renal CNNM2 maintains blood pressure* | Kidney-specific/heterozygous KO hypomagnesemia |
| [35170241](https://pubmed.ncbi.nlm.nih.gov/35170241/) | *Tyr189Cys case + review* | Core triad; ~24 cases; *de novo* pathogenic missense |
| [34490037](https://pubmed.ncbi.nlm.nih.gov/34490037/) | *Brain damage/epilepsy without hypomagnesemia* | Neuro phenotype dissociable from serum Mg²⁺ |
| [37532502](https://pubmed.ncbi.nlm.nih.gov/37532502/) | *c.1448delT case* | *De novo* truncating pathogenic variant (ACMG) |
| [40612795](https://pubmed.ncbi.nlm.nih.gov/40612795/) | *Novel variants p.E298del, p.P360R* | Expands mutation/functional spectrum |
| [27899452](https://pubmed.ncbi.nlm.nih.gov/27899452/) | *PRL-1–CNNM2 structure* | Regulatory PRL-CNNM interaction raises intracellular Mg²⁺ |
| [27856537](https://pubmed.ncbi.nlm.nih.gov/27856537/) | *Phosphocysteine in PRL-CNNM pathway* | Regulation of Mg²⁺ homeostasis |
| [22399287](https://pubmed.ncbi.nlm.nih.gov/22399287/) | *Membrane topology/processing of CNNM2* | Structure, glycosylation, ATP-binding by CBS |
| [38871680](https://pubmed.ncbi.nlm.nih.gov/38871680/) | *Magnesium biology (review)* | DCT Mg²⁺ physiology; CNNM2 basolateral extrusion |
| [36941847](https://pubmed.ncbi.nlm.nih.gov/36941847/) | *Subcutaneous Mg infusion* | Treatment for refractory renal Mg²⁺ wasting |
| [34515155](https://pubmed.ncbi.nlm.nih.gov/34515155/) | *Diagnostic dilemma case* | Recommends CNNM2 testing in neuro + hypomagnesemia |
| [32369769](https://pubmed.ncbi.nlm.nih.gov/32369769/) | *TRPM6 variant (FHSH)* | Differential diagnosis |
| [30929901](https://pubmed.ncbi.nlm.nih.gov/30929901/) | *Schizophrenia-gene zebrafish atlas* | cnnm2 forebrain development role |
| gnomAD v2.1.1 | Constraint (computational) | pLI ≈ 1.0, LOEUF = 0.29, mis_Z = 5.77 → haploinsufficiency |

---

## Limitations and Knowledge Gaps

1. **Rarity limits epidemiology.** With ~24–34 reported cases, prevalence, incidence, sex ratio, penetrance, and carrier frequency cannot be precisely estimated; phenotype frequencies remain qualitative.
2. **Genotype–phenotype map is incomplete.** The dominant-vs-recessive severity gradient is established qualitatively, but systematic variant-level functional classification is lacking for most alleles.
3. **CNS mechanism is partly inferred.** The Mg²⁺-independent neurodevelopmental role rests on zebrafish and the hypomagnesemia-independent case; direct demonstration in human neurons is limited.
4. **Haploinsufficiency vs dominant-negative** is not fully resolved for individual variants, though gene-level constraint favors haploinsufficiency.
5. **No human treatment-outcome data.** The effect of Mg²⁺ supplementation on long-term cognitive/seizure outcomes has not been systematically studied.
6. **Some citation snippets were flagged as title-based ("mismatch")** in the knowledge state (e.g., PMID 33859252, 34490037, 27856537) and should be verified against full abstracts before public-database ingestion.

---

## Proposed Follow-up Experiments / Actions

1. **Conditional CNS-specific Cnnm2 knockout mice** (e.g., Nestin-Cre) to dissect cell-autonomous brain requirement from systemic hypomagnesemia and test whether early Mg²⁺ correction rescues neurodevelopment.
2. **Patient iPSC-derived neurons/organoids** carrying dominant (T568I, Tyr189Cys) and recessive variants to measure Mg²⁺ handling, TRPM7 regulation, and developmental defects in a human neural context.
3. **Deep mutational scanning / functional assay** of CNNM2 variants (Mg²⁺ flux, CBS-module conformation, surface expression) to build an evidence-based ACMG variant-classification map.
4. **Natural-history registry** for HSMR to quantify onset age, seizure trajectory, cognitive outcomes, and supplementation response across genotypes.
5. **Structural studies of additional pathogenic variants** (p.P360R, p.E298del) to test whether they share the T568I "flat-lock" mechanism or act via misfolding/trafficking.
6. **Verify flagged citations** and resolve ClinVar/ACMG classifications for all reported variants before knowledge-base ingestion.

---

*Evidence source types: human clinical (case reports/cohorts), model organism (mouse, zebrafish), in vitro (HEK293, crystallography), and computational (gnomAD constraint).*


## Artifacts

- [OpenScientist final report](Hypomagnesemia_Seizures_And_Intellectual_Disability_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hypomagnesemia_Seizures_And_Intellectual_Disability_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 22 |
| On topic | 11 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:27856537` (4 mentions) - Phosphocysteine in the PRL-CNNM pathway mediates magnesium homeostasis.
  - shared terms: genetic

Weighed against this report's own most characteristic terms: `cnnm2`, `hypomagnesemia`, `seizure`, `variant`, `brain`, `phenotype`, `renal`, `genetic`, `cause`, `disorder`, `zebrafish`, `basolateral`, `development`, `disability`, `intellectual`, `developmental`, `dominant`, `serum`, `trpm7`, `wasting`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 17 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0020787` (2 mentions) - the report calls it "MONDO"; MONDO calls it **hypomagnesemia, seizures, and impaired intellectual development 1**
- `HP:0002917` (1 mention) - the report calls it "Very frequent (core; occasionally absent)"; HP calls it **Hypomagnesemia**
- `HP:0001250` (1 mention) - the report calls it "Frequent (core)"; HP calls it **Seizure**
- `HP:0000750` (1 mention) - the report calls it "Common"; HP calls it **Delayed speech and language development**
- `HP:0001270` (1 mention) - the report calls it "Common"; HP calls it **Motor delay**
- `HP:0002011` (1 mention) - the report calls it "Subset (can occur w/o hypomagnesemia)"; HP calls it **Morphological central nervous system abnormality**
- `HP:0002353` (1 mention) - the report calls it "Common with seizures"; HP calls it **EEG abnormality**
- `HP:0001410` (1 mention) - the report calls it "Single reports"; HP calls it **Decreased liver function**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C29236` (Murine Monoclonal Antibody (LYM-1)) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CHEBI:30616` (1 mention) - the report calls it "ATP"; CHEBI calls it **ATP(4-)**, and lists "ATP" among its other names
- `GO:0016323` (1 mention) - the report calls it "basolateral plasma membrane", "Subcellular level:** **basolateral plasma membrane"; GO calls it **basolateral plasma membrane**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0016323` - called "basolateral plasma membrane", "Subcellular level:** **basolateral plasma membrane"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.