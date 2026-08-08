---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-04T22:45:05.255282'
end_time: '2026-08-04T23:09:15.631121'
duration_seconds: 1450.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Juvenile Absence Epilepsy
  mondo_id: ''
  category: Complex
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
  web_search_requests: 30
  num_turns: 58
  total_cost_usd: 5.751017500000001
  session_id: 11bbb8a3-ae44-4969-9d68-106595343893
  stop_reason: end_turn
citation_count: 42
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Juvenile Absence Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Juvenile Absence Epilepsy** covering all of the
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

# Juvenile Absence Epilepsy — Comprehensive Research Report

**Target:** Juvenile Absence Epilepsy (JAE) · **MONDO:0800453** (verified locally against `sqlite:obo:mondo`) · Category: Complex/multifactorial

---

## ⚠️ Read this before you paste anything into YAML

sup — quick housekeeping before the science. This report was assembled from live web search + fetch, and a chunk of the "quotes" below came back through a summarizing layer rather than as raw abstract text. That means **some of them are paraphrases wearing quotation marks**, which is exactly the failure mode dismech's reference validator exists to catch. It's the same problem as a PCR product that looks like the right band on a gel but is actually primer-dimer — plausible shape, wrong molecule.

So:

- Snippets marked **[VERBATIM]** came back as complete abstract text and are very likely exact. Still run them through `just fetch-reference` + `just validate-references`.
- Everything else marked **[PARAPHRASE — DO NOT QUOTE]** must be replaced with a real quote pulled from the cached abstract, or dropped.
- Ontology terms marked **✓OAK** were verified locally in this worktree against the OBO SQLite adapters. Terms marked **⚠unverified** are suggestions only.

---

## 1. Disease Information

### Overview

Juvenile absence epilepsy is one of four syndromes the ILAE recognizes as **idiopathic generalized epilepsies (IGEs)**, which sit inside the broader bucket of **genetic generalized epilepsies (GGEs)**. The other three are childhood absence epilepsy (CAE), juvenile myoclonic epilepsy (JME), and epilepsy with generalized tonic-clonic seizures alone (GTCA).

The core picture: an otherwise neurologically normal adolescent starts having absence seizures around puberty, and — unlike in childhood absence epilepsy — those absences are **infrequent** rather than dozens-to-hundreds per day, and generalized tonic-clonic seizures show up in the great majority of patients. Think of CAE and JAE as the same instrument played at different tempos: CAE is a stuttering metronome, JAE is a slower, heavier bell that also rings the whole body.

**Primary source — the ILAE nosology position statement:**

> **[VERBATIM]** "In 2017, the International League Against Epilepsy (ILAE) Classification of Epilepsies described the 'genetic generalized epilepsies' (GGEs), which contained the 'idiopathic generalized epilepsies' (IGEs). The goal of this paper is to delineate the four syndromes comprising the IGEs, namely childhood absence epilepsy, juvenile absence epilepsy, juvenile myoclonic epilepsy, and epilepsy with generalized tonic-clonic seizures alone. … Patients that do not fulfill criteria for one of these syndromes, but that have one, or a combination, of the following generalized seizure types: absence, myoclonic, tonic-clonic and myoclonic-tonic-clonic seizures, with 2.5–5.5 Hz generalized spike-wave should be classified as having GGE. Recognizing these four IGE syndromes as a special grouping among the GGEs is helpful, as they carry prognostic and therapeutic implications."
> — Hirsch E, French J, Scheffer IE, et al. *Epilepsia* 2022;63(6):1475–1499. **PMID:35503716**, DOI 10.1111/epi.17236. (Note: **not open access** — Europe PMC reports no PMCID.)

### Identifiers

| Resource | Identifier |
|---|---|
| MONDO | **MONDO:0800453** — `juvenile absence epilepsy` (✓OAK) |
| OMIM | **607631** — EPILEPSY, JUVENILE ABSENCE, SUSCEPTIBILITY TO, 1; EJA1 (EFHC1, 6p12) |
| OMIM | **607628** — EPILEPSY, IDIOPATHIC GENERALIZED, SUSCEPTIBILITY TO, 11; EIG11 (contains EJA2 / CLCN2, 3q26) — **see the retraction caveat in §4** |
| ICD-10 | **G40.A** (absence epilepsy syndrome; G40.A0*/G40.A1* intractability/status modifiers). ⚠ verify against a current ICD release — historically JAE was coded under G40.3 (generalized idiopathic epilepsy) |
| ICD-11 | **8A61.1** Absence epilepsies (juvenile absence epilepsy is a subordinate entity) — ⚠ verify code against the current ICD-11 MMS browser |
| MeSH | **D004832** "Epilepsy, Absence" (no JAE-specific MeSH descriptor exists) |
| Orphanet | JAE is covered under ORPHA entries for idiopathic generalized epilepsy; ⚠ a dedicated ORPHA code should be confirmed via `just structured-rebuild-orphanet` / Orphadata rather than guessed |
| epilepsydiagnosis.org | `syndrome/jae-overview.html` (ILAE's own syndrome portal) |

### Synonyms

- Juvenile absence epilepsy (preferred)
- JAE
- Absence epilepsy of adolescence / adolescent-onset absence epilepsy
- "Non-pyknoleptic absence epilepsy" (historical, contrasting with CAE's *pyknolepsy* = dense/clustered absences)
- Janz–Christian "juvenile absence" (historical eponym usage; use with care)

### Data provenance character

Almost everything here is **aggregated disease-level knowledge** — ILAE consensus syndrome definitions, hospital-based retrospective cohorts, and case-series literature. Two exceptions worth noting for dismech:

- **EHR/registry-derived, individual-patient level:** the Danish national-registry cohort (PMID:35595971) links individual JAE cases to school grades and prescription redemptions.
- **Genotype-level population data:** the ILAE Consortium GWAS (PMID:37653029) is individual-genotype based but reports at the GGE-subtype level.

---

## 2. Etiology

### Causal architecture in one sentence

JAE is **complex/polygenic**, not Mendelian. It behaves like a threshold trait: lots of common variants of small effect, plus occasional rare high-impact variants (most importantly *SLC2A1*), summing to a thalamocortical circuit that is too eager to oscillate.

### Genetic risk factors

**Common-variant / polygenic contribution — the strongest modern evidence:**

> **[VERBATIM]** "Epilepsy is a highly heritable disorder affecting over 50 million people worldwide, of which about one-third are resistant to current treatments. Here we report a multi-ancestry genome-wide association study including 29,944 cases, stratified into three broad categories and seven subtypes of epilepsy, and 52,538 controls. We identify 26 genome-wide significant loci, 19 of which are specific to genetic generalized epilepsy (GGE). We implicate 29 likely causal genes underlying these 26 loci. SNP-based heritability analyses show that common variants explain between 39.6% and 90% of genetic risk for GGE and its subtypes. Subtype analysis revealed markedly different genetic architectures between focal and generalized epilepsies. Gene-set analyses of GGE signals implicate synaptic processes in both excitatory and inhibitory neurons in the brain. Prioritized candidate genes overlap with monogenic epilepsy genes and with targets of current antiseizure medications. Finally, we leverage our results to identify alternate drugs with predicted efficacy if repurposed for epilepsy treatment."
> — International League Against Epilepsy Consortium on Complex Epilepsies. *Nat Genet* 2023;55:1471–1482. **PMID:37653029**, DOI 10.1038/s41588-023-01485-w.

That "39.6% to 90%" range is the single most important etiologic number for a JAE entry: **common variation dominates**, and 19 of 26 loci are GGE-specific rather than shared with focal epilepsy. The genetic architecture of JAE is a chorus, not a soloist.

**Rare/monogenic contributions** — see §4 for gene-by-gene detail. Headline: *SLC2A1* (GLUT1 deficiency) is the one genuinely actionable monogenic cause hiding inside absence-epilepsy cohorts.

**Family history:** family history of epilepsy is common in JAE probands. StatPearls reports family history of epilepsy in **41.8%** and parental consanguinity in **40.3%** — but ⚠ that consanguinity figure almost certainly reflects a specific regional cohort rather than JAE generally, and should not be generalized into a dismech entry without tracing the primary source.

### Environmental / non-genetic risk factors

There are no established environmental **causes** of JAE. What exists are well-documented **seizure precipitants** in an already-genetically-susceptible person:

- **Sleep deprivation** — classic and strongly associated with GTCS breakthrough in IGE broadly
- **Hyperventilation** — the most reliable clinical provocateur of absences; 3 minutes of good hyperventilation failing to produce generalized spike-wave makes ongoing absence seizures unlikely (per the ILAE syndrome portal)
- **Photic stimulation** — relevant in a minority (see §3)
- **Alcohol / withdrawal, stress, non-adherence, menstrual cycle**
- **Aggravating drugs** — this is the important one and is genuinely mechanistic, not merely behavioral: sodium-channel blockers and GABAergic drugs that raise thalamic tonic inhibition *worsen* absences (carbamazepine, oxcarbazepine, phenytoin, gabapentin, pregabalin, vigabatrin, tiagabine)

### Protective factors

- **Genetic:** none established. No protective allele has been convincingly reported for JAE. (Contrast with the abundant literature on susceptibility loci — this is a genuine asymmetry in the field.)
- **Environmental/behavioral:** sleep hygiene, adherence, avoidance of the aggravating drugs above, and — in the specific GLUT1-deficient subgroup — **ketogenic diet**, which is arguably the only truly "mechanism-corrective" intervention in the whole absence-epilepsy space.

### Gene–environment interaction

The best-characterized GxE in JAE is **pharmacogenetic** rather than toxicological: an *SLC2A1*-positive patient responds to ketogenic diet in a way a non-carrier does not, and a *POLG*-variant carrier exposed to valproate risks fatal hepatotoxicity (§12). These are the interactions that change clinical decisions. ⚠ Classical toxin/pollutant GxE data for JAE: **not available** — flag as a knowledge gap.

---

## 3. Phenotypes

### 3.1 Absence seizures (the defining feature)

| Attribute | Value |
|---|---|
| Frequency among affected | ~100% (definitional) |
| Onset | Adolescent/peripubertal; range **8–20 y**, peak **9–13 y** (ILAE syndrome portal); StatPearls gives mean onset **12.3 ± 2.8 y**; a 58-patient Chinese cohort gives **11.86 ± 3.87 y** (PMID:40945312) |
| Severity | Moderate — impairment of awareness is typically **less complete** than in CAE |
| Progression | Episodic; often improves with treatment, but frequently lifelong |
| Character | **Non-pyknoleptic**: typically fewer than one per day, versus the tens-to-hundreds daily of CAE. This is *the* clinical discriminator. |
| Duration | Longer than CAE absences (often >10 s; reported up to ~30 s) |
| Semiology extras | Mild eyelid/perioral myoclonus *during* the absence; oral/manual automatisms, classically emerging ~6–10 s after EEG discharge onset |

**HPO suggestions:**
- **HP:0002121** `Generalized non-motor (absence) seizure` ✓OAK — the correct primary term
- **HP:0011147** `Typical absence seizure` ✓OAK — use for the specific typical-absence claim
- **HP:0011149** `Absence seizure with eyelid myoclonia` ✓OAK — only if eyelid myoclonia is documented; note this is also the defining feature of *Jeavons syndrome*, a **differential**, so use carefully
- **HP:0032678** `Eyelid myoclonia seizure` ✓OAK

> ⚠ Note for curators: HP:0002121's label is **"Generalized non-motor (absence) seizure"**, not "Absence seizure." Don't write the colloquial label into `term.label`.

### 3.2 Generalized tonic-clonic seizures

| Attribute | Value |
|---|---|
| Frequency | **79–95%** of JAE patients (StatPearls) — this high fraction is the second key discriminator from CAE |
| Onset | Usually *after* absence onset, but can precede it |
| Timing | Frequently on awakening; sleep-deprivation-sensitive |
| Prognostic weight | Presence of GTCS predicts substantially worse seizure-freedom outcomes (§11) |

**HPO:** **HP:0002069** `Bilateral tonic-clonic seizure` ✓OAK

### 3.3 Myoclonic seizures

| Attribute | Value |
|---|---|
| Frequency | **21–39%** (StatPearls) |
| Nosological caution | Under ILAE 2022, prominent myoclonic seizures are **exclusionary** for JAE except for subtle myoclonus occurring *during* an absence — their presence pushes the diagnosis toward JME |

**HPO:** **HP:0002123** `Generalized myoclonic seizure` ✓OAK; **HP:0032794** `Myoclonic seizure` ✓OAK

### 3.4 Absence status epilepticus

| Attribute | Value |
|---|---|
| Frequency | Commonly cited at **~20%** in JAE — JAE is among the syndromes with the *highest* rate of typical absence status. Typical absence status is reported in **10–30%** of IGE-with-absences overall, versus only **6.7%** in JME |
| Character | Prolonged confusional state lasting ≥10 minutes to hours (rarely days) |
| QoL impact | High — presents as prolonged altered mental status, frequently misdiagnosed as psychiatric or toxic-metabolic encephalopathy |

**HPO:** **HP:0002133** `Status epilepticus` ✓OAK
⚠ **[PARAPHRASE — DO NOT QUOTE]** the "~20%" figure; trace it to a primary series (Agathonikou/Panayiotopoulos-lineage literature) before curating a frequency.

### 3.5 Convulsive status epilepticus

~**6%** (StatPearls) ⚠ paraphrased figure.

### 3.6 Cognitive, academic, and psychiatric phenotypes

This is the part clinicians historically under-weighted, and where the strongest recent population data live.

**Danish national registry cohort** — Boesen MS, Børresen ML, Christensen SK, et al. *J Neurol* 2022;269(9). **PMID:35595971**, DOI 10.1007/s00415-022-11147-2. Cohort: **92 JAE cases**, 190 JME, 27 GTCA, 15,084 non-neurological chronic-disease controls, plus population controls.

Reported for JAE: **~2× hazard for special-needs education** vs. age-matched population controls; lower grade point averages in secondary and high school; **15% fewer JAE patients attended high school**; elevated redemption of sleep medication and ADHD medication vs. chronic-disease controls.
⚠ **[PARAPHRASE — DO NOT QUOTE]** — all of the above came through a summarizer. Fetch and re-quote.

**Other reported figures (all ⚠ paraphrase-level, StatPearls/secondary):**
- Mild-to-severe academic underachievement in **65%**
- Comorbidities affecting learning in **38%**
- Psychiatric comorbidity in **43%** of JAE
- Cognitive deficits occur **even without breakthrough seizures** — i.e., they are not simply a seizure-burden readout

**HPO suggestions:** **HP:0007018** `Attention deficit hyperactivity disorder` ✓OAK · **HP:0000739** `Anxiety` ✓OAK · **HP:0000716** `Depression` ✓OAK · **HP:0002360** `Sleep disturbance` ✓OAK

**Anxiety has direct prognostic weight** — see the Datta cohort in §8/§11.

### 3.7 Antecedent history

- Development, neurological exam, head size, and cognition **normal prior to onset** (ILAE syndrome portal) — this is close to a mandatory feature
- Prior **febrile seizures** occasionally reported — **HP:0002373** `Febrile seizure (within the age range of 3 months to 6 years)` ✓OAK

### 3.8 EEG phenotype (laboratory/electrophysiological)

| Feature | Finding |
|---|---|
| Background | **Normal.** Generalized slowing does not occur; focal slowing should prompt search for a structural lesion |
| OIRDA | Occipital intermittent rhythmic delta activity may be seen |
| Ictal discharge | **Regular 3–5.5 Hz generalized spike-wave or polyspike-wave** with absences |
| Interictal | Generalized spike-wave, fragments of GSW, or polyspike-wave; focal spikes may occur but should not consistently localize |
| Exclusionary | Slow spike-wave **<2.5 Hz** is absent — its presence suggests an alternative diagnosis (e.g., Lennox-Gastaut) |
| vs. CAE | JAE discharges are **slightly faster, more fragmented, and more disorganized** than CAE's regular 3 Hz |
| Activation | Hyperventilation provokes GSW and clinical absences; **3 min of successful hyperventilation without GSW makes absence seizures unlikely**. Sleep deprivation, drowsiness, and sleep enhance abnormalities, though spike-wave fragments in sleep |
| Photoparoxysmal response | Low in JAE — reported around **7.5%** in one IGE-syndrome series and **10%** (2/20) in another |
| ILAE criterion | An ictal EEG is **not required** for diagnosis, provided the interictal study shows paroxysms of **3–5.5 Hz** GSW during wakefulness |

**HPO suggestions:** **HP:0011198** `EEG with generalized epileptiform discharges` ✓OAK · **HP:0012000** `EEG with generalized spikes` ✓OAK · **HP:0011182** `Interictal epileptiform activity` ✓OAK
⚠ Do **not** use HP:0010845 for spike-wave — its real label is `EEG with generalized slow activity` (✓OAK), a different claim entirely.

### 3.9 Quality-of-life impact

Not formally quantified with EQ-5D/SF-36/PROMIS in JAE-specific literature (**gap**). Documented functional impacts:
- **Driving restrictions** — a live issue in GGE; see PMID:38500008 (*J Child Neurol* 2024, "Clearance for Driving in Genetic Generalized Epilepsy")
- **Educational attainment** — the Danish cohort above
- **Self-esteem, aggression, body perception, alexithymia** in adolescent IGE — PMID:41857384 (*Eur J Pediatr* 2026)
- **Lifelong medication burden** — most JAE patients require indefinite treatment

---

## 4. Genetic / Molecular Information

### 4.1 The honest framing

There is **no single causal gene for JAE.** OMIM's "EJA1/EJA2" entries are *susceptibility* loci, and one of the two rests on a retracted paper. A dismech entry should model JAE as polygenic with a small monogenic tail, and should explicitly record the retraction — this is exactly the kind of thing a knowledge base should get right where secondary sources get it wrong.

### 4.2 Named susceptibility genes

**EFHC1 (HGNC:16406 ⚠verify; OMIM \*608815; 6p12) — "EJA1", OMIM #607631**

Susceptibility to juvenile absence epilepsy-1 is conferred by variation in *EFHC1*. The gene was originally established for **JME**:

- Suzuki T, Delgado-Escueta AV, Aguan K, et al. "Mutations in EFHC1 cause juvenile myoclonic epilepsy." *Nat Genet* 2004;36:842–849. **PMID:15258581** ⚠verify PMID. Heterozygous missense variants (229C→A, 662G→A, 685T→C, 628G→A, 757G→T) cosegregating in six Mexican JME families, with **reduced penetrance** (unaffected carriers present). Functional claim: variants reversed EFHC1-induced neuronal cell death and the EFHC1-dependent increase in **R-type Ca²⁺ current**.
- **Critical caveat:** a formal ACMG/NHGRI reanalysis concluded the causality evidence is weak — Subaran/Bailey et al., "EFHC1 variants in juvenile myoclonic epilepsy: reanalysis according to NHGRI and ACMG guidelines for assigning disease causality," *Genet Med* 2016. **PMID:27467453**. Curate *EFHC1* as **DISPUTED/limited**, not established.

**CLCN2 (OMIM \*600570; 3q26) — "EJA2", under OMIM #607628 — RETRACTED PRIMARY EVIDENCE**

This one needs a loud flag in any KB entry:

- Original: Haug K, et al. "Mutations in CLCN2 encoding a voltage-gated chloride channel are associated with idiopathic generalized epilepsies." *Nat Genet* 2003. **PMID:12612585**.
- **Retracted** in *Nat Genet* 2009;41:1043. Grounds: far fewer clinically affected individuals than reported, substantially different pedigree structures and phenotypes, and asymptomatic mutation carriers on re-examination — refuting the claimed complete cosegregation. The authors stated they regretted failing to recognize that important family data were false before publication.
- Subsequent dispute: Niemeyer et al., "No evidence for a role of CLCN2 variants in idiopathic generalized epilepsy," *Nat Genet* 2010;42:3, arguing lack of functional consequence — against Kleefuss-Lie et al. (*Nat Genet* 2009;41:954) who argued some of the original work retained merit.
- Note *CLCN2* **is** a real disease gene — for **CLCN2-related leukoencephalopathy** (GeneReviews, NBK326661) — which is a different phenotype and a classic named-entity trap.

**CACNA1H (Cav3.2 T-type calcium channel; 16p13.3) — the mechanistically satisfying one**

- Heron SE, Khosravani H, Varela D, et al. "Extended spectrum of idiopathic generalized epilepsies associated with CACNA1H functional variants." *Ann Neurol* 2007;62(6):560–568. **PMID:17696120**, DOI 10.1002/ana.21169. >100 heterozygous variants (19 novel) across 240 IGE patients; **9 of 11 tested variants altered channel properties in a gain-of-function manner**.
- Interpretive line worth curating verbatim-ish (⚠ re-quote from abstract): variants **contribute to susceptibility but are not sufficient to cause epilepsy on their own.** This is the textbook "susceptibility modifier, not driver" pattern.
- Variant class: **missense**, germline, **gain-of-function**.
- **Note the correspondence with the GAERS rat model (§15), which carries a gain-of-function Cacna1h R1584P — a rare instance where the human susceptibility gene and the flagship animal model converge on the same channel.**

**SLC2A1 / GLUT1 (1p34.2) — the actionable rare cause**

This is the gene that changes management, because it makes ketogenic diet a mechanism-directed therapy.

- Mullen SA, Suls A, De Jonghe P, Berkovic SF, Scheffer IE. "Absence epilepsies with widely variable onset are a key feature of familial GLUT1 deficiency." *Neurology* 2010;75:432–440. **PMID:20574033**. Two kindreds (9 individuals/3 generations; 6/2 generations). Of **15 SLC2A1 mutation carriers, 12 developed epilepsy**; absence seizures predominated (**10/12**) with onset spanning **3 to 34 years**. Phenotypes: IGE-with-absence 8/12, myoclonic-astatic 2/12, focal 2/12. Paroxysmal exertional dyskinesia in 7, often subtle and previously undiagnosed. Two carriers unaffected (**incomplete penetrance**).
- Arsov T, Mullen SA, Damiano JA, et al. "Early onset absence epilepsy: 1 in 10 cases is caused by GLUT1 deficiency." *Epilepsia* 2012;53(12). **PMID:23106342**. 55 patients with absence onset before age 4; **mutations in 7 (13%)** — five missense, one single-amino-acid in-frame deletion, one two-exon deletion. Pooled across studies: **~12% of 89 patients**. Conclusion: *SLC2A1* analysis should be strongly considered in early-onset absence epilepsy given treatment and genetic-counseling implications.
- Larsen J, et al. *Epilepsia* 2015. **PMID:26537434** — role of SLC2A1 in myoclonic-astatic and absence epilepsy; population frequency of SLC2A1 mutations in Denmark estimated ~**1:83,000**; true GLUT1DS prevalence estimated at least **1:24,000**. **None of 120** MAE patients carried SLC2A1 mutations in that series.
- **JAE-specific caution:** the strongest GLUT1 yield is in **early-onset** absence epilepsy (onset <4 y), not classic peripubertal JAE. Mullen's kindreds show absence onset up to age 34, so JAE-range onset does occur — but a dismech entry should not imply a 10% GLUT1 yield in typical JAE. Mullen et al. also published "GLUT1 mutations are a rare cause of familial idiopathic generalized epilepsy" (*Neurology* 2011) — the deflationary companion paper.

**Other reported susceptibility genes (all weak-to-moderate evidence; curate as SUSCEPTIBILITY, not causal):**

*GRIK1* (allelic variants conferring susceptibility — cited in StatPearls for JAE), *ADGRV1* (familial GGE; see PMC8567843), *CACNA1A*, *CACNB4*, *GABRG2*, *GABRA1*, *GABRB3*. The GABA-A receptor subunit genes are more firmly established in **CAE** than in JAE.

### 4.3 Inheritance / mode

- **Multifactorial/polygenic** for the syndrome as a whole
- **Autosomal dominant with incomplete penetrance** for the *SLC2A1* familial subgroup
- Rare familial aggregation with **syndrome-shifting within families** — a JAE proband may have a JME or GTCA sibling, consistent with shared genetic architecture across IGE

### 4.4 Allele frequency, somatic/germline, functional consequence

- All established variants are **germline**. No somatic contribution reported (**not applicable** for JAE).
- *SLC2A1*: **loss of function** (haploinsufficiency of the blood-brain-barrier glucose transporter)
- *CACNA1H*: **gain of function** (enhanced T-type current)
- *EFHC1*: originally proposed loss of a pro-apoptotic/Ca²⁺-modulatory function — now **disputed**
- gnomAD frequencies: ⚠ not retrieved in this pass; should be pulled per-variant before curation

### 4.5 Modifier genes, epigenetics, chromosomal abnormalities

- **Modifiers:** *CACNA1H* is arguably best modeled as a modifier rather than a driver. No formally validated modifier locus for JAE.
- **Epigenetics:** ⚠ **no JAE-specific methylation/histone data found.** Genuine knowledge gap.
- **Chromosomal abnormalities:** none characteristic. JAE is **not** a CNV syndrome; a pathogenic CNV or abnormal microarray should prompt reconsideration of the diagnosis. (Contrast with 15q13.3/16p13.11/15q11.2 microdeletions in GGE broadly — those *are* enriched in GGE cohorts and are worth a note, but they are not JAE-defining.)

---

## 5. Environmental Information

- **Environmental toxicants:** no established etiologic exposure. **Not applicable / no evidence.**
- **Lifestyle factors:** sleep deprivation, alcohol, and non-adherence are seizure precipitants, not causes. Photic environments (strobes, some video content) matter for the photosensitive minority.
- **Infectious agents:** **not applicable.** JAE is by definition idiopathic; an infectious or inflammatory etiology excludes the syndrome.
- **Nutritional:** the only nutrition-mechanism link is the **ketogenic diet** as *therapy* in GLUT1 deficiency, where ketone bodies bypass the defective glucose transporter — a metabolic detour around a broken bridge.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain, upstream to downstream

Here's the mechanism in the shape dismech wants — a chain of nodes with a clear direction of travel:

```
Polygenic + rare variant load (CACNA1H GoF, SLC2A1 LoF, GABA-A subunit variants,
26 GWAS loci enriched for synaptic genes in excitatory AND inhibitory neurons)
        ↓  [MOLECULAR]
Altered ion-channel gating / synaptic transmission
   — enhanced low-voltage-activated (T-type) Ca²⁺ current in thalamic neurons
   — altered GABA-A/GABA-B mediated inhibition
        ↓  [CELLULAR]
Hyperpolarization → de-inactivation of T-type channels → rebound low-threshold
Ca²⁺ spikes → burst firing in thalamocortical relay neurons and thalamic
reticular nucleus neurons
        ↓  [CELLULAR/TISSUE]
Reciprocal cortico-thalamo-cortical loop entrainment;
cortical initiation focus recruits the loop within ~ms
        ↓  [TISSUE]
Bilaterally synchronous 3–5.5 Hz generalized spike-wave discharge
        ↓  [ORGANISM]
Impairment of awareness / behavioral arrest (absence seizure);
when the same network fails to terminate → absence status epilepticus;
when a different recruitment mode dominates → GTCS
```

### 6.2 The thalamocortical oscillator — the core machinery

The circuit has three players: **cortical glutamatergic pyramidal neurons**, **thalamocortical relay neurons**, and the **GABAergic neurons of the thalamic reticular nucleus (nRT)**. Together they form a resonant loop that normally generates sleep spindles; in absence epilepsy the same loop slips into a pathological 3-Hz mode. It's the difference between a bell rung once and a bell that won't stop.

**The T-type calcium channel is the timing element.** After depolarization, T-type channels briefly pass Ca²⁺ then inactivate; reactivation requires sustained hyperpolarization, which **GABA-B receptor activation** supplies. That non-linear coupling between GABA-B-mediated hyperpolarization and T-type de-inactivation is what sets the oscillation frequency — and it's why GABA-B agonism *worsens* absences while GABA-A-directed benzodiazepines can help.

Channel-subtype distribution:
- **Cav3.1 (CACNA1G)** — highly expressed in **thalamocortical relay neurons**
- **Cav3.2 (CACNA1H)** and **Cav3.3 (CACNA1I)** — mainly in **nRT neurons**

Key references:
- Crunelli V, Leresche N. "Childhood absence epilepsy: genes, channels, neurons and networks." *Nat Rev Neurosci* 2002;3(5):371–382. **PMID:11988776**, DOI 10.1038/nrn811. **[VERBATIM]** — "Childhood absence epilepsy is an idiopathic, generalized non-convulsive epilepsy with a multifactorial genetic aetiology. Molecular-genetic analyses of affected human families and experimental models, together with neurobiological investigations, have led to important breakthroughs in the identification of candidate genes and loci, and potential pathophysiological mechanisms for this type of epilepsy."
- Powell KL, Cain SM, Snutch TP, O'Brien TJ. "The role of T-type calcium channel genes in absence seizures." **PMID:24847307** (*Front Neurol*/review; PMC4023043)
- Tringham E, et al. "T-type calcium channel blockers that attenuate thalamic burst firing and suppress absence seizures." *Sci Transl Med* 2012. **PMID:22344687** — pharmacological proof-of-mechanism.

### 6.3 Cortical focus vs. thalamic pacemaker — a real, curatable controversy

Two competing (now partly reconciled) models of *where* the discharge starts. This is a good candidate for dismech `mechanistic_hypotheses`:

- **Thalamic pacemaker model (CANONICAL, historical):** nRT drives the loop; the thalamus is the metronome.
- **Cortical focus model (now dominant for rodent models):** Meeren HKM, Pijn JPM, van Luijtelaar ELJM, Coenen AML, Lopes da Silva FH. "Cortical focus drives widespread corticothalamic networks during spontaneous absence seizures in rats." *J Neurosci* 2002;22(4):1480–1495. **PMID:11850474**. Nonlinear association analysis in WAG/Rij rats revealed a consistent cortical "focus" in the **peri-oral region of somatosensory cortex**; a cortical focus is the dominant factor initiating the paroxysmal oscillation within corticothalamic loops, with large-scale synchronization mediated by extremely fast intracortical spread. ⚠ re-quote from abstract before curating.
- **HUMAN_MODEL_MISMATCH flag:** the cortical focus is established in **rat genetic models** (WAG/Rij, GAERS). Whether a discrete somatosensory-cortex focus exists in human JAE is not settled — human data point to frontal/thalamic network involvement without a single anatomically stereotyped focus. This is exactly the `HUMAN_MODEL_MISMATCH` discussion kind, not a plain knowledge gap.

Also: Sorokin JM, et al. / McCafferty C, et al. "Cortical drive and thalamic feed-forward inhibition control thalamic output synchrony during absence seizures." *Nat Neurosci* 2018 — a synthesis position: cortex drives, thalamus synchronizes.

### 6.4 Network-level and human neuroimaging findings

**Default mode network / striatal networks — JAE-specific:**

> **[VERBATIM]** "Purpose: To explore the features of dynamic functional connectivity (dFC) variability of striatal-cortical/subcortical networks in juvenile absence epilepsy (JAE). Methods: We collected resting-state functional magnetic imaging data from 18 JAE patients and 28 healthy controls. The striatum was divided into six pairs of regions: the inferior-ventral striatum (VSi), superior-ventral striatum (VSs), dorsal-caudal putamen, dorsal-rostral putamen, dorsal-caudate (DC) and ventral-rostral putamen. We assessed the dFC variability of each subdivision in the whole brain using the sliding-window method, and correlated altered circuit with clinical variables in JAE patients. Results: We found altered dFC variability of striatal-cortical/subcortical networks in patients with JAE. The VSs exhibited decreased dFC variability with subcortical regions, and dFC variability between VSs and thalamus was negatively correlated with epilepsy duration. For the striatal-cortical networks, the dFC variability was decreased in VSi-affective network but increased in DC-executive network. The altered dynamics of striatal-cortical networks involved crucial nodes of the default mode network (DMN). Conclusion: JAE patients exhibit excessive stability in the striatal-subcortical networks. For striatal-cortical networks in JAE, the striatal-affective circuit was more stable, while the striatal-executive circuit was more variable. Furthermore, crucial nodes of DMN were changed in striatal-cortical networks in JAE."
> — Zhang T, Zhang Y, Ren J, et al. *Epilepsy Behav* 2023. **PMID:37925871**

**EEG graph-theory network dynamics in drug-naïve JAE:**

> **[VERBATIM]** "Objective: We aimed to investigate the brain network activity during seizures in patients with untreated juvenile absence epilepsy. Methods: Thirty-six juvenile absence epilepsy (JAE) patients with a current high frequency of seizures (more than five seizures during a 2 h EEG examination) were included. … Results: Compared with the resting state of the HC group, the global efficiency, local efficiency, and clustering coefficients of the JAE group decreased in the inter-ictal state. In addition, the ictal state showed significantly increased global and local efficiency and clustering coefficients (p < 0.05) and a decreased small-world index and the shortest path length (p < 0.05) in the theta and alpha bands, compared to the remaining states within the JAE group. Moreover, subgroup analysis revealed that those JAE patients with typical 3 Hz discharges had upgraded global efficiency, local efficiency, and clustering coefficients in both delta and beta1 bands, compared to those JAE patients with non-3 Hz discharges during seizures. Conclusion: The present study supported the idea that the changes in the EEG brain networks in JAE patients are characterized by decreased global and local efficiency and clustering coefficient in the alpha band. Moreover, the onset of seizures is accompanied by excessively enhanced network efficiency. JAE patients with different ictal discharge patterns may have different functional network oscillations."
> — Tan L, Tang H, Luo H, et al. *Front Neurol* 2024;15:1340959. **PMID:38550342**

**Structural + task-fMRI, with an endophenotype angle (2026, JAE-specific and syndrome-discriminating):**

Xiao F, Caciagli L, Delazer L, et al. "Syndrome-specific and familial imaging traits in juvenile absence epilepsy." *Epilepsia* 2026. **PMID:41531116**. 23 JAE patients, 18 unaffected siblings, 28 controls. Reported: increased motor-cortex activation during an attention-only condition in patients vs. controls and siblings; reduced grey matter volume in sensorimotor and frontal regions; **increased midcingulate grey matter volume as a possible familial (endophenotype) marker related to attentional vulnerability**; and functional reorganization patterns **distinct from JME**. ⚠ **[PARAPHRASE — DO NOT QUOTE]**.

This last one is genuinely valuable for a dismech entry because it separates JAE from JME at the imaging level and offers a heritable-trait node.

### 6.5 Metabolic mechanism (the GLUT1 branch)

In *SLC2A1*-related absence epilepsy the chain is different and cleaner:

```
SLC2A1 haploinsufficiency → reduced facilitated glucose transport across the
blood-brain barrier → chronic cerebral energy deficit (low CSF glucose) →
impaired inhibitory interneuron function / network instability → absence seizures
+ paroxysmal exertional dyskinesia + (variable) intellectual disability
```

Therapeutic corollary: **ketone bodies bypass GLUT1**, hence the ketogenic diet.

### 6.6 Immune, inflammatory, fibrotic, oxidative mechanisms

**Not applicable.** JAE has no established autoimmune, inflammatory, oxidative-stress, or tissue-destruction mechanism. There is **no neurodegeneration, no gliosis, no cell death** — this is a *functional* channelopathy-adjacent network disorder, and imaging/pathology are normal by definition. Any KB entry asserting inflammatory mechanism here would be over-reaching. (Recent Mendelian-randomization papers linking IL-6R and epilepsy subtypes — e.g. PMID:39165549 — are hypothesis-generating at best and should not be curated as mechanism.)

### 6.7 Omics

- **Transcriptomics/proteomics/single-cell/spatial for human JAE:** ⚠ **none found.** Genuine gap. GWAS gene-set analysis implicates synaptic processes in both excitatory and inhibitory neurons (PMID:37653029) — that's the closest thing to a molecular signature.
- **Metabolomics:** PMID:39629734 — "Metabolite Associations with Childhood and Juvenile Absence Epilepsy: A Bidirectional Mendelian Randomization Study" (*Psychiatry Clin Psychopharmacol* 2024). ⚠ MR study, COMPUTATIONAL evidence source, low weight.
- **Functional genomics screens (CRISPR/RNAi):** none JAE-specific.

### Suggested GO terms (all ✓OAK verified locally)

| GO ID | Label | Use |
|---|---|---|
| **GO:0090676** | calcium ion transmembrane transport via low voltage-gated calcium channel | T-type current — the single best-fitting term |
| **GO:0070588** | calcium ion transmembrane transport | broader |
| **GO:0015085** | calcium ion transmembrane transporter activity | molecular function |
| **GO:0051932** | synaptic transmission, GABAergic | inhibitory arm |
| **GO:0007214** | gamma-aminobutyric acid signaling pathway | GABA-A/GABA-B signaling |
| **GO:0042391** | regulation of membrane potential | hyperpolarization/de-inactivation node |
| **GO:0019228** | neuronal action potential | burst firing |
| **GO:1904659** | D-glucose transmembrane transport | SLC2A1/GLUT1 branch |
| **GO:0021794** | thalamus development | developmental context (use sparingly) |

---

## 7. Anatomical Structures Affected

### Organ / system level

- **Body system:** nervous system, exclusively
- **Primary organ:** brain
- **Secondary organ involvement:** none intrinsic. Secondary harms are injury-related (falls, trauma during GTCS) and treatment-related (liver, bone marrow, teratogenesis)

### Structures

| Structure | UBERON | Status | Role |
|---|---|---|---|
| Thalamus | **UBERON:0001897** `dorsal plus ventral thalamus` | ✓OAK | Oscillator hub |
| Thalamic reticular nucleus | ⚠ **needs lookup** — UBERON search did not resolve cleanly in this pass; do NOT guess an ID | ⚠ | GABAergic pacemaker element; expresses Cav3.2/Cav3.3 |
| Cerebral cortex | **UBERON:0000956** | ✓OAK | Initiation/driving |
| Neocortex | **UBERON:0001950** | ✓OAK | |
| Somatosensory cortex | **UBERON:0008930** | ✓OAK | Rodent cortical focus (peri-oral region) — **model-organism finding, flag as such** |
| Frontal cortex / midcingulate | ⚠ needs lookup | ⚠ | Human imaging findings (Xiao 2026) |
| Striatum (ventral striatum, dorsal caudate, putamen subdivisions) | ⚠ needs lookup | ⚠ | Zhang 2023 dFC findings |
| Blood-brain barrier | ⚠ needs lookup | ⚠ | GLUT1 branch only |

### Cell types

| Cell type | CL | Status | Role |
|---|---|---|---|
| Glutamatergic neuron | **CL:0000679** | ✓OAK | Cortical drive; thalamocortical relay |
| GABAergic neuron | **CL:0000617** | ✓OAK | nRT inhibitory pacemaker |
| Pyramidal neuron | **CL:0000598** | ✓OAK | Cortical layer V/VI initiation |
| Cortical interneuron | **CL:0008031** | ✓OAK | Feed-forward inhibition |
| Thalamocortical relay neuron | ⚠ needs lookup (CL may lack a precise term) | ⚠ | Cav3.1-expressing burst generator |
| Microglial cell | **CL:0000129** | ✓OAK | ⚠ **Do not use** unless you have real evidence — there is no established microglial mechanism in JAE. Listed only so a curator doesn't reach for it reflexively. |

### Subcellular

- **Plasma membrane / voltage-gated calcium channel complex** — the T-type channels
- **Presynaptic and postsynaptic membranes** — GABAergic synapse
- **Endoplasmic reticulum** — relevant only via the GAERS calnexin-trafficking mechanism (model organism)
⚠ GO cellular-component IDs not verified in this pass.

### Lateralization

**Bilateral and synchronous** — this is definitional. The discharge is generalized from onset, bilaterally synchronous, and symmetric. **Consistently lateralized or focal-onset discharges are an exclusionary/alert feature**, though transient asymmetry and non-consistent focal spikes are permitted.

---

## 8. Temporal Development

### Onset

- **Age range:** 8–20 years; **peak 9–13 years** (ILAE syndrome portal)
- **Mean:** 12.3 ± 2.8 y (StatPearls) and 11.86 ± 3.87 y (PMID:40945312)
- **Pattern:** **insidious**. Absences are infrequent and subtle in JAE, so the diagnostic trigger is frequently the **first GTCS** rather than the absences — which are then discovered retrospectively. This is a clinically important asymmetry vs. CAE, where daily absences get noticed at school.
- **HPO onset:** `Juvenile onset` ⚠ verify HP ID before use

### The 8–11 year "watershed"

There's a genuine nosological grey zone where CAE, JAE, and JME overlap. The best study of it:

> **[VERBATIM]** "Introduction: Absence seizures occur in various epilepsy syndromes, including childhood and juvenile absence epilepsy and juvenile myoclonic epilepsy. When children present with absence seizures at ages when syndromes overlap, initial syndrome designation is not always possible, making early prognostication challenging. For these children, the study objective is to determine clinical and initial electroencephalograph (EEG) findings to predict the development of generalized tonic-clonic seizures, which is a factor that affects outcome. Methods: Children with new-onset absence seizures between 8 and 11 years of age with at least 5 years of follow-up data were studied through the review of medical records and initial EEG tracings. Results: Ninety-eight patients were included in the study. The median age of absence seizure onset was 9 years (interquartile range [IQR] = 8.00, 10.00) and follow-up was 15 years (IQR = 13.00, 18.00). Forty-six percent developed generalized tonic-clonic seizures and 20% developed myoclonic seizures. On multiple regression analysis, a history of myoclonic seizures, anxiety, as well as bifrontal slowing and mild background slowing on initial EEG (P < .05) were associated with generalized tonic-clonic seizures. Although not statistically significant, a shorter duration of shortest EEG burst on baseline EEG was also associated with generalized tonic-clonic seizures. Conclusion: On initial EEG, bifrontal and background slowing and myoclonic seizures and anxiety are associated with developing generalized tonic-clonic seizures, which is of prognostic significance when early syndrome designation is difficult."
> — Datta AN, Crawford J, Wallbank L, Wong PKH. *J Child Neurol* 2023;38(8–9). **PMID:37461321**

Note the striking finding: **anxiety** — a psychiatric comorbidity — predicts GTCS development. Not a direction most people would guess.

### Course and progression

- **Course pattern:** episodic/recurrent seizures on a **stable, non-degenerative** substrate. JAE does **not** progress neurologically; there is no atrophy-driven decline. (⚠ Caveat: PMID:41604608, "Progressive Changes in Brain Morphology in People With Idiopathic Generalized Epilepsy," *Neurology* 2026, reports longitudinal morphometric change in IGE — worth curating as an emerging, non-clinical finding, not as clinical progression.)
- **Duration:** **chronic, frequently lifelong.** This is the sharpest contrast with CAE, which usually remits in adolescence. JAE typically does not outgrow itself.
- **Evolution to JME:** approximately **18%** of JAE progresses to JME (StatPearls) ⚠ paraphrase — trace to primary source.
- **Seizure-type evolution:** absences first, GTCS added later in most patients.

### Critical windows

- **Puberty** — the syndrome's onset window; hormonal and maturational timing is unexplained (**gap**)
- **Adolescence/early adulthood** — highest risk period for sleep-deprivation-triggered GTCS, driving, and alcohol exposure
- **Female reproductive years** — the window where valproate choice becomes irreversible in consequence (§12)
- **Post-seizure-freedom withdrawal window** — see §11

---

## 9. Inheritance and Population

### Epidemiology

| Measure | Value | Source |
|---|---|---|
| Prevalence | **~0.1 per 1,000** = **10 per 100,000** | StatPearls ⚠ paraphrase |
| Share of childhood epilepsies | **1–2%** | StatPearls ⚠ |
| Share of idiopathic generalized epilepsy | **~15–20%** | StatPearls ⚠ |
| Sex ratio | **Approximately 1:1** (male:female) — ILAE portal states it affects both sexes equally | ILAE syndrome portal |
| Absence-seizure incidence (all syndromes, context) | 0.7–4.6 / 100,000 / yr general population; 6–8 / 100,000 in ages 0–15 | secondary ⚠ |
| Absence-seizure prevalence (context) | 5–50 / 100,000 general population | secondary ⚠ |

**Prevalence class for dismech `Prevalence`:** `BAND_1_5_PER_10000` with `rate_per_100000: 10.0`, `measure_type: POINT_PREVALENCE`, `population: Worldwide`. ⚠ The underlying 0.1/1,000 figure is secondary-source; ideally re-anchor on Orphanet epidemiology or a primary population study before curating.

### Inheritance

- **Pattern:** **multifactorial / polygenic** — this is the correct top-level `inheritance_term`. HPO `Multifactorial inheritance` / `Polygenic inheritance` (**HP:0010982**) ⚠ verify IDs.
- **Autosomal dominant with incomplete penetrance** applies **only** to the *SLC2A1* familial subgroup — model this as a subtype-level inheritance block, not disease-level. Mullen 2010: 15 carriers, 12 affected → **penetrance ~80%** in those kindreds.
- **Expressivity:** highly variable — the same *SLC2A1* variant produced IGE-with-absence, myoclonic-astatic epilepsy, and focal epilepsy within the same families, with absence onset spanning **3 to 34 years**.
- **Anticipation:** none reported. **Not applicable** (no repeat expansion).
- **Germline mosaicism:** not reported for JAE.
- **Founder effects:** none established for JAE. (*EFHC1* JME variants were described in Mexican families — that's ascertainment, not a demonstrated founder effect.)
- **Consanguinity:** StatPearls reports 40.3% parental consanguinity ⚠ — this is inconsistent with a polygenic dominant-ish model and almost certainly reflects a single regional cohort. **Do not curate this without tracing it.**
- **Carrier frequency:** not applicable for a polygenic syndrome. For *SLC2A1*, Danish population frequency estimated **~1:83,000** (PMID:26537434).

### Population demographics

- **Ethnic/geographic variation:** none established. The GWAS was multi-ancestry but did not report JAE-specific ancestry effects.
- **Age distribution:** onset concentrated 9–13 y; prevalent population skews adolescent-to-adult given the chronic course.
- **Sex:** ~equal. ⚠ Some series report slight female predominance in IGE overall; the ILAE portal states equal for JAE, so use equal.

---

## 10. Diagnostics

### Diagnosis is clinical + electroencephalographic. There is no biomarker.

### ILAE 2022 diagnostic criteria (Hirsch 2022, PMID:35503716)

**Mandatory:**
- Absence seizures (the defining seizure type)
- **3–5.5 Hz generalized spike-wave** on EEG. An **ictal** EEG is not required provided the interictal study shows paroxysms of 3–5.5 Hz GSW **during wakefulness**
- Normal EEG background
- Age at onset within the juvenile window (8–20 y, peak 9–13 y)

**Exclusionary:**
- **Myoclonic seizures** — except for subtle myoclonus occurring *during* an absence (prominent myoclonus → JME)
- Slow spike-wave **<2.5 Hz**
- Generalized EEG background slowing
- Abnormal neurological exam / developmental regression / abnormal structural imaging
- Consistently localizing focal discharges

**Alerts** (do not exclude, but should trigger a rethink and further investigation): the ILAE framework notes that "the more alerts that are present, the less confident one can be about diagnosis of a specific syndrome."
⚠ The full mandatory/exclusionary/alert tables live in the paywalled Table for JAE in PMID:35503716 — **fetch the actual table before curating a `definitions` block.**

### Electrophysiology (the diagnostic centerpiece)

- **Routine EEG with 3 minutes of hyperventilation** — the single highest-yield test. Failure to provoke GSW after adequate hyperventilation makes ongoing absence seizures unlikely.
- **Intermittent photic stimulation** — photoparoxysmal response in a minority (~7.5–10%)
- **Sleep-deprived EEG / prolonged video-EEG** — for cases with normal routine EEG, and to characterize seizure frequency. Note PMID:38550342 used 2-hour video EEG with ≥5 seizures as an inclusion threshold.
- **24-hour ambulatory EEG** — used as the endpoint measure in the brivaracetam trial (§12)
- **Emerging:** wearable-device seizure counting (PMID:40116734, *Epilepsia* 2025, "Tailoring antiseizure treatment with a wearable device: A proof-of-concept study in absence epilepsy"); ultra-long-term subcutaneous EEG in drug-refractory IGE (PMID:41066224, *Epilepsia* 2026)

**LOINC:** EEG study ⚠ specific LOINC codes not retrieved; look up rather than guess.

### Imaging

**Normal by definition.** MRI is typically negative; non-specific findings occasionally seen. An abnormal MRI showing a structural lesion **excludes** the syndrome. Research-grade quantitative MRI shows group-level differences (§6.4) but has **no diagnostic role**.

### Laboratory tests

- **No diagnostic blood/urine test exists.**
- **Lumbar puncture with paired CSF/plasma glucose** — the one high-value lab test, and only when GLUT1 deficiency is suspected (early-onset absence, absence + paroxysmal exertional dyskinesia, absence + family history of movement disorder, drug-resistant absence). Low CSF glucose and low CSF:plasma glucose ratio.
- Routine chemistry/CBC/LFTs are **treatment-monitoring** tests (valproate), not diagnostic.

### Genetic testing

| Test | Utility in JAE |
|---|---|
| **Targeted *SLC2A1* testing** | **The highest-yield genetic test**, and the only one that reliably changes management. Arsov 2012 conclusion: SLC2A1 analysis "should be strongly considered" in early-onset absence epilepsy. Extend the indication to drug-resistant absence and absence + PED at any age. |
| **Epilepsy gene panel** | Reasonable in atypical, drug-resistant, or familial cases. Genes of interest: *SLC2A1, CACNA1H, CACNA1A, CACNA1G, CACNB4, GABRG2, GABRA1, GABRB3, GRIK1, EFHC1* (interpret with the caveats in §4) |
| **WES / WGS** | Not routine. Consider for drug-resistant or syndromic presentations. |
| **Chromosomal microarray** | **Low yield in typical JAE**; a pathogenic CNV should prompt diagnostic reconsideration. Some value in GGE cohorts for 15q13.3 / 16p13.11 / 15q11.2 recurrent CNVs. |
| **Karyotype / FISH / mtDNA / repeat expansion** | **Not indicated.** No role in JAE. |
| **Polygenic risk scores** | Research only. The 2023 GWAS makes GGE PRS technically feasible but it is **not clinically actionable** for JAE. |

### Omics-based diagnostics

**None validated.** RNA-seq, proteomics, metabolomics, epigenomics, liquid biopsy: all **not applicable** to JAE diagnosis. Flag as gap rather than inventing utility.

### Differential diagnosis — the ones that actually matter

| Differential | Distinguishing features |
|---|---|
| **Childhood absence epilepsy (CAE)** | Younger onset (6–7 y); **pyknoleptic** (tens-to-hundreds of absences/day); shorter absences with more complete impairment; regular 3 Hz GSW; GTCS uncommon; high spontaneous remission |
| **Juvenile myoclonic epilepsy (JME)** | **Prominent myoclonic jerks on awakening** (exclusionary for JAE); polyspike-wave; higher photosensitivity |
| **Epilepsy with GTCS alone (GTCA)** | No absences |
| **Eyelid myoclonia with absences (Jeavons)** | Marked eyelid myoclonia, eye-closure sensitivity, high photosensitivity |
| **Myoclonic absence epilepsy** | Rhythmic myoclonus with tonic abduction during the absence |
| **GLUT1 deficiency syndrome** | Very early or very late onset, paroxysmal exertional dyskinesia, low CSF glucose, drug resistance, ketogenic-diet responsiveness |
| **Focal impaired-awareness (temporal/frontal) seizures** | Aura, longer duration, post-ictal confusion, focal EEG, structural MRI abnormality |
| **Absence-to-bilateral-tonic-clonic with focal features** | See PMID:40347446 (*Epileptic Disord* 2025) — a genuine diagnostic trap |
| **Non-epileptic staring / daydreaming / inattentive ADHD** | Interruptible; no EEG correlate; hyperventilation-negative |
| **Lennox-Gastaut** | <2.5 Hz slow spike-wave, abnormal background, intellectual disability, tonic seizures |

The StatPearls differential list (benign centrotemporal epilepsy, benign neonatal convulsions, benign occipital paroxysms) is unhelpfully off-target for JAE — I'd not carry it into a dismech entry.

### Screening

- **No population screening exists or is indicated.** JAE is polygenic, not amenable to newborn or carrier screening.
- **Cascade testing** is appropriate only in *SLC2A1*-positive families — where it is genuinely valuable, because unrecognized carriers may have subtle PED or absences and would benefit from a ketogenic diet.

---

## 11. Outcome / Prognosis

### Survival and mortality

- **Life expectancy:** near-normal. JAE is not a life-shortening disease per se.
- **SUDEP:** the principal disease-attributable mortality risk, driven by **GTCS burden**. Since 79–95% of JAE patients have GTCS, this is not a trivial concern. ⚠ No JAE-specific SUDEP incidence figure found — **gap**.
- **Disease-specific mortality:** not quantified for JAE. Additional mortality routes: seizure-related trauma, drowning, status epilepticus.

### Seizure outcome — the core prognostic data

**Landmark long-term cohort:**
Trinka E, Baumgartner S, Unterberger I, Unterrainer J, Luef G, Haberlandt E, Bauer G. "Long-term prognosis for childhood and juvenile absence epilepsy." *J Neurol* 2004;251(10). **PMID:15503104**, DOI 10.1007/s00415-004-0521-1.
- 163 patients, hospital-based, treated 1970–1997, follow-up 1999–2000, **mean follow-up ~25.8 years**
- Seizure-free ≥2 years: **CAE 56%, JAE 62%**, overlap group 54%; overall remission **58%**
- **Key conclusion:** the absence *pattern* (pyknoleptic vs. non-pyknoleptic) together with later development of additional seizure types predicted long-term outcome **better than the CAE/JAE syndrome label itself** — a genuinely important nosological finding
- Widely cited derived figures: **seizure freedom 78%** in those with absences only vs. **35%** in those with GTCS ⚠ **[PARAPHRASE — DO NOT QUOTE]**

**Contemporary 10-year cohort:**
Wang X, Zhang X, Wei J, et al. "Long-term seizure outcomes and the likelihood of antiseizure medication withdrawal in patients with juvenile absence epilepsy: A 10-year follow-up study." *Seizure* 2025. **PMID:40945312**.
- 58 JAE patients, mean onset **11.86 ± 3.87 y**, median follow-up **9.57 y**
- **38 (65.5%) achieved seizure freedom for ≥2 years**
- **ASM withdrawal attempted in 48.3%**; **64.3%** of those had no recurrence during tapering; ASMs discontinued in **9 patients** at last follow-up
- **Favorable predictor:** valproate treatment (independent predictor of seizure freedom)
- **Unfavorable predictors:** total number of GTCS experienced; absence seizures on follow-up EEG; persistence of hyperventilation positivity on EEG
- GSWD patterns improved on follow-up EEG in the majority
⚠ **[PARAPHRASE — DO NOT QUOTE]** — abstract came through a summarizer.

**Reported range across the literature:** remission rates from **21% to 89%** (StatPearls) — the spread reflects wildly different definitions of "remission," cohort ascertainment (tertiary referral vs. population), and follow-up duration. A dismech entry should present the range and name the reason for the spread rather than pick a single number.

### Withdrawal and relapse

- Older data (StatPearls, ⚠): "**All** patients with JAE relapsed after AED withdrawal, and 25% of patients continuing on AEDs relapsed" in one study — versus another prospective study where only 3 of 9 seizure-free patients relapsed.
- Newer data (PMID:40945312) is considerably more optimistic: ~2/3 of withdrawal attempts succeeded without recurrence.
- **Practical upshot:** JAE is traditionally taught as lifelong-treatment, but the 2025 data suggest withdrawal is viable in a well-selected subgroup. Worth curating as a **shifting evidence base**, not settled fact.
- Related: PMID:39654414 (*J Child Neurol* 2025) on the need for repeat EEG after ASM withdrawal in pediatric IGE.

### Prognostic factors

| Factor | Direction |
|---|---|
| **GTCS present / high GTCS count** | Worse |
| **Myoclonic seizures** | Worse (and prompts JME reclassification) |
| **Anxiety at presentation** | Predicts GTCS development (PMID:37461321) |
| **Bifrontal slowing / mild background slowing on initial EEG** | Predicts GTCS development (PMID:37461321) |
| **Persistent absences or hyperventilation positivity on follow-up EEG** | Worse |
| **Valproate treatment** | Better (PMID:40945312) — but see the teratogenicity trade-off |
| **Non-pyknoleptic absence pattern** | Prognostically informative independent of syndrome label (PMID:15503104) |

**Prognostic biomarkers:** none molecular. All prognostic markers are clinical/EEG. Genuine gap.

### Morbidity, disability, function

- **Educational:** ~2× hazard for special-needs education; lower GPA; 15% fewer attending high school (PMID:35595971)
- **Psychiatric:** anxiety, depression, ADHD, sleep disorder; psychiatric comorbidity ~43% ⚠
- **Cognitive:** deficits in attention, executive function, language — present **even without breakthrough seizures** ⚠
- **Social:** driving restriction, employment limitation, medication burden, pregnancy-planning constraints
- **QoL instruments:** no JAE-specific EQ-5D/SF-36/PROMIS data — **gap**

---

## 12. Treatment

### 12.1 First-line pharmacotherapy — and the central dilemma

JAE treatment has a structural problem: **the most effective drug is the one you cannot safely give to half the patient population.** Most JAE patients are adolescent, and roughly half of them are female and entering reproductive years exactly as treatment begins. Valproate works best and is teratogenic. That tension shapes the entire algorithm.

| Drug | Role | Notes |
|---|---|---|
| **Valproate / valproic acid** | First-line for absences **and** GTCS; independent predictor of seizure freedom | Contraindicated in females of childbearing potential except under a Pregnancy Prevention Programme; contraindicated with *POLG* variants |
| **Lamotrigine** | First-line alternative, **preferred in young females** | Best JAE-specific evidence in women (below) |
| **Levetiracetam** | Widely used first-line, especially in women | Inferior to valproate in SANAD II; inferior to lamotrigine in JAE women (below) |
| **Ethosuximide** | Effective for **absences only** — does **not** protect against GTCS | Since 79–95% of JAE patients get GTCS, ethosuximide monotherapy is usually inadequate in JAE (unlike CAE, where it's optimal first-line) |
| **Topiramate, zonisamide, perampanel, clobazam, brivaracetam** | Second-line / adjunctive | See trial data below |

**Key trial evidence:**

- **SANAD II (generalised/unclassifiable arm)** — Marson A, et al. *Lancet* 2021;397:1375–1386. In per-protocol analysis, **valproate was superior to levetiracetam** for both time to 12-month remission and time to treatment failure; the trial "did not support the use of levetiracetam as a first-line treatment for newly diagnosed generalised epilepsy at 12 months." ⚠ verify PMID (likely 33838757) and re-quote.
- **Glauser CAE trial** — ethosuximide and valproate superior to lamotrigine for treatment failure in a 14-week double-blind RCT; ethosuximide the optimal initial monotherapy for **childhood** absence epilepsy given efficacy + attentional tolerability. ⚠ **This is CAE, not JAE** — do not import the conclusion wholesale, because the GTCS burden in JAE changes the calculus entirely. (Cochrane update: PMID:28195639.)
- **JAE-specific, women of childbearing age — the most directly applicable modern evidence:**
  Cerulli Irelli E, Cocchi E, Gesche J, Peña-Ceballos J, Caraballo RH, Lattanzi S, et al. "Lamotrigine vs levetiracetam in female patients of childbearing age with juvenile absence epilepsy: A Bayesian reanalysis." *Epilepsia* 2024. **PMID:39126356**. Multicenter; **123 women with JAE**, lamotrigine (n=67) vs. levetiracetam (n=56) as initial monotherapy. LTG showed lower treatment failure and higher ASM retention, with a **99.2% posterior probability of LTG superiority** for treatment failure; comparable safety profiles. Conclusion supports considering LTG as first-line monotherapy for JAE in women of childbearing age. ⚠ **[PARAPHRASE — DO NOT QUOTE]** — re-fetch for exact wording.

### 12.2 Drugs that AGGRAVATE absence seizures — curate this as mechanism, not just a warning

**Contraindicated / seizure-aggravating in JAE:** carbamazepine, oxcarbazepine, phenytoin, gabapentin, pregabalin, vigabatrin (and tiagabine).

This is not idiosyncratic toxicity — it's the thalamocortical mechanism running in reverse. Sodium-channel blockers and drugs that raise thalamic GABA tone (vigabatrin/tiagabine raise extracellular GABA → more GABA-B-mediated hyperpolarization → more T-type de-inactivation → more burst firing). Giving vigabatrin for absences is like fixing a squeaky hinge by oiling the wrong side of the door.

### 12.3 Mechanism-directed therapy

- **Ethosuximide** — T-type calcium channel blocker. The one classical ASM whose mechanism maps directly onto §6. Good candidate for a `target_mechanisms` link to the T-type/burst-firing node.
- **Valproate** — broad-spectrum; T-type modulation + GABAergic + sodium-channel effects
- **Ketogenic diet** — mechanism-directed **only** in GLUT1 deficiency, where ketone bodies bypass the defective transporter. This is the closest thing JAE has to precision medicine, and it's a strong `target_mechanisms` candidate against the SLC2A1/glucose-transport node.
- **Experimental T-type blockers** — Tringham et al., *Sci Transl Med* 2012, **PMID:22344687**; the CX-8998 program (NCT03406702, absence seizures) represents the translational arm of this mechanism.

### 12.4 Newer agents and trials

- **Brivaracetam monotherapy in CAE/JAE** — Bast T, et al. "Efficacy and tolerability of brivaracetam monotherapy in childhood and juvenile absence epilepsy: An innovative adaptive trial design." *Epilepsia Open* 2022. **PMID:35844134**, DOI 10.1002/epi4.12628. Trial **N01269 / NCT04666610**, phase 2/3, ages 2–25 with CAE or JAE. Adaptive design: dose-selection/futility stage → interim analysis → optimal-dose stage; each with ≤2-week screening, 2-week placebo-controlled period, 11-week active treatment (10 weeks + 24-h EEG + 1 additional week for 24-h EEG assessment); absence-seizure-free patients enter a ≤4-week randomized withdrawal period. Started July 2021.
- **Long-term brivaracetam safety extension:** **NCT06315322**
- Case-level brivaracetam response in drug-resistant JAE: PMID:40853097 (*An Sist Sanit Navar* 2025)
- **Cenobamate** — reported in JME (PMID:40042429); JAE evidence not established

### 12.5 Pharmacogenomics

- ***POLG* and valproate** — the strongest actionable PGx signal. Valproate is **contraindicated** in patients with known *POLG*-related mitochondrial disorders and in children <2 y clinically suspected of mitochondrial disease. Seven *POLG1* variants (L304R, A467T, G588D, Q879H, T885S, E1143G, Q1236H) have been associated with valproate-induced liver toxicity. Reported: fatal outcomes in **53/102 (52%)** of POLG valproate-exposed patients, all harboring recessive mutations. Mechanism: mitochondrial toxicity via inhibition of beta-oxidation. See NCBI Medical Genetics Summaries NBK620296 and PMID:20138553 ("POLG DNA testing as an emerging standard of care before instituting valproic acid therapy for pediatric seizure disorders"). ⚠ figures paraphrased.
- ***HLA-B\*15:02* and lamotrigine/carbamazepine** — SJS/TEN risk in Southeast Asian ancestry. ⚠ Relevant to lamotrigine dosing decisions; verify current CPIC guidance before curating.
- **No JAE-specific efficacy pharmacogenomics exists.**

### 12.6 Non-pharmacological

- **Ketogenic / modified Atkins diet** — first-line in GLUT1DS; second-line in drug-resistant absence
- **Sleep hygiene and trigger avoidance** — behavioral, meaningful
- **Surgery** — **contraindicated / not applicable.** JAE is generalized with no resectable focus. Neuromodulation (VNS/DBS) is not established for JAE.
- **Genetic counseling** — indicated in *SLC2A1*-positive families and for reproductive planning on valproate

### 12.7 Adverse events worth curating

| Drug | Key AEs |
|---|---|
| Valproate | Teratogenicity (**~10% major congenital malformations**; **~30–40% neurodevelopmental disorders**, dose-dependent — neural tube defects, hypospadias, cardiac defects, orofacial clefts; reduced IQ, autism, ADHD); weight gain; hepatotoxicity (POLG); pancreatitis; hyperammonemia; PCOS; tremor; alopecia |
| Lamotrigine | Rash/SJS-TEN (dose-titration dependent); insomnia; **oral-contraceptive and pregnancy-related clearance changes requiring level monitoring** |
| Levetiracetam | Behavioral/psychiatric adverse effects (irritability, aggression, depression) — non-trivial in an adolescent population already carrying psychiatric comorbidity |
| Ethosuximide | GI upset, hiccups, blood dyscrasias, headache; attentional effects milder than valproate |
| Topiramate | Cognitive slowing, word-finding difficulty, weight loss, nephrolithiasis, teratogenicity |

**Valproate Pregnancy Prevention Programme:** valproate must not be used in females of childbearing potential unless PPP conditions are met — educational program, evaluation/control of therapy, and distribution control. A 2026 joint position statement (Society for Birth Defects Research and Prevention / OTIS / Developmental Neurotoxicology Society) calls for REMS-level risk evaluation and mitigation strategies. ⚠ paraphrased.

### 12.8 Suggested NCIT treatment terms

Following the dismech `treatment_term` + `therapeutic_agent` pattern:

| Treatment | `treatment_term` (NCIT) | `therapeutic_agent` | `therapeutic_modality` |
|---|---|---|---|
| Valproate | NCIT:C15986 Pharmacotherapy | **CHEBI:39867** `valproic acid` ✓OAK | SMALL_MOLECULE |
| Ethosuximide | NCIT:C15986 | **CHEBI:4887** `ethosuximide` ✓OAK | SMALL_MOLECULE |
| Lamotrigine | NCIT:C15986 | **CHEBI:6367** `lamotrigine` ✓OAK | SMALL_MOLECULE |
| Levetiracetam | NCIT:C15986 | **CHEBI:6437** `levetiracetam` ✓OAK | SMALL_MOLECULE |
| Brivaracetam | NCIT:C15986 | **CHEBI:133013** `brivaracetam` ✓OAK | SMALL_MOLECULE |
| Topiramate | NCIT:C15986 | **CHEBI:63631** `topiramate` ✓OAK | SMALL_MOLECULE |
| Zonisamide | NCIT:C15986 | **CHEBI:10127** `zonisamide` ✓OAK | SMALL_MOLECULE |
| Perampanel | NCIT:C15986 | **CHEBI:71013** `perampanel` ✓OAK | SMALL_MOLECULE |
| Clobazam | NCIT:C15986 | **CHEBI:31413** `clobazam` ✓OAK | SMALL_MOLECULE |
| Ketogenic diet | NCIT:C15447 Dietary Intervention ⚠verify | — | BEHAVIORAL |
| Genetic counseling | NCIT:C15240 Genetic Counseling ⚠verify | — | OTHER |

Aggravating drug (for a REFUTE/contraindication evidence item): **CHEBI:3387** `carbamazepine` ✓OAK.

> ⚠ Per the project memory note on `therapeutic_agent`: NCIT drug terms often fail `therapeutic_agent` validation — **prefer CHEBI**, which is what I've verified above.

### 12.9 Treatment algorithm sketch

1. Confirm syndrome (EEG with hyperventilation; exclude JME by ruling out prominent myoclonus)
2. Consider *SLC2A1* testing if early-onset, drug-resistant, PED present, or suggestive family history → if positive, **ketogenic diet**
3. Choose first agent by **sex and reproductive plans**:
   - Male, or female with no childbearing potential → **valproate**
   - Female of childbearing potential → **lamotrigine** first (PMID:39126356), levetiracetam as alternative
4. Do **not** use ethosuximide alone if GTCS have occurred or are likely
5. **Never** use carbamazepine/oxcarbazepine/phenytoin/gabapentin/pregabalin/vigabatrin
6. Address sleep, alcohol, adherence, and psychiatric comorbidity as first-class targets, not afterthoughts
7. Consider withdrawal only after prolonged seizure freedom with a normalized EEG — and counsel on relapse risk and driving

---

## 13. Prevention

### Primary prevention

**Not possible.** JAE is polygenic and constitutional; there is no modifiable exposure to remove. Any "primary prevention" claim in a KB entry would be wrong.

### Secondary prevention (early detection)

- No population screening. Diagnostic vigilance in an adolescent with unexplained staring, declining school performance, or a first GTCS.
- **EEG with hyperventilation** early in evaluation is the practical "screening" step.
- Rapid syndrome assignment matters because the wrong drug (carbamazepine) actively worsens the disease.

### Tertiary prevention (preventing complications — where the real action is)

| Target | Intervention |
|---|---|
| GTCS / SUDEP | Optimize ASM adherence; treat GTCS aggressively; nocturnal supervision counseling in high-risk patients |
| Absence status epilepticus | Recognize prodrome; avoid aggravating drugs; benzodiazepine rescue plans |
| Injury/drowning | Swimming supervision, bathing precautions, driving restrictions per jurisdiction (PMID:38500008) |
| Teratogenic harm | Valproate PPP; preconception counseling; **high-dose folic acid** preconception; switch to lamotrigine/levetiracetam before conception, not after |
| Hepatotoxicity | *POLG* testing before valproate in suspicious presentations |
| Educational/psychiatric harm | Proactive neuropsychological assessment and school support — justified by PMID:35595971 |
| Trigger-driven breakthrough | Sleep hygiene, alcohol moderation, stress management |

### Immunization

**Not applicable** as prevention of JAE. General vaccination is appropriate; there is no vaccine-JAE relationship in either direction.

### Genetic screening and counseling

- **Carrier screening / PGD / prenatal testing:** **not applicable** for polygenic JAE
- **Applicable only in *SLC2A1*-positive families**, where AD inheritance with incomplete penetrance makes cascade testing, counseling, and (rarely) reproductive options meaningful
- Empiric recurrence risk counseling for JAE relatives: modestly elevated over population baseline, with a **syndrome-shifting** caveat (relatives may have JME or GTCA rather than JAE)

### Public health / environmental interventions

**Not applicable.**

---

## 14. Other Species / Natural Disease

### Naturally occurring absence-like epilepsy

- **Rat (NCBITaxon:10116):** the two flagship strains — **GAERS** (Genetic Absence Epilepsy Rats from Strasbourg) and **WAG/Rij** — arose as *spontaneous* inbred-colony phenotypes, not engineered models. They are arguably the closest thing to "natural disease" in another species, though they exist only in laboratory colonies.
- **Mouse (NCBITaxon:10090):** *tottering*, *lethargic*, *stargazer*, *ducky* are all **spontaneous** mutants discovered in mouse colonies — again, natural mutations, laboratory context.
- **Dog (NCBITaxon:9615):** idiopathic epilepsy is the commonest cause of canine seizures, affecting up to ~1% of dogs. A study in **Cavalier King Charles Spaniels** reported absence seizures with ictal discharges "characterised by generalized onset, 3 to 4 Hz, spike-and-wave complexes" ⚠ — remarkably close to the human phenotype. This is the best candidate for genuine naturally-occurring absence epilepsy in a companion animal. **VBO term for Cavalier King Charles Spaniel: ⚠ needs lookup.**
- **Cat (NCBITaxon:9685):** idiopathic epilepsy affects up to ~2%; absence-specific phenotypes not well characterized.
- **OMIA:** ⚠ no JAE-specific OMIA entry retrieved in this pass. Worth a direct OMIA query before curating.

### Orthologous genes

| Human | Mouse ortholog | Relevance |
|---|---|---|
| *CACNA1H* | *Cacna1h* | GAERS R1584P (rat) |
| *CACNA1A* | *Cacna1a* | *tottering*, *leaner* |
| *CACNB4* | *Cacnb4* | *lethargic* |
| *CACNG2* | *Cacng2* | *stargazer* |
| *CACNA2D2* | *Cacna2d2* | *ducky* |
| *SLC2A1* | *Slc2a1* | GLUT1 models |

⚠ NCBI Gene IDs not retrieved; look up rather than guess.

### Comparative pathology and conservation

The thalamocortical oscillator is **deeply conserved** across mammals — which is why rodent SWDs look so much like human spike-wave and why ethosuximide suppresses them in both. Key species difference: **human absence SWD runs at ~3 Hz; mouse SWD is usually 5–7 Hz.** Rat GAERS/WAG-Rij SWDs run ~7–11 Hz. That frequency offset is a real translational caveat and belongs in a `HUMAN_MODEL_MISMATCH` discussion.

### Zoonotic potential / transmission

**Not applicable.** JAE is genetic and non-transmissible.

---

## 15. Model Organisms

### 15.1 Rat models

**GAERS (Genetic Absence Epilepsy Rats from Strasbourg)** — the single best-characterized model.

- **Causal variant:** homozygous **gain-of-function R1584P** substitution in *Cacna1h* (Cav3.2 T-type Ca²⁺ channel), in exon 24 encoding the proximal III–IV linker (arginine → proline)
- **Mechanism:** the mutation alters the **Cav3.2/calnexin interaction**, increasing channel surface expression and Ca²⁺ influx — a trafficking mechanism, not a pure gating mechanism. Refs: *Sci Rep* 2017 (PMC5599688); *Neurobiol Dis* 2023, PMID:37391087 (R1584P effects in GAERS and NEC congenic rats)
- **Phenotype:** spontaneous behavioral arrest and staring, clonic vibrissal twitching, high-amplitude SWDs
- **Comparator strain:** NEC (Non-Epileptic Control) — an isogenic-ish control, which is methodologically valuable
- **Genome resource:** whole-genome sequence of GAERS and NEC published (PMID:28708842, *PLoS One* 2017)
- **Colony variation caveat:** PMID:25377760 documents seizure expression, behavior, and brain morphology differences *between GAERS colonies* — a reproducibility caveat worth curating

**WAG/Rij rats** — the other flagship strain; the substrate for the **cortical focus** discovery (Meeren 2002, PMID:11850474), which localized initiation to peri-oral somatosensory cortex.

### 15.2 Mouse models — the calcium channel subunit quartet

All four spontaneous mutants converge on **voltage-dependent calcium channel subunits**, exhibit bilaterally synchronous SWDs on cortical EEG with behavioral arrest, and **respond to ethosuximide** — that last point is the pharmacological validation that makes them credible absence models rather than generic seizure mice.

| Model | Gene | Subunit | Notes |
|---|---|---|---|
| *tottering* (tg) | *Cacna1a* | Cav2.1 α1A | Also ataxia/dystonia |
| *leaner* | *Cacna1a* | Cav2.1 α1A | More severe allele |
| *lethargic* (lh) | *Cacnb4* | β4 | |
| *stargazer* (stg) | *Cacng2* | γ2 (also an AMPA-receptor TARP) | Ataxia, head-tossing; NMDA-receptor changes in thalamus (PMC5318904); asynchronous visual-cortex suppression during SWD (*Nat Commun* 2018) |
| *ducky* (du) | *Cacna2d2* | α2δ-2 | Epilepsy + ataxia; decreased Ca²⁺ current in cerebellar Purkinje cells (*J Neurosci* 2001;21:6095) |

Modifier evidence: a targeted *Cacng4* mutation **exacerbates** spike-wave seizures in *stargazer* mice (*PNAS* 2005) — a clean demonstration of digenic modification in an absence model.

**Engineered models:**
- **Cav3.1 (*Cacna1g*) knockout mice are resistant** to absence seizures — the loss-of-function complement that closes the causal loop on T-type channels
- **Cav3.1 α1G overexpression** produces "pure absence epilepsy": "Genetic Enhancement of Thalamocortical Network Activity by Elevating α1G-Mediated Low-Voltage-Activated Calcium Current Induces Pure Absence Epilepsy," *J Neurosci* 2009;29:1615. This bidirectional evidence (KO protects, overexpression causes) is the strongest mechanistic support in the entire field.
- ***Slc2a1*/GLUT1 haploinsufficient mice** — model GLUT1DS including seizures and ketogenic-diet responsiveness

### 15.3 Model characteristics and limitations

**What models recapitulate well:**
- Spontaneous, bilaterally synchronous spike-wave discharges with behavioral arrest
- Ethosuximide responsiveness and carbamazepine/vigabatrin aggravation — pharmacological isomorphism
- The thalamocortical circuit mechanism and T-type dependence
- The GAERS *Cacna1h* gain-of-function mirrors human *CACNA1H* gain-of-function susceptibility variants (Heron 2007) — a genuine cross-species convergence

**What they do NOT capture (curate as `HUMAN_MODEL_MISMATCH`, not `KNOWLEDGE_GAP`):**
- **Frequency mismatch:** human 3 Hz vs. mouse 5–7 Hz vs. rat ~7–11 Hz
- **Age-of-onset structure:** rodent models don't reproduce the peripubertal onset window that *defines* JAE, nor the CAE→JAE age separation
- **Syndrome specificity:** rodent models model *absence seizures*, not *juvenile absence epilepsy*. No model reproduces the JAE-specific combination of infrequent absences **plus** a 79–95% GTCS rate. This is the single biggest translational gap.
- **Genetic architecture:** the models are single-gene, high-penetrance; human JAE is polygenic
- **Cortical focus:** anatomically stereotyped (peri-oral somatosensory) in rat; not demonstrated in human
- **Comorbidity:** rodent models don't model the academic/psychiatric burden that dominates real-world JAE morbidity
- **Colony drift:** GAERS phenotype varies between colonies (PMID:25377760)

### 15.4 Applications and resources

- **Applications:** ASM screening (ethosuximide-positive controls), T-type blocker development (PMID:22344687, CX-8998), circuit dissection with optogenetics, network-synchrony studies, trafficking/chaperone biology (calnexin/Cav3.2)
- **Databases:** MGI (mouse), RGD (rat), Alliance of Genome Resources, IMSR/JAX for strain availability, IMPC/KOMP for engineered alleles

---

## Curation Notes for the dismech Entry

A few structural suggestions, since this is heading into `kb/disorders/Juvenile_Absence_Epilepsy.yaml`:

**Module conformance — strong candidate:**
`epilepsy_excitation_inhibition_imbalance` — the existing module (ion-channel/synaptic dysfunction → excitation/inhibition imbalance → neuronal hyperexcitability and hypersynchrony → seizure generation → recurrent unprovoked seizures) fits JAE almost perfectly. Key conformance target: `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`. JAE would substitute the T-type/GABA-B thalamocortical specifics for the module's generic nodes.

**`biological_scale` tags for pathophysiology nodes:**
- Variant load / channel gating → `MOLECULAR`
- Thalamic burst firing, nRT/relay-neuron behavior → `CELLULAR`
- Cortico-thalamo-cortical loop entrainment, generalized spike-wave → `TISSUE`
- Absence seizure, absence status, GTCS → `ORGANISM`

**Discussions to include:**
- `KNOWLEDGE_GAP` — no molecular/prognostic biomarker; no epigenetic or transcriptomic data; no JAE-specific SUDEP rate; no validated QoL instrument data
- `HUMAN_MODEL_MISMATCH` — SWD frequency offset; absent peripubertal onset window in rodents; rodent cortical focus not demonstrated in humans; single-gene models vs. polygenic human disease
- `mechanistic_hypotheses` — thalamic pacemaker (CANONICAL/legacy) vs. cortical focus (now dominant in models) vs. distributed-network (EMERGING, human imaging)

**Evidence-source discipline:**
- Meeren 2002, GAERS/WAG-Rij, all mouse mutants → `MODEL_ORGANISM`
- Heron 2007 electrophysiology, calnexin trafficking → `IN_VITRO`
- Mendelian-randomization papers (PMIDs 39629734, 39165549, 41443308, etc.) → `COMPUTATIONAL`, and weight them lightly
- Hirsch 2022, Trinka 2004, Boesen 2022, Cerulli Irelli 2024, Wang 2025, Datta 2023, Arsov 2012, Mullen 2010 → `HUMAN_CLINICAL`

**Named-entity-confusion watch:** JAE sits squarely in a high-NEC-risk class — it's one of four members of a numbered/named IGE series with heavy phenotypic overlap, and "juvenile absence" vs. "juvenile myoclonic" vs. "childhood absence" are exactly the kind of near-synonym cluster that DR tools blend. If any deep-research report is used, run `just preflight-dr <report> MONDO:0800453` first. Also watch for *CLCN2* leukoencephalopathy bleeding into the JAE genetics section — different disease, same gene.

**The retraction:** please do carry the *CLCN2* retraction into the entry explicitly. A knowledge base that quietly repeats OMIM's EJA2 entry without the 2009 retraction is propagating a known-false claim, and this is one of the rare cases where dismech can be more correct than its upstream source.

---

## Sources

- [ILAE definition of the Idiopathic Generalized Epilepsy Syndromes (Hirsch 2022, Epilepsia) — PMID:35503716](https://pubmed.ncbi.nlm.nih.gov/35503716/)
- [ILAE syndrome portal — Juvenile Absence Epilepsy overview](https://www.epilepsydiagnosis.org/syndrome/jae-overview.html)
- [ILAE syndrome portal — JAE EEG](https://www.epilepsydiagnosis.org/syndrome/jae-eeg.html)
- [Juvenile Absence Epilepsy — StatPearls (NBK559055)](https://www.ncbi.nlm.nih.gov/books/NBK559055/)
- [GWAS meta-analysis of over 29,000 people with epilepsy (Nat Genet 2023) — PMID:37653029](https://pubmed.ncbi.nlm.nih.gov/37653029/)
- [Long-term prognosis for childhood and juvenile absence epilepsy (Trinka 2004) — PMID:15503104](https://pubmed.ncbi.nlm.nih.gov/15503104/)
- [Long-term seizure outcomes and ASM withdrawal in JAE: 10-year follow-up (Seizure 2025) — PMID:40945312](https://www.sciencedirect.com/science/article/abs/pii/S105913112500247X)
- [Lamotrigine vs levetiracetam in women of childbearing age with JAE (Epilepsia 2024) — PMID:39126356](https://pubmed.ncbi.nlm.nih.gov/39126356/)
- [Syndrome-specific and familial imaging traits in juvenile absence epilepsy (Epilepsia 2026) — PMID:41531116](https://pubmed.ncbi.nlm.nih.gov/41531116/)
- [School performance and psychiatric comorbidity in JAE and JME, Danish cohort (J Neurol 2022) — PMID:35595971](https://pubmed.ncbi.nlm.nih.gov/35595971/)
- [Outcome of Absence Epilepsy With Onset at 8-11 Years (J Child Neurol 2023) — PMID:37461321](https://pmc.ncbi.nlm.nih.gov/articles/PMC10493039/)
- [Exploring brain network oscillations in drug-naïve JAE (Front Neurol 2024) — PMID:38550342](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2024.1340959/full)
- [Dynamic alterations of striatal-related functional networks in JAE (Epilepsy Behav 2023) — PMID:37925871](https://pubmed.ncbi.nlm.nih.gov/37925871/)
- [Childhood absence epilepsy: genes, channels, neurons and networks (Crunelli & Leresche 2002) — PMID:11988776](https://pubmed.ncbi.nlm.nih.gov/11988776/)
- [Cortical focus drives widespread corticothalamic networks (Meeren 2002) — PMID:11850474](https://pubmed.ncbi.nlm.nih.gov/11850474/)
- [The role of T-type calcium channel genes in absence seizures — PMID:24847307](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4023043/)
- [T-type calcium channel blockers that suppress absence seizures (Sci Transl Med 2012) — PMID:22344687](https://pubmed.ncbi.nlm.nih.gov/22344687/)
- [Extended spectrum of IGEs associated with CACNA1H functional variants (Heron 2007) — PMID:17696120](https://pubmed.ncbi.nlm.nih.gov/17696120/)
- [OMIM #607631 — EJA1 (EFHC1)](https://www.omim.org/entry/607631)
- [OMIM #607628 — EIG11 / EJA2 (CLCN2)](https://omim.org/entry/607628)
- [Mutations in EFHC1 cause juvenile myoclonic epilepsy (Suzuki 2004, Nat Genet)](https://www.nature.com/articles/ng1393)
- [EFHC1 variants in JME: ACMG/NHGRI reanalysis — PMID:27467453](https://pubmed.ncbi.nlm.nih.gov/27467453/)
- [Retraction Note: Mutations in CLCN2 … (Nat Genet 2009)](https://www.nature.com/articles/ng0909-1043)
- [No evidence for a role of CLCN2 variants in idiopathic generalized epilepsy (Nat Genet 2010)](https://www.nature.com/articles/ng0110-3)
- [Absence epilepsies with widely variable onset are a key feature of familial GLUT1 deficiency (Mullen 2010) — PMID:20574033](https://www.neurology.org/doi/10.1212/WNL.0b013e3181eb58b4)
- [Early onset absence epilepsy: 1 in 10 cases is caused by GLUT1 deficiency (Arsov 2012) — PMID:23106342](https://pubmed.ncbi.nlm.nih.gov/23106342/)
- [Role of SLC2A1 mutations in MAE and absence epilepsy (Larsen 2015) — PMID:26537434](https://pubmed.ncbi.nlm.nih.gov/26537434/)
- [SANAD II: valproate versus levetiracetam for generalised and unclassifiable epilepsy (Lancet 2021)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8047813/)
- [Ethosuximide, sodium valproate or lamotrigine for absence seizures (Cochrane) — PMID:28195639](https://pubmed.ncbi.nlm.nih.gov/28195639/)
- [Brivaracetam monotherapy in CAE/JAE: adaptive trial design (Epilepsia Open 2022) — PMID:35844134](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9712476/)
- [NCT06315322 — long-term brivaracetam safety in CAE/JAE](https://clinicaltrials.gov/study/NCT06315322)
- [Valproic Acid Therapy and POLG Genotype — Medical Genetics Summaries (NBK620296)](https://www.ncbi.nlm.nih.gov/books/NBK620296/)
- [POLG DNA testing before valproic acid therapy — PMID:20138553](https://pubmed.ncbi.nlm.nih.gov/20138553/)
- [Cacna1h mutation in GAERS enhances T-type currents via calnexin-dependent trafficking (Sci Rep 2017)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5599688/)
- [Whole genome sequence data from GAERS and NEC — PMID:28708842](https://pubmed.ncbi.nlm.nih.gov/28708842/)
- [Seizure expression and morphology differences between GAERS colonies — PMID:25377760](https://pubmed.ncbi.nlm.nih.gov/25377760/)
- [Ducky mouse phenotype associated with Cacna2d2 mutations (J Neurosci 2001)](https://www.jneurosci.org/content/21/16/6095)
- [The Voltage-Gated Calcium Channel and Absence Epilepsy — Jasper's (NBK98208)](https://www.ncbi.nlm.nih.gov/books/NBK98208/)
- [Genetic enhancement of thalamocortical network activity induces pure absence epilepsy (J Neurosci 2009)](https://www.jneurosci.org/content/29/6/1615)
- [A targeted mutation in Cacng4 exacerbates spike-wave seizures in stargazer mice (PNAS 2005)](https://www.pnas.org/doi/10.1073/pnas.0409527102)
- [Clearance for Driving in Genetic Generalized Epilepsy (J Child Neurol 2024) — PMID:38500008](https://pubmed.ncbi.nlm.nih.gov/38500008/)
- [Involvement of ADGRV1 Gene in Familial Forms of Genetic Generalized Epilepsy (PMC8567843)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8567843/)