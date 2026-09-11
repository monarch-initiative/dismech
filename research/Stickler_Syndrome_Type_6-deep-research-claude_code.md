---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-07T21:41:45.173678'
end_time: '2026-09-07T21:47:28.710937'
duration_seconds: 343.54
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Stickler Syndrome Type 6
  mondo_id: MONDO:0031047
  category: Mendelian
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
  - claude-sonnet-5
  web_search_requests: 16
  num_turns: 34
  total_cost_usd: 1.5537824000000005
  session_id: 8ebdc07f-4d6e-520e-ba30-ed7a3a7db882
  stop_reason: end_turn
  assistant_text_blocks: 3
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
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 15
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 46
  verified: 43
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 28
  labels_matching: 12
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: HP:0000699
    reported_labels:
    - approx.; verify
    ontology_label: Diastema
  - term_id: HP:0005280
    reported_labels:
    - verify
    ontology_label: Depressed nasal bridge
  - term_id: HP:0000463
    reported_labels:
    - Congenital
    ontology_label: Anteverted nares
  - term_id: HP:0002980
    reported_labels:
    - Bowing of the legs
    ontology_label: Femoral bowing
  - term_id: CL:0002327
    reported_labels:
    - "mammary basal cell \u2014 not relevant, disregard"
    ontology_label: mammary gland epithelial cell
  - term_id: CL:0002617
    reported_labels:
    - "endothelial cell of vitreous \u2014 verify"
    ontology_label: adipocyte of breast
  - term_id: UBERON:0003889
    reported_labels:
    - vitreous body
    ontology_label: fallopian tube
  - term_id: UBERON:0000362
    reported_labels:
    - cochlea
    ontology_label: renal medulla
  - term_id: UBERON:0002513
    reported_labels:
    - epiphysis
    ontology_label: endochondral bone
  - term_id: UBERON:0002520
    reported_labels:
    - cartilage tissue
    ontology_label: submandibular lymph node
  - term_id: UBERON:0000992
    reported_labels:
    - "intervertebral disc \u2014 verify exact ID"
    ontology_label: ovary
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0062023
    ontology_label: obsolete collagen-containing extracellular matrix
    replaced_by: GO:0031012
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Stickler Syndrome Type 6
- **MONDO ID:** MONDO:0031047 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Stickler Syndrome Type 6** covering all of the
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

I'll research Stickler Syndrome Type 6 now, using web search and fetch tools to gather authoritative, citable information.

I now have sufficient primary-literature grounding. Here is the comprehensive research report.

# Stickler Syndrome Type 6 (COL9A3-Related Stickler Syndrome) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Stickler syndrome type VI (STL6) is an ultra-rare, autosomal recessive connective tissue disorder caused by biallelic (homozygous or compound heterozygous) loss-of-function variants in *COL9A3*, which encodes the α3 chain of type IX collagen. It belongs to the broader Stickler syndrome spectrum — a group of hereditary collagenopathies affecting the eye, ear, face, and joints — but is genetically and phenotypically distinct from the far more common autosomal dominant forms (Stickler type I–III, due to *COL2A1*, *COL11A1*, *COL11A2*). STL6 is one of three "type IX collagen" recessive subtypes (STL4/*COL9A1*, STL5/*COL9A2*, STL6/*COL9A3*), which are clinically similar to one another and are collectively often discussed together in the literature as "type IX collagen–related (recessive) Stickler syndrome."

**Key identifiers:**
| Resource | Identifier |
|---|---|
| OMIM phenotype | #620022 — STICKLER SYNDROME, TYPE VI (STL6) |
| OMIM gene | *120270 — COLLAGEN, TYPE IX, ALPHA-3 (COL9A3); HGNC:2219 |
| Orphanet | ORPHA:250984 (per search results; verify against current Orphadata export) |
| MONDO | MONDO:0031047 (as supplied — cross-reference not independently confirmed via OLS/Monarch due to a network access limitation during this research session; recommend confirming via `just fetch-reference` / OAK before curation) |
| Locus | 20q13.33 |
| Gene family | FACIT collagen (Fibril-Associated Collagens with Interrupted Triple helices) |

**Synonyms:** Stickler syndrome, type VI; STL6; autosomal recessive Stickler syndrome, COL9A3-related; hereditary arthro-ophthalmopathy (generic Stickler syndrome synonym, not type-specific).

**Evidence base:** Information is derived almost entirely from aggregated case reports/case series and one larger multi-family cohort study — not EHR-scale or population registries, given the rarity of the recessive, *COL9A3*-specific subtype (fewer than 10 published families as of 2022; a 2024 combined *COL9A1/2/3* cohort added 13 patients from 11 families) (Rad et al. 2022, PMC8892745/PMID:35241111; cohort study PMID:39406934).

---

## 2. Etiology

**Disease causal factor:** STL6 is caused exclusively by biallelic loss-of-function (LOF) variants in *COL9A3* (nonsense, frameshift, canonical splice-site, or whole-exon-skipping variants), resulting in absence of a functional α3(IX) collagen chain and, because type IX collagen is an obligate heterotrimer, functional loss of the entire collagen IX molecule.

> "Pathogenic variants in COL9A1, COL9A2, and COL9A3 associated with Stickler syndrome are biallelic and have a loss-of-function effect, resulting in complete absence of the protein." (GeneReviews, NBK1302)

**Genetic risk factors:**
- Biallelic *COL9A3* pathogenic variants (homozygous or compound heterozygous) — causal, not merely a risk factor.
- Reported variants include: c.107_116del p.(Pro36Argfs\*49); c.1204C>T p.(Arg402\*); c.355delC p.(Leu119Serfs\*9) (Rad et al. 2022, PMC8892745); the original loss-of-function report (Faletra et al. 2014, PMID:24273071); and a subsequent case (Hanson-Kahn et al. 2018, PMID:30450842).
- **Consanguinity is a major risk-enabling factor**: in the 2024 cohort of 13 patients from 11 families with type IX collagen–related recessive Stickler syndrome, 53.8% had consanguineous parents (PMID:39406934) — consistent with rare autosomal recessive disease enrichment in consanguineous unions.
- **Founder/heterozygous allelic variants at the same locus increase risk for *related but distinct* phenotypes**, not STL6 itself: the *COL9A3* "Trp3" allele (c.307C>T, p.Arg103Trp) is a common missense polymorphism (not the biallelic LOF mechanism of STL6) associated with ~3-fold increased risk of lumbar intervertebral disc disease in heterozygous carriers (Paassilta et al. 2001, *JAMA*, PMID:11308397: found in 12.2% of lumbar disc disease cases vs. 4.7% of controls). Separately, heterozygous *COL9A3* splice-site/missense variants cause multiple epiphyseal dysplasia type 3 (EDM3/MED3, OMIM #600969) via a dominant-negative mechanism (Paassilta et al. 1999/2000-era reports; PMID:10090888 "COL9A3: A third locus for multiple epiphyseal dysplasia").

**Environmental risk factors:** None identified specific to this Mendelian recessive collagenopathy; no gene-environment interaction data were located.

**Protective factors:** None reported in the literature; this is a fully penetrant Mendelian LOF disorder once biallelic, so no protective allele has been described.

**Gene-environment interactions:** Not established/not applicable for this monogenic disorder.

---

## 3. Phenotypes

Phenotype frequency data below are pooled from the two principal case series of type IX collagen–related recessive Stickler syndrome (Rad et al. 2022, n=~7 COL9A3 patients across 3 families plus literature review to 4 families; and the larger combined COL9A1/2/3 cohort, PMID:39406934, n=13/11 families). Because *COL9A3*-specific numbers are drawn from very small samples, frequencies for the combined "type IX collagen" group are given where *COL9A3*-only figures were not separately reported — this is an important caveat for curation.

| Phenotype | Type | Frequency (type IX collagen recessive Stickler, pooled) | Onset | HPO term (to verify) |
|---|---|---|---|---|
| Sensorineural hearing loss (moderate–severe/profound, downsloping high-frequency-predominant) | Clinical sign / audiometric | 91.7–100% (near-universal; "all patients with variants... had sensorineural hearing loss" per GeneReviews) | Early childhood, sometimes present but missed on newborn screening; progressive | HP:0000407 (Sensorineural hearing loss) |
| High myopia (>−6D) | Clinical sign | 77–100% | Congenital/early childhood, non-progressive refractive component but vitreous disease progresses | HP:0011003 (High myopia) / HP:0000545 (Myopia) |
| Vitreous anomaly (hypoplastic/"optically empty" vitreous, membranous or beaded) | Clinical/imaging sign | 92.3% | Congenital | HP:0007957 (vitreoretinal degeneration) or HP:0000572-family; verify exact term |
| Retinal detachment / retinal tear | Complication | 8–18% in COL9A-related recessive forms specifically (PMID:39406934: 15.4%, 2/13, both horseshoe tears post-PVD, no bilateral cases or giant retinal tears) — substantially **lower** than the up to 78% reported in dominant (COL2A1/COL11A1) Stickler syndrome | Young adulthood (documented ages 24 and 36 in the cohort) | HP:0000541 (Retinal detachment) |
| Lattice retinal degeneration | Clinical/imaging sign | Present in some families without progressing to detachment (Rad et al. 2022) | Variable | HP:0000699 (approx.; verify) |
| Cataract | Clinical sign | Reported but frequency not separately quantified for COL9A3 | Variable, often earlier than general population | HP:0000518 (Cataract) |
| Midface/malar hypoplasia | Physical/craniofacial | 30.8% | Congenital, may be subtle | HP:0011800 or HP:0000271 (Abnormality of the face) — verify specific term |
| Depressed/flat nasal bridge | Physical | Variable, reported in younger patients with more prominent skeletal phenotype | Congenital | HP:0005280 (verify) |
| Anteverted nares | Physical | Reported, especially in younger/more skeletally affected patients | Congenital | HP:0000463 |
| **Cleft palate / Pierre Robin sequence** | Physical | **0% reported in COL9A1/2/3-related (recessive) Stickler syndrome** — a key distinguishing negative feature versus dominant *COL11A1/COL11A2*-related Stickler syndrome, where cleft palate is common | — | HP:0000175 (Cleft palate) — noted as absent |
| Mild spondyloepiphyseal dysplasia | Skeletal | Reported, especially in younger patients (ages 3–11 in Rad et al. 2022); older patients (ages 57–65) presented with myopia/hearing loss but minimal skeletal findings | Childhood-onset, may attenuate/be less clinically apparent with age | HP:0002651 (Spondyloepiphyseal dysplasia) |
| Precocious/early-onset osteoarthritis | Skeletal, progressive | Reported (consistent with collagen IX cartilage role) | Adult, earlier than general population | HP:0002829 (Arthralgia) / HP:0002758 (Osteoarthritis) |
| Joint hypermobility / joint pain | Skeletal | ~15% joint pain reported in aggregated literature review of COL9A-variant patients | Variable | HP:0001382 (Joint hypermobility) |
| Tibial/femoral bowing at birth | Skeletal | Reported in at least one family (Rad et al. 2022) | Congenital | HP:0002980 (Bowing of the legs) — verify exact term |

**Quality of life impact:** Not formally measured with validated instruments (EQ-5D, SF-36) in the STL6-specific literature located. Qualitatively, the combination of early progressive sensorineural hearing loss and high myopia with vitreoretinal fragility carries substantial risk to communication development and vision-dependent function; the lower (but non-zero) retinal detachment risk versus dominant Stickler forms still warrants lifelong ophthalmologic surveillance. No disease-specific QOL studies were found; this should be flagged as a knowledge gap.

---

## 4. Genetic/Molecular Information

**Causal gene:** *COL9A3* (HGNC:2219; OMIM *120270), chromosome 20q13.33, encoding the α3(IX) collagen chain.

**Variant classification/type:** All reported STL6-causing variants are biallelic loss-of-function: frameshift (c.107_116del, c.355delC), nonsense (c.1204C>T p.Arg402\*), and splice-site variants, consistent with a null/LOF disease mechanism rather than dominant-negative. This contrasts with the *heterozygous* missense/splice variants that cause the allelic conditions multiple epiphyseal dysplasia type 3 (dominant-negative mechanism) and the *COL9A3* Trp3 risk allele for disc disease (hypomorphic/structural mechanism).

**Population allele frequency:** Specific gnomAD constraint metrics (pLI/LOEUF) for *COL9A3* were not retrievable in this session (network access to gnomad.broadinstitute.org was not available); this should be checked directly in gnomAD before curation, as *COL9A3* biallelic-LOF-tolerant vs. -intolerant classification is directly relevant to the "recessive" gene category the field expects for this gene.

**Somatic vs. germline:** Germline only; no somatic/oncologic relevance.

**Functional consequence:** Complete loss of α3(IX) chain → failure of the obligate α1(IX)/α2(IX)/α3(IX) heterotrimer assembly → functional absence of collagen IX at the tissue level (a "functional knockout" of the whole protein, per the mouse literature, PMID:9252382), despite only one of the three chains being genetically null.

**Modifier genes:** None specifically established for STL6; general genotype-phenotype variability within families (e.g., differing skeletal severity by age at the time of the Rad et al. 2022 report) suggests age-dependent expressivity rather than a documented modifier locus.

**Epigenetic information:** No disease-specific epigenetic (DNA methylation/histone) data identified for *COL9A3*/STL6.

**Chromosomal abnormalities:** Not applicable — STL6 is due to intragenic sequence-level LOF variants, not large chromosomal rearrangements.

**Allelic disorders at the *COL9A3* locus (important for differential/knowledge-base cross-linking):**
- Multiple epiphyseal dysplasia, type 3 (EDM3/MED3; OMIM #600969) — heterozygous, dominant-negative *COL9A3* variants (PMID:10090888).
- Intervertebral disc disease, susceptibility to (OMIM #603932) — the common Trp3 (p.Arg103Trp) polymorphism, heterozygous, ~3-fold odds ratio (PMID:11308397; ClinVar RCV000018677).

---

## 5. Environmental Information

No environmental toxins, occupational exposures, radiation, or infectious triggers were identified as contributing to STL6 pathogenesis in the literature search — consistent with its status as a fully genetically determined Mendelian recessive collagenopathy. Lifestyle factors are not etiologic but are relevant to secondary complication risk in a general sense (e.g., high-impact activity and retinal detachment risk in myopic/vitreopathic eyes is a commonly cited precaution across the Stickler syndrome spectrum, though this is anecdotal clinical guidance rather than a quantified risk-factor finding specific to *COL9A3* patients in the literature reviewed). No infectious agents are implicated.

---

## 6. Mechanism / Pathophysiology

**Causal chain (numbered, from molecular lesion to clinical manifestation):**

1. Biallelic loss-of-function variant in *COL9A3* (nonsense/frameshift/splice) leads to **absence of a functional α3(IX) collagen polypeptide** (demonstrated directly in humans by variant type; PMID:24273071, PMID:35241111).
2. Because type IX collagen is an obligate heterotrimer of α1(IX)/α2(IX)/α3(IX) chains, absence of α3(IX) **results in failure of collagen IX heterotrimer assembly and secretion**, producing a functional null for the entire collagen IX molecule — this step is *inferred by analogy from mouse Col9a1-null models*, in which loss of a single chain functionally knocks out the whole trimer (PMID:9252382: "Absence of the α1(IX) chain leads to a functional knock-out of the entire collagen IX protein in mice"), rather than directly demonstrated for the human α3-null state, but is considered the accepted mechanistic model in the human genetics literature (PMID:35241111 explicitly states each of the three collagen IX chains is essential for collagen IX function).
3. Collagen IX (a FACIT collagen) normally decorates the surface of type II/XI collagen fibrils in vitreous, cartilage, the tectorial membrane of the cochlea, and intervertebral disc, cross-linking fibrils and connecting them to other extracellular matrix components. **Loss of collagen IX leads to disrupted fibril crosslinking/organization** in each of these collagen-II-containing tissues — this step is *inferred* from the known biochemical role of collagen IX and from mouse structural studies, rather than directly visualized in human tissue in the cited reports.
4. In the **vitreous**, disrupted fibrillar organization leads to abnormal/hypoplastic vitreous architecture and vitreoretinal degeneration, which in turn predisposes to **high myopia**, lattice degeneration, and (with posterior vitreous detachment as a precipitating event) **retinal tears/detachment** — demonstrated clinically by near-universal myopia/vitreous anomaly and a measurable (8–18%) detachment rate temporally associated with PVD in the human cohort (PMID:39406934).
5. In the **cochlea**, disrupted collagen IX–dependent matrix organization of the tectorial membrane leads to **progressive sensorineural hearing loss**, beginning basally (high-frequency) and progressing apically — demonstrated directly in *Col9a1*-null mice, which show "progressive hearing loss, already apparent at young age, and morphological changes of the tectorial membrane, starting in the basal turn of the cochlea and progressing towards the apical turn" (mouse model evidence cited in PMC9498449's review of hearing loss in Stickler syndrome), and corroborated clinically by the human high-frequency-predominant, progressive audiometric pattern.
6. In **cartilage and epiphyseal growth plates**, loss of collagen IX leads to disorganized chondrocyte/matrix architecture, producing **mild spondyloepiphyseal dysplasia** in childhood and, over time, **early-onset degenerative joint disease/osteoarthritis** — directly demonstrated in *Col9a1*-null mice, which "develop early-onset degenerative joint disease resembling osteoarthritis" with no skeletal abnormality at birth (PMID:8197187), mirroring the human pattern in which skeletal features are more prominent in younger patients and attenuate with age as osteoarthritis supervenes (PMID:35241111).
7. In the **intervertebral disc**, collagen IX loss contributes to **disc matrix fragility**, plausibly underlying both the biallelic-null skeletal phenotype and, at the heterozygous-carrier level for the distinct Trp3 allele, susceptibility to intervertebral disc disease (PMID:11308397) — this is a related but mechanistically and allelically distinct pathway from STL6 itself and should not be conflated with the biallelic STL6 phenotype.
8. In **craniofacial development**, the tissue distribution of collagen IX (largely cartilage/vitreous/inner ear rather than the palatal shelf mesenchyme relevant to cleft palate) plausibly explains why **cleft palate/Pierre Robin sequence is not observed** in COL9A-related recessive Stickler syndrome, unlike the dominant *COL11A1/COL11A2* forms — this is an inference from the consistent absence of the phenotype across all reported cases rather than a directly demonstrated tissue-specific mechanism.

**Molecular pathways:** No specific signaling cascade (Wnt/MAPK/mTOR/etc.) has been implicated; the mechanism is structural extracellular matrix disruption rather than dysregulated signal transduction.

**Cellular processes:** Disrupted chondrocyte extracellular matrix organization; secondary early chondrocyte/cartilage degeneration consistent with osteoarthritis pathobiology (not classical inflammatory arthritis).

**Protein dysfunction:** Complete loss-of-function (null) rather than misfolding/aggregation or dominant-negative gain-of-function — distinguishing STL6 mechanistically from the heterozygous dominant-negative *COL9A3* MED3 allelic disorder.

**Tissue damage mechanism:** Structural/mechanical extracellular matrix fragility (fibril cross-linking failure) rather than oxidative stress, ischemia, or classic fibrosis.

**Suggested GO terms:** GO:0030198 (extracellular matrix organization), GO:0030199 (collagen fibril organization), GO:0032964 (collagen biosynthetic process), GO:0007601 (visual perception, downstream/phenotypic), GO:0007605 (sensory perception of sound, downstream/phenotypic).

**Suggested CL terms:** CL:0000138 (chondrocyte), CL:0002327 (mammary basal cell — not relevant, disregard), CL:0000064 (ciliated cell — not relevant); relevant candidates: CL:0000138 (chondrocyte), CL:0002617 (endothelial cell of vitreous — verify), and inner-ear-specific cell types associated with the tectorial membrane (e.g., interdental cells; verify exact CL ID before curation).

**Molecular profiling / advanced technologies:** No transcriptomic, proteomic, single-cell, or spatial data specific to human *COL9A3*-null tissue were identified in this search; this is a knowledge gap for an ultra-rare disease with no dedicated omics studies located.

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: eye (vitreous, retina, lens), inner ear (cochlea), skeleton (epiphyses, joints, long bones), craniofacial skeleton (variable).
- Secondary: intervertebral discs (via the allelic/heterozygous mechanism more than the biallelic STL6 phenotype itself).
- Body systems: ophthalmic, auditory/vestibular, musculoskeletal; **not** typically cardiovascular, respiratory (beyond the dominant-form Pierre Robin airway risk, which is not a feature of STL6), or gastrointestinal.

**Tissue/cell level:** Cartilage (hyaline, epiphyseal growth plate), vitreous body extracellular matrix, cochlear tectorial membrane, intervertebral disc annulus/nucleus.

**Subcellular level:** Extracellular matrix compartment (collagen fibril surface); GO Cellular Component candidate: GO:0005581 (collagen trimer), GO:0062023 (collagen-containing extracellular matrix).

**Localization (UBERON candidates, to verify against OAK before curation):**
- UBERON:0003889 (vitreous body) / UBERON:0001797 (vitreous humor)
- UBERON:0000965 (lens) 
- UBERON:0000955 → cochlea-specific: UBERON:0000362 (cochlea), tectorial membrane term (verify exact UBERON ID)
- UBERON:0002513 (epiphysis) / UBERON:0002520 (cartilage tissue)
- UBERON:0000992 (intervertebral disc — verify exact ID)

**Lateralization:** Bilateral for hearing loss and myopia (systemic connective tissue disorder); retinal detachment events in the reported cohort were unilateral at presentation with no contralateral involvement documented at follow-up (PMID:39406934).

---

## 8. Temporal Development

**Onset:** Congenital/early-childhood for the ocular (myopia, vitreous anomaly) and skeletal (spondyloepiphyseal changes, long-bone bowing) features; hearing loss may be present from infancy but escape newborn hearing screening in some cases ("both failed and uneventful auditory screening at young age has been reported").

**Onset pattern:** Insidious/subclinical initial presentation for hearing loss, with clear progression documented over time; ocular anomalies are structurally congenital but their complications (retinal tear/detachment) are age-dependent events typically in young adulthood (ages 24 and 36 in the reported cohort).

**Progression:**
- Hearing loss: progressive, "even to profound hearing loss" with age, following a basal-to-apical cochlear pattern.
- Skeletal: more prominent spondyloepiphyseal/craniofacial findings in younger patients (ages 3–11), with older patients (ages 57–65) showing minimal skeletal findings but persistent myopia/hearing loss — interpreted in the source as an apparent attenuation of skeletal manifestations with age, though this could also reflect ascertainment/cohort differences and is presented with that caveat by the primary authors (PMID:35241111).
- Retinal detachment: not congenital — an event superimposed on longstanding vitreous anomaly, precipitated by posterior vitreous detachment in adulthood.

**Disease course pattern:** Chronic, non-remitting, generally progressive rather than relapsing-remitting; not life-limiting based on available reports (no early mortality reported).

**Critical periods:** Childhood is the critical window for surveillance/early intervention (hearing amplification, myopia correction, orthopedic monitoring) given the combination of early-onset progressive sensorineural hearing loss and high myopia.

---

## 9. Inheritance and Population

**Epidemiology:** Stickler syndrome overall has an estimated incidence of ~1:7,500–1:9,000 births, making it one of the most common causes of inherited/familial retinal detachment — but this figure is overwhelmingly driven by the dominant *COL2A1*-related form (type 1). **STL6 specifically is ultra-rare**: as of the 2022 systematic description, only 4 families with biallelic *COL9A3* variants had been reported in the literature; a 2024 cohort study identified 13 patients from 11 families with recessive Stickler syndrome due to *COL9A1*, *COL9A2*, *or COL9A3* combined (not COL9A3 alone) through the NHS England Highly Specialised Stickler Syndrome Service (2015–2022) (PMID:39406934). No population-specific prevalence/incidence estimate for *COL9A3*-only STL6 was located; it should likely be recorded as `NOT_YET_DOCUMENTED` / `CASES_IN_LITERATURE` in a structured prevalence model, given the single-digit-families evidence base.

**Inheritance pattern:** Autosomal recessive (in contrast to autosomal dominant types 1–3).

**Penetrance:** Appears complete for biallelic LOF genotypes based on all reported cases, though the very small number of families precludes formal penetrance estimation.

**Expressivity:** Variable — notably in skeletal severity by age at ascertainment, and in ocular complication severity between families (e.g., in Rad et al. 2022, one family had retinal detachment with advanced vitreoretinal degeneration while the other two had lattice degeneration without detachment).

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported for *COL9A3*.

**Founder effects:** Not established; the high consanguinity rate (53.8%) in the largest combined cohort suggests genetic isolate/relatedness effects at the family level rather than a documented population founder allele.

**Consanguinity role:** Substantial — over half of reported families in the largest cohort had consanguineous parents, as expected for an ultra-rare autosomal recessive condition.

**Carrier frequency:** Not established in population databases for *COL9A3*-null alleles specifically; the common Trp3 missense allele carrier frequency (~4.7% in Finnish controls) should not be conflated with LOF carrier frequency for STL6.

**Population demographics:** No specific ethnic/geographic enrichment for *COL9A3*-null STL6 was identified beyond the consanguinity association; reported families appear geographically dispersed (Italy — original 2013 report; additional international families in subsequent reports; UK-based NHS cohort for the combined COL9A1/2/3 series).

**Sex ratio:** No sex predilection reported (autosomal recessive, biologically expected to be equal).

---

## 10. Diagnostics

**Clinical tests:**
- Ophthalmologic exam: slit-lamp/dilated fundus exam for vitreous architecture (hypoplastic/optically empty vitreous), myopia refraction, lattice degeneration, retinal status.
- Audiology: pure-tone audiometry showing downsloping sensorineural hearing loss; serial testing to document progression; newborn hearing screening (may be falsely reassuring, as noted above).
- Skeletal imaging: radiographs for epiphyseal changes (spondyloepiphyseal dysplasia pattern), assessment for long-bone bowing in infancy.
- Craniofacial exam: assessment for midface hypoplasia, nasal bridge/nares morphology (absence of cleft palate is itself diagnostically informative, distinguishing from dominant COL11A-related forms).

**Genetic testing:** Multigene panel testing (Stickler/collagenopathy panel covering *COL2A1*, *COL11A1*, *COL11A2*, *COL9A1*, *COL9A2*, *COL9A3*) or exome sequencing is the recommended approach per GeneReviews, given phenotypic overlap across genes and the need to distinguish dominant from recessive inheritance for counseling; single-gene *COL9A3* sequencing is appropriate when recessive inheritance/consanguinity and a compatible phenotype (no cleft palate, prominent hearing loss) raise specific suspicion.

**Clinical criteria:** No STL6-specific formal diagnostic criteria were located; general Stickler syndrome clinical diagnostic criteria (ocular + auditory + orofacial + skeletal major/minor criteria, historically per Rose et al.) are applied, with molecular confirmation of biallelic *COL9A3* variants required to specify the STL6 subtype.

**Differential diagnosis:** Marshall syndrome (flatter/retracted midface, short stature, thick calvaria, intracranial calcifications — distinguishing from Stickler's flat malar appearance); Wagner syndrome (vitreoretinal findings without systemic features); Kniest dysplasia ("Swiss-cheese" collagen appearance on electron microscopy, more severe skeletal dysplasia); spondyloepiphyseal dysplasia congenita; spondyloperipheral dysplasia; metatropic dysplasia; multiple epiphyseal dysplasia (including the allelic *COL9A3*-heterozygous EDM3); Knobloch syndrome; Marfan syndrome.

**Omics-based diagnostics:** Not routinely used; standard clinical practice relies on targeted/panel/exome DNA sequencing rather than transcriptomic or proteomic diagnostics for this condition.

**Screening:** No population newborn screening exists for STL6 specifically; carrier screening/prenatal diagnosis would be offered on a family-specific basis once a proband's biallelic variants are identified, consistent with standard autosomal recessive genetic counseling practice (25% recurrence risk per GeneReviews).

---

## 11. Outcome/Prognosis

**Survival and mortality:** No mortality or reduced life expectancy has been reported in association with STL6; the disorder is not known to be life-limiting.

**Morbidity/function:** Principal morbidity is sensory: potential for significant-to-profound hearing impairment if untreated, and vision-threatening complications (retinal detachment) in a minority of patients, superimposed on universal high myopia. Early-onset osteoarthritis contributes to musculoskeletal morbidity in adulthood.

**Disease course/complications:** Retinal detachment (documented risk ~15% in the largest combined type-IX-collagen recessive cohort, notably lower than the dominant forms' risk of up to 78%); progressive hearing loss to potentially profound levels; early osteoarthritis.

**Recovery potential:** With treatment (hearing amplification/audiologic management, prophylactic and therapeutic retinal interventions, myopia correction), functional outcomes for vision and hearing can be substantially improved; without surveillance, undetected retinal detachment risks permanent vision loss.

**Prognostic factors:** Age (skeletal findings may be more apparent/severe in childhood; ocular complications accrue risk with age via PVD-related tear formation); genotype (LOF variant type does not yet show clear genotype-severity correlation given the small case numbers, though the 2022 report explicitly frames its findings as contributing "genotype-phenotype associations from the literature" for future correlation work).

---

## 12. Treatment

**Pharmacotherapy:** No disease-modifying pharmacotherapy exists; management is manifestation-based/supportive. NCIT candidate: `NCIT:C15747` (Supportive Care).

**Ophthalmic — surgical/interventional:**
- Prophylactic laser retinopexy / cryotherapy for high-risk vitreoretinal changes (extensively studied and best characterized in the dominant Stickler population, with extrapolated but less quantified application in recessive/COL9A forms); NCIT: `NCIT:C15313` (Radiation Therapy) is not a fit — laser retinopexy would map more appropriately to a specific ophthalmic procedure term (verify exact NCIT/procedure code; consider `NCIT:C15329` Surgical Procedure with a device/procedure qualifier, per the project's device-vs-action convention).
- Retinal detachment repair: vitrectomy, scleral buckle, and/or laser/cryotherapy combination when detachment occurs (as used in the reported cohort's two detachment cases).
- Myopia correction: spectacles/refractive correction. NCIT: none specific; general optical correction is not typically NCIT-coded as a clinical intervention procedure.

**Auditory:**
- Hearing aid amplification for moderate-to-severe loss.
- Cochlear implantation would be the standard-of-care escalation pathway for profound sensorineural hearing loss based on general otologic practice, though STL6/COL9A3-specific cochlear implant outcome data were not identified in this search (knowledge gap). NCIT: candidate device-implant term, mapped via the project's device/procedure qualifier convention rather than as a bare treatment term.

**Musculoskeletal/supportive:**
- Physical therapy for joint symptoms/early osteoarthritis (`NCIT:C15302` Physical Therapy).
- Orthopedic monitoring/management as needed for skeletal dysplasia features (`NCIT:C16186` Orthopedic Surgical Procedure, if surgery is required).

**Genetic counseling:** `NCIT:C15240` (Genetic Counseling) — appropriate given autosomal recessive inheritance and 25% sibling recurrence risk.

**Experimental treatments:** No STL6- or *COL9A3*-specific clinical trials were identified via search; general Stickler syndrome trials (e.g., laser prophylaxis studies, NCT07146516 "Retinal Detachment Prevention (Laser Prophylaxis) in Stickler Syndrome") are ongoing but are not restricted to or specifically powered for the *COL9A3* subtype.

**Treatment outcomes:** Prophylactic laser retinopexy studies in Stickler syndrome broadly (not COL9A3-specific) report favorable detachment-prevention outcomes with a trade-off of measurable peripheral visual field constriction (e.g., one dominant-Stickler case series: no detachment/tear over mean 8.7-year follow-up in laser-treated eyes, with asymptomatic visual field constriction to ~50° per meridian) — cited here as general Stickler syndrome management evidence, not COL9A3-validated outcome data specifically.

**Treatment strategy:** Multidisciplinary care (ophthalmology, audiology, genetics, orthopedics/rehabilitation) is the standard approach; no COL9A3/STL6-specific treatment algorithm beyond general Stickler syndrome surveillance protocols (e.g., GeneReviews-recommended annual vitreoretinal and audiologic evaluation) was identified.

---

## 13. Prevention

**Primary prevention:** Not applicable in the classic sense (no modifiable environmental cause); genetic counseling and, where desired by families, carrier screening/preimplantation or prenatal genetic diagnosis are the relevant "primary prevention" tools for recurrence in known-carrier families.

**Secondary prevention:** Early detection via newborn hearing screening (imperfectly sensitive per the literature caveat above) and early ophthalmologic examination in at-risk families (siblings of an affected proband) to catch vitreoretinal changes before complications arise; prophylactic laser retinopexy in eyes judged high-risk for detachment, applied by extrapolation from dominant Stickler syndrome protocols.

**Tertiary prevention:** Ongoing surveillance to prevent progression of complications once diagnosed — e.g., serial audiometry to trigger timely amplification, ongoing retinal surveillance in known STL6 patients per GeneReviews-recommended annual evaluations.

**Immunization:** Not applicable (non-infectious genetic disorder).

**Screening:** No population-level newborn or carrier screening program specific to *COL9A3*/STL6 exists; family-specific cascade testing following identification of a proband's biallelic variants is the applicable model, per standard autosomal recessive genetic counseling practice.

**Behavioral interventions/public health measures:** Not applicable to this monogenic disorder beyond general activity precautions sometimes advised for high-myopia/vitreopathic patients (anecdotal across the Stickler syndrome literature, not COL9A3-specific evidence).

---

## 14. Other Species / Natural Disease

No naturally occurring *COL9A3*-null disease has been reported in companion animals or other species in the sources reviewed (OMIA and veterinary literature were not directly queried in this session and should be checked — for example, canine chondrodysplasias with collagen IX involvement are a plausible area to search but were not confirmed here). This is a knowledge gap that should be verified against OMIA before curation.

**Orthologous genes:** *Col9a3* is conserved in mouse (Mouse Genome Informatics; NCBI Gene) and other vertebrates as part of the conserved collagen IX/FACIT gene family; specific ortholog NCBI Gene IDs were not retrieved in this session but should be pulled from NCBI Gene/HomoloGene/Alliance of Genome Resources during curation.

---

## 15. Model Organisms

**Mouse — the primary model system for collagen IX biology, though largely characterized for *Col9a1* rather than *Col9a3* specifically:**

- *Col9a1*-null mice (Fässler et al. 1994, *PNAS*, PMID:8197187): "Homozygous mutant mice lacking α1(IX) collagen are viable and show no detectable abnormalities at birth but develop a severe degenerative joint disease resembling human osteoarthritis." This is the foundational model demonstrating that loss of one collagen IX chain functionally ablates the heterotrimer.
- Absence of the α1(IX) chain functionally knocks out the entire collagen IX protein (PMID:9252382) — mechanistic support for extrapolating from single-chain-null mouse data to the human α3(IX)-null (STL6) situation, though this is an **extrapolation across chains**, not a direct *Col9a3*-specific mouse study, and should be flagged as such in any model-link curation (a between-chain, not merely between-species, translational gap).
- *Col9a1*-null mice additionally show: progressive early-onset osteoarthritis-like joint disease, intervertebral disc herniation, progressive hearing loss with basal-to-apical tectorial membrane pathology, and trabecular bone deterioration with enlarged osteoclasts (Papas et al., PMC2677084) — collectively recapitulating the multi-tissue human STL4-6 phenotype (joint, disc, cochlear, and bone involvement) reasonably well, albeit generated from the α1 rather than α3 chain knockout.
- Col9a2-depletion mouse studies (e.g., a bioRxiv preprint on Col9a2 and osteochondral homeostasis) further support the cartilage/joint phenotype but were not peer-reviewed-confirmed in this search and should be verified before citation.

**Model characteristics/limitations:** The mouse literature strongly recapitulates the joint/skeletal and auditory phenotypes of human recessive Stickler syndrome. However, essentially all mechanistic mouse data available are for *Col9a1*, not *Col9a3* — meaning any model-to-mechanism link drawn for STL6 pathophysiology nodes would need to be flagged with an appropriate `divergences`/`limitations` caveat (a cross-chain, not merely cross-species, extrapolation) if incorporated into a dismech entry, per this project's model-credibility conventions. No *Col9a3*-specific knockout mouse study was identified in this search; this is a specific, actionable knowledge gap.

**Applications:** The *Col9a1*-null mouse remains the field's standard tool for studying collagen-IX-dependent joint degeneration, cochlear/tectorial membrane pathology, and disc degeneration mechanisms relevant by extension to STL6.

---

## Summary of Key Knowledge Gaps (flagged for curation awareness)

1. **MONDO:0031047 cross-reference to OMIM #620022/ORPHA:250984 was not independently re-verified via OLS/Monarch** in this session due to a network access restriction — confirm before use as a `disease_term`.
2. gnomAD constraint metrics (pLI/LOEUF, allele frequencies) for *COL9A3* were not retrieved directly and should be pulled from the gnomAD browser.
3. No *Col9a3*-specific (as opposed to *Col9a1*-generalized) mouse model data were found; any pathograph model link should record this as a limitation/divergence rather than treating *Col9a1* mouse data as direct.
4. Quality-of-life instrument data (EQ-5D/SF-36/disease-specific) are absent for this ultra-rare subtype.
5. Veterinary/other-species natural disease data were not confirmed (OMIA not directly queried).
6. Exact HPO term IDs listed above are best-effort candidates based on general Human Phenotype Ontology familiarity and should be confirmed via OAK/HPO browser lookup before binding into a knowledge base entry, per this project's ontology term contract.

---

## Sources

- [OMIM #620022 — Stickler Syndrome, Type VI (STL6)](https://omim.org/entry/620022)
- [OMIM Clinical Synopsis #620022](https://omim.org/clinicalSynopsis/620022)
- [OMIM *120270 — COL9A3](https://omim.org/entry/120270)
- [OMIM #600969 — Multiple Epiphyseal Dysplasia 3 context / COL9A3: A third locus for MED — PubMed PMID:10090888](https://pubmed.ncbi.nlm.nih.gov/10090888/)
- [OMIM #603932 — Intervertebral Disc Disease](https://www.omim.org/entry/603932)
- [Stickler Syndrome — GeneReviews®, NCBI Bookshelf NBK1302](https://www.ncbi.nlm.nih.gov/books/NBK1302/)
- [Autosomal recessive Stickler syndrome due to a loss of function mutation in the COL9A3 gene — PubMed PMID:24273071](https://pubmed.ncbi.nlm.nih.gov/24273071/)
- [Autosomal recessive Stickler syndrome resulting from a COL9A3 mutation — PubMed PMID:30450842](https://pubmed.ncbi.nlm.nih.gov/30450842/)
- [Identification of three novel homozygous variants in COL9A3 causing autosomal recessive Stickler syndrome — Orphanet J Rare Dis 2022, PMC8892745 / PMID:35241111](https://pmc.ncbi.nlm.nih.gov/articles/PMC8892745/)
- [Retinal detachment in Type IX collagen recessive Stickler syndrome — PMC11733291 / PMID:39406934](https://pmc.ncbi.nlm.nih.gov/articles/PMC11733291/)
- [Hearing Loss in Stickler Syndrome: An Update — PMC9498449](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9498449/)
- [Hearing impairment in Stickler syndrome: a systematic review — PMC3551705](https://pmc.ncbi.nlm.nih.gov/articles/PMC3551705/)
- [Autosomal Recessive Stickler Syndrome — PMC9324312](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9324312/)
- [Mice lacking alpha 1(IX) collagen develop noninflammatory degenerative joint disease — PNAS, PMID:8197187](https://www.pnas.org/content/91/11/5070)
- [Absence of the α1(IX) chain leads to a functional knock-out of the entire collagen IX protein in mice — PubMed PMID:9252382](https://pubmed.ncbi.nlm.nih.gov/9252382/)
- [Trabecular Bone Deterioration in col9a1+/− Mice — PMC2677084](https://pmc.ncbi.nlm.nih.gov/articles/PMC2677084/)
- [Identification of a novel common genetic risk factor for lumbar disk disease (COL9A3 Trp3 allele) — JAMA 2001, PMID:11308397](https://pubmed.ncbi.nlm.nih.gov/11308397/?dopt=Abstract)
- [Orphanet: Stickler syndrome](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=828)
- [Diagnosis and Management of Stickler Syndrome — American Academy of Ophthalmology](https://www.aao.org/eyenet/article/diagnosis-and-management-of-stickler-syndrome)
- [Encircling Laser Prophylaxis for Retinal Detachment in Stickler Syndrome — PMC13381354](https://pmc.ncbi.nlm.nih.gov/articles/PMC13381354/)
- [COL9A3 gene — MedlinePlus](https://medlineplus.gov/download/genetics/gene/col9a3.pdf)
- [Stickler Syndrome, Type VI — MalaCards](https://www.malacards.org/card/stickler_syndrome_type_vi)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 15 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 28 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000699` (1 mention) - the report calls it "approx.; verify"; HP calls it **Diastema**
- `HP:0005280` (1 mention) - the report calls it "verify"; HP calls it **Depressed nasal bridge**
- `HP:0000463` (1 mention) - the report calls it "Congenital"; HP calls it **Anteverted nares**
- `HP:0002980` (1 mention) - the report calls it "Bowing of the legs"; HP calls it **Femoral bowing**
- `CL:0002327` (1 mention) - the report calls it "mammary basal cell — not relevant, disregard"; CL calls it **mammary gland epithelial cell**
- `CL:0002617` (1 mention) - the report calls it "endothelial cell of vitreous — verify"; CL calls it **adipocyte of breast**
- `UBERON:0003889` (1 mention) - the report calls it "vitreous body"; UBERON calls it **fallopian tube**
- `UBERON:0000362` (1 mention) - the report calls it "cochlea"; UBERON calls it **renal medulla**
- `UBERON:0002513` (1 mention) - the report calls it "epiphysis"; UBERON calls it **endochondral bone**
- `UBERON:0002520` (1 mention) - the report calls it "cartilage tissue"; UBERON calls it **submandibular lymph node**
- `UBERON:0000992` (1 mention) - the report calls it "intervertebral disc — verify exact ID"; UBERON calls it **ovary**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0062023` (obsolete collagen-containing extracellular matrix) (1 mention) - replaced by `GO:0031012`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002651` (1 mention) - the report calls it "Spondyloepiphyseal dysplasia"; HP calls it **Spondyloepimetaphyseal dysplasia**
- `GO:0007601` (1 mention) - the report calls it "visual perception, downstream/phenotypic"; GO calls it **visual perception**
- `GO:0007605` (1 mention) - the report calls it "sensory perception of sound, downstream/phenotypic"; GO calls it **sensory perception of sound**
- `CL:0000064` (1 mention) - the report calls it "ciliated cell — not relevant"; CL calls it **ciliated cell**
- `GO:0062023` (1 mention) - the report calls it "collagen-containing extracellular matrix"; GO calls it **obsolete collagen-containing extracellular matrix**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.