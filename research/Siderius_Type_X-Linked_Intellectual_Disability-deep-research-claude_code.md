---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T00:36:02.290635'
end_time: '2026-08-01T00:51:27.827351'
duration_seconds: 925.54
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Siderius Type X-Linked Intellectual Disability
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
  - claude-opus-5[1m]
  web_search_requests: 5
  num_turns: 89
  total_cost_usd: 5.654327500000001
  session_id: 9ed0bf7e-9428-4610-84cd-99bb0f1b0519
  stop_reason: end_turn
citation_count: 13
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Siderius Type X-Linked Intellectual Disability
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Siderius Type X-Linked Intellectual Disability** covering all of the
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

# Comprehensive Research Report: Siderius Type X‑Linked Intellectual Disability (PHF8‑XLID / MRXSSD)

**Prepared:** 2026‑08‑01 · **Target KB entry:** `kb/disorders/Siderius_Type_X-Linked_Intellectual_Disability.yaml` (draft exists, 44 lines)

> **Verification status legend used throughout**
> ✅ = quote verified verbatim against a cached abstract already present in this repo's `references_cache/`
> ⚠ = content retrieved from a web/API source that summarizes; **the snippet must be re-fetched with `just fetch-reference PMID:x` and re-verified before being committed as an evidence `snippet:`**
> ❌ = not available / not retrievable in this session
>
> An NEC preflight was performed conceptually: MONDO:0010286 (syndromic X‑linked intellectual disability Siderius type) ↔ OMIM:300263 ↔ ORPHA:85287 ↔ gene **PHF8** (HGNC:20672) are mutually consistent across OMIM, GTR/MedGen, GenCC and every primary paper reviewed. There is **no** eponym collision detected (Siderius‑Hamel = same entity). No PHF8/PHF6, PHF8/PHF21A confusion appeared in the retrieved literature. **Caution flag:** "Siderius" is a *personal-name eponym* and the disorder sits in the numbered XLID/MRX series — both high-NEC-risk classes per `research/nec_risk_disease_classes.md`. Any deep-research report on this disease should be gene-frequency checked against PHF8 before use.

---

## 1. Disease Information

### 1.1 Overview

Siderius type syndromic X‑linked intellectual developmental disorder (MRXSSD), increasingly called **PHF8‑XLID** in the recent literature, is a rare X‑linked recessive **chromatinopathy** caused by loss‑of‑function variants in *PHF8* at Xp11.22. *PHF8* encodes a JmjC‑domain, Fe(II)/2‑oxoglutarate‑dependent histone lysine demethylase (KDM7B). The classical clinical description — derived from the founding families — is **mild-to-borderline intellectual disability with cleft lip and/or cleft palate and mild facial dysmorphism in affected males**. The 2022 multicenter expansion (n = 16 new affected males) substantially reframed the phenotype: developmental delay is universal, ID is near-universal, **autism spectrum disorder and ADHD are frequent and were previously under-recognized, and orofacial clefting is much less common than the founding-cohort literature implied (3/16, 19%)**.

Key framing quote (Sobering et al. 2022, HGG Adv, PMID:35469323) ✅:

> "Loss-of-function variants in PHD Finger Protein 8 (PHF8) cause Siderius X-linked intellectual disability (ID) syndrome, hereafter called PHF8-XLID. PHF8 is a histone demethylase that is important for epigenetic regulation of gene expression. PHF8-XLID is an under-characterized disorder with only five previous reports describing different PHF8 predicted loss-of-function variants in eight individuals."

### 1.2 Identifiers

| Resource | Identifier | Notes |
|---|---|---|
| MONDO | **MONDO:0010286** | syndromic X-linked intellectual disability Siderius type (matches draft entry) |
| OMIM (phenotype) | **300263** | INTELLECTUAL DEVELOPMENTAL DISORDER, X-LINKED, SYNDROMIC, SIDERIUS TYPE; MRXSSD |
| OMIM (gene) | **300560** | PHF8 |
| Orphanet | **ORPHA:85287** | X-linked intellectual disability, Siderius type ⚠ (orpha.net blocked this session; code confirmed via GTR + GenCC) |
| MedGen / UMLS | **C1846055** (MedGen UID 375779) | ⚠ from GTR |
| HGNC | **HGNC:20672** (`hgnc:20672` in dismech lowercase convention) | PHF8 |
| NCBI Gene | **23133** | PHF8, Xp11.22 |
| UniProt | **Q9UPP1** (PHF8_HUMAN) | Histone lysine demethylase PHF8 |
| Ensembl | ENSG00000172943 | ⚠ not independently re-verified |
| RefSeq transcript | **NM_015107.3** (NM_015107.2 in older reports) | |
| ICD-10 / ICD-11 / MeSH | ❌ **not verified** | No specific MeSH descriptor exists; PubMed indexes under *X-Linked Intellectual Disability* (D038901) + *Cleft Lip* / *Cleft Palate*. Do not assert an ICD code without checking Orphanet's cross-reference table. |

### 1.3 Synonyms

- MRXSSD (OMIM preferred abbreviation)
- Siderius X-linked mental retardation syndrome
- Siderius–Hamel syndrome / Siderius‑Hamel cleft lip‑palate syndrome
- Mental retardation, X-linked, syndromic, Siderius type (legacy OMIM title)
- **PHF8-XLID** (preferred in Sobering et al. 2022 and increasingly the working name)
- X-linked mental retardation with cleft lip/palate (descriptive, historical)
- Gene aliases used as disease-adjacent labels: JHDM1F, KDM7B, ZNF422

### 1.4 Data provenance character

Information is **aggregated disease-level and case-series derived**, not EHR-derived. The entire literature base is ~29 affected individuals across ~15 families in 6 primary reports plus contiguous-deletion cases. There is **no registry, no natural-history study, no EHR cohort, and no clinical trial** for this disorder. Any prevalence, frequency, or prognostic statement in this report is therefore case-series-derived and subject to strong ascertainment bias (see §3.4).

---

## 2. Etiology

### 2.1 Primary causal factor

**Monogenic, germline, X-linked recessive loss of PHF8 function.** No environmental, infectious, or multifactorial etiology is established. The mechanism of pathogenicity is loss of function; both truncating variants and catalytically inactivating missense variants have been shown to abolish demethylase activity.

Laumonnier et al. 2005 (J Med Genet, PMID:16199551) ✅ — the founding molecular report:

> "Truncating mutations were found in the PHF8 gene (encoding the PHD finger protein 8) in two unrelated families with X linked mental retardation (XLMR) associated with cleft lip/palate (MIM 300263)."
> "The association of XLMR and cleft lip/palate in these patients with mutations in PHF8 suggests an important function of PHF8 in midline formation and in the development of cognitive abilities, and links this gene to XLMR associated with cleft lip/palate."

Original linkage (Siderius et al. 1999, Am J Med Genet, PMID:10398231) ✅:

> "A family is described in which X-linked mild to borderline mental retardation (MR) is associated with cleft lip/palate. Linkage analysis showed a maximum LOD score of Z=2.78 at straight theta=0.0 for the DXS441 locus with flanking markers DXS337 and DXS990, defining the region Xp11.3-q21.3 with a linkage interval of 25 cM."

### 2.2 Genetic risk factors

- **Causal:** hemizygous PHF8 LoF variant in a male (see §4 for the variant catalogue).
- **Carrier status:** heterozygous mother. In Sobering 2022, **10/12 tested mothers were unaffected carriers**; **2 probands' mothers carried no variant (de novo)** ⚠.
- **De novo occurrence:** 3 of 11 LoF families in Sobering 2022 were de novo (c.596+1G>A, c.1627-1G>A, c.1965_1966dup) ⚠ — clinically important, since absence of family history does **not** exclude the diagnosis.
- **Contiguous gene deletions at Xp11.22** encompassing PHF8 ± FAM120C ± WNK3 produce an overlapping/expanded phenotype (Qiao et al. 2008, PMID:18498374, two brothers with ASD; De Wolf et al. 2014, PMID:25258334, "The deletion of PHF8 most likely explains the cleft palate and mild intellectual disability" ⚠; Huang et al. 2020, PMID:32219840, prenatal CMA detection of Xp11.22 deletion in a fetus with cleft lip and palate ⚠).
- **Modifier genes:** none identified. A *pathway-level* candidate framework exists: PHF8 physically and functionally interacts with two other XLID proteins, **ZNF711** and **KDM5C/JARID1C** (Kleine-Kohlbrecher et al. 2010, PMID:20346720) ✅ — "our results functionally link the XLMR gene PHF8 to two other XLMR genes, ZNF711 and JARID1C, indicating that MR genes may be functionally linked in pathways, causing the complex phenotypes observed in patients developing MR." Poeta et al. 2019 (PMID:31691806) place KDM5C at the crossroads of ARX, ZNF711 and PHF8 transcriptional axes ⚠. Whether variation in these partners modifies PHF8-XLID severity is **untested**.
- **X-inactivation as a female modifier:** skewed XCI tested in 3 carrier mothers — 2 completely skewed, 1 uninformative ⚠ (Sobering 2022). This is the presumed explanation for carrier females being unaffected.

### 2.3 Environmental risk factors

None established for this disorder. There is one **mechanistically motivated hypothesis worth curating as a knowledge gap, not as fact**: because PHF8 is a 2‑oxoglutarate/Fe(II)/**O₂**-dependent oxygenase, its catalytic output is oxygen-dependent, and maternal hypoxia is an established modifier of cleft lip/palate risk in mice.

Loenarz et al. 2010 (Hum Mol Genet, PMID:19843542) ✅ (abstract):

> "The dependence of PHF8 activity on oxygen availability is interesting because the occurrence of fetal cleft lip has been demonstrated to increase with maternal hypoxia in mouse studies. Cleft lip and other congenital anomalies are also linked indirectly to maternal hypoxia in humans, including from maternal smoking and maternal anti-hypertensive treatment."

and from the cached full text ✅:

> "Episodes of maternal respiratory hypoxia in mice also correlate with increased incidence of cleft lip/palate (gestational day 10-11, 10% O2), while hyperoxia rescued mouse strains that are genetically susceptible for cleft lip/palate (gestational day 10-11, 50% O2) (5), suggesting that gestational oxygen levels mediate genetic and environmental factors."

**Curation guidance:** this is a plausible gene–environment interaction (hypomorphic PHF8 × gestational hypoxia → clefting penetrance) but has **never been tested in PHF8-mutant humans or mice**. Model it as a `discussions` entry with `kind: KNOWLEDGE_GAP` (or as a `mechanistic_hypotheses` group with `status: EMERGING`), not as an etiologic claim.

### 2.4 Protective factors

- **Genetic:** none identified. No protective alleles, no gnomAD LoF-tolerant signal reported.
- **Environmental:** none disease-specific. Periconceptional folic acid supplementation is protective for orofacial clefting in the general population but has **not** been studied in PHF8-related clefting — do not import that claim into this entry.
- **A counterintuitive "protective" finding in mice:** Phf8-null mice show *resilience* to stress-induced anxiety/depression-like behavior (Walsh et al. 2017, PMID:28485378) ⚠ — "we report a striking resiliency to stress-induced anxiety- and depression-like behaviour on loss of Phf8." This has no demonstrated human counterpart and should be curated as `evidence_source: MODEL_ORGANISM` with an explicit `HUMAN_MODEL_MISMATCH` discussion (see §15.4).

---

## 3. Phenotypes

### 3.1 Cohort-derived frequency table (Sobering et al. 2022, n = 16 affected males with LoF variants) ⚠

All frequencies below are from the PMC full text of PMID:35469323 and **must be re-verified against the paper before entering as `frequency:` with evidence** (see `docs/frequency-evidence-guidelines.md` — a frequency band needs its own quantitative snippet).

| Phenotype | Frequency (Sobering 2022) | Suggested HPO term | Suggested dismech `frequency` band |
|---|---|---|---|
| Developmental delay (global) | 16/16 (100%) | HP:0001263 Global developmental delay | OBLIGATE / VERY_FREQUENT |
| Speech delay | 16/16 (100%) | HP:0000750 Delayed speech and language development | OBLIGATE / VERY_FREQUENT |
| Intellectual disability (borderline→severe) | 14/16 (88%) | HP:0001249 Intellectual disability | VERY_FREQUENT |
| Fine motor delay | 14/16 (88%) | HP:0007010 Poor fine motor coordination ⚠ *(term not verified)* | VERY_FREQUENT |
| Gross motor delay (mean walking 20 mo) | 12/16 (75%) | HP:0002194 Delayed gross motor development ⚠ | FREQUENT |
| Hypertelorism | 11/16 (69%) | HP:0000316 Hypertelorism ⚠ | FREQUENT |
| Retrognathia | 10/16 (63%) | HP:0000278 Retrognathia ⚠ | FREQUENT |
| Infantile feeding difficulty | 10/16 (63%) | HP:0011968 Feeding difficulties ⚠ | FREQUENT |
| Elongated (long) face | 8/16 (50%) | HP:0000276 Long face | FREQUENT |
| Autism spectrum disorder | 7/16 (44%) | HP:0000717 Autism ⚠ | FREQUENT |
| ADHD | 7/16 (44%) | **HP:0007018 Attention deficit hyperactivity disorder** ✅ *(label verified via OLS)* | FREQUENT |
| Microcephaly | 6/16 (38%) | HP:0000252 Microcephaly | OCCASIONAL/FREQUENT |
| High-arched palate | 6/16 (38%) | HP:0000218 High palate ⚠ | OCCASIONAL |
| Seizures | 5/16 (31%) | HP:0001250 Seizure ⚠ | OCCASIONAL |
| Low-set ears (4 posteriorly rotated) | 5/16 (31%) | HP:0000369 Low-set ears ⚠ | OCCASIONAL |
| **Orofacial clefting** | **3/16 (19%)** | HP:0410030 Cleft lip ✅ / HP:0000175 Cleft palate | OCCASIONAL |

### 3.2 HPO disease annotations currently attached to OMIM:300263

Retrieved from the HPO annotation API (ontology.jax.org) ⚠ — note these derive from the **older, clefting-ascertained families**, which is why cleft frequencies are far higher than in Sobering:

| HPO ID | Label | Annotated frequency |
|---|---|---|
| HP:0001256 | Mild intellectual disability | 7/7 |
| HP:0000276 | Long face | 4/4 |
| HP:0410030 | Cleft lip | 6/8 |
| HP:0000175 | Cleft palate | 5/8 |
| HP:0000455 | Broad nasal tip | 3/7 |
| HP:0001176 | Large hands | 2/7 |
| HP:0001763 | Pes planus | 1/7 |
| HP:0000252 | Microcephaly | 1/1 |
| HP:0001249 | Intellectual disability | 1/1 |
| HP:0000750 | Delayed speech and language development | — |
| HP:0000340 | Sloping forehead | — |
| HP:0000582 | Upslanted palpebral fissure | — |
| HP:0000336 | Prominent supraorbital ridges | — |
| HP:0000664 | Synophrys | — |
| HP:0002162 | Low posterior hairline | — |
| HP:0001611 | Hypernasal speech | — |
| HP:0002942 | Thoracic kyphosis | — |
| HP:0001166 | Arachnodactyly | — |
| HP:0010511 | Long toe | — |
| HP:0001419 | X-linked recessive inheritance | — |

Additional features named in OMIM/GTR/MalaCards summaries but not in the HPO table above ⚠: **cryptorchidism**, **preaxial polydactyly**, **broad nasal bridge**. Treat these as low-confidence single-case observations.

### 3.3 Neuroimaging phenotypes (6 individuals imaged, Sobering 2022) ⚠

- 1 normal
- 1 mildly increased subarachnoid space + white matter changes
- **2 (identical twins) polymicrogyria and cortical dysplasia** → HP:0002126 Polymicrogyria ⚠
- 1 abnormal striatal signal (caudate/globus pallidus)
- 1 cranio-occipital malformation + thin corpus callosum → HP:0033725 / HP:0002079 ⚠

The twin polymicrogyria observation is mechanistically interesting given the 2026 finding that PHF8 loss arrests neurogenesis in mouse embryos (§6.6), but n = 2 in one family — curate as OCCASIONAL at most.

### 3.4 The clefting discordance — flag this explicitly in the KB entry

The single most important curation nuance for this disease: **earlier cohorts were ascertained *because of* clefting** (Koivisto et al. 2007 screened 7,712 cleft-surgery patients), so cleft frequency in the pre-2022 literature (~70–75%) is inflated by design. Sobering et al. found 3/16 (19%) and concluded ⚠:

> "Orofacial clefting was seen in three individuals from our cohort, suggesting that this feature is less common than previously reported."

Recommendation for the dismech entry: annotate cleft lip/palate as a **characteristic but not obligate** feature (`frequency: OCCASIONAL` per Sobering) with a `notes:` field recording the ascertainment-bias discordance, and cite both frequency sources.

### 3.5 Phenotype characteristics

- **Onset:** clefting is **congenital** (HP:0003577 Congenital onset ⚠); developmental delay is apparent in **infancy/early childhood** (HP:0011463 Childhood onset ⚠); facial gestalt evolves with age (elongated face "tends to worsen with age" ⚠).
- **Severity:** classically mild-to-borderline ID; Sobering broadened this to **borderline through severe**, with two individuals having no ID (one with dyscalculia, one with mild learning difficulties) ✅ — "All affected individuals exhibited developmental delay and all but two had borderline to severe ID."
- **Progression:** **static / non-progressive** neurodevelopmental disorder. No neurodegeneration, no regression, and no progressive organ involvement has been reported in any of the ~29 published individuals. Use `clinical_course: STABLE` for the ID node.
- **Frequency among affected individuals:** see tables above.

### 3.6 Quality-of-life impact

❌ **No disease-specific QoL data exist** (no EQ-5D, SF-36, PROMIS, or disease-specific instrument has been applied). Inferable, non-citable impacts: educational support needs (universal DD), speech intelligibility (hypernasal speech + clefting), feeding difficulty in infancy (63%), behavioral/social burden of ASD+ADHD (~44% each), and seizure burden (31%). Do **not** assert QoL numbers.

---

## 4. Genetic / Molecular Information

### 4.1 Gene

**PHF8** (PHD finger protein 8), Xp11.22, NCBI Gene 23133, HGNC:20672, OMIM 300560. Aliases: JHDM1F, KDM7B, ZNF422, KIAA1111, MRXSSD.

Protein: UniProt Q9UPP1, canonical isoform **1,060 aa** (Sobering et al. describe the disease-relevant isoform as **1,024 aa**; multiple transcript variants exist — note the discrepancy when curating). Domains: N-terminal **PHD finger** (H3K4me3 reader), central **JmjC catalytic domain (aa 231–387 per UniProt)**, **multiple nuclear localization signals**, and a **serine-rich region**. Subcellular localization: nucleus and nucleolus; "recruited to H3K4me3 sites on chromatin during interphase" and dissociates during mitosis ⚠ (UniProt).

### 4.2 Reported pathogenic variants

**Previously reported (the "five previous reports," 8 individuals)** — as tabulated in Sobering et al. Table 1 ⚠:

| cDNA | Protein | Type | Original report |
|---|---|---|---|
| c.943_946+8del | p.(Thr315Leufs*25) | frameshift/splice-region deletion | Siderius et al. 1999 family (molecularly solved by Laumonnier 2005) |
| c.631C>T | p.(Arg211*) | nonsense | Laumonnier et al. 2005 (PMID:16199551) |
| c.529A>T | p.(Lys177*) | nonsense | Abidi et al. 2007 (PMID:17594395) |
| c.836C>T | p.(Phe279Ser) | **missense, catalytically dead** | Koivisto et al. 2007 (PMID:17661819) |
| c.144C>A | p.(Tyr48*) | nonsense | Ibarluzea et al. ⚠ (year cited as 2013 in the table; verify) |

**New in Sobering et al. 2022 (11 LoF variants / 11 families, 16 males)** ⚠:

| cDNA | Protein | Type | Inheritance |
|---|---|---|---|
| del exons 9–10 | p.Gly316_Arg380del | intragenic deletion | maternal |
| c.294-1820_597-603del | p.Ser98_Thr198del | intragenic deletion | maternal |
| c.596+1G>A | — | splice donor | **de novo** |
| c.1627-1G>A | — | splice acceptor | **de novo** |
| c.1731-2A>G | — | splice acceptor | maternal |
| c.862C>T | p.(Gln288*) | nonsense | maternal |
| c.1030C>T | p.(Gln343*) | nonsense | maternal |
| c.738_739insT | p.(His247Serfs*3) | frameshift | maternal |
| c.1965_1966dup | p.(Glu656Valfs*174) | frameshift | **de novo** |
| c.1996delG | p.(Glu666Argfs*163) | frameshift | maternal |
| c.2760dupC | p.(Thr921Hisfs*19) | frameshift | maternal |

**VUS reported (5 individuals / 4 families, all maternally inherited missense)** ⚠: c.143A>G p.(Tyr48Cys); c.257C>T p.(Thr86Met); c.808C>T p.(Arg270Cys); c.1150G>A p.(Glu384Lys). Sobering explicitly separates these from the LoF cohort — do **not** curate them as pathogenic.

A benign in-frame variant to know about: **p.Ser969del** — "it is abundantly found in gnomAD in both heterozygous males and homozygous females" ⚠ (Sobering 2022). Useful as a negative control / interpretation caveat.

### 4.3 Variant classification, spectrum, and origin

- **Origin:** germline, exclusively. No somatic PHF8 disease variants relevant to this disorder (somatic/overexpression PHF8 biology is a *cancer* story — see §6.9 — and must be kept out of the disease mechanism graph).
- **Types:** nonsense, frameshift, canonical splice-site, intragenic multi-exon deletions, contiguous Xp11.22 deletions, and one recurrent catalytically inactivating missense (F279S). The older literature emphasized that mutations **cluster in the JmjC-encoding exons**; the 2022 cohort shows LoF variants distributed across the gene, including C-terminal frameshifts.
- **Functional consequence:** **loss of function** — via (a) truncation removing the JmjC domain and NLSs, (b) catalytic inactivation, and (c) mislocalization.

Loenarz et al. ✅ on both loss-of-catalysis and mislocalization:

> "Clinically observed mutations to the PHF8 gene cluster in exons encoding for the double stranded beta-helix fold and will therefore disrupt catalytic activity."
> "This mutant encodes a F279S variant of PHF8 that modifies a conserved hydrophobic region; assays with both peptides and intact histones reveal this variant to be catalytically inactive."
> (full text) "In contrast to the wild-type HA-PHF8, analogous studies revealed that the clinically observed F279S variant did not show clear nuclear localization, with apparent cytoplasmic localization."

Abidi et al. 2007 ✅ on the truncation mechanism:

> "The mutation results in a truncated PHF8 protein lacking the Jumonji-like C terminus domain and five nuclear localization signals."

Koivisto et al. 2007 ✅ on F279S:

> "A novel missense mutation c.836C>T of the PHF8 gene was identified in a Finnish family with multiple-affected male patients. The mutation resides in exon 8 and changes phenylalanine to serine (F279S) in the functionally important Jmonji C domain of the protein."
> "The mutation was not present in 200 anonymous blood donors (approximately 300 X-chromosomes)."

Independent confirmation of F279S catalytic death: Qi et al. 2010 ✅ ("a point mutation in the catalytic domain (phenylalanine to serine, F279S) abolished PHF8 demethylase activities"); Qiu et al. 2010 ✅ ("a mutant PHF8 (phenylalanine at position 279 to serine) identified in the XLMR patients is defective in enzymatic activity, indicating that the loss of histone demethylase activity is causally linked with the onset of disease"); Fortschegger et al. 2010 ✅ ("a PHF8 disease mutant was defective in demethylation and in coactivation").

### 4.4 Population / database data

- **ClinVar:** 537 total records for `PHF8[gene]`; 251 returned by a `pathogenic[clinical significance]` filter ⚠ — **this filter over-counts** (it captures likely-pathogenic and conflicting interpretations); do not quote 251 as "pathogenic variants." Get the exact breakdown from ClinVar Miner or a fresh ClinVar query before curating.
- **gnomAD constraint (pLI / LOEUF / o-e LoF):** ❌ **not retrievable this session** (gnomAD's GraphQL endpoint requires POST; DECIPHER blocked). This must be filled in manually before curating any constraint claim.
- **Allele frequency of pathogenic variants:** all reported pathogenic variants are private/family-specific. No founder allele is known. F279S absent from ~300 control X chromosomes (Koivisto) ✅.
- **ClinGen Gene-Disease Validity:** reported as **Definitive** for PHF8 – syndromic X-linked intellectual disability Siderius type, X-linked, supported by ≥7 variants from 5 publications plus mouse, zebrafish and cell-culture models with rescue; mechanism = loss of function ⚠. **Recommended action:** rather than citing a web page, run `just clingen-refresh` and cite the `CGGV:` assertion as a structured-source evidence row.

### 4.5 Epigenetic information

Two distinct senses matter here and should not be conflated in the KB:

1. **PHF8 is itself an epigenetic effector** — its loss changes the histone-methylation landscape (see §6). This is the disease mechanism.
2. **Episignature (methylation signature) for diagnostic classification:** ❌ **No published DNA-methylation episignature for PHF8-XLID was found.** Many chromatinopathies (Kabuki, Sotos, CHARGE, etc.) have EpiSign classifiers; PHF8 does not appear among them in the retrieved literature. This is a genuine, curatable **knowledge gap** and a natural `proposed_experiments` item.

### 4.6 Chromosomal abnormalities

Xp11.22 microdeletions removing PHF8 (± FAM120C, WNK3) — Qiao 2008 (PMID:18498374, familial deletion in two brothers with ASD; "complete deletion of the plant homeodomain finger protein 8 (PHF8) gene" ⚠), De Wolf 2014 (PMID:25258334, syndromic autism ⚠), Huang 2020 (PMID:32219840, prenatal detection in a fetus with cleft lip and palate ⚠). These support CMA as a diagnostic modality and support haploinsufficiency/nullisomy as the mechanism.

---

## 5. Environmental Information

- **Environmental factors:** none established. The only mechanistically grounded candidate is **gestational hypoxia** acting on an O₂-dependent 2‑OG oxygenase (§2.3) — hypothesis only.
- **Lifestyle factors:** none disease-specific. Maternal smoking is cited by Loenarz et al. only as a general hypoxia-mediated cleft risk factor in the population, **not** as a PHF8 interaction.
- **Infectious agents:** not applicable.
- **Toxicological note (model-organism only, do not curate as human etiology):** chronic exposure to the PFAS replacement GenX induced transgenerational motor deficits via the *C. elegans* PHF8 ortholog *jmjd-1.2* (PMID:40803444, Environ Pollut 2025) ⚠. Interesting as a conservation-of-mechanism datapoint (§14), not as a human risk factor.

---

## 6. Mechanism / Pathophysiology

### 6.1 The core enzymatic lesion (MOLECULAR scale)

PHF8 is a **PHD-finger reader + JmjC-domain eraser**: it binds H3K4me3 at active promoters through its PHD finger and removes repressive mono-/di-methyl marks through its Fe(II)/2‑OG-dependent JmjC domain, thereby acting as a **transcriptional coactivator**.

Loenarz et al. 2010 ✅:
> "We report that recombinant PHF8 is an Fe(II) and 2-oxoglutarate-dependent N(epsilon)-methyl lysine demethylase, which acts on histone substrates. PHF8 is selective in vitro for N(epsilon)-di- and mono-methylated lysine residues and does not accept trimethyl substrates."
> (full text) "our results reveal that PHF8 is a 2OG oxygenase with selectivity for H3K9me2/me1, H3K27me2 and H3K36me2 residues."

Kleine-Kohlbrecher et al. 2010 ✅:
> "the XLMR protein PHF8 and a C. elegans homolog F29B9.2 catalyze demethylation of di- and monomethylated lysine 9 of histone H3 (H3K9me2/me1). The PHD domain of PHF8 binds to H3K4me3 and colocalizes with H3K4me3 at transcription initiation sites."

Qi et al. 2010 (Nature) ✅ — the H4K20me1 activity and the genome-wide picture:
> "Here we provide multiple lines of evidence establishing PHF8 as the first mono-methyl histone H4 lysine 20 (H4K20me1) demethylase, with additional activities towards histone H3K9me1 and me2."
> "PHF8 is located around the transcription start sites (TSS) of approximately 7,000 RefSeq genes and in gene bodies and intergenic regions (non-TSS). PHF8 depletion resulted in upregulation of H4K20me1 and H3K9me1 at the TSS and H3K9me2 in the non-TSS sites, respectively, demonstrating differential substrate specificities at different target locations."
> "Importantly, patient mutations significantly compromised PHF8 catalytic function."

Fortschegger et al. 2010 ✅ — the RNAPII coupling:
> "Chromatin immunoprecipitation followed by high-throughput sequencing indicated that PHF8 is enriched at the transcription start sites of many active or poised genes, mirroring the presence of RNA polymerase II (RNAPII) and of H3K4me3-bearing nucleosomes... we present evidence for direct interaction of PHF8 with the C-terminal domain of RNAPII."

Feng et al. 2010 (PMID:20208542) adds the rDNA/nucleolar arm: PHF8 "activates transcription of rRNA genes through H3K4me3 binding and H3K9me1/2 demethylation" ⚠.

**Suggested GO annotations (verify all with OAK before use):**

| GO ID | Label | Verification |
|---|---|---|
| GO:0032454 | histone H3K9 demethylase activity | ✅ label verified via OLS |
| GO:0035575 | histone H4K20 demethylase activity | ✅ label verified via OLS |
| GO:0140457 / GO:0071558 | H3K27 demethylase activity | ⚠ ID not verified — check |
| GO:0006338 | chromatin remodeling | ⚠ |
| GO:0045893 | positive regulation of DNA-templated transcription | ⚠ |
| GO:0006360 | transcription by RNA polymerase I | ⚠ (rDNA arm) |
| GO:0060021 | roof of mouth development | ✅ label verified via OLS |
| GO:0000082 | G1/S transition of mitotic cell cycle | ⚠ |
| GO:0032008 | positive regulation of TOR signaling | ⚠ |
| GO:0006564 | L-serine biosynthetic process | ⚠ |
| GO:0006914 | autophagy | ⚠ |

CHEBI cofactors/substrates: 2-oxoglutarate (CHEBI:16810 ⚠), iron(2+) (CHEBI:29033 ⚠), dioxygen (CHEBI:15379 ⚠), L-serine (CHEBI:17115 ⚠), sirolimus/rapamycin (**CHEBI:9168** ✅ verified).

### 6.2 Downstream arm 1 — neuronal/cognitive: the mTOR–RSK1 axis

Chen et al. 2018 (Nat Commun, PMID:29317619) ✅ is the strongest mechanistic chain from gene to cognition, and it is **druggable**:

> "Here we report that Phf8 knockout mice displayed impaired learning and memory, and impaired hippocampal long-term potentiation (LTP) without gross morphological defects. We also show that mTOR signaling pathway is hyperactive in hippocampus in Phf8 knockout mouse. Mechanistically, we show that demethylation of H4K20me1 by Phf8 results in transcriptional suppression of RSK1 and homeostasis of mTOR signaling. Pharmacological suppression of mTOR signaling with rapamycin in Phf8 knockout mice recovers the weakened LTP and cognitive deficits."

Causal chain: **PHF8 loss → failure to demethylate H4K20me1 at *RSK1* → RSK1 de-repression → mTOR hyperactivation in hippocampus → impaired LTP → learning/memory deficit** (rescued by rapamycin). Note the paper places PHF8 in the same "mTORopathy-adjacent" company as tuberous sclerosis, Fragile X and Down syndrome ✅ (intro).

### 6.3 Downstream arm 2 — neuronal differentiation and cytoskeleton

- **RAR coactivation / neuronal differentiation** — Qiu et al. 2010 (Cell Res, PMID:20548336) ✅: "knockdown of PHF8 in mouse embryonic carcinoma P19 cells impairs RA-induced neuronal differentiation, whereas overexpression of the wild-type but not the F279S mutant PHF8 drives P19 cells toward neuronal differentiation. Furthermore, we show that PHF8 interacts with RARalpha and functions as a coactivator for RARalpha."
- **Cytoskeleton / neurite outgrowth** — Asensio-Juan et al. 2012 (NAR, PMID:22850744) ✅: "PHF8 controls the expression of genes involved in cell adhesion and cytoskeleton organization such as RhoA, Rac1 and GSK3β... Further analysis in neurons shows that depletion of PHF8 results in down-regulation of cytoskeleton genes and leads to a deficient neurite outgrowth. Overall, our results suggest that the mental retardation phenotype associated with loss of function of PHF8 could be due to abnormal neuronal connections as a result of alterations in cytoskeleton function."
- **REST/NRSF co-occupancy at neuronal gene promoters** — Wang et al. 2014 (Sci Rep, PMID:24852203) ✅ (title/abstract: "PHF8 and REST/NRSF co-occupy gene promoters to regulate proximal gene expression").

### 6.4 Downstream arm 3 — glial biology (newer, and under-appreciated)

- **Astrocytes** — Iacobucci et al. 2021 (Development, PMID:34081130) ✅: "we investigate the contribution of the XLID-associated histone demethylase PHF8 to astrocyte differentiation and function. Using genome-wide analyses and biochemical assays in mouse astrocytic cultures, we reveal a regulatory crosstalk between PHF8 and the Notch signaling [pathway]…"
- **Oligodendrocytes** — Kremp et al. 2024 (Glia, PMID:38613395) ✅: "Phf8 promotes the proliferation of rodent oligodendrocyte progenitor cells and impairs their differentiation to oligodendrocytes... Phf8 has a strong positive impact on Olig2 expression by acting on several regulatory regions of the gene and changing their histone modification profile... We conclude that Phf8 may impact nervous system development at least in part through its action in oligodendroglial cells." Companion review: Kremp & Wegner 2026, Neural Regen Res (PMID:40145966) ⚠.

This gives a **non-neuronal (glial) contribution to the neurodevelopmental phenotype** — worth its own pathophysiology node with CL:0002453 (oligodendrocyte precursor cell ✅ verified) and CL:0000127 (astrocyte ⚠).

### 6.5 Downstream arm 4 — craniofacial / midline development

Qi et al. 2010 ✅ provides the only direct in-vivo craniofacial mechanism:

> "PHF8 regulates cell survival in the zebrafish brain and jaw development, thus providing a potentially relevant biological context for understanding the clinical symptoms associated with PHF8 patients. Lastly, genetic and molecular evidence supports a model whereby PHF8 regulates zebrafish neuronal cell survival and jaw development in part by directly regulating the expression of the homeodomain transcription factor MSX1/MSXB, which functions downstream of multiple signalling and developmental pathways. Our findings indicate that an imbalance of histone methylation dynamics has a critical role in XLMR."

*MSX1* is a well-established human orofacial-clefting gene, which makes the PHF8→MSX1 link the most credible molecular explanation for the clefting phenotype. Kremp et al. 2024 ✅ independently characterize Phf8 as "implicated by mutation in mice and humans in neural crest defects and neurodevelopmental disturbances." Bone-forming relevance: Han et al. 2015 (PMID:25923143) ⚠ — "PHF8, a major H4K20/H3K9 demethylase, plays a critical role in craniofacial and bone development."

Causal chain: **PHF8 loss → H4K20me1/H3K9me1-2 accumulation at *MSX1/msxb* → reduced MSX1 expression in cranial neural crest-derived facial primordia → impaired fusion of facial prominences / palatal shelves → cleft lip ± cleft palate**, in parallel with **increased apoptosis of brain cells**.

### 6.6 Downstream arm 5 — metabolic control of neurogenesis (2026, newest)

Artés/Iacobucci et al. 2026 (EMBO Rep, PMID:41714361) ⚠ identifies "PHF8 as a key driver of the serine biosynthesis pathway, safeguarding the intracellular serine pool essential for neural progenitor proliferation," with PHF8 depletion causing disrupted metabolism, blocked autophagy, replication defects and proliferation arrest, and PHF8 deficiency halting neurogenesis and brain development in mouse embryos. **This is the newest and arguably most important mechanistic advance for this disease** — it supplies a proliferation/metabolism node upstream of the cognitive phenotype and is consistent with the polymicrogyria seen in the twins. Verify the abstract before quoting.

### 6.7 Downstream arm 6 — cell cycle, DNA damage, transcription recovery

- **Cell cycle:** PHF8 controls the G1–S transition with E2F1/HCF-1/SET1A via H4K20me1 demethylation (Liu et al. 2010, Nature, PMID:20622854) ⚠.
- **DNA damage:** Kim et al. 2024 (NAR, PMID:39087553) ⚠ — PHF8 is "the major demethylase that reverses transcriptionally repressive epigenetic modification laid down by the DYRK1B-EHMT2 pathway," concentrating at damage tracks and promoting "timely resolution of local H3K9me2 to facilitate the resumption of transcription," including at rDNA. Relevance to the neurodevelopmental phenotype is unestablished — curate as mechanistic context, not as disease mechanism.

### 6.8 Immune / metabolic / tissue-damage dimensions

- **Immune:** no immunodeficiency or autoimmunity in patients. A 2026 paper (PMID:41709745) ⚠ reports "the Znf711-Phf8 complex functions as a transcriptional rheostat essential for neutrophil development" in a model system — no human hematologic phenotype has been reported in PHF8-XLID, so this is a **prediction to watch**, not a curatable human phenotype.
- **Metabolic:** the serine-biosynthesis finding (§6.6) is the only metabolic axis. No metabolic decompensation phenotype; do **not** conform this entry to `metabolic_intoxication_decompensation`.
- **Tissue damage:** none — this is a developmental, not a degenerative or inflammatory, disorder. No fibrosis, ischemia, oxidative-injury or necrosis mechanism applies.

### 6.9 ⚠ Scope guardrail: the PHF8 cancer literature

A large and growing body of work (≥20 papers in 2025–2026 alone: TNBC, gastric, prostate, hepatocellular, colorectal) treats PHF8 as an **overexpressed oncogenic driver and drug target**. This is the *opposite* direction of effect from the disease (LoF), involves somatic/expression biology rather than germline lesions, and **must not be imported into this disease entry's pathophysiology graph**. If any of it is curated at all, it belongs in a separate context with an explicit note that the disease is loss-of-function.

### 6.10 Suggested pathophysiology node chain for the dismech entry

```
1. PHF8 Loss-of-Function Variant (MOLECULAR)
     ↓ CAUSES
2. Loss of JmjC Histone Demethylase Activity (MOLECULAR)
     [H3K9me1/2, H4K20me1, H3K27me2 fail to be erased; PHD-H3K4me3 reading uncoupled from erasure]
     ↓ CAUSES
3. Failure of PHF8-Dependent Transcriptional Coactivation at Target Promoters (MOLECULAR)
     ↓ branches into:
   3a. RSK1 de-repression → mTOR hyperactivation (CELLULAR)  → impaired hippocampal LTP (CELLULAR/TISSUE) → ID, learning/memory deficit (ORGANISM)
   3b. Impaired serine biosynthesis / autophagy block in neural progenitors (CELLULAR) → arrested neurogenesis (TISSUE) → ID ± cortical malformation (ORGANISM)
   3c. Impaired RAR-dependent neuronal differentiation + RhoA/Rac1/GSK3β cytoskeletal gene loss (CELLULAR) → deficient neurite outgrowth/connectivity (CELLULAR) → ID/ASD (ORGANISM)
   3d. Impaired Olig2 induction in OPCs / Notch-crosstalk in astrocytes (CELLULAR) → altered glial development (TISSUE) → contributory NDD (ORGANISM)
   3e. Reduced MSX1/msxb in cranial neural crest derivatives (MOLECULAR/CELLULAR) → failed fusion of facial prominences and palatal shelves (TISSUE) → cleft lip/palate (ORGANISM)
```

Treatment link for the drug-target pattern: an mTOR-inhibitor node (`target_mechanisms` with `INHIBITS` on node 3a) is the natural place to hang rapamycin — but **flag it as preclinical-only** (mouse, no human data).

**Module conformance assessment:** no existing `kb/modules/` module is a clean fit. `pharyngeal_arch_patterning_serial_homology` is *tempting* for the craniofacial arm but is the wrong mechanism — Siderius clefting is a **midline fusion failure** (lip/palate), not a serially homologous arch-derivative bundle (mandible+maxilla+zygoma+ear), and the lesion is chromatin-level, not an arch-identity code. Recommend **no `conforms_to`** rather than a forced fit. A future "chromatinopathy / histone-modifier neurodevelopmental disorder" module would be the right home; note this as a module-creation candidate.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

| Structure | Involvement | UBERON (⚠ all need OAK verification) |
|---|---|---|
| Brain | Primary — cognition, LTP, neurogenesis | UBERON:0000955 brain |
| Hippocampus | Primary — LTP deficit locus (mouse) | UBERON:0002421 hippocampal formation |
| Cerebral cortex | Polymicrogyria/cortical dysplasia in 2/6 imaged | UBERON:0000956 cerebral cortex |
| Prefrontal cortex | Serotonin-signaling dysregulation (mouse) | UBERON:0000451 prefrontal cortex |
| Corpus callosum | Thin in 1/6 imaged | UBERON:0002336 corpus callosum |
| Striatum (caudate, globus pallidus) | Abnormal signal in 1/6 | UBERON:0002435 striatum |
| Upper lip | Cleft lip | UBERON:0001834 upper lip |
| Palate / secondary palate | Cleft palate, high-arched palate | UBERON:0001716 secondary palate |
| Face / craniofacial skeleton | Dysmorphism, retrognathia, elongated face | UBERON:0001456 face |
| Ear (external) | Low-set, posteriorly rotated | UBERON:0001690 ear |
| Hands / feet | Large hands, arachnodactyly, long toes, pes planus | UBERON:0002398 manus / UBERON:0002387 pes |
| Vertebral column | Thoracic kyphosis | UBERON:0002415 vertebral column ⚠ |
| Testis | Cryptorchidism (rare) | UBERON:0000473 testis |

**Body systems:** nervous (primary), craniofacial/musculoskeletal (secondary), and — in a minority — genitourinary. No cardiac, renal, hepatic, hematologic, immune, endocrine or ophthalmologic involvement is reported.

**Lateralization:** clefting may be **unilateral or bilateral** (Koivisto's two siblings differed: one unilateral CL/P, one bilateral CL/P ✅) — a nice intrafamilial-variability datapoint. Facial asymmetry is noted as "mild" in Sobering ⚠.

### 7.2 Tissue and cell level

| Cell type | Role | CL term |
|---|---|---|
| Central nervous system neuron | Target of impaired differentiation, neurite outgrowth, LTP | **CL:2000029** ✅ verified |
| Neural progenitor / neural stem cell | Proliferation arrest via serine pathway (2026) | CL:0000047 neural stem cell ⚠ |
| Oligodendrocyte precursor cell | Phf8 promotes proliferation, Olig2 effector | **CL:0002453** ✅ verified |
| Oligodendrocyte | Differentiation altered | CL:0000128 ⚠ |
| Astrocyte | Differentiation/function via Notch crosstalk | CL:0000127 ⚠ |
| Cranial neural crest cell / migratory neural crest cell | Craniofacial/clefting arm (zebrafish, mouse) | CL:0000333 ⚠ |
| Bone marrow stromal cell / osteoblast lineage | Craniofacial bone formation (Han 2015) | CL:0000134 / CL:0000062 ⚠ |
| Neutrophil (model-only, no human phenotype) | Znf711-Phf8 rheostat | CL:0000775 ⚠ |

### 7.3 Subcellular level

- **Nucleus** (GO:0005634 ⚠) — primary site of PHF8 action; **chromatin** (GO:0000785 ⚠); **nucleolus** (GO:0005730 ⚠) for the rDNA/RNA Pol I arm.
- Pathogenic relevance: F279S and truncating variants that delete the NLSs cause **cytoplasmic mislocalization** — the subcellular compartment shift is itself part of the molecular pathology ✅ (Loenarz full text).

---

## 8. Temporal Development

- **Onset:**
  - *Prenatal/congenital:* orofacial clefting (detectable on prenatal ultrasound/CMA — Huang 2020 ⚠); brain malformations where present.
  - *Infancy:* feeding difficulties (63%), hypotonia/motor delay; mean age at independent walking **20 months** ⚠.
  - *Early childhood:* speech delay (100%), then ID; ASD/ADHD typically recognized in preschool/school years.
- **Onset pattern:** **congenital/insidious developmental**, not acute.
- **Progression:** **static (non-progressive)**. There is no reported regression, neurodegeneration, or organ deterioration. The facial gestalt evolves (long face becomes more marked with age ⚠) — that is a morphologic evolution, not disease progression.
- **Course:** chronic, lifelong.
- **Stages:** no staging system exists or is applicable.
- **Remission:** not applicable.
- **Critical periods:**
  - *Weeks 4–10 of gestation* — lip and palatal fusion; the only window in which the clefting phenotype could theoretically be modified (and the window in which the hypoxia hypothesis would operate).
  - *Perinatal-to-early-childhood* — the intervention window for cleft repair, feeding support, and early developmental/speech intervention, where outcome is genuinely modifiable.
  - *Preclinically*, the Chen 2018 rapamycin rescue was performed in adult mice and **restored** LTP and cognition — implying, in mice, a post-developmental window of reversibility. That is a striking and citable claim, but strictly `MODEL_ORGANISM` evidence.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **Prevalence:** ❌ no formal estimate published. Orphanet classifies it in its rare-disease register; based on ~29 reported individuals worldwide, the appropriate dismech `prevalence_class` is **`BELOW_1_IN_1000000`** or, more defensibly, **`NOT_YET_DOCUMENTED`** with `measure_type: CASES_IN_LITERATURE` and a count. Recommended structured record:
  ```yaml
  prevalence:
  - population: Worldwide
    measure_type: CASES_IN_LITERATURE
    prevalence_class: NOT_YET_DOCUMENTED
    notes: >-
      Approximately 29 affected males from ~15 families reported: 8 individuals
      in five reports before 2022, plus 16 individuals from 11 families in
      Sobering et al. 2022 (plus 5 individuals with VUS from 4 families).
  ```
- **Incidence:** ❌ unknown.
- **Denominator context (do not attribute to this disorder):** X-linked ID overall affects ~1–4 per 2,000 males — Qi et al. 2010 ✅: "XLMR affects 1–4 out of 2,000 males, causing intellectual disability (Intelligence Quotient (IQ) <70)". PHF8 is a rare cause within that.
- **Screening-based frequency estimate:** Koivisto et al. sequenced PHF8 in 18 selected patients drawn from a nationwide cohort of **7,712 cleft-surgery patients** and found **one** family ✅ — i.e., PHF8 is a very rare cause of syndromic clefting.

### 9.2 Genetic epidemiology

- **Inheritance:** **X-linked recessive** (HP:0001419 ✅ in HPO annotations; GenCC/ClinGen submissions use HP:0001417 X-linked inheritance). Suggested dismech `inheritance_term`: HP:0001419 X-linked recessive inheritance (bind the `term:` — do not leave `preferred_term` alone).
- **Penetrance:** appears **complete in hemizygous males** for developmental delay (16/16) and near-complete for ID (14/16); **incomplete/variable for clefting** (3/16 in the unbiased cohort). Carrier females: essentially non-penetrant.
- **Expressivity:** **highly variable**, including within families. Abidi et al. ✅ documents intrafamilial variability directly: "One of the truncating mutations was found in the original family with Siderius-Hamel CL/P syndrome where only two of the three affected individuals had mental retardation (MR) with CL/P and one individual had mild MR. The second mutation was present in a family with four affected men, three of whom had MR and CL/P, while the fourth individual had mild MR without clefting."
- **Genotype–phenotype correlation:** **none identified.** Sobering et al. ⚠: "The phenotypic variability does not appear to be linked to the variant location in individuals who harbor a null allele." Variants inside vs. outside the JmjC domain did not differ in severity.
- **Anticipation:** not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** ❌ not reported; cannot be excluded (relevant to recurrence counseling after an apparently de novo variant).
- **Founder effects:** none. The Finnish F279S family is a single family, not a founder population effect.
- **Consanguinity:** not a factor (X-linked recessive in males).
- **Carrier frequency:** ❌ unknown; no population carrier-screening data.

### 9.3 Population demographics

- **Sex ratio:** affected individuals are essentially all **male**. Carrier females are typically unaffected (skewed XCI). ❌ No symptomatic heterozygous female has been convincingly reported in the retrieved literature — this is worth stating explicitly and worth flagging as something to re-check as cohorts grow.
- **Ethnic/geographic distribution:** no predilection. Sobering's 11 families were of diverse ancestry: **9 Western European, 3 Moroccan, 2 Asian-Indian, 1 Afro-Caribbean** (family counts as reported) ⚠. Prior families were Dutch (Siderius), French/Italian (Laumonnier), American (Abidi), Finnish (Koivisto).
- **Age distribution:** lifelong from birth; published individuals span infancy to adulthood.

---

## 10. Diagnostics

### 10.1 Genetic testing (the diagnostic backbone)

There is **no biochemical or imaging test that establishes this diagnosis** — it is molecular.

| Modality | Utility |
|---|---|
| **Exome sequencing (ES)** | **First-line.** Most 2022-cohort diagnoses came from ES (many via GeneDx / UW Center for Mendelian Genomics) ⚠. Detects nonsense, frameshift, splice-site, and missense variants. |
| **Genome sequencing (GS)** | Adds deep-intronic and structural resolution; the c.294-1820_597-603del intragenic deletion illustrates why breakpoint-capable methods matter ⚠. |
| **XLID / ID multigene panels** | PHF8 is included on XLID and broad ID/ASD panels; GTR lists **17 clinical tests** for this condition (14 sequence analysis, 10 del/dup, 2 homozygosity, 1 targeted variant) ⚠. |
| **Single-gene PHF8 sequencing** | Reasonable when the classic gestalt (male, ID + CL/P + long face) is present, or for targeted familial variant testing. |
| **Deletion/duplication analysis (MLPA / exon-level array / read-depth)** | **Essential** — intragenic multi-exon deletions (exons 9–10) occur and are missed by sequencing-only pipelines. |
| **Chromosomal microarray (CMA)** | Detects the Xp11.22 contiguous deletions; also the route to prenatal detection (PMID:32219840) ⚠. |
| Karyotype / FISH | Low yield; FISH used historically to confirm CMA calls (Qiao 2008) ⚠. |
| mtDNA testing, repeat-expansion testing | Not applicable. |
| **RNA sequencing** | Potentially useful for the three canonical-splice variants (functional confirmation of aberrant splicing) — **not** reported as used in any published case; a reasonable `proposed_experiments` item. |
| **Methylation episignature (EpiSign)** | ❌ **Not available for PHF8.** Genuine diagnostic gap for VUS resolution — Sobering reported 5 individuals with unresolved missense VUS who would be the exact use case. |
| Proteomics / metabolomics / liquid biopsy | ❌ not applicable/not developed. |

**Carrier testing:** targeted familial variant testing in the mother; X-inactivation studies are informative but not diagnostic.

### 10.2 Clinical, imaging and functional testing (supportive, not diagnostic)

- **Brain MRI:** variable and non-specific — normal in some, polymicrogyria/cortical dysplasia, thin corpus callosum, striatal signal change, or increased subarachnoid space in others (6 imaged) ⚠. Justified where seizures or focal findings exist.
- **EEG:** indicated for the ~31% with seizures ⚠.
- **Developmental/neuropsychological assessment:** to quantify ID severity and identify ASD/ADHD (formal ASD and ADHD assessment should be routine given ~44% each).
- **Audiology and speech assessment:** required with clefting (velopharyngeal insufficiency → hypernasal speech, HP:0001611) and given universal speech delay.
- **Laboratory tests / biomarkers:** ❌ **none.** No enzyme assay, no metabolite, no circulating biomarker. Histone-methylation levels in patient cells are a research measure, not a clinical test.
- **Biopsy / histopathology:** not indicated.

### 10.3 Clinical criteria and differential diagnosis

- **Standardized diagnostic criteria:** ❌ none published. Diagnosis = compatible phenotype + hemizygous PHF8 LoF variant.
- **Differential diagnosis:**
  - Other **XLID chromatinopathies**, especially the functionally linked ones: **KDM5C/JARID1C** (Claes-Jensen; microcephaly, short stature) and **ZNF711**-related XLID — mechanistically intertwined with PHF8 (Kleine-Kohlbrecher 2010 ✅; Poeta 2019 ⚠).
  - Other **syndromic clefting + ID** disorders: *MSX1*-related (Witkop/orofacial cleft), *IRF6* (Van der Woude — lip pits), *TP63* (EEC), 22q11.2 deletion (velocardiofacial — cardiac, immune, hypocalcemia), Kabuki syndrome (*KMT2D/KDM6A* — another chromatinopathy with clefting).
  - **Xp11.22 contiguous deletion syndrome** (broader phenotype; distinguished by CMA).
  - **Nonsyndromic cleft lip/palate with coincidental ID** — distinguished only by molecular testing.
  - Because clefting is present in only ~19%, **PHF8 should be considered in males with unexplained DD/ID + ASD/ADHD + subtle dysmorphism even without clefting** — arguably the single most actionable clinical message of the 2022 paper.

### 10.4 Screening

- Newborn screening: ❌ not applicable (no treatable metabolic marker).
- Population carrier screening: ❌ not offered; PHF8 is not on standard expanded carrier-screening panels.
- **Cascade testing** of at-risk female relatives after a proband diagnosis: standard of care and the main practical screening activity.

---

## 11. Outcome / Prognosis

- **Survival / life expectancy / mortality:** ❌ **No mortality or survival data have been published.** No deaths attributable to the disorder are reported. Adults are described in multiple families (the original Siderius pedigree and Abidi's four affected men), implying survival to adulthood is expected. **Do not assert a numeric life expectancy.** The defensible statement is: "no evidence of reduced life expectancy has been reported; formal survival data are absent."
- **Morbidity:** driven by (1) lifelong intellectual disability with educational and independent-living implications; (2) neurobehavioral comorbidity (ASD ~44%, ADHD ~44%); (3) epilepsy (~31%); (4) surgical and speech burden of clefting where present (~19%); (5) infant feeding difficulty/failure to thrive (~63%).
- **Disability outcomes:** ID severity spans borderline to severe; most published individuals fall in the mild-to-moderate range. Two individuals in Sobering had no ID (dyscalculia; mild learning difficulty) ✅ — the mild tail of the spectrum is real.
- **QoL measures:** ❌ none applied.
- **Complications:** velopharyngeal insufficiency/hypernasal speech, feeding and growth issues in infancy, seizure-related morbidity, behavioral comorbidity. No progressive organ complications.
- **Recovery potential:** none for the ID itself (static encephalopathy). Cleft repair, speech therapy and educational intervention meaningfully improve function.
- **Prognostic factors:** ❌ none validated. Notably, **variant type and position do not predict severity** ⚠ (Sobering), which is itself a prognostically relevant negative finding — counseling cannot be refined by genotype. Sibling pairs were more concordant than the cohort at large ⚠, hinting at genetic-background modifiers.
- **Prognostic biomarkers:** ❌ none.

---

## 12. Treatment

**There is no disease-modifying therapy.** Management is entirely supportive/symptomatic and follows generic best practice for syndromic ID with clefting. Sobering et al. explicitly offer no management recommendations beyond diagnosis and counseling ⚠.

### 12.1 Suggested treatment annotations (NCIT — ⚠ all IDs require OAK verification against `sqlite:obo:ncit`)

| Treatment | `treatment_term` (NCIT) | `therapeutic_modality` | Notes |
|---|---|---|---|
| Cleft lip and palate surgical repair (cheiloplasty/palatoplasty, staged) | NCIT:C15329 Surgical Procedure ⚠ (check for a specific palatoplasty/cheiloplasty term) | `SURGERY` | Timing per standard cleft-team protocols |
| Speech and language therapy | NCIT:C159273 Speech Therapy ⚠ | `BEHAVIORAL` | Universal indication (100% speech delay; hypernasality) |
| Physical therapy | NCIT:C15302 Physical Therapy ⚠ | `BEHAVIORAL` | Motor delay (75%) |
| Occupational therapy | NCIT:C121351 Occupational Therapy ⚠ | `BEHAVIORAL` | Fine motor delay (88%) |
| Special education / early developmental intervention | NCIT:C15747 Supportive Care ⚠ | `BEHAVIORAL` | |
| Feeding support (specialized cleft bottles, NG feeding, nutrition) | NCIT:C15433 Nutritional Support ⚠ | *needs per-case judgment* — **do not auto-tag `BEHAVIORAL`** per CLAUDE.md guidance | Infantile feeding difficulty 63% |
| Antiseizure medication | NCIT:C15986 Pharmacotherapy ⚠ + `therapeutic_agent` per drug | `SMALL_MOLECULE` | No PHF8-specific ASM preference known |
| ADHD pharmacotherapy (e.g., methylphenidate) | NCIT:C15986 ⚠ | `SMALL_MOLECULE` | Generic ADHD management; no disease-specific evidence |
| ASD behavioral intervention | NCIT:C15747 ⚠ / behavioral counseling NCIT:C181743 ⚠ | `BEHAVIORAL` | |
| Genetic counseling | NCIT:C15240 Genetic Counseling ⚠ | *n/a* | X-linked recurrence risk; carrier and prenatal options |
| Audiology / hearing management | — | `DEVICE` (if hearing aid) | Cleft-associated otitis media risk (general cleft care) |

### 12.2 Pharmacogenomics

❌ No PHF8-specific pharmacogenomic interactions are known. Standard CPIC guidance applies to any ASM or psychotropic used.

### 12.3 Advanced therapeutics

- **Gene therapy / gene editing / ASO / siRNA / cell therapy:** ❌ **none in development.** No PHF8 program appears in the retrieved literature or trial registries. Note that ASO strategies are ill-suited here — the lesion is loss of a large multidomain nuclear enzyme, not a splice-correctable or knockdown-amenable target (a few canonical splice-site variants are conceivable splice-modulation targets, but this is speculative).
- **Targeted / repurposed pharmacotherapy — the one real lead:** **rapamycin/sirolimus (CHEBI:9168 ✅)**, based on Chen et al. 2018 ✅ ("Pharmacological suppression of mTOR signaling with rapamycin in Phf8 knockout mice recovers the weakened LTP and cognitive deficits... provides a potential therapeutic drug target to treat XLID"). **Strictly preclinical, mouse-only, and complicated by the Walsh 2017 Phf8-KO line showing *no* cognitive impairment (§15.4).** Curate as `evidence_source: MODEL_ORGANISM` with an explicit caveat; do not present as a treatment option.
- **Immunotherapy:** not applicable.

### 12.4 Clinical trials

❌ **No clinical trials for Siderius syndrome / PHF8-XLID were identified.** No NCT identifiers to record.

### 12.5 Treatment outcomes, adverse events, algorithms

❌ No disease-specific response rates, adverse-event data, treatment algorithms, combination regimens, or genotype-guided strategies exist. Cleft repair outcomes follow general cleft-care literature and should not be attributed to this disorder.

---

## 13. Prevention

- **Primary prevention:** not possible for a germline monogenic disorder. **Genetic counseling** is the operative intervention: a carrier mother has a 50% chance of transmitting the variant to each child — affected sons, carrier daughters. De novo occurrence in ~3/11 families ⚠ means recurrence risk is low but not zero after an apparently de novo event (germline mosaicism cannot be excluded).
- **Reproductive options:** prenatal diagnosis (CVS/amniocentesis with targeted variant testing), **preimplantation genetic testing for monogenic disorders (PGT-M)**, donor gametes. Prenatal ultrasound may detect clefting; Xp11.22 deletions are detectable by prenatal CMA (PMID:32219840) ⚠.
- **Secondary prevention (early detection):** cascade carrier testing of maternal female relatives; early developmental surveillance in known at-risk males, enabling early speech/behavioral intervention before formal diagnosis.
- **Tertiary prevention (complication avoidance):** timely cleft repair to prevent speech and feeding morbidity; audiologic surveillance (middle-ear disease in cleft palate); seizure control; proactive ASD/ADHD assessment (the 2022 paper's practical message is that these are under-recognized in this disorder).
- **Immunization / public-health / environmental interventions:** not applicable. (General periconceptional folic acid is population cleft-prevention advice; it has no PHF8-specific evidence base.)
- **Prophylaxis:** none.

---

## 14. Other Species / Natural Disease

### 14.1 Orthologs and taxonomy

| Species | NCBI Taxon | Gene | Notes |
|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | PHF8 (NCBI Gene 23133) | Xp11.22 |
| *Mus musculus* | NCBITaxon:10090 | **Phf8, MGI:2444341**, X chromosome ⚠ | "strong expression of the mouse orthologue Phf8 in embryonic and adult brain structures" ✅ (Laumonnier 2005) |
| *Danio rerio* | NCBITaxon:7955 | phf8 | Morphant brain/jaw phenotype (Qi 2010) ✅ |
| *Caenorhabditis elegans* | NCBITaxon:6239 | **F29B9.2 / jmjd-1.2** | Catalytically conserved H3K9me2/me1 demethylase; neuronal expression; locomotion defect ✅ |
| *Rattus norvegicus* | NCBITaxon:10116 | Phf8 | Primary oligodendroglial cultures (Kremp 2024) ✅ |
| Teleost (mangrove rivulus) | — | Phf8 among 25 Kdm orthologues | Comparative Kdm family survey (PMID:30458291) ⚠ |

Conservation quote (Kleine-Kohlbrecher 2010, cached full text) ✅:
> "Two closely related homologs are present in C. elegans showing conservation of the overall domain structure and of the primary amino acid sequence in the PHD and JmjC domains, indicating an evolutionary conserved role for these proteins."

### 14.2 Naturally occurring disease in other species

❌ **No naturally occurring PHF8-related disease is recorded in OMIA or the veterinary literature** (no companion-animal or livestock PHF8 disorder was found). No breed associations; **no VBO identifiers apply**. Veterinary relevance: none.

### 14.3 Comparative biology

The **enzymatic function is deeply conserved** (worm→human), and so is the **neuronal requirement**: the *C. elegans* homolog is "highly expressed in neurons, and mutant animals show impaired locomotion" ✅, zebrafish morphants show brain-cell apoptosis and jaw defects ✅, and mice show hippocampal LTP/memory deficits ✅ (in one line). The **craniofacial arm is conserved from fish to human** (jaw/msxb in zebrafish; cleft lip/palate in humans; "neural crest defects" in mice ✅ per Kremp 2024). The notable **non-conservation** is the mouse craniofacial phenotype: no mouse model reproduces cleft lip/palate (§15.4).

### 14.4 Transmission

Not applicable — non-infectious, non-zoonotic.

---

## 15. Model Organisms

### 15.1 Mouse (*Mus musculus*) — MGI:2444341

Two independently generated **Phf8 knockout** lines, with **discordant cognitive phenotypes** — this is the central caveat of the mouse literature:

| Line | Key findings | Citation |
|---|---|---|
| Chen et al. 2018 (Phf8 KO) | "impaired learning and memory, and impaired hippocampal long-term potentiation (LTP) **without gross morphological defects**"; hippocampal mTOR hyperactivation via RSK1 de-repression; **rapamycin rescues LTP and cognition** ✅ | PMID:29317619 |
| Walsh et al. 2017 (Phf8 KO) | "Phf8 deficient mice **neither display obvious developmental defects nor signs of cognitive impairment**. However, we report a striking resiliency to stress-induced anxiety- and depression-like behaviour"; serotonin misregulation in PFC; **Htr1a and Htr2a are direct PHF8 targets** ⚠ | PMID:28485378 |

MGI's own summary of the two alleles ⚠: one null allele → impaired learning/memory and impaired hippocampal LTP; another null allele → resiliency to depression-like behavior and decreased anxiety.

Mouse embryonic work (2026) adds a developmental phenotype: PHF8 deficiency **halted neurogenesis and brain development in mouse embryos** ⚠ (PMID:41714361) — potentially reconciling the adult-behavior discordance by shifting attention to embryonic stages and to background/allele differences.

**Available model types:** targeted knockouts (≥2 independent lines) ✅; conditional/humanized/knock-in models — ❌ none reported. IMPC data for Phf8 ❌ not retrievable this session (fetch attempt returned the wrong gene page — do not rely on it).

### 15.2 Zebrafish (*Danio rerio*)

The best craniofacial model. Qi et al. 2010 ✅: phf8 knockdown → **apoptosis/reduced cell survival in the brain and defective jaw development**, mediated at least in part by direct regulation of **msxb (MSX1)**; catalytically dead PHF8 fails to rescue, tying the phenotype to demethylase activity. A separate zebrafish study extends the sensory phenotype: He et al. 2020 (PMID:33330448) ⚠ — "PHF8 knockdown significantly disrupted the development of the posterior lateral line system" and caused "severe malformation of the semicircular canal and otoliths." (Inner-ear involvement has **not** been described in humans — treat as model-only.)

### 15.3 Invertebrate and cellular models

- ***C. elegans*** — F29B9.2/jmjd-1.2: neuronal expression, impaired locomotion, global H3K9me2/H3K27me2 increase in mutants ✅. Also the vehicle for the GenX toxicology study ⚠.
- **P19 mouse embryonal carcinoma cells** — RA-induced neuronal differentiation assay; PHF8 knockdown impairs it, WT (but not F279S) rescues/drives differentiation ✅ (Qiu 2010). A 2024 follow-up: PMID:38463639 ⚠.
- **Primary rodent oligodendroglial cultures + oligodendroglial cell lines** ✅ (Kremp 2024).
- **Mouse astrocyte cultures** ✅ (Iacobucci 2021).
- **Human iPSC-derived oligodendrocytes** — notably, "generation of human oligodendrocytes from induced pluripotent stem cells did not require PHF8 in a system that relies on forced expression of Olig2" ✅ (Kremp 2024) — a clean epistasis result placing Olig2 downstream.
- **HeLa / U2OS / HEK** — biochemistry, ChIP-seq, localization ✅.
- **Patient-derived iPSC or organoid models:** ❌ **none published.** Given the 2026 neurogenesis/serine finding, a patient-iPSC cortical organoid is the obvious next model and a strong `proposed_experiments` entry.

### 15.4 Phenotype recapitulation and limitations — curate as `HUMAN_MODEL_MISMATCH`

This disorder is a textbook case for dismech's `HUMAN_MODEL_MISMATCH` discussion kind (evidence exists in models but translational validity is the open question):

1. **No mouse model reproduces the human clefting phenotype.** Both published Phf8 KO lines are reported without craniofacial malformation ("neither display obvious developmental defects"; "without gross morphological defects"). The cleft phenotype is recapitulated only in **zebrafish jaw** development. Mechanistic implication: species differences in redundancy (PHF2/KDM7A may compensate in mouse) or in the MSX1-dependence of lip/palate fusion.
2. **The two mouse KO lines disagree about cognition** — one shows impaired learning/memory + LTP deficits, the other shows no cognitive impairment. Any KB claim that "Phf8 KO mice model the ID phenotype" must be qualified with both citations.
3. **The mouse behavioral phenotype that *is* robust (stress resilience / altered serotonin signaling) has no reported human counterpart** — no depression/anxiety-resilience phenotype has been described in PHF8-XLID patients. This is a genuinely testable, unaddressed clinical question.
4. **The rapamycin rescue is single-line, mouse-only** and rests on the line whose phenotype the other lab did not replicate.

Suggested discussion entries:
```yaml
discussions:
- kind: HUMAN_MODEL_MISMATCH
  attaches_to: "pathophysiology#Reduced MSX1 Expression in Cranial Neural Crest"
  prompt: >-
    Why do Phf8-null mice fail to develop cleft lip/palate when human PHF8
    loss-of-function causes orofacial clefting and zebrafish phf8 knockdown
    causes jaw malformation?
  rationale: >-
    Both published Phf8 knockout mouse lines are reported without craniofacial
    malformation, while the craniofacial arm of the mechanism rests on zebrafish
    msxb data. Possible paralog compensation (PHF2/KDM7A) or species differences
    in the MSX1 dependence of lip/palate fusion.
- kind: HUMAN_MODEL_MISMATCH
  attaches_to: "pathophysiology#mTOR Hyperactivation via RSK1 De-repression"
  prompt: >-
    Is the mTOR-dependent cognitive phenotype (and its rapamycin rescue) a
    reliable model of human PHF8-XLID, given that a second independent Phf8
    knockout line showed no cognitive impairment?
- kind: KNOWLEDGE_GAP
  attaches_to: "pathophysiology#Loss of PHF8 Histone Demethylase Function"
  prompt: >-
    Does PHF8-XLID have a detectable DNA-methylation episignature that could
    resolve the reported missense variants of uncertain significance?
```

### 15.5 Model resources

MGI (`informatics.jax.org`, Phf8 = MGI:2444341), IMPC/KOMP (status ❌ unverified), ZFIN, WormBase, Alliance of Genome Resources, Cellosaurus (for HeLa/U2OS/P19).

---

## Appendix A — Consolidated citation list

| PMID | Short citation | Evidence type | Cached verbatim in repo? |
|---|---|---|---|
| 10398231 | Siderius et al. 1999, Am J Med Genet — original linkage | HUMAN_CLINICAL | ✅ |
| 16199551 | Laumonnier et al. 2005, J Med Genet — PHF8 identified | HUMAN_CLINICAL | ✅ |
| 17594395 | Abidi et al. 2007, Clin Genet — p.K177X | HUMAN_CLINICAL | ✅ |
| 17661819 | Koivisto et al. 2007, Clin Genet — F279S, Finnish family | HUMAN_CLINICAL | ✅ |
| 18498374 | Qiao et al. 2008, Clin Genet — Xp11.22 microdeletion, ASD | HUMAN_CLINICAL | ❌ (fetch needed) |
| 19843542 | Loenarz et al. 2010, Hum Mol Genet — 2-OG demethylase; F279S dead | IN_VITRO | ✅ (full text) |
| 20208542 | Feng et al. 2010, Nat Struct Mol Biol — rDNA activation | IN_VITRO | ❌ |
| 20346720 | Kleine-Kohlbrecher et al. 2010, Mol Cell — H3K9me2/1; ZNF711 link | IN_VITRO | ✅ (full text) |
| 20421419 | Fortschegger et al. 2010, Mol Cell Biol — RNAPII coactivator | IN_VITRO | ✅ |
| 20548336 | Qiu et al. 2010, Cell Res — RAR coactivator, neuronal differentiation | IN_VITRO | ✅ |
| 20622853 | Qi et al. 2010, Nature — H4K20me1; zebrafish brain/jaw; MSX1 | MODEL_ORGANISM | ✅ (full text) |
| 20622854 | Liu et al. 2010, Nature — H4K20me1, G1-S | IN_VITRO | ❌ |
| 22850744 | Asensio-Juan et al. 2012, NAR — cytoskeleton, neurite outgrowth | IN_VITRO | ✅ |
| 24852203 | Wang et al. 2014, Sci Rep — PHF8/REST co-occupancy | IN_VITRO | ✅ (full text) |
| 25258334 | De Wolf et al. 2014, AJMG A — Xp11.22 deletion, syndromic autism | HUMAN_CLINICAL | ❌ |
| 25923143 | Han et al. 2015, Tissue Eng A — craniofacial bone repair | MODEL_ORGANISM | ❌ |
| 28485378 | Walsh et al. 2017, Nat Commun — Phf8 KO, stress resilience, 5-HT | MODEL_ORGANISM | ❌ |
| 29317619 | Chen et al. 2018, Nat Commun — mTOR/RSK1, rapamycin rescue | MODEL_ORGANISM | ✅ (full text) |
| 31691806 | Poeta et al. 2019, Hum Mol Genet — KDM5C/ARX/ZNF711/PHF8 hub | IN_VITRO | ✅ |
| 32219840 | Huang et al. 2020 — prenatal CMA, Xp11.22 deletion, CL/P | HUMAN_CLINICAL | ❌ |
| 33330448 | He et al. 2020, Front Cell Dev Biol — zebrafish inner ear/PLL | MODEL_ORGANISM | ❌ |
| 34081130 | Iacobucci et al. 2021, Development — astrocyte differentiation | IN_VITRO | ✅ |
| 35469323 | **Sobering et al. 2022, HGG Adv — 16 new individuals; phenotype expansion** | HUMAN_CLINICAL | ✅ |
| 38613395 | Kremp et al. 2024, Glia — Olig2 downstream of Phf8 | IN_VITRO | ✅ |
| 39087553 | Kim et al. 2024, NAR — transcription recovery after DSB | IN_VITRO | ❌ |
| 39311138 | Fan et al. 2024, Epigenomes — PHF8/KDM7B review | review | ❌ |
| 40145966 | Kremp & Wegner 2026, Neural Regen Res — oligodendroglial review | review | ❌ |
| 41709745 | Tan et al. 2026, Haematologica — Znf711-Phf8 in neutrophils | MODEL_ORGANISM | ❌ |
| 41714361 | **Artés/Iacobucci et al. 2026, EMBO Rep — serine biosynthesis, neurogenesis** | IN_VITRO + MODEL_ORGANISM | ❌ |

Also relevant, not fetched: an erratum to Sobering et al. exists (HGG Adv. 2022 Dec 20;4(1):100168) ✅ — **check it before transcribing any variant nomenclature from Table 1.**

---

## Appendix B — Pre-commit checklist for the curator

1. `just fetch-reference PMID:X` for every PMID marked ❌ in Appendix A that you intend to cite, then re-verify each snippet as an exact substring.
2. Re-verify **all** ⚠ quotes (Sobering frequencies, Walsh abstract, Qiao, De Wolf, Huang, He, Kim, Fan, Tan, Artés) against freshly cached abstracts — the frequency table in §3.1 came from a summarizing fetch of the PMC full text, not from a verified cache.
3. Read the **Sobering erratum** (HGG Adv 4(1):100168) before entering variant nomenclature.
4. Run `just validate-terms` on the file — **every** ontology ID in this report marked ⚠ is unverified (OAK and OLS were both unavailable in this session; only GO:0032454, GO:0035575, GO:0060021, HP:0410030, HP:0007018, CL:2000029, CL:0002453, CHEBI:9168 were label-verified).
5. Fill the gnomAD constraint gap (pLI / LOEUF / o-e LoF) manually from gnomAD v4.
6. Pull the ClinGen assertion properly: `just clingen-refresh` + cite the `CGGV:` id rather than the web page, for the "Definitive" classification.
7. Consider adding an `ORPHA:85287` structured-source evidence row via `just structured-rebuild-orphanet --id 85287` for prevalence/definition (orpha.net was unreachable directly).
8. Bind `inheritance_term` to **HP:0001419** with a full `term:` block (the common gap).
9. Do **not** add a `conforms_to` module reference — no existing module fits (see §6.10).
10. Record the clefting frequency discordance (§3.4) in `notes:`, and add the three suggested `discussions` entries (§15.4).
11. Add a history record: `just new-history --kind disorder --slug Siderius_Type_X-Linked_Intellectual_Disability --event CREATE ...`.

---

**Sources (web-retrieved, non-PubMed):**
[OMIM 300263](https://omim.org/entry/300263) · [GTR: Syndromic X-linked intellectual disability Siderius type](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1846055/) · [Orphanet ORPHA:85287](https://www.orpha.net/en/disease/detail/85287) · [GenCC PHF8 submissions](https://search.thegencc.org/submissions/GENCC_000102-HGNC_20672-MONDO_0010286-HP_0001417-GENCC_100001) · [ClinGen conditions: MONDO:0010286](https://search.clinicalgenome.org/kb/conditions/MONDO:0010286) · [ClinVar Miner: PHF8 / Siderius](https://www.clinvarminer.org/variants-by-condition/Syndromic%20X-linked%20intellectual%20disability%20Siderius%20type/gene/PHF8) · [MedlinePlus Genetics: PHF8](https://medlineplus.gov/genetics/gene/phf8/) · [GARD: Siderius type](https://rarediseases.info.nih.gov/diseases/9704/syndromic-x-linked-intellectual-disability-siderius-type) · [MGI Phf8 (MGI:2444341)](https://www.informatics.jax.org/marker/MGI:2444341) · [UniProt Q9UPP1](https://rest.uniprot.org/uniprotkb/Q9UPP1) · [NCBI Gene 23133](https://www.ncbi.nlm.nih.gov/gene/23133) · [HPO annotations, OMIM:300263](https://ontology.jax.org/api/network/annotation/OMIM:300263) · [EBI OLS4](https://www.ebi.ac.uk/ols4) · PubMed/PMC via NCBI E-utilities (PMIDs cited inline; DOIs listed in the cached reference files).