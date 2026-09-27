---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-04T23:21:34.837573'
end_time: '2026-08-04T23:40:35.779956'
duration_seconds: 1140.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Focal Cortical Dysplasia Type II
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
  web_search_requests: 5
  num_turns: 56
  total_cost_usd: 4.713958999999999
  session_id: 2be1bd42-97bb-43bd-bd3d-cb20092e774d
  stop_reason: end_turn
citation_count: 11
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Focal Cortical Dysplasia Type II
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Focal Cortical Dysplasia Type II** covering all of the
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

# Focal Cortical Dysplasia Type II — Comprehensive Research Report

**Prepared:** 2026-08-04 · **Target entity:** MONDO:0011818 (isolated focal cortical dysplasia type II) · **Intended use:** dismech knowledge-base entry population

> **Verification note for the curator.** Every ontology identifier in this report marked ✅ was resolved locally with OAK against `sqlite:obo:{mondo,hp,go,cl,uberon,chebi,hgnc}` during preparation. Identifiers marked ⚠️ (chiefly NCIT and OMIM) were **not** machine-verified and must be checked with `just validate-terms` before commit. Direct quotes are reproduced verbatim from PubMed abstracts retrieved via NCBI E-utilities; each is tagged with its PMID. Two citations are flagged as needing a `just fetch-reference` round-trip before use as evidence snippets.

---

## 1. Disease Information

### 1.1 Overview

Focal cortical dysplasia type II (FCD II) is a **focal, sporadic malformation of cortical development (MCD)** in which a circumscribed region of neocortex fails to laminate normally and contains characteristic abnormal cell types. It is the single most important surgically remediable cause of drug-resistant focal epilepsy in children, and a major cause in adults.

The defining lesion is **cortical dyslamination plus dysmorphic neurons**, with or without balloon cells. As the 2022 ILAE update review states (PMID:35163267):

> "Type II focal cortical dysplasia (FCD) is a neuropathological entity characterised by cortical dyslamination with the presence of dysmorphic neurons only (FCDIIA) or **the presence of both dysmorphic neurons and balloon cells (FCDIIB)**."

Mechanistically, FCD II is now understood not as an idiopathic developmental accident but as a **mosaic mTORopathy** — a somatic (post-zygotic) genetic disease of a clonal patch of cortical progenitors and their progeny. Baldassari et al. put this categorically (PMID:31444548):

> "We show that panel-negative FCD2 cases display strong pS6-immunostaining, stressing that **all FCD2 are mTORopathies**."

The lesion sits on a mechanistic continuum with hemimegalencephaly (HME) and tuberous sclerosis complex (TSC) cortical tubers; the same genes, hit at different developmental times and in different progenitor pools, produce lesions of different size (PMID:29281825).

### 1.2 Key identifiers

| Resource | Identifier | Label |
|---|---|---|
| MONDO ✅ | `MONDO:0011818` | isolated focal cortical dysplasia type II |
| MONDO ✅ | `MONDO:0017101` | isolated focal cortical dysplasia type IIa |
| MONDO ✅ | `MONDO:0017102` | isolated focal cortical dysplasia type IIb |
| MONDO ✅ (parent) | `MONDO:0019009` | isolated focal cortical dysplasia |
| OMIM ⚠️ | `OMIM:607341` | FOCAL CORTICAL DYSPLASIA, TYPE II (xref from MONDO) |
| Orphanet | `ORPHA:268994` (type II); `ORPHA:269001` (IIa); `ORPHA:269008` (IIb) | |
| MeSH | `C537067` | |
| UMLS | `C1846385` (II); `C1846386` (IIa); `C5679768` (IIb) | |
| MedGen | `339510` (II); `375876` (IIa); `1842232` (IIb) | |
| GARD | `0010190` (II); `0017270` (IIa); `0017271` (IIb) | |
| HPO ✅ | `HP:0032051` Focal cortical dysplasia type II; `HP:0032052` type IIa; `HP:0032053` type IIb | |
| HPO ✅ (parents) | `HP:0032046` Focal cortical dysplasia; `HP:0002539` Cortical dysplasia | |
| ICD-10 | `Q04.3` (other reduction deformities of brain) — non-specific; FCD has no dedicated ICD-10 code | |
| ICD-11 | `LA05.4` / `8A6Z` region — malformations of cortical development; no FCD-II-specific stem code | |

**Note on ICD:** neither ICD-10 nor ICD-11 codes FCD II specifically. Coding in practice is by epilepsy type (`G40.2` focal symptomatic epilepsy) plus the malformation code. Flag this as a `KNOWLEDGE_GAP` if the entry carries ICD mappings.

### 1.3 Synonyms and alternative names (from MONDO ✅)

- FCD type II / FCD II / FCDII / FCD2
- **Cortical dysplasia, Taylor type** / focal cortical dysplasia of Taylor / cortical dysplasia of Taylor (the historical eponym, after Taylor's 1971 description)
- Taylor-type cortical dysplasia
- CDT, FCDT, FCORD2 (related synonyms)
- FCD IIa = "focal cortical dysplasia with dysmorphic neurons"
- FCD IIb = "focal cortical dysplasia with dysmorphic neurons and balloon cells"; historically overlapping with "forme fruste of tuberous sclerosis"

### 1.4 Provenance of the evidence base

The FCD II literature is overwhelmingly **surgical-series based** — resected tissue from tertiary epilepsy surgery centers. This creates a systematic **ascertainment bias toward drug-resistant, surgically-accessible, MRI-visible lesions**. The largest disease-level resource is the European Epilepsy Brain Bank series of 9,523 surgical specimens (PMID:29069555). Genetic data derive from matched blood–brain deep sequencing of surgical cohorts. There is essentially **no population-based EHR-derived FCD II cohort**; individuals with FCD II who are seizure-free or never surgically evaluated are largely invisible to the literature. Curators should record this as a `HUMAN_MODEL_MISMATCH`-adjacent limitation — the phenotype spectrum is defined by the surgically-treated tail of the distribution.

---

## 2. Etiology

### 2.1 Primary causal factors — somatic mosaicism in the PI3K–AKT–mTOR pathway

FCD II is caused by **post-zygotic (somatic) mosaic variants restricted to the brain**, in genes of the mTOR (mechanistic target of rapamycin) signaling cascade. Two mutually exclusive genetic architectures produce the same downstream state — constitutive mTORC1 hyperactivation:

**Architecture 1 — single somatic gain-of-function hit in an mTOR *activator*.**
Somatic activating missense variants in `MTOR`, and less commonly `AKT3`, `PIK3CA`, `RHEB`. One hit suffices because these are dominant activating changes.

**Architecture 2 — two-hit loss-of-function in an mTOR *repressor*.**
A germline (usually inherited or de novo constitutional) loss-of-function allele in `DEPDC5`, `NPRL2`, `NPRL3` (the GATOR1 complex) or `TSC1`/`TSC2`, plus a **somatic second hit** in the same gene occurring in a cortical progenitor. The somatic hit removes the remaining wild-type allele in a clonal patch — a Knudson-style two-hit mechanism transplanted from oncology into a non-neoplastic developmental disease.

The Pract Neurol review states this cleanly (PMID:36823117):

> "FCDs are caused either by **single somatic activating mutations in MTOR pathway genes or by double-hit inactivating mutations with a constitutional and a somatic loss-of-function mutation in repressors of the signalling pathway**."

Baldassari et al. resolved the architecture-to-subtype mapping empirically (PMID:31444548):

> "Somatic gain-of-function variants in MTOR and its activators (AKT3, PIK3CA, RHEB), as well as germline, somatic and two-hit loss-of-function variants in its repressors (DEPDC5, TSC1, TSC2) were found **exclusively in FCD2/HME cases**."

And demonstrated the second hit directly:

> "Single-cell microdissection followed by sequencing of enriched pools of DNs unveiled a **somatic second-hit loss-of-heterozygosity in a DEPDC5 germline case**."

A 2025 clinical case study confirms the diagnostic utility of hunting the second hit (PMID:40742146):

> "Identification of the second somatic hit in brain tissue (DEPDC5 c.982C>T, p.(Arg328*)) confirmed the two-hit situation in this patient and supported disease causality of the germline variant."

**Timing determines lesion size.** D'Gama et al. showed that mutations in the same gene produce (PMID:29281825):

> "a disease continuum from FCD to HME to bilateral brain overgrowth"

reflecting **when during dorsal telencephalic progenitor expansion the mutation arose**. Earlier hit → larger clone → larger lesion (hemimegalencephaly, megalencephaly); later hit → small clone → focal, sometimes bottom-of-sulcus, dysplasia.

### 2.2 Genetic risk factors

**Causal / driver genes** (all ✅ HGNC-verified):

| Gene | HGNC | Role in pathway | Variant class in FCD II | Typical origin |
|---|---|---|---|---|
| `MTOR` | `hgnc:3942` | mTOR kinase, catalytic core of mTORC1 | GoF missense (kinase/FAT domain) | Brain somatic |
| `AKT3` | `hgnc:393` | PI3K–AKT effector upstream of mTORC1 | GoF missense (e.g. p.Glu17Lys) | Brain somatic |
| `PIK3CA` | `hgnc:8975` | PI3K catalytic α subunit | GoF hotspot missense | Brain somatic |
| `RHEB` | `hgnc:10011` | Small GTPase, direct mTORC1 activator | GoF missense; a reported **doublet** variant | Brain somatic |
| `DEPDC5` | `hgnc:18423` | GATOR1 complex, mTORC1 repressor | LoF (nonsense/frameshift/splice) | Germline + somatic 2nd hit |
| `NPRL2` | `hgnc:24969` | GATOR1 complex | LoF | Germline + somatic 2nd hit |
| `NPRL3` | `hgnc:14124` | GATOR1 complex | LoF | Germline + somatic 2nd hit |
| `TSC1` | `hgnc:12362` | TSC1–TSC2 complex, mTORC1 repressor | LoF | Germline and/or brain somatic |
| `TSC2` | `hgnc:12363` | TSC1–TSC2 complex (GAP for RHEB) | LoF | Germline and/or brain somatic |
| `SLC35A2` | `hgnc:11022` | UDP-galactose transporter | LoF | Brain somatic — **causes MOGHE/FCD I, NOT FCD II** |
| `PIK3R2` | `hgnc:8980` | PI3K regulatory subunit | GoF | Reported in the megalencephaly spectrum |

⚠️ **Critical curation guardrail:** `SLC35A2` belongs to the **mild MCD / MOGHE / FCD I** arm, not FCD II. Baldassari et al. (PMID:31444548) are explicit that these are "two distinct genetic entities." Do **not** curate `SLC35A2` as an FCD II gene.

**Detection rates (highly cohort- and method-dependent):**

| Study | Cohort | Yield |
|---|---|---|
| Lim et al. 2015, Nat Med (PMID:25799227) | 77 FCDII | `MTOR` somatic in **15.6% (12/77)** |
| Lim et al. 2017, AJHG (PMID:28215400) | 40 `MTOR`-negative FCDII | `TSC1`/`TSC2` somatic in **12.5% (5/40)** |
| D'Gama et al. 2017, Cell Rep (PMID:29281825) | 66 FCD/HME | etiology in **41% (27/66)** |
| Baldassari et al. 2019, Acta Neuropathol (PMID:31444548) | 80 surgical MCD | **63% of FCD2/HME** elucidated; 29% of mMCD/FCD1 |
| Zhang et al. 2023, Neurobiol Dis (PMID:37149062) | literature synthesis | 292 patients with somatic mTOR-activating variants reviewed |

Lim's 2016 review gives the mosaicism magnitude (PMID:26779999):

> "Our recent study on FCD utilizing various deep sequencing platforms identified somatic mutations in MTOR (**existing as low as 1% allelic frequency**) only in the affected brain tissues."

**Variant allele fraction (VAF)** in bulk resected tissue is typically **1–5%**, occasionally <1%, reflecting the small fraction of mutation-carrying cells. Baldassari et al. observed a dose relationship:

> "We further observed **a correlation between the density of pathological cells and the variant-detection likelihood.**"

This is the single most important technical fact for diagnostics: standard clinical exome/genome on blood is **negative by design** for the single-hit architecture.

**Modifier and susceptibility loci:** none established. There is no published GWAS of FCD II — the disease is not polygenic and case numbers are far too small. A Bonn cohort found family history of epilepsy had only "a marginal influence on long-term outcomes" (PMID:34177771), which is the closest thing to a modifier signal in the literature.

### 2.3 Environmental risk factors

**No established environmental cause.** FCD II is a cell-autonomous genetic lesion arising during corticogenesis. Specifically:

- No association with maternal infection, teratogen exposure, prematurity, or perinatal hypoxia has been reproducibly demonstrated for FCD II (as distinct from FCD IIId, which is *defined* by an early acquired lesion).
- HHV-6 has been detected in a minority of FCD surgical specimens — "six of 23 with focal cortical dysplasia (FCD)" were HHV-6 positive (PMID:34324277) — but the study's own conclusion attributes a possible role only to mesial temporal sclerosis, not FCD. Treat any HHV-6–FCD causal claim as **unsupported**; if curated at all, curate as `supports: NO_EVIDENCE` or as a `KNOWLEDGE_GAP` discussion.
- Age, sex, and family history are not established risk factors for FCD II itself.

### 2.4 Protective factors

None identified. No protective allele, dietary factor, or exposure has been described. This is expected for a stochastic somatic-mutation disease.

### 2.5 Gene–environment interactions

**Not applicable in the conventional sense.** The one clinically meaningful "interaction" is **gene × developmental timing**: the same variant produces FCD, HME, or bilateral overgrowth depending on the developmental window in which it arises (PMID:29281825). Curate this as a temporal/developmental modifier of the genetic lesion, not as a G×E interaction.

A second, therapy-relevant interaction is **genotype × drug response** — see §12.

---

## 3. Phenotypes

### 3.1 Core seizure phenotype

| Phenotype | HPO ✅ | Type | Frequency | Onset | Course |
|---|---|---|---|---|---|
| Focal-onset seizure | `HP:0007359` | Clinical sign | Near-universal; **90.2%** in a 112-child FCDII cohort (PMID:31368639) | Infancy–childhood | Recurrent |
| Drug-resistant epilepsy | (use `HP:0011146` Dialeptic seizure / `HP:0001250` Seizure + `modifier`) | Clinical | Defining feature of surgical series; **74%** pharmacoresistance in a 124-child FCD cohort (PMID:35985831 — ⚠️ abstract not directly retrieved; verify before quoting) | Early | Progressive/refractory |
| Epileptic spasms | (`HP:0012469` Infantile spasms — ⚠️ verify) | Clinical sign | **20.5%** of young children with FCDII (PMID:31368639) | Infancy | Age-dependent |
| Focal to bilateral tonic–clonic seizure | `HP:0032662` (evolving into bilateral convulsive status epilepticus) ✅ | Clinical sign | Common; an adverse surgical prognostic marker (PMID:34177771) | Variable | Episodic |
| Status epilepticus | `HP:0002133` ✅ | Clinical sign | Occasional | Variable | Episodic |
| Seizure (generic parent) | `HP:0001250` ✅ | | | | |

The Lancet Neurology review frames the clinical variability (PMID:19679275):

> "**Clinical presentation is variable, and depends on age of onset of seizures and the location and size of lesion.** As FCD type II cannot be diagnosed with certainty in the clinic, in vivo identification by use of MRI is important."

Seizures in FCD II are typically **frequent, brief, stereotyped, and cluster-prone**, often with prominent nocturnal/hypermotor semiology when frontal — which overlaps clinically with sleep-related hypermotor epilepsy (relevant to the `DEPDC5-Related_Epilepsy` and `Familial_Sleep_Related_Hypermotor_Epilepsy` entries already in the KB).

### 3.2 Neurodevelopmental and cognitive phenotypes

| Phenotype | HPO ✅ | Frequency | Notes |
|---|---|---|---|
| Developmental delay / intellectual disability | `HP:0001249` (Intellectual disability) | **49.1%** moderate/severe pre-surgical developmental delay in children with onset ≤6 y (PMID:31368639) | Correlates with earlier seizure onset |
| Developmental regression | `HP:0002376` | Present in the epileptic-encephalopathy subgroup | |
| Epileptic encephalopathy | (curate via seizure + regression terms) | **12.5%** of young FCDII children (PMID:31368639) | "associated with earlier epilepsy onset and higher rate of bilateral onset on ictal EEG" |
| Autism / autistic behaviour | `HP:0000717` | Reported in mTORopathy cohorts generally; not well quantified for isolated FCD II | ⚠️ frequency not evidenced — omit `frequency:` |
| Focal neurological deficit (hemiparesis, visual field defect) | (lesion-location dependent) | Uncommon pre-operatively; usually post-surgical | |

The strongest quantitative statement (PMID:31368639):

> "Before surgery, **49.1% showed moderate/severe developmental delay**, associated with earlier seizure onset and higher rate of history of epileptic encephalopathy (OR = 0.740, 5.160, P = .023, .042)."

And the sobering corollary on reversibility:

> "For 48 children with preoperatively moderate/severe developmental delay, **DQ rank at 6 months postsurgery was improved in only four cases**."

### 3.3 Onset, severity, progression

- **Age of onset:** typically **infancy to early childhood**. Median onset age **0.9 years (range 0.01–5.9)** in the Peking University young-child FCDII cohort (PMID:31368639). Adult-onset FCD II exists but is the minority — in the European brain bank, "focal cortical dysplasia was the most common type [of MCD], **52.7% of cases of which were in children**" (PMID:29069555).
- **Latency to surgery is long.** Across all epilepsy-surgery diagnoses, "the mean duration of epilepsy before surgical resection was **20.1 years among adults and 5.3 years among children**" (PMID:29069555). This diagnostic delay is itself a major morbidity driver.
- **Severity:** variable; determined by lesion size, eloquence of location, and age at onset.
- **Progression:** the *lesion* is static (a fixed developmental malformation), but the *epilepsy* behaves as a chronic, often refractory condition. There is debate about a superimposed degenerative element — the Lancet Neurol review notes "There seem to be both **neurodevelopmental abnormalities and possible premature neurodegeneration in FCD**" (PMID:19679275). Curate that as an `EMERGING` mechanistic hypothesis, not settled fact.
- **Course pattern:** chronic, lifelong absent successful surgery; episodic seizures with clustering.

### 3.4 Quality-of-life impact

No FCD-II-specific EQ-5D/SF-36/PROMIS data were located. Extrapolate cautiously from drug-resistant focal epilepsy generally. Domains most affected: driving eligibility, employment, educational attainment, injury risk, medication burden, caregiver burden in pediatric cases, and SUDEP anxiety. Post-surgical seizure freedom is associated with substantial QoL gain — the BOSD series reports "33 (87%) patients are seizure-free, **31 off antiseizure medication**" (PMID:33947776), medication discontinuation being a proxy for QoL benefit. **Flag QoL as a `KNOWLEDGE_GAP`.**

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes and pathogenic variants

**Prototype variant (the founding observation), Lim et al. 2015 (PMID:25799227):**

> "we used deep whole-exome sequencing (read depth, 412–668×) validated by site-specific amplicon sequencing (100–347,499×) in paired brain-blood DNA from four subjects with FCDII and uncovered a **de novo brain somatic mutation, mechanistic target of rapamycin (MTOR) c.7280T>C (p.Leu2427Pro)** in two subjects."

> "Deep sequencing of the MTOR gene in an additional 73 subjects with FCDII using hybrid capture and PCR amplicon sequencing identified **eight different somatic missense mutations** found in multiple brain tissue samples of ten subjects. The identified mutations accounted for **15.6% of all subjects with FCDII studied (12 of 77)**. The identified mutations induced the **hyperactivation of mTOR kinase**."

**Variant characteristics:**

- **Type/class:** predominantly **missense** for activators (`MTOR`, `AKT3`, `PIK3CA`, `RHEB`); predominantly **truncating** (nonsense, frameshift, canonical splice) for repressors (`DEPDC5`, `NPRL2`, `NPRL3`, `TSC1`, `TSC2`). One `RHEB` case carried a **doublet** (adjacent dinucleotide) variant.
- **Functional consequence:** **gain of function** for activators; **loss of function** for repressors. Both converge on mTORC1 hyperactivation. `TSC1`/`TSC2` variants act by disrupting complex assembly — "All mutations disrupted TSC1-TSC2 complex formation, hyperactivating mTOR signaling" (PMID:28215400).
- **Somatic vs germline:** activator variants are **brain-restricted somatic**, absent from blood/saliva. Repressor variants are typically **germline (blood-detectable) plus a brain-restricted somatic second hit**.
- **Allele frequency in population databases:** the somatic driver variants are, by definition, **absent from gnomAD** as germline variants. Many of the `MTOR` hotspots overlap oncogenic hotspots catalogued in **COSMIC**. Germline `DEPDC5` LoF variants are present in gnomAD at low frequency and are associated with reduced-penetrance familial focal epilepsy.
- **ACMG classification:** somatic drivers are best classified against oncology-style somatic frameworks (AMP/ASCO/CAP tiers) rather than germline ACMG. Germline `DEPDC5` VUS reclassification is directly enabled by finding the somatic second hit (PMID:40742146).

### 4.2 Cell-type localization of the mutant allele

Two independent lines of evidence place the mutation in the abnormal cells themselves.

Baldassari et al., by laser microdissection (PMID:31444548):

> "Analysis of microdissected cells demonstrated that **DNs and BCs carry the pathogenic variants**."

The 2025 *Nature Neuroscience* single-nucleus study refines this (PMID:40307383):

> "**Mutations were detected in distinct cell types, including glutamatergic neurons and astrocytes**," with "**a small fraction of mutated cells**" exhibiting cytomegalic features.

That last clause is important and under-appreciated: **most mutation-carrying cells are morphologically normal**. Curate this as a distinct mechanistic node — the mutant clone is larger than the histologically abnormal patch.

### 4.3 Modifier genes

None established. The strongest modifier candidate is **the degree of mTORC1 hyperactivation itself**, which behaves as a graded severity determinant — demonstrated experimentally rather than genetically (PMID:30700531):

> "Constitutively active Rheb (RhebCA), the canonical activator of mTOR complex 1 (mTORC1), was expressed in mouse embryos of either sex via in utero electroporation at **low, intermediate, and high concentrations to induce different mTORC1 activity levels** in developing cortical neurons."

### 4.4 Epigenetics

Direct epigenomic (methylome/ChIP) data on FCD II are sparse. Available data are transcriptional and spatial rather than epigenetic. **Flag as `KNOWLEDGE_GAP`.** Relevant adjacency: DNA-methylation classifiers have been developed for MOGHE/`SLC35A2` lesions, and analogous classifier work on FCD II is an active area but not yet a validated diagnostic.

### 4.5 Chromosomal abnormalities

**Not a feature.** FCD II is not caused by aneuploidy, translocation, or copy-number change. Chromosomal microarray on blood is expected to be normal and is **not** a first-line test. Somatic copy-neutral loss of heterozygosity (LOH) in brain tissue is the exception — it is the mechanism of the second hit in some `DEPDC5` cases (PMID:31444548).

---

## 5. Environmental Information

- **Environmental factors:** none established (see §2.3).
- **Lifestyle factors:** none causal. Post-diagnosis, sleep deprivation, alcohol, and missed antiseizure medication doses are recognized **seizure precipitants**, not disease causes.
- **Infectious agents:** none established. The HHV-6 detection in a subset of FCD specimens (PMID:34324277) is unexplained and confounded; it should not be curated as an etiology.

This section is genuinely thin, and that is a positive finding, not a gap: FCD II's etiology is fully accounted for by somatic genetics in the majority of characterized cases.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain (proposed pathograph)

```
[MOLECULAR] Somatic GoF variant in mTOR activator (MTOR/AKT3/PIK3CA/RHEB)
            OR germline + somatic 2nd-hit LoF in repressor (DEPDC5/NPRL2/NPRL3/TSC1/TSC2)
            arising in a dorsal telencephalic radial glial progenitor
                                    ↓
[MOLECULAR] Constitutive mTORC1 hyperactivation
            (readout: pS6 Ser235/236, pS6 Ser240/244, p4E-BP1)
                                    ↓
[CELLULAR]  Excess cap-dependent translation, cell-size dysregulation,
            suppressed autophagy, altered progenitor differentiation trajectory
                                    ↓
[CELLULAR]  Impaired radial neuronal migration  +  cytomegaly
                                    ↓
[TISSUE]    Cortical dyslamination; dysmorphic neurons (± balloon cells);
            grey–white junction blurring; white-matter heterotopic neurons
                                    ↓
[TISSUE]    Altered synaptic/receptor composition (GluN2C-containing NMDARs,
            HCN channel changes); interneuron abnormality; local inflammation
                                    ↓
[ORGANISM]  Intrinsically epileptogenic cortical zone → focal seizures
                                    ↓
[ORGANISM]  Drug-resistant focal epilepsy; developmental impairment
```

### 6.2 Molecular pathway

**PI3K–AKT–mTORC1** is the sole established pathway. Suggested GO terms (all ✅ verified):

| GO term | Label | Use |
|---|---|---|
| `GO:0031929` | TOR signaling | Parent process |
| `GO:0038202` | TORC1 signaling | Precise complex-level process |
| `GO:0032008` | positive regulation of TOR signaling | With `modifier: INCREASED` |
| `GO:0001764` | neuron migration | With `modifier: DECREASED` |
| `GO:0021895` | cerebral cortex neuron differentiation | With `modifier: ABNORMAL` |
| `GO:0006914` | autophagy | With `modifier: DECREASED` (see GATOR1 subtype below) |
| `GO:0007399` | nervous system development | Broad context |
| `GO:0006954` | inflammatory response | Balloon-cell region (see §6.6) |

The GATOR1 complex (`DEPDC5`/`NPRL2`/`NPRL3`) acts as a **GTPase-activating protein for RagA/B**, gating mTORC1 activation in response to amino acids (notably leucine and arginine). `TSC1`–`TSC2` acts as the GAP for `RHEB`. Both are brakes; FCD II is what happens when a brake fails in one clonal patch.

### 6.3 Genotype → histopathology mapping (a curation-grade distinction)

A 2023 deep genotype–phenotype analysis found that the two genetic architectures produce **different lesions** (PMID:37946310):

> "Participants with **GATOR1 variants showed only FCDIIa presentation with a distinctive vacuolizing phenotype**, while those with mTOR variants presented both subtypes. GATOR1-related cases predominantly involved frontal lobe lesions with '**subtle or negative MRI findings**' yet achieved seizure freedom after surgery in most cases, whereas **mTOR variants showed 'larger lesions on MRI including the white matter, suggesting compromised neural cell migration**.'"

The paper's own framing — **"the GATOR1-altered autophagocytic subtype IIa" vs. "MTOR-altered migration deficient subtype IIb"** — is a strong candidate for two `mechanistic_hypotheses` groups or two `has_subtypes` entries in a dismech entry. This is arguably the most curation-actionable finding of the last five years for FCD II.

### 6.4 Cellular processes

- **Impaired radial migration.** Demonstrated causally by in utero electroporation of mutant `MTOR` (PMID:25799227): "Focal cortical expression of mutant MTOR by in utero electroporation in mice was sufficient to **disrupt neuronal migration** and cause spontaneous seizures and cytomegalic neurons."
- **Cytomegaly.** Dysmorphic neurons are defined by soma diameter **>25 μm** (ILAE 2022 criteria, PMID:35706131) with abnormal cytoskeletal (neurofilament) accumulation.
- **Autophagy suppression.** Enriched in the dysmorphic-neuron compartment — spatial transcriptomics found "the DNs region in a gene enrichment network enriched for the **mTOR signalling pathway, autophagy and the ubiquitin–proteasome system**" (PMID:39614299).
- **Aberrant differentiation trajectory.** The 2026 organoid model found "**aberrant differentiation trajectories leading to premature upper-layer neuron generation**" (PMID:41789478).

### 6.5 Protein dysfunction

- `MTOR` GoF missense cluster in the **FAT and kinase domains**, relieving autoinhibition → constitutive kinase activity.
- `TSC1`/`TSC2` LoF → failure of **TSC1–TSC2 complex assembly** → unopposed RHEB-GTP → mTORC1 on (PMID:28215400).
- `DEPDC5` truncation → loss of GATOR1 GAP activity toward RagA/B → mTORC1 insensitive to amino-acid withdrawal.
- Downstream: hyperphosphorylation of **S6K1 → rpS6** (the pS6 immunostain that defines the lesion histologically) and **4E-BP1** (releasing eIF4E, driving cap-dependent translation).

### 6.6 Immune system involvement

Not autoimmune, but **local innate immune activation is a real and spatially-resolved feature**. The 2024 spatial transcriptomics study (PMID:39614299) localizes it specifically to balloon cells:

> "the '**BCs region**' showed '**stronger expression of components of the inflammatory response and complement activation**.'"

This suggests a two-compartment model within a single FCD IIb lesion: dysmorphic neurons = mTOR/autophagy/proteostasis compartment; balloon cells = inflammation/complement compartment. Suggested terms: `GO:0006954` (inflammatory response) ✅, complement activation (⚠️ `GO:0006956` — verify), `CL:0000129` microglial cell ✅.

### 6.7 Electrophysiological / biochemical abnormalities

Two mechanistically distinct, recently-characterized hyperexcitability mechanisms:

**GluN2C-containing NMDA receptors** (PMID:38717560, Epilepsia 2024, rat model):

> "neurons expressing the mutant protein displayed an **excessive activation of GluN2C NMDAR-mediated spontaneous excitatory postsynaptic currents**."

The effect was **developmentally windowed (postnatal days 9–20)** and reversed by GluN2C-selective inhibitors — an appealing precision target, but note this is `MODEL_ORGANISM` evidence only.

**HCN4 and synaptic drive** (PMID:40512428, Epilepsia 2025):

> "FMCD neurons display a complex set of alterations, including **dendrite hypertrophy associated with decreased rheobase**."

**Interneuron involvement.** A 2025 histological review flags "emerging evidence regarding **inhibitory interneuron populations**" in FCD II epileptogenesis (PMID:41487994) — i.e., the excitation/inhibition imbalance is not purely an excitatory-neuron story. This links directly to the KB's existing `epilepsy_excitation_inhibition_imbalance` module.

### 6.8 Molecular profiling summary

| Modality | Key finding | PMID | Evidence source |
|---|---|---|---|
| Single-nucleus genotyping + transcriptomics | Mutations in glutamatergic neurons and astrocytes; "cell-type-specific transcriptional dysregulations in **both mutated and nonmutated FCDII cells**," incl. synapse and neurodevelopment pathways | 40307383 | HUMAN_CLINICAL (surgical tissue) |
| Spatial transcriptomics (FCD IIb) | DN region = mTOR/autophagy/UPS; BC region = inflammation/complement | 39614299 | HUMAN_CLINICAL |
| snRNA-seq + spatial (FCD **I**) | Excitatory neurons and astrocytes most altered; aberrant EN–astrocyte ligand–receptor signaling | 42068085 | HUMAN_CLINICAL — ⚠️ **FCD type I, not II**; use only as contrast |
| Human cortical organoids (`DEPDC5` mosaic) | Increased mTOR activity rescued by rapamycin; dysmorphic-like neurons; premature upper-layer neurogenesis | 41789478 | IN_VITRO |
| Proteomics / metabolomics / lipidomics | **No FCD-II-specific datasets located** | — | `KNOWLEDGE_GAP` |

The bystander finding in PMID:40307383 — transcriptional dysregulation in **non-mutated** cells — deserves its own pathophysiology node. It implies non-cell-autonomous spread of dysfunction beyond the mutant clone, which has direct surgical implications (how much do you resect?).

---

## 7. Anatomical Structures Affected

### 7.1 Organ and region level

| Structure | UBERON ✅ | Involvement |
|---|---|---|
| Brain | `UBERON:0000955` | Primary organ |
| Cerebral cortex | `UBERON:0000956` | Primary site — the dysplastic cortex |
| Frontal lobe | `UBERON:0016525` | **Most common lobe.** FCD IIa "represent[s] approximately 9% of epilepsy surgery cases, **predominantly in frontal lobes**" (PMID:35706131 — ⚠️ verify the 9% figure against the full text before quoting) |
| Cerebral hemisphere white matter | `UBERON:0002437` | Subcortical white matter — site of the transmantle radial band and heterotopic neurons |
| Lobe of cerebral hemisphere | `UBERON:0016526` | Generic lobar container |

**Lobar distribution:** frontal > temporal > parietal > occipital. Frontal predominance is especially marked for **GATOR1-related FCD IIa** (PMID:37946310). Extratemporal location is the norm, distinguishing FCD II from hippocampal sclerosis.

**Lateralization:** FCD II is **unilateral and focal by definition**. Bilateral or multifocal findings should prompt reconsideration (TSC, HME spectrum, or a diffuse MCD). Curate as `unilateral`, `focal`.

**Bottom-of-sulcus dysplasia (BOSD)** is a clinically important anatomic variant: a small FCD II confined to the depth of a single sulcus, easily missed on MRI, with excellent outcomes from limited resection (PMID:33947776). The 2022 ILAE update notes "Bottom-of-sulcus FCD localization in frontal sulci correlates with favorable surgical outcomes."

### 7.2 Tissue and cell level

| Cell type | CL ✅ | Role |
|---|---|---|
| Pyramidal neuron | `CL:0000598` | Substrate of dysmorphic neurons (cytomegalic, >25 μm, abnormal neurofilament) |
| Glutamatergic neuron | `CL:0000679` | Mutation-carrying population (PMID:40307383) |
| Astrocyte | `CL:0000127` | Mutation-carrying population; transcriptionally dysregulated |
| Microglial cell | `CL:0000129` | Inflammatory compartment, BC region |
| Oligodendrocyte | `CL:0000128` | "compromised oligodendroglial populations" in FCD IIb (PMID:35706131) |
| Oligodendrocyte precursor cell | `CL:0002453` | Relevant to the MOGHE contrast |

**Balloon cells** have no dedicated Cell Ontology term. They are large, opalescent, eosinophilic cells with eccentric nuclei and a **mixed glioneuronal immunophenotype** — co-expressing vimentin, nestin, GFAP(-δ), SOX2, and sometimes neuronal markers — consistent with an arrested/undifferentiated progenitor. This is a genuine **OBO gap**; recommend curating with `preferred_term: balloon cell` and either omitting `term:` or binding to a neural-progenitor parent with an explicit note. ⚠️ Do not invent a CL id.

**Diagnostic immunohistochemistry:**
- **pS6 (Ser235/236 and Ser240/244)** — the mTOR-activation readout; strongly positive in DNs and BCs even in panel-negative cases (PMID:31444548).
- **SMI-32 / non-phosphorylated neurofilament** — highlights dysmorphic neurons.
- **Vimentin, nestin, GFAP** — balloon cells.
- **CD34** — a genuinely subtype-discriminating marker (PMID:27885945): "Distinct **nonendothelial cellular CD34 staining was found exclusively in tissue from patients with MRI-positive FCD Type IIB**."
- **NeuN** — demonstrates dyslamination and white-matter heterotopic neurons.

### 7.3 Subcellular level

Suggested GO Cellular Component terms (⚠️ verify all with OAK before use): `GO:0031931` TORC1 complex; `GO:0005764` lysosome (the mTORC1 activation platform — Rag GTPases recruit mTORC1 to the lysosomal surface, and this is precisely where GATOR1 acts); `GO:0005776` autophagosome; `GO:0005886` plasma membrane (NMDAR/HCN localization).

The **lysosomal surface** is the single most mechanistically important compartment: it is where amino-acid sufficiency is sensed, where GATOR1/Rag/RHEB converge, and therefore where FCD II genetics is physically enacted.

---

## 8. Temporal Development

### 8.1 Onset

- **Lesion onset:** prenatal — during **cortical neurogenesis and radial migration**, roughly gestational weeks 6–20 depending on the progenitor pool hit. The lesion is fully formed at birth.
- **Seizure onset:** typically **infancy to early childhood**. Median **0.9 years** in a young-onset FCDII cohort (PMID:31368639); median surgical age in that cohort **4.1 years (0.8–16.2)**.
- **Onset pattern:** seizures begin **acutely and recur**, often with rapid establishment of a high seizure burden. Not insidious.

### 8.2 Progression

- **Stages:** there is no formal staging system. A practical clinical staging is: (1) seizure onset → (2) failure of ≥2 appropriate antiseizure medications (= drug-resistant epilepsy by ILAE definition, usually within 1–2 years) → (3) presurgical evaluation → (4) surgery → (5) post-surgical outcome.
- **Rate:** the malformation is **static**. The epilepsy is chronic and, if untreated surgically, tends toward cumulative cognitive and psychosocial morbidity rather than lesion growth.
- **Course:** chronic, refractory, episodic seizures.
- **Duration:** lifelong absent curative surgery.

### 8.3 Patterns

- **Spontaneous remission:** rare. FCD II is characteristically pharmacoresistant from early on.
- **Treatment-induced remission:** achievable and common with **complete resection** — see §11. This is one of the few epilepsies where "cure" is a realistic word.
- **Critical periods:**
  - *Developmental*: the prenatal window during which the somatic hit occurs determines lesion extent (PMID:29281825).
  - *Therapeutic*: early surgery is advocated to protect development, though the evidence on developmental rescue is mixed. Note the pair of findings — young children benefit for seizures ("88.4% achieved seizure-free," PMID:31368639) but not reliably for cognition (only 4/48 improved DQ at 6 months) — while a comparative study found seizure outcome "**favorable in the whole population (72.6% were classified in Engel's Class Ia+Ic), independently from age at surgery**" (PMID:28410464). Curate this tension explicitly as a `KNOWLEDGE_GAP` discussion rather than asserting that early surgery rescues cognition.
  - *Mechanistic*: the GluN2C hyperexcitability window in the rat model was **P9–P20** (PMID:38717560), suggesting an age-restricted pharmacological opportunity — but this is model-organism evidence and its human translation is unknown. This is a textbook `HUMAN_MODEL_MISMATCH` candidate.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

**Precise population prevalence is not established.** FCD II is defined histopathologically, so ascertainment requires surgery. Available anchors:

- In drug-resistant **focal epilepsy** cohorts, FCD prevalence is reported between **5% and 25%** depending on cohort and imaging (secondary source — ⚠️ verify against a primary citation before use as evidence).
- In the largest surgical series (9,523 specimens, 36 centers, 12 countries, 25 years), **malformations of cortical development accounted for 19.8%** of diagnoses, and within these, "**focal cortical dysplasia was the most common type, 52.7% of cases of which were in children**" (PMID:29069555).
- FCD is the **most common histopathological diagnosis in pediatric epilepsy surgery**; hippocampal sclerosis (36.4%) dominates in adults (PMID:29069555).
- Pharmacoresistance within FCD cohorts is high — **~71–74%** in pediatric series (PMID:35985831 ⚠️).

Suggested dismech `Prevalence` records:

```yaml
prevalence:
- population: Worldwide surgical epilepsy cohorts (European Epilepsy Brain Bank, n=9523)
  measure_type: UNKNOWN          # a proportion-of-surgical-cases, not a population rate
  prevalence_class: UNKNOWN
  notes: >-
    Malformations of cortical development accounted for 19.8% of 9523 epilepsy
    surgery specimens; focal cortical dysplasia was the most common MCD type,
    52.7% of FCD cases occurring in children. This is a case-mix proportion,
    NOT a population prevalence.
```

⚠️ **Do not convert surgical case-mix percentages into `rate_per_100000`.** They are not population rates and the conversion would be a fabrication. Record `prevalence_class: NOT_YET_DOCUMENTED` for true population prevalence and note the gap.

### 9.2 Inheritance

FCD II is **overwhelmingly sporadic and non-heritable**, because the causal event is a post-zygotic somatic mutation confined to brain. Two important qualifications:

1. **The two-hit repressor architecture *does* have a heritable component.** Germline `DEPDC5`, `NPRL2`, `NPRL3`, `TSC1`, `TSC2` LoF variants are transmitted **autosomal dominantly with markedly incomplete penetrance**; family members may have familial focal epilepsy with variable foci (FFEVF), sleep-related hypermotor epilepsy, or be unaffected. Whether a carrier develops an FCD lesion depends on whether a somatic second hit happens to occur in a cortical progenitor — a stochastic event. This is the mechanistic basis for the observation (PMID:40742146) that "Germline variants in DEPDC5 are a cause of familial focal epilepsy with variable foci. **Affected individuals may have focal cortical dysplasia if a second brain somatic variant occurs**."
2. **Recurrence risk counseling therefore diverges sharply by genotype.** Single-somatic-hit `MTOR`/`AKT3`/`PIK3CA`/`RHEB` FCD II carries **near-population-baseline recurrence risk** for siblings and offspring. Germline-`DEPDC5`-associated FCD II carries **50% transmission of the germline allele** with reduced penetrance for epilepsy and much lower penetrance for a visible FCD lesion.

- **Penetrance:** for germline GATOR1 variants, epilepsy penetrance is incomplete (literature estimates commonly ~50–60% for `DEPDC5`; ⚠️ verify against a primary source before curating a number).
- **Expressivity:** highly variable within GATOR1 families — the same germline allele produces unaffected carriers, non-lesional focal epilepsy, and FCD II in different relatives.
- **Anticipation:** not a feature (no repeat expansion).
- **Germline mosaicism:** theoretically possible for the germline allele; not a documented recurrent issue in FCD II.
- **Founder effects / carrier frequency:** none established for FCD II specifically.
- **Consanguinity:** not a relevant risk factor (dominant/somatic mechanism).

Suggested `Inheritance` blocks: somatic mosaicism (⚠️ `HP:0001442` Somatic mosaicism — verify current label, HPO has revised this term family) for the primary mode, plus autosomal dominant (⚠️ `HP:0000006`) for the germline GATOR1/TSC arm. **Bind both `inheritance_term.term` — an unbound `preferred_term` is the recurring gap flagged in the project instructions.**

### 9.3 Population demographics

- **Ethnic/geographic variation:** none established. Reported series come from Europe, East Asia (Korea, China, Japan), and North America with broadly similar findings.
- **Sex ratio:** approximately **1:1**. The MELD Graph test cohort was 125 female (48%) / 135 male (52%), and the independent cohort 62 female (53%) / 54 male (47%) (PMID:39992650) — consistent with no sex bias.
- **Age distribution:** bimodal in the surgical literature — a large pediatric peak (median surgical age ~4 y in dedicated pediatric series) and an adult tail reflecting delayed referral (mean 20.1 y epilepsy duration before adult surgery, PMID:29069555).

---

## 10. Diagnostics

### 10.1 The diagnostic architecture

The 2022 ILAE update replaced a purely histopathological diagnosis with a **multi-layered scheme** (PMID:35706131):

> "The task force recommends '**a multi-layered diagnostic scheme**' integrating histopathological classification with advanced neuroimaging and genetic studies to comprehensively diagnose FCD subtypes and develop targeted treatment options."

The four layers:

| Layer | Content |
|---|---|
| **1** | Histopathological diagnosis with immunohistochemical confirmation |
| **2** | Genetic findings — methodology, tissue source, specific variants |
| **3** | Neuroimaging — MRI characteristics, field strength, analysis method |
| **4** | **Integrated diagnosis** synthesizing layers 1–3 |

This superseded the 2011 scheme (PMID:21219302), which had proposed "**a three-tiered classification system**" distinguishing FCD Type I (dyslamination), Type II (cortical dyslamination with dysmorphic neurons, with or without balloon cells), and Type III (associated with a principal lesion).

The 2022 update also added **mMCD**, **MOGHE**, and **"no definite FCD on histopathology"** as categories, and confirmed the genetic underpinnings (PMID:35706131): mTOR-pathway genes in FCD II — "**AKT3, DEPDC5, MTOR, NPRL2, NPRL3, PIK3CA, RHEB, TSC1, TSC2**" — and `SLC35A2` in MOGHE.

### 10.2 Imaging

**MRI is the primary in vivo diagnostic modality.** Characteristic FCD II features:

- Cortical thickening
- **Blurring of the grey–white matter junction**
- Increased T2/FLAIR signal in cortex and subcortical white matter
- Abnormal sulcal/gyral pattern
- **The transmantle sign** — pathognomonic-ish for FCD IIb. Per the 2022 ILAE update: "a linear or triangular T2/FLAIR signal extending from lesion toward ventricle **strongly suggests FCDIIb**." The AJNR study adds a refinement (PMID:31097427): "The transmantle sign is typically hyperintense on T2WI and FLAIR and hypointense on T1WI. However, in some cases, it shows T1 high signal... **The number of balloon cells was significantly higher in group A [T1-high] than in the other groups.**"

**MRI-negative FCD II is common and is the central diagnostic problem**, especially for GATOR1-related FCD IIa with "subtle or negative MRI findings" (PMID:37946310).

**Post-processing and AI-assisted detection** are now clinically relevant. The MELD Graph study (PMID:39992650) is the landmark:

> "In the test dataset, the MELD Graph had a **sensitivity of 81.6% in histopathologically confirmed patients seizure-free 1 year after surgery and 63.7% in MRI-negative patients with FCD**. The PPV of putative lesions... was **67% (70% sensitivity; 60% specificity)**, compared with 39% (67% sensitivity; 54% specificity) using an existing baseline algorithm."

Companion tools reviewed in PMID:41317206: **MELD-Graph, MAP18** (voxel-based morphometry), **FLAT1** (FLAIR/T1 ratio mapping), **SUPR-FLAIR** (normalized FLAIR surface projection). Their collective value: "Advanced post-processing tools substantially increase sensitivity for detecting subtle cortical abnormalities, particularly in **MRI-negative pediatric epilepsy**."

Real-world MRI accuracy with a dedicated protocol (PMID:36856785): "The MRI and histopathology were concordant in 101 and discordant in 15 patients" of 116; and a caution — "**Small MRI positive FCD can be histopathologically missed, most likely due to sampling errors resulting from insufficient harvesting of tissue.**"

**FDG-PET** is highly complementary: "FDG-PET revealed localized hypo- or hypermetabolism in **47 (92%) of 51 patients**," and MRI was positive in 46/51 (90%) (PMID:37948689). **Ictal SPECT** showed concordant hyperperfusion in 37/42.

### 10.3 Electrophysiology

- **Scalp EEG:** interictal focal epileptiform discharges, often with a characteristic **rhythmic/repetitive spiking or "brushes"** pattern over the dysplastic cortex; ictal onset regional.
- **Intracranial EEG / SEEG:** used selectively. In the lesion-oriented Japanese series, "Intracranial EEG was used in only 13 patients (25%), including 5 with negative MRI results and 4 with subtle MRI findings" (PMID:37948689).
- **ECoG-based network analysis** is an emerging localization aid (PMID:35989902): "Clustering coefficient, local efficiency, node out-degree, and node out-strength with higher values are the most reliable biomarkers for the delineation of EZ."
- **Intraoperative ECoG:** its added value is contested — the same series concluded "**Intraoperative ECoG may thus be unnecessary**" when MRI/PET localization is clean (PMID:37948689).

### 10.4 Genetic testing

**This is where FCD II diagnostics diverge most sharply from standard practice.**

| Test | Utility in FCD II |
|---|---|
| **Deep targeted panel on RESECTED BRAIN TISSUE** | **The highest-yield test.** Requires ≥1000–2000× coverage to call 1–5% VAF variants. Baldassari used "targeted gene sequencing (≥2000X read depth) on matched blood-brain samples" and elucidated **63% of FCD2/HME** (PMID:31444548) |
| **Droplet digital PCR (ddPCR)** on brain tissue | Orthogonal confirmation of a candidate low-VAF variant; used to confirm the second `DEPDC5` hit (PMID:40742146) |
| **Blood WES/WGS at standard depth** | **Low yield.** Detects only the germline allele of the two-hit architecture. Negative in single-somatic-hit FCD II by design. Still worth doing to find a germline `DEPDC5`/`NPRL2`/`NPRL3`/`TSC1`/`TSC2` variant with counseling implications |
| **CSF cell-free DNA (liquid biopsy)** | **Emerging, not yet clinical.** PMID:33834539: "brain mosaicism can be detected in the CSF-derived cfDNA" in **3 of 12** epileptic patients with previously identified somatic mutations. Low sensitivity; promising direction |
| **Chromosomal microarray / karyotype / FISH** | **Not indicated.** No CNV mechanism |
| **mtDNA testing / repeat expansion testing** | **Not applicable** |
| **RNA-seq / methylation classifier** | Research only for FCD II; methylation classifiers are further advanced for MOGHE |

Practical recommendation for the KB entry: curate a `Diagnostic` node stating that **negative blood genetic testing does not exclude FCD II**, and that **brain tissue is the required substrate** for single-hit detection. Curate the CSF cfDNA approach with `validation_status: PROPOSED`.

### 10.5 Histopathology / biopsy findings (Layer 1)

Per the ILAE 2022 criteria (PMID:35706131):

- **FCD IIa** — "dysmorphic neurons—**cytomegalic cells exceeding 25 μm diameter**—without balloon cells," with cortical dyslamination.
- **FCD IIb** — "**both dysmorphic neurons AND balloon cells**, along with compromised oligodendroglial populations."

Additional consistent features: loss of the six-layer laminar architecture, blurred grey–white boundary, heterotopic neurons in white matter, abnormal neurofilament accumulation, and diffuse **pS6 positivity** in the abnormal cells.

### 10.6 Clinical criteria and differential diagnosis

FCD II has **no clinical diagnostic criteria** — it cannot be diagnosed on symptoms alone (PMID:19679275: "FCD type II cannot be diagnosed with certainty in the clinic").

**Differential diagnosis, with distinguishing features:**

| Differential | Distinguishing features |
|---|---|
| **Tuberous sclerosis complex** (`Tuberous_Sclerosis_Complex.yaml` in KB) | Multiple bilateral cortical tubers, SEN/SEGA, skin/renal/cardiac findings, germline `TSC1`/`TSC2` in blood. FCD IIb histology is nearly identical to a tuber — the distinction is systemic and multiplicity, not microscopy |
| **Hemimegalencephaly** | Same genes, whole-hemisphere enlargement; earlier developmental hit |
| **FCD type I / mMCD / MOGHE** | Dyslamination without dysmorphic neurons or balloon cells; `SLC35A2`, not mTOR pathway; MOGHE has oligodendroglial hyperplasia |
| **FCD type III** | Dysplasia adjacent to a principal lesion (hippocampal sclerosis, tumor, vascular malformation, early acquired injury) |
| **Ganglioglioma / DNET (LEATs)** | Neoplastic; CD34-positive; often temporal; may coexist with FCD IIIb |
| **Polymicrogyria, lissencephaly, heterotopia** | Different malformation classes; often bilateral; different genes (`TUBB2B`, `ARX`, `ADGRG1` — all present in this KB) |
| **Rasmussen encephalitis** | Progressive hemispheric atrophy, inflammatory, progressive hemiparesis |
| **Long-term epilepsy-associated glial scar** | May mimic FCD on MRI; PMID:36856785 notes one of 28 FCD II with an associated glial scar was misread as glial scar only |

### 10.7 Screening

**No population screening exists or is warranted** for FCD II. Two narrow exceptions:

1. **Cascade family testing** when a germline GATOR1 or `TSC1`/`TSC2` variant is identified — relatives may carry the allele with epilepsy risk.
2. **Early-life MRI in infants with focal seizures.** The ILAE neuroimaging task force has specifically addressed MRI detection of early-life epilepsy caused by FCD (PMID:40317795 — ⚠️ abstract not retrieved; verify before quoting), reflecting the known difficulty of detecting FCD in the unmyelinated/partially-myelinated infant brain.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

No FCD-II-specific survival data were located. Mortality risk derives from the epilepsy: **SUDEP**, status epilepticus, seizure-related accidents and drowning. Drug-resistant focal epilepsy carries an elevated standardized mortality ratio; successful surgery reduces it. **Flag disease-specific mortality as a `KNOWLEDGE_GAP`** — do not import generic epilepsy mortality figures as FCD II data.

### 11.2 Surgical outcome — the dominant prognostic literature

FCD II is one of the **best-outcome** epilepsy surgery pathologies when the lesion is fully resected.

| Series | n | Outcome |
|---|---|---|
| Lesionectomy, MRI/FDG-PET-guided (PMID:37948689) | 51 | "Postoperative seizure outcomes were **Engel class I in 47 patients (92%) and Ia in 45 (88%)**." All 5 MRI-negative patients achieved Engel I |
| Bonn cohort (PMID:34177771) | 102 | "**71% of patients at 12 months** ... and **54% ... at the last available FU** (63 ± 5.00 months) achieved complete seizure freedom (Engel class IA), and **84 and 69% of patients, respectively, displayed Engel class I** outcome" |
| Bottom-of-sulcus dysplasia, limited corticectomy (PMID:33947776) | 38 | "At a median 6.3 (IQR 4.8–9.9) years of follow-up, **33 (87%) patients are seizure-free, 31 off antiseizure medication**" |
| Young children ≤6 y at onset (PMID:31368639) | 112 | "At the last follow-up, **88.4% achieved seizure-free**" |
| Pediatric vs adult comparison (PMID:28410464) | 106 | "Surgical outcome was favorable in the whole population (**72.6% ... Engel's Class Ia+Ic**), **independently from age at surgery**" |
| GATOR1-variant cases (PMID:37946310) | 17 total | GATOR1 cases "achieved seizure freedom after surgery in most cases" despite subtle/negative MRI |

Note the **attrition between 12-month and long-term follow-up** in the Bonn series (71% → 54% Engel IA). Curate the time-dependence explicitly; single-timepoint seizure-freedom rates overstate durable benefit.

### 11.3 Prognostic factors

Consistently identified predictors of seizure freedom:

1. **Complete resection of the MRI-visible lesion** — the strongest and most reproducible factor. "Predictive factors for favorable seizure outcome were **complete resection of the MRI lesion (p = 0.006) and frontal lobe surgery (p = 0.012)**" (PMID:37948689); "Long-term post-surgical outcome was primarily influenced by **the extent of resection** and history of FTBTCS" (PMID:34177771).
2. **Absence of focal-to-bilateral tonic–clonic seizures** pre-operatively (PMID:34177771).
3. **MRI-positive lesion** (though MRI-negative patients did well when PET-guided with intracranial EEG — PMID:37948689).
4. **Frontal lobe location** (PMID:37948689).
5. **Smaller, well-circumscribed lesion (e.g. BOSD)** (PMID:33947776).
6. **Genotype** — an emerging factor. GATOR1-related FCD IIa did well surgically (PMID:37946310).

Notably **age at surgery was NOT an independent predictor** of seizure outcome in the direct comparison (PMID:28410464) — an important corrective to the assumption that earlier is always better *for seizures*. (It may still matter for development; see §8.3.)

### 11.4 Morbidity, function, and complications

- **Post-surgical neurological deficit:** modest and often acceptable. In lesions near eloquent cortex, "Postoperative neurological deficits were noted in only **4 (27%) of 15 patients** with FCD in the vicinity of eloquent areas," and "**13 (87%) achieved a class I outcome**" (PMID:37948689).
- **Cognitive outcome:** the weak link. Only **4/48** children with pre-operative moderate/severe developmental delay improved DQ rank at 6 months post-surgery (PMID:31368639). Longer follow-up may be more favorable but was not reported.
- **Ongoing morbidity:** antiseizure medication burden and side effects, injury risk, driving restriction, educational/vocational impact, psychiatric comorbidity (depression, anxiety, ADHD — well documented in focal epilepsy generally).
- **Recovery potential:** genuinely high **for seizures** with complete resection — a meaningful fraction come off medication entirely (31/38 in the BOSD series). Recovery of already-established developmental delay is limited.
- **Prognostic biomarkers:** none validated. Candidates under investigation: genotype (GATOR1 vs mTOR-activator), pS6 staining intensity, ECoG network metrics (PMID:35989902), and completeness-of-resection quantification on post-op MRI.

---

## 12. Treatment

### 12.1 Pharmacotherapy — antiseizure medications

Standard focal-epilepsy antiseizure medications are used first-line: carbamazepine, oxcarbazepine, levetiracetam, lacosamide, lamotrigine, valproate, topiramate, vigabatrin (particularly for spasms), clobazam, perampanel, brivaracetam, cenobamate. **Efficacy is poor** — the Lancet Neurol review states plainly (PMID:19679275):

> "**Drug treatment commonly proves ineffective, whereas appropriate surgical treatment can be curative in many cases.**"

Suggested annotation:
```yaml
treatments:
- name: Antiseizure Medication
  therapeutic_modality: SMALL_MOLECULE
  treatment_term:
    preferred_term: Pharmacotherapy
    term: {id: NCIT:C15986, label: Pharmacotherapy}   # ⚠️ verify
```

### 12.2 mTOR-inhibitor therapy — the mechanism-targeted arm

**This is the highest-value, most nuanced section for a mechanism knowledge base, and the honest answer is: the mechanism is right, the clinical result is negative-with-a-signal.**

**Everolimus randomized crossover trial (NCT03198949), Epilepsia Open 2025 (PMID:39607729).** 21 patients with pathologically confirmed FCD 2, aged 4–40 y, everolimus 4.5 mg/m²/day targeting 5–15 ng/mL:

> "**There was no significant difference in the primary outcome between everolimus and placebo groups (24% vs. 19%, p = 0.66).**"

> "Three patients with a pathogenic variant in the MTOR gene or no genetic abnormalities achieved seizure freedom with everolimus in the last month of the core phase, **while none of the patients with variants in other genes did**."

> "**Adverse events, such as mucositis or skin ulceration, were more common with everolimus (19/21 vs. 7/21, p < 0.001).**"

Conclusion: "Everolimus treatment for 12 weeks did not show overall superiority in reducing seizures compared to placebo. However, it showed promise, **mostly in patients with a pathogenic variant in the MTOR gene**."

**Sirolimus (FCDS-01), Epilepsia Open 2022** — 16 patients aged 6–57 y, target trough 5–15 ng/mL; focal seizure frequency reduced by 25% in all patients during maintenance; **response rate 33.3%**. ⚠️ **Cached as PMC8862414; PMID not confirmed in this session — run `just fetch-reference` before curating any snippet.**

**Curation guidance.** Curate mTOR inhibition as a `target_mechanisms` treatment linked to the mTORC1-hyperactivation node with `modifier: INHIBITS`, but **do not overstate efficacy**. The correct framing is: *pharmacologically validated mechanism, genotype-dependent and modest clinical benefit, meaningful toxicity, negative primary endpoint in the only randomized trial*. This is a textbook case for a `KNOWLEDGE_GAP` discussion on why a mechanistically-perfect drug underperforms — plausible reasons include the mutation being present in only a small cell fraction, the lesion being a fixed developmental structure rather than an ongoing process, and inadequate CNS drug exposure.

```yaml
- name: Everolimus
  therapeutic_modality: SMALL_MOLECULE
  treatment_term:
    preferred_term: Pharmacotherapy
    term: {id: NCIT:C15986, label: Pharmacotherapy}   # ⚠️ verify
    therapeutic_agent:
    - preferred_term: everolimus
      term: {id: CHEBI:68478, label: everolimus}      # ✅ verified
  target_mechanisms:
  - node: "mTORC1 Hyperactivation"
    modifier: INHIBITS
```
(`sirolimus` = `CHEBI:9168` ✅ verified.)

### 12.3 Pharmacogenomics

The everolimus trial (PMID:39607729) provides the field's clearest genotype–response signal: response concentrated in `MTOR`-variant and genetically-undefined patients, absent in patients with variants in other genes. This is **not** classical pharmacogenomics (drug metabolism) — it is **target genotype–driven response**, closer to precision oncology logic. Curate it as such.

Standard PGx applies to some ASMs (e.g. `HLA-B*15:02` and carbamazepine-associated SJS/TEN in Southeast Asian ancestry) but is not FCD-II-specific — the KB's `drug_hypersensitivity_scar` module already covers that logic.

### 12.4 Surgical and interventional treatment — the mainstay

| Approach | Detail | Evidence |
|---|---|---|
| **Lesionectomy / limited corticectomy** | The primary curative intervention. Complete resection of the MRI lesion is the key determinant of outcome | PMID:37948689, PMID:33947776 |
| **Tailored resection / lobectomy** | For larger or multilobar lesions | PMID:34177771 |
| **SEEG-guided radiofrequency thermocoagulation (RF-TC)** | Minimally invasive; useful for deep/eloquent BOSD. Case report of tapered electrode implantation along the sulcus bottom achieving Engel I at 26 months (PMID:34499250) | PMID:34499250 |
| **MR-guided laser interstitial thermal therapy (LITT/MRgLITT)** | "a safe and effective option"; used for FCD among other etiologies (PMID:32672117). Morphometry-assisted MRgLITT in 9 patients: "Engel Ia, Ib, and IV scores were obtained at 1-year follow-up for 6, 1, and 2 patients" (PMID:36001745) | PMID:32672117, PMID:36001745 |
| **Neuromodulation (VNS, RNS, DBS)** | Palliative, for non-resectable or multifocal cases; not curative | — |

Suggested NCIT terms (⚠️ all need verification): `NCIT:C15329` Surgical Procedure; `NCIT:C49236` Therapeutic Procedure; `NCIT:C15747` Supportive Care; `NCIT:C15240` Genetic Counseling; `NCIT:C15315` Rehabilitation.

### 12.5 Supportive, rehabilitative, and dietary

- **Ketogenic diet / modified Atkins** — used in drug-resistant pediatric epilepsy including FCD; not FCD-II-specific evidence. Mechanistically interesting given that the ketogenic diet is known to **suppress mTOR signaling**, though this has not been tested as a targeted strategy in FCD II. Worth a `KNOWLEDGE_GAP` note.
- **Developmental/educational support, speech and occupational therapy** — for the ~half of early-onset children with developmental delay.
- **Psychiatric care** for comorbid depression, anxiety, ADHD.

### 12.6 Experimental and future therapeutics

- **Gene editing.** The 2025 *Cells* review (PMID:40358185) frames the ambition and its limits: "Current treatments primarily rely on mTOR inhibitors, such as rapamycin, which reduce seizure frequency and tumor size but **fail to address underlying genetic causes**. Advances in gene editing, particularly via **CRISPR/Cas9**, offer promising avenues for precision therapies targeting the genetic mutations driving mTORopathies... **While gene editing holds curative potential, challenges remain concerning delivery, long-term safety, and ethical considerations.**" Note: for a mosaic disease where the mutation is in a minority of cells in a defined focal region, focal AAV delivery is at least geometrically plausible — this is one of the more realistic gene-therapy targets in neurology. All preclinical.
- **GluN2C-selective NMDAR antagonists** — proposed by PMID:38717560; rat-model evidence only, with a narrow developmental window.
- **CSF cfDNA-guided pre-surgical genotyping** (PMID:33834539) — would enable genotype-informed medical therapy before, or instead of, resection.
- **Human cortical organoid models for drug screening** (PMID:41789478) — mosaic patient-derived organoids with rapamycin-rescuable phenotypes provide a tractable screening platform.

### 12.7 Treatment algorithm

```
Focal seizures + suspected/confirmed FCD II
  ↓
Trial of ≥2 appropriately chosen ASMs
  ↓ (failure → drug-resistant epilepsy, typically within 1–2 y)
Comprehensive presurgical evaluation:
  3T epilepsy-protocol MRI + post-processing (MELD-Graph / MAP / FLAT1)
  FDG-PET; ictal SPECT; video-EEG
  ↓
Concordant, resectable, non-eloquent?  ── YES ──→ Lesionectomy / tailored resection
  │                                                 (goal: COMPLETE resection)
  │                                                          ↓
  │                                            Brain tissue → deep panel sequencing
  │                                            (Layer 2 of ILAE integrated diagnosis)
  NO / discordant / MRI-negative
  ↓
SEEG (intracranial EEG)
  ↓
Resectable? ── YES ──→ Resection    ── NO ──→ RF-TC / LITT
  ↓ (not resectable at all)
Neuromodulation (VNS/RNS) ± mTOR inhibitor trial (genotype-informed) ± ketogenic diet
```

---

## 13. Prevention

**Primary prevention is not possible.** FCD II arises from a stochastic somatic mutation during fetal corticogenesis. There is no modifiable exposure, no vaccine, no behavioral intervention, and no dietary factor known to reduce risk. Any prevention section should say this plainly rather than importing generic epilepsy prevention advice.

**Secondary prevention (early detection) is the actionable level:**

- **Early MRI in infants with focal seizures**, using epilepsy-dedicated protocols. Detection in the infant brain is genuinely hard because of incomplete myelination; the ILAE neuroimaging task force has issued specific guidance (PMID:40317795 ⚠️).
- **Automated post-processing on previously "MRI-negative" scans.** MELD Graph achieved 63.7% sensitivity in MRI-negative FCD patients (PMID:39992650) — reclassifying "MRI-negative" epilepsy into surgical candidacy is the single highest-yield secondary-prevention action available.
- **Prompt referral to a surgical epilepsy center once ≥2 ASMs have failed.** The 20.1-year mean delay to adult surgery (PMID:29069555) is the field's most conspicuous, most preventable harm.

**Tertiary prevention (preventing complications):**

- Complete resection to achieve seizure freedom, preventing cumulative cognitive/psychosocial injury and SUDEP risk.
- Seizure-safety counseling (bathing, swimming, driving, heights).
- Medication adherence and sleep hygiene.

**Genetic counseling** — genuinely important, and genotype-stratified:

| Genotype | Counseling |
|---|---|
| Brain-somatic only (`MTOR`, `AKT3`, `PIK3CA`, `RHEB`) | Recurrence risk near population baseline; **not heritable** |
| Germline GATOR1 (`DEPDC5`/`NPRL2`/`NPRL3`) or `TSC1`/`TSC2` | Autosomal dominant transmission of the germline allele with **incomplete penetrance**; cascade testing of relatives; prenatal/PGT technically available but complicated by the fact that inheriting the germline allele does **not** predict an FCD lesion (that requires a stochastic second hit) |

This asymmetry — a heritable predisposition whose phenotypic expression depends on a second, unpredictable somatic event — is the most counseling-relevant and most frequently misunderstood aspect of FCD II. Suggested `NCIT:C15240` Genetic Counseling ⚠️.

**Immunization, public health, environmental interventions, prophylaxis:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy of relevance:** *Homo sapiens* (`NCBITaxon:9606`); model species *Mus musculus* (`NCBITaxon:10090`), *Rattus norvegicus* (`NCBITaxon:10116`).
- **Naturally occurring FCD II in other species:** **none documented.** No OMIA entry corresponds to FCD II. Focal cortical dysplasia has occasionally been described in veterinary neuropathology (e.g. in dogs with epilepsy) but not as a genetically-characterized mTORopathy analogous to human FCD II. **This is a genuine absence, not an unsearched gap** — curate as `not applicable`.
- **Breed (VBO):** no breed predisposition identified.
- **Orthologous genes:** all FCD II genes are deeply conserved. Mouse orthologs: *Mtor*, *Depdc5*, *Tsc1*, *Tsc2*, *Akt3*, *Pik3ca*, *Rheb*, *Nprl2*, *Nprl3*. The mTOR pathway is conserved to yeast (TOR1/TOR2), and the GATOR/SEACIT amino-acid-sensing machinery is conserved to *S. cerevisiae*.
- **Comparative pathology:** the lissencephalic mouse cortex lacks the outer subventricular zone and outer radial glia that characterize human (gyrencephalic) corticogenesis, so mouse models reproduce cytomegaly, migration failure, and seizures but **not** human-specific progenitor biology or the gyral/sulcal anatomy that defines bottom-of-sulcus dysplasia. This is a `HUMAN_MODEL_MISMATCH` worth curating explicitly.
- **Zoonotic potential / cross-species transmission:** not applicable (non-infectious, non-transmissible).

---

## 15. Model Organisms

### 15.1 The workhorse model — focal in utero electroporation (IUE)

The defining methodological advance in FCD II research is **focal somatic mosaicism engineered in vivo by in utero electroporation**, which reproduces the human genetic architecture (a mutation in a spatially restricted clone) rather than a whole-animal knockout.

**Mutant `MTOR` IUE** — the model that closed the causal loop (PMID:25799227):

> "Focal cortical expression of mutant MTOR by in utero electroporation in mice was sufficient to **disrupt neuronal migration and cause spontaneous seizures and cytomegalic neurons**. Inhibition of mTOR with rapamycin **suppressed cytomegalic neurons and epileptic seizures**."

**CRISPR/Cas9 `Tsc1`/`Tsc2` IUE** (PMID:28215400):

> "In utero CRISPR-Cas9 genome editing of Tsc1 or Tsc2 induced **spontaneous behavioral seizures, cytomegalic neurons, and cortical dyslamination**, establishing that brain somatic mutations in these genes cause FCD."

**RhebCA dose-titration IUE** (PMID:30700531) — the model that established mTOR activation as a **graded** severity determinant, expressing constitutively active RHEB "at low, intermediate, and high concentrations to induce different mTORC1 activity levels."

**Conditional mouse genetics** (PMID:29281825): "conditional mouse studies demonstrated that **mTOR activation in excitatory neurons and glia causes abnormal cortical overgrowth**" — establishing the cell-type requirements.

**Rat IUE model of pathogenic `MTOR`** (PMID:38717560) — used to discover the GluN2C NMDAR mechanism.

**`Slc35a2` IUE** (PMID:38909838) — the contrast model for the FCD I/MOGHE arm: "Slc35a2 KO or KD caused **disrupted radial migration** ... Spontaneous seizures were **not** observed in focal Slc35a2 KO mice, but there was **reduced seizure threshold** following pentylenetetrazol injection." Note the phenotypic contrast with mTOR models (spontaneous seizures) — useful for distinguishing the two disease arms in a KB.

### 15.2 Human cellular models

**Patient-derived mosaic human cortical organoids** are the newest and most human-relevant system (PMID:41789478, *Brain* 2026):

> "Researchers created patient-derived human cortical organoids with DEPDC5 two-hit inactivation mosaicism. The organoids displayed '**increased mTOR activity that was rescued by the mTOR inhibitor rapamycin**' alongside **dysmorphic neurons and enhanced excitability**. Single-cell transcriptomics revealed '**aberrant differentiation trajectories leading to premature upper-layer neuron generation**'."

This is notable because it engineers **mosaicism itself** into the model — most iPSC models are uniformly mutant, which is biologically wrong for FCD II.

### 15.3 Model characteristics

**Recapitulated well:**
- Focal, mosaic mTORC1 hyperactivation with pS6 readout
- Cytomegalic/dysmorphic neurons
- Disrupted radial migration and heterotopic neurons
- Spontaneous seizures (mTOR-pathway models)
- **Rapamycin rescue** — of both cellular and seizure phenotypes

**Not recapitulated / limitations:**
- **Balloon cells are poorly reproduced** in rodent models — the defining feature of FCD IIb has no robust animal correlate. This is the single largest model gap.
- **Gyrencephaly and sulcal anatomy** — mouse lissencephaly precludes modeling bottom-of-sulcus dysplasia or transmantle radial bands.
- **Human-specific outer radial glia / OSVZ biology** absent in rodents.
- **Cognitive/developmental phenotypes** are difficult to map onto human intellectual disability.
- **Timing fidelity** — IUE delivers the mutation at a single experimenter-chosen embryonic day, whereas human somatic mutations arise stochastically across a window.
- Organoids lack vasculature, microglia (unless co-cultured), and mature network activity, and reach only fetal-equivalent maturity.

**Curation guidance:** curate rodent findings with `evidence_source: MODEL_ORGANISM` and organoid findings with `evidence_source: IN_VITRO`. Per project policy, **model-organism evidence must not be the sole support for human phenotype claims** — the GluN2C mechanism (PMID:38717560) and the developmental-window claim are the two places where this rule most needs enforcing.

### 15.4 Resources

- **MGI** (Mouse Genome Informatics) — *Mtor*, *Depdc5*, *Tsc1*, *Tsc2*, *Rheb*, *Akt3* alleles
- **IMPC / KOMP / EuMMCR / IMSR / MMRRC / EMMA** — conditional and null alleles for all pathway genes
- **RGD** — rat models
- **Alliance of Genome Resources** — cross-species orthology and phenotype
- **Cellosaurus / ATCC** — iPSC lines; patient-derived lines from the organoid studies

---

## Appendix A — Verified ontology term suggestions

**Verified locally with OAK (✅ safe to use):**

| Domain | CURIE | Label |
|---|---|---|
| Disease | `MONDO:0011818` | isolated focal cortical dysplasia type II |
| Disease | `MONDO:0017101` | isolated focal cortical dysplasia type IIa |
| Disease | `MONDO:0017102` | isolated focal cortical dysplasia type IIb |
| Disease | `MONDO:0019009` | isolated focal cortical dysplasia |
| Phenotype | `HP:0032051` | Focal cortical dysplasia type II |
| Phenotype | `HP:0032052` | Focal cortical dysplasia type IIa |
| Phenotype | `HP:0032053` | Focal cortical dysplasia type IIb |
| Phenotype | `HP:0032046` | Focal cortical dysplasia |
| Phenotype | `HP:0002539` | Cortical dysplasia |
| Phenotype | `HP:0007359` | Focal-onset seizure |
| Phenotype | `HP:0032662` | Focal-onset seizure evolving into bilateral convulsive status epilepticus |
| Phenotype | `HP:0002133` | Status epilepticus |
| Phenotype | `HP:0001250` | Seizure |
| Phenotype | `HP:0011146` | Dialeptic seizure |
| Phenotype | `HP:0001249` | Intellectual disability |
| Phenotype | `HP:0002376` | Developmental regression |
| Phenotype | `HP:0000717` | Autism |
| Process | `GO:0031929` | TOR signaling |
| Process | `GO:0038202` | TORC1 signaling |
| Process | `GO:0032008` | positive regulation of TOR signaling |
| Process | `GO:0001764` | neuron migration |
| Process | `GO:0021895` | cerebral cortex neuron differentiation |
| Process | `GO:0006914` | autophagy |
| Process | `GO:0007399` | nervous system development |
| Process | `GO:0006954` | inflammatory response |
| Cell type | `CL:0000598` | pyramidal neuron |
| Cell type | `CL:0000679` | glutamatergic neuron |
| Cell type | `CL:0000127` | astrocyte |
| Cell type | `CL:0000129` | microglial cell |
| Cell type | `CL:0000128` | oligodendrocyte |
| Cell type | `CL:0002453` | oligodendrocyte precursor cell |
| Anatomy | `UBERON:0000955` | brain |
| Anatomy | `UBERON:0000956` | cerebral cortex |
| Anatomy | `UBERON:0016525` | frontal lobe |
| Anatomy | `UBERON:0016526` | lobe of cerebral hemisphere |
| Anatomy | `UBERON:0002437` | cerebral hemisphere white matter |
| Chemical | `CHEBI:9168` | sirolimus |
| Chemical | `CHEBI:68478` | everolimus |
| Gene | `hgnc:3942` | MTOR |
| Gene | `hgnc:18423` | DEPDC5 |
| Gene | `hgnc:12362` | TSC1 |
| Gene | `hgnc:12363` | TSC2 |
| Gene | `hgnc:393` | AKT3 |
| Gene | `hgnc:8975` | PIK3CA |
| Gene | `hgnc:10011` | RHEB |
| Gene | `hgnc:24969` | NPRL2 |
| Gene | `hgnc:14124` | NPRL3 |
| Gene | `hgnc:11022` | SLC35A2 (**contrast gene — FCD I/MOGHE, not FCD II**) |
| Gene | `hgnc:8980` | PIK3R2 |

**Requires verification before use (⚠️):** all NCIT treatment terms; `OMIM:607341`; `HP:0012469` (Infantile spasms); `HP:0001442` (somatic mosaicism); `HP:0000006` (autosomal dominant inheritance); `GO:0031931` (TORC1 complex); `GO:0005764` (lysosome); `GO:0006956` (complement activation).

---

## Appendix B — Citation index with evidence-source classification

| PMID | Short citation | `evidence_source` |
|---|---|---|
| 21219302 | Blümcke et al., *Epilepsia* 2011 — ILAE FCD consensus classification | OTHER (expert consensus) |
| 35706131 | Najm et al., *Epilepsia* 2022;63(8):1899–1919 — ILAE FCD classification update (DOI 10.1111/epi.17301) | OTHER (expert consensus) |
| 25799227 | Lim et al., *Nat Med* 2015 — brain somatic `MTOR` causes FCD II | HUMAN_CLINICAL + MODEL_ORGANISM (split into separate items) |
| 26779999 | Lee & Lee, *BMB Rep* 2016 — review of brain somatic `MTOR` in FCD | OTHER (review) |
| 28215400 | Lim et al., *Am J Hum Genet* 2017 — somatic `TSC1`/`TSC2` in FCD | HUMAN_CLINICAL + MODEL_ORGANISM |
| 29281825 | D'Gama et al., *Cell Rep* 2017 — mTOR continuum FCD→HME | HUMAN_CLINICAL |
| 31444548 | Baldassari et al., *Acta Neuropathol* 2019 — large surgical cohort genetics | HUMAN_CLINICAL |
| 29069555 | Blümcke et al., *N Engl J Med* 2017 — 9,523 epilepsy surgery specimens | HUMAN_CLINICAL |
| 19679275 | Palmini/Tassi-era review, *Lancet Neurol* 2009 — FCD II biology & clinical perspectives | OTHER (review) |
| 37149062 | *Neurobiol Dis* 2023 — mTOR pathway brain mosaicism review (292 patients) | OTHER (review) |
| 35163267 | *Int J Mol Sci* 2022 — cortical dysplasia and mTOR, human tissue narrative review | OTHER (review) |
| 37946310 | *Acta Neuropathol Commun* 2023 — GATOR1-IIa vs mTOR-IIb genotype–histopathology | HUMAN_CLINICAL |
| 40307383 | *Nat Neurosci* 2025 — single-cell genotyping + transcriptomics of mosaic FCD | HUMAN_CLINICAL |
| 39614299 | *Acta Neuropathol Commun* 2024 — spatial transcriptomics of FCD IIb | HUMAN_CLINICAL |
| 41789478 | *Brain* 2026 — mosaic `DEPDC5` human cortical organoids | IN_VITRO |
| 33834539 | *Ann Neurol* 2021 — brain somatic mutations in CSF cfDNA | HUMAN_CLINICAL |
| 40742146 | *Am J Med Genet A* 2025 — second-hit `DEPDC5` reclassifies germline VUS | HUMAN_CLINICAL |
| 39992650 | *JAMA Neurol* 2025 — MELD Graph neural-network FCD detection | HUMAN_CLINICAL |
| 41317206 | *Neuroradiology* 2026 — advanced neuroimaging in pediatric epilepsy surgery | OTHER (review) |
| 31097427 | *AJNR* 2019 — transmantle sign radiologic–pathologic correlation | HUMAN_CLINICAL |
| 36856785 | *Clin Neuroradiol* 2023 — epilepsy-dedicated MRI diagnostic accuracy | HUMAN_CLINICAL |
| 37948689 | *J Neurosurg* 2023 — lesionectomy for localized FCD II (n=51) | HUMAN_CLINICAL |
| 34177771 | *Front Neurol* 2021 — Bonn FCD II post-surgical outcomes (n=102) | HUMAN_CLINICAL |
| 33947776 | *Neurology* 2021 — one-stage limited resection for BOSD (n=38) | HUMAN_CLINICAL |
| 31368639 | *CNS Neurosci Ther* 2020 — young children with FCD II (n=112) | HUMAN_CLINICAL |
| 28410464 | *Epilepsy Behav* 2017 — FCD II outcomes by age group | HUMAN_CLINICAL |
| 27885945 | *J Neurosurg Pediatr* 2017 — extratemporal FCD II, CD34 in IIB | HUMAN_CLINICAL |
| 41487994 | *Front Cell Neurosci* 2025 — architecture/cellular composition review | OTHER (review) |
| 39607729 | *Epilepsia Open* 2025 — everolimus RCT in FCD 2 (NCT03198949) | HUMAN_CLINICAL |
| 38717560 | *Epilepsia* 2024 — `MTOR` variant → GluN2C NMDAR hyperexcitability (rat) | MODEL_ORGANISM |
| 30700531 | *J Neurosci* 2019 — RhebCA dose-graded mTOR hyperactivity | MODEL_ORGANISM |
| 40512428 | *Epilepsia* 2025 — HCN4 and synaptic excitation in Rheb-mTOR | MODEL_ORGANISM |
| 38909838 | *Neurosci Lett* 2024 — `Slc35a2` loss alters mouse cortex (**FCD I contrast**) | MODEL_ORGANISM |
| 40358185 | *Cells* 2025 — mTORopathies, gene editing futures | OTHER (review) |
| 36823117 | *Pract Neurol* 2023 — FCD practical guide for neurologists | OTHER (review) |
| 32672117 | *Int J Hyperthermia* 2020 — LITT in pediatric neurosurgery | OTHER (review) |
| 36001745 | *Oper Neurosurg* 2022 — morphometry-assisted MRgLITT (n=9) | HUMAN_CLINICAL |
| 34499250 | *Acta Neurochir* 2021 — SEEG RF-thermocoagulation of BOSD (case report) | HUMAN_CLINICAL |
| 35989902 | *Front Neurol* 2022 — ECoG network analysis for EZ delineation (n=10) | HUMAN_CLINICAL |
| 34324277 | *Epilepsia Open* 2021 — HHV-6 and epilepsy (**negative/confounded for FCD**) | HUMAN_CLINICAL |
| 29069555 | *N Engl J Med* 2017 (repeat) | HUMAN_CLINICAL |

**Citations requiring `just fetch-reference` verification before use as evidence snippets:** PMID:35985831 (pharmacoresistance in pediatric FCD), PMID:40317795 (ILAE neuroimaging task force, early-life FCD), PMID:16411966 (FCD prevalence/clinical presentation), and the sirolimus FCDS-01 trial (PMC8862414 — PMID unresolved). The ~9%-of-epilepsy-surgery-cases figure for FCD IIa in PMID:35706131 was obtained from a page-summary rather than the primary text and must be checked against the full article before curation.

---

## Appendix C — Recommended dismech modeling decisions

1. **Entity scope.** Curate `Focal_Cortical_Dysplasia_Type_II` as a single `Disease` with `has_subtypes: [IIa, IIb]`, rather than two separate entries. The subtypes share genetics and management and differ by one histological feature plus a genotype tendency. Use short slug-friendly subtype names (`IIa`, `IIb`) with `display_name` for verbose labels.

2. **Module conformance candidates.**
   - `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance` — strong fit; substitute the FCD-specific drivers (GluN2C NMDAR overactivation, HCN4 changes, interneuron abnormality).
   - Consider whether a **new `mtor_pathway_hyperactivation` module** is warranted. FCD II, TSC, hemimegalencephaly, Smith-Kingsmore syndrome, and `DEPDC5`-related epilepsy all converge on the same trigger→consequence chain, and the KB already holds `Tuberous_Sclerosis_Complex` and `DEPDC5-Related_Epilepsy`. This looks like a genuine recurrent conserved mechanism rather than a one-off — worth proposing via the `create-module` skill.

3. **`mechanistic_hypotheses` worth curating.**
   - `gator1_autophagocytic_iia` vs `mtor_migration_deficient_iib` (PMID:37946310) — two genotype-anchored routes to the FCD II phenotype.
   - `premature_neurodegeneration` (PMID:19679275) — status `EMERGING`; the claim that FCD II involves a degenerative as well as developmental component is longstanding but unresolved.
   - `non_cell_autonomous_bystander_dysfunction` (PMID:40307383) — transcriptional dysregulation in non-mutated cells; status `EMERGING`.

4. **`KNOWLEDGE_GAP` discussions to record.**
   - Why does everolimus fail its primary endpoint despite a perfectly validated target? (PMID:39607729)
   - True population prevalence is undocumented; all figures are surgical case-mix.
   - No quality-of-life, mortality, or omics (proteomic/metabolomic/lipidomic) data specific to FCD II.
   - Does early surgery rescue cognition? (PMID:31368639 vs PMID:28410464 conflict.)

5. **`HUMAN_MODEL_MISMATCH` discussions to record.**
   - Balloon cells — the defining FCD IIb feature — are not reproduced in rodent models.
   - The GluN2C therapeutic window (P9–P20 in rat) has no established human equivalent (PMID:38717560).
   - Lissencephalic rodent cortex cannot model bottom-of-sulcus or transmantle anatomy, nor human outer radial glia.

6. **Guardrails.** Do not curate `SLC35A2` as an FCD II gene. Do not curate HHV-6 as an etiology. Do not convert surgical case-mix percentages to `rate_per_100000`. Do not assert an mTOR-inhibitor efficacy claim stronger than "genotype-dependent partial response, negative randomized primary endpoint."

**Sources (web):** [ILAE 2022 consensus classification (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9545778/) · [Lim et al., *Nature Medicine* 2015](https://www.nature.com/articles/nm.3824) · [Lim et al., *AJHG* 2017 (somatic TSC1/TSC2)](https://www.cell.com/ajhg/fulltext/S0002-9297(17)30031-9) · [D'Gama et al., *Cell Reports* 2017](https://www.cell.com/cell-reports/fulltext/S2211-1247(17)31790-4) · [Mosaic human cortical organoids, *Brain* 2026](https://academic.oup.com/brain/advance-article/doi/10.1093/brain/awag086/8509128) · [Pineau et al., *Epilepsia* 2024 (GluN2C)](https://onlinelibrary.wiley.com/doi/10.1111/epi.18000) · [Kim et al., everolimus in FCD2, *Epilepsia Open* 2025](https://pubmed.ncbi.nlm.nih.gov/39607729/) · [Sirolimus for FCD II seizures (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8862414/) · [Everolimus population PK in FCD, *Front Pharmacol* 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10704167/) · [Incidence and prevalence of epilepsy-associated brain lesions (PMC)](https://ncbi.nlm.nih.gov/pmc/articles/PMC8885987) · [Blümcke classification, Radiopaedia](https://radiopaedia.org/articles/blumcke-classification-of-focal-cortical-dysplasia?lang=us)