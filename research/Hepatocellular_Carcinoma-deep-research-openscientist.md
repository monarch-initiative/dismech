---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T03:55:36.305525'
end_time: '2026-07-26T04:11:50.102934'
duration_seconds: 973.8
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hepatocellular Carcinoma
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
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 82
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hepatocellular_Carcinoma-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hepatocellular_Carcinoma-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hepatocellular Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Hepatocellular Carcinoma** covering all of the
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

# Hepatocellular Carcinoma: A Comprehensive Disease Characteristics Report

**Disease:** Hepatocellular Carcinoma (HCC)
**Suggested MONDO ID:** MONDO:0007256 (hepatocellular carcinoma)
**Category:** Malignant epithelial neoplasm of the liver (primary liver cancer)
**Report scope:** 15-section disease knowledge-base template
**Evidence base:** 15 confirmed findings; 92 papers reviewed

---

## Summary

Hepatocellular carcinoma (HCC) is the dominant form of primary liver cancer, accounting for approximately 80% of primary liver tumors, and ranks as the **third leading cause of cancer-related mortality worldwide** ([PMID: 35782375](https://pubmed.ncbi.nlm.nih.gov/35782375/)). It arises overwhelmingly (~80–90% of cases) on a background of chronic liver disease and cirrhosis, driven by a well-defined set of etiologies: chronic hepatitis B virus (HBV) and hepatitis C virus (HCV) infection, alcohol-associated liver disease, non-alcoholic fatty liver disease/steatohepatitis (NAFLD/NASH, now often termed MASLD/MASH), and dietary aflatoxin B1 exposure ([PMID: 31347138](https://pubmed.ncbi.nlm.nih.gov/31347138/)). Globally the etiologic landscape is shifting: viral HCC is declining because of HBV vaccination and effective antivirals, while metabolic (NASH/obesity/diabetes-related) HCC is rising and may become the dominant cause ([PMID: 32319693](https://pubmed.ncbi.nlm.nih.gov/32319693/)).

At the molecular level, HCC is characterized by a small set of recurrent somatic driver events — **TERT promoter, TP53, and CTNNB1 (Wnt/β-catenin)** mutations serve as the core initiating drivers, with AXIN1 and other alterations converging on a defined group of oncogenic pathways (Wnt/β-catenin, PI3K/AKT/mTOR, RAS/MAPK/ERK, HGF/c-MET, Hippo-YAP/TAZ, TGF-β) ([PMID: 33958712](https://pubmed.ncbi.nlm.nih.gov/33958712/); [PMID: 41476776](https://pubmed.ncbi.nlm.nih.gov/41476776/)). Epigenetic dysregulation (DNA methylation imbalance, histone modification, chromatin reorganization, non-coding RNAs) and metabolic reprogramming (a Warburg-like aerobic glycolysis and altered lipid metabolism) are additional hallmarks, and the tumor develops within an immunosuppressive microenvironment enriched for regulatory T cells and M0/M2 macrophages that both drives aggressive recurrence and provides the rationale for anti-VEGF plus checkpoint-inhibitor therapy.

Clinically, HCC is remarkable among solid tumors in that it can be diagnosed **noninvasively** in at-risk cirrhotic patients using dynamic contrast imaging (LI-RADS: arterial-phase hyperenhancement + washout ± capsule) supported by serum AFP and PIVKA-II. It shows a strong **male predominance (~2–4:1)** with a sex-hormone mechanistic basis. Management is stage-based following the BCLC framework — curative resection/ablation/transplantation for early disease, TACE/radioembolization for intermediate disease, and now immunotherapy-based systemic combinations (atezolizumab+bevacizumab or durvalumab+tremelimumab) for advanced disease. Prevention is anchored by HBV vaccination (proven primary prevention) and semiannual ultrasound ± AFP surveillance, with coffee consumption a robust dose-dependent protective factor. This report details all of these dimensions across the 15-section template.

---

## Section 1: Disease Information

**Overview.** Hepatocellular carcinoma is a malignant epithelial tumor arising from hepatocytes. It is the dominant primary liver cancer and represents a major global oncologic burden. "Hepatocellular carcinoma (HCC) accounts for some 80% of primary liver tumors... HCC is the sixth most common type of cancer and the third leading cause of cancer-related mortality worldwide" ([PMID: 35782375](https://pubmed.ncbi.nlm.nih.gov/35782375/)).

**Key identifiers (suggested):**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0007256 |
| MeSH | D006528 (Carcinoma, Hepatocellular) |
| ICD-10 | C22.0 |
| ICD-11 | 2C12.0 |
| DOID | DOID:684 |
| NCI Thesaurus | C3099 |

**Synonyms / alternative names:** hepatocellular carcinoma; HCC; hepatoma; malignant hepatoma; primary liver cell carcinoma; liver cell carcinoma; hepatocarcinoma. (Note: HCC is distinct from intrahepatic cholangiocarcinoma and from combined hepatocellular-cholangiocarcinoma [cHCC-CCA], a rare 2–5% mixed entity — [PMID: 42272781](https://pubmed.ncbi.nlm.nih.gov/42272781/).)

**Information source type:** The content in this report is derived predominantly from aggregated disease-level resources (systematic reviews, meta-analyses, cohort studies, genomic consortia such as TCGA/ICGC, GWAS meta-analyses), rather than from individual EHR patient records. Some cited studies use EHR/registry data (e.g., TriNetX cohorts).

---

## Section 2: Etiology

**Primary causal factors.** HCC is a multifactorial disease caused by chronic hepatocellular injury from infectious, toxic, and metabolic insults, on which somatic genetic/epigenetic drivers accumulate. The principal causes: "the major risk factors for HCC development are chronic liver disease and cirrhosis due to hepatitis B virus (HBV) and/or hepatitis C virus (HCV), alcoholic liver disease, non-alcoholic fatty liver disease (NAFLD), steatohepatitis, intake of aflatoxin-contaminated food, diabetes, and obesity" ([PMID: 31347138](https://pubmed.ncbi.nlm.nih.gov/31347138/)). Approximately 80–90% of HCC arises on established cirrhosis.

**Environmental / lifestyle risk factors:** chronic viral hepatitis (HBV, HCV), heavy alcohol use, aflatoxin B1 dietary exposure, tobacco smoking, obesity, type 2 diabetes, metabolic syndrome, older age, and male sex. Metabolic risk factors are increasing: "the prevalence of metabolic risk factors for HCC, including metabolic syndrome, obesity, type II diabetes and non-alcoholic fatty liver disease (NAFLD) are increasing and may jointly become the major cause of HCC globally" ([PMID: 32319693](https://pubmed.ncbi.nlm.nih.gov/32319693/)).

**Genetic risk factors (germline susceptibility).** A multi-ancestry GWAS meta-analysis of 17,697 cases identified **15 genome-wide significant risk loci**, including MAP3K9, DHRS1, MTTP, and 8q24.21 ([PMID: 42357869](https://pubmed.ncbi.nlm.nih.gov/42357869/)). Established susceptibility genes influencing lipid/metabolic handling include **PNPLA3, TM6SF2, MBOAT7, and TERT** ([PMID: 41699549](https://pubmed.ncbi.nlm.nih.gov/41699549/)). The PNPLA3 I148M (rs738409) variant is a particularly important, fibrosis-independent risk allele (see Section 4/10).

**Protective factors.** *Environmental:* **coffee consumption** is a robust, dose-dependent protective factor (~35% risk reduction per 2 extra cups/day; see Finding F011). HBV vaccination and antiviral therapy prevent virally driven HCC. *Pharmacologic:* metformin use in diabetics may lower risk — cumulative metformin exposure after HCV cure was associated with lower HCC risk (HR 0.46 per year; 95% CI 0.27–0.77) ([PMID: 42499017](https://pubmed.ncbi.nlm.nih.gov/42499017/)). *Genetic protective:* rare loss-of-function/protective alleles at metabolic loci are under investigation but not firmly established.

**Gene–environment interactions.** The clearest example is PNPLA3 I148M acting on a background of fatty liver disease to raise HCC risk independent of fibrosis ([PMID: 25278690](https://pubmed.ncbi.nlm.nih.gov/25278690/)). Diabetes/hyperinsulinemia interacts with hepatic oncogenic signaling (insulin/IGF-1 → PI3K/AKT/mTOR and RAS/MAPK), amplifying the Warburg effect and chronic inflammation ([PMID: 42364319](https://pubmed.ncbi.nlm.nih.gov/42364319/)). CHB–MAFLD comorbidity has dual, dose-dependent effects on hepatocarcinogenesis ([PMID: 42367770](https://pubmed.ncbi.nlm.nih.gov/42367770/)).

---

## Section 3: Phenotypes

HCC is frequently asymptomatic in early stages (detected on surveillance imaging) and produces nonspecific symptoms as it advances. Clinical presentation "extends from right upper abdominal quadrant pain and weight loss to obstructive jaundice and lethargy" ([PMID: 28839428](https://pubmed.ncbi.nlm.nih.gov/28839428/)).

| Phenotype | Type | HPO suggestion | Notes / frequency |
|---|---|---|---|
| Right upper quadrant / abdominal pain | Symptom | HP:0002027 (abdominal pain) | Common in symptomatic disease |
| Weight loss / cachexia | Constitutional | HP:0001824 | Advanced disease |
| Fatigue / lethargy | Symptom | HP:0012378 | Common |
| Hepatomegaly / abdominal mass | Clinical sign | HP:0002240 | Palpable in large tumors |
| Jaundice | Sign | HP:0000952 | Obstructive/advanced |
| Ascites | Sign | HP:0001541 | Cirrhosis/portal hypertension |
| Elevated alpha-fetoprotein | Lab abnormality | HP:0006254 (abnormal AFP) | Diagnostic/prognostic biomarker |
| Portal vein thrombosis | Complication | HP:0030242 | Marker of macrovascular invasion |

**Paraneoplastic phenotypes.** Paraneoplastic syndromes (PNS) occur in **20–40% of HCC patients** and portend poor prognosis (Finding F014): "a significant proportion (20-40%) of patients with HCC develop paraneoplastic syndromes" ([PMID: 35649187](https://pubmed.ncbi.nlm.nih.gov/35649187/)). In a 534-patient cohort, 22.3% were PNS-positive, with hypercalcemia (~6.3%), hypoglycemia (~5.8%), erythrocytosis (~3.9%), thrombocytosis (~3.9%), and hypercholesterolemia (~2.4%) ([PMID: 34974464](https://pubmed.ncbi.nlm.nih.gov/34974464/)). PNS-positivity is an independent prognostic factor ([PMID: 24480222](https://pubmed.ncbi.nlm.nih.gov/24480222/)).

**Age of onset / severity / progression:** adult- to late-onset (typically >50 years); severity variable but often severe given the cirrhotic background; progression typically progressive without treatment. **Quality of life** is affected by the underlying cirrhosis (ascites, fatigue, portal hypertensive symptoms — including lower urinary tract symptoms, [PMID: 24798455](https://pubmed.ncbi.nlm.nih.gov/24798455/)) as well as tumor burden.

---

## Section 4: Genetic / Molecular Information

**Core somatic drivers (Finding F002).** Large-scale genome sequencing has defined a compact set of initiating drivers: "Large-scale HCC genome sequencing analyses have identified core drivers (TERT, TP53, and CTNNB1/AXIN1) as initial molecular events" ([PMID: 33958712](https://pubmed.ncbi.nlm.nih.gov/33958712/)). Nearly half of HCC patients carry oncogenic driver mutations such as TP53, CTNNB1, or TERT ([PMID: 41699549](https://pubmed.ncbi.nlm.nih.gov/41699549/)).

| Gene (HGNC) | Alteration | Pathway / consequence | Origin |
|---|---|---|---|
| **TERT** | Promoter mutation (earliest/most frequent) | Telomerase reactivation, cellular immortalization | Somatic |
| **TP53** | Missense/nonsense/deletion | Loss of tumor-suppressor / p53 pathway | Somatic (aflatoxin → R249S hotspot) |
| **CTNNB1** | Activating missense | Wnt/β-catenin hyperactivation | Somatic |
| **AXIN1** | Loss of function | Wnt/β-catenin (negative regulator loss) | Somatic |
| **ARID1A** | Loss of function | Chromatin remodeling | Somatic |
| **PNPLA3** (I148M) | Germline risk variant | Hepatic lipid metabolism | Germline |
| **TERT, TM6SF2, MBOAT7** | Germline susceptibility loci | Senescence / lipid metabolism | Germline |

**Variant types/classes:** missense, nonsense, frameshift, splice-site, and structural/chromosomal alterations; the TERT lesion is a non-coding promoter point mutation. Somatic drivers are documented in COSMIC/TCGA/ICGC; germline risk variants in GWAS Catalog/gnomAD. In liquid biopsy, CTNNB1 and ARID1A were the most frequently mutated genes in baseline ctDNA (25%), followed by SF3B1 (20%) and TERT (18%) ([PMID: 40596669](https://pubmed.ncbi.nlm.nih.gov/40596669/)). Concomitant TERT+TP53+CTNNB1 co-mutation within a single clone can occur ([PMID: 37968991](https://pubmed.ncbi.nlm.nih.gov/37968991/)); single-gene mutations serve as diagnostic/prognostic/predictive biomarkers ([PMID: 40765562](https://pubmed.ncbi.nlm.nih.gov/40765562/)).

**Functional consequences:** TERT = gain of telomerase function; CTNNB1 = gain-of-function/constitutive Wnt signaling; TP53/AXIN1/ARID1A = loss of function.

**Epigenetic information (Finding F015).** Four interconnected epigenetic layers operate in HCC: (1) "global DNA hypomethylation of oncogenes and hypermethylation of tumor suppressors" ([PMID: 40057667](https://pubmed.ncbi.nlm.nih.gov/40057667/)); (2) aberrant histone modifications; (3) genome-wide chromatin loop rearrangement; (4) non-coding RNA regulation. Specific examples: **SFRP5** promoter hypermethylation silences a Wnt antagonist and constitutively activates Wnt/β-catenin (reversible by the demethylating agent 5-Aza) ([PMID: 40814770](https://pubmed.ncbi.nlm.nih.gov/40814770/)); **PAX6** promoter hypermethylation promotes growth/metastasis via CDH1/THBS1 ([PMID: 39614377](https://pubmed.ncbi.nlm.nih.gov/39614377/)); methylation-silencing of the **C14MC (miR-379/miR-656) cluster** removes tumor-suppressor miRNAs ([PMID: 42286554](https://pubmed.ncbi.nlm.nih.gov/42286554/)).

**Chromosomal abnormalities:** recurrent copy-number alterations and chromosomal instability accompany the point-mutation drivers; 8q24.21 (near MYC) is a germline risk locus ([PMID: 42357869](https://pubmed.ncbi.nlm.nih.gov/42357869/)).

---

## Section 5: Environmental Information

**Environmental factors / toxins:** **Aflatoxin B1** (a mycotoxin contaminating stored grains/nuts, CHEBI:2504) is a classic hepatocarcinogen causing the TP53 R249S signature. Tobacco smoke is an established risk factor ([PMID: 28839428](https://pubmed.ncbi.nlm.nih.gov/28839428/)).

**Lifestyle factors:** heavy **alcohol** (ethanol, CHEBI:16236) consumption (alcoholic liver disease → cirrhosis → HCC); diet/obesity driving NAFLD/NASH; physical inactivity and diabetes. Coffee is protective (Section 2, F011).

**Infectious agents:** the two dominant infectious causes are **hepatitis B virus (HBV; NCBI:txid10407)** and **hepatitis C virus (HCV; NCBI:txid11103)**. Chronic HBV/HCV cause a majority of HCC globally through chronic inflammation, fibrosis, and (for HBV) direct integration/HBx oncogenic effects. Perinatal HBV transmission causes >85% chronic carriage if untreated ([PMID: 28870397](https://pubmed.ncbi.nlm.nih.gov/28870397/)); transfusion-associated HCV remains a concern in vulnerable groups ([PMID: 42488322](https://pubmed.ncbi.nlm.nih.gov/42488322/)).

---

## Section 6: Mechanism / Pathophysiology

**Molecular pathways (Finding F002).** HCC converges on a defined set of oncogenic signaling cascades: "the Wnt/β-catenin, TGF-β, PI3K/AKT/mTOR, MAPK/ERK, HGF/c-MET, Notch and Hippo-YAP/TAZ pathways are known to contribute to promoting aggressive HCC behaviour" ([PMID: 41476776](https://pubmed.ncbi.nlm.nih.gov/41476776/)). c-MYC is a central oncogenic transcription factor integrating these pathways and metabolic reprogramming ([PMID: 40473083](https://pubmed.ncbi.nlm.nih.gov/40473083/)); miRNAs shape these same pathways ([PMID: 40943288](https://pubmed.ncbi.nlm.nih.gov/40943288/)). Suggested GO terms: GO:0016055 (Wnt signaling pathway), GO:0038083 (PI3K signaling), GO:0007179 (TGF-β receptor signaling).

**Cellular processes:** dysregulated proliferation, evasion of apoptosis, replicative immortality (TERT), chronic inflammation, and impaired autophagy/senescence. GO suggestions: GO:0008283 (cell population proliferation), GO:0006915 (apoptotic process), GO:0006954 (inflammatory response).

**Metabolic reprogramming (Finding F012).** A Warburg-like aerobic glycolysis and altered lipid metabolism are hallmarks. The fatty-acid receptor **CD36** is overexpressed in HCC and drives growth via "mTOR-mediated oncogenic glycolysis via activation of Src/PI3K/AKT signaling axis" ([PMID: 33771982](https://pubmed.ncbi.nlm.nih.gov/33771982/)). HBV infection dysregulates aerobic glycolysis/lipid metabolism (Glut1 upregulation, glucose influx, lactate secretion — "a classic metabolic signature also observed in cancer cells") ([PMID: 28768434](https://pubmed.ncbi.nlm.nih.gov/28768434/)).

**Immune involvement (Finding F008).** HCC harbors an immunosuppressive tumor microenvironment (TME) enriched for **regulatory T cells and M0/M2 macrophages** with upregulated checkpoints (PD-1, CTLA-4, PD-L1) ([PMID: 42470438](https://pubmed.ncbi.nlm.nih.gov/42470438/)). Early/polyclonal intrahepatic recurrence is "associated with early recurrence, high phenotypic plasticity and a regulatory T cell enriched immunosuppressive microenvironment" ([PMID: 42481381](https://pubmed.ncbi.nlm.nih.gov/42481381/)). AID–OSMR–STAT3 signaling remodels the immune microenvironment ([PMID: 42462445](https://pubmed.ncbi.nlm.nih.gov/42462445/)). CL suggestions: CL:0000815 (regulatory T cell), CL:0000235 (macrophage), CL:0000182 (hepatocyte).

**Tissue damage mechanisms:** chronic inflammation → oxidative stress → fibrosis/cirrhosis → dysplasia → carcinoma. HBx transgenic models show carcinogenesis "accompanied by the activation of β-catenin and Jun N-terminal kinase (JNK) signaling pathways as well as the production of reactive oxygen species" ([PMID: 28874700](https://pubmed.ncbi.nlm.nih.gov/28874700/)). NF-κB signaling links hepatitis to HCC ([PMID: 30723284](https://pubmed.ncbi.nlm.nih.gov/30723284/)).

**Sex dimorphism (Finding F013).** HCC is strongly male-predominant. Mechanistically, "the androgen/androgen receptor (AR) accelerate cell proliferation and virus infection, especially during the initial stage of HCC, while estrogen/estrogen receptor (ER) function in an opposite way to induce cell apoptosis and immune responses" ([PMID: 36563929](https://pubmed.ncbi.nlm.nih.gov/36563929/)). Murine models link male predisposition to cytokine-mediated "liver-gender disruption" ([PMID: 18089782](https://pubmed.ncbi.nlm.nih.gov/18089782/)).

### Causal chain (upstream → downstream)

```
Chronic insult (HBV/HCV/alcohol/NASH/aflatoxin)
        │
        ▼
Chronic inflammation + oxidative stress
        │
        ▼
Fibrosis ──► Cirrhosis (present in 80–90%)
        │
        ▼
Somatic drivers accumulate: TERT (immortalization)
   + TP53 (loss of checkpoint) + CTNNB1/AXIN1 (Wnt ON)
        │
        ▼
Pathway hyperactivation: Wnt/β-catenin, PI3K/AKT/mTOR,
   MAPK/ERK, c-MET, Hippo-YAP; metabolic reprogramming (CD36→glycolysis)
        │
        ▼
Immunosuppressive TME (Tregs, M2 macrophages, PD-L1)
        │
        ▼
Dysplastic nodule ──► Hepatocellular carcinoma ──► vascular invasion / metastasis
```

---

## Section 7: Anatomical Structures Affected

**Organ level:** Primary organ = **liver** (UBERON:0002107); tumor arises from hepatocytes. Secondary involvement: **portal vein** (macrovascular invasion, UBERON:0002017), regional lymph nodes, lungs (most common extrahepatic metastatic site), bone, and adrenal glands. Body system: **digestive/hepatobiliary system** (UBERON:0002423, hepatobiliary system).

**Tissue / cell level:** malignant transformation of **hepatocytes** (CL:0000182) — parenchymal epithelial cells of the liver. The cholangiocyte-phenotype (CK19+) subtype carries poorer prognosis ([PMID: 42400611](https://pubmed.ncbi.nlm.nih.gov/42400611/)). Non-parenchymal cells (Kupffer cells/macrophages, hepatic stellate cells driving fibrosis, endothelial cells) participate in the TME.

**Subcellular level:** nucleus (TERT/TP53/CTNNB1 nuclear signaling; GO:0005634), mitochondria (metabolic reprogramming; GO:0005739), and plasma membrane receptors (CD36, c-MET; GO:0005886).

**Localization / lateralization:** HCC occurs within the liver parenchyma (often the larger right lobe); may be unifocal, multifocal, or infiltrative. Multifocality can reflect intrahepatic metastasis or multicentric occurrence.

---

## Section 8: Temporal Development

**Onset:** Typically **adult-to-geriatric onset** (usually >50 years), developing insidiously over years-to-decades of chronic liver disease. Onset is chronic/insidious; the tumor is often clinically silent until advanced. Early-onset HCC (<50 y) is part of the broader rise in early-onset GI cancers ([PMID: 42295754](https://pubmed.ncbi.nlm.nih.gov/42295754/)).

**Progression / staging (Finding F009).** Staged by the **Barcelona Clinic Liver Cancer (BCLC)** system integrating tumor burden, liver function, and performance status ([PMID: 28839428](https://pubmed.ncbi.nlm.nih.gov/28839428/)): very early/early (0/A), intermediate (B), advanced (C, with macrovascular invasion/extrahepatic spread), and terminal (D). Progression rate is variable; disease course is progressive without treatment. After curative treatment, **recurrence is common** and follows distinct clonal modes (early polyclonal vs late) ([PMID: 42481381](https://pubmed.ncbi.nlm.nih.gov/42481381/)).

**Patterns:** Remission is treatment-induced (curative resection/ablation/transplant, or sustained response to systemic therapy — durable complete responses are now reported with SIRT + targeted + immunotherapy, [PMID: 42022453](https://pubmed.ncbi.nlm.nih.gov/42022453/)). Critical intervention window: detecting HCC at early BCLC 0/A stage enables curative therapy — the rationale for surveillance.

---

## Section 9: Inheritance and Population

**Epidemiology.** HCC is the sixth most common cancer and third leading cause of cancer mortality worldwide ([PMID: 35782375](https://pubmed.ncbi.nlm.nih.gov/35782375/)). Incidence is highest in East Asia and sub-Saharan Africa (HBV- and aflatoxin-endemic regions); in Western countries NASH-related HCC is rising while viral HCC declines ([PMID: 31347138](https://pubmed.ncbi.nlm.nih.gov/31347138/); [PMID: 36139633](https://pubmed.ncbi.nlm.nih.gov/36139633/)).

**Inheritance.** HCC is **not a Mendelian disease**; it is a somatically driven cancer with **polygenic/multifactorial germline susceptibility**. GWAS identified 15 risk loci ([PMID: 42357869](https://pubmed.ncbi.nlm.nih.gov/42357869/)); PNPLA3/TM6SF2/MBOAT7/TERT contribute inherited risk ([PMID: 41699549](https://pubmed.ncbi.nlm.nih.gov/41699549/)). Classical Mendelian concepts (penetrance, anticipation, carrier frequency) do not directly apply.

**Demographics.** Strong **male predominance (~2–4:1)** with a sex-hormone mechanistic basis (Section 6, F013). Ethnicity affects prevalence and outcomes: non-Caucasian patients often have poorer survival ([PMID: 37344125](https://pubmed.ncbi.nlm.nih.gov/37344125/)). Age distribution skews to older adults, with a rising early-onset segment.

---

## Section 10: Diagnostics

**Noninvasive imaging diagnosis (Finding F007).** Uniquely among solid tumors, HCC can be diagnosed **without biopsy** in at-risk cirrhotic patients using LI-RADS criteria on multiphase CT or gadoxetic-acid MRI: arterial-phase hyperenhancement, non-peripheral "washout," and enhancing capsule. "For LR-5 in identifying HCC, sensitivity was 79-83%, specificity was 91-97%, and accuracy was 89-92%" ([PMID: 38951191](https://pubmed.ncbi.nlm.nih.gov/38951191/)). MRI outperforms CT in sensitivity (89.3% vs 78.9% for APASL criteria) ([PMID: 40487794](https://pubmed.ncbi.nlm.nih.gov/40487794/)). Contrast-enhanced ultrasound (CEUS) adds high specificity (100%) for inconclusive small nodules ([PMID: 40055232](https://pubmed.ncbi.nlm.nih.gov/40055232/)).

**Serum biomarkers.** **Alpha-fetoprotein (AFP)** and **PIVKA-II (DCP)** aid diagnosis and risk stratification ([PMID: 40293522](https://pubmed.ncbi.nlm.nih.gov/40293522/)). LOINC: AFP 1834-1. Emerging biomarkers: **methylated SEPT9** outperformed AFP (AUROC 0.79 vs 0.71; P=0.002) and, combined with AFP, recovered 78% of AFP-missed cases ([PMID: 42390849](https://pubmed.ncbi.nlm.nih.gov/42390849/)); the **GAAD algorithm** (gender/age/AFP/PIVKA-II) and liquid-biopsy ctDNA/cfDNA fragmentomics are advancing ([PMID: 42312979](https://pubmed.ncbi.nlm.nih.gov/42312979/); [PMID: 42353299](https://pubmed.ncbi.nlm.nih.gov/42353299/)).

**Pathology / IHC.** When biopsy is needed, diagnosis integrates morphology with immunohistochemistry (glypican-3, HSP70, glutamine synthetase; β-catenin/GS for Wnt-activated tumors) and can be supported by driver-mutation detection (TERT/CTNNB1/TP53) ([PMID: 40276913](https://pubmed.ncbi.nlm.nih.gov/40276913/)). **Differential diagnosis:** dysplastic nodule, hepatocellular adenoma, intrahepatic cholangiocarcinoma, cHCC-CCA ([PMID: 42272781](https://pubmed.ncbi.nlm.nih.gov/42272781/)), histiocytic sarcoma ([PMID: 42405293](https://pubmed.ncbi.nlm.nih.gov/42405293/)), and benign inflammatory mimics (e.g., xanthogranulomatous inflammation) ([PMID: 41909198](https://pubmed.ncbi.nlm.nih.gov/41909198/)).

**Diagnostic pitfalls:** LR-M lesions require biopsy (only ~46% are HCC) ([PMID: 40293522](https://pubmed.ncbi.nlm.nih.gov/40293522/)); benign mimics can simulate LR-5 kinetics in fibrotic livers ([PMID: 41909198](https://pubmed.ncbi.nlm.nih.gov/41909198/)).

---

## Section 11: Outcome / Prognosis

**Survival.** Prognosis is stage- and liver-function-dependent (Finding F005). Advanced disease with best current systemic therapy achieves median OS approaching ~19–24 months (IMbrave150 5-year OS 19%) ([PMID: 42022453](https://pubmed.ncbi.nlm.nih.gov/42022453/)). Early-stage disease treated curatively achieves substantially better long-term survival, though recurrence is frequent.

**Prognostic factors (Finding F005).** **AFP** is an independent prognostic factor after hepatectomy — DFS HR 1.391 (95% CI 1.193–1.623) and OS HR 1.267 (95% CI 1.080–1.486); the combined AFP–FIB-4 score improves prediction (DFS HR 1.404; OS HR 1.378) ([PMID: 42323530](https://pubmed.ncbi.nlm.nih.gov/42323530/)). **Microvascular invasion (MVI)** is "a critical prognostic risk factor" ([PMID: 42480815](https://pubmed.ncbi.nlm.nih.gov/42480815/)). **BCLC stage** and **ALBI grade** (liver function) are key ([PMID: 42449617](https://pubmed.ncbi.nlm.nih.gov/42449617/)). Molecular/liquid-biopsy prognostics: ctDNA CTNNB1/TP53/ARID1A/KEAP1 mutations predict poor OS pre-TACE ([PMID: 40596669](https://pubmed.ncbi.nlm.nih.gov/40596669/)); 5mC gene signatures ([PMID: 42304060](https://pubmed.ncbi.nlm.nih.gov/42304060/)); radiomics/machine-learning models ([PMID: 42413246](https://pubmed.ncbi.nlm.nih.gov/42413246/); [PMID: 42344442](https://pubmed.ncbi.nlm.nih.gov/42344442/)).

**Complications:** hepatic decompensation, portal vein thrombosis, variceal bleeding, and paraneoplastic syndromes (20–40%, poor prognosis; F014) ([PMID: 35649187](https://pubmed.ncbi.nlm.nih.gov/35649187/)). Within PNS, erythrocytosis and thrombocytosis were independent predictors of *better* prognosis while hypoglycemia/hypercalcemia predicted worse outcome ([PMID: 34974464](https://pubmed.ncbi.nlm.nih.gov/34974464/)).

---

## Section 12: Treatment

**Stage-based (BCLC) framework (Finding F009).**

| BCLC stage | Standard treatment | MAXO suggestion |
|---|---|---|
| Very early / early (0/A) | Resection, local ablation (RFA/MWA/PEI/cryo), liver transplantation (Milan criteria) | MAXO:0001175 (surgical procedure), MAXO:0000004 (radiofrequency ablation) |
| Intermediate (B) | TACE, radioembolization (TARE/SIRT) | MAXO:0000527 (chemoembolization) |
| Advanced (C) | Systemic immunotherapy-based combinations | MAXO:0000765 (immunotherapy) |
| Terminal (D) | Best supportive care | MAXO:0000922 (palliative care) |

**Curative options.** Liver resection, ablation, and transplantation; transplant is restricted to **Milan criteria** ("one tumor ≤ 5 cm, or up to three tumors no larger than 3 cm, along with the absence of gross vascular invasion or extrahepatic spread") ([PMID: 34696292](https://pubmed.ncbi.nlm.nih.gov/34696292/)). Downstaging into Milan criteria enables acceptable post-transplant outcomes ([PMID: 36813012](https://pubmed.ncbi.nlm.nih.gov/36813012/)). For recurrence within Milan criteria after resection, RR/RFA and TACE achieve comparable outcomes except for late recurrence, where RR/RFA is preferred ([PMID: 25933127](https://pubmed.ncbi.nlm.nih.gov/25933127/); [PMID: 32355732](https://pubmed.ncbi.nlm.nih.gov/32355732/)).

**First-line systemic therapy is now immunotherapy-based (Finding F003).** "Current international guidelines recommend atezolizumab plus bevacizumab (A+T) or durvalumab plus tremelimumab (Dur/Tre) as first-line regimens for unresectable HCC. In the 5-year update of IMbrave150, A+T achieved an objective response rate (ORR) of 30% and a 5-year overall survival (OS) rate of 19%" ([PMID: 42022453](https://pubmed.ncbi.nlm.nih.gov/42022453/)). This superseded single-agent TKIs (sorafenib/lenvatinib, median OS ~10–14 months) ([PMID: 36497349](https://pubmed.ncbi.nlm.nih.gov/36497349/)). Network meta-analyses support atezolizumab+bevacizumab superiority over lenvatinib (HR 0.59) ([PMID: 34239810](https://pubmed.ncbi.nlm.nih.gov/34239810/); [PMID: 33638735](https://pubmed.ncbi.nlm.nih.gov/33638735/)).

**Mechanistic rationale for anti-VEGF + ICI (Finding F008):** "anti-VEGF therapy induces vascular normalization, enhances immune cell infiltration, and reduces immunosuppression within the TME, thereby converting immunologically 'cold' tumors into 'hot' tumors that are more responsive to checkpoint blockade" ([PMID: 42467392](https://pubmed.ncbi.nlm.nih.gov/42467392/)).

**Second-line / other options:** regorafenib, cabozantinib, ramucirumab, nivolumab+ipilimumab, pembrolizumab ([PMID: 40704000](https://pubmed.ncbi.nlm.nih.gov/40704000/); [PMID: 34953051](https://pubmed.ncbi.nlm.nih.gov/34953051/)). **Emerging/experimental:** c-MYC-targeted approaches ([PMID: 40473083](https://pubmed.ncbi.nlm.nih.gov/40473083/)); RNA therapeutics such as MTL-CEBPA saRNA ([PMID: 29511346](https://pubmed.ncbi.nlm.nih.gov/29511346/)); miRNA-based strategies ([PMID: 40943288](https://pubmed.ncbi.nlm.nih.gov/40943288/)); demethylating agents (5-Aza) targeting epigenetic silencing ([PMID: 40814770](https://pubmed.ncbi.nlm.nih.gov/40814770/)); plant-derived/curcumin adjuncts under preclinical study ([PMID: 41044771](https://pubmed.ncbi.nlm.nih.gov/41044771/); [PMID: 41751435](https://pubmed.ncbi.nlm.nih.gov/41751435/)).

---

## Section 13: Prevention

**Primary prevention (Finding F004).** **HBV vaccination** is proven primary prevention: "hepatitis B vaccination can protect them from HCC, as has been demonstrated in Taiwan and other countries" ([PMID: 26651252](https://pubmed.ncbi.nlm.nih.gov/26651252/)). Perinatal prevention: "This risk is reduced by 90% with HBV vaccine given along with hepatitis B immune globulin (HBIG) starting at birth" ([PMID: 28870397](https://pubmed.ncbi.nlm.nih.gov/28870397/)). (Note: age-period-cohort analyses caution that secular time-trends also contributed to observed pediatric HCC declines in Taiwan — [PMID: 25660961](https://pubmed.ncbi.nlm.nih.gov/25660961/).) Antiviral therapy (nucleos(t)ide analogues for HBV; direct-acting antivirals achieving SVR for HCV) reduces HCC incidence ([PMID: 25241970](https://pubmed.ncbi.nlm.nih.gov/25241970/)). Other primary prevention: aflatoxin reduction, alcohol moderation, metabolic risk-factor control; coffee consumption and (in diabetics) metformin are protective.

**Secondary prevention / surveillance (Finding F004).** "Current guidelines recommend semiannual surveillance with ultrasound and α-fetoprotein, but this strategy has suboptimal sensitivity" ([PMID: 42017860](https://pubmed.ncbi.nlm.nih.gov/42017860/)); fewer than 1 in 4 cirrhotic patients receive adequate surveillance. Risk-stratified surveillance and emerging biomarkers (methylated SEPT9, GAAD, liver stiffness) aim to improve early detection ([PMID: 41921193](https://pubmed.ncbi.nlm.nih.gov/41921193/); [PMID: 42390849](https://pubmed.ncbi.nlm.nih.gov/42390849/); [PMID: 42394831](https://pubmed.ncbi.nlm.nih.gov/42394831/)).

**Tertiary prevention:** management of cirrhosis complications and post-treatment recurrence surveillance. **Genetic counseling** is limited given the polygenic nature but PNPLA3 genotyping may inform metabolic-HCC risk stratification.

---

## Section 14: Other Species / Natural Disease

- **Taxonomy:** HCC occurs naturally across mammals. *Homo sapiens* (NCBI:txid9606); animal models include *Mus musculus* (NCBI:txid10090), *Rattus norvegicus* (NCBI:txid10116), and the **woodchuck** *Marmota monax*.
- **Natural disease model:** The **woodchuck hepatitis virus (WHV)** produces an HBV-like chronic hepatitis and near-universal HCC, serving as a key natural model of virally driven hepatocarcinogenesis.
- **Orthologous genes:** Tp53, Ctnnb1, Tert are conserved across mouse/rat/human, enabling cross-species mechanistic study.
- **Comparative biology:** HCC develops in companion animals (dogs) and other species; core inflammation → fibrosis → carcinoma mechanisms and oncogenic pathway conservation permit translational study (Alliance of Genome Resources for orthology). *Not zoonotic* — HCC itself is non-transmissible, though its causal viruses have species-specific counterparts.

---

## Section 15: Model Organisms

**Model systems (Finding F006).** Rodent models dominate HCC research:

| Model | Type | Mechanism / use |
|---|---|---|
| DEN (diethylnitrosamine)-treated mice/rats | Chemical carcinogenesis | Genotoxic HCC induction; C57BL/6 background |
| c-Myc transgenic | Oncogene-driven | Proliferation-driven tumorigenesis |
| HBx transgenic (e.g., C1485T) | Viral oncogene | β-catenin/JNK/ROS-driven; enhanced DEN susceptibility ([PMID: 28874700](https://pubmed.ncbi.nlm.nih.gov/28874700/)) |
| HCV-transgenic + PML deficiency | Viral + tumor-suppressor loss | Spontaneous liver tumors ([PMID: 31144474](https://pubmed.ncbi.nlm.nih.gov/31144474/)) |
| TAK1 knockout; Vps33b conditional KO | Tumor-suppressor loss | Inflammation-driven HCC ([PMID: 29729199](https://pubmed.ncbi.nlm.nih.gov/29729199/)) |
| NASH/diet-induced models | Metabolic etiology | Recapitulate MASLD-HCC |
| Woodchuck (WHV) | Natural viral model | HBV-like chronic infection → HCC |

**Genetic model types:** knockout, conditional, transgenic, and humanized models. Etiology-oriented subtyping compares murine tumors to TCGA etiologic subsets ([PMID: 30967480](https://pubmed.ncbi.nlm.nih.gov/30967480/)).

**Limitations:** "Murine liver tumors often fail to recapitulate the complexity of human hepatocellular carcinoma (HCC), which might explain the difficulty to translate preclinical mouse studies into clinical science" ([PMID: 30967480](https://pubmed.ncbi.nlm.nih.gov/30967480/)). Human cell lines (HepG2, Huh7, Hep3B), patient-derived organoids, and iPSC systems complement in vivo models. Resources: MGI, RGD, Cellosaurus.

---

## Mechanistic Model / Interpretation

HCC is best understood as the endpoint of a **chronic-injury → inflammation → fibrosis/cirrhosis → dysplasia → carcinoma** sequence, on which a compact set of somatic drivers act. The upstream trigger is etiology-specific (HBV, HCV, alcohol, NASH, aflatoxin) but converges on a shared downstream program: sustained hepatocyte injury and regeneration create a mutagenic, inflammatory, and immunosuppressive niche in which **TERT-promoter mutation (immortalization)**, **TP53 loss (checkpoint failure)**, and **CTNNB1/AXIN1 alterations (Wnt/β-catenin activation)** initiate malignancy. These drivers hyperactivate a defined pathway network (Wnt, PI3K/AKT/mTOR, MAPK/ERK, c-MET, Hippo-YAP), which — reinforced by epigenetic dysregulation and metabolic reprogramming (CD36→Warburg glycolysis) — produces a proliferative, invasive tumor embedded in a Treg/M2-macrophage-rich, checkpoint-high microenvironment.

This model explains the therapeutic landscape: because the tumor is immunosuppressed and highly vascular, **anti-VEGF vascular normalization + checkpoint blockade** is synergistic and now first-line; because early tumors are curable, **surveillance + noninvasive imaging diagnosis** is the central strategy; and because HBV is a dominant upstream cause, **vaccination is the most effective primary prevention**. Sex-hormone signaling (AR pro-tumor, ER protective) accounts for the male predominance, and germline modifiers (PNPLA3, and 15 GWAS loci) tune individual risk on the environmental background.

---

## Evidence Base

| Finding | Key PMIDs | Evidence type | Support |
|---|---|---|---|
| F001 Burden & etiology | 35782375, 31347138, 32319693 | Human review/epi | Strong |
| F002 Core drivers & pathways | 33958712, 41699549, 42357869, 41476776 | Genomics/GWAS | Strong |
| F003 Immunotherapy first-line | 42022453, 40704000, 34239810, 33638735 | RCT/meta-analysis | Strong |
| F004 HBV vaccine & surveillance | 26651252, 42017860, 28870397 | Human/guidelines | Strong |
| F005 Prognostic factors | 42323530, 42480815, 42449617 | Cohort | Strong |
| F006 Animal models | 30967480, 28874700, 31144474 | Model organism | Moderate |
| F007 Noninvasive imaging dx | 38951191, 40487794, 40055232 | Diagnostic accuracy | Strong |
| F008 Immunosuppressive TME | 42467392, 42481381, 42470438 | Human/multi-omics | Strong |
| F009 Stage-based treatment | 34696292, 36813012, 33780876 | Guidelines | Strong |
| F010 PNPLA3 / non-cirrhotic NAFLD-HCC | 25278690 | Human review | Moderate |
| F011 Coffee protective | 28490552, 28846640, 32830818 | Dose-response meta-analysis | Strong |
| F012 Metabolic reprogramming | 33771982, 28768434 | In vitro/mechanistic | Moderate |
| F013 Sex dimorphism | 36563929, 18089782 | Human/mouse | Moderate |
| F014 Paraneoplastic syndromes | 35649187, 24480222, 34974464 | Cohort/review | Moderate |
| F015 Epigenetic dysregulation | 40057667, 40814770, 42286554, 39614377 | Mechanistic | Strong |

**Selected landmark evidence.** The genomic landscape defining TERT/TP53/CTNNB1 as initiating events ([PMID: 33958712](https://pubmed.ncbi.nlm.nih.gov/33958712/)) and the multi-ancestry GWAS of 15 risk loci ([PMID: 42357869](https://pubmed.ncbi.nlm.nih.gov/42357869/)) anchor the genetics sections. The IMbrave150-based practice change ([PMID: 42022453](https://pubmed.ncbi.nlm.nih.gov/42022453/)) and the TME/anti-VEGF+ICI mechanism ([PMID: 42467392](https://pubmed.ncbi.nlm.nih.gov/42467392/)) together explain modern treatment. Coffee dose-response meta-analyses ([PMID: 28490552](https://pubmed.ncbi.nlm.nih.gov/28490552/); [PMID: 28846640](https://pubmed.ncbi.nlm.nih.gov/28846640/)) provide the strongest protective-factor evidence.

---

## Limitations and Knowledge Gaps

1. **Etiologic drift not fully quantified.** The transition from viral to metabolic (MASLD/MASH) HCC is documented directionally but exact future incidence projections remain uncertain ([PMID: 32319693](https://pubmed.ncbi.nlm.nih.gov/32319693/)).
2. **Non-cirrhotic HCC.** NAFLD-HCC arising in non-cirrhotic livers challenges surveillance strategies keyed to cirrhosis ([PMID: 25278690](https://pubmed.ncbi.nlm.nih.gov/25278690/)); no validated surveillance protocol exists for this population.
3. **Surveillance sensitivity.** Ultrasound ± AFP has suboptimal sensitivity and poor real-world uptake; emerging biomarkers (SEPT9, GAAD, ctDNA) need prospective validation and survival-benefit confirmation ([PMID: 42017860](https://pubmed.ncbi.nlm.nih.gov/42017860/); [PMID: 42390849](https://pubmed.ncbi.nlm.nih.gov/42390849/)).
4. **Model fidelity.** Murine models incompletely recapitulate human tumor complexity, limiting translation ([PMID: 30967480](https://pubmed.ncbi.nlm.nih.gov/30967480/)).
5. **Predictive biomarkers for immunotherapy.** No robust biomarker reliably predicts response to atezolizumab+bevacizumab / durvalumab+tremelimumab; ~70% do not achieve objective response.
6. **No dedicated experimental data.** This report is a literature synthesis; no primary dataset was analyzed. Findings F001–F015 rest on published human, model-organism, and in vitro evidence, and some ontology IDs (MONDO/HPO/GO/CL/UBERON/CHEBI/MAXO) are suggested and should be verified against current ontology releases.

---

## Proposed Follow-up Experiments / Actions

1. **Validate multi-analyte early-detection panels** (methylated SEPT9 + AFP + PIVKA-II/GAAD + cfDNA fragmentomics) prospectively for survival benefit, especially in non-cirrhotic MASLD-HCC.
2. **Develop and validate risk-stratified surveillance models** incorporating PNPLA3 genotype, FIB-4/liver stiffness, and etiology to tailor surveillance intensity ([PMID: 41921193](https://pubmed.ncbi.nlm.nih.gov/41921193/)).
3. **Immunotherapy response biomarkers:** correlate TME composition (Treg/M2 density, PD-L1, Wnt/β-catenin activation status) with response to anti-VEGF+ICI to enable patient selection.
4. **Test epigenetic combination therapy:** demethylating agents (5-Aza) restoring SFRP5/C14MC + checkpoint blockade in preclinical models.
5. **Chemoprevention trials:** prospective evaluation of metformin (in diabetics) and coffee/caffeine as adjunct prevention in high-risk cirrhosis.
6. **Sex-hormone axis intervention:** explore AR-targeting strategies given the androgen-driven early carcinogenesis mechanism.
7. **Improve models:** develop humanized/organoid systems that better capture the immunosuppressive TME for translational immunotherapy testing.

---

*Report compiled from 15 confirmed findings and 92 reviewed papers. Evidence types span human clinical/epidemiological, model-organism, in vitro, and computational sources as annotated. Ontology suggestions (MONDO, HPO, GO, CL, UBERON, CHEBI, MAXO) are provided for knowledge-base curation and should be verified against current ontology releases.*


## Artifacts

- [OpenScientist final report](Hepatocellular_Carcinoma-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hepatocellular_Carcinoma-deep-research-openscientist_artifacts/final_report.pdf)
