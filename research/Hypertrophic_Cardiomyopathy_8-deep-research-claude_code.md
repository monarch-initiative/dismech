---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T20:57:52.048106'
end_time: '2026-08-01T21:25:36.807453'
duration_seconds: 1664.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 8
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
  web_search_requests: 11
  num_turns: 89
  total_cost_usd: 7.899586999999998
  session_id: f2b809c0-4faf-4879-8731-78b7c33ab031
  stop_reason: end_turn
citation_count: 16
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 8
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 8** covering all of the
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

# Hypertrophic Cardiomyopathy 8 (CMH8 / MYL3-Related Hypertrophic Cardiomyopathy)
## Comprehensive Disease Characteristics Research Report

**Prepared:** 2026-08-01 | **Target entity:** Hypertrophic cardiomyopathy 8 | **MONDO:0012111** | **Category:** Mendelian (sarcomeric cardiomyopathy)

**Verification note:** Every PMID cited below was retrieved from PubMed via `just fetch-reference` and the quoted snippets were read directly from the cached abstract/full text (`references_cache/PMID_*.md`). All ontology identifiers (HP, GO, CL, UBERON, CHEBI, NCIT, MONDO, hgnc) were verified with OAK against the local ontology builds before inclusion. Where a fact could not be verified from a primary source, it is explicitly flagged.

---

## 1. Disease Information

### 1.1 Overview

Hypertrophic cardiomyopathy 8 (CMH8) is the form of familial hypertrophic cardiomyopathy caused by variants in **MYL3**, the gene encoding the **ventricular/slow-skeletal myosin essential light chain (ELC, also "alkali light chain", MLC-1v/MLC1SB, CMLC1)**. It is one of the eight sarcomere genes with a **Definitive** ClinGen gene–disease relationship to HCM, but is quantitatively a *minor* HCM gene (well under 5% of genotype-positive HCM; myosin light chain genes together ≈1% of HCM).

Two features distinguish CMH8 from the "generic" HCM entry and justify a separate knowledge-base entity:

1. **A characteristic morphological subtype** — hypertrophy that is maximal in the **mid-ventricular segments and papillary muscles**, producing **mid-cavity (intracavitary) obstruction** rather than classical subaortic LVOT obstruction, sometimes with **restrictive physiology** and (in one report) an **LV apical aneurysm**. This is reflected in the OMIM alternative title "Cardiomyopathy, hypertrophic, mid-left ventricular chamber type, 1."
2. **A genuine dual inheritance architecture** — classic autosomal dominant missense disease *and* well-documented **autosomal recessive disease from biallelic loss-of-function (LOF) MYL3 variants**, which is unusual among sarcomeric cardiomyopathies and has direct counseling consequences.

Olson et al. framed the dominant/recessive duality explicitly: *"Distinct mutations affecting the same sarcomeric protein can cause either dominant or recessive cardiomyopathy."* (PMID:12021217)

### 1.2 Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| OMIM (phenotype) | **#608751** — CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 8; CMH8 | Phenotype–gene relationship: MYL3, 3p21.31 |
| OMIM (gene) | ***160790** — MYOSIN, LIGHT CHAIN 3, ALKALI, VENTRICULAR, SKELETAL, SLOW; MYL3 | |
| MONDO | **MONDO:0012111** — hypertrophic cardiomyopathy 8 | Verified with OAK (`ols:mondo`) |
| MedGen | **CUI C1837471** (UID 324806) | Gene: MYL3, 3p21.31; xref Monarch MONDO:0012111 |
| HGNC (gene) | **hgnc:7584** — MYL3 | Lowercase prefix per repo convention; already used in `kb/disorders/Hypertrophic_Cardiomyopathy.yaml` |
| UniProt | **P08590** (MYL3_HUMAN), 195 aa, ~21.9 kDa | 3 EF-hand regions (49–86, 128–163, 163–195); N-terminal disordered extension ~1–37 |
| Ensembl | ENSG00000160808 | |
| ClinVar | 517 records for MYL3[gene]; **14 pathogenic/likely-pathogenic** (queried 2026-08-01 via E-utilities) | |
| ICD-10 | **I42.1** (obstructive hypertrophic cardiomyopathy) / **I42.2** (other hypertrophic cardiomyopathy) | No CMH8-specific code |
| ICD-11 | **BC43.0** Hypertrophic cardiomyopathy (BC43.00 obstructive) | No CMH8-specific code |
| MeSH | **D024741** Cardiomyopathy, Hypertrophic, Familial (verified via MeSH E-utilities UID 68024741); broader **D002312** Cardiomyopathy, Hypertrophic | |
| Orphanet | No CMH8-specific ORPHA code; subsumed under familial isolated hypertrophic cardiomyopathy | The local `references_cache/` contains no ORPHA record for this entity and orpha.net is bot-gated — **not verified** |
| ClinGen | MYL3–**Hypertrophic cardiomyopathy** (MONDO:0005045): **Definitive**, HCM GCEP, 2021-06-07, AD | Also MYL3–DCM: **Disputed** (DCM GCEP, 2025-05-30); MYL3–ARVC: **Limited** (2019-09-13); dosage: haploinsufficiency score **0**, triplosensitivity **0** (2015-11-18) |

### 1.3 Synonyms and alternative names

- Cardiomyopathy, familial hypertrophic, 8; CMH8; HCM8
- **Cardiomyopathy, hypertrophic, mid-left ventricular chamber type, 1** (OMIM alternative title; MedGen synonym)
- MYL3-related familial hypertrophic cardiomyopathy (MedGen synonym)
- Myosin essential light chain–associated HCM; ELC-associated HCM
- Mid-cavitary / mid-ventricular obstructive hypertrophic cardiomyopathy (phenotype-level descriptor, not a formal synonym)

### 1.4 Nature of the underlying evidence

Knowledge of CMH8 is derived almost entirely from **aggregated disease-level resources and small family/case series**, not from EHR or patient-level registries:
- Landmark family-based linkage/candidate-gene studies (PMID:8673105; PMID:12021217)
- Consanguineous-family exome studies (PMID:33288880)
- Cohort screening studies of sarcomere genes (PMID:12404107; PMID:20031618; PMID:25611685; PMID:26443374; PMID:37431535)
- Curated variant/gene resources (ClinVar, ClinGen HCM GCEP, gnomAD)
- Single case reports for the rarest phenotypes (PMID:35288424; PMID:23594557)
- Mechanistic transgenic-mouse, iPSC-CM, zebrafish and biophysics literature

There is **no CMH8-specific patient registry**; MYL3 carriers are pooled into general HCM registries (e.g., SHaRe, PMID:30297972) and meta-analyses (PMID:37929589).

---

## 2. Etiology

### 2.1 Primary causal factor

CMH8 is a **monogenic sarcomeropathy**: heterozygous (dominant) or homozygous/biallelic (recessive) variants in **MYL3** (hgnc:7584), encoding the ventricular myosin essential light chain that stabilizes the myosin lever arm/neck region and, through its cardiac-specific N-terminal extension, contacts actin.

Poetter et al. established causality in the founding report: *"We report here the identification of distinct missense mutations in a skeletal/ventricular ELC and RLC, each of which are associated with a rare variant of cardiac hypertrophy as well as abnormal skeletal muscle. We show that myosin containing the mutant ELC has abnormal function…"* (PMID:8673105, Nat Genet 1996; HUMAN_CLINICAL + IN_VITRO)

### 2.2 Genetic risk factors

**Causal variants (autosomal dominant, missense):** M149V, R154H (PMID:8673105); R94H (PMID:26443374); V79I (PMID:22957257); E152K/c.454G>A (PMID:35288424); E56G, E177G (UniProt P08590 variant annotations; biophysically characterized in PMID:36509720); c.530A>G exon 5 (infantile, PMID:23594557).

**Causal variants (autosomal recessive):** homozygous **E143K** (PMID:12021217); homozygous **A57D (c.170C>A)**, homozygous nonsense **E36\* (c.106G>T)**, and homozygous essential splice-acceptor **c.482-1G>A** (PMID:33288880).

**Susceptibility/penetrance context:** MYL3 has the **lowest measured penetrance among the definitive sarcomere genes** — *"Penetrance varied from ≈32% for MYL3 (myosin light chain 3) to ≈55% for MYBPC3 …, ≈60% for TNNT2 … and TNNI3 …, and ≈65% for MYH7"* (PMID:37929589, Circulation 2024). This makes MYL3 heterozygosity better modeled as a strongly-penetrant-but-incomplete risk allele than as a deterministic one.

**Consanguinity as a population-level genetic risk factor:** In a prospective Egyptian HCM cohort (n=514) vs. European comparison (n=684), *"A higher prevalence of homozygous variants was observed in Egyptian patients (4.1% vs. 0.1%, P = 2 × 10-7), with variants in the minor HCM genes MYL2, MYL3, and CSRP3 more likely to present in homozygosity than the major genes, suggesting these variants are less penetrant in heterozygosity."* (PMID:37431535, Eur Heart J 2023)

**Modifier genes:** No CMH8-specific modifier locus is established. Generic HCM modifiers (polygenic background, common-variant scores, second sarcomere variants) apply; note that digenic/compound sarcomere genotypes are documented in HCM cohorts generally (e.g., 5/42 mutation-positive pediatric patients carried two mutations, PMID:20031618). One report explicitly invoked genetic background to explain a null iPSC-CM result: *"this may also reflect the genetic background of the heterozygote and the presence of gene modifiers in this individual"* (PMID:33288880).

### 2.3 Environmental risk factors

No MYL3-specific environmental cause is established. Recognized general modifiers of HCM expression/outcome (extrapolated, not MYL3-specific):
- **Age** — dominant determinant of penetrance; mean age at HCM diagnosis in P/LP carriers 38 years (95% CI 36–40) (PMID:37929589)
- **Sex** — detection rates in clinical testing were *"higher in females compared with males"* (PMID:25611685); sex differences in HCM expression are well described
- **Family history / first-degree relationship to a proband** — the operational risk factor driving cascade screening
- **Intense competitive exercise, afterload (hypertension), obesity** — general HCM/LVH modifiers; **no MYL3-stratified data**
- **Catabolic/hemodynamic stressors** (pregnancy, atrial fibrillation onset) precipitate decompensation but are not causal

### 2.4 Protective factors

- **Genetic:** No validated protective allele. Notably, N-terminal ELC truncation is *protective in mice* for the HCM allele — *"In A57G×Δ43 mice, Δ43 expression improved heart function and reduced hypertrophy and fibrosis"* (PMID:39211545, iScience 2024, MODEL_ORGANISM) — a therapeutic hypothesis, **not** a human protective variant.
- **Heterozygosity for recessive LOF alleles is effectively "protected":** *"Family members with one Glu143Lys allele had normal echocardiograms and ECGs, even in late adulthood"* (PMID:12021217), attributed to *"compensatory mechanisms that preserve cardiac structure and function."*
- **Environmental:** No MYL3-specific protective exposure. Guideline-endorsed general measures (avoidance of dehydration/vasodilator excess in obstructive disease, treatment of hypertension, moderate exercise) are supportive, not disease-preventing (PMID:38718139).

### 2.5 Gene–environment interaction

No formal GxE study exists for MYL3. The mechanistically plausible interactions are (a) **allele × age** (dominant, quantified: penetrance ≈32%, late onset — PMID:22957257 reported mean age 47 in penetrant vs. 15 in non-penetrant carriers of p.V79I); (b) **allele × consanguinity/ancestry** (PMID:37431535); (c) **allele × hemodynamic load** — transgenic A57G mice show *"a significant increase in passive tension in response to stretch … indicating a mutation-induced myocardial stiffness"* (PMID:23748425), i.e., a load-dependent amplification loop.

---

## 3. Phenotypes

### 3.1 Cardiac structural phenotypes

| Phenotype | HPO term (OAK-verified) | Onset | Severity | Course | Frequency | Evidence |
|---|---|---|---|---|---|---|
| Hypertrophic cardiomyopathy | **HP:0001639** Hypertrophic cardiomyopathy | Infancy→late adult | Mild→severe | Progressive | Defining feature | PMID:8673105; 12021217; 33288880 |
| Left ventricular hypertrophy | **HP:0001712** Left ventricular hypertrophy | variable | max WT 18–21 mm reported | Progressive | Very frequent | PMID:22957257 (max WT 21 mm); PMID:26443374 (18±3 mm) |
| Asymmetric septal hypertrophy | **HP:0001670** Asymmetric septal hypertrophy (also **HP:0005144** Ventricular septal hypertrophy) | Adult | Substantial | Progressive | Frequent (R94H, A57G-family phenotype) | PMID:26443374; A57G described in "familial asymmetric septal hypertrophy" families per PMID:33288880 |
| **Mid-ventricular / mid-cavitary hypertrophy with mid-cavity obstruction** | No exact HPO term (nearest: HP:0001712 + **HP:0025445** Abnormal papillary muscle morphology) — **ontology gap worth flagging** | Childhood→adult | Gradients 16→41 mm Hg documented | Progressive/dynamic | The signature CMH8 morphology; 6/13 affected in the original M149V family had mid-LV chamber thickening | PMID:8673105; PMID:12021217; PMID:35288424 |
| Papillary muscle hypertrophy | **HP:0025445** Abnormal papillary muscle morphology (no dedicated hypertrophy term) | — | — | — | Reported | PMID:8673105 (papillary muscle involvement); PMID:35288424 (discussion of Poetter phenotype) |
| Left ventricular apical aneurysm | **HP:6000144** Left ventricular aneurysm | Adult | High-risk feature | Progressive | Single case (first report in MYL3) | PMID:35288424: *"To our knowledge, the presence of a left ventricular apical aneurysm has not been previously reported in literature concerning the MYL3 gene mutation."* |
| Restrictive cardiomyopathy / restrictive physiology | **HP:0001723** Restrictive cardiomyopathy | Childhood (recessive E143K) | Severe | Progressive | Homozygous E143K siblings | PMID:12021217 |
| Dilated cardiomyopathy | **HP:0001644** Dilated cardiomyopathy | Age 6 (transplanted) | Severe | Progressive | Rare; recessive LOF only; ClinGen calls MYL3–DCM *Disputed* | PMID:33288880 |
| Left atrial enlargement | **HP:0031295** Left atrial enlargement | Adult | 54 mm reported | Progressive | Frequent | PMID:22957257 |
| Myofiber disarray | **HP:0031318** Myofiber disarray | — | — | — | Histopathologic hallmark of HCM (assumed for CMH8; MYL3-specific histopathology reported in PMID:23594557) | PMID:23594557 |
| Myocardial fibrosis / late gadolinium enhancement | **HP:0001685** Myocardial fibrosis | Adult | Diffuse LGE | Progressive | Reported | PMID:35288424 (*"diffuse delayed gadolinium enhancement"*) |
| Cardiomegaly | **HP:0001640** Cardiomegaly | — | — | — | Secondary | General HCM |

### 3.2 Functional / hemodynamic and arrhythmic phenotypes

| Phenotype | HPO term | Notes / evidence |
|---|---|---|
| Left ventricular diastolic dysfunction | **HP:0025168** | Grade II diastolic dysfunction reported (PMID:35288424) |
| Left ventricular systolic dysfunction | **HP:0025169** | EF 49–50%, mild-to-moderate LVSD (PMID:35288424) |
| Congestive heart failure | **HP:0001635** | NYHA class III CHF; BNP 4394 pg/mL (PMID:35288424) |
| Increased circulating brain natriuretic peptide | **HP:0033534** | Same case |
| Ventricular tachycardia (non-sustained) | **HP:0004756** | Holter NSVT (PMID:35288424) |
| Atrial fibrillation | **HP:0005110** | Refractory AF/atrial flutter (PMID:35288424) |
| Sudden cardiac death | **HP:0001645** | Recurring theme: *"Mutations in MYL3 … are rare and have been associated with sudden death"* (PMID:22957257); 4 SCD events in family A and 3 in family C (PMID:33288880) |
| Cardiac arrest | **HP:0001695** | Component of SCD |
| Syncope | **HP:0001279** | Notably **absent** in the mid-cavity/aneurysm case (PMID:35288424) |
| Dyspnea / exertional dyspnea | **HP:0002094** | Presenting symptom at age 26 (PMID:33288880); orthopnea (PMID:35288424) |
| Heart murmur | **HP:0030148** (systolic: **HP:0031664**) | Index presentation of a 38-year-old asymptomatic male *"referred because of a murmur"* (PMID:22957257) |
| Palpitations | **HP:0001962** | MedGen HPO annotation for CMH8 |
| Abnormal T-wave | **HP:0005135**; Abnormal EKG **HP:0003115** | MedGen HPO annotations |
| Exercise intolerance | **HP:0003546** | General HCM |
| Chest pain | **HP:0100749** | General HCM |
| Stroke (cardioembolic) | **HP:0001297** | Recurrent CVAs incl. retinal artery occlusion and gangliocapsular/corona radiata infarcts in the apical-aneurysm case (PMID:35288424) |

### 3.3 Extracardiac phenotypes

- **Skeletal muscle involvement:** The founding paper described the ELC/RLC phenotype as *"a rare myopathy in human heart and skeletal muscle"* with *"abnormal skeletal muscle"* (PMID:8673105) — HPO **HP:0003198** Myopathy. This is *not* reproduced in most later cohorts: in the three recessive families, *"Affected individuals from the three families showed no evidence of muscle weakness by neurological examination or by history."* (PMID:33288880). **Curation guidance: model skeletal myopathy as a rare/variable, historically-reported feature attached specifically to the Poetter alleles, not as a general CMH8 feature.**
- **Horseshoe kidney** in one homozygous E36\* proband (PMID:33288880) — almost certainly coincidental in a consanguineous pedigree; do not curate as a CMH8 phenotype.

### 3.4 Laboratory abnormalities

- Elevated BNP/NT-proBNP (LOINC 30934-4 / 33762-6; HP:0033534) — nonspecific heart-failure marker.
- Troponin elevation is variable and not diagnostic. No CMH8-specific biomarker exists.

### 3.5 Quality-of-life impact

No MYL3-specific PRO data. From the HCM literature that CMH8 patients are enrolled in:
- KCCQ-CSS and HCMSQ-SoB are the validated instruments; obstructive HCM produces clinically meaningful KCCQ deficits reversible with myosin inhibition (KCCQ-CSS +9.1 points vs. placebo, PMID:32871100).
- Peak VO₂ impairment is the objective functional correlate (mean baseline peak VO₂ deficits; +1.7 mL/kg/min treatment effect with aficamten, PMID:38739079).
- The dominant QoL burdens in this genotype specifically are (a) exertional dyspnea from mid-cavity gradient and diastolic dysfunction; (b) anxiety/activity restriction from SCD risk and ICD carriage; (c) stroke-related disability where apical aneurysm/AF coexist (PMID:35288424); (d) for families, the psychological burden of cascade screening in a low-penetrance gene where VUS are common.

---

## 4. Genetic / Molecular Information

### 4.1 Gene and protein

- **MYL3**, 3p21.31, ~6 kb, 7 exons; transcript **NM_000258** (variant nomenclature in the literature uses NM_000258.2/.3).
- Protein **P08590**, 195 aa, ventricular/slow-skeletal myosin **essential (alkali) light chain**; contains a **cardiac-specific N-terminal extension (~residues 1–43, disordered)** that binds actin, plus **three EF-hand-like regions (49–86, 128–163, 163–195)** that are structural (the cardiac ELC does not bind Ca²⁺ productively; the "EF-hand Ca²⁺-binding motif" language used in the clinical literature refers to the motif architecture).
- Expression: ventricular myocardium and slow-twitch skeletal muscle (long ELC isoform only in heart): *"Cardiac musculature has been shown to only exhibit the long isoform, and studies have postulated the role of ELC as a modulator of crossbridge kinetics and optimum force production."* (PMID:35288424)
- Suggested GO annotations: **GO:0032036** myosin heavy chain binding; **GO:0003779** actin binding; **GO:0003774** cytoskeletal motor activity; **GO:0005509** calcium ion binding (motif-level); components **GO:0030017** sarcomere, **GO:0032982** myosin filament, **GO:0016460** myosin II complex, **GO:0005859** muscle myosin complex, **GO:0031672** A band.

### 4.2 Reported pathogenic and candidate variants

| Variant (protein) | cDNA | Type | Inheritance | Domain/position | Phenotype | Evidence |
|---|---|---|---|---|---|---|
| **M149V** | — | missense | AD (3-generation family) | conserved residue; lever-arm interface | HCM incl. mid-LV chamber thickening (6/13 affected) | PMID:8673105; biophysics PMID:36509720 |
| **R154H** | — | missense | AD (de novo/family) | — | Young boy with massive mid-cavity chamber obstruction | PMID:8673105 |
| **E143K** | — | missense (charge reversal) | **AR (homozygous)** | EF-hand region 2 | Childhood-onset mid-cavitary hypertrophy + restrictive physiology in 3 siblings | PMID:12021217; mouse PMID:28371863 |
| **A57D** | c.170C>A (rs139794067) | missense | AR (homozygous; VUS by ACMG) | EF-hand Ca²⁺-binding motif | Recessive HCM + SCD family history (family A) | PMID:33288880; **contradicted functionally** by PMID:29914921 |
| **E36\*** | c.106G>T | nonsense (LOF) | **AR (homozygous)** | truncates 159 C-terminal aa | Infantile DCM, transplant at age 6; sibling SCD age 2 | PMID:33288880 |
| **c.482-1G>A** | — | essential splice acceptor (LOF) | AR (presumed homozygous) | exon 5 skipping → p.(Gly161_Glu186del); disrupts EF-hands 2 and 3 | Unclassified cardiomyopathy age 2.5, SCD age 8 | PMID:33288880 |
| **R94H** | c.281G>A | missense | AD | — | Asymmetric septal hypertrophy, max WT 18±3 mm, **penetrance 88%**, no obstruction | PMID:26443374 |
| **V79I** | — | missense | AD | ELC–myosin lever-arm contact region | Late-onset, low-expressivity HCM; penetrance 40% | PMID:22957257 |
| **E152K** | c.454G>A (exon 4) | missense | AD (heterozygous) | EF-hand region | Mid-cavity obstruction + **LV apical aneurysm** + NSVT + recurrent stroke | PMID:35288424 |
| — | c.530A>G (exon 5) | missense | AD, paternally inherited (father asymptomatic) | — | **Severe progressive infantile HCM at 3 months, fatal** | PMID:23594557 |
| **E56G**, **E177G** | — | missense | AD (reported) | E56G near EF-hand 1; E177G EF-hand 3 | HCM (clinical detail sparse for E56G) | UniProt P08590; function PMID:36509720; PMID:33288880 notes *"No clinical information is available for the p.(Glu56Gly) variant"* |
| **A57G** | — | missense | AD | EF-hand Ca²⁺ motif | Reported in two Korean families and one Japanese patient with *"dominant familial asymmetric septal hypertrophy and a high incidence of SCD"* (as summarized in PMID:33288880); the canonical mouse HCM allele | PMID:33288880; PMID:23748425; PMID:32034976 |

### 4.3 Variant classification, allele frequency, and interpretive caveats

- **ClinVar (2026-08-01):** 517 MYL3 records; only **14** pathogenic/likely pathogenic — i.e., the great majority are VUS/benign. This ratio is the practical clinical problem for this gene.
- **ClinGen Cardiomyopathy VCEP:** 5 MYL3 variant assertions, *predominantly Uncertain Significance*.
- **gnomAD:** c.170C>A (A57D) present on one allele, *"frequency 0.01588%"*; c.106G>T and c.482-1G>A absent from gnomAD and the Greater Middle East Variome; none homozygous in any database (PMID:33288880). The E152K variant was *"not been detected in the ExAC … 1000 Genomes … and gnomAD database"* (PMID:35288424).
- **Somatic vs germline:** exclusively **germline**. No somatic MYL3 disease mechanism is described.
- **A cautionary, curation-relevant contradiction:** the same A57D allele that ClinVar labeled "likely pathogenic" behaved benignly in an isogenic iPSC-CM panel — *"The heterozygous VUS MYL3(170C>A)-iPSC-CMs did not show an HCM phenotype at the gene expression, morphology, or functional levels. Furthermore, genome-edited homozygous VUS MYL3(170C>A)- and frameshift mutation MYL3(170C>A/fs)-iPSC-CMs lines were also asymptomatic, supporting a benign assessment for this particular MYL3 variant."* (PMID:29914921, Circulation 2018, IN_VITRO). PMID:33288880 (zebrafish rescue failure) reaches the opposite conclusion. **This is an ideal `discussions` entry with `kind: KNOWLEDGE_GAP` or a hypothesis-group split (model-system discordance for A57D), and arguably `HUMAN_MODEL_MISMATCH` given the iPSC-vs-zebrafish-vs-human-family divergence.**
- **Dosage:** ClinGen haploinsufficiency score **0** (no evidence, 2015) — yet PMID:33288880 demonstrates that **biallelic** LOF causes disease. The reconciliation is that MYL3 LOF is recessive, not haploinsufficient; the ClinGen score is consistent with, not contradictory to, the recessive LOF data.

### 4.4 Functional consequences (allelic mechanism classes)

Three mechanistically distinct classes should be modeled separately:

1. **Dominant missense — gain of function / hypercontractility.** A57G destabilizes the SRX state and increases available heads: *"The hypercontractile activity of A57G-ELC cross-bridges was manifested by the inhibition of the SRX state, increased number of myosin heads available for interaction with actin, and higher ATPase activity."* (PMID:32034976)
2. **Dominant missense — restrictive/hypercontractile with SRX stabilization.** E143K: *"E143K-myosin had increased duty ratio and binding affinity to actin compared with WT-myosin, increased actin-activated ATPase activity and slower rates of ATP-dependent dissociation of the acto-myosin complex, indicating an E143K-induced myosin hypercontractility."* (PMID:28371863). Paradoxically, at the SRX level the two alleles diverge: *"The HCM-A57G and RCM-E143K mutations had antagonistic effects on the ATP-dependent myosin energetic states, with HCM-A57G cross-bridges fostering the disordered relaxed (DRX) state and the RCM-E143K model favoring the energy-conserving SRX state."* (PMID:34014247)
3. **Recessive loss of function.** *"Our data demonstrate that homozygous MYL3 loss-of-function variants can cause of recessive cardiomyopathy and occurrence of sudden cardiac death, most likely due to impaired or loss of myosin essential light chain function."* (PMID:33288880); and for E143K homozygosity, *"These findings, coupled with previous studies of myosin light chain structure and function in the heart, suggest a loss-of-function disease mechanism."* (PMID:12021217)

Allele-specific biophysics is heterogeneous even among HCM alleles: *"Only the M149V mutation upregulated the actin-activated ATPase activity of S1. All mutations significantly increased the Ca2+-sensitivity of the sliding velocity of thin filaments … while mutations E56G and M149V (but not E177G) reduced the sliding velocity of regulated thin filaments and F-actin filaments almost twice. Therefore, despite the fact that all studied mutations in ELCv are involved in the development of hypertrophic cardiomyopathy, the mechanisms of their influence on the actin–myosin interaction are different."* (PMID:36509720, IN_VITRO)

### 4.5 Structural interface hypothesis (2026)

A cryo-EM-based thick-filament interactome mapping study included 5 MYL3 variants among 233: *"We identified HCM variants residing in 30 molecular interfaces of the complex thick filament interactome, including the two main interfaces of the myosin interacting-heads motif (IHM), and interfaces involving the MHC, essential and regulatory light chains, and cMyBP-C. None of the 21 variants classified as benign were within interfaces. We demonstrated earlier disease onset and adverse outcomes in HCM patients with pathogenic variants within vs. outside of molecular interfaces."* (PMID:42372158, PNAS 2026). This provides a **structure-based risk-stratification hypothesis** directly applicable to MYL3 variant curation.

### 4.6 Epigenetics and chromosomal abnormalities

- **Epigenetics:** No MYL3-specific methylation/histone data. Generic HCM epigenetic remodeling (and one 2025 report of altered myocardial *lactylation* in obstructive HCM, PMID:40281739 — not MYL3-specific) exists. **Not applicable at the CMH8 level; record as a knowledge gap.**
- **Chromosomal abnormalities:** None. MYL3 CNVs are not an established mechanism (ClinGen dosage score 0). Copy-number screening of "minor" HCM genes has low yield (PMID:28771489). **Not applicable.**

---

## 5. Environmental Information

- **Environmental toxicants/radiation/occupational exposure:** No established contribution. CTD contains no curated MYL3–chemical–disease axis relevant to CMH8. **Not applicable.**
- **Lifestyle:** No MYL3-specific data. General HCM guidance (individualized exercise prescription rather than blanket restriction; treat hypertension/obesity; moderate alcohol) is from the 2024 AHA/ACC guideline (PMID:38718139).
- **Infectious agents:** Not applicable — CMH8 is not infection-triggered. (Myocarditis is a differential diagnosis, not an etiologic cofactor.)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (upstream → downstream), suitable for a dismech pathograph

**Node 1 (MOLECULAR, trigger).** *MYL3 variant alters the myosin essential light chain* — either a missense substitution in the N-terminal actin-binding extension / EF-hand regions / lever-arm contact surface, or a LOF allele (nonsense, splice) reducing/abolishing functional ELC.
- GO: GO:0032036 myosin heavy chain binding; GO:0003779 actin binding
- Evidence: PMID:8673105; PMID:33288880

**Node 2 (MOLECULAR).** *Impaired ELC N-terminal tension-sensor function and disrupted N-ELC–actin interaction.* *"HCM-mutant pathology involved an impaired N-ELC tension sensor, disrupted N-ELC-actin interactions, an altered force-pCa relationship, and a destabilized myosin's super-relaxed state."* (PMID:39211545). Mechanistic basis: *"These results support an important role for the N-terminal ELC extension in prepositioning the cross-bridge for optimal force production."* (PMID:21885653)

**Node 3 (MOLECULAR).** *Shift of the myosin SRX↔DRX equilibrium and altered cross-bridge kinetics.* A57G-type alleles inhibit SRX → more heads available → higher ATPase (PMID:32034976); E143K stabilizes SRX yet raises duty ratio and actin affinity (PMID:28371863; PMID:34014247). Also **altered RLC phosphorylation** (≈40% higher in HCM-A57G; ≈2-fold lower in RCM-E143K) (PMID:34014247).
- GO: GO:0016887 ATP hydrolysis activity; GO:0030049 muscle filament sliding

**Node 4 (CELLULAR).** *Increased myofilament Ca²⁺ sensitivity with altered maximal force.* *"Compared with the Tg-WT, there was a significant increase in the Ca²⁺ sensitivity of force (ΔpCa₅₀ ≅ 0.1) and an ~1.3-fold decrease in maximal force per cross section of muscle observed in the mutant preparations."* (PMID:23748425). Confirmed for E56G/M149V/E177G in vitro (PMID:36509720).
- GO: GO:0060048 cardiac muscle contraction; GO:0006936 muscle contraction

**Node 5 (CELLULAR/TISSUE).** *Cardiomyocyte hypercontractility, increased passive tension and myocardial stiffness, impaired relaxation.* *"a significant increase in passive tension in response to stretch was monitored in Tg-A57G vs. Tg-WT strips indicating a mutation-induced myocardial stiffness"* (PMID:23748425); *"augmented active and passive tension measured in skinned papillary muscle fibres"* for E143K (PMID:28371863). Force-transient duration diverges by allele: *"shorter (HCM-A57G) or longer (RCM-E143K) transients measured in electrically stimulated papillary muscles"* (PMID:34014247).
- CL: **CL:0002131** regular ventricular cardiac myocyte / **CL:2000046** ventricular cardiac muscle cell

**Node 6 (MOLECULAR/CELLULAR, parallel).** *Increased energetic demand and metabolic adaptation.* *"proteomic analysis evidenced RCM-dependent metabolic adaptations and higher energy demands"* (PMID:28371863); Δ43 hearts (SRX-stabilized) show *"significantly decreased ATP utilization and low actin-activated myosin ATPase"* (PMID:32034976). This node is the mechanistic bridge to the classic HCM "energy-depletion" hypothesis.

**Node 7 (TISSUE).** *Maladaptive hypertrophic remodeling with interstitial fibrosis and ultrastructural/sarcomeric disarray.* *"the hearts of Tg-A57G mice demonstrated a high level of fibrosis and hypertrophy manifested by increased heart weight-to-body weight ratios"* (PMID:23748425); *"The hearts of mutant-mice demonstrated ultrastructural defects and fibrosis that progressively worsened in senescent animals"* with *"upregulation of stress-response and collagen genes"* (PMID:28371863).
- GO: **GO:0003300** cardiac muscle hypertrophy; **GO:0014898** cardiac muscle hypertrophy in response to stress; CL: **CL:0002548** fibroblast of cardiac tissue; HP:0001685; HP:0031318

**Node 8 (ORGAN).** *Regionally patterned hypertrophy: mid-ventricular segments and papillary muscles → mid-cavity obstruction ± apical aneurysm; or asymmetric septal hypertrophy.* Poetter et al. proposed the mechanistic explanation that the mutations *"disrupt the stretch activation response of the cardiac papillary muscles"* (PMID:8673105) — a still-unresolved but testable hypothesis for why ELC disease is topographically distinctive. Clinically: *"left ventricular hypertrophy at mid-ventricular segments resulting in a mid-cavitary obstruction and a left ventricular apical aneurysm"* (PMID:35288424).
- UBERON: **UBERON:0002084** heart left ventricle; **UBERON:0002494** papillary muscle of heart / **UBERON:0004524** papillary muscle of left ventricle; **UBERON:0002094** interventricular septum

**Node 9 (ORGANISM).** *Diastolic dysfunction ± restrictive physiology, intracavitary gradient, heart failure; arrhythmogenic substrate (fibrosis + aneurysm + hypertrophy) → NSVT/VT → sudden cardiac death; atrial remodeling → AF → cardioembolic stroke.*
- HP:0025168, HP:0001723, HP:0001635, HP:0004756, HP:0001645, HP:0005110, HP:0001297

### 6.2 Mechanism annotations by requested subheading

- **Molecular pathways:** Actomyosin cross-bridge cycling and thick-filament autoinhibition (IHM/SRX) — the primary axis. Downstream: stress-response/hypertrophic signaling with collagen gene upregulation (PMID:28371863). No canonical Wnt/MAPK/mTOR pathway is established as MYL3-specific; treat generic hypertrophic signaling as inferred, not evidenced.
- **Cellular processes:** cardiomyocyte hypertrophy, increased myofilament Ca²⁺ sensitivity, impaired relaxation, myofibrillar disarray, cardiac fibroblast activation/fibrosis, senescence-associated worsening (PMID:28371863 notes progression *"in senescent animals"*).
- **Protein dysfunction:** Neither misfolding nor aggregation. The dominant class is a **functional/allosteric** defect at protein–protein interfaces (ELC–MHC lever arm, N-ELC–actin, thick-filament interfaces: PMID:42372158); the recessive class is **quantitative loss of protein/domain** (truncation; EF-hand 2/3 deletion: PMID:33288880).
- **Metabolic changes:** increased ATP utilization/energy demand in hypercontractile alleles (PMID:32034976; PMID:28371863). Reported proteomic/metabolic adaptation in RCM-E143K hearts. CHEBI:15422 ATP is the relevant chemical entity.
- **Immune involvement:** No autoimmune or immunodeficiency component. Sterile inflammation accompanying fibrosis is plausible but unstudied for MYL3. **Not applicable / knowledge gap.**
- **Tissue damage mechanisms:** myocyte stress/death with replacement fibrosis; ischemia at the level of microvascular supply–demand mismatch in hypertrophied mid-ventricular myocardium (mechanistically expected; not MYL3-specifically demonstrated); apical wall stress from mid-cavity obstruction → aneurysm formation (PMID:35288424).
- **Biochemical abnormalities:** altered actin-activated myosin ATPase, altered myosin duty ratio/actin affinity, altered RLC phosphorylation stoichiometry (PMID:28371863; PMID:34014247; PMID:36509720). No enzyme deficiency, receptor defect, or ion-channel defect.
- **Epigenetic changes:** none characterized (gap).
- **Molecular profiling:** Transcriptomics — *"Gene expression profiles of E143K-hearts supported the histopathology results and showed an upregulation of stress-response and collagen genes"* (PMID:28371863). Proteomics — mutant-specific proteome/metabolic signatures (PMID:28371863; PMID:26668058 proteomic comparison of physiological vs. pathological ELC-mutant remodeling). Structural genomics — cryo-EM thick-filament interactome mapping (PMID:42372158). Metabolomics/lipidomics — **no MYL3-specific data**. Single-cell/spatial transcriptomics — **no MYL3-specific data**. CRISPR/RNAi functional screens — no MYL3 screen; but targeted CRISPR isogenic editing has been applied (PMID:29914921) and a MYL3 knockout hESC line now exists (PMID:40311326).

---

## 7. Anatomical Structures Affected

**Organ level**
- Primary: **heart** (UBERON:0000948), specifically **left ventricle** (UBERON:0002084) with predilection for **mid-ventricular segments** and **papillary muscles** (UBERON:0002494; left-sided UBERON:0004524); **interventricular septum** (UBERON:0002094) in septal-hypertrophy alleles (R94H, A57G).
- Secondary: **left atrium** (UBERON:0002079) — dilation/AF; **brain** (via cardioembolic stroke: retinal artery, gangliocapsular, corona radiata territories — PMID:35288424); lungs (pulmonary congestion); systemic venous congestion.
- Body systems: cardiovascular (primary), central nervous (secondary/embolic), respiratory (secondary), musculoskeletal (rare, historical: slow-twitch skeletal muscle).

**Tissue and cell level**
- **Cardiac muscle tissue** (UBERON:0001133); **cardiac muscle tissue of papillary muscle** (UBERON:0004494) — the tissue in which the ELC "stretch activation" defect was hypothesized.
- Cells: **CL:0002131** regular ventricular cardiac myocyte; **CL:2000046** ventricular cardiac muscle cell; **CL:0000746** cardiac muscle cell (parent); **CL:0002548** fibroblast of cardiac tissue (fibrotic remodeling).
- **Skeletal muscle tissue** (UBERON:0001134), slow-twitch fibers — rare/historical (PMID:8673105); explicitly absent in the recessive families (PMID:33288880).

**Subcellular level**
- **GO:0030017** sarcomere; **GO:0032982** myosin filament; **GO:0016460** myosin II complex; **GO:0005859** muscle myosin complex; **GO:0031672** A band. Mitochondria are implicated only indirectly via energetic demand (GO:0005739 mitochondrion — inferred).

**Localization / lateralization**
- Left-sided and, within the LV, **regional/segmental** (mid-cavity, papillary, or septal) rather than uniform — a distinguishing feature. Right ventricular involvement is not a described feature of CMH8. Apical aneurysm is a focal apical lesion (HP:6000144).

---

## 8. Temporal Development

**Onset**
- Extremely broad: **3 months** (fatal infantile HCM, c.530A>G — PMID:23594557); **age 2–2.5 years** (recessive unclassified cardiomyopathy — PMID:33288880); **age 6** (recessive DCM, transplanted — PMID:33288880); **childhood** (homozygous E143K siblings — PMID:12021217); **26 years** (recessive A57D HCM — PMID:33288880); **38 years** (asymptomatic murmur, V79I — PMID:22957257); **late adult**.
- HPO onset terms: Congenital/Infantile onset **HP:0003593**, Childhood onset **HP:0011463**, Adult onset **HP:0003581** — model as **variable onset**, with a genotype rule of thumb: **biallelic LOF → infantile/childhood onset and severe course; heterozygous missense → adolescent-to-adult onset, often late.**
- Onset pattern: **insidious/chronic**, frequently detected on family screening or incidentally (murmur) before symptoms. Presentation may be abrupt if the first event is SCD or arrhythmia.

**Progression**
- Course: **chronic, progressive**, lifelong; punctuated by episodic arrhythmic events.
- Documented dynamic progression of the mid-cavity gradient: in the Olson family, *"a dynamic progression in peak intracavitary LV gradient from 16 to 41 mm Hg across a span of 2 years"* (reviewed in PMID:35288424) — *"This reported feature demonstrates the potential for dynamic progression of the condition and may well indicate consideration of serial morphological measurements of the structures."*
- Stages (adapted from general HCM staging): (i) genotype-positive/phenotype-negative (subclinical); (ii) classic hypertrophic phase ± obstruction; (iii) adverse remodeling with fibrosis, AF, LGE burden; (iv) end-stage/burnt-out HCM with systolic dysfunction or restrictive physiology → transplant.
- Recessive LOF course is fast and malignant: *"Homozygosity for LOF variants … appear to cause a more severe phenotype resulting in early SCD and fatality"* (PMID:33288880).
- Phenotypic conversion rate (all sarcomere genes, longitudinal family studies): *"the pooled phenotypic conversion across all genes was 15% over an average of ≈8 years of follow-up"* (PMID:37929589).

**Patterns**
- **Remission:** No spontaneous remission. Treatment-induced *phenotypic improvement* (gradient reduction, symptom class, favorable remodeling) is achievable with myosin inhibitors or septal reduction (PMID:32871100; PMID:37639243), but this is disease modification, not remission.
- **Critical periods:** (a) infancy/early childhood for biallelic LOF genotypes — the window for transplant referral; (b) adolescence through the 5th decade — the window of highest arrhythmic risk and the interval in which cascade-screening surveillance must be repeated (mean diagnosis age 38 years, PMID:37929589); (c) periods of hemodynamic stress (pregnancy, new-onset AF).

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **HCM overall:** classically ~1 in 500 (0.2%; 200/100,000); Semsarian et al. argue for a higher true figure once genotype-positive/phenotype-negative individuals and modern imaging are counted — *"For the past 20 years, most data have supported the occurrence of HCM at about 1 in 500 … They suggest that HCM is more common than previously estimated"* (PMID:25814232). The commonly quoted revised figure is ~1 in 200 including subclinical carriers.
- **CMH8 specifically:** no direct prevalence estimate exists. Derivable bounds:
  - Myosin light chain genes (MYL2 + MYL3) account for *"about 1% of cases"* of HCM — *"In conclusion, myosin light chain mutations are a very rare cause of HCM responsible for about 1% of cases."* (PMID:12404107; in that series of 186 HCM patients, **no** MYL3 mutation was found at all).
  - Pediatric HCM: *"mutations in TNNT2, ACTC, MYL3, and TNNI3 accounted for <5% of cases each"* (PMID:20031618; 79 children ≤13 years).
  - Sarcomere detection rate in unselected HCM probands ≈32% (PMID:25611685); ≈34% prevalence of sarcomere variants in clinically diagnosed HCM (PMID:37929589).
  - **Order-of-magnitude estimate for a dismech `Prevalence` record:** if HCM point prevalence ≈200/100,000 and MYL3 explains ≈0.5–1% of HCM, CMH8 point prevalence ≈**1–2 per 100,000** → `prevalence_class: BAND_1_9_PER_100000`, `measure_type: POINT_PREVALENCE`, with `notes` making the derivation explicit. **This is a derived estimate, not a published figure — label it as such.**
- **Incidence:** no published incidence for CMH8. **Not available.**

### 9.2 Inheritance

- **Autosomal dominant** (HP:0000006) — the ClinGen-curated MOI for MYL3–HCM (Definitive, 2021). Classic families: M149V (3 generations), R94H, V79I, E152K.
- **Autosomal recessive** (HP:0000007) — independently established twice: homozygous E143K (PMID:12021217) and homozygous LOF alleles in three consanguineous Iranian families (PMID:33288880). *"we identify homozygous variants in MYL3 in three unrelated families with cardiomyopathies and occurrence of SCD, but no skeletal myopathy. The recessive inheritance of the likely LOF MYL3 variants are associated with a particularly severe phenotype resulting in early SCD and lethality."*
- **Curation guidance:** model **both** `Inheritance` blocks with bound HPO terms (HP:0000006 and HP:0000007), and consider a subtype split (`has_subtypes`: e.g., `AD missense` / `AR LOF`) since onset, severity, morphology and counseling all differ. CMH8 is a legitimate member of a "dominant-and-recessive same-gene" pattern; it is **not** digenic (do not use HP:0010984).
- **Penetrance:** **incomplete and age-dependent**; the lowest of the definitive sarcomere genes at **≈32%** (PMID:37929589). Allele-specific values span the range: **40%** for V79I (*"The penetrance, if we consider this borderline HCM the phenotype of the p.V79I mutation, was 40%, but the mean age of the nonpenetrant mutation carriers is 15, while the mean age of the penetrant mutation carriers is 47"* — PMID:22957257) to **88%** for R94H (*"disease-penetrance of 88%"* — PMID:26443374). Heterozygotes for recessive alleles show 0% penetrance into late adulthood (PMID:12021217).
- **Expressivity:** highly **variable**, intra- and interfamilial — *"this case highlights the marked phenotypic heterogeneity associated with sarcomeric protein mutations both within and between families"* (PMID:23594557); *"a rare cause of HCM with inter- and intrafamilial variability ranging from benign to malignant forms with cardiac failure and SCD"* (PMID:33288880).
- **Genetic anticipation:** none (not a repeat-expansion disorder). **Not applicable.**
- **Germline mosaicism:** not reported for MYL3. **Not available.**
- **Founder effects:** none established. A57G has been reported in two Korean families and a Japanese patient (per PMID:33288880), which is suggestive of recurrence rather than a proven founder allele.
- **Consanguinity:** central to the recessive form — all three recessive families were consanguineous (first or second cousins) (PMID:33288880); and at population scale, homozygous minor-gene variants are ~40× more frequent in the consanguineous Egyptian cohort (PMID:37431535).
- **Carrier frequency:** no published carrier frequency for MYL3 LOF alleles. gnomAD allele counts for the specific LOF variants are 0–1, i.e. ultra-rare. **Not available.**

### 9.3 Population demographics

- **Affected populations:** reported worldwide — USA/Europe (PMID:8673105; PMID:12021217; PMID:22957257 Danish/South African context), **Japan** (PMID:26443374, Kanazawa registry; R94H found in 5 affected relatives + 2 additional registry carriers out of 600), **Korea/Japan** (A57G, via PMID:33288880), **Iran** (recessive, PMID:33288880), **India/UK** (PMID:35288424), **Egypt/North Africa** (homozygous minor-gene variants, PMID:37431535).
- **Geographic distribution of variants:** recessive LOF alleles cluster where consanguinity is common (Middle East, North Africa); no other geographic signature is established.
- **Sex ratio:** No CMH8-specific ratio. General HCM cohorts are male-predominant in ascertainment (SHaRe: *"37% of patients were female"*, PMID:30297972) while genetic testing yield is *"higher in females compared with males"* (PMID:25611685). **Model as no established sex bias for CMH8; report the ascertainment asymmetry as a caveat.**
- **Age distribution:** bimodal by genotype class — infantile/childhood (biallelic LOF, rare severe missense) and adult (heterozygous missense, mean HCM diagnosis ~38 years for sarcomere carriers generally).

---

## 10. Diagnostics

### 10.1 Imaging (the diagnostic core)

- **Transthoracic echocardiography** (NCIT:C16525 Echocardiography Test; LOINC 34552-0 class): unexplained LV wall thickness ≥15 mm (≥13 mm with family history), **with particular attention to mid-ventricular segments and papillary muscles**, resting/provoked **mid-cavity gradient**, absence of LVOT obstruction/SAM, diastolic function grading, left atrial size. In the index mid-cavity case: *"TTE identified biatrial dilation, LV hypertrophy predominantly in the mid-ventricular segments, mid-cavitary rest gradient of 33 mm Hg, mild-to-moderate LV systolic dysfunction, grade II diastolic dysfunction and no evidence of LVOTO or SAM of the mitral valve at rest."* (PMID:35288424)
- **Cardiac MRI with late gadolinium enhancement** (essential in this genotype, because apical aneurysm and mid-cavity obliteration are frequently missed on echo): *"Subsequent cardiac magnetic resonance … detected an EF of 49% with positive morphologies of mid-cavitary HCM, obliterated in systole with flow acceleration in the LV apical aneurysm and diffuse delayed gadolinium enhancement"* (PMID:35288424).
- Provocation (Valsalva, exercise echo) to unmask dynamic gradients; serial imaging is specifically warranted given documented gradient progression (16→41 mm Hg over 2 years).

### 10.2 Electrophysiology and functional testing

- **12-lead ECG** (HP:0003115; abnormal T-waves HP:0005135) — abnormal in most affected and in some borderline carriers: *"Cascade screening revealed a further nine heterozygote mutation carriers, three of whom had ECG and/or echocardiographic abnormalities but did not fulfil diagnostic criteria for HCM."* (PMID:22957257)
- **Ambulatory (Holter) monitoring** — NSVT detection is decisive for ICD decisions: *"Holter analysis revealed sinus rhythm with runs of non-sustained ventricular tachycardia"* (PMID:35288424).
- **Cardiopulmonary exercise testing (peak VO₂)** — functional staging and trial endpoint (PMID:32871100; PMID:38739079).
- Invasive hemodynamics/catheterization when intracavitary vs. valvular/outflow gradients must be separated; coronary angiography to exclude CAD as a cause of apical aneurysm (normal epicardial coronaries documented, PMID:35288424).

### 10.3 Laboratory tests and biomarkers

- **BNP / NT-proBNP** (HP:0033534) for heart-failure staging (BNP 4394 pg/mL in decompensated case, PMID:35288424).
- High-sensitivity troponin — prognostic in HCM generally, not CMH8-specific.
- **No CMH8-specific biochemical biomarker exists.** Biomarker testing is chiefly used to exclude phenocopies: NT-proBNP/troponin, serum/plasma free light chains and immunofixation (AL amyloidosis), alpha-galactosidase A activity and lyso-Gb3 (Fabry disease), CK (metabolic/mitochondrial myopathy), glucose/HbA1c and creatinine (PRKAG2/Danon considerations).
- **FDA/BEST biomarker context:** no qualified biomarker for HCM subtype assignment.

### 10.4 Biopsy / pathology

- Endomyocardial biopsy is not required for diagnosis; when tissue is available (explant, autopsy, or the infantile case), findings are the HCM canon: myocyte hypertrophy, **myofiber disarray (HP:0031318)**, interstitial and replacement fibrosis (HP:0001685), and (per MedGen's HPO annotation set for CMH8) endomyocardial fibrosis. Histopathology was specifically reported in the infantile MYL3 case (PMID:23594557: *"We report on genetic and histopathological findings in a 3-month-old infant presenting with severe progressive HCM"*).

### 10.5 Genetic testing

- **Recommended approach:** multigene **HCM panel** (NCIT:C15709 Genetic Testing) covering at minimum the 8 definitive sarcomere genes (MYBPC3, MYH7, TNNT2, TNNI3, TPM1, ACTC1, MYL2, **MYL3**) plus phenocopy genes; MYL3 is on essentially all commercial HCM panels and on the Genomics England HCM PanelApp green list.
- Yield: *"The detection rate is ~32% among unselected probands, with inconclusive results in an additional 15%"*, and *"An expanded gene panel encompassing more than 50 genes identified only a very small number of additional pathogenic variants beyond those identifiable in our original panels"* (PMID:25611685) — i.e., **do not order oversized panels**; the ClinGen curation exists precisely because *"Of 4191 HCM variants in ClinVar, 31% were in genes with limited or no evidence of disease association"* (PMID:30681346).
- **WES/WGS:** useful in atypical, syndromic, pediatric, or consanguineous presentations. WES identified MYL3 R94H as the sole surviving candidate in a large family (PMID:26443374: *"WES combined with CADD score and HHE gene data may be useful even in HCM"*), and identified all three recessive MYL3 genotypes (PMID:33288880).
- **Single-gene MYL3 testing:** appropriate only for targeted familial variant testing (cascade/site-specific).
- **Homozygosity mapping / segregation analysis in consanguineous families** is essential — recessive MYL3 disease will be misinterpreted as non-informative heterozygosity otherwise (PMID:12021217; PMID:33288880).
- **CMA, karyotype, FISH, mtDNA, repeat-expansion testing:** **not indicated** for CMH8 (no CNV or repeat mechanism; ClinGen dosage score 0). CMA/mtDNA testing belongs to the differential-diagnosis workup of syndromic or mitochondrial LVH, not to MYL3 diagnosis.
- **Functional adjuncts for VUS resolution (research-grade, increasingly clinical):** isogenic CRISPR-edited iPSC-CM panels (PMID:29914921), zebrafish `cmlc1` rescue assays and minigene splicing assays (PMID:33288880), and structural interface mapping (PMID:42372158).

### 10.6 Omics-based diagnostics

- **RNA sequencing:** no clinical role for MYL3; relevant only for splice-variant interpretation (the c.482-1G>A minigene assay is the functional analogue: *"skipping of exon 5 … thereby disrupting the EF-hand Ca2+ binding motifs 2 and 3"*, PMID:33288880).
- **Proteomics / metabolomics / epigenomics / liquid biopsy:** no validated diagnostic application. **Not applicable.**

### 10.7 Clinical criteria and differential diagnosis

- **Diagnostic criteria:** 2024 AHA/ACC/AMSSM/HRS/PACES/SCMR HCM guideline (PMID:38718139, Circulation 2024;149:e1239–e1311) and 2023 ESC Guidelines for the management of cardiomyopathies (PMID:37622657) — unexplained LV wall thickness ≥15 mm (adults; ≥13 mm with family history/positive genotype), or z-score-based criteria in children, in the absence of another cause.
- **Differential diagnosis** (with the discriminating feature):
  - Other sarcomeric HCM (MYH7, MYBPC3, TNNT2, TNNI3, TPM1, ACTC1, MYL2) — genotype; MYL3 favored by mid-cavity/papillary morphology
  - **Apical HCM** and other causes of apical aneurysm (LAD stenosis/prior MI) — coronary imaging (excluded in PMID:35288424)
  - Cardiac amyloidosis (ATTR/AL) — LGE pattern, free light chains, bone scintigraphy
  - Fabry disease, Danon disease, PRKAG2 glycogen storage cardiomyopathy — enzyme/gene testing, conduction disease/WPW
  - Noonan/RASopathy LVH, mitochondrial cardiomyopathy — syndromic features
  - Athlete's heart, hypertensive LVH, aortic stenosis — loading conditions
  - Idiopathic restrictive cardiomyopathy — relevant because homozygous E143K produces restrictive physiology (PMID:12021217)

### 10.8 Screening

- **Cascade family screening** is the highest-yield intervention: *"the finding that one sixth of patients with sarcomeric disease were diagnosed in infancy suggests that current views on pathogenesis and natural history of familial HCM may have to be revised … all first-degree relatives of any child diagnosed with HCM should be offered screening"* (PMID:20031618). Cascade genotyping *"eliminated the need for longitudinal cardiac evaluations in 691 individuals"* with substantial cost savings (PMID:25611685).
- CMH8-specific caveat: with ≈32% penetrance, **genotype-positive/phenotype-negative status is the modal outcome of cascade testing in MYL3 families** — surveillance intervals (typically 1–3 years in children/adolescents, 3–5 years in adults per guideline) must be explained accordingly.
- No newborn screening or population carrier screening for MYL3 exists or is recommended.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

- No CMH8-specific survival curve is published. **Genotype-class stratification is the usable signal:**
  - **Biallelic LOF:** malignant — SCD at ages 2, 5–9 years; transplant at age 6 (PMID:33288880). *"Homozygosity for LOF variants, p.(Glu36Ter) in family B, and likely homozygosity of the splice acceptor variant, c.482-1G>A in family C, appear to cause a more severe phenotype resulting in early SCD and fatality."*
  - **Homozygous E143K:** *"those with two mutant alleles developed severe cardiomyopathy in childhood"*; *"homozygous carriers of a sarcomeric protein defect may have a malignant course"* (PMID:12021217).
  - **Severe pediatric missense:** fatal infantile HCM (PMID:23594557, "Fatal Outcome" MeSH tag).
  - **Heterozygous missense in adults:** ranges from lifelong asymptomatic (nonpenetrant carriers) to SCD; MYL3 variants are noted as *"associated with sudden death"* (PMID:22957257) and *"The majority of reported variants are, however, associated with SCD at a young age"* (PMID:33288880).
- **General sarcomere-positive HCM benchmark (applicable by extension):** *"Patients with pathogenic/likely pathogenic sarcomere mutations had two-fold greater risk for adverse outcomes compared to patients without mutations"*; *"Young HCM patients (20-29 years) had 4-fold higher mortality than the general United States population at a similar age"*; and *"Ventricular arrhythmias occurred in 32% [23%, 40%] of patients <40 years at diagnosis, but in 1% [1%, 2%] >60 years"* (PMID:30297972, SHaRe, n=4591).
- Mortality/DALY figures specific to CMH8 are **not available** (GBD/CDC report HCM at most, not gene-level).

### 11.2 Morbidity and function

- Dominant morbidities: heart failure symptoms, exercise limitation, atrial fibrillation with cardioembolic stroke and its neurological disability, ICD carriage and its complications, anticoagulation-related hemorrhage (an extra-axial hemorrhage extending into the posterior fossa, *"potentially secondary to long-term anticoagulation"*, occurred in the index apical-aneurysm case — PMID:35288424).
- From SHaRe: *"Heart failure and atrial fibrillation were the most prevalent adverse events, although typically not emerging for several years after diagnosis."* (PMID:30297972)
- QoL instruments: KCCQ-CSS, HCMSQ-SoB, SF-36, EQ-5D (no CMH8-specific published scores).

### 11.3 Complications (to curate as downstream nodes)

Mid-cavity obstruction with progressive gradient → **LV apical aneurysm** → apical thrombus, ventricular tachyarrhythmia, thromboembolism, and (in immature aneurysms) rupture (PMID:35288424 discussion of the Maron apical-aneurysm series); atrial fibrillation → stroke; progressive fibrosis → systolic dysfunction/end-stage HCM → transplant; restrictive physiology → low-output heart failure; SCD.

### 11.4 Prognostic factors and biomarkers

- **Genotype/inheritance class:** biallelic LOF ≫ heterozygous missense in severity (PMID:33288880; PMID:12021217). Allele-specific penetrance also differs sharply (88% R94H vs. 40% V79I).
- **Structural position of the variant:** *"We demonstrated earlier disease onset and adverse outcomes in HCM patients with pathogenic variants within vs. outside of molecular interfaces, emphasizing their importance in normal thick filament function and improving risk stratification of patients."* (PMID:42372158) — an emerging, MYL3-inclusive prognostic principle.
- **Age at diagnosis:** *"Patients <40 years old at diagnosis had a 77% … cumulative incidence of the overall composite outcome by age 60, compared to 32% … by age 70 for patients diagnosed >60 years"* (PMID:30297972).
- **Imaging/arrhythmic risk markers driving ICD decisions** (documented in the MYL3 case): SCD in first-degree relatives, NSVT, extensive LGE, LV systolic dysfunction, **LV apical aneurysm** — *"Risk stratification for an implantable cardioverter defibrillator (ICD) was conducted due to the presence of an LV apical aneurysm, NSVT, LVSD, late gadolinium enhancement (LGE) on CMR and SCD in first-degree relatives."* (PMID:35288424)
- Formal tools: HCM Risk-SCD (ESC) and the 2024 AHA/ACC risk-marker approach (PMID:37622657; PMID:38718139). No MYL3-specific calculator.
- **Recovery potential:** hypertrophy/fibrosis are not reversed by current therapy; symptomatic and hemodynamic recovery is achievable (myosin inhibitors, myectomy), and favorable remodeling has been documented with prolonged mavacamten (PMID:37639243 and its long-term follow-up).

---

## 12. Treatment

There is **no MYL3-genotype-specific therapy**. Management follows guideline-directed HCM care (PMID:38718139; PMID:37622657), with two genotype-relevant emphases: (i) **mid-cavity obstruction and apical aneurysm require different surgical/anticoagulation reasoning than subaortic obstruction**, and (ii) the **hypercontractility mechanism established for MYL3 alleles is exactly the target of cardiac myosin inhibitors**, making mavacamten/aficamten mechanistically rational here (though neither trial reported MYL3-stratified results).

### 12.1 Pharmacotherapy

| Treatment | Mechanism | NCIT / CHEBI suggestions | Evidence |
|---|---|---|---|
| **Beta blockers** (metoprolol, bisoprolol, propranolol) | Negative inotropy/chronotropy; reduce dynamic gradient, improve diastolic filling | `treatment_term` NCIT:C15986 Pharmacotherapy; `therapeutic_agent` **NCIT:C29576** Beta-Adrenergic Antagonist / **CHEBI:6904** metoprolol; `therapeutic_modality: SMALL_MOLECULE` | Guideline first line (PMID:38718139) |
| **Non-dihydropyridine calcium channel blockers** (verapamil, diltiazem) | Negative inotropy; improve diastolic function | NCIT:C15986 + **CHEBI:9948** verapamil | Guideline (PMID:38718139) |
| **Disopyramide** | Class IA antiarrhythmic with potent negative inotropy; gradient reduction | NCIT:C15986 + **NCIT:C61730** Disopyramide / **CHEBI:4657** disopyramide | Guideline add-on for obstructive disease (PMID:38718139) |
| **Mavacamten** | **Cardiac myosin ATPase inhibitor** — reduces the number of force-generating heads / hypercontractility (directly antagonizes the SRX→DRX shift shown for A57G-type ELC alleles) | NCIT:C15986 + **NCIT:C174901** Mavacamten; `therapeutic_modality: SMALL_MOLECULE`; `target_mechanisms: INHIBITS` the hypercontractility node | EXPLORER-HCM: *"45 (37%) of 123 patients on mavacamten versus 22 (17%) of 128 on placebo met the primary endpoint (difference +19·4%, 95% CI 8·7 to 30·1; p=0·0005)"*, with post-exercise LVOT gradient −36 mm Hg and pVO₂ +1.4 mL/kg/min (PMID:32871100, NCT03470545). VALOR-HCM week 56 (PMID:37639243) — sustained avoidance of septal reduction therapy |
| **Aficamten** | Next-generation selective cardiac myosin inhibitor | NCIT:C15986 + **NCIT:C179072** Aficamten | SEQUOIA-HCM: *"the mean change in the peak oxygen uptake was 1.8 ml per kilogram per minute … in the aficamten group and 0.0 … in the placebo group (least-squares mean between-group difference, 1.7 ml per kilogram per minute; 95% CI, 1.0 to 2.4; P<0.001)"*; *"The results for all 10 secondary end points were significantly improved"* (PMID:38739079, NCT05186818) |
| **Oral anticoagulation** (DOAC or warfarin) | Stroke prevention in AF and/or apical aneurysm with thrombus risk | NCIT:C15986 + e.g. **CHEBI:2907** warfarin (verify preferred agent per case) | AF management per guideline; the MYL3 apical-aneurysm case required long-term anticoagulation after recurrent CVAs — and illustrates the bleeding trade-off (PMID:35288424) |
| **Antiarrhythmics** (amiodarone, sotalol) / rate control | AF/VT suppression | NCIT:C15986 | Guideline |
| **Heart-failure therapy** in the non-obstructive/end-stage phase (ACEi/ARB/ARNI, beta blocker, MRA, SGLT2i, diuretics) | Standard HF GDMT — used explicitly in the MYL3 case: *"She was diagnosed with New York Heart Association class III congestive cardiac failure and treated with guideline-directed therapy for heart failure."* | NCIT:C15986 | PMID:35288424 |
| **Avoid**: high-dose vasodilators, pure afterload reducers, digoxin, and aggressive diuresis in significant obstruction | Worsen dynamic gradient | — | Guideline (PMID:38718139) |

**Pharmacogenomics:** No MYL3-specific PGx. Relevant general PGx: **CYP2D6** metabolizer status for metoprolol (CPIC guideline) and mavacamten (CYP2C19/CYP3A4 metabolism, with genotype-informed dosing and REMS-mandated echo monitoring for LVEF <50%); **CYP2C9/VKORC1** for warfarin. These are drug-level, not disease-level, annotations.

### 12.2 Advanced therapeutics

- **Gene therapy / gene editing:** none clinical for MYL3. Mechanistically, the mouse cross-genotype data provide a striking, curatable therapeutic hypothesis — deleting the malfunctioning N-terminal ELC sensor rescues the HCM allele but not the RCM allele: *"Removal of the malfunctioning N-ELC sensor led to functional rescue in HCM-truncated mutant hearts. However, the RCM mutation could not be rescued by N-ELC deletion, likely due to its proximity to the myosin motor domain, affecting lever-arm rigidity and myosin function."* (PMID:39211545). NCIT:C15238 Gene Therapy; `therapeutic_modality: GENE_THERAPY` (preclinical only).
- **RNA-based therapies (ASO/siRNA):** none for MYL3. Note that for a recessive LOF genotype, allele-silencing approaches are conceptually inappropriate; gene replacement would be required. Do **not** create an `antisense_oligonucleotide_therapy` conformance for this entry.
- **Cell therapy / immunotherapy / targeted oncology-style therapy:** not applicable.

### 12.3 Surgical and interventional

| Intervention | NCIT | Notes |
|---|---|---|
| **Septal myectomy / extended myectomy** — for mid-cavity obstruction this must be an **extended (mid-ventricular) myectomy ± papillary muscle reorientation**, not a standard subaortic myectomy | **NCIT:C51591** Myectomy (also NCIT:C15329 Surgical Procedure) | Guideline Class 1 at experienced centers for drug-refractory obstruction (PMID:38718139). Anatomically the key genotype-specific point for CMH8 |
| **Alcohol septal ablation** | **NCIT:C80439** Septal Ablation | Alternative to myectomy in selected adults; **generally unsuitable for mid-cavity obstruction** (target septal perforator anatomy does not supply mid-ventricular hypertrophy) |
| **ICD implantation** (primary or secondary prevention) | **NCIT:C80435** Implantable Cardioverter-Defibrillator Placement (device: NCIT:C93238); `therapeutic_modality: DEVICE` | The decisive intervention in this genotype given SCD burden: *"a decision was made for recommendation of an automatic ICD for the purpose of primary prevention of SCD"* (PMID:35288424) |
| **Catheter ablation** / AF management | NCIT:C49236 Therapeutic Procedure | AF was *"refractory to pharmacological and direct current cardioversion"* in the reported case (PMID:35288424) |
| **Apical aneurysm resection / surgical exclusion** | NCIT:C15329 | Selected cases; also LV thrombus management |
| **Heart transplantation** | **NCIT:C15246** Heart Transplantation; `therapeutic_modality: SURGERY` | End-stage disease; performed at age 6 for the homozygous E36\* DCM proband (PMID:33288880) |

### 12.4 Supportive, rehabilitative, and counseling

- Symptom-directed supportive care (NCIT:C15747 Supportive Care); volume/hydration management; sleep-apnea treatment.
- **Cardiac rehabilitation / individualized exercise prescription** (NCIT:C15315 Rehabilitation; NCIT:C15302 Physical Therapy) — the 2024 guideline moved away from blanket exercise restriction toward shared decision-making (PMID:38718139).
- **Genetic counseling** (**NCIT:C15240** Genetic Counseling) — essential and genotype-nuanced: recurrence risk is 50% for dominant alleles but 25% for sibs in recessive families, and *"Recognizing recessive inheritance in children with cardiomyopathy is essential for appropriate family counseling."* (PMID:12021217)

### 12.5 Experimental treatments and trials

- **NCT03470545** — EXPLORER-HCM (mavacamten, phase 3, completed) (PMID:32871100)
- **NCT04349072** — VALOR-HCM (mavacamten in patients referred for septal reduction; week 56 results PMID:37639243) *(NCT number from the trial report; verify against ClinicalTrials.gov before curating as `clinical_trials`)*
- **NCT05186818** — SEQUOIA-HCM (aficamten, phase 3) (PMID:38739079)
- No trial has enrolled by MYL3 genotype; no MYL3-directed gene therapy has entered trials. **Curate trials as HCM-level context with explicit notes that they are not MYL3-stratified.**

### 12.6 Treatment outcomes, adverse effects, and strategy

- Response rates: see EXPLORER-HCM/SEQUOIA-HCM numbers above; both drugs improved symptoms and gradients with adverse-event incidence *"similar in the two groups"* (PMID:38739079).
- Key adverse events to flag: myosin-inhibitor–induced **reduction in LVEF** (requires echocardiographic surveillance and REMS-type programs), disopyramide anticholinergic effects and QT prolongation, beta-blocker fatigue/bradycardia, anticoagulation hemorrhage (documented, PMID:35288424), ICD lead complications and inappropriate shocks.
- Algorithm (obstructive CMH8): beta blocker → verapamil/diltiazem if intolerant → add disopyramide or switch to a myosin inhibitor → septal reduction (extended myectomy for mid-cavity disease) for refractory symptoms; **in parallel and independent of symptoms**, SCD risk stratification with CMR (LGE, apical aneurysm) and Holter, ICD when indicated; anticoagulation on AF/aneurysm-thrombus grounds; cascade genetic testing of relatives.
- Personalized medicine: currently limited to (a) family-specific variant cascade testing, (b) morphology-driven procedure selection, (c) emerging variant-position–based risk stratification (PMID:42372158). MYL3 genotype does **not** yet alter drug choice.

---

## 13. Prevention

- **Primary prevention (of the disease itself):** not possible — the cause is germline. The actionable primary-prevention targets are the *consequences*: SCD (ICD, activity counseling), stroke (anticoagulation in AF/aneurysm), and heart failure (afterload/AF control). For families, **reproductive prevention** is available: genetic counseling, carrier/partner testing in consanguineous families where a recessive LOF allele has been identified, **preimplantation genetic testing (PGT-M)** and prenatal diagnosis. Consanguinity counseling is the single highest-yield population measure for the recessive form (PMID:33288880; PMID:37431535).
- **Secondary prevention (early detection):** **cascade genetic and clinical screening** of first-degree relatives is the core intervention (PMID:20031618; PMID:25611685); serial ECG/echo ± CMR surveillance of genotype-positive/phenotype-negative relatives, with intervals set by age (more frequent through adolescence and early adulthood). Because MYL3 penetrance is only ≈32% and late (PMID:37929589; PMID:22957257), **surveillance cannot be discontinued in adulthood** for a genotype-positive relative.
- **Tertiary prevention (complication prevention in affected individuals):** ICD for SCD; anticoagulation for AF/apical aneurysm; myosin inhibition or myectomy to prevent progressive remodeling; endocarditis prophylaxis is **not** indicated for HCM per se; treat hypertension and sleep apnea; annual reassessment of risk markers.
- **Immunization:** no disease-specific vaccine. Routine influenza/COVID/pneumococcal immunization is advisable in heart failure (general, not CMH8-specific).
- **Behavioral interventions:** individualized exercise prescription (avoid burst/isometric extremes in obstructive disease), avoidance of dehydration and stimulants, weight and blood-pressure management (PMID:38718139).
- **Public-health/environmental interventions:** not applicable, except population-level consanguinity education and improved representation of Middle Eastern/North African populations in reference databases — a documented equity problem for this gene: rare variants in Egyptian patients were *"less likely to be classified as (likely) pathogenic compared with Europeans (40.8% vs. 61.6%, P = 1.6 × 10-5) due to the underrepresentation of Middle Eastern populations in current reference"* resources (PMID:37431535).
- **Prophylaxis:** no pharmacological prophylaxis prevents phenotype conversion in genotype-positive/phenotype-negative carriers (trials of pre-clinical intervention are ongoing in HCM generally; none MYL3-specific).

---

## 14. Other Species / Natural Disease

- **Taxonomy of species with characterized MYL3/ELC biology:**
  - *Homo sapiens* — **NCBITaxon:9606** (MYL3, hgnc:7584)
  - *Mus musculus* — **NCBITaxon:10090** (*Myl3*, **MGI:97268**, chromosome 9, 110,592,746–110,598,870 bp, + strand; 1:1 stringent ortholog of human MYL3; MGI lists 7 mutations/alleles — 5 endonuclease-mediated, 2 targeted — and 20 IMSR strains; MGI links the human MYL3 association to **hypertrophic cardiomyopathy 8, OMIM:608751**)
  - *Danio rerio* — **NCBITaxon:7955** (*cmlc1*, the MYL3 ortholog: *"Cmlc1 shows over 70% homology with human ELC, and is highly expressed in zebrafish ventricle and weakly expressed in the atrium, while cmlc2 is homologous to human myosin regulatory light chain (RLC)"* — PMID:33288880)
  - *Sus scrofa* — **NCBITaxon:9823** (porcine cardiac muscle strips were used for recombinant ELC protein-exchange experiments: PMID:23748425)
  - *Rattus norvegicus* — **NCBITaxon:10116** (1:1 ortholog per MGI)
- **Breed (VBO):** **not applicable** — no breed-associated MYL3 variant is known.
- **Orthologous genes:** mouse *Myl3* (MGI:97268), rat *Myl3*, zebrafish *cmlc1*. (NCBI Gene IDs: human 4634; mouse 17897 — *the mouse Gene ID should be re-verified before curation.*)
- **Natural disease in other species:** **None documented.** A direct OMIA query by gene symbol MYL3 returned **"No phene records found"** (omia.org, queried 2026-08-01). This is a notable contrast to feline HCM, where *MYBPC3* variants (Maine Coon A31P, Ragdoll R820W) are established — **MYL3 has no veterinary counterpart disease**, and this absence is itself worth recording.
- **Veterinary relevance:** none established for MYL3.
- **Comparative pathology / evolutionary conservation:** ELC function is deeply conserved — the zebrafish rescue experiments demonstrate cross-species functional equivalence: *"Thus, MYL3 shows conserved function to cmlc1 in the zebrafish and represents a valid system for testing pathogenic function of MYL3 variants."* (PMID:33288880). The mutated residues are evolutionarily conserved (*"Multiple sequence alignment confirms that the p.(Ala57Asp) substitution affects an evolutionarily conserved residue"*; E143K was *"a highly conserved amino acid that was absent in 150 controls"* — PMID:12021217).
- **Zoonotic potential / cross-species susceptibility:** not applicable (non-transmissible genetic disease).

---

## 15. Model Organisms

### 15.1 Mammalian genetic models (mouse, *Mus musculus*, NCBITaxon:10090)

The University of Miami (Szczesna-Cordary) transgenic series is the definitive MYL3 model resource; all express **human** ventricular ELC transgenes:

| Model | Type | Phenotype recapitulation | Key evidence |
|---|---|---|---|
| **Tg-A57G** (HCM allele) | Transgenic, cardiac-specific human ELC | Increased Ca²⁺ sensitivity of force (ΔpCa₅₀ ≈ 0.1), ~1.3-fold reduced maximal force, increased passive tension/myocardial stiffness, fibrosis, hypertrophy (increased heart/body weight ratio), increased end-systolic elastance (contractility); SRX inhibited with more heads available and higher ATPase; increased RLC phosphorylation (~40%); shortened force transients | PMID:23748425; PMID:32034976; PMID:34014247 |
| **Tg-E143K** (RCM allele) | Transgenic | Diastolic dysfunction with augmented active and passive tension, hypercontractile myosin (increased duty ratio, actin affinity, actin-activated ATPase, slower actomyosin dissociation), reduced RLC phosphorylation, ultrastructural defects and progressive fibrosis worsening with age, upregulated stress-response/collagen genes, reduced cardiac output/stroke work; SRX stabilized; lengthened force transients | PMID:28371863; PMID:34014247 |
| **Tg-Δ43** (N-terminally truncated ELC, residues 1–43 removed) | Transgenic "near-physiological remodeling" control | Hypertrophy with time but *"do not show any abnormalities in cardiac morphology or function"*; SRX stabilized, decreased ATP utilization; shifts cross-bridge mass toward thin filaments (X-ray I₁,₁/I₁,₀ increased 1.3-fold) | PMID:32034976; PMID:21885653 |
| **Tg-WT-ELC** | Transgenic control expressing non-mutated human ventricular ELC | Baseline comparator for all above | PMID:34014247 |
| **A57G × Δ43 and E143K × Δ43 crosses** | Cross-genotype rescue models | *"In A57G×Δ43 mice, Δ43 expression improved heart function and reduced hypertrophy and fibrosis. No improvements were seen in E143K×Δ43"* — allele-class-specific rescue | PMID:39211545 |
| Endonuclease-mediated / targeted *Myl3* alleles (7 total in MGI) | Knockout/targeted | MGI records 5 phenotypes across 2 alleles/3 backgrounds (growth/size/body, immune system, skeleton categories; also an osteoarthritis model) — **notably, no cardiac phenotype is recorded in MGI for the constitutive alleles**; a genuine gap and a caution against assuming a mouse *Myl3*-null cardiac model exists | MGI:97268 |

**Applications:** myofilament mechanics (skinned papillary muscle fibers, force–pCa), small/low-angle X-ray diffraction of filament lattice spacing, SRX/DRX single-nucleotide-turnover assays, in vitro motility, echocardiography and invasive PV-loop hemodynamics, histology/fibrosis quantification, cardiac transcriptomics and proteomics (PMID:26668058), and testing of mechanism-directed rescue.

**Limitations to record explicitly:** (a) transgenic overexpression on a mouse α-MHC background — mouse ventricle is α-MHC-dominant whereas human is β-MHC, altering baseline cross-bridge kinetics; (b) the models capture hypercontractility, stiffness and fibrosis but **do not reproduce the human mid-cavity/papillary hypertrophy morphology or apical aneurysm**, so the topographic signature of CMH8 remains unmodeled; (c) Tg-A57G shows *"a phenotype of eccentric hypertrophy … enhanced left ventricular (LV) cavity dimension without changes in LV posterior/anterior wall thickness"* (PMID:23748425) — i.e., the geometric phenotype diverges from human concentric/segmental HCM; (d) no mouse model of the human **recessive LOF** genotype exists; (e) no mouse model of arrhythmic SCD in ELC disease. **These are strong candidates for `discussions` with `kind: HUMAN_MODEL_MISMATCH`.**

### 15.2 Non-mammalian in vivo model (zebrafish, NCBITaxon:7955)

*cmlc1* morpholino knockdown with human MYL3 mRNA rescue: *"morphants displayed a nonfunctioning heart, characterized by a small ventricle with reduced contractility and a dilated atrium"*; wild-type human MYL3 rescued (ventricular shortening fraction 7.3% → 17.7%, P ≤ 0.001), whereas *"The nonsense-coding variant c.106G>T … was unable to rescue the cmlc1 morphant phenotype"* and c.170C>A gave only partial rescue with no significant improvement in shortening fraction (PMID:33288880). Limitations acknowledged by the authors: transient mRNA expression, mosaic uptake, inability to test splice variants (addressed instead with a minigene assay), and inherent morpholino caveats.

### 15.3 Cellular / in vitro human models

- **Patient-derived and isogenic CRISPR-edited iPSC-CM panel for MYL3 c.170C>A (A57D):** four isogenic lines (corrected control; homozygous VUS; heterozygous frameshift; known pathogenic c.170C>G) assayed for gene expression, sarcomere structure, cell size, contractility, action potentials and calcium handling (PMID:29914921). Result: benign assessment for A57D, pathogenic assessment for c.170C>G — establishing iPSC-CMs as *"a promising VUS risk-assessment tool."* Cell types: **CL:0002131** regular ventricular cardiac myocyte (iPSC-derived); relevant to the repo's MorPhiC-style `category: Cellular` phenotype pattern with `evidence_source: IN_VITRO`.
- **MYL3 knockout hESC line WAe009-A-1H** generated by episomal-vector CRISPR/Cas9 (PMID:40311326) — a new, citable resource for modeling ELC loss of function in human cardiomyocytes (directly relevant to the recessive LOF genotype that has no mouse model).
- **Recombinant protein / protein-exchange biophysics:** porcine cardiac muscle strips exchanged with recombinant A57G or WT ELC (PMID:23748425); recombinant human ELCv E56G/M149V/E177G in myosin S1 ATPase and in vitro motility assays (PMID:36509720).
- **Structural/computational model:** cryo-EM-based atomic model of the human cardiac thick filament used to map 5 MYL3 variants onto molecular interfaces (PMID:42372158; COMPUTATIONAL/structural).

### 15.4 Model resources

MGI (**MGI:97268**), IMSR (20 strains for *Myl3*), IMPC/KOMP (targeted alleles), ZFIN (*cmlc1*), Alliance of Genome Resources, Cellosaurus (for WAe009-A-1H and iPSC lines), Addgene/investigator-held transgenic lines (University of Miami ELC series).

---

## 16. Curation Notes and Recommendations for the dismech Entry

1. **Module conformance.** CMH8 conforms well to **`cardiomyopathy_maladaptive_remodeling`** (`#Ventricular Remodeling` node) — cardiomyocyte insult → remodeling → contractile dysfunction → heart failure. It does **not** primarily conform to `cardiac_ion_channel_repolarization` (this is a structural, not electrical, channelopathy), though the arrhythmic substrate is downstream. The fibrosis arm can reference **`fibrotic_response`** (cardiac fibroblast activation, collagen gene upregulation — PMID:28371863). Consider whether a new **thick-filament hypercontractility / SRX-DRX** module is warranted; it would be shared by MYH7-, MYL2-, MYL3- and MYBPC3-related HCM and would carry the **myosin-inhibitor drug-target pattern** (`target_mechanisms: INHIBITS` on the hypercontractility node for mavacamten/aficamten) — an unusually clean recurrent-mechanism + drug-pattern candidate under the repo's module guidance.
2. **Subtypes.** Recommend `has_subtypes` entries `AD missense` and `AR loss-of-function` (short slug-friendly names), since onset, morphology, severity, penetrance and counseling all diverge; then attach phenotypes/genetics/prognosis records via the `subtype` foreign key.
3. **Inheritance blocks.** Two blocks with bound terms: **HP:0000006** Autosomal dominant inheritance and **HP:0000007** Autosomal recessive inheritance, each with its own PMID-anchored evidence (PMID:8673105 / PMID:12021217 + PMID:33288880). Bind the `term:` — do not leave `preferred_term` alone.
4. **Ontology gap to flag.** There is no HPO term for *mid-cavity (mid-ventricular) obstruction* or *papillary muscle hypertrophy*. Use HP:0001712 + HP:0025445 with a more specific `preferred_term` (the repo explicitly permits a `preferred_term` more granular than `term.label`), and record the gap.
5. **Evidence-source discipline.** Most mechanistic claims are **MODEL_ORGANISM** (transgenic mice) or **IN_VITRO** (motility assays, iPSC-CMs); only the clinical phenotypes, penetrance and epidemiology are **HUMAN_CLINICAL**. Do not let mouse hypercontractility data stand as the sole support for a human phenotype node. PMID:42372158's interface mapping is best tagged **COMPUTATIONAL** (structural modeling on a cryo-EM model) even though it also reports human outcome associations — split into two evidence items if both claims are used.
6. **Model-mismatch discussions worth curating.** (a) A57D: ClinVar "likely pathogenic" vs. benign isogenic iPSC-CM result vs. failed zebrafish rescue (PMID:29914921 vs. PMID:33288880); (b) mouse Tg-A57G eccentric hypertrophy vs. human segmental/concentric HCM; (c) MGI records no cardiac phenotype for constitutive *Myl3* alleles despite a demonstrated human recessive LOF disease; (d) ClinGen haploinsufficiency score 0 (2015) predating the 2021 recessive LOF evidence — a candidate for a `KNOWLEDGE_GAP` note that the dosage curation is stale rather than wrong.
7. **Prevalence record.** Populate structured `Prevalence` slots only; the derived 1–2/100,000 figure must sit in `notes` with its derivation, `prevalence_class: BAND_1_9_PER_100000`, and evidence pointing to PMID:12404107 (≈1% of HCM from MLC genes) plus PMID:25814232 (HCM background prevalence) — **not** a fabricated single-source citation.
8. **Do not curate** as CMH8 features: horseshoe kidney (incidental, PMID:33288880); MYL3–DCM as an established association (ClinGen: **Disputed**) except as the specific recessive-LOF observation; MYL3–ARVC (ClinGen: **Limited**, already handled in `kb/disorders/Arrhythmogenic_Right_Ventricular_Cardiomyopathy.yaml`).

---

## Master Reference List (all verified against PubMed; cached in `references_cache/`)

| PMID | Citation | Evidence type |
|---|---|---|
| 8673105 | Poetter K, et al. Mutations in either the essential or regulatory light chains of myosin are associated with a rare myopathy in human heart and skeletal muscle. *Nat Genet* 1996;13(1):63-9. doi:10.1038/ng0596-63 | HUMAN_CLINICAL + IN_VITRO |
| 12021217 | Olson TM, Karst ML, Whitby FG, Driscoll DJ. Myosin light chain mutation causes autosomal recessive cardiomyopathy with mid-cavitary hypertrophy and restrictive physiology. *Circulation* 2002;105(20):2337-40 | HUMAN_CLINICAL |
| 12404107 | Kabaeva ZT, et al. Systematic analysis of the regulatory and essential myosin light chain genes: genetic variants and mutations in hypertrophic cardiomyopathy. *Eur J Hum Genet* 2002;10(11):741-8 | HUMAN_CLINICAL |
| 11748309 | Andersen PS, et al. Myosin light chain mutations in familial hypertrophic cardiomyopathy: phenotypic presentation and frequency in Danish and South African populations. *J Med Genet* 2001;38(12):E43 (letter; **no abstract available**) | HUMAN_CLINICAL |
| 20031618 | Kaski JP, et al. Prevalence of sarcomere protein gene mutations in preadolescent children with hypertrophic cardiomyopathy. *Circ Cardiovasc Genet* 2009 | HUMAN_CLINICAL |
| 21885653 | Muthu P, et al. Structural and functional aspects of the myosin essential light chain in cardiac muscle contraction. *FASEB J* 2011;25(12):4394-405 | MODEL_ORGANISM/IN_VITRO |
| 22957257 | Andersen PS, et al. A novel myosin essential light chain mutation causes hypertrophic cardiomyopathy with late onset and low expressivity. *Biochem Res Int* 2012;2012:685108 | HUMAN_CLINICAL |
| 23594557 | Jay A, Chikarmane R, Poulik J, Misra VK. Infantile hypertrophic cardiomyopathy associated with a novel MYL3 mutation. *Cardiology* 2013;124(4):248-51 | HUMAN_CLINICAL |
| 23748425 | Kazmierczak K, et al. Discrete effects of A57G-myosin essential light chain mutation associated with familial hypertrophic cardiomyopathy. *Am J Physiol Heart Circ Physiol* 2013;305(4):H575-89 | MODEL_ORGANISM |
| 25295008 | Kazmierczak K, Yuan CC, Liang J, et al. Remodeling of the heart in hypertrophy in animal models with myosin essential light chain mutations. *Front Physiol* 2014 | MODEL_ORGANISM (review) |
| 25611685 | Alfares AA, et al. Results of clinical genetic testing of 2,912 probands with hypertrophic cardiomyopathy: expanded panels offer limited additional sensitivity. *Genet Med* 2015 | HUMAN_CLINICAL |
| 25814232 | Semsarian C, Ingles J, Maron MS, Maron BJ. New perspectives on the prevalence of hypertrophic cardiomyopathy. *J Am Coll Cardiol* 2015;65(12):1249-54 | HUMAN_CLINICAL (review) |
| 26443374 | Nomura A, et al. Whole exome sequencing combined with integrated variant annotation prediction identifies a causative myosin essential light chain variant in hypertrophic cardiomyopathy. *J Cardiol* 2016;67(2):133-9 | HUMAN_CLINICAL |
| 26668058 | Proteomic analysis of physiological versus pathological cardiac remodeling in animal models expressing mutations in myosin essential light chains. *J Muscle Res Cell Motil* 2015 | MODEL_ORGANISM |
| 27532257 | Walsh R, et al. Reassessment of Mendelian gene pathogenicity using 7,855 cardiomyopathy cases and 60,706 reference samples. *Genet Med* 2017;19(2):192-203 | HUMAN_CLINICAL |
| 28371863 | Yuan CC, et al. Hypercontractile mutant of ventricular myosin essential light chain leads to disruption of sarcomeric structure and function and results in restrictive cardiomyopathy in mice. *Cardiovasc Res* 2017;113(10):1124-36 | MODEL_ORGANISM |
| 29914921 | Ma N, et al. Determining the pathogenicity of a genomic variant of uncertain significance using CRISPR/Cas9 and human-induced pluripotent stem cells. *Circulation* 2018;138(23):2666-81 | IN_VITRO |
| 30297972 | Ho CY, et al. Genotype and lifetime burden of disease in hypertrophic cardiomyopathy: insights from the Sarcomeric Human Cardiomyopathy Registry (SHaRe). *Circulation* 2018 | HUMAN_CLINICAL |
| 30681346 | Ingles J, et al. Evaluating the clinical validity of hypertrophic cardiomyopathy genes. *Circ Genom Precis Med* 2019;12(2):e002460 | HUMAN_CLINICAL (curation) |
| 32034976 | Sitbon YH, et al. Ablation of the N terminus of cardiac essential light chain promotes the super-relaxed state of myosin and counteracts hypercontractility in hypertrophic cardiomyopathy mutant mice. *FEBS J* 2020;287(18):3989-4004 | MODEL_ORGANISM |
| 32871100 | Olivotto I, et al. Mavacamten for treatment of symptomatic obstructive hypertrophic cardiomyopathy (EXPLORER-HCM). *Lancet* 2020;396(10253):759-69 (NCT03470545) | HUMAN_CLINICAL (RCT) |
| 33288880 | Osborn DPS, et al. Autosomal recessive cardiomyopathy and sudden cardiac death associated with variants in MYL3. *Genet Med* 2021;23(4):787-92 | HUMAN_CLINICAL + MODEL_ORGANISM |
| 34014247 | Sitbon YH, et al. Cardiomyopathic mutations in essential light chain reveal mechanisms regulating the super relaxed state of myosin. *J Gen Physiol* 2021;153(7):e202012801 | MODEL_ORGANISM |
| 35288424 | Mavilakandy A, Ahamed H. Mutation of the MYL3 gene in a patient with mid-ventricular obstructive hypertrophic cardiomyopathy. *BMJ Case Rep* 2022;15(3):e244573 | HUMAN_CLINICAL (case report) |
| 36509720 | Yampolskaya DS, et al. Properties of cardiac myosin with cardiomyopathic mutations in essential light chains. *Biochemistry (Mosc)* 2022;87(11):1260-7 | IN_VITRO |
| 37431535 | Allouba M, et al. Ethnicity, consanguinity, and genetic architecture of hypertrophic cardiomyopathy. *Eur Heart J* 2023;44(48):5146-58 | HUMAN_CLINICAL |
| 37622657 | Arbelo E, et al. 2023 ESC Guidelines for the management of cardiomyopathies | HUMAN_CLINICAL (guideline) |
| 37639243 | Desai MY, et al. Mavacamten in patients with hypertrophic cardiomyopathy referred for septal reduction: week 56 results from the VALOR-HCM randomized clinical trial. *JAMA Cardiol* 2023 | HUMAN_CLINICAL (RCT) |
| 37929589 | Topriceanu CC, Pereira AC, Moon JC, Captur G, Ho CY. Meta-analysis of penetrance and systematic review on transition to disease in genetic hypertrophic cardiomyopathy. *Circulation* 2024;149(2):107-23 | HUMAN_CLINICAL (meta-analysis) |
| 38718139 | Ommen SR, Ho CY, et al. 2024 AHA/ACC/AMSSM/HRS/PACES/SCMR Guideline for the Management of Hypertrophic Cardiomyopathy. *Circulation* 2024;149(23):e1239-e1311 | HUMAN_CLINICAL (guideline) |
| 38739079 | Maron MS, et al. Aficamten for symptomatic obstructive hypertrophic cardiomyopathy (SEQUOIA-HCM). *N Engl J Med* 2024;390(20):1849-61 (NCT05186818) | HUMAN_CLINICAL (RCT) |
| 39132495 | Hespe S, et al. ClinGen Hereditary Cardiovascular Disease GCEP: Reappraisal of genes associated with hypertrophic cardiomyopathy. *medRxiv* 2024 (published version: *JACC* 2025) | HUMAN_CLINICAL (curation) |
| 39211545 | Sitbon YH, et al. Dual effect of N-terminal deletion of cardiac myosin essential light chain in mitigating cardiomyopathy. *iScience* 2024;27(8):110591 | MODEL_ORGANISM |
| 40311326 | Generation of a MYL3 knockout stem cell line (WAe009-A-1H) by episomal vector-based CRISPR/Cas9 system. *Stem Cell Res* 2025 | IN_VITRO |
| 42372158 | Dutta D, Kim Y, Ho CY, Seidman JG, Seidman CE, Craig R, Padrón R. Thick filament molecular interfaces play a critical role in the pathogenesis of hypertrophic cardiomyopathy. *PNAS* 2026;123(27):e2529234123 | COMPUTATIONAL/structural + HUMAN_CLINICAL |

**Non-literature sources consulted:** OMIM 608751 / 160790 (via MedGen and secondary indexing — omim.org returns HTTP 403 to automated fetches, so OMIM text was **not** read directly and OMIM-attributed statements here are corroborated by MedGen or primary papers); MedGen CUI C1837471; ClinVar E-utilities (517 MYL3 records; 14 P/LP, queried 2026-08-01); ClinGen `search.clinicalgenome.org/kb/genes/HGNC:7584` (gene–disease validity, dosage, VCEP assertions); UniProt REST P08590; MGI:97268; OMIA gene-symbol query (no phene records for MYL3); OAK-verified ontology terms from local HP/CL/CHEBI builds and OLS GO/UBERON/NCIT/MONDO.

**Known gaps in this report:** no direct OMIM full-text read (403); no Orphanet prevalence record obtained (bot gate; no cached ORPHA file); no gnomAD constraint metrics (pLI/o-e) for MYL3 retrieved; no MYL3-stratified outcome, QoL, sex-ratio, or trial-response data exists in the literature; no metabolomic, lipidomic, epigenomic, single-cell or spatial data specific to MYL3; NCBI Gene ID for mouse *Myl3* stated from memory and should be re-verified before curation.

**Sources (web):**
- [OMIM #608751 CMH8](https://omim.org/entry/608751) · [OMIM *160790 MYL3](https://omim.org/entry/160790)
- [MedGen: hypertrophic cardiomyopathy 8](https://www.ncbi.nlm.nih.gov/medgen/?term=hypertrophic+cardiomyopathy+8)
- [ClinGen gene page HGNC:7584 (MYL3)](https://search.clinicalgenome.org/kb/genes/HGNC:7584) · [ClinGen HCM GCEP](https://clinicalgenome.org/affiliation/40008/)
- [ClinVar MYL3](https://www.ncbi.nlm.nih.gov/clinvar/?term=MYL3%5Bgene%5D)
- [UniProt P08590](https://rest.uniprot.org/uniprotkb/P08590.txt)
- [MGI:97268 Myl3](https://www.informatics.jax.org/marker/MGI:97268) · [OMIA](https://www.omia.org/home/)
- [Genomics England PanelApp: MYL3 (HCM)](https://panelapp.genomicsengland.co.uk/panels/49/gene/MYL3/)
- [GeneReviews: Nonsyndromic Hypertrophic Cardiomyopathy Overview](https://www.ncbi.nlm.nih.gov/sites/books/NBK1768/)
- [Olson 2002, Circulation (full text)](https://www.ahajournals.org/doi/10.1161/01.cir.0000018444.47798.94) · [Osborn 2021, Genet Med](https://www.nature.com/articles/s41436-020-01028-2) · [Mavilakandy 2022, BMJ Case Rep](https://pmc.ncbi.nlm.nih.gov/articles/PMC8921845/) · [Sitbon 2021, J Gen Physiol](https://rupress.org/jgp/article/153/7/e202012801/212172/) · [Sitbon 2020, FEBS J (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7888128/)