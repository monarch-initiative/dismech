---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T13:20:00.305565'
end_time: '2026-08-01T13:39:55.064830'
duration_seconds: 1194.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CAPOS Syndrome
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
  web_search_requests: 4
  num_turns: 65
  total_cost_usd: 5.781391000000001
  session_id: d9bb9bac-42a9-4e1c-be9a-785ab5e0bf67
  stop_reason: end_turn
citation_count: 72
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CAPOS Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CAPOS Syndrome** covering all of the
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

# Comprehensive Research Report: CAPOS Syndrome

**Prepared:** 1 August 2026 · **Target:** CAPOS syndrome · **MONDO:0011038** · Category: Mendelian (monogenic, autosomal dominant)

---

## ⚠️ Evidence-Provenance Note (read before curating)

Abstracts below were retrieved via NCBI E-utilities and Europe PMC. Quotes marked **[V]** were captured from raw abstract text and are believed to be verbatim; quotes marked **[P]** came through a summarizing fetch layer and **may be paraphrased**. Per the dismech SOP, **every** snippet must be re-verified with `just fetch-reference PMID:XXXX` + `just validate-references` before commit. Ontology IDs marked **[OLS-verified]** were checked against the EBI Ontology Lookup Service during this pass; all others must be checked with `just validate-terms`.

**Named Entity Confusion (NEC) preflight — PASSED.** A literature search on the bare string "CAPOS" returns several unrelated entities that must be excluded: PMID:8556850 (California Adult Performance Outcome Survey), PMID:15889615 (concentration-camp "Capos"), PMID:23452420 (cannulated paediatric osteotomy system), PMID:23942172 (CAPO, Canadian Assoc. of Psychosocial Oncology), and multiple obstetric "composite adverse perinatal outcome (CAPO)" papers (PMID:39233371, PMID:40623699). The gene named throughout the retained corpus is **ATP1A3**, matching the MONDO:0011038 definition and the OMIM:601338 xref — identity confirmed.

---

## 1. Disease Information

### Overview

CAPOS syndrome is a **rare autosomal dominant neurological disorder** whose acronym encodes its five cardinal features: **C**erebellar ataxia, **A**reflexia, **P**es cavus, **O**ptic atrophy, and **S**ensorineural hearing loss. Its defining natural-history signature is *episodic*: early-childhood onset of one to three **acute, fever-triggered ataxic encephalopathy episodes**, each followed by incomplete recovery leaving a stepwise-accumulating fixed deficit, with subsequently **progressive** optic atrophy and sensorineural hearing loss.

It is caused, in every genetically confirmed case reported to date, by a **single recurrent heterozygous missense variant** in *ATP1A3*: **c.2452G>A, p.(Glu818Lys)** — making CAPOS one of the most genetically homogeneous Mendelian disorders known.

The syndrome was delineated clinically in 1996 by Nicolaides, Appleton and Fryer (PMID:8733056) from a single three-generation family; the molecular cause remained unknown for 18 years until whole-exome sequencing in 2014 (PMID:24468074).

**Original clinical delineation** (PMID:8733056, *J Med Genet* 1996) **[V]**:
> "We report three family members who presented with a relapsing, early onset cerebellar ataxia, associated with progressive optic atrophy and sensorineural deafness. All three patients have areflexia (in the absence of a peripheral neuropathy), a pes cavus deformity, and show varying degrees of severity. Extensive neurological investigations have been normal, and the aetiology and pathophysiology of this disorder remain unclear."

Prescient closing note from the same abstract **[V]**: *"which is likely to either have an autosomal dominant or maternal mitochondrial pattern of inheritance"* — the mitochondrial hypothesis was later excluded, but the phenotype's mitochondrial *mimicry* remains a recognized diagnostic pitfall (see §10).

### Key Identifiers

| Resource | Identifier |
|---|---|
| **MONDO** | **MONDO:0011038** — "cerebellar ataxia-areflexia-pes cavus-optic atrophy-sensorineural hearing loss syndrome" [OLS-verified] |
| OMIM (phenotype) | **601338** — CEREBELLAR ATAXIA, AREFLEXIA, PES CAVUS, OPTIC ATROPHY, AND SENSORINEURAL HEARING LOSS; CAPOS |
| OMIM (gene) | **182350** (*ATP1A3*) |
| Orphanet | **ORPHA:1171** |
| MedGen | CUI **C1832466**, UID **318633** |
| MeSH (supplementary concept) | **C535351** |
| UMLS | C1832466 |
| SNOMED CT | 720634003 |
| GARD | 0001188 |
| NANDO (Japan) | 1200526 |
| ICD-10 | Not authoritatively confirmed in this pass; Orphanet maps most hereditary ataxia-plus syndromes to **G11.8** ("Other hereditary ataxias"). **Verify before curating.** |
| ICD-11 | Not confirmed. **Verify.** |
| HGNC (gene) | **HGNC:801** → dismech lowercase form **`hgnc:801`** |
| dbSNP | rs587777771 |
| ClinVar | VCV **000156238** |

### Synonyms and Alternative Names

- **CAPOS syndrome** (exact synonym, MONDO)
- **CAOS syndrome** — used when pes cavus is absent; pes cavus occurs in only ~30% of patients (PMID:25895915, PMID:29625811, PMID:31780320). *Recommend curating "CAOS" as a related synonym and noting the acronym instability.*
- Cerebellar ataxia – areflexia – pes cavus – optic atrophy – sensorineural hearing loss (long form)
- Cerebellar ataxia, areflexia, pes cavus, optic atrophy and sensorineural deafness
- **Contextual umbrella term:** *ATP1A3-related disorder* / *ATP1A3 spectrum disorder* — the currently preferred framing (see §2).

### Information Provenance

Knowledge of CAPOS derives almost entirely from **aggregated case-level literature** (single families and small multi-family series), not from EHR/registry data. The largest CAPOS-specific series is **18 genetically confirmed patients from 11 families** (PMID:29305691). GeneReviews (PMID:20301294, *ATP1A3-Related Disorder*) tabulates **53 individuals from 40 families** reported to date **[P]**. There is no CAPOS-specific patient registry; affected individuals are captured within broader ATP1A3/AHC registries (e.g. the AHC Foundation, IAHCRC consortium). Consequently every frequency figure in this report is **literature-ascertainment-biased toward severe/complete phenotypes**.

---

## 2. Etiology

### Disease Causal Factors

CAPOS is a **pure monogenic channelopathy/pump-opathy** with a **single causal allele**:

> **ATP1A3 NM_152296.5:c.2452G>A, p.(Glu818Lys)** — heterozygous, autosomal dominant.

PMID:24468074 (Demos et al., *Orphanet J Rare Dis* 2014) established this **[V]**:
> "We found an identical heterozygous missense mutation, c.2452G > A (p.(Glu818Lys)), in the Na⁺/K⁺ ATPase α₃(ATP1A3) gene in the proband and his affected sister and mother, but not in either unaffected maternal grandparent, in the first family. The same mutation was also identified in the proband and three other affected members of the second family and in all three affected members of the third family. This mutation was not found in more than 3600 chromosomes from unaffected individuals."

Genetic homogeneity was confirmed independently (PMID:27091223, Maas et al. 2016 — title: *"The Genetic Homogeneity of CAPOS Syndrome"*) and re-affirmed in the 2021 animal-model review (PMID:34612482) **[P]**: *"All of the reported cases of CAPOS, to date, are heterozygous for a single recurrent missense mutation, E818K."*

**Locus heterogeneity: none reported.** No non-*ATP1A3* cause and no second *ATP1A3* allele has ever been shown to produce the full CAPOS phenotype. Other *ATP1A3* variants produce *different* allelic disorders (see §4).

### Risk Factors

**Genetic risk factors**
- The *only* genetic risk factor is inheritance/de-novo occurrence of p.Glu818Lys. There are no known susceptibility loci or GWAS signals (CAPOS is far too rare for GWAS).
- **No modifier genes have been identified.** However, the marked intrafamilial variability in severity within pedigrees carrying the identical allele (PMID:26453127, PMID:28483396, PMID:34655904) is strong indirect evidence that modifiers — genetic, epigenetic, or stochastic-developmental — exist. *This is a genuine knowledge gap; curate as `discussions: kind: KNOWLEDGE_GAP`.*
- Parental age effects on the de novo rate have not been studied.

**Environmental risk factors (episode triggers, not disease-causation factors)**

The critical distinction for CAPOS: environment does not cause the disease, but it **precipitates every acute decompensation**. Documented triggers:

| Trigger | Evidence |
|---|---|
| **Febrile illness** (the dominant trigger) | PMID:8733056, PMID:24468074, PMID:27091223 **[V]** — episodes "were consistently associated with febrile illness"; PMID:31410291 **[V]** — "three fever related episodes of acute neurological deterioration" |
| **Pregnancy and the peripartum period** | PMID:29090527 **[V]** — "one of the affected individuals experienced markedly worsening features during her three pregnancies and in the immediate postpartum period, a potential element of the natural history of CAPOS previously unreported" |
| Physical/emotional/psychological stress; missed meals; sleep deprivation | GeneReviews **[P]** (generic ATP1A3 guidance) |
| Environmental stress: bright/fluorescent light, heat/cold, excessive noise, crowds | GeneReviews **[P]** (generic ATP1A3 guidance; strongest evidence in AHC) |
| Non-febrile infection (e.g. URTI) | PMID:36484864 **[V]** — for AHC in the same cohort, "the most common trigger was an upper respiratory tract infection without fever"; extrapolation to CAPOS is uncertain |

- **Age**: onset window is narrow — usually 6 months to 5 years (GeneReviews **[P]**). The risk of a *first* episode falls sharply after early childhood, though adult-onset episodes occur (PMID:29625811 reports an episode at age 37).
- **Sex**: no established sex bias for CAPOS; pregnancy is a female-specific additional trigger.
- **Family history**: ~50% of cases are familial (see §9).

### Protective Factors

- **Genetic protective factors:** none known. No protective/modifier alleles reported.
- **Environmental protective factors:** none proven. Plausible, biologically coherent, but **unvalidated** candidates:
  - Aggressive antipyresis and early treatment of febrile illness — PMID:35047275 **[V]**: *"Aggressive management of febrile illness may be helpful in alleviating the symptoms."* (This paper describes a residue-756 FIPWE patient, not CAPOS — apply with care.)
  - Prophylactic acetazolamide — PMID:27091223 **[V]**: *"After initiation of acetazolamide in two patients, no further episodes occurred."* (n=2, uncontrolled.)
  - Routine childhood immunization (indirect, by reducing febrile-illness burden) — plausible but **entirely unstudied** in CAPOS.

### Gene–Environment Interaction

CAPOS is a textbook **G×E disorder**, and this is arguably its single most curation-worthy mechanistic feature. The mechanistic model:

> A **thermally/metabolically marginal Na⁺/K⁺-ATPase α3 pump** (constitutive, genotype-determined) becomes **functionally insufficient only when neuronal Na⁺ load and metabolic demand rise** (fever-induced increases in metabolic rate, neuronal firing, and possibly temperature-dependent destabilization of the mutant pump), producing acute neuronal-excitability failure that manifests as an ataxic-encephalopathic episode.

The functional data supporting the "marginal pump" leg (PMID:30409907) show the mutant pump's deficits *"precluded proper pump activation under physiological conditions"* **[V]**. The fever leg is clinically overwhelming but **mechanistically unproven at the molecular level** — no study has shown temperature-dependent aggravation of E818K pump function *in vitro*.

Explicitly acknowledged as unknown (PMID:30862413, on the closely related RECA phenotype) **[V]**:
> "The pathophysiology of the dysfunctions of the mutated ATPase pump, triggered by fever is unknown."

**Curation recommendation:** model this as a disease-level `mechanistic_hypotheses` entry with `status: EMERGING`, and attach a `discussions` entry of `kind: KNOWLEDGE_GAP` with `proposed_experiments` (temperature-dependent two-electrode voltage clamp of E818K-expressing oocytes; E818K knock-in mouse thermal challenge — see §15, no such mouse exists).

---

## 3. Phenotypes

### 3.1 HPO Annotations (from the official HPO annotation set for OMIM:601338)

These are the curated HPO annotations with their published *n/N* frequencies. **These are directly usable as dismech `phenotype_term` bindings with `frequency` — but note the small denominators (n≤11) and severe ascertainment bias.**

| HP ID | Label | Frequency (n/N) | dismech `FrequencyEnum` |
|---|---|---|---|
| **HP:0000648** | Optic atrophy | **11/11 (100%)** | OBLIGATE / VERY_FREQUENT |
| **HP:0001284** | Areflexia | **11/11 (100%)** | OBLIGATE / VERY_FREQUENT |
| **HP:0002131** | Episodic ataxia | **10/10 (100%)** | VERY_FREQUENT |
| **HP:0000407** | Sensorineural hearing impairment | **10/10 (100%)** | VERY_FREQUENT |
| **HP:0001324** | Muscle weakness | **10/10 (100%)** | VERY_FREQUENT |
| **HP:0000639** | Nystagmus | 7/10 (70%) | FREQUENT |
| **HP:0002066** | Gait ataxia | 6/11 (55%) | FREQUENT |
| **HP:0001260** | Dysarthria | 4/11 (36%) | FREQUENT |
| **HP:0001761** | **Pes cavus** | **3/10 (30%)** | FREQUENT / OCCASIONAL |
| **HP:0002015** | Dysphagia | 3/11 (27%) | FREQUENT / OCCASIONAL |
| **HP:0006852** | Episodic generalized hypotonia | 3/10 (30%) | FREQUENT / OCCASIONAL |
| **HP:0000618** | Blindness | 2/10 (20%) | OCCASIONAL |
| **HP:0001310** | Dysmetria | 2/10 (20%) | OCCASIONAL |
| **HP:0002311** | Incoordination | 2/11 (18%) | OCCASIONAL |
| **HP:0000729** | Autistic behavior | 2/10 (20%) | OCCASIONAL |
| **HP:0001332** | Dystonia | 1/10 (10%) | OCCASIONAL |
| **HP:0001250** | Seizure | 1/10 (10%) | OCCASIONAL |
| **HP:0003477** | Peripheral axonal neuropathy | 1/10 (10%) | OCCASIONAL |
| **HP:0001716** | Wolff-Parkinson-White syndrome | 1/10 (10%) | OCCASIONAL |
| **HP:0000012** | Urinary urgency | 1/10 (10%) | OCCASIONAL |
| HP:0007965 | Undetectable visual evoked potentials | 1/1 | — |
| HP:0002067 | Bradykinesia | 1/1 | — |
| HP:0002172 | Postural instability | 1/1 | — |
| HP:0001269 | Hemiparesis | 1/1 | — |
| HP:0031960 | Arm dystonia | 1/1 | — |
| HP:0004372 | Reduced consciousness | 1/1 | — |
| HP:0001252 | Hypotonia | 1/1 | — |
| HP:0000505 | Visual impairment | 1/1 | — |
| HP:0000365 | Hearing impairment | 1/1 | — |
| HP:0000251 (see note) | — | — | — |
| **HP:0000529** | Progressive visual loss | no freq | — |
| **HP:0000572** | Visual loss | no freq | — |
| **HP:0000408** | Progressive sensorineural hearing impairment | no freq | — |
| **HP:0002078** | Truncal ataxia | no freq | — |
| **HP:0001251** | Ataxia | 1/1 | — |

**Clinical course annotations:** HP:0011463 Childhood onset (6/11), HP:0003593 Infantile onset (3/10), HP:0003621 Juvenile onset (2/10).
**Inheritance:** HP:0000006 Autosomal dominant inheritance.

**⚠️ Critical curation note on the acronym:** *Pes cavus (HP:0001761) is present in only 3/10 (30%) of annotated patients* — the least frequent of the five acronym features. Meanwhile **muscle weakness (HP:0001324)** and **episodic ataxia (HP:0002131)** are at 100% but are *not* in the acronym. The name CAPOS is therefore a historically anchored misnomer regarding relative feature frequency, which is precisely why "CAOS" was proposed (PMID:25895915, PMID:29625811). Consider a `notes` field capturing this.

### 3.2 Phenotypes Organized by Type

#### A. Acute (episodic) manifestations — the fever-triggered decompensation

Per GeneReviews **[P]**: *"CAPOS syndrome presents in infancy or childhood (usually ages 6 months to 5 years) with cerebellar ataxia during or after a fever."* The acute febrile encephalopathy may include **hypotonia, flaccidity, nystagmus, strabismus, dysarthria/anarthria, lethargy, loss of consciousness, and coma.**

Detailed acute phenomenology (PMID:27091223, Maas et al.) **[V]**:
> "The individuals presented here experienced one to three paroxysmal, short-lasting episodes in childhood with cerebellar symptoms and signs, hypotonia, ophthalmoparesis, motor weakness, areflexia, and/or lethargy that were consistently associated with febrile illness."

Severe end of the acute spectrum (PMID:29625811, Hayashida et al.) **[P]**: *"Acute manifestations encompassed unconsciousness, headache, abnormal ocular movements, flaccid paralysis with areflexia, ataxia, dysphagia, and movement disturbances."*

| Acute feature | HPO suggestion | Notes |
|---|---|---|
| Fever-triggered ataxic encephalopathy | HP:0002131 Episodic ataxia + HP:0001298 Encephalopathy | The signature event |
| Reduced consciousness / lethargy → coma | HP:0004372 Reduced consciousness; HP:0001259 Coma | |
| Acute flaccid weakness / hypotonia | HP:0006852 Episodic generalized hypotonia; HP:0001324 Muscle weakness | Can mimic Guillain-Barré / transverse myelitis |
| Ophthalmoparesis / abnormal eye movements | HP:0000602 Ophthalmoplegia; HP:0000639 Nystagmus; HP:0000486 Strabismus | |
| Anarthria/dysarthria; dysphagia | HP:0001260 Dysarthria; HP:0002015 Dysphagia | Brainstem/bulbar involvement |
| Areflexia (acute and persistent) | HP:0001284 Areflexia | |

- **Onset:** infantile to early childhood; **6 months – 5 years** is the canonical window.
- **Severity:** severe during episodes (can require ICU care and be mistaken for acute encephalitis/ADEM).
- **Progression:** **episodic/paroxysmal** with incomplete inter-episode recovery — GeneReviews **[P]**: *"Usually, considerable recovery occurs within days to weeks; however, persistence of some degree of ataxia and other manifestations is typical."*
- **Number of episodes:** typically **1–3** in childhood (PMID:27091223, PMID:28483396 **[V]** — "They usually present one to three episodes").
- **QoL:** catastrophic acutely — loss of acquired motor milestones, temporary total dependence, ICU admission, parental distress; no formal QoL instrument has ever been applied.

#### B. Persistent / progressive neurological manifestations

GeneReviews enumerates the residual features **[P]**: *hypotonia, flaccidity, hyporeflexia, areflexia, pes cavus, dystonia, choreiform movements, abnormal eye movements, progressive optic nerve atrophy with vision loss, progressive sensorineural hearing loss, brief generalized tonic-clonic seizures, dysarthria/anarthria, dysphagia, cognitive dysfunction, and neurobehavioral/psychiatric manifestations.*

| Feature | HPO | Onset | Severity | Course |
|---|---|---|---|---|
| Cerebellar/gait/truncal ataxia | HP:0002066, HP:0002078, HP:0001251 | Post-episode, childhood | Mild→severe, variable | Static-to-slowly-progressive; **can improve** (PMID:31410291) |
| Areflexia | HP:0001284 | Childhood, permanent | — | Static, **non-progressive**, present without demonstrable neuropathy |
| Pes cavus | HP:0001761 | Childhood | Mild-moderate | Slowly progressive skeletal deformity |
| Dystonia, chorea, myoclonus, tremor | HP:0001332, HP:0002072, HP:0001336, HP:0001337 | Variable, post-episode | Variable | Fluctuating (PMID:27091223, PMID:29625811) |
| Dysarthria | HP:0001260 | Childhood | Mild-severe (to anarthria) | Persistent |

#### C. Sensory phenotypes — the discriminating features

**Sensorineural hearing loss — specifically AUDITORY NEUROPATHY (auditory synaptopathy/neuropathy spectrum disorder, ANSD).** This is the highest-value mechanistic phenotype in the entry.

PMID:29305691 (Tranebjærg et al., *Hum Genet* 2018) — the definitive audiological study, **verbatim [V]**:
> "In this retrospective analysis of audiological data, we show for the first time that cochlear outer hair cell activity was preserved as shown by the presence of otoacoustic emissions and cochlear microphonic potentials, but the auditory brainstem responses were grossly abnormal, likely reflecting neural dyssynchrony. Poor speech perception was observed, especially in noise, which was beyond the hearing level obtained in the pure tone audiograms in several of the patients presented here."

and:
> "In conclusion, we demonstrate for the first time evidence for auditory neuropathy in CAPOS syndrome, which may reflect impaired propagation of electrical impulses along the spiral ganglion neurons."

PMID:29184165 (Han et al., *Sci Rep* 2017) **[V]**:
> "This ANSD phenotype was compatible with known expression of ATP1A3 mainly in the synapse between afferent nerve and inner hair cells."
> "Collectively, the de novo ATP1A3 variant can cause postlingual-onset auditory synaptopathy, making this gene a significant contributor to sporadic progressive ANSD and a biomarker ensuring favorable short-term CI outcomes."

**Hearing loss may be the ONLY or FIRST manifestation.** GeneReviews **[P]**: *14 individuals experienced hearing loss "as the first or only manifestation"*, and *"Some individuals with the p.Glu818Lys pathogenic variant manifest only the auditory neuropathy phenotype of CAPOS syndrome."* Confirmed independently in Chinese and Korean ANSD cohorts: PMID:34692702 **[V]** — *"The other two patients (patient 3 and patient 4, who were 8 and 6 years old, respectively) denied any neurological symptoms."*

| Feature | HPO | Details |
|---|---|---|
| Sensorineural hearing impairment | HP:0000407 | 10/10 |
| Progressive SNHL | HP:0000408 | Progressive over years (PMID:34692702, 15-yr follow-up) |
| **Auditory neuropathy** | **HP:0031815 Auditory neuropathy** (verify with OAK) | Present OAEs/CM + absent-abnormal ABR |
| Abnormal ABR | HP:0006958 Abnormal auditory evoked potentials | |
| Speech-in-noise disproportion | no clean HP term | Speech perception worse than PTA predicts |

**Optic atrophy and visual loss.**

| Feature | HPO | Details |
|---|---|---|
| Optic atrophy | HP:0000648 | 11/11 (100%) — the most consistent feature alongside areflexia |
| Progressive visual loss | HP:0000529 | Progressive after episodes |
| Blindness | HP:0000618 | 2/10 (20%) — end-stage |
| Undetectable VEP | HP:0007965 | 1/1 |
| Nystagmus | HP:0000639 | 7/10 |
| Strabismus | HP:0000486 | Reported in acute and chronic phases |

QoL impact of the dual sensory loss is the dominant lifelong burden: combined progressive deafblindness plus ataxia constitutes **acquired deafblindness with motor disability** — education, communication, employment, and independent mobility are all affected. *No CAPOS-specific EQ-5D, SF-36, PROMIS, or disease-specific PRO data exist. This is a real gap.*

#### D. Cognitive, behavioural and psychiatric

- Cognitive dysfunction — HP:0001268 Mental deterioration / HP:0001249 Intellectual disability. PMID:29625811 reports "moderate intellectual disability" post-episodes **[P]**.
- Autistic behaviour — HP:0000729 (2/10). PMID:27276195 **[V]**: *"Social behavioral deficits have been observed in patients diagnosed with alternating hemiplegia of childhood (AHC), rapid-onset dystonia-parkinsonism and CAPOS syndrome."*
- Emotional and behavioural changes — PMID:27091223 **[V]**: *"other possibly related sequelae included dystonia, myoclonus, and emotional and behavioral changes."*

#### E. Cardiac phenotype (under-recognized; safety-critical)

PMID:32913013 (*Neurology* 2020, 110-patient multicenter cohort) **[V]**:
> "Resting ECG abnormalities were found in 52 of 87 (60%) with AHC, 2 of 3 (67%) with CAPOS, and 6 of 9 (67%) with RDP."
> "We found increased prevalence of ECG dynamic abnormalities in all ATP1A3-related syndromes, with a risk of life-threatening cardiac rhythm abnormalities equivalent to that in established cardiac channelopathies (≈3%). Sudden cardiac death due to conduction abnormality emerged as a seizure-related outcome in murine Atp1a3-related disease. ATP1A3-related syndromes are cardiac diseases and neurologic diseases."

Also: **incomplete right bundle branch block** in a CAPOS patient (PMID:29625811) **[P]**; **Wolff-Parkinson-White syndrome** in the HPO annotation set (HP:0001716, 1/10).

**⚠️ CAPOS-specific n = 3. Curate this as ATP1A3-spectrum-level evidence with `explanation` noting the tiny CAPOS denominator.** Suggest HPO: HP:0001695 Cardiac arrest; HP:0011675 Arrhythmia; HP:0012722 Sudden cardiac death; HP:0011710 Bundle branch block; HP:0001716 Wolff-Parkinson-White syndrome.

#### F. Other reported associations (single reports — curate with `frequency` omitted)

- **Hemiplegic migraine** — PMID:26453127 **[V]**: *"This is also the first report showing the co-occurrence of hemiplegic migraine and CAPOS syndrome in a patient with ATP1A3 mutations. Migraine has not been previously documented in ATP1A3 mutation carriers."* HP:0002083 Migraine / HP:0002076 Migraine with aura.
- **Peripheral axonal neuropathy** — HP:0003477 (1/10). Note the tension with the original description's "areflexia (in the absence of a peripheral neuropathy)" (PMID:8733056). PMID:34655904 documented **[V]** *"abnormal EMG showing low amplitude motor responses with acute denervation."* **The origin of areflexia — central vs. peripheral — is a genuine unresolved mechanistic question.** Curate as KNOWLEDGE_GAP.
- **Urinary urgency** — HP:0000012 (1/10).
- **Mild cerebellar atrophy on MRI** — PMID:36484864 **[V]**: *"the brain MRI indicated mild cerebellar atrophy."* HP:0001272 Cerebellar atrophy. Note: MRI is **normal in most** CAPOS patients.

---

## 4. Genetic / Molecular Information

### Causal Gene

| Field | Value |
|---|---|
| Gene symbol | **ATP1A3** |
| Approved name | ATPase Na+/K+ transporting subunit alpha 3 |
| HGNC | **HGNC:801** → dismech CURIE `hgnc:801` |
| Cytogenetic location | **19q13.2** |
| NCBI Gene | 478 |
| Ensembl | ENSG00000105409 |
| UniProt | **P13637** (AT1A3_HUMAN) |
| OMIM (gene) | 182350 |
| MANE Select transcript | **NM_152296.5** (1,013 aa) |

### The Pathogenic Variant

| Field | Value |
|---|---|
| HGVS (coding) | **NM_152296.5:c.2452G>A** |
| HGVS (protein) | **p.(Glu818Lys)** / **p.E818K** |
| Genomic (GRCh38) | chr19:41,970,275 G>A |
| Genomic (GRCh37/hg19) | chr19:42,474,427 G>A |
| dbSNP | rs587777771 |
| ClinVar | VCV000156238 |
| **ClinVar germline classification** | **Pathogenic** (last evaluated 2025-05-25) |
| ClinVar review status | *"criteria provided, multiple submitters, no conflicts"* — 2★ |
| Submissions | 18 SCVs across 6 RCVs |
| Conditions in ClinVar | ATP1A3-related disorder; Cerebellar ataxia-areflexia-pes cavus-optic atrophy-sensorineural hearing loss syndrome; Alternating hemiplegia of childhood 2; Dystonia 12; inborn genetic diseases |
| Variant type | **Missense** (single-nucleotide substitution) |
| Origin | **Germline** — either de novo or inherited. No somatic association. |
| Population frequency | **Absent from population controls.** Demos 2014 **[V]**: *"This mutation was not found in more than 3600 chromosomes from unaffected individuals."* gnomAD could not be queried directly during this pass (JS-rendered); **verify gnomAD v4 allele count before asserting a numeric AF.** Expected: 0 or singleton, consistent with a highly penetrant de novo dominant allele. |

### ⚠️ Transcript-Numbering Hazard

PMID:41235133 (*Neurol Genet* 2025, "Pathogenic Variants in ATP1A3: Why Is There So Much Confusion?") warns **[P]** that sequencing services use **three different mRNA transcripts** for variant numbering, causing misidentification, and recommends *using only the MANE Select transcript (encoding 1,013 amino acids)*. **Always curate CAPOS as NM_152296.5:c.2452G>A p.(Glu818Lys)** and treat any alternate residue numbering in older reports with suspicion. This matters especially because the AHC variant **p.Glu815Lys** sits only 3 residues away.

### Functional Consequence — Detailed Biophysics

The definitive functional characterization is **PMID:30409907** (*J Biol Chem* 2019, "Functional consequences of the CAPOS mutation E818K of Na⁺,K⁺-ATPase"), **verbatim [V]**:

> "We found that these amino acid substitutions reduce the apparent Na⁺ affinity at the cytoplasmic-facing sites of the pump protein and that this effect is more pronounced for the lysine and glutamine substitutions (3-4-fold) than for the alanine substitution. The electrophysiological measurements indicated a more conspicuous, ∼30-fold reduction of apparent Na⁺ affinity for the extracellular-facing sites in the CAPOS mutant, which was related to an accelerated transition between the phosphoenzyme intermediates E1P and E2P. The apparent affinity for K⁺ activation of the ATPase activity was unaffected by these substitutions, suggesting that primarily the Na⁺-specific site III is affected. Furthermore, the apparent affinities for ATP and vanadate were WT-like in E818K, indicating a normal E1-E2 equilibrium of the dephosphoenzyme. Proton-leak currents were not increased in E818K. However, the CAPOS mutation caused a weaker voltage dependence of the pumping rate and a stronger inhibition by cytoplasmic K⁺ than the WT enzyme, which together with the reduced Na⁺ affinity of the cytoplasmic-facing sites precluded proper pump activation under physiological conditions. The functional deficiencies could be traced to the participation of Glu-818 in an intricate hydrogen-bonding/salt-bridge network, connecting it to key residues involved in Na⁺ interaction at site III."

Corroborating structural/electrophysiological data (PMID:29305691) **[V]**:
> "Heterologous expression studies of α3 with the p.Glu818Lys mutation affects sodium binding to, and release from, the sodium-specific site in the pump, the third ion-binding site. Molecular dynamics simulations confirm that the structure of the C-terminal region is affected."

And structural destabilization prediction (PMID:25895915) **[V]**:
> "Whole exome sequencing identified a deleterious heterozygous c.2452 G>A, p.(E818K) variant in the ATP1A3 gene and structural analysis predicted its protein-destabilizing effect."

**Mechanistic classification.** E818K is best described as a **specific loss-of-function of Na⁺-site-III handling** — a *selective, partial, kinetic* LoF, not a null and not a general leak. Two contrasts sharpen this:

- **Not a cation-leak mechanism.** *"Proton-leak currents were not increased in E818K"* (PMID:30409907) **[V]**. Contrast p.Pro775Leu, which **does** leak — PMID:37043503 **[V]**: *"Uniquely among known ATP1A3 variants, P775L causes leakage of sodium ions and protons into the cell… Cation leak provides a molecular explanation for this genotype-phenotype correlation."*
- **Not a simple haploinsufficiency.** Whole-gene *ATP1A3* deletion produces an AHC2-like phenotype, **not** CAPOS — PMID:34421501 **[V]**: *"Our data suggest that the deletion of the ATP1A3 gene is a causative factor of the AHC2 phenotype in the patient."* This is strong evidence that **E818K is not merely LoF**; the CAPOS-specific phenotype must arise from the particular kinetic signature (and/or dominant-negative interference within the α3 population).

Suggested dismech `modifier` values: `DECREASED` on Na⁺-affinity/pump-activity nodes; `INCREASED` on intracellular Na⁺ accumulation nodes.

### Allelic Disorders — The ATP1A3 Spectrum

*ATP1A3* variants produce a **phenotypic continuum**, not clean separate diseases. This is the single most important framing decision for the KB entry.

| Phenotype | Canonical variant(s) | OMIM |
|---|---|---|
| **CAPOS** | **p.Glu818Lys (only)** | 601338 |
| Alternating hemiplegia of childhood 2 (AHC2) | p.Asp801Asn, p.Glu815Lys, p.Gly947Arg | 614820 |
| Rapid-onset dystonia-parkinsonism (RDP/DYT12) | p.Thr613Met, others | 128235 |
| **RECA / FIPWE** (relapsing encephalopathy with cerebellar ataxia / fever-induced paroxysmal weakness and encephalopathy) | **residue 756**: p.Arg756His, p.Arg756Cys, p.Arg756Leu | — |
| Early-infantile epileptic encephalopathy | various | — |
| **Polymicrogyria** | various de novo | — |
| Complex spastic paraplegia / ID | **p.Pro775Leu** | — |
| Cone-rod dystrophy (adCORD) | p.Asp591Val | — |

Key spectrum quotes:
- PMID:33868146 **[V]**: *"Because of this, ATP1A3-disorders are now beginning to be viewed as a phenotypic continuum representing discrete expressions along a broadly heterogeneous clinical spectrum."*
- PMID:26400718 **[V]**: *"Rather than multiple overlapping syndromes, ATP1A3-related disorders might be seen as a phenotypic continuum."*
- PMID:41850905 (*Mov Disord* 2026, n=88) **[P]**: only **25%** met criteria for a single canonical phenotype; 32% canonical-plus; 20% met criteria for multiple canonical phenotypes; **23% fit no canonical category**. Chronic movement disorders in 75% (dystonia 53%); paroxysmal events in 88%.
- PMID:33762331 **[P]**: de novo *ATP1A3* variants cause *"a severe form of polymicrogyria with epilepsy and developmental delay"* — a *"previously unidentified category."*

**However, GeneReviews maintains a genotype-specific exception for E818K [P]:** *"A unique correlation has been reported between the p.Glu818Lys pathogenic variant and its fever-induced ataxia phenotype"* and *"CAPOS syndrome has little clinical overlap with AHC"* — despite p.Glu818Lys being only three residues from the AHC p.Glu815Lys.

**Curation recommendation:** create a dismech **Grouping** `ATP1A3-Related_Disorders` with `grouping_basis: [SHARED_GENE_FAMILY, SHARED_MECHANISM]` and a `NECESSARY` `HAS_GENE` criterion on `hgnc:801`, with CAPOS, AHC2, RDP, and RECA as `members[]` and per-member `differentiating_mechanisms` keyed to residue position and biophysical signature. This is a near-ideal grouping use case.

**Blurred-boundary reports to cite in `differentiating_mechanisms`:** CAPOS+hemiplegic migraine (PMID:26453127); CAPOS/AHC overlap (PMID:25056583, PMID:29625811); CAPOS+dystonia (PMID:32576493); E818K presenting as childhood rapid-onset ataxia without full CAPOS (PMID:29397530); E818K presenting as isolated auditory neuropathy (PMID:29184165, PMID:34692702).

### Modifier Genes

**None identified.** See §2.

### Epigenetics

**No CAPOS-specific epigenetic data.** No DNA-methylation episignature has been reported for *ATP1A3* disorders (in contrast to many chromatinopathies). **Not applicable / genuine gap.**

### Chromosomal Abnormalities

Not a mechanism in CAPOS. The one relevant *ATP1A3* CNV report (PMID:34421501, 88.8 kb 19q13.2 deletion of *RABAC1*, *ARHGEF1*, *ATP1A3*) produced an **AHC2-like**, not CAPOS, phenotype — mechanistically informative (see above) but not a CAPOS cause. Chromosomal microarray has **no diagnostic role** in CAPOS.

---

## 5. Environmental Information

- **Environmental toxins / radiation / pollution / occupational exposure:** **No role.** No toxicant is implicated in causation or triggering. Not applicable.
- **Lifestyle factors:** No dietary, smoking, alcohol, or exercise association established. Missed meals and sleep deprivation are listed among general ATP1A3 stressors to avoid (GeneReviews **[P]**), but with no CAPOS-specific evidence.
- **Infectious agents:** Infections are **triggers, not causes**. Any febrile illness — most commonly common childhood viral infections and URTIs — can precipitate an episode. **No specific pathogen is implicated** and no pathogen taxon should be curated as an etiologic agent. The relevant curation object is the *fever/systemic-inflammatory state*, not the organism.
- **Physiological states:** **Pregnancy and the peripartum period** are a documented trigger (PMID:29090527) — clinically important, since it is modifiable through anticipatory obstetric planning.
- **Thermal:** Fever is central. Whether the operative variable is *temperature per se* or the *metabolic/inflammatory correlates* of fever is unresolved. (In the *Matoub*/E815K AHC mouse, warm-water immersion induced hemiplegia — PMID:34612482 **[P]** — supporting a genuine thermal component in ATP1A3 biology generally.)

---

## 6. Mechanism / Pathophysiology

### 6.1 The Causal Chain (dismech pathograph skeleton)

```
[1] MOLECULAR — Heterozygous ATP1A3 c.2452G>A p.(Glu818Lys)
      ↓ (disrupts the H-bond/salt-bridge network anchoring Na+ site III)
[2] MOLECULAR — Impaired Na+ binding/release at Na+-specific site III of Na+/K+-ATPase α3
      • ~3-4x reduced apparent cytoplasmic Na+ affinity
      • ~30x reduced apparent extracellular Na+ affinity
      • accelerated E1P → E2P transition
      • weaker voltage dependence of pumping rate
      • stronger inhibition by cytoplasmic K+
      • K+ affinity, ATP affinity, E1-E2 equilibrium all normal; NO cation leak
      ↓
[3] MOLECULAR/CELLULAR — Failure of α3 pump activation under physiological conditions
      ↓
[4] CELLULAR — Impaired restoration of the transmembrane Na+/K+ gradient after
      high-frequency neuronal activity (α3 is the "rescue pump")
      ↓
[5] CELLULAR — Intracellular Na+ accumulation; depolarized/unstable resting potential;
      impaired repolarization; impaired Na+-gradient-dependent secondary transport
      (neurotransmitter reuptake, Na+/Ca2+ exchange → Ca2+ dysregulation)
      ↓
[6] CELLULAR — Neuronal excitability failure / conduction dyssynchrony, most severe
      in the highest-firing-rate, highest-Na+-load neurons
      ↓  ↘ (acute arm, gated by FEVER)              ↘ (chronic arm)
[7a] TISSUE/ORGANISM — ACUTE: fever raises metabolic and firing demand beyond the
      marginal pump's capacity → acute cerebellar/brainstem network failure
      → ataxic encephalopathy, flaccid weakness, ophthalmoparesis, coma
      → cortico-subcortical cerebral blood flow imbalance (PMID:30904181)
      ↓
[8a] Partial recovery over days-weeks with a RESIDUAL FIXED DEFICIT (stepwise accrual)

[7b] TISSUE — CHRONIC: sustained metabolic/ionic stress in long, high-firing,
      metabolically demanding projection neurons
      → spiral ganglion neuron / IHC-ribbon-synapse dysfunction → AUDITORY NEUROPATHY
      → retinal ganglion cell axon degeneration → OPTIC ATROPHY
      → cerebellar Purkinje/network dysfunction ± atrophy → PERSISTENT ATAXIA
      → reflex-arc failure → AREFLEXIA
      → chronic denervation of intrinsic foot muscles → PES CAVUS
      → cardiac conduction-system involvement → ECG abnormalities, arrhythmia risk
```

**Upstream vs downstream.** [1]–[3] are strictly upstream and genotype-determined. [4]–[6] are the shared cellular hub. **[7a] is environmentally gated** — this is the G×E node, and the correct attachment point for a `mechanistic_hypotheses` group. [7b] is the slow, cumulative, tissue-selective arm and explains why the *sensory* features progress even between episodes.

### 6.2 Molecular Pathways

- **Na⁺/K⁺-ATPase (P-type ATPase) ion-transport cycle** (Post-Albers E1/E1P/E2P/E2 cycle). Not a KEGG/Reactome "signaling cascade" in the canonical sense — this is a primary active-transport pathway. Reactome: "Ion transport by P-type ATPases" (R-HSA-936837); KEGG: hsa04260/hsa04261 (cardiac muscle contraction / adrenergic signaling in cardiomyocytes) include *ATP1A3*.
- **Brain energy metabolism.** The Na⁺/K⁺-ATPase is the largest single consumer of neuronal ATP; α3 dysfunction produces a functional *energy-failure* phenotype. PMID:26400718 **[V]**: *"The phenotype of this patient, resembling mitochondrial oxidative phosphorylation defects, emphasizes the possible role of brain energy deficiency in patients with ATP1A3 mutations."*
- **Glutamatergic signaling and the NKA-as-receptor role.** PMID:27313535 **[V]**: *"Data indicates that the central glutamatergic system is affected by mutations in the α2 isoform, however further investigations are required to establish a connection to mutations in the α3 isoform, especially given the diagnostic confusion and overlap with glutamate transporter disease."* The NKA also acts as a signaling receptor interacting with NMDA receptors and via NOS/cGMP/PKG.
- **Calcium homeostasis (secondary).** Reduced Na⁺ gradient impairs NCX-mediated Ca²⁺ extrusion. Demonstrated for another ATP1A3 variant, PMID:42116168 **[P]**: patient-derived neurons showed *"significantly prolonged calcium transient decay times."* **Not yet shown for E818K** — an explicit gap.
- **Neuronal autosis (autophagy-dependent cell death).** PMID:38796484 **[V]**: *"autosis is not dependent on the ubiquitous subunit ATP1a1 in neurons, as in dividing cell types, but on the neuronal specific ATP1a3 subunit."* Speculative relevance to CAPOS neurodegeneration; curate as EMERGING at most.

**GO biological process suggestions:**

| GO ID | Label | Status |
|---|---|---|
| **GO:0005391** | P-type sodium:potassium-exchanging transporter activity | [OLS-verified] — molecular function |
| **GO:0005890** | sodium:potassium-exchanging ATPase complex | [OLS-verified] — cellular component |
| **GO:0035725** | sodium ion transmembrane transport | [OLS-verified] |
| **GO:0006883** | intracellular sodium ion homeostasis | [OLS-verified] |
| **GO:0042391** | regulation of membrane potential | [OLS-verified] |
| GO:0030007 | intracellular potassium ion homeostasis | verify |
| GO:0086009 | membrane repolarization | verify |
| GO:0007605 | sensory perception of sound | verify |
| GO:0007601 | visual perception | verify |
| GO:0006754 | ATP biosynthetic process | verify |
| GO:0006816 | calcium ion transport | verify |
| GO:0098662 | inorganic cation transmembrane transport | verify |

Use `modifier: DECREASED` on GO:0005391 and GO:0035725; `modifier: INCREASED` on the intracellular-Na⁺ node.

### 6.3 Cellular Processes

The unifying cell-biological principle is **α3 as the neuronal "rescue pump."** PMID:27378932 **[V]**:
> "The α3 isoform has approximately four-fold lower Na⁺ affinity compared to α1 and is specifically required for rapid restoration of large transient increases in [Na⁺]i. Conditions associated with α3 deficiency are therefore likely aggravated by suprathreshold neuronal activity. The α3 isoform been suggested to support re-uptake of neurotransmitters."

and:
> "The α1 isoform is ubiquitously expressed in the adult central nervous system (CNS) whereas α2 primarily is expressed in astrocytes and α3 in neurons."

Corroborated by PMID:33868146 **[V]**: *"The α3 isoform is required as a rescue pump, after repeated action potentials, with a distribution predominantly in neurons of the central nervous system."*

**The key insight for selectivity:** because α3 already has ~4-fold *lower* Na⁺ affinity than α1 by design, an *additional* 3–4-fold reduction in cytoplasmic Na⁺ affinity is catastrophic specifically in cells that depend on rapid high-Na⁺-load clearance — i.e., **high-firing-rate neurons under thermal/metabolic stress**. This is the mechanistic explanation for both the fever-dependence and the tissue selectivity.

Cellular processes to curate: impaired membrane repolarization; impaired neurotransmitter reuptake; disrupted Na⁺-coupled secondary transport; Ca²⁺ dysregulation; energy-failure/metabolic stress; neural conduction dyssynchrony; axonal degeneration; possibly autosis.

### 6.4 Protein Dysfunction

- **Protein:** UniProt **P13637**, Na⁺/K⁺-ATPase subunit α-3, 1,013 aa, 10-TM P-type ATPase; functions as a heteromeric α-β(-FXYD/γ) complex at the plasma membrane.
- **Residue Glu818:** in transmembrane helix M6/M6-M7 region, part of a hydrogen-bonding/salt-bridge network coordinating the **Na⁺-specific ion binding site III** — the site that distinguishes the 3Na⁺-out/2K⁺-in stoichiometry.
- **Mechanism class:** **selective kinetic loss-of-function** at Na⁺ site III, with predicted **local structural destabilization of the C-terminal region** (PMID:29305691, PMID:25895915). **Not** misfolding-with-aggregation; **not** cation leak; **not** null. Whether it exerts a **dominant-negative** effect on the α3 pool (as opposed to simple 50% functional dosage) is unresolved and is a stated gap — noting that whole-gene deletion gives AHC2 rather than CAPOS.
- **Expression level:** studies on other AHC/RDP variants found no expression difference (PMID:27634470 **[V]**: *"The expression of the mutant form (R756C) of ATP1A3 did not differ markedly from that of the wild-type and D801N proteins"*); E818K-specific expression data were not located.
- Structural resources: AlphaFold P13637; PDB structures of pig/shark Na⁺/K⁺-ATPase (e.g. 2ZXE, 3B8E) used as homology templates in the CAPOS modelling studies.

### 6.5 Metabolic Changes

No primary metabolic defect. The relevant abnormality is **secondary neuronal energy insufficiency**: the α3 pump's ATP demand cannot be met productively because pump activation itself is impaired. Clinically this produces a **mitochondrial-disease mimic** — PMID:26400718 **[V]** (see above) — and this mimicry is the single most common source of diagnostic delay. **Lactate/pyruvate, CSF lactate, respiratory-chain enzymology and mtDNA analysis are characteristically normal or non-diagnostic in CAPOS.** No metabolomic or lipidomic signature has been described.

### 6.6 Immune System Involvement

Not a primary immune disease. Two threads deserve curation as *hypotheses*, both explicitly framed as questions:

1. **Is fever's effect inflammatory rather than thermal?** PMID:36339296 asks exactly this in its title: *"ATP1A3-Related Relapsing Encephalopathy with Cerebellar Ataxia (RECA): A Genetic Disorder with an Inflammatory Basis?"* (abstract not retrieved; **fetch before citing**).
2. **Autoantibody cross-reference.** PMID:25809299 identified neuronal Na⁺/K⁺-ATPase (α3) as a **paraneoplastic autoantibody target** in a patient with colon adenocarcinoma and a cerebellar syndrome **[P]**. This is a *phenocopy by a different route* (autoimmune vs. genetic) hitting the same protein — an elegant convergent-mechanism data point, and a differential-diagnosis item for adult-onset cerebellar syndromes.

There is no evidence for autoimmunity, immunodeficiency, or chronic inflammation *as a mechanism of CAPOS itself*. Steroids/IVIG are frequently given empirically during acute episodes (mistaken for ADEM/encephalitis) with no demonstrated benefit.

### 6.7 Tissue Damage Mechanisms

- **Excitotoxicity / ionic-osmotic stress** during acute decompensation (hypothesized).
- **Cerebral perfusion dysregulation** — the best direct human *in vivo* mechanistic data in CAPOS. PMID:30904181 (serial SPECT in a CAPOS boy) **[V]**: *"The serial CBF-SPECT findings using statistical methods showed progressive hyperperfusion in the frontal lobes, basal ganglia and thalamus, and hypoperfusion in the occipital and temporal lobes during the acute and subacute phases. Thereafter, the dynamic changes of CBF improved in the chronic but hypoperfusion in thalamus appeared to the chronic phase."* and *"The abnormal cortico-subcortical CBF may contribute to an acute encephalopathy-like condition in the acute stage of CAPOS syndrome."*
- **Chronic axonal degeneration** of long/high-demand projections — optic nerve (RGC axons) and spiral ganglion neurons.
- **Cerebellar atrophy** in a minority (PMID:36484864).
- **Notably absent:** fibrosis, necrosis, ischemia-as-primary, and inflammation. **No neuropathological/autopsy study of a CAPOS patient has been published** — a significant gap.

### 6.8 Biochemical Abnormalities

The core defect: **deficient P-type sodium:potassium-exchanging transporter activity (GO:0005391) restricted to the α3 isoform**, arising from impaired Na⁺ site-III occupancy. Quantitatively (PMID:30409907): ~3–4× reduced cytoplasmic apparent Na⁺ affinity; ~30× reduced extracellular apparent Na⁺ affinity; accelerated E1P→E2P; K⁺, ATP, vanadate affinities WT-like; no increased proton leak; weaker voltage dependence; enhanced cytoplasmic-K⁺ inhibition.

CHEBI entities for the pathograph: **CHEBI:29101** sodium(1+); **CHEBI:29103** potassium(1+); **CHEBI:15422** ATP; **CHEBI:29108** calcium(2+) (verify each with OAK).

### 6.9 Epigenetic Changes

None described. Not applicable.

### 6.10 Molecular Profiling

**All four omics categories are essentially empty for CAPOS.** Specifically:

- **Transcriptomics:** no CAPOS patient-derived transcriptomic study. GTEx shows *ATP1A3* is brain-enriched (highest in cerebellum, cortex, basal ganglia) — useful as background expression evidence but not disease-state data.
- **Proteomics:** none. Human Protein Atlas confirms neuronal/brain-restricted ATP1A3 protein distribution.
- **Metabolomics / lipidomics:** none.
- **Single-cell / spatial transcriptomics:** none for CAPOS. Allen Brain Atlas and Human Cell Atlas data confirm *ATP1A3* enrichment in neurons (vs. astrocytic *ATP1A2*) — the cell-type-selectivity evidence base.
- **Functional genomics (CRISPR/RNAi screens):** no CAPOS-directed screen. DepMap is uninformative (neuronal, non-cancer gene).
- **Multi-omics integration:** none.

**This is the largest single evidence gap in the disease.** Curate as `discussions: kind: KNOWLEDGE_GAP` with `proposed_experiments` including: patient-derived iPSC → cerebellar/retinal-ganglion/inner-ear-organoid differentiation with paired scRNA-seq and electrophysiology; isogenic E818K knock-in iPSC lines. (Note the MorPhiC framing in CLAUDE.md — *ATP1A3* is not a listed MorPhiC anchor gene, so no MorPhiC-derived cellular phenotypes are available.)

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary — nervous system (UBERON:0001016).** CAPOS is a pure neurological disorder; no primary involvement of liver, kidney, lung, gut, or endocrine organs.

| Structure | UBERON | Involvement |
|---|---|---|
| **Cerebellum** | UBERON:0002037 | Ataxia (episodic + persistent); mild atrophy in a minority |
| **Optic nerve / cranial nerve II** | **UBERON:0000941** [OLS-verified, label "cranial nerve II"] | Progressive optic atrophy — 100% |
| **Cochlea / spiral ganglion** | **UBERON:0001844** cochlea [OLS-verified]; **UBERON:0002227** spiral organ of cochlea [OLS-verified] | Auditory neuropathy — 100% |
| **Vestibulocochlear nerve** | UBERON:0001648 (verify) | Cochlear-nerve conduction dyssynchrony |
| **Brainstem** | UBERON:0002298 (verify) | Acute brainstem dysfunction: ophthalmoparesis, dysphagia, altered consciousness (PMID:34464766) |
| **Basal ganglia** | UBERON:0002420 (verify) | Dystonia/chorea; SPECT hyperperfusion (PMID:30904181) |
| **Thalamus** | UBERON:0001897 (verify) | SPECT hyper- then hypo-perfusion (PMID:30904181) |
| **Cerebral cortex** (frontal, occipital, temporal) | UBERON:0000956 (verify) | Regional CBF imbalance; cognitive/behavioural sequelae |
| **Retina** | UBERON:0000966 (verify) | RGC/RNFL loss upstream of optic atrophy |
| **Spinal cord / reflex arc** | UBERON:0002240 (verify) | Areflexia |
| **Peripheral nerve** | UBERON:0001021 (verify) | Variable — axonal neuropathy in a minority (contested) |

**Secondary organ involvement:**
- **Heart (UBERON:0000948)** — cardiac conduction system; ECG abnormalities in 2/3 CAPOS patients studied; arrhythmia/SCD risk ≈3% across the ATP1A3 spectrum (PMID:32913013). Mechanism plausibly direct (α3 expression in cardiac conduction tissue) rather than truly "secondary."
- **Foot skeleton (UBERON:0002387)** — pes cavus as a secondary neuro-orthopaedic deformity.
- **Musculoskeletal** — secondary contractures, scoliosis from chronic ataxia/weakness.

**Body systems:** nervous (central, peripheral, autonomic), **special sense organs (visual + auditory — the discriminating pair)**, cardiovascular (conduction), musculoskeletal (secondary).

### Tissue and Cell Level

**Tissue types:** nervous tissue (neurons + their axons) predominantly; sensory neuroepithelium of the cochlea; retinal neural tissue. Muscle, connective tissue, and epithelium are **not primarily affected**.

**Cell populations (Cell Ontology):**

| CL ID | Label | Role |
|---|---|---|
| **CL:0000540** | neuron | The α3-expressing cell class — the fundamental unit of disease |
| **CL:0011113** | **spiral ganglion neuron** [OLS-verified] | **Primary site of auditory neuropathy** — impaired impulse propagation (PMID:29305691) |
| CL:4023115 / CL:4023116 | type 1 / type 2 spiral ganglion neuron [OLS-verified] | Type 1 SGNs (95% of afferents, IHC-innervating) are the relevant subtype |
| **CL:0000589** | **cochlear inner hair cell** [OLS-verified] | IHC–afferent ribbon synapse; PMID:29184165 **[V]**: *"the synapse between afferent nerve and inner hair cells"* |
| **CL:0000601** | cochlear outer hair cell [OLS-verified] | **SPARED** — this is diagnostically decisive (preserved OAEs/CM). Curate with an explicit "spared" note. |
| **CL:0000121** | **Purkinje cell** [OLS-verified] | Cerebellar output neuron; presumed but **not histologically demonstrated** in CAPOS |
| CL:0000740 | retinal ganglion cell (verify) | Optic atrophy substrate |
| CL:0000120 | granule cell (verify) | Cerebellar granule cells (high-firing, α3-rich) |
| CL:0000598 | pyramidal neuron (verify) | Cortical involvement |
| CL:0000127 | astrocyte (verify) | Express α2 (*ATP1A2*), **not** α3 — relevant as a *contrast* cell, not an affected one |
| CL:0000108 | cholinergic neuron / motor neuron (verify) | Reflex arc, weakness |

**Curation tip:** the **preserved OHC / affected SGN** dissociation is the single most information-rich cell-level statement in the entry and directly supports the "post-synaptic / neural, not cochlear-sensory" mechanistic claim.

### Subcellular Level

| GO CC | Label | Relevance |
|---|---|---|
| **GO:0005890** | sodium:potassium-exchanging ATPase complex [OLS-verified] | The dysfunctional machine |
| GO:0005886 | plasma membrane (verify) | Pump localization |
| GO:0043005 | neuron projection (verify) | Axonal/dendritic pump distribution |
| GO:0044304 | main axon (verify) | Nodal/internodal α3 for impulse propagation |
| GO:0045202 | synapse (verify) | Ribbon-synapse / afferent-terminal region |
| GO:0098793 | presynapse (verify) | IHC ribbon synapse |
| GO:0005739 | mitochondrion (verify) | ATP supply — *secondary*, not the primary compartment; important to state explicitly given the mitochondrial-mimic pitfall |

### Localization and Lateralization

- **Bilateral and largely symmetric** for the chronic features: bilateral optic atrophy, bilateral SNHL, midline/appendicular cerebellar signs, symmetric areflexia, bilateral pes cavus.
- **Acute episodes may be asymmetric.** PMID:34761051 **[V]** notes across the ATP1A3 spectrum: *"Three common features were a sudden onset, asymmetrical neurological symptoms, as well as the presence of triggering factors."* Hemiparesis (HP:0001269) is annotated in the CAPOS HPO set (1/1), and hemiplegic migraine has been reported (PMID:26453127).
- Suggested descriptor: `laterality: BILATERAL` for chronic sensory/cerebellar features; note asymmetry as a possible acute feature.

---

## 8. Temporal Development

### Onset

- **Typical age:** **6 months to 5 years** (GeneReviews **[P]**). HPO clinical-course annotations: childhood onset 6/11, infantile onset 3/10, juvenile onset 2/10.
- **Earliest reported:** ~7 months (PMID:30904181 — episode at 7 months; PMID:29625811 — 7–8 months).
- **Onset pattern:** **ACUTE / paroxysmal.** The disease announces itself as an abrupt neurological catastrophe during a febrile illness in a previously normal child, not as insidious developmental delay. This is the crucial diagnostic signature.
- **Important exception — pre-episode and non-episode presentations:** PMID:28483396 documented a sibling who *"developed generalized areflexia and mild instability without an acute episode"* and a mother previously diagnosed only with SNHL and optic atrophy **[V]**; the paper is titled *"Early Diagnosis of CAPOS Syndrome Before Acute-Onset Ataxia."* And in ANSD cohorts, isolated hearing loss can be the sole and first presentation, sometimes with **teenage onset** (PMID:29184165, PMID:34692702).
- **Adult-onset first episodes** occur but are rare (PMID:29625811 — an episode at 37 years, in a patient with prior childhood episodes; PMID:26400718 — the RECA patient presented at 34).

Suggested `OnsetDescriptor`: `onset_category: INFANTILE_ONSET` / `CHILDHOOD_ONSET` with a `notes` field on late/attenuated presentations. HPO onset terms: HP:0003593 Infantile onset, HP:0011463 Childhood onset, HP:0003621 Juvenile onset.

### Progression

**Stage model (proposed for curation as `progression`):**

| Stage | Description |
|---|---|
| **0. Pre-symptomatic carrier** | Genotype-positive, no/minimal signs. May show only areflexia or mild instability (PMID:28483396). Fully penetrant carriers may go undiagnosed for decades — PMID:34655904 **[V]**: *"his symptomatic mother went undiagnosed for thirty years until his diagnosis."* |
| **1. Acute decompensation** | Fever-triggered ataxic encephalopathy ± flaccid weakness, ophthalmoparesis, reduced consciousness. Days. |
| **2. Subacute recovery** | Considerable but **incomplete** recovery over days–weeks. PMID:28483396 **[V]**: *"The acute symptoms improve within days, but most patients show slow progression afterward."* |
| **3. Residual/stepwise-accrual phase** | Fixed ataxia, areflexia; each subsequent episode (typically 1–3 total) adds deficit. |
| **4. Chronic progressive sensory phase** | Optic atrophy and SNHL **progress independently of episodes**, over years-to-decades. Pes cavus develops. |
| **5. Late/stable adult phase** | Variable. Many stabilize; some improve motorically. |

**Progression rate:** slow. **Course pattern:** **episodic-with-residuum, superimposed on a slowly progressive sensory neurodegeneration** — a hybrid pattern that does not map cleanly onto a single enum value. Recommend `RELAPSING` or `PROGRESSIVE` at the disease level with per-phenotype `clinical_course` qualifiers: `PROGRESSIVE` on optic atrophy and SNHL; `EPISODIC`/`RECURRENT` on ataxic encephalopathy; `STABLE` on areflexia.

**Duration:** **chronic, lifelong.** Not self-limited.

### Patterns

- **Remission:** No true remission. **Partial spontaneous recovery** after each acute episode is the rule. A genuinely encouraging outlier — PMID:31410291 **[V]**: *"Previous reports suggest a gradual progression of the disease after the initial episodes, while this patient showed a good outcome with improvement of motor skills from adolescence long after the last deterioration episode."*
- **Treatment-induced episode suppression:** anecdotally with acetazolamide — PMID:27091223 **[V]**: *"After initiation of acetazolamide in two patients, no further episodes occurred."* But contradicted in another cohort — PMID:36484864 **[V]**: *"No fluctuation was noted after using Acetazolamide."* (Note: that sentence is ambiguous in the original and should be read in full context before curation.)
- **Critical periods / windows of vulnerability:**
  1. **Ages 6 mo – 5 yr** — the window of maximal episode risk. Antipyretic vigilance matters most here.
  2. **Each febrile illness** is a discrete vulnerability window throughout life.
  3. **Pregnancy and the peripartum period** in affected women (PMID:29090527).
  4. **The pre-first-episode window** is the key *opportunity* window: PMID:28483396's whole point is that identifying at-risk relatives before their first episode enables anticipatory management.
  5. **Post-diagnosis hearing/vision windows** for cochlear implantation and low-vision/educational intervention.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence: not established.** Orphanet does not publish a numeric prevalence class for ORPHA:1171 that could be retrieved in this pass. For dismech `Prevalence`, use:
  - `measure_type: CASES_IN_LITERATURE`
  - `prevalence_class: ULTRA_RARE`
  - `rate_per_100000`: **omit** (no defensible estimate)
  - `notes`: cumulative reported cases (see below)
- **Cumulative reported cases (the only real denominator):**
  | Year | Count | Source |
  |---|---|---|
  | 1996 | 3 (1 family) | PMID:8733056 |
  | 2014 | ~10 (3 families) | PMID:24468074 |
  | 2016 | "seventh and eighth family identified worldwide" | PMID:27091223 **[V]** |
  | 2017 | 22 reported; 25 with the new Spanish family | PMID:28483396 **[V]**: *"a rare disease that has been reported in 22 patients so far"* … *"Only 25 Individuals with CAPOS syndrome have been reported, including our family."* |
  | 2018 | 18 genetically confirmed patients from 11 families in one series (10 previously unreported) | PMID:29305691 **[V]** |
  | current | **53 individuals from 40 families** | GeneReviews (PMID:20301294) **[P]** |
- **Incidence:** unknown. Cannot be estimated.
- **Under-ascertainment is near-certain and directional.** Two independent reasons: (a) PMID:30904181 **[V]** — *"CAPOS syndrome is not often reported, and is possibly an under-recognized syndrome in clinically mild cases"*; (b) systematic discovery of E818K in **sporadic progressive auditory neuropathy** cohorts without neurological features (PMID:29184165 found 2/106 sporadic progressive hearing losses; PMID:34692702 found 4 AN patients with E818K, 2 with no neurological symptoms). **CAPOS is very likely substantially more common than 53 cases**, hidden inside the ANSD population.

### Genetic Etiology Parameters

| Parameter | Value | Evidence |
|---|---|---|
| **Inheritance pattern** | **Autosomal dominant** (HP:0000006) | PMID:24468074, PMID:25895915 **[V]**: *"a unique inherited autosomal dominant neurologic syndrome"* |
| **De novo rate** | **~50%** | GeneReviews **[P]**: *"About half of individuals reported to date with CAPOS syndrome (53 individuals from 40 families)…have an apparently de novo pathogenic variant"* |
| **Familial rate** | **~50%**; >50% of case *reports* are multiplex families | GeneReviews **[P]**: *"more than half of CAPOS syndrome case reports include families with more than one affected member"* |
| **Penetrance** | **Complete / no evidence of reduced penetrance** | GeneReviews **[P]**: *"There is no evidence of reduced penetrance in the families/individuals reported to date."* ⚠️ Caveat: penetrance for *"some manifestation"* is complete; penetrance for the *full pentad* is clearly incomplete, given isolated-ANSD carriers. Curate this distinction explicitly. |
| **Expressivity** | **Highly variable, including intrafamilial** | PMID:26453127 **[V]**: *"The symptoms were triggered by fever and varied in severity in family members"*; PMID:28483396 (three relatives, three different presentations) |
| **Recurrence risk** | 50% per child of an affected parent | GeneReviews **[P]** |
| **Genetic anticipation** | **None.** Not a repeat-expansion disorder. Not applicable. | — |
| **Germline mosaicism** | **Documented in ATP1A3 generally; not yet for E818K specifically** | PMID:27726050 **[V]**: *"Both families displayed parental germline mosaicism… To our knowledge, mosaicism has not previously been reported in ATP1A3-related disorders. This report, therefore, provides evidence that germline mosaicism for ATP1A3 mutations is a likely explanation for familial recurrence and should be considered during recurrence risk counseling."* **⚠️ Counselling-critical: the recurrence risk for apparently unaffected parents of a de novo case is low but NOT zero.** |
| **Founder effect** | **None.** | Multi-ethnic, unrelated pedigrees worldwide — the recurrence reflects a mutational hotspot, not shared ancestry. PMID:26453127 **[V]**: *"This study confirms that the specific c.2452G>A mutation in the ATP1A3 gene is associated with the CAPOS syndrome in pedigrees of different ethnic backgrounds."* PMID:34692702 **[V]**: *"Our study confirms that p.E818K in the ATP1A3 gene is a multiethnic cause of AN."* |
| **Consanguinity** | **No role** — dominant disorder. Not applicable. |
| **Carrier frequency** | **Not applicable** (dominant, fully penetrant, essentially absent from controls). "Carriers" = affected individuals. |

### Population Demographics

- **Affected populations:** no ethnic predilection. Reported in: **UK** (PMID:8733056), **Canada** (PMID:24468074), **Israel** (PMID:25895915), **Serbia/SE Europe** (PMID:26453127), **Netherlands** (PMID:27091223), **Spain** (PMID:28483396 — *"the first time a Spanish family has been described"* **[V]**), **USA** (PMID:29090527 — *"the first ascertained in the United States"* **[V]**), **Korea** (PMID:29184165 — *"the first reported CAPOS allele in Koreans"* **[V]**), **Japan** (PMID:29625811, PMID:30904181), **Norway** (PMID:31410291 — *"the first Norwegian patient reported"* **[V]**), **China** (PMID:32135597, PMID:34692702, PMID:36484864, PMID:38297853), **Denmark, Sweden, Germany** (PMID:29305691), **Middle East / Turkey** (PMID:41480049).
- **Geographic distribution:** worldwide; the apparent European/East Asian concentration reflects **genomic-medicine access**, not biology.
- **Variant geography:** the *same single variant* everywhere — genuinely notable, and consistent with a recurrent de novo hypermutable CpG-adjacent site rather than any founder haplotype. (A formal haplotype analysis across pedigrees appears never to have been published — a nice small gap.)
- **Sex ratio:** no established bias; ~1:1 expected for an autosomal dominant. Females carry the additional pregnancy-related trigger. PMID:38243045 reported 14 F : 12 M across a mixed ATP1A3 cohort **[V]** and noted *"higher females prevalence of atypical presentation"* — ATP1A3-general, not CAPOS-specific, and likely ascertainment noise at that n.
- **Age distribution:** bimodal in presentation — a large early-childhood peak (acute episodes) and a long tail of adults diagnosed retrospectively after a child's diagnosis (PMID:34655904, PMID:28483396) or via ANSD workup (PMID:29184165).

---

## 10. Diagnostics

### Clinical Tests

**Laboratory tests (all characteristically NORMAL — their normality is diagnostically informative):**
- Routine CSF (cell count, protein, glucose), serum/CSF lactate and pyruvate, plasma amino acids, urine organic acids, acylcarnitines, ammonia, CK, very-long-chain fatty acids, respiratory-chain enzymology, mtDNA. PMID:8733056 **[V]**: *"Extensive neurological investigations have been normal."* PMID:34464766 **[V]**: *"These cases highlight ATP1A3-related disorders as a possible cause of acute brainstem dysfunction with normal ancillary testing."*
- PMID:30862413 **[V]**: *"Severe recurrent neurological decompensation episodes triggered by fever, without any metabolic cause, should lead to the sequencing of ATP1A3."*

**Biomarkers:** **None.** There is no biochemical, protein, or imaging biomarker for CAPOS. The genotype is the biomarker. *(An interesting exception in framing: PMID:29184165 **[V]** calls the variant itself a biomarker — "a biomarker ensuring favorable short-term CI outcomes.")*

**Imaging:**
- **Brain MRI:** typically **normal**, both acutely and chronically (PMID:31410291, PMID:36484864 for other ATP1A3 phenotypes). Mild **cerebellar atrophy** in a minority (PMID:36484864). MRI's role is to *exclude* ADEM, encephalitis, stroke, and posterior-fossa lesions.
- **SPECT (research/selected):** dynamic cortico-subcortical CBF imbalance (PMID:30904181) — the only imaging modality shown to be abnormal in the acute phase.
- **OCT (retinal nerve fibre layer):** clinically indicated to quantify optic atrophy; specific CAPOS OCT/RNFL datasets were not retrieved in this pass.

**Functional / electrophysiological tests — the diagnostic core:**

| Test | Finding | Evidence |
|---|---|---|
| **Otoacoustic emissions (OAE)** | **PRESENT / preserved** | PMID:29305691 **[V]** |
| **Cochlear microphonic (CM)** | **PRESENT / preserved** | PMID:29305691 **[V]** |
| **Auditory brainstem response (ABR)** | **Grossly abnormal or absent** | PMID:29305691 **[V]**: *"the auditory brainstem responses were grossly abnormal, likely reflecting neural dyssynchrony"* |
| **Pure-tone audiometry (PTA)** | Variable, progressive; **underestimates functional disability** | PMID:29305691 **[V]**: speech perception *"was beyond the hearing level obtained in the pure tone audiograms"* |
| **Speech audiometry, esp. in noise** | Disproportionately poor | PMID:29305691 **[V]** |
| **Visual evoked potentials (VEP)** | Abnormal to undetectable (HP:0007965) | HPO annotation |
| **EEG** | Non-specific; may show slowing | PMID:38243045 **[V]**: *"EEG and MRI were non-specific"* |
| **ECG (12-lead) ± Holter** | Abnormal in 2/3 CAPOS patients; dynamic changes | PMID:32913013 **[V]** |
| **Echocardiography** | **Normal** | PMID:32913013 **[V]**: *"Echocardiography was normal."* |
| **EMG / nerve conduction** | Usually normal; occasionally abnormal | PMID:34655904 **[V]**: *"abnormal EMG showing low amplitude motor responses with acute denervation"* |

> **The OAE-present / CM-present / ABR-absent triad is the pathognomonic non-genetic finding in CAPOS.** It defines auditory neuropathy, immediately excludes cochlear (sensory) hearing loss, and is the single most actionable diagnostic clue in a child with fever-triggered ataxia plus deafness.

**Biopsy / pathology:** **No role.** Muscle and nerve biopsy are unrevealing and should be avoided; they are often performed during the mitochondrial-mimic workup. **No autopsy neuropathology has been published** — see §6.7.

### Genetic Testing

**Recommended approach (in order of yield-per-cost):**

1. **Targeted single-variant / single-gene *ATP1A3* sequencing** — the highest-yield first-line test when the phenotype is recognized, because CAPOS is a **single-variant disease**. PMID:27091223 **[V]**: *"Targeted sequencing of the ATP1A3 gene is recommended in children exhibiting paroxysmal, fever-induced ataxia and in adults with a more or less stationary or slowly progressive cerebellar syndrome since childhood accompanied by mixed combinations of areflexia, pes cavus, profound visual impairment, and/or sensorineural hearing loss."* Also PMID:29090527 **[V]**: *"Targeted sequencing of ATP1A3 should be considered in any patient presenting with cerebellar ataxia triggered by febrile illness, or pregnancy and delivery."*
2. **Multigene panels** — *ATP1A3* is (or should be) on: hereditary ataxia panels, episodic ataxia panels, epileptic-encephalopathy panels, **non-syndromic + syndromic hearing loss / auditory neuropathy panels**, movement-disorder panels, optic-atrophy panels. Note the ANSD-panel route is how "isolated hearing loss" CAPOS is found.
3. **WES / WGS** — how the disease was solved (PMID:24468074, PMID:25895915) and the appropriate route for unrecognized/atypical presentations. **Trio WES** is preferred to establish de-novo status. PMID:29396171 **[V]**: *"The authors recommend extending ATP1A3 gene analysis to children exhibiting channelopathy-resembling episodes and those with early-onset, fever-associated encephalopathy."* PMID:34761051 **[V]**: *"the authors argue to perform exome sequencing in an early stage."*
4. **Parental Sanger testing** — mandatory for counselling (de novo vs. inherited; mosaicism).

**Tests with NO role in CAPOS:** chromosomal microarray (CMA), karyotype, FISH, mitochondrial DNA testing, repeat-expansion testing. Each is commonly ordered in the ataxia/mito-mimic workup and each is **negative by design**. *(CMA has an incidental role only in the rare whole-gene-deletion AHC2 scenario — PMID:34421501.)*

**⚠️ Transcript caution:** confirm the report uses MANE Select **NM_152296.5** (PMID:41235133).

### Omics-Based Diagnostics

- **RNA sequencing:** no established role (missense variant, no splicing effect).
- **Proteomics / metabolomics / epigenomics (episignature) / liquid biopsy:** **no role; none validated.**

### Clinical Criteria

- **No formal consensus diagnostic criteria exist** for CAPOS (unlike AHC, which has Aicardi criteria). Diagnosis = compatible phenotype + p.Glu818Lys.
- GeneReviews **[P]**: *"The combination of cerebellar ataxia, areflexia, pes cavus, optic atrophy, and sensorineural hearing loss is unique to CAPOS syndrome."* — but the same source cautions that individuals may present with only a subset or a single feature (especially hearing loss), causing diagnostic delay.
- **Proposed practical trigger for testing:** *acute fever-induced ataxic encephalopathy in a child aged 6 mo – 5 yr with normal ancillary testing*, **or** *unexplained progressive auditory neuropathy at any age*, **or** *a childhood-onset non-/slowly-progressive cerebellar syndrome with areflexia + optic atrophy + SNHL*.

**Differential diagnosis (with distinguishing features):**

| Differential | How to distinguish |
|---|---|
| **Mitochondrial disease** (Leigh syndrome, MELAS, POLG, mtDNA disorders) | *The single most common misdiagnosis.* Normal lactate, normal MRI (no Leigh lesions), normal respiratory chain; PMID:26400718 explicitly notes the resemblance **[V]** |
| **Acute disseminated encephalomyelitis (ADEM) / acute encephalitis** | MRI normal; CSF bland; recurrent fever-triggered stereotyped episodes; family history |
| **Miller Fisher syndrome / Guillain-Barré** | Areflexia + ataxia + ophthalmoparesis overlaps closely; anti-GQ1b negative, no CSF albuminocytological dissociation, recurrent + familial |
| **Episodic ataxia types 1, 2, 5, 6** (*KCNA1, CACNA1A, CACNB4, SLC1A3*) | EA episodes typically shorter, no encephalopathy, no optic atrophy/deafness; **EA2 is also acetazolamide-responsive** — response does not discriminate |
| **Friedreich ataxia** | Ataxia + areflexia + pes cavus + optic atrophy + deafness overlaps substantially! Distinguish by: *FXN* GAA expansion, cardiomyopathy, diabetes, sensory neuropathy on NCS, **no fever-triggered episodes** |
| **Charcot-Marie-Tooth / hereditary neuropathies** | Pes cavus + areflexia overlap; NCS clearly abnormal in CMT, normal/near-normal in CAPOS |
| **Refsum disease, abetalipoproteinemia, AVED** | Treatable ataxia-plus-retinopathy mimics; phytanic acid, lipids, vitamin E |
| **Other ATP1A3 phenotypes (AHC, RDP, RECA/FIPWE)** | RECA/FIPWE is the closest mimic — **residue 756** variants, no optic atrophy/deafness (PMID:30862413, PMID:34342181) |
| **Wolfram syndrome (*WFS1*)** | Optic atrophy + deafness; add diabetes mellitus/insipidus, no ataxic episodes |
| **Autoimmune/paraneoplastic anti-Na⁺/K⁺-ATPase cerebellar syndrome** | Adult onset, tumour association, autoantibody positive (PMID:25809299) |
| **Biotinidase deficiency / biotin-thiamine-responsive basal ganglia disease** | Treatable; ataxia + deafness + optic atrophy; enzyme/*SLC19A3* testing |

### Screening

- **Newborn screening:** **Not included** in any NBS panel. Not currently justifiable (no proven presymptomatic intervention) — though the existence of a possible prophylactic (acetazolamide) and a critical pre-first-episode window makes this a legitimate future question.
- **Newborn hearing screening:** **⚠️ Important caveat — standard OAE-based newborn hearing screening will MISS CAPOS**, because OAEs are preserved. Only ABR-based (AABR) screening detects auditory neuropathy. This is a concrete, actionable public-health point worth curating.
- **Carrier screening:** not applicable (dominant).
- **Cascade testing:** **Strongly indicated.** Targeted p.Glu818Lys testing of at-risk relatives is cheap, definitive, and clinically actionable — it identifies pre-episode children who need antipyretic vigilance and audiological/ophthalmological surveillance, and adults with unexplained deafness/ataxia. PMID:28483396 is the model case; PMID:34655904 **[V]** shows the cost of not doing it (*"undiagnosed for thirty years"*).

---

## 11. Outcome / Prognosis

### Survival and Mortality

- **No systematic survival data exist for CAPOS.** No published mortality rate, 5-/10-year survival, or life-expectancy figure.
- GeneReviews **[P]**: *"Permanence of CAPOS symptoms, level of functioning, and life expectancy vary widely."*
- **Most reported patients survive into adulthood**, including into the fourth decade (PMID:29625811, age 38; PMID:26400718, age 34; PMID:29090527, three-generation pedigree with grandparental-generation carriers).
- **The one quantified mortality-relevant risk is cardiac.** PMID:32913013 **[V]**: *"a risk of life-threatening cardiac rhythm abnormalities equivalent to that in established cardiac channelopathies (≈3%)"* and *"Sudden cardiac death due to conduction abnormality emerged as a seizure-related outcome in murine Atp1a3-related disease."* This is spectrum-wide; CAPOS n=3.
- Acute episodes can involve coma and require intensive care; **death during an acute episode has not, to my reading of this corpus, been reported in CAPOS** — but the corpus is small and publication-biased toward survivors.

**Curation guidance:** record survival/mortality as **UNKNOWN / not established**, with the ≈3% ATP1A3-spectrum arrhythmia risk as the one quantified hazard, clearly scoped.

### Morbidity and Function

**The dominant burden is combined progressive sensory loss plus ataxia** — i.e., a *deafblind-plus-motor-disability* phenotype accumulating from early childhood.

Disability domains: mobility (ataxia, weakness, pes cavus); vision (to blindness in 20%); hearing (to profound, with disproportionate speech-in-noise disability); communication (dysarthria/anarthria + deafness + visual loss compounding); swallowing (dysphagia, aspiration risk); cognition and behaviour; education and employment.

**Quality of life:** **No CAPOS-specific QoL study has ever been performed.** No EQ-5D, SF-36, PROMIS, PedsQL, or disease-specific instrument data. This is a stark, curable gap, and it is arguably the most patient-relevant one in the entire entry.

### Disease Course and Complications

| Complication | Notes |
|---|---|
| Recurrent fever-triggered decompensations | 1–3 typical; ICU-level care possible |
| Progressive blindness | 20% reach HP:0000618 |
| Progressive profound deafness | Universal; auditory-neuropathy type |
| Aspiration pneumonia | From dysphagia (HP:0002015, 3/11) |
| Seizures | HP:0001250, 1/10; brief GTCS |
| Cardiac arrhythmia / SCD | ≈3% spectrum-wide (PMID:32913013) |
| Orthopaedic sequelae | Pes cavus, contractures, scoliosis |
| Psychiatric/behavioural | Autistic features, emotional/behavioural change |
| Peripartum deterioration | PMID:29090527 |

**Recovery potential:** partial and real. Recovery after each episode is *"considerable"* within days–weeks (GeneReviews **[P]**) but incomplete. Encouragingly, PMID:31410291 documented **late motor improvement in adolescence** long after the last episode **[V]**, and PMID:29184165 documented **remarkable benefit from cochlear implantation** **[V]**. Vision and hearing loss, by contrast, are **not recoverable** — they progress.

### Prognostic Factors

**No validated prognostic model or biomarker exists.** Candidate factors, all inferred from case series and **unvalidated**:
- Number and severity of acute episodes (stepwise deficit accrual)
- Age at first episode (earlier = presumed worse; unproven)
- Degree of inter-episode recovery after the first episode
- Presence of encephalopathy/coma vs. isolated ataxia during episodes
- Successful trigger avoidance / antipyresis
- Early cochlear implantation for auditory outcome
- Presence of ECG abnormality for cardiac risk

**Prognostic biomarkers: none.** Not applicable.

---

## 12. Treatment

> **Bottom line: there is no disease-modifying therapy for CAPOS. All management is supportive, preventive, and rehabilitative.** PMID:34655904 **[V]**: *"Treatment remains mostly supportive."* PMID:35047275 **[V]**: *"The mainstay management for patients with ATP1A3 related diseases is symptomatic treatment as there is no specific proposed treatment."*

### Pharmacotherapy

| Agent | Rationale / Evidence | Strength |
|---|---|---|
| **Acetazolamide** (carbonic anhydrase inhibitor; CHEBI:27690 [OLS-verified]) | Episode prophylaxis, by analogy with episodic ataxia. **PMID:27091223 [V]**: *"After initiation of acetazolamide in two patients, no further episodes occurred."* Same paper's measured conclusion **[V]**: *"Similar to some other types of episodic ataxia, acetazolamide may be considered in patients with CAPOS syndrome to prevent or attenuate bouts of ataxia, but this requires further study."* **Counter-evidence** PMID:36484864 **[V]**: *"No fluctuation was noted after using Acetazolamide."* | **Very weak** (n=2 uncontrolled, conflicting) |
| **Flunarizine** (calcium channel blocker; CHEBI:135652 [OLS-verified]) | Standard AHC prophylaxis, extrapolated. **PMID:29090527 [V]**: *"Prophylactic administration of acetazolamide or flunarizine may prevent acute episodes of ataxia or mitigate neurologic symptoms, although their efficacies have not been well studied."* In AHC generally: PMID:32339621 **[P]** — symptom reduction in 83% of AHC cases. In the *Matoub* E815K mouse: shortened hemiplegia duration, **no long-term benefit** (PMID:34612482 **[P]**). | **Very weak** for CAPOS |
| **Antipyretics** (paracetamol/acetaminophen, ibuprofen) | Trigger mitigation — the most mechanistically coherent intervention. PMID:35047275 **[V]**: *"Aggressive management of febrile illness may be helpful in alleviating the symptoms."* | Weak but universally recommended |
| **Anti-seizure medications** | For the minority with seizures. Levetiracetam most used across ATP1A3 cohorts (PMID:38243045 **[V]**). | Symptomatic |
| **Topiramate** | AHC prophylaxis; PMID:32339621 **[P]** — 25% of AHC cases. Not CAPOS-specific. | Very weak |
| **Levodopa** | Effective for a *specific* ATP1A3 paroxysmal-oculogyria presentation (PMID:26417536). **Not** a CAPOS treatment. | Not indicated |
| Benzodiazepines | Acute abortive use during episodes (empirical practice) | Anecdotal |

**Pharmacogenomics:** No PharmGKB/CPIC guideline involves *ATP1A3*. No genotype-guided dosing. **Not applicable.**

**⚠️ Anaesthesia caution (safety-relevant, weak evidence):** the *Atp1a3* D801Y mouse was *"refractory to ketamine anesthesia"* (PMID:39111836 **[P]**). Anaesthetic and perioperative planning should be cautious given the stress-trigger biology and cardiac conduction risk; there is **no CAPOS-specific anaesthesia literature**.

### Advanced Therapeutics

**None available for CAPOS. All are preclinical and developed against AHC alleles, not E818K.**

- **Gene therapy (AAV):** PMID:33577387 — AAV9-mediated gene therapy in the *Mashlool* (D801N) AHC mouse; PMID:34612482 **[P]** notes it *"improved hemiplegic episodes and beam-walking performance."*
- **Gene editing / prime editing — the most exciting recent development.** PMID:40695277 (*Cell*, 2025): **[P]** *"AAV9-mediated in vivo PE corrected Atp1a3 D801N and E815K mutations with up to 48% DNA correction"* and treatment *"restored ATPase activity; ameliorated paroxysmal spells, motor defects, and cognition deficits; and dramatically extended"* lifespan. **Note: E815K, three residues from E818K — the platform is directly transferable in principle, but E818K has not been targeted.**
- **Antisense oligonucleotides:** PMID:41048925 **[P]** highlights *"emerging therapeutic strategies, including gene therapy, antisense oligonucleotides, and small-molecule interventions."* No specific ASO program for E818K. *(Note: an allele-selective ASO knockdown strategy is mechanistically awkward here since E818K is not a clean gain-of-function; a splice/steric approach has no obvious target. Curate as speculative.)*
- **Cell therapy, immunotherapy, targeted small molecules:** none.

### Surgical and Interventional

| Intervention | Detail |
|---|---|
| **Cochlear implantation (CI)** — the highest-value intervention in CAPOS | PMID:29305691 **[V]**: *"Auditory neuropathy is difficult to treat with conventional hearing aids, but preliminary improvement in speech perception in some patients suggests that cochlear implantation may be effective in CAPOS patients."* PMID:29184165 **[V]**: *"cochlear implantation (CI) was performed in the first proband, leading to remarkable benefits."* Mixed results also reported — PMID:34692702 **[V]**: *"Patient 2 underwent CI on his left ear, and the result was poor."* Systematic review of post-synaptic auditory neuropathies incl. CAPOS, PMID:33136025 **[P]**: *"Overall trend was towards good post-CI outcomes with 22 of the total 25 patients displaying modest to significant benefit."* **CI is the right default; counsel about variability.** |
| **Orthopaedic surgery** for pes cavus/contractures | Standard neuro-orthopaedic indications |
| **Strabismus surgery** | As indicated |
| **Pacemaker / ICD** | PMID:32913013 **[V]**: *"We provide guidance to identify patients potentially at higher risk of sudden cardiac death who may benefit from insertion of a pacemaker or implantable cardioverter-defibrillator."* |
| Gastrostomy | For severe dysphagia/aspiration |

**Conventional hearing aids** are explicitly of limited benefit in auditory neuropathy (PMID:29305691 **[V]**) — an important negative recommendation. FM/remote-microphone systems help with the speech-in-noise problem.

### Supportive and Rehabilitative

- Aggressive fever management and early treatment of infection; a written **sick-day / emergency plan** for families.
- **Physical therapy** (ataxia, gait, balance, strength), **occupational therapy**, **speech and language therapy** (dysarthria + deafness), **swallowing therapy**.
- **Deafblind-specific services**: tactile communication, orientation and mobility training, assistive technology, educational support.
- **Low-vision rehabilitation**; **audiological rehabilitation**.
- Nutrition and aspiration-risk management.
- Psychological/psychiatric support; family and genetic counselling.

### Experimental Treatments / Clinical Trials

**No CAPOS-specific interventional clinical trial was identified in this pass.** No NCT identifier could be attributed to CAPOS. Relevant activity is in the AHC/ATP1A3 space (natural-history registries; preclinical gene-therapy programs). **Recommend a targeted ClinicalTrials.gov query for "ATP1A3" before curating a `clinical_trials` block, and populate only with verified NCT IDs.**

### Treatment Outcomes

- **Response rates:** unquantified for every intervention except CI (see above).
- **Adverse events:** acetazolamide — paraesthesia, anorexia, metabolic acidosis, nephrolithiasis, growth effects in children; flunarizine — sedation, weight gain, depression, extrapyramidal effects; CI — surgical risks, device failure, variable benefit.

### Treatment Strategy

**No published treatment algorithm or guideline exists for CAPOS.** A defensible pragmatic pathway synthesized from the corpus:

1. Confirm genotype (*ATP1A3* p.Glu818Lys) → stop the mitochondrial/metabolic workup.
2. **Baseline multidisciplinary assessment** (GeneReviews **[P]**): ophthalmology (acuity, optic atrophy, refraction, strabismus); audiology **with ABR + OAE** (not PTA alone); neurology + imaging; **cardiology with ECG and echocardiogram**; developmental/cognitive assessment in children.
3. **Trigger management plan**: antipyretic protocol, illness action plan, avoidance of physical/emotional/environmental stressors, peripartum planning in women.
4. **Consider prophylaxis** (acetazolamide ± flunarizine) after explicit shared decision-making about the weak evidence base.
5. **Sensory habilitation**: early CI evaluation for auditory neuropathy; low-vision services; deafblind educational planning.
6. **Rehabilitation**: PT/OT/SLT.
7. **Surveillance** (GeneReviews **[P]**): *at least once or twice yearly*, focused on progression of hearing and vision.
8. **Genetic counselling + cascade testing** of at-risk relatives.
9. **Personalized medicine:** genotype-guided only in the trivial sense that the genotype *is* the diagnosis. No genotype-stratified therapy exists.

### Suggested NCIT Treatment Annotations

| Treatment | `treatment_term` | `therapeutic_agent` | `therapeutic_modality` |
|---|---|---|---|
| Acetazolamide prophylaxis | NCIT:C15986 Pharmacotherapy | **CHEBI:27690** acetazolamide [OLS-verified] | SMALL_MOLECULE |
| Flunarizine prophylaxis | NCIT:C15986 Pharmacotherapy | **CHEBI:135652** flunarizine [OLS-verified] | SMALL_MOLECULE |
| Antipyretic therapy | NCIT:C15986 Pharmacotherapy | CHEBI:46195 paracetamol (verify) | SMALL_MOLECULE |
| Anti-seizure medication | NCIT:C15986 Pharmacotherapy | CHEBI:6437 levetiracetam (verify) | SMALL_MOLECULE |
| **Cochlear implantation** | NCIT:C15329 Surgical Procedure *(no NCIT clinical-action term for "cochlear implantation" was found under NCIT:C25218; **NCIT:C157820 "Cochlear Implant" is a DEVICE term and likely fails the `TreatmentTerm` dynamic enum — verify with `just validate-terms`)*| — | **DEVICE** |
| Physical therapy | NCIT:C15302 Physical Therapy | — | BEHAVIORAL |
| Occupational therapy | NCIT:C121351 Occupational Therapy (verify) | — | BEHAVIORAL |
| Speech therapy | NCIT:C159273 Speech Therapy (verify) | — | BEHAVIORAL |
| Low-vision / deafblind rehabilitation | NCIT:C15315 Rehabilitation | — | BEHAVIORAL |
| Supportive care | NCIT:C15747 Supportive Care | — | OTHER |
| Genetic counseling | NCIT:C15240 Genetic Counseling | — | BEHAVIORAL |
| Pacemaker / ICD insertion | NCIT:C15329 Surgical Procedure | — | DEVICE |
| Orthopaedic surgery (pes cavus) | NCIT:C16186 Orthopedic Surgical Procedure | — | SURGERY |

---

## 13. Prevention

### Primary Prevention (preventing the disease)

**Not possible.** CAPOS is caused by a germline de novo or inherited dominant variant. There is no modifiable exposure that prevents its occurrence.

The only meaningful primary prevention is **reproductive**: preventing transmission from an affected parent (see Genetic Screening below).

### Secondary Prevention (early detection and pre-emptive management)

This is where the real opportunity lies, and it is well-supported:

- **Cascade genetic testing** of first-degree relatives of an index case. PMID:28483396 is the model — identifying children **before their first acute episode** *"could aid early diagnosis and management before the onset of acute episodes"* **[V]**.
- **ABR-inclusive hearing screening.** Because CAPOS causes auditory *neuropathy*, OAE-only newborn screening misses it. Where a family is known to segregate p.Glu818Lys, **AABR screening plus serial ABR** should be specified.
- **Early consideration of ATP1A3 testing in sporadic progressive auditory neuropathy** — the highest-yield diagnostic-discovery route (PMID:29184165: 2/106; PMID:34692702: 4 patients).
- **Baseline and serial ophthalmological and audiological surveillance** in known carriers.
- **Baseline ECG** in all *ATP1A3* patients (PMID:32913013).

### Tertiary Prevention (preventing complications in affected individuals)

- **Trigger avoidance and aggressive antipyresis** — the central tertiary-prevention measure (§2, §12).
- **Peripartum planning** in affected women (PMID:29090527).
- **Prophylactic acetazolamide/flunarizine** — offered, with honest uncertainty.
- **Cardiac surveillance** with ECG ± Holter; pacemaker/ICD in selected high-risk patients (PMID:32913013).
- **Aspiration prevention** (swallow assessment, diet modification).
- **Sensory habilitation** (CI, low-vision services) to prevent secondary developmental, communicative, and educational deficits.
- **Falls/injury prevention** given ataxia + visual loss.

### Immunization

**No vaccine prevents CAPOS.** However, **routine childhood immunization is a rational, low-cost tertiary-prevention measure** because it reduces the burden of febrile illness — the dominant episode trigger. Notably, **influenza and COVID-19 vaccination** should be encouraged for the same reason.

**⚠️ A real and under-discussed tension:** vaccination itself commonly causes fever, and post-vaccination fever could plausibly trigger an episode. I found **no published CAPOS case of a vaccine-triggered episode and no guidance on this**. Pragmatic practice would be to vaccinate with **prophylactic antipyretic cover**. **Flag this explicitly as a knowledge gap with clinical consequence.**

### Screening and Early Detection

- **Population newborn screening:** not currently indicated (no proven presymptomatic intervention meeting Wilson-Jungner criteria). Revisit if acetazolamide prophylaxis or gene therapy is validated.
- **Genetic screening / reproductive options** for an affected parent (50% transmission risk):
  - **Prenatal diagnosis** — CVS or amniocentesis with targeted p.Glu818Lys testing.
  - **Preimplantation genetic testing for monogenic disease (PGT-M)** — technically straightforward for a known single-nucleotide variant.
  - Donor gametes; adoption.
  - **⚠️ Counselling caveat:** because expressivity is highly variable *within* families (from isolated hearing loss to severe encephalopathic disease), **genotype does not predict severity.** This must be central to any prenatal counselling conversation.
  - **⚠️ For parents of an apparently de novo case:** recurrence risk is low but **not zero** because of documented germline mosaicism in *ATP1A3* (PMID:27726050). Offer prenatal testing.
- **Risk stratification:** the only stratifier is genotype. No polygenic or clinical risk score exists.

### Behavioural Interventions

Illness-action planning; fever vigilance; sleep hygiene and meal regularity (per general ATP1A3 guidance); avoidance of extreme heat/cold, excessive noise, and crowds; stress management; injury-prevention adaptations.

### Counselling

**Genetic counselling is a core, non-optional component.** Content should cover: autosomal dominant inheritance and 50% recurrence risk; ~50% de novo rate; complete penetrance for *some* manifestation but highly variable expressivity; germline-mosaicism caveat; reproductive options (PGT-M, prenatal diagnosis); cascade testing of relatives; the fact that a positive genotype in a currently asymptomatic relative predicts *risk*, not severity — GeneReviews **[P]**: *"individuals and family members with the p.Glu818Lys pathogenic variant should be considered at risk of disease progression and development of other features."*

### Public Health and Environmental Interventions

Largely not applicable. The two systemic levers with real reach:
1. **Include *ATP1A3* on all clinical hearing-loss/auditory-neuropathy gene panels** — the single highest-yield systems-level change for CAPOS ascertainment.
2. **Promote ABR-based (not OAE-only) newborn hearing screening**, which would surface auditory neuropathy generally, CAPOS included.

### Prophylaxis

Covered above: acetazolamide/flunarizine (unproven), antipyretics (rational), immunization (rational, with the caveat noted).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** CAPOS is a **human-only** disease entity. **NCBITaxon:9606** (*Homo sapiens*). No naturally occurring CAPOS-equivalent disease has been described in any other species.
- **Breed (VBO):** **Not applicable.** No breed-associated *ATP1A3* disorder is recorded.
- **Orthologous genes:**
  | Species | Gene | NCBI Gene ID | Notes |
  |---|---|---|---|
  | *Homo sapiens* | *ATP1A3* | 478 | Glu818 in TM6 region |
  | *Mus musculus* | *Atp1a3* | 232975 | High conservation; basis of all mouse models |
  | *Rattus norvegicus* | *Atp1a3* | 24213 | |
  | *Danio rerio* | *atp1a3a*, *atp1a3b* | (verify) | Duplicated paralogs |
  | *Drosophila melanogaster* | *ATPα* | (verify) | Single α gene |
  | *C. elegans* | *eat-6* | (verify) | Single α gene |
  *(Verify all non-human Gene IDs against NCBI Gene before curating.)*
  Glu818 lies in a highly conserved region of the P-type ATPase; the corresponding Drosophila and C. elegans models used *equivalent* residues at other positions (PMID:34612482 **[P]**: CJ10 G744S "equivalent to G755 variants in humans"; DTS2 D981N "equivalent to D992 region in humans"), demonstrating that residue-mapping across these orthologs is routine.
- **Natural disease in other species:** **None reported.** A targeted OMIA (Online Mendelian Inheritance in Animals) search for a spontaneous *ATP1A3* disorder was not performed in this pass; **recommend an OMIA check before asserting absence definitively**, but the literature corpus contains no such report.
- **Veterinary relevance:** none currently.
- **Comparative pathology:** Not available for CAPOS specifically. Across ATP1A3 models generally, comparative work shows that the *pattern* of neurological dysfunction differs substantially between mouse and human even for identical residues — see §15 limitations.
- **Evolutionary conservation of mechanism:** The Na⁺/K⁺-ATPase is deeply conserved across Metazoa; the α-isoform diversification (α1 ubiquitous, α2 glial, α3 neuronal) is a vertebrate innovation. Invertebrate models have a **single α gene**, which is a fundamental limitation: they cannot model *isoform-specific* pathology. PMID:34612482 **[P]** flags this: Drosophila models have *"ubiquitous expression; not neurone-specific."*
- **Transmission / zoonotic potential:** **Not applicable.** CAPOS is genetic and non-transmissible.

---

## 15. Model Organisms

### 🔴 Headline Finding: No CAPOS Model Exists

**There is no animal or organoid model carrying the CAPOS E818K variant.** This was explicitly documented in the 2021 comprehensive review (PMID:34612482) and my search of the 2022–2026 *Atp1a3* animal-model literature (19 papers) found **no** E818K model has been generated since. Every published *Atp1a3* mouse targets a different allele: D801N, D801Y, E815K, I810N, D591V, or hypomorphic/null alleles.

**This is the single largest translational gap for CAPOS**, and it is particularly consequential because:
- The fever-trigger mechanism cannot be tested without a thermally challengeable *in vivo* model.
- The auditory-neuropathy and optic-atrophy phenotypes — the two features that *define* CAPOS against AHC/RDP — have never been modelled.
- Gene-editing therapy has now been demonstrated for the neighbouring **E815K** allele in mice (PMID:40695277), so the platform exists; only the CAPOS-specific model and target validation are missing.

**Curate this as a `discussions` entry with `kind: HUMAN_MODEL_MISMATCH`** — the situation is not merely "evidence absent" but "all available model evidence comes from mechanistically distinct alleles whose fidelity to CAPOS biology is unestablished."

### Available ATP1A3 Models (all non-CAPOS alleles)

Source: PMID:34612482 (*Dis Model Mech* 2021) **[P]** unless otherwise noted.

#### Mouse (*Mus musculus*, NCBITaxon:10090)

| Model | Allele | Phenotype recapitulation | Limitations |
|---|---|---|---|
| **Myshkin** | **I810N** (ENU) | *"spontaneous and vestibular stress-induced seizures, medial temporal sclerosis, sleep abnormalities, and a variety of motor, cognitive, social and other behavioural deficits"*; models AHC; hypofrontality. Social deficits in nest building, pup retrieval, three-chamber test (PMID:27276195). Cognitive deficits (PMID:27549929). | Homozygous neonatal lethal. AHC, not CAPOS. |
| **Mashlool / Mashl** | **D801N** | Transient hemiplegia/hemiparesis in ~40%; age-dependent worsening; core AHC features. **AAV9 gene therapy improved hemiplegic episodes and beam-walking** (PMID:33577387). Used for the cardiac-death study in PMID:32913013 **[V]**: *"resting ECGs showed intracardiac conduction delay; during induced seizures, heart block or complete sinus arrest led to death."* | Homozygous lethal at birth. |
| **Matoub** | **E815K** | **Most severe AHC phenotype**; **fever/heat-induced hemiplegia after warm-water exposure** — the only model with a demonstrated thermal trigger, and therefore the closest available proxy for CAPOS fever biology. Flunarizine shortened hemiplegia duration, no long-term benefit. | ~33% mortality during seizures; none survive beyond 9 months. **E815K, not E818K.** |
| **Atp1a3 D801Y** | D801Y | **Cold-**induced dystonia (not heat-induced); seizure susceptibility; learning impairment. Hyperactivity, diminished posture, motor deficits, *"refractory to ketamine anesthesia"* (PMID:39111836 **[P]**). | Temperature trigger direction is opposite to human RDP/CAPOS. Neither this nor tm1Ling shows fixed dystonia or human-type seizures. |
| **Atp1a3^tm1Ling/+** | Hypomorph | Increased locomotor activity; spatial memory deficits; **sex-dependent** stress-induced motor deficits (females only); ethanol-induced hyperkinesia (PMID:39111836). | Not a null; models no specific human variant. |
| **Atp1a3^tm2Kwk** | Near-null | Altered inhibitory neurotransmission; reduced social behaviour; decreased ascorbic acid. | Mildest phenotype; no stress-induced seizures. |
| **ROSA26-ATP1A3 D591V** | D591V transgene | Models autosomal-dominant cone-rod dystrophy; retinal dysfunction by 12 months. **The only retinal ATP1A3 model** — of tangential interest for CAPOS optic atrophy, but adCORD is a photoreceptor disease and CAPOS optic atrophy is an RGC/axonal disease. | Endogenous *Atp1a3* intact; milder than human. |
| **D801N & E815K comparative study** | Both | PMID:40381892 **[P]**: *"differential impact"* of the two variants on paroxysmal episodes, motor function, and neuroinflammation. Important precedent that residue-adjacent alleles produce genuinely distinct biology. | AHC alleles only. |

#### Zebrafish (*Danio rerio*, NCBITaxon:7955)
- **atp1a3a / atp1a3b morpholino knockdown** — hydrocephalus; delayed motor responses to tactile stimulation. **Limitation:** hydrocephalus is *not* a human ATP1A3 phenotype, so the model's construct validity is doubtful.
- **A813V zebrafish** (PMID:42116168 **[P]**) — displayed *"neuronal hyperexcitability before neurodegeneration"*; a newer, more phenotypically relevant zebrafish approach.

#### Drosophila (*Drosophila melanogaster*, NCBITaxon:7227)
- **CJ10 (ATPα G744S)** — age-dependent mechanical-stress-induced paralysis; **heat-induced reversible paralysis** (relevant to fever-trigger biology!); age-dependent neurodegeneration with vacuolar/spongiform pathology.
- **DTS2 (ATPα D981N)** — age-dependent loss of locomotor activity; mechanical-stress-induced paralysis at 28 °C; heat-induced paralysis at 37–38 °C.
- **Limitation for both:** ubiquitous rather than neurone-specific expression; single α isoform.

#### *C. elegans* (NCBITaxon:6239)
- **eat-6 G304S** (modelling human ARA-related G316S) — viable homozygotes (hypomorphic); progressive bradykinesia of pharyngeal pumping by day 8; aldicarb hypersensitivity.
- **Limitation:** minimal behavioural repertoire; great evolutionary distance; single α gene.

#### Cellular / *in vitro* systems (the actual workhorses for CAPOS)
- **Xenopus oocyte and mammalian cell heterologous expression** — the *only* systems in which E818K itself has been characterized. Used in PMID:30409907 (biochemistry + electrophysiology) and PMID:29305691 (heterologous expression + molecular dynamics). **These, plus molecular-dynamics simulation, constitute the entire experimental evidence base for CAPOS pathophysiology.**
- **Pump-survival assays** (ouabain-resistance rescue) — PMID:32653672 **[P]**: across 12 RDP/AHC variants, *"All studied mutations led to functional impairment of the pump, as reflected by lower survival rate and reduced pump current"*, but *"No difference in the extent of impairment, nor in the expression level, was found between the two phenotypes"* — a key cautionary result: **pump-function magnitude does not predict phenotype**.
- **iPSC-derived neurons:** demonstrated for A813V (PMID:42116168) but **not for E818K**.
- **Organoids:** none.

### Induced (non-genetic) Models
Ouabain infusion (pharmacological Na⁺/K⁺-ATPase inhibition) has been used historically to model dystonia; not CAPOS-specific.

### Research Applications and Gaps

**What existing models CAN support:** general α3 pump biology; Na⁺ homeostasis and excitability; stress/thermal triggering (Matoub, Drosophila CJ10/DTS2); cardiac conduction and seizure-related death (Mashlool); gene-therapy and prime-editing platform development (Mashlool, Matoub).

**What NO model can currently support:** CAPOS auditory neuropathy; CAPOS optic atrophy; the specific fever→ataxic-encephalopathy sequence with incomplete recovery; E818K-specific target validation for gene editing; preclinical testing of acetazolamide/flunarizine in a CAPOS-relevant genetic background.

**Priority proposed experiments** (for `proposed_experiments` in the KNOWLEDGE_GAP/HUMAN_MODEL_MISMATCH entries):
1. Generate an **Atp1a3^E818K/+ knock-in mouse**; phenotype with ABR/OAE/DPOAE, OCT/RGC counts, rotarod/beam-walk, and a controlled **thermal (fever-mimic) challenge**.
2. **Temperature-dependent electrophysiology** of E818K in oocytes/HEK cells across 33–41 °C to test the thermal-lability hypothesis directly.
3. **Patient-derived and isogenic iPSC** → cerebellar, retinal-ganglion, and inner-ear/otic organoids with paired scRNA-seq and electrophysiology.
4. **Prime-editing correction of E818K** in patient iPSC-neurons, leveraging the PMID:40695277 platform.
5. Neuropathological study of a CAPOS brain, cochlea, and optic nerve (post-mortem tissue donation program).

### Model Databases
MGI (mouse; *Atp1a3* MGI:88107 — verify), IMPC, IMSR, MMRRC, ZFIN, FlyBase, WormBase, Alliance of Genome Resources, RGD, Cellosaurus, ATCC.

---

## Appendix A — Consolidated Suggested Ontology Bindings

**Disease:** `MONDO:0011038` — cerebellar ataxia-areflexia-pes cavus-optic atrophy-sensorineural hearing loss syndrome [OLS-verified]

**Gene:** `hgnc:801` — ATP1A3 (lowercase prefix per dismech convention) [HGNC-verified]

**Inheritance:** `HP:0000006` — Autosomal dominant inheritance

**Top phenotypes (all with published frequencies — see §3.1):** `HP:0000648` optic atrophy (11/11), `HP:0001284` areflexia (11/11), `HP:0002131` episodic ataxia (10/10), `HP:0000407` sensorineural hearing impairment (10/10), `HP:0001324` muscle weakness (10/10), `HP:0000639` nystagmus (7/10), `HP:0002066` gait ataxia (6/11), `HP:0001761` pes cavus (3/10)

**Molecular function / cellular component:** `GO:0005391` P-type sodium:potassium-exchanging transporter activity (`modifier: DECREASED`) [OLS-verified]; `GO:0005890` sodium:potassium-exchanging ATPase complex [OLS-verified]

**Biological processes:** `GO:0035725` sodium ion transmembrane transport (DECREASED) [OLS-verified]; `GO:0006883` intracellular sodium ion homeostasis (DISRUPTED/INCREASED intracellular Na⁺) [OLS-verified]; `GO:0042391` regulation of membrane potential (DECREASED) [OLS-verified]

**Cell types:** `CL:0011113` spiral ganglion neuron [OLS-verified]; `CL:0000589` cochlear inner hair cell [OLS-verified]; `CL:0000601` cochlear outer hair cell (**spared**) [OLS-verified]; `CL:0000121` Purkinje cell [OLS-verified]; `CL:0000540` neuron; `CL:0000740` retinal ganglion cell (verify)

**Anatomy:** `UBERON:0000941` cranial nerve II [OLS-verified]; `UBERON:0001844` cochlea [OLS-verified]; `UBERON:0002227` spiral organ of cochlea [OLS-verified]; `UBERON:0002037` cerebellum (verify)

**Chemicals:** `CHEBI:27690` acetazolamide [OLS-verified]; `CHEBI:135652` flunarizine [OLS-verified]; `CHEBI:29101` sodium(1+) (verify); `CHEBI:29103` potassium(1+) (verify); `CHEBI:15422` ATP (verify)

---

## Appendix B — Candidate Mechanism-Module Relationships

For dismech `conforms_to` consideration:

- **`peripheral_axonal_degeneration`** — partial fit for the areflexia/pes cavus arm, but the corpus is genuinely conflicted on whether CAPOS areflexia is peripheral at all (PMID:8733056 says *"in the absence of a peripheral neuropathy"*; PMID:34655904 documents abnormal EMG). **Recommend NOT declaring conformance** until the central-vs-peripheral question is resolved; instead curate the conflict as a KNOWLEDGE_GAP.
- **`cerebellar_purkinje_degeneration`** — plausible for the persistent-ataxia arm, but there is **no histological evidence of Purkinje loss in CAPOS** and MRI is usually normal. Conformance would be aspirational. Consider declaring at the "loss of cerebellar cortical output" node only, with an explicit note.
- **`photoreceptor_degeneration`** — **poor fit.** CAPOS optic atrophy is an RGC/axonal disease, not a photoreceptor disease. Do **not** declare conformance. *(Note the contrast with ATP1A3 p.D591V adCORD, which IS a photoreceptor disease — a nice illustration of allele-specific tissue targeting.)*
- **`sensorineural_hair_cell_loss`** — **explicitly wrong for CAPOS and worth saying so.** That module's chain runs through *"Hair Cell Mechanotransduction Failure and Death"*; CAPOS hair cells are **preserved** (OAEs and CM present). CAPOS is post-synaptic/neural. This is a good candidate for a **new module** — e.g. `auditory_neuropathy_synaptopathy` (afferent synapse/spiral-ganglion-neuron conduction failure with preserved OHC function), which would also serve *OTOF*, *OPA1*, *DIAPH3*, and *AIFM1* disorders. **Strong recommendation.**
- **`cardiac_ion_channel_repolarization`** — partial fit for the ATP1A3-spectrum arrhythmia risk, but the mechanism is pump-mediated conduction delay rather than channel repolarization. Weak; curate the cardiac risk as a phenotype with evidence rather than as module conformance.
- **`epilepsy_excitation_inhibition_imbalance`** — applicable only to the 1/10 with seizures; weak.

---

## Appendix C — Priority Knowledge Gaps (for `discussions`)

| Gap | Kind | Attaches to |
|---|---|---|
| Mechanism by which fever triggers decompensation is unknown (explicitly stated, PMID:30862413) | KNOWLEDGE_GAP | acute-decompensation node |
| No E818K animal model exists; all *in vivo* evidence comes from mechanistically distinct alleles | **HUMAN_MODEL_MISMATCH** | whole pathograph |
| Is CAPOS areflexia central or peripheral? Original report vs. PMID:34655904 EMG | KNOWLEDGE_GAP | areflexia node |
| Why does E818K produce sensory (auditory/optic) disease when the adjacent E815K produces AHC? | KNOWLEDGE_GAP | genotype→phenotype edge |
| Is E818K dominant-negative or simple partial LoF? (whole-gene deletion → AHC2, not CAPOS) | KNOWLEDGE_GAP | molecular node |
| Modifier genes explaining intrafamilial severity variation | KNOWLEDGE_GAP | disease level |
| No omics data of any kind (transcriptomic, proteomic, metabolomic, single-cell) | KNOWLEDGE_GAP | disease level |
| No neuropathology/autopsy study published | KNOWLEDGE_GAP | tissue-damage nodes |
| No QoL/PRO data; no natural-history registry | KNOWLEDGE_GAP | disease level |
| Acetazolamide efficacy unproven and contradicted (PMID:27091223 vs PMID:36484864) | KNOWLEDGE_GAP | treatment |
| Vaccination-associated fever as a potential trigger — unstudied, clinically consequential | KNOWLEDGE_GAP | trigger node |
| True prevalence unknown; likely substantially underestimated within the ANSD population | KNOWLEDGE_GAP | prevalence |

---

## Sources

Primary literature (PubMed): [PMID:8733056](https://pubmed.ncbi.nlm.nih.gov/8733056/) · [PMID:24468074](https://pubmed.ncbi.nlm.nih.gov/24468074/) · [PMID:25056583](https://pubmed.ncbi.nlm.nih.gov/25056583/) · [PMID:25447930](https://pubmed.ncbi.nlm.nih.gov/25447930/) · [PMID:25809299](https://pubmed.ncbi.nlm.nih.gov/25809299/) · [PMID:25895915](https://pubmed.ncbi.nlm.nih.gov/25895915/) · [PMID:26400718](https://pubmed.ncbi.nlm.nih.gov/26400718/) · [PMID:26417536](https://pubmed.ncbi.nlm.nih.gov/26417536/) · [PMID:26453127](https://pubmed.ncbi.nlm.nih.gov/26453127/) · [PMID:27091223](https://pubmed.ncbi.nlm.nih.gov/27091223/) · [PMID:27276195](https://pubmed.ncbi.nlm.nih.gov/27276195/) · [PMID:27313535](https://pubmed.ncbi.nlm.nih.gov/27313535/) · [PMID:27378932](https://pubmed.ncbi.nlm.nih.gov/27378932/) · [PMID:27549929](https://pubmed.ncbi.nlm.nih.gov/27549929/) · [PMID:27634470](https://pubmed.ncbi.nlm.nih.gov/27634470/) · [PMID:27726050](https://pubmed.ncbi.nlm.nih.gov/27726050/) · [PMID:28483396](https://pubmed.ncbi.nlm.nih.gov/28483396/) · [PMID:29090527](https://pubmed.ncbi.nlm.nih.gov/29090527/) · [PMID:29184165](https://www.nature.com/articles/s41598-017-16676-9) · [PMID:29287866](https://pubmed.ncbi.nlm.nih.gov/29287866/) · [PMID:29291920](https://pubmed.ncbi.nlm.nih.gov/29291920/) · [PMID:29305691](https://link.springer.com/article/10.1007/s00439-017-1862-z) · [PMID:29396171](https://pubmed.ncbi.nlm.nih.gov/29396171/) · [PMID:29397530](https://pubmed.ncbi.nlm.nih.gov/29397530/) · [PMID:29625811](https://www.sciencedirect.com/science/article/abs/pii/S0387760418300895) · [PMID:30409907](https://pubmed.ncbi.nlm.nih.gov/30409907/) · [PMID:30554714](https://pubmed.ncbi.nlm.nih.gov/30554714/) · [PMID:30862413](https://pubmed.ncbi.nlm.nih.gov/30862413/) · [PMID:30904181](https://pubmed.ncbi.nlm.nih.gov/30904181/) · [PMID:31410291](https://pubmed.ncbi.nlm.nih.gov/31410291/) · [PMID:32339621](https://pubmed.ncbi.nlm.nih.gov/32339621/) · [PMID:32653672](https://pubmed.ncbi.nlm.nih.gov/32653672/) · [PMID:32913013](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7734736/) · [PMID:33136025](https://pubmed.ncbi.nlm.nih.gov/33136025/) · [PMID:33577387](https://pubmed.ncbi.nlm.nih.gov/33577387/) · [PMID:33762331](https://pubmed.ncbi.nlm.nih.gov/33762331/) · [PMID:33868146](https://pubmed.ncbi.nlm.nih.gov/33868146/) · [PMID:34342181](https://pubmed.ncbi.nlm.nih.gov/34342181/) · [PMID:34421501](https://pubmed.ncbi.nlm.nih.gov/34421501/) · [PMID:34464766](https://pubmed.ncbi.nlm.nih.gov/34464766/) · [PMID:34612482](https://journals.biologists.com/dmm/article/14/10/dmm048938/272403/Genetically-altered-animal-models-for-ATP1A3) · [PMID:34655904](https://pubmed.ncbi.nlm.nih.gov/34655904/) · [PMID:34692702](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8531511/) · [PMID:34761051](https://pubmed.ncbi.nlm.nih.gov/34761051/) · [PMID:35047275](https://pubmed.ncbi.nlm.nih.gov/35047275/) · [PMID:36339296](https://pubmed.ncbi.nlm.nih.gov/36339296/) · [PMID:36484864](https://pubmed.ncbi.nlm.nih.gov/36484864/) · [PMID:37043503](https://pubmed.ncbi.nlm.nih.gov/37043503/) · [PMID:38243045](https://pubmed.ncbi.nlm.nih.gov/38243045/) · [PMID:38297853](https://lcehen.whuhzzs.com/article/doi/10.13201/j.issn.2096-7993.2024.01.012) · [PMID:38796484](https://pubmed.ncbi.nlm.nih.gov/38796484/) · [PMID:38821025](https://pubmed.ncbi.nlm.nih.gov/38821025/) · [PMID:39111836](https://pubmed.ncbi.nlm.nih.gov/39111836/) · [PMID:39533828](https://pubmed.ncbi.nlm.nih.gov/39533828/) · [PMID:40381892](https://pubmed.ncbi.nlm.nih.gov/40381892/) · [PMID:40695277](https://pubmed.ncbi.nlm.nih.gov/40695277/) · [PMID:41048925](https://pubmed.ncbi.nlm.nih.gov/41048925/) · [PMID:41235133](https://pubmed.ncbi.nlm.nih.gov/41235133/) · [PMID:41480049](https://pubmed.ncbi.nlm.nih.gov/41480049/) · [PMID:41850905](https://pubmed.ncbi.nlm.nih.gov/41850905/) · [PMID:42116168](https://pubmed.ncbi.nlm.nih.gov/42116168/) · [PMID:42151635](https://pubmed.ncbi.nlm.nih.gov/42151635/)

Databases and reference resources: [GeneReviews — ATP1A3-Related Disorder (PMID:20301294)](https://www.ncbi.nlm.nih.gov/books/NBK1115/) · [OMIM #601338](https://omim.org/entry/601338) · [Orphanet ORPHA:1171](https://www.orpha.net/en/disease/detail/1171) · [MedGen C1832466](https://www.ncbi.nlm.nih.gov/medgen/C1832466) · [ClinVar VCV000156238](https://www.ncbi.nlm.nih.gov/clinvar/) · [MONDO:0011038 via EBI OLS](https://www.ebi.ac.uk/ols4/) · [Human Phenotype Ontology annotations for OMIM:601338](https://ontology.jax.org/) · [HGNC:801](https://rest.genenames.org/fetch/symbol/ATP1A3) · [Europe PMC](https://www.ebi.ac.uk/europepmc/) · [NCBI E-utilities](https://eutils.ncbi.nlm.nih.gov/)

---

### Handoff Notes for the Curator

1. **Run the reference-fetch loop first.** Every PMID cited here needs `just fetch-reference PMID:XXXX`; every snippet needs `just validate-references`. Quotes marked **[P]** are the highest-risk — assume they need replacement with a verified exact quote or removal.
2. **Verify all non-`[OLS-verified]` ontology IDs** with `just validate-terms`. The NCIT cochlear-implantation term in particular is likely to fail the `TreatmentTerm` dynamic-enum reachability check from `NCIT:C25218`.
3. **The NEC preflight passed** — but note that a naive PubMed query on "CAPOS" returns five unrelated entities. Any future automated literature sweep for this disease must anchor on `ATP1A3` or the full expanded acronym, never on the bare string.
4. **Consider proposing a new `auditory_neuropathy_synaptopathy` module** (Appendix B) — CAPOS would be its flagship conformer, and it would immediately serve *OTOF*, *OPA1*, *AIFM1*, and *DIAPH3* disorders. The existing `sensorineural_hair_cell_loss` module is mechanistically wrong for this class.
5. **Consider a `ATP1A3-Related_Disorders` Grouping** (§4) with CAPOS, AHC2, RDP, and RECA as members and residue-position-keyed `differentiating_mechanisms`.
6. **Do not overstate prevalence.** Use `measure_type: CASES_IN_LITERATURE` and `prevalence_class: ULTRA_RARE`; omit `rate_per_100000`.
7. **The pes cavus / acronym mismatch** (30% frequency for the "P" in CAPOS) is worth a `notes` field — it is a recurring source of missed diagnoses.