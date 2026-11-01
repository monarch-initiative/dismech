---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T14:00:13.385639'
end_time: '2026-10-31T14:20:03.478700'
duration_seconds: 1190.09
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Renal Hypomagnesemia 2
  mondo_id: MONDO:0007937
  category: Mendelian
  causal_genes: FXYD2
  omim_id: OMIM:154020
  synonyms: familial primary hypomagnesemia caused by mutation in FXYD2; FXYD2 familial
    primary hypomagnesemia; FXYD2 primary hypomagnesemia; HOMG2; isolated autosomal
    dominant hypomagnesemia; isolated renal magnesium wasting; primary hypomagnesemia
    caused by mutation in FXYD2; renal hypomagnesemia type 2
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
citation_count: 13
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 10
  off_topic: 1
  off_topic_references:
  - PMID:11278761
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 20
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 4
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0007937
    reported_labels:
    - MONDO
    ontology_label: renal hypomagnesemia 2
  - term_id: HP:0002917
    reported_labels:
    - Lab abnormality
    ontology_label: Hypomagnesemia
  - term_id: HP:0003127
    reported_labels:
    - Lab abnormality
    ontology_label: Hypocalciuria
  - term_id: HP:0000934
    reported_labels:
    - Physical/imaging
    ontology_label: Chondrocalcinosis
  - term_id: HP:0001250
    reported_labels:
    - Clinical sign
    ontology_label: Seizure
  - term_id: HP:0003394
    reported_labels:
    - Symptom
    ontology_label: Muscle spasm
  - term_id: HP:0001281
    reported_labels:
    - Clinical sign
    ontology_label: Tetany
  - term_id: HP:0012605
    reported_labels:
    - Lab/physiologic
    ontology_label: Hypernatriuria
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Renal_Hypomagnesemia_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Renal_Hypomagnesemia_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Renal Hypomagnesemia 2
- **MONDO ID:** MONDO:0007937 (if available)
- **Causal gene(s):** FXYD2
- **OMIM:** OMIM:154020
- **Synonyms:** familial primary hypomagnesemia caused by mutation in FXYD2; FXYD2 familial primary hypomagnesemia; FXYD2 primary hypomagnesemia; HOMG2; isolated autosomal dominant hypomagnesemia; isolated renal magnesium wasting; primary hypomagnesemia caused by mutation in FXYD2; renal hypomagnesemia type 2
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Renal Hypomagnesemia 2** covering all of the
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

# Renal Hypomagnesemia 2 (HOMG2 / Isolated Dominant Hypomagnesemia): Comprehensive Disease Characterization

**Disease:** Renal Hypomagnesemia 2 (HOMG2) — Isolated Dominant Hypomagnesemia with Hypocalciuria (IDH)
**MONDO ID:** MONDO:0007937 · **OMIM:** #154020 · **Causal gene:** **FXYD2** (Na⁺,K⁺-ATPase γ-subunit)

---

## Summary

**Renal Hypomagnesemia 2 is an autosomal dominant renal tubulopathy caused by the gene *FXYD2*, which encodes the γ (gamma) regulatory subunit of the Na⁺,K⁺-ATPase.** To date, essentially a single recurrent heterozygous missense allele — **c.121G>A, p.Gly41Arg (G41R)** — accounts for all genetically resolved cases. The disease is defined biochemically by isolated renal magnesium wasting producing hypomagnesemia (serum Mg²⁺ < 0.7 mmol/L), accompanied by paradoxically low urinary calcium excretion (hypocalciuria). Clinically it manifests with neuromuscular irritability (muscle cramps, tetany), seizures/convulsions, and, in longstanding cases, chondrocalcinosis. The term "renal hypomagnesemia **2**" is a serial numbering within the OMIM family of primary hypomagnesemias; the gene it refers to is unambiguously *FXYD2*, distinguishing it from TRPM6-, CLDN16-, CNNM2-, and HNF1B-related hypomagnesemias.

Mechanistically, G41R acts primarily through a **dominant-negative** effect. The mutant γ-subunit is incorrectly folded/routed and accumulates in perinuclear (ER/Golgi) compartments rather than reaching the basolateral plasma membrane of the distal convoluted tubule (DCT). Because FXYD2 oligomerizes, the mutant hetero-oligomerizes with wild-type γ-subunit and traps it intracellularly, abrogating its normal routing and glycosylation. The net result is loss of functional γ-subunit at the DCT basolateral membrane, impairing Na⁺,K⁺-ATPase-dependent transcellular Mg²⁺ reabsorption. Haploinsufficiency was formally excluded (individuals with a single *FXYD2* copy have normal serum Mg²⁺), confirming that the dominant phenotype requires the poisoning of wild-type protein by the mutant. A secondary, complementary **gain-of-function** branch has also been demonstrated: the fraction of G41R protein that does reach the membrane behaves as an aberrant inward-rectifying nonselective cation channel.

The condition is **ultra-rare**; the G41R allele arose on a shared haplotype in Dutch kindreds (founder effect) and has recurred in a small number of additional families. Importantly, the broader clinical picture of "isolated renal Mg wasting" is **genetically heterogeneous** — an American family with a clinically similar phenotype did not link to the *FXYD2* locus at 11q23, demonstrating that not all isolated renal magnesium wasting is FXYD2-related. Management is lifelong oral/parenteral magnesium supplementation; life expectancy is normal. This report synthesizes six confirmed findings across 19 reviewed papers and maps the causal chain from mutation to clinical manifestation.

---

## Key Findings

### Finding 1 — HOMG2 is caused by the recurrent *FXYD2* p.Gly41Arg mutation

Linkage analysis in a large Dutch family mapped the disease trait to chromosome **11q23** within a ~5.6-cM region. Within this interval, a heterozygous mutation **c.121G>A** in *FXYD2* — producing the amino acid substitution **p.Gly41Arg** — cosegregated with all affected family members and was absent from 132 control chromosomes ([PMID: 12763862](https://pubmed.ncbi.nlm.nih.gov/12763862/); [PMID: 11062458](https://pubmed.ncbi.nlm.nih.gov/11062458/)). The same mutation was subsequently found to recur in two additional families with isolated dominant hypomagnesemia and hypocalciuria, with haplotype analysis revealing an **overlapping haplotype indicating a founder effect** ([PMID: 25765846](https://pubmed.ncbi.nlm.nih.gov/25765846/)).

> *"we identified a heterozygous mutation in the FXYD2 gene, encoding the Na(+),K(+)-ATPase gamma-subunit, cosegregating with the patients of this family, which was not found in 132 control chromosomes. The mutation leads to a G41R substitution"* — [PMID: 12763862](https://pubmed.ncbi.nlm.nih.gov/12763862/)

> *"We report a p.Gly41Arg FXYD2 mutation in two families with hypomagnesaemia and hypocalciuria. Interestingly, this is the same mutation as was described in the original study"* — [PMID: 25765846](https://pubmed.ncbi.nlm.nih.gov/25765846/)

Glycine 41 is a highly conserved residue within the single transmembrane span of the 65-residue γ-subunit; its substitution by the bulky, positively charged arginine is the molecular lesion underlying the disease.

### Finding 2 — The dominant-negative mechanism: mutant G41R misroutes and traps wild-type γ-subunit

Heterologous expression of the mutant γ-subunit in Sf9 and COS-1 cells demonstrated that **the mutant protein is incorrectly routed and accumulates in perinuclear structures**, lacking a post-translational modification (glycosylation) that marks correctly trafficked protein. Critically, **haploinsufficiency was excluded**: individuals carrying only a single functional *FXYD2* copy have normal serum Mg²⁺, meaning simple loss of one allele is not sufficient to cause disease — the mutant must actively interfere with the wild-type product ([PMID: 12763862](https://pubmed.ncbi.nlm.nih.gov/12763862/)).

The physical basis of this interference was established by co-immunoprecipitation showing that FXYD2 oligomerizes, and that G41R hetero-oligomerizes with wild-type γ-subunit, reducing its glycosylation and plasma-membrane routing ([PMID: 17980699](https://pubmed.ncbi.nlm.nih.gov/17980699/)). Biophysical work on synthetic transmembrane peptides confirmed that the G41R substitution **abrogates normal γ-TM oligomerization** (as does the conservative G41L substitution), whereas an arginine substitution on a different helical face (position 35) retains oligomerization — directly linking the disease to disrupted γ-subunit quaternary assembly ([PMID: 12225751](https://pubmed.ncbi.nlm.nih.gov/12225751/)).

> *"binding of FXYD2-G41R to wild type FXYD2 subunit might abrogate the routing of wild type FXYD2 to the plasma membrane thus causing the dominant nature of this mutation"* — [PMID: 17980699](https://pubmed.ncbi.nlm.nih.gov/17980699/)

> *"the mutant gamma-subunit protein was incorrectly routed and accumulated in perinuclear structures"* — [PMID: 12763862](https://pubmed.ncbi.nlm.nih.gov/12763862/)

### Finding 3 — Clinical phenotype: isolated renal Mg²⁺ wasting with hypocalciuria and neuromuscular features

Affected individuals show **serum Mg²⁺ below ~0.7 mmol/L** due to inappropriate renal magnesium wasting, together with **hypocalciuria** (low urinary calcium). The clinical spectrum includes **muscle cramps/tetany, chondrocalcinosis, and epilepsy/convulsions** ([PMID: 25765846](https://pubmed.ncbi.nlm.nih.gov/25765846/); [PMID: 12763862](https://pubmed.ncbi.nlm.nih.gov/12763862/)). The phenotype is "isolated" in that it is not accompanied by the broader electrolyte derangements (hypokalemia, metabolic alkalosis) seen in Gitelman/Bartter syndromes, nor the secondary hypocalcemia of TRPM6 disease.

> *"several patients suffered from muscle cramps, chondrocalcinosis and epilepsy"* — [PMID: 25765846](https://pubmed.ncbi.nlm.nih.gov/25765846/)

> *"These disorders share the general symptoms of hypomagnesemia, tetany and epileptiformic convulsions, and often include secondary or associated disturbances in calcium excretion"* — [PMID: 12763862](https://pubmed.ncbi.nlm.nih.gov/12763862/)

**Suggested HPO terms:** Hypomagnesemia (HP:0002917); Hypocalciuria (HP:0003127); Chondrocalcinosis (HP:0000934); Seizure (HP:0001250); Muscle cramps (HP:0003394); Tetany (HP:0001281); Renal magnesium wasting (HP:0012605).

### Finding 4 — Normal γ-subunit function: tuning Na,K-ATPase ATP/cation affinity; γa vs γb isoforms

Under normal conditions, the FXYD2 γ-subunit is a type-2 single-pass transmembrane regulator of the Na,K-ATPase. Rat kidney expresses two splice variants, **γa and γb**, differing only at the extracellular N-terminus. Functionally, the γ-subunit produces **(i) an increase in apparent affinity for ATP** (secondary to a left shift in the E1↔E2 conformational equilibrium) **and (ii) an increase in K⁺ antagonism of cytoplasmic Na⁺ activation**. The subunit localizes to the basolateral membrane of several tubule segments, most strongly in the medullary thick ascending limb and also in the DCT ([PMID: 11278761](https://pubmed.ncbi.nlm.nih.gov/11278761/)).

This normal function is woven into the broader DCT magnesium-handling network: the transcription factor **HNF1B specifically activates the γa isoform**, and *HNF1B* mutations impair γa through a dominant-negative effect, linking the HNF1B-associated hypomagnesemia syndrome to the same FXYD2 pathway ([PMID: 21130072](https://pubmed.ncbi.nlm.nih.gov/21130072/)).

> *"an increase in apparent affinity for ATP, probably secondary to a left shift in E(1) <--> E(2) conformational equilibrium and (ii) an increase in K(+) antagonism of cytoplasmic Na(+) activation"* — [PMID: 11278761](https://pubmed.ncbi.nlm.nih.gov/11278761/)

> *"HNF-1B specifically acts as an activator of the γa-subunit"* — [PMID: 21130072](https://pubmed.ncbi.nlm.nih.gov/21130072/)

### Finding 5 — Gain-of-function branch: membrane-reaching G41R acts as an inward-rectifying cation channel

Electrophysiology in *Xenopus* oocytes showed that both wild-type and G41R FXYD2 generate large nonselective ion currents, but **only G41R produces inward-rectifying cation currents upon hyperpolarization**. The rectification depended on the presence of a positive charge at residue 41, was blocked by extracellular divalent/trivalent cations (Ca²⁺, Ba²⁺, La³⁺), and was removed by intracellular EDTA ([PMID: 18448590](https://pubmed.ncbi.nlm.nih.gov/18448590/)). In MDCK renal epithelial cells, wild-type FXYD2 (but not G41R) supported a Mg²⁺-gradient-driven transepithelial current that was inhibited by basolateral Ba²⁺, supporting a physiological role for FXYD2 in basolateral Mg²⁺ extrusion.

> *"in contrast to the wild-type FXYD2 currents, inward rectifying cation currents were induced by hyperpolarization pulses in oocytes expressing the G41R mutant"* — [PMID: 18448590](https://pubmed.ncbi.nlm.nih.gov/18448590/)

> *"FXYD2 can mediate basolateral extrusion of magnesium from cultured renal epithelial cells"* — [PMID: 18448590](https://pubmed.ncbi.nlm.nih.gov/18448590/)

This establishes a **dual pathological mechanism**: dominant-negative misrouting (the dominant contributor, since most mutant protein never reaches the membrane) plus aberrant channel behavior in the residual membrane-resident fraction.

### Finding 6 — Inheritance and epidemiology: autosomal dominant, ultra-rare founder allele, with locus heterogeneity

All reported genetically resolved IDH families carry the **identical p.Gly41Arg mutation on an overlapping haplotype**, indicating a Dutch founder effect ([PMID: 25765846](https://pubmed.ncbi.nlm.nih.gov/25765846/)). The trait is autosomal dominant (OMIM #154020). Crucially, an American family with a clinically similar isolated renal Mg-wasting phenotype **did not link to 11q23** (multipoint LOD = −2.97 across five 11q23 loci), demonstrating genetic **locus heterogeneity** — i.e., the clinical phenotype of isolated renal Mg wasting is not exclusively FXYD2-mediated ([PMID: 11836293](https://pubmed.ncbi.nlm.nih.gov/11836293/)).

> *"Haplotype analysis revealed an overlapping haplotype in all families, suggesting a founder effect"* — [PMID: 25765846](https://pubmed.ncbi.nlm.nih.gov/25765846/)

> *"our data demonstrate locus heterogeneity for the phenotype of isolated renal Mg wasting with hypomagnesemia"* — [PMID: 11836293](https://pubmed.ncbi.nlm.nih.gov/11836293/)

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** Renal Hypomagnesemia 2 (HOMG2), also called **Isolated Dominant Hypomagnesemia with hypocalciuria (IDH)**, is a Mendelian autosomal dominant renal tubulopathy in which the kidney inappropriately wastes magnesium, producing chronic hypomagnesemia with low urinary calcium. It is caused by mutation in *FXYD2* (Na,K-ATPase γ-subunit).

**Key identifiers.**
| Resource | Identifier |
|---|---|
| OMIM | #154020 |
| MONDO | MONDO:0007937 |
| Orphanet | Primary hypomagnesemia / isolated dominant hypomagnesemia group |
| ICD-10 | E83.42 (Hypomagnesemia) |
| ICD-11 | 5C64.41 (Magnesium deficiency) |
| MeSH | Magnesium Deficiency / renal tubular disorders |
| Gene (HGNC) | FXYD2, HGNC:4028 |

**Synonyms:** familial primary hypomagnesemia caused by FXYD2 mutation; FXYD2 familial primary hypomagnesemia; HOMG2; isolated autosomal dominant hypomagnesemia; isolated renal magnesium wasting; renal hypomagnesemia type 2.

**Information source.** Derived predominantly from **aggregated disease-level resources** (OMIM, Orphanet) built on a small number of **individual-patient family studies** — the original Dutch kindred and ≤2 additional families. There is no large EHR-derived cohort given the ultra-rarity.

### 2. Etiology

**Primary cause — genetic.** The sole established cause is the heterozygous *FXYD2* **c.121G>A (p.Gly41Arg)** missense mutation ([PMID: 12763862](https://pubmed.ncbi.nlm.nih.gov/12763862/); [PMID: 25765846](https://pubmed.ncbi.nlm.nih.gov/25765846/)).

**Genetic risk factors.** The causal variant is itself the risk factor (fully penetrant dominant allele in reported families). A founder haplotype underlies recurrence in Dutch families. No modifier genes have been defined for HOMG2 specifically, though the broader DCT Mg²⁺ network (HNF1B, TRPM6, CNNM2, PCBD1) provides candidate interacting loci.

**Environmental risk factors.** None established as causal. Acquired/environmental causes of hypomagnesemia generally (diuretics, proton pump inhibitors, EGFR inhibitors, calcineurin inhibitors, alcohol, malnutrition) are relevant to differential diagnosis and may exacerbate the genetic deficit but are not part of the Mendelian etiology ([PMID: 25540137](https://pubmed.ncbi.nlm.nih.gov/25540137/)).

**Protective factors.** No genetic protective alleles described. Dietary magnesium adequacy mitigates severity but cannot correct the renal wasting.

**Gene–environment interactions.** Not formally studied for FXYD2; plausibly, concurrent Mg²⁺-wasting drugs would compound the phenotype.

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset / Severity | Frequency |
|---|---|---|---|---|
| Hypomagnesemia (serum Mg²⁺ <0.7 mmol/L) | Lab abnormality | HP:0002917 | Likely childhood/early; variable | Obligate (defining) |
| Renal magnesium wasting | Lab/physiologic | HP:0012605 | Lifelong | Obligate |
| Hypocalciuria | Lab abnormality | HP:0003127 | Lifelong | Characteristic |
| Muscle cramps | Symptom | HP:0003394 | Variable | Common |
| Tetany | Clinical sign | HP:0001281 | Episodic | Variable |
| Seizures / convulsions | Clinical sign | HP:0001250 | Variable | Reported subset |
| Chondrocalcinosis | Physical/imaging | HP:0000934 | Adult/late | Longstanding cases |

**Characteristics.** Onset is typically early in life (the biochemical defect is congenital), but symptomatic presentation varies from asymptomatic hypomagnesemia detected incidentally to overt neuromuscular irritability. Severity is **variable**; the course is **chronic and stable** (non-progressive at the organ level, as this is not a nephropathy that progresses to renal failure). Chondrocalcinosis is a late complication of chronic hypomagnesemia (also seen in Gitelman syndrome).

**Quality-of-life impact.** Generally modest with adequate supplementation; cramps, fatigue and occasional seizures can impair daily functioning. No disease-specific QoL instrument data (EQ-5D/SF-36) exist for this ultra-rare condition.

### 4. Genetic / Molecular Information

- **Causal gene:** *FXYD2* (HGNC:4028), chromosome 11q23, encoding the Na,K-ATPase γ-subunit (UniProt P54710).
- **Pathogenic variant:** **c.121G>A, p.Gly41Arg (G41R)** — a missense change affecting a highly conserved transmembrane glycine. Classified **pathogenic** (cosegregation, absence from controls, functional confirmation; ACMG criteria PS3/PP1/PM1/PM2-supporting). It is essentially the only recurrent pathogenic *FXYD2* allele reported for HOMG2.
- **Variant type:** Single-nucleotide missense; germline.
- **Allele frequency:** Absent from population controls (not in 132 control chromosomes in the original study); effectively absent/ultra-rare in gnomAD.
- **Functional consequence:** **Dominant-negative** (loss of wild-type function via misrouting/trapping) with an additional **gain-of-function** cation-channel activity in membrane-reaching protein ([PMID: 12763862](https://pubmed.ncbi.nlm.nih.gov/12763862/); [PMID: 17980699](https://pubmed.ncbi.nlm.nih.gov/17980699/); [PMID: 18448590](https://pubmed.ncbi.nlm.nih.gov/18448590/)).
- **Modifier genes / epigenetics / chromosomal abnormalities:** None established for HOMG2. HNF1B transcriptionally regulates the γa isoform and is a mechanistically related locus ([PMID: 21130072](https://pubmed.ncbi.nlm.nih.gov/21130072/)).

### 5. Environmental Information

No environmental, lifestyle, or infectious agents cause HOMG2 — it is monogenic. Environmental magnesium-depleting factors (diuretics, PPIs, alcohol) are relevant only as confounders/exacerbators and to the differential diagnosis ([PMID: 25540137](https://pubmed.ncbi.nlm.nih.gov/25540137/)).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (mutation → clinical manifestation):**

1. Heterozygous **FXYD2 c.121G>A** introduces **p.Gly41Arg** in the transmembrane helix of the γ-subunit → *results in* a misfolded/mis-assembling subunit.
2. G41R **abrogates normal γ-TM oligomerization geometry** (demonstrated with TM peptides) → *leads to* aberrant quaternary assembly.
3. The mutant subunit is **incorrectly routed and accumulates in perinuclear (ER/Golgi) structures**, lacking its normal post-translational modification → *results in* failure to reach the DCT basolateral membrane.
4. Because FXYD2 oligomerizes, **mutant hetero-oligomerizes with wild-type γ-subunit and traps it intracellularly** (dominant-negative) → *leads to* depletion of functional γ-subunit at the membrane (haploinsufficiency excluded).
5. Loss of functional basolateral γ-subunit **impairs Na,K-ATPase ATP/cation-affinity tuning in the DCT** → *results in* reduced transcellular Mg²⁺ reabsorption.
   - **Branch (gain-of-function):** the residual membrane-reaching G41R behaves as an **inward-rectifying nonselective cation channel**, perturbing membrane potential/ion flux (inferred to contribute; demonstrated in oocytes/MDCK).
6. Reduced DCT Mg²⁺ reabsorption → *results in* **renal magnesium wasting and hypomagnesemia**; coupling of Na⁺/Mg²⁺ handling → *leads to* **hypocalciuria**.
7. Low extracellular Mg²⁺ increases **neuromuscular excitability** → *results in* **muscle cramps, tetany, and seizures**; chronic Mg²⁺ deficiency → *leads to* **chondrocalcinosis**.

**Molecular/cellular detail.** The DCT is the final determinant of urinary Mg²⁺, as nephron segments beyond it are largely Mg²⁺-impermeable ([PMID: 19812536](https://pubmed.ncbi.nlm.nih.gov/19812536/)). Apical Mg²⁺ entry occurs via TRPM6; the basolateral Na,K-ATPase (with its γ-subunit) maintains the electrochemical gradient driving transcellular transport. The γ-subunit modulates ATP affinity and K⁺/Na⁺ kinetics of the pump ([PMID: 11278761](https://pubmed.ncbi.nlm.nih.gov/11278761/)). Upstream vs downstream: the mutation and misrouting are **upstream**; impaired DCT transport and systemic hypomagnesemia are **downstream**; neuromuscular symptoms are the terminal clinical readout.

**Ontology suggestions.** GO:0015693 (magnesium ion transport); GO:0006883 (intracellular sodium ion homeostasis); GO:0005890 (sodium:potassium-exchanging ATPase complex, CC); GO:0016020 (membrane); GO:0034976 (response to ER stress — inferred). **Cell type:** CL:1000849 (kidney distal convoluted tubule epithelial cell). **CHEBI:** CHEBI:18420 (magnesium(2+)); CHEBI:29108 (calcium(2+)).

### 7. Anatomical Structures Affected

- **Primary organ:** Kidney (UBERON:0002113), specifically the **distal convoluted tubule** (UBERON:0001292).
- **Cell type:** DCT epithelial cell (CL:1000849); subcellular locus of defect = **basolateral plasma membrane** (normal site) and **perinuclear ER/Golgi** (mutant accumulation site).
- **Body systems:** Renal/urinary (primary); neuromuscular and musculoskeletal (secondary, via hypomagnesemia); the γ-subunit is also expressed in medullary thick ascending limb and other segments ([PMID: 11278761](https://pubmed.ncbi.nlm.nih.gov/11278761/)).
- **Subcellular GO CC:** sodium:potassium-exchanging ATPase complex (GO:0005890); endoplasmic reticulum membrane (GO:0005789).
- **Lateralization:** Bilateral (systemic genetic defect affecting both kidneys).

### 8. Temporal Development

- **Onset:** Congenital biochemical defect; clinically detected from childhood through adulthood, often insidious.
- **Course:** Chronic, lifelong, non-progressive at the organ level (does not typically cause renal failure). Symptoms episodic/fluctuating (cramps, seizures) depending on Mg²⁺ level.
- **Progression:** Stable; chondrocalcinosis accrues over decades.
- **Remission:** No spontaneous remission; biochemical improvement is treatment-induced via supplementation.
- **Critical period:** Continuous supplementation; attention during periods of additional Mg²⁺ loss (illness, concurrent diuretics).

### 9. Inheritance and Population

- **Inheritance:** Autosomal dominant (OMIM #154020).
- **Penetrance / expressivity:** High penetrance for the biochemical phenotype in reported families; variable clinical expressivity.
- **Founder effect:** Yes — identical G41R on overlapping haplotype in Dutch families ([PMID: 25765846](https://pubmed.ncbi.nlm.nih.gov/25765846/)).
- **Epidemiology:** Ultra-rare; precise prevalence/incidence not established (only a handful of families reported worldwide).
- **Locus heterogeneity:** The isolated renal Mg-wasting phenotype is genetically heterogeneous — a US family did not link to 11q23 ([PMID: 11836293](https://pubmed.ncbi.nlm.nih.gov/11836293/)).
- **Sex ratio:** No strong sex bias reported (autosomal).
- **Consanguinity / carrier frequency:** Not applicable in the usual sense (dominant); no carrier-screening framework.

### 10. Diagnostics

- **Laboratory tests:** Serum Mg²⁺ (LOINC 19123-9) — low (<0.7 mmol/L); 24-h urinary Mg²⁺ — inappropriately high (fractional excretion of Mg elevated, confirming renal wasting); urinary calcium — **low (hypocalciuria)**, a key discriminator; serum K⁺ and acid–base typically normal (distinguishing from Gitelman/Bartter).
- **Biomarkers:** Serum/urine magnesium and calcium are the operative biomarkers; no protein/metabolite biomarker beyond electrolytes.
- **Imaging:** Joint radiographs may reveal chondrocalcinosis in longstanding disease.
- **Genetic testing:** Targeted single-gene *FXYD2* sequencing (for the recurrent G41R) is diagnostic; hypomagnesemia **gene panels** (including FXYD2, TRPM6, CLDN16, CLDN19, CNNM2, HNF1B, KCNA1, SLC12A3, EGF) or **WES/WGS** are appropriate when the phenotype overlaps other tubulopathies. Karyotype/CMA/FISH/mtDNA testing are not indicated (point mutation, not structural/mitochondrial).
- **Clinical criteria / differential diagnosis:** Diagnose by the triad of hypomagnesemia + renal Mg wasting + hypocalciuria, normal K⁺/acid–base, AD family history, and *FXYD2* G41R. **Differentials:** Gitelman syndrome (*SLC12A3*; adds hypokalemia/metabolic alkalosis/hypocalciuria), Bartter syndrome, TRPM6/HSH (hypomagnesemia with secondary hypocalcemia, AR), CLDN16/19 (hypomagnesemia with hypercalciuria/nephrocalcinosis), CNNM2, HNF1B (+ cysts/MODY5), EAST/SeSAME (*KCNJ10*), and acquired drug-induced hypomagnesemia ([PMID: 27234911](https://pubmed.ncbi.nlm.nih.gov/27234911/); [PMID: 32622651](https://pubmed.ncbi.nlm.nih.gov/32622651/)).
- **Screening:** Cascade testing of at-risk first-degree relatives (serum Mg²⁺ ± *FXYD2* sequencing).

### 11. Outcome / Prognosis

- **Survival / life expectancy:** Normal with adequate magnesium replacement; no excess mortality reported.
- **Morbidity:** Driven by neuromuscular symptoms (cramps, tetany, seizures) and chronic complications (chondrocalcinosis). Generally manageable.
- **Disease course:** Chronic/lifelong; does not progress to end-stage renal disease.
- **Prognostic factors:** Adequacy of Mg²⁺ supplementation and avoidance of additional Mg²⁺-wasting insults (diuretics, GI losses). No molecular prognostic biomarker beyond serum Mg²⁺.

### 12. Treatment

- **Pharmacotherapy / supportive care:** Lifelong **oral magnesium supplementation** (e.g., magnesium oxide, magnesium chloride, magnesium aspartate; organic salts often better tolerated with less diarrhea). Doses are titrated to symptom control; complete normalization of serum Mg²⁺ is often not achievable because supplementation drives further renal loss. Severe symptomatic episodes (seizures, tetany) require **IV magnesium sulfate**. By analogy to Gitelman management, **potassium-sparing diuretics (e.g., amiloride)** are a potential Mg²⁺-retaining adjunct in some tubulopathies, though evidence specific to FXYD2 is limited ([PMID: 32622651](https://pubmed.ncbi.nlm.nih.gov/32622651/)).
- **NCIT suggestion:** Magnesium supplement therapy; Magnesium Sulfate; dietary/electrolyte management.
- **Advanced/experimental therapeutics:** No gene therapy, RNA therapy, cell therapy, or targeted small molecule exists or is in trials for HOMG2.
- **Pharmacogenomics:** Not applicable.
- **Personalized approach:** Genotype confirmation (G41R) guides counseling and family screening; management remains supportive.

### 13. Prevention

- **Primary prevention:** Not possible (Mendelian). **Genetic counseling** for autosomal dominant 50% transmission risk; prenatal/preimplantation genetic testing is theoretically available given a known familial variant.
- **Secondary prevention:** Early biochemical screening (serum Mg²⁺) in at-risk relatives; cascade testing.
- **Tertiary prevention:** Consistent Mg²⁺ supplementation to prevent seizures/tetany and reduce chondrocalcinosis risk; avoid magnesium-wasting drugs.
- **Immunization / public health / environmental interventions:** Not applicable.

### 14. Other Species / Natural Disease

- **Orthologous gene:** *Fxyd2* is conserved in mouse (NCBI Gene 11936) and rat (NCBI Gene 29639); rat studies defined the γa/γb isoforms and their renal localization ([PMID: 11278761](https://pubmed.ncbi.nlm.nih.gov/11278761/)).
- **Natural disease in other species:** No naturally occurring FXYD2 hypomagnesemia disease is documented in companion animals or wildlife (OMIA has no established entry for this phenotype).
- **Comparative biology:** The Na,K-ATPase and its FXYD regulators are deeply evolutionarily conserved; the DCT Mg²⁺-handling mechanism is conserved across mammals, making rodents informative models of normal γ-subunit physiology.
- **Zoonotic potential:** Not applicable (non-infectious Mendelian disease).

### 15. Model Organisms

- **In vitro / heterologous systems (principal evidence):** Sf9 and COS-1 cells (mislocalization/misrouting; [PMID: 12763862](https://pubmed.ncbi.nlm.nih.gov/12763862/)); co-immunoprecipitation systems for oligomerization ([PMID: 17980699](https://pubmed.ncbi.nlm.nih.gov/17980699/)); synthetic transmembrane peptides with CD/FRET ([PMID: 12225751](https://pubmed.ncbi.nlm.nih.gov/12225751/)); *Xenopus* oocytes and MDCK epithelial monolayers for electrophysiology ([PMID: 18448590](https://pubmed.ncbi.nlm.nih.gov/18448590/)).
- **Mammalian models:** Rat kidney for γa/γb localization and function ([PMID: 11278761](https://pubmed.ncbi.nlm.nih.gov/11278761/)). No dedicated G41R knock-in mouse recapitulating HOMG2 is reported in the reviewed literature — a notable gap.
- **Phenotype recapitulation:** Cellular/oocyte models faithfully reproduce the molecular lesions (misrouting, dominant-negative trapping, aberrant channel activity) but do not model the integrated renal/systemic phenotype. A conditional DCT *Fxyd2^G41R* knock-in would be the logical next step.

---

## Mechanistic Model / Interpretation

```
 FXYD2 c.121G>A (p.Gly41Arg)   [germline, heterozygous, autosomal dominant]
            │
            ▼
 Disrupted TM-helix oligomerization geometry (G41R)          [PMID 12225751]
            │
            ▼
 Misfolding → ER/Golgi (perinuclear) retention of mutant γ    [PMID 12763862]
            │
            ├───────────────► Hetero-oligomerizes with WT γ → traps WT intracellularly
            │                  (DOMINANT-NEGATIVE; haploinsufficiency excluded)  [PMID 17980699]
            │                        │
            │                        ▼
            │             Loss of functional γ at DCT basolateral membrane
            │                        │
            │                        ▼
            │             Impaired Na,K-ATPase ATP/cation tuning            [PMID 11278761]
            │                        │
            ▼                        ▼
 Residual membrane G41R →   Reduced transcellular Mg²⁺ reabsorption in DCT   [PMID 19812536]
 aberrant inward-rectifying           │
 cation channel (GAIN-OF-FN)          ▼
 [PMID 18448590]           Renal Mg²⁺ wasting → HYPOMAGNESEMIA + HYPOCALCIURIA
                                      │
                                      ▼
              Neuromuscular hyperexcitability → cramps, tetany, seizures
                           + chronic deficiency → chondrocalcinosis           [PMID 25765846]
```

The **dominant-negative misrouting branch is the principal driver** (quantitatively, most mutant protein never reaches the membrane and additionally sequesters wild-type protein), while the **gain-of-function channel branch** operates on the minority of protein that reaches the surface and may further perturb DCT ion handling. Both converge on the same clinical endpoint: a DCT unable to reclaim filtered magnesium.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role |
|---|---|---|---|
| [12763862](https://pubmed.ncbi.nlm.nih.gov/12763862/) | Misrouting of Na,K-ATPase γ-subunit | Human + in vitro | Establishes G41R as causal; misrouting; haploinsufficiency excluded |
| [11062458](https://pubmed.ncbi.nlm.nih.gov/11062458/) | Dominant isolated renal Mg loss | Human | Original identification of dominant-negative FXYD2 mutation |
| [25765846](https://pubmed.ncbi.nlm.nih.gov/25765846/) | Recurrent p.Gly41Arg | Human | Recurrence + founder effect; clinical features |
| [17980699](https://pubmed.ncbi.nlm.nih.gov/17980699/) | Impaired routing after oligomerization | In vitro | Mechanism of dominant-negative trapping |
| [12225751](https://pubmed.ncbi.nlm.nih.gov/12225751/) | TM-peptide oligomerization | Biophysical | G41R abrogates γ-TM oligomerization |
| [18448590](https://pubmed.ncbi.nlm.nih.gov/18448590/) | G41R inward-rectifying channel | In vitro electrophysiology | Gain-of-function branch; basolateral Mg²⁺ extrusion |
| [11278761](https://pubmed.ncbi.nlm.nih.gov/11278761/) | γa/γb function & localization | Model organism (rat) | Normal γ-subunit physiology |
| [21130072](https://pubmed.ncbi.nlm.nih.gov/21130072/) | HNF-1B regulates γa | In vitro | Links FXYD2 to HNF1B hypomagnesemia pathway |
| [11836293](https://pubmed.ncbi.nlm.nih.gov/11836293/) | Genetic heterogeneity | Human linkage | Demonstrates locus heterogeneity |
| [19812536](https://pubmed.ncbi.nlm.nih.gov/19812536/) | DCT Mg²⁺ players (review) | Review | Places FXYD2 in DCT transport network |
| [27234911](https://pubmed.ncbi.nlm.nih.gov/27234911/) | Genetic causes of hypomagnesemia | Review | Differential diagnosis context |
| [25540137](https://pubmed.ncbi.nlm.nih.gov/25540137/) | Magnesium in health & disease | Review | Hypomagnesemia overview, acquired causes |
| [32622651](https://pubmed.ncbi.nlm.nih.gov/32622651/) | Bartter-Gitelman syndromes | Review | Differential + supplementation strategy |

---

## Limitations and Knowledge Gaps

1. **Single-allele evidence base.** Virtually all genetic knowledge rests on one recurrent variant (G41R) in a small number of Dutch-founder families. The allelic spectrum of *FXYD2* in HOMG2 is essentially unexplored; it is unknown whether other *FXYD2* variants cause disease.
2. **No precise epidemiology.** Prevalence/incidence are unquantified; the condition is reported only as case/family series.
3. **No in vivo disease model.** There is no published G41R knock-in mouse recapitulating the renal phenotype, limiting study of integrated pathophysiology and therapeutics.
4. **Relative weight of the two mechanisms** (dominant-negative vs gain-of-function) at the whole-organ level is not quantified.
5. **Hypocalciuria mechanism** in FXYD2 disease is described but not mechanistically dissected at the DCT level.
6. **Penetrance/expressivity** data are limited to small families; genotype–phenotype correlation beyond G41R is nonexistent.
7. **No QoL or natural-history cohort** data; long-term outcomes inferred rather than measured.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a DCT-targeted *Fxyd2^G41R* knock-in mouse** to test in vivo recapitulation of renal Mg²⁺ wasting, hypocalciuria, and neuromuscular phenotype, and to dissect dominant-negative vs channel contributions (e.g., compare to a membrane-trafficking-rescued allele).
2. **Resequence *FXYD2*** in unexplained isolated renal Mg-wasting cohorts (and query gnomAD/large biobanks) to define the full allelic spectrum and whether non-G41R pathogenic variants exist.
3. **Quantitative trafficking/electrophysiology** in polarized DCT-like cells (e.g., mpkDCT) to measure the fraction of G41R reaching the membrane and the magnitude of aberrant cation current under physiological gradients.
4. **Therapeutic screen for trafficking correctors** (pharmacological chaperones) that could rescue wild-type γ-subunit routing from mutant trapping — a mechanism-based treatment beyond symptomatic Mg²⁺ repletion.
5. **Natural-history / registry study** across known families to quantify penetrance, chondrocalcinosis/seizure risk, and QoL, informing supplementation guidelines.
6. **Test amiloride/potassium-sparing diuretics** prospectively as Mg²⁺-retaining adjuncts in FXYD2 disease, by analogy to Gitelman management.

---

*Report compiled from 6 confirmed findings across 19 reviewed papers (5 investigation iterations). Evidence types: human clinical/genetic, in vitro/heterologous expression, biophysical peptide studies, and rodent model-organism physiology.*


## Artifacts

- [OpenScientist final report](Renal_Hypomagnesemia_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Renal_Hypomagnesemia_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 10 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:11278761` (15 mentions) - Functional role and immunocytochemical localization of the gamma a and gamma b forms of the Na,K-ATPase gamma subunit.
  - shared terms: subunit

Weighed against this report's own most characteristic terms: `renal`, `fxyd2`, `hypomagnesemia`, `g41r`, `subunit`, `magnesium`, `disease`, `phenotype`, `dominant`, `dominant-negative`, `dct`, `mutation`, `wasting`, `hypocalciuria`, `clinical`, `isolated`, `normal`, `gene`, `genetic`, `chondrocalcinosis`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 16 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007937` (2 mentions) - the report calls it "MONDO"; MONDO calls it **renal hypomagnesemia 2**
- `HP:0002917` (2 mentions) - the report calls it "Lab abnormality"; HP calls it **Hypomagnesemia**
- `HP:0003127` (2 mentions) - the report calls it "Lab abnormality"; HP calls it **Hypocalciuria**
- `HP:0000934` (2 mentions) - the report calls it "Physical/imaging"; HP calls it **Chondrocalcinosis**
- `HP:0001250` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Seizure**
- `HP:0003394` (2 mentions) - the report calls it "Symptom"; HP calls it **Muscle spasm**
- `HP:0001281` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Tetany**
- `HP:0012605` (2 mentions) - the report calls it "Lab/physiologic"; HP calls it **Hypernatriuria**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005890` (2 mentions) - the report calls it "sodium:potassium-exchanging ATPase complex, CC", "Subcellular GO CC:** sodium:potassium-exchanging ATPase complex"; GO calls it **sodium:potassium-exchanging ATPase complex**
- `GO:0034976` (1 mention) - the report calls it "response to ER stress — inferred"; GO calls it **response to endoplasmic reticulum stress**, and lists "response to ER stress" among its other names
- `CL:1000849` (2 mentions) - the report calls it "kidney distal convoluted tubule epithelial cell", "Cell type:** DCT epithelial cell"; CL calls it **kidney distal convoluted tubule epithelial cell**
- `UBERON:0002113` (1 mention) - the report calls it "Primary organ:** Kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:4028` - called "FXYD2", "Causal gene:** *FXYD2"
- `GO:0005890` - called "sodium:potassium-exchanging ATPase complex, CC", "Subcellular GO CC:** sodium:potassium-exchanging ATPase complex"
- `CL:1000849` - called "kidney distal convoluted tubule epithelial cell", "Cell type:** DCT epithelial cell"