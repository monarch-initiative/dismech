---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-07-25T11:42:38.868934'
end_time: '2026-07-25T12:06:03.555244'
duration_seconds: 1404.69
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Unverricht-Lundborg Disease
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
  web_search_requests: 3
  num_turns: 54
  total_cost_usd: 6.397909999999999
  session_id: 5fea9205-2c05-44a7-a656-c6eb8905f018
  stop_reason: end_turn
citation_count: 13
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Unverricht-Lundborg Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Unverricht-Lundborg Disease** covering all of the
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

# Unverricht–Lundborg Disease (EPM1 / ULD) — Comprehensive Research Report

**Prepared:** 2026-07-25 · **Target MONDO:** `MONDO:0009698` · **Category:** Mendelian (autosomal recessive)

> **A note on quote provenance, because this feeds a KB.** Every snippet marked **[VQ]** ("verified quote") was pulled directly from the PubMed abstract via NCBI E-utilities during this session and is an exact substring of that abstract — safe to drop into an `evidence.snippet` after a `just fetch-reference` round-trip. Snippets marked **[UNVERIFIED-BODY]** come from full-text or GeneReviews prose rendered through a web fetch; they are *leads only* and must be re-verified (or, better, replaced with an abstract quote) before curation. Ontology terms marked **[OAK✓]** were checked against the local OAK adapters in this repo; unmarked ones need a lookup.

---

## 1. Disease Information

### Overview

Unverricht–Lundborg disease is the most common of the progressive myoclonus epilepsies (PMEs). Think of it as a slow structural failure in a house whose wiring was fine at construction: children develop normally, then somewhere between ages 6 and 16 the myoclonus starts — brief, involuntary jerks that fire on *action* and on *stimulus* (light, touch, startle, stress, physical effort) — followed by generalized tonic-clonic seizures, and then, over years, ataxia, intention tremor, and dysarthria. Unlike Lafora disease or the neuronal ceroid lipofuscinoses, cognition is comparatively spared: patients stay mentally alert with only mild decline, which makes the progressive motor disability especially cruel.

Orphanet's definition (ORPHA:308):

> "A rare progressive myoclonic epilepsy (PME) disorder characterized by action- and stimulus-sensitive myoclonus, and tonic-clonic seizures with ataxia, but with only a mild cognitive decline over time." — Orphanet/Orphadata, ORPHA:308, snapshot 2026-06-23

### Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | `MONDO:0009698` | Label: *Unverricht-Lundborg syndrome* (confirmed live via OLS4) |
| **OMIM** | `254800` | "Epilepsy, progressive myoclonic 1A (Unverricht and Lundborg)" — exact map to ORPHA:308 |
| **OMIM (gene)** | `601145` | CSTB |
| **Orphanet** | `ORPHA:308` | Preferred term: *Progressive myoclonic epilepsy type 1* |
| **ICD-10** | `G40.3` | NTBT (ORPHAcode narrower than the code) |
| **ICD-11** | `8A61.41` | NTBT |
| **MeSH** | `D020194` | Unverricht-Lundborg Syndrome (exact) |
| **UMLS** | `C0751785` | exact |
| **MedDRA** | `10054895` | exact |
| **GARD** | `3876` | exact |
| **HGNC** | `hgnc:2482` | CSTB [OAK✓] |
| **NCBI Gene** | `NCBIGene:1476` | CSTB |
| **UniProt** | `P04080` (CYTB_HUMAN) | 98 aa; PDB 1STF, 2OCT, 4N6V |

**Related-but-distinct OMIM entries mapped by Orphanet as *narrower* than ORPHA:308** (i.e., Orphanet lumps, OMIM splits — a lump/split decision worth recording in the entry): `OMIM:612437` (EPM1B, *PRICKLE1*) and `OMIM:310370`.

### Synonyms / alternative names

EPM1; EPM1A; ULD; Unverricht-Lundborg syndrome; progressive myoclonic epilepsy type 1; progressive myoclonus epilepsy type 1; **Baltic myoclonus** / Baltic myoclonic epilepsy; **Mediterranean myoclonus** / Ramsay Hunt syndrome type 1 (historical, now deprecated — the "Mediterranean myoclonus" and "Baltic myoclonus" labels were unified once CSTB was cloned). Orphanet synonym list: `['EPM1', 'Progressive myoclonus epilepsy type 1', 'ULD', 'Unverricht-Lundborg disease']`.

⚠️ **NEC (named-entity-confusion) risk flag.** EPM1 sits squarely in two of the high-risk classes from `research/nec_risk_disease_classes.md`: (a) a **numbered series** (EPM1–EPM11+, plus the EPM1A/EPM1B split), and (b) **eponymic/geographic aliasing** (Ramsay Hunt syndrome type 1 is *also* the name of a herpes-zoster oticus syndrome — completely unrelated). Any deep-research report for "Unverricht-Lundborg" must be gene-checked against **CSTB**; a report dominated by *PRICKLE1*, *EPM2A/NHLRC1*, *KCNC1*, or *SCARB2* is describing a different entity.

### Data provenance

Information here is **aggregated disease-level** (OMIM, Orphanet, HPO annotations, GeneReviews, primary literature). Notably, EPM1 is one of the few rare diseases with genuine **population-registry** data: Sipilä et al. combined Finnish national registries with medical records for *every* patient treated in Finland 1998–2016 (PMID:32943486) — i.e., real EHR/registry-derived epidemiology rather than literature-case aggregation.

---

## 2. Etiology

### Primary cause

Biallelic **loss-of-function** alterations in *CSTB* (cystatin B / stefin B), at chromosome **21q22.3**, encoding a 98-amino-acid intracellular inhibitor of cysteine cathepsins. This is a pure monogenic disorder — no infectious, toxic, or autoimmune etiology.

The founding evidence (PMID:8596935) **[VQ]**:

> "Progressive myoclonus epilepsy of the Unverricht-Lundborg type (EPM1) is an autosomal recessive inherited form of epilepsy, previously linked to human chromosome 21q22.3. The gene encoding cystatin B was shown to be localized to this region, and levels of messenger RNA encoded by this gene were found to be decreased in cells from affected individuals."

### The dominant mutational mechanism: a promoter dodecamer expansion

The overwhelming majority of EPM1 alleles are not coding mutations at all but an **unstable expansion of a 12-bp (dodecamer) repeat, `CCCCGCCCCGCG`, ~70 nt upstream of the CSTB transcription start site**. This is a promoter/regulatory expansion — the gene body is intact, but transcription is throttled.

PMID:9126745 (Lalioti et al., *Nature* 1997) **[VQ]**:

> "Here we report that the majority of EPM1 alleles contain expansions of a dodecamer (12-mer) repeat located about 70 nucleotides upstream of the transcription start site nearest to the 5' end of the CSTB gene. Normal alleles contain 2 or 3 copies of this repeat whereas mutant alleles contain more than 60 such repeats and have reduced levels of CSTB messenger RNA in blood but not in cell lines. 'Premutation' CSTB alleles with 12-17 repeats show marked instability when transmitted to offspring."

PMID:9090386 (Virtaneva et al., *Nat Genet* 1997) reported the same expansion independently and established the founder structure **[VQ]**:

> "In this study, we report a novel type of disease-causing mutation, an unstable 15- to 18-mer minisatellite repeat expansion in the putative promoter region of the CST6 gene. The mutation accounts for the majority of EPM1 patients worldwide. Haplotype data are compatible with a single ancestral founder mutation."

(Note the historical gene symbol *CST6* in that 1997 paper — it is the gene now called *CSTB*. `CST6` today denotes cystatin E/M, a different gene. Another NEC trap.)

### Risk factors

**Genetic (causal):** biallelic *CSTB* alterations. There are no established susceptibility loci or polygenic contributors — EPM1 is fully Mendelian.

**Genetic (modifier — see §4):** expansion allele length (modulating, not deterministic); *APOE* ε4 (2025 evidence, mixed direction); as-yet-unidentified intrafamilial modifiers, since siblings with identical repeat sizes differ in severity.

**Environmental:** none causal. However, **provoking factors for symptoms** are prominent and clinically actionable — photic stimulation, physical exertion, stress, and (in one reported case) menstrual cycle phase (PMID:40442775) all trigger myoclonus. **Iatrogenic aggravation is the single most important modifiable "environmental" risk factor** (see §12: phenytoin, sodium-channel blockers, GABAergic drugs, gabapentinoids).

**Consanguinity** raises risk for the rare homozygous point/frameshift genotypes — e.g., the severe Sri Lankan sibling pair born to consanguineous parents (PMID:28378817).

### Protective factors

No established genetic protective variants. On the environmental side, protection is essentially therapeutic and rehabilitative: avoidance of aggravating antiseizure medications, early physiotherapy, and psychosocial support. GeneReviews attributes the improvement in survival directly to this **[UNVERIFIED-BODY]**: *"With better pharmacologic, physiotherapeutic, and psychosocial supportive treatment, life expectancy is comparable to controls up to age 40 years, but is poorer over the long term."*

An intriguing and genuinely unresolved finding: in a Finnish cohort of 65 expansion-homozygous patients, *APOE* ε4 carriers reported **better** quality of life and had **better-preserved hippocampal/amygdalar volumes** despite *more* white-matter degeneration (PMID:41042579) **[VQ]**:

> "Despite greater white matter degeneration and reduced cortical thickness, APOE ε4 carriers exhibited preserved deep brain volumes and better self-reported well-being."

This is the opposite of the ε4 direction in Alzheimer disease and should be curated as an **emerging, unreplicated** mechanistic hypothesis, not an established protective factor.

### Gene–environment interactions

The clearest G×E axis in EPM1 is **pharmacogenetic-by-way-of-mechanism** rather than metabolic: because the underlying lesion is loss of GABAergic inhibition plus cortical hyperexcitability, drugs that further destabilize that balance produce paradoxical clinical worsening. Kälviäinen 2008 (PMID:18325013) **[VQ]**:

> "There are a number of agents that aggravate clinical course of EPM1 such as phenytoin aggravating the associated neurologic symptoms or even accelerating cerebellar degeneration."

A second axis: **oxidative stress as environmental amplifier of a genetic redox deficit** — CSTB is normally *induced* by oxidative stress, and the EPM1 promoter expansion breaks that induction, so the cell loses its stress-response reserve exactly when it needs it (PMID:19420257, quoted in §6).

---

## 3. Phenotypes

### HPO annotations on record (HPO API, `OMIM:254800`, retrieved 2026-07-25)

| HP ID | Label | Annotated frequency (n/N) | Category |
|---|---|---|---|
| `HP:0001336` | Myoclonus [OAK✓] | **42/42 (100%)** | Nervous system |
| `HP:0002069` | Bilateral tonic-clonic seizure [OAK✓] | **31/32 (97%)** | Nervous system |
| `HP:0003621` | Juvenile onset [OAK✓] | **29/29 (100%)** | Clinical course |
| `HP:0011182` | Interictal epileptiform activity [OAK✓] | 6/10 (60%) | Nervous system |
| `HP:0001268` | Mental deterioration [OAK✓] | 4/10 (40%) | Nervous system |
| `HP:0001251` | Ataxia [OAK✓] | 2/3 | Nervous system |
| `HP:0010850` | EEG with spike-wave complexes [OAK✓] | 2/3 | Nervous system |
| `HP:0000726` | Dementia | 1/3 | Nervous system |
| `HP:0001256` | Mild intellectual disability | 1/3 | Nervous system |
| `HP:0001260` | Dysarthria [OAK✓] | — | Nervous system |
| `HP:0002392` | EEG with polyspike wave complexes [OAK✓] | — | Nervous system |
| `HP:0002121` | Generalized non-motor (absence) seizure | — | Nervous system |
| `HP:0000007` | Autosomal recessive inheritance [OAK✓] | — | Inheritance |

The existing HPO annotation set is **thin and under-frequencied** relative to the literature. Suggested additions below are supported by primary sources.

### Suggested phenotype curation (with characteristics)

#### Cardinal motor phenotypes

**Action- and stimulus-sensitive myoclonus** — `HP:0001336` Myoclonus [OAK✓], with `HP:0002123` Generalized myoclonic seizure [OAK✓] and `HP:0001327` Photosensitive myoclonic seizure [OAK✓] for the photic-triggered component.
- *Type:* clinical sign / physical manifestation
- *Onset:* 6–16 years (`onset_category` juvenile; `HP:0003621`)
- *Severity:* variable → severe; quantified with the **Unified Myoclonus Rating Scale (UMRS)**, action myoclonus subscale (section 4) scored /160
- *Progression:* PROGRESSIVE
- *Frequency:* obligate (100%, 42/42 HPO)
- *QoL impact:* the dominant disability driver. Action-induced jerks make writing, eating, dressing, and walking progressively impossible; ~1/3 become wheelchair-dependent within 5–10 years **[UNVERIFIED-BODY, GeneReviews]**.

PMID:38179183 states the primacy plainly **[VQ]**: *"The key clinical manifestation in EPM1 is progressive, stimulus-sensitive, in particular action-induced myoclonus."*

**Generalized tonic-clonic seizures** — `HP:0002069` [OAK✓]; consider `HP:0007207` Photosensitive tonic-clonic seizure [OAK✓].
- *Frequency:* 31/32 (97%). Often the presenting symptom (about half present with GTCS, about half with myoclonus).
- *Progression:* frequently improve/remit with treatment over time, while myoclonus worsens — a clinically important dissociation.
- *Complication:* `HP:0002133` Status epilepticus [OAK✓] (myoclonic status), noted by Michelucci et al. (PMID:27629998) **[VQ]**: *"The emergency treatment of motor status, which often complicates the course of PMEs, consists of intravenous administration of benzodiazepines, valproate, or levetiracetam."*

**Cerebellar syndrome** — `HP:0001251` Ataxia [OAK✓], `HP:0002078` Truncal ataxia [OAK✓], `HP:0001310` Dysmetria [OAK✓], `HP:0002080` Intention tremor [OAK✓], `HP:0002345` Action tremor [OAK✓], `HP:0001260` Dysarthria [OAK✓].
- *Onset:* delayed relative to myoclonus — "some years after the onset."
- PMID:18325013 **[VQ]**: *"Some years after the onset ataxia, incoordination, intentional tremor, and dysarthria develop."*

**Loss of ambulation** — `HP:0002505` [OAK✓]; *frequency* ≈1/3 within 5–10 years **[UNVERIFIED-BODY]**. Note the important counterweight from population data: ~10% of Finnish patients had a very mild course with decades of retained independence (PMID:32943486).

**Dysphagia** — `HP:0002015` [OAK✓]; late; mechanistically linked to the aspiration-pneumonia mortality pathway (see §11).

#### Cognitive / behavioral phenotypes

**Mild, slow cognitive decline** — `HP:0001268` Mental deterioration [OAK✓].
PMID:18325013 **[VQ]**: *"Individuals with EPM1 are mentally alert but show emotional lability, depression, and mild decline in intellectual performance over time."*
This is the key discriminator from Lafora disease and NCL, where dementia is early and severe.

**Emotional lability** — `HP:0000712` [OAK✓]; **Depression** — `HP:0000716` [OAK✓ / live HPO label confirmed "Depression"]. Both explicitly named in the sentence above; frequency qualitative ("show"), so per `docs/frequency-evidence-guidelines.md` I would **omit a `frequency:` band** rather than invent one.

Cognitive decline correlates with disease duration and earlier onset — PMID:25770194 **[VQ]**: *"An earlier age at onset for EPM1 and longer disease duration were associated with more severe action myoclonus, lower performance IQ, increased MT, and prolonged SP."*

#### Neurophysiological / laboratory phenotypes

- `HP:0010850` EEG with spike-wave complexes [OAK✓]; `HP:0002392` EEG with polyspike wave complexes [OAK✓]; `HP:0010852` EEG with photoparoxysmal response [OAK✓]; `HP:0011182` Interictal epileptiform activity [OAK✓].
- `HP:0001312` **Giant somatosensory evoked potentials** [OAK✓] — the classic cortical-hyperexcitability marker of cortical myoclonus (curate as `category: Cellular`/neurophysiological with `evidence_source: HUMAN_CLINICAL`).
- **Reduced short-interval intracortical inhibition (SICI)** on TMS — a *measurable GABAergic deficit*. PMID:36398398 **[VQ]**: *"Compared to controls, patients demonstrated significantly less SICI (median mSICI ratio 1.18 vs 0.38; p < .001)."* No exact HP term; curate as a biochemical/neurophysiological readout or with `preferred_term: Reduced short-interval intracortical inhibition` bound to a broader HP parent.

#### Imaging phenotypes

- `HP:0002120` Cerebral cortical atrophy [OAK✓] — specifically motor-network. PMID:19704079 **[VQ]**: *"VBM analysis revealed atrophy in the bilateral primary, premotor, and supplementary motor cortex. The thalamus and precuneus were also bilaterally affected."*
- `HP:0001272` Cerebellar atrophy [OAK✓] — present in longer-standing/severe disease; notably *absent* from the group-level VBM analysis in the Koskenkorva cohort (*"No infratentorial changes were detected in the group analysis."* **[VQ]**), so curate with a modifier and don't overstate frequency.
- Routine clinical brain MRI is characteristically **normal** at diagnosis — a differential-diagnostic point.

#### Rare severe-variant phenotype (genotype-specific)

Homozygous *CSTB* frameshift produces a phenotype barely recognizable as classic ULD — profound developmental delay, microcephaly, cortical blindness, diffuse hypomyelination, no head control (PMID:28378817). Curate as a distinct `has_subtypes` entry (suggested `name: Severe null phenotype`) rather than folding into the main phenotype list.

---

## 4. Genetic / Molecular Information

### Causal gene

**CSTB** (cystatin B; stefin B) — `hgnc:2482` [OAK✓], `NCBIGene:1476`, `OMIM:601145`, `UniProt:P04080`, chromosome **21q22.3**, protein length **98 aa**. UniProt function: *"This is an intracellular thiol proteinase inhibitor. Tightly binding reversible inhibitor of cathepsins L, H and B."* Subcellular locations recorded: **cytoplasm, nucleus**.

The paralogous distinction matters for curation: CSTB is a **type 1 cystatin (stefin)** — no signal peptide, no disulfides — yet it is nevertheless found extracellularly in CSF (see the secretion finding in §6).

### Pathogenic variant classes

**(1) Dodecamer promoter repeat expansion — ~90% of pathogenic alleles.**

Repeat unit: `CCCCGCCCCGCG`. Allele-size tiers (GeneReviews; **[UNVERIFIED-BODY]** for the exact tier boundaries, but corroborated by primary sources below):

| Repeat copies | Interpretation |
|---|---|
| 2–3 | Normal |
| 12–17 | Premutation / uncertain significance; **markedly unstable in transmission** (PMID:9126745 **[VQ]**) |
| 18–29 | *Not observed* — a genuine gap in the allele-size distribution |
| ≥30 | Pathogenic, full penetrance |

Observed pathogenic sizes: **~30 to ~75 copies** (PMID:9529356 **[VQ]**: *"The largest detected expansion was approximately 75 copies; the smallest was approximately 30 copies."*); **38–77** in the Finnish nationwide cohort (PMID:25770194).

*Somatic/meiotic instability:* PMID:9529356 **[VQ]**: *"We identified affected siblings with repeat expansions, of different sizes, on the same haplotype, which confirms the repeat's instability during transmissions. Expansions were observed directly; contractions were deduced by comparison of allele sizes within a family."*

*Technical note for diagnostics:* expanded alleles are **GC-rich and PCR-refractory**; standard NGS panels and exome/genome sequencing miss them entirely. Deamination-based PCR protocols (PMID:14517952) and Southern blotting are required.

**(2) Point / indel variants — ~10% of alleles, usually compound-heterozygous with an expansion.**

Reported and well-supported examples:
- `c.202C>T` (p.Arg68Ter) — nonsense; the recurrent severe allele
- `c.67-1G>C` — 3′ splice-acceptor
- `c.149G>A` (p.Gly50Glu) — missense hitting the conserved **QVVAG** cathepsin-binding motif
- `c.168+1_18del` — 18-bp intronic deletion affecting splicing
- `c.116_117delAG` — novel indel, first Chinese ULD case (PMID:40442775)
- Homozygous frameshift — severe hypomyelination phenotype (PMID:28378817)

PMID:17003839 **[VQ]** on the missense mechanism: *"The p.G50E mutation that affects the conserved QVVAG amino acid sequence critical for cathepsin binding fails to associate with lysosomes. This further supports the previously implicated physiological importance of the CSTB-lysosome association."*

As of the 2025 review, **fewer than ~20 distinct pathogenic point/indel CSTB variants** have been reported worldwide (PMID:40442775 and the hiPSC study PMID:36359887).

**Origin:** exclusively **germline**. No somatic-mosaicism or COSMIC-type involvement.

**Functional consequence:** **loss of function via reduced expression**, not a structurally altered protein (for the expansion class). This is the crux — PMID:17003839 **[VQ]**:

> "Expression of CSTB mRNA and protein was markedly reduced in lymphoblastoid cells of the patients irrespective of the mutation type. Patients homozygous for the dodecamer expansion mutation showed 5-10% expression compared to controls."

So the expansion is a **hypomorph**: ~5–10% residual expression. That residual is likely why the expansion-homozygous phenotype is milder than the frameshift-null phenotype — a dose-of-protein relationship rather than an on/off switch.

**Allele frequency:** the dodecamer expansion is essentially absent from gnomAD-style short-read databases *by construction* (repeat expansions are not called by standard pipelines) — do not cite a gnomAD AF for it. Point variants are individually ultra-rare. Estimated **Finnish carrier frequency ~1 in 70** is derivable from the ~1:20,000 birth incidence under Hardy-Weinberg (q ≈ 0.007) — flag as *derived*, not directly measured.

### Genotype–phenotype correlations (an area of genuine, curatable disagreement)

**Compound heterozygotes (expansion + point variant) are more severely affected.** This is well replicated. PMID:21757863 **[VQ]**:

> "Age at onset of symptoms was significantly lower in the compound heterozygotes than in the homozygous EPM1 patients. They also had severer myoclonus and drug-resistant tonic-clonic seizures. Moreover, they had lower cognitive performance."

Independently confirmed in an Italian series (PMID:23205931; 6/52 families = 11.5% compound heterozygous) and in the 2025 Chinese report (PMID:40442775 **[VQ]**): *"By comparison with homozygous promoter expansions, we found an earlier age of first symptom onset and more refractory BTCS of ULD patients with compound or homozygous point/indel variants."*

**Repeat length vs. severity — conflicting evidence.** Curate this as a `mechanistic_hypotheses` disagreement, with `supports: SUPPORT` / `supports: REFUTE` evidence on both sides:

- **REFUTE:** PMID:9529356 **[VQ]** — *"In a sample of 28 patients, we found no correlation between age at onset of EPM1 and the size of the expanded dodecamer. This suggests that once the dodecamer repeat expands beyond a critical threshold, cystatin B expression is reduced in certain cells, with pathological consequences."* (threshold model)
- **PARTIAL/SUPPORT:** PMID:25770194 **[VQ]** — *"the actual size of the longer CSTB expansion mutation allele is likely to have a modulating effect on the age at disease onset, myoclonus severity, and cortical neurophysiology"* (n=66, larger and better powered; modulator model)
- **SUPPORT (neurophysiological endophenotype):** PMID:36398398 **[VQ]** — *"In participants with biallelic repeat expansions, the number of repeats in the more affected allele (greater repeat number [GRN]) correlated with LICI (rho = 0.872; p < .001) and SICI (rho = 0.689; p = .006)."*

The reconciliation most consistent with all three: a **threshold with a superimposed weak dose effect**, detectable only in large cohorts and most cleanly at the neurophysiological (not clinical) level.

### Modifier genes

- ***APOE* ε4** — PMID:41042579, 65 expansion-homozygous patients, 20 ε4 carriers. No difference in UMRS or disease duration; carriers had *better* QOLIE-31 emotional well-being (p=.047), energy/fatigue (p=.048), medical effects (p=.024), preserved hippocampal/amygdalar volume, but *more* cortical thinning and *more* white-matter degeneration. Genuinely ambiguous; curate as EMERGING.
- **Unidentified modifiers** — required to explain intrafamilial variability among siblings with matched repeat sizes. This is a good candidate for a `discussions` entry with `kind: KNOWLEDGE_GAP`.

### Epigenetics

The expansion is a **CpG-rich, GC-rich promoter element**, and hypermethylation of expanded alleles is the mechanistically obvious silencing route (and is exploited diagnostically — bisulfite/deamination-based PCR protocols, PMID:14517952). I did **not** retrieve a definitive primary paper quantifying methylation of expanded CSTB promoters in patient brain during this session; **treat promoter hypermethylation as a plausible but not-yet-verified mechanism and flag it as a knowledge gap.** What *is* established is a downstream chromatin effect — sustained histone H3 N-terminal tail clipping by unrestrained nuclear cathepsin L (PMID:36533126, §6).

### Chromosomal abnormalities

None characteristic. EPM1 is not a CNV/microdeletion disorder; chromosomal microarray has no diagnostic role except to exclude alternatives.

---

## 5. Environmental Information

Essentially **not applicable as an etiology**. Curate explicitly as negative to prevent downstream inference errors:

- **Toxins/occupational/radiation:** no established role.
- **Lifestyle:** no dietary, smoking, or exercise factor causes EPM1. Physical exertion and stress *provoke* myoclonus symptomatically (a trigger, not a risk factor). Photic environments (strobes, flickering screens, sunlight through trees) provoke both myoclonus and seizures.
- **Infectious agents:** none causal. Infections matter at the *other* end — lower respiratory tract infection is the leading immediate cause of death (56% of deaths, PMID:32943486).
- **Iatrogenic:** the one genuinely modifiable exposure. See §12.

---

## 6. Mechanism / Pathophysiology

Here is the causal chain as best supported, upstream → downstream. The honest summary: **CSTB is a brake on cysteine cathepsins, and EPM1 is what happens when you take a cell's protease brake pads down to 5–10% of spec.** Proteolysis that should be confined to the lysosome starts leaking into the cytosol and the nucleus; neurons lose their oxidative-stress reserve; microglia switch on early and stay on; inhibitory circuits thin out; and the cortex ends up chronically hyperexcitable while slowly losing cells.

### 6.1 Molecular trigger — loss of cathepsin inhibition

CSTB reversibly and tightly inhibits cathepsins **B, H, and L** (UniProt P04080) via the conserved **QVVAG** wedge. In EPM1, expression falls to 5–10% (PMID:17003839), releasing cathepsin activity.

- GO: `GO:0004869` cysteine-type endopeptidase inhibitor activity [OAK✓]; `GO:0006508` proteolysis [OAK✓]; `GO:0005764` lysosome [OAK✓]
- CHEBI/protein targets: cathepsin B, cathepsin L, cathepsin H
- Corroborating in-vitro human data: patient-derived hiPSC neurons show *"an increased expression of lysosomal cathepsins (B, D, and L) and a reduced expression of CSTB protein"* (PMID:36359887) **[UNVERIFIED-BODY — from the article body/summary; re-verify against abstract before curation]**

### 6.2 Redox failure — the best-characterized death pathway

This is the mechanistic keystone, and it has a lovely feed-forward cruelty to it: oxidative stress normally *induces* CSTB, and the EPM1 promoter mutation specifically breaks that induction. The cell's fire extinguisher is bolted shut precisely by the fire.

PMID:19420257 **[VQ]** (the whole causal chain in one abstract):

> "Here, we report impaired redox homeostasis as a key mechanism by which Cystatin B deficiency triggers neurodegeneration. Oxidative stress induces the expression of Cystatin B in cerebellar granule neurons, and EPM1 patient-linked mutation of the Cystatin B gene promoter impairs oxidative stress induction of Cystatin B transcription. Importantly, Cystatin B knockout or knockdown sensitizes cerebellar granule neurons to oxidative stress-induced cell death. The Cystatin B deficiency-induced predisposition to oxidative stress in neurons is mediated by the lysosomal protease Cathepsin B. We uncover evidence of oxidative damage, reflected by depletion of antioxidants and increased lipid peroxidation, in the cerebellum of Cystatin B knock-out mice in vivo."

- GO: `GO:0006979` response to oxidative stress [OAK✓]; `GO:0051402` neuron apoptotic process [OAK✓]; `GO:0043524` negative regulation of neuron apoptotic process [OAK✓]
- CL: `CL:0001031` cerebellar granule cell [OAK✓]
- Evidence classes: MODEL_ORGANISM + IN_VITRO (this is a mouse/CGN-culture study, **not** human clinical — tag accordingly)
- **Cathepsin B is the effector**, which makes it a rational drug target and is the mechanistic basis for antioxidant strategies (NAC).

Mitochondrial involvement (secondary amplifier): reduced SOD, glutathione, and catalase in mutant cerebellum, destabilized mitochondrial membrane potential, and proteomics showing mitochondrial proteins over-represented among differentially expressed synaptosomal proteins (PMID:38247861 review) **[UNVERIFIED-BODY]**.

### 6.3 Nuclear/chromatin arm — unrestrained cathepsin L clips histone H3

A distinct, non-lysosomal mechanism, and one of the more novel results in the field. PMID:36533126 **[VQ]**:

> "On the contrary, the brains of Cstb -/- mice showed sustained H3cs1 proteolysis to adulthood with increased chromatin-associated cathepsin L activity, implying that CSTB regulates chromatin-associated cathepsin L activity in the postnatal mouse brain."

Normal brain restricts H3 tail clipping to the first postnatal month; CSTB-deficient brain never turns it off. GO: `GO:0000785` chromatin [OAK✓]. The paper explored (but did not establish) a link to cellular senescence — *"the results remained inconclusive"* **[VQ]** — so curate the senescence link as a KNOWLEDGE_GAP rather than a mechanism.

### 6.4 Neurodevelopmental arm — CSTB is secreted and guides interneurons

This reframes EPM1 as partly a **developmental** disorder rather than purely degenerative. PMID:32378798 **[VQ]**:

> "We find that CSTB (but not one of its pathological variants) is secreted into the mouse cerebral spinal fluid and the conditioned media from hCOs. In embryonic mouse brain, we find that functional CSTB influences progenitors' proliferation and modulates neuronal distribution by attracting interneurons to the site of secretion via cell-non-autonomous mechanisms. Similarly, in patient-derived hCOs, low levels of functional CSTB result in an alteration of progenitor's proliferation, premature differentiation, and changes in interneurons migration."

- Evidence classes: MODEL_ORGANISM (mouse) + **IN_VITRO on human patient-derived cerebral organoids** — the strongest human-relevant mechanistic evidence available
- CL: `CL:0011005` GABAergic interneuron [OAK✓]; `CL:0010011` cerebral cortex GABAergic interneuron [OAK✓]

### 6.5 GABAergic disinhibition — the seizure mechanism proper

**Mouse:** PMID:24586687 **[VQ]**:

> "Electrophysiological recordings from Cstb(-/-) cerebellar Purkinje cells revealed a shift of the balance towards decreased inhibition, yet the amount of inhibitory interneurons was not declined in young animals. Instead, we found diminished number of GABAergic terminals and reduced ligand binding to GABAA receptors in Cstb(-/-) cerebellum. These results suggest that alterations in GABAergic signaling could result in reduced inhibition in Cstb(-/-) cerebellum leading to the hyperexcitable phenotype of Cstb(-/-) mice."

Note the *sequence*: **synaptic terminal loss and receptor binding loss come before interneuron loss.** Early disease is a synaptic problem; interneuron depletion is later.

**Human:** PMID:36398398 **[VQ]**: *"Our results strengthen the finding of deranged γ-aminobutyric acid (GABA)ergic inhibition in EPM1. LICI and SICI may have use as markers of GABAergic impairment in future trials of disease-modifying treatment in this condition."*

- GO: `GO:0007214` gamma-aminobutyric acid signaling pathway [OAK✓]
- CL: `CL:0000617` GABAergic neuron [OAK✓]; `CL:0000121` Purkinje cell [OAK✓]
- This is the natural `conforms_to` anchor for `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`.

### 6.6 Neuroinflammation — microglia fire first

Timing is the whole point here: microglial activation is not reactive cleanup after neuron death, it *precedes* both neuron loss and the first myoclonus. Whether it's causal or merely a very early sentinel is the open question.

PMID:22157618 **[VQ]**:

> "Our data reveal early and localized glial activation in brain regions where neuron loss subsequently occurs. These changes are most pronounced in the thalamocortical system, with neuron loss occurring first within the cortex and only subsequently in the corresponding thalamic relay nucleus. Microglial activation precedes the emergence of myoclonia and is followed by successive astrocytosis and selective neuron loss. Neuron loss was not detected in thalamic relay nuclei that displayed no glial activation."

Microglial phenotype dynamics — PMID:25327891 **[VQ]**:

> "Our results show significantly higher Cstb mRNA expression in microglia than in neurons and astrocytes. ... M1/M2 polarization of microglia in presymptomatic Cstb(-/-) mice is, compared to control mice, skewed towards M2 type at postnatal day 14 (P14), but towards M1 type at P30, a time point associated with onset of myoclonus."

So there is a **polarization flip that coincides with symptom onset** — a candidate therapeutic window. (Caveat for curation: M1/M2 is now regarded as an oversimplified framework; report it as the authors did but don't over-interpret.)

Peripheral extension — PMID:27894304 **[VQ]**:

> "We found higher concentrations of chemokines and pro-inflammatory cytokines in the serum of Cstb -/- mice and higher CXCL13 expression in activated microglia in Cstb -/- compared to control mouse brains. The elevated chemokine levels were not accompanied by blood-brain barrier disruption, despite increased brain vascularization."

- GO: `GO:0001774` microglial cell activation [OAK✓]; `GO:0006954` inflammatory response [OAK✓]
- CL: `CL:0000129` microglial cell [OAK✓]; `CL:0000127` astrocyte [OAK✓]
- Transcriptomic corroboration — PMID:24586687 **[VQ]**: *"At P30, the microarray data revealed a marked upregulation of immune and defense response genes, compatible with the previously reported early glial activation that precedes neuronal degeneration."*

### 6.7 Cell death — cerebellar granule cell apoptosis

PMID:9806543 **[VQ]**:

> "We found that mice lacking cystatin B develop myoclonic seizures and ataxia, similar to symptoms seen in the human disease. The principal cytopathology appears to be a loss of cerebellar granule cells, which frequently display condensed nuclei, fragmented DNA and other cellular changes characteristic of apoptosis. This mouse model of EPM1 provides evidence that cystatin B, a non-caspase cysteine protease inhibitor, has a role in preventing cerebellar apoptosis."

### 6.8 Synaptic and developmental transcriptomics

PMID:24586687 **[VQ]**: *"Differentially expressed genes in P7 cerebella were connected to synaptic function and plasticity, and in cultured cerebellar granule cells, to cell cycle, cytoskeleton, and intracellular transport."*

### Proposed dismech pathophysiology chain (node sketch)

```
CSTB Loss of Function (MOLECULAR)
  → Cathepsin B/L/H Disinhibition (MOLECULAR)
      → Impaired Oxidative Stress Response (CELLULAR)   [GO:0006979]
      → Nuclear Cathepsin L Histone H3 Clipping (MOLECULAR) [GO:0000785]
      → Impaired Interneuron Migration & Progenitor Proliferation (CELLULAR)
  → Early Microglial Activation (CELLULAR)              [GO:0001774]
      → Astrocytosis and Neuroinflammation (TISSUE)     [GO:0006954]
  → GABAergic Synaptic Deficit (CELLULAR)               [GO:0007214]
      → Cortical Hyperexcitability / E-I Imbalance (TISSUE)
          → Action- and Stimulus-Sensitive Myoclonus (ORGANISM)  [HP:0001336]
          → Generalized Tonic-Clonic Seizures (ORGANISM)         [HP:0002069]
  → Cerebellar Granule Neuron Apoptosis (CELLULAR)      [GO:0051402]
      → Cerebellar and Thalamocortical Atrophy (TISSUE) [HP:0001272, HP:0002120]
          → Progressive Ataxia / Dysarthria (ORGANISM)  [HP:0001251, HP:0001260]
```

**Suggested module conformance:** `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance` (strong fit) and `cerebellar_purkinje_degeneration#Purkinje Neuron Degeneration` (partial fit — EPM1's cerebellar loss is *granule-cell*-predominant with secondary Purkinje involvement, so document the substitution explicitly rather than forcing it).

### Molecular profiling summary

| Modality | Finding | Source |
|---|---|---|
| Transcriptomics | Cerebellar microarray: P7 synaptic/plasticity genes; P30 immune/defense upregulation; GABAergic pathway hit | PMID:24586687 |
| Proteomics | Synaptosome proteomics: ~1/3 of DE proteins mitochondrial; ribosomal + intracellular transport altered | PMID:38247861 **[UNVERIFIED-BODY]** |
| Proteomics (human organoid) | *"Secretion and extracellular matrix organization are the biological processes particularly affected as suggested by a proteomic analysis in patients' hCOs"* **[VQ]** | PMID:32378798 |
| Metabolomics / lipidomics | Not systematically profiled — **knowledge gap** | — |
| Single-cell / spatial | Not reported for EPM1 — **knowledge gap** | — |
| CRISPR/RNAi screens | Targeted RNAi only (CSTB and CTSB knockdown, PMID:19420257); no genome-wide screen published | — |
| Structural | PDB 1STF (stefin B–papain complex), 2OCT, 4N6V | UniProt P04080 |

---

## 7. Anatomical Structures Affected

### Organ / system level

- **Primary:** central nervous system. Body system: nervous system exclusively.
- **Secondary:** respiratory system (aspiration pneumonia from dysphagia/immobility — the mortality pathway); musculoskeletal (contractures, deconditioning from immobility).
- **Not involved:** liver, kidney, heart, skin, eye (contrast with Lafora — skin biopsy positive; with NCL — retinal degeneration; with sialidosis — cherry-red spot). This negative profile is diagnostically load-bearing.

### Regional CNS localization (UBERON)

| Structure | UBERON | Evidence |
|---|---|---|
| Cerebellum | `UBERON:0002037` [OAK✓] | granule cell apoptosis, PMID:9806543 |
| Cerebellar cortex | `UBERON:0002129` [OAK✓] | GABAergic terminal loss, PMID:24586687 |
| Cerebral cortex | `UBERON:0000956` [OAK✓] | VBM atrophy, PMID:19704079 |
| Primary motor cortex | `UBERON:0001384` [OAK✓] | *"bilateral primary, premotor, and supplementary motor cortex"* **[VQ]** PMID:19704079 |
| Thalamus (dorsal plus ventral) | `UBERON:0001897` [OAK✓] | bilateral thalamic atrophy, PMID:19704079; thalamocortical system, PMID:22157618 |
| Hippocampal formation | `UBERON:0002421` [OAK✓] | volumetry, APOE study PMID:41042579 |
| Precuneus | (needs OAK lookup) | PMID:19704079 |

**The thalamocortical system is the anatomical epicenter**, which maps neatly onto the myoclonus phenotype. PMID:19704079 **[VQ]**: *"The cortical motor areas of the brain are particularly affected in EPM1, correlating with the motor symptoms of this disease."*

### Tissue and cell level (CL)

- `CL:0001031` cerebellar granule cell [OAK✓] — principal dying population
- `CL:0000121` Purkinje cell [OAK✓] — secondary loss; site of the recorded inhibitory-balance shift
- `CL:0011005` GABAergic interneuron [OAK✓] / `CL:0010011` cerebral cortex GABAergic interneuron [OAK✓] — depleted in cortex; migration disrupted developmentally
- `CL:0000129` microglial cell [OAK✓] — **highest CSTB expression of the three cell classes tested** (PMID:25327891); earliest activated
- `CL:0000127` astrocyte [OAK✓] — secondary astrocytosis; CSTB is lysosomal in astrocytes
- Oligodendrocytes — implied by the hypomyelination phenotype in the severe frameshift case (PMID:28378817)

### Subcellular level (GO cellular component)

- `GO:0005764` lysosome [OAK✓] — CSTB–lysosome association is functionally required (p.G50E abolishes it, PMID:17003839)
- Cytoplasm and nucleus (UniProt P04080 subcellular locations)
- `GO:0000785` chromatin [OAK✓] — nuclear cathepsin L target compartment
- Mitochondrion — CSTB reported in rat cerebellar granule cell mitochondria; mitochondrial protein/bioenergetic changes in synaptosomes **[UNVERIFIED-BODY]**
- Synapse/synaptosome — GABAergic terminals; Kif1a-dependent transport

### Lateralization

**Bilateral and broadly symmetric** — VBM atrophy was bilateral in primary/premotor/supplementary motor cortex, thalamus, and precuneus (PMID:19704079). Myoclonus is multifocal-to-generalized, not lateralized.

---

## 8. Temporal Development

### Onset

- **Typical age:** 6–16 years (pediatric/juvenile). `HP:0003621` Juvenile onset [OAK✓], 29/29 in HPO annotations.
- **Best population-based figure:** mean **9.4 ± 2.3 years**, range **7.0–14.6 years**, no sex difference (n=135, Finland; PMID:32943486 **[VQ]**).
- Different source ranges reflect ascertainment: 6–15 (PMID:9090386), 6–13 (PMID:9126745), 6–16 (PMID:18325013, PMID:9529356).
- **Onset pattern:** insidious/subacute. Roughly half present with myoclonus, half with GTCS.
- **Earlier onset in compound heterozygotes** (PMID:21757863).
- EEG abnormality can **precede clinical onset** **[UNVERIFIED-BODY, GeneReviews]**: *"EEG is always abnormal, even before the onset of manifestations."*

### Disease stages (proposed for curation)

1. **Presymptomatic** — normal development; EEG may already be abnormal.
2. **Early / seizure-predominant** (onset to ~2 y) — GTCS ± emerging myoclonus; myoclonus initially morning-predominant and stimulus-triggered.
3. **Intermediate / myoclonus-predominant** (~2–10 y) — GTCS often come under control while action myoclonus worsens; ataxia, intention tremor, dysarthria emerge; UMRS scores climb; mild cognitive slowing.
4. **Advanced** (~5–15 y+) — severe action myoclonus limiting all voluntary movement; ~1/3 wheelchair-dependent within 5–10 years; dysphagia; dependence for ADLs.
5. **Late/end-stage** — immobility, aspiration risk, respiratory infection.

### Progression rate and course

- **Course:** chronic, lifelong, **progressive** — but with a striking severity spread. PMID:32943486 **[VQ]**: *"In approximately 10% of all cases, the disease progression appeared very mild; some patients retained functional independence for decades."*
- **Rate correlates with onset age and duration** — PMID:25770194 **[VQ]**: *"As a group, earlier disease onset and longer duration are associated with more severe phenotype."*
- Historically the disease was considered relentlessly fatal in early adulthood; contemporary care has substantially altered the trajectory (see §11).
- **Remission:** no spontaneous remission of myoclonus. Treatment-induced remission of *generalized seizures* is common and clinically expected; myoclonus responds only partially.

### Critical periods

- **Developmental window (prenatal/early postnatal):** the interneuron-migration and progenitor-proliferation defects (PMID:32378798) occur before symptom onset — implying that any future disease-modifying or gene-directed therapy has a component of damage already fixed at birth. Important caveat for gene-therapy expectations.
- **Presymptomatic inflammatory window:** microglial activation precedes myoclonus in the mouse, with the M2→M1 flip at P30 coinciding with onset (PMID:22157618, PMID:25327891). This is the single most-cited candidate intervention window.
- **Diagnosis-to-first-prescription window:** avoiding the aggravating drugs before they are ever started is the highest-yield practical intervention point.

---

## 9. Inheritance and Population

### Inheritance

**Autosomal recessive** (`HP:0000007` [OAK✓]). Sibling recurrence risk 25%; carrier risk 50% for unaffected sibs. Penetrance appears **complete** for biallelic ≥30-repeat genotypes; **expressivity is variable**, including intrafamilially.

- **Anticipation:** not classically demonstrated in the clinical sense, *but* the repeat is unstable in transmission — premutation alleles (12–17 copies) *"show marked instability when transmitted to offspring"* (PMID:9126745 **[VQ]**), and same-haplotype siblings carry differently sized expansions (PMID:9529356). Curate as **repeat instability without established clinical anticipation** — an important distinction from DM1/HD.
- **Germline mosaicism:** not documented; the instability data make it biologically plausible. Knowledge gap.
- **Founder effect:** yes, and a striking one — PMID:9090386 **[VQ]**: *"Haplotype data are compatible with a single ancestral founder mutation."*
- **Consanguinity:** relevant for the rare homozygous point/frameshift genotypes (PMID:28378817).
- **Carrier frequency:** ~1/70 in Finland (derived from 1:20,000 birth incidence; flag as derived).

### Epidemiology — structured prevalence records

The Finnish nationwide study is the gold standard here (PMID:32943486, all patients treated 1998–2016) **[VQ]**:

> "A total of 135 persons with EPM1 (54% women) were identified and 105 were alive on December 31, 2016 (point prevalence 1.91/100,000 persons). The age-standardized (European Standard Population 2013) prevalence was 1.53/100,000 persons. Annual incidence during the study period was 0.022/100,000 person-years, with a mean age at onset of 9.4 ± 2.3 years (range 7.0-14.6 years, no sex difference)."

Suggested `prevalence:` records:

```yaml
prevalence:
- population: Finland
  measure_type: POINT_PREVALENCE
  prevalence_class: BAND_1_9_PER_100000
  rate_per_100000: 1.91
  notes: Nationwide registry point prevalence, 105 living patients on 2016-12-31.
  evidence:
  - reference: PMID:32943486
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: "105 were alive on December 31, 2016 (point prevalence 1.91/100,000 persons)"
- population: Finland
  measure_type: ANNUAL_INCIDENCE
  prevalence_class: BELOW_1_IN_1000000
  rate_per_100000: 0.022
- population: Finland
  measure_type: BIRTH_PREVALENCE
  prevalence_class: BAND_1_9_PER_100000
  rate_per_100000: 5.0
  notes: Orphanet birth-prevalence value/class for Finland (≈1 in 20,000 births).
  evidence:
  - reference: ORPHA:308
- population: Worldwide
  measure_type: POINT_PREVALENCE
  prevalence_class: ULTRA_RARE
  notes: >-
    No reliable global estimate; EPM1 is the most common PME but is rare
    outside Finland and the western Mediterranean.
```

Orphanet (ORPHA:308) records: **birth prevalence 1–9/100,000 (value 5.0), Finland**; **point prevalence 1–9/100,000 (value 2.0), Finland** — both sourced to `PMID:20301321` (GeneReviews).

The 1:20,000 Finnish birth figure traces to PMID:9126745 **[VQ]**: *"It is a rare disorder but more common in Finland (1 in 20,000) and the western Mediterranean."*

### Population demographics

- **Highest prevalence:** Finland. PMID:32943486 **[VQ]**: *"Unverricht-Lundborg disease is rare in Finland but still more common than anywhere else in the world. The disease course appears somewhat more severe than elsewhere, disability mounts early, and death occurs prematurely."*
- **Other clusters:** western Mediterranean / Maghreb — Tunisia, Algeria, Morocco (reflected in the author rosters of PMID:9529356: Ouazzani, M'Rabet, Gouider, Chkili); Italy (large Besta/Genoa series, PMID:23205931); historically Estonia, Latvia, and the Baltic region ("Baltic myoclonus").
- **Rare in East Asia:** the first Chinese case was reported only in 2025 (PMID:40442775) **[VQ]**: *"The best-known area for ULD are the shores of the Baltic and Mediterranean Sea and few cases have been recorded from Asia."*
- **Sex ratio:** ~1:1. Finnish cohort 54% women; Hyppönen cohort exactly 33 men / 33 women. No sex difference in onset age or age at death.
- **Age distribution:** onset juvenile; prevalent population spans adolescence through the sixth decade.
- **Variant geography:** the dodecamer expansion is on a shared ancestral haplotype worldwide; `c.202C>T` recurs in Finland; the point/indel variants are private/population-specific.

---

## 10. Diagnostics

### Clinical criteria

Diagnosis is clinical + neurophysiological + molecular. The clinical gestalt: **juvenile-onset stimulus-sensitive action myoclonus + GTCS + later ataxia + relatively preserved cognition + normal brain MRI.**

Molecular confirmation is required. GeneReviews criteria **[UNVERIFIED-BODY]**: biallelic abnormal dodecamer repeat expansions, **or** compound heterozygosity for an expansion plus a sequence variant.

### Electrophysiology (highest-yield non-genetic testing)

- **EEG:** always abnormal; photosensitive generalized spike-and-wave and polyspike-and-wave paroxysms, labile/slowed background. `HP:0010850`, `HP:0002392`, `HP:0010852`, `HP:0011182` [all OAK✓]. **[UNVERIFIED-BODY, GeneReviews]**: *"photosensitive, generalized spike-and-wave and polyspike-and-wave paroxysms."*
- **Somatosensory evoked potentials:** giant SEPs (`HP:0001312` [OAK✓]) — cortical myoclonus signature.
- **TMS (research/emerging):** reduced SICI; `mSICI` ratio 1.18 vs 0.38 in controls (p<.001), PMID:36398398. Proposed as a **GABAergic biomarker for disease-modifying trials** — a strong candidate for a dismech `biochemical`/functional readout with `reference_ranges` once a normative interval is published.
- **Back-averaged EEG-EMG polygraphy** for cortical myoclonus characterization (PMID:23205931).

### Imaging

- **Brain MRI:** characteristically **normal** on routine clinical reading — its main role is exclusion.
- **Quantitative MRI (research):** VBM atrophy of bilateral primary/premotor/supplementary motor cortex, thalamus, precuneus (PMID:19704079, 34 patients vs 30 controls); DTI shows reduced FA and increased MD in white matter (PMID:41042579).

### Genetic testing (the decision tree that matters)

**The single most important diagnostic caveat:** ⚠️ **exome and genome sequencing miss the causative variant in ~90% of patients.** The GC-rich promoter expansion is invisible to standard short-read pipelines. GeneReviews **[UNVERIFIED-BODY]**: *"Standard sequence-based panels and exome/genome sequencing cannot detect pathogenic repeat expansions."*

Recommended approach:
1. **Targeted dodecamer repeat expansion analysis** — Southern blot or specialized/deamination-based PCR (PMID:14517952, PMID:17003839). Detects ~90% of alleles.
2. **CSTB sequence analysis** — adds ~10%; essential for the second allele in compound heterozygotes. In Finland, combined testing reaches ~99% **[UNVERIFIED-BODY]**.
3. **PME gene panel** (must include CSTB *plus* an orthogonal repeat assay) — reasonable first-line where the phenotype is ambiguous; covers EPM2A, NHLRC1, KCNC1, SCARB2, GOSR2, PRICKLE1, CLN genes, NEU1, POLG.
4. **WES/WGS** — appropriate only to find non-CSTB causes or the point-variant allele; **never sufficient alone to exclude EPM1**.
5. Not indicated: chromosomal microarray, karyotype, FISH, mtDNA testing (except to exclude MERRF).

### Laboratory / biopsy

- No diagnostic blood or urine biomarker. Routine labs normal.
- Research-grade: CSTB mRNA/protein quantification in lymphoblastoid cells (5–10% of control in expansion homozygotes, PMID:17003839).
- **Skin biopsy** — negative for Lafora bodies; **useful specifically to exclude Lafora disease**. Absence of storage material also distinguishes from NCL.
- **Muscle biopsy** — no ragged-red fibers (excludes MERRF).
- Autopsy neuropathology: cerebellar granule cell and Purkinje cell loss; **no storage material** — this negative is the pathological hallmark.

### Differential diagnosis

| Condition | Gene | Distinguishing features |
|---|---|---|
| **Lafora disease** | *EPM2A*, *NHLRC1* | Rapid dementia, visual seizures, Lafora bodies on skin biopsy, death within ~10 y |
| **MEAK** (myoclonic epilepsy and ataxia due to K⁺ channel mutation) | *KCNC1* (p.Arg320His, de novo) | Dominant/de novo; clinically near-identical to ULD — Crespel's perampanel series deliberately included one such patient (PMID:28166365) |
| **Action myoclonus–renal failure** | *SCARB2* | Proteinuria/renal failure |
| **North Sea PME** | *GOSR2* | Early ataxia, scoliosis, areflexia, elevated CK |
| **EPM1B** | *PRICKLE1* | OMIM 612437; Orphanet maps it *under* ORPHA:308 |
| **Neuronal ceroid lipofuscinoses** | *CLN* genes | Visual loss, storage material, dementia |
| **MERRF** | mtDNA *MT-TK* | Maternal inheritance, ragged-red fibers, lactate |
| **Sialidosis type I** | *NEU1* | Cherry-red spot, urinary oligosaccharides |
| **Gaucher disease type 3** | *GBA1* | Organomegaly, supranuclear gaze palsy, low glucocerebrosidase (PMID:34991910) |
| **DRPLA** | *ATN1* CAG | Dominant, anticipation, choreoathetosis |
| **Juvenile myoclonic epilepsy** | polygenic | Non-progressive; no ataxia — the most common *early* misdiagnosis |

### Screening

- **No newborn screening** anywhere (no treatable metabolic marker, and the causative expansion is not amenable to standard NBS assays).
- **Carrier screening:** technically feasible in Finland given the founder haplotype; not currently a population program.
- **Cascade testing** of at-risk relatives once both familial alleles are known — standard of care.
- **Prenatal / preimplantation genetic testing:** available once both parental variants are identified **[UNVERIFIED-BODY, GeneReviews]**.

---

## 11. Outcome / Prognosis

### Survival and mortality — the best data in the field

All from PMID:32943486 (Finnish nationwide, n=135, 34 deaths) **[VQ]**:

> "The median age at death (n = 34) was 53.9 years (interquartile range 46.4, 60.3; range 23.2-63.8), with no sex differences. The immediate cause of death was a lower respiratory tract infection in 56% of deaths. The survival rates of the patients were comparable to matched controls up to 40 years of age, but poorer during long-term follow-up (cumulative survival 26.4% vs 78.0%), with a hazard ratio (HR) for death of 4.61. The risk of death decreased with increasing age at onset (HR 0.76 per year, 95% confidence interval 0.65-0.89)."

Key structured facts for the KB:
- **Median age at death: 53.9 y** (IQR 46.4–60.3; range 23.2–63.8)
- **Leading immediate cause of death: lower respiratory tract infection, 56%**
- **Survival equals matched controls up to ~40 y**, then diverges sharply (cumulative survival 26.4% vs 78.0%)
- **HR for death: 4.61**
- **Protective gradient: HR 0.76 per additional year of onset age** (95% CI 0.65–0.89) — later onset is strongly prognostic
- Historical comparison **[UNVERIFIED-BODY, GeneReviews]**: many patients formerly died 8–15 years after onset, before age 30 — i.e., modern care has roughly doubled survival.

### Morbidity, disability, function

- ~1/3 wheelchair-dependent within 5–10 years of onset **[UNVERIFIED-BODY]**; contrast the ~10% very-mild subgroup with decades of independence (PMID:32943486). The distribution is genuinely bimodal-ish, not a single trajectory.
- Disability is driven by **action myoclonus**, not by seizures — the seizures usually respond to medication; the jerks do not.
- **Cognitive:** mild, slow decline; most patients retain insight and normal-range function, which contributes to high rates of depression.
- **QoL instruments used in EPM1:** **QOLIE-31** (epilepsy-specific), **UMRS** (myoclonus severity), **WAIS-R** (intellectual ability) — all three used in PMID:41042579. No EPM1-specific PROM exists — a knowledge gap.

### Complications

Aspiration pneumonia and lower respiratory infection (the mortality pathway); myoclonic status epilepticus; falls and injury; depression; drug-induced aggravation of myoclonus; medication adverse effects (perampanel behavioral effects in 50%, PMID:28166365).

### Prognostic factors

| Factor | Direction | Source |
|---|---|---|
| Later age at onset | **Protective** (HR 0.76/y for death) | PMID:32943486 |
| Earlier age at onset | Worse myoclonus, lower performance IQ, higher motor threshold | PMID:25770194 |
| Longer disease duration | Worse | PMID:25770194 |
| Compound heterozygosity (expansion + point variant) | **Worse**: earlier onset, severer myoclonus, drug-resistant GTCS, lower cognition | PMID:21757863, PMID:23205931, PMID:40442775 |
| Larger expansion allele (GRN) | Modulating only; correlates with TMS inhibition measures | PMID:25770194, PMID:36398398 (vs. no correlation in PMID:9529356) |
| *APOE* ε4 | Ambiguous — better self-reported QoL, more WM degeneration | PMID:41042579 |
| Exposure to aggravating ASMs | **Worse** (potentially accelerates cerebellar degeneration) | PMID:18325013 |

### Prognostic biomarkers

No validated molecular prognostic biomarker. Candidates: TMS-derived SICI/LICI and motor threshold; quantitative MRI volumetry/DTI; UMRS trajectory. All research-grade.

---

## 12. Treatment

Treatment is **entirely symptomatic**. As Michelucci et al. put it (PMID:27629998) **[VQ]**: *"Moreover, treatment is only symptomatic, since therapy targeting the underlying aetiology for these genetic conditions is in its infancy."*

### First-line pharmacotherapy

**Valproic acid** — `CHEBI:39867` [OAK✓] (or sodium valproate `CHEBI:9925` [OAK✓]).
PMID:18325013 **[VQ]**: *"Valproic acid, the first drug of choice, diminishes myoclonus and the frequency of generalized seizures."*

```yaml
- name: Valproic Acid
  therapeutic_modality: SMALL_MOLECULE
  treatment_term:
    preferred_term: Pharmacotherapy
    term: {id: NCIT:C15986, label: Pharmacotherapy}
    therapeutic_agent:
    - preferred_term: valproic acid
      term: {id: CHEBI:39867, label: valproic acid}
```

### Add-on agents for myoclonus and seizures

| Drug | CHEBI | Evidence |
|---|---|---|
| **Clonazepam** | `CHEBI:3756` [OAK✓] | PMID:18325013 **[VQ]**: *"Clonazepam and high-dose piracetam are used to treat myoclonus"* |
| **Piracetam** | `CHEBI:32010` [OAK✓] | Best RCT evidence for myoclonus (below) |
| **Levetiracetam** | `CHEBI:6437` [OAK✓] | PMID:18325013 **[VQ]**: *"levetiracetam seems to be effective for both myoclonus and generalized seizures"* |
| **Perampanel** | `CHEBI:71013` [OAK✓] | PMID:28166365 (below) |
| **Topiramate** | `CHEBI:63631` [OAK✓] | PMID:27629998 **[VQ]**: *"Newer drugs which have been shown to be effective include piracetam, levetiracetam, topiramate, zonisamide"* |
| **Zonisamide** | `CHEBI:10127` [OAK✓] | same |
| **Brivaracetam** | `CHEBI:133013` [OAK✓] | RCTs negative (below) |
| Phenobarbital / primidone | (lookup) | PMID:27629998 **[VQ]**: *"Traditional antiepileptic drugs for the treatment of PMEs are valproate, clonazepam, and phenobarbital (or primidone)."* |

**Piracetam — the strongest myoclonus evidence, and it's a dose-response.** PMID:9527146 (randomized, double-blind, crossover, n=20 classical ULD) **[VQ]**:

> "Treatment with 24 g/day piracetam produced significant and clinically relevant improvement in the primary outcome measure of mean sum score (p=0.005) and in the means of its subtests of motor impairment (p=0.02), functional disability (p=0.003), and in global assessments by both investigator (p=0.002) and patient (p=0.01)."

and:

> "This study provides further evidence that piracetam is an effective and safe medication in patients with Unverricht-Lundborg disease. In addition, it shows that a dose of 24 g is highly beneficial, more effective than lower doses and that a dose-effect relation exists."

**Perampanel — striking open-label efficacy, real behavioral cost.** PMID:28166365 (n=12, 11 EPM1 + 1 KCNC1) **[VQ]**:

> "Ten patients had a clear clinical response of myoclonus, and five were able to reduce concomitant therapy. Improvement was noted sometimes as soon as with 2 mg/day. Epileptic seizures stopped on PER in the six patients who still had experienced generalized tonic-clonic or myoclonic seizures (100%). ... Weight gain was reported in six patients (50%). Psychological and behavioral side-effects were observed in six patients (50%) and led to withdrawal of PER in three cases and dose reduction in three."

Corroborated in the 2025 Chinese case at 2 mg/day, with a partial escape at 24 months (PMID:40442775).

**Brivaracetam — a well-run negative result worth curating as REFUTE evidence.** PMID:26666500, two phase III RCTs (N01187/NCT00357669, N01236/NCT00368251) **[VQ]**:

> "Estimated differences versus placebo were not statistically significant."

and:

> "Effect of BRV on action myoclonus was not statistically significant. However, action myoclonus score showed wide intrapatient variability and may not have been the optimal tool to measure severity of myoclonus in EPM1."

Long-term open-label extension (NCT00175916) included 94 ULD patients; 39.4% had ≥96 months of exposure, and 92.6% reported TEAEs (PMID:33461041) — i.e., tolerable and widely continued despite the failed primary endpoint, which is itself informative about the endpoint rather than the drug.

### ⚠️ Contraindicated / aggravating drugs (the most actionable clinical content)

PMID:18325013 **[VQ]**:

> "There are a number of agents that aggravate clinical course of EPM1 such as phenytoin aggravating the associated neurologic symptoms or even accelerating cerebellar degeneration. Sodium channel blockers (carbamazepine, oxcarbazepine) and GABAergic drugs (tiagabine, vigabatrin) as well as gabapentin and pregabalin may aggravate myoclonus and myoclonic seizures."

PMID:27629998 adds lamotrigine **[VQ]**:

> "When treating PMEs, particular care should be paid to avoid drugs known to aggravate myoclonus or myoclonic seizures, such as phenytoin, carbamazepine, oxcarbazepine, lamotrigine, vigabatrin, tiagabine, gabapentin, and pregabalin."

Phenytoin: `CHEBI:8107` [OAK✓]. This belongs in the entry as an explicit contraindication with `supports: SUPPORT` evidence.

### Neuromodulation and procedures

- **Vagus nerve stimulation:** reported to reduce seizures and improve cerebellar function **[UNVERIFIED-BODY, GeneReviews]**; also flagged as a discussed option in PMID:27629998 **[VQ]**: *"The potential of other drugs (such as L-triptophan and N-acetylcysteine) and procedures (such as vagal and deep brain stimulation) has also been discussed."*
- **Deep brain stimulation — negative for the GPi target.** PMID:38469950, title: *"Globus Pallidus Internus (GPi) Neuromodulation is Not Effective in Unverricht-Lundborg Disease to Control Myoclonia."* (Correspondence; abstract-free, so cite the title/PMID rather than quoting a snippet.) Curate as `supports: REFUTE`.

### Supportive and rehabilitative care

Lifelong multidisciplinary management. PMID:18325013 **[VQ]**:

> "Symptomatic pharmacologic and rehabilitative management, including psychosocial support, are the mainstay of EPM1 patients' care."

and:

> "EPM1 patients need lifelong clinical follow-up, including evaluation of the drug-treatment and comprehensive rehabilitation."

MAXO-annotatable components:
- Physical / occupational therapy — `MAXO:0000011` physical therapy [OAK✓]
- Speech-language therapy for dysarthria (MAXO term lookup needed)
- Feeding/swallow management to prevent aspiration (directly targets the 56%-of-deaths pathway)
- Psychosocial support and depression treatment
- Supportive care — `MAXO:0000950` [OAK✓]
- Genetic counseling — `MAXO:0000079` [OAK✓]
- Surgical procedure (VNS/DBS implantation) — `MAXO:0000004` [OAK✓]

### Experimental / investigational

- **N-acetylcysteine** — `CHEBI:28939` [OAK✓]. The mechanistic rationale is excellent (the redox pathway of PMID:19420257), the clinical evidence is anecdotal (PMID:27629998 lists it as "discussed"). Curate as EXPERIMENTAL with an explicit note that mechanism ≠ demonstrated efficacy.
- **L-tryptophan** — historical, discussed in PMID:27629998.
- **Cathepsin B inhibition** — rational target given *"The Cystatin B deficiency-induced predisposition to oxidative stress in neurons is mediated by the lysosomal protease Cathepsin B"* (PMID:19420257 **[VQ]**). No clinical program identified.
- **Anti-inflammatory / microglia-directed therapy** — rationale from the presymptomatic microglial-activation window (PMID:22157618, PMID:25327891). No trial identified.
- **Gene therapy / CSTB replacement / ASO** — **no published preclinical or clinical program found in this session's searches.** Given the hypomorphic (5–10% residual) mechanism, promoter-directed upregulation or gene addition is conceptually attractive; the developmental interneuron-migration defect (PMID:32378798) argues that postnatal restoration would not be fully corrective. Record as an explicit knowledge gap.
- **Registered trials:** NCT00357669, NCT00368251 (brivaracetam, completed, negative); NCT00175916 (long-term OLE).

### Pharmacogenomics

No CPIC/PharmGKB EPM1-specific guidance. Standard *CYP2C9*/*HLA-B\*15:02* considerations apply to the aggravating drugs (phenytoin, carbamazepine) — but in EPM1 those drugs are avoided for pharmacodynamic reasons anyway, which supersedes the PGx question.

### Treatment algorithm (synthesis)

1. Confirm genotype; **document that sodium-channel blockers and gabapentinoids are contraindicated** in the chart.
2. Start **valproate** (monitor for hepatic/teratogenic risk; in females of childbearing potential, weigh levetiracetam-first).
3. Add **clonazepam** and/or **levetiracetam** for residual myoclonus/seizures.
4. Add **high-dose piracetam** (up to 24 g/day, individualized) for action myoclonus.
5. Consider **perampanel** at low dose (2 mg) for refractory myoclonus, counseling explicitly about the ~50% rate of behavioral effects and titrating slowly.
6. Topiramate / zonisamide / phenobarbital as further add-ons.
7. Concurrent, non-optional: physiotherapy, OT, speech therapy, swallow assessment, depression screening and treatment, genetic counseling.
8. Reserve VNS for refractory cases; **do not offer GPi DBS** for myoclonia control on current evidence.

---

## 13. Prevention

- **Primary prevention:** not possible for a recessive Mendelian condition other than through reproductive genetics. **Genetic counseling** (`MAXO:0000079` [OAK✓]) with 25% sibling recurrence risk; carrier testing of partners in founder populations; **prenatal diagnosis and PGT** once both familial variants are known.
- **Secondary prevention (early detection):** no population screening exists or is currently justified. In practice, secondary prevention means *avoiding diagnostic delay and avoiding harmful first prescriptions* — a juvenile-onset myoclonic epilepsy that fails to behave like JME (progressive myoclonus, emerging ataxia, worsening on carbamazepine) should trigger PME workup including a repeat-expansion assay.
- **Tertiary prevention (the highest-yield category here):**
  - **Avoid aggravating ASMs** — phenytoin, carbamazepine, oxcarbazepine, lamotrigine, vigabatrin, tiagabine, gabapentin, pregabalin (PMID:18325013, PMID:27629998).
  - **Aspiration prevention** — swallow assessment, feeding programs, positioning, prompt treatment of respiratory infection. Given LRTI accounts for **56% of deaths**, this is arguably the single most life-extending intervention available.
  - **Fall/injury prevention** — home adaptation, mobility aids, helmet where appropriate.
  - **Photic trigger avoidance** — polarized lenses, screen management.
  - **Depression screening and treatment** — high burden in a cognitively intact population with progressive motor disability.
  - **Sustained physiotherapy** to preserve ambulation.
- **Immunization:** no disease-specific vaccine. **Routine influenza and pneumococcal vaccination is a rational, mechanism-aligned intervention** given the respiratory-infection mortality pattern — flag as *inferred clinical practice*, not as an EPM1-specific guideline recommendation, since I found no guideline explicitly stating it.
- **Public health / environmental:** not applicable.

---

## 14. Other Species / Natural Disease

- **Naturally occurring EPM1-equivalent disease in other species:** **none identified.** No OMIA entry for a CSTB-associated natural disease surfaced in this session's searching. Curate this as explicitly absent rather than unknown-and-omitted, and treat it as a soft knowledge gap (a targeted OMIA query is worth running before finalizing).
- **Orthologous genes:** mouse *Cstb* (chromosome 10) is the workhorse ortholog; CSTB/stefins are broadly conserved across vertebrates. The QVVAG cathepsin-binding motif is the conserved functional core — its disruption by p.Gly50Glu (PMID:17003839) is the cleanest evidence of functional conservation of that site.
- **Breed (VBO):** not applicable.
- **Comparative pathology:** the *Cstb*⁻ᐟ⁻ mouse reproduces myoclonus, motor disturbance, cerebellar granule cell apoptosis, glial activation, and progressive atrophy — a high-fidelity model of the *cellular* pathology, with caveats below.
- **Evolutionary conservation of mechanism:** cathepsin-inhibitor balance and redox coupling are deeply conserved; the *human-specific* element is the dodecamer promoter repeat itself, which has no mouse counterpart. **No mouse model of the actual human mutation exists** — every model is a null, not a hypomorph. Given that human expansion homozygotes retain 5–10% CSTB, this is a real construct-validity gap and a legitimate `HUMAN_MODEL_MISMATCH` discussion.
- **Zoonotic potential / cross-species transmission:** not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

### The flagship: *Cstb*⁻ᐟ⁻ mouse

Originating paper, PMID:9806543 **[VQ]**:

> "We found that mice lacking cystatin B develop myoclonic seizures and ataxia, similar to symptoms seen in the human disease. The principal cytopathology appears to be a loss of cerebellar granule cells, which frequently display condensed nuclei, fragmented DNA and other cellular changes characteristic of apoptosis."

**Phenotype recapitulation:**

| Human feature | Mouse | Source |
|---|---|---|
| Myoclonus | ✅ Yes, ~P30 onset; software-detectable from video | PMID:9806543, PMID:38179183 |
| Generalized seizures | ✅ Myoclonic seizures | PMID:9806543 |
| Cerebellar granule cell loss | ✅ Prominent, apoptotic | PMID:9806543 |
| Purkinje cell loss | ✅ Reported | PMID:38247861 **[UNVERIFIED-BODY]** |
| Cortical/thalamic atrophy | ✅ Thalamocortical, cortex-first | PMID:22157618 |
| GABAergic deficit | ✅ Reduced terminals + GABA_A binding | PMID:24586687 |
| Neuroinflammation | ✅ Early microglia → astroglia → neuron loss | PMID:22157618, PMID:25327891, PMID:27894304 |
| Oxidative damage | ✅ Antioxidant depletion + lipid peroxidation in vivo | PMID:19420257 |
| Ataxia | ⚠️ **Not reproduced on pure 129S2/SvHsd** | PMID:38179183 |

**Deep behavioral phenotyping caveat** — PMID:38179183 **[VQ]**:

> "Additionally, we observed that the mice were hyperactive and showed reduced startle response, problems in motor coordination and lack of inhibition. We were, however, not able to demonstrate an ataxic phenotype in them. This detailed behavioral phenotyping of the Cstb-/- mice reveals new aspects of this mouse model. The nature of the motor problems in the Cstb-/- mice seems to be more complex and more resembling the human phenotype than initially described."

Note the **reduced startle response** — the mouse is *hypo*-reactive where human patients are *stimulus-hyper*sensitive. That inversion is worth a `HUMAN_MODEL_MISMATCH` discussion entry: the model reproduces the cellular pathology well but the defining human clinical feature (stimulus sensitivity) is not straightforwardly recapitulated.

**Model limitations (curate as HUMAN_MODEL_MISMATCH):**
1. Null allele, not the human hypomorphic promoter expansion (no residual 5–10% protein).
2. No dodecamer-expansion knock-in exists; the human regulatory element has no mouse counterpart.
3. Ataxia absent on pure 129S2/SvHsd background — strain-background-dependent phenotype expression.
4. Startle response reduced, not enhanced.
5. Cognitive/affective features (depression, emotional lability) not modeled.
6. Human EPM1 spans decades; the mouse compresses it into months.

**Applications:** target validation (cathepsin B, redox, microglia), biomarker development, preclinical drug testing (the 2023 behavioral paper is co-authored by Orion Pharma R&D — i.e., built for screening), natural-history mapping of presymptomatic windows.

### Human cellular and organoid models (increasingly the primary human-relevant system)

- **Patient-derived cerebral organoids (hCOs)** — PMID:32378798. Establishes proliferation, premature differentiation, and interneuron-migration defects *in human tissue*, plus a proteomic signature of impaired secretion and ECM organization. `evidence_source: IN_VITRO`.
- **Patient-derived hiPSCs (two affected siblings)** — PMID:36359887; iPSC-derived neurons show increased cathepsin B/D/L and reduced CSTB **[UNVERIFIED-BODY]**.
- **Primary cerebellar granule neuron cultures** (mouse) with CSTB and CTSB RNAi — the redox mechanism system (PMID:19420257).
- **Primary microglial cultures** from *Cstb*⁻ᐟ⁻ mice — elevated chemokine release, enhanced chemotaxis, suppressed MHCII surface expression, impaired phagocytosis of apoptotic cells (PMID:25327891).
- **Lymphoblastoid cell lines** from patients — the source of the canonical 5–10% expression figure (PMID:17003839).

### Model systems NOT available

No zebrafish, *Drosophila*, *C. elegans*, or rat EPM1 model surfaced in this session's searching. No conditional/cell-type-specific *Cstb* allele or humanized (dodecamer knock-in) mouse identified. These are real, curatable gaps — a conditional microglia-specific *Cstb* knockout would directly test whether the early microglial activation is causal or merely the earliest visible symptom, which is currently the field's central unresolved question.

### Resources

MGI (*Cstb*, mouse), IMSR / IMPC for allele availability, Alliance of Genome Resources for orthology, Cellosaurus for the patient hiPSC lines.

---

## Curation Summary — Suggested Entry Skeleton

**Highest-confidence, fully-quotable evidence anchors (all abstract-verified this session):**

| Claim | PMID | Type |
|---|---|---|
| CSTB is the EPM1 gene; 21q22.3; reduced mRNA | 8596935 | HUMAN_CLINICAL |
| Dodecamer promoter expansion; 2–3 normal, >60 mutant; premutation 12–17 unstable | 9126745 | HUMAN_CLINICAL |
| Single ancestral founder haplotype | 9090386 | HUMAN_CLINICAL |
| Expansion range 30–75; no repeat-size/onset correlation | 9529356 | HUMAN_CLINICAL |
| 5–10% CSTB expression in expansion homozygotes; p.G50E fails lysosomal association | 17003839 | IN_VITRO |
| Clinical picture; drug of choice; aggravating drugs | 18325013 | HUMAN_CLINICAL |
| Compound heterozygotes more severe | 21757863 | HUMAN_CLINICAL |
| Nationwide epidemiology, survival, cause of death | 32943486 | HUMAN_CLINICAL |
| Repeat length modulates onset/severity/neurophysiology | 25770194 | HUMAN_CLINICAL |
| Reduced SICI; GRN correlates with LICI/SICI | 36398398 | HUMAN_CLINICAL |
| Motor cortex + thalamic VBM atrophy | 19704079 | HUMAN_CLINICAL |
| Piracetam 24 g/day RCT positive | 9527146 | HUMAN_CLINICAL |
| Brivaracetam RCTs negative | 26666500 | HUMAN_CLINICAL |
| Perampanel open-label efficacy + 50% behavioral AEs | 28166365 | HUMAN_CLINICAL |
| GPi DBS ineffective | 38469950 | HUMAN_CLINICAL (title only) |
| Cerebellar granule cell apoptosis in Cstb⁻ᐟ⁻ | 9806543 | MODEL_ORGANISM |
| Oxidative stress mechanism, cathepsin B-mediated | 19420257 | MODEL_ORGANISM / IN_VITRO |
| Microglia activate before neuron loss and myoclonus | 22157618 | MODEL_ORGANISM |
| M1/M2 flip at symptom onset; microglia highest Cstb | 25327891 | MODEL_ORGANISM / IN_VITRO |
| Peripheral inflammation, CXCL13, intact BBB | 27894304 | MODEL_ORGANISM |
| GABAergic terminal/receptor deficit precedes interneuron loss | 24586687 | MODEL_ORGANISM |
| CSTB secreted; guides interneuron migration (human organoids) | 32378798 | MODEL_ORGANISM + IN_VITRO |
| Sustained histone H3 clipping by nuclear cathepsin L | 36533126 | MODEL_ORGANISM |
| Behavioral phenotyping; no ataxia on 129S2/SvHsd | 38179183 | MODEL_ORGANISM |
| PME pharmacology review; drugs to avoid | 27629998 | HUMAN_CLINICAL |
| Severe hypomyelination phenotype, homozygous frameshift | 28378817 | HUMAN_CLINICAL |
| First Chinese case; point/indel = earlier onset, refractory BTCS | 40442775 | HUMAN_CLINICAL |
| APOE ε4 modifier | 41042579 | HUMAN_CLINICAL |
| Compound het electroclinical series, 11.5% of families | 23205931 | HUMAN_CLINICAL |
| Brivaracetam long-term OLE, 94 ULD patients | 33461041 | HUMAN_CLINICAL |

**Structured-source citations available:** `ORPHA:308` (definition, prevalence rows, xrefs — will need `just structured-rebuild-orphanet --id 308` since it is not in the local cache).

**Knowledge gaps to file as `discussions`:**
1. `KNOWLEDGE_GAP` — Is promoter hypermethylation the mechanism of expansion-mediated CSTB silencing? Not directly demonstrated in patient brain.
2. `KNOWLEDGE_GAP` — What explains intrafamilial severity variation at matched repeat sizes? Modifier loci unidentified.
3. `KNOWLEDGE_GAP` — No metabolomic, lipidomic, single-cell, or spatial profiling of EPM1 tissue exists.
4. `HUMAN_MODEL_MISMATCH` — *Cstb*⁻ᐟ⁻ is a null; human disease is a 5–10% hypomorph. No dodecamer knock-in model.
5. `HUMAN_MODEL_MISMATCH` — Mouse shows *reduced* startle; the human hallmark is *stimulus hypersensitivity*. Ataxia absent on pure 129S2/SvHsd.
6. `KNOWLEDGE_GAP` — Is early microglial activation causal or merely the earliest detectable event? Requires a conditional cell-type-specific *Cstb* knockout that does not yet exist.
7. `KNOWLEDGE_GAP` — Would postnatal CSTB restoration help, given the prenatal interneuron-migration defect? Bears directly on gene-therapy feasibility.
8. `KNOWLEDGE_GAP` — Repeat-size/severity relationship: threshold model (PMID:9529356) vs modulator model (PMID:25770194) unresolved; curate as competing `mechanistic_hypotheses`.

---

### Sources

- [GeneReviews: Unverricht-Lundborg Disease (NBK1142)](https://www.ncbi.nlm.nih.gov/books/NBK1142/) — PMID:20301321
- [The Roles of Cystatin B in the Brain and Pathophysiological Mechanisms of Progressive Myoclonic Epilepsy Type 1 (Cells 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10814315/) — PMID:38247861
- [Cystatin B deficiency sensitizes neurons to oxidative stress](https://pubmed.ncbi.nlm.nih.gov/19420257/) — PMID:19420257
- [Dodecamer repeat expansion in cystatin B gene (Nature 1997)](https://www.nature.com/articles/386847a0) — PMID:9126745
- [Cystatin B: mutation detection, alternative splicing and expression (EJHG 2007)](https://www.nature.com/articles/5201723) — PMID:17003839
- [Brain inflammation is accompanied by peripheral inflammation in Cstb−/− mice](https://jneuroinflammation.biomedcentral.com/articles/10.1186/s12974-016-0764-7) — PMID:27894304
- [Gene expression alterations in the cerebellum and granule neurons of Cstb−/− mouse](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3937333/) — PMID:24586687
- [In depth behavioral phenotyping of the Cstb−/− mouse](https://pmc.ncbi.nlm.nih.gov/articles/PMC10764494/) — PMID:38179183
- [Insights into the Genetic Profile of Two Siblings Affected by ULD Using Patient-Derived hiPSCs](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9655992/) — PMID:36359887
- [A novel c.116-117del variant in ULD: first report in a large Chinese population](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12121152/) — PMID:40442775
- [Severer phenotype in EPM1 compound heterozygotes](https://pubmed.ncbi.nlm.nih.gov/21757863/) — PMID:21757863
- [PCR-based analysis using deaminated DNA of dodecamer expansions in CSTB](https://pubmed.ncbi.nlm.nih.gov/16379547/) — related methodology
- [MedlinePlus Genetics: Unverricht-Lundborg disease](https://medlineplus.gov/download/genetics/condition/unverricht-lundborg-disease.pdf)
- Orphanet / Orphadata API, ORPHA:308 (snapshot 2026-06-23); HPO API `OMIM:254800`; OLS4 (MONDO); UniProt P04080; NCBI E-utilities (all abstracts quoted above).