---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T20:57:41.739181'
end_time: '2026-08-01T21:12:40.835696'
duration_seconds: 899.1
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 20
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
  web_search_requests: 17
  num_turns: 55
  total_cost_usd: 3.9409095000000005
  session_id: 38cd7995-eaf6-41fb-acea-e603378ec251
  stop_reason: end_turn
citation_count: 26
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 20
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 20** covering all of the
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

# Comprehensive Research Report: Hypertrophic Cardiomyopathy 20 (CMH20 / NEXN-related HCM)

**Prepared:** 2026-08-01 · **Target MONDO:** MONDO:0013477 · **Category:** Mendelian (nominal)

---

## ⚠️ Executive Summary and Critical Curation Caveat — Read First

**CMH20 is a nominal OMIM phenotype-series entry whose gene–disease validity is contested and has never risen above "Limited."** This is the single most important fact for a knowledge-base entry, and it should shape every downstream claim in the record.

| Assertion | Source | Status |
|---|---|---|
| NEXN – **hypertrophic cardiomyopathy** (MONDO:0005045), AD | ClinGen **Hereditary Cardiovascular Disease GCEP**, curated 2023-03-23 | **LIMITED** |
| NEXN – **dilated cardiomyopathy 1CC** (MONDO:0013147), AD | ClinGen **Dilated Cardiomyopathy GCEP**, curated 2026-03-04 | **STRONG** (upgraded from Moderate/2021) |

The evidence base for CMH20 rests almost entirely on a **single 2010 report of two Han Chinese families** (PMID:20970104). Every subsequent well-powered cohort study has failed to replicate an HCM association:

- **Ingles et al. 2019** (PMID:30681346) — of 33 curated HCM genes, only 8 (24%) were Definitive; NEXN fell in the limited/no-evidence group, and "genes deemed to have limited evidence … were not significantly associated with HCM."
- **ClinGen HCM reappraisal** (PMID:39132495; JACC 2025, doi:10.1016/j.jacc.2024.12.010) — NEXN was among 6 genes that "retained their original classification … 6 limited (KLF10, **NEXN**, OBSCN, PDLIM3, RYR2, TTN)," scoring only 0.5 genetic + 1.0 experimental = 1.5 points.
- **Hermida et al. 2024** (PMID:38059363), 9,516 sequenced index patients — "We also detected NEXN variants in patients with hypertrophic cardiomyopathy and sudden infant death syndrome/idiopathic ventricular fibrillation, **although a causal link could not be established.**"
- **Perotto et al. 2025** (PMID:40680702), the largest NEXN carrier cohort to date (n=60) — "a significant enrichment of NEXN-truncating variants (tvs) was found in the DCM/NDLVC cohort (0.39% vs 0.09% in gnomAD NFE; P = 0.0001), **whereas no association was observed with HCM.**"
- A 2025 state-of-the-art review (PMID:40161564) states flatly that there is "no solid evidence linking it [NEXN] to HCM, and it is consequently not included in HCM panels."

**Curation recommendation:** model CMH20 as a real MONDO/OMIM entity but flag the gene–disease relationship explicitly — e.g. a `discussions` block with `kind: KNOWLEDGE_GAP`, and evidence items carrying `supports: PARTIAL` or `supports: REFUTE` for the replication-failure papers. **Do not curate CMH20 pathophysiology as though it were an established mechanism.** The mechanistically solid, well-replicated NEXN disease is DCM/NDLVC (`Dilated_Cardiomyopathy_1CC`), not HCM.

> **Reference-cache note:** PMIDs 19881492, 20301725, 20970104, 38059363, and 40680702 are already cached in this worktree and their content is quoted verbatim below. **All other PMIDs cited in this report must be fetched with `just fetch-reference PMID:XXXX` and every snippet re-verified with `just validate-references` before it enters YAML.** Quotes sourced from web-fetched abstracts are marked ⚑ and are *leads, not verified snippets*.

---

## 1. Disease Information

### Overview

Hypertrophic cardiomyopathy 20 (CMH20) is the OMIM phenotype-series designation for hypertrophic cardiomyopathy attributed to heterozygous mutation in *NEXN* (nexilin F-actin binding protein), a **Z-disc** rather than a **sarcomeric thick/thin-filament** gene. Conceptually it belongs to the "non-sarcomeric HCM" hypothesis of the late 2000s–early 2010s, in which Z-disc structural genes (*NEXN*, *CSRP3*, *TCAP*, *LDB3*, *MYOZ2*, *ACTN2*, *VCL*) were proposed to account for part of the ~50% of HCM with no myofilament mutation. Of these, only *ACTN2* and *CSRP3* have retained meaningful HCM validity in ClinGen reappraisal; *NEXN* has not.

The clinical phenotype, as described in the founding report, is conventional HCM: asymmetric left ventricular hypertrophy, predominantly septal, without a hemodynamic explanation, with dyspnea, syncope, palpitations, chest pain, and risk of sudden cardiac death.

### Key Identifiers

| Resource | Identifier | Label |
|---|---|---|
| **MONDO** | `MONDO:0013477` | hypertrophic cardiomyopathy 20 |
| **OMIM** (phenotype) | `OMIM:613876` | CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 20; CMH20 |
| **OMIM** (gene) | `OMIM:613121` | NEXILIN F-ACTIN-BINDING PROTEIN; NEXN |
| **DOID** | `DOID:0110326` | — |
| **MedGen** | `462617` | — |
| **UMLS** | `C3151267` | — |
| **GARD** | `GARD:0024932` | — |
| **HGNC** | `hgnc:29557` | NEXN |
| **MANE Select** | `NM_144573.4` | — |
| **Orphanet** (parent) | `ORPHA:217569` | Rare hypertrophic cardiomyopathy (a *group*, not a disease) |
| **ICD-10** | `I42.1` / `I42.2` | Obstructive / other hypertrophic cardiomyopathy |
| **ICD-11** | `BC43.00` | Hypertrophic cardiomyopathy |
| **MeSH** | `D002312` | Cardiomyopathy, Hypertrophic |

MONDO parent axis: `is_a MONDO:0024573` (familial hypertrophic cardiomyopathy); `intersection_of MONDO:0005045` + `RO:0004003 HGNC:29557`.

### Synonyms

CMH20 · Cardiomyopathy, familial hypertrophic, 20 · Cardiomyopathy, hypertrophic, 20 · Hypertrophic cardiomyopathy type 20 · NEXN hypertrophic cardiomyopathy · Hypertrophic cardiomyopathy caused by mutation in NEXN.

### Information Provenance

Almost entirely **aggregated disease-level** (OMIM/MONDO/MedGen ontology records propagating a single 2010 primary report). The only genuinely patient-level datasets are the three multicenter cohorts — Hermida 2024 (French national sequencing network, n=9,516 index cases; PMID:38059363), Perotto 2025 (12 referral centers, n=60 carriers; PMID:40680702), and the original two-family pedigree study (PMID:20970104). **No EHR-derived or registry-derived CMH20-specific cohort exists.**

---

## 2. Etiology

### Disease Causal Factors

**Proposed (Limited-validity) primary cause:** heterozygous missense variants in *NEXN* at 1p31.1 (GRCh38: chr1:77,888,624–77,943,895), inherited in an autosomal dominant pattern. The proposed molecular lesion is disruption of nexilin's F-actin/α-actin binding at the cardiac Z-disc, destabilizing the Z-disc under contractile mechanical load.

Wang et al. framed the rationale (PMID:20970104, cached):

> "Nexilin, encoded by NEXN, is a cardiac Z-disc protein recently identified as a crucial protein that functions to protect cardiac Z-discs from forces generated within the sarcomere."

> "In as many as 50% of HCM cases, the genetic cause remains unknown, suggesting that more genes may be involved."

**Countervailing evidence:** the more robustly supported causal role of *NEXN* is in DCM/NDLVC via **truncating** variants, and in a lethal fetal cardiomyopathy via **biallelic** loss of function. The HCM claim rests on two missense variants, one of which (p.Arg279Cys) is now population-frequent.

### Risk Factors

**Genetic**
- The two originally reported variants: **c.391C>G p.(Gln131Glu)** (exon 5, actin-binding domain 1) and **c.835C>T p.(Arg279Cys)** (exon 8, coiled-coil domain). ⚑ p.(Arg279Cys) has ~141 occurrences in gnomAD and is now widely regarded as too common to be pathogenic — reclassified toward VUS/benign.
- Family history of HCM or SCD — in Family A the proband's mother died suddenly at 38; in Family B the grandmother died suddenly at ~40 (⚑ PMID:20970104 full text).
- **Digenic/oligogenic burden:** Hermida 2024 found 2 of 31 NEXN carriers had *double* NEXN variants, and these had "severe and early onset phenotypes" (PMID:38059363, cached). This is a plausible dose-dependence signal.
- Genetic background/modifier burden (common-variant polygenic score for LV wall thickness) is an established modifier in HCM generally, but has **not** been studied in CMH20.

**Environmental / demographic**
- Male sex (general HCM: males over-represented in referral cohorts; Hermida cohort 16/29 male).
- Age — LVH is typically absent in childhood and manifests through adolescence into mid-adulthood.
- **Intense/competitive exercise** — a classical trigger consideration in HCM; the 2024 AHA/ACC guideline (PMID:38718139) has substantially liberalized exercise restriction relative to prior guidance.
- Systemic hypertension and obesity as phenotype amplifiers (general HCM; not CMH20-specific).
- **Mechanical strain is mechanistically specific here:** Hassel et al. showed "Increasing mechanical strain aggravated Z-disk damage in nexilin-deficient skeletal muscle, implying a unique role of nexilin in protecting Z-disks from mechanical trauma" (PMID:19881492, cached). This is the strongest available biological rationale for a load/exercise gene–environment interaction in NEXN disease.

### Protective Factors

No CMH20-specific protective genetic or environmental factor has been reported. **Not available for this disease.** By extension from general HCM: avoidance of dehydration/vasodilators in obstructive physiology; weight management; blood-pressure control.

### Gene–Environment Interactions

The only mechanistically grounded GxE hypothesis is **nexilin haploinsufficiency/dysfunction × mechanical afterload**: a partially destabilized Z-disc is predicted to fail preferentially under high wall stress. This is supported by model-organism data (PMID:19881492) but has **never been tested clinically in NEXN carriers**. This is a genuine, curatable knowledge gap — an appropriate `discussions` entry with `kind: KNOWLEDGE_GAP` and `proposed_experiments` (e.g. exercise-stress CMR in NEXN carriers; strain-conditioned iPSC-CM engineered heart tissue).

---

## 3. Phenotypes

### Phenotype Table with HPO Terms (all IDs OAK-verified against `sqlite:obo:hp`)

| Phenotype | HPO ID | Label | Type | Onset | Course | Frequency | Notes |
|---|---|---|---|---|---|---|---|
| Hypertrophic cardiomyopathy | `HP:0001639` | Hypertrophic cardiomyopathy | Clinical sign / imaging | Adolescent–adult | Progressive | Defining | Core CMH20 feature |
| Left ventricular hypertrophy | `HP:0001712` | Left ventricular hypertrophy | Imaging | Adolescent–adult | Progressive | Defining | Wall thickness 14–22 mm in reported families |
| Left ventricular outflow tract obstruction | `HP:0032092` | Left ventricular outflow tract obstruction | Physiology | Adult | Variable | Not reported in CMH20 probands | Family A proband explicitly **non**-obstructive |
| Atrial fibrillation | `HP:0005110` | Atrial fibrillation | ECG | Adult | Recurrent→persistent | Listed in MedGen/OMIM clinical synopsis | |
| Reduced left ventricular ejection fraction | `HP:0012664` | Reduced left ventricular ejection fraction | Imaging | Adult | Progressive | Listed in MedGen/OMIM clinical synopsis | Suggests burnt-out/overlap phenotype |
| Sudden cardiac death | `HP:0001645` | Sudden cardiac death | Outcome | Adult | Episodic/terminal | 2 pedigree deaths (ages 38, 40) ⚑ | |
| Syncope | `HP:0001279` | Syncope | Symptom | Adolescent–adult | Episodic | Reported for HCM generally | |
| Dyspnea | `HP:0002094` | Dyspnea | Symptom | Adult | Progressive | Common in HCM | Exertional |
| Chest pain | `HP:0100749` | Chest pain | Symptom | Adult | Episodic | Common in HCM | |
| Palpitations | `HP:0001962` | Palpitations | Symptom | Adult | Episodic | Common in HCM | |
| Ventricular arrhythmia | `HP:0004308` | Ventricular arrhythmia | ECG | Adult | Episodic | See Perotto (25% MVA in NEXN-DCM) | |
| Ventricular tachycardia | `HP:0004756` | Ventricular tachycardia | ECG | Adult | Episodic | | |
| Myocardial fibrosis | `HP:0001685` | Myocardial fibrosis | Imaging/histology | Adult | Progressive | **64%** in NEXN-tv DCM/NDLVC (PMID:40680702) | LGE on CMR |
| Myofiber disarray | `HP:0031318` | Myofiber disarray | Histopathology | — | — | HCM hallmark | |
| Left ventricular diastolic dysfunction | `HP:0025168` | Left ventricular diastolic dysfunction | Imaging | Adult | Progressive | HCM hallmark | |
| Congestive heart failure | `HP:0001635` | Congestive heart failure | Clinical | Adult | Progressive | Uncommon in NEXN-CMP (71% NYHA I) | |
| Cardiac arrest | `HP:0001695` | Cardiac arrest | Outcome | Adult | Episodic | IVF cases in Hermida cohort | |

**Adjacent NEXN phenotypes (for cross-linking, not CMH20 proper):** Dilated cardiomyopathy `HP:0001644`; Endocardial fibroelastosis `HP:0001706`; Cardiomegaly `HP:0001640`.

### Phenotype Characteristics

**Age of onset.** Adolescent to mid-adult. In the founding pedigrees the youngest carriers were 12 and 16 years old; probands were 37 and 45. Across the broader NEXN cohort, median age at diagnosis was **32.0 years (IQR 26.0–49.0)** (PMID:38059363, cached) and 45 years (IQR 36–55) for NEXN-tv DCM/NDLVC (PMID:40680702, cached). HPO onset: `Adult onset` / `Juvenile onset`.

**Severity.** Variable. Reported wall thicknesses spanned 14–21 mm (Family A) and 17–22 mm (Family B) ⚑ — i.e. mild-to-marked, with at least one proband reaching the ≥20 mm threshold that itself constitutes an SCD risk marker in the 2024 guideline.

**Progression.** Progressive hypertrophy through adolescence/early adulthood, then plateau; a minority progress to systolic dysfunction ("burnt-out" HCM), consistent with the reduced-LVEF entry in the OMIM clinical synopsis.

**Frequency among affected individuals.** **Explicitly not quantifiable for CMH20.** With ~7 reported HCM carriers worldwide with segregation data plus 3 non-segregating probands (Hermida), no phenotype frequency band can be honestly assigned. Per the dismech frequency-evidence SOP, **omit `frequency:` rather than fabricate**. Where a frequency IS defensible, cite the NEXN-CMP cohort figures explicitly and label them as *NEXN cardiomyopathy broadly*, not CMH20:
- Myocardial fibrosis **64%**; ICD implantation **53%**; malignant ventricular arrhythmias **25%**; NYHA I **71%** (all PMID:40680702, DCM/NDLVC arm).

**Quality of life.** No CMH20-specific QoL data. General HCM QoL is measured with the **KCCQ** (Kansas City Cardiomyopathy Questionnaire) and **HCMSQ** (HCM Symptom Questionnaire); EQ-5D and SF-36 are used secondarily. EXPLORER-HCM established KCCQ and pVO₂ improvement with mavacamten. **Not available for CMH20 specifically.**

---

## 4. Genetic / Molecular Information

### Causal Gene

**NEXN** — nexilin F-actin binding protein
- HGNC: `hgnc:29557` · OMIM gene: `613121` · NCBI Gene: `91624` · Ensembl: `ENSG00000162614` · UniProt: `Q0ZGT2` (NEXN_HUMAN)
- Location: **1p31.1**, GRCh38 chr1:77,888,624–77,943,895
- MANE Select transcript: **NM_144573.4**
- Structure: **13 exons**, encoding two N-terminal actin-binding domains (ABD), a central coiled-coil domain (CC), and a C-terminal Ig-superfamily/IGcam domain
- Originally identified in 1998 as a novel filamentous-actin-binding protein; re-identified as a cardiac Z-disc protein in 2009 (PMID:19881492)

### Pathogenic Variants — CMH20 (the two founding variants)

| Variant (NM_144573.4) | Protein | Exon | Domain | Type | Original claim | Current status |
|---|---|---|---|---|---|---|
| c.391C>G | p.(Gln131Glu) / p.Q131E | 5 | Actin-binding domain 1 | Missense | Segregated in Family A; absent from 384 control chromosomes | VUS; **strongest functional evidence** — abolishes F-actin binding |
| c.835C>T | p.(Arg279Cys) / p.R279C | 8 | Coiled-coil | Missense | Segregated in Family B; absent from 384 control chromosomes | ⚑ **Likely benign** — ~141 gnomAD occurrences; "too high frequency to be considered pathogenic" |

Verbatim from the founding paper (PMID:20970104, cached — safe to quote):

> "Two missense mutations, c.391C>G (p.Q131E) and c.835C>T (p.R279C), were identified in exons 5 and 8 of NEXN, respectively, in two probands. Each of the two mutations segregated with the HCM phenotype in the family and was absent in 384 control chromosomes."

> "In silico analysis revealed that both of the mutations affect highly conserved amino acid residues, which are predicted to be functionally deleterious."

The 384-control-chromosome standard was adequate in 2010 but is **radically underpowered** by current ACMG/AMP criteria — this is precisely why p.R279C survived initial filtering and later failed.

**Functional consequences.** p.Q131E is a **loss of actin binding with a probable dominant-negative ("poison peptide") component** — the mutant protein is expressed, mislocalizes into cytoplasmic aggregates, and fails to bind its ligand:

> "Cellular transfection studies showed that the two mutations resulted in local accumulations of nexilin and that the expressed fragment of actin-binding domain containing p.Q131E completely lost the ability to bind F-actin in C2C12 cells. Coimmunoprecipitation assay indicated that the p.Q131E mutation decreased the binding of full-length NEXN to α-actin and abolished the interaction between the fragment of actin-binding domain and α-actin." (PMID:20970104, cached; `evidence_source: IN_VITRO`)

Dominant-negative action for NEXN missense alleles is independently supported in vivo by the zebrafish rescue/overexpression experiments of Hassel et al. (PMID:19881492, cached; `evidence_source: MODEL_ORGANISM`):

> "Expression in zebrafish of nexilin proteins encoded by NEXN mutant alleles induced Z-disk damage and heart failure, demonstrating a dominant-negative effect and confirming the disease-causing nature of these mutations."

Note carefully: **Hassel's variants were DCM variants, not the HCM variants.** Do not transfer that quote to a CMH20 mechanism node without stating the DCM provenance.

### NEXN Variant Landscape Beyond CMH20 (for contrast and cross-linking)

- **DCM 1CC (`OMIM:613122`, `MONDO:0013147`)** — AD, ClinGen **Strong** (2026-03-04). Truncating variants enriched: **0.39% in DCM/NDLVC vs 0.09% in gnomAD NFE, P = 0.0001** (PMID:40680702, cached).
- **p.(Gly650del)** — a recurrent/founder-like German DCM allele; ⚑ 6/994 German DCM patients vs 168/1,613,646 population controls, **OR ≈ 57.9**, late-onset (mean 51 y) (PMID:40161564 review).
- **Biallelic loss of function → lethal fetal cardiomyopathy with cardiomegaly + endocardial fibroelastosis** — Johansson et al. 2022, Swedish family with three consecutive intrauterine fetal deaths, homozygous NEXN (PMID:35166435). Two further homozygous infants with novel alleles **c.1156dup p.(Met386fs)** and **c.1579_1584del p.(Glu527_Glu528del)** had, atypically, a *favorable* course (PMID:39183344, Ital J Pediatr 2024).
- **ClinVar** — ⚑ ≥31 NEXN variants classified P/LP as of April 2024, "most being loss-of-function variants" (PMID:40161564). The P/LP mass is LoF/DCM, **not** missense/HCM — a decisive asymmetry for the CMH20 record.

### Population Constraint (gnomAD v4.0, via ClinGen)

| Metric | Value | Interpretation |
|---|---|---|
| **pLI** | **0** | Not haploinsufficiency-intolerant by pLI |
| **LOEUF** | **0.88** | Only mildly LoF-constrained (v2 value reported as 0.78) |
| **%HI** | 14.3 | Low predicted haploinsufficiency |

This constraint profile is **discordant with a highly penetrant dominant HCM gene** and is corroborating evidence for the Limited classification. It is compatible with the observed reality: heterozygous LoF gives mild, incompletely penetrant DCM/NDLVC; biallelic LoF is lethal.

### Modifier Genes

None established. Candidate mechanism: NEXN's partners **RYR2** and **JPH2** (junctional membrane complex) and Z-disc partners are plausible modifiers, but no modifier study exists. **Not available.**

### Epigenetics

No CMH20-specific DNA-methylation, histone-modification, or chromatin data. Of note, ⚑ NEXN expression in smooth muscle is regulated by **myocardin-family coactivators and YAP** (Sci Rep 2018, doi:10.1038/s41598-018-31328-2) — a transcriptional-regulation lead, not an epigenetic disease mechanism. **Not available for CMH20.**

### Chromosomal Abnormalities

No recurrent CNV, translocation, or aneuploidy associated with CMH20. ClinGen reports **0 dosage-sensitivity classifications** for NEXN (neither haploinsufficiency nor triplosensitivity curated). Whole-gene deletions at 1p31.1 are not an established CMH20 mechanism. **Not applicable.**

---

## 5. Environmental Information

- **Environmental factors:** none causally implicated. CMH20 is a monogenic hypothesis; no toxin, radiation, pollutant, or occupational exposure has been linked. **Not applicable.**
- **Lifestyle factors:** high-intensity isometric/competitive exercise is the classical HCM consideration and is mechanistically attractive here given nexilin's role in mechanical protection (PMID:19881492), but is **unstudied in NEXN carriers**. Alcohol, obesity, and hypertension act as general HCM phenotype amplifiers.
- **Infectious agents:** none. **Not applicable.**

---

## 6. Mechanism / Pathophysiology

### The Proposed Causal Chain (CMH20 — hypothesis-grade)

```
[MOLECULAR] NEXN missense variant in actin-binding domain (p.Q131E)
    ↓ loss of F-actin / α-actin binding + cytoplasmic mislocalization (dominant-negative)
[MOLECULAR] Impaired nexilin–actin anchoring at the cardiac Z-disc
    ↓
[CELLULAR] Z-disc destabilization under sarcomere-generated mechanical force
    ↓
[CELLULAR] Disturbed mechanotransduction / myofibril and sarcomere disorganization
    ↓
[CELLULAR] Cardiomyocyte hypertrophic response
    ↓
[TISSUE]   Myocyte hypertrophy + myofiber disarray + interstitial fibrosis
    ↓
[ORGAN]    Asymmetric septal LV hypertrophy; diastolic dysfunction; arrhythmogenic substrate
    ↓
[ORGANISM] Dyspnea, chest pain, syncope, palpitations; AF; ventricular arrhythmia; SCD
```

**Epistemic status of each step.** Steps 1–2 are supported by direct in-vitro evidence (PMID:20970104, IN_VITRO). Step 3 is supported in model organisms but from *DCM* alleles (PMID:19881492, MODEL_ORGANISM). Steps 4–6 are **inferred by analogy to sarcomeric HCM and have never been demonstrated for a NEXN allele in human or animal tissue.** No animal model has ever reproduced a hypertrophic phenotype from a NEXN lesion — every one produces **dilated** cardiomyopathy (see §15). This is the mechanistic heart of the Limited classification and should be recorded as a `HUMAN_MODEL_MISMATCH` discussion, not a `KNOWLEDGE_GAP`: model evidence exists in abundance, but it points to the *wrong phenotype*.

### The Well-Supported NEXN Mechanism (DCM arm — for the module/comorbidity cross-link)

Nexilin is now understood as far more than a Z-disc actin anchor. Liu et al. (Circulation 2019; PMID:30982350) established it as a **junctional membrane complex (JMC)** component:

> "Membrane contact sites are fundamental for transmission and translation of signals in multicellular organisms." ⚑

⚑ Loss of *Nexn* produced progressive DCM; NEXN interacted with junctional sarcoplasmic-reticulum proteins and was essential for calcium transients and the *initiation* of T-tubule formation. Spinozzi et al. (Circ Heart Fail 2020; PMID:32635769) extended this to the adult heart:

> "NEXN was essential for optimal contraction and calcium handling, and was required for maintenance of T-tubule network organization (transverse tubular component in icKO reduced by 40% with respect to CTRLs, p<0.05)." ⚑

> "Results here reported revealed NEXN to be a pivotal component of adult junctional membrane complexes required for maintenance of transverse-axial tubular architecture." ⚑

⚑ Per the 2025 review (PMID:40161564), NEXN interacts with **ryanodine receptor 2 (RYR2)** and **junctophilin 2 (JPH2)**, both "essential for T-tubule formation and calcium homeostasis."

**Curation implication:** if a NEXN pathophysiology graph is built, the defensible mechanism is **Z-disc + JMC/T-tubule + excitation–contraction-coupling failure → contractile deficit → chamber dilation and arrhythmogenesis**, which conforms to `cardiomyopathy_maladaptive_remodeling` (dilated arm), *not* to a hypertrophic pathway. The high fibrosis rate (64%) and arrhythmia-out-of-proportion-to-dysfunction profile also make `fibrotic_response` and `cardiac_ion_channel_repolarization` (arrhythmogenic-substrate node) plausible conformance targets.

### Molecular Pathways

- **Sarcomere/Z-disc structural pathway** — actin cytoskeleton anchoring; no canonical named signaling cascade (Wnt/MAPK/mTOR) has been implicated in NEXN disease.
- **Z-disc mechanosensing** — the Z-disc is "postulated to play a key role in both cell signaling and sarcomere assembly" and "may act as a mechanosensor that converts myosin-generated force into the intracellular signaling that drives hypertrophy." ⚑ (Front Physiol 2023, doi:10.3389/fphys.2023.1143858). In sarcomeric HCM the downstream effectors are calcineurin–NFAT, MEF2, and CaMKII; **whether NEXN engages these is unknown.**
- **Excitation–contraction coupling / calcium cycling** — RyR2, SERCA2, JPH2 dysregulation demonstrated in Nexn-null adult mice ⚑.
- KEGG: hsa04260 (Cardiac muscle contraction), hsa05410 (Hypertrophic cardiomyopathy), hsa04261 (Adrenergic signaling in cardiomyocytes). Reactome: R-HSA-390522 (Striated muscle contraction).

### Cellular Processes and GO Terms (all OAK-verified against `sqlite:obo:go`)

| GO ID | Label | Aspect | Relevance |
|---|---|---|---|
| `GO:0030018` | Z disc | CC | **Primary nexilin localization** |
| `GO:0030315` | T-tubule | CC | JMC / TATS role |
| `GO:0016529` | sarcoplasmic reticulum | CC | jSR interaction |
| `GO:0014801` | longitudinal sarcoplasmic reticulum | CC | TATS axial component |
| `GO:0051015` | actin filament binding | MF | **Lost by p.Q131E** |
| `GO:0045214` | sarcomere organization | BP | Z-disc integrity |
| `GO:0030239` | myofibril assembly | BP | |
| `GO:0060048` | cardiac muscle contraction | BP | |
| `GO:0055117` | regulation of cardiac muscle contraction | BP | |
| `GO:0070296` | sarcoplasmic reticulum calcium ion transport | BP | Ca²⁺ handling defect |
| `GO:0086001` | cardiac muscle cell action potential | BP | Arrhythmogenesis |
| `GO:0003300` | cardiac muscle hypertrophy | BP | **Proposed CMH20 output — unvalidated for NEXN** |
| `GO:0055008` | cardiac muscle tissue morphogenesis | BP | Developmental arm |
| `GO:0003009` | skeletal muscle contraction | BP | Skeletal Z-disc arm (PMID:19881492) |

### Protein Dysfunction

Nexilin (Q0ZGT2, 675 aa canonical) — two N-terminal ABDs, coiled-coil, C-terminal IGcam. p.Q131E lies in ABD1 and destroys F-actin binding outright; the full-length mutant still binds α-actin, but weakly. The **mislocalization into cytoplasmic aggregates** is the key gain-of-toxicity feature distinguishing this from simple haploinsufficiency. No experimental structure of the nexilin ABD in complex with actin is deposited in the PDB; AlphaFold model **AF-Q0ZGT2-F1** is available. No misfolding/amyloid mechanism.

### Metabolic Changes, Immune Involvement, Biochemical Abnormalities

- **Metabolic:** no CMH20-specific metabolomic data. General HCM shows impaired myocardial energetics (reduced PCr/ATP by ³¹P-MRS) and increased ATP cost of tension — mechanistically attributed to myosin, not Z-disc, lesions. **Not available for CMH20.**
- **Immune:** no autoimmune or immunodeficiency component. Fibrosis in NEXN-CMP implies secondary reparative/inflammatory signaling but no primary immune mechanism. **Not applicable.**
- **Biochemical:** the defect is a protein–protein interaction failure (nexilin↔F-actin/α-actin), not an enzyme deficiency, receptor defect, or ion-channel mutation. Secondary Ca²⁺-handling protein dysregulation (RyR2, SERCA2) is documented in mouse ⚑.

### Tissue Damage Mechanisms

Mechanical Z-disc failure under contractile load → myocyte injury → **replacement and interstitial fibrosis** (myocardial fibrosis in 64% of NEXN-tv carriers by CMR-LGE, PMID:40680702) → arrhythmogenic scar substrate. In the biallelic/null setting, **endocardial fibroelastosis** is the signature lesion (PMID:35166435; PMID:26659360).

### Molecular Profiling

- **Transcriptomics:** RNA-seq performed on Nexn-KO mouse hearts (PMID:30982350) ⚑ — no human CMH20 transcriptomic dataset. GTEx confirms NEXN expression is highest in heart and skeletal muscle.
- **Proteomics:** mass spectrometry defined the NEXN interactome in mouse heart (PMID:30982350) ⚑, identifying junctional SR partners. No human CMH20 proteomic study.
- **Metabolomics / lipidomics:** **Not available.**
- **Single-cell / spatial transcriptomics / multi-omics / CRISPR screens:** no NEXN- or CMH20-specific studies. **Not available.** (Note: the CRISPR work cited below is targeted gene editing in zebrafish, not a functional-genomics screen.)

---

## 7. Anatomical Structures Affected

### Organ Level

- **Primary:** heart (`UBERON:0000948`) — specifically the **left ventricle** (`UBERON:0002084`) and **interventricular septum** (`UBERON:0002094`), with asymmetric septal predominance.
- **Secondary:** left atrium (dilation → AF); lungs (pulmonary congestion); brain (cardioembolic stroke from AF); systemic circulation (low-output states).
- **Body system:** cardiovascular. Skeletal muscle is a *potential* subclinical target given nexilin's skeletal Z-disc role under strain (PMID:19881492) — but **no human skeletal myopathy has been reported in NEXN carriers.**

### Tissue and Cell Level

| Term | ID | Role |
|---|---|---|
| Myocardium | `UBERON:0002349` | Site of hypertrophy, disarray, fibrosis |
| Left ventricle myocardium | `UBERON:0006566` | Predominant site |
| Cardiac muscle tissue | `UBERON:0001133` | |
| Cardiac muscle cell | `CL:0000746` | **Primary affected cell type** |
| Regular cardiac myocyte | `CL:0002098` | Working myocardium |
| Fibroblast of cardiac tissue | `CL:0002548` | Fibrotic remodeling effector |
| Fibroblast | `CL:0000057` | Generic parent |

Endocardium (`UBERON:0002165`) is the target in the biallelic/EFE phenotype, not CMH20.

### Subcellular Level

Z disc (`GO:0030018`) — primary; T-tubule (`GO:0030315`); sarcoplasmic reticulum (`GO:0016529`); longitudinal SR (`GO:0014801`); junctional membrane complex (dyad — no clean GO CC term; nearest is `GO:0030315` + `GO:0016529`); actin cytoskeleton (`GO:0015629`).

### Localization and Lateralization

**Bilateral in the sense of being a whole-heart genetic lesion, but phenotypically left-dominant and regionally asymmetric.** The hallmark is asymmetric septal hypertrophy — a *within-organ* asymmetry, not a body-lateralization phenomenon. Right ventricular involvement (`HP:0011663`) is not a reported CMH20 feature. The NEXN-tv DCM/NDLVC phenotype is likewise left-sided (mild LV dilation, indexed EDV 69 mL, LVEF 44%).

---

## 8. Temporal Development

**Onset.** Adolescent-to-adult; insidious. Youngest reported carriers with detectable hypertrophy were 12 and 16 ⚑. Median age at diagnosis across NEXN carriers: **32.0 years (IQR 26.0–49.0)** (PMID:38059363, cached). HPO onset: `Juvenile onset` (HP:0003621) / `Adult onset` (HP:0003581). Note the sharp contrast with **biallelic** NEXN disease, which is **fetal/prenatal onset** (PMID:35166435, PMID:39183344) — a striking allelic-dose–onset gradient worth curating explicitly.

**Progression.**
- *Early:* subclinical/genotype-positive–phenotype-negative; normal wall thickness; possible ECG abnormalities preceding hypertrophy.
- *Intermediate:* established LVH with diastolic dysfunction; exertional symptoms; AF risk rises with LA dilation.
- *Advanced:* progressive fibrosis; arrhythmic burden; in a minority, systolic decline ("burnt-out" phase → reduced LVEF, the phenotype captured in the OMIM synopsis).
- *End-stage:* refractory heart failure requiring transplant, or SCD.

**Rate.** Slow and variable; hypertrophy typically stabilizes after adolescent growth. In the NEXN-tv DCM/NDLVC arm the striking feature is **arrhythmia out of proportion to dysfunction**: "Compared with TTN-CMP, NEXN-CMP exhibited earlier and more frequent MVAs at higher ejection fractions" (PMID:40680702, cached). If this arrhythmia-forward signature generalizes to NEXN-HCM, it would carry real management weight.

**Course.** Chronic, lifelong, progressive with episodic arrhythmic events. Median follow-up in the cohorts: 45 months (Perotto) and 6.0 years (Hermida).

**Remission.** No spontaneous remission of hypertrophy. Treatment-induced reverse remodeling is achievable — in the NEXN **DCM** arm, LVEF "improved with treatment in 13 (61.9%)" of 21 patients (PMID:38059363, cached), a genuinely favorable and quotable finding. Mavacamten produces reversible reduction in LV mass and LVOT gradient in obstructive HCM.

**Critical periods.** Adolescence through the third decade — the window of hypertrophy development, hence the anchor for cascade-screening intervals. A second window is the peri-diagnostic period for SCD risk stratification.

---

## 9. Inheritance and Population

### Epidemiology

**CMH20-specific prevalence is not established and should be recorded as `UNKNOWN` / `CASES_IN_LITERATURE`.** Fewer than ~10 individuals have ever been reported with a segregating NEXN-HCM variant.

The only defensible numerator/denominator figures:

| Measure | Value | Population | Source |
|---|---|---|---|
| NEXN putative-pathogenic variant frequency **among HCM probands** | **0.14%** (3/~2,100) | French national sequencing cohort | PMID:38059363 (cached) |
| NEXN putative-pathogenic variant frequency **among DCM probands** | **0.33%** (21/~6,400) | Same | PMID:38059363 (cached) |
| NEXN-truncating variants in DCM/NDLVC vs population | **0.39% vs 0.09%**, P = 0.0001 | Multicentre vs gnomAD NFE | PMID:40680702 (cached) |
| NEXN in HCM vs population | **No enrichment** | Same | PMID:40680702 (cached) |

For context, **HCM overall** has a prevalence of ~1 in 500 (≈200 per 100,000), with recent imaging-informed estimates spanning 1 in 200 to 1 in 500 (PMID:25814232 and subsequent). If CMH20 were real and accounted for 0.14% of HCM, its population prevalence would be ~0.28 per 100,000 — but given the absence of case-control enrichment, even that is an overestimate. Suggested dismech `prevalence_class`: **`NOT_YET_DOCUMENTED`** or **`UNKNOWN`**, with `measure_type: CASES_IN_LITERATURE` and the 0.14% figure recorded in `notes`.

### Genetic Etiology Parameters

- **Inheritance pattern:** Autosomal dominant (`HP:0000006`) for CMH20. ClinGen curates the NEXN-HCM MOI as AD. **Autosomal recessive** (`HP:0000007`) applies to the distinct lethal fetal cardiomyopathy phenotype. Consider curating both as separate `Inheritance` blocks with a note on the allelic-dose gradient.
- **Penetrance:** Incomplete and age-dependent. Family A: 3 affected carriers including a 16-year-old; Family B: 4 carriers including a 12-year-old — early-adolescent carriers may simply be pre-penetrant rather than mildly affected. Reliable penetrance estimates are **not available**.
- **Expressivity:** Variable. OMIM notes CMH20 has "inter- and intrafamilial variability ranging from benign to malignant forms with high risk of cardiac failure and sudden cardiac death" ⚑ — though this is boilerplate carried across the CMH series, not CMH20-specific observation.
- **Genetic anticipation:** No. Not a repeat-expansion disorder. **Not applicable.**
- **Germline mosaicism:** Not reported. **Not available.**
- **Founder effects:** None for the HCM alleles. For DCM, ⚑ **p.(Gly650del)** behaves as a recurrent German allele (OR ≈ 57.9). The Johansson biallelic allele arose in a Swedish family (PMID:35166435) — consanguinity/endogamy plausible but not characterized as a founder event.
- **Consanguinity:** Relevant only to the biallelic fetal phenotype.
- **Carrier frequency:** For the recessive lethal fetal phenotype, no carrier-frequency estimate exists. gnomAD LOEUF 0.88 / pLI 0 indicate NEXN LoF alleles are **not** strongly depleted, so heterozygous LoF carriers are not vanishingly rare — consistent with the observed mild, incompletely penetrant heterozygous phenotype.

### Population Demographics

- **Affected populations:** The two founding families were **Han Chinese** (PMID:20970104). Subsequent NEXN cohorts are predominantly European (French, Italian, Dutch, Spanish, UK, Hungarian) and one Swedish family. No population shows established CMH20 excess.
- **Geographic distribution:** No endemic pattern. Reporting bias tracks cardiogenetics infrastructure.
- **Sex ratio:** Roughly balanced in the available data — 16/29 male in the Hermida single-variant cohort (55%); 53% male in the Perotto NEXN-tv DCM/NDLVC arm. Consistent with autosomal dominant inheritance and no strong sex effect. (HCM broadly shows male over-representation in referral cohorts, generally attributed to ascertainment.)
- **Age distribution:** Diagnoses cluster in the third-to-fifth decades (median 32; IQR 26–49).

---

## 10. Diagnostics

### Clinical Tests

**Imaging (primary diagnostic modality)**
- **Transthoracic echocardiography** — the diagnostic cornerstone: maximal LV wall thickness **≥15 mm** (or ≥13 mm with family history) unexplained by loading conditions; assessment of asymmetric septal hypertrophy, SAM of the mitral valve, LVOT gradient at rest and with provocation (Valsalva, exercise), diastolic function, LA size.
- **Cardiac MRI with late gadolinium enhancement (CMR-LGE)** — tissue characterization, apical/anterolateral hypertrophy missed by echo, and **fibrosis quantification**; LGE extent ≥15% of LV mass is an SCD risk modifier in the 2024 guideline. Highly relevant here — 64% of NEXN-tv carriers had myocardial fibrosis (PMID:40680702).
- **Exercise stress echocardiography** — provocable obstruction; functional capacity.

**Electrophysiology**
- **12-lead ECG** — abnormal in >90% of HCM; LVH voltage criteria, repolarization abnormalities, pathological Q waves. ECG changes may precede hypertrophy in genotype-positive individuals.
- **Ambulatory Holter (≥24–48 h, extended monitoring)** — mandatory for NSVT detection (SCD risk factor) and AF screening. Given the arrhythmia-forward NEXN signature, arguably warrants intensified surveillance.
- Electrophysiology study — not routine.

**Laboratory / biomarkers**
- **NT-proBNP** (LOINC `33762-6`) and **BNP** (LOINC `30934-4`) — prognostic in HCM, elevated with wall stress/diastolic dysfunction.
- **High-sensitivity cardiac troponin T/I** (LOINC `67151-1`) — subclinical myocyte injury; associated with LGE burden.
- No NEXN- or CMH20-specific biochemical biomarker exists. **Not available.**
- Phenocopy exclusion panel: serum/plasma **alpha-galactosidase A** activity and *GLA* testing (Fabry), **serum/urine free light chains + technetium-pyrophosphate scintigraphy + TTR genotyping** (ATTR amyloidosis), **creatine kinase** (Danon, glycogen storage), **lysosome-associated membrane protein 2** (Danon).

**Biopsy / pathology**
- Endomyocardial biopsy is **not** indicated for HCM diagnosis; reserved for suspected infiltrative/inflammatory phenocopy. Classic HCM histopathology: myocyte hypertrophy, **myofiber disarray** (`HP:0031318`), interstitial and replacement fibrosis, intramural small-vessel disease. **No CMH20-specific histopathology has ever been published** — a notable gap given that the Z-disc hypothesis would predict ultrastructural Z-disc abnormalities on EM. Hassel et al. did report that "Nexilin mutation carriers showed the same cardiac Z-disk pathology as observed in nexilin-deficient zebrafish" (PMID:19881492, cached) — but again, **in DCM carriers**.

### Genetic Testing

**Recommended approach.** Per the 2024 AHA/ACC HCM guideline (PMID:38718139), genetic testing is a **Class 1** recommendation for patients with clinically diagnosed HCM, coupled with genetic counseling, primarily to enable cascade screening of relatives.

- **Multi-gene HCM panel** — first-line. **Critically: NEXN is increasingly excluded from contemporary HCM panels.** ⚑ The 2025 review states NEXN "is consequently not included in HCM panels" (PMID:40161564), and the ClinGen reappraisal advises that "Clinical laboratories are discouraged from reporting variants in genes with disputed HCM-association" — with Limited genes treated as genes of uncertain significance. Core validated HCM panel content: *MYBPC3, MYH7, TNNT2, TNNI3, TPM1, ACTC1, MYL2, MYL3* (Definitive), plus phenocopy genes (*GLA, LAMP2, PRKAG2, TTR, PTPN11/RASopathies, GAA*).
- **NEXN single-gene testing** — appropriate only when the clinical suspicion is **DCM/NDLVC**, or for cascade testing in a family with an established segregating variant, or for fetal/perinatal cardiomyopathy with EFE (biallelic).
- **WES/WGS** — reserved for panel-negative cases, syndromic presentations, or research. Genome sequencing offers no proven incremental yield over panels in isolated HCM.
- **Chromosomal microarray, karyotyping, FISH** — not indicated for isolated HCM; consider CMA if syndromic/dysmorphic features suggest a contiguous-gene disorder. **Not applicable to CMH20.**
- **Mitochondrial DNA testing** — indicated only if maternal inheritance, lactic acidosis, or multisystem involvement suggests mitochondrial cardiomyopathy (a phenocopy).
- **Repeat expansion testing** — **Not applicable.** Not a repeat disorder. (Friedreich ataxia *GAA* expansion is the one repeat disorder with an HCM phenotype and should be considered a phenocopy, not CMH20.)

**Variant-interpretation caution specific to this gene:** because most NEXN P/LP variants in ClinVar are LoF and the HCM claims rest on missense alleles — one of which is population-frequent — apply PM2/BS1 rigorously and weight gnomAD frequency heavily. p.(Arg279Cys) is the cautionary example.

### Omics-Based Diagnostics

None validated. RNA-seq/proteomics/metabolomics/epigenomics/liquid biopsy have **no established diagnostic role** in CMH20. **Not available.**

### Clinical Criteria

- **Diagnostic criteria:** 2024 AHA/ACC/AMSSM/HRS/PACES/SCMR guideline (PMID:38718139) and 2023 ESC cardiomyopathy guideline — unexplained LV wall thickness ≥15 mm (adults; ≥13 mm with family history or positive genotype), or z-score ≥2 in children, not explained by loading conditions.
- **Differential diagnosis (essential to exclude):**

| Phenocopy | Distinguishing features |
|---|---|
| Hypertensive heart disease / athlete's heart | Concentric, ≤15 mm, regresses with detraining/BP control |
| **Fabry disease** (*GLA*) | Low T1 on CMR, acroparesthesia, angiokeratoma, renal involvement, low α-Gal A |
| **ATTR / AL amyloidosis** | High T1/ECV, low-voltage ECG discordant with wall thickness, ⁹⁹ᵐTc-PYP uptake, monoclonal protein |
| **Danon disease** (*LAMP2*) | X-linked, WPW, skeletal myopathy, intellectual disability, extreme LVH |
| **PRKAG2 syndrome** | Pre-excitation, conduction disease, glycogen storage |
| **RASopathies** (Noonan/*PTPN11*) | Dysmorphism, pulmonary valve stenosis, short stature |
| **Pompe disease** (*GAA*) | Infantile hypotonia, low acid α-glucosidase |
| **Friedreich ataxia** (*FXN*) | Ataxia, concentric LVH, GAA expansion |
| **NEXN-DCM/NDLVC** | ← Most relevant here: distinguish a *dilated/non-dilated hypokinetic* NEXN phenotype from a genuine hypertrophic one before invoking CMH20 |

### Screening

- **Cascade family screening** — the primary preventive intervention. If a pathogenic variant is identified: predictive genetic testing of first-degree relatives; genotype-negative relatives discharged. If no variant identified (the common situation for CMH20-suspected families given the Limited validity): **serial clinical screening** with ECG + echocardiography — every 1–2 years ages 12–21, every 3–5 years thereafter.
- **Newborn screening:** not applicable.
- **Carrier screening:** not applicable for the dominant phenotype; relevant only for reproductive counseling in families with the recessive lethal fetal phenotype.

---

## 11. Outcome / Prognosis

### CMH20-Specific Data

**Essentially absent.** No survival curve, mortality rate, or outcome study exists for CMH20. The only outcome data points are the two pedigree SCDs (mother at 38, grandmother at ~40) ⚑ from PMID:20970104 — anecdotal and unadjudicated.

### NEXN-Cardiomyopathy Outcomes (DCM/NDLVC arm — the best available proxy, and it is an imperfect one)

From Perotto et al. 2025 (PMID:40680702, cached):
- Mild disease at baseline: indexed LVEDV 69 mL (IQR 46–87), LVEF 44% (IQR 31–53), NYHA I in **71%**
- Myocardial fibrosis in **64%**
- Over 45-month median follow-up: **53%** received an ICD; **25%** had malignant ventricular arrhythmias
- Key comparative finding: "Compared with TTN-CMP, NEXN-CMP exhibited earlier and more frequent MVAs at higher ejection fractions, and no significant differences were found against FLNC-CMP."
- Conclusion: "NEXNtvs were significantly associated with DCM/NDLVC, characterized by mild cardiac abnormalities, infrequent heart failure, common fibrosis, and arrhythmias."

**This FLNC-equivalence is the clinically actionable finding in the entire NEXN literature.** *FLNC* truncating variants are a recognized arrhythmogenic-cardiomyopathy genotype warranting a lowered ICD threshold. If NEXN behaves similarly, NEXN carriers merit arrhythmia-forward risk stratification even with preserved EF.

From Hermida et al. 2024 (PMID:38059363, cached):
- "For patients with dilated cardiomyopathy, the median left ventricle ejection fraction was 37.5% (26.25-50.0) at diagnosis and improved with treatment in 13 (61.9%)."
- "Over a median follow-up period of 6.0 years, we recorded 3 severe arrhythmic events and 2 severe hemodynamic events."
- "Putative pathogenic NEXN variants were mainly associated with dilated cardiomyopathy; in these individuals, the prognosis appeared to be relatively good. However, severe and early onset phenotypes were also observed-especially in patients with double NEXN variants."

### General HCM Prognostic Context

Contemporary HCM management has driven disease-related mortality to **~0.5% per year** across all age groups, "lower than in the other cardiac or noncardiac risks of living, and largely confined to nonobstructive patients with progressive heart failure, including those awaiting heart transplant" ⚑ (PMID:38368039, 2024). Most HCM patients now "achieve normal or extended life expectancy without major disability" ⚑.

### Complications

Sudden cardiac death (`HP:0001645`); malignant ventricular arrhythmia (`HP:0004308`); atrial fibrillation (`HP:0005110`) with cardioembolic stroke; progressive heart failure (`HP:0001635`); infective endocarditis (obstructive HCM with SAM); "burnt-out" systolic dysfunction requiring transplant.

### Prognostic Factors

Established HCM SCD risk markers (2024 AHA/ACC): prior cardiac arrest/sustained VT; family history of SCD; unexplained syncope; maximal wall thickness ≥30 mm; LV apical aneurysm; LVEF <50%; extensive CMR-LGE (≥15% LV mass); NSVT on monitoring. The ESC **HCM Risk-SCD** calculator provides a 5-year risk estimate. **None of these has been validated in NEXN carriers**, and the Perotto finding of arrhythmia at *preserved* EF suggests conventional EF-based thresholds may underestimate risk in this genotype.

### Prognostic Biomarkers

NT-proBNP and hs-troponin (general HCM). CMR-LGE burden. **No NEXN-specific prognostic biomarker.**

---

## 12. Treatment

There is **no genotype-specific therapy for CMH20**. Management follows the 2024 AHA/ACC/AMSSM/HRS/PACES/SCMR HCM guideline (PMID:38718139) and, where the phenotype is actually dilated/hypokinetic, guideline-directed medical therapy for heart failure.

### Pharmacotherapy

| Treatment | NCIT term (OAK-verified) | Therapeutic agent (NCIT) | Modality | Indication |
|---|---|---|---|---|
| Beta blocker (e.g. metoprolol) | `NCIT:C15986` Pharmacotherapy | `NCIT:C61845` Metoprolol | SMALL_MOLECULE | First-line for symptomatic obstructive and nonobstructive HCM |
| Non-dihydropyridine CCB (verapamil) | `NCIT:C15986` Pharmacotherapy | `NCIT:C928` Verapamil | SMALL_MOLECULE | Alternative first-line if beta blockers not tolerated |
| Disopyramide | `NCIT:C15986` Pharmacotherapy | `NCIT:C61730` Disopyramide | SMALL_MOLECULE | Negative inotrope added to BB/CCB for refractory obstruction |
| **Mavacamten** | `NCIT:C15986` Pharmacotherapy | `NCIT:C174901` Mavacamten | SMALL_MOLECULE | **Cardiac myosin inhibitor**; symptomatic obstructive HCM refractory to first-line therapy |
| Oral anticoagulation (DOAC) | `NCIT:C15986` Pharmacotherapy | — | SMALL_MOLECULE | AF in HCM — anticoagulate regardless of CHA₂DS₂-VASc |
| GDMT for HF (ACEi/ARNI, BB, MRA, SGLT2i) | `NCIT:C15986` Pharmacotherapy | — | SMALL_MOLECULE | For the NEXN dilated/burnt-out phenotype |

**Mavacamten mechanism** — "Cardiac myosin inhibitors inhibit actin-myosin interaction to decrease cardiac contractility and reduce left ventricular outflow tract obstruction, with mavacamten currently being the only FDA-approved agent" ⚑ (2024 guideline coverage). Approved on the EXPLORER-HCM (NCT03470545) and VALOR-HCM (NCT04349072) trials. **Aficamten**, a second-generation cardiac myosin inhibitor (SEQUOIA-HCM, NCT05186818), has completed phase 3.

**Important mechanistic caveat for curation:** mavacamten targets the **actin–myosin cross-bridge**, i.e. the hypercontractility of sarcomeric HCM. A Z-disc structural lesion is **not** obviously a hypercontractility disease, and there is no evidence that myosin inhibition benefits NEXN carriers. Do not curate a `target_mechanisms` link from mavacamten to a NEXN Z-disc node — that would assert an untested mechanism.

**Drugs to avoid in obstructive HCM:** vasodilators (nitrates, dihydropyridine CCBs, ACE inhibitors in obstructive physiology), high-dose diuretics, digoxin, and positive inotropes — all worsen the outflow gradient.

### Pharmacogenomics

**Mavacamten is dosed by CYP2C19 metabolizer status** — the FDA label incorporates CYP2C19 poor-metabolizer dose adjustment, and concomitant strong CYP2C19/CYP3A4 inhibitors are contraindicated or require dose modification. This is the one genuinely actionable PGx element in HCM care (PharmGKB). No NEXN-related pharmacogenomics.

### Advanced Therapeutics

- **Gene therapy** (`NCIT:C15238`): AAV9-*MYBPC3* gene replacement is in early clinical development for *MYBPC3* HCM (e.g. TN-201, NCT05836259). **No NEXN gene therapy program exists.** Note that NEXN's cDNA (~2 kb) is well within AAV packaging capacity, making it theoretically tractable — but there is no program and no preclinical proof of concept for the HCM phenotype.
- **Gene editing / base editing:** preclinical only for sarcomeric HCM; nothing for NEXN.
- **RNA-based therapies (ASO/siRNA):** none for NEXN. For a dominant-negative missense allele such as p.Q131E, allele-selective knockdown would be the mechanistically apt strategy — a legitimate hypothesis, but entirely speculative.
- **Cell therapy, targeted therapy, immunotherapy:** **Not applicable.**

### Surgical and Interventional

| Intervention | NCIT term | Modality | Indication |
|---|---|---|---|
| Surgical septal myectomy | `NCIT:C51591` Myectomy | SURGERY | Drug-refractory severe LVOT obstruction; gold standard at experienced centers |
| Alcohol septal ablation | `NCIT:C49236` Therapeutic Procedure | SURGERY/DEVICE | Alternative in selected anatomy/high surgical risk |
| ICD implantation | `NCIT:C80435` Implantable Cardioverter-Defibrillator Placement | DEVICE | Primary or secondary SCD prevention per risk stratification |
| Heart transplantation | `NCIT:C15289` Organ Transplantation | SURGERY | End-stage HF / refractory arrhythmia |
| Catheter ablation | `NCIT:C49236` Therapeutic Procedure | SURGERY | Symptomatic AF; selected VT |

"Invasive septal reduction therapies (surgical septal myectomy and alcohol septal ablation), when performed by experienced HCM teams at dedicated centers, can provide safe and effective symptomatic relief for patients with drug-refractory or severe outflow tract obstruction" ⚑ (2024 guideline).

### Supportive, Rehabilitative, Counseling

- Supportive care `NCIT:C15747`; cardiac rehabilitation `NCIT:C15315`; **genetic counseling `NCIT:C15240`** — Class 1 and especially important here, because a Limited-validity NEXN result must be communicated as *not diagnostic* and must not be used to release relatives from clinical surveillance.
- The 2024 guideline liberalized exercise recommendations: mild-to-moderate recreational exercise is beneficial; competitive-sport participation is now a shared decision-making conversation rather than a blanket prohibition.

### Experimental Treatments

No CMH20-specific trial exists. Relevant HCM trials: EXPLORER-HCM (NCT03470545), VALOR-HCM (NCT04349072), SEQUOIA-HCM (NCT05186818, aficamten), ODYSSEY-HCM (NCT05582395, mavacamten in nonobstructive HCM), MAPLE-HCM (NCT05767346, aficamten monotherapy). **None enrolls by genotype, and none has reported NEXN-carrier subgroups.**

### Treatment Strategy

Obstructive HCM: BB or verapamil → add disopyramide or mavacamten → septal reduction therapy. Nonobstructive HCM: symptom-directed; treat diastolic HF; consider mavacamten (ODYSSEY-HCM pending). AF: rate/rhythm control + anticoagulation. SCD prevention: risk-stratify → ICD. **If the NEXN carrier's phenotype is actually dilated/hypokinetic, switch entirely to four-pillar HF GDMT and consider an FLNC-like lowered ICD threshold.**

---

## 13. Prevention

**Primary prevention.** Not possible — the germline variant is present from conception. Reproductive options for known carriers: preimplantation genetic testing for monogenic disorders (PGT-M) and prenatal diagnosis, which are far more compelling for the **biallelic lethal fetal** phenotype (recurrence risk 25%) than for the Limited-validity dominant HCM claim.

**Secondary prevention (the mainstay).** Cascade genetic testing and serial clinical screening of first-degree relatives (ECG + echocardiography; intervals per §10). Early detection permits pre-symptomatic risk stratification and ICD placement before a first arrhythmic event.

**Tertiary prevention.** ICD for SCD prevention; anticoagulation for AF-related stroke; septal reduction to prevent progressive HF; GDMT to prevent adverse remodeling; endocarditis awareness in obstructive disease with SAM.

**Immunization.** Not disease-specific; routine influenza/COVID/pneumococcal vaccination is standard for chronic cardiac disease. **Not applicable as a targeted intervention.**

**Genetic screening.** Cascade predictive testing (only when a genuinely pathogenic variant is identified — a high bar for NEXN missense alleles); PGT-M and prenatal testing for the recessive fetal phenotype. `NCIT:C15240` Genetic Counseling.

**Risk stratification.** ESC HCM Risk-SCD calculator; 2024 AHA/ACC major risk marker enumeration; CMR-LGE quantification. **Unvalidated in NEXN carriers.**

**Behavioral interventions.** Blood-pressure and weight control; avoid dehydration and provocative vasodilators in obstructive physiology; individualized exercise prescription; avoid stimulants.

**Public health / environmental interventions.** Community AED deployment and CPR training reduce out-of-hospital cardiac-arrest mortality in HCM populations. Pre-participation athletic ECG screening remains contested (endorsed in Italy, not in the US). No environmental intervention applies.

---

## 14. Other Species / Natural Disease

### Taxonomy and Orthology

| Species | NCBI Taxon | Gene | NCBI Gene ID |
|---|---|---|---|
| *Homo sapiens* | `NCBITaxon:9606` | NEXN | 91624 |
| *Mus musculus* | `NCBITaxon:10090` | Nexn | 68810 |
| *Danio rerio* | `NCBITaxon:7955` | nexn | — (ZFIN) |
| *Rattus norvegicus* | `NCBITaxon:10116` | Nexn | — (RGD) |

Nexilin's cardiac Z-disc function is deeply conserved across the vertebrate lineage — the zebrafish loss-of-function phenotype (Z-disc destabilization + heart failure) directly recapitulates the mammalian one, which is why zebrafish was the discovery system (PMID:19881492).

### Natural Disease in Other Species

**No naturally occurring NEXN-associated cardiomyopathy has been reported in any non-human species.** A targeted search of OMIA and the veterinary literature returned no NEXN entry for dogs, cats, or livestock. This is notable because feline HCM (especially *MYBPC3* in Maine Coon and Ragdoll cats) and canine DCM (Doberman *PDK4*/*TTN*, Boxer *STRN*) are both well-characterized natural models — NEXN simply is not among their known loci.

- **Breed (VBO):** **Not applicable** — no NEXN-associated breed predisposition identified.
- **Veterinary relevance:** none established. **Not applicable.**

### Comparative Biology

- **Comparative pathology:** the striking cross-species observation is that **every** NEXN loss-of-function model — zebrafish, mouse global KO, mouse cardiomyocyte-specific KO, mouse inducible adult KO, mouse G650del knock-in — produces **dilated**, not hypertrophic, cardiomyopathy, frequently with endomyocardial/endocardial fibroelastosis. Human biallelic loss also produces dilated cardiomyopathy with EFE (PMID:35166435, PMID:39183344). This convergence across four model systems and two human genotypes is the single most compelling argument against a NEXN-HCM mechanism.
- **Evolutionary conservation:** the affected residues Q131 and R279 are "highly conserved amino acid residues" across species (PMID:20970104, cached) — conservation supports functional importance but, given the population frequency of R279C, is clearly insufficient for pathogenicity.

### Transmission

**Not applicable** — monogenic, non-communicable. No zoonotic potential; no cross-species susceptibility.

---

## 15. Model Organisms

### Available Models

| Model | Type | Genotype | Key phenotype | Reference |
|---|---|---|---|---|
| Zebrafish nexn morphant | Vertebrate, in vivo | Knockdown | Perturbed Z-disk stability, heart failure | PMID:19881492 |
| Zebrafish + human mutant nexilin | Vertebrate, in vivo | mRNA overexpression | Z-disk damage, heart failure → **dominant-negative** | PMID:19881492 |
| Zebrafish *nexn* CRISPR KO | Vertebrate, in vivo | Constitutive homozygous | Reduced cardiac contractility; impaired skeletal muscle organization under stress | PMID:38114601 (Sci Rep 2023) |
| Mouse *Nexn* global KO | Mammalian, in vivo | Constitutive null | **Dilated cardiomyopathy + endomyocardial fibroelastosis**; perinatal/early lethality | PMID:26659360 (Aherrahrou, Basic Res Cardiol 2016) |
| Mouse *Nexn* cardiomyocyte-specific KO | Mammalian, in vivo | Conditional (Cre) | Progressive DCM; loss of T-tubule initiation; impaired Ca²⁺ transients | PMID:30982350 (Liu, Circulation 2019) |
| Mouse *Nexn* inducible adult CM-specific KO | Mammalian, in vivo | Tamoxifen-inducible | DCM; 13% FS reduction; **40% loss of transverse tubular component**; impaired Ca²⁺ handling | PMID:32635769 (Spinozzi, Circ Heart Fail 2020) |
| Mouse *Nexn* G650del knock-in | Mammalian, in vivo | Homozygous | ~30% of WT Nexn expression; progressive DCM with reduced T-tubule formation | PMID:32814711 (Liu, JCI Insight 2020) |
| C2C12 myoblasts | Cellular, in vitro | Transfection with p.Q131E / p.R279C | Cytoplasmic nexilin aggregates; complete loss of F-actin binding (p.Q131E) | PMID:20970104 |

### Model Types Available

- **Genetic:** knockout (global and conditional), knock-in (G650del), morpholino knockdown, CRISPR/Cas9 constitutive KO, transgenic mutant overexpression.
- **Cellular:** C2C12 myoblast transfection (the only system in which the HCM alleles have ever been studied).
- **Not available:** humanized mouse; **iPSC-derived cardiomyocytes carrying a NEXN HCM variant**; engineered heart tissue with NEXN lesions; organoids; rat models; induced (drug/surgical) models.

### Phenotype Recapitulation — the Central Problem

**No model recapitulates hypertrophic cardiomyopathy.** Every in vivo NEXN model produces a dilated phenotype:

> "Loss of nexilin in zebrafish led to perturbed Z-disk stability and heart failure." (PMID:19881492, cached)

> "Global and cardiomyocyte specific loss of Nexn in mice leads to a rapidly progressive dilated cardiomyopathy and premature death." ⚑ (PMID:32635769)

The only experimental evidence bearing directly on the *HCM* alleles is the C2C12 in-vitro work in the original paper — a myoblast transfection assay showing loss of actin binding, with **no cardiomyocyte, no hypertrophy readout, and no in vivo component**. In ClinGen terms, this is why NEXN's experimental evidence score was capped at 1.0 point.

**This is a textbook `HUMAN_MODEL_MISMATCH`, not a `KNOWLEDGE_GAP`.** Abundant model evidence exists; it consistently indicates the opposite phenotype from the one the disease entity asserts. Recommended `discussions` block:

```yaml
discussions:
- kind: HUMAN_MODEL_MISMATCH
  attaches_to: "pathophysiology#Cardiomyocyte Hypertrophic Response"
  prompt: >
    Every in vivo NEXN loss-of-function model (zebrafish morphant and CRISPR KO;
    mouse global, cardiomyocyte-specific, inducible adult, and G650del knock-in)
    produces DILATED cardiomyopathy with T-tubule and calcium-handling failure —
    never hypertrophy. Does any NEXN allele actually produce a hypertrophic
    phenotype in a human-relevant cardiomyocyte system?
  rationale: >
    The only experimental support for the CMH20 hypertrophic mechanism is a C2C12
    myoblast transfection assay (PMID:20970104) showing loss of F-actin binding —
    a non-cardiomyocyte system with no hypertrophy readout. The phenotypic
    direction of every in vivo model is opposite to the asserted disease. This
    mismatch is a principal basis for the ClinGen "Limited" classification.
  proposed_experiments:
    - Generate isogenic iPSC-CM lines carrying NEXN p.Gln131Glu and assay
      cell size, sarcomere organization, and hypertrophic gene program
      (NPPA/NPPB/MYH7) versus corrected controls.
    - Engineered heart tissue under graded afterload to test the
      mechanical-strain gene-environment hypothesis (PMID:19881492).
    - Knock-in mouse carrying the orthologous Q131E allele with serial
      echocardiography to test whether hypertrophy ever emerges.
```

### Model Limitations

Mouse constitutive KO is perinatally lethal, truncating the window for adult-phenotype study — the explicit rationale for the zebrafish CRISPR model (PMID:38114601). Zebrafish hearts are two-chambered with no T-tubules in the mammalian sense, limiting translation of the JMC findings. C2C12 is a *skeletal* myoblast line, not a cardiomyocyte. **No model of the human HCM alleles in a cardiac context exists at all.**

### Research Applications

Available models support study of: Z-disc mechanobiology and strain resistance; T-tubule/TATS biogenesis and maintenance; junctional membrane complex assembly and RyR2/JPH2 interaction; excitation–contraction coupling; endocardial fibroelastosis pathogenesis; DCM natural history. They do **not** support study of NEXN-related hypertrophy.

### Model Databases

MGI (*Nexn*, MGI:1919060); IMPC; ZFIN (*nexn*); RGD; Alliance of Genome Resources; IMSR/MMRRC for strain availability; Cellosaurus for C2C12 (CVCL_0188).

---

## Consolidated Ontology Term Suggestions

All IDs below were verified with OAK against the repository's configured adapters (`sqlite:obo:hp`, `:cl`, `:go`, `:uberon`, `:mondo`, `:ncit`) — none is hallucinated.

**Disease:** `MONDO:0013477` hypertrophic cardiomyopathy 20

**Gene:** `hgnc:29557` NEXN (note lowercase prefix per repo convention)

**Phenotypes (HP):** `HP:0001639` · `HP:0001712` · `HP:0032092` · `HP:0005110` · `HP:0012664` · `HP:0001645` · `HP:0001279` · `HP:0002094` · `HP:0100749` · `HP:0001962` · `HP:0004308` · `HP:0004756` · `HP:0001685` · `HP:0031318` · `HP:0025168` · `HP:0001635` · `HP:0001695`

**Inheritance:** `HP:0000006` Autosomal dominant inheritance (CMH20); `HP:0000007` Autosomal recessive inheritance (biallelic lethal fetal phenotype)

**Cell types (CL):** `CL:0000746` cardiac muscle cell · `CL:0002098` regular cardiac myocyte · `CL:0002548` fibroblast of cardiac tissue

**Anatomy (UBERON):** `UBERON:0000948` heart · `UBERON:0002084` heart left ventricle · `UBERON:0002094` interventricular septum · `UBERON:0002349` myocardium · `UBERON:0006566` left ventricle myocardium · `UBERON:0001133` cardiac muscle tissue

**Biological processes / components (GO):** `GO:0030018` Z disc · `GO:0030315` T-tubule · `GO:0016529` sarcoplasmic reticulum · `GO:0014801` longitudinal sarcoplasmic reticulum · `GO:0051015` actin filament binding · `GO:0045214` sarcomere organization · `GO:0030239` myofibril assembly · `GO:0060048` cardiac muscle contraction · `GO:0055117` regulation of cardiac muscle contraction · `GO:0070296` sarcoplasmic reticulum calcium ion transport · `GO:0086001` cardiac muscle cell action potential · `GO:0003300` cardiac muscle hypertrophy

**Treatments (NCIT):** `NCIT:C15986` Pharmacotherapy · `NCIT:C174901` Mavacamten · `NCIT:C61845` Metoprolol · `NCIT:C928` Verapamil · `NCIT:C61730` Disopyramide · `NCIT:C51591` Myectomy · `NCIT:C80435` Implantable Cardioverter-Defibrillator Placement · `NCIT:C15289` Organ Transplantation · `NCIT:C15240` Genetic Counseling · `NCIT:C15747` Supportive Care · `NCIT:C49236` Therapeutic Procedure · `NCIT:C15238` Gene Therapy

**Candidate module conformance:** `cardiomyopathy_maladaptive_remodeling#Ventricular Remodeling` (dilated arm — for the well-supported NEXN-DCM mechanism); `fibrotic_response` (64% fibrosis); `cardiac_ion_channel_repolarization#Arrhythmogenic Substrate and Triggered Activity` (arrhythmia-at-preserved-EF signature). **Do not** conform a CMH20 entry to a hypertrophy module without flagging the model mismatch.

---

## Evidence Register — PMIDs, Status, and Verification Requirements

| PMID | Citation | Evidence source | Cached? | Role in entry |
|---|---|---|---|---|
| **20970104** | Wang H et al. *Am J Hum Genet* 2010;87(5):687-93 | HUMAN_CLINICAL + IN_VITRO | ✅ | **Founding CMH20 report** — split into separate items by evidence_source |
| **19881492** | Hassel D et al. *Nat Med* 2009;15(11):1281-8 | MODEL_ORGANISM | ✅ | Nexilin as Z-disc protein; dominant-negative; mechanical strain (DCM alleles) |
| **38059363** | Hermida A et al. *Circ Genom Precis Med* 2024;17(1):e004285 | HUMAN_CLINICAL | ✅ | **Non-replication** — "a causal link could not be established" |
| **40680702** | Perotto M et al. *JACC Heart Fail* 2025;13(9):102529 | HUMAN_CLINICAL | ✅ | **Non-replication** — "no association was observed with HCM"; FLNC-equivalent arrhythmia risk |
| **20301725** | (GeneReviews-family entry, cached in worktree) | HUMAN_CLINICAL | ✅ | Verify target before citing |
| 30681346 | Ingles J et al. *Circ Genom Precis Med* 2019;12(2):e002460 | HUMAN_CLINICAL | ❌ fetch | First formal HCM clinical-validity curation |
| 39132495 | ClinGen HCD GCEP HCM reappraisal (medRxiv; JACC 2025) | HUMAN_CLINICAL | ❌ fetch | NEXN retains **Limited** |
| 38718139 | 2024 AHA/ACC/AMSSM/HRS/PACES/SCMR HCM Guideline | HUMAN_CLINICAL | ❌ fetch | Diagnosis, risk stratification, treatment |
| 40161564 | Năstasie OC et al. *World J Cardiol* 2025;17(3):100290 | OTHER (review) | ❌ fetch | NEXN phenotype spectrum; "not included in HCM panels" |
| 38985384 | Rahimzadeh M et al. *Heart Fail Rev* 2024 | OTHER (review) | ❌ fetch | Nexilin roles; EFE focus |
| 30982350 | Liu C et al. *Circulation* 2019;140(1):55-66 | MODEL_ORGANISM | ❌ fetch | JMC / T-tubule formation |
| 32635769 | Spinozzi S et al. *Circ Heart Fail* 2020 | MODEL_ORGANISM | ❌ fetch | Adult TATS maintenance; Ca²⁺ handling |
| 26659360 | Aherrahrou Z et al. *Basic Res Cardiol* 2016 | MODEL_ORGANISM | ❌ fetch | Nexn KO → DCM + endomyocardial fibroelastosis |
| 32814711 | Liu C et al. *JCI Insight* 2020 | MODEL_ORGANISM | ❌ fetch | G650del knock-in mouse |
| 38114601 | *Sci Rep* 2023;13:22599 | MODEL_ORGANISM | ❌ fetch | Zebrafish CRISPR nexn KO |
| 35166435 | Johansson J et al. *Am J Med Genet A* 2022;188(6):1676-87 | HUMAN_CLINICAL | ❌ fetch | Biallelic lethal fetal cardiomyopathy + EFE |
| 39183344 | *Ital J Pediatr* 2024;50:163 | HUMAN_CLINICAL | ❌ fetch | Two biallelic infants; novel alleles; favorable course |
| 38368039 | *Am J Cardiol* 2024 | HUMAN_CLINICAL | ❌ fetch | Contemporary HCM mortality ~0.5%/yr |
| 25814232 | Semsarian C et al. *J Am Coll Cardiol* 2015 | HUMAN_CLINICAL | ❌ fetch | HCM prevalence re-estimation |

**Structured-source citations available without fetching:** `CGGV:` for the ClinGen NEXN gene-disease validity assertions (HCM/Limited and DCM 1CC/Strong) — check `references_cache/` for the matching assertion IDs, or refresh with `just clingen-rebuild`. These give snippet-validatable rows for the two classifications that anchor this entry.

---

## Recommended Curation Posture

1. **Create the entry** — CMH20 is a legitimate MONDO/OMIM entity and belongs in the KB. Absence would be a gap.
2. **Lead with the validity caveat** — record the ClinGen Limited classification as a first-class, evidence-backed claim (`CGGV:` snippet), not a footnote.
3. **Curate the mechanism as hypothesis-grade** — a `mechanistic_hypotheses` block with `status: DISPUTED` or `EMERGING`, and causal edges opting into that hypothesis group via `downstream[].hypothesis_groups`.
4. **Include the refuting evidence** — Perotto 2025 and Hermida 2024 as `supports: REFUTE` / `supports: PARTIAL` items. The schema supports this; use it. An entry that cites only the 2010 founding paper would misrepresent the state of the field.
5. **Add the `HUMAN_MODEL_MISMATCH` discussion** — the model-phenotype inversion is the most curatable insight in this entry.
6. **Cross-link, don't merge** — keep CMH20 distinct from a future `Dilated_Cardiomyopathy_1CC` entry, where the NEXN mechanism is genuinely well supported and the Z-disc/JMC/T-tubule pathophysiology can be curated with confidence.
7. **Re-verify every ⚑ quote** with `just fetch-reference` + `just validate-references` before it enters YAML. The five cached PMIDs are safe to quote as written above.

---

## Sources

- [OMIM #613876 — CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 20; CMH20](https://omim.org/entry/613876)
- [OMIM *613121 — NEXILIN F-ACTIN-BINDING PROTEIN; NEXN](https://omim.org/entry/613121)
- [MedGen 462617 — Cardiomyopathy, familial hypertrophic, 20](https://www.ncbi.nlm.nih.gov/medgen/462617)
- [ClinGen — NEXN (HGNC:29557) curation results](https://search.clinicalgenome.org/kb/genes/HGNC:29557)
- [ClinGen HCD GCEP: Reappraisal of Genes associated with Hypertrophic Cardiomyopathy (PMC11312670)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11312670/)
- [Genes Associated With Hypertrophic Cardiomyopathy: A Reappraisal (JACC 2025)](https://www.jacc.org/doi/10.1016/j.jacc.2024.12.010)
- [Ingles et al. — Evaluating the Clinical Validity of Hypertrophic Cardiomyopathy Genes (PMID:30681346)](https://pubmed.ncbi.nlm.nih.gov/30681346/)
- [Wang et al. 2010 — Mutations in NEXN, a Z-disc gene, are associated with HCM (PMC2978958)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2978958/)
- [Hermida et al. 2024 — NEXN Gene in Cardiomyopathies and Sudden Cardiac Deaths](https://www.ahajournals.org/doi/10.1161/CIRCGEN.123.004285)
- [Perotto et al. 2025 — Genetic and Phenotypic Characterization of NEXN-Related Cardiomyopathy](https://www.sciencedirect.com/science/article/pii/S2213177925004561)
- [Năstasie et al. 2025 — Nexilin mutations, a cause of chronic heart failure (PMC11947951)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947951/)
- [Rahimzadeh et al. 2024 — Nexilin in cardiomyopathy (Heart Fail Rev)](https://link.springer.com/article/10.1007/s10741-024-10416-8)
- [Liu et al. 2019 — Nexilin Is a New Component of Junctional Membrane Complexes (PMID:30982350)](https://pubmed.ncbi.nlm.nih.gov/30982350/)
- [Spinozzi et al. 2020 — Nexilin is necessary for maintaining the TATS (PMC7583668)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7583668/)
- [Aherrahrou et al. 2016 — Knock-out of nexilin in mice (PMID:26659360)](https://pubmed.ncbi.nlm.nih.gov/26659360/)
- [Liu et al. 2020 — Homozygous G650del nexilin variant causes cardiomyopathy in mice (JCI Insight)](https://insight.jci.org/articles/view/138780)
- [CRISPR/Cas9-mediated nexilin deficiency in zebrafish (PMID:38114601)](https://pubmed.ncbi.nlm.nih.gov/38114601/)
- [Johansson et al. 2022 — Loss of Nexilin function, recessive lethal fetal cardiomyopathy](https://onlinelibrary.wiley.com/doi/full/10.1002/ajmg.a.62685)
- [Biallelic NEXN variants and fetal onset dilated cardiomyopathy (PMID:39183344)](https://pubmed.ncbi.nlm.nih.gov/39183344/)
- [2024 AHA/ACC/AMSSM/HRS/PACES/SCMR Guideline for the Management of HCM (PMID:38718139)](https://pubmed.ncbi.nlm.nih.gov/38718139/)
- [Advances in the Management of HCM Leading to Low Disease-Related Mortality in 2023 (PMID:38368039)](https://pubmed.ncbi.nlm.nih.gov/38368039/)
- [New perspectives on the prevalence of hypertrophic cardiomyopathy (PMID:25814232)](https://pubmed.ncbi.nlm.nih.gov/25814232/)
- [Structural and signaling proteins in the Z-disk and their role in cardiomyopathies (Front Physiol 2023)](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2023.1143858/full)
- [Orphanet — Rare hypertrophic cardiomyopathy (ORPHA:217569)](https://www.orpha.net/en/disease/detail/217569)
- [GeneCards — NEXN](https://www.genecards.org/cgi-bin/carddisp.pl?gene=NEXN)
- [Genomics England PanelApp — NEXN in Hypertrophic cardiomyopathy panel](https://panelapp.genomicsengland.co.uk/panels/49/gene/NEXN/)