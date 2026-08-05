---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-07-25T11:36:14.556213'
end_time: '2026-07-25T11:49:38.831346'
duration_seconds: 804.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SLC6A1-Related Disorder (SLC6A1/GAT-1 GABA transporter epilepsy and
    neurodevelopmental disorder; myoclonic-atonic epilepsy)
  mondo_id: MONDO:0014633
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
  web_search_requests: 2
  num_turns: 34
  total_cost_usd: 4.577056000000001
  session_id: 190f0638-7116-40b3-9d1d-ed6532a7055f
  stop_reason: end_turn
citation_count: 10
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SLC6A1-Related Disorder (SLC6A1/GAT-1 GABA transporter epilepsy and neurodevelopmental disorder; myoclonic-atonic epilepsy)
- **MONDO ID:** MONDO:0014633 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SLC6A1-Related Disorder (SLC6A1/GAT-1 GABA transporter epilepsy and neurodevelopmental disorder; myoclonic-atonic epilepsy)** covering all of the
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

# SLC6A1-Related Disorder — Comprehensive Research Report

**Prepared:** 2026-07-25 · **Target entity:** SLC6A1-related neurodevelopmental disorder (SLC6A1-NDD); GAT-1 GABA transporter epilepsy; epilepsy with myoclonic-atonic seizures (MAE/Doose-type) · **Suggested MONDO:** MONDO:0014633

> **Curation caveat up front (scope mismatch).** MONDO:0014633 is labeled *"epilepsy with myoclonic atonic seizures"* and is defined against OMIM:616421 / ORPHA:1942 (Doose syndrome). That is a **seizure-syndrome** concept, whereas the modern clinical entity is a **gene-defined neurodevelopmental disorder** in which MAE is only one of several presentations (absence epilepsy, generalized epilepsy NOS, focal epilepsy, ID/ASD without epilepsy). Verified from OLS: `MONDO:0014633` → label "epilepsy with myoclonic atonic seizures"; xrefs `OMIM:616421`, `Orphanet:1942`, `DOID:0060475`, `MEDGEN:98284`, `UMLS:C0393702`, `SCTID:230421008`, `GARD:0016108`, `ICD9:345.10`. A dedicated MONDO class for "SLC6A1-related neurodevelopmental disorder" does **not** currently exist (OLS search over MONDO for "SLC6A1" returns only MONDO:0014633). This repo already carries `kb/disorders/Epilepsy_with_Myoclonic_Atonic_Seizures.yaml`, so a new SLC6A1 entry should either (a) be curated as the gene-defined disorder with an explicit note that MONDO under-covers it, or (b) be modeled as a distinct entry with a `differentials`/`mappings` link to the MAE entry. Flag as an open ontology gap.

---

## 1. Disease Information

### Overview

SLC6A1-related neurodevelopmental disorder is an autosomal dominant, de-novo-predominant condition caused by heterozygous loss-of-function variants in *SLC6A1*, which encodes **GAT-1**, the principal presynaptic and astrocytic GABA reuptake transporter of the CNS. The core clinical triad is **developmental delay/intellectual disability with disproportionate language impairment, generalized epilepsy (most characteristically myoclonic-atonic and absence seizures, onset ~1.5–5 years), and behavioral/autistic features**, frequently with hypotonia and a movement disorder (ataxia, tremor, stereotypies).

The mechanistic headline is counter-intuitive and worth encoding explicitly in the pathograph: **losing a transporter for the brain's main inhibitory neurotransmitter causes epilepsy not by removing inhibition, but by letting ambient GABA linger and over-drive extrasynaptic, tonically active GABA-A receptors in thalamocortical circuits.** Think of a sink whose drain is half-blocked — the problem is not too little water in the pipes, it's a basin that never empties, and downstream rhythm generation drowns in it.

Framing from the 2026 scoping review (PMID:42173049):

> "Pathogenic heterozygous loss-of-function variants of SLC6A1 cause a developmental and epileptic encephalopathy characterized by early-onset epilepsy, intellectual disability, and autistic features."

Original gene-disease discovery (PMID:25865495, *Am J Hum Genet* 2015):

> "GAT-1, encoded by SLC6A1, is one of the major gamma-aminobutyric acid (GABA) transporters in the brain and is responsible for re-uptake of GABA from the synapse. In this study, targeted resequencing of 644 individuals with epileptic encephalopathies led to the identification of six SLC6A1 mutations in seven individuals, all of whom have epilepsy with myoclonic-atonic seizures (MAE)."

### Key identifiers

| Resource | Identifier |
|---|---|
| MONDO (best available) | **MONDO:0014633** — epilepsy with myoclonic atonic seizures |
| OMIM (phenotype) | **616421** — Myoclonic-atonic epilepsy (MAE) |
| OMIM (gene) | **137165** — *SLC6A1* |
| Orphanet | **ORPHA:1942** (myoclonic-astatic epilepsy / Doose) |
| DOID | DOID:0060475 |
| MedGen / UMLS | C0393702 (CUI); MedGen 98284 |
| SNOMED CT | 230421008 |
| GARD | 0016108 |
| ICD-9 | 345.10 · **ICD-10:** G40.4 (other generalized epilepsy, by convention) · **ICD-11 foundation:** 951920505 |
| Gene: HGNC | **hgnc:11042** (*SLC6A1*) |
| Gene: NCBI Gene | 6529 (human) |
| Gene: Ensembl | ENSG00000157103 |
| Protein: UniProt | **P30531** (SC6A1_HUMAN), "Sodium- and chloride-dependent GABA transporter 1", 599 aa, 12 transmembrane helices |
| Locus | chr3:10,992,186–11,039,247 (GRCh38) = **3p25.3** (gnomAD API) |
| Variant portal | SLC6A1 portal, Broad Institute — https://slc6a1-portal.broadinstitute.org/ (PMID:37647852) |
| Patient organization | SLC6A1 Connect (PMID:39380901) |

### Synonyms / alternative names

SLC6A1-NDD · SLC6A1-related neurodevelopmental disorder · SLC6A1 deficiency disorder · SLC6A1 epileptic encephalopathy · GAT-1 deficiency · SLC6A1-related epilepsy · myoclonic-atonic epilepsy (MAE/EMAtS) · myoclonic-astatic epilepsy · Doose syndrome (when the seizure syndrome is the framing). MONDO synonym list for MONDO:0014633: "Doose syndrome", "EMAS", "EMAtS", "MAE", "myoclonic astatic epilepsy", "epilepsy with myoclonic-astatic seizures", "myoclonic-astatic epilepsy in early childhood".

### Nature of the evidence base

Predominantly **aggregated, provider-ascertained cohorts** (Johannesen n=34; Goodspeed n=116; Kahen n=28; Brain 2023 n=172 with functional data on 184 variants; AJHG 2024 functional data on 213 variants) plus **participatory/parent-report registries** (Simons Searchlight NCT01238250, GenIDA). Individual-patient EHR data has been used once for healthcare-resource-utilization work (PMID:40624551, n=30 SLC6A1). Parent-report registry data has been formally benchmarked against provider publications and found broadly consistent (PMID:35761184). **No prospective natural history results are yet published** — a UCB-sponsored longitudinal natural history study (NCT07531511) started 2026-07-21.

---

## 2. Etiology

### Primary causal factor

Monogenic. **Heterozygous loss-of-function variants in *SLC6A1***, overwhelmingly de novo, causing reduced GAT-1-mediated GABA reuptake. Haploinsufficiency is the established mechanism (PMID:38781976):

> "De novo variants consistently resulted in a decrease in GABA uptake, in keeping with haploinsufficiency underlying all neurodevelopmental phenotypes."

Contiguous-gene **3p25.3 microdeletions** removing *SLC6A1* together with *SLC6A11* (GAT-3) are a second causal route (PMID:25256099, PMID:39923323, PMID:40517887). **Balanced translocations** disrupting *SLC6A1* have also been reported (PMID:36966012; PMID:29621621, disrupting *SLC6A1* and *NAA15*).

### Genetic risk factors

- **Causal:** de novo missense (majority) and truncating variants; recurrent hotspots p.Gly232Val, p.Ala288Val, p.Val342Met, p.Gly362Arg (PMID:29315614).
- **Constraint (gnomAD v4, retrieved via API):** pLI ≈ **1.0**; LoF observed/expected = **4/72.1 = 0.055**, LOEUF (o/e upper bound) = **0.127**; missense Z = **5.92**; LoF Z = 6.81. Both LoF- and missense-constrained — consistent with observed missense enrichment in patients.
- **Missense vulnerability + CpG hypermutability** explain the clinical picture of recurrent de novo missense (PMID:38781976): "The extent of this missense vulnerability accounts for the clinically observed missense enrichment; overlap with hypermutable CpG sites accounts for the recurrent missense variants."
- **Susceptibility (non-Mendelian) associations** — treat as separate, weaker claims: rare damaging de novo missense in *SLC6A1* is enriched in schizophrenia trios (PMID:31932766); *SLC6A1* has been implicated in ADHD susceptibility with a reported gene-environment interaction (PMID:28442423) and in alcohol-use-disorder risk alongside *GABBR1* (PMID:26727527); a 21-bp promoter insertion polymorphism creates an enhancer element and potentiates promoter activity (PMID:19077666).

### Environmental risk factors

**No established environmental cause.** Advanced paternal age is the generic de-novo-mutation risk factor for this class of disorder but has not been specifically quantified for *SLC6A1*. No toxin, infection, or occupational exposure is implicated in disease causation.

**Seizure/regression triggers** (not causes) are documented: developmental regression episodes were "triggered by seizures, infection, or spontaneously" (PMID:36895422), and hyperventilation exacerbates the spike-wave EEG signature (GeneReviews).

### Protective factors

None genetically established. No protective allele, modifier, or dietary exposure has been reported. Practically, the closest analogue to a "protective factor" is **residual GAT-1 activity**: variants retaining >10% GABA uptake are enriched in milder phenotypes (PMID:37647852).

### Gene–environment interactions

Little formal data. The one specific report is a *SLC6A1* × environment interaction in ADHD susceptibility (PMID:28442423) — this concerns common-variant susceptibility, **not** the Mendelian disorder, and should not be conflated in the KB entry. For the Mendelian disorder, the clinically meaningful "environment" is **pharmacological**: drugs that further reduce GAT-1 function (tiagabine) or that raise GABA tone would be expected to worsen the tonic-inhibition mechanism; levetiracetam is associated with disproportionate behavioral intolerance (GeneReviews).

---

## 3. Phenotypes

### Frequency table (with sources and suggested HP terms — all HP IDs verified non-obsolete via OLS)

| Phenotype | Frequency | Source | HP term |
|---|---|---|---|
| Global developmental delay | >90% | GeneReviews | **HP:0001263** Global developmental delay |
| Intellectual disability (any) | 82–100% (DD/ID combined); ID specifically ~35% in GeneReviews, 28/34 mild-moderate in Johannesen | PMID:42173049; PMID:29315614 | **HP:0001249** Intellectual disability |
| Delayed speech and language development | Most prominent feature; "language impairment being the most common feature" | PMID:29315614 | **HP:0000750** Delayed speech and language development |
| Seizures (any) | 85–90% | GeneReviews; PMID:42173049 | **HP:0001250** Seizure |
| Absence / atypical absence seizures | 60–72% | PMID:42173049 | **HP:0002121** Generalized non-motor (absence) seizure; **HP:0011146** Dialeptic seizure |
| Myoclonic-atonic seizures | 24–35% | PMID:42173049 | **HP:0032794** Myoclonic seizure + **HP:0010819** Atonic seizure |
| Atonic seizures / drop attacks | Common | PMID:42173049; PMID:39889538 | **HP:0010819** Atonic seizure |
| Generalized tonic-clonic seizures | Reported, minority | GeneReviews; PMID:37662110 | **HP:0002069** Bilateral tonic-clonic seizure |
| Focal-onset seizures | <10% | GeneReviews | HP:0007359 Focal-onset seizure |
| Hypotonia | 60–71% | GeneReviews; PMID:42173049 | **HP:0001252** Hypotonia |
| Autism spectrum disorder / autistic features | 22–65% (GeneReviews ~30%; ~1/3 in literature review of 204) | PMID:42173049; PMID:37700749 | **HP:0000717** Autism |
| ADHD / attention deficit | ~15% formal ADHD; attention deficits in 5/5 in one neuropsych series | GeneReviews; PMID:37700749 | **HP:0007018** ADHD; **HP:0000752** Hyperactivity |
| Movement disorder (tremor, ataxia, stereotypies) | ~40% | GeneReviews | **HP:0001251** Ataxia; **HP:0001337** Tremor; **HP:0000733** Motor stereotypy |
| Ataxia specifically | 7/34 (21%) | PMID:29315614 | **HP:0001251** Ataxia |
| Developmental regression | Subset; documented cohort of 24 | PMID:36895422 | **HP:0002376** Developmental regression |
| Sleep disturbance | Common | PMID:34006619; GeneReviews | **HP:0002360** Sleep disturbance |
| GI dysfunction (constipation/diarrhea) | Common | GeneReviews | **HP:0002019** Constipation |
| Aggression / irritability / self-injury | Common | GeneReviews; PMID:37700749 | HP:0000718 Aggressive behavior |
| Anxiety | Reported | PMID:37700749; PMID:39889538 | HP:0000739 Anxiety |
| Abnormal EEG (2–4 Hz generalized spike/polyspike-wave) | 25/31 (81%) | PMID:29315614 | **HP:0002353** EEG abnormality; HP:0010850 EEG with spike-wave complexes |
| Occipital/rhythmic intermittent delta activity (OIRDA) | Characteristic | GeneReviews; PMID:33961861; PMID:39889538 | **HP:0010845** EEG with generalized slow activity |
| Dysmorphic features | **Absent** — "No consistent dysmorphic features" | GeneReviews | — |
| Distinctive neuroimaging | **Absent** — nonspecific white matter changes possible | GeneReviews | (HP:0006808 Cerebral hypomyelination, if present) |

### Phenotype characteristics

**Age of onset.** Cognitive/language concerns typically precede epilepsy. Scoping review (PMID:42173049): "seizure onset typically between 14 months and 5 years… cognitive impairment antedating seizure onset in over 60% of cases." Johannesen: "Epilepsy was diagnosed in 31/34 cases with mean onset at 3.7 years." Motor milestones are relatively spared: sitting ~9 mo (5–13), walking ~19 mo (11–33); language lags harder — babbling ~14 mo (6–36), first words ~25 mo (10–52), phrases ~34 mo (23–54) (GeneReviews).

**Severity.** Highly variable, mild to severe, and **correlated with residual GAT-1 function** (PMID:37647852): "For variants with complete loss of in vitro GABA uptake, we found a 4.6-fold enrichment in patients having severe disease versus non-severe disease (P = 2.9 × 10-3, 95% confidence interval: 1.5-15.3)."

**Progression / course.** Chronic and lifelong; epilepsy is often but not always treatable. Cognitive trajectory can worsen: "After epilepsy onset, cognition deteriorated in 46% (11/24) of cases" (PMID:29315614) and "Three out of five patients underwent at least two neuropsychological evaluations, which revealed a worsening of cognitive functions over time" (PMID:37700749). Regression: "The mean age at regression was 2.7 years and most subjects had regression of language or motor skills triggered by seizures, infection, or spontaneously" (PMID:36895422).

**Adult phenotype** (PMID:37662110, n=15 adults): "9/13 patients had moderate to severe ID… Epilepsy was prevalent (11/15)… Epilepsy was refractory in 7/11, while four patients were seizure free with lamotrigine, valproate, or lamotrigine in combination with valproate… Schizophrenia was not reported in any of the patients." Authors note ID "appeared to be more severe in the adult patients," with ascertainment bias as an alternative explanation.

### Quality-of-life impact

First disease-specific QoL data (PMID:38663152, n=52 across a trial-readiness cohort and Simons Searchlight): mean **QI-Disability 73 ± 12.3**, **QOLCE-55 49 ± 17.1**, **PedsQL Family Impact Module 51 ± 17.6**; proposed clinically significant thresholds QI-Disability <61, QOLCE-55 <46, PedsQL-FIM <42. A longitudinal subset (n=7) showed a decline in the Family Relationship domain (Δ −10.0, P = 0.035).

Per-phenotype QoL drivers (PMID:41066795): "Lower QOLCE-55 total scores were associated with regression, absence seizures, clinical severity, coordination difficulties, and male gender (P < 0.039). Autism severity was significantly associated with lower total scores on all three QoL measures (P < 0.025; ρ = -0.473 to -0.681)." **Autism severity — not seizure burden — is the single most consistent QoL driver across instruments.** This is a curation-relevant, non-obvious finding.

---

## 4. Genetic / Molecular Information

### Causal gene

***SLC6A1*** (hgnc:11042; NCBI Gene 6529; OMIM 137165), 3p25.3, encoding GAT-1 (UniProt P30531), a 599-aa, 12-TM sodium- and chloride-dependent neurotransmitter transporter of the SLC6/NSS (LeuT-fold) family.

UniProt function annotation: *"Mediates transport of gamma-aminobutyric acid (GABA) together with sodium and chloride and is responsible for the reuptake of GABA from the synapse (PubMed:30132828)."* Subcellular location: cell membrane; presynapse. Reverse (efflux) transport is thermodynamically possible depending on membrane potential and ion gradients — relevant to mechanism modeling.

### Pathogenic variants

- **Spectrum:** missense (majority), nonsense, frameshift, splice-site, small intragenic indels; whole-gene deletion is rare. GeneReviews: "Sequence analysis detects >99% of pathogenic variants"; gene-targeted del/dup <1%.
- **Missense:truncating ratio:** 15/21 (71%) missense vs 6/21 (29%) truncating in the Simons Searchlight cohort (PMID:34006619).
- **Structural clustering:** "The GAT1 transmembrane domains 1, 6 and extracellular loop 4 (EL4) were enriched for patient over population variants" (PMID:37647852). Kahen: "Missense variants were largely clustered around the sixth and seventh transmembrane domains, which functions as a GABA binding pocket" (PMID:34006619). Ligand proximity predicts loss of function: "the spatial proximity from the ligand was associated with loss-of-function in the GAT1 transporter activity."
- **ClinVar:** 1,097 *SLC6A1* records (NCBI eSearch, 2026-07-25). A large fraction remain unscored — AJHG 2024 notes "the functional data can inform future reports for the remaining 72% of unscored variants."
- **Population allele frequency:** pathogenic variants are essentially absent from gnomAD (4 observed LoF vs 72 expected across the gene); there is no common risk allele for the Mendelian disorder.
- **Somatic vs germline:** germline. **Somatic/gonadal mosaicism is documented** — a two-sibling pedigree with p.Val125Met absent in the asymptomatic mother, "suggesting gonadal mosaicism" (PMID:33961861).
- **Functional consequence:** **loss of function → haploinsufficiency.** Notably, dominant-negative and gain-of-function effects were specifically sought and **not** found at scale: "recurrent de novo missense variants showed moderate loss-of-function effects that reduced GABA uptake with no evidence for dominant-negative or gain-of-function effects" (PMID:38781976). This directly qualifies an earlier in-vitro observation that mutant GAT-1 can retain wild-type GAT-1 in the ER via aberrant oligomerization (PMID:35911425). **Curate as competing hypotheses (`mechanistic_hypotheses` with `hypothesis_groups`), not as a settled dominant-negative claim.**
- **Two functional sub-classes of LoF missense** (PMID:38781976): "two-thirds of loss-of-function missense variants prevented GAT-1 from being present on the membrane while GAT-1 was on the surface but with reduced activity for the remaining third." This distinction is therapeutically load-bearing — chaperone therapy targets the trafficking-defective two-thirds.
- **Splicing:** a splice-site variant "disrupted canonical splicing of exon 9 in the mRNA transcript, leading to premature protein truncation" (PMID:30132828).

### Modifier genes

None established. Intrafamilial variability is documented (PMID:37502687 and its corrigendum PMID:37638311; PMID:33961861), and a hypomorphic allele (p.Ala334S) has been used to explain part of the variable expressivity (PMID:41174879): "We conclude that the p.A334S variant is a hypomorphic allele and begin to elucidate the underlying variability in SLC6A1-NDD." Allelic severity, not trans-acting modifiers, is the current best explanation.

### Epigenetics

Not implicated in the Mendelian disorder. Separate literature: reduced DNA methylation around the *SLC6A1* promoter in temporal lobe epilepsy (PMID:39344240) — an acquired-epilepsy finding, **do not import into the Mendelian entry**. A 21-bp promoter insertion polymorphism creating an enhancer element is a *cis*-regulatory variant of unclear clinical relevance (PMID:19077666).

### Chromosomal abnormalities

- **3p25.3 microdeletion** encompassing *SLC6A1* + *SLC6A11*: "three novel patients with overlapping proximal microdeletions 3p25.3 of 1.1-1.5 Mb in size showing a consistent non-3p- phenotype with ID, epilepsy/EEG abnormalities, poor speech, ataxia and stereotypic hand movements" (PMID:25256099). Functionally confirmed: "The haploinsufficient GAT-1 and GAT-3 conditions demonstrated reduced GABA uptake and protein expression, comparable to known SLC6A1 missense variants" (PMID:39923323). Also PMID:40517887 (seizures/EEG in 3p deletion involving *SLC6A1*).
- **Balanced translocations** disrupting the locus (PMID:36966012; PMID:29621621).

---

## 5. Environmental Information

- **Environmental factors:** none causal. Not applicable.
- **Lifestyle factors:** none causal. Diet is relevant *therapeutically* (ketogenic diet, low glycemic index therapy) rather than etiologically.
- **Infectious agents:** none causal. Intercurrent infection is a documented **trigger of developmental regression episodes** (PMID:36895422) and, as in any epilepsy, of seizure exacerbation.
- **Iatrogenic/pharmacological environment (the practically important one):** tiagabine is a direct GAT-1 inhibitor (PMID:35676483) and the *Slc6a1* knockout mouse "partially phenocopy[s] the clinical side effects of tiagabine" (PMID:15788781) — mechanistically, GAT-1 inhibitors should be avoided. Levetiracetam is associated with disproportionate behavioral intolerance (GeneReviews). Betaine, an endogenous osmolyte and dietary constituent, is a GAT-1 modulator (PMID:38884791) — a plausible but unproven dietary modifier.

---

## 6. Mechanism / Pathophysiology

### Causal chain (upstream → downstream)

**Node 1 — Molecular lesion (MOLECULAR).** Heterozygous LoF variant in *SLC6A1*. For the trafficking-defective majority: mutant GAT-1 misfolds, is retained in the endoplasmic reticulum, and is degraded. PMID:34028503: "The reduced GABA uptake appears to be due to reduced cell surface expression of the variant transporter caused by variant protein misfolding, endoplasmic reticulum retention, and subsequent degradation." Reviewed in PMID:39268250: "many SLC6A1 mutations are now known to impair protein folding, and consequently fail to reach the plasma membrane."
GO: **GO:0005783** endoplasmic reticulum; GO:0006457 protein folding; GO:0030433 ubiquitin-dependent ERAD pathway; GO:0034976 response to ER stress.

**Node 2 — Reduced cell-surface GAT-1 and reduced GABA uptake (MOLECULAR).** Confirmed across 213 variants by ³H-GABA uptake (PMID:38781976) and in patient iPSC-derived astrocytes and neurons (PMID:34028503). In knock-in mice, "γ-aminobutyric acid transporter 1 protein was markedly reduced in cortex, hippocampus, thalamus and cerebellum in both mutant mouse lines" with **no compensatory GAT-3 upregulation** (PMID:38650830).
GO: **GO:0015812** gamma-aminobutyric acid transport; GO:0005332 GABA:sodium symporter activity; **GO:0005886** plasma membrane; **GO:0098793** presynapse. Modifier: DECREASED.

**Node 3 — Elevated ambient/extracellular GABA and slowed synaptic GABA clearance (CELLULAR).** PMID:35840120: "Reduced GABA uptake is due to decreased functional GAT-1, which, in thalamic astrocytes, could result in increased extracellular GABA accumulation and enhanced tonic inhibition, leading to seizures and abnormal EEGs." In KO mice, "The reduced rate of GABA clearance from the synaptic cleft is probably responsible for the slower decay of spontaneous IPSCs in cerebellar granule cells" (PMID:15788781).
CHEBI: **CHEBI:16865** gamma-aminobutyric acid (INCREASED, extracellular).

**Node 4 — Increased extrasynaptic (δ-subunit) GABA-A receptor tonic conductance (CELLULAR).** PMID:15788781: "The compromised GABA uptake in mGAT1 KO mice results in an increased GABA(A) receptor-mediated tonic conductance in both cerebellar granule and Purkinje cells." Generalized to absence epilepsy by PMID:19966779: "extrasynaptic GABA(A) receptor-dependent 'tonic' inhibition is increased in thalamocortical neurons from diverse genetic and pharmacological models of absence seizures. Increased tonic inhibition is due to compromised GABA uptake by the GABA transporter GAT-1 in the genetic models tested, and GAT-1 is crucial in governing seizure genesis."
GO: GO:1902476 chloride transmembrane transport; GO:0060080 inhibitory postsynaptic potential.

**Node 5 — Thalamocortical network hypersynchrony → spike-wave discharges (TISSUE).** Extrasynaptic GABA-A activation in ventrobasal thalamocortical neurons deinactivates T-type Ca²⁺ currents and promotes burst firing, sustaining the ~3 Hz thalamo-cortico-thalamic oscillation. PMID:19966779: "the selective activation of thalamic extrasynaptic GABA(A) receptors is sufficient to elicit both electrographic and behavioral correlates of seizures in normal rats." Mouse counterpart: "The Slc6a+/A288V mouse, representative of MAE, had increased 5-7 Hz spike-wave discharges and absence seizures" (PMID:35840120); GAT-1^S295L/+ mice "have spike-and-wave discharges with motor arrest consistent with absence-type seizures" (PMID:37501613).
UBERON: **UBERON:0001897** dorsal plus ventral thalamus; **UBERON:0001903** thalamic reticular nucleus; **UBERON:0002596** ventral posterior nucleus of thalamus; **UBERON:0001950** neocortex.

**Node 6 — Developmental arm (TISSUE/ORGANISM).** *SLC6A1* is expressed in the developing brain very early — "abundantly expressed in the developing brain even before the CNS is formed" (PMID:34028503) — so GABAergic signaling is perturbed during circuit assembly, not just in the mature network. New evidence for an interneuron-development defect: human MGE organoids "uncover a previously unreported migration deficit of MGE interneurons in a disease model of SLC6A1 developmental and epileptic encephalopathy, offering potential insights into the developmental contributions to epileptogenesis" (PMID:40631166).
GO: **GO:0021853** cerebral cortex GABAergic interneuron migration; GO:0021894 cerebral cortex GABAergic interneuron development; GO:0007268 chemical synaptic transmission.

**Node 7 — Clinical manifestation (ORGANISM).** Epilepsy (absence, myoclonic-atonic, atonic, GTC), ID/language disorder, ASD, hypotonia, ataxia/tremor, behavioral dysregulation.

### Cell types involved

| Cell type | Role | CL term |
|---|---|---|
| Astrocyte | Astrocytic GAT-1 controls ambient GABA; the thalamic astrocyte pool is the seizure-relevant one | **CL:0000127** astrocyte |
| GABAergic neuron / presynaptic terminal | Neuronal GAT-1 reuptake is non-redundant — "The GABA uptake function of GAT-1 in neurons cannot be compensated for by other GABA transporters" (PMID:34028503) | **CL:0000617** GABAergic neuron |
| Cortical interneuron (incl. PV+, MGE-derived) | Migration deficit in organoid model | **CL:0010011** cerebral cortex GABAergic interneuron; **CL:4023018** pvalb GABAergic interneuron |
| Thalamocortical (relay) neuron | Site of pathological tonic conductance | **CL:0000679** glutamatergic neuron |
| Cerebellar granule cell, Purkinje cell | Increased tonic conductance; substrate for tremor/ataxia | **CL:0000120** granule cell; **CL:0000121** Purkinje cell |

### Protein dysfunction and structure

GAT-1 is a LeuT-fold Na⁺/Cl⁻-coupled symporter. The full-length human GAT-1 cryo-EM structure with tiagabine (PMID:35676483) provides the structural frame used for variant interpretation: "Our structure reveals that tiagabine locks GAT1 in the inward-open conformation, by blocking the intracellular gate of the GABA release pathway, and thus suppresses neurotransmitter uptake." Machine-learning/homology modeling consistently predicts that pathogenic missense variants **destabilize global protein conformation** (PMID:35840120; PMID:31176687; PMID:33961861 — the last quantifying p.Val125Met at "~30% of the wildtype").

### Metabolic, immune, and tissue-damage arms

- **Metabolic:** no primary metabolic defect. The ketogenic diet's efficacy (PMID:27600546) has prompted speculation about a diet–GABA-reuptake interaction, explicitly framed as a hypothesis: "An effect of the diet on gamma-aminobutyric acid reuptake mediated by gamma-aminobutyric acid transporter protein 1 is suggested."
- **Immune system:** **not implicated.** No autoimmune or inflammatory component.
- **Tissue damage:** no neurodegeneration, gliosis, or structural lesion is characteristic. Neuroimaging is typically normal. One outlier case describes a "Globus Pallidus Lesion With Iron Deposition and Dopaminergic Denervation" (PMID:38515990) — a single-case observation, not a disease feature.

### Molecular profiling

- **Transcriptomics:** *SLC6A1* longitudinal and cell-type-specific expression across human brain development was analyzed in PMID:33241211. Disease-specific patient transcriptomics: **not available**.
- **Proteomics / metabolomics / lipidomics:** **not available** for this disorder.
- **Functional genomics:** two scalable variant-effect platforms now exist — the ³H-GABA uptake MAVE-style survey of 213 variants (PMID:38781976) and a high-throughput GABA-fluorescence imaging assay (PMID:41279425). No CRISPR/RNAi modifier screen has been published.
- **Single-cell / organoid:** MGE organoid + cortical organoid fusion model (PMID:40631166); patient iPSC-derived astrocytes and neurons (PMID:34028503); a heterozygous G307R patient iPSC line, FINi007-A (PMID:41248596).

---

## 7. Anatomical Structures Affected

**Organ level.** Brain only (**UBERON:0000955**). Body system: **nervous system**. No primary involvement of other organ systems; GI symptoms (constipation/diarrhea) are common but are best modeled as secondary/comorbid rather than as primary organ involvement.

**Regional.** Thalamus (**UBERON:0001897**; thalamic reticular nucleus **UBERON:0001903**; ventrobasal complex **UBERON:0002596**) — the pacemaker of the spike-wave rhythm; cerebral cortex / neocortex (**UBERON:0000956**, **UBERON:0001950**); hippocampal formation (**UBERON:0002421**); cerebellar cortex (**UBERON:0002129**) — tremor/ataxia substrate, and the region where increased tonic conductance was first demonstrated. GAT-1 loss was confirmed in "cortex, hippocampus, thalamus and cerebellum" of both knock-in lines (PMID:38650830).

**Tissue/cell level.** Nervous tissue; GABAergic neurons and astrocytes (see table in §6). Note the transporter division of labor: GAT-3 (*SLC6A11*) "is only abundantly expressed in the thalamus and there was no compensatory increase of γ-aminobutyric acid transporter 3 in either of the mutant mouse lines" (PMID:38650830).

**Subcellular level.** Plasma membrane (**GO:0005886**) and presynaptic membrane (**GO:0098793**) — the normal destination; endoplasmic reticulum (**GO:0005783**) — the pathological destination; synapse (**GO:0045202**); Golgi apparatus (GO:0005794) — trafficking checkpoint.

**Lateralization.** Bilateral and generalized; there is no focal or lateralized anatomical signature. EEG abnormalities are generalized, with an occipital-predominant rhythmic delta component (OIRDA).

---

## 8. Temporal Development

**Onset.** Pediatric. Developmental concerns (language, hypotonia) in infancy/toddlerhood; epilepsy onset "typically between 14 months and 5 years" (PMID:42173049), mean 3.7 years in the Johannesen cohort. Onset pattern: **insidious for the developmental phenotype, acute/episodic for seizures**. Cognitive impairment precedes epilepsy in >60% of cases — clinically important because it argues the neurodevelopmental phenotype is **not** simply epileptic encephalopathy secondary to seizures.

**Stages.** No formal staging system exists. A pragmatic natural-history framing from the literature:
1. **Infancy** — hypotonia, feeding/motor mildness, emerging language delay; often no seizures.
2. **Early childhood (1.5–5 y)** — epilepsy onset (absence/myoclonic-atonic), EEG 2–4 Hz generalized spike-wave, possible regression episodes (mean 2.7 y).
3. **Mid-childhood** — seizure control achievable in many (20/31 became seizure-free, PMID:29315614), but cognition may deteriorate post-onset in ~46%.
4. **Adolescence/adulthood** — persistent ID (moderate-severe in 9/13 adults), refractory epilepsy in >60% of adults with epilepsy, ongoing behavioral/psychiatric burden; EEG rhythmic delta bursts "persisting from childhood to adulthood" (PMID:39889538).

**Progression rate.** Slow/variable; not a neurodegenerative course. **Duration:** chronic, lifelong.

**Remission.** Seizure remission is treatment-induced and common in childhood series (VPA-led); spontaneous remission is not documented. Cognitive/behavioral features do not remit.

**Critical periods.** Two, both actionable:
- **Regression window** ~2–3 years, seizure/infection/spontaneously triggered (PMID:36895422).
- **Therapeutic window for gene replacement** — the strongest preclinical efficacy signal is developmentally gated: "our data demonstrate compelling efficacy when mice are treated at an early development age" (PMID:39589822). Early diagnosis therefore has mechanistic, not merely administrative, value.

---

## 9. Inheritance and Population

**Prevalence/incidence.** GeneReviews: *"Fewer than 500 individuals have been reported worldwide, with an estimated incidence of 2.65 in 100,000 births."* Converted for dismech `Prevalence` structure: `measure_type: BIRTH_PREVALENCE` (best fit for an "incidence per births" statement), `rate_per_100000: 2.65`, `prevalence_class: BAND_1_9_PER_100000`. A second, cohort-based framing: pathogenic *SLC6A1* variants account for **~4% of unsolved MAE** (6/160; PMID:25865495) and a **1.7% diagnostic yield in 460 unselected epilepsy patients** (PMID:30132828). Reported case count now exceeds 300 (PMID:39889538) and *SLC6A1*-NDD is described as "one of the most common monogenic disorders reported in genetic databases" (PMID:41066795) — the gap between reported cases and estimated birth incidence implies substantial under-ascertainment.

**Inheritance pattern.** Autosomal dominant, predominantly **de novo**. HP:0000006 Autosomal dominant inheritance.

**Penetrance.** Incomplete (GeneReviews). Rare inherited cases have parents with milder phenotypes (learning difficulties, epilepsy, behavior disorder) — the p.Ala334S hypomorph family being the best-characterized (PMID:41174879).

**Expressivity.** Highly variable, including **intrafamilial** variability (PMID:37502687; PMID:33961861).

**Genetic anticipation.** Not applicable — no repeat expansion.

**Germline/gonadal mosaicism.** Documented (PMID:33961861). GeneReviews recurrence-risk figure: **~1%** when both parents test negative.

**Founder effects.** None reported. Recurrent variants arise independently at hypermutable CpG sites, not by descent (PMID:38781976).

**Consanguinity.** Not relevant (dominant, de novo).

**Carrier frequency.** Not applicable.

**Population demographics.** No ethnic or geographic predilection reported; cohorts are international (US, Europe, Korea, China, Turkey, India). **Sex ratio:** no established skew; note that male sex was associated with lower QOLCE-55 scores (PMID:41066795), an outcome rather than incidence finding. **Age distribution:** ascertained population is heavily pediatric; adults are "likely underrecognized due to limited genetic testing availability" (GeneReviews).

---

## 10. Diagnostics

### Genetic testing (the definitive route)

Diagnosis requires a heterozygous pathogenic/likely pathogenic *SLC6A1* variant plus a compatible phenotype (GeneReviews). Recommended approach: **epilepsy multigene panel or comprehensive exome/genome sequencing**, preferred over single-gene testing; sequence analysis detects >99% of pathogenic variants, del/dup analysis <1%.

- **WES/WGS** (MAXO:0009004 clinical whole-exome sequencing): first-line for unexplained DD/epilepsy; the route by which most cases have been found.
- **Gene panels:** any epilepsy/DEE or ID/ASD panel including *SLC6A1*.
- **Chromosomal microarray:** required to detect 3p25.3 microdeletions involving *SLC6A1* ± *SLC6A11* (PMID:25256099; PMID:39923323).
- **Karyotype/FISH:** low yield, but relevant for balanced translocations disrupting the locus (PMID:36966012; PMID:29621621) — consider when CMA is normal and there is a familial rearrangement.
- **mtDNA testing, repeat expansion testing:** not applicable.
- **Variant interpretation aids:** the SLC6A1 portal (https://slc6a1-portal.broadinstitute.org/) with structure-mapped pathogenicity (PMID:37647852); functional GABA-uptake data for 213 variants (PMID:38781976); high-throughput GABA-fluorescence assay for prospective VUS resolution (PMID:41279425); *Drosophila* allelic-series assay for hard VUS (PMID:41174879). **Functional assay is the most useful VUS-resolution tool in this gene**, given the 72% of ClinVar entries unscored.

### Electrophysiology (MAXO:0000932 electroencephalography)

The disorder's most informative non-genetic test. GeneReviews: *"2-4 Hz spike and wave discharges, exacerbated by hyperventilation, and intermittent rhythmic delta activity, especially in the occipital region."* Johannesen: "irregular bursts of diffuse 2.5-3.5 Hz spikes/polyspikes-and-slow waves in 25/31"; two patients developed an ESES-like pattern. OIRDA is a recurring signature (PMID:33961861; PMID:39889538).

**Emerging quantitative EEG biomarker** (PMID:41893060): "Patients with SLC6A1-NDD exhibited significantly elevated delta power (19.4 ± 4.1) compared to controls (14.2 ± 3.0; p < 0.001)"; delta power increased with age in patients but declined in controls; wake-epoch classifier AUC = 0.93. Cross-platform concordance (EEGLAB vs Persyst) was imperfect (R² = 0.644) — the authors flag pipeline standardization as a prerequisite. This is the leading candidate objective endpoint for trials.

### Laboratory tests and biomarkers

**No diagnostic blood, urine, or CSF biomarker exists.** No enzyme assay, no metabolite signature. Plasma/CSF GABA is not an established diagnostic test. This is a genuine gap: current biomarker development is entirely qEEG-based, with a possible future imaging biomarker — a GAT-1 PET tracer, **[18F]GATT-44**, is in first-in-human evaluation (NCT07457736, Yale, recruiting, start 2026-04), which would give direct target-engagement readout for chaperone and gene therapy trials.

### Imaging

Brain MRI is typically **normal**; "No distinctive neuroimaging findings; nonspecific white matter changes possible" (GeneReviews). MRI's role is exclusionary.

### Biopsy / pathology

Not applicable — no diagnostic histopathology.

### Clinical criteria and differential diagnosis

No consensus diagnostic criteria for the gene-defined disorder; ILAE criteria for **epilepsy with myoclonic-atonic seizures** apply to the MAE subgroup (16/34 fulfilled MAE criteria in PMID:29315614). Differential (GeneReviews):

| Differential | Distinguishing feature |
|---|---|
| GABA-A receptor epilepsies (*GABRA1*, *GABRB2*, *GABRB3*, *GABRG2*) | Overlapping GABAergic mechanism; distinguished by gene |
| *GLUT1* deficiency (*SLC2A1*) | Overlapping DD+epilepsy+movement disorder triad; low CSF glucose/CSF:blood glucose ratio; ketogenic diet is disease-specific therapy. Direct phenotype comparison published: PMID:40311539 |
| Rett syndrome (*MECP2*) | Regression, hand stereotypies, acquired microcephaly, female predominance |
| Angelman syndrome (*UBE3A*) | Characteristic EEG, ataxic gait, happy demeanor, absent speech |
| Sodium channelopathies (*SCN1A/2A/8A*) | Febrile seizure onset, different seizure semiology and drug responses |
| *CHD2*, *CACNA1A* | Also acetazolamide-responsive DD/epilepsy/ataxia triads (PMID:41131961) |
| Other DEE genes (*STXBP1* etc.) | Panel/exome resolves |

### Screening

No newborn screening. No carrier screening (dominant, de novo). **Cascade testing** of parents is indicated for recurrence-risk counseling and to detect mildly affected/mosaic carriers.

---

## 11. Outcome / Prognosis

**Survival/mortality.** GeneReviews: *"It is unknown whether life expectancy in individuals with SLC6A1-NDD is reduced."* Survival into adulthood is documented. No published mortality rate, no SUDEP incidence estimate specific to this gene. **Explicitly not available** — an important gap to record rather than to fill by analogy.

**Morbidity/disability.** The dominant burden is lifelong intellectual and communication disability plus behavioral dysregulation, not seizure mortality. Adults: moderate-to-severe ID in 9/13; refractory epilepsy in 7/11 of those with epilepsy (PMID:37662110). Some individuals never develop verbal language despite better receptive communication (GeneReviews) — a strong argument for early AAC.

**Quality-of-life measures.** See §3. QOLCE-55 performed best as a disease-sensitive instrument; autism severity was the strongest cross-instrument driver (PMID:41066795; PMID:38663152).

**Healthcare burden.** Neurology is the most frequent specialty encounter; diagnosis reshapes rather than reduces utilization — "significant changes in types of HRU suggest that diagnosis leads to more appropriate care and treatment" (PMID:40624551).

**Complications.** Developmental regression episodes; status epilepticus including de novo absence status (PMID:37877664); ESES-like EEG evolution (PMID:29315614); injury from atonic drop attacks; sleep disruption; feeding/GI issues; caregiver/family strain.

**Recovery potential.** Skills lost in regression may or may not be recovered (PMID:36895422). Seizure freedom is attainable (20/31 in the childhood cohort) but does **not** reliably translate to cognitive gain: "There was no clear-cut correlation between seizure control and cognitive outcome" (PMID:29315614). **This decoupling should be modeled explicitly** — it is the central reason the field has moved to disease-modifying rather than purely anti-seizure therapy.

**Prognostic factors.** Residual GAT-1 uptake activity is the best-supported molecular prognostic marker (<10% residual → 4.6-fold enrichment for severe disease; PMID:37647852). Clinical prognostic markers: presence of regression, autism severity, absence seizures, coordination difficulty (all associated with lower QoL; PMID:41066795). **Prognostic biomarkers:** none validated; delta power is the leading candidate.

---

## 12. Treatment

### Antiseizure pharmacotherapy

MAXO: **MAXO:0000167** anticonvulsant agent therapy; NCIT:C15986 Pharmacotherapy for the generic action with `therapeutic_agent` bound to CHEBI (all CHEBI IDs below verified via OLS).

| Drug | Evidence | CHEBI |
|---|---|---|
| **Valproate** — first-line | "Twenty of 31 patients became seizure-free, with valproic acid being the most effective drug" (PMID:29315614); reaffirmed as "the most consistently effective antiseizure medication" (PMID:42173049) | **CHEBI:39867** valproic acid |
| **Lamotrigine** | Second-line; adults seizure-free on LTG or LTG+VPA (PMID:37662110; PMID:42173049) | **CHEBI:6367** lamotrigine |
| **Clobazam** | Third-line per scoping review (PMID:42173049) | **CHEBI:31413** clobazam |
| **Ethosuximide** | Effective for the absence component; bidirectionally modulates SWDs in GAT-1^S295L/+ and GAT-1^+/− mice (PMID:37501613; PMID:42173049) | **CHEBI:4887** ethosuximide |
| **Acetazolamide (adjunctive)** | Exploratory case series, n=6: "Three (50%) patients achieved full seizure remission, and the remaining three patients had a reduction in seizure frequency ranging from 50 to 90%"; mean dose 16.2 mg/kg/day over 30 months; 3/4 with ataxia improved (PMID:41131961) | **CHEBI:27690** acetazolamide |
| **Levetiracetam — use with caution** | GeneReviews: "Individuals with SLC6A1-NDD have intolerable behavioral side effects with levetiracetam at higher rates than reported in the general population." Scoping review softens this to "behavioral adverse effects should be monitored" (PMID:42173049) | **CHEBI:6437** levetiracetam |
| **Tiagabine — mechanistically contraindicated** | Direct GAT-1 inhibitor locking the transporter inward-open (PMID:35676483); KO mice "partially phenocopy the clinical side effects of tiagabine" (PMID:15788781). *Inference from mechanism, not from a clinical trial — label accordingly.* | **CHEBI:9586** tiagabine |

### Dietary therapy

MAXO: **MAXO:0030010** ketogenic diet intake (or MAXO:0000088 dietary intervention). Ketogenic diet supported by case-level response (PMID:27600546) and endorsed as an "evidence-supported adjunctive option" (PMID:42173049); low glycemic index therapy reported in drug-refractory *SLC6A1* MAE (PMID:38443714).

### Disease-modifying: pharmacological chaperone (4-phenylbutyrate)

The most advanced repurposing program. Rationale: restore trafficking of ER-retained mutant **and** wild-type GAT-1, exploiting the fact that every patient retains one normal allele.

- **Preclinical:** "4-Phenylbutyrate increased γ-amino butyric acid uptake in both mouse and human astrocytes and neurons bearing the variants… 4-phenylbutyrate alone increased γ-amino butyric acid transporter 1 expression and suppressed spike wave discharges in heterozygous knockin mice" (PMID:35911425).
- **Mechanism resolved:** "PBA restored GABA uptake and GAT-1 surface expression across all variants, and TUDCA mimicked the effects of PBA. HDAC inhibitors exhibited modest rescue in vitro but failed to restore GAT-1 function or mitigate seizures in the knockin mice… PBA acts as a pharmacochaperone, not an HDAC inhibitor" (PMID:42157447). TUDCA (**CHEBI:80774**) is therefore a rational second chaperone candidate.
- **Beyond seizures:** PBA improved motor and sleep phenotypes in Slc6a1^+/S295L mice, "supporting its potential as a disease-modifying therapy" (PMID:41385967).
- **Clinical:** Phase Early-1 **NCT04937062** (glycerol phenylbutyrate / Ravicti; Weill Cornell; STXBP1 + SLC6A1 DEE; active, not recruiting). Scoping review summary: "4-phenylbutyrate restores GAT-1 trafficking in endoplasmic reticulum-retained variants and has demonstrated seizure reduction in 80% and seizure freedom in 40% of treated patients in the largest clinical cohort" (PMID:42173049).
- **Real-world safety/efficacy** (PMID:42447769, n=18 STXBP1+SLC6A1): "Among 11 children with uncontrolled seizures, 8 showed improvement (all with ≥50% seizure reduction), resulting in a 73% seizure response rate. Nearly all families (17/18) reported improvements in development." Toxicity: mild (sedation, decreased appetite, nausea) in 14/18, resolving in 2–10 days; **one severe event — "metabolic acidosis and aspiration pneumonia requiring intubation."**
- **3p25.3 deletion patients** also showed benefit: "Post-treatment EEGs showed a moderate reduction in epileptiform discharges following PBA administration, and patients exhibited improved motor function" (PMID:39923323).

CHEBI: **CHEBI:41500** 4-phenylbutyric acid; **CHEBI:134745** glycerol phenylbutyrate. Therapeutic modality: SMALL_MOLECULE.

### Disease-modifying: gene replacement therapy

MAXO: **MAXO:0001001** gene therapy. Modality: GENE_THERAPY.

- **Preclinical** (PMID:39589822): AAV9 vectors with JeT or MeP promoters. "Neonatal intracerebroventricular administration of either vector resulted in significantly normalized EEG patterns in Slc6a1-/- or Slc6a1+/- mice as well as improvement in several behavioral phenotypes." Critically: "our treatments in the heterozygous mice, which genotypically match human patients, have resulted in stronger benefits," while neonatal treatment carried "some mortality and adverse effects."
- **Clinical:** **NCT07173153**, "Gene Therapy for SLC6A1 Neurodevelopmental Disorder," AAV9.SLC6A1, Phase 1/2, enrolling by invitation, start 2025-08-25, sponsor Emily de los Reyes (Nationwide Children's). **First patient dosed December 2025** (PMID:42173049).
- **Combination strategy** in preprint: 4-PBA plus gene augmentation as dual therapy (PMID:42327277) — preprint, not peer-reviewed; flag accordingly.

### Other advanced modalities

- **RNA-based therapies (ASO, siRNA):** none in development for *SLC6A1*. Note the mechanistic mismatch — haploinsufficiency calls for allele upregulation, so a TANGO-style splice-modulating or upregulating ASO would be the theoretically apt design, but none is published. AJHG 2024 frames the therapeutic goal precisely: "Strategies to increase the expression of the wild-type SLC6A1 allele are likely to be beneficial across neurodevelopmental disorders" (PMID:38781976).
- **Cell therapy, immunotherapy, targeted oncology-style therapy:** not applicable.
- **Surgery:** no role. Epilepsy is generalized; resective surgery is not indicated. VNS/corpus callosotomy for drop attacks would follow generic refractory-generalized-epilepsy practice — no *SLC6A1*-specific evidence.

### Supportive, rehabilitative, and behavioral care

Per GeneReviews (MAXO terms in brackets): speech-language therapy with early consideration of AAC devices [**MAXO:0000930** speech therapy]; physical therapy [**MAXO:0000011**]; occupational therapy [**MAXO:0001351**]; developmental/educational support [MAXO:0009101 early intervention services]; gastroenterology evaluation for GI dysfunction; multidisciplinary coordination and family/social-work support [**MAXO:0000950** supportive care].

Behavioral/psychiatric pharmacotherapy: stimulants for ADHD; **risperidone or aripiprazole** (FDA-approved for irritability in ASD) for irritability/aggression; sleep hygiene plus melatonin, clonidine, or trazodone for sleep disturbance (GeneReviews).

### Pharmacogenomics

No CPIC/PharmGKB guideline specific to *SLC6A1*. The relevant "pharmacogenomic" logic is **genotype-mechanism-guided rather than metabolism-guided**: chaperone therapy is predicted to benefit trafficking-defective/ER-retained variants (about two-thirds of LoF missense) more than surface-expressed-but-inactive variants (the remaining third) (PMID:38781976). Curate as a personalized-medicine hypothesis, not established practice.

### Treatment algorithm (synthesized)

1. Confirm genetic diagnosis → 2. First-line valproate; add lamotrigine and/or ethosuximide by seizure type; clobazam as adjunct → 3. Monitor for levetiracetam behavioral intolerance; avoid GAT-1 inhibitors → 4. If drug-resistant: ketogenic diet or low glycemic index therapy; consider adjunctive acetazolamide → 5. Concurrently and from diagnosis: speech/AAC, PT/OT, behavioral and sleep management → 6. Consider trial enrollment (phenylbutyrate, AAV9 gene therapy, natural history) — noting the developmentally gated therapeutic window.

---

## 13. Prevention

**Primary prevention.** Not possible for de novo dominant disease. No vaccination, exposure modification, or population-level intervention applies.

**Secondary prevention (early detection).** The dominant actionable lever. Early genetic testing is explicitly recommended: PMID:39889538 concludes the electroclinical/neurodevelopmental profile "suggest[s] the importance of early genetic testing for SLC6A1-NDD diagnosis." Because gene-therapy efficacy is developmentally gated (PMID:39589822) and cognitive impairment precedes epilepsy in >60% (PMID:42173049), shortening time-to-diagnosis has direct therapeutic consequence — the HRU study makes the same argument from the health-systems side: stakeholders "should consider the value of an early diagnosis to improve long-term outcomes" (PMID:40624551). No newborn screening program includes *SLC6A1*.

**Tertiary prevention.** Seizure control to reduce regression risk (seizures are a documented regression trigger, PMID:36895422); avoidance of behaviorally destabilizing and mechanistically counterproductive drugs; injury prevention for atonic drop attacks (protective headgear); sleep and behavioral management; surveillance of development, seizures, movement disorder, and GI symptoms at each visit (GeneReviews).

**Genetic counseling.** MAXO:**MAXO:0000079** genetic counseling. 50% transmission risk from an affected individual; ~1% empiric recurrence risk to siblings when both parents test negative, due to possible parental gonadal mosaicism — a risk that is not theoretical here (PMID:33961861). Prenatal and preimplantation genetic testing are available once the familial variant is known (GeneReviews).

**Immunization, public health, environmental interventions, prophylaxis.** Not applicable.

---

## 14. Other Species / Natural Disease

**Taxonomy and orthologs** (NCBI Gene IDs retrieved via eSearch):

| Species | NCBI Taxon | Gene | NCBI Gene ID |
|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | *SLC6A1* | 6529 |
| *Mus musculus* | NCBITaxon:10090 | *Slc6a1* | 232333 |
| *Rattus norvegicus* | NCBITaxon:10116 | *Slc6a1* | 79212 |
| *Danio rerio* | NCBITaxon:7955 | *slc6a1a* / *slc6a1b* | 492490; 568985 |
| *Drosophila melanogaster* | NCBITaxon:7227 | *Gat* (GABA transporter) | used for allelic-series modeling (PMID:41174879) |

**Naturally occurring disease in other species.** **None reported.** No OMIA entry for a naturally occurring *SLC6A1* disorder in companion animals or livestock; no wildlife disease. All animal disease is experimentally induced.

**Breed-specific disease (VBO).** Not applicable — no breed predisposition described.

**Comparative biology.** GAT-1 is deeply conserved across bilaterians; the SLC6/NSS fold is conserved back to bacterial LeuT, which is precisely why LeuT-based homology models were used for variant interpretation before the human cryo-EM structure existed (PMID:35676483). The disease mechanism is functionally conserved: mouse KO reproduces tremor, ataxia, and increased cerebellar tonic conductance (PMID:15788781); *Drosophila* expressing patient variants "confirm phenotypes in flies… consistent with a partial loss-of-function mechanism" (PMID:41174879). This cross-phylum reproducibility is the strongest argument that the primary lesion is transporter function per se, not a human-specific interaction.

**Zoonotic potential / cross-species transmission.** Not applicable — genetic disorder.

---

## 15. Model Organisms

### Mouse (primary system)

| Model | Type | Phenotype recapitulation | Reference |
|---|---|---|---|
| *Slc6a1*^−/− (GAT1 KO) | Constitutive knockout | "motor disorders, including gait abnormality, constant 25-32 Hz tremor… reduced rotarod performance, and reduced locomotor activity"; prepulse-inhibition deficit; increased GABA-A tonic conductance in cerebellar granule and Purkinje cells; reduced body weight; normal lifespan | PMID:15788781 |
| *Slc6a1*^+/− | Heterozygous null — **genotypically matches patients** | Spike-wave discharges; EEG normalized by AAV9 gene therapy | PMID:39589822; PMID:37501613 |
| *Slc6a1*^+/A288V | Patient-variant knock-in (partial LoF) | "increased 5-7 Hz spike-wave discharges and absence seizures"; ER-retained ring-like GAT-1 distribution | PMID:35840120; PMID:38650830 |
| *Slc6a1*^+/S295L | Patient-variant knock-in (complete LoF) | SWDs with motor arrest; bidirectional pharmacosensitivity to ethosuximide and NO-711 (GAT-1^−/− insensitive to both); prolonged neonatal righting reflex, reduced locomotion, reduced hanging, altered sleep — all PBA-responsive | PMID:37501613; PMID:41385967; PMID:38650830 |

**Key modeling insight for KB curation:** the homozygous null is the *worse* model for translation. PMID:39589822: "the severe homozygous KO model is more refractory to treatment, whereas our treatments in the heterozygous mice, which genotypically match human patients, have resulted in stronger benefits." Curate mouse-derived efficacy claims with `evidence_source: MODEL_ORGANISM` and note zygosity.

**Model limitations.** Mice do not model language, autism, or intellectual disability in any construct-valid way — precisely the domains that dominate patient QoL. Absence-type SWDs and motor phenotypes are well captured; the neurodevelopmental core is not. This is a legitimate `HUMAN_MODEL_MISMATCH` discussion candidate for the dismech entry.

### Human cellular and organoid systems

- **Patient iPSC-derived astrocytes and neurons** — showed that "the loss of GABA uptake function and endoplasmic reticulum retention is consistent across induced pluripotent stem cell-derived cell types, including astrocytes and neurons" (PMID:34028503). Deposited line: **FINi007-A**, heterozygous G307R (PMID:41248596).
- **MGE organoids fused to cortical organoids** — revealed an interneuron **migration deficit** in an SLC6A1 DEE model (PMID:40631166). Preprint; verify on peer-reviewed publication before curating as established.
- **HEK293T / HeLa heterologous expression with ³H-GABA uptake and surface biotinylation** — the workhorse assay across the variant-function literature (PMID:30132828; PMID:31176687; PMID:33961861; PMID:38781976).
- **High-throughput GABA-fluorescence imaging assay** for scalable variant classification (PMID:41279425; preprint).

### Invertebrate

***Drosophila melanogaster*** allelic series expressing patient *SLC6A1* variants, used to resolve a VUS (p.Ala334S) as a hypomorph (PMID:41174879).

### Databases and resources

MGI (mouse *Slc6a1*), RGD (rat), ZFIN (zebrafish *slc6a1a/b*), FlyBase, Alliance of Genome Resources, IMSR/KOMP for allele availability, Cellosaurus/hPSCreg for FINi007-A, and the disease-specific **SLC6A1 portal** (Broad) for variant-level function.

---

## Curation notes for the dismech entry

1. **Ontology gap to flag:** MONDO lacks a gene-defined "SLC6A1-related neurodevelopmental disorder" class; MONDO:0014633 is seizure-syndrome-scoped and already used by `Epilepsy_with_Myoclonic_Atonic_Seizures.yaml`. Consider a MONDO term request and, meanwhile, an explicit `notes` statement plus `differentials` linking the two entries.
2. **Module conformance candidates:** `epilepsy_excitation_inhibition_imbalance` (conform at `#Excitation-Inhibition Imbalance`, but with an inverted sign — this disorder produces *excess tonic inhibition* in thalamus, an instructive edge case worth a `mechanistic_hypotheses` note rather than a silent conformance). Also consider a trafficking/ER-retention pattern — this disorder shares the misfolding→ER-retention→degradation→pharmacochaperone-rescue chain with CFTR/ΔF508 (explicitly drawn as an analogy in PMID:35911425), which may warrant a new "misfolded membrane protein ER retention" module if other dismech entries share it.
3. **Competing-mechanism curation:** dominant-negative oligomerization (PMID:35911425, in vitro) vs pure haploinsufficiency (PMID:38781976, 213-variant scale). Use `hypothesis_groups` on the relevant causal edges; the large-scale functional data currently favors haploinsufficiency.
4. **Evidence-source discipline:** the therapeutic literature is heavily MODEL_ORGANISM and IN_VITRO. Only PMID:41131961 (acetazolamide, n=6), PMID:42447769 (PBA parent-report, n=18), PMID:29315614 / PMID:37662110 (ASM effectiveness in cohorts) are HUMAN_CLINICAL, and none is randomized. The scoping review explicitly names this: "Critical gaps include the absence of prospective natural history data with standardized outcomes, lack of randomized controlled trials, and incomplete characterization of the adult phenotype" (PMID:42173049).
5. **Preprints to hold:** PMID:42327277, PMID:41648160, PMID:41279425, PMID:40631166, PMID:39399018 are bioRxiv/medRxiv. Note that PMID:39399018 (medRxiv) and PMID:41174879 (*HGG Adv*) are the same work — cite the journal version.
6. **Clinical trials to include:** NCT07173153 (AAV9 gene therapy, Ph1/2), NCT04937062 (glycerol phenylbutyrate, Early Ph1), NCT07531511 (UCB prospective natural history), NCT01238250 (Simons Searchlight registry), NCT07457736 ([18F]GATT-44 GAT-1 PET, healthy volunteers — relevant as a future biomarker, not a treatment).

---

## Sources

- [SLC6A1-Related Neurodevelopmental Disorder — GeneReviews (NCBI Bookshelf)](https://www.ncbi.nlm.nih.gov/books/NBK589173/)
- [SLC6A1–Related Neurodevelopmental Disorder: A Scoping Review — Pediatr Neurol 2026 (PMID:42173049)](https://www.sciencedirect.com/science/article/pii/S0887899426001293)
- [Current knowledge of SLC6A1-related neurodevelopmental disorders — Brain Commun 2020 (PMID:33241211)](https://academic.oup.com/braincomms/article/2/2/fcaa170/5922604)
- [Common molecular mechanisms of SLC6A1 variant-mediated NDDs in astrocytes and neurons — Brain 2021 (PMID:34028503)](https://doi.org/10.1093/brain/awab207)
- [AAV9/SLC6A1 gene therapy rescues abnormal EEG patterns — J Clin Invest 2024 (PMID:39589822)](https://www.jci.org/articles/view/182235)
- [The phenotypic presentation of adult individuals with SLC6A1-related NDDs — Front Neurosci 2023 (PMID:37662110)](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1216653/full)
- [Phenotypic similarities and differences between SLC6A1-NDD and GLUT1 deficiency — Seizure 2025 (PMID:40311539)](https://www.sciencedirect.com/science/article/abs/pii/S1059131125001001)
- [AAV9.SLC6A1 Gene Therapy in SLC6A1 — NCT07173153](https://ichgcp.net/clinical-trials-registry/NCT07173153)
- [SLC6A1-related Neurodevelopmental Disorder — NORD](https://rarediseases.org/rare-diseases/slc6a1-epileptic-encephalopathy/)
- PubMed/NCBI E-utilities (abstracts, ClinVar counts, Gene IDs), ClinicalTrials.gov API v2, gnomAD GraphQL API, EMBL-EBI OLS4 API, UniProt REST — all queried 2026-07-25.