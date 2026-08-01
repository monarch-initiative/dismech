---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T07:34:46.864203'
end_time: '2026-07-26T07:54:02.136849'
duration_seconds: 1155.27
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: arrhythmogenic right ventricular cardiomyopathy
  mondo_id: MONDO:0016587
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
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 59
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Arrhythmogenic_Right_Ventricular_Cardiomyopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Arrhythmogenic_Right_Ventricular_Cardiomyopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** arrhythmogenic right ventricular cardiomyopathy
- **MONDO ID:** MONDO:0016587 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **arrhythmogenic right ventricular cardiomyopathy** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Arrhythmogenic Right Ventricular Cardiomyopathy (ARVC) — Comprehensive Disease Characteristics Report

**Target disease:** Arrhythmogenic right ventricular cardiomyopathy
**MONDO ID:** MONDO:0016587 · **Category:** Mendelian (autosomal dominant, desmosomal)
**Investigation:** 5 iterations · 20 confirmed findings · 81 papers reviewed

---

## Summary

Arrhythmogenic right ventricular cardiomyopathy (ARVC) is an inherited myocardial disease defined by progressive **fibrofatty replacement** of the ventricular myocardium — classically the right ventricle — that creates an electrically unstable substrate producing ventricular arrhythmias, heart failure, and **sudden cardiac death (SCD)**, especially in young people and endurance athletes. It is fundamentally a **disease of the cardiac desmosome**: pathogenic loss-of-function variants in desmosomal genes account for the majority of cases, with *PKP2* (plakophilin-2) the single most common cause, followed by *DSP*, *DSG2*, *DSC2*, and *JUP*, plus important non-desmosomal causes including *TMEM43*, *PLN*, and *FLNC*. Desmosomal gene variants account for **67.4% of ARVC cases** in cohort studies and **96.1% of pathogenic variants** in ClinVar ([PMID: 42366226](https://pubmed.ncbi.nlm.nih.gov/42366226/)).

Mechanistically, destabilization of the intercalated disc triggers a convergent signaling cascade: activation of the **Hippo pathway** (Merlin/NF2 → MST1/2 → LATS1/2 → YAP phosphorylation), **suppression of canonical Wnt/β-catenin** signaling via nuclear plakoglobin/YAP–β-catenin sequestration, and engagement of **TGF-β signaling** — together driving a pro-adipogenic, pro-fibrotic transcriptional program. A shared, mutation-agnostic downstream feature is **downregulation of the gap-junction protein connexin-43 (Cx43)**, which contributes to arrhythmogenesis independent of the causal gene. Increasingly, ARVC is also recognized as an **inflammatory cardiomyopathy** with episodic "hot phases" that mimic myocarditis. The key environmental modifier is **endurance/high-intensity exercise**, which accelerates penetrance and arrhythmic risk in a dose-dependent manner and largely explains the observed male predominance.

Clinically, ARVC has a prevalence of **~1:2,000 to 1:5,000**, presents typically between the second and fourth decades of life, and is diagnosed by the multiparametric **2010 modified Task Force Criteria** and **2020 Padua criteria** integrating imaging, ECG, tissue, arrhythmia, and genetic data. Management is currently **palliative**: exercise restriction, beta-blockers and antiarrhythmics, catheter ablation, and ICD implantation guided by the 2019 ARVC risk calculator, with heart transplantation reserved for end-stage disease. A new generation of **AAV-based gene therapies** — *PKP2* gene replacement (LX2020) and mutation-agnostic Cx43 restoration — show strong preclinical efficacy and represent the first potentially disease-modifying treatments.

---

## 1. Disease Information

ARVC is an inherited cardiomyopathy characterized by progressive fibrofatty replacement of ventricular myocardium, ventricular arrhythmias, and increased sudden cardiac death risk. It was originally called **arrhythmogenic right ventricular dysplasia (ARVD)**, later broadened to **arrhythmogenic cardiomyopathy (ACM)** to encompass left-dominant and biventricular forms; the 2023 ESC guidelines reintroduced "ARVC" specifically for fibrofatty right ventricular disease while using "non-dilated left ventricular cardiomyopathy" for left-sided phenotypes ([PMID: 39980788](https://pubmed.ncbi.nlm.nih.gov/39980788/)).

**Key identifiers:**
- **MONDO:** MONDO:0016587
- **OMIM:** ARVD1 (107970, TGFB3), ARVD2 (600996, RYR2), ARVD5 (604400, TMEM43), ARVD8 (607450, DSP), ARVD9 (609040, PKP2), ARVD10 (610193, DSG2), ARVD11 (610476, DSC2), ARVD12 (611528, JUP)
- **Orphanet:** ORPHA:247
- **ICD-10:** I42.8 · **ICD-11:** BC43.3 · **MeSH:** D019571 (Arrhythmogenic Right Ventricular Dysplasia)

**Synonyms/alternative names:** arrhythmogenic right ventricular dysplasia (ARVD), arrhythmogenic right ventricular cardiomyopathy/dysplasia (ARVC/D), arrhythmogenic cardiomyopathy (ACM), right ventricular cardiomyopathy. Left-predominant forms are termed arrhythmogenic left ventricular cardiomyopathy (ALVC).

**Information source:** Data are derived from aggregated disease-level resources (OMIM, Orphanet, ClinVar), disease registries (Johns Hopkins ARVC Registry, Utrecht, SHaRe, Scandinavian cohorts), and clinical/pathology studies rather than individual EHR-level extraction.

---

## 2. Etiology

### Disease Causal Factors
The primary cause of ARVC is **genetic**, predominantly heterozygous loss-of-function variants in genes encoding the **cardiac desmosome** — the cell–cell adhesion junction of the intercalated disc. Desmosomal gene variants are predominant, "accounting for 67.4% of cases in cohort studies and 96.1% of pathogenic variants in ClinVar" ([PMID: 42366226](https://pubmed.ncbi.nlm.nih.gov/42366226/)). Non-desmosomal genetic causes include *TMEM43*, *PLN*, *FLNC*, *LMNA*, *SCN5A*, *DES*, and *RBM20* ([PMID: 34970070](https://pubmed.ncbi.nlm.nih.gov/34970070/)).

### Genetic Risk Factors
- **Causal genes:** *PKP2* (most common), *DSP*, *DSG2*, *DSC2*, *JUP*, *TMEM43*, *PLN*, *FLNC*.
- **Founder/high-penetrance variants:** *TMEM43* p.S358L (fully penetrant, Newfoundland founder); *PKP2* Q59L (Finnish founder, ~20% penetrance).
- **Modifier effect of multiple variants:** carriers of >1 mutation (~4%) have earlier VT/VF (28±12 yr) and worse outcomes ([PMID: 25616645](https://pubmed.ncbi.nlm.nih.gov/25616645/)).

### Environmental Risk Factors
- **Endurance/high-intensity exercise** is the dominant modifier: "intense exercise may accelerate the phenotypic expression and the propensity to ventricular arrhythmias in patients with ACM" ([PMID: 40470644](https://pubmed.ncbi.nlm.nih.gov/40470644/)).
- **Male sex** and **age** are associated with worse arrhythmic outcomes, but much of the sex effect is mediated by higher exercise dose in men ([PMID: 33829244](https://pubmed.ncbi.nlm.nih.gov/33829244/)).
- **Family history** of ARVC/SCD.

### Protective Factors
- **Exercise restriction** reduces arrhythmic risk and slows phenotypic progression — the primary modifiable protective intervention.
- No well-established protective genetic variants have been defined for ARVC. Non-carrier status among relatives in cascade screening is effectively protective.

### Gene–Environment Interactions
The exercise–genotype interaction is the paradigmatic GxE relationship in ARVC. Mechanical load from endurance exercise stresses an already compromised desmosome, accelerating fibrofatty remodeling and arrhythmia. In a longitudinal cohort, male sex marked arrhythmia risk (OR 2.6) but lost significance after adjusting for exercise dose, indicating exercise mediates much of the sex difference ([PMID: 33829244](https://pubmed.ncbi.nlm.nih.gov/33829244/)).

---

## 3. Phenotypes

ARVC symptoms typically emerge from the **second to fourth decade of life** ([PMID: 25894016](https://pubmed.ncbi.nlm.nih.gov/25894016/)). The disease is **progressive** and often **episodic** (with arrhythmic and inflammatory "hot phase" flares).

| Phenotype | Type | HPO term | Frequency / notes |
|-----------|------|----------|-------------------|
| Palpitations | Symptom | HP:0001962 | 57% in definite ARVC vs 17% non-definite ([PMID: 36635648](https://pubmed.ncbi.nlm.nih.gov/36635648/)) |
| Syncope | Symptom | HP:0001279 | 35% vs 6% ([PMID: 36635648](https://pubmed.ncbi.nlm.nih.gov/36635648/)) |
| Dyspnea | Symptom | HP:0002094 | 28% vs 5% (p<0.001) |
| Ventricular tachycardia | Clinical sign | HP:0004756 | LBBB morphology; common presenting arrhythmia |
| Ventricular fibrillation / SCD | Clinical sign | HP:0001663 / HP:0001645 | Cause of SCD in 29% of competitive athletes ([PMID: 42305082](https://pubmed.ncbi.nlm.nih.gov/42305082/)) |
| Premature ventricular contractions | Clinical sign | HP:0006682 | Very frequent (15/19 pediatric) |
| T-wave inversion V1–V3 | Lab/ECG abnormality | HP:0012251 (abnormal T wave) | Hallmark; all pediatric pts ≥14 yr ([PMID: 31375646](https://pubmed.ncbi.nlm.nih.gov/31375646/)) |
| Epsilon wave | Lab/ECG abnormality | — | Present only in definite group; 13/19 pediatric |
| Right ventricular dilatation/dysfunction | Physical manifestation | HP:0001707 / HP:0001654 | Structural criterion |
| Heart failure | Clinical sign | HP:0001635 | More common in DSP/DSG2 genotypes |

In a tertiary cohort, "patients in the definite group were more symptomatic, with palpitations (57% vs. 17%), syncope (35% vs. 6%) and shortness of breath (28% vs. 5%, p < 0.001). T-wave inversion in V1-V3 and epsilon waves were observed only in the definite group" ([PMID: 36635648](https://pubmed.ncbi.nlm.nih.gov/36635648/)).

**Severity/progression:** Variable and progressive; ranges from a "concealed phase" (arrhythmic risk without overt structure) to end-stage biventricular failure. In a Brazilian cohort, 5-year cumulative life-threatening arrhythmic event (LTAE) probability was 30% and HF-death/heart transplant 10% ([PMID: 36720007](https://pubmed.ncbi.nlm.nih.gov/36720007/)).

**Quality of life:** Impaired by arrhythmia burden, ICD shocks, exercise restriction (particularly affecting athletes), heart-failure symptoms, and the psychological burden of SCD risk and cascade family screening. Formal EQ-5D/SF-36 disease-specific data were not identified in this investigation.

---

## 4. Genetic / Molecular Information

### Causal Genes and Genotype–Phenotype Correlations

| Gene | HGNC / OMIM | Frequency & phenotype |
|------|-------------|------------------------|
| **PKP2** (plakophilin-2) | HGNC:9024 / 602861 | Most common (~50% in Polish cohort); truncating variants; younger diagnosis but **better prognosis** (higher LVEF, less HF) ([PMID: 34191271](https://pubmed.ncbi.nlm.nih.gov/34191271/)) |
| **DSG2** (desmoglein-2) | HGNC:3049 / 125671 | Higher risk of transplant/HF-related death vs PKP2 (log-rank P<0.001); more LV dysfunction ([PMID: 30790397](https://pubmed.ncbi.nlm.nih.gov/30790397/)) |
| **DSP** (desmoplakin) | HGNC:3052 / 125647 | >4-fold LV dysfunction (40%) and HF (13%) vs PKP2; left-dominant/biventricular; hot phases ([PMID: 25616645](https://pubmed.ncbi.nlm.nih.gov/25616645/)) |
| **DSC2** (desmocollin-2) | HGNC:3036 / 125645 | TCF7→TGF-β2 fibrosis pathway |
| **JUP** (plakoglobin) | HGNC:6207 / 173325 | Naxos disease (recessive, cardiocutaneous) |
| **TMEM43** | HGNC:28472 / 612048 | ARVD5; p.S358L fully penetrant founder; malignant |
| **PLN, FLNC, LMNA, SCN5A, DES, RBM20** | — | Non-desmosomal ACM; FLNC/LMNA/PLN high-risk for SCD |

### Variant Classification and Type
Variants are classified per ACMG/AMP guidelines (pathogenic, likely pathogenic, VUS). Most are **truncating/loss-of-function** (frameshift, nonsense, splice-site) — e.g., the *PKP2* spectrum reported "5 frameshift, 2 nonsense, 2 splicing, 1 missense variants" ([PMID: 34191271](https://pubmed.ncbi.nlm.nih.gov/34191271/)) — with important **missense** exceptions such as *TMEM43* p.S358L. NGS panels in inherited heart disease clinics carry high VUS rates (~54%) ([PMID: 39009076](https://pubmed.ncbi.nlm.nih.gov/39009076/)). Pathogenicity hotspots localize to critical domains (*PKP2* ARM7/ARM8; *DSG2* N-terminal cadherin repeats), whereas incidentally identified variants distribute like background population variation ([PMID: 30985088](https://pubmed.ncbi.nlm.nih.gov/30985088/)).

### Allele Frequency and Penetrance
ARVC-associated desmosomal variants are surprisingly prevalent in the general population but with **reduced penetrance**. In a Finnish cohort (n=6,334), "the collective prevalence of all 5 mutations... was 31 of 6,334 individuals, or 0.5%. The apparent founder mutation PKP2 Q59L is present in 0.3% of Finns and was previously shown to have an approximately 20% disease penetrance" ([PMID: 21397041](https://pubmed.ncbi.nlm.nih.gov/21397041/)) — roughly 1 in 200 Finns carries a desmosomal variant.

### Origin and Functional Consequences
Variants are **germline**. Functional consequence is predominantly **loss of function / haploinsufficiency** of desmosomal adhesion, with some **dominant-negative** effects. Endomyocardial samples of a *DSG2* deletion carrier showed reduced immunoreactive signal for desmoglein-2, plakophilin-2, plakoglobin, and desmoplakin — indicating collective destabilization of the desmosomal complex ([PMID: 21397041](https://pubmed.ncbi.nlm.nih.gov/21397041/)).

### Modifier Genes, Epigenetics, Chromosomal
Carriage of a second variant modifies severity ([PMID: 25616645](https://pubmed.ncbi.nlm.nih.gov/25616645/)). Epigenetic regulation involves tissue **microRNAs**: "miR-21-5p and miR-29b-3p are associated with fibrosis and extracellular matrix remodeling, whereas miR-133a-b and miR-130a are linked to cardiomyocyte integrity loss and desmosomal dysfunction" ([PMID: 42353884](https://pubmed.ncbi.nlm.nih.gov/42353884/)); miR-217-5p, miR-708-5p, miR-135b link to Wnt/β-catenin and Hippo. No recurrent large-scale chromosomal abnormalities cause ARVC, though structural deletions (e.g., *DSG2*) occur.

---

## 5. Environmental Information

- **Environmental factors:** No environmental toxin or radiation exposure causes ARVC. The dominant non-genetic factor is **mechanical/hemodynamic load from exercise**.
- **Lifestyle factors:** **Endurance and high-intensity/competitive sport** is the principal lifestyle modifier — accelerating penetrance and arrhythmia; ARVC is among the most common causes of SCD in athletes ([PMID: 40470644](https://pubmed.ncbi.nlm.nih.gov/40470644/); [PMID: 42305082](https://pubmed.ncbi.nlm.nih.gov/42305082/)).
- **Infectious agents:** **None cause ARVC.** However, desmosomal cardiomyopathy can present as **myocarditis-like "hot phases"** (most commonly *DSP*) with troponin release mimicking acute myocarditis, involving NLRP3-inflammasome activation and anti-desmosomal/anti-intercalated-disc autoantibodies ([PMID: 41448261](https://pubmed.ncbi.nlm.nih.gov/41448261/)). This aseptic intracellular inflammation is frequently misdiagnosed as viral myocarditis, particularly in children ([PMID: 41255689](https://pubmed.ncbi.nlm.nih.gov/41255689/)).

---

## 6. Mechanism / Pathophysiology

### Core Causal Chain

```
Desmosomal LOF variant (PKP2/DSP/DSG2/DSC2/JUP)
        │
        ▼
Intercalated disc destabilization  →  ↓ Connexin-43 (Cx43) gap junctions
        │                                       │
        ▼                                       ▼
Plakoglobin translocates to nucleus     Slowed conduction, Na-current↓
        │                                (arrhythmogenic substrate)
        ▼
Hippo activation (Merlin/NF2→MST1/2→LATS1/2→YAP-P)
        │
        ▼
YAP-P + phospho-β-catenin sequestered  →  ↓ canonical Wnt/β-catenin, ↓TEAD
        │
        ▼
Pro-adipogenic + pro-fibrotic transcription  (+ DSC2→TCF7→TGF-β2 in fibroblasts)
        │
        ▼
FIBROFATTY REPLACEMENT of myocardium  →  VT/VF, SCD, heart failure
        │
   (accelerated by exercise; amplified by inflammation/autoantibodies)
```

### Molecular Pathways
Multiple independent reviews converge on **canonical and non-canonical WNT signaling, the Hippo-YAP pathway, and TGF-β signaling** as the central dysregulated pathways: "these pathways include canonical and non-canonical WNT signalling, the Hippo-Yes-associated protein (YAP) pathway and transforming growth factor-β signalling" ([PMID: 31028357](https://pubmed.ncbi.nlm.nih.gov/31028357/)). "Imbalance in the Wnt/β-catenin signaling and also in the crosslinked Hippo pathway leads to the transcription of proadipogenic and profibrotic genes" ([PMID: 36289882](https://pubmed.ncbi.nlm.nih.gov/36289882/)). Experimentally, "altered protein constituents of intercalated discs were associated with activation of the upstream Hippo molecules" ([PMID: 24276085](https://pubmed.ncbi.nlm.nih.gov/24276085/)). A distinct fibrosis arm operates through DSC2: "DSC2 deficiency upregulated transcription factor 7 (TCF7) expression, promoting its binding to TGF-β2 promoter regions to enhance TGF-β2 transcription in cardiac fibroblasts" ([PMID: 42366226](https://pubmed.ncbi.nlm.nih.gov/42366226/)).

### Shared Mutation-Agnostic Defect: Cx43
"The reduction in expression of the ventricular gap junction protein Cx43 (connexin-43) is a common molecular alteration underlying desmosomal junctional deficits and arrhythmias" ([PMID: 41582809](https://pubmed.ncbi.nlm.nih.gov/41582809/)) — making Cx43 both a unifying mechanism and a therapeutic target.

### Cellular Processes
- **Cardiomyocyte death** (apoptosis/necrosis) → replacement fibrosis.
- **Fibro-adipogenic differentiation** of cardiac progenitor/interstitial cells.
- **Microtubule detyrosination:** PKP2 loss increases microtubule detyrosination and membrane stiffness, reducing sodium current; parthenolide rescues both ([PMID: 42366968](https://pubmed.ncbi.nlm.nih.gov/42366968/)).
- **Inflammation:** ACM is increasingly framed as an inflammatory cardiomyopathy — desmosomal variants activate NFκB and GSK3β signaling, promoting cytokine release and immune infiltration that may **precede** structural change ([PMID: 42193878](https://pubmed.ncbi.nlm.nih.gov/42193878/)).

### Immune / Autoantibody Involvement
"Three pathogenic ACM-IgGs activated GSK-3β upstream of p38MAPK, leading to phosphorylation and junctional loss of β-catenin. GSK-3β inhibition rescued the loss of cell cohesion" ([PMID: 42219531](https://pubmed.ncbi.nlm.nih.gov/42219531/)) — establishing a pathogenic autoantibody/GSK-3β axis and a druggable node.

### Single-cell / Molecular Profiling
Single-nucleus RNA-seq of left-dominant ACM hearts (5 ACM vs 4 donors) "revealed an increased proportion of fibroblasts and adipocytes in the left ventricles of LACM patients, suggesting a cellular basis for the fibrofatty remodeling observed in the disease," plus a disease-associated cardiomyocyte subpopulation (CM1) upregulating fibrosis/metabolism/stress markers ([PMID: 40383406](https://pubmed.ncbi.nlm.nih.gov/40383406/)).

**Suggested ontology terms:** GO:0016055 (Wnt signaling), GO:0035329 (Hippo signaling), GO:0007179 (TGF-β receptor signaling), GO:0007507 (heart development), GO:0050900 (leukocyte migration); CL:0000746 (cardiac muscle cell), CL:0000057 (fibroblast), CL:0000136 (adipocyte).

---

## 7. Anatomical Structures Affected

**Organ level:** The **heart** (UBERON:0000948), primarily the **right ventricle** (UBERON:0002080); secondary/left ventricle (UBERON:0002084) in biventricular and left-dominant variants. Body system: **cardiovascular** (UBERON:0004535).

**"Triangle of dysplasia":** Structural remodeling primarily involves three RV regions — "the three regions ('ARVC triangle') primarily involved in ARVC structural remodeling": RV inflow/subtricuspid region, RV outflow tract, and RV apex ([PMID: 33927217](https://pubmed.ncbi.nlm.nih.gov/33927217/)). Ex vivo 9.4T MRI showed high fat content in these regions: "the healthy heart exhibited twice less fat than the ARVC heart (31.9%, 28.7% and 1.3% of fat in the same regions, respectively)," histologically confirmed, with fibrosis also present in fat-poor areas ([PMID: 33927217](https://pubmed.ncbi.nlm.nih.gov/33927217/)).

**Tissue/cell level:** Cardiac muscle tissue is replaced by **fibrous** (connective) and **adipose** tissue. Cell populations: cardiomyocytes (CL:0000746, lost), fibroblasts (CL:0000057, expanded), adipocytes (CL:0000136, expanded) ([PMID: 40383406](https://pubmed.ncbi.nlm.nih.gov/40383406/)).

**Subcellular level:** The **intercalated disc / desmosome** (GO:0030057 desmosome; GO:0005912 adherens junction), **gap junction** (GO:0005921), **nucleus** (plakoglobin/YAP translocation; increased nuclear stiffness in TMEM43 carriers), and **cytoskeleton/microtubules** (GO:0005874).

**Progression pattern:** Fibrofatty replacement typically advances **from epicardium/mid-myocardium toward endocardium**. Left-dominant/biventricular variants involve LV lateral/posterior basal segments — "cardiac magnetic resonance showed LV late gadolinium enhancement in the LV lateral and posterior basal segments in all patients" ([PMID: 33197325](https://pubmed.ncbi.nlm.nih.gov/33197325/)).

**Lateralization:** RV-dominant (classic), LV-dominant (ALVC), or biventricular.

---

## 8. Temporal Development

- **Onset:** Usually **adolescence to adulthood (2nd–4th decades)** ([PMID: 25894016](https://pubmed.ncbi.nlm.nih.gov/25894016/)); pediatric-onset ARVD occurs (mean 12±4 yr) and may be misdiagnosed as myocarditis ([PMID: 31375646](https://pubmed.ncbi.nlm.nih.gov/31375646/)). Late presentation (≥50 yr) occurs in ~21% and is **not benign** — 65% sustained VA over 6 years ([PMID: 28215569](https://pubmed.ncbi.nlm.nih.gov/28215569/)).
- **Onset pattern:** Insidious/chronic, punctuated by acute arrhythmic or inflammatory ("hot phase") episodes.
- **Disease stages:** (1) **Concealed phase** — arrhythmic risk with subtle/absent structure; (2) **Overt electrical disease** — symptomatic arrhythmias, ECG changes, structural RV abnormality; (3) **RV failure**; (4) **Biventricular/end-stage failure**.
- **Progression rate:** Variable, generally slowly progressive over decades; accelerated by exercise.
- **Course pattern:** Progressive with episodic arrhythmic/inflammatory flares.
- **Duration:** Chronic, lifelong.
- **Critical periods:** Adolescence/young adulthood coincident with sport participation is the critical window for SCD and for intervention (exercise restriction, ICD).

---

## 9. Inheritance and Population

- **Prevalence:** ~**1:2,000 to 1:5,000**: "Arrhythmogenic right ventricular cardiomyopathy (ARVC) is a genetic heart disease with a prevalence of 1 : 2000 to 1 : 5000" ([PMID: 40202346](https://pubmed.ncbi.nlm.nih.gov/40202346/)).
- **Inheritance:** Predominantly **autosomal dominant** with reduced, age-dependent penetrance and variable expressivity. Recessive cardiocutaneous forms: **Naxos disease** — "mutations in the genes encoding the desmosomal proteins plakoglobin and desmoplakin have been identified as the cause of Naxos disease" (*JUP*; woolly hair + palmoplantar keratoderma; ~100% cardiac penetrance by adolescence — [PMID: 16722579](https://pubmed.ncbi.nlm.nih.gov/16722579/)) — and **Carvajal syndrome** (*DSP*, left-dominant — [PMID: 25824144](https://pubmed.ncbi.nlm.nih.gov/25824144/)).
- **Penetrance:** Incomplete and age-dependent — e.g., *PKP2* Q59L ~20% penetrance ([PMID: 21397041](https://pubmed.ncbi.nlm.nih.gov/21397041/)); by contrast *TMEM43* p.S358L is **fully penetrant** ([PMID: 24598986](https://pubmed.ncbi.nlm.nih.gov/24598986/)).
- **Founder effects:** *TMEM43* p.S358L (Newfoundland; "an estimated age of 1300-1500 years for the mutation, which proves the European origin of the Newfoundland mutation" — [PMID: 24598986](https://pubmed.ncbi.nlm.nih.gov/24598986/)); *PKP2* Q59L (Finland).
- **Carrier frequency:** ~0.5% collective desmosomal-variant carrier prevalence (~1 in 200) in Finland ([PMID: 21397041](https://pubmed.ncbi.nlm.nih.gov/21397041/)).
- **Sex ratio:** Male predominance. "Ventricular arrhythmia had occurred at inclusion or occurred during follow-up in 85 patients (33% of females vs. 55% of males, P = 0.002). Exercise doses were higher in males compared with females," and the sex effect lost significance after adjustment for exercise dose ([PMID: 33829244](https://pubmed.ncbi.nlm.nih.gov/33829244/)); SHaRe registry showed 61% male predominance with gene-specific variation (*DSP* more common in females, OR 3.3) ([PMID: 42159538](https://pubmed.ncbi.nlm.nih.gov/42159538/)).
- **Age distribution:** Clinically overt from 2nd–4th decades; a substantial minority present after 50.

---

## 10. Diagnostics

### Clinical Criteria
Diagnosis uses the multiparametric **1994 Task Force Criteria**, revised as the **2010 modified Task Force Criteria** with quantitative structural thresholds, and updated by the **2020 Padua criteria** (adding left-predominant/biventricular criteria incorporating CMR late gadolinium enhancement). "The original right-dominant phenotype is traditionally diagnosed using the 2010 task force criteria, a multifactorial algorithm divided into major and minor criteria" ([PMID: 38512728](https://pubmed.ncbi.nlm.nih.gov/38512728/)); "in 2010, the task force criteria were revised to include quantitative abnormalities" ([PMID: 32032135](https://pubmed.ncbi.nlm.nih.gov/32032135/)). The 2010 criteria are more specific: "Of 968 patients, 220 (22.7%) fulfilled either a major or a minor 1994 TFC, and 25 (2.6%) fulfilled any of the 2010 TFC criterion" ([PMID: 24996808](https://pubmed.ncbi.nlm.nih.gov/24996808/)).

### Tests
- **ECG:** T-wave inversion V1–V3, epsilon wave, QRS fragmentation, low precordial QRS voltage, signal-averaged ECG late potentials, LBBB-morphology VT.
- **Imaging:** Echocardiography and **cardiac MRI** (gold standard) demonstrating RV dilatation, reduced RVEF, aneurysms/regional wall-motion abnormalities, and late gadolinium enhancement; RV angiography ("pile d'assiettes" appearance) in select cases.
- **Tissue:** Endomyocardial biopsy showing fibrofatty replacement and reduced desmosomal immunoreactivity.
- **Genetic testing:** Broad **cardiomyopathy/arrhythmia NGS gene panels** (not limited to validated ARVC genes) are recommended; WES/WGS in select cases. Panels have ~31% diagnostic yield with ~54% VUS in ICC clinics ([PMID: 39009076](https://pubmed.ncbi.nlm.nih.gov/39009076/)). "Using a broad cardiomyopathy and arrhythmia gene panel in ARVC probands, rather than limiting testing to validated ARVC genes alone, is warranted" ([PMID: 42389803](https://pubmed.ncbi.nlm.nih.gov/42389803/)).
- **Biomarkers:** Circulating miR-15a-5p, miR-16-5p, miR-92a-3p differentiate high- vs low-risk patients ([PMID: 40222719](https://pubmed.ncbi.nlm.nih.gov/40222719/)).
- **Emerging:** Machine-learning models (gradient-boosted trees, AUC 0.943) enhance ARVC detection from multimodal data ([PMID: 41884351](https://pubmed.ncbi.nlm.nih.gov/41884351/)).

### Differential Diagnosis
Idiopathic RVOT VT, myocarditis (including hot-phase overlap), cardiac sarcoidosis, Brugada syndrome, dilated cardiomyopathy, athlete's heart, and non-desmosomal phenocopies (e.g., RIT1-related) ([PMID: 41918562](https://pubmed.ncbi.nlm.nih.gov/41918562/)).

### Screening
First-degree relatives undergo **cascade genetic + clinical screening** (ECG, echo, Holter, CMR) with genetic counseling.

---

## 11. Outcome / Prognosis

- **Mortality/SCD:** Principal risk is SCD from ventricular arrhythmia, especially in young athletes — "ACM was the cause of SCD in 29% of athletes" in a 4-decade national juvenile registry ([PMID: 42305082](https://pubmed.ncbi.nlm.nih.gov/42305082/)).
- **Natural history:** "The 5-year cumulative probability of LTAE was 30% and HF-death/HTx was 10%" ([PMID: 36720007](https://pubmed.ncbi.nlm.nih.gov/36720007/)).
- **Genotype-specific prognosis:** *PKP2* better prognosis ([PMID: 34191271](https://pubmed.ncbi.nlm.nih.gov/34191271/)); *DSG2/DSP* higher HF/transplant risk; *TMEM43* p.S358L malignant — "TMEM patients had worse composite endpoint of death or transplantation (60% vs. 0, P = 0.035; log-rank P = 0.013)" ([PMID: 28960618](https://pubmed.ncbi.nlm.nih.gov/28960618/)).

### Risk Stratification
The **2019 ARVC risk calculator** estimates 5-year sustained-VA risk. Enhancers:

| Predictor | Evidence |
|-----------|----------|
| LV late gadolinium enhancement | "132 (34.3%) had LV LGE on cardiac magnetic resonance, with 98 (25.5%) having a high-risk pattern"; HR 1.82 for VA ([PMID: 41608798](https://pubmed.ncbi.nlm.nih.gov/41608798/)) |
| Ringlike LV LGE | 66.7% VA vs 10% no LGE; adj HR 6.91 ([PMID: 38031154](https://pubmed.ncbi.nlm.nih.gov/38031154/)) |
| Reduced RV/LV strain (FT-CMR) | Reduced in VA patients (no incremental value over risk calculator) ([PMID: 35152298](https://pubmed.ncbi.nlm.nih.gov/35152298/)) |
| Endocardial voltage-mapping scar | "Previous cardiac arrest or syncope (hazard ratio=3.4; 95% CI, 1.4-8.8; P=0.03)"; bipolar low-voltage HR 1.7 per 5% ([PMID: 23392584](https://pubmed.ncbi.nlm.nih.gov/23392584/)) |
| ECG (QRS ratio ≤0.48, inferior TWI, QRS fragmentation) | Independent MACE predictors ([PMID: 24792740](https://pubmed.ncbi.nlm.nih.gov/24792740/)) |
| Reduced RV FAC | Strongest echo predictor (HR 1.08/1% decrease) ([PMID: 24515411](https://pubmed.ncbi.nlm.nih.gov/24515411/)) |
| Circulating miRNAs | miR-15a-5p, 16-5p, 92a-3p ([PMID: 40222719](https://pubmed.ncbi.nlm.nih.gov/40222719/)) |

Other established prognostic factors: prior cardiac arrest/syncope, sustained VT, RV/LV dysfunction, extent of T-wave inversion, male sex, and young age.

---

## 12. Treatment

Current therapy is **palliative** — it manages arrhythmias and heart failure but does not address the molecular substrate ([PMID: 41301430](https://pubmed.ncbi.nlm.nih.gov/41301430/)).

### Pharmacotherapy (MAXO:0000058 pharmacotherapy)
- **Beta-blockers** — grade I for extrasystoles/VT: "Beta-blockers are recommended for patients with extrasystoles or ventricular tachycardia (grade I recommendation). If beta-blockers alone have an insufficient effect, amiodarone, flecainide or sotalol can be added (grade IIa)" ([PMID: 40202346](https://pubmed.ncbi.nlm.nih.gov/40202346/)). Drug classes: beta-adrenergic antagonists, amiodarone (CHEBI:2663), sotalol, flecainide.
- **Heart failure therapy** for ventricular dysfunction.

### Interventional / Device
- **Catheter ablation** — grade IIa for recurrent VT; palliative. Meta-analysis (24 studies, 717 patients): "acute efficacy of 89.8%, major complication of 5.2%, follow-up of 28.9 months, VT freedom of 75.3%, all-cause mortality of 1.1% and heart transplantation of 0.6%"; "epicardial ablation is associated with better long-term VT freedom" (OR 0.50 vs endocardial-only) ([PMID: 33343648](https://pubmed.ncbi.nlm.nih.gov/33343648/)). *DSP*-ACM and *TMEM43* require endo-epicardial mapping ([PMID: 38206263](https://pubmed.ncbi.nlm.nih.gov/38206263/)).
- **ICD** (MAXO implantable cardioverter defibrillator) — grade I for SCD survivors; primary-prevention decisions guided by the ARVC risk calculator; earlier ICD reasonable for *PLN/FLNC/LMNA* genotypes.
- **Heart transplantation** (MAXO:0000384) — for end-stage HF or intractable arrhythmias.

### Lifestyle
- **Exercise restriction** — central, because intense exercise accelerates phenotype and arrhythmia ([PMID: 40470644](https://pubmed.ncbi.nlm.nih.gov/40470644/)).

### Emerging / Experimental Therapies
- **AAV *PKP2* gene replacement (LX2020, AAVrh10):** "we show minimal doses required for efficacy for AAVrh10.PKP2 (LX2020) to rescue cardiac (molecular and especially RV) deficits, arrhythmia burden and survival in PKP2 ACM mice," with no adverse events in non-human-primate safety studies ([PMID: 40175378](https://pubmed.ncbi.nlm.nih.gov/40175378/)).
- **Mutation-agnostic AAV-Cx43 restoration:** "Administration of AAV-Cx43 (adeno-associated-viral-mediated connexin-43) gene therapy alleviated the severe biventricular dilatation, contractile dysfunction, and arrhythmias, while prolonging lifespan in 2 severe desmosomal ACM mouse models" ([PMID: 41582809](https://pubmed.ncbi.nlm.nih.gov/41582809/)).
- **AAV8-FGF21:** mitigated structural change and adrenergic arrhythmias in PKP2-cKO mice ([PMID: 41759869](https://pubmed.ncbi.nlm.nih.gov/41759869/)).
- **Small molecules:** parthenolide (microtubule detyrosination — [PMID: 42366968](https://pubmed.ncbi.nlm.nih.gov/42366968/)); GSK-3β inhibition (autoantibody axis — [PMID: 42219531](https://pubmed.ncbi.nlm.nih.gov/42219531/)); apremilast (PDE4 inhibitor; improves cardiomyocyte cohesion via plakoglobin Ser665 phosphorylation and ERK1/2 — [PMID: 41185038](https://pubmed.ncbi.nlm.nih.gov/41185038/)).
- **Immunomodulation** during active inflammatory phases (NFκB/GSK3β/cytokine-directed) ([PMID: 42193878](https://pubmed.ncbi.nlm.nih.gov/42193878/)).

### Pharmacogenomics / Personalized Medicine
Genotype-guided management is emerging (e.g., earlier ICD for *PLN/FLNC/LMNA*; gene-specific ablation strategy) ([PMID: 34970070](https://pubmed.ncbi.nlm.nih.gov/34970070/)).

---

## 13. Prevention

- **Primary prevention:** Exercise restriction/avoidance of competitive endurance sport in carriers; ICD in high-risk individuals.
- **Secondary prevention:** **Cascade genetic and clinical screening** of first-degree relatives with pre-/post-test genetic counseling; genotype-positive/phenotype-negative relatives receive periodic follow-up. "Pre-test and post-test counseling were provided to probands and cascade screening offered to relatives" ([PMID: 39009076](https://pubmed.ncbi.nlm.nih.gov/39009076/)). Family screening is warranted even in gene-elusive ARVC — 17% of gene-elusive families harbored a P/LP variant in a different cardiomyopathy/arrhythmia gene ([PMID: 42389803](https://pubmed.ncbi.nlm.nih.gov/42389803/)).
- **Tertiary prevention:** ICD, ablation, and HF therapy to prevent SCD and progression.
- **Risk stratification:** ARVC risk calculator + CMR LGE/strain + electroanatomic mapping (Section 11).
- **Immunization/public health:** Not applicable (non-infectious, non-communicable Mendelian disease).
- **Counseling:** Genetic counseling for family planning; preimplantation/prenatal testing possible for known familial variants.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens* (NCBI:txid9606); naturally occurring in *Canis lupus familiaris* (dog, NCBI:txid9615).
- **Breeds:** **Boxer** and **English bulldog** dogs. "This myocardial disorder has also been described in Boxer and English bulldogs (EBs)" ([PMID: 40540101](https://pubmed.ncbi.nlm.nih.gov/40540101/)). Boxer ARVC is associated with a **striatin (STRN)** deletion.
- **Comparative pathology:** Canine ACM recapitulates human ECG phenotype — in 59 EBs, ACM dogs showed wider QRS and longer terminal activation, and "the TWI and ɛ wave in ACM group were respectively present in 19% and 32%," correlating with echocardiographic RV parameters ([PMID: 40540101](https://pubmed.ncbi.nlm.nih.gov/40540101/)).
- **Orthologous genes:** PKP2, DSP, DSG2, DSC2, JUP, TMEM43 are conserved across mammals; STRN in dogs.
- **Zoonotic potential:** None (genetic disease, not transmissible).

---

## 15. Model Organisms

| Model | Type | Utility / recapitulation |
|-------|------|--------------------------|
| **PKP2 cardiac-specific KO mouse** (tamoxifen-inducible) | Mammalian, genetic | Recapitulates RV dysfunction, arrhythmia, microtubule detyrosination, Cx43 loss; used for AAV-PKP2/FGF21 gene therapy ([PMID: 40175378](https://pubmed.ncbi.nlm.nih.gov/40175378/); [PMID: 41759869](https://pubmed.ncbi.nlm.nih.gov/41759869/); [PMID: 42366968](https://pubmed.ncbi.nlm.nih.gov/42366968/)) |
| **Dsp / Jup mutant mice** | Mammalian, genetic | Hippo activation, adipogenesis; severe biventricular desmosomal ACM for Cx43 gene therapy ([PMID: 24276085](https://pubmed.ncbi.nlm.nih.gov/24276085/); [PMID: 41582809](https://pubmed.ncbi.nlm.nih.gov/41582809/)) |
| **PKP2-knockdown HL-1 atrial myocytes** | In vitro cell line | Hippo/desmosomal signaling ([PMID: 24276085](https://pubmed.ncbi.nlm.nih.gov/24276085/)) |
| **Patient hiPSC-derived cardiomyocytes** (e.g., DSP mutation) | In vitro human | "Human induced pluripotent stem cells from a healthy control (hiPSC) and an ACM index patient (ACM-hiPSC) carrying a heterozygous desmoplakin (DSP) gene mutation" — cohesion/arrhythmia/drug testing ([PMID: 41185038](https://pubmed.ncbi.nlm.nih.gov/41185038/)) |
| **Non-human primate** | Mammalian | AAV-PKP2 (LX2020) safety studies ([PMID: 40175378](https://pubmed.ncbi.nlm.nih.gov/40175378/)) |
| **Boxer / English bulldog dogs** | Natural mammalian | Spontaneous ACM; STRN in Boxer ([PMID: 40540101](https://pubmed.ncbi.nlm.nih.gov/40540101/)) |

Comprehensive reviews of intercalated-disc-gene animal models confirm that murine and hiPSC models have driven mechanistic understanding and therapeutic development ([PMID: 38892395](https://pubmed.ncbi.nlm.nih.gov/38892395/); [PMID: 42137277](https://pubmed.ncbi.nlm.nih.gov/42137277/)). **Limitations:** murine models incompletely capture the exercise-dependent, slowly progressive, and inflammatory "hot-phase" aspects of human disease and human variant heterogeneity. Resources: MGI, IMPC, Cellosaurus, Alliance of Genome Resources, OMIA.

---

## Mechanistic Model / Interpretation

ARVC is best understood as a **desmosome-initiated, signaling-amplified, mechanically-triggered fibrofatty cardiomyopathy**. The upstream event is loss of desmosomal adhesion at the intercalated disc. This has two immediate consequences that map onto the two clinical hallmarks:

1. **Electrical instability (upstream, early):** reduced Cx43 gap junctions and altered sodium-channel function (partly via microtubule detyrosination) slow conduction and create a re-entrant substrate — explaining why arrhythmias and SCD can **precede** overt structural disease (the concealed phase). This is the mutation-agnostic arrhythmia axis and the rationale for Cx43-restoration therapy.

2. **Structural remodeling (downstream, progressive):** nuclear translocation of plakoglobin, Hippo-YAP activation, Wnt/β-catenin suppression, and TGF-β/TCF7 engagement redirect transcription toward adipogenesis and fibrosis, producing the "triangle of dysplasia" fibrofatty replacement, RV dilatation/aneurysms, and eventually biventricular failure.

Layered on top is an **inflammatory amplifier** (NFκB/GSK3β, NLRP3-inflammasome, anti-DSG2 autoantibodies) that produces episodic myocarditis-like hot phases, and a **mechanical accelerator** (endurance exercise) that increases wall stress on an adhesion-deficient myocardium — accounting for the dose-dependent exercise effect and the male predominance mediated by exercise. Genotype tunes the phenotype: *PKP2* is RV-predominant and comparatively benign; *DSG2/DSP* skew toward LV involvement and heart failure; *TMEM43* p.S358L is fully penetrant and malignant.

---

## Evidence Base

| Domain | Key PMIDs | Contribution |
|--------|-----------|--------------|
| Genetic architecture | [42366226](https://pubmed.ncbi.nlm.nih.gov/42366226/), [34191271](https://pubmed.ncbi.nlm.nih.gov/34191271/), [30790397](https://pubmed.ncbi.nlm.nih.gov/30790397/), [25616645](https://pubmed.ncbi.nlm.nih.gov/25616645/) | Desmosomal predominance; PKP2/DSG2/DSP genotype–phenotype |
| Founder/penetrance | [21397041](https://pubmed.ncbi.nlm.nih.gov/21397041/), [24598986](https://pubmed.ncbi.nlm.nih.gov/24598986/), [28960618](https://pubmed.ncbi.nlm.nih.gov/28960618/) | Carrier frequency, reduced penetrance, TMEM43 malignancy |
| Mechanism | [24276085](https://pubmed.ncbi.nlm.nih.gov/24276085/), [31028357](https://pubmed.ncbi.nlm.nih.gov/31028357/), [36289882](https://pubmed.ncbi.nlm.nih.gov/36289882/), [41582809](https://pubmed.ncbi.nlm.nih.gov/41582809/), [40383406](https://pubmed.ncbi.nlm.nih.gov/40383406/) | Hippo/Wnt/TGF-β, Cx43, single-cell remodeling |
| Inflammation/autoimmunity | [42193878](https://pubmed.ncbi.nlm.nih.gov/42193878/), [42219531](https://pubmed.ncbi.nlm.nih.gov/42219531/), [41448261](https://pubmed.ncbi.nlm.nih.gov/41448261/) | Inflammatory paradigm, GSK-3β autoantibody axis, hot phases |
| Diagnosis | [38512728](https://pubmed.ncbi.nlm.nih.gov/38512728/), [32032135](https://pubmed.ncbi.nlm.nih.gov/32032135/), [24996808](https://pubmed.ncbi.nlm.nih.gov/24996808/), [36635648](https://pubmed.ncbi.nlm.nih.gov/36635648/) | Task Force/Padua criteria, symptom/ECG frequencies |
| Risk/prognosis | [41608798](https://pubmed.ncbi.nlm.nih.gov/41608798/), [38031154](https://pubmed.ncbi.nlm.nih.gov/38031154/), [23392584](https://pubmed.ncbi.nlm.nih.gov/23392584/), [36720007](https://pubmed.ncbi.nlm.nih.gov/36720007/) | LGE, scar mapping, natural history |
| Treatment | [40202346](https://pubmed.ncbi.nlm.nih.gov/40202346/), [33343648](https://pubmed.ncbi.nlm.nih.gov/33343648/), [40175378](https://pubmed.ncbi.nlm.nih.gov/40175378/), [41582809](https://pubmed.ncbi.nlm.nih.gov/41582809/) | Pharmacotherapy, ablation, gene therapy |
| Exercise/sex | [40470644](https://pubmed.ncbi.nlm.nih.gov/40470644/), [33829244](https://pubmed.ncbi.nlm.nih.gov/33829244/), [42305082](https://pubmed.ncbi.nlm.nih.gov/42305082/), [42159538](https://pubmed.ncbi.nlm.nih.gov/42159538/) | Exercise modifier, sex differences |
| Animal/models | [40540101](https://pubmed.ncbi.nlm.nih.gov/40540101/), [38892395](https://pubmed.ncbi.nlm.nih.gov/38892395/), [41185038](https://pubmed.ncbi.nlm.nih.gov/41185038/) | Canine disease, murine/hiPSC models |

---

## Limitations and Knowledge Gaps

1. **Reduced penetrance and VUS burden:** ~0.5% population carrier frequency with ~20% penetrance and ~54% VUS rate in panels complicate individual risk prediction and genetic counseling.
2. **Gene-elusive disease:** A substantial fraction of clinically definite ARVC lacks an identified pathogenic variant, limiting cascade screening in those families.
3. **Risk stratification imperfection:** The 2019 risk calculator underperforms in non-classical/left-dominant ACM; ringlike LGE and other markers add value but are not fully integrated.
4. **Palliative therapeutics:** No approved disease-modifying therapy currently exists; gene therapies remain preclinical/early-phase.
5. **Causality of inflammation/autoantibodies:** Whether inflammation initiates or merely amplifies disease — and whether anti-DSG2 autoantibodies are causal — remains incompletely established.
6. **Quality-of-life data:** Formal per-phenotype QoL instrument data (EQ-5D/SF-36) for ARVC were not identified in this investigation.
7. **Model limitations:** Murine models incompletely capture exercise-dependent, slowly progressive, and hot-phase human features.

---

## Proposed Follow-up Experiments / Actions

1. **Advance AAV gene therapies to clinical trials** — track *PKP2* replacement (LX2020) and mutation-agnostic Cx43 restoration; monitor ClinicalTrials.gov for first-in-human data.
2. **Prospective validation of multimodal + ML risk models** integrating CMR LGE (including ringlike pattern), FT-CMR strain, electroanatomic scar, and circulating miRNAs to improve the ARVC risk calculator, especially for left-dominant/biventricular phenotypes.
3. **Test targeted small molecules** (parthenolide, GSK-3β inhibitors, apremilast) and **immunomodulation during hot phases** in controlled preclinical and early-phase human studies.
4. **Deep-phenotype gene-elusive families** with WGS, structural-variant, and non-coding analyses; adopt broad cardiomyopathy/arrhythmia panels as standard.
5. **Functionally reclassify VUS** using hiPSC-CM and high-throughput assays to reduce diagnostic uncertainty.
6. **Longitudinal exercise-dose studies** to define safe activity thresholds by genotype and sex.
7. **Collect standardized QoL/PROM data** (EQ-5D, SF-36, ICD-specific measures) across ARVC registries.

---

## References (selected PMIDs)

42366226, 42244336, 40202346, 25894016, 42305082, 40470644, 24276085, 34191271, 30790397, 25616645, 16722579, 21397041, 36635648, 36720007, 41582809, 42219531, 41185038, 40540101, 38512728, 32032135, 24996808, 41608798, 23392584, 40222719, 33927217, 33197325, 39009076, 42389803, 40383406, 42353884, 24598986, 28960618, 33343648, 33829244, 42159538, 31028357, 36289882, 40175378, 41759869, 42193878, 41448261, 41255689, 42366968, 38031154, 35152298, 24792740, 24515411, 28215569, 38206263, 41918562, 41884351, 34970070, 38892395, 42137277, 39980788, 25824144, 30985088, 41301430


## Artifacts

- [OpenScientist final report](Arrhythmogenic_Right_Ventricular_Cardiomyopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Arrhythmogenic_Right_Ventricular_Cardiomyopathy-deep-research-openscientist_artifacts/final_report.pdf)
