---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-03T01:44:55.760250'
end_time: '2026-08-03T01:50:28.321393'
duration_seconds: 332.56
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ADPRS-Related Stress-Induced Neurodegeneration
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
  - claude-sonnet-5
  web_search_requests: 20
  num_turns: 32
  total_cost_usd: 2.0204929
  session_id: ccfe4e45-02a4-514e-bba5-3af1e8db647b
  stop_reason: end_turn
citation_count: 25
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ADPRS-Related Stress-Induced Neurodegeneration
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ADPRS-Related Stress-Induced Neurodegeneration** covering all of the
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

# ADPRS-Related Stress-Induced Neurodegeneration (CONDSIAS): Comprehensive Research Report

## 1. Disease Information

### Overview
ADPRS-Related Stress-Induced Neurodegeneration — formally designated **CONDSIAS** (**C**hildhood-**O**nset **N**eurodegeneration, Stress-Induced, with variable **A**taxia and **S**eizures) — is an ultra-rare, autosomal recessive neurodegenerative disorder caused by biallelic loss-of-function variants in *ADPRS* (formerly *ADPRHL2*), which encodes the enzyme **ADP-ribosylhydrolase 3 (ARH3)**. Affected children are typically born after normal early development and then experience progressive, often stepwise neurological deterioration — ataxia, seizures, developmental regression — that is classically triggered or exacerbated by physiologic "stress," most commonly febrile infectious illness, but also surgery, vaccination, or emotional stress [PMC6218634](https://pmc.ncbi.nlm.nih.gov/articles/PMC6218634/).

The disease was first delineated in 2018 by two independent groups publishing back-to-back: Danhauser et al. (9 individuals, 7 families) and Ghosh et al. (further families), both in the *American Journal of Human Genetics* [PMC6218634](https://pmc.ncbi.nlm.nih.gov/articles/PMC6218634/). As of late 2024, approximately **50 cases from ~29 families and 23 distinct variants** have been reported worldwide, making this one of the rarest known Mendelian neurodegenerative disorders [ScienceDirect 2024](https://www.sciencedirect.com/science/article/pii/S266624772400126X).

### Key Identifiers
| Resource | Identifier |
|---|---|
| OMIM Phenotype | **#618170** — Neurodegeneration, Childhood-Onset, Stress-Induced, with Variable Ataxia and Seizures (CONDSIAS) [OMIM 618170](https://omim.org/entry/618170) |
| OMIM Gene | **#610624** — ADP-Ribosylserine Hydrolase; ADPRS (formerly ADPRHL2) [OMIM 610624](https://mirror.omim.org/entry/610624) |
| HGNC | **HGNC:21304** (ADPRS) [GenCC](https://thegencc.org/genes/HGNC:21304) |
| MONDO | **MONDO:0100095** (per OMIM clinical synopsis cross-reference) |
| Orphanet | **ORPHA:494922** (per OMIM clinical synopsis; some sources list a similar ID) |
| UniProt (protein) | **Q9NX46** (ARH3/ADPRHL2/ADPRS) [UniProt](https://www.uniprot.org/uniprotkb/Q9NX46/entry) |
| Gene locus | Chromosome **1p34.1** (per search aggregation; note some database entries list 1p35.3-p34.1) |
| Inheritance | Autosomal recessive |

### Synonyms
- CONDSIAS
- Stress-induced childhood-onset neurodegeneration with variable ataxia and seizures
- ADPRHL2-related neurodegeneration / ADPRHL2 deficiency
- ARH3 deficiency
- "Degenerative pediatric stress-induced epileptic ataxia syndrome" (original 2018 title) [ResearchGate erratum](https://research.vumc.nl/en/publications/erratum-biallelic-mutations-in-adprhl2-encoding-adp-ribosylhydrol)
- Gene synonyms: *ADPRHL2* (older/legacy symbol), ARH3

### Data Source Type
Nearly all clinical knowledge derives from **aggregated case reports and small case series** (individual patients and families identified via whole-exome/genome sequencing), not large-scale EHR or registry data, given the extreme rarity of the condition (<50 cases published cumulatively).

---

## 2. Etiology

### Disease Causal Factors
CONDSIAS is caused exclusively by **biallelic (homozygous or compound heterozygous) pathogenic variants in *ADPRS*** that abolish or severely reduce ARH3 enzymatic activity or protein stability. There is no known non-genetic cause; the disorder is purely Mendelian, but its **clinical expression is stress-gated** — an environmental trigger (infection, fever) is required to precipitate or worsen episodes on the background of the genetic lesion [PMC6218634](https://pmc.ncbi.nlm.nih.gov/articles/PMC6218634/).

### Genetic Risk Factors
- **Causal gene**: *ADPRS* (HGNC:21304), biallelic loss-of-function or severely hypomorphic missense variants.
- Reported pathogenic variant types include: **missense** (e.g., c.1004T>G p.Val335Gly — the most recurrent allele, found in 6 of the original 8 families; c.545A>G p.His182Arg; c.484C>T p.Leu162Pro), **nonsense** (c.1038C>G p.Tyr346Ter; c.580C>T p.Gln194Ter), **frameshift** (c.292delG p.Val98Trpfs*23), **splice-site** (c.309-1G>T; c.803-1G>A), and **in-frame indel** (c.744_746del p.Lys248_Ile249delinsAsn) variants [PMC6218634](https://pmc.ncbi.nlm.nih.gov/articles/PMC6218634/), [PMC9160522](https://pmc.ncbi.nlm.nih.gov/articles/PMC9160522/), [PMC11667697](https://pmc.ncbi.nlm.nih.gov/articles/PMC11667697/).
- **Allele frequency**: The most common recurrent variant (c.1004T>G, p.Val335Gly) was observed **27 times heterozygously among 277,240 gnomAD alleles**, with **no homozygotes reported in population databases** — consistent with the extreme rarity and severity of biallelic loss [PMC6218634](https://pmc.ncbi.nlm.nih.gov/articles/PMC6218634/). This implies a carrier frequency in the general population on the order of ~1 in 10,000, though this is not ancestry-stratified in available sources.
- **Consanguinity** is reported in several families with homozygous variants (e.g., c.1004T>G recurring in Turkish/Middle Eastern families), consistent with a founder or regionally enriched allele.

### Modifier / Susceptibility Considerations
No modifier genes have yet been identified; disease severity instead correlates loosely with variant type (truncating/null alleles trend toward more severe, earlier, and fatal presentations vs. hypomorphic missense alleles, which may present later or with milder/adult-onset phenotypes — see PAMP syndrome below).

### Environmental Risk Factors (Triggers)
The hallmark etiological feature is **stress-triggered exacerbation**:
- Febrile/infectious illness (most common trigger — respiratory infections, diarrheal illness)
- Physical stress (surgery, vaccination)
- Emotional/psychological stress
- The proposed mechanism is that cellular oxidative/genotoxic stress during illness increases poly(ADP-ribose) (PAR) generation by PARP1, which cannot be cleared in ARH3-deficient cells, precipitating a cell-death cascade (see Mechanism, Section 6) [insight.jci.org](https://insight.jci.org/articles/view/124519).

### Protective Factors
None have been established in humans. In model systems, **pharmacological PARP1 inhibition** (see Treatment) acts as a protective/rescue intervention against the downstream consequences of ARH3 loss, suggesting that anything reducing PARP1 activation during stress episodes may be protective — this remains experimental.

### Gene-Environment Interaction
CONDSIAS is a paradigmatic gene-environment interaction disease: the genetic lesion (loss of ARH3) is necessary but the environmental trigger (oxidative/genotoxic stress from infection) is required to unmask cytotoxic PAR accumulation and precipitate clinical episodes — patients can be relatively stable between stress episodes, with stepwise deterioration occurring specifically during/after triggers [PMC6218634](https://pmc.ncbi.nlm.nih.gov/articles/PMC6218634/).

---

## 3. Phenotypes

### Core Neurological Phenotypes (from the founding cohorts, n=12 in Danhauser et al.; expanded across ~50 total cases)

| Phenotype | Frequency (founding cohort) | Suggested HPO term |
|---|---|---|
| Gait abnormality/ataxia | 12/12 (100%) initial; ataxia 10/11 | HP:0002066 (Gait ataxia) / HP:0001251 (Ataxia) |
| Developmental delay/regression | 10/11 | HP:0002376 (Developmental regression) |
| Seizures | 6/12 (variable across cohorts, up to majority in some series) | HP:0001250 (Seizure) |
| Cerebellar atrophy (progressive, on serial MRI) | 8/10 over disease course | HP:0001272 (Cerebellar atrophy) |
| Peripheral axonal neuropathy | 6/8 tested | HP:0003477 (Axonal neuropathy) |
| Nystagmus / diplopia / strabismus | 5/11 | HP:0000639 (Nystagmus), HP:0000486 (Strabismus) |
| Facial myoclonia | 2/12 | HP:0002380 (Facial myoclonus, closest term) |
| Dysarthria/articulation disorder | Reported across series | HP:0001260 (Dysarthria) |
| Tremor | Reported | HP:0001337 (Tremor) |
| Ptosis / ophthalmoplegia | Reported | HP:0000508 (Ptosis), HP:0000602 (Ophthalmoplegia) |
| Sensorineural hearing loss | Reported in subset | HP:0000407 |
| Autism spectrum features | Reported | HP:0000717 |
| Spinal cord atrophy | Reported on imaging | HP:0007344 (approx.) |
| Respiratory insufficiency/failure requiring ventilation | 3/12 initial cohort; recurring theme in later reports (up to tracheostomy dependence) | HP:0002093 (Respiratory insufficiency) |
| Dystonic posturing / dystonia | Reported (e.g., torticollis attacks, truncal dystonia) | HP:0001332 (Dystonia) |
| Muscle weakness / hypotonia | Reported | HP:0001324 / HP:0001252 |

Extended/atypical phenotypes reported in recent expansion papers (2023–2025):
- **Parkinsonism** (truncal dystonia, bradykinesia) emerging in the second decade [PubMed 40493129](https://pubmed.ncbi.nlm.nih.gov/40493129/)
- **Ichthyosis** and **cataracts** — novel extra-neurological associations [PubMed 40493129](https://pubmed.ncbi.nlm.nih.gov/40493129/)
- **Torticollis attacks** as a presenting paroxysmal feature [PMC9175411](https://ncbi.nlm.nih.gov/pmc/articles/PMC9175411)
- **Dystonia and myelopathy**
- Cardiac involvement — **cardiac arrest** in roughly **one-third of homozygous-mutant patients**, described as possibly neurogenic in origin, implicating ARH3 in myocardial function maintenance (echoing the cardiac phenotype in *Arh3* knockout mice) [bioRxiv](https://www.biorxiv.org/content/10.1101/2023.02.07.527369v1.full)

### Phenotype Characteristics
- **Age of onset**: Highly variable — from **14 months to 15 years** across the combined literature, with most cases in early-mid childhood (median around 2–6 years); rarer adult-onset presentations (PAMP syndrome, see below) occur around age 20.
- **Severity**: Variable — ranges from milder ataxia-predominant courses to fulminant fatal presentations with seizures/respiratory failure within months of onset.
- **Progression**: Classically **episodic/stepwise** — periods of relative stability punctuated by acute stress-triggered deterioration, though some patients show more continuous progressive decline.
- **Outcome heterogeneity**: In the founding cohort, 3/12 died in childhood, 5/12 progressed into their teens; later reports document deaths from seizures (within months of onset in the most severe cases) and from respiratory/cardiac arrest during stress episodes.

### Quality of Life Impact
Progressive loss of ambulation, dysarthria, seizures, and (in severe cases) ventilator dependence create substantial functional impairment; no formal EQ-5D/SF-36 data exist given the rarity of the disease, but case reports uniformly describe major impact on mobility, communication, and independence, often culminating in early mortality in the more severe genotypes.

---

## 4. Genetic/Molecular Information

### Causal Gene
- ***ADPRS*** (HGNC:21304; MIM 610624), formerly *ADPRHL2*, located at chromosome 1 (1p34 region per OMIM), encodes **ADP-ribosylhydrolase 3 (ARH3)**.

### Pathogenic Variant Spectrum (compiled across case reports)
| Variant (cDNA) | Protein | Type | Zygosity/Notes |
|---|---|---|---|
| c.1004T>G | p.Val335Gly | Missense | Most recurrent — 6/8 original families; likely founder allele |
| c.545A>G | p.His182Arg | Missense | Active-site residue; causes protein instability/mislocalization [PMC11667697](https://pmc.ncbi.nlm.nih.gov/articles/PMC11667697/) |
| c.484C>T (approx.) | p.Leu162Pro | Missense | Reported in Neurology Genetics 2023 [Neurology Genetics](https://www.neurology.org/doi/10.1212/NXG.0000000000200375) |
| c.1038C>G | p.Tyr346Ter | Nonsense | Truncating |
| c.580C>T | p.Gln194Ter | Nonsense | NMD-predicted; compound het |
| c.292delG | p.Val98Trpfs*23 | Frameshift | Truncating |
| c.744_746del | p.Lys248_Ile249delinsAsn | In-frame deletion | |
| c.309-1G>T | — | Splice-site | Canonical splice acceptor |
| c.803-1G>A | — | Splice-site | Intron 5 retention; compound het |

- **Variant classification**: Reported variants are classified Pathogenic/Likely Pathogenic per ACMG/AMP criteria (PVS1, PM2_Supporting, PS3, PM3 combinations cited in case reports) [PMC9160522](https://pmc.ncbi.nlm.nih.gov/articles/PMC9160522/).
- **Zygosity**: Both homozygous (in consanguineous families or with founder alleles) and compound heterozygous genotypes are reported.
- **Somatic vs. germline**: All reported variants are **germline**.
- **Functional consequence**: Loss-of-function via (a) nonsense-mediated decay/truncation, (b) catalytic inactivation of the di-Mg²⁺ active site, or (c) protein destabilization and mislocalization (loss of nuclear import) as demonstrated for p.His182Arg, which has a protein half-life of ~2.4 hours vs. >8 hours for wild-type, and mislocalizes to cytoplasm only [PMC11667697](https://pmc.ncbi.nlm.nih.gov/articles/PMC11667697/).

### Modifier Genes / Epigenetics
No modifier genes or disease-specific epigenetic (DNA methylation/histone) studies have been reported. However, mechanistically, ARH3 loss causes **abnormal persistence of mono-ADP-ribose ("PAR scars") on core histones** after DNA strand-break repair — an epigenetic-adjacent chromatin mark — described in Fontana et al., *Nature Communications* 2020 [Nature Comms 2020](https://www.nature.com/articles/s41467-020-17069-9).

### Chromosomal Abnormalities
None reported — CONDSIAS is caused by point mutations/small indels, not large structural rearrangements.

---

## 5. Environmental Information

- **Environmental triggers** are central to disease expression rather than causal on their own: febrile/infectious illness (most common), physical stress, and vaccination have all been documented as precipitants of acute deterioration episodes.
- **Infectious agents**: No specific pathogen is causally linked; a broad range of childhood infections (respiratory, gastrointestinal/diarrheal illness) have been documented as triggers in case reports, acting as generic inducers of physiologic/oxidative stress rather than direct pathogens of the nervous system.
- **Lifestyle factors**: Not applicable/described — this is a pediatric-onset monogenic disorder without known lifestyle risk modifiers.

---

## 6. Mechanism / Pathophysiology

### Molecular Function of ARH3
ARH3 (ADP-ribosylhydrolase 3) is a **di-Mg²⁺-dependent, all-α-helical fold hydrolase** (structurally distinct from macrodomain hydrolases like PARG, MacroD2, TARG1) that:
1. **Degrades protein-linked poly(ADP-ribose) (PAR)** synthesized by PARP1/PARP2 during the DNA damage response and oxidative stress [UniProt Q9NX46](https://www.uniprot.org/uniprotkb/Q9NX46/entry), [PNAS](https://www.pnas.org/doi/10.1073/pnas.0606762103).
2. Is the **major serine-specific mono-ADP-ribosylhydrolase** in cells, reversing serine-MARylation [Nature Comms 2017](https://www.nature.com/articles/s41467-017-02253-1).
3. Is uniquely important in **mitochondria**, where it is described as "the only known poly(ADP-ribose)-hydrolyzing enzyme," giving it a non-redundant role in mitochondrial ADP-ribose clearance [PMC6218634](https://pmc.ncbi.nlm.nih.gov/articles/PMC6218634/).
4. Localizes to nucleus, cytoplasm, and mitochondria.

### Causal Chain (Trigger → Clinical Manifestation)
1. **Trigger**: Physiologic stress (infection, fever) → oxidative stress and DNA single-strand breaks in neurons and other cells.
2. **PARP1/PARP2 activation** → massive synthesis of poly(ADP-ribose) (PAR) on nuclear proteins (histones) and elsewhere, as part of normal DNA damage response.
3. **Failure of PAR clearance**: In ARH3-deficient cells, PAR (and mono-ADP-ribose) cannot be degraded — "a ring-shaped signal remained in ADPRHL2-mutant fibroblasts" for hours after H2O2 exposure that normalized within 2 hours in controls [PMC6218634](https://pmc.ncbi.nlm.nih.gov/articles/PMC6218634/).
4. **PAR translocation and AIF release**: Excess PAR translocates from nucleus to cytoplasm and to mitochondria, triggering release of a cleaved, pro-apoptotic form of **apoptosis-inducing factor (AIF)** from mitochondria [insight.jci.org](https://insight.jci.org/articles/view/124519).
5. **Parthanatos**: AIF translocates to the nucleus, activating endonucleases and causing **large-scale DNA fragmentation and chromatin condensation** — this PARP1-dependent, AIF-mediated cell death pathway is termed **parthanatos** [insight.jci.org](https://insight.jci.org/articles/view/124519), [PMC review of parthanatos](https://pmc.ncbi.nlm.nih.gov/articles/PMC11445734/).
6. **Cell death in vulnerable populations**: Neurons (cerebellar Purkinje cells, peripheral axons) and cardiomyocytes appear particularly vulnerable, producing progressive cerebellar atrophy, axonal neuropathy, and in some cases cardiac dysfunction/arrest.
7. **Chromatin "scarring"**: Even sublethal episodes leave persistent mono-ADP-ribose marks on core histones as a molecular memory of prior DNA strand-break repair, potentially compounding cumulative dysfunction with repeated stress episodes [Nature Comms 2020](https://www.nature.com/articles/s41467-020-17069-9).

### Cellular Processes Involved
- DNA damage response / DNA strand-break repair
- Poly- and mono-ADP-ribosylation (PARylation/MARylation) signaling
- Regulated (parthanatic) cell death
- Mitochondrial dysfunction under low-glucose/high-oxidative-phosphorylation conditions — patient fibroblasts show significantly reduced viability specifically when forced toward mitochondrial respiration (galactose/low-glucose media with H2O2 challenge), but not under high-glucose (glycolytic) conditions, implicating **mitochondrial energy stress** as a key vulnerability [PMC6218634](https://pmc.ncbi.nlm.nih.gov/articles/PMC6218634/).

### Suggested GO Terms
- GO:0006471 protein ADP-ribosylation
- GO:0140290 peptidyl-serine ADP-deribosylation (or closest ARH3-specific catalytic activity term)
- GO:0006281 DNA repair
- GO:0006302 double-strand break repair (contextual)
- GO:0097345 mitochondrial outer membrane permeabilization involved in apoptotic signaling pathway (AIF release)
- GO:0006915 apoptotic process (parthanatos as regulated necrosis, GO:0097468 programmed necrotic cell death may also apply)

### Suggested CL Terms
- CL:0000121 Purkinje cell (cerebellar atrophy)
- CL:0000540 neuron (generic, for axonal neuropathy)
- CL:0002305 cardiac myocyte (cardiac phenotype)
- CL:0002573 Schwann cell (peripheral neuropathy, if demyelinating component)

### Functional/Rescue Evidence
- Transduction of ARH3-deficient fibroblasts with **wild-type ADPRHL2 cDNA** restored viability under stress conditions.
- The **PARP1 inhibitor DPQ** rescued cell viability in mutant fibroblasts, directly supporting PAR accumulation as the proximate pathomechanism [PMC6218634](https://pmc.ncbi.nlm.nih.gov/articles/PMC6218634/).
- *Arh3* knockout mouse cardiomyocytes and neurons show increased PAR accumulation and heightened vulnerability to ischemic/oxidative injury, rescued by PARP1 inhibitors veliparib and rucaparib (see Section 15) [insight.jci.org](https://insight.jci.org/articles/view/124519), [bioRxiv rucaparib](https://www.biorxiv.org/content/10.1101/2023.02.07.527369v1.full).

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary**: Central nervous system — cerebellum, spinal cord, cerebral cortex (secondary/late), peripheral nerves.
- **Secondary**: Cardiovascular system (cardiac dysfunction/arrest in ~1/3 of severe homozygotes); respiratory system (neurogenic/muscular respiratory insufficiency); skin (ichthyosis in atypical cases); eye (cataracts, ophthalmoplegia); ear (sensorineural hearing loss).
- **Body systems involved**: Nervous, cardiovascular, respiratory, integumentary (rare), ophthalmologic, auditory.

### Tissue and Cell Level
- Cerebellar cortex/Purkinje cell layer (atrophy)
- Spinal cord (atrophy, myelopathy)
- Peripheral nerve axons (axonal neuropathy)
- Cardiac myocytes (per mouse model and human cardiac-arrest phenotype)
- Skeletal muscle (secondary, from denervation/weakness)

### Subcellular Level
- **Nucleus**: site of PARP1-mediated PARylation and (in wild-type) ARH3-mediated PAR clearance; chromatin/histone ADP-ribose "scarring" (GO Cellular Component: nucleus, chromatin)
- **Mitochondria**: unique non-redundant site of ARH3 PAR-hydrolysis activity; site of AIF release
- **Cytoplasm**: site of PAR translocation and downstream signaling

### Localization / Lateralization
Neurodegeneration is typically **bilateral/symmetric** (cerebellar atrophy, bilateral sensorineural hearing loss, bilateral peripheral neuropathy) — consistent with a systemic metabolic/genotoxic-stress mechanism rather than a focal lesion.

---

## 8. Temporal Development

- **Onset**: Pediatric, typically after a period of normal early development; reported range 14 months to 15 years (most commonly early-to-mid childhood, ~2–6 years). Rare adult-onset variant phenotype (PAMP syndrome, onset ~age 20) also described.
- **Onset pattern**: Acute/subacute — often abrupt deterioration during or shortly after a febrile/infectious illness in a previously well child.
- **Progression**: **Episodic/stepwise** deterioration punctuated by stress triggers, though some patients show more continuously progressive decline; disease course is highly variable even for the same genotype (documented phenotypic variability between siblings/patients sharing the identical mutation) [PMC9175411](https://ncbi.nlm.nih.gov/pmc/articles/PMC9175411).
- **Disease duration**: Ranges from a fulminant course (death within ~4 months of symptom onset in the most severe reported case) to a chronic, multi-decade course with survival into the second/third decade and evolving phenotype (e.g., later parkinsonism).
- **Critical periods**: Each stress/infectious episode represents a "critical period" of vulnerability during which irreversible neurological injury can accrue — this has direct implications for anticipatory/prophylactic management during intercurrent illness.
- **Remission**: No spontaneous disease-modifying remission is described; some acute symptoms (e.g., transient ataxia/psychosis in PAMP syndrome) can partially resolve between episodes, but cumulative injury (atrophy) is typically permanent/progressive.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence/Incidence**: Not formally established — CONDSIAS is documented almost exclusively through individual case reports; approximately **50 cases from ~29 families** reported cumulatively worldwide since 2018 [ScienceDirect 2024](https://www.sciencedirect.com/science/article/pii/S266624772400126X). No population-based prevalence estimate exists; this qualifies as an **ultra-rare disease**.

### Inheritance Pattern
- **Autosomal recessive**. Both homozygous and compound heterozygous genotypes reported.
- **Penetrance**: Appears high among biallelic carriers of null/severely hypomorphic alleles, though clinical **expressivity is highly variable** — even siblings with the identical genotype can show markedly different severity/course [PMC9175411](https://ncbi.nlm.nih.gov/pmc/articles/PMC9175411), [Karger Case Reports Neurol](https://karger.com/crn/article/16/1/188/909784/Clinical-Genetic-and-Pathological-Studies-in-Two).
- **Founder effect**: The recurrent p.Val335Gly (c.1004T>G) allele, seen in 6 of the original 8 families, suggests a founder mutation in certain populations (reported disproportionately in Turkish/Middle Eastern-ancestry families in the literature).
- **Consanguinity**: A recognized risk factor given the homozygous presentations in multiple reported families.
- **Carrier frequency**: Approximately 27/277,240 gnomAD alleles heterozygous for the most common variant alone (~1/10,000), with additional rarer pathogenic alleles contributing to overall carrier burden; population-specific carrier frequency data are not systematically reported.

### Population Demographics
- Reported cases span diverse ancestries, including European, Turkish, Middle Eastern, and Somali/African families [PMC11667697](https://pmc.ncbi.nlm.nih.gov/articles/PMC11667697/).
- **Sex ratio**: No clear sex predilection reported (autosomal recessive; both sexes affected in reported cohorts).
- No specific geographic endemicity beyond scattered founder-allele clusters.

---

## 10. Diagnostics

### Clinical/Laboratory Tests
- No specific diagnostic biomarker or lab test exists; laboratory findings in reported cases are nonspecific (e.g., elevated lactate, abnormal CSF findings, elevated cardiac enzymes during acute episodes) [PMC9160522](https://pmc.ncbi.nlm.nih.gov/articles/PMC9160522/).
- **EEG**: Multifocal spike/epileptiform activity during seizure episodes.
- **Brain/spine MRI**: Progressive cerebellar atrophy (widened cerebellar sulci) is the most consistent imaging finding; spinal cord atrophy also documented; secondary cortical/basal ganglia/corpus callosum changes in advanced/hypoxic-injury cases.
- **Nerve conduction studies/EMG**: Confirm axonal peripheral neuropathy in affected individuals.
- **Cardiac evaluation**: Warranted given reported sudden cardiac arrest risk; echocardiography may show reduced ejection fraction analogous to the mouse model phenotype.

### Genetic Testing
- **Diagnosis is established by molecular genetic testing** identifying biallelic pathogenic *ADPRS* variants — typically via **trio whole-exome sequencing (WES)** given the nonspecific, heterogeneous clinical presentation and extreme rarity [PMC7397971](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7397971/).
- **WES/WGS** are the primary diagnostic modalities in the literature; no dedicated commercial gene panel is described, though *ADPRS* would be expected to be included on comprehensive pediatric neurodegeneration/ataxia gene panels.
- **Functional/RNA studies** (e.g., RNA-seq to confirm splice variant consequences, immunoblotting for protein loss, cellular PAR-accumulation assays) have been used in research settings to confirm variant pathogenicity but are not standard clinical tests.
- Single-gene *ADPRS* Sanger sequencing is appropriate for confirming a suspected/known familial variant or for carrier testing in relatives of an affected proband.

### Clinical Criteria / Differential Diagnosis
No standardized formal diagnostic criteria exist (disease too rare for consensus criteria). Differential diagnosis includes other pediatric-onset progressive ataxia/neurodegeneration syndromes, particularly those with **episodic/stress-triggered decompensation** — e.g., mitochondrial disorders (e.g., Leigh syndrome, POLG-related disease), other DNA-repair disorders (ataxia-telangiectasia, ataxia with oculomotor apraxia), and metabolic decompensation disorders (organic acidemias, urea cycle disorders) — distinguished definitively by *ADPRS* molecular testing.

### Screening
No newborn screening or population carrier screening program currently exists for *ADPRS*/CONDSIAS given its rarity; carrier screening would be relevant in known consanguineous families or those from populations with an identified founder allele, following standard reproductive genetic counseling pathways.

---

## 11. Outcome/Prognosis

- **Mortality**: Substantial — in the founding cohort, 3/12 patients died in childhood; subsequent case reports document deaths from intractable seizures (as early as 4 months after symptom onset in the most severe reported case) and from cardiac arrest/respiratory failure during stress episodes. Approximately **one-third of homozygous ARH3-deficient patients reportedly die of cardiac arrest**, suggested to be neurogenic [bioRxiv](https://www.biorxiv.org/content/10.1101/2023.02.07.527369v1.full).
- **Survival heterogeneity**: Some patients survive into their teens/second decade with progressive but survivable disability; a subset requires long-term ventilatory support (tracheostomy-dependent) [PMC11667697](https://pmc.ncbi.nlm.nih.gov/articles/PMC11667697/).
- **Morbidity**: Progressive loss of ambulation, dysarthria, cognitive decline (variable), seizures, and in advanced cases ventilator dependence.
- **Prognostic factors**: Variant type (truncating/null vs. missense/hypomorphic) appears to influence severity, though genotype-phenotype correlation is imperfect (documented intra-familial variability with identical genotypes). Frequency/severity of stress-triggered episodes appears to drive cumulative disability.
- **Recovery potential**: Partial recovery between acute episodes is described in some milder cases (e.g., transient ataxia/psychosis resolving within months in PAMP syndrome), but cumulative structural injury (cerebellar/spinal atrophy) is generally irreversible.

---

## 12. Treatment

There is **no approved disease-modifying therapy**; management is currently supportive, with an emerging experimental rationale for PARP1-inhibitor repurposing.

### Pharmacotherapy (Investigational/Off-label)
- **PARP1 inhibitors** — the leading mechanistic candidate therapeutic class, based on direct evidence that PARP1 inhibition rescues ARH3-deficient cells and mice from PAR-driven parthanatos:
  - **DPQ** (PARP1 inhibitor) restored viability in patient-derived ARH3-deficient fibroblasts under oxidative stress [PMC6218634](https://pmc.ncbi.nlm.nih.gov/articles/PMC6218634/).
  - **Veliparib** dramatically reduced cerebral infarct size and PAR accumulation in ARH3-deficient mice subjected to brain ischemia [insight.jci.org](https://insight.jci.org/articles/view/124519).
  - **Rucaparib** improved cardiac dysfunction (hypertrophy, reduced ejection fraction, ischemia-reperfusion injury) in *Arh3*-knockout mice [bioRxiv rucaparib](https://www.biorxiv.org/content/10.1101/2023.02.07.527369v1.full).
  - A human case report describes **repurposing doxycycline** (via a proposed anti-neuroinflammatory/mitochondrial-protective mechanism) in a patient with a novel *ADPRHL2* missense mutation, though this is anecdotal [ResearchGate](https://www.researchgate.net/publication/385000152_Repurposing_doxycycline_for_a_case_of_CONDSIAS_Syndrome_with_a_novel_ADPRHL2_missense_mutation).
  - Suggested NCIT term: **NCIT:C1647** (PARP Inhibitor) as a class; specific agents (rucaparib, veliparib) are CHEBI-mappable small molecules (e.g., rucaparib CHEBI:75033; veliparib).
- **Immunomodulatory attempts** (e.g., IVIG/gamma-globulin, corticosteroids) have been tried empirically in acute presentations without clear benefit [PMC9160522](https://pmc.ncbi.nlm.nih.gov/articles/PMC9160522/).

### Supportive and Rehabilitative Care
- Anti-seizure medications for symptomatic seizure control (agent selection not standardized; case reports describe use of various anticonvulsants).
- Physical, occupational, and speech therapy for ataxia/dysarthria/mobility support (NCIT:C15302 Physical Therapy).
- Respiratory support up to and including mechanical ventilation/tracheostomy for neurogenic respiratory insufficiency (NCIT:C15329 category — Surgical/Procedural, e.g., tracheostomy).
- Cardiac monitoring given the recognized risk of cardiac arrest; consideration of proactive cardiology involvement in known homozygotes.
- Aggressive, early treatment of febrile/infectious illness to blunt stress-triggered decompensation (a rational, though unproven, "prophylactic" strategy given the disease's stress-induced mechanism).

### Experimental / Clinical Trials
No registered interventional clinical trials specific to CONDSIAS/*ADPRS* were identified on ClinicalTrials.gov in available sources; management data derive entirely from single-patient case reports and preclinical (mouse/cell) PARP-inhibitor studies. This represents a clear translational gap — repurposing of FDA-approved oncology PARP inhibitors (rucaparib, veliparib, olaparib) for compassionate/off-label use in CONDSIAS is a plausible near-term avenue given the strong preclinical mechanistic rationale, but has not been formally trialed in humans.

### Genetic Counseling
Standard autosomal recessive counseling for parents of an affected child (25% recurrence risk per pregnancy); carrier testing of relatives and reproductive partners recommended in known-variant families; prenatal/preimplantation genetic testing is an option once the familial variant(s) are identified.

---

## 13. Prevention

- **Primary prevention**: Not applicable in the classic sense (monogenic recessive disease); genetic/reproductive counseling and carrier screening in at-risk (consanguineous or founder-allele) families is the primary preventive lever.
- **Secondary prevention**: Early diagnosis via genetic testing in children presenting with unexplained stress-triggered ataxia/seizures allows anticipatory guidance (e.g., aggressive fever/infection management, avoidance of unnecessary physiologic stressors) to potentially blunt acute deteriorations, though this is not evidence-based, only mechanistically plausible.
- **Tertiary prevention**: Prompt supportive management of intercurrent infections, seizure control, and cardiac/respiratory monitoring to minimize stress-triggered morbidity/mortality in known patients.
- **Screening**: No population or newborn screening program exists; targeted carrier screening is appropriate in families with a known pathogenic *ADPRS* allele or from populations bearing an identified founder variant.
- **Prophylaxis**: No established pharmacologic prophylaxis; PARP1 inhibition remains a theoretical/experimental prophylactic strategy pending clinical validation.

---

## 14. Other Species / Natural Disease

- No naturally occurring veterinary/companion-animal disease analog to CONDSIAS has been reported in available sources (unlike some Mendelian diseases with recognized veterinary counterparts).
- **Orthologous gene**: Mouse *Adprs* (Arh3), NCBI Taxon 10090 (*Mus musculus*), MGI:2140364 [MGI](https://www.informatics.jax.org/marker/MGI:2140364) — used extensively for engineered knockout modeling (see below), not natural disease.

---

## 15. Model Organisms

### Mouse Models (the dominant model system for this disease)
- ***Arh3* (Adprs) knockout (KO) mice** — the principal genetic model, generated and characterized across multiple studies:
  - **Neuro/oxidative-stress phenotype**: *Arh3*-KO mouse neurons show sustained PAR elevation after oxidative stress and increased susceptibility to cell death via parthanatos; *in vivo* brain ischemia-reperfusion produces larger infarcts in KO mice, rescued by the PARP1 inhibitor **veliparib** [insight.jci.org, JCI Insight](https://insight.jci.org/articles/view/124519).
  - **Cardiac phenotype**: *Arh3*-KO mice develop **cardiac hypertrophy, reduced ejection fraction, and enhanced susceptibility to myocardial ischemia-reperfusion injury**; heterozygous (*Arh3*-HT) mice show an intermediate phenotype (reduced contractile reserve under dobutamine stress, increased infarct size) — a **gene-dosage effect** paralleling the recognized cardiac-arrest risk in human homozygotes. The PARP1 inhibitor **rucaparib** improved cardiac dysfunction and reduced ischemia-reperfusion injury in this model [bioRxiv, rucaparib Arh3 mice](https://www.biorxiv.org/content/10.1101/2023.02.07.527369.full.pdf).
  - **Molecular/chromatin phenotype**: Patient-derived and *Arh3*-null cells accumulate persistent mono-ADP-ribose "scars" on core histones following DNA strand-break repair, a phenomenon studied mechanistically in Fontana et al. 2020 [Nature Communications](https://www.nature.com/articles/s41467-020-17069-9).

### Cellular / In Vitro Models
- **Patient-derived dermal fibroblasts** are the primary human cellular model used across nearly all published studies — demonstrating impaired PAR clearance after H2O2 challenge, reduced viability under mitochondrial-respiration-forcing (low-glucose) conditions, and rescue by wild-type ADPRHL2 cDNA transduction or PARP1 inhibitor (DPQ) treatment [PMC6218634](https://pmc.ncbi.nlm.nih.gov/articles/PMC6218634/).
- **HEK293/transfection systems** expressing wild-type vs. mutant ARH3-Flag constructs (e.g., H182R) have been used to dissect protein stability, half-life, and subcellular (nuclear vs. cytoplasmic) localization defects [PMC11667697](https://pmc.ncbi.nlm.nih.gov/articles/PMC11667697/).

### Model Characteristics — Recapitulation and Limitations
- The mouse KO model recapitulates the **cardiac** and **cell-death/parthanatos** biochemical phenotype convincingly and has directly informed the PARP-inhibitor therapeutic hypothesis, but a fully penetrant **cerebellar ataxia/seizure/neurodegeneration** phenotype paralleling the human CNS disease has not been prominently reported in these mouse studies as of the literature surveyed here — the mouse work has focused predominantly on ischemia-reperfusion (brain and cardiac) stress-challenge paradigms rather than spontaneous progressive ataxia, representing a translational gap between the human "spontaneous, stress-precipitated, cerebellum-predominant" phenotype and the induced-injury mouse paradigm.
- Patient fibroblasts robustly model the core PAR-clearance defect and stress-conditional viability phenotype but obviously cannot recapitulate CNS-specific vulnerability (e.g., Purkinje cell loss) directly.

### Related Model: *Arh2* (a paralog)
- A related paralog, **ARH2**, has also been studied in knockout mice (cardiac dysfunction, tumorigenesis, inflammation phenotypes), providing comparative insight into the ADP-ribosylhydrolase gene family's role in maintaining genome/organelle integrity, though ARH2 is not itself implicated in human CONDSIAS [bioRxiv Arh2](https://www.biorxiv.org/content/10.1101/2023.02.07.527494.full.pdf).

---

## Summary of Key Evidence Gaps for Curation
1. **No formally validated pathogenicity classification (ClinVar) data or systematic gnomAD carrier-frequency table** could be independently retrieved beyond the single reported allele-count figure — worth verifying directly against gnomAD/ClinVar databases during curation.
2. **Precise Orphanet and MONDO identifiers** should be cross-checked against a live OMIM Clinical Synopsis or Monarch Initiative query (OMIM.org blocked WebFetch in this session; identifiers above were extracted via secondary aggregation and should be confirmed).
3. **No dedicated CONDSIAS clinical trial** exists; the PARP-inhibitor therapeutic rationale is preclinical/case-report level only and should be flagged as an emerging/experimental hypothesis rather than established treatment.
4. **Genotype-phenotype correlation** is documented as imperfect/variable (including intra-familial variability with identical genotype) and should be curated with appropriate hedging.

---

### Sources
- [OMIM #618170 — CONDSIAS](https://omim.org/entry/618170)
- [OMIM #610624 — ADPRS gene](https://mirror.omim.org/entry/610624)
- [Danhauser et al. 2018, AJHG — PMC6218634 (original description)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6218634/)
- [Sharma et al., PMC9160522 — Compound heterozygous ADPRS case report](https://pmc.ncbi.nlm.nih.gov/articles/PMC9160522/)
- [PMC11667697 / ScienceDirect 2024–2025 — ARH3 H182R variant, respiratory failure](https://pmc.ncbi.nlm.nih.gov/articles/PMC11667697/) / [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S266624772400126X)
- [Neurology Genetics 2023 — p.Leu162Pro variant](https://www.neurology.org/doi/10.1212/NXG.0000000000200375)
- [Fontana et al. 2020, Nature Communications — ARH3 chromatin scars](https://www.nature.com/articles/s41467-020-17069-9)
- [JCI Insight — PARP1 inhibition in ARH3-deficient mice/cells](https://insight.jci.org/articles/view/124519)
- [bioRxiv — Rucaparib improves cardiac dysfunction in Arh3-deficient mice](https://www.biorxiv.org/content/10.1101/2023.02.07.527369v1.full)
- [PAMP syndrome — Neurological Sciences 2021 / PubMed 33528672](https://pubmed.ncbi.nlm.nih.gov/33528672/)
- [PubMed 40493129 — Phenotypic diversity: Parkinsonism, ichthyosis, cataract](https://pubmed.ncbi.nlm.nih.gov/40493129/)
- [PMC9175411 — Torticollis attacks, phenotypic variability](https://ncbi.nlm.nih.gov/pmc/articles/PMC9175411)
- [PMC7397971 / BMC Neurology — Novel imaging/clinical phenotypes, frameshift variant](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7397971/)
- [UniProt Q9NX46 — ARH3 protein](https://www.uniprot.org/uniprotkb/Q9NX46/entry)
- [MGI:2140364 — Mouse Adprs gene](https://www.informatics.jax.org/marker/MGI:2140364)
- [GenCC — ADPRS gene-disease curation](https://thegencc.org/genes/HGNC:21304)