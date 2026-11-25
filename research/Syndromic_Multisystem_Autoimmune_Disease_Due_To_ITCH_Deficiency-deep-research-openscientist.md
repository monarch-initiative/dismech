---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-13T08:50:34.513908'
end_time: '2026-11-13T09:23:04.559620'
duration_seconds: 1950.05
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Syndromic Multisystem Autoimmune Disease Due to ITCH Deficiency
  mondo_id: MONDO:0013245
  category: Mendelian
  causal_genes: ITCH
  omim_id: OMIM:613385
  synonyms: not recorded
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    save_artifacts: true
    artifact_max_bytes: 5242880
    artifact_keep_runtime: false
    artifact_extra_extensions: []
    artifact_include_globs: []
    artifact_exclude_globs: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
run_metadata:
  job_id: 2db8bac8-5a91-4714-af77-cadec50b1e66
citation_count: 13
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 16
  on_topic: 11
  validator_version: 0.5.1
term_validation:
  total_terms: 38
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 6
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0013245
    reported_labels:
    - MONDO
    ontology_label: syndromic multisystem autoimmune disease due to ITCH deficiency
  - term_id: HP:0001508
    reported_labels:
    - Common (core feature)
    ontology_label: Failure to thrive
  - term_id: HP:0006530
    reported_labels:
    - Severe cases (tracheostomy, ventilation)
    ontology_label: Abnormal pulmonary interstitial morphology
  - term_id: HP:0004386
    reported_labels:
    - Frequent
    ontology_label: Gastrointestinal inflammation
  - term_id: HP:0030149
    reported_labels:
    - parotitis
    ontology_label: Cardiogenic shock
  labels_variant: 7
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Syndromic_Multisystem_Autoimmune_Disease_Due_To_ITCH_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Syndromic_Multisystem_Autoimmune_Disease_Due_To_ITCH_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Syndromic Multisystem Autoimmune Disease Due to ITCH Deficiency
- **MONDO ID:** MONDO:0013245 (if available)
- **Causal gene(s):** ITCH
- **OMIM:** OMIM:613385
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Syndromic Multisystem Autoimmune Disease Due to ITCH Deficiency** covering all of the
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

# Syndromic Multisystem Autoimmune Disease Due to ITCH Deficiency — Comprehensive Research Report

**Disease:** Syndromic Multisystem Autoimmune Disease Due to ITCH Deficiency
**MONDO ID:** MONDO:0013245 · **OMIM:** #613385 · **Orphanet:** ORPHA:228426 · **GARD:** 0010775
**Causal gene:** ***ITCH*** (itchy E3 ubiquitin protein ligase; HGNC:13890; NCBI Gene 83737; UniProt Q96J02; 20q11.22)
**Category:** Mendelian, autosomal recessive

> Note: the gene symbol *ITCH* derives from the "itchy" mouse and should not be confused with pruritus or other "itch" phenotypes. The identifiers above (MONDO:0013245, OMIM 613385, gene *ITCH* on chr20) define this entry.

---

## Summary

**Syndromic multisystem autoimmune disease due to ITCH deficiency is an autosomal-recessive primary immune-regulatory disorder caused by biallelic loss-of-function variants in *ITCH***, the gene encoding the itchy E3 ubiquitin protein ligase — a NEDD4-family HECT-domain enzyme located at chromosome 20q11.22. The condition was first defined in 2010 in a large Old Order Amish kindred, in which autozygosity mapping linked the phenotype to chromosome 20 and identified a homozygous truncating *ITCH* mutation (the founder frameshift allele c.378_394del) in ten affected patients ([PMID: 20170897](https://pubmed.ncbi.nlm.nih.gov/20170897/)). The disorder carries the synonyms **"Autoimmune Disease, Multisystem, with Facial Dysmorphism (ADMFD)"** and **"ITCH E3 ubiquitin ligase deficiency."**

Mechanistically, ITCH is an E3 ubiquitin ligase that enforces peripheral T-cell tolerance. It ubiquitylates and degrades a defined set of substrates — JunB, c-Jun, Notch, p63/p73, c-FLIP and TIEG1 — and participates in the A20 (TNFAIP3)/TAX1BP1 ubiquitin-editing complex that restrains NF-κB signaling. When ITCH is absent, these brakes fail: JunB accumulates and drives Th2 skewing, T cells cannot be rendered anergic, TGF-β/Foxp3-dependent regulatory T-cell generation is impaired, and NF-κB signaling is disinhibited. The net result is early-onset, progressive, multi-organ autoimmunity — autoimmune hepatitis, enteropathy, chronic interstitial lung disease, thyroiditis, type 1 diabetes, myositis and arthritis — layered on a syndromic background of failure to thrive, facial dysmorphism and developmental delay.

The disease has high morbidity and mortality. Management rests on broad immunosuppression for individual autoimmune manifestations, but the only reported disease-modifying/curative therapy is **allogeneic hematopoietic stem cell transplantation (HSCT)**, which produced durable multisystem remission at three years in a severely affected patient ([PMID: 42148098](https://pubmed.ncbi.nlm.nih.gov/42148098/)). The **itchy / non-agouti-lethal 18H (a18H) mouse**, in which a paracentric inversion disrupts *Itch*, faithfully recapitulates the human multi-organ immunopathology and remains the principal model organism. A 2022 report also expanded the phenotype to include a cellular mitochondrial bioenergetic defect ([PMID: 36338154](https://pubmed.ncbi.nlm.nih.gov/36338154/)).

---

## 1. Disease Information

**Overview.** ITCH deficiency is a rare monogenic syndrome combining systemic autoimmunity with dysmorphic and developmental features. Affected children typically present in infancy or early childhood with failure to thrive, distinctive facial dysmorphism, developmental delay, and organ-specific autoimmune disease that accrues over time. The original description emphasized that patients "not only have multisystem autoimmune disease but also display morphologic and developmental abnormalities" ([PMID: 20170897](https://pubmed.ncbi.nlm.nih.gov/20170897/)), i.e., the disorder is *syndromic* rather than a pure immune dysregulation phenotype.

**Key identifiers (verified cross-references for MONDO:0013245).**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0013245 |
| OMIM | #613385 |
| Orphanet | ORPHA:228426 |
| GARD | 0010775 |
| MedGen / UMLS | C3150649 (MedGen 461999) |
| NANDO | 2200739 |
| ICD-11 (foundation) | 1970749000 |
| Causal gene (HGNC) | HGNC:13890 (*ITCH*) |
| NCBI Gene | 83737 |
| Ensembl | ENSG00000078747 |

**Synonyms / alternative names.** "Autoimmune disease, multisystem, with facial dysmorphism (ADMFD)"; "ITCH E3 ubiquitin ligase deficiency"; "ITCH deficiency"; "syndromic multisystem autoimmune disease due to ITCH deficiency."

**Source of information.** The knowledge base entry is derived from aggregated disease-level resources (OMIM, Orphanet, MONDO) combined with individual-patient case reports and small case series (the original Amish cohort of 10 patients; subsequent White British, Black German, and other individual patients). There is no large EHR-derived or registry dataset for this ultra-rare disease — knowledge is derived from **individual patient reports and functional studies**, supplemented by the *Itch*-null mouse and in-vitro biochemistry.

---

## 2. Etiology

**Primary cause — genetic.** The disease is caused by biallelic (homozygous or compound-heterozygous) loss-of-function variants in *ITCH*. The founding event in the Amish population is a homozygous truncating frameshift (c.378_394del, p.Lys126fs). Other patients carry two novel variants resulting in complete absence of ITCH protein in fibroblasts ([PMID: 20170897](https://pubmed.ncbi.nlm.nih.gov/20170897/); [PMID: 36338154](https://pubmed.ncbi.nlm.nih.gov/36338154/)).

**Genetic risk factors.** The disorder is Mendelian; the causal risk factor is inheritance of two pathogenic *ITCH* alleles. In the Amish founder population, the single frameshift allele segregates at elevated frequency; **consanguinity** and membership in a genetically isolated founder population are the dominant risk-conferring circumstances. Carrier (heterozygous) status is not known to cause disease.

**Environmental risk factors.** None established as causal. Because the phenotype is autoimmune, environmental immune triggers (infections, antigenic exposures) plausibly modulate the timing or severity of specific autoimmune flares, but no specific environmental factor has been demonstrated. Age (young) and the autoimmune milieu influence expression; a firm sex predominance has not been established in this small cohort.

**Protective factors.** No genetic or environmental protective factors have been identified for this monogenic recessive disease (not applicable in the usual GWAS/epidemiological sense).

**Gene–environment interactions.** Mechanistically, loss of ITCH removes a tolerance checkpoint, so ordinary antigenic/environmental stimuli that would normally be tolerized instead provoke autoimmunity. In the mouse model, high-dose tolerizing antigen **failed** to block airway inflammation in *Itch⁻/⁻* animals ([PMID: 16557301](https://pubmed.ncbi.nlm.nih.gov/16557301/)) — a direct demonstration that the genetic lesion reprograms the response to an environmental (antigen) exposure. No formal human GxE data exist.

---

## 3. Phenotypes

ITCH deficiency is a multisystem disorder. The table below summarizes the principal phenotypes compiled from the original Amish series and subsequent case reports, with suggested HPO terms.

| Phenotype | Type | Onset | Frequency (qualitative) | Suggested HPO term |
|---|---|---|---|---|
| Failure to thrive / growth failure | Physical / constitutional | Infancy | Common (core feature) | HP:0001508 |
| Dysmorphic facial features | Physical | Congenital | Common (core feature) | HP:0001999 |
| Developmental delay | Neurodevelopmental | Infancy/childhood | Common (core feature) | HP:0001263 |
| Autoimmune hepatitis | Clinical sign / lab | Childhood | Frequent; can cause acute liver failure | HP:0001409 (hepatitis) + HP:0002960 (autoimmunity) |
| Chronic interstitial lung disease | Clinical sign | Childhood | Severe cases (tracheostomy, ventilation) | HP:0006530 |
| Enteropathy / chronic diarrhea | Clinical sign | Childhood | Frequent | HP:0004386 |
| Thyroiditis (autoimmune) | Lab / clinical | Childhood | Reported | HP:0100646 |
| Type 1 diabetes mellitus | Lab / clinical | Childhood | Reported | HP:0100651 |
| Juvenile polymyositis / myositis | Clinical sign | Childhood | Reported | HP:0003198 |
| Inflammatory (autoimmune) arthritis | Clinical sign | Childhood | Reported | HP:0001369 |
| Psoriasis | Physical / skin | Childhood | Reported | HP:0003765 |
| Sjögren's-like parotitis | Clinical sign | Childhood | Reported | HP:0030149 (parotitis) |
| Immune / autoimmune neutropenia | Lab | Childhood | Reported | HP:0001882 |

**Characteristics.** Onset is early (neonatal to early childhood) with an **insidious-then-progressive** course: the syndromic features (failure to thrive, dysmorphism, developmental delay) are present early, and autoimmune organ involvement accumulates over time. Severity ranges from moderate to severe/life-threatening, with autoimmune hepatitis capable of progressing to acute liver failure ([PMID: 30705142](https://pubmed.ncbi.nlm.nih.gov/30705142/)) and chronic lung disease requiring tracheostomy and long-term ventilation ([PMID: 42148098](https://pubmed.ncbi.nlm.nih.gov/42148098/)). Expressivity is variable even among patients sharing the same genotype.

**Quality-of-life impact.** Severe. Chronic ventilator dependence, recurrent autoimmune flares, hepatic and gastrointestinal dysfunction, developmental delay and failure to thrive collectively impose a very high burden on daily functioning. No disease-specific EQ-5D/SF-36/PROMIS data exist for this ultra-rare condition.

---

## 4. Genetic / Molecular Information

**Causal gene.** *ITCH* (itchy E3 ubiquitin protein ligase), HGNC:13890, OMIM *606409, NCBI Gene 83737, Ensembl ENSG00000078747, located at 20q11.22. RefSeq transcript NM_031483.7; protein UniProt Q96J02, 903 amino acids.

**Protein domain architecture.** ITCH is a NEDD4-family E3 ligase with:
- an N-terminal **C2 domain** (≈ aa 1–115; membrane/Ca²⁺-phospholipid binding),
- four **WW domains** (≈ aa 326–511; substrate recognition via PY motifs), and
- a C-terminal catalytic **HECT domain** (≈ aa 569–903; ubiquitin transfer) ([PMID: 24787015](https://pubmed.ncbi.nlm.nih.gov/24787015/)).

**Pathogenic variants.** ClinVar pathogenic / likely-pathogenic alleles are overwhelmingly loss-of-function:

| Variant (cDNA) | Protein | Class | Note |
|---|---|---|---|
| c.378_394del | p.Lys126fs | Frameshift | **Amish founder allele** |
| c.1300_1303del | p.Leu434fs | Frameshift | |
| c.2334del | p.Ile778fs | Frameshift | |
| — | p.Gln121Ter | Nonsense | |
| — | p.Trp65Ter | Nonsense | |
| — | p.Trp555Ter | Nonsense | |
| — | p.Tyr579Ter | Nonsense | |
| c.337+1G>A | — | Canonical splice-site | |
| c.1569+1G>T | — | Canonical splice-site | |
| c.2214+1G>T | — | Canonical splice-site | |
| — | p.Met1Ile | Start-loss | |

**Variant classification & population frequency.** Variants are classified pathogenic / likely pathogenic under ACMG/AMP criteria (predicted LOF in a gene with an established LOF disease mechanism). Pathogenic alleles are extremely rare in gnomAD; the Amish frameshift is enriched specifically in that founder population.

**Functional consequence.** **Loss of function.** The Amish allele produces a truncated protein ([PMID: 20170897](https://pubmed.ncbi.nlm.nih.gov/20170897/)); in other patients, ITCH protein is completely absent from fibroblasts ([PMID: 36338154](https://pubmed.ncbi.nlm.nih.gov/36338154/)). **Somatic vs germline:** germline. **Chromosomal abnormalities:** none required in humans; however, the mouse model arises from a paracentric inversion disrupting *Itch* (see §15).

**Modifier genes / epigenetics.** No specific human modifier genes or disease-driving epigenetic changes have been defined. Mechanistically ITCH cooperates with Cbl-b/Nedd4 in tolerance circuits (see §6), which could in principle modulate expressivity, but this is not demonstrated for human disease severity.

---

## 5. Environmental Information

- **Environmental factors (toxins/radiation/occupational):** none implicated.
- **Lifestyle factors:** none implicated.
- **Infectious agents:** none causal. Infections may act as nonspecific immune triggers, and infectious susceptibility is a clinical concern in immune-dysregulated, immunosuppressed patients, but no pathogen causes or defines the disease.

This is a fundamentally **genetic** disorder; environmental contributions are secondary modulators at most.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function *ITCH* mutation** (e.g., Amish c.378_394del frameshift) **leads to** absence or truncation of the ITCH HECT-domain E3 ubiquitin ligase. *(Demonstrated — truncated/absent protein in patients.)*
2. Loss of ITCH catalytic activity **results in** failure to ubiquitylate and degrade ITCH substrates — **JunB, c-Jun, Notch, p63/p73, c-FLIP, and TIEG1** — which therefore accumulate. *(Demonstrated for substrates in vitro/mouse.)*
3. **Branch A — Th2 skewing:** accumulation of **JunB** (a Th2-driving transcription factor) **leads to** excessive Th2 differentiation with elevated IL-4, IL-5, IgG1 and IgE. *(Demonstrated in itchy mice.)*
4. **Branch B — failed anergy/tolerance:** loss of ITCH-mediated ubiquitination, which normally converges with **MEKK1–JNK signaling**, **results in** inability to induce T-cell anergy; tolerizing antigen can no longer suppress responses. *(Demonstrated — high-dose antigen fails to tolerize Itch⁻/⁻ mice.)*
5. **Branch C — deficient Treg generation:** loss of ITCH-mediated monoubiquitination of **TIEG1** **leads to** reduced Foxp3 transcription and impaired TGF-β–induced regulatory T-cell generation. *(Demonstrated mechanistically.)*
6. **Branch D — NF-κB disinhibition:** loss of ITCH within the **A20 (TNFAIP3)/TAX1BP1 ubiquitin-editing complex** **results in** failure to downregulate K63-linked ubiquitination of TRAF6, **leading to** sustained NF-κB signaling and pro-inflammatory gene expression. *(Demonstrated in the complex; contribution to human disease inferred.)*
7. Branches A–D converge: Th2 skewing + failed anergy + deficient Tregs + NF-κB disinhibition **result in** breakdown of peripheral T-cell tolerance and chronic activation of autoreactive lymphocytes. *(Inferred synthesis.)*
8. Autoreactive, Th2-skewed, poorly regulated lymphocytes **lead to** multi-organ autoimmune attack — liver (autoimmune hepatitis), gut (enteropathy), lung (interstitial inflammation), thyroid, pancreatic islets (T1D), muscle (myositis), joints, skin. *(Demonstrated clinically.)*
9. In parallel/downstream, cellular **mitochondrial bioenergetic dysfunction** (reduced mtDNA copy number, decreased fatty-acid oxidation, oxidative phosphorylation and ATP production) **contributes to** tissue vulnerability and the syndromic growth/developmental features. *(Demonstrated in one patient; relationship to autoimmunity inferred.)*

### Supporting detail

**Molecular pathways.** Ubiquitin–proteasome system (ITCH HECT E3 ligase); TGF-β → TIEG1 → Foxp3 (Treg generation); MEKK1–JNK (anergy); JunB/AP-1 (Th2 transcription); A20/TAX1BP1–TRAF6–NF-κB (innate/inflammatory signaling); Notch signaling (via Notch as an ITCH substrate).

**Cellular processes.** T-cell differentiation and tolerance (anergy), regulatory T-cell development, Th1/Th2 balance, autophagy regulation (ITCH substrates affect cell fate), inflammation. Suggested **GO** terms: GO:0016567 (protein ubiquitination), GO:0002456 (T cell–mediated immunity), GO:0002667 (regulation of T-cell anergy), GO:0050852 (T cell receptor signaling), GO:0043123 (positive regulation of canonical NF-κB signal transduction).

**Protein dysfunction.** Loss of function of the E3 ligase — the catalytic HECT domain (or the whole protein) is lost, abolishing substrate ubiquitination. ITCH *"is a HECT domain-containing E3 ligase that promotes the ubiquitylation and degradation of several proteins, including p73, p63, c-Jun, JunB, Notch and c-FLIP, thus affecting cell fate"* ([PMID: 24787015](https://pubmed.ncbi.nlm.nih.gov/24787015/)).

**Metabolic changes.** Mitochondrial dysfunction: patient muscle mtDNA copy number was **57% of controls**, with decreased mitochondrial fatty-acid oxidation, decreased oxidative phosphorylation and decreased ATP production in fibroblasts ([PMID: 36338154](https://pubmed.ncbi.nlm.nih.gov/36338154/)).

**Immune system involvement.** Central: autoimmunity driven by failed peripheral tolerance. *"E3 ligases Cbl-b and Itch have emerged as dominant 'tolerogenic' regulators of T cells because their deficiency results in severe autoimmune diseases"* ([PMID: 20395198](https://pubmed.ncbi.nlm.nih.gov/20395198/)).

**Cell types involved.** CD4⁺ T helper cells (Th2), regulatory T cells (Foxp3⁺ Tregs), and antigen-stimulated effector T cells. Suggested **CL** terms: CL:0000624 (CD4-positive, alpha-beta T cell), CL:0000815 (regulatory T cell), CL:0000899 (Th2 cell).

### Mechanistic schematic

```
 Biallelic LOF ITCH mutation
            │
            ▼
   Absent / truncated ITCH E3 ligase
            │  (no ubiquitination/degradation of substrates)
            ▼
 ┌───────────┬───────────────┬────────────────┬───────────────────┐
 │ JunB ↑    │ MEKK1-JNK     │ TIEG1 not       │ A20/TAX1BP1       │
 │           │ anergy axis   │ mono-Ub'd       │ complex impaired  │
 ▼           ▼               ▼                 ▼
 Th2 skew    Failed T-cell   ↓Foxp3 →          ↑K63-Ub TRAF6 →
 (IL-4/5,    anergy          ↓Treg generation   sustained NF-κB
  IgE/IgG1)
 └───────────┴───────────────┴────────────────┴───────────────────┘
            │
            ▼
   Breakdown of peripheral T-cell tolerance
            │
            ▼
   Multi-organ autoimmunity  +  mitochondrial bioenergetic defect
   (liver, gut, lung, thyroid, islets, muscle, joints, skin)
            │
            ▼
   Syndromic multisystem autoimmune disease (ADMFD)
```

---

## 7. Anatomical Structures Affected

**Organ level (primary).** Liver (autoimmune hepatitis; UBERON:0002107), lung (chronic interstitial inflammation; UBERON:0002048), gastrointestinal tract / intestine (enteropathy; UBERON:0000160), thyroid gland (thyroiditis; UBERON:0002046), endocrine pancreas / islets (type 1 diabetes; UBERON:0000006), skeletal muscle (myositis; UBERON:0001134), joints (arthritis; UBERON:0001474), skin (psoriasis; UBERON:0002097), salivary/parotid gland (parotitis; UBERON:0001831).

**Body systems.** Immune/lymphoid (primary), hepatobiliary, respiratory, digestive, endocrine, musculoskeletal, integumentary.

**Tissue and cell level.** Autoimmune attack targets epithelial and glandular tissues (hepatocytes, intestinal and alveolar epithelium, thyroid follicular cells, pancreatic β-cells, salivary epithelium). Effector cells are lymphoid. In the mouse model there is **hyperplasia of lymphoid cells, haematopoietic cells and forestomach epithelium** ([PMID: 9462742](https://pubmed.ncbi.nlm.nih.gov/9462742/)). Suggested CL terms: CL:0000624 (CD4⁺ T cell), CL:0000815 (Treg), CL:0000899 (Th2 cell).

**Subcellular level.** Cytoplasm/plasma membrane (ITCH C2-domain membrane association; ubiquitination machinery), nucleus (transcription-factor substrates JunB/c-Jun/p63/p73/TIEG1→Foxp3), and **mitochondria** (bioenergetic defect). Suggested GO cellular-component terms: GO:0005829 (cytosol), GO:0005739 (mitochondrion), GO:0005634 (nucleus).

**Localization / lateralization.** Systemic and bilateral — a multi-organ, generalized autoimmune process without lateralization.

---

## 8. Temporal Development

**Onset.** Early — neonatal to early childhood. The syndromic features (failure to thrive, facial dysmorphism, developmental delay) are congenital/early-infantile; autoimmune organ disease begins in infancy/childhood. Onset pattern is **insidious/chronic**.

**Progression.** **Progressive and accumulating.** Patients add autoimmune manifestations over time — a representative patient *"subsequently accumulated multiple autoimmune manifestations including autoimmune hepatitis, enteropathy, psoriasis, inflammatory arthritis, and Sjögren's-like parotitis"* ([PMID: 42148098](https://pubmed.ncbi.nlm.nih.gov/42148098/)). Individual organ processes can be chronic-progressive (interstitial lung disease, hepatitis) or flaring. Progression rate is variable; overall course is chronic and lifelong absent curative therapy.

**Patterns.** Remission of individual manifestations is treatment-induced (immunosuppression) rather than spontaneous; the one reported **durable, multisystem remission** followed HSCT ([PMID: 42148098](https://pubmed.ncbi.nlm.nih.gov/42148098/)). **Critical period / window of opportunity:** transplantation before irreversible end-organ damage (e.g., before fixed lung fibrosis or liver failure) is the key intervention window.

---

## 9. Inheritance and Population

**Inheritance.** Autosomal recessive (OMIM #613385, MONDO:0013245). Disease requires two pathogenic *ITCH* alleles.

**Epidemiology.** Ultra-rare; no reliable prevalence/incidence figures. The original cohort comprised **10 consanguineous Old Order Amish patients**; subsequent individual patients of White British and Black German ethnicity have been reported, expanding the ethnic range beyond the Amish founder population ([PMID: 36338154](https://pubmed.ncbi.nlm.nih.gov/36338154/)).

**Penetrance / expressivity.** Penetrance of the biallelic genotype appears high (essentially complete for the disorder), but **expressivity is variable** — which organs are affected and disease severity differ among patients, even within the founder genotype.

**Founder effect / consanguinity.** Strong founder effect in the Old Order Amish (single frameshift allele c.378_394del enriched by genetic isolation); consanguinity is a major risk circumstance, as expected for an AR disorder.

**Carrier frequency.** Elevated specifically within the Amish founder population; very low in the general population.

**Demographics.** No established sex predominance; affected individuals are children. Geographic clustering historically centered on Amish communities, with sporadic cases worldwide.

**Genetic anticipation / mosaicism.** Not applicable (not a repeat-expansion disorder); no germline-mosaicism reports.

---

## 10. Diagnostics

**Clinical laboratory.** Organ-specific autoimmune serologies and function tests reflecting involved systems — e.g., elevated transaminases and autoantibodies / hypergammaglobulinemia in autoimmune hepatitis; thyroid autoantibodies; islet autoantibodies / hyperglycemia in T1D; muscle enzymes in myositis; blood counts (immune neutropenia). These are nonspecific individually.

**Biomarkers.** The definitive biomarker is molecular: biallelic pathogenic *ITCH* variants and/or **absent ITCH protein** on immunoblot of patient fibroblasts ([PMID: 36338154](https://pubmed.ncbi.nlm.nih.gov/36338154/)). Mitochondrial studies (reduced mtDNA copy number; reduced fatty-acid oxidation / OXPHOS / ATP) can be a supportive cellular biomarker.

**Imaging / functional / pathology.** Chest imaging and pulmonary function for interstitial lung disease; liver biopsy may show interface hepatitis; muscle biopsy for myositis. Findings reflect the specific autoimmune organ disease rather than being disease-specific.

**Genetic testing (the diagnostic cornerstone).** Because the phenotype is syndromic and overlaps with other primary immune-regulatory and primary atopic disorders, **upfront broad genomic sequencing (WGS or WES)** is recommended for rapid diagnosis of such rare monogenic immune disorders ([PMID: 39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/)). Approaches in order of typical utility: WES/WGS → inborn-errors-of-immunity / primary-immunodeficiency gene panels including *ITCH* → targeted single-gene *ITCH* testing (useful in Amish probands where the founder allele is known). Chromosomal microarray/karyotype/FISH are not primary tools (no recurrent CNV cause in humans). mtDNA testing and repeat-expansion testing are not indicated.

**Clinical criteria / differential diagnosis.** No formal consensus diagnostic criteria exist; diagnosis is molecular. The differential includes other monogenic autoimmunity/immune-dysregulation syndromes — IPEX (FOXP3), CTLA-4 haploinsufficiency, LRBA deficiency, APECED (AIRE), STAT-related disorders, and primary atopic disorders ([PMID: 39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/)). Pediatric autoimmune hepatitis of unexplained cause should prompt consideration of *ITCH* mutation ([PMID: 30705142](https://pubmed.ncbi.nlm.nih.gov/30705142/)), and atypical steroid-refractory cholestatic/hepatic disease warrants genetic testing ([PMID: 41878599](https://pubmed.ncbi.nlm.nih.gov/41878599/)).

**Screening.** In the Amish, carrier/cascade screening for the known founder allele and prenatal/targeted testing are feasible. No general newborn screening exists.

---

## 11. Outcome / Prognosis

**Survival / mortality.** The disorder carries **high morbidity and mortality** without effective immune control. Autoimmune hepatitis can progress to **acute liver failure** ([PMID: 30705142](https://pubmed.ncbi.nlm.nih.gov/30705142/)), and chronic interstitial lung disease can require tracheostomy and long-term ventilation ([PMID: 42148098](https://pubmed.ncbi.nlm.nih.gov/42148098/)). The original Amish description emphasized severe multisystem disease. No formal 5-/10-year survival statistics exist for this ultra-rare condition.

**Morbidity / function.** Severe cumulative disability from progressive multi-organ autoimmunity, growth failure and developmental delay.

**Disease course / complications.** Complications include liver failure, respiratory failure, malabsorption/failure to thrive, endocrinopathy (T1D, thyroid disease), and complications of chronic immunosuppression (infection).

**Recovery potential.** With immunosuppression, individual manifestations can be controlled but not cured; relapse is typical. **Durable multisystem recovery has been achieved with HSCT** — sustained immune and pulmonary recovery three years post-transplant ([PMID: 42148098](https://pubmed.ncbi.nlm.nih.gov/42148098/)).

**Prognostic factors.** Severity/number of organs involved, presence of irreversible end-organ damage (lung fibrosis, liver failure) at the time of definitive therapy, and access to HSCT.

---

## 12. Treatment

**Pharmacotherapy (immunosuppression/immunomodulation).** Management is organ-directed immunosuppression — corticosteroids and steroid-sparing agents (e.g., azathioprine, mycophenolate, calcineurin inhibitors) for autoimmune hepatitis, enteropathy, myositis and arthritis; topical/systemic therapy for psoriasis; standard endocrine replacement for T1D and thyroid disease. Responses are partial and relapse is common. Suggested **NCIT** concepts: C15282 (Immunosuppressive Therapy), C305 (Corticosteroid), C2008 (Immunotherapy).

**Advanced / curative therapeutics.** **Allogeneic hematopoietic stem cell transplantation (HSCT)** is the only reported disease-modifying/curative option: *"These findings support consideration of HSCT as a therapeutic option in carefully selected patients with severe, refractory autoimmune manifestations due to ITCH deficiency"* ([PMID: 42148098](https://pubmed.ncbi.nlm.nih.gov/42148098/)), producing durable multisystem remission at three years. Suggested NCIT: C15431 (Hematopoietic Stem Cell Transplantation), C9306 (Allogeneic Bone Marrow Transplantation). Gene therapy, cell therapy (other than HSCT), RNA-based and targeted biologic therapies specific to ITCH deficiency are not yet established.

**Pharmacogenomics.** No ITCH-specific pharmacogenomic guidance. Of note, a drug-discovery screen identified antidepressants as modulators of ITCH activity/autophagy — a pharmacological-tool finding, not a therapy for this disease ([PMID: 24787015](https://pubmed.ncbi.nlm.nih.gov/24787015/)).

**Surgical / supportive / rehabilitative.** Supportive care is central: nutritional support for failure to thrive/enteropathy, respiratory support (tracheostomy, ventilation), management of liver disease (including transplantation consideration for liver failure), and developmental/rehabilitative services.

**Treatment strategy.** Escalate from organ-directed immunosuppression to consideration of **HSCT in severe, refractory, multisystem disease**, ideally before irreversible end-organ damage. There are no published formal treatment algorithms or combination-therapy trials for ITCH deficiency specifically.

---

## 13. Prevention

**Primary prevention.** Not possible for a monogenic recessive disease once both pathogenic alleles are inherited. Primary prevention is reproductive/genetic: **carrier screening, genetic counseling, and reproductive options** (prenatal diagnosis, preimplantation genetic testing), especially in the Amish founder population and consanguineous families.

**Secondary prevention.** Early molecular diagnosis via upfront genomic sequencing enables earlier immunomodulation and earlier consideration of HSCT — limiting cumulative organ damage ([PMID: 39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/)). Cascade testing of relatives of a proband (particularly for the known Amish allele) is valuable.

**Tertiary prevention.** Preventing complications in affected patients: vigilant surveillance for new autoimmune organ involvement, infection prophylaxis under immunosuppression, nutritional/respiratory support, and timely transplantation.

**Counseling.** Autosomal-recessive genetic counseling: 25% recurrence risk per pregnancy for carrier couples; cascade carrier testing; discussion of founder-allele frequency where relevant.

**Immunization / public health / environmental.** No disease-specific vaccine or public-health/environmental prevention; standard immunization caution applies under immunosuppression (avoid live vaccines as clinically indicated).

---

## 14. Other Species / Natural Disease

**Taxonomy / orthologs.** Mouse ortholog *Itch* (MGI:1202301; NCBI Gene 16396; Ensembl ENSMUSG00000027598; chromosome 2). The gene and its tolerance function are evolutionarily conserved in mammals.

**Natural disease in animals.** The best-characterized natural/spontaneous model is the **mouse itchy mutant (non-agouti-lethal 18H, a18H)**, a spontaneously arising allele in which a paracentric inversion disrupts both *agouti* and *Itch* ([PMID: 9462742](https://pubmed.ncbi.nlm.nih.gov/9462742/)). No companion-animal (OMIA-catalogued) natural ITCH-deficiency disease is established.

**Comparative pathology.** The mouse immunopathology strikingly parallels the human disease (multi-organ autoimmune/inflammatory involvement of lung, gut, skin and lymphoid tissue), supporting a conserved mechanism. **Zoonotic potential:** none (genetic disease).

---

## 15. Model Organisms

**Principal model — the itchy / a18H mouse.** The *itchy* locus was discovered in non-agouti-lethal 18H (a18H) mice; *"a18H results from an inversion and … Itch encodes a novel E3 ubiquitin protein ligase"* ([PMID: 9462742](https://pubmed.ncbi.nlm.nih.gov/9462742/)). Affected mice develop **background-dependent immunopathology**: on some backgrounds inflammatory large-intestine disease; on C57BL/6J *"they develop a fatal disease characterized by pulmonary chronic interstitial inflammation and alveolar proteinosis, inflammation of the glandular stomach and skin resulting in scarring due to constant itching, and hyperplasia of lymphoid cells, haematopoietic cells and the forestomach epithelium"* ([PMID: 9462742](https://pubmed.ncbi.nlm.nih.gov/9462742/)).

**Mechanistic/knockout models.** *Itch⁻/⁻* mice show Th2-skewed activation with elevated IL-4, IL-5, IgG1 and IgE, and defective Th2 tolerance: *"Itch associated with and induced ubiquitination of JunB, a transcription factor that is involved in TH2 differentiation"* ([PMID: 11828324](https://pubmed.ncbi.nlm.nih.gov/11828324/)); and *"injection of high-dose tolerizing antigen failed to block the development of airway inflammation in Itch-/- mice"* ([PMID: 16557301](https://pubmed.ncbi.nlm.nih.gov/16557301/)). These models also established the TIEG1→Foxp3/Treg and MEKK1-JNK axes.

**Phenotype recapitulation.** Excellent for the autoimmune/inflammatory (lung, gut, skin, lymphoid) and immunological (Th2 skew, failed tolerance, Treg deficit) features. **Limitations:** the mouse does not reproduce the human syndromic facial dysmorphism/developmental features, and the agouti-coat phenotype is a mouse-specific artifact of the linked inversion. **Cellular models:** patient-derived skin fibroblasts have been used to show absent ITCH protein and the mitochondrial bioenergetic defect ([PMID: 36338154](https://pubmed.ncbi.nlm.nih.gov/36338154/)). **Resources:** MGI (*Itch*, MGI:1202301).

---

## Key Findings (with evidence)

### F1 — Biallelic *ITCH* truncating mutation causes the disease (first human ITCH deficiency)
Autozygosity mapping in a large Old Order Amish kindred linked the disease to chromosome 20, identifying a homozygous truncating *ITCH* mutation in 10 affected patients; inheritance is autosomal recessive. *"Using autozygosity mapping in a large Amish kindred, we identified a linkage region on chromosome 20 and selected candidate genes for screening. We describe, in ten patients, identification of a mutation resulting in truncation of ITCH"* and these patients *"not only have multisystem autoimmune disease but also display morphologic and developmental abnormalities"* ([PMID: 20170897](https://pubmed.ncbi.nlm.nih.gov/20170897/)).

### F2 — ITCH is a HECT-domain E3 ligase with defined substrates
*"ITCH is a HECT domain-containing E3 ligase that promotes the ubiquitylation and degradation of several proteins, including p73, p63, c-Jun, JunB, Notch and c-FLIP, thus affecting cell fate"* ([PMID: 24787015](https://pubmed.ncbi.nlm.nih.gov/24787015/)); *"Itch associated with and induced ubiquitination of JunB"* ([PMID: 11828324](https://pubmed.ncbi.nlm.nih.gov/11828324/)).

### F3 — ITCH enforces peripheral T-cell tolerance (Treg + anergy)
*"Itch promotes ubiquitin conjugation to TGF-beta inducible early gene 1 product (TIEG1). Moreover, monoubiquitinated TIEG1 positively modulates the transcription of Foxp3 gene"* ([PMID: 19198068](https://pubmed.ncbi.nlm.nih.gov/19198068/)); *"injection of high-dose tolerizing antigen failed to block the development of airway inflammation in Itch-/- mice"* ([PMID: 16557301](https://pubmed.ncbi.nlm.nih.gov/16557301/)); *"E3 ligases Cbl-b and Itch have emerged as dominant 'tolerogenic' regulators of T cells because their deficiency results in severe autoimmune diseases"* ([PMID: 20395198](https://pubmed.ncbi.nlm.nih.gov/20395198/)).

### F4 — Clinical spectrum and HSCT as disease-modifying therapy
*"subsequently accumulated multiple autoimmune manifestations including autoimmune hepatitis, enteropathy, psoriasis, inflammatory arthritis, and Sjögren's-like parotitis"* and *"These findings support consideration of HSCT as a therapeutic option in carefully selected patients with severe, refractory autoimmune manifestations due to ITCH deficiency"* ([PMID: 42148098](https://pubmed.ncbi.nlm.nih.gov/42148098/)). ITCH mutation also causes pediatric intractable autoimmune hepatitis with risk of acute liver failure ([PMID: 30705142](https://pubmed.ncbi.nlm.nih.gov/30705142/)).

### F5 — ADMFD synonym and syndromic triad
*"Autoimmune Disease, Multisystem, with Facial Dysmorphism (ADMFD) is an autosomal recessive disorder due to pathogenic variants in the ITCH gene. It is characterized by failure to thrive, dysmorphic facial features, developmental delay, and systemic autoimmunity…"* and *"It was originally described in 10 consanguineous Old Order Amish patients, and more recently in two patients of White British and Black German ethnicities"* ([PMID: 36338154](https://pubmed.ncbi.nlm.nih.gov/36338154/)).

### F6 — Mitochondrial bioenergetic dysfunction (phenotype expansion)
*"Clinical studies of patient muscle showed mitochondrial DNA copy number of 57% compared to controls. Functional studies in skin fibroblasts revealed decreased activity of mitochondrial fatty acid oxidation and oxidative phosphorylation, and decreased overall ATP production"* ([PMID: 36338154](https://pubmed.ncbi.nlm.nih.gov/36338154/)).

### F7 — itchy/a18H mouse recapitulates the multi-organ disease
*"they develop a fatal disease characterized by pulmonary chronic interstitial inflammation and alveolar proteinosis, inflammation of the glandular stomach and skin resulting in scarring due to constant itching, and hyperplasia of lymphoid cells, haematopoietic cells and the forestomach epithelium"*; *"a18H results from an inversion and … Itch encodes a novel E3 ubiquitin protein ligase"* ([PMID: 9462742](https://pubmed.ncbi.nlm.nih.gov/9462742/)).

### F8 — ITCH in the A20/TAX1BP1 complex restraining NF-κB
*"…ubiquitin-editing enzyme A20 complex including A20, Tax1-binding protein 1 (TAX1BP1) and Itch, … subsequently downregulated the K63-ubiquitination of TNF receptor associated factor 6 (TRAF6) and NF-κB signaling pathway"* ([PMID: 34454289](https://pubmed.ncbi.nlm.nih.gov/34454289/)).

### F9 — Variant spectrum: biallelic LOF; Amish founder frameshift
RefSeq NM_031483.7; UniProt Q96J02 (903 aa); domains: C2 (aa 1–115), 4× WW (aa 326–511), HECT (aa 569–903). ClinVar P/LP alleles are overwhelmingly LOF (frameshift incl. founder c.378_394del; nonsense; canonical splice-site; start-loss). The founder allele yields a truncated protein ([PMID: 20170897](https://pubmed.ncbi.nlm.nih.gov/20170897/)); other patients show complete absence of ITCH protein ([PMID: 36338154](https://pubmed.ncbi.nlm.nih.gov/36338154/)).

### F10 — Verified cross-reference identifiers
MONDO:0013245 ↔ OMIM 613385, Orphanet ORPHA:228426, GARD 0010775, MedGen/UMLS C3150649, NANDO 2200739, ICD-11 foundation 1970749000; gene ITCH HGNC:13890, NCBI 83737, Ensembl ENSG00000078747 (20q11.22); mouse Itch MGI:1202301, NCBI 16396.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [20170897](https://pubmed.ncbi.nlm.nih.gov/20170897/) | Human ITCH deficiency causes syndromic multisystem autoimmune disease | Human clinical / genetics | F1, F9 (gene discovery, founder allele, syndromic phenotype) |
| [36338154](https://pubmed.ncbi.nlm.nih.gov/36338154/) | ITCH phenotype expansion & mitochondrial dysfunction | Human clinical / in vitro | F5, F6, F9 (ADMFD synonym, ethnic expansion, mitochondrial defect, absent protein) |
| [42148098](https://pubmed.ncbi.nlm.nih.gov/42148098/) | Sustained recovery 3 yrs after HSCT for ITCH deficiency | Human clinical (case report) | F4 (clinical spectrum, curative HSCT) |
| [30705142](https://pubmed.ncbi.nlm.nih.gov/30705142/) | ITCH mutation & pediatric autoimmune hepatitis / liver failure | Human clinical | F4, F5 (hepatic phenotype) |
| [24787015](https://pubmed.ncbi.nlm.nih.gov/24787015/) | HTS for ITCH HECT ligase inhibitors | In vitro / biochemical | F2 (HECT class, substrate list, domains) |
| [11828324](https://pubmed.ncbi.nlm.nih.gov/11828324/) | Itch in TH2 differentiation (itchy mice) | Model organism | F2, F3, F7 (JunB substrate, Th2 skew) |
| [16557301](https://pubmed.ncbi.nlm.nih.gov/16557301/) | Itch ubiquitination + MEKK1-JNK in Th2 tolerance | Model organism | F3 (failed anergy, airway inflammation) |
| [19198068](https://pubmed.ncbi.nlm.nih.gov/19198068/) | Itch regulates T-cell differentiation / Foxp3 | Model organism / in vitro | F3 (TIEG1→Foxp3/Treg) |
| [20395198](https://pubmed.ncbi.nlm.nih.gov/20395198/) | Cbl-b and Itch: peripheral T-cell tolerance | Review | F3 (tolerogenic role) |
| [9462742](https://pubmed.ncbi.nlm.nih.gov/9462742/) | itchy locus / a18H mouse E3 ligase | Model organism | F7 (mouse model, inversion, E3 ligase) |
| [34454289](https://pubmed.ncbi.nlm.nih.gov/34454289/) | A20 ubiquitin-editing complex (incl. Itch) | In vitro / mechanistic | F8 (A20/TAX1BP1-TRAF6-NF-κB) |
| [39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/) | Upfront genomic sequencing for primary atopic disorders | Review / methodology | Diagnostics (WGS/WES approach) |
| [20108139](https://pubmed.ncbi.nlm.nih.gov/20108139/) | Foxp3⁺ Tregs regulated by Itch | Review | F3 (Treg regulation) |
| [20143240](https://pubmed.ncbi.nlm.nih.gov/20143240/) | iTregs in T1D show higher ITCH levels | Human / in vitro | Context: ITCH–Treg–T1D link |
| [41878599](https://pubmed.ncbi.nlm.nih.gov/41878599/) | Cholestatic liver disease / genetic testing in atypical cases | Human clinical | Diagnostics (genetic testing of atypical hepatic disease) |
| [16493086](https://pubmed.ncbi.nlm.nih.gov/16493086/) | Itch/Cbl-b/Nedd4 anergy factors in filariasis | Human / mechanistic | Context: anergy-factor network |

---

## Limitations and Knowledge Gaps

- **Extreme rarity / small N.** Human evidence rests on a founder Amish cohort (n=10) plus scattered case reports. Prevalence, incidence, penetrance and sex ratio are not quantifiable; expressivity is clearly variable but poorly parameterized.
- **No natural-history or registry data.** Survival, long-term outcomes and QoL metrics are anecdotal.
- **Mechanistic attribution.** The NF-κB/A20 branch and the mitochondrial defect are demonstrated biochemically / in single patients, but their quantitative contribution to the human autoimmune phenotype is inferred, not proven. The link between mitochondrial dysfunction and autoimmunity is unresolved (parallel effect vs. causal contributor).
- **Model gaps.** The itchy mouse omits the human syndromic dysmorphism/developmental features, and strain background strongly modifies its phenotype — limiting direct translation.
- **Therapeutics.** HSCT evidence is a single durable-remission case; optimal timing, conditioning, patient selection and risk/benefit versus organ-directed immunosuppression remain undefined. No gene/RNA/targeted therapy exists.
- **Variant-level data.** Genotype–phenotype correlations across the (few) known alleles are not established.

---

## Proposed Follow-up Experiments / Actions

1. **International patient registry & natural-history study** to quantify prevalence, organ-involvement frequencies, penetrance, survival and QoL, and to define genotype–phenotype correlations across known *ITCH* alleles.
2. **Systematic HSCT outcome collection** (timing, conditioning, GvHD, long-term immune/organ recovery) to build an evidence base for transplantation criteria and the therapeutic window before irreversible lung/liver damage.
3. **Deep immunophenotyping of patients** (Treg number/function, Th2 cytokines, NF-κB activation signatures) to validate, in humans, the Treg/anergy/NF-κB branches established in mice, and to identify monitorable biomarkers.
4. **Mechanistic dissection of the mitochondrial phenotype** — determine whether ITCH loss directly perturbs mitochondrial substrates/bioenergetics or whether the defect is secondary to chronic inflammation; test whether it contributes to tissue damage.
5. **Preclinical targeted-therapy evaluation** in *Itch⁻/⁻* mice — e.g., JAK/NF-κB inhibitors, Th2-directed biologics (anti-IL-4/IL-5), or Treg-enhancing strategies (low-dose IL-2) — to find disease-modifying pharmacotherapy short of HSCT.
6. **Patient-derived iPSC/organoid and gene-correction models** to study tissue-specific pathology and to provide a platform for future gene-replacement/editing approaches.
7. **Carrier/cascade screening programs** for the Amish founder allele with integrated genetic counseling and reproductive options.

---

*Report compiled from 10 confirmed findings and 16 reviewed papers over a 5-iteration autonomous investigation. Causal gene confirmed as **ITCH** (HGNC:13890) per the provided MONDO:0013245 / OMIM 613385 identifiers.*


## Artifacts

- [OpenScientist final report](Syndromic_Multisystem_Autoimmune_Disease_Due_To_ITCH_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Syndromic_Multisystem_Autoimmune_Disease_Due_To_ITCH_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 18 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013245` (7 mentions) - the report calls it "MONDO"; MONDO calls it **syndromic multisystem autoimmune disease due to ITCH deficiency**
- `HP:0001508` (1 mention) - the report calls it "Common (core feature)"; HP calls it **Failure to thrive**
- `HP:0006530` (1 mention) - the report calls it "Severe cases (tracheostomy, ventilation)"; HP calls it **Abnormal pulmonary interstitial morphology**
- `HP:0004386` (1 mention) - the report calls it "Frequent"; HP calls it **Gastrointestinal inflammation**
- `HP:0030149` (1 mention) - the report calls it "parotitis"; HP calls it **Cardiogenic shock**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001999` (1 mention) - the report calls it "Common (core feature)"; HP calls it **Abnormal facial shape**, and lists "Dysmorphic facial features" among its other names
- `HP:0001263` (1 mention) - the report calls it "Common (core feature)"; HP calls it **Global developmental delay**, and lists "Psychomotor development failure" among its other names
- `GO:0050852` (1 mention) - the report calls it "T cell receptor signaling"; GO calls it **T cell receptor signaling pathway**
- `GO:0043123` (1 mention) - the report calls it "positive regulation of canonical NF-κB signal transduction"; GO calls it **positive regulation of canonical NF-kappaB signal transduction**
- `CL:0000624` (2 mentions) - the report calls it "CD4-positive, alpha-beta T cell", "CD4⁺ T cell"; CL calls it **CD4-positive, alpha-beta T cell**
- `CL:0000815` (2 mentions) - the report calls it "regulatory T cell", "Treg"; CL calls it **regulatory T cell**, and lists "Treg" among its other names
- `CL:0000899` (2 mentions) - the report calls it "Th2 cell"; CL calls it **T-helper 17 cell**, and lists "Th17 cell" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000624` - called "CD4-positive, alpha-beta T cell", "CD4⁺ T cell"
- `CL:0000815` - called "regulatory T cell", "Treg"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.