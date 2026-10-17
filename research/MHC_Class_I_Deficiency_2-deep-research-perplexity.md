---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-15T14:48:51.954003'
end_time: '2026-10-15T14:52:37.293165'
duration_seconds: 225.34
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: MHC Class I Deficiency 2
  mondo_id: MONDO:0971011
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: low
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 57
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 0
  quotes_valid: 0
  quotes_not_checkable: 1
  relevance_assessed: 18
  on_topic: 4
  validator_version: 0.3.0
term_validation:
  total_terms: 51
  verified: 47
  not_found: 1
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.021
  labels_checked: 1
  labels_matching: 1
  unresolved_terms:
  - HP:0005784
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MHC Class I Deficiency 2
- **MONDO ID:** MONDO:0971011 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MHC Class I Deficiency 2** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

# MHC Class I Deficiency 2 — Comprehensive Disease-Characteristics Report

**Disease:** MHC class I deficiency 2  
**Preferred symbol:** MHC1D2  
**MONDO:** MONDO:0971011  
**Molecular cause:** Biallelic loss-of-function variants in **TAP2**  
**Inheritance:** Autosomal recessive  
**Evidence cutoff:** 15 October 2026

> **Scope note.** “MHC class I deficiency” or “bare lymphocyte syndrome type I” is genetically heterogeneous and can result from **TAP1, TAP2, TAPBP**, or **B2M** defects. This report focuses on the **TAP2-specific entity MHC class I deficiency 2 (OMIM 620813)**. Older literature often combines TAP1- and TAP2-deficient patients because their clinical phenotypes overlap. Where evidence is not TAP2-specific, it is explicitly identified as syndrome-level evidence.

---

## Executive summary

MHC class I deficiency 2 is an exceptionally rare autosomal-recessive inborn error of immunity caused by biallelic **TAP2** loss of function. TAP2 normally heterodimerizes with TAP1 in the endoplasmic-reticulum membrane and uses ATP to transport cytosolic peptides into the ER for loading onto HLA class I molecules. TAP2 deficiency therefore markedly reduces peptide-loaded HLA-A, HLA-B, and HLA-C at the cell surface, alters CD8 T-cell selection and subsets, and changes NK- and unconventional T-cell regulation. [Web source, OMIM record, updated 3 November 2025](https://omim.org/entry/620813) [1][71]

The characteristic clinical spectrum comprises childhood or adolescent-onset chronic bacterial rhinitis, sinusitis, otitis, bronchitis and pneumonia, with possible bronchiectasis and respiratory failure; destructive necrotizing granulomatous lesions of the skin, nose, or upper airway often appear later. However, expressivity is strikingly variable: some homozygotes remain asymptomatic, and recent TAP2 cases have had severe skin disease without pulmonary involvement. [PMID 36227411, published January 2023](https://pubmed.ncbi.nlm.nih.gov/36227411/) [16]

The most informative diagnostic biomarker is **markedly reduced HLA class I surface expression by flow cytometry**, followed by confirmation of biallelic TAP2 variants. Total CD8 counts may be normal and are insufficiently sensitive; naïve CD8-cell enumeration can be more revealing. No disease-specific curative therapy or standardized treatment guideline exists. Management emphasizes rapid treatment and prevention of respiratory infections, airway clearance, vaccination, avoidance of tobacco smoke, and cautious individualized treatment of skin granulomas. Immunosuppression can be dangerous when chronic pulmonary infection or bronchiectasis is present. [PMID 10931128](https://pubmed.ncbi.nlm.nih.gov/10931128/) [61]

---

# 1. Disease information

## 1.1 Definition and identifiers

| Identifier system | Identifier/name | Scope and interpretation |
|---|---|---|
| MONDO | **MONDO:0971011 — MHC class I deficiency 2** | TAP2-specific disease entity; confirmed in NCBI MedGen mapping. [46] |
| OMIM phenotype | **620813 — MHC class I deficiency 2; MHC1D2** | TAP2-specific phenotype, chromosome 6p21.32, autosomal recessive. [1][71] |
| OMIM gene | **170261 — TAP2** | Transporter 2, ATP-binding cassette subfamily B member |
| MedGen | **C5935617; UID 1862135** | MHC class I deficiency 2. [46] |
| Orphanet | **ORPHA:34592 — immunodeficiency by defective expression of MHC class I** | Broader grouping including TAP1-, TAP2-, TAPBP- and B2M-associated disease, not a TAP2-only record. [53] |
| Broad OMIM phenotype series | **PS604571** | Bare lymphocyte syndrome/MHC class I deficiency grouping; not specific to TAP2 |
| MeSH/supplementary concept | **Bare Lymphocyte Syndrome, Type I** | PubMed supplementary concept; associated MeSH headings include Histocompatibility Antigens Class I, Antigen Presentation, and Granuloma. [33] |
| ICD-10 | No dedicated TAP2-specific code | Best represented under an “other specified immunodeficiency” category according to local coding rules; do not infer genotype from ICD coding alone. |
| ICD-11 | No clearly established TAP2-specific leaf code | Use the relevant primary-immunodeficiency/inborn-error-of-immunity category plus molecular diagnosis. |
| Gene | **TAP2**, HGNC:44, UniProt **Q03519** | Located at 6p21.32; encodes antigen peptide transporter 2. [128] |

### Synonyms

| Preferred or alternative name | Qualification |
|---|---|
| MHC class I deficiency 2 | TAP2-specific preferred disease name |
| MHC1D2 | Abbreviation |
| TAP2 deficiency | Molecularly explicit synonym |
| TAP2-associated MHC class I deficiency | Recommended unambiguous descriptive name |
| Bare lymphocyte syndrome type I due to TAP2 deficiency | Common clinical-genetic synonym |
| BLS type I; BLS-I | Broader and potentially ambiguous because TAP1/TAPBP/B2M defects may produce the same syndrome |
| HLA class I deficiency due to TAP2 deficiency | Descriptive synonym |
| TAP deficiency syndrome | Broader term covering TAP1 and TAP2 defects |
| Wegener-like granulomatosis associated with HLA class I deficiency | Historical clinical description; should not be confused with granulomatosis with polyangiitis |

**Important nomenclature warning:** bare lymphocyte syndrome **type I** denotes MHC class I deficiency, whereas bare lymphocyte syndrome **type II** denotes MHC class II deficiency. Occasional papers invert this terminology; molecular designation is safer.

## 1.2 Evidence provenance

The knowledge base should classify most information as **aggregated disease-level evidence** derived from OMIM, Orphanet, MedGen, IUIS classifications, case reports, and small case series. It is not primarily based on population-scale EHR analysis. Patient-level observations exist, but usually involve one family or a few individuals.

OMIM defines MHC1D2 as an autosomal-recessive disorder with first- or second-decade bacterial sinobronchial infection, nasal polyps, later necrotizing granulomatous lesions, bronchiectasis, respiratory failure, and reduced or absent surface MHC I. [OMIM, updated 3 November 2025](https://omim.org/entry/620813) [71]

---

# 2. Etiology

## 2.1 Causal and risk factors

| Factor | Evidence and interpretation |
|---|---|
| Biallelic TAP2 loss-of-function variants | Established primary cause. The landmark report identified a homozygous TAP2 nonsense mutation in affected Moroccan siblings. **PMID: 7517574**, published 8 July 1994. [36][40] |
| Homozygosity/compound heterozygosity | Disease follows autosomal-recessive inheritance; pathogenic alleles are germline. |
| Consanguinity | Increases the probability of homozygous rare variants but is neither necessary nor diagnostically sensitive. |
| Family history | Affected siblings or homozygous asymptomatic relatives support recessive segregation; absence of family history does not exclude disease. |
| Respiratory bacterial exposure | Does not cause the genetic disease but influences infection frequency, chronic airway colonization, bronchiectasis, and severity. |
| Delayed diagnosis/treatment | Permits repeated infection and irreversible airway injury; thus acts as a severity factor. |
| Immunosuppression | May worsen infectious and pulmonary complications and has coincided with severe CNS infections in historical patients. [PMID 10931128](https://pubmed.ncbi.nlm.nih.gov/10931128/) [4] |
| Tobacco smoke and crowded infant settings | Not proven disease-specific causal factors, but experts advise avoidance because they increase respiratory infectious or airway burden. [66] |

No reproducible environmental toxin, occupational exposure, sex-specific factor, GWAS locus, or polygenic risk score is known to cause MHC1D2.

## 2.2 Protective factors

No variant has been validated as genetically protective. The existence of completely asymptomatic homozygotes implies that modifying factors exist, but they remain unidentified. In the 2023 Iranian study, three additional homozygous relatives were asymptomatic despite HLA-I expression of only 4–15% of controls. This is strong human evidence for incomplete clinical penetrance or substantial modifying influences. [PMID 36227411](https://pubmed.ncbi.nlm.nih.gov/36227411/) [33]

Practical protective measures are inferred from immunodeficiency and bronchiectasis care:

- vaccination against respiratory pathogens;
- avoidance of tobacco smoke;
- prompt culture-directed antibiotics;
- airway clearance/chest physiotherapy where secretions or bronchiectasis are present;
- surveillance before irreversible bronchiectasis develops;
- avoidance of unnecessary immunosuppression.

These reduce complications rather than preventing the inherited molecular defect. [61][66]

## 2.3 Gene–environment interaction

The most plausible interaction is:

1. TAP2 deficiency creates constitutively low peptide-loaded HLA-I.
2. Exposure to respiratory bacteria triggers recurrent mucosal infection.
3. Repeated infection and inflammation produce structural airway damage and colonization.
4. Infection-induced cytokines may activate otherwise hyporesponsive NK and γδ T cells.
5. Activated cells encounter autologous tissues with insufficient inhibitory HLA-I and may contribute to destructive granulomatous inflammation.

The final immune-mediated tissue-damage step is biologically supported but not proven in every patient. [108][119]

---

# 3. Phenotypes

Because available cohorts are extremely small and often combine TAP1 and TAP2 deficiencies, frequencies should be stored with the evidence denominator and not treated as stable population estimates.

## 3.1 Clinical phenotype table

| Phenotype/type | Suggested HPO term | Onset, severity, course and frequency | Functional/QOL effect |
|---|---|---|---|
| Recurrent respiratory infections — symptom/clinical history | **Recurrent respiratory infections, HP:0002205** | Usually childhood; chronic or episodic bacterial infections. Present in most historical symptomatic patients, but absent in some recent TAP2 cases. | School/work absence, repeated antibiotics and hospitalization |
| Chronic rhinitis/purulent rhinorrhea — sign | **Chronic rhinitis, HP:0002257** | Often among earliest manifestations, typically within first six years in historical TAP cohorts | Persistent discharge, impaired sleep and smell |
| Chronic/recurrent sinusitis — sign | **Chronic sinusitis, HP:0011109** | Childhood to adolescence; recurrent or persistent | Facial discomfort, impaired breathing, chronic antibiotic burden |
| Recurrent otitis media — sign | **Recurrent otitis media, HP:0000403** | Childhood; may require tympanostomy/myringotomy | Conductive hearing difficulty and developmental impact |
| Nasal polyposis — physical manifestation | **Nasal polyposis, HP:0100582** | Common in classical disease; chronic/progressive | Nasal obstruction and impaired smell |
| Nasal septum ulceration/perforation — physical manifestation | **Nasal septum perforation, HP:0009924** | Usually later, after chronic inflammation; potentially severe | Disfigurement, obstruction, bleeding |
| Chronic bronchitis — sign | **Chronic bronchitis, HP:0004469** | Often appears in the second decade; recurrent/progressive | Cough, sputum and exercise limitation |
| Recurrent bacterial pneumonia — clinical event | **Recurrent pneumonia, HP:0006532** | Childhood/adolescence onward; episodic, variable severity | Hospitalization and risk of permanent lung injury |
| Bronchiectasis — structural complication | **Bronchiectasis, HP:0002110** | Acquired after repeated lower-airway infection; progressive | Chronic cough, sputum, reduced exercise tolerance, respiratory failure risk |
| Respiratory insufficiency/failure — severe complication | **Respiratory insufficiency, HP:0002093** | Advanced disease; not universal | Major disability and possible mortality |
| Necrotizing granulomatous skin disease — physical/pathology finding | **Granulomatous skin inflammation** and **Skin ulcer, HP:0200042** | Often adolescence/adulthood; seven of ten historical TAP-deficient patients had skin lesions, six after age 15. Recent TAP2 cases may present in childhood or adulthood without lung disease. [4] | Pain, wound care, infection risk, scarring, disfigurement, impaired mobility |
| Midfacial destructive granuloma — physical manifestation | **Destructive lesion of the nose/midface** | Slowly progressive; may mimic lethal midline granuloma or granulomatosis with polyangiitis | Severe cosmetic, breathing and psychosocial effects |
| Leukocytoclastic vasculitis/purpura — sign/pathology | **Leukocytoclastic vasculitis, HP:0025403**; **Purpura, HP:0000979** | Uncommon; two of ten in historical combined TAP cohort | Pain, skin breakdown and diagnostic confusion |
| Polyarthritis — sign | **Polyarthritis, HP:0005784** | Uncommon, episodic; historically associated with immune complexes/infection | Pain and restricted mobility |
| Cerebral abscess — complication | **Brain abscess, HP:0032045** | Rare; two CNS infections occurred in immunosuppressed historical patients | Life-threatening neurologic morbidity |
| Retinal vasculitis — sign | **Retinal vasculitis, HP:0008045** | Rare | Vision impairment |
| Reduced surface HLA class I — laboratory abnormality | **Reduced MHC class I expression** | Hallmark; often approximately 1–15% of control but residual expression varies | Diagnostic biomarker rather than subjective disability |
| Reduced naïve CD8 T cells — laboratory abnormality | **Abnormal CD8-positive T-cell number** | Strongly impaired in the 2023 TAP2 series even where total CD8 counts were normal | Reflects impaired cellular immune maturation |
| Low total CD8 T cells — laboratory abnormality | **Decreased CD8-positive T-cell count, HP:0005403** | Frequent but not universal and insufficiently sensitive | Diagnostic clue |
| Expanded γδ T, MAIT or iNKT cells — laboratory abnormality | Use specific immune-cell-count abnormality terms where available | γδ expansion reported historically; MAIT and iNKT elevation reported in 2023 cases | Mechanistic biomarker; clinical significance uncertain |
| Low IgM — laboratory abnormality | **Decreased circulating IgM, HP:0002850** | Reported in recent cohorts/cases but not universal | May increase bacterial susceptibility; requires confirmation |
| Asymptomatic biochemical phenotype | **Clinically asymptomatic** | Documented in homozygotes with severely reduced HLA-I | No current QOL impairment, but surveillance remains appropriate |

In the historical ten-patient TAP1/TAP2 cohort, ENT disease occurred in **10/10**, lower-respiratory disease in **8/10**, and necrotizing skin granulomas in **7/10**. These are syndrome-level, not TAP2-only estimates. [PMID 10931128](https://pubmed.ncbi.nlm.nih.gov/10931128/) [4]

### Recent primary evidence

The 2023 TAP2 paper states:

> “Herein, we described two Iranian cases with 2 and 3 decades of delayed diagnosis of chronic necrotizing granulomatous skin lesions due to TAP2 deficiency without pulmonary involvement.”

It also found HLA-I expression at **4–15% of control**, markedly reduced naïve CD8 cells, and increased MAIT and iNKT cells. [PMID 36227411; online 13 October 2022, issue January 2023](https://pubmed.ncbi.nlm.nih.gov/36227411/) [33]

A 2024 case involved a ten-year-old girl with six asymmetric granulomatous plaques, recurrent otitis, low CD8 cells, low IgM, and no reported pulmonary involvement. Biopsy showed subepidermal granulomatous inflammation with caseating necrosis; extensive testing excluded fungi, Leishmania and mycobacteria. The genotype was a homozygous structural deletion affecting both TAP1 and TAP2, so it is not a pure TAP2-only case. [Published online 25 June 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11437240/) [17]

## 3.2 Quality-of-life evidence

No TAP2-specific EQ-5D, SF-36, PROMIS, or disease-specific QOL study was found. Clinical inference indicates the largest burdens are:

- chronic cough, sputum and exercise intolerance from bronchiectasis;
- repeated hospitalizations and antibiotic courses;
- chronic wound care, pain and secondary infection;
- scarring or midfacial disfigurement;
- hearing and educational impact from recurrent otitis;
- anxiety caused by delayed diagnosis and fear of progression.

These effects should be marked as **clinically inferred**, not formally quantified.

---

# 4. Genetic and molecular information

## 4.1 Causal gene

| Attribute | TAP2 |
|---|---|
| Official symbol | **TAP2** |
| Name | Transporter 2, ATP-binding cassette subfamily B member |
| HGNC | **HGNC:44** |
| OMIM gene | **170261** |
| UniProt | **Q03519** |
| Cytogenetic location | **6p21.32** |
| Protein localization | Multipass endoplasmic-reticulum membrane protein |
| Protein complex | TAP1–TAP2 heterodimer; component/scaffold of the MHC-I peptide-loading machinery |
| Functional consequence in MHC1D2 | Loss of peptide transport and reduced stable cell-surface HLA-I |

The TAP1/TAP2 transporter contains transmembrane peptide-binding/translocation domains and cytosolic nucleotide-binding domains. ATP hydrolysis powers transport of proteasome-derived peptides from cytosol to ER. [125][126]

## 4.2 Reported pathogenic or likely pathogenic variants

The table includes established or recently reported disease alleles identifiable from the retrieved primary/database evidence; it is not a substitute for a current ClinVar or HGMD export.

| Variant | Type/origin | Classification or evidence | Functional consequence/frequency |
|---|---|---|---|
| **p.Arg253Ter (R253X)**; transcript-dependent cDNA nomenclature | Homozygous germline nonsense | Landmark pathogenic TAP2 mutation in Moroccan siblings; **PMID 7517574** | Premature termination and nonfunctional transporter; population frequency expected to be extremely rare. [1][40] |
| **NM_000544.3:c.753dupA; p.Arg252ThrfsTer11** | Homozygous germline frameshift | Reported pathogenic | Truncates TAP2 in/near the transporter domain; population frequency not established. [77] |
| **NM_001290043.2:c.815del; p.Leu272CysfsTer5** | Germline frameshift | ClinVar pathogenic, Variation ID 2164746 | Predicted absent/disrupted protein, probably nonsense-mediated decay; ClinVar cites PMIDs 7517574, 11529920, 12067308 and 23662797. [76] |
| **NM_000544.5:c.1022dupC; p.Ala341fs** | Homozygous germline frameshift | Disease-associated in recent cohort | Disrupts protein between transmembrane domains 7 and 8. [79] |
| **NM_000544.5:c.1569del; p.Gly524ValfsTer14** | Homozygous germline frameshift | Novel disease-associated variant in recent cohort | Predicted nonsense-mediated decay or truncated dysfunctional protein. [79] |
| **NM_001290043.1:c.1_1467+1del**, TAP2 exons 1–7 | Homozygous germline structural deletion | Pathogenic in a 2024 BLS-I case | Part of an approximately 17-kb deletion also involving TAP1 exons 8–11; absent from documented population data. [86] |
| **NM_001290043.2:c.979_983delinsGGGG; p.Arg327GlyfsTer53** | Homozygous germline complex indel/frameshift | Reported in recent TAP2-deficient patients | Loss of function; reported with chronic cutaneous granuloma/rubella investigation. [89] |

### Variant interpretation principles

- The dominant disease mechanism is **loss of function**.
- Most established alleles are nonsense, frameshift, splice-disrupting, or multiexon deletions.
- Variants are inherited and **germline**, not somatic.
- A single heterozygous pathogenic variant is ordinarily insufficient for diagnosis.
- Transcript version must be retained because TAP2 HGVS coordinates differ between transcripts.
- Population frequency should be checked directly in the current gnomAD release during curation; available reports usually describe alleles as absent or exceptionally rare rather than supplying stable frequencies.
- Functional support can include absent TAP2 protein, defective peptide translocation, markedly reduced HLA-I, and restoration of HLA-I after wild-type TAP2 complementation. GenCC cites restoration experiments and classifies the TAP2–disease relationship as strong. [20][103]

## 4.3 Modifier, epigenetic and chromosomal findings

| Category | Current evidence |
|---|---|
| Modifier genes | None validated. HLA haplotype, residual TAP-independent peptide loading, NK receptor repertoire, infection history and other immune variants are plausible modifiers. |
| Protective alleles | None established. |
| Epigenetic signature | No disease-specific DNA-methylation, histone, or chromatin signature has been validated. |
| Large chromosomal abnormalities | No recurrent aneuploidy or translocation causes MHC1D2. Multiexon/contiguous TAP1–TAP2 deletion is possible and requires copy-number-aware testing. |
| Somatic variants | Not an established cause. Acquired TAP2 downregulation can occur in cancer, but that is biologically distinct from germline MHC1D2. |
| Anticipation | Not expected or reported. |
| Mosaicism | Germline or somatic mosaicism has not been established as a recurrent mechanism. |

---

# 5. Environmental information

| Domain | Finding |
|---|---|
| Toxins/radiation/pollution | No specific exposure causes TAP2 deficiency. Air pollution and tobacco smoke may aggravate respiratory morbidity but have not been quantified specifically. |
| Diet/exercise/alcohol | No disease-specific causal or protective association. Adequate nutrition and physical activity should be adapted to lung function and chronic wounds. |
| Respiratory bacteria | Historically cultured organisms include *Haemophilus influenzae*, *Streptococcus pneumoniae*, *Staphylococcus aureus*, *Klebsiella* spp., *Escherichia coli*, and *Pseudomonas aeruginosa*. [4] |
| Viruses | Severe disseminated viral infection was surprisingly uncommon in historical cohorts, possibly owing to compensatory NK/γδ responses and TAP-independent antigen presentation. This does not mean viral infection cannot occur. |
| Rubella virus | Recent work has identified rubella virus in chronic granulomas in some MHC-I-pathway deficiencies, including TAP deficiency; this is a trigger or persistent lesional infection, not the inherited cause. [89] |
| Mycobacteria/fungi/Leishmania | Important differentials for necrotizing granulomas. They were repeatedly excluded in several published lesions, including the 2024 case. [17] |
| Lifestyle | Tobacco avoidance, respiratory hygiene and adherence to airway clearance are rational tertiary-prevention measures. |

---

# 6. Mechanism and pathophysiology

## 6.1 Ordered causal chain

1. **Biallelic germline TAP2 loss-of-function variants lead to** absent, truncated, unstable, or nonfunctional TAP2 protein.
2. **Loss of functional TAP2 leads to** failure or severe dysfunction of the ER-membrane TAP1–TAP2 heterodimer.
3. **TAP dysfunction leads to** deficient ATP-dependent transport of cytosolic proteasome-derived peptides into the ER.
4. **Peptide shortage leads to** inefficient peptide loading and stabilization of HLA-A, HLA-B and HLA-C heavy chain–β2-microglobulin complexes.
5. **Unstable peptide-poor HLA-I leads to** ER retention/degradation and markedly reduced HLA-I surface expression on nucleated cells.
6. **Reduced HLA-I during thymic development leads to** abnormal positive selection and contraction of conventional naïve CD8 αβ T cells.
7. **Impaired HLA-I antigen presentation leads to** deficient conventional cytotoxic-T-cell recognition of selected intracellular and bacterial antigens.
8. **Altered microbial control leads to** recurrent bacterial airway infection and chronic colonization.
9. **Repeated infection leads to** neutrophilic inflammation, airway-wall destruction and bronchiectasis; advanced structural damage can result in respiratory failure.
10. **In parallel, chronically low self-HLA-I leads to** altered NK-cell education and altered γδ T-, MAIT- and iNKT-cell compartments.
11. **Resting NK-cell hyporesponsiveness initially leads to** partial protection from “missing-self” autoreactivity, while infection/cytokine activation can lead to restored or excessive cytotoxicity.
12. **Activated NK and/or Vδ1 γδ T cells acting on HLA-I-low autologous tissue may lead to** destructive granulomatous skin and nasal lesions; this final causal link is **supported but not conclusively demonstrated in every patient**.
13. **Persistent organisms such as rubella virus may branch into** chronic antigenic stimulation within granulomas in some patients, further sustaining tissue inflammation; this is a recently recognized, patient-subset mechanism.

## 6.2 Mechanistic detail and ontology suggestions

| Mechanism | Evidence and cells | Suggested ontology terms |
|---|---|---|
| TAP peptide transport | TAP2/TAP1 form an ATP-binding-cassette heterodimer that transports cytosolic peptides into ER. [121][126] | GO:0015433 ABC-type peptide antigen transporter activity; GO:0046961 proton-transporting ATPase activity is **not** appropriate |
| Antigen processing and presentation | Failure reduces stable peptide–MHC-I complexes | GO:0002474 antigen processing and presentation of peptide antigen via MHC class I |
| ER peptide-loading complex | TAP interacts with tapasin and nascent HLA-I | GO:0005783 endoplasmic reticulum; GO:0033116 endoplasmic-reticulum membrane; GO:0042824 MHC class I peptide-loading complex |
| CD8 T-cell development | Reduced HLA-I changes thymic positive selection, particularly naïve CD8 cells | GO:0045061 thymic T-cell selection; CL:0000625 CD8-positive αβ T cell |
| NK-cell education | Chronic absence of inhibitory self-HLA signals generates resting hyporesponsiveness/unlicensed NK cells | GO:0001775 cell activation; CL:0000623 natural killer cell |
| Cytokine-driven cytotoxicity | IL-2/cytokine activation can restore NK killing, including killing of autologous HLA-I-low fibroblasts | GO:0001910 regulation of leukocyte-mediated cytotoxicity; CL:0000057 fibroblast |
| γδ T-cell expansion | Elevated γδ cells and occasional autoreactive clones documented | CL:0000798 γδ T cell |
| MAIT/iNKT change | Increased MAIT and iNKT counts in the 2023 TAP2 series | CL terms for mucosal-associated invariant T cell and natural killer T cell |
| Chronic granulomatous inflammation | Activated NK/γδ cells and persistent antigen may organize destructive granulomas | GO:0006954 inflammatory response; GO:0002437 inflammatory response to antigenic stimulus |
| Bronchiectasis | Recurrent infection and neutrophilic inflammation cause airway-wall injury | GO:0006955 immune response; GO:0009617 response to bacterium |
| Macrophage contribution | Lung macrophage HLA-I presentation may be important; Tap2-mutant mice show impaired inflammatory macrophage survival | CL:0000235 macrophage; GO:0043066 negative regulation of apoptotic process |

The landmark mechanistic paper reported:

> “Homozygous human TAP peptide transporter mutation in HLA class I deficiency.”

That study established TAP2 mutation as the molecular lesion and showed the connection between defective peptide transport and low HLA-I. **PMID: 7517574**, *Science*, 8 July 1994. [40]

A human TAP2 NK-cell study found “markedly diminished cytotoxicity against class I negative K562 target cells and no detectable autoreactivity,” demonstrating that constitutive HLA-I loss does not simply produce uncontrolled baseline NK killing. **PMID: 11529920**, 2001. [109][111]

## 6.3 Biochemical/metabolic and omics status

- **Biochemical defect:** ATP-dependent peptide translocation, not a conventional small-molecule metabolic deficiency.
- **Energy metabolism:** no systemic metabolic signature established.
- **Transcriptomics/proteomics/metabolomics/lipidomics:** no validated disease-specific diagnostic profile.
- **Single-cell data:** no large disease-specific single-cell atlas was identified; the 2023 deep immunophenotyping study is the closest current cell-resolved clinical analysis.
- **Spatial transcriptomics:** no established MHC1D2 study.
- **CRISPR screens:** general antigen-presentation screens support TAP2 function, but no TAP2-deficiency-specific clinical screen defines prognosis or therapy.
- **Structural biology:** TAP1/TAP2 each contain transmembrane and nucleotide-binding domains; the N-terminal regions support peptide-loading-complex assembly and the core domains mediate peptide transport. [126]

---

# 7. Anatomical structures affected

| Level | Structure/cell/compartment | Suggested ontology |
|---|---|---|
| Primary organ system | Immune system | UBERON:0002405 immune system |
| Upper respiratory tract | Nasal cavity, paranasal sinuses, nasopharynx | UBERON:0001707 nasal cavity; UBERON terms for paranasal sinus |
| Ear | Middle ear | UBERON:0001756 middle ear |
| Lower respiratory tract | Bronchi and lung | UBERON:0002185 bronchus; UBERON:0002048 lung |
| Skin | Dermis/subcutaneous tissues, especially legs, arms and midface | UBERON:0002097 skin; UBERON:0002067 dermis |
| Secondary sites | Brain/CNS, retina, joints, gastrointestinal tract | Rare complications |
| Immune cells | CD8 αβ T cells, NK cells, γδ T cells, MAIT/iNKT cells, macrophages, neutrophils | Relevant CL terms |
| Structural cells | Airway epithelial cells and fibroblasts as targets or damaged tissue | CL:0000066 epithelial cell; CL:0000057 fibroblast |
| Subcellular | ER membrane, cytosolic face of TAP, peptide-loading complex | GO:0005783; GO:0005789; GO:0042824 |
| Cell surface | Plasma-membrane HLA-I is markedly reduced | GO:0005886 plasma membrane |

Skin lesions are frequently asymmetric, so no fixed lateralization applies. Respiratory disease is generally bilateral/systemic rather than unilateral.

---

# 8. Temporal development

| Stage | Typical pattern |
|---|---|
| Molecular onset | Congenital: TAP2 loss is present from conception |
| Presymptomatic interval | Common; some affected people remain well for years or indefinitely |
| Early clinical disease | Purulent rhinitis, sinusitis and otitis may begin in childhood, historically often within the first six years |
| Intermediate disease | Recurrent bronchitis and pneumonia may become prominent in later childhood or the second decade |
| Structural lung disease | Bronchiectasis develops after repeated infections; generally chronic and irreversible |
| Skin/granulomatous phase | Often adolescence or adulthood, although childhood onset occurs |
| Advanced disease | Destructive nasal lesions, extensive skin ulceration, chronic respiratory insufficiency, rarely CNS infection |
| Course | Highly variable: asymptomatic, skin-predominant, lung-predominant, or combined; infections are episodic while established bronchiectasis and scarring are chronic |
| Remission | Infection-related symptoms may improve with antibiotics; ulcers may partially heal but relapse. Structural bronchiectasis does not spontaneously reverse. |
| Critical window | Before bronchiectasis develops: early recognition and aggressive infection control offer the best chance to prevent irreversible pulmonary injury. |

The 2023 cases demonstrate diagnostic delays of **two and three decades**, emphasizing that skin-only disease and normal total CD8 counts can substantially delay recognition. [PMID 36227411](https://pubmed.ncbi.nlm.nih.gov/36227411/) [16]

---

# 9. Inheritance and population

## 9.1 Genetic epidemiology

| Characteristic | Current understanding |
|---|---|
| Inheritance | Autosomal recessive |
| Recurrence risk | If both parents are carriers: 25% affected, 50% carrier, 25% unaffected/noncarrier per pregnancy |
| Penetrance | Molecular/immunologic penetrance appears high for low HLA-I, but **clinical penetrance is incomplete** |
| Expressivity | Extremely variable, including asymptomatic homozygotes and severe pulmonary or cutaneous disease |
| Anticipation | Not reported and biologically unexpected |
| Germline mosaicism | Not established; residual recurrence risk after an apparently de novo finding should be handled conventionally |
| Founder effects | No globally established founder allele; individual consanguineous kindreds may show private homozygous alleles |
| Consanguinity | Enriches homozygosity but is not required |
| Carrier phenotype | Heterozygous carriers are generally clinically unaffected |
| Carrier frequency | Unknown; no reliable population estimate |
| Sex ratio | No established sex bias; both sexes affected |
| Ethnic/geographic distribution | Reported across Moroccan, European, Iranian, Saudi and other families; ascertainment is strongly influenced by access to immunologic/genetic testing |

## 9.2 Prevalence and incidence

No robust population prevalence or annual incidence is available. The disease is classified as **very rare**. The 2023 paper stated:

> “To date, only 12 TAP2-deficient patients were reported in the literature.”

That count depends on publication date and case definition and should not be interpreted as prevalence. [PMID 36227411](https://pubmed.ncbi.nlm.nih.gov/36227411/) [33]

Older reviews suggested substantial underdiagnosis because idiopathic bronchiectasis and atypical granulomatous skin disease are not routinely screened for HLA-I expression. [Published 15 October 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6803596/) [74]

---

# 10. Diagnostics

## 10.1 Recommended diagnostic pathway

1. **Suspect the disease** in recurrent childhood sinopulmonary infection, unexplained bronchiectasis, chronic necrotizing granulomatous skin or nasal lesions, Wegener-like disease without typical serology, or affected siblings.
2. **Measure surface HLA-A/B/C expression by flow cytometry** on peripheral-blood leukocytes using a pan-HLA-I antibody such as W6/32.
3. Obtain **lymphocyte subsets**, including total and naïve CD8 T cells, γδ T cells, NK cells, B cells and CD4:CD8 ratios.
4. Measure quantitative **IgG, IgA, IgM and IgE** and vaccine antibody responses as clinically indicated.
5. Evaluate infections with respiratory cultures, chest imaging, pulmonary-function testing and skin-biopsy microbiology where appropriate.
6. Confirm with **biallelic TAP2 pathogenic/likely pathogenic variants**, including deletion/duplication analysis.
7. Test parents and siblings for segregation and identify asymptomatic homozygotes or carriers.
8. Where variants are uncertain, perform functional assessment: TAP2 protein, peptide transport or HLA-I expression/complementation.

## 10.2 Clinical and laboratory tests

| Test | Expected/possible result | Role |
|---|---|---|
| Pan-HLA class I flow cytometry | Markedly reduced HLA-ABC percentage and/or fluorescence intensity | Best screening biomarker |
| β2-microglobulin-associated surface proteins | Reduced MHC-I; IUIS also notes absent/reduced CD1a, CD1b and CD1c in TAP deficiency | Supportive immune phenotype. [64] |
| CD3/CD4/CD8 subsets | Low CD8 in many but normal total CD8 possible | Supportive, not exclusionary |
| Naïve CD8 cells | Markedly reduced in recent TAP2 cases | Higher diagnostic utility than total CD8 alone |
| γδ T, MAIT, iNKT cells | May be increased | Mechanistic/supportive |
| NK-cell count/function | Count normal, low or increased; resting cytotoxicity often reduced | Variable; research/specialist test |
| Immunoglobulins | Often broadly normal; low IgM or hypergammaglobulinemia may occur | Detect coexisting humoral abnormality |
| Respiratory cultures | Typical encapsulated or Gram-negative bacteria | Direct antimicrobial therapy |
| Chest high-resolution CT | Bronchial dilation, wall thickening, mucus plugging | Diagnose and stage bronchiectasis |
| Pulmonary-function tests | Obstruction or reduced function in advanced disease | Longitudinal monitoring |
| Sinus CT/endoscopy | Chronic sinusitis, polyps, destructive changes | ENT assessment |
| Skin biopsy | Necrotizing/caseating or noncaseating granulomatous inflammation; possible vasculitis | Exclude infection, malignancy and mimics |
| PR3-ANCA/c-ANCA, urinalysis/renal tests | Typically lack classic GPA pattern; no characteristic glomerulonephritis | Differential diagnosis |

Historical diagnostic guidance explicitly recommends serologic HLA typing and/or pan-HLA-I flow cytometry rather than relying on molecular HLA typing, which does not assess expression. [66]

## 10.3 Genetic testing

| Method | Utility |
|---|---|
| TAP2 sequencing | Appropriate when immune phenotype strongly indicates isolated TAP2 deficiency |
| Inborn-error-of-immunity panel | Usually preferred; include **TAP2, TAP1, TAPBP, B2M**, and genes causing similar bronchiectasis/granulomatous disease |
| Exome sequencing | Useful in atypical cases; must include reliable copy-number calling |
| Genome sequencing | Potentially best for multiexon deletions, complex structural variants and noncoding/splice lesions |
| Deletion/duplication assay | Essential if sequencing identifies one allele or HLA-I phenotype is convincing |
| RNA sequencing | May verify splice effects or nonsense-mediated decay but is not first-line |
| CMA | May detect large 6p deletions, but smaller exon-level deletions can be missed |
| Karyotype/FISH | Low yield unless a large rearrangement is suspected |
| mtDNA/repeat-expansion testing | Not indicated for isolated MHC1D2 |

## 10.4 Differential diagnosis

| Differential | Distinguishing feature |
|---|---|
| TAP1-associated MHC-I deficiency | Same functional phenotype; distinguish genetically |
| TAPBP/tapasin deficiency | Reduced peptide loading and HLA-I; distinguish genetically and biochemically |
| B2M deficiency | Low/absent HLA-I and β2-microglobulin abnormalities; B2M genotype |
| MHC class II deficiency/BLS type II | Low HLA-DR/DP/DQ, profound CD4-related combined immunodeficiency; different genes |
| Chronic granulomatous disease | Abnormal neutrophil oxidative burst; deep bacterial/fungal infections |
| Common variable immunodeficiency | Low IgG with impaired vaccine responses; HLA-I not characteristically absent |
| Cystic fibrosis/primary ciliary dyskinesia | Mucociliary/CFTR abnormalities; normal HLA-I expression |
| Granulomatosis with polyangiitis | PR3-ANCA, glomerulonephritis and classic vasculitis pattern; not constitutively low HLA-I |
| NK/T-cell lymphoma, nasal type | Malignant clonal process, often EBV-associated |
| Mycobacterial, fungal or leishmanial infection | Organisms/culture/PCR; must be excluded before immunosuppression |
| Pyoderma gangrenosum | Clinical-pathologic diagnosis without the hallmark low HLA-I phenotype |
| WHIM/GATA2/DOCK8 or other IEI | Distinct blood counts, infections, viral phenotype and genotype |

## 10.5 Screening

- No population or newborn screening program exists.
- **Cascade family screening** with HLA-I flow cytometry and targeted variant testing is indicated.
- Prenatal or preimplantation testing is technically possible once familial variants are known.
- Asymptomatic homozygous relatives merit respiratory and immune surveillance because future penetrance is uncertain.

---

# 11. Outcome and prognosis

| Outcome domain | Evidence |
|---|---|
| Survival | No reliable five- or ten-year survival estimate |
| Life expectancy | Unknown; likely near-normal in mild/asymptomatic disease but potentially shortened by severe bronchiectasis, respiratory failure or treatment-related infection |
| Major morbidity | Chronic sinus disease, bronchiectasis, extensive skin ulceration, scarring, nasal destruction, hearing problems |
| Major mortality mechanism | Progressive pulmonary infection/respiratory failure; quantitative mortality rate unavailable |
| Recovery | Acute infections may resolve; granulomas may improve or relapse; bronchiectasis and major tissue destruction are generally irreversible |
| Favorable factors | Early diagnosis, preserved lung structure, prompt antimicrobial treatment, adherence to airway clearance, avoidance of harmful immunosuppression |
| Adverse factors | Established bronchiectasis, chronic *Pseudomonas* colonization, respiratory insufficiency, extensive destructive granulomas, delayed diagnosis |
| Biomarkers | HLA-I expression confirms mechanism but does not reliably predict severity; normal total CD8 does not ensure a mild course |
| QOL metrics | No disease-specific validated data |

Historical evidence indicates progressive lung damage can culminate in respiratory failure and death, but the same literature also documents adult survivors and clinically asymptomatic individuals. [4]

---

# 12. Treatment

No medication, gene therapy, or transplant strategy is specifically approved for TAP2 deficiency. Published management is based on case experience and bronchiectasis/immunodeficiency principles.

## 12.1 Current treatment strategy

| Intervention | Indication/evidence | Risks/limitations | Suggested NCIt concept |
|---|---|---|---|
| Prompt culture-directed antibiotics | Acute bacterial sinusitis, bronchitis or pneumonia | Resistance, allergy, microbiome effects | **Antibiotic Therapy** |
| Long-term/macrolide prophylaxis | Consider under bronchiectasis specialist guidance for frequent exacerbations; no TAP2-specific trial | Resistance, QT prolongation and drug interactions | **Antibiotic Prophylaxis** |
| Airway-clearance/chest physiotherapy | Bronchiectasis, mucus retention | Requires adherence | **Chest Physiotherapy** |
| Bronchodilator/inhaled therapy | Individualized to obstruction or reactive airways | Not disease-modifying | **Bronchodilator Therapy** |
| IV immunoglobulin | Not routinely required when humoral immunity is normal; historically appeared useful as adjunct in some severe pneumonias | Infusion reactions, thrombosis, cost | **Intravenous Immunoglobulin Therapy** |
| Vaccination | Respiratory-pathogen prevention according to immunology guidance | Responses should be assessed when relevant | **Vaccination** |
| Saline/benzoyl-peroxide wound care | Gentle debridement and reduction of bacterial colonization in ulcers | Local irritation | **Wound Care** |
| PUVA | Transient benefit in two historical patients | Phototoxicity and long-term skin-cancer risk | **PUVA Therapy** |
| Corticosteroids | May improve skin inflammation in selected lung-free cases | Can worsen infection; not broadly recommended | **Corticosteroid Therapy** |
| Tacrolimus/systemic immunomodulation | Used in a 2024 skin-predominant case | Infection, renal and metabolic toxicity; no controlled evidence | **Tacrolimus Therapy** |
| Thalidomide | Maintained skin-lesion stability in one 2024 combined TAP1/TAP2 deletion case | Severe teratogenicity, neuropathy, thrombosis; specialist-only use | **Thalidomide Therapy** |
| Sinus surgery | Sometimes necessary for complications, but historical experts cautioned that surgery could worsen local disease/postnasal spread | Tissue injury and progression | **Sinus Surgery** |
| Lung transplantation | Theoretical option for end-stage lung disease; no robust TAP2-specific outcome evidence | Rejection, infection, immune complications | **Lung Transplantation** |
| Hematopoietic stem-cell transplantation | Not established standard therapy; ubiquitous nonhematopoietic HLA-I deficiency may not be fully corrected | GVHD and donor-NK concerns | **Hematopoietic Stem Cell Transplantation** |

The central historical recommendation is:

> “The primary objective of therapy for patients with TAP deficiency syndrome is tight control of infections in order to prevent the development or progression of bronchiectasis and ultimately respiratory failure.”

[PMID 10931128, August 2000](https://pmc.ncbi.nlm.nih.gov/articles/PMC1905688/) [4]

## 12.2 Skin-directed evidence from 2024

In the 2024 combined TAP1/TAP2 deletion case:

- prednisolone 40 mg daily improved plaques;
- tacrolimus was added;
- thalidomide 50 mg daily maintained stability;
- lesions relapsed severely after approximately 18 months off thalidomide.

This is single-patient evidence and cannot establish efficacy. The authors emphasized individualized treatment and cautioned that immunosuppression may be ineffective or fatal when bronchiectasis is present. [Published 25 June 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11437240/) [17]

## 12.3 Treatments to avoid or use cautiously

- Broad immunosuppression without excluding infection.
- Cyclophosphamide, methotrexate, azathioprine or cyclosporine for a presumed vasculitis: historical patients experienced progression of pulmonary and skin disease.
- Interferon-α or interferon-γ: historical use was associated with lesion progression and systemic adverse effects.
- Repeated surgery on inflamed nasal tissue without multidisciplinary planning.

## 12.4 Advanced/experimental treatment

No active disease-specific gene-replacement, CRISPR, RNA therapy, or TAP2-directed clinical trial was established in the retrieved evidence. In principle, gene correction of hematopoietic stem cells could restore TAP2 to immune cells, but:

- HLA-I is expressed throughout nucleated tissues;
- nonhematopoietic cells would remain deficient;
- restoration of missing-self signaling could produce complex NK-cell effects;
- preclinical efficacy and safety have not been established.

No disease-specific pharmacogenomic guideline exists.

---

# 13. Prevention

| Prevention level | Measures |
|---|---|
| Primary prevention of the genotype | Genetic counseling, carrier testing in relatives, reproductive options including prenatal diagnosis or PGT-M |
| Primary prevention of infection | Vaccination, respiratory hygiene, avoidance of tobacco smoke and unnecessary infectious exposure |
| Secondary prevention | Cascade testing, early HLA-I flow cytometry in suspicious bronchiectasis/granulomatous disease, early genetic confirmation |
| Tertiary prevention | Rapid treatment of infections, airway clearance, bronchiectasis surveillance, culture-guided therapy, wound care |
| Drug-related prevention | Avoid unnecessary immunosuppression and monitor antimicrobial toxicity |
| Monitoring | Periodic pulmonary assessment, oxygenation/PFTs as indicated, cultures, ENT review, skin review and hearing assessment |
| Public health | No special sanitation or vector-control program; standard infection-prevention measures apply |

General vaccine recommendations should be individualized by an immunologist. Historical absence of severe viral infection does **not** justify withholding routine immunization. Live-vaccine decisions should consider the patient’s complete immune phenotype rather than TAP2 genotype alone.

---

# 14. Other species and natural disease

## 14.1 Natural disease

No well-established naturally occurring companion-animal or livestock syndrome equivalent to human TAP2-associated MHC1D2 was identified in OMIA. Consequently:

- no validated VBO breed association is available;
- there is no zoonotic transmission;
- the human condition is inherited, not contagious;
- cross-species relevance is primarily experimental and comparative.

## 14.2 Comparative biology

| Species | Taxon | Ortholog/phenotype relevance |
|---|---:|---|
| Human | **NCBI Taxon 9606** | TAP2-associated MHC1D2 |
| House mouse | **NCBI Taxon 10090** | *Tap2* models show low MHC-I, markedly reduced peripheral CD8 cells and macrophage abnormalities |
| Rat | **NCBI Taxon 10116** | Conserved Tap2 antigen-processing ortholog; no prominent natural homologous disease identified |
| Zebrafish | **NCBI Taxon 7955** | Conserved antigen-processing machinery; limited direct MHC1D2 modeling |

The core mechanism—TAP-dependent peptide transport and MHC-I stabilization—is evolutionarily conserved among jawed vertebrates. Species differences in MHC loci, NK receptors and pathogen exposure limit direct translation of inflammatory phenotypes.

---

# 15. Model organisms and experimental systems

| Model | Type and genotype | Phenotype recapitulated | Applications and limitations |
|---|---|---|---|
| **Eightless mouse** | Spontaneous *Tap2* nonsense mutation, p.Gln285Ter, C57BL/6J | Absent TAP2, loss of surface MHC-I, severe peripheral CD8-cell deficiency; reduced peritoneal macrophages and impaired inflammatory macrophage survival | Strong model of molecular and immune phenotype; does not fully reproduce the variable human chronic skin and airway disease. **PMID: 27861817**. [100][103] |
| Chemically induced *Tap2* mutant mice | ENU/chemically induced alleles, including MGI entries | Reduced MHC-I and altered CD8 immunity depending on allele | Useful for allelic series and infection studies; phenotype depends on strain and microbiota |
| *Tap1*-deficient mice | Related pathway model rather than TAP2-specific | Low MHC-I, reduced CD8 cells, altered NK education | Helps study TAP-complex biology but cannot distinguish TAP2-specific protein functions |
| TAP2-deficient patient fibroblasts | Primary human in-vitro cells | Low HLA-I; may be killed by cytokine-activated autologous NK cells | Direct human mechanistic system; limited availability and does not model whole-organ physiology |
| EBV-transformed B-cell lines | Patient-derived cellular model | Defective peptide transport/HLA-I; used for complementation and NK cytotoxicity | EBV transformation alters cell biology and antigen presentation |
| Transfected/complemented cell lines | Wild-type TAP2 re-expression in deficient cells | Restoration of HLA-I supports variant causality | Excellent functional assay, but overexpression may not reflect endogenous dosage |
| Structural/biochemical proteoliposome systems | Purified or recombinant TAP1/TAP2 | ATP binding, peptide recognition and transport | Resolves transporter mechanism but cannot model immune development |
| iPSC/organoid models | Theoretically feasible | No established TAP2-deficiency disease platform identified | Future utility for airway epithelium, immune co-culture and gene correction |

The mouse study’s summary states:

> “This strain randomly arose in one of our C57BL/6J mouse colonies and was initially discovered because of the lack of CD8+ T cells in the periphery.”

It further identified absent surface MHC-I and impaired macrophage survival, suggesting a possible explanation for the phagocyte-like bacterial phenotype in patients. [Published online 2016; PMID 27861817](https://onlinelibrary.wiley.com/doi/full/10.1111/imm.12694) [101]

Relevant resources include **MGI gene MGI:98484**, IMSR/MMRRC, and the Alliance of Genome Resources. [93]

---

# Evidence assessment and current research gaps

| Question | Current evidence level |
|---|---|
| Is TAP2 loss causal? | **Strong/established:** human segregation, functional defect, rescue experiments and animal models |
| Is low HLA-I the central biomarker? | **Strong** |
| Are bacterial airway infections and granulomatous lesions characteristic? | **Strong**, but frequencies are uncertain |
| Is clinical penetrance complete? | **No:** asymptomatic homozygotes are documented |
| Do NK/γδ cells cause granulomas? | **Moderate mechanistic evidence**, not universally proven |
| Does persistent rubella drive some granulomas? | **Emerging evidence** in a subset |
| Is reduced total CD8 required? | **No:** sensitivity is inadequate; naïve CD8 may be more informative |
| Is there a curative therapy? | **No established curative treatment** |
| Are prognosis and survival quantifiable? | **No:** insufficient cohort size |
| Are omics signatures available? | **No validated clinical signature** |
| Are modifier genes known? | **No** |
| Is newborn screening justified? | **Insufficient evidence** |

## Priority research needs

1. International registry with genotype, residual HLA-I expression, naïve CD8 subsets, infection history and longitudinal lung outcomes.
2. Standardized HLA-I flow-cytometry thresholds and age-specific immune reference ranges.
3. Direct comparison of skin-, lung-, and asymptomatic phenotypes within families.
4. Metagenomic and rubella-specific testing of chronic granulomas.
5. Single-cell and spatial profiling of granulomatous lesions.
6. Functional assessment of newly reported missense and splice variants.
7. Prospective evidence for antimicrobial prophylaxis and skin-directed therapy.
8. Evaluation of hematopoietic gene correction in humanized models.

---

## Key primary literature

| Publication | Main contribution |
|---|---|
| de la Salle H, et al. **Homozygous human TAP peptide transporter mutation in HLA class I deficiency.** *Science*. 8 July 1994;265:237–241. **PMID: 7517574.** [PubMed-linked record](https://pubmed.ncbi.nlm.nih.gov/7517574/) | Landmark identification of homozygous TAP2 mutation and defective peptide transport |
| Matamoros N, et al. **Molecular studies and NK cell function of a new case of TAP2 homozygous human deficiency.** *Clin Exp Immunol*. August 2001;125:274–282. **PMID: 11529920.** [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC1906123/) | Human TAP2 molecular and NK-function analysis |
| Gadola SD, et al. **TAP deficiency syndrome.** *Clin Exp Immunol*. August 2000;121:173–178. **PMID: 10931128.** [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC1905688/) | Classical phenotype, frequency estimates, mechanisms and management |
| Darazam IA, et al. **Delayed Diagnosis of Chronic Necrotizing Granulomatous Skin Lesions due to TAP2 Deficiency.** *J Clin Immunol*. January 2023;43:217–228. **PMID: 36227411.** [PubMed](https://pubmed.ncbi.nlm.nih.gov/36227411/) | Two skin-predominant TAP2 cases, asymptomatic homozygotes and deep immunophenotyping |
| **Type I bare lymphocyte syndrome with novel TAP1 and TAP2 pathogenic variants.** Published online 25 June 2024. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11437240/) | Novel contiguous TAP1/TAP2 deletion and individualized treatment of severe skin lesions |
| **A novel spontaneous mutation in the TAP2 gene unravels its role in macrophage survival.** **PMID: 27861817.** [Article](https://onlinelibrary.wiley.com/doi/full/10.1111/imm.12694) | Eightless mouse model, absent MHC-I/CD8 cells and macrophage-survival phenotype |

**Overall interpretation:** MHC1D2 is a molecularly well-established but clinically under-characterized TAP2 loss-of-function disorder. Its defining laboratory feature is profoundly reduced cell-surface HLA-I, but the phenotype ranges from lifelong asymptomatic status to destructive skin granulomas and end-stage bronchiectatic lung disease. The strongest current clinical strategy is early molecular diagnosis plus prevention of irreversible infectious lung injury; treatment of granulomatous inflammation remains individualized and supported mainly by case-level evidence.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 0 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 0 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 18 |
| On topic | 4 |
| Off topic | 0 |

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:10931128`: "The primary objective of therapy for patients with TAP deficiency syndrome is tight control of infections in order to prevent the development or progression of bronchiectasis and ultimately respiratory failure."
  - Reference resolved but exposes no abstract or full text to search

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 51 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 1 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0005784` (1 mention) - HP does not contain this term

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.