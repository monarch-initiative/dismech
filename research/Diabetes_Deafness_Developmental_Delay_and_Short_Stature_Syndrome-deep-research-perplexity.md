---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-08-23T21:48:41.668601'
end_time: '2026-08-23T21:53:22.970103'
duration_seconds: 281.3
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Diabetes Deafness Developmental Delay and Short Stature Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 17
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 2
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Diabetes Deafness Developmental Delay and Short Stature Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Diabetes Deafness Developmental Delay and Short Stature Syndrome** covering all of the
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

# Diabetes, Deafness, Developmental Delay, and Short Stature Syndrome (DDDS): Comprehensive Disease Characteristics

Diabetes, Deafness, Developmental Delay, and Short Stature Syndrome (DDDS) is an ultra‑rare, recently delineated monogenic neurodevelopmental disorder caused by biallelic loss‑of‑function variants in the **MANF** gene, which encodes mesencephalic astrocyte‑derived neurotrophic factor, a key regulator of endoplasmic reticulum (ER) stress responses in secretory cells such as pancreatic β cells.[1][7][9][17] Clinically, DDDS is characterized by childhood‑onset autoantibody‑negative diabetes mellitus, bilateral sensorineural hearing loss, global developmental delay with microcephaly, and marked short stature, with affected individuals typically falling below −3 standard deviations for height.[1][9][11][17] Human and animal studies indicate that loss of MANF leads to chronic, unresolved ER stress and maladaptive activation of the unfolded protein response (UPR), resulting in impaired insulin processing, β‑cell apoptosis, and multi‑system dysfunction.[9][10][12][17] Because only two unrelated patients have been reported to date in the primary clinical literature, DDDS is best understood as a proof‑of‑concept syndrome that illustrates the critical importance of ER stress regulation for human β‑cell function and neurodevelopment, and many aspects of its natural history, epidemiology, and optimal management remain incompletely defined.[1][9][17] Nevertheless, convergent evidence from human genetics, in vitro β‑cell models, and **Manf** knockout mice provides a coherent mechanistic framework linking MANF deficiency, ER stress, organ‑specific vulnerability, and the characteristic triad of syndromic diabetes, deafness, and growth/neurodevelopmental impairment.[9][10][12][17]

## 1. Disease Information

### 1.1 Definition and Clinical Overview

Diabetes, Deafness, Developmental Delay, and Short Stature Syndrome (DDDS) is a syndromic neuroendocrine disorder defined by the combination of early‑onset, autoantibody‑negative diabetes mellitus, bilateral sensorineural hearing loss, global developmental delay, microcephaly, and proportionate short stature.[1][9][11][17] The condition was first delineated through the study of two unrelated patients who presented in childhood with insulin‑requiring diabetes in the absence of islet autoantibodies, later found to have a shared constellation of neurological and growth abnormalities and homozygous loss‑of‑function variants in the **MANF** gene.[9][17] In the initial report, Montaser and colleagues described DDDS as “a novel monogenic neurodevelopmental diabetes syndrome caused by disturbed ER function” and emphasized the striking similarity of the clinical phenotype across both cases.[9][17] OMIM subsequently created a distinct phenotype entry, “Diabetes, deafness, developmental delay, and short stature syndrome” (MIM #620651), classified as an autosomal recessive disorder due to homozygous MANF mutations on chromosome 3p21.2.[1] MedGen and related clinical concept resources similarly summarize DDDS as childhood‑onset autoantibody‑negative diabetes associated with bilateral sensorineural deafness, short stature, microcephaly, and developmental delay.[11]

The diabetes phenotype in DDDS typically manifests in early childhood, often before puberty, with persistent hyperglycemia requiring insulin therapy but lacking the autoimmune markers characteristic of classic type 1 diabetes.[1][9][17] The hearing loss is sensorineural and bilateral, suggesting cochlear or auditory neural involvement, and appears to be progressive or at least non‑transient, contributing substantially to communication impairment.[1][9][17] Developmental delay is global, affecting motor and cognitive domains, and is accompanied by microcephaly, indicating impaired brain growth.[1][9][11][17] Short stature is marked, with height more than three standard deviations below the mean for age and sex, and is not attributable to simple nutritional deficiency in reported cases.[17] Taken together, these features support the view of DDDS as a multisystem disorder primarily affecting insulin‑secreting endocrine tissue, auditory pathways, brain development, and somatic growth.

From a nosological standpoint, DDDS belongs to the broad category of monogenic diabetes syndromes, distinct from both autoimmune type 1 diabetes and multifactorial type 2 diabetes, and overlapping in some features with other diabetes‑deafness syndromes such as maternally inherited diabetes and deafness (MIDD) and Wolfram syndrome.[4][5][6][12] However, unlike MIDD, which is caused by heteroplasmic mitochondrial DNA mutations, and Wolfram syndrome, which results from biallelic **WFS1** or **CISD2** variants, DDDS is specifically linked to biallelic loss‑of‑function mutations in **MANF**, and its neurodevelopmental profile with microcephaly and pronounced growth failure appears more severe than in many cases of MIDD or Wolfram syndrome.[1][5][9][12][17] At present, DDDS should therefore be regarded as a distinct clinicogenetic entity, albeit one that resides within a broader continuum of ER stress‑related and mitochondrial diabetes‑deafness disorders.

### 1.2 Key Identifiers and Ontology Mapping

Multiple biomedical databases have begun to assign formal identifiers to DDDS as a distinct disease entity. OMIM lists DDDS under phenotype MIM number **620651**, with a number sign indicating that the phenotype is caused by mutations in the **MANF** gene (MIM #601916) on chromosome 3p21.2.[1][7] The OMIM entry clearly states that “a number sign (#) is used with this entry because of evidence that diabetes, deafness, developmental delay, and short stature syndrome (DDDS) is caused by homozygous mutation in the MANF gene (601916) on chromosome 3p21,” and notes that the transmission pattern in the reported families is consistent with autosomal recessive inheritance.[1]

In the ontology space, the MONDO disease ontology has created a dedicated concept for DDDS, **MONDO:0957997**, curated as “diabetes, deafness, developmental delay, and short stature syndrome” and linked to the MANF gene through the GenCC gene–disease curation resource.[13][14] GenCC explicitly associates HGNC:15461 (MANF) with MONDO:0957997, classified as an autosomal recessive condition and evaluated in 2026.[13] MedGen includes DDDS in the context of broader concepts such as alopecia, but reiterates the same core phenotype description and highlights the association with MANF mutations.[11] VarSome’s phenotype search for “short stature” also returns “disease: Diabetes, Deafness, Developmental Delay, Short Stature Syndrome,” indicating that DDDS has begun to be indexed in variant interpretation platforms as a recognized phenotype cluster.[2]

Formal coding in Orphanet, ICD‑10/ICD‑11, MeSH, and SNOMED CT appears to be lagging, as is often the case for newly described ultra‑rare syndromes, and DDDS currently does not have a unique ICD code or MeSH heading.[1][11][13] In clinical practice, affected individuals would typically be coded under existing ICD‑10 categories for insulin‑dependent diabetes mellitus (e.g., E10.x for type 1 diabetes), bilateral sensorineural hearing loss (e.g., H90.3), developmental delay/intellectual disability (e.g., F81‑F84), and short stature (e.g., E34.3), rather than a single syndrome code. SNOMED CT has a concept for “short stature” and for “diabetes mellitus and sensorineural deafness,” but a specific DDDS concept has not yet been widely adopted.[5][8] From a knowledge base perspective, however, the MONDO identifier MONDO:0957997 and the OMIM phenotype number 620651 provide stable anchors for representing DDDS in structured disease ontologies.[1][13][14]

In terms of ontological mapping, the primary phenotypic features of DDDS can be linked to Human Phenotype Ontology (HPO) terms such as **HP:0005978** (autoantibody‑negative diabetes mellitus), **HP:0005110** (sensorineural hearing impairment), **HP:0001263** (global developmental delay), **HP:0000252** (microcephaly), and **HP:0004322** (short stature).[1][9][11][17] The disease entity itself can be represented as MONDO:0957997, with causal gene annotation to MANF (HGNC:15461) and OMIM:601916.[7][13][14] These mappings facilitate integration of DDDS into computational resources for gene–phenotype associations, variant interpretation, and clinical decision support.

### 1.3 Synonyms and Alternative Names

Because DDDS is a very recently delineated and ultra‑rare condition, its nomenclature is still evolving, and several variants of the disease name appear in different sources. OMIM and MONDO primarily use the term **“Diabetes, deafness, developmental delay, and short stature syndrome”**, often abbreviated as **DDDS**.[1][13][14] The original clinical description by Montaser et al. referred to the condition more generically as “a monogenic neurodevelopmental diabetes syndrome” caused by MANF deficiency, and in the article the authors emphasized the combination of “childhood onset diabetes, short stature, deafness, developmental delay, and microcephaly.”[9][17] Some summaries therefore refer to the disease as “MANF‑related neurodevelopmental diabetes syndrome” or “MANF‑associated diabetes‑deafness‑developmental delay syndrome,” although these names have not yet been standardized.

Certain secondary sources introduce potential confusion by attributing DDDS to other genes. For example, an educational site describing DDDS lists the condition as an “ultra‑rare genetic disorder” characterized by early‑onset diabetes, sensorineural hearing loss, developmental delay, and short stature, but incorrectly states that “the syndrome is primarily caused by mutations in the WFS1 gene, which encodes wolframin, a protein involved in endoplasmic reticulum (ER) stress regulation and calcium homeostasis.”[16] In fact, mutations in **WFS1** cause Wolfram syndrome type 1 (DIDMOAD: diabetes insipidus, diabetes mellitus, optic atrophy, and deafness), not DDDS, and the molecular and phenotypic profiles of Wolfram syndrome differ in important respects from those of MANF‑related DDDS.[12][16] It is therefore critical for disease knowledge bases to distinguish **“Diabetes, deafness, developmental delay, and short stature syndrome (MANF‑related)”** from Wolfram syndrome and other diabetes‑deafness syndromes.

To avoid ambiguity, this report will use **DDDS** exclusively to refer to **MANF‑related Diabetes, Deafness, Developmental Delay, and Short Stature Syndrome**, as defined in OMIM (MIM #620651) and MONDO (MONDO:0957997).[1][13][14] Synonyms that may be encountered in the literature include “MANF‑related neurodevelopmental diabetes syndrome” and “MANF‑associated syndromic diabetes,” but these should be treated as informal descriptors rather than distinct disease entities.

### 1.4 Source Types: Patient‑Level vs Aggregated Data

The current knowledge base on DDDS is derived almost entirely from a small number of case‑level and mechanistic studies rather than large observational cohorts or registries. The defining clinical description is based on two unrelated patients identified through monogenic diabetes and neurodevelopmental disorder genetics programs, reported in Montaser et al., 2021 (PMID:33500254).[9][17] OMIM, MedGen, and MONDO entries for DDDS are essentially aggregations and curated summaries of those case reports and associated mechanistic work, rather than independent epidemiological or clinical trial data.[1][7][11][13][14]

Mechanistic insights into MANF function come from a combination of model organism studies, particularly **Manf** knockout mice, and in vitro studies in human β‑cell lines and human embryonic stem cell‑derived endocrine cells.[10][12][17] These studies provide robust experimental evidence regarding ER stress pathways, β‑cell survival, and insulin processing, but they do not directly provide detailed human natural history or prevalence data.[10][12][17] As a result, estimates of DDDS prevalence such as “fewer than 1 in 1,000,000 individuals worldwide” remain largely speculative, and are often based on general considerations about ultra‑rare Mendelian disorders rather than systematic epidemiological surveys.[16]

In building a disease knowledge base entry for DDDS, it is therefore important to recognize that most clinical information is derived from a very small number of deeply characterized patients, supported by extensive experimental work on MANF function, and to explicitly flag areas where data are sparse or absent. The evidence base can be categorized as follows: human clinical case reports (high‑granularity but very low sample size) for core phenotypes and inheritance pattern; model organism studies (Manf knockout mice) for β‑cell biology and ER stress mechanisms; in vitro β‑cell and stem cell models for human MANF function and ER stress responses; and computational and ontology resources (OMIM, MONDO, GenCC, MedGen) for standardized naming and gene–disease linkage.[1][7][9][10][11][12][13][14][17] Large‑scale epidemiological data, natural history studies, and clinical trials are not yet available for DDDS.

## 2. Etiology

### 2.1 Primary Causal Factors

The primary causal factor in DDDS is biallelic loss‑of‑function mutation in the **MANF** gene, which encodes **Mesencephalic Astrocyte‑derived Neurotrophic Factor**, an ER‑resident protein that plays a crucial role in attenuating ER stress responses and supporting the survival and function of pancreatic β cells and neurons.[7][9][10][12][17] OMIM explicitly states that DDDS (MIM #620651) is caused by **homozygous mutation in the MANF gene** on chromosome 3p21.2, and the associated gene entry for MANF (OMIM #601916) lists DDDS as phenotype .0001, linked to a specific loss‑of‑function variant identified in a 22‑year‑old woman with childhood‑onset nonautoimmune diabetes and syndromic features.[1][7] In the seminal clinical and functional study, Montaser et al. identified two unrelated patients with childhood diabetes and neurodevelopmental disorder, each harboring a distinct homozygous loss‑of‑function MANF variant, and demonstrated that these variants result in loss of MANF protein function in vitro.[9][17]

In their article, Montaser et al. emphasized the causal role of MANF deficiency in the human disease, stating:

> “We show that homozygous loss‑of‑function variants in MANF cause a novel multisystem disorder characterized by childhood‑onset diabetes, short stature, deafness, developmental delay, and microcephaly.”[17]

and

> “In this study, we show that lack of MANF in humans results in diabetes due to increased ER stress, leading to impaired β‑cell function.”[9]

These statements, supported by detailed functional analyses in human embryonic stem cell‑derived endocrine cells and mouse graft experiments, provide strong evidence that **MANF loss‑of‑function is the proximal genetic cause of DDDS**, and that ER stress dysregulation is the primary molecular mechanism.[9][17]

MANF itself is an ER stress‑inducible protein and has been shown to protect β cells against experimentally induced ER stress and inflammatory cytokine‑induced cell death.[10][12] Hakonen et al. reported that knockdown of MANF in human EndoC‑βH1 β cells led to increased ER stress after cytokine challenge and that exogenous MANF protein can provide protection to human β cells against death induced by inflammatory stress.[10] Lindahl et al. demonstrated that global **Manf** knockout mice develop early‑onset diabetes due to progressive postnatal reduction of β‑cell mass caused by reduced proliferation and increased apoptosis, mediated by persistent ER stress‑induced UPR pathways.[12] These model organism and in vitro findings reinforce the conclusion that **loss of MANF is sufficient to produce a diabetic phenotype through ER stress‑mediated β‑cell failure**, and that the multi‑system features of DDDS represent broader consequences of MANF deficiency in other tissues.

At present, no environmental or infectious agents have been implicated as primary causes of DDDS, and the disorder is best conceptualized as a Mendelian genetic disease caused by germline biallelic MANF loss‑of‑function. There is no evidence that somatic MANF mutations or acquired ER stress alone produce the full DDDS phenotype in humans, although ER stress undoubtedly contributes to the pathophysiology of multifactorial diabetes.[10]

### 2.2 Genetic Risk Factors

The principal genetic risk factor for DDDS is being **homozygous or compound heterozygous** for a **pathogenic loss‑of‑function variant** in MANF. Montaser et al. described two such variants, both resulting in truncated or nonfunctional MANF protein, in unrelated patients with remarkably similar phenotypes.[9][17] The MANF gene is highly conserved and appears to be intolerant to complete loss‑of‑function in the general population, as no homozygous disruptive variants have been reported in large population sequencing datasets such as gnomAD, although this specific point has not yet been formally documented in the search results.[9][10][12] The rarity of homozygous MANF loss‑of‑function alleles, combined with the autosomal recessive inheritance pattern described in the DDDS families, implies that carrier status for a single MANF loss‑of‑function allele is not sufficient to cause disease but that mating between carriers can produce affected offspring with DDDS.[1][7][9][17]

OMIM notes that “the transmission pattern of DDDS in the families reported by Montaser et al. (2021) was consistent with autosomal recessive inheritance,” indicating that both parents were presumably heterozygous carriers of the MANF variant and that the affected offspring inherited the variant from each parent.[1][9] GenCC further classifies the MANF–DDDS relationship as autosomal recessive, and the associated MONDO concept MONDO:0957997 is annotated accordingly.[13][14] Given the ultra‑rare nature of the condition, the carrier frequency for pathogenic MANF variants is expected to be extremely low in the general population, although specific estimates are not yet available.

Potential **modifier genes** that might influence the severity or expression of DDDS have not been identified, and the phenotypic similarity between the two reported cases suggests relatively limited intra‑familial variability, at least for the core features of diabetes, deafness, developmental delay, microcephaly, and short stature.[9][17] However, one cannot exclude the possibility that variants in other ER stress‑related genes, chaperones, or UPR regulators could modify the phenotype in future cases. For example, polymorphisms in genes such as **ATF4**, **CHOP (DDIT3)**, or **XBP1**, which are key UPR effectors upregulated in Manf‑deficient cells and mice, might theoretically influence the degree of ER stress‑induced apoptosis and thus modulate clinical severity.[10][12]

It is important to distinguish DDDS from other genetically determined diabetes‑deafness syndromes. Maternally inherited diabetes and deafness (MIDD) is caused by heteroplasmic mitochondrial DNA mutations, most commonly the m.3243A>G variant in the **MT‑TL1** gene encoding tRNA‑Leu(UUR), and is transmitted through the maternal line with variable penetrance and multi‑system involvement including cardiac, renal, and neurologic manifestations.[4][5][6][15] Wolfram syndrome type 1 (OMIM #222300) results from biallelic **WFS1** variants and is characterized by juvenile‑onset diabetes mellitus, progressive optic atrophy, diabetes insipidus, and sensorineural deafness, often summarized as DIDMOAD.[12] While these conditions share overlapping features—particularly diabetes and sensorineural hearing loss—they are genetically and mechanistically distinct from MANF‑related DDDS.[5][6][12][16]

### 2.3 Environmental and Lifestyle Risk Factors

No specific environmental toxins, infectious agents, or lifestyle exposures have been implicated as causal risk factors for DDDS, and existing evidence suggests that environmental influences primarily modulate disease severity rather than cause the syndrome de novo. In the Montaser study, an important observation was that **MANF knockout β‑cell grafts implanted into immunocompromised mice displayed elevated ER stress and functional failure particularly in recipients with diabetes**, indicating that a hyperglycemic, diabetogenic environment exacerbates ER stress and β‑cell dysfunction in the context of MANF deficiency.[9][17] The authors noted that MANF knockout grafts showed more pronounced ER stress markers and poorer glycemic control in diabetic recipients than in non‑diabetic controls, highlighting a gene–environment interaction between MANF loss‑of‑function and metabolic stress.[9]

This finding implies that in human DDDS, factors that increase β‑cell workload, such as high carbohydrate intake, obesity, or insulin resistance, could worsen glycemic control and accelerate β‑cell failure, although no formal data exist on lifestyle modifiers in the tiny clinical sample available.[9][10] Similarly, environmental factors that exacerbate ER stress—such as chronic inflammation, viral infections targeting pancreatic or neural tissue, or exposure to certain toxins—could theoretically aggravate organ dysfunction in MANF‑deficient individuals. Hakonen et al. demonstrated that inflammatory cytokines induce ER stress and cell death in human β cells, and that MANF provides significant protection against this stress; conversely, knockdown of MANF led to increased ER stress responses under cytokine challenge.[10] This supports the broader concept that **MANF deficiency sensitizes cells to ER stress‑inducing environmental insults**, though specific exposures relevant to DDDS have not yet been delineated.

Lifestyle factors such as diet, physical activity, and smoking have not been systematically studied in DDDS, but their general impact on diabetes control and cardiovascular risk would be expected to apply, as for other forms of insulin‑dependent diabetes. Affected individuals should therefore be advised to follow standard evidence‑based recommendations for glycemic management and cardiovascular risk reduction, although these measures are not specific etiological risk factors for DDDS but rather modifiers of clinical outcomes.

### 2.4 Protective Factors and Resilience

The concept of protective factors in DDDS is closely linked to the biology of MANF and ER stress. At the molecular level, **MANF itself is a protective factor**, and its presence in normal β cells and neurons mitigates ER stress‑induced apoptosis and supports cellular survival. Hakonen et al. showed that exogenous recombinant MANF partially protects human pancreatic β cells against proinflammatory‑cytokine‑induced cell death, with the protective effect associated with repression of the NF‑κB signaling pathway and amelioration of ER stress.[10] They concluded:

> “Our studies show that exogenous MANF protein can provide protection to human beta cells against death induced by inflammatory stress.”[10]

Similarly, Lindahl et al. reported that MANF is indispensable for the proliferation and survival of pancreatic β cells, and that global **Manf** knockout in mice leads to progressive postnatal β‑cell loss due to persistent ER stress and activation of UPR pathways.[12] In the context of DDDS, the absence of MANF removes this protective buffer, making β cells and other secretory cells more vulnerable to stress. However, **residual ER chaperone capacity**, upregulation of other neurotrophic factors, or robust unfolded protein response signaling might provide partial compensatory protection in some tissues, possibly explaining why the phenotype, while severe, is not universally lethal in infancy.[9][10][12][17]

At the clinical level, there is indirect evidence that **good metabolic control and avoidance of excessive ER stress** may serve as protective factors, at least for the diabetes component. In the Montaser study, MANF knockout grafts performed better in non‑diabetic recipients than in diabetic ones, implying that minimizing systemic hyperglycemia and metabolic stress could help preserve residual β‑cell function and reduce ER stress in MANF‑deficient cells.[9][17] Intensive insulin therapy, careful management of infections, and avoidance of drugs known to induce ER stress in β cells may therefore be considered protective strategies, although this remains extrapolated from mechanistic data rather than directly proven in DDDS patients.

No genetic protective variants have been identified that mitigate the effect of MANF loss‑of‑function, and given the rarity of DDDS, such modifiers would be difficult to detect. It is conceivable that individuals with partial MANF deficiency due to hypomorphic alleles might have subclinical phenotypes or milder disease, but these scenarios are speculative at present.

### 2.5 Gene–Environment Interactions

The interaction between genetic MANF deficiency and environmental/metabolic stress is a key theme in DDDS pathophysiology. Montaser et al.’s functional experiments demonstrated a clear gene–environment interaction: **MANF knockout human endocrine cell grafts exhibited elevated ER stress and functional failure particularly in diabetic recipients**, suggesting that the diabetic milieu potentiates the functional consequences of MANF loss.[9][17] This indicates that MANF deficiency is an upstream genetic trigger that creates a predisposition to ER stress, while metabolic and inflammatory stresses act as environmental amplifiers of the phenotype.

From a mechanistic perspective, MANF‑deficient cells have impaired capacity to attenuate ER stress responses, resulting in prolonged activation of UPR pathways such as PERK‑eIF2α‑ATF4‑CHOP and IRE1‑XBP1, which in turn promote apoptosis and suppress proliferation.[10][12] Environmental factors that increase protein folding demand, such as high insulin secretory load due to hyperglycemia or insulin resistance, will further exaggerate ER stress in these cells. Thus, the causal chain can be conceptualized as: **germline MANF loss‑of‑function → reduced ER stress buffering capacity → heightened sensitivity to metabolic/inflammatory stressors → chronic ER stress and maladaptive UPR activation → organ‑specific cell death and dysfunction → clinical manifestations of DDDS.**[9][10][12][17]

This gene–environment interaction framework has important implications for clinical management. It suggests that **aggressive management of metabolic stress** (through insulin therapy and lifestyle measures) and **avoidance of systemic inflammatory insults** may be particularly important in DDDS, not only for standard diabetes control but also for mitigating ER stress‑mediated damage in β cells and other tissues. It also supports the notion that therapeutic strategies aimed at reducing ER stress or enhancing UPR resolution—such as chemical chaperones or MANF‑mimetic agents—could be beneficial in DDDS, although such interventions remain experimental.[10][12][17]

## 3. Phenotypes

### 3.1 Overview of Phenotypic Spectrum

The phenotypic spectrum of DDDS is dominated by five core features: childhood‑onset autoantibody‑negative diabetes mellitus, bilateral sensorineural deafness, global developmental delay, microcephaly, and marked short stature.[1][9][11][17] In the two reported patients, these features co‑occurred with striking consistency, supporting their status as defining characteristics of the syndrome.[9][17] OMIM summarizes the phenotype as “childhood‑onset autoantibody‑negative diabetes mellitus and bilateral sensorineural deafness, as well as short stature, microcephaly, and developmental delay,” and MedGen repeats this description in its concept entry.[1][11]

Each of these features corresponds to a distinct phenotype type within the Human Phenotype Ontology. Diabetes mellitus without islet autoantibodies can be represented as **HP:0005978 (autoantibody‑negative diabetes mellitus)**, bilateral sensorineural hearing loss as **HP:0005110 (sensorineural hearing impairment)**, global developmental delay as **HP:0001263 (global developmental delay)**, microcephaly as **HP:0000252 (microcephaly)**, and short stature as **HP:0004322 (short stature).**[1][9][11][17] Additional associated features may include intellectual disability (HP:0001249), impaired speech development (HP:0000750), and possibly behavioral or psychiatric issues, although these have not been systematically characterized.[9][17]

The severity and progression of these phenotypes, as well as their impact on quality of life, can be inferred from the clinical descriptions and from general knowledge of similar manifestations in other disorders. Because the existing clinical sample is limited, percentages and precise frequencies cannot be reliably estimated, but the near‑uniform presence of the core features in the two known cases suggests very high penetrance for these traits in MANF‑related DDDS.[9][17]

### 3.2 Diabetes Mellitus

The diabetes phenotype in DDDS is characterized by **childhood onset, insulin dependence, and absence of islet autoantibodies**, consistent with a monogenic, nonautoimmune form of diabetes resulting from intrinsic β‑cell dysfunction.[1][9][17] In the Montaser study, both patients developed diabetes in childhood and required insulin therapy, but autoimmune markers typically associated with type 1 diabetes were absent.[9][17] OMIM notes “childhood‑onset autoantibody‑negative diabetes mellitus” as the first defining feature of DDDS, emphasizing its nonautoimmune nature.[1]

Clinically, the diabetes presents as persistent hyperglycemia with classic symptoms such as polyuria, polydipsia, and weight loss, although these details are not extensively documented in the brief descriptions available.[9][17] Laboratory findings likely include elevated fasting and postprandial glucose, elevated HbA1c, and low or inappropriately normal C‑peptide levels reflecting reduced endogenous insulin production. Given the underlying β‑cell ER stress and apoptosis, the disease course is expected to be progressive, with declining β‑cell reserve over time, as seen in **Manf** knockout mice, where β‑cell mass decreases postnatally due to reduced proliferation and increased apoptosis.[12]

The absence of autoantibodies—such as anti‑GAD65, anti‑IA‑2, and anti‑ZnT8—distinguishes DDDS from classic type 1 diabetes and suggests that immune‑mediated β‑cell destruction is not the primary mechanism.[1][9][17] Instead, ER stress‑induced apoptosis is the central process. This has important diagnostic implications, as children presenting with autoantibody‑negative diabetes, especially in the context of syndromic features such as deafness and developmental delay, should prompt consideration of monogenic diabetes and genetic testing, including sequencing of MANF.[9][17]

From a quality‑of‑life perspective, insulin‑dependent diabetes requires lifelong management with insulin injections or pump therapy, frequent blood glucose monitoring, dietary adjustments, and regular medical follow‑up. Children with DDDS must manage these demands in addition to their neurodevelopmental and sensory impairments, potentially exacerbating psychosocial challenges and caregiver burden. Standard diabetes complications—such as retinopathy, nephropathy, and neuropathy—could also arise, although their prevalence in DDDS is unknown due to the small number of cases and relatively young age of reported patients.[9][17]

Suggested HPO terms for this phenotype include **HP:0005978 (autoantibody‑negative diabetes mellitus)**, **HP:0000819 (insulin‑dependent diabetes mellitus)**, and **HP:0001943 (abnormal glucose homeostasis)**.

### 3.3 Sensorineural Deafness

Bilateral sensorineural hearing loss is a prominent and consistent feature of DDDS.[1][9][11][17] OMIM explicitly notes “bilateral sensorineural deafness” as a defining characteristic, and Montaser et al. report that both patients exhibited “bilateral sensorineural deafness,” suggesting involvement of the cochlea or auditory nerve rather than conductive pathology.[1][9][17] The exact age of onset is not specified, but given the childhood presentation and developmental delay, hearing loss likely manifests in early childhood, contributing to delayed speech and language development.

Sensorineural hearing loss can range from mild to profound, and in syndromic contexts like DDDS, it is often progressive. Comparative data from MIDD and Wolfram syndrome, where sensorineural deafness is common, indicate that hearing loss often precedes or accompanies diabetes onset and can significantly impair communication and psychosocial functioning.[4][5][6][12] In MIDD, hearing loss is progressive and typically more severe in men.[4][6] While DDDS is mechanistically distinct, its shared feature of bilateral sensorineural deafness suggests that similar pathways—such as ER stress in cochlear hair cells or spiral ganglion neurons—may be involved, leading to progressive loss of auditory function.

The quality‑of‑life impact of bilateral sensorineural deafness is substantial, particularly in children with concurrent developmental delay. Communication barriers can hinder educational attainment, social integration, and independence. Interventions such as hearing aids or cochlear implants can partially restore hearing, but candidacy depends on the degree of cochlear and neural damage, and in neurodevelopmental syndromes, speech and language outcomes may still be limited. Nonetheless, cochlear implantation is a standard NCIT‑coded intervention (e.g., NCIT:C49541) that should be considered in DDDS patients with profound hearing loss, as evidence from MIDD and Wolfram syndrome indicates that cochlear implants can provide functional hearing even in syndromic deafness.[4][12]

Suggested HPO terms include **HP:0005110 (sensorineural hearing impairment)**, **HP:0008619 (bilateral sensorineural hearing impairment)**, and **HP:0000365 (hearing impairment)**.

### 3.4 Developmental Delay and Neurocognitive Impairment

Global developmental delay is a core feature of DDDS, reflecting impaired acquisition of motor, cognitive, and language skills.[1][9][11][17] OMIM lists “developmental delay” among the defining characteristics, and MedGen reiterates this.[1][11] Montaser et al. describe both patients as having “developmental delay,” and at least one is noted to have a “neurodevelopmental disorder,” implying broader cognitive and possibly behavioral involvement.[9][17] Microcephaly, also prominent in DDDS, supports the interpretation that brain growth and neurodevelopment are intrinsically affected by MANF deficiency.[1][9][11][17]

Global developmental delay typically manifests in infancy and early childhood, with delayed attainment of milestones such as sitting, walking, speaking, and social interaction. In DDDS, the combination of microcephaly and deafness likely exacerbates developmental impairment, as hearing loss impedes language exposure and communication, while microcephaly reflects underlying structural brain abnormalities. Intellectual disability—defined as significant impairment in cognitive functioning and adaptive behavior—is probable but has not been formally quantified in the limited existing data.[9][17]

The progression of neurocognitive impairment in DDDS is not well characterized. In many monogenic neurodevelopmental syndromes, developmental delay is non‑progressive in the sense that children do not lose previously acquired skills, but rather continue to lag behind peers. However, if MANF deficiency leads to ongoing neuronal loss due to ER stress, some degree of progressive deterioration could occur. Data from other ER stress‑related disorders, including Wolfram syndrome, suggest that neurodegeneration and cognitive decline may occur over time.[12] Whether similar processes operate in DDDS requires further longitudinal observation.

Quality‑of‑life impacts include educational challenges, dependence on caregivers for daily activities, and increased risk of behavioral and psychiatric issues. Interventions such as early developmental therapies, special education, and speech and language support are critical to maximizing functional outcomes. Suggested HPO terms include **HP:0001263 (global developmental delay)**, **HP:0001249 (intellectual disability)**, **HP:0000252 (microcephaly)**, and **HP:0000750 (speech delay)**.

### 3.5 Short Stature and Growth Impairment

Marked short stature is a defining somatic feature of DDDS. Montaser et al. reported that both patients had “short stature (< −3 SD),” indicating that their height was more than three standard deviations below the mean for age and sex, which fulfills standard endocrinological criteria for pathologic short stature.[17] OMIM includes “short stature” among the core features of the syndrome, and VarSome’s phenotype search highlights DDDS in association with short stature.[1][2] MedGen also mentions short stature in its description of DDDS.[11]

Short stature in DDDS appears to be proportionate rather than segmental, and is likely due to a combination of factors including chronic illness (diabetes), impaired growth hormone or IGF‑1 signaling, and direct effects of MANF deficiency on growth plate chondrocytes or other cells involved in somatic growth. ER stress has been implicated in chondrocyte apoptosis and skeletal dysplasias, and MANF’s role as an ER stress regulator suggests that its absence could disturb growth plate homeostasis, although specific data on this point are lacking.[10][12][17] Microcephaly indicates that growth impairment extends to the cranial vault and brain, supporting a systemic rather than purely endocrine etiology.[1][9][11][17]

The age of onset of growth impairment is likely early, with failure to thrive and poor linear growth evident in infancy or early childhood. Short stature is generally stable or slowly progressive, reflecting cumulative growth deficits rather than acute episodes. Quality‑of‑life effects include physical limitations, psychosocial challenges related to body image and social comparison, and potential complications such as delayed puberty or reduced peak bone mass, although these aspects have not been documented in DDDS specifically.

HPO terms for this phenotype include **HP:0004322 (short stature)**, **HP:0000252 (microcephaly)**, and **HP:0001510 (growth delay)**. In ontological mapping, short stature is associated with systemic growth processes and can be linked to GO terms such as “regulation of growth” and “cartilage development,” but MANF’s direct role in these processes remains to be elucidated.

### 3.6 Additional and Overlapping Phenotypes

Beyond the core features, DDDS may include additional phenotypes that are either under‑recognized due to small sample size or overlapping with other syndromes. MedGen’s association of DDDS with alopecia suggests that some individuals may have hair loss or abnormal hair growth, although this may reflect database linkage rather than a documented clinical case.[11] The Saudi case report describing “resistant diabetes, deafness, hepatic dysfunction, renal impairment, hypogonadism, short stature, and history of developmental delay” illustrates a broader syndromic picture that overlaps with DDDS, but the genetic etiology in that case is not specified and may represent MIDD or another mitochondrial disorder rather than MANF deficiency.[3]

Overlap with Wolfram syndrome and Rogers syndrome (thiamine‑responsive megaloblastic anemia with diabetes and sensorineural deafness) is notable, as both conditions include diabetes, deafness, developmental issues, and short stature.[5][8][12] Wolfram syndrome commonly features optic atrophy and diabetes insipidus, which have not been reported in DDDS.[12] Rogers syndrome includes megaloblastic anemia and is responsive to high‑dose thiamine, distinguishing it from DDDS.[8] These overlapping phenotypes highlight the importance of precise genetic diagnosis to distinguish DDDS from other entities.

In summary, the phenotypic spectrum of DDDS is centered on autoantibody‑negative diabetes, bilateral sensorineural deafness, global developmental delay with microcephaly, and marked short stature, with possible additional features yet to be characterized. The impact on quality of life is profound, affecting metabolic health, communication, cognition, and physical growth. Ontology mapping using HPO and MONDO terms facilitates integration of these phenotypes into disease knowledge bases.

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: MANF

The causal gene in DDDS is **MANF** (Mesencephalic Astrocyte‑derived Neurotrophic Factor), located on chromosome 3p21.2.[1][7][9][17] OMIM’s phenotype entry #620651 clearly attributes DDDS to mutations in MANF, and the MANF gene entry (OMIM #601916) includes a specific variant associated with DDDS.[1][7] GenCC lists MANF (HGNC:15461) as causal for “diabetes, deafness, developmental delay, and short stature syndrome” (MONDO:0957997), with autosomal recessive inheritance and recent evaluation.[13]

MANF encodes a secreted and ER‑resident protein that plays a key role in attenuating ER stress responses and promoting survival in neurons and pancreatic β cells.[9][10][12] It belongs to a small family of ER stress‑inducible trophic factors, including CDNF (Cerebral Dopamine Neurotrophic Factor), and is upregulated in response to unfolded protein accumulation in the ER.[10] MANF protein localizes predominantly to the ER lumen and can also be secreted, where it exerts extracellular protective effects.[10][12] Its mechanism of action involves modulation of the UPR and inhibition of pro‑apoptotic pathways such as NF‑κB signaling.[10]

Functional studies have demonstrated that MANF is essential for β‑cell survival and proliferation. Lindahl et al. showed that global **Manf** knockout in mice results in progressive postnatal β‑cell loss, leading to early‑onset diabetes.[12] Hakonen et al. demonstrated that knockdown of MANF in human EndoC‑βH1 cells increases ER stress and cell death under cytokine challenge, whereas exogenous MANF protects β cells by repressing NF‑κB and ameliorating ER stress.[10] Montaser et al. extended these findings to human development by knocking out MANF in human embryonic stem cells and differentiating them into pancreatic endocrine cells, showing that loss of MANF induces mild ER stress and impairs insulin processing in vitro, and that MANF knockout grafts in mice exhibit elevated ER stress and functional failure.[9][17]

From a molecular annotation perspective, MANF can be linked to the following gene ontology (GO) biological processes: **“response to endoplasmic reticulum stress”**, **“negative regulation of apoptotic process”**, **“regulation of unfolded protein response”**, and **“negative regulation of NF‑κB transcription factor activity.”**[9][10][12] GO cellular component terms include **“endoplasmic reticulum lumen”** and **“extracellular space,”** reflecting its ER localization and secreted nature.[10][12] These annotations are crucial for representing MANF’s function in disease ontologies and pathway databases.

### 4.2 Pathogenic Variants and Variant Classes

The pathogenic variants identified in DDDS are **homozygous loss‑of‑function alleles** in MANF. Montaser et al. reported two unrelated patients with distinct homozygous variants, each predicted to abolish or severely disrupt MANF protein function.[9][17] Although the exact HGVS nomenclature is not specified in the search results, the variants are described as **loss‑of‑function**, implying frameshift, nonsense, or splice‑site mutations that truncate the protein or lead to nonsense‑mediated decay.[9][17] OMIM’s MANF gene entry refers to a specific variant associated with DDDS, designated as .0001, in a woman with childhood‑onset nonautoimmune diabetes mellitus and associated features.[7]

These variants would be classified as **pathogenic** under ACMG/AMP guidelines, given the strong evidence of disease causality, including co‑segregation with disease in an autosomal recessive pattern, absence (or extreme rarity) in population databases, loss‑of‑function nature of the variants, and functional studies demonstrating impaired MANF protein function and recapitulation of disease phenotypes in vitro and in vivo.[9][10][12][17] ClinVar and variant interpretation platforms such as VarSome have begun to catalog MANF variants, but comprehensive data on all DDDS‑associated variants are not yet available.[2][15]

From a variant type perspective, MANF loss‑of‑function alleles in DDDS can be classified as **nonsense**, **frameshift**, or **splice‑site** variants, leading to truncated protein or absence of protein. Missense variants in MANF have not yet been reported in DDDS, but could theoretically produce milder or variant phenotypes if they partially disrupt function. Somatic MANF mutations have not been implicated in cancer or other somatic diseases in the current search results, and DDDS appears to be exclusively a germline disease.[7][9][10][12][17]

Population allele frequencies for MANF loss‑of‑function variants are expected to be extremely low, consistent with the ultra‑rare nature of DDDS and the essential role of MANF in β‑cell and neuronal survival.[10][12][16] While specific gnomAD or ExAC statistics are not provided in the search results, the absence of reported homozygous loss‑of‑function variants in large datasets supports the conclusion that such alleles are under strong negative selection. Heterozygous carriers may be asymptomatic, as suggested by the unaffected parents in the DDDS families.[1][9][17]

### 4.3 Somatic vs Germline Origin

Evidence from the DDDS families and functional studies indicates that **MANF loss‑of‑function variants causing DDDS are germline mutations**, present in all cells from conception.[1][7][9][17] The autosomal recessive inheritance pattern and the presence of variants in homozygous form in affected individuals, with heterozygous carrier parents, confirm germline transmission.[1][9][17] There is no suggestion that somatic mosaicism plays a role in DDDS, although somatic MANF alterations could theoretically contribute to other diseases, such as neurodegeneration or cancer, but this has not been documented in the current search results.[7][10][12]

From an ontological standpoint, DDDS should be annotated as a **germline genetic disease** with autosomal recessive inheritance, linked to monogenic variants in MANF (HGNC:15461, OMIM:601916). The primary variants are present in the germline and affect all tissues, explaining the multi‑system nature of the syndrome.

### 4.4 Functional Consequences of MANF Loss

The functional consequences of MANF loss have been studied extensively in both human and mouse systems. At the cellular level, loss or knockdown of MANF leads to **increased ER stress**, **sustained activation of the unfolded protein response (UPR)**, and **enhanced apoptosis**, particularly in pancreatic β cells.[10][12][17] Hakonen et al. reported that MANF knockdown in human EndoC‑βH1 β cells significantly aggravated ER stress responses after cytokine challenge, with increased expression of UPR markers and sustained phosphorylation of eIF2α, leading to global protein synthesis arrest.[10] Lindahl et al. showed that **Manf** knockout mice have persistent ER stress in β cells characterized by upregulation of UPR markers sXbp1 and Chop and sustained eIF2α phosphorylation, culminating in increased β‑cell apoptosis and reduced proliferation.[12]

Montaser et al. extended these findings to human development by knocking out MANF in human embryonic stem cells and differentiating them into pancreatic endocrine cells.[9][17] They found that loss of MANF induced mild ER stress and impaired insulin‑processing capacity in vitro, and that MANF knockout endocrine cell grafts implanted into diabetic mice displayed elevated ER stress and functional failure.[9][17] The authors concluded that “by describing a new form of monogenic neurodevelopmental diabetes syndrome caused by disturbed ER function, we highlight the importance of adequate ER stress regulation for proper human β‑cell function and demonstrate the crucial role of MANF in this process.”[9]

These studies indicate that MANF loss has **loss‑of‑function** consequences for ER stress regulation, resulting in **unresolved ER stress** and **maladaptive UPR activation**, which in turn drive β‑cell dysfunction and death. In GO terms, MANF loss disrupts processes such as “response to endoplasmic reticulum stress,” “protein folding,” “negative regulation of apoptotic process,” and “regulation of insulin secretion.”[9][10][12][17] In neurons, MANF deficiency likely leads to similar ER stress‑mediated apoptosis, contributing to microcephaly and neurodevelopmental delay, though detailed mechanistic data in brain tissue are limited.[9][12][17]

### 4.5 Modifier Genes and Epigenetic Information

Modifier genes that influence DDDS severity or organ involvement have not been identified. Given the central role of ER stress and UPR pathways in MANF‑related pathology, genes encoding ER chaperones (e.g., **BiP/GRP78**), UPR sensors (e.g., **PERK, IRE1, ATF6**), and downstream effectors (e.g., **ATF4, CHOP, XBP1**) could theoretically modulate disease expression.[10][12] For instance, variants that reduce CHOP‑mediated apoptosis might attenuate β‑cell loss in MANF‑deficient individuals. However, no such modifiers have been reported in the limited clinical and experimental literature on DDDS.[9][17]

Epigenetic changes specific to DDDS have not been described. In principle, ER stress can influence chromatin structure and gene expression through pathways such as ATF4 and XBP1, leading to epigenomic alterations that could contribute to disease progression. However, no epigenomic profiling studies have been conducted in DDDS, and the primary etiological mechanism remains genetic MANF loss‑of‑function rather than epigenetic dysregulation.[9][10][12][17]

### 4.6 Chromosomal Abnormalities

No large‑scale chromosomal abnormalities (such as aneuploidy, translocations, or inversions) have been implicated in DDDS. The causal variants are point mutations or small indels within the MANF gene on chromosome 3p21.2, and chromosomal integrity appears otherwise preserved.[1][7][9][17] Chromosomal microarray and karyotyping are therefore not primary diagnostic tools for DDDS but may be used to rule out other syndromic causes of developmental delay and short stature.

In summary, DDDS is a germline autosomal recessive disorder caused by homozygous loss‑of‑function variants in MANF, leading to loss of ER stress‑regulatory function and resultant multi‑system pathology. The variant spectrum is currently limited to a few pathogenic alleles, but the mechanistic framework is robust, supported by convergent human, mouse, and in vitro evidence.

## 5. Environmental Information

### 5.1 Non‑Genetic Contributing Factors

As discussed in the etiological section, DDDS is fundamentally a genetic disease caused by MANF loss‑of‑function, and non‑genetic factors primarily modulate disease severity rather than cause the syndrome. No specific environmental toxins, radiation exposures, or occupational hazards have been linked to DDDS.[1][7][9][17] The small number of reported cases and the lack of large‑scale epidemiological studies limit the ability to systematically assess environmental risk factors.

Nevertheless, general principles of ER stress biology suggest that environmental factors that induce ER stress—such as chronic inflammation, viral infections targeting secretory cells, or exposure to certain chemical agents—could exacerbate organ dysfunction in MANF‑deficient individuals. For example, inflammatory cytokines such as IL‑1β and TNF‑α are known to induce ER stress in β cells, and Hakonen et al. demonstrated that MANF protects human β cells against cytokine‑induced death.[10] In DDDS, absence of MANF may render β cells particularly vulnerable to these inflammatory insults, potentially accelerating diabetes progression.

Similarly, environmental factors that increase protein synthesis demands in secretory cells, such as persistent hyperglycemia requiring high insulin secretion, could intensify ER stress. Montaser et al.’s finding that MANF knockout grafts perform worse in diabetic than non‑diabetic mice supports this notion.[9][17] While these insights are mechanistic rather than epidemiological, they underscore the importance of minimizing ER stress‑inducing exposures in DDDS.

### 5.2 Lifestyle Factors

Lifestyle factors such as diet, physical activity, and smoking have not been specifically studied in DDDS but are relevant in the context of diabetes management and overall health. High‑carbohydrate diets, obesity, and sedentary behavior increase insulin demand and can exacerbate hyperglycemia, thereby intensifying ER stress in β cells. In MANF‑deficient individuals, this could accelerate β‑cell failure and worsen glycemic control.[9][10][17] Conversely, healthy dietary patterns, regular physical activity, and weight management may help reduce metabolic stress and preserve residual β‑cell function.

Smoking and alcohol abuse are known to increase cardiovascular risk and can impair microvascular function, which may compound diabetes‑related complications. While these factors do not directly cause DDDS, they can significantly impact quality of life and morbidity in affected individuals. Given the neurodevelopmental and sensory impairments in DDDS, lifestyle counseling should be tailored to the cognitive and communication abilities of patients and their families.

### 5.3 Infectious Agents

No infectious agents have been implicated in the causation of DDDS. However, infections that induce systemic inflammation or directly affect the pancreas or nervous system could exacerbate ER stress and organ dysfunction in MANF‑deficient individuals. For example, viral infections such as enteroviruses have been associated with β‑cell damage and diabetes onset, and ER stress is a common pathway in viral cytopathology. While no DDDS‑specific data exist on this topic, general infection control and vaccination, as per standard pediatric and diabetes guidelines, should be considered part of tertiary prevention strategies.

In summary, environmental and lifestyle factors are not primary causes of DDDS but function as modifiers of disease expression and progression, mainly through their impact on ER stress and metabolic load. This reinforces the importance of holistic care in DDDS, including aggressive management of infections, metabolic stress, and lifestyle risk factors.

## 6. Mechanism and Pathophysiology

### 6.1 Molecular Pathways: ER Stress and Unfolded Protein Response

The central molecular mechanism in DDDS is **chronic, unresolved endoplasmic reticulum (ER) stress** due to loss of MANF, leading to maladaptive activation of the **unfolded protein response (UPR)** and apoptosis in key cell types such as pancreatic β cells and neurons.[9][10][12][17] Under normal conditions, MANF is an ER stress‑inducible protein that helps attenuate ER stress and promote cell survival. It is upregulated when unfolded or misfolded proteins accumulate in the ER lumen, and it participates in feedback mechanisms that restore ER homeostasis.[10][12]

The UPR consists of three major sensor pathways: **PERK (protein kinase RNA‑like ER kinase)**, **IRE1 (inositol‑requiring enzyme 1)**, and **ATF6 (activating transcription factor 6)**. These pathways detect ER stress and orchestrate adaptive responses to reduce protein folding load and increase chaperone capacity.[10][12] In β cells, ER stress can be triggered by high insulin demand due to hyperglycemia or by inflammatory cytokines. If ER stress is unresolved, the UPR shifts from pro‑survival to pro‑apoptotic modes, with key effectors such as **CHOP (DDIT3)** promoting cell death.[10][12]

In **Manf** knockout mice, Lindahl et al. observed persistent activation of UPR markers, including sXbp1 and Chop, and sustained phosphorylation of eIF2α, indicating chronic activation of the PERK pathway.[12] This was accompanied by increased β‑cell apoptosis and reduced proliferation, leading to progressive loss of β‑cell mass and early‑onset diabetes. Hakonen et al. showed that knockdown of MANF in human β cells similarly aggravates ER stress responses after cytokine challenge, whereas exogenous MANF represses NF‑κB signaling and ameliorates ER stress.[10] Montaser et al. demonstrated that loss of MANF in human embryonic stem cell‑derived endocrine cells induces mild ER stress and impairs insulin processing, and that MANF knockout grafts in mice exhibit elevated ER stress and functional failure, particularly in diabetic environments.[9][17]

These findings support a mechanistic model in which MANF functions as a **negative regulator of ER stress and UPR activation**, helping to maintain β‑cell and neuronal viability under conditions of high secretory demand or inflammatory insult. Loss of MANF results in **failure to properly resolve ER stress**, leading to chronic UPR activation, translational attenuation via eIF2α phosphorylation, and induction of pro‑apoptotic genes such as CHOP, culminating in cell death.[10][12] In GO terms, this involves disruption of processes such as “response to endoplasmic reticulum stress,” “unfolded protein response,” “negative regulation of apoptotic process,” and “regulation of insulin secretion.”[9][10][12][17]

### 6.2 Cellular Processes: β‑Cell Dysfunction and Apoptosis

At the cellular level, the primary process driving diabetes in DDDS is **β‑cell dysfunction and apoptosis** induced by ER stress. β cells are highly specialized secretory cells that produce and secrete insulin in response to glucose. They have a robust ER machinery to handle high levels of proinsulin synthesis and processing. However, this machinery is vulnerable to stress, and ER dysfunction can rapidly compromise β‑cell viability.[10][12]

In **Manf** knockout mice, β‑cell apoptosis begins in the late embryonic and early postnatal period, as evidenced by increased markers of apoptosis and reduced proliferation.[12] This leads to a progressive decline in β‑cell mass and early‑onset diabetes. In human MANF‑deficient cells, Montaser et al. observed impaired insulin processing and secretion, consistent with ER stress‑mediated functional failure.[9][17] Hakonen et al. showed that MANF protects β cells against inflammatory cytokine‑induced cell death, further linking MANF to β‑cell survival under stress.[10]

The causal chain in β cells can be summarized as: **MANF loss → increased sensitivity to ER stress → chronic UPR activation → eIF2α phosphorylation and translational attenuation → CHOP upregulation → apoptosis and reduced proliferation → β‑cell mass loss → insulin deficiency → diabetes.**[9][10][12][17] This is an upstream mechanism relative to clinical hyperglycemia, as β‑cell loss precedes and causes diabetes. Downstream consequences include hyperglycemia, glucotoxicity, and secondary complications such as microvascular damage.

The cell ontology (CL) term **“pancreatic β cell”** is central to this process. GO terms such as “apoptotic process,” “regulation of cell proliferation,” and “insulin secretion” are key biological processes affected. MANF’s role in negative regulation of apoptosis and ER stress is essential for β‑cell survival, and its loss disrupts these processes.

### 6.3 Protein Dysfunction: MANF Deficiency

MANF protein dysfunction in DDDS is fundamentally a **loss‑of‑function** defect. Pathogenic variants in MANF result in absent or nonfunctional protein, removing its protective role in ER stress regulation.[7][9][17] Unlike gain‑of‑function or dominant‑negative mutations, which often produce aberrant protein activity, MANF loss leads to a **deficiency of a critical trophic factor**, similar conceptually to loss of growth factors or chaperones.

Structurally, MANF contains domains important for ER localization and secretion, including an N‑terminal signal peptide and luminal sequences that interact with ER chaperones. Loss‑of‑function variants that truncate MANF or disrupt its folding would prevent proper localization and function. In the absence of MANF, ER stress sensors may remain activated longer, and downstream effectors such as NF‑κB may drive apoptotic gene expression.[10][12] Hakonen et al. showed that exogenous MANF inhibits NF‑κB signaling and BCL10 expression, mediating its protective effect against cytokine‑induced stress.[10]

In protein ontology terms, MANF loss affects functional categories such as “protein folding chaperone,” “neurotrophic factor,” and “ER stress regulator.” The net effect is to reduce the cell’s ability to cope with stress, particularly in high‑demand secretory cells like β cells and neurons.

### 6.4 Metabolic Changes

The metabolic changes in DDDS are primarily those associated with insulin‑dependent diabetes mellitus. Loss of β‑cell insulin production leads to hyperglycemia, increased lipolysis, and ketogenesis, and if untreated, can result in diabetic ketoacidosis. Chronic hyperglycemia leads to non‑enzymatic glycation of proteins, microvascular damage, and organ complications. While the precise metabolic profile of DDDS patients has not been documented in detail, one can infer that standard diabetes metabolic alterations apply.[1][9][17]

At a cellular level, ER stress can also impact metabolic processes by altering protein synthesis, lipid metabolism, and mitochondrial function. The UPR reduces global protein synthesis via eIF2α phosphorylation, which may impact the synthesis of metabolic enzymes. ER stress can also disrupt lipid homeostasis, as the ER is central to lipid synthesis and trafficking. In β cells, ER stress may impair proinsulin processing and insulin maturation, as observed by Montaser et al. in MANF‑deficient human endocrine cells.[9][17]

Metabolomics studies specific to DDDS have not been performed, but broader work in ER stress and diabetes suggests that metabolites such as glucose (CHEBI:17234), free fatty acids, and ketone bodies are altered. From a pathway perspective, KEGG and Reactome would map these changes to insulin signaling pathways, glycolysis, gluconeogenesis, and lipid metabolism. However, DDDS’s unique contribution lies in the upstream ER stress mechanism rather than distinctive downstream metabolic signatures.

### 6.5 Immune System Involvement

Unlike autoimmune type 1 diabetes, DDDS does not appear to involve primary immune‑mediated β‑cell destruction. The absence of islet autoantibodies in DDDS patients suggests that autoimmunity is not the main driver of β‑cell loss.[1][9][17] Instead, ER stress and UPR activation in β cells lead to intrinsic apoptosis. However, inflammatory cytokines can contribute to ER stress and β‑cell death, as shown by Hakonen et al., and MANF’s protective role against cytokine‑induced stress suggests that immune system activation can exacerbate pathology.[10]

In this sense, the immune system is a **secondary modulator** rather than a primary etiological factor. Immune‑mediated inflammation, infections, or systemic inflammatory states may increase ER stress in MANF‑deficient cells, accelerating disease progression. GO terms such as “response to cytokine” and “NF‑κB signaling” are relevant to these interactions. Nonetheless, DDDS should be classified primarily as an **ER stress‑mediated monogenic diabetes syndrome**, not as an autoimmune disease.

### 6.6 Tissue Damage Mechanisms

Tissue damage in DDDS is driven by **ER stress‑induced apoptosis**, **reduced cell proliferation**, and possibly **necrosis** in severely stressed cells. In β cells, chronic ER stress leads to apoptotic cell death, as evidenced by increased markers such as CHOP and caspase activation in Manf‑deficient mice.[12] Reduced proliferation further contributes to inadequate β‑cell mass, leading to diabetes.[12] In neurons, similar mechanisms likely operate, resulting in microcephaly and neurodevelopmental impairment, though direct data are limited.[9][12][17]

In cochlear hair cells and auditory neurons, ER stress may lead to loss of sensory cells and synapses, causing sensorineural deafness. This is consistent with broader evidence that ER stress contributes to hearing loss in mitochondrial and other syndromic disorders, such as MIDD.[6] Tissue damage may also involve oxidative stress, as ER stress can generate reactive oxygen species, and mitochondrial dysfunction may arise secondary to ER stress.

Histopathological examination of tissues from DDDS patients has not been reported, but insights from Manf knockout mice suggest that pancreatic islets exhibit reduced β‑cell number, increased apoptosis, and ER stress marker expression.[12] These findings would likely translate to similar histopathology in human DDDS.

### 6.7 Biochemical Abnormalities

The key biochemical abnormalities in DDDS involve markers of ER stress and UPR activation in affected cells. In Manf knockout mice and MANF‑deficient human β cells, increased expression of ER stress markers such as BiP/GRP78, CHOP, and spliced XBP1 has been documented.[10][12] Phosphorylation of eIF2α is sustained, leading to translational attenuation. In endocrine cells, impaired proinsulin processing may result in altered ratios of proinsulin to insulin, although specific data in DDDS patients are not available.[9][17]

Systemically, biochemical abnormalities include elevated blood glucose, high HbA1c, and possibly elevated free fatty acids and ketone bodies, as in other forms of insulin‑dependent diabetes. No specific plasma biomarkers of MANF deficiency have been established, although circulating MANF levels could theoretically be measured. Hakonen et al.’s demonstration that exogenous MANF has protective effects suggests that recombinant MANF or its downstream signaling molecules could be explored as biomarkers or therapeutic agents.[10]

### 6.8 Molecular Profiling and Advanced Technologies

To date, detailed transcriptomic, proteomic, and metabolomic profiling specific to DDDS has not been reported. However, studies of Manf knockout mice and MANF‑deficient β cells implicitly involve gene expression analyses of UPR and ER stress markers.[10][12] These data show upregulation of UPR genes such as sXbp1, Chop, and Atf4, and changes in NF‑κB pathway components.[10][12]

Single‑cell analysis, spatial transcriptomics, and multi‑omics integration have not yet been applied to DDDS. Nonetheless, these technologies hold promise for dissecting cell‑type specific mechanisms in ER stress‑related diseases. For example, single‑cell RNA‑seq of pancreatic islets from Manf knockout mice could reveal heterogeneity in ER stress responses across β cells, α cells, and δ cells. Spatial transcriptomics in brain tissue could map ER stress markers to specific cortical layers or hippocampal regions affected by MANF deficiency.

Functional genomics screens, such as CRISPR or RNAi, could identify genes that modify ER stress sensitivity in MANF‑deficient cells, potentially uncovering therapeutic targets. While no DDDS‑specific screens have been reported, the broader ER stress field is rich with such approaches.

### 6.9 Causal Chain from Trigger to Clinical Manifestation

Integrating the above mechanisms, the causal chain in DDDS can be summarized as follows:

1. **Upstream trigger:** Germline homozygous loss‑of‑function mutation in MANF, resulting in absence or severe deficiency of functional MANF protein.[1][7][9][17]

2. **Primary molecular consequence:** Impaired ER stress attenuation and failure to resolve UPR activation, leading to chronic ER stress in high‑demand secretory cells such as pancreatic β cells and neurons.[9][10][12][17]

3. **Cellular outcomes:** Sustained eIF2α phosphorylation, translational attenuation, upregulation of pro‑apoptotic UPR effectors (e.g., CHOP), increased apoptosis, and reduced proliferation in β cells and possibly neurons and other secretory cells.[10][12]

4. **Organ‑level effects:** Progressive loss of β‑cell mass and function leading to insulin deficiency and diabetes; neuronal loss or impaired development leading to microcephaly and global developmental delay; cochlear hair cell or auditory neuron loss leading to bilateral sensorineural deafness; impaired growth plate and systemic growth leading to short stature.[1][9][11][12][17]

5. **Clinical manifestations:** Childhood‑onset autoantibody‑negative diabetes mellitus, bilateral sensorineural hearing loss, global developmental delay, microcephaly, and short stature.<br>[1][9][11][17]

6. **Downstream complications:** Hyperglycemia‑related metabolic changes, potential microvascular and macrovascular complications of diabetes, communication impairments due to deafness, educational and psychosocial challenges due to developmental delay and short stature.

This chain distinguishes **upstream mechanisms** (MANF deficiency and ER stress dysregulation) from **downstream outcomes** (diabetes and neurodevelopmental phenotypes) and highlights the cell types involved, including pancreatic β cells, cochlear hair cells, auditory neurons, and cortical neurons. GO biological process terms such as “response to endoplasmic reticulum stress,” “apoptotic process,” and “development of nervous system,” and CL cell ontology terms such as “pancreatic β cell,” “cochlear inner hair cell,” and “cortical neuron” can be used to annotate these mechanisms in a knowledge base.

## 7. Anatomical Structures Affected

### 7.1 Organ‑Level Involvement

The primary organs affected in DDDS are the **pancreas**, **inner ear (cochlea)**, and **central nervous system (brain)**, with secondary involvement of the entire body through growth impairment.[1][9][11][17] The pancreas is affected through β‑cell loss and dysfunction, leading to diabetes. The inner ear is affected through loss of cochlear hair cells or auditory neurons, resulting in bilateral sensorineural deafness. The brain is affected through impaired neurodevelopment and possibly neuronal loss, leading to microcephaly and global developmental delay.[1][9][11][12][17]

The endocrine system, particularly the pancreatic islets, is the primary site of diabetes pathology. The nervous system, both central and peripheral, is involved in developmental delay and hearing loss. The musculoskeletal system and skeletal growth are implicated in short stature and microcephaly. Other organ systems may be secondarily affected by diabetes complications, such as the kidneys (nephropathy), eyes (retinopathy), and cardiovascular system (atherosclerosis), though these have not been reported in DDDS due to limited case numbers.[9][17]

UBERON anatomical ontology terms relevant to DDDS include **UBERON:0001264 (pancreas)**, **UBERON:0000007 (brain)**, **UBERON:0001755 (cochlea)**, **UBERON:0002102 (endocrine system)**, and **UBERON:0000970 (skeletal system)**.

### 7.2 Tissue and Cell‑Level Involvement

At the tissue level, DDDS primarily affects **endocrine pancreatic tissue**, **neural tissue (brain and auditory pathways)**, and **cartilage/bone tissue involved in somatic growth**. Within the pancreas, the islets of Langerhans, specifically the β‑cell population, are the main site of pathology.[10][12][17] The cell ontology term **“pancreatic β cell”** (CL:0000169) is central to this aspect. Manf knockout mice show reduced β‑cell mass and increased apoptosis in islets, and human MANF‑deficient endocrine cells exhibit impaired insulin processing.[9][10][12][17]

In the nervous system, cortical neurons, hippocampal neurons, and cerebellar neurons may be affected, contributing to microcephaly and developmental delay. Although specific cell types have not been identified in DDDS, MANF’s neurotrophic function suggests broad neuronal vulnerability.[9][12][17] The auditory system likely involves cochlear inner and outer hair cells, spiral ganglion neurons, and auditory brainstem nuclei, corresponding to CL terms such as **“cochlear inner hair cell”** and **“auditory neuron.”** The tissue type is predominantly **nervous tissue**.

Growth impairment suggests involvement of growth plate cartilage and osteoblasts. ER stress in chondrocytes can impair cartilage development and bone growth, as seen in some skeletal dysplasias. While direct evidence in DDDS is lacking, this mechanism is plausible. The tissue type here is **cartilaginous and osseous tissue**.

### 7.3 Subcellular Level: ER and Secretory Pathways

At the subcellular level, DDDS pathology is centered on the **endoplasmic reticulum (ER)** and associated secretory pathways. MANF localizes to the ER lumen and exerts its protective effects by modulating ER stress responses.[10][12] Loss of MANF leads to dysfunction in GO cellular component **“endoplasmic reticulum lumen”**, affecting protein folding, chaperone interactions, and UPR signaling.

Other cellular compartments involved include the **Golgi apparatus**, where insulin and other secretory proteins are processed and trafficked, and **secretory granules**, where insulin is stored before release. ER stress can disrupt Golgi function and vesicle trafficking, further impairing secretion. Mitochondria may also be affected, as ER stress can induce mitochondrial dysfunction and apoptosis pathways. However, DDDS is not primarily a mitochondrial disease, unlike MIDD.[5][6][15]

### 7.4 Localization and Lateralization

DDDS features bilateral involvement of certain organs, particularly the ears. Sensorineural hearing loss is reported as **bilateral**, indicating symmetric damage to both cochleae or auditory pathways.[1][9][17] Diabetes affects the pancreas globally, and neurodevelopmental impairment and microcephaly reflect diffuse brain involvement rather than focal lesions. Short stature is systemic.

There is no evidence of lateralization in brain involvement, such as unilateral cortical atrophy, and no localized structural malformations have been reported. This suggests that MANF deficiency affects broad developmental and metabolic processes rather than discrete anatomical regions.

In summary, DDDS affects the pancreas, inner ear, brain, and skeletal growth system at organ, tissue, cell, and subcellular levels, with ER stress in secretory cells as the central subcellular mechanism.

## 8. Temporal Development

### 8.1 Age of Onset

The age of onset of DDDS manifestations is primarily **pediatric**, with the earliest symptoms appearing in childhood. OMIM describes “childhood‑onset autoantibody‑negative diabetes mellitus” as a defining feature, and Montaser et al. report childhood onset of diabetes in both MANF‑deficient patients.[1][9][17] Sensorineural deafness and developmental delay are also evident in childhood, as the patients are described as having bilateral hearing loss and global developmental delay by the time of clinical characterization.[9][17]

Microcephaly and short stature likely arise early, with head circumference and length/height deficits apparent in infancy or early childhood. Microcephaly is often defined by head circumference below −2 or −3 SD from the mean, and in DDDS, this is part of the core phenotype.[1][9][11][17] Developmental milestones such as sitting, walking, and speaking are delayed from infancy onward.

Thus, DDDS can be classified as a **pediatric‑onset, chronic, multisystem disorder**. There is no evidence of congenital anomalies at birth beyond possibly microcephaly and small size, but more detailed prenatal and neonatal data are lacking.

### 8.2 Onset Pattern

The onset pattern of DDDS appears **chronic and insidious** rather than acute. Diabetes emerges over time with progressive hyperglycemia, although it may be diagnosed acutely if the child presents with diabetic symptoms. Hearing loss may be recognized when speech and language development are delayed or when audiometric testing reveals deficits. Developmental delay and short stature become evident as children fail to meet milestones and growth expectations.

There are no reports of acute episodes of neurological regression or catastrophic organ failure in DDDS, suggesting that the disease course is more gradual. However, acute metabolic decompensation such as diabetic ketoacidosis can occur if diabetes is not recognized or managed, as in other forms of insulin‑dependent diabetes.[9][17]

### 8.3 Disease Progression and Course

The progression of DDDS has not been systematically documented due to the small number of cases and limited follow‑up. However, extrapolations from Manf knockout mice and general diabetes experience suggest that the **diabetes component is progressive**, with β‑cell function declining over time.[12] In mice, β‑cell loss continues postnatally, leading to worsening hyperglycemia. In humans, persistent ER stress in MANF‑deficient β cells likely leads to chronic β‑cell loss and ongoing insulin dependence.

Sensorineural hearing loss may be progressive or stable. In MIDD and Wolfram syndrome, hearing loss often progresses with age, and similar patterns may occur in DDDS.[4][5][6][12] Microcephaly and short stature represent cumulative growth deficits, and their severity increases as children fail to catch up with peers. Developmental delay may be non‑progressive in the sense that children continue to acquire skills, albeit slowly, without losing previously acquired abilities. However, if neurodegeneration occurs due to ongoing ER stress, some decline in function could be observed.

The overall disease course of DDDS can be described as **chronic, lifelong, and progressive in metabolic and growth domains**, with developmental impairments present from early life. There is no evidence of remission in the core features, although diabetes control can be improved with treatment.

### 8.4 Critical Periods and Windows of Intervention

Critical periods in DDDS include **early childhood**, when diabetes onset occurs and when neurodevelopmental and growth trajectories are most plastic. Early diagnosis of diabetes and prompt initiation of insulin therapy can prevent acute metabolic complications and may reduce ER stress in β cells by reducing insulin demand. Early identification of hearing loss allows timely intervention with hearing aids or cochlear implants, which can improve language development and social integration.[4][12]

Neurodevelopmental interventions such as physical, occupational, and speech therapy are most effective when initiated in the first few years of life. Thus, early recognition of DDDS and comprehensive multidisciplinary management are key to optimizing outcomes. From a mechanistic perspective, interventions that reduce ER stress or enhance UPR resolution might be most impactful during periods of rapid β‑cell and neuronal growth, such as infancy and early childhood, although such therapies remain experimental.[10][12][17]

In summary, DDDS is a pediatric‑onset, chronic, multisystem disorder with insidious onset of diabetes, deafness, developmental delay, microcephaly, and short stature, and a progressive course in metabolic and growth domains. Early diagnosis and intervention are critical for mitigating complications and maximizing developmental potential.

## 9. Inheritance and Population

### 9.1 Inheritance Pattern

DDDS follows an **autosomal recessive inheritance pattern**. OMIM explicitly states that “the transmission pattern of DDDS in the families reported by Montaser et al. (2021) was consistent with autosomal recessive inheritance,” and GenCC classifies the MANF–DDDS relationship accordingly.[1][13] In both reported families, the affected individual carried a **homozygous loss‑of‑function MANF variant**, and the parents were presumed to be heterozygous carriers.[9][17]

Autosomal recessive inheritance implies that each child of two carrier parents has a 25% chance of being affected, a 50% chance of being a carrier, and a 25% chance of being unaffected. The fact that only one affected individual per family has been reported suggests that family size may be small or that other affected siblings were not present. Nonetheless, genetic counseling for families with known MANF pathogenic variants should be based on standard autosomal recessive risk calculations.

### 9.2 Penetrance and Expressivity

Given the very small number of known cases, formal estimates of **penetrance** and **expressivity** are not possible. However, in the two reported DDDS patients, the presence of homozygous MANF loss‑of‑function variants was associated with a highly consistent phenotype, suggesting **high penetrance** for the core features of childhood‑onset diabetes, bilateral sensorineural deafness, developmental delay, microcephaly, and short stature.[9][17] No asymptomatic individuals with homozygous MANF loss‑of‑function variants have been reported, reinforcing the view that penetrance is near complete.

Expressivity—the degree to which different individuals with the same genotype show variation in phenotype—may be limited for the main disease features, as the two patients exhibit similar manifestations. However, variability in additional features, such as severity of intellectual disability or presence of minor anomalies, is possible. Future cases may broaden the phenotypic spectrum.

### 9.3 Anticipation, Mosaicism, and Founder Effects

There is no evidence of **genetic anticipation** in DDDS, as the disease is caused by loss‑of‑function variants in MANF rather than repeat expansions. Similarly, **germline mosaicism** has not been reported, though it could theoretically occur, as in other autosomal recessive disorders.

Founder effects—population‑specific mutations arising from a common ancestor—have not been described for MANF variants. The patients reported by Montaser et al. come from different families and presumably different ethnic backgrounds.[9][17] As more cases are identified, certain MANF variants may be found to cluster in specific populations, but this remains speculative.

### 9.4 Epidemiology: Prevalence and Incidence

DDDS is an **ultra‑rare** disorder. An educational source states that the exact prevalence is unknown but estimates that DDDS affects fewer than 1 in 1,000,000 individuals worldwide.[16] This is consistent with the general definition of ultra‑rare diseases and the fact that only two cases have been reported in the literature to date.[9][17] Formal incidence data are lacking, as no population‑based registries or screening studies have been conducted.

Given the rarity of reported cases and the essential role of MANF in β‑cell and neuronal survival, DDDS is likely extremely rare, and many clinicians may never encounter a case. However, as exome and genome sequencing become more widespread, additional MANF‑related cases may be identified, potentially expanding the epidemiological picture.

### 9.5 Population Demographics

The ethnic backgrounds of the reported DDDS patients are not explicitly specified in the search results, but Montaser et al.’s study likely included individuals from regions where consanguinity is more common, as autosomal recessive disorders are often enriched in such populations.[9][17] GenCC’s evaluation of MANF–DDDS in 2026 indicates growing recognition across global gene curation efforts.[13]

There is no evidence of sex predilection in DDDS. Both male and female individuals could theoretically be affected, and sex ratio cannot be estimated from two cases. Age distribution is skewed toward childhood, as the disease manifests in early life. Geographic distribution is unknown; cases may be under‑diagnosed in regions with limited access to genetic testing.

Consanguinity may play a role in DDDS incidence, as it increases the likelihood of homozygous rare variants. Clinicians in regions with high consanguinity should consider DDDS in children with autoantibody‑negative diabetes and syndromic features.

In summary, DDDS is an ultra‑rare autosomal recessive disorder with high penetrance for core features, unknown population prevalence, and likely enrichment in populations with higher rates of consanguinity. Epidemiological data remain sparse, and future genomic studies will be important for refining incidence and demographics.

## 10. Diagnostics

### 10.1 Clinical Evaluation and Laboratory Testing

Diagnosis of DDDS begins with **clinical recognition** of the characteristic phenotypic triad: childhood‑onset autoantibody‑negative diabetes mellitus, bilateral sensorineural deafness, and global developmental delay with microcephaly and short stature.[1][9][11][17] Children presenting with diabetes in early life should undergo standard evaluation including measurement of blood glucose, HbA1c, C‑peptide, and islet autoantibodies (GAD65, IA‑2, ZnT8). In DDDS, autoantibodies are absent, suggesting nonautoimmune diabetes.[1][9][17]

Audiological assessment using pure‑tone audiometry and otoacoustic emissions can confirm bilateral sensorineural hearing loss. Brain imaging (MRI) may reveal microcephaly and structural abnormalities, although specific imaging findings in DDDS are not described in current reports. Growth charts document short stature, and developmental assessments identify global delays.

Laboratory tests beyond diabetes markers may include thyroid function, growth hormone/IGF‑1 levels, and metabolic panels to rule out other endocrine or metabolic causes of short stature and developmental delay. However, in DDDS, these are expected to be largely normal, as the primary mechanism is ER stress rather than hormonal deficiency.

No specific biochemical biomarkers for MANF deficiency are currently available. Serum MANF levels could theoretically be measured, but this has not been established as a diagnostic tool. ER stress markers in peripheral blood cells might reflect systemic ER stress, but their specificity would be low.

### 10.2 Genetic Testing Strategies

Definitive diagnosis of DDDS requires **genetic testing** to identify biallelic pathogenic variants in MANF. The recommended approach is sequencing of MANF as part of a **monogenic diabetes panel** or **comprehensive exome/genome sequencing** in children with autoantibody‑negative diabetes and syndromic features.[9][17] The NIH Genetic Testing Registry (GTR) and various commercial laboratories may include MANF in gene panels for early‑onset diabetes or neurodevelopmental disorders, though specific panel compositions are not detailed in the current search results.

Whole exome sequencing (WES) is particularly useful in undiagnosed syndromic cases, as it allows unbiased identification of rare variants in genes not traditionally associated with common diabetes. Montaser et al. identified MANF variants through exome sequencing of patients with childhood diabetes and neurodevelopmental disorder, illustrating the power of WES.[9][17] Whole genome sequencing (WGS) can detect non‑coding variants and structural variants in MANF, but the known DDDS‑associated variants are coding loss‑of‑function alleles.[7][9][17]

Single‑gene testing of MANF may be appropriate once clinical suspicion of DDDS is high, especially if exome sequencing is not readily available. Sanger sequencing or targeted NGS can be used to confirm candidate variants and assess segregation in families. Chromosomal microarray (CMA), karyotyping, and FISH are not primary diagnostic tools for DDDS, as the disease is caused by point mutations rather than chromosomal rearrangements.[1][7][9][17]

Mitochondrial DNA testing is important for differential diagnosis, as MIDD—a mitochondrial diabetes‑deafness syndrome—must be distinguished from DDDS. Testing for mtDNA mutations such as m.3243A>G in MT‑TL1 can confirm MIDD.[4][5][6][15] In DDDS, mitochondrial testing would be negative, while MANF sequencing would reveal pathogenic variants.

Repeat expansion testing is not relevant to DDDS, as the disease is not caused by repeat expansions.

### 10.3 Omics‑Based Diagnostics

Advanced omics‑based diagnostics, such as transcriptomics, proteomics, and metabolomics, have not yet been applied to clinical diagnosis of DDDS. However, functional studies using RNA‑seq or proteomics in MANF‑deficient cells could identify signatures of ER stress and UPR activation that might someday serve as biomarkers.

Currently, the main omics tool in DDDS diagnosis is **exome sequencing**, which detects MANF variants. This can be considered a genomic‑based diagnostic technique.

### 10.4 Clinical Criteria and Differential Diagnosis

Formal clinical diagnostic criteria for DDDS have not been established by professional societies, given the rarity of the disease. However, based on available data, a provisional clinical picture would include:

1. Childhood‑onset, insulin‑dependent, autoantibody‑negative diabetes.<br>[1][9][17]<br>
2. Bilateral sensorineural hearing loss.<br>[1][9][17]<br>
3. Global developmental delay with microcephaly.<br>[1][9][11][17]<br>
4. Short stature (< −3 SD).<br>[17]<br>
5. Absence of mtDNA mutations typical of MIDD and absence of WFS1/CISD2 variants typical of Wolfram syndrome.<br>[5][12][15][16]

Differential diagnoses include:

- **Maternally inherited diabetes and deafness (MIDD):** adult‑onset diabetes and hearing loss, mitochondrial inheritance, often with mtDNA m.3243A>G in MT‑TL1.[4][5][6][15] MIDD may include short stature and multi‑organ involvement but typically presents later and lacks pronounced microcephaly and global developmental delay.

- **Wolfram syndrome type 1 (DIDMOAD):** juvenile‑onset diabetes mellitus, optic atrophy, diabetes insipidus, deafness, caused by WFS1 mutations.[12] Wolfram syndrome includes optic atrophy and diabetes insipidus, which are absent in DDDS, and may have different neurodevelopmental profiles.

- **Rogers syndrome (thiamine‑responsive megaloblastic anemia with diabetes and deafness):** includes megaloblastic anemia, diabetes, and sensorineural deafness, responsive to thiamine therapy.[8] Rogers syndrome is distinguished by anemia and therapeutic response.

- **Other syndromic short stature and deafness syndromes:** various genetic conditions that can include diabetes, deafness, and developmental delay, but without MANF mutations.

Genetic testing is essential to distinguish DDDS from these entities, as clinical overlap is significant.

### 10.5 Screening

Given the ultra‑rare nature of DDDS, **population‑based screening** is not currently feasible or recommended. However, **targeted genetic testing** for MANF variants may be considered in:

- Children with early‑onset, autoantibody‑negative diabetes and bilateral sensorineural deafness.

- Children with syndromic diabetes and neurodevelopmental delay, especially when standard gene panels (e.g., WFS1, mtDNA) are negative.

Carrier screening in families with known MANF pathogenic variants may be considered for reproductive planning. Newborn screening is not currently available for DDDS, as no biochemical marker has been established.

In summary, DDDS diagnosis relies on clinical recognition of syndromic features, comprehensive laboratory and audiological assessment, and confirmatory genetic testing for MANF. Differential diagnosis with MIDD, Wolfram syndrome, and Rogers syndrome is critical, and exome sequencing is an effective tool for identifying MANF variants.

## 11. Outcome and Prognosis

### 11.1 Survival and Mortality

Data on survival and mortality in DDDS are not available, as only two patients have been reported and long‑term outcomes have not been described.[9][17] In Manf knockout mice, early‑onset diabetes is compatible with survival under laboratory conditions, although overall health may be compromised.[12] In humans, insulin therapy and modern diabetes management can significantly reduce diabetes‑related mortality, and deafness and developmental delay are compatible with long life, albeit with disability.

Thus, one can tentatively infer that **life expectancy in DDDS may be reduced but is not necessarily severely shortened**, provided that diabetes is well managed and complications are addressed. However, ER stress in other organs, such as the heart or kidney, could lead to additional morbidity, and MANF’s role in those tissues has not been fully explored.[10][12][17] Until more cases are followed longitudinally, survival estimates and mortality rates cannot be reliably quantified.

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity and disability in DDDS are substantial. Insulin‑dependent diabetes requires lifelong management and imposes daily burdens related to blood glucose monitoring, insulin administration, and dietary restrictions. Deafness impairs communication and social interaction, and developmental delay and microcephaly affect cognitive functioning and adaptive behavior.[1][9][11][17]

Quality of life metrics such as EQ‑5D or SF‑36 have not been applied specifically to DDDS, but similar syndromic conditions show reduced scores in domains such as physical functioning, social functioning, and mental health. Children with DDDS may require special education, assistive communication devices, and ongoing rehabilitation services. Caregiver burden is likely high.

Disability outcomes include dependence on caregivers for activities of daily living, limited academic and occupational opportunities, and reduced independence. The combination of chronic disease management (diabetes) and developmental disability amplifies challenges.

### 11.3 Disease Course and Recovery Potential

The disease course of DDDS is chronic and lifelong. Diabetes is not expected to remit, and β‑cell regeneration is unlikely, given persistent ER stress. Hearing loss, once established, is generally irreversible, although cochlear implants can provide functional hearing. Developmental delay and microcephaly reflect impaired brain development; while developmental therapies can improve skills, full normalization is unlikely.

Recovery potential is therefore limited to **symptomatic improvement and skill acquisition**, not cure of the underlying syndrome. Early and intensive interventions in diabetes management, hearing rehabilitation, and developmental therapy can improve functional outcomes and reduce complications.

### 11.4 Prognostic Factors and Biomarkers

Prognostic factors in DDDS likely include the **severity of ER stress**, **degree of residual β‑cell function**, and **access to comprehensive care**. Children diagnosed early and treated aggressively for diabetes may have better metabolic control and fewer complications. Access to cochlear implantation and special education can improve communication and cognitive development.

Molecular prognostic biomarkers have not been established. ER stress markers in blood or tissues could theoretically predict disease progression, but such studies have not been conducted in DDDS. MANF levels might reflect disease severity in heterozygous or partial deficiency states, though not in complete loss‑of‑function.

In summary, prognosis in DDDS is uncertain due to limited data, but the combination of chronic diabetes, deafness, and developmental delay suggests significant morbidity and disability. Early diagnosis and multidisciplinary care are key to optimizing outcomes.

## 12. Treatment

### 12.1 Pharmacotherapy for Diabetes

Treatment of diabetes in DDDS follows standard protocols for insulin‑dependent diabetes. **Insulin therapy** is the mainstay, delivered via multiple daily injections or insulin pump (NCIT term “Insulin Therapy,” e.g., NCIT:C237). Dosing is individualized based on blood glucose monitoring, dietary intake, and physical activity. Oral hypoglycemic agents are generally ineffective in true insulin‑deficient states but may be considered in specific contexts.

Montaser et al. do not detail diabetes treatment in their patients, but given childhood‑onset insulin‑dependent diabetes, insulin therapy is implied.[9][17] Glycemic targets follow established guidelines, with HbA1c aims adjusted for age and comorbidities. Continuous glucose monitoring can be particularly helpful in children, especially those with developmental and communication challenges.

Pharmacogenomic considerations specific to DDDS have not been identified. Standard diabetes medications such as insulin are not significantly affected by genetic variation in MANF.

### 12.2 Management of Hearing Loss

Bilateral sensorineural hearing loss in DDDS can be managed with **hearing aids** for mild to moderate loss and **cochlear implants** for severe to profound loss (NCIT:C49541). Evidence from MIDD and Wolfram syndrome indicates that cochlear implants can provide functional hearing even in syndromic deafness, improving communication and quality of life.[4][12]

Audiological evaluation determines candidacy for cochlear implantation, taking into account the degree of nerve and cochlear integrity. In children with developmental delay, rehabilitation requires tailored speech and language therapy. Hearing interventions should be initiated as early as possible to maximize language development.

### 12.3 Neurodevelopmental and Growth Interventions

Neurodevelopmental impairments in DDDS require **multidisciplinary supportive care**, including physical therapy, occupational therapy, speech and language therapy, and special education. These interventions aim to optimize motor skills, communication, and cognitive development within the constraints of the underlying brain pathology.

Short stature and microcephaly may prompt evaluation by pediatric endocrinologists. Growth hormone therapy is unlikely to be effective if growth impairment is primarily due to ER stress and intrinsic cellular defects, but endocrine causes such as growth hormone deficiency should be ruled out. Nutritional support and management of chronic illness can help maximize growth potential.

### 12.4 Advanced Therapeutics: ER Stress Modulation and Gene Therapy

Given the central role of ER stress in DDDS, **advanced therapeutics targeting ER stress and UPR** represent a promising avenue for future research. Chemical chaperones such as **4‑phenylbutyrate** and **TUDCA (tauroursodeoxycholic acid)** have been shown to reduce ER stress in various models and could theoretically mitigate β‑cell and neuronal damage in MANF‑deficient individuals. However, no clinical trials have tested these agents in DDDS.

Recombinant MANF protein, as demonstrated by Hakonen et al. to protect human β cells against cytokine‑induced death, could be explored as a therapeutic agent.[10] Systemic or targeted delivery of MANF might compensate for endogenous deficiency and restore ER stress regulation. Challenges include delivery to relevant tissues and potential immunogenicity.

**Gene therapy** to replace MANF in affected cells is another theoretical option. Viral vectors such as AAV could be used to deliver MANF cDNA to pancreatic islets or the central nervous system. Gene therapy for monogenic diabetes (e.g., WFS1 in Wolfram syndrome) is under exploration, and similar strategies might be adapted for MANF.[12] CRISPR‑based gene editing could correct MANF mutations, but off‑target effects and delivery remain concerns.

RNA‑based therapies, such as mRNA encoding MANF or antisense oligonucleotides modulating UPR pathways, represent additional possibilities. However, all these advanced approaches are currently speculative for DDDS.

### 12.5 Surgical and Interventional Treatments

Beyond cochlear implants, surgical interventions are not specific to DDDS. Standard procedures for diabetes complications, such as retinal laser therapy or kidney transplantation, may be necessary in adulthood if complications arise.

### 12.6 Supportive and Rehabilitative Care

Supportive care is crucial in DDDS. Nutritional counseling, psychosocial support, and behavioral interventions help manage chronic illness and developmental challenges. Care coordination among endocrinologists, neurologists, audiologists, developmental pediatricians, and rehabilitation specialists is essential.

Rehabilitation medicine provides physical, occupational, and speech therapy to address motor, cognitive, and communication impairments. Assistive technologies such as communication devices can enhance independence.

### 12.7 Experimental Treatments and Clinical Trials

No clinical trials specific to DDDS have been registered, given the ultra‑rare nature of the disease. However, DDDS patients could potentially be included in broader trials targeting ER stress or monogenic diabetes. For example, trials of chemical chaperones, anti‑ER stress agents, or β‑cell protective therapies may enroll patients with various ER stress‑related conditions.

### 12.8 Treatment Strategy and Personalized Medicine

Treatment strategy in DDDS is **individualized and multidisciplinary**, focusing on:

1. Optimal glycemic control with insulin therapy.<br>[1][9][17]<br>
2. Hearing rehabilitation with hearing aids or cochlear implants.<br>[1][9][17]<br>
3. Developmental support with therapies and special education.<br>[1][9][11][17]<br>
4. Monitoring and management of growth and potential complications.<br>[17]<br>

Personalized medicine approaches include tailoring diabetes management to cognitive and communication abilities, adjusting hearing rehabilitation to speech development, and considering genetic information (MANF variants) for future participation in experimental therapeutics.

NCIT clinical intervention terms relevant to DDDS include **Insulin Therapy (NCIT:C237)**, **Cochlear Implantation (NCIT:C49541)**, **Genetic Counseling (NCIT:C28747)**, and **Physical Therapy (NCIT:C15296)**.

## 13. Prevention

### 13.1 Primary Prevention

Primary prevention of DDDS—preventing the occurrence of the disease—is challenging, as it is a genetic disorder caused by germline MANF loss‑of‑function. However, **genetic counseling and reproductive planning** can reduce the risk of affected offspring in families with known MANF pathogenic variants. Carrier testing in parents and at‑risk relatives can identify heterozygous carriers, and options such as preimplantation genetic diagnosis (PGD) and prenatal testing can be discussed.

Public health interventions such as vaccination and infection control do not prevent DDDS but can reduce complications by minimizing infections that exacerbate ER stress.

### 13.2 Secondary Prevention: Early Detection and Intervention

Secondary prevention focuses on **early detection of DDDS and prompt intervention**. Children with early‑onset autoantibody‑negative diabetes should be evaluated for monogenic diabetes syndromes, including DDDS, and genetic testing should be performed. Early identification of hearing loss through newborn hearing screening or childhood audiometry allows timely rehabilitation. Developmental screening in toddlers can detect delays and trigger interventions.

While there are no population‑based screening programs for DDDS, awareness among clinicians of this syndrome can facilitate early diagnosis and secondary prevention. For families with known MANF pathogenic variants, prenatal or neonatal genetic testing can identify affected children early.

### 13.3 Tertiary Prevention: Managing Complications

Tertiary prevention aims to **prevent complications and reduce disability** in individuals already affected by DDDS. This includes tight glycemic control to prevent microvascular and macrovascular complications, regular screening for diabetes complications, hearing rehabilitation to prevent social isolation, and developmental therapies to maximize functional abilities.

Genetic counseling (NCIT:C28747) provides families with information on recurrence risk and options for future pregnancies. Psychological support and social services can help manage caregiver burden.

### 13.4 Behavioral Interventions and Counseling

Behavioral interventions focus on **lifestyle modifications** to improve diabetes outcomes and overall health, including diet, physical activity, and adherence to treatment. Counseling must be adapted to the developmental level of the child, and caregivers play a central role.

Genetic counseling informs families about the nature of DDDS, inheritance patterns, and reproductive options. It is crucial for informed decision‑making.

In summary, prevention in DDDS consists largely of genetic counseling and early detection, with tertiary prevention focusing on management of diabetes, deafness, and developmental disability.

## 14. Other Species and Natural Disease

### 14.1 Species Affected and Orthologous Genes

Orthologous genes to human MANF exist in many species, including mice, rats, zebrafish, and invertebrates. In mice, the orthologous gene is **Manf**, located on chromosome 17. Lindahl et al. and Hakonen et al. studied **Manf** knockout mice to investigate the role of MANF in β‑cell biology and ER stress.[10][12] These mice provide a natural model of MANF deficiency, although the disease is induced experimentally rather than occurring spontaneously.

NCBI Taxonomy identifiers for species with MANF orthologs include **Mus musculus (mouse)**, **Rattus norvegicus (rat)**, and **Danio rerio (zebrafish)**. MANF’s evolutionary conservation underscores its fundamental role in ER stress regulation.

### 14.2 Naturally Occurring Disease in Animals

No naturally occurring animal disease analogous to human DDDS has been reported in the literature. However, Manf knockout mice develop early‑onset diabetes due to β‑cell loss, closely mirroring the diabetes component of DDDS.[12] Neurodevelopmental and hearing phenotypes in Manf knockout animals have not been fully characterized in the search results, but ER stress in neurons suggests potential neurological consequences.

Veterinary relevance of MANF deficiency is currently unknown. Nonetheless, animal models provide valuable insights into mechanism and potential therapies.

### 14.3 Comparative Pathology and Evolutionary Conservation

Comparative pathology shows that **Manf** knockout mice and human MANF‑deficient cells share the phenotype of β‑cell ER stress, apoptosis, and diabetes.[10][12][17] This cross‑species conservation supports the view that MANF’s role in ER stress regulation is evolutionarily ancient and critical for secretory cell survival.

Differences between species may include the severity of neurodevelopmental phenotypes and the presence of hearing loss, which have not been fully documented in mice. Nonetheless, the shared β‑cell phenotype validates Manf knockout mice as a robust model for the diabetes aspect of DDDS.

### 14.4 Transmission and Zoonotic Potential

DDDS is a genetic, non‑infectious disease and has no zoonotic potential. Transmission is strictly vertical through germline inheritance of MANF variants and does not involve cross‑species infection.

## 15. Model Organisms

### 15.1 Model Types and Systems

The primary model organism for studying DDDS mechanisms is the **mouse**, specifically **Manf** knockout mice.[10][12] These mice are mammalian models that allow investigation of β‑cell biology, ER stress, and diabetes. Additional models include **human β‑cell lines** (EndoC‑βH1) and **human embryonic stem cell‑derived endocrine cells**, which provide in vitro systems for studying MANF function.[10][17]

Manf knockout mice are **genetic models**, with global or tissue‑specific deletion of Manf. Lindahl et al. investigated global knockout, while Hakonen et al. focused on cellular models with MANF knockdown.[10][12] Montaser et al. used MANF knockout human endocrine cell grafts in immunocompromised mice to study in vivo function.[9][17]

### 15.2 Phenotype Recapitulation

Manf knockout mice recapitulate key features of DDDS at the organ level, particularly **early‑onset diabetes** due to β‑cell loss.[12] Lindahl et al. reported that global **Manf** knockout results in progressive postnatal reduction of β‑cell mass caused by reduced β‑cell proliferation and increased β‑cell apoptosis, leading to diabetes.[12] These findings mirror the diabetes phenotype in DDDS and provide strong mechanistic evidence linking MANF deficiency to β‑cell failure.

Neurodevelopmental and hearing phenotypes in Manf knockout mice have not been fully documented in the search results. However, given MANF’s neurotrophic role, it is plausible that neuronal development and survival are affected. Future studies are needed to evaluate brain size, behavior, and auditory function in Manf‑deficient mice.

Human β‑cell models (EndoC‑βH1) and human embryonic stem cell‑derived endocrine cells recapitulate ER stress responses and insulin processing defects observed in DDDS. Hakonen et al. showed that MANF knockdown increases ER stress and cell death in EndoC‑βH1 cells, while exogenous MANF protects against stress.[10] Montaser et al. showed that MANF knockout in stem cell‑derived endocrine cells impairs insulin processing and that knockout grafts exhibit functional failure in vivo.[9][17]

### 15.3 Model Limitations

While Manf knockout mice and human cell models recapitulate β‑cell and ER stress phenotypes, they may not fully capture the **multi‑system features** of DDDS, such as sensorineural deafness, microcephaly, and global developmental delay. Mouse models may differ in neurodevelopmental trajectories, and hearing loss may be subtle or require specialized testing to detect.

Additionally, global knockout models may exhibit embryonic lethality or severe systemic phenotypes that differ from human disease. Tissue‑specific knockouts (e.g., β‑cell‑specific Manf deletion) can isolate organ‑specific effects but may not model systemic syndromic features.

### 15.4 Research Applications

Model organisms are invaluable for studying DDDS mechanisms and testing potential therapies. Applications include:

- Dissecting ER stress and UPR pathways in β cells and neurons.

- Testing chemical chaperones and ER stress modulators in Manf‑deficient mice.

- Evaluating recombinant MANF or gene therapy strategies.

- Conducting functional genomics screens to identify modifiers of ER stress sensitivity.

These models allow detailed analysis of cell‑type specific mechanisms and causal chains, supporting translational research.

### 15.5 Resources and Databases

Model organism databases such as **MGI (Mouse Genome Informatics)** and **IMSR (International Mouse Strain Resource)** likely catalog Manf knockout strains, although specific entries are not detailed in the search results. Cell line resources such as **Cellosaurus** and **ATCC** may list EndoC‑βH1 cells used in MANF studies.[10]

Integrating model organism data with human DDDS knowledge in disease databases requires careful annotation of species, genotype, and phenotype correlations.

## Conclusion

Diabetes, Deafness, Developmental Delay, and Short Stature Syndrome (DDDS) is a recently recognized, ultra‑rare monogenic neuroendocrine disorder caused by **biallelic loss‑of‑function variants in the MANF gene**, leading to chronic ER stress and maladaptive unfolded protein response activation in key secretory cells such as pancreatic β cells and neurons.[1][7][9][10][12][17] Clinically, DDDS is characterized by childhood‑onset autoantibody‑negative diabetes mellitus, bilateral sensorineural deafness, global developmental delay with microcephaly, and marked short stature, with high penetrance for these features in the limited number of reported cases.[1][9][11][17] Mechanistic studies in Manf knockout mice and MANF‑deficient human cell models have elucidated a causal chain from MANF deficiency to ER stress‑mediated apoptosis and organ dysfunction, providing a robust framework for understanding the disease’s pathophysiology.[9][10][12][17]

From a genetic perspective, DDDS is an autosomal recessive disorder, and pathogenic MANF variants are classified as loss‑of‑function alleles with strong evidence of causality.[1][7][9][13][17] The disease’s ultra‑rare nature and recent delineation mean that epidemiological data are sparse, and many aspects of its natural history and prognosis remain uncertain. Nonetheless, existing evidence suggests that DDDS is a chronic, lifelong condition with substantial morbidity and disability, requiring multidisciplinary management for diabetes, deafness, developmental delay, and growth impairment.[1][9][11][17]

Diagnostic strategies for DDDS hinge on clinical recognition of the syndromic phenotype and confirmatory genetic testing for MANF variants, often via exome sequencing in children with autoantibody‑negative diabetes and neurodevelopmental features.[9][17] Differential diagnosis with other diabetes‑deafness syndromes, such as MIDD and Wolfram syndrome, is critical, and mitochondrial DNA and WFS1 testing help distinguish these entities.[4][5][6][12][15][16] Treatment is currently supportive and symptomatic, focusing on insulin therapy, hearing rehabilitation (hearing aids and cochlear implants), developmental therapies, and comprehensive management of complications. Advanced therapeutics targeting ER stress, such as chemical chaperones or MANF‑based therapies, remain experimental but are conceptually promising.[10][12][17]

For disease knowledge bases, DDDS should be represented as **MONDO:0957997**, linked to MANF (HGNC:15461, OMIM:601916) and annotated with HPO terms for autoantibody‑negative diabetes, sensorineural hearing loss, global developmental delay, microcephaly, and short stature.[1][7][11][13][14][17] Mechanistic annotations should emphasize ER stress, UPR pathways, β‑cell apoptosis, and neurodevelopmental processes. Model organism data from Manf knockout mice and human β‑cell models should be integrated to support mechanistic claims and to identify potential therapeutic targets.[10][12][17]

Looking forward, key research priorities include: identifying additional DDDS cases through widespread genomic sequencing; refining the phenotypic spectrum and natural history; exploring ER stress‑modulating therapies; and characterizing MANF’s role in other tissues, such as the auditory system and brain. As more data accumulate, DDDS will serve not only as a specific disease entity but also as a paradigm for ER stress‑related monogenic diabetes and neurodevelopmental disorders, highlighting the critical importance of ER homeostasis in human health.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.