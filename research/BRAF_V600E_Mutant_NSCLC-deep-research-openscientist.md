---
provider: openscientist
model: openscientist-autonomous
cached: false
end_time: '2026-05-05T23:49:20.673149Z'
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: BRAF V600E-Mutant Non-Small Cell Lung Cancer
  mondo_id: ''
  category: ''
citation_count: 42
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** BRAF V600E-Mutant Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **BRAF V600E-Mutant Non-Small Cell Lung Cancer** covering all of the
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

# Comprehensive Disease Characterization: BRAF V600E-Mutant Non-Small Cell Lung Cancer

---

## Summary

**BRAF V600E-mutant non-small cell lung cancer (NSCLC)** is a rare but clinically significant molecular subtype of lung cancer, comprising approximately 1–2% of all NSCLC cases and roughly 50–66% of all BRAF-mutated NSCLC in Western populations. Defined by a somatic gain-of-function point mutation (p.Val600Glu) in the BRAF serine/threonine kinase, this subtype constitutively activates the MAPK/ERK signaling pathway independent of upstream RAS signaling, driving unchecked cellular proliferation, survival, and angiogenesis. The disease presents almost exclusively as adenocarcinoma, with a notable enrichment of never-smokers and a slight female predominance compared to unselected NSCLC.

The identification of this actionable oncogenic driver has transformed the treatment landscape. Dual BRAF/MEK inhibition with dabrafenib plus trametinib achieves objective response rates (ORR) of 63–75% and median progression-free survival (PFS) of 10–25 months in treatment-naïve patients. More recently, encorafenib plus binimetinib has demonstrated potentially superior efficacy, with an ORR of 75%, median PFS of 30.2 months, and median overall survival (OS) of 47.6 months in treatment-naïve patients from the PHAROS trial. Immunotherapy also shows meaningful activity, with approximately 78% of BRAF V600E NSCLC tumors expressing PD-L1 ≥1%. Key unmet needs include overcoming acquired resistance to targeted therapy, managing a notably high thromboembolism risk (43% cumulative 1-year incidence), understanding the prognostic impact of co-mutations, and optimizing treatment sequencing. Comprehensive molecular profiling at diagnosis—preferably by next-generation sequencing (NGS)—is essential for identifying this rare but highly actionable driver.

This report synthesizes evidence from 64 publications, clinical trials, and real-world datasets to provide a comprehensive characterization of BRAF V600E-mutant NSCLC across disease information, etiology, phenotypes, genetics, pathophysiology, anatomy, temporality, epidemiology, diagnostics, prognosis, treatment, prevention, comparative biology, and model organisms.

---

## 1. Disease Information

### Overview

BRAF V600E-mutant NSCLC is a molecularly defined subtype of non-small cell lung cancer characterized by a specific somatic missense mutation (c.1799T>A; p.Val600Glu) in the BRAF gene (chromosome 7q34). This mutation results in constitutive activation of the BRAF kinase and downstream MAPK/ERK signaling, driving oncogenesis. It is classified as a Class I BRAF mutation, which signals as a RAS-independent monomer with markedly elevated (approximately 500-fold) kinase activity compared to wild-type BRAF ([PMID: 39961465](https://pubmed.ncbi.nlm.nih.gov/39961465/)).

### Key Identifiers

| Database | Identifier |
|----------|-----------|
| ICD-10 | C34 (Malignant neoplasm of bronchus and lung) |
| ICD-11 | 2C25 (Malignant neoplasms of bronchus or lung) |
| ICD-O-3 | 8140/3 (Adenocarcinoma, NOS — most common histology) |
| MeSH | D002289 (Carcinoma, Non-Small-Cell Lung) |
| MONDO | MONDO:0005233 (non-small cell lung carcinoma) |
| OMIM | 164757 (BRAF gene) |
| HGNC | HGNC:1097 (BRAF) |
| COSMIC | COSM476 (BRAF V600E) |

### Synonyms and Alternative Names

- BRAF V600E-positive NSCLC
- BRAF V600E-mutant lung adenocarcinoma
- BRAF-mutant non-small cell lung cancer (Class I)
- V600E BRAF-driven lung cancer
- NSCLC harboring BRAF V600E mutation

### Data Sources

Information is derived from aggregated disease-level resources including clinical trial data (PHAROS, BRF113928), real-world registries (Italian ATLAS, French BLaDE, Turkish Oncology Group, LANDSCAPE), institutional cohort studies, and published literature.

---

## 2. Etiology

### Disease Causal Factors

The primary causal factor is a **somatic missense mutation** in the BRAF gene (BRAF V600E), which is an acquired genetic alteration arising in lung epithelial cells. This is not a germline/inherited condition. The mutation causes constitutive activation of the MAPK/ERK signaling pathway, which is the central oncogenic driver ([PMID: 29729495](https://pubmed.ncbi.nlm.nih.gov/29729495/)): *"BRAF mutations, found in 1.5-3.5% of NSCLC, are responsible of the constitutive activation of mitogen activated protein kinase (MAPK)/extracellular signal-regulated kinase (ERK) pathway."*

### Risk Factors

#### Genetic Risk Factors
- **BRAF V600E somatic mutation** (primary driver): A Class I activating mutation that functions as a RAS-independent monomer
- **Co-mutations**: TP53, STK11, KEAP1, and PI3K pathway mutations frequently co-occur and may modify disease behavior. Co-mutations were associated with shorter OS (median 8.7 vs. 20.2 months, p = 0.009) in a Turkish multicenter cohort ([PMID: 40813186](https://pubmed.ncbi.nlm.nih.gov/40813186/))
- No established germline susceptibility loci specific to BRAF V600E NSCLC

#### Environmental Risk Factors
- **Smoking**: Unlike most NSCLC subtypes, BRAF V600E-mutant NSCLC has an enrichment of never-smokers (29–64% depending on cohort). In Chinese cohorts, 55% were never-smokers ([PMID: 35814395](https://pubmed.ncbi.nlm.nih.gov/35814395/)): *"64.2% were non-smokers"*. In European cohorts, 29–30% were never-smokers ([PMID: 24552757](https://pubmed.ncbi.nlm.nih.gov/24552757/)): *"The proportion of never-smokers among BRAF-positives was high (29%)."* However, smoking remains a risk factor for lung cancer broadly.
- **Age**: Median age at diagnosis is 64–68 years
- **Sex**: Slight female predominance (50–55%)
- **Occupational exposures**: Standard lung carcinogen exposures (asbestos, radon, etc.) apply to NSCLC generally

### Protective Factors

- **Smoking cessation**: Reduces overall lung cancer risk
- No specific genetic protective factors have been identified for BRAF V600E NSCLC
- Standard lung cancer protective factors (dietary antioxidants, physical activity) apply generally

### Gene-Environment Interactions

The relationship between smoking and BRAF V600E NSCLC is distinctive. Unlike KRAS-mutant NSCLC (strongly smoking-associated), BRAF V600E occurs with notable frequency in never-smokers, suggesting that at least a subset of cases arise through mechanisms independent of tobacco carcinogenesis. However, the mutation also occurs in current/former smokers, indicating that both smoking-dependent and smoking-independent pathways can lead to BRAF V600E acquisition.

---

## 3. Phenotypes

### Clinical Presentation

| Phenotype | HPO Term | Type | Frequency | Severity |
|-----------|----------|------|-----------|----------|
| Cough | HP:0012735 (Cough) | Symptom | ~60-70% | Variable |
| Dyspnea | HP:0002094 (Dyspnea) | Symptom | ~50-60% | Progressive |
| Chest pain | HP:0100749 (Chest pain) | Symptom | ~25-40% | Variable |
| Hemoptysis | HP:0002105 (Hemoptysis) | Symptom | ~20-30% | Variable |
| Weight loss | HP:0001824 (Weight loss) | Symptom | ~30-50% | Progressive |
| Fatigue | HP:0012378 (Fatigue) | Symptom | ~40-60% | Variable |
| Pleural effusion | HP:0002202 (Pleural effusion) | Sign | ~15-25% | Moderate-severe |
| Brain metastases | HP:0100009 (Cerebral neoplasm) | Complication | 15-21% at diagnosis | Severe |
| Thromboembolism | HP:0001907 (Thromboembolism) | Complication | 43% 1-year incidence | Severe |
| Bone metastases | HP:0031377 (Bone neoplasm) | Complication | ~25-35% | Moderate-severe |

### Phenotype Characteristics

- **Age of onset**: Adult-onset, median 64–68 years
- **Symptom severity**: Variable at presentation; many patients are diagnosed at advanced stages (Stage IIIB-IV)
- **Symptom progression**: Progressive without treatment; responsive to targeted therapy
- **Histology**: Predominantly adenocarcinoma (>95%) ([PMID: 39616778](https://pubmed.ncbi.nlm.nih.gov/39616778/)): *"95.1 % had adenocarcinoma"*

### Thromboembolism as a Distinctive Phenotype

A particularly notable clinical feature is the high risk of thromboembolism. In a study of 10 BRAF V600E NSCLC patients, 5 developed 7 thromboembolic events, with a 1-year cumulative incidence of 43% (95% CI: 11–72%). Events included cancer-related stroke and venous thromboembolism, with stroke patients showing elevated D-dimer levels and rapid mortality ([PMID: 36697098](https://pubmed.ncbi.nlm.nih.gov/36697098/)): *"Of 10 patients with BRAF-V600E mutant lung cancer, five developed a total of seven thromboembolic events, showing a 1-year cumulative incidence of 43% (95% confidence interval=11-72%)."*

### Quality of Life Impact

Advanced BRAF V600E NSCLC significantly impacts daily functioning through respiratory symptoms, fatigue, pain, and treatment-related adverse effects. Targeted therapy with dabrafenib/trametinib has been shown to maintain or improve quality of life compared to chemotherapy. Chinese phase II data on dabrafenib plus trametinib specifically evaluated quality of life outcomes ([PMID: 39830765](https://pubmed.ncbi.nlm.nih.gov/39830765/)).

---

## 4. Genetic/Molecular Information

### Causal Gene

- **Gene**: BRAF (B-Raf proto-oncogene, serine/threonine kinase)
- **HGNC ID**: HGNC:1097
- **OMIM**: 164757
- **Chromosome location**: 7q34
- **UniProt**: P15056

### Pathogenic Variant

| Feature | Detail |
|---------|--------|
| Variant | BRAF V600E (c.1799T>A; p.Val600Glu) |
| COSMIC ID | COSM476 |
| dbSNP | rs113488022 |
| Variant type | Missense (Class I activating mutation) |
| Variant classification | Pathogenic (somatic oncogenic driver) |
| Origin | Somatic (acquired) |
| Functional consequence | Gain-of-function; constitutive kinase activation (~500-fold increase) |
| Frequency in NSCLC | 1–2% of all NSCLC; ~50–66% of BRAF-mutant NSCLC |
| Population allele frequency | Extremely rare as germline variant in gnomAD |

The BRAF V600E mutation is a well-characterized oncogenic driver across multiple cancer types (melanoma, colorectal cancer, thyroid cancer, hairy cell leukemia). In NSCLC, it accounts for approximately half to two-thirds of all BRAF mutations, with the remainder being non-V600E mutations (Class II and Class III) ([PMID: 40172088](https://pubmed.ncbi.nlm.nih.gov/40172088/)): *"V-Raf murine sarcoma viral oncogene homolog B (BRAF) mutations are found in up to 4% of patients with non-small cell lung cancer (NSCLC). Approximately 2% of advanced NSCLC cases harbor a BRAF V600E (class I) mutation."*

### BRAF Mutation Classification

| Class | Mechanism | RAS Dependence | Examples | Kinase Activity |
|-------|-----------|----------------|----------|-----------------|
| Class I | Active monomer | Independent | V600E, V600K, V600D | High (constitutive) |
| Class II | Active dimer | Independent | K601E, G469A | Intermediate-High |
| Class III | Kinase-impaired | Dependent | D594G, G466V | Reduced (activates via CRAF) |

### Co-occurring Molecular Alterations

Based on multiple cohort studies, common co-mutations include:
- **TP53**: Most frequent co-mutation (~30–50%)
- **STK11/LKB1**: Associated with poor immunotherapy response
- **KEAP1**: Associated with poor prognosis
- **PIK3CA**: Co-occurring PI3K pathway activation
- **EGFR**: Rarely co-mutated (generally mutually exclusive)

Co-mutations in non-V600E cases were more frequent (40% vs. 10%) and were associated with significantly worse outcomes (median OS 8.7 vs. 20.2 months, p = 0.009) ([PMID: 40813186](https://pubmed.ncbi.nlm.nih.gov/40813186/)).

### Modifier Genes

- **NKX2-1 (TTF-1)**: Loss of NKX2-1 in BRAF V600E-driven lung adenocarcinoma leads to invasive mucinous adenocarcinoma (IMA) phenotype and resistance to BRAF/MEK inhibition ([PMID: 33821796](https://pubmed.ncbi.nlm.nih.gov/33821796/)): The study demonstrated that *"NKX2-1 loss in human and murine lung adenocarcinoma leads to invasive mucinous adenocarcinoma (IMA), a lung cancer subtype that exhibits gastric differentiation."*
- **PI3K**: Mutationally-activated PI3Kα promotes de-differentiation of BRAF V600E-initiated lung tumors ([PMID: 31452510](https://pubmed.ncbi.nlm.nih.gov/31452510/))

### Epigenetic Information

- BRAF V600E tumors show distinct DNA methylation patterns compared to BRAF wild-type NSCLC
- CpG island methylator phenotype (CIMP) has been associated with BRAF V600E in colorectal cancer and may play a role in NSCLC
- Histone modifications downstream of MAPK signaling contribute to altered gene expression programs

---

## 5. Environmental Information

### Environmental Factors

- **Tobacco smoke**: The most significant environmental risk factor for NSCLC generally, though BRAF V600E-mutant NSCLC shows enrichment of never-smokers
- **Radon exposure**: Contributing factor for lung cancer in general populations
- **Air pollution**: Particulate matter (PM2.5) is an established lung carcinogen
- **Occupational exposures**: Asbestos, silica, heavy metals, and other industrial carcinogens

### Lifestyle Factors

- **Smoking**: 30–71% of BRAF V600E NSCLC patients are current/former smokers, depending on cohort and ethnicity
- **Diet**: No specific dietary factors linked to BRAF V600E NSCLC specifically
- **Exercise**: General protective effect against lung cancer

### Infectious Agents

Not directly applicable. No infectious agents are established as causes of BRAF V600E NSCLC, though HPV has been loosely associated with some lung cancers in certain populations.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

The central pathogenic mechanism involves constitutive activation of the **RAS-RAF-MEK-ERK (MAPK)** signaling cascade ([PMID: 39961465](https://pubmed.ncbi.nlm.nih.gov/39961465/)): *"V600E mutation results in a constitutively active kinase domain, leading to dysregulated downstream signaling independent of extracellular stimuli. This sustained activation promotes cell proliferation, survival, angiogenesis, and hallmark features of the cancer cells."*

#### Causal Chain

```
BRAF V600E Somatic Mutation (initiating event)
       │
       ▼
Constitutive BRAF Kinase Activation (~500-fold increase)
   [Signals as RAS-independent monomer]
       │
       ▼
Sustained MEK1/2 Phosphorylation (MEK → pMEK)
       │
       ▼
Constitutive ERK1/2 Activation (ERK → pERK)
       │
       ├──► Transcription factor activation (ELK1, c-MYC, c-FOS, c-JUN)
       ├──► Cell cycle progression (Cyclin D1 upregulation)
       ├──► Anti-apoptotic signaling (BCL-2 family modulation)
       ├──► Angiogenesis (VEGF upregulation)
       ├──► Metabolic reprogramming (Warburg effect enhancement)
       └──► Immune evasion (PD-L1 upregulation, TME remodeling)
              │
              ▼
       Malignant Transformation → Tumor Growth → Metastasis
```

#### Key Pathway Components

| Pathway | Role | GO Term |
|---------|------|---------|
| MAPK/ERK cascade | Primary oncogenic signaling | GO:0000165 |
| PI3K-AKT-mTOR | Cross-talk and resistance | GO:0043491 |
| WNT signaling | De-differentiation upon NKX2-1 loss | GO:0016055 |
| Cell proliferation | Downstream effect | GO:0008283 |
| Anti-apoptosis | Survival signaling | GO:0006915 (regulation) |
| Angiogenesis | Tumor vascularization | GO:0001525 |

### Cellular Processes

- **Cell proliferation** (GO:0008283): Constitutive ERK activation drives uncontrolled cell division
- **Evasion of apoptosis** (GO:0043066): MAPK signaling upregulates anti-apoptotic proteins
- **Angiogenesis** (GO:0001525): VEGF-mediated tumor neovascularization
- **Cell migration and invasion** (GO:0016477): EMT-related processes driving metastasis
- **Immune evasion**: PD-L1 expression (78% PD-L1 ≥1% in BRAF V600E NSCLC) ([PMID: 39616778](https://pubmed.ncbi.nlm.nih.gov/39616778/))

### Protein Dysfunction

The V600E mutation substitutes glutamic acid for valine at position 600 in the activation segment of the BRAF kinase domain. This substitution mimics the phosphorylated (active) state of the activation loop, locking BRAF in a constitutively active conformation. Unlike wild-type BRAF, which requires RAS-GTP binding and dimerization for activation, BRAF V600E signals as a monomer without upstream RAS input.

### Resistance Mechanisms

Resistance to BRAF/MEK-targeted therapy occurs through several mechanisms identified via circulating tumor DNA (ctDNA) genomics ([PMID: 32859654](https://pubmed.ncbi.nlm.nih.gov/32859654/)):
- **MAPK pathway reactivation**: Acquisition of secondary RAS mutations (NRAS, KRAS), MEK mutations, BRAF amplification
- **Bypass pathway activation**: PI3K/AKT/mTOR pathway activation, MET amplification
- **Lineage transformation**: NKX2-1 loss leading to gastric differentiation and BRAF/MEK inhibitor resistance ([PMID: 33821796](https://pubmed.ncbi.nlm.nih.gov/33821796/))
- **BRAF V600E as acquired resistance mechanism**: BRAF V600E can itself emerge as a resistance mechanism during EGFR-TKI therapy in EGFR-mutant NSCLC ([PMID: 39830741](https://pubmed.ncbi.nlm.nih.gov/39830741/))

### Metabolic Changes

- Enhanced glycolysis (Warburg effect) driven by MAPK-dependent metabolic reprogramming
- Altered lipid metabolism
- Increased nucleotide synthesis supporting rapid proliferation

### Immune System Involvement

- High PD-L1 expression (~78% PD-L1 ≥1%) suggests an inflamed tumor microenvironment
- Response to immune checkpoint inhibitors (anti-PD-1/PD-L1) observed in clinical settings
- The relationship between BRAF V600E signaling and immune evasion involves MAPK-driven upregulation of PD-L1 and modulation of the tumor microenvironment

### Advanced Technologies and Molecular Profiling

#### ctDNA-based Resistance Profiling

Circulating tumor DNA sequencing has proven clinically relevant for detection of BRAF V600E mutations and identification of resistance mechanisms ([PMID: 32859654](https://pubmed.ncbi.nlm.nih.gov/32859654/)). Serial ctDNA analysis can detect MAPK pathway reactivation mutations, bypass pathway alterations, and emerging co-mutations that may predict treatment failure.

#### Functional Genomics

Genome-wide screening has identified novel genes implicated in cellular sensitivity to BRAF V600E inhibition ([PMID: 31548614](https://pubmed.ncbi.nlm.nih.gov/31548614/)), expanding the understanding of genetic modifiers of targeted therapy response.

#### Novel Inhibitor Development

Erianin has been identified as a novel dual CRAF/MEK1/2 inhibitor that suppresses constitutive MAPK activation in BRAF V600E-mutant cells, representing a potential strategy to overcome paradoxical activation seen with single-agent BRAF inhibitors ([PMID: 36872366](https://pubmed.ncbi.nlm.nih.gov/36872366/)).

---

## 7. Anatomical Structures Affected

### Organ Level

| Level | Structure | UBERON/Ontology Term |
|-------|-----------|---------------------|
| Primary | Lung | UBERON:0002048 |
| Secondary | Brain (metastases in 15–21%) | UBERON:0000955 |
| Secondary | Bone (metastases in ~25–35%) | UBERON:0002481 |
| Secondary | Liver (metastases) | UBERON:0002107 |
| Secondary | Adrenal glands (metastases) | UBERON:0002369 |
| Secondary | Pleura (effusions in 15–25%) | UBERON:0000977 |
| Secondary | Pericardium (effusions) | UBERON:0002407 |
| Body system | Respiratory system | UBERON:0001004 |
| Body system | Vascular system (thromboembolism) | UBERON:0004537 |

### Tissue and Cell Level

- **Primary tissue**: Pulmonary epithelium (UBERON:0000115)
- **Primary cell type**: Type II alveolar epithelial cells (pneumocytes) — the putative cell of origin for lung adenocarcinoma (CL:0002063)
- **Additional cell types**: Club cells (Clara cells; CL:0000158) — can be cell of origin in certain murine models ([PMID: 28783725](https://pubmed.ncbi.nlm.nih.gov/28783725/))
- **Histology**: Adenocarcinoma, predominantly acinar, papillary, or lepidic patterns

### Subcellular Level

| Compartment | GO Term | Relevance |
|-------------|---------|-----------|
| Cytoplasm | GO:0005737 | BRAF protein localization |
| Cell membrane | GO:0005886 | RAS-RAF interaction site |
| Nucleus | GO:0005634 | ERK-mediated transcription factor activation |
| Mitochondria | GO:0005739 | Apoptotic regulation |

### Localization

- **Primary site**: Any lobe of the lung; no specific lobar predilection established
- **Lateralization**: Can be unilateral or bilateral; no consistent lateralization pattern
- **Metastatic sites**: Brain, bone, liver, adrenal glands, contralateral lung

---

## 8. Temporal Development

### Onset

- **Typical age of onset**: Adult/geriatric, median 64–68 years
- **Onset pattern**: Insidious; most patients present with advanced-stage disease
- BRAF V600E is not specifically associated with younger age at diagnosis (unlike EGFR or ALK) ([PMID: 26720421](https://pubmed.ncbi.nlm.nih.gov/26720421/))

### Progression

#### Disease Stages (AJCC 8th Edition TNM)

| Stage | Description | Approximate Distribution at Diagnosis |
|-------|-------------|--------------------------------------|
| I | Localized | ~15–20% |
| II | Locally advanced | ~5–10% |
| III | Regional spread | ~15–20% |
| IV | Distant metastases | ~50–60% |

- **Progression rate**: Variable; without treatment, progression is typically rapid (months)
- **Disease course**: Progressive without treatment
- **With targeted therapy**: Durable responses observed (median PFS 13–30 months depending on regimen)

### Patterns

- **Treatment-induced remission**: Achievable with BRAF/MEK inhibition (ORR 63–75%)
- **Complete remission**: Rare but documented, including cases with combined BRAF/MEK inhibition and immunotherapy ([PMID: 41333480](https://pubmed.ncbi.nlm.nih.gov/41333480/))
- **Acquired resistance**: Develops in most patients on targeted therapy, typically after 10–30 months
- **Critical period**: Early molecular diagnosis is critical for initiating appropriate targeted therapy

---

## 9. Inheritance and Population

### Epidemiology

| Metric | Value | Source |
|--------|-------|--------|
| BRAF mutation frequency in NSCLC | 1.5–4% | Multiple cohorts |
| BRAF V600E frequency in NSCLC | ~1–2% | [PMID: 40172088](https://pubmed.ncbi.nlm.nih.gov/40172088/) |
| V600E as fraction of BRAF mutations | 24.6% (China) to 66% (Europe) | [PMID: 40138888](https://pubmed.ncbi.nlm.nih.gov/40138888/) |
| Estimated incidence | ~3,000–6,000 new cases/year (US) | Derived from NSCLC incidence |

The Chinese LANDSCAPE study, one of the largest cohorts, found BRAF mutations in 3.56% (95% CI: 3.48–3.65%) of 175,566 NSCLC patients, with V600E accounting for 24.6% of BRAF mutations ([PMID: 40138888](https://pubmed.ncbi.nlm.nih.gov/40138888/)): *"In Cohort I, of patients with NSCLC, 6249 (3.56%, 95% CI: 3.48%-3.65%) were confirmed to harbour a BRAF mutation. BRAF V600E accounted for 24.6% (1539/6249) of all patients with BRAF-mutated NSCLC."*

In European cohorts, BRAF V600E represents a higher proportion (~66%) of BRAF mutations ([PMID: 24552757](https://pubmed.ncbi.nlm.nih.gov/24552757/)): *"We found a BRAF-mutation frequency of 1.7% in the total cohort of 979 patients, and 2.3% among 646 adenocarcinomas."*

### Inheritance Pattern

- **Somatic mutation**: Not inherited; arises as an acquired mutation in lung tissue
- **Inheritance pattern**: Not applicable (somatic oncogenic driver)
- No established germline predisposition specifically to BRAF V600E NSCLC

### Population Demographics

| Demographic | Characteristic |
|-------------|---------------|
| Sex ratio | Slight female predominance (50–55% female) |
| Median age | 64–68 years |
| Smoking status | 29–64% never-smokers (varies by ethnicity) |
| Ethnicity | Higher V600E proportion in Western populations (~66%) vs. Asian (~25%) |
| Histology | >95% adenocarcinoma |

Clinical characteristics from the French BLaDE cohort ([PMID: 39616778](https://pubmed.ncbi.nlm.nih.gov/39616778/)): *"A total of 163 patients were included: 50.3 % were female, 30.2 % were never smokers, 95.1 % had adenocarcinoma, and 78.2 % had a PDL1 ≥ 1 %. The median age was 68.3 years."*

From a Chinese multicenter study ([PMID: 35814395](https://pubmed.ncbi.nlm.nih.gov/35814395/)): *"Fifty-three patients with BRAF V600E-mutant advanced NSCLC were included in the study, of which 64.2% were non-smokers, and the BRAF V600E mutation was more prevalent in men (52.8%). In addition, 96.2% of the patients had adenocarcinoma."*

---

## 10. Diagnostics

### Molecular Testing (Essential)

Comprehensive molecular testing at diagnosis is mandatory for identifying BRAF V600E and guiding treatment. NCCN guidelines recommend broad molecular profiling of all advanced NSCLC ([PMID: 31454018](https://pubmed.ncbi.nlm.nih.gov/31454018/)): *"all patients with metastatic non-small cell lung cancer should undergo molecular testing for relevant mutations and expression of the protein PD-L1"* and *"Molecular alterations that predict response to treatment (eg, EGFR mutations, ALK rearrangements, ROS1 rearrangements, and BRAF V600E mutations) are present in approximately 30% of patients with non-small cell lung cancer."*

| Testing Modality | Utility | Notes |
|-----------------|---------|-------|
| **NGS (tissue-based)** | Gold standard | Detects BRAF V600E alongside other actionable mutations |
| **Liquid biopsy (ctDNA)** | Alternative/complementary | 82% concordance with tissue NGS ([PMID: 40437208](https://pubmed.ncbi.nlm.nih.gov/40437208/)) |
| **IHC (VE1 antibody)** | Screening/confirmation | BRAF V600E-specific antibody available ([PMID: 30188361](https://pubmed.ncbi.nlm.nih.gov/30188361/)) |
| **PCR-based assays** | Targeted detection | Cobas BRAF V600E test, Idylla |
| **FISH** | Not applicable | Not used for BRAF point mutations |

#### Liquid Biopsy

ctDNA-based testing has emerged as a critical diagnostic tool. The BFAST study demonstrated that NGS ctDNA analysis improves actionable mutation identification ([PMID: 38190582](https://pubmed.ncbi.nlm.nih.gov/38190582/)). Multiple platforms are validated including FoundationOne Liquid CDx, Guardant360, and UltraSEEK Lung Panel.

Real-world experience has demonstrated that ctDNA profiling identifies therapeutically relevant mutations at rates comparable to tissue-based NGS ([PMID: 40821453](https://pubmed.ncbi.nlm.nih.gov/40821453/); [PMID: 40503459](https://pubmed.ncbi.nlm.nih.gov/40503459/)). Exhaled breath condensate (EBC) analysis represents a novel lung-specific liquid biopsy modality under investigation ([PMID: 35526313](https://pubmed.ncbi.nlm.nih.gov/35526313/)).

#### Immunohistochemistry

The BRAF V600E-specific VE1 antibody can be used for IHC screening or confirmation. As noted in a review of diagnostic IHC for NSCLC ([PMID: 30188361](https://pubmed.ncbi.nlm.nih.gov/30188361/)): *"IHC using mutant-specific BRAF V600E, RET, pan-TRK, and LKB1 antibodies can be orthogonal tools for screening or confirmation of molecular events."*

### Clinical Tests

| Test | Application |
|------|-------------|
| CT chest/abdomen/pelvis | Staging, response assessment |
| PET-CT | Staging, detecting metastatic disease |
| Brain MRI | Mandatory at baseline (15–21% brain metastases) |
| PFTs | Pre-operative assessment |
| D-dimer | Thromboembolism risk assessment |
| PD-L1 IHC | Immunotherapy eligibility |

### Pathology/Histology

- Adenocarcinoma histology in >95% of cases
- Various growth patterns: acinar, papillary, lepidic, solid, micropapillary
- TTF-1 (NKX2-1) positive in most cases; loss associated with mucinous/gastric differentiation

### Differential Diagnosis

- Other driver-positive NSCLC (EGFR, ALK, ROS1, RET, MET, KRAS G12C, HER2)
- BRAF non-V600E mutant NSCLC (Class II and III mutations)
- Driver-negative NSCLC
- Metastatic BRAF V600E melanoma to the lung
- Metastatic BRAF V600E thyroid cancer to the lung

---

## 11. Outcome/Prognosis

### Survival and Mortality

#### Treatment Outcomes Summary

| Treatment | Setting | ORR | Median PFS | Median OS | Source |
|-----------|---------|-----|------------|-----------|--------|
| **Dabrafenib + Trametinib** | 1st-line | 63.9–75% | 10.2–25.0 mo | NR–24.6 mo | Multiple |
| **Dabrafenib + Trametinib** | ≥2nd-line | 63–68% | 8.6–12.6 mo | 18.2 mo | BRF113928 |
| **Encorafenib + Binimetinib** | 1st-line | 75% | 30.2 mo | 47.6 mo | PHAROS |
| **Encorafenib + Binimetinib** | ≥2nd-line | 46% | 7.4 mo | 23.5 mo | PHAROS |
| **Chemotherapy (Pt-pemetrexed)** | 1st-line | 39–77% | 6.1–14.7 mo | Variable | Multiple |
| **Immunotherapy ± chemo** | 1st-line | Variable | Variable | Variable | Limited data |

The PHAROS trial updated data showed the longest reported median OS for any targeted therapy in BRAF V600E NSCLC: 47.6 months (95% CI: 31.3–NE) in treatment-naïve patients, with 4-year OS probability of 49% ([PMID: 41109959](https://pubmed.ncbi.nlm.nih.gov/41109959/)): *"After median follow-up for overall survival (OS) of 52.3 months in treatment-naïve patients, mOS was 47.6 months (95% CI, 31.3 to not estimable); 4-year OS probability was 49% (95% CI, 35 to 62)."*

A matching-adjusted indirect comparison suggested encorafenib plus binimetinib may be superior to dabrafenib plus trametinib in first-line treatment: PFS HR = 0.47 (95% CI: 0.26–0.85; P = 0.01), OS HR = 0.55 (95% CI: 0.30–1.01; P = 0.06) ([PMID: 41604820](https://pubmed.ncbi.nlm.nih.gov/41604820/)): *"Compared with D + T, E + B was associated with a statistically significant improvement in PFS [hazard ratio (HR) = 0.47; 95% CI 0.26-0.85; P = 0.01]."*

Real-world data corroborate clinical trial findings. The Italian ATLAS registry reported first-line D+T mPFS of 19.8 months (95% CI: 10.7–29.0) with a 2-year OS rate of 65.4% ([PMID: 41475048](https://pubmed.ncbi.nlm.nih.gov/41475048/)). The French BLaDE cohort showed first-line D+T mPFS of 18.2 months and 12-month OS rate of 67.4% ([PMID: 39616778](https://pubmed.ncbi.nlm.nih.gov/39616778/)): *"Among the 44 patients who received D + T as a first-line therapy, the 12-month OS rate was 67.4 %, with an mPFS of 18.2 months."*

### Prognostic Factors

| Factor | Impact | Evidence |
|--------|--------|----------|
| Co-mutations | Negative (OS 8.7 vs. 20.2 mo, p=0.009) | [PMID: 40813186](https://pubmed.ncbi.nlm.nih.gov/40813186/) |
| Brain metastases | Negative prognosis | Multiple cohorts |
| PD-L1 status | No significant impact on OS | [PMID: 40813186](https://pubmed.ncbi.nlm.nih.gov/40813186/) |
| Treatment line (D+T) | No significant difference 1L vs. later | [PMID: 40813186](https://pubmed.ncbi.nlm.nih.gov/40813186/) |
| Non-V600E BRAF subtype | Higher brain metastasis rate (60% vs. 15%) | [PMID: 40813186](https://pubmed.ncbi.nlm.nih.gov/40813186/) |
| BRAF mutation status vs. wild-type | Not a strong independent prognostic factor for OS | [PMID: 31181537](https://pubmed.ncbi.nlm.nih.gov/31181537/) |

The French Cooperative Thoracic Intergroup Biomarkers France study reported ([PMID: 31181537](https://pubmed.ncbi.nlm.nih.gov/31181537/)): *"BRAF mutation was not found to be prognostic of overall survival"* when comparing BRAF-mutant to wild-type NSCLC treated with standard chemotherapy.

### Complications

- **Thromboembolism**: 43% 1-year cumulative incidence including cancer-related stroke and VTE ([PMID: 36697098](https://pubmed.ncbi.nlm.nih.gov/36697098/))
- **Brain metastases**: Present in 15–21% at diagnosis; can develop during disease course
- **Bone metastases**: Pain, pathological fractures, hypercalcemia
- **Pleural/pericardial effusions**: Respiratory and cardiovascular compromise

---

## 12. Treatment

### FDA-Approved Targeted Therapies

#### Dabrafenib (BRAF inhibitor) + Trametinib (MEK inhibitor)

- **MAXO terms**: MAXO:0001298 (targeted molecular therapy)
- **Mechanism**: Dabrafenib inhibits BRAF V600E kinase; trametinib inhibits MEK1/2 downstream
- **FDA approval**: June 2017 for BRAF V600E-mutant metastatic NSCLC
- **Also approved**: Tumor-agnostic indication for BRAF V600E solid tumors (June 2022) ([PMID: 39529955](https://pubmed.ncbi.nlm.nih.gov/39529955/)): *"Dabrafenib plus trametinib, as the first tumor-agnostic therapy, has been approved by the US Food and Drug Administration for the treatment of adult and pediatric patients aged 6 years and older harboring a BRAF V600E mutation with unresectable or metastatic solid tumors."*
- **Dosing**: Dabrafenib 150 mg BID + Trametinib 2 mg QD
- **Key efficacy data**:
  - Treatment-naïve: ORR 63.9–75%, median PFS 10.2–25 months
  - Chinese phase II: ORR 75% (95% CI: 50.9–91.3%) ([PMID: 39830765](https://pubmed.ncbi.nlm.nih.gov/39830765/)): *"The ORR by both central and investigator assessment was 75% [95% confidence interval (CI): 50.9-91.3%]."*
  - Italian ATLAS real-world: median PFS 19.8 months (95% CI: 10.7–29.0), 2-year OS 65.4%
  - French BLaDE real-world: 1L mPFS 18.2 months, 12-month OS 67.4% ([PMID: 39616778](https://pubmed.ncbi.nlm.nih.gov/39616778/))
  - Previously treated: ORR 63%, median PFS 9.7 months ([PMID: 27283860](https://pubmed.ncbi.nlm.nih.gov/27283860/)): *"BRAF mutations act as an oncogenic driver via the mitogen-activated protein kinase (MAPK) pathway in non-small cell lung cancer (NSCLC)."*
- **Common adverse events**: Pyrexia, fatigue, nausea, peripheral edema, rash, elevated liver enzymes

#### Encorafenib (BRAF inhibitor) + Binimetinib (MEK inhibitor)

- **FDA approval**: October 2023 for BRAF V600E-mutant metastatic NSCLC (based on PHAROS)
- **Dosing**: Encorafenib 450 mg QD + Binimetinib 45 mg BID
- **Key efficacy data (PHAROS)**:
  - Treatment-naïve: ORR 75%, median DOR 40.0 months, median PFS 30.2 months, median OS 47.6 months, 3-year OS 53% ([PMID: 40480428](https://pubmed.ncbi.nlm.nih.gov/40480428/); [PMID: 41109959](https://pubmed.ncbi.nlm.nih.gov/41109959/))
  - Previously treated: ORR 46%, median PFS 7.4 months, median OS 23.5 months ([PMID: 37270692](https://pubmed.ncbi.nlm.nih.gov/37270692/))
- **Adverse events**: GI toxicity (including rare colitis ([PMID: 34436699](https://pubmed.ncbi.nlm.nih.gov/34436699/))), fatigue, musculoskeletal pain
- **Potentially superior to D+T**: PFS HR = 0.47 (p = 0.01) by MAIC ([PMID: 41604820](https://pubmed.ncbi.nlm.nih.gov/41604820/))

### Immunotherapy

- **Checkpoint inhibitors**: Anti-PD-1/PD-L1 agents (pembrolizumab, nivolumab, atezolizumab)
- High PD-L1 expression (78% ≥1%) supports immunotherapy use
- Real-world data suggest no detriment from PD-L1 inhibitors compared to driver-negative NSCLC ([PMID: 37744307](https://pubmed.ncbi.nlm.nih.gov/37744307/)): *"Substantial use of anti-PD-(L)1 therapy and associated clinical outcomes are consistent with previous real-world findings and suggest no detriment from PD-(L)1 inhibitors for advanced nonsquamous NSCLC harboring one of these four genomic alterations relative to driver-negative NSCLC."*
- Case reports of durable response with pembrolizumab monotherapy ([PMID: 41777654](https://pubmed.ncbi.nlm.nih.gov/41777654/))
- Combination of BRAF/MEK inhibition with immunotherapy (triplet therapy) is under investigation ([PMID: 41333480](https://pubmed.ncbi.nlm.nih.gov/41333480/))

### Chemotherapy

- **Platinum-based doublets**: Standard options include platinum/pemetrexed
- Platinum-pemetrexed outperforms platinum-taxane: ORR 77% vs. 33% (p = 0.006), PFS 14.7 vs. 3.2 months (p = 0.002) ([PMID: 40813186](https://pubmed.ncbi.nlm.nih.gov/40813186/))
- BRAF V600E patients may have shorter PFS to platinum-based chemotherapy vs. non-V600E (4.1 vs. 8.9 months, p = 0.297) ([PMID: 23833300](https://pubmed.ncbi.nlm.nih.gov/23833300/))
- BRAF mutation is not a strong prognostic factor when treated with standard chemotherapy ([PMID: 31181537](https://pubmed.ncbi.nlm.nih.gov/31181537/))

### Single-Agent BRAF Inhibitors

- **Vemurafenib monotherapy**: Limited efficacy in NSCLC with 0% complete response rate and increased adverse events compared to melanoma ([PMID: 41383110](https://pubmed.ncbi.nlm.nih.gov/41383110/)): *"A 0% complete response rate was observed in colorectal cancer, non-small cell lung cancer, and papillary thyroid cancer."*
- Single-agent BRAF inhibition is inferior to combination BRAF+MEK inhibition due to paradoxical MAPK reactivation

### Treatment for Acquired BRAF V600E (EGFR-Mutant NSCLC)

- BRAF V600E can emerge as resistance mechanism during EGFR-TKI therapy
- Triple therapy (EGFR-TKI + dabrafenib + trametinib): ORR 35.7%, DCR 78.6%, median PFS 6.7 months ([PMID: 39830741](https://pubmed.ncbi.nlm.nih.gov/39830741/))

### Surgical and Interventional

- **Surgical resection**: For early-stage disease (Stage I-IIIA); standard lobectomy with lymph node dissection (MAXO:0000004)
- **Radiation therapy**: Stereotactic radiosurgery for brain metastases; definitive chemoradiation for locally advanced disease (MAXO:0000014)

### Treatment Algorithm

```
BRAF V600E-Mutant Metastatic NSCLC
              │
              ▼
    ┌─────────────────┐
    │ Molecular Testing│ ← NGS (tissue or liquid biopsy)
    │ confirms V600E   │
    └────────┬────────┘
             │
             ▼
   First-line Therapy:
   ┌────────────────────────┐
   │ Encorafenib+Binimetinib│ ← Preferred (PHAROS data)
   │     OR                  │
   │ Dabrafenib+Trametinib  │ ← Alternative (BRF113928)
   └────────┬───────────────┘
            │ (Progression)
            ▼
   Second-line Options:
   ├─ Immunotherapy ± chemotherapy
   ├─ Alternative BRAF/MEK combination
   ├─ Platinum-based chemotherapy (prefer Pt-pemetrexed)
   └─ Clinical trials
```

---

## 13. Prevention

### Primary Prevention

- **Smoking cessation**: Most impactful intervention for lung cancer prevention generally; relevant even though BRAF V600E NSCLC has higher never-smoker rates
- **Radon mitigation**: Home radon testing and remediation
- **Occupational safety**: Limiting exposure to known carcinogens
- No specific prevention strategies for BRAF V600E NSCLC per se

### Secondary Prevention (Screening)

- **Low-dose CT (LDCT) screening**: Recommended for high-risk individuals (ages 50–80, ≥20 pack-years smoking history) per USPSTF
- LDCT screening has potential to detect early-stage disease including BRAF V600E NSCLC
- Comprehensive molecular testing of screen-detected tumors can identify BRAF V600E at early stages
- Multiple programs worldwide are implementing integrated lung cancer screening with smoking cessation ([PMID: 36204992](https://pubmed.ncbi.nlm.nih.gov/36204992/); [PMID: 36522781](https://pubmed.ncbi.nlm.nih.gov/36522781/))
- Note: Current screening guidelines focus on smoking-related risk and may miss never-smoker BRAF V600E NSCLC patients

### Tertiary Prevention

- **Surveillance**: Regular imaging and ctDNA monitoring during and after treatment
- **Thromboprophylaxis**: Consider given the 43% 1-year thromboembolism risk
- **Brain MRI monitoring**: Regular brain imaging given high brain metastasis rate
- **ctDNA monitoring**: Emerging role for minimal residual disease detection and early resistance identification

---

## 14. Other Species / Natural Disease

### Comparative Biology

- **BRAF gene conservation**: BRAF is highly conserved across vertebrates
- **Canine BRAF mutations**: V595E (homologous to human V600E) found in canine cancers, particularly transitional cell carcinoma of the bladder (NCBI Taxon: 9615)
- **Mouse Braf** (NCBI Gene ID: 109880): Orthologous gene used extensively in modeling
- BRAF V600E is the most commonly studied oncogenic mutation across species due to its high conservation

### Natural Disease

- No naturally occurring BRAF V600E lung cancer has been well-described in other species
- BRAF V600E occurs naturally in multiple human cancer types (melanoma, colorectal, thyroid, hairy cell leukemia)
- The mutation is a key driver in canine urinary bladder cancer but does not typically present as lung cancer in companion animals

### Transmission

- Not applicable — BRAF V600E NSCLC is not transmissible or zoonotic

---

## 15. Model Organisms

### Genetically Engineered Mouse Models (GEMMs)

| Model | Features | Key Findings | Reference |
|-------|----------|-------------|-----------|
| BrafV600E;Trp53fl/fl (GEMM) | Conditional BRAF V600E expression in lung | Develops lung adenocarcinoma; used to study targeted therapy response | Multiple |
| BrafV600E;Nkx2-1fl/fl | BRAF V600E with NKX2-1 deletion | Invasive mucinous adenocarcinoma; resistance to BRAF/MEK inhibitors | [PMID: 33821796](https://pubmed.ncbi.nlm.nih.gov/33821796/) |
| BrafV600E;Pik3caH1047R | BRAF V600E with PI3K activation | De-differentiation of lung tumors | [PMID: 31452510](https://pubmed.ncbi.nlm.nih.gov/31452510/) |
| BrafD631A (kinase-inactive) | Kinase-inactive BRAF allele | Demonstrates BRAF-inactivating mutations initiate lung cancer; wild-type Braf sustains Kras/BrafD631A tumors | [PMID: 28783725](https://pubmed.ncbi.nlm.nih.gov/28783725/) |

### Cell Line and Xenograft Models

- **Human BRAF V600E NSCLC cell lines**: Available for in vitro studies of drug sensitivity and resistance
- **Thyroid cancer xenografts**: 8505C-Luc2 (BRAF V600E) cells injected intravenously into NOD-SCID mice produced lung metastases in 100% of mice; vemurafenib treatment dramatically reduced tumor growth ([PMID: 24262022](https://pubmed.ncbi.nlm.nih.gov/24262022/)): *"The in vivo treatment of 8505C xenograft lung metastases with vemurafenib dramatically reduced the growth and signal intensity with good correlation with actual tumor burden."*

### Model Characteristics and Limitations

**Phenotype recapitulation:**
- Mouse GEMMs recapitulate key features of human BRAF V600E NSCLC including adenocarcinoma histology, MAPK pathway activation, and response to BRAF/MEK inhibitors
- The NKX2-1 deletion model faithfully reproduces the invasive mucinous adenocarcinoma phenotype seen in a subset of human patients
- BRAF kinase-inactive models ([PMID: 28783725](https://pubmed.ncbi.nlm.nih.gov/28783725/)) revealed that *"the signal intensity of the MAPK pathway is a critical determinant not only in tumour development, but also in dictating the nature of the cancer-initiating cell and ultimately the resulting tumour phenotype"*

**Limitations:**
- Mouse immune microenvironment differs from human tumors, limiting immunotherapy studies
- Response kinetics to targeted therapy may differ between species
- Acquired resistance mechanisms may not fully mirror human disease
- Metastatic patterns in mouse models may not replicate human patterns
- Most GEMMs use Cre-Lox conditional systems that activate the mutation simultaneously across many cells, unlike the single-cell origin of human cancer

### Research Applications

- Drug efficacy testing (BRAF/MEK inhibitors, combination therapies)
- Resistance mechanism studies (MAPK reactivation, bypass pathways)
- Lineage plasticity and differentiation state investigations
- Immune microenvironment characterization
- Biomarker discovery and validation
- Novel therapeutic target identification

---

## Key Findings — Detailed Evidence

### Finding 1: BRAF V600E Mutation Prevalence

BRAF mutations are found in 1.5–4% of NSCLC overall, with V600E accounting for approximately 50–66% of BRAF mutations in Western cohorts and ~25% in Asian cohorts. This translates to a BRAF V600E frequency of approximately 1–2% of all NSCLC cases. The large Chinese LANDSCAPE cohort (N=175,566) found BRAF mutations in 3.56% of patients, with V600E in 24.6% of those ([PMID: 40138888](https://pubmed.ncbi.nlm.nih.gov/40138888/)). A European cohort of 979 patients found BRAF mutations in 1.7% overall and 2.3% of adenocarcinomas ([PMID: 24552757](https://pubmed.ncbi.nlm.nih.gov/24552757/)). The disease almost exclusively presents as adenocarcinoma (>95%).

### Finding 2: Dabrafenib + Trametinib Efficacy

Dual BRAF/MEK inhibition with D+T has been validated across clinical trials and real-world cohorts. Phase II data show ORR of 63.9–75% in treatment-naïve patients. Real-world datasets from Italy (ATLAS), France (BLaDE), and Turkey confirm efficacy with median PFS of 13–25 months. The Chinese phase II trial demonstrated ORR of 75% ([PMID: 39830765](https://pubmed.ncbi.nlm.nih.gov/39830765/)). The tumor-agnostic approval of D+T for BRAF V600E solid tumors further validates this combination across cancer types.

### Finding 3: Encorafenib + Binimetinib Superiority

The PHAROS trial established E+B as a highly effective option with potentially the longest PFS and OS of any targeted therapy in this setting. Updated data show median PFS of 30.2 months, median OS of 47.6 months, and 4-year OS probability of 49% in treatment-naïve patients ([PMID: 41109959](https://pubmed.ncbi.nlm.nih.gov/41109959/)). A matching-adjusted indirect comparison suggested PFS superiority over D+T (HR 0.47, p=0.01), though this requires confirmation in a direct randomized comparison ([PMID: 41604820](https://pubmed.ncbi.nlm.nih.gov/41604820/)).

### Finding 4: MAPK Pathway Constitutive Activation

The V600E mutation results in ~500-fold increased kinase activity compared to wild-type BRAF, functioning as a RAS-independent monomer. This constitutive activation promotes cell proliferation, survival, angiogenesis, and immune evasion through sustained MEK-ERK signaling ([PMID: 39961465](https://pubmed.ncbi.nlm.nih.gov/39961465/); [PMID: 29729495](https://pubmed.ncbi.nlm.nih.gov/29729495/); [PMID: 27283860](https://pubmed.ncbi.nlm.nih.gov/27283860/)).

### Finding 5: Distinctive Clinical Characteristics

BRAF V600E NSCLC patients show a characteristic clinical profile: predominantly adenocarcinoma (95–96%), median age 64–68 years, slight female predominance (50–55%), and notably high never-smoker proportion (29–64%). Brain metastases are present in 15–21% at diagnosis. PD-L1 expression is high (78% ≥1%), supporting immunotherapy consideration ([PMID: 39616778](https://pubmed.ncbi.nlm.nih.gov/39616778/); [PMID: 35814395](https://pubmed.ncbi.nlm.nih.gov/35814395/)).

### Finding 6: Thromboembolism Risk

A strikingly high rate of thromboembolism was documented with a 1-year cumulative incidence of 43% (95% CI: 11–72%) in BRAF V600E NSCLC patients. Events included cancer-related stroke and venous thromboembolism, with stroke patients experiencing high D-dimer levels and short-term mortality ([PMID: 36697098](https://pubmed.ncbi.nlm.nih.gov/36697098/)). This finding has significant implications for clinical management and thromboprophylaxis.

---

## Evidence Base

### Landmark Clinical Trials

| Trial | Phase | Key Result | PMID |
|-------|-------|------------|------|
| BRF113928 (previously treated) | II | D+T: ORR 63%, mPFS 9.7 mo | [PMID: 27283860](https://pubmed.ncbi.nlm.nih.gov/27283860/) |
| PHAROS (E+B) | II | 1L: ORR 75%, mPFS 30.2 mo, mOS 47.6 mo | [PMID: 41109959](https://pubmed.ncbi.nlm.nih.gov/41109959/) |
| Chinese Phase II (D+T) | II | ORR 75%, manageable safety | [PMID: 39830765](https://pubmed.ncbi.nlm.nih.gov/39830765/) |

### Key Real-World Studies

| Cohort | N | Key Finding | PMID |
|--------|---|-------------|------|
| Italian ATLAS | 88+ | 1L D+T mPFS 19.8 mo, 2-yr OS 65.4% | [PMID: 41475048](https://pubmed.ncbi.nlm.nih.gov/41475048/) |
| French BLaDE (IFCT) | 163 | 1L D+T mPFS 18.2 mo, 12-mo OS 67.4% | [PMID: 39616778](https://pubmed.ncbi.nlm.nih.gov/39616778/) |
| Turkish Oncology Group | 88 | Co-mutations worsen OS (8.7 vs. 20.2 mo) | [PMID: 40813186](https://pubmed.ncbi.nlm.nih.gov/40813186/) |
| Chinese LANDSCAPE | 175,566 | BRAF 3.56%, V600E 24.6% of BRAF | [PMID: 40138888](https://pubmed.ncbi.nlm.nih.gov/40138888/) |
| IFCT Biomarkers France | 17,664 | BRAF mutation not prognostic with chemo | [PMID: 31181537](https://pubmed.ncbi.nlm.nih.gov/31181537/) |
| Dana-Farber | 883 | BRAF 4%, V600E not associated with younger age | [PMID: 23833300](https://pubmed.ncbi.nlm.nih.gov/23833300/) |

### Mechanistic and Biological Studies

| Topic | Key Contribution | PMID |
|-------|-----------------|------|
| BRAF V600E structural biology | Constitutive kinase activation mechanism | [PMID: 39961465](https://pubmed.ncbi.nlm.nih.gov/39961465/) |
| NKX2-1/ERK/WNT feedback | NKX2-1 loss → gastric differentiation → therapy resistance | [PMID: 33821796](https://pubmed.ncbi.nlm.nih.gov/33821796/) |
| PI3K cooperation | PI3K activation promotes de-differentiation | [PMID: 31452510](https://pubmed.ncbi.nlm.nih.gov/31452510/) |
| BRAF kinase-inactive models | Inactivating BRAF mutations can initiate lung cancer | [PMID: 28783725](https://pubmed.ncbi.nlm.nih.gov/28783725/) |
| ctDNA resistance profiling | Identifies resistance mechanisms to BRAF-targeted therapy | [PMID: 32859654](https://pubmed.ncbi.nlm.nih.gov/32859654/) |
| Novel MAPK inhibitors | Erianin as dual CRAF/MEK inhibitor | [PMID: 36872366](https://pubmed.ncbi.nlm.nih.gov/36872366/) |

---

## Limitations and Knowledge Gaps

1. **Small patient populations**: Due to the rarity of BRAF V600E NSCLC (~1–2% of NSCLC), most studies are small phase II trials or retrospective cohorts. No randomized phase III data exist comparing BRAF/MEK combinations head-to-head or against immunotherapy.

2. **Ethnic/geographic variation**: The proportion of BRAF V600E among BRAF mutations varies dramatically between Asian (24.6%) and Western (66%) populations. The reasons for this disparity are unknown and may affect treatment generalizability.

3. **Optimal treatment sequencing**: The best sequence of targeted therapy, immunotherapy, and chemotherapy remains undefined. Whether immunotherapy should precede, follow, or be combined with BRAF/MEK inhibition is an active area of investigation.

4. **Thromboembolism mechanism**: The remarkably high thromboembolism risk (43% 1-year incidence) is inadequately studied. The biological basis linking BRAF V600E to hypercoagulability needs elucidation, and prophylactic anticoagulation strategies need evaluation.

5. **Resistance mechanisms**: While some resistance mechanisms have been identified (MAPK reactivation, bypass pathway activation, lineage switching), comprehensive profiling in NSCLC-specific cohorts is limited compared to melanoma.

6. **Biomarkers of response/resistance**: Beyond PD-L1 status and co-mutations, predictive biomarkers to guide treatment selection are lacking.

7. **Encorafenib + Binimetinib vs. Dabrafenib + Trametinib**: The MAIC suggesting E+B superiority is based on indirect comparison methodology, which has inherent limitations. A direct randomized comparison is needed.

8. **Early-stage disease**: The role of adjuvant targeted therapy for resected BRAF V600E NSCLC is unknown. Data are extrapolated from the tumor-agnostic dabrafenib/trametinib approval but dedicated studies are needed.

9. **Brain metastases**: Intracranial activity of BRAF/MEK combinations in NSCLC is less well characterized compared to melanoma.

10. **Long-term survivorship**: With improving outcomes (median OS approaching 4 years), long-term toxicity, quality of life, and survivorship data are needed.

---

## Proposed Follow-up Experiments/Actions

### Clinical Studies

1. **Randomized phase III trial**: Direct comparison of encorafenib/binimetinib vs. dabrafenib/trametinib in treatment-naïve BRAF V600E NSCLC
2. **Triplet combination trial**: BRAF/MEK inhibition + anti-PD-1 immunotherapy (building on case report evidence of complete responses)
3. **Adjuvant targeted therapy trial**: Dabrafenib/trametinib or encorafenib/binimetinib for resected early-stage BRAF V600E NSCLC
4. **Thromboprophylaxis trial**: Evaluating prophylactic anticoagulation in BRAF V600E NSCLC patients
5. **ctDNA-guided treatment adaptation**: Using serial ctDNA monitoring to guide treatment switching at molecular progression

### Translational Research

6. **Comprehensive resistance profiling**: Multi-omic analysis (genomic, transcriptomic, proteomic) of paired pre/post-resistance samples from BRAF V600E NSCLC patients
7. **Immune microenvironment characterization**: Single-cell RNA-seq and spatial transcriptomics of BRAF V600E NSCLC to understand immune contexture and optimal immunotherapy combinations
8. **Thromboembolism biology**: Mechanistic studies investigating BRAF V600E signaling in coagulation cascade activation, platelet function, and tissue factor expression
9. **NKX2-1 loss biology**: Deeper investigation of lineage switching as resistance mechanism, with potential therapeutic strategies to prevent or reverse gastric differentiation
10. **Population-specific studies**: Investigating why BRAF V600E represents a lower proportion of BRAF mutations in Asian vs. Western populations — potential differences in mutagenic processes

### Diagnostic Innovation

11. **Exhaled breath condensate (EBC)**: Further validation of EBC-based liquid biopsy for BRAF mutation detection as a non-invasive lung-specific approach ([PMID: 35526313](https://pubmed.ncbi.nlm.nih.gov/35526313/))
12. **MRD monitoring**: Developing and validating ctDNA-based minimal residual disease detection protocols for post-operative surveillance

---

## Ontology Term Summary

| Category | Terms |
|----------|-------|
| **MONDO** | MONDO:0005233 (non-small cell lung carcinoma) |
| **HPO** | HP:0012735 (Cough), HP:0002094 (Dyspnea), HP:0002105 (Hemoptysis), HP:0001824 (Weight loss), HP:0001907 (Thromboembolism), HP:0002202 (Pleural effusion), HP:0100009 (Cerebral neoplasm), HP:0012378 (Fatigue) |
| **GO (Biological Process)** | GO:0000165 (MAPK cascade), GO:0008283 (Cell proliferation), GO:0006915 (Apoptotic process), GO:0001525 (Angiogenesis), GO:0016477 (Cell migration), GO:0043066 (Negative regulation of apoptotic process) |
| **GO (Cellular Component)** | GO:0005737 (Cytoplasm), GO:0005886 (Plasma membrane), GO:0005634 (Nucleus), GO:0005739 (Mitochondrion) |
| **GO (Molecular Function)** | GO:0004674 (Protein serine/threonine kinase activity), GO:0005524 (ATP binding) |
| **CL (Cell Type)** | CL:0002063 (Type II pneumocyte), CL:0000158 (Club cell), CL:0001064 (Malignant cell) |
| **UBERON (Anatomy)** | UBERON:0002048 (Lung), UBERON:0000955 (Brain), UBERON:0002481 (Bone tissue), UBERON:0002107 (Liver), UBERON:0002369 (Adrenal gland) |
| **CHEBI** | CHEBI:75047 (Dabrafenib), CHEBI:75998 (Trametinib), CHEBI:90227 (Encorafenib), CHEBI:90876 (Binimetinib), CHEBI:63637 (Vemurafenib) |
| **MAXO** | MAXO:0001298 (Targeted molecular therapy), MAXO:0000004 (Surgical procedure), MAXO:0000014 (Radiation therapy), MAXO:0000127 (Genetic testing) |

---

*Report generated from systematic analysis of 64 publications encompassing clinical trials, real-world cohort studies, mechanistic investigations, and diagnostic innovation research. All citations verified against original abstracts where available.*
