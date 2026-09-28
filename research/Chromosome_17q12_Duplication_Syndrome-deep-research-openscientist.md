---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-17T16:18:07.597304'
end_time: '2026-09-17T16:32:56.132137'
duration_seconds: 888.53
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Chromosome 17q12 Duplication Syndrome
  mondo_id: MONDO:0013796
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
citation_count: 26
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 15
  quotes_valid: 13
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:17924346
  - PMID:39286125
  relevance_assessed: 28
  on_topic: 20
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 45
  verified: 41
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 35
  labels_matching: 11
  labels_mismatched: 14
  mislabelled_terms:
  - term_id: MONDO:0013796
    reported_labels:
    - MONDO
    ontology_label: chromosome 17q12 duplication syndrome
  - term_id: HP:0001249
    reported_labels:
    - cognitive
    ontology_label: Intellectual disability
  - term_id: HP:0000717
    reported_labels:
    - behavioral
    ontology_label: Autism
  - term_id: HP:0100753
    reported_labels:
    - psychiatric
    ontology_label: Schizophrenia
  - term_id: HP:0001250
    reported_labels:
    - neurological
    ontology_label: Seizure
  - term_id: HP:0100033
    reported_labels:
    - behavioral
    ontology_label: Tics
  - term_id: HP:0012443
    reported_labels:
    - CNS malformation
    ontology_label: Abnormal brain morphology
  - term_id: HP:0001999
    reported_labels:
    - physical
    ontology_label: Abnormal facial shape
  - term_id: HP:0001388
    reported_labels:
    - connective tissue
    ontology_label: obsolete Joint laxity
  - term_id: HP:0002247
    reported_labels:
    - GI malformation
    ontology_label: Duodenal atresia
  - term_id: HP:0002032
    reported_labels:
    - GI malformation
    ontology_label: Esophageal atresia
  - term_id: NCIT:C15318
    reported_labels:
    - Rehabilitation Therapy
    ontology_label: Reproducibility
  - term_id: NCIT:C15328
    reported_labels:
    - Behavioral Therapy
    ontology_label: Splenectomy
  - term_id: NCIT:C15311
    reported_labels:
    - Monitoring
    ontology_label: Quality Control
  labels_variant: 10
  obsolete_terms:
  - term_id: HP:0001388
    ontology_label: obsolete Joint laxity
    replaced_by: HP:0001382
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Chromosome_17q12_Duplication_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Chromosome_17q12_Duplication_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chromosome 17q12 Duplication Syndrome
- **MONDO ID:** MONDO:0013796 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chromosome 17q12 Duplication Syndrome** covering all of the
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

# Chromosome 17q12 Duplication Syndrome — Comprehensive Disease Characterization Report

**Target Disease:** Chromosome 17q12 Duplication Syndrome
**MONDO ID:** MONDO:0013796
**Category:** Mendelian (recurrent genomic/copy-number disorder)
**Report basis:** 11 confirmed findings, 37 primary papers reviewed over 5 iterations

---

## Summary

Chromosome 17q12 duplication syndrome is a rare, autosomal-dominant **genomic (copy-number) disorder** caused by a recurrent ~1.4–1.5 Mb copy-number **gain** at chromosome band 17q12 (hg19 chr17:~34.8–36.2 Mb). The region is flanked by segmental duplications that predispose it to **non-allelic homologous recombination (NAHR)**, generating both this duplication and its reciprocal deletion. The duplicated interval spans roughly 15 OMIM genes, chief among them the dosage-sensitive transcription factor **HNF1B** (hepatocyte nuclear factor 1 beta), together with **LHX1** and **ACACA**. The disorder was first described alongside its reciprocal deletion in 2007 as "the first example of a recurrent genomic disorder associated with diabetes" ([PMID: 17924346](https://pubmed.ncbi.nlm.nih.gov/17924346/)).

Clinically, the duplication produces a **highly variable, incompletely penetrant, predominantly neurodevelopmental/neuropsychiatric phenotype**. Reported features include a variable degree of intellectual disability/learning disability, delayed speech and language, delayed motor milestones, autism spectrum disorder, schizophrenia (odds ratio ≈ 4), epilepsy, ADHD, and — established more recently — tics and Tourette/persistent tic disorder (a genome-wide significant association). Because penetrance is incomplete and expressivity is wide, the duplication is frequently inherited from a mildly-affected or apparently unaffected parent. Congenital malformations are less consistent than in the reciprocal deletion but include prenatal duodenal atresia ("double bubble" sign), cardiac malformations (including tetralogy of Fallot), growth anomalies, and variable renal and esophageal anomalies.

Diagnosis rests on **chromosomal microarray analysis (CMA)** — the sub-microscopic (~1.4 Mb) CNV is invisible to standard karyotyping — with prenatal detection via CMA/CNV-seq on amniotic fluid, usually prompted by fetal ultrasound anomalies. Parental testing is essential given frequent inheritance. There is **no curative or disease-specific therapy**; management is supportive, symptom-directed, and multidisciplinary, with a notable pharmacovigilance caution against valproate given documented valproate-induced pancreatitis in this population and the syndrome's underlying pancreatic/metabolic susceptibility. Short-term prognosis appears generally favorable. The leading mechanistic hypothesis is **HNF1B gene-dosage imbalance**; a zebrafish ortholog (*vhnf1*) is dosage-sensitive in both loss- and gain-of-function directions and, when overexpressed, perturbs hindbrain patterning — supporting a gain-of-dosage mechanism relevant to the CNS phenotype.

---

## Section 1 — Disease Information

**Overview.** 17q12 duplication syndrome is a recurrent contiguous-gene copy-number gain disorder. It is the reciprocal counterpart of the better-characterized 17q12 deletion syndrome (Renal Cysts and Diabetes syndrome, RCAD/MODY5). Whereas the deletion produces a relatively specific renal-and-diabetes phenotype, the duplication produces a **less specific, primarily neurodevelopmental/neuropsychiatric** phenotype with wide expressivity and incomplete penetrance ([PMID: 36548033](https://pubmed.ncbi.nlm.nih.gov/36548033/); [PMID: 27409573](https://pubmed.ncbi.nlm.nih.gov/27409573/)).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0013796 |
| Cytogenetic locus | 17q12 (hg19 chr17:~34.8–36.2 Mb) |
| Core gene | HNF1B (TCF2), OMIM 189907, HGNC:11630 |
| Related deletion syndrome | 17q12 deletion / RCAD (OMIM 137920) |

**Synonyms / alternative names:** Chromosome 17q12 microduplication syndrome; 17q12 recurrent duplication; dup(17)(q12); reciprocal duplication of the 17q12 region.

**Data provenance:** The knowledge base for this disorder is drawn primarily from **aggregated disease-level resources** — case series, prenatal CMA cohorts, psychiatric CNV cohorts, and individual case reports — rather than a single EHR-derived individual-patient dataset. Evidence spans human clinical case series (majority), plus supporting model-organism (zebrafish, mouse) and in vitro data for mechanism.

---

## Section 2 — Etiology

**Primary cause (genetic).** The disorder is caused by a **recurrent ~1.4–1.5 Mb duplication at 17q12 arising via NAHR** between flanking segmental duplications (Finding F001). Mefford et al. 2007 first described the reciprocal rearrangements and noted the duplication "appears to be enriched in samples from patients with epilepsy" ([PMID: 17924346](https://pubmed.ncbi.nlm.nih.gov/17924346/)). The recurrent aberrations "encompass the genes, HNF1B, LHX1, and ACACA, among others" ([PMID: 27409573](https://pubmed.ncbi.nlm.nih.gov/27409573/)).

**Genetic risk factors.** The duplication itself is the causal lesion; the dosage-sensitive driver is **HNF1B** (Finding F005). No independent susceptibility loci are established as necessary for expression, but **variable expressivity and incomplete penetrance** imply the action of modifier alleles and/or second genetic hits. Co-occurrence with independent pathogenic variants has been documented and can complicate the phenotype (e.g., co-inheritance with an *ARX* nonsense variant [PMID: 32519823](https://pubmed.ncbi.nlm.nih.gov/32519823/); with a *CCDC103* PCD mutation [PMID: 26123568](https://pubmed.ncbi.nlm.nih.gov/26123568/); a sibling pair with reciprocal 16p11.2 deletion and 17q12 duplication [PMID: 34538867](https://pubmed.ncbi.nlm.nih.gov/34538867/)) — illustrating that a "second hit" may modulate outcome.

**Environmental risk factors / protective factors.** None established. As a Mendelian CNV disorder, there are no proven environmental causes, lifestyle risk factors, protective variants, or gene–environment interactions specific to disease occurrence. This is a genuine knowledge gap rather than a negative finding. (Advanced parental age is *not* associated with higher recurrent-CNV yield; in one prenatal cohort advanced maternal age carried a *lower* incidence, [PMID: 38081620](https://pubmed.ncbi.nlm.nih.gov/38081620/).)

---

## Section 3 — Phenotypes

The duplication phenotype is dominated by neurodevelopmental and neuropsychiatric features, with variable congenital malformations (Findings F002, F004, F007, F008). Rasmussen et al. described "an extremely wide phenotypic spectrum, including a variable degree of learning disabilities, delayed language development, delayed motor milestones, and a broad range of psychiatric and neurological features" ([PMID: 27409573](https://pubmed.ncbi.nlm.nih.gov/27409573/)).

| Phenotype | Type | HPO suggestion | Onset | Frequency / notes |
|---|---|---|---|---|
| Intellectual disability / learning disability | cognitive | HP:0001249 | childhood | Common; IQ range reported 52–99 ([PMID: 30134084](https://pubmed.ncbi.nlm.nih.gov/30134084/)) |
| Delayed speech and language development | neurodevelopmental | HP:0000750 | childhood | Common ([PMID: 27409573](https://pubmed.ncbi.nlm.nih.gov/27409573/)) |
| Motor delay | neurodevelopmental | HP:0001270 | infancy/childhood | Common |
| Autism spectrum disorder | behavioral | HP:0000717 | childhood | Recurrent ([PMID: 22488896](https://pubmed.ncbi.nlm.nih.gov/22488896/); [PMID: 34538867](https://pubmed.ncbi.nlm.nih.gov/34538867/)) |
| Schizophrenia | psychiatric | HP:0100753 | adolescence/adult | OR ≈ 4.16 (P=0.018) ([PMID: 24776740](https://pubmed.ncbi.nlm.nih.gov/24776740/)) |
| Epilepsy / seizures | neurological | HP:0001250 | variable | Duplication "enriched in patients with epilepsy" ([PMID: 17924346](https://pubmed.ncbi.nlm.nih.gov/17924346/)) |
| ADHD / behavioral abnormalities | behavioral | HP:0007018 / HP:0000708 | childhood | Common |
| Tics / Tourette / persistent tic disorder | behavioral | HP:0100033 | childhood | Genome-wide significant association ([PMID: 40894066](https://pubmed.ncbi.nlm.nih.gov/40894066/)) |
| Structural brain abnormalities | CNS malformation | HP:0012443 | congenital | Reported in shared del/dup features |
| Facial dysmorphism | physical | HP:0001999 | congenital | Reported |
| Joint laxity | connective tissue | HP:0001388 | congenital | Reported |
| Renal anomalies | renal | HP:0000077 | congenital | Variable (less consistent than deletion) ([PMID: 21540130](https://pubmed.ncbi.nlm.nih.gov/21540130/)) |
| Duodenal atresia ("double bubble") | GI malformation | HP:0002247 | prenatal | Prenatal duplication feature ([PMID: 33678321](https://pubmed.ncbi.nlm.nih.gov/33678321/)) |
| Cardiac malformation (incl. tetralogy of Fallot) | cardiovascular | HP:0001636 / HP:0001631 | prenatal | 4/7 (57%) in one prenatal series ([PMID: 39433644](https://pubmed.ncbi.nlm.nih.gov/39433644/)) |
| Esophageal atresia | GI malformation | HP:0002032 | prenatal | Reported ([PMID: 21540130](https://pubmed.ncbi.nlm.nih.gov/21540130/)) |
| Growth anomalies | growth | HP:0001507 | prenatal/childhood | Prenatal duplication feature ([PMID: 33678321](https://pubmed.ncbi.nlm.nih.gov/33678321/)) |

**Characteristics.** Severity is **variable** (mild to severe), progression is generally **stable** rather than degenerative (neurodevelopmental features are static, though psychiatric features such as schizophrenia and tics have their own developmental onset windows). Age of onset ranges from **congenital/prenatal** (malformations) to **childhood** (neurodevelopmental) to **adolescence/adulthood** (schizophrenia).

**Quality of life impact.** No disease-specific EQ-5D/SF-36/PROMIS data were identified. Impact is inferred to be driven by intellectual disability, behavioral/psychiatric burden, and — where present — surgical malformations. This is a knowledge gap.

---

## Section 4 — Genetic / Molecular Information

**Causal lesion and gene content (Findings F001, F005, F010).** The canonical recurrent duplication maps to **hg19 chr17:~34.8–36.2 Mb** ([PMID: 40894066](https://pubmed.ncbi.nlm.nih.gov/40894066/)); a representative case spanned chr17:34,460,444–36,243,365 (GRCh37) ([PMID: 39793343](https://pubmed.ncbi.nlm.nih.gov/39793343/)). Reported CNV sizes range 1.42–1.91 Mb and "included 15 OMIM genes, such as HNF1B, LHX1, and ACACA" ([PMID: 39433644](https://pubmed.ncbi.nlm.nih.gov/39433644/)).

| Gene | HGNC / OMIM | Role |
|---|---|---|
| **HNF1B** (TCF2) | HGNC:11630 / OMIM 189907 | Master transcription factor; kidney, pancreas, genitourinary development; leading dosage-sensitive driver |
| **LHX1** | HGNC:6593 / OMIM 601999 | LIM-homeobox TF; genitourinary and neural development |
| **ACACA** | HGNC:84 | Acetyl-CoA carboxylase alpha; lipid/fatty-acid metabolism |
| Other interval genes | — | AATF, DDX52, CCL3P, ZNHIT3, MYO19, PIGW, GGNBP2, DHRS11, MRM1, TADA2A, DUSP14, among others |

**Variant classification and type.** The pathogenic event is a **structural variant (recurrent copy-number gain)**, not a point mutation — classified as **pathogenic** as a recurrent genomic disorder, though its clinical interpretation is complicated by incomplete penetrance and variable expressivity. Origin is **germline**. Functional consequence is **gene dosage increase (three copies)** of the interval genes; for HNF1B this is a **gain of dosage** (contrast with the reciprocal deletion's haploinsufficiency).

**Allele frequency.** As a recurrent NDD-CNV, the duplication is present at low frequency in the general/control population — a key reason its penetrance is now estimated lower than early case-control studies suggested ([PMID: 34817560](https://pubmed.ncbi.nlm.nih.gov/34817560/); [PMID: 22130109](https://pubmed.ncbi.nlm.nih.gov/22130109/)).

**Modifier genes / epigenetics.** No specific modifier genes or epigenetic marks are validated for the duplication. Variable expressivity implies modifiers exist; identifying them is a gap. Co-occurring independent variants (ARX, CCDC103, 16p11.2) act as phenotypic modifiers in reported families.

**Chromosomal abnormality.** By definition this is a **recurrent interstitial microduplication** (dup 17q12), NAHR-mediated, flanked by segmental duplications (Finding F001).

---

## Section 5 — Environmental Information

**Environmental factors, lifestyle factors, infectious agents:** **Not applicable.** This is a Mendelian genomic disorder with no established toxic, occupational, radiation, dietary, behavioral, or infectious contributors to disease occurrence. The only environmental consideration identified is **iatrogenic** (drug exposure): valproic acid can precipitate pancreatitis in these patients (see Sections 9/12, Finding F009).

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **NAHR between flanking segmental duplications at 17q12** → *results in* a recurrent ~1.4–1.5 Mb duplication (three copies of the interval) (Finding F001).
2. Extra copy of interval genes → *leads to* **increased gene dosage**, most consequentially of the dosage-sensitive transcription factor **HNF1B** (and LHX1, ACACA) (Finding F005).
3. Elevated HNF1B/LHX1 dosage during development → *perturbs* transcriptional programs that pattern multiple organ primordia. In zebrafish, *overexpression* of the HNF1B ortholog *vhnf1* "induces expansion of the val expression domain in the hindbrain," demonstrating that increased dosage disrupts **CNS (hindbrain) patterning** (Finding F011, [PMID: 11731484](https://pubmed.ncbi.nlm.nih.gov/11731484/)).
4. Disrupted neurodevelopmental patterning → *results in* the **neurodevelopmental/neuropsychiatric phenotype** — intellectual disability, speech/motor delay, autism, epilepsy, ADHD, tics/Tourette, and increased schizophrenia risk (Findings F002, F007; [PMID: 27409573](https://pubmed.ncbi.nlm.nih.gov/27409573/), [PMID: 24776740](https://pubmed.ncbi.nlm.nih.gov/24776740/), [PMID: 40894066](https://pubmed.ncbi.nlm.nih.gov/40894066/)).
5. **Branch — organogenesis:** dosage perturbation of HNF1B/LHX1 in kidney, pancreas, genitourinary, gut, and (inferred) cardiac primordia → *contributes to* variable **congenital malformations** — renal anomalies, duodenal atresia, cardiac defects (tetralogy of Fallot), esophageal atresia, growth anomalies (Findings F004, F008; [PMID: 33678321](https://pubmed.ncbi.nlm.nih.gov/33678321/), [PMID: 21540130](https://pubmed.ncbi.nlm.nih.gov/21540130/), [PMID: 39433644](https://pubmed.ncbi.nlm.nih.gov/39433644/)).
6. **Modifier layer (inferred):** incomplete penetrance and variable expressivity → *modulated by* genetic background/second hits and stochastic developmental factors, explaining transmission from mildly/unaffected parents (Finding F003; [PMID: 30134084](https://pubmed.ncbi.nlm.nih.gov/30134084/)).

### Detail by category

- **Molecular pathways / cellular processes.** Core mechanism is **transcription-factor dosage dysregulation** during embryonic **regional specification of organ primordia** (GO:0009952 anterior/posterior pattern specification; GO:0007389 pattern specification process; GO:0048513 animal organ development). HNF1B is a master regulator of nephrogenesis and pancreatic/hepatic development. In zebrafish, "vhnf1 controls development of multiple organs through regulating regional specification of organ primordia" ([PMID: 11731484](https://pubmed.ncbi.nlm.nih.gov/11731484/)).
- **Protein dysfunction.** No misfolding/aggregation; the defect is **quantitative overexpression** of otherwise normal proteins (gain of dosage). HNF1B is a POU-homeodomain transcription factor (UniProt P35680).
- **Metabolic changes.** ACACA (acetyl-CoA carboxylase) lies in the interval, linking the locus to fatty-acid/lipid metabolism; HNF1B dosage affects pancreatic development. These underlie the syndrome's **pancreatic/metabolic susceptibility**, clinically relevant to valproate-induced pancreatitis (Finding F009).
- **Immune involvement / tissue damage / oxidative stress:** not implicated — this is a developmental patterning disorder, not an inflammatory or degenerative one.
- **Molecular profiling.** No disease-specific transcriptomic/proteomic/metabolomic signature for the *duplication* was identified; mechanistic inference derives from the reciprocal deletion and model organisms. This is a gap.

**GO term suggestions:** GO:0009952, GO:0007389, GO:0048513, GO:0001822 (kidney development), GO:0031016 (pancreas development), GO:0021537 (telencephalon development).
**CL term suggestions:** CL:0000057 (fibroblast, for iPSC modeling), CL:0002518 (kidney epithelial cell), CL:0000164 (enteroendocrine/pancreatic lineage), CL:0000540 (neuron).

---

## Section 7 — Anatomical Structures Affected

| Level | Structure | UBERON / ontology | Involvement |
|---|---|---|---|
| Organ | Brain / CNS | UBERON:0000955 | Primary — neurodevelopment, structural brain anomalies, hindbrain patterning |
| Organ | Kidney | UBERON:0002113 | Variable — cystic/dysplastic/hypoplastic kidney, VUR |
| Organ | Pancreas | UBERON:0001264 | Susceptible — pancreatic development; pancreatitis risk |
| Organ | Heart | UBERON:0000948 | Malformation — tetralogy of Fallot, pulmonary artery anomalies |
| Organ | Duodenum / GI tract | UBERON:0002114 | Duodenal atresia ("double bubble"), esophageal atresia |
| Organ | Esophagus | UBERON:0001043 | Esophageal atresia |
| Body systems | Nervous, renal/urinary, cardiovascular, digestive, endocrine | — | Multi-system |

**Tissue/cell level.** Predominantly **neural tissue** (neurons, CNS progenitors) and **epithelial tissues** of kidney, pancreas, and gut. **Subcellular:** HNF1B/LHX1 act in the **nucleus** (GO:0005634) as transcription factors. **Localization/lateralization:** malformations are variably unilateral or bilateral (e.g., unilateral multicystic kidney reported, [PMID: 42099279](https://pubmed.ncbi.nlm.nih.gov/42099279/); bilateral hypoplastic kidneys reported, [PMID: 21540130](https://pubmed.ncbi.nlm.nih.gov/21540130/)); CNS involvement is bilateral/diffuse.

---

## Section 8 — Temporal Development

- **Onset.** Spans **prenatal/congenital** (malformations detectable on ultrasound), **infancy/childhood** (developmental delay, autism, epilepsy, ADHD, tics), and **adolescence/adulthood** (schizophrenia). Onset pattern is **insidious/chronic** for neurodevelopmental features.
- **Progression.** Neurodevelopmental features are largely **static/stable** (non-degenerative). Psychiatric features (schizophrenia, tics) follow their own developmental trajectories. Disease is **chronic/lifelong**.
- **Course.** Not relapsing-remitting at the syndrome level; individual manifestations (epilepsy, tics, psychiatric episodes) may fluctuate.
- **Critical periods.** The **embryonic/fetal window** of organ primordia specification is the mechanistically critical period (during which HNF1B dosage exerts its effect); postnatally, **early childhood** is the window for developmental/behavioral intervention.
- **Prognosis note.** Despite incomplete penetrance, "short-term prognosis appears positive" ([PMID: 39286125](https://pubmed.ncbi.nlm.nih.gov/39286125/), Finding F009).

---

## Section 9 — Inheritance and Population

**Epidemiology (Finding F003).** The reciprocal 17q12 deletion has an estimated population prevalence of ~1:4,000; recurrent NDD-CNVs collectively occur in ~0.48% of newborns (~1 in 200 across 13 loci) ([PMID: 32778765](https://pubmed.ncbi.nlm.nih.gov/32778765/)). The duplication is rarer and less precisely quantified but is on the order of 1 in several thousand. In prenatal CMA cohorts, 17q12 CNVs are recurrently detected among fetuses with ultrasound anomalies ([PMID: 38081620](https://pubmed.ncbi.nlm.nih.gov/38081620/)).

**Inheritance.**
- **Pattern:** Autosomal dominant.
- **De novo vs inherited:** ~one-third de novo, ~two-thirds inherited. "Approximately a third of the newborn recurrent NDD CNVs (34%, N = 20/59) are de novo variants" ([PMID: 32778765](https://pubmed.ncbi.nlm.nih.gov/32778765/)). The duplication "is often inherited from an apparently unaffected parent" ([PMID: 30134084](https://pubmed.ncbi.nlm.nih.gov/30134084/)).
- **Penetrance:** Incomplete. "17q12 copy number variants have variable presentations and incomplete penetrance, challenging prenatal counseling and management" ([PMID: 39286125](https://pubmed.ncbi.nlm.nih.gov/39286125/)).
- **Expressivity:** Highly variable, even within a single family (three-generation family, IQ 52–99; four affected children of a healthy mother, [PMID: 30134084](https://pubmed.ncbi.nlm.nih.gov/30134084/); [PMID: 36548033](https://pubmed.ncbi.nlm.nih.gov/36548033/)).
- **Anticipation / mosaicism / founder effects / consanguinity:** No genetic anticipation expected (not a repeat-expansion disorder). Germline mosaicism not specifically established for the duplication. No founder effect or consanguinity role — recurrence is driven by the NAHR-prone architecture, not by specific population haplotypes.

**Population demographics.** No strong ethnic predilection; recurrence is architecture-driven and thus pan-ethnic. **Sex ratio:** roughly balanced, though CNV pathogenicity may be sex-modulated for some neuropsychiatric outcomes ([PMID: 34817560](https://pubmed.ncbi.nlm.nih.gov/34817560/)). No distinct geographic clustering.

---

## Section 10 — Diagnostics

**Cornerstone test — CMA (Finding F006).** "17q12 deletions and duplications are two distinct, recurrent chromosomal aberrations usually diagnosed by chromosomal microarray analysis (CMA)" ([PMID: 27409573](https://pubmed.ncbi.nlm.nih.gov/27409573/)); "Diagnosis is mostly established by chromosomal microarray" ([PMID: 38379631](https://pubmed.ncbi.nlm.nih.gov/38379631/)).

| Modality | Utility for 17q12 duplication |
|---|---|
| **Chromosomal microarray (CMA)** | First-line and definitive; detects the sub-microscopic ~1.4 Mb gain |
| **CNV-seq** | Equivalent prenatal alternative on amniotic fluid |
| **Karyotyping** | Insufficient — CNV is below cytogenetic resolution |
| **FISH / MLPA / qPCR** | Targeted confirmation of the specific CNV |
| **Parental CMA** | Essential — determines inheritance vs de novo, informs recurrence risk |
| **WES/WGS** | Not first-line for this CNV; useful when a co-occurring monogenic disorder is suspected ([PMID: 40315683](https://pubmed.ncbi.nlm.nih.gov/40315683/), [PMID: 40993696](https://pubmed.ncbi.nlm.nih.gov/40993696/)) |

**Prenatal pathway.** Detection typically follows **fetal ultrasound anomalies** — renal (hyperechogenic kidneys), duodenal "double bubble," or cardiac findings — prompting amniocentesis and CMA/CNV-seq ([PMID: 33678321](https://pubmed.ncbi.nlm.nih.gov/33678321/); [PMID: 39286125](https://pubmed.ncbi.nlm.nih.gov/39286125/); [PMID: 38081620](https://pubmed.ncbi.nlm.nih.gov/38081620/)).

**Biomarkers / laboratory tests.** No specific circulating biomarker. Metabolic surveillance (glucose, given HNF1B/pancreatic involvement) and renal function monitoring are advisable. **Imaging:** renal ultrasound, echocardiography, and brain MRI as clinically indicated.

**Differential diagnosis.** Reciprocal 17q12 **deletion** (RCAD/MODY5 — renal cysts + diabetes, more specific phenotype); other recurrent NDD-CNVs (16p11.2, 15q11.2, 22q11.2, 1q21.1); isolated HNF1B point mutations; and co-occurring monogenic disorders that can mimic or compound the phenotype.

**Screening.** No population newborn screening. **Cascade testing** of relatives after a proband is diagnosed is appropriate given autosomal-dominant inheritance and frequent transmission from mildly-affected parents.

---

## Section 11 — Outcome / Prognosis

- **Survival / mortality.** No excess early mortality is established for the isolated duplication; life-limiting risk derives from severe congenital malformations (major cardiac defects, complex GI atresia) when present. No disease-specific survival curves exist.
- **Morbidity / function.** Chief morbidity is **neurodevelopmental and psychiatric** — intellectual disability, autism, ADHD, epilepsy, tics, and elevated schizophrenia risk — producing variable long-term functional impairment. Congenital malformations contribute surgical morbidity.
- **Disease course.** Chronic and lifelong but generally **non-progressive**; "short-term prognosis appears positive" ([PMID: 39286125](https://pubmed.ncbi.nlm.nih.gov/39286125/), Finding F009).
- **Prognostic factors.** Severity is unpredictable due to incomplete penetrance/variable expressivity; presence and severity of congenital malformations and degree of intellectual disability are the main determinants. No validated prognostic biomarkers.

---

## Section 12 — Treatment

**No curative or disease-specific therapy exists.** Management is **supportive, symptom-directed, and multidisciplinary** (Finding F009): "Treatment involves a multidisciplinary approach" ([PMID: 38379631](https://pubmed.ncbi.nlm.nih.gov/38379631/)).

| Manifestation | Intervention | NCIT suggestion |
|---|---|---|
| Epilepsy | Antiseizure medication (avoid valproate where possible) | NCIT:C264 (Anticonvulsant) |
| Developmental delay / ID | Early developmental intervention, special education, speech & occupational therapy | NCIT:C15318 (Rehabilitation Therapy) |
| Autism / ADHD / behavioral | Behavioral therapy, psychiatric management | NCIT:C15328 (Behavioral Therapy) |
| Psychiatric (schizophrenia) | Standard psychiatric pharmacotherapy | NCIT:C265 (Antipsychotic Agent) |
| Renal/metabolic | Nephrology surveillance, glucose monitoring | NCIT:C15311 (Monitoring) |
| Duodenal/esophageal atresia | Surgical repair | NCIT:C15329 (Surgical Procedure) |
| Cardiac defects (e.g., TOF) | Cardiac surgical repair | NCIT:C15329 |

**Pharmacovigilance caution (Finding F009).** **Valproic acid should be used cautiously.** A 14-year-old with 17q12 duplication, focal epilepsy, ASD, and ADHD developed valproate-induced acute pancreatitis (lipase 1,572 U/L); "Discontinuation of the VPA led to rapid clinical improvement and normalization of lab values" (probable ADR by Naranjo scale) ([PMID: 41700275](https://pubmed.ncbi.nlm.nih.gov/41700275/)). This is mechanistically plausible given the syndrome's pancreatic/metabolic susceptibility (HNF1B/ACACA in the interval).

**Pharmacogenomics, gene/cell/RNA/targeted/immuno-therapies:** **Not applicable / none available.** No advanced or experimental disease-modifying therapies or registered clinical trials specific to 17q12 duplication were identified. **Personalized medicine** currently amounts to genotype-informed surveillance (renal, metabolic) and drug selection (valproate avoidance).

---

## Section 13 — Prevention

- **Primary prevention.** Not possible — the causal lesion is a germline CNV. The only actionable primary-prevention avenue is **reproductive**: prenatal diagnosis (CMA/CNV-seq) and **preimplantation genetic testing (PGT)** for carrier parents.
- **Secondary prevention.** Early detection via prenatal ultrasound + CMA, and **cascade genetic testing** of relatives, enabling early developmental/surveillance intervention.
- **Tertiary prevention.** Surveillance and management of complications — renal function monitoring, glucose/metabolic monitoring, timely surgical repair, and **avoidance of valproate** to prevent iatrogenic pancreatitis.
- **Genetic counseling (central).** Given autosomal-dominant inheritance, incomplete penetrance, variable expressivity, and frequent transmission from mildly/unaffected parents, counseling must convey that (a) a carrier parent has a 50% transmission risk, (b) an inheriting child's phenotype is unpredictable, and (c) parental testing is essential ([PMID: 30134084](https://pubmed.ncbi.nlm.nih.gov/30134084/); [PMID: 39286125](https://pubmed.ncbi.nlm.nih.gov/39286125/)).
- **Immunization / public health / environmental interventions:** Not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy / natural disease.** No naturally occurring 17q12-duplication syndrome is described in companion animals or wildlife (OMIA: none identified). The disorder is human-specific in its recurrent-CNV form because it depends on the human-specific segmental-duplication architecture flanking 17q12.
- **Orthologous genes.** HNF1B ortholog in mouse (*Hnf1b*, NCBI Gene 21410) and zebrafish (*vhnf1/hnf1ba*). LHX1 and ACACA are conserved across vertebrates.
- **Comparative biology / conservation.** HNF1B's developmental role is **evolutionarily conserved**: the zebrafish ortholog regulates gut, pronephros, and hindbrain specification ([PMID: 11731484](https://pubmed.ncbi.nlm.nih.gov/11731484/)), indicating conserved dosage sensitivity of the mechanism.
- **Zoonotic potential / cross-species transmission:** Not applicable (non-infectious genetic disorder).

---

## Section 15 — Model Organisms

**Zebrafish (Finding F011).** The strongest gain-of-dosage evidence comes from zebrafish *vhnf1* (the MODY5/GCKD ortholog). Mutants show "formation of kidney cysts, underdevelopment of the pancreas and the liver, and reduction in size of the otic vesicles," and critically, "overexpression of vhnf1 induces expansion of the val expression domain in the hindbrain" — demonstrating dosage sensitivity in **both** loss- and gain-of-function directions and directly modeling how *increased* HNF1B dosage perturbs CNS patterning ([PMID: 11731484](https://pubmed.ncbi.nlm.nih.gov/11731484/)). This is the most disease-relevant model for the **duplication** specifically.

**Mouse.** *Hnf1b* (MGI; NCBI Gene 21410): complete null is early-embryonic lethal; conditional/heterozygous models produce renal cystic dysplasia and pancreatic hypoplasia — modeling **haploinsufficiency (the deletion)** more than the duplication. Ciliary-gene knockout mice display an "adipopancreatosis" phenotype linking related pathways to exocrine pancreatic disease ([PMID: 42613169](https://pubmed.ncbi.nlm.nih.gov/42613169/)).

**Model gaps.** **No published mouse model of the full multigene 17q12 duplication was identified.** iPSC/organoid models of patient-derived duplications would be a high-value addition. **Model databases:** MGI (*Hnf1b*), ZFIN (*vhnf1/hnf1ba*), Alliance of Genome Resources.

| Model | Type | Recapitulation | Limitation |
|---|---|---|---|
| Zebrafish *vhnf1* overexpression | gain-of-function | Hindbrain patterning perturbation (CNS relevance) | Single-gene, not full CNV |
| Mouse *Hnf1b* het/conditional KO | loss-of-function | Renal cystic dysplasia, pancreatic hypoplasia | Models the deletion, not duplication |
| Patient iPSC/organoids | in vitro | (proposed) | Not yet reported for the duplication |

---

## Mechanistic Model / Interpretation

```
   Segmental duplications flanking 17q12
                 │  (predispose to NAHR)
                 ▼
   Recurrent ~1.4–1.5 Mb DUPLICATION (3 copies)
        [HNF1B, LHX1, ACACA + ~12 genes]
                 │
                 ▼
     ↑ GENE DOSAGE  (HNF1B master TF, dosage-sensitive)
                 │
        ┌────────┴─────────────────────────┐
        ▼                                   ▼
  Disrupted CNS patterning          Disrupted organogenesis
  (hindbrain, telencephalon)        (kidney, pancreas, gut, heart)
        │                                   │
        ▼                                   ▼
  NEURODEVELOPMENTAL /              VARIABLE CONGENITAL
  NEUROPSYCHIATRIC phenotype        MALFORMATIONS
  • ID, speech/motor delay          • duodenal atresia (double bubble)
  • autism, ADHD                    • tetralogy of Fallot / cardiac
  • epilepsy                        • renal (cystic/hypoplastic)
  • schizophrenia (OR≈4)            • esophageal atresia
  • tics/Tourette (GWS)             • growth anomalies
        │                                   │
        └──────── MODIFIED BY ──────────────┘
        Incomplete penetrance + variable expressivity
        (genetic background / second hits / stochastic)
        → transmission from mildly/unaffected parents
```

The unifying principle is **transcription-factor gene-dosage imbalance**. The reciprocal deletion (HNF1B haploinsufficiency → RCAD/MODY5, a renal-and-diabetes phenotype) and the duplication (HNF1B overexpression → predominantly neurodevelopmental phenotype) are two ends of one dosage spectrum. The zebrafish gain-of-function data are pivotal because they show that *too much* HNF1B-ortholog activity, not just too little, disrupts development — grounding the duplication's CNS phenotype in a demonstrated (not merely inferred) mechanism.

---

## Evidence Base

| PMID | Contribution | Supports finding |
|---|---|---|
| [17924346](https://pubmed.ncbi.nlm.nih.gov/17924346/) | First description of reciprocal 17q12 rearrangements; duplication enriched in epilepsy; "first recurrent genomic disorder associated with diabetes" | F001 |
| [27409573](https://pubmed.ncbi.nlm.nih.gov/27409573/) | Danish cohort (38 patients); defines wide dup phenotype; genes HNF1B/LHX1/ACACA; CMA as diagnostic | F001, F002, F006 |
| [24776740](https://pubmed.ncbi.nlm.nih.gov/24776740/) | Swedish schizophrenia CNV study; 17q12 dup OR=4.16, P=0.018 | F002 |
| [30134084](https://pubmed.ncbi.nlm.nih.gov/30134084/) | Multi-generation family; variable penetrance; inheritance from unaffected parent; IQ 52–99 | F002, F003 |
| [32778765](https://pubmed.ncbi.nlm.nih.gov/32778765/) | 12,252-trio newborn study; ~34% de novo; prevalence estimates | F003 |
| [39286125](https://pubmed.ncbi.nlm.nih.gov/39286125/) | Prenatal CMA cohort; incomplete penetrance; favorable short-term prognosis | F003, F009 |
| [33678321](https://pubmed.ncbi.nlm.nih.gov/33678321/) | Prenatal duplication features: double bubble, cardiac, growth anomalies | F004, F008 |
| [21540130](https://pubmed.ncbi.nlm.nih.gov/21540130/) | Renal malformations & esophageal atresia can occur with the duplication | F004 |
| [24487052](https://pubmed.ncbi.nlm.nih.gov/24487052/) | HNF1B as dosage-sensitive driver (kidney/pancreas/GU); RCAD | F005 |
| [38379631](https://pubmed.ncbi.nlm.nih.gov/38379631/) | Neuropsychiatric case report; CMA diagnosis; multidisciplinary treatment | F006, F009 |
| [40894066](https://pubmed.ncbi.nlm.nih.gov/40894066/) / [42749776](https://pubmed.ncbi.nlm.nih.gov/42749776/) | Genome-wide significant 17q12 dup association with TS/persistent tic disorder | F007 |
| [39433644](https://pubmed.ncbi.nlm.nih.gov/39433644/) | Prenatal series; cardiovascular anomalies 4/7 incl. TOF; 15 OMIM genes | F008, F010 |
| [41700275](https://pubmed.ncbi.nlm.nih.gov/41700275/) | Valproate-induced pancreatitis in a 17q12 dup patient | F009 |
| [39793343](https://pubmed.ncbi.nlm.nih.gov/39793343/) | Precise GRCh37 coordinates of a 17q12 duplication | F010 |
| [11731484](https://pubmed.ncbi.nlm.nih.gov/11731484/) | Zebrafish *vhnf1*: dosage sensitivity; overexpression perturbs hindbrain | F011 |

**Evidence-type distribution:** Predominantly **human clinical** (case series, prenatal cohorts, psychiatric CNV cohorts, case reports), with supporting **model-organism** (zebrafish gain-of-function; mouse *Hnf1b*) mechanistic data. No disease-specific in vitro/omics profiling of the duplication was identified.

---

## Limitations and Knowledge Gaps

1. **Penetrance and expressivity are quantitatively imprecise.** Population-based estimates are confounded by higher-than-expected control frequencies; per-phenotype penetrance figures for the duplication remain uncertain.
2. **Frequency data are largely borrowed from the deletion** or from pooled recurrent-CNV cohorts; a duplication-specific prevalence is not firmly established.
3. **No duplication-specific molecular profiling** (transcriptomics/proteomics/metabolomics) exists; mechanism is inferred from the reciprocal deletion, single genes, and model organisms.
4. **No mouse model of the full multigene duplication;** the strongest gain-of-dosage evidence is from a single-gene zebrafish overexpression experiment.
5. **Contributions of non-HNF1B genes** (LHX1, ACACA, others) to the duplication phenotype are poorly delineated.
6. **No validated modifiers** explain the wide intrafamilial variability; second-hit contributions are documented anecdotally (ARX, CCDC103, 16p11.2) but not systematically.
7. **No quality-of-life, disability, or long-term outcome instruments** have been applied to this population.
8. **No disease-modifying therapy or clinical trials** — treatment is entirely symptomatic.

---

## Proposed Follow-up Experiments / Actions

1. **Patient-derived iPSC and cerebral/kidney organoid models** of the recurrent duplication to obtain duplication-specific transcriptomic/proteomic signatures and test HNF1B-dosage causality directly in human cells.
2. **Engineer a mouse (or zebrafish) model carrying the syntenic multigene duplication** to compare against single-gene *Hnf1b* overexpression and dissect gene-by-gene dosage contributions (LHX1, ACACA).
3. **Assemble a large, prospectively phenotyped 17q12-duplication registry** with parental testing to derive robust, per-phenotype penetrance and expressivity estimates and formal QoL/functional outcomes.
4. **Genetic-modifier and second-hit study**: WGS across variably affected carriers within families to identify modifier alleles explaining variable expressivity.
5. **Pharmacovigilance analysis** (FAERS + registry) to quantify valproate-associated pancreatitis risk in HNF1B-dosage disorders and formalize a valproate-avoidance recommendation.
6. **Systematic cardiac and GI malformation surveillance protocol** for prenatally diagnosed cases, given newly recognized tetralogy-of-Fallot and duodenal-atresia associations.
7. **Cross-locus comparison** of neuropsychiatric trajectories (schizophrenia, tics, ASD) between 17q12 duplication and other recurrent NDD-CNVs to refine genotype-specific counseling.

---

*Report compiled from 11 confirmed findings and 37 primary papers. Evidence is predominantly human clinical, supported by zebrafish and mouse model-organism data for mechanism. Where information was not available or not applicable (environmental etiology, infectious agents, veterinary natural disease, advanced/experimental therapeutics), this is stated explicitly.*


## Artifacts

- [OpenScientist final report](Chromosome_17q12_Duplication_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Chromosome_17q12_Duplication_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 15 |
| Quoted claims found in source | 13 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 28 |
| On topic | 20 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:17924346` *(abstract only)*: "enriched in patients with epilepsy"
  - closest text in source: "We also identified the reciprocal duplication, which appears to be enriched in samples from patients with epilepsy"
- `PMID:39286125` *(abstract only)*: "17q12 copy number variants have variable presentations and incomplete penetrance, challenging prenatal counseling and management"
  - closest text in source: "PURPOSE: 17q12 copy number variants (CNVs) have variable presentations and incomplete penetrance, challenging prenatal counseling and management"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 35 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 14 |
| Terms whose name is worth a second look | 10 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013796` (2 mentions) - the report calls it "MONDO"; MONDO calls it **chromosome 17q12 duplication syndrome**
- `HP:0001249` (1 mention) - the report calls it "cognitive"; HP calls it **Intellectual disability**
- `HP:0000717` (1 mention) - the report calls it "behavioral"; HP calls it **Autism**
- `HP:0100753` (1 mention) - the report calls it "psychiatric"; HP calls it **Schizophrenia**
- `HP:0001250` (1 mention) - the report calls it "neurological"; HP calls it **Seizure**
- `HP:0100033` (1 mention) - the report calls it "behavioral"; HP calls it **Tics**
- `HP:0012443` (1 mention) - the report calls it "CNS malformation"; HP calls it **Abnormal brain morphology**
- `HP:0001999` (1 mention) - the report calls it "physical"; HP calls it **Abnormal facial shape**
- `HP:0001388` (1 mention) - the report calls it "connective tissue"; HP calls it **obsolete Joint laxity**
- `HP:0002247` (1 mention) - the report calls it "GI malformation"; HP calls it **Duodenal atresia**
- `HP:0002032` (1 mention) - the report calls it "GI malformation"; HP calls it **Esophageal atresia**
- `NCIT:C15318` (1 mention) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Reproducibility**
- `NCIT:C15328` (1 mention) - the report calls it "Behavioral Therapy"; NCIT calls it **Splenectomy**
- `NCIT:C15311` (1 mention) - the report calls it "Monitoring"; NCIT calls it **Quality Control**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0001388` (obsolete Joint laxity) (1 mention) - replaced by `HP:0001382`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000750` (1 mention) - the report calls it "neurodevelopmental"; HP calls it **Delayed speech and language development**, and lists "Poor language development" among its other names
- `HP:0001270` (1 mention) - the report calls it "neurodevelopmental"; HP calls it **Motor delay**, and lists "Motor developmental delay" among its other names
- `HP:0000077` (1 mention) - the report calls it "renal"; HP calls it **Abnormality of the kidney**, and lists "Renal anomaly" among its other names
- `HP:0001507` (1 mention) - the report calls it "growth"; HP calls it **Growth abnormality**, and lists "Growth issue" among its other names
- `CL:0000057` (1 mention) - the report calls it "fibroblast, for iPSC modeling"; CL calls it **fibroblast**
- `CL:0000164` (1 mention) - the report calls it "enteroendocrine/pancreatic lineage"; CL calls it **enteroendocrine cell**
- `UBERON:0000955` (1 mention) - the report calls it "Brain / CNS"; UBERON calls it **brain**
- `UBERON:0002114` (1 mention) - the report calls it "Duodenum / GI tract"; UBERON calls it **duodenum**
- `NCIT:C265` (1 mention) - the report calls it "Antipsychotic Agent"; NCIT calls it **Antidepressant Agent**
- `NCIT:C15329` (2 mentions) - the report calls it "Surgical Procedure", "Cardiac surgical repair"; NCIT calls it **Surgical Procedure**, and lists "Surgical Intervention" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C15329` - called "Surgical Procedure", "Cardiac surgical repair"
