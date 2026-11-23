---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-19T14:29:09.757219'
end_time: '2026-11-19T14:38:32.609264'
duration_seconds: 562.85
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: SYNJ1-Related Parkinson Disease
  mondo_id: MONDO:0014233
  category: Mendelian
  causal_genes: SYNJ1
  omim_id: OMIM:615530
  synonyms: early-onset Parkinson disease type 20; Parkinson disease caused by mutation
    in SYNJ1; SYNJ1 Parkinson disease
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
  - claude-opus-5-5
  web_search_requests: 7
  num_turns: 16
  total_cost_usd: 1.3993117449999999
  session_id: acf8848e-8587-4ca0-a94e-b52d786d4a7d
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 41
  retrieval_calls: 39
  assistant_text_blocks: 2
citation_count: 0
reference_validation:
  total_references: 34
  verified: 34
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 26
  quotes_valid: 19
  quotes_unsupported: 7
  unsupported_quote_references:
  - PMID:35328025
  - PMID:32356558
  - PMID:33841314
  - PMID:14622578
  - PMID:29515184
  relevance_assessed: 34
  on_topic: 19
  off_topic: 2
  off_topic_references:
  - PMID:10535736
  - PMID:14622578
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 45
  verified: 43
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 1
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0001332
    reported_labels:
    - Dystonia (limb, trunk; off-period or end-of-dose)
    ontology_label: Dystonia
  - term_id: HP:0007325
    reported_labels:
    - verify
    ontology_label: Generalized dystonia
  - term_id: HP:0002454
    reported_labels:
    - verify
    ontology_label: Eye of the tiger anomaly of globus pallidus
  - term_id: HP:0012444
    reported_labels:
    - verify
    ontology_label: Brain atrophy
  - term_id: UBERON:0000956
    reported_labels:
    - cortical hypometabolism and atrophy; PMIDs 23804577, 24816432
    ontology_label: cerebral cortex
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SYNJ1-Related Parkinson Disease
- **MONDO ID:** MONDO:0014233 (if available)
- **Causal gene(s):** SYNJ1
- **OMIM:** OMIM:615530
- **Synonyms:** early-onset Parkinson disease type 20; Parkinson disease caused by mutation in SYNJ1; SYNJ1 Parkinson disease
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **SYNJ1-Related Parkinson Disease** covering all of the
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

I'm pulling primary abstracts from PubMed for the key SYNJ1 papers. Next I'll verify the founding reports, the model papers and the clinical cohort data.

I've finished the database lookups and am now writing the full report.

# SYNJ1-Related Parkinson Disease (PARK20 / early-onset Parkinson disease 20)

**How this report was scoped:** I researched MONDO:0014233 / OMIM:615530, which is autosomal recessive early-onset parkinsonism caused by biallelic variants in **SYNJ1** (synaptojanin 1; HGNC:11503; 21q22.11). Biallelic SYNJ1 variants also cause a separate, severe developmental and epileptic encephalopathy (DEE) with neonatal or infantile onset. That disorder has a different OMIM entry, which I did not retrieve. I discuss it only as a differential and as the severe end of the allelic spectrum.

**Evidence sources and limits:**
- Claims come from PubMed abstracts fetched through NCBI E-utilities, the full text of Lesage et al. 2021, the OLS4 MONDO record and the HGNC REST record.
- I could not retrieve the following, so they are not reported as fact:
  - Orphanet pages (blocked).
  - Full text of the MDSGene review, Wittke et al. 2021 (blocked).
  - gnomAD and ClinVar records.
- All HPO, GO, CL, UBERON, CHEBI and NCIT IDs are **suggestions from my own ontology knowledge, not retrieved this session**. Verify them before loading.

---

## 1. Disease Information

**Overview.** PARK20 is a rare autosomal recessive form of early-onset or juvenile parkinsonism caused by biallelic variants in *SYNJ1*.
- SYNJ1 is a presynaptic phosphoinositide phosphatase with two catalytic domains: an N-terminal Sac1-like domain and a central 5′-phosphatase domain. It works in synaptic vesicle endocytosis.
- The disease was first reported in 2013 by two groups who independently found the homozygous p.Arg258Gln (R258Q) variant:
  - Krebs et al., an Iranian consanguineous family (PMID 23804563). They describe "a homozygous mutation (c.773G>A; p.Arg258Gln) lying within the NH2-terminal Sac1-like inositol phosphatase domain."
  - Quadri et al., an Italian consanguineous family with "Parkinsonism, dystonia, and cognitive deterioration" (PMID 23804577).
- The phenotype is often atypical or complex: dystonia, seizures, cognitive impairment, eye-movement abnormalities, and levodopa response that is poor or limited by dyskinesia.
- Reviews group SYNJ1 with the "atypical PD, often associated with additional symptoms (ATP13A2, FBXO7, DNAJC6, VPS13C, SYNJ1, PLA2G6)" (Cogan 2025, PMID 41253044; Jia 2022, PMID 35328025).

**Identifiers**

| Resource | ID | Source |
|---|---|---|
| MONDO | MONDO:0014233, "early-onset Parkinson disease 20". Definition: "Any Parkinson disease in which the cause of the disease is a mutation in the SYNJ1 gene." | OLS4 |
| OMIM (phenotype) | 615530 | MONDO xref |
| OMIM (gene) | 604297 | HGNC |
| UMLS | C3809824 | MONDO xref |
| DOID | 0060898 | MONDO xref |
| GARD | 0018462 | MONDO xref |
| MedGen | 816154 | MONDO xref |
| Orphanet | Not retrieved (site blocked). HGNC lists Orphanet gene ID 394615, which is a gene identifier, not a disease code. | HGNC |
| ICD-10 / ICD-11 / MeSH | No xref in the MONDO record. Generic Parkinson-disease codes (ICD-10 G20; MeSH "Parkinsonian Disorders") would be the closest, but I did not verify them this session. | — |

**Synonyms** (MONDO): Parkinson disease 20, early-onset; early-onset Parkinson disease type 20; PARK20; Parkinson disease caused by mutation in SYNJ1; SYNJ1 Parkinson disease. The MDS nomenclature form is PARK-SYNJ1 (Farsana 2026, PMID 40829774).

**Data provenance.** Knowledge comes almost entirely from aggregated case and family reports, about 20 parkinsonism families worldwide, plus disease-level resources. There are no EHR-based cohorts.

---

## 2. Etiology

**Cause.** The disease is monogenic and autosomal recessive, caused by homozygous or compound-heterozygous loss-of-function variants in *SYNJ1*. Most families are consanguineous.

**Genetic risk factors**
- **Biallelic causal variants.** See §4.
- **Rare heterozygous variants are a possible risk factor for PD.**
  - Senkevich et al. 2024 studied 8,165 PD cases, 818 of them early-onset (EOPD), and 70,363 controls (PMID 39455605).
  - They found a burden of rare nonsynonymous and high-CADD variants in the Sac1 domain (P_FDR = 0.040).
  - In EOPD: "A meta-analysis of EOPD patients demonstrated an association between all rare heterozygous SYNJ1 variants and PD" (P_FDR = 0.029).
  - The authors say replication is needed.
- **Possible digenic or oligogenic co-occurrence (unproven):**
  - Heterozygous SYNJ1 p.Ser1422Arg together with a heterozygous PINK1 truncating variant (Quadri 2013, PMID 23804577).
  - Heterozygous SYNJ1 p.Cys21Phe together with homozygous PRKN p.Asn52Metfs*29 in a Brazilian EOPD patient, proposed as "a potential synergistic effect" (Cotrin 2024, PMID 38836947).
- **Expression in sporadic PD:** SYNJ1 transcript is "down-regulat[ed] … in a subset of sporadic PD brains" (Pan 2020, PMID 32356558).

**Environmental risk factors.** None are reported for PARK20.

**Protective factors.** None are known, genetic or environmental.

**Gene–environment interactions.** None are documented. CTD and GxE resources gave nothing specific to SYNJ1-PD in the searches I ran.

---

## 3. Phenotypes

The frequencies below are my own counts. They come from Table 1 of Lesage et al. 2021 (PMID 33841314), which tabulates 23 people with PARK20-type disease: 19 previously published plus 4 new. They are approximate.

| Phenotype | Suggested HPO | Type | Onset / course | Approximate frequency | Evidence |
|---|---|---|---|---|---|
| Parkinsonism (bradykinesia, rigidity) | HP:0001300 Parkinsonism; HP:0002067 Bradykinesia; HP:0002063 Rigidity | Sign | Motor onset mostly 12–40 y (range 12–52); progressive | 100% (defining) | PMIDs 23804563, 23804577, 27496670, 33841314 |
| Resting tremor | HP:0002322 | Sign | Early | Common; the "principal" features are "tremor, dystonia, bradykinesia" | PMID 33841314; Kirola 2016 (tremor, bradykinesia, rigidity), PMID 27496670 |
| Dystonia (limb, trunk; off-period or end-of-dose) | HP:0001332 | Sign | Early or with treatment | Most patients | PMIDs 23804577, 24816432, 30473187, 33841314 |
| Seizures (generalized tonic-clonic, febrile; often in childhood, before parkinsonism) | HP:0001250; HP:0002069 | Sign | Infancy to young adulthood; may predate parkinsonism by years | About 40–50% of PARK20 patients; varies within families | PMIDs 23804563, 24816432, 30187305, 33841314. "The presence of seizures might represent a red flag to suspect PARK20" (PMID 24816432) |
| Cognitive impairment / intellectual disability / frontal syndrome | HP:0100543; HP:0001249; HP:0000727 | Sign / behavioural | Childhood developmental delay or progressive adult decline | Common, especially with R258Q | PMIDs 23804577, 24816432, 26725142, 30187305, 33841314 |
| Developmental (psychomotor) delay | HP:0001263 | Sign | Childhood | Some R258Q families | Olgiati 2014: "mild developmental psychomotor delay" (PMID 24816432) |
| Eye-movement abnormalities (vertical gaze palsy, diplopia) | HP:0000496; HP:0000651; HP:0007814 (verify) | Sign | Variable | Some patients | PMIDs 30473187, 33841314 |
| Levodopa-induced dyskinesia / poor levodopa tolerance | HP:0007325 (verify) | Treatment response | Early in treatment | Frequent | "Response to levodopa was poor, and limited by side effects" (PMID 23804577); "intense dyskinesia and dystonia" on levodopa (PMID 27496670) |
| Motor fluctuations | HP:0002454 (verify) | Treatment response | Years after onset | Some patients | PMIDs 26149920, 33841314 |
| Mood and behavioural disorders | HP:0000708; HP:0000716 | Behavioural | Progressive | Reported in 2 of 2 siblings | De Rosa 2016 (PMID 26725142) |
| Non-motor symptoms: drooling, dysphagia, pain, urinary dysfunction, cold intolerance; REM sleep behaviour disorder absent | HP:0002307; HP:0002015; HP:0000012 | Symptom | Progressive | Small series | PMID 26725142: "RBD were not found, whereas the neuropsychological assessment revealed a progressive cognitive impairment." |
| Pyramidal signs / spasticity | HP:0007256; HP:0001257 | Sign | Variable | Described in complex EOPD cohorts | Secondary mention only, not well quantified |
| Brain atrophy, cerebral hypometabolism (imaging) | HP:0012444 (verify) | Imaging / lab | — | Some patients | PMID 23804577 |

**Quality of life.** No EQ-5D, SF-36 or PDQ-39 data exist for PARK20. Disability comes mainly from:
- early and disabling dyskinesia, which limits dopaminergic therapy;
- cognitive impairment, which in severe R258Q cases prevented neuropsychological testing (PMID 33841314);
- seizures.

Pain in SYNJ1 carriers is under-studied: the evidence "is limited and insufficient" (Alizadeh 2023, PMID 38020640).

---

## 4. Genetic / Molecular Information

**Gene.** *SYNJ1*, synaptojanin 1.
- Identifiers: HGNC:11503; Entrez 8867; Ensembl ENSG00000159082; UniProt O43426; OMIM 604297. Location 21q22.11. Aliases INPP5G, PARK20 (HGNC REST).
- Domains: Sac1 domain, which hydrolyzes PI4P and PI3P; 5′-phosphatase domain, which hydrolyzes PI(4,5)P2; proline-rich C-terminus.

**Reported variants.** Source is Table 1 of Lesage 2021 (PMID 33841314) plus the abstracts cited. Most are not yet in ClinVar or ACMG-classified in the retrieved sources. The parkinsonism allele with the strongest evidence is p.R258Q.

| Variant (protein) | cDNA | Domain | Zygosity | Ancestry | Phenotype | PMID |
|---|---|---|---|---|---|---|
| p.Arg258Gln (R258Q) | c.773G>A | Sac1 | Homozygous | Iran; Italy (Sicily, Naples); Algeria | Parkinsonism ± seizures, dystonia, cognitive impairment | 23804563, 23804577, 24816432, 33841314 |
| p.Trp171* / p.Arg258Gln | — | Sac1 | Compound het | Germany | Parkinsonism; childhood/neonatal seizures | Rauschendorf (cited in Lesage Table 1; PMID not retrieved) |
| p.Tyr232His / p.Asp791Ilefs*4 | — | Sac1 / 5′-phosphatase | Double het, phase unknown | France | Dystonia-parkinsonism at 39 y, frontal syndrome, vertical gaze palsy | 33841314 |
| p.Arg459Pro | c.1376C>G | Sac1 / linker region | Homozygous | India | Juvenile PD, onset 12 and 18 y | 27496670 |
| p.Arg459His | — | — | Homozygous | India | Onset 34 y | Kumar (cited in Lesage Table 1) |
| p.Tyr832Cys | c.2495A>G | 5′-phosphatase | Homozygous | China; Senegal | Typical, slowly progressive, levodopa-responsive PD; onset 20–52 y | 31751865, 33841314 |
| p.Arg839Cys | — | 5′-phosphatase | Homozygous | Iran | Parkinsonism ± seizure; poor levodopa response | Taghavi (cited in Lesage Table 1) |
| p.Ala860Glyfs*5 (c.2579-2A>G, exon 20 skipping) / p.Pro1282Leu (c.3845C>A) | — | — | Compound het | China (non-consanguineous) | Diplopia, dystonia, parkinsonism; responded to clonazepam | 30473187 |
| p.Leu1406Phefs*42 / p.Lys1321Glu | — | C-terminal | Compound het | Tunisia | Juvenile PD (16, 21 y) + epilepsy; good levodopa response | 30187305 |
| p.Thr657Ala | c.1969A>G | — | Homozygous | China | EOPD treated with DBS | 42517031 |
| c.1627+13T>A | — | Intronic | Not stated | China | EOPD treated with DBS (pathogenicity uncertain) | 42517031 |
| rs2254562 (T>C) | — | — | Homozygous | Spain | Juvenile parkinsonism + seizures + cognitive impairment | 39273702. Pathogenicity uncertain: reported as a common SNP; interpret cautiously |

**Allelic DEE (severe end of the spectrum, for comparison).** These are truncating or dual-phosphatase-null variants: p.Arg136*, p.Gln237* (c.709C>T), p.Gln287Profs*27, p.Trp843*, p.Gln647Argfs*6/p.Ser1122Thrfs*3, p.Tyr888Cys, and c.242-2A>G.
- Hardies 2016 on p.Tyr888Cys: "impair, but not abolish, the dual phosphatase activity of SYNJ1" (PMID 27435091).
- Al Zaabi 2018: p.Gln237*, a homozygous null variant (PMID 29179256).
- Maj 2023: c.242-2A>G (PMID 36148638).

**Classification.** ACMG classes were not given in the retrieved papers, and ClinVar was not retrieved. Rarity evidence available:
- p.R459P was absent from dbSNP, 1000 Genomes, ExAC and ESP (PMID 27496670).
- p.Y232H and p.D791Ifs*4 were not in gnomAD (PMID 33841314).

**Origin.** Germline only.

**Functional consequence.** Loss of function, partial or domain-specific. R258Q "impaired the phosphatase activity of SYNJ1 against its Sac1 domain substrates in vitro" (PMID 23804563).

**Genotype–phenotype.** Lesage 2021 speculated that biallelic truncating variants "may lead to severe progressive neurodegeneration," while missense or missense-plus-stop combinations "lead to milder phenotypes associated with parkinsonism." They also found that "clinical severity does not depend exclusively on the protein domain affected" (PMID 33841314).

**Modifier genes, epigenetics, chromosomal abnormalities.**
- No validated modifiers. PINK1 and PRKN co-occurrence is only anecdotal (PMIDs 23804577, 38836947).
- No epigenetic data.
- No chromosomal or structural causes reported. *SYNJ1* lies on chromosome 21 and is over-expressed in trisomy 21, but that is unrelated to PARK20 (PMID 35194165).

---

## 5. Environmental Information

No environmental, lifestyle or infectious contributors are known. There is one possible trigger observation: in the Algerian proband, a generalized tonic-clonic seizure at age 2 occurred after fever (PMID 33841314).

---

## 6. Mechanism / Pathophysiology

### Causal chain
1. **Biallelic *SYNJ1* variants** lead to loss of Sac1 phosphatase activity (R258Q) or of 5′-phosphatase activity, or to reduced protein. *Demonstrated in vitro* (PMID 23804563) and in knock-in mice (PMID 28231468).
2. Loss of phosphatase activity results in **failure to dephosphorylate presynaptic phosphoinositides**: PI4P/PI3P for the Sac1 domain, PI(4,5)P2 for the 5′-phosphatase domain.
   - Synj1-null mice show raised PI(4,5)P2 (Cremona 1999, PMID 10535736).
   - Synj1+/− midbrain neurons have "elevated PI(4,5)P2" (PMID 32356558).
3. Abnormal phosphoinositide levels lead to **impaired clathrin uncoating and synaptic vesicle endocytosis**. Clathrin-coated vesicles and intermediates accumulate.
   - Mouse evidence: "Parkinson Sac Domain Mutation in Synaptojanin 1 Impairs Clathrin Uncoating at Synapses" (PMID 28231468); Cremona 1999 (PMID 10535736).
   - Fly evidence: Synj is "recruited by endophilin to promote synaptic vesicle uncoating" (PMID 14622578).
   - **Branch A: endolysosomal and autophagy defects.**
     - R258Q blocks presynaptic autophagosome maturation in flies and in patient iPSC-derived neurons. "Synaptojanin is essential for macroautophagy within presynaptic terminals" (Vanhauwaert 2017, PMID 28331029).
     - Synj1 depletion enlarges early endosomes and impairs transferrin recycling, and "the same alterations … occur in fibroblasts of PARK20 patients" (PMID 29515184).
   - **Branch B: α-synuclein handling.**
     - Synj1+/− mice show α-synuclein accumulation and impaired autophagy (PMID 32356558).
     - SYNJ1 depletion raises PIP3, which promotes α-synuclein aggregation (Choong 2023, PMID 36939875).
     - *Inferred* for the human disease: no PARK20 autopsy has been retrieved.
   - **Branch C: compensatory proteostasis stress.** "Mutant brains had elevated auxilin (PARK19) and parkin (PARK2) levels" (PMID 28231468). This links SYNJ1 to the DNAJC6 and PRKN pathways.
4. These presynaptic defects are **selective for nigrostriatal dopaminergic terminals**. R258Q mice show dystrophic changes in dopaminergic striatal axons (PMID 28231468). In a subset of dopaminergic axons in the dorsolateral striatum, these appear as dystrophic membrane infoldings with reduced dopamine release (Wu 2026, PMID 42853660). Synj1+/− mice show dopaminergic terminal degeneration (PMID 32356558).
5. Terminal dysfunction leads to **reduced striatal dopamine signalling**, then to parkinsonism. Patients have "severe nigrostriatal dopaminergic defects" on imaging (PMID 24816432). Flies carrying the R258Q-equivalent mutation lose dopaminergic neurons (PMID 28331029).
6. **Parallel branch:** the same synaptic-vesicle recycling defect in cortical and hippocampal circuits likely leads to seizures and cognitive impairment.
   - R258Q mice have "neurological manifestations similar to those of human patients," including epilepsy (PMID 28231468).
   - Dual-phosphatase loss causes refractory infantile seizures (PMID 27435091).
   - The cortical circuit mechanism is *inferred*.
7. Variable dopaminergic terminal pathology combined with relatively preserved postsynaptic receptors probably explains the **narrow levodopa therapeutic window and early dyskinesia**. This is *inferred*, not demonstrated.

**Pathways:**
- Phosphatidylinositol phosphate metabolism (KEGG hsa04070; Reactome "Synthesis of PIPs at the plasma membrane").
- Clathrin-mediated endocytosis and synaptic vesicle cycle (KEGG hsa04721).
- Autophagy and endosomal recycling.

There is no notable immune or epigenetic involvement. No omics, single-cell or CRISPR-screen data specific to PARK20 were found.

**Suggested GO terms:**
- synaptic vesicle endocytosis, GO:0048488
- clathrin coat disassembly, GO:0072318
- phosphatidylinositol dephosphorylation, GO:0046856
- phosphatidylinositol-4,5-bisphosphate 5-phosphatase activity, GO:0004439
- autophagosome maturation, GO:0097352
- presynaptic endocytosis (verify ID)
- dopamine secretion, GO:0014046

**Suggested CL terms:**
- dopaminergic neuron, CL:0000700
- neuron, CL:0000540
- hair cell and cone photoreceptor, from zebrafish models only: CL:0000855, CL:0000573

---

## 7. Anatomical Structures Affected

- **Primary:** the brain, specifically the nigrostriatal system.
  - substantia nigra pars compacta, UBERON:0001965
  - striatum, UBERON:0002435
  - dorsolateral striatum / putamen, UBERON:0001874
- **Other:** cerebral cortex, UBERON:0000956 (cortical hypometabolism and atrophy; PMIDs 23804577, 24816432).
- **Autonomic:** cardiac sympathetic innervation is **spared**. "Indexes of cardiac sympathetic innervation in the two patients did not differ from those of control subjects" (PMID 26725142).
- **Body system:** nervous system.
- **Subcellular:**
  - presynaptic terminal, GO:0098793
  - clathrin-coated vesicle, GO:0030136
  - early endosome, GO:0005769
  - autophagosome, GO:0005776
- **Lateralization:** not specifically characterized. Imaging defects are described as bilateral, e.g. "bilateral nigrostriatal dopaminergic deficit" in the German family (PMID 33841314).

---

## 8. Temporal Development

- **Onset.** Juvenile to early adult.
  - Motor onset 12–40 y in most cases. Typical PARK20 onset is stated as "20–31 years" (PMID 33841314), though tabulated cases range from 12 to 52 y.
  - Seizures or developmental delay may begin in infancy or childhood (PMIDs 24816432, 33841314).
  - Onset is insidious.
- **Progression.** Chronic and progressive, at a variable rate.
  - Slow in p.Y832C homozygotes (PMID 31751865).
  - Progressive cognitive decline in R258Q (PMID 26725142).
  - In one heterozygous p.A551V carrier: motor fluctuations at 11 y after diagnosis and dementia at 13 y (PMID 26149920; that carrier's causality is doubtful).
- **Postural instability.** It appears on gene-specific timelines in monogenic parkinsonisms; SYNJ1 was included in the individual-patient meta-analysis (Marsili 2021, PMID 32436106). I did not retrieve the SYNJ1-specific value.
- **Remission.** None.
- **Critical periods.** Not defined.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive. Most families are consanguineous (Iran, Italy, India, Algeria, Tunisia, China).
- **Prevalence:** unknown and extremely rare.
  - Lesage 2021 counted 33 SYNJ1 carriers from 19 families in the literature, including the DEE cases (PMID 33841314).
  - In a French-led cohort of 460 early-onset index cases, 3 index families carried biallelic variants. That is about 0.65% (my calculation).
  - Across Africa, "ATP13A2-, SYNJ1-, and PARK7-related autosomal recessive (atypical) PD was very rare (0.08%) and only observed in NA [North Africa]" (Banjaw 2026, PMID 41958045).
  - In a Taiwanese cohort of 250 EOPD and 100 familial PD cases, "No patients harbored homozygous or compound heterozygous mutations" (Chen 2015, PMID 26149920).
  - In an Indian juvenile-parkinsonism cohort, "PARK-PRKN, PARK-PLA2G6, and PARK-SYNJ1 are the common causes of genetically mediated juvenile parkinsonism in India" (Farsana 2026, PMID 40829774).
- **Penetrance:** appears complete for biallelic genotypes; formal estimates are not available. Heterozygous parents are unaffected.
- **Expressivity:** highly variable, even within families. "Susceptibility to seizures varies considerably, even within families" (PMID 33841314).
- **Anticipation and germline mosaicism:** not reported.
- **Founder effect:** p.R258Q recurs in Iranian, Italian (Sicilian and Neapolitan), Algerian and German families. I did not retrieve haplotype analysis.
- **Carrier frequency:** not retrieved from gnomAD.
- **Sex ratio:** roughly equal in reported sibships.

---

## 10. Diagnostics

- **Imaging.**
  - Dopamine transporter or presynaptic dopaminergic imaging shows "severe nigrostriatal dopaminergic defects" (PMID 24816432).
  - FDG-PET may show striatal and cortical hypometabolism (PMIDs 23804577, 24816432).
  - MRI is normal or shows mild cortical atrophy or white-matter hyperintensities (PMID 33841314).
  - Cardiac MIBG is normal, unlike in typical PD (PMID 26725142).
- **EEG:** slowing in some patients; hypsarrhythmia in the allelic DEE (PMIDs 33841314, 29179256).
- **Laboratory / biomarkers:** none specific. In research settings, patient fibroblasts show enlarged early endosomes (PMID 29515184).
- **Genetic testing:**
  - Multigene EOPD or parkinsonism panels that include SYNJ1, or WES/WGS. WGS found p.Gln237* (PMID 29179256).
  - Homozygosity mapping plus WES in consanguineous families (PMID 23804563).
  - Intronic and splice variants may need RNA studies. c.2579-2A>G caused exon 20 skipping (PMID 30473187).
  - CMA, karyotype, FISH, mtDNA and repeat-expansion testing are not indicated, except to rule out differentials.
  - GeneReviews "Monogenic Parkinson Disease Overview" covers the evaluation strategy (PMID 20301402).
  - Lesage suggests SYNJ1 screening "should be considered in isolated cases and in patients with a later AO" (PMID 33841314).
- **Clinical criteria:** none specific to PARK20. Diagnosis combines MDS clinical criteria for parkinsonism with molecular confirmation.
- **Differential diagnosis:**
  - PRKN, PINK1, PARK7: typical EOPD with good levodopa response.
  - DNAJC6 (PARK19), the closest mechanistic relative.
  - ATP13A2, FBXO7, PLA2G6, VPS13C.
  - Wilson disease, NBIA disorders, dopa-responsive dystonia, juvenile Huntington disease.
  - MDSGene notes that "the age at onset was earlier in monogenic atypical parkinsonism (24 vs 40 years)" (Wittke 2021, PMID 34396589).
- **Screening:** no population or newborn screening. Cascade carrier testing of relatives is possible once the familial variants are known.

---

## 11. Outcome / Prognosis

- **Survival:** no data for PARK20. In the allelic DEE, death occurred in adolescence: "Both siblings died at an approximate age of 16 years" (PMID 36148638).
- **Morbidity:** progressive motor disability, disabling dyskinesia, cognitive decline and epilepsy. Example off-medication scores: UPDRS-III 35/108 with Hoehn & Yahr 2.5 at age 25 (PMID 33841314).
- **Prognostic factors (tentative):**
  - Truncating biallelic genotypes lead to more severe disease.
  - Missense genotypes such as p.Y832C give a milder, more typical, levodopa-responsive course (PMIDs 31751865, 33841314).
- **Validated biomarkers or QoL instruments:** none.

---

## 12. Treatment

There are no disease-modifying therapies and no clinical trials. Evidence comes from case reports only.

| Intervention | Suggested NCIT | Outcome | PMID |
|---|---|---|---|
| Levodopa/carbidopa | Levodopa C603 (verify) | Response varies from poor to good, often limited by early severe dyskinesia. Example: "good respond to low doses of levodopa … with no dyskinesia" in compound-het Tunisian siblings. p.Y832C: "excellent response to levodopa." | 23804577, 27496670, 30187305, 31751865 |
| Dopamine agonists, anticholinergics | Dopamine agonist (verify) | "Partial improvement" | 24816432 |
| Clonazepam | Clonazepam C28920 (verify) | "Clonazepam resolved the clinical symptoms, especially the severe trunk dystonia" (preliminary report) | 30473187 |
| Deep brain stimulation | Deep Brain Stimulation (verify) | GPi-DBS: LEDD 775 → 300 mg/day with less dyskinesia. STN-DBS: LEDD 955 → 605 mg/day and UPDRS-III 51 → 32 at 1.5 y. | 42517031 |
| Antiseizure medications | Anticonvulsant agent (verify) | Standard practice for seizures; no SYNJ1-specific data | — |

- **Pharmacogenomics:** none.
- **Gene, RNA or cell therapy:** none in humans. Two preclinical observations:
  - SYNJ1 overexpression rescued defects in DNAJC6-mutant flies (Jacquemyn 2023, PMID 36739293).
  - SYNJ1 overexpression rescued motor deficits in SNCA-A53T and MPTP mice (Tian 2023, PMID 37419331).
- **Supportive care:** physiotherapy, speech and swallowing therapy, cognitive and psychiatric support. These are extrapolated from general PD care.

---

## 13. Prevention

- **Primary prevention:** not possible beyond reproductive options.
- **Genetic counselling:** each sibling of an affected person has a 25% recurrence risk. Carrier testing, prenatal diagnosis and PGT are possible once the familial variants are known. This follows the general AR counselling covered in GeneReviews (PMID 20301402).
- **Secondary prevention:** early molecular diagnosis to guide cautious dopaminergic dosing, given early dyskinesia.
- **Vaccines, prophylaxis, public-health measures:** not applicable.

---

## 14. Other Species / Natural Disease

- **Naturally occurring disease:** none reported. OMIA was not searched successfully.
- **Orthologs:** I did not retrieve NCBI Gene IDs this session; verify them in NCBI Gene.
  - mouse *Synj1*
  - zebrafish *synj1*; its mutants nrc, slacker and comet are retinal and hair-cell mutants (PMIDs 15470129, 24419318, 19424431)
  - Drosophila *synj* (PMID 14622578)
  - C. elegans *unc-26*
- **Conservation:** the synaptic-vesicle uncoating function is conserved across species (PMIDs 14622578, 10535736). There is no zoonotic relevance.

---

## 15. Model Organisms

| Model | Phenotype / recapitulation | PMID |
|---|---|---|
| **Synj1 R258Q knock-in mouse** (De Camilli lab) | "Mice carrying this mutation developed neurological manifestations similar to those of human patients." Seizures; clathrin-coated intermediates build up; dystrophic dopaminergic striatal axons; auxilin and parkin raised. | 28231468 |
| R258Q mouse, follow-up | A subset of dorsolateral-striatum dopaminergic axons has membrane infoldings and reduced dopamine release | 42853660 |
| **Synj1 knockout mouse** | "Exhibit neurological defects and die shortly after birth"; PI(4,5)P2 raised; clathrin-coated vesicles accumulate. Models the DEE end of the spectrum. | 10535736 |
| **Synj1+/− mouse** | Male mice: age-dependent motor deficits, α-synuclein accumulation, impaired autophagy, dopaminergic terminal degeneration | 32356558 |
| **Drosophila synj^RQ knock-in** | Autophagosome maturation is blocked at synapses; "dopaminergic neuron loss" | 28331029 |
| Drosophila *synj* null | Vesicle uncoating defects, endophilin-dependent | 14622578 |
| **Patient iPSC-derived neurons (R258Q)** | Presynaptic autophagy defect | 28331029 |
| Isogenic hPSC collection (iSCORE-PD, includes SYNJ1) | A public resource of 65 edited lines | 42310027 |
| Patient fibroblasts | Early endosome enlargement; impaired transferrin recycling | 29515184 |
| Zebrafish *synj1* (nrc, slacker, comet) | Cone ribbon detachment, endolysosomal and autophagy defects, hair-cell transmission fatigue, vestibular deficits. Not PD models. | 15470129, 24392132, 27417116, 19424431, 33584199 |

**Limitations of the models:**
- Mouse and fly models capture dopaminergic terminal dystrophy, but widespread loss of nigral cell bodies and Lewy pathology are not clearly reproduced.
- Zebrafish models address sensory synapses only.
- Rodent-model reviews: Sanchiz-Calvo 2022 (PMID 34628360).

**Resources:** MGI (Synj1), FlyBase (synj; human disease model report FBhh0000626), ZFIN (synj1).

---

### Key gaps
- No ClinVar or ACMG classifications or gnomAD frequencies were retrieved.
- No Orphanet code or prevalence class was retrieved.
- No MDSGene SYNJ1-specific frequency table (full text was blocked).
- No human neuropathology.
- No natural-history or QoL data.
- The Rauschendorf, Taghavi, Kumar, Dyment and Samanta case reports were seen only through Lesage 2021 Table 1, so I have no PMIDs for them.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 26 |
| Quoted claims found in source | 19 |
| Quoted claims **not** found in source | 7 |
| References weighed for topical relevance | 34 |
| On topic | 19 |
| Off topic | 2 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:35328025` *(abstract only)*: "atypical PD, often associated with additional symptoms (ATP13A2, FBXO7, DNAJC6, VPS13C, SYNJ1, PLA2G6)"
  - closest text in source: "Moreover, atypical or complex parkinsonism may be due to mutations in genes such as ATP13A2, DCTN1, DNAJC6, FBXO7, PLA2G6, and SYNJ1"
- `PMID:32356558` *(abstract only)*: "down-regulat[ed] … in a subset of sporadic PD brains"
  - closest text in source: "We demonstrate down-regulation of SYNJ1 transcript in a subset of sporadic PD brains, implicating a potential role of Synj1 deficiency in the decline of dopaminergic function during aging."
- `PMID:33841314` *(abstract only)*: "clinical severity does not depend exclusively on the protein domain affected"
  - Text part not found as substring: 'clinical severity does not depend exclusively on the protein domain affected' (note: only abstract available for PMID:33841314, full text may contain this excerpt)
- `PMID:14622578` *(abstract only)*: "recruited by endophilin to promote synaptic vesicle uncoating"
  - closest text in source: "Interestingly, Synj is mislocalized and destabilized at synapses devoid of Endophilin, suggesting that Endophilin recruits and stabilizes Synj on newly formed vesicles to promote vesicle uncoating"
- `PMID:29515184` *(abstract only)*: "the same alterations … occur in fibroblasts of PARK20 patients"
  - closest text in source: "Importantly, the same alterations of early endosomal compartments and trafficking defects occur in fibroblasts of PARK20 patients"
- `PMID:33841314` *(abstract only)*: "Susceptibility to seizures varies considerably, even within families"
  - closest text in source: "In addition, two siblings from an Algerian consanguineous family carried the homozygous p.R258Q mutation and presented generalized tonic-clonic seizures during childhood, with severe intellectual disability, followed by progressive parkinsonism during their teens"
- `PMID:33841314` *(abstract only)*: "should be considered in isolated cases and in patients with a later AO"
  - closest text in source: "We identified two isolated cases carrying biallelic mutations of SYNJ1 (double-heterozygous p.D791fs/p.Y232H and homozygous p"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:10535736` (2 mentions) - Essential role of phosphoinositide metabolism in synaptic vesicle recycling.
  - shared terms: none
- `PMID:14622578` (2 mentions) - Synaptojanin is recruited by endophilin to promote synaptic vesicle uncoating.
  - shared terms: found

Weighed against this report's own most characteristic terms: `synj1`, `disease`, `park20`, `seizure`, `parkinsonism`, `variant`, `patient`, `r258q`, `verify`, `cognitive`, `severe`, `biallelic`, `dopaminergic`, `levodopa`, `dyskinesia`, `lesage`, `cause`, `dee`, `found`, `onset`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 7 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001332` (1 mention) - the report calls it "Dystonia (limb, trunk; off-period or end-of-dose)"; HP calls it **Dystonia**
- `HP:0007325` (1 mention) - the report calls it "verify"; HP calls it **Generalized dystonia**
- `HP:0002454` (1 mention) - the report calls it "verify"; HP calls it **Eye of the tiger anomaly of globus pallidus**
- `HP:0012444` (1 mention) - the report calls it "verify"; HP calls it **Brain atrophy**
- `UBERON:0000956` (1 mention) - the report calls it "cortical hypometabolism and atrophy; PMIDs 23804577, 24816432"; UBERON calls it **cerebral cortex**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001263` (1 mention) - the report calls it "Developmental (psychomotor) delay"; HP calls it **Global developmental delay**, and lists "Psychomotor developmental delay" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.