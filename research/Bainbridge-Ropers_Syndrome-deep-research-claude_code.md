---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-07-31T18:26:09.014497'
end_time: '2026-07-31T18:44:26.752508'
duration_seconds: 1097.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bainbridge-Ropers syndrome
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 6
  num_turns: 101
  total_cost_usd: 5.717229749999999
  session_id: d9b0cd47-8a1c-40d9-8594-2d81fc6cb2c3
  stop_reason: end_turn
citation_count: 58
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bainbridge-Ropers syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bainbridge-Ropers syndrome** covering all of the
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

# Bainbridge–Ropers Syndrome (ASXL3-Related Disorder) — Comprehensive Research Report

**Prepared:** 2026-07-31 · **Target:** `Bainbridge-Ropers syndrome` · **Category:** Mendelian, autosomal dominant, chromatinopathy / neurodevelopmental

**Verification note (per dismech DR policy):** Every PMID below was retrieved from Europe PMC / NCBI E-utilities during this session, and quoted material is taken from the retrieved abstract text. Ontology identifiers marked **[verify]** were assigned by me from domain knowledge and have *not* been checked with OAK — run `just validate-terms` before committing. Identifiers marked **[OLS-checked]** were confirmed against OLS4 in this session. HPO annotations in §3 were pulled directly from the HPO annotation API for OMIM:615485 and carry authoritative ID↔label pairs.

**NEC preflight:** MONDO:0014205 xrefs to OMIM:615485 and ORPHA:352577; the causal gene named across all retrieved sources is uniformly **ASXL3** (18q12.1). No named-entity confusion detected. The main confusable entities are the *sibling* ASXL disorders (ASXL1/Bohring–Opitz, ASXL2/Shashi–Pena) — these are distinct diseases and are explicitly treated as differential diagnoses below, not as synonyms.

---

## 1. Disease Information

### 1.1 Overview

Bainbridge–Ropers syndrome (BRPS), increasingly referred to in the clinical genetics literature as **ASXL3-related disorder**, is a rare autosomal dominant neurodevelopmental syndrome caused by heterozygous loss-of-function (predominantly de novo truncating) variants in *ASXL3*. It was delineated in 2013 by Bainbridge, Ropers and colleagues through whole-genome/whole-exome sequencing of four undiagnosed probands (PMID:23383720).

The core phenotype is: **global developmental delay / moderate-to-severe intellectual disability, profoundly limited or absent speech, infantile hypotonia, feeding difficulties with failure to thrive, autistic features and other neurobehavioral problems, and a recognizable craniofacial gestalt.**

A concise contemporary definition (PMID:41659201, *Front Neurosci* 2025):

> "Bainbridge-Ropers syndrome (BRPS, OMIM #615485) is a rare, heterogeneous autosomal dominant genetic disease that is mainly characterized by intellectual disability (ID) of varying degrees, developmental delay (DD), language impairments, failure to thrive, behavioral issues, hypotonia, feeding difficulties, and distinctive craniofacial features. It is caused by heterozygous pathogenic variants in the additional sex combs-like 3 (ASXL3, OMIM #615115) gene."

BRPS belongs to the **chromatinopathies / Mendelian disorders of the epigenetic machinery**, and specifically to the **ASXL family disorder triad**:

| Gene | Syndrome | OMIM |
|---|---|---|
| *ASXL1* | Bohring–Opitz syndrome (BOS) | 605039 |
| *ASXL2* | Shashi–Pena syndrome (SHAPNS) | 617190 |
| *ASXL3* | **Bainbridge–Ropers syndrome (BRPS)** | **615485** |

### 1.2 Key identifiers

| Resource | Identifier |
|---|---|
| **MONDO** | **MONDO:0014205** — label: *"severe feeding difficulties-failure to thrive-microcephaly due to ASXL3 deficiency syndrome"* (OLS-checked) |
| OMIM (phenotype) | **615485** — BAINBRIDGE-ROPERS SYNDROME; BRPS |
| OMIM (gene) | **615115** — ASXL TRANSCRIPTIONAL REGULATOR 3; ASXL3 |
| Orphanet | **ORPHA:352577** — "Bainbridge-Ropers syndrome" |
| ICD-10 | **Q87.0** (Orphanet maps ORPHA:352577 as *narrower than* Q87.0, "Congenital malformation syndromes predominantly affecting facial appearance") |
| ICD-11 | Not asserted in the Orphanet cross-reference record retrieved (gap) |
| MeSH (supplementary concept) | **C000726367** |
| UMLS | **C4750837** |
| MedGen | **1656239** |
| DOID | **DOID:0080893** |
| GARD | **13259** |
| NCBI Gene | **80816** (ASXL3; 18q12.1; NC_000018.10:33,578,219–33,751,195) |
| HGNC | **hgnc:29357** (dismech lowercase-prefix convention) |
| UniProt | **Q9C0F0** — Putative Polycomb group protein ASXL3 |
| Ensembl gene | ENSG00000141431 |
| Reference transcript | **NM_030632.3** (used throughout the clinical literature) |
| MGI (mouse ortholog) | MGI:2685175, *Asxl3*, mouse Chr 18 |

### 1.3 Synonyms and alternative names

- Bainbridge-Ropers syndrome / BRPS
- **ASXL3-related disorder** (preferred by GeneReviews and by the Balasubramanian/Woods group; increasingly the recommended label because the phenotype extends beyond the original BRPS description)
- ASXL3-related syndrome
- Severe feeding difficulties–failure to thrive–microcephaly due to ASXL3 deficiency syndrome (Orphanet/MONDO label)
- "Bainbridge-Roppers syndrome" (misspelling retained as a MONDO exact synonym)
- ASXL3 deficiency syndrome
- Historically: "Bohring–Opitz-like syndrome" (superseded — see §10.4)

### 1.4 Provenance of information

Information in this report is **disease-level aggregated** (OMIM, Orphanet, GeneReviews, MONDO, ClinGen, HPO, ClinVar) plus **individual-patient literature** (case reports and multi-centre cohort series totalling >200 published individuals). There is **no EHR-derived / registry-scale phenotyping dataset**. The closest to systematic patient-level data are:

- The **International ASXL3 Natural History Study** (IRAS 316055; 64 individuals, PMID:40552904) — quasi-natural-history design, direct clinic/caregiver consultation.
- The **ARRE Foundation** patient advocacy registry (ASXL Rare Research Endowment) supporting the ASXL1/2/3 deep-phenotyping work at UCLA/CHLA (PMID:38027485, PMID:40808361).
- The **DDD (Deciphering Developmental Disorders) study** and **DECIPHER**, which supplied several published cohorts (PMID:28100473, PMID:29367179, PMID:34436830).

---

## 2. Etiology

### 2.1 Disease causal factors

BRPS is a **monogenic, primarily de novo, haploinsufficiency disorder**. There is no infectious, toxic, or acquired etiology.

**Primary cause:** heterozygous loss-of-function variants in *ASXL3* — nonsense, frameshift, and canonical splice-site variants clustered in exons 11 and 12.

Founding evidence (PMID:23383720, *Genome Med* 2013, HUMAN_CLINICAL):
> "Using genome-wide sequencing, we identified heterozygous, de novo truncating mutations in ASXL3, a transcriptional repressor related to ASXL1, in four unrelated probands. We found that these probands shared similar phenotypes, including severe feeding difficulties, failure to thrive, and neurologic abnormalities with significant developmental delay."

Mechanism of disease causation per GeneReviews (*ASXL3-Related Disorder*, NBK563693, Balasubramanian & Schirwani): **"Loss of function."** ClinGen Dosage Sensitivity assigns **haploinsufficiency score 3 — Sufficient Evidence for Haploinsufficiency** (last evaluated 2017-11-22), citing a haploinsufficiency index of **13.78** and **pLI 1.00**.

### 2.2 Risk factors

**Genetic risk factors**

1. **Causal variants** — see §4. Essentially all reported pathogenic variants are protein-truncating (PTV) or splice-site.
2. **Parental germline / gonosomal mosaicism** — a *bona fide* recurrence-risk factor. GeneReviews: *"Sib recurrence due to presumed parental germline mosaicism has been reported in three families."* Confirmed by ultra-deep sequencing (PMID:40980137, 2025):
   > "We definitively diagnosed this family by WES and found the lowest level of paternal mosaicism reported to date, with a peripheral blood variant allele frequency (VAF) of 8.17% and a semen VAF of 15.03%."
   Also PMID:42194125 (2026): a clinically unaffected mother mosaic at **~15% VAF in peripheral blood DNA** transmitted `c.1648_1649del; p.Met550Aspfs*5` to two half-brothers.
3. **Inherited variants from a mildly affected parent** — established (PMID:36177608; PMID:42494517).
4. **Advanced paternal age** — the generic de novo mutation risk factor. Not specifically quantified for *ASXL3*; **evidence gap**.
5. **Modifier / second-locus effects** — see §4.3.

**Environmental risk factors:** None identified. No toxin, teratogen, occupational, dietary, or infectious risk factor has been associated with BRPS. Sex does not appear to be a strong risk modifier (see §9.4). **Not applicable / no evidence.**

### 2.3 Protective factors

**No genetic or environmental protective factors have been identified.** Two adjacent observations are worth recording:

- **Reduced penetrance / mild expression.** GeneReviews and PMID:34436830 explicitly discuss "nonpenetrance" and mildly affected individuals; PMID:33242595 notes *"The exact molecular mechanism of these mutations resulting in the disease phenotype is still uncertain due to the observation of LOF mutations in healthy population."* Whatever buffers these individuals is unknown — an important open question, not a documented protective factor.
- **A potentially "protective"/therapeutic window** exists in the mouse model: neonatal thyroid hormone supplementation rescues behaviour, but adolescent supplementation does not (bioRxiv PPR1237608; see §6.1 and §12.3).

### 2.4 Gene–environment interactions

No documented GxE interaction. The single mechanistic candidate arising from the 2026 mouse work is a **gene–hormone/nutrient interaction**: *Asxl3* haploinsufficiency depletes brain thyroid hormone via DIO3 derepression, which in principle makes early-life thyroid status a modifiable environmental variable. This is **model-organism-only** and unvalidated in humans.

---

## 3. Phenotypes

### 3.1 GeneReviews frequency table (authoritative aggregate)

GeneReviews *ASXL3-Related Disorder* (NBK563693), Table "Select Features of *ASXL3*-Related Disorder" — reproduced as printed (confirmed on two independent retrievals):

| Feature | % of persons w/feature | Comment |
|---|---|---|
| Speech delay | **100%** | "Most are nonverbal or have very limited speech." |
| Intellectual disability | **99%** | "Typically moderate to severe" |
| Facial dysmorphism | **98%** | See Suggestive Findings |
| Hypotonia | **86%** | "Central hypotonia can be assoc w/↑ tone in upper & lower limbs." |
| Behavioral concerns | **78%** | "Incl autistic traits or an ASD diagnosis" |
| Feeding difficulties | **78%** | "Most affected persons in the early stages are referred w/feeding difficulties & failure to thrive." |
| Skeletal findings | **74%** | — |
| Eyes | **~50%** | "Strabismus is the most common finding." |
| Seizures | **38%** | "GTCS & absence seizures; most have normal brain MRI imaging." |

Independent systematic review (PMID:38420660, *Clin Genet* 2024, Woods et al.):
> "Common phenotypic features comprised global developmental delay or intellectual disability (97%), feeding problems (76%), hypotonia (88%) and characteristic facial features (93%)."

Spanish cohort, n=22 (PMID:39833101, *Clin Genet* 2025):
> "The predominant prenatal finding was intrauterine growth restriction (35%) followed, after birth, by feeding difficulties (90.5%), hypotonia (85.7%), and gastroesophageal reflux disease (82.4%). Later in life, intellectual disability, language impairment, autism spectrum disorder (75%), and joint laxity (73.7%) were noted."

DDD cohort, n=12 (PMID:28100473, *J Med Genet* 2017):
> "severe intellectual disability (11/12), poor/ absent speech (12/12), autistic traits (9/12)" … hypotonia 11/12, feeding difficulties 9/12.

### 3.2 HPO annotations (from HPO annotation API, OMIM:615485)

These are the authoritative curated HPO ID↔label↔frequency triples. Frequencies are *n/N* as curated from source publications (small denominators — treat as qualitative, not population estimates).

**Neurodevelopmental / behavioral**

| HPO ID | Label | Frequency |
|---|---|---|
| HP:0001249 | Intellectual disability | 16/16 |
| HP:0000750 | Delayed speech and language development | 12/12 |
| HP:0001344 | Absent speech | 5/8 |
| HP:0011344 | Severe global developmental delay | 4/4 |
| HP:0001263 | Global developmental delay | 4/4 |
| HP:0000729 | Autistic behavior | 10/13 |
| HP:0000717 | Autism | 1/1 |
| HP:0100023 | Recurrent hand flapping | 3/12 |
| HP:0000733 | Motor stereotypy | 1/1 |
| HP:0100716 | Self-injurious behavior | 1/1 |
| HP:0031936 | Delayed ability to walk | — |
| HP:0002540 | Inability to walk | 1/4 |

**Neurologic / tone**

| HPO ID | Label | Frequency |
|---|---|---|
| HP:0001252 | Hypotonia | 14/15 |
| HP:0001290 | Generalized hypotonia | 1/4 |
| HP:0001276 | Hypertonia | 1/4 |
| HP:0001250 | Seizure | 4/15 |

**Growth / feeding / GI**

| HPO ID | Label | Frequency |
|---|---|---|
| HP:0011968 | Feeding difficulties | 12/15 |
| HP:0001508 | Failure to thrive | 4/4 |
| HP:0033454 | Tube feeding | 3/4 (onset HP:0003593 infantile) |
| HP:0040288 | Nasogastric tube feeding | 3/3 |
| HP:0002020 | Gastroesophageal reflux | 2/4 |
| HP:0002013 | Vomiting | 1/1 |
| HP:0002566 | Intestinal malrotation | 1/12 |
| HP:0001510 | Growth delay | — |
| HP:0001511 | Intrauterine growth retardation | 2/3 (onset HP:0011461 fetal) |
| HP:0001519 | Disproportionate tall stature | 3/12 |

**Craniofacial**

| HPO ID | Label | Frequency |
|---|---|---|
| HP:0000218 | High palate | 11/16 |
| HP:0000494 | Downslanted palpebral fissures | 8/15 |
| HP:0002553 | Highly arched eyebrow | 5/7 |
| HP:0000463 | Anteverted nares | 5/8 |
| HP:0011220 | Prominent forehead | 4/19 |
| HP:0000316 | Hypertelorism | 4/17 |
| HP:0003196 | Short nose | 4/7 |
| HP:0000369 | Low-set ears | 4/7 |
| HP:0000358 | Posteriorly rotated ears | 4/20 |
| HP:0000426 | Prominent nasal bridge | 3/12 |
| HP:0000252 | Microcephaly | 3/8 |
| HP:0000243 | Trigonocephaly | 2/7 |
| HP:0011330 | Metopic synostosis | 1/1 |
| HP:0000664 | Synophrys | 2/12 |
| HP:0000430 | Underdeveloped nasal alae | 2/5 |
| HP:0000331 | Short chin | 2/3 |
| HP:0000347 | Micrognathia | 2/12 |
| HP:0000678 | Dental crowding | 2/12 |
| HP:0000212 | Gingival overgrowth | 1/4 |
| HP:0000232 | Everted lower lip vermilion | — |
| HP:0000154 | Wide mouth | — |
| HP:0000455 | Broad nasal tip | — |
| HP:0002000 | Short columella | 1/1 |
| HP:0000431 | Wide nasal bridge | 1/3 |
| HP:0000527 | Long eyelashes | 1/4 |
| HP:0000278 | Retrognathia | 1/4 |
| HP:0000272 | Malar flattening | 1/12 |
| HP:0000239 | Large fontanelles | 1/4 |
| HP:0030799 | Scaphocephaly | 1/12 |

**Ophthalmologic**

| HPO ID | Label | Frequency |
|---|---|---|
| HP:0000486 | Strabismus | 7/12 |
| HP:0000540 | Hypermetropia | 2/7 |
| HP:0000490 | Deeply set eye | 1/12 |
| HP:0000520 | Proptosis | **0/3** (explicitly negative — key BOS discriminator) |

**Musculoskeletal / limb**

| HPO ID | Label | Frequency |
|---|---|---|
| HP:0009487 | Ulnar deviation of the hand | 3/7 |
| HP:0006191 | Deep palmar crease | 3/4 |
| HP:0001188 | Hand clenching | 2/4 |
| HP:0001166 | Arachnodactyly | 2/12 |
| HP:0002650 | Scoliosis | 1/12 |
| HP:0001763 | Pes planus | 1/12 |
| HP:0009276 | Contracture of 4th finger PIP joint | 1/12 |

**Neuroimaging**

| HPO ID | Label | Frequency |
|---|---|---|
| HP:0002079 | Hypoplasia of the corpus callosum | 1/3 |
| HP:0007068 | Inferior cerebellar vermis hypoplasia | 1/4 |
| HP:0006956 | Lateral ventricle dilatation | 1/1 |

**Other systems**

| HPO ID | Label | Frequency |
|---|---|---|
| HP:0001601 | Laryngomalacia | 1/12 |
| HP:0000452 | Choanal stenosis | 1/12 |
| HP:0000826 | Precocious puberty | 1/2 |
| HP:0001007 | Hirsutism | 2/16 |
| HP:0008070 | Sparse hair | 1/4 |
| HP:0002719 | Recurrent infections | 1/3 |
| HP:0000028 | Cryptorchidism | 1/4 |
| HP:0002558 | Supernumerary nipple | 1/4 |
| HP:0001522 | Death in infancy | 1/4 |
| HP:0011410 | Caesarean section | 9/12 |
| HP:0001561 | Polyhydramnios | 1/12 |
| HP:0001623 | Breech presentation | 1/1 |
| HP:0000006 | Autosomal dominant inheritance | — |

### 3.3 Additional / expanding phenotypes not yet in the HPO annotation set

These are recent, well-documented additions worth curating with their own evidence:

- **Hyperventilation–athetosis** (PMID:28955728, *Neurol Genet* 2017, Dad et al.). Hyperventilation escalating with nervousness, with athetotic movements developing in both upper extremities, especially the hands; interpreted as evidence of "a neural connection, in the context of ASXL3 deficiency, between pathways of respiration and of motor control." Suggested terms: **HP:0002883 Hyperventilation [verify]**, **HP:0002305 Athetosis [verify]**.
- **Breath-holding spells with dystonic posturing, no ictal EEG correlate; refractory** (PMID:35172777). Refractory to iron, acetazolamide, desipramine.
- **Dystonic cerebral palsy phenotype** (PMID:35863334, *Neuropediatrics* 2022): *"infantile-onset limb/trunk dystonic postures and secondarily evolving distal spastic contractures."* Authors conclude *"ASXL3 should be added to target-gene lists used for molecular evaluation of cerebral palsy."* Terms: **HP:0001332 Dystonia [verify]**, **HP:0002061 Lower limb spasticity [verify]**.
- **Developmental coordination disorder** (PMID:38027485, *Front Neurosci* 2023): *"100% of individuals who underwent the development questionnaire met a diagnosis of developmental coordination disorder."* n=7 ASXL3; hypotonia predominant in BRS vs mixed hypo/hypertonia in BOS.
- **Renal phenotype (emerging), obesity in later childhood, antenatal/neonatal structural anomalies, lower-than-expected seizure prevalence** (PMID:40552904, 2025):
  > "Findings include: an increased prevalence of antenatal and neonatal structural anomalies, an emerging renal phenotype, a tendency for poor post-natal growth (with novel reports of obesity later in childhood), and a lower-than-expected prevalence of seizures (compared to the existing literature)."
- **Sleep apnea** — statistically enriched in the NMD and MCR1 subgroups (PMID:42494517). Term: **HP:0010535 Sleep apnea [verify]**.
- **Oro-dental**: high-arched palate, narrow maxilla, posterior crossbite, open bite, fibrotic frenulum, mouth breathing (PMID:40237215, 2025).
- **Prenatal / fetal**: arthrogryposis on ultrasound with neuropathological **pontocerebellar hypoplasia type 1** (PMID:29316359). Terms: **HP:0002505 Arthrogryposis multiplex congenita [verify]**, **HP:0007034 Pontocerebellar hypoplasia [verify]**.
- **Cardiac**: congenital laryngeal cartilage hypoplasia and **dextrocardia** reported as novel complications (PMID:41659201, 2025). Term: **HP:0001651 Dextrocardia [verify]**.
- **Progressive cerebral/cerebellar atrophy** in a severe case (PMID:35172777). Term: **HP:0002059 Cerebral atrophy [verify]**, **HP:0001272 Cerebellar atrophy [verify]**.
- **Precocious/premature pubarche signals** — but note the ASXL1/BOS group carried the stronger signal; *"Findings between the BOS (ASXL1) and BRS (ASXL3) individuals differed, representing distinct pubertal phenotypes within these populations"* (PMID:40808361, 2026).
- **Adolescent-onset feeding difficulty / ARFID** — first report (PMID:38711055, 2024), notable because feeding problems otherwise typically *improve* with age.
- **Precursor B-cell acute lymphoblastic leukemia** — a single pediatric co-occurrence (PMID:35733401). **Interpretation caution:** this is n=1; ASXL1/ASXL2 are established somatic myeloid drivers, so a germline *ASXL3* cancer predisposition is biologically speculative and unproven. Do not curate as an established association.

### 3.4 Phenotype characteristics

**Age of onset.** Congenital to neonatal. IUGR/polyhydramnios/arthrogryposis may be detected prenatally (35% IUGR, PMID:39833101). Hypotonia, feeding difficulty and failure to thrive are apparent in the neonatal period; developmental delay becomes evident in infancy; seizures are childhood-onset (PMID:29367179); ASD diagnosis typically in early childhood.

**Severity.** Highly variable. Historically described as severe, but the spectrum now clearly extends to mild. PMID:40552904: *"We report significant phenotypic variability… We also provide the first qualitative descriptions of several mildly affected probands, at different ages."* Some carriers of inherited variants are clinically unaffected or minimally affected.

**Progression.** Non-degenerative and largely **static with improvement trends**, which is prognostically important:
> "…improvement trends in feeding, hypotonia, verbalisation, and motor skills over time." (PMID:40552904)

Counter-signals: hypotonia may transition to spasticity/contractures (GeneReviews; PMID:35863334); one severe case showed progressive cerebral/cerebellar atrophy (PMID:35172777); one case had adolescent-onset feeding decline (PMID:38711055).

**Course patterns.** Chronic lifelong. Seizures are episodic (GTCS ± atypical absence). Breath-holding/hyperventilation episodes are paroxysmal. Behavioral crises can be episodic and treatable (PMID:39698206).

### 3.5 Quality-of-life impact

No disease-specific EQ-5D/SF-36/PROMIS data exist for BRPS — **evidence gap**. Available proxies:

- **Motor impairment → school engagement.** PMID:38027485 reports motor impairments "negatively impact school engagement" and are "meaningful intervention targets."
- **Unmet rehabilitation need.** PMID:42111080 (*Front Neurol* 2026): *"There exists limited evidence-based medical care and rehabilitation regimen for individuals with BRPS. Thus, the health care needs of individuals with BRPS are hugely unmet."*
- **Caregiver-facing burden of behavior.** PMID:34086428: sleep impairment 71%, disruptive behavior 57%, aggression 57%, self-injurious behavior 43%; *"All 7 patients (100%) had multiple DSM-5 diagnoses."*
- **Communication.** Near-universal absent/limited speech is the single largest driver of functional dependency.
- A generic instrument potentially applicable: QI-Disability / QID-12 for children with intellectual disability (PMID:41920472) — not yet applied to BRPS.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

**ASXL3** (ASXL transcriptional regulator 3), 18q12.1, NCBI Gene 80816, OMIM 615115, HGNC:29357, aliases *BRPS*, *KIAA1713*. Reference transcript **NM_030632.3**. The gene's coding sequence is dominated by two very large exons (11 and 12), which is where essentially all pathogenic variants fall.

**ClinGen Gene–Disease Validity:** *ASXL3* — **Syndromic intellectual disability (MONDO:0000508)** — **Autosomal dominant** — **DEFINITIVE**, Intellectual Disability and Autism GCEP, classified **2021-10-06**. ClinGen explicitly notes: *"ASXL3 will be curated for syndromic intellectual disability because of the variability in reported phenotypes that don't necessarily fall within the bounds of Bainbridge-Ropers syndrome."*

### 4.2 Pathogenic variants

**Variant class distribution.** Overwhelmingly **protein-truncating**: nonsense and frameshift, plus canonical splice-site variants. PMID:38420660: *"The majority of genetic variants were de novo truncating variants in exon 11 or 12 of the ASXL3 gene."* GeneReviews detection rates: sequence analysis **98–99%**, gene-targeted del/dup **1–2%**, CMA rarely.

**Mutational cluster regions (MCRs).** Two clusters are consistently described. The most precise coordinates come from PMID:42494517 (2026):

- **MCR1** = `c.1095_2237`, **exon 11** (n=66 published individuals)
- **MCR2** = `c.3043_4906`, **exon 12** (n=101 published individuals)

MCR2 was the "second mutation cluster region" first identified in PMID:28100473.

**Representative published variants** (all NM_030632.3, all confirmed de novo unless noted):

| Variant (cDNA) | Protein | Source |
|---|---|---|
| c.1897_1898delCA | frameshift | PMID:24044690 (Dinwiddie 2013) |
| c.1210C>T | p.Gln404* | PMID:35863334 (dystonic CP) |
| c.1276del | p.Val426* | PMID:41659201 (novel) |
| c.1612G>T | p.Glu538* | PMID:35172777 |
| c.1648_1649del | p.Met550Aspfs*5 | PMID:42194125 (maternal mosaic, inherited) |
| c.1667_1668del | p.Thr556Argfs*3 | PMID:39610869 (novel) |
| c.2791_2792del | p.Gln931fs | PMID:36177608 (father→son) |
| p.Pro1010Leufs*14 | — | PMID:29445472 |
| c.3324del | p.Lys1109Serfs*34 | PMID:39610869 (novel) |
| c.3349C>T | p.Arg1117* | PMID:29429203 |
| c.3493_3494delTG | p.Cys1165* (exon 12) | PMID:32517662 |
| c.3750del | p.Glu1251Asnfs*5 | PMID:41659201 (novel) |
| c.4330C>T | p.Arg1444* | PMID:41659201 (recurrent) |
| c.4336_4337delAG | p.Arg1446fs*2 | PMID:41659201 (recurrent) |
| c.4441dup | p.Leu1481fs | PMID:36177608 (mother→daughter) |
| c.4534C>T | p.Gln1512* | PMID:36177608 (mother→2 children) |
| c.4678C>T | p.Arg1560* | PMID:39610869 (recurrent, 2 unrelated) |

**Recurrent variants** (useful for prioritization): `p.Arg1444*`, `p.Arg1560*`, `p.Gln1512*` — a systematic recurrent-variant analysis is in PMID:42494517.

**ACMG/AMP classification.** PTVs in the established MCRs meeting de novo criteria are typically **Pathogenic** (PVS1 + PS2 + PM2). **Inherited** PTVs are more difficult: PMID:42494517 cautions that family reports *"may reflect uncertainty about the pathogenicity of inherited ASXL3 variants."*

**ClinVar (queried 2026-07-31, NCBI E-utilities):** **1,086 total records** for `ASXL3[gene]`; **453** records with Pathogenic or Likely Pathogenic clinical significance. (Counts are record-level, not unique-allele-level — treat as approximate.)

**Population allele frequency / constraint.** *ASXL3* is among the most LoF-constrained genes in the genome:
- **pLI = 1.00** (ClinGen dosage curation, citing gnomAD/ExAC)
- **Haploinsufficiency Index = 13.78** (ClinGen)
- **pLI 0.9999** in ExAC (SFARI Gene)
- **LOEUF ≈ 0.23** (gnomAD v4.0) — *reported via secondary source only in this session; **[verify against gnomAD directly]***

Pathogenic BRPS variants are absent from gnomAD (PM2). **Caveat worth curating:** PMID:33242595 notes *"the observation of LOF mutations in healthy population"*, which is why the disease mechanism at MCR level is still debated (see §4.4).

**Somatic vs germline.** BRPS variants are **germline** (constitutional) or **parental mosaic**. *ASXL3* is not an established somatic cancer driver (unlike *ASXL1*/*ASXL2* in myeloid neoplasia). Somatic *ASXL3* mutations appear incidentally in tumour sequencing (e.g., neuroendocrine prostate cancer, ccRCC, T-cell lymphoma studies retrieved in this session) but with **no established driver role**.

**Functional consequence — the NMD vs no-NMD dichotomy.** This is now the leading mechanistic axis. From PMID:42494517 (2026):

> "Statistical comparisons were made between individuals with variants leading to no protein product (nonsense-mediated messenger RNA decay [NMD], *n* = 87) and those with protein-truncating variants (no-NMD, *n* = 117)."
> "Microcephaly, sleep apnea, hyperventilation, and feeding tube use had a statistically increased prevalence in the NMD and MCR1 groups. Intellectual disability and global developmental delay were more severe in the NMD and MCR1 groups and were significant for the MCR1/MCR2 comparison (*P* = .0031 and *P* = .0183). Although autistic features were observed across all groups, the no-NMD and MCR2 cohorts had a higher proportion of individuals with formal autism diagnoses."

This implies **two mechanisms coexist**: true haploinsufficiency (NMD, MCR1 — more severe, more microcephaly) and a **truncated-protein / possible dominant-negative or gain-of-function effect** (no-NMD, MCR2 — more formal autism diagnoses). NMD of the mutant allele was directly demonstrated in patient fibroblasts (PMID:26647312): *"ASXL3 mRNA transcripts from the mutated allele are prone to nonsense-mediated decay, and expression of ASXL3 is reduced."*

**Genotype–phenotype correlation status.** Contradictory across sources — worth curating as a live controversy:
- GeneReviews (2020): *"No genotype-phenotype correlations for ASXL3 have been identified."*
- PMID:39833101 (2025): *"Individuals with variants in the 3' mutational cluster region (MCR) of exon 12 exhibited more perinatal feeding problems, and those with variants in the 5' MCR of exon 11 displayed lower percentiles in height and occipitofrontal circumference, as well as higher frequency of arched eyebrows."*
- PMID:42494517 (2026): statistically significant MCR1 vs MCR2 differences (above).

**Verdict:** correlations are emerging and now statistically supported, superseding the earlier "none identified" statement.

**Missense variants.** Not established as a cause of the autosomal dominant disorder. GeneReviews: *"Missense variants are not thought to be causative for autosomal dominant inheritance. Biallelic missense variants have been reported in four individuals with congenital heart defects; further evidence needed."* PMID:34436830 and PMID:38420660 both flag *"the disease contribution of missense variants"* as an open gap. Separately, PMID:32132929 notes: *"Human genomic studies also identified missense ASXL3 variants associated with autism spectrum disorder, but lacking more severe Bainbridge-Ropers syndromic features."*

### 4.3 Modifier genes and multilocus variation

- **15q11.2 BP1–BP2 microdeletion as a modifier.** PMID:41458212 (2025) reports a 7-month-old with a de novo *ASXL3* nonsense variant plus a paternally inherited (asymptomatic father) 15q11.2 BP1-BP2 microdeletion, with *"severe global developmental delay, hypotonia, feeding difficulties, microcephaly and recurrent respiratory infections"*; authors propose *"multilocus pathogenic variation can generate a blended, severe phenotype"* with *"convergence at the pathway rather than the complex level."* n=1 — hypothesis-generating.
- **Unidentified modifiers.** PMID:42494517: *"The family reports emphasize the possibility of additional, yet currently unidentified, factors influencing phenotypic expression."*
- **Thyroid hormone axis genes** (*DIO3*, *THRA*) — mechanistic modifier candidates from the mouse model (§6.1).

### 4.4 Epigenetic information

*ASXL3* is itself an epigenetic regulator (§6), so "epigenetic information" here has two senses.

**(a) Downstream chromatin consequence.** Elevated **H2AK119Ub1** in patient fibroblasts (PMID:26647312) — the direct chromatin readout of PR-DUB dysfunction.

**(b) DNA methylation episignature — a striking NEGATIVE result.** This is an important, curation-worthy finding. Awamleh et al. (PMID:35361921, *EJHG* 2022) developed a blood DNAm signature for Bohring-Opitz syndrome and tested it on ASXL2 and ASXL3:

> "We identified 763 differentially methylated CpG sites in individuals with BOS. Differentially methylated sites overlapped 323 unique genes, including HOXA5 and HOXB4… The DNAm profile of one individual with the ASXL2 variant was BOS-like, whereas the DNAm profiles of three individuals with **ASXL3 variants were control-like**. We also used Horvath's epigenetic clock, which showed acceleration in DNAm age in individuals with pathogenic ASXL1 variants, and the individual with the pathogenic ASXL2 variant, **but not in individuals with ASXL3 variants**."

**Implications:** (i) there is currently **no validated BRPS episignature** and the BOS classifier cannot be used to interpret *ASXL3* VUS; (ii) *ASXL3* dysfunction is **mechanistically divergent** from *ASXL1* despite paralogy — consistent with the distinct clinical syndromes; (iii) no epigenetic age acceleration in BRPS. n=3 ASXL3 individuals — a dedicated, adequately powered BRPS episignature study is a clear knowledge gap.

**(c) Regulation of *ASXL3* itself.** PMID:38791157 (*Int J Mol Sci* 2024, ASXL-family review): *"Their expression is commonly regulated by DNA methylation at CpG islands preceding transcription starting sites."* The same review notes *"non-coding RNAs have been identified following mutations in the ASXL1 or ASXL3 gene."*

### 4.5 Chromosomal abnormalities

Whole-gene or multi-exon deletions of *ASXL3* are **rare** (GeneReviews: gene-targeted del/dup analysis detects 1–2%; CMA rarely). ClinGen notes *"genomic copy-number variations causing haploinsufficiency in Bainbridge-Ropers syndrome patients have not yet been reported"* as of the 2017 dosage curation — so 18q12.1 deletion patients are under-described relative to what pLI 1.00 predicts. **Triplosensitivity score 0** — *"At this time there is no evidence that supports the triplosensitivity of ASXL3."*

No recurrent translocation, inversion, or aneuploidy mechanism.

---

## 5. Environmental Information

**Environmental factors:** None. BRPS is a fully penetrant-at-the-molecular-level Mendelian disorder; there is no documented toxin, radiation, pollution, or occupational contribution to causation. No entries in CTD linking environmental chemicals to *ASXL3*-mediated BRPS pathogenesis.

**Lifestyle factors:** Not applicable to causation. Relevant to **management**: nutritional intake (failure to thrive early, obesity risk later per PMID:40552904), sleep hygiene (sleep disturbance in 71% per PMID:34086428), and physical activity/rehabilitation (PMID:42111080).

**Infectious agents:** Not applicable to causation. Recurrent infections are reported as a secondary complication (HP:0002719, 1/3; recurrent respiratory infections in PMID:41458212), plausibly secondary to hypotonia, aspiration, and feeding difficulty rather than intrinsic immunodeficiency. No primary immunodeficiency has been characterized in BRPS — **evidence gap**.

**One indirect environmental/nutritional lead:** the mouse thyroid-hormone axis (§6.1) implies early-life thyroid hormone availability could be a modifiable environmental variable — entirely unvalidated in humans.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain

**Node 1 — Molecular scale: heterozygous ASXL3 loss-of-function variant → reduced ASXL3 protein dosage**

De novo truncating variant in exon 11 or 12 → NMD of the mutant transcript (MCR1/NMD class) or production of a truncated protein (MCR2/no-NMD class).

Evidence (PMID:26647312, IN_VITRO, patient fibroblasts):
> "ASXL3 mRNA transcripts from the mutated allele are prone to nonsense-mediated decay, and expression of ASXL3 is reduced."

Suggested annotations: `biological_scale: MOLECULAR`; GO:0000184 nuclear-transcribed mRNA catabolic process, nonsense-mediated decay **[verify]**.

---

**Node 2 — Molecular scale: impaired PR-DUB (Polycomb Repressive Deubiquitinase) complex function**

ASXL3 is a non-catalytic scaffolding subunit of PR-DUB, pairing with the deubiquitinase **BAP1**. Loss of ASXL3 impairs BAP1-mediated removal of monoubiquitin from histone H2A lysine 119.

Evidence (PMID:26647312):
> "We found that ASXL3 interacts with BAP1, a hydrolase that removes mono-ubiquitin from histone H2A lysine 119 (H2AK119Ub1) as a component of the Polycomb repressive deubiquitination (PR-DUB) complex."

UniProt Q9C0F0 confirms: "Core component of the PR-DUB complex containing BAP1, ASXL proteins, and MBD proteins"; interacts with FOXK1, FOXK2, KDM1B, HCFC1, OGT.

Annotations: **GO:0035517 PR-DUB complex [OLS-checked]**; **GO:0140950 histone H2A deubiquitinase activity [OLS-checked]**; GO:0016578 histone deubiquitination **[verify]**; `biological_scale: MOLECULAR`.

---

**Node 3 — Molecular scale: increased H2AK119 monoubiquitination (aberrant chromatin state)**

Evidence (PMID:26647312, IN_VITRO):
> "A significant increase in H2AK119Ub1 was observed in ASXL3 patient fibroblasts, highlighting an important functional role for ASXL3 in PR-DUB mediated deubiquitination."
> "This is the first single gene disorder linked to defects in deubiquitination of H2AK119Ub1…"

Annotations: GO:0000122 negative regulation of transcription by RNA polymerase II **[verify]**; GO:0006325 chromatin organization **[verify]**; GO:0005634 nucleus (CC) **[verify]**; `biological_scale: MOLECULAR`.

---

**Node 4 — Molecular/cellular scale: genome-wide transcriptional dysregulation**

Evidence (PMID:26647312, IN_VITRO):
> "Out of 564 significantly differentially expressed genes (DEGs) in ASXL3 patient fibroblasts, 52% were upregulated and 48% downregulated. DEGs were enriched in molecular processes impacting transcriptional regulation, development and proliferation, consistent with the features of BRS."

Note the roughly symmetric up/down split — consistent with a chromatin scaffold whose loss both derepresses Polycomb targets and destabilizes activation, not a pure repressor.

Broader chromatin context (PMID:38791157): ASXL proteins act *"through interactions with chromatin regulators (PRC2, TrxG, PR-DUB, SRC1, HP1α, and BET proteins) and with transcription factors, including nuclear hormone receptors (RAR, PPAR, ER, and LXR)"*, with associated marks including *"histone H3K9 acetylation and methylation, H3K4 methylation, H3K27 methylation, and H2AK119 deubiquitination."* The nuclear-hormone-receptor arm is mechanistically prescient given Node 5.

---

**Node 5 — Molecular scale (novel, MODEL_ORGANISM): DIO3 derepression → brain thyroid hormone depletion**

This is the single most important new mechanistic result and the first specific, druggable node in BRPS. bioRxiv preprint **PPR1237608** (2026), Ding, Yuan, Hu, Zhang, Wu, Du, Qiu — *"An ASXL3–thyroid hormone axis in parvalbumin interneurons controls autism-like behaviors"*:

> "Mechanistically, Asxl3 loss derepresses the thyroid hormone (TH)–inactivating enzyme DIO3 via altered histone H2A monoubiquitination, depleting brain TH."

**Preprint caveat:** not yet peer-reviewed. Flag accordingly if curated; consider `evidence_source: MODEL_ORGANISM` and a `HUMAN_MODEL_MISMATCH` discussion node.

Annotations: CHEBI:60311 thyroid hormone **[OLS-checked]**; GO:0042403 thyroid hormone metabolic process **[verify]**; `biological_scale: MOLECULAR`.

---

**Node 6 — Cellular scale: disrupted neural cell-fate specification and cortical development**

Two independent model systems converge here.

*Xenopus laevis* (PMID:32132929, MODEL_ORGANISM):
> "We have found that ASXL3 protein knockdown during early embryo development highly perturbs neural cell fate specification, potentially resembling the Bainbridge-Ropers syndrome phenotype in humans."
> "Dynamic chromatin modifications play important roles in the specification of cell fates during early neural patterning and development."

*Mouse Asxl3^+/−* (PPR1237608):
> "Asxl3 haploinsufficiency in mice reduces cortical thickness and upper-layer projection neurons while increasing parvalbumin (PV) interneuron density and producing ASD-like behavioral abnormalities."

Annotations: GO:0021895 cerebral cortex neuron differentiation **[verify]**; GO:0030182 neuron differentiation **[verify]**; GO:0007399 nervous system development **[verify]**. Cell types: **CL:4023018 pvalb GABAergic interneuron [OLS-checked]**; CL:0011001 spinal cord motor neuron *(not applicable)*; use CL:0000679 glutamatergic neuron **[verify]** and CL:0000099 interneuron **[verify]** for the projection-neuron/interneuron pair. `biological_scale: CELLULAR`.

---

**Node 7 — Cellular/tissue scale: excitation–inhibition imbalance via PV interneuron expansion**

PPR1237608 establishes causality through a receptor-conditional knockout:
> "Conditional deletion of the TH receptor Thra in inhibitory neuron progenitors phenocopies the PV interneuron expansion, linking impaired TH signaling to PV circuit remodeling."

Annotations: GO:0051966 regulation of synaptic transmission, glutamatergic **[verify]**; GO:0060079 excitatory postsynaptic potential **[verify]**. `biological_scale: CELLULAR`.

---

**Node 8 — Organism scale: neurodevelopmental phenotype**

Cortical thinning + PV interneuron expansion + E/I imbalance → developmental delay, ID, absent speech, ASD, hypotonia, seizures. In humans, cortical/structural correlates are often subtle or absent — GeneReviews notes seizures occur with *"most have normal brain MRI imaging"* — but where imaging is abnormal the findings are: thin corpus callosum, widened frontal subarachnoid space, deepened sulci (PMID:32517662); cerebellar vermis hypoplasia, ventriculomegaly (HPO); prominence of the Sylvian fissure with bitemporal hollowing (PMID:29445472); pontocerebellar hypoplasia type 1 in a fetus (PMID:29316359); progressive cerebral/cerebellar atrophy in a severe case (PMID:35172777).

---

**Parallel branch — cardiomyocyte proliferation/apoptosis (biallelic missense, congenital heart disease)**

Distinct from the dominant BRPS mechanism. PMID:37435360 (*Biochem Biophys Rep* 2023, IN_VITRO/MODEL_ORGANISM, mouse cardiomyocytes): compound heterozygous *ASXL3* mutations *"inhibited the proliferation of cardiomyocytes and accelerated cell apoptosis by promoting the expression of lncRNAs,"* via lncRNA NONMMUT063967.2 → suppression of FGFR2 → inhibition of Ras/ERK signaling; *"suppression of lncRNA NONMMUT063967.2 and overexpression of FGFR2 reversed the effects."* This corresponds to the GeneReviews note about biallelic missense variants in four individuals with congenital heart defects. **Treat as a separate, provisional allelic mechanism**, not part of the BRPS pathograph.

### 6.2 Upstream vs downstream summary

| Position | Node | Scale |
|---|---|---|
| Upstream (trigger) | *ASXL3* LoF variant → reduced dosage / truncated product | MOLECULAR |
| Upstream | PR-DUB (ASXL3–BAP1) dysfunction | MOLECULAR |
| Convergent hub | ↑ H2AK119Ub1 → transcriptional dysregulation | MOLECULAR |
| Mid | DIO3 derepression → brain TH depletion → THRA signaling loss | MOLECULAR |
| Downstream | Disrupted neural cell-fate specification; ↓ cortical thickness, ↓ upper-layer projection neurons, ↑ PV interneurons | CELLULAR |
| Downstream | Excitation–inhibition imbalance | CELLULAR/TISSUE |
| Terminal | DD/ID, absent speech, ASD, hypotonia, seizures, feeding failure, dysmorphism | ORGANISM |

### 6.3 Other mechanism dimensions

- **Protein dysfunction.** UniProt Q9C0F0: 2,248 aa; **HTH HARE-type domain (aa 10–84)**, **DEUBAD domain (aa 254–363)** — the BAP1-binding module — and an **atypical PHD-type zinc finger (aa 2,210–2,247)**. Note that **MCR1 (c.1095_2237 ≈ aa 365–746) lies immediately C-terminal to the DEUBAD domain**, while **MCR2 (c.3043_4906 ≈ aa 1015–1635)** is mid-protein; **both classes of truncation remove the C-terminal PHD finger**, which is a plausible structural explanation for the shared core phenotype. Mechanism: loss of function (GeneReviews).
- **Metabolic changes.** No classic metabolic derangement. The only metabolic axis implicated is **thyroid hormone inactivation via DIO3** (mouse only). No routine metabolic screen abnormality is described in BRPS.
- **Immune system involvement.** None established. Recurrent infections are likely secondary (aspiration/hypotonia). **Evidence gap.**
- **Tissue damage mechanisms.** BRPS is a **developmental/patterning** disorder, not a degenerative or injury-driven one. No oxidative stress, ischemia, fibrosis, or necrosis mechanism is described. The occasional reports of progressive atrophy are unexplained outliers.
- **Biochemical abnormalities.** No enzyme deficiency, receptor defect, or channelopathy. No diagnostic biomarker.
- **Molecular profiling.**
  - *Transcriptomics:* 564 DEGs in patient fibroblasts, 52% up / 48% down (PMID:26647312). Cortical transcriptomics in mouse (PPR1237608).
  - *Proteomics:* none for BRPS — **gap**.
  - *Metabolomics / lipidomics:* none — **gap**.
  - *Epigenomics:* H2AK119Ub1 ChIP in fibroblasts (PMID:26647312); blood DNAm profiling with **no BRPS-specific signature** (PMID:35361921).
  - *Single-cell / spatial:* none published for BRPS specifically — **gap**. PV-interneuron density quantification in mouse (PPR1237608) is the closest.
  - *Functional genomics screens:* no BRPS-directed CRISPR/RNAi screen — **gap**.
- **Expression pattern.** Human Protein Atlas: low tissue specificity (tau 0.66), with the strongest signal in testis-associated clusters; brain-region RNA data sparse; highest single-cell signal in pituitary stem cells. GeneReviews states ASXL3 is *"expressed in similar tissues to ASXL1 including brain, spinal cord, kidney, liver, and bone marrow, but at a lower level."* MGI GXD records 608 assay results across 9 tissues with embryonic expression across nervous, cardiovascular, musculoskeletal and reproductive systems. **Note the tension:** bulk adult-tissue data understate brain expression, while the developmental and model data place the critical requirement in the **embryonic/fetal brain**. Chromatin regulators binding *"primarily during fetal development"* (PMID:42111080).

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary:** central nervous system — cerebral cortex (thinning, reduced upper-layer projection neurons), corpus callosum (thin/hypoplastic), cerebellum (vermis hypoplasia; pontocerebellar hypoplasia in a fetal case), ventricular system (dilatation).

**Body systems involved:**

| System | Involvement |
|---|---|
| Nervous | Primary — DD/ID, speech, hypotonia→spasticity, seizures, dystonia/athetosis, respiratory-motor coupling abnormality |
| Musculoskeletal | Hypotonia, contractures, ulnar deviation, arachnodactyly, scoliosis, kyphosis, pes planus/planovarus, coxa valga, joint laxity (73.7%) |
| Craniofacial / skeletal | Distinctive gestalt; trigonocephaly/metopic synostosis; high-arched palate; narrow maxilla |
| Digestive | Feeding difficulty, GERD (82.4%), dysphagia/aspiration, intestinal malrotation |
| Respiratory | Laryngomalacia, congenital laryngeal cartilage hypoplasia, sleep apnea, breath-holding/hyperventilation, aspiration pneumonia |
| Ophthalmic | Strabismus (most common), hypermetropia, refractive error |
| Genitourinary / renal | **Emerging renal phenotype** (PMID:40552904) → baseline renal imaging now recommended; cryptorchidism |
| Endocrine | Growth failure then later obesity; pubertal timing questions (PMID:40808361); TH axis (mouse) |
| Cardiovascular | Dextrocardia (single report); congenital heart defects with biallelic missense (provisional) |
| Dental | Crowding, hypodontia, malocclusion, crossbite, open bite, gingival overgrowth |
| Integumentary | Hirsutism, sparse hair, long eyelashes |

**Secondary/complication organs:** lung (aspiration), esophagus (reflux esophagitis), spine (neuromuscular scoliosis), skin (self-injury sequelae).

**UBERON suggestions [all verify]:** UBERON:0000955 brain; UBERON:0000956 cerebral cortex; UBERON:0002336 corpus callosum; UBERON:0002037 cerebellum; UBERON:0004720 cerebellar vermis; UBERON:0002240 spinal cord; UBERON:0001004 respiratory system; UBERON:0001007 digestive system; UBERON:0002113 kidney; UBERON:0000970 eye; UBERON:0001456 face; UBERON:0001474 bone element.

### 7.2 Tissue and cell level

**Tissues:** nervous tissue (cerebral cortical grey matter, white matter tracts, cerebellar cortex); skeletal muscle (secondarily, via central hypotonia — muscle biopsy is not characteristically abnormal); connective tissue (joint laxity); oral mucosa/gingiva.

**Cell populations (CL):**
- **CL:4023018 pvalb GABAergic interneuron [OLS-checked]** — expanded in *Asxl3^+/−* mouse cortex; the central cellular node of the new mechanism. (Human-specific alternative: **CL:4072029 pvalb GABAergic interneuron (Homo sapiens) [OLS-checked]**; related: **CL:0020071 parvalbumin-positive basket cell [OLS-checked]**.)
- Cortical upper-layer projection (glutamatergic) neurons — reduced. CL:0000679 glutamatergic neuron **[verify]**; CL:0011005 GABAergic interneuron **[verify]**.
- Neural progenitor / neural stem cells — cell-fate specification perturbed (Xenopus). CL:0011020 neural progenitor cell **[verify]**.
- Cardiomyocyte — CL:0000746 cardiac muscle cell **[verify]** (biallelic-missense branch only).
- Dermal fibroblast — the principal *ex vivo* experimental cell type (CL:0000057 fibroblast **[verify]**); not a disease-affected cell type per se.

### 7.3 Subcellular level

- **Nucleus** — GO:0005634 **[verify]**; the site of all ASXL3 function.
- **Chromatin / nucleosome** — GO:0000785 chromatin **[verify]**.
- **PR-DUB complex** — **GO:0035517 [OLS-checked]** (the most specific and best-supported cellular-component annotation for ASXL3).

### 7.4 Localization and lateralization

CNS involvement is **bilateral and diffuse/symmetric**. Craniofacial features are symmetric. Ulnar deviation and contractures are typically bilateral. One reported **dextrocardia** (situs abnormality) is a laterality exception in a single patient (PMID:41659201) — do not generalize.

---

## 8. Temporal Development

**Onset**
- **Prenatal (fetal):** IUGR ~35% (PMID:39833101); polyhydramnios; breech presentation; arthrogryposis; pontocerebellar hypoplasia detectable at fetopathology (PMID:29316359). *"An increased prevalence of antenatal and neonatal structural anomalies"* (PMID:40552904).
- **Neonatal/infantile:** hypotonia, feeding difficulty, failure to thrive — the presenting complaint in most. Caesarean delivery 9/12 (HPO).
- **Early childhood:** developmental delay recognized; absent/limited speech; autistic features; strabismus.
- **Childhood:** seizure onset — *"All three had childhood-onset generalized epilepsy"* (PMID:29367179).
- **Adolescence/adulthood:** behavioral escalation; possible obesity; pubertal timing questions; rare late-onset feeding decline (PMID:38711055); rare adult diagnosis (a 28-year-old first diagnosed, PMID:39698206).

**Onset pattern:** congenital, insidious. Not acute.

**Progression**
- **Rate:** slow; substantially **non-progressive/static with improvement** in core domains. PMID:40552904: *"improvement trends in feeding, hypotonia, verbalisation, and motor skills over time."*
- **Stages:** no formal staging system exists. A pragmatic natural-history framing from the literature: (1) *infantile* — feeding/hypotonia/FTT dominate; (2) *early childhood* — developmental and communication deficits dominate, seizures may appear; (3) *school-age/adolescent* — behavior, sleep, motor/orthopedic and dental issues dominate, feeding often improves; (4) *adult* — behavioral/psychiatric management, mobility and contracture management.
- **Course:** chronic, lifelong; not relapsing-remitting; seizures and breath-holding are episodic.
- **Divergent trajectories:** hypotonia→spasticity/contracture conversion; rare progressive atrophy.

**Remission patterns:** No spontaneous remission of the core disorder. **Symptom-level remission is achievable**: near-complete remission of self-aggression with pregabalin (PMID:39698206); behavioral reduction of self-injury with ABA (PMID:36249891); feeding independence is often regained.

**Critical periods (intervention windows)**
- **Neonatal/infantile feeding window** — early feeding therapy and timely G-tube placement determine growth trajectory.
- **Early intervention 0–3 years** — GeneReviews-recommended; standard for DD/ID.
- **A biologically defined neonatal window in the mouse model** — PPR1237608: *"Neonatal, but not adolescent, TH supplementation restores PV interneuron numbers and rescues behavior in Asxl3 +/− mice, defining a critical early window for intervention."* If translatable, this would be the most consequential finding in the field. Currently MODEL_ORGANISM only.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **Prevalence: unknown.** GeneReviews: *"The prevalence of ASXL3-related disorder is not known. However, to date ASXL3 is one of the top ten genes in which pathogenic variants have been found in large-scale exome sequencing studies of individuals with ID."*
- **Orphanet (ORPHA:352577, via Orphadata API):**
  - Point prevalence, **class `<1 / 1 000 000`**, Worldwide, Validated → in dismech terms: `measure_type: POINT_PREVALENCE`, `prevalence_class: BELOW_1_IN_1000000`, `rate_per_100000: <0.1`.
  - Cases/families: **77**, Worldwide, Validated (`measure_type: CASES_IN_LITERATURE`), sourced to PMID:28955728. This is now clearly out of date.
- **Published case count over time** (a useful ascertainment curve): 4 (2013, PMID:23383720) → 9 (2016, PMID:27901041) → 27 (2017, PMID:28955728) → 29–33 (2018–2021, PMID:29316359, PMID:33242595) → 45 new + literature (2021, PMID:34436830) → 64 (2025 NHS, PMID:40552904) → **204 individuals in the 2026 literature review** (PMID:42494517). Note PMID:40237215 (2025) still cites "only 45 cases" — the literature is inconsistent; prefer the 2026 figure.
- **Incidence:** no published estimate. **Gap.**
- **Relative diagnostic yield:** ASXL3 recurs in ID/ASD/DD exome cohorts (DDD, DECIPHER, ASC). PMID:28100473 notes the condition's *"surprisingly high frequency."* SFARI: exome-wide significance for ASD in Zhou et al. 2022 (42,607 ASD cases, P < 2.5E-06).

**Curation recommendation:** record Orphanet's `BELOW_1_IN_1000000` point-prevalence class with a note that it is likely an underestimate driven by ascertainment, and record `CASES_IN_LITERATURE: 204` from PMID:42494517 as the current best count.

### 9.2 Inheritance

- **Mode:** **Autosomal dominant** (HP:0000006; HPO-annotated for OMIM:615485). GeneReviews: *"ASXL3-related disorder is an autosomal dominant disorder typically caused by a de novo pathogenic variant."*
- **De novo fraction:** the large majority. PMID:29429203's literature review found *"31 variations in ASXL3 gene…all de novo variations."*
- **Penetrance:** GeneReviews has **no Penetrance heading** (confirmed on direct retrieval). Penetrance is therefore formally **not established**; multiple sources discuss reduced penetrance and nonpenetrance in inherited-variant families (PMID:34436830; PMID:42494517; PMID:33242595 on LoF in healthy individuals). **This is a genuine and important knowledge gap** — flag for a `KNOWLEDGE_GAP` discussion node.
- **Expressivity:** **highly variable, including intrafamilial.** PMID:36177608: *"This report demonstrates intrafamilial phenotypic heterogeneity and confirms heritability of ASXL3-related disorder."*
- **Genetic anticipation:** not applicable (no repeat expansion). No evidence.
- **Germline / parental mosaicism:** **Established and clinically important.** GeneReviews documents germline mosaicism in three families. Directly demonstrated: paternal mosaicism at 8.17% blood VAF / 15.03% semen VAF (PMID:40980137); maternal mosaicism ~15% blood VAF transmitted to two half-brothers (PMID:42194125); parental mosaicism causing non-twin sibling recurrence in the Spanish cohort (PMID:39833101); presumed de novo variant shared by siblings (PMID:29305346).
- **Founder effects:** none identified. Recurrent variants (`p.Arg1444*`, `p.Arg1560*`) reflect mutational hotspots (likely CpG transitions), not founders.
- **Consanguinity:** irrelevant for the dominant disorder. Potentially relevant only for the unproven biallelic-missense/CHD branch.
- **Carrier frequency:** not applicable (dominant, de novo). Population carrier frequency of pathogenic *ASXL3* PTVs is effectively zero (pLI 1.00).

**Recurrence risk counseling (from GeneReviews):**
- Parent carries the variant → **50%** to each sib.
- Variant undetectable in parental leukocyte DNA → *"recurrence risk to sibs is slightly greater than that of the general population because of the possibility of parental germline mosaicism."*
- Offspring of an affected individual → **50%**.
- PMID:40980137 argues for upgrading this: *"This study establishes parental chimerism as an important genetic mechanism for ASXL3-associated disorders and emphasizes the need for ultrasensitive testing in genetic counseling."*

### 9.3 Population demographics

- **Ethnicity/ancestry:** GeneReviews — affected individuals reported *"across all ethnicities,"* with ascertainment concentrated in countries performing genomic testing. Published cohorts: UK/DDD (PMID:28100473, PMID:34436830), Germany/Europe (PMID:27901041), Spain n=22 (PMID:39833101), multiple Chinese cohorts (PMID:41659201, PMID:39610869, PMID:32517662, PMID:35276034), Japan (PMID:29445472, PMID:38711055), Turkey (PMID:40237215), Sudan (PMID:34886823), India (PMID:31638014), USA, Switzerland, Slovakia.
- **Geographic distribution:** worldwide; no endemic focus. Apparent regional clustering reflects genomic-testing access, not biology.
- **Variant geography:** no ancestry-specific variants. PMID:41659201 and PMID:39610869 both suggest *"subtle distinctions in clinical manifestations between Chinese patients and other racial groups"* — likely ascertainment/reporting differences; treat cautiously.
- **Sex ratio:** no significant skew reported. Individual series are small and mixed (PMID:34086428: 5 males, 2 females). **No formal sex-ratio analysis published — gap.**
- **Age distribution:** cohorts are predominantly pediatric, reflecting ascertainment via developmental-disorder testing. Adults are increasingly recognized (28- and 30-year-olds in PMID:39698206; late-onset epilepsy in an older adult male, PMID:29628764). One HPO-annotated "death in infancy" (1/4) at the severe end.

---

## 10. Diagnostics

### 10.1 Genetic testing — the definitive modality

GeneReviews: *"The diagnosis of ASXL3-related disorder is established in a proband by identification of a heterozygous pathogenic (or likely pathogenic) variant in ASXL3 by molecular genetic testing."*

**Recommended approach (GeneReviews):**
1. **Chromosomal microarray (CMA)** first-line, to detect large deletions/duplications (rarely identifies *ASXL3* variants but is standard-of-care for undiagnosed DD/ID).
2. **Intellectual disability multigene panel** or **exome sequencing** if CMA nondiagnostic.
3. **Trio-based exome sequencing** is the workhorse in practice — used in essentially every published cohort (PMID:28100473, PMID:39610869, PMID:41659201, PMID:40980137).

**Detection rates:** sequence analysis **98–99%**; gene-targeted deletion/duplication analysis **1–2%**; CMA rarely.

**Other modalities:**
- **Whole genome sequencing (WGS):** used in the founding study (PMID:23383720). Adds value for splice/deep-intronic/structural variants; no BRPS-specific WGS yield data.
- **Single-gene testing:** appropriate only for targeted familial-variant testing or prenatal/cascade testing.
- **Sanger sequencing:** confirmatory and for segregation analysis (universal in published reports).
- **Ultra-deep / targeted deep sequencing of parental DNA (blood ± semen):** newly recommended when a variant appears de novo but the family wants accurate recurrence-risk counseling (PMID:40980137, PMID:42194125). This is an actionable practice change.
- **Karyotyping, FISH, mtDNA testing, repeat-expansion testing:** **not indicated** for BRPS.

### 10.2 Omics-based diagnostics

- **DNA methylation episignature: NOT available for BRPS.** *"the DNAm profiles of three individuals with ASXL3 variants were control-like"* (PMID:35361921). Do not use the BOS classifier for *ASXL3* VUS. This is a real diagnostic gap for missense/VUS interpretation.
- **RNA sequencing:** not established diagnostically. Research-only demonstration of NMD and 564 DEGs in fibroblasts (PMID:26647312). RNA-seq could in principle confirm NMD for splice VUS.
- **Proteomics, metabolomics, liquid biopsy:** none. **Not applicable.**

### 10.3 Clinical, laboratory, imaging, and functional tests

- **Laboratory tests / biomarkers:** **none.** There is no diagnostic or prognostic biomarker for BRPS. Labs are used for supportive management (nutritional status, growth) only.
- **Imaging:** Brain MRI — most individuals have normal imaging even with seizures (GeneReviews). When abnormal: thin corpus callosum, widened frontal subarachnoid space, deep sulci (PMID:32517662); ventriculomegaly; cerebellar vermis hypoplasia; prominence of the Sylvian fissure with bitemporal hollowing (PMID:29445472); pontocerebellar hypoplasia (fetal, PMID:29316359). **Renal ultrasound** is now recommended at baseline (PMID:40552904). Spine radiography for scoliosis. Prenatal ultrasound may show IUGR/arthrogryposis.
- **Electrophysiology — EEG:** the most informative functional test. PMID:29367179:
  > "EEG typically showed features consistent with generalized epilepsy including generalized spike-wave, photoparoxysmal response, and occipital intermittent rhythmic epileptiform activity."
  Critically, breath-holding/dystonic episodes are **non-epileptic**: *"frequent episodes of breath-holding accompanied by dystonic posturing… without ictal EEG correlate"* (PMID:35172777). Video-EEG is therefore essential to avoid over-treatment with anti-seizure medication.
- **Functional/motor assessment:** quantitative gait analysis + neurological examination + developmental questionnaires (PMID:38027485); a proposed structured neuromotor assessment framework borrowed from cerebral palsy and spina bifida (PMID:42111080).
- **Other functional:** sleep study (polysomnography) for sleep apnea; swallow study / videofluoroscopy for aspiration risk; formal ophthalmologic and dental evaluation; audiology as part of DD workup.
- **Biopsy / histopathology:** **no diagnostic role.** Skin biopsy fibroblasts are used for research only. Fetal neuropathology contributed to one prenatal case (PMID:29316359).

### 10.4 Clinical criteria and differential diagnosis

**Suggestive findings (GeneReviews):** DD/ID (typically moderate-to-severe) **plus** any of — speech/language delay or absent speech; ASD or autistic traits; the dysmorphic gestalt (prominent forehead, highly arched eyebrows, synophrys, widely spaced eyes, downslanted palpebral fissures, long tubular nose, wide mouth with full everted lower lip, crowded teeth); feeding difficulties; hypotonia; poor postnatal growth; epilepsy (GTCS and absence); vision impairment/strabismus; skeletal abnormalities (Marfanoid habitus, pectus excavatum, scoliosis, arachnodactyly, joint contractures).

There is **no consensus clinical diagnostic criteria set** (no DSM/ICD/society criteria); diagnosis is molecular.

**Differential diagnosis — the key discriminations:**

| Condition | Gene | How to distinguish from BRPS |
|---|---|---|
| **Bohring–Opitz syndrome** | *ASXL1* | The historically critical differential. PMID:27901041: *"The majority of key features characteristic for Bohring-Opitz syndrome were absent in our patients (eg, the typical posture of arms, intrauterine growth retardation, microcephaly, trigonocephaly, typical facial gestalt with nevus flammeus of the forehead and exophthalmos). Therefore we emphasize that BRPS syndrome, caused by ASXL3 loss-of-function variants, is a clinically distinct intellectual disability syndrome with a recognizable phenotype distinguishable from that of Bohring-Opitz syndrome."* Also: mixed hypo/hypertonia in BOS vs hypotonia in BRS (PMID:38027485); BOS has a DNAm episignature and epigenetic age acceleration, BRPS does not (PMID:35361921). |
| **Shashi–Pena syndrome** | *ASXL2* | Macrocephaly and abnormal brain imaging (GeneReviews). |
| **Angelman syndrome / AS-like** | *UBE3A* and mimics | *ASXL3* appears in AS-like cohorts (PMID:34653234). Overlap: absent speech, happy demeanor, seizures, ataxia. |
| **Dystonic cerebral palsy** | — | PMID:35863334: *"ASXL3 should be added to target-gene lists used for molecular evaluation of cerebral palsy."* |
| **Pontocerebellar hypoplasia type 1** | *EXOSC3*, *VRK1*, etc. | *ASXL3* now a recognized prenatal PCH1 mimic (PMID:29316359). |
| **Rett/Rett-like, Pitt–Hopkins, Coffin–Siris, Kleefstra, other chromatinopathies** | — | Clinically overlapping ID + limited speech + behaviour; separated by molecular testing. |
| **Nonspecific syndromic ID** | — | GeneReviews notes the DD is nonspecific, so the differential is effectively "all ID disorders"; consult the OMIM AD/AR/XL intellectual developmental disorder phenotypic series. |
| **Breath-holding spells (benign, idiopathic)** | — | In BRPS these are refractory and dystonic (PMID:35172777) — do not dismiss as benign. |
| **Limbic encephalitis** | — | Excluded in the adolescent-onset feeding-decline case (PMID:38711055). |

### 10.5 Screening

- **Newborn screening:** **not applicable** — no biochemical marker; not on any NBS panel.
- **Carrier screening:** **not applicable** (dominant, de novo).
- **Cascade screening:** applicable once a familial variant is identified, especially given documented inherited variants and mildly affected/nonpenetrant relatives.
- **Parental ultra-deep sequencing** (blood ± semen) after an apparently de novo diagnosis — an emerging recommendation (PMID:40980137).
- **Prenatal diagnosis:** amniocentesis with targeted variant testing once the familial variant is known (successfully applied at 18 weeks in PMID:40980137). PMID:36317208 reports prenatal diagnosis for a Chinese BRPS pedigree.

---

## 11. Outcome / Prognosis

**Survival and mortality**
- **No survival curve, 5-/10-year survival, or life-expectancy estimate exists** for BRPS. **Major evidence gap.**
- HPO annotates **HP:0001522 Death in infancy at 1/4** in one small early series — this reflects severe-end ascertainment and should **not** be read as a general infant mortality rate.
- Long-term survival to adulthood is clearly the norm in more recent series: patients diagnosed at 28 and managed at 30 (PMID:39698206); an older adult male with late-onset epilepsy (PMID:29628764); the 2025 NHS cohort spans a wide age range (PMID:40552904).
- Mortality risk is presumably driven by **aspiration, respiratory compromise, refractory seizures, and severe feeding failure** — plausible but not quantified.

**Morbidity and function**
- Morbidity is high and lifelong: near-universal ID with absent/limited speech means most individuals require substantial lifelong support.
- 100% of assessed individuals met criteria for **developmental coordination disorder** (PMID:38027485).
- Motor: ranges from independent ambulation to inability to walk (HP:0002540, 1/4).
- No BRPS-specific ICF/disability or QoL instrument data — **gap**.

**Disease course / complications**
- Aspiration pneumonia and respiratory infections; GERD and esophagitis; failure to thrive then possible obesity; neuromuscular scoliosis and contractures; refractory epilepsy in a minority; refractory breath-holding spells; severe self-injury and aggression; sleep apnea; dental disease; strabismus/amblyopia; emerging renal involvement.
- Single reported precursor B-ALL (PMID:35733401) — **not an established complication.**

**Recovery potential**
- No cure; the underlying developmental lesion is not reversible with current therapy.
- **Meaningful functional gains are documented** and should be communicated to families: *"improvement trends in feeding, hypotonia, verbalisation, and motor skills over time"* (PMID:40552904). Many children wean off tube feeding.
- Behavioral symptoms can respond dramatically to targeted intervention (PMID:39698206, PMID:36249891).

**Prognostic factors**
- **Variant class and location** are the best-supported prognostic markers: NMD-predicted variants and MCR1 (exon 11) variants associate with more severe ID/GDD, more microcephaly, more sleep apnea, more hyperventilation, and more feeding-tube use; MCR2 (exon 12) / no-NMD associate with more formal autism diagnoses and more perinatal feeding problems (PMID:42494517; PMID:39833101).
- Presence of refractory seizures or refractory breath-holding spells marks a severe phenotype (PMID:35172777).
- Age is favorable — older individuals do better in feeding, tone, motor and verbal domains.
- **Prognostic biomarkers: none.**

---

## 12. Treatment

**There is no disease-modifying therapy.** Management is entirely symptomatic, supportive, and multidisciplinary, per GeneReviews.

### 12.1 Supportive and rehabilitative care (the mainstay)

| Manifestation | Intervention | Suggested NCIT / CHEBI |
|---|---|---|
| DD/ID | Early intervention (0–3 y), developmental preschool (3–5 y), IEP, developmental pediatrics, transition planning | NCIT:C15315 Rehabilitation **[verify]** |
| Gross motor / hypotonia / contractures | Physical therapy; durable medical equipment (wheelchairs, walkers, orthotics) | **NCIT:C15302 Physical Therapy**; modality `BEHAVIORAL` |
| Fine motor / adaptive | Occupational therapy | NCIT:C121351 Occupational Therapy **[verify]** |
| Speech / communication | Speech-language therapy; **AAC is essential** given near-universal absent speech | NCIT:C159273 Speech Therapy **[verify]** |
| Feeding / FTT | Feeding therapy; low threshold for clinical feeding evaluation; NG tube then **gastrostomy** if persistent | **NCIT:C52006 Gastrostomy [OLS-checked]**; NCIT:C157864 Gastrostomy Tube Procedure [OLS-checked]; NCIT:C15433 Nutritional Support **[verify]** |
| GERD | Anti-reflux medication; fundoplication in severe cases | NCIT:C15986 Pharmacotherapy; NCIT:C15329 Surgical Procedure **[verify]** |
| Contractures / scoliosis / pes planus | Standard orthopedic management + PT | **NCIT:C16186 Orthopedic Surgical Procedure** |
| Sleep apnea | ENT / sleep specialist; standard treatment | NCIT:C15747 Supportive Care **[verify]** |
| Dental | Preventive dentistry — fissure sealants, fluoride varnish, dietary regulation, interceptive orthodontics (PMID:40237215) | NCIT:C15320 Dental Procedure **[verify]** |
| Strabismus / refractive error | Standard ophthalmologic management, refractive correction | NCIT:C15329 Surgical Procedure **[verify]** |
| Family | Genetic counseling; social work support | **NCIT:C15240 Genetic Counseling** |

A structured, CP/spina-bifida-derived neuromotor assessment-and-management framework is proposed in PMID:42111080 — the first BRPS-specific rehabilitation protocol proposal, though it is a perspective paper, not a trial.

### 12.2 Pharmacotherapy

**Anti-seizure medications.** Standard management by a neurologist for childhood-onset generalized epilepsy with GTCS ± atypical absence (PMID:29367179). Given the generalized phenotype, broad-spectrum agents (valproate, levetiracetam, lamotrigine) are the rational choice; **note there are no BRPS-specific ASM efficacy data.** Encoding: `treatment_term` NCIT:C15986 Pharmacotherapy + `therapeutic_agent` CHEBI term per agent **[verify]**.

**Pregabalin for severe challenging behavior — a notable single-case success.** PMID:39698206 (*Front Psychiatry* 2024), a 30-year-old with BRPS, severe ID, ASD and epilepsy admitted for self-aggression, agitation, hetero-aggression and mood change:
> "The introduction of Pregabalin leads to rapid stabilization of the clinical state, almost complete improvement in challenging behavior and gradual withdrawal of other treatments (class 2 analgesics, neuroleptics, antidepressants, and benzodiazepines). At the neurological check-up 9 months after discharge from hospital, clinical stability was confirmed… with almost complete disappearance of auto-aggressive gestures."
Encoding: `treatment_term` NCIT:C15986 Pharmacotherapy; `therapeutic_agent` **CHEBI:64356 pregabalin [OLS-checked]**; `therapeutic_modality: SMALL_MOLECULE`. **n=1 — curate with appropriate evidence weighting.**

**Failed pharmacotherapy — worth recording as negative evidence.** Refractory breath-holding spells did **not** respond to iron supplementation, acetazolamide, or desipramine (PMID:35172777). Suitable for `supports: REFUTE` / `NO_EVIDENCE` evidence items.

**Psychotropics generally.** Standard management of ADHD, aggression, self-injury, and sleep disturbance; PMID:34086428 documents the high psychiatric comorbidity burden requiring this. No BRPS-specific evidence base.

**Pharmacogenomics:** none specific to BRPS.

### 12.3 Advanced therapeutics — preclinical only

**AAV-delivered split-intein ASXL3 gene replacement — the most advanced therapeutic concept.** From bioRxiv PPR1237608 (2026):
> "An intein-based AAV system that reconstitutes full-length ASXL3 normalizes cortical architecture and behavior in Asxl3 +/− mice and drives efficient ASXL3 expression in non-human primate brain, establishing an ASXL3–TH–PV interneuron axis as a targetable pathway in ASD."

This solves the central obstacle for *ASXL3* gene therapy — the 2,248-aa coding sequence far exceeds AAV packaging capacity — by splitting the transgene across two vectors and reconstituting the protein via split inteins. NHP expression data raise translational plausibility. Encoding if curated: `therapeutic_modality: GENE_THERAPY`; NCIT:C15238 Gene Therapy **[verify]**. **Status: preprint, mouse + NHP expression only. No human data.**

**Neonatal thyroid hormone supplementation.** Same preprint: rescues PV interneuron numbers and behaviour in *Asxl3^+/−* mice when given neonatally but not in adolescence. Potentially repurposable (levothyroxine/liothyronine are approved, cheap, and safe) — but the target is *brain* TH depletion via DIO3, and whether systemic supplementation reaches the brain compartment in humans, and whether a comparable window exists postnatally in humans, is unknown. **Do not present as a clinical option.** Suggested CHEBI: **CHEBI:60311 thyroid hormone [OLS-checked]**; specific agents (levothyroxine, liothyronine) **[verify]**.

**Cell therapy, ASO, siRNA, mRNA, gene editing, immunotherapy, targeted small molecules:** **none reported.** Note that ASO/siRNA knockdown strategies are conceptually inapplicable to a haploinsufficiency disorder; upregulation approaches (TANGO-style, CRISPRa) would be the logical modality and have not been attempted.

### 12.4 Behavioral intervention (best-evidenced non-pharmacologic modality for behavior)

PMID:36249891 (*Behav Anal Pract* 2023) — first published behavioral treatment in BRPS:
> "There are no published treatments for BRPS. We targeted self-injury in a child with BRPS using a functional analysis and differential reinforcement, with several extensions to common procedures. Results present the first example of behavioral reduction for self-injury in BRPS. • ABA strategies can reduce self-injury in BRPS • Evaluating multiply maintained self-injury following identification of an automatic function is important. • Sleep deficits may complicate assessment."

Encoding: `therapeutic_modality: BEHAVIORAL`; NCIT:C181743 Behavioral Counseling **[verify]** (note: OLS search for "applied behavior analysis" returned only NCIT:C204364 *Behavioral Analyst*, a role term, not an intervention — do not use it as a `treatment_term`).

### 12.5 Surgical / interventional

Gastrostomy; Nissen fundoplication for severe GERD; orthopedic surgery for contractures/scoliosis; strabismus surgery; ENT/airway surgery for laryngomalacia or obstructive sleep apnea. All standard-of-care, none BRPS-specific.

### 12.6 Experimental treatments / clinical trials

**No interventional clinical trials in BRPS were identified.** No NCT identifiers. The only registered study found is observational: the **International ASXL3 Natural History Study (IRAS 316055)** (PMID:40552904). This is a therapeutic desert and, given the AAV-intein preclinical result, a natural target for trial-readiness work (biomarker development, outcome-measure validation, patient registry expansion).

### 12.7 Treatment outcomes and strategy

- **Response rates:** not quantifiable — no controlled data. Anecdotal: pregabalin near-complete behavioral remission (n=1); ABA effective for self-injury (n=1); breath-holding refractory to three agents (n=1).
- **Adverse events:** no BRPS-specific safety signal. Standard agent-specific risks apply.
- **Treatment algorithm:** the GeneReviews evaluation/treatment/surveillance tables (§12.1, §13) constitute the de facto algorithm. PMID:40552904 adds two explicit new recommendations: *"baseline renal imaging after diagnosis, and Dental and Ophthalmological follow-up for all."*
- **Personalized/genotype-guided treatment:** none yet — but the MCR1/MCR2 and NMD/no-NMD stratification (PMID:42494517) is the natural substrate for genotype-guided surveillance intensity (e.g., prioritize sleep-apnea and microcephaly surveillance in NMD/MCR1; prioritize autism-specific supports in no-NMD/MCR2).

---

## 13. Prevention

**Primary prevention:** Not possible for de novo variants. The only genuine primary-prevention lever is **reproductive**: preimplantation genetic testing (PGT-M) or prenatal diagnosis for a family with a known variant — GeneReviews: *"Once the ASXL3 pathogenic variant has been identified in an affected family member, prenatal testing for a pregnancy at increased risk and preimplantation genetic testing are possible."* No behavioral, dietary, vaccination, environmental, or public-health intervention prevents BRPS.

**Secondary prevention (early detection):**
- No population or newborn screening.
- Early trio-ES in infants with hypotonia + feeding difficulty + FTT + developmental delay is the practical secondary-prevention route, enabling early intervention.
- **Prenatal detection:** possible via WES in fetuses with arthrogryposis / IUGR / PCH1-pattern findings (PMID:29316359); amniocentesis with targeted testing when a parental mosaic or affected-parent variant is known (PMID:40980137, PMID:36317208).

**Tertiary prevention (preventing complications) — the highest-yield category.** Per GeneReviews surveillance table plus 2025 additions:

| System | Surveillance | Frequency |
|---|---|---|
| Development | Monitor progress and educational needs | Each visit |
| Psychiatric/behavioral | Assess attention, aggression, self-injury; screen for sleep disturbance | Each visit |
| Feeding/growth | Growth measurement, nutritional status, GERD assessment (add obesity screening in later childhood) | Each visit |
| Neurologic | Monitor seizures; assess new manifestations | Each visit / as indicated |
| Musculoskeletal | Physical medicine / PT / OT assessment (contractures, scoliosis) | Each visit |
| Respiratory | Sleep disturbance / apnea signs | Each visit |
| **Renal** | **Baseline renal imaging after diagnosis** (new, PMID:40552904) | At diagnosis |
| Dental | Dentist evaluation | **Every 6 months after age 3 y** — and *"Dental… follow-up for all"* (PMID:40552904) |
| Eyes | Ophthalmology evaluation | **Annually** — and *"Ophthalmological follow-up for all"* (PMID:40552904) |
| Family | Social-work / support assessment | Each visit |

Additional tertiary measures: aspiration precautions and timely gastrostomy; seizure action plan and caregiver education; AAC provision to reduce frustration-driven behavior; multidisciplinary dental prevention (PMID:40237215).

**Genetic counseling:** central. Must cover (i) 50% recurrence for a carrier parent, 50% for offspring of an affected individual; (ii) the **elevated-above-background** sib recurrence risk from germline mosaicism even when parental blood testing is negative; (iii) the case for **ultra-deep parental sequencing** including semen where feasible (PMID:40980137); (iv) the reality of **variable expressivity and possible nonpenetrance** in inherited-variant families, which complicates counseling of apparently unaffected relatives (PMID:42494517).

**Immunization:** routine schedule; no contraindication and no disease-specific vaccine. **Not applicable.**

**Public health / environmental interventions:** **Not applicable.**

**Prophylaxis:** No specific prophylactic medication. Aspiration and respiratory-infection prophylaxis is supportive.

---

## 14. Other Species / Natural Disease

**Taxonomy of species with characterized *ASXL3* orthologs used in disease research:**

| Species | NCBI Taxon | Role |
|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | Disease species |
| *Mus musculus* | NCBITaxon:10090 | Principal disease model (§15) |
| *Xenopus laevis* | NCBITaxon:8355 | Developmental model (PMID:32132929) |
| Non-human primate (species not specified in preprint) | NCBITaxon:9443 (Primates) [verify] | AAV expression/translational testing (PPR1237608) |

**Orthologous genes:** mouse *Asxl3* (**MGI:2685175**, Chr 18, 22,477,303–22,663,072 bp, + strand, 11.96 cM) — direct ortholog of human *ASXL3* (18q12.1). *Xenopus laevis asxl3* — ortholog used for knockdown. The ASXL family (*ASXL1/2/3*) descends from *Drosophila melanogaster* **Additional sex combs (Asx)**; PMID:38791157 notes *"Genes in this family and their neighbor genes are evolutionary conserved in humans and mice."*

**Natural disease in other species:** **None reported.** No OMIA entry, no naturally occurring *ASXL3* disorder in companion animals or wildlife has been described. Veterinary relevance: **none**. (An incidental hit for canine gastrointestinal lymphoma somatic mutations, PMID:40046420, is unrelated to BRPS.)

**Comparative pathology:** BRPS-like phenotypes exist only in engineered models. *Asxl3^+/−* mice recapitulate the ASD-like behavior and cortical architectural changes but the full human syndrome (craniofacial gestalt, absent speech, feeding failure) is not modeled — see §15.

**Evolutionary conservation of mechanism:** strongly conserved. The Asx→ASXL1/2/3 lineage and the PR-DUB complex (Asx–Calypso in fly; ASXL–BAP1 in mammals) are deeply conserved, and H2AK119Ub1 regulation is a core metazoan chromatin mechanism. The *Xenopus* knockdown reproducing neural cell-fate perturbation is direct evidence of conserved developmental function across ~350 My of vertebrate divergence.

**Transmission / zoonotic potential:** **Not applicable** — non-communicable genetic disorder.

---

## 15. Model Organisms

### 15.1 Mouse (*Mus musculus*) — the principal model

**Resources:** MGI:2685175, *Asxl3*. **8 alleles** available (3 endonuclease-mediated, 1 gene-trapped, 4 targeted); **97 strains/lines** listed through IMSR. MGI records **13 phenotypes from multigenic genotypes** and 11 phenotype references. GXD holds 608 expression assay results across 9 tissues with embryonic expression in nervous, cardiovascular, musculoskeletal and reproductive systems.

**IMPC status (Data Release 24.0):** *Asxl3* has been phenotyped with **0 significant phenotypes** across 15 of 24 physiological systems tested (9 systems untested); no adult or embryonic expression data recorded. **This is an important negative:** the standard IMPC broad-based pipeline does not detect the *Asxl3* heterozygote phenotype — CNS/behavioral deep phenotyping is required, which is exactly what the 2026 study supplied.

**The definitive model — *Asxl3^+/−* haploinsufficient mouse** (bioRxiv PPR1237608, 2026; Ding, Yuan, Hu, Zhang, Wu, Du, Qiu):
- **Model type:** germline heterozygous null — genetically faithful to the human dominant LoF mechanism (the correct design; homozygous nulls would model a non-existent human genotype).
- **Phenotype recapitulation:** reduced cortical thickness; reduced upper-layer projection neurons; **increased PV interneuron density**; ASD-like behavioral abnormalities. Molecular: DIO3 derepression via altered H2A monoubiquitination → brain TH depletion.
- **Mechanistic validation:** *Thra* conditional deletion in inhibitory neuron progenitors phenocopies the PV expansion.
- **Therapeutic validation:** neonatal (not adolescent) TH supplementation rescues PV number and behavior; intein-based AAV reconstitution of full-length ASXL3 normalizes cortical architecture and behavior.
- **Limitations:** does not model the craniofacial gestalt, feeding failure/FTT, absent speech (no analog), seizures (not reported), or the human MCR1/MCR2 and NMD/no-NMD distinction (a single null allele cannot capture the truncated-protein class). Preprint status.

**Other mouse work:** PMID:37435360 used mouse cardiomyocytes to model *biallelic missense* ASXL3 mutations and congenital heart disease — a different genotype and a different disease question; not a BRPS model. A closely relevant family model is *Asxl1* loss in mice causing microcephaly via neural stem cell survival (PMID:40276524) — useful for comparative interpretation.

### 15.2 *Xenopus laevis* — developmental patterning model

PMID:32132929 (*Front Physiol* 2020, Lichtig et al.), MODEL_ORGANISM:
> "In this study, we utilize the frog, *Xenopus laevis* as a simpler and more accessible vertebrate neurodevelopmental model system to understand the embryological cause of Bainbridge-Ropers syndrome. We have found that ASXL3 protein knockdown during early embryo development highly perturbs neural cell fate specification, potentially resembling the Bainbridge-Ropers syndrome phenotype in humans. Thus, the frog embryo is a powerful tool for understanding the etiology of Bainbridge-Ropers syndrome in humans."

- **Model type:** morpholino/protein knockdown in early embryos (not a genetic null; standard morpholino specificity caveats apply).
- **Recapitulation:** early neural cell-fate specification defects — captures the *developmental patterning* arm.
- **Limitations:** knockdown rather than heterozygous LoF; early embryonic window only; no behavioral, craniofacial-gestalt, or postnatal readouts; morpholino off-target risk.
- **Applications:** rapid screening of variant function; early neural patterning mechanism; potentially a variant-function assay for missense VUS interpretation (an unexploited opportunity given the absent episignature).

### 15.3 Cellular / in vitro models

- **Patient-derived primary dermal fibroblasts** — the workhorse for the founding mechanism (PMID:26647312): NMD demonstration, H2AK119Ub1 quantification, and RNA-seq (564 DEGs). Limitation: fibroblasts are not a disease-relevant cell type for a brain disorder, so the 564-DEG signature should not be over-interpreted as the neuronal program.
- **iPSC-derived neurons / cortical organoids / neural progenitors:** **not reported for *ASXL3*** — a conspicuous gap. Given the PV-interneuron and upper-layer-projection-neuron findings in mouse, human iPSC-derived cortical and MGE-derived interneuron models are the obvious next step and would be the natural place for MorPhiC-style null-allele cellular phenotyping (`category: Cellular`, `evidence_source: IN_VITRO`). *ASXL3* is not among the MorPhiC anchor genes (ISL1, EOMES, GCM1, NKX2-1).
- **Mouse cardiomyocytes** (PMID:37435360) — biallelic-missense/CHD branch only.

### 15.4 Model resources

MGI (informatics.jax.org, MGI:2685175); IMPC (mousephenotype.org, Data Release 24.0, CC BY 4.0); IMSR (97 *Asxl3* lines); Xenbase; Alliance of Genome Resources.

---

## Summary of Evidence Gaps (for `KNOWLEDGE_GAP` / `HUMAN_MODEL_MISMATCH` curation)

| # | Gap | Type |
|---|---|---|
| 1 | **Penetrance is not established.** GeneReviews has no Penetrance section; LoF variants observed in apparently healthy individuals (PMID:33242595); nonpenetrance discussed in inherited-variant families (PMID:34436830, PMID:42494517) | KNOWLEDGE_GAP |
| 2 | **No prevalence or incidence estimate.** Orphanet's `<1/1,000,000` class and 77-case count are ascertainment-limited and out of date (204 published individuals by 2026) | KNOWLEDGE_GAP |
| 3 | **No survival, life-expectancy, or mortality data** | KNOWLEDGE_GAP |
| 4 | **No validated DNAm episignature** — the BOS classifier returns control-like profiles for ASXL3 (PMID:35361921, n=3), leaving VUS/missense interpretation without a functional assay | KNOWLEDGE_GAP |
| 5 | **Role of missense variants unresolved**; the biallelic-missense/CHD association needs replication (GeneReviews; PMID:38420660) | KNOWLEDGE_GAP |
| 6 | **No human neuronal model.** All neural mechanism is mouse/Xenopus; the PV-interneuron/TH axis has never been tested in human iPSC-derived neurons or patient tissue | HUMAN_MODEL_MISMATCH |
| 7 | **Neonatal-TH-window rescue is mouse-only** and the human developmental equivalent of that window is unknown; the AAV-intein result is mouse + NHP expression only, both in a preprint | HUMAN_MODEL_MISMATCH |
| 8 | **IMPC broad pipeline detects 0 significant phenotypes** for *Asxl3*, despite a clear deep-phenotyping CNS phenotype — model-sensitivity mismatch | HUMAN_MODEL_MISMATCH |
| 9 | **Contradiction on genotype–phenotype correlation:** GeneReviews (2020) says none exist; PMID:39833101 (2025) and PMID:42494517 (2026) report statistically significant MCR/NMD correlations. Curate the 2026 position and note the superseded statement | Controversy |
| 10 | **No interventional clinical trials**, no BRPS-specific QoL instrument data, no proteomic/metabolomic/single-cell/spatial/CRISPR-screen data, no formal sex-ratio analysis, no ICD-11 mapping | KNOWLEDGE_GAP |
| 11 | **Precursor B-ALL co-occurrence (n=1)** — insufficient to assert cancer predisposition; ASXL1/2 somatic myeloid biology makes it tempting but unsupported | Do not curate as association |

---

## Sources

**Primary literature (PubMed / Europe PMC)**
- [PMID:23383720](https://pubmed.ncbi.nlm.nih.gov/23383720/) — Bainbridge MN et al. *Genome Med* 2013 — founding description
- [PMID:24044690](https://pubmed.ncbi.nlm.nih.gov/24044690/) — Dinwiddie DL et al. *BMC Med Genomics* 2013
- [PMID:26647312](https://pubmed.ncbi.nlm.nih.gov/26647312/) — Srivastava A et al. *Hum Mol Genet* 2016 — PR-DUB/H2AK119Ub1 mechanism
- [PMID:27901041](https://pubmed.ncbi.nlm.nih.gov/27901041/) — Kuechler A et al. *Eur J Hum Genet* 2017 — recognizable condition; BOS distinction
- [PMID:28100473](https://pubmed.ncbi.nlm.nih.gov/28100473/) — Balasubramanian M et al. *J Med Genet* 2017 — DDD cohort, second MCR
- [PMID:28955728](https://pubmed.ncbi.nlm.nih.gov/28955728/) — Dad R et al. *Neurol Genet* 2017 — hyperventilation-athetosis
- [PMID:29316359](https://pubmed.ncbi.nlm.nih.gov/29316359/) — Bacrot S et al. *Birth Defects Res* 2018 — first fetal case / PCH1
- [PMID:29367179](https://pubmed.ncbi.nlm.nih.gov/29367179/) — Myers KA et al. *Epilepsy Res* 2018 — childhood-onset generalized epilepsy
- [PMID:29445472](https://pubmed.ncbi.nlm.nih.gov/29445472/) — Chinen Y et al. *Clin Case Rep* 2018
- [PMID:29429203](https://pubmed.ncbi.nlm.nih.gov/29429203/) — Zhang R et al. *Zhonghua Er Ke Za Zhi* 2018
- [PMID:32132929](https://pubmed.ncbi.nlm.nih.gov/32132929/) — Lichtig H et al. *Front Physiol* 2020 — Xenopus model
- [PMID:32517662](https://pubmed.ncbi.nlm.nih.gov/32517662/) — Yang L et al. *BMC Pediatr* 2020 — imaging
- [PMID:33242595](https://pubmed.ncbi.nlm.nih.gov/33242595/) — Yu KP et al. *Eur J Med Genet* 2021 — MCR genotype-phenotype
- [PMID:33751773](https://pubmed.ncbi.nlm.nih.gov/33751773/) — Cuddapah VA et al. *Am J Med Genet A* 2021 — ASXL family spectrum
- [PMID:34086428](https://pubmed.ncbi.nlm.nih.gov/34086428/) — Ikekwere JC et al. *Prim Care Companion CNS Disord* 2021 — psychiatric comorbidity
- [PMID:34436830](https://pubmed.ncbi.nlm.nih.gov/34436830/) — Schirwani S et al. *Am J Med Genet A* 2021 — 45 unpublished individuals
- [PMID:35172777](https://pubmed.ncbi.nlm.nih.gov/35172777/) — Khan TR et al. *BMC Neurol* 2022 — breath-holding + intractable epilepsy
- [PMID:35361921](https://pubmed.ncbi.nlm.nih.gov/35361921/) — Awamleh Z et al. *Eur J Hum Genet* 2022 — DNAm signature (ASXL3 control-like)
- [PMID:35733401](https://pubmed.ncbi.nlm.nih.gov/35733401/) — Slatnick LR et al. *Pediatr Blood Cancer* 2023 — B-ALL case
- [PMID:35863334](https://pubmed.ncbi.nlm.nih.gov/35863334/) — Švantnerová J et al. *Neuropediatrics* 2022 — dystonic CP
- [PMID:36177608](https://pubmed.ncbi.nlm.nih.gov/36177608/) — Schirwani S et al. *Am J Med Genet A* 2023 — familial inheritance, milder phenotype
- [PMID:36249891](https://pubmed.ncbi.nlm.nih.gov/36249891/) — Scheithauer M et al. *Behav Anal Pract* 2023 — ABA for self-injury
- [PMID:37435360](https://pubmed.ncbi.nlm.nih.gov/37435360/) — Liu Z et al. *Biochem Biophys Rep* 2023 — cardiomyocyte / biallelic missense
- [PMID:38027485](https://pubmed.ncbi.nlm.nih.gov/38027485/) — Ayoub MC et al. *Front Neurosci* 2023 — motor phenotyping BOS vs BRS
- [PMID:38420660](https://pubmed.ncbi.nlm.nih.gov/38420660/) — Woods E et al. *Clin Genet* 2024 — molecular phenotyping review
- [PMID:38711055](https://pubmed.ncbi.nlm.nih.gov/38711055/) — Arai Y et al. *BMC Pediatr* 2024 — adolescent-onset feeding difficulty
- [PMID:38791157](https://pubmed.ncbi.nlm.nih.gov/38791157/) — Kim N et al. *Int J Mol Sci* 2024 — ASXL family epigenetics review
- [PMID:39610869](https://pubmed.ncbi.nlm.nih.gov/39610869/) — Ling S et al. *Front Neurosci* 2024
- [PMID:39698206](https://pubmed.ncbi.nlm.nih.gov/39698206/) — Geiser M et al. *Front Psychiatry* 2024 — pregabalin
- [PMID:39833101](https://pubmed.ncbi.nlm.nih.gov/39833101/) — Trujillano L et al. *Clin Genet* 2025 — Spanish cohort n=22
- [PMID:40237215](https://pubmed.ncbi.nlm.nih.gov/40237215/) — Aşık A et al. *Am J Med Genet A* 2025 — dentofacial
- [PMID:40552904](https://pubmed.ncbi.nlm.nih.gov/40552904/) — Woods E et al. *Am J Med Genet A* 2025 — International Natural History Study
- [PMID:40808361](https://pubmed.ncbi.nlm.nih.gov/40808361/) — Piring A et al. *Am J Med Genet A* 2026 — pubertal timing
- [PMID:40980137](https://pubmed.ncbi.nlm.nih.gov/40980137/) — Zhao B et al. *Front Pediatr* 2025 — paternal mosaicism
- [PMID:41458212](https://pubmed.ncbi.nlm.nih.gov/41458212/) — Yang M et al. *Front Genet* 2025 — 15q11.2 modifier
- [PMID:41659201](https://pubmed.ncbi.nlm.nih.gov/41659201/) — Yang Q et al. *Front Neurosci* 2025 — four Chinese patients
- [PMID:42111080](https://pubmed.ncbi.nlm.nih.gov/42111080/) — Yaddanapudi S et al. *Front Neurol* 2026 — rehabilitation framework
- [PMID:42194125](https://pubmed.ncbi.nlm.nih.gov/42194125/) — Mariano D et al. *Children (Basel)* 2026 — familial, maternal mosaicism
- [PMID:42494517](https://pubmed.ncbi.nlm.nih.gov/42494517/) — Woods E et al. *Genet Med Open* 2026 — 204 individuals, NMD/MCR analysis
- [bioRxiv PPR1237608](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22ASXL3%22%20AND%20%22parvalbumin%22) — Ding C et al. 2026 — ASXL3–thyroid hormone–PV interneuron axis (**preprint**)

**Databases and resources**
- [GeneReviews: ASXL3-Related Disorder (NBK563693)](https://www.ncbi.nlm.nih.gov/books/NBK563693/) — Balasubramanian M, Schirwani S
- [OMIM 615485](https://omim.org/entry/615485) (403 during this session; identifiers confirmed via MONDO/Orphanet xrefs) · [OMIM 615115](https://omim.org/entry/615115)
- [MONDO:0014205 via OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0014205)
- [Orphanet ORPHA:352577 — Orphadata API](https://api.orphadata.com/rd-cross-referencing/orphacodes/352577?lang=en) · [epidemiology](https://api.orphadata.com/rd-epidemiology/orphacodes/352577?lang=en)
- [HPO annotations for OMIM:615485](https://ontology.jax.org/api/network/annotation/OMIM:615485)
- [ClinGen ASXL3 gene curation](https://search.clinicalgenome.org/kb/genes/HGNC:29357) · [ClinGen ASXL3 dosage sensitivity](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:29357)
- [UniProt Q9C0F0](https://rest.uniprot.org/uniprotkb/Q9C0F0.json)
- [NCBI Gene 80816](https://www.ncbi.nlm.nih.gov/gene/80816) · [ClinVar ASXL3](https://www.ncbi.nlm.nih.gov/clinvar/?term=ASXL3%5Bgene%5D)
- [MGI:2685175 (mouse Asxl3)](https://www.informatics.jax.org/marker/MGI:2685175) · [IMPC Asxl3](https://www.mousephenotype.org/data/genes/MGI:2685175)
- [SFARI Gene: ASXL3](https://gene.sfari.org/database/human-gene/ASXL3) — score 1S (High Confidence, Syndromic)
- [Human Protein Atlas: ASXL3](https://www.proteinatlas.org/ENSG00000141431-ASXL3/tissue)
- [NORD: ASXL3-Related Disorder](https://rarediseases.org/rare-diseases/asxl3-related-disorder/) · [ARRE Foundation](https://arrefoundation.org/article/genereviews-asxl3-related-disorder/)