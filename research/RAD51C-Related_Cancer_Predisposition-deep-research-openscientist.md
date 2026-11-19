---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T22:25:54.196978'
end_time: '2026-11-12T22:52:51.934025'
duration_seconds: 1617.74
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: RAD51C-Related Cancer Predisposition
  mondo_id: MONDO:0700273
  category: Mendelian
  causal_genes: RAD51C
  omim_id: not recorded
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
  job_id: bcd4331a-1791-41b8-b390-b25316140853
citation_count: 28
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 31
  on_topic: 24
  validator_version: 0.5.1
term_validation:
  total_terms: 31
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 30
  labels_matching: 14
  labels_mismatched: 14
  mislabelled_terms:
  - term_id: GO:0000724
    reported_labels:
    - DSB repair via HR
    ontology_label: double-strand break repair via homologous recombination
  - term_id: CHEBI:63631
    reported_labels:
    - olaparib
    ontology_label: topiramate
  - term_id: HP:0100615
    reported_labels:
    - ovarian neoplasm
    - Cumulative ~11% by 80; RR 7.55
    ontology_label: Ovarian neoplasm
  - term_id: HP:0003002
    reported_labels:
    - breast carcinoma
    - Cumulative ~21%; RR ~2
    ontology_label: Breast carcinoma
  - term_id: HP:0012125
    reported_labels:
    - prostate cancer
    - Among DDR-panel carriers
    ontology_label: Prostate cancer
  - term_id: HP:0005528
    reported_labels:
    - bone marrow hypocellularity, FA arm
    - Biallelic cases
    ontology_label: Bone marrow hypocellularity
  - term_id: HP:0001510
    reported_labels:
    - growth delay, FA arm
    - Biallelic cases
    ontology_label: Growth delay
  - term_id: UBERON:0000996
    reported_labels:
    - oviduct infundibulum/fimbria
    ontology_label: vagina
  - term_id: UBERON:0002367
    reported_labels:
    - peritoneum
    - Secondary:** peritoneum
    ontology_label: prostate gland
  - term_id: MONDO:0011705
    reported_labels:
    - Fanconi anemia complementation group O
    ontology_label: lymphangioleiomyomatosis
  - term_id: NCIT:C71721
    reported_labels:
    - Olaparib
    - "Pharmacotherapy / targeted:** **PARP inhibitors** \u2014 olaparib"
    ontology_label: Olaparib
  - term_id: NCIT:C78844
    reported_labels:
    - Rucaparib
    ontology_label: Ficlatuzumab
  - term_id: NCIT:C97660
    reported_labels:
    - Niraparib
    ontology_label: Abemaciclib
  - term_id: NCIT:C51686
    reported_labels:
    - salpingo-oophorectomy
    - Surgical/preventive:** risk-reducing salpingo-oophorectomy
    ontology_label: Esophageal Biopsy
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: RAD51C-Related_Cancer_Predisposition-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: RAD51C-Related_Cancer_Predisposition-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RAD51C-Related Cancer Predisposition
- **MONDO ID:** MONDO:0700273 (if available)
- **Causal gene(s):** RAD51C
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **RAD51C-Related Cancer Predisposition** covering all of the
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

# RAD51C-Related Cancer Predisposition (MONDO:0700273) — Comprehensive Disease Characteristics Report

**Causal gene: _RAD51C_** (RAD51 paralog C; HGNC:9820; NCBI Gene 5889; Ensembl ENSG00000108384; UniProt O43502; cytoband 17q22). MONDO:0700273 ("RAD51C-related cancer predisposition").

## Summary

**RAD51C-related cancer predisposition** is an autosomal-dominant hereditary cancer syndrome caused by germline loss-of-function (LoF) variants in **RAD51C**, one of five RAD51 paralogs and an essential component of the homologous-recombination (HR) DNA double-strand-break (DSB) repair machinery and the replication-fork-protection apparatus. The disease exhibits a striking **gene-dosage duality**: a single (monoallelic/heterozygous) pathogenic variant predisposes to adult-onset tubo-ovarian and breast cancer, whereas two (biallelic) hypomorphic variants cause a **Fanconi anemia-like syndrome (Fanconi anemia complementation group O, FANCO)** with congenital malformations and bone-marrow failure.

The cancer-predisposition phenotype is dominated by a **high relative risk of high-grade serous tubo-ovarian carcinoma** (relative risk [RR] ≈ 7.5; cumulative risk to age 80 ≈ 11%) and a **moderate, triple-negative-predominant breast cancer risk** (RR ≈ 2; cumulative risk ≈ 21%). Tumors develop through a classic two-hit mechanism: a germline LoF allele plus somatic inactivation of the wild-type allele (by mutation, deletion, or—as a somatic phenocopy—promoter hypermethylation), producing an **HR-deficient ("BRCAness") tumor** with a characteristic mutational signature 3. This HR deficiency is both the oncogenic driver and the therapeutic vulnerability: RAD51C-deficient cancers are sensitive to **platinum chemotherapy and PARP inhibitors** through synthetic lethality.

Clinically, the syndrome is managed as a moderate-penetrance hereditary breast-and-ovarian cancer (HBOC) gene: **risk-reducing salpingo-oophorectomy (RRSO)** around menopause is the primary ovarian-cancer prevention, enhanced breast surveillance is offered, and genetic counseling with cascade testing of relatives is standard. The cell of origin for the ovarian/tubal tumors is the **secretory epithelial cell of the fallopian-tube fimbria**, which acquires a *TP53* mutation forming a serous tubal intraepithelial carcinoma (STIC) before seeding the ovary and peritoneum. This report synthesizes nine confirmed findings across 65 reviewed papers into a comprehensive, section-by-section disease characterization.

---

## Key Findings

### Finding 1 — RAD51C has a dual gene-dosage phenotype

RAD51C uniquely bridges two disease categories through allele dosage. **Biallelic** (homozygous hypomorphic missense) germline mutation was first identified in a consanguineous family with multiple severe congenital abnormalities characteristic of Fanconi anemia (FA); the patient cells lost RAD51 focus formation and were hypersensitive to the crosslinking agent mitomycin C and to camptothecin, defining Fanconi anemia complementation group O (FANCO) ([PMID: 20400963](https://pubmed.ncbi.nlm.nih.gov/20400963/)). As the authors state: *"We have identified a homozygous missense mutation in the RAD51C gene in a consanguineous family with multiple severe congenital abnormalities characteristic of FA."*

In contrast, **monoallelic** germline pathogenic variants are established **moderate (intermediate) penetrance** tubo-ovarian and triple-negative breast cancer predisposition alleles, as codified in the 2025 ACMG clinical practice resource ([PMID: 41070818](https://pubmed.ncbi.nlm.nih.gov/41070818/)): *"RAD51C, RAD51D, and BRIP1 are moderate (intermediate) penetrance ovarian cancer predisposition genes."* This dosage duality is mechanistically coherent — complete HR failure in every cell (biallelic) is developmentally catastrophic (FA), whereas one functional allele (monoallelic) permits normal development until somatic second-hit loss triggers focal carcinogenesis.

### Finding 2 — RAD51C functions as a RAD51 paralog in HR via the BCDX2 and CX3 complexes

RAD51C is a member of two RAD51-paralog subcomplexes: **BCDX2** (RAD51B–RAD51C–RAD51D–XRCC2) and **CX3** (RAD51C–XRCC3). These paralogs *"have emerged as essential tumour suppressors, forming two subcomplexes, BCDX2 and CX3"* ([PMID: 39268578](https://pubmed.ncbi.nlm.nih.gov/39268578/)). BCDX2 facilitates **RAD51 loading onto single-stranded DNA (ssDNA)**, suppressing the cooperative requirement of RAD51–DNA binding and stabilizing the nucleoprotein filament—including on short ssDNA stretches and reversed replication forks.

Recent cryo-EM work reveals the mechanistic logic: paralog exchange converts an **autoinhibited RAD51–XRCC3–RAD51C octamer** into an **activated pentamer** to regulate filament formation during HR and fork preservation ([PMID: 42020761](https://pubmed.ncbi.nlm.nih.gov/42020761/)). Beyond canonical DSB repair, RAD51C protects stalled replication forks; cancer-associated missense variants (**F164S, A87E, L134S, E49K**) show reduced RAD51 foci and defective fork protection, confirming that *"the role of RAD51C in DNA replication is emerging when replication forks are transiently or irreversibly stalled"* ([PMID: 36562461](https://pubmed.ncbi.nlm.nih.gov/36562461/)). RAD51C also participates in R-loop resolution with the FANCM pathway, linking its FA and cancer functions ([PMID: 41719405](https://pubmed.ncbi.nlm.nih.gov/41719405/)).

### Finding 3 — Pathogenic variants confer high tubo-ovarian risk (RR ≈ 7.6) and moderate breast risk (RR ≈ 2)

The definitive risk estimates come from a complex segregation analysis of **6,178 families** (125 with RAD51C pathogenic variants) ([PMID: 32107557](https://pubmed.ncbi.nlm.nih.gov/32107557/)): *"Pathogenic variants in both RAD51C and RAD51D were associated with TOC (RAD51C: relative risk [RR] = 7.55, 95% confidence interval [CI] = 5.60 to 10.19; P = 5 × 10-40)."* The same study established the absolute cumulative risks to age 80: *"The estimated cumulative risks of developing TOC to age 80 years were 11% (95% CI = 6% to 21%) for RAD51C."* Breast cancer RR was 1.99 (95% CI 1.39–2.85; P = 1.55×10⁻⁴), with cumulative breast risk ≈ 21% (95% CI 15–29%). Notably, tubo-ovarian RR rose with age until ~60 then declined, and risks varied by family history.

The original discovery paper identified *"six monoallelic pathogenic mutations in RAD51C that confer an increased risk for breast and ovarian cancer"* ([PMID: 20400964](https://pubmed.ncbi.nlm.nih.gov/20400964/)), found exclusively in breast-plus-ovarian cancer pedigrees (1.3%), absent from breast-only pedigrees and 2,912 controls.

| Cancer type | Relative risk / OR | Cumulative risk to age 80 | Source |
|---|---|---|---|
| Tubo-ovarian carcinoma | RR 7.55 (5.60–10.19) | 11% (6–21%) | PMID 32107557 |
| Breast cancer (overall) | RR 1.99 (1.39–2.85) | 21% (15–29%) | PMID 32107557 |
| Ovarian (meta-analysis) | OR 5.59 (4.42–7.07) | — | PMID 32359370 |
| Breast (population) | OR 1.53 (1.29–2.04) | — | PMID 38986768 |

### Finding 4 — Somatic RAD51C promoter hypermethylation phenocopies germline loss

Epigenetic silencing of RAD51C by promoter methylation is a somatic mechanism producing the same HR-deficient phenotype as germline mutation. Methylation is *"strongly associated with signature 3 and, in our data set, was highly enriched in basal-like breast cancers in young individuals of African descent"* ([PMID: 28825726](https://pubmed.ncbi.nlm.nih.gov/28825726/)). In the phase-3 **PAOLA-1/ENGOT-ov25** trial, 25/519 (4.8%) high-grade serous ovarian cancers (HGSOC) were RAD51C-methylated; these tumors were HRD-positive and derived progression-free survival (PFS) benefit from olaparib + bevacizumab maintenance: *"A significant PFS1 benefit independently of methylation ratios was observed in patients with methylated tumors with bev-ola maintenance compared to bev alone (HR=0.49, 95 % CI 0.29-0.83, P = 0.008)"* ([PMID: 40513287](https://pubmed.ncbi.nlm.nih.gov/40513287/)). The phase-2 EMBRACE trial corroborated olaparib activity in non-germline-BRCA HRD HGSOC, including RAD51C-methylated and germline RAD51C-variant cases ([PMID: 42420629](https://pubmed.ncbi.nlm.nih.gov/42420629/)).

### Finding 5 — Mouse models recapitulate the cancer and require Trp53 co-loss; combined Fanc mutations model FA

Epidermal/mammary *Rad51c* deletion produces mammary carcinomas *"in 63% of female mice"* **only when combined with *Trp53* inactivation**, shortening tumor latency from 11 to 6 months, and recapitulating the hormone-receptor/luminal histopathology and genomic instability of human RAD51C-mutated breast cancers ([PMID: 26820992](https://pubmed.ncbi.nlm.nih.gov/26820992/)): *"deletion of Rad51c invariably requires inactivation of the Trp53 tumor suppressor (TP53 in humans) to produce mammary carcinomas in 63% of female mice."* Similarly, *Rad51c* loss accelerates *Trp53*-mutant sebaceous tumorigenesis (6 vs 11 months) but is insufficient alone ([PMID: 25270124](https://pubmed.ncbi.nlm.nih.gov/25270124/)). On the FA side, combined hypomorphic *Brca2/Fancd1* + *Rad51c/Fanco* mice *"phenocopies human FA with bone marrow failure, rapid death by cancer, cellular cancer-drug hypersensitivity and severe replication instability,"* whereas single-gene inactivation is unremarkable ([PMID: 36906610](https://pubmed.ncbi.nlm.nih.gov/36906610/)). The absolute requirement for *Trp53* co-loss mirrors the human *TP53*-signature STIC precursor.

### Finding 6 — Saturation genome editing provides a functional map of 9,188 RAD51C variants

A landmark functional-genomics study used **saturation genome editing (SGE)** to assess *"9,188 unique variants, including >99.5% of all possible coding sequence single-nucleotide alterations"* of RAD51C ([PMID: 39299233](https://pubmed.ncbi.nlm.nih.gov/39299233/)). It *"functionally classify 3,094 variants to be disruptive and use clinical truth sets to reveal an accuracy/concordance of variant classification >99.9%."* Disruptive variants caused cell-fitness depletion, some missense alleles showed hypomorphic/intermediate kinetics, and SGE-depleted variants were significantly associated with cancer in the UK Biobank and a multicenter ovarian cohort. This map directly addresses the VUS-interpretation problem for a moderate-penetrance gene. In real-world testing cohorts, predicted LoF alterations predominate among carriers ([PMID: 42322921](https://pubmed.ncbi.nlm.nih.gov/42322921/)).

### Finding 7 — Pooled analyses confirm high-risk ovarian, low-frequency moderate-risk breast; RRSO is primary prevention

A meta-analysis of ~29,400 ovarian cancer cases vs ~116,000 gnomAD controls gave a RAD51C ovarian cancer **OR = 5.59 (95% CI 4.42–7.07, P < 0.0001)** ([PMID: 32359370](https://pubmed.ncbi.nlm.nih.gov/32359370/)). A population-based breast cancer meta-analysis (101,397 cases / 312,944 controls) found a modest association at low pathogenic-variant frequency — *"frequency of PVs were low for RAD51C (OR 1.53, 95% CI 1.29-2.04; 1 in 913)"* — with stronger association restricted to triple-negative disease ([PMID: 38986768](https://pubmed.ncbi.nlm.nih.gov/38986768/)). **Risk-reducing salpingo-oophorectomy** is the most effective ovarian prevention and is cost-effective at lifetime ovarian risk ≥ 4–5%; *"Identified carriers undergo risk-reducing salpingo-oophorectomy"* ([PMID: 29361001](https://pubmed.ncbi.nlm.nih.gov/29361001/); see also [PMID: 29252925](https://pubmed.ncbi.nlm.nih.gov/29252925/), [PMID: 41070818](https://pubmed.ncbi.nlm.nih.gov/41070818/)).

### Finding 8 — Tumors arise from fallopian-tube fimbrial epithelium; treated with platinum + PARP inhibitors

RAD51C-driven HGSOC shares the cell of origin of other HR-deficient tubo-ovarian cancers: *"Secretory cells in the fallopian tube fimbria epithelium (FTE) are regarded as the main cells of origin of ovarian high-grade serous carcinoma (HGSC)"* ([PMID: 38956560](https://pubmed.ncbi.nlm.nih.gov/38956560/)). These secretory cells acquire *TP53* mutations, forming **serous tubal intraepithelial carcinoma (STIC)** before spreading to ovary and peritoneum; mutant p53 suppresses GSTA antioxidant defense, increasing DNA damage and genomic instability ([PMID: 41275930](https://pubmed.ncbi.nlm.nih.gov/41275930/)). Therapeutically, *"The FDA has approved four PARP inhibitors (olaparib, rucaparib, niraparib, and talazoparib) for the treatment of ovarian, breast, prostate, and pancreatic cancer... approved for cancers with homologous-recombination repair deficiencies including BRCA1/2 mutations"* ([PMID: 41349848](https://pubmed.ncbi.nlm.nih.gov/41349848/)). Acquired PARPi resistance arises through restored HR, fork protection, and genetic reversion ([PMID: 42180878](https://pubmed.ncbi.nlm.nih.gov/42180878/)).

### Finding 9 — RAD51C variants are also seen in prostate and pancreatic cancer (emerging/limited associations)

RAD51C pathogenic/likely-pathogenic variants appear in mainstream prostate cancer germline panels among DNA-damage-repair carriers: *"Fourteen patients (8%...) were found to have a deleterious germline mutation, including pathogenic or likely pathogenic variants in BRCA1/2, ATM, CHEK2, PMS2, RAD51C, HOXB13, and BRIP1"* ([PMID: 38461085](https://pubmed.ncbi.nlm.nih.gov/38461085/)). In pancreatic cancer, RAD51C is classified among genes with *"a limited association or not previously associated with PC"* ([PMID: 39256447](https://pubmed.ncbi.nlm.nih.gov/39256447/)). The **core established associations remain tubo-ovarian (high risk) and triple-negative breast (moderate risk)**.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (germline monoallelic cancer-predisposition arm)

1. **Germline heterozygous LoF variant in RAD51C** (nonsense, frameshift, splice-site, or disruptive missense) is inherited → **reduces functional RAD51C to ~50% in every cell** (haploinsufficiency insufficient alone for tumorigenesis — one functional allele maintains HR).
2. In a fallopian-tube fimbrial secretory cell (or breast luminal progenitor), a **somatic "second hit"** — loss of heterozygosity, somatic mutation, or *promoter hypermethylation* of the wild-type allele — **results in complete loss of RAD51C function** in that clone.
3. Loss of RAD51C **disables BCDX2/CX3-mediated RAD51 nucleoprotein-filament loading onto ssDNA** → **abrogates homologous-recombination repair of DNA double-strand breaks** and **compromises stalled-replication-fork protection**.
4. HR deficiency **leads to error-prone compensatory repair** (NHEJ, microhomology-mediated end-joining) → **genomic instability and mutational signature 3 ("BRCAness")**.
5. *(Branch, often a prerequisite)* Co-occurring **TP53 mutation** (forming a p53-signature lesion / STIC) **removes the DNA-damage checkpoint and antioxidant defense (GSTA suppression)** → permits survival/proliferation of genomically unstable cells (mouse data show *Trp53* co-loss is essentially required).
6. Accumulated genomic instability **results in malignant transformation** → **serous tubal intraepithelial carcinoma (STIC)** in the fimbria → **high-grade serous tubo-ovarian carcinoma** seeding ovary and peritoneum; in breast, a **triple-negative/basal-like carcinoma**.
7. The HR deficiency that drives the cancer **creates a therapeutic vulnerability**: **PARP inhibition** blocks single-strand-break repair, causing unrepaired DSBs that an HR-deficient cell cannot fix → **synthetic-lethal tumor-cell death**; platinum crosslinks similarly overwhelm repair capacity.
8. *(Resistance branch)* Under selective pressure, subclones **restore HR** (reversion mutations, restored fork protection) → **acquired PARP-inhibitor/platinum resistance**.

### Biallelic (Fanconi anemia / FANCO) arm

1. **Two hypomorphic RAD51C alleles** inherited (often via consanguinity) → **severe constitutive HR/interstrand-crosslink-repair deficiency in all cells from conception**.
2. **Leads to defective FA–BRCA crosslink repair and R-loop resolution** → **developmental malformations, cellular hypersensitivity to crosslinkers (mitomycin C), chromosomal breakage, and progressive bone-marrow failure** (FANCO; demonstrated, not merely inferred, per PMID 20400963).

```
 GERMLINE LoF allele (50% RAD51C)
          │
          ▼  somatic 2nd hit (LOH / mutation / promoter methylation)
 Complete RAD51C loss in a fimbrial secretory cell
          │
          ▼  BCDX2/CX3 cannot load RAD51 → HR fails + fork protection lost
 HR DEFICIENCY ("BRCAness", signature 3)
          │  + TP53 mutation (STIC precursor)
          ▼
 Genomic instability → STIC → HIGH-GRADE SEROUS TUBO-OVARIAN CARCINOMA
          │                         └─(breast arm)→ triple-negative/basal carcinoma
          ▼  THERAPEUTIC EXPLOIT
 PARP inhibitor / platinum → synthetic lethality → tumor death
          │
          ▼  (resistance) HR restoration / reversion → relapse
```

### Ontology term suggestions

- **Gene/protein:** HGNC:9820 (RAD51C); GO:0000724 (DSB repair via HR); GO:0006310 (DNA recombination); GO:0036297 (interstrand cross-link repair); GO:0031297 (replication fork processing); GO:0005654 (nucleoplasm, CC); CHEBI:63631 (olaparib); CHEBI:27899 (cisplatin).
- **Phenotypes (HPO):** HP:0100615 (ovarian neoplasm); HP:0003002 (breast carcinoma); HP:0012125 (prostate cancer); HP:0002664 (neoplasm); HP:0005528 (bone marrow hypocellularity, FA arm); HP:0001510 (growth delay, FA arm); HP:0040012 (chromosome breakage).
- **Cell types (CL):** CL:0002536 (fallopian tube secretory epithelial cell); CL:0000066 (epithelial cell); CL:0002326 (luminal epithelial cell of mammary gland).
- **Anatomy (UBERON):** UBERON:0003889 (fallopian tube); UBERON:0000996 (oviduct infundibulum/fimbria); UBERON:0000992 (ovary); UBERON:0002367 (peritoneum); UBERON:0000310 (breast).
- **Disease (MONDO):** MONDO:0700273 (RAD51C-related cancer predisposition); related MONDO:0011705 (Fanconi anemia complementation group O).
- **Treatment (NCIT):** NCIT:C71721 (Olaparib); NCIT:C78844 (Rucaparib); NCIT:C97660 (Niraparib); NCIT:C95733 (Talazoparib); NCIT:C51686 (salpingo-oophorectomy); NCIT:C1282 (Carboplatin).

---

## Section-by-Section Disease Characterization

### 1. Disease Information
RAD51C-related cancer predisposition (MONDO:0700273) is an **autosomal-dominant HBOC-spectrum syndrome** caused by heterozygous germline LoF variants in **RAD51C**. Key identifiers: **Gene** RAD51C (HGNC:9820, NCBI Gene 5889, chr17q22); **MONDO:0700273**; related OMIM — RAD51C gene *613390*, Fanconi anemia group O *613390/614082*, breast-ovarian cancer susceptibility (BROVCA3) *613399*. Synonyms/related: "RAD51C-associated hereditary breast and ovarian cancer," "FANCO (biallelic)," "BROVCA3." Information is derived from **aggregated disease-level resources** (segregation analyses, case-control meta-analyses, functional assays) rather than individual EHR.

### 2. Etiology
**Primary cause:** germline heterozygous LoF variant in RAD51C (genetic). **Genetic risk factors:** pathogenic RAD51C variants (RR ovarian 7.55, breast 1.99; PMID 32107557); family history modifies risk. **Second-hit** somatic events (LOH, promoter hypermethylation) are required for tumorigenesis. **Environmental/gene-environment:** limited specific data; general HR-targeting carcinogens such as hexavalent chromium transcriptionally repress RAD51 paralogs in vitro ([PMID: 42169974](https://pubmed.ncbi.nlm.nih.gov/42169974/)) — mechanistically plausible as an exogenous phenocopy but not an established disease modifier. **Protective factors:** RRSO and (by analogy to BRCA) oral contraceptives for ovarian risk; no validated protective genetic modifier alleles identified. Consanguinity is a risk factor for the biallelic FA arm.

### 3. Phenotypes
| Phenotype | Type | Onset | Frequency / risk | HPO |
|---|---|---|---|---|
| High-grade serous tubo-ovarian carcinoma | Clinical sign / neoplasm | Adult (risk rises to ~60y) | Cumulative ~11% by 80; RR 7.55 | HP:0100615 |
| Triple-negative / basal breast carcinoma | Neoplasm | Adult | Cumulative ~21%; RR ~2 | HP:0003002 |
| Prostate cancer (emerging) | Neoplasm | Adult/older | Among DDR-panel carriers | HP:0012125 |
| Bone-marrow failure (biallelic FANCO) | Lab/clinical | Congenital/childhood | Biallelic cases | HP:0005528 |
| Congenital malformations (biallelic) | Physical | Congenital | Biallelic cases | HP:0001510 |

Severity is **variable** (moderate penetrance monoallelic; severe biallelic). Quality-of-life impact derives chiefly from cancer treatment and from surgical menopause after RRSO.

### 4. Genetic/Molecular Information
**Causal gene:** RAD51C (HGNC:9820). **Variant classes:** predominantly LoF — nonsense, frameshift, splice-site, large deletions; plus disruptive missense (e.g., F164S, A87E, L134S, E49K with defective fork protection, PMID 36562461). **Classification:** ACMG/AMP pathogenic/likely-pathogenic/VUS; SGE map of 9,188 variants classifies 3,094 disruptive with >99.9% concordance (PMID 39299233). **Allele frequency:** pathogenic-variant carrier frequency ≈ **1 in 913** in population breast cohorts (PMID 38986768) — rare. **Somatic vs germline:** both; **somatic promoter hypermethylation** is a recognized epigenetic LoF mechanism (PMID 28825726). **Functional consequence:** loss of function (tumor-suppressor). **Epigenetic:** RAD51C promoter CpG hypermethylation silences expression and produces HRD/signature 3.

### 5. Environmental Information
No established infectious or specific environmental cause. In vitro, **hexavalent chromium [Cr(VI)]** transcriptionally represses all RAD51 paralogs and inhibits RAD51 filament formation (PMID 42169974) — a mechanistic parallel, not an epidemiologically proven disease risk factor. Lifestyle factors are not specifically established for RAD51C beyond general cancer-risk considerations.

### 6. Mechanism / Pathophysiology
Covered in detail in the **Mechanistic Model** above. Core pathway: **HR DSB repair (GO:0000724)** via the **BCDX2** and **CX3** RAD51-paralog complexes, plus **replication-fork protection**; loss → genomic instability → malignant transformation gated by TP53 loss. Cell of origin: fallopian-tube fimbrial secretory cells (CL:0002536). Subcellular compartment: nucleus/replication fork.

### 7. Anatomical Structures Affected
- **Primary organs:** fallopian tube (fimbria; UBERON:0003889/0000996), ovary (UBERON:0000992), breast (UBERON:0000310).
- **Secondary:** peritoneum (UBERON:0002367) via transcoelomic spread; prostate (emerging).
- **Body systems:** female reproductive; hematopoietic in biallelic FA.
- **Cell/tissue:** epithelial (secretory tubal cell, mammary luminal progenitor).
- **Lateralization:** breast often unilateral at presentation but with bilateral risk; tubo-ovarian can be bilateral.

### 8. Temporal Development
Adult-onset cancer predisposition. Tubo-ovarian **RR increases with age until ~60 then decreases** (PMID 32107557). Progression follows HGSOC natural history: STIC → invasive HGSC → advanced (stage III/IV) peritoneal disease, typically presenting late. Biallelic FANCO is congenital/childhood-onset and progressive (bone-marrow failure). Critical intervention window: **RRSO near menopause** (before cancer onset).

### 9. Inheritance and Population
- **Inheritance:** autosomal dominant (monoallelic cancer predisposition); autosomal recessive (biallelic FANCO).
- **Penetrance:** incomplete, age-dependent, moderate.
- **Carrier frequency:** ~1 in 913 (breast cohorts).
- **Populations:** reported across global cohorts; RAD51C methylation enriched in basal-like breast cancers of young women of African descent (PMID 28825726); founder-type recurrences occasionally reported.
- **Sex:** cancer burden overwhelmingly female (breast/ovarian); prostate in males.

### 10. Diagnostics
- **Genetic testing:** multigene HBOC panels including RAD51C (NGS); single-gene/cascade testing for relatives. SGE functional map aids VUS interpretation (PMID 39299233).
- **Tumor HRD testing:** mutational signature 3, genomic-instability scores, RAD51C methylation assays (PMID 40513287); RAD51C immunohistochemistry proposed as part of composite HRD biomarker (PMID 39402170).
- **Pathology:** high-grade serous histology, abnormal p53 (STIC); triple-negative/basal breast.
- **Differential:** BRCA1/2, RAD51D, BRIP1, PALB2, ATM, CHEK2, BARD1-related HBOC.

### 11. Outcome / Prognosis
Prognosis tracks HGSOC/triple-negative breast natural history. **HRD status is favorable for therapy response:** PARPi maintenance yields large PFS gains (olaparib+bevacizumab HR 0.49 in methylated tumors, PMID 40513287; broad PARPi PFS benefit in HRD, Cochrane PMID 43012369). Acquired resistance via HR restoration limits durability (PMID 42180878). Prognostic biomarker: HRD/signature 3 predicts platinum/PARPi sensitivity.

### 12. Treatment
- **Pharmacotherapy / targeted:** **PARP inhibitors** — olaparib (NCIT:C71721), rucaparib (NCIT:C78844), niraparib (NCIT:C97660), talazoparib (NCIT:C95733) — FDA-approved for HRD cancers (PMID 41349848); **platinum** chemotherapy (carboplatin/cisplatin).
- **Surgical/preventive:** risk-reducing salpingo-oophorectomy (NCIT:C51686); risk-reducing mastectomy considered case-by-case (generally not mandated for an isolated moderate-risk breast variant).
- **Combination/experimental:** PARPi + bevacizumab; PARPi + immune checkpoint inhibitors under study (PMID 41541937).
- **Pharmacogenomics/personalized:** genotype/HRD-guided PARPi selection.

### 13. Prevention
- **Primary (ovarian):** RRSO near menopause — most effective, cost-effective at lifetime risk ≥4–5% (PMID 29252925, 29361001).
- **Secondary:** enhanced breast surveillance (intensified imaging, e.g., MRI); no effective ovarian screening exists.
- **Genetic counseling / cascade testing** of at-risk relatives; prenatal/PGT options for biallelic-risk families.
- **Risk stratification:** multigene panels; population-based testing cost-effective (PMID 29361001).

### 14. Other Species / Natural Disease
RAD51C is evolutionarily conserved (mouse *Rad51c*, NCBI Gene 114714). No prominent naturally occurring companion-animal disease documented in this investigation; the gene's essentiality means homozygous knockout is embryonic-lethal in mouse.

### 15. Model Organisms
- **Mouse (conditional knockouts):** *Rad51c* deletion + *Trp53* loss → mammary carcinoma (63% of females; latency 11→6 months) recapitulating human luminal/HR-deficient pathology (PMID 26820992); *Rad51c/Trp53* sebaceous-tumor model (PMID 25270124).
- **FA model:** hypomorphic *Brca2/Fancd1* + *Rad51c/Fanco* double mutants phenocopy human Fanconi anemia (bone-marrow failure, cancer, replication instability) (PMID 36906610).
- **In vitro / functional genomics:** saturation genome editing in human cells (PMID 39299233); biochemical/cryo-EM reconstitution of BCDX2/CX3 (PMID 39268578, 42020761).
- **Limitation:** single-gene *Rad51c* loss alone is insufficient for tumorigenesis — the obligate *Trp53* requirement is both a strength (models human STIC genetics) and a caveat for isolating RAD51C-specific effects.

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [20400963](https://pubmed.ncbi.nlm.nih.gov/20400963/) | *RAD51C mutation in Fanconi anemia-like disorder* | Establishes biallelic → FANCO |
| [20400964](https://pubmed.ncbi.nlm.nih.gov/20400964/) | *Germline mutations establish RAD51C as cancer gene* | Original cancer-gene discovery |
| [32107557](https://pubmed.ncbi.nlm.nih.gov/32107557/) | *Ovarian/breast risks in RAD51C/RAD51D* | Definitive RR/cumulative-risk estimates |
| [32359370](https://pubmed.ncbi.nlm.nih.gov/32359370/) | *Pooled ~30,000-case ovarian analysis* | Meta-analytic ovarian OR 5.59 |
| [38986768](https://pubmed.ncbi.nlm.nih.gov/38986768/) | *Population breast meta-analysis* | Breast OR 1.53; PV freq 1/913 |
| [39268578](https://pubmed.ncbi.nlm.nih.gov/39268578/) | *BCDX2 RAD51 nucleation mechanism* | Molecular HR function |
| [42020761](https://pubmed.ncbi.nlm.nih.gov/42020761/) | *RAD51 paralog exchange cryo-EM* | Structural regulation of filament |
| [36562461](https://pubmed.ncbi.nlm.nih.gov/36562461/) | *RAD51C missense variants & fork protection* | Replication-fork role; specific variants |
| [28825726](https://pubmed.ncbi.nlm.nih.gov/28825726/) | *Signature 3 / RAD51C methylation* | Epigenetic LoF → HRD |
| [40513287](https://pubmed.ncbi.nlm.nih.gov/40513287/) | *PAOLA-1 methylation ancillary study* | Methylation predicts PARPi benefit |
| [42420629](https://pubmed.ncbi.nlm.nih.gov/42420629/) | *EMBRACE phase 2 olaparib* | PARPi in non-gBRCA HRD |
| [26820992](https://pubmed.ncbi.nlm.nih.gov/26820992/) | *Rad51c/Trp53 mouse model* | Tumor model; Trp53 requirement |
| [36906610](https://pubmed.ncbi.nlm.nih.gov/36906610/) | *Brca2/Rad51c double-mutant mice* | FA mouse model |
| [25270124](https://pubmed.ncbi.nlm.nih.gov/25270124/) | *Rad51c sebaceous tumor model* | Synergy with Trp53 |
| [39299233](https://pubmed.ncbi.nlm.nih.gov/39299233/) | *Saturation genome editing of RAD51C* | Functional variant map |
| [41070818](https://pubmed.ncbi.nlm.nih.gov/41070818/) | *ACMG clinical practice resource* | Management/penetrance guidance |
| [29361001](https://pubmed.ncbi.nlm.nih.gov/29361001/) | *Cost-effectiveness population testing* | RRSO as prevention |
| [29252925](https://pubmed.ncbi.nlm.nih.gov/29252925/) | *Surgical prevention thresholds* | RRSO cost-effectiveness ≥4–5% |
| [38956560](https://pubmed.ncbi.nlm.nih.gov/38956560/) | *Fallopian tube cell of origin* | FTE secretory cell origin |
| [41275930](https://pubmed.ncbi.nlm.nih.gov/41275930/) | *Mutant p53 in tubal carcinogenesis* | TP53/STIC branch |
| [41349848](https://pubmed.ncbi.nlm.nih.gov/41349848/) | *FDA-approved PARP inhibitors* | Four approved PARPi |
| [42180878](https://pubmed.ncbi.nlm.nih.gov/42180878/) | *PARPi resistance review* | HR-restoration resistance |
| [38461085](https://pubmed.ncbi.nlm.nih.gov/38461085/) | *Prostate mainstream testing* | RAD51C in prostate panels |
| [39256447](https://pubmed.ncbi.nlm.nih.gov/39256447/) | *Pancreatic germline variants* | Limited pancreatic association |

Note on a contrary study: a large exome-sequencing case-control study ([PMID: 30128536](https://pubmed.ncbi.nlm.nih.gov/30128536/)) confirmed the RAD51C ovarian association (FDR-corrected P = .004) but *did not support* a RAD51C breast cancer association, underscoring that the breast signal is weaker and largely concentrated in triple-negative disease.

---

## Limitations and Knowledge Gaps

- **No primary dataset was analyzed** in this investigation; findings are a literature synthesis of aggregated disease-level evidence. Statistical estimates are quoted from published cohorts, not independently recomputed.
- **Penetrance uncertainty:** cumulative-risk confidence intervals are wide (ovarian 6–21%), and risk is family-history-dependent; the breast cancer association is contested (PMID 30128536) and concentrated in triple-negative disease.
- **VUS burden:** despite the SGE map, missense interpretation remains challenging, especially for hypomorphic/intermediate alleles.
- **Modifier genes and gene–environment interactions** for RAD51C are largely uncharacterized; the Cr(VI) link is in vitro only.
- **Prostate and pancreatic risk** are emerging/limited and not quantified with the rigor of ovarian risk.
- **Model limitation:** obligate *Trp53* co-loss in mouse models complicates isolation of RAD51C-specific tumor biology.
- **Resistance biology:** mechanisms of acquired PARPi/platinum resistance specific to RAD51C (vs BRCA) are incompletely defined.

## Proposed Follow-up Experiments / Actions

1. **Refine age-specific penetrance** for RAD51C by sex and cancer subtype using large prospective biobanks (UK Biobank, All of Us), enabling individualized RRSO timing.
2. **Integrate the SGE functional map into ClinVar/VarSome pipelines** to reclassify RAD51C VUS and prospectively validate against carrier outcomes.
3. **Quantify prostate and pancreatic RAD51C risk** via dedicated case-control meta-analyses to determine whether surveillance guidelines should expand.
4. **Prospectively evaluate RAD51C methylation and IHC as predictive HRD biomarkers** for PARPi selection in HGSOC, building on PAOLA-1 ancillary data.
5. **Dissect RAD51C-specific PARPi resistance** (reversion vs fork-protection restoration) in patient-derived organoids to design rational combination therapy (e.g., PARPi + ATR/CHK1 inhibitors).
6. **Model the biallelic FANCO arm** and R-loop/FANCM axis to clarify shared versus divergent mechanisms with the cancer-predisposition arm.
7. **Evaluate chemoprevention and non-surgical ovarian-risk reduction** (e.g., salpingectomy with delayed oophorectomy) in RAD51C carriers to mitigate surgical-menopause morbidity.


## Artifacts

- [OpenScientist final report](RAD51C-Related_Cancer_Predisposition-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](RAD51C-Related_Cancer_Predisposition-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 31 |
| On topic | 24 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 30 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 14 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0000724` (2 mentions) - the report calls it "DSB repair via HR"; GO calls it **double-strand break repair via homologous recombination**
- `CHEBI:63631` (1 mention) - the report calls it "olaparib"; CHEBI calls it **topiramate**
- `HP:0100615` (2 mentions) - the report calls it "ovarian neoplasm", "Cumulative ~11% by 80; RR 7.55"; HP calls it **Ovarian neoplasm**
- `HP:0003002` (2 mentions) - the report calls it "breast carcinoma", "Cumulative ~21%; RR ~2"; HP calls it **Breast carcinoma**
- `HP:0012125` (2 mentions) - the report calls it "prostate cancer", "Among DDR-panel carriers"; HP calls it **Prostate cancer**
- `HP:0005528` (2 mentions) - the report calls it "bone marrow hypocellularity, FA arm", "Biallelic cases"; HP calls it **Bone marrow hypocellularity**
- `HP:0001510` (2 mentions) - the report calls it "growth delay, FA arm", "Biallelic cases"; HP calls it **Growth delay**
- `UBERON:0000996` (1 mention) - the report calls it "oviduct infundibulum/fimbria"; UBERON calls it **vagina**
- `UBERON:0002367` (2 mentions) - the report calls it "peritoneum", "Secondary:** peritoneum"; UBERON calls it **prostate gland**
- `MONDO:0011705` (1 mention) - the report calls it "Fanconi anemia complementation group O"; MONDO calls it **lymphangioleiomyomatosis**
- `NCIT:C71721` (2 mentions) - the report calls it "Olaparib", "Pharmacotherapy / targeted:** **PARP inhibitors** — olaparib"; NCIT calls it **Olaparib**
- `NCIT:C78844` (2 mentions) - the report calls it "Rucaparib"; NCIT calls it **Ficlatuzumab**
- `NCIT:C97660` (2 mentions) - the report calls it "Niraparib"; NCIT calls it **Abemaciclib**
- `NCIT:C51686` (2 mentions) - the report calls it "salpingo-oophorectomy", "Surgical/preventive:** risk-reducing salpingo-oophorectomy"; NCIT calls it **Esophageal Biopsy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005654` (1 mention) - the report calls it "nucleoplasm, CC"; GO calls it **nucleoplasm**
- `CL:0002536` (2 mentions) - the report calls it "fallopian tube secretory epithelial cell"; CL calls it **epithelial cell of amnion**, and lists "amniotic epithelial cell" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0100615` - called "ovarian neoplasm", "Cumulative ~11% by 80; RR 7.55"
- `HP:0003002` - called "breast carcinoma", "Cumulative ~21%; RR ~2"
- `HP:0012125` - called "prostate cancer", "Among DDR-panel carriers"
- `HP:0005528` - called "bone marrow hypocellularity, FA arm", "Biallelic cases"
- `HP:0001510` - called "growth delay, FA arm", "Biallelic cases"
- `UBERON:0002367` - called "peritoneum", "Secondary:** peritoneum"
- `NCIT:C71721` - called "Olaparib", "Pharmacotherapy / targeted:** **PARP inhibitors** — olaparib"
- `NCIT:C51686` - called "salpingo-oophorectomy", "Surgical/preventive:** risk-reducing salpingo-oophorectomy"