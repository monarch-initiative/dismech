---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-25T17:22:05.254098'
end_time: '2026-10-25T17:33:49.818618'
duration_seconds: 704.56
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neurodevelopmental Disorder With Movement Abnormalities, Abnormal
    Gait, And Autistic Features
  mondo_id: MONDO:0060642
  category: Mendelian
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: NEDMAGA; ZSWIM6-related intellectual disability without frontonasal or
    limb malformations
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
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 5
  validator_version: 0.4.0
term_validation:
  total_terms: 49
  verified: 47
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 3
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0001252
    reported_labels:
    - high
    ontology_label: Hypotonia
  - term_id: HP:0012171
    reported_labels:
    - present
    ontology_label: Stereotypical hand wringing
  - term_id: HP:0001250
    reported_labels:
    - 3/7 (+1 suspected)
    ontology_label: Seizure
  - term_id: HP:0009830
    reported_labels:
    - 1/7 (biopsy-proven)
    ontology_label: Peripheral neuropathy
  - term_id: HP:0001265
    reported_labels:
    - subset
    ontology_label: Hyporeflexia
  - term_id: HP:0002019
    reported_labels:
    - subset
    ontology_label: Constipation
  - term_id: GO:0007224
    reported_labels:
    - Hedgehog
    ontology_label: smoothened signaling pathway
  labels_variant: 4
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_With_Movement_Abnormalities_Abnormal_Gait_And_Autistic_Features-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_With_Movement_Abnormalities_Abnormal_Gait_And_Autistic_Features-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Movement Abnormalities, Abnormal Gait, And Autistic Features
- **MONDO ID:** MONDO:0060642 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** NEDMAGA; ZSWIM6-related intellectual disability without frontonasal or limb malformations
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Movement Abnormalities, Abnormal Gait, And Autistic Features** covering all of the
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

# Neurodevelopmental Disorder With Movement Abnormalities, Abnormal Gait, And Autistic Features (NEDMAGA)

**Causal gene: *ZSWIM6* (Zinc finger SWIM-type containing 6).** NEDMAGA (OMIM **#617865**; MONDO:0060642) is an ultra-rare, autosomal-dominant neurodevelopmental disorder caused by a single recurrent **de novo** heterozygous nonsense variant, **NM_020928.2:c.2737C>T (p.Arg913Ter / R913X)**, in the penultimate exon (exon 13) of *ZSWIM6* on chromosome 5q12.1. It was delineated by Palmer et al. 2017 (PMID 29198722) in 7 unrelated individuals with severe-to-profound intellectual disability **without** the frontonasal/limb malformations seen in the allelic *ZSWIM6* disorder acromelic frontonasal dysostosis (AFND, OMIM #603671; caused by the different missense variant c.3487C>T, p.Arg1163Trp). This report follows the MONDO ID and the stated causal gene; the name correctly points to *ZSWIM6*.

> **Evidence base.** Information is aggregated from fewer than ~10 individual patients described in the primary literature (Palmer 2017, n=7, PMID 29198722; Yanagishita 2021, n=1 Japanese patient, PMID 33958584; Corazza 2024 case report, PMID 38386481) plus disease-level resources (OMIM #617865, ClinVar, UniProt, MGI, ZFIN) and model-organism studies (mouse: Tischfield 2017, PMID 28433741; zebrafish: Smith 2014, PMID 25105228). No large registry, EHR cohort, or natural-history study exists. Evidence source types are flagged throughout as **[human clinical]**, **[model organism]**, **[in vitro]**, or **[computational/database]**.

---

## 1. Disease Information

- **Overview.** NEDMAGA is characterized by infantile-onset global developmental delay, severe-to-profound intellectual disability, mildly delayed walking with a broad-based unsteady gait, absent/minimal language, autistic features with a characteristic *happy demeanor*, and a variety of movement abnormalities (stereotypies, spasticity, dyskinetic movements). It is a multisystem disorder with both central and peripheral nervous system involvement. **[human clinical]**
- **Key identifiers:**
  - **OMIM:** #617865 (disease); *ZSWIM6* gene *615951
  - **MONDO:** MONDO:0060642
  - **ICD-11:** best mapped to LD90.Y / 6A00-range (disorders of intellectual development / developmental disorders); no dedicated code.
  - **ICD-10:** no specific code (maps loosely to F79 / F84).
  - **MeSH:** no dedicated term; covered by "Neurodevelopmental Disorders" (D065886).
  - **Orphanet:** *ZSWIM6* listed by the Gene Curation Coalition; no dedicated ORPHA number with prevalence retrievable.
  - **ClinVar:** Variation ID 431797 (rs1554041295); RCV000578491.
- **Synonyms / alternative names:** NEDMAGA; ZSWIM6-related intellectual disability without frontonasal or limb malformations; ZSWIM6-related neurodevelopmental disorder.

## 2. Etiology

- **Primary cause — genetic.** A single recurrent **de novo** heterozygous nonsense variant in *ZSWIM6*, c.2737C>T (p.Arg913Ter). All tested cases arose de novo (not inherited). **[human clinical]** Direct quote (PMID 29198722): *"seven unrelated individuals with a recurrent de novo nonsense variant (c.2737C>T [p.Arg913Ter]) in the penultimate exon of ZSWIM6 who have severe-profound intellectual disability."*
- **Genetic risk factors.** The causal variant is the sole known genetic determinant; no susceptibility loci or modifier genes have been identified. The variant is a C>T transition at a CpG-associated position (consistent with recurrent de novo mutability).
- **Environmental risk factors.** None identified. As a de novo monogenic disorder, the only recognized correlate of de novo mutation burden generally is advanced paternal age (not specifically demonstrated for NEDMAGA). **Not established for this disease.**
- **Protective factors (genetic or environmental).** None known. **Not applicable.**
- **Gene–environment interactions.** None described. **Not applicable** (fully penetrant monogenic etiology).

## 3. Phenotypes

Frequencies below are from the 7-patient Palmer 2017 cohort unless noted. Because n is tiny, frequencies are approximate.

| Phenotype | Type | Onset | Severity | Course | Frequency | HPO suggestion |
|---|---|---|---|---|---|---|
| Global developmental delay | sign | infantile/congenital | severe | static→slowly progressive | ~100% | HP:0001263 |
| Intellectual disability, severe–profound | sign | infantile | severe-profound | static | ~100% | HP:0010864 / HP:0002187 |
| Absent or minimal speech | sign | childhood | severe | static | ~100% | HP:0001344 |
| Autism / autistic features | behavioral | early childhood | variable | static | 5/7 (~71%) | HP:0000717 / HP:0000729 |
| Hyperactivity | behavioral | childhood | mild-mod | static | 4/7 (~57%) | HP:0000752 |
| Happy demeanor / sociable | behavioral | childhood | — | static | ~100% | HP:0100024 (cheerful disposition) |
| Broad-based, unsteady gait / ataxic gait | sign | toddler (walk 2–5 yr) | mod-severe | some lose ambulation | high | HP:0002136 / HP:0002317 |
| Hypotonia | sign | infantile | mod | may evolve to hypertonia | high | HP:0001252 |
| Spasticity / hypertonia | sign | childhood | mod | progressive | 3/7 | HP:0001257 |
| Stereotypic hand movements | behavioral | childhood | — | static | present | HP:0012171 |
| Paroxysmal tongue movements / head tics | sign | childhood | — | episodic | present | HP:0100022 (abnormal movement) |
| Seizures (well-controlled) | sign | childhood | mild | episodic, treatable | 3/7 (+1 suspected) | HP:0001250 |
| Microcephaly (progressive) | physical | postnatal | — | progressive | 3/7 | HP:0000252 |
| Macrocephaly | physical | — | — | — | 1/7 | HP:0000256 |
| Coarse facies / prominent forehead / short nose / depressed nasal bridge | physical | progressive w/ age | mild | progressive | subset | HP:0000280 / HP:0011220 / HP:0003196 / HP:0005280 |
| Peripheral neuropathy (axonal + demyelinating) | sign/lab | childhood | mod | — | 1/7 (biopsy-proven) | HP:0009830 |
| Hyporeflexia | sign | childhood | — | — | subset | HP:0001265 |
| Reduced pain sensitivity (→ self-injury) | sign | childhood | — | static | 2/7 | HP:0007021 |
| Failure to thrive / poor feeding | sign | infantile | mod | — | subset | HP:0001508 / HP:0011968 |
| Gastroesophageal reflux / vomiting | sign | infantile | variable→severe | may be refractory | subset | HP:0002020 / HP:0002013 |
| Constipation | sign | childhood | mild | chronic | subset | HP:0002019 |

- **Quality-of-life impact.** Profound: non-verbal, dependent for most ADLs, mobility impaired (some non-ambulatory), lifelong care required. Formal QoL instruments (EQ-5D/SF-36/PROMIS) have not been applied. The *happy demeanor* and social responsiveness are notable positive features for caregiver interaction. **[human clinical]**

## 4. Genetic / Molecular Information

- **Causal gene:** *ZSWIM6* — HGNC:29316; NCBI Gene 57688; Ensembl ENSG00000130449; UniProt **Q9HCJ5** (ZSWM6_HUMAN); OMIM gene *615951; locus **5q12.1** (chr5:61,332,258–61,546,172, GRCh38). Paralog: *ZSWIM5*.
- **Pathogenic variant:** NM_020928.2:**c.2737C>T (p.Arg913Ter)**; dbSNP rs1554041295; ClinVar Variation 431797.
  - **Classification:** **Pathogenic** (ACMG support: PS2 de novo, PS4 recurrent in affected/absent in controls, PM2 absent from gnomAD; caveat on PVS1 because it escapes NMD).
  - **Type/class:** nonsense (stop-gain) single-nucleotide variant.
  - **Allele frequency:** 0 — absent from gnomAD, 1000 Genomes, ESP. **[database]**
  - **Origin:** germline, de novo (not somatic/mosaic in probands, though parental germline mosaicism cannot be formally excluded).
  - **Functional consequence:** The variant lies at the 3′ terminus and **does not trigger nonsense-mediated decay**, producing a truncated protein lacking the C-terminal **Sin3-like domain** — proposed **dominant-negative** mechanism. Direct quote (PMID 29198722): *"This finding supports the existence of a truncated ZSWIM6 protein lacking the Sin3-like domain, which could have a dominant-negative effect."* **[in vitro, patient-derived cells]**
  - **Allelic contrast:** AFND is caused by missense c.3487C>T (p.Arg1163Trp) in the same Sin3-like domain, proposed **gain-of-function** (PMID 25105228). Same gene → distinct phenotypes depending on variant.
- **Modifier genes:** none identified.
- **Epigenetic information:** no disease-specific methylation/histone signature reported; note the Sin3-like domain implies a role in transcriptional co-repressor (Sin3/HDAC) complexes, i.e., chromatin regulation, but this is inferred. **Not demonstrated for the disease.**
- **Chromosomal abnormalities:** none — a point mutation, not a CNV/structural change.

## 5. Environmental Information

- **Environmental factors, lifestyle factors, infectious agents:** **None — not applicable.** NEDMAGA is a monogenic de novo disorder with no known toxic, nutritional, behavioral, or infectious contribution.

## 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **de novo** C>T mutation creates *ZSWIM6* c.2737C>T (p.Arg913Ter) **→ leads to** a premature stop codon in the penultimate exon. **[human clinical]**
2. Because the stop is 3′-terminal, it **escapes nonsense-mediated decay → results in** a stable, truncated ZSWIM6 protein lacking the C-terminal **Sin3-like domain**. **[in vitro, demonstrated — mRNA persists in patient cells]**
3. The truncated protein **is inferred to act as a dominant-negative** (interfering with wild-type ZSWIM6 and/or its partner complexes) rather than a simple loss-of-function. **[inferred]**
4. Loss/perturbation of normal ZSWIM6 function **→ dysregulates** its molecular activities: (a) a putative **E3 ubiquitin-ligase** function (ZSWIM6 ubiquitinates NAT10; PMID 38246918) and (b) a **Sin3-like transcriptional co-regulator** role, and **→ is linked to Hedgehog (SHH) pathway dysregulation** (the AFND allele activates Hedgehog; PMID 25105228). **[in vitro; branch — Hedgehog shown for the AFND allele, inferred for NEDMAGA]**
5. In the developing and postnatal brain, ZSWIM6 is **highly expressed in the striatum** (restricted postnatally), so its dysfunction **→ impairs striatal development**, reducing striatal volume and altering **medium spiny neuron (MSN)** morphology. **[model organism — mouse KO, PMID 28433741]**
6. Abnormal striatal/MSN circuitry **→ produces** dysregulated motor control: hyperactivity, impaired motor coordination, repetitive/stereotypic movements, and altered dopaminergic responsiveness (amphetamine hyperresponsiveness in mice). **[model organism]** In humans this **→ manifests as** broad-based unsteady gait, stereotypies, hyperkinetic movements, and autistic repetitive behavior. **[human clinical, inferred linkage]**
7. In parallel, ZSWIM6 dysfunction in peripheral nerve **→ causes** a mixed axonal/demyelinating neuropathy (reduced myelinated-fiber density, thin myelin, abnormal neurofilament accumulation on sural-nerve biopsy) **→ producing** hyporeflexia and reduced pain sensitivity. **[human clinical, 1 biopsy-proven case]**
8. Broad CNS developmental disruption **→ results in** severe-profound intellectual disability, absent language, microcephaly, and (in some) seizures. **[human clinical]**

**Supporting detail by category:**
- **Molecular pathways:** Hedgehog/SHH signaling (GO:0007224 smoothened signaling) — activated by AFND allele, inferred relevance here; ubiquitin–proteasome pathway (via ZSWIM6 E3-ligase activity on NAT10); Sin3/HDAC transcriptional co-repression (inferred from the Sin3-like domain).
- **Cellular processes:** neuronal development and differentiation (GO:0030182), striatal MSN morphogenesis, regulation of locomotion/motor behavior (GO:0040012), protein ubiquitination (GO:0016567), myelination (GO:0042552, peripheral).
- **Protein dysfunction:** truncation removing the Sin3-like domain → dominant-negative; contrast gain-of-function missense in AFND.
- **Molecular profiling:** qRT-PCR of AFND patient osteoblast/fibroblast lines suggested Hedgehog activation (PMID 25105228) **[in vitro]**; no transcriptomic/proteomic/metabolomic/lipidomic dataset exists specifically for NEDMAGA.
- **Functional genomics:** *Zswim6* knockout mouse (reverse genetics) is the principal functional model. No CRISPR/RNAi screens reported.
- **Immune/metabolic involvement:** none described. **Not applicable.**
- **Cell types (CL):** medium spiny neuron (CL:1001474); striatal neuron; myelinating Schwann cell (CL:0002573, peripheral neuropathy).
- **GO biological processes to annotate:** GO:0007399 (nervous system development), GO:0021799 (cerebral cortex development), GO:0007224 (Hedgehog), GO:0016567 (protein ubiquitination).

## 7. Anatomical Structures Affected

- **Organ level / body systems:** Primarily the **central nervous system** (brain) and **peripheral nervous system**; secondary involvement of the **gastrointestinal system** (GERD, constipation, feeding) and **musculoskeletal/muscle** (tone abnormalities). Craniofacial structures mildly affected (dysmorphism). **[human clinical]**
- **Specific CNS sites (UBERON):** **striatum** (UBERON:0002435) and caudate/putamen (UBERON:0001873/UBERON:0001874) — principal site per mouse model; cerebral cortex (UBERON:0000956, mild atrophy in 1 patient); telencephalon (UBERON:0001893); midbrain/hindbrain (developmental expression). Peripheral nerve (UBERON:0001021); sural nerve (UBERON:0003716).
- **Tissue/cell level:** nervous tissue; medium spiny neurons (CL:1001474); peripheral myelinated axons / Schwann cells (CL:0002573).
- **Subcellular (GO cellular component):** nucleus (GO:0005634, for Sin3-like transcriptional function); cytoplasm; the neuropathy shows abnormal **neurofilament** (cytoskeletal) accumulation. **[human clinical, biopsy]**
- **Lateralization:** bilateral / symmetric (generalized neurodevelopmental involvement).

## 8. Temporal Development

- **Onset:** congenital/infantile; global developmental delay evident in infancy; walking delayed to 2–5 years. **Onset pattern:** chronic/insidious (developmental). **[human clinical]**
- **Progression:** largely static developmental disability, but with some **progressive** features — progressive spasticity (3/7), progressive microcephaly (3/7), progressively apparent facial dysmorphism with age, and possible loss of ambulation. Overall slow/variable. **Disease duration:** chronic, lifelong.
- **Patterns:** no remission; seizures are episodic but well-controlled. **Critical period:** early neurodevelopment (prenatal–early childhood) — the window where striatal/cortical circuitry is established; no proven intervention window exists.

## 9. Inheritance and Population

- **Epidemiology:** Ultra-rare; ~8–10 reported individuals worldwide. Palmer et al. estimated the frequency of *ZSWIM6* pathogenic variants at **1.7–4.9 × 10⁻⁴** among patients with neurocognitive disorders (PMID 29198722). True population prevalence/incidence undefined (likely <1/1,000,000). **[human clinical]**
- **Inheritance:** **Autosomal dominant**, essentially always **de novo**. **Penetrance:** complete in reported cases. **Expressivity:** relatively consistent core phenotype with variability in seizures, head size, neuropathy, and GI severity.
- **Genetic anticipation:** not applicable (not a repeat-expansion disorder). **Germline mosaicism:** not reported but theoretically possible → small recurrence risk for apparently unaffected parents. **Founder effect:** none (recurrent de novo at a mutational hotspot, not inherited). **Consanguinity:** not relevant (dominant de novo). **Carrier frequency:** not applicable (variant absent from population databases).
- **Population demographics:** Reported across diverse populations (European-ancestry cohorts in Palmer 2017; a Japanese patient in Yanagishita 2021), indicating no ethnic restriction. **Sex ratio:** not established (small n; includes males and females). **Age distribution:** children through adults (reported ages 3–29 years).

## 10. Diagnostics

- **Primary diagnostic test — genetic.** Diagnosis is molecular: identification of the de novo **c.2737C>T (p.Arg913Ter)** variant in *ZSWIM6*.
  - **WES / WGS:** first-line and the method by which the disorder was discovered; trio (proband + parents) exome/genome sequencing demonstrates de novo status. High utility.
  - **Gene panels:** intellectual disability / autism / epilepsy NGS panels that include *ZSWIM6*.
  - **Single-gene / targeted testing:** Sanger confirmation of the recurrent variant.
  - **CMA / karyotype / FISH:** normal (no structural abnormality) — useful to exclude differentials, not diagnostic here.
  - **mtDNA / repeat-expansion testing:** not applicable.
- **Supportive clinical tests (characterize, not diagnose):**
  - **Brain MRI:** usually **normal** (5/7); mild cortical atrophy in 1. **[human clinical]**
  - **EEG:** for seizure evaluation in affected subset.
  - **Nerve conduction studies / EMG:** may show mixed axonal–demyelinating neuropathy.
  - **Sural nerve biopsy:** reduced myelinated-fiber density, thin myelin, neurofilament accumulation (research/selected cases).
  - **Routine labs/metabolic workup:** non-specific/normal; no diagnostic biomarker exists.
- **Biomarkers:** none; the genetic variant is the only specific marker. No FDA biomarker.
- **Clinical criteria / differential diagnosis:** No formal criteria. Differentials include Rett syndrome and *MEF2C*-related disorder (NEDHSIL, OMIM #613443 — overlapping stereotypies/hypotonia/absent speech), Angelman syndrome (happy demeanor, ataxic gait, ID), other ID/ASD syndromes, and hereditary spastic paraplegia/CMT-overlap (for the neuropathy/spasticity). *ZSWIM6*-AFND is distinguished by frontonasal/limb malformations (absent in NEDMAGA). Resolution is by genetic testing.
- **Screening:** No newborn/population screening. Cascade testing of parents is for recurrence-risk counseling; because variant is de novo, parental testing is typically negative.

## 11. Outcome / Prognosis

- **Survival/mortality:** No systematic mortality data; patients survive into adulthood (oldest reported 29 years). Life-threatening risk relates to severe refractory GERD/aspiration and feeding failure in the most severe cases. **[human clinical]**
- **Morbidity/disability:** Severe lifelong disability — non-verbal, intellectual disability, impaired mobility (some non-ambulatory), dependence for ADLs. ICF domains broadly affected.
- **QoL measures:** none formally applied.
- **Complications:** seizures, spasticity/contractures, feeding difficulties/GERD with vomiting (can be refractory even after gastrostomy), self-injury from reduced pain sensitivity, aspiration.
- **Recovery potential:** none for the core disability; supportive care improves function/comfort.
- **Prognostic factors:** severity of feeding/GI involvement and ambulation status are the main functional determinants; no molecular prognostic biomarker (single recurrent variant).

## 12. Treatment

**No curative or disease-specific/targeted therapy exists; management is entirely supportive and symptom-directed.**

- **Pharmacotherapy (symptomatic):**
  - **Antiepileptic/anticonvulsant drugs** for seizures (well-controlled in reported patients). NCIT: Anticonvulsant Agent.
  - **Anti-reflux therapy** (proton-pump inhibitors, prokinetics) for GERD/vomiting; NCIT: Proton Pump Inhibitor.
  - **Laxatives/bowel regimen** for constipation.
  - Agents for spasticity (e.g., baclofen) and behavioral/hyperactivity management as clinically indicated.
  - **Pharmacogenomics:** none specific to *ZSWIM6*.
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** **None available or in trials.** Conceptually, a dominant-negative, NMD-escaping allele might be amenable to allele-selective antisense-oligonucleotide/RNA knockdown, but this is hypothetical and not under development. **Not applicable currently.**
- **Surgical/interventional:** **Gastrostomy (PEG)** for feeding failure (note GERD may persist post-PEG; anti-reflux surgery/fundoplication may be considered). NCIT: Gastrostomy.
- **Supportive/rehabilitative:** **Physical therapy** (gait, spasticity, contracture prevention), **occupational therapy**, **speech/communication therapy** (AAC given absent language), nutritional support, orthopedic/management of tone, protective measures for pain-insensitivity self-injury. NCIT: Physical Therapy; Occupational Therapy; Speech Therapy; Supportive Care.
- **Experimental trials:** none (no NCT identifiers).
- **Treatment outcomes/strategy:** symptom-based multidisciplinary care; seizures generally respond well; GERD may be refractory. No treatment algorithm or precision-medicine approach established.

## 13. Prevention

- **Primary prevention:** Not possible for a sporadic de novo disorder. **Genetic counseling** is central: recurrence risk for parents of an affected child is low (de novo), but ~**50%** for an affected individual's own offspring (dominant) — though reproduction is unlikely given severity.
- **Secondary prevention (early detection):** Early genetic diagnosis via trio WES/WGS enables early intervention (developmental therapies) and anticipatory management of seizures/GI issues. **Prenatal testing / preimplantation genetic testing (PGT)** are available for the known variant in the rare situation of a prior affected child (covers germline-mosaicism risk).
- **Tertiary prevention:** Prevent complications — aspiration/reflux management, seizure control, contracture prevention (PT), protection from self-injury, nutritional optimization.
- **Immunization / behavioral / public-health / environmental interventions:** Not applicable (no environmental/infectious component).

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *ZSWIM6* is conserved across vertebrates — human (NCBI Taxon 9606), mouse *Zswim6* (Taxon 10090; NCBI Gene 67263; MGI:1914513; ENSMUSG00000032846), rat *Zswim6* (Taxon 10116; NCBI Gene 310062; RGD 1306624), zebrafish *zswim6* (Taxon 7955; ZFIN ZDB-GENE-060602-4). 1:1 orthology (stringent).
- **Natural disease in other species:** **None reported** — no entry in OMIA; no naturally occurring NEDMAGA-equivalent in companion animals or wildlife. No breed (VBO) associations. **Not applicable.**
- **Comparative biology:** Conserved brain expression (striatal/telencephalic) across mouse and zebrafish supports an evolutionarily conserved neurodevelopmental role.
- **Transmission / zoonosis:** Not applicable (genetic, non-communicable).

## 15. Model Organisms

- **Mouse — *Zswim6* knockout (Tischfield et al. 2017, PMID 28433741) [model organism].** Mammalian, germline knockout. **Phenotype recapitulation:** reduced striatal volume, altered medium-spiny-neuron morphology, hyperactivity, impaired rotarod performance, repetitive movements, amphetamine hyperresponsiveness — recapitulating NEDMAGA's motor-regulation and repetitive/autistic-like features and localizing function to the striatum. Direct quote: *"Loss of Zswim6 causes a reduction in striatal volume and changes in medium spiny neuron morphology. These changes are associated with alterations in motor control, including hyperactivity, impaired rotarod performance, repetitive movements, and behavioral hyperresponsiveness to amphetamine."* **Limitation:** it is a loss-of-function model, whereas the human allele is a NMD-escaping, truncating, proposed **dominant-negative** variant; the KO may therefore under- or mis-represent human pathobiology; craniofacial/AFND features and the specific human truncation are not modeled. Resource: MGI:1914513; IMPC.
- **Zebrafish — *zswim6* (Smith et al. 2014, PMID 25105228) [model organism].** Used for developmental expression mapping (telencephalic at 24 hpf; midbrain/hindbrain/retinal at 48 hpf), supporting a neurodevelopmental role. Resource: ZFIN ZDB-GENE-060602-4.
- **In vitro / cellular models:** patient-derived osteoblast/fibroblast lines (AFND, Hedgehog qRT-PCR; PMID 25105228) and patient-derived cells showing NMD escape of the NEDMAGA allele (PMID 29198722). No iPSC/organoid model reported for NEDMAGA.
- **Applications:** mouse KO enables study of striatal circuitry, motor behavior, and MSN biology; zebrafish for developmental expression. **Gaps:** no knock-in model of p.Arg913Ter to test the dominant-negative hypothesis.

---

## Limitations and Future Directions

- **Evidence is extremely sparse** (<10 patients, single defining cohort), so frequencies and genotype–phenotype correlations are preliminary; sex ratio, prevalence, and natural history are undefined.
- **Mechanism is partly inferred:** the dominant-negative effect and Hedgehog involvement for the NEDMAGA allele are hypotheses extrapolated from the AFND allele and the Sin3-like domain; NMD escape and striatal expression are the best-demonstrated steps.
- **No targeted therapy or trials;** an allele-selective knockdown strategy is a logical but untested future direction.
- **Priority future work:** a knock-in p.Arg913Ter mouse/iPSC-neuron model to test dominant-negative vs loss-of-function; transcriptomic/proteomic profiling of patient neurons; a patient registry (humandiseasegenes.nl/zswim6) to define natural history; clarification of the severe refractory GERD mechanism.

### Key references
- Palmer EE, et al. *Am J Hum Genet.* 2017. **PMID 29198722** — defining NEDMAGA cohort, p.Arg913Ter, NMD escape, dominant-negative hypothesis. [human clinical / in vitro]
- Smith JD, et al. *Am J Hum Genet.* 2014. **PMID 25105228** — AFND, p.Arg1163Trp, Hedgehog activation, zebrafish expression. [human clinical / model organism]
- Tischfield DJ, et al. *Neurobiol Dis.* 2017. **PMID 28433741** — *Zswim6* knockout mouse striatal/motor phenotype. [model organism]
- Yanagishita T, et al. *Hum Genome Var.* 2021. **PMID 33958584** — second NEDMAGA patient; epilepsy, microcephaly, refractory GERD. [human clinical]
- Corazza G, et al. *Mov Disord Clin Pract.* 2024. **PMID 38386481** — NEDMAGA case report (movement-disorder perspective). [human clinical]
- Wang Y, et al. 2024. **PMID 38246918** — ZSWIM6 as an E3 ubiquitin ligase (NAT10). [in vitro]


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_With_Movement_Abnormalities_Abnormal_Gait_And_Autistic_Features-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_With_Movement_Abnormalities_Abnormal_Gait_And_Autistic_Features-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001252` (1 mention) - the report calls it "high"; HP calls it **Hypotonia**
- `HP:0012171` (1 mention) - the report calls it "present"; HP calls it **Stereotypical hand wringing**
- `HP:0001250` (1 mention) - the report calls it "3/7 (+1 suspected)"; HP calls it **Seizure**
- `HP:0009830` (1 mention) - the report calls it "1/7 (biopsy-proven)"; HP calls it **Peripheral neuropathy**
- `HP:0001265` (1 mention) - the report calls it "subset"; HP calls it **Hyporeflexia**
- `HP:0002019` (1 mention) - the report calls it "subset"; HP calls it **Constipation**
- `GO:0007224` (2 mentions) - the report calls it "Hedgehog"; GO calls it **smoothened signaling pathway**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0100024` (1 mention) - the report calls it "cheerful disposition"; HP calls it **Conspicuously happy disposition**
- `HP:0100022` (1 mention) - the report calls it "abnormal movement"; HP calls it **Abnormality of movement**
- `GO:0030182` (1 mention) - the report calls it "Cellular processes:** neuronal development and differentiation"; GO calls it **neuron differentiation**
- `GO:0021799` (1 mention) - the report calls it "cerebral cortex development"; GO calls it **cerebral cortex radially oriented cell migration**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.