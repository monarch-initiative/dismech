---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T15:29:48.254549'
end_time: '2026-10-30T15:46:07.907946'
duration_seconds: 979.65
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Pseudohypoaldosteronism Type 2D
  mondo_id: MONDO:0013781
  category: Mendelian
  causal_genes: KLHL3
  omim_id: OMIM:614495
  synonyms: KLHL3 pseudohypoaldosteronism type 2; PHA2D; pseudohypoaldosteronism type
    2 caused by mutation in KLHL3
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
citation_count: 22
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 22
  on_topic: 17
  off_topic: 1
  off_topic_references:
  - PMID:19448535
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 25
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 1
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0013781
    reported_labels:
    - MONDO
    ontology_label: pseudohypoaldosteronism type 2D
  - term_id: HP:0002153
    reported_labels:
    - Lab abnormality
    ontology_label: Hyperkalemia
  - term_id: HP:0000822
    reported_labels:
    - Clinical sign
    ontology_label: Hypertension
  - term_id: HP:0040331
    reported_labels:
    - abnormal renin
    ontology_label: Focal hypointensity of cerebral white matter on MRI
  - term_id: HP:0002150
    reported_labels:
    - Lab abnormality
    ontology_label: Hypercalciuria
  - term_id: HP:0004322
    reported_labels:
    - Physical
    ontology_label: Short stature
  - term_id: HP:0001324
    reported_labels:
    - Symptom
    ontology_label: Muscle weakness
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
  path: Pseudohypoaldosteronism_Type_2D-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pseudohypoaldosteronism_Type_2D-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pseudohypoaldosteronism Type 2D
- **MONDO ID:** MONDO:0013781 (if available)
- **Causal gene(s):** KLHL3
- **OMIM:** OMIM:614495
- **Synonyms:** KLHL3 pseudohypoaldosteronism type 2; PHA2D; pseudohypoaldosteronism type 2 caused by mutation in KLHL3
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Pseudohypoaldosteronism Type 2D** covering all of the
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

# Pseudohypoaldosteronism Type 2D (PHA2D): A Comprehensive Disease Characteristics Report

**Disease:** Pseudohypoaldosteronism Type 2D (PHA2D)
**Causal gene:** **KLHL3** (Kelch-like family member 3; HGNC:15531; UniProt Q9UH77; locus 5q31.2)
**MONDO:** MONDO:0013781 | **OMIM:** 614495 | **Category:** Mendelian

---

## Summary

Pseudohypoaldosteronism type 2D (PHA2D) is a rare monogenic form of **familial hyperkalemic hypertension (FHHt)**, also known as **Gordon syndrome** or **pseudohypoaldosteronism type II (PHAII)**, caused by germline mutations in **KLHL3**. KLHL3 encodes the kelch-domain substrate adaptor of a Cullin-3 (CUL3)-based E3 ubiquitin ligase whose physiological job in the distal nephron is to bind and ubiquitinate the serine-threonine kinases WNK1 and WNK4, targeting them for proteasomal degradation. When KLHL3 loses the ability to bind its WNK substrates (or to engage CUL3), WNK kinase levels rise. The excess WNK signal activates the SPAK/OSR1 kinases, which phosphorylate and activate the thiazide-sensitive Na-Cl cotransporter (NCC, *SLC12A3*) in the distal convoluted tubule. The net result is a stereotyped clinical triad: **salt-sensitive, low-renin hypertension; hyperkalemia; and hyperchloremic (type-4) metabolic acidosis**, with aldosterone that is inappropriately normal rather than elevated — hence "pseudohypoaldosteronism."

PHA2D is distinctive among the four FHHt genes (WNK1, WNK4, KLHL3, CUL3) in that it can be inherited in **both autosomal dominant and autosomal recessive** fashion. Dominant missense variants cluster in the kelch propeller and BTB domains (the substrate- and cullin-binding surfaces); recessive disease typically arises in consanguineous families. The mechanism has been validated extensively in human genetics, knock-in mouse models that reproduce the full triad, structural/biochemical studies, and cell biology, converging on a single, coherent causal chain. Importantly, because the pathway terminates in NCC gain-of-function, the disease is **fully and specifically reversed by low-dose thiazide diuretics and/or dietary salt restriction**, making PHA2D one of the few forms of hypertension with a precise, mechanism-based cure.

This report consolidates ten confirmed findings across 34 reviewed papers into a complete disease knowledge-base entry covering etiology, phenotypes, molecular genetics, pathophysiology (as an ordered causal chain), affected anatomy, temporal course, epidemiology, diagnostics, prognosis, treatment, prevention, and model systems.

---

## Key Findings

### Finding 1 — KLHL3 mutations cause PHA2D by impairing WNK kinase ubiquitination in the distal nephron

Exome sequencing of PHAII patients from 41 unrelated families identified mutations in **KLHL3 or CUL3** as causes of the disorder, establishing KLHL3 as a bona fide FHHt gene ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/)). A key quote: *"Here we used exome sequencing to identify mutations in kelch-like 3 (KLHL3) or cullin 3 (CUL3) in PHAII patients from 41 unrelated families. KLHL3 mutations are either recessive or dominant, whereas CUL3 mutations are dominant and predominantly de novo."* An independent linkage-plus-exome study identified KLHL3 as a third FHHt gene, reporting 11 additional missense mutations and showing that *"the KLHL3 protein belongs to the BTB-BACK-kelch family of actin-binding proteins that recruit substrates for Cullin3-based ubiquitin ligase complexes. KLHL3 is coexpressed with NCC and downregulates NCC expression at the cell surface"* ([PMID: 22406640](https://pubmed.ncbi.nlm.nih.gov/22406640/)). A mechanistic review confirmed the loss-of-degradation principle: *"In PHAII, the loss of interaction between KLHL3 and WNK4 induces increased levels of WNK kinases due to impaired ubiquitination"* ([PMID: 26152401](https://pubmed.ncbi.nlm.nih.gov/26152401/)). Together these establish KLHL3 as the CUL3 substrate adaptor whose loss-of-function raises WNK abundance.

### Finding 2 — KLHL3-WNK4 binding is physiologically regulated by angiotensin II/PKC phosphorylation at Ser433

The KLHL3-WNK4 interaction is not static but hormonally tuned. KLHL3 is phosphorylated at **serine 433** in the kelch domain by **protein kinase C (PKC)**, which prevents WNK4 binding and degradation; angiotensin II drives this phosphorylation in vivo, raising WNK4 and NCC levels ([PMID: 25313067](https://pubmed.ncbi.nlm.nih.gov/25313067/)): *"We show that KLHL3 is phosphorylated at serine 433 in the Kelch domain (a site frequently mutated in hypertension with hyperkalemia) by protein kinase C in cultured cells and that this phosphorylation prevents WNK4 binding and degradation."* Strikingly, **Ser433 is itself a residue frequently mutated in PHAII** — so a pathogenic mutation at S433 mimics the constitutively phosphorylated (binding-incompetent) state. The opposing phosphatase is calcineurin, which dephosphorylates KLHL3; this explains why **calcineurin inhibitors (tacrolimus, cyclosporine) phenocopy PHAII** hypertension and hyperkalemia via NCC activation ([PMID: 30718414](https://pubmed.ncbi.nlm.nih.gov/30718414/)): *"WNK4 is an activator of NCC and is degraded by binding to KLHL3 followed by WNK4's ubiquitylation and proteasomal degradation."* A molecular dynamics study provided the structural basis: *"phosphorylation of KLHL3 at S433 disrupts the hydrogen bonds, hydrophobic and electrostatic interactions between the Kelch domain of KLHL3 and the AM of WNK4"* ([PMID: 27727489](https://pubmed.ncbi.nlm.nih.gov/27727489/)) — the phospho-group makes the acidic-motif binding pocket more electronegative, abolishing substrate binding.

### Finding 3 — KLHL3(R528H/+) knock-in mice recapitulate the full PHA2D triad

Direct causal proof comes from a knock-in mouse carrying a dominant human KLHL3 mutation. **KLHL3(R528H/+) mice** developed *"salt-sensitive hypertension, hyperkalemia and metabolic acidosis"* — the complete PHAII triad — and *"the phosphorylation of NCC was increased in the KLHL3(R528H/+) mouse kidney"* ([PMID: 24821705](https://pubmed.ncbi.nlm.nih.gov/24821705/)). The upstream lesion was confirmed biochemically: *"the protein expression of both WNK1 and WNK4 was significantly increased in the KLHL3(R528H/+) mouse kidney."* The R528H mutant KLHL3 showed impaired binding to WNK1/WNK4 peptides. This study closes the loop from mutation → impaired WNK binding → WNK accumulation → NCC hyperphosphorylation → clinical triad in a single intact mammalian model.

### Finding 4 — PHA2D is one of four FHHt/Gordon syndrome genes; KLHL3 is unique in showing both dominant and recessive inheritance

Gordon syndrome/FHHt is caused by variants in **four genes — WNK1, WNK4, KLHL3, and CUL3 — all converging on NCC activation** ([PMID: 31795491](https://pubmed.ncbi.nlm.nih.gov/31795491/); [PMID: 23683032](https://pubmed.ncbi.nlm.nih.gov/23683032/)). KLHL3 is the only one of the four that shows **both autosomal dominant and autosomal recessive inheritance** ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/)). In a UK FHHt cohort, *"we have identified novel disease-causing variants in CUL3 and KLHL3 segregating in 63% of the pedigrees with previously unexplained FHHt"*, and importantly *"KLHL3 variants all occur in kelch-repeat domains and so probably disrupt WNK complex binding"* ([PMID: 24266877](https://pubmed.ncbi.nlm.nih.gov/24266877/)). Dominant missense mutations cluster in short segments of the kelch propeller and BTB domains (substrate- and cullin-binding surfaces) and phenocopy recessive loss of function.

### Finding 5 — Thiazide diuretics are the definitive, mechanism-based treatment

Because the entire pathway terminates in NCC gain-of-function, the thiazide class — which directly inhibits NCC — is curative. *"Disease features are reversed by thiazide diuretics, which inhibit the Na-Cl cotransporter in the distal nephron of the kidney; KLHL3 and CUL3 are expressed in this location"* ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/)). FHHt is *"effectively treated by thiazide diuretics and/or dietary salt restriction"* ([PMID: 24266877](https://pubmed.ncbi.nlm.nih.gov/24266877/)). However, thiazides have limitations: *"Thiazide diuretics are currently the main treatment option for Gordon's syndrome. However, they have a number of side effects, and chronic usage can lead to compensatory adaptations in the nephron"* ([PMID: 32724175](https://pubmed.ncbi.nlm.nih.gov/32724175/)), which is motivating development of direct **WNK-SPAK/OSR1 inhibitors**.

### Finding 6 — Clinical/laboratory phenotype: hyperkalemia + hypertension + hyperchloremic metabolic acidosis with suppressed renin and preserved GFR

*"Pseudohypoaldosteronism type 2 (PHA2) is a rare autosomal dominant electrolyte disorder characterized by hypertension, hyperkalemia, metabolic acidosis, and suppressed renin activity, usually with preserved renal function"* ([PMID: 41380172](https://pubmed.ncbi.nlm.nih.gov/41380172/)). Aldosterone is inappropriately normal (not elevated) despite hyperkalemia — the "pseudohypoaldosteronism" paradox. In pediatric patients, *"persistent metabolic acidosis and hypertension may lead to significant growth and developmental impairments"* ([PMID: 41380172](https://pubmed.ncbi.nlm.nih.gov/41380172/)), supporting **short stature/growth impairment** as a downstream consequence. Genetic testing is emphasized as *"indispensable for precise subtyping"* and prognostication ([PMID: 41982973](https://pubmed.ncbi.nlm.nih.gov/41982973/)). **Hypercalciuria** is a recognized feature of pseudohypoaldosteronism ([PMID: 16357816](https://pubmed.ncbi.nlm.nih.gov/16357816/)).

### Finding 7 — Variant spectrum and urinary NCC biomarker

Specific KLHL3 variants include the **dominant Q309R** and the **recessive S553L**. A consanguineous Jewish family of Yemenite extraction carrying S553L included *"2 homozygous and 7 heterozygous affected subjects"* ([PMID: 28511177](https://pubmed.ncbi.nlm.nih.gov/28511177/)). Increased **urinary exosomal NCC** was detected in affected members with the dominant Q309R variant and in homozygotes (and some heterozygotes) in the recessive family — providing a functional biomarker that directly reflects the pathway's NCC gain-of-function. KLHL3 disease is "mostly dominant" with a few recessive cases, and consanguinity underlies the recessive form. Pathogenic KLHL3 variants are predominantly missense in kelch-repeat/BTB domains ([PMID: 24266877](https://pubmed.ncbi.nlm.nih.gov/24266877/)).

### Finding 8 — The WNK-OSR1/SPAK-NCC cascade is necessary and sufficient for the phenotype downstream of KLHL3/WNK dysregulation

Genetic epistasis experiments pinpoint the effector pathway. In Wnk4(D561A/+) PHAII mice, **deleting SPAK abolished the phenotype**: *"Wnk4 (D561A/+).Spak (-/-) mice became normotensive and lacked the PHA II phenotype"* ([PMID: 24039833](https://pubmed.ncbi.nlm.nih.gov/24039833/)), whereas kidney-specific Osr1 knockout did not rescue — identifying **SPAK as the principal effector kinase**. Triple knock-in mice preventing SPAK/OSR1 activation almost completely abolished NCC phosphorylation and corrected the triad: *"the high blood pressure, hyperkalemia and metabolic acidosis observed in Wnk4(D561A/+) mice were corrected in the triple knock-in mice. These results clearly establish that PHAII caused by the WNK4 D561A mutation is dependent on the activation of the WNK-OSR1/SPAK-NCC cascade"* ([PMID: 21486947](https://pubmed.ncbi.nlm.nih.gov/21486947/)). The cascade is physiologically regulated by dietary salt and aldosterone ([PMID: 18800028](https://pubmed.ncbi.nlm.nih.gov/18800028/)). KLHL3 acts upstream by controlling WNK abundance, feeding into this same shared effector pathway.

### Finding 9 — Hyperkalemia and acidosis arise from WNK-mediated suppression of distal K⁺/H⁺ secretion plus reduced Na⁺ delivery

The hyperkalemia/acidosis branch is mechanistically separable from the hypertension branch. WNK4 (stabilized when KLHL3 is mutated) *"is a serine-threonine kinase expressed in the distal nephron that inhibits ROMK activity and renal K(+) secretion"* ([PMID: 23885063](https://pubmed.ncbi.nlm.nih.gov/23885063/)) and also inhibits the large-conductance **BK/Maxi-K channel** by promoting its ubiquitin-/lysosome-dependent degradation ([PMID: 21613417](https://pubmed.ncbi.nlm.nih.gov/21613417/)). A review confirms: *"WNK4 also regulates the expression or function of renal outer medullary potassium (ROMK) channels, ENaCs, and Cl transporters. WNK1 also regulates NCC and ROMK. Aldosterone inactivates WNK1 and WNK4 activity"* ([PMID: 20829405](https://pubmed.ncbi.nlm.nih.gov/20829405/)). Mouse models implicate ROMK and maxi-K dysregulation in producing hyperkalemia ([PMID: 19448535](https://pubmed.ncbi.nlm.nih.gov/19448535/)). In parallel, enhanced upstream NCC activity **reduces Na⁺ delivery to the aldosterone-sensitive distal nephron**, diminishing the electrochemical driving force for both K⁺ and H⁺ secretion.

### Finding 10 — Synthesis: a thiazide-reversible distal-nephron channelopathy of impaired WNK-kinase ubiquitination

Integrating human genetics, mouse models, cell biology, and clinical reports: **KLHL3** (HGNC:15531, UniProt Q9UH77, 5q31.2) is the CUL3-ligase adaptor whose loss-of-function (dominant or recessive) raises WNK1/WNK4, activating SPAK/OSR1→NCC (driving hypertension) while suppressing ROMK/BK and reducing distal Na⁺ delivery (driving hyperkalemia and type-4 acidosis). Renin is suppressed and aldosterone inappropriately normal. The anchoring evidence: *"Disease features are reversed by thiazide diuretics... KLHL3 and CUL3 are expressed in this location"* ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/)) and *"KLHL3 is coexpressed with NCC and downregulates NCC expression at the cell surface"* ([PMID: 22406640](https://pubmed.ncbi.nlm.nih.gov/22406640/)).

---

## Section-by-Section Report

### 1. Disease Information

PHA2D is a rare, Mendelian, salt-retaining tubulopathy — a subtype of **familial hyperkalemic hypertension (FHHt) / Gordon syndrome / pseudohypoaldosteronism type II (PHAII)** — specifically caused by mutations in **KLHL3**. It is defined by renal tubular **gain** of NaCl reabsorption with impaired K⁺ and H⁺ excretion, producing hypertension, hyperkalemia, and metabolic acidosis in the face of normal glomerular filtration.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM | 614495 |
| MONDO | MONDO:0013781 |
| Gene (HGNC) | KLHL3, HGNC:15531 |
| UniProt | Q9UH77 |
| Locus | 5q31.2 |
| ICD-10 | E26.8 (other mineralocorticoid disorders) — nearest mapping |
| MeSH | Pseudohypoaldosteronism (D011546) |
| Orphanet | ORPHA:757 (Gordon hyperkalemia-hypertension syndrome) |

**Synonyms:** PHA2D; KLHL3 pseudohypoaldosteronism type 2; pseudohypoaldosteronism type 2 caused by mutation in KLHL3; a molecular subtype of Gordon syndrome / Familial Hyperkalemic Hypertension (FHHt) / PHAII. Information is derived from **aggregated disease-level resources** (OMIM, gene-discovery cohorts) and **individual patient/family reports**, not from EHR-scale datasets.

### 2. Etiology

**Causal factors:** Purely **genetic** — germline missense mutations in **KLHL3**. No infectious or environmental cause initiates the disease. Dominant mutations cluster in the kelch-repeat propeller (substrate-binding) and BTB (CUL3-binding) domains; recessive mutations cause loss of function, typically in consanguineous families ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/); [PMID: 24266877](https://pubmed.ncbi.nlm.nih.gov/24266877/)).

**Genetic risk factors:** The KLHL3 mutation is the sole driver; there are no documented susceptibility loci beyond the four FHHt genes (WNK1, WNK4, KLHL3, CUL3). **Modifier:** background NCC/SLC12A3 genotype could in principle modulate severity (NCC phosphorylation state governs the phenotype), though this is inferred, not demonstrated for KLHL3 specifically.

**Environmental/lifestyle modifiers:** **Dietary salt** is the key modifiable factor — the phenotype is salt-sensitive, worsened by high Na⁺ intake and improved by salt restriction ([PMID: 18800028](https://pubmed.ncbi.nlm.nih.gov/18800028/)). **Angiotensin II** and **calcineurin-inhibitor drugs (tacrolimus/cyclosporine)** phenocopy/aggravate the mechanism by shifting KLHL3 phosphorylation toward the WNK4-binding-incompetent state ([PMID: 25313067](https://pubmed.ncbi.nlm.nih.gov/25313067/); [PMID: 30718414](https://pubmed.ncbi.nlm.nih.gov/30718414/)).

**Protective factors:** A **low-sodium diet** is protective (reduces NCC-mediated salt retention). Loss-of-function in the downstream SPAK kinase would be protective (abolishes the phenotype in mice) — the pharmacological rationale for SPAK/OSR1 inhibitors.

**Gene–environment interaction:** A clear GxE axis exists — the genetic lesion (KLHL3 loss-of-function) raises the setpoint of the WNK-SPAK-NCC cascade, but **dietary salt and aldosterone/AngII tone determine the degree of expression**. Calcineurin inhibitors convert a drug exposure into a biochemical phenocopy, demonstrating convergence of pharmacologic and genetic inputs on the same node.

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset / severity / frequency |
|---|---|---|---|
| Hyperkalemia | Lab abnormality | HP:0002153 | Often earliest/most constant sign; frequently neonatal–childhood; near-universal |
| Hypertension | Clinical sign | HP:0000822 | Variable; may be later-onset than hyperkalemia; common but can be mild/absent in young recessive cases |
| Hyperchloremic metabolic acidosis (type-4 RTA) | Lab abnormality | HP:0004910 / HP:0001942 | Common; contributes to growth impairment |
| Suppressed plasma renin | Lab abnormality | HP:0040331 (abnormal renin) | Characteristic |
| Inappropriately normal aldosterone | Lab abnormality | — | Characteristic ("pseudo" feature) |
| Hypercalciuria | Lab abnormality | HP:0002150 | Recognized feature ([PMID: 16357816](https://pubmed.ncbi.nlm.nih.gov/16357816/)) |
| Short stature / growth impairment | Physical | HP:0004322 | In pediatric cases with persistent acidosis ([PMID: 41380172](https://pubmed.ncbi.nlm.nih.gov/41380172/)) |
| Muscle weakness (hyperkalemia-related) | Symptom | HP:0001324 | Variable/episodic |

**Characteristics:** Age of onset ranges from **neonatal/childhood (hyperkalemia often first)** to **adult (hypertension)**; severity is **variable** and genotype-dependent; course is **chronic and stable/lifelong** rather than episodic; renal function is preserved. **Quality-of-life impact** is driven chiefly by hyperkalemia risk (arrhythmia, muscle weakness), hypertension-related cardiovascular risk, and, in children, growth/developmental impairment — all largely correctable with treatment.

### 4. Genetic / Molecular Information

**Causal gene:** KLHL3 (HGNC:15531; UniProt Q9UH77; chromosome 5q31.2). Protein: a **BTB-BACK-kelch substrate adaptor** that recruits WNK1/WNK4 for a CUL3-based E3 ubiquitin ligase.

**Variant classes:** Predominantly **missense** variants in the **kelch-repeat propeller** (substrate binding) and **BTB** (CUL3 binding) domains. Representative variants: **R528H** (dominant; validated in knock-in mice, [PMID: 24821705](https://pubmed.ncbi.nlm.nih.gov/24821705/)), **Q309R** (dominant, [PMID: 28511177](https://pubmed.ncbi.nlm.nih.gov/28511177/)), **S553L** (recessive, [PMID: 28511177](https://pubmed.ncbi.nlm.nih.gov/28511177/)), and the regulatory hotspot **S433** (dominant; phosphomimetic effect, [PMID: 25313067](https://pubmed.ncbi.nlm.nih.gov/25313067/)). **Classification:** pathogenic/likely pathogenic per segregation and functional data. **Allele frequency:** extremely rare in gnomAD (private/family-specific). **Origin:** germline. **Functional consequence:** **loss of function** of KLHL3's WNK-degradation activity — dominant variants act by **dominant-negative/haploinsufficiency** on substrate or cullin binding; recessive variants require biallelic loss.

**Modifier genes:** The downstream SPAK (STK39), OSR1 (OXSR1), NCC (SLC12A3), WNK1, and WNK4 set phenotype magnitude. **Epigenetic/chromosomal abnormalities:** none described — PHA2D is a single-gene point-mutation disorder, not a copy-number/structural disease.

### 5. Environmental Information

PHA2D is genetically determined; the only clinically important non-genetic contributors are **dietary sodium** (aggravates), **angiotensin II tone**, and **calcineurin-inhibitor drugs** (tacrolimus/cyclosporine), which phenocopy the biochemical lesion by dephosphorylation-blockade of KLHL3 ([PMID: 30718414](https://pubmed.ncbi.nlm.nih.gov/30718414/)). There are **no infectious agents** involved.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A germline **KLHL3 missense mutation** (dominant in kelch/BTB domains, or biallelic recessive) **leads to** loss of KLHL3's ability to bind WNK1/WNK4 (or to engage CUL3). *(Demonstrated: impaired peptide binding, [PMID: 24821705](https://pubmed.ncbi.nlm.nih.gov/24821705/).)*
2. Impaired substrate binding **results in** failure of CUL3-KLHL3-mediated ubiquitination of WNK1/WNK4. *(Demonstrated, [PMID: 26152401](https://pubmed.ncbi.nlm.nih.gov/26152401/).)*
3. Failed ubiquitination **leads to** accumulation of WNK1 and WNK4 protein in the distal convoluted tubule. *(Demonstrated in vivo: both WNK1 and WNK4 increased in KLHL3(R528H/+) kidney, [PMID: 24821705](https://pubmed.ncbi.nlm.nih.gov/24821705/).)*
4. Elevated WNK kinases **activate** the STE20-family kinases **SPAK (and OSR1)**. *(Demonstrated; SPAK is the principal effector, [PMID: 24039833](https://pubmed.ncbi.nlm.nih.gov/24039833/).)*
5. Activated SPAK/OSR1 **phosphorylate and activate** the **Na-Cl cotransporter NCC** at the apical membrane. *(Demonstrated: increased p-NCC, [PMID: 24821705](https://pubmed.ncbi.nlm.nih.gov/24821705/); [PMID: 21486947](https://pubmed.ncbi.nlm.nih.gov/21486947/).)*

   **Branch A (hypertension):** Enhanced NCC-mediated NaCl reabsorption **leads to** plasma volume expansion → **salt-sensitive, low-renin hypertension**.

   **Branch B (hyperkalemia + acidosis):** Two parallel sub-mechanisms:
   - 6a. Elevated WNK4 **directly inhibits ROMK** and **promotes degradation of BK/Maxi-K** channels, **reducing** distal K⁺ secretion → **hyperkalemia** ([PMID: 23885063](https://pubmed.ncbi.nlm.nih.gov/23885063/); [PMID: 21613417](https://pubmed.ncbi.nlm.nih.gov/21613417/)).
   - 6b. Increased upstream NCC activity **reduces Na⁺ delivery** to the aldosterone-sensitive distal nephron, **diminishing** the electrochemical driving force (ENaC-dependent lumen-negativity) for K⁺ and H⁺ secretion → **hyperkalemia and hyperchloremic (type-4) metabolic acidosis** ([PMID: 19448535](https://pubmed.ncbi.nlm.nih.gov/19448535/); [PMID: 20829405](https://pubmed.ncbi.nlm.nih.gov/20829405/)).
7. Volume expansion **suppresses renin**; hyperkalemia should raise aldosterone, but aldosterone is **inappropriately normal** — the "pseudohypoaldosteronism" paradox.

```
KLHL3 mutation
      │ (loss of WNK binding / ubiquitination)
      ▼
 ↑ WNK1 / WNK4  ───►  ↑ SPAK/OSR1  ───►  ↑ p-NCC (active)
      │                                        │
      │                          ┌─────────────┴─────────────┐
      │                          ▼                           ▼
      │                  ↑ NaCl reabsorption        ↓ Na+ delivery to ASDN
      │                          │                           │
      │                          ▼                           ▼
      │                  volume expansion            ↓ K+/H+ secretion
      │                          │                           │
      ▼                          ▼                           ▼
 ↓ ROMK, ↓ BK  ──────►   LOW-RENIN HYPERTENSION    HYPERKALEMIA + ACIDOSIS
   (↓ K+ secretion)
```

**Regulatory overlay:** KLHL3-WNK4 binding is normally switched off by AngII/PKC phosphorylation at Ser433 and switched on by calcineurin dephosphorylation — so AngII and calcineurin inhibitors push the system toward the PHA2D state even without a mutation ([PMID: 25313067](https://pubmed.ncbi.nlm.nih.gov/25313067/); [PMID: 30718414](https://pubmed.ncbi.nlm.nih.gov/30718414/); [PMID: 27727489](https://pubmed.ncbi.nlm.nih.gov/27727489/)).

**Pathway/ontology annotations:** Molecular pathway — CUL3-KLHL3 E3 ubiquitin ligase / WNK-SPAK/OSR1-NCC signaling. **GO terms:** protein polyubiquitination (GO:0000209), protein K48-linked ubiquitination (GO:0070936), Cul3-RING ubiquitin ligase complex (GO:0031463), sodium ion transmembrane transport (GO:0035725), potassium ion transmembrane transport (GO:0071805), regulation of blood pressure (GO:0008217). **Protein dysfunction:** loss of adaptor function (substrate/cullin binding). **Biochemical abnormality:** ion-transporter dysregulation (NCC gain; ROMK/BK loss). No autoimmunity, metabolic-enzyme deficiency, or inflammatory component. **CHEBI entities:** potassium(1+) (CHEBI:29103), chloride (CHEBI:17996), sodium(1+) (CHEBI:29101), aldosterone (CHEBI:27584).

### 7. Anatomical Structures Affected

- **Organ:** **Kidney** (UBERON:0002113), specifically the **distal convoluted tubule** (UBERON:0001292) and the **aldosterone-sensitive distal nephron / connecting tubule–cortical collecting duct**.
- **Body system:** **Renal/urinary** and **endocrine (mineralocorticoid axis)**; secondary **cardiovascular** involvement (hypertension) and growth/skeletal effects in children.
- **Cell type:** **Distal convoluted tubule epithelial cell** (CL:1000849 / kidney DCT cell), where KLHL3 is coexpressed with NCC ([PMID: 22406640](https://pubmed.ncbi.nlm.nih.gov/22406640/)); and **principal cells** of the collecting duct (site of ROMK/ENaC-dependent K⁺/H⁺ handling).
- **Tissue:** renal tubular **epithelium**.
- **Subcellular (GO Cellular Component):** apical plasma membrane (GO:0016324) — NCC, ROMK, BK localization; cytoplasm — WNK/SPAK signaling; Cul3-RING ligase complex (GO:0031463).
- **Lateralization:** bilateral (systemic genetic disorder affecting both kidneys).

### 8. Temporal Development

**Onset:** Variable and biphasic — **hyperkalemia often appears first in childhood (sometimes neonatally)**, while **hypertension frequently develops later (adolescence/adulthood)**. Onset is **insidious/chronic**, not acute. A 9-year follow-up of early-onset PHA2 documents childhood presentation ([PMID: 41380172](https://pubmed.ncbi.nlm.nih.gov/41380172/)).

**Progression:** Slow, **stable, chronic and lifelong**; not relapsing-remitting or episodic. Renal function is typically preserved. Untreated persistent acidosis/hypertension in childhood can impair growth. **Remission** is **treatment-induced** (thiazide/salt restriction), not spontaneous. **Critical period:** early recognition in childhood is the key window to prevent growth impairment and long-term cardiovascular damage.

### 9. Inheritance and Population

**Epidemiology:** PHA2/Gordon syndrome is **rare** (Orphanet ORPHA:757); precise prevalence/incidence figures for the KLHL3 (PHA2D) subtype are **not established** — reported as scattered families and small case series. Among FHHt cohorts, KLHL3/CUL3 variants explained ~63% of previously unexplained pedigrees ([PMID: 24266877](https://pubmed.ncbi.nlm.nih.gov/24266877/)).

**Inheritance:** **Both autosomal dominant and autosomal recessive** — unique to KLHL3 among FHHt genes ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/)). Dominant disease is "mostly" the rule; recessive disease arises with **consanguinity** (e.g., S553L in a consanguineous Yemenite Jewish family with 2 homozygous + 7 heterozygous affected, [PMID: 28511177](https://pubmed.ncbi.nlm.nih.gov/28511177/)). **Penetrance:** high but with **variable expressivity** (age-dependent for hypertension). **Founder effects:** plausible in consanguineous recessive kindreds. **Genetic anticipation / mitochondrial inheritance / germline mosaicism:** not features of this disorder. **Sex ratio:** no strong predilection reported. **Carrier frequency:** very low (private variants).

### 10. Diagnostics

**Laboratory (core):** serum **K⁺ (↑)**, serum **HCO₃⁻ (↓)/Cl⁻ (↑)** indicating hyperchloremic metabolic acidosis, **plasma renin (↓/suppressed)**, **aldosterone (inappropriately normal)**, normal creatinine/eGFR; blood-pressure monitoring. **LOINC-type analytes:** potassium serum (2823-3), bicarbonate (1963-8), renin, aldosterone. **Biomarker:** increased **urinary exosomal NCC** reflects pathway activation and can distinguish affected members ([PMID: 28511177](https://pubmed.ncbi.nlm.nih.gov/28511177/)).

**Genetic testing (confirmatory and essential):** *"genetic testing is indispensable for precise subtyping"* ([PMID: 41982973](https://pubmed.ncbi.nlm.nih.gov/41982973/)). Approach: **targeted single-gene or FHHt/Gordon gene-panel sequencing (WNK1, WNK4, KLHL3, CUL3)**, or **whole-exome sequencing** for undiagnosed familial hyperkalemic hypertension (the original discovery method, [PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/)). CMA/karyotype/FISH/mtDNA/repeat-expansion testing are **not applicable** (point-mutation disorder).

**Clinical criteria / differential diagnosis:** Diagnose by the triad of hyperkalemia + (hyper)tension + hyperchloremic metabolic acidosis with suppressed renin, normal GFR, and inappropriately normal aldosterone. **Differentials:** PHA type I / adrenal insufficiency (salt-wasting, low BP — opposite), chronic kidney disease (abnormal GFR), Addison disease, drug-induced hyperkalemia (ACEi/ARB/K-sparing diuretics, calcineurin inhibitors), and the other FHHt genes (WNK1/WNK4/CUL3) — distinguished by genetic testing. **Screening:** cascade genetic/biochemical screening of first-degree relatives in known families.

### 11. Outcome / Prognosis

Prognosis is **excellent with treatment**. There is **no inherent reduction in life expectancy** when hyperkalemia and hypertension are controlled; renal function is generally preserved. **Morbidity** without treatment stems from hyperkalemia (arrhythmia, muscle weakness), hypertension-related cardiovascular/end-organ risk, and — in children — **growth and developmental impairment** from persistent acidosis ([PMID: 41380172](https://pubmed.ncbi.nlm.nih.gov/41380172/)). **Recovery potential** is high: biochemical and blood-pressure abnormalities are **fully reversible** on thiazide/salt restriction ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/)). **Prognostic factors:** genotype (dominant vs recessive; specific variant), age at diagnosis, and treatment adherence.

### 12. Treatment

**First-line / definitive — Thiazide diuretics** (e.g., hydrochlorothiazide, chlorthalidone) directly inhibit NCC, the pathway endpoint, **reversing all three disease features** ([PMID: 22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/); [PMID: 24266877](https://pubmed.ncbi.nlm.nih.gov/24266877/)). *NCIT:* Thiazide Diuretic (C29723); Hydrochlorothiazide (C29281). **Adjunct — dietary sodium restriction** (mechanistically synergistic). Thiazides correct hyperkalemia (by restoring distal Na⁺ delivery/flow-dependent K⁺ secretion), acidosis, and hypertension simultaneously.

**Limitations and emerging therapy:** Chronic thiazide use has side effects and provokes compensatory nephron adaptation ([PMID: 32724175](https://pubmed.ncbi.nlm.nih.gov/32724175/)); **direct WNK-SPAK/OSR1 inhibitors** are in development as mechanism-targeted alternatives. **Avoid** agents that aggravate the mechanism: ACE inhibitors/ARBs are not first-line (renin already suppressed), and **calcineurin inhibitors** phenocopy the lesion ([PMID: 30718414](https://pubmed.ncbi.nlm.nih.gov/30718414/)). **Supportive:** monitor potassium and blood pressure; treat pediatric acidosis to protect growth. Gene/cell/RNA therapies are **not applicable/available** for this condition.

### 13. Prevention

PHA2D cannot be prevented at the genetic level, but complications are highly preventable. **Primary prevention** does not apply (monogenic). **Secondary prevention:** cascade biochemical + genetic **screening of relatives** in known kindreds enables pre-symptomatic diagnosis and early thiazide/salt-restriction intervention. **Tertiary prevention:** ongoing control of K⁺ and blood pressure to prevent arrhythmia, cardiovascular damage, and (in children) growth failure. **Genetic counseling** should address the dual AD/AR inheritance — autosomal dominant transmission (50% offspring risk) in most families, and recessive risk with consanguinity ([PMID: 28511177](https://pubmed.ncbi.nlm.nih.gov/28511177/)). Prenatal/preimplantation testing is technically feasible once the familial variant is known. No immunization or public-health/environmental intervention applies.

### 14. Other Species / Natural Disease

**Orthologs:** KLHL3 is conserved in mouse (*Klhl3*), rat, and other vertebrates; the entire CUL3-KLHL3-WNK-SPAK-NCC axis is evolutionarily conserved, which is why mouse models faithfully reproduce the human disease ([PMID: 24821705](https://pubmed.ncbi.nlm.nih.gov/24821705/)). **NCBI Taxon:** human (9606), mouse (10090). **Natural disease in companion animals/wildlife:** no naturally occurring KLHL3 PHA2D is documented in OMIA. **Zoonotic potential:** none (non-transmissible genetic disorder).

### 15. Model Organisms

| Model | Type | Phenotype recapitulation | Reference |
|---|---|---|---|
| **KLHL3(R528H/+) knock-in mouse** | Mammalian, dominant knock-in | **Full triad** — salt-sensitive hypertension, hyperkalemia, metabolic acidosis; ↑WNK1/WNK4; ↑p-NCC | [PMID: 24821705](https://pubmed.ncbi.nlm.nih.gov/24821705/) |
| Wnk4(D561A/+) knock-in mouse | Mammalian (WNK4 FHHt model, shared effector pathway) | Full PHAII triad; salt/aldosterone-regulated cascade | [PMID: 21486947](https://pubmed.ncbi.nlm.nih.gov/21486947/); [PMID: 18800028](https://pubmed.ncbi.nlm.nih.gov/18800028/) |
| Wnk4(D561A/+);Spak⁻/⁻ | Genetic epistasis cross | Normotensive, phenotype abolished — proves SPAK is effector | [PMID: 24039833](https://pubmed.ncbi.nlm.nih.gov/24039833/) |
| SPAK/OSR1 triple knock-in | Mammalian | Corrects BP, hyperkalemia, acidosis | [PMID: 21486947](https://pubmed.ncbi.nlm.nih.gov/21486947/) |
| Xenopus oocytes / HEK293 cells | In vitro | Quantify NCC surface expression, WNK ubiquitination, KLHL3 binding | [PMID: 22406640](https://pubmed.ncbi.nlm.nih.gov/22406640/) |

The **KLHL3(R528H/+) knock-in mouse is the direct, high-fidelity model of PHA2D**, recapitulating both the biochemistry (WNK accumulation, NCC hyperphosphorylation) and the clinical triad. **Limitation:** mouse models emphasize the hypertension/NCC branch; the human severity balance of hyperkalemia vs hypertension is genotype-variable and incompletely captured. Resources: MGI, IMPC, IMSR.

---

## Mechanistic Model / Interpretation

PHA2D is best understood as a **"loss of a brake on salt reabsorption."** Normally, the CUL3-KLHL3 E3 ligase continuously degrades WNK1/WNK4 kinases, keeping the WNK-SPAK/OSR1-NCC salt-reabsorption cascade restrained and tunable by salt, aldosterone, and angiotensin II. A KLHL3 mutation removes this brake: WNK kinases accumulate, the cascade runs hot, and NCC over-reabsorbs NaCl. The disease then splits into **two mechanistically distinct but linked branches** from the single node of excess WNK/NCC activity: a **volume/pressure branch** (hypertension, renin suppression) and a **potassium/acid branch** (hyperkalemia, type-4 acidosis), the latter arising both from direct WNK4 inhibition of ROMK/BK channels and from reduced distal Na⁺ delivery that starves the K⁺/H⁺ secretory driving force. The elegance — and therapeutic key — is that **everything funnels through NCC**, so a thiazide (or salt restriction) that blocks NCC corrects the entire syndrome at once. The S433/PKC/calcineurin regulatory layer unifies the Mendelian disease with acquired phenocopies (calcineurin-inhibitor toxicity, AngII-driven salt-sensitive hypertension), giving PHA2D outsized importance as a model for common essential hypertension.

## Evidence Base

| PMID | Contribution | Supports |
|---|---|---|
| [22266938](https://pubmed.ncbi.nlm.nih.gov/22266938/) | KLHL3/CUL3 gene discovery; dual AD/AR; thiazide reversibility | F001, F004, F005, F010 |
| [22406640](https://pubmed.ncbi.nlm.nih.gov/22406640/) | KLHL3 as CUL3 adaptor; coexpressed with NCC; downregulates NCC | F001, F010 |
| [26152401](https://pubmed.ncbi.nlm.nih.gov/26152401/) | Loss of KLHL3-WNK4 interaction raises WNK | F001 |
| [25313067](https://pubmed.ncbi.nlm.nih.gov/25313067/) | S433 PKC phosphorylation blocks WNK4 binding | F002 |
| [30718414](https://pubmed.ncbi.nlm.nih.gov/30718414/) | Calcineurin dephosphorylates KLHL3; CNI phenocopy | F002 |
| [27727489](https://pubmed.ncbi.nlm.nih.gov/27727489/) | Structural basis of S433 disruption | F002 |
| [24821705](https://pubmed.ncbi.nlm.nih.gov/24821705/) | KLHL3(R528H/+) mouse; full triad; ↑WNK1/4; ↑p-NCC | F003 |
| [24266877](https://pubmed.ncbi.nlm.nih.gov/24266877/) | 63% FHHt yield; kelch-repeat variants; thiazide/salt treatment | F004, F005, F007 |
| [31795491](https://pubmed.ncbi.nlm.nih.gov/31795491/) / [23683032](https://pubmed.ncbi.nlm.nih.gov/23683032/) | Four-gene FHHt framework; SPAK intermediary | F004, F008 |
| [32724175](https://pubmed.ncbi.nlm.nih.gov/32724175/) | Thiazide limitations; WNK-SPAK/OSR1 inhibitors | F005 |
| [41380172](https://pubmed.ncbi.nlm.nih.gov/41380172/) | Clinical phenotype; growth impairment; 9-yr follow-up | F006 |
| [41982973](https://pubmed.ncbi.nlm.nih.gov/41982973/) | Genetic testing indispensable for subtyping | F006 |
| [28511177](https://pubmed.ncbi.nlm.nih.gov/28511177/) | Q309R (dom) vs S553L (rec); urinary NCC biomarker | F007 |
| [24039833](https://pubmed.ncbi.nlm.nih.gov/24039833/) | SPAK deletion abolishes PHAII | F008 |
| [21486947](https://pubmed.ncbi.nlm.nih.gov/21486947/) | Triple KI proves cascade dependence | F008 |
| [23885063](https://pubmed.ncbi.nlm.nih.gov/23885063/) / [21613417](https://pubmed.ncbi.nlm.nih.gov/21613417/) | WNK4 inhibits ROMK and BK | F009 |
| [20829405](https://pubmed.ncbi.nlm.nih.gov/20829405/) / [19448535](https://pubmed.ncbi.nlm.nih.gov/19448535/) | WNK regulation of distal channels; Na delivery/flow | F009 |
| [18800028](https://pubmed.ncbi.nlm.nih.gov/18800028/) | Salt/aldosterone regulate the cascade | F008 |

## Limitations and Knowledge Gaps

1. **Epidemiology is unquantified.** No reliable prevalence/incidence figures exist for the KLHL3 subtype specifically; the disease is reported as families and small case series.
2. **Genotype–phenotype correlation is incomplete.** Why some patients present chiefly with hyperkalemia and others with hypertension, and how dominant vs recessive variants and specific residues (Q309R, R528H, S553L, S433) tune severity, is not fully mapped.
3. **Mouse models over-represent the NCC/hypertension branch** and may under-represent the human hyperkalemia phenotype.
4. **No large natural-history or quality-of-life cohort** exists for PHA2D; growth-impairment data come from limited pediatric reports.
5. **Human functional data for many KLHL3 variants** remain at the in-vitro/computational level; several variants are inferred pathogenic by analogy and segregation rather than individually functionally proven.

## Proposed Follow-up Experiments / Actions

1. **Assemble an international PHA2D registry** linking KLHL3 genotype (dominant/recessive, residue) to quantitative phenotype (K⁺, BP, HCO₃⁻, height-SDS) to establish penetrance, expressivity, and genotype–phenotype rules.
2. **Deep-mutational scanning of KLHL3** (kelch + BTB domains) with a WNK4-binding/ubiquitination readout to prospectively classify VUS and refine ACMG calls.
3. **Validate urinary exosomal NCC** as a routine functional biomarker for diagnosis, carrier detection, and treatment monitoring across both dominant and recessive families.
4. **Clinical evaluation of WNK-SPAK/OSR1 inhibitors** in FHHt/PHA2D as thiazide-sparing, mechanism-targeted therapy, with endpoints for hyperkalemia correction and nephron adaptation.
5. **Generate recessive-allele knock-in mice (e.g., S553L homozygous)** to test whether recessive loss-of-function produces a distinct (more hyperkalemia-weighted) phenotype than dominant R528H.
6. **Prospective pediatric study** of acidosis correction and catch-up growth to define the critical treatment window for preventing developmental impairment.

---

*Report compiled from 10 confirmed findings across 34 reviewed papers (5 investigation iterations). Evidence spans human genetics, knock-in mouse models, structural/molecular dynamics, in vitro cell biology, and clinical case series.*


## Artifacts

- [OpenScientist final report](Pseudohypoaldosteronism_Type_2D-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pseudohypoaldosteronism_Type_2D-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 22 |
| On topic | 17 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:19448535` (6 mentions) - Distal potassium handling based on flow modulation of maxi-K channel activity.
  - shared terms: hyperkalemia

Weighed against this report's own most characteristic terms: `klhl3`, `ncc`, `hyperkalemia`, `hypertension`, `dominant`, `wnk4`, `acidosis`, `pha2d`, `recessive`, `genetic`, `disease`, `wnk1`, `fhht`, `cul3`, `aldosterone`, `gene`, `osr1`, `mutation`, `phenotype`, `wnk`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 9 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013781` (2 mentions) - the report calls it "MONDO"; MONDO calls it **pseudohypoaldosteronism type 2D**
- `HP:0002153` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hyperkalemia**
- `HP:0000822` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hypertension**
- `HP:0040331` (1 mention) - the report calls it "abnormal renin"; HP calls it **Focal hypointensity of cerebral white matter on MRI**
- `HP:0002150` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hypercalciuria**
- `HP:0004322` (1 mention) - the report calls it "Physical"; HP calls it **Short stature**
- `HP:0001324` (1 mention) - the report calls it "Symptom"; HP calls it **Muscle weakness**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002113` (1 mention) - the report calls it "Kidney", "Organ:** **Kidney"; UBERON calls it **kidney**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002113` - called "Kidney", "Organ:** **Kidney"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.