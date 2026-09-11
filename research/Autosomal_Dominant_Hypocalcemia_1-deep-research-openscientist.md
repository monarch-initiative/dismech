---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T16:21:32.842440'
end_time: '2026-08-28T16:36:20.952107'
duration_seconds: 888.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Hypocalcemia 1
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
citation_count: 21
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 31
  quotes_valid: 29
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:31189130
  - PMID:40531442
  relevance_assessed: 21
  on_topic: 17
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 28
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 4
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: CL:1000456
    reported_labels:
    - kidney collecting duct principal cell
    ontology_label: mesothelial cell of parietal peritoneum
  labels_variant: 2
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
  path: Autosomal_Dominant_Hypocalcemia_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Autosomal_Dominant_Hypocalcemia_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Hypocalcemia 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Hypocalcemia 1** covering all of the
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

# Autosomal Dominant Hypocalcemia 1 (ADH1): Comprehensive Disease Characteristics Report

**Disease:** Autosomal Dominant Hypocalcemia 1 (ADH1)
**Gene:** *CASR* (calcium-sensing receptor)
**OMIM:** #601198 (phenotype), *601199 (gene) | **Orphanet:** ORPHA:428 | **MONDO:** 0008833 | **HGNC:** 1514 | **UniProt:** P41180 | **Category:** Mendelian (autosomal dominant)

> **Evidence source note:** This report is compiled from **disease-level** aggregated resources (OMIM, Orphanet, HGNC/UniProt) and **primary literature** (human clinical case series, in-vitro functional studies, and mouse-model studies), not from individual EHR data. Evidence type is indicated per claim.

---

## Summary

Autosomal Dominant Hypocalcemia type 1 (ADH1; OMIM #601198) is a rare Mendelian endocrine disorder caused by **heterozygous gain-of-function (activating) missense mutations in *CASR***, the gene encoding the calcium-sensing receptor (CaSR), a class C G-protein-coupled receptor on chromosome 3q13.33. The activating mutations "left-shift" the set-point for extracellular calcium sensing — the receptor is triggered at abnormally low calcium concentrations. This single molecular defect produces a dual-organ pathophysiology: in the parathyroid glands the over-active receptor inappropriately suppresses parathyroid hormone (PTH) secretion, producing **hypocalcemia with inappropriately low/normal PTH**; in the kidney the over-active receptor drives **hypercalciuria** and impairs urinary concentration. The result is a characteristic biochemical signature of low serum calcium, high phosphate, low-normal magnesium, low PTH, and relative-to-frank hypercalciuria.

Clinically, ADH1 spans a wide severity spectrum, from asymptomatic individuals detected on family screening to neonates and children presenting with **seizures, tetany, carpopedal spasm, and paresthesias**. Long-term complications are dominated by **renal disease (nephrocalcinosis, nephrolithiasis, progressive chronic kidney disease)**, along with basal ganglia calcification, early cataracts, and cardiac QT prolongation. The central therapeutic dilemma is that conventional treatment (oral calcium plus active vitamin D) corrects hypocalcemia but **worsens hypercalciuria and accelerates renal damage** — so the guiding principle is to relieve symptoms while keeping serum calcium at the *low end of normal*, with thiazide diuretics as a useful adjunct.

The field is advancing toward **mechanism-matched targeted therapy**: calcilytics (negative allosteric CaSR modulators such as NPSP795/SHP635 and encaleret) have raised PTH and serum calcium in ADH1 patients and mouse models, and PTH-replacement approaches (palopegteriparatide) have rescued refractory pediatric cases. The **Nuf mouse** (*Casr* p.Leu723Gln) is the principal, faithful animal model. As an autosomal dominant disorder with 50% transmission risk (plus frequent de novo and mosaic events), prevention rests on genetic counseling, cascade testing, and reproductive genetic options. This report synthesizes 11 confirmed findings across 35 reviewed papers into a comprehensive knowledge-base entry.

---

## Key Findings

### Finding 1 — Genetic cause: heterozygous activating *CASR* mutations

ADH1 is caused by **heterozygous gain-of-function (activating) missense variants in *CASR***. More than 400 germline CASR mutations (both loss- and gain-of-function) have been catalogued across the spectrum of calcium homeostasis disorders. In ADH1 specifically, the activating variants lower the EC50 for calcium-dependent G-protein activation, producing a left-shifted set-point so the receptor signals as if calcium is high even when it is low or normal. Inheritance is autosomal dominant, and **de novo variants are common** (e.g., p.Leu723Arg, p.Leu123Ser). ADH1 is molecularly distinct from ADH2, caused by gain-of-function variants in *GNA11* (encoding Gα11, the CaSR's signaling partner).

> "Autosomal dominant hypocalcemia (ADH) is due to enhanced calcium-dependent signaling caused by heterozygous gain-of-function (GOF) variants in the CASR gene (ADH1) or in the GNA11 gene, encoding Gα11 (ADH2)." — [PMID: 39658204](https://pubmed.ncbi.nlm.nih.gov/39658204/)

> "It is caused by the activating mutations of the calcium-sensing receptor gene (CASR), which produces a left-shift in the set point for extracellular calcium." — [PMID: 34160437](https://pubmed.ncbi.nlm.nih.gov/34160437/)

> "the identification of >400 different germline loss- and gain-of-function CaSR mutations that give rise to disorders of Ca2+ homeostasis" — [PMID: 31189130](https://pubmed.ncbi.nlm.nih.gov/31189130/)

### Finding 2 — Biochemical and clinical phenotype

The cardinal biochemistry of ADH1 is **hypocalcemia** (e.g., serum calcium 1.53–1.85 mmol/L), **inappropriately low/normal PTH**, **hyperphosphatemia**, **hypomagnesemia**, and **relative-to-frank hypercalciuria**. Clinical features include neuromuscular irritability (paresthesias, carpopedal spasm, tetany) and **seizures**, which are frequently the presenting feature in infancy and childhood. Complications include **nephrocalcinosis/nephrolithiasis, basal ganglia calcification, and early cataracts**. A key feature is **variable expressivity**: symptom severity is not tightly correlated with the degree of hypocalcemia. A severe subset manifests a **Bartter-like (type V) salt-wasting phenotype**.

> "Affected members had hypocalcaemia (1.53-1.85 mmol/l), hypercalciuria, low but detectable parathyroid hormone (PTH) and hypomagnesaemia. Four of seven affected individuals were symptomatic (seizures, abdominal pains and paraesthesias), unrelated to severity of hypocalcaemia. Additional complications include nephrocalcinosis (n = 3) and basal ganglia calcification" — [PMID: 16128246](https://pubmed.ncbi.nlm.nih.gov/16128246/)

> "presented with hypocalcemia, recurrent tetany, seizures, hypercalciuria, nephrocalcinosis, basal ganglia calcifications, and early-onset cataracts" — [PMID: 42388864](https://pubmed.ncbi.nlm.nih.gov/42388864/)

> "Clinical manifestations of the index case started with seizures at 14 months of age; cognitive impairment and several neuropsychological disabilities were noted during childhood. Extrapyramidal signs and basal ganglia calcification developed later" — [PMID: 27617113](https://pubmed.ncbi.nlm.nih.gov/27617113/)

**Suggested HPO terms:** Hypocalcemia (HP:0002901), Hypoparathyroidism (HP:0000829), Hyperphosphatemia (HP:0002905), Hypomagnesemia (HP:0002917), Hypercalciuria (HP:0002150), Seizure (HP:0001250), Tetany (HP:0001281), Paresthesia (HP:0003401), Nephrocalcinosis (HP:0000121), Nephrolithiasis (HP:0000787), Basal ganglia calcification (HP:0002135), Cataract (HP:0000518), Prolonged QT interval (HP:0001657).

### Finding 3 — The therapeutic dilemma and emerging targeted therapies

Standard-of-care treatment (oral calcium plus active vitamin D — calcitriol or alfacalcidol) corrects hypocalcemia but **exacerbates hypercalciuria**, promoting nephrocalcinosis and renal impairment. Cautious ("judicious") dosing is therefore recommended. Targeted therapy is emerging on two fronts: **calcilytics** (negative allosteric CaSR modulators) — NPSP795/SHP635 raised PTH and serum calcium in five ADH1 adults, and JTT-305 reversed renal AQP2 downregulation in CaSR knock-in mice; encaleret is in clinical development. **PTH-replacement** approaches (palopegteriparatide) resolved symptoms and lowered the calcium-phosphate product in a refractory pediatric case.

> "Calcilytics are negative allosteric modulators of the extracellular calcium receptor (CaR) and therefore may have therapeutic benefits in ADH1. Five adults with ADH1 due to four distinct CAR mutations received escalating doses of the calcilytic compound NPSP795 (SHP635)" — [PMID: 31063613](https://pubmed.ncbi.nlm.nih.gov/31063613/)

> "In vivo treatment of KI mice with the calcilytic JTT-305, a CaSR antagonist, increased AQP2 expression and reduced AQP2-targeting miRNA137 levels in KI mice." — [PMID: 38367250](https://pubmed.ncbi.nlm.nih.gov/38367250/)

> "Optimal management of ADHH is difficult and we recommend judicious treatment to avoid an increased risk of nephrocalcinosis." — [PMID: 16128246](https://pubmed.ncbi.nlm.nih.gov/16128246/)

**Suggested NCIT terms:** Calcium (C332), Calcitriol (C376), Vitamin D (C902), Thiazide Diuretic (C29713), Parathyroid Hormone (C2354).

### Finding 4 — The Nuf mouse: the principal animal model

The **Nuf mouse** carries a germline gain-of-function *Casr* (Gprc2a) missense mutation **Leu723Gln** (chromosome 16), which lowers the receptor EC50. Both heterozygous and homozygous mice display **hypocalcemia, hyperphosphatemia, inappropriately low PTH, ectopic/soft-tissue calcification, and nuclear cataracts** — faithfully mirroring human ADH1. The model also revealed additional CaSR-dependent phenotypes, including impaired glucose tolerance and insulin secretion (hyperglycemia) that is rectified by calcilytics. Calcilytics (NPS 2143, NPSP795, and quinazolinones ATF936/AXT914) raise PTH and plasma calcium in Nuf mice; oral AXT914 raised PTH from 23±4 to 104±29 pmol/L (p<0.05).

> "Nuf mice also display ectopic calcification, hypocalcemia, hyperphosphatemia, and inappropriately reduced levels of plasma parathyroid hormone. These features are similar to those observed in patients with autosomal dominant hypocalcemia." — [PMID: 15347804](https://pubmed.ncbi.nlm.nih.gov/15347804/)

> "Oral administration of 10 mg/kg AXT914 to Nuf mice increased parathyroid hormone to 104 ± 29 pmol/l compared with 23 ± 4 pmol/l for vehicle-treated mice, p < 0.05" — [PMID: 40086735](https://pubmed.ncbi.nlm.nih.gov/40086735/)

> "Heterozygous- (CasrNuf/+) and homozygous-affected (CasrNuf/Nuf) mice were shown to have hypocalcemia in association with impaired glucose tolerance and insulin secretion." — [PMID: 28575322](https://pubmed.ncbi.nlm.nih.gov/28575322/)

### Finding 5 — Dual-organ pathophysiology

Activated CaSR in **parathyroid chief cells** suppresses PTH secretion at a lowered set-point, producing hypocalcemia with inappropriately low PTH. In the **kidney**, CaSR overactivity in the thick ascending limb and distal nephron independently increases urinary calcium excretion (hypercalciuria) via **Claudin-14 (Cldn14) upregulation**, and in the **collecting duct** impairs the vasopressin–AQP2 axis. CaSR knock-in mice show reduced AQP2 with increased AQP2 phosphorylation at Ser261 through a **p38MAPK–ATF1–miR137 pathway**, contributing to a urinary concentrating/Bartter-like tendency. The calcilytic JTT-305 reversed this AQP2 downregulation, confirming the mechanism is receptor-driven.

> "CaSR knock-in (KI) mice mimicking autosomal dominant hypocalcaemia, display a significant decrease in the total content of AQP2 associated with significantly higher levels of AQP2 phosphorylation at Ser261" — [PMID: 38367250](https://pubmed.ncbi.nlm.nih.gov/38367250/)

> "Our findings suggest that parathyroid CaSR overactivity can reduce plasma Ca" — [PMID: 35313217](https://pubmed.ncbi.nlm.nih.gov/35313217/)

**Suggested GO/CL/UBERON terms:** GO:0007200 (phospholipase C-activating GPCR signaling), GO:0055074 (calcium ion homeostasis), GO:0038066 (p38 MAPK cascade), CL:0000446 (parathyroid chief cell), CL:1000456 (kidney collecting duct principal cell), UBERON:0001132 (parathyroid gland), UBERON:0002113 (kidney).

### Finding 6 — Diagnostic approach

Diagnosis rests on **biochemistry plus *CASR* sequencing**. The workup includes serum calcium (low), phosphate (high), magnesium (often low), and PTH (inappropriately low/normal), plus a 24-hour urinary calcium showing relative/frank hypercalciuria. ADH1 is confirmed by identifying a heterozygous activating *CASR* variant (single-gene test or hypoparathyroidism/mineral gene panel; WES/WGS in undiagnosed cases). Monogenic causes account for only ~5–10% of hypoparathyroidism, so genetic testing is targeted to clinically suspicious cases. **Thiazide diuretics** enhance renal calcium reabsorption and are of particular benefit in patients with activating CaSR mutations. ADH1 must be distinguished from other hypoparathyroidism etiologies (postsurgical, autoimmune, DiGeorge/22q11 deletion).

> "thiazide diuretics are of value as they enhance renal calcium reabsorption and increase serum calcium and are of particular benefit in those with activating mutations of the calcium-sensing receptor" — [PMID: 22863393](https://pubmed.ncbi.nlm.nih.gov/22863393/)

> "which have a monogenic aetiology in 5%-10% of cases" — [PMID: 34935164](https://pubmed.ncbi.nlm.nih.gov/34935164/)

> "Genetic testing forms an important tool in the investigation of PHPT and HP patients and is usually reserved for those deemed to be an increased risk of a monogenic disorder." — [PMID: 34935164](https://pubmed.ncbi.nlm.nih.gov/34935164/)

### Finding 7 — CaSR structure and biased signaling

CaSR (UniProt **P41180**) is a class C G-protein-coupled receptor functioning as a **homodimer** with a large Venus flytrap extracellular domain (ECD), a cysteine-rich domain, and a 7-transmembrane domain (TMD). Five cryo-EM structures of near-full-length CaSR show how Ca2+/agonist binding in the ECD is transmitted to the TMD to activate G proteins (Gq/11, Gi), and how allosteric modulators tune this. Activating ADH1 mutations map to regions important for structural integrity, dimerization, and ligand binding; a **TMD "hotspot" (e.g., residue 723)** is also the common calcilytic-binding pocket. Some variants produce **biased signaling** — the de novo p.Leu723Arg variant selectively lowers the EC50 for Gα11 activation without affecting Gi/Gq/Gs.

> "five cryo-EM structures of the near full-length CaSR have been published, demonstrating how agonist-binding transmits changes in the CaSR extracellular domain to the transmembrane region to activate G proteins, and how allosteric modulators affect these structural dynamics" — [PMID: 36707151](https://pubmed.ncbi.nlm.nih.gov/36707151/)

> "the study of disease-causing mutations has demonstrated that CaSR signals in a biased manner" — [PMID: 31189130](https://pubmed.ncbi.nlm.nih.gov/31189130/)

> "the Leu723Arg variant was normally expressed but resulted in a significantly lower EC50 for extracellular calcium activation of G11 but not other G proteins" — [PMID: 39658204](https://pubmed.ncbi.nlm.nih.gov/39658204/)

> "bind at a common region within the CaSR transmembrane domain, which is also an ADH1 mutational hotspot" — [PMID: 40086735](https://pubmed.ncbi.nlm.nih.gov/40086735/)

### Finding 8 — Nosology, identifiers, and inheritance

ADH1 identifiers: **OMIM #601198**; gene *CASR* (*601199, HGNC:1514, 3q13.33); Orphanet **ORPHA:428** ("autosomal dominant hypocalcemia"); **MONDO:0008833**; MeSH via "Hypocalcemia"/"Receptors, Calcium-Sensing". **Synonyms:** hypocalcemia autosomal dominant; hypoparathyroidism, familial isolated, autosomal dominant; ADHH (autosomal dominant hypocalcemia with hypercalciuria); familial/sporadic isolated hypoparathyroidism; Bartter syndrome type V (severe subset). **Inheritance:** autosomal dominant with frequent de novo mutations; **germline/gonadal mosaicism** has been reported (asymptomatic transmitting parent), producing variable/incomplete expressivity within families. ADH accounts for the majority of genetic isolated hypoparathyroidism; ADH1 (CASR) is far more common than ADH2 (GNA11). ADH2 (OMIM #615361) is caused by gain-of-function *GNA11* mutations and is associated with **short stature in ~42%** and less consistent hypercalciuria — a key distinguishing feature.

> "ADH1 patients typically manifest hypercalciuria, while ADH2 is associated with short stature in approximately 42% of cases." — [PMID: 39658204](https://pubmed.ncbi.nlm.nih.gov/39658204/)

> "autosomal dominant hypocalcemia type 2 (ADH2) are due to loss- and gain-of-function mutations, respectively, of the GNA11 gene that encodes the G protein subunit Gα11, a signaling partner of the calcium-sensing receptor (CaSR)" — [PMID: 36970776](https://pubmed.ncbi.nlm.nih.gov/36970776/)

> "Sequencing analysis in the mother suggested mosaicism for the same variant, and she was clinically and biochemically unaffected." — [PMID: 27617113](https://pubmed.ncbi.nlm.nih.gov/27617113/)

### Finding 9 — Variable onset, allelic spectrum, and phenocopies

Onset is **highly variable**: ADH may be asymptomatic (detected on family screening or incidental hypocalcemia) or present with seizures in the neonatal period, childhood, or adulthood; severe neonatal cases require IV calcium (e.g., de novo p.Glu228Lys). *CASR* is a single locus with a **graded allelic spectrum**: heterozygous loss-of-function → familial hypocalciuric hypercalcemia (FHH1); homozygous LOF → neonatal severe hyperparathyroidism (NSHPT); heterozygous gain-of-function → ADH1. A common polymorphism **Ala986Ser (A986S)** in the intracellular tail modestly influences serum calcium and can act as a modifier. Acquired **activating anti-CaSR autoantibodies** produce an autoimmune ADH phenocopy (an important differential). Drug interactions matter clinically: phenobarbital accelerates 1-alfacalcidol metabolism, causing swings between hypo- and hypercalcemia.

> "Heterozygous activating mutations of the CASR cause autosomal dominant hypocalcemia (ADH) that may be asymptomatic or present with seizures in the neonatal period or childhood or later in life. Phenocopies of FHH or ADH are due to circulating CASR inactivating or activating autoantibodies, respectively." — [PMID: 20374733](https://pubmed.ncbi.nlm.nih.gov/20374733/)

> "A common polymorphism in the intracellular tail of the CASR, Ala to Ser at position 986, has a modest effect on the serum calcium concentration in healthy individuals." — [PMID: 11013439](https://pubmed.ncbi.nlm.nih.gov/11013439/)

> "The child presented in the neonatal period with clinical seizures associated with severe hypocalcaemia, hyperphosphataemia, low parathyroid hormone levels and elevated urine calcium:creatinine ratios." — [PMID: 25227206](https://pubmed.ncbi.nlm.nih.gov/25227206/)

### Finding 10 — Prognosis: normal life expectancy but chronic renal morbidity

ADH1 is a **chronic, lifelong disorder with generally good survival**, but morbidity is driven by **renal complications**, amplified by both the intrinsic hypercalciuria and by conventional calcium/active-vitamin-D therapy. A systematic review of chronic hypoparathyroidism on conventional therapy reports nephrolithiasis rates up to 36% and nephrocalcinosis up to 38%, with progression to renal insufficiency/CKD. Additional complications include hypocalcemic seizures, basal ganglia (and other ectopic) calcification, cataracts, and QT-prolongation risk. Postsurgical chronic hypoparathyroidism cohorts show elevated renal disease (moderate-to-severe 28.8% vs 5.6%), nephrocalcinosis (59.9% vs 0.6%), and higher mortality (HR ~2.75) versus controls — underscoring the renal/cardiovascular burden of the hypoparathyroid state that ADH1 shares and exacerbates.

> "The reported rate of nephrolithiasis was up to 36%, with the lowest rates in studies reporting shorter duration of disease. The rate of nephrocalcinosis was up to 38%." — [PMID: 33599907](https://pubmed.ncbi.nlm.nih.gov/33599907/)

> "a higher prevalence of moderate-to-severe renal disease (28.8% vs. 5.6%), nephrocalcinosis (59.9% vs. 0.6%), and nephrolithiasis (8.3% vs. 1.0%). They also had significantly greater mortality (hazard ratio [HR] 2.75)" — [PMID: 40531442](https://pubmed.ncbi.nlm.nih.gov/40531442/)

### Finding 11 — Management principles and prevention

Because overtreatment drives renal damage, the guiding therapeutic principle is to **relieve symptoms while keeping serum calcium at the low end of normal**, using thiazides to blunt hypercalciuria. Human proof-of-concept for mechanism-matched therapy: the calcilytic NPSP795/SHP635 increased PTH in ADH1 patients, and in-vitro assays show variant-specific responsiveness (supporting genotype-guided calcilytic selection); PTH-based therapy (palopegteriparatide) rescued a refractory pediatric case. **Prevention is exclusively at the reproductive/clinical level**: as an autosomal dominant disorder, each child of an affected parent has a 50% risk; de novo and mosaic events mean absence of family history does not exclude risk. Preventive tools are genetic counseling, cascade testing of relatives, and prenatal/preimplantation genetic testing for a known familial *CASR* variant. No population-based primary prevention exists.

> "Calcilytics are negative allosteric modulators of the extracellular calcium receptor (CaR) and therefore may have therapeutic benefits in ADH1." — [PMID: 31063613](https://pubmed.ncbi.nlm.nih.gov/31063613/)

> "also to allow the identification of other family members who may be at risk of disease" — [PMID: 34935164](https://pubmed.ncbi.nlm.nih.gov/34935164/)

---

## Mechanistic Model / Interpretation

ADH1 is fundamentally a **single-gene, gain-of-function signalopathy** with a two-organ output. The causal chain:

```
    Heterozygous activating CASR missense variant (e.g., L723Q, R205C, E228K)
                              │
                 Left-shifted Ca2+ set-point (↓ EC50 for Ca2+)
                              │
          Receptor "reads" normal/low Ca2+ as if it were HIGH
                 ┌────────────┴──────────────┐
                 ▼                            ▼
       PARATHYROID GLAND                  KIDNEY
    (chief cells, CL:0000446)     (TAL + distal nephron + CD)
                 │                            │
      ↓ PTH secretion            ↑ Cldn14 → ↑ urinary Ca2+ excretion
      (inappropriately low)      ↓ AQP2 (p38MAPK-ATF1-miR137)
                 │                            │
                 ▼                            ▼
      HYPOCALCEMIA               HYPERCALCIURIA + urine-concentration defect
      Hyperphosphatemia          (Bartter-like tendency in severe subset)
                 │                            │
                 └────────────┬───────────────┘
                              ▼
       CLINICAL: seizures, tetany, paresthesias (acute);
       nephrocalcinosis, nephrolithiasis, CKD, basal ganglia
       calcification, cataracts, QT prolongation (chronic)
```

**Upstream vs downstream:** The upstream driver is the mutant receptor's shifted set-point. The parathyroid PTH suppression and renal calcium-wasting are **parallel, independent downstream arms** — a critical insight because it explains why simply raising serum calcium (which further activates the already over-sensitive renal receptor) worsens hypercalciuria. This is the mechanistic root of the treatment dilemma.

**Why calcilytics work:** By binding the TMD allosteric pocket (which coincides with the ADH1 mutational hotspot around residue 723), calcilytics raise the receptor's EC50 back toward normal, de-repressing PTH and reducing renal calcium wasting simultaneously — addressing both arms at their common origin rather than downstream.

**Comparative nosology of *CASR* dosage:**

| Genotype | Receptor activity | Disorder | Calcium phenotype |
|---|---|---|---|
| Heterozygous LOF | ↓ | FHH1 (familial hypocalciuric hypercalcemia) | High Ca, low urine Ca |
| Homozygous LOF | ↓↓ | NSHPT (neonatal severe hyperparathyroidism) | Severe high Ca |
| Heterozygous GOF | ↑ | **ADH1** | Low Ca, high urine Ca |
| — (*GNA11* GOF) | ↑ (via Gα11) | ADH2 | Low Ca, short stature ~42% |

---

## Report by Template Section

### 1. Disease Information
Rare AD form of hypoparathyroidism from activating *CASR* variants; hypocalcemia with inappropriately low PTH and hypercalciuria. Identifiers: OMIM #601198 (gene *601199), ORPHA:428, MONDO:0008833, HGNC:1514, UniProt P41180; ICD-10 E20.8 / ICD-11 5A50.0 (no ADH1-specific code); MeSH under *Hypocalcemia* / *Receptors, Calcium-Sensing*. Synonyms: ADHH, familial isolated hypoparathyroidism (AD), Bartter syndrome type V (severe subset). Data are from aggregated disease-level resources plus published clinical case series/pedigrees.

### 2. Etiology
Primary cause is genetic/monogenic — heterozygous activating *CASR* missense variants (Finding 1). Genetic modifier: A986S (rs1801725) polymorphism. No environmental or infectious causation; environmental modifiers (dietary calcium/vitamin D, phenobarbital) alter severity only. Acquired activating anti-CaSR autoantibodies produce a phenocopy (differential, not etiology). No established protective alleles.

### 3. Phenotypes
See Finding 2 and the HPO list. Onset neonatal→adult; variable severity/expressivity; chronic lifelong course with episodic acute symptoms (seizures/tetany). QoL impacted by seizures, renal disease, and treatment burden; no ADH1-specific QoL instrument exists.

### 4. Genetic/Molecular Information
Causal gene *CASR* (3q13.33). Variant class predominantly heterozygous missense, gain-of-function; TMD hotspot (residue 723); some biased-signaling variants (Findings 1, 7). Classification: functionally validated activating variants are Pathogenic/Likely Pathogenic; novel variants often require in-vitro Ca2+-response assays. Allele frequency: private/rare, essentially absent in gnomAD; many de novo. Germline (with mosaicism reported). Modifier: A986S. No characteristic epigenetic or chromosomal abnormalities.

### 5. Environmental Information
Not causal. Modifiers of expression only: dietary calcium/vitamin D status; enzyme-inducing drugs (phenobarbital) that alter vitamin-D-analog metabolism. No infectious agents.

### 6. Mechanism/Pathophysiology
See Mechanistic Model and Finding 5. Pathways: Gq/11–PLC and Gi signaling, p38MAPK–ATF1–miR137 (renal AQP2), Cldn14-mediated renal calcium handling. Protein dysfunction: class C GPCR homodimer biased toward active state (Finding 7). CHEBI: calcium(2+) (CHEBI:29108), phosphate (CHEBI:43474). Immune involvement: none intrinsic.

### 7. Anatomical Structures Affected
Primary: parathyroid gland (UBERON:0001132), kidney/nephron (UBERON:0002113). Secondary: basal ganglia (UBERON:0002420), ocular lens (UBERON:0000965), soft tissue (ectopic calcification), heart (functional QT). Cells: parathyroid chief cell (CL:0000446), collecting-duct principal cell (CL:1000456), TAL epithelium. Subcellular: plasma membrane (GO:0005886), ER (trafficking). Lateralization: systemic/bilateral. Systems: endocrine, renal/urinary, nervous, cardiac electrophysiology.

### 8. Temporal Development
Onset congenital/neonatal → adult, or asymptomatic. Pattern chronic/insidious with acute symptomatic episodes. Course lifelong; renal complications slowly progressive. Critical periods: neonatal seizure risk; intercurrent illness, pregnancy, and medication changes; early diagnosis is the key intervention window to avoid overtreatment-related renal damage.

### 9. Inheritance and Population
Autosomal dominant; frequent de novo; germline/gonadal mosaicism reported (Finding 8). High biochemical penetrance, variable symptomatic expressivity; negative family history does not exclude ADH1. No anticipation, founder effect, or consanguinity role in the classic sense. Epidemiology: rare; precise prevalence not established; ADH is the most common genetic cause of isolated hypoparathyroidism; monogenic causes ~5–10% of all hypoparathyroidism; ADH1 >> ADH2. No strong sex or geographic predilection.

### 10. Diagnostics
Biochemistry: low Ca, high phosphate, low/normal PTH, often low Mg, high urine Ca (24-h or Ca:creatinine). Imaging: renal ultrasound, brain CT, ECG (QTc); slit-lamp for cataract. Genetic testing: single-gene *CASR* sequencing or hypoparathyroidism/mineral panel; WES/WGS if undiagnosed; functional assays for VUS. Diagnostic clue: hypoparathyroidism *with* hypercalciuria. Differential: postsurgical, autoimmune (incl. anti-CaSR autoantibody phenocopy), 22q11.2 deletion, hypomagnesemia-related, pseudohypoparathyroidism, vitamin D disorders, ADH2 (*GNA11*). Screening: cascade genetic testing; prenatal/PGT for a known variant; no population newborn screening.

### 11. Outcome/Prognosis
Near-normal life expectancy with treatment; dominant morbidity is renal (nephrocalcinosis up to ~38%, nephrolithiasis up to ~36%, progression to CKD), amplified by intrinsic hypercalciuria and overtreatment (Finding 10). Other complications: seizures, ectopic/basal ganglia calcification, cataracts, QT prolongation. Prognostic factors: cumulative urinary calcium load, treatment approach, disease duration. Established nephrocalcinosis/CKD is not fully reversible — prevention is key.

### 12. Treatment
Conventional: oral calcium + active vitamin D (calcitriol/alfacalcidol), targeting low-normal serum calcium with judicious dosing; thiazide diuretics (of particular benefit in activating-CaSR patients); magnesium repletion. Targeted: calcilytics (NPSP795/SHP635, NPS 2143, ATF936/AXT914, encaleret) and PTH-replacement (palopegteriparatide, recombinant PTH) (Finding 3). Pharmacogenomics: avoid enzyme inducers (phenobarbital). No approved gene/cell/RNA therapy; surgery not applicable. Personalized medicine: in-vitro variant response can guide calcilytic vs PTH-based choice. NCIT terms listed in Finding 3.

### 13. Prevention
Primary prevention not possible (germline). Genetic counseling (AD, 50% offspring risk; de novo/mosaicism caveats) and reproductive options (PGT/prenatal testing) are the main tools. Secondary: cascade testing and early biochemical surveillance of relatives. Tertiary (most important): avoid overtreatment, maintain low-normal calcium, monitor 24-h urine calcium and renal imaging, use thiazides/calcilytics/PTH to prevent nephrocalcinosis/CKD. Immunization/public-health/environmental interventions not applicable.

### 14. Other Species / Natural Disease
Taxonomy: *Homo sapiens* (NCBI:txid9606); modeled in *Mus musculus* (NCBI:txid10090). No notable naturally occurring ADH1 in companion animals/wildlife documented. Ortholog: mouse *Casr* (historically *Gprc2a*); receptor and its Ca2+-homeostasis role are evolutionarily conserved, so mechanisms translate well to mouse models. Zoonosis/transmission: not applicable.

### 15. Model Organisms
Principal model — the Nuf mouse (*Casr* p.Leu723Gln; Finding 4): AD gain-of-function; recapitulates hypocalcemia, hyperphosphatemia, low PTH, ectopic calcification, and cataracts; plus impaired glucose tolerance. CaSR knock-in mice dissect renal AQP2/vasopressin pathology. Cellular/in-vitro: HEK293 expressing WT vs mutant CaSR for intracellular-Ca2+/BRET assays and calcilytic docking. Applications: validating calcilytics, studying biased signaling, renal/pancreatic CaSR biology. Limitations: mouse mineral set-points/lifespan differ; neurological (basal ganglia calcification) features less emphasized. Resource: MGI (mouse *Casr*).

---

## Evidence Base

| PMID | Title (abbreviated) | Supports finding(s) | Evidence type |
|---|---|---|---|
| [39658204](https://pubmed.ncbi.nlm.nih.gov/39658204/) | Activating CaSR variant with biased signaling | F1, F7, F8 | Human genetics + in vitro |
| [31189130](https://pubmed.ncbi.nlm.nih.gov/31189130/) | CaSR mutation review | F1, F7 | Review |
| [34160437](https://pubmed.ncbi.nlm.nih.gov/34160437/) | p.Arg205Cys ADH1 pedigree | F1 | Human clinical |
| [16128246](https://pubmed.ncbi.nlm.nih.gov/16128246/) | ADHH family, treatment challenges | F2, F3, F10, F11 | Human clinical |
| [42388864](https://pubmed.ncbi.nlm.nih.gov/42388864/) | Palopegteriparatide pediatric ADH1 | F2, F3 | Human clinical case |
| [27617113](https://pubmed.ncbi.nlm.nih.gov/27617113/) | Novel p.Leu123Ser + mosaicism | F2, F8 | Human clinical |
| [31063613](https://pubmed.ncbi.nlm.nih.gov/31063613/) | Calcilytic NPSP795 in ADH1 patients | F3, F11 | Human clinical trial |
| [38367250](https://pubmed.ncbi.nlm.nih.gov/38367250/) | Calcilytic reverses renal AQP2 defect | F3, F5 | Model organism (KI mouse) |
| [15347804](https://pubmed.ncbi.nlm.nih.gov/15347804/) | Nuf mouse cataracts + calcification | F4 | Model organism |
| [40086735](https://pubmed.ncbi.nlm.nih.gov/40086735/) | Quinazolinone calcilytic in Nuf mice | F4, F7 | Model organism |
| [28575322](https://pubmed.ncbi.nlm.nih.gov/28575322/) | Nuf mice hyperglycemia | F4 | Model organism |
| [35313217](https://pubmed.ncbi.nlm.nih.gov/35313217/) | Parathyroid vs kidney CaSR contributions | F5 | Model organism |
| [22863393](https://pubmed.ncbi.nlm.nih.gov/22863393/) | Hypoparathyroidism review (thiazides) | F6 | Review |
| [34935164](https://pubmed.ncbi.nlm.nih.gov/34935164/) | Genetics of calcium/bone disorders | F6, F11 | Review |
| [36707151](https://pubmed.ncbi.nlm.nih.gov/36707151/) | CaSR cryo-EM structures | F7 | Structural/computational |
| [36970776](https://pubmed.ncbi.nlm.nih.gov/36970776/) | GNA11 variants (ADH2) | F8 | Human genetics |
| [20374733](https://pubmed.ncbi.nlm.nih.gov/20374733/) | CaSR-associated diseases + autoantibodies | F9 | Review |
| [11013439](https://pubmed.ncbi.nlm.nih.gov/11013439/) | CASR mutation spectrum + A986S | F9 | Human genetics |
| [25227206](https://pubmed.ncbi.nlm.nih.gov/25227206/) | Neonatal ADH1 + phenobarbital interaction | F9 | Human clinical |
| [33599907](https://pubmed.ncbi.nlm.nih.gov/33599907/) | Renal complications systematic review | F10 | Systematic review |
| [40531442](https://pubmed.ncbi.nlm.nih.gov/40531442/) | Postsurgical hypoparathyroidism outcomes | F10 | Retrospective cohort |

The evidence base is coherent and mutually reinforcing across human clinical, human genetics, model organism, and structural/computational domains. Human genetic studies establish causation (activating *CASR* variants), the Nuf mouse and CaSR knock-in models provide mechanistic validation and pharmacological proof-of-concept, cryo-EM structures rationalize where mutations and calcilytics act, and clinical/registry studies define the phenotype, therapeutic dilemma, and prognosis. No paper in the reviewed set contradicts the central model.

---

## Supported vs Refuted Hypotheses

**Supported (evidence-backed):**
1. ADH1 = heterozygous activating *CASR* variants, left-shifted Ca2+ set-point (gain of function) [PMID 39658204; 34160437].
2. Phenotype = hypocalcemia + inappropriately low PTH + hypercalciuria + calcification complications [PMID 16128246].
3. Dual parathyroid + renal CaSR overactivity explains hypocalcemia **with** hypercalciuria; renal AQP2 pathway involved [PMID 35313217; 38367250].
4. Calcilytics are mechanism-matched therapy (human n=5 + mouse) [PMID 31063613; 40086735].
5. Nuf mouse faithfully models the disease [PMID 15347804].

**Refuted / not applicable:** environmental or infectious causation; loss-of-function/misfolding mechanism (that is FHH/NSHPT); a role for population-based primary prevention.

---

## Limitations and Knowledge Gaps

1. **Epidemiology is poorly quantified.** No reliable population prevalence/incidence figures for ADH1 specifically; estimates are extrapolated from the broader hypoparathyroidism population (monogenic ~5–10%). Precise prevalence, incidence, sex ratio, and geographic/ethnic distribution remain gaps.
2. **Penetrance and expressivity are incompletely characterized.** Variable expressivity and mosaicism are documented, but formal penetrance estimates by variant are lacking.
3. **Genotype–phenotype correlations are limited.** Symptom severity is explicitly *not* tightly correlated with hypocalcemia degree; systematic variant-level correlation (including biased-signaling variants) is needed.
4. **Targeted therapy evidence is early-stage.** Calcilytic human data are limited (n=5 for NPSP795) and PTH-replacement evidence is a single pediatric case. Long-term renal-protective outcomes are not yet established.
5. **Quality-of-life data are essentially absent** — no EQ-5D/SF-36/PROMIS data specific to ADH1.
6. **Cross-species natural disease** beyond engineered mouse models is not documented.

---

## Proposed Follow-up Experiments / Actions

1. **Assemble a natural-history registry** for ADH1 to quantify prevalence, penetrance, age-of-onset distribution, and long-term renal/neurological outcomes, stratified by variant.
2. **Systematic variant-function mapping:** couple in-vitro Gq/11/Gi signaling assays with clinical severity to build a genotype–phenotype and calcilytic-responsiveness atlas guiding personalized therapy.
3. **Complete calcilytic clinical development** (e.g., encaleret) with renal endpoints (24-h urine calcium, GFR trajectory, nephrocalcinosis imaging) as primary outcomes, not just PTH/serum calcium.
4. **Head-to-head comparison** of thiazide + conventional therapy vs calcilytic vs PTH-replacement (palopegteriparatide) on renal protection in ADH1.
5. **Prospective QoL assessment** using validated instruments to capture disease and treatment burden.
6. **Mechanistic follow-up on the renal AQP2/Cldn14 axis** in patient-derived models (e.g., iPSC-derived kidney organoids carrying ADH1 variants) to validate the p38MAPK–ATF1–miR137 pathway in human cells.

---

*Report compiled from 11 confirmed findings across 35 reviewed papers over 5 investigation iterations. Evidence spans human clinical, human genetics, model organism (Nuf/knock-in mouse), and structural/computational sources. PMIDs cited inline.*


## Artifacts

- [OpenScientist final report](Autosomal_Dominant_Hypocalcemia_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Autosomal_Dominant_Hypocalcemia_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 31 |
| Quoted claims found in source | 29 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 21 |
| On topic | 17 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:31189130` *(abstract only)*: "the identification of >400 different germline loss- and gain-of-function CaSR mutations that give rise to disorders of Ca2+ homeostasis"
  - closest text in source: "The importance of the CaSR in the regulation of Ca2+ e has been highlighted by the identification of >400 different germline loss- and gain-of-function CaSR mutations that give rise to disorders of Ca2+ e homeostasis"
- `PMID:40531442` *(abstract only)*: "a higher prevalence of moderate-to-severe renal disease (28.8% vs. 5.6%), nephrocalcinosis (59.9% vs. 0.6%), and nephrolithiasis (8.3% vs. 1.0%). They also had significantly greater mortality (hazard ratio [HR] 2.75)"
  - closest text in source: "a higher prevalence of moderate-to-severe renal disease (28.8% vs. 5.6%), nephrocalcinosis (59.9% vs. 0.6%), and nephrolithiasis (8.3% vs. 1.0%). They also had significantly greater mortality (hazard ratio [HR] 2.75)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 7 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:1000456` (2 mentions) - the report calls it "kidney collecting duct principal cell"; CL calls it **mesothelial cell of parietal peritoneum**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007200` (1 mention) - the report calls it "phospholipase C-activating GPCR signaling"; GO calls it **phospholipase C-activating G protein-coupled receptor signaling pathway**, and lists "PLC-activating GPCR signaling pathway" among its other names
- `CL:0000446` (3 mentions) - the report calls it "parathyroid chief cell"; CL calls it **chief cell of parathyroid gland**, and lists "parathyroid chief cell" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.