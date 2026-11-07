---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T15:29:40.418678'
end_time: '2026-10-30T15:40:54.434664'
duration_seconds: 674.02
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Combined Oxidative Phosphorylation Defect Type 3
  mondo_id: MONDO:0012512
  category: Mendelian
  causal_genes: TSFM
  omim_id: OMIM:610505
  synonyms: combined oxidative phosphorylation deficiency type 3; TSFM combined oxidative
    phosphorylation deficiency; combined oxidative phosphorylation deficiency caused
    by mutation in TSFM; fatal mitochondrial disease due to COXPD3
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
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 11
  on_topic: 10
  validator_version: 0.4.0
term_validation:
  total_terms: 40
  verified: 38
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 0
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0001639
    reported_labels:
    - common (a presenting feature in many)
    ontology_label: Hypertrophic cardiomyopathy
  - term_id: HP:0001644
    reported_labels:
    - subset
    ontology_label: Dilated cardiomyopathy
  - term_id: HP:0003128
    reported_labels:
    - very common
    ontology_label: Lactic acidosis
  - term_id: HP:0002415
    reported_labels:
    - common in neuro forms
    ontology_label: Leukodystrophy
  - term_id: HP:0001251
    reported_labels:
    - subset
    ontology_label: Ataxia
  - term_id: HP:0000648
    reported_labels:
    - subset
    ontology_label: Optic atrophy
  - term_id: HP:0009830
    reported_labels:
    - subset
    ontology_label: Peripheral neuropathy
  - term_id: HP:0000407
    reported_labels:
    - subset
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0001511
    reported_labels:
    - subset
    ontology_label: Intrauterine growth retardation
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
  path: Combined_Oxidative_Phosphorylation_Defect_Type_3-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Oxidative_Phosphorylation_Defect_Type_3-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Defect Type 3
- **MONDO ID:** MONDO:0012512 (if available)
- **Causal gene(s):** TSFM
- **OMIM:** OMIM:610505
- **Synonyms:** combined oxidative phosphorylation deficiency type 3; TSFM combined oxidative phosphorylation deficiency; combined oxidative phosphorylation deficiency caused by mutation in TSFM; fatal mitochondrial disease due to COXPD3
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Defect Type 3** covering all of the
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

# Combined Oxidative Phosphorylation Deficiency Type 3 (COXPD3) — Comprehensive Disease Report

**Causal gene: _TSFM_ (mitochondrial translation elongation factor Ts, EF‑Ts).** COXPD3 is an autosomal‑recessive mitochondrial disease caused by biallelic pathogenic variants in the nuclear gene **TSFM**, which encodes mitochondrial elongation factor Ts (EF‑Ts). EF‑Ts is the guanine‑nucleotide‑exchange factor (GEF) for elongation factor Tu (EF‑Tu/TUFM); loss of EF‑Ts destabilizes EF‑Tu and cripples synthesis of the 13 mtDNA‑encoded oxidative‑phosphorylation (OXPHOS) subunits, producing a **combined (multiple) respiratory‑chain complex deficiency** — the defining biochemical lesion of this disorder (PMID 17033963).

> Evidence source types are flagged throughout as **[human clinical]**, **[in vitro]**, **[computational]**, or **[model organism]**.

---

## 1. Disease Information

**Overview.** COXPD3 is a rare, severe, clinically heterogeneous primary mitochondrial disorder of mitochondrial protein synthesis. Because the 13 polypeptides encoded by mtDNA are all core OXPHOS subunits, a translation‑elongation defect reduces assembly of complexes I, III, IV and V simultaneously (complex II, entirely nuclear‑encoded, is spared), impairing ATP generation in energy‑dependent tissues (heart, brain, optic nerve, liver, skeletal muscle). **[human clinical / in vitro]** (PMID 17033963)

**Key identifiers.**
- **MONDO:** MONDO:0012512
- **OMIM (phenotype):** 610505 (COXPD3); **OMIM (gene):** 604723 (TSFM)
- **Orphanet:** mitochondrial DNA translation‑defect / combined OXPHOS deficiency group (ORPHA:254913 "Combined oxidative phosphorylation defect"; subtype‑level)
- **ICD‑11:** 5C53.0 (disorders of mitochondrial energy metabolism / nuclear‑encoded) — code at category level
- **ICD‑10:** E88.49 (other mitochondrial metabolism disorders)
- **MeSH:** "Mitochondrial Diseases"; "OXPHOS" / "Oxidative Phosphorylation" (no COXPD3‑specific MeSH)
- **Gene:** HGNC:11701, NCBI Gene 10102, Ensembl ENSG00000123297, UniProt P43897

**Synonyms:** combined oxidative phosphorylation deficiency type 3; TSFM combined oxidative phosphorylation deficiency; combined oxidative phosphorylation deficiency caused by mutation in TSFM; fatal mitochondrial disease due to COXPD3; (EF‑Ts deficiency; mitochondrial translation elongation factor Ts deficiency).

**Information source.** Derived from **aggregated disease‑level resources** (OMIM, Orphanet) built from **individual patient case reports and small case series** — this is an ultra‑rare disorder with only a few dozen reported families; no large EHR cohorts exist.

---

## 2. Etiology

**Causal factors — genetic (Mendelian).** Biallelic (homozygous or compound‑heterozygous) loss‑of‑function/hypomorphic variants in **TSFM**. No environmental or infectious cause; disease is fully determined by genotype. **[human clinical]** (PMID 17033963, 21741925, 25037205).

**Genetic risk factors.**
- Causal variants: see Section 4. The recurrent **c.997C>T (p.Arg333Trp;** older numbering **R312W)** is the most frequently reported allele and causes the most severe outcomes.
- **Consanguinity** underlies many homozygous cases (reported Pakistani, Mediterranean, and other families). 
- **Founder effect:** Finnish p.Gln286X (c.856C>T) nonsense allele with carrier frequency ~1:80 (PMID 25037205).

**Environmental / lifestyle / infectious factors.** None established as causal. As in other mitochondrial diseases, **intercurrent infection, fever, fasting, and catabolic/metabolic stress** can precipitate acute decompensation (metabolic crises, lactic acidosis) — a gene‑environment interaction at the level of energy demand rather than disease causation. Certain mitochondrial toxins (e.g., aminoglycosides, valproate, some anaesthetics) are best avoided but are not disease triggers per se. **[inferred from mitochondrial‑disease class knowledge]**

**Protective factors.** None genetically defined. The compensatory up‑regulation of EF‑Tu and mitochondrial biogenesis seen in some patient tissues is an endogenous buffering mechanism that may mitigate severity in sparable tissues (PMID 30911037) **[in vitro]**.

---

## 3. Phenotypes

COXPD3 shows **marked phenotypic heterogeneity**; the same genotype (R333W) can present as encephalomyopathy, cardiomyopathy, or liver failure (PMID 21741925). Core manifestations with suggested HPO terms:

| Phenotype | Type | Onset | Severity / course | Frequency | HPO |
|---|---|---|---|---|---|
| Hypertrophic cardiomyopathy | clinical sign | neonatal–infantile | severe, often progressive | common (a presenting feature in many) | HP:0001639 |
| Dilated cardiomyopathy (± fibro‑adipose replacement) | clinical sign | variable (to adulthood) | severe, end‑stage → transplant | subset | HP:0001644 |
| Lactic acidosis | lab abnormality | neonatal–infantile | moderate–severe, episodic ↔ persistent | very common | HP:0003128 |
| Leigh / Leigh‑like encephalopathy | clinical sign | infantile–juvenile | progressive | common in neuro forms | HP:0002415 |
| Ataxia | clinical sign | childhood–juvenile | slowly progressive | subset | HP:0001251 |
| Optic atrophy | clinical sign | juvenile | progressive | subset | HP:0000648 |
| Peripheral neuropathy | clinical sign | juvenile | progressive | subset | HP:0009830 |
| Sensorineural hearing loss | clinical sign | childhood | progressive | subset | HP:0000407 |
| Encephalopathy / developmental delay / hypotonia | clinical sign | infantile | severe | common in neuro forms | HP:0001263 / HP:0001252 |
| Hepatic failure / dysfunction | clinical sign | neonatal | severe, often fatal | subset | HP:0001399 / HP:0001410 |
| Intrauterine growth retardation | physical | prenatal | — | subset | HP:0001511 |

**Quality‑of‑life impact.** Severe across forms: infantile presentations are frequently fatal; survivors have major disability from cardiac failure, neurodegeneration (Leigh disease), blindness (optic atrophy), deafness, ataxia and neuropathy, with high dependency for daily functioning. No disease‑specific QoL instrument (EQ‑5D/SF‑36) data exist; generic mitochondrial‑disease QoL is markedly reduced. **[human clinical]** (PMID 17033963, 25037205, 30911037)

---

## 4. Genetic / Molecular Information

**Causal gene.** TSFM (HGNC:11701; NCBI Gene 10102; Ensembl ENSG00000123297; UniProt P43897; OMIM 604723), chromosome **12q14.1**. Encodes mitochondrial EF‑Ts.

**Reported pathogenic variants (all germline, autosomal recessive):**
- **c.997C>T, p.Arg333Trp** (a.k.a. R312W in shorter isoform numbering) — recurrent missense; most severe; homozygous in encephalomyopathy, HCM, and infantile liver failure (PMID 17033963, 21741925). Also seen compound‑het with p.Val119Leu (PMID 35071363).
- **c.944G>A, p.Cys315Tyr** and **c.856C>T, p.Gln286X** (nonsense) — Finnish, compound‑het, juvenile Leigh/neuropathy/optic atrophy (PMID 25037205).
- **c.547G>A, p.Gly183Ser** — homozygous; encephalocardiomyopathy + sensorineural hearing loss (PMID 31267352).
- Novel compound‑heterozygous variants causing dilated cardiomyopathy with fibro‑adipose replacement (PMID 30911037).
- A homozygous missense causing childhood ataxia + HCM (PMID 27677415).

**Variant classification (ACMG/AMP):** recurrent alleles are **Pathogenic/Likely Pathogenic** (functional rescue evidence PS3; recurrence/segregation; rarity in gnomAD). **Variant types:** predominantly **missense**, plus **nonsense (p.Q286X)** and **splice‑site** alleles. **Allele frequencies:** very rare globally in gnomAD; p.Q286X enriched in Finland (~1:80 carriers). **Functional consequence:** **loss of function** via protein destabilization (reduced EF‑Ts steady‑state → secondary EF‑Tu loss); no gain‑of‑function/dominant‑negative mechanism. **[in vitro/computational]** (PMID 17033963, 25037205)

**Modifier genes.** Not specifically identified for TSFM, but tissue‑specific and nuclear‑modifier influences are invoked to explain why identical genotypes yield divergent organ phenotypes; "unknown factors" are explicitly cited (PMID 27677415). EF‑Tu (TUFM) abundance is a candidate buffering modifier (PMID 30911037).

**Epigenetic / chromosomal abnormalities.** None described; COXPD3 is a single‑gene point‑mutation disorder without reported methylation changes or large structural/cytogenetic lesions.

---

## 5. Environmental Information

**Environmental factors:** none causal. **Lifestyle factors:** not applicable to a monogenic infantile disease; avoidance of mitochondrial‑toxic drugs and catabolic stressors is prudent management. **Infectious agents:** none causal; intercurrent infections can trigger metabolic decompensation. **[not applicable / inferred]**

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic TSFM mutation** → produces a **misfolded/unstable EF‑Ts protein** (loss of function; R333W disrupts the subdomain structure and the EF‑Ts dimerization/EF‑Tu‑interaction interface — *demonstrated by molecular modeling and reduced steady‑state protein*). (PMID 17033963)
2. → **reduced steady‑state EF‑Ts**, which **leads to secondary depletion of EF‑Tu** (EF‑Ts is EF‑Tu's nucleotide‑exchange factor; patient fibroblasts: EF‑Ts −75%, EF‑Tu −60%). (PMID 17033963)
3. → **impaired formation/recycling of the EF‑Tu·GTP·aminoacyl‑tRNA ternary complex**, which **results in defective delivery of aminoacyl‑tRNAs to the mitoribosomal A‑site** and **stalled translation elongation**. (*mechanistically inferred from EF‑Ts/EF‑Tu biochemistry; translation defect demonstrated*) (PMID 25037205)
4. → **decreased synthesis of the 13 mtDNA‑encoded OXPHOS subunits**, which **leads to impaired assembly of respiratory‑chain complexes I, III, IV and V** (complexes reduced 35–91%; complex II spared because it is fully nuclear‑encoded). (PMID 17033963)
5. → **reduced oxidative phosphorylation / ATP output**, which **results in a shift to anaerobic glycolysis → lactate accumulation → lactic acidosis**. (PMID 21741925)
6. → **energy failure in high‑demand post‑mitotic tissues**, which **leads to cell dysfunction, apoptosis/necrosis, and tissue injury** — branching by organ:
   - **Heart** → hypertrophic or dilated cardiomyopathy, biventricular fibro‑adipose replacement (PMID 30911037);
   - **CNS (basal ganglia, brainstem)** → Leigh‑like necrotizing encephalopathy (PMID 25037205);
   - **Optic nerve / peripheral nerve** → optic atrophy, neuropathy;
   - **Liver** → hepatocellular failure (PMID 21741925);
   - **Cochlea** → sensorineural hearing loss (PMID 31267352).
7. **Compensatory branch (partially protective):** in some tissues, **EF‑Tu up‑regulation + induction of mitochondrial biogenesis** restores oxygen consumption, **explaining tissue‑specific sparing** (e.g., fibroblasts normal despite affected myocardium). (PMID 30911037)

### Supporting detail
- **Molecular pathways / biochemistry:** mitochondrial translation (KEGG hsa03010‑analogous mitoribosome machinery); OXPHOS (KEGG hsa00190; Reactome "Respiratory electron transport"). GO biological processes: **mitochondrial translational elongation (GO:0070125)**, **oxidative phosphorylation (GO:0006119)**, **mitochondrial respiratory chain complex assembly (GO:0033108)**. GO molecular functions: **translation elongation factor activity (GO:0003746)**, **guanyl‑nucleotide exchange factor activity (GO:0005085)**.
- **Cellular processes:** energy‑deprivation‑triggered apoptosis/necrosis; integrated stress / mitochondrial biogenesis response (inferred).
- **Protein dysfunction:** destabilization / loss of function at the EF‑Ts–EF‑Tu interface (PDB homologs of bacterial EF‑Ts; AlphaFold model of P43897). **[computational]**
- **Metabolic changes:** elevated lactate, pyruvate, alanine; secondary TCA‑cycle/energy‑metabolism disruption (CHEBI: lactate CHEBI:24996).
- **Immune involvement:** none (not an immune‑mediated disease).
- **Tissue‑damage mechanism:** bioenergetic failure/oxidative stress → cell death; cardiac fibro‑adipose remodeling.
- **Molecular profiling:** patient myocardium/fibroblasts show reduced EF‑Ts/EF‑Tu, combined complex deficiency, and compensatory biogenesis transcriptional signatures (PMID 30911037) **[in vitro]**. No dedicated single‑cell/spatial/CRISPR‑screen datasets specific to TSFM.

**Upstream vs downstream:** mutation → protein instability (most upstream) → translation defect → OXPHOS assembly failure → ATP deficit/lactic acidosis → organ‑specific cell death (most downstream).
**Cell types (CL):** cardiomyocyte (CL:0000746), neuron (CL:0000540), hepatocyte (CL:0000182), skeletal muscle cell (CL:0000188). **Subcellular (GO‑CC):** mitochondrion (GO:0005739), mitochondrial matrix (GO:0005759).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** heart (UBERON:0000948); brain — basal ganglia (UBERON:0002420), brainstem (UBERON:0002298); optic nerve (UBERON:0000941); liver (UBERON:0002107); skeletal muscle (UBERON:0001134); peripheral nerve (UBERON:0001021); inner ear/cochlea (UBERON:0001844).
- **Body systems:** cardiovascular, central & peripheral nervous, hepatic/digestive, musculoskeletal, special sensory (visual, auditory).
- **Secondary involvement:** heart failure → systemic hypoperfusion; hepatic failure → coagulopathy; failure to thrive/IUGR.
- **Tissue/cell level:** cardiac muscle (cardiomyocytes, CL:0000746), CNS neurons/glia (CL:0000540), hepatocytes (CL:0000182), skeletal myocytes.
- **Subcellular:** mitochondrion / mitochondrial matrix (GO:0005739 / GO:0005759); biopsy shows mitochondrial hyperplasia/proliferation (PMID 35071363).
- **Localization / laterality:** CNS lesions are characteristically **bilateral and symmetric** (Leigh pattern). **[human clinical]**

---

## 8. Temporal Development

- **Onset:** congenital/neonatal to juvenile. Most severe (R333W homozygous) → **neonatal–infantile**; hypomorphic genotypes → **childhood–adolescent** onset. Onset pattern ranges acute (neonatal lactic‑acidotic crisis) to insidious/chronic (slowly progressive ataxia). (PMID 17033963, 21741925, 27677415, 25037205)
- **Progression:** generally **chronic‑progressive**; cardiac disease can advance to end‑stage requiring transplant; neuro forms show stepwise/progressive decline, sometimes with partially reversible neuroimaging changes (PMID 31267352).
- **Course pattern:** progressive, with episodic metabolic decompensations superimposed on a declining baseline.
- **Duration:** lifelong; infantile forms often fatal within the first months–years.
- **Critical periods:** neonatal/infancy is the window of greatest vulnerability and of greatest potential benefit from early supportive intervention. **[human clinical]**

---

## 9. Inheritance and Population

- **Epidemiology:** no COXPD3‑specific prevalence; it is ultra‑rare (<1/1,000,000; only a few dozen families reported). Primary mitochondrial disease collectively affects **≥1 in 4,300** (PMID 33105273).
- **Inheritance:** **autosomal recessive** (biallelic). (PMID 17033963, 25037205)
- **Penetrance:** effectively complete for biallelic pathogenic genotypes; **expressivity highly variable** (organ and severity differ even for identical genotypes) (PMID 21741925, 27677415).
- **Genetic anticipation / germline mosaicism:** not reported / not applicable.
- **Founder effect:** **Finnish p.Q286X**, carrier frequency **~1:80**; notably **no homozygotes** among 35,000 controls or patients, consistent with lethality of that genotype (PMID 25037205).
- **Consanguinity:** major contributor to homozygous cases worldwide.
- **Carrier frequency:** high regionally (Finland); otherwise rare.
- **Demographics:** reported across populations (Finnish, Pakistani/Pakhtun, Mediterranean, Chinese, others); no strong sex bias (autosomal); age distribution skewed to infancy/childhood. **[human clinical]**

---

## 10. Diagnostics

- **Laboratory:** elevated **blood & CSF lactate** (LOINC 2524‑7), elevated pyruvate, **elevated plasma alanine**, lactic aciduria with increased TCA intermediates. (PMID 38571879)
- **Biopsy / biochemistry:** muscle or cardiac biopsy shows **combined reduction of respiratory‑chain complexes I, III, IV with normal complex II**, plus **mitochondrial hyperplasia/proliferation** and sometimes COX‑deficient fibres (PMID 35071363, 17033963). This **combined, complex‑II‑sparing** pattern is a key diagnostic signature.
- **Imaging:** brain MRI — **bilateral symmetric T2‑hyperintense lesions of basal ganglia/brainstem** (Leigh pattern); **MR spectroscopy lactate peak** (PMID 38571879). Echocardiography for cardiomyopathy.
- **Electrophysiology:** ECG (cardiomyopathy/arrhythmia), nerve‑conduction studies (neuropathy), BAER/audiometry (hearing loss).
- **Genetic testing (definitive):** **WES/WGS** or **NGS mitochondrial/nuclear multigene panels** identifying biallelic TSFM variants, with Sanger confirmation and parental segregation. **mtDNA testing is typically normal** (nuclear‑gene disorder) and helps exclude mtDNA Leigh/mito‑cardiomyopathy. (PMID 25037205, 30911037, 35071363)
- **Omics diagnostics:** research‑level proteomics/transcriptomics (reduced EF‑Ts/EF‑Tu; biogenesis signatures). No routine metabolomic/epigenomic test.
- **Clinical criteria / differential:** distinguish from other **mitochondrial translation‑factor defects (GFM1/EF‑G1, TUFM/EF‑Tu, mt‑aminoacyl‑tRNA synthetases)**, **mtDNA‑encoded Leigh syndrome**, **POLG disease**, and other combined‑OXPHOS‑deficiency genes. (PMID 35703069, 22283595)
- **Screening:** no newborn screening; **carrier/cascade testing** and **prenatal/PGT** feasible once familial variants are known (relevant in Finnish founder and consanguineous families). **[human clinical]**

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **poor** overall; the recurrent severe allele causes **fatal infantile** encephalomyopathy, HCM, or neonatal liver failure (PMID 17033963, 21741925). Hypomorphic genotypes allow survival into childhood/adolescence/adulthood (PMID 25037205, 27677415).
- **Morbidity/disability:** high — cardiac failure, neurodegeneration, blindness (optic atrophy), deafness, ataxia, neuropathy; severe dependency.
- **Complications:** intractable heart failure, metabolic/lactic‑acidotic crises, hepatic failure, respiratory failure, feeding difficulties.
- **Recovery:** limited; some neuroimaging changes partially reversible (PMID 31267352), but structural damage is generally irreversible. **Cardiac transplantation** rescued an adult with end‑stage TSFM dilated cardiomyopathy (PMID 30911037).
- **Prognostic factors:** **genotype severity (residual EF‑Ts function)**, age/organ of onset, and **degree of cardiac involvement** are the main determinants. No validated circulating prognostic biomarker specific to TSFM (GDF‑15 is a general mitochondrial‑disease marker). **[human clinical]**

---

## 12. Treatment

**No disease‑specific or curative therapy exists.** Management is **supportive, organ‑directed, and empiric** (PMID 33105273, 11282042).

- **Pharmacotherapy / "mito cocktail" (NCIT‑relevant, empiric):** Coenzyme Q10/ubiquinone (CHEBI:16389), riboflavin (CHEBI:17015), thiamine (CHEBI:18385), L‑carnitine (CHEBI:16347), **vitamin E** and **N‑acetylcysteine** (strongest preclinical antioxidant evidence), B‑vitamins; **L‑arginine** for stroke‑like episodes. **Vitamin C lacks efficacy**; **L‑carnitine** use is nuanced (possible pro‑atherogenic signal). Combinatorial **glucose + nicotinic acid + N‑acetylcysteine** was synergistic in complex‑I disease models. (PMID 33105273, 33640978)
- **Pharmacogenomics:** avoid mitochondrial‑toxic drugs (aminoglycosides, valproate, certain anaesthetics); no TSFM‑specific PGx guidance.
- **Advanced therapeutics:** no approved gene, cell, RNA, or targeted therapy; none in trials specifically for TSFM. Gene replacement is conceptually attractive (EF‑Ts cDNA rescues patient cells in vitro — PMID 17033963) but not clinically available.
- **Surgical/interventional:** **heart transplantation** for end‑stage cardiomyopathy (NCIT heart transplantation) (PMID 30911037); cardiac device/HF management; cochlear implantation for deafness (supportive).
- **Supportive/rehabilitative:** HF pharmacotherapy, anti‑seizure medication, nutritional/feeding support, management of lactic acidosis; physical/occupational/speech therapy; low‑vision and audiologic rehabilitation.
- **Treatment outcomes:** no validated response rates; evidence base weak owing to rarity and heterogeneity (no RCTs). **[human clinical / model organism]**

**NCIT intervention terms:** Coenzyme Q10 Therapy, Riboflavin, Thiamine, L‑Carnitine, Vitamin E, N‑Acetylcysteine, L‑Arginine, Heart Transplantation, Supportive Care.

---

## 13. Prevention

- **Primary prevention:** none (monogenic). **Genetic counseling** (25% recurrence risk per pregnancy for carrier couples), **carrier screening** (especially Finnish founder p.Q286X and consanguineous families), **prenatal diagnosis/PGT‑M** once familial variants known (ACMG/NSGC frameworks, GeneReviews). 
- **Secondary prevention:** early molecular diagnosis enables timely supportive care and surveillance (cardiac, neurologic, hepatic). No population newborn screening.
- **Tertiary prevention:** proactive cardiac monitoring/HF management, avoidance of catabolic stress and mitochondrial‑toxic drugs, prompt treatment of intercurrent illness to prevent decompensation.
- **Immunization/public‑health/environmental measures:** standard childhood vaccination to reduce infection‑triggered crises; no disease‑specific public‑health intervention. **[human clinical / guideline‑based]**

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** TSFM/EF‑Ts is **deeply conserved from bacteria (E. coli _tsf_) through yeast to mammals**; the mitochondrial translation apparatus "resembles that found in prokaryotes" (PMID 17033963), reflecting endosymbiotic bacterial ancestry. Orthologs: **mouse _Tsfm_** (NCBI Gene 219138), rat, zebrafish, _Drosophila_, and bacterial _tsf_.
- **Natural disease (OMIA):** no naturally occurring TSFM‑associated disease documented in companion animals or wildlife in the literature reviewed.
- **Comparative biology / evolutionary conservation:** strong conservation of the EF‑Ts/EF‑Tu nucleotide‑exchange mechanism makes bacterial and yeast systems informative for mechanism (PMID 23727608).
- **Transmission / zoonosis:** not applicable (genetic disease). **[computational / comparative]**

---

## 15. Model Organisms

- **Model types used:** predominantly **in vitro human cellular models** — **patient‑derived skin fibroblasts** and **cardiac/skeletal‑muscle tissue**, with **wild‑type TSFM (or TUFM) cDNA/retroviral complementation** as the gold‑standard functional proof of causation (rescue of translation and OXPHOS assembly) (PMID 17033963, 27677415) **[in vitro]**.
- **Yeast systems** have been used to study suppression of mitochondrial translation‑elongation‑factor defects, exploiting the conserved machinery (PMID 23727608) **[model organism]**.
- **Dedicated animal models:** **no purpose‑built _Tsfm_ knockout/knock‑in mammalian model** was identified in the reviewed literature. A **constitutive _Tsfm_ knockout is predicted to be embryonic‑lethal** (consistent with the absence of surviving human null‑homozygotes), so **conditional/tissue‑specific** models would be required; iPSC‑derived cardiomyocytes/organoids are a logical future platform.
- **Phenotype recapitulation / limitations:** patient‑cell models faithfully reproduce the **molecular defect** (EF‑Ts/EF‑Tu loss, translation defect, combined complex deficiency) and allow rescue experiments, but **do not model organ‑level pathology** (cardiomyopathy, Leigh‑like neurodegeneration); this is the principal gap.
- **Resources:** MGI (mouse _Tsfm_), Cellosaurus/ATCC (patient fibroblast lines), Alliance of Genome Resources. **[in vitro / model organism]**

---

## Summary Answer

**Combined Oxidative Phosphorylation Deficiency Type 3 (COXPD3; MONDO:0012512, OMIM 610505) is a rare autosomal‑recessive mitochondrial disease caused by biallelic mutations in _TSFM_, encoding mitochondrial translation elongation factor EF‑Ts.** Mutant EF‑Ts is destabilized and secondarily depletes its partner EF‑Tu, crippling mitochondrial translation elongation and the synthesis of the 13 mtDNA‑encoded OXPHOS subunits, producing a **combined deficiency of respiratory‑chain complexes I, III, IV and V (complex II spared)**, ATP failure and lactic acidosis. The clinical spectrum is broad and genotype‑/organ‑dependent — **hypertrophic or dilated cardiomyopathy, Leigh‑like encephalopathy, ataxia, optic atrophy, peripheral neuropathy, sensorineural hearing loss, and infantile liver failure** — ranging from fatal neonatal multisystem disease (recurrent p.Arg333Trp allele) to survivable juvenile neurological forms. Diagnosis rests on lactic acidosis, a combined (complex‑II‑sparing) respiratory‑chain enzyme defect on biopsy, Leigh‑pattern MRI, and molecular confirmation of biallelic TSFM variants by WES/panel sequencing; a Finnish founder nonsense allele (p.Gln286X, carrier ~1:80) is notable. **No curative therapy exists** — management is supportive (mitochondrial cofactor/antioxidant "cocktail," heart‑failure care, transplantation) — and prevention relies on genetic counseling and carrier/prenatal testing.

---

### Supported hypotheses / conclusions
1. TSFM/EF‑Ts loss of function is the sole, sufficient cause (rescue‑confirmed). **Supported.**
2. The biochemical lesion is a combined, complex‑II‑sparing OXPHOS deficiency. **Supported.**
3. Phenotype severity tracks residual EF‑Ts function; compensation explains tissue sparing. **Supported.**
4. Autosomal recessive with a Finnish founder allele. **Supported.**

### Refuted / excluded
- Environmental, infectious, immune, epigenetic, or chromosomal primary causation. **Excluded** (no evidence; monogenic point‑mutation disorder).
- mtDNA mutation as cause. **Excluded** (nuclear gene; mtDNA normal).

### Limitations and future directions
- Ultra‑rare: all data from individual case reports/small series; no prevalence, natural‑history cohort, QoL, or RCT data specific to TSFM.
- No dedicated animal model; organ‑level pathogenesis (why heart vs brain vs liver) is unresolved — modifier genes and tissue EF‑Tu buffering are leading hypotheses.
- Therapeutic opportunity: gene replacement is biologically validated in vitro but clinically undeveloped; iPSC‑cardiomyocyte/organoid models and targeted trials are needed.

---

### Key references (PMID)
- 17033963 — Smeitink et al. 2006. Distinct phenotypes from an EF‑Ts (TSFM) mutation; mechanism, rescue. **[landmark]**
- 21741925 — Vedrenne et al. 2012. TSFM R312W → infantile liver failure; same mutation, distinct syndromes.
- 25037205 — Ahola et al. 2014. Juvenile Leigh/neuropathy/optic atrophy; Finnish p.Q286X founder (1:80).
- 27677415 — Emperador et al. 2016. Childhood ataxia + HCM; cDNA rescue; variable phenotypes.
- 31267352 — Scala et al. 2019. p.G183S encephalocardiomyopathy + hearing loss; reversible imaging.
- 30911037 — Perli et al. 2019. Dilated cardiomyopathy, fibro‑adipose replacement, transplant; compensation.
- 35071363 — Yang et al. 2021. HCM + lactic acidosis; compound het R333W/V119L; biopsy.
- 35703069 — Khan et al. 2022. Three mitochondrial elongation factors (TSFM/TUFM/GFM1).
- 33105273 — Barcelos et al. 2020. Mitochondrial medicine therapies, dosing, prevalence ≥1/4300.
- 33640978 — Guha et al. 2021. Combinatorial Glu+NA+NAC synergy in complex‑I models.
- 23727608 — Montanari et al. 2013. Yeast model of mitochondrial translation factor suppression.
- 22283595 — Rahman 2012. Mitochondrial disease and epilepsy (classification context).


## Artifacts

- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Defect_Type_3-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Defect_Type_3-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 11 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 9 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001639` (1 mention) - the report calls it "common (a presenting feature in many)"; HP calls it **Hypertrophic cardiomyopathy**
- `HP:0001644` (1 mention) - the report calls it "subset"; HP calls it **Dilated cardiomyopathy**
- `HP:0003128` (1 mention) - the report calls it "very common"; HP calls it **Lactic acidosis**
- `HP:0002415` (1 mention) - the report calls it "common in neuro forms"; HP calls it **Leukodystrophy**
- `HP:0001251` (1 mention) - the report calls it "subset"; HP calls it **Ataxia**
- `HP:0000648` (1 mention) - the report calls it "subset"; HP calls it **Optic atrophy**
- `HP:0009830` (1 mention) - the report calls it "subset"; HP calls it **Peripheral neuropathy**
- `HP:0000407` (1 mention) - the report calls it "subset"; HP calls it **Sensorineural hearing impairment**
- `HP:0001511` (1 mention) - the report calls it "subset"; HP calls it **Intrauterine growth retardation**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.