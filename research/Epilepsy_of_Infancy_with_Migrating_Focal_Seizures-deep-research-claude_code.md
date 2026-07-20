---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-18T11:06:13.268925'
end_time: '2026-07-18T11:11:46.379563'
duration_seconds: 333.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Epilepsy of Infancy with Migrating Focal Seizures
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
  - claude-opus-4-8
  web_search_requests: 6
  num_turns: 10
  total_cost_usd: 1.53185025
  session_id: bc953088-e1b8-44a6-ba66-f8990c56a59f
  stop_reason: end_turn
citation_count: 18
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Epilepsy of Infancy with Migrating Focal Seizures
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Epilepsy of Infancy with Migrating Focal Seizures** covering all of the
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

Alright, I've got a solid haul of sources. Here's the full report.

---

# Epilepsy of Infancy with Migrating Focal Seizures (EIMFS) — Disease Characteristics Research Report

*sup Harry — so this one's a real heartbreaker of a disease. EIMFS is one of the nastiest early-life epilepsies we know of: a baby's brain gets a channel stuck in the "on" position and seizures start wandering around the cortex like a storm system that never clears. Below is the full workup. One housekeeping note up top, because your whole repo is built around not trusting synthesized citations: the PMIDs I **personally pulled and confirmed this session** are 31872048, 29196579, 30234941, 36173683, and 32505479. Everything else I've named by author/journal/year and tagged `[verify]` — run `just fetch-reference` on those before any snippet lands in a YAML. Don't let me hand you a hallucinated quote.*

---

## 1. Disease Information

**What it is.** EIMFS is a rare, severe **developmental and epileptic encephalopathy (DEE)** of early infancy. The defining feature is *migrating* focal seizures — focal (partial) seizures that arise independently at multiple, shifting cortical foci and appear to "travel" from one brain region or hemisphere to another, both within a single seizure and across seizures. They're relentlessly drug-resistant, become nearly continuous by 6–9 months of age, and drag psychomotor development to a halt (arrest, then regression). Think of it less like a single short-circuit and more like a grid where breakers keep tripping in a rolling blackout across the whole city.

**Key identifiers:**
| Resource | ID |
|---|---|
| OMIM | **614959** — Developmental and epileptic encephalopathy 14 (DEE14; formerly EIEE14), the KCNT1 locus |
| Orphanet | **ORPHA:293181** |
| MONDO | ~**MONDO:0013820** `[verify against sqlite:obo:mondo — run the NEC preflight, this is a numbered-DEE series and prime named-entity-confusion territory]` |
| ICD-11 | **8A62** (Developmental and epileptic encephalopathies) — no leaf code specific to EIMFS |
| ICD-10 | G40.4 (other generalized epilepsy) is the usual crosswalk; no specific code |
| MeSH | No dedicated descriptor; indexed under *Epilepsies, Partial* / *Spasms, Infantile* / *Epileptic Encephalopathy* |

**Synonyms / alternative names:** Malignant Migrating Partial Seizures of Infancy (**MMPSI** — the original 1995 name, Coppola et al.), Migrating Partial Seizures of Infancy (MPSI), Migrating Partial Epilepsy of Infancy, and gene-anchored labels like **KCNT1-related epilepsy** / DEE14. ILAE now formally recognizes EIMFS as a distinct infantile-onset epilepsy syndrome in its 2022 neonatal/infantile classification.

**Data provenance.** This report is built from **aggregated disease-level resources** (OMIM, Orphanet, GeneReviews, ILAE classification) plus cohort and case-series primary literature — *not* individual EHR data.

*Sources: [GeneReviews KCNT1-Related Epilepsy](https://www.ncbi.nlm.nih.gov/books/NBK525917/) (PMID:30234941); [MedlinePlus EIMFS](https://medlineplus.gov/genetics/condition/epilepsy-of-infancy-with-migrating-focal-seizures/); [ILAE 2022 syndrome classification](https://www.ilae.org/files/dmfile/Neonatal_Infantile_Finalapril5.pdf).*

---

## 2. Etiology

**Primary cause: genetic.** EIMFS is genetically heterogeneous, but one gene dominates: **KCNT1**, where **de novo gain-of-function** missense variants account for roughly **~40–50% of cases**. This is the flagship story — Barcia et al. (*Nature Genetics* 2012, `[verify PMID:23086397]`) first tied KCNT1 gain-of-function to MMPSI.

**Genetic risk factors / causal variants.** Beyond KCNT1, a long tail of genes has been reported. The consistently replicated second-tier causes:
- **SCN2A** — second most common genetic cause of EIMFS
- **SCN1A**, **SCN8A** — voltage-gated sodium channels
- **SLC25A22** — mitochondrial glutamate carrier (autosomal recessive)
- **TBC1D24** — recessive
- **PLCB1** — phospholipase C beta 1 (recessive)
- **SLC12A5 (KCC2)** — biallelic loss-of-function impairing the neuronal chloride exporter (Stödberg et al. *Nat Commun* 2015 `[verify PMID:26333769]`; Saitsu et al. 2016)
- **KCNT2** — de novo variants exerting *inhibitory* effects on the heteromeric KNa1.1/KNa1.2 channel (Ambrosino et al., *Front Mol Neurosci* — [PMC6992647](https://pmc.ncbi.nlm.nih.gov/articles/PMC6992647/) `[verify PMID]`)

A broader list reported in EIMFS/EIMFS-like presentations includes *KCNQ2, CDKL5, GABRB3/GABRA1/GABRG2, HCN1, ITPA, QARS, FARS2, KARS, BRAT1, ATP1A3, WWOX, PCDH19, SMC1A, PIGA* and others — many of these are "EIMFS-like" rather than classic.

**Environmental / non-genetic factors.** EIMFS is fundamentally a **monogenic channelopathy** — there is **no established environmental, infectious, or toxic cause**, and no meaningful lifestyle or occupational exposure signal (it's an infant disease). Age (first months of life) and the presence of a pathogenic variant are the whole story.

**Protective factors.** None described genetically or environmentally. This isn't a complex-trait disease with modifiable risk — it's a single dominant-acting molecular lesion. `[Not applicable / not available.]`

**Gene–environment interactions.** Not applicable in the usual GxE sense. The one "interaction" worth curating is **modifier/second-hit variability**: the same KCNT1 variant can produce anything from lethal EIMFS to an asymptomatic carrier within one family (see §4, §9), which points to genetic-background modifiers we haven't mapped yet.

*Sources: [KCNT1 hotspots paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC6878841/) (PMID:31872048); [Genetic Landscape of EIMFS](https://pmc.ncbi.nlm.nih.gov/articles/PMC7423163/); [Locus Heterogeneity in EIMFS](https://pmc.ncbi.nlm.nih.gov/articles/PMC4749118/).*

---

## 3. Phenotypes

Onset is **neonatal-to-early-infantile** — mean seizure onset **~1 month** (range: 1 hour of life to ~4 months, occasionally up to ~7 months) per the 17-patient cohort in PMID:31872048. Course is **progressive**: milestones may be reached briefly, then **arrest and regression** follow seizure onset.

| Phenotype | Type | Characteristics | Suggested HPO |
|---|---|---|---|
| **Migrating focal (multifocal) seizures** | Clinical/electrographic sign | The defining feature; onset <6 mo; near-continuous by 6–9 mo; pharmacoresistant | **HP:0011153** Focal-onset seizure; **HP:0032807** Migrating focal seizures |
| Focal motor seizures | Symptom | Clonic/tonic limb, eye deviation, head turning | **HP:0011153** |
| **Autonomic features** (apnea, perioral cyanosis, flushing, apnea/desaturation, salivation) | Sign | "Common"; can be the presenting event | **HP:0011153** + **HP:0002104** Apnea; **HP:0000961** Cyanosis |
| Seizure intractability / drug resistance | Sign | Refractory to multiple ASMs | **HP:0032794** Refractory epilepsy |
| **Developmental arrest / regression** | Sign | Onset after seizures begin; near-universal | **HP:0002376** Developmental regression |
| **Profound intellectual disability / global developmental delay** | Sign | Most never walk or speak | **HP:0002187** Profound global developmental delay; **HP:0010864** Intellectual disability, severe |
| Acquired microcephaly | Physical | Postnatal deceleration of head growth | **HP:0005484** Postnatal microcephaly |
| **Axial hypotonia** | Sign | Common; with later appendicular spasticity/dystonia | **HP:0008936** Axial hypotonia |
| Dystonia / movement disorder (incl. status dystonicus) | Sign | Reported with specific KCNT1 variants | **HP:0001332** Dystonia |
| Choreoathetosis / abnormal movements | Sign | | **HP:0001269** |
| Feeding difficulties / failure to thrive | Sign | Secondary; frequently needs G-tube | **HP:0011968** Feeding difficulties |
| **Peripheral autonomic dysregulation** (temperature instability, GI dysmotility) | Sign | | **HP:0002027** Abdominal pain / **HP:0012332** Abnormal autonomic nervous system physiology |
| Cortical visual impairment | Sign | | **HP:0100704** Cerebral visual impairment |
| **Rare: pulmonary hemorrhage** (ages 4–19 mo) | Lab/clinical | KCNT1-specific, potentially fatal | **HP:0002105** Hemoptysis |
| **Rare: cardiac arrhythmia / Brugada pattern** | Lab/clinical | KCNT1 is expressed in heart; relevant for quinidine safety | **HP:0011675** Arrhythmia |

**EEG signature** (the electrophysiology is diagnostic): **migrating ictal pattern** — ictal discharges begin focally, then involve progressively adjacent and contralateral regions with independent multifocal onsets. Interictal backgrounds are abnormal; **suppression-burst** (4/17) and **hypsarrhythmia** with infantile spasms (3/17) were seen in the hotspots cohort (PMID:31872048).

**Frequency among affected:** migrating seizures, refractoriness, developmental arrest → essentially universal (definitional). Autonomic features "common." Movement disorders and the rare pulmonary/cardiac features are variant-associated minorities.

**Quality of life:** Catastrophic. Profound disability means near-total dependence for feeding, mobility, and communication; families bear enormous caregiving burden. No EIMFS-specific validated QoL instrument exists — generic pediatric DEE tools (e.g., caregiver-reported measures) are what's used. `[Per-phenotype QoL data: not available.]`

*Sources: [KCNT1 hotspots](https://pmc.ncbi.nlm.nih.gov/articles/PMC6878841/) (PMID:31872048); [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK525917/) (PMID:30234941); [36-patient cohort, Sci Rep 2022](https://www.nature.com/articles/s41598-022-13974-9).*

---

## 4. Genetic / Molecular Information

**Causal gene — KCNT1** (HGNC:18865; `hgnc:18865`; OMIM *608167*; chr **9q34.3**). Encodes **KNa1.1** (a.k.a. **Slack**, **SLO2.2**), a **sodium-activated potassium channel** — a large-conductance K⁺ channel gated by intracellular Na⁺ (and Cl⁻), assembling as a tetramer with a big cytoplasmic C-terminal RCK (regulator of K⁺ conductance) domain. It sets the slow after-hyperpolarization and tunes neuronal firing.

**Variant class:** Nearly all pathogenic KCNT1 variants are **heterozygous missense** (loss-of-function/truncating is rare and tends to give milder or different phenotypes). **Functional consequence = gain of function**: mutant channels show markedly **increased K⁺ current amplitude**, and multiple variants cause **constitutive opening / loss of cooperative gating**. There's growing evidence for a *second* mechanism — impaired **non-conducting** functions, i.e., the mutant C-terminus fails to properly interact with developmental signaling partners like **FMRP (fragile-X mental retardation protein)** — so it's not purely "too much potassium current."

**Mutation hotspots** (recurrent residues, mostly C-terminal): **p.G288S** (pore region), **p.R398Q**, **p.R428Q**, **p.R474C**, **p.R474H**, **p.A934T**, plus p.L437P, p.M516V, p.M896I, p.A965V, p.R1106P and others (PMID:31872048). Computational modeling implicates **abnormal pore function and impaired tetramer assembly**.

**Genotype–phenotype (weak, but a trend):** EIMFS-associated variants cluster in the **S5 transmembrane and RCK/NAD⁺-binding (C-terminal) domains**; ADNFLE variants concentrate near the NAD⁺-binding domain. BUT — and this is the load-bearing caveat — **the same variant (p.G288S, p.R398Q, p.A934T) shows up in *both* EIMFS and ADNFLE**, sometimes **within one family** (the R398Q three-generation family: severe EIMFS proband, ADNFLE father, asymptomatic uncle). So no clean single-variant → single-phenotype rule exists. Modifier genes are strongly implicated but unmapped.

**Allele frequency:** Pathogenic KCNT1 EIMFS variants are **de novo** and essentially **absent from gnomAD** (as expected for a lethal-tending dominant DEE). ADNFLE variants may recur in families.

**Somatic vs germline:** Predominantly **germline de novo**. But **somatic and germline mosaicism** have been documented — in unaffected/mildly affected transmitting parents, and low-level somatic mosaicism can modulate severity. Relevant for recurrence counseling.

**Modifier genes / epigenetics / chromosomal abnormalities:** Modifiers strongly suspected (intrafamilial variability) but not characterized. **No epigenetic mechanism and no chromosomal/structural abnormality** is part of the EIMFS mechanism — this is a point-mutation channelopathy. `[Not applicable for CNV/karyotype.]`

Suggested GO / entities: **GO:0005228** intracellular sodium activated potassium channel activity; **GO:0008076** voltage-gated potassium channel complex; **GO:0051260** protein homooligomerization (tetramer assembly); **CHEBI:29103** potassium(1+); **CHEBI:29101** sodium(1+).

*Sources: [KCNT1 hotspots](https://pmc.ncbi.nlm.nih.gov/articles/PMC6878841/) (PMID:31872048); [KCNT1-related severe early-onset epilepsy](https://pubmed.ncbi.nlm.nih.gov/29196579/) (PMID:29196579); [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK525917/) (PMID:30234941); [status dystonicus KCNT1 variant](https://pmc.ncbi.nlm.nih.gov/articles/PMC6764634/).*

---

## 5. Environmental Information

There is essentially nothing to curate here, and that's itself the finding. EIMFS is a **monogenic developmental channelopathy** with **no established environmental, lifestyle, or infectious contribution**. It's a congenital/early-infantile genetic disease — no toxin, radiation, pollutant, occupational exposure, diet, or pathogen has been shown to cause or trigger it. Fever and intercurrent illness can *provoke* seizure worsening (as in any epilepsy), but that's a nonspecific seizure threshold effect, not an etiologic factor. `[Environmental / infectious factors: not applicable.]`

---

## 6. Mechanism / Pathophysiology

**The causal chain (upstream → downstream):**

1. **De novo GoF missense variant in KCNT1** →
2. **Constitutively hyperactive KNa1.1 (Slack) channels** — increased Na⁺-activated K⁺ current, loss of cooperative gating, channels open when they shouldn't →
3. Paradoxically, this K⁺ hyperactivity in specific neuronal populations (notably **GABAergic interneurons**) is thought to **shorten action potentials / speed repolarization and dampen inhibitory interneuron output**, tipping the network toward **excitation–inhibition imbalance** →
4. **Neuronal hyperexcitability and hypersynchrony** across multiple independent cortical foci →
5. **Migrating multifocal seizures + epileptogenesis** →
6. Ongoing seizures + disrupted KCNT1 developmental signaling → **developmental arrest / regression / encephalopathy**.

This is a clean conformer to your **`epilepsy_excitation_inhibition_imbalance`** module — the key target node `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance` maps directly onto steps 3–4. And there's a nice mechanistic twist worth a `mechanistic_hypotheses` block: EIMFS is a rare case where a **gain-of-function in a *potassium* (inhibitory-current) channel causes *hyper*excitability** — the resolution is cell-type-specific (the interneuron story), which is a genuinely open question and a good candidate for a `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion.

**Second mechanistic arm — non-conducting functions:** KCNT1's C-terminus scaffolds developmental signaling proteins (**FMRP** among them). Mutations disrupt these protein–protein interactions independent of ion flux, which may explain why the encephalopathy is more severe than pure ictal burden predicts, and flags a therapeutic target beyond channel-blockade.

- **Molecular pathways / cellular processes:** Ion transport / membrane potential regulation (**GO:0006813** potassium ion transport; **GO:0051899** membrane depolarization; **GO:0019228** neuronal action potential); synaptic transmission, GABAergic (**GO:0051932**); regulation of neuronal excitability.
- **Protein dysfunction:** Gain-of-function channel opening + impaired oligomerization/tetramer formation + disrupted C-terminal interactome. Not misfolding/aggregation — it's a hyperfunctional, mis-gated channel.
- **Cell types (CL):** cortical **GABAergic interneuron** (**CL:0000617**), glutamatergic/pyramidal **neuron** (**CL:0000598 / CL:0000679**). KCNT1 is broadly expressed in CNS neurons.
- **Immune / metabolic / fibrosis / oxidative-stress mechanisms:** **Not involved.** (Exception: the *SLC25A22* recessive form is a mitochondrial glutamate-transport/energetics defect — but that's a distinct EIMFS-causing gene, not the KCNT1 mechanism.)
- **Molecular profiling (transcriptomics/proteomics/metabolomics):** No robust human EIMFS omics signature published. Mechanistic data come from **heterologous electrophysiology** (Xenopus oocyte / mammalian cell expression, patch-clamp) and **mouse models**, not patient tissue omics. `[Omics: largely not available.]`
- **Functional genomics:** Rescue/knockdown work exists via ASO in mouse (see §12), not CRISPR screens.

*Sources: [KCNT1-related severe early-onset epilepsy](https://pubmed.ncbi.nlm.nih.gov/29196579/) (PMID:29196579); [Neurology Genetics migrating focal seizures](https://www.neurology.org/doi/10.1212/NXG.0000000000000363); [KCNT1 hotspots](https://pmc.ncbi.nlm.nih.gov/articles/PMC6878841/) (PMID:31872048).*

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** **Brain** — the **cerebral cortex** (**UBERON:0000956**), diffusely and multifocally; this is a whole-cortex network disease, not a single-lobe focus. **Nervous system** (UBERON:0001016) is the affected body system.
- **Secondary organ involvement:** Systemic sequelae of severe DEE — respiratory (aspiration, apnea; rare **pulmonary hemorrhage**), cardiac (**KCNT1 arrhythmia / Brugada risk** — genuinely important because quinidine has cardiac effects), GI (dysmotility, feeding failure). Growth (postnatal microcephaly).
- **Neuroimaging structural correlates:** Brain MRI is **often normal early**, but longitudinal imaging shows **delayed myelination, progressive cerebral/cerebellar atrophy, and hippocampal volume loss** — i.e., acquired, not malformative. (Cerebellum **UBERON:0002037**; hippocampus **UBERON:0002421**.)
- **Tissue / cell level:** **Nervous tissue**; **cortical GABAergic interneurons (CL:0000617)** and glutamatergic pyramidal neurons (CL:0000679) are the mechanistically central populations.
- **Subcellular (GO Cellular Component):** **plasma membrane** (GO:0005886), **voltage-gated potassium channel complex** (GO:0008076), **neuronal cell body / axon initial segment** where Slack channels localize.
- **Localization / lateralization:** **Bilateral, asymmetric, multifocal, shifting** — the "migrating"/independent-multifocal onset is the anatomic hallmark. No fixed lateralization.

---

## 8. Temporal Development

- **Onset:** **Neonatal to early infantile.** Mean ~1 month; range from the **first hours/week of life to ~4 (occasionally ~7) months**. Onset pattern is **subacute-to-progressive** — seizures start, then escalate.
- **Progression / stages:**
  - *Early phase* — focal seizures begin, initially sporadic, sometimes with brief normal or near-normal development.
  - *Peak/plateau phase (~6–9 months)* — seizures become **very frequent to near-continuous**, migrating multifocal pattern fully established; **developmental arrest then regression**.
  - *Chronic phase* — seizure frequency may fluctuate/partially wane in some survivors over years, but **profound disability persists**; spasticity/dystonia and microcephaly evolve.
- **Progression rate:** Rapid in the first year; then chronic-static-to-slowly-progressive disability.
- **Course pattern:** Chronic, lifelong, **pharmacoresistant**; seizures episodic-to-continuous.
- **Remission:** **Spontaneous remission is rare.** Rare partial, treatment-associated responses reported (quinidine in some KCNT1 cases; ketogenic diet occasionally) but true seizure freedom is uncommon and developmental outcome rarely normalizes even when seizures improve.
- **Critical window:** The first months of life are both the vulnerability window and the presumed **therapeutic window** — the whole rationale behind *early* quinidine and future genetic therapies is intervening before irreversible developmental injury accrues.

*Sources: [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK525917/) (PMID:30234941); [36-patient cohort](https://www.nature.com/articles/s41598-022-13974-9).*

---

## 9. Inheritance and Population

**Epidemiology.** EIMFS is **rare/ultra-rare** — an estimated prevalence on the order of **~0.11 per 100,000 children** (i.e., roughly 1 in ~900,000; well within Orphanet's ultra-rare band). Incidence figures are not firmly established; it's a small slice of the overall DEE burden (cumulative DEE incidence ~169/100,000). Literature has aggregated on the order of **~120 patients across ~116 families** for KCNT1 specifically as of the hotspots review (PMID:31872048), with GeneReviews citing ~88 KCNT1 probands.

- **Prevalence class (for the KB):** `BELOW_1_IN_1000000`–`ULTRA_RARE` neighborhood; `rate_per_100000` ≈ **0.11**, `measure_type: POINT_PREVALENCE`.

**Inheritance pattern:**
- **KCNT1 EIMFS = de novo, autosomal dominant** — essentially all EIMFS probands are **simplex cases** from a de novo variant (**HP:0000006** Autosomal dominant inheritance; often effectively sporadic).
- **Recessive forms** exist for other genes: **SLC25A22, TBC1D24, PLCB1, SLC12A5** are **autosomal recessive** (**HP:0000007**) — consanguinity is relevant for those.
- **Penetrance:** **~100% for KCNT1-related EIMFS**; **reduced/variable** for the milder KCNT1 phenotypes (ADNFLE, asymptomatic carriers).
- **Expressivity:** **Highly variable** — the same variant spans lethal EIMFS to asymptomatic within a single pedigree.
- **Genetic anticipation:** Not a feature (not a repeat-expansion disorder). `[Not applicable.]`
- **Mosaicism:** **Documented** — somatic and germline mosaicism in transmitting parents; matters for recurrence-risk counseling.
- **Founder effects / carrier frequency:** No founder effect described; de novo variants aren't in population carrier databases. `[Not applicable.]`

**Population demographics:**
- **Ethnicity/geography:** No ethnic predilection; reported worldwide (European, North American, East Asian, South Indian cohorts all published). No endemic geography.
- **Sex ratio:** Roughly **equal / no strong sex bias** (the 17-patient cohort was 8 F / 9 M).
- **Age distribution:** By definition an **infantile-onset** disorder; the affected population is children (and the reduced number of survivors reaching later childhood/adulthood with profound disability).

*Sources: [KCNT1 hotspots](https://pmc.ncbi.nlm.nih.gov/articles/PMC6878841/) (PMID:31872048); [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK525917/) (PMID:30234941); [DEE epidemiology](https://pmc.ncbi.nlm.nih.gov/articles/PMC10065214/).*

---

## 10. Diagnostics

**The diagnostic pillars are EEG + genetics.**

- **Electrophysiology (central):** **Video-EEG** showing the **migrating ictal pattern** — focal ictal discharges arising independently at multiple sites, migrating across contiguous regions and between hemispheres, on an abnormal interictal background (± suppression-burst, ± hypsarrhythmia). This is the phenotypic anchor of the diagnosis. **ECG/Holter** is important adjunctively — both to screen for KCNT1-associated arrhythmia and as **baseline before quinidine**.
- **Imaging:** **Brain MRI** — typically **normal early**; used to exclude structural/malformative and metabolic mimics, and to track later atrophy/myelination delay.
- **Laboratory / metabolic workup:** Done to **exclude treatable metabolic epilepsies** (e.g., pyridoxine-dependent/ALDH7A1, PNPO, glucose transporter, mitochondrial disorders) — CSF/serum metabolic panels, lactate, amino/organic acids. Normal in KCNT1 EIMFS; abnormal points you to a different diagnosis.
- **Genetic testing (definitive):**
  - **First-line: broad epilepsy/DEE next-generation-sequencing panel or exome/genome (WES/WGS)** — GeneReviews explicitly recommends **multigene panel or comprehensive genomic testing over single-gene testing** given locus heterogeneity. Sequence analysis detects ~100% of KCNT1 variants.
  - **Single-gene KCNT1 testing** only when the EEG/clinical picture is classic and you want targeted confirmation.
  - **CMA / karyotype / FISH:** low yield (this is a point-mutation disease) but part of a general DEE workup to exclude CNV mimics. `[Mostly not applicable.]`
  - **Repeat-expansion / mtDNA testing:** not indicated for KCNT1; mtDNA relevant only if a mitochondrial phenotype (e.g., SLC25A22-like) is suspected.
- **Omics-based diagnostics:** No validated clinical omics assay for EIMFS beyond DNA sequencing. `[RNA-seq/proteomics/metabolomics: research-only / not available.]`
- **Clinical/diagnostic criteria:** **ILAE 2022** infantile-onset syndrome criteria for EIMFS (characteristic seizure semiology + migrating EEG pattern + developmental course), plus molecular confirmation.
- **Differential diagnosis:** other early-infantile DEEs — **Ohtahara syndrome / early-infantile DEE**, **West syndrome (infantile spasms)**, **Dravet syndrome (SCN1A)**, **KCNQ2 encephalopathy**, **CDKL5 deficiency**, **pyridoxine/PNPO-responsive epilepsies**, **GLUT1 deficiency**, and structural/metabolic epilepsies. Distinguishing feature: the **migrating multifocal ictal EEG pattern** + KCNT1 genotype.
- **Screening:** No population newborn screen. **Cascade testing** in families is complicated by mosaicism/variable expressivity; **genetic counseling** is essential.

*Sources: [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK525917/) (PMID:30234941); [MedLink EIMFS](https://www.medlink.com/articles/epilepsy-in-infancy-with-migrating-focal-seizures).*

---

## 11. Outcome / Prognosis

**Prognosis is poor** — this is one of the most severe DEEs. In the well-characterized **36-patient EIMFS cohort** (*Sci Rep* 2022): **13/36 had ineffective seizure control, 14/36 had severe intellectual disability, and 6/36 died.** GeneReviews frames long-term EIMFS prognosis as still incompletely defined but uniformly severe.

- **Survival / mortality:** **Reduced life expectancy.** Early mortality is substantial (roughly **~15–20%** in cohorts), from status epilepticus, intercurrent illness/aspiration, the rare pulmonary hemorrhage, and **SUDEP** (sudden unexpected death in epilepsy) risk inherent to severe drug-resistant epilepsy. Formal 5-/10-year survival curves aren't well established given rarity.
- **Morbidity / function:** **Profound, lifelong.** Most survivors have **severe-to-profound intellectual disability**, never achieve independent ambulation or speech, and depend fully on caregivers; spasticity, dystonia, microcephaly, feeding difficulty (frequent G-tube), and cortical visual impairment are common.
- **Disease course / complications:** recurrent status epilepticus, aspiration pneumonia, growth failure, orthopedic complications of spasticity, and the KCNT1-specific rare complications (pulmonary hemorrhage, cardiac arrhythmia).
- **Recovery potential:** **Low.** Even when seizures partially respond (e.g., quinidine responders), **developmental outcome rarely normalizes** — quinidine cut seizure burden ~90% in two reported responders but did *not* rescue developmental milestones.
- **Prognostic factors:** earlier onset and higher seizure burden trend worse; specific variant and (hypothesized) modifier background influence severity; **early effective seizure control** is the main potentially modifiable factor and the rationale for early targeted therapy.
- **Prognostic biomarkers:** none validated beyond genotype and seizure-control trajectory. `[Molecular prognostic markers: not available.]`

QoL measures: generic pediatric/caregiver DEE instruments; no EIMFS-specific validated tool.

*Sources: [36-patient cohort](https://www.nature.com/articles/s41598-022-13974-9); [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK525917/) (PMID:30234941); [early quinidine 2-patient study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6277296/).*

---

## 12. Treatment

*The honest headline: it's mostly refractory, and the "precision" drug (quinidine) has been a genuine disappointment outside a few responders. The real hope is upstream — genetic therapy.*

**Pharmacotherapy — conventional antiseizure medicines (ASMs):**
- Broadly **drug-resistant**. Combinations tried include **stiripentol + benzodiazepines** (clonazepam), **levetiracetam**, sodium-channel blockers, topiramate, vigabatrin, etc. Responses are partial at best.
- **MAXO/NCIT:** `NCIT:C15986` Pharmacotherapy; **MAXO:0000009** pharmacotherapy.

**Targeted / precision therapy — Quinidine** (the marquee "channelopathy repurposing" story):
- **Rationale:** Quinidine is a **partial KNa1.1/Slack blocker** → it should counteract KCNT1 gain-of-function. Milligan et al. (2014) showed quinidine reverses KCNT1 GoF in vitro `[verify PMID:24838348]`; Bearden et al. (2014) first reported clinical benefit in a patient `[verify]`.
- **Reality check:** Results are **highly variable and often disappointing**. Some KCNT1-EIMFS patients (esp. with **early** treatment + drug-level/cardiac monitoring) get **~90% seizure reduction** ([2-patient study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6277296/)); many others get **no benefit and dose-limiting cardiotoxicity** (QT prolongation, arrhythmia). A **randomized quinidine trial in KCNT1-ADNFLE was negative** (Mullen et al. 2018 `[verify PMID:~29196578]`). GeneReviews is notably cautious. **Bottom line for the KB:** quinidine is a *variant-/patient-dependent* option requiring cardiac monitoring and therapeutic drug level titration — **not** a reliable cure. Variable in-vitro blockade across variants partly explains the inconsistency.
- **CHEBI:** quinidine **CHEBI:28593**. **Therapeutic_agent** pattern fits here.
- **`therapeutic_modality: SMALL_MOLECULE`**, with a `target_mechanisms` link back to the excitation–inhibition/KCNT1 node (INHIBITS).

**Other pharmacological options:**
- **Cannabidiol** — used in refractory DEEs including some KCNT1 cases; anecdotal/limited EIMFS-specific evidence. CHEBI:69478. `[Evidence limited.]`
- **Nonnarcotic antitussives (cloperastine)** — one notable **case report** of KCNT1-EIMFS seizure control *after quinidine failure* (PMID:32505479); mechanism putatively also Slack-related. Interesting lead, single case.

**Dietary:**
- **Ketogenic diet** — tried; occasional partial responders; part of the standard refractory-DEE toolkit. **MAXO:0000088** dietary intervention / ketogenic diet.

**Advanced / experimental — the actual frontier:**
- **Antisense oligonucleotide (ASO) therapy** — the most exciting preclinical development. Burbano et al. (**JCI Insight** 2022, **PMID:36173683**) built a **Kcnt1 p.P924L knock-in mouse**; a **single ICV bolus of a Kcnt1 gapmer ASO** in symptomatic mice **reduced seizure frequency, improved behavior, and extended survival** in a gene-specific, dose-dependent way. This is a **direct EIMFS gene-silencing precision therapy** in the pipeline. Maps beautifully onto your **`antisense_oligonucleotide_therapy#Pathogenic mRNA Accumulation`** module node (RNase-H knockdown paradigm). `therapeutic_modality: ANTISENSE_OLIGONUCLEOTIDE`; `aso_mechanism: RNASE_H_KNOCKDOWN`; `target_gene: KCNT1 (hgnc:18865)`.
- A related **cross-syndrome** finding: **reducing Kcnt1 was therapeutic in SCN1A and SCN8A epilepsy mouse models** ([Front Neurosci 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10603267/)) — suggesting Slack knockdown could be broadly useful.
- No approved gene therapy / CRISPR / cell therapy yet; these remain preclinical.

**Surgical / interventional:** Resective epilepsy surgery is generally **not applicable** — the multifocal, migrating, bilateral nature means there's no single resectable focus. **Vagus nerve stimulation (VNS)** and **corpus callosotomy** have been tried as palliative options in refractory DEE with limited benefit.

**Supportive / rehabilitative (the backbone of real-world care):** seizure-rescue protocols, respiratory and feeding support (G-tube), physical/occupational/speech therapy, spasticity and dystonia management, and family/palliative support. **MAXO:0000950** supportive care; **MAXO:0000011** physical therapy.

**Treatment strategy / algorithm:** confirm genotype → trial standard ASMs → if **KCNT1 GoF**, consider **early monitored quinidine** (with cardiology) → ketogenic diet / cannabidiol as adjuncts → supportive/palliative care throughout → enroll in trials / watch the ASO pipeline. **Genotype-guided** care is the emerging paradigm.

*Sources: [ASO therapy for KCNT1 encephalopathy](https://pubmed.ncbi.nlm.nih.gov/36173683/) (PMID:36173683); [early quinidine 2-patient study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6277296/); [cloperastine case report](https://pubmed.ncbi.nlm.nih.gov/32505479/) (PMID:32505479); [Kcnt1 reduction in SCN1A/SCN8A models](https://pmc.ncbi.nlm.nih.gov/articles/PMC10603267/); [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK525917/) (PMID:30234941).*

---

## 13. Prevention

Because EIMFS is a **de novo genetic disease with no environmental input**, classic prevention doesn't apply — you can't lifestyle your way out of a de novo channel mutation. Prevention is essentially **reproductive-genetic** and **tertiary**.

- **Primary prevention:** **Not applicable** in the public-health sense (no modifiable exposure, no vaccine, and de novo variants mean unaffected parents have no warning). The only "primary prevention" lever is **reproductive**: for families with a proven transmitting variant or germline mosaicism, **preimplantation genetic testing (PGT-M)** and **prenatal diagnosis** can prevent recurrence.
- **Secondary prevention (early detection):** **Rapid genetic diagnosis** in a neonate/infant with the characteristic seizures + migrating EEG — the "screening" that matters is fast **exome/genome sequencing** to enable early genotype-guided treatment during the presumed therapeutic window. No population newborn screen exists.
- **Tertiary prevention (preventing complications):** the mainstay — aggressive seizure/status-epilepticus management, aspiration/respiratory precautions, nutrition support, spasticity management, SUDEP-risk mitigation, and coordinated multidisciplinary care.
- **Genetic counseling:** **Essential.** Covers the de novo/simplex nature, **recurrence risk elevated by possible parental germline mosaicism** (so recurrence risk isn't zero even with unaffected parents), and reproductive options. **MAXO:0000079** genetic counseling.
- **Immunization / infectious / environmental interventions:** **Not applicable.**

*Sources: [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK525917/) (PMID:30234941).*

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human disease — **NCBITaxon:9606** (*Homo sapiens*). No naturally occurring animal counterpart is a recognized clinical entity.
- **Orthologous gene:** **Kcnt1** in mouse (*Mus musculus*, NCBITaxon:10090; NCBI Gene ID **227632**) and rat; the Slack/KNa1.1 channel is **evolutionarily conserved** across vertebrates (and has an invertebrate homolog — *Drosophila* **slowpoke-related** *slo-2*).
- **Natural disease in other species:** **Not described** — no spontaneous KCNT1-EIMFS reported in companion animals or wildlife (OMIA has no established equivalent). `[Not available.]`
- **Comparative biology:** The conserved Slack channel makes **engineered** models highly translatable (see §15), but natural-disease comparative pathology data don't exist for EIMFS.
- **Transmission / zoonosis:** **Not applicable** — genetic, non-communicable.

---

## 15. Model Organisms

- **Primary model — mouse (*Mus musculus*, MGI):**
  - **Kcnt1 p.P924L knock-in** (Burbano et al., PMID:36173683): **homozygotes** recapitulate frequent debilitating seizures and developmental compromise; the platform used to validate ASO therapy. **Model type:** mammalian genetic **knock-in** (patient-variant humanized-equivalent).
  - **Kcnt1 knockout** and additional **gain-of-function knock-in** lines exist for mechanism and drug testing; **Kcnt1 reduction** was therapeutic in **Scn1a and Scn8a** epilepsy mouse models ([Front Neurosci 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10603267/)).
- **In vitro / cellular models:** **Heterologous expression electrophysiology** — *Xenopus* oocytes and mammalian cell lines (CHO/HEK) expressing mutant KCNT1 with **patch-clamp** — the workhorse for demonstrating **gain-of-function**, tetramer/pore modeling, and **quinidine blockade sensitivity** per variant. **iPSC-derived neurons** from patients are an emerging platform.
- **Model characteristics:**
  - *Phenotype recapitulation:* good for the **electrophysiologic** gain-of-function and (in the knock-in) seizures + developmental phenotype; strong translational value for **target validation and ASO/drug testing**.
  - *Limitations:* human **cell-type-specific interneuron circuitry**, the **non-conducting FMRP-interactome** biology, and the full developmental-encephalopathy phenotype are **incompletely captured**; zygosity mismatch (mouse needs homozygous P924L vs. human heterozygous de novo) is a notable caveat — a good `HUMAN_MODEL_MISMATCH` flag for the KB.
- **Applications:** dissecting GoF mechanism, testing channel blockers (quinidine and analogs), and **preclinical validation of ASO gene-silencing** — the main path to a real therapy.
- **Resources:** **MGI** (Mouse Genome Informatics), **IMPC/KOMP** for Kcnt1 alleles, **Cellosaurus** for expression lines.

*Sources: [ASO therapy / Kcnt1 P924L mouse](https://pubmed.ncbi.nlm.nih.gov/36173683/) (PMID:36173683); [Kcnt1 reduction in SCN1A/SCN8A models](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1282201/full).*

---

## Curation quick-reference (for the dismech entry)

- **Module conformance:** `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance` (core), and `antisense_oligonucleotide_therapy#Pathogenic mRNA Accumulation` (KCNT1 ASO, RNase-H knockdown, `target_gene: hgnc:18865`).
- **Inheritance block:** de novo **AD** (`HP:0000006`) for KCNT1; **AR** (`HP:0000007`) for SLC25A22/TBC1D24/PLCB1/SLC12A5 subforms — worth a `has_subtypes` split by gene.
- **Prevalence record:** `POINT_PREVALENCE`, `rate_per_100000 ≈ 0.11`, ultra-rare band.
- **Genetic heterogeneity:** consider `case_fractions` — KCNT1 ~40–50%, SCN2A second, long recessive/other-gene tail.
- **NEC preflight before you commit the MONDO ID** — DEE14 sits in a numbered series (high named-entity-confusion risk); confirm the gene named in the MONDO `def:` is KCNT1 and the OMIM xref is 614959 before trusting `MONDO:0013820`.

**Verified-this-session PMIDs (safe to fetch):** 30234941 (GeneReviews), 31872048 (hotspots), 29196579 (KCNT1 severe early-onset characterization), 36173683 (ASO/JCI Insight), 32505479 (cloperastine case report).

**PMIDs I named but did NOT verify this session — `just fetch-reference` and check the snippet before use:** Barcia 2012 *Nat Genet* (KCNT1 GoF causes MMPSI), Milligan 2014 (quinidine reverses GoF in vitro), Bearden 2014 (first quinidine clinical use), Mullen 2018 (negative quinidine ADNFLE RCT), Stödberg/Saitsu 2015–2016 (SLC12A5), Coppola 1995 (original MMPSI description), and the KCNT2 EIMFS paper. Treat every one of those as a *lead*, not gospel — exactly the way your CLAUDE.md wants it.