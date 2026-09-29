---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T19:30:25.622958'
end_time: '2026-09-25T19:52:43.338690'
duration_seconds: 1337.72
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Anaerobic Pneumonia
  mondo_id: MONDO:0004649
  category: Infectious Disease
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
citation_count: 38
reference_validation:
  total_references: 38
  verified: 38
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 23
  quotes_valid: 17
  quotes_unsupported: 6
  unsupported_quote_references:
  - PMID:15824979
  - PMID:35271580
  - PMID:23398871
  - PMID:12959026
  - PMID:30264525
  relevance_assessed: 38
  on_topic: 19
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 37
  verified: 36
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 8
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0025406
    reported_labels:
    - Fatigue-related
    ontology_label: Asthenia
  - term_id: HP:0031246
    reported_labels:
    - Purulent sputum
    ontology_label: Nonproductive cough
  - term_id: HP:0025426
    reported_labels:
    - Pulmonary cavity
    ontology_label: Abnormal bronchus morphology
  - term_id: NCIT:C47384
    reported_labels:
    - sulbactam
    ontology_label: Albendazole
  - term_id: NCIT:C61785
    reported_labels:
    - Broad, incl. Gram-negatives
    ontology_label: Hydrocortisone Acetate
  - term_id: NCIT:C1741
    reported_labels:
    - Anti-anaerobic fluoroquinolone
    ontology_label: Chloride Ion
  - term_id: NCIT:C639
    reported_labels:
    - Adjunct only (not monotherapy)
    ontology_label: Mesylates
  - term_id: NCIT:C1602
    reported_labels:
    - Severe/mixed/GNB
    ontology_label: Saquinavir Mesylate
  - term_id: NCIT:C15311
    reported_labels:
    - Preventive Intervention
    ontology_label: Quality Control
  - term_id: NCIT:C15234
    reported_labels:
    - Oral Hygiene
    ontology_label: Follow-Up Study
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0070265
    ontology_label: obsolete necrotic cell death
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Anaerobic_Pneumonia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Anaerobic_Pneumonia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Anaerobic Pneumonia
- **MONDO ID:** MONDO:0004649 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Anaerobic Pneumonia** covering all of the
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

# Anaerobic Pneumonia (MONDO:0004649): A Comprehensive Disease Characteristics Report

*Category: Infectious Disease | Evidence base: 51 papers reviewed, 10 confirmed findings*

---

## Summary

**Anaerobic pneumonia is an acquired, non-genetic infectious lung disease caused by aspiration of oropharyngeal and gingival anaerobic bacteria into dependent lung segments.** It is fundamentally a *polymicrobial* infection, dominated by obligate anaerobes—principally pigmented and nonpigmented *Prevotella* species, *Fusobacterium nucleatum*, *Peptostreptococcus* species, and *Bacteroides* species—that frequently co-exist with microaerophilic streptococci and aerobic Gram-negative bacilli. Because the causative organisms are members of the normal mouth flora, the disease has no Mendelian genetic basis; instead its "etiology" is a chain that begins with a breach of airway protective reflexes (impaired consciousness, dysphagia, impaired cough) combined with a large oral bacterial inoculum (periodontal disease), which permits aspirated anaerobes to establish a synergistic, tissue-destructive infection in the lung.

The disease follows a characteristic **subacute course**: over roughly 8–14 days after the aspiration event, an initial aspiration pneumonitis evolves into necrotizing pneumonia, then to cavitary lung abscess, and can progress to empyema and bronchopleural fistula. The clinical hallmark is *foul-smelling, putrid sputum* with fever and productive cough, and the diagnostic hallmark is a cavitary lesion with an air–fluid level in a dependent lung segment on chest imaging. Anaerobic culture is often falsely negative because specimens are contaminated by upper-airway flora, and modern comprehensive metagenomic next-generation sequencing (mNGS) of bronchoalveolar lavage fluid can recover fastidious anaerobes missed by culture and targeted panels.

**Antibiotic therapy cures 80–90% of cases**, with clindamycin and β-lactam/β-lactamase-inhibitor combinations as first-line agents; surgery/drainage is reserved for complications such as empyema. Prevention rests on oral hygiene (professional oral care in long-term-care settings) and dysphagia management. A notable epidemiologic trend is a *shift in microbial etiology* away from classical anaerobes toward Gram-negative bacilli (e.g., *Klebsiella pneumoniae*), and mortality in severe aspiration-related disease remains high (20–50% in critically ill patients). The disease occurs naturally across mammalian species, with dogs (post-anesthetic aspiration, laryngeal paralysis, megaesophagus) and horses (transport-associated pleuropneumonia) serving as informative veterinary counterparts.

---

## Section 1. Disease Information

**Overview.** Anaerobic pneumonia is a lower-respiratory-tract infection of the lung parenchyma caused predominantly by obligate anaerobic bacteria that normally colonize the oral cavity, gingival crevice, and upper airway. It is most often the consequence of aspiration of oropharyngeal secretions, and it sits on a clinical-pathological continuum with aspiration pneumonitis, necrotizing pneumonia, lung abscess, and empyema. Anaerobes "are involved in infections such as pneumonia, aspiration pneumonia, lung abscess and empyema" and "lower respiratory infections are usually either polymicrobial or mixed anaerobic-aerobic infections" ([PMID: 12959026](https://pubmed.ncbi.nlm.nih.gov/12959026/)).

**Key identifiers.**
- **MONDO:** 0004649
- **MeSH:** "Pneumonia, Aspiration" / anaerobic bacterial infections (closest indexing terms; there is no dedicated OMIM entry).
- **ICD-10:** J69.0 (Pneumonitis due to inhalation of food and vomit / aspiration pneumonia) is the code used in mortality databases for the aspiration process ([PMID: 42740601](https://pubmed.ncbi.nlm.nih.gov/42740601/)); anaerobic bacterial pneumonia maps to J15.8/J15.9 (other/unspecified bacterial pneumonia).
- **OMIM / Orphanet:** Not applicable — this is an acquired infectious disease, not a Mendelian or rare genetic disorder.

**Synonyms / alternative names.** Anaerobic pleuropulmonary infection; anaerobic lung infection; aspiration pneumonia (overlapping term); putrid/necrotizing pneumonia; anaerobic lung abscess (when cavitary).

**Source of information.** The knowledge here is derived from *aggregated disease-level* clinical and microbiological literature — bacteriologic case series, cohort studies, systematic reviews, and mechanistic/animal studies — rather than from individual patient EHR records.

---

## Section 2. Etiology

**Primary cause — infectious/mechanistic, not genetic.** The proximate cause is aspiration of oropharyngeal/gingival flora into the lower respiratory tract in a host with impaired airway protection. There is **no causal gene, no Mendelian inheritance, and no defined pathogenic variant** for anaerobic pneumonia itself (see Section 4). The dominant organisms are obligate anaerobes; a retrospective bacteriologic study of 116 specimens from 110 patients found that "cultures yielded an average of 3.0 anaerobes and 0.6 nonanaerobes per specimen. The most commonly encountered anaerobes were pigmented *Prevotella* species, nonpigmented *Prevotella* species, *Fusobacterium nucleatum*, *Peptostreptococcus* species, and *Bacteroides* species" ([PMID: 8324128](https://pubmed.ncbi.nlm.nih.gov/8324128/)). In acute community-acquired lung abscess, a mean of 2.3 bacterial species per patient was isolated, with "anaerobes alone being isolated in 44% of cases, aerobes alone in 19%, and mixed aerobic and anaerobic isolates in 22%" ([PMID: 7555164](https://pubmed.ncbi.nlm.nih.gov/7555164/)).

**Environmental / clinical risk factors.** The classic predisposing conditions reduce or defeat airway protective reflexes:
- **Compromised mental status** — "alcoholism, sedatives, stroke" — and **esophageal dysfunction** — "herniation, vomiting" — are important risk factors ([PMID: 11695090](https://pubmed.ncbi.nlm.nih.gov/11695090/)).
- **Swallowing dysfunction, impaired cough reflex, and degenerative neurological diseases** predispose to aspiration pneumonia ([PMID: 39536943](https://pubmed.ncbi.nlm.nih.gov/39536943/)).
- **Oral frailty / dysphagia markers** carry measurable risk: in long-term-care residents, "inability to gargle (OR = 1.991; 95% CI: 1.139–3.479) and unclear speech (OR = 1.752; 95% CI: 1.085–2.829) remained significantly associated with" aspiration pneumonia ([PMID: 42548261](https://pubmed.ncbi.nlm.nih.gov/42548261/)).
- **Periodontal disease / large oral bacterial inoculum** supplies the pathogens; anaerobes "are predominant components of normal oral cavity, upper respiratory tract" flora ([PMID: 12959026](https://pubmed.ncbi.nlm.nih.gov/12959026/)).
- **Diabetes mellitus** is a risk factor for the Gram-negative (*Klebsiella*) subset of lung abscess: "Lung abscess due to K. pneumoniae was associated with underlying diabetes mellitus (odds ratio [OR], 4.3; 95% confidence interval [CI], 1.0–18.4; P = .039)" ([PMID: 15824979](https://pubmed.ncbi.nlm.nih.gov/15824979/)).
- **Age / functional dependence** — older, functionally dependent inpatients are heavily affected; ~20% of dementia-care-eligible hospitalizations were for pneumonia or aspiration pneumonia ([PMID: 42711657](https://pubmed.ncbi.nlm.nih.gov/42711657/)).

**Genetic risk factors.** None established in humans. (In dogs, a heritable predisposition to megaesophagus indirectly raises aspiration risk — see Section 14.)

**Protective factors.** Environmental/behavioral: professional oral health care and dysphagia rehabilitation reduce risk (Sections 5, 13). No genetic protective variants are defined.

**Gene–environment interactions.** Not applicable in humans; the disease is driven by host functional state (consciousness, swallowing) interacting with oral microbial burden rather than by host genotype.

---

## Section 3. Phenotypes

The clinical phenotype is a **subacute febrile pneumonia with productive, putrid sputum**, often progressing to cavitary disease. Phenotype frequencies (largely from lung-abscess cohorts) and suggested HPO terms:

| Phenotype (type) | Frequency / characteristics | Suggested HPO term |
|---|---|---|
| Fever (symptom/sign) | 91% in a pediatric lung-abscess cohort (n=23); subacute onset | HP:0001945 (Fever) |
| Productive cough (symptom) | 87% ("Cough was reported in 87% of cases") | HP:0031245 (Productive cough) / HP:0012735 (Cough) |
| Hypoactivity / malaise (sign) | 91% | HP:0025406 (Fatigue-related); constitutional |
| Foul-smelling / putrid sputum (sign) | Characteristic; appears 8–14 days post-aspiration | HP:0031246 (Purulent sputum); putrid odor is disease-specific |
| Cavitary pulmonary lesion (radiographic/physical manifestation) | Hallmark; air–fluid level on CT | HP:0025426 (Pulmonary cavity) |
| Pleural effusion / empyema (sign) | Complication; loculated fluid | HP:0002202 (Pleural effusion); HP:0032247 (Empyema) |
| Hemoptysis, chest pain (symptoms) | Reported in abscess series | HP:0002105 (Hemoptysis); HP:0100749 (Chest pain) |

**Symptom characteristics.** Onset is typically *adult* (and geriatric), though pediatric cases occur; the pattern is *subacute/insidious*. Classic anaerobic infection produces "the characteristic, foul-smelling, putrid discharge [that] only occur[s] 8–14 days after the initial aspiration event," together with "necrotizing pneumonia [and] pulmonary abscesses" ([PMID: 20477271](https://pubmed.ncbi.nlm.nih.gov/20477271/)). In pediatric lung abscess, "systemic symptoms such as fever (91%) and hypoactivity (91%) were common. Cough was reported in 87% of cases" ([PMID: 41886424](https://pubmed.ncbi.nlm.nih.gov/41886424/)). Severity ranges from mild pneumonitis to severe necrotizing/cavitary disease; progression without treatment is *progressive*, but with antibiotics is usually resolving (radiologic resolution in 91% after ~4.8 weeks of antibiotics in the pediatric cohort).

**Quality-of-life impact.** Not formally quantified with EQ-5D/SF-36 in the reviewed literature. Indirect impact is substantial: aspiration pneumonia drives prolonged hospitalization, ICU admission, nasogastric-tube dependence, and functional decline in frail and dementia populations ([PMID: 42472523](https://pubmed.ncbi.nlm.nih.gov/42472523/); [PMID: 42711657](https://pubmed.ncbi.nlm.nih.gov/42711657/)).

---

## Section 4. Genetic / Molecular Information

**Not applicable — this is an acquired bacterial infection.** There are no causal human genes, no pathogenic germline or somatic variants (no ClinVar/HGMD entries), no modifier genes, no disease-defining epigenetic marks, and no chromosomal abnormalities associated with anaerobic pneumonia. Host susceptibility is determined by *functional* states (level of consciousness, swallowing and cough reflexes, oral hygiene, comorbidities such as diabetes) rather than by genotype.

The only genetic finding in the broader disease space concerns an **animal model of a predisposing condition**: canine congenital idiopathic megaesophagus (which causes recurrent aspiration pneumonia) is associated with an intronic VNTR in *MCHR2* (Melanin-Concentrating Hormone Receptor 2) in German Shepherd dogs, with "The single-copy allele … strongly associated with CIM (P-val = 1.32×10⁻¹⁷)" ([PMID: 35271580](https://pubmed.ncbi.nlm.nih.gov/35271580/)). This is a susceptibility locus for aspiration risk in dogs, **not** for anaerobic pneumonia per se, and has no human ortholog association with the disease.

---

## Section 5. Environmental Information

**Environmental / occupational factors.** None of the classical toxicologic type (no CTD toxin associations). The relevant "exposure" is the microbial reservoir of the oral cavity plus events that provoke aspiration (sedation, anesthesia, alcohol intoxication, vomiting).

**Lifestyle factors.** Alcoholism (compromised consciousness), sedative use, and smoking are contributors. Long-term smoking was common (75%) in an mNGS-confirmed anaerobic lung-abscess series, in which "all patients had oral diseases, and 75% were long-term smokers" ([PMID: 41054501](https://pubmed.ncbi.nlm.nih.gov/41054501/)). Poor oral hygiene/periodontal disease is a modifiable lifestyle-linked exposure.

**Infectious agents (NCBI Taxonomy).** The pathogens are the etiologic core of the disease:
- *Prevotella* spp. (e.g., *Prevotella intermedia*) — pigmented and nonpigmented (NCBI:txid838 genus)
- *Fusobacterium nucleatum* (NCBI:txid851)
- *Peptostreptococcus* spp. (NCBI:txid1257)
- *Bacteroides* spp. (NCBI:txid816)
- Microaerophilic/anaerobic streptococci (co-pathogens)
- *Actinomyces* spp. (e.g., *A. graevenitzii*) in actinomycosis-type presentations ([PMID: 40923736](https://pubmed.ncbi.nlm.nih.gov/40923736/))
- Increasingly, aerobic Gram-negative bacilli — *Klebsiella pneumoniae* (NCBI:txid573) — in the shifting etiology ([PMID: 15824979](https://pubmed.ncbi.nlm.nih.gov/15824979/))

"*Peptostreptococcus*, *Fusobacterium*, *Prevotella* and *Bacteroides* are the most common anaerobes" in lower respiratory infections ([PMID: 12959026](https://pubmed.ncbi.nlm.nih.gov/12959026/)).

---

## Section 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Impaired airway protection** (depressed consciousness, dysphagia, impaired cough reflex; alcohol, sedation, stroke, megaesophagus) **leads to** loss of the normal barrier that clears oropharyngeal secretions.
2. This **results in aspiration** of oropharyngeal/gingival secretions carrying a high anaerobic bacterial load into the lower respiratory tract — "the process of alveolar inflammation induced by the inhalation of oropharyngeal secretions into the lower respiratory tract" ([PMID: 39536943](https://pubmed.ncbi.nlm.nih.gov/39536943/)).
3. Aspirated material **deposits by gravity in dependent lung segments** (posterior segments of upper lobes, superior segments of lower lobes), determining lesion location; pulmonary distribution is "determined by a complex interplay between infection routes, lung anatomy and physiology, host defense mechanisms" ([PMID: 42279473](https://pubmed.ncbi.nlm.nih.gov/42279473/)).
4. Anaerobes **establish a polymicrobial/mixed anaerobic-aerobic community** in the airway ([PMID: 12959026](https://pubmed.ncbi.nlm.nih.gov/12959026/)).
5. **Microbial synergy amplifies infection and inflammation** — *inferred from model evidence*: supernatant of the periodontopathic anaerobe *Prevotella intermedia* upregulated alveolar platelet-activating-factor receptor (PAFR) and "in A549 cells, PiSup increased pneumococcal adhesion and PAFR transcript levels," producing more severe bacteremic pneumonia with higher MIP-2 and TNF-α in mice ([PMID: 24478074](https://pubmed.ncbi.nlm.nih.gov/24478074/)).
6. Sustained mixed infection with anaerobic tissue-destroying enzymes and host neutrophilic inflammation **leads to tissue necrosis** → necrotizing pneumonia (branch point).
7. Necrosis **results in liquefaction and cavitation** → lung abscess with an air–fluid level; putrid sputum reflects anaerobic metabolic byproducts; these features "only occur 8–14 days after the initial aspiration event" ([PMID: 20477271](https://pubmed.ncbi.nlm.nih.gov/20477271/)).
8. **Branch:** extension to the pleural space **results in** parapneumonic effusion → empyema; erosion into airways **results in** bronchopleural fistula and metastatic (e.g., subpleural, brain) abscess ([PMID: 41174571](https://pubmed.ncbi.nlm.nih.gov/41174571/)).

### Detail by category

- **Molecular pathways.** PAFR-mediated bacterial adhesion (model evidence) links anaerobe products to enhanced pathogen attachment and cytokine induction (MIP-2/CXCL2, TNF-α) ([PMID: 24478074](https://pubmed.ncbi.nlm.nih.gov/24478074/)). Suggested GO terms: GO:0006954 (inflammatory response), GO:0071222 (cellular response to lipopolysaccharide).
- **Cellular processes.** Neutrophilic inflammation, phagocytosis, tissue necrosis. GO:0006909 (phagocytosis), GO:0070265 (necrotic cell death), GO:0002438 (acute inflammatory response to antigenic stimulus).
- **Immune involvement.** Innate neutrophil-dominated response; no autoimmunity or primary immunodeficiency required, though immunosuppression worsens outcome. GO:0006955 (immune response).
- **Tissue-damage mechanisms.** Necrosis and abscess formation via bacterial proteases/toxins and host proteolytic burst; suppurative and, in *Actinomyces*, granulomatous inflammation with sulfur granules ([PMID: 40923736](https://pubmed.ncbi.nlm.nih.gov/40923736/)).
- **Molecular profiling.** No transcriptomic/proteomic/metabolomic host disease signatures are established for anaerobic pneumonia; the most relevant "omics" tool is **metagenomic sequencing for pathogen detection** (Section 10), not host profiling.

**Cell types involved (CL):** CL:0000775 (neutrophil), CL:0000235 (macrophage), CL:0000066 (epithelial cell — alveolar/airway), CL:0002063 (type II pneumocyte; A549 is a type-II-like line).

---

## Section 7. Anatomical Structures Affected

- **Primary organ:** lung (**UBERON:0002048**), respiratory system (**UBERON:0001004**).
- **Localization:** *dependent* lung segments — posterior segments of upper lobes and superior segments of lower lobes — reflecting gravitational deposition of aspirate. Right lower lobe is frequently involved (right main bronchus is more vertical); cases document right-lower-lobe abscess ([PMID: 41688916](https://pubmed.ncbi.nlm.nih.gov/41688916/)).
- **Lateralization:** commonly *unilateral* and dependent-segment predominant, but may be bilateral.
- **Secondary/adjacent structures:** pleura and pleural cavity (**UBERON:0002402 / UBERON:0002384**) → empyema; bronchi (**UBERON:0002185**) → bronchopleural fistula; mediastinum by extension.
- **Tissue level:** alveolar and bronchial **epithelium** (**UBERON:0000483**), lung parenchyma/connective tissue; suppurative destruction of parenchyma.
- **Subcellular (GO cellular component):** infection is extracellular/luminal; host responses engage plasma-membrane receptors (PAFR, GO:0005886 plasma membrane) and secretory/inflammatory machinery. No defined organelle-level lesion.
- **Body systems:** respiratory (primary); systemic (sepsis/bacteremia) as complication.

---

## Section 8. Temporal Development

- **Onset:** predominantly *adult and geriatric*, though pediatric cases occur; pattern is *subacute/insidious*. The disease characteristically declares itself over **8–14 days** after aspiration, when "necrotizing pneumonia, pulmonary abscesses and the characteristic, foul-smelling, putrid discharge" appear ([PMID: 20477271](https://pubmed.ncbi.nlm.nih.gov/20477271/)).
- **Stages / progression:** aspiration pneumonitis → necrotizing pneumonia → lung abscess → empyema/bronchopleural fistula. These "bacteria are relatively common in selected types of lung infections including aspiration pneumonia, lung abscess, necrotizing pneumonia and emphyema [empyema]" ([PMID: 23398871](https://pubmed.ncbi.nlm.nih.gov/23398871/)).
- **Progression rate:** subacute; slower than typical pyogenic (e.g., pneumococcal) pneumonia, contributing to delayed diagnosis.
- **Course pattern:** typically *progressive* if untreated; can be *recurrent* when the predisposing condition (e.g., megaesophagus, persistent dysphagia) is uncorrected.
- **Duration:** treatment courses are prolonged — weeks. Pediatric abscess achieved full radiologic resolution in 91% after ~4.8 weeks of antibiotics ([PMID: 41886424](https://pubmed.ncbi.nlm.nih.gov/41886424/)).
- **Remission:** treatment-induced remission is the norm with adequate antibiotics ± drainage.
- **Critical period for intervention:** the window before cavitation/empyema — early antibiotic therapy and airway protection prevent progression.

---

## Section 9. Inheritance and Population

- **Inheritance:** none — acquired infectious disease; no Mendelian pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier frequency applies to humans.
- **Epidemiology:** anaerobic pneumonia is a subset of aspiration-related pneumonia; exact population prevalence/incidence for the anaerobic subset is not well delineated because of culture blind spots. Aspiration pneumonia is a major burden in elderly, institutionalized, and neurologically impaired populations (~20% of dementia-care hospitalizations involved pneumonia/aspiration pneumonia; [PMID: 42711657](https://pubmed.ncbi.nlm.nih.gov/42711657/)).
- **Mortality:** high in severe disease — "Aspiration pneumonia is a common and life-threatening condition among critically ill patients, with mortality reaching 20-50%," and a MIMIC-IV ICU cohort of 2,132 patients had 25.5% in-hospital mortality ([PMID: 42721055](https://pubmed.ncbi.nlm.nih.gov/42721055/)). US aspiration-pneumonitis mortality with co-listed stroke declined from an age-adjusted 9.20 to 3.55 per 100,000 (1999–2024) ([PMID: 42740601](https://pubmed.ncbi.nlm.nih.gov/42740601/)).
- **Demographics:** male predominance in aspiration-pneumonitis mortality (AAMR 13.38→4.92 in men vs 6.79→2.46 in women); higher rates in nonmetropolitan/rural counties and the US South ([PMID: 42740601](https://pubmed.ncbi.nlm.nih.gov/42740601/)).
- **Geographic microbiological variation:** in Taiwan, ~21% of community-acquired lung abscesses were due to *Klebsiella pneumoniae*, reflecting regional dominance of Gram-negative etiology ([PMID: 15824979](https://pubmed.ncbi.nlm.nih.gov/15824979/)).

---

## Section 10. Diagnostics

**The central diagnostic challenge is recovering the causative anaerobes.** Routine culture frequently fails because specimens are contaminated by upper-airway flora and anaerobic bacteriology is technically demanding — anaerobes "are rarely recovered" and "anaerobic bacteriology is inadequate" ([PMID: 23398871](https://pubmed.ncbi.nlm.nih.gov/23398871/)).

**Imaging (RadLex/Radiopaedia).** Chest radiograph and CT are the primary tools. The hallmark is a **cavitary lesion with an air–fluid level** in a dependent segment: "Chest CT revealed a cavitary lesion with an air-fluid level in the right lower lobe" ([PMID: 41688916](https://pubmed.ncbi.nlm.nih.gov/41688916/)). Non-contrast high-resolution CT distinguishes necrotizing pneumonia, abscess, and other cavitary lesions using features such as irregular borders and pleural-effusion heterogeneity ([PMID: 42487366](https://pubmed.ncbi.nlm.nih.gov/42487366/)). Radiographic pattern (lobar, bronchopneumonic, necrotizing, abscess-forming, cavitating) correlates with pathogen and host ([PMID: 42279473](https://pubmed.ncbi.nlm.nih.gov/42279473/)).

**Microbiological sampling.** Uncontaminated specimens are needed: pus/purulent fluid, transtracheal aspirate, protected specimen brush, bronchoalveolar lavage (BAL), or pleural fluid ([PMID: 12959026](https://pubmed.ncbi.nlm.nih.gov/12959026/)). Fiberoptic bronchoscopy with protected-specimen brushing also helps exclude airway obstruction/neoplasm.

**Molecular / omics diagnostics.** Metagenomic next-generation sequencing (mNGS) of BAL fluid overcomes culture and targeted-panel blind spots: "tNGS was unable to detect anaerobic pathogens due to the limited scope of anaerobic bacterial targets in commercial panels. In contrast, comprehensive mNGS, when correctly interpreted in conjunction with clinical context, can detect anaerobic sequences" ([PMID: 42445473](https://pubmed.ncbi.nlm.nih.gov/42445473/)). mNGS has revealed fastidious anaerobes in culture-negative pediatric and adult abscesses ([PMID: 39239243](https://pubmed.ncbi.nlm.nih.gov/39239243/); [PMID: 41054501](https://pubmed.ncbi.nlm.nih.gov/41054501/)).

**Differential diagnosis of cavitary lung disease.** "Differential diagnosis includes bronchial neoplasms, either as necrotizing carcinoma or as the cause of poststenotic cavernous pneumonia, other infectious diseases like tuberculosis, Pneumocystis carinii pneumonia or endocarditis with septic metastases, and lung artery embolism or vasculitis" ([PMID: 11695090](https://pubmed.ncbi.nlm.nih.gov/11695090/)). Additional mimics in the reviewed literature: primary pulmonary osteosarcoma ([PMID: 1430451](https://pubmed.ncbi.nlm.nih.gov/1430451/)), tuberculosis with niveau-like shadows ([PMID: 8683908](https://pubmed.ncbi.nlm.nih.gov/8683908/)), infected pancreatic pseudocyst ([PMID: 17352178](https://pubmed.ncbi.nlm.nih.gov/17352178/)), hydatid cyst, and pulmonary aspergilloma.

**Genetic testing / screening:** not applicable.

---

## Section 11. Outcome / Prognosis

- **Cure / response:** favorable with adequate therapy — antibiotics "can provide cure in 80-90% of cases" ([PMID: 20477271](https://pubmed.ncbi.nlm.nih.gov/20477271/)); pediatric abscess resolved radiologically in 91% ([PMID: 41886424](https://pubmed.ncbi.nlm.nih.gov/41886424/)).
- **Mortality:** high in severe/critically ill and elderly frail patients (20–50%; ICU in-hospital 25.5%) ([PMID: 42721055](https://pubmed.ncbi.nlm.nih.gov/42721055/)); persistent critical illness is common after aspiration-related respiratory failure and confers ~3-fold higher one-year mortality after onset ([PMID: 42748124](https://pubmed.ncbi.nlm.nih.gov/42748124/)).
- **Complications:** lung abscess, necrotizing pneumonia, empyema, bronchopleural fistula, subpleural/brain abscess (metastatic); severe necrotizing infection can evolve to "necrotizing pneumonia, multiple lung abscesses, bronchopleural fistula, empyema and subpleural abscess" ([PMID: 41174571](https://pubmed.ncbi.nlm.nih.gov/41174571/)).
- **Prognostic factors:** severity/critical illness, host frailty and comorbidity (diabetes, dementia, neurologic disease), Gram-negative etiology, empyema/loculation, and delayed diagnosis. Systemic inflammatory indices are being explored as ICU prognostic markers ([PMID: 42721055](https://pubmed.ncbi.nlm.nih.gov/42721055/)).
- **Recovery:** high with timely antibiotics ± drainage; recurrence occurs if the underlying aspiration risk is uncorrected.

---

## Section 12. Treatment

**Pharmacotherapy (first-line).** "Preferred antibiotics for these infections based on clinical experience are clindamycin and any beta-lactam–beta-lactamase inhibitor" ([PMID: 23398871](https://pubmed.ncbi.nlm.nih.gov/23398871/)). Equal clinical efficacy is reported for aminopenicillin/β-lactamase-inhibitor combinations, newer anti-anaerobic fluoroquinolones (moxifloxacin), and clindamycin ([PMID: 20477271](https://pubmed.ncbi.nlm.nih.gov/20477271/)). Anaerobes are susceptible to "metronidazole … amoxicillin/clavulanate, ampicillin/sulbactam, piperacillin/tazobactam, imipenem and clindamycin" ([PMID: 12959026](https://pubmed.ncbi.nlm.nih.gov/12959026/)).

**β-lactamase coverage matters:** "Thirty percent of the anaerobic gram-negative rods were beta-lactamase producers," justifying β-lactamase-inhibitor combinations ([PMID: 8324128](https://pubmed.ncbi.nlm.nih.gov/8324128/)).

**Metronidazole caveat:** monotherapy fails because it lacks activity against the microaerophilic/aerobic streptococci in the mixed flora — combination therapy with an agent active against both anaerobes and aerobes is recommended ([PMID: 12959026](https://pubmed.ncbi.nlm.nih.gov/12959026/)).

| Drug / class | Role | NCIT (suggested) |
|---|---|---|
| Clindamycin (lincosamide) | First-line | NCIT:C376 |
| Amoxicillin-clavulanate | First-line β-lactam/BLI | NCIT:C29257 (amoxicillin) |
| Ampicillin-sulbactam | First-line β-lactam/BLI | NCIT:C47384 (sulbactam) |
| Piperacillin-tazobactam | Broad, incl. Gram-negatives | NCIT:C61785 |
| Moxifloxacin | Anti-anaerobic fluoroquinolone | NCIT:C1741 |
| Metronidazole | Adjunct only (not monotherapy) | NCIT:C639 |
| Imipenem/carbapenems | Severe/mixed/GNB | NCIT:C1602 |

**Surgical / interventional.** Reserved for complications: "Since antibiotics can provide cure in 80-90% of cases, surgical procedures are limited to severe complications, such as pleural empyema" ([PMID: 20477271](https://pubmed.ncbi.nlm.nih.gov/20477271/)). For empyema, "the presence of loculated pleural fluid determined the need for thoracotomy" and decortication ([PMID: 22610800](https://pubmed.ncbi.nlm.nih.gov/22610800/)). Minimally invasive percutaneous/thoracoscopic drainage is effective for abscess plus parapneumonic empyema, with faster recovery and shorter antibiotic courses ([PMID: 20223322](https://pubmed.ncbi.nlm.nih.gov/20223322/)).

**Supportive/rehabilitative.** Airway protection, swallowing rehabilitation, nutrition, and treatment of the underlying predisposing condition.

**Pharmacogenomics / advanced (gene, cell, RNA, targeted, immuno) therapies:** not applicable.

---

## Section 13. Prevention

**Primary prevention — oral hygiene.** Professional oral health care reduces respiratory infection in institutionalized populations: a systematic review of 13 studies (10 RCTs) found "moderate-to-strong evidence that onsite POHC in LTC homes, provided mostly by dental hygienists, is effective in preventing" mouth–lung infection ([PMID: 38020079](https://pubmed.ncbi.nlm.nih.gov/38020079/)). Mechanistic rationale: "NHAP is associated with poor oral hygiene and may be caused by aspiration of oropharyngeal flora into the lung. Oral care measures to remove or disrupt oral plaque might reduce the risk of NHAP" ([PMID: 30264525](https://pubmed.ncbi.nlm.nih.gov/30264525/)). A Cochrane review found low-quality evidence that professional oral care may reduce pneumonia-associated mortality (RR 0.41, 95% CI 0.24–0.72) though effects on incidence were inconclusive ([PMID: 30264525](https://pubmed.ncbi.nlm.nih.gov/30264525/)).

**Dysphagia management / secondary prevention.** Comprehensive oral care improved swallowing function and enabled nasogastric-tube removal in dysphagic LTC residents in a multicenter RCT ([PMID: 42472523](https://pubmed.ncbi.nlm.nih.gov/42472523/)). Early dysphagia screening and specialist swallow assessment reduce stroke-associated pneumonia risk ([PMID: 42500843](https://pubmed.ncbi.nlm.nih.gov/42500843/)).

**Behavioral / positioning.** Meal positioning, aspiration precautions, avoiding oversedation, and careful peri-anesthetic airway management (analogous canine data show ~10-fold pneumonia reduction after protocol changes, [PMID: 30375098](https://pubmed.ncbi.nlm.nih.gov/30375098/)).

**Tertiary prevention.** Prompt antibiotics and drainage to prevent progression to empyema/fistula.

**Immunization / genetic screening / chemoprophylaxis:** not applicable (no vaccine targets the polymicrobial oral flora).

Suggested NCIT: NCIT:C15311 (Preventive Intervention); NCIT:C15234 (Oral Hygiene).

---

## Section 14. Other Species / Natural Disease

Aspiration/anaerobic pneumonia occurs naturally across mammals, providing veterinary counterparts and models:

| Species (NCBI Taxon) | Setting / finding | Evidence |
|---|---|---|
| Dog — *Canis lupus familiaris* (txid9615) | Post-anesthetic aspiration pneumonia in 0.17% of 140,711 cases; risk factors "regurgitation and administration of hydromorphone at induction" | [PMID: 24588929](https://pubmed.ncbi.nlm.nih.gov/24588929/) |
| Dog | Aspiration pneumonia in 18.6–31.8% after arytenoid lateralization for laryngeal paralysis; "Postoperative megaesophagus (hazard ratio [HR], 2.58; 95% CI 1.56 to 3.93)" | [PMID: 26720085](https://pubmed.ncbi.nlm.nih.gov/26720085/) |
| Dog (German Shepherd) | Congenital idiopathic megaesophagus → recurrent aspiration pneumonia; sex-differentiated, *MCHR2* VNTR (GWAS P=1.32×10⁻¹⁷) | [PMID: 35271580](https://pubmed.ncbi.nlm.nih.gov/35271580/) |
| Dog | Generalized megaesophagus: radiographic aspiration pneumonia predicts death before discharge; median survival 90 days | [PMID: 21671818](https://pubmed.ncbi.nlm.nih.gov/21671818/) |
| Horse — *Equus caballus* (txid9796) | Transport-associated pleuropneumonia; "The finding of anaerobic bacteria in thoracic fluid was not associated with a lower survival rate"; 83% positive cultures | [PMID: 7744650](https://pubmed.ncbi.nlm.nih.gov/7744650/) |

**Comparative pathology.** The core mechanism — aspiration of oral flora due to impaired airway protection or esophageal dysmotility, followed by mixed/anaerobic lung infection — is conserved across dogs, horses, and humans. **Zoonotic potential:** none (organisms are host-associated oral commensals; disease is not transmissible). Orthologous predisposition gene: *MCHR2* (dog) has a human ortholog (HGNC MCHR2), but no human disease association is established.

---

## Section 15. Model Organisms

- **Mouse (*Mus musculus*) — mechanistic model.** The best experimental evidence for anaerobe-driven synergy comes from a mouse pneumococcal-pneumonia model in which *Prevotella intermedia* supernatant upregulated PAFR, increased pneumococcal adhesion, and produced "severe bacteremic pneumococcal pneumonia … with upregulated platelet-activating factor receptor expression," alongside higher MIP-2 and TNF-α ([PMID: 24478074](https://pubmed.ncbi.nlm.nih.gov/24478074/)). Companion **in vitro** model: A549 human alveolar epithelial cells ("In A549 cells, PiSup increased pneumococcal adhesion and PAFR transcript levels").
- **Naturally occurring animal models (induced/spontaneous).** Canine post-anesthetic aspiration, laryngeal-paralysis, and megaesophagus models (Section 14) recapitulate the *predisposition-to-aspiration* arm of the disease well, including risk-factor identification and outcome prediction. Equine transport pleuropneumonia models the anaerobic pleural-infection arm.
- **Phenotype recapitulation.** Animal models reproduce aspiration risk, mixed/anaerobic lung infection, and complication (pleural) biology; the *Prevotella* mouse model reproduces anaerobe-driven inflammatory amplification.
- **Limitations.** No single genetic model reproduces the full human polymicrobial anaerobic pneumonia; mouse work is largely mechanistic (synergy) rather than a faithful spontaneous-disease model; anaerobic culture/detection limitations apply in animals too.
- **Resources:** MGI (mouse), OMIA (canine/equine natural disease), Cellosaurus (A549).

---

## Mechanistic Model / Interpretation

```
  Impaired airway protection            High oral anaerobic load
  (↓consciousness, dysphagia,           (periodontal disease,
   ↓cough reflex; alcohol,               poor oral hygiene,
   sedation, stroke, mega-               smoking)
   esophagus)
        │                                       │
        └──────────────┬────────────────────────┘
                       ▼
          ASPIRATION of oropharyngeal / gingival secretions
                       │  (gravity → dependent lung segments;
                       ▼   R-lower & posterior-upper lobes)
        Polymicrobial / mixed anaerobic–aerobic community
        (Prevotella, Fusobacterium, Peptostreptococcus,
         Bacteroides ± streptococci ± Gram-neg bacilli)
                       │
                       │  microbial SYNERGY
                       │  (Prevotella → ↑PAFR → ↑adhesion,
                       ▼   ↑MIP-2/TNF-α — model evidence)
        Neutrophilic inflammation + tissue proteolysis
                       │  (8–14 days)
                       ▼
             NECROTIZING PNEUMONIA
                       │
                       ▼
        LUNG ABSCESS (cavity + air–fluid level, putrid sputum)
                  ┌────┴─────┐
                  ▼          ▼
        EMPYEMA          BRONCHOPLEURAL FISTULA / metastatic abscess
     (loculated →           (severe necrotizing disease)
      thoracotomy/
      decortication)

  Treatment: clindamycin OR β-lactam/β-lactamase-inhibitor
  (± metronidazole as adjunct, never alone) → cure 80–90%;
  drainage/surgery for empyema.
  Prevention: oral hygiene + dysphagia management (upstream nodes).
```

**Upstream vs downstream.** The two upstream nodes (impaired airway protection *and* high oral bacterial load) are the intervention targets — prevention acts here. Aspiration and polymicrobial synergy are the mechanistic core; necrosis, cavitation, and empyema are downstream, treated by antibiotics and drainage. A key modern modifier is the **etiologic shift toward Gram-negative bacilli**, which changes empiric-therapy considerations: "Accumulating evidence projects a fading contribution of anaerobic bacteria in aspiration pneumonia at the expense of Gram-negative bacilli" ([PMID: 39536943](https://pubmed.ncbi.nlm.nih.gov/39536943/)).

---

## Evidence Base

| PMID | Finding supported | Contribution |
|---|---|---|
| [8324128](https://pubmed.ncbi.nlm.nih.gov/8324128/) | F001, F003 | Polymicrobial anaerobic bacteriology (3.0 anaerobes/specimen); 30% β-lactamase producers |
| [7555164](https://pubmed.ncbi.nlm.nih.gov/7555164/) | F001 | Frequency of anaerobic (44%) vs mixed etiology in lung abscess |
| [11695090](https://pubmed.ncbi.nlm.nih.gov/11695090/) | F002, F006, F010 | Risk factors; subacute course; cavitary differential diagnosis |
| [20477271](https://pubmed.ncbi.nlm.nih.gov/20477271/) | F002, F003, F006, F009 | 8–14 day putrid course; 80–90% cure; surgery for empyema |
| [42548261](https://pubmed.ncbi.nlm.nih.gov/42548261/) | F002 | Oral-frailty risk ORs (gargle, speech) |
| [23398871](https://pubmed.ncbi.nlm.nih.gov/23398871/) | F003, F009, F010 | First-line antibiotics; complication spectrum; culture blind spots |
| [12959026](https://pubmed.ncbi.nlm.nih.gov/12959026/) | F003, F007 | Anaerobe genera, susceptibilities, combination-therapy rationale |
| [39536943](https://pubmed.ncbi.nlm.nih.gov/39536943/) | F004, F007 | Etiologic shift to Gram-negatives; definition of aspiration process |
| [15824979](https://pubmed.ncbi.nlm.nih.gov/15824979/) | F004 | Klebsiella lung abscess; diabetes association (OR 4.3) |
| [42721055](https://pubmed.ncbi.nlm.nih.gov/42721055/) | F004, F011 | ICU mortality 20–50% / 25.5%; inflammatory prognostic index |
| [42740601](https://pubmed.ncbi.nlm.nih.gov/42740601/) | F004 | US mortality trends and disparities |
| [38020079](https://pubmed.ncbi.nlm.nih.gov/38020079/) | F005 | Professional oral care prevents mouth–lung infection |
| [30264525](https://pubmed.ncbi.nlm.nih.gov/30264525/) | F005 | Cochrane: oral care pathogenesis/prevention rationale |
| [41886424](https://pubmed.ncbi.nlm.nih.gov/41886424/) | F006 | Symptom frequencies; radiologic resolution |
| [41688916](https://pubmed.ncbi.nlm.nih.gov/41688916/) | F006 | Hallmark cavitary air–fluid-level imaging |
| [42279473](https://pubmed.ncbi.nlm.nih.gov/42279473/) | F006 | Pulmonary distribution determinants |
| [24478074](https://pubmed.ncbi.nlm.nih.gov/24478074/) | F007 | Prevotella-driven synergy (PAFR, adhesion, cytokines) — model evidence |
| [24588929](https://pubmed.ncbi.nlm.nih.gov/24588929/) | F008 | Canine post-anesthetic aspiration risk factors |
| [7744650](https://pubmed.ncbi.nlm.nih.gov/7744650/) | F008 | Equine anaerobic pleuropneumonia |
| [26720085](https://pubmed.ncbi.nlm.nih.gov/26720085/) | F008 | Megaesophagus → aspiration (HR 2.58) |
| [35271580](https://pubmed.ncbi.nlm.nih.gov/35271580/) | F008 | Canine megaesophagus MCHR2 genetics (predisposition) |
| [41174571](https://pubmed.ncbi.nlm.nih.gov/41174571/) | F009 | Severe complication cascade (abscess→fistula→empyema) |
| [22610800](https://pubmed.ncbi.nlm.nih.gov/22610800/) | F009 | Empyema management (loculation → thoracotomy) |
| [20223322](https://pubmed.ncbi.nlm.nih.gov/20223322/) | F009 | Thoracoscopic drainage of abscess + empyema |
| [42445473](https://pubmed.ncbi.nlm.nih.gov/42445473/) | F010 | mNGS > culture/tNGS for anaerobes |
| [39239243](https://pubmed.ncbi.nlm.nih.gov/39239243/), [41054501](https://pubmed.ncbi.nlm.nih.gov/41054501/) | F010 | mNGS detects fastidious anaerobes; smoking/oral disease context |

---

## Limitations and Knowledge Gaps

1. **Diagnostic underascertainment.** The anaerobic subset of aspiration pneumonia is systematically underdiagnosed because anaerobes are hard to culture and specimens are contaminated by oral flora ([PMID: 23398871](https://pubmed.ncbi.nlm.nih.gov/23398871/)). Reported bacteriology therefore likely underestimates true anaerobic contribution, while the observed "shift to Gram-negatives" may partly reflect detection-method changes rather than true epidemiologic change.
2. **No dedicated epidemiology.** Prevalence/incidence figures are for aspiration pneumonia broadly, not the anaerobic subset specifically.
3. **Thin mechanistic evidence.** The synergy mechanism rests largely on a single *Prevotella intermedia*/pneumococcus mouse–A549 model ([PMID: 24478074](https://pubmed.ncbi.nlm.nih.gov/24478074/)); host transcriptomic/proteomic/metabolomic signatures are undefined.
4. **QoL data absent.** No EQ-5D/SF-36/PROMIS measurements specific to anaerobic pneumonia were identified.
5. **Small/older bacteriology series.** Several foundational studies are decades old and from single centers; susceptibility patterns and prevalence may have drifted.
6. **Treatment evidence is largely observational/experience-based.** Head-to-head modern RCTs of antibiotic regimens for anaerobic pneumonia are lacking; the 80–90% cure figure derives from clinical experience/review ([PMID: 20477271](https://pubmed.ncbi.nlm.nih.gov/20477271/)).
7. **Prevention evidence quality.** Cochrane rated oral-care evidence as low quality with inconclusive incidence effects ([PMID: 30264525](https://pubmed.ncbi.nlm.nih.gov/30264525/)).

---

## Proposed Follow-up Experiments / Actions

1. **Prospective mNGS-based bacteriology cohort.** Systematically apply comprehensive mNGS to BAL/pleural fluid in suspected aspiration/anaerobic pneumonia to quantify the *true* anaerobic contribution and re-test the "shift to Gram-negatives" hypothesis with detection method held constant.
2. **Host–microbe synergy mechanistics.** Extend the *Prevotella*/PAFR model to additional anaerobe–aerobe pairs and to primary human airway organoids; test whether PAFR antagonism attenuates synergy and disease severity.
3. **Randomized antibiotic comparison.** Modern RCT of clindamycin vs amoxicillin-clavulanate vs moxifloxacin (with mNGS-defined inclusion) to update regimen choice, including outcomes stratified by β-lactamase status.
4. **Oral-care prevention trial.** Adequately powered RCT of intensive professional oral care + dysphagia rehabilitation in high-risk (stroke, dementia, LTC) populations, with pneumonia incidence and anaerobic-confirmed cases as endpoints, to resolve Cochrane uncertainty.
5. **Prognostic biomarker validation.** Validate inflammatory indices (e.g., systemic immune-inflammation index; [PMID: 42721055](https://pubmed.ncbi.nlm.nih.gov/42721055/)) and imaging severity features for risk stratification and early drainage decisions.
6. **Cross-species mechanism synthesis.** Leverage canine megaesophagus/laryngeal-paralysis and equine pleuropneumonia cohorts as natural models to study the aspiration→anaerobic-infection continuum and test preventive interventions translatable to humans.

---

*Report compiled from 10 confirmed findings and 51 reviewed papers across 5 investigation iterations. Evidence source types: predominantly human clinical (case series, cohorts, systematic reviews) and veterinary clinical; mechanistic evidence is in vitro (A549) and mouse model; no computational/omics host-profiling data were available for this disease.*


## Artifacts

- [OpenScientist final report](Anaerobic_Pneumonia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Anaerobic_Pneumonia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 38 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 23 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 6 |
| References weighed for topical relevance | 38 |
| On topic | 19 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:15824979` *(abstract only)*: "Lung abscess due to K. pneumoniae was associated with underlying diabetes mellitus (odds ratio [OR], 4.3; 95% confidence interval [CI], 1.0–18.4; P = .039)"
  - closest text in source: "pneumoniae was associated with underlying diabetes mellitus (odds ratio [OR], 4.3; 95% confidence interval [CI], 1.0-18.4; P = .039) and negatively correlated with a time from onset of symptoms to diagnosis of >30 days (OR, 0.2; 95% CI, 0.1-0.7; P = .008)"
- `PMID:35271580` *(abstract only)*: "The single-copy allele … strongly associated with CIM (P-val = 1.32×10⁻¹⁷)"
  - closest text in source: "The single-copy allele is strongly associated with CIM (P-val = 1.32x10-17), with homozygosity for this allele posing the most significant risk"
- `PMID:23398871` *(abstract only)*: "anaerobic bacteriology is inadequate"
  - Text part not found as substring: 'anaerobic bacteriology is inadequate' (note: only abstract available for PMID:23398871, full text may contain this excerpt)
- `PMID:23398871` *(abstract only)*: "Preferred antibiotics for these infections based on clinical experience are clindamycin and any beta-lactam–beta-lactamase inhibitor"
  - closest text in source: "Preferred antibiotics for these infections based on clinical experience are clindamycin and any betalactam-betalactamase inhibitor."
- `PMID:12959026` *(abstract only)*: "metronidazole … amoxicillin/clavulanate, ampicillin/sulbactam, piperacillin/tazobactam, imipenem and clindamycin"
  - closest text in source: "Anaerobic bacteria are susceptible to metronidazole, tinidazole (exception of Gram-positive rods), amoxicillin/clavulanate, ampicillin/sulbactam, piperacillin/tazobactam, imipenem and clindamycin"
- `PMID:30264525` *(abstract only)*: "NHAP is associated with poor oral hygiene and may be caused by aspiration of oropharyngeal flora into the lung. Oral care measures to remove or disrupt oral plaque might reduce the risk of NHAP"
  - closest text in source: "Oral care measures to remove or disrupt oral plaque might be effective in reducing the risk of NHAP"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 23 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0025406` (1 mention) - the report calls it "Fatigue-related"; HP calls it **Asthenia**
- `HP:0031246` (1 mention) - the report calls it "Purulent sputum"; HP calls it **Nonproductive cough**
- `HP:0025426` (1 mention) - the report calls it "Pulmonary cavity"; HP calls it **Abnormal bronchus morphology**
- `NCIT:C47384` (1 mention) - the report calls it "sulbactam"; NCIT calls it **Albendazole**
- `NCIT:C61785` (1 mention) - the report calls it "Broad, incl. Gram-negatives"; NCIT calls it **Hydrocortisone Acetate**
- `NCIT:C1741` (1 mention) - the report calls it "Anti-anaerobic fluoroquinolone"; NCIT calls it **Chloride Ion**
- `NCIT:C639` (1 mention) - the report calls it "Adjunct only (not monotherapy)"; NCIT calls it **Mesylates**
- `NCIT:C1602` (1 mention) - the report calls it "Severe/mixed/GNB"; NCIT calls it **Saquinavir Mesylate**
- `NCIT:C15311` (1 mention) - the report calls it "Preventive Intervention"; NCIT calls it **Quality Control**
- `NCIT:C15234` (1 mention) - the report calls it "Oral Hygiene"; NCIT calls it **Follow-Up Study**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0070265` (obsolete necrotic cell death) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0070265` (1 mention) - the report calls it "necrotic cell death"; GO calls it **obsolete necrotic cell death**
- `CL:0000066` (1 mention) - the report calls it "epithelial cell — alveolar/airway"; CL calls it **epithelial cell**
- `CL:0002063` (1 mention) - the report calls it "type II pneumocyte; A549 is a type-II-like line"; CL calls it **pulmonary alveolar type 2 cell**, and lists "type II pneumocyte" among its other names
- `NCIT:C376` (1 mention) - the report calls it "First-line"; NCIT calls it **Cisplatin**
- `NCIT:C29257` (1 mention) - the report calls it "amoxicillin"; NCIT calls it **Miconazole Nitrate**, and lists "Micatin" among its other names