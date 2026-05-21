---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-06T08:23:46.352353'
end_time: '2026-05-06T09:49:06.280008'
duration_seconds: 5119.93
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: RET-Rearranged Non-Small Cell Lung Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
citation_count: 51
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RET-Rearranged Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **RET-Rearranged Non-Small Cell Lung Cancer** covering all of the
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

# Comprehensive Disease Profile: RET-Rearranged Non-Small Cell Lung Cancer

---

## Summary

**RET-rearranged non-small cell lung cancer (NSCLC)** is a rare but highly actionable molecular subtype affecting approximately 1–2% of NSCLC patients, predominantly presenting as lung adenocarcinoma in younger, female, never-smoking individuals. The disease is driven by somatic chromosomal rearrangements — most commonly intrachromosomal inversions on chromosome 10 — that fuse the RET receptor tyrosine kinase gene with partner genes such as KIF5B (47–62%), CCDC6 (20–28%), and NCOA4 (6–14%), producing constitutively active chimeric kinases that aberrantly activate RAS-MAPK, PI3K-AKT, and PLCγ signaling cascades to promote uncontrolled cell proliferation, survival, and migration.

The treatment landscape has been revolutionized by selective RET tyrosine kinase inhibitors. Selpercatinib demonstrated superior progression-free survival (PFS) of 24.8 months versus 11.2 months for chemotherapy ± pembrolizumab (HR 0.46, P<0.001) in the phase 3 LIBRETTO-431 trial, with an objective response rate (ORR) of 84% in treatment-naïve patients and robust intracranial activity (ORR 85%). Pralsetinib, the second FDA-approved selective RET inhibitor, achieved an ORR of 72% in treatment-naïve patients in the ARROW trial. Real-world data confirm a survival benefit with selective RET inhibitors (median OS 34.3 vs. 17.5 months without targeted therapy, p=0.002), while immunotherapy alone shows minimal benefit due to the characteristically immune-cold tumor microenvironment (low TMB, poor T-cell infiltration).

Resistance inevitably emerges, primarily through on-target RET G810 solvent front mutations (G810R/S/C) and off-target bypass pathways including MET amplification, KRAS amplification, and AXL/IGF-1R activation. Next-generation RET inhibitors such as vepafestinib and APS03118, designed to overcome G810 resistance mutations, are advancing through clinical development. This report synthesizes findings from 96 peer-reviewed publications across 15 disease characteristic domains to provide a comprehensive knowledge base entry for RET-rearranged NSCLC.

---

## 1. Disease Information

### Overview

RET-rearranged NSCLC is a molecular subtype of non-small cell lung cancer defined by somatic chromosomal rearrangements involving the *RET* (REarranged during Transfection) proto-oncogene on chromosome 10q11.21. These rearrangements create oncogenic fusion proteins with constitutive kinase activity that drive tumorigenesis. The KIF5B-RET fusion was first identified in 2012 by Ju et al. through whole-genome and transcriptome sequencing of a lung adenocarcinoma from a 33-year-old never-smoker, revealing "a novel fusion gene between KIF5B and the RET proto-oncogene caused by a pericentric inversion of 10p11.22-q11.21" that "overexpresses chimeric RET receptor tyrosine kinase, which could spontaneously induce cellular transformation" ([PMID: 22194472](https://pubmed.ncbi.nlm.nih.gov/22194472/)). Suehara et al. independently identified KIF5B-RET through a systematic NanoString-based screen for tyrosine kinase fusions in pan-negative lung adenocarcinomas ([PMID: 23052255](https://pubmed.ncbi.nlm.nih.gov/23052255/)).

### Key Identifiers

| Database | Identifier |
|---|---|
| **ICD-10** | C34 (Malignant neoplasm of bronchus and lung) |
| **ICD-11** | 2C25 (Malignant neoplasms of bronchus or lung) |
| **ICD-O-3** | 8140/3 (Adenocarcinoma, NOS) — most common histologic subtype |
| **MeSH** | D002289 (Carcinoma, Non-Small-Cell Lung) |
| **MONDO** | MONDO:0005233 (non-small cell lung carcinoma) — no specific MONDO ID for RET-rearranged subset |
| **OMIM** | 164761 (RET proto-oncogene) |
| **Orphanet** | ORPHA:70573 (Non-small cell lung carcinoma) |

### Synonyms and Alternative Names

- RET fusion-positive NSCLC
- RET-rearranged lung adenocarcinoma
- RET translocation-positive NSCLC
- RET+ NSCLC
- Non-small cell lung cancer with RET rearrangement

### Data Source Type

Disease-level aggregated resources, including clinical trial data, molecular profiling databases (e.g., COSMIC, TCGA, cBioPortal), real-world observational studies, and systematic literature reviews across 96 publications.

---

## 2. Etiology

### Disease Causal Factors

RET-rearranged NSCLC is caused by **somatic (acquired) chromosomal rearrangements** (inversions or translocations) that fuse the 3' kinase domain of the *RET* gene with the 5' portion of various partner genes. The resulting fusion protein retains the catalytic kinase activity of RET but is expressed under control of the partner gene's promoter, leading to ligand-independent constitutive activation of RET signaling. RET fusions occur in "1-2% of non-small cell lung carcinoma" ([PMID: 40544107](https://pubmed.ncbi.nlm.nih.gov/40544107/)).

The most common fusion partners and their frequencies are:

| Fusion | Frequency in NSCLC | Chromosomal Event |
|---|---|---|
| **KIF5B-RET** | ~47-62% | inv(10)(p11.22q11.21) |
| **CCDC6-RET** | ~20-28% | inv(10)(q11.21q21) |
| **NCOA4-RET** | ~6-14% | inv(10)(q11.21q11.2) |
| **Other partners** (TRIM33, ERC1, RUFY2, etc.) | ~5-10% | Interchromosomal translocations |

"KIF5B (46.8%) was the most common fusion partner followed by CCDC6 (28.3%) and NCOA4 (13.8%) in RET+ solid tumors. KIF5B-RET was the dominant fusion variant in RET+ NSCLC" ([PMID: 37516008](https://pubmed.ncbi.nlm.nih.gov/37516008/)). In Chinese NSCLC, KIF5B-RET accounts for 59.4% of cases ([PMID: 39497173](https://pubmed.ncbi.nlm.nih.gov/39497173/)).

#### Fusion Partner Gene Biology

All three major fusion partners reside on chromosome 10, explaining the predominance of intrachromosomal pericentric inversions:

| Partner Gene | NCBI Gene ID | Chromosome | Normal Function | Mechanism in Fusion |
|---|---|---|---|---|
| **KIF5B** | 3799 | 10p11.22 | Kinesin-1 heavy chain; microtubule-dependent transport | Coiled-coil domain mediates constitutive dimerization; ubiquitous promoter drives high-level expression |
| **CCDC6** | 8030 | 10q21.2 | DNA damage response; potential tumor suppressor | Loss of tumor suppressor function + coiled-coil drives RET dimerization |
| **NCOA4** | 8031 | 10q11.2 | Androgen receptor coactivator; mediates ferritinophagy | Coiled-coil domain forces ligand-independent RET dimerization |

### Risk Factors

#### Genetic Risk Factors
- **Somatic RET gene fusions** (driver alteration; not a germline predisposition)
- **Co-occurring TP53 mutations** (39.0% of cases) and **CDKN2A alterations** (13.0%), which may modify disease behavior
- "Concomitant mutations were identified in 28.7% of patients, most commonly TP53 (39.0%) and CDKN2A (13.0%), with CDKN2A alterations predominantly consisting of functionally inactivating SNVs concurrent with shallow deletions more enriched in non-KIF5B (p = 0.0393)" ([PMID: 41707338](https://pubmed.ncbi.nlm.nih.gov/41707338/))
- RET fusions are generally mutually exclusive with other oncogenic drivers (EGFR, ALK, ROS1, KRAS)

#### Environmental Risk Factors
- **Notably enriched in never-smokers** (60.8% never/light smokers) ([PMID: 41707338](https://pubmed.ncbi.nlm.nih.gov/41707338/)), distinguishing it from smoking-associated lung cancers
- Younger age at diagnosis (median 58 years)
- Female sex predominance (57.0%)
- No specific occupational or environmental exposure linked to RET rearrangement formation

### Protective Factors

No specific genetic or environmental protective factors have been identified for RET-rearranged NSCLC. General lung cancer protective factors (smoking avoidance, reduced air pollution exposure) apply broadly.

### Gene-Environment Interactions

RET fusions occur predominantly in never/light smokers, suggesting they arise through mechanisms independent of tobacco carcinogenesis (which more commonly drives KRAS mutations and high TMB). The precise molecular triggers for RET rearrangements remain unclear. Prior ionizing radiation exposure has been associated with RET fusions in thyroid cancer (post-Chernobyl), but this association has not been established for NSCLC.

---

## 3. Phenotypes

### Symptoms and Clinical Signs

| Phenotype | HPO Term | Frequency | Onset | Severity |
|---|---|---|---|---|
| Cough | HP:0012735 | ~50-65% | Variable | Mild to moderate |
| Dyspnea | HP:0002094 | ~40-55% | Progressive | Moderate to severe |
| Hemoptysis | HP:0002105 | ~15-20% | Variable | Variable |
| Chest pain | HP:0100749 | ~25-30% | Variable | Moderate |
| Weight loss | HP:0001824 | ~20-35% | Insidious | Moderate |
| Fatigue | HP:0012378 | ~30-45% | Insidious | Mild to moderate |
| Bone pain (metastases) | HP:0002653 | ~12% | Late | Moderate to severe |
| Headache/neurological symptoms (brain metastases) | HP:0002315 | ~7-25% | Late | Variable |
| Pleural effusion | HP:0002202 | ~12-20% | Variable | Moderate |

### Phenotype Characteristics

- **Age of onset**: Predominantly adult-onset; median age 58 years, somewhat younger than unselected NSCLC (median ~70 years). Enrichment in patients ≤40 years has been demonstrated ([PMID: 28177518](https://pubmed.ncbi.nlm.nih.gov/28177518/), [PMID: 40122770](https://pubmed.ncbi.nlm.nih.gov/40122770/))
- **Severity**: Variable; many patients present with advanced (stage III-IV) disease
- **Histology**: Almost exclusively adenocarcinoma
- **Metastatic pattern**: "Bone (12.3%), pleural (11.9%), and brain metastases (6.7%) were the most common metastatic sites" ([PMID: 41707338](https://pubmed.ncbi.nlm.nih.gov/41707338/))
- **Brain metastases**: Notable propensity for CNS involvement; up to 25-30% during disease course. Brain metastases are a common pattern of treatment failure ([PMID: 39563271](https://pubmed.ncbi.nlm.nih.gov/39563271/))

### Quality of Life Impact

Patient-reported outcome (PRO) data from clinical trials demonstrate significant QoL impacts and treatment-related improvements:

- **LIBRETTO-431 PRO analysis**: Selpercatinib "delayed TTCD of all individual NSCLC-SAQ symptoms versus control. A clinically meaningful improvement in the NSCLC-SAQ total score (mean difference = -2.00, 95% confidence interval [CI]: -2.94 to -1.05) was also observed at 1 year for selpercatinib versus control" ([PMID: 40567260](https://pubmed.ncbi.nlm.nih.gov/40567260/))
- **LIBRETTO-001 PRO analysis**: "The percentage of patients who experienced clinically meaningful improvements ranged from 61.1% to 66.7% for global health status, 33.3% to 61.1% for dyspnea, and 46.2% to 63.0% for pain" ([PMID: 34523767](https://pubmed.ncbi.nlm.nih.gov/34523767/))
- **Chinese patients (LIBRETTO-321)**: 47.4% showed definite improvement in global health status with <20% showing worsening; >64% of patients either improved or remained stable for symptoms ([PMID: 37655205](https://pubmed.ncbi.nlm.nih.gov/37655205/))

---

## 4. Genetic/Molecular Information

### Causal Gene

- **RET** (REarranged during Transfection)
  - HGNC ID: HGNC:9967
  - NCBI Gene ID: 5979
  - OMIM: 164761
  - UniProt: P07949 (RET_HUMAN)
  - Chromosome: 10q11.21
  - Encodes: Proto-oncogene tyrosine-protein kinase receptor Ret (1114 amino acids)

**Normal RET function**: RET is "a receptor tyrosine kinase essential for normal development of the kidneys, ureters, peripheral and enteric nervous systems" ([PMID: 24022366](https://pubmed.ncbi.nlm.nih.gov/24022366/)). "RET signalling is crucial for the development of the enteric nervous system. RET also regulates the development of sympathetic, parasympathetic, motor, and sensory neurons, and is necessary for the postnatal maintenance of dopaminergic neurons" ([PMID: 17934909](https://pubmed.ncbi.nlm.nih.gov/17934909/)).

#### RET Protein Domain Architecture

| Domain | Position (aa) | Function |
|---|---|---|
| Signal peptide | 1-28 | Secretory pathway targeting |
| Cadherin-like domains | 168-510 | Extracellular; GFRα coreceptor interaction |
| Cysteine-rich domain | ~510-635 | Extracellular; ligand binding |
| Transmembrane domain | ~636-657 | Single-pass membrane anchor |
| Protein kinase domain | 724-1016 | Intracellular; catalytic tyrosine kinase |

#### Structural Biology

| PDB ID | Resolution | Complex | Significance |
|---|---|---|---|
| **7JU6** | 2.06 Å | RET kinase + selpercatinib | Co-crystal revealing selpercatinib binding mode and G810 resistance basis |
| **7JU5** | 1.90 Å | RET kinase + pralsetinib | Co-crystal showing pralsetinib ATP-competitive binding |
| **6Q2J** | ~4.0 Å | RET ECD + GFRα1 + GDNF | Cryo-EM of ternary signaling complex |

### Pathogenic Variants — Fusion Rearrangements

All RET fusions in NSCLC are **somatic** (acquired), distinguishing them from germline RET point mutations that cause MEN2A/2B and hereditary medullary thyroid carcinoma ([PMID: 40102258](https://pubmed.ncbi.nlm.nih.gov/40102258/)).

**Functional consequence**: Gain of function — the partner gene's coiled-coil/oligomerization domain replaces RET's extracellular ligand-binding domain, forcing constitutive, ligand-independent dimerization and autophosphorylation of the retained intracellular kinase domain.

### Acquired Resistance Mutations

| Mutation | Location | Effect | Clinical Relevance |
|---|---|---|---|
| **G810R** | Solvent front | Steric clash with selpercatinib/pralsetinib | Most frequent G810 variant |
| **G810S** | Solvent front | Steric clash | Common |
| **G810C** | Solvent front | Steric clash | Common |
| **G810D** | Solvent front | Resistant to both approved TKIs | Rare ([PMID: 37070927](https://pubmed.ncbi.nlm.nih.gov/37070927/)) |
| **G810V** | Solvent front | NOT resistant (surprisingly) | Rare ([PMID: 37070927](https://pubmed.ncbi.nlm.nih.gov/37070927/)) |
| **V804L/M** | Gatekeeper | Resistant to multi-kinase inhibitors; sensitive to selective RET TKIs | Historical |

"Analysis of circulating tumor DNA revealed emergence of RET G810R, G810S, and G810C mutations in the RET solvent front before the emergence of clinical resistance" ([PMID: 31988000](https://pubmed.ncbi.nlm.nih.gov/31988000/)).

### Modifier Genes and Co-occurring Alterations

- **TP53** (39.0%) — most common co-occurring alteration; associated with worse prognosis
- **CDKN2A** (13.0%) — more enriched in non-KIF5B fusions (p=0.0393)
- **RASA1** (14.3%) and **ARID1A** (11.6%) — additional co-occurring alterations ([PMID: 37516008](https://pubmed.ncbi.nlm.nih.gov/37516008/))

### Epigenetic Information

- Limited RET fusion-specific epigenetic data
- SMARCA4 loss (chromatin remodeling defect) identified in 55% of post-TKI resistant tumors ([PMID: 38768929](https://pubmed.ncbi.nlm.nih.gov/38768929/))
- The partner gene's promoter and epigenetic landscape drives expression of the chimeric protein

### Chromosomal Abnormalities

RET fusions arise from pericentric inversions of chromosome 10 (for KIF5B-RET, CCDC6-RET) or inter-chromosomal translocations (for partners on other chromosomes). These are focal rearrangements, not large-scale aneuploidy.

---

## 5. Environmental Information

### Environmental Factors
- No specific environmental toxins definitively linked to RET rearrangement formation
- RET-rearranged NSCLC occurs predominantly in never-smokers
- Prior ionizing radiation associated with RET fusions in thyroid cancer (post-Chernobyl) but not established for NSCLC

### Lifestyle Factors
- **Smoking**: Enriched in never/light smokers (60.8%), similar to ALK- and ROS1-rearranged NSCLC
- No specific dietary, exercise, or alcohol associations

### Infectious Agents
- Not applicable; no infectious agents causally linked

---

## 6. Mechanism / Pathophysiology

### Causal Chain: From Genomic Event to Clinical Disease

```
UPSTREAM TRIGGER
    Somatic chromosomal rearrangement (inv/translocation on chr 10)
         ↓
    RET fusion gene expression (e.g., KIF5B-RET)
         ↓
    Partner coiled-coil domain → constitutive dimerization
         ↓
    Ligand-independent RET kinase autophosphorylation (Y905, Y1015, Y1062, Y1096)
         ↓
SIGNALING CASCADE
    ├── RAS → RAF → MEK → ERK (proliferation)
    ├── PI3K → AKT → mTOR (survival/growth)
    ├── PLCγ → DAG + IP3 → PKC (signaling)
    ├── JAK → STAT3 (immune evasion)
    └── SRC → FAK (invasion/metastasis)
         ↓
DOWNSTREAM EFFECTS
    ├── Uncontrolled proliferation
    ├── Evasion of apoptosis
    ├── Angiogenesis
    ├── Immune-cold microenvironment (low TMB, poor T-cell infiltration)
    └── Metastasis (bone, pleura, brain)
         ↓
CLINICAL MANIFESTATION
    Advanced lung adenocarcinoma with metastatic disease
```

"This activated complex regulates a number of downstream signaling cascades (PLCγ, MAPK, and PI3K) that control proliferation, migration, renewal, and apoptosis" ([PMID: 24022366](https://pubmed.ncbi.nlm.nih.gov/24022366/)).

### Molecular Pathways

| Pathway | KEGG ID | Role in Tumorigenesis |
|---|---|---|
| RAS-MAPK (ERK1/2) | hsa04010 | Cell proliferation, differentiation |
| PI3K-AKT-mTOR | hsa04151 | Cell survival, metabolism, growth |
| PLCγ-PKC | — | Calcium signaling, proliferation |
| JAK-STAT3 | hsa04630 | Survival, immune evasion |
| SRC signaling | — | Migration, invasion, adhesion |

### Immune System Involvement — Immune-Cold Phenotype

RET-fusion NSCLC is characterized by a distinctly **immune-cold tumor microenvironment**:

- "Genomic predictors of poor response included EGFR and ALK/RET/ROS1 fusions... all linked to immune-cold phenotypes with low tumor mutational burden (TMB) and poor T-cell infiltration" ([PMID: 41424613](https://pubmed.ncbi.nlm.nih.gov/41424613/))
- "EGFR-sensitizing mutations, ALK, RET, and ROS1 rearrangements were associated with lower TMB and PD-L1+/TMB-H proportions" ([PMID: 33655698](https://pubmed.ncbi.nlm.nih.gov/33655698/))
- Real-world confirmation: "there was no difference between patients treated with immunotherapy versus untreated patients" in overall survival ([PMID: 35838839](https://pubmed.ncbi.nlm.nih.gov/35838839/))
- Single-cell RNA-seq of rare-driver NSCLC tumors after anti-PD-1 treatment identified GZMK+ CD8 T-cells as key expanded population ([PMID: 40021042](https://pubmed.ncbi.nlm.nih.gov/40021042/))

### Resistance Mechanisms

Multiple resistance pathways emerge after selective RET inhibitor therapy:

| Mechanism | Type | Frequency | Evidence |
|---|---|---|---|
| **RET G810R/S/C** | On-target (solvent front) | Most common | [PMID: 31988000](https://pubmed.ncbi.nlm.nih.gov/31988000/) |
| **MET amplification** | Off-target bypass | ~15% | [PMID: 33007380](https://pubmed.ncbi.nlm.nih.gov/33007380/) |
| **KRAS amplification** | Off-target bypass | Rare | [PMID: 33007380](https://pubmed.ncbi.nlm.nih.gov/33007380/) |
| **AXL activation** | Off-target bypass | Clone-specific | [PMID: 38768929](https://pubmed.ncbi.nlm.nih.gov/38768929/) |
| **IGF-1R activation** | Off-target bypass | Clone-specific | [PMID: 38768929](https://pubmed.ncbi.nlm.nih.gov/38768929/) |
| **SMARCA4 loss** | Chromatin remodeling | 55% post-TKI | [PMID: 38768929](https://pubmed.ncbi.nlm.nih.gov/38768929/) |
| **Mitochondrial dysfunction** | Metabolic | Clone-specific | [PMID: 38768929](https://pubmed.ncbi.nlm.nih.gov/38768929/) |
| **EGFR reactivation** | Off-target feedback | Variable | [PMID: 28428274](https://pubmed.ncbi.nlm.nih.gov/28428274/) |

"Three resistant cases (15%) harbored acquired MET amplification without concurrent RET resistance mutations, and one specimen had acquired KRAS amplification" ([PMID: 33007380](https://pubmed.ncbi.nlm.nih.gov/33007380/)).

### Relevant GO Terms

- GO:0006468 (Protein phosphorylation)
- GO:0007169 (Transmembrane receptor protein tyrosine kinase signaling pathway)
- GO:0008283 (Cell population proliferation)
- GO:0006915 (Apoptotic process — dysregulated)
- GO:0001525 (Angiogenesis)
- GO:0001837 (Epithelial to mesenchymal transition)

### Relevant Cell Types (CL Terms)

- CL:0002063 (Type II pneumocyte) — proposed cell of origin
- CL:0002328 (Bronchial epithelial cell)
- CL:0000625 (CD8-positive, alpha-beta T cell) — reduced in TME
- CL:0000235 (Macrophage) — tumor-associated macrophages

---

## 7. Anatomical Structures Affected

### Organ Level

| Level | Structure | UBERON Term | Involvement |
|---|---|---|---|
| **Primary** | Lung | UBERON:0002048 | Primary site of adenocarcinoma |
| **Secondary** | Bone | UBERON:0002481 | Most common metastatic site (12.3%) |
| | Pleura | UBERON:0000977 | Second most common (11.9%) |
| | Brain | UBERON:0000955 | Third most common (6.7%); up to 25-30% over disease course |
| | Liver | UBERON:0002107 | Common distant metastasis |
| | Adrenal glands | UBERON:0002369 | Occasional metastatic site |
| | Lymph nodes | UBERON:0000029 | Regional and distant spread |

**Body system**: Respiratory system (UBERON:0001004)

### Tissue and Cell Level

- **Tissue**: Glandular epithelium (adenocarcinoma pattern); lepidic, acinar, papillary, micropapillary, and solid patterns
- **Cell of origin**: CL:0002063 (Type II pneumocyte)
- **Affected cells**: CL:0002328 (Bronchial epithelial cell), CL:0000066 (Epithelial cell)

### Subcellular Level

| Compartment | GO Cellular Component | Relevance |
|---|---|---|
| Plasma membrane | GO:0005886 | RET fusion protein localization |
| Cytoplasm | GO:0005737 | Downstream signaling cascades |
| Nucleus | GO:0005634 | Transcription factor activation |
| Endosome membrane | GO:0010008 | RET internalization and signaling |
| Mitochondria | GO:0005739 | Dysfunction in resistance |

### Localization
- Predominantly peripheral lung nodules/masses
- Typically unilateral at diagnosis
- Metastatic spread: bilateral lung, skeletal, CNS

---

## 8. Temporal Development

### Onset
- **Typical age of onset**: Adult, median 58 years ([PMID: 41707338](https://pubmed.ncbi.nlm.nih.gov/41707338/)); enriched in younger patients <40 years ([PMID: 28177518](https://pubmed.ncbi.nlm.nih.gov/28177518/), [PMID: 40122770](https://pubmed.ncbi.nlm.nih.gov/40122770/))
- **Onset pattern**: Insidious; symptoms develop gradually as tumor grows

### Progression

| Stage (AJCC 8th Edition) | Approximate Proportion at Diagnosis |
|---|---|
| Stage I-II | ~15-25% |
| Stage III | ~15-20% |
| Stage IV | ~55-65% |

- **Progression rate**: Variable; untreated tumors progress over months
- **Disease course**: Progressive without treatment; with selective RET inhibitors, durable responses are achievable (median PFS >20 months first-line)
- **Disease duration**: Chronic; requires ongoing treatment

### Treatment-Modulated Progression

| Setting | Median PFS | ORR |
|---|---|---|
| Selpercatinib 1L (LIBRETTO-431) | 24.8 months | 84% |
| Selpercatinib 2L+ (LIBRETTO-001) | 24.9 months | 61% |
| Pralsetinib 1L (ARROW) | 13.0 months | 72% |
| Pralsetinib 2L+ (ARROW) | 16.5 months | 59% |
| Chemotherapy ± pembrolizumab (control) | 11.2 months | 65% |

### Critical Periods
- **Early molecular testing window**: Comprehensive genomic profiling at diagnosis is critical for timely identification and initiation of targeted therapy
- **Resistance emergence**: Typically after 1-2 years on selective RET inhibitors; ctDNA monitoring can detect resistance mutations before clinical progression ([PMID: 35242632](https://pubmed.ncbi.nlm.nih.gov/35242632/))

---

## 9. Inheritance and Population

### Epidemiology

| Parameter | Value | Source |
|---|---|---|
| **Prevalence among NSCLC** | 1-2% | [PMID: 40544107](https://pubmed.ncbi.nlm.nih.gov/40544107/) |
| **Estimated new cases/year (US)** | ~2,300-4,600 | Based on ~230,000 new NSCLC cases/year |
| **Estimated new cases/year (global)** | ~18,000-36,000 | Based on ~1.8M new lung cancer cases/year |

### Genetic Considerations
- **Somatic, not inherited**: RET fusions in NSCLC are exclusively somatic events — NOT inherited
- **Distinction from germline RET mutations**: Germline gain-of-function point mutations in RET cause MEN2A/2B and familial medullary thyroid carcinoma (autosomal dominant, high penetrance) ([PMID: 40102258](https://pubmed.ncbi.nlm.nih.gov/40102258/)). These are entirely distinct from somatic RET fusions in NSCLC.

### Population Demographics

- **Sex ratio**: Female predominant (57.0% female) ([PMID: 41707338](https://pubmed.ncbi.nlm.nih.gov/41707338/))
- **Age distribution**: Median 58 years; enriched in younger patients; "a striking enrichment of fusions (ALK and RET) in young-onset LC" was confirmed in Indian patients ≤40 years ([PMID: 40122770](https://pubmed.ncbi.nlm.nih.gov/40122770/))
- **Smoking status**: 60.8% never/light smokers ([PMID: 41707338](https://pubmed.ncbi.nlm.nih.gov/41707338/))
- **Geographic distribution**: Global; ~1-2% prevalence consistent across regions. RET fusion frequency ~2% in Hispanic/Latino NSCLC ([PMID: 37729688](https://pubmed.ncbi.nlm.nih.gov/37729688/)). Consistent features confirmed in Latin American cohort ([PMID: 41005103](https://pubmed.ncbi.nlm.nih.gov/41005103/))

---

## 10. Diagnostics

### Molecular Testing (Essential)

RET fusion detection is required for diagnosis and treatment selection. "Currently, four methods are widely used for detecting gene rearrangements: next-generation sequencing (NGS), reverse transcription-polymerase chain reaction (RT-PCR), fluorescence in situ hybridization (FISH), and immunohistochemistry (IHC)" ([PMID: 37718634](https://pubmed.ncbi.nlm.nih.gov/37718634/)).

| Method | Sensitivity | Specificity | Advantages | Limitations |
|---|---|---|---|---|
| **RNA-based NGS** (preferred) | High (~95%) | High (>99%) | Detects all partners; multiplexed | Requires adequate tissue; RNA quality |
| **DNA-based NGS** | Moderate-High | High | Part of comprehensive panels; detects co-mutations | May miss some fusions |
| **FISH (break-apart)** | Moderate (~80%) | Moderate-High | Works on small specimens | Cannot identify fusion partner |
| **RT-PCR** | High (known fusions) | High | Rapid, cost-efficient | Cannot detect novel partners |
| **IHC** | Low-Moderate | Low-Moderate | Screening only | Not validated for RET in NSCLC |

"Targeted RNA NGS was confirmed to be the most efficient technique for gene fusion identification in clinical practice" ([PMID: 37190044](https://pubmed.ncbi.nlm.nih.gov/37190044/)). Sequential DNA→RNA NGS testing increased driver detection to 66% of NSCLC patients ([PMID: 34536732](https://pubmed.ncbi.nlm.nih.gov/34536732/)).

### Liquid Biopsy
- cfDNA NGS can detect RET fusions in plasma but has "limited sensitivity for ALK, ROS1, RET, and NTRK rearrangements" compared to point mutations ([PMID: 40944810](https://pubmed.ncbi.nlm.nih.gov/40944810/))
- Useful for monitoring acquired resistance mutations (RET G810, MET amplification)
- Liquid biopsy turnaround time significantly shorter (8.18 vs 19.75 days) ([PMID: 40944810](https://pubmed.ncbi.nlm.nih.gov/40944810/))

### Imaging Studies
- CT chest/abdomen/pelvis: Standard staging and response monitoring
- Brain MRI: Recommended at baseline due to CNS metastasis propensity
- PET-CT: Staging and metabolic assessment

### Histopathology
- Predominantly adenocarcinoma; TTF-1 positive, CK7 positive
- PD-L1 testing: Often low expression in RET-rearranged NSCLC

### Differential Diagnosis
Other oncogene-driven NSCLC subtypes (generally mutually exclusive): ALK-rearranged, ROS1-rearranged, NTRK fusion-positive, EGFR-mutated, KRAS G12C-mutated, MET exon 14 skipping, BRAF V600E-mutated, HER2-mutated NSCLC. Comprehensive molecular profiling distinguishes these.

### Screening
- LDCT screening for lung cancer targets high-risk smokers; most RET-fusion patients are never-smokers who would not meet current screening criteria
- Reflexive molecular testing of all newly diagnosed advanced NSCLC is recommended by NCCN, ESMO, and IASLC guidelines

---

## 11. Outcome/Prognosis

### Survival and Mortality

| Outcome Metric | Value | Setting | Source |
|---|---|---|---|
| **Median OS (selective RET TKI)** | 34.3 months | Real-world | [PMID: 35838839](https://pubmed.ncbi.nlm.nih.gov/35838839/) |
| **Median OS (no RET-targeted therapy)** | 17.5 months | Real-world | [PMID: 35838839](https://pubmed.ncbi.nlm.nih.gov/35838839/) |
| **Median OS (selpercatinib, MAIC)** | Not reached | Indirect comparison | [PMID: 40458063](https://pubmed.ncbi.nlm.nih.gov/40458063/) |
| **Median OS (pralsetinib, MAIC)** | 43.9 months | Indirect comparison | [PMID: 40458063](https://pubmed.ncbi.nlm.nih.gov/40458063/) |
| **1-year OS (pralsetinib, real-world)** | 64.3% | Chinese cohort | [PMID: 39497173](https://pubmed.ncbi.nlm.nih.gov/39497173/) |

"Overall survival was prolonged in patients treated with selective RET inhibitors versus untreated patients (median 34.3 versus 17.5 months; p = 0.002) during a median follow-up of 28.7 months. But there was no difference between patients treated with immunotherapy versus untreated patients" ([PMID: 35838839](https://pubmed.ncbi.nlm.nih.gov/35838839/)).

### Key Efficacy Data

**Selpercatinib (LIBRETTO-001, extended follow-up, [PMID: 36122315](https://pubmed.ncbi.nlm.nih.gov/36122315/)):**
- Treatment-naïve: ORR 84% (95% CI 73-92), 6% CR, median DoR 20.2 months, median PFS 22.0 months
- Previously treated: ORR 61% (55-67), 7% CR, median DoR 28.6 months, median PFS 24.9 months
- Intracranial ORR: 85% (65-96) with 27% CR in measurable CNS metastases

"In treatment-naive patients, the ORR was 84% (95% CI, 73 to 92); 6% achieved complete responses (CRs). The median DoR was 20.2 months (95% CI, 13.0 to could not be evaluated); 40% of responses were ongoing at the data cutoff" ([PMID: 36122315](https://pubmed.ncbi.nlm.nih.gov/36122315/))

**Selpercatinib (LIBRETTO-431, [PMID: 37870973](https://pubmed.ncbi.nlm.nih.gov/37870973/)):**
- First-line: "median progression-free survival was 24.8 months (95% CI, 16.9 to not estimable) with selpercatinib and 11.2 months (95% CI, 8.8 to 16.8) with control treatment (hazard ratio for progression or death, 0.46; 95% CI, 0.31 to 0.70; P<0.001)"

**Pralsetinib (ARROW, [PMID: 35973665](https://pubmed.ncbi.nlm.nih.gov/35973665/)):**
- Treatment-naïve: ORR 72% (60-82%), median PFS 13.0 months
- Previously treated: ORR 59% (50-67%), median PFS 16.5 months

**Indirect comparison**: PFS 22.1 vs 13.3 months for selpercatinib vs pralsetinib (HR 0.67; 95% CI 0.53-0.85) ([PMID: 40458063](https://pubmed.ncbi.nlm.nih.gov/40458063/))

**Meta-analysis of selective RET inhibitors**: Combined ORR 67%, DCR 92%, mPFS 16.09 months, intracranial ORR 86% ([PMID: 37603207](https://pubmed.ncbi.nlm.nih.gov/37603207/))

### Prognostic Factors
- **Positive**: Good ECOG performance status, treatment-naïve status, absence of brain metastases
- **Negative**: TP53 co-mutation, brain metastases at baseline, poor ECOG PS (p=0.018) ([PMID: 39563271](https://pubmed.ncbi.nlm.nih.gov/39563271/)), prior treatment ([PMID: 39926433](https://pubmed.ncbi.nlm.nih.gov/39926433/))

---

## 12. Treatment

### Selective RET Inhibitors (First-Generation, FDA-Approved)

#### Selpercatinib (LOXO-292, Retevmo®)
- **Class**: Selective RET kinase inhibitor (MAXO:0001001)
- **Dose**: 160 mg BID orally, continuous 28-day cycles
- **FDA approval**: May 2020 (accelerated); tumor-agnostic for all RET-fusion solid tumors
- **Key trials**: LIBRETTO-001 (NCT03157128), LIBRETTO-431 (NCT04194944)
- **East Asian subgroup**: Consistent efficacy, HR 0.38 (95% CI 0.22-0.68) ([PMID: 40980186](https://pubmed.ncbi.nlm.nih.gov/40980186/))

#### Pralsetinib (BLU-667, Gavreto®)
- **Class**: Selective RET kinase inhibitor (MAXO:0001001)
- **Dose**: 400 mg QD orally
- **FDA approval**: September 2020 (accelerated)
- **Key trial**: ARROW (NCT03037385)
- **Chinese patients**: Treatment-naïve ORR 83.3% ([PMID: 37282666](https://pubmed.ncbi.nlm.nih.gov/37282666/))

### Safety Profile Comparison

| Parameter | Selpercatinib | Pralsetinib |
|---|---|---|
| Grade ≥3 TRAEs | 39.3% | 62.6% |
| Discontinuation due to TRAEs | 3.6% | 10.0% |
| Key grade ≥3 AEs | Hypertension, elevated ALT/AST | Neutropenia, anemia, hypertension |

([PMID: 40458063](https://pubmed.ncbi.nlm.nih.gov/40458063/))

### Multi-Kinase Inhibitors (Historical)
- Cabozantinib, vandetanib, lenvatinib: Modest activity (ORR ~18-30%); higher off-target toxicity
- Alectinib at high doses showed "limited activity in advanced RET-fusion positive NSCLC" ([PMID: 38405208](https://pubmed.ncbi.nlm.nih.gov/38405208/))
- Largely supplanted by selective RET inhibitors

### Immunotherapy
- Generally **ineffective** in RET-fusion NSCLC due to immune-cold phenotype
- No OS benefit vs untreated patients ([PMID: 35838839](https://pubmed.ncbi.nlm.nih.gov/35838839/))
- LIBRETTO-431 confirmed selpercatinib superiority over chemo + pembrolizumab ([PMID: 38807655](https://pubmed.ncbi.nlm.nih.gov/38807655/))

### Next-Generation RET Inhibitors (Overcoming G810 Resistance)

| Agent | Key Features | Status |
|---|---|---|
| **Vepafestinib (TAS0953/HM06)** | "Best-in-class selectivity against RET, while exerting activity against commonly reported on-target resistance mutations" and high CNS penetration ([PMID: 37743366](https://pubmed.ncbi.nlm.nih.gov/37743366/)) | Phase 1/2 |
| **APS03118** | Novel tricyclic scaffold; potent against wild-type and mutant RET ([PMID: 40920215](https://pubmed.ncbi.nlm.nih.gov/40920215/)) | Preclinical/Early clinical |
| **HSN608** | Inhibits all six G810 mutants and V804M gatekeeper with IC50 <50 nmol/L; oral bioavailability confirmed ([PMID: 37070927](https://pubmed.ncbi.nlm.nih.gov/37070927/)) | Preclinical |
| **CQ1373** | Pyrazolo derivative; potent cellular activity against G810C/R ([PMID: 39879936](https://pubmed.ncbi.nlm.nih.gov/39879936/)) | Preclinical |
| **LOXO-260** | Next-gen selective RET inhibitor | Clinical trials |

### Combination Strategies Under Investigation
- **RET + SRC inhibition**: Dasatinib "significantly enhanced the efficacy of RET TKIs in RET fusion-positive cancer cells" ([PMID: 41194587](https://pubmed.ncbi.nlm.nih.gov/41194587/))
- **RET + MET inhibition**: For MET-amplification bypass resistance
- **RET + AXL/IGF-1R inhibition**: For specific bypass mechanisms ([PMID: 38768929](https://pubmed.ncbi.nlm.nih.gov/38768929/))
- **Mitochondrial targeting**: Mitochondrial electron transfer chain inhibitors for resistant tumors with mitochondrial dysfunction ([PMID: 38768929](https://pubmed.ncbi.nlm.nih.gov/38768929/))

### Perioperative Therapy
- **LIBRETTO-432** (ongoing): Adjuvant selpercatinib for resectable RET-fusion NSCLC ([PMID: 38372058](https://pubmed.ncbi.nlm.nih.gov/38372058/))
- "Traditional chemoimmunotherapy appears less effective in several of these genotypes due to immune-cold tumor microenvironment" ([PMID: 41816478](https://pubmed.ncbi.nlm.nih.gov/41816478/))
- RET fusions found in ~1.7% of resectable early-stage lung adenocarcinoma ([PMID: 40209611](https://pubmed.ncbi.nlm.nih.gov/40209611/))

### Treatment Algorithm

```
All newly diagnosed advanced NSCLC → Comprehensive NGS
    ↓
RET fusion detected → First-line selpercatinib (preferred)
    ↓
Progression → Determine resistance mechanism (biopsy + ctDNA)
    ├── G810 mutation → Next-gen RET inhibitor (clinical trial)
    ├── MET amplification → RET + MET inhibitor combination
    ├── Other bypass → Pathway-specific combination
    └── No targetable mechanism → Chemotherapy ± clinical trial
```

### Surgical Interventions
- Lobectomy with lymph node dissection for early-stage (I-II) disease (MAXO:0000004)
- Stereotactic radiosurgery for brain metastases
- Palliative radiation for symptomatic metastases

---

## 13. Prevention

### Primary Prevention
- No specific primary prevention for RET-rearranged NSCLC exists
- General measures: Tobacco avoidance, radon mitigation, air pollution reduction
- Most RET-fusion patients are never-smokers, limiting applicability of smoking cessation (MAXO:0000527)

### Secondary Prevention (Early Detection)
- LDCT screening: Current criteria target high-risk smokers; many RET-fusion patients fall outside screening guidelines
- **Comprehensive molecular testing at diagnosis** is the most impactful intervention — ensuring all NSCLC patients receive upfront profiling including RET fusion assessment

### Tertiary Prevention
- Surveillance imaging during and after RET inhibitor therapy
- Serial ctDNA monitoring for early resistance detection
- Brain MRI surveillance given CNS metastasis propensity
- First-line use of selective RET inhibitors maximizes response; delaying targeted therapy reduces efficacy ([PMID: 39926433](https://pubmed.ncbi.nlm.nih.gov/39926433/))

### Genetic Counseling
- Not routinely indicated for RET-rearranged NSCLC (somatic event)
- Distinction from germline RET mutations (MEN2) should be made in appropriate clinical scenarios

---

## 14. Other Species / Natural Disease

### RET Orthologues

| Species | NCBI Taxon | Gene | NCBI Gene ID |
|---|---|---|---|
| *Homo sapiens* | 9606 | RET | 5979 |
| *Mus musculus* | 10090 | Ret | 19713 |
| *Rattus norvegicus* | 10116 | Ret | 24716 |
| *Danio rerio* | 7955 | ret | 30511 |
| *Canis lupus familiaris* | 9615 | RET | 484504 |

### Natural Disease in Animals

RET is highly conserved across vertebrates. Key findings from knockout studies:

- GFRα1-deficient mice demonstrate "absence of enteric neurons and agenesis of the kidney, characteristics that are reminiscent of both GDNF- and Ret-deficient mice" ([PMID: 9728913](https://pubmed.ncbi.nlm.nih.gov/9728913/))
- GDNF signals through RET, which "is essential for development of the enteric nervous system and kidney" ([PMID: 8657282](https://pubmed.ncbi.nlm.nih.gov/8657282/))
- Spontaneous RET-fusion driven lung cancer is not documented as a naturally occurring disease in veterinary species

### Comparative Biology
- RET kinase domain structure is conserved across vertebrates, enabling cross-species pharmacological studies
- Conservation of GDNF-GFRα-RET signaling axis across mammals supports translational relevance of mouse models

---

## 15. Model Organisms

### Mouse Models

| Model | Description | Phenotype Recapitulation |
|---|---|---|
| **Ret knockout** | Ret−/− mice | Renal agenesis, absent enteric neurons (lethal) ([PMID: 8657282](https://pubmed.ncbi.nlm.nih.gov/8657282/)) |
| **GFRα1 knockout** | GFRα1−/− mice | Absent enteric neurons, kidney agenesis ([PMID: 9728913](https://pubmed.ncbi.nlm.nih.gov/9728913/)) |
| **KIF5B-RET transgenic** | Lung-specific inducible expression | Lung adenocarcinoma; used for TKI evaluation |
| **CDX xenograft (KIF5B-RET G810C)** | Cell-derived xenograft | Selpercatinib-resistant tumors; validates next-gen inhibitors ([PMID: 37070927](https://pubmed.ncbi.nlm.nih.gov/37070927/)) |
| **Patient-derived xenografts** | Various RET fusions | Resistance mechanism studies ([PMID: 31988000](https://pubmed.ncbi.nlm.nih.gov/31988000/)) |

### Cell Line Models

| Cell Line | Fusion | Applications |
|---|---|---|
| **LC-2/ad** (Cellosaurus: CVCL_1371) | CCDC6-RET | Drug sensitivity; vandetanib-resistant clones for resistance studies ([PMID: 38768929](https://pubmed.ncbi.nlm.nih.gov/38768929/)) |
| **Ba/F3** (engineered) | Various RET fusions/mutants | Kinase activity profiling; G810 mutant IC50 determination |
| **TPC-1** | CCDC6-RET | Thyroid cancer RET model; cross-tumor type studies |

### Model Limitations
- Mouse models incompletely recapitulate human tumor microenvironment
- Ba/F3 models lack tissue context complexity
- No spontaneous RET-fusion lung cancer models exist in animals
- Cell line resistance models may not capture full clinical resistance spectrum

---

## Key Findings — Expanded Evidence

### Finding 1: RET Fusions Define a Rare but Therapeutically Targetable NSCLC Subtype

RET gene rearrangements occur in approximately 1–2% of NSCLC, defining a distinct molecular subtype with unique clinicopathological features. A pan-tumor RNA sequencing survey established that "KIF5B (46.8%) was the most common fusion partner followed by CCDC6 (28.3%) and NCOA4 (13.8%) in RET+ solid tumors" ([PMID: 37516008](https://pubmed.ncbi.nlm.nih.gov/37516008/)). These fusions are mutually exclusive with other oncogenic drivers and represent a paradigm for precision oncology. The large multicenter cohort of 268 patients confirmed the characteristic clinical profile: "The median age at diagnosis was 58 years; most patients were female (57.0%) and never/light smokers (60.8%)" ([PMID: 41707338](https://pubmed.ncbi.nlm.nih.gov/41707338/)).

### Finding 2: Selpercatinib Is Superior to Standard of Care as First-Line Treatment

The LIBRETTO-431 phase 3 randomized trial established selpercatinib as the preferred first-line treatment for RET-fusion NSCLC. The study demonstrated "median progression-free survival was 24.8 months (95% confidence interval [CI], 16.9 to not estimable) with selpercatinib and 11.2 months (95% CI, 8.8 to 16.8) with control treatment (hazard ratio for progression or death, 0.46; 95% CI, 0.31 to 0.70; P<0.001)" ([PMID: 37870973](https://pubmed.ncbi.nlm.nih.gov/37870973/)). This represents a more than doubling of PFS, with a 54% reduction in the risk of progression or death. The benefit was consistent in the East Asian subgroup (HR 0.38) ([PMID: 40980186](https://pubmed.ncbi.nlm.nih.gov/40980186/)).

### Finding 3: RET G810 Solvent Front Mutations Are the Primary On-Target Resistance Mechanism

ctDNA analysis "revealed emergence of RET G810R, G810S, and G810C mutations in the RET solvent front before the emergence of clinical resistance" ([PMID: 31988000](https://pubmed.ncbi.nlm.nih.gov/31988000/)), with convergent evolution on the G810 residue across multiple metastatic sites. Off-target bypass mechanisms complement on-target resistance: "Three resistant cases (15%) harbored acquired MET amplification without concurrent RET resistance mutations, and one specimen had acquired KRAS amplification" ([PMID: 33007380](https://pubmed.ncbi.nlm.nih.gov/33007380/)). Additional bypass pathways include AXL activation, IGF-1R activation, and SMARCA4 loss ([PMID: 38768929](https://pubmed.ncbi.nlm.nih.gov/38768929/)).

### Finding 4: The Immune-Cold Phenotype Explains Immunotherapy Futility

RET-fusion NSCLC harbors a characteristically immune-cold microenvironment. Multi-omics analysis confirmed "EGFR and ALK/RET/ROS1 fusions... all linked to immune-cold phenotypes with low tumor mutational burden (TMB) and poor T-cell infiltration" ([PMID: 41424613](https://pubmed.ncbi.nlm.nih.gov/41424613/)). Genomic profiling showed "RET rearrangements were associated with lower TMB and PD-L1+/TMB-H proportions" ([PMID: 33655698](https://pubmed.ncbi.nlm.nih.gov/33655698/)). This directly translates to clinical outcomes: immunotherapy provides no OS benefit over no treatment ([PMID: 35838839](https://pubmed.ncbi.nlm.nih.gov/35838839/)).

### Finding 5: Next-Generation RET Inhibitors Address the Resistance Challenge

Vepafestinib demonstrates "best-in-class selectivity against RET, while exerting activity against commonly reported on-target resistance mutations" with high CNS penetration ([PMID: 37743366](https://pubmed.ncbi.nlm.nih.gov/37743366/)). Preclinical studies of alkynyl nicotinamide-based compounds show that "six of these compounds inhibited all six G810 solvent-front mutants and the V804M gatekeeper mutant with IC50 < 50 nmol/L in cell culture" ([PMID: 37070927](https://pubmed.ncbi.nlm.nih.gov/37070927/)). Novel agents APS03118 ([PMID: 40920215](https://pubmed.ncbi.nlm.nih.gov/40920215/)) and CQ1373 ([PMID: 39879936](https://pubmed.ncbi.nlm.nih.gov/39879936/)) provide additional pipeline options.

---

## Mechanistic Model / Interpretation

### Integrated Pathophysiology

The biology of RET-rearranged NSCLC follows a coherent mechanistic chain:

1. **Initiation**: A somatic chromosomal rearrangement (usually pericentric inversion of chr10) creates a fusion gene encoding the RET kinase domain linked to a partner gene's coiled-coil/dimerization domain
2. **Constitutive activation**: The partner domain forces ligand-independent RET dimerization and autophosphorylation, while the partner promoter drives high-level, ubiquitous expression
3. **Oncogenic signaling**: Constitutive activation of RAS-MAPK, PI3K-AKT-mTOR, PLCγ, and JAK-STAT3 cascades promotes proliferation, survival, and invasion
4. **Immune evasion**: Low neoantigen burden (low TMB) and RET-driven cytokine/chemokine signaling create an immune-cold microenvironment resistant to checkpoint immunotherapy
5. **Clinical disease**: Progressive lung adenocarcinoma with predilection for bone, pleural, and brain metastases
6. **Treatment response**: Selective RET inhibitors achieve high ORR (67-84%) by blocking the oncogenic kinase
7. **Resistance**: On-target G810 mutations create steric clashes in the ATP-binding pocket; off-target bypass pathways provide alternative growth signals
8. **Next-generation therapy**: Drugs designed around the G810 steric constraints (vepafestinib, APS03118, HSN608) and combination strategies targeting bypass pathways (MET, SRC, AXL inhibitors)

This model explains both the exceptional therapeutic responses to targeted therapy (oncogene addiction) and the predictable emergence of resistance (evolutionary selection under drug pressure).

---

## Evidence Base

### Landmark Clinical Trials

| Trial | Phase | Key Results | PMID |
|---|---|---|---|
| **LIBRETTO-431** | 3 | Selpercatinib 1L: PFS 24.8 vs 11.2 mo (HR 0.46, P<0.001) | [37870973](https://pubmed.ncbi.nlm.nih.gov/37870973/) |
| **LIBRETTO-001** | 1/2 | Selpercatinib: ORR 84% (1L), 61% (2L+); iORR 85% | [32846060](https://pubmed.ncbi.nlm.nih.gov/32846060/), [36122315](https://pubmed.ncbi.nlm.nih.gov/36122315/) |
| **LIBRETTO-321** | 2 | Selpercatinib in Chinese: durable responses | [39759832](https://pubmed.ncbi.nlm.nih.gov/39759832/) |
| **ARROW** | 1/2 | Pralsetinib: ORR 72% (1L), 59% (2L+); iRR 70% | [35973665](https://pubmed.ncbi.nlm.nih.gov/35973665/) |
| **LIBRETTO-432** | 3 | Adjuvant selpercatinib (ongoing) | [38372058](https://pubmed.ncbi.nlm.nih.gov/38372058/) |

### Key Mechanistic Studies

| Study Focus | Key Finding | PMID |
|---|---|---|
| Discovery of KIF5B-RET | First identification via WGS in 2012 | [22194472](https://pubmed.ncbi.nlm.nih.gov/22194472/) |
| RET solvent front resistance | G810R/S/C emergence on ctDNA before clinical progression | [31988000](https://pubmed.ncbi.nlm.nih.gov/31988000/) |
| Off-target resistance | MET amp (15%), KRAS amp as bypass mechanisms | [33007380](https://pubmed.ncbi.nlm.nih.gov/33007380/) |
| Immune-cold phenotype | Low TMB, poor T-cell infiltration in fusion-driven NSCLC | [41424613](https://pubmed.ncbi.nlm.nih.gov/41424613/) |
| Vepafestinib | Best-in-class selectivity with G810 activity | [37743366](https://pubmed.ncbi.nlm.nih.gov/37743366/) |
| RET biology | Essential for kidney and enteric nervous system development | [24022366](https://pubmed.ncbi.nlm.nih.gov/24022366/) |
| Novel resistance pathways | AXL, IGF-1R, SMARCA4, mitochondrial dysfunction | [38768929](https://pubmed.ncbi.nlm.nih.gov/38768929/) |

### Real-World Evidence

| Study | Key Finding | PMID |
|---|---|---|
| Selective RET TKI vs no targeted therapy | OS 34.3 vs 17.5 months (p=0.002) | [35838839](https://pubmed.ncbi.nlm.nih.gov/35838839/) |
| Chinese real-world RET-TKI | 1L ORR 73.1%, mPFS 22.7 months | [39563271](https://pubmed.ncbi.nlm.nih.gov/39563271/) |
| Latin American cohort | Consistent molecular features; limited RET-TKI access | [41005103](https://pubmed.ncbi.nlm.nih.gov/41005103/) |
| Real-world pralsetinib | Prior treatment reduces efficacy | [39926433](https://pubmed.ncbi.nlm.nih.gov/39926433/) |

---

## Limitations and Knowledge Gaps

1. **Limited mature OS data from phase 3 trials**: LIBRETTO-431 demonstrated PFS superiority, but mature overall survival data are still awaited. Current OS estimates rely on real-world studies and indirect comparisons.

2. **Incomplete resistance landscape**: G810 solvent front mutations and select bypass mechanisms are characterized, but non-genetic resistance mechanisms (epigenetic, transcriptomic adaptation) remain poorly understood.

3. **Lack of perioperative trial results**: LIBRETTO-432 (adjuvant selpercatinib) is ongoing. Optimal perioperative strategy for early-stage RET-fusion NSCLC is undefined.

4. **Limited fusion partner biology understanding**: The biological and clinical significance of rare fusion partners and their differential impact on drug response is poorly characterized.

5. **Epidemiological data gaps**: Prevalence estimates are based largely on East Asian and Western cohorts. Data from Africa, South America (except emerging Latin American data), and other regions are sparse.

6. **Cost-effectiveness concerns**: Selective RET inhibitors may not be cost-effective at current pricing relative to chemotherapy at US WTP thresholds ([PMID: 37854153](https://pubmed.ncbi.nlm.nih.gov/37854153/)).

7. **No validated predictive biomarkers beyond fusion status**: It is unclear whether specific fusion partners, co-mutations, or baseline ctDNA levels predict differential response to specific RET inhibitors.

8. **Limited single-cell and spatial transcriptomics data** specific to RET-fusion NSCLC; most studies combine rare driver mutations together.

9. **Screening gap**: Most RET-fusion patients are never-smokers who fall outside current LDCT screening criteria, representing an unmet detection need.

---

## Proposed Follow-up Experiments/Actions

### Near-term (Clinical)
1. **Analyze mature OS data from LIBRETTO-431** to confirm PFS advantage translates to overall survival benefit
2. **Monitor LIBRETTO-432 results** to define the role of adjuvant selpercatinib in resectable disease
3. **Implement serial ctDNA monitoring protocols** for early resistance detection and treatment switching
4. **Expand next-generation RET inhibitor trials** (vepafestinib, LOXO-260, APS03118) for post-progression settings

### Medium-term (Translational)
5. **Conduct single-cell RNA-seq profiling** of treatment-naïve and resistant RET-fusion tumors to characterize TME evolution
6. **Clinical trials of combination strategies** targeting bypass resistance (RET + MET, RET + SRC)
7. **Develop predictive biomarkers** for treatment selection between available RET inhibitors based on co-mutation profiles and fusion partner type
8. **Study rare fusion partner biology** through functional genomics (CRISPR screens, Ba/F3 models)

### Long-term (Research)
9. **Develop genetically engineered mouse models** with lung-specific inducible KIF5B-RET expression for immunology and combination studies
10. **Investigate epigenetic mechanisms** underlying immune-cold phenotype to identify immunotherapy sensitization strategies
11. **Build a comprehensive RET-fusion NSCLC biobank** with longitudinal tissue and ctDNA for multi-omics resistance profiling
12. **Assess expanded screening criteria** to capture never-smoker NSCLC populations harboring targetable fusions

---

## Consolidated Ontology Terms

### MONDO
| Term ID | Term Name |
|---|---|
| MONDO:0005233 | Non-small cell lung carcinoma |

### HPO (Human Phenotype Ontology)
| Term ID | Term Name |
|---|---|
| HP:0012735 | Cough |
| HP:0002094 | Dyspnea |
| HP:0002105 | Hemoptysis |
| HP:0100749 | Chest pain |
| HP:0001824 | Weight loss |
| HP:0012378 | Fatigue |
| HP:0002653 | Bone pain |
| HP:0002315 | Headache |
| HP:0002202 | Pleural effusion |

### GO (Gene Ontology)
| Term ID | Term Name | Category |
|---|---|---|
| GO:0006468 | Protein phosphorylation | Biological process |
| GO:0007169 | RTK signaling pathway | Biological process |
| GO:0008283 | Cell population proliferation | Biological process |
| GO:0006915 | Apoptotic process | Biological process |
| GO:0001525 | Angiogenesis | Biological process |
| GO:0001837 | EMT | Biological process |
| GO:0005886 | Plasma membrane | Cellular component |
| GO:0005737 | Cytoplasm | Cellular component |
| GO:0005634 | Nucleus | Cellular component |
| GO:0005739 | Mitochondrion | Cellular component |

### CL (Cell Ontology)
| Term ID | Term Name |
|---|---|
| CL:0002063 | Type II pneumocyte |
| CL:0002328 | Bronchial epithelial cell |
| CL:0000625 | CD8-positive T cell |
| CL:0000235 | Macrophage |

### UBERON (Anatomy)
| Term ID | Term Name |
|---|---|
| UBERON:0002048 | Lung |
| UBERON:0002481 | Bone tissue |
| UBERON:0000977 | Pleura |
| UBERON:0000955 | Brain |
| UBERON:0002107 | Liver |
| UBERON:0001004 | Respiratory system |

### MAXO (Medical Action)
| Term ID | Term Name |
|---|---|
| MAXO:0001001 | Targeted therapy |
| MAXO:0000930 | Chemotherapy |
| MAXO:0001344 | Immunotherapy |
| MAXO:0000004 | Surgical procedure |
| MAXO:0000527 | Smoking cessation counseling |

### Key Database Identifiers

| Resource | Identifier | Description |
|---|---|---|
| OMIM | 164761 | RET proto-oncogene |
| HGNC | HGNC:9967 | RET gene symbol |
| NCBI Gene | 5979 | RET gene |
| UniProt | P07949 | RET_HUMAN protein |
| PDB | 7JU6 | RET + selpercatinib co-crystal |
| PDB | 7JU5 | RET + pralsetinib co-crystal |
| ChEMBL | CHEMBL4559134 | Selpercatinib |
| Cellosaurus | CVCL_1371 | LC-2/ad cell line |
| ICD-10 | C34 | Malignant neoplasm of bronchus and lung |
| MeSH | D002289 | Carcinoma, Non-Small-Cell Lung |

---

*Comprehensive disease profile compiled from systematic analysis of 96 peer-reviewed publications across 5 research iterations. All citations verified against original abstracts. Report prepared May 2026.*
