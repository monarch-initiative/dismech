---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-07T22:02:52.463806'
end_time: '2026-09-07T22:07:42.172137'
duration_seconds: 289.71
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Intellectual Disability Autosomal Recessive 65
  mondo_id: MONDO:0020850
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
  web_search_requests: 12
  num_turns: 26
  total_cost_usd: 1.4299566
  session_id: 8e6a3453-99e0-563b-8e2c-3bcb30d1c949
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 12
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 59
  verified: 54
  not_found: 0
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 9
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: HP:0001263
    reported_labels:
    - ~100% (all reported cases)
    ontology_label: Global developmental delay
  - term_id: HP:0000750
    reported_labels:
    - Most patients (e.g., "5 words" at age 4 in one case)
    ontology_label: Delayed speech and language development
  - term_id: HP:0001510
    reported_labels:
    - Mild, in a subset
    ontology_label: Growth delay
  - term_id: HP:0000268
    reported_labels:
    - Present in a subset
    ontology_label: Dolichocephaly
  - term_id: HP:0012385
    reported_labels:
    - Present in majority (hallmark feature)
    ontology_label: Camptodactyly
  - term_id: HP:0001382
    reported_labels:
    - ~50% in 2024 cohort
    ontology_label: Joint hypermobility
  - term_id: HP:0000708
    reported_labels:
    - Present in all biallelic cases assessed
    ontology_label: Atypical behavior
  - term_id: HP:0001631
    reported_labels:
    - One patient
    ontology_label: Atrial septal defect
  - term_id: HP:0002558
    reported_labels:
    - One patient
    ontology_label: Supernumerary nipple
  - term_id: HP:0000609
    reported_labels:
    - One patient (sibling case)
    ontology_label: Optic nerve hypoplasia
  - term_id: HP:0000767
    reported_labels:
    - One patient
    ontology_label: Pectus excavatum
  - term_id: NCIT:C15302
    reported_labels:
    - Early intervention / developmental therapies:** physical therapy
    ontology_label: Physical Therapy
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0016575
    ontology_label: obsolete histone deacetylation
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Disability Autosomal Recessive 65
- **MONDO ID:** MONDO:0020850 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Disability Autosomal Recessive 65** covering all of the
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

I'll research this condition using web search and primary literature sources to build a comprehensive report.

Now let me gather a few more details on functional/molecular mechanisms, treatment/management, and the original founding cohort description.

I have sufficient primary and secondary source material now. Let me compile the comprehensive research report.

# Intellectual Disability, Autosomal Recessive 65 (MRT65): Comprehensive Research Report

## 1. Disease Information

**Overview.** Intellectual Developmental Disorder, Autosomal Recessive 65 (MRT65) is a rare Mendelian neurodevelopmental disorder caused by biallelic (homozygous or compound heterozygous) loss-of-function variants in **KDM5B** (lysine demethylase 5B), located on chromosome 1q32.1. It is characterized by moderate-to-severe intellectual disability, global developmental delay, characteristic facial dysmorphism, and camptodactyly, with onset in infancy ([OMIM #618109](https://omim.org/entry/618109); [MalaCards](https://www.malacards.org/card/intellectual_developmental_disorder_autosomal_recessive_65)).

**Key identifiers:**
- **OMIM:** #618109 (phenotype); *605393 (KDM5B gene locus)
- **MONDO:** MONDO:0020850
- **Gene:** KDM5B, HGNC (HGNC:29332), NCBI Gene, chromosome 1q32.1
- **Related Orphanet entries:** KDM5B is listed as causal for "Autosomal recessive non-syndromic intellectual disability" (ORPHA:88616) and as a candidate gene for autosomal dominant non-syndromic intellectual disability (ORPHA:178469) ([Orphanet gene page](https://www.orpha.net/en/disease/gene/KDM5B))
- **Synonyms:** MRT65; Intellectual disability, autosomal recessive 65; KDM5B-related recessive intellectual disability syndrome; KDM5B-associated developmental delay with facial dysmorphism and camptodactyly

**Note on nomenclature confusion (important for curation):** MRT65/KDM5B-biallelic disease is **distinct** from "Alwadei syndrome" (also loosely called MRT61 in some lay sources), which is caused by biallelic **RUSC2** variants on chromosome 9p13.3 (OMIM #617773) and is a separate, phenotypically overlapping but genetically unrelated autosomal recessive ID syndrome ([Wikipedia summary of Alwadei syndrome, citing Alwadei et al. 2016, *Dev Med Child Neurol*](https://en.wikipedia.org/wiki/Alwadei_syndrome)). Some tertiary aggregator pages conflate the two; this should not be repeated in a curated entry.

**Source of information:** Nearly all clinical description derives from **aggregated case-series/cohort publications** (not large-scale EHR data) — a small number of published families/probands (originally 3, now up to ~10–11 published biallelic cases across multiple reports), supplemented by structured databases (OMIM, ClinVar, Orphanet, gnomAD) and model-organism data.

---

## 2. Etiology

### Disease Causal Factors
MRT65 is a **monogenic, purely genetic** disorder — no environmental, infectious, or acquired mechanism is implicated. Disease results from **biallelic loss-of-function (LoF) variants in KDM5B**: nonsense, frameshift, and canonical splice-site variants that are predicted to trigger nonsense-mediated decay or truncate the protein before/within critical catalytic domains, as well as at least one compound-heterozygous case pairing a damaging missense variant (p.Ala635Thr, in the catalytic JmjC domain) with a frameshift null allele ([Martin syndrome case report, PMC8467522](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8467522/)).

### Genetic Risk Factors
- **Causal variants (original cohort, Faundes et al. 2018, *Am J Hum Genet* 102(1):175-187, PMID:[29276005](https://pubmed.ncbi.nlm.nih.gov/29276005/)):**
  - Patient 12: homozygous c.4109T>G, p.(Leu1370Ter)
  - Patient 13: compound heterozygous c.2475-2A>G (splice acceptor) / c.895C>T, p.(Arg299Ter)
  - Patient 14: compound heterozygous c.3906delC, p.(Asn1302LysfsTer45) / c.622dupT, p.(Tyr208LeufsTer5)
- **Additional reported variant** (ClinVar, [RCV001764151](https://www.ncbi.nlm.nih.gov/clinvar/RCV001764151/)): c.3424-2A>G, a splice-acceptor variant
- **Compound heterozygous missense + frameshift** in siblings with agenesis of the corpus callosum: c.1903G>A p.(Ala635Thr) [CADD 28.8, JmjC domain, conserved across KDM5 paralogues] with c.3463del p.(Ser1155AlafsTer4) ([PMC8467522](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8467522/))
- **Statistical evidence of pathogenicity:** Fisher's exact test showed a **96.89-fold enrichment of homozygous protein-truncating variants (PTVs)** in affected cohorts versus gnomAD background (95% CI 3.95–2,378.87; p=0.03); no homozygous KDM5B knockouts were observed among 3,222 adults from a high-consanguinity reference cohort, consistent with strong purifying selection against biallelic LoF ([Faundes et al. 2018](https://pubmed.ncbi.nlm.nih.gov/29276005/)).
- **Cumulative literature:** A 2024 genotype/phenotype study (Chong et al., *Genes* 15(8):1033, PMC11353349) catalogs 2 newly reported plus ~8 previously published biallelic cases (total ~10), all with LoF-type variants (nonsense/frameshift), contrasted against 19 individuals (18 novel) with monoallelic (dominant) KDM5B variants including 8 missense, 3 nonsense, 2 splice-site, 4 frameshift, and 1 whole-gene deletion ([PMC11353349](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11353349/)).
- **Modifier genes:** None established.
- **Consanguinity:** Multiple reported homozygous cases arise in the setting of parental consanguinity or regions of homozygosity, consistent with an autosomal recessive founder-type mechanism in some families (not formally reported as a specific founder allele/population to date).

### Environmental Risk Factors
None identified; this is a Mendelian disorder with no reported environmental/lifestyle contribution to causation.

### Protective Factors
None specifically described for the recessive form. Population data show that **heterozygous (single-allele) LoF carriers are largely unaffected or mildly affected** — heterozygous PTVs are common enough in the population (and in unaffected relatives/controls) to be associated only with subtle cognitive effects (see below), implying the wild-type allele in trans provides substantial functional buffering in carriers.

### Gene-Environment Interactions
Not reported; no GxE data available for this ultra-rare monogenic disorder.

---

## 3. Phenotypes

Below are the principal reported phenotypes, aggregated primarily from Faundes et al. 2018 (original 3 patients), the sibling agenesis-of-corpus-callosum report (PMC8467522), and the 2024 genotype/phenotype cohort (PMC11353349).

| Phenotype | Type | Onset | Frequency (biallelic cohort) | Suggested HPO term |
|---|---|---|---|---|
| Global developmental delay | Sign | Infancy | ~100% (all reported cases) | HP:0001263 |
| Intellectual disability (moderate–severe) | Sign | Recognized in childhood | 100% | HP:0002510 (moderate)/HP:0010864 (severe) |
| Delayed walking (achieved age 2–4 y) | Sign | Infancy/toddler | Most patients | HP:0031936 (Delayed ability to walk) |
| Delayed/limited speech | Sign | Infancy/toddler | Most patients (e.g., "5 words" at age 4 in one case) | HP:0000750 |
| Neonatal/infantile feeding difficulties | Sign | Neonatal | Reported in original 3 patients | HP:0011968 |
| Poor overall growth / mild postnatal growth deficiency | Sign | Infancy | Mild, in a subset | HP:0001510 |
| Dolichocephaly | Physical sign | Congenital | Present in a subset | HP:0000268 |
| Prominent/broad metopic ridge or forehead | Physical sign | Congenital | Common | HP:0000348 / HP:0011220 |
| Square face | Physical sign | — | Some patients | HP:0000321 |
| Dysplastic/low-set ears | Physical sign | Congenital | Some patients | HP:0008551 / HP:0000369 |
| High nasal bridge, bulbous nasal tip, smooth philtrum, thin lips | Physical signs | Congenital | Recurrent facial gestalt across cases | HP:0000426, HP:0000414, HP:0000319, HP:0000219 |
| Camptodactyly (fixed flexion, typically digits 4–5) | Physical sign | Congenital | Present in majority (hallmark feature) | HP:0012385 |
| Joint hypermobility / hand abnormalities | Physical sign | — | ~50% in 2024 cohort | HP:0001382 |
| Behavioral problems (nonspecific) | Behavioral | Childhood | Present in all biallelic cases assessed | HP:0000708 |
| Agenesis/hypoplasia of corpus callosum | Structural brain anomaly | Congenital | Reported in multiple biallelic cases (Patient 12; sibling pair) | HP:0001274 (agenesis) / HP:0002079 (hypoplasia) |
| Camptodactyly with cardiac defects (atrial septal defect) | Sign | Congenital | One patient | HP:0001631 |
| Cryptorchidism, hypospadias | Sign | Congenital | One patient (male) | HP:0000028, HP:0000047 |
| Inguinal hernia / umbilical hernia | Sign | Infancy | Individual patients | HP:0000023 / HP:0001537 |
| Supernumerary nipple | Sign | Congenital | One patient | HP:0002558 |
| Optic nerve hypoplasia | Sign | Congenital | One patient (sibling case) | HP:0000609 |
| Pectus excavatum | Sign | Congenital | One patient | HP:0000767 |

**Notably absent** in the biallelic (recessive) cohort, in contrast to the monoallelic/dominant KDM5B phenotype: **autism spectrum disorder and seizures were not observed** in the 2024 systematic genotype/phenotype study's recessive cases, whereas ASD (53–64%) and sleep disorders (47%) are common in dominant KDM5B disease ([PMC11353349](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11353349/)).

**Progression/severity:** Developmental milestones are markedly delayed but generally achieved (walking and speech onset between 2–4 years in the original cohort); the disorder is considered a static/stable neurodevelopmental disability rather than a progressive neurodegenerative process, though hippocampal/memory-related deficits demonstrated in mouse models raise the possibility of an ongoing (not purely developmental) component to the cognitive phenotype (see Mechanism section).

**Quality of life impact:** Not formally studied with standardized instruments (EQ-5D, SF-36) in this ultra-rare population; qualitatively, affected individuals require lifelong support for intellectual disability, communication impairment, and (in a subset) structural brain and congenital anomalies requiring surgical/medical management.

---

## 4. Genetic/Molecular Information

**Causal gene:** KDM5B (also known as JARID1B, PLU1, RBBP2H1A, CT31), OMIM *605393, chromosome 1q32.1.

**Gene product/domain architecture:** KDM5B contains **7 annotated domains**: JmjN domain, catalytic JmjC domain, ARID (DNA-binding) domain, C5HC2 zinc finger, and three PHD (plant homeodomain) fingers (PHD1–3) ([*Sci Rep* 2019, molecular architecture paper](https://www.nature.com/articles/s41598-019-40573-y); [*Functions and Interactions of Mammalian KDM5 Demethylases*, PMC9309374](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9309374/)).

**Molecular function:** KDM5B is an **Fe(II)/2-oxoglutarate-dependent JmjC-domain histone demethylase** that removes methyl groups from **trimethylated, dimethylated, and monomethylated lysine 4 of histone H3 (H3K4me3/me2/me1)** — a promoter-proximal mark generally associated with transcriptional activation. Catalysis proceeds via decarboxylation of 2-oxoglutarate to succinate + CO₂ coupled to hydroxylation of the methylated lysine, yielding an unstable hemiaminal that spontaneously decomposes to release formaldehyde and demethylated lysine. KDM5B additionally regulates RNA polymerase II initiation/elongation rates and alternative splicing.

**Variant classification (ACMG/AMP) in the recessive disease:** Reported biallelic variants are predominantly classified pathogenic/likely pathogenic loss-of-function alleles:
- Nonsense: p.(Leu1370Ter), p.(Arg299Ter)
- Frameshift: p.(Asn1302LysfsTer45), p.(Tyr208LeufsTer5), p.(Ser1155AlafsTer4)
- Canonical splice-site: c.2475-2A>G, c.3424-2A>G ([ClinVar RCV000678688](https://www.ncbi.nlm.nih.gov/clinvar/RCV000678688/), [RCV001764151](https://www.ncbi.nlm.nih.gov/clinvar/RCV001764151/))
- One missense (p.Ala635Thr, JmjC domain, CADD 28.8) reported in trans with a frameshift null, in a family with corpus callosum agenesis; classified as likely pathogenic on the basis of conservation, domain location, and segregation ([PMC8467522](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8467522/))

**Population allele frequency (gnomAD):** The pathogenic missense variant (p.Ala635Thr) was observed in a single gnomAD heterozygote; the frameshift null was absent from gnomAD, consistent with strong selection against biallelic loss-of-function. No homozygous KDM5B PTV carriers were found among 3,222 highly consanguineous individuals in reference data. KDM5B shows strong constraint against loss-of-function in gnomAD generally (specific pLI/LOEUF values were not independently verifiable via the sources retrieved in this session and should be confirmed directly against the gnomAD browser before curation).

**Somatic vs. germline:** All reported disease-causing variants are **germline**; KDM5B is separately studied as a somatically amplified oncogene in some cancers (breast, prostate), but that is a distinct biological context from the germline recessive ID disorder.

**Functional consequences:** Loss-of-function variants are predicted/demonstrated to cause **haploinsufficiency-on-a-null-background** — i.e., the recessive disease requires near-complete loss of KDM5B demethylase activity from both alleles, since heterozygous LoF carriers are generally unaffected or only mildly affected (see Section 2). This is mechanistically consistent with the semi-dominant/dosage-sensitive biology of KDM5 family demethylases.

**Modifier genes:** None established.

**Epigenetic information:** KDM5B is itself a chromatin-modifying enzyme; its loss is predicted to cause **genome-wide dysregulation of the H3K4me3 landscape**, particularly at promoters of activity-dependent and developmentally regulated genes (directly demonstrated in mouse hippocampal models — see Mechanism section). No human DNA methylation/EWAS "episignature" for MRT65 was identified in the sources reviewed in this session.

**Chromosomal abnormalities:** No microdeletion/microduplication syndrome mechanism is described for MRT65; disease arises from intragenic sequence variants, not copy-number rearrangement (in contrast to some dominant KDM5B cases, one of which involved a whole-gene deletion).

**Suggested ontology bindings:**
- Gene: hgnc:29332 (KDM5B)
- GO Molecular Function: GO:0032454 (histone H3-K9 demethylase activity — not correct; correct term is GO:0032453, "histone H3K4 demethylase activity, trimethyl-H3K4-specific") — **verify exact GO ID against OAK/AmiGO before binding**
- GO Biological Process: GO:0016575 (histone deacetylation — not applicable); more precisely, "negative regulation of gene expression, epigenetic" GO:0045814, or "histone H3-K4 demethylation" (verify exact CURIE)

---

## 5. Environmental Information

No environmental factors, lifestyle exposures, or infectious agents are implicated in causation of MRT65. This is a purely monogenic Mendelian disorder.

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered, from molecular lesion to clinical phenotype)

1. **Biallelic KDM5B loss-of-function or damaging missense variant** (nonsense, frameshift, canonical splice-site, or a JmjC-domain missense in trans with a null allele) **leads to** near-complete loss of functional KDM5B protein or catalytic activity in the affected individual (demonstrated statistically by enrichment of homozygous PTVs over population background; PMID:29276005).
2. **Loss of KDM5B H3K4 demethylase activity leads to** failure to remove trimethyl/dimethyl/monomethyl marks from histone H3 lysine 4 at target gene promoters, **resulting in** genome-wide dysregulation of the H3K4me3 chromatin landscape — this step is demonstrated directly in a demethylase-dead mouse model (Kdm5bΔARID/ΔARID), which shows **abnormal baseline H3K4me3 accumulation** in hippocampal neurons (PMID:38575342/PMC11079963). *This mouse-model step is inferred to translate to human neurons; it has not been directly demonstrated in human tissue.*
3. **Dysregulated H3K4me3 leads to** abnormal baseline transcription of activity-dependent immediate-early genes (Egr1, Npas4, cFos are downregulated at baseline) **and**, upon a learning/activity stimulus, **hyperactivated and pathologically prolonged transcription** of the same genes (persisting ~3 hours vs. transient in controls) — a bidirectional dysregulation of neuronal activity-dependent gene programs (model-organism evidence, PMC11079963).
4. **Dysregulated activity-dependent transcription leads to** impaired postsynaptic long-term potentiation (LTP) stability in hippocampal CA1 neurons following theta-burst stimulation, with intact presynaptic release and short-term plasticity — i.e., a **selective postsynaptic synaptic-plasticity defect** (model-organism evidence).
5. **Impaired synaptic plasticity leads to** deficits in long-term (but not short-term) spatial memory consolidation, demonstrated behaviorally in Morris water maze and object-location memory tasks in mice, while short-term memory and cognitive flexibility are preserved (model-organism evidence).
6. **In humans, this cascade is inferred (by analogy/extrapolation from the mouse mechanistic data, not directly demonstrated) to manifest as** global developmental delay and moderate-to-severe intellectual disability, with a possible ongoing (not purely developmental) memory-consolidation component — raising the hypothesis that some cognitive deficits could remain modifiable in postnatal/adult life, a claim explicitly framed as therapeutically speculative by the authors (PMC11079963).
7. **In parallel, independent of the neuronal/synaptic branch**, KDM5B's broader role in **regulating cell differentiation, developmental gene expression programs, and (in mouse knockouts) cranial neural crest/skeletal and craniofacial development leads to** the syndromic congenital anomalies seen in humans — camptodactyly, characteristic facial dysmorphism (broad forehead/metopic prominence, high nasal bridge, bulbous nasal tip, thin lips), and in a subset, structural brain malformation (corpus callosum agenesis/hypoplasia) and other congenital anomalies (cardiac septal defects, genitourinary anomalies, hernias). This branch is supported by **Kdm5b-null mouse phenotypes**: disorganized cranial nerves, eye developmental defects, exencephaly, and skeletal anomalies, with most homozygous-null pups dying within the first postnatal day (perinatal lethality), and surviving pups showing developmental defects into adulthood (PMID:29276005; MGI:1922855).
8. **A distinct, dosage-dependent branch**: heterozygous (monoallelic) KDM5B protein-truncating variants, insufficient to cause the full recessive syndrome, **are nonetheless associated with** measurably reduced educational attainment, slower reaction time, and worse verbal-numerical reasoning at the population level, and are enriched among individuals with ADHD in two independent large case-control sequencing studies — indicating a **dose-dependent (semi-dominant) relationship between KDM5B function and cognitive/behavioral phenotype severity**, from mild population-level cognitive effects (heterozygous LoF) through syndromic dominant disease (heterozygous disruptive or missense variants with more severe/penetrant effects, including ASD and renal/dermatologic anomalies) to the fully penetrant recessive syndrome described here (biallelic LoF) (PMC10260403; PMC11353349; medRxiv 2025.01.14.25320294; *Nat Commun* 2024, 10.1038/s41467-024-50247-7).

### Molecular pathways
Histone H3K4 methylation/demethylation cycle (writers: SET1/MLL family KMTs; erasers: KDM5 family, including KDM5A/B/C/D); RNA Pol II transcriptional initiation/elongation regulation; alternative splicing regulation.

### Cellular processes
Neuronal activity-dependent transcription (immediate-early gene induction), synaptic plasticity (LTP), neural differentiation, cranial neural crest-derived craniofacial/skeletal development.

### Protein dysfunction
Loss of catalytic JmjC-domain demethylase activity (nonsense/frameshift → truncated/degraded protein via NMD; missense in JmjC domain → predicted catalytic impairment).

### Cell types and biological processes implicated (suggested ontology terms)
- Cell types: hippocampal pyramidal neuron (CL:0002614 or more specific CA1 pyramidal neuron term), cranial neural crest cell (CL:0000333)
- GO Biological Process candidates: "histone H3-K4 demethylation," "regulation of synaptic plasticity" (GO:0048167), "positive regulation of transcription by RNA polymerase II" (GO:0045944), "long-term memory" (GO:0007616), "neural crest cell development" (GO:0014032) — **all CURIEs should be verified against OAK before binding.**

### Single-cell / omics data
No human single-cell, spatial transcriptomic, or multi-omic dataset specific to MRT65 patient tissue was identified in this session's searches. The relevant "omics" evidence base is exclusively **mouse hippocampal transcriptomic (RNA-seq of immediate-early and late-response genes) and ChIP-based H3K4me3 profiling** from the 2024 *J Neurosci* study (PMC11079963), plus a related 2024/2025 preprint on autism-like phenotypes and increased NMDAR2D expression in KDM5B-deficient mice (*Sci Adv*, PMC13189110) describing altered glutamatergic signaling gene expression.

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: **central nervous system** (intellectual disability, developmental delay; structural anomaly — corpus callosum agenesis/hypoplasia, absent interthalamic adhesion, hypoplastic anterior commissure in severe cases; optic nerve hypoplasia)
- Secondary: musculoskeletal system (camptodactyly, joint hypermobility), craniofacial skeleton (dolichocephaly, metopic prominence, facial dysmorphism), cardiovascular system (atrial septal defect in one patient), genitourinary system (cryptorchidism, hypospadias in one patient), abdominal wall (inguinal/umbilical hernia)
- Body systems: nervous, skeletal, craniofacial, cardiovascular (occasional), genitourinary (occasional)

**Tissue/cell level:** Neurons (particularly hippocampal), cranial neural crest-derived mesenchyme/craniofacial tissue, developing corpus callosum axonal tracts (with Probst bundle formation in complete agenesis — anomalous longitudinally-oriented axon bundles that fail to cross the midline).

**Subcellular level:** Nucleus (chromatin/nucleosome — GO Cellular Component: "nucleus" GO:0005634; more specifically chromatin, GO:0000785), consistent with KDM5B's role as a chromatin-modifying nuclear enzyme.

**Localization/UBERON suggestions:** brain (UBERON:0000955), corpus callosum (UBERON:0002336), hippocampus (UBERON:0002421), hand digit / phalanx (for camptodactyly — UBERON:0002389 or more specific digit terms), face (UBERON:0001456).

**Lateralization:** Not reported as asymmetric; anomalies (corpus callosum agenesis, camptodactyly) are typically bilateral/midline.

---

## 8. Temporal Development

- **Onset:** Congenital/infantile — feeding difficulties and dysmorphic features present from birth or early infancy; developmental delay recognized in infancy.
- **Onset pattern:** Insidious/developmental rather than acute.
- **Progression:** The intellectual disability and developmental delay are generally considered a **static (non-progressive) neurodevelopmental disability** once diagnosed, though affected individuals continue to acquire skills at a delayed rate (walking and first words achieved between ages 2–4 years in the original cohort). No degenerative course has been reported.
- **Disease course pattern:** Stable/lifelong; no remission.
- **Critical periods:** Mouse mechanistic data suggest KDM5B has functions in **both prenatal neurodevelopment and ongoing adult synaptic plasticity/memory consolidation** (demonstrated via adult hippocampal knockdown reproducing memory deficits) — raising the hypothesis of a postnatal "window of continued relevance" for gene function, distinct from a purely prenatal critical period, though this remains an extrapolation from animal data with unproven human therapeutic implications (PMC11079963).

---

## 9. Inheritance and Population

**Epidemiology:** MRT65 is an **ultra-rare disorder**. As of the original description, only 3 unrelated patients (all boys) had been reported (Faundes et al. 2018); by the 2024 genotype/phenotype study, roughly 10 biallelic cases total were catalogued in the literature ([PMC11353349](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11353349/)). No formal population prevalence or incidence estimate exists; this would be classified `prevalence_class: NOT_YET_DOCUMENTED` or an ultra-rare qualitative tier per dismech convention, sourced to `measure_type: CASES_IN_LITERATURE`.

**Inheritance pattern:** Autosomal recessive (biallelic KDM5B variants — homozygous or compound heterozygous).

**Penetrance:** Appears fully penetrant for the biallelic LoF genotype based on reported cases, though ascertainment bias in an ultra-rare, case-report-driven literature cannot be excluded.

**Expressivity:** Variable — e.g., presence/absence of craniofacial dysmorphism, corpus callosum anomalies, cardiac/genitourinary anomalies differ among the reported patients despite shared biallelic LoF mechanism (Patient 13 notably lacked craniofacial dysmorphism).

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported for KDM5B.

**Founder effects:** Not established; however, several published families are consanguineous, consistent with the general expectation for an ultra-rare autosomal recessive disorder.

**Consanguinity role:** Multiple reported homozygous cases arose from consanguineous unions; the population-genetics analysis in Faundes et al. specifically leveraged **highly consanguineous reference cohorts** (3,222 individuals) to show absence of homozygous PTV carriers as pathogenicity evidence.

**Carrier frequency:** Not established for MRT65 specifically; heterozygous KDM5B PTVs are present in the general population at a frequency sufficient to be studied for population-level cognitive/ADHD associations (i.e., not vanishingly rare), consistent with a modest carrier frequency, though a precise number was not identified in this session's sources — **verify via gnomAD before curation.**

**Population demographics:** All three original patients were male (boys), though this is very likely an ascertainment artifact from a small case series rather than a true sex-linked susceptibility, since the gene is autosomal. No specific ethnic/geographic enrichment has been reported; cases described in the literature originate from genetically heterogeneous ascertainment (Deciphering Developmental Disorders (DDD)-type cohorts and clinical case reports internationally).

**Sex ratio:** Not formally established (small sample skewed male in original description; not confirmed as a true biological sex bias).

---

## 10. Diagnostics

**Genetic testing (primary diagnostic modality):**
- **Whole exome sequencing (WES)** or **whole genome sequencing (WGS)** — the diagnostic method by which essentially all reported cases were identified (via trio-based DDD-type cohorts or diagnostic clinical WES), given the ultra-rare and clinically non-specific nature of the phenotype.
- **Gene panel testing** for intellectual disability/developmental delay panels that include KDM5B (e.g., Genomics England PanelApp Intellectual Disability panel, green/confidence level 10 — well-established gene-disease association) ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/285/gene/KDM5B/)).
- **Single-gene KDM5B sequencing** reasonable only when phenotype (camptodactyly + facial gestalt + developmental delay) is strongly suggestive, given the rarity.
- **Chromosomal microarray** — not the primary diagnostic tool for this sequence-variant-driven disorder (as opposed to dominant cases with a reported whole-gene deletion), but useful to exclude CNV-based differentials.
- **RNA/splicing studies:** Used in at least one report to functionally validate splice-site variants ("Novel KDM5B splice variants identified in patients with developmental disorders: Functional consequences," ScienceDirect/ResearchGate) — demonstrating aberrant transcript products from canonical splice-site variants.

**Clinical/imaging tests:**
- **Brain MRI** — recommended given the reported association with corpus callosum agenesis/hypoplasia, absent interthalamic adhesion, hypoplastic anterior commissure, and optic nerve hypoplasia in a subset of patients; prenatal fetal MRI has also identified partial corpus callosum agenesis (splenium absence) at 22 weeks gestation in one case.
- **Cardiac echocardiogram** — indicated given a reported atrial septal defect.
- **Skeletal/hand examination** — camptodactyly assessment.
- **Developmental/cognitive assessment** — standardized developmental and IQ testing to characterize the moderate-to-severe intellectual disability.

**Differential diagnosis:** Other genetic causes of syndromic intellectual disability with camptodactyly and/or corpus callosum anomalies, including but not limited to other chromatin-modifier-related neurodevelopmental disorders (KMT2D/Kabuki syndrome spectrum, other KDM5-family disorders — KDM5A, KDM5C [X-linked, Claes-Jensen syndrome], KDM5D), and **RUSC2-related Alwadei syndrome** (biallelic, overlapping ID + facial dysmorphism + occasional corpus callosum hypoplasia phenotype, OMIM #617773) — this is a genuine differential to flag given surface-level phenotypic overlap and nomenclature confusion in secondary sources.

**Screening:** No population or newborn screening program exists for this ultra-rare disorder; diagnosis is reactive, prompted by clinical developmental delay/dysmorphism evaluation.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No mortality directly attributable to MRT65 itself has been reported in surviving liveborn patients (oldest reported patient in the 2024 cohort was 28 years old); one reported pregnancy was electively terminated at 24 weeks for severe prenatal brain malformation (partial corpus callosum agenesis), reflecting reproductive-decision outcomes rather than a mortality statistic of the postnatal disease.
- **Morbidity/function:** Lifelong moderate-to-severe intellectual disability with need for ongoing developmental, educational, and adaptive support; camptodactyly may require orthopedic/hand-therapy management; structural brain anomalies (when present) correlate with more severe neurological phenotype.
- **Complications:** Congenital anomalies in a subset (cardiac septal defect, cryptorchidism/hypospadias, hernias) may require surgical correction.
- **Recovery potential:** No cure; supportive management only. The mouse memory-consolidation data (PMC11079963) raise a **speculative, not yet clinically validated**, hypothesis that some adult cognitive deficits could theoretically remain responsive to intervention beyond the developmental period — this should be flagged in any curated entry as a `HUMAN_MODEL_MISMATCH`-type caveat rather than an established human therapeutic avenue.
- **Prognostic factors:** Presence/severity of structural brain anomaly (corpus callosum agenesis) appears to correlate with greater phenotypic severity in the small reported series, though this is not statistically established given sample size.

---

## 12. Treatment

**No disease-specific or targeted pharmacotherapy exists.** Management is entirely **supportive and symptom-directed**:

- **Supportive care / multidisciplinary developmental management:** NCIT:C15747 (Supportive Care)
- **Early intervention / developmental therapies:** physical therapy (NCIT:C15302), occupational therapy (NCIT:C121351), speech therapy (NCIT:C159273) — addressing motor delay, camptodactyly-related hand function, and speech/communication delay
- **Special education / behavioral support** for intellectual disability and behavioral problems
- **Orthopedic surgical procedure** (NCIT:C16186) — potential management of camptodactyly if functionally limiting
- **Cardiac surgical correction** — for structural cardiac anomalies (atrial septal defect) if hemodynamically significant, NCIT:C15329 (Surgical Procedure)
- **Genetic counseling** (NCIT:C15240) — essential given autosomal recessive inheritance and 25% recurrence risk for future pregnancies of carrier parents; prenatal diagnosis is feasible once the familial variants are known (as demonstrated by the prenatal case detected via fetal MRI/genetic testing).

**Experimental/clinical trials:** No KDM5B/MRT65-specific clinical trials were identified in ClinicalTrials.gov searches performed in this session; none should be assumed to exist without direct verification.

**Genotype-guided considerations:** None currently established; the disorder is too rare for stratified precision-medicine approaches to have been developed.

---

## 13. Prevention

- **Primary prevention:** Not applicable (no modifiable risk factor); **genetic counseling** for known carrier couples (e.g., after an affected child) regarding 25% recurrence risk in future pregnancies.
- **Secondary prevention:** **Prenatal diagnosis** via chorionic villus sampling/amniocentesis for known familial variants once identified in a proband, as illustrated by the prenatal detection case (partial corpus callosum agenesis on fetal MRI, followed by molecular confirmation) (PMC8467522). **Preimplantation genetic diagnosis (PGD)** is a theoretical option for known carrier couples, though not specifically documented as used in the literature reviewed.
- **Tertiary prevention:** Early developmental intervention services to optimize functional outcomes once diagnosed.
- **Population/genetic screening:** No population carrier-screening panel currently includes KDM5B as a routine component (it is not among common expanded-carrier-screening panel genes at this time), consistent with its very recent (2018) disease-gene establishment and ultra-rare status.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary/companion-animal disease caused by biallelic KDM5B loss-of-function has been reported in the sources reviewed (no OMIA entry identified). KDM5B orthologs are broadly conserved (mouse Kdm5b, MGI:1922855; Drosophila kdm5/lid; and other KDM5-family members across vertebrates), but disease association is currently a human/laboratory-model finding rather than a recognized natural veterinary disease.

---

## 15. Model Organisms

**Mouse models (primary model system used):**
- **Constitutive Kdm5b knockout mice (MGI:1922855):** Homozygous knockout causes **postnatal lethality in the majority of pups**, most dying within the first 24 hours of life; surviving pups develop normally into adulthood but show increased incidence of **exencephaly, eye developmental defects, disorganized cranial nerves, and skeletal anomalies** — recapitulating several structural/congenital features of the human syndrome, but with far greater lethality than seen in humans, indicating the mouse null is **not a fully faithful model of viable human biallelic loss** (relevant for a `FAILS_TO_RECAPITULATE`/`PARTIALLY_RECAPITULATES` model-link annotation, `fidelity: LOW–MODERATE`, with a `SPECIES_MISMATCH` or `BOUNDARY_OMISSION` divergence given the survival discrepancy) (PMID:29276005; MGI:1922855).
- **Kdm5bΔARID/ΔARID mice** (demethylase-catalytically-dead, but not full protein-null): viable, adult-survivable model used to study **postnatal/adult hippocampal function** — hyperactivity, long-term (but not short-term) spatial memory deficits, impaired hippocampal LTP, and dysregulated activity-dependent immediate-early gene transcription (PMID:38575342/PMC11079963). This model **partially recapitulates** the human cognitive phenotype at the behavioral/circuit level (`RECAPITULATES` for memory/behavioral readouts) but does **not** model the congenital/dysmorphic features of the human syndrome, since it preserves partial protein structure and is not a full LoF-null.
- **Adult hippocampal shRNA knockdown (CA1-targeted, wild-type mice):** Demonstrates that **postnatal/adult-only** knockdown is sufficient to cause spontaneous seizures, hyperactivity, and hippocampus-dependent long-term memory/LTP deficits — showing the phenotype is not exclusively attributable to developmental loss, supporting a model where **ongoing adult gene function is separately required** (PMC11079963).
- **Mouse model of autism-like phenotypes:** A 2024–2025 study (*Science Advances*, PMC13189110) reports KDM5B-deficient mice show **autism-like behavioral phenotypes and increased NMDAR2D (Grin2d) expression**, suggesting altered glutamatergic signaling as an additional mechanistic branch — this maps more directly to the **dominant/monoallelic** human KDM5B-ASD phenotype than to the biallelic MRT65 phenotype (which notably lacks ASD in the 2024 clinical cohort), and should be flagged as a **model-to-phenotype scale/relevance mismatch** if used to support the recessive MRT65 entry specifically.

**Invertebrate models:** *Drosophila* KDM5 (fly ortholog, "lid") knockdown/mutant studies demonstrate roles in **synaptic structure and function at the neuromuscular junction**, **larval growth**, and **chromatin insulator activity in the brain** — supporting deep evolutionary conservation of KDM5's neurodevelopmental role, but these are invertebrate systems with substantial biological distance from the human CNS phenotype (`fidelity: LOW`, useful mechanistically but not for direct phenotype recapitulation claims).

**Model limitations (general):** No existing animal model — including the closest available (Kdm5bΔARID/ΔARID) — reproduces the full human MRT65 syndromic phenotype (camptodactyly, characteristic facial dysmorphism, corpus callosum agenesis) together with viable adult survival; the constitutive null best matches structural/congenital features but is embryonic/perinatal lethal in the majority of animals, while the catalytically-dead ARID model best matches the cognitive/memory phenotype but lacks the structural and craniofacial anomalies. This split strongly suggests the human syndrome as a whole has never been fully modeled in one animal system to date, an appropriate `HUMAN_MODEL_MISMATCH` discussion point for curation.

---

## Summary of Key Primary Citations

| PMID/Source | Citation | Contribution |
|---|---|---|
| [29276005](https://pubmed.ncbi.nlm.nih.gov/29276005/) | Faundes V, et al. *Am J Hum Genet.* 2018 Jan 4;102(1):175-187. | Original description establishing biallelic KDM5B LoF as cause of recessive ID syndrome (3 patients); population-genetics pathogenicity evidence; mouse KO phenotype summary |
| PMC8467522 | Case report, compound het missense/frameshift KDM5B, sibling pair | Corpus callosum agenesis phenotype, prenatal detection, expands allelic spectrum |
| PMC11353349 (Chong et al.) | *Genes* 2024;15(8):1033 | Genotype/phenotype study contrasting biallelic vs. monoallelic KDM5B disease; ~10 biallelic cases catalogued |
| 35905858 | Harrington et al. review, *Biochim Biophys Acta Gene Regul Expr.* 2022 | Comprehensive review of pathogenic KDM5B variant spectrum, recessive vs dominant |
| 38575342 / PMC11079963 | *J Neurosci.* 2024;44(19):e1544232024 | Mouse mechanistic model: hippocampal H3K4me3 dysregulation, memory consolidation deficits |
| PMC13189110 (*Sci Adv*) | Autism-like phenotypes/NMDAR2D in KDM5B-deficient mice | Mechanistic link to glutamatergic signaling (relevant mainly to dominant/ASD phenotype) |
| PMC10260403 | Rare protein-coding variation and adult cognitive function | Population-level heterozygous KDM5B PTV effect on cognition |
| OMIM #618109 | Clinical synopsis, MRT65 | Curated phenotype/gene summary |

---

**Curation caveats to flag explicitly:** (1) The disorder is defined by an extremely small published case count (~10 biallelic patients across all literature to date) — treat prevalence as `CASES_IN_LITERATURE`/undocumented, not a population rate. (2) Distinguish this recessive entry sharply from dominant/monoallelic KDM5B disease and from RUSC2-related Alwadei syndrome, both of which are conflated in some secondary/tertiary web sources. (3) Mouse mechanistic data (hippocampal memory consolidation, autism-like NMDAR2D findings) come from models that do not fully recapitulate the human biallelic-null phenotype and should be evidence-graded `MODEL_ORGANISM` with explicit `HUMAN_MODEL_MISMATCH`/divergence annotations rather than treated as directly confirmed human mechanism. (4) Several ontology CURIEs suggested above (GO terms in particular) are provisional and must be verified against OAK/live ontology lookup before binding, per this repository's term-validation policy.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 59 |
| Resolved | 54 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 23 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001263` (1 mention) - the report calls it "~100% (all reported cases)"; HP calls it **Global developmental delay**
- `HP:0000750` (1 mention) - the report calls it "Most patients (e.g., "5 words" at age 4 in one case)"; HP calls it **Delayed speech and language development**
- `HP:0001510` (1 mention) - the report calls it "Mild, in a subset"; HP calls it **Growth delay**
- `HP:0000268` (1 mention) - the report calls it "Present in a subset"; HP calls it **Dolichocephaly**
- `HP:0012385` (1 mention) - the report calls it "Present in majority (hallmark feature)"; HP calls it **Camptodactyly**
- `HP:0001382` (1 mention) - the report calls it "~50% in 2024 cohort"; HP calls it **Joint hypermobility**
- `HP:0000708` (1 mention) - the report calls it "Present in all biallelic cases assessed"; HP calls it **Atypical behavior**
- `HP:0001631` (1 mention) - the report calls it "One patient"; HP calls it **Atrial septal defect**
- `HP:0002558` (1 mention) - the report calls it "One patient"; HP calls it **Supernumerary nipple**
- `HP:0000609` (1 mention) - the report calls it "One patient (sibling case)"; HP calls it **Optic nerve hypoplasia**
- `HP:0000767` (1 mention) - the report calls it "One patient"; HP calls it **Pectus excavatum**
- `NCIT:C15302` (1 mention) - the report calls it "Early intervention / developmental therapies:** physical therapy"; NCIT calls it **Physical Therapy**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016575` (obsolete histone deacetylation) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000321` (1 mention) - the report calls it "Some patients"; HP calls it **Square face**, and lists "Square facies" among its other names
- `GO:0016575` (1 mention) - the report calls it "histone deacetylation — not applicable"; GO calls it **obsolete histone deacetylation**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.