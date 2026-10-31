---
provider: claude_code
model: claude-opus-5-5
cached: false
start_time: '2026-10-23T17:35:31.707154'
end_time: '2026-10-23T17:39:03.907495'
duration_seconds: 212.2
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Pure Autonomic Failure
  mondo_id: MONDO:0018608
  category: Complex
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Bradbury Eggleston syndrome; Bradbury-Eggleston syndrome; PAF; Pure dysautonomia;
    Pure idiopatic dysautonomia; idiopathic orthostatic hypotension
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
  - claude-opus-5-5
  num_turns: 21
  total_cost_usd: 2.629656
  session_id: 84c1f18c-70de-4ca2-8eb1-134345f54917
  stop_reason: end_turn
  permission_denials: 6
  denied_tools:
  - Bash
  - Write
  assistant_text_blocks: 4
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: claude_code
  succeeded: true
reference_validation:
  total_references: 59
  verified: 59
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 13
  quotes_valid: 13
  relevance_assessed: 59
  on_topic: 52
  validator_version: 0.3.0
term_validation:
  total_terms: 43
  verified: 42
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 3
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0012378
    reported_labels:
    - Fatigue, weakness, lethargy
    ontology_label: Fatigue
  - term_id: HP:0000017
    reported_labels:
    - Nocturia / nocturnal pressure natriuresis
    ontology_label: Nocturia
  - term_id: HP:0001662
    reported_labels:
    - Bradycardia / slow steady heart rate
    ontology_label: Bradycardia
  - term_id: HP:0012099
    reported_labels:
    - parent term
    ontology_label: Abnormal circulating catecholamine concentration
  - term_id: HP:0001903
    reported_labels:
    - Anemia (normocytic, low erythropoietin)
    ontology_label: Anemia
  - term_id: UBERON:0000948
    reported_labels:
    - cardiac denervation
    ontology_label: heart
  - term_id: UBERON:0002113
    reported_labels:
    - renal cortex
    ontology_label: kidney
  labels_variant: 7
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pure Autonomic Failure
- **MONDO ID:** MONDO:0018608 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Bradbury Eggleston syndrome; Bradbury-Eggleston syndrome; PAF; Pure dysautonomia; Pure idiopatic dysautonomia; idiopathic orthostatic hypotension
- **Category:** Complex

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Pure Autonomic Failure** covering all of the
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

I'm pulling the abstracts out of the PAF references already cached in this worktree. I'll use them as the evidence base for the report.

Reading the treatment and symptom abstracts now.

I've confirmed the ontology terms against the local caches. Doing one more gene-ID lookup, then writing the report.

# Pure Autonomic Failure (PAF): Research Report

**MONDO:0018608** · ORPHA:441 · MeSH D054970 · ICD-11 8D84 · ICD-10 G90.8 (Orphanet maps this as "Narrower") · UMLS C0393911 · GARD 10428
*Report prepared 2026-10-23. Evidence comes from the abstracts and full texts already cached for this entry in `references_cache/`. Ontology CURIEs were checked against the repository's term caches (`cache/*/terms.csv`); terms that were not in the cache are marked "lookup needed".*

---

## 1. Disease information

### Overview
Pure autonomic failure (PAF) is a rare, sporadic, adult-onset neurodegenerative disease of the peripheral autonomic nervous system. It is classed as an α-synucleinopathy. Its defining feature is chronic **neurogenic orthostatic hypotension (nOH)** with no identified secondary cause and no motor or cognitive signs of central neurodegeneration.

**PAF has no causal gene, and no OMIM entry is recorded.** It is not a Mendelian disease. Orphanet records its inheritance as "Not applicable". Its molecular substrate is aggregated α-synuclein, the protein encoded by *SNCA* (hgnc:11138). That makes SNCA the disease protein, not a germline causal gene, and this report found no source naming a PAF-specific variant.

- Orphanet definition: "A rare sporadic neurodegenerative disease characterized by slowly progressive symptoms of orthostatic hypotension (OH), and other symptoms of generalised dysautonomia related to the impairment of the sympathetic component of the autonomic nervous system." (ORPHA:441)
- "Pure autonomic failure (PAF) is a rare sporadic neurodegenerative autonomic disorder characterized by slowly progressive pan autonomic failure without other features of neurologic dysfunctions." (PMID:27338613, 2016 review)
- Historical description: "A 1925 report by Bradbury and Eggleston first described patients with extreme orthostatic hypotension and a low, steady heart rate." (PMID:24095130)

### Synonyms
Bradbury-Eggleston syndrome, idiopathic orthostatic hypotension, PAF, pure dysautonomia, and "pure idiopatic dysautonomia" (Orphanet's own spelling). Older literature also uses "asympathicotonic orthostatic hypotension" (PMID:34669076).

### Nature of the data
Nearly all of the evidence is aggregated at the disease level: multicentre cohorts, single-centre retrospective series, autopsy case reports, and consensus statements. There are no EHR-derived phenotype profiles.

### A conceptual caveat
PAF is diagnosed clinically, and autopsy and neurochemical data show that the clinical label covers two separate conditions (PMID:34669076, Goldstein 2021):
> "This approach lumps together two nOH syndromes that are pathologically and neurochemically distinct. One is characterized by intraneuronal cytoplasmic alpha-synuclein aggregates (i.e., Lewy bodies) and degeneration of postganglionic sympathetic neurons, as in PD and DLB; the other is not, as in MSA."

One autopsied clinically diagnosed PAF case had **no** synuclein pathology anywhere (PMID:28188385):
> "In pure autonomic failure, sympathetic noradrenergic denervation can occur without concurrent Lewy bodies or alpha-synuclein deposition in the brain or sympathetic ganglion tissue."

---

## 2. Etiology

| Factor | Evidence |
|---|---|
| **Primary cause** | Idiopathic neurodegeneration with misfolded α-synuclein deposited mainly in peripheral autonomic neurons. "PAF is a peripheral autonomic neurodegenerative disease caused by alpha-synuclein deposition that is predominantly confined to peripheral autonomic neurons." (PMID:34392300) |
| **Genetic risk** | No causal genes, susceptibility loci, or GWAS signals specific to PAF were found in the cached literature. Orphanet: inheritance "Not applicable". |
| **Environmental risk** | None established. This report found no toxin, occupational, or infectious exposure linked to PAF. |
| **Demographics** | Age is the main correlate: onset is in adulthood or old age. Men predominate in pooled data (63.8% male; PMID:42081229), although one small Stanford series was 63% female (PMID:27757562). |
| **Protective factors** | None documented. |
| **Gene–environment interaction** | No data. |

The prion-like spreading model is the leading mechanistic hypothesis for the whole synucleinopathy family. It is cited as background in PMID:28093795: "α-Syn spreads from cell-to-cell in a 'prion-like fashion.'" No PAF-specific trigger has been identified.

---

## 3. Phenotypes

Onset is in adulthood. The course is chronic and slowly progressive, and repeat testing shows worsening autonomic failure over time (PMID:40397689).

| Phenotype | HPO (cache-verified) | Frequency / data | Source |
|---|---|---|---|
| Orthostatic hypotension (neurogenic, severe) | HP:0001278 | Defining; Orphanet: very frequent (99–80%). Neurogenic OH: SBP fall −44 ± 25 mmHg with HR rise of only 8 ± 8 bpm (synucleinopathy cohort) | ORPHA:441; PMID:29405350 |
| Syncope | HP:0001279 | 91% of PAF patients | PMID:10552235 |
| Dizziness / light-headedness | lookup needed | 84% | PMID:10552235 |
| Visual disturbance on standing | HP:0000505 (Visual impairment; may be too coarse) | 75% | PMID:10552235 |
| "Coat-hanger" suboccipital/paracervical neck pain | HP:0030833 Neck pain | 81% | PMID:10552235 |
| Chest pain (orthostatic) | HP:0100749 | 44% (versus 13% in MSA) | PMID:10552235 |
| Fatigue, weakness, lethargy | HP:0012378 | 91% | PMID:10552235 |
| Supine hypertension | lookup needed | "at least half"; "affects most patients" | PMID:11927799; PMID:26644241; PMID:36601916 |
| Nocturia / nocturnal pressure natriuresis | HP:0000017 | Mechanistically linked to supine hypertension | PMID:11927799; PMID:36601916 |
| Postprandial hypotension | lookup needed | Supine BP falls after a meal in PAF but not in controls | PMID:8492945 |
| Anhidrosis / hypohidrosis | HP:0000970 / HP:0000966 | Orphanet: very frequent. Median 51% body-surface anhidrosis (IQR 3–93%) in stable PAF | ORPHA:441; PMID:40053259 |
| Bladder symptoms / urinary incontinence | HP:0000020; HP:0000016 (retention) | 59%; severe (catheter or incontinence) in 37.6% | PMID:40053259 |
| Constipation | HP:0002019 | 45% | PMID:40053259 |
| Sexual dysfunction / erectile dysfunction | HP:0100639; HP:0000802 | 40% | PMID:40053259 |
| Thermoregulatory dysfunction / heat intolerance | HP:0002046 | 38% | PMID:40053259 |
| REM sleep behavior disorder / dream enactment | HP:5200291 | 52% endorsed (median 7 years after OH onset); 5 of 8 confirmed by vPSG. An earlier 1998 series of 6 found none. | PMID:40053259; PMID:27757562; PMID:9598693 |
| Hyposmia | HP:0004409 | Mean UPSIT 22 ± 3 (similar to PD, lower than MSA); a second study found it milder than in PD | PMID:19201246; PMID:19433741 |
| Bradycardia / slow steady heart rate | HP:0001662 | Typical of patients who keep the PAF phenotype | PMID:28093795; PMID:24095130 |
| Low plasma norepinephrine | HP:0012099 (parent term) | Very frequent; "very low plasma norepinephrine levels" | ORPHA:441; PMID:28093795 |
| Anemia (normocytic, low erythropoietin) | HP:0001903 | 38% of 84 patients with primary autonomic failure | PMID:8017744 |
| Sympathetic pupillary deficit | HP:0007686 | Frequent in PAF compared with MSA and LBD | PMID:40696849 |
| Left ventricular hypertrophy (from supine hypertension) | HP:0001712 | Reported in supine hypertension; hypertensive organ disease in a 3-case series | PMID:11927799; PMID:15633433 |

**Aggravating factors and quality of life.** "Postural symptoms (mainly dizziness and neck pain) were worse in the morning and with warm temperature, straining, exertion, arm movements and food ingestion" (PMID:10552235). Compensatory palpitations and sweating were absent. Patients may only be able to stand for minutes at a time (PMID:21664375; PMID:25185131). Falls and syncope drive disability (PMID:33705537).

---

## 4. Genetic and molecular information

- **Causal genes:** none. This is a sporadic, non-Mendelian disease.
- **Disease protein:** α-synuclein (SNCA, hgnc:11138), present as phosphorylated or misfolded aggregates. CSF α-syn seeding assays (PMCA) are positive in 94% of PAF patients (PMID:33881777).
- **Molecular deficits in noradrenergic terminals.** Forearm vein biopsies show "normal abundance of the NE transporter (NET) protein, together with very low levels of tyrosine hydroxylase (TH)... and reduced vesicular monoamine transporter 2 (VMAT2)" (PMID:29162745). The relevant genes are TH (hgnc:11782), SLC18A2/VMAT2 (lookup needed), and SLC6A2/NET (hgnc:11048).
- **Variants, allele frequencies, ClinVar entries, modifiers, epigenetics, chromosomal abnormalities:** none reported in the sources reviewed. No ClinGen gene–disease validity applies.

---

## 5. Environmental information

No established environmental, lifestyle, or infectious cause. Factors that *aggravate symptoms* (not causes) are heat, meals, straining, exertion, and vasoactive drugs such as alpha-blockers (PMID:10552235; PMID:32979782; PMID:28717053).

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Initiating event (unknown).** α-Synuclein misfolds and aggregates in peripheral autonomic neurons. The trigger is unknown, and prion-like spread is a hypothesis carried over from the synucleinopathy literature rather than something shown in PAF.
2. **This leads to Lewy bodies and neurites in sympathetic ganglia and distal autonomic axons**, and degeneration of preganglionic intermediolateral-column neurons and postganglionic sympathetic neurons. PMID:9255396: "histopathologically by cell loss in intermediolateral columns and sympathetic ganglia"; Lewy bodies were found "in sympathetic ganglia, as well as in autonomic axons in the epicardial fat... and autonomic nerves in the muscularis of the urinary bladder." PMID:27338613: "neuronal degeneration of pre- and postganglionic sympathetic and parasympathetic neurons in the thoracic spinal cord and paravertebral autonomic ganglia."
   - **Branch:** the non-Lewy form, a preganglionic lesion only, carries a risk of premotor MSA (PMID:34669076).
3. **This results in postganglionic noradrenergic denervation plus a vesicular storage defect in the surviving nerves.** "PAF entails moderately decreased cardiac sympathetic innervation and a substantial vesicular storage defect in residual nerves" (PMID:32945121). Denervation is widespread, affecting the heart and renal cortex (PMID:16269589), and skin, where p-syn is found "in the postganglionic sympathetic adrenergic and cholinergic nerve fibers" (PMID:23390175).
4. **This leads to failure of norepinephrine synthesis and release.** TH is low and VMAT2 reduced (PMID:29162745). The lesions "are responsible for defects in the synthesis and release of norepinephrine from sympathetic nerve terminals, resulting in significant hypotension" (PMID:28717053). Plasma NE is very low.
5. **This results in failed baroreflex-mediated vasoconstriction on standing**, giving neurogenic OH with a blunted heart-rate response (ΔHR/ΔSBP < 0.5 bpm/mmHg; PMID:29405350). Peripheral resistance is not maintained. PMID:39608812 *infers* that "P-syn deposition on autonomic nerves may impair control of total peripheral resistance giving rise to symptomatic orthostatic hypotension."
6. **Cerebral and muscle hypoperfusion** follow, producing syncope, dizziness, visual disturbance, and coat-hanger pain (PMID:10552235).
7. **Parallel branches from denervation:**
   - **Denervation supersensitivity** of β-adrenoceptors and pressor sensitivity: "supersensitivity of cardiac beta-adrenoreceptors" (PMID:18514012). This underlies exaggerated responses to pressor drugs and to the water-drinking osmopressor reflex (PMID:21048076).
   - **Supine hypertension.** The mechanism is incompletely understood. Plasma renin is suppressed, but angiotensin II is elevated and mineralocorticoid receptors are activated (PMID:26644241). Supine hypertension then drives **nocturnal pressure natriuresis**, which leads to volume depletion and worse morning OH (PMID:11927799), and also LVH.
   - **Loss of sympathetic drive to erythropoiesis**, giving low erythropoietin and anemia (PMID:8017744; the authors' hypothesis is that "the sympathetic nervous system stimulates erythropoiesis").
   - **Sudomotor, bladder, bowel, and sexual dysfunction** from involvement of the cholinergic sympathetic and parasympathetic pathways.
8. **Central spread in a subset (phenoconversion).** Nigral dopaminergic loss is already present: "PAF and PD entail similarly severe nigral and overall central dopaminergic denervation," with the striatum relatively spared (PMID:18363034). Neuromelanin MRI shows loss in the locus ceruleus and substantia nigra in high-risk PAF (PMID:39825743). Hyposmia and RBD are central markers. Progression leads to PD, DLB, or MSA (see §8).

### Checklist mapping

- **Cell types (cache-verified CL):** sympathetic neuron CL:0011103; noradrenergic neuron CL:0008025; cholinergic neuron CL:0000108; dopaminergic neuron CL:0000700. A preganglionic neuron term needs lookup.
- **Processes (GO terms still need lookup; none were verified here):** norepinephrine biosynthesis, catecholamine secretion and storage (vesicular monoamine transport), protein aggregation, baroreflex blood-pressure regulation, neuron death.
- **Chemicals (CHEBI):** noradrenaline CHEBI:33569.
- **Immune involvement:** none described.
- **Molecular profiling:** no transcriptomic, proteomic, or single-cell PAF datasets were found in the cached sources. CSF NfL is elevated only in patients who later convert to MSA (PMID:33881777).

---

## 7. Anatomical structures affected

- **Primary:** the peripheral autonomic nervous system. This means the sympathetic ganglia (UBERON term lookup needed), the thoracic intermediolateral column, and postganglionic fibres.
- **End organs (UBERON, cache-verified):** heart UBERON:0000948 (cardiac denervation); kidney UBERON:0002113 (renal cortex); skin of body UBERON:0002097 and sweat gland UBERON:0001820; urinary bladder (lookup needed).
- **Central nervous system (subclinical or in converters):** substantia nigra UBERON:0002038 and locus ceruleus UBERON:0002148 (PMID:9255396; PMID:18363034; PMID:39825743).
- **Subcellular:** neuronal cytoplasmic inclusions (Lewy bodies) and synaptic or secretory vesicles (the storage defect).
- **Distribution:** symmetric and length-dependent, with small-fibre loss (PMID:26606657). In PAF, p-syn is found at every biopsy site: "the site of analysis is irrelevant in PAF."

---

## 8. Temporal development

- **Onset:** insidious, in adulthood or old age. Pooled mean onset age is 63.1 ± 4.3 years (PMID:42081229). At enrollment in the US cohort, patients were 68 years old (median) and had had autonomic failure for 5 years (PMID:28093795). Most non-OH autonomic symptoms begin near OH onset, while RBD comes later (median 7 years; PMID:40053259).
- **Course:** chronic and progressive, with no remission.
- **Phenoconversion (the central prognostic issue):**

| Study | n | Follow-up | Converted | Breakdown |
|---|---|---|---|---|
| US consortium (PMID:28093795) | 74 | ≤4 y | 34% | DLB 13, PD 6, MSA 6 |
| Mayo retrospective (PMID:28202694) | 78 assessable of 318 | ≥3 y | 12% of possible PAF | MSA 22, PD/DLB 11 |
| Mayo (PMID:32546656) | 275 | — | 24% | MSA 34, PD/DLB 33 |
| 8-centre prospective (PMID:38366572; NCT01799915) | 149 | mean 3 y | 33% | PD 42%, DLB 35%, MSA 23%; **~12% per year** |
| Queen Square (PMID:40397689) | 281 | median 10 y | 33% | 53% of deaths still had the PAF phenotype |
| UK multimodal (PMID:40696849) | 194 | median 13 y | 26% | MSA or LBD |
| **Meta-analysis (PMID:42081229)** | 900 (9 studies) | 6.4 y | **30%** | MSA 12%, DLB 11%, PD 7%; **5.09 per 100 person-years** |

The meta-analysis concludes that "PAF may be a prodromal presentation of PD, DLB, or MSA with phenoconversion incidence rates similar to those of RBD." MSA conversions cluster in the early years, while Lewy body conversions occur at a steady rate. Note that the annual-risk estimates differ: about 12% per year in PMID:38366572 against about 5% per year in the pooled analysis.

- **Critical window:** the pre-motor phase is the opportunity for disease-modifying trials (PMID:37843677; PMID:42444112).

---

## 9. Inheritance and population

- **Inheritance:** sporadic, not applicable (ORPHA:441). There is no penetrance, anticipation, founder effect, or carrier-frequency data.
- **Prevalence:** Orphanet gives a point-prevalence class of **1–9 per 1,000,000 (Europe)**. The source field in that row reads "PMID:2007", which looks malformed and should be checked before citing. No population-based incidence study was found.
- **Sex:** male predominance in pooled cohorts (63.8%; PMID:42081229). In the Queen Square cohort, male sex was associated with conversion to Lewy body disease (PMID:40397689).
- **Geography and ethnicity:** no data. Cohorts are mainly from the US and UK.

---

## 10. Diagnostics

**Clinical criteria.** OH is defined as a sustained fall of ≥20 mmHg systolic or ≥10 mmHg diastolic blood pressure within 3 minutes of standing or tilt (consensus statement, PMID:21431947). PAF additionally requires no secondary cause and no motor or cognitive CNS features (1996 consensus criteria, as cited in PMID:40696849). Neurogenic supine hypertension is defined as SBP ≥140 and/or DBP ≥90 mmHg after 5 minutes supine (PMID:29766366). Screening and treatment recommendations: PMID:28050656.

| Test | Finding in PAF | Source |
|---|---|---|
| Tilt table / active stand | nOH; **ΔHR/ΔSBP < 0.492 bpm/mmHg** (sensitivity 91.3%, specificity 88.4%) | PMID:29405350 |
| Supine plasma norepinephrine | Very low. Values >100 pg/mL (Mayo) or ≥200 pg/mL (UK, Queen Square) predict conversion | PMID:28093795; PMID:28202694; PMID:40696849 |
| Cardiac ¹⁸F-dopamine PET / ¹²³I-MIBG | Denervated. MIBG abnormal in 84.6% of 39 cases. Low cardiac ¹⁸F-dopamine predicts conversion to LBD; normal uptake points toward MSA | PMID:16269589; PMID:41072204; PMID:37843677 |
| **Skin biopsy for phosphorylated α-synuclein** | Positive in **100%** (22 of 22) in Synuclein-One versus 3.3% of controls. A total p-syn score >3 separates PAF from MSA (specificity 100%, sensitivity 82%). Absent in acquired autonomic neuropathies | PMID:38506839; PMID:39608812; PMID:23390175; PMID:26606657 |
| Skin autonomic innervation, sympathetic skin responses | Marked postganglionic denervation, whereas skin innervation is preserved in MSA | PMID:20660924; PMID:18805037 |
| CSF α-syn PMCA and NfL | PMCA positive in 94%. An MSA-like seeding profile or raised NfL predicts MSA | PMID:33881777 |
| Autonomic reflex screen / thermoregulatory sweat test | Moderate to severe failure. A preganglionic sweat-loss pattern predicts MSA | PMID:40053259; PMID:28202694 |
| Smell test (UPSIT) | Hyposmia, which points toward PD/DLB conversion | PMID:19201246; PMID:42081229 |
| DaTSCAN, FDOPA-PET, neuromelanin MRI | Abnormal DaTSCAN in 39% of patients up to 7 years before conversion | PMID:40397689; PMID:39825743 |
| Polysomnography | RBD confirmation | PMID:27757562 |
| Pupillometry | Sympathetic deficits. Normal pupils predict conversion | PMID:40696849 |

**Genetic testing:** not indicated for PAF itself. It can be used to exclude mimics.

**Differential diagnosis:** prodromal MSA, PD or DLB with OH, autoimmune autonomic ganglionopathy, amyloid and diabetic autonomic neuropathy, and non-neurogenic OH from volume depletion, anemia, or polypharmacy (PMID:34392300; PMID:29405350). The MDS prodromal-MSA criteria are 92–100% sensitive in PAF but only 56–67% specific. Requiring UPSIT >28 raises specificity to 90–97% (PMID:42444112).

**Screening:** no population or newborn screening exists.

---

## 11. Outcome and prognosis

- **Survival:** median **15 years from orthostatic symptom onset**, driven mainly by age and OH severity (PMID:40397689). In that cohort, 41% died during follow-up. Survival is better than in the other synucleinopathies (PMID:27338613; PMID:24095130).
- **Patients who stay "pure"** have very low NE, a slow resting heart rate, no RBD, and preserved smell (PMID:28093795). "not all patients with pure autonomic failure will develop motor or cognitive symptoms, even with prolonged follow-up" (PMID:40053259).
- **Predictors of conversion to MSA:** younger onset, severe bladder dysfunction, preserved smell, HR rise on tilt >10 bpm, higher NE, preganglionic anhidrosis, subtle motor signs, CSF NfL (PMID:28093795; PMID:38366572; PMID:33881777).
- **Predictors of conversion to PD/DLB:** hyposmia, blunted tilt HR response (HR 6.1 for PD), RBD, low cardiac ¹⁸F-dopamine, male sex, older age (PMID:38366572; PMID:37843677; PMID:40397689).
- **Predictor of any conversion:** RBD (odds ratio 7.1; PMID:28093795).
- **Complications:** syncope, falls, injury, supine hypertension with end-organ damage (LVH, transient ischemic attack in one case series), anemia (PMID:15633433; PMID:11927799; PMID:8017744).

---

## 12. Treatment

There is no disease-modifying therapy: "There is currently no specific treatment to stop progression in PAF" (PMID:27338613). The goal of treatment is to relieve symptoms, not to normalize blood pressure (PMID:33705537).

**Choosing a drug.** Patients with low "sympathetic reserve", which includes PAF, "tend to respond better to 'norepinephrine replacers' (midodrine and droxidopa)" (PMID:32979782).

| Intervention | Mechanism | Evidence | Suggested NCIT / CHEBI |
|---|---|---|---|
| Non-pharmacologic: avoid triggers, high salt and fluid intake, counter-maneuvers, compression garments | Volume and venous return | First-line (PMID:21664375; PMID:28050656) | Supportive Care NCIT:C15747 |
| Abdominal binder (40 mmHg) | Raises stroke volume | Standing BP +15/6 mmHg (PMID:15241645) | — |
| Rapid water drinking (~500 mL) | Osmopressor reflex | PMID:21048076 | — |
| Head-up tilt sleeping | Reduces nocturnal natriuresis | Scoping review (PMID:37626994) | — |
| **Midodrine** | α1-agonist (direct vasoconstriction) | RCT, n=171: improved standing SBP and symptoms; adverse effects include supine hypertension, piloerection, urinary retention (PMID:9091692) | Pharmacotherapy NCIT:C15986 + CHEBI:6933 |
| **Droxidopa** | Norepinephrine prodrug | Phase 3: OHQ composite +0.90 (p=0.003), standing SBP +11.2 mmHg (PMID:24944260). Withdrawal trial missed its primary endpoint (PMID:25350981) | CHEBI:31524 |
| Fludrocortisone | Volume expansion (mineralocorticoid) | Use with caution (PMID:33705537; PMID:15633433) | CHEBI:50885 |
| Pyridostigmine | Ganglionic enhancer | Reduced standing diastolic BP fall with no supine rise (PMID:16476804). Better suited to preserved reserve | CHEBI:8665 |
| Atomoxetine | NET inhibitor | Acutely beat midodrine (PMID:25185131), but a 4-week RCT showed no benefit over placebo (PMID:39294522). Response depends on residual sympathetic tone (PMID:34176285) | CHEBI:127342 |
| Recombinant erythropoietin | Corrects anemia | Hb 108 → 133 g/L in 5 of 5 patients (PMID:8017744) | — |
| **Supine hypertension:** avoid lying flat in the daytime, short-acting nighttime antihypertensives (e.g., transdermal nitroglycerin) | — | PMID:11927799 | — |
| Eplerenone (night dose) | Mineralocorticoid receptor antagonist | Supine SBP −32 mmHg (crossover, n=10, 7 with PAF) (PMID:26644241) | CHEBI:31547 |
| CPAP (8–12 cmH₂O overnight) | Valsalva-like fall in cardiac output | Night SBP −23 mmHg, less nocturia, better morning orthostatic tolerance (PMID:36601916) | — |

- **Pharmacogenomics:** none described.
- **Gene, cell, and RNA therapies:** none.
- **Trials:** registered work is mostly observational, e.g., NCT01799915 (natural history) and NCT04700722 (Synuclein-One). Phenoconversion biomarkers are being developed specifically to select patients for future disease-modification trials (PMID:37843677; PMID:42444112).

---

## 13. Prevention

- **Primary prevention:** none is possible, because the cause is unknown.
- **Secondary prevention:** early detection through skin p-syn and autonomic testing, and stratifying conversion risk for trial enrollment.
- **Tertiary prevention:** fall and syncope prevention through education about triggers and medications (PMID:33705537); treating supine hypertension to prevent LVH and nocturnal natriuresis (PMID:11927799; PMID:29766366).
- **Genetic counseling:** not applicable, since PAF is sporadic.
- **Vaccination, public-health, and environmental measures:** not applicable.

---

## 14. Other species and natural disease

No naturally occurring PAF in animals was found in the cached literature, and there is no relevant OMIA entry. Not applicable for transmission or zoonosis.

---

## 15. Model organisms

There is **no dedicated PAF animal model** in the reviewed sources.

- **Related models:** sinoaortic-denervated mice, which model loss of baroreflex buffering, show the osmopressor response. Trpv4 is implicated in that response (PMID:21048076, review, MODEL_ORGANISM).
- **What a model would need to capture:** a peripherally restricted synucleinopathy with postganglionic noradrenergic degeneration and spared striatum. The SNCA-based models of the wider synucleinopathy literature were not reviewed here, and none in the cached sources was shown to reproduce PAF specifically. This is a candidate `KNOWLEDGE_GAP` / `HUMAN_MODEL_MISMATCH`.

---

## Notes for knowledge-base curation

1. **Lump/split:** a single Disease entry seems right. Two candidate subtypes or hypotheses could be modelled: Lewy-body PAF (postganglionic, converts to PD/DLB) and non-Lewy PAF (preganglionic, possible premotor MSA) (PMID:34669076; PMID:28188385; PMID:37843677).
2. **Do not add `genetic:` causal genes.** SNCA belongs on pathophysiology nodes (aggregation) as the disease protein.
3. **Wire every phenotype into the pathograph.** OH should be the hub, with branches to cerebral hypoperfusion (syncope, dizziness, visual symptoms), muscle hypoperfusion (neck pain), supine hypertension → nocturia/LVH, and denervation → anemia.
4. **Conformance target:** check `just list-modules` for an α-synuclein aggregation or autonomic module before adding one.
5. **CURIEs still to look up:** HP terms for supine hypertension, dizziness, and postprandial hypotension; UBERON terms for sympathetic ganglion, intermediolateral column, and urinary bladder; a CL term for preganglionic neuron; all GO process terms; HGNC for SLC18A2.
6. **Orphanet epidemiology source:** the "PMID:2007" source in the ORPHA:441 epidemiology row looks malformed. Do not cite it as a PMID.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 59 |
| Resolved | 59 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 13 |
| Quoted claims found in source | 13 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 59 |
| On topic | 52 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 17 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012378` (1 mention) - the report calls it "Fatigue, weakness, lethargy"; HP calls it **Fatigue**
- `HP:0000017` (1 mention) - the report calls it "Nocturia / nocturnal pressure natriuresis"; HP calls it **Nocturia**
- `HP:0001662` (1 mention) - the report calls it "Bradycardia / slow steady heart rate"; HP calls it **Bradycardia**
- `HP:0012099` (1 mention) - the report calls it "parent term"; HP calls it **Abnormal circulating catecholamine concentration**
- `HP:0001903` (1 mention) - the report calls it "Anemia (normocytic, low erythropoietin)"; HP calls it **Anemia**
- `UBERON:0000948` (1 mention) - the report calls it "cardiac denervation"; UBERON calls it **heart**
- `UBERON:0002113` (1 mention) - the report calls it "renal cortex"; UBERON calls it **kidney**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001278` (1 mention) - the report calls it "Orthostatic hypotension (neurogenic, severe)"; HP calls it **Orthostatic hypotension**
- `HP:0000505` (1 mention) - the report calls it "Visual impairment; may be too coarse"; HP calls it **Visual impairment**
- `HP:0100749` (1 mention) - the report calls it "Chest pain (orthostatic)"; HP calls it **Chest pain**
- `HP:0002046` (1 mention) - the report calls it "Thermoregulatory dysfunction / heat intolerance"; HP calls it **Heat intolerance**
- `HP:5200291` (1 mention) - the report calls it "REM sleep behavior disorder / dream enactment"; HP calls it **REM sleep behavior disorder**
- `HP:0007686` (1 mention) - the report calls it "Sympathetic pupillary deficit"; HP calls it **Abnormal pupillary function**
- `HP:0001712` (1 mention) - the report calls it "Left ventricular hypertrophy (from supine hypertension)"; HP calls it **Left ventricular hypertrophy**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.