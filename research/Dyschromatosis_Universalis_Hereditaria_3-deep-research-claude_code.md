---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5
cached: false
start_time: '2026-11-18T15:00:22.928257'
end_time: '2026-11-18T15:25:25.260350'
duration_seconds: 1502.33
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Dyschromatosis Universalis Hereditaria 3
  mondo_id: MONDO:0014169
  category: Mendelian
  causal_genes: ABCB6
  omim_id: OMIM:615402
  synonyms: dyschromatosis universalis hereditaria type 3; ABCB6 dyschromatosis universalis
    hereditaria; dyschromatosis universalis hereditaria caused by mutation in ABCB6
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-5-5
  - claude-opus-5
  web_search_requests: 5
  num_turns: 28
  total_cost_usd: 3.81693576
  session_id: fdcae5d3-a7b9-4926-9165-a05746f7313e
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  tool_calls: 121
  retrieval_calls: 118
  assistant_text_blocks: 4
citation_count: 40
reference_validation:
  total_references: 50
  verified: 49
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.02
  relevance_assessed: 49
  on_topic: 25
  unresolved_references:
  - PMID:22294697
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 203
  verified: 173
  not_found: 2
  obsolete: 2
  unverifiable: 26
  confabulation_rate: 0.011
  labels_checked: 69
  labels_matching: 39
  labels_mismatched: 19
  mislabelled_terms:
  - term_id: MONDO:0014169
    reported_labels:
    - MONDO
    ontology_label: dyschromatosis universalis hereditaria 3
  - term_id: MONDO:0000736
    reported_labels:
    - Parent term (generic DUH)
    - generic DUH
    ontology_label: dyschromatosis universalis hereditaria
  - term_id: HP:0007441
    reported_labels:
    - "Generalized hyperpigmentation \u2014 if widespread"
    ontology_label: Hyperpigmented/hypopigmented macules
  - term_id: HP:0007513
    reported_labels:
    - Abnormal dermal melanin deposition
    ontology_label: Generalized hypopigmentation
  - term_id: HP:0011009
    reported_labels:
    - Chronic
    ontology_label: Acute
  - term_id: HP:0001087
    reported_labels:
    - Iris atrophy
    ontology_label: Developmental glaucoma
  - term_id: HP:0012629
    reported_labels:
    - Abnormal iris morphology
    ontology_label: Phakodonesis
  - term_id: HP:0007906
    reported_labels:
    - Iris coloboma
    ontology_label: Ocular hypertension
  - term_id: NCIT:C15431
    reported_labels:
    - Supportive Care
    ontology_label: Hematopoietic Cell Transplantation
  - term_id: NCIT:C15688
    reported_labels:
    - Phototherapy
    - Ultraviolet B Phototherapy
    ontology_label: Maintenance Therapy
  - term_id: NCIT:C15632
    reported_labels:
    - Genetic Counseling
    ontology_label: Chemotherapy
  - term_id: NCIT:C15229
    reported_labels:
    - Watchful Waiting / observation
    ontology_label: Antitumor Drug Screening Assay
  - term_id: NCIT:C29234
    reported_labels:
    - Hydroquinone
    ontology_label: MSM/Glucosamine
  - term_id: NCIT:C92948
    reported_labels:
    - Intense Pulsed Light Therapy
    ontology_label: Rh Factor Measurement
  - term_id: NCIT:C15316
    reported_labels:
    - Psychotherapy/Psychosocial support
    ontology_label: Relaxation Therapy
  - term_id: NCIT:C19399
    reported_labels:
    - Preimplantation Genetic Diagnosis
    ontology_label: Computational Chemistry Statistics
  - term_id: NCIT:C17076
    reported_labels:
    - Prenatal Diagnosis
    ontology_label: Prolactin Receptor
  - term_id: MP:0004362
    reported_labels:
    - abnormal auditory brainstem response
    ontology_label: cochlear hair cell degeneration
  - term_id: MP:0006325
    reported_labels:
    - increased or absent threshold for auditory brainstem response
    ontology_label: impaired hearing
  labels_variant: 11
  unresolved_terms:
  - HP:0008553
  - NCIT:C168003
  obsolete_terms:
  - term_id: CL:0002331
    ontology_label: CL_0002331
    replaced_by: CL:1000349
  - term_id: UBERON:0002543
    ontology_label: obsolete median fin skeleton
  unresolvable_prefixes:
  - EXT_ID
  - OMIM
  - ORPHA
  - GARD
  - OMIMPS
  - Orphanet
  - SCTID
  - UMLS
  - NC_000002.11
  - RHEA
  - MGI
  - RGD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dyschromatosis Universalis Hereditaria 3
- **MONDO ID:** MONDO:0014169 (if available)
- **Causal gene(s):** ABCB6
- **OMIM:** OMIM:615402
- **Synonyms:** dyschromatosis universalis hereditaria type 3; ABCB6 dyschromatosis universalis hereditaria; dyschromatosis universalis hereditaria caused by mutation in ABCB6
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Dyschromatosis Universalis Hereditaria 3** covering all of the
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

I'll research this disease now, starting with the core identifiers and literature.

Let me pull structured data from the ontology and variant APIs directly.

## Target 1: Murthy et al. 2023 review (Int J Dermatol 62(10):1218-1227)

I got the full record from Semantic Scholar, Crossref, and Europe PMC, so I stopped there and did not try the ResearchGate or Europe PMC article alternates. The abstract is in the copyright-restricted set, so I can only quote short passages verbatim. The rest is paraphrased.

**Bibliographic details:** Europe PMC lists the authors as "Murthy AB, Palaniappan V, Karthikeyan K, Anbarasan V." Your citation omits the fourth author, Varshini Anbarasan. PMID 37634201, DOI 10.1111/ijd.16817, published online 2023-08-27.

**Abstract, paraphrased and quoted:**
- It covers three reticulate pigmentary dyschromatoses: DUH, dyschromatosis symmetrica hereditaria (reticulate acropigmentation of Dohi), and unilateral dermatomal pigmentary dermatosis.
- The disease was first described by Ichikawa and Hiraga in 1933.
- **Prevalence:** 0.3 per 100,000, with a "female preponderance." The abstract gives no numeric sex ratio.
- **Onset and course:** lesions "usually appear in infancy or early childhood and cease to progress beyond adolescence."
- **Inheritance:** DUH 1 and DUH 3 are autosomal dominant, the most common pattern. DUH 2 is autosomal recessive.
- **Genes:** "The most common gene involved in DUH is ABCB6, while the other genes include SASH 1, PER 3, and KITLG (DUH type 2)." The abstract gives no gene-by-gene frequencies, so I cannot confirm the ABCB6 vs SASH1 proportions you asked about.
- **Clinical pattern:** irregular hyperpigmented macules mixed with hypopigmented macules in a mottled pattern over the trunk and extremities. "The face is involved in 50% of individuals." Hair, nails, mucous membranes, palms, and soles are involved rarely. Other patterns include localized forms, sun-exposed localization, and unilateral involvement.
- **Systemic associations:** the authors report DUH cases with hepatocellular carcinoma, solitary keratoacanthoma, and dermoid cyst. These are their own observations, not a systematic association.
- **Diagnostics:** dermoscopy, histopathology, electron microscopy, and targeted gene sequencing.
- **Treatment:** NBUVB and lasers have been tried. "no treatment is promising." No efficacy data are given.
- **Prognosis:** the course is stable after adolescence, per the onset/course quote above.

The full text was not available to me, so I cannot report the review's tables or the body text on treatment numbers.

## Target 2: Zhong et al. 2019 (Clin Exp Dermatol 44(3):e58-e60)

Europe PMC confirms the bibliographic details: title "Atypical presentation of dyschromatosis universalis hereditaria with a novel ABCB6 mutation," PMID 30430618, DOI 10.1111/ced.13833. It is a Letter/Case Report, epub 2018-11-14. The author list matches your citation.

The record has no abstract text and no mesh or keyword detail about the variant. **I could not get the ABCB6 variant (cDNA or protein), the reason the presentation was "atypical," the lesion distribution, palm/sole or mucosal involvement, onset age, or the patient and family details.** The first REST call timed out and the retry returned only metadata. The europepmc.org article page returned HTTP 403, which is a permanent refusal, so I did not retry it.

## Target 3: Lu et al. 2014 (J Dermatol Sci 76(3):255-258), PMID 25288164

Europe PMC confirms the title "Novel missense mutations of ABCB6 in two chinese families with dyschromatosis universalis hereditaria," DOI 10.1016/j.jdermsci.2014.08.015, pages 255-258. The record has no abstract and no variant nomenclature. **I could not get the two variants.** The first call timed out and the retry returned only metadata. The record describes them as missense mutations, but it gives no c. or p. notation.

## Summary of gaps

- Variant nomenclature for both ABCB6 papers (2019 and 2014) is unavailable from these sources. Europe PMC does not index their full text, so these papers need the publisher pages (DOIs above) or institutional access.
- Sending the same URLs again would fail the same way, except the two timeouts, which were retried once already.

Final URLs read:
- https://api.semanticscholar.org/graph/v1/paper/DOI:10.1111/ijd.16817?fields=title,abstract,year,authors,venue,externalIds
- https://api.crossref.org/works/10.1111/ijd.16817
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:37634201&resultType=core&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30430618&resultType=core&format=json
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:25288164&resultType=core&format=json

Not read: https://europepmc.org/article/MED/30430618 (HTTP 403).

**Scope note / interpretation:** This report covers **MONDO:0014169 / OMIM:615402 — dyschromatosis universalis hereditaria 3 (DUH3)**, the form of DUH caused by heterozygous variants in **ABCB6**. It is deliberately *not* about DUH1 (SASH1, OMIM 127500) or DUH2 (OMIM 612715 / KITLG), although those are discussed where differential diagnosis or shared literature requires it. Several authoritative sources could not be retrieved in this session (OMIM full text, Orphanet ORPHA:241, the Int J Dermatol 2023 review full text, and per-variant gnomAD frequencies); each such gap is stated explicitly in the relevant section rather than filled from memory. Passages marked as verbatim quotes were transcribed from the retrieved page; where a source permitted only paraphrase, this is indicated.

---

# Dyschromatosis Universalis Hereditaria 3 (DUH3, *ABCB6*) — Comprehensive Disease Report

---

## 1. Disease Information

### 1.1 Overview

Dyschromatosis universalis hereditaria 3 (DUH3) is a rare, autosomal dominant pigmentary genodermatosis caused by heterozygous missense (and at least one frameshift) variants in **ABCB6** (ATP-binding cassette subfamily B member 6; the Langereis/Lan blood group gene), located at chromosome **2q35**. The cardinal feature is the early-life appearance of irregularly shaped, asymptomatic **hyperpigmented and hypopigmented macules intermixed in a mottled or reticulate pattern**, generalized over the trunk and limbs and often the face, with palms, soles, hair, nails and mucosae typically spared. The disorder is cosmetic/dermatologic rather than life-limiting; systemic involvement is uncommon but ocular abnormalities have been documented in some *ABCB6* families.

The MONDO definition is terse and gene-anchored — verbatim from the Monarch/OLS record: *"Any dyschromatosis universalis hereditaria in which the cause of the disease is a mutation in the ABCB6 gene."* ([OLS4 / MONDO](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0014169); [HPO/JAX annotation API](https://ontology.jax.org/api/network/annotation/OMIM:615402))

MedGen's definition (attributed to OMIM, summarized from Zhang et al. 2013) describes DUH as a rare autosomal dominant genodermatosis with irregularly shaped, asymptomatic hyper- and hypopigmented macules appearing in infancy or early childhood, generalized over trunk and limbs and sometimes the face, with palms and soles usually spared; hair and nail abnormalities have been reported, and some cases show dermal connective tissue, nerve tissue, or other systemic abnormalities. The entry explicitly flags genetic heterogeneity by pointing to DUH1 (OMIM 127500). ([MedGen C3809394 / UID 815724](https://www.ncbi.nlm.nih.gov/medgen/C3809394))

### 1.2 Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | **MONDO:0014169** | label: *dyschromatosis universalis hereditaria 3*; subsets `gard_rare`, `rare`; no children; single parent MONDO:0000736 |
| **OMIM** | **615402** (DUH3, phenotype) | gene entry: **OMIM 605452** (*ABCB6*) |
| **UMLS CUI** | C3809394 | |
| **MedGen UID** | 815724 | |
| **GARD** | GARD:0015959 (DUH3); GARD:0001996 (parent DUH) | |
| **MalaCards** | `dyschromatosis_universalis_hereditaria_3` | listed as curated-content resource in MONDO |
| **Parent term (generic DUH)** | **MONDO:0000736** | xrefs: DOID:0060304, GARD:0001996, MEDGEN:419691, **MESH:C535730**, NCIT:C173131, **OMIMPS:127500**, **Orphanet:241**, **SCTID:239082002**, UMLS:C2930995, icd11.foundation:480710406 |
| **KEGG DISEASE** | **H02350** (Dyschromatosis universalis hereditaria) | BRITE: ICD-11 ch. 14 → Genetic or developmental disorders affecting the skin → **EC23** Genetic disorders of skin pigmentation; "Other DBs": ICD-11 **EC23.Y**, MeSH **C535730**, OMIM 127500 + 615402 ([KEGG H02350](https://www.kegg.jp/entry/H02350)) |
| **Gene** | *ABCB6*, **HGNC:47**, NCBI Gene **10058**, Ensembl **ENSG00000115657**, UniProt **Q9NP58** | |

**Important ontology caveat for knowledge-base curation:** MONDO:0014169 itself carries **no Orphanet, MeSH, ICD-10, ICD-11, SNOMED CT or DOID cross-reference**. Those codes exist only on the *parent* term MONDO:0000736 (generic DUH) — i.e., ORPHA:241, MeSH C535730, SNOMED CT 239082002, DOID:0060304, ICD-11 foundation 480710406 / EC23.Y. DUH3 is a gene-defined child of a clinically defined parent, and no coding system below MONDO distinguishes the *ABCB6* subtype. An **ICD-10 code specific to DUH could not be confirmed** in this session (L81.x was not verifiable from a retrieved source).

### 1.3 Synonyms and alternative names

From MONDO (typed synonyms):
- **Exact:** `ABCB6 dyschromatosis universalis hereditaria`; `dyschromatosis universalis hereditaria 3` (xref OMIM:615402); `dyschromatosis universalis hereditaria caused by mutation in ABCB6`
- **Related (abbreviation):** `DUH3`
- Also present in the flattened synonym array: `dyschromatosis universalis hereditaria type 3`
- Parent-level synonyms (generic DUH): `DUH` (abbreviation), `dyschromatosis universalis`, and GARD's "other names" `duh; dyschromatosis universalis`
- Historical/eponymous: the entity derives from the 1933 description by **Ichikawa and Hiraga** (per Murthy et al. 2023); the broader family is termed **reticulate pigmentary dyschromatoses**

### 1.4 Nature of the evidence base

**DUH3 knowledge is derived almost entirely from aggregated disease-level resources built on individual case reports and small multiplex family studies — not from EHR, registry, or population cohorts.** The entire published *ABCB6*-DUH literature comprises roughly **seven primary genetic reports** (Zhang 2013; Cui 2013; Liu 2014; Lu 2014; Liu JW 2016; Zhong 2019; Aldokhayel 2021/22), plus mechanistic cell-biology and structural papers that used DUH variants as reagents. HPO's annotation of OMIM:615402 rests on a **single source publication (PMID:23519333)**. There are no natural-history studies, no patient registries, no quality-of-life instruments applied to this disease, and no clinical trials. Every quantitative claim below should be read as case-series-derived.

---

## 2. Etiology

### 2.1 Primary causal factor

DUH3 is a **monogenic (Mendelian) disorder** caused by heterozygous germline variants in *ABCB6*. There is no infectious, environmental, or acquired component to disease causation. Three independent groups established the gene association within ~12 months:

1. **Zhang C, Li D, Zhang J, et al.** "Mutations in ABCB6 cause dyschromatosis universalis hereditaria." *J Invest Dermatol* 2013 Sep;133(9):2221–8. doi:10.1038/jid.2013.145. **PMID 23519333**. Linkage in a five-generation Chinese DUH family mapped to **2q33.3–q36.1**; exome sequencing identified a co-segregating *ABCB6* missense variant (**p.Leu356Pro**), with two further missense variants in sporadic patients (**p.Ser170Gly**, **p.Gly579Glu**). Wild-type ABCB6 localized to endosome-like compartments (and dendrite tips in B16 mouse melanoma cells), whereas the disease variants were **retained in the Golgi apparatus**. This is the sole source publication underlying the HPO annotation of OMIM:615402.
2. **Cui YX, Xia XY, Zhou Y, et al.** "Novel mutations of ABCB6 associated with autosomal dominant dyschromatosis universalis hereditaria." *PLoS One* 2013 Nov 5;8(11):e79808. doi:10.1371/journal.pone.0079808. **PMID 24224009 / PMC3818219**.
3. **Liu H, Li Y, Hung KKH, et al.** "Genome-wide linkage, exome sequencing and functional analyses identify ABCB6 as the pathogenic gene of dyschromatosis universalis hereditaria." *PLoS One* 2014 Feb 3;9(2):e87250. doi:10.1371/journal.pone.0087250. **PMID 24498303 / PMC3911924**.

### 2.2 Genetic risk factors

- **Causal variants:** heterozygous *ABCB6* variants (full catalogue in §4.2). Inheritance is **autosomal dominant** (HP:0000006), consistent with **dominant-negative** action for at least some alleles (see §6).
- **Family history** is the dominant risk determinant: an affected parent confers a 50% transmission risk per pregnancy.
- **De novo / sporadic cases** occur: Cui et al. screened three unrelated sporadic patients and found a frameshift (**c.459delC**) in one; Zhang et al. found variants in 2 of 6 sporadic patients. Liu et al. found no *ABCB6* variant in their two sporadic cases.
- **No susceptibility loci, modifier genes, or GWAS signals** have been reported for DUH3. No GWAS Catalog entry for this phenotype was identified.
- **Locus heterogeneity within DUH (not modifiers of DUH3):** *SASH1* (DUH1), a chromosome 12q21–q23 recessive locus (Stuhrmann et al., *Clin Genet* 2008, **PMID 18462451**), *KITLG* (assigned to DUH type 2 by Murthy et al. 2023), and *PER3* (Chen et al. 2023). Murthy et al. (2023) state verbatim: *"The most common gene involved in DUH is ABCB6, while the other genes include SASH 1, PER 3, and KITLG (DUH type 2)."*

### 2.3 Environmental risk factors

**No environmental, occupational, toxic, dietary, or infectious risk factor has been identified or proposed for DUH3.** Sex, age, and ethnicity are discussed under §9. The disease is fully determined by genotype; the only reported environmental *modulator* of the phenotype (not of disease occurrence) is ultraviolet light — Cui et al. reported that macules in their family **darkened with sun exposure**, and Cao et al. (2021) argue that apparent genotype–phenotype differences in DUH reflect "skin colour, age and UV exposure" rather than genotype alone.

### 2.4 Protective factors

- **Genetic protective factors:** none identified. Notably, *ABCB6* **complete loss of function is not protective but is also not causal** — individuals homozygous or compound heterozygous for *ABCB6* null alleles constitute the **Lan-negative (Langereis-null) blood group phenotype** and are clinically healthy. Helias V, Saison C, Ballif BA, et al., "ABCB6 is dispensable for erythropoiesis and specifies the new blood group system Langereis," *Nat Genet* 2012 Jan 15;44(2):170–3, doi:10.1038/ng.1069, **PMID 22246506 / PMC3664204**, reported **ten different null mutations in 12 Lan-negative individuals with no noted clinical consequences**. This is a critical mechanistic constraint: simple haploinsufficiency is unlikely to explain dominant DUH3 (see §6).
- **Environmental protective factors:** none established. **Photoprotection is plausibly cosmetically beneficial** (reducing contrast by limiting tanning of hyperpigmented macules) but **no retrieved source demonstrates efficacy**; this is inference, not evidence.

### 2.5 Gene–environment interactions

No formal GxE study exists. The only documented interaction is **UV-dependent accentuation of lesional contrast** (Cui et al. 2013). The Chen et al. 2023 *PER3* work (**PMID 36790533**, *J Mol Med (Berl)* 2023;101(3):279–294, doi:10.1007/s00109-023-02288-6) describes a **gene–gene** interaction in a non-*ABCB6* DUH family — a *PER3* c.517C>T (p.P173S; rs772027021) variant plus a *SASH1* c.1574C>G (p.T525R) variant acting cooperatively to promote hyperpigmentation — which is mechanistically interesting (circadian gene × pigmentation) but **does not involve ABCB6** and should not be annotated to DUH3.

---

## 3. Phenotypes

### 3.1 Formally annotated HPO terms (OMIM:615402)

The HPO annotation set for DUH3 is minimal — **four terms, all from a single source (PMID:23519333), with no frequency or sex data** ([ontology.jax.org API](https://ontology.jax.org/api/network/annotation/OMIM:615402)):

| HP ID | Term | Category | Onset qualifier | Frequency |
|---|---|---|---|---|
| **HP:0001034** | Hypermelanotic macule | Skin, Hair, and Nails | HP:0011463 (Childhood onset) | not stated |
| **HP:0020073** | Hypopigmented macule | Skin, Hair, and Nails | HP:0011463 (Childhood onset) | not stated |
| **HP:0011463** | Childhood onset | Clinical course | — | — |
| **HP:0000006** | Autosomal dominant inheritance | Inheritance | — | — |

MedGen lists the same two cutaneous features (Hypermelanotic macule, MedGen UID 375013 / C1842774; Hypopigmented macule, MedGen UID 760487 / C2047793), both under "Abnormality of the integument."

GARD's HPO-sourced symptom list for the *parent* term (generic DUH, not DUH3-specific) is broader: flat discolored skin area (macule); freckling; **hearing impairment**; hyperpigmented spots; multiple café-au-lait spots; patchy hypopigmentation; hypopigmented skin patches; **photosensitive skin**; and, as uncommon, **short stature**. ([GARD 1996](https://rarediseases.info.nih.gov/diseases/1996/dyschromatosis-universalis-hereditaria))

### 3.2 Phenotype detail, by feature

#### (a) Mottled hyper- and hypopigmented macules — the defining phenotype
- **Type:** physical manifestation / clinical sign (visible dyspigmentation)
- **Suggested HPO:** HP:0001034 (Hypermelanotic macule); HP:0020073 (Hypopigmented macule); HP:0007441 (Generalized hyperpigmentation — if widespread); HP:0001000 (Abnormality of skin pigmentation, parent); HP:0007441/HP:0011121 as applicable; HP:0007513 (Abnormal dermal melanin deposition) for histologic correlate
- **Morphology:** macules **3–7 mm in diameter** (Cui et al. 2013); hyperpigmented lesions dark brown, hypopigmented lesions light brown to white; "mottled," "reticulate" or "reticular" arrangement. Cao et al. (2021), summarizing Wu et al., describe the *ABCB6*-associated presentation verbatim as *"generalized mottled hyperpigmented macules mixed with hypopigmented macules arranged in a reticular pattern"* — and add that *SASH1*-related disease is more often confused with generalized lentiginosis.
- **Distribution:** generalized — trunk and extremities predominantly. Cui et al.'s proband had macules *"scattered over the entire body including the hands, feet, back, face, and scalp."* Murthy et al. 2023 state verbatim that **"The face is involved in 50% of individuals,"** and that hair, nails, mucous membranes, palms and soles are involved only rarely.
- **Palms/soles:** characteristically **spared**. Cui et al.: palms, soles, mucous membranes, teeth, nails and hair all appeared normal. Aldokhayel et al.: palms and soles normal in both patients; hair, nails and mucosa uninvolved.
- **Laterality:** **bilateral and symmetric** (Aldokhayel et al. describe "diffuse, symmetric hyper- and hypopigmented mottled macules"). Unilateral/dermatomal forms exist within the reticulate dyschromatosis family (unilateral dermatomal pigmentary dermatosis) but are a separate entity.
- **Age of onset:** infancy to early childhood. Murthy et al. 2023, verbatim: lesions *"usually appear in infancy or early childhood and cease to progress beyond adolescence."* Cui et al.'s proband reported macules appearing **within 2 months after birth**; the Saudi mother's lesions began in childhood on the chest; her son's began **within the first 3 years of life** on the inner thighs. Cao et al.'s (SASH1) proband began at age 4. HPO onset term: **HP:0011463 (Childhood onset)**; **HP:0003593 (Infantile onset)** is also supportable; **HP:0003577 (Congenital onset)** is not generally appropriate.
- **Severity:** cosmetic; **mild to moderate** in medical terms, but potentially high psychosocial burden (see §3.3). Highly variable extent between individuals.
- **Progression:** progressive spread during childhood (chest → trunk → whole body including face in the Saudi mother; inner thighs → trunk → forehead in her son), then **stable/plateau after adolescence**. Aldokhayel et al. describe the course verbatim as *"neither progression nor spontaneous regression with age."* HPO course terms: **HP:0003680 (Nonprogressive)** post-adolescence; **HP:0011009 (Chronic)**.
- **Frequency among affected individuals:** **100%** — it is the diagnostic criterion.
- **Symptoms:** **asymptomatic** — no pruritus, pain, or abnormal sensation reported (Cui et al. explicitly: macules darkened with sun exposure "with no abnormal sensations"). HPO: **HP:0000951 (Abnormality of the skin)** parent; absence of pruritus is noteworthy for differential diagnosis.

#### (b) Ocular abnormalities
- **Type:** clinical sign / physical examination finding
- **Evidence:** Liu et al. 2014 performed ophthalmological examination of *ABCB6* variant carriers and found: in Family 1, individuals **II-5 and III-4 had abnormal pitting of the iris**, and **IV-4 had raised intraocular pressure (L 24 mmHg, R 19 mmHg)**. **No microphthalmia or anophthalmia** was observed. Family 2 individual IV-1 had no eye abnormality. The authors concluded their findings reveal *"the shared pathogenic mechanism between pigmentary DUH and ocular coloboma."*
- **Suggested HPO:** HP:0000593 (Abnormality of the iris) / HP:0001087 (Iris atrophy) or HP:0012629 (Abnormal iris morphology); HP:0007906 (Iris coloboma) — for the related MCOPCB7 phenotype; HP:0007906; HP:0012632 (Abnormal intraocular pressure) / HP:0007906; HP:0040194 (Increased intraocular pressure); HP:0000589 (Coloboma) for the allelic disorder.
- **Frequency:** low and uncertain — observed in a minority of examined carriers in one family; **not** reported in the Zhang, Cui, Lu, or Aldokhayel cohorts. Cui et al. explicitly state no affected family member had **ocular coloboma**.
- **Progression/severity:** not characterized.

#### (c) Hearing impairment
- **Type:** functional/laboratory abnormality (audiometric)
- **Evidence:** "High-tone deafness" is listed by Liu et al. 2014 among features occasionally reported in DUH generally. GARD lists hearing impairment as a common HPO-derived symptom of the parent DUH term. **No audiometric data from a genotyped DUH3 patient was retrieved.** However, the biological plausibility is now substantially strengthened by Baril et al. 2024 (see §6, §15): Abcb6-knockout mice show **increased ABR thresholds at all tested frequencies**, and zebrafish *abcb6a* knockdown reduces inner-ear hair cells and abolishes the utricular otolith.
- **Suggested HPO:** HP:0000365 (Hearing impairment); HP:0008553 (High-frequency hearing impairment / HP:0008596 High-frequency sensorineural hearing impairment).
- **Frequency:** rare/uncertain in *ABCB6*-DUH specifically. **This should be curated as a plausible, mechanistically supported but clinically unconfirmed DUH3 feature.**

#### (d) Other features reported in DUH (not specifically validated for ABCB6-DUH3)
Liu et al. 2014 (Introduction) list occasionally reported DUH features: **high-tone deafness, ocular abnormalities, photosensitivity, learning difficulties, epilepsy, diabetes, and small stature**. Murthy et al. 2023 report their own observations of DUH co-occurring with **hepatocellular carcinoma, solitary keratoacanthoma, and dermoid cyst** — these are authors' observations, not established associations. A case report describes DUH with **primary ovarian failure** (Jayanthi NS et al., *J Clin Diagn Res* 2016, **PMID 27134983**), genotype not established as *ABCB6*.

Suggested HPO for these (annotate with low confidence / "parent-term DUH" provenance): HP:0000365 (Hearing impairment); HP:0000989 (Pruritus — N/A, excluded); HP:0000988/HP:0000951; HP:0000958; HP:0001250 (Seizure); HP:0001263/HP:0001328 (Specific learning disability); HP:0000819 (Diabetes mellitus); HP:0004322 (Short stature); HP:0000957 (Café-au-lait spot); HP:0001480 (Freckling); HP:0000992 (Cutaneous photosensitivity).

**Explicitly negative / excluded features in ABCB6-DUH3 (useful for curation as NOT-annotations):** no skin cancer, no ocular coloboma in the Cui family; no palmoplantar involvement; no mucosal involvement; no hair or nail abnormality in the Cui and Aldokhayel families (although MedGen's OMIM-derived definition notes hair/nail abnormalities "have been reported" in DUH broadly); normal pregnancy/perinatal history; no intellectual disability reported in the genotyped families.

### 3.3 Quality-of-life impact

**No disease-specific or generic QoL instrument (DLQI, EQ-5D, SF-36, PROMIS, Skindex) has been applied to DUH or DUH3 in any retrieved publication.** This is a genuine evidence gap.

What can be said from retrieved sources:
- The cutaneous lesions are **asymptomatic** — there is no pain, pruritus, or functional impairment of the skin barrier reported.
- The burden is therefore **entirely cosmetic and psychosocial**, and is amplified by the **high rate of facial involvement (50% per Murthy et al. 2023)** and generalized distribution, and by onset in early childhood (affecting body image through formative years).
- Patients actively seek treatment and accept laser therapy: in the Yuan et al. 2025 case, the patient underwent IPL and then picosecond laser, and **discontinued further sessions because of cost** — a documented access/affordability barrier (Skin Health Dis 2025, DOI 10.1093/skinhd/vzaf024, [PMC12202865](https://pmc.ncbi.nlm.nih.gov/articles/PMC12202865)).
- Per-phenotype QoL mapping is not possible from the literature.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

| Field | Value |
|---|---|
| **Gene symbol** | *ABCB6* |
| **Official full name** | ATP binding cassette subfamily B member 6 (LAN blood group) |
| **HGNC** | HGNC:47 |
| **NCBI Gene ID** | 10058 |
| **Ensembl** | ENSG00000115657 |
| **UniProt** | Q9NP58 (ABCB6_HUMAN), reviewed/Swiss-Prot |
| **OMIM (gene)** | 605452 |
| **Cytoband** | 2q35 |
| **GRCh38 coordinates** | NC_000002.12: **chr2:219,209,771–219,218,957**, **minus strand**, **19 exons** (NCBI Gene esummary). Alliance/HGNC gives 219,209,765–219,219,012. gnomAD GraphQL returned chr2:219,209,772–219,218,994, strand "−". GRCh37: NC_000002.11:220,074,493–220,083,679 |
| **MANE Select transcript** | NM_005689.4 (used by all ClinVar records) |
| **Protein** | 842 aa, 93,886 Da |
| **Aliases** | ABC, LAN, MTABC3, PRP, umat |

**RefSeq gene summary (verbatim, NCBI Gene, Mar 2017):** *"This gene encodes a member of the ATP-binding cassette (ABC) transporter superfamily. ABC proteins transport various molecules across extra- and intra-cellular membranes. This protein is a member of the heavy metal importer subfamily and plays a role in porphyrin transport. This gene is the molecular basis of the Langereis (Lan) blood group antigen and mutations in this gene underlie familial pseudohyperkalemia and dyschromatosis universalis hereditaria."*

**Protein architecture (UniProt Q9NP58):** homodimer; two independently folding units — an **N-terminal transmembrane domain (TMD0, residues 1–205)** mediating lysosomal targeting, and an **ABC-core domain (residues 206–842)** carrying ATPase activity. ABC transmembrane type-1 domain 265–556 (PRU00441); ABC transporter (nucleotide-binding) domain 590–824 (PRU00434). ATP-binding sites at residue 599 and 623–634. **Eleven predicted transmembrane helices**: 27–47, 73–93, 107–127, 148–168, 186–206, 264–284, 292–312, 376–396, 398–418, 500–520, 530–550. N-linked glycosylation at Asn6; disulfide bond Cys8–Cys26. N-terminus (1–26) lumenal; C-terminal region (551–842) cytoplasmic. ABCB6 is a **"half-transporter"** that functions as a homodimer.

**Allelic disorders at this locus** (important for variant interpretation and differential annotation):
- **Microphthalmia, isolated, with coloboma 7 (MCOPCB7)** — UniProt DI-03384, **OMIM 614497**, MONDO:0013783, Orphanet 98938
- **Dyschromatosis universalis hereditaria 3 (DUH3)** — UniProt DI-03880, **OMIM 615402**
- **Familial pseudohyperkalemia 2, due to red cell leak (PSHK2)** — UniProt DI-04131, **OMIM 609153**, MONDO:0012204, Orphanet 90044
- **Langereis (Lan) blood group** — OMIM 111600; a polymorphism, clinically silent except in transfusion/pregnancy contexts
- **Porphyria severity modification** — UniProt notes ABCB6 "may be the cause of a severe porphyria" (PubMed 27507172)

### 4.2 Pathogenic variants in DUH3

Cao et al. 2021 (*BMC Med Genomics* 14:168, doi:10.1186/s12920-021-01014-w, **PMID 34174894 / PMC8236144**) state verbatim: **"To date, nine mutations have been discovered in ABCB6 associated with DUH."** Baril et al. 2024 subsequently refer to **ten** reported DUH variants and make one important nomenclature correction.

**Complete catalogue of reported *ABCB6* DUH variants:**

| cDNA (NM_005689.4) | Protein | Exon | Variant class | Reported by | ClinVar |
|---|---|---|---|---|---|
| c.508A>G | p.Ser170Gly | exon 1 (per search summary) | missense | Zhang 2013 (PMID 23519333), sporadic case | **VCV000064647.2 — Pathogenic** (2013-09-01, no assertion criteria, 0★), rs397514757; OMIM 605452.00xx |
| c.964A>C | p.Ser322Lys *(corrected to* **p.Ser322Arg** *by Baril 2024)* | exon 4 | missense | Liu 2014 (PMID 24498303), Family 2 | rs1574815954 (UniProt lists 322 S→R) |
| c.1067T>C | **p.Leu356Pro** | exon 3 (per search summary) | missense | Zhang 2013, 5-generation family | **VCV000064646.1 — Pathogenic** (2013-09-01, 0★), rs397514756 |
| c.1144G>A | p.Gly382Arg | exon 5 | missense | Aldokhayel 2021/22 (PMID 35024399), Saudi family | not in the retrieved ClinVar set |
| c.1270T>C | p.Tyr424His | — | missense | catalogued by Cao 2021; a **recurrent** *ABCB6* c.1270T>C was reported by Liu JW 2016 (PMID 26712430) | not in the retrieved ClinVar set |
| c.1358C>T | p.Ala453Val | exon 7 | missense | Liu 2014, Family 1 | not in the retrieved ClinVar set |
| c.1663C>A | p.Gln555Lys | exon 11 | missense | Cui 2013 (PMID 24224009), 4-generation Shandong family | **VCV000208249.2 — Pathogenic** (2013-01-01, 0★), rs796065353, OMIM 605452.0011 |
| c.1736G>A | p.Gly579Glu | exon 12 (per search summary) | missense | Zhang 2013, sporadic case | **VCV000064648.1 — Pathogenic** (2013-09-01, 0★), rs397514758 |
| c.2017A>G | p.Thr673Ala | — | missense | catalogued by Cao 2021 | not in the retrieved ClinVar set |
| **c.459delC** | **p.Trp154Glyfs\*96** | exon 1 | **frameshift deletion** | Cui 2013, sporadic case | **VCV001686417.2 — Uncertain significance** (2025-04-18, 2★, multiple submitters no conflicts), rs755723161 |

Additionally, **p.Asn467Ser (p.N467S)** in *ABCB6* was reported in a case of **xeroderma pigmentosum group C with DUH-like pigmentation** (cited as ref. 26 in Cao et al. 2021); it is **not counted** among the nine/ten canonical DUH variants.

**Variant class summary:** **9/10 missense, 1/10 frameshift.** No nonsense, canonical splice-site, or structural/copy-number variant has been reported in DUH3. All are **heterozygous germline**; **no somatic origin** is implicated (UniProt notes one unrelated somatic ABCB6 variant, p.Arg69Gly, in a breast cancer sample — irrelevant to DUH).

**Clustering:** The DUH variants cluster in the **ABC transmembrane domain**. Liu et al. 2014 noted that both of their variants lie in the ABC transmembrane domain, whereas the coloboma variant p.Leu811Val lies in the transporter-like (nucleotide-binding) domain and p.Ala57Thr lies outside both — a **genotype–domain correlation distinguishing DUH3 from MCOPCB7**. Baril et al. 2024 add structural placement: **S170G is in TMD0**; **S322R is in the "TM7 bulge loop" (residues 318–324)**; **L356P is in/adjacent to a coupling helix**. All affected residues are highly conserved across species (Cui et al.: Gln555 conserved across species; Liu et al.: both their residues "highly conserved").

**Non-DUH ABCB6 disease variants (for differential annotation; UniProt feature table, verbatim positions):** 57 A→T (rs387906911, MCOPCB7, "uncertain significance, hypomorphic"); 192 R→Q (decreased expression, loss of plasma-membrane expression); 276 R→W (rs57467915, porphyria severity modifier); 375 R→Q (rs754667801) and 375 R→W (rs764893806), both **PSHK2**; 492 A→T (rs147445258, porphyria modifier, impairs ATP binding, abolishes coproporphyrin III transport); 811 L→V (MCOPCB7, per Wang et al. 2012).

### 4.3 Variant classification (ACMG/AMP context)

ClinVar's record for *ABCB6* + "dyschromatosis" returned **16 variation records** (esearch count = 16). Classification status:

- **Pathogenic (4):** c.508A>G (p.Ser170Gly), c.1067T>C (p.Leu356Pro), c.1663C>A (p.Gln555Lys), c.1736G>A (p.Gly579Glu) — **all four have review status "no assertion criteria provided" (0 stars)**, i.e. legacy literature-derived submissions that have *not* been re-assessed under ACMG/AMP 2015 criteria.
- **Likely pathogenic (1):** c.1452+2T>A (splice donor), 1★, rs201100181 — condition DUH3; this canonical splice-donor variant is **not** among the published DUH case variants.
- **Uncertain significance (7):** c.1864-4A>G; c.2359A>G (p.Thr787Ala); c.192G>C (p.Trp64Cys); c.2029A>T (p.Asn677Tyr); c.659A>T (p.Glu220Val); c.1694T>C (p.Phe565Ser); **c.459del (p.Trp154fs)** — note the published Cui frameshift sits here at VUS.
- **Conflicting classifications (3):** c.1511T>C (p.Val504Ala); c.1361T>C (p.Val454Ala); c.1123C>T (p.Arg375Trp — the PSHK2 allele).
- **Benign/Likely benign (1):** c.688-9C>T, 2★.

**Curation implication:** DUH3 has **no ClinGen Variant Curation Expert Panel**, no gene-disease validity classification retrieved, and the four "Pathogenic" calls carry zero stars. Several of the published DUH variants (p.Gly382Arg, p.Tyr424His, p.Ala453Val, p.Thr673Ala) are **absent from ClinVar entirely** in the retrieved set. ClinVar records for *ABCB6* variants are typically multi-condition, simultaneously listing DUH3, MCOPCB7, familial pseudohyperkalemia, and the Langereis blood group — reflecting panel-based reporting rather than phenotype-specific curation.

### 4.4 Population allele frequencies

**Gene-level constraint (gnomAD v4, GraphQL API, ENSG00000115657):**

| Metric | Value |
|---|---|
| **pLI** | **4.49 × 10⁻²⁶** (essentially zero) |
| **LOEUF (o/e LoF upper CI)** | **1.046** (lower CI 0.736) |
| o/e LoF (point) | 0.875 |
| Observed LoF | 87 |
| Expected LoF | 99.41 |
| o/e missense | 0.956 |
| Missense Z | 0.616 |
| o/e synonymous | 1.077 |

**Interpretation — this is one of the most important facts for mechanistic reasoning about DUH3.** *ABCB6* is **completely unconstrained for loss of function** (pLI ≈ 0, LOEUF ≈ 1.05, 87 observed LoF alleles vs 99.4 expected) and **unconstrained for missense** (missense Z 0.62, o/e 0.96). This is entirely concordant with the Lan-negative literature (Helias et al. 2012, PMID 22246506): *ABCB6*-null humans exist and are healthy. **Therefore DUH3 cannot plausibly be a haploinsufficiency disorder**, and a dominant-negative or neomorphic mechanism is required (see §6). Cui et al.'s own proposal that their frameshift might act via nonsense-mediated decay and haploinsufficiency sits uneasily with these population data and should be curated as the authors' hypothesis rather than established mechanism.

**Variant-level frequencies:** per-variant gnomAD AC/AN/AF **could not be retrieved in this session** (the gene-level variant payload exceeded the fetch limit and per-rsID Ensembl calls failed with connection resets). One targeted query was completed: **chr2-219216084-A-G (GRCh38), which corresponds to c.1067T>C / p.Leu356Pro on the minus strand, returned "Variant not found" in gnomAD v4** — i.e. this variant appears to be **absent from gnomAD v4**. For context, per-variant exome AN across the *ABCB6* region in gnomAD v4 ranges roughly **1.04 million to 1.46 million alleles**, with genome AN ≈ 152,000.

**Control-cohort evidence from the primary papers (direct, and more informative than gnomAD for East Asian populations):**
- Zhang et al. 2013: the family variant was absent from **500 geographically matched controls**.
- Cui et al. 2013: both c.1663C>A and c.459delC were absent from **455 ethnically matched normal Chinese individuals** and from dbSNP at the time.
- Liu et al. 2014: p.Ala453Val and p.Ser322Lys were absent from the **1000 Genomes Project, dbSNP, 500 exomes, and 1,516 (reported variously as 1,016 exon-specific) Chinese controls**.

### 4.5 Modifier genes

**None identified for DUH3.** No modifier-gene study has been performed. The only published multi-gene interaction in any DUH family is the *PER3* + *SASH1* digenic cooperation described by Chen et al. 2023 (PMID 36790533), which does not involve *ABCB6*.

### 4.6 Epigenetic information

**No DNA methylation, histone modification, or chromatin study of DUH3 has been published.** No ENCODE/Roadmap/DiseaseMeth entry specific to this disease was identified. This is a complete evidence gap. The one adjacent observation is that **ABCB6 mRNA levels are unchanged** in patient skin (Liu et al. 2014: qRT-PCR of skin from four carriers vs four controls, **P = 0.44**), arguing against transcriptional/epigenetic dysregulation as the proximate mechanism.

### 4.7 Chromosomal abnormalities

**None.** No aneuploidy, translocation, inversion, or copy-number variant has been reported in DUH3. Chromosomal microarray, karyotyping and FISH have no established role (see §10). The only cytogenetic-scale findings in the literature are **linkage intervals**, not abnormalities: 2q33.3–q36.1 (Zhang 2013); 2q35–q37.2, ~17 Mbp, HLOD 4.68 (Cui 2013, with a spurious secondary 6p22 peak, ~300 kbp, HLOD 4.59, containing no annotated gene); and combined two-family single-point HLOD 5.08 (p = 6.6 × 10⁻⁷) for Liu 2014.

---

## 5. Environmental Information

- **Environmental factors:** **Not applicable.** No toxin, radiation, pollutant, heavy metal, drug, or occupational exposure has been linked to DUH3 causation. No CTD/TOXNET association was identified. (Of tangential interest: ABCB6 *in vitro* confers resistance to **arsenic, cadmium, 5-fluorouracil, SN-38 and vincristine** per UniProt — so ABCB6 is a xenobiotic-handling protein, and mouse *Abcb6* knockouts show **MP:0009766 increased susceptibility to xenobiotic induced morbidity/mortality** and altered xenobiotic sensitivity — but no human DUH3 exposure interaction is documented.)
- **Lifestyle factors:** **Not applicable** to causation. **UV exposure modulates lesional contrast** (Cui et al. 2013: macules darkened with sun exposure); this is a phenotype modifier, not a risk factor.
- **Infectious agents:** **Not applicable.** DUH3 has no infectious etiology or trigger.

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain

The following chain integrates human genetics, structural biology, and melanocyte cell biology. Steps marked **[inferred]** are not directly demonstrated for DUH3 patient skin.

1. **A heterozygous missense variant arises in *ABCB6*, almost always within the ABC transmembrane domain** (p.Ser170Gly in TMD0; p.Ser322Arg in the TM7 bulge loop; p.Leu356Pro at a coupling helix; p.Gly382Arg; p.Tyr424His; p.Ala453Val; p.Gln555Lys; p.Gly579Glu; p.Thr673Ala) — **leading to** a structurally altered half-transporter subunit. *(Human genetics: PMIDs 23519333, 24224009, 24498303, 25288164, 35024399; structural placement: Baril et al. 2024, PMID 39557842)*

2. **The variant subunit misfolds and/or fails to traffic correctly, resulting in retention in the biosynthetic pathway rather than delivery to its functional compartment.** Zhang et al. 2013 showed that wild-type ABCB6 localizes to **endosome-like compartments and dendrite tips** in B16 mouse melanoma cells, while the DUH variants are **retained in the Golgi apparatus**. Baril et al. 2024 quantified reduced steady-state expression in HEK293 cells for **S170G (p = 0.020), S322R (p < 0.0001), and L356P (p < 0.0001)**, and showed that the chemical chaperone **4-PBA increased L356P expression (p = 0.00262)** while MG132 and chloroquine did not — consistent with a folding/trafficking defect rather than accelerated proteasomal or lysosomal degradation. UniProt annotates p.Ser170Gly and p.Leu356Pro explicitly as "**retained in Golgi**."

3. **For at least one allele (L356P), the misfolded subunit is also catalytically dead, and — because ABCB6 functions as a homodimer — it poisons the wild-type partner, producing a dominant-negative effect.** Baril et al. 2024: L356P showed **no detectable ATP-agarose binding (p = 0.0004)** and **negligible ATPase activity, comparable to the catalytically dead E752Q mutant**; a thermal-shift assay gave **Tm 57.8 °C for L356P vs 42.5 °C for wild type (+15.3 °C)**, with AMP-PNP producing only minor further stabilization, indicating poor nucleotide interaction; molecular dynamics (triplicate 500 ns) showed loss of the L356(NH)–His352(O) backbone hydrogen bond present in **55%/63%** of wild-type simulation frames, with loss of helical character and truncation of the coupling helix; the L356P loop **occludes the nucleotide site and clashes with modeled ATP**. The authors conclude a WT/L356P heterodimer is "highly likely" nonfunctional and that L356P **"likely acts as dominant-negative-allele."** Liu et al. 2014 reached the same conclusion from different evidence: patient-skin ABCB6 **mRNA was unchanged (P = 0.44)** and protein expression by IHC was not significantly different from control, so their transmembrane-domain missense variants "more likely influence the subcellular location" of ABCB6 and act through a **dominant-negative effect**.
   - **Branch — the one frameshift allele:** Cui et al.'s c.459delC (p.Trp154Glyfs\*96) cannot act by dominant negative if it undergoes nonsense-mediated decay; the authors proposed NMD and **haploinsufficiency**, and suggested both their alleles are **hypomorphic**. **[inferred, and in tension with population data]** — gnomAD shows *ABCB6* is entirely LoF-unconstrained (pLI ≈ 0, LOEUF 1.05, 87 observed LoF alleles), and Lan-negative humans homozygous for null alleles are healthy (PMID 22246506). ClinVar currently classifies c.459del as **Uncertain significance**. This branch therefore remains unresolved and should be curated as such.

4. **Loss of functional ABCB6 at the melanosome membrane disrupts the earliest stages of melanosome biogenesis — specifically, PMEL amyloid fibril matrix formation in stage I/II melanosomes.** Bergam P, Reisecker JM, Rakvács Z, Kucsma N, Raposo G, Szakacs G, van Niel G, "ABCB6 Resides in Melanosomes and Regulates Early Steps of Melanogenesis Required for PMEL Amyloid Matrix Formation," *J Mol Biol* 2018 Oct 12;430(20):3802–3818, doi:10.1016/j.jmb.2018.06.033, **PMID 29940187**, showed in the human melanocytic line **MNT-1** that ABCB6 localizes to the **membrane of early melanosomes and of lysosomes**; **siRNA depletion of ABCB6 impaired PMEL amyloidogenesis in early melanosomes** and caused **aberrant multilamellar aggregates to accumulate in pigmented melanosomes**. Critically, **wild-type ABCB6 overexpression restored PMEL fibril formation and normal melanosome maturation, whereas the catalytically inactive K629M mutant and the DUH variant G579E did not** — directly tying **transporter catalytic activity** to melanogenesis and tying the **DUH allele specifically** to the defect. UniProt records this as ABCB6 "may have a role in early melanogenesis, producing PMEL amyloid fibrils," and lists **melanosome membrane (SL-0160)** among its locations.

5. **Failure of the PMEL amyloid scaffold leads to melanosomes that cannot mature normally and cannot deposit melanin onto an ordered matrix — resulting in a population of immature, under-pigmented melanosomes within melanocytes that are present in normal numbers.** This is the key human-tissue observation. Cui et al. 2013 performed methylene-blue light microscopy and electron microscopy on hyper- and hypopigmented macules: **basal melanocytes were present in normal numbers and morphologically intact in both lesion types**; hyperpigmented macules had melanosome content similar to control; **hypopigmented macules had less mature melanosome content than control, with "empty immature melanosomes" in hypopigmented melanocytes**. The authors concluded verbatim that DUH *"might be a disorder of melanosome maturing, rather than a disorder of melanocyte number."* Aldokhayel et al. 2021/22 corroborated at the light-microscopic level: hyperpigmented macules showed **increased basal-layer melanin with melanophages**, hypopigmented macules **decreased basal-layer melanin**, both with mild perivascular lymphocytic infiltrate and occasional melanophages; melanosome numbers are reduced in hypopigmented lesions. Bergam et al.'s *Abcb6*-knockout mouse **retinal pigment epithelium showed a significant decrease in melanosome numbers**, independently supporting the same step.

6. **Mosaic, stochastic variation in the severity of this melanosome-maturation defect across clonal melanocyte populations in the skin produces the characteristic intermixed hyper- and hypopigmented macules — rather than uniform hypopigmentation. [inferred]** No retrieved source directly demonstrates the clonal/mosaic basis of the mottled pattern; this is the standard interpretation of the reticulate dyschromatoses and should be curated as hypothesis. ABCB6 is expressed in melanocytes but **not in basal keratinocytes** (Liu et al. 2014 IHC, patient and control skin; Cui et al. 2013: *"Melanocytes showed positive immunoreactivity to ABCB6."*) — confining the primary cellular lesion to the melanocyte.

7. **Melanin transfer to keratinocytes is correspondingly reduced or increased focally, yielding the clinically visible macules; UV exposure accentuates the contrast** (Cui et al. 2013), **completing the chain from mutation to clinical manifestation.**

8. **Parallel branch — ocular:** The same ABCB6 dysfunction in the **retinal pigment epithelium and developing eye** produces iris and intraocular-pressure abnormalities in some carriers (Liu et al. 2014) and, for a distinct set of alleles in the nucleotide-binding/transporter-like domain (p.Leu811Val) or outside both domains (p.Ala57Thr), the allelic disorder **ocular coloboma (MCOPCB7)**. Wang L, He F, et al., "ABCB6 mutations cause ocular coloboma," *Am J Hum Genet* 2012;90(1):40–48, **PMID 22226084 / PMC3257322**, mapped p.Leu811Val in a three-generation Chinese autosomal-dominant coloboma family (7 affected, 6 unaffected, **LOD 3.2 at θ = 0**) and found p.Ala57Thr in **3 of 116 sporadic cases**; Myc-tagged ABCB6 localized to **ER and Golgi in RPE cells**; **zebrafish morpholino knockdown produced a coloboma-like phenotype rescued by wild-type but not mutant ABCB6 mRNA**. Liu et al. 2014 explicitly framed their ocular findings as revealing *"the shared pathogenic mechanism between pigmentary DUH and ocular coloboma."*

9. **Parallel branch — inner ear [emerging]:** Baril et al. 2024 (*Nat Commun* 15:9885, doi:10.1038/s41467-024-53663-x, **PMID 39557842 / PMC11574312**) showed **zebrafish *abcb6a* is expressed in the otic vesicle at 3 dpf**; splice-blocking morpholino MO15 reduced hair cells per neuromast (two-way ANOVA genotype effect **F(1,111) = 126.6, p < 0.0001**; p53-independent, p = 0.35 vs p53-null background), **blocked utricular otolith formation up to 14 dpf** with the saccule intact (rescued by human *ABCB6* mRNA: 52.6% wild-type, 42.1% partial, 5.3% unrescued, N = 19), and produced a vestibular behavioural deficit at 21 dpf (bottom-third occupancy **39.9% vs 1.2%, p < 0.0001**; vertical distance 160.7 vs 79.7 px, p = 0.0041). **Abcb6-knockout mice (N = 6 KO vs 5 WT, 5–6 weeks) showed increased ABR thresholds at all tested frequencies**, with cochlear RNA-seq showing increased *Zbtb20*, *Kcna10*, *Egfr* and decreased *Spag6*, *Dync1li1*. The authors conclude verbatim: *"Taken together, these data suggest that Abcb6 is required for normal inner ear development in zebrafish."* This provides a mechanistic substrate for the long-reported but poorly documented **high-tone deafness** in DUH.

10. **Parallel branch — erythroid/porphyrin (DUH-irrelevant but mechanistically foundational):** ABCB6's originally described role is porphyrin transport. Krishnamurthy PC, Du G, Fukuda Y, et al., "Identification of a mammalian mitochondrial porphyrin transporter," *Nature* 2006 Oct 5;443(7111):586–9, **PMID 17006453**, reported that ABCB6 is *"uniquely located in the outer mitochondrial membrane and is required for mitochondrial porphyrin uptake"*, that porphyrin uptake then activates de novo porphyrin biosynthesis, and that the findings *"challenge previous assumptions"* about porphyrin movement and haem biosynthesis control. **However**, Helias et al. 2012 (PMID 22246506) demonstrated that **ABCB6 is dispensable for human erythropoiesis** — so this branch does not contribute to DUH3 pathology.

### 6.2 Mechanism detail by category

**Molecular pathways.** There is **no canonical signaling cascade (Wnt, MAPK, mTOR, PI3K-AKT) implicated in DUH3**. The relevant "pathway" is **melanosome biogenesis / pigment granule maturation** — a membrane-trafficking and organelle-biogenesis process rather than a signaling pathway. Upstream of this, ABCB6's biochemical activity is **ATP-dependent porphyrin/heme transport**. UniProt lists the catalytic reactions with Rhea identifiers: **heme b in→out (RHEA:19261)**, **coproporphyrin III (RHEA:66664)**, **protoporphyrin IX (RHEA:61336)**, **pheophorbide a (RHEA:61360)**, **uroporphyrin III (RHEA:66776)**. Kinetics for purified mitochondrial ABCB6: **ATP Km 0.99 mM, Vmax 492.3 nmol/min/mg; coproporphyrin III Km 11.97 µM in liposomes**. Liu et al. 2014 raised **copper homeostasis** as a candidate link, noting that **tyrosinase is a copper-dependent enzyme required for melanin synthesis** — a plausible but, in the retrieved literature, **unproven** bridge; no copper or tyrosinase assay in DUH tissue was retrieved.
  - *Suggested GO BP terms:* **GO:0048066** (developmental pigmentation) / **GO:0043473** (pigmentation); **GO:0032438** (melanosome organization); **GO:0006582** (melanin metabolic process); **GO:0042438** (melanin biosynthetic process); **GO:0015886** (heme transport); **GO:0006778/GO:0006779/GO:0033013** (porphyrin-containing compound metabolic/biosynthetic process; tetrapyrrole metabolism); **GO:0055085** (transmembrane transport); **GO:0006878/GO:0006879** (intracellular copper/iron ion homeostasis); **GO:0042168** (heme metabolic process); **GO:0035351** (heme transmembrane transport); **GO:0043588** (skin development); **GO:0098849** (cellular detoxification of cadmium ion).
  - *Suggested GO MF terms:* **GO:0015439** (ABC-type heme transporter activity); **GO:0140359** (ABC-type transporter activity); **GO:0005524** (ATP binding); **GO:0016887** (ATP hydrolysis activity); **GO:0015562** (efflux transmembrane transporter activity); **GO:0020037** (heme binding); **GO:0046906** (tetrapyrrole binding).

**Cellular processes.** Protein **folding and quality control** (ER/Golgi retention, 4-PBA-responsive); **intracellular protein transport and organelle targeting** (TMD0-mediated lysosomal targeting); **organelle (melanosome) biogenesis and maturation**; **amyloid fibril assembly** (PMEL). Notably **absent** from the mechanism: apoptosis, cell-cycle dysregulation, autophagy, and inflammation — melanocyte numbers are normal and there is no melanocyte loss (Cui et al. 2013). The only inflammatory finding is a **mild perivascular lymphocytic infiltrate** in both lesion types (Aldokhayel et al.), which is non-specific and likely incidental.
  - *Suggested GO BP terms:* **GO:0006457** (protein folding); **GO:0034976** (response to ER stress); **GO:0072657** (protein localization to membrane); **GO:1990000** (amyloid fibril formation).

**Protein dysfunction.** Mixed and allele-dependent: (i) **misfolding with Golgi/ER retention** (S170G, L356P, S322R — reduced steady-state expression, 4-PBA-rescuable); (ii) **loss of catalytic function** (L356P — no ATP binding, ATPase comparable to catalytically dead E752Q); (iii) **dominant-negative poisoning of the obligate homodimer** (inferred for L356P by Baril et al.; proposed generally by Liu et al.); (iv) **loss of a specific transport function with preserved substrate binding** — all tested mutants **including G579E bound hemin-agarose comparably to wild type**, so the defect is downstream of substrate recognition; Baril et al. explicitly caution that binding "does not necessarily correlate to hydrolysis or transport rates," and **no transport assay was performed on the DUH mutants**; (v) **possible haploinsufficiency** for the single frameshift allele (unresolved — see §6.1 step 3 branch).

**Metabolic changes.** No systemic metabolic abnormality. The relevant metabolism is **intracellular porphyrin/heme and possibly copper handling** within the melanocyte. **CHEBI terms:** heme b (CHEBI:60344 / heme CHEBI:30413); protoporphyrin IX (CHEBI:15430); coproporphyrin III (CHEBI:131725); uroporphyrin III (CHEBI:15437); pheophorbide a (CHEBI:38257); melanin (CHEBI:133324 / eumelanin); ATP (CHEBI:30616); copper(2+) (CHEBI:29036); L-tyrosine (CHEBI:17895); L-DOPA (CHEBI:15765); 4-phenylbutyrate (CHEBI:41500). **No metabolomic or lipidomic study of DUH3 exists.**

**Immune system involvement.** **None.** DUH3 is not autoimmune, not immunodeficiency-associated, and not inflammatory. The mild perivascular lymphocytic infiltrate on biopsy is a non-specific incidental finding.

**Tissue damage mechanisms.** **None in the conventional sense** — there is no oxidative injury, ischemia, fibrosis, necrosis, atrophy or scarring. The "lesion" is purely a **pigment-distribution abnormality in architecturally intact epidermis**. This is diagnostically important: the absence of atrophy, telangiectasia, poikiloderma and actinic damage distinguishes DUH from xeroderma pigmentosum and dyskeratosis congenita (Aldokhayel et al.).

**Biochemical abnormalities.** **ABC-type heme/porphyrin transporter dysfunction (EC 7.6.2.5).** No enzyme deficiency, receptor defect, or ion-channel abnormality. (The *ABCB6*-related **familial pseudohyperkalemia** phenotype does reflect a red-cell cation-leak defect, but it is a distinct allelic disorder at residue 375.)

**Epigenetic changes.** None studied. **ABCB6 mRNA is normal in patient skin (P = 0.44, Liu et al. 2014)** — the defect is post-transcriptional.

**Molecular profiling.**
- *Transcriptomics:* no DUH3 patient transcriptomic dataset exists. The only RNA-seq in the ABCB6 literature is **murine cochlea** (Baril et al. 2024: *Zbtb20*, *Kcna10*, *Egfr* up; *Spag6*, *Dync1li1* down in KO). Patient-skin **qRT-PCR for ABCB6 showed no difference (P = 0.44)**. No GEO/ArrayExpress accession for DUH3 was identified.
- *Proteomics:* no DUH3 proteomic study. Protein-level evidence is confined to **immunohistochemistry** (ABCB6-positive melanocytes, ABCB6-negative basal keratinocytes, no quantitative difference patient vs control — Liu et al. 2014; Cui et al. 2013 using monoclonal antibody HZ817454 at 1:400) and **Western/pulldown assays in HEK293 and MNT-1** (Baril 2024; Bergam 2018).
- *Metabolomics / lipidomics:* none.
- *Genomic structural features:* none beyond the gene coordinates in §4.1.

**Advanced technologies.**
- *Structural biology (the strongest recent advance):* **cryo-EM structure of human ABCB6 at 2.93 Å**, inward-facing apo state, **PDB 9DBQ**, **EMDB EMD-46724** (Baril et al. 2024). TMD0 is absent from the final model. Comparison structures: 7DNY, 7DNZ (hemin/glutathione-bound), 7D7N, 7D7R, 7EKM, and ABCB10 4AYT for ATP-site overlay. Triplicate **500 ns molecular dynamics** simulations of WT and L356P.
- *Single-cell analysis:* **no single-cell or spatial transcriptomic study of DUH3 skin exists.** This is a clear research opportunity given the mosaic macular phenotype.
- *Spatial transcriptomics:* none.
- *Multi-omics integration:* none.
- *Functional genomics screens (CRISPR/RNAi):* no DUH3-specific screen. siRNA knockdown of ABCB6 in MNT-1 (Bergam 2018) and morpholino knockdown in zebrafish (Liu 2014; Wang 2012; Baril 2024) are the functional-perturbation evidence base.

### 6.3 Cell types and compartments involved

- **Primary cell type: the epidermal melanocyte.** Cell Ontology: **CL:0000148** (melanocyte); **CL:0002331**/**CL:1000458** (epidermal melanocyte — melanocyte of skin); **CL:0000312** (keratinocyte, as the recipient of melanin transfer, secondarily affected); **CL:0002586** (retinal pigment epithelial cell, for the ocular branch); **CL:0000589**/**CL:0000601** (cochlear inner/outer hair cell, for the auditory branch, animal-model evidence only).
- **Subcellular compartments (GO CC):** **GO:0042470** (melanosome) — the key compartment; **GO:0033162** (melanosome membrane); **GO:0005765** (lysosomal membrane); **GO:0010008** (endosome membrane); **GO:0031902** (late endosome membrane); **GO:0031901** (early endosome membrane); **GO:0032585** (multivesicular body membrane); **GO:0000139** (Golgi membrane) — the site of pathological retention; **GO:0005789** (endoplasmic reticulum membrane); **GO:0005741** (mitochondrial outer membrane); **GO:0005886** (plasma membrane); **GO:0070062** (extracellular exosome).
  UniProt lists, with explicit evidence, the subcellular locations: cell membrane (SL-0039), **mitochondrion outer membrane (SL-0172)**, ER membrane (SL-0097), **Golgi apparatus membrane (SL-0134)**, endosome membrane (SL-0100), **lysosome membrane (SL-0157)**, late endosome membrane (SL-0151) and early endosome membrane (SL-0093, by similarity from O70595), secreted/extracellular exosome (SL-0466), mitochondrion (SL-0173), multivesicular body membrane (SL-0175), and **melanosome membrane (SL-0160)**. UniProt states verbatim that ABCB6's intracellular localization **"is a matter of debate,"** with mitochondrial and endolysosomal reports conflicting — a genuinely unsettled point in the field that any knowledge-base entry should preserve rather than resolve.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary organ: the skin.**
- **UBERON:0002097** — skin of body (primary affected organ)
- **UBERON:0001003** — skin epidermis
- **UBERON:0002025**/**UBERON:0002073** — specific regional skin as applicable
- **System:** integumentary system — **UBERON:0002416**

**Regional distribution (UBERON terms for localization annotation):**
- **UBERON:0001085** / **UBERON:0001088** — skin of trunk (**UBERON:0001085** is an approximation; use **UBERON:0008200** skin of trunk where available) — most consistently involved
- **UBERON:0002097** generalized; **UBERON:0001456** — face (involved in **50%** per Murthy et al. 2023)
- **UBERON:0001519** / **UBERON:0001511** — skin of limb/upper limb; **UBERON:0004264** — skin of lower limb
- **UBERON:0001416** — skin of abdomen (biopsy site in Aldokhayel et al.)
- **UBERON:0001068** — skin of back
- **UBERON:0000014** — zone of skin
- **UBERON:0001457** / **UBERON:0001511** — scalp (**UBERON:0000403**) — involved in the Cui proband
- **Characteristically spared:** **UBERON:0001511** palm (skin of palm, **UBERON:0001511**/**UBERON:0006011**), **UBERON:0001513** sole (skin of sole), oral mucosa (**UBERON:0000344**), hair (**UBERON:0001037**), nail (**UBERON:0001705**)

**Secondary organ involvement:**
- **Eye — UBERON:0000970.** Specifically: **iris (UBERON:0001769)** — "abnormal pitting of the iris" in two carriers (Liu et al. 2014); **anterior chamber / aqueous outflow** reflected in raised intraocular pressure in one carrier; **retinal pigment epithelium (UBERON:0001782)** — the site of the mouse melanosome deficit (Bergam et al. 2018) and of ABCB6 expression in human retina/RPE (Wang et al. 2012). **Coloboma (UBERON:0000970 / HP:0000589)** belongs to the allelic disorder MCOPCB7, not DUH3 proper — Cui et al. explicitly record no coloboma in their family.
- **Inner ear — UBERON:0001846.** Animal-model evidence only: **cochlea (UBERON:0001844)**, **utricle (UBERON:0001869)**, **otolith/lapillus (UBERON:0011078 otolith)**, **neuromast (UBERON:0002543)** and **lateral line (UBERON:0002540)** in zebrafish. ZFIN records an *abcb6a* phenotype "lapillus absence of anatomical entity, abnormal" citing PMID 39557842.
- **Blood/erythrocyte — UBERON:0000178 / CL:0000232.** Relevant only to the allelic Lan blood group and pseudohyperkalemia phenotypes, **not to DUH3**.

**Body systems involved:** integumentary (primary); visual/ocular (secondary, minority); auditory/vestibular (possible, animal-model-supported). **Not involved:** cardiovascular, respiratory, digestive, renal, musculoskeletal, immune. Central nervous system involvement (learning difficulties, epilepsy) is reported for DUH broadly but not substantiated for *ABCB6*-DUH3.

### 7.2 Tissue and cell level

- **Tissue type:** stratified squamous epithelium of the epidermis — **UBERON:0001003** (skin epidermis); specifically the **basal layer / stratum basale, UBERON:0002025 (basal cell layer of epidermis)**, where melanocytes reside and where the melanin content is altered (increased in hyperpigmented macules, decreased in hypopigmented macules — Aldokhayel et al.). The **papillary dermis (UBERON:0002067)** contains melanophages in hyperpigmented lesions.
- **Cell populations (Cell Ontology):**
  - **CL:0000148** melanocyte — the primary affected cell (normal in number and morphology; defective in melanosome maturation)
  - **CL:1000458** melanocyte of skin / **CL:0002331** epidermal melanocyte
  - **CL:0000312** keratinocyte / **CL:0002187** basal cell of epidermis — secondarily affected recipients of melanin; **ABCB6-negative by IHC** (Liu et al. 2014)
  - **CL:0000235** macrophage → **melanophage** (dermal melanin-laden macrophage; observed in both lesion types)
  - **CL:0002586** retinal pigment epithelial cell — secondary/ocular
  - **CL:0000542** lymphocyte — mild perivascular infiltrate, non-specific
- **Key negative:** **melanocyte number is normal**; this is not a melanocyte-loss disease (contrast vitiligo).

### 7.3 Subcellular level

The **melanosome (GO:0042470)** is the central affected organelle, with the lesion placed at **stage I/II (early, pre-melanin) melanosomes** where PMEL amyloid matrix assembly occurs. Associated compartments: **melanosome membrane (GO:0033162)**, **lysosomal membrane (GO:0005765)**, **endosome membrane (GO:0010008)**, **Golgi membrane (GO:0000139)** — the compartment of pathological retention of mutant ABCB6, **ER membrane (GO:0005789)**, **mitochondrial outer membrane (GO:0005741)**.

### 7.4 Localization pattern

- **Bilateral and symmetric**, generalized, non-dermatomal, non-segmental. Aldokhayel et al. describe "diffuse, symmetric hyper- and hypopigmented mottled macules."
- **Not photodistributed** — this is a key discriminator from xeroderma pigmentosum: lesions are generalized rather than confined to sun-exposed sites (Aldokhayel et al.), though existing lesions darken with sun exposure.
- **Acral sparing** (palms/soles) is characteristic; this discriminates from reticulate acropigmentation of Kitamura and from dyschromatosis symmetrica hereditaria, which is **acral-predominant** (dorsa of hands and feet).

---

## 8. Temporal Development

### 8.1 Onset

- **Typical age:** **infancy to early childhood**. Murthy et al. 2023, verbatim: lesions *"usually appear in infancy or early childhood."* HPO annotates **HP:0011463 (Childhood onset)** to both cutaneous features of OMIM:615402, sourced from PMID:23519333. GARD states, from Orphanet, that "Symptoms may start to appear as an Infant and as a Child."
- **Documented individual onsets:** within **2 months of birth** (Cui et al. proband, 33-year-old female); in **childhood** on the chest (Aldokhayel mother, 30 years old at report); within the **first 3 years of life** on the inner thighs (Aldokhayel son, 13 years old at report); the broader DUH literature (Cui Introduction) notes DUH "most often manifests within the first year of life."
- **Congenital presentation** is possible but not typical; MedGen's definition says "infancy or early childhood."
- **Onset pattern:** **insidious and gradual** — macules appear at a single site and accrue over months to years. Not acute, not episodic.

### 8.2 Progression

- **Stages:** no formal staging system exists for DUH3. A pragmatic natural-history framing from the case literature:
  1. **Initial (infancy–early childhood):** first macules at a localized site — chest, inner thighs, face, or hands.
  2. **Spreading (childhood–adolescence):** centrifugal extension to trunk, then limbs, then face/scalp. The Saudi mother progressed chest → trunk → whole body including face; her son inner thighs → trunk → forehead.
  3. **Plateau (post-adolescence–adult):** Murthy et al. 2023 verbatim — lesions *"cease to progress beyond adolescence."* Aldokhayel et al. describe the subsequent course verbatim as *"neither progression nor spontaneous regression with age."*
- **Progression rate:** **slow**, over years.
- **Course pattern:** **progressive during childhood, then stable/non-progressive lifelong.** HPO course: **HP:0003680 (Nonprogressive)** applies to the adult phase; **HP:0003674 (Onset)** / **HP:0011463**; **HP:0011009 (Chronic)**.
- **Duration:** **chronic, lifelong**. Not self-limited.

### 8.3 Patterns

- **Remission:** **no spontaneous remission** has been documented. Aldokhayel et al.: "neither progression nor spontaneous regression with age." Treatment-induced improvement is partial and device-dependent (see §12).
- **Critical periods:** The biologically critical window is **melanosome biogenesis during melanocyte development and ongoing melanocyte turnover in childhood**, and — by extrapolation from the animal models — **inner-ear and ocular development in embryogenesis** (zebrafish *abcb6a* is required for otic vesicle/otolith development; Abcb6 KO mice have developmental hearing deficits). **There is no established therapeutic window**: no intervention has been shown to alter the disease trajectory, and no source supports an early-intervention benefit. The practical "window of opportunity" is diagnostic/counselling, not therapeutic.
- **Seasonal/UV variation:** macules darken with sun exposure (Cui et al.), so contrast may fluctuate seasonally — a fluctuating *appearance* on a stable substrate.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **Prevalence:** Murthy et al. 2023 report a prevalence of **0.3 per 100,000**, with a **"female preponderance"** (verbatim). This figure is for **DUH as a whole**, not DUH3 specifically; **no ABCB6-specific prevalence estimate exists**.
- **Incidence:** **no incidence data exist** for DUH or DUH3.
- **Total reported cases:** Yuan et al. 2025 state that **more than 100 DUH cases have been reported**, and that **"more than three-quarters"** came from **Japan, India, China and other Asian countries**. The number of *genotyped ABCB6* cases is far smaller — roughly **40–50 individuals across ~7 publications** (Cui et al.'s single family contributing 21 affected individuals).
- **Orphanet prevalence class could not be retrieved** (orpha.net and the Orphacode API both refused automated access in this session). GARD does not list a prevalence figure. MONDO places DUH3 in the `rare` and `gard_rare` subsets.

### 9.2 Inheritance characteristics

- **Pattern:** **Autosomal dominant** — **HP:0000006**. HPO annotates AD inheritance to OMIM:615402 from PMID:23519333. Murthy et al. 2023: "DUH 1 and DUH 3 are autosomal dominant," the most common pattern, while **DUH 2 is autosomal recessive**. Aldokhayel et al. summarize DUH overall as "mostly autosomal dominant with variable penetrance, with autosomal recessive and sporadic cases also described."
- **Penetrance:** **Apparently complete for the cutaneous phenotype in reported families**, though this is ascertainment-biased. Supporting data: Cui et al. — the c.1663C>A variant was present in **all 21 affected and absent from all 14 unaffected** family members; Liu et al. — p.Ala453Val heterozygous in **all 5 affected and absent in all 8 unaffected** tested members of Family 1, and p.Ser322Lys in **all 7 affected and absent in all 7 unaffected** of Family 2. No non-penetrant obligate carrier has been documented in a published *ABCB6* pedigree. **Age-dependent penetrance applies in early life** — the phenotype is not fully expressed at birth. Note that Aldokhayel et al. describe DUH generally as showing "variable penetrance."
- **Expressivity:** **Variable** — extent of body-surface involvement, facial involvement (50% overall), and the hyper-/hypopigmented balance differ between affected relatives and between families. Cao et al. 2021 argue that phenotypic differences attributed to genotype may instead reflect "skin colour, age and UV exposure," and that genotype–phenotype correlation **"needs to be further investigated."** Ocular involvement is clearly variably expressed: present in 3 of the examined carriers in Liu Family 1, absent in Family 2's tested carrier, and absent in the Cui family.
- **Genetic anticipation:** **Not applicable** — no repeat expansion; no anticipation reported.
- **Germline mosaicism:** **Not reported.** No published instance of recurrence in siblings of unaffected parents attributable to gonadal mosaicism in *ABCB6*-DUH3.
- **Somatic mosaicism:** not reported, though it is an attractive untested hypothesis for the mottled pattern.
- **De novo variants / sporadic cases:** yes — Zhang et al. identified variants in **2 of 6 sporadic patients**; Cui et al. in **1 of 3 sporadic patients** (c.459delC); Liu et al. found none in their **2 sporadic cases**. Parental testing confirming de novo status was not reported in the retrieved material.
- **Founder effects:** **None identified.** The recurrent variant is **c.1270T>C (p.Tyr424His)**, reported as recurrent by Liu JW et al. 2016 — but recurrence in two Chinese reports is insufficient to establish founder status, and no haplotype analysis has been published.
- **Consanguinity:** **Not a factor for DUH3** (dominant). Of note, in the Saudi family (Aldokhayel et al.), the affected mother's **parents were non-consanguineous**, while she herself married a **first-degree cousin who had no similar lesions** — consistent with dominant transmission from the mother, not recessive inheritance. Consanguinity *is* relevant to the recessive DUH2 locus at 12q21–q23 (Stuhrmann et al. 2008, PMID 18462451).
- **Carrier frequency:** **Not applicable** — DUH3 is dominant; heterozygotes are affected. For the allelic **Lan-negative** phenotype, *ABCB6*-null alleles are present at population level (87 LoF alleles observed in gnomAD v4), but these are clinically silent and are not DUH3 alleles.

### 9.3 Population demographics

- **Affected populations:** The genotyped *ABCB6*-DUH3 literature is **overwhelmingly Han Chinese** — Zhang (5-generation Chinese family + Chinese sporadic cases), Cui (4-generation Han Chinese family from rural **Shandong Province**), Liu (multiplex Chinese families), Lu (two Chinese families), Liu JW (two Chinese families), Zhong (Chinese). The sole non-Chinese *ABCB6* family is **Saudi Arabian** (Aldokhayel et al.). DUH as a clinical entity is reported predominantly from **Japan, India, China and other Asian countries** (>75% of >100 reported cases, per Yuan et al. 2025). **This distribution almost certainly reflects ascertainment and research activity rather than a true ethnic predisposition** — DUH's macular dyspigmentation is more conspicuous on moderately pigmented skin, and the major genetic studies were conducted in Chinese dermatogenetics centres.
- **Geographic distribution:** no endemic area; no geographic clustering of specific variants beyond the Chinese concentration of reports.
- **Geographic distribution of specific variants:** c.1144G>A (p.Gly382Arg) — Saudi Arabia (single family); all other reported variants — China.
- **Sex ratio:** **Contested.** Murthy et al. 2023 report a **"female preponderance"** without a numeric ratio. Cui et al.'s single large family was markedly skewed: **21 affected = 4 male, 17 female** — but in an autosomal dominant condition this is almost certainly chance in one pedigree, not a biological sex effect. A 2022 case report in *Pigment International* states DUH shows **equal sex preponderance**. For *SASH1*-related cases, one 2023 source notes 15 of 22 were male. **Recommended curation: sex ratio unknown/approximately equal, with a reported female preponderance of uncertain reliability.** There is no X-linked or sex-limited mechanism.
- **Age distribution of affected individuals:** since onset is in infancy/childhood and the condition is lifelong and non-lethal, **affected individuals span all ages from infancy onward**; prevalence is effectively age-independent after early childhood.

---

## 10. Diagnostics

### 10.1 Clinical tests

**Laboratory tests.** There is **no biochemical, serologic, urinary, or enzymatic test for DUH3.** Routine laboratory evaluation is normal. Two *ABCB6*-adjacent laboratory considerations that are **not** DUH3 diagnostics but are worth knowing:
- **Serum potassium in stored whole blood** — raised in familial pseudohyperkalemia 2 (allelic, residue 375 variants); a pre-analytic artefact, not a DUH3 feature.
- **Langereis (Lan) blood group typing** — relevant only for transfusion medicine in *ABCB6*-null individuals.
LOINC codes applicable: none disease-specific.

**Biomarkers.** **None.** No diagnostic, prognostic, or pharmacodynamic biomarker exists. ABCB6 protein levels are **not** a biomarker: patient skin shows **no significant difference in ABCB6 protein by IHC** and **no difference in mRNA (P = 0.44)** versus control (Liu et al. 2014). No FDA Biomarker List or BEST entry.

**Imaging studies.** **Not applicable.** No role for X-ray, CT, MRI, PET, or ultrasound in diagnosis. (Ophthalmic imaging/examination is indicated only if ocular symptoms arise.)

**Functional tests.** No pulmonary, cardiac, or other functional testing. **Audiometry** is reasonable if hearing impairment is suspected, given the reported high-tone deafness association and the animal-model evidence — but **no guideline recommends routine audiometry in DUH3**, and this would be a clinician judgment call. **Minimal erythema dose (MED) testing** has been used in the DUH literature to assess photosensitivity (Yuan et al. 2025 report UVA-MED 25.4 J/cm² and UVB-MED 44.6 mJ/cm² in a *SASH1* case, documenting absence of photosensitivity).

**Electrophysiology.** **Not applicable** for diagnosis. (ABR was used to demonstrate the hearing phenotype in *Abcb6*-knockout **mice**, not in patients.)

**Dermoscopy.** Listed by Murthy et al. 2023 among the diagnostic methods for the reticulate pigmentary dyschromatoses. Specific dermoscopic criteria for DUH3 were not retrievable.

**Biopsy / histopathology.** Skin biopsy of both a hyperpigmented and a hypopigmented macule is the standard histologic approach. Findings (Aldokhayel et al., two 0.3 × 0.2 cm punch biopsies from the abdomen):
- **Hyperpigmented macule:** increased melanin in the **basal layer**, with melanophages in the dermis.
- **Hypopigmented macule:** decreased basal-layer melanin; mild hyperkeratosis noted in the figure legend.
- **Both:** mild perivascular lymphocytic infiltrate with occasional melanophages.
- **Crucially: melanocyte number is normal** — Cui et al., by methylene-blue light microscopy, found normal numbers of morphologically intact basal melanocytes in both lesion types. **The absence of melanocyte loss excludes vitiligo.**
Immunohistochemistry for ABCB6 is **not diagnostic** (melanocytes are ABCB6-positive in both patients and controls; basal keratinocytes are negative in both).
SNOMED CT concept for the entity: **239082002** (on the parent DUH term).

**Electron microscopy.** Listed by Murthy et al. 2023 as a diagnostic method. The characteristic finding (Cui et al. 2013): hypopigmented macules contain **"empty immature melanosomes"** and reduced mature melanosome content, while hyperpigmented macules have melanosome content similar to control — supporting *"a disorder of melanosome maturing, rather than a disorder of melanocyte number."* EM is research-grade rather than routine.

### 10.2 Genetic testing

**Recommended approach.** DUH is genetically heterogeneous (*ABCB6*, *SASH1*, *PER3*, *KITLG*, plus an unmapped 12q21–q23 recessive locus), and clinically it overlaps substantially with dyschromatosis symmetrica hereditaria (*ADAR1/DSRAD*). **A targeted multigene panel covering the pigmentary dyschromatoses is therefore the most efficient first-line test**, with exome sequencing as the fallback. Liu JW et al. 2016 (*Chin Med J* 129(1):33–38, doi:10.4103/0366-6999.172564, **PMID 26712430 / PMC4797540**) demonstrated exactly this: three patients from two families, both initially diagnosed clinically as DUH, were resolved by **targeted gene sequencing** into one family with a novel *ADAR1* variant (i.e. DSH, not DUH) and one with a recurrent *ABCB6* variant (c.1270T>C) — "Differential Diagnosis of Two Chinese Families with Dyschromatoses by Targeted Gene Sequencing." *(Note: the full text of this paper was blocked by a bot-check in this session; the variant assignments above derive from the PubMed/Europe PMC record and the Cao et al. 2021 variant catalogue.)*

| Modality | Utility in DUH3 |
|---|---|
| **Single-gene testing (*ABCB6*)** | High yield when the phenotype is classic generalized mottled dyschromatosis with a dominant pedigree; *ABCB6* is "the most common gene involved in DUH" (Murthy et al. 2023). Sanger sequencing of all 19 coding exons. |
| **Gene panel** | **Preferred first-line.** Should include *ABCB6*, *SASH1*, *ADAR* (*ADAR1/DSRAD*), *KITLG*, *PER3*; broader pigmentary-disorder panels also cover *POFUT1*/*POGLUT1* (Dowling-Degos), *KRT5*, *TYR*, *OCA2*, *SLC45A2*, *MITF*, *KIT*, *EDNRB*, *SOX10*. **Genomics England PanelApp hosts a "Pigmentary skin disorders" panel (Panel 559) that includes ABCB6** ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/559/gene/ABCB6/)). **GTR lists 12 genetic tests registered for DUH3** (MedGen). |
| **WES** | Useful when a panel is negative or the phenotype is atypical/syndromic. WES was the discovery modality in Zhang 2013, Cui 2013, Liu 2014, and Chen 2023. |
| **WGS** | No established incremental utility over WES/panel for DUH3; no deep-intronic or structural *ABCB6* variant has been reported. Reserve for unsolved cases. |
| **Chromosomal microarray (CMA)** | **No established role.** No CNV has been implicated. |
| **Karyotype** | **No role.** |
| **FISH** | **No role.** |
| **Mitochondrial DNA testing** | **No role** — despite ABCB6's historical "mitochondrial ABC transporter 3 / MTABC3" name, this is a **nuclear** gene and the disorder is not mitochondrially inherited. This naming is a genuine source of confusion worth flagging in a knowledge base. |
| **Repeat expansion testing** | **No role.** |

**Linkage analysis** retains historical/research importance only (HLOD 4.68 at 2q35–q37.2, Cui; 5.08 combined, Liu; LOD 1.81 at 2q34–q37 and other loci, Liu Family 1).

### 10.3 Omics-based diagnostics

- **RNA sequencing / transcriptomics:** **no diagnostic role.** ABCB6 mRNA is normal in patient skin (P = 0.44). RNA-seq might theoretically resolve a splice variant such as c.1452+2T>A (ClinVar Likely pathogenic) but this has not been reported.
- **Proteomics:** no role; ABCB6 protein level in skin does not discriminate patients from controls.
- **Metabolomics:** no role; no metabolite signature known.
- **Epigenomics:** no role; no methylation episignature described.
- **Liquid biopsy:** not applicable (non-neoplastic germline disorder).

### 10.4 Clinical criteria and differential diagnosis

**There is no formal, society-endorsed diagnostic criterion set, no DSM/ICD operational definition, and no published clinical practice guideline for DUH3.** MedGen's "Professional guidelines" section lists only a single research article (Liu JW et al. 2016, PMID 26712430), not an actual guideline. No GeneReviews chapter exists for DUH3. Diagnosis is **clinical (morphology + distribution + onset + pedigree), supported by histopathology, and confirmed by molecular testing.**

A practical working definition: generalized, asymptomatic, bilaterally symmetric, intermixed hyper- and hypopigmented macules of irregular shape and size, 3–7 mm, over trunk and extremities ± face, sparing palms/soles/mucosae, with onset in infancy/early childhood, progression ceasing after adolescence, normal melanocyte numbers on biopsy, and a heterozygous *ABCB6* variant.

**Differential diagnosis:**

| Condition | Distinguishing features |
|---|---|
| **Dyschromatosis symmetrica hereditaria (DSH) / reticulate acropigmentation of Dohi** — *ADAR1* (*DSRAD*), OMIM 127400 | **The single most important differential.** DSH is **acral-predominant** (dorsa of hands and feet, sometimes face), whereas DUH is **generalized/truncal**. Resolution by *ADAR1* vs *ABCB6* sequencing (Liu JW et al. 2016 did exactly this). Explicitly listed as the first differential by Aldokhayel et al. |
| **DUH1 (*SASH1*) / DUH2 / *PER3*-DUH** | Clinically overlapping; distinguished only genetically. Cao et al. report that *SASH1*-related disease is more often confused with **generalized lentiginosis**, whereas *ABCB6*-related disease shows the typical "generalized mottled hyperpigmented macules mixed with hypopigmented macules arranged in a reticular pattern" — though these same authors say they "have different views" on how reliable this distinction is. *SASH1* carries additional concerns (palmoplantar keratoderma and skin carcinoma for some alleles), so **genotype matters for surveillance**. |
| **Xeroderma pigmentosum** | DUH lesions are **generalized rather than photo-exposed**, and show **no atrophy or telangiectasia** (Aldokhayel et al.). XP has marked photosensitivity, poikiloderma, and early cutaneous malignancy. *Caveat:* an *ABCB6* p.N467S variant was reported in a **XP-C** patient with DUH-like pigmentation — overlap exists. |
| **Dyskeratosis congenita** | Listed by Aldokhayel et al. DC has the triad of reticulate pigmentation, nail dystrophy and oral leukoplakia, plus bone-marrow failure — DUH3 spares nails and mucosae and has no haematologic involvement. |
| **Dowling-Degos disease** (*KRT5*, *POFUT1*, *POGLUT1*) | Flexural reticulate hyperpigmentation with comedo-like lesions and pitted perioral scars; later onset; **no hypopigmented component**. |
| **Reticulate acropigmentation of Kitamura** (*ADAM10*) | Atrophic reticulate pigmentation of the dorsa of hands/feet with **palmar pits and breaks in dermatoglyphics** — DUH spares palms. |
| **Naevus depigmentosus / vitiligo** | Vitiligo shows **melanocyte loss** on biopsy (DUH does not), is typically later-onset, often progressive, and lacks the intermixed hyperpigmented component. Naevus depigmentosus is segmental/stable and purely hypopigmented. |
| **Naevoid/segmental pigmentary mosaicism, incontinentia pigmenti, linear and whorled naevoid hypermelanosis** | Follow **Blaschko lines** — DUH does not. |
| **Unilateral dermatomal pigmentary dermatosis** | Within the reticulate dyschromatosis family but **unilateral/dermatomal** (Murthy et al. 2023). |
| **Generalized lentiginosis / LEOPARD-Noonan spectrum (*PTPN11*)** | Zhang J et al. 2016 (*Clin Genet*, **PMID 27659786**) specifically addressed "lentiginous phenotypes caused by diverse pathogenic genes (*SASH1* and *PTPN11*): clinical and molecular discrimination." |
| **Post-inflammatory dyspigmentation, pityriasis versicolor, confluent and reticulated papillomatosis** | Acquired, later-onset, non-familial; versicolor is KOH-positive. |

### 10.5 Screening

- **Newborn screening:** **not indicated and not performed anywhere.** DUH3 is non-lethal, non-progressive after adolescence, and has no effective treatment — it fails every Wilson-Jungner criterion.
- **Carrier screening:** **not applicable** (dominant disorder; heterozygotes are affected, not carriers). Not on any ACMG expanded carrier screening panel.
- **Cascade testing:** **appropriate and the main screening application.** Once a familial *ABCB6* variant is identified, at-risk relatives can be tested — chiefly for reproductive counselling and diagnostic certainty rather than for any medical intervention. Clinical skin examination of first-degree relatives is simple and informative (Aldokhayel et al. identified an affected sister of the proband).
- **Targeted surveillance in diagnosed individuals:** no evidence-based protocol. **Ophthalmological examination** is reasonable given Liu et al.'s iris and IOP findings and the allelic coloboma disorder; **audiometry** is reasonable given the reported deafness association and animal-model data. **Both are clinician judgment, not guideline-supported.**

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

- **Survival rate:** **Normal.** No excess mortality has been reported.
- **Life expectancy:** **Not reduced.** No retrieved source reports any mortality attributable to DUH3.
- **Mortality rate / disease-specific mortality:** **Zero / not applicable.** There are no deaths attributable to DUH3 in the literature. The disease has no organ-failure, malignant, or metabolic complication pathway.
- **Caveat on cancer risk:** Cui et al. explicitly record that **no affected member of their 21-patient family had skin cancer**. Murthy et al. 2023 report their own observations of DUH with **hepatocellular carcinoma** and **solitary keratoacanthoma** — anecdotal co-occurrence, not an established risk. Cancer concern in the DUH literature attaches principally to ***SASH1*** (Yuan et al. 2025 note that the skin-carcinoma risk must be considered when using NB-UVB in *SASH1*-related DUH; Cao et al. note a *SASH1* allele linked to palmoplantar keratoderma and skin carcinoma). **No elevated malignancy risk has been established for *ABCB6*-DUH3.**

### 11.2 Morbidity and function

- **Morbidity:** **Cosmetic and psychosocial only.** The lesions are asymptomatic, the skin barrier is intact, and there is no pain, pruritus, infection risk, or functional skin impairment.
- **Disability outcomes:** **None** attributable to the cutaneous phenotype. Potential, unquantified, minority contributors to disability would be **hearing impairment** (reported in DUH generally; mechanistically supported by *Abcb6* animal models) and **ocular abnormality** (iris changes, raised IOP in individual carriers — with glaucoma a theoretical downstream risk if IOP elevation is sustained and untreated, though this was not followed in the source).
- **Quality of life measures:** **No EQ-5D, SF-36, PROMIS, DLQI or Skindex data exist for DUH or DUH3.** This is an explicit evidence gap. The high rate of facial involvement (50%) and childhood onset make a substantial psychosocial burden likely, but this is inference.
- **ICF framing:** impairment of body structure (skin pigmentation) without impairment of body function; activity limitation nil; **participation restriction possible via appearance-related stigma** — not studied.

### 11.3 Disease course and complications

- **Complications:** none intrinsic. There is no progression to organ failure, no infection risk, no scarring. **The documented adverse events in this disease are treatment-related, not disease-related:** Yuan et al. 2025 report that IPL caused **erythema and crusting** at treatment sites immediately, with **no significant improvement after 2 months**.
- **Recovery potential:** **The pigmentary changes are permanent.** Aldokhayel et al., verbatim on the course: *"neither progression nor spontaneous regression with age."* Yuan et al. 2025, verbatim: *"An effective treatment for DUH has not yet been established."* Murthy et al. 2023 conclude that **"no treatment is promising."** Partial, device-dependent cosmetic improvement is achievable (§12).
- **Stability:** the best-established prognostic statement is Murthy et al.'s — lesions **"cease to progress beyond adolescence."** Patients and families can be counselled that the condition will stabilize.

### 11.4 Prediction

- **Prognostic factors:** **None validated.** No age, severity, biomarker, or treatment-response predictor has been established. By analogy with other pigmentary disorders, extent of involvement at presentation and facial involvement would be expected to predict psychosocial burden — unstudied.
- **Prognostic biomarkers:** **None.** ABCB6 protein and mRNA levels in skin do not differ from control and therefore have no prognostic value.
- **Genotype–prognosis correlation:** Cao et al. 2021 state the genotype–phenotype correlation in DUH **"needs to be further investigated."** The one actionable genotype distinction is **gene-level, not allele-level**: *SASH1*-related DUH carries skin-carcinoma considerations that *ABCB6*-related DUH does not, which affects whether NB-UVB is advisable.

---

## 12. Treatment

### 12.1 Overall treatment position

**There is no disease-modifying, curative, or reliably effective treatment for DUH3.** The two most recent sources are unambiguous. Murthy et al. 2023 (*Int J Dermatol* review) conclude that NBUVB and lasers have been tried and that **"no treatment is promising."** Yuan et al. 2025 state verbatim: **"An effective treatment for DUH has not yet been established."** Management is therefore **cosmetic, symptomatic-reassurance, and genetic-counselling based.** No treatment has been studied in a controlled trial.

**NCIT suggestions for the overall category:** NCIT:C15431 (Supportive Care); NCIT:C15313 (Laser Therapy); NCIT:C15688 (Phototherapy); NCIT:C15632 (Genetic Counseling); NCIT:C15229 (Watchful Waiting / observation).

### 12.2 Pharmacotherapy

- **No pharmacological agent has established efficacy in DUH3.** No drug is approved for this indication by FDA, EMA, or any regulator. No DrugBank/RxNorm/ATC entry maps to DUH3.
- Topical depigmenting agents (hydroquinone, tretinoin) and topical camouflage are standard dermatologic tools for dyspigmentation generally, but **no retrieved source reports their use or efficacy in DUH** — notably, Yuan et al. 2025's treatment discussion makes **no mention of hydroquinone, tretinoin, sunscreen or camouflage**. These should be curated as plausible but unevidenced for this disease, not as recommended therapy.
- **NCIT (if a depigmenting approach is annotated):** NCIT:C29234 (Hydroquinone); NCIT:C900 (Tretinoin). **Annotate as "not established for this disease."**

### 12.3 Pharmacogenomics

**No pharmacogenomic consideration specific to DUH3 exists** (PharmGKB/CPIC have no DUH3 entry). However, a **gene-level** pharmacologic note is worth recording for a knowledge base: **ABCB6 is an ATP-dependent xenobiotic/porphyrin efflux transporter that confers in vitro resistance to arsenic, cadmium, 5-fluorouracil, SN-38 and vincristine** (UniProt Q9NP58), and mouse *Abcb6* knockouts show **MP:0009766 increased susceptibility to xenobiotic induced morbidity/mortality**, **MP:0008873 increased** and **MP:0008874 decreased physiological sensitivity to xenobiotic** (allele-dependent). Whether heterozygous DUH3 patients have altered handling of these agents is **untested and unknown** — a legitimate open question rather than a clinical recommendation.

### 12.4 Advanced therapeutics

- **Gene therapy:** none; no preclinical program identified. The skin is an accessible target, but the dominant-negative mechanism would require **allele-specific silencing or editing**, not gene addition. **No study retrieved.**
- **Cell therapy:** none. (Melanocyte transplantation is used in stable vitiligo but would be futile here, since DUH3 melanocytes are present in normal numbers and intrinsically defective.)
- **RNA-based therapies (ASO/siRNA):** none reported. Conceptually attractive for a dominant-negative allele; wholly hypothetical.
- **Targeted therapies / small-molecule correctors:** **The most interesting preclinical lead.** Baril et al. 2024 showed the chemical chaperone **4-phenylbutyrate (4-PBA) significantly increased L356P ABCB6 expression (p = 0.00262)** in HEK293 cells, while MG132 and chloroquine did not — raising the possibility of a **proteostasis/corrector strategy** analogous to CFTR correctors. **This is an in vitro observation in a heterologous cell line only; no melanocyte, animal, or human data exist.** CHEBI:41500 (4-phenylbutyrate).
- **Immunotherapies:** not applicable.

### 12.5 Surgical and interventional

- **Laser therapy** is the mainstay of attempted cosmetic treatment. Evidence:
  - **Q-switched alexandrite laser, 755 nm**, applied to hyperpigmented macules on exposed areas (citing Nogita 2011): Yuan et al. 2025 note that **"the long-term efficacy remains uncertain."** Also mentioned in the Aldokhayel et al. discussion as a reported option, though **not administered to their patients**.
  - **Picosecond laser (Cynosure; 3 mm spot, fluence 2.83 J/cm², pulse width 750 ps)**: in the single published case (Yuan et al. 2025, an 11-year-old with *SASH1*-related DUH), this produced **"significant improvement" at 1 week**. **Important caveats:** this is an **n = 1 case report in SASH1-DUH, not ABCB6-DUH3**; the **number of sessions is not stated**; the patient **declined further treatment because of cost**, so **no long-term follow-up exists**; and adverse effects of the picosecond laser were not described. The authors conclude picosecond laser is "safe and effective" for hyperpigmented lesions but state that **larger cohorts are needed**.
  - **Intense pulsed light (IPL)** — in the same case, Lumenis M22, 560 nm cutoff filter, 17 J/cm², two pulses, 35 ms pulse delay: caused immediate **erythema and crusting** and produced **no significant improvement after 2 months**. **IPL should be regarded as ineffective and poorly tolerated based on this report.**
- **Ablative/destructive modalities** — surgical excision, dermabrasion, electrodesiccation, chemical peeling — are described by Yuan et al. 2025 (citing Nogita 2011) as **limited by scarring and dyspigmentation**, i.e. the complication reproduces the problem being treated. **Not recommended.**
- **NCIT:** NCIT:C15313 (Laser Therapy); NCIT:C158874/NCIT:C15313 (Q-switched laser therapy); NCIT:C92948 (Intense Pulsed Light Therapy); NCIT:C15215 (Dermabrasion); NCIT:C15329 (Chemical Peel); NCIT:C15329.

### 12.6 Phototherapy

- **Narrowband UVB (NB-UVB):** Yuan et al. 2025 state it **"is effective in some patients"** (citing Yadalla 2013); Murthy et al. 2023 list it among tried modalities while concluding no treatment is promising. **Critical caveat from Yuan et al.: skin carcinoma risk must be considered — but that caution was raised specifically in the context of the *SASH1* association.** Whether NB-UVB is appropriate in *ABCB6*-DUH3 is unaddressed; its use would also be counterintuitive for lesions that darken with UV exposure.
- **NCIT:** NCIT:C15688 (Phototherapy); NCIT:C158897/NCIT:C15688 (Ultraviolet B Phototherapy).

### 12.7 Supportive and rehabilitative care

- **Cosmetic camouflage** and **photoprotection** are the rational, low-risk supportive measures — though, again, **no retrieved source documents their efficacy in DUH**.
- **Psychological/psychosocial support** for appearance-related distress, particularly in children and adolescents, is clinically sensible given onset age and 50% facial involvement. **Not studied in this disease.**
- **Rehabilitation (PT/OT/speech):** **not applicable** — there is no functional impairment.
- **Audiologic and ophthalmologic management** if those features are present: standard care for the specific finding (hearing aids, IOP management), not DUH-specific.
- **NCIT:** NCIT:C15431 (Supportive Care); NCIT:C168003/NCIT:C15632 (Genetic Counseling); NCIT:C15316 (Psychotherapy/Psychosocial support).

### 12.8 Experimental treatments / clinical trials

**No clinical trial of any intervention for dyschromatosis universalis hereditaria was identified in this session, and no NCT identifier can be cited.** There is no interventional or observational trial, no natural-history study, and no registry. The only "experimental" lead is the preclinical 4-PBA observation above.

### 12.9 Treatment outcomes, response rates and adverse events

- **Response rates:** no cohort data exist; **n = 1 reports only**. Picosecond laser: "significant improvement" at 1 week (1 patient, SASH1-DUH). IPL: no significant improvement at 2 months (same patient). Q-switched alexandrite: long-term efficacy uncertain. NB-UVB: "effective in some patients," unquantified.
- **Adverse events:** IPL — immediate erythema and crusting. Ablative modalities — scarring and dyspigmentation. NB-UVB — theoretical cutaneous carcinogenesis (emphasized for *SASH1*). **No FAERS signal is applicable** (no drug is used).

### 12.10 Treatment strategy and personalized medicine

There is **no published treatment algorithm, clinical pathway, or decision tree** for DUH3. A defensible pragmatic approach, synthesized from the above (and explicitly labelled as synthesis, not guideline):

1. **Establish the molecular diagnosis** by panel/single-gene testing — this matters because **gene identity changes management**: *SASH1* raises skin-carcinoma considerations relevant to phototherapy choice, *ADAR1* reclassifies the patient as DSH, *ABCB6* raises (unvalidated) ocular and auditory considerations.
2. **Counsel on natural history** — asymptomatic, benign, stabilizes after adolescence, no excess mortality, no spontaneous resolution. For many families this is the most valuable intervention.
3. **Offer genetic counselling** and, if desired, cascade testing and reproductive options (§13).
4. **Consider baseline ophthalmologic examination** (Liu et al.'s iris/IOP findings; allelic coloboma disorder) and **audiometric assessment** if symptoms suggest — judgment-based, not guideline-based.
5. **For cosmetically distressing lesions**, discuss photoprotection and camouflage first; then, if the patient wishes, **Q-switched or picosecond laser directed at hyperpigmented macules**, with explicit counselling that evidence is limited to single cases, long-term efficacy is unknown, and **IPL and ablative/destructive modalities are not advised**.
6. **Avoid promising a result.** Both the most recent review and the most recent case report state that no effective treatment is established.

- **Combination therapies:** none studied.
- **Genotype-guided treatment:** no allele-specific therapy exists. The gene-level distinction described in step 1 is the only "personalized medicine" currently operative.

---

## 13. Prevention

### 13.1 Primary prevention

**Primary prevention of DUH3 is possible only through reproductive genetics.** Because the disorder is monogenic, fully genetically determined, and has no modifiable environmental component, there is **no behavioural, dietary, vaccination, or exposure-reduction strategy that prevents its occurrence.**

The one documented preventive intervention in the DUH literature is **preimplantation genetic testing (PGT)**:
- **Wang XL, Zou T, Wu YC, Weng YY, Yao Q, Sun WW.** "Preventing transmission of dyschromatosis universalis hereditaria through preimplantation genetic testing: A case report." *World J Clin Cases* 2025 Nov 6;13(31):110620. doi:10.12998/wjcc.v13.i31.110620. **PMID 41283180 / PMC12635852.** A 30-year-old woman with a DUH-causing variant underwent assisted reproduction with preimplantation genetic testing, and the couple had a healthy baby. **Important caveat for curation: this case involved a *SASH1* mutation, not *ABCB6*** — but the approach is directly transferable to *ABCB6*-DUH3, since both are autosomal dominant single-gene disorders with an identifiable familial variant.
- **Prenatal diagnosis** (CVS or amniocentesis with targeted familial-variant testing) is technically straightforward once the familial *ABCB6* variant is known, but raises a substantial ethical question given that DUH3 is a **benign, non-life-limiting, non-disabling cosmetic condition** — a point that should be made explicitly in counselling rather than left implicit.
- **NCIT:** NCIT:C92837/NCIT:C19399 (Preimplantation Genetic Diagnosis); NCIT:C17076 (Prenatal Diagnosis).

### 13.2 Secondary prevention (early detection)

- **Cascade clinical and genetic evaluation of first-degree relatives** of a proband. This is low-cost and effective at case-finding (Aldokhayel et al.'s proband had a sister recently diagnosed with DUH). Its value, however, is diagnostic clarity and counselling — **not earlier treatment, since no treatment alters the course.**
- **No population screening program exists or is justified.** DUH3 fails the standard screening criteria: no asymptomatic latent phase amenable to intervention, no effective treatment, negligible morbidity.
- **Newborn screening: not indicated.** Not on the RUSP or any national NBS panel.

### 13.3 Tertiary prevention (preventing complications in affected individuals)

Because DUH3 has essentially no intrinsic complications, tertiary prevention reduces to:
- **Avoiding iatrogenic harm** — specifically, avoiding ablative/destructive modalities (dermabrasion, electrodesiccation, deep chemical peels, surgical excision) that risk scarring and further dyspigmentation, and avoiding IPL on the single reported experience (erythema, crusting, no benefit).
- **Weighing carcinogenic risk before phototherapy**, particularly where a *SASH1* genotype is in play.
- **Surveillance for the minority associated features** — ophthalmologic examination (iris abnormality, intraocular pressure) and audiometric assessment where indicated. **No evidence-based surveillance interval exists; this is clinician judgment.**
- **Photoprotection** to limit UV-driven accentuation of lesional contrast (mechanistically sensible given Cui et al.'s observation of sun-driven darkening; efficacy unproven).

### 13.4 Immunization

**Not applicable.** DUH3 has no infectious component; no vaccine is relevant to its prevention or management.

### 13.5 Genetic screening and risk stratification

- **Carrier screening:** not applicable (dominant disorder).
- **Risk stratification:** trivially determined by pedigree — 50% risk to each offspring of an affected individual. No polygenic score, risk model, or clinical calculator exists or is needed.
- **Predictive testing in at-risk minors:** since onset is in infancy/early childhood and the condition is visually apparent, predictive genetic testing in asymptomatic children has little clinical utility.

### 13.6 Genetic counselling

This is **the single most valuable intervention in DUH3.** Content should cover:
- **50% recurrence risk** to each child of an affected parent; both sexes equally affected and equally transmitting.
- **Penetrance appears complete** in published *ABCB6* pedigrees, but **expressivity is variable** — an affected child may be more or less extensively involved than the parent, and facial involvement cannot be predicted.
- **Benign natural history**: asymptomatic, non-progressive after adolescence, normal life expectancy, no established cancer risk for *ABCB6*.
- **Limited treatment options** and the importance of not over-promising cosmetic results.
- **Reproductive options**: natural conception with or without prenatal diagnosis; PGT (precedent: PMID 41283180); gamete donation; adoption — presented non-directively, with explicit acknowledgment that the condition is cosmetic.
- **Possibility of sporadic/de novo cases** (2/6 and 1/3 in the two sporadic series), meaning an isolated case does not exclude *ABCB6*.
- **Resources:** NSGC; ACMG; **GTR lists 12 registered tests** for DUH3. **No GeneReviews chapter exists** for this disorder.
- **NCIT:** NCIT:C15632 (Genetic Counseling); NCIT:C15709 (Genetic Testing).

### 13.7 Public health and environmental interventions

**Not applicable.** DUH3 has no environmental, occupational, sanitation, vector, or nutritional determinant. No public health intervention is relevant. No EPA/WHO environmental health measure applies.

### 13.8 Prophylaxis

**No prophylactic medication or procedure exists or is indicated.**

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy and orthologous genes

Orthologs of human *ABCB6* (HGNC:47), from the Alliance of Genome Resources stringent ortholog set:

| Species | NCBI Taxon | Gene ID | Symbol | Best score | Confidence | Methods matched |
|---|---|---|---|---|---|---|
| *Homo sapiens* | **NCBITaxon:9606** | NCBI Gene 10058 / HGNC:47 | *ABCB6* | — | — | — |
| *Mus musculus* | **NCBITaxon:10090** | **MGI:1921354** / NCBI Gene **74104** / ENSMUSG00000026198 | *Abcb6* | Yes | **high** | 10 |
| *Rattus norvegicus* | **NCBITaxon:10116** | **RGD:71077** | *Abcb6* | Yes | **high** | 10 |
| *Danio rerio* | **NCBITaxon:7955** | **ZFIN:ZDB-GENE-070912-584** / NCBI Gene 100004801 | *abcb6b* | Yes | high | 6 |
| *Danio rerio* | NCBITaxon:7955 | **ZFIN:ZDB-GENE-050517-9** / NCBI Gene 564067 | *abcb6a* | No | low | 1 |
| *Xenopus tropicalis* | **NCBITaxon:8364** | Xenbase:XB-GENE-1001119 | *abcb6* | Yes | high | 9 |
| *Xenopus laevis* | **NCBITaxon:8355** | Xenbase:XB-GENE-6487681 | *abcb6.L* | Yes | high | 1 |
| *Caenorhabditis elegans* | **NCBITaxon:6239** | WB:WBGene00001815 | ***hmt-1*** | Yes | high | 9 |
| *Drosophila melanogaster* | **NCBITaxon:7227** | FB:FBgn0038376 | ***Hmt-1*** | Yes | high | 9 |

**No yeast ortholog** is present in the Alliance stringent set.

**Mouse *Abcb6* location:** chromosome 1, minus strand, 75,148,361–75,157,036 (per MGI quicksearch; assembly not stated in the retrieved record).

**Note of practical importance:** the zebrafish functional work in the DUH literature has been performed on ***abcb6a*** (ZDB-GENE-050517-9) — the paralog with the *lower* Alliance ortholog confidence — in Liu et al. 2014, Wang et al. 2012, and Baril et al. 2024. *abcb6b*, the higher-confidence ortholog, has **zero phenotype annotations** in ZFIN. This ortholog-assignment discrepancy should be noted when interpreting the zebrafish data.

### 14.2 Breed

**Not applicable.** No breed-specific *ABCB6* pigmentary disorder has been reported. No VBO identifier is assignable.

### 14.3 Natural disease in other species

**No naturally occurring *ABCB6*-associated dyschromatosis has been documented in any companion animal, livestock species, or wildlife population.** No OMIA (Online Mendelian Inheritance in Animals) entry for an *ABCB6* pigmentary phenotype was identified in this session. All animal data derive from **engineered laboratory models**, not natural disease. **Veterinary relevance: none established.**

### 14.4 Comparative biology

- **Evolutionary conservation of the gene is deep and strong**: single-copy, high-confidence orthologs span mammals, amphibians, fish, insects and nematodes. The invertebrate orthologs are named ***hmt-1*** ("heavy metal tolerance") in both *C. elegans* and *Drosophila*, reflecting the ancestral function of this ABC half-transporter subfamily in **heavy-metal/xenobiotic detoxification** — consistent with human ABCB6's in vitro arsenic and cadmium resistance and with GO:0098849 (cellular detoxification of cadmium ion). The **pigmentation role is a vertebrate-specific elaboration** layered onto an ancient transport function.
- **Conservation of the disease residues:** the DUH-affected residues are highly conserved across species (Cui et al.: Gln555; Liu et al.: both their residues). Zebrafish Abcb6 **binds ATP and porphyrins comparably to human ABCB6**, though it **lacks the N-linked glycosylation site and is not a glycoprotein** (Baril et al. 2024) — a species difference relevant to trafficking studies.
- **Comparative pathology — a crucial caveat:** **the pigmentary phenotype does not transfer cleanly to mice.** Baril et al. 2024 explicitly note that a **prior C57BL/6 *Abcb6* knockout showed no pigmentation, eye, or balance abnormalities**. The mouse captures the **melanosome-number deficit only at the subcellular level in the RPE** (Bergam et al. 2018) and captures a **hearing phenotype** (Baril et al. 2024), but **not the dyschromatosis**. This is expected if the human disease is dominant-negative rather than loss-of-function, since knockouts model the wrong mechanism.
- **Zebrafish recapitulates the melanocyte phenotype best** (see §15).

### 14.5 Transmission

**Not applicable.** DUH3 is a non-communicable, non-infectious germline genetic disorder. There is **no zoonotic potential and no cross-species transmissibility.**

---

## 15. Model Organisms

### 15.1 Mouse (*Mus musculus*, NCBITaxon:10090; *Abcb6*, MGI:1921354)

**Available alleles** (Alliance/MGI):

| Allele ID | Symbol | Type |
|---|---|---|
| **MGI:5426703** | *Abcb6<sup>tm1Jsch</sup>* | targeted knockout (Schuetz lab) — the most phenotyped allele |
| **MGI:5463225** | *Abcb6<sup>tm1Pkr</sup>* | targeted |
| **MGI:4362220** | *Abcb6<sup>tm1a(KOMP)Wtsi</sup>* | KOMP knockout-first, conditional-ready |
| **MGI:4363653** | *Abcb6<sup>tm1e(KOMP)Wtsi</sup>* | KOMP targeted |
| **MGI:7309238** | *Abcb6<sup>em1Gpt</sup>* (syn. *Abcb6<sup>em1Cflox</sup>*) | CRISPR-derived conditional (floxed) |

So the full toolkit exists: **constitutive knockout, knockout-first/conditional-ready, and a CRISPR floxed conditional allele** — enabling melanocyte-specific or RPE-specific deletion, which to my knowledge has not yet been exploited for pigmentation studies.

**Reported MP phenotypes** (Alliance; list is partial — the response was truncated, and the total was reported as 8):

| MP ID | Term | Allele | Reference |
|---|---|---|---|
| **MP:0003656** | abnormal erythrocyte physiology | *Abcb6<sup>tm1Jsch</sup>* (MGI:5426703) | PMID:22294697 |
| **MP:0006036** | abnormal mitochondrial physiology | *Abcb6<sup>tm1Jsch</sup>* | PMID:22294697 |
| **MP:0009766** | increased susceptibility to xenobiotic induced morbidity/mortality | *Abcb6<sup>tm1Jsch</sup>* | PMID:22294697 |
| **MP:0010831** | lethality, incomplete penetrance | *Abcb6<sup>tm1Jsch</sup>* | PMID:22294697 |
| MP:0031276 | abnormal stress erythropoiesis | *Abcb6<sup>tm1Jsch</sup>* | PMID:22294697 |
| MP:0002098 | abnormal vibrissa morphology | *Abcb6<sup>tm1a(KOMP)Wtsi</sup>* (MGI:4362220) | MGI:5576271 (IMPC) |
| MP:0008873 | increased physiological sensitivity to xenobiotic | *Abcb6<sup>tm1Jsch</sup>* | PMID:22294697 |
| MP:0008874 | decreased physiological sensitivity to xenobiotic | *Abcb6<sup>tm1Pkr</sup>* (MGI:5463225) | PMID:22761424 |

*(The last four rows derive from a model-extracted portion of the Alliance response and should be verified against MGI directly before being treated as definitive.)*

**Phenotypes reported in the primary literature but not (yet) in the MP annotation set:**
- **Reduced melanosome numbers in the retinal pigment epithelium** of *Abcb6*-knockout mice (Bergam et al. 2018, PMID 29940187). Suggested MP: **MP:0005195 (abnormal posterior eye segment morphology)** / an RPE-pigmentation term; suggested GO/CL anchors: GO:0042470 (melanosome), CL:0002586 (RPE cell).
- **Increased auditory brainstem response thresholds at all tested frequencies** in 5–6-week-old knockouts (N = 6 KO vs 5 WT, C57/129 mixed background) with cochlear transcriptomic changes (*Zbtb20*, *Kcna10*, *Egfr* up; *Spag6*, *Dync1li1* down) — Baril et al. 2024, PMID 39557842. Suggested MP: **MP:0004362 (abnormal auditory brainstem response)** / MP:0006325 (increased or absent threshold for auditory brainstem response).
- **Explicit negative:** an earlier **C57BL/6 knockout showed no pigmentation, eye, or balance abnormalities** (noted by Baril et al.) — background-dependence is likely and matters for model selection.

**Phenotype recapitulation:** **Poor for the cardinal human phenotype.** The *Abcb6* knockout mouse does **not** reproduce mottled cutaneous dyschromatosis. It does reproduce a **subcellular melanosome deficit in the RPE** and a **hearing deficit**. **Limitations:** (i) the mouse models **loss of function**, whereas the human disease is most likely **dominant-negative** — a knock-in of a human DUH allele (e.g. L356P) would be the mechanistically correct model and **has not been made**; (ii) mouse coat pigmentation biology differs fundamentally from human epidermal/interfollicular melanocyte biology, since mouse interfollicular epidermis is largely amelanotic; (iii) strain-background dependence; (iv) incompletely penetrant lethality complicates cohort generation.

**Applications:** porphyrin/heme transport and stress erythropoiesis; xenobiotic handling; RPE melanosome biogenesis; inner-ear development and auditory function. **Not currently useful for modelling the human cutaneous phenotype or for testing cosmetic/dermatologic therapeutics.**

### 15.2 Zebrafish (*Danio rerio*, NCBITaxon:7955; *abcb6a*, ZFIN:ZDB-GENE-050517-9)

**The best available model of the DUH pigmentary phenotype.** Zebrafish melanophores are externally visible and countable, giving a direct quantitative pigmentation readout.

**Liu et al. 2014 (PMID 24498303), morpholino knockdown of z*abcb6*:** two morpholinos targeting exon 6 and exon 8 (homologous to human exons 4 and 7, i.e. the exons harbouring their two DUH variants). No gross morphological defect at 5 dpf. **Mature head melanocytes at 5 dpf:**

| Group | Melanocytes (mean ± SEM) | n | p |
|---|---|---|---|
| Uninjected control | **48.84 ± 0.68** | 57 | — |
| exon 6 morphants | **23.38 ± 3.20** | 13 | < 0.001 |
| exon 8 morphants | **29.04 ± 1.18** | 24 | < 0.001 |
| exon 6 + human *ABCB6* mRNA rescue | **39.71 ± 2.47** | 19 | < 0.001 (vs morphant) |
| exon 8 + human *ABCB6* mRNA rescue | **40.77 ± 1.26** | 30 | < 0.001 (vs morphant) |

This is a **~52% and ~41% reduction in melanocyte number, substantially rescued by human wild-type *ABCB6* mRNA** — establishing that ABCB6 function is required for normal melanocyte development/pigmentation in vivo.

**ZFIN phenotype annotations for *abcb6a*** (partial, from Alliance):
- "embryo development delayed, abnormal" (GO:0009790, PATO:0000502), fish ZFIN:ZDB-FISH-150901-11943 (WT + MO2-abcb6a), **PMID:22226084**, standard conditions
- "head melanocyte decreased amount, abnormal" — **PMID:24498303**, fish ZDB-FISH-150901-609 and ZDB-FISH-150901-22427
- "iris perforate, abnormal" — **PMID:22226084** (the coloboma phenotype)
- "lapillus absence of anatomical entity, abnormal" — **PMID:39557842** (the otolith phenotype)
*(The last three derive from a model-extracted portion of a very large response; verify against ZFIN directly.)*

**Wang et al. 2012 (PMID 22226084):** morpholino knockdown produced a **coloboma-like phenotype matching the index human case**, corrected by co-injection of wild-type *ABCB6* mRNA but **not** by mutant mRNA. *(Baril et al. 2024 critique this study for not validating the knockdown.)*

**Baril et al. 2024 (PMID 39557842):** *abcb6a* is expressed in the otic vesicle at 3 dpf (WISH). Splice-blocking **MO15** (exon15/intron15) reduced hair cells per neuromast (two-way ANOVA genotype effect **F(1,111) = 126.6, p < 0.0001**; N = 8 uninjected, N = 9 MO15, 3 dpf Brn3c:GFP), **p53-independent** (p = 0.35 vs MO15 + p53 MO). **MO15 blocked utricular otolith formation up to 14 dpf with the saccule intact**; human *ABCB6* mRNA rescue (N = 19) gave 52.6% wild-type, 42.1% partial, 5.3% unrescued. **MO7** (exon 7) also reduced hair cells but did **not** produce the single-otolith phenotype — the authors suggest MO15 may generate a misfolded product acting as a **dominant negative**, which is mechanistically resonant with the human disease. Vestibular behaviour at 21 dpf (N = 18 uninjected, N = 25 MO15): bottom-third occupancy **39.9% vs 1.2% (p < 0.0001)**; vertical distance **160.7 vs 79.7 px (p = 0.0041)**; horizontal distance not significant (p = 0.0785). Some MO15 larvae had few neuromasts at 3 dpf and failed to inflate the swim bladder at 4 dpf but looked normal by 5 dpf. **Red blood cells (o-dianisidine) were unaffected.**

**Phenotype recapitulation:** **Good for melanocyte/pigmentation, good for coloboma, good for inner ear.** **Limitations:** (i) all data are **morpholino knockdown**, not germline mutants — no *abcb6a* CRISPR knockout line has been reported, and morpholino off-target and toxicity concerns apply (partially addressed by p53-null controls and mRNA rescue); (ii) zebrafish melanophore biology differs from human epidermal melanocyte biology; (iii) the model tests **loss of function**, not the human dominant-negative mechanism; (iv) *abcb6a* vs *abcb6b* ortholog assignment is ambiguous (see §14.1); (v) zebrafish Abcb6 is not glycosylated, unlike human ABCB6.

### 15.3 Cellular and in vitro models

| System | Use | Source |
|---|---|---|
| **MNT-1** (human melanocytic cell line) | **The key pigment-cell model.** ABCB6 localization to early-melanosome and lysosome membranes; siRNA depletion impairs PMEL amyloidogenesis and causes multilamellar aggregates; rescue by WT but **not** by **K629M** (catalytically dead) or **G579E** (DUH allele). Cellosaurus: MNT-1 (CVCL_5624) | Bergam et al. 2018, PMID 29940187 |
| **B16 mouse melanoma** | WT ABCB6 → endosome-like compartments and dendrite tips; **DUH mutants retained in Golgi**. Cellosaurus: B16 (CVCL_F936) | Zhang et al. 2013, PMID 23519333 |
| **HEK293 (transient transfection)** | Expression, ATP-agarose and hemin-agarose binding, ATPase, thermal shift, 4-PBA chaperone rescue for **S170G, S322R, L356P, Y424H, A453V, Q555K, G579E** | Baril et al. 2024, PMID 39557842 |
| **Human primary epidermal melanocytes (HEM)** | ABCB6 protein detected; used for IHC validation | Liu et al. 2014, PMID 24498303 |
| **Immortalized human melanocytes** | Used for the *SASH1*/TGF-β1 work (Cui H et al. 2020, *Int J Biol Sci* 16(7):1264–1273, doi:10.7150/ijbs.38415, **PMID 32174800 / PMC7053321**) — relevant to DUH1, not DUH3 |
| **RPE cells (transfected, Myc-tagged ABCB6)** | ER and Golgi localization | Wang et al. 2012, PMID 22226084 |
| **Proteoliposomes / purified mitochondrial ABCB6** | Transport kinetics: ATP Km 0.99 mM, Vmax 492.3 nmol/min/mg; coproporphyrin III Km 11.97 µM | UniProt Q9NP58 |
| **Purified protein → cryo-EM** | **2.93 Å structure, PDB 9DBQ, EMDB EMD-46724**; triplicate 500 ns MD of WT and L356P | Baril et al. 2024 |

**Not reported for DUH3:** patient-derived **iPSC** lines, iPSC-derived melanocytes, **skin organoids**, 3D reconstructed epidermis models, or patient primary melanocyte cultures. **These are the most conspicuous missing model systems**, and a patient-derived iPSC-melanocyte or isogenic CRISPR knock-in melanocyte line would directly test the dominant-negative hypothesis in the correct cell type.

### 15.4 Model databases

- **MGI / Mouse Genome Informatics** — https://www.informatics.jax.org/ (mouse *Abcb6*, **MGI:1921354**)
- **IMPC / KOMP** — https://www.mousephenotype.org/ (*Abcb6<sup>tm1a(KOMP)Wtsi</sup>*, MGI:4362220)
- **IMSR / MMRRC / EMMA** — strain repositories for the above alleles
- **RGD** — rat *Abcb6*, **RGD:71077**
- **ZFIN** — zebrafish *abcb6a* **ZDB-GENE-050517-9**, *abcb6b* **ZDB-GENE-070912-584**
- **Alliance of Genome Resources** — https://www.alliancegenome.org/gene/HGNC:47 (cross-species integration; the most reliable single entry point given ZFIN and MGI bot-blocking)
- **Xenbase** — XB-GENE-1001119 (*X. tropicalis*), XB-GENE-6487681 (*X. laevis*)
- **WormBase** — WBGene00001815 (*hmt-1*); **FlyBase** — FBgn0038376 (*Hmt-1*)
- **Cellosaurus** — MNT-1, B16, HEK293
- **PDB / EMDB** — **9DBQ**, **EMD-46724** (and comparison structures 7DNY, 7DNZ, 7D7N, 7D7R, 7EKM, 4AYT)

---

## Appendix A — Primary literature inventory (ABCB6 + DUH)

| PMID | Citation | Relevance |
|---|---|---|
| **23519333** | Zhang C, Li D, Zhang J, et al. *J Invest Dermatol* 2013;133(9):2221–8. doi:10.1038/jid.2013.145 | **Gene discovery.** L356P, S170G, G579E; Golgi retention. **Sole HPO annotation source for OMIM:615402** |
| **24224009** | Cui YX, Xia XY, Zhou Y, et al. *PLoS One* 2013;8(11):e79808. doi:10.1371/journal.pone.0079808. PMC3818219 | Q555K; c.459delC; EM melanosome maturation data; 21-affected Shandong family |
| **24498303** | Liu H, Li Y, Hung KKH, et al. *PLoS One* 2014;9(2):e87250. doi:10.1371/journal.pone.0087250. PMC3911924 | A453V, S322K/R; zebrafish melanocyte counts; ocular findings; dominant-negative hypothesis |
| **25288164** | Lu C, Liu J, Liu F, Liu Y, Ma D, Zhang X. *J Dermatol Sci* 2014;76(3):255–8. doi:10.1016/j.jdermsci.2014.08.015 | Two novel missense variants in two Chinese families. **Variant nomenclature could not be retrieved** |
| **26712430** | Liu JW, Asan, Sun J, et al. *Chin Med J* 2016;129(1):33–8. doi:10.4103/0366-6999.172564. PMC4797540 | Targeted panel differentiating *ADAR1* (DSH) from *ABCB6* (DUH); recurrent *ABCB6* c.1270T>C |
| **30430618** | Zhong W, Pan Y, Shao Y, Yang Y, Yu B, Lin Z. *Clin Exp Dermatol* 2019;44(3):e58–e60. doi:10.1111/ced.13833 | "Atypical presentation" with a novel *ABCB6* mutation. **No abstract indexed; variant and clinical details could not be retrieved** |
| **35024399** | Aldokhayel S, et al. *JAAD Case Rep* 2021;19:97–99. doi:10.1016/j.jdcr.2021.11.017. PMC8727889 | **c.1144G>A, p.Gly382Arg, exon 5**; Saudi mother (30 y) and son (13 y); the only non-Chinese *ABCB6* family |
| **29940187** | Bergam P, Reisecker JM, Rakvács Z, et al. *J Mol Biol* 2018;430(20):3802–18. doi:10.1016/j.jmb.2018.06.033 | **Core mechanism:** ABCB6 in melanosomes; PMEL amyloid; K629M and G579E fail to rescue; KO mouse RPE |
| **39557842** | Baril SA, Wilson KA, Shaik MM, et al. *Nat Commun* 2024;15:9885. doi:10.1038/s41467-024-53663-x. PMC11574312 | **Cryo-EM 2.93 Å (PDB 9DBQ)**; functional dissection of 7 DUH variants; L356P dominant-negative; inner-ear phenotype |
| **22246506** | Helias V, Saison C, Ballif BA, et al. *Nat Genet* 2012;44(2):170–3. doi:10.1038/ng.1069. PMC3664204 | **ABCB6 is dispensable for erythropoiesis; Langereis blood group; null humans are healthy** |
| **22226084** | Wang L, He F, et al. *Am J Hum Genet* 2012;90(1):40–48. PMC3257322 | *ABCB6* and ocular coloboma (MCOPCB7): L811V, A57T; zebrafish eye phenotype |
| **17006453** | Krishnamurthy PC, Du G, Fukuda Y, et al. *Nature* 2006;443(7111):586–9 | ABCB6 as mitochondrial porphyrin transporter (foundational function) |
| **37634201** | Murthy AB, Palaniappan V, Karthikeyan K, Anbarasan V. *Int J Dermatol* 2023;62(10):1218–27. doi:10.1111/ijd.16817 | **Most recent comprehensive review.** Prevalence 0.3/100,000; 50% facial involvement; "no treatment is promising" |
| **18462451** | Stuhrmann M, et al. *Clin Genet* 2008 | DUH autosomal recessive; 12q21–q23 locus (DUH2 context) |
| **34174894** | Cao L, et al. *BMC Med Genomics* 2021;14:168. doi:10.1186/s12920-021-01014-w. PMC8236144 | **Catalogue of the nine ABCB6 DUH variants**; ABCB6 vs SASH1 phenotype discussion |
| **36790533** | Chen H, et al. *J Mol Med (Berl)* 2023;101(3):279–94. doi:10.1007/s00109-023-02288-6 | *PER3* rs772027021 + *SASH1* digenic DUH (non-*ABCB6*) |
| **41283180** | Wang XL, Zou T, Wu YC, et al. *World J Clin Cases* 2025;13(31):110620. doi:10.12998/wjcc.v13.i31.110620. PMC12635852 | **Preimplantation genetic testing to prevent DUH transmission** (SASH1 case) |
| — | Yuan L, et al. *Skin Health Dis* 2025. doi:10.1093/skinhd/vzaf024. PMC12202865 (PMID 40584949) | Picosecond laser improvement; IPL failure; treatment-landscape statements |

## Appendix B — Explicit evidence gaps and retrieval failures in this session

**Could not be retrieved (blocked, 403/404, or bot-checked), and therefore not reported:**
- **OMIM 615402 and 605452 full text** — omim.org returned HTTP 403. The OMIM Clinical Synopsis, the full TEXT sections, the complete Allelic Variant list with `.000X` numbers, and the OMIM reference list are therefore absent from this report. (Partial recovery: ClinVar `variation_xrefs` confirm **OMIM 605452.0011** for c.1663C>A/p.Gln555Lys and **OMIM 605452.0014** for c.1123C>T/p.Arg375Trp.)
- **Orphanet ORPHA:241** — orpha.net served an anti-bot interstitial; the Orphacode API returned HTTP 401. The official Orphanet definition, prevalence class, ICD cross-references, and management text are missing.
- **ICD-10 and ICD-11 codes for DUH** — the ICD-11 browser is a JavaScript application that did not render. Only the indirect evidence is available: KEGG places H02350 under **ICD-11 EC23.Y** (Genetic disorders of skin pigmentation, other specified), and MONDO:0000736 carries `icd11.foundation:480710406`. **An ICD-10 code could not be confirmed.**
- **Murthy et al. 2023 full text** — Wiley returned HTTP 403; only the abstract (via Semantic Scholar, Crossref and Europe PMC) was available. Tables, gene-frequency breakdowns, and treatment detail are missing.
- **Lu et al. 2014 variant nomenclature** and **Zhong et al. 2019 variant and clinical details** — neither is indexed with an abstract in PubMed or Europe PMC, and publisher pages were blocked.
- **Liu JW et al. 2016 full text** — PMC served a reCAPTCHA interstitial.
- **Per-variant gnomAD allele frequencies** for the ten DUH variants — the gene-level payload exceeded the fetch limit and Ensembl REST calls failed with connection resets. **One targeted query completed: chr2-219216084-A-G (c.1067T>C / p.Leu356Pro) returned "Variant not found" in gnomAD v4.** Gene-level constraint metrics (§4.4) were retrieved successfully.
- **Bergam et al. 2018 full text** — abstract only (Europe PMC); quantitative figure-level data on melanosome counts, melanin content, and localization percentages are missing.
- **Verbatim abstract text** for most PubMed records — the retrieval route permitted only limited direct quotation; where quotes appear above they are marked, and the remainder is faithful paraphrase of retrieved text.

**Genuinely absent from the literature (not a retrieval problem):**
- GeneReviews chapter; clinical practice guideline; ClinGen gene-disease validity classification or VCEP
- Any clinical trial, natural-history study, or patient registry
- Any quality-of-life measurement in DUH or DUH3
- Epigenomic, transcriptomic, proteomic, metabolomic, lipidomic, single-cell or spatial data from DUH3 patient tissue
- Patient-derived iPSC, organoid, or isogenic knock-in melanocyte models
- A knock-in mouse carrying a human DUH allele (the mechanistically correct model)
- Incidence data, ABCB6-specific prevalence, and a reliable sex ratio
- Modifier genes, protective alleles, and any gene–environment interaction study

---

## Sources

- [MedGen C3809394 — Dyschromatosis universalis hereditaria 3](https://www.ncbi.nlm.nih.gov/medgen/C3809394)
- [HPO / JAX annotation API — OMIM:615402](https://ontology.jax.org/api/network/annotation/OMIM:615402)
- [EBI OLS4 — MONDO:0014169](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0014169)
- [KEGG DISEASE H02350 — Dyschromatosis universalis hereditaria](https://www.kegg.jp/entry/H02350)
- [UniProt Q9NP58 — ABCB6_HUMAN](https://rest.uniprot.org/uniprotkb/Q9NP58.json)
- [gnomAD — ABCB6 (ENSG00000115657) constraint, GraphQL API](https://gnomad.broadinstitute.org/gene/ENSG00000115657)
- [NCBI Gene 10058 — ABCB6 (E-utilities esummary)](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&retmode=json&id=10058)
- [ClinVar — ABCB6 variants associated with dyschromatosis (E-utilities)](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&retmode=json&retmax=100&term=ABCB6%5Bgene%5D+AND+%22dyschromatosis%22)
- [Alliance of Genome Resources — ABCB6 (HGNC:47) and orthologs](https://www.alliancegenome.org/gene/HGNC:47)
- [GARD 1996 — Dyschromatosis universalis hereditaria](https://rarediseases.info.nih.gov/diseases/1996/dyschromatosis-universalis-hereditaria)
- [Cui YX et al., PLoS One 2013;8(11):e79808 — Novel mutations of ABCB6 (PMC3818219)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3818219/)
- [Liu H et al., PLoS One 2014;9(2):e87250 — Genome-wide linkage, exome sequencing and functional analyses identify ABCB6 (PMC3911924)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3911924/)
- [Zhang C et al., J Invest Dermatol 2013;133(9):2221-8 — Mutations in ABCB6 cause DUH (PMID 23519333)](https://pubmed.ncbi.nlm.nih.gov/23519333/)
- [Lu C et al., J Dermatol Sci 2014;76(3):255-8 (PMID 25288164)](https://pubmed.ncbi.nlm.nih.gov/25288164/)
- [Zhong W et al., Clin Exp Dermatol 2019;44(3):e58-e60 (PMID 30430618)](https://pubmed.ncbi.nlm.nih.gov/30430618/)
- [Aldokhayel S et al., JAAD Case Rep 2021;19:97-99 — Novel ABCB6 mutation in a Saudi family (PMC8727889)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8727889/)
- [Murthy AB et al., Int J Dermatol 2023;62(10):1218-1227 — Dyschromatosis universalis hereditaria](https://onlinelibrary.wiley.com/doi/10.1111/ijd.16817)
- [Cao L et al., BMC Med Genomics 2021;14:168 — Novel SASH1 missense mutation (PMC8236144)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8236144)
- [Baril SA et al., Nat Commun 2024;15:9885 — The role of ABCB6 in the inner ear (PMC11574312)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11574312/)
- [Bergam P et al., J Mol Biol 2018;430(20):3802-3818 — ABCB6 resides in melanosomes (PMID 29940187)](https://pubmed.ncbi.nlm.nih.gov/29940187/)
- [Helias V et al., Nat Genet 2012;44(2):170-3 — ABCB6 is dispensable for erythropoiesis / Langereis (PMID 22246506)](https://pubmed.ncbi.nlm.nih.gov/22246506/)
- [Krishnamurthy PC et al., Nature 2006;443(7111):586-9 — Mitochondrial porphyrin transporter (PMID 17006453)](https://pubmed.ncbi.nlm.nih.gov/17006453/)
- [Wang L et al., Am J Hum Genet 2012;90(1):40-48 — ABCB6 mutations cause ocular coloboma (PMID 22226084)](https://pubmed.ncbi.nlm.nih.gov/22226084/)
- [Liu JW et al., Chin Med J 2016;129(1):33-38 — Differential diagnosis by targeted gene sequencing (PMC4797540)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4797540/)
- [Yuan L et al., Skin Health Dis 2025 — DUH with SASH1 mutation improved with picosecond laser (PMC12202865)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12202865)
- [Chen H et al., J Mol Med (Berl) 2023;101(3):279-294 — PER3 rs772027021 and DUH (PMID 36790533)](https://pubmed.ncbi.nlm.nih.gov/36790533/)
- [Cui H et al., Int J Biol Sci 2020;16(7):1264-1273 — SASH1 promotes melanin synthesis (PMID 32174800)](https://pubmed.ncbi.nlm.nih.gov/32174800/)
- [Wang XL et al., World J Clin Cases 2025;13(31):110620 — PGT to prevent DUH transmission (PMID 41283180)](https://pubmed.ncbi.nlm.nih.gov/41283180/)
- [Jayanthi NS et al., J Clin Diagn Res 2016 — DUH with primary ovarian failure (PMID 27134983)](https://pubmed.ncbi.nlm.nih.gov/27134983/)
- [Zhang J et al., Clin Genet 2016 — Lentiginous phenotypes: SASH1 and PTPN11 discrimination (PMID 27659786)](https://pubmed.ncbi.nlm.nih.gov/27659786/)
- [Genomics England PanelApp — Pigmentary skin disorders (Panel 559), ABCB6](https://panelapp.genomicsengland.co.uk/panels/559/gene/ABCB6/)
- [PubMed search inventory — "ABCB6 dyschromatosis"](https://pubmed.ncbi.nlm.nih.gov/?term=ABCB6+dyschromatosis)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 50 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 49 |
| On topic | 25 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:22294697` (6 mentions) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 203 |
| Resolved | 173 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 2 |
| Unverifiable | 26 |
| Terms whose name was checked | 69 |
| Terms named correctly | 39 |
| Terms named as a **different** term | 19 |
| Terms whose name is worth a second look | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014169` (7 mentions) - the report calls it "MONDO"; MONDO calls it **dyschromatosis universalis hereditaria 3**
- `MONDO:0000736` (4 mentions) - the report calls it "Parent term (generic DUH)", "generic DUH"; MONDO calls it **dyschromatosis universalis hereditaria**
- `HP:0007441` (2 mentions) - the report calls it "Generalized hyperpigmentation — if widespread"; HP calls it **Hyperpigmented/hypopigmented macules**
- `HP:0007513` (1 mention) - the report calls it "Abnormal dermal melanin deposition"; HP calls it **Generalized hypopigmentation**
- `HP:0011009` (2 mentions) - the report calls it "Chronic"; HP calls it **Acute**
- `HP:0001087` (1 mention) - the report calls it "Iris atrophy"; HP calls it **Developmental glaucoma**
- `HP:0012629` (1 mention) - the report calls it "Abnormal iris morphology"; HP calls it **Phakodonesis**
- `HP:0007906` (3 mentions) - the report calls it "Iris coloboma"; HP calls it **Ocular hypertension**
- `NCIT:C15431` (2 mentions) - the report calls it "Supportive Care"; NCIT calls it **Hematopoietic Cell Transplantation**
- `NCIT:C15688` (3 mentions) - the report calls it "Phototherapy", "Ultraviolet B Phototherapy"; NCIT calls it **Maintenance Therapy**
- `NCIT:C15632` (3 mentions) - the report calls it "Genetic Counseling"; NCIT calls it **Chemotherapy**
- `NCIT:C15229` (1 mention) - the report calls it "Watchful Waiting / observation"; NCIT calls it **Antitumor Drug Screening Assay**
- `NCIT:C29234` (1 mention) - the report calls it "Hydroquinone"; NCIT calls it **MSM/Glucosamine**
- `NCIT:C92948` (1 mention) - the report calls it "Intense Pulsed Light Therapy"; NCIT calls it **Rh Factor Measurement**
- `NCIT:C15316` (1 mention) - the report calls it "Psychotherapy/Psychosocial support"; NCIT calls it **Relaxation Therapy**
- `NCIT:C19399` (1 mention) - the report calls it "Preimplantation Genetic Diagnosis"; NCIT calls it **Computational Chemistry Statistics**
- `NCIT:C17076` (1 mention) - the report calls it "Prenatal Diagnosis"; NCIT calls it **Prolactin Receptor**
- `MP:0004362` (1 mention) - the report calls it "abnormal auditory brainstem response"; MP calls it **cochlear hair cell degeneration**
- `MP:0006325` (1 mention) - the report calls it "increased or absent threshold for auditory brainstem response"; MP calls it **impaired hearing**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0008553` (1 mention) - HP does not contain this term
- `NCIT:C168003` (1 mention) - NCIT does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `CL:0002331` (CL_0002331) (2 mentions) - replaced by `CL:1000349`
- `UBERON:0002543` (obsolete median fin skeleton) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000006` (3 mentions) - the report calls it "autosomal dominant", "Autosomal dominant inheritance"; HP calls it **Autosomal dominant inheritance**, and lists "Autosomal dominant" among its other names
- `HP:0001000` (1 mention) - the report calls it "Abnormality of skin pigmentation, parent"; HP calls it **Abnormal skin pigmentation**, and lists "Abnormality of skin pigmentation" among its other names
- `HP:0000593` (1 mention) - the report calls it "Abnormality of the iris"; HP calls it **Abnormal anterior chamber morphology**, and lists "Abnormality of the anterior chamber" among its other names
- `HP:0040194` (1 mention) - the report calls it "Increased intraocular pressure"; HP calls it **Increased head circumference**
- `HP:0000989` (1 mention) - the report calls it "Pruritus — N/A, excluded"; HP calls it **Pruritus**
- `HP:0000957` (1 mention) - the report calls it "Café-au-lait spot"; HP calls it **Cafe-au-lait spot**
- `CHEBI:41500` (2 mentions) - the report calls it "4-phenylbutyrate"; CHEBI calls it **4-phenylbutyric acid**
- `CL:0002586` (3 mentions) - the report calls it "RPE cell"; CL calls it **retinal pigment epithelial cell**, and lists "RPE" among its other names
- `NCIT:C15313` (3 mentions) - the report calls it "Laser Therapy", "Q-switched laser therapy"; NCIT calls it **Radiation Therapy**, and lists "Cancer Radiotherapy" among its other names
- `NCIT:C15215` (1 mention) - the report calls it "Dermabrasion"; NCIT calls it **Cryosurgery**, and lists "CRYOABLATION" among its other names
- `NCIT:C15329` (2 mentions) - the report calls it "Chemical Peel"; NCIT calls it **Surgical Procedure**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0000736` - called "Parent term (generic DUH)", "generic DUH"
- `HGNC:47` - called "HGNC", "ABCB6", "cross-species integration; the most reliable single entry point given ZFIN and MGI bot-blocking"
- `HP:0000006` - called "autosomal dominant", "Autosomal dominant inheritance"
- `NCIT:C15313` - called "Laser Therapy", "Q-switched laser therapy"
- `NCIT:C15688` - called "Phototherapy", "Ultraviolet B Phototherapy"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `EXT_ID`, `OMIM`, `ORPHA`, `GARD`, `OMIMPS`, `Orphanet`, `SCTID`, `UMLS`, `NC_000002.11`, `RHEA`, `MGI`, `RGD`.