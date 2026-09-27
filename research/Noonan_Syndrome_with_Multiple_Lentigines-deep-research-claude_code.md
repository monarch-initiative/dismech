---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T02:55:47.125252'
end_time: '2026-07-31T03:00:15.029898'
duration_seconds: 267.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Noonan Syndrome with Multiple Lentigines
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 13
  num_turns: 15
  total_cost_usd: 1.5971185
  session_id: c757be3d-51af-581f-b492-1a7cf737508a
  stop_reason: end_turn
citation_count: 9
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Noonan Syndrome with Multiple Lentigines
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Noonan Syndrome with Multiple Lentigines** covering all of the
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

# Noonan Syndrome with Multiple Lentigines (NSML) — Comprehensive Research Report

## Executive Summary

Noonan syndrome with multiple lentigines (NSML), historically known as **LEOPARD syndrome**, is a rare autosomal dominant RASopathy caused predominantly by loss-of-function/dominant-negative missense variants in **PTPN11** (encoding the tyrosine phosphatase SHP2), with rarer causal variants in **RAF1**, **BRAF**, and **MAP2K1**. It is defined clinically by the acronym-derived features: multiple **L**entigines, **E**CG conduction abnormalities, **O**cular hypertelorism, **P**ulmonary valve stenosis, **A**bnormal genitalia, **R**etardation of growth, and sensorineural **D**eafness — though the name is now deprecated in favor of "Noonan syndrome with multiple lentigines" to reflect its position on the Noonan syndrome/RASopathy phenotypic continuum (GeneReviews, [NBK1383](https://www.ncbi.nlm.nih.gov/books/NBK1383/)).

---

## 1. Disease Information

**Overview:** NSML is a multisystem RASopathy presenting with progressive multiple lentigines, hypertrophic cardiomyopathy (HCM) and other cardiac defects, short stature, pectus deformity, characteristic facial dysmorphism, sensorineural hearing loss, and — in a subset — mild intellectual disability. It is mechanistically and phenotypically distinct from, yet overlapping with, classic Noonan syndrome (NS) and cardiofaciocutaneous syndrome (CFCS), together forming the RASopathy spectrum of RAS/MAPK pathway disorders.

**Key identifiers:**
- **OMIM:** Phenotypic series PS151100
  - #151100 — LEOPARD syndrome 1 (LPRD1), *PTPN11*
  - #611554 — LEOPARD syndrome 2 (LPRD2), *RAF1*
  - #613707 — LEOPARD syndrome 3 (LPRD3), *BRAF*
- **Orphanet:** ORPHA:500 ("Leopard syndrome")
- **MONDO:** MONDO:0007893
- **ICD-10-CM:** Q87.1 (Congenital malformation syndromes predominantly associated with short stature)
- **MeSH:** LEOPARD Syndrome (D007925)
- **GeneReviews:** [NBK1383](https://www.ncbi.nlm.nih.gov/books/NBK1383/)

**Synonyms:** LEOPARD syndrome; Lentiginosis profusa; Multiple lentigines syndrome; Cardiocutaneous syndrome; Capute syndrome; Noonan syndrome with multiple lentigines (current preferred term, per 2018 international RASopathy nomenclature consensus, reflecting recognition that the disorder is a subtype within the Noonan spectrum rather than a fully distinct entity).

**Evidence basis:** Information is derived from aggregated disease-level resources (OMIM, Orphanet, GeneReviews) built from case reports, case series (~150+ reported individuals, per GeneReviews), and cohort studies, rather than a large EHR-scale population. This is consistent with a genuinely rare condition without population-based prevalence data.

---

## 2. Etiology

**Disease causal factors:** NSML is caused by **heterozygous germline pathogenic missense variants** in one of four RAS/MAPK pathway genes. There is no environmental, infectious, or purely mechanistic etiology — this is a monogenic developmental signaling disorder.

**Genetic causal factors (per GeneReviews NBK1383):**

| Gene | HGNC | % of NSML | Mechanism |
|---|---|---|---|
| **PTPN11** | HGNC:9644 | >95% (85–90% in earlier series) | Predominantly catalytically-inactivating, dominant-negative variants in the SHP2 PTP (catalytic) domain |
| **RAF1** | HGNC:9829 | <3% | Gain-of-function (activating) variants, mostly at Ser259 |
| **BRAF** | HGNC:1097 | Rare (few reported cases) | Gain-of-function variants |
| **MAP2K1** | HGNC:6840 | Very rare (~1 reported individual) | Gain-of-function |

Foundational papers establishing PTPN11 as the major NSML gene: **Digilio MC, et al. "Grouping of multiple-lentigines/LEOPARD and Noonan syndromes on the PTPN11 gene." Am J Hum Genet. 2002;71(2):389-394. PMID:[12161596](https://pubmed.ncbi.nlm.nih.gov/12161596/)** — the paper that first showed distinct PTPN11 mutations (exon 8 and exon 13 "hotspots," e.g., Y279C, T468M) segregate specifically with the LEOPARD/NSML phenotype rather than classic NS.

RAF1 causal role: **Pandit B, et al. "Gain-of-function RAF1 mutations cause Noonan and LEOPARD syndromes with hypertrophic cardiomyopathy." Nat Genet. 2007;39(8):1007-1012. PMID:[17603483](https://pubmed.ncbi.nlm.nih.gov/17603483/)** — reported that of subjects with RAF1 mutations at two hotspots (mostly flanking Ser259, the 14-3-3 binding autoinhibitory residue), **95% developed HCM**, versus ~18% background HCM prevalence in general NS.

**Molecular mechanism distinction (critical for pathophysiology modeling):** Unlike classic-NS-causing PTPN11 variants, which are activating (gain-of-function for SHP2 phosphatase activity, increasing RAS-MAPK flux), **NSML-causing PTPN11 variants are catalytically inactivating and act as dominant-negatives** — see **Kontaridis MI, et al. "PTPN11 (Shp2) mutations in LEOPARD syndrome have dominant negative, not activating, effects." J Biol Chem. 2006;281(10):6785-6792. PMID:[16377799](https://pubmed.ncbi.nlm.nih.gov/16377799/)**: *"LEOPARD syndrome mutants are catalytically defective and act as dominant negative mutations that interfere with growth factor/Erk-mitogen-activated protein kinase-mediated signaling."* This distinction (LOF/dominant-negative SHP2 in NSML vs. GOF SHP2 in NS) is the central mechanistic bifurcation of the PTPN11-associated RASopathies, despite both converging on paradoxically hyperactive ERK signaling in specific tissue contexts (notably heart), likely via SHP2-independent scaffolding/PZR-mediated compensatory mechanisms.

**Risk factors:**
- *Genetic:* Autosomal dominant inheritance — an affected parent confers 50% transmission risk per child. Most cases are simplex (presumed de novo), though the proportion of de novo cases is not firmly established (GeneReviews).
- *Environmental:* None established. This is a purely germline monogenic disorder; there is no known toxin, occupational, or infectious contribution.
- *Age/sex:* No sex predilection reported. Onset is congenital/prenatal at the molecular level; clinical features (especially lentigines) accumulate progressively through childhood.

**Protective factors:** None specifically established for disease occurrence (it is fully penetrant once the variant is inherited/arises de novo). Notably, at the *phenotypic/metabolic* level, the LEOPARD-associated SHP2 mutation has been shown in mouse models to confer a protective metabolic phenotype (see Mechanism section) — an unusual "trade-off" finding.

**Gene-environment interactions:** Not established; NSML severity and expressivity appear to be driven by allelic/genotype effects (which gene, which specific residue) rather than documented environmental modifiers.

---

## 3. Phenotypes

All phenotype frequencies below are from GeneReviews (NBK1383) unless otherwise cited; HPO term suggestions are given per phenotype.

### Cutaneous
- **Multiple lentigines** (nearly all affected individuals; the defining/eponymous feature) — flat, black-brown macules 2–5 mm concentrated on face, neck, and upper trunk, sparing mucosa; typically absent at birth, appearing around age 4–5 years and increasing to the thousands by puberty. **HP:0001065** (Lentigines).
- **Café-au-lait macules** (70–80%), which may precede lentigines. **HP:0000957** (Café-au-lait spot).
- Nevi, may also occur.

### Cardiovascular
- **Cardiac defects overall** (~85% of patients).
- **Hypertrophic cardiomyopathy (HCM)** — the dominant cardiac feature, ~70–80% of those with cardiac defects (frequently left-ventricular, sometimes progressive, often presenting in infancy). **HP:0001639** (Hypertrophic cardiomyopathy).
- **Pulmonary valve stenosis** (~20–25%). **HP:0001642** (Pulmonic stenosis).
- **ECG/conduction abnormalities** (~25%) — including left-axis deviation, abnormal Q waves, arrhythmia. **HP:0003115** (Abnormal EKG).
- Gene-specific note: RAF1-mutated NSML shows near-universal (~95%) HCM association (Pandit et al. 2007, PMID:17603483), making RAF1-NSML one of the strongest known monogenic HCM risk genotypes.

### Growth
- **Short stature** — >50% significantly affected, most individuals below 25th percentile. Onset is typically postnatal, becoming apparent in childhood. **HP:0004322** (Short stature).

### Skeletal
- **Pectus deformity** (excavatum/carinatum), a cardinal diagnostic feature. **HP:0000766**/**HP:0000768**.

### Craniofacial
- **Dysmorphic facial features** (nearly all): widely spaced eyes/ocular hypertelorism, ptosis, low-set posteriorly rotated ears, broad or webbed neck. **HP:0000316** (Hypertelorism), **HP:0000508** (Ptosis).

### Genitourinary
- **Cryptorchidism** in ~30–33% of affected males. **HP:0000028**.
- Renal anomalies less common but part of surveillance recommendations.

### Neurologic / Sensory
- **Sensorineural hearing loss** (~15–20%), which can be congenital and is sometimes the presenting feature. **HP:0000407** (Sensorineural hearing loss).
- **Mild intellectual disability / learning difficulties** in ~30% (typically mild). **HP:0001256** (Intellectual disability, mild).
- Autism-spectrum-related traits have also been studied comparatively between NS and NSML cohorts (Molecular Autism, 2025), suggesting overlapping neurodevelopmental profiles across RASopathies, though NSML-specific autism prevalence data remain limited.
- Occasional reports of seizures and, rarely, intracerebral hemorrhage in PTPN11-mutated NSML (case report, PMC7983560).

### Oncologic (rare but notable)
- Elevated tumor predisposition has been reported in NSML/PTPN11-related RASopathies, including **neuroblastoma**, **acute myeloid leukemia**, and **acute lymphoblastic leukemia**; broader RASopathy literature reports solid tumors (rhabdomyosarcoma, neuroblastoma, bladder carcinoma) in ~15% of Noonan-spectrum patients by age 20, though NSML-specific tumor incidence figures are less precisely quantified than for classic juvenile myelomonocytic leukemia risk in NS.

**Progression/course:** Lentigines are absent at birth and accumulate over childhood/adolescence (progressive). HCM, if present, often manifests in infancy and can be progressive. Hearing loss and short stature are generally stable once established but require ongoing developmental/audiologic monitoring. Overall disease course is **chronic and lifelong**, non-remitting, with severity highly variable even within families (variable expressivity).

**Quality of life impact:** Cosmetic impact of lentigines can be psychosocially significant (visible facial/trunk pigmentation from childhood). Cardiac disease (HCM, arrhythmia risk) and hearing loss are the principal drivers of morbidity and long-term QoL burden; no NSML-specific EQ-5D/SF-36 data were identified in this search, but general RASopathy QoL literature emphasizes cardiac and neurodevelopmental domains as most impactful.

---

## 4. Genetic/Molecular Information

**Causal genes (detailed):**

| Gene | HGNC ID | Protein | Chromosomal locus | OMIM gene |
|---|---|---|---|---|
| PTPN11 | HGNC:9644 | SHP2 (tyrosine-protein phosphatase non-receptor type 11) | 12q24.13 | *176876 |
| RAF1 | HGNC:9829 | RAF1/c-Raf (serine/threonine kinase) | 3p25.2 | *164760 |
| BRAF | HGNC:1097 | B-Raf | 7q34 | *164757 |
| MAP2K1 | HGNC:6840 | MEK1 | 15q22.31 | *176872 |

**Pathogenic variant characteristics:**
- **Variant type:** Overwhelmingly missense (single amino-acid substitutions), consistent with a requirement for a specific structural/functional perturbation rather than simple loss of the gene product (null alleles are not typically disease-causing in this manner).
- **PTPN11 hotspots:** Classic NSML-associated residues cluster in the PTP catalytic domain, notably **Y279C** and **T468M** (together accounting for the majority of PTPN11-NSML cases), plus others including A461T, G464A, Q506P, Q510E/P, T507K. These are largely non-overlapping with the N-SH2/PTP-interface hotspots that cause classic gain-of-function NS (e.g., N308D, D61G).
- **Variant classification:** ClinVar lists numerous PTPN11 variants specifically annotated "Pathogenic"/"Likely pathogenic" for "Noonan syndrome with multiple lentigines" (e.g., NM_002834.5:c.836A>G p.Tyr279Cys; c.1403C>T p.Thr468Met — both classic NSML hotspot alleles).
- **RAF1 hotspot:** Predominantly substitutions flanking **Ser259** (a 14-3-3 binding/autoinhibitory residue), which when mutated relieve autoinhibition → constitutive kinase activation (Pandit et al. 2007, PMID:17603483).
- **Germline vs somatic:** NSML variants are constitutional/germline (heritable), distinguishing them from the *somatic* PTPN11 mutations found in juvenile myelomonocytic leukemia and other sporadic cancers, which — notably — are typically the *activating* class of PTPN11 mutation, not the NSML dominant-negative class.
- **Functional consequence:** PTPN11-NSML variants → loss of SHP2 catalytic (phosphatase) activity with dominant-negative interference of normal SHP2 signaling (PMID:16377799). RAF1/BRAF/MAP2K1-NSML variants → classic gain-of-function kinase activation, paralleling their mechanism in classic NS.
- **Allele frequency:** These are rare, highly penetrant pathogenic alleles essentially absent from population databases (gnomAD) consistent with disease severity and predominantly de novo/small-pedigree segregation.

**Modifier genes:** No well-established modifier genes for NSML severity have been robustly identified in the literature reviewed; expressivity varies substantially even within PTPN11-Y279C or T468M carriers, suggesting stochastic or background-genetic modulation not yet mapped.

**Epigenetic information:** No NSML-specific DNA methylation/chromatin studies were identified in this search; SHP2 broadly participates in growth-factor receptor signal transduction rather than direct epigenetic regulation, though downstream ERK activity can influence chromatin-modifying enzyme activity indirectly.

**Chromosomal abnormalities:** None — NSML is caused by point mutations, not large structural/copy-number chromosomal changes.

---

## 5. Environmental Information

No environmental toxins, radiation, pollutants, occupational exposures, lifestyle factors, or infectious agents are implicated in NSML causation — it is a purely monogenic germline disorder. This section is not applicable beyond noting the absence of such associations in the literature reviewed.

---

## 6. Mechanism / Pathophysiology

**Overview causal chain:** Germline PTPN11 (or RAF1/BRAF/MAP2K1) missense variant → altered RAS/MAPK (ERK) pathway signal transduction (tissue-context-dependent gain vs. loss of specific signaling outputs) → aberrant developmental signaling in cardiac, craniofacial, melanocytic, growth-plate, and neural tissues → the multisystem NSML phenotype.

**Molecular pathway:** RAS-MAPK (RAS/RAF/MEK/ERK) signal transduction pathway — GO/KEGG: **KEGG hsa04010** (MAPK signaling pathway); relevant GO biological process term **GO:0007265** (Ras protein signal transduction) and **GO:0038095** (Fc-epsilon receptor signaling pathway components feeding into ERK, where SHP2 also participates), plus **GO:0004725** (protein tyrosine phosphatase activity) for SHP2's catalytic function.

**SHP2/PTPN11-specific mechanism:** SHP2 is a cytoplasmic non-receptor protein-tyrosine phosphatase that normally acts as a *positive* transducer of RTK (receptor tyrosine kinase)-RAS-ERK signaling in most contexts (its N-SH2 domain autoinhibits the PTP domain at baseline; growth-factor-induced phosphotyrosine binding to the SH2 domains opens the catalytic pocket). Classic NS mutations destabilize this autoinhibited conformation → constitutively open/active SHP2 → excess RAS-ERK flux. **NSML mutations instead directly impair PTP catalytic activity** (many cluster in/near the catalytic cleft) while still permitting normal SH2-mediated docking, producing a catalytically-dead but still-scaffolding SHP2 species that acts as a **dominant-negative**, sequestering binding partners and paradoxically causing tissue-specific *hyperactivation* of ERK in some contexts (e.g., developing heart) via PZR-dependent or other scaffold-mediated compensatory signaling (Kontaridis 2006, PMID:16377799; Lauriol et al., JCI 2016, PMID:27348588).

**Cardiac hypertrophy mechanism (best-characterized organ pathophysiology):**
- **Lauriol J, et al. "Developmental SHP2 dysfunction underlies cardiac hypertrophy in Noonan syndrome with multiple lentigines." J Clin Invest. 2016;126(8):2989-3005. PMID:[27348588](https://pubmed.ncbi.nlm.nih.gov/27348588/)** — showed using a knock-in Ptpn11^Y279C/+ mouse (NSML model) that HCM originates from aberrant SHP2 signaling in the **developing endocardium**; endothelial-specific expression of the NSML mutant SHP2 was sufficient to induce adult-onset cardiac hypertrophy, implicating a developmental-origin, tissue-autonomous endocardial signaling defect rather than a purely adult cardiomyocyte-intrinsic process.
- **Marin TM, et al. (PZR paper) "PZR coordinates Shp2 Noonan and LEOPARD syndrome signaling in zebrafish and mice." J Clin Invest. 2011 (cited via PubMed). PMID:[24865967](https://pubmed.ncbi.nlm.nih.gov/24865967/)** — identifies PZR (a transmembrane SHP2-binding adaptor) as a convergence point coordinating both NS (GOF) and NSML (dominant-negative) SHP2 signaling in cardiac tissue across zebrafish and mouse models.
- **Marin TM, et al. "Rapamycin reverses hypertrophic cardiomyopathy in a mouse model of LEOPARD syndrome-associated PTPN11 mutation." J Clin Invest. 2011;121(3):1026-1043. PMID:[21339643](https://pubmed.ncbi.nlm.nih.gov/21339643/)** — demonstrated that NSML-associated PTPN11 mutant knock-in mice develop HCM via **mTOR pathway hyperactivation** downstream of the aberrant SHP2 signal, and that rapamycin (an mTOR inhibitor) reverses established cardiac hypertrophy — a key mechanistic and therapeutic-rationale finding, and one of the first proof-of-concept "mechanism-targeted therapy reverses RASopathy cardiomyopathy" studies.
- **Edouard T, et al./Kontaridis lab, JCI Insight, "Tyrosyl phosphorylation of PZR promotes hypertrophic cardiomyopathy in PTPN11-associated Noonan syndrome with multiple lentigines"** — further elaborates the PZR-tyrosine-phosphorylation axis as necessary for NSML-associated cardiac hypertrophy.

**Cellular processes involved:** Aberrant cardiomyocyte/endocardial growth-factor signaling → hypertrophic cardiomyocyte growth program (mTOR/ERK hyperactivation); dysregulated melanocyte proliferation/pigment production underlying lentigo formation; abnormal chondrocyte/growth-plate signaling contributing to short stature; RAS-MAPK-dependent craniofacial neural crest/mesenchymal patterning defects producing dysmorphic facial features (consistent with the broader RASopathy craniofacial mechanism also seen in NS/CFCS).

**Protein dysfunction:** Loss-of-function (catalytic) combined with dominant-negative scaffolding retention for PTPN11-NSML SHP2; classic gain-of-function kinase activation for RAF1/BRAF/MAP2K1-NSML variants — see UniProt **Q06124** (PTPN11/SHP2), **P04049** (RAF1), **P15056** (BRAF) for domain/structure annotations.

**Metabolic changes:** Notably, **Tajan M, et al. "LEOPARD syndrome-associated SHP2 mutation confers leanness and protection from diet-induced obesity." Proc Natl Acad Sci USA. 2014;111(42):E4494-E4503. PMID:[25288766](https://pubmed.ncbi.nlm.nih.gov/25288766/)** — found that mice carrying the NSML-associated SHP2 mutation display **reduced adiposity, resistance to diet-induced obesity, and improved carbohydrate metabolism**, with impaired adipogenesis and increased energy expenditure. This is a striking, disease-relevant metabolic phenotype directly attributable to loss of catalytic SHP2 activity in adipose tissue, representing a rare example of a RASopathy mutation conferring a "beneficial" systemic metabolic trade-off alongside its pathogenic manifestations (relevant to HMDB/metabolomics framing).

**Immune system involvement:** Not a primary disease axis for NSML specifically (contrast with somatic activating PTPN11 mutations, which are strongly linked to myeloproliferative/leukemic disease via hematopoietic stem/progenitor cell effects — a related but mechanistically distinct PTPN11 disease axis, per the eLife 2022 HSPC inflammatory-response paper referenced in the broader PTPN11 literature).

**Single-cell / advanced technologies:** Endothelial/endocardial-lineage-restricted Cre-driver mouse studies (Lauriol 2016) represent the primary cell-type-resolved mechanistic dissection available; no human single-cell or spatial transcriptomic NSML-specific datasets were identified in this search.

**Suggested GO/CL terms:**
- GO:0004725 — protein tyrosine phosphatase activity (SHP2 catalytic function)
- GO:0007173 — epidermal growth factor receptor signaling pathway (upstream RTK input)
- GO:0043408 — regulation of MAPK cascade
- GO:0038095 — Fc-epsilon receptor signaling pathway (SHP2-relevant scaffold context)
- CL:0000746 — cardiac muscle cell (myocyte hypertrophy)
- CL:0002350 — endocardial cell (developmental origin of cardiac hypertrophy per Lauriol 2016)
- CL:0000148 — melanocyte (lentigo formation)
- CL:0000138 — chondrocyte (growth-plate/short-stature mechanism, by analogy to NS)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Heart (myocardium/endocardium — HCM, pulmonary valve, conduction system), skin (melanocytes — lentigines, café-au-lait), skeletal system (chest wall — pectus; growth plates — short stature), craniofacial skeleton/soft tissue, inner ear (cochlea — sensorineural hearing loss), gonads (testes — cryptorchidism).
- **Secondary:** CNS (mild ID, rare seizures/hemorrhage), hematopoietic/lymphoid tissue (rare leukemia association), neural crest-derived tissues broadly (neuroblastoma risk).
- **Body systems:** Cardiovascular, integumentary, musculoskeletal, endocrine/growth, auditory, genitourinary, nervous, and (rarely) hematologic/oncologic systems.

**Tissue/cell level:** Cardiomyocytes and endocardial cells (**CL:0000746**, **CL:0002350**); epidermal melanocytes (**CL:0000148**); growth-plate chondrocytes (**CL:0000138**); cochlear hair cells/spiral ganglion (sensorineural hearing loss mechanism, by analogy — **CL:0000202** hair cell).

**Subcellular level:** Cytoplasmic signaling (SHP2 is cytosolic/membrane-proximal — **GO:0005829** cytosol, **GO:0005886** plasma membrane for RTK-proximal docking); nuclear ERK translocation for transcriptional output (**GO:0005634**).

**UBERON localization:** UBERON:0000948 (heart), UBERON:0002050 (embryonic heart tube/endocardium), UBERON:0002097 (skin), UBERON:0001911 (skin of face), UBERON:0002415 (thorax/chest wall — pectus), UBERON:0001846 (auditory receptor organ/cochlea — hearing loss), UBERON:0000473 (testis — cryptorchidism).

**Lateralization:** Not a laterality-defined disorder; findings are generally bilateral/symmetric (facial features, hearing loss when present) with the exception of asymmetric distribution of individual lentigines.

---

## 8. Temporal Development

- **Onset:** Congenital at the molecular/developmental level (a germline variant present from conception; cardiac and craniofacial developmental effects begin prenatally per the endocardial-origin HCM mechanism). Clinically apparent features emerge across a **spectrum**: cardiac defects can be detected prenatally/neonatally; lentigines are characteristically **absent at birth**, emerging around age 4–5 years; short stature becomes apparent through childhood; hearing loss may be congenital or emerge later.
- **Onset pattern:** Insidious/progressive for pigmentary and growth features; can be acute/critical in infancy for severe neonatal HCM presentations (rare RAF1-mutant cases reported with severe neonatal HCM).
- **Progression:** Lentigines progressively increase in number from childhood through puberty (thousands by adolescence). HCM, when present, is often progressive, particularly in RAF1-mutated cases, and can require escalating cardiac management. Short stature and craniofacial features are generally stable once fully expressed in adulthood.
- **Disease course pattern:** Chronic, lifelong, generally non-remitting for the structural/pigmentary features; cardiac status may stabilize, progress, or (rarely, with mechanism-targeted therapy such as MEK inhibition) improve.
- **Critical periods:** Prenatal/early postnatal cardiac development is a mechanistically critical window (per the endocardial-origin HCM data), suggesting early identification and cardiac surveillance are especially important in infancy.

---

## 9. Inheritance and Population

**Epidemiology:** Population prevalence is **not precisely established** — NSML is considered a rare condition even among RASopathies; GeneReviews notes ~150+ individuals reported in the literature to date. For context, classic Noonan syndrome (the broader RASopathy family) occurs in ~1:1,000–1:2,500 live births, but NSML is substantially rarer than NS overall.

**Inheritance pattern:** **Autosomal dominant** (all four causal genes — PTPN11, RAF1, BRAF, MAP2K1).

**Penetrance:** High/complete penetrance for the core phenotype in reported pedigrees, though **expressivity is highly variable** — even among relatives sharing the identical variant, severity of cardiac, cutaneous, and growth features differs substantially.

**Genetic anticipation:** Not a described feature (this is a missense-variant disorder, not a repeat-expansion disorder).

**Germline mosaicism:** Recognized as a mechanism for sibling recurrence in families where the proband's variant is presumed de novo — GeneReviews estimates **sibling recurrence risk of ~1%** in de novo cases, attributable to possible parental germline mosaicism.

**Founder effects:** No specific NSML founder population/mutation was identified in this search (contrast with some other RASopathy-adjacent conditions where specific founder alleles are described in isolated populations).

**Consanguinity:** Not a relevant risk factor, given the autosomal dominant (not recessive) mode of inheritance.

**Population demographics:** No specific ethnic or geographic enrichment was identified in the sources reviewed; reported cases span multiple populations and geographic regions (Italy, Korea, China, and others represented in the literature surveyed here).

**Sex ratio:** No sex predilection reported.

**Age distribution:** Diagnosed across the lifespan, from prenatal/neonatal (via cardiac findings and, increasingly, prenatal genetic testing) through adulthood; many cases are identified in childhood when lentigines and growth/cardiac features become apparent.

---

## 10. Diagnostics

**Clinical diagnostic criteria (per GeneReviews/van der Burgt-style criteria):**
- Multiple lentigines **plus 2 other cardinal features** (cardiac abnormality; short stature; pectus deformity; dysmorphic facial features), **OR**
- In the absence of lentigines: **3 cardinal features plus an affected first-degree relative**.

**Genetic testing:**
- **Recommended approach:** Given genetic heterogeneity, a **multigene panel** covering PTPN11, RAF1, BRAF, and MAP2K1 (and often the broader RASopathy/Noonan-spectrum gene panel to capture phenocopies) is the preferred first-tier test, per GeneReviews.
- **Single-gene testing:** PTPN11 sequencing alone captures >95% of molecularly-confirmed cases and is a reasonable first step if resources are constrained, given the high prior probability.
- **Detection rate:** Sequence analysis (Sanger or NGS) detects the causal variant in nearly 100% of cases with a variant in PTPN11 or RAF1 once a gene is targeted; large deletions/duplications are not a recognized mechanism (this is a missense-only disease mechanism).
- **WES/WGS:** Useful when the multigene panel is non-diagnostic or when the phenotype is atypical/overlaps other RASopathies; exome-first strategies are increasingly used given the broader RASopathy differential.
- **Prenatal/preimplantation testing:** Available once a familial pathogenic variant is identified.

**Clinical/laboratory tests (non-genetic):**
- **Echocardiogram** — first-line for HCM/pulmonary stenosis detection; LOINC-coded structured echo reporting applicable.
- **ECG** — for conduction abnormalities.
- **Audiology (audiometry)** — for sensorineural hearing loss screening.
- **Ophthalmologic exam** — for hypertelorism-associated or other ocular findings.
- **Renal ultrasound** — part of baseline evaluation per GeneReviews surveillance.
- **Developmental/neuropsychological assessment** — for intellectual disability/learning difficulties.

**Differential diagnosis (critical for accurate curation, per GeneReviews):**
- **Classic Noonan syndrome** — NSML is distinguished primarily by the profuse pigmented lesions/lentigines, which NS typically lacks; molecular testing (LOF/dominant-negative vs GOF PTPN11 variant) is definitive.
- **Cardiofaciocutaneous syndrome (CFCS)** — more severe intellectual disability, structural CNS anomalies, seizures, more extensive skin pathology than NSML.
- **Costello syndrome** — another RASopathy on the differential, with its own distinct HRAS-driven features.
- **Turner syndrome** — requires karyotype exclusion; Turner syndrome shows predominantly left-sided heart defects (coarctation, bicuspid aortic valve) rather than HCM.
- **Williams syndrome** — requires 7q11.23 deletion testing to exclude.
- **Legius syndrome / NF1** — for café-au-lait-predominant presentations without lentigines/cardiac features.

**Screening:** No population-based newborn screening program exists for NSML (it is not amenable to biochemical newborn screening); identification is via clinical suspicion (cardiac finding, dermatologic finding) followed by targeted or panel genetic testing, or via cascade testing of relatives once a familial variant is known.

---

## 11. Outcome/Prognosis

**Survival/mortality:** No population-based survival statistics were identified in this search; prognosis is heavily dependent on the severity of the cardiac phenotype — severe, early-onset (especially RAF1-associated) HCM is the principal driver of morbidity/mortality risk, while individuals without significant cardiac involvement generally have a normal life expectancy.

**Morbidity/complications:**
- Progressive/obstructive HCM can lead to heart failure, arrhythmia, and (in severe pediatric cases) need for advanced heart-failure therapies.
- Sensorineural hearing loss can affect speech/language development if unaddressed.
- Rare but reported complications include neuroblastoma, leukemia (AML/ALL), and — in isolated case reports — intracerebral hemorrhage in PTPN11-mutated individuals (PMC7983560).
- Psychosocial morbidity from visible cutaneous lentiginosis.

**Recovery potential / treatment response:** Emerging mechanism-targeted therapy data (MEK inhibition — see Treatment section) show that cardiac hypertrophy can be **pharmacologically reversed or ameliorated** in some cases, a substantial shift from purely supportive management historically available.

**Prognostic factors:** Causal gene is a major prognostic determinant — RAF1-mutated NSML carries a markedly higher (~95%) risk of HCM than PTPN11-mutated NSML, making genotype an important prognostic/surveillance-intensity variable.

---

## 12. Treatment

**Standard/supportive management (per GeneReviews):**
- **Cardiac:** Standard HCM management (beta-blockers, surveillance for outflow obstruction/arrhythmia, surgical septal myectomy in severe obstructive cases); standard management of structural defects (e.g., pulmonary valve stenosis — balloon valvuloplasty as needed).
- **Ophthalmologic:** Management of eye anomalies/eye movement abnormalities.
- **Audiologic:** Hearing aids/early intervention for sensorineural hearing loss.
- **Endocrine/growth:** **Growth hormone therapy may be contraindicated in individuals with hypertrophic cardiomyopathy** (explicit GeneReviews caution) — an important genotype-informed prescribing constraint distinct from classic NS management, where GH therapy is more routinely considered.
- **Urologic:** Standard management of cryptorchidism (orchiopexy).
- **Neurodevelopmental:** Early intervention/educational support for developmental and learning issues; seizure management when present.
- **Dermatologic:** Cosmetic/dermatologic management of lentigines is generally elective (no medical necessity), though psychosocial support may be warranted.

**Emerging mechanism-targeted (MEK inhibitor) therapy — RASopathy-wide, actively being extended to NSML/HCM:**
- **Trametinib** (a selective, FDA-approved MEK1/2 inhibitor originally for melanoma) has shown efficacy in case reports and early trials for RASopathy-associated obstructive HCM, including RAF1-associated Noonan-spectrum cardiomyopathy — see *"Treatment of RAF1-Related Obstructive Hypertrophic Cardiomyopathy by MEK Inhibition Using Trametinib"* and *"MEK Inhibition in a Newborn with RAF1-Associated Noonan Syndrome Ameliorates Hypertrophic Cardiomyopathy"* (PMC8774485).
- An active randomized clinical trial (**NCT06555237**, "MEK Inhibitors for the Treatment of Hypertrophic Cardiomyopathy in Patients With RASopathies") is evaluating trametinib in children (age 0–18) with RAS-MAPK-pathway-confirmed HCM.
- Mechanistically, this rationale is directly supported by the mouse-model literature above (Marin 2011, PMID:21339643 — mTOR inhibition with rapamycin reverses NSML-model HCM; and the broader RAS-MAPK hyperactivation-in-cardiac-tissue mechanism), even though the causal PTPN11-NSML lesion is a phosphatase loss-of-function — underscoring that downstream pathway output (not just the proximal lesion direction) determines therapeutic targetability. **MAXO:0000647** (chemotherapy — closest generic action term; trametinib itself would be better captured via `therapeutic_agent`/NCIT/CHEBI rather than forcing into a chemotherapy action term) and a Pharmacotherapy (**NCIT:C15986**) treatment_term with `therapeutic_agent` bound to Trametinib (**NCIT:C77908**) would be the appropriate dismech-style annotation pattern.
- **Rapamycin/mTOR inhibitors** — proof-of-concept reversal of HCM in the NSML mouse model (PMID:21339643) supports mTOR inhibition as an alternative/complementary mechanistic target, though clinical translation specifically in NSML patients is less advanced than for trametinib.

**Surgical:** Cardiac surgery (septal myectomy) for severe obstructive HCM; orchiopexy for cryptorchidism; standard pectus repair surgery when clinically indicated.

**Suggested MAXO terms:**
- MAXO:0000011 — physical therapy (as needed for developmental support)
- MAXO:0000004 — surgical procedure (cardiac/orchiopexy/pectus)
- MAXO:0000079 — genetic counseling
- MAXO:0000950 — supportive care

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense (this is a de novo/inherited germline genetic disorder, not preventable via risk-factor modification); however, family planning options (preimplantation genetic testing, prenatal diagnosis) constitute the primary "prevention" lever once a familial pathogenic variant is known.

**Secondary prevention (early detection):** Early echocardiographic screening in infants of affected parents (or those presenting with suggestive features) allows early HCM detection before symptomatic heart failure develops; early audiologic screening supports early intervention for hearing loss.

**Genetic counseling:** Central to NSML management — counseling on 50% transmission risk to offspring of an affected individual, ~1% sibling recurrence risk in de novo cases (germline mosaicism), variable expressivity (a parent with mild disease can have a more severely affected child, and vice versa), and reproductive options (prenatal testing, preimplantation genetic testing). GeneReviews and NSGC-aligned genetic counseling resources are the relevant authorities.

**Screening (population level):** No population-based newborn or carrier screening program exists for NSML; identification remains clinically/case-driven.

**Prophylaxis:** No specific prophylactic medications are indicated beyond standard cardiac surveillance-triggered management (e.g., beta-blockade once HCM is identified, per general HCM management guidelines).

---

## 14. Other Species / Natural Disease

No naturally-occurring NSML has been reported in non-human species in the literature surveyed — this is not a recognized veterinary/companion-animal disease (OMIA search not specifically performed but no indication of natural animal disease emerged from the mechanism-focused searches). All animal data relate to **induced/engineered models** (see Section 15) rather than spontaneously-occurring disease in other species. PTPN11 orthologs are broadly conserved across vertebrates (mouse *Ptpn11*, zebrafish *ptpn11a*/*ptpn11b*), supporting the strong cross-species conservation of the underlying RAS-MAPK signaling mechanism, but no natural disease phenocopy has been documented.

---

## 15. Model Organisms

**Mouse models (genetic, knock-in):**
- **Ptpn11^Y279C/+ knock-in mouse** — the principal NSML mouse model, used in the Lauriol 2016 (PMID:27348588) and Marin 2011 (PMID:21339643) studies, recapitulating hypertrophic cardiomyopathy and enabling dissection of the developmental endocardial origin of cardiac hypertrophy and the mTOR-dependence of the phenotype (reversible with rapamycin).
- **Ptpn11^D61G/+ mouse** — the classic-NS gain-of-function comparator model, used alongside the Y279C NSML model in the PZR studies (PMID:24865967) to directly contrast GOF-NS vs. dominant-negative-NSML mechanisms in the same experimental system.
- Adipose-tissue-targeted studies of the NSML mutation (Tajan et al. 2014, PMID:25288766) demonstrated the leanness/metabolic-protection phenotype, illustrating how the same germline mutation produces organ-specific, sometimes opposing, physiological consequences (pathogenic in heart, "protective" in adipose tissue).

**Zebrafish models:**
- Zebrafish carry two *ptpn11* paralogs (*ptpn11a*, *ptpn11b*), both functionally relevant (PLOS ONE, PMC3988099), enabling developmental dissection of SHP2 function; D61G (NS) and A462T (NSML-equivalent) Shp2 zebrafish models have been used in the PZR-coordination studies (PMID:24865967) to study cardiac and hematopoietic phenotypes with the transparency/rapid-development advantages of the zebrafish system.
- Zebrafish models have also been used more broadly to study Shp2-MAPK signaling in developmental contexts (e.g., fin-fold regeneration), providing mechanistic insight transferable to the RASopathy signaling framework even outside the cardiac-specific NSML literature.

**Phenotype recapitulation:** The mouse knock-in models successfully recapitulate the cardinal cardiac phenotype (hypertrophic cardiomyopathy) and have been sufficient to establish causal, cell-type-specific (endocardial), and pathway-specific (mTOR-dependent) mechanisms, and to demonstrate pharmacological reversibility — a strong translational validation. Recapitulation of the pigmentary (lentigines), growth (short stature), and neurodevelopmental phenotypes in mouse/zebrafish models is less well documented in the sources reviewed here and would need separate confirmation before being asserted as strongly validated.

**Model limitations:** As with most RASopathy models, full recapitulation of the human variable-expressivity pattern (why genetically identical mutations produce a spectrum of severity across human family members) is not achieved in inbred mouse models, which are typically more phenotypically uniform.

**Applications:** These models have directly enabled (1) mechanistic dissection of GOF-NS vs. dominant-negative-NSML divergence at the same locus, (2) identification of developmental (endocardial) origin of adult HCM, and (3) preclinical proof-of-concept for both mTOR-inhibitor (rapamycin) and, by extension via the broader RASopathy MEK-inhibitor literature, MEK-inhibitor (trametinib) therapeutic strategies now advancing to human clinical trials (NCT06555237).

---

## Summary Table: Suggested Ontology Term Bindings for KB Curation

| Domain | Suggested term | ID |
|---|---|---|
| Disease | Noonan syndrome with multiple lentigines | MONDO:0007893 |
| Gene (primary) | PTPN11 | hgnc:9644 |
| Gene | RAF1 | hgnc:9829 |
| Gene | BRAF | hgnc:1097 |
| Gene | MAP2K1 | hgnc:6840 |
| Phenotype | Lentigines | HP:0001065 |
| Phenotype | Café-au-lait spot | HP:0000957 |
| Phenotype | Hypertrophic cardiomyopathy | HP:0001639 |
| Phenotype | Pulmonic stenosis | HP:0001642 |
| Phenotype | Sensorineural hearing loss | HP:0000407 |
| Phenotype | Short stature | HP:0004322 |
| Phenotype | Hypertelorism | HP:0000316 |
| Phenotype | Ptosis | HP:0000508 |
| Phenotype | Cryptorchidism | HP:0000028 |
| Cell type | Cardiac muscle cell | CL:0000746 |
| Cell type | Endocardial cell | CL:0002350 |
| Cell type | Melanocyte | CL:0000148 |
| Biological process | Ras protein signal transduction | GO:0007265 |
| Molecular function | Protein tyrosine phosphatase activity | GO:0004725 |
| Treatment | Pharmacotherapy (+ trametinib therapeutic_agent) | NCIT:C15986 / NCIT:C77908 |

---

## Key References (PMID-verified in this research)

1. Digilio MC, et al. Grouping of multiple-lentigines/LEOPARD and Noonan syndromes on the PTPN11 gene. *Am J Hum Genet.* 2002;71(2):389-394. PMID:[12161596](https://pubmed.ncbi.nlm.nih.gov/12161596/)
2. Kontaridis MI, et al. PTPN11 (Shp2) mutations in LEOPARD syndrome have dominant negative, not activating, effects. *J Biol Chem.* 2006;281(10):6785-6792. PMID:[16377799](https://pubmed.ncbi.nlm.nih.gov/16377799/)
3. Pandit B, et al. Gain-of-function RAF1 mutations cause Noonan and LEOPARD syndromes with hypertrophic cardiomyopathy. *Nat Genet.* 2007;39(8):1007-1012. PMID:[17603483](https://pubmed.ncbi.nlm.nih.gov/17603483/)
4. Marin TM, et al. Rapamycin reverses hypertrophic cardiomyopathy in a mouse model of LEOPARD syndrome-associated PTPN11 mutation. *J Clin Invest.* 2011;121(3):1026-1043. PMID:[21339643](https://pubmed.ncbi.nlm.nih.gov/21339643/)
5. PZR coordinates Shp2 Noonan and LEOPARD syndrome signaling in zebrafish and mice. PMID:[24865967](https://pubmed.ncbi.nlm.nih.gov/24865967/)
6. Tajan M, et al. LEOPARD syndrome-associated SHP2 mutation confers leanness and protection from diet-induced obesity. *PNAS.* 2014;111(42):E4494-E4503. PMID:[25288766](https://pubmed.ncbi.nlm.nih.gov/25288766/)
7. Lauriol J, et al. Developmental SHP2 dysfunction underlies cardiac hypertrophy in Noonan syndrome with multiple lentigines. *J Clin Invest.* 2016;126(8):2989-3005. PMID:[27348588](https://pubmed.ncbi.nlm.nih.gov/27348588/)
8. GeneReviews: Sarkozy A, Digilio MC, Zampino G, et al. Noonan Syndrome with Multiple Lentigines. [NBK1383](https://www.ncbi.nlm.nih.gov/books/NBK1383/) (authoritative source for diagnostic criteria, frequencies, and management recommendations cited throughout).
9. Orphanet: Leopard syndrome, ORPHA:500. [orpha.net/consor/cgi-bin/OC_Exp.php?Expert=500](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Expert=500)
10. OMIM #151100 (LEOPARD syndrome 1/PTPN11), #611554 (LEOPARD syndrome 2/RAF1), #613707 (LEOPARD syndrome 3/BRAF).

**Note on evidence gaps:** Population-based prevalence/incidence figures, NSML-specific quality-of-life instrument data, MAP2K1/BRAF variant-level detail (beyond "rare reported cases"), and precise quantified tumor-risk statistics specific to NSML (as opposed to the broader Noonan spectrum) were not found with high-confidence primary-source citations in this search and would need targeted follow-up (e.g., direct OMIM/Orphanet full-text review, ClinVar variant-level pull, and a dedicated PubMed search for NSML-specific malignancy cohort studies) before being asserted as curated facts in a knowledge-base entry.