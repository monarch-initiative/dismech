---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-28T23:45:37.660144'
end_time: '2026-08-29T00:01:20.624501'
duration_seconds: 942.97
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ring Chromosome 14 Syndrome
  mondo_id: ''
  category: Genetic
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
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 12
  num_turns: 45
  total_cost_usd: 4.5275824999999985
  session_id: c1a5786e-686a-4b57-8d37-48fb97e181db
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 1
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 22
reference_validation:
  total_references: 33
  verified: 33
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 33
  on_topic: 25
  off_topic: 1
  off_topic_references:
  - PMID:22579566
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 175
  verified: 172
  not_found: 0
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 24
  labels_matching: 4
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: MONDO:0014708
    reported_labels:
    - MONDO
    ontology_label: ring chromosome 14
  - term_id: HP:0000752
    reported_labels:
    - large proportion of patients" **[verify]
    ontology_label: Hyperactivity
  - term_id: HP:0000733
    reported_labels:
    - Frequent
    ontology_label: Motor stereotypy
  - term_id: HP:0002360
    reported_labels:
    - Less frequent
    ontology_label: Sleep disturbance
  - term_id: HP:0002205
    reported_labels:
    - "Recurring features include \u2026 increased incidence of infections, particularly\
      \ respiratory infections\" **[verify]"
    ontology_label: Recurrent respiratory infections
  - term_id: HP:0006532
    reported_labels:
    - Spectrum "from recurrent upper airways infections to severe pneumonia" **[verify]
    ontology_label: Recurrent pneumonia
  - term_id: UBERON:0001007
    reported_labels:
    - feeding difficulty, dysphagia, GERD, celiac disease
    ontology_label: digestive system
  - term_id: UBERON:0001130
    reported_labels:
    - scoliosis, kyphosis
    ontology_label: vertebral column
  - term_id: UBERON:0004288
    reported_labels:
    - osteopenia/osteoporosis
    ontology_label: skeleton
  - term_id: UBERON:0001015
    reported_labels:
    - hypotonia
    ontology_label: musculature
  - term_id: GO:0005794
    reported_labels:
    - site of IgG N-glycan maturation
    ontology_label: Golgi apparatus
  - term_id: NCIT:C121351
    reported_labels:
    - implied by multidisciplinary model
    ontology_label: Occupational Therapy
  - term_id: NCIT:C15240
    reported_labels:
    - de novo, low recurrence risk
    ontology_label: Genetic Counseling
  labels_variant: 7
  obsolete_terms:
  - term_id: GO:0016458
    ontology_label: obsolete gene silencing
  - term_id: GO:0006486
    ontology_label: obsolete protein glycosylation
    replaced_by: GO:0009101
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ring Chromosome 14 Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Ring Chromosome 14 Syndrome** covering all of the
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

# Ring Chromosome 14 Syndrome — Comprehensive Research Report

**Prepared:** 2026-08-28 · **Target:** `Ring_Chromosome_14` · **MONDO:0014708**
**Scope:** disease-knowledge-base curation input (dismech schema sections 1–15)

> **Snippet-verification caveat.** Several quotations below were extracted from full-text HTML/PDF via automated fetch and summarization. Before any of these is used as an evidence `snippet:` in `kb/disorders/Ring_Chromosome_14.yaml`, it **must** be re-verified against a `just fetch-reference PMID:…` cache — `just count-verified-snippets` / `just validate-references` is the gate, not this report. Quotes I am confident are verbatim complete abstracts (Zollino 2012 PMID:22579566→22564756, Bershteyn 2014 PMID:24413397) are marked **[abstract-verbatim]**. Everything else is marked **[verify]**.

---

## 1. Disease Information

### Overview

Ring chromosome 14 syndrome (r(14) syndrome) is an ultra-rare constitutional chromosomal disorder in which one copy of chromosome 14 is circularized after breakage in the short and long arms with end-to-end reunion, usually with loss of the 14q terminal segment. It is defined clinically by the near-obligate combination of **early-onset, drug-resistant epilepsy**, **moderate-to-severe intellectual disability with disproportionate language impairment**, **postnatal microcephaly**, **a recognizable but subtle facial gestalt**, **retinal pigmentary abnormalities**, and **increased susceptibility to respiratory infection**.

The syndrome's defining puzzle — and the reason it is mechanistically interesting rather than merely a contiguous-gene deletion — is that individuals with *linear* (non-ring) 14q terminal deletions of comparable size do **not** develop the refractory epilepsy or the retinal changes. The ring configuration itself, not simply the deleted gene content, appears to be pathogenic (Vaisfeld et al., *Epilepsia* 2021, PMID:33205446).

### Key identifiers

| Resource | Identifier |
|---|---|
| MONDO | **MONDO:0014708** |
| OMIM | **616606** (RING CHROMOSOME 14 SYNDROME) |
| Orphanet | **ORPHA:1440** |
| ICD-10 | **Q93.2** (Chromosome replaced with ring, dicentric or isochromosome) |
| ICD-11 | **LD7Y** (per ORDO cross-reference) |
| MeSH | **C535487** |
| UMLS / MedGen | **C2930916** / MedGen UID 419284 |
| GARD | 6072 |
| Karyotype (ISCN) | `46,XX,r(14)(p11q32.33)` or `46,XY,r(14)(p11q32.3)` (typical) |

Source: [MedGen 419284](https://www.ncbi.nlm.nih.gov/medgen/419284); [ORDO via OLS4](https://www.ebi.ac.uk/ols4/); [OMIM 616606](https://omim.org/entry/616606).

### Synonyms

- Ring 14 syndrome; Ring14 syndrome; r(14) syndrome; RC14 syndrome
- Ring chromosome 14
- Chromosome 14 ring
- Ring 14
- (Historic/imprecise) "14q ring syndrome"

**Do not conflate with:** *14q terminal deletion syndrome* (linear del(14)(q32.3qter)) or *14q11.2 microdeletion syndrome*. These are separate MONDO concepts, and the whole point of the Vaisfeld 2021 analysis is that the ring and linear forms are phenotypically dissociable.

### Data provenance character

Essentially **all published knowledge is case-level and aggregated from small series** — there is no population EHR-derived cohort of meaningful size. The largest coherent clinical datasets are:

- Zollino et al. 2012, own series of **27 patients** plus literature review (PMID:22564756)
- Giovannini et al. 2013, **22 patients** with EEG phenotyping (PMID:24116895)
- The **Ring14 International clinical database** (~54 patients; genetics, growth, neurology, comorbidities, therapies) — [ring14.org](http://www.ring14.org/eng/120/clinical-database/)
- The 2017 ad hoc task-force guideline, consensus over the above (PMID:28399883 / PMC5387247)

EHR-derived signal exists but is thin: Barbour et al. (*Epilepsia* 2024, PMID:38795333) attempted incidence estimation for 28 rare epilepsies from NYC EHR text search and explicitly noted that "data were limited for" ring chromosome 14 and similar "genetic epilepsies with nonspecific clinical features" **[verify]**.

---

## 2. Etiology

### Primary cause

A **de novo structural chromosomal rearrangement**: chromosome 14 forms a ring, requiring two breakpoints — one in the short arm (an acrocentric, gene-poor p arm) and one in the long arm — followed by fusion of the broken ends and loss of the intervening terminal material.

Zollino et al. 2012 quantified the molecular spectrum in 27 patients **[abstract-verbatim]**:

> "In our own sample of patients the ring was complete, with no apparent loss of chromosome material, in 6/27 cases, while it showed a small terminal deletion, varying in size from 0.3 to 5 Mb, in the other 21. In two of these a cryptic 14q duplication of 2.5 and 9.7 Mb, respectively, proximal to the deleted segment, was also identified. Deleted rings were 75% paternal and 25% maternal in origin. UPD (14) was excluded in all cases."
> — Zollino M, Ponzi E, Gobbi G, Neri G. *Eur J Med Genet* 2012;55:374–380. **PMID:22564756**, DOI:10.1016/j.ejmg.2012.03.009

Three points from this are curation-critical:

1. **~22% of rings are "complete"** — cytogenetically visible ring, no detectable copy-number loss on array. These patients still have the syndrome. Copy-number loss is therefore *not necessary* for the phenotype.
2. **Parental origin is skewed paternal (3:1)** for deleted rings.
3. **UPD(14) is excluded** — so neither Temple syndrome nor Kagami–Ogata imprinting mechanisms are operating here (an important differential, since chromosome 14 carries the *DLK1-MEG3* imprinted domain at 14q32.2).

Multiple ring-formation mechanisms are described generally for ring chromosomes (Guilherme et al., *BMC Med Genet* 2011, PMID:22151179): breaks in both arms with end-to-end reunion; a break in one arm fusing to the opposite subtelomere; subtelomere–subtelomere fusion; and pure **telomere–telomere fusion** (which yields a complete ring with no loss).

### Risk factors

**Genetic risk factors.** There is no known heritable susceptibility. The rearrangement is sporadic. There is no reported association with parental age, and no recurrent breakpoint-flanking segmental duplication architecture has been established (unlike recurrent microdeletion syndromes). The paternal-origin skew is the only reproducible parent-of-origin signal.

**Modifier candidates (hypothesis-level, not established):**
- The **size of the terminal deletion** (0.3–5 Mb) modifies which 14q32.33 genes are hemizygous — most consequentially the *IGH* locus (immune phenotype) and *PACS2* (epilepsy candidate).
- The **degree of ring mitotic instability** (see §6) plausibly modifies severity, including growth failure and possibly epileptogenicity, but this has never been prospectively correlated with outcome.
- Presence of a **cryptic proximal 14q duplication** (2/27 in Zollino's series) adds a second dosage lesion.

**Environmental risk factors.** None identified. No teratogen, exposure, occupational, maternal-nutritional, or infectious risk factor has been associated with ring chromosome formation in humans. Ionizing radiation and clastogens can produce ring chromosomes *somatically* in vitro and in irradiated individuals, but no epidemiological link to constitutional ring 14 exists. **Treat this as "no evidence," not "no association."**

**Protective factors.** None identified — genetic or environmental. Not applicable to a de novo structural event.

**Gene–environment interaction.** No established GxE. The one arguably interaction-shaped observation is that **infection burden interacts with the underlying immune lesion**: hemizygosity of the 14q32.33 immunoglobulin heavy-chain locus plus altered IgG glycosylation (§6) is thought to convert ordinary respiratory pathogen exposure into recurrent/severe pneumonia, which the 2017 guideline names as the leading cause of adult death.

---

## 3. Phenotypes

### 3.1 Neurological — epilepsy (the cardinal feature)

**Frequency: ~100%.** Giovannini et al. 2013 (PMID:24116895), 22 patients:

> "The incidence of epilepsy in patients with r(14) syndrome is virtually 100%, characterized by early onset, polymorphic seizures, and drug-resistant seizures." **[verify]**

Guideline consensus (PMC5387247) **[verify]**:

> "All individuals with r(14) syndrome suffer from epilepsy, which is drug resistant in most cases." Onset "usually occurs in the first months of life."

| Attribute | Value | HPO suggestion |
|---|---|---|
| Onset | First months of life; commonly < 12 months (a Chinese series reported onset 3–24 months in its r(14) cases, PMID:41087847) | HP:0003593 Infantile onset; HP:0003623 Neonatal onset |
| Predominant type | **Focal, with or without secondary generalization** (modern reclassification) | HP:0007359 Focal-onset seizure; HP:0002384 Focal impaired awareness seizure |
| Also seen | Generalized tonic–clonic, myoclonic-tonic, clonic | HP:0002197 Generalized-onset seizure; HP:0002069 Bilateral tonic-clonic seizure; HP:0002123 Generalized myoclonic seizure |
| Status epilepticus | **~50%** of individuals | HP:0002133 Status epilepticus |
| Clustering | Seizures on awakening/falling asleep, in clusters lasting a day or more | HP:0011146? (verify) |
| Drug resistance | **~50% frankly drug-resistant**; remaining 50% variable control | HP:0011348? — prefer free text + `treatments` block |
| Severity | Severe in early childhood | — |
| Course | **Improves with age** — "starting with frequent severe seizures that may ameliorate over time and eventually decrease in frequency during late adolescence" **[verify]** | — |
| Encephalopathic effect | Intense early epileptic activity associated with **regression** of acquired psychomotor/language milestones | HP:0002376 Developmental regression; HP:0200134 Epileptic encephalopathy |

**EEG (Giovannini 2013; guideline)** **[verify]**: slow, unstructured/disorganized background in both wake and sleep; generalized bursts of slow, large, asynchronous waves in frontal and posterior regions; multifocal spikes; complex spike-and-wave over occipital regions; focal spikes with secondary generalization. EEG severity **negatively correlated with cognitive development** — a curation-relevant causal claim (epileptic activity → cognitive outcome, not merely co-occurring).

**Quality-of-life impact:** dominant. Seizure burden, seizure-related injury risk, sleep disruption, and caregiver vigilance are the primary drivers of family burden (SanInocencio et al. 2026, below).

### 3.2 Neurodevelopmental / cognitive / behavioral

| Phenotype | Frequency | HPO |
|---|---|---|
| Global developmental delay | ~100% | HP:0001263 |
| Intellectual disability, moderate–severe | ~100% ("One consistent feature … is moderate to severe intellectual disability" **[verify]**) | HP:0001249; HP:0002342 (moderate); HP:0010864 (severe) |
| Delayed speech and language development / poor or absent speech | Very frequent; language is "one of the most affected developmental area" **[verify]**; many patients are **nonverbal** | HP:0000750; HP:0002465; HP:0001344 |
| Motor delay — sitting ~12 months; first steps 2–3 y; **some never walk** | Frequent | HP:0001270; HP:0002540 (inability to walk) |
| Hypotonia (generalized, axial) | Very frequent | HP:0001252; HP:0001290 |
| Hyperactivity | "large proportion of patients" **[verify]** | HP:0000752 |
| Motor stereotypies | Frequent | HP:0000733 |
| Autistic traits / full autistic phenotype in some | Frequent traits; formal ASD in a subset | HP:0000729 Autistic behavior; HP:0000717 Autism |
| Aggressive outbursts | Occasional — children "usually good natured" with "only occasional bursts of aggressiveness" **[verify]** | HP:0000718 Aggressive behavior |
| Sleep disorder | Less frequent | HP:0002360 |

Behavior disorders were assigned by Zollino to the **14q32** region (haploinsufficiency mechanism) **[abstract-verbatim]**.

### 3.3 Growth and nutrition

| Phenotype | Note | HPO |
|---|---|---|
| Short stature / shortness of stature | Part of the defining gestalt (Zollino 2009, PMID:19441122; Zollino 2012) | HP:0004322 |
| Postnatal microcephaly | Recurring; **postnatal-onset** specifically | HP:0005484 (postnatal microcephaly); HP:0000252 |
| Failure to thrive / underweight | "Children with r(14) syndrome are extremely underweight and are frequently affected by anorexia that leads to malnutrition." **[verify]** | HP:0001508; HP:0004325 |
| Feeding difficulties, dysphagia/aspiration | Frequent enough to warrant enteral feeding recommendation | HP:0011968; HP:0002015 |
| Intrauterine growth restriction | Reported (GARD) | HP:0001511 |

Growth failure is the classical **"ring syndrome"** phenotype (Kosztolányi) attributed to ring mitotic instability rather than to deleted gene content — see §6.

### 3.4 Craniofacial

The facial gestalt is real but subtle; Vaisfeld 2021 cautions **[verify]**: *"it is very difficult to diagnose any one of the reviewed conditions based on a gestaltic impression."*

Guideline description **[verify]**: "long and sometimes asymmetrical face, full cheeks, large forehead, hypoplastic supraorbital ridges with horizontal eyebrows, strabismus, apparent hypertelorism" — and importantly, "All these features have been reported only in patients with r(14) syndrome carrying a long arm terminal deletion of at least 650 kb."

Case-report-level features (Meza-Espinoza 2024, PMID:39020403) **[verify]**: prominent narrow forehead, sparse short eyebrows, palpebral ptosis, horizontal palpebral fissures, broad nasal bridge, prominent nasal tip, flat philtrum, hypertelorism, midfacial hypoplasia, thin upper lip, crowded teeth, ogival (high-arched) palate, retrognathia, wide neck.

HPO set: HP:0000316 Hypertelorism · HP:0000494 Downslanted palpebral fissures · HP:0000286 Epicanthus · HP:0005280 Depressed nasal bridge · HP:0000457 Depressed nasal ridge · HP:0000463 Anteverted nares · HP:0000369 Low-set ears · HP:0000218 High palate · HP:0000470 Short neck · HP:0005469 Flat occiput · HP:0000268 Dolichocephaly · HP:0000581 Blepharophimosis · HP:0000508 Ptosis · HP:0000347 Micrognathia · HP:0000219 Thin upper lip vermilion · HP:0000678 Dental crowding · HP:0000319 Smooth philtrum · HP:0007874 Almond-shaped palpebral fissure.

Dental management has its own literature: Ivanoff et al., *Folia Med* 2023, PMID:36855970 — "what the dentist should know to manage children with r(14) effectively."

### 3.5 Ophthalmological

Zollino 2012 **[abstract-verbatim]**: ocular abnormalities "consisting mainly of abnormal retinal pigmentation, but also retinitis pigmentosa, strabismus, glaucoma, and abnormal macula."

Guideline **[verify]**: "myopia, strabismus, cataracts, maculopathy, optic nerve damage, glaucoma and anomalies in retinal pigmentation," plus "microphtalmia and colobomas."

Vasconcelos et al., *Ophthalmic Genet* 2019 (PMID:31755799) documented an 11-year-old with **macular yellow dots on multimodal imaging**, arguing for routine ophthalmologic surveillance **[verify]**.

HPO: HP:0000580 Pigmentary retinopathy (annotated "Occasional" in HPOA) · HP:0000510 Retinitis pigmentosa · HP:0007754 Macular dystrophy · HP:0000486 Strabismus · HP:0000545 Myopia · HP:0000518 Cataract · HP:0000501 Glaucoma · HP:0000612 Iris coloboma · HP:0000568 Microphthalmia · HP:0000648 Optic atrophy · HP:0000505 Visual impairment.

**Curation note:** GARD states retinal abnormalities are "typically not affecting vision." The retinal phenotype is a *diagnostic marker* more than a functional burden in most patients — worth capturing as a `notes` distinction rather than assuming visual impairment.

### 3.6 Immune / infectious

| Phenotype | Note | HPO |
|---|---|---|
| Recurrent respiratory infections | "Recurring features include … increased incidence of infections, particularly respiratory infections" **[verify]** | HP:0002205 |
| Severe pneumonia | Spectrum "from recurrent upper airways infections to severe pneumonia" **[verify]** | HP:0006532 |
| Altered immunoglobulin / antibody profile | "Only some individuals with r(14) syndrome have altered immunological and/or antibody profile" **[verify]** — IgA deficiency most cited | HP:0002720 Decreased circulating IgA level *(verify CURIE)*; HP:0004313 Decreased circulating antibody level |

**This is the leading cause of adult mortality** — "Infections are one of the worse prognostic factors and the main cause of death in adulthood" **[verify]**.

### 3.7 Musculoskeletal, GI, other

- **Scoliosis** (HP:0002650) — part of the defining gestalt; assigned by Zollino to 14q32. Kyphosis (HP:0002808) also reported.
- **Juvenile osteoporosis / osteopenia** (HP:0000939 / HP:0000938) — "less frequently observed" **[verify]**
- **Arthritis** (HP:0001369) — less frequent
- **Celiac disease** — less frequent **[verify CURIE]**
- **Gastrointestinal symptoms / GERD / constipation** — "affect many children" **[verify]**
- **Café-au-lait spots** (HP:0000957) — less frequent
- **Lymphedema — "puffy hands and/or feet"** (HP:0001004) — reported by MedlinePlus/GARD; frequency not quantified in the primary series
- **Congenital malformations of heart, kidneys, urinary tract — "very rarely reported"** **[verify]**. This is a discriminating negative: r(14) is *not* a multiple-congenital-anomaly syndrome in the usual sense.

### 3.8 Neuroimaging

Guideline **[verify]**: "Magnetic resonance imaging does not typically detect any specific changes." When abnormal: "mild brain atrophy, abnormalities of the corpus callosum, mild ventricular dilatation, hippocampus anomalies and structural alterations of the cerebellum."

HPO: HP:0002059 Cerebral atrophy · HP:0001274/HP:0002079 corpus callosum abnormality · HP:0002119 Ventriculomegaly · HP:0025100? hippocampal abnormality *(verify)* · HP:0001317 Abnormal cerebellum morphology.

### 3.9 Quality of life — the 2026 patient-centered model

**SanInocencio C, et al. "Development of a patient-centered conceptual disease model in Ring 14 syndrome: a patient-centered model of lived experience." *Qual Life Res* 2026. PMID:41533279, DOI:10.1007/s11136-025-04140-5.**

17 caregivers representing 12 patients; semi-structured interviews. The model spans **patient domains** (cognitive, physical, behavioral, social-emotional, QoL) and **caregiver domains** (mental health, family/social, medical care). Key finding **[verify]**:

> "impacts listed under the patient quality of life domain as well as the caregiver domain are inadequately represented in the literature"

This is the single most important recent addition for QoL curation, and it is explicitly a critique of the existing literature's clinician-centric framing. No EQ-5D/SF-36/PROMIS data exist for r(14).

---

## 4. Genetic / Molecular Information

### 4.1 The lesion

There is **no single causal gene**. The lesion is the ring structure plus variable 14q32.33 hemizygosity.

**Chromosome 14 (GRCh38):** acrocentric, 107,043,718 bp. The p arm is heterochromatic/rDNA-bearing and gene-poor; the p-arm breakpoint (typically p11 or p13) is therefore usually phenotypically silent for coding content but **is central to the position-effect hypothesis** (§6).

**Terminal 14q deletion sizes reported:**
- Zollino 2012 (n=27): **0.3–5 Mb** in 21/27; complete ring in 6/27 **[abstract-verbatim]**
- Zollino 2009 (n=20): **0.65–5 Mb** in 14/20; complete ring in 6/20
- Meza-Espinoza 2024 (n=1): **~1.7 Mb, chr14:105,194,385–106,876,229 (GRCh38), 23 genes** **[verify]**
- Gardner et al. 2024 (PMID:38824650): "Ring Chromosome 14 with a Terminal 14q32.33 Deletion"

### 4.2 Genes in the commonly deleted 14q32.33 interval

Verified coordinates (Ensembl REST, GRCh38):

| Gene | HGNC | Coordinates (GRCh38) | Distance from 14qter | Relevance |
|---|---|---|---|---|
| **PACS2** | hgnc:23794 *(verify)* | chr14:105,300,563–105,398,147 | ~1.65 Mb | **Leading epilepsy candidate.** Recurrent *de novo* missense (p.Glu209Lys) causes DEE-66 (neonatal-onset developmental and epileptic encephalopathy with cerebellar dysgenesis). Deleted whenever the terminal deletion exceeds ~1.65 Mb. |
| **IGHM** (IGH locus) | hgnc:5541 | chr14:105,851,705–105,856,218 (IGH cluster ≈105.6–106.9 Mb) | ~1.2 Mb | **Immunoglobulin heavy-chain locus.** Deleted in essentially all deletion-bearing rings with >~0.2 Mb loss. Guideline explicitly links infection susceptibility to this: "the distal region of 14q contains the genes for heavy chains of antibodies" **[verify]** |

Other genes in the terminal ~2 Mb (for completeness; individually unvalidated for r(14) phenotype): *INF2, ADSS1(ADSSL1), SIVA1, AKT1, ZBTB42, CEP170B, PLD4, AHNAK2, CDCA4, GPR132, JAG2, NUDT14, BRF1, PACS2, TEX22, MTA1, CRIP1/CRIP2, TMEM121, ELK2AP, ADAM6*.

**Assay-relevant caution:** *AKT1* (14q32.33) and *DICER1* (14q32.13) are cancer-relevant genes on this chromosome, but **no increased neoplasia risk has been reported in r(14) syndrome** and *DICER1* lies well proximal to typical ring 14 deletions. Do not curate a tumor-predisposition claim.

### 4.3 The 40 chromosome-14 epilepsy genes (Vaisfeld 2021)

Vaisfeld et al. catalogued **40 epilepsy-related genes across chromosome 14** and analyzed seven in detail **[verify]**:

| Gene | Cytoband | Association |
|---|---|---|
| **CHD8** | 14q11.2 | ASD; seizures in 20–30%; macrocephaly |
| **FOXG1** | 14q12 | Microcephaly, psychomotor delay, drug-resistant early-onset seizures (congenital Rett variant) |
| **OTX2** | 14q22.3 | Eye malformations, pituitary anomalies, possible retinal abnormalities |
| **PSEN1** | 14q24.2 | Alzheimer-associated seizures (late-onset; low relevance) |
| **IRF2BPL** | 14q24.3 | DEE, Lennox–Gastaut-like phenotype |
| **DYNC1H1** | 14q32.31 | Neurological disease; LOF not epilepsy-associated |
| **PACS2** | 14q32.33 | Neonatal-onset DEE with cerebellar dysgenesis |

Crucially, **all of these except *PACS2* lie outside the deleted segment** in ring 14 — they are present in two copies. That is precisely the enigma. Vaisfeld's conclusion **[verify]**:

> "With the exception of FOXG1 and PACS2, none of the genes … has a clear and unquestionable epileptogenic potential."

### 4.4 Zollino's regional assignment (the standing genotype–phenotype model)

From the 2012 abstract **[abstract-verbatim]**:

> "Based on literature review of linear deletions, affecting either the proximal or the distal 14q region, we could deduce that retinal abnormalities and epilepsy map within the proximal 14q11.2-q12 region. Because this region is preserved in all patients with ring 14, we speculate that genes residing in the proximal 14q interval are disregulated through heterochromatinization spreading from the adjacent short arm of the chromosome. Behavior disorders and susceptibility to infections can be assigned to the 14q32 region, haploinsufficiency being the most likely underlying mechanism."

This yields a **two-mechanism model** that should structure the dismech pathophysiology graph:

- **Proximal 14q11.2–q12 (present in 2 copies) → dysregulated by position effect / heterochromatin spreading → epilepsy + retinal abnormalities.** Candidate effector: *FOXG1*.
- **Distal 14q32.33 (hemizygous) → classical haploinsufficiency → behavior disorders + infection susceptibility (IGH), possibly seizures via PACS2.**

Note that Zollino 2009 (PMID:19441122) placed microcephaly and intellectual disability with the proximal group as well; scoliosis with 14q32.

### 4.5 Variant classification, allele frequency, origin

- **Classification:** Not an ACMG sequence-variant question. Reported as a **pathogenic structural/cytogenetic abnormality**; ClinVar/DECIPHER/ECARUCA/dbVar carry the CNV component (terminal 14q32.33 loss) but not the ring topology.
- **Allele frequency:** Not applicable. Terminal 14q32.33 deletions of this size are absent from gnomAD-SV control frequencies at any appreciable level.
- **Origin:** **Germline, de novo**, in the overwhelming majority. Deleted rings 75% paternal / 25% maternal (Zollino 2012) **[abstract-verbatim]**. Somatic mosaicism for ring loss is universal (§6) but is a *secondary* somatic event on a germline lesion.
- **Functional consequence:** Combined **loss of function** (hemizygosity, 14q32.33) and **loss of normal regulation** (position effect on 14q proximal — a qualitative, not quantitative, change).

> **dismech schema note.** For the 14q32.33 genes, `GeneticContext.functional_impact_category: LOSS_OF_FUNCTION` with `allele_type` structural/CNV. For the *proximal* 14q dysregulation, the correct slot is `Descriptor.modifier` — and because the claim is that the locus is "no longer under normal regulatory control" rather than merely running low, `LOSS_OF_FUNCTION` (qualitative, unbound) is defensible over `DECREASED`. Make that trade explicitly per CLAUDE.md guidance.

### 4.6 Modifier genes

None validated. Candidate modifiers, all hypothesis-level: deletion size (determines *PACS2* / *IGH* status); presence of cryptic proximal duplication; degree of somatic ring instability; parental origin (paternal skew — imprinting at *DLK1-MEG3* 14q32.2 is a theoretical but unproven contributor, and UPD(14) was excluded in all Zollino cases).

### 4.7 Epigenetics

This is where the modern mechanistic action is.

- **Heterochromatin spreading / telomere position effect (TPE):** ring formation juxtaposes the acrocentric p-arm heterochromatin (rDNA, satellite) with proximal 14q euchromatin, and removes the native 14q telomere. Guideline **[verify]**: ring formation may cause "perturbation of the epigenetic state of specific genes along chromosome 14," with "heterochromatin spreading and possible repositioning" as proposed mechanisms.
- **Empirical support:** Ferreira et al., *J Appl Genet* 2015 — "Position effect modifying gene expression in a patient with ring chromosome 14." Guideline notes recent studies "confirmed gene expression changes in patients with r(14) syndrome" **[verify]**. Analogous TPE evidence exists for ring 17 (PMC3892072) and transcriptome-level evidence for ring 20 (PMID:33207017).
- **Non-coding RNA gap (Vaisfeld 2021)** **[verify]**: "there is essentially no literature concerning the possible role of untranslated RNAs in the r(14) syndrome," and the 14q32 region "contains the largest cluster of microRNAs in the entire human genome" — the imprinted *DLK1-DIO3* miRNA mega-cluster at 14q32.2. **This is a first-class `KNOWLEDGE_GAP` discussion for the entry.**
- **TADs:** the active NCT06813469 study (below) is testing whether ring formation disrupts topologically associating domains.

### 4.8 Chromosomal abnormality summary

- Constitutional ring chromosome 14, replacing one normal chromosome 14
- Typical ISCN: `46,XX,r(14)(p11q32.33)` / `46,XY,r(14)(p13q32.33)`
- Frequently accompanied *in vivo* by a secondary somatic mosaic: `45,XX,-14 / 46,XX,r(14) / 46,XX,r(14)x2 / 47,XX,r(14),+r(14)` etc.
- Detected by **karyotype** (ring topology) + **array CGH/SNP array** (deletion extent). Array alone will miss a complete ring and will misclassify a deleted ring as a linear terminal deletion — a diagnostically consequential error.

---

## 5. Environmental Information

**Environmental factors:** None causally implicated. Ring chromosome formation is a de novo mitotic/meiotic accident; no toxin, radiation, pollutant, or occupational exposure has been linked to constitutional r(14).

**Lifestyle factors:** None causally implicated in disease occurrence. Post-diagnosis, nutrition is a major *modifying* exposure — anorexia/malnutrition is a named prognostic determinant, and vitamin D insufficiency is prevalent enough that the guideline recommends **double-RDA supplementation (≈800–1,000 IU/day)** prophylactically **[verify]**.

**Infectious agents:** Not causal. But **respiratory pathogens are a first-class disease-modifying exposure** — they act on an established immune lesion and represent the main adult mortality mechanism. This is the one environmental entry that genuinely earns `influences_mechanisms` in the dismech pathograph:

```yaml
environmental:
- name: Recurrent respiratory pathogen exposure
  influences_mechanisms:
  - target: Impaired humoral immunity
    environmental_effect: EXACERBATES
    causal_link_type: DIRECT
```

A second, iatrogenic exposure is documented: **chronic aspiration of cannabis oil** used for seizure control caused **lipoid pneumonia** in a 4-year-old with ring chromosome 14 (Hanzal et al., *Chest* 2025, PMID:40348517) **[verify]** — a real adverse-event signal given how commonly CBD oil is used in this population.

ECTO binding candidates (all require OAK verification against `cache/ecto/`; per the `dismech-terms` rule, *no term beats a bad one*): exposure to respiratory pathogens; oral exposure to cannabidiol. If ECTO has nothing precise, leave unbound with a `review_notes:` waiver recording the search.

---

## 6. Mechanism / Pathophysiology

This is the section that should carry the entry's mechanistic weight. The causal architecture has **four partially independent arms**, and the field explicitly does not know which dominates.

### 6.1 Upstream initiating event

**Ring chromosome 14 formation** — two breakpoints (14p + 14q), end-to-end fusion, telomere loss.

GO: GO:0032200 telomere organization · GO:0006281 DNA repair · GO:0000724 double-strand break repair via homologous recombination · GO:0051276 chromosome organization.

### 6.2 Arm A — Position effect / heterochromatin spreading (→ epilepsy, retinal phenotype)

**Causal chain:**

```
ring formation
  → loss of 14q telomere + juxtaposition of 14p acrocentric heterochromatin to proximal 14q
  → heterochromatin spreading / altered nuclear repositioning (telomere position effect)
  → transcriptional silencing/dysregulation of proximal 14q11.2–q12 genes (2 copies present)
  → reduced FOXG1 (and neighbors) function in developing forebrain
  → abnormal cortical neuron differentiation and excitation/inhibition imbalance
  → early-onset drug-resistant focal epilepsy; microcephaly; retinal pigmentary abnormality
```

This arm explains the central dissociation: linear 14q deletions of matched size cause neither refractory epilepsy nor retinal changes, because they leave the p-arm/telomere relationship intact.

GO: GO:0031507 heterochromatin formation · GO:0016458 gene silencing · GO:0006357 regulation of transcription by RNA Pol II · GO:0007399 nervous system development · GO:0021895 cerebral cortex neuron differentiation · GO:0060384? — prefer GO:0050767 regulation of neurogenesis.
CL: CL:0000540 neuron · CL:0000598 pyramidal neuron · CL:0000617 GABAergic neuron · CL:0000679 glutamatergic neuron · CL:0011005? (verify) · CL:0002586 retinal pigment epithelial cell.
UBERON: UBERON:0000955 brain · UBERON:0000956 cerebral cortex · UBERON:0002421 hippocampal formation · UBERON:0000966 retina.

`biological_scale:` — the heterochromatin/transcription nodes are `MOLECULAR`; neuron differentiation is `CELLULAR`; epilepsy is `ORGANISM`.

### 6.3 Arm B — Ring mitotic instability and dynamic mosaicism (→ growth failure, possible epileptogenic focus)

Rings are structurally unstable. Sister chromatid exchange within a ring generates dicentric and interlocked rings; anaphase bridging and lagging generate ring loss and micronuclei.

Vaisfeld 2021 **[verify]**:
> "Sister chromatid exchanges occurring during mitosis can result in the generation of dicentric or interlocked rings, or lead to ring chromosome loss, creating a mosaic of cells with different functional properties."

And, critically for tissue-specificity:
> the proportion of cells with complete ring loss "is known to be around 20% in peripheral blood cells" — but "it could be higher in areas of the brain contributing to a potential epileptogenic focus."

**Directly measured instability** (Meza-Espinoza et al., *Mol Cytogenet* 2024, PMID:39020403) **[verify]**:
- 30/243 cells (**12.3%**) monosomic for 14 (ring lost)
- 15/243 cells (**6.2%**) with three signals (duplicated/dicentric ring)
- 27/305 (**9%**) interphase cells with micronuclei; FISH confirmed r(14) inside **21/21** micronuclei tested
- Authors: "we were able to verify an instability of the r(14) chromosome, mainly involving anaphasic lags and its exclusion from the nucleus in the form of a micronucleus."

The guideline's counterpoint on the diagnostic side **[verify]**: in blood, "at least 85–90%" of cells harbor the ring, and aneuploid fractions are "usually below the sensitivity of a CGH-array."

**Kosztolányi's "ring syndrome"**: growth failure as the near-universal, chromosome-independent consequence of ring instability ("dynamic mosaicism"), because mosaic monosomic cells have low viability and high death rate. Contemporary opinion has partly shifted toward hemizygous gene loss as the driver of malformations, with dynamic mosaicism retained principally for **growth failure**.

```
ring instability
  → anaphase lag / bridge → micronucleus formation → ring loss
  → mosaic monosomy 14 in a subset of somatic cells
  → cell-cycle arrest / apoptosis / reduced proliferative output
  → generalized growth failure, short stature, postnatal microcephaly
  → (hypothesized) locally high monosomic fraction in cortex → epileptogenic focus
```

GO: GO:0007059 chromosome segregation · GO:0140014 mitotic nuclear division · GO:0007094 mitotic spindle assembly checkpoint signaling · GO:0006915 apoptotic process · GO:0090398 cellular senescence · GO:0008283 cell population proliferation.

### 6.4 Arm C — 14q32.33 haploinsufficiency (→ immune, behavior, ?seizures)

```
terminal 14q32.33 deletion (0.3–5 Mb)
  → hemizygosity of IGH constant-region locus (chr14:~105.6–106.9 Mb)
  → reduced/skewed immunoglobulin heavy-chain repertoire
  → impaired humoral immunity (esp. IgA)
  → recurrent upper-airway infection → severe pneumonia → adult mortality

  → (when deletion >1.65 Mb) hemizygosity of PACS2
  → possible minimally penetrant epileptogenic effect, "enhanced by the formation of the ring"
```

Vaisfeld on *PACS2* **[verify]**: "it may be worth exploring whether haploinsufficiency has a minimally penetrant epileptogenic effect, which is enhanced by the formation of the ring." This is an explicit **two-hit / synergy hypothesis** and should be curated as a `mechanistic_hypotheses` group with `status: EMERGING`, with the relevant `downstream` edges opting in via `hypothesis_groups`.

GO: GO:0002377 immunoglobulin production · GO:0006959 humoral immune response · GO:0016064 immunoglobulin mediated immune response · GO:0002250 adaptive immune response.
CL: CL:0000236 B cell · CL:0000786 plasma cell · CL:0000084 T cell.
UBERON: UBERON:0002405 immune system · UBERON:0001004 respiratory system · UBERON:0002048 lung.

### 6.5 Arm D — Aberrant IgG N-glycosylation (2026, newest)

**Messina A, et al. "IgG Glycosylation Analysis in Patients with Ring14 Syndrome Unveils Novel Pathomechanisms and New Therapy Perspectives." *Biomolecules* 2026;16(6):760. PMID:42352229, DOI:10.3390/biom16060760** (preprint: doi:10.20944/preprints202604.0844.v1)

Six RC14 patients vs. age-matched controls; UHPLC-FLR + high-resolution ESI-MS **[verify]**:
- **Decreased galactosylation and sialylation**, "resembling pro-inflammatory patterns observed in autoimmune diseases"
- Increases in the **afucosylated species A2G1** and the **agalactosylated structures FA2 and FA2B**; increases in bisected and afucosylated N-glycans
- ANOVA identified **seven N-glycans with significant intensity differences**
- Changes appeared **selective to IgG**
- Interpretation: alterations "might enhance the pro-inflammatory IgG structures while decreasing the anti-inflammatory ones"

**The mechanistic puzzle the authors themselves raise** **[verify]**: "No genes encoding galactosyltransferases or sialyltransferases are located on chromosome 14." So the glycosylation phenotype cannot be explained by simple hemizygosity — it is either a *trans* consequence of ring-driven transcriptional dysregulation or a secondary inflammatory-state readout. Curate this explicitly as a `KNOWLEDGE_GAP`.

**Therapeutic signal:** Patient 1 on IVIG showed "a reduction in seizures from 5–6/week to one/week," causality uncertain **[verify]**. Authors propose IVIG and/or monoclonal antibodies to modulate the inflammatory response.

GO: GO:0006487 protein N-linked glycosylation · GO:0006486 protein glycosylation · GO:0006954 inflammatory response · GO:0002455? humoral immune response mediated by circulating immunoglobulin.
CHEBI: N-glycan / oligosaccharide terms — verify before binding.

### 6.6 What is *not* known

- No proteomics, metabolomics, or lipidomics studies of r(14) exist beyond the IgG glycan work.
- No single-cell or spatial transcriptomics.
- No CRISPR/RNAi functional screen.
- Transcriptomics is limited to small position-effect studies (Ferreira 2015) and the ring 20 analogue (PMID:33207017).
- The MD-RING study (NCT06813469) is the first systematic multi-omic/long-read effort — see §12/§15.

---

## 7. Anatomical Structures Affected

### Organ level

**Primary:**
- **Brain / central nervous system** — UBERON:0000955. Cerebral cortex (UBERON:0000956), hippocampal formation (UBERON:0002421), corpus callosum (UBERON:0002336), cerebellum (UBERON:0002037), lateral ventricles (UBERON:0002285).
- **Eye / retina** — UBERON:0000970 eye; UBERON:0000966 retina; UBERON:0004864? macula lutea (verify); UBERON:0000941 optic nerve; UBERON:0001769 iris; UBERON:0000965 lens of camera-type eye.

**Secondary / systemic:**
- **Immune system** — UBERON:0002405; **respiratory system** — UBERON:0001004; **lung** — UBERON:0002048
- **Digestive system** — UBERON:0001007 (feeding difficulty, dysphagia, GERD, celiac disease)
- **Musculoskeletal**: vertebral column — UBERON:0001130 (scoliosis, kyphosis); skeleton — UBERON:0004288 (osteopenia/osteoporosis); musculature — UBERON:0001015 (hypotonia)
- **Craniofacial skeleton** — UBERON:0010363? / UBERON:0001474 bone element; **dentition** — UBERON:0003672? (verify)
- **Lymphatic system** — UBERON:0006558? / UBERON:0002465 lymphoid system (lymphedema of hands/feet)

**Body systems:** nervous, visual/sensory, immune, respiratory, digestive, musculoskeletal, lymphatic. **Notably spared:** cardiovascular and renal/urinary — congenital malformations of heart, kidney, and urinary tract are "very rarely reported."

### Tissue and cell level

| Tissue/cell | CL/UBERON | Basis |
|---|---|---|
| Cortical neurons (excitatory/inhibitory) | CL:0000540, CL:0000679, CL:0000617, CL:0000598 | epilepsy, E/I imbalance |
| Neural progenitor cells | CL:0011020 neural progenitor cell | microcephaly, FOXG1 biology |
| Astrocytes, microglia | CL:0000127, CL:0000129 | inferred; not directly demonstrated in r(14) |
| Retinal pigment epithelium | CL:0002586 | pigmentary retinopathy |
| Photoreceptors (rod/cone) | CL:0000604 / CL:0000573 | retinitis pigmentosa reports |
| B cells / plasma cells | CL:0000236 / CL:0000786 | IGH hemizygosity, IgA deficiency |
| Skeletal muscle | CL:0000188 | hypotonia (likely central, not myopathic — curate cautiously) |
| Dermal fibroblasts | CL:0000057 | the tissue in which ring instability and iPSC reprogramming are studied |

### Subcellular level

- **Nucleus** — GO:0005634; **chromosome / centromeric region** — GO:0000775; **heterochromatin** — GO:0000792; **nuclear periphery/lamina** — GO:0005652? nuclear lamina *(verify)* — relevant to repositioning
- **Micronucleus** — GO:0097604? *(verify; may require free text)* — the direct cytological readout of ring loss
- **Mitotic spindle** — GO:0072686
- **Golgi apparatus** — GO:0005794 (site of IgG N-glycan maturation)

### Localization / lateralization

Brain involvement is **bilateral and diffuse**; EEG shows generalized slow background with **multifocal** spikes and a posterior/occipital predominance of complex spike-and-wave. Retinal involvement is **bilateral**. Facial asymmetry ("long and sometimes asymmetrical face") is a described but minor asymmetric feature. Scoliosis is by definition an asymmetric axial deformity.

---

## 8. Temporal Development

### Onset

- **Lesion:** congenital — de novo, arising in gametogenesis or very early embryogenesis.
- **Growth restriction:** may begin prenatally (IUGR reported), but **microcephaly is characteristically postnatal-onset** — a useful discriminator.
- **Epilepsy:** "usually … in the first months of life"; infantile onset is the annotated HPO onset (HP:0003593). One series reported r(14) seizure onset at **3–24 months**, after developmental delay was already apparent (PMID:41087847) **[verify]**.
- **Developmental delay:** recognized in infancy, frequently **before** seizure onset.
- **Onset pattern:** chronic/insidious for the developmental phenotype; the epilepsy onset can be abrupt.

### Progression

The disease is **non-progressive at the level of the underlying lesion** (GARD explicitly: "Condition is non-progressive"), but the *clinical course* has three distinguishable phases:

| Phase | Age | Character |
|---|---|---|
| **Early / encephalopathic** | 0–5 y | Highest seizure burden; status epilepticus; risk of **developmental regression** — "intense epileptic activity, more frequent in the early years of life, may be associated with regression of the stages of psychomotor development or previously acquired language" **[verify]**. This is the critical window. |
| **Plateau** | childhood–adolescence | Slow developmental gains; seizures persist but frequency often declines |
| **Late / adult** | late adolescence onward | Seizures "eventually decrease in frequency during late adolescence" **[verify]**; morbidity shifts to **infection, malnutrition, scoliosis, osteopenia** |

**Progression rate:** variable, driven by seizure burden. **Course pattern:** episodic seizures (with clusters) on a stable, non-degenerative developmental baseline. **Duration:** chronic, lifelong.

### Patterns

- **Remission:** no spontaneous remission of the disorder. Seizure amelioration with age is real but partial. **A critical caveat from the guideline** **[verify]**: "Interrupting effective antiepileptic therapies when the symptomatology appears less severe could lead to the return of seizures that may even result no longer responsive to previously effective treatments." — i.e. apparent improvement is *not* a license to withdraw ASMs.
- **Critical periods / intervention windows:**
  1. **First 5 years** — aggressive seizure control to protect the developmental trajectory (the encephalopathic-effect claim)
  2. **Infancy onward** — early physical therapy "to reduce hypotonic complications (such as scoliosis) due to the reduced muscle tone" **[verify]**
  3. **Throughout** — nutritional support before malnutrition is established
  4. **Adulthood** — infection prophylaxis/surveillance, the dominant mortality risk

---

## 9. Inheritance and Population

### Epidemiology

| Measure | Value | Source |
|---|---|---|
| Point prevalence | **<1 / 1,000,000** worldwide | Orphanet ORPHA:1440 (ORDO annotation) |
| Cumulative reported cases | **~80–100** since first report in **1971** | Guideline PMC5387247: "Over 80 cases have been described since the first report in 1971"; MedlinePlus: "More than 80 affected individuals have been reported in the scientific literature" |
| Incidence | **Not established** | — |
| Registry cohort | **~54 patients** in the Ring14 International clinical database | ring14.org |

For dismech `prevalence:`:

```yaml
prevalence:
- population: Worldwide
  measure_type: POINT_PREVALENCE
  prevalence_class: BELOW_1_IN_1000000
  rate_per_100000: 0.1        # upper bound; <1 per 1,000,000 = <0.1 per 100,000
  notes: >-
    Orphanet worldwide point-prevalence class <1/1,000,000. Approximately 80-100
    cases reported in the literature since 1971; exact prevalence unknown and
    almost certainly underascertained because array-only testing misses the ring.
```

**Ascertainment caveat worth curating:** because chromosomal microarray has largely displaced karyotyping as a first-tier test, a deleted ring 14 is now readily misreported as a *linear* 14q terminal deletion, and a **complete** ring 14 (no copy-number change, ~22% of cases) is invisible to array entirely. Reported prevalence is therefore a floor.

### Inheritance

- **Pattern:** **Sporadic / de novo**, not inherited (HP:0003745 Sporadic). ORDO annotates inheritance as "Not applicable; Unknown."
- MedlinePlus: "Ring chromosome 14 syndrome is typically not inherited. A ring chromosome usually occurs as a random event during the formation of reproductive cells or during early embryonic development." Rare familial transmission has been documented but is exceptional.
- **Penetrance:** complete for the ring carrier state (all reported ring 14 individuals are affected).
- **Expressivity:** **variable** — driven by deletion size, ring instability, and cryptic duplications.
- **Anticipation:** not applicable (no repeat expansion; transmission is essentially never observed).
- **Germline mosaicism:** not reported; empiric recurrence risk to parents is very low but a de novo event cannot be formally excluded from a gonadal-mosaicism origin.
- **Somatic mosaicism:** **universal** — for ring loss/duplication (see §6.3). Distinguish carefully from *constitutional* mosaicism for the ring itself, which is occasionally reported.
- **Founder effects:** none. **Consanguinity:** no role. **Carrier frequency:** not applicable.

### Population demographics

- **Ethnic/geographic:** no predilection reported; cases described worldwide (Italy, USA, Mexico, Russia, China, Turkey, Bulgaria, Estonia in the recent literature).
- **Sex ratio:** **not established.** A general ring-chromosome cohort (Murry et al., *Genes* 2025, PMID:40725393; 40 constitutional rings over 37 years) noted "a preponderance of pediatric-aged females at first ascertainment" **[verify]** — but this is an ascertainment observation across all rings, **not** an r(14)-specific sex ratio, and should not be curated as one. A 2025 Chinese series of 9 ring-chromosome children was 6F:3M overall (PMID:41087847), again too small and not r(14)-specific.
- **Age distribution:** diagnosis typically in infancy/early childhood following seizure onset and developmental delay; GARD notes symptom recognition often ages 2–11 y. Adults are described but the adult natural history is poorly characterized.

---

## 10. Diagnostics

### The diagnostic algorithm (2017 task-force consensus)

The guideline's central diagnostic recommendation has two halves, and **the second is the one most often missed** **[verify]**:

1. **Array-CGH as the first diagnostic step** for a child with "neuro-psychological alterations and drug-resistant epilepsy."
2. **"All subject for whom a 14q terminal deletion is identified should be addressed to a standard karyotype to assess the presence of the ring."**

Plus a sensitivity requirement: **"The analysis of at least 30 metaphases is necessary for a >95% chance of detecting a r(14) chromosome that occurs in at least 80% of cells."**

### Genetic testing

| Modality | Utility for r(14) |
|---|---|
| **Karyotype (≥30 metaphases)** | **Essential and diagnostic.** The only routine test that visualizes ring topology. Also quantifies mosaic ring loss/duplication. |
| **Chromosomal microarray (CMA / aCGH / SNP array)** | Defines terminal deletion size and gene content; **cannot detect a complete ring**; will mislabel a deleted ring as linear. SNP arrays additionally exclude UPD(14). |
| **FISH (subtelomeric 14q, centromere 14)** | Confirms ring, quantifies mosaic monosomy/duplicated rings, identifies r(14) within micronuclei (Meza-Espinoza 2024 method). |
| **Long-read sequencing (LRS)** | Investigational — the intervention under study in NCT06813469 for breakpoint resolution and TAD analysis. |
| **WES** | Low yield for the ring itself; useful to exclude phenocopies. |
| **WGS** | Can call the terminal CNV and, with structural-variant calling, the fusion junction. Not yet standard. |
| **Gene panels / single-gene testing** | Not diagnostic. Epilepsy panels covering *FOXG1*, *PACS2*, *CHD8*, *IRF2BPL*, *CDKL5*, *STXBP1*, *SCN1A* will be **negative** and can delay diagnosis — a real clinical trap. |
| **mtDNA testing / repeat expansion testing** | Not applicable. |
| **Parental karyotypes** | Recommended for counseling (rare familial ring). |

### Baseline clinical evaluation (guideline) **[verify]**

"cerebral MR, EEG, heart and abdomen US, oculistic and audiologic evaluation, neuropsychological assessment."

### Clinical / laboratory / imaging tests

- **EEG** (essential; also a severity marker correlating negatively with cognition) — LOINC/NCIT term needed
- **Brain MRI** — usually normal or with nonspecific mild atrophy/callosal/ventricular/hippocampal/cerebellar changes
- **Ophthalmologic exam incl. dilated fundoscopy and multimodal imaging** (OCT, fundus autofluorescence, near-infrared reflectance — Vasconcelos 2019 showed macular yellow dots only on multimodal imaging)
- **Immunological workup**: quantitative immunoglobulins (IgG, IgA, IgM), IgG subclasses, specific antibody responses — annually per guideline
- **Nutritional/growth**: anthropometrics, vitamin D, swallow study when aspiration suspected
- **Skeletal**: spine radiographs for scoliosis; DXA for osteopenia
- **Cytogenetic instability assays** (research/specialist): micronucleus assay + FISH (Meza-Espinoza 2024)
- **Emerging biomarker (research only):** **IgG N-glycan profile** by UHPLC-FLR/ESI-MS — decreased galactosylation and sialylation (Messina 2026). Not validated; no PPV/NPV data.

**No validated biochemical biomarker, no newborn-screening analyte, no FDA-listed biomarker exists.**

### Diagnostic criteria and differential

There are **no formal consensus diagnostic criteria** (no DSM/ICD-style rule set). Diagnosis is cytogenetic.

**Differential diagnosis:**

| Condition | Distinguishing feature |
|---|---|
| **Linear 14q32.33 terminal deletion syndrome** | Same CNV, **no ring** → epilepsy reported in only ~2/11 published cases and **no retinal abnormalities reported** (Vaisfeld 2021) **[verify]**. The single most important distinction. |
| *FOXG1* syndrome (congenital Rett variant) | Point mutation/14q12 deletion; postnatal microcephaly + dyskinesia; no ring |
| *PACS2*-DEE (DEE-66) | Neonatal seizures, cerebellar dysgenesis; recurrent p.Glu209Lys |
| **Ring chromosome 20 syndrome** | Also epilepsy-dominant ring; characteristic prolonged nonconvulsive status with distinctive EEG; normal development early |
| Dravet syndrome (*SCN1A*) | Fever-sensitive hemiclonic seizures; normal early development |
| Angelman syndrome | Happy demeanour, ataxia, characteristic EEG; 15q11-13 |
| Lennox–Gastaut syndrome | Slow spike-wave, tonic seizures in sleep — a *pattern*, not an etiology; r(14) can present LGS-like |
| Temple syndrome / Kagami–Ogata (UPD14) | Imprinting; **excluded** in r(14) series |
| Other DEEs (*CDKL5*, *STXBP1*, *SCN2A*) | Gene-specific |

### Screening

- **Newborn screening:** not applicable — no biochemical marker.
- **Carrier screening:** not applicable — de novo.
- **Cascade screening:** not indicated (parental karyotype is for counseling reassurance, not cascade testing).
- **Prenatal:** karyotype ± CMA on CVS/amniocentesis will detect a ring 14; NIPT/cfDNA will **not** reliably detect it (small terminal CNV; no ring topology information). Prenatal detection is generally incidental or follows an abnormal ultrasound (IUGR).

---

## 11. Outcome / Prognosis

### Survival and mortality

The honest curation answer is **"not established."** Guideline **[verify]**:

> "A precise prognosis in terms of expected lifespan in individuals with r(14) syndrome has yet to be established."
> "Prognosis should be estimated individually and depends primarily on comorbidities and medical complications."
> "The epileptic burden, infectious complications and nutritional deficiencies should be considered as major determinants."

- **No 5-year or 10-year survival figures, no life-expectancy estimate, no mortality rate** exists in the literature. Do not manufacture one.
- **Leading cause of adult death: infection.** "Infections are one of the worse prognostic factors and the main cause of death in adulthood" **[verify]**.
- Survival into adulthood is clearly attainable — the Meza-Espinoza 2024 index case was 21 years old.
- SUDEP risk is not quantified for r(14) but is a reasonable concern given lifelong drug-resistant epilepsy; **do not curate a numeric estimate**.

### Morbidity and function

- **Intellectual disability, moderate to severe, in essentially all patients** — the dominant long-term functional determinant alongside epilepsy.
- Many patients are **nonverbal**; the guideline's management emphasis on preserving communication reflects this.
- Ambulation: achieved late (2–3 years) in most; **some never walk**.
- Lifelong dependence for activities of daily living is the norm.
- **No EQ-5D, SF-36, PROMIS, or disease-specific validated QoL instrument** has been applied. The SanInocencio 2026 conceptual disease model (PMID:41533279) is the **first** systematic characterization of lived experience and is explicitly the foundation for a future COA/PRO instrument — cite it as the QoL source of record and note the absence of quantitative instruments as a gap.

### Complications

Recurrent/severe respiratory infection · aspiration pneumonia (including iatrogenic lipoid pneumonia from oil-based CBD, PMID:40348517) · status epilepticus (~50%) · developmental regression during periods of intense epileptic activity · malnutrition requiring enteral feeding · scoliosis · juvenile osteoporosis/osteopenia with fracture risk · visual impairment in a minority · sleep disorder · celiac disease.

### Recovery potential

None in the sense of cure. Meaningful, treatment-attributable improvement is possible in **seizure frequency** (with ASMs, ketogenic diet, VNS, CBD), **nutritional status** (enteral feeding), and **motor complications** (early physiotherapy). The developmental disability itself is not reversible with current therapy.

### Prognostic factors

1. **Seizure burden and EEG severity in the first years** — negatively correlated with cognitive development (Giovannini 2013)
2. **Infection frequency/severity** — the adult mortality driver
3. **Nutritional status** — named guideline determinant
4. **Deletion size** — larger terminal deletions include *PACS2* and more of *IGH*; the ≥650 kb threshold marks the recognizable facial gestalt
5. **Degree of ring instability** — biologically plausible, clinically unvalidated

**No prognostic biomarker is validated.** The IgG glycan profile is the only candidate on the horizon.

---

## 12. Treatment

There is **no disease-modifying or curative therapy**. Management is symptomatic, multidisciplinary, and guideline-directed.

### 12.1 Antiseizure pharmacotherapy

Guideline **[verify]**: "Antiepileptic drugs are frequently used: barbiturates (in the first months of life), valproic acid, carbamazepine, topiramate, vigabatrin, clobazam and levetiracetam." And: "About half of patients with r(14) syndrome show drug resistance, while in the remaining half seizure control is variable."

| Drug | Class / MoA | dismech annotation |
|---|---|---|
| Phenobarbital | Barbiturate; GABA-A positive allosteric modulator. First months of life. High-dose oral phenobarbital was effective in 7/11 (63.6%) children with refractory seizures in a series that included r(14) (PMID:40129048) **[verify]** | `treatment_term: NCIT:C15986` Pharmacotherapy; `therapeutic_agent: CHEBI` phenobarbital *(verify CURIE)*; `therapeutic_modality: SMALL_MOLECULE` |
| Valproic acid | Broad-spectrum; HDAC inhibition, GABAergic, Na⁺ channel | CHEBI:39867 *(verify)* |
| Carbamazepine | Na⁺ channel blocker; appropriate given predominantly **focal** semiology | CHEBI:3387 *(verify)* |
| Topiramate | Multi-mechanism | *(verify CURIE)* |
| Vigabatrin | Irreversible GABA-transaminase inhibitor. **Retinal toxicity risk — noteworthy in a syndrome with baseline retinal pathology; visual-field/ERG monitoring is doubly important here.** | *(verify CURIE)* |
| Clobazam | Benzodiazepine | *(verify CURIE)* |
| Levetiracetam | SV2A ligand | *(verify CURIE)* |

**Explicit management warning to curate** **[verify]**: do not withdraw an effective ASM during a quiescent phase — "Interrupting effective antiepileptic therapies when the symptomatology appears less severe could lead to the return of seizures that may even result no longer responsive to previously effective treatments."

### 12.2 Cannabidiol

Guideline preliminary data **[verify]**: seizure frequency reduced with an "adequate safety profile," dosing "2–5 mg/Kg per day, up-titrated until intolerance or to a maximum of 20–25 mg/kg per day" — i.e. the Epidiolex regimen. Note that CBD has RCT-grade evidence and FDA/EMA approval in **Dravet and Lennox–Gastaut**, not in r(14); its use here is extrapolation plus small-series experience.

**Safety signal:** oil-based CBD aspiration caused **lipoid pneumonia** in a 4-year-old with ring chromosome 14 (PMID:40348517) — relevant given the high baseline aspiration risk in this population.

`therapeutic_modality: SMALL_MOLECULE`; `therapeutic_agent`: cannabidiol *(verify CHEBI CURIE)*.

### 12.3 Non-pharmacological seizure therapy

- **Ketogenic diet** — "may be taken in consideration for the therapeutic strategy" **[verify]**. `treatment_term: NCIT:C15447` Dietary Intervention; `therapeutic_modality: BEHAVIORAL`.
- **Vagus nerve stimulation** — same recommendation strength. `therapeutic_modality: DEVICE`; NCIT term for vagus nerve stimulation *(verify)*.
- **Epilepsy surgery** — not applicable; the epilepsy is multifocal/diffuse with no resectable focus.

### 12.4 Immunological / experimental

- **IVIG** — one RC14 patient on IVIG showed seizure reduction from 5–6/week to ~1/week (Messina 2026) **[verify]**; causality explicitly uncertain, n=1. The authors propose IVIG and/or monoclonal antibodies to modulate inflammation. **Curate as `EMERGING` hypothesis with `supports: PARTIAL`, not as an established treatment.**
- **Antibiotic prophylaxis / immunization** — implied by the annual immunology follow-up recommendation; specific regimens are not specified in the guideline.

### 12.5 Supportive, nutritional, rehabilitative

| Intervention | Guideline detail **[verify]** | NCIT |
|---|---|---|
| Enteral tube feeding | "recommended when anorexia is limiting caloric intake and/or when aspiration occurs during swallowing" | NCIT:C15433 Nutritional Support (+ gastrostomy procedure term) |
| Vitamin D supplementation | "must be given at twice the of recommended daily allowance (approximately 800-1.000 IU/day)" | NCIT:C15433; `therapeutic_agent`: cholecalciferol *(CHEBI, verify)*; `therapeutic_modality: SMALL_MOLECULE` |
| Physical therapy | "Start physical therapy early to reduce hypotonic complications (such as scoliosis) due to the reduced muscle tone" | NCIT:C15302 Physical Therapy; `BEHAVIORAL` |
| Speech / AAC | "Many patients … are nonverbal and thus maintaining their ability to communicate is always essential" | NCIT:C159273 Speech Therapy; `BEHAVIORAL` |
| Occupational therapy | implied by multidisciplinary model | NCIT:C121351 |
| Scoliosis management (bracing/surgery) | complication-driven | NCIT:C16186 Orthopedic Surgical Procedure; `SURGERY` |
| Genetic counseling | de novo, low recurrence risk | NCIT:C15240 |
| Multidisciplinary specialist care | "Multidisciplinary care at a major clinical facility should be available for patients and their relatives to reduce medical complications and improve quality of life" | NCIT:C15747 Supportive Care |

**Follow-up cadence (guideline)** **[verify]**: "Immunologist, once per year; child Neurologist/Neurologist, as needed; Ophthalmologist, as needed; Gastroenterologist/Nutritionist, as needed."

### 12.6 Advanced therapeutics — none available

- **Gene therapy / gene editing:** not applicable in current form — the lesion spans megabases and, per the position-effect model, involves chromosome architecture rather than a single gene.
- **RNA-based therapy (ASO/siRNA):** no target established.
- **Cell therapy:** none clinically. But see the "chromosome therapy" concept in §15 — reprogramming-mediated ring correction is the only conceptual disease-modifying route ever proposed for ring disorders, and it is preclinical.
- **Pharmacogenomics:** no r(14)-specific PGx. Standard CPIC guidance applies (notably *HLA-B\*15:02*/*HLA-A\*31:01* for carbamazepine, *CYP2C9* for phenytoin/valproate considerations, *POLG* contraindication screening before valproate in unexplained epileptic encephalopathy). These are population-standard, not disease-specific.

### 12.7 Clinical trials

| NCT | Title | Status | Type |
|---|---|---|---|
| **NCT06813469** | Multi-Dimensional Genomic Dissection of Ring Chromosome 14 Syndrome (MD-RING) | Active, not recruiting | Interventional (registry-classified); intervention = **LRS analysis** (long-read sequencing) |

Brief summary **[verify]**: "The MD-RING study investigates how position effects and TAD alterations may cause ring chromosome 14 syndrome. Researchers aim to clarify genetic-to-clinical relationships, establish resources for ring syndrome research, and ultimately enhance family counseling, patient management, and identify potential therapeutic approaches."

**No interventional therapeutic trial specific to ring chromosome 14 has ever been conducted.**

---

## 13. Prevention

**Primary prevention: not possible.** A de novo structural chromosomal event with no known modifiable risk factor. There is nothing to modify — no vaccination, no exposure reduction, no behavioral intervention that alters occurrence.

**Secondary prevention (early detection):**
- No population screening program exists or is justifiable at this prevalence.
- The actionable secondary-prevention message is **diagnostic**: karyotype every child in whom a 14q terminal deletion is found on array, and karyotype (≥30 metaphases) children with early-onset drug-resistant epilepsy + developmental delay + microcephaly + retinal changes whose gene panel is negative. Earlier diagnosis enables earlier immunological, ophthalmologic, and nutritional surveillance.
- **Prenatal/reproductive:** karyotype ± CMA on CVS/amniocentesis detects a ring 14. PGT is theoretically available but essentially never indicated given the de novo origin and negligible recurrence risk. Prenatal testing in a subsequent pregnancy may be offered for reassurance.

**Tertiary prevention (preventing complications) — this is where nearly all the actionable prevention lives:**

| Target complication | Preventive action |
|---|---|
| Developmental regression | Aggressive early seizure control; do not withdraw effective ASMs prematurely |
| Recurrent/severe infection → adult mortality | Annual immunology review; routine + risk-based immunization; prompt treatment of respiratory infection |
| Malnutrition | Early nutritional assessment; enteral feeding before failure to thrive is entrenched |
| Aspiration pneumonia | Swallow assessment; caution with **oil-based** CBD preparations (PMID:40348517) |
| Scoliosis | Early physiotherapy from infancy |
| Osteopenia/fracture | Vitamin D at 2× RDA (800–1,000 IU/day); weight-bearing where possible; note valproate/ASM bone effects |
| Vision loss | Regular ophthalmologic exam; special vigilance with vigabatrin |
| Dental disease | Ivanoff 2023 (PMID:36855970) — dedicated dental management guidance |

**Genetic counseling:** the core message is (1) sporadic, de novo origin; (2) **recurrence risk to the parents is very low** (empiric, with the caveat that germline mosaicism cannot be formally excluded); (3) parental karyotypes are appropriate to exclude the rare familial ring; (4) recurrence risk for the affected individual's own offspring is not a practical question given the severity of the phenotype. NCIT:C15240 Genetic Counseling.

**Public health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

### Direct orthologue disease

**None.** There is no naturally occurring "ring chromosome 14 syndrome" in any non-human species, and there cannot be a direct orthologue: human chromosome 14 is a synteny construct that maps onto multiple chromosomes in mouse (principally Mmu 12 and Mmu 14) and other mammals. The *disease concept* is human-chromosome-specific.

- **NCBI Taxonomy:** NCBITaxon:9606 *Homo sapiens* — the only species in which this disease entity is defined.
- **VBO breed terms:** not applicable.

### Comparative biology that *is* relevant

- **Ring chromosomes as a class occur in other species.** Constitutional and radiation-induced ring chromosomes are documented in mouse, dog, cattle, and horse cytogenetics, and ring-chromosome instability (anaphase bridging, sister-chromatid-exchange–driven ring loss) is a **conserved mitotic phenomenon**, not a human peculiarity. This makes the *instability* arm of the mechanism (§6.3) comparatively tractable even though the disease is not.
- **OMIA:** no ring chromosome 14 entry. Searching OMIA for ring-chromosome entries is worthwhile for the general instability biology but will not yield a disease analogue.
- **Gene orthologues** (for arm-specific modeling rather than for the syndrome): *Foxg1* (mouse, NCBI Gene 15228), *Pacs2* (mouse), *Chd8* (mouse) — all have well-characterized mouse models with neurodevelopmental phenotypes.
- **Evolutionary conservation:** telomere position effect and heterochromatin spreading are deeply conserved (classic *Drosophila* position-effect variegation, *S. cerevisiae* subtelomeric silencing), which is the strongest cross-species support for the position-effect hypothesis — though as an analogy, not as evidence about r(14) itself.

### Transmission

Not applicable. Non-infectious, non-zoonotic, no cross-species susceptibility.

---

## 15. Model Organisms

### The core problem

**There is no animal model of ring chromosome 14 syndrome, and building one is not straightforward.** A mouse cannot carry a ring human chromosome 14; engineering a ring from the syntenic mouse regions would not reproduce either the gene content or the p-arm heterochromatin juxtaposition that the position-effect model depends on. Vaisfeld et al. close by calling for work "especially addressing the expression and functional consequences of candidate pathogenic genes and the role of epigenetic mechanisms in **simplified model systems**" **[verify]** — an explicit acknowledgment that no faithful whole-organism model exists.

For dismech, this belongs in a **`HUMAN_MODEL_MISMATCH` discussion**, not a generic `KNOWLEDGE_GAP`: model-system evidence exists for the component genes, but its translational validity to the ring-specific mechanism is precisely the open question.

### 15.1 Patient-derived cellular models (the workhorse)

| System | Use | Notes |
|---|---|---|
| **Patient dermal fibroblasts** (CL:0000057) | Cytogenetic instability assays: metaphase FISH for mosaic monosomy/duplicated ring; micronucleus assay; SCE | The substrate for Meza-Espinoza 2024's instability quantification. Directly `MEASURES` the ring-instability node. |
| **Peripheral blood lymphocytes** | Standard karyotype (≥30 metaphases); mosaicism quantification | Guideline-mandated diagnostic tissue |
| **Patient-derived iPSCs** (CL:0002248 *verify*) | Position-effect / transcriptome studies; differentiation to neurons | **Major caveat below** |
| **iPSC-derived cortical neurons / cerebral organoids** | The only plausible route to modeling the epileptogenic mechanism in human cells | Not yet published for r(14) |
| **Lymphoblastoid cell lines** | Expression profiling (the Ferreira 2015 position-effect approach) | Blood-derived; brain relevance limited |

### 15.2 The iPSC caveat that must be curated

**Bershteyn M, Hayashi Y, Desachy G, et al. "Cell-autonomous correction of ring chromosomes in human induced pluripotent stem cells." *Nature* 2014;507(7490):99–103. PMID:24413397, DOI:10.1038/nature12923** — studied **ring 13 and ring 17**, not ring 14. Abstract **[abstract-verbatim]**:

> "Ring chromosomes are structural aberrations commonly associated with birth defects, mental disabilities and growth retardation. Rings form after fusion of the long and short arms of a chromosome, and are sometimes associated with large terminal deletions. Owing to the severity of these large aberrations that can affect multiple contiguous genes, no possible therapeutic strategies for ring chromosome disorders have been proposed. During cell division, ring chromosomes can exhibit unstable behaviour leading to continuous production of aneuploid progeny with low viability and high cellular death rate. The overall consequences of this chromosomal instability have been largely unexplored in experimental model systems. Here we generated human induced pluripotent stem cells (iPSCs) from patient fibroblasts containing ring chromosomes with large deletions and found that reprogrammed cells lost the abnormal chromosome and duplicated the wild-type homologue through the compensatory uniparental disomy (UPD) mechanism. The karyotypically normal iPSCs with isodisomy for the corrected chromosome outgrew co-existing aneuploid populations, enabling rapid and efficient isolation of patient-derived iPSCs devoid of the original chromosomal aberration. Our results suggest a fundamentally different function for cellular reprogramming as a means of 'chromosome therapy' to reverse combined loss-of-function across many genes in cells with large-scale aberrations involving ring structures. In addition, our work provides an experimentally tractable human cellular system for studying mechanisms of chromosomal number control, which is of critical relevance to human development and disease."

**The two-edged implication for r(14) modeling:**

1. **As therapy concept** — "chromosome therapy": reprogramming purges the ring. Related work: Kim et al. (PMID:25482192), and PMID:27882407 on ring correction via iPSC reprogramming. Entirely preclinical; no route to correcting a whole organism.
2. **As a modeling hazard — this is the point that matters for curation.** iPSC lines derived from ring-chromosome patients **spontaneously lose the ring and become karyotypically normal via compensatory UPD**, and the corrected cells then outcompete the ring-bearing ones. Any r(14) iPSC model therefore requires continuous karyotypic surveillance, and an apparently "isogenic control" may in fact be the intended disease line that self-corrected. See also "Complex biology of constitutional ring chromosomes structure and (in)stability revealed by somatic cell reprogramming," *Sci Rep* 2021, doi:10.1038/s41598-021-83399-3.

In dismech `experimental_models` terms, a patient iPSC line for r(14) is at best `PARTIALLY_RECAPITULATES` with `fidelity: LOW-to-MODERATE` and a mandatory `limitations` field naming the compensatory-UPD self-correction.

### 15.3 Component-gene animal models (surrogate, not disease models)

These model *candidate effector genes*, not the syndrome. Each should be curated with an explicit limitation that the ring context is absent.

| Model | Species | Relevance | Databases |
|---|---|---|---|
| *Foxg1*<sup>+/−</sup> and conditional *Foxg1* mice | Mouse (NCBITaxon:10090) | Forebrain development, microcephaly; the leading position-effect target | MGI, IMPC |
| *Pacs2* mouse models | Mouse | DEE-66 candidate; the only deleted-region epilepsy gene | MGI |
| *Chd8*<sup>+/−</sup> mice | Mouse | ASD/seizure biology; **not deleted in r(14)** — surrogate only | MGI, IMPC |
| *foxg1a/b* zebrafish | Zebrafish (NCBITaxon:7955) | Rapid seizure phenotyping (PTZ assays), forebrain patterning | ZFIN |
| *Drosophila* position-effect variegation systems | *D. melanogaster* (NCBITaxon:7227) | The canonical experimental system for heterochromatin spreading — the mechanism, not the disease | FlyBase |
| *S. cerevisiae* subtelomeric silencing / TPE | Yeast (NCBITaxon:4932) | Same: mechanism-level | SGD |

**Phenotype recapitulation:** none of these reproduces the r(14) syndrome. *Foxg1* models capture microcephaly and seizure susceptibility but not the retinal phenotype, the immune phenotype, or the ring itself. **Limitations to record:** no model reproduces (a) ring topology and its instability, (b) the p-arm heterochromatin juxtaposition, (c) combined proximal position effect + distal haploinsufficiency, (d) the human *IGH* locus architecture.

### 15.4 Resources

MGI · IMPC · KOMP · IMSR · EMMA · MMRRC (mouse); ZFIN (zebrafish); FlyBase; SGD; Alliance of Genome Resources; Cellosaurus / Coriell / NIGMS Human Genetic Cell Repository (patient fibroblast and lymphoblastoid lines); **Ring14 International biobank and clinical database** ([ring14.org](http://www.ring14.org/eng/120/clinical-database/)) — the practical route to patient-derived material.

---

## Appendix A — Core reference set for the dismech entry

| PMID / ID | Citation | Use |
|---|---|---|
| **22564756** | Zollino M, Ponzi E, Gobbi G, Neri G. The ring 14 syndrome. *Eur J Med Genet* 2012;55:374–380 | Genotype–phenotype model; deletion sizes; parental origin; position-effect hypothesis. **Full abstract verified.** |
| **19441122** | Zollino M, et al. The ring 14 syndrome: clinical and molecular definition. *Am J Med Genet A* 2009 | Core clinical gestalt; regional assignment |
| **24116895** | Giovannini S, et al. Epilepsy in ring 14 syndrome: a clinical and EEG study of 22 patients. *Epilepsia* 2013;54(12) | Epilepsy phenotype and EEG; ~100% penetrance |
| **28399883** (PMC5387247) | Guideline recommendations for diagnosis and clinical management of Ring14 syndrome — first report of an ad hoc task force. *Orphanet J Rare Dis* 2017;12:69 | Management, diagnostics, prognosis, follow-up schedule. **Verify PMID before use.** |
| **33205446** | Vaisfeld A, Spartano S, Gobbi G, Vezzani A, Neri G. Chromosome 14 deletions, rings, and epilepsy genes: a riddle wrapped in a mystery inside an enigma. *Epilepsia* 2021;62(1):25–40 | Ring vs linear dissociation; 40 chr14 epilepsy genes; mechanism hypotheses |
| **39020403** | Meza-Espinoza JP, et al. Chromosomal instability in a patient with ring chromosome 14 syndrome. *Mol Cytogenet* 2024;17:15 | Quantified ring instability (12.3% monosomy, 6.2% triple signal, 9% micronuclei); 1.7 Mb/23-gene deletion |
| **42352229** | Messina A, et al. IgG glycosylation analysis in patients with Ring14 syndrome. *Biomolecules* 2026;16(6):760 | Novel immune pathomechanism; IVIG signal |
| **41533279** | SanInocencio C, et al. Patient-centered conceptual disease model in Ring 14 syndrome. *Qual Life Res* 2026 | QoL and caregiver burden — the QoL source of record |
| **31755799** | Vasconcelos HM Jr, et al. Multimodal imaging of ring 14 syndrome associated maculopathy. *Ophthalmic Genet* 2019 | Retinal/macular phenotype |
| **24413397** | Bershteyn M, et al. Cell-autonomous correction of ring chromosomes in human iPSCs. *Nature* 2014;507:99–103 | Model-system caveat + "chromosome therapy." **Full abstract verified.** |
| **38795333** | Barbour K, et al. Population-based study of rare epilepsy incidence in a US urban population. *Epilepsia* 2024 | EHR ascertainment limits |
| **40348517** | Hanzal N, et al. Lipoid pneumonia following chronic aspiration of cannabis oil. *Chest* 2025 | CBD-oil safety signal in an r(14) patient |
| **36855970** | Ivanoff AE, et al. *Folia Med* 2023 | Dental management |
| **38824650** | Gardner JA, et al. Ring chromosome 14 with a terminal 14q32.33 deletion. *J Assoc Genet Technol* 2024 | Cytogenetic case |
| **22151179** | Guilherme RS, et al. Mechanisms of ring chromosome formation, ring instability and clinical consequences. *BMC Med Genet* 2011;12:171 | Ring formation mechanisms (general) |
| **NCT06813469** | MD-RING: Multi-Dimensional Genomic Dissection of Ring Chromosome 14 Syndrome | Active study; position effects + TADs; long-read sequencing |
| **ORPHA:1440** | Orphanet | Prevalence class, ICD-10 Q93.2, ICD-11 LD7Y, definition |

---

## Appendix B — Suggested `mechanistic_hypotheses` groups

| `hypothesis_group_id` | Label | Status | Core claim |
|---|---|---|---|
| `position_effect_proximal_14q` | Heterochromatin spreading dysregulates proximal 14q11.2–q12 | `CANONICAL` (best-supported explanation of the ring-vs-linear dissociation) | Ring topology silences *FOXG1*-region genes present in 2 copies → epilepsy + retinal phenotype |
| `dynamic_mosaicism_growth_failure` | Ring instability → mosaic monosomy 14 → growth failure | `ALTERNATIVE` | Kosztolányi "ring syndrome"; measured instability (Meza-Espinoza 2024) |
| `brain_mosaic_monosomy_epileptogenesis` | Locally elevated monosomy-14 fraction in cortex creates an epileptogenic focus | `EMERGING` | Vaisfeld 2021 speculation; **untested — no human brain tissue data** |
| `pacs2_haploinsufficiency_synergy` | *PACS2* haploinsufficiency is minimally penetrant alone but enhanced by the ring | `EMERGING` | Vaisfeld 2021; requires deletion >~1.65 Mb |
| `igh_haploinsufficiency_infection` | 14q32.33 *IGH* hemizygosity → impaired humoral immunity → recurrent infection → adult mortality | `CANONICAL` | Zollino 2012 regional assignment; guideline |
| `igg_glycosylation_inflammation` | Pro-inflammatory IgG N-glycan shift contributes to infection susceptibility and possibly seizures | `EMERGING` | Messina 2026, n=6; no chr14 glycosyltransferase gene → mechanism unexplained |
| `dlk1_dio3_mirna_dysregulation` | 14q32 imprinted miRNA mega-cluster dysregulation contributes | `EMERGING` / gap | Vaisfeld 2021: "essentially no literature" |

## Appendix C — Suggested `discussions` (knowledge gaps)

1. `KNOWLEDGE_GAP` — *Why do ring 14 and size-matched linear 14q deletions diverge so sharply for epilepsy and retinal phenotype?* `attaches_to: pathophysiology#Ring chromosome 14 formation`
2. `KNOWLEDGE_GAP` — *No brain-tissue data exist to test whether mosaic monosomy 14 is enriched in cortex.* `attaches_to: pathophysiology#Mosaic monosomy 14`
3. `KNOWLEDGE_GAP` — *The 14q32 DLK1-DIO3 miRNA cluster is entirely unstudied in r(14).*
4. `KNOWLEDGE_GAP` — *No gene on chromosome 14 encodes a galactosyl- or sialyltransferase; the IgG glycan phenotype is mechanistically unexplained.* `attaches_to: pathophysiology#Aberrant IgG N-glycosylation`
5. `HUMAN_MODEL_MISMATCH` — *Patient-derived iPSCs spontaneously purge the ring via compensatory UPD, so the standard human cellular model self-corrects away the lesion it is meant to model.* `attaches_to: experimental_models#…`
6. `KNOWLEDGE_GAP` — *No life-expectancy, mortality-rate, or validated QoL-instrument data exist.* `attaches_to: clinical_burden#`

---

**Next step:** the highest-value thing to do before touching `kb/disorders/Ring_Chromosome_14.yaml` is to cache the reference set — `just fetch-reference PMID:22564756 PMID:24116895 PMID:33205446 PMID:39020403 PMID:42352229 PMID:41533279` (plus `ORPHA:1440`, which is already ingestible via the structured Orphanet source) — and confirm the 2017 guideline's PMID, since every management and frequency claim in §3, §10, §11, and §12 traces to it and I have not verified its PMID against PubMed. Want me to run that fetch and report which snippets survive verification?

### Sources

- [Guideline recommendations for diagnosis and clinical management of Ring14 syndrome — Orphanet J Rare Dis 2017 (PMC5387247)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5387247/)
- [Zollino et al., The ring 14 syndrome, Eur J Med Genet 2012 — PMID 22564756](https://pubmed.ncbi.nlm.nih.gov/22564756/)
- [Zollino et al., The ring 14 syndrome: clinical and molecular definition, 2009 — PMID 19441122](https://pubmed.ncbi.nlm.nih.gov/19441122/)
- [Vaisfeld et al., Chromosome 14 deletions, rings, and epilepsy genes, Epilepsia 2021 — PMID 33205446](https://pubmed.ncbi.nlm.nih.gov/33205446/) ([full text PDF](https://cris.unibo.it/retrieve/58b1f230-f985-4519-8f51-9cef4f713de5/draft_Proof_Ring14_2020.pdf))
- [Giovannini et al., Epilepsy in ring 14 syndrome, Epilepsia 2013 — PMID 24116895](https://pubmed.ncbi.nlm.nih.gov/24116895/)
- [Meza-Espinoza et al., Chromosomal instability in ring chromosome 14 syndrome, Mol Cytogenet 2024 (PMC11256661)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11256661/)
- [Messina et al., IgG Glycosylation Analysis in Ring14 Syndrome, Biomolecules 2026 (PMC13297435)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13297435/)
- [SanInocencio et al., patient-centered conceptual disease model, Qual Life Res 2026 — PMID 41533279](https://europepmc.org/article/MED/41533279)
- [Bershteyn et al., Cell-autonomous correction of ring chromosomes in human iPSCs, Nature 2014 — PMID 24413397](https://www.nature.com/articles/nature12923)
- [Vasconcelos et al., Multimodal imaging of ring 14 syndrome associated maculopathy — PMID 31755799](https://pubmed.ncbi.nlm.nih.gov/31755799/)
- [Guilherme et al., Mechanisms of ring chromosome formation, ring instability and clinical consequences, BMC Med Genet 2011](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3309960/)
- [MedGen: Ring chromosome 14 (C2930916)](https://www.ncbi.nlm.nih.gov/medgen/419284)
- [MedlinePlus Genetics: Ring chromosome 14 syndrome](https://medlineplus.gov/genetics/condition/ring-chromosome-14-syndrome/)
- [GARD: Ring chromosome 14](https://rarediseases.info.nih.gov/diseases/6072/ring-chromosome-14)
- [OMIM 616606](https://omim.org/entry/616606)
- [ClinicalTrials.gov NCT06813469 — MD-RING](https://clinicaltrials.gov/study/NCT06813469)
- [Ring14 International clinical database](http://www.ring14.org/eng/120/clinical-database/)
- [Hanzal et al., Lipoid pneumonia following chronic aspiration of cannabis oil, Chest 2025 — PMID 40348517](https://pubmed.ncbi.nlm.nih.gov/40348517/)
- [Ivanoff et al., Ring chromosome 14 syndrome: what the dentist should know, Folia Med 2023 — PMID 36855970](https://pubmed.ncbi.nlm.nih.gov/36855970/)
- [Barbour et al., Population-based study of rare epilepsy incidence, Epilepsia 2024 — PMID 38795333](https://pubmed.ncbi.nlm.nih.gov/38795333/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 33 |
| On topic | 25 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:22579566` (1 mention) - Evolution of metabolic rate in a parasitic wasp: the role of limitation in intrinsic resources.
  - shared terms: phenotype

Weighed against this report's own most characteristic terms: `ring`, `verify`, `chromosome`, `syndrome`, `gene`, `guideline`, `deletion`, `epilepsy`, `seizure`, `patient`, `phenotype`, `terminal`, `disease`, `q32`, `instability`, `zollino`, `model`, `retinal`, `mechanism`, `human`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 175 |
| Resolved | 172 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 24 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014708` (2 mentions) - the report calls it "MONDO"; MONDO calls it **ring chromosome 14**
- `HP:0000752` (1 mention) - the report calls it "large proportion of patients" **[verify]"; HP calls it **Hyperactivity**
- `HP:0000733` (1 mention) - the report calls it "Frequent"; HP calls it **Motor stereotypy**
- `HP:0002360` (1 mention) - the report calls it "Less frequent"; HP calls it **Sleep disturbance**
- `HP:0002205` (1 mention) - the report calls it "Recurring features include … increased incidence of infections, particularly respiratory infections" **[verify]"; HP calls it **Recurrent respiratory infections**
- `HP:0006532` (1 mention) - the report calls it "Spectrum "from recurrent upper airways infections to severe pneumonia" **[verify]"; HP calls it **Recurrent pneumonia**
- `UBERON:0001007` (1 mention) - the report calls it "feeding difficulty, dysphagia, GERD, celiac disease"; UBERON calls it **digestive system**
- `UBERON:0001130` (1 mention) - the report calls it "scoliosis, kyphosis"; UBERON calls it **vertebral column**
- `UBERON:0004288` (1 mention) - the report calls it "osteopenia/osteoporosis"; UBERON calls it **skeleton**
- `UBERON:0001015` (1 mention) - the report calls it "hypotonia"; UBERON calls it **musculature**
- `GO:0005794` (1 mention) - the report calls it "site of IgG N-glycan maturation"; GO calls it **Golgi apparatus**
- `NCIT:C121351` (1 mention) - the report calls it "implied by multidisciplinary model"; NCIT calls it **Occupational Therapy**
- `NCIT:C15240` (2 mentions) - the report calls it "de novo, low recurrence risk"; NCIT calls it **Genetic Counseling**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016458` (obsolete gene silencing) (1 mention)
- `GO:0006486` (obsolete protein glycosylation) (1 mention) - replaced by `GO:0009101`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000957` (1 mention) - the report calls it "Café-au-lait spots"; HP calls it **Cafe-au-lait spot**, and lists "Cafe-au-lait spots" among its other names
- `HP:0001004` (1 mention) - the report calls it "Lymphedema — "puffy hands and/or feet"; HP calls it **Lymphedema**, and lists "Onset of lymphedema around puberty" among its other names
- `CL:0002586` (2 mentions) - the report calls it "Retinal pigment epithelium"; CL calls it **retinal pigment epithelial cell**
- `CL:0000188` (1 mention) - the report calls it "Skeletal muscle"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `CL:0000057` (2 mentions) - the report calls it "Dermal fibroblasts", "Patient dermal fibroblasts"; CL calls it **fibroblast**
- `NCBITaxon:7227` (1 mention) - the report calls it "D. melanogaster"; NCBITaxon calls it **Drosophila melanogaster**
- `NCBITaxon:4932` (1 mention) - the report calls it "Yeast"; NCBITaxon calls it **Saccharomyces cerevisiae**, and lists "baker's yeast" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `ORPHA:1440` - called "Orphanet", "ORDO annotation"
- `CL:0000057` - called "Dermal fibroblasts", "Patient dermal fibroblasts"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.