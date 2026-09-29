---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T20:37:56.284264'
end_time: '2026-09-29T21:12:36.537278'
duration_seconds: 2080.25
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Severe Congenital Neutropenia 7, Autosomal Recessive
  mondo_id: MONDO:0014865
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
citation_count: 17
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 21
  on_topic: 18
  off_topic: 1
  off_topic_references:
  - PMID:17389229
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 37
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 14
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: HP:0002718
    reported_labels:
    - ~all
    ontology_label: Recurrent bacterial infections
  - term_id: HP:0009110
    reported_labels:
    - Subset
    ontology_label: Diaphragmatic eventration
  - term_id: HP:0011107
    reported_labels:
    - Common
    ontology_label: Recurrent aphthous stomatitis
  - term_id: HP:0012758
    reported_labels:
    - Subset (4/32)
    ontology_label: Neurodevelopmental delay
  - term_id: HP:0000938
    reported_labels:
    - Subset
    ontology_label: Osteopenia
  - term_id: HP:0005249
    reported_labels:
    - Subset
    ontology_label: Functional intestinal obstruction
  - term_id: HP:0001508
    reported_labels:
    - Subset
    ontology_label: Failure to thrive
  - term_id: NCIT:C1683
    reported_labels:
    - Filgrastim/G-CSF
    ontology_label: Tyrphostin A47
  - term_id: NCIT:C1863
    reported_labels:
    - Sargramostim/GM-CSF
    ontology_label: Entinostat
  - term_id: NCIT:C4711
    reported_labels:
    - Allogeneic
    ontology_label: Borderline Cystadenoma
  - term_id: UBERON:0001723
    reported_labels:
    - tongue/oral mucosa for aphthae
    ontology_label: tongue
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Severe_Congenital_Neutropenia_7_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Severe_Congenital_Neutropenia_7_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Severe Congenital Neutropenia 7, Autosomal Recessive
- **MONDO ID:** MONDO:0014865 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Severe Congenital Neutropenia 7, Autosomal Recessive** covering all of the
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

# Severe Congenital Neutropenia 7, Autosomal Recessive (SCN7) — Comprehensive Disease Report

**Disease:** Severe Congenital Neutropenia 7, Autosomal Recessive
**MONDO ID:** MONDO:0014865 · **OMIM phenotype:** #616022 · **Causal gene:** *JAGN1* (OMIM *616012, HGNC:26926)
**Category:** Mendelian (monogenic, autosomal recessive)

---

## Summary

Severe Congenital Neutropenia 7 (SCN7) is a rare autosomal recessive primary immunodeficiency / bone-marrow-failure disorder caused by **biallelic loss-of-function variants in *JAGN1*** (Jagunal homolog 1), a small, evolutionarily conserved endoplasmic reticulum (ER)-resident integral membrane protein. Whole-exome sequencing first defined the disorder in 2014, identifying 9 distinct homozygous *JAGN1* mutations in 14 affected individuals ([PMID: 25129144](https://pubmed.ncbi.nlm.nih.gov/25129144/)). *JAGN1* deficiency is now estimated to account for **roughly 10% of all severe congenital neutropenia (SCN) cases** ([PMID: 41751872](https://pubmed.ncbi.nlm.nih.gov/41751872/)).

Mechanistically, SCN7 is best understood as a **myeloid ER-secretory / glycosylation and G-CSF-receptor-signaling disorder**. Loss of JAGN1 disrupts ER vesicular trafficking, protein N-glycosylation and sialylation, cytotoxic granule formation, and granulocyte colony-stimulating factor receptor (G-CSFR) signaling. This produces a **two-branch phenotype**: a *quantitative* defect (maturation arrest and calpain-dependent apoptosis of myeloid progenitors → severe neutropenia) and a *qualitative* defect (impaired neutrophil adhesion, migration, degranulation and microbial killing — present in mouse models even without frank neutropenia). Clinically, patients present in the neonatal period or early infancy with recurrent bacterial and fungal infections, aphthous stomatitis, and skin abscesses; about a third have a syndromic spectrum including short stature, facial dysmorphism, and bone/neurodevelopmental abnormalities.

Prognostically, SCN7 is a lifelong condition dominated by infection- and leukemia-related morbidity. Unlike *ELANE*- or *HAX1*-related SCN, **most *JAGN1* patients respond poorly to recombinant G-CSF**, and GM-CSF has also failed to rescue neutrophil counts in reported cases. Like all SCN, it carries a premalignant risk of myelodysplastic syndrome / acute myeloid leukemia (MDS/AML). **Allogeneic hematopoietic stem cell transplantation (alloHSCT) is the only definitive, curative therapy** and is preferentially applied to poor G-CSF responders — the group that includes most *JAGN1*-deficient patients.

---

## Key Findings

### Finding 1 — SCN7 is caused by biallelic (autosomal recessive) loss-of-function variants in *JAGN1*

The genetic basis of SCN7 was established by whole-exome sequencing, which identified **9 distinct homozygous *JAGN1* mutations in 14 individuals** with severe congenital neutropenia ([PMID: 25129144](https://pubmed.ncbi.nlm.nih.gov/25129144/)): *"We identify 9 distinct homozygous mutations in the JAGN1 gene encoding Jagunal homolog 1 in 14 individuals with SCN."* The homozygous state across all 14 patients directly supports strict autosomal recessive inheritance.

*JAGN1* encodes **Jagunal homolog 1**, an ER-resident membrane protein of ~189 amino acids with multiple transmembrane domains. The corresponding OMIM entries are phenotype **#616022 (SCN7)** and gene **\*616012**. Recurrent and representative pathogenic variants include:

| Variant (cDNA) | Protein | Class | Notable association |
|---|---|---|---|
| c.3G>A | p.Met1? | Start-loss | "Pure" neutropenia; rarely extramedullary (except short stature in 1 patient) |
| c.63G>T | p.Glu21Asp | Missense | Syndromic facial features + bone metabolism disorders; found in Romanian patients |
| c.130C>T | p.His44Tyr | Missense | Syndromic facial features + bone metabolism disorders |
| c.40G>A | p.Gly14Ser | Missense | Reported SCN7 allele |

*JAGN1* deficiency is estimated to account for **~10% of all SCN cases** ([PMID: 41751872](https://pubmed.ncbi.nlm.nih.gov/41751872/)): *"Jagunal homolog 1 (JAGN1) deficiency has been described as a genetic cause of SCN and is now estimated to account for approximately 10% of all SCN cases."*

**Ontology suggestions:** Gene — HGNC:26926 (*JAGN1*); Disease — MONDO:0014865; variant classes — SO:0001583 (missense_variant), SO:0002012 (start_lost).

### Finding 2 — JAGN1 deficiency disrupts the ER secretory pathway, N-glycosylation, and G-CSFR signaling, causing arrested neutrophil maturation and apoptosis

*JAGN1*-mutant granulocytes are *"characterized by ultrastructural defects, a paucity of granules, aberrant N-glycosylation of multiple proteins and increased incidence of apoptosis"* ([PMID: 25129144](https://pubmed.ncbi.nlm.nih.gov/25129144/)), and JAGN1 is required for **G-CSF receptor-mediated signaling**. This establishes the core cellular lesion: a defective early secretory pathway that impairs both the glycoprotein-processing machinery and the surface signaling apparatus of developing neutrophils.

A distinct cell-death program underlies the apoptosis. In myeloid cells expressing SCN-associated JAGN1 mutants, cells were *"remarkably susceptible to agonists that normally trigger degranulation and succumbed to a calcium-dependent cell death programme. This mode of cell death was completely prevented by pharmacological inhibition of calpain but unaffected by caspase inhibition"* ([PMID: 33206996](https://pubmed.ncbi.nlm.nih.gov/33206996/)). Thus the death is **calcium- and calpain-dependent (caspase-independent)** — a mechanistically specific and potentially druggable node.

An in vivo zebrafish model refined the causal ordering, showing that *"Jagn1b has a critical role in granulocyte colony-stimulating factor receptor signaling and steady-state granulopoiesis, shedding light on the pathogenesis of neutropenia associated with JAGN1 mutations"* ([PMID: 38739706](https://pubmed.ncbi.nlm.nih.gov/38739706/)), with unfolded protein response (UPR) activation and apoptosis appearing **secondary** to the primary G-CSFR/granulopoiesis defect. Newer work identifies that Jagn1 preserves **protein sialylation** during neutrophil differentiation, and that its expression is transcriptionally controlled by **C/EBP-α** ([PMID: 42685351](https://pubmed.ncbi.nlm.nih.gov/42685351/)).

**Ontology suggestions:** GO:0006888 (ER to Golgi vesicle-mediated transport); GO:0006487 (protein N-linked glycosylation); GO:0009101 (glycoprotein biosynthetic process); GO:0006915 (apoptotic process); GO:0030593 (neutrophil chemotaxis); GO:0038158 (granulocyte colony-stimulating factor signaling pathway).

### Finding 3 — Clinical phenotype: neonatal-onset severe neutropenia with recurrent infections, plus a syndromic spectrum

In the ESID/EBMT multicenter cohort of **32 JAGN1-deficient patients**, *"Autosomal recessively inherited variants in JAGN1 lead to congenital neutropenia, early-onset bacterial infections, aphthosis, and skin abscesses due to aberrant differentiation and maturation of neutrophils. Bone metabolism disorders and syndromic phenotype, including facial features, short stature, and neurodevelopmental delay, have been reported"* ([PMID: 39775668](https://pubmed.ncbi.nlm.nih.gov/39775668/)).

**Core features (essentially all patients):** congenital / early-onset severe neutropenia (ANC <0.5×10⁹/L), early-onset bacterial infections, aphthous stomatitis, and skin abscesses. In this cohort **all patients** experienced infectious complications.

**Syndromic features (~a third of patients):** In the 32-patient cohort, **12/32 (~38%)** had short stature and facial features, and neurodevelopmental delay occurred in 4 patients from 3 families. Additional reported features include **delayed umbilical cord separation, failure to thrive, bone metabolism disorders (e.g., osteopenia), and recurrent fungal infections** ([PMID: 37120535](https://pubmed.ncbi.nlm.nih.gov/37120535/)): *"Recurrent abscess formation unresponsive to antibiotic therapy, a history of delayed umbilical separation, frequent bacterial or fungal infection, dysmorphic face, failure to thrive, and other coexisting organ abnormalities should prompt physicians to syndromic immunodeficiencies involving neutrophils."*

**Genotype–phenotype correlation** ([PMID: 39775668](https://pubmed.ncbi.nlm.nih.gov/39775668/)): *"Variant c.3G>A p.Met1, found in 9 patients, was never connected to extramedullary symptoms, except for short stature in 1 patient. Patients with the variants c.63G>T, p.Glu21Asp and c130c>T p.His44 Tyr presented more often with syndromic facial features and bone metabolism disorders."* In short, the start-loss allele tends toward **"pure" neutropenia**, whereas certain missense alleles produce the **syndromic** end of the spectrum.

| Phenotype | Type | Onset | Frequency | Suggested HPO |
|---|---|---|---|---|
| Severe neutropenia (ANC <0.5×10⁹/L) | Lab abnormality | Congenital/neonatal | ~all | HP:0000778 / HP:0001875 |
| Recurrent bacterial infections | Clinical | Infancy | ~all | HP:0002718 |
| Recurrent fungal infections | Clinical | Infancy/childhood | Subset | HP:0009110 |
| Aphthous stomatitis | Clinical sign | Childhood | Common | HP:0011107 |
| Skin abscesses | Clinical sign | Infancy/childhood | Common | HP:0025503 / HP:0100658 |
| Short stature | Physical | Childhood | ~38% | HP:0004322 |
| Facial dysmorphism | Physical | Congenital | ~38% | HP:0001999 |
| Neurodevelopmental delay | Behavioral/neuro | Childhood | Subset (4/32) | HP:0012758 |
| Osteopenia / bone metabolism disorder | Lab/imaging | Childhood | Subset | HP:0000938 |
| Delayed umbilical cord separation | Clinical sign | Neonatal | Subset | HP:0005249 |
| Failure to thrive | Clinical | Infancy | Subset | HP:0001508 |

**Quality of life:** Not formally quantified with instruments (EQ-5D, SF-36) for this ultra-rare disease; morbidity is driven by recurrent infections, hospitalizations, and — where syndromic — growth and developmental impact.

### Finding 4 — Poor G-CSF response; alloHSCT is the definitive curative treatment

A therapeutically decisive feature of SCN7 is that *"most have been described as low-responders to recombinant granulocyte colony-stimulating factor (G-CSF) therapy"* ([PMID: 39286252](https://pubmed.ncbi.nlm.nih.gov/39286252/)). In two G-CSF-refractory patients, GM-CSF (sargramostim) was trialed as an alternative but *"GM-CSF did not increase neutrophil counts in our patients"* — and both ultimately underwent successful HSCT.

The multicenter cohort positions transplant clearly ([PMID: 39775668](https://pubmed.ncbi.nlm.nih.gov/39775668/)): *"Allogeneic hematopoietic stem cell transplantation (alloHSCT) is a treatment option for patients who respond poorly to therapy with G-CSF and those who suffer from complicated infections."* Six of the 32 patients underwent alloHSCT.

Broader SCN evidence frames the trade-offs: long-term G-CSF reduces sepsis mortality but reveals an **MDS/AML predisposition** that plateaus at ~2.3%/year after 10 years ([PMID: 20456363](https://pubmed.ncbi.nlm.nih.gov/20456363/)), and *"Allogeneic hematopoietic stem cell transplantation (HSCT) is the only curative treatment for SCN"* ([PMID: 21072829](https://pubmed.ncbi.nlm.nih.gov/21072829/)).

**Ontology suggestions:** NCIT:C1683 (Filgrastim/G-CSF), NCIT:C1863 (Sargramostim/GM-CSF), NCIT:C15431 (Hematopoietic Stem Cell Transplantation), NCIT:C4711 (Allogeneic).

### Finding 5 — JAGN1 is an evolutionarily conserved ER integral-membrane protein that reorganizes the ER and facilitates vesicular/secretory trafficking

The ancestral cell-biological function of JAGN1 was defined in *Drosophila* oogenesis, where Jagunal concentrates the ER into subcortical clusters and is required for vesicular traffic ([PMID: 17389229](https://pubmed.ncbi.nlm.nih.gov/17389229/)): *"This ER reorganization requires Jagunal, which is an evolutionarily conserved ER membrane protein. Loss of Jagunal reduces vesicular traffic to the oocyte lateral membrane."* Jagn also mediates asymmetric ER partitioning during mitosis in proneural cells ([PMID: 28381427](https://pubmed.ncbi.nlm.nih.gov/28381427/)), and a genetic-modifier screen links Jagn to Sec63, Presenilin/γ-secretase, and Notch signaling ([PMID: 36932646](https://pubmed.ncbi.nlm.nih.gov/36932646/)).

Structural/topological reasoning suggests JAGN1 acts in **cargo sorting and vesicle formation**, sharing topology with tetraspanins and Erv cargo-sorting proteins ([PMID: 32783652](https://pubmed.ncbi.nlm.nih.gov/32783652/)): *"JAGN1, tetraspanins, and Erv proteins: is common topology indicative of common function in cargo sorting?"* This deep conservation explains why loss-of-function produces a defect in the early secretory pathway across species.

**Ontology suggestions:** GO:0005789 (endoplasmic reticulum membrane); GO:0005783 (endoplasmic reticulum); GO:0006888 (ER to Golgi vesicle-mediated transport).

### Finding 6 — Animal and cellular models recapitulate JAGN1-SCN and reveal glycosylation-dependent neutrophil dysfunction rescuable by GM-CSF

A hematopoietic-lineage–specific *Jagn1* knockout mouse demonstrated the qualitative branch of disease. *"Global glycobiome analysis identified marked alterations in the glycosylation of proteins involved in cell adhesion and cytotoxicity in Jagn1-deficient neutrophils"* ([PMID: 25129145](https://pubmed.ncbi.nlm.nih.gov/25129145/)), with *"impaired formation of cytotoxic granules, as well as defective myeloperoxidase release and killing of Candida albicans."* Critically, *"GM-CSF also restored the defective fungicidal activity of bone marrow cells from humans with JAGN1 mutations"* — a candidate therapeutic mechanism (albeit not borne out for correcting neutrophil counts in the later clinical report, PMID 39286252).

The zebrafish *jagn1a/jagn1b* model attributes neutropenia primarily to impaired G-CSFR signaling and steady-state granulopoiesis, with secondary UPR/apoptosis ([PMID: 38739706](https://pubmed.ncbi.nlm.nih.gov/38739706/)). Cellular models — patient-mutant HL-60 promyelocytes ([PMID: 33206996](https://pubmed.ncbi.nlm.nih.gov/33206996/)) and Hoxb8-ER-immortalized progenitors ([PMID: 42685351](https://pubmed.ncbi.nlm.nih.gov/42685351/)) — respectively demonstrate calpain-dependent death and C/EBP-α-controlled, sialylation-dependent adhesion defects (impaired E-selectin and CXCL8 binding).

### Finding 7 — Diagnosis by CBC + bone marrow + NGS; autosomal recessive inheritance with consanguinity/founder contribution

Diagnostic workup rests on **persistent severe neutropenia (ANC <0.5×10⁹/L)** on repeated CBC with differential, a bone marrow aspirate showing **maturation arrest at the promyelocyte/myelocyte stage** (a general SCN feature), and molecular confirmation. Because JAGN1 is not covered by first-line ELANE/G6PC3 Sanger testing, it requires next-generation sequencing (gene panels or WES). In the Israeli congenital-neutropenia registry, *"Sanger sequencing was performed for ELANE or G6PC3, and patients with wild-type ELANE/G6PC3 were referred for next-generation sequencing. Sixty-five patients with neutropenia were included"* ([PMID: 38600884](https://pubmed.ncbi.nlm.nih.gov/38600884/)).

Inheritance is strictly autosomal recessive, and cohorts are enriched for consanguinity: *"The Israeli population is characterized by an ethnically diverse population with a high rate of consanguinity"* ([PMID: 38600884](https://pubmed.ncbi.nlm.nih.gov/38600884/)). Recurrent variants show founder/geographic clustering (e.g., c.3G>A p.Met1? across multiple families; c.63G>T p.Glu21Asp including Romanian patients). Homozygosity across all 14 originally described patients ([PMID: 25129144](https://pubmed.ncbi.nlm.nih.gov/25129144/)) further supports autosomal recessive inheritance with a consanguinity contribution.

### Finding 8 — Prognosis: lifelong disease with infection- and leukemia-related morbidity; prevention centers on prophylaxis, surveillance, and counseling

Untreated SCN carries high early-life mortality from bacterial sepsis. With long-term G-CSF, SCN sepsis mortality falls substantially, but a premalignant MDS/AML predisposition emerges — *"Long-term, the annual risk of MDS/AML attained a plateau (2.3%/year after 10 years)"* ([PMID: 20456363](https://pubmed.ncbi.nlm.nih.gov/20456363/)). Poor G-CSF responders — the group that includes most JAGN1 patients — fare worst: *"In these less-responsive patients, the cumulative incidence of adverse events was highest: after 10 years, 40% developed MDS/AML and 14% died of sepsis"* ([PMID: 16497969](https://pubmed.ncbi.nlm.nih.gov/16497969/)).

Because *"SCN is also a premalignant condition; a significant proportion of patients develop myelodysplastic syndrome or leukemia (MDS/L). Allogeneic hematopoietic stem cell transplantation (HSCT) is the only curative treatment for SCN"* ([PMID: 21072829](https://pubmed.ncbi.nlm.nih.gov/21072829/)), management emphasizes infection prophylaxis, regular hematologic surveillance (CBC, bone marrow with cytogenetics for MDS/AML transformation, monitoring for *CSF3R* mutations in SCN generally), and genetic counseling for at-risk families. In a congenital-neutropenia registry, ~12% of patients showed myeloid transformation and ~29% required HSCT ([PMID: 38600884](https://pubmed.ncbi.nlm.nih.gov/38600884/)).

### Finding 9 — Integrated two-branch mechanistic model of SCN7

Convergent evidence across human patient cells, mouse ([PMID: 25129145](https://pubmed.ncbi.nlm.nih.gov/25129145/)), zebrafish ([PMID: 38739706](https://pubmed.ncbi.nlm.nih.gov/38739706/)), *Drosophila* ([PMID: 17389229](https://pubmed.ncbi.nlm.nih.gov/17389229/)), and in-vitro systems ([PMID: 33206996](https://pubmed.ncbi.nlm.nih.gov/33206996/), [PMID: 42685351](https://pubmed.ncbi.nlm.nih.gov/42685351/)) supports a unified model in which a single conserved ER-secretory/glycosylation lesion produces **both** quantitative and qualitative neutrophil defects. The zebrafish model refines earlier views by showing UPR/apoptosis are secondary to the G-CSFR/granulopoiesis defect.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function *JAGN1* variants** (start-loss, missense, etc.) → **loss/reduction of functional Jagunal homolog 1** in the ER membrane of myeloid cells. *(demonstrated — homozygous mutations, PMID 25129144)*
2. Loss of JAGN1 → **disrupted ER organization and ER-to-Golgi vesicular trafficking / cargo sorting**. *(demonstrated across species; PMID 17389229, 32783652)*
3. Impaired secretory trafficking → **aberrant N-glycosylation and reduced sialylation of glycoproteins**, controlled during differentiation by C/EBP-α. *(demonstrated; PMID 25129144, 25129145, 42685351)*
4. From step 3 the mechanism **branches** (see diagram).

```
                 Biallelic JAGN1 LOF (step 1)
                          │
              Disrupted ER trafficking (step 2)
                          │
        Aberrant N-glycosylation / hyposialylation (step 3)
                    ┌─────┴───────────────────────┐
             BRANCH A                         BRANCH B
   Impaired G-CSFR signaling            Hyposialylation of adhesion
   + calcium/calpain-dependent          receptors (E-selectin ligands,
   caspase-independent apoptosis        CXCR2/CXCL8); poor granule &
   + secondary UPR                      MPO formation
             │                                    │
   Maturation arrest at                 Defective rolling, adhesion,
   promyelocyte/myelocyte;              migration, degranulation,
   progenitor apoptosis                 and microbial killing
             │                                    │
   SEVERE NEUTROPENIA                    DYSFUNCTIONAL NEUTROPHILS
   (quantitative defect)                (qualitative defect; present
             │                          even without neutropenia in mice)
             └──────────────┬───────────────────┘
                            ▼
     Congenital-onset recurrent bacterial & fungal infections,
     aphthous stomatitis, skin abscesses (± syndromic features)
                            │
                            ▼
     Premalignant marrow → MDS/AML risk; poor G-CSF response
                            │
                            ▼
     Cured only by allogeneic HSCT
```

**Branch A (quantitative → neutropenia):** JAGN1 is required for G-CSFR signaling; its loss impairs steady-state granulopoiesis (zebrafish, PMID 38739706) and sensitizes myeloid progenitors to a **calcium- and calpain-dependent, caspase-independent** death program (PMID 33206996), with UPR/apoptosis as secondary events. The net result is maturation arrest and severe neutropenia.

**Branch B (qualitative → dysfunctional neutrophils):** Even neutrophils that are produced are defective. Hyposialylation of adhesion-relevant receptors impairs E-selectin-dependent rolling and CXCL8/CXCR2-mediated adhesion; cytotoxic granule formation, myeloperoxidase release, and *Candida* killing are all impaired (PMID 25129145, 42685351). This branch is demonstrable in mouse models independent of neutrophil count, explaining why infection susceptibility can exceed what the ANC alone would predict.

**Upstream vs downstream:** The mutation and ER-trafficking defect are upstream; glycosylation/sialylation changes are central mediators; G-CSFR signaling failure, apoptosis, and adhesion/killing defects are downstream effectors; infection, marrow premalignancy, and syndromic features are the clinical endpoints.

**Cell types / compartments involved:** neutrophils and their progenitors (promyelocytes, myelocytes) — CL:0000775 (neutrophil), CL:0000557 (granulocyte monocyte progenitor); subcellular compartments — GO:0005789 (ER membrane), GO:0005794 (Golgi apparatus), GO:0042582 (azurophil granule). Anatomy — UBERON:0002371 (bone marrow), UBERON:0000178 (blood), UBERON:0001723 (tongue/oral mucosa for aphthae), UBERON:0002097 (skin).

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [25129144](https://pubmed.ncbi.nlm.nih.gov/25129144/) | *JAGN1 deficiency causes aberrant myeloid cell homeostasis and congenital neutropenia* | Human genetics/cell | Causal gene, AR inheritance, core cellular defects (F1, F2, F7) |
| [25129145](https://pubmed.ncbi.nlm.nih.gov/25129145/) | *Jagunal homolog 1 is a critical regulator of neutrophil function in fungal host defense* | Mouse + human cells | Glycosylation defect, functional killing defect, GM-CSF rescue (F6, F9) |
| [33206996](https://pubmed.ncbi.nlm.nih.gov/33206996/) | *SCN-associated JAGN1 mutations unleash a calpain-dependent cell death programme* | In vitro (HL-60) | Calpain-dependent, caspase-independent apoptosis (F2, F6) |
| [38739706](https://pubmed.ncbi.nlm.nih.gov/38739706/) | *JAGN1-associated SCN zebrafish model: altered G-CSFR signaling and UPR* | Zebrafish | G-CSFR/granulopoiesis as primary driver; UPR secondary (F2, F6, F9) |
| [42685351](https://pubmed.ncbi.nlm.nih.gov/42685351/) | *Jagn1 safeguards neutrophil function by preserving sialylation* | Mouse/Hoxb8 progenitors | Sialylation, C/EBP-α control, adhesion defect (F2, F6, F9) |
| [39775668](https://pubmed.ncbi.nlm.nih.gov/39775668/) | *Extended phenotypes/treatment in 32 JAGN1-deficient patients (ESID/EBMT)* | Human cohort (n=32) | Phenotype spectrum, genotype–phenotype, HSCT (F3, F4) |
| [37120535](https://pubmed.ncbi.nlm.nih.gov/37120535/) | *JAGN1 mutation with distinct clinical features* | Case reports | Additional syndromic features (F3) |
| [39286252](https://pubmed.ncbi.nlm.nih.gov/39286252/) | *GM-CSF sargramostim did not rescue neutrophil phenotype in two JAGN1 patients* | Case reports | Poor G-CSF/GM-CSF response; proceed to HSCT (F4) |
| [41751872](https://pubmed.ncbi.nlm.nih.gov/41751872/) | *Phenotypic variability with c.63G>T variant* | Cohort/review | ~10% of SCN; founder clustering (F1, F7) |
| [38600884](https://pubmed.ncbi.nlm.nih.gov/38600884/) | *Genetic backgrounds of congenital neutropenias in Israel* | Registry | NGS diagnostic tiering; consanguinity; transformation/HSCT rates (F7, F8) |
| [17389229](https://pubmed.ncbi.nlm.nih.gov/17389229/) | *Jagunal is required for reorganizing the ER during Drosophila oogenesis* | Drosophila | Conserved ER-trafficking function (F5, F9) |
| [32783652](https://pubmed.ncbi.nlm.nih.gov/32783652/) | *JAGN1, tetraspanins, and Erv proteins: common topology/cargo sorting?* | Computational/structural | Cargo-sorting hypothesis (F5) |
| [28381427](https://pubmed.ncbi.nlm.nih.gov/28381427/) | *ER partitioned asymmetrically during mitosis in proneural cells* | Drosophila | Jagn in ER partitioning (F5) |
| [36932646](https://pubmed.ncbi.nlm.nih.gov/36932646/) | *Deficiency screen for modifiers of Drosophila Jagunal* | Drosophila | Sec63/Presenilin/Notch genetic interactions (F5) |
| [20456363](https://pubmed.ncbi.nlm.nih.gov/20456363/) | *Stable long-term risk of leukaemia in SCN on G-CSF* | Registry | MDS/AML plateau ~2.3%/yr (F4, F8) |
| [16497969](https://pubmed.ncbi.nlm.nih.gov/16497969/) | *Incidence of leukemia and mortality from sepsis in SCN on G-CSF* | Registry | Poor responders: 40% MDS/AML, 14% sepsis death at 10y (F8) |
| [21072829](https://pubmed.ncbi.nlm.nih.gov/21072829/) | *HSCT in severe congenital neutropenia* | Review | HSCT the only curative therapy; premalignant nature (F4, F8) |

### Comparative context (SCN subtypes)

| Subtype | Gene | Inheritance | G-CSF response | Distinguishing note |
|---|---|---|---|---|
| SCN1 | *ELANE* | AD | Usually responsive | Most common; maturation arrest (PMID 25427142, 41037715) |
| SCN3 (Kostmann) | *HAX1* | AR | Responsive | Neurological features in some transcripts (PMID 37193639) |
| SCN4 | *G6PC3* | AR | Variable | Cardiac/urogenital features, prominent veins (PMID 32623377) |
| **SCN7** | ***JAGN1*** | **AR** | **Poor (most)** | **ER/glycosylation defect; ~10% of SCN; syndromic in ~⅓** |

---

## Limitations and Knowledge Gaps

- **Small evidence base / ultra-rare disease.** The largest dedicated JAGN1 cohort is 32 patients (PMID 39775668); most other clinical data are case reports. Frequencies (e.g., ~38% with syndromic features) rest on small denominators and are subject to ascertainment bias.
- **No formal epidemiology for SCN7 specifically.** Overall SCN incidence is often cited at ~1–2 per million; the JAGN1 share (~10%) is an estimate. True prevalence, incidence, carrier frequency (gnomAD-derived), sex ratio, and geographic-variant distributions are not precisely established.
- **No validated quality-of-life data** (EQ-5D/SF-36/PROMIS) for SCN7.
- **Mechanistic ordering not fully settled.** Whether UPR/apoptosis is strictly secondary to G-CSFR signaling failure (zebrafish, PMID 38739706) versus a parallel driver is not fully resolved in humans; the relative weighting of Branch A vs Branch B for clinical infection risk is inferred, not directly quantified in patients.
- **Therapeutic ambiguity.** GM-CSF rescued fungicidal activity of human cells ex vivo (PMID 25129145) but failed to raise neutrophil counts in two patients (PMID 39286252); the discrepancy between functional rescue and count correction is unexplained.
- **Genotype–phenotype correlations are provisional**, based on modest patient numbers; modifier genes and epigenetic contributors in humans are essentially uncharacterized.
- **Animal-model caveats:** zebrafish paralog redundancy (*jagn1a/jagn1b*) and mouse conditional-vs-global differences complicate direct human extrapolation.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective natural-history registry** for JAGN1-SCN7 through SCNIR/ESID/EBMT to establish incidence, penetrance, sex ratio, MDS/AML transformation rate specific to *JAGN1* (as opposed to pooled SCN), and long-term HSCT outcomes.
2. **Systematic genotype–phenotype mapping** across all reported alleles (c.3G>A start-loss vs c.63G>T/c.130C>T missense) to confirm the "pure vs syndromic" dichotomy with adequate statistical power.
3. **Test calpain inhibition** (e.g., calpeptin/analogous agents) as a mechanism-based strategy to rescue myeloid progenitor survival, building on PMID 33206996.
4. **Glyco-engineering / sialylation restoration** studies (e.g., supplementation or pathway modulation) in patient-derived iPSC-neutrophils, following the sialylation mechanism (PMID 42685351).
5. **Resolve the GM-CSF paradox** — dose/route/timing studies and biomarkers to reconcile ex-vivo functional rescue with in-vivo count failure (PMID 25129145 vs 39286252).
6. **Gene-correction proof-of-concept.** Given HSCT is curative, adapt CRISPR/HDR autologous HSPC correction approaches (as demonstrated for *ELANE*, PMID 32822592) to *JAGN1*, potentially avoiding allo-transplant morbidity.
7. **Population carrier screening** using gnomAD allele frequencies in consanguineous/founder populations (Israel, Romania) to inform genetic counseling and cascade testing.
8. **Standardized MDS/AML surveillance protocol** (serial marrow cytogenetics, *CSF3R* monitoring) tailored to poor-responder SCN7 patients, who carry the highest transformation risk (PMID 16497969).

---

## Section-by-Section Reference Map

- **1. Disease information / identifiers:** MONDO:0014865; OMIM #616022 (phenotype) / \*616012 (gene); MeSH "Congenital Bone Marrow Failure Syndromes"/"Neutropenia"; ICD-10 D70; Orphanet SCN. Synonyms: JAGN1 deficiency, JAGN1-related severe congenital neutropenia. Derived from aggregated disease-level resources + individual patient reports. (F1)
- **2. Etiology:** Biallelic *JAGN1* LOF (genetic; no environmental/infectious primary cause). Risk factors — consanguinity, founder alleles. No established protective factors. (F1, F7)
- **3. Phenotypes:** See table under Finding 3 with HPO terms.
- **4. Genetic/molecular:** *JAGN1*, HGNC:26926; variants pathogenic/likely pathogenic (ACMG); missense/start-loss; germline; loss-of-function. (F1)
- **5. Environmental:** Not a driver; infections are consequences, not causes. (F3)
- **6. Mechanism:** See causal chain and two-branch model. (F2, F5, F6, F9)
- **7. Anatomy:** Bone marrow (UBERON:0002371), blood, oral mucosa, skin, bone. (F3)
- **8. Temporal:** Congenital/neonatal onset; chronic lifelong; premalignant progression. (F3, F8)
- **9. Inheritance/population:** AR; consanguinity/founder effects; ~10% of SCN. (F1, F7)
- **10. Diagnostics:** CBC (ANC <0.5×10⁹/L), marrow maturation arrest, NGS/WES. (F7)
- **11. Prognosis:** Infection- and MDS/AML-driven; poor responders worst. (F4, F8)
- **12. Treatment:** G-CSF (often poor response), GM-CSF (failed in reports), supportive antimicrobials, alloHSCT (curative). (F4)
- **13. Prevention:** Infection prophylaxis, MDS/AML surveillance, genetic counseling, prenatal/carrier testing. (F8)
- **14. Other species:** Conserved orthologs — *Drosophila* Jagn, zebrafish *jagn1a/jagn1b*, mouse *Jagn1*; no described natural companion-animal disease. (F5, F6)
- **15. Model organisms:** Mouse (conditional/global KO), zebrafish (morphant/CRISPR/mutant), *Drosophila* (RNAi/deficiency screens), HL-60 and Hoxb8-ER progenitor cell models. Phenotype recapitulation strong for neutropenia and glycosylation/functional defects. (F5, F6)

---

*Report compiled from 9 confirmed findings and 30 reviewed papers over 5 investigation iterations. Evidence types span human clinical/genetic cohorts, mouse and zebrafish in-vivo models, in-vitro cell systems, and computational/structural analyses.*


## Artifacts

- [OpenScientist final report](Severe_Congenital_Neutropenia_7_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Severe_Congenital_Neutropenia_7_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 18 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:17389229` (7 mentions) - Jagunal is required for reorganizing the endoplasmic reticulum during Drosophila oogenesis.
  - shared terms: cell

Weighed against this report's own most characteristic terms: `jagn1`, `patient`, `cell`, `scn`, `neutropenia`, `neutrophil`, `defect`, `feature`, `phenotype`, `bone`, `model`, `syndromic`, `scn7`, `severe`, `infection`, `g-csf`, `glycosylation`, `variant`, `gm-csf`, `signaling`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 29 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002718` (1 mention) - the report calls it "~all"; HP calls it **Recurrent bacterial infections**
- `HP:0009110` (1 mention) - the report calls it "Subset"; HP calls it **Diaphragmatic eventration**
- `HP:0011107` (1 mention) - the report calls it "Common"; HP calls it **Recurrent aphthous stomatitis**
- `HP:0012758` (1 mention) - the report calls it "Subset (4/32)"; HP calls it **Neurodevelopmental delay**
- `HP:0000938` (1 mention) - the report calls it "Subset"; HP calls it **Osteopenia**
- `HP:0005249` (1 mention) - the report calls it "Subset"; HP calls it **Functional intestinal obstruction**
- `HP:0001508` (1 mention) - the report calls it "Subset"; HP calls it **Failure to thrive**
- `NCIT:C1683` (1 mention) - the report calls it "Filgrastim/G-CSF"; NCIT calls it **Tyrphostin A47**
- `NCIT:C1863` (1 mention) - the report calls it "Sargramostim/GM-CSF"; NCIT calls it **Entinostat**
- `NCIT:C4711` (1 mention) - the report calls it "Allogeneic"; NCIT calls it **Borderline Cystadenoma**
- `UBERON:0001723` (1 mention) - the report calls it "tongue/oral mucosa for aphthae"; UBERON calls it **tongue**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006888` (2 mentions) - the report calls it "ER to Golgi vesicle-mediated transport"; GO calls it **endoplasmic reticulum to Golgi vesicle-mediated transport**, and lists "ER to Golgi vesicle-mediated transport" among its other names
- `GO:0005789` (2 mentions) - the report calls it "endoplasmic reticulum membrane", "ER membrane"; GO calls it **endoplasmic reticulum membrane**, and lists "ER membrane" among its other names
- `CL:0000557` (1 mention) - the report calls it "granulocyte monocyte progenitor"; CL calls it **granulocyte monocyte progenitor cell**, and lists "granulocyte/monocyte progenitor" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005789` - called "endoplasmic reticulum membrane", "ER membrane"