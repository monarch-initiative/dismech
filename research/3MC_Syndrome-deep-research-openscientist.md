---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-29T10:06:00.949873'
end_time: '2026-08-29T10:18:13.740058'
duration_seconds: 732.79
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: 3MC Syndrome
  mondo_id: ''
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
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 19
  on_topic: 15
  validator_version: 0.2.1
term_validation:
  total_terms: 61
  verified: 52
  not_found: 2
  obsolete: 1
  unverifiable: 6
  confabulation_rate: 0.036
  labels_checked: 30
  labels_matching: 8
  labels_mismatched: 18
  mislabelled_terms:
  - term_id: MONDO:0018721
    reported_labels:
    - 3MC syndrome
    ontology_label: obsolete rare combined vascular malformation
  - term_id: HP:0000316
    reported_labels:
    - physical/craniofacial sign
    ontology_label: Hypertelorism
  - term_id: HP:0000581
    reported_labels:
    - physical sign
    ontology_label: Blepharophimosis
  - term_id: HP:0000508
    reported_labels:
    - physical sign
    ontology_label: Ptosis
  - term_id: HP:0002553
    reported_labels:
    - physical sign
    ontology_label: Highly arched eyebrow
  - term_id: HP:0000537
    reported_labels:
    - physical sign
    ontology_label: Epicanthus inversus
  - term_id: HP:0000494
    reported_labels:
    - physical sign
    ontology_label: Downslanted palpebral fissures
  - term_id: HP:0000365
    reported_labels:
    - lab/functional sign
    ontology_label: Hearing impairment
  - term_id: HP:0100541
    reported_labels:
    - tail-like
    ontology_label: Femoral hernia
  - term_id: HP:0001363
    reported_labels:
    - physical sign
    ontology_label: Craniosynostosis
  - term_id: HP:0003042
    reported_labels:
    - physical sign
    ontology_label: Elbow dislocation
  - term_id: HP:0007700
    reported_labels:
    - ophthalmic sign
    ontology_label: Ocular anterior segment dysgenesis
  - term_id: HP:0001537
    reported_labels:
    - physical sign
    ontology_label: Umbilical hernia
  - term_id: HP:0004209
    reported_labels:
    - physical sign
    ontology_label: Clinodactyly of the 5th finger
  - term_id: HP:0011003
    reported_labels:
    - ophthalmic sign
    ontology_label: High myopia
  - term_id: CHEBI:37671
    reported_labels:
    - high-mannose oligosaccharide/mannose
    ontology_label: (1->3)-beta-D-glucan
  - term_id: UBERON:0000970
    reported_labels:
    - Eyes / periocular
    ontology_label: eye
  - term_id: UBERON:0002113
    reported_labels:
    - Kidney & urinary tract
    ontology_label: kidney
  labels_variant: 4
  unresolved_terms:
  - UBERON:0000905
  - UBERON:0009832
  obsolete_terms:
  - term_id: MONDO:0018721
    ontology_label: obsolete rare combined vascular malformation
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
  path: 3MC_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: 3MC_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 3MC Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **3MC Syndrome** covering all of the
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

# 3MC Syndrome — Comprehensive Disease Characterization Report

*Prepared for a disease knowledge base entry. Evidence type is human clinical unless otherwise noted (model organism / in vitro / computational). Primary literature cited by PMID.*

---

## Summary (Answer to the Research Question)

**3MC syndrome** is a rare, autosomal-recessive congenital malformation syndrome that unifies four historically separate disorders — **M**alpuech, **M**ichels, **M**ingarelli and **C**arnevale syndromes ("3MC"). It is caused by biallelic loss-of-function variants in one of three genes of the **lectin pathway of complement**: **MASP1** (encoding MASP-1/MASP-3), **COLEC11** (encoding collectin-11/CL-K1), and **COLEC10** (encoding collectin-10/CL-L1). The shared mechanism is loss of a collectin/MASP-3 chemoattractant guidance cue required for **neural crest cell migration**, producing a distinctive facial gestalt (hypertelorism, blepharophimosis, blepharoptosis, highly arched eyebrows) together with cleft lip/palate, postnatal growth deficiency, developmental delay, hearing loss, a characteristic caudal appendage, skeletal (craniosynostosis, radioulnar synostosis) and genitourinary anomalies (PMIDs 21258343, 28301481).

---

## 1. Disease Information

- **Overview:** A rare autosomal-recessive multiple-congenital-anomaly / dysmorphism syndrome affecting craniofacial, skeletal, genitourinary, ophthalmic and (variably) cardiac development. The name "3MC" was proposed as a unifying term for the overlapping Carnevale, Mingarelli, Malpuech and Michels syndromes (PMID 21258343).
- **Key identifiers (suggested):**
  - **MONDO:** MONDO:0018721 ("3MC syndrome") — with subtypes 3MC syndrome type 1/2/3.
  - **OMIM (phenotype):** 3MC syndrome 1 (**#257920**, *MASP1/COLEC11* — historically Malpuech/Carnevale), 3MC syndrome 2 (**#265050**, *COLEC11*), 3MC syndrome 3 (**#248340**, *COLEC10* — historically Michels). (PMIDs 36503917, 34636477)
  - **OMIM (gene):** MASP1 *600521; COLEC11 *612502; COLEC10 *607620.
  - **Orphanet:** ORPHA:293843 (3MC syndrome); legacy entries Malpuech syndrome (ORPHA:1993), Michels syndrome (ORPHA:1394), Carnevale/Mingarelli.
  - **ICD-10:** Q87.0 (congenital malformation syndromes predominantly affecting facial appearance). **ICD-11:** LD2F.0Y (other specified syndromes with facial features as a major feature).
  - **MeSH:** No dedicated descriptor; indexed under "Abnormalities, Multiple" / supplementary concept "3MC syndrome."
- **Synonyms / alternative names:** Malpuech–Michels–Mingarelli–Carnevale syndrome; Malpuech facial clefting syndrome; Michels syndrome; Carnevale syndrome; Mingarelli syndrome; Malpuech syndrome; OSA syndrome; craniofacial-ulnar-renal syndrome; blepharophimosis-ptosis-cleft-lip syndrome (descriptive).
- **Data derivation:** Information here is derived from **aggregated disease-level resources** (OMIM/Orphanet) and **individual patient case reports / small cohorts** (fewer than ~100 molecularly confirmed patients worldwide). There is no large EHR-based dataset for this ultra-rare disorder.

---

## 2. Etiology

- **Primary cause — genetic:** Biallelic (homozygous or compound heterozygous) pathogenic variants in **MASP1**, **COLEC11**, or **COLEC10** — all encoding components of the lectin complement pathway (PMID 21258343: *"identified two mutated genes, COLEC11 and MASP1, both of which encode proteins in the lectin complement pathway"*; PMID 28301481 for COLEC10). There is evidence of further **genetic heterogeneity**: some clinically typical patients from consanguineous families have no MASP1/COLEC11/COLEC10 variant (PMID 26789649).
- **Genetic risk factors:**
  - Causal variants in the three genes (Section 4).
  - **Consanguinity** — a major risk factor; most reported families are consanguineous with homozygous variants.
  - **Founder alleles** — e.g., COLEC10 c.311G>T (p.Gly104Val) in Ashkenazi Jews (carrier frequency ~1/99; PMID 35943032); COLEC10 c.807_810delCTGT in Apulia, Italy (PMID 34740859).
  - **Modifier genes:** Model-organism data suggest other complement components (MASP-2, factor B, C3) may modify skeletal severity (PMID 41774788, model organism).
- **Environmental risk factors:** None established. 3MC is a monogenic Mendelian disorder; no toxin, infectious, lifestyle, occupational, age or sex exposure is a known cause. (Not applicable.)
- **Protective factors:** No genetic or environmental protective factors described for the developmental syndrome. (Free **L-fucose** is protective against CL-11-mediated *renal ischemia-reperfusion injury* in mice — PMID 31914693 — but this concerns adult acquired injury, not the developmental syndrome.)
- **Gene–environment interactions:** None documented for 3MC syndrome. (Not applicable.)

---

## 3. Phenotypes

*Frequencies drawn largely from a 7-patient cohort (PMID 41703727) and case series (PMIDs 36503917, 26789649). Onset is congenital/prenatal for structural features; course is generally stable/non-progressive (malformative) with lifelong sequelae.*

| Phenotype | Type | HPO term | Frequency / notes |
|---|---|---|---|
| Hypertelorism | physical/craniofacial sign | HP:0000316 | Very frequent; core gestalt |
| Blepharophimosis | physical sign | HP:0000581 | Frequent; core gestalt |
| Blepharoptosis (ptosis) | physical sign | HP:0000508 | 7/7 in cohort; core gestalt |
| Highly arched eyebrows | physical sign | HP:0002553 | 7/7; core gestalt |
| Epicanthus inversus | physical sign | HP:0000537 | Frequent |
| Downslanted palpebral fissures | physical sign | HP:0000494 | Frequent |
| Cleft lip and/or palate (often bilateral) | physical malformation | HP:0000202 / HP:0000175 | ~6/7 (86%); variable — may be absent |
| Postnatal growth deficiency / short stature | clinical sign | HP:0008897 / HP:0004322 | Frequent |
| Global developmental delay / intellectual disability | behavioral/cognitive | HP:0001263 / HP:0001249 | Common (7/7 neuromotor delay in cohort); variable severity, may be absent |
| Hearing loss | lab/functional sign | HP:0000365 | ~4/7 (57%) |
| Caudal appendage / prominent elongated coccyx (sacral protuberance) | physical sign | HP:0100541 (tail-like) / sacral appendage | ~4/7; relatively specific diagnostic clue |
| Craniosynostosis | physical sign | HP:0001363 | Subset |
| Radioulnar synostosis | physical sign | HP:0003042 | Subset; limb feature |
| Genital anomalies (e.g., hypospadias, cryptorchidism) | physical sign | HP:0000078 / HP:0000047 / HP:0000028 | Subset |
| Vesicorenal anomalies (horseshoe/pelvic kidney, reflux) | physical sign | HP:0000119 / HP:0000085 | Subset |
| Congenital heart disease (e.g., PDA) | physical sign | HP:0001627 / HP:0001643 | ~2/7 (29%) |
| Anterior chamber / anterior-segment dysgenesis | ophthalmic sign | HP:0007700 | Subset (notably Michels-type) |
| Umbilical / periumbilical anomalies, umbilical hernia | physical sign | HP:0001537 | ~6/7 in recent cohort |
| Clinodactyly of 5th finger | physical sign | HP:0004209 | Subset |
| High myopia | ophthalmic sign | HP:0011003 | Reported |
| Behavioral/psychiatric (ADHD, ODD, depression) | behavioral | HP:0007018 / — | Case-reported comorbidity (PMID 37463393) |

- **Age of onset:** Congenital/prenatal (structural malformations detectable prenatally — bilateral cleft lip/palate + sacral protuberance + renal anomaly; PMID 32441374). Growth deficiency is *postnatal*.
- **Severity:** Variable (mild to severe), even within the same gene and family (PMID 29407414 describes an adult with the facial gestalt but without cleft lip/palate, intellectual disability, or short stature).
- **Progression:** Non-progressive/stable malformative disorder; sequelae are lifelong.
- **Quality-of-life impact:** Cleft repair, hearing loss, developmental delay, short stature and limb/skeletal anomalies affect feeding, speech, hearing, mobility and learning; no formal EQ-5D/SF-36 studies exist for this ultra-rare disease (not available).

---

## 4. Genetic / Molecular Information

- **Causal genes (HGNC / locus / OMIM gene / product):**
  - **MASP1** — HGNC:6901; 3q27.3; *600521; encodes **MASP-1** and **MASP-3** (alternative splicing). 3MC-causing variants are truncating, or **missense within exon 12** encoding the MASP-3-specific C-terminal serine protease domain (PMID 29407414).
  - **COLEC11** — HGNC:17213; 2p25.3; *612502; encodes **collectin-11 (CL-K1 / CL-11 / collectin kidney-1)**.
  - **COLEC10** — HGNC:2311; 8q24.12; *607620; encodes **collectin-10 (CL-L1 / collectin liver-1)**.
- **Representative pathogenic variants (all germline, biallelic):**
  - COLEC11 p.Gly204Ser — associated with undetectable serum protein (PMID 25912189, in vitro).
  - COLEC10 p.Arg9Ter (c.25C>T), p.Gly77Glufs*66 (c.226delA), p.Cys176Trp (c.528C>G) — impair CL-L1 expression/secretion (PMID 28301481, in vitro).
  - COLEC10 c.311G>T; p.Gly104Val — Ashkenazi Jewish founder variant (PMID 35943032).
  - COLEC10 c.807_810delCTGT; p.Cys270Serfs*33 (loss of natural stop, +24 aa) — Apulian founder (PMID 34740859).
  - COLEC10 c.128_129delCA; p.Thr43AsnfsTer9 — Iranian, first homozygous frameshift (PMID 34636477).
  - MASP1 c.310C>T; p.Gln104Ter — nonsense (PMID 33765348).
  - MASP1 homozygous ~2 kb intragenic deletion partially affecting exon 12; also exon-level deletions (PMIDs 29407414, 41703727) — may be missed by standard exome pipelines.
- **Variant classification & type:** Pathogenic/likely pathogenic per ACMG/AMP; predominantly **loss-of-function** — nonsense, frameshift, splice, intragenic/exon-level deletions, and secretion-impairing missense. **Functional consequence = loss of function** (protein deficiency or non-secretion). No gain-of-function or dominant-negative mechanism reported.
- **Allele frequency:** Causal alleles are rare/absent in gnomAD except population-specific founders (Ashkenazi COLEC10 carrier freq ≈1.01%, PMID 35943032).
- **Somatic vs germline:** Exclusively **germline**, biallelic (autosomal recessive). No somatic/COSMIC relevance.
- **Modifier genes:** Complement components MASP-2, factor B, C3 modulate skeletal phenotype in mice (PMID 41774788, model organism).
- **Epigenetics:** No disease-specific methylation/histone signature reported (not available).
- **Chromosomal abnormalities:** None characteristic; the disorder is caused by single-gene point/indel/small-deletion variants (some detectable only by careful CNV analysis of WES/WGS; PMID 29407414).

**Suggested gene/GO annotations:** MASP1/COLEC11/COLEC10; GO:0001867 (complement activation, lectin pathway), GO:0030246 (carbohydrate binding), GO:0005509 (calcium ion binding).

---

## 5. Environmental Information

- **Environmental factors:** None known. (Not applicable — Mendelian disorder.)
- **Lifestyle factors:** None known (not applicable).
- **Infectious agents:** None (not applicable). Note the biological irony that the causative genes are innate-immune anti-microbial pattern-recognition molecules, but the syndrome itself is developmental, not infectious.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**
Biallelic LOF variant in MASP1/COLEC11/COLEC10 → deficient or mis-secreted collectin (CL-K1 or CL-L1) or non-functional MASP-3 → loss of the **CL-K1·MASP-3 chemoattractant guidance cue** for **cranial neural crest cells (cNCC)** → aberrant NCC migration/differentiation → malformation of NCC-derived and midline structures (craniofacial skeleton, palate, heart outflow, genitourinary tract, vertebral/coccygeal elements) → clinical phenotype (PMID 21258343).

- **Molecular pathways:** Lectin pathway of complement (and its link to the alternative pathway). CL-K1/CL-L1 form Ca²⁺-dependent heteromeric collectin complexes that associate with MASP-1/2/3 (PMID 27782323). **MASP-3 is the exclusive pro-factor D activator in resting blood, linking the lectin and alternative pathways** (PMID 27535802: *"activated MASP-3 is the exclusive pro-FD activator in resting blood, which demonstrates a fundamental link between the lectin and alternative pathways."*).
- **Cellular processes:** **Neural crest cell migration** (GO:0001755) — CL-K1 acts as a directional guidance cue (PMID 21258343). Also **osteoclast differentiation** (GO:0030316) — CL-11 regulates osteoclastogenesis complement-dependently (PMID 41774788, model organism/in vitro).
- **Protein dysfunction:** LOF via impaired **secretion** and loss of **Ca²⁺ binding** in the carbohydrate-recognition domain (CRD). Disease mutations do not necessarily block folding/oligomerization in vitro, but abolish Ca²⁺ binding and secretion, producing serum protein deficiency (PMID 25912189, in vitro).
- **Metabolic/biochemical:** CL-K1 recognizes **high-mannose oligosaccharides** and **L-fucose** on stressed/altered self-surfaces (PMIDs 25912189, 31914693). Enzymatically, MASP-3 has low amidolytic activity relative to other C1r/C1s/MASP proteases (PMID 23861840, in vitro/structural).
- **Immune involvement:** The causative molecules are innate-immune complement effectors; however, 3MC patients are not primarily immunodeficient — the phenotype reflects the **developmental (non-immune) moonlighting role** of these proteins ("a broader functionality of the complement system than previously anticipated," PMID 27782323).
- **Tissue-damage mechanism (adult context):** In acquired renal ischemia-reperfusion injury, CL-11 binds a fucosylated damage ligand on tubular epithelium and triggers complement/C5b-9 injury — mechanistically informative but distinct from the developmental syndrome (PMIDs 28663231, 31914693, model organism).
- **Molecular profiling / omics / single-cell / CRISPR screens:** No disease-specific transcriptomic, proteomic, metabolomic or functional-genomics screens published for 3MC (not available); mechanistic evidence is from targeted zebrafish morphants, mouse expression/knockout, and in vitro biochemistry.

**Suggested ontology terms:** GO:0001755 (neural crest cell migration), GO:0001867 (lectin-pathway complement activation), GO:0030316 (osteoclast differentiation), GO:0045087 (innate immune response); **CL:0000333** (migratory neural crest cell / cranial NCC), CL:0000138 (chondrocyte), CL:0000092 (osteoclast); CHEBI:2181 (L-fucose), CHEBI:29108 (calcium(2+)), CHEBI:37671 (high-mannose oligosaccharide/mannose).

---

## 7. Anatomical Structures Affected

- **Organ / system level:**
  - **Craniofacial skeleton & face** (UBERON:0001456 face; UBERON:0001716 secondary palate) — cleft lip/palate, hypertelorism, dysmorphism.
  - **Skull sutures** (UBERON:0000905) — craniosynostosis.
  - **Eyes / periocular** (UBERON:0000970) — blepharophimosis, ptosis, anterior-segment dysgenesis (UBERON:0000481 anterior chamber).
  - **Skeleton / limbs** — radioulnar synostosis (radius UBERON:0001423 / ulna UBERON:0001424); vertebral column/**coccyx** (UBERON:0009832) — caudal appendage.
  - **Kidney & urinary tract** (UBERON:0002113) — horseshoe/pelvic kidney, vesicoureteral reflux.
  - **Genitalia** (UBERON:0000990) — genital anomalies.
  - **Heart** (UBERON:0000948) — congenital heart disease (e.g., PDA).
  - **Ear / auditory system** (UBERON:0001690) — hearing loss.
  - **CNS** — developmental delay/cognitive impairment (functional).
- **Tissue / cell level:** Connective/skeletal tissue (cartilage, bone) and epithelial (palatal) tissue; the key targeted cell population is the **cranial neural crest cell (CL:0000333)** and its derivatives (chondrocytes, cranial mesenchyme); osteoclasts implicated in skeletal maintenance (PMID 41774788).
- **Subcellular level:** Secreted proteins traffic through the **endoplasmic reticulum / secretory pathway** (GO:0005783 ER; GO:0005576 extracellular region); LOF mutations cause ER retention / secretion failure (PMID 25912189).
- **Localization / lateralization:** Malformations are typically **bilateral/midline** (bilateral cleft lip/palate, hypertelorism, radioulnar synostosis often bilateral), consistent with a midline/symmetric developmental patterning defect.

---

## 8. Temporal Development

- **Onset:** **Congenital** — structural anomalies arise during embryogenesis and are detectable **prenatally** (first prenatal diagnosis: bilateral cleft lip/palate + sacral abnormality + pelvic kidney + brachycephaly; PMID 32441374). Growth deficiency is **postnatal**.
- **Onset pattern:** Non-acute; features are present from birth (insidious/static developmental).
- **Progression:** Non-progressive malformative syndrome; **stable** course. Skeletal contractures or scoliosis may require intervention over time (e.g., knee flexion contracture managed with a Taylor Spatial Frame — PMID 34589314).
- **Disease course / duration:** Chronic, lifelong; individuals can survive to adulthood (PMID 29407414 describes a 21-year follow-up in an adult).
- **Remission / critical periods:** No remission (structural). The critical window is **embryonic craniofacial neural-crest migration**; interventions are corrective/supportive postnatally rather than preventive of the malformation.

---

## 9. Inheritance and Population

- **Epidemiology:** Ultra-rare; **<50** molecularly confirmed COLEC11/MASP1 patients reported as of 2020 (PMID 32441374), with additional COLEC10 cases since. Formal prevalence/incidence per 100,000 is **not established** (not available).
- **Inheritance:** **Autosomal recessive** (all three genes) (PMIDs 21258343, 28301481).
- **Penetrance / expressivity:** Presumed high penetrance for a recognizable phenotype in biallelic carriers, but **highly variable expressivity** (mild adult cases lacking cleft/ID/short stature — PMID 29407414).
- **Genetic anticipation:** Not applicable (no repeat expansion).
- **Germline mosaicism:** Not reported.
- **Founder effects / consanguinity:** Strong role of **consanguinity**; documented founders — Ashkenazi Jewish COLEC10 c.311G>T (**carrier frequency 1 in 99**, PMID 35943032) and Apulian (Italian) COLEC10 c.807_810delCTGT (PMID 34740859).
- **Carrier frequency:** ≈1.01% in Ashkenazi Jews for the COLEC10 founder allele; otherwise very rare (PMID 35943032).
- **Population demographics:** Cases reported worldwide (Turkey/Kurdish, Iran, Italy, Mexico, Ashkenazi Jewish, and others), often from consanguineous or founder populations. **Sex ratio:** roughly equal (autosomal; cohort of 7 had 5 F / 2 M — small-sample skew, PMID 41703727). **Age distribution:** predominantly diagnosed in infancy/childhood.

---

## 10. Diagnostics

- **Clinical recognition:** Diagnosis is suspected on the **facial gestalt** (hypertelorism, blepharophimosis, blepharoptosis, highly arched eyebrows) plus cleft lip/palate and — a relatively specific clue — a **caudal appendage** (PMIDs 34899147, 26789649).
- **Genetic testing (confirmatory, gold standard):**
  - **Whole-exome (WES) / whole-genome (WGS) sequencing** or a **3MC/multiple-congenital-anomaly gene panel** covering **MASP1, COLEC11, COLEC10**. Important caveat: some **clinical exome panels omit COLEC10**, causing missed diagnoses — targeted Sanger of COLEC10 may be needed (PMID 34740859).
  - **CNV / deletion analysis:** exon-level and intragenic deletions occur (MASP1) and can be missed by routine pipelines — require careful visual/CNV analysis of WES/WGS (PMIDs 29407414, 41703727).
  - Single-gene / Sanger for founder alleles (e.g., Ashkenazi COLEC10 c.311G>T).
  - Karyotype/FISH/mtDNA/repeat-expansion testing: not indicated (normal/uninformative).
- **Biomarkers / functional assays:** Serum/plasma **CL-K1 or CL-L1 levels** may be reduced/undetectable with secretion-impairing variants (PMID 25912189), but levels can be **normal** despite pathogenic variants (PMID 34740859) — so protein level is supportive, not definitive.
- **Imaging:** Prenatal **ultrasound** (facial clefts + sacral/spinal defect + renal anomaly; PMID 32441374); postnatal skeletal survey/radiographs (radioulnar synostosis, craniosynostosis, coccygeal appendage); renal ultrasound; echocardiography; audiology; ophthalmologic exam (anterior-segment).
- **Clinical criteria / differential diagnosis:** No formal consensus criteria. Differential includes other blepharophimosis–ptosis syndromes (e.g., BPES), oral-facial-clefting syndromes, Fraser syndrome, and other craniofacial-limb-renal syndromes; the **caudal appendage + radioulnar synostosis + facial gestalt** combination and molecular confirmation distinguish 3MC (PMID 35943032 notes 3MC should be in the differential for short stature + radioulnar synostosis + cleft lip/palate).
- **Screening:** **Carrier / cascade screening** in founder populations (Ashkenazi Jewish COLEC10) and consanguineous families; **prenatal molecular testing** feasible once a family variant is known (PMID 32441374). No newborn-screening program exists.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** No formal survival statistics; the disorder is generally **compatible with survival to adulthood** (PMID 29407414, 21-year follow-up). Severe multi-organ involvement (cardiac, renal) can affect prognosis in individual cases.
- **Morbidity / function:** Chronic disability from cognitive impairment, hearing loss, short stature, cleft-related speech/feeding issues, and skeletal/limb constraints (radioulnar synostosis, contractures). Variable — some individuals have mild, near-normal cognition (PMID 29407414).
- **Quality-of-life measures:** No disease-specific QoL data (not available).
- **Complications:** Cleft-related feeding/speech difficulties and otitis/hearing loss; renal anomalies may predispose to urinary complications; skeletal contractures/scoliosis; psychiatric comorbidity reported (ADHD/ODD/depression; PMID 37463393).
- **Recovery / prognostic factors:** Malformations are static; outcomes improve with corrective surgery, hearing rehabilitation, and developmental support. Prognosis is modulated by severity of cardiac/renal/CNS involvement. No validated prognostic biomarkers.

---

## 12. Treatment

*No disease-modifying or gene-specific therapy exists. Management is multidisciplinary, symptomatic, and supportive.*

- **Pharmacotherapy:** None specific to 3MC. Symptomatic (e.g., stimulants/SSRIs for comorbid ADHD/depression as clinically indicated; PMID 37463393). No pharmacogenomic considerations established. *(NCIT: Supportive Care; Symptomatic Treatment.)*
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** None approved or in trials for 3MC (not applicable). The lectin-pathway/CL-11 axis is a therapeutic target in *acquired renal IRI* (L-fucose decoy strategy, PMID 32472330, model organism) — not for the developmental syndrome.
- **Surgical / interventional:** **Cleft lip and palate repair** (NCIT: Cleft Lip Repair / Cleft Palate Repair); craniofacial/craniosynostosis surgery; ptosis/blepharophimosis correction; orthopedic correction of limb contractures/synostosis (e.g., **Taylor Spatial Frame** for knee flexion contracture, PMID 34589314); urologic/genital corrective surgery as needed.
- **Supportive / rehabilitative:** **Hearing aids/audiologic management**; speech therapy; physical/occupational therapy; growth and nutritional monitoring; developmental/educational support; ophthalmologic care.
- **Treatment strategy:** Individualized, coordinated by clinical genetics + craniofacial/plastic surgery, ENT/audiology, orthopedics, urology/nephrology, cardiology, ophthalmology, and developmental pediatrics. **Genetic counseling** is integral.
- **Experimental treatments / trials:** None registered specifically for 3MC (not available).

**Suggested NCIT terms:** Supportive Care; Surgical Procedure; Cleft Lip Repair; Cleft Palate Repair; Physical Therapy; Genetic Counseling; Hearing Aid.

---

## 13. Prevention

- **Primary prevention:** Not preventable once conceived (congenital genetic disorder). Preconception risk reduction via **genetic counseling** for consanguineous couples and known-carrier families.
- **Secondary prevention / early detection:** **Prenatal molecular diagnosis** and **prenatal ultrasound** (facial clefts + sacral/renal anomalies) enable early identification and reproductive planning (PMID 32441374). **Preimplantation genetic testing (PGT-M)** is an option when the familial variant is known.
- **Genetic screening:** **Carrier and cascade screening** — high-yield in the Ashkenazi Jewish population for COLEC10 c.311G>T (carrier ~1/99) and in consanguineous/founder populations (PMID 35943032).
- **Counseling:** Autosomal-recessive recurrence risk 25% per pregnancy for carrier couples; molecular confirmation "allows for alternate reproductive options" (PMID 32441374).
- **Tertiary prevention:** Early cleft repair, hearing rehabilitation, developmental therapy, and orthopedic/urologic surveillance to limit complications.
- **Immunization / public-health / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy of gene orthologs:** MASP1, COLEC11, COLEC10 are conserved in vertebrates — **Mus musculus** (NCBI Taxon 10090), **Danio rerio** (7955), **Homo sapiens** (9606).
- **Naturally occurring animal disease:** No naturally occurring 3MC-equivalent Mendelian disease is catalogued in companion animals/livestock (OMIA — not available). Phenotypes are known only from engineered/experimental models.
- **Comparative biology / conservation:** The lectin complement pathway and its developmental role are evolutionarily conserved; zebrafish colec11/masp1 knockdown reproduces craniofacial and pigmentary defects (PMID 21258343), demonstrating conserved mechanism.
- **Transmission / zoonosis:** Not applicable (genetic, non-transmissible).

---

## 15. Model Organisms

- **Zebrafish (*Danio rerio*, ZFIN):** **Morpholino knockdown (morphants)** of *colec11* or *masp1* produce **pigmentary defects and severe craniofacial abnormalities** — the key model recapitulating the human craniofacial phenotype and demonstrating the neural-crest guidance mechanism (PMID 21258343, model organism). *Recapitulation: strong for craniofacial/neural-crest features.*
- **Mouse (*Mus musculus*, MGI):**
  - **Expression studies:** CL-K1 is highly expressed in embryonic craniofacial cartilage, heart, bronchi, kidney, and vertebral bodies (PMID 21258343); COLEC10/CL-L1 is expressed in the base membrane of the developing palate (PMID 28301481) — spatially concordant with affected human structures.
  - **Knockouts:** CL-11 (Colec11) knockout alone does **not** reproduce skeletal abnormalities; **combined** CL-11 + MASP-2 / factor B / C3 deficiency causes vertebral bone loss and spinal curvature via impaired osteoclastogenesis (PMID 41774788, model organism) — a *limitation* (single-gene mouse KO under-recapitulates the human skeletal phenotype) and a clue that complement modifiers matter.
- **In vitro / cellular models:** Mammalian expression systems demonstrating that disease mutations block CL-K1/CL-L1 secretion and Ca²⁺ binding (PMIDs 25912189, 28301481); **human iPSC-derived osteoclasts** showing CL-11 dependence (PMID 41774788); recombinant MASP-3 serine-protease domain structural/enzymatic studies (PMID 23861840).
- **Model limitations:** Mouse single-gene KOs incompletely reproduce the full malformation spectrum (skeletal features require compound complement deficiency); morpholino zebrafish models capture craniofacial/pigment phenotypes but are transient knockdowns.
- **Resources:** ZFIN (zebrafish), MGI/IMPC (mouse), Cellosaurus (iPSC lines).

---

## Evidence Source Summary

| Domain | Evidence type | Key PMIDs |
|---|---|---|
| Gene discovery (MASP1, COLEC11) | Human + zebrafish + mouse | 21258343 |
| Gene discovery (COLEC10) | Human + mouse + in vitro | 28301481 |
| Mutation mechanism (secretion, Ca²⁺) | In vitro / structural | 25912189, 23861840 |
| Complement pathway link (MASP-3→factor D) | In vitro | 27535802, 27782323 |
| Phenotype spectrum & frequencies | Human cohorts/case series | 41703727, 36503917, 26789649, 29407414 |
| Founder allele / carrier frequency | Human population | 35943032, 34740859, 34636477, 33765348 |
| Prenatal diagnosis | Human case | 32441374 |
| Skeletal/osteoclast mechanism | Mouse + iPSC | 41774788 |
| Renal CL-11/fucose (adult context) | Mouse / review | 31914693, 32472330, 28663231, 27286717 |
| Orthopedic management | Human case | 34589314 |
| Psychiatric comorbidity | Human case | 37463393 |

---

## Limitations and Future Directions

- **Ultra-rarity:** <~100 molecularly confirmed patients; frequencies are from small cohorts and case reports, limiting precision of penetrance/expressivity and genotype–phenotype correlation.
- **Genetic heterogeneity:** Some clinically typical, consanguineous patients lack variants in the three known genes (PMID 26789649) — additional lectin-pathway genes likely remain to be discovered.
- **No omics datasets:** No published transcriptomic/proteomic/metabolomic/single-cell profiling of patient tissues; mechanism rests on targeted models and biochemistry.
- **Future directions:** Deeper phenotyping registries; CNV-aware sequencing (to capture exon-level deletions); functional CL-K1/CL-L1 assays as adjunct diagnostics; delineating the neural-crest guidance mechanism at single-cell resolution; exploring complement modifiers of skeletal severity.


## Artifacts

- [OpenScientist final report](3MC_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](3MC_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 19 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 61 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 1 |
| Unverifiable | 6 |
| Terms whose name was checked | 30 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 18 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0018721` (1 mention) - the report calls it "3MC syndrome"; MONDO calls it **obsolete rare combined vascular malformation**
- `HP:0000316` (1 mention) - the report calls it "physical/craniofacial sign"; HP calls it **Hypertelorism**
- `HP:0000581` (1 mention) - the report calls it "physical sign"; HP calls it **Blepharophimosis**
- `HP:0000508` (1 mention) - the report calls it "physical sign"; HP calls it **Ptosis**
- `HP:0002553` (1 mention) - the report calls it "physical sign"; HP calls it **Highly arched eyebrow**
- `HP:0000537` (1 mention) - the report calls it "physical sign"; HP calls it **Epicanthus inversus**
- `HP:0000494` (1 mention) - the report calls it "physical sign"; HP calls it **Downslanted palpebral fissures**
- `HP:0000365` (1 mention) - the report calls it "lab/functional sign"; HP calls it **Hearing impairment**
- `HP:0100541` (1 mention) - the report calls it "tail-like"; HP calls it **Femoral hernia**
- `HP:0001363` (1 mention) - the report calls it "physical sign"; HP calls it **Craniosynostosis**
- `HP:0003042` (1 mention) - the report calls it "physical sign"; HP calls it **Elbow dislocation**
- `HP:0007700` (1 mention) - the report calls it "ophthalmic sign"; HP calls it **Ocular anterior segment dysgenesis**
- `HP:0001537` (1 mention) - the report calls it "physical sign"; HP calls it **Umbilical hernia**
- `HP:0004209` (1 mention) - the report calls it "physical sign"; HP calls it **Clinodactyly of the 5th finger**
- `HP:0011003` (1 mention) - the report calls it "ophthalmic sign"; HP calls it **High myopia**
- `CHEBI:37671` (1 mention) - the report calls it "high-mannose oligosaccharide/mannose"; CHEBI calls it **(1->3)-beta-D-glucan**
- `UBERON:0000970` (1 mention) - the report calls it "Eyes / periocular"; UBERON calls it **eye**
- `UBERON:0002113` (1 mention) - the report calls it "Kidney & urinary tract"; UBERON calls it **kidney**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `UBERON:0000905` (1 mention), reported as "Skull sutures" - UBERON does not contain this term
- `UBERON:0009832` (1 mention), reported as "coccyx" - UBERON does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `MONDO:0018721` (obsolete rare combined vascular malformation) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0001755` (2 mentions) - the report calls it "Neural crest cell migration", "Cellular processes:** **Neural crest cell migration", "neural crest cell migration"; GO calls it **neural crest cell migration**
- `CHEBI:2181` (1 mention) - the report calls it "L-fucose"; CHEBI calls it **L-fucopyranose**, and lists "(-)-L-Fucose" among its other names
- `UBERON:0000990` (1 mention) - the report calls it "Genitalia"; UBERON calls it **reproductive system**, and lists "genitalia" among its other names
- `UBERON:0001690` (1 mention) - the report calls it "Ear / auditory system"; UBERON calls it **ear**, and lists "auditory apparatus" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0001867` - called "complement activation, lectin pathway", "lectin-pathway complement activation"
- `GO:0001755` - called "Neural crest cell migration", "Cellular processes:** **Neural crest cell migration", "neural crest cell migration"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.