---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T04:43:02.391899'
end_time: '2026-08-27T04:47:51.419392'
duration_seconds: 289.03
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SCUBE3-Related Short Stature Syndrome
  mondo_id: ''
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
  web_search_requests: 11
  num_turns: 21
  total_cost_usd: 1.0721868000000003
  session_id: a1f65bb8-1b49-516c-9197-25fb2b9c84dd
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 14
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 7
  on_topic: 5
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SCUBE3-Related Short Stature Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SCUBE3-Related Short Stature Syndrome** covering all of the
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

I'll research SCUBE3-Related Short Stature Syndrome using primary literature sources. Let me start by loading the necessary web research tools and searching for information.

# SCUBE3-Related Short Stature Syndrome — Comprehensive Research Report

## Executive Summary

SCUBE3-related short stature syndrome — formally catalogued as **Short Stature, Facial Dysmorphism, and Skeletal Anomalies with or without Cardiac Anomalies-2 (SSFSC2)** — is an ultra-rare autosomal recessive skeletal dysplasia/malformation syndrome caused by biallelic loss-of-function variants in *SCUBE3* (Signal peptide, CUB domain, EGF-like domain-containing protein 3), a secreted BMP2/BMP4 co-receptor essential for endochondral bone growth, craniofacial patterning, and tooth development. First delineated in 2021 from 18 affected individuals across 9 families, fewer than ~20-25 patients have been reported to date, making this one of the more recently characterized monogenic short-stature syndromes. It is mechanistically and phenotypically related to — but genetically distinct from — SSFSC1, caused by heterozygous (dominant, haploinsufficient) *BMP2* variants, since SCUBE3 is a direct co-receptor for BMP2/4 signaling.

---

## 1. Disease Information

**Overview:** SSFSC2 is a syndromic form of primordial/postnatal short stature combining growth failure, a recognizable craniofacial gestalt, dental anomalies, and skeletal (and occasionally cardiac) malformations, without intellectual disability in the great majority of reported cases. It results from loss of function of SCUBE3, a matricellular BMP2/4 co-receptor.

**Key identifiers:**
- **OMIM (phenotype):** #619184 — Short Stature, Facial Dysmorphism, and Skeletal Anomalies with or without Cardiac Anomalies 2 (SSFSC2) ([OMIM #619184](https://omim.org/entry/619184))
- **OMIM (gene):** *614708 — SCUBE3 ([OMIM 614708](https://omim.org/entry/614708))
- **MONDO:** MONDO:0030953
- **HGNC:** HGNC:13655 (SCUBE3)
- **Gene locus:** 6p21.31 (NC_000006.12: 35,213,956–35,253,079; 24 exons)
- **Ensembl:** ENSG00000146197
- **Inheritance:** Autosomal recessive
- **NCBI GTR condition ID:** C5543057
- **Related/allelic-pathway disorder:** OMIM #617877 — SSFSC1, caused by heterozygous (dominant, haploinsufficient) *BMP2* variants — phenotypically overlapping but genetically and mechanistically distinct (see Etiology/Mechanism below)

**Synonyms:** SSFSC2; SCUBE3-related developmental disorder; SCUBE3 loss-of-function syndrome.

**Evidence basis:** This is an aggregated disease-level resource (OMIM, MONDO, MalaCards, GeneReviews-style descriptions) built from a small number of published cohort and case reports rather than large-scale EHR data, reflecting its extreme rarity.

Sources: [OMIM #619184](https://omim.org/entry/619184) · [MalaCards](https://www.malacards.org/card/short_stature_facial_dysmorphism_and_skeletal_anomalies_with_or_without_cardiac_anomalies_2) · [GTR C5543057](https://www.ncbi.nlm.nih.gov/gtr/conditions/C5543057/)

---

## 2. Etiology

### Disease Causal Factors
SSFSC2 is a purely genetic (Mendelian) disorder caused by **biallelic (homozygous or compound heterozygous) inactivating variants in *SCUBE3***. There is no known environmental, infectious, or acquired contribution to disease onset — it is a congenital developmental disorder present from before birth (prenatal growth restriction is a core feature).

### Genetic Risk Factors
- **Causal variants:** The founding cohort (Lin et al., 2021, *AJHG*; PMID 33308444) identified **eight distinct SCUBE3 mutations** across 9 families/18 patients — a spectrum including **missense, nonsense, frameshift, and canonical splice-site changes, plus a complex intragenic rearrangement**. All were biallelic (homozygous in consanguineous families, or compound heterozygous).
- A subsequent case (Turkish consanguineous family, 2025; PMID 40331102) added a **novel homozygous missense variant, c.908G>C (p.Cys303Ser)**, in the seventh calcium-binding EGF-like domain, classified *likely pathogenic* by ACMG criteria and absent from ClinVar, HGMD, LOVD, and population allele-frequency databases (gnomAD) — consistent with the ultra-rarity of pathogenic *SCUBE3* alleles.
- **Consanguinity** is a recurrent risk factor in reported pedigrees (multiple families, including the index Turkish and other Middle Eastern/consanguineous kindreds), consistent with autosomal recessive inheritance and a founder/private-variant mutational spectrum rather than recurrent hotspot mutations.
- No modifier genes have yet been reported; the cohort is too small for genotype-phenotype correlation studies beyond noting that truncating/complete loss-of-function alleles broadly track with the "classic" presentation.

### Protective Factors
None reported — expected, given the disease is caused by biallelic loss of a single gene's function rather than a susceptibility-locus model.

### Gene-Environment Interactions
None documented; SSFSC2 behaves as a fully penetrant monogenic recessive trait in reported families.

Sources: [Lin et al. 2021, AJHG (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S0002929720304122) · [PMC12052373 (2025 case report)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12052373/) · [PubMed 40331102](https://pubmed.ncbi.nlm.nih.gov/40331102/)

---

## 3. Phenotypes

Phenotype data derive almost entirely from the 2021 index cohort (18 patients/9 families) plus subsequent single-case reports.

### Growth
- **Prenatal growth restriction** (e.g., birth weight −3.7 SDS in the 2025 case report) — onset is congenital/prenatal.
- **Postnatal short stature**, often severe (e.g., height −3.6 SDS at age 13 in the reported case); growth failure is generally **stable/non-progressive** rather than deteriorating over time, though systematic longitudinal growth-curve data across the full cohort have not been separately published.
- **HP suggestions:** HP:0004322 (Short stature), HP:0001511 (Intrauterine growth retardation)

### Craniofacial dysmorphism (near-universal; hallmark of the syndrome)
- Broad forehead with temporal narrowing; flat midface; short nose with anteverted nares; long philtrum; thin upper lip; short/receding chin. In older individuals a long, triangular face with high/broad forehead, high nasal bridge with long nose, and thick lips has also been described (suggesting some age-dependent evolution of the facial gestalt).
- Additional individual case features: high arched eyebrows, epicanthus, blepharoptosis, hypotelorism.
- **HP suggestions:** HP:0000341 (Narrow forehead)/HP:0011220 (Prominent forehead), HP:0000272 (Facial asymmetry — variable), HP:0000348 (High forehead), HP:0000463 (Anteverted nares), HP:0000343 (Long philtrum), HP:0000219 (Thin upper lip vermilion), HP:0000278 (Retrognathia)

### Skeletal
- **Thin, short long bones**
- **Brachydactyly** — reported in 12/15 evaluable cases in the index cohort (a majority feature)
- **Scoliosis**
- **Eleven rib pairs** (axial patterning defect — notably shared with the BMP2-related SSFSC1, consistent with a common BMP-pathway mechanism)
- Mild radial bowing; narrow iliac wings
- **HP suggestions:** HP:0009826 (Limb undergrowth), HP:0001156 (Brachydactyly), HP:0002650 (Scoliosis), HP:0000878 (11 pairs of ribs), HP:0002986 (Bowing of the arm)

### Dental
- **Crowded dentition**, **high-arched or cleft palate**
- Hypodontia, taurodontism, severe crowding (2025 case)
- **HP suggestions:** HP:0000678 (Dental crowding), HP:0000218 (High-arched palate), HP:0000175 (Cleft palate), HP:0000668 (Dental malocclusion), HP:0006476 (Delayed eruption)/HP:0000668

### Cardiac (variable, "with or without")
- Atrial septal defect (ASD) in 2 patients
- Patent foramen ovale (PFO) in 2 patients
- Ventricular extrasystoles with first-degree AV block in 1 patient
- **HP suggestions:** HP:0001631 (ASD), HP:0001655 (PFO), HP:0001708 (First degree AV block)

### Hearing/other
- **Conductive hearing loss** (recurrent but not universal — reported in the index cohort and again in the 2025 case)
- **HP suggestion:** HP:0000405 (Conductive hearing impairment)

### Neurocognitive
- **Developmental delay/intellectual disability is NOT a defining feature** — this is an explicit distinguishing point in OMIM/MalaCards descriptions.
- However, the 2025 case report described **mild learning difficulties** and a Pierre Robin sequence (with surgically corrected cleft palate), noted by the authors as only the **second documented case with learning difficulty**, suggesting occasional but non-obligate cognitive involvement, and that taurodontism may be an under-recognized additional dental manifestation.
- **HP suggestions:** HP:0001999 (Abnormal facial shape, generic), HP:0000175 relevant to Pierre Robin sequence (HP:0000431 broad nasal tip not specifically noted; use HP:0009926 Pierre-Robin sequence if applicable)

### Frequency/severity
Numeric frequencies are sparse given cohort size (n≈18–25 total published cases); qualitative frequency bands (e.g., "most," "majority," "rare") are the best-supported level of precision presently available. Severity and expressivity appear somewhat variable (e.g., presence/absence of cardiac defects, presence/absence of learning difficulty), consistent with the "with or without cardiac anomalies" naming.

### Quality of life
No dedicated QoL instrument (EQ-5D, SF-36) studies have been published for this ultra-rare condition; impact is inferred from the phenotype burden (skeletal, dental, hearing, and occasional cognitive involvement) rather than measured directly.

Sources: [PMC12052373](https://pmc.ncbi.nlm.nih.gov/articles/PMC12052373/) · [OMIM #619184](https://omim.org/entry/619184) · [MalaCards](https://www.malacards.org/card/short_stature_facial_dysmorphism_and_skeletal_anomalies_with_or_without_cardiac_anomalies_2)

---

## 4. Genetic/Molecular Information

### Causal Gene
- ***SCUBE3*** (HGNC:13655), OMIM *614708, chromosome 6p21.31, 24 exons, encoding a ~993-amino-acid secreted protein (NP_689966; processed/cleaved form ~65 kDa after furin-like cleavage in the spacer region).

### Pathogenic Variant Spectrum
- **Variant types:** missense, nonsense, frameshift, canonical splice-site, and a complex intragenic rearrangement (Lin et al. 2021 index cohort of 8 distinct mutations); an additional novel missense variant (c.908G>C, p.Cys303Ser) reported in 2025.
- **Classification:** Reported variants are classified pathogenic/likely pathogenic under ACMG/AMP guidelines; the p.Cys303Ser variant scored 0.999 on AlphaMissense pathogenicity prediction.
- **Structural mechanism (missense example):** AlphaFold3 modeling of p.Cys303Ser showed disruption of the **C303–C316 disulfide bridge within the seventh calcium-binding EGF-like domain**, compromising protein stability/folding — directly parallel to the murine N294K ENU-induced allele, which also maps to calcium-binding EGF domain VII and is proposed to impair homo-/heterodimerization and TGF-β/Hedgehog-pathway coupling.
- **Allele frequency:** Pathogenic *SCUBE3* alleles are essentially absent from population databases (gnomAD, 1000 Genomes) — consistent with an ultra-rare recessive disorder with largely private/family-specific variants rather than recurrent founder mutations, though consanguinity is a recurring feature of reported pedigrees.
- **Somatic vs. germline:** All reported variants are germline.
- **Functional consequences:** In vitro validation (Lin et al. 2021) showed **variable impact of disease variants on transcript processing, protein secretion, and BMP-signaling function** — i.e., a mixture of loss-of-function mechanisms (reduced secretion, impaired receptor engagement) rather than a single uniform biochemical defect. Overall, the functional theme is **loss-of-function/haploinsufficiency-on-recessive-background** rather than gain-of-function or dominant-negative.

### Modifier Genes
None established; cohort size to date is insufficient to support formal modifier-gene analysis.

### Epigenetic Information / Chromosomal Abnormalities
No epigenetic (DNA methylation, histone) mechanism or large chromosomal rearrangement (aneuploidy, translocation) has been implicated — disease mechanism is point-variant/small-indel driven at a single recessive locus.

### Disease-Gene Relationship, in molecular pathway context
Notably, **SCUBE3 is not merely "a gene that happens to cause short stature" — it is the direct molecular co-receptor for BMP2 and BMP4**, and *BMP2* haploinsufficiency independently causes the allelic-pathway disorder SSFSC1 (OMIM #617877), which shares core features (facial dysmorphism, 11 rib pairs, brachydactyly of the fifth ray, variable cardiac outflow-tract defects) but follows **autosomal dominant** inheritance via truncating/haploinsufficient *BMP2* variants. This gene-pathway pairing (ligand vs. co-receptor, dominant vs. recessive) is a key differential-diagnosis and pathway-level insight.

Sources: [OMIM 614708](https://omim.org/entry/614708) · [OMIM #617877](https://omim.org/entry/617877) · [PMC12052373](https://pmc.ncbi.nlm.nih.gov/articles/PMC12052373/) · [Lin et al. 2021](https://www.sciencedirect.com/science/article/pii/S0002929720304122)

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents have been implicated in SSFSC2 causation — it is a fully penetrant monogenic recessive disorder of prenatal onset. Not applicable beyond the genetic etiology described above.

---

## 6. Mechanism / Pathophysiology

### Molecular pathway: BMP2/4 co-receptor function (primary mechanism)
**SCUBE3 functions as a cell-surface/matrix-associated co-receptor that potentiates BMP2 and BMP4 signaling.** Mechanistically:
- SCUBE3 binds BMP ligands (BMP2, BMP4, and reportedly BMP7) and their receptors (BMPR1A, BMPR1B, BMPR2) via its C-terminal **CUB domain**.
- It **recruits BMP receptor complexes into lipid-raft membrane microdomains**, augmenting specific BMP–BMP-type-I-receptor interactions and amplifying downstream SMAD1/5/8 phosphorylation.
- Loss of SCUBE3 function attenuates this potentiation, producing a **BMP-signaling-insufficiency phenotype** phenocopying (in a milder/recessive form) loss of BMP2 itself.
- **GO term suggestion:** GO:0030509 (BMP signaling pathway); GO:0007398 (ectoderm development, via craniofacial patterning)

### Cellular processes: osteoblast/chondrocyte differentiation defect
- SCUBE3 is **specifically expressed in the periosteum and trabecular endosteum**, i.e., in osteoprogenitor and osteoblast populations, and highly expressed in primary osteoblasts and in the cartilage of the developing axial skeleton.
- Ectopic SCUBE3 overexpression in C3H10T1/2 mesenchymal cells markedly induces alkaline phosphatase (ALP) activity and enhances BMP2/4-induced SMAD1/5/8 phosphorylation — i.e., SCUBE3 is **pro-osteogenic**.
- Conversely, *Scube3−/−* cell cultures show **>90% reduction in osteocalcin protein levels** and significantly reduced matrix mineralization, both basally and after BMP2/BMP4 stimulation — directly connecting SCUBE3 loss to **impaired osteoblast differentiation and defective endochondral ossification**, which is the proposed cellular basis for short/thin long bones and short stature in affected patients.
- **CL term suggestions:** CL:0000062 (osteoblast), CL:0000138 (chondrocyte), CL:0000137 (osteocyte)

### Additional signaling cross-talk
- **FGF signaling:** SCUBE3 interacts with FGF8/FGFR4 (shown in zebrafish fast-muscle development) via its EGF-like, spacer, and CUB domains, suggesting a broader growth-factor-modulatory role beyond BMP alone.
- **TGF-β signaling:** SCUBE3's CUB domain also binds TGF-β type II receptor (TβRII) and TGF-β1, promoting canonical TGF-β signaling — a mechanism separately implicated in **cardiac hypertrophy** and in **lung cancer epithelial-mesenchymal transition (EMT)**, indicating SCUBE3 is a multi-pathway growth-factor co-receptor rather than BMP-pathway-exclusive.
- **Hedgehog pathway:** SCUBE proteins as a family (particularly the paralog SCUBE2) are implicated in Hedgehog ligand release/diffusion; SCUBE3-specific Hedgehog data are comparatively limited, though the murine N294K allele (in EGF domain VII) has been proposed to affect TGFβ/Hedgehog pathway coupling.

### Causal chain (proposed)
1. **Biallelic *SCUBE3* loss-of-function variant** →
2. **Reduced/absent functional SCUBE3 co-receptor protein** (via impaired transcript processing, secretion, or receptor engagement) →
3. **Attenuated BMP2/4 (and secondarily FGF8/TGF-β) receptor signaling** in periosteal/endosteal osteoprogenitors and craniofacial/dental epithelial-mesenchymal tissue →
4. **Impaired osteoblast differentiation, reduced matrix mineralization, defective endochondral bone growth and chondrogenesis** →
5. **Short/thin long bones, growth failure, craniofacial dysmorphism, dental anomalies** (clinical phenotype); variable cardiac outflow/septal involvement reflects BMP2/4's parallel roles in cardiac development.

### Molecular profiling / advanced technologies
No transcriptomic (RNA-seq/GEO), proteomic, metabolomic, single-cell, or spatial-transcriptomic datasets specific to human SSFSC2 patient tissue have been published to date — mechanistic data derive from (a) in vitro variant functional assays (transcript/protein/secretion/signaling readouts) and (b) mouse model histology/skeletal-phenotyping, not from omics profiling of patient material.

Sources: [Lin et al. 2021 (AJHG)](https://www.sciencedirect.com/science/article/pii/S0002929720304122) · ["The biology of SCUBE" review, PMC10214685](https://pmc.ncbi.nlm.nih.gov/articles/PMC10214685/) · [BMP/osteoblast search synthesis, ScienceDirect/PMC sources above]

---

## 7. Anatomical Structures Affected

### Organ level
- **Skeletal system:** long bones (thin/short), axial skeleton/ribs (11 pairs), vertebral column (scoliosis), pelvis (narrow iliac wings), hands (brachydactyly)
- **Craniofacial skeleton and soft tissue:** forehead, midface, nose, philtrum, lips, mandible
- **Dentition:** teeth/jaws (crowding, hypodontia, taurodontism, palate)
- **Cardiovascular system:** atrial septum, foramen ovale, conduction system (in a subset of patients)
- **Auditory system:** middle ear (conductive hearing loss)
- **Nervous system:** generally spared (no obligate ID), occasional mild learning difficulty in isolated cases

**UBERON suggestions:** UBERON:0002101 (limb), UBERON:0001474 (bone element), UBERON:0000209 (rib), UBERON:0002516 (skull), UBERON:0001456 (face), UBERON:0001456, UBERON:0001987 (palate), UBERON:0003129 (skeletal system), UBERON:0000948 (heart), UBERON:0001846 (middle ear)

### Tissue/cell level
- Periosteum and trabecular endosteum (osteoprogenitor/osteoblast niche)
- Cartilage of the axial skeleton (chondrogenic centers) during endochondral ossification
- Craniofacial epithelium (branchial arches, nasal/otic placodes) during embryogenesis
- Tooth germ epithelium/mesenchyme

**CL suggestions:** CL:0000062 (osteoblast), CL:0000138 (chondrocyte), CL:0000134 (mesenchymal stem cell)

### Subcellular level
- Secretory pathway (signal peptide-directed secretion; furin-like cleavage in the spacer domain)
- Lipid-raft plasma-membrane microdomains (site of BMP receptor complex recruitment)

**GO Cellular Component suggestions:** GO:0005886 (plasma membrane), GO:0005615 (extracellular space), GO:0009986 (cell surface)

### Localization
Bilateral/symmetric skeletal and craniofacial involvement is the norm (no lateralization pattern reported).

---

## 8. Temporal Development

- **Onset:** Prenatal — intrauterine growth restriction is documented (e.g., birth weight −3.7 SDS), i.e., this is a **congenital** disorder with onset in utero, continuing into postnatal short stature.
- **Onset pattern:** Insidious/constitutional rather than acute; the phenotype is present from birth and evolves through childhood (craniofacial gestalt reported to become more distinctive with age — e.g., the "long triangular face" description specifically noted "in older individuals").
- **Progression:** Predominantly a **stable, non-progressive** malformation/growth syndrome rather than a degenerative one — skeletal and facial features are developmental in origin rather than accumulating damage over time, though formal natural-history/longitudinal cohort data have not yet been published given the small number of known cases.
- **Disease course pattern:** Chronic, lifelong (structural/skeletal and dental anomalies persist); no remission pattern is applicable, as this is not an episodic or relapsing-remitting condition.
- **Critical periods:** Embryonic/early fetal development (branchial arch, nasal/otic placode, limb bud, and dental primordia stages, per mouse expression data at E9.5–E15.5) represents the biologically critical window during which SCUBE3-dependent BMP signaling shapes the ultimate craniofacial and skeletal phenotype — though this is inferred from mouse expression timing rather than direct human intervention-window data.

Sources: [PMC12052373](https://pmc.ncbi.nlm.nih.gov/articles/PMC12052373/) · ["The biology of SCUBE," PMC10214685](https://pmc.ncbi.nlm.nih.gov/articles/PMC10214685/)

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence/incidence:** Not formally calculated (no population-based ascertainment); the condition is described simply as **"very rare,"** with **approximately 20–25 patients reported in the literature to date** (18 in the founding 2021 cohort across 9 families, plus subsequent isolated case reports in 2024–2025).
- No GBD, SEER, or national-registry prevalence estimate exists — this reflects extreme rarity and likely under-ascertainment/under-diagnosis rather than a truly established low prevalence.

### Genetic inheritance
- **Pattern:** Autosomal recessive.
- **Penetrance:** Appears complete/full in reported biallelic carriers, though the small sample size limits confidence in this estimate.
- **Expressivity:** Variable — e.g., presence/absence of cardiac anomalies ("with or without cardiac anomalies" in the disease name itself), presence/absence of learning difficulty, and presence/absence of conductive hearing loss all vary between affected individuals, even reportedly within families (unaffected/heterozygous siblings noted in the 2025 case).
- **Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically reported.
- **Founder effects:** Not established; reported mutations to date are largely private/family-specific, though **consanguinity is a recurring feature** of the pedigrees described (e.g., the Turkish consanguineous family in the 2025 report), suggesting each identified pathogenic allele may function as a local founder variant within that kindred rather than a broadly recurrent population-wide founder mutation.
- **Consanguinity role:** Prominent — multiple reported families are consanguineous, consistent with a recessive, allele-heterogeneous, likely under-ascertained disorder more readily unmasked in consanguineous unions.
- **Carrier frequency:** Not established in any population database (pathogenic alleles essentially absent from gnomAD).

### Population demographics
- **Affected populations:** Reported cases span multiple ancestries/geographies (the founding cohort's 9 families and subsequent Turkish case), without an established ethnic-group-specific enrichment beyond the general observation that consanguineous populations are overrepresented among reported pedigrees (an ascertainment effect typical of ultra-rare recessive disorders).
- **Geographic distribution:** No endemic or regionally clustered pattern established; cases are essentially globally sporadic/private.
- **Sex ratio:** No skewing reported (autosomal, not X-linked).
- **Age distribution:** Diagnosed from infancy/childhood onward, consistent with congenital onset.

Sources: [OMIM #619184](https://omim.org/entry/619184) · [PMC12052373](https://pmc.ncbi.nlm.nih.gov/articles/PMC12052373/) · [MalaCards](https://www.malacards.org/card/short_stature_facial_dysmorphism_and_skeletal_anomalies_with_or_without_cardiac_anomalies_2)

---

## 10. Diagnostics

### Clinical tests
- **Radiographic/skeletal survey:** long-bone radiographs (thin/short long bones, radial bowing), rib count (11 pairs), pelvic imaging (narrow iliac wings), spine imaging (scoliosis).
- **Dental radiography/exam:** for hypodontia, taurodontism, crowding, palate assessment.
- **Cardiac evaluation:** echocardiography to screen for ASD/PFO/conduction abnormality (given the "with or without cardiac anomalies" designation, cardiac screening is clinically indicated at diagnosis).
- **Audiology:** given recurrent conductive hearing loss, formal audiometric evaluation is warranted.
- No SSFSC2-specific biomarker (serum/urine analyte) has been established.

### Genetic testing
- **Recommended approach:** Given a recognizable but non-pathognomonic multisystem phenotype (short stature + facial gestalt + skeletal + dental ± cardiac), **exome sequencing (WES) or a skeletal-dysplasia/short-stature gene panel including *SCUBE3*** is the practical diagnostic route, given the extreme rarity and continually expanding mutation spectrum (missense, nonsense, frameshift, splice-site, and structural/intragenic rearrangement variants have all been reported) — single-gene Sanger sequencing alone risks missing structural/splice variants.
- **Chromosomal microarray/karyotype:** not primarily indicated, as the disorder is a single-gene point-variant disease rather than a copy-number/chromosomal disorder, though a broader microarray is often part of standard short-stature diagnostic algorithms to exclude alternative etiologies.
- **Confirmatory testing:** Segregation analysis in parents (typically consanguineous, both heterozygous carriers) supports variant interpretation, as demonstrated in the 2025 case report.
- Protein/structural modeling (e.g., AlphaFold3, AlphaMissense pathogenicity scoring) has been used as supporting evidence for novel missense variant classification under ACMG/AMP guidelines, given the ultra-low prior probability of finding the same variant previously reported.

### Clinical criteria / differential diagnosis
- No formal consensus diagnostic criteria (e.g., DSM/ICD-style) exist for this ultra-rare condition; diagnosis rests on the combination of **recognizable facial gestalt + short stature + skeletal/dental findings + confirmatory biallelic *SCUBE3* variants**.
- **Key differential diagnosis: SSFSC1 (OMIM #617877)** — caused by heterozygous, dominant, haploinsufficient *BMP2* variants. Both conditions share midface retrusion/facial dysmorphism, 11 rib pairs, brachydactyly, and variable cardiac outflow/septal defects, reflecting their shared BMP-pathway mechanism; they are distinguished primarily by **inheritance pattern (dominant BMP2 vs. recessive SCUBE3) and by genetic testing**, since clinical overlap can be substantial.
- Other short-stature/skeletal-dysplasia syndromes with craniofacial dysmorphism (e.g., other BMP/TGF-β pathway disorders) should be considered in the differential given phenotypic overlap in short-stature syndromic presentations generally.

### Screening
No population or newborn screening program exists for this disorder, consistent with its extreme rarity; carrier screening would only be relevant in known-affected families or in consanguineous unions where a familial variant has already been identified.

Sources: [OMIM #617877](https://omim.org/entry/617877) · [PMC12052373](https://pmc.ncbi.nlm.nih.gov/articles/PMC12052373/) · [OMIM #619184](https://omim.org/entry/619184)

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No mortality data are reported; the disorder does not appear to be life-limiting based on the published cohort — cardiac anomalies described (ASD, PFO, first-degree AV block) are generally non-severe/manageable rather than life-threatening congenital heart lesions, though systematic long-term outcome data are lacking given the small number of known patients.
- **Morbidity/function:** Primary morbidity burden relates to short stature, skeletal deformity (scoliosis), dental anomalies requiring orthodontic/dental intervention, and conductive hearing loss; **cognitive/developmental outcome is generally normal**, which is a favorable and clinically important distinguishing prognostic feature relative to many other syndromic short-stature disorders.
- **Quality of life:** Not formally measured; inferred to be shaped predominantly by physical/skeletal and dental burden rather than neurodevelopmental impact.
- **Complications:** Scoliosis, malocclusion/dental crowding requiring orthodontic care, conductive hearing loss potentially requiring management (hearing aids, tympanostomy as indicated), and — in the subset with cardiac involvement — cardiac follow-up.
- **Prognostic factors:** No established biomarker or variant-class predictor of severity yet exists, though truncating/complete-loss-of-function alleles are mechanistically expected to associate with more severe BMP-signaling loss; this has not been formally correlated with outcome across the small published cohort.

---

## 12. Treatment

There is **no disease-specific, mechanism-targeted therapy** for SSFSC2; management is supportive and multidisciplinary, following general principles for syndromic skeletal dysplasia/short-stature care (no dedicated clinical trials or FDA-approved SCUBE3-targeted therapies exist, consistent with the disorder's very recent delineation, 2021, and small patient population).

**Suggested management domains (extrapolated from the phenotype, not from disease-specific trial evidence):**
- **Orthopedic management:** monitoring/management of scoliosis and limb-bone anomalies (NCIT:C16186 — Orthopedic Surgical Procedure; NCIT:C15302 — Physical Therapy as needed)
- **Dental/orthodontic care:** for crowding, hypodontia, taurodontism, malocclusion, and palatal anomalies (relevant NCIT terms include general dental/orthodontic procedure codes; no SCUBE3-specific dental protocol has been published)
- **Cardiac surveillance and, where indicated, intervention:** echocardiographic monitoring; standard ASD/PFO management per general pediatric cardiology practice if hemodynamically significant (NCIT:C15329 — Surgical Procedure, as applicable)
- **Audiology:** hearing aid fitting or other otologic intervention for conductive hearing loss as clinically indicated
- **Growth evaluation:** formal endocrine growth-hormone-axis assessment has not been specifically reported as part of the SSFSC2 phenotype description (the short stature is attributed to a primary skeletal/growth-plate mechanism via defective BMP signaling rather than a hypothalamic-pituitary GH-axis defect), so growth hormone therapy is **not established** as a treatment for this specific condition based on currently published literature; this should be evaluated case-by-case by pediatric endocrinology rather than assumed.
- **Genetic counseling:** recommended given autosomal recessive inheritance, especially in consanguineous families, for recurrence-risk counseling (NCIT:C15240 — Genetic Counseling)
- **Supportive/multidisciplinary care coordination:** given the multisystem nature of the phenotype (NCIT:C15747 — Supportive Care)

**Experimental treatments:** None identified — no registered clinical trials (ClinicalTrials.gov) specifically targeting SCUBE3 or SSFSC2 were found in this research pass, consistent with the disorder's rarity and recent characterization.

**Personalized/precision approaches:** Given SCUBE3's role as a BMP2/4 co-receptor, there is a theoretical mechanistic rationale for future BMP-pathway-modulating approaches (as explored generically in other BMP-signaling skeletal disorders), but no such approach has been developed, tested, or reported specifically for SSFSC2 patients.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (this is a congenital monogenic disorder); the only relevant "primary prevention" lever is **reproductive genetic counseling** in families with a known pathogenic variant, particularly in consanguineous unions, including discussion of carrier testing, prenatal diagnosis, or preimplantation genetic diagnosis (PGD) where a familial variant has been identified (standard practice for known autosomal recessive disorders, though not specifically documented as having been used for SSFSC2 in the literature reviewed).
- **Secondary prevention:** Early diagnosis via genetic testing in at-risk families (previously affected sibling) could enable early multidisciplinary surveillance (cardiac, audiologic, dental, orthopedic) rather than prevention of the underlying malformation itself, since the developmental anomalies are established prenatally/early in embryogenesis.
- **Tertiary prevention:** Standard complication-focused management as described in Treatment above (scoliosis monitoring, dental care, cardiac follow-up, hearing management) to minimize downstream morbidity.
- **Screening:** No population, newborn, or targeted screening program exists; carrier screening is only relevant within families with an established pathogenic variant.

No public-health, environmental, or prophylactic-medication prevention strategies apply, as there is no environmental or modifiable risk factor identified for this disorder.

---

## 14. Other Species / Natural Disease

No naturally occurring SSFSC2-like disease has been reported in companion animals or wildlife (no OMIA entries identified in this research pass). *SCUBE3* orthologs exist across vertebrates (mouse *Scube3*, MGI:3045253; zebrafish *scube3*, ZFIN ZDB-GENE-060717-1), and are studied experimentally (see Model Organisms below) rather than as a naturally occurring veterinary disease entity.

**Taxonomy/orthology:**
- Mouse: *Scube3*, MGI:3045253, NCBI Taxon 10090
- Zebrafish: *scube3*, ZFIN ZDB-GENE-060717-1, NCBI Taxon 7955
- Human ortholog: *SCUBE3*, NCBI Gene 222663, NCBI Taxon 9606

Sources: [MGI:3045253](https://www.informatics.jax.org/marker/MGI:3045253) · [ZFIN scube3](https://zfin.org/ZDB-GENE-060717-1)

---

## 15. Model Organisms

### Mouse models
Three distinct mouse-model lines/studies have characterized *Scube3* loss or mutation:

1. **Constitutive *Scube3* knockout (PLOS One, 2013; PMID 23383134):** Despite a dynamic embryonic expression pattern (neuroectoderm, endoderm, endochondral tissues, especially craniofacial region), constitutive knockout mice show **no overt embryonic phenotype** — mutants are born at expected Mendelian ratios, are viable and fertile, and retain apparently normal Hedgehog signaling activity in craniofacial tissue at the embryonic stage examined. This established that *Scube3* is "dispensable for embryonic survival" despite broad developmental expression — an important negative/limiting finding.
2. **Postnatal phenotyping of the same/related knockout line:** Despite the benign embryonic phenotype, **postnatal *Scube3−/−* mice display craniofacial defects** — misaligned upper/lower incisors, shorter and narrower face, smaller forehead, reduced frontonasal and mandibular regions — indicating the functional requirement for SCUBE3 manifests primarily **postnatally**, a translationally important nuance (the human disease's prenatal growth restriction may reflect a distinct or more severe loss-of-function threshold than the mouse null).
3. **ENU-induced *Scube3^N294K/N294K* mutant line — "The First Scube3 Mutant Mouse Line with Pleiotropic Phenotypic Alterations" (G3: Genes|Genomes|Genetics, 2016; PMC5144972):** This missense allele in calcium-binding EGF-like domain VII produces a **pleiotropic phenotype**: no gross craniofacial abnormality on X-ray, but **malformation of thoracic and lumbar vertebrae, shorter femora** (independent of overall body-size reduction), and **significantly decreased bone mineral density (BMD) and bone mineral content (BMC)**. The mutation is proposed to impair the domain's calcium-dependent homo-/heterodimerization capability, thereby blocking TGFβ/Hedgehog-pathway coupling important for bone development/homeostasis.
4. **Direct disease-modeling knock-in (Lin et al. 2021):** In the founding human-disease paper, *Scube3−/−* mice (a knockout allele used specifically to model the human condition) showed **craniofacial and dental defects, reduced body size, and defective endochondral bone growth attributable to impaired BMP-mediated chondrogenesis and osteogenesis**, which the authors describe as **recapitulating the human disorder** — this is the key translational validation linking mouse loss-of-function to the human SSFSC2 phenotype (fidelity: the paper's own claim is that it recapitulates growth, craniofacial, dental, and skeletal aspects; cardiac and hearing phenotypes were not specifically highlighted as recapitulated).

### Cellular/in vitro models
- **C3H10T1/2 murine mesenchymal cell line:** used to demonstrate SCUBE3's pro-osteogenic, BMP-signaling-potentiating function (ALP induction, enhanced SMAD1/5/8 phosphorylation upon SCUBE3 overexpression).
- ***Scube3−/−* primary cell cultures:** used to show >90% reduction in osteocalcin and reduced mineralization, directly linking loss of SCUBE3 to defective osteoblast differentiation at the cellular level.
- **In vitro variant functional assays** (transcript processing, protein secretion, BMP-signaling activity) were used in Lin et al. 2021 to functionally validate each of the 8 identified patient variants — providing direct human-variant-to-mechanism evidence rather than model-organism-only inference.

### Zebrafish
- Zebrafish *scube3* has been studied for its role in **FGF8/FGFR4 signaling during fast-muscle development**; single *scube3* knockout in zebrafish produces **no overt vascular phenotype**, suggesting redundancy with other SCUBE paralogs (SCUBE1/SCUBE2) for at least some functions — relevant context for interpreting incomplete penetrance of specific phenotype domains (e.g., cardiac, vascular) in both model organisms and humans.

### Model limitations
- The constitutive knockout's benign embryonic phenotype versus the human disease's prenatal-onset growth restriction indicates **imperfect fidelity at the earliest developmental stage**, with mouse phenotype instead manifesting postnatally — a translational caveat worth flagging (a candidate `HUMAN_MODEL_MISMATCH`-type observation: the mouse model's postnatal-onset craniofacial phenotype does not fully recapitulate the human disorder's prenatal growth restriction, though the disease-modeling paper's *Scube3−/−* line is described as recapitulating growth, craniofacial, dental and skeletal features overall).
- Redundancy among SCUBE family paralogs (suggested by zebrafish vascular data) may mask or attenuate phenotypes in single-gene animal models relative to the human disease, particularly for cardiac/vascular phenotypes.

Sources: [PLOS One 2013, PMID 23383134](https://pubmed.ncbi.nlm.nih.gov/23383134/) · [G3 2016 / PMC5144972](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5144972/) · [Lin et al. 2021 AJHG](https://www.sciencedirect.com/science/article/pii/S0002929720304122) · [MGI:3045253](https://www.informatics.jax.org/marker/MGI:3045253) · [ZFIN scube3](https://zfin.org/ZDB-GENE-060717-1)

---

## Notable Gaps / Not Available

- No published prevalence/incidence rate (only "very rare," ~20–25 total reported patients)
- No dedicated quality-of-life instrument data
- No RNA-seq/proteomic/metabolomic profiling of human patient tissue
- No clinical trials or disease-specific pharmacotherapy
- No formal genotype-phenotype correlation study (cohort too small)
- No naturally occurring veterinary/wildlife disease counterpart identified
- No confirmed carrier frequency or founder-variant data in any specific population
- Growth-hormone-axis status is not established as abnormal in this condition (mechanism is primary skeletal/BMP-pathway, not GH-axis), so GH therapy is not a validated treatment for this specific disorder — flagged as an assumption to avoid before curation

---

## Full Source List

- [OMIM #619184 — SSFSC2](https://omim.org/entry/619184)
- [OMIM *614708 — SCUBE3](https://omim.org/entry/614708)
- [OMIM #617877 — SSFSC1 (BMP2)](https://omim.org/entry/617877)
- [MalaCards — SSFSC2](https://www.malacards.org/card/short_stature_facial_dysmorphism_and_skeletal_anomalies_with_or_without_cardiac_anomalies_2)
- [NCBI GTR — Condition C5543057](https://www.ncbi.nlm.nih.gov/gtr/conditions/C5543057/)
- [Lin YC, Niceta M, et al. "SCUBE3 loss-of-function causes a recognizable recessive developmental disorder due to defective bone morphogenetic protein signaling." Am J Hum Genet. 2021;108(1):115-133. PMID 33308444](https://www.sciencedirect.com/science/article/pii/S0002929720304122)
- ["A Novel Homozygous Missense SCUBE3 Variant with Protein Modeling in a Patient Diagnosed as Short Stature, Facial Dysmorphism, and Skeletal Anomalies with or without Cardiac Anomalies 2." PMID 40331102, PMC12052373 (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12052373/)
- [Joustra et al., genetic findings in short Turkish children, PMID 38838658 (cited within PMC12052373)]
- ["The biology of SCUBE" review, PMC10214685](https://pmc.ncbi.nlm.nih.gov/articles/PMC10214685/)
- ["The First Scube3 Mutant Mouse Line with Pleiotropic Phenotypic Alterations," G3: Genes|Genomes|Genetics 2016, PMC5144972](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5144972/)
- ["Scube3 Is Expressed in Multiple Tissues during Development but Is Dispensable for Embryonic Survival in the Mouse," PLOS One, PMID 23383134](https://pubmed.ncbi.nlm.nih.gov/23383134/)
- [MGI:3045253 — mouse Scube3](https://www.informatics.jax.org/marker/MGI:3045253)
- [ZFIN ZDB-GENE-060717-1 — zebrafish scube3](https://zfin.org/ZDB-GENE-060717-1)
- [Ensembl ENSG00000146197 — SCUBE3](https://www.ensembl.org/id/ENSG00000146197)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 7 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.
